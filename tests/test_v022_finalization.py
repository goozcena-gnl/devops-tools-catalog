from __future__ import annotations

import os
import subprocess
import sys
import tomllib
from functools import lru_cache
from pathlib import Path
from typing import Any

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/maintenance/v0.2.2-carryover-execution-manifest.yaml"
COMPLETION = ROOT / "docs/maintenance/v0.2.2-remediation-completion.md"
RELEASE_NOTES = ROOT / "docs/releases/v0.2.2-notes.md"
CHANGELOG = ROOT / "CHANGELOG.md"
PYPROJECT = ROOT / "pyproject.toml"

SOURCE_SHA = "dc7cfd457a7c9638b1132048792092c8b5e3ae02"
IMPLEMENTATION_SHA = "8c07b17be553147a219c5227cb20e9d66210552b"

LEDGERS = {
    "N1a": ROOT / "docs/maintenance/v0.2.2-n1a-access-retry-review.md",
    "N1b": ROOT / "docs/maintenance/v0.2.2-n1b-access-retry-review.md",
    "N2a": ROOT / "docs/maintenance/v0.2.2-n2a-hard-url-review.md",
    "N2b": ROOT / "docs/maintenance/v0.2.2-n2b-hard-url-review.md",
    "N3a": ROOT / "docs/maintenance/v0.2.2-n3a-archived-governance-review.md",
}

EXPECTED_CHANGES = {
    ("agones", "official_url"),
    ("ansible-lint", "documentation_url"),
    ("ansible-lint", "official_url"),
    ("azure-devops", "official_url"),
    ("bottlerocket", "documentation_url"),
    ("cedar-policy", "official_url"),
    ("coroot", "documentation_url"),
    ("etckeeper", "repository_url"),
    ("exoway", "documentation_url"),
    ("juju", "repository_url"),
    ("k8s-cleaner-sveltos", "official_url"),
    ("kata-containers", "documentation_url"),
    ("kdash", "official_url"),
    ("kubernetes-dashboard", "repository_url"),
    ("mantis", "official_url"),
}

EXPECTED_CANONICAL_FILES = {
    "data/tools/application-cloud-security.yaml",
    "data/tools/ci-build-testing.yaml",
    "data/tools/cloud-platforms-management.yaml",
    "data/tools/configuration-management.yaml",
    "data/tools/deprecated-historical.yaml",
    "data/tools/kubernetes-distributions-operations.yaml",
    "data/tools/kubernetes-networking-storage-addons.yaml",
    "data/tools/monitoring-metrics-logs-tracing.yaml",
    "data/tools/virtualization-bare-metal-homelab.yaml",
}

EXPECTED_GENERATED_DOCS = {
    "docs/categories/application-cloud-security.md",
    "docs/categories/ci-build-testing.md",
    "docs/categories/cloud-platforms-management.md",
    "docs/categories/configuration-management.md",
    "docs/categories/deprecated-historical.md",
    "docs/categories/kubernetes-distributions-operations.md",
    "docs/categories/kubernetes-networking-storage-addons.md",
    "docs/categories/monitoring-metrics-logs-tracing.md",
    "docs/categories/virtualization-bare-metal-homelab.md",
    "docs/lifecycle/build.md",
    "docs/lifecycle/deploy.md",
    "docs/lifecycle/operate.md",
    "docs/lifecycle/retire.md",
    "docs/lifecycle/secure.md",
    "docs/lifecycle/test.md",
    "docs/roles/cloud-security-engineer.md",
    "docs/roles/developer-experience-engineer.md",
    "docs/roles/devops-engineer.md",
    "docs/roles/devsecops-engineer.md",
    "docs/roles/kubernetes-engineer.md",
    "docs/roles/platform-engineer.md",
    "docs/roles/release-engineer.md",
    "docs/roles/site-reliability-engineer.md",
}

HOLD_IDS = {
    "autopwn-suite",
    "cai-robotsec",
    "ctop",
    "elastic-apm-server",
    "elastic-stack-elk",
}


def _git(*args: str) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            encoding="utf-8",
            check=True,
        )
    except FileNotFoundError as exc:
        raise AssertionError("Git is required for v0.2.2 immutable accounting") from exc
    return result.stdout


