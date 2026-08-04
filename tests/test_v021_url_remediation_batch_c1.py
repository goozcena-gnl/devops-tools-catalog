from __future__ import annotations

import csv
import os
import subprocess
from collections import Counter
from pathlib import Path

import yaml

from tests.link_review_test_utils import is_machine_api_endpoint

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "maintenance" / "v0.2.1-url-remediation-batch-c1-review.md"
PLAN_CSV = ROOT / "docs" / "maintenance" / "v0.2.1-url-remediation-plan.csv"

BATCH = "batch-c1-access-retry"
BATCH_C1_BASELINE_SHA = "0e001953922a63f7fdda62cdf2085e0004823b5c"

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

EXPECTED_MULTI_FIELD_DUPLICATES = {
    "ansible-lint",
    "argo-workflows",
    "argocd",
    "argocd-image-updater",
    "argocd-vault-plugin",
}

REQUIRED_LEDGER_COLUMNS = {
    "tool_id",
    "affected_field",
    "canonical_yaml_file",
    "previous_value",
    "final_value",
    "previous_report_classification",
    "previous_network_observation",
    "primary_sources",
    "evidence_summary",
    "final_decision",
    "canonical_changed",
    "remaining_boundary",
    "risk",
}


def _planning_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with PLAN_CSV.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            if row.get("proposed_batch", "").strip() == BATCH:
                rows.append(row)
    return rows


def _ledger_rows(ledger_path: Path = LEDGER) -> list[dict[str, str]]:
    assert ledger_path.exists(), f"Missing batch C1 review ledger: {ledger_path}"

    lines = [
        line.rstrip() for line in ledger_path.read_text(encoding="utf-8").splitlines()
    ]
    table_lines = [line for line in lines if line.startswith("|")]
    assert table_lines, (
        f"Batch C1 review ledger contains no Markdown table: {ledger_path}"
    )

    header = [part.strip() for part in table_lines[0].strip("|").split("|")]
    missing_columns = REQUIRED_LEDGER_COLUMNS - set(header)
    assert not missing_columns, (
        "Batch C1 review ledger is missing required columns "
        f"{sorted(missing_columns)}: {ledger_path}"
    )

    rows: list[dict[str, str]] = []
    for row_number, line in enumerate(table_lines[2:], start=3):
        stripped = line.strip()
        if stripped and set(stripped) <= {"|", "-", ":", " "}:
            continue
        values = [part.strip() for part in line.strip("|").split("|")]
        assert len(values) == len(header), (
            f"Batch C1 review ledger has malformed row at line {row_number}: "
            f"expected {len(header)} columns, got {len(values)}: {ledger_path}"
        )
        rows.append(dict(zip(header, values, strict=True)))
    return rows


def _load_tool(yaml_file: str, tool_id: str) -> dict:
    path = ROOT / yaml_file
    assert path.exists(), f"Canonical YAML file not found: {path}"
    tools = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(tools, list), f"Expected list in {path}"
    by_id = {t["id"]: t for t in tools if isinstance(t, dict) and "id" in t}
    assert tool_id in by_id, f"Tool {tool_id!r} not found in {path}"
    return by_id[tool_id]


