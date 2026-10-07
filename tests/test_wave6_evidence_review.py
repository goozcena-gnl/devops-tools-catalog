"""Durable upstream, execution and licence boundaries reviewed in Wave 6."""

import pytest

from scripts.catalog import load_tools


@pytest.fixture(scope="module")
def catalogue() -> dict[str, dict]:
    return {tool["id"]: tool for tool in load_tools()}


@pytest.mark.parametrize(
    ("tool_id", "repository", "spdx"),
    [
        ("opentofu", "opentofu/opentofu", "MPL-2.0"),
        ("buildkit", "moby/buildkit", "Apache-2.0"),
        ("buildah", "containers/buildah", "Apache-2.0"),
        ("kubevirt", "kubevirt/kubevirt", "Apache-2.0"),
        ("vcluster", "loft-sh/vcluster", "Apache-2.0"),
        ("cadvisor", "google/cadvisor", "Apache-2.0"),
        ("uptime-kuma", "louislam/uptime-kuma", "MIT"),
    ],
)
def test_oss_records_keep_their_upstream_software_licences(
    catalogue, tool_id, repository, spdx
) -> None:
    tool = catalogue[tool_id]
    assert tool["repository_url"] == f"https://github.com/{repository}"
    assert tool["license_model"] == "oss"
    assert tool["license_spdx"] == spdx
    assert any("/blob/" in source and "LICENSE" in source for source in tool["sources"])


def test_opentofu_governance_and_migration_are_evidenced(catalogue) -> None:
    tool = catalogue["opentofu"]
    assert "https://github.com/opentofu/org/blob/main/CHARTER.md" in tool["sources"]
    assert "https://opentofu.org/docs/intro/migration/" in tool["sources"]
    assert tool["deployment_models"] == ["local"]


def test_packer_current_source_does_not_inherit_historical_mpl(catalogue) -> None:
    tool = catalogue["packer"]
    assert tool["license_model"] == "source-available"
    assert tool["license_spdx"] == "BUSL-1.1"
    assert "https://github.com/hashicorp/packer/blob/main/LICENSE" in tool["sources"]
    assert tool["commercial_offering"] is True
    assert tool["deployment_models"] == ["local"]
    assert "https://developer.hashicorp.com/packer/docs/hcp" in tool["sources"]
    assert (
        "https://developer.hashicorp.com/packer/docs/plugins/install" in tool["sources"]
    )
    assert "deploy" not in tool["lifecycle_stages"]


def test_buildkit_backend_is_distinct_from_buildx_client(catalogue) -> None:
    tool = catalogue["buildkit"]
    assert tool["deployment_models"] == ["self-hosted"]
    assert "https://docs.docker.com/build/concepts/overview/" in tool["sources"]
    assert "backend" in tool["summary"].lower()
    assert "Buildx" in tool["summary"]


def test_buildah_image_builder_is_distinct_from_podman_runtime(catalogue) -> None:
    tool = catalogue["buildah"]
    assert tool["deployment_models"] == ["local"]
    assert "daemonless" in tool["summary"].lower()
    assert "runtime" in " ".join(tool["avoid_when"]).lower()
    assert tool["documentation_url"].startswith(
        "https://github.com/podman-container-tools/buildah/"
    )


def test_kubevirt_vm_scope_and_governance_are_separate_from_kubernetes(
    catalogue,
) -> None:
    tool = catalogue["kubevirt"]
    assert "virtualization-bare-metal-homelab" in tool["categories"]
    assert "https://www.cncf.io/projects/kubevirt/" in tool["sources"]
    assert tool["documentation_url"] == "https://kubevirt.io/user-guide/"
    assert tool["deployment_models"] == ["self-hosted"]


def test_vcluster_oss_does_not_license_platform_entitlements(catalogue) -> None:
    tool = catalogue["vcluster"]
    assert tool["commercial_offering"] is True
    assert (
        "https://www.vcluster.com/docs/vcluster/introduction/oss-vs-free"
        in tool["sources"]
    )
    assert (
        "https://www.vcluster.com/docs/platform/understand/licensing" in tool["sources"]
    )
    assert "tier-gated" in " ".join(tool["avoid_when"])


def test_cadvisor_uses_upstream_as_its_official_entry_point(catalogue) -> None:
    tool = catalogue["cadvisor"]
    assert tool["official_url"] == tool["repository_url"]
    assert (
        tool["documentation_url"]
        == "https://github.com/google/cadvisor/tree/master/docs"
    )
    assert tool["deployment_models"] == ["self-hosted"]


def test_uptime_kuma_does_not_inherit_third_party_hosting(catalogue) -> None:
    tool = catalogue["uptime-kuma"]
    assert tool["deployment_models"] == ["self-hosted"]
    assert tool["documentation_url"] == "https://github.com/louislam/uptime-kuma/wiki"
    assert "commercial_offering" not in tool


def test_camunda_parent_platform_does_not_inherit_sdk_oss_licences(catalogue) -> None:
    tool = catalogue["camunda"]
    assert tool["name"] == "Camunda 8"
    assert tool["license_model"] == "commercial"
    assert "license_spdx" not in tool
    assert tool["commercial_offering"] is True
    assert tool["repository_url"] == "https://github.com/camunda/camunda"
    assert "https://docs.camunda.io/docs/reference/licenses/" in tool["sources"]
    assert {"hosted-saas", "self-hosted"} <= set(tool["deployment_models"])
    assert "non-production" in " ".join(tool["avoid_when"])


def test_passbolt_server_agpl_is_separate_from_subscription_keys(catalogue) -> None:
    tool = catalogue["passbolt"]
    assert tool["repository_url"] == "https://github.com/passbolt/passbolt_api"
    assert tool["license_model"] == "oss"
    assert tool["license_spdx"] == "AGPL-3.0-or-later"
    assert tool["commercial_offering"] is True
    assert (
        "https://github.com/passbolt/passbolt_api/blob/master/composer.json"
        in tool["sources"]
    )
    assert "https://www.passbolt.com/terms/pro" in tool["sources"]
    assert "subscription-key" in " ".join(tool["avoid_when"])
    assert {"hosted-saas", "self-hosted"} <= set(tool["deployment_models"])
