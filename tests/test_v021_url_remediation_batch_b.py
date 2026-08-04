from __future__ import annotations

import csv
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "maintenance" / "v0.2.1-url-remediation-batch-b-review.md"
PLAN_CSV = ROOT / "docs" / "maintenance" / "v0.2.1-url-remediation-plan.csv"

EXPECTED_IDS = {
    "cdktf",
    "grafana-oncall",
    "juju",
    "kaniko",
    "keptn",
    "kubeapps",
    "kubernetes-dashboard",
    "localstack",
    "minio",
    "tnu",
}

# keptn appears twice: official_url + repository_url
EXPECTED_WORK_ITEMS = {
    ("cdktf", "repository_url"),
    ("grafana-oncall", "repository_url"),
    ("juju", "repository_url"),
    ("kaniko", "repository_url"),
    ("keptn", "official_url"),
    ("keptn", "repository_url"),
    ("kubeapps", "repository_url"),
    ("kubernetes-dashboard", "repository_url"),
    ("localstack", "repository_url"),
    ("minio", "repository_url"),
    ("tnu", "repository_url"),
}

EXPECTED_CHANGED_IDS = {"grafana-oncall", "kubernetes-dashboard"}
EXPECTED_UNCHANGED_IDS = EXPECTED_IDS - EXPECTED_CHANGED_IDS

RECOGNIZED_DECISIONS = {
    "retain historical provenance; clear needs_review",
    "retain historical URL; clear needs_review",
    "replace with official cold-storage location; clear needs_review",
    "replace with official retirement location; clear needs_review",
    "retain; needs_review remains true",
    "no change required; boundary already correctly documented",
}


def _ledger_rows(ledger_path: Path = LEDGER) -> list[dict[str, str]]:
    assert ledger_path.exists(), f"Missing batch B review ledger: {ledger_path}"
    lines = [
        line.rstrip() for line in ledger_path.read_text(encoding="utf-8").splitlines()
    ]
    table_lines = [line for line in lines if line.startswith("|")]
    assert table_lines, (
        f"Batch B review ledger contains no Markdown table: {ledger_path}"
    )
    header = [part.strip() for part in table_lines[0].strip("|").split("|")]
    required_columns = {
        "tool_id",
        "affected_field",
        "previous_value",
        "final_value",
        "final_decision",
        "canonical_changed",
    }
    missing_columns = required_columns - set(header)
    assert not missing_columns, (
        "Batch B review ledger is missing required columns "
        f"{sorted(missing_columns)}: {ledger_path}"
    )

    rows: list[dict[str, str]] = []
    for row_number, line in enumerate(table_lines[2:], start=3):
        stripped = line.strip()
        if stripped and set(stripped) <= {"|", "-", ":", " "}:
            continue
        values = [part.strip() for part in line.strip("|").split("|")]
        assert len(values) == len(header), (
            f"Batch B review ledger has malformed row at line {row_number}: "
            f"expected {len(header)} columns, got {len(values)}: {ledger_path}"
        )
        rows.append(dict(zip(header, values, strict=True)))
    return rows


def _planning_rows() -> list[dict[str, str]]:
    rows = []
    with PLAN_CSV.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            if row.get("proposed_batch", "").strip() == "batch-b-archived-boundary":
                rows.append(row)
    return rows


def _load_tool(yaml_file: str, tool_id: str) -> dict:
    path = ROOT / yaml_file
    assert path.exists(), f"Canonical YAML file not found: {path}"
    tools = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(tools, list), f"Expected list in {path}"
    by_id = {t["id"]: t for t in tools if isinstance(t, dict) and "id" in t}
    assert tool_id in by_id, f"Tool {tool_id!r} not found in {path}"
    return by_id[tool_id]


# ---------------------------------------------------------------------------
# Scope tests
# ---------------------------------------------------------------------------


def test_batch_b_review_ledger_exists() -> None:
    assert LEDGER.exists(), f"Missing batch B review ledger: {LEDGER}"


def test_batch_b_review_ledger_row_count() -> None:
    rows = _ledger_rows()
    assert len(rows) == 11, f"Expected 11 ledger rows, got {len(rows)}"


def test_batch_b_review_ledger_unique_ids() -> None:
    rows = _ledger_rows()
    ids = {row["tool_id"] for row in rows}
    assert ids == EXPECTED_IDS, (
        f"ID mismatch. Missing: {EXPECTED_IDS - ids}. Extra: {ids - EXPECTED_IDS}"
    )


def test_batch_b_review_ledger_work_items() -> None:
    rows = _ledger_rows()
    work_items = {(row["tool_id"], row["affected_field"]) for row in rows}
    assert work_items == EXPECTED_WORK_ITEMS, (
        f"Work-item mismatch. Missing: {EXPECTED_WORK_ITEMS - work_items}. "
        f"Extra: {work_items - EXPECTED_WORK_ITEMS}"
    )


