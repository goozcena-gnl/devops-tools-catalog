from __future__ import annotations

import csv
import subprocess
from collections import Counter, defaultdict
from copy import deepcopy
from functools import cache
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/maintenance/v0.2.2-carryover-execution-manifest.yaml"
PLAN_CSV = ROOT / "docs/maintenance/v0.2.1-url-remediation-plan.csv"
SCHEMA = ROOT / "schema/tool.schema.json"
CATALOG_DIR = ROOT / "data/tools"

EXPECTED_SOURCE_SHA = "dc7cfd457a7c9638b1132048792092c8b5e3ae02"
EXPECTED_UNIQUE_IDS = 63
EXPECTED_FIELD_ROWS = 82
EXPECTED_TOP_LEVEL_KEYS = {
    "manifest_version",
    "source_release",
    "source_main_sha",
    "execution_baseline_policy",
    "scope_policy",
    "expected_unique_ids",
    "expected_field_level_work_items",
    "excluded_global_needs_review_population",
    "logical_workstreams",
    "execution_sub_batches",
    "hold_register",
    "multi_field_ids",
    "global_invariants",
    "work_items",
}
EXPECTED_WORK_ITEM_KEYS = {
    "sequence_number",
    "logical_workstream",
    "execution_sub_batch",
    "tool_id",
    "canonical_yaml_file",
    "affected_field",
    "current_value",
    "current_status",
    "current_needs_review",
    "current_license_model",
    "current_license_spdx",
    "v021_source_batch",
    "v021_report_classification",
    "v021_previous_decision",
    "v021_evidence_sources",
    "unresolved_boundary",
    "authoritative_evidence_required",
    "allowed_decisions",
    "forbidden_decisions",
    "risk_level",
    "readiness_class",
    "implementation_dependency",
    "regression_test_requirement",
    "human_review_requirement",
    "hold_reason",
}
EXPECTED_STREAM_COUNTS = {
    "N1": (35, 30),
    "N2": (24, 23),
    "N3": (5, 5),
    "N4": (18, 5),
}
EXPECTED_BATCH_COUNTS = {
    "N1a": (25, 20),
    "N1b": (10, 10),
    "N2a": (21, 20),
    "N2b": (3, 3),
    "N3a": (5, 5),
    "HOLD": (18, 5),
}
ALLOWED_WORKSTREAMS = set(EXPECTED_STREAM_COUNTS)
ALLOWED_EXECUTION_BATCHES = set(EXPECTED_BATCH_COUNTS)
EXPECTED_MULTI_FIELD_IDS = {
    "ansible-lint",
    "argo-workflows",
    "argocd",
    "argocd-image-updater",
    "argocd-vault-plugin",
    "hoji-ai",
    "autopwn-suite",
    "cai-robotsec",
    "ctop",
    "elastic-apm-server",
    "elastic-stack-elk",
}
EXCLUDED_CHANGED_IDS = {
    "deeptutor",
    "odysseus",
    "terraform-cloud",
    "trivy",
    "yokecd",
    "cdktf",
    "kaniko",
    "keptn",
    "kubeapps",
    "tnu",
}
N4_IDS = {
    "autopwn-suite",
    "cai-robotsec",
    "ctop",
    "elastic-apm-server",
    "elastic-stack-elk",
}
LEDGER_BY_SOURCE_BATCH = {
    "batch-a1-hard-url-failures": "docs/maintenance/v0.2.1-url-remediation-batch-a1-review.md",
    "batch-a2-hard-url-failures": "docs/maintenance/v0.2.1-url-remediation-batch-a2-review.md",
    "batch-b-archived-boundary": "docs/maintenance/v0.2.1-url-remediation-batch-b-review.md",
    "batch-c1-access-retry": "docs/maintenance/v0.2.1-url-remediation-batch-c1-review.md",
    "batch-c2-access-retry": "docs/maintenance/v0.2.1-url-remediation-batch-c2-review.md",
    "batch-d-license-lifecycle-ambiguity": "docs/maintenance/v0.2.1-license-lifecycle-remediation-batch-d-review.md",
}
READINESS_BY_CLASSIFICATION = {
    "manual-verification-required": "READY_PRIMARY_EVIDENCE",
    "http-error": "READY_PRIMARY_EVIDENCE",
    "tls-failure": "READY_PRIMARY_EVIDENCE",
    "rate-limited": "READY_CONTROLLED_RETRY",
    "restricted-or-bot-blocked": "READY_CONTROLLED_RETRY",
    "transient-failure": "READY_CONTROLLED_RETRY",
    "dns-inconclusive": "READY_CONTROLLED_RETRY",
    "repository-archived": "READY_GOVERNANCE_VERIFICATION",
    "lifecycle-license-ambiguity": "HOLD_NO_NEW_EVIDENCE",
}


