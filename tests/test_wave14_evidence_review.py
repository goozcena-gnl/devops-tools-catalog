"""CI/CD product, source, licence and execution boundaries verified in Wave 14."""

import subprocess
from pathlib import Path

import pytest
import yaml

from scripts.catalog import load_tools

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = "data/tools/ci-build-testing.yaml"
REPORT = "docs/maintenance/2026-10-16-wave-14-cicd-platforms-evidence-review.md"
COHORT = (
    "github-actions",
    "gitlab-ci",
    "jenkins",
    "jenkins-x",
    "gocd",
    "woodpecker-ci",
    "onedev",
    "devtron",
    "nektos-act",
    "semaphore-ci",
)
CORE_LICENCES = (
    ("jenkins", "MIT", "jenkinsci/jenkins/blob/master/LICENSE.txt"),
    ("jenkins-x", "Apache-2.0", "jenkins-x/jx/blob/main/LICENSE"),
    ("gocd", "Apache-2.0", "gocd/gocd/blob/master/LICENSE"),
    ("woodpecker-ci", "Apache-2.0", "woodpecker-ci/woodpecker/blob/main/LICENSE"),
    ("onedev", "MIT", "theonedev/onedev/blob/main/license.txt"),
    ("devtron", "Apache-2.0", "devtron-labs/devtron/blob/main/LICENSE"),
    ("nektos-act", "MIT", "nektos/act/blob/master/LICENSE"),
)


@pytest.fixture(scope="module")
def catalogue():
    return {tool["id"]: tool for tool in load_tools()}


@pytest.fixture(scope="module")
def report():
    return (ROOT / REPORT).read_text(encoding="utf-8")


def test_report_has_240_unique_field_decisions_and_ten_dispositions(report):
    assert {line[4:] for line in report.splitlines() if line.startswith("### ")} == set(
        COHORT
    )
    fields = set()
    count = 0
    for tool_id in COHORT:
        section = report.split(f"### {tool_id}\n", 1)[1].split("\n### ", 1)[0]
        section = section.split("\n## ", 1)[0]
        rows = [line for line in section.splitlines() if line.startswith("| `")]
        names = [line.split(" | ")[0].removeprefix("| ").strip("`") for line in rows]
        assert len(names) == len(set(names)) == 24
        assert all(
            "](https://" in line and ("CHANGED." in line or "UNCHANGED." in line)
            for line in rows
        )
        assert "**Disposition: CLEAR REVIEW.**" in section
        fields.update(names)
        count += len(names)
    assert len(fields) == 24 and count == 240