def test_batch_b_keptn_duplicate_rows_present() -> None:
    rows = _ledger_rows()
    keptn_rows = [row for row in rows if row["tool_id"] == "keptn"]
    assert len(keptn_rows) == 2, (
        f"Expected 2 keptn rows (official_url + repository_url), got {len(keptn_rows)}"
    )
    fields = {row["affected_field"] for row in keptn_rows}
    assert fields == {"official_url", "repository_url"}, (
        f"keptn work items must be official_url and repository_url; got {fields}"
    )


def test_batch_b_recognized_decisions() -> None:
    rows = _ledger_rows()
    for row in rows:
        assert row["final_decision"] in RECOGNIZED_DECISIONS, (
            f"Unrecognized decision for ({row['tool_id']}, {row['affected_field']}): "
            f"{row['final_decision']!r}"
        )


# ---------------------------------------------------------------------------
# Planning-row cross-check
# ---------------------------------------------------------------------------


def test_batch_b_planning_rows() -> None:
    planning = _planning_rows()
    assert len(planning) == 11, f"Expected 11 planning rows, got {len(planning)}"
    plan_items = {(r["tool_id"], r["affected_field"]) for r in planning}
    assert plan_items == EXPECTED_WORK_ITEMS, (
        f"Planning work-item mismatch: {plan_items ^ EXPECTED_WORK_ITEMS}"
    )


def test_batch_b_previous_values_match_planning_csv() -> None:
    planning = _planning_rows()
    plan_map = {
        (r["tool_id"], r["affected_field"]): r["current_canonical_value"]
        for r in planning
    }
    rows = _ledger_rows()
    for row in rows:
        key = (row["tool_id"], row["affected_field"])
        expected_prev = plan_map[key]
        assert row["previous_value"] == expected_prev, (
            f"previous_value mismatch for {key}: "
            f"ledger={row['previous_value']!r}, plan={expected_prev!r}"
        )


# ---------------------------------------------------------------------------
# Canonical YAML cross-check
# ---------------------------------------------------------------------------


def test_batch_b_final_values_match_canonical_yaml() -> None:
    planning = _planning_rows()
    yaml_map = {
        (r["tool_id"], r["affected_field"]): r["canonical_yaml_file"] for r in planning
    }
    rows = _ledger_rows()
    for row in rows:
        key = (row["tool_id"], row["affected_field"])
        yaml_file = yaml_map[key]
        tool = _load_tool(yaml_file, row["tool_id"])
        actual_value = tool.get(row["affected_field"])
        assert str(actual_value) == row["final_value"], (
            f"final_value mismatch for {key}: "
            f"ledger={row['final_value']!r}, yaml={actual_value!r}"
        )


def test_batch_b_changed_ids_canonical_changed_yes() -> None:
    rows = _ledger_rows()
    by_id_field = {(row["tool_id"], row["affected_field"]): row for row in rows}
    for changed_id in EXPECTED_CHANGED_IDS:
        for _, field in EXPECTED_WORK_ITEMS:
            key = (changed_id, field)
            if key in by_id_field:
                assert by_id_field[key]["canonical_changed"] == "yes", (
                    f"Expected canonical_changed=yes for {key}"
                )


def test_batch_b_unchanged_ids_canonical_changed_no() -> None:
    rows = _ledger_rows()
    by_id_field = {(row["tool_id"], row["affected_field"]): row for row in rows}
    for unchanged_id in EXPECTED_UNCHANGED_IDS:
        for key, row in by_id_field.items():
            if key[0] == unchanged_id:
                assert row["canonical_changed"] == "no", (
                    f"Expected canonical_changed=no for {key}, got {row['canonical_changed']!r}"
                )


def test_batch_b_unchanged_ids_preserve_previous_values() -> None:
    rows = _ledger_rows()
    by_id_field = {(row["tool_id"], row["affected_field"]): row for row in rows}
    for key, row in by_id_field.items():
        if row["canonical_changed"] == "no":
            assert row["final_value"] == row["previous_value"], (
                f"canonical_changed=no but values differ for {key}: "
                f"previous={row['previous_value']!r}, final={row['final_value']!r}"
            )


# ---------------------------------------------------------------------------
# Pinned expected values
# ---------------------------------------------------------------------------