def _read_yaml_mapping(path: Path = MANIFEST) -> dict:
    assert path.exists(), f"Missing manifest: {path}"
    text = path.read_text(encoding="utf-8")
    assert text.strip(), f"Manifest is empty: {path}"
    payload = yaml.safe_load(text)
    assert isinstance(payload, dict), "Manifest must be a YAML mapping"
    return payload


def _read_plan_rows() -> list[dict[str, str]]:
    with PLAN_CSV.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _expanded_frozen_plan() -> dict[tuple[str, str], dict[str, str]]:
    expanded = {}
    for row in _read_plan_rows():
        if row["tool_id"] in EXCLUDED_CHANGED_IDS:
            continue
        for field in row["affected_field"].split("|"):
            key = (row["tool_id"], field)
            assert key not in expanded, f"Duplicate frozen planning row: {key}"
            expanded[key] = row
    return expanded


def _catalog_file_records(path: Path) -> list[dict]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        records = payload
    else:
        assert isinstance(payload, dict), (
            f"Canonical file must be a mapping/list: {path}"
        )
        records = payload.get("tools")
    assert isinstance(records, list), f"Canonical tools must be a list: {path}"
    return records


def _index_canonical_records(paths: list[Path]) -> dict[str, tuple[Path, dict]]:
    by_id: dict[str, tuple[Path, dict]] = {}
    for path in paths:
        for record in _catalog_file_records(path):
            assert isinstance(record, dict), f"Malformed canonical record in {path}"
            tool_id = record.get("id")
            assert isinstance(tool_id, str) and tool_id, (
                f"Missing canonical ID in {path}"
            )
            assert tool_id not in by_id, f"Duplicate canonical ID: {tool_id}"
            by_id[tool_id] = (path, record)
    return by_id


def _canonical_index() -> dict[str, tuple[Path, dict]]:
    paths = sorted(CATALOG_DIR.glob("*.yaml"))
    assert paths, f"No canonical YAML files found under {CATALOG_DIR}"
    return _index_canonical_records(paths)


def _canonical_index_at(revision: str) -> dict[str, tuple[Path, dict]]:
    try:
        listing = subprocess.run(
            [
                "git",
                "ls-tree",
                "-r",
                "--name-only",
                revision,
                "--",
                "data/tools/",
            ],
            cwd=ROOT,
            capture_output=True,
            encoding="utf-8",
            check=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError) as exc:
        raise AssertionError(
            f"Unable to load frozen canonical snapshot {revision}"
        ) from exc

    by_id: dict[str, tuple[Path, dict]] = {}
    yaml_paths = [
        line for line in listing.stdout.splitlines() if line.endswith(".yaml")
    ]
    assert yaml_paths, f"No canonical YAML in frozen snapshot {revision}"
    for relative in yaml_paths:
        try:
            shown = subprocess.run(
                ["git", "show", f"{revision}:{relative}"],
                cwd=ROOT,
                capture_output=True,
                encoding="utf-8",
                check=True,
            )
        except (FileNotFoundError, subprocess.CalledProcessError) as exc:
            raise AssertionError(
                f"Unable to read frozen canonical file {revision}:{relative}"
            ) from exc
        payload = yaml.safe_load(shown.stdout)
        records = payload if isinstance(payload, list) else payload.get("tools")
        assert isinstance(records, list), (
            f"Canonical tools must be a list: {revision}:{relative}"
        )
        path = ROOT / relative
        for record in records:
            tool_id = record.get("id") if isinstance(record, dict) else None
            assert isinstance(tool_id, str) and tool_id
            assert tool_id not in by_id, f"Duplicate canonical ID: {tool_id}"
            by_id[tool_id] = (path, record)
    return by_id


@cache
def _schema_fields() -> frozenset[str]:
    import json

    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return frozenset(schema["properties"])


def _canonical_value(record: dict, field: str):
    assert field in _schema_fields(), f"Unknown canonical field: {field}"
    if field in record:
        return record[field]
    # Preserve the absence of an optional SPDX value without manufacturing one.
    assert field == "license_spdx", f"Missing affected field: {field}"
    return None