def _require_batch_c1_baseline() -> None:
    import pytest

    try:
        subprocess.run(
            ["git", "cat-file", "-e", f"{BATCH_C1_BASELINE_SHA}^{{commit}}"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except FileNotFoundError as exc:
        raise AssertionError(
            "Git executable is required for Batch C1 pinned-baseline invariants"
        ) from exc
    except subprocess.CalledProcessError as exc:
        if os.getenv("GITHUB_ACTIONS") == "true":
            raise AssertionError(
                f"Baseline commit {BATCH_C1_BASELINE_SHA} is not reachable in this "
                "GitHub Actions checkout, so Batch C1 invariants cannot be enforced. "
                "Verify .github/workflows/quality.yml checkout uses fetch-depth: 0."
            ) from exc

        pytest.skip(
            f"Baseline commit {BATCH_C1_BASELINE_SHA} is not reachable in this local "
            "shallow/partial clone; skipping Batch C1 pinned-baseline invariants"
        )


def _changed_canonical_yaml_files() -> set[str]:
    _require_batch_c1_baseline()

    try:
        result = subprocess.run(
            [
                "git",
                "diff",
                "--name-only",
                BATCH_C1_BASELINE_SHA,
                "HEAD",
                "--",
                "data/tools/",
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        stderr = (exc.stderr or "").strip()
        raise AssertionError(
            "Unable to compute the Batch C1 canonical diff from baseline "
            f"{BATCH_C1_BASELINE_SHA}: {stderr or exc}"
        ) from exc

    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


# ---------------------------------------------------------------------------
# Scope lock and accounting
# ---------------------------------------------------------------------------


def test_batch_c1_planning_scope_counts() -> None:
    planning = _planning_rows()
    assert len(planning) == 25, f"Expected 25 planning rows, got {len(planning)}"

    ids = [row["tool_id"] for row in planning]
    counts = Counter(ids)

    assert set(ids) == EXPECTED_IDS
    assert len(set(ids)) == 20

    dup_ids = {tool_id for tool_id, count in counts.items() if count > 1}
    assert dup_ids == EXPECTED_MULTI_FIELD_DUPLICATES, (
        f"Duplicate-ID mismatch. Expected {EXPECTED_MULTI_FIELD_DUPLICATES}, got {dup_ids}"
    )

    unexpected_dups = dup_ids - EXPECTED_MULTI_FIELD_DUPLICATES
    assert unexpected_dups == set(), (
        f"Unexpected duplicate IDs outside approved multi-field list: {unexpected_dups}"
    )


def test_batch_c1_planning_work_items_exact() -> None:
    planning = _planning_rows()
    plan_items = {(row["tool_id"], row["affected_field"]) for row in planning}
    assert plan_items == EXPECTED_WORK_ITEMS, (
        f"Planning work-item mismatch. Missing: {EXPECTED_WORK_ITEMS - plan_items}. "
        f"Extra: {plan_items - EXPECTED_WORK_ITEMS}"
    )


def test_batch_c1_each_selected_id_field_exists_in_canonical_yaml() -> None:
    for row in _planning_rows():
        tool = _load_tool(row["canonical_yaml_file"], row["tool_id"])
        field = row["affected_field"]
        assert field in tool, (
            f"Canonical field {field!r} missing for {row['tool_id']!r} "
            f"in {row['canonical_yaml_file']}"
        )


# ---------------------------------------------------------------------------
# Ledger structure and coherence
# ---------------------------------------------------------------------------


def test_batch_c1_ledger_exists_and_row_count() -> None:
    rows = _ledger_rows()
    assert len(rows) == 25, f"Expected 25 ledger rows, got {len(rows)}"


def test_batch_c1_every_planned_row_reviewed_exactly_once() -> None:
    planning = _planning_rows()
    ledger = _ledger_rows()

    plan_items = Counter((row["tool_id"], row["affected_field"]) for row in planning)
    reviewed_items = Counter((row["tool_id"], row["affected_field"]) for row in ledger)

    missing = sorted(k for k in plan_items if reviewed_items[k] < plan_items[k])
    extra = sorted(k for k in reviewed_items if reviewed_items[k] > plan_items[k])

    assert not missing, f"Planned work items missing from ledger: {missing}"
    assert not extra, f"Unexpected extra work items in ledger: {extra}"


def test_batch_c1_previous_values_match_planning_csv() -> None:
    planning = _planning_rows()
    plan_prev = {
        (row["tool_id"], row["affected_field"]): row["current_canonical_value"]
        for row in planning
    }

    for row in _ledger_rows():
        key = (row["tool_id"], row["affected_field"])
        assert row["previous_value"] == plan_prev[key], (
            f"previous_value mismatch for {key}: "
            f"ledger={row['previous_value']!r}, plan={plan_prev[key]!r}"
        )


def test_batch_c1_final_values_match_canonical_yaml() -> None:
    planning = _planning_rows()
    yaml_map = {
        (row["tool_id"], row["affected_field"]): row["canonical_yaml_file"]
        for row in planning
    }

    for row in _ledger_rows():
        key = (row["tool_id"], row["affected_field"])
        tool = _load_tool(yaml_map[key], row["tool_id"])
        actual = tool.get(row["affected_field"])
        assert str(actual) == row["final_value"], (
            f"final_value mismatch for {key}: "
            f"ledger={row['final_value']!r}, yaml={actual!r}"
        )


def test_batch_c1_exact_changed_canonical_fields() -> None:
    changed = {
        (row["tool_id"], row["affected_field"])
        for row in _ledger_rows()
        if row["canonical_changed"] == "yes"
    }
    assert changed == set(), f"Expected no changed canonical fields, got {changed}"


def test_batch_c1_machine_api_replacements_zero() -> None:
    candidates = [
        row["final_value"]
        for row in _ledger_rows()
        if row["canonical_changed"] == "yes"
        and is_machine_api_endpoint(row["final_value"])
    ]
    assert candidates == [], (
        "Machine/API replacement candidates found among changed canonical values: "
        f"{candidates}"
    )


def test_batch_c1_inconclusive_rows_remain_unresolved() -> None:
    for row in _ledger_rows():
        if row["canonical_changed"] == "no":
            assert row["final_decision"], (
                "Every unchanged row must record an explicit unresolved-or-retain "
                f"decision: {(row['tool_id'], row['affected_field'])}"
            )
            assert row["remaining_boundary"], (
                "Every unchanged row must document a remaining boundary: "
                f"{(row['tool_id'], row['affected_field'])}"
            )


# ---------------------------------------------------------------------------
# Git scope invariants
# ---------------------------------------------------------------------------


def test_batch_c1_no_non_selected_canonical_record_changed() -> None:
    changed_yaml = _changed_canonical_yaml_files()
    assert changed_yaml == set(), (
        "No canonical YAML changes were expected in Batch C1; found: "
        f"{sorted(changed_yaml)}"
    )


def test_batch_c1_protected_planning_files_unchanged_since_baseline() -> None:
    protected = [
        "docs/maintenance/v0.2.1-url-remediation-plan.md",
        "docs/maintenance/v0.2.1-url-remediation-plan.csv",
        "tests/test_v021_url_remediation_plan.py",
        "tests/link_review_test_utils.py",
    ]

    _require_batch_c1_baseline()

    result = subprocess.run(
        [
            "git",
            "diff",
            "--name-only",
            BATCH_C1_BASELINE_SHA,
            "HEAD",
            "--",
            *protected,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    changed = {line.strip() for line in result.stdout.splitlines() if line.strip()}
    assert changed == set(), f"Protected planning files changed: {sorted(changed)}"


def test_batch_c1_canonical_diff_uses_explicit_two_commit_range() -> None:
    import unittest.mock as mock

    captured: list[list[str]] = []

    def _record(*args: object, **kwargs: object) -> subprocess.CompletedProcess:
        if args:
            captured.append(list(args[0]))
        return subprocess.CompletedProcess(args[0], 0, stdout="", stderr="")

    with mock.patch("subprocess.run", side_effect=_record):
        changed_files = _changed_canonical_yaml_files()

    assert changed_files == set(), (
        "The fully mocked successful diff should return an empty changed-file set"
    )

    diff_calls = [c for c in captured if len(c) >= 3 and c[:2] == ["git", "diff"]]
    assert diff_calls, "Expected at least one git diff invocation"

    diff_cmd = diff_calls[0]
    three_dot_args = [arg for arg in diff_cmd if "..." in arg]
    assert not three_dot_args, (
        "Three-dot revision range must not be used in the diff command; "
        f"found: {three_dot_args}"
    )
    assert BATCH_C1_BASELINE_SHA in diff_cmd
    assert "HEAD" in diff_cmd
    sha_idx = diff_cmd.index(BATCH_C1_BASELINE_SHA)
    assert diff_cmd[sha_idx + 1] == "HEAD", (
        "HEAD must follow immediately after the baseline SHA; "
        f"got {diff_cmd[sha_idx + 1]!r}"
    )


def test_batch_c1_require_baseline_available_succeeds() -> None:
    import unittest.mock as mock

    with mock.patch(
        "subprocess.run",
        return_value=subprocess.CompletedProcess(
            ["git", "cat-file"], 0, stdout="", stderr=""
        ),
    ):
        _require_batch_c1_baseline()


def test_batch_c1_require_baseline_missing_local_skips(monkeypatch: object) -> None:
    import unittest.mock as mock

    import pytest

    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)

    with (
        mock.patch(
            "subprocess.run",
            side_effect=subprocess.CalledProcessError(
                128, "git", stderr="not a valid object"
            ),
        ),
        pytest.raises(pytest.skip.Exception) as exc_info,
    ):
        _require_batch_c1_baseline()

    message = str(exc_info.value)
    assert BATCH_C1_BASELINE_SHA in message
    assert "local" in message
    assert "shallow/partial clone" in message


def test_batch_c1_require_baseline_missing_in_ci_is_actionable_failure(
    monkeypatch: object,
) -> None:
    import unittest.mock as mock

    monkeypatch.setenv("GITHUB_ACTIONS", "true")

    with mock.patch(
        "subprocess.run",
        side_effect=subprocess.CalledProcessError(
            128, "git", stderr="not a valid object"
        ),
    ):
        try:
            _require_batch_c1_baseline()
            raise AssertionError(  # pragma: no cover
                "Expected AssertionError when baseline is missing in CI"
            )
        except AssertionError as exc:
            text = str(exc)
            assert BATCH_C1_BASELINE_SHA in text
            assert "Batch C1 invariants cannot be enforced" in text
            assert "fetch-depth: 0" in text


def test_batch_c1_require_baseline_git_unavailable_actionable_error() -> None:
    import unittest.mock as mock

    with mock.patch("subprocess.run", side_effect=FileNotFoundError("git missing")):
        try:
            _require_batch_c1_baseline()
            raise AssertionError(  # pragma: no cover
                "Expected AssertionError when git executable is unavailable"
            )
        except AssertionError as exc:
            assert "Git executable is required" in str(exc)


def test_quality_workflow_checkout_pinned_and_fetch_depth_zero() -> None:
    workflow = ROOT / ".github" / "workflows" / "quality.yml"
    text = workflow.read_text(encoding="utf-8")
    assert "uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1" in text
    assert "fetch-depth: 0" in text


def test_batch_c1_protected_parity_command_uses_explicit_two_commit_range() -> None:
    import unittest.mock as mock

    captured: list[list[str]] = []

    def _record(*args: object, **kwargs: object) -> subprocess.CompletedProcess:
        if args:
            captured.append(list(args[0]))
        return subprocess.CompletedProcess(args[0], 0, stdout="", stderr="")

    with mock.patch("subprocess.run", side_effect=_record):
        test_batch_c1_protected_planning_files_unchanged_since_baseline()

    diff_calls = [c for c in captured if len(c) >= 3 and c[:2] == ["git", "diff"]]
    assert diff_calls, "Expected at least one git diff invocation"

    diff_cmd = diff_calls[0]
    three_dot_args = [arg for arg in diff_cmd if "..." in arg]
    assert not three_dot_args, (
        "Three-dot revision range must not be used in the protected parity command; "
        f"found: {three_dot_args}"
    )
    assert BATCH_C1_BASELINE_SHA in diff_cmd
    assert "HEAD" in diff_cmd
    sha_idx = diff_cmd.index(BATCH_C1_BASELINE_SHA)
    assert diff_cmd[sha_idx + 1] == "HEAD", (
        "HEAD must follow immediately after the baseline SHA in protected parity diff; "
        f"got {diff_cmd[sha_idx + 1]!r}"
    )


def test_batch_c1_protected_parity_subprocess_failure_is_actionable() -> None:
    import unittest.mock as mock

    call_count = 0

    def _side_effect(*args: object, **kwargs: object) -> subprocess.CompletedProcess:
        nonlocal call_count
        call_count += 1
        if call_count == 1:
            return subprocess.CompletedProcess(args[0], 0, stdout="", stderr="")
        raise subprocess.CalledProcessError(128, "git", stderr="simulated diff error")

    with mock.patch("subprocess.run", side_effect=_side_effect):
        try:
            test_batch_c1_protected_planning_files_unchanged_since_baseline()
            raise AssertionError(  # pragma: no cover
                "Expected CalledProcessError when protected parity git diff fails"
            )
        except subprocess.CalledProcessError as exc:
            assert exc.returncode == 128
