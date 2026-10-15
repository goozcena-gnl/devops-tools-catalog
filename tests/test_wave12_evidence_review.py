"""Observability identity, software-grant and telemetry execution boundaries."""

import subprocess
from pathlib import Path

import pytest
import yaml

from scripts.catalog import load_tools, load_yaml

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = "data/tools/monitoring-metrics-logs-tracing.yaml"
REPORT = "docs/maintenance/2026-10-14-wave-12-observability-ebpf-evidence-review.md"
COHORT = (
    "grafana-beyla",
    "opentelemetry-ebpf-instrumentation",
    "grafana-pyroscope",
    "kubernetes-monitoring-mixins",
    "blackbox-exporter",
    "cortex",
    "victoriametrics",
    "vector",
    "fluentd",
    "telegraf",
)
LICENCES = (
    ("grafana-beyla", "grafana/beyla", "main", "Apache-2.0"),
    (
        "opentelemetry-ebpf-instrumentation",
        "open-telemetry/opentelemetry-ebpf-instrumentation",
        "main",
        "Apache-2.0",
    ),
    ("grafana-pyroscope", "grafana/pyroscope", "main", "AGPL-3.0-only"),
    (
        "kubernetes-monitoring-mixins",
        "kubernetes-sigs/kubernetes-mixin",
        "master",
        "Apache-2.0",
    ),
    ("blackbox-exporter", "prometheus/blackbox_exporter", "master", "Apache-2.0"),
    ("cortex", "cortexproject/cortex", "master", "Apache-2.0"),
    ("victoriametrics", "VictoriaMetrics/VictoriaMetrics", "master", "Apache-2.0"),
    ("vector", "vectordotdev/vector", "master", "MPL-2.0"),
    ("fluentd", "fluent/fluentd", "master", "Apache-2.0"),
    ("telegraf", "influxdata/telegraf", "master", "MIT"),
)


@pytest.fixture(scope="module")
def catalogue():
    return {tool["id"]: tool for tool in load_tools()}


@pytest.fixture(scope="module")
def report():
    return (ROOT / REPORT).read_text(encoding="utf-8")


def test_report_has_only_the_ten_selected_record_sections_and_240_fields(report):
    sections = {
        line.removeprefix("### ")
        for line in report.splitlines()
        if line.startswith("### ")
    }
    assert len(COHORT) == len(set(COHORT)) == 10
    assert sections == set(COHORT)
    all_fields = set()
    row_count = 0
    for tool_id in COHORT:
        section = report.split(f"### {tool_id}\n", 1)[1].split("\n### ", 1)[0]
        section = section.split("\n## ", 1)[0]
        fields = [
            line.split(" | ")[0].removeprefix("| ").strip("`")
            for line in section.splitlines()
            if line.startswith("| `")
        ]
        assert len(fields) == len(set(fields)) == 24
        all_fields.update(fields)
        row_count += len(fields)
    assert len(all_fields) == 24
    assert row_count == 240


