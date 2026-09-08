from __future__ import annotations

from collections import Counter
from copy import deepcopy
from pathlib import Path

from scripts.catalog import load_tools
from tests import test_v022_n1a_access_retry as n1a
from tests.test_migration_provenance import legacy_pointer, reconciliation_rows

EXPECTED_IDS = {
    "mcp-server-kubernetes",
    "floci",
    "opnsense",
    "xcp-ng",
}
ROOT = Path(__file__).resolve().parents[1]
EXPECTED_PRIMARY_SOURCES = {
    "mcp-server-kubernetes": {
        "https://www.npmjs.com/package/mcp-server-kubernetes",
        "https://github.com/Flux159/mcp-server-kubernetes",
        "https://github.com/Flux159/mcp-server-kubernetes#readme",
        "https://github.com/Flux159/mcp-server-kubernetes/blob/main/LICENSE",
        "https://github.com/Flux159/mcp-server-kubernetes/blob/main/package.json",
    },
    "floci": {
        "https://floci.io/aws/",
        "https://floci.io/floci/",
        "https://github.com/floci-io/floci",
        "https://github.com/floci-io/floci/blob/main/LICENSE",
    },
    "opnsense": {
        "https://opnsense.org/opnsense/",
        "https://docs.opnsense.org/",
        "https://github.com/opnsense/core",
        "https://docs.opnsense.org/legal.html",
        "https://opnsense.com/support-overview/",
    },
    "xcp-ng": {
        "https://xcp-ng.org/",
        "https://docs.xcp-ng.org/",
        "https://docs.xcp-ng.org/project/architecture/",
        "https://docs.xcp-ng.org/project/licenses/",
        "https://xcp-ng.com/",
    },
}


def _corrected_tools() -> dict[str, dict]:
    return {tool["id"]: tool for tool in load_tools() if tool["id"] in EXPECTED_IDS}


def test_deferred_correction_wave_has_exact_expected_ids() -> None:
    catalogue = load_tools()
    tools = _corrected_tools()
    counts = Counter(tool["id"] for tool in catalogue)
    assert set(tools) == EXPECTED_IDS
    assert {tool_id: counts[tool_id] for tool_id in EXPECTED_IDS} == {
        tool_id: 1 for tool_id in EXPECTED_IDS
    }
    assert len(catalogue) == 1423


def test_deferred_records_are_verified_active_and_documented() -> None:
    for tool in _corrected_tools().values():
        assert tool["status"] == "active"
        assert tool["needs_review"] is False
        assert tool["verified_on"] == "2026-09-03"
        assert tool["documentation_url"].startswith("https://")
        assert tool["use_when"]
        assert tool["avoid_when"]
        assert tool["deployment_models"]
        assert tool["sources"]
        primary = EXPECTED_PRIMARY_SOURCES[tool["id"]]
        assert all(source.startswith("https://") for source in primary)
        assert primary <= set(tool["sources"])


def test_deferred_records_drop_known_stale_identities() -> None:
    tools = _corrected_tools()
    assert tools["mcp-server-kubernetes"]["repository_url"] != (
        "https://github.com/modelcontextprotocol/servers"
    )
    assert tools["opnsense"]["official_url"] != "https://github.com/opnsense"
    assert tools["xcp-ng"]["official_url"] != "https://github.com/xcp-ng"
    rows = reconciliation_rows()
    for tool_id, tool in tools.items():
        legacy = {legacy_pointer(row) for row in rows if row["canonical_id"] == tool_id}
        assert legacy
        # Exact union rejects stale URLs, unrelated provenance and other schemes.
        assert set(tool["sources"]) == EXPECTED_PRIMARY_SOURCES[tool_id] | legacy
        assert len(tool["sources"]) == len(set(tool["sources"]))