def _validate_structure(payload: dict) -> None:
    assert set(payload) == EXPECTED_TOP_LEVEL_KEYS, "Unexpected top-level keys"
    assert payload["manifest_version"] == 1
    assert payload["source_release"] == "v0.2.1"
    assert payload["source_main_sha"] == EXPECTED_SOURCE_SHA
    assert payload["execution_baseline_policy"] == "pin_current_main_at_batch_start"
    assert "execution_baseline_sha" not in payload
    assert payload["scope_policy"] == "reviewed_but_unchanged_carryover_only"
    assert payload["expected_unique_ids"] == EXPECTED_UNIQUE_IDS
    assert payload["expected_field_level_work_items"] == EXPECTED_FIELD_ROWS
    assert payload["excluded_global_needs_review_population"] is True

    rows = payload["work_items"]
    assert isinstance(rows, list), "work_items must be a list"
    assert len(rows) == EXPECTED_FIELD_ROWS
    for index, row in enumerate(rows, start=1):
        assert isinstance(row, dict), f"Malformed work item at position {index}"
        assert set(row) == EXPECTED_WORK_ITEM_KEYS, (
            f"Unexpected work-item keys at position {index}"
        )
        for key in (
            "tool_id",
            "canonical_yaml_file",
            "affected_field",
            "v021_report_classification",
            "risk_level",
            "readiness_class",
        ):
            assert isinstance(row[key], str) and row[key].strip(), (
                f"Empty {key} at position {index}"
            )
        assert row["logical_workstream"] in ALLOWED_WORKSTREAMS, (
            f"Unknown logical workstream: {row['logical_workstream']}"
        )
        assert row["execution_sub_batch"] in ALLOWED_EXECUTION_BATCHES, (
            f"Unknown execution batch: {row['execution_sub_batch']}"
        )
        assert str(row["allowed_decisions"]).strip()
        assert str(row["forbidden_decisions"]).strip()
        assert row["allowed_decisions"] != row["forbidden_decisions"]

    sequence_numbers = [row["sequence_number"] for row in rows]
    assert sequence_numbers == list(range(1, EXPECTED_FIELD_ROWS + 1)), (
        "Sequence numbers must be exactly 1 through 82"
    )
    field_rows = [(row["tool_id"], row["affected_field"]) for row in rows]
    assert len(field_rows) == len(set(field_rows)), "Duplicate field row"


def _validate_accounting(payload: dict) -> None:
    rows = payload["work_items"]
    assert len({row["tool_id"] for row in rows}) == EXPECTED_UNIQUE_IDS

    stream_headers = {entry["id"]: entry for entry in payload["logical_workstreams"]}
    assert set(stream_headers) == ALLOWED_WORKSTREAMS
    for stream, (row_count, unique_count) in EXPECTED_STREAM_COUNTS.items():
        assert stream_headers[stream]["field_level_rows"] == row_count
        assert stream_headers[stream]["unique_ids"] == unique_count
    assert stream_headers["N4"]["execution_state"] == "HOLD_NO_NEW_EVIDENCE"

    for stream, (row_count, unique_count) in EXPECTED_STREAM_COUNTS.items():
        selected = [row for row in rows if row["logical_workstream"] == stream]
        assert len(selected) == row_count, f"Wrong row count for {stream}"
        assert len({row["tool_id"] for row in selected}) == unique_count, (
            f"Wrong unique-ID count for {stream}"
        )

    for batch, (row_count, unique_count) in EXPECTED_BATCH_COUNTS.items():
        selected = [row for row in rows if row["execution_sub_batch"] == batch]
        assert len(selected) == row_count, f"Wrong row count for {batch}"
        assert len({row["tool_id"] for row in selected}) == unique_count, (
            f"Wrong unique-ID count for {batch}"
        )

    batch_headers = payload["execution_sub_batches"]
    assert {entry["id"] for entry in batch_headers} == (
        ALLOWED_EXECUTION_BATCHES - {"HOLD"}
    )
    for entry in batch_headers:
        assert set(entry) == {
            "id",
            "parent_workstream",
            "max_unique_ids",
            "unique_ids",
            "tool_ids",
        }
        assert entry["max_unique_ids"] == 20
        assert entry["unique_ids"] == len(set(entry["tool_ids"])) <= 20
        manifest_ids = {
            row["tool_id"] for row in rows if row["execution_sub_batch"] == entry["id"]
        }
        assert set(entry["tool_ids"]) == manifest_ids
        assert all(
            row["logical_workstream"] == entry["parent_workstream"]
            for row in rows
            if row["execution_sub_batch"] == entry["id"]
        )

    ownership: dict[str, set[str]] = defaultdict(set)
    for row in rows:
        if row["execution_sub_batch"] != "HOLD":
            ownership[row["tool_id"]].add(row["execution_sub_batch"])
    assert all(len(batches) == 1 for batches in ownership.values())

    n4_rows = [row for row in rows if row["logical_workstream"] == "N4"]
    assert {row["tool_id"] for row in n4_rows} == N4_IDS
    for row in n4_rows:
        assert row["execution_sub_batch"] == "HOLD"
        assert row["readiness_class"] == "HOLD_NO_NEW_EVIDENCE"
        assert str(row["hold_reason"]).strip() not in {"", "n/a"}

    counts = Counter(row["tool_id"] for row in rows)
    actual_multi = {tool_id for tool_id, count in counts.items() if count > 1}
    assert actual_multi == EXPECTED_MULTI_FIELD_IDS
    declared_multi = {
        entry["tool_id"]: entry["field_level_rows"]
        for entry in payload["multi_field_ids"]
    }
    assert declared_multi == {
        tool_id: counts[tool_id] for tool_id in EXPECTED_MULTI_FIELD_IDS
    }

    hold = payload["hold_register"]
    assert len(hold) == 1
    assert set(hold[0]["tool_ids"]) == N4_IDS
    assert hold[0]["row_count"] == 18


