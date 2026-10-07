"""Durable software, service and ecosystem boundaries reviewed in Wave 8."""

import pytest

from scripts.catalog import load_tools


@pytest.fixture(scope="module")
def catalogue() -> dict[str, dict]:
    return {tool["id"]: tool for tool in load_tools()}


@pytest.mark.parametrize(
    ("tool_id", "repository", "spdx"),
    [
        ("prometheus", "prometheus/prometheus", "Apache-2.0"),
        ("grafana-loki", "grafana/loki", "AGPL-3.0-only"),
        ("grafana-tempo", "grafana/tempo", "AGPL-3.0-only"),
        ("grafana-mimir", "grafana/mimir", "AGPL-3.0-only"),
        (
            "opentelemetry-collector",
            "open-telemetry/opentelemetry-collector",
            "Apache-2.0",
        ),
        ("jaeger", "jaegertracing/jaeger", "Apache-2.0"),
        ("thanos", "thanos-io/thanos", "Apache-2.0"),
        ("kube-state-metrics", "kubernetes/kube-state-metrics", "Apache-2.0"),
    ],
)
def test_implementation_licences_have_own_upstream_evidence(
    catalogue, tool_id, repository, spdx
) -> None:
    tool = catalogue[tool_id]
    assert tool["repository_url"] == f"https://github.com/{repository}"
    assert tool["license_model"] == "oss"
    assert tool["license_spdx"] == spdx
    assert f"https://github.com/{repository}/blob/main/LICENSE" in tool["sources"]


def test_grafana_family_does_not_inherit_one_oss_spdx(catalogue) -> None:
    tool = catalogue["grafana"]
    assert tool["license_model"] == "open-core"
    assert "license_spdx" not in tool
    assert tool["commercial_offering"] is True
    assert set(tool["deployment_models"]) == {"self-hosted", "hosted-saas"}
    assert all(
        edition in tool["summary"] for edition in ("OSS", "Enterprise", "Grafana Cloud")
    )
    assert "https://grafana.com/legal/grafana-labs-license/" in tool["sources"]
    assert "https://grafana.com/legal/enterprise-plugins/" in tool["sources"]
    assert "https://grafana.com/legal/msa/" in tool["sources"]


@pytest.mark.parametrize(
    ("tool_id", "cloud_product"),
    [
        ("grafana-loki", "Grafana Cloud Logs"),
        ("grafana-tempo", "Grafana Cloud Traces"),
        ("grafana-mimir", "Grafana Cloud Metrics"),
    ],
)
def test_grafana_backends_remain_oss_software_separate_from_cloud(
    catalogue, tool_id, cloud_product
) -> None:
    tool = catalogue[tool_id]
    assert tool["license_model"] == "oss"
    assert tool["license_spdx"] == "AGPL-3.0-only"
    assert tool["deployment_models"] == ["self-hosted"]
    assert tool["commercial_offering"] is True
    assert cloud_product in tool["summary"]
    assert tool["documentation_url"].startswith("https://grafana.com/docs/")
    assert "/cloud/" not in tool["documentation_url"]
    assert any(source.endswith("/LICENSING.md") for source in tool["sources"])


def test_opentelemetry_umbrella_is_not_a_single_implementation(catalogue) -> None:
    umbrella = catalogue["opentelemetry"]
    collector = catalogue["opentelemetry-collector"]
    assert umbrella["official_url"] == "https://opentelemetry.io/"
    assert umbrella["documentation_url"] == "https://opentelemetry.io/docs/"
    assert "repository_url" not in umbrella
    assert "repository_archived" not in umbrella
    assert umbrella["deployment_models"] == []
    assert "https://github.com/open-telemetry" in umbrella["sources"]
    assert "SDKs" in umbrella["summary"]
    assert "external" in umbrella["summary"]
    assert "develop" in umbrella["lifecycle_stages"]
    assert collector["repository_url"].endswith("/opentelemetry-collector")


