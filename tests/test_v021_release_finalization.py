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


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class _NoPrDiff(RuntimeError):
    pass


def _resolve_base_ref() -> tuple[str, bool]:
    pr_base = os.getenv("GITHUB_BASE_REF", "").strip()
    if pr_base:
        for ref in (f"origin/{pr_base}", pr_base):
            check = subprocess.run(
                ["git", "rev-parse", "--verify", ref],
                cwd=ROOT,
                text=True,
                capture_output=True,
            )
            if check.returncode == 0:
                return ref, True
        raise AssertionError(
            f"Unable to resolve pull_request base ref for GITHUB_BASE_REF={pr_base!r}"
        )

    for ref in ("origin/main", "main"):
        check = subprocess.run(
            ["git", "rev-parse", "--verify", ref],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        if check.returncode == 0:
            return ref, False
    raise AssertionError("Unable to resolve merge-base against main")


def _diff_names(base: str, *paths: str) -> set[str]:
    cmd = ["git", "diff", "--name-only", f"{base}..HEAD", "--", *paths]
    out = subprocess.check_output(cmd, cwd=ROOT, text=True)
    return {line.strip() for line in out.splitlines() if line.strip()}


def _pr_changed_files() -> set[str]:
    base_ref, is_pr_context = _resolve_base_ref()
    merge_base = subprocess.check_output(
        ["git", "merge-base", "HEAD", base_ref], cwd=ROOT, text=True
    ).strip()
    head_sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
    ).strip()

    if not is_pr_context and merge_base == head_sha:
        raise _NoPrDiff(
            "No active PR/file-scope diff in this local post-merge context; "
            "skipping PR-only changed-file scope invariant"
        )

    return _diff_names(merge_base, ".")


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
    try:
        changed = _pr_changed_files()
    except _NoPrDiff as exc:
        pytest.skip(str(exc))
    assert changed == ALLOWED_CHANGED_FILES


def test_no_protected_paths_modified_by_finalization_pr() -> None:
    base_ref, _ = _resolve_base_ref()
    base = subprocess.check_output(
        ["git", "merge-base", "HEAD", base_ref], cwd=ROOT, text=True
    ).strip()
    changed = _diff_names(base, *PROTECTED_PATHS)
    assert changed == set()


def test_finalization_scope_helper_never_uses_git_status(monkeypatch: object) -> None:
    monkeypatch.setenv("GITHUB_BASE_REF", "main")

    def _mock_run(args: list[str], **kwargs: object) -> subprocess.CompletedProcess:
        if args[:3] == ["git", "rev-parse", "--verify"]:
            return subprocess.CompletedProcess(args, 0, stdout="ok\n", stderr="")
        return subprocess.CompletedProcess(args, 0, stdout="", stderr="")

    def _mock_check_output(args: list[str], **kwargs: object) -> str:
        if args[:2] == ["git", "status"]:
            raise AssertionError("git status must not be used")
        if args[:2] == ["git", "merge-base"]:
            return "abc123\n"
        if args[:2] == ["git", "rev-parse"]:
            return "def456\n"
        if args[:3] == ["git", "diff", "--name-only"]:
            return "pyproject.toml\nCHANGELOG.md\n"
        raise AssertionError(f"Unexpected command: {args}")

    monkeypatch.setattr(subprocess, "run", _mock_run)
    monkeypatch.setattr(subprocess, "check_output", _mock_check_output)

    changed = _pr_changed_files()
    assert changed == {"pyproject.toml", "CHANGELOG.md"}


def test_finalization_scope_helper_skips_post_merge_main_context(
    monkeypatch: object,
) -> None:
    monkeypatch.delenv("GITHUB_BASE_REF", raising=False)

    def _mock_run(args: list[str], **kwargs: object) -> subprocess.CompletedProcess:
        if args[:3] == ["git", "rev-parse", "--verify"] and args[-1] in {
            "origin/main",
            "main",
        }:
            return subprocess.CompletedProcess(args, 0, stdout="ok\n", stderr="")
        return subprocess.CompletedProcess(args, 1, stdout="", stderr="")

    def _mock_check_output(args: list[str], **kwargs: object) -> str:
        if args[:2] == ["git", "merge-base"]:
            return "same-sha\n"
        if args[:2] == ["git", "rev-parse"]:
            return "same-sha\n"
        raise AssertionError(f"Unexpected command: {args}")

    monkeypatch.setattr(subprocess, "run", _mock_run)
    monkeypatch.setattr(subprocess, "check_output", _mock_check_output)

    with pytest.raises(_NoPrDiff):
        _pr_changed_files()


def test_finalization_scope_helper_pr_context_enforces_exact_eight_files(
    monkeypatch: object,
) -> None:
    monkeypatch.setenv("GITHUB_BASE_REF", "main")

    expected = sorted(ALLOWED_CHANGED_FILES)

    def _mock_run(args: list[str], **kwargs: object) -> subprocess.CompletedProcess:
        if args[:3] == ["git", "rev-parse", "--verify"]:
            return subprocess.CompletedProcess(args, 0, stdout="ok\n", stderr="")
        return subprocess.CompletedProcess(args, 0, stdout="", stderr="")

    def _mock_check_output(args: list[str], **kwargs: object) -> str:
        if args[:2] == ["git", "merge-base"]:
            return "base-sha\n"
        if args[:2] == ["git", "rev-parse"]:
            return "head-sha\n"
        if args[:3] == ["git", "diff", "--name-only"]:
            return "\n".join(expected) + "\n"
        raise AssertionError(f"Unexpected command: {args}")

    monkeypatch.setattr(subprocess, "run", _mock_run)
    monkeypatch.setattr(subprocess, "check_output", _mock_check_output)

    changed = _pr_changed_files()
    assert changed == ALLOWED_CHANGED_FILES


def test_finalization_scope_helper_does_not_broadly_suppress_exceptions(
    monkeypatch: object,
) -> None:
    monkeypatch.setenv("GITHUB_BASE_REF", "main")

    def _mock_run(args: list[str], **kwargs: object) -> subprocess.CompletedProcess:
        if args[:3] == ["git", "rev-parse", "--verify"]:
            return subprocess.CompletedProcess(args, 0, stdout="ok\n", stderr="")
        return subprocess.CompletedProcess(args, 0, stdout="", stderr="")

    def _mock_check_output(args: list[str], **kwargs: object) -> str:
        if args[:2] == ["git", "merge-base"]:
            return "base-sha\n"
        if args[:2] == ["git", "rev-parse"]:
            return "head-sha\n"
        if args[:3] == ["git", "diff", "--name-only"]:
            raise subprocess.CalledProcessError(2, args, stderr="bad diff")
        raise AssertionError(f"Unexpected command: {args}")

    monkeypatch.setattr(subprocess, "run", _mock_run)
    monkeypatch.setattr(subprocess, "check_output", _mock_check_output)

    with pytest.raises(subprocess.CalledProcessError):
        _pr_changed_files()
