"""Every reconciled legacy occurrence must remain traceable in its canonical record."""

from __future__ import annotations

import csv
import json
import subprocess
from collections import Counter

import pytest
import yaml

from scripts.catalog import ROOT, load_tools

RESTORATION_BASE = "81e3774dc31589a7f19991645cbf5b6ed676a266"
REPAIRED_IDS = {
    "pangolin",
    "plumber",
    "floci",
    "mcp-server-kubernetes",
    "opnsense",
    "xcp-ng",
    "gitea",
    "knative",
    "kubescape",
    "parrot-security",
    "haproxy-data-plane-api",
    "yokecd",
}


def reconciliation_rows() -> list[dict[str, str]]:
    with (ROOT / "migration/reconciliation.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        return list(csv.DictReader(handle))


def legacy_pointer(row: dict[str, str]) -> str:
    return f"legacy:{row['source_file']}#L{row['line']}"


def assert_provenance(tools: list[dict], rows: list[dict[str, str]]) -> None:
    counts = Counter(tool["id"] for tool in tools)
    duplicates = {tool_id: count for tool_id, count in counts.items() if count != 1}
    assert not duplicates, f"Duplicate canonical IDs: {duplicates}"
    by_id = {tool["id"]: tool for tool in tools}
    for row in rows:
        tool_id = row["canonical_id"]
        pointer = legacy_pointer(row)
        assert tool_id in by_id, f"Unresolved canonical ID {tool_id}: {pointer}"
        assert pointer in by_id[tool_id]["sources"], f"{tool_id}: missing {pointer}"


@pytest.fixture(scope="module")
def catalogue() -> list[dict]:
    return load_tools()


def test_every_reconciled_occurrence_has_exact_canonical_provenance(catalogue) -> None:
    assert_provenance(catalogue, reconciliation_rows())


def test_reconciliation_accounting_matches_every_original_occurrence(catalogue) -> None:
    rows = reconciliation_rows()
    original = json.loads((ROOT / "migration/source-entries.json").read_text("utf-8"))
    row_keys = Counter((row["source_file"], int(row["line"])) for row in rows)
    original_keys = Counter((row["source_file"], row["line"]) for row in original)
    assert len(rows) == len(original) == 1894
    assert row_keys == original_keys
    assert all(count == 1 for count in row_keys.values())
    assert Counter(row["disposition"] for row in rows) == {
        "kept": 1085,
        "merged": 802,
        "archived": 7,
    }
    assert len(catalogue) == len({tool["id"] for tool in catalogue}) == 1305


def test_restoration_closes_exact_historical_twenty_pointer_gap(catalogue) -> None:
    # Pin the pre-restoration history, not HEAD, so later unrelated work is allowed.
    baseline = {}
    paths = subprocess.check_output(
        ["git", "ls-tree", "-r", "--name-only", RESTORATION_BASE, "data/tools"],
        cwd=ROOT,
        encoding="utf-8",
    ).splitlines()
    for relative in paths:
        if not relative.endswith(".yaml"):
            continue
        content = subprocess.check_output(
            ["git", "show", f"{RESTORATION_BASE}:{relative}"],
            cwd=ROOT,
            encoding="utf-8",
        )
        baseline.update((tool["id"], tool) for tool in yaml.safe_load(content))
    missing = [
        row
        for row in reconciliation_rows()
        if legacy_pointer(row) not in baseline[row["canonical_id"]]["sources"]
    ]
    assert len(missing) == 20
    assert {row["canonical_id"] for row in missing} == REPAIRED_IDS
    assert_provenance(catalogue, missing)
    current = {tool["id"]: tool for tool in catalogue}
    for tool_id in REPAIRED_IDS:
        assert set(baseline[tool_id]["sources"]) <= set(current[tool_id]["sources"])
        assert len(current[tool_id]["sources"]) == len(set(current[tool_id]["sources"]))


def test_each_required_pointer_is_individually_protected(catalogue) -> None:
    by_id = {tool["id"]: tool for tool in catalogue}
    for row in reconciliation_rows():
        tool_id = row["canonical_id"]
        pointer = legacy_pointer(row)
        original = by_id[tool_id]
        # Keep every other source: an arbitrary legacy pointer cannot satisfy this row.
        damaged = {
            **original,
            "sources": [s for s in original["sources"] if s != pointer],
        }
        with pytest.raises(AssertionError) as exc:
            assert_provenance([damaged], [row])
        assert tool_id in str(exc.value)
        assert pointer in str(exc.value)


def test_unresolved_mapping_and_duplicate_ids_are_rejected(catalogue) -> None:
    row = reconciliation_rows()[0]
    tool = next(tool for tool in catalogue if tool["id"] == row["canonical_id"])
    with pytest.raises(AssertionError, match="Unresolved canonical ID"):
        assert_provenance([], [row])
    with pytest.raises(AssertionError, match="Duplicate canonical IDs"):
        assert_provenance([tool, tool], [row])