def _validate_frozen_scope(payload: dict) -> None:
    frozen = _expanded_frozen_plan()
    actual = {(row["tool_id"], row["affected_field"]) for row in payload["work_items"]}
    assert actual == set(frozen), "Missing or extra frozen field rows"
    actual_ids = {tool_id for tool_id, _field in actual}
    assert actual_ids.isdisjoint(EXCLUDED_CHANGED_IDS)


def _validate_canonical_parity(payload: dict) -> None:
    by_id = _canonical_index_at(payload["source_main_sha"])
    for row in payload["work_items"]:
        tool_id = row["tool_id"]
        assert tool_id in by_id, f"Missing canonical ID: {tool_id}"
        actual_path, record = by_id[tool_id]
        declared_path = ROOT / row["canonical_yaml_file"]
        assert declared_path.exists(), f"Missing canonical file: {declared_path}"
        assert actual_path.resolve() == declared_path.resolve(), (
            f"Canonical ID is not in declared file: {tool_id}"
        )

        field = row["affected_field"]
        current_value = _canonical_value(record, field)
        assert row["current_value"] == current_value, (
            f"Canonical-value mismatch: {tool_id}.{field}"
        )
        assert row["current_status"] == record["status"]
        assert row["current_needs_review"] is record["needs_review"]
        assert row["current_license_model"] == record["license_model"]
        assert row["current_license_spdx"] == _canonical_value(record, "license_spdx")


def _validate_evidence(payload: dict) -> None:
    frozen = _expanded_frozen_plan()
    ledger_cache = {}
    for row in payload["work_items"]:
        key = (row["tool_id"], row["affected_field"])
        plan_row = frozen[key]
        assert row["v021_source_batch"] == plan_row["proposed_batch"]
        assert row["v021_report_classification"] == plan_row["report_classification"]

        expected_ledger = LEDGER_BY_SOURCE_BATCH[row["v021_source_batch"]]
        source_parts = [
            part.strip() for part in row["v021_evidence_sources"].split(";")
        ]
        assert source_parts == [row["v021_source_batch"], expected_ledger]
        assert "batch-batch" not in expected_ledger
        ledger_path = ROOT / expected_ledger
        assert ledger_path.exists(), f"Missing source ledger: {ledger_path}"
        ledger_text = ledger_cache.setdefault(
            ledger_path, ledger_path.read_text(encoding="utf-8")
        )
        assert row["tool_id"] in ledger_text, (
            f"Tool is not traceable to ledger: {row['tool_id']}"
        )

        expected_readiness = READINESS_BY_CLASSIFICATION[
            row["v021_report_classification"]
        ]
        assert row["readiness_class"] == expected_readiness
        allowed = {part.strip() for part in row["allowed_decisions"].split("|")}
        forbidden = {part.strip() for part in row["forbidden_decisions"].split("|")}
        assert all(allowed) and all(forbidden)
        assert allowed.isdisjoint(forbidden)
        if row["logical_workstream"] == "N4":
            assert any(
                decision.startswith("retain safest canonical state only")
                for decision in allowed
            )


def test_manifest_is_complete_and_consistent() -> None:
    payload = _read_yaml_mapping()
    _validate_structure(payload)
    _validate_accounting(payload)
    _validate_frozen_scope(payload)
    _validate_canonical_parity(payload)
    _validate_evidence(payload)


