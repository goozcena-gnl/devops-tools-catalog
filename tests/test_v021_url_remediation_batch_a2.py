from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "maintenance" / "v0.2.1-url-remediation-batch-a2-review.md"

EXPECTED_IDS = {
    "mantis",
    "microsoft-azure",
    "odysseus",
    "soos-dast",
    "terraform-cloud",
    "trivy",
    "yokecd",
    "yotascale",
}

EXPECTED_CHANGED_IDS = {"odysseus", "terraform-cloud", "trivy", "yokecd"}
EXPECTED_UNCHANGED_IDS = EXPECTED_IDS - EXPECTED_CHANGED_IDS


def _ledger_rows(ledger_path: Path = LEDGER) -> list[dict[str, str]]:
    assert ledger_path.exists(), f"Missing batch A2 review ledger: {ledger_path}"
    lines = [
        line.rstrip() for line in ledger_path.read_text(encoding="utf-8").splitlines()
    ]
    table_lines = [line for line in lines if line.startswith("|")]
    assert table_lines, (
        f"Batch A2 review ledger contains no Markdown table: {ledger_path}"
    )
    header = [part.strip() for part in table_lines[0].strip("|").split("|")]
    required_columns = {
        "tool_id",
        "affected_field",
        "final_value",
        "decision",
        "canonical_changed",
    }
    missing_columns = required_columns - set(header)
    assert not missing_columns, (
        "Batch A2 review ledger is missing required columns "
        f"{sorted(missing_columns)}: {ledger_path}"
    )

    rows: list[dict[str, str]] = []
    for row_number, line in enumerate(table_lines[2:], start=3):
        stripped = line.strip()
        if stripped and set(stripped) <= {"|", "-", ":", " "}:
            continue
        values = [part.strip() for part in line.strip("|").split("|")]
        assert len(values) == len(header), (
            f"Batch A2 review ledger has malformed row at line {row_number}: "
            f"expected {len(header)} columns, got {len(values)}: {ledger_path}"
        )
        rows.append(dict(zip(header, values, strict=True)))
    return rows


def test_batch_a2_review_ledger_scope_and_rows() -> None:
    rows = _ledger_rows()
    assert LEDGER.exists()
    assert len(rows) == 8

    ids = {row["tool_id"] for row in rows}
    assert ids == EXPECTED_IDS


def test_batch_a2_final_decisions_are_pinned() -> None:
    rows = _ledger_rows()
    by_id_field = {(row["tool_id"], row["affected_field"]): row for row in rows}

    terraform_cloud = by_id_field[("terraform-cloud", "official_url")]
    assert (
        terraform_cloud["final_value"]
        == "https://developer.hashicorp.com/terraform/cloud-docs"
    )
    assert terraform_cloud["decision"] == "replace URL with primary-source proof"
    assert terraform_cloud["canonical_changed"] == "yes"

    trivy = by_id_field[("trivy", "documentation_url")]
    assert trivy["final_value"] == "https://trivy.dev/docs/latest/"
    assert trivy["decision"] == "replace URL with primary-source proof"
    assert trivy["canonical_changed"] == "yes"

    odysseus = by_id_field[("odysseus", "official_url")]
    assert odysseus["final_value"] == "https://odysseus-dev.github.io/odysseus"
    assert odysseus["decision"] == "replace URL with primary-source proof"
    assert odysseus["canonical_changed"] == "yes"

    yokecd = by_id_field[("yokecd", "repository_url")]
    assert yokecd["final_value"] == "https://github.com/yokecd/yoke"
    assert yokecd["decision"] == "replace URL with primary-source proof"
    assert yokecd["canonical_changed"] == "yes"

    mantis = by_id_field[("mantis", "official_url")]
    assert (
        mantis["final_value"] == "https://mantis.getaugur.ai/docs/introduction/overview"
    )
    assert mantis["decision"] == "remain inconclusive"
    assert mantis["canonical_changed"] == "no"

    microsoft_azure = by_id_field[("microsoft-azure", "official_url")]
    assert microsoft_azure["final_value"] == "https://azure.microsoft.com"
    assert microsoft_azure["decision"] == "retain current value"
    assert microsoft_azure["canonical_changed"] == "no"

    soos_dast = by_id_field[("soos-dast", "official_url")]
    assert soos_dast["final_value"] == "https://hub.docker.com/r/soosio/dast"
    assert soos_dast["decision"] == "remain inconclusive"
    assert soos_dast["canonical_changed"] == "no"

    yotascale = by_id_field[("yotascale", "official_url")]
    assert yotascale["final_value"] == "https://www.yotascale.com"
    assert yotascale["decision"] == "remain inconclusive"
    assert yotascale["canonical_changed"] == "no"


def test_batch_a2_unique_change_accounting() -> None:
    rows = _ledger_rows()
    changed_ids = {row["tool_id"] for row in rows if row["canonical_changed"] == "yes"}
    unchanged_ids = {row["tool_id"] for row in rows if row["canonical_changed"] == "no"}

    assert changed_ids == EXPECTED_CHANGED_IDS
    assert unchanged_ids == EXPECTED_UNCHANGED_IDS
    assert len(changed_ids) == 4
    assert len(unchanged_ids) == 4


def test_committed_batch_a2_ledger_parses_successfully() -> None:
    rows = _ledger_rows()
    assert rows
    assert len(rows) == 8
