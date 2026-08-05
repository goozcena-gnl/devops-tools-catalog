from __future__ import annotations

import csv
import os
import subprocess
from collections import Counter
from pathlib import Path

import yaml

from tests.link_review_test_utils import is_machine_api_endpoint

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "maintenance" / "v0.2.1-url-remediation-batch-c2-review.md"
PLAN_CSV = ROOT / "docs" / "maintenance" / "v0.2.1-url-remediation-plan.csv"
WORKFLOW = ROOT / ".github" / "workflows" / "quality.yml"

BATCH = "batch-c2-access-retry"
BATCH_C2_BASELINE_SHA = "52be634373c5bece54a376808c46ac31eceb3675"
BATCH_C2_RESULT_SHA = "45dedfdecf2a80207eb0acf6585e4298078cf469"

EXPECTED_IDS = {
    "oracle-cloud-infrastructure-oci",
    "paperless-ngx",
    "predictive-horizontal-pod-autoscaler",
    "pytest",
    "scrapling",
    "udemy-cka-course",
    "vegacloud-inform",
    "volsync",
    "vultr",
    "wine",
}

EXPECTED_WORK_ITEMS = {
    ("oracle-cloud-infrastructure-oci", "official_url"),
    ("paperless-ngx", "official_url"),
    ("predictive-horizontal-pod-autoscaler", "official_url"),
    ("pytest", "official_url"),
    ("scrapling", "official_url"),
    ("udemy-cka-course", "official_url"),
    ("vegacloud-inform", "official_url"),
    ("volsync", "official_url"),
    ("vultr", "official_url"),
    ("wine", "official_url"),
}

EXPECTED_SCOPE = {
    ("oracle-cloud-infrastructure-oci", "official_url"): {
        "canonical_yaml_file": "data/tools/cloud-platforms-management.yaml",
        "current_canonical_value": "https://www.oracle.com/cloud",
    },
    ("paperless-ngx", "official_url"): {
        "canonical_yaml_file": "data/tools/emerging-experimental.yaml",
        "current_canonical_value": "https://docs.paperless-ngx.com",
    },
    ("predictive-horizontal-pod-autoscaler", "official_url"): {
        "canonical_yaml_file": "data/tools/kubernetes-networking-storage-addons.yaml",
        "current_canonical_value": "https://predictive-horizontal-pod-autoscaler.readthedocs.io/en/latest",
    },
    ("pytest", "official_url"): {
        "canonical_yaml_file": "data/tools/ci-build-testing.yaml",
        "current_canonical_value": "https://docs.pytest.org/en/stable",
    },
    ("scrapling", "official_url"): {
        "canonical_yaml_file": "data/tools/developer-experience-local-environments.yaml",
        "current_canonical_value": "https://scrapling.readthedocs.io/en/latest",
    },
    ("udemy-cka-course", "official_url"): {
        "canonical_yaml_file": "data/tools/documentation-learning-career.yaml",
        "current_canonical_value": "https://www.udemy.com/course/certified-kubernetes-administrator-with-practice-tests",
    },
    ("vegacloud-inform", "official_url"): {
        "canonical_yaml_file": "data/tools/finops-sustainability.yaml",
        "current_canonical_value": "https://www.vegacloud.io/products/inform",
    },
    ("volsync", "official_url"): {
        "canonical_yaml_file": "data/tools/backup-disaster-recovery-resilience.yaml",
        "current_canonical_value": "https://volsync.readthedocs.io",
    },
    ("vultr", "official_url"): {
        "canonical_yaml_file": "data/tools/cloud-platforms-management.yaml",
        "current_canonical_value": "https://www.vultr.com",
    },
    ("wine", "official_url"): {
        "canonical_yaml_file": "data/tools/developer-experience-local-environments.yaml",
        "current_canonical_value": "https://www.winehq.org",
    },
}

REQUIRED_LEDGER_COLUMNS = {
    "tool_id",
    "affected_field",
    "canonical_yaml_file",
    "previous_value",
    "final_value",
    "previous_report_classification",
    "previous_network_observation",
    "controlled_retry_observation",
    "product_lifecycle_status",
    "primary_sources",
    "evidence_summary",
    "final_decision",
    "canonical_changed",
    "remaining_boundary",
    "risk",
}