def test_wave14_changes_exactly_its_existing_canonical_cohort():
    result = subprocess.run(
        ["git", "merge-base", "HEAD", "origin/main"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        pytest.skip("Wave 14 scope check requires the main ref")
    base = result.stdout.strip()
    merged = subprocess.run(
        ["git", "cat-file", "-e", f"{base}:{REPORT}"],
        cwd=ROOT,
        capture_output=True,
        check=False,
    )
    if merged.returncode == 0:
        pytest.skip("Wave 14 is already in the base; later work has its own scope")
    paths = subprocess.check_output(
        ["git", "diff", "--name-only", base, "--", "data/tools"],
        cwd=ROOT,
        text=True,
    ).splitlines()
    assert paths == [CANONICAL]
    before = yaml.safe_load(
        subprocess.check_output(["git", "show", f"{base}:{CANONICAL}"], cwd=ROOT)
    )
    after = yaml.safe_load((ROOT / CANONICAL).read_text(encoding="utf-8"))
    before = {t["id"]: t for t in before}
    after = {t["id"]: t for t in after}
    assert before.keys() == after.keys()
    assert {i for i in before if before[i] != after[i]} == set(COHORT)
    for tool_id in COHORT:
        assert set(before[tool_id]["sources"]) <= set(after[tool_id]["sources"])
        for field in (
            "id",
            "categories",
            "subcategories",
            "roles",
            "alternatives",
            "tags",
        ):
            assert before[tool_id].get(field) == after[tool_id].get(field)


@pytest.mark.parametrize("tool_id", COHORT)
def test_reviewed_identity_docs_and_consistent_disposition(catalogue, tool_id):
    tool = catalogue[tool_id]
    assert tool["status"] == "active" and tool["needs_review"] is False
    assert tool["maturity"] in {"growing", "established"}
    assert tool["documentation_url"] in tool["sources"]
    assert tool["categories"] == ["ci-build-testing"]
    assert tool["use_when"] and tool["avoid_when"] and tool["deployment_models"]


@pytest.mark.parametrize(("tool_id", "spdx", "path"), CORE_LICENCES)
def test_core_spdx_has_actual_licence_source_and_scoped_summary(
    catalogue, tool_id, spdx, path
):
    tool = catalogue[tool_id]
    assert tool["license_spdx"] == spdx
    assert f"https://github.com/{path}" in tool["sources"]
    assert spdx in tool["summary"]


@pytest.mark.parametrize(
    ("tool_id", "model"),
    [
        ("github-actions", "commercial"),
        ("gitlab-ci", "open-core"),
        ("semaphore-ci", "open-core"),
    ],
)
def test_platform_has_no_invented_universal_spdx(catalogue, tool_id, model):
    tool = catalogue[tool_id]
    assert tool["license_model"] == model
    assert "license_spdx" not in tool
    assert tool["commercial_offering"] is True


def test_github_product_page_is_not_a_runner_repository(catalogue):
    tool = catalogue["github-actions"]
    assert "repository_url" not in tool and "repository_archived" not in tool
    assert tool["official_url"] == "https://github.com/features/actions"
    assert "https://github.com/actions/runner/blob/main/LICENSE" in tool["sources"]
    assert "self-hosted-agent" in tool["deployment_models"]


def test_gitlab_application_source_is_not_runner_or_all_saas(catalogue):
    tool = catalogue["gitlab-ci"]
    assert "repository_url" not in tool and "repository_archived" not in tool
    assert "https://gitlab.com/gitlab-org/gitlab" in tool["sources"]
    assert "separately deployed GitLab Runner" in tool["summary"]
    assert (
        "https://gitlab.com/gitlab-org/gitlab/-/blob/master/ee/LICENSE"
        in tool["sources"]
    )


def test_github_enterprise_control_plane_is_separate_from_job_execution(catalogue):
    tool = catalogue["github-actions"]
    assert {"hosted-saas", "enterprise-self-hosted", "self-hosted-agent"} <= set(
        tool["deployment_models"]
    )
    assert any("/enterprise-server@" in url for url in tool["sources"])
    assert "GitHub Enterprise Server" in tool["summary"]
    assert any(
        "GitHub-hosted runners for GitHub Enterprise Server" in text
        and "require self-hosted runners" in text
        for text in tool["avoid_when"]
    )


def test_gitlab_free_self_managed_is_not_hidden_by_enterprise_filter(catalogue):
    tool = catalogue["gitlab-ci"]
    assert {"self-hosted", "enterprise-self-hosted", "self-hosted-agent"} <= set(
        tool["deployment_models"]
    )
    assert "https://docs.gitlab.com/install/package/" in tool["sources"]
    assert "free Community" in " ".join(tool["use_when"])
    assert "repository_url" not in tool


def test_jenkins_x_rename_preserves_id_and_independent_licensing(catalogue):
    tool = catalogue["jenkins-x"]
    assert "JayeX" in tool["name"] and "Jenkins X" in tool["name"]
    assert tool["repository_url"] == "https://github.com/jenkins-x/jx"
    assert tool["official_url"] == "https://jayex.io/"
    assert "https://cd.foundation/blog/2026/04/16/announcing-jayex/" in tool["sources"]
    assert "Tekton" in tool["summary"] and "Lighthouse" in tool["summary"]


def test_onedev_canonical_source_and_enterprise_exclusion(catalogue):
    tool = catalogue["onedev"]
    assert tool["repository_url"] == "https://code.onedev.io/onedev/server"
    assert "repository_archived" not in tool
    assert tool["license_model"] == "open-core" and tool["commercial_offering"]
    assert "https://onedev.io/license-agreement" in tool["sources"]
    assert "https://github.com/theonedev/onedev" in tool["sources"]


def test_devtron_core_is_separate_from_commercial_and_argo(catalogue):
    tool = catalogue["devtron"]
    assert tool["repository_url"] == "https://github.com/devtron-labs/devtron"
    assert tool["license_model"] == "open-core" and tool["commercial_offering"]
    assert "https://devtron.ai/pricing" in tool["sources"]
    assert "Argo CD" in " ".join(tool["avoid_when"]) or "GitOps" in tool["summary"]


def test_semaphore_successor_does_not_license_the_service(catalogue):
    tool = catalogue["semaphore-ci"]
    assert tool["repository_url"] == "https://github.com/semaphoreio/semaphore"
    assert tool["repository_archived"] is False
    assert (
        "https://github.com/semaphoreci/semaphore/blob/main/README.md"
        in tool["sources"]
    )
    assert (
        "https://github.com/semaphoreio/semaphore/blob/main/ee/LICENSE"
        in tool["sources"]
    )
    assert "outside ee/" in tool["summary"]
    assert {"hosted-saas", "self-hosted", "enterprise-self-hosted"} <= set(
        tool["deployment_models"]
    )


@pytest.mark.parametrize(
    ("tool_id", "terms"),
    [
        ("github-actions", ("untrusted", "tokens", "self-hosted")),
        ("gitlab-ci", ("variables", "runners", "protected")),
        ("jenkins", ("controller", "credentials", "isolation")),
        ("jenkins-x", ("deprecated", "kubernetes", "secret")),
        ("gocd", ("security", "most recent release")),
        ("woodpecker-ci", ("local execution", "privileged", "secrets")),
        ("onedev", ("shell executors", "authorization", "enterprise")),
        ("devtron", ("kubernetes", "rbac", "credentials")),
        ("nektos-act", ("compatibility", "oidc", "docker socket")),
        ("semaphore-ci", ("archived", "cloud", "isolation")),
    ],
)
def test_security_and_compatibility_limits_are_not_erased(catalogue, tool_id, terms):
    text = " ".join(catalogue[tool_id]["avoid_when"]).lower()
    assert all(term in text for term in terms)