def test_batch_b_pinned_final_decisions() -> None:
    rows = _ledger_rows()
    by_id_field = {(row["tool_id"], row["affected_field"]): row for row in rows}

    # Changed records
    grafana = by_id_field[("grafana-oncall", "repository_url")]
    assert grafana["final_value"] == "https://github.com/grafana-cold-storage/oncall"
    assert grafana["canonical_changed"] == "yes"
    assert (
        grafana["final_decision"]
        == "replace with official cold-storage location; clear needs_review"
    )

    k8s_dashboard = by_id_field[("kubernetes-dashboard", "repository_url")]
    assert (
        k8s_dashboard["final_value"]
        == "https://github.com/kubernetes-retired/dashboard"
    )
    assert k8s_dashboard["canonical_changed"] == "yes"
    assert (
        k8s_dashboard["final_decision"]
        == "replace with official retirement location; clear needs_review"
    )

    # Historical provenance retained
    cdktf = by_id_field[("cdktf", "repository_url")]
    assert cdktf["final_value"] == "https://github.com/hashicorp/terraform-cdk"
    assert cdktf["canonical_changed"] == "no"
    assert cdktf["final_decision"] == "retain historical provenance; clear needs_review"

    kaniko = by_id_field[("kaniko", "repository_url")]
    assert kaniko["final_value"] == "https://github.com/GoogleContainerTools/kaniko"
    assert kaniko["canonical_changed"] == "no"

    keptn_url = by_id_field[("keptn", "official_url")]
    assert keptn_url["final_value"] == "https://keptn.sh"
    assert keptn_url["canonical_changed"] == "no"
    assert keptn_url["final_decision"] == "retain historical URL; clear needs_review"

    keptn_repo = by_id_field[("keptn", "repository_url")]
    assert keptn_repo["final_value"] == "https://github.com/keptn/keptn"
    assert keptn_repo["canonical_changed"] == "no"

    kubeapps = by_id_field[("kubeapps", "repository_url")]
    assert kubeapps["final_value"] == "https://github.com/vmware-tanzu/kubeapps"
    assert kubeapps["canonical_changed"] == "no"

    tnu = by_id_field[("tnu", "repository_url")]
    assert tnu["final_value"] == "https://github.com/jfroy/tnu"
    assert tnu["canonical_changed"] == "no"

    # Active products with retained boundaries
    juju = by_id_field[("juju", "repository_url")]
    assert juju["final_value"] == "https://github.com/canonical/juju"
    assert juju["canonical_changed"] == "no"
    assert juju["final_decision"] == "retain; needs_review remains true"

    localstack = by_id_field[("localstack", "repository_url")]
    assert localstack["final_value"] == "https://github.com/localstack/localstack"
    assert localstack["canonical_changed"] == "no"
    assert (
        localstack["final_decision"]
        == "no change required; boundary already correctly documented"
    )

    minio = by_id_field[("minio", "repository_url")]
    assert minio["final_value"] == "https://github.com/minio/minio"
    assert minio["canonical_changed"] == "no"
    assert minio["final_decision"] == "retain; needs_review remains true"


# ---------------------------------------------------------------------------
# Lifecycle invariant tests
# ---------------------------------------------------------------------------


def test_batch_b_grafana_oncall_yaml_coherent() -> None:
    tool = _load_tool("data/tools/deprecated-historical.yaml", "grafana-oncall")
    assert tool["repository_url"] == "https://github.com/grafana-cold-storage/oncall"
    assert tool["status"] == "archived"
    assert tool.get("repository_archived") is True
    assert tool.get("needs_review") is False


def test_batch_b_kubernetes_dashboard_yaml_coherent() -> None:
    tool = _load_tool("data/tools/deprecated-historical.yaml", "kubernetes-dashboard")
    assert tool["repository_url"] == "https://github.com/kubernetes-retired/dashboard"
    assert tool["status"] == "archived"
    assert tool.get("repository_archived") is True
    assert tool.get("needs_review") is False


def test_batch_b_active_products_not_archived_by_repository_flag() -> None:
    # localstack is active despite repository_archived; ensure status remains active
    localstack = _load_tool(
        "data/tools/virtualization-bare-metal-homelab.yaml", "localstack"
    )
    assert localstack["status"] == "active", (
        "localstack status must remain active; product is live at localstack.cloud"
    )


def test_batch_b_historical_records_needs_review_cleared() -> None:
    confirmed_closed = [
        "cdktf",
        "kaniko",
        "keptn",
        "kubeapps",
        "tnu",
        "grafana-oncall",
        "kubernetes-dashboard",
    ]
    for tid in confirmed_closed:
        tool = _load_tool("data/tools/deprecated-historical.yaml", tid)
        assert tool.get("needs_review") is False, (
            f"{tid}.needs_review must be false after Batch B review"
        )


def test_batch_b_inconclusive_records_needs_review_preserved() -> None:
    juju = _load_tool("data/tools/configuration-management.yaml", "juju")
    assert juju.get("needs_review") is True, (
        "juju.needs_review must remain true: repository boundary unresolved"
    )

    minio = _load_tool("data/tools/databases-caching-data-infrastructure.yaml", "minio")
    assert minio.get("needs_review") is True, (
        "minio.needs_review must remain true: repository boundary unresolved"
    )


# ---------------------------------------------------------------------------
# Non-selected canonical record invariant
# ---------------------------------------------------------------------------


def test_batch_b_no_non_selected_canonical_record_changed() -> None:
    import subprocess

    selected_yaml_files = {
        "data/tools/deprecated-historical.yaml",
        "data/tools/configuration-management.yaml",
        "data/tools/virtualization-bare-metal-homelab.yaml",
        "data/tools/databases-caching-data-infrastructure.yaml",
    }
    result = subprocess.run(
        ["git", "diff", "--name-only", "main...HEAD", "--", "data/tools/"],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )
    changed_yaml = set(result.stdout.strip().splitlines())
    non_selected_changed = changed_yaml - selected_yaml_files
    assert not non_selected_changed, (
        f"Non-selected canonical YAML files changed: {sorted(non_selected_changed)}"
    )