def _require_commits() -> None:
    for label, sha in (("source", SOURCE_SHA), ("implementation", IMPLEMENTATION_SHA)):
        try:
            _git("cat-file", "-e", f"{sha}^{{commit}}")
        except subprocess.CalledProcessError as exc:
            message = (
                f"v0.2.2 {label} commit {sha} is not reachable; immutable accounting "
                f"requires the explicit range {SOURCE_SHA} -> {IMPLEMENTATION_SHA}."
            )
            if os.getenv("GITHUB_ACTIONS") == "true":
                raise AssertionError(
                    f"{message} Ensure checkout uses fetch-depth: 0."
                ) from exc
            pytest.skip(f"{message} Local checkout may be shallow or partial.")


@lru_cache(maxsize=2)
def _catalog_at(commit: str) -> dict[str, dict[str, Any]]:
    _require_commits()
    paths = _git("ls-tree", "-r", "--name-only", commit, "--", "data/tools")
    records: dict[str, dict[str, Any]] = {}
    for path in (line for line in paths.splitlines() if line.endswith(".yaml")):
        payload = yaml.safe_load(_git("show", f"{commit}:{path}"))
        for record in payload:
            tool_id = record["id"]
            assert tool_id not in records, (
                f"Duplicate catalogue ID at {commit}: {tool_id}"
            )
            records[tool_id] = record
    return records


def _changed_files(*paths: str) -> set[str]:
    _require_commits()
    output = _git(
        "diff",
        "--name-only",
        SOURCE_SHA,
        IMPLEMENTATION_SHA,
        "--",
        *paths,
    )
    return {line for line in output.splitlines() if line}


def _manifest_rows() -> list[dict[str, Any]]:
    payload = yaml.safe_load(MANIFEST.read_text(encoding="utf-8"))
    return payload["work_items"]


