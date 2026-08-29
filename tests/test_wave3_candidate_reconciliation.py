from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

from scripts.catalog import load_tools

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/maintenance/2026-08-wave3-candidate-reconciliation.csv"
REQUIRED_COLUMNS = {
    "input_index",
    "input_label",
    "input_url",
    "normalized_input_url",
    "canonical_name",
    "canonical_official_url",
    "canonical_repository_url",
    "existing_catalog_id",
    "decision",
    "resulting_catalog_id",
    "duplicate_of_input_index",
    "categories",
    "license_model",
    "license_spdx",
    "status",
    "needs_review",
    "primary_evidence",
    "notes",
}
EXPECTED_DECISIONS = {
    "ADD": 56,
    "UPDATE_EXISTING": 3,
    "ALREADY_PRESENT_NO_CHANGE": 1,
    "SKIP_DUPLICATE": 1,
    "SKIP_OUT_OF_SCOPE": 1,
}


def _rows() -> list[dict[str, str]]:
    with LEDGER.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def test_wave3_ledger_accounts_for_every_submitted_occurrence() -> None:
    rows = _rows()
    assert len(rows) == 62
    assert set(rows[0]) == REQUIRED_COLUMNS
    assert [int(row["input_index"]) for row in rows] == list(range(1, 63))
    assert Counter(row["decision"] for row in rows) == EXPECTED_DECISIONS


def test_wave3_additions_resolve_to_unique_canonical_records() -> None:
    rows = _rows()
    tools_by_id = {tool["id"]: tool for tool in load_tools(ROOT)}
    added_ids = [
        row["resulting_catalog_id"] for row in rows if row["decision"] == "ADD"
    ]
    assert len(added_ids) == len(set(added_ids)) == 56
    assert set(added_ids) <= set(tools_by_id)
    assert len(tools_by_id) == 1285


def test_wave3_duplicate_and_existing_boundaries_are_explicit() -> None:
    rows = {int(row["input_index"]): row for row in _rows()}
    assert rows[52]["duplicate_of_input_index"] == "51"
    assert rows[52]["resulting_catalog_id"] == "openstack-magnum"
    assert rows[28]["existing_catalog_id"] == "snyk"
    assert rows[40]["existing_catalog_id"] == "civo"
    assert rows[50]["existing_catalog_id"] == "okd"
    assert rows[55]["existing_catalog_id"] == "pulumi"


def test_wave3_submitted_deep_and_tracking_urls_are_normalized() -> None:
    rows = {int(row["input_index"]): row for row in _rows()}
    assert "utm_" not in rows[11]["normalized_input_url"]
    assert not rows[29]["normalized_input_url"].endswith("/tree/main")
    assert rows[39]["normalized_input_url"] == "https://crc.dev/"
