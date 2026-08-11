from __future__ import annotations

import subprocess
from collections import Counter
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "maintenance" / "v0.2.2-carryover-execution-manifest.yaml"
LEDGER = ROOT / "docs" / "maintenance" / "v0.2.2-n1b-access-retry-review.md"

N1B_EXECUTION_BASELINE_SHA = "af5ac0d27b59cf5211d074f57f48adbdecdcb2c6"
# N1b accepted every selected canonical value unchanged. The accepted canonical
# result is therefore the permanent execution-baseline commit, not a branch-only
# evidence/test commit that would become unreachable after a rebase merge.
N1B_ACCEPTED_CANONICAL_SHA = N1B_EXECUTION_BASELINE_SHA

EXPECTED_SCOPE = {
    ("oracle-cloud-infrastructure-oci", "official_url"): (
        "data/tools/cloud-platforms-management.yaml",
        "https://www.oracle.com/cloud",
    ),
    ("paperless-ngx", "official_url"): (
        "data/tools/emerging-experimental.yaml",
        "https://docs.paperless-ngx.com",
    ),
    ("predictive-horizontal-pod-autoscaler", "official_url"): (
        "data/tools/kubernetes-networking-storage-addons.yaml",
        "https://predictive-horizontal-pod-autoscaler.readthedocs.io/en/latest",
    ),
    ("pytest", "official_url"): (
        "data/tools/ci-build-testing.yaml",
        "https://docs.pytest.org/en/stable",
    ),
    ("scrapling", "official_url"): (
        "data/tools/developer-experience-local-environments.yaml",
        "https://scrapling.readthedocs.io/en/latest",
    ),
    ("udemy-cka-course", "official_url"): (
        "data/tools/documentation-learning-career.yaml",
        "https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests",
    ),
    ("vegacloud-inform", "official_url"): (
        "data/tools/finops-sustainability.yaml",
        "https://www.vegacloud.io/products/inform",
    ),
    ("volsync", "official_url"): (
        "data/tools/backup-disaster-recovery-resilience.yaml",
        "https://volsync.readthedocs.io",
    ),
    ("vultr", "official_url"): (
        "data/tools/cloud-platforms-management.yaml",
        "https://www.vultr.com",
    ),
    ("wine", "official_url"): (
        "data/tools/developer-experience-local-environments.yaml",
        "https://www.winehq.org",
    ),
}

EXPECTED_IDS = {tool_id for tool_id, _field in EXPECTED_SCOPE}
EXPECTED_WORK_ITEMS = set(EXPECTED_SCOPE)

PROTECTED_SELECTED_FIELDS = {
    "status",
    "needs_review",
    "license_model",
    "license_spdx",
    "repository_url",
}

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
    return [row for row in payload["work_items"] if row["execution_sub_batch"] == "N1b"]


def _parse_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _ledger_rows(path: Path = LEDGER) -> list[dict[str, str]]:
    assert path.exists(), f"Missing N1b review ledger: {path}"
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
    assert header_index is not None, f"No N1b evidence table header in {path}"
    headers = _parse_cells(lines[header_index])
    missing = REQUIRED_LEDGER_COLUMNS - set(headers)
    assert not missing, f"N1b ledger is missing columns: {sorted(missing)}"

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
    command = ["git", *args]
    try:
        result = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            encoding="utf-8",
            check=True,
        )
    except FileNotFoundError as exc:
        raise AssertionError("Git is required for N1b pinned-range invariants") from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or str(exc)).strip()
        raise AssertionError(
            "N1b pinned-range invariant failed for explicit refs "
            f"{N1B_EXECUTION_BASELINE_SHA} -> {N1B_ACCEPTED_CANONICAL_SHA}: "
            f"{detail}"
        ) from exc
    return result.stdout


def _require_refs() -> None:
    for sha in (N1B_EXECUTION_BASELINE_SHA, N1B_ACCEPTED_CANONICAL_SHA):
        _git("cat-file", "-e", f"{sha}^{{commit}}")


def _changed_canonical_files() -> set[str]:
    _require_refs()
    output = _git(
        "diff",
        "--name-only",
        N1B_EXECUTION_BASELINE_SHA,
        N1B_ACCEPTED_CANONICAL_SHA,
        "--",
        "data/tools/",
    )
    return {line for line in output.splitlines() if line}


def _yaml_paths_at(revision: str) -> list[str]:
    output = _git("ls-tree", "-r", "--name-only", revision, "--", "data/tools/")
    return sorted(line for line in output.splitlines() if line.endswith(".yaml"))


