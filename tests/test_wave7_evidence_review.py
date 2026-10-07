"""Durable product, licence and execution boundaries reviewed in Wave 7."""

import pytest

from scripts.catalog import load_tools


@pytest.fixture(scope="module")
def catalogue() -> dict[str, dict]:
    return {tool["id"]: tool for tool in load_tools()}


@pytest.mark.parametrize(
    ("tool_id", "repository", "spdx"),
    [
        ("rancher", "rancher/rancher", "Apache-2.0"),
        ("renovate", "renovatebot/renovate", "AGPL-3.0-only"),
        ("bazel", "bazelbuild/bazel", "Apache-2.0"),
        ("skaffold", "GoogleContainerTools/skaffold", "Apache-2.0"),
        ("rke2", "rancher/rke2", "Apache-2.0"),
        ("kube-bench", "aquasecurity/kube-bench", "Apache-2.0"),
    ],
)
def test_oss_implementation_licences_do_not_inherit_service_terms(
    catalogue, tool_id, repository, spdx
) -> None:
    tool = catalogue[tool_id]
    assert tool["repository_url"] == f"https://github.com/{repository}"
    assert tool["license_model"] == "oss"
    assert tool["license_spdx"] == spdx
    assert any(
        "/blob/" in source and "license" in source.lower() for source in tool["sources"]
    )


def test_terraform_cloud_stable_id_represents_renamed_hosted_product(catalogue) -> None:
    tool = catalogue["terraform-cloud"]
    assert tool["name"] == "HCP Terraform"
    assert tool["license_model"] == "commercial"
    assert tool["commercial_offering"] is True
    assert "license_spdx" not in tool
    assert "repository_url" not in tool
    assert "repository_archived" not in tool
    assert tool["deployment_models"] == ["hosted-saas"]
    assert "https://www.hashicorp.com/en/hcp-terraform" in tool["sources"]
    assert "Terraform Enterprise" in tool["summary"]


def test_private_agents_do_not_make_hcp_control_plane_self_hosted(catalogue) -> None:
    tool = catalogue["terraform-cloud"]
    assert (
        "https://developer.hashicorp.com/terraform/cloud-docs/agents" in tool["sources"]
    )
    assert "self-hosted control plane" in " ".join(tool["avoid_when"])


@pytest.mark.parametrize("tool_id", ["terraform", "nomad"])
def test_current_ce_source_licences_do_not_inherit_historical_mpl(
    catalogue, tool_id
) -> None:
    tool = catalogue[tool_id]
    assert tool["license_model"] == "source-available"
    assert tool["license_spdx"] == "BUSL-1.1"
    assert (
        f"https://github.com/hashicorp/{tool_id}/blob/main/LICENSE" in tool["sources"]
    )
    assert any(
        "/blob/v" in source and source.endswith("/LICENSE")
        for source in tool["sources"]
    )
    assert tool["commercial_offering"] is True


def test_terraform_ce_cli_is_distinct_from_hcp_and_providers(catalogue) -> None:
    tool = catalogue["terraform"]
    assert tool["name"] == "Terraform Community Edition"
    assert tool["deployment_models"] == ["local"]
    assert "providers" in tool["summary"]
    assert "HCP Terraform" in tool["summary"]
    assert (
        "https://developer.hashicorp.com/terraform/intro/terraform-editions"
        in tool["sources"]
    )


def test_nomad_ce_support_does_not_grant_enterprise_entitlements(catalogue) -> None:
    tool = catalogue["nomad"]
    assert tool["deployment_models"] == ["self-hosted"]
    assert (
        "https://developer.hashicorp.com/nomad/docs/ce-license-support"
        in tool["sources"]
    )
    assert (
        "https://developer.hashicorp.com/nomad/commands/license/inspect"
        in tool["sources"]
    )
    assert "Enterprise entitlements" in " ".join(tool["avoid_when"])


