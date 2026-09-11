from __future__ import annotations

import subprocess
import tomllib
from pathlib import Path

from scripts.catalog import load_tools

ROOT = Path(__file__).resolve().parents[1]
PYPROJECT = ROOT / "pyproject.toml"
CHANGELOG = ROOT / "CHANGELOG.md"
RELEASE_NOTES = ROOT / "docs/releases/v0.5.0-notes.md"
V040_NOTES = ROOT / "docs/releases/v0.4.0-notes.md"


def git_show(path: str, tag: str = "v0.4.0") -> str:
    return subprocess.run(
        ["git", "show", f"{tag}:{path}"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def test_v050_project_version_and_release_metadata_exist() -> None:
    project = tomllib.loads(PYPROJECT.read_text(encoding="utf-8"))
    changelog = CHANGELOG.read_text(encoding="utf-8")
    notes = RELEASE_NOTES.read_text(encoding="utf-8")

    assert project["project"]["version"] == "0.5.0"
    assert "## [0.5.0] - 2026-09-11" in changelog
    assert notes.startswith("# DevOps Tools Catalogue v0.5.0")


def test_v050_catalogue_cardinality_and_advertised_growth() -> None:
    tools = load_tools(ROOT)
    assert len(tools) == len({tool["id"] for tool in tools}) == 1423
    for text in (
        CHANGELOG.read_text(encoding="utf-8"),
        RELEASE_NOTES.read_text(encoding="utf-8"),
    ):
        assert "1,285" in text
        assert "1,423" in text
        assert "138" in text


def test_v050_preserves_immutable_v040_version_and_notes() -> None:
    historical_project = tomllib.loads(git_show("pyproject.toml"))
    historical_notes = git_show("docs/releases/v0.4.0-notes.md")

    assert historical_project["project"]["version"] == "0.4.0"
    assert historical_notes.startswith("# DevOps Tools Catalogue v0.4.0")
    assert "1,285 canonical records" in historical_notes
    assert V040_NOTES.read_text(encoding="utf-8") == historical_notes


def test_v050_preserves_v040_changelog_entry() -> None:
    current = CHANGELOG.read_text(encoding="utf-8")
    historical = git_show("CHANGELOG.md")
    historical_v040 = historical[historical.index("## [0.4.0]") :]

    assert current.endswith(historical_v040)


def test_v050_metadata_does_not_claim_publication() -> None:
    changelog = CHANGELOG.read_text(encoding="utf-8").lower()
    v050_changelog = changelog[: changelog.index("## [0.4.0]")]
    notes = RELEASE_NOTES.read_text(encoding="utf-8").lower()
    combined = f"{v050_changelog}\n{notes}"
    prohibited_claims = {
        "v0.5.0 has been published",
        "v0.5.0 tag exists",
        "github release v0.5.0 has been published",
        "github release v0.5.0 is live",
    }

    assert all(claim not in combined for claim in prohibited_claims)
    assert "no v0.5.0 tag or github release had been created" in combined
    assert "separate owner-approved action" in combined
