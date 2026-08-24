from __future__ import annotations

import csv
import os
import subprocess
from collections import Counter
from pathlib import Path

import yaml

from tests.link_review_test_utils import is_machine_api_endpoint

ROOT = Path(__file__).resolve().parents[1]
LEDGER = (
    ROOT
    / "docs"
    / "maintenance"
    / "v0.2.1-license-lifecycle-remediation-batch-d-review.md"
)
PLAN_CSV = ROOT / "docs" / "maintenance" / "v0.2.1-url-remediation-plan.csv"
WORKFLOW = ROOT / ".github" / "workflows" / "quality.yml"

BATCH = "batch-d-license-lifecycle-ambiguity"
BATCH_D_BASELINE_SHA = "45dedfdecf2a80207eb0acf6585e4298078cf469"
BATCH_D_RESULT_SHA = "e04412ebfb85118d33a2f9bc584a44b8f2334259"

EXPECTED_IDS = {
    "autopwn-suite",
    "cai-robotsec",
    "ctop",
    "elastic-apm-server",
    "elastic-stack-elk",
}

EXPECTED_SCOPE = {
    "autopwn-suite": {
        "canonical_yaml_file": "data/tools/application-cloud-security.yaml",
        "affected_field": "status|needs_review|license_model|license_spdx",
        "current_canonical_value": "status=needs-review; needs_review=true; license_model=source-available",
    },
    "cai-robotsec": {
        "canonical_yaml_file": "data/tools/application-cloud-security.yaml",
        "affected_field": "status|needs_review|license_model|license_spdx",
        "current_canonical_value": "status=needs-review; needs_review=true; license_model=source-available",
    },
    "ctop": {
        "canonical_yaml_file": "data/tools/virtualization-bare-metal-homelab.yaml",
        "affected_field": "status|needs_review",
        "current_canonical_value": "status=needs-review; needs_review=true",
    },
    "elastic-apm-server": {
        "canonical_yaml_file": "data/tools/monitoring-metrics-logs-tracing.yaml",
        "affected_field": "status|needs_review|license_model|license_spdx",
        "current_canonical_value": "status=needs-review; needs_review=true; license_model=source-available",
    },
    "elastic-stack-elk": {
        "canonical_yaml_file": "data/tools/monitoring-metrics-logs-tracing.yaml",
        "affected_field": "status|needs_review|license_model|license_spdx",
        "current_canonical_value": "status=needs-review; needs_review=true; license_model=source-available",
    },
}

EXPECTED_PERMITTED_FIELDS = {
    "autopwn-suite": {"status", "needs_review", "license_model", "license_spdx"},
    "cai-robotsec": {"status", "needs_review", "license_model", "license_spdx"},
    "ctop": {"status", "needs_review"},
    "elastic-apm-server": {
        "status",
        "needs_review",
        "license_model",
        "license_spdx",
    },
    "elastic-stack-elk": {
        "status",
        "needs_review",
        "license_model",
        "license_spdx",
    },
}

REQUIRED_LEDGER_COLUMNS = {
    "tool_id",
    "canonical_yaml_file",
    "permitted_fields",
    "previous_status",
    "final_status",
    "previous_needs_review",
    "final_needs_review",
    "previous_license_model",
    "final_license_model",
    "previous_license_spdx",
    "final_license_spdx",
    "primary_sources",
    "licence_evidence",
    "lifecycle_evidence",
    "product_repository_boundary",
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
    "docs/maintenance/v0.2.1-url-remediation-batch-c2-review.md",
    "tests/test_v021_url_remediation_batch_a1.py",
    "tests/test_v021_url_remediation_batch_a2.py",
    "tests/test_v021_url_remediation_batch_b.py",
    "tests/test_v021_url_remediation_batch_c1.py",
    "tests/test_v021_url_remediation_batch_c2.py",
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


def _parse_markdown_table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _planning_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    with PLAN_CSV.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            if row.get("proposed_batch", "").strip() == BATCH:
                rows.append(row)
    return rows


def _fields_from_pipe(value: str) -> set[str]:
    normalized = value.replace("|", ",")
    return {part.strip() for part in normalized.split(",") if part.strip()}


def _ledger_rows(ledger_path: Path = LEDGER) -> list[dict[str, str]]:
    assert ledger_path.exists(), f"Missing batch D review ledger: {ledger_path}"

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
        f"{ledger_path}: could not find Batch D evidence table header"
    )

    missing_columns = REQUIRED_LEDGER_COLUMNS - set(header_cells)
    assert not missing_columns, (
        f"{ledger_path}:{header_line_idx + 1}: missing required header columns: "
        f"{sorted(missing_columns)}"
    )

    expected_count = len(header_cells)
    header_index = {name: i for i, name in enumerate(header_cells)}

    rows: list[dict[str, str]] = []
    seen_ids: set[str] = set()

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
        tool_id = row["tool_id"]
        assert tool_id not in seen_ids, (
            f"{ledger_path}:{line_idx}: duplicate tool_id row: {tool_id}"
        )
        seen_ids.add(tool_id)
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