@pytest.mark.parametrize("content", ["", "[]\n"])
def test_manifest_reader_rejects_empty_or_non_mapping(
    tmp_path: Path, content: str
) -> None:
    manifest = tmp_path / "manifest.yaml"
    manifest.write_text(content, encoding="utf-8")
    with pytest.raises(AssertionError):
        _read_yaml_mapping(manifest)


def test_manifest_reader_rejects_missing_manifest(tmp_path: Path) -> None:
    with pytest.raises(AssertionError, match="Missing manifest"):
        _read_yaml_mapping(tmp_path / "missing.yaml")


def test_structure_rejects_missing_top_level_key() -> None:
    payload = deepcopy(_read_yaml_mapping())
    del payload["source_release"]
    with pytest.raises(AssertionError, match="top-level"):
        _validate_structure(payload)


@pytest.mark.parametrize("mutation", ["missing_key", "malformed_item"])
def test_structure_rejects_malformed_work_items(mutation: str) -> None:
    payload = deepcopy(_read_yaml_mapping())
    if mutation == "missing_key":
        del payload["work_items"][0]["risk_level"]
    else:
        payload["work_items"][0] = "not-a-mapping"
    with pytest.raises(AssertionError, match="work.item|Malformed"):
        _validate_structure(payload)


def test_structure_rejects_duplicate_sequence_number() -> None:
    payload = deepcopy(_read_yaml_mapping())
    payload["work_items"][1]["sequence_number"] = 1
    with pytest.raises(AssertionError, match="Sequence numbers"):
        _validate_structure(payload)


def test_structure_rejects_duplicate_field_row() -> None:
    payload = deepcopy(_read_yaml_mapping())
    payload["work_items"][1]["tool_id"] = payload["work_items"][0]["tool_id"]
    payload["work_items"][1]["affected_field"] = payload["work_items"][0][
        "affected_field"
    ]
    with pytest.raises(AssertionError, match="Duplicate field row"):
        _validate_structure(payload)


@pytest.mark.parametrize(
    ("key", "bad_value", "message"),
    [
        ("logical_workstream", "N5", "Unknown logical workstream"),
        ("execution_sub_batch", "N9", "Unknown execution batch"),
    ],
)
def test_structure_rejects_unknown_stream_or_batch(
    key: str, bad_value: str, message: str
) -> None:
    payload = deepcopy(_read_yaml_mapping())
    payload["work_items"][0][key] = bad_value
    with pytest.raises(AssertionError, match=message):
        _validate_structure(payload)


@pytest.mark.parametrize(
    ("key", "bad_value", "message"),
    [
        ("canonical_yaml_file", "data/tools/missing.yaml", "Missing canonical file"),
        ("tool_id", "missing-tool", "Missing canonical ID"),
        ("affected_field", "commercial_offering", "Missing affected field"),
        ("current_value", "definitely-wrong", "Canonical-value mismatch"),
    ],
)
def test_canonical_parity_rejects_missing_or_mismatched_data(
    key: str, bad_value: str, message: str
) -> None:
    payload = deepcopy(_read_yaml_mapping())
    payload["work_items"][0][key] = bad_value
    with pytest.raises(AssertionError, match=message):
        _validate_canonical_parity(payload)


def test_canonical_index_rejects_duplicate_ids(tmp_path: Path) -> None:
    first = tmp_path / "first.yaml"
    second = tmp_path / "second.yaml"
    record = [{"id": "duplicate-id"}]
    first.write_text(yaml.safe_dump(record), encoding="utf-8")
    second.write_text(yaml.safe_dump(record), encoding="utf-8")
    with pytest.raises(AssertionError, match="Duplicate canonical ID"):
        _index_canonical_records([first, second])


def test_evidence_rejects_missing_source_ledger(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    payload = deepcopy(_read_yaml_mapping())
    monkeypatch.setitem(
        LEDGER_BY_SOURCE_BATCH,
        "batch-c1-access-retry",
        "docs/maintenance/missing-ledger.md",
    )
    payload["work_items"][0]["v021_evidence_sources"] = (
        "batch-c1-access-retry; docs/maintenance/missing-ledger.md"
    )
    with pytest.raises(AssertionError, match="Missing source ledger"):
        _validate_evidence(payload)


def test_accounting_rejects_invalid_n4_state() -> None:
    payload = deepcopy(_read_yaml_mapping())
    n4_row = next(
        row for row in payload["work_items"] if row["logical_workstream"] == "N4"
    )
    n4_row["readiness_class"] = "READY_PRIMARY_EVIDENCE"
    with pytest.raises(AssertionError):
        _validate_accounting(payload)
