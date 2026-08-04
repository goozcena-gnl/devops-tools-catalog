from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC_NOTES = ROOT / "docs" / "releases" / "v0.2.0-notes.md"
INTERNAL_DRAFT = ROOT / "docs" / "releases" / "v0.2.0-draft.md"
CHANGELOG = ROOT / "CHANGELOG.md"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_public_notes_are_public_only() -> None:
    text = _read(PUBLIC_NOTES)

    assert text.startswith("# DevOps Tools Catalogue v0.2.0")
    assert "- [ ]" not in text
    assert "```bash" not in text
    assert "DO NOT RUN DURING THIS PR" not in text
    assert "Issue #2 remains open" in text


def test_internal_draft_references_public_notes_file() -> None:
    text = _read(INTERNAL_DRAFT)

    assert "Public GitHub Release notes source: docs/releases/v0.2.0-notes.md" in text
    assert "--notes-file docs/releases/v0.2.0-notes.md" in text


def test_changelog_v020_remains_unreleased_draft() -> None:
    text = _read(CHANGELOG)

    assert "## [0.2.0] - Draft" in text
    assert "Publication metadata finalized on 2026-08-04" in text