PROTECTED_PATHS = [
    "docs/maintenance/v0.2.1-url-remediation-plan.md",
    "docs/maintenance/v0.2.1-url-remediation-plan.csv",
    "tests/test_v021_url_remediation_plan.py",
    "tests/link_review_test_utils.py",
    "docs/maintenance/v0.2.1-url-remediation-batch-a1-review.md",
    "docs/maintenance/v0.2.1-url-remediation-batch-a2-review.md",
    "docs/maintenance/v0.2.1-url-remediation-batch-b-review.md",
    "docs/maintenance/v0.2.1-url-remediation-batch-c1-review.md",
    "tests/test_v021_url_remediation_batch_a1.py",
    "tests/test_v021_url_remediation_batch_a2.py",
    "tests/test_v021_url_remediation_batch_b.py",
    "tests/test_v021_url_remediation_batch_c1.py",
    "reports/link-report.json",
    "reports/link-report.md",
    "docs/link-review-ledger.md",
    "schema/",
    "scripts/",
    "config/",
    ".github/workflows/",
    "requirements.txt",
    "requirements-dev.txt",
    "poetry.lock",
    "Pipfile",
    "Pipfile.lock",
    "pyproject.toml",
    "CHANGELOG.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
]


def _planning_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with PLAN_CSV.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            if row.get("proposed_batch", "").strip() == BATCH:
                rows.append(row)
    return rows


def _parse_markdown_table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _ledger_rows(ledger_path: Path = LEDGER) -> list[dict[str, str]]:
    assert ledger_path.exists(), f"Missing batch C2 review ledger: {ledger_path}"

    lines = ledger_path.read_text(encoding="utf-8").splitlines()

    header_line_idx = None
    header_cells: list[str] | None = None
    for idx, line in enumerate(lines):
        if not line.startswith("|"):
            continue
        cells = _parse_markdown_table_cells(line)
        if "tool_id" in cells and "final_decision" in cells:
            header_line_idx = idx
            header_cells = cells
            break

    assert header_line_idx is not None and header_cells is not None, (
        f"{ledger_path}: could not find Batch C2 evidence table header"
    )

    missing_columns = REQUIRED_LEDGER_COLUMNS - set(header_cells)
    assert not missing_columns, (
        f"{ledger_path}:{header_line_idx + 1}: missing required header columns: "
        f"{sorted(missing_columns)}"
    )

    expected_count = len(header_cells)
    header_index = {name: i for i, name in enumerate(header_cells)}

    rows: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()

    for line_idx, line in enumerate(
        lines[header_line_idx + 2 :], start=header_line_idx + 3
    ):
        if not line.startswith("|"):
            if rows:
                break
            continue

        stripped = line.strip()
        if stripped and set(stripped) <= {"|", "-", ":", " "}:
            continue

        values = _parse_markdown_table_cells(line)
        assert len(values) == expected_count, (
            f"{ledger_path}:{line_idx}: malformed ledger row; expected "
            f"{expected_count} columns, got {len(values)}"
        )

        row = {name: values[idx] for name, idx in header_index.items()}
        key = (row["tool_id"], row["affected_field"])
        assert key not in seen, (
            f"{ledger_path}:{line_idx}: duplicate work item row: {key}"
        )
        seen.add(key)
        rows.append(row)

    return rows


def _load_tool(yaml_file: str, tool_id: str) -> dict:
    path = ROOT / yaml_file
    assert path.exists(), f"Canonical YAML file not found: {path}"
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(payload, list), f"Expected list in {path}"
    by_id = {
        record["id"]: record
        for record in payload
        if isinstance(record, dict) and "id" in record
    }
    assert tool_id in by_id, f"Tool {tool_id!r} not found in {path}"
    return by_id[tool_id]


