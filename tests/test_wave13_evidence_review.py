"""Kubernetes diagnostic, permission and lifecycle boundaries reviewed in Wave 13."""

import subprocess
from pathlib import Path

import pytest
import yaml

from scripts.catalog import load_tools

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = "data/tools/kubernetes-distributions-operations.yaml"
REPORT = "docs/maintenance/2026-10-16-wave-13-kubernetes-diagnostics-evidence-review.md"
COHORT = (
    "kubeconform",
    "kube-score",
    "popeye",
    "kubectx-kubens",
    "kor",
    "kubectl-ai",
    "kube-hunter",
    "kubesec",
    "kubeplumber",
    "kubeview",
)
LICENCES = (
    ("kubeconform", "yannh/kubeconform", "master", "Apache-2.0"),
    ("kube-score", "zegl/kube-score", "master", "MIT"),
    ("popeye", "derailed/popeye", "master", "Apache-2.0"),
    ("kubectx-kubens", "ahmetb/kubectx", "master", "Apache-2.0"),
    ("kor", "yonahd/kor", "main", "MIT"),
    ("kubectl-ai", "GoogleCloudPlatform/kubectl-ai", "main", "Apache-2.0"),
    ("kube-hunter", "aquasecurity/kube-hunter", "main", "Apache-2.0"),
    ("kubesec", "controlplaneio/kubesec", "master", "Apache-2.0"),
    ("kubeplumber", "David-VTUK/KubePlumber", "main", "Apache-2.0"),
    ("kubeview", "benc-uk/kubeview", "main", "MIT"),
)


@pytest.fixture(scope="module")
def catalogue():
    return {tool["id"]: tool for tool in load_tools()}


@pytest.fixture(scope="module")
def report():
    return (ROOT / REPORT).read_text(encoding="utf-8")


def limits(tool):
    return " ".join(tool["avoid_when"])


def test_report_accounts_for_all_240_canonical_field_decisions(report):
    sections = {
        line.removeprefix("### ")
        for line in report.splitlines()
        if line.startswith("### ")
    }
    assert len(set(COHORT)) == 10
    assert sections == set(COHORT)
    total = 0
    all_fields = set()
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
        total += len(fields)
    assert total == 240
    assert len(all_fields) == 24


