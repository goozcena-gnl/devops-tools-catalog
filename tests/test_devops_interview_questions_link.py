from __future__ import annotations

import csv
from pathlib import Path

from scripts.catalog import load_tools


def test_interview_questions_identity_and_provenance() -> None:
    root = Path(__file__).resolve().parents[1]
    matches = [
        tool for tool in load_tools(root) if tool["id"] == "devops-interview-questions"
    ]
    assert len(matches) == 1
    tool = matches[0]
    repository = "https://github.com/rohitg00/devops-interview-questions"
    historical_url = "https://interview.devopscommunity.in/"
    assert tool["official_url"] == tool["repository_url"] == repository
    assert tool["documentation_url"] == f"{repository}/blob/main/README.md"
    assert tool["repository_archived"] is False
    for field in ("official_url", "repository_url", "documentation_url"):
        assert tool.get(field, "").rstrip("/") != historical_url.rstrip("/")
    assert tool["license_model"] == "documentation"
    assert not tool.get("license_spdx")
    assert tool["status"] == "needs-review"
    assert tool["needs_review"] is True

    with (root / "migration/reconciliation.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = [
            row
            for row in csv.DictReader(handle)
            if row["canonical_id"] == "devops-interview-questions"
        ]
    assert {(row["source_file"], row["line"], row["disposition"]) for row in rows} == {
        ("devopstools_final.md", "128", "kept"),
        ("1_Foundational-Skills/README.md", "48", "merged"),
    }
    assert all(row["source_url"] == historical_url for row in rows)
    assert historical_url in tool["sources"]
    assert {f"legacy:{row['source_file']}#L{row['line']}" for row in rows} <= set(
        tool["sources"]
    )
