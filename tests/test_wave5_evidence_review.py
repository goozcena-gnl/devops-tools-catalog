"""Durable product and lifecycle boundaries from Evidence Review Wave 5."""

import pytest

from scripts.catalog import load_tools


@pytest.fixture(scope="module")
def catalogue() -> dict[str, dict]:
    return {tool["id"]: tool for tool in load_tools()}


@pytest.mark.parametrize("tool_id", ["teamcity", "spacelift", "cloudbees"])
def test_commercial_parent_does_not_inherit_component_oss_licences(
    catalogue, tool_id
) -> None:
    tool = catalogue[tool_id]
    assert tool["license_model"] == "commercial"
    assert tool["commercial_offering"] is True
    assert "license_spdx" not in tool
    assert "repository_url" not in tool
    assert "repository_archived" not in tool


def test_nexus_core_repository_does_not_license_the_whole_distribution(
    catalogue,
) -> None:
    tool = catalogue["nexus-repository"]
    assert tool["repository_url"] == "https://github.com/sonatype/nexus-public"
    assert tool["license_model"] == "open-core"
    assert "license_spdx" not in tool
    assert (
        "https://www.sonatype.com/dnt/usage/community-edition-eula" in tool["sources"]
    )
    assert {"self-hosted", "hosted-saas"} <= set(tool["deployment_models"])


@pytest.mark.parametrize(
    ("tool_id", "repository", "spdx"),
    [
        ("k0rdent", "k0rdent/k0rdent", "Apache-2.0"),
        ("helm", "helm/helm", "Apache-2.0"),
        ("tekton", "tektoncd/pipeline", "Apache-2.0"),
        ("terragrunt", "gruntwork-io/terragrunt", "MIT"),
        ("cdk8s", "cdk8s-team/cdk8s", "Apache-2.0"),
        ("spinnaker", "spinnaker/spinnaker", "Apache-2.0"),
    ],
)
def test_first_party_oss_keeps_its_canonical_boundary(
    catalogue, tool_id, repository, spdx
) -> None:
    tool = catalogue[tool_id]
    assert tool["repository_url"] == f"https://github.com/{repository}"
    assert tool["license_model"] == "oss"
    assert tool["license_spdx"] == spdx
    assert any("/blob/" in source and "LICENSE" in source for source in tool["sources"])


def test_k0rdent_is_cluster_management_not_a_security_scanner(catalogue) -> None:
    tool = catalogue["k0rdent"]
    assert tool["categories"][0] == "kubernetes-distributions-operations"
    assert "application-cloud-security" not in tool["categories"]
    assert {"platform-engineer", "kubernetes-engineer"} <= set(tool["roles"])
    assert {"deploy", "operate"} <= set(tool["lifecycle_stages"])


def test_spacelift_workers_are_distinguished_from_the_control_plane(catalogue) -> None:
    tool = catalogue["spacelift"]
    assert {"hosted-saas", "self-hosted"} <= set(tool["deployment_models"])
    assert "https://docs.spacelift.io/concepts/worker-pools" in tool["sources"]
    assert "https://docs.spacelift.io/self-hosted" in tool["sources"]
    assert "control plane" in " ".join(tool["avoid_when"]).lower()


def test_cloudbees_identity_is_the_ci_product(catalogue) -> None:
    tool = catalogue["cloudbees"]
    assert tool["name"] == "CloudBees CI"
    assert "/cloudbees-ci/" in tool["documentation_url"]
    assert tool["deployment_models"] == ["self-hosted"]


def test_tekton_project_is_broader_than_pipelines_and_has_current_governance(
    catalogue,
) -> None:
    tool = catalogue["tekton"]
    assert "ecosystem" in tool["summary"].lower()
    assert "https://www.cncf.io/projects/tekton/" in tool["sources"]
    assert tool["documentation_url"] == "https://tekton.dev/docs/"
    assert {"build", "test", "deploy"} <= set(tool["lifecycle_stages"])


def test_terragrunt_supports_both_opentofu_and_terraform(catalogue) -> None:
    tool = catalogue["terragrunt"]
    text = " ".join([tool["summary"], *tool["use_when"]]).lower()
    assert "opentofu" in text
    assert "terraform" in text


def test_cdk8s_synthesizes_manifests_without_deploying(catalogue) -> None:
    tool = catalogue["cdk8s"]
    assert "deploy" not in tool["lifecycle_stages"]
    assert "build" in tool["lifecycle_stages"]
    assert "synthes" in tool["summary"].lower()
    assert "separate tools" in tool["summary"].lower()
    assert "kubectl" in " ".join(tool["use_when"])
    assert "JavaScript" in tool["summary"]
    assert "JavaScript" in " ".join(tool["use_when"])


def test_spinnaker_project_lifecycle_is_separate_from_halyard_deprecation(
    catalogue,
) -> None:
    tool = catalogue["spinnaker"]
    assert tool["status"] == "active"
    assert tool["repository_archived"] is False
    assert tool["categories"][0] == "cd-gitops-release-promotion"
    assert {"release", "deploy"} <= set(tool["lifecycle_stages"])
    assert "https://spinnaker.io/docs/setup/install/" in tool["sources"]
    assert "Kustomize" in " ".join(tool["use_when"])
    guidance = " ".join(tool["avoid_when"])
    assert "Halyard" in guidance
    assert "deprecated" in guidance
    assert "unsupported" in guidance
