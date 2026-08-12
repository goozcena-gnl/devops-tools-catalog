from __future__ import annotations

import subprocess
from collections import Counter
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/maintenance/v0.2.2-carryover-execution-manifest.yaml"
LEDGER = ROOT / "docs/maintenance/v0.2.2-n3a-archived-governance-review.md"

N3A_EXECUTION_BASELINE_SHA = "ffa08a2ff3797de9a33235bfcf9853f6c2b6bb04"
N3A_ACCEPTED_DATA_TREE_SHA = "a3da73ad7556badd7cb2176c9336c10df5ba0aca"

EXPECTED_SCOPE = {
    ("grafana-oncall", "repository_url"): (
        "data/tools/deprecated-historical.yaml",
        "https://github.com/grafana/oncall",
        "https://github.com/grafana/oncall",
    ),
    ("juju", "repository_url"): (
        "data/tools/configuration-management.yaml",
        "https://github.com/canonical/juju",
        "https://github.com/juju/juju",
    ),
    ("kubernetes-dashboard", "repository_url"): (
        "data/tools/deprecated-historical.yaml",
        "https://github.com/kubernetes/dashboard",
        "https://github.com/kubernetes-retired/dashboard",
    ),
    ("localstack", "repository_url"): (
        "data/tools/virtualization-bare-metal-homelab.yaml",
        "https://github.com/localstack/localstack",
        "https://github.com/localstack/localstack",
    ),
    ("minio", "repository_url"): (
        "data/tools/databases-caching-data-infrastructure.yaml",
        "https://github.com/minio/minio",
        "https://github.com/minio/minio",
    ),
}
EXPECTED_IDS = {tool_id for tool_id, _field in EXPECTED_SCOPE}
EXPECTED_WORK_ITEMS = set(EXPECTED_SCOPE)
EXPECTED_CHANGES = {
    key: (before, after)
    for key, (_path, before, after) in EXPECTED_SCOPE.items()
    if before != after
}
PROTECTED_SELECTED_FIELDS = {
    "status",
    "needs_review",
    "license_model",
    "license_spdx",
    "official_url",
    "documentation_url",
}
REQUIRED_LEDGER_COLUMNS = {
    "tool_id",
    "affected_field",
    "canonical_yaml_file",
    "previous_value",
    "final_value",
    "v021_previous_decision",
    "fresh_repository_observation",
    "authoritative_governance_evidence",
    "inference",
    "final_decision",
    "canonical_changed",
    "unresolved_boundary",
}


def _manifest_rows() -> list[dict[str, Any]]:
    payload = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    return [row for row in payload["work_items"] if row["execution_sub_batch"] == "N3a"]


def _parse_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _ledger_rows(path: Path = LEDGER) -> list[dict[str, str]]:
    assert path.exists(), f"Missing N3a review ledger: {path}"
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
    assert header_index is not None, f"No N3a evidence table header in {path}"
    headers = _parse_cells(lines[header_index])
    missing = REQUIRED_LEDGER_COLUMNS - set(headers)
    assert not missing, f"N3a ledger is missing columns: {sorted(missing)}"

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
        raise AssertionError(
            "Git is required for N3a pinned-object invariants"
        ) from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or str(exc)).strip()
        raise AssertionError(
            "N3a pinned-object invariant failed for baseline "
            f"{N3A_EXECUTION_BASELINE_SHA} and accepted data tree "
            f"{N3A_ACCEPTED_DATA_TREE_SHA}: {detail}"
        ) from exc
    return result.stdout


def _baseline_data_tree() -> str:
    return _git("rev-parse", f"{N3A_EXECUTION_BASELINE_SHA}:data/tools").strip()


def _require_objects() -> None:
    _git("cat-file", "-e", f"{N3A_EXECUTION_BASELINE_SHA}^{{commit}}")
    _git("cat-file", "-e", f"{N3A_ACCEPTED_DATA_TREE_SHA}^{{tree}}")


def _yaml_paths_at_tree(tree_sha: str) -> list[str]:
    output = _git("ls-tree", "-r", "--name-only", tree_sha)
    return sorted(line for line in output.splitlines() if line.endswith(".yaml"))


def _records_at_tree(tree_sha: str) -> dict[str, tuple[str, dict[str, Any]]]:
    records: dict[str, tuple[str, dict[str, Any]]] = {}
    for relative_path in _yaml_paths_at_tree(tree_sha):
        payload = yaml.safe_load(_git("show", f"{tree_sha}:{relative_path}"))
        assert isinstance(payload, list)
        canonical_path = f"data/tools/{relative_path}"
        for record in payload:
            assert isinstance(record, dict) and isinstance(record.get("id"), str)
            tool_id = record["id"]
            assert tool_id not in records, f"Duplicate canonical ID {tool_id!r}"
            records[tool_id] = (canonical_path, record)
    return records