def _load_tool_at_rev(rev: str, yaml_file: str, tool_id: str) -> dict:
    try:
        result = subprocess.run(
            ["git", "show", f"{rev}:{yaml_file}"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError as exc:
        stderr = (exc.stderr or "").strip()
        raise AssertionError(
            f"Unable to load {yaml_file} at {rev}: {stderr or exc}"
        ) from exc

    payload = yaml.safe_load(result.stdout)
    assert isinstance(payload, list), f"Expected list in {yaml_file} at {rev}"
    by_id = {
        record["id"]: record
        for record in payload
        if isinstance(record, dict) and "id" in record
    }
    assert tool_id in by_id, f"Tool {tool_id!r} missing in {yaml_file} at {rev}"
    return by_id[tool_id]


def _require_batch_d_refs() -> None:
    import pytest

    refs = [
        ("baseline", BATCH_D_BASELINE_SHA),
        ("result", BATCH_D_RESULT_SHA),
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
                "Git executable is required for Batch D pinned baseline/result invariants"
            ) from exc
        except subprocess.CalledProcessError as exc:
            if os.getenv("GITHUB_ACTIONS") == "true":
                raise AssertionError(
                    f"{label.capitalize()} commit {sha} is not reachable in this "
                    "GitHub Actions checkout, so Batch D invariants cannot be "
                    "enforced. Required refs: "
                    f"{BATCH_D_BASELINE_SHA} -> {BATCH_D_RESULT_SHA}. "
                    "Verify .github/workflows/quality.yml checkout uses fetch-depth: 0."
                ) from exc

            pytest.skip(
                f"{label.capitalize()} commit {sha} is not reachable in this local "
                "shallow/partial clone; skipping Batch D pinned baseline/result invariants "
                f"({BATCH_D_BASELINE_SHA} -> {BATCH_D_RESULT_SHA})"
            )


def _git_diff_name_only(paths: list[str]) -> set[str]:
    _require_batch_d_refs()

    cmd = [
        "git",
        "diff",
        "--name-only",
        BATCH_D_BASELINE_SHA,
        BATCH_D_RESULT_SHA,
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
            "Unable to compute Batch D baseline/result diff using explicit "
            f"two-commit range ({BATCH_D_BASELINE_SHA} {BATCH_D_RESULT_SHA}): "
            f"{stderr or exc}"
        ) from exc

    return {line.strip() for line in result.stdout.splitlines() if line.strip()}


def _canonical_fields_for_id(tool_id: str, row: dict[str, str]) -> dict[str, str]:
    values = {
        "status": row["final_status"],
        "needs_review": row["final_needs_review"],
        "license_model": row["final_license_model"],
        "license_spdx": row["final_license_spdx"],
    }
    return values


# ---------------------------------------------------------------------------
# Scope lock
# ---------------------------------------------------------------------------


def test_batch_d_selector_and_scope_counts() -> None:
    rows = _planning_rows()
    assert len(rows) == 5, f"Expected 5 planning rows, got {len(rows)}"

    ids = [row["tool_id"] for row in rows]
    counts = Counter(ids)

    assert set(ids) == EXPECTED_IDS
    assert len(set(ids)) == 5

    dup_ids = sorted(tool_id for tool_id, count in counts.items() if count > 1)
    assert dup_ids == [], f"Expected no duplicate IDs, got {dup_ids}"


def test_batch_d_exact_work_items_and_scope_values() -> None:
    rows = _planning_rows()
    for row in rows:
        tool_id = row["tool_id"]
        expected = EXPECTED_SCOPE[tool_id]
        assert row["canonical_yaml_file"] == expected["canonical_yaml_file"]
        assert row["affected_field"] == expected["affected_field"]
        assert row["current_canonical_value"] == expected["current_canonical_value"]


def test_batch_d_exact_permitted_field_set_per_id() -> None:
    rows = _planning_rows()
    actual = {row["tool_id"]: _fields_from_pipe(row["affected_field"]) for row in rows}
    assert actual == EXPECTED_PERMITTED_FIELDS


# ---------------------------------------------------------------------------
# Ledger coherence and field boundaries
# ---------------------------------------------------------------------------


def test_batch_d_ledger_exists_and_exactly_covers_selected_ids() -> None:
    ledger = _ledger_rows()
    assert len(ledger) == 5, f"Expected 5 ledger rows, got {len(ledger)}"

    actual_ids = {row["tool_id"] for row in ledger}
    assert actual_ids == EXPECTED_IDS, (
        f"Ledger selected-ID mismatch. Missing: {sorted(EXPECTED_IDS - actual_ids)}. "
        f"Extra: {sorted(actual_ids - EXPECTED_IDS)}"
    )


def test_batch_d_ledger_permitted_fields_match_scope() -> None:
    for row in _ledger_rows():
        tool_id = row["tool_id"]
        ledger_fields = _fields_from_pipe(row["permitted_fields"])
        assert ledger_fields == EXPECTED_PERMITTED_FIELDS[tool_id]


def test_batch_d_no_url_fields_changed() -> None:
    # Batch D is lifecycle/license ambiguity only; URL fields must stay untouched.
    changed = _git_diff_name_only(["data/tools/"])
    assert changed == set(), (
        "No canonical YAML changes were expected in Batch D; changed files: "
        f"{sorted(changed)}"
    )


def test_batch_d_no_non_selected_or_non_permitted_field_changes() -> None:
    planning = {row["tool_id"]: row for row in _planning_rows()}
    for row in _ledger_rows():
        tool_id = row["tool_id"]
        permitted = EXPECTED_PERMITTED_FIELDS[tool_id]

        changed_fields = set()
        if row["previous_status"] != row["final_status"]:
            changed_fields.add("status")
        if row["previous_needs_review"] != row["final_needs_review"]:
            changed_fields.add("needs_review")
        if row["previous_license_model"] != row["final_license_model"]:
            changed_fields.add("license_model")
        if row["previous_license_spdx"] != row["final_license_spdx"]:
            changed_fields.add("license_spdx")

        assert changed_fields <= permitted, (
            f"Changed non-permitted fields for {tool_id}: {sorted(changed_fields - permitted)}"
        )

        expected_file = EXPECTED_SCOPE[tool_id]["canonical_yaml_file"]
        assert planning[tool_id]["canonical_yaml_file"] == expected_file


def test_batch_d_ledger_previous_values_match_pinned_baseline() -> None:
    planning = {row["tool_id"]: row for row in _planning_rows()}
    for row in _ledger_rows():
        tool_id = row["tool_id"]
        yaml_file = planning[tool_id]["canonical_yaml_file"]
        baseline_tool = _load_tool_at_rev(BATCH_D_BASELINE_SHA, yaml_file, tool_id)

        assert row["previous_status"] == str(baseline_tool.get("status", ""))
        assert (
            row["previous_needs_review"]
            == str(baseline_tool.get("needs_review", "")).lower()
        )
        assert row["previous_license_model"] == str(
            baseline_tool.get("license_model", "")
        )
        assert row["previous_license_spdx"] == str(
            baseline_tool.get("license_spdx", "") or ""
        )


def test_batch_d_ledger_final_values_match_pinned_result() -> None:
    planning = {row["tool_id"]: row for row in _planning_rows()}
    for row in _ledger_rows():
        tool_id = row["tool_id"]
        yaml_file = planning[tool_id]["canonical_yaml_file"]
        tool = _load_tool_at_rev(BATCH_D_RESULT_SHA, yaml_file, tool_id)

        assert row["final_status"] == str(tool.get("status", ""))
        assert row["final_needs_review"] == str(tool.get("needs_review", "")).lower()
        assert row["final_license_model"] == str(tool.get("license_model", ""))
        assert row["final_license_spdx"] == str(tool.get("license_spdx", "") or "")


def test_batch_d_changed_fields_require_authoritative_evidence() -> None:
    for row in _ledger_rows():
        changed = row["canonical_changed"] == "yes"
        if not changed:
            continue

        assert row["primary_sources"].strip(), (
            f"Changed row missing primary_sources for {row['tool_id']}"
        )
        assert row["licence_evidence"].strip(), (
            f"Changed row missing licence_evidence for {row['tool_id']}"
        )
        assert row["lifecycle_evidence"].strip(), (
            f"Changed row missing lifecycle_evidence for {row['tool_id']}"
        )


def test_batch_d_spdx_change_requires_explicit_spdx_evidence() -> None:
    for row in _ledger_rows():
        if row["previous_license_spdx"] == row["final_license_spdx"]:
            continue

        evidence = row["licence_evidence"].lower()
        assert "spdx" in evidence or "license" in evidence or "licence" in evidence, (
            f"SPDX changed without explicit evidence language for {row['tool_id']}"
        )


def test_batch_d_needs_review_false_requires_no_unresolved_boundary() -> None:
    for row in _ledger_rows():
        if row["final_needs_review"] != "false":
            continue
        boundary = row["remaining_boundary"].strip().lower()
        assert boundary in {"", "none", "n/a", "na", "-"}, (
            f"needs_review=false requires no unresolved boundary for {row['tool_id']}"
        )


def test_batch_d_inconclusive_rows_keep_needs_review_true() -> None:
    for row in _ledger_rows():
        if "inconclusive" not in row["final_decision"].lower():
            continue
        assert row["final_needs_review"] == "true", (
            f"Inconclusive record must preserve needs_review=true for {row['tool_id']}"
        )


def test_batch_d_canonical_changed_flag_is_coherent() -> None:
    for row in _ledger_rows():
        any_difference = any(
            [
                row["previous_status"] != row["final_status"],
                row["previous_needs_review"] != row["final_needs_review"],
                row["previous_license_model"] != row["final_license_model"],
                row["previous_license_spdx"] != row["final_license_spdx"],
            ]
        )
        assert (row["canonical_changed"] == "yes") == any_difference, (
            f"canonical_changed coherence failed for {row['tool_id']}"
        )


def test_batch_d_no_machine_api_endpoint_introduced() -> None:
    planning = {row["tool_id"]: row for row in _planning_rows()}
    machine_candidates = []

    for row in _ledger_rows():
        if row["canonical_changed"] != "yes":
            continue

        tool_id = row["tool_id"]
        yaml_file = planning[tool_id]["canonical_yaml_file"]
        tool = _load_tool(yaml_file, tool_id)

        for field in ["official_url", "documentation_url", "repository_url"]:
            value = tool.get(field)
            if isinstance(value, str) and value and is_machine_api_endpoint(value):
                machine_candidates.append((tool_id, field, value))

    assert not machine_candidates, (
        f"Machine/API canonical URL candidates found: {machine_candidates}"
    )


def test_batch_d_no_lost_or_new_selected_ids() -> None:
    expected = set(EXPECTED_IDS)
    present = set()
    planning = _planning_rows()

    for row in planning:
        tool = _load_tool(row["canonical_yaml_file"], row["tool_id"])
        present.add(tool["id"])

    lost = sorted(expected - present)
    new = sorted(present - expected)
    assert not lost, f"Lost selected IDs: {lost}"
    assert not new, f"Unexpected new selected IDs: {new}"


# ---------------------------------------------------------------------------
# Baseline and diff invariants
# ---------------------------------------------------------------------------


def test_batch_d_baseline_available_succeeds() -> None:
    import unittest.mock as mock

    with mock.patch(
        "subprocess.run",
        return_value=subprocess.CompletedProcess(
            ["git", "cat-file"], 0, stdout="", stderr=""
        ),
    ):
        _require_batch_d_refs()


def test_batch_d_baseline_missing_local_skips(monkeypatch: object) -> None:
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
        _require_batch_d_refs()

    text = str(exc_info.value)
    assert BATCH_D_BASELINE_SHA in text
    assert BATCH_D_RESULT_SHA in text
    assert "local" in text
    assert "shallow/partial clone" in text


def test_batch_d_baseline_missing_in_ci_fails_actionably(monkeypatch: object) -> None:
    import unittest.mock as mock

    monkeypatch.setenv("GITHUB_ACTIONS", "true")

    with mock.patch(
        "subprocess.run",
        side_effect=subprocess.CalledProcessError(
            128, "git", stderr="not a valid object"
        ),
    ):
        try:
            _require_batch_d_refs()
            raise AssertionError(  # pragma: no cover
                "Expected AssertionError when baseline is missing in CI"
            )
        except AssertionError as exc:
            text = str(exc)
            assert BATCH_D_BASELINE_SHA in text
            assert BATCH_D_RESULT_SHA in text
            assert "Batch D invariants cannot be enforced" in text
            assert "fetch-depth: 0" in text


def test_batch_d_result_missing_local_skips(monkeypatch: object) -> None:
    import unittest.mock as mock

    import pytest

    monkeypatch.delenv("GITHUB_ACTIONS", raising=False)

    def _side_effect(*args: object, **kwargs: object) -> subprocess.CompletedProcess:
        cmd = list(args[0])
        if f"{BATCH_D_BASELINE_SHA}^{{commit}}" in cmd:
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")
        if f"{BATCH_D_RESULT_SHA}^{{commit}}" in cmd:
            raise subprocess.CalledProcessError(128, cmd, stderr="not a valid object")
        return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

    with (
        mock.patch("subprocess.run", side_effect=_side_effect),
        pytest.raises(pytest.skip.Exception) as exc_info,
    ):
        _require_batch_d_refs()

    text = str(exc_info.value)
    assert BATCH_D_BASELINE_SHA in text
    assert BATCH_D_RESULT_SHA in text
    assert "local" in text


def test_batch_d_result_missing_in_ci_fails_actionably(monkeypatch: object) -> None:
    import unittest.mock as mock

    monkeypatch.setenv("GITHUB_ACTIONS", "true")

    def _side_effect(*args: object, **kwargs: object) -> subprocess.CompletedProcess:
        cmd = list(args[0])
        if f"{BATCH_D_BASELINE_SHA}^{{commit}}" in cmd:
            return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")
        if f"{BATCH_D_RESULT_SHA}^{{commit}}" in cmd:
            raise subprocess.CalledProcessError(128, cmd, stderr="not a valid object")
        return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

    with mock.patch("subprocess.run", side_effect=_side_effect):
        try:
            _require_batch_d_refs()
            raise AssertionError(  # pragma: no cover
                "Expected AssertionError when result is missing in CI"
            )
        except AssertionError as exc:
            text = str(exc)
            assert BATCH_D_BASELINE_SHA in text
            assert BATCH_D_RESULT_SHA in text
            assert "Batch D invariants cannot be enforced" in text
            assert "fetch-depth: 0" in text


def test_batch_d_git_unavailable_fails_actionably() -> None:
    import unittest.mock as mock

    with mock.patch("subprocess.run", side_effect=FileNotFoundError("git missing")):
        try:
            _require_batch_d_refs()
            raise AssertionError(  # pragma: no cover
                "Expected AssertionError when git executable is unavailable"
            )
        except AssertionError as exc:
            assert "Git executable is required" in str(exc)


def test_batch_d_protected_files_unchanged_since_baseline() -> None:
    changed = _git_diff_name_only(PROTECTED_PATHS)
    assert changed == set(), (
        f"Protected files changed since Batch D baseline: {sorted(changed)}"
    )


def test_batch_d_diff_commands_use_explicit_two_commit_range() -> None:
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
    assert BATCH_D_BASELINE_SHA in cmd
    assert BATCH_D_RESULT_SHA in cmd
    idx = cmd.index(BATCH_D_BASELINE_SHA)
    assert cmd[idx + 1] == BATCH_D_RESULT_SHA, (
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


def test_batch_d_parser_missing_file_is_actionable(tmp_path: Path) -> None:
    missing = tmp_path / "missing.md"
    try:
        _ledger_rows(missing)
        raise AssertionError("Expected missing ledger assertion")  # pragma: no cover
    except AssertionError as exc:
        msg = str(exc)
        assert "Missing batch D review ledger" in msg
        assert str(missing) in msg


def test_batch_d_parser_empty_file_fails_actionably(tmp_path: Path) -> None:
    ledger = tmp_path / "empty.md"
    ledger.write_text("", encoding="utf-8")

    try:
        _ledger_rows(ledger)
        raise AssertionError("Expected empty-ledger assertion")  # pragma: no cover
    except AssertionError as exc:
        text = str(exc)
        assert "could not find Batch D evidence table header" in text
        assert str(ledger) in text


def test_batch_d_parser_missing_required_column_fails(tmp_path: Path) -> None:
    ledger = tmp_path / "missing-column.md"
    ledger.write_text(
        "\n".join(
            [
                "| tool_id | final_decision |",
                "|---|---|",
                "| ctop | retain |",
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


def test_batch_d_parser_malformed_row_fails_with_line_number(tmp_path: Path) -> None:
    ledger = tmp_path / "malformed.md"
    ledger.write_text(
        "\n".join(
            [
                "| tool_id | canonical_yaml_file | permitted_fields | previous_status | final_status | previous_needs_review | final_needs_review | previous_license_model | final_license_model | previous_license_spdx | final_license_spdx | primary_sources | licence_evidence | lifecycle_evidence | product_repository_boundary | final_decision | canonical_changed | remaining_boundary | risk |",
                "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
                "| ctop | data/tools/virtualization-bare-metal-homelab.yaml | status, needs_review | needs-review | needs-review | true | true | oss | oss | MIT | MIT | https://github.com/bcicen/ctop | MIT license text | no archival signal | repo is project of record | retain | no | unresolved lifecycle statement |",
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


def test_batch_d_parser_duplicate_id_rejected(tmp_path: Path) -> None:
    ledger = tmp_path / "dup.md"
    ledger.write_text(
        "\n".join(
            [
                "| tool_id | canonical_yaml_file | permitted_fields | previous_status | final_status | previous_needs_review | final_needs_review | previous_license_model | final_license_model | previous_license_spdx | final_license_spdx | primary_sources | licence_evidence | lifecycle_evidence | product_repository_boundary | final_decision | canonical_changed | remaining_boundary | risk |",
                "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
                "| ctop | data/tools/virtualization-bare-metal-homelab.yaml | status, needs_review | needs-review | needs-review | true | true | oss | oss | MIT | MIT | https://github.com/bcicen/ctop | MIT license text | no archival signal | repo is project of record | retain | no | unresolved lifecycle statement | medium |",
                "| ctop | data/tools/virtualization-bare-metal-homelab.yaml | status, needs_review | needs-review | needs-review | true | true | oss | oss | MIT | MIT | https://github.com/bcicen/ctop | MIT license text | no archival signal | repo is project of record | retain | no | unresolved lifecycle statement | medium |",
            ]
        ),
        encoding="utf-8",
    )

    try:
        _ledger_rows(ledger)
        raise AssertionError("Expected duplicate-row assertion")  # pragma: no cover
    except AssertionError as exc:
        assert "duplicate tool_id row" in str(exc)


def test_batch_d_parser_rejects_missing_or_unexpected_ids() -> None:
    rows = _ledger_rows()
    actual_ids = {row["tool_id"] for row in rows}

    missing = sorted(EXPECTED_IDS - actual_ids)
    unexpected = sorted(actual_ids - EXPECTED_IDS)

    assert not missing, f"Missing expected IDs in ledger: {missing}"
    assert not unexpected, f"Unexpected IDs in ledger: {unexpected}"
