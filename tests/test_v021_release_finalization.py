from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
PYPROJECT = ROOT / "pyproject.toml"
CHANGELOG = ROOT / "CHANGELOG.md"
PUBLIC_NOTES = ROOT / "docs" / "releases" / "v0.2.1-notes.md"
INTERNAL_DRAFT = ROOT / "docs" / "releases" / "v0.2.1-draft.md"
COMPLETION = ROOT / "docs" / "maintenance" / "v0.2.1-remediation-completion.md"

FINALIZATION_BASELINE_SHA = "e04412ebfb85118d33a2f9bc584a44b8f2334259"
FINALIZATION_RESULT_SHA = "9f1c6e9f13acf954cffa57ff9a7f0275314af4fa"

ALLOWED_CHANGED_FILES = {
    "pyproject.toml",
    "CHANGELOG.md",
    "docs/releases/v0.2.1-notes.md",
    "docs/releases/v0.2.1-draft.md",
    "docs/maintenance/v0.2.1-remediation-completion.md",
    "tests/test_v021_release_finalization.py",
    "tests/test_v021_url_remediation_batch_c2.py",
    "tests/test_v021_license_lifecycle_remediation_batch_d.py",
}

PROTECTED_PATHS = [
    "data/tools",
    "docs/maintenance/v0.2.1-url-remediation-plan.md",
    "docs/maintenance/v0.2.1-url-remediation-plan.csv",
    "docs/maintenance/v0.2.1-url-remediation-batch-a1-review.md",
    "docs/maintenance/v0.2.1-url-remediation-batch-a2-review.md",
    "docs/maintenance/v0.2.1-url-remediation-batch-b-review.md",
    "docs/maintenance/v0.2.1-url-remediation-batch-c1-review.md",
    "docs/maintenance/v0.2.1-url-remediation-batch-c2-review.md",
    "docs/maintenance/v0.2.1-license-lifecycle-remediation-batch-d-review.md",
    "reports/link-report.json",
    "reports/link-report.md",
    "docs/link-review-ledger.md",
    "schema",
    "scripts",
    "config",
    ".github/workflows",
]

MISSING_REF_CI_MESSAGE_FRAGMENT = "is not reachable in this GitHub Actions checkout"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _require_finalization_refs() -> None:
    refs = [
        ("baseline", FINALIZATION_BASELINE_SHA),
        ("result", FINALIZATION_RESULT_SHA),
    ]

    for label, sha in refs:
        try:
            subprocess.run(
                ["git", "cat-file", "-e", f"{sha}^{{commit}}"],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=True,
            )
        except FileNotFoundError as exc:
            raise AssertionError(
                "Git executable is required for finalization pinned baseline/result invariants"
            ) from exc
        except subprocess.CalledProcessError as exc:
            if os.getenv("GITHUB_ACTIONS") == "true":
                raise AssertionError(
                    f"{label.capitalize()} commit {sha} is not reachable in this "
                    "GitHub Actions checkout, so finalization pinned baseline/result "
                    "invariants cannot be enforced. Required refs: "
                    f"{FINALIZATION_BASELINE_SHA} -> {FINALIZATION_RESULT_SHA}. "
                    "Verify .github/workflows/quality.yml checkout uses fetch-depth: 0."
                ) from exc

            pytest.skip(
                f"{label.capitalize()} commit {sha} is not reachable in this local "
                "shallow/partial clone; skipping finalization pinned baseline/result "
                f"invariants ({FINALIZATION_BASELINE_SHA} -> {FINALIZATION_RESULT_SHA})"
            )


