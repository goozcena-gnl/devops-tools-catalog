from scripts.catalog import load_tools


def _tools_by_id() -> dict[str, dict[str, object]]:
    return {tool["id"]: tool for tool in load_tools()}


def test_azure_functions_service_is_distinct_from_oss_runtime() -> None:
    tools = _tools_by_id()
    service = tools["azure-functions"]
    runtime = tools["azure-functions-host"]

    assert service["license_model"] == "commercial"
    assert service["deployment_models"] == ["managed-service"]
    assert "repository_url" not in service
    assert runtime["license_model"] == "oss"
    assert runtime["repository_url"] == "https://github.com/Azure/azure-functions-host"


def test_commercial_platforms_do_not_inherit_component_licenses() -> None:
    tools = _tools_by_id()
    commercial_products = {
        "azure-devops",
        "bitrise",
        "buildkite",
        "cast-ai",
        "chainguard",
        "checkmarx",
        "circleci",
    }

    for tool_id in commercial_products:
        assert tools[tool_id]["license_model"] == "commercial"
        assert "repository_url" not in tools[tool_id]

    assert tools["kics"]["license_model"] == "oss"
    assert tools["checkmarx"]["name"] == "Checkmarx One"
    assert tools["chainguard"]["name"] == "Chainguard Containers"


def test_batch_02_standalone_oss_identities_use_canonical_repositories() -> None:
    tools = _tools_by_id()
    expected = {
        "casavue": ("https://github.com/czoczo/casavue", "GPL-3.0"),
        "cc-switch": ("https://github.com/farion1231/cc-switch", "MIT"),
    }

    for tool_id, (repository, spdx) in expected.items():
        tool = tools[tool_id]
        assert tool["repository_url"] == repository
        assert tool["repository_archived"] is False
        assert tool["license_model"] == "oss"
        assert tool["license_spdx"] == spdx
        assert tool["needs_review"] is False


def test_bamboo_is_deprecated_with_documented_data_center_exit_boundary() -> None:
    bamboo = _tools_by_id()["bamboo"]

    assert bamboo["status"] == "deprecated"
    assert bamboo["license_model"] == "commercial"
    assert bamboo["needs_review"] is False
    assert "2029" in " ".join(bamboo["avoid_when"])
