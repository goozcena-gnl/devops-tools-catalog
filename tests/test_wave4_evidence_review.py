"""Parent-product boundaries established by the October 2026 evidence review."""

import pytest

from scripts.catalog import load_tools


@pytest.fixture(scope="module")
def catalogue() -> dict[str, dict]:
    return {tool["id"]: tool for tool in load_tools()}


@pytest.mark.parametrize(
    "tool_id",
    [
        "orbstack",
        "octopus-deploy",
        "mergify",
        "palo-alto-cortex-cloud",
        "manageengine-network-configuration-manager",
        "gremlin",
        "komodor",
        "morpheus-data",
    ],
)
def test_commercial_parent_does_not_inherit_component_licences(
    catalogue, tool_id
) -> None:
    tool = catalogue[tool_id]
    assert tool["license_model"] == "commercial"
    assert tool["commercial_offering"] is True
    assert "license_spdx" not in tool
    assert "repository_url" not in tool
    assert "repository_archived" not in tool


@pytest.mark.parametrize("tool_id", ["nvidia-dgx-cloud", "moogsoft"])
def test_unresolved_parent_identity_retains_review(catalogue, tool_id) -> None:
    tool = catalogue[tool_id]
    assert tool["needs_review"] is True
    assert tool["status"] == "needs-review"
    assert tool["license_model"] == "unknown"
    assert "license_spdx" not in tool
    assert "repository_url" not in tool
    assert tool["documentation_url"] in tool["sources"]


def test_hpe_identity_keeps_stable_id_and_software_deployment(catalogue) -> None:
    tool = catalogue["morpheus-data"]
    assert "HPE" in tool["name"]
    assert tool["official_url"].startswith("https://www.hpe.com/")
    assert tool["deployment_models"] == ["self-hosted"]
    assert "Enterprise" in tool["summary"]
    assert any(source.startswith("legacy:") for source in tool["sources"])
    assert "https://developer.hpe.com/platform/morpheus/home/" in tool["sources"]


def test_cortex_licence_evidence_stays_with_cloud_product(catalogue) -> None:
    tool = catalogue["palo-alto-cortex-cloud"]
    assert "cortex-cloud-docs" in tool["documentation_url"]
    assert any(
        "/cortex-cloud-runtime-security/" in source
        and source.endswith("/understand-license-plans")
        for source in tool["sources"]
    )
    assert not any("/cortex-xsiam/" in source for source in tool["sources"])


def test_octopus_is_classified_for_release_and_deployment(catalogue) -> None:
    tool = catalogue["octopus-deploy"]
    assert "cd-gitops-release-promotion" in tool["categories"]
    assert {"release", "deploy"} <= set(tool["lifecycle_stages"])
    assert {"hosted-saas", "self-hosted"} <= set(tool["deployment_models"])


def test_komodor_distinguishes_control_plane_from_agent_workers(catalogue) -> None:
    tool = catalogue["komodor"]
    assert "https://docs.komodor.com/get-started/deployment-methods" in tool["sources"]
    boundary = " ".join(tool["avoid_when"]).lower()
    assert "control plane" in boundary
    assert "beta" in boundary
    assert "agreement" in boundary