def _require_batch_c2_refs() -> None:
    import pytest

    refs = [
        ("baseline", BATCH_C2_BASELINE_SHA),
        ("result", BATCH_C2_RESULT_SHA),
    ]
    for label, sha in refs:
        try:
            subprocess.run(
                ["git", "cat-file", "-e", f"{sha}^{{commit}}"],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=True,
            )
        except FileNotFoundError as exc:
            raise AssertionError(
                "Git executable is required for Batch C2 pinned-result invariants"
            ) from exc
        except subprocess.CalledProcessError as exc:
            if os.getenv("GITHUB_ACTIONS") == "true":
                raise AssertionError(
                    f"{label.capitalize()} commit {sha} is not reachable in this "
                    "GitHub Actions checkout, so Batch C2 invariants cannot be "
                    "enforced. Required refs: "
                    f"{BATCH_C2_BASELINE_SHA} -> {BATCH_C2_RESULT_SHA}. "
                    "Verify .github/workflows/quality.yml checkout uses fetch-depth: 0."
                ) from exc

            pytest.skip(
                f"{label.capitalize()} commit {sha} is not reachable in this local "
                "shallow/partial clone; skipping Batch C2 pinned-result invariants "
                f"({BATCH_C2_BASELINE_SHA} -> {BATCH_C2_RESULT_SHA})"
            )


