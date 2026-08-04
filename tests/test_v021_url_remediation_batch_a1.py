from __future__ import annotations

from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs" / "maintenance" / "v0.2.1-url-remediation-batch-a1-review.md"

EXPECTED_IDS = {
    "agones",
    "azure-devops",
    "bottlerocket",
    "burp-suite",
    "cedar-policy",
    "certmate",
    "coroot",
    "deeptutor",
    "devops-projects",
    "etckeeper",
    "exoway",
    "fortify-static-code-analyzer",
    "gremlin",
    "hoji-ai",
    "jumpserver",
    "k8s-cleaner-sveltos",
    "kata-containers",
    "kdash",
    "komodor",
    "kubeflame",
}

EXPECTED_CHANGED_IDS = {"deeptutor"}
EXPECTED_UNCHANGED_IDS = EXPECTED_IDS - EXPECTED_CHANGED_IDS


def _ledger_rows() -> list[dict[str, str]]:
    assert LEDGER.exists(), f"Missing batch A1 review ledger: {LEDGER}"
    lines = [line.rstrip() for line in LEDGER.read_text(encoding="utf-8").splitlines()]
    table_lines = [line for line in lines if line.startswith("|")]
    header = [part.strip() for part in table_lines[0].strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in table_lines[2:]:
        stripped = line.strip()
        if stripped and set(stripped) <= {"|", "-", ":", " "}:
            continue
        values = [part.strip() for part in line.strip("|").split("|")]
        if len(values) != len(header):
            continue
        rows.append(dict(zip(header, values, strict=True)))
    return rows


def test_batch_a1_review_ledger_scope_and_rows() -> None:
    rows = _ledger_rows()
    assert LEDGER.exists()
    assert len(rows) == 21

    ids = [row["tool_id"] for row in rows]
    counts = Counter(ids)
    assert len(set(ids)) == 20
    assert set(ids) == EXPECTED_IDS
    assert counts["hoji-ai"] == 2
    assert sorted(k for k, v in counts.items() if v > 1) == ["hoji-ai"]


def test_batch_a1_final_decisions_are_pinned() -> None:
    rows = _ledger_rows()
    by_id_field = {(row["tool_id"], row["affected_field"]): row for row in rows}

    deeptutor = by_id_field[("deeptutor", "official_url")]
    assert deeptutor["final_value"] == "https://deeptutor.info/"
    assert deeptutor["decision"] == "replace URL with primary-source proof"
    assert deeptutor["canonical_changed"] == "yes"

    cleaner = by_id_field[("k8s-cleaner-sveltos", "official_url")]
    assert cleaner["final_value"] == "https://sveltos.projectsveltos.io/k8sCleaner.html"
    assert cleaner["decision"] == "remain inconclusive"
    assert cleaner["canonical_changed"] == "no"

    hoji_official = by_id_field[("hoji-ai", "official_url")]
    hoji_repo = by_id_field[("hoji-ai", "repository_url")]
    assert hoji_official["final_value"] == "https://hoji.ai"
    assert hoji_repo["final_value"] == "https://github.com/hoji-ai/hoji"
    assert hoji_official["decision"] == "remain inconclusive"
    assert hoji_repo["decision"] == "remain inconclusive"


def test_batch_a1_reviewed_ids_are_exactly_the_selected_set() -> None:
    rows = _ledger_rows()
    reviewed_ids = {row["tool_id"] for row in rows}
    assert reviewed_ids == EXPECTED_IDS
    assert "mantis" not in reviewed_ids
    assert "microsoft-azure" not in reviewed_ids
    assert "oracle-cloud-infrastructure-oci" not in reviewed_ids
    assert "autopwn-suite" not in reviewed_ids


def test_batch_a1_unique_change_accounting() -> None:
    rows = _ledger_rows()
    changed_ids = {row["tool_id"] for row in rows if row["canonical_changed"] == "yes"}
    unchanged_ids = {row["tool_id"] for row in rows if row["canonical_changed"] == "no"}

    assert changed_ids == EXPECTED_CHANGED_IDS
    assert unchanged_ids == EXPECTED_UNCHANGED_IDS
    assert len(changed_ids) == 1
    assert len(unchanged_ids) == 19


def test_markdown_separator_rows_with_alignment_are_skipped(tmp_path: Path) -> None:
    ledger = tmp_path / "ledger.md"
    ledger.write_text(
        "\n".join(
            [
                "| tool_id | affected_field | canonical_changed |",
                "|---|---|---|",
                "|:---|---:|:---:|",
                "| deeptutor | official_url | yes |",
            ]
        ),
        encoding="utf-8",
    )

    lines = [line.rstrip() for line in ledger.read_text(encoding="utf-8").splitlines()]
    table_lines = [line for line in lines if line.startswith("|")]
    header = [part.strip() for part in table_lines[0].strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in table_lines[2:]:
        stripped = line.strip()
        if stripped and set(stripped) <= {"|", "-", ":", " "}:
            continue
        values = [part.strip() for part in line.strip("|").split("|")]
        if len(values) != len(header):
            continue
        rows.append(dict(zip(header, values, strict=True)))

    assert len(rows) == 1
    assert rows[0]["tool_id"] == "deeptutor"
    assert rows[0]["affected_field"] == "official_url"
    assert rows[0]["canonical_changed"] == "yes"
