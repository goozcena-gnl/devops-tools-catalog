from scripts.catalog import load_tools

BATCH_05_IDS = {
    "git-push-no-mistakes",
    "github",
    "gke",
    "gonzo",
    "google-artifact-registry",
    "google-cloud-build",
    "google-cloud-functions",
    "google-cloud-organization-policy",
    "google-cloud-run",
    "haproxy-kubernetes-ingress-controller",
    "harness",
    "hermes-agent",
    "heroku",
    "honeycomb",
    "hortator",
    "humanitec",
    "hybrid-analysis",
    "ibm-guardium-key-lifecycle-manager",
    "intellij-idea",
    "isms-builder",
}


def _tools_by_id() -> dict[str, dict[str, object]]:
    return {tool["id"]: tool for tool in load_tools()}


def test_batch_05_records_are_current_and_fully_accounted() -> None:
    tools = _tools_by_id()

    assert len(BATCH_05_IDS) == 20
    for tool_id in BATCH_05_IDS:
        tool = tools[tool_id]
        assert tool["verified_on"] == "2026-09-14"
        assert tool["status"] == "active"
        assert tool["license_model"] != "unknown"
        assert tool["maturity"] != "unknown"
        assert tool["needs_review"] is False


def test_standalone_software_uses_its_canonical_repository_licence() -> None:
    tools = _tools_by_id()
    expected = {
        "git-push-no-mistakes": ("https://github.com/kunchenguid/no-mistakes", "MIT"),
        "gonzo": ("https://github.com/control-theory/gonzo", "MIT"),
        "haproxy-kubernetes-ingress-controller": (
            "https://github.com/haproxytech/kubernetes-ingress",
            "Apache-2.0",
        ),
        "hermes-agent": ("https://github.com/NousResearch/hermes-agent", "MIT"),
        "isms-builder": (
            "https://github.com/coolstartnow/isms-builder",
            "AGPL-3.0-only",
        ),
    }

    for tool_id, (repository, spdx) in expected.items():
        tool = tools[tool_id]
        assert tool["repository_url"] == repository
        assert tool["license_model"] == "oss"
        assert tool["license_spdx"] == spdx


def test_managed_products_do_not_inherit_component_licences() -> None:
    tools = _tools_by_id()
    managed_products = {
        "github",
        "gke",
        "google-artifact-registry",
        "google-cloud-build",
        "google-cloud-functions",
        "google-cloud-organization-policy",
        "google-cloud-run",
        "harness",
        "heroku",
        "honeycomb",
        "humanitec",
        "ibm-guardium-key-lifecycle-manager",
    }

    for tool_id in managed_products:
        tool = tools[tool_id]
        assert tool["license_model"] == "commercial"
        assert tool["commercial_offering"] is True
        assert "repository_url" not in tool


def test_mixed_and_hosted_product_boundaries_remain_explicit() -> None:
    tools = _tools_by_id()

    cloud_functions = tools["google-cloud-functions"]
    assert cloud_functions["name"] == "Cloud Run functions"
    assert any(
        "formerly" in source or "is-now" in source
        for source in cloud_functions["sources"]
    )

    for tool_id in {"hortator", "intellij-idea"}:
        assert tools[tool_id]["license_model"] == "open-core"
        assert tools[tool_id]["commercial_offering"] is True

    hybrid_analysis = tools["hybrid-analysis"]
    assert hybrid_analysis["license_model"] == "free-saas"
    assert "repository_url" not in hybrid_analysis
