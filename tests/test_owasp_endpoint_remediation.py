from __future__ import annotations

import csv
from pathlib import Path

import pytest

from scripts.catalog import load_tools, load_yaml

ROOT = Path(__file__).resolve().parents[1]
ENDPOINTS = {
    "owasp-docksec": ("docksec", "https://owasp.org/DockSec/", "OWASP/DockSec", "MIT"),
    "owasp-amass": (
        "amass",
        "https://owasp.org/www-project-amass/",
        "owasp-amass/amass",
        "Apache-2.0",
    ),
    "dependencycheck": (
        "dependency-check",
        "https://owasp.org/www-project-dependency-check",
        "dependency-check/DependencyCheck",
        "Apache-2.0",
    ),
}


@pytest.mark.parametrize("tool_id", ENDPOINTS)
def test_owasp_current_endpoints_preserve_identity(tool_id: str) -> None:
    matches = [tool for tool in load_tools(ROOT) if tool["id"] == tool_id]
    assert len(matches) == 1
    tool = matches[0]
    slug, historical, repository, spdx = ENDPOINTS[tool_id]
    assert tool["official_url"] == f"https://owasp.org/projects/{slug}"
    assert tool["repository_url"] == f"https://github.com/{repository}"
    assert tool["license_model"] == "oss"
    assert tool["license_spdx"] == spdx
    assert tool["status"] == "active"
    assert tool["needs_review"] is False
    assert historical in tool["sources"]
    for field in ("official_url", "repository_url", "documentation_url"):
        assert tool.get(field, "").rstrip("/") != historical.rstrip("/")
    aliases = load_yaml(ROOT / "config/import-overrides.yaml")["url_aliases"]
    assert historical not in aliases
    if tool_id == "dependencycheck":
        assert (
            tool["documentation_url"]
            == "https://dependency-check.github.io/DependencyCheck/"
        )
    elif tool_id == "owasp-docksec":
        assert (
            tool["documentation_url"]
            == "https://github.com/OWASP/DockSec/blob/main/README.md"
        )
        assert tool["repository_archived"] is False
    else:
        assert tool["repository_archived"] is False


def test_owasp_historical_occurrences_remain_original() -> None:
    with (ROOT / "migration/reconciliation.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = [
            r for r in csv.DictReader(handle) if r["canonical_id"] == "dependencycheck"
        ]
    assert {(r["source_file"], r["line"], r["disposition"]) for r in rows} == {
        ("devopstools_final.md", "856", "kept"),
        ("6_Security/README.md", "20", "merged"),
    }
    assert all(r["source_url"] == ENDPOINTS["dependencycheck"][1] + "/" for r in rows)
    for name, tool_id in (
        ("2026-08-wave2-candidate-reconciliation.csv", "owasp-amass"),
        ("2026-09-08-wave4-candidate-reconciliation.csv", "owasp-docksec"),
    ):
        with (ROOT / "docs/maintenance" / name).open(
            encoding="utf-8", newline=""
        ) as handle:
            entries = [
                r
                for r in csv.DictReader(handle)
                if r["resulting_catalog_id"] == tool_id
            ]
        assert len(entries) == 1
        assert entries[0]["decision"] == "ADD"
        assert entries[0]["input_url"] == ENDPOINTS[tool_id][1]
        assert entries[0]["canonical_official_url"] == ENDPOINTS[tool_id][1]