def test_umbrella_spdx_is_backed_by_project_software_policy(catalogue) -> None:
    tool = catalogue["opentelemetry"]
    assert tool["license_model"] == "oss"
    assert tool["license_spdx"] == "Apache-2.0"
    assert (
        "https://github.com/open-telemetry/community/blob/main/README.md"
        in tool["sources"]
    )
    assert (
        "https://github.com/open-telemetry/community/blob/main/LICENSE"
        in tool["sources"]
    )
    assert "https://opentelemetry.io/status/" in tool["sources"]
    assert "uniform stability" in " ".join(tool["avoid_when"])


def test_collector_core_is_not_contrib_or_a_storage_backend(catalogue) -> None:
    tool = catalogue["opentelemetry-collector"]
    assert "core" in tool["summary"] and "contrib" in tool["summary"]
    assert all(
        word in tool["summary"] for word in ("receivers", "processors", "exporters")
    )
    assert tool["deployment_models"] == ["self-hosted"]
    assert tool["subcategories"] == ["Telemetry collection and processing"]
    assert "https://opentelemetry.io/docs/collector/distributions/" in tool["sources"]
    assert any(source.endswith("/component-stability.md") for source in tool["sources"])


def test_prometheus_server_does_not_absorb_ecosystem_components(catalogue) -> None:
    tool = catalogue["prometheus"]
    assert all(
        word in tool["summary"] for word in ("Alertmanager", "exporters", "separate")
    )
    assert "PromQL" in tool["summary"]
    assert tool["deployment_models"] == ["self-hosted"]
    assert "billing" in " ".join(tool["avoid_when"])


def test_loki_content_queries_do_not_imply_full_text_index(catalogue) -> None:
    tool = catalogue["grafana-loki"]
    assert "labels" in tool["summary"] and "LogQL" in tool["summary"]
    assert "full-text index" in " ".join(tool["avoid_when"])
    assert "tenant headers" in " ".join(tool["avoid_when"])
    assert (
        "https://grafana.com/docs/loki/latest/operations/authentication/"
        in tool["sources"]
    )


def test_tempo_search_and_protocols_are_not_trace_id_only(catalogue) -> None:
    tool = catalogue["grafana-tempo"]
    assert "TraceQL search" in tool["summary"]
    assert all(protocol in tool["summary"] for protocol in ("OTLP", "Jaeger", "Zipkin"))
    assert "configurable" in tool["summary"]
    assert "https://grafana.com/docs/tempo/latest/configuration/" in tool["sources"]


def test_jaeger_uses_opentelemetry_without_becoming_the_umbrella(catalogue) -> None:
    tool = catalogue["jaeger"]
    assert "backend" in tool["summary"] and "UI" in tool["summary"]
    assert "OpenTelemetry Collector framework" in tool["summary"]
    assert (
        tool["repository_url"] != catalogue["opentelemetry-collector"]["repository_url"]
    )
    assert tool["deployment_models"] == ["self-hosted"]


def test_thanos_extends_prometheus_and_keeps_own_identity(catalogue) -> None:
    tool = catalogue["thanos"]
    assert "global queries" in tool["summary"]
    assert "object stores" in tool["summary"]
    assert "HA pairs" in " ".join(tool["use_when"])
    assert tool["repository_url"] != catalogue["prometheus"]["repository_url"]
    assert tool["repository_url"] != catalogue["grafana-mimir"]["repository_url"]


def test_kube_state_metrics_is_sig_owned_object_state_not_resource_usage(
    catalogue,
) -> None:
    tool = catalogue["kube-state-metrics"]
    assert tool["name"] == "kube-state-metrics"
    assert "SIG Instrumentation" in tool["summary"]
    assert "object state" in tool["summary"]
    assert all(
        component in tool["summary"]
        for component in ("metrics-server", "cAdvisor", "Prometheus")
    )
    assert (
        "https://github.com/kubernetes/community/blob/main/sig-instrumentation/README.md"
        in tool["sources"]
    )
    assert "kubernetes-engineer" in tool["roles"]


@pytest.mark.parametrize("tool_id", ["prometheus", "opentelemetry", "jaeger", "thanos"])
def test_foundation_governance_does_not_replace_licence_evidence(
    catalogue, tool_id
) -> None:
    tool = catalogue[tool_id]
    assert f"https://www.cncf.io/projects/{tool_id}/" in tool["sources"]
    assert tool["license_spdx"] == "Apache-2.0"
    assert any(source.endswith("/LICENSE") for source in tool["sources"])