def test_deferred_record_identity_and_licence_semantics() -> None:
    tools = _corrected_tools()

    mcp = tools["mcp-server-kubernetes"]
    assert mcp["official_url"] == (
        "https://www.npmjs.com/package/mcp-server-kubernetes"
    )
    assert mcp["repository_url"] == ("https://github.com/Flux159/mcp-server-kubernetes")
    assert mcp["repository_archived"] is False
    assert mcp["documentation_url"] == (
        "https://github.com/Flux159/mcp-server-kubernetes#readme"
    )
    assert mcp["license_model"] == "oss"
    assert mcp["license_spdx"] == "MIT"
    assert mcp["categories"] == [
        "mlops-llmops-ai-infrastructure",
        "kubernetes-distributions-operations",
    ]
    assert mcp["roles"] == [
        "cloud-engineer",
        "platform-engineer",
        "kubernetes-engineer",
        "mlops-ai-infrastructure-engineer",
    ]
    assert mcp["lifecycle_stages"] == ["deploy", "operate", "secure"]

    floci = tools["floci"]
    assert floci["official_url"] == "https://floci.io/aws/"
    assert floci["repository_url"] == "https://github.com/floci-io/floci"
    assert floci["repository_archived"] is False
    assert floci["documentation_url"] == "https://floci.io/floci/"
    assert floci["license_spdx"] == "MIT"
    assert floci["alternatives"] == ["localstack"]
    assert floci["categories"] == [
        "developer-experience-local-environments",
        "cloud-platforms-management",
    ]
    assert floci["roles"] == [
        "cloud-engineer",
        "devops-engineer",
        "developer-experience-engineer",
    ]
    assert floci["lifecycle_stages"] == ["develop", "test"]

    opnsense = tools["opnsense"]
    assert opnsense["official_url"] == "https://opnsense.org/opnsense/"
    assert opnsense["repository_url"] == "https://github.com/opnsense/core"
    assert opnsense["repository_archived"] is False
    assert opnsense["documentation_url"] == "https://docs.opnsense.org/"
    assert opnsense["license_model"] == "oss"
    assert "license_spdx" not in opnsense
    assert opnsense["commercial_offering"] is True
    assert opnsense["alternatives"] == ["pfsense"]
    assert opnsense["categories"] == ["application-cloud-security"]
    assert opnsense["roles"] == [
        "devsecops-engineer",
        "cloud-security-engineer",
        "infrastructure-systems-engineer",
    ]
    assert opnsense["lifecycle_stages"] == ["deploy", "secure", "operate"]

    xcp_ng = tools["xcp-ng"]
    assert xcp_ng["official_url"] == "https://xcp-ng.org/"
    assert xcp_ng["documentation_url"] == "https://docs.xcp-ng.org/"
    assert "repository_url" not in xcp_ng
    assert xcp_ng["license_model"] == "oss"
    assert "license_spdx" not in xcp_ng
    assert xcp_ng["commercial_offering"] is True
    assert xcp_ng["alternatives"] == ["proxmox-virtual-environment-ve"]
    assert xcp_ng["categories"] == ["virtualization-bare-metal-homelab"]
    assert xcp_ng["roles"] == [
        "devops-engineer",
        "platform-engineer",
        "infrastructure-systems-engineer",
    ]
    assert xcp_ng["lifecycle_stages"] == ["deploy", "operate"]


def test_n1a_supersession_is_exact_and_does_not_weaken_other_guards() -> None:
    assert {
        ("mcp-server-kubernetes", "repository_url"),
        ("mcp-server-kubernetes", "license_spdx"),
        ("mcp-server-kubernetes", "status"),
        ("mcp-server-kubernetes", "needs_review"),
    } == n1a.N1A_CURRENT_STATE_SUPERSESSIONS

    accepted = n1a._records_at(n1a.N1A_RESULT_SHA)
    future = deepcopy(accepted)
    future["mcp-server-kubernetes"][1]["repository_url"] = (
        "https://github.com/Flux159/mcp-server-kubernetes"
    )
    future["mcp-server-kubernetes"][1]["license_spdx"] = "MIT"
    future["mcp-server-kubernetes"][1]["status"] = "active"
    future["mcp-server-kubernetes"][1]["needs_review"] = False
    n1a._assert_current_n1a_persistence(future, accepted)

    future["mcp-server-kubernetes"][1]["license_model"] = "commercial"
    try:
        n1a._assert_current_n1a_persistence(future, accepted)
        raise AssertionError("An unrelated protected-field change must still fail")
    except AssertionError as exc:
        assert "license_model" in str(exc)

    unrelated = deepcopy(accepted)
    unrelated["ansible-lint"][1]["repository_url"] = "https://example.invalid/drift"
    try:
        n1a._assert_current_n1a_persistence(unrelated, accepted)
        raise AssertionError("An unrelated N1a record must remain protected")
    except AssertionError as exc:
        assert "ansible-lint" in str(exc)
        assert "repository_url" in str(exc)


def test_n1a_historical_accounting_remains_exact() -> None:
    assert len(n1a.EXPECTED_IDS) == 20
    assert len(n1a.EXPECTED_WORK_ITEMS) == 25
    assert len(n1a.EXPECTED_CHANGED_FIELDS) == 2
    assert ("mcp-server-kubernetes", "official_url") in n1a.EXPECTED_WORK_ITEMS
    assert all(tool_id == "ansible-lint" for tool_id, _ in n1a.EXPECTED_CHANGED_FIELDS)


def test_generated_category_docs_reflect_corrected_identities() -> None:
    expected_links = {
        "docs/categories/mlops-llmops-ai-infrastructure.md": (
            "### mcp-server-kubernetes",
            "https://github.com/Flux159/mcp-server-kubernetes",
        ),
        "docs/categories/developer-experience-local-environments.md": (
            "### Floci",
            "https://floci.io/aws/",
        ),
        "docs/categories/application-cloud-security.md": (
            "### OPNsense",
            "https://opnsense.org/opnsense/",
        ),
        "docs/categories/virtualization-bare-metal-homelab.md": (
            "### XCP-ng",
            "https://xcp-ng.org/",
        ),
    }
    for relative_path, expected in expected_links.items():
        text = (ROOT / relative_path).read_text(encoding="utf-8")
        assert all(value in text for value in expected)