def _records_at(revision: str) -> dict[str, tuple[str, dict[str, Any]]]:
    records: dict[str, tuple[str, dict[str, Any]]] = {}
    for yaml_path in _yaml_paths_at(revision):
        payload = yaml.safe_load(_git("show", f"{revision}:{yaml_path}"))
        assert isinstance(payload, list), f"Expected list at {revision}:{yaml_path}"
        for record in payload:
            assert isinstance(record, dict) and isinstance(record.get("id"), str)
            tool_id = record["id"]
            assert tool_id not in records, f"Duplicate canonical ID {tool_id!r}"
            records[tool_id] = (yaml_path, record)
    return records


def _current_records() -> dict[str, tuple[str, dict[str, Any]]]:
    records: dict[str, tuple[str, dict[str, Any]]] = {}
    for path in sorted((ROOT / "data" / "tools").glob("*.yaml")):
        relative = path.relative_to(ROOT).as_posix()
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert isinstance(payload, list), f"Expected list in {path}"
        for record in payload:
            assert isinstance(record, dict) and isinstance(record.get("id"), str)
            tool_id = record["id"]
            assert tool_id not in records, f"Duplicate canonical ID {tool_id!r}"
            records[tool_id] = (relative, record)
    return records


def _assert_n1b_owned_values(
    current: dict[str, tuple[str, dict[str, Any]]],
    accepted: dict[str, tuple[str, dict[str, Any]]],
) -> None:
    for key, (expected_path, expected_value) in EXPECTED_SCOPE.items():
        tool_id, field = key
        assert tool_id in current, f"Current catalogue lost N1b ID {tool_id!r}"
        assert tool_id in accepted, f"N1b result is missing selected ID {tool_id!r}"
        current_path, current_record = current[tool_id]
        accepted_path, accepted_record = accepted[tool_id]
        assert current_path == expected_path
        assert accepted_path == expected_path
        assert accepted_record.get(field) == expected_value
        assert current_record.get(field) == expected_value
        for protected_field in PROTECTED_SELECTED_FIELDS:
            assert current_record.get(protected_field) == accepted_record.get(
                protected_field
            ), f"N1b-protected field drifted for {(tool_id, protected_field)}"


def test_n1b_frozen_selector_is_exact() -> None:
    rows = _manifest_rows()
    assert len(rows) == 10
    assert [row["sequence_number"] for row in rows] == list(range(26, 36))
    assert {row["tool_id"] for row in rows} == EXPECTED_IDS
    assert len({row["tool_id"] for row in rows}) == 10
    assert {(row["tool_id"], row["affected_field"]) for row in rows} == (
        EXPECTED_WORK_ITEMS
    )
    assert Counter(row["tool_id"] for row in rows).most_common(1)[0][1] == 1


def test_n1b_manifest_scope_matches_expected_values() -> None:
    for row in _manifest_rows():
        key = (row["tool_id"], row["affected_field"])
        expected_path, expected_value = EXPECTED_SCOPE[key]
        assert row["canonical_yaml_file"] == expected_path
        assert row["current_value"] == expected_value
        assert row["affected_field"] == "official_url"


def test_n1b_ledger_exactly_covers_frozen_rows() -> None:
    rows = _ledger_rows()
    assert len(rows) == 10
    assert {(row["tool_id"], row["affected_field"]) for row in rows} == (
        EXPECTED_WORK_ITEMS
    )


def test_n1b_ledger_values_match_manifest_and_current_catalogue() -> None:
    current = _current_records()
    for row in _ledger_rows():
        key = (row["tool_id"], row["affected_field"])
        expected_path, expected_value = EXPECTED_SCOPE[key]
        current_path, current_record = current[row["tool_id"]]
        assert row["canonical_yaml_file"] == expected_path == current_path
        assert row["previous_value"] == expected_value
        assert row["final_value"] == expected_value
        assert current_record[row["affected_field"]] == expected_value
        assert row["v021_previous_decision"] == "reviewed-but-unchanged in v0.2.1"
        assert row["canonical_changed"] == "no"


def test_n1b_ledger_separates_observation_evidence_and_inference() -> None:
    for row in _ledger_rows():
        assert "2026-08-12" in row["fresh_network_observation"]
        assert "https://" in row["authoritative_evidence"]
        assert (
            "Primary source" in row["inference"] or "primary source" in row["inference"]
        )
        assert row["final_decision"] == "retain current value"
        assert row["unresolved_boundary"]


def test_n1b_historical_canonical_result_is_explicitly_unchanged() -> None:
    assert N1B_ACCEPTED_CANONICAL_SHA == N1B_EXECUTION_BASELINE_SHA
    assert _changed_canonical_files() == set()


