from __future__ import annotations

import json
import subprocess
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def git_show(path: str, tag: str = "v0.4.0") -> str:
    return subprocess.run(
        ["git", "show", f"{tag}:{path}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def test_v040_project_version_and_release_metadata_exist() -> None:
    project = tomllib.loads(git_show("pyproject.toml"))
    changelog = git_show("CHANGELOG.md")
    notes = git_show("docs/releases/v0.4.0-notes.md")

    assert project["project"]["version"] == "0.4.0"
    assert "## [0.4.0] - 2026-08-29" in changelog
    assert notes.startswith("# DevOps Tools Catalogue v0.4.0")


def test_v040_advertised_catalogue_growth_matches_canonical_data() -> None:
    statistics = json.loads(git_show("docs/catalog-statistics.json"))
    assert statistics["canonical_records"] == 1285
    for text in (
        git_show("CHANGELOG.md"),
        git_show("docs/releases/v0.4.0-notes.md"),
    ):
        assert "1,229" in text
        assert "1,285" in text
        assert "56" in text


def test_v040_metadata_preserves_historical_v030_release() -> None:
    historical_project = tomllib.loads(git_show("pyproject.toml", "v0.3.0"))
    historical_notes = git_show("docs/releases/v0.3.0-notes.md", "v0.3.0")

    assert historical_project["project"]["version"] == "0.3.0"
    assert historical_notes.startswith("# DevOps Tools Catalogue v0.3.0")
    assert "1,229 canonical records" in historical_notes


def test_v040_metadata_does_not_claim_publication() -> None:
    changelog = git_show("CHANGELOG.md").lower()
    notes = git_show("docs/releases/v0.4.0-notes.md").lower()
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