def test_rancher_manager_oss_is_distinct_from_prime_services(catalogue) -> None:
    tool = catalogue["rancher"]
    assert tool["name"] == "Rancher Manager"
    assert tool["commercial_offering"] is True
    assert tool["deployment_models"] == ["self-hosted"]
    assert "Rancher Prime" in tool["summary"]
    assert any(
        source.endswith("/deploy-rancher-manager/prime") for source in tool["sources"]
    )


def test_gitlab_parent_does_not_inherit_ce_mirror_mit_badge(catalogue) -> None:
    tool = catalogue["gitlab"]
    assert tool["repository_url"] == "https://gitlab.com/gitlab-org/gitlab"
    assert "https://github.com/gitlabhq/gitlabhq" in tool["sources"]
    assert tool["license_model"] == "open-core"
    assert "license_spdx" not in tool
    assert tool["commercial_offering"] is True
    assert (
        "https://gitlab.com/gitlab-org/gitlab/-/raw/master/ee/LICENSE"
        in tool["sources"]
    )
    assert {"hosted-saas", "self-hosted"} == set(tool["deployment_models"])
    assert "Free means CE" in " ".join(tool["avoid_when"])


def test_renovate_oss_execution_is_distinct_from_mend_hosting(catalogue) -> None:
    tool = catalogue["renovate"]
    assert tool["commercial_offering"] is True
    assert {"local", "self-hosted"} == set(tool["deployment_models"])
    assert (
        "https://github.com/renovatebot/renovate/blob/main/package.json"
        in tool["sources"]
    )
    assert "https://docs.renovatebot.com/mend-hosted/overview/" in tool["sources"]
    assert "deploy" not in tool["lifecycle_stages"]


def test_bazel_is_a_build_test_system_with_external_backends(catalogue) -> None:
    tool = catalogue["bazel"]
    assert tool["categories"] == ["ci-build-testing"]
    assert tool["lifecycle_stages"] == ["build", "test"]
    assert tool["deployment_models"] == ["local"]
    assert "https://bazel.build/release" in tool["sources"]
    assert "automatic hermeticity" in " ".join(tool["avoid_when"])


def test_skaffold_loop_scope_and_planned_retirement_are_evidenced(catalogue) -> None:
    tool = catalogue["skaffold"]
    assert {"develop", "build", "test", "deploy"} <= set(tool["lifecycle_stages"])
    assert tool["deployment_models"] == ["local"]
    assert (
        "https://github.com/GoogleContainerTools/skaffold/blob/main/docs-v2/content/en/docs/_index.md"
        in tool["sources"]
    )
    assert "archiv" in tool["summary"].lower()
    assert "upstream maintenance" in " ".join(tool["avoid_when"])


def test_rke2_security_positioning_is_not_automatic_certification(catalogue) -> None:
    tool = catalogue["rke2"]
    assert tool["commercial_offering"] is True
    assert tool["deployment_models"] == ["self-hosted"]
    assert "https://docs.rke2.io/security/hardening_guide" in tool["sources"]
    assert "https://docs.rke2.io/security/fips_support" in tool["sources"]
    assert "certifies compliance" in " ".join(tool["avoid_when"])
    assert "validate FIPS component choices" in " ".join(tool["use_when"])


def test_kube_bench_implementation_does_not_define_cis_or_exclude_workers(
    catalogue,
) -> None:
    tool = catalogue["kube-bench"]
    assert tool["official_url"] == tool["repository_url"]
    assert "https://aquasecurity.github.io/kube-bench" in tool["sources"]
    assert "https://www.cisecurity.org/benchmark/kubernetes" in tool["sources"]
    assert (
        "https://github.com/aquasecurity/kube-bench/blob/main/docs/platforms.md"
        in tool["sources"]
    )
    assert "does not define the CIS" in tool["summary"]
    assert "worker-node" in " ".join(tool["use_when"])
    assert "provider-managed control plane" in " ".join(tool["avoid_when"])
