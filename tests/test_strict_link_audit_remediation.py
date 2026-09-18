from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

from scripts.catalog import load_tools
from scripts.check_links import LinkResult, assess_strict_results, load_baseline

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_IDS = {"milvus", "systemd", "wozz"}
BASELINE_NORMALIZED_SHA256 = (
    "9d91d5960126a2343a86c934e07eea0827915fa15c2171ba9331432e682164aa"
)
REVIEWED_BLOCKERS = {
    "https://github.com/hoji-ai/hoji",
    "https://github.com/ophircloud/DevOps-Projects",
    "https://hub.docker.com/r/soosio/dast",
    "https://kubeflame.github.io",
    "https://www.opentext.com/products/static-application-security-testing",
    "https://www.yotascale.com",
}
ORIGINAL_UNBASELINED_BLOCKERS = {
    "https://milvus.io",
    "https://milvus.io/docs",
    "https://systemd.io/COMMAND_LINE/",
    "https://wozz.io/index.html",
}
WOZZ_PRIMARY_SOURCES = {
    "https://github.com/WozzHQ/wozz",
    "https://github.com/WozzHQ/wozz#readme",
    "https://github.com/WozzHQ/wozz/blob/main/LICENSE",
}
WOZZ_LEGACY_SOURCES = {
    "legacy:devopstools_final.md#L637",
    "legacy:4_Kubernetes-Containers/README.md#L141",
}


def _tools() -> dict[str, dict]:
    return {tool["id"]: tool for tool in load_tools() if tool["id"] in EXPECTED_IDS}


def test_remediation_scope_and_canonical_count() -> None:
    catalogue = load_tools()
    counts = Counter(tool["id"] for tool in catalogue)
    assert set(_tools()) == EXPECTED_IDS
    assert {tool_id: counts[tool_id] for tool_id in EXPECTED_IDS} == {
        tool_id: 1 for tool_id in EXPECTED_IDS
    }
    assert len(catalogue) == 1423


def test_corrected_link_identities_are_exact() -> None:
    tools = _tools()
    milvus = tools["milvus"]
    assert milvus["official_url"] == "https://milvus.io"
    assert milvus["documentation_url"] == "https://milvus.io/docs"
    assert milvus["repository_url"] == "https://github.com/milvus-io/milvus"

    systemd = tools["systemd"]
    assert systemd["documentation_url"] == (
        "https://www.freedesktop.org/software/systemd/man/latest/"
    )
    assert systemd["verified_on"] == "2026-09-03"
    assert "https://systemd.io/COMMAND_LINE/" not in systemd.values()

    wozz = tools["wozz"]
    assert wozz["official_url"] == "https://github.com/WozzHQ/wozz"
    assert wozz["repository_url"] == "https://github.com/WozzHQ/wozz"
    assert wozz["documentation_url"] == "https://github.com/WozzHQ/wozz#readme"
    assert wozz["repository_archived"] is False
    assert wozz["license_model"] == "oss"
    assert wozz["license_spdx"] == "MIT"
    assert wozz["status"] == "active"
    assert wozz["needs_review"] is False
    active_urls = {
        wozz["official_url"],
        wozz["repository_url"],
        wozz["documentation_url"],
    }
    assert "https://wozz.io/index.html" not in active_urls
    assert set(wozz["sources"]) == WOZZ_PRIMARY_SOURCES | WOZZ_LEGACY_SOURCES


def test_wozz_sources_preserve_migration_provenance() -> None:
    reconciliation_path = ROOT / "migration" / "reconciliation.csv"
    with reconciliation_path.open(encoding="utf-8", newline="") as handle:
        rows = [row for row in csv.DictReader(handle) if row["canonical_id"] == "wozz"]

    assert {(row["source_file"], row["line"], row["disposition"]) for row in rows} == {
        ("devopstools_final.md", "637", "kept"),
        ("4_Kubernetes-Containers/README.md", "141", "merged"),
    }
    migration_sources = {f"legacy:{row['source_file']}#L{row['line']}" for row in rows}
    assert migration_sources == WOZZ_LEGACY_SOURCES
    assert migration_sources <= set(_tools()["wozz"]["sources"])


def test_original_unbaselined_blocker_values_are_accounted_for() -> None:
    tools = _tools()
    current_urls = {
        str(tool[field])
        for tool in tools.values()
        for field in ("official_url", "repository_url", "documentation_url")
        if tool.get(field)
    }
    assert ORIGINAL_UNBASELINED_BLOCKERS & current_urls == {
        "https://milvus.io",
        "https://milvus.io/docs",
    }
    assert ORIGINAL_UNBASELINED_BLOCKERS.isdisjoint(REVIEWED_BLOCKERS)


def test_reviewed_blocker_baseline_is_unchanged() -> None:
    path = ROOT / "config" / "link-audit-baseline.json"
    normalized_bytes = path.read_text(encoding="utf-8").encode("utf-8")
    assert hashlib.sha256(normalized_bytes).hexdigest() == BASELINE_NORMALIZED_SHA256
    baseline = load_baseline(path)
    assert set(baseline) == REVIEWED_BLOCKERS
    assert len(baseline) == 6


def test_generated_docs_reflect_corrected_links() -> None:
    milvus_doc = (ROOT / "docs/categories/mlops-llmops-ai-infrastructure.md").read_text(
        encoding="utf-8"
    )
    systemd_doc = (ROOT / "docs/categories/foundations-linux-scripting.md").read_text(
        encoding="utf-8"
    )
    wozz_doc = (
        ROOT / "docs/categories/kubernetes-networking-storage-addons.md"
    ).read_text(encoding="utf-8")
    assert "https://milvus.io/docs" in milvus_doc
    assert "https://www.freedesktop.org/software/systemd/man/latest/" in systemd_doc
    assert "https://systemd.io/COMMAND_LINE/" not in systemd_doc
    assert "https://github.com/WozzHQ/wozz" in wozz_doc
    assert "https://wozz.io/index.html" not in wozz_doc


def test_strict_assessment_still_fails_for_genuine_new_blocker() -> None:
    blocker = LinkResult(
        url="https://new-unreviewed.example",
        classification="tls-failure",
        status=None,
        final_url=None,
        redirect_codes=(),
        attempts=1,
        error="certificate failure",
        checked_at="2026-09-03T00:00:00+00:00",
    )
    assessment = assess_strict_results([blocker], {})
    assert assessment.passed is False
    assert assessment.blocking_new == (blocker,)


def test_tracked_report_baseline_remains_self_consistent() -> None:
    payload = json.loads(
        (ROOT / "reports/link-report.json").read_text(encoding="utf-8")
    )
    strict_counts = Counter(item["strict_status"] for item in payload["results"])
    assert payload["strict"]["blocking_known"] == strict_counts["blocking-known"]
    assert payload["strict"]["blocking_new"] == strict_counts["blocking-new"]
