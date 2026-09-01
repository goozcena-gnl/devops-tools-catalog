from __future__ import annotations

import subprocess
import tomllib
from pathlib import Path

from scripts.catalog import load_tools

ROOT = Path(__file__).resolve().parents[1]
PYPROJECT = ROOT / "pyproject.toml"
CHANGELOG = ROOT / "CHANGELOG.md"
RELEASE_NOTES = ROOT / "docs/releases/v0.4.0-notes.md"
HISTORICAL_NOTES = ROOT / "docs/releases/v0.3.0-notes.md"


def test_v040_project_version_and_release_metadata_exist() -> None:
    project = tomllib.loads(PYPROJECT.read_text(encoding="utf-8"))
    changelog = CHANGELOG.read_text(encoding="utf-8")
    notes = RELEASE_NOTES.read_text(encoding="utf-8")

    assert project["project"]["version"] == "0.4.0"
    assert "## [0.4.0] - 2026-08-29" in changelog
    assert notes.startswith("# DevOps Tools Catalogue v0.4.0")


def test_v040_advertised_catalogue_growth_matches_canonical_data() -> None:
    assert len(load_tools(ROOT)) == 1305
    for text in (
        CHANGELOG.read_text(encoding="utf-8"),
        RELEASE_NOTES.read_text(encoding="utf-8"),
    ):
        assert "1,229" in text
        assert "1,285" in text
        assert "56" in text


def test_v040_metadata_preserves_historical_v030_release() -> None:
    result = subprocess.run(
        ["git", "show", "v0.3.0:pyproject.toml"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    historical_project = tomllib.loads(result.stdout)
    historical_notes = HISTORICAL_NOTES.read_text(encoding="utf-8")

    assert historical_project["project"]["version"] == "0.3.0"
    assert historical_notes.startswith("# DevOps Tools Catalogue v0.3.0")
    assert "1,229 canonical records" in historical_notes


def test_v040_metadata_does_not_claim_publication() -> None:
    changelog = CHANGELOG.read_text(encoding="utf-8").lower()
    notes = RELEASE_NOTES.read_text(encoding="utf-8").lower()
    combined = f"{changelog}\n{notes}"
    prohibited_claims = {
        "v0.4.0 has been published",
        "v0.4.0 tag exists",
        "v0.4.0 github release published",
        "github release is live",
    }
    assert all(claim not in combined for claim in prohibited_claims)
    assert "at v0.4.0 preparation time, no v0.4.0 tag" in changelog
    assert "at release-preparation review time, no v0.4.0 tag" in notes
    assert "owner-approved action" in changelog
    assert "owner-approved action" in notes
