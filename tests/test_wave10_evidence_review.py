"""Durable DNS, gateway, metrics, storage and autoscaling identity boundaries."""

import pytest

from scripts.catalog import load_tools


@pytest.fixture(scope="module")
def catalogue() -> dict[str, dict]:
    return {tool["id"]: tool for tool in load_tools()}


@pytest.mark.parametrize(
    ("tool_id", "repository", "branch", "licence"),
    [
        ("istio", "istio/istio", "master", "LICENSE"),
        ("coredns", "coredns/coredns", "master", "LICENSE"),
        ("metallb", "metallb/metallb", "main", "LICENSE"),
        ("externaldns", "kubernetes-sigs/external-dns", "master", "LICENSE.md"),
        ("envoy-gateway", "envoyproxy/gateway", "main", "LICENSE"),
        ("longhorn", "longhorn/longhorn", "master", "LICENSE"),
        ("metrics-server", "kubernetes-sigs/metrics-server", "master", "LICENSE"),
        ("kubernetes-autoscaler", "kubernetes/autoscaler", "master", "LICENSE"),
        ("karpenter", "kubernetes-sigs/karpenter", "main", "LICENSE"),
        ("keda", "kedacore/keda", "main", "LICENSE"),
    ],
)
def test_project_licences_have_project_specific_evidence(
    catalogue, tool_id, repository, branch, licence
) -> None:
    tool = catalogue[tool_id]
    assert tool["repository_url"] == f"https://github.com/{repository}"
    assert tool["license_model"] == "oss"
    assert tool["license_spdx"] == "Apache-2.0"
    assert f"https://github.com/{repository}/blob/{branch}/{licence}" in set(
        tool["sources"]
    )


@pytest.mark.parametrize(
    "tool_id",
    [
        "istio",
        "coredns",
        "metallb",
        "externaldns",
        "envoy-gateway",
        "longhorn",
        "metrics-server",
        "karpenter",
        "keda",
    ],
)
def test_cluster_services_describe_server_controller_execution(catalogue, tool_id):
    assert catalogue[tool_id]["deployment_models"] == ["self-hosted"]


def test_coredns_and_externaldns_have_distinct_dns_roles(catalogue):
    server, controller = catalogue["coredns"], catalogue["externaldns"]
    assert server["repository_url"] != controller["repository_url"]
    assert "DNS server" in server["summary"]
    assert "Kubernetes plugin" in server["summary"]
    assert "synchronizes DNS records" in controller["summary"]
    assert "not a DNS server" in controller["summary"]
    assert server["documentation_url"].startswith("https://coredns.io/")
    assert controller["documentation_url"].startswith(
        "https://kubernetes-sigs.github.io/external-dns/"
    )


def test_mesh_gateway_and_proxy_identities_remain_distinct(catalogue):
    mesh, gateway = catalogue["istio"], catalogue["envoy-gateway"]
    assert mesh["repository_url"] == "https://github.com/istio/istio"
    assert gateway["repository_url"] == "https://github.com/envoyproxy/gateway"
    assert all(mode in mesh["summary"] for mode in ("sidecar", "ambient"))
    assert "control plane" in gateway["summary"]
    assert "Envoy Proxy supplies the traffic dataplane" in gateway["summary"]
    assert "Gateway API defines the configuration standard" in gateway["summary"]
    assert "service mesh" in " ".join(gateway["avoid_when"])


def test_metallb_scopes_loadbalancer_services_and_network_requirements(catalogue):
    tool = catalogue["metallb"]
    assert all(term in tool["summary"] for term in ("LoadBalancer", "Layer 2", "BGP"))
    assert "ingress controllers" in tool["summary"]
    assert "router" in " ".join(tool["avoid_when"])
    assert "https://metallb.io/concepts/bgp/" in set(tool["sources"])


