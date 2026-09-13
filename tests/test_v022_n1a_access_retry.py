from __future__ import annotations

import subprocess
from collections import Counter
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "maintenance" / "v0.2.2-carryover-execution-manifest.yaml"
LEDGER = ROOT / "docs" / "maintenance" / "v0.2.2-n1a-access-retry-review.md"

N1A_BASELINE_SHA = "4a682ec8eca022712d5f62b6579880b4411d2a9e"
N1A_RESULT_SHA = "4a39a9ad5e04514277ec6a28d97a88b79d58ee93"
N1A_HISTORICAL_PRE_REBASE_CANDIDATE_SHA = "b1270542ba9d824997bbb3f65a9ade73f905a173"

EXPECTED_IDS = {
    "ansible-lint",
    "apache-cloudstack",
    "argo-workflows",
    "argocd",
    "argocd-agent",
    "argocd-image-updater",
    "argocd-vault-plugin",
    "black",
    "cilium",
    "cosmian-kms",
    "drata",
    "entrust-keycontrol",
    "helmfile",
    "kcli",
    "keda-gpu-scaler",
    "kubechecks",
    "kuttl",
    "labex-devops-tutorials",
    "linuxjourney",
    "mcp-server-kubernetes",
}

EXPECTED_WORK_ITEMS = {
    ("ansible-lint", "documentation_url"),
    ("ansible-lint", "official_url"),
    ("apache-cloudstack", "documentation_url"),
    ("argo-workflows", "documentation_url"),
    ("argo-workflows", "official_url"),
    ("argocd", "documentation_url"),
    ("argocd", "official_url"),
    ("argocd-agent", "official_url"),
    ("argocd-image-updater", "documentation_url"),
    ("argocd-image-updater", "official_url"),
    ("argocd-vault-plugin", "documentation_url"),
    ("argocd-vault-plugin", "official_url"),
    ("black", "official_url"),
    ("cilium", "documentation_url"),
    ("cosmian-kms", "official_url"),
    ("drata", "official_url"),
    ("entrust-keycontrol", "official_url"),
    ("helmfile", "official_url"),
    ("kcli", "official_url"),
    ("keda-gpu-scaler", "official_url"),
    ("kubechecks", "official_url"),
    ("kuttl", "official_url"),
    ("labex-devops-tutorials", "official_url"),
    ("linuxjourney", "official_url"),
    ("mcp-server-kubernetes", "official_url"),
}

EXPECTED_CHANGED_FIELDS = {
    ("ansible-lint", "documentation_url"): (
        "https://ansible.readthedocs.io/projects/lint/",
        "https://docs.ansible.com/projects/lint/",
    ),
    ("ansible-lint", "official_url"): (
        "https://ansible.readthedocs.io/projects/lint",
        "https://docs.ansible.com/projects/lint/",
    ),
}

EXPECTED_RESULT_FILES = {
    "data/tools/ci-build-testing.yaml",
    "docs/categories/ci-build-testing.md",
    "docs/lifecycle/build.md",
    "docs/lifecycle/test.md",
    "docs/roles/developer-experience-engineer.md",
    "docs/roles/devops-engineer.md",
    "docs/roles/release-engineer.md",
}

FORBIDDEN_SELECTED_FIELDS = {
    "status",
    "needs_review",
    "license_model",
    "license_spdx",
    "repository_url",
}

