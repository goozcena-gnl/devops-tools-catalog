from __future__ import annotations

import subprocess
from collections import Counter
from copy import deepcopy
from pathlib import Path
from typing import Any

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/maintenance/v0.2.2-carryover-execution-manifest.yaml"
LEDGER = ROOT / "docs/maintenance/v0.2.2-n2b-hard-url-review.md"

N2B_EXECUTION_BASELINE_SHA = "1c4c3a72ef863cba819c580bdffc69c34c70ca37"
# N2b accepted every selected canonical value unchanged. Keep the durable
# baseline as the accepted result instead of a branch-only evidence commit.
N2B_ACCEPTED_CANONICAL_SHA = N2B_EXECUTION_BASELINE_SHA
N2B_CURRENT_MAIN_REF = "origin/main"

EXPECTED_SCOPE = {
    ("microsoft-azure", "official_url"): (
        "data/tools/cloud-platforms-management.yaml",
        "https://azure.microsoft.com",
    ),
    ("soos-dast", "official_url"): (
        "data/tools/application-cloud-security.yaml",
        "https://hub.docker.com/r/soosio/dast",
    ),
    ("yotascale", "official_url"): (
        "data/tools/finops-sustainability.yaml",
        "https://www.yotascale.com",
    ),
}
EXPECTED_IDS = {tool_id for tool_id, _field in EXPECTED_SCOPE}
EXPECTED_WORK_ITEMS = set(EXPECTED_SCOPE)
REQUIRED_LEDGER_COLUMNS = {
    "tool_id",
    "affected_field",
    "canonical_yaml_file",
    "previous_value",
    "final_value",
    "v021_previous_decision",
    "fresh_network_observation",
    "authoritative_evidence",
    "inference",
    "final_decision",
    "canonical_changed",
    "unresolved_boundary",
}


def _manifest_rows() -> list[dict[str, Any]]:
    payload = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    return [row for row in payload["work_items"] if row["execution_sub_batch"] == "N2b"]


def _parse_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _ledger_rows(path: Path = LEDGER) -> list[dict[str, str]]:
    assert path.exists(), f"Missing N2b review ledger: {path}"
    lines = path.read_text(encoding="utf-8").splitlines()
    header_index = next(
        (
            index
            for index, line in enumerate(lines)
            if line.startswith("|")
            and {"tool_id", "final_decision"} <= set(_parse_cells(line))
        ),
        None,
    )
    assert header_index is not None, f"No N2b evidence table header in {path}"
    headers = _parse_cells(lines[header_index])
    missing = REQUIRED_LEDGER_COLUMNS - set(headers)
    assert not missing, f"N2b ledger is missing columns: {sorted(missing)}"

    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for line_number, line in enumerate(
        lines[header_index + 2 :], start=header_index + 3
    ):
        if not line.startswith("|"):
            if rows:
                break
            continue
        cells = _parse_cells(line)
        assert len(cells) == len(headers), (
            f"{path}:{line_number}: expected {len(headers)} cells, got {len(cells)}"
        )
        row = dict(zip(headers, cells, strict=True))
        key = (row["tool_id"], row["affected_field"])
        assert key not in seen, f"{path}:{line_number}: duplicate work item {key}"
        seen.add(key)
        rows.append(row)
    return rows


def _git(*args: str) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            capture_output=True,
            encoding="utf-8",
            check=True,
        )
    except FileNotFoundError as exc:
        raise AssertionError("Git is required for N2b pinned-range invariants") from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or str(exc)).strip()
        raise AssertionError(
            "N2b pinned-range invariant failed for explicit refs "
            f"{N2B_EXECUTION_BASELINE_SHA} -> {N2B_ACCEPTED_CANONICAL_SHA}: {detail}"
        ) from exc
    return result.stdout


def _require_refs() -> None:
    for sha in (N2B_EXECUTION_BASELINE_SHA, N2B_ACCEPTED_CANONICAL_SHA):
        _git("cat-file", "-e", f"{sha}^{{commit}}")


def _changed_canonical_files() -> set[str]:
    _require_refs()
    output = _git(
        "diff",
        "--name-only",
        N2B_EXECUTION_BASELINE_SHA,
        N2B_ACCEPTED_CANONICAL_SHA,
        "--",
        "data/tools/",
    )
    return set(output.splitlines())