def _git_diff_name_only(paths: list[str]) -> set[str]:
    _require_batch_c2_refs()

    cmd = [
        "git",
        "diff",
        "--name-only",
        BATCH_C2_BASELINE_SHA,
        BATCH_C2_RESULT_SHA,
        "--",
        *paths,
    ]
    try:
        result = subprocess.run(
            cmd,
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        stderr = (exc.stderr or "").strip()
        raise AssertionError(
            "Unable to compute Batch C2 baseline/result diff using explicit "
            f"two-commit range ({BATCH_C2_BASELINE_SHA} {BATCH_C2_RESULT_SHA}): "
            f"{stderr or exc}"
        ) from exc

    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


# ---------------------------------------------------------------------------
# Scope lock
# ---------------------------------------------------------------------------


def test_batch_c2_selector_and_scope_counts() -> None:
    rows = _planning_rows()
    assert len(rows) == 10, f"Expected 10 planning rows, got {len(rows)}"

    ids = [row["tool_id"] for row in rows]
    counts = Counter(ids)

    assert set(ids) == EXPECTED_IDS
    assert len(set(ids)) == 10

    dup_ids = sorted(tool_id for tool_id, count in counts.items() if count > 1)
    assert dup_ids == [], f"Expected no duplicate IDs, got {dup_ids}"


def test_batch_c2_exact_work_items() -> None:
    rows = _planning_rows()
    work_items = {(row["tool_id"], row["affected_field"]) for row in rows}
    assert work_items == EXPECTED_WORK_ITEMS, (
        f"Work-item mismatch. Missing: {EXPECTED_WORK_ITEMS - work_items}. "
        f"Extra: {work_items - EXPECTED_WORK_ITEMS}"
    )


def test_batch_c2_exact_planning_values() -> None:
    rows = _planning_rows()
    for row in rows:
        key = (row["tool_id"], row["affected_field"])
        expected = EXPECTED_SCOPE[key]
        assert row["canonical_yaml_file"] == expected["canonical_yaml_file"]
        assert row["current_canonical_value"] == expected["current_canonical_value"]


# ---------------------------------------------------------------------------
# Ledger coherence
# ---------------------------------------------------------------------------


def test_batch_c2_ledger_exists_and_exactly_covers_planning_rows() -> None:
    planning = _planning_rows()
    ledger = _ledger_rows()

    assert len(ledger) == 10, f"Expected 10 ledger rows, got {len(ledger)}"

    plan_items = Counter((row["tool_id"], row["affected_field"]) for row in planning)
    ledger_items = Counter((row["tool_id"], row["affected_field"]) for row in ledger)

    missing = sorted(k for k in plan_items if ledger_items[k] < plan_items[k])
    extra = sorted(k for k in ledger_items if ledger_items[k] > plan_items[k])

    assert not missing, f"Planned work items missing from ledger: {missing}"
    assert not extra, f"Unexpected work items in ledger: {extra}"


def test_batch_c2_ledger_previous_values_match_planning() -> None:
    planning = {
        (row["tool_id"], row["affected_field"]): row for row in _planning_rows()
    }
    for row in _ledger_rows():
        key = (row["tool_id"], row["affected_field"])
        assert row["previous_value"] == planning[key]["current_canonical_value"], (
            f"previous_value mismatch for {key}: ledger={row['previous_value']!r}, "
            f"plan={planning[key]['current_canonical_value']!r}"
        )


def test_batch_c2_ledger_final_values_match_canonical_yaml() -> None:
    planning = {
        (row["tool_id"], row["affected_field"]): row for row in _planning_rows()
    }
    for row in _ledger_rows():
        key = (row["tool_id"], row["affected_field"])
        yaml_file = planning[key]["canonical_yaml_file"]
        tool = _load_tool(yaml_file, row["tool_id"])
        actual = tool.get(row["affected_field"])
        assert str(actual) == row["final_value"], (
            f"final_value mismatch for {key}: ledger={row['final_value']!r}, "
            f"yaml={actual!r}"
        )


def test_batch_c2_canonical_changed_flag_is_coherent() -> None:
    for row in _ledger_rows():
        values_differ = row["previous_value"] != row["final_value"]
        assert (row["canonical_changed"] == "yes") == values_differ, (
            f"canonical_changed coherence failed for {(row['tool_id'], row['affected_field'])}: "
            f"previous={row['previous_value']!r}, final={row['final_value']!r}, "
            f"canonical_changed={row['canonical_changed']!r}"
        )


def test_batch_c2_no_machine_api_replacement_candidates() -> None:
    candidates = []
    for row in _ledger_rows():
        if row["canonical_changed"] != "yes":
            continue
        if is_machine_api_endpoint(row["final_value"]):
            candidates.append((row["tool_id"], row["final_value"]))
    assert not candidates, (
        f"Machine/API replacement candidates found among changed values: {candidates}"
    )


# ---------------------------------------------------------------------------
# Baseline and diff invariants
# ---------------------------------------------------------------------------


def test_batch_c2_baseline_available_succeeds() -> None:
    import unittest.mock as mock

    with mock.patch(
        "subprocess.run",
        return_value=subprocess.CompletedProcess(
            ["git", "cat-file"], 0, stdout="", stderr=""
        ),
    ):
        _require_batch_c2_refs()


def test_batch_c2_baseline_missing_local_skips(monkeypatch: object) -> None:
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
        _require_batch_c2_refs()

    text = str(exc_info.value)
    assert BATCH_C2_BASELINE_SHA in text
    assert BATCH_C2_RESULT_SHA in text
    assert "local" in text
    assert "shallow/partial clone" in text


def test_batch_c2_baseline_missing_in_ci_fails_actionably(monkeypatch: object) -> None:
    import unittest.mock as mock

    monkeypatch.setenv("GITHUB_ACTIONS", "true")

    with mock.patch(
        "subprocess.run",
        side_effect=subprocess.CalledProcessError(
            128, "git", stderr="not a valid object"
        ),
    ):
        try:
            _require_batch_c2_refs()
            raise AssertionError(  # pragma: no cover
                "Expected AssertionError when baseline is missing in CI"
            )
        except AssertionError as exc:
            text = str(exc)
            assert BATCH_C2_BASELINE_SHA in text
            assert BATCH_C2_RESULT_SHA in text
            assert "Batch C2 invariants cannot be enforced" in text
            assert "fetch-depth: 0" in text


def test_batch_c2_result_missing_local_skips(monkeypatch: object) -> None:
    import unittest.mock as mock

    import pytest

    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)

    def _side_effect(*args: object, **kwargs: object) -> subprocess.CompletedProcess:
        cmd = list(args[0])
        if f"{BATCH_C2_BASELINE_SHA}^{{commit}}" in cmd:
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")
        if f"{BATCH_C2_RESULT_SHA}^{{commit}}" in cmd:
            raise subprocess.CalledProcessError(128, cmd, stderr="not a valid object")
        return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

    with (
        mock.patch("subprocess.run", side_effect=_side_effect),
        pytest.raises(pytest.skip.Exception) as exc_info,
    ):
        _require_batch_c2_refs()

    text = str(exc_info.value)
    assert BATCH_C2_BASELINE_SHA in text
    assert BATCH_C2_RESULT_SHA in text
    assert "local" in text


