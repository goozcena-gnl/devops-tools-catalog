from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "maintenance" / "v0.2.2-carryover-execution-manifest.yaml"

EXPECTED_SOURCE_SHA = "dc7cfd457a7c9638b1132048792092c8b5e3ae02"
EXPECTED_UNIQUE_IDS = 63
EXPECTED_FIELD_ROWS = 82


def _read_manifest() -> dict:
    assert MANIFEST.exists(), f"Missing manifest: {MANIFEST}"
    payload = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    assert isinstance(payload, dict), "Manifest must be a YAML mapping"
    return payload


def test_manifest_header_and_source_sha() -> None:
    m = _read_manifest()
    assert m["manifest_version"] == 1
    assert m["source_release"] == "v0.2.1"
    assert m["source_main_sha"] == EXPECTED_SOURCE_SHA
    assert m["scope_policy"] == "reviewed_but_unchanged_carryover_only"
    assert m["excluded_global_needs_review_population"] is True


def test_work_item_scope_counts_and_uniques() -> None:
    m = _read_manifest()
    rows = m["work_items"]
    assert len(rows) == EXPECTED_FIELD_ROWS

    ids = {r["tool_id"] for r in rows}
    assert len(ids) == EXPECTED_UNIQUE_IDS

    by_stream = Counter(r["logical_workstream"] for r in rows)
    assert by_stream == Counter({"N1": 35, "N2": 24, "N3": 5, "N4": 18})

    unique_by_stream = {
        s: len({r["tool_id"] for r in rows if r["logical_workstream"] == s})
        for s in ("N1", "N2", "N3", "N4")
    }
    assert unique_by_stream == {"N1": 30, "N2": 23, "N3": 5, "N4": 5}


def test_executable_sub_batches_are_bounded_and_cover_non_hold_scope() -> None:
    m = _read_manifest()
    rows = m["work_items"]

    sub_batches = m["execution_sub_batches"]
    ids_by_sub_batch = {b["id"]: set(b["tool_ids"]) for b in sub_batches}

    for batch in sub_batches:
        assert batch["unique_ids"] == len(set(batch["tool_ids"]))
        assert batch["unique_ids"] <= 20

    executable_ids = set().union(*ids_by_sub_batch.values())
    non_hold_ids = {r["tool_id"] for r in rows if r["logical_workstream"] != "N4"}
    assert executable_ids == non_hold_ids

    hold_rows = [r for r in rows if r["logical_workstream"] == "N4"]
    assert hold_rows
    assert all(r["execution_sub_batch"] == "HOLD" for r in hold_rows)


def test_sub_batch_ownership_is_single_and_deterministic() -> None:
    m = _read_manifest()
    rows = m["work_items"]

    ownership: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        if row["logical_workstream"] == "N4":
            continue
        ownership[row["tool_id"]].add(row["execution_sub_batch"])

    for tool_id, owned in ownership.items():
        assert len(owned) == 1, f"{tool_id} has multiple execution sub-batches: {owned}"


def test_multi_field_ids_match_expected() -> None:
    m = _read_manifest()
    rows = m["work_items"]
    count = Counter(r["tool_id"] for r in rows)
    actual = sorted([k for k, v in count.items() if v > 1])
    expected = sorted(
        [
            "ansible-lint",
            "argo-workflows",
            "argocd",
            "argocd-image-updater",
            "argocd-vault-plugin",
            "autopwn-suite",
            "cai-robotsec",
            "ctop",
            "elastic-apm-server",
            "elastic-stack-elk",
            "hoji-ai",
        ]
    )
    assert actual == expected


def test_hold_register_matches_n4_rows() -> None:
    m = _read_manifest()
    rows = m["work_items"]
    hold = m["hold_register"]
    assert len(hold) == 1
    entry = hold[0]

    n4_ids = sorted({r["tool_id"] for r in rows if r["logical_workstream"] == "N4"})
    assert sorted(entry["tool_ids"]) == n4_ids
    assert entry["row_count"] == sum(1 for r in rows if r["logical_workstream"] == "N4")