def _records_at(revision: str) -> dict[str, tuple[str, dict[str, Any]]]:
    paths = _git("ls-tree", "-r", "--name-only", revision, "--", "data/tools/")
    records: dict[str, tuple[str, dict[str, Any]]] = {}
    for path in sorted(line for line in paths.splitlines() if line.endswith(".yaml")):
        payload = yaml.safe_load(_git("show", f"{revision}:{path}"))
        for record in payload:
            tool_id = record["id"]
            assert tool_id not in records
            records[tool_id] = (path, record)
    return records


def _current_records() -> dict[str, tuple[str, dict[str, Any]]]:
    records: dict[str, tuple[str, dict[str, Any]]] = {}
    for path in sorted((ROOT / "data/tools").glob("*.yaml")):
        relative = path.relative_to(ROOT).as_posix()
        for record in yaml.safe_load(path.read_text(encoding="utf-8")):
            tool_id = record["id"]
            assert tool_id not in records
            records[tool_id] = (relative, record)
    return records


def _assert_n2b_owned_values(
    current: dict[str, tuple[str, dict[str, Any]]],
    accepted: dict[str, tuple[str, dict[str, Any]]],
) -> None:
    for (tool_id, field), (expected_path, expected_value) in EXPECTED_SCOPE.items():
        assert tool_id in current, f"Current catalogue lost N2b ID {tool_id!r}"
        assert tool_id in accepted, f"N2b result is missing selected ID {tool_id!r}"
        current_path, current_record = current[tool_id]
        accepted_path, accepted_record = accepted[tool_id]
        assert current_path == accepted_path == expected_path
        assert accepted_record.get(field) == expected_value
        assert current_record.get(field) == expected_value, (
            f"N2b-owned field drifted for {(tool_id, field)}"
        )


def test_n2b_frozen_selector_is_exact() -> None:
    rows = _manifest_rows()
    assert len(rows) == 3
    assert [row["sequence_number"] for row in rows] == [57, 58, 59]
    assert {row["tool_id"] for row in rows} == EXPECTED_IDS
    assert {(row["tool_id"], row["affected_field"]) for row in rows} == (
        EXPECTED_WORK_ITEMS
    )
    assert Counter(row["tool_id"] for row in rows).most_common(1)[0][1] == 1


def test_n2b_manifest_scope_matches_expected_values() -> None:
    for row in _manifest_rows():
        expected_path, expected_value = EXPECTED_SCOPE[
            (row["tool_id"], row["affected_field"])
        ]
        assert row["canonical_yaml_file"] == expected_path
        assert row["current_value"] == expected_value
        assert row["affected_field"] == "official_url"


def test_n2b_ledger_exactly_covers_scope_and_current_values() -> None:
    rows = _ledger_rows()
    current = _current_records()
    assert len(rows) == 3
    assert {(row["tool_id"], row["affected_field"]) for row in rows} == (
        EXPECTED_WORK_ITEMS
    )
    for row in rows:
        key = (row["tool_id"], row["affected_field"])
        expected_path, expected_value = EXPECTED_SCOPE[key]
        assert row["canonical_yaml_file"] == current[row["tool_id"]][0] == expected_path
        assert row["previous_value"] == row["final_value"] == expected_value
        assert current[row["tool_id"]][1][row["affected_field"]] == expected_value
        assert row["v021_previous_decision"] == "reviewed-but-unchanged in v0.2.1"
        assert row["final_decision"] == "retain current value"
        assert row["canonical_changed"] == "no"
        assert "2026-08-12" in row["fresh_network_observation"]
        assert "https://" in row["authoritative_evidence"]
        assert row["inference"].lower().startswith(("primary source", "primary-source"))
        assert row["unresolved_boundary"]


def test_n2b_historical_result_is_explicitly_zero_delta() -> None:
    assert N2B_ACCEPTED_CANONICAL_SHA == N2B_EXECUTION_BASELINE_SHA
    assert _changed_canonical_files() == set()
    _git(
        "merge-base", "--is-ancestor", N2B_EXECUTION_BASELINE_SHA, N2B_CURRENT_MAIN_REF
    )


def test_n2b_selected_ids_and_owned_values_are_preserved() -> None:
    baseline = _records_at(N2B_EXECUTION_BASELINE_SHA)
    current = _current_records()
    assert baseline.keys() >= EXPECTED_IDS
    assert current.keys() >= EXPECTED_IDS
    _assert_n2b_owned_values(current, baseline)


def test_n2b_unrelated_future_change_does_not_invalidate_history() -> None:
    accepted = _records_at(N2B_ACCEPTED_CANONICAL_SHA)
    future = deepcopy(accepted)
    unrelated_id = next(tool_id for tool_id in future if tool_id not in EXPECTED_IDS)
    future[unrelated_id][1]["summary"] = "Later authorized unrelated change."
    _assert_n2b_owned_values(future, accepted)