def test_n1b_selected_ids_exist_at_baseline_and_current_state() -> None:
    baseline = _records_at(N1B_EXECUTION_BASELINE_SHA)
    current = _current_records()
    assert baseline.keys() >= EXPECTED_IDS
    assert current.keys() >= EXPECTED_IDS


def test_n1b_current_state_preserves_owned_decisions() -> None:
    _assert_n1b_owned_values(
        _current_records(),
        _records_at(N1B_ACCEPTED_CANONICAL_SHA),
    )


def test_n1b_unrelated_future_canonical_change_does_not_invalidate_history() -> None:
    accepted = _records_at(N1B_ACCEPTED_CANONICAL_SHA)
    future = deepcopy(accepted)
    unrelated_id = next(tool_id for tool_id in future if tool_id not in EXPECTED_IDS)
    future[unrelated_id][1]["summary"] = "A later authorized unrelated change."
    _assert_n1b_owned_values(future, accepted)


def test_n1b_selected_protected_fields_match_execution_baseline() -> None:
    baseline = _records_at(N1B_EXECUTION_BASELINE_SHA)
    current = _current_records()
    for tool_id in EXPECTED_IDS:
        for field in PROTECTED_SELECTED_FIELDS:
            assert current[tool_id][1].get(field) == baseline[tool_id][1].get(field), (
                f"Forbidden N1b drift for {(tool_id, field)}"
            )


def test_n1b_selected_urls_remain_typed_strings() -> None:
    current = _current_records()
    for tool_id, field in EXPECTED_WORK_ITEMS:
        assert isinstance(current[tool_id][1][field], str)


def test_n1b_ledger_records_baseline_and_zero_delta_result() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    assert f"Execution baseline SHA: `{N1B_EXECUTION_BASELINE_SHA}`" in text
    assert f"Accepted canonical result SHA: `{N1B_ACCEPTED_CANONICAL_SHA}`" in text
    assert "No branch-only commit is used as an executable historical ref" in text
    assert "Canonical baseline/result delta: `0` files, `0` IDs, `0` fields" in text


def test_n1b_scope_audit_totals_are_recorded() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    for expected in (
        "SELECTED_MANIFEST_ROWS: 10",
        "REVIEWED_MANIFEST_ROWS: 10",
        "UNREVIEWED_MANIFEST_ROWS: 0",
        "SELECTED_UNIQUE_IDS: 10",
        "DUPLICATE_SELECTED_IDS: 0",
        "TOTAL_CHANGED_CANONICAL_IDS: 0",
        "TOTAL_CHANGED_CANONICAL_FIELDS: 0",
        "REVIEWED_BUT_UNCHANGED_IDS: 10",
        "NON_SELECTED_CHANGED_IDS: 0",
        "LOST_IDS: 0",
        "NEW_IDS: 0",
        "MACHINE_API_REPLACEMENT_CANDIDATES: 0",
    ):
        assert expected in text


def test_n1b_missing_ref_is_always_an_actionable_failure(monkeypatch: Any) -> None:
    def fail(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        raise subprocess.CalledProcessError(128, args[0], stderr="missing object")

    monkeypatch.setattr(subprocess, "run", fail)
    try:
        _require_refs()
        raise AssertionError("Expected missing pinned ref to fail")
    except AssertionError as exc:
        message = str(exc)
        assert N1B_EXECUTION_BASELINE_SHA in message
        assert N1B_ACCEPTED_CANONICAL_SHA in message
        assert "missing object" in message


def test_n1b_git_unavailable_is_actionable(monkeypatch: Any) -> None:
    def fail(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        raise FileNotFoundError("git missing")

    monkeypatch.setattr(subprocess, "run", fail)
    try:
        _require_refs()
        raise AssertionError("Expected missing Git to fail")
    except AssertionError as exc:
        assert "Git is required" in str(exc)


def test_n1b_historical_diff_uses_two_explicit_commits(monkeypatch: Any) -> None:
    commands: list[list[str]] = []

    def record(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        command = list(args[0])
        commands.append(command)
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", record)
    _changed_canonical_files()
    diff = next(command for command in commands if command[:2] == ["git", "diff"])
    baseline_index = diff.index(N1B_EXECUTION_BASELINE_SHA)
    assert diff[baseline_index + 1] == N1B_ACCEPTED_CANONICAL_SHA
    assert "HEAD" not in diff
    assert not any("..." in argument for argument in diff)


def test_n1b_ledger_parser_rejects_malformed_rows(tmp_path: Path) -> None:
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