def _cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _ledger_rows(path: Path) -> list[dict[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    header_index = next(
        (
            index
            for index, line in enumerate(lines)
            if line.startswith("|")
            and {"tool_id", "affected_field", "canonical_changed"} <= set(_cells(line))
        ),
        None,
    )
    assert header_index is not None, f"Missing execution ledger table in {path}"
    headers = _cells(lines[header_index])
    required = {
        "tool_id",
        "affected_field",
        "canonical_changed",
        "unresolved_boundary",
    }
    assert required <= set(headers)

    rows: list[dict[str, str]] = []
    for line in lines[header_index + 2 :]:
        if not line.startswith("|"):
            if rows:
                break
            continue
        values = _cells(line)
        assert len(values) == len(headers), f"Malformed ledger row in {path}: {line}"
        rows.append(dict(zip(headers, values, strict=True)))
    return rows


def test_release_metadata_and_boundary_statements() -> None:
    project = tomllib.loads(PYPROJECT.read_text(encoding="utf-8"))
    assert project["project"]["version"] == "0.2.2"

    changelog = CHANGELOG.read_text(encoding="utf-8")
    notes = RELEASE_NOTES.read_text(encoding="utf-8")
    completion = COMPLETION.read_text(encoding="utf-8")
    assert "## [0.2.2] - 2026-08-12" in changelog
    assert notes.startswith("# DevOps Tools Catalogue v0.2.2")

    for text in (changelog, notes, completion):
        lowered = text.lower()
        assert "issue #2 remains open" in lowered
        assert "n4 remains unresolved" in lowered
        assert "complete catalogue" in lowered
        assert "does not claim" in lowered

    assert "no v0.2.2 tag exists" in completion.lower()
    assert "no v0.2.2 github release exists" in completion.lower()
    assert "- [ ]" not in notes
    assert "```bash" not in notes


def test_manifest_and_execution_ledgers_close_exactly() -> None:
    rows = _manifest_rows()
    executed = [row for row in rows if row["logical_workstream"] != "N4"]
    held = [row for row in rows if row["logical_workstream"] == "N4"]

    assert len(rows) == 82
    assert len({row["tool_id"] for row in rows}) == 63
    assert len(executed) == 64
    assert len({row["tool_id"] for row in executed}) == 58
    assert len(held) == 18
    assert {row["tool_id"] for row in held} == HOLD_IDS
    assert {row["hold_reason"] for row in held} == {
        "authoritative lifecycle/license boundary evidence not yet established "
        "in v0.2.1 ledgers"
    }

    expected_keys = {(row["tool_id"], row["affected_field"]) for row in executed}
    ledger_rows = [row for path in LEDGERS.values() for row in _ledger_rows(path)]
    ledger_keys = [(row["tool_id"], row["affected_field"]) for row in ledger_rows]
    assert len(ledger_rows) == 64
    assert len(set(ledger_keys)) == 64
    assert set(ledger_keys) == expected_keys

    changed_ledger_keys = {
        (row["tool_id"], row["affected_field"])
        for row in ledger_rows
        if row["canonical_changed"].lower() == "yes"
    }
    assert changed_ledger_keys == EXPECTED_CHANGES

    uncleared = [
        row
        for row in ledger_rows
        if not row["unresolved_boundary"]
        .strip()
        .lower()
        .startswith(("none", "no unresolved", "no remaining"))
    ]
    assert len(uncleared) == 36
    assert len({row["tool_id"] for row in uncleared}) == 35


def test_immutable_catalogue_accounting_and_selected_changes() -> None:
    source = _catalog_at(SOURCE_SHA)
    result = _catalog_at(IMPLEMENTATION_SHA)
    assert source.keys() == result.keys()

    differences = {
        (tool_id, field)
        for tool_id in source
        for field in source[tool_id].keys() | result[tool_id].keys()
        if source[tool_id].get(field) != result[tool_id].get(field)
    }
    assert differences == EXPECTED_CHANGES
    assert len({tool_id for tool_id, _field in differences}) == 14

    executed = [row for row in _manifest_rows() if row["logical_workstream"] != "N4"]
    executed_keys = {(row["tool_id"], row["affected_field"]) for row in executed}
    unchanged_keys = executed_keys - differences
    assert len(unchanged_keys) == 49
    assert len({tool_id for tool_id, _field in unchanged_keys}) == 44
    assert differences <= executed_keys


def test_immutable_file_changes_are_exact() -> None:
    assert _changed_files("data/tools") == EXPECTED_CANONICAL_FILES
    assert (
        _changed_files(
            "README.md",
            "docs/categories",
            "docs/lifecycle",
            "docs/roles",
        )
        == EXPECTED_GENERATED_DOCS
    )


def test_completion_report_contains_exact_accounting_and_changes() -> None:
    text = COMPLETION.read_text(encoding="utf-8")
    required = {
        "TOTAL_PLANNED_ROWS: 82",
        "TOTAL_PLANNED_UNIQUE_IDS: 63",
        "TOTAL_REVIEWED_ROWS: 64",
        "TOTAL_REVIEWED_UNIQUE_IDS: 58",
        "TOTAL_HOLD_ROWS: 18",
        "TOTAL_HOLD_UNIQUE_IDS: 5",
        "TOTAL_CHANGED_CANONICAL_FIELDS: 15",
        "TOTAL_CHANGED_CANONICAL_IDS: 14",
        "TOTAL_REVIEWED_BUT_UNCHANGED_ROWS: 49",
        "TOTAL_REVIEWED_BUT_UNCHANGED_IDS: 44",
        "LOST_IDS: 0",
        "NEW_IDS: 0",
        "NON_SELECTED_CHANGED_IDS: 0",
        "MACHINE_API_REPLACEMENT_CANDIDATES: 0",
        "GENERATED_DOC_CHANGED_FILES: 23",
    }
    for statement in required:
        assert statement in text
    for tool_id, field in EXPECTED_CHANGES:
        assert f"`{tool_id}.{field}`" in text


def test_git_helpers_use_explicit_two_commit_range(monkeypatch: object) -> None:
    captured: list[tuple[str, ...]] = []

    def fake_git(*args: str) -> str:
        captured.append(args)
        return ""

    module = sys.modules[__name__]
    monkeypatch.setattr(module, "_require_commits", lambda: None)
    monkeypatch.setattr(module, "_git", fake_git)
    _changed_files("data/tools")

    assert captured == [
        (
            "diff",
            "--name-only",
            SOURCE_SHA,
            IMPLEMENTATION_SHA,
            "--",
            "data/tools",
        )
    ]
    assert "HEAD" not in captured[0]
    assert not any("..." in argument for argument in captured[0])


def test_missing_immutable_commit_fails_actionably_in_ci(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setenv("GITHUB_ACTIONS", "true")

    def missing_git(*args: str) -> str:
        raise subprocess.CalledProcessError(128, ["git", *args])

    monkeypatch.setattr(sys.modules[__name__], "_git", missing_git)
    with pytest.raises(AssertionError, match="fetch-depth: 0") as exc_info:
        _require_commits()
    assert SOURCE_SHA in str(exc_info.value)
    assert IMPLEMENTATION_SHA in str(exc_info.value)
