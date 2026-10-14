"""IaC identity, distribution licence and execution boundaries reviewed in Wave 11."""

from pathlib import Path

import pytest

from scripts.catalog import load_tools

COHORT = (
    "azure-verified-modules-avm",
    "tflint",
    "terraform-docs",
    "terraform-plugin-docs",
    "terrateam",
    "opentaco",
    "score",
    "tofu-controller",
    "flux-operator",
    "gitops-bridge",
)


@pytest.fixture(scope="module")
def catalogue():
    return {tool["id"]: tool for tool in load_tools()}


def test_cohort_contains_exactly_ten_existing_ids(catalogue):
    assert len(COHORT) == len(set(COHORT)) == 10
    assert set(COHORT) <= catalogue.keys()
    report = (
        Path(__file__).resolve().parents[1]
        / "docs/maintenance/2026-10-13-wave-11-iac-gitops-evidence-review.md"
    ).read_text(encoding="utf-8")
    sections = {
        line.removeprefix("### ")
        for line in report.splitlines()
        if line.startswith("### ")
    }
    assert sections == set(COHORT)


@pytest.mark.parametrize("tool_id", COHORT)
def test_review_status_is_consistent_and_provenance_retained(catalogue, tool_id):
    tool = catalogue[tool_id]
    assert tool["needs_review"] == (tool["status"] == "needs-review")
    assert tool["documentation_url"] in tool["sources"]
    assert any(source.startswith("legacy:") for source in tool["sources"])


@pytest.mark.parametrize(
    ("tool_id", "repository", "branch", "model", "spdx"),
    [
        (
            "azure-verified-modules-avm",
            "Azure/Azure-Verified-Modules",
            "main",
            "oss",
            "MIT",
        ),
        (
            "tflint",
            "terraform-linters/tflint",
            "master",
            "source-available",
            "MPL-2.0 AND BUSL-1.1",
        ),
        ("terraform-docs", "terraform-docs/terraform-docs", "master", "oss", "MIT"),
        (
            "terraform-plugin-docs",
            "hashicorp/terraform-plugin-docs",
            "main",
            "oss",
            "MPL-2.0",
        ),
        ("terrateam", "stategraph/stategraph", "main", "open-core", "MPL-2.0"),
        ("opentaco", "diggerhq/digger", "develop", "open-core", "MIT AND Apache-2.0"),
        ("score", "score-spec/spec", "main", "oss", "Apache-2.0"),
        ("tofu-controller", "flux-iac/tofu-controller", "main", "oss", "Apache-2.0"),
        (
            "flux-operator",
            "controlplaneio-fluxcd/flux-operator",
            "main",
            "oss",
            "AGPL-3.0",
        ),
        (
            "gitops-bridge",
            "gitops-bridge-dev/gitops-bridge",
            "main",
            "oss",
            "Apache-2.0",
        ),
    ],
)
def test_distribution_licences_have_project_specific_evidence(
    catalogue, tool_id, repository, branch, model, spdx
):
    tool = catalogue[tool_id]
    assert tool["repository_url"] == f"https://github.com/{repository}"
    assert tool["license_model"] == model
    assert tool["license_spdx"] == spdx
    assert f"https://github.com/{repository}/blob/{branch}/LICENSE" in tool["sources"]


def test_avm_umbrella_has_no_independent_deployment(catalogue):
    tool = catalogue["azure-verified-modules-avm"]
    assert tool["deployment_models"] == []
    assert all(
        term in tool["summary"]
        for term in ("standards", "indexes", "separate module repositories")
    )
    assert "every indexed implementation" in " ".join(tool["avoid_when"])


def test_tflint_binary_and_external_plugin_licences_are_distinct(catalogue):
    tool = catalogue["tflint"]
    assert (
        "https://github.com/terraform-linters/tflint/blob/master/LICENSE-BUSL"
        in tool["sources"]
    )
    assert "external plugins have separate licences" in tool["summary"]
    assert tool["deployment_models"] == []
    assert all(
        term in " ".join(tool["avoid_when"])
        for term in ("plan/apply", "security testing", "OpenTofu")
    )