def _current_records() -> dict[str, tuple[str, dict[str, Any]]]:
    records: dict[str, tuple[str, dict[str, Any]]] = {}
    for path in sorted((ROOT / "data/tools").glob("*.yaml")):
        relative = path.relative_to(ROOT).as_posix()
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert isinstance(payload, list)
        for record in payload:
            tool_id = record["id"]
            assert tool_id not in records, f"Duplicate canonical ID {tool_id!r}"
            records[tool_id] = (relative, record)
    return records


def _field_changes() -> dict[tuple[str, str], tuple[Any, Any]]:
    baseline = _records_at_tree(_baseline_data_tree())
    accepted = _records_at_tree(N3A_ACCEPTED_DATA_TREE_SHA)
    assert baseline.keys() == accepted.keys()
    changes: dict[tuple[str, str], tuple[Any, Any]] = {}
    for tool_id in baseline:
        baseline_path, before = baseline[tool_id]
        accepted_path, after = accepted[tool_id]
        assert baseline_path == accepted_path
        for field in before.keys() | after.keys():
            if before.get(field) != after.get(field):
                changes[(tool_id, field)] = (before.get(field), after.get(field))
    return changes


def _assert_owned_values(
    current: dict[str, tuple[str, dict[str, Any]]],
    accepted: dict[str, tuple[str, dict[str, Any]]],
) -> None:
    for (tool_id, field), (
        expected_path,
        _before,
        expected_value,
    ) in EXPECTED_SCOPE.items():
        current_path, current_record = current[tool_id]
        accepted_path, accepted_record = accepted[tool_id]
        assert current_path == accepted_path == expected_path
        assert current_record[field] == accepted_record[field] == expected_value
        for protected_field in PROTECTED_SELECTED_FIELDS:
            assert current_record.get(protected_field) == accepted_record.get(
                protected_field
            )


def test_n3a_frozen_selector_is_exact() -> None:
    rows = _manifest_rows()
    assert len(rows) == 5
    assert [row["sequence_number"] for row in rows] == [60, 61, 62, 63, 64]
    assert {row["tool_id"] for row in rows} == EXPECTED_IDS
    assert {(row["tool_id"], row["affected_field"]) for row in rows} == (
        EXPECTED_WORK_ITEMS
    )
    assert Counter(row["tool_id"] for row in rows).most_common(1)[0][1] == 1


def test_n3a_manifest_matches_expected_baseline_values() -> None:
    for row in _manifest_rows():
        expected_path, previous_value, _final_value = EXPECTED_SCOPE[
            (row["tool_id"], row["affected_field"])
        ]
        assert row["canonical_yaml_file"] == expected_path
        assert row["current_value"] == previous_value
        assert row["affected_field"] == "repository_url"
        assert row["human_review_requirement"] == "required"


def test_n3a_ledger_exactly_covers_scope_and_values() -> None:
    rows = _ledger_rows()
    assert len(rows) == 5
    assert {(row["tool_id"], row["affected_field"]) for row in rows} == (
        EXPECTED_WORK_ITEMS
    )
    for row in rows:
        key = (row["tool_id"], row["affected_field"])
        expected_path, previous_value, final_value = EXPECTED_SCOPE[key]
        assert row["canonical_yaml_file"] == expected_path
        assert row["previous_value"] == previous_value
        assert row["final_value"] == final_value
        assert row["v021_previous_decision"] == "reviewed-but-unchanged in v0.2.1"
        assert "2026-08-12" in row["fresh_repository_observation"]
        assert "https://" in row["authoritative_governance_evidence"]
        assert row["inference"]
        assert row["final_decision"]
        assert (row["canonical_changed"] == "yes") == (key in EXPECTED_CHANGES)
        assert row["unresolved_boundary"]


def test_n3a_explicit_accepted_tree_has_exact_canonical_delta() -> None:
    _require_objects()
    assert _field_changes() == EXPECTED_CHANGES


def test_n3a_has_no_lost_or_new_ids() -> None:
    baseline = _records_at_tree(_baseline_data_tree())
    accepted = _records_at_tree(N3A_ACCEPTED_DATA_TREE_SHA)
    assert baseline.keys() == accepted.keys()


def test_n3a_selected_protected_fields_match_baseline() -> None:
    baseline = _records_at_tree(_baseline_data_tree())
    accepted = _records_at_tree(N3A_ACCEPTED_DATA_TREE_SHA)
    for tool_id in EXPECTED_IDS:
        for field in PROTECTED_SELECTED_FIELDS:
            assert baseline[tool_id][1].get(field) == accepted[tool_id][1].get(field)