def test_batch_c2_result_missing_in_ci_fails_actionably(monkeypatch: object) -> None:
    import unittest.mock as mock

    monkeypatch.setenv("GITHUB_ACTIONS", "true")

    def _side_effect(*args: object, **kwargs: object) -> subprocess.CompletedProcess:
        cmd = list(args[0])
        if f"{BATCH_C2_BASELINE_SHA}^{{commit}}" in cmd:
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")
        if f"{BATCH_C2_RESULT_SHA}^{{commit}}" in cmd:
            raise subprocess.CalledProcessError(128, cmd, stderr="not a valid object")
        return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

    with mock.patch("subprocess.run", side_effect=_side_effect):
        try:
            _require_batch_c2_refs()
            raise AssertionError(  # pragma: no cover
                "Expected AssertionError when result is missing in CI"
            )
        except AssertionError as exc:
            text = str(exc)
            assert BATCH_C2_BASELINE_SHA in text
            assert BATCH_C2_RESULT_SHA in text
            assert "Batch C2 invariants cannot be enforced" in text
            assert "fetch-depth: 0" in text


def test_batch_c2_git_unavailable_fails_actionably() -> None:
    import unittest.mock as mock

    with mock.patch("subprocess.run", side_effect=FileNotFoundError("git missing")):
        try:
            _require_batch_c2_refs()
            raise AssertionError(  # pragma: no cover
                "Expected AssertionError when git executable is unavailable"
            )
        except AssertionError as exc:
            assert "Git executable is required" in str(exc)


def test_batch_c2_canonical_scope_diff_has_no_non_selected_changes() -> None:
    changed = _git_diff_name_only(["data/tools/"])
    assert changed == set(), (
        "No canonical YAML changes were expected in Batch C2; changed files: "
        f"{sorted(changed)}"
    )


def test_batch_c2_no_lost_or_new_selected_ids() -> None:
    expected = set(EXPECTED_IDS)
    present = set()
    for row in _planning_rows():
        tool = _load_tool(row["canonical_yaml_file"], row["tool_id"])
        present.add(tool["id"])

    lost = sorted(expected - present)
    new = sorted(present - expected)
    assert not lost, f"Lost selected IDs: {lost}"
    assert not new, f"Unexpected new selected IDs: {new}"


def test_batch_c2_only_selected_fields_are_touched() -> None:
    changed = {
        (row["tool_id"], row["affected_field"])
        for row in _ledger_rows()
        if row["canonical_changed"] == "yes"
    }
    assert changed <= EXPECTED_WORK_ITEMS, (
        f"Changed fields outside selected work items: {sorted(changed - EXPECTED_WORK_ITEMS)}"
    )


def test_batch_c2_protected_files_unchanged_since_baseline() -> None:
    changed = _git_diff_name_only(PROTECTED_PATHS)
    assert changed == set(), (
        f"Protected files changed since Batch C2 baseline: {sorted(changed)}"
    )


def test_batch_c2_diff_commands_use_explicit_two_commit_range() -> None:
    import unittest.mock as mock

    captured: list[list[str]] = []

    def _record(*args: object, **kwargs: object) -> subprocess.CompletedProcess:
        if args:
            captured.append(list(args[0]))
        return subprocess.CompletedProcess(args[0], 0, stdout="", stderr="")

    with mock.patch("subprocess.run", side_effect=_record):
        _git_diff_name_only(["data/tools/"])

    diff_calls = [
        cmd for cmd in captured if len(cmd) >= 3 and cmd[:2] == ["git", "diff"]
    ]
    assert diff_calls, "Expected at least one git diff call"

    cmd = diff_calls[0]
    assert BATCH_C2_BASELINE_SHA in cmd
    assert BATCH_C2_RESULT_SHA in cmd
    idx = cmd.index(BATCH_C2_BASELINE_SHA)
    assert cmd[idx + 1] == BATCH_C2_RESULT_SHA, (
        "Result SHA must immediately follow baseline SHA"
    )
    assert "HEAD" not in cmd
    assert not [arg for arg in cmd if "..." in arg], (
        f"Three-dot revision must not be used: {cmd}"
    )


def test_quality_workflow_checkout_is_pinned_with_full_history() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert "uses: actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1" in text
    assert "fetch-depth: 0" in text


# ---------------------------------------------------------------------------
# Parser robustness
# ---------------------------------------------------------------------------


