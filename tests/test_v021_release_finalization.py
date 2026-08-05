from __future__ import annotations

import subprocess
from pathlib import Path

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


def _merge_base_ref() -> str:
    for ref in ("origin/main", "main"):
        check = subprocess.run(
            ["git", "rev-parse", "--verify", ref],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        if check.returncode == 0:
            return subprocess.check_output(
                ["git", "merge-base", "HEAD", ref], cwd=ROOT, text=True
            ).strip()
    raise AssertionError("Unable to resolve merge-base against main")


def _diff_names(base: str, *paths: str) -> set[str]:
    cmd = ["git", "diff", "--name-only", f"{base}..HEAD", "--", *paths]
    out = subprocess.check_output(cmd, cwd=ROOT, text=True)
    return {line.strip() for line in out.splitlines() if line.strip()}


def _working_tree_changed_names() -> set[str]:
    out = subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT, text=True)
    changed = set()
    for line in out.splitlines():
        if not line.strip():
            continue
        path = line[3:]
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        changed.add(path.strip())
    return changed


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
    base = _merge_base_ref()
    changed = _diff_names(base, ".")
    if not changed:
        changed = _working_tree_changed_names()
    assert changed == ALLOWED_CHANGED_FILES


def test_no_protected_paths_modified_by_finalization_pr() -> None:
    base = _merge_base_ref()
    changed = _diff_names(base, *PROTECTED_PATHS)
    assert changed == set()