def test_module_and_provider_documentation_have_separate_identities(catalogue):
    module, provider = catalogue["terraform-docs"], catalogue["terraform-plugin-docs"]
    assert module["repository_url"] != provider["repository_url"]
    assert "module documentation" in module["summary"]
    assert "provider/plugin documentation" in provider["summary"]
    assert module["license_spdx"] != provider["license_spdx"]
    assert "schema extraction builds the provider" in " ".join(provider["avoid_when"])
    assert module["deployment_models"] == provider["deployment_models"] == []


def test_terrateam_continuation_preserves_history_and_edition_boundaries(catalogue):
    tool = catalogue["terrateam"]
    assert "formerly Terrateam" in tool["name"]
    assert {
        "https://github.com/terrateamio/terrateam",
        "https://terrateam.io",
        "https://stategraph.com/about",
    } <= set(tool["sources"])
    assert tool["deployment_models"] == ["self-hosted", "saas"]
    assert tool["commercial_offering"] is True
    assert all(
        term in tool["summary"]
        for term in ("CI runners", "Enterprise", "Infrastructure as a Database")
    )


def test_opentaco_rebrand_does_not_erase_component_licences(catalogue):
    tool = catalogue["opentaco"]
    assert tool["name"] == "OpenTaco"
    assert "renamed Digger" in tool["summary"]
    assert all(
        f"https://github.com/diggerhq/digger/blob/develop/{path}" in tool["sources"]
        for path in ("backend/LICENSE", "ee/LICENSE")
    )
    assert "backend server" in " ".join(tool["avoid_when"])
    assert "beta remote runs" in tool["summary"]
    assert tool["maturity"] == "growing"


def test_score_specification_does_not_execute_its_implementations(catalogue):
    tool = catalogue["score"]
    assert tool["deployment_models"] == []
    assert all(
        term in tool["summary"]
        for term in (
            "specification",
            "separate implementations",
            "not a Kubernetes deployment platform",
        )
    )
    assert "all implementations support the same" in " ".join(tool["avoid_when"])


def test_flux_related_controllers_have_distinct_execution_and_licences(catalogue):
    tofu, operator = catalogue["tofu-controller"], catalogue["flux-operator"]
    assert tofu["repository_url"] != operator["repository_url"]
    assert tofu["license_spdx"] != operator["license_spdx"]
    assert tofu["deployment_models"] == operator["deployment_models"] == ["self-hosted"]
    assert "runner Pods" in tofu["summary"]
    assert "state Secrets" in " ".join(tofu["avoid_when"])
    assert "FluxInstance" in operator["summary"]
    assert "Flux CD core" in " ".join(operator["avoid_when"])


def test_gitops_bridge_keeps_precise_maintenance_review_debt(catalogue):
    tool = catalogue["gitops-bridge"]
    assert tool["needs_review"] is True
    assert tool["status"] == "needs-review"
    assert tool["maturity"] == "unknown"
    assert tool["repository_archived"] is False
    assert tool["deployment_models"] == []
    assert "pattern and example repository" in tool["summary"]
    assert "Flux integration is listed as in progress" in tool["summary"]
    assert "verify present maintenance" in " ".join(tool["avoid_when"])


def test_evidence_report_uses_record_specific_workflow_and_provenance_rationale():
    report = (
        Path(__file__).resolve().parents[1]
        / "docs/maintenance/2026-10-13-wave-11-iac-gitops-evidence-review.md"
    ).read_text(encoding="utf-8")
    workflows = {
        "azure-verified-modules-avm": "central index does not execute deployments",
        "tflint": "static checks",
        "terraform-docs": "module reference preparation",
        "terraform-plugin-docs": "provider documentation generation",
        "terrateam": "separate CI runners",
        "opentaco": "beta remote runs",
        "score": "specification itself does not execute",
        "tofu-controller": "runner execution",
        "flux-operator": "FluxInstance",
        "gitops-bridge": "no independent deployment runtime",
    }
    for tool_id, scope in workflows.items():
        section = report.split(f"### {tool_id}\n", 1)[1].split("\n### ", 1)[0]
        rows = {
            line.split(" | ")[0].removeprefix("| ").strip("`"): line
            for line in section.splitlines()
            if line.startswith("| `")
        }
        assert scope in rows["lifecycle_stages"]
        if tool_id != "gitops-bridge":
            assert "GitOps Bridge" not in rows["repository_archived"]
        if tool_id != "terrateam":
            assert "terrateam.io" not in rows["sources"]