def _finalization_changed_files(*paths: str) -> set[str]:
    _require_finalization_refs()

    cmd = [
        "git",
        "diff",
        "--name-only",
        FINALIZATION_BASELINE_SHA,
        FINALIZATION_RESULT_SHA,
        "--",
        *paths,
    ]
    result = subprocess.run(
        cmd,
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


def test_pyproject_version_is_021() -> None:
    text = _read(PYPROJECT)
    assert 'version = "0.2.1"' in text


def test_changelog_has_v021_draft_and_not_published_claim() -> None:
    text = _read(CHANGELOG)
    assert "## [0.2.1] - Draft" in text
    assert "v0.2.1 tag created" not in text.lower()
    assert "v0.2.1 github release published" not in text.lower()


def test_public_notes_are_public_only() -> None:
    text = _read(PUBLIC_NOTES)
    assert text.startswith("# DevOps Tools Catalogue v0.2.1")
    assert "- [ ]" not in text
    assert "```bash" not in text
    assert "DO NOT RUN" not in text
    assert "internal publication" not in text.lower()


def test_internal_runbook_references_public_notes() -> None:
    text = _read(INTERNAL_DRAFT)
    assert "docs/releases/v0.2.1-notes.md" in text
    assert "--notes-file docs/releases/v0.2.1-notes.md" in text


def test_completion_report_core_totals_and_issue_state() -> None:
    text = _read(COMPLETION)
    required = [
        "TOTAL_PLANNED_ROWS: 80",
        "TOTAL_REVIEWED_ROWS: 80",
        "TOTAL_UNIQUE_IDS: 73",
        "TOTAL_CHANGED_CANONICAL_IDS: 10",
        "TOTAL_CHANGED_CANONICAL_FIELDS: 10",
        "TOTAL_REVIEWED_BUT_UNCHANGED_IDS: 63",
        "UNREVIEWED_ROWS: 0",
        "DUPLICATE_UNEXPECTED_ROWS: 0",
        "MACHINE_API_REPLACEMENT_CANDIDATES: 0",
        "Issue #2 remains open.",
    ]
    for needle in required:
        assert needle in text


def test_completion_report_lists_all_ten_changes() -> None:
    text = _read(COMPLETION)
    for needle in (
        "deeptutor.official_url",
        "odysseus.official_url",
        "terraform-cloud.official_url",
        "trivy.documentation_url",
        "yokecd.repository_url",
        "cdktf.needs_review: true -> false",
        "kaniko.needs_review: true -> false",
        "keptn.needs_review: true -> false",
        "kubeapps.needs_review: true -> false",
        "tnu.needs_review: true -> false",
    ):
        assert needle in text


def test_public_notes_do_not_claim_full_evidence_debt_resolution() -> None:
    text = _read(PUBLIC_NOTES).lower()
    assert "all evidence debt is resolved" not in text


def test_finalization_pr_changed_file_scope_is_limited() -> None:
    changed = _finalization_changed_files(".")
    assert changed == ALLOWED_CHANGED_FILES


def test_no_protected_paths_modified_by_finalization_pr() -> None:
    changed = _finalization_changed_files(*PROTECTED_PATHS)
    assert changed == set()


def test_finalization_refs_missing_baseline_in_ci_fails_actionably(
    monkeypatch: object,
) -> None:
    monkeypatch.setenv("GITHUB_ACTIONS", "true")

    def _side_effect(args: list[str], **kwargs: object) -> subprocess.CompletedProcess:
        if (
            args[:3] == ["git", "cat-file", "-e"]
            and args[3] == f"{FINALIZATION_BASELINE_SHA}^{{commit}}"
        ):
            raise subprocess.CalledProcessError(128, args, stderr="not a valid object")
        return subprocess.CompletedProcess(args, 0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", _side_effect)

    with pytest.raises(AssertionError) as exc_info:
        _require_finalization_refs()

    text = str(exc_info.value)
    assert FINALIZATION_BASELINE_SHA in text
    assert FINALIZATION_RESULT_SHA in text
    assert "fetch-depth: 0" in text


def test_finalization_refs_missing_result_in_ci_fails_actionably(
    monkeypatch: object,
) -> None:
    monkeypatch.setenv("GITHUB_ACTIONS", "true")

    def _side_effect(args: list[str], **kwargs: object) -> subprocess.CompletedProcess:
        if (
            args[:3] == ["git", "cat-file", "-e"]
            and args[3] == f"{FINALIZATION_RESULT_SHA}^{{commit}}"
        ):
            raise subprocess.CalledProcessError(128, args, stderr="not a valid object")
        return subprocess.CompletedProcess(args, 0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", _side_effect)

    with pytest.raises(AssertionError) as exc_info:
        _require_finalization_refs()

    text = str(exc_info.value)
    assert FINALIZATION_BASELINE_SHA in text
    assert FINALIZATION_RESULT_SHA in text
    assert "fetch-depth: 0" in text


def test_scope_parity_test_does_not_intercept_ci_missing_baseline(
    monkeypatch: object,
) -> None:
    monkeypatch.setenv("GITHUB_ACTIONS", "true")

    def _side_effect(args: list[str], **kwargs: object) -> subprocess.CompletedProcess:
        if (
            args[:3] == ["git", "cat-file", "-e"]
            and args[3] == f"{FINALIZATION_BASELINE_SHA}^{{commit}}"
        ):
            raise subprocess.CalledProcessError(128, args, stderr="not a valid object")
        return subprocess.CompletedProcess(args, 0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", _side_effect)

    with pytest.raises(
        AssertionError,
        match=MISSING_REF_CI_MESSAGE_FRAGMENT,
    ):
        test_finalization_pr_changed_file_scope_is_limited()


def test_protected_path_parity_test_does_not_intercept_ci_missing_result(
    monkeypatch: object,
) -> None:
    monkeypatch.setenv("GITHUB_ACTIONS", "true")

    def _side_effect(args: list[str], **kwargs: object) -> subprocess.CompletedProcess:
        if (
            args[:3] == ["git", "cat-file", "-e"]
            and args[3] == f"{FINALIZATION_RESULT_SHA}^{{commit}}"
        ):
            raise subprocess.CalledProcessError(128, args, stderr="not a valid object")
        return subprocess.CompletedProcess(args, 0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", _side_effect)

    with pytest.raises(
        AssertionError,
        match=MISSING_REF_CI_MESSAGE_FRAGMENT,
    ):
        test_no_protected_paths_modified_by_finalization_pr()


def test_ci_missing_ref_match_rejects_unrelated_assertion_text() -> None:
    with (
        pytest.raises(
            AssertionError,
            match="Regex pattern did not match",
        ),
        pytest.raises(
            AssertionError,
            match=MISSING_REF_CI_MESSAGE_FRAGMENT,
        ),
    ):
        raise AssertionError("Unrelated assertion text")


def test_finalization_refs_missing_result_local_skips(monkeypatch: object) -> None:
    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)

    def _side_effect(args: list[str], **kwargs: object) -> subprocess.CompletedProcess:
        if (
            args[:3] == ["git", "cat-file", "-e"]
            and args[3] == f"{FINALIZATION_RESULT_SHA}^{{commit}}"
        ):
            raise subprocess.CalledProcessError(128, args, stderr="not a valid object")
        return subprocess.CompletedProcess(args, 0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", _side_effect)

    with pytest.raises(pytest.skip.Exception) as exc_info:
        _require_finalization_refs()

    text = str(exc_info.value)
    assert FINALIZATION_BASELINE_SHA in text
    assert FINALIZATION_RESULT_SHA in text
    assert "shallow/partial clone" in text


def test_finalization_diff_uses_explicit_two_commit_range(monkeypatch: object) -> None:
    captured: list[list[str]] = []

    def _side_effect(args: list[str], **kwargs: object) -> subprocess.CompletedProcess:
        captured.append(list(args))
        if args[:3] == ["git", "cat-file", "-e"]:
            return subprocess.CompletedProcess(args, 0, stdout="", stderr="")
        if args[:3] == ["git", "diff", "--name-only"]:
            return subprocess.CompletedProcess(
                args,
                0,
                stdout="\n".join(sorted(ALLOWED_CHANGED_FILES)) + "\n",
                stderr="",
            )
        raise AssertionError(f"Unexpected command: {args}")

    monkeypatch.setattr(subprocess, "run", _side_effect)

    changed = _finalization_changed_files(".")
    assert changed == ALLOWED_CHANGED_FILES

    diff_calls = [
        cmd
        for cmd in captured
        if len(cmd) >= 3 and cmd[:3] == ["git", "diff", "--name-only"]
    ]
    assert diff_calls, "Expected git diff command"

    cmd = diff_calls[0]
    assert cmd[3] == FINALIZATION_BASELINE_SHA
    assert cmd[4] == FINALIZATION_RESULT_SHA
    assert "HEAD" not in cmd
    assert not [arg for arg in cmd if "..." in arg]
    assert not [called for called in captured if called[:2] == ["git", "status"]]


def test_finalization_protected_path_parity_uses_pinned_refs(
    monkeypatch: object,
) -> None:
    captured: list[list[str]] = []

    def _side_effect(args: list[str], **kwargs: object) -> subprocess.CompletedProcess:
        captured.append(list(args))
        if args[:3] == ["git", "cat-file", "-e"]:
            return subprocess.CompletedProcess(args, 0, stdout="", stderr="")
        if args[:3] == ["git", "diff", "--name-only"]:
            return subprocess.CompletedProcess(args, 0, stdout="", stderr="")
        raise AssertionError(f"Unexpected command: {args}")

    monkeypatch.setattr(subprocess, "run", _side_effect)

    changed = _finalization_changed_files(*PROTECTED_PATHS)
    assert changed == set()

    diff_calls = [
        cmd
        for cmd in captured
        if len(cmd) >= 3 and cmd[:3] == ["git", "diff", "--name-only"]
    ]
    assert diff_calls, "Expected git diff command"
    cmd = diff_calls[0]
    assert cmd[3] == FINALIZATION_BASELINE_SHA
    assert cmd[4] == FINALIZATION_RESULT_SHA
    assert "HEAD" not in cmd


def test_finalization_helper_subprocess_failure_propagates(monkeypatch: object) -> None:
    def _side_effect(args: list[str], **kwargs: object) -> subprocess.CompletedProcess:
        if args[:3] == ["git", "cat-file", "-e"]:
            return subprocess.CompletedProcess(args, 0, stdout="", stderr="")
        if args[:3] == ["git", "diff", "--name-only"]:
            raise subprocess.CalledProcessError(2, args, stderr="bad diff")
        raise AssertionError(f"Unexpected command: {args}")

    monkeypatch.setattr(subprocess, "run", _side_effect)

    with pytest.raises(subprocess.CalledProcessError):
        _finalization_changed_files(".")
