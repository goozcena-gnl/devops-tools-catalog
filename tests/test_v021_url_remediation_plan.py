from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

from tests.link_review_test_utils import (
    STRICT_CLASSES,
    is_machine_api_endpoint,
    parse_strict_ledger_rows,
)

ROOT = Path(__file__).resolve().parents[1]
PLAN_MD = ROOT / "docs" / "maintenance" / "v0.2.1-url-remediation-plan.md"
PLAN_CSV = ROOT / "docs" / "maintenance" / "v0.2.1-url-remediation-plan.csv"
LEDGER = ROOT / "docs" / "link-review-ledger.md"
REPORT = ROOT / "reports" / "link-report.json"
SCHEMA = ROOT / "schema" / "tool.schema.json"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _catalog_ids() -> set[str]:
    ids: set[str] = set()
    seen_at: dict[str, tuple[Path, int]] = {}
    for path in sorted((ROOT / "data" / "tools").glob("*.yaml")):
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert isinstance(payload, list), (
            f"{path}: expected top-level YAML list, got {type(payload).__name__}"
        )
        for idx, record in enumerate(payload):
            assert isinstance(record, dict), (
                f"{path}: record[{idx}] expected mapping, got {type(record).__name__}"
            )
            assert "id" in record, f"{path}: record[{idx}] missing required 'id'"
            record_id = record["id"]
            assert isinstance(record_id, str) and record_id.strip(), (
                f"{path}: record[{idx}] id must be a non-empty string"
            )

            previous = seen_at.get(record_id)
            assert previous is None, (
                f"Duplicate canonical id '{record_id}' in {path}: record[{idx}] "
                f"(already defined in {previous[0]}: record[{previous[1]}])"
            )

            seen_at[record_id] = (path, idx)
            ids.add(record_id)
    return ids


def _plan_rows() -> list[dict[str, str]]:
    with PLAN_CSV.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _strict_ledger_rows() -> list:
    return parse_strict_ledger_rows(LEDGER)


def test_plan_artifacts_exist() -> None:
    assert PLAN_MD.exists(), f"Missing planning document: {PLAN_MD}"
    assert PLAN_CSV.exists(), f"Missing planning matrix: {PLAN_CSV}"


def test_shared_helper_imports_are_used_by_both_test_modules() -> None:
    v021_source = _read(ROOT / "tests" / "test_v021_url_remediation_plan.py")
    ledger_source = _read(ROOT / "tests" / "test_link_review_ledger.py")
    expected_import = "from tests.link_review_test_utils import"
    assert expected_import in v021_source
    assert expected_import in ledger_source


def test_planned_ids_exist_and_are_disjoint_with_batch_limits() -> None:
    rows = _plan_rows()
    assert rows, "Planning CSV has no rows"

    catalog_ids = _catalog_ids()
    batch_to_ids: dict[str, set[str]] = defaultdict(set)
    id_to_batch: dict[str, str] = {}

    for row in rows:
        tool_id = row["tool_id"]
        batch = row["proposed_batch"]
        assert tool_id in catalog_ids, (
            f"Planned tool ID is missing from canonical YAML: {tool_id}"
        )
        batch_to_ids[batch].add(tool_id)

        previous = id_to_batch.get(tool_id)
        if previous is None:
            id_to_batch[tool_id] = batch
        else:
            assert previous == batch, (
                f"Tool ID appears in multiple batches: {tool_id} in {previous} and {batch}"
            )

    for batch, ids in sorted(batch_to_ids.items()):
        assert len(ids) <= 20, f"Batch exceeds 20-ID limit: {batch} has {len(ids)} IDs"


def test_strict_rows_and_counts_are_accounted_for() -> None:
    plan_ids = {row["tool_id"] for row in _plan_rows()}

    strict_rows = [
        row for row in _strict_ledger_rows() if row.result_category in STRICT_CLASSES
    ]
    strict_counts = Counter(row.result_category for row in strict_rows)

    assert len(strict_rows) == 38
    assert strict_counts["manual-verification-required"] == 25
    assert strict_counts["http-error"] == 2
    assert strict_counts["tls-failure"] == 1
    assert strict_counts["repository-archived"] == 10

    strict_ids = {row.tool_id for row in strict_rows}
    missing = sorted(strict_ids - plan_ids)
    assert not missing, f"Strict unresolved IDs missing from plan: {missing}"

    report = json.loads(_read(REPORT))
    summary = report["summary"]
    assert summary["manual-verification-required"] == 25
    assert summary["http-error"] == 2
    assert summary["tls-failure"] == 1
    assert summary["repository-archived"] == 10


def test_machine_api_replacement_candidates_remain_zero() -> None:
    strict_rows = [
        row for row in _strict_ledger_rows() if row.result_category in STRICT_CLASSES
    ]

    machine_candidates = [
        row.candidate_replacement_url
        for row in strict_rows
        if row.candidate_replacement_url != "-"
        and is_machine_api_endpoint(row.candidate_replacement_url)
    ]
    assert not machine_candidates, (
        f"Machine/API candidates found in strict ledger: {machine_candidates}"
    )


def test_plan_csv_header_semantics_and_lf_endings() -> None:
    raw = PLAN_CSV.read_bytes()
    assert b"\r" not in raw
    assert raw.endswith(b"\n")

    rows = _plan_rows()
    assert rows, "Planning CSV has no rows"
    headers = set(rows[0].keys())
    assert "current_catalog_status" in headers
    assert "http_status_or_network" not in headers

    status_values = {
        row["current_catalog_status"]
        for row in rows
        if row["report_classification"] != "lifecycle-license-ambiguity"
    }
    assert status_values
    assert status_values <= {"active", "archived", "needs-review"}


def test_allowed_fields_are_schema_valid() -> None:
    schema = json.loads(_read(SCHEMA))
    schema_fields = set(schema["properties"].keys())

    plan_text = _read(PLAN_MD)
    section_start = plan_text.index(
        "Allowed canonical fields during implementation batches"
    )
    section_end = plan_text.index("Prohibited in v0.2.1 implementation batches")
    section = plan_text[section_start:section_end]

    fields = re.findall(r"- `([^`]+)`", section)
    assert fields, "No allowed fields found in plan"

    invalid = sorted(set(fields) - schema_fields)
    assert not invalid, f"Plan allows non-schema fields: {invalid}"


def test_plan_contains_required_governance_boundaries() -> None:
    text = _read(PLAN_MD)

    assert re.search(r"Planning baseline `main` SHA: [0-9a-f]{40}", text)
    assert "human-review" in text.casefold()
    assert "No canonical YAML edits in this planning PR" in text
    assert "No URL/lifecycle/licence implementation in this planning PR" in text
    assert "Issue #2 can be proposed for closure only when" in text

    assert "bulk scripted replacements" in text
    assert "HTTP/network observations are triage inputs only" in text

    assert "all catalogue debt is resolved" not in text.casefold()
    assert "implementation complete" not in text.casefold()
