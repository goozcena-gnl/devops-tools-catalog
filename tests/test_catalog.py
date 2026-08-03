from __future__ import annotations

import csv

from scripts.catalog import ROOT, load_tools
from scripts.validate_catalog import validate_records
from tests.conftest import minimal_record, write_catalog


def test_duplicate_id_detection(tmp_path) -> None:
    write_catalog(tmp_path, [minimal_record(), minimal_record()])
    assert any(
        "duplicate id example-tool" in error for error in validate_records(tmp_path)
    )


def test_duplicate_canonical_url_detection(tmp_path) -> None:
    records = [
        minimal_record(),
        minimal_record(id="another-tool", name="Another Tool"),
    ]
    write_catalog(tmp_path, records)
    assert any(
        "duplicate official_url" in error for error in validate_records(tmp_path)
    )


def test_invalid_category_detection(tmp_path) -> None:
    write_catalog(tmp_path, [minimal_record(categories=["not-a-category"])])
    assert any("invalid categories" in error for error in validate_records(tmp_path))


def test_invalid_role_detection(tmp_path) -> None:
    write_catalog(tmp_path, [minimal_record(roles=["not-a-role"])])
    assert any("invalid roles" in error for error in validate_records(tmp_path))


def test_multi_category_tool_is_preserved() -> None:
    trivy = next(tool for tool in load_tools() if tool["id"] == "trivy")
    assert set(trivy["categories"]) == {
        "kubernetes-networking-storage-addons",
        "application-cloud-security",
    }


def test_arm_templates_license_is_verified() -> None:
    arm_templates = next(tool for tool in load_tools() if tool["id"] == "arm-templates")
    assert arm_templates["license_model"] == "oss"
    assert arm_templates["license_spdx"] == "MIT"
    assert arm_templates["needs_review"] is False


def test_localstack_active_tool_with_archived_repository() -> None:
    localstack = next(tool for tool in load_tools() if tool["id"] == "localstack")
    assert localstack["status"] == "active"
    assert localstack["repository_archived"] is True
    assert localstack["needs_review"] is False


def test_every_source_occurrence_has_a_disposition() -> None:
    with (ROOT / "migration" / "reconciliation.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 1894
    assert all(row["disposition"] and row["reason"] for row in rows)
