from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path

import pytest

from scripts.catalog import load_tools, load_yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/maintenance/2026-09-08-wave4-candidate-reconciliation.csv"
COLUMNS = [
    "input_index",
    "input_label",
    "input_url",
    "normalized_input_url",
    "canonical_name",
    "canonical_official_url",
    "canonical_repository_url",
    "existing_catalog_id",
    "decision",
    "resulting_catalog_id",
    "duplicate_of_input_index",
    "categories",
    "license_model",
    "license_spdx",
    "status",
    "needs_review",
    "primary_evidence",
    "notes",
]
DECISIONS = {
    "ADD",
    "UPDATE_EXISTING",
    "ALREADY_PRESENT_NO_CHANGE",
    "ALIAS_ONLY",
    "SKIP_DUPLICATE",
    "SKIP_OUT_OF_SCOPE",
    "HISTORICAL_OR_ARCHIVED",
    "NEEDS_REVIEW",
}
COUNTS = {
    "ADD": 117,
    "UPDATE_EXISTING": 11,
    "SKIP_DUPLICATE": 7,
    "SKIP_OUT_OF_SCOPE": 15,
    "NEEDS_REVIEW": 2,
}
DUPLICATES = {24: 23, 43: 8, 48: 47, 52: 51, 59: 58, 141: 129, 142: 121}


@pytest.fixture(scope="module")
def rows() -> dict[int, dict[str, str]]:
    with LEDGER.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        assert reader.fieldnames == COLUMNS
        loaded = list(reader)
    assert [int(row["input_index"]) for row in loaded] == list(range(1, 153))
    return {int(row["input_index"]): row for row in loaded}


@pytest.fixture(scope="module")
def catalogue() -> dict[str, dict]:
    tools = load_tools(ROOT)
    assert len(tools) == len({tool["id"] for tool in tools})
    return {tool["id"]: tool for tool in tools}


def test_wave4_preserves_all_original_labels_and_urls(rows) -> None:
    submitted = [
        (row["input_index"], row["input_label"], row["input_url"])
        for row in rows.values()
    ]
    encoded = json.dumps(submitted, ensure_ascii=False, separators=(",", ":")).encode()
    assert hashlib.sha256(encoded).hexdigest() == (
        "e0c6029221ff465305800cbe8d9f910c23adb14ab4dc6c491de110b12e6241e9"
    )


def test_wave4_dispositions_account_for_every_occurrence(rows) -> None:
    counts = Counter(row["decision"] for row in rows.values())
    assert set(counts) <= DECISIONS
    assert counts == COUNTS
    assert sum(counts.values()) == 152


def test_wave4_additions_and_baseline_ids_are_preserved(rows, catalogue) -> None:
    added = [
        row["resulting_catalog_id"] for row in rows.values() if row["decision"] == "ADD"
    ]
    assert len(added) == len(set(added)) == 117
    assert set(added) <= set(catalogue)
    assert len(catalogue) == 1306 + len(added) == 1423
    baseline_ids = "\n".join(sorted(set(catalogue) - set(added))).encode()
    assert hashlib.sha256(baseline_ids).hexdigest() == (
        "be35d3c8a5fb8ab71b126e8dc7c52ab1b9b0b19412cd42e3cf3566e521f1565a"
    )


def test_wave4_updates_preserve_existing_identity(rows, catalogue) -> None:
    updated = [row for row in rows.values() if row["decision"] == "UPDATE_EXISTING"]
    assert len(updated) == 11
    assert len({row["existing_catalog_id"] for row in updated}) == 11
    for row in updated:
        assert row["existing_catalog_id"] == row["resulting_catalog_id"]
        assert row["existing_catalog_id"] in catalogue
        assert "Fields changed:" in row["notes"]
        assert row["primary_evidence"]


