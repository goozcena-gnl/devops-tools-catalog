from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

from scripts.catalog import load_tools
from scripts.check_links import LinkResult, assess_strict_results, load_baseline

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_IDS = {"milvus", "systemd", "wozz"}
BASELINE_SHA256 = "ea610c49fe7cf71299eb11610574cf623198df3345b4fdb294d9e3748743289c"
REVIEWED_BLOCKERS = {
    "https://github.com/gremlin-io/gremlin",
    "https://github.com/hoji-ai/hoji",
    "https://github.com/komodorio/komodor",
    "https://github.com/ophircloud/DevOps-Projects",
    "https://github.com/usual2970/certmate",
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


def _tools() -> dict[str, dict]:
    return {tool["id"]: tool for tool in load_tools() if tool["id"] in EXPECTED_IDS}


def test_remediation_scope_and_canonical_count() -> None:
    catalogue = load_tools()
    counts = Counter(tool["id"] for tool in catalogue)
    assert set(_tools()) == EXPECTED_IDS
    assert {tool_id: counts[tool_id] for tool_id in EXPECTED_IDS} == {
        tool_id: 1 for tool_id in EXPECTED_IDS
    }
    assert len(catalogue) == 1305


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
    assert "https://wozz.io/index.html" not in wozz.values()
    assert all(source.startswith("https://") for source in wozz["sources"])


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


def test_reviewed_blocker_baseline_is_byte_for_byte_unchanged() -> None:
    path = ROOT / "config" / "link-audit-baseline.json"
    assert hashlib.sha256(path.read_bytes()).hexdigest() == BASELINE_SHA256
    baseline = load_baseline(path)
    assert set(baseline) == REVIEWED_BLOCKERS
    assert len(baseline) == 9


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