def test_n2b_owned_url_drift_invalidates_history() -> None:
    accepted = _records_at(N2B_ACCEPTED_CANONICAL_SHA)
    future = deepcopy(accepted)
    tool_id, field = next(iter(sorted(EXPECTED_WORK_ITEMS)))
    future[tool_id][1][field] = "https://example.invalid/drift"
    with pytest.raises(AssertionError, match="N2b-owned field drifted"):
        _assert_n2b_owned_values(future, accepted)


def test_n2b_later_non_owned_metadata_evolution_does_not_invalidate_history() -> None:
    accepted = _records_at(N2B_ACCEPTED_CANONICAL_SHA)
    future = deepcopy(accepted)
    tool_id, _field = next(iter(sorted(EXPECTED_WORK_ITEMS)))
    selected = future[tool_id][1]
    selected["status"] = "active"
    selected["needs_review"] = False
    selected["license_model"] = "commercial"
    selected["license_spdx"] = "LicenseRef-later-review"
    selected["repository_url"] = "https://example.com/later-authorized-repository"
    _assert_n2b_owned_values(future, accepted)


def test_n2b_selected_urls_remain_strings() -> None:
    current = _current_records()
    for tool_id, field in EXPECTED_WORK_ITEMS:
        assert isinstance(current[tool_id][1][field], str)


def test_n2b_ledger_records_persistent_baseline_and_totals() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    assert f"Execution baseline SHA: `{N2B_EXECUTION_BASELINE_SHA}`" in text
    assert f"Accepted canonical result SHA: `{N2B_ACCEPTED_CANONICAL_SHA}`" in text
    assert "No branch-only commit is used as an executable historical ref" in text
    assert "Canonical baseline/result delta: `0` files, `0` IDs, `0` fields" in text
    for expected in (
        "SELECTED_MANIFEST_ROWS: 3",
        "REVIEWED_MANIFEST_ROWS: 3",
        "UNREVIEWED_MANIFEST_ROWS: 0",
        "SELECTED_UNIQUE_IDS: 3",
        "DUPLICATE_SELECTED_IDS: 0",
        "TOTAL_CHANGED_CANONICAL_IDS: 0",
        "TOTAL_CHANGED_CANONICAL_FIELDS: 0",
        "REVIEWED_BUT_UNCHANGED_IDS: 3",
        "NON_SELECTED_CHANGED_IDS: 0",
        "LOST_IDS: 0",
        "NEW_IDS: 0",
        "MACHINE_API_REPLACEMENT_CANDIDATES: 0",
    ):
        assert expected in text


def test_n2b_missing_ref_is_actionable(monkeypatch: Any) -> None:
    def fail(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        raise subprocess.CalledProcessError(128, args[0], stderr="missing object")

    monkeypatch.setattr(subprocess, "run", fail)
    try:
        _require_refs()
        raise AssertionError("Expected missing pinned ref to fail")
    except AssertionError as exc:
        assert N2B_EXECUTION_BASELINE_SHA in str(exc)
        assert "missing object" in str(exc)


def test_n2b_git_unavailable_is_actionable(monkeypatch: Any) -> None:
    def fail(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        raise FileNotFoundError("git missing")

    monkeypatch.setattr(subprocess, "run", fail)
    try:
        _require_refs()
        raise AssertionError("Expected missing Git to fail")
    except AssertionError as exc:
        assert "Git is required" in str(exc)


def test_n2b_historical_diff_uses_two_explicit_commits(monkeypatch: Any) -> None:
    commands: list[list[str]] = []

    def record(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        command = list(args[0])
        commands.append(command)
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", record)
    _changed_canonical_files()
    diff = next(command for command in commands if command[:2] == ["git", "diff"])
    baseline_index = diff.index(N2B_EXECUTION_BASELINE_SHA)
    assert diff[baseline_index + 1] == N2B_ACCEPTED_CANONICAL_SHA
    assert "HEAD" not in diff
    assert not any("..." in argument for argument in diff)


def test_n2b_ledger_parser_rejects_malformed_rows(tmp_path: Path) -> None:
    path = tmp_path / "bad.md"
    path.write_text(
        "| tool_id | final_decision |\n|---|---|\n| only-one-cell |\n",
        encoding="utf-8",
    )
    try:
        _ledger_rows(path)
        raise AssertionError("Expected malformed ledger to fail")
    except AssertionError as exc:
        assert "missing columns" in str(exc) or "expected" in str(exc)