@pytest.mark.parametrize(("duplicate", "authority"), DUPLICATES.items())
def test_wave4_duplicate_identity_boundaries(rows, duplicate, authority) -> None:
    assert 1 <= authority < duplicate <= 152
    assert rows[duplicate]["decision"] == "SKIP_DUPLICATE"
    assert rows[duplicate]["duplicate_of_input_index"] == str(authority)
    assert (
        rows[duplicate]["resulting_catalog_id"]
        == rows[authority]["resulting_catalog_id"]
    )
    assert rows[authority]["decision"] in {"ADD", "UPDATE_EXISTING"}


def test_wave4_ledger_matches_canonical_metadata(rows, catalogue) -> None:
    for row in rows.values():
        if not row["resulting_catalog_id"]:
            continue
        tool = catalogue[row["resulting_catalog_id"]]
        for column, field in (
            ("canonical_name", "name"),
            ("canonical_official_url", "official_url"),
            ("canonical_repository_url", "repository_url"),
            ("license_model", "license_model"),
            ("license_spdx", "license_spdx"),
            ("status", "status"),
        ):
            assert row[column] == tool.get(field, ""), (row["input_index"], column)
        assert row["categories"].split(";") == tool["categories"]
        assert row["needs_review"] == str(tool["needs_review"]).lower()


def test_wave4_kubelogin_upstreams_remain_distinct(rows, catalogue) -> None:
    azure = catalogue[rows[4]["resulting_catalog_id"]]
    oidc = catalogue[rows[5]["resulting_catalog_id"]]
    assert azure["id"] != oidc["id"]
    assert azure["repository_url"] == "https://github.com/Azure/kubelogin"
    assert oidc["repository_url"] == "https://github.com/int128/kubelogin"


def test_wave4_feature_and_product_family_boundaries(rows, catalogue) -> None:
    assert rows[20]["resulting_catalog_id"] == "bitbucket-pipelines"
    assert "bitbucket" in catalogue
    assert rows[76]["resulting_catalog_id"] == "kong"
    assert "kong-gateway" not in catalogue
    assert rows[85]["resulting_catalog_id"] == "agentsroom"
    assert rows[86]["resulting_catalog_id"] == "cursor"
    assert "agentsroom-teams" not in catalogue
    assert "cursor-3-0" not in catalogue
    assert (
        rows[87]["canonical_repository_url"]
        == "https://github.com/superset-sh/superset"
    )
    assert rows[87]["canonical_name"] != "Apache Superset"
    assert rows[45]["license_model"] == "documentation"


def test_wave4_licences_do_not_cross_product_boundaries(rows, catalogue) -> None:
    assert rows[22]["license_model"] == "oss"
    assert rows[22]["license_spdx"] == "AGPL-3.0-only"
    assert rows[49]["license_model"] == "commercial"
    assert not rows[49]["license_spdx"]
    assert rows[50]["license_spdx"] == "MIT"
    assert rows[49]["resulting_catalog_id"] != rows[50]["resulting_catalog_id"]
    assert rows[31]["license_model"] == "open-core"
    assert rows[31]["license_spdx"] == "MIT"
    assert rows[77]["license_model"] == "commercial"
    assert rows[78]["license_model"] == "source-available"
    assert rows[83]["license_model"] == rows[102]["license_model"] == "open-core"
    assert rows[126]["license_spdx"] == "GPL-3.0-only"
    assert (
        catalogue["varnish-cache"]["repository_url"]
        == "https://github.com/varnish/varnish"
    )
    assert catalogue["varnish-cache"]["repository_archived"] is False


def test_wave4_container_runtimes_cover_operations(catalogue) -> None:
    for tool_id in ("youki", "crun"):
        assert "operate" in catalogue[tool_id]["lifecycle_stages"]
        assert "release" not in catalogue[tool_id]["lifecycle_stages"]


def test_wave4_commercial_support_is_separate_from_source_licence(catalogue) -> None:
    oracle = catalogue["oracle-linux"]
    assert oracle["license_model"] == "oss"
    assert oracle["commercial_offering"] is True
    superset = catalogue["superset-agent-workspace"]
    assert superset["license_model"] == "source-available"
    assert superset["license_spdx"] == "Elastic-2.0"
    assert superset["commercial_offering"] is True