# Later, evidence-backed catalogue maintenance may supersede an N1a current-state
# protection without rewriting the pinned N1a history. Keep this allowlist at field
# granularity: later evidence reviews independently verified only the listed fields
# for Cosmian/Eviden KMS and mcp-server-kubernetes.
N1A_CURRENT_STATE_SUPERSESSIONS = {
    ("cosmian-kms", "repository_url"),
    ("cosmian-kms", "official_url"),
    ("cosmian-kms", "license_model"),
    ("cosmian-kms", "license_spdx"),
    ("cosmian-kms", "status"),
    ("cosmian-kms", "needs_review"),
    ("mcp-server-kubernetes", "repository_url"),
    ("mcp-server-kubernetes", "license_spdx"),
    ("mcp-server-kubernetes", "status"),
    ("mcp-server-kubernetes", "needs_review"),
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
    return [row for row in payload["work_items"] if row["execution_sub_batch"] == "N1a"]


def _parse_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _ledger_rows(path: Path = LEDGER) -> list[dict[str, str]]:
    assert path.exists(), f"Missing N1a review ledger: {path}"
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
    assert header_index is not None, f"No N1a evidence table header in {path}"
    headers = _parse_cells(lines[header_index])
    missing = REQUIRED_LEDGER_COLUMNS - set(headers)
    assert not missing, f"N1a ledger is missing columns: {sorted(missing)}"

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
        raise AssertionError("Git is required for N1a pinned-range invariants") from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or str(exc)).strip()
        raise AssertionError(
            "N1a pinned-range invariant failed for explicit refs "
            f"{N1A_BASELINE_SHA} -> {N1A_RESULT_SHA}: {detail}"
        ) from exc
    return result.stdout


def _require_refs() -> None:
    for sha in (N1A_BASELINE_SHA, N1A_RESULT_SHA):
        _git("cat-file", "-e", f"{sha}^{{commit}}")


def _changed_files() -> set[str]:
    _require_refs()
    output = _git(
        "diff",
        "--name-only",
        N1A_BASELINE_SHA,
        N1A_RESULT_SHA,
        "--",
    )
    return {line for line in output.splitlines() if line}


def _yaml_paths_at(revision: str) -> list[str]:
    output = _git(
        "ls-tree",
        "-r",
        "--name-only",
        revision,
        "--",
        "data/tools/",
    )
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
            tool_id = record["id"]
            assert tool_id not in records, f"Duplicate canonical ID {tool_id!r}"
            records[tool_id] = (relative, record)
    return records


def _field_changes() -> dict[tuple[str, str], tuple[Any, Any]]:
    baseline = _records_at(N1A_BASELINE_SHA)
    result = _records_at(N1A_RESULT_SHA)
    assert baseline.keys() == result.keys(), (
        f"Canonical ID drift: lost={sorted(baseline.keys() - result.keys())}, "
        f"new={sorted(result.keys() - baseline.keys())}"
    )

    changes: dict[tuple[str, str], tuple[Any, Any]] = {}
    for tool_id in baseline:
        baseline_path, before = baseline[tool_id]
        result_path, after = result[tool_id]
        assert baseline_path == result_path, f"Canonical file moved for {tool_id}"
        for field in before.keys() | after.keys():
            if before.get(field) != after.get(field):
                changes[(tool_id, field)] = (before.get(field), after.get(field))
    return changes


def _assert_current_n1a_persistence(
    current: dict[str, tuple[str, dict[str, Any]]],
    accepted: dict[str, tuple[str, dict[str, Any]]],
) -> None:
    for tool_id in EXPECTED_IDS:
        assert tool_id in current, f"Current catalogue lost N1a ID {tool_id!r}"
        assert tool_id in accepted, f"N1a result is missing selected ID {tool_id!r}"
        current_record = current[tool_id][1]
        accepted_record = accepted[tool_id][1]
        for field in FORBIDDEN_SELECTED_FIELDS:
            if (tool_id, field) in N1A_CURRENT_STATE_SUPERSESSIONS:
                continue
            assert current_record.get(field) == accepted_record.get(field), (
                f"N1a-protected field drifted for {(tool_id, field)}"
            )

    for tool_id, field in EXPECTED_WORK_ITEMS:
        if (tool_id, field) in N1A_CURRENT_STATE_SUPERSESSIONS:
            continue
        assert current[tool_id][1].get(field) == accepted[tool_id][1].get(field), (
            f"Accepted N1a decision drifted for {(tool_id, field)}"
        )


