from scripts.catalog import load_tools


def _tools_by_id() -> dict[str, dict[str, object]]:
    return {tool["id"]: tool for tool in load_tools()}


def test_docker_build_umbrella_remains_an_identity_blocker() -> None:
    tools = _tools_by_id()
    docker_build = tools["docker-build"]

    assert docker_build["status"] == "needs-review"
    assert docker_build["license_model"] == "unknown"
    assert docker_build["maturity"] == "unknown"
    assert docker_build["needs_review"] is True
    assert "repository_url" not in docker_build
    assert (
        tools["docker-buildx"]["repository_url"] == "https://github.com/docker/buildx"
    )
    assert tools["buildkit"]["repository_url"] == "https://github.com/moby/buildkit"


def test_docker_product_and_oss_component_boundaries_remain_distinct() -> None:
    tools = _tools_by_id()

    for tool_id in {"docker-desktop", "docker-hub", "docker-offload"}:
        assert tools[tool_id]["license_model"] == "commercial"
        assert "repository_url" not in tools[tool_id]

    docker_agent = tools["docker-agent"]
    assert docker_agent["license_model"] == "oss"
    assert docker_agent["license_spdx"] == "Apache-2.0"
    assert docker_agent["repository_url"] == "https://github.com/docker/docker-agent"

    docker_hub_mcp = tools["docker-hub-mcp"]
    assert docker_hub_mcp["license_model"] == "unknown"
    assert docker_hub_mcp["status"] == "needs-review"
    assert docker_hub_mcp["needs_review"] is True
    assert "repository_url" not in docker_hub_mcp
    assert tools["docker-mcp-gateway"]["repository_url"] == (
        "https://github.com/docker/mcp-gateway"
    )


def test_codiga_shutdown_is_recorded_as_historical() -> None:
    codiga = _tools_by_id()["codiga"]

    assert codiga["status"] == "historical"
    assert codiga["license_model"] == "commercial"
    assert codiga["needs_review"] is False
    assert "2023-05-04" in " ".join(codiga["avoid_when"])


def test_eviden_kms_preserves_source_available_product_boundary() -> None:
    kms = _tools_by_id()["cosmian-kms"]

    assert kms["name"] == "Eviden KMS"
    assert kms["repository_url"] == "https://github.com/Cosmian/kms"
    assert kms["license_model"] == "source-available"
    assert "license_spdx" not in kms
    assert kms["commercial_offering"] is True
    assert kms["needs_review"] is False
