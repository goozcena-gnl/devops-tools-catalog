from __future__ import annotations

import json

from jsonschema import Draft202012Validator, FormatChecker

from scripts.catalog import ROOT, load_tools
from scripts.validate_catalog import validate_records
from tests.conftest import minimal_record


def test_catalogue_loads_successfully() -> None:
    tools = load_tools()
    assert len(tools) == 1092
    assert tools == sorted(tools, key=lambda item: item["id"])


def test_catalogue_passes_schema_and_taxonomy_validation() -> None:
    assert validate_records() == []


def test_schema_accepts_archived_tools() -> None:
    schema = json.loads(
        (ROOT / "schema" / "tool.schema.json").read_text(encoding="utf-8")
    )
    record = minimal_record(status="archived", needs_review=False)
    Draft202012Validator(schema, format_checker=FormatChecker()).validate(record)


def test_verified_archived_tool_is_separated_from_active_catalogue() -> None:
    kaniko = next(tool for tool in load_tools() if tool["id"] == "kaniko")
    assert kaniko["status"] == "archived"
    assert kaniko["categories"][0] == "deprecated-historical"
    assert kaniko["lifecycle_stages"] == ["retire"]


def test_archived_repository_can_remain_for_active_tool() -> None:
    localstack = next(tool for tool in load_tools() if tool["id"] == "localstack")
    assert localstack["repository_archived"] is True
    assert localstack["status"] == "active"


def test_moved_repository_uses_active_official_location() -> None:
    dependency_check = next(
        tool for tool in load_tools() if tool["id"] == "dependencycheck"
    )
    assert dependency_check["repository_url"] == (
        "https://github.com/dependency-check/DependencyCheck"
    )