def test_n1a_frozen_selector_is_exact() -> None:
    rows = _manifest_rows()
    assert len(rows) == 25
    assert [row["sequence_number"] for row in rows] == list(range(1, 26))
    assert {row["tool_id"] for row in rows} == EXPECTED_IDS
    assert len({row["tool_id"] for row in rows}) == 20
    assert {(row["tool_id"], row["affected_field"]) for row in rows} == (
        EXPECTED_WORK_ITEMS
    )
    duplicates = {
        tool_id
        for tool_id, count in Counter(row["tool_id"] for row in rows).items()
        if count > 1
    }
    assert duplicates == {
        "ansible-lint",
        "argo-workflows",
        "argocd",
        "argocd-image-updater",
        "argocd-vault-plugin",
    }


def test_n1a_ledger_exactly_covers_frozen_rows() -> None:
    rows = _ledger_rows()
    assert len(rows) == 25
    assert {(row["tool_id"], row["affected_field"]) for row in rows} == (
        EXPECTED_WORK_ITEMS
    )


def test_n1a_ledger_records_previous_and_final_values() -> None:
    manifest = {
        (row["tool_id"], row["affected_field"]): row for row in _manifest_rows()
    }
    result = _records_at(N1A_RESULT_SHA)
    for row in _ledger_rows():
        key = (row["tool_id"], row["affected_field"])
        expected = manifest[key]
        yaml_path, record = result[row["tool_id"]]
        assert row["canonical_yaml_file"] == expected["canonical_yaml_file"]
        assert row["canonical_yaml_file"] == yaml_path
        assert row["previous_value"] == str(expected["current_value"])
        assert row["final_value"] == str(record[row["affected_field"]])
        assert row["v021_previous_decision"] == "reviewed-but-unchanged in v0.2.1"


def test_n1a_ledger_separates_observation_evidence_and_inference() -> None:
    for row in _ledger_rows():
        key = (row["tool_id"], row["affected_field"])
        assert row["fresh_network_observation"]
        assert row["authoritative_evidence"]
        assert row["inference"]
        assert row["final_decision"]
        assert row["unresolved_boundary"]
        changed = key in EXPECTED_CHANGED_FIELDS
        assert (row["canonical_changed"] == "yes") == changed
        if changed:
            assert "HTTP 200 redirect" in row["fresh_network_observation"]
            assert (
                "Official ansible/ansible-lint README" in row["authoritative_evidence"]
            )
            assert "primary-source proof" in row["final_decision"]


def test_n1a_explicit_historical_result_diff_is_exact() -> None:
    assert _changed_files() == EXPECTED_RESULT_FILES
    assert _field_changes() == EXPECTED_CHANGED_FIELDS


def test_n1a_has_no_lost_or_new_canonical_ids() -> None:
    baseline = _records_at(N1A_BASELINE_SHA)
    result = _records_at(N1A_RESULT_SHA)
    assert baseline.keys() == result.keys()


def test_n1a_selected_protected_fields_are_unchanged() -> None:
    baseline = _records_at(N1A_BASELINE_SHA)
    result = _records_at(N1A_RESULT_SHA)
    for tool_id in EXPECTED_IDS:
        before = baseline[tool_id][1]
        after = result[tool_id][1]
        for field in FORBIDDEN_SELECTED_FIELDS:
            assert before.get(field) == after.get(field), (
                f"Forbidden N1a change for {(tool_id, field)}"
            )


def test_n1a_changed_values_remain_typed_strings() -> None:
    result = _records_at(N1A_RESULT_SHA)
    for tool_id, field in EXPECTED_CHANGED_FIELDS:
        assert isinstance(result[tool_id][1][field], str)


def test_n1a_current_state_preserves_owned_decisions() -> None:
    _assert_current_n1a_persistence(
        _current_records(),
        _records_at(N1A_RESULT_SHA),
    )


