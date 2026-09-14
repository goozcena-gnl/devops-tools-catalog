from scripts.catalog import load_tools

BATCH_06_IDS = {
    "jarvis-os",
    "jfrog-connect",
    "jfrog-distribution",
    "jfrog-pipelines",
    "jfrog-platform",
    "jira",
    "json-crack",
    "k8s-diagram-builder",
    "k8studio",
    "kasten-k10",
    "katalon-studio",
    "kindling",
    "kion-finops",
    "kiuwan",
    "kontroler",
    "kro",
    "kubara",
    "kube-argus",
    "kubegui",
    "kubehatch",
}


def _tools_by_id() -> dict[str, dict[str, object]]:
    return {tool["id"]: tool for tool in load_tools()}


def test_batch_06_records_are_current_and_fully_accounted() -> None:
    tools = _tools_by_id()

    assert len(BATCH_06_IDS) == 20
    for tool_id in BATCH_06_IDS:
        assert tools[tool_id]["verified_on"] == "2026-09-14"

    blocker = tools["kindling"]
    assert blocker["status"] == "needs-review"
    assert blocker["license_model"] == "unknown"
    assert blocker["maturity"] == "unknown"
    assert blocker["needs_review"] is True

    for tool_id in BATCH_06_IDS - {"kindling"}:
        tool = tools[tool_id]
        assert tool["license_model"] != "unknown"
        assert tool["maturity"] != "unknown"
        assert tool["needs_review"] is False


def test_jfrog_product_and_lifecycle_boundaries_remain_explicit() -> None:
    tools = _tools_by_id()

    for tool_id in {
        "jfrog-connect",
        "jfrog-distribution",
        "jfrog-pipelines",
        "jfrog-platform",
    }:
        tool = tools[tool_id]
        assert tool["license_model"] == "commercial"
        assert tool["commercial_offering"] is True
        assert "repository_url" not in tool

    assert tools["jfrog-pipelines"]["status"] == "historical"
    for tool_id in {"jfrog-connect", "jfrog-distribution", "jfrog-platform"}:
        assert tools[tool_id]["status"] == "active"


def test_commercial_products_do_not_inherit_component_licences() -> None:
    tools = _tools_by_id()

    for tool_id in {
        "jira",
        "k8studio",
        "kasten-k10",
        "katalon-studio",
        "kion-finops",
        "kiuwan",
    }:
        tool = tools[tool_id]
        assert tool["license_model"] == "commercial"
        assert tool["commercial_offering"] is True
        assert "repository_url" not in tool

    assert tools["jira"]["status"] == "active"
    assert tools["kasten-k10"]["name"] == "Veeam Kasten for Kubernetes"
    assert tools["kion-finops"]["name"] == "Kion FinOps+"


def test_standalone_projects_use_their_canonical_repository_licences() -> None:
    tools = _tools_by_id()
    expected = {
        "jarvis-os": ("https://github.com/JarvisOSLinux/jarvisos", "GPL-3.0-only"),
        "json-crack": (
            "https://github.com/AykutSarac/jsoncrack.com",
            "Apache-2.0",
        ),
        "k8s-diagram-builder": (
            "https://github.com/abhayraghuwanshi/k8s-ingress-gen",
            "MIT",
        ),
        "kontroler": (
            "https://github.com/GreedyKomodoDragon/Kontroler",
            "AGPL-3.0-only",
        ),
        "kro": ("https://github.com/kubernetes-sigs/kro", "Apache-2.0"),
        "kubara": ("https://github.com/kubara-io/kubara", "Apache-2.0"),
        "kube-argus": (
            "https://github.com/manishchaudhary101/kube-argus",
            "Apache-2.0",
        ),
        "kubegui": ("https://github.com/gerbil/kubegui", "MIT"),
        "kubehatch": (
            "https://github.com/vClusterLabs-Experiments/kubehatch",
            "MIT",
        ),
    }

    for tool_id, (repository, spdx) in expected.items():
        tool = tools[tool_id]
        assert tool["repository_url"] == repository
        assert tool["license_model"] == "oss"
        assert tool["license_spdx"] == spdx
