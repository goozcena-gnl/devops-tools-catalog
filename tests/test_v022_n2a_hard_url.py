from __future__ import annotations

import subprocess
from collections import Counter
from copy import deepcopy
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "maintenance" / "v0.2.2-carryover-execution-manifest.yaml"
LEDGER = ROOT / "docs" / "maintenance" / "v0.2.2-n2a-hard-url-review.md"

N2A_BASELINE_SHA = "be3d54483b778b1d57b4a4e712d331ea7918c4b7"
N2A_RESULT_SHA = "24e5230c90bd81f1207b9b3fc8b8158eef1712ca"
N2A_HISTORICAL_PRE_REBASE_CANDIDATE_SHA = "a87818631a06a038c3df1f7dfdc8cff68e1b066e"
N2A_RESULT_TREE_SHA = "21592d368eaa2c678b22dc43edac3b020cb3ea42"
N2A_CURRENT_MAIN_REF = "origin/main"

EXPECTED_SCOPE = {
    ("agones", "official_url"): (
        "data/tools/kubernetes-networking-storage-addons.yaml",
        "https://agones.dev/site",
        "https://agones.dev",
    ),
    ("azure-devops", "official_url"): (
        "data/tools/ci-build-testing.yaml",
        "https://azure.microsoft.com/en-us/services/devops",
        "https://azure.microsoft.com/en-us/products/devops/",
    ),
    ("bottlerocket", "documentation_url"): (
        "data/tools/virtualization-bare-metal-homelab.yaml",
        "https://bottlerocket.dev/en/docs/",
        "https://bottlerocket.dev/",
    ),
    ("burp-suite", "official_url"): (
        "data/tools/application-cloud-security.yaml",
        "https://portswigger.net/burp",
        "https://portswigger.net/burp",
    ),
    ("cedar-policy", "official_url"): (
        "data/tools/application-cloud-security.yaml",
        "https://cedarpolicy.com/en",
        "https://www.cedarpolicy.com",
    ),
    ("certmate", "repository_url"): (
        "data/tools/iam-secrets-certificates.yaml",
        "https://github.com/usual2970/certmate",
        "https://github.com/usual2970/certmate",
    ),
    ("coroot", "documentation_url"): (
        "data/tools/monitoring-metrics-logs-tracing.yaml",
        "https://coroot.com/docs/",
        "https://docs.coroot.com/",
    ),
    ("devops-projects", "repository_url"): (
        "data/tools/documentation-learning-career.yaml",
        "https://github.com/ophircloud/DevOps-Projects",
        "https://github.com/ophircloud/DevOps-Projects",
    ),
    ("etckeeper", "repository_url"): (
        "data/tools/configuration-management.yaml",
        "https://github.com/etckeeper/etckeeper",
        "https://git.joeyh.name/index.cgi/etckeeper.git",
    ),
    ("exoway", "documentation_url"): (
        "data/tools/cloud-platforms-management.yaml",
        "https://help.exoway.io/fr/",
        "https://doc.exoway.io/",
    ),
    ("fortify-static-code-analyzer", "official_url"): (
        "data/tools/application-cloud-security.yaml",
        "https://www.opentext.com/products/static-application-security-testing",
        "https://www.opentext.com/products/static-application-security-testing",
    ),
    ("gremlin", "repository_url"): (
        "data/tools/chaos-performance-engineering.yaml",
        "https://github.com/gremlin-io/gremlin",
        "https://github.com/gremlin-io/gremlin",
    ),
    ("hoji-ai", "official_url"): (
        "data/tools/mlops-llmops-ai-infrastructure.yaml",
        "https://hoji.ai",
        "https://hoji.ai",
    ),
    ("hoji-ai", "repository_url"): (
        "data/tools/mlops-llmops-ai-infrastructure.yaml",
        "https://github.com/hoji-ai/hoji",
        "https://github.com/hoji-ai/hoji",
    ),
    ("jumpserver", "official_url"): (
        "data/tools/iam-secrets-certificates.yaml",
        "https://www.jumpserver.com",
        "https://www.jumpserver.com",
    ),
    ("k8s-cleaner-sveltos", "official_url"): (
        "data/tools/kubernetes-distributions-operations.yaml",
        "https://sveltos.projectsveltos.io/k8sCleaner.html",
        "https://gianlucam76.github.io/k8s-cleaner/",
    ),
    ("kata-containers", "documentation_url"): (
        "data/tools/virtualization-bare-metal-homelab.yaml",
        "https://katacontainers.io/docs/",
        "https://github.com/kata-containers/kata-containers/tree/main/docs",
    ),
    ("kdash", "official_url"): (
        "data/tools/kubernetes-distributions-operations.yaml",
        "https://kdash.cli.rs",
        "https://kdash-rs.github.io",
    ),
    ("komodor", "repository_url"): (
        "data/tools/monitoring-metrics-logs-tracing.yaml",
        "https://github.com/komodorio/komodor",
        "https://github.com/komodorio/komodor",
    ),
    ("kubeflame", "official_url"): (
        "data/tools/kubernetes-distributions-operations.yaml",
        "https://kubeflame.github.io",
        "https://kubeflame.github.io",
    ),
    ("mantis", "official_url"): (
        "data/tools/ci-build-testing.yaml",
        "https://mantis.getaugur.ai/docs/introduction/overview",
        "https://getmantis.ai",
    ),
}