def test_n1a_unrelated_future_canonical_change_does_not_invalidate_history() -> None:
    accepted = _records_at(N1A_RESULT_SHA)
    future = deepcopy(accepted)
    unrelated_id = next(tool_id for tool_id in future if tool_id not in EXPECTED_IDS)
    future[unrelated_id][1]["summary"] = "A later authorized unrelated change."

    _assert_current_n1a_persistence(future, accepted)


def test_n1a_ledger_records_permanent_result_and_pre_rebase_provenance() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    assert f"Permanent N1a result SHA: `{N1A_RESULT_SHA}`" in text
    assert (
        "Historical pre-rebase candidate SHA: "
        f"`{N1A_HISTORICAL_PRE_REBASE_CANDIDATE_SHA}`" in text
    )
    assert "provenance only" in text


def test_n1a_scope_audit_totals_are_recorded() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    for expected in (
        "SELECTED_MANIFEST_ROWS: 25",
        "REVIEWED_MANIFEST_ROWS: 25",
        "UNREVIEWED_MANIFEST_ROWS: 0",
        "SELECTED_UNIQUE_IDS: 20",
        "TOTAL_CHANGED_CANONICAL_IDS: 1",
        "TOTAL_CHANGED_CANONICAL_FIELDS: 2",
        "REVIEWED_BUT_UNCHANGED_IDS: 19",
        "NON_SELECTED_CHANGED_IDS: 0",
        "LOST_IDS: 0",
        "NEW_IDS: 0",
    ):
        assert expected in text


def test_n1a_missing_ref_is_always_an_actionable_failure(monkeypatch: Any) -> None:
    def fail(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        raise subprocess.CalledProcessError(128, args[0], stderr="missing object")

    monkeypatch.setattr(subprocess, "run", fail)
    try:
        _require_refs()
        raise AssertionError("Expected missing pinned refs to fail")
    except AssertionError as exc:
        message = str(exc)
        assert N1A_BASELINE_SHA in message
        assert N1A_RESULT_SHA in message
        assert "missing object" in message


def test_n1a_missing_result_ref_is_always_a_failure(monkeypatch: Any) -> None:
    calls = 0

    def fail_second(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        nonlocal calls
        calls += 1
        if calls == 1:
            return subprocess.CompletedProcess(args[0], 0, stdout="", stderr="")
        raise subprocess.CalledProcessError(128, args[0], stderr="missing result")

    monkeypatch.setattr(subprocess, "run", fail_second)
    try:
        _require_refs()
        raise AssertionError("Expected missing result ref to fail")
    except AssertionError as exc:
        message = str(exc)
        assert N1A_BASELINE_SHA in message
        assert N1A_RESULT_SHA in message
        assert "missing result" in message


def test_n1a_git_unavailable_is_actionable(monkeypatch: Any) -> None:
    def fail(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        raise FileNotFoundError("git missing")

    monkeypatch.setattr(subprocess, "run", fail)
    try:
        _require_refs()
        raise AssertionError("Expected missing Git to fail")
    except AssertionError as exc:
        assert "Git is required" in str(exc)


def test_n1a_historical_diff_uses_two_explicit_commits(monkeypatch: Any) -> None:
    commands: list[list[str]] = []

    def record(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        command = list(args[0])
        commands.append(command)
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", record)
    _changed_files()
    diff = next(command for command in commands if command[:2] == ["git", "diff"])
    baseline_index = diff.index(N1A_BASELINE_SHA)
    assert diff[baseline_index + 1] == N1A_RESULT_SHA
    assert not any("..." in argument for argument in diff)


def test_n1a_pre_rebase_sha_is_never_an_executable_ref(monkeypatch: Any) -> None:
    commands: list[list[str]] = []

    def record(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        command = list(args[0])
        commands.append(command)
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", record)
    _changed_files()
    command_text = "\n".join(" ".join(command) for command in commands)
    assert N1A_HISTORICAL_PRE_REBASE_CANDIDATE_SHA not in command_text
    assert N1A_RESULT_SHA in command_text


def test_n1a_ledger_parser_rejects_malformed_rows(tmp_path: Path) -> None:
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
