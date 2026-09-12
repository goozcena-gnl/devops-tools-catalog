from scripts.catalog import load_tools


def _batch_tools() -> dict[str, dict[str, object]]:
    selected = {"aitmpl-agents", "aws-cloud9"}
    return {tool["id"]: tool for tool in load_tools() if tool["id"] in selected}


def test_cloud9_lifecycle_reflects_new_customer_closure() -> None:
    cloud9 = _batch_tools()["aws-cloud9"]

    assert cloud9["status"] == "deprecated"
    assert cloud9["license_model"] == "commercial"
    assert cloud9["needs_review"] is False
    assert "new customer" in " ".join(cloud9["avoid_when"]).lower()


def test_aitmpl_agents_retains_review_for_component_license_boundary() -> None:
    aitmpl = _batch_tools()["aitmpl-agents"]

    assert (
        aitmpl["repository_url"] == "https://github.com/davila7/claude-code-templates"
    )
    assert aitmpl["license_model"] == "unknown"
    assert aitmpl["status"] == "needs-review"
    assert aitmpl["needs_review"] is True