EXPECTED_IDS = {tool_id for tool_id, _field in EXPECTED_SCOPE}
EXPECTED_WORK_ITEMS = set(EXPECTED_SCOPE)
EXPECTED_CHANGED_FIELDS = {
    key: (before, after)
    for key, (_path, before, after) in EXPECTED_SCOPE.items()
    if before != after
}

EXPECTED_CANDIDATE_FILES = {
    "data/tools/application-cloud-security.yaml",
    "data/tools/ci-build-testing.yaml",
    "data/tools/cloud-platforms-management.yaml",
    "data/tools/configuration-management.yaml",
    "data/tools/kubernetes-distributions-operations.yaml",
    "data/tools/kubernetes-networking-storage-addons.yaml",
    "data/tools/monitoring-metrics-logs-tracing.yaml",
    "data/tools/virtualization-bare-metal-homelab.yaml",
    "docs/categories/application-cloud-security.md",
    "docs/categories/ci-build-testing.md",
    "docs/categories/cloud-platforms-management.md",
    "docs/categories/configuration-management.md",
    "docs/categories/kubernetes-distributions-operations.md",
    "docs/categories/kubernetes-networking-storage-addons.md",
    "docs/categories/monitoring-metrics-logs-tracing.md",
    "docs/categories/virtualization-bare-metal-homelab.md",
    "docs/lifecycle/build.md",
    "docs/lifecycle/deploy.md",
    "docs/lifecycle/operate.md",
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

PROTECTED_SELECTED_FIELDS = {
    "status",
    "needs_review",
    "license_model",
    "license_spdx",
}

AUTHORIZED_CURRENT_DRIFT = {
    ("azure-devops", "license_model"): "commercial",
    ("azure-devops", "needs_review"): False,
    ("azure-devops", "status"): "active",
    ("burp-suite", "license_model"): "commercial",
    ("burp-suite", "needs_review"): False,
    ("burp-suite", "status"): "active",
    ("coroot", "license_model"): "open-core",
    ("coroot", "license_spdx"): "Apache-2.0",
    ("fortify-static-code-analyzer", "license_model"): "commercial",
    ("fortify-static-code-analyzer", "needs_review"): False,
    ("fortify-static-code-analyzer", "status"): "active",
}

AUTHORIZED_CURRENT_URL_DRIFT = {
    ("certmate", "repository_url"): "https://github.com/fabriziosalmi/certmate",
    ("gremlin", "repository_url"): None,
    ("komodor", "repository_url"): None,
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
    return [row for row in payload["work_items"] if row["execution_sub_batch"] == "N2a"]


def _parse_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def _ledger_rows(path: Path = LEDGER) -> list[dict[str, str]]:
    assert path.exists(), f"Missing N2a review ledger: {path}"
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
    assert header_index is not None, f"No N2a evidence table header in {path}"
    headers = _parse_cells(lines[header_index])
    missing = REQUIRED_LEDGER_COLUMNS - set(headers)
    assert not missing, f"N2a ledger is missing columns: {sorted(missing)}"

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
        raise AssertionError("Git is required for N2a pinned-range invariants") from exc
    except subprocess.CalledProcessError as exc:
        detail = (exc.stderr or exc.stdout or str(exc)).strip()
        raise AssertionError(
            "N2a pinned-range invariant failed for explicit refs "
            f"{N2A_BASELINE_SHA} -> {N2A_RESULT_SHA}: {detail}"
        ) from exc
    return result.stdout


def _require_refs() -> None:
    for sha in (N2A_BASELINE_SHA, N2A_RESULT_SHA):
        _git("cat-file", "-e", f"{sha}^{{commit}}")


def _changed_files() -> set[str]:
    _require_refs()
    output = _git(
        "diff",
        "--name-only",
        N2A_BASELINE_SHA,
        N2A_RESULT_SHA,
        "--",
    )
    return {line for line in output.splitlines() if line}


def _yaml_paths_at(revision: str) -> list[str]:
    output = _git("ls-tree", "-r", "--name-only", revision, "--", "data/tools/")
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
            assert isinstance(record, dict) and isinstance(record.get("id"), str)
            tool_id = record["id"]
            assert tool_id not in records, f"Duplicate canonical ID {tool_id!r}"
            records[tool_id] = (relative, record)
    return records


def _field_changes() -> dict[tuple[str, str], tuple[Any, Any]]:
    baseline = _records_at(N2A_BASELINE_SHA)
    result = _records_at(N2A_RESULT_SHA)
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


def _assert_current_n2a_persistence(
    current: dict[str, tuple[str, dict[str, Any]]],
    accepted: dict[str, tuple[str, dict[str, Any]]],
) -> None:
    for key, (expected_path, _before, expected_value) in EXPECTED_SCOPE.items():
        tool_id, field = key
        assert tool_id in current, f"Current catalogue lost N2a ID {tool_id!r}"
        assert tool_id in accepted, f"N2a candidate is missing selected ID {tool_id!r}"
        current_path, current_record = current[tool_id]
        accepted_path, accepted_record = accepted[tool_id]
        assert current_path == expected_path == accepted_path
        assert accepted_record.get(field) == expected_value
        current_value = current_record.get(field)
        if current_value != expected_value:
            assert key in AUTHORIZED_CURRENT_URL_DRIFT, (
                f"N2a-owned field drifted without authorization for {key}"
            )
            assert current_value == AUTHORIZED_CURRENT_URL_DRIFT[key]
        for protected_field in PROTECTED_SELECTED_FIELDS:
            current_value = current_record.get(protected_field)
            accepted_value = accepted_record.get(protected_field)
            if current_value == accepted_value:
                continue
            authorized_value = AUTHORIZED_CURRENT_DRIFT.get((tool_id, protected_field))
            if authorized_value is not None:
                assert current_value == authorized_value
                continue
            raise AssertionError(
                f"N2a-protected field drifted for {(tool_id, protected_field)}"
            )


def test_n2a_frozen_selector_is_exact() -> None:
    rows = _manifest_rows()
    assert len(rows) == 21
    assert [row["sequence_number"] for row in rows] == list(range(36, 57))
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
    assert duplicates == {"hoji-ai"}


def test_n2a_manifest_scope_matches_expected_baseline_values() -> None:
    for row in _manifest_rows():
        key = (row["tool_id"], row["affected_field"])
        expected_path, previous_value, _final_value = EXPECTED_SCOPE[key]
        assert row["canonical_yaml_file"] == expected_path
        assert row["current_value"] == previous_value
        assert row["affected_field"] in {
            "official_url",
            "documentation_url",
            "repository_url",
        }


def test_n2a_ledger_exactly_covers_frozen_rows() -> None:
    rows = _ledger_rows()
    assert len(rows) == 21
    assert {(row["tool_id"], row["affected_field"]) for row in rows} == (
        EXPECTED_WORK_ITEMS
    )


def test_n2a_ledger_records_previous_and_final_values() -> None:
    result = _records_at(N2A_RESULT_SHA)
    for row in _ledger_rows():
        key = (row["tool_id"], row["affected_field"])
        expected_path, previous_value, final_value = EXPECTED_SCOPE[key]
        result_path, result_record = result[row["tool_id"]]
        assert row["canonical_yaml_file"] == expected_path == result_path
        assert row["previous_value"] == previous_value
        assert row["final_value"] == final_value
        assert result_record[row["affected_field"]] == final_value
        assert row["v021_previous_decision"] == "reviewed-but-unchanged in v0.2.1"
        assert (row["canonical_changed"] == "yes") == (key in EXPECTED_CHANGED_FIELDS)


def test_n2a_ledger_separates_observation_evidence_and_inference() -> None:
    for row in _ledger_rows():
        assert "2026-08-12" in row["fresh_network_observation"]
        assert row["authoritative_evidence"]
        assert row["inference"]
        assert row["final_decision"]
        assert row["unresolved_boundary"]
        assert "redirect alone" not in row["final_decision"].lower()


def test_n2a_explicit_historical_result_diff_is_exact() -> None:
    assert _changed_files() == EXPECTED_CANDIDATE_FILES
    assert _field_changes() == EXPECTED_CHANGED_FIELDS


def test_n2a_has_no_lost_or_new_canonical_ids() -> None:
    baseline = _records_at(N2A_BASELINE_SHA)
    result = _records_at(N2A_RESULT_SHA)
    assert baseline.keys() == result.keys()


def test_n2a_selected_protected_fields_are_unchanged() -> None:
    baseline = _records_at(N2A_BASELINE_SHA)
    result = _records_at(N2A_RESULT_SHA)
    for tool_id in EXPECTED_IDS:
        for field in PROTECTED_SELECTED_FIELDS:
            assert baseline[tool_id][1].get(field) == result[tool_id][1].get(field), (
                f"Forbidden N2a change for {(tool_id, field)}"
            )


def test_n2a_selected_values_remain_typed_strings() -> None:
    result = _records_at(N2A_RESULT_SHA)
    for tool_id, field in EXPECTED_SCOPE:
        assert isinstance(result[tool_id][1][field], str)


def test_n2a_current_state_preserves_owned_decisions() -> None:
    _assert_current_n2a_persistence(
        _current_records(),
        _records_at(N2A_RESULT_SHA),
    )


def test_n2a_unrelated_future_canonical_change_does_not_invalidate_history() -> None:
    accepted = _records_at(N2A_RESULT_SHA)
    future = deepcopy(accepted)
    unrelated_id = next(tool_id for tool_id in future if tool_id not in EXPECTED_IDS)
    future[unrelated_id][1]["summary"] = "A later authorized unrelated change."
    _assert_current_n2a_persistence(future, accepted)


def test_n2a_ledger_records_permanent_result_and_pre_rebase_provenance() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    assert f"Execution baseline SHA: `{N2A_BASELINE_SHA}`" in text
    assert f"Permanent N2a result SHA: `{N2A_RESULT_SHA}`" in text
    assert (
        "Historical pre-rebase candidate SHA: "
        f"`{N2A_HISTORICAL_PRE_REBASE_CANDIDATE_SHA}`" in text
    )
    assert f"Result tree SHA: `{N2A_RESULT_TREE_SHA}`" in text
    assert "provenance only" in text


def test_n2a_scope_audit_totals_are_recorded() -> None:
    text = LEDGER.read_text(encoding="utf-8")
    for expected in (
        "SELECTED_MANIFEST_ROWS: 21",
        "REVIEWED_MANIFEST_ROWS: 21",
        "UNREVIEWED_MANIFEST_ROWS: 0",
        "SELECTED_UNIQUE_IDS: 20",
        "DUPLICATE_SELECTED_IDS: 1",
        "TOTAL_CHANGED_CANONICAL_IDS: 11",
        "TOTAL_CHANGED_CANONICAL_FIELDS: 11",
        "REVIEWED_BUT_UNCHANGED_ROWS: 10",
        "REVIEWED_BUT_UNCHANGED_IDS: 9",
        "NON_SELECTED_CHANGED_IDS: 0",
        "LOST_IDS: 0",
        "NEW_IDS: 0",
        "MACHINE_API_REPLACEMENT_CANDIDATES: 0",
    ):
        assert expected in text


def test_n2a_missing_ref_is_always_an_actionable_failure(monkeypatch: Any) -> None:
    def fail(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        raise subprocess.CalledProcessError(128, args[0], stderr="missing object")

    monkeypatch.setattr(subprocess, "run", fail)
    try:
        _require_refs()
        raise AssertionError("Expected missing pinned refs to fail")
    except AssertionError as exc:
        message = str(exc)
        assert N2A_BASELINE_SHA in message
        assert N2A_RESULT_SHA in message
        assert "missing object" in message


def test_n2a_missing_result_ref_is_always_a_failure(monkeypatch: Any) -> None:
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
        assert N2A_BASELINE_SHA in message
        assert N2A_RESULT_SHA in message
        assert "missing result" in message


def test_n2a_git_unavailable_is_actionable(monkeypatch: Any) -> None:
    def fail(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        raise FileNotFoundError("git missing")

    monkeypatch.setattr(subprocess, "run", fail)
    try:
        _require_refs()
        raise AssertionError("Expected missing Git to fail")
    except AssertionError as exc:
        assert "Git is required" in str(exc)


def test_n2a_historical_diff_uses_two_explicit_commits(monkeypatch: Any) -> None:
    commands: list[list[str]] = []

    def record(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        command = list(args[0])
        commands.append(command)
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", record)
    _changed_files()
    diff = next(command for command in commands if command[:2] == ["git", "diff"])
    baseline_index = diff.index(N2A_BASELINE_SHA)
    assert diff[baseline_index + 1] == N2A_RESULT_SHA
    assert "HEAD" not in diff
    assert not any("..." in argument for argument in diff)


def test_n2a_permanent_result_has_expected_identity_and_history() -> None:
    _require_refs()
    assert _git("rev-parse", f"{N2A_RESULT_SHA}^{{tree}}").strip() == (
        N2A_RESULT_TREE_SHA
    )
    assert _git("rev-parse", f"{N2A_RESULT_SHA}^").strip() == N2A_BASELINE_SHA
    _git("merge-base", "--is-ancestor", N2A_RESULT_SHA, N2A_CURRENT_MAIN_REF)


def test_n2a_pre_rebase_sha_is_never_an_executable_ref(monkeypatch: Any) -> None:
    commands: list[list[str]] = []

    def record(*args: Any, **kwargs: Any) -> subprocess.CompletedProcess[str]:
        command = list(args[0])
        commands.append(command)
        return subprocess.CompletedProcess(command, 0, stdout="", stderr="")

    monkeypatch.setattr(subprocess, "run", record)
    _changed_files()
    command_text = "\n".join(" ".join(command) for command in commands)
    assert N2A_HISTORICAL_PRE_REBASE_CANDIDATE_SHA not in command_text
    assert N2A_RESULT_SHA in command_text


def test_n2a_ledger_parser_rejects_malformed_rows(tmp_path: Path) -> None:
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
