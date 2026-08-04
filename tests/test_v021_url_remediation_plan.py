from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
PLAN_MD = ROOT / "docs" / "maintenance" / "v0.2.1-url-remediation-plan.md"
PLAN_CSV = ROOT / "docs" / "maintenance" / "v0.2.1-url-remediation-plan.csv"
LEDGER = ROOT / "docs" / "link-review-ledger.md"
REPORT = ROOT / "reports" / "link-report.json"
SCHEMA = ROOT / "schema" / "tool.schema.json"

STRICT_CLASSES = {
    "manual-verification-required",
    "http-error",
    "tls-failure",
    "repository-archived",
}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _catalog_ids() -> set[str]:
    ids: set[str] = set()
    for path in sorted((ROOT / "data" / "tools").glob("*.yaml")):
        payload = yaml.safe_load(path.read_text(encoding="utf-8")) or []
        for record in payload:
            ids.add(record["id"])
    return ids


def _plan_rows() -> list[dict[str, str]]:
    with PLAN_CSV.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _strict_ledger_rows() -> list[dict[str, str]]:
    lines = _read(LEDGER).splitlines()
    header_idx = next(
        i for i, line in enumerate(lines) if line.startswith("| tool_id |")
    )
    rows: list[dict[str, str]] = []
    for line in lines[header_idx + 2 :]:
        if not line.startswith("|"):
            if rows:
                break
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        rows.append(
            {
                "tool_id": cells[0],
                "checked_url": cells[2],
                "result_category": cells[3],
                "candidate_replacement_url": cells[6],
            }
        )
    return rows


def _is_machine_api_endpoint(url: str) -> bool:
    parsed = urlparse(url)
    host = (parsed.hostname or "").casefold()
    path = parsed.path.casefold().rstrip("/")

    def _is_or_prefix(prefix: str) -> bool:
        return path == prefix or path.startswith(prefix + "/")

    if host == "api.github.com":
        return True
    if host == "api.githubcopilot.com" and _is_or_prefix("/graphql"):
        return True
    if _is_or_prefix("/api/v3"):
        return True
    return _is_or_prefix("/api/graphql")


def test_plan_artifacts_exist() -> None:
    assert PLAN_MD.exists(), f"Missing planning document: {PLAN_MD}"
    assert PLAN_CSV.exists(), f"Missing planning matrix: {PLAN_CSV}"


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
        row for row in _strict_ledger_rows() if row["result_category"] in STRICT_CLASSES
    ]
    strict_counts = Counter(row["result_category"] for row in strict_rows)

    assert len(strict_rows) == 38
    assert strict_counts["manual-verification-required"] == 25
    assert strict_counts["http-error"] == 2
    assert strict_counts["tls-failure"] == 1
    assert strict_counts["repository-archived"] == 10

    strict_ids = {row["tool_id"] for row in strict_rows}
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
        row for row in _strict_ledger_rows() if row["result_category"] in STRICT_CLASSES
    ]

    machine_candidates = [
        row["candidate_replacement_url"]
        for row in strict_rows
        if row["candidate_replacement_url"] != "-"
        and _is_machine_api_endpoint(row["candidate_replacement_url"])
    ]
    assert not machine_candidates, (
        f"Machine/API candidates found in strict ledger: {machine_candidates}"
    )


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