def test_longhorn_block_storage_does_not_inherit_rancher_product_terms(catalogue):
    tool = catalogue["longhorn"]
    assert "block storage" in tool["summary"]
    assert "CSI" in tool["summary"]
    assert "file-sharing" in tool["summary"]
    assert all(
        product in " ".join(tool["avoid_when"])
        for product in ("Rancher Manager", "Rancher Prime", "Rook/Ceph")
    )
    assert tool["license_model"] == "oss"
    assert "https://github.com/longhorn/longhorn-manager/blob/master/LICENSE" in set(
        tool["sources"]
    )


def test_metrics_server_is_resource_api_not_historical_monitoring(catalogue):
    tool = catalogue["metrics-server"]
    assert tool["official_url"] == "https://github.com/kubernetes-sigs/metrics-server"
    assert tool["documentation_url"].endswith("/metrics-server/blob/master/README.md")
    assert all(
        term in tool["summary"]
        for term in (
            "CPU",
            "memory",
            "kubelets",
            "Metrics API",
            "HPA",
            "VPA",
            "kubectl top",
        )
    )
    assert "not historical time-series storage" in tool["summary"]
    assert all(
        other in " ".join(tool["avoid_when"])
        for other in ("Prometheus", "kube-state-metrics", "cAdvisor")
    )


def test_autoscaler_umbrella_separates_components_and_core_hpa(catalogue):
    tool = catalogue["kubernetes-autoscaler"]
    assert tool["repository_url"] == "https://github.com/kubernetes/autoscaler"
    assert tool["deployment_models"] == []
    assert all(
        component in tool["summary"]
        for component in (
            "Cluster Autoscaler",
            "Vertical Pod Autoscaler",
            "Addon Resizer",
        )
    )
    assert "Horizontal Pod Autoscaler is a separate Kubernetes-core" in tool["summary"]
    assert tool["documentation_url"].endswith("/autoscaler/blob/master/README.md")
    assert all(
        other in " ".join(tool["avoid_when"]) for other in ("HPA", "KEDA", "Karpenter")
    )


def test_karpenter_parent_core_preserves_aws_provider_provenance(catalogue):
    tool = catalogue["karpenter"]
    assert tool["repository_url"] == "https://github.com/kubernetes-sigs/karpenter"
    assert tool["official_url"] == tool["repository_url"]
    assert tool["documentation_url"].endswith("/karpenter/blob/main/README.md")
    assert "shared APIs and controllers" in tool["summary"]
    assert "separate provider implementations" in tool["summary"]
    assert "unschedulable pods" in tool["summary"]
    assert "shared core alone installs a cloud provider" in " ".join(tool["avoid_when"])
    assert any(
        source == "https://github.com/aws/karpenter-provider-aws"
        for source in tool["sources"]
    )
    assert any(source == "https://karpenter.sh" for source in tool["sources"])


def test_keda_scopes_workload_hpa_events_and_jobs_not_nodes(catalogue):
    tool = catalogue["keda"]
    assert all(
        term in tool["summary"]
        for term in ("workload", "HPA", "external metrics", "Jobs")
    )
    assert "separate from node provisioning" in tool["summary"]
    assert "Metrics Server" in tool["summary"]
    assert "event-source system" in " ".join(tool["avoid_when"])
    assert tool["repository_url"] not in {
        catalogue["karpenter"]["repository_url"],
        catalogue["kubernetes-autoscaler"]["repository_url"],
        catalogue["metrics-server"]["repository_url"],
    }


def test_foundation_and_beta_evidence_do_not_replace_software_licences(catalogue):
    assert catalogue["metallb"]["maturity"] == "growing"
    assert "https://metallb.io/concepts/maturity/" in set(
        catalogue["metallb"]["sources"]
    )
    for tool_id in ("istio", "coredns", "longhorn", "keda"):
        tool = catalogue[tool_id]
        assert f"https://www.cncf.io/projects/{tool_id}/" in set(tool["sources"])
        assert any(
            "/blob/" in source and source.endswith("/LICENSE")
            for source in tool["sources"]
        )
