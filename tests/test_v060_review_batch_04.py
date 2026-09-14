from scripts.catalog import load_tools


def _tools_by_id() -> dict[str, dict[str, object]]:
    return {tool["id"]: tool for tool in load_tools()}


def test_docker_swarm_umbrella_remains_an_identity_blocker() -> None:
    swarm = _tools_by_id()["docker-swarm"]

    assert swarm["status"] == "needs-review"
    assert swarm["license_model"] == "unknown"
    assert swarm["maturity"] == "unknown"
    assert swarm["needs_review"] is True
    assert "repository_url" not in swarm
    assert "https://github.com/moby/swarmkit" in swarm["sources"]
    assert "https://github.com/docker-archive/classicswarm" in swarm["sources"]


def test_filigran_vendor_does_not_inherit_opencti_metadata() -> None:
    filigran = _tools_by_id()["filigran"]

    assert filigran["status"] == "needs-review"
    assert filigran["license_model"] == "unknown"
    assert filigran["maturity"] == "unknown"
    assert filigran["needs_review"] is True
    assert "repository_url" not in filigran
    assert "documentation_url" not in filigran
    assert any("OpenCTI-Platform/opencti" in source for source in filigran["sources"])


def test_aws_container_service_boundaries_remain_distinct() -> None:
    tools = _tools_by_id()

    expected_names = {
        "ecs": "Amazon ECS",
        "eks": "Amazon EKS",
        "fargate": "AWS Fargate",
    }
    for tool_id, name in expected_names.items():
        tool = tools[tool_id]
        assert tool["name"] == name
        assert tool["license_model"] == "commercial"
        assert tool["commercial_offering"] is True
        assert tool["status"] == "active"
        assert tool["needs_review"] is False
        assert "repository_url" not in tool


def test_product_and_standalone_software_licences_stay_separate() -> None:
    tools = _tools_by_id()

    key_manager = tools["entrust-keycontrol"]
    assert key_manager["name"] == (
        "Entrust Cryptographic Security Platform Key Manager"
    )
    assert key_manager["license_model"] == "commercial"
    assert key_manager["needs_review"] is False

    dockhand = tools["dockhand"]
    assert dockhand["repository_url"] == "https://github.com/Finsys/dockhand"
    assert dockhand["license_model"] == "source-available"
    assert dockhand["license_spdx"] == "BUSL-1.1"
    assert dockhand["categories"] == ["virtualization-bare-metal-homelab"]
    assert "kubernetes-distributions-operations" not in dockhand["categories"]
    assert dockhand["subcategories"] == ["Virtualization & Containerization"]
    assert "Kubernetes Management & Operations" not in dockhand.get("subcategories", [])
    assert set(dockhand["roles"]) == {
        "infrastructure-systems-engineer",
        "devops-engineer",
    }

    flathub = tools["flathub"]
    assert flathub["license_model"] == "free-saas"
    assert "repository_url" not in flathub

    garage_webui = tools["garage-webui"]
    assert garage_webui["repository_url"] == (
        "https://github.com/khairul169/garage-webui"
    )
    assert garage_webui["license_model"] == "oss"
    assert garage_webui["license_spdx"] == "MIT"