def test_wave4_uncertain_candidates_are_held_without_new_records(
    rows, catalogue
) -> None:
    for index in (98, 150):
        assert rows[index]["decision"] == "NEEDS_REVIEW"
        assert rows[index]["needs_review"] == "true"
        assert not rows[index]["resulting_catalog_id"]
    assert rows[98]["license_model"] == "commercial"
    assert rows[150]["license_model"] == "unknown"
    assert "portkube" not in catalogue
    assert "kubiya" not in catalogue


def test_wave4_maturity_and_taxonomy_are_separate_from_review(rows, catalogue) -> None:
    for index in (15, 21, 28, 40, 56, 113):
        tool = catalogue[rows[index]["resulting_catalog_id"]]
        assert tool["maturity"] == "experimental"
        assert tool["status"] == "active"
        assert tool["needs_review"] is False
    assert catalogue["agent-skills"]["categories"] == [
        "developer-experience-local-environments"
    ]
    assert catalogue["llmrouter"]["categories"] == ["mlops-llmops-ai-infrastructure"]
    assert rows[109]["decision"] == rows[111]["decision"] == "SKIP_OUT_OF_SCOPE"


def test_wave4_tracking_urls_and_ambiguities_do_not_create_aliases(rows) -> None:
    for row in rows.values():
        assert "utm_" not in row["normalized_input_url"]
    aliases = load_yaml(ROOT / "config/import-overrides.yaml")["url_aliases"]
    assert aliases[rows[43]["input_url"]] == "https://almalinux.org/"
    assert (
        aliases[rows[93]["input_url"]]
        == "https://github.com/IvanJosipovic/ACR-SyncTool"
    )
    assert rows[87]["input_url"] not in aliases
    assert rows[121]["input_url"] not in aliases
    assert rows[129]["input_url"] not in aliases


def test_wave4_altcha_keeps_usable_core_and_commercial_boundary(catalogue) -> None:
    tool = catalogue["altcha"]
    assert tool["repository_url"] == "https://github.com/altcha-org/altcha"
    assert tool["repository_archived"] is False
    assert tool["commercial_offering"] is True
    assert (
        "https://github.com/altcha-org/altcha/blob/main/LICENSE.txt" in tool["sources"]
    )
    assert "server-side verification" in " ".join(tool["use_when"])
    assert "commercial Sentinel and Cloud" in " ".join(tool["avoid_when"])


def test_wave4_steampipe_source_does_not_relicense_vendor_binaries(catalogue) -> None:
    tool = catalogue["steampipe"]
    assert tool["repository_url"] == "https://github.com/turbot/steampipe"
    assert tool["commercial_offering"] is True
    assert "AGPL source distribution" in " ".join(tool["use_when"])
    assert "Turbot binaries and services" in " ".join(tool["avoid_when"])
    assert "https://turbot.com/open-source" in tool["sources"]


def test_wave4_authoritative_licence_grants_are_recorded(catalogue) -> None:
    expected = {
        "lightpanda": "AGPL-3.0-or-later",
        "mariadb-server": "GPL-2.0-only",
        "crun": "GPL-2.0-or-later",
        "sniffglue": "GPL-3.0-or-later",
        "kftray": "GPL-3.0-only",
        "sofka": "MIT OR Apache-2.0",
        "openobserve": "AGPL-3.0-only",
    }
    for tool_id, spdx in expected.items():
        assert catalogue[tool_id]["license_spdx"] == spdx


def test_wave4_platform_generation_and_function_host_scope(catalogue, rows) -> None:
    generator = catalogue["kubernetes-crd-model-gen"]
    assert "CLI" in generator["summary"]
    sdk = catalogue["crossplane-function-sdk-csharp"]
    assert "gRPC function host" in sdk["summary"]
    assert sdk["maturity"] == "emerging"
    assert sdk["status"] == "active"
    assert rows[149]["decision"] == rows[151]["decision"] == "SKIP_OUT_OF_SCOPE"