def test_wave13_changes_only_its_fixed_existing_canonical_cohort():
    base = subprocess.run(
        ["git", "merge-base", "HEAD", "origin/main"],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if base.returncode:
        pytest.skip("Wave 13 scope check requires the local main ref")
    base_sha = base.stdout.strip()
    present = subprocess.run(
        ["git", "cat-file", "-e", f"{base_sha}:{REPORT}"],
        cwd=ROOT,
        capture_output=True,
    )
    if present.returncode == 0:
        pytest.skip(
            "Wave 13 is already in the base; later reviews have their own scope"
        )
    files = subprocess.check_output(
        ["git", "diff", "--name-only", base_sha, "--", "data/tools"],
        cwd=ROOT,
        text=True,
    ).splitlines()
    assert files == [CANONICAL]
    old = yaml.safe_load(
        subprocess.check_output(["git", "show", f"{base_sha}:{CANONICAL}"], cwd=ROOT)
    )
    old = {tool["id"]: tool for tool in old}
    new = {
        tool["id"]: tool
        for tool in yaml.safe_load((ROOT / CANONICAL).read_text(encoding="utf-8"))
    }
    assert old.keys() == new.keys()
    assert {key for key in old if old[key] != new[key]} == set(COHORT)
    for tool_id in COHORT:
        assert set(old[tool_id]["sources"]) <= set(new[tool_id]["sources"])


@pytest.mark.parametrize("tool_id", COHORT)
def test_status_flags_and_documentation_match_review_disposition(catalogue, tool_id):
    tool = catalogue[tool_id]
    retained = tool_id == "kube-hunter"
    assert tool["needs_review"] is retained
    assert tool["status"] == ("needs-review" if retained else "active")
    assert tool["repository_archived"] is False
    assert tool["categories"] == ["kubernetes-distributions-operations"]
    assert tool["documentation_url"] in tool["sources"]


@pytest.mark.parametrize(("tool_id", "repo", "branch", "spdx"), LICENCES)
def test_licence_grant_is_backed_by_the_actual_upstream_file(
    catalogue, tool_id, repo, branch, spdx
):
    tool = catalogue[tool_id]
    assert tool["repository_url"] == f"https://github.com/{repo}"
    assert tool["license_model"] == "oss"
    assert tool["license_spdx"] == spdx
    assert f"https://github.com/{repo}/blob/{branch}/LICENSE" in tool["sources"]


def test_schema_validation_and_reliability_recommendations_are_distinct(catalogue):
    conform = catalogue["kubeconform"]
    score = catalogue["kube-score"]
    assert "JSON schemas" in conform["summary"]
    assert "offline validation requires" in limits(conform)
    assert "Custom resources are not in the default" in limits(conform)
    assert "controller-side semantic validation" in limits(conform)
    assert "recommend" in score["summary"]
    assert "kubeconform schema validation" in limits(score)
    assert "Kubesec" in limits(score)


def test_kubesec_scoring_keeps_hosted_data_and_admission_boundaries(catalogue):
    tool = catalogue["kubesec"]
    assert "risk scoring" in tool["summary"]
    assert "Do not submit sensitive YAML" in limits(tool)
    assert "separate integration" in limits(tool)
    assert "v1 API is deprecated" in limits(tool)
    assert "saas" in tool["deployment_models"]


def test_popeye_live_read_only_lint_has_explicit_version_limits(catalogue):
    tool = catalogue["popeye"]
    assert "Read-only" in tool["summary"]
    assert "live-cluster linter" in tool["summary"]
    assert "metrics-server" in tool["summary"]
    assert "not kube-hunter" in limits(tool)
    assert "Kubernetes 1.25.X" in limits(tool)
    assert "get/list permissions" in limits(tool)


def test_companion_context_tools_do_not_grant_rbac(catalogue):
    tool = catalogue["kubectx-kubens"]
    assert "kubectx and kubens" in tool["summary"]
    assert "does not authenticate" in limits(tool)
    assert "RBAC" in limits(tool)
    assert "client-side convenience" in limits(tool)


def test_kor_false_positives_and_optional_deletion_are_visible(catalogue):
    tool = catalogue["kor"]
    assert "optionally deletes" in tool["summary"]
    assert "false positives" in limits(tool)
    assert "--delete" in limits(tool) and "--no-interactive" in limits(tool)
    assert "write permissions" in limits(tool)
    assert tool["commercial_offering"] is True
    assert "https://korpro.io/pricing" in tool["sources"]
    assert "saas" not in tool["deployment_models"]


def test_ai_model_data_costs_and_cluster_permissions_are_independent(catalogue):
    tool = catalogue["kubectl-ai"]
    assert "GoogleCloudPlatform" in tool["repository_url"]
    assert "local or hosted" in tool["summary"]
    assert "not an officially supported Google product" in limits(tool)
    assert "model context" in limits(tool)
    assert "billing" in limits(tool)
    assert "Kubernetes credentials" in limits(tool)


def test_ai_confirmation_is_not_a_sandbox_or_mcp_authentication(catalogue):
    tool = catalogue["kubectl-ai"]
    assert "modifying or unknown" in limits(tool)
    assert "--skip-permissions" in limits(tool)
    assert "unauthenticated by default" in limits(tool)
    assert "not" in limits(tool) and "security sandbox" in limits(tool)
    assert any(s.endswith("/pkg/agent/conversation.go") for s in tool["sources"])


def test_hunter_retains_unknown_current_support_despite_unarchived_repo(catalogue):
    tool = catalogue["kube-hunter"]
    assert tool["needs_review"] is True
    assert tool["maturity"] == "unknown"
    assert "no longer under active development" in tool["summary"]
    assert "Trivy" in tool["summary"]
    assert "--active" in limits(tool)
    assert "authorized" in limits(tool)
    assert "closed-source plugin" in limits(tool)


def test_plumber_runs_mutating_workloads_with_bounded_platform_evidence(catalogue):
    tool = catalogue["kubeplumber"]
    assert "creates test workloads" in tool["summary"]
    assert "not read-only" in limits(tool)
    assert "pods/exec" in limits(tool)
    assert "host networking" in limits(tool)
    assert "K3d/K3s" in limits(tool)
    assert "not every CNI" in limits(tool)
    assert any(
        s.endswith("/internal/cleanup/removeTestResources.go") for s in tool["sources"]
    )


def test_visualization_is_not_authorization_or_monitoring_storage(catalogue):
    tool = catalogue["kubeview"]
    assert "SSE" in tool["summary"]
    assert "does not enforce user authentication or authorization" in limits(tool)
    assert "Secrets" in limits(tool) and "pod logs" in limits(tool)
    assert "monitoring storage backend" in limits(tool)
    assert any(s.endswith("/templates/service-account.yaml") for s in tool["sources"])


def test_all_historical_sources_remain_and_no_duplicate_id_is_created(catalogue):
    assert len(COHORT) == len(set(COHORT))
    for tool_id in COHORT:
        assert any(
            source.startswith("legacy:") for source in catalogue[tool_id]["sources"]
        )


def test_maturity_decisions_do_not_erase_upstream_limitations(catalogue):
    assert catalogue["kubectl-ai"]["maturity"] == "emerging"
    assert catalogue["kubeplumber"]["maturity"] == "emerging"
    assert catalogue["popeye"]["maturity"] == "growing"
    assert catalogue["kube-hunter"]["maturity"] == "unknown"


def test_report_has_record_specific_workflow_and_lifecycle_rationales(report):
    workflow_terms = {
        "kubeconform": "build",
        "kube-score": "build",
        "popeye": "live",
        "kubectx-kubens": "context",
        "kor": "cleanup",
        "kubectl-ai": "credential",
        "kube-hunter": "assessment",
        "kubesec": "scores",
        "kubeplumber": "temporary",
        "kubeview": "live",
    }
    for tool_id in COHORT:
        section = report.split(f"### {tool_id}\n", 1)[1].split("\n### ", 1)[0]
        fields = {
            line.split(" | ")[0].removeprefix("| ").strip("`"): line
            for line in section.splitlines()
            if line.startswith("| `")
        }
        assert "primary" in fields["license_spdx"]
        assert "https://" in fields["repository_archived"]
        assert "not" in fields["repository_archived"]
        assert workflow_terms[tool_id] in fields["lifecycle_stages"]