def test_batch_c2_parser_missing_file_is_actionable(tmp_path: Path) -> None:
    missing = tmp_path / "missing.md"
    try:
        _ledger_rows(missing)
        raise AssertionError("Expected missing ledger assertion")  # pragma: no cover
    except AssertionError as exc:
        msg = str(exc)
        assert "Missing batch C2 review ledger" in msg
        assert str(missing) in msg


def test_batch_c2_parser_empty_file_fails_actionably(tmp_path: Path) -> None:
    ledger = tmp_path / "empty.md"
    ledger.write_text("", encoding="utf-8")

    try:
        _ledger_rows(ledger)
        raise AssertionError("Expected empty-ledger assertion")  # pragma: no cover
    except AssertionError as exc:
        text = str(exc)
        assert "could not find Batch C2 evidence table header" in text
        assert str(ledger) in text


def test_batch_c2_parser_missing_required_column_fails(tmp_path: Path) -> None:
    ledger = tmp_path / "missing-column.md"
    ledger.write_text(
        "\n".join(
            [
                "| tool_id | affected_field | final_decision |",
                "|---|---|---|",
                "| pytest | official_url | retain |",
            ]
        ),
        encoding="utf-8",
    )

    try:
        _ledger_rows(ledger)
        raise AssertionError("Expected missing-column assertion")  # pragma: no cover
    except AssertionError as exc:
        text = str(exc)
        assert "missing required header columns" in text
        assert str(ledger) in text


def test_batch_c2_parser_malformed_row_fails_with_line_number(tmp_path: Path) -> None:
    ledger = tmp_path / "malformed.md"
    ledger.write_text(
        "\n".join(
            [
                "| tool_id | affected_field | canonical_yaml_file | previous_value | final_value | previous_report_classification | previous_network_observation | controlled_retry_observation | product_lifecycle_status | primary_sources | evidence_summary | final_decision | canonical_changed | remaining_boundary | risk |",
                "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
                "| pytest | official_url | data/tools/ci-build-testing.yaml | https://docs.pytest.org/en/stable | https://docs.pytest.org/en/stable | rate-limited | HTTP 429 | attempt 1: HTTP 429 | needs-review | https://docs.pytest.org/en/stable | summary | retain | no |",
            ]
        ),
        encoding="utf-8",
    )

    try:
        _ledger_rows(ledger)
        raise AssertionError("Expected malformed-row assertion")  # pragma: no cover
    except AssertionError as exc:
        text = str(exc)
        assert "malformed ledger row" in text
        assert str(ledger) in text


def test_batch_c2_parser_duplicate_and_unexpected_work_items_rejected(
    tmp_path: Path,
) -> None:
    ledger = tmp_path / "dup.md"
    ledger.write_text(
        "\n".join(
            [
                "| tool_id | affected_field | canonical_yaml_file | previous_value | final_value | previous_report_classification | previous_network_observation | controlled_retry_observation | product_lifecycle_status | primary_sources | evidence_summary | final_decision | canonical_changed | remaining_boundary | risk |",
                "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
                "| pytest | official_url | data/tools/ci-build-testing.yaml | https://docs.pytest.org/en/stable | https://docs.pytest.org/en/stable | rate-limited | HTTP 429 | attempt 1: HTTP 429 | needs-review | https://docs.pytest.org/en/stable | summary | retain | no | boundary | low |",
                "| pytest | official_url | data/tools/ci-build-testing.yaml | https://docs.pytest.org/en/stable | https://docs.pytest.org/en/stable | rate-limited | HTTP 429 | attempt 1: HTTP 429 | needs-review | https://docs.pytest.org/en/stable | summary | retain | no | boundary | low |",
            ]
        ),
        encoding="utf-8",
    )

    try:
        _ledger_rows(ledger)
        raise AssertionError("Expected duplicate-row assertion")  # pragma: no cover
    except AssertionError as exc:
        assert "duplicate work item row" in str(exc)


def test_batch_c2_parser_rejects_missing_or_unexpected_set() -> None:
    rows = _ledger_rows()
    actual = {(row["tool_id"], row["affected_field"]) for row in rows}

    missing = sorted(EXPECTED_WORK_ITEMS - actual)
    unexpected = sorted(actual - EXPECTED_WORK_ITEMS)

    assert not missing, f"Missing expected work items in ledger: {missing}"
    assert not unexpected, f"Unexpected work items in ledger: {unexpected}"