def test_n3a_current_state_preserves_owned_decisions() -> None:
    _assert_owned_values(
        _current_records(),
        _records_at_tree(N3A_ACCEPTED_DATA_TREE_SHA),
    )


def test_n3a_unrelated_future_change_does_not_invalidate_history() -> None:
    accepted = _records_at_tree(N3A_ACCEPTED_DATA_TREE_SHA)
    future = deepcopy(accepted)
    unrelated_id = next(tool_id for tool_id in future if tool_id not in EXPECTED_IDS)
    future[unrelated_id][1]["summary"] = "Later authorized unrelated change."
    _assert_owned_values(future, accepted)


def test_n3a_selected_repository_urls_remain_strings() -> None:
    current = _current_records()
    for tool_id, field in EXPECTED_WORK_ITEMS:
        assert isinstance(current[tool_id][1][field], str)


def test_n3a_generated_docs_contain_accepted_repository_urls() -> None:
    expected_files = {
        "juju": [ROOT / "docs/categories/configuration-management.md"],
        "kubernetes-dashboard": [
            ROOT / "docs/categories/deprecated-historical.md",
            ROOT / "docs/categories/kubernetes-distributions-operations.md",
            ROOT / "docs/lifecycle/retire.md",
            ROOT / "docs/roles/kubernetes-engineer.md",
            ROOT / "docs/roles/platform-engineer.md",
            ROOT / "docs/roles/site-reliability-engineer.md",
        ],
    }
    for tool_id, paths in expected_files.items():
        final_value = EXPECTED_SCOPE[(tool_id, "repository_url")][2]
        for path in paths:
            assert final_value in path.read_text(encoding="utf-8")


def test_n3a_ledger_records_durable_objects_and_totals() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    assert f"Execution baseline SHA: `{N3A_EXECUTION_BASELINE_SHA}`" in text
    assert (
        f"Accepted canonical `data/tools` tree: `{N3A_ACCEPTED_DATA_TREE_SHA}`" in text
    )
    assert "does not depend on a pre-rebase branch commit" in text
    for expected in (
        "SELECTED_MANIFEST_ROWS: 5",
        "REVIEWED_MANIFEST_ROWS: 5",
        "UNREVIEWED_MANIFEST_ROWS: 0",
        "SELECTED_UNIQUE_IDS: 5",
        "DUPLICATE_SELECTED_IDS: 0",
        "TOTAL_CHANGED_CANONICAL_IDS: 2",
        "TOTAL_CHANGED_CANONICAL_FIELDS: 2",
        "REVIEWED_BUT_UNCHANGED_IDS: 3",
        "NON_SELECTED_CHANGED_IDS: 0",
        "LOST_IDS: 0",
        "NEW_IDS: 0",
        "MACHINE_API_REPLACEMENT_CANDIDATES: 0",
    ):
        assert expected in text


def test_n3a_missing_object_is_actionable(monkeypatch: Any) -> None:
    def fail(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        raise subprocess.CalledProcessError(128, args[0], stderr="missing object")

    monkeypatch.setattr(subprocess, "run", fail)
    try:
        _require_objects()
        raise AssertionError("Expected missing pinned object to fail")
    except AssertionError as exc:
        assert N3A_EXECUTION_BASELINE_SHA in str(exc)
        assert N3A_ACCEPTED_DATA_TREE_SHA in str(exc)
        assert "missing object" in str(exc)


def test_n3a_git_unavailable_is_actionable(monkeypatch: Any) -> None:
    def fail(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        raise FileNotFoundError("git missing")

    monkeypatch.setattr(subprocess, "run", fail)
    try:
        _require_objects()
        raise AssertionError("Expected missing Git to fail")
    except AssertionError as exc:
        assert "Git is required" in str(exc)


def test_n3a_historical_diff_uses_explicit_trees(monkeypatch: Any) -> None:
    commands: list[list[str]] = []

    def record(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        command = list(args[0])
        commands.append(command)
        if command[1:3] == ["rev-parse", f"{N3A_EXECUTION_BASELINE_SHA}:data/tools"]:
            return subprocess.CompletedProcess(
                command, 0, stdout="baseline-tree\n", stderr=""
            )
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", record)
    baseline_tree = _baseline_data_tree()
    _git("diff", "--name-only", baseline_tree, N3A_ACCEPTED_DATA_TREE_SHA)
    diff = next(command for command in commands if command[:2] == ["git", "diff"])
    baseline_index = diff.index("baseline-tree")
    assert diff[baseline_index + 1] == N3A_ACCEPTED_DATA_TREE_SHA
    assert "HEAD" not in diff
    assert not any("..." in argument for argument in diff)


def test_n3a_ledger_parser_rejects_malformed_rows(tmp_path: Path) -> None:
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