def test_bounded_wave12_pr_changes_only_selected_existing_canonical_records():
    """Enforce this PR's scope without freezing all future catalogue reviews."""
    base = subprocess.run(
        ["git", "merge-base", "HEAD", "origin/main"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if base.returncode:
        pytest.skip("Wave 12 scope check requires the local main ref")
    base_sha = base.stdout.strip()
    already_in_base = subprocess.run(
        ["git", "cat-file", "-e", f"{base_sha}:{REPORT}"],
        cwd=ROOT,
        capture_output=True,
    )
    if already_in_base.returncode == 0:
        pytest.skip(
            "Wave 12 is already in the base; later reviews have their own scope"
        )
    files = subprocess.check_output(
        ["git", "diff", "--name-only", base_sha, "--", "data/tools"],
        cwd=ROOT,
        text=True,
    ).splitlines()
    assert files == [CANONICAL]
    old = yaml.safe_load(
        subprocess.check_output(
            ["git", "show", f"{base_sha}:{CANONICAL}"], cwd=ROOT, text=True
        )
    )
    before = {tool["id"]: tool for tool in old}
    after = {tool["id"]: tool for tool in load_yaml(ROOT / CANONICAL)}
    assert before.keys() == after.keys()
    assert {tool_id for tool_id in before if before[tool_id] != after[tool_id]} == set(
        COHORT
    )
    for tool_id in COHORT:
        assert set(before[tool_id]["sources"]) <= set(after[tool_id]["sources"])


@pytest.mark.parametrize("tool_id", COHORT)
def test_review_flags_and_historical_provenance_are_consistent(catalogue, tool_id):
    tool = catalogue[tool_id]
    assert tool["needs_review"] == (tool["status"] == "needs-review")
    assert tool["status"] == "active"
    assert tool["needs_review"] is False
    assert tool["repository_archived"] is False
    assert tool["categories"] == ["monitoring-metrics-logs-tracing"]
    assert tool["documentation_url"] in tool["sources"]
    assert any(source.startswith("legacy:") for source in tool["sources"])


@pytest.mark.parametrize(("tool_id", "repository", "branch", "spdx"), LICENCES)
def test_actual_project_licence_evidence_is_present(
    catalogue, tool_id, repository, branch, spdx
):
    tool = catalogue[tool_id]
    assert tool["repository_url"] == f"https://github.com/{repository}"
    assert tool["license_spdx"] == spdx
    assert tool["license_model"] == "oss"
    assert f"https://github.com/{repository}/blob/{branch}/LICENSE" in tool["sources"]


def test_beyla_distribution_and_obi_upstream_are_not_collapsed(catalogue):
    beyla = catalogue["grafana-beyla"]
    obi = catalogue["opentelemetry-ebpf-instrumentation"]
    assert beyla["repository_url"] != obi["repository_url"]
    assert "Grafana-supported distribution" in beyla["summary"]
    assert "distinct from upstream OBI" in beyla["summary"]
    assert "https://grafana.com/docs/beyla/latest/obi/" in beyla["sources"]
    assert "https://github.com/grafana/beyla" in beyla["sources"]
    assert beyla["status"] == obi["status"] == "active"
    assert "release" in " ".join(beyla["avoid_when"])


def test_obi_governance_does_not_erase_development_or_surface_limits(catalogue):
    obi = catalogue["opentelemetry-ebpf-instrumentation"]
    limits = " ".join(obi["avoid_when"])
    assert obi["maturity"] != "established"
    assert "development-stage" in obi["summary"]
    assert "Development" in limits
    assert "v0 minor releases may break" in limits
    assert "explicitly stable signals and attributes" in limits
    assert "v1 release candidate" in limits
    for path in ("VERSIONING.md", "TELEMETRY.md", "SUPPORT_MATRIX.md"):
        assert (
            "https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation"
            f"/blob/main/{path}"
        ) in obi["sources"]


def test_pyroscope_profiles_and_component_grants_are_not_cloud_terms(catalogue):
    tool = catalogue["grafana-pyroscope"]
    assert "ingests, stores and queries" in tool["summary"]
    assert "separate from distributed tracing storage" in tool["summary"]
    assert "https://github.com/grafana/pyroscope/blob/main/LICENSING.md" in set(
        tool["sources"]
    )
    assert "Apache-2.0 component exceptions" in " ".join(tool["avoid_when"])
    assert "Grafana Cloud service terms are separate" in " ".join(tool["avoid_when"])
    assert "saas" not in tool["deployment_models"]
    assert tool["commercial_offering"] is True


def test_mixin_transfer_preserves_former_upstream_and_generation_scope(catalogue):
    tool = catalogue["kubernetes-monitoring-mixins"]
    assert "https://github.com/kubernetes-monitoring/kubernetes-mixin" in set(
        tool["sources"]
    )
    assert tool["deployment_models"] == []
    assert tool["lifecycle_stages"] == ["build", "deploy", "monitor"]
    assert "Jsonnet monitoring mixin" in tool["summary"]
    assert "not kube-prometheus itself" in " ".join(tool["avoid_when"])
    assert "Kubernetes version alone does not prove" in " ".join(tool["avoid_when"])


def test_blackbox_probe_endpoint_is_not_storage_or_availability_guarantee(catalogue):
    tool = catalogue["blackbox-exporter"]
    assert tool["official_url"] == tool["repository_url"]
    assert all(p in tool["summary"] for p in ("HTTP(S)", "DNS", "TCP", "ICMP", "gRPC"))
    limits = " ".join(tool["avoid_when"])
    assert "arbitrary targets" in limits
    assert "individual probes do not guarantee" in limits
    assert "Prometheus storage" in limits
    assert "https://prometheus.io/docs/operating/security/" in tool["sources"]


def test_cortex_keeps_own_upstream_and_external_tenant_authentication(catalogue):
    tool = catalogue["cortex"]
    assert "maintained separately from Grafana Mimir" in tool["summary"]
    assert "object storage" in tool["summary"]
    assert "Authentication and authorization must be configured outside Cortex" in (
        " ".join(tool["avoid_when"])
    )
    assert "https://github.com/cortexproject/cortex/blob/master/GOVERNANCE.md" in set(
        tool["sources"]
    )


def test_victoriametrics_oss_clustering_does_not_grant_enterprise_rights(catalogue):
    tool = catalogue["victoriametrics"]
    assert "Apache-2.0 single-node and cluster" in tool["summary"]
    assert "Clustering is available in OSS" in " ".join(tool["avoid_when"])
    assert "separately licensed Enterprise and Cloud" in tool["summary"]
    assert "MetricsQL/PromQL semantic differences" in " ".join(tool["avoid_when"])
    assert tool["commercial_offering"] is True
    assert "saas" not in tool["deployment_models"]


def test_vector_has_component_specific_traces_and_no_universal_exactly_once(catalogue):
    tool = catalogue["vector"]
    assert "source-transform-sink" in tool["summary"]
    assert "component-specific trace handling" in tool["summary"]
    assert "OTLP source is beta" in " ".join(tool["avoid_when"])
    assert "do not create universal exactly-once" in " ".join(tool["avoid_when"])
    assert "queryable observability storage backend" in " ".join(tool["avoid_when"])


def test_fluentd_event_routing_keeps_fluent_bit_and_plugin_boundaries(catalogue):
    tool = catalogue["fluentd"]
    assert "Ruby-based log-event collector and forwarder" in tool["summary"]
    assert "maintained separately from Fluent Bit" in tool["summary"]
    limits = " ".join(tool["avoid_when"])
    assert "memory or file buffers" in limits
    assert "independently supplied plugins" in limits
    assert "persistent log-query database" in limits


def test_telegraf_stages_and_mit_agent_are_not_enterprise_or_database(catalogue):
    tool = catalogue["telegraf"]
    assert "input, processor, aggregator and output" in " ".join(tool["use_when"])
    assert "InfluxDB or other backends" in tool["summary"]
    assert "distinct from a time-series database" in tool["summary"]
    assert "Telegraf Enterprise" in " ".join(tool["avoid_when"])
    assert "InfluxDB Cloud/Enterprise" in " ".join(tool["avoid_when"])
    assert tool["commercial_offering"] is True


def test_report_rationale_describes_each_records_actual_workflow(report):
    workflow_terms = {
        "grafana-beyla": "Beyla instruments running processes",
        "opentelemetry-ebpf-instrumentation": "OBI observes executing user-space",
        "grafana-pyroscope": "Profile collection and analysis",
        "kubernetes-monitoring-mixins": "Jsonnet generation belongs to build",
        "blackbox-exporter": "Endpoint probes produce metrics",
        "cortex": "Cortex ingests, retains and queries",
        "victoriametrics": "VictoriaMetrics persists and queries",
        "vector": "Agent/aggregator collection, VRL transforms",
        "fluentd": "Input, route, buffer and output",
        "telegraf": "input/processor/aggregator/output pipeline",
    }
    repos = {tool_id: repository for tool_id, repository, _, _ in LICENCES}
    for tool_id, term in workflow_terms.items():
        section = report.split(f"### {tool_id}\n", 1)[1].split("\n### ", 1)[0]
        rows = {
            line.split(" | ")[0].removeprefix("| ").strip("`"): line
            for line in section.splitlines()
            if line.startswith("| `")
        }
        assert term in rows["lifecycle_stages"]
        assert repos[tool_id] in rows["repository_archived"]
