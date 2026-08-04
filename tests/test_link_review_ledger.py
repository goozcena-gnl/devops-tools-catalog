from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = ROOT / "docs" / "link-review-ledger.md"
REPORT_PATH = ROOT / "reports" / "link-report.json"
STRICT_CLASSES = {
    "manual-verification-required",
    "http-error",
    "tls-failure",
    "repository-archived",
}


def _parse_ledger_rows() -> list[dict[str, str]]:
    lines = LEDGER_PATH.read_text(encoding="utf-8").splitlines()
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
        assert len(cells) == 11, f"Malformed ledger row with {len(cells)} columns"
        rows.append(
            {
                "tool_id": cells[0],
                "tool_name": cells[1],
                "checked_url": cells[2],
                "result_category": cells[3],
                "status_or_repo_state": cells[4],
                "existing_canonical_url": cells[5],
                "candidate_replacement_url": cells[6],
                "primary_source_evidence": cells[7],
                "recommended_action": cells[8],
                "confidence": cells[9],
                "human_decision_required": cells[10],
            }
        )
    return rows


def _is_machine_api_endpoint(url: str) -> bool:
    parsed = urlparse(url)
    host = parsed.netloc.casefold()
    path = parsed.path
    return (
        host == "api.github.com"
        or "/api/v3/" in path
        or (host == "api.githubcopilot.com" and "/graphql" in path)
        or (host.endswith("github.com") and path.rstrip("/").endswith("/graphql"))
    )


def test_link_review_ledger_candidates_and_strict_counts() -> None:
    rows = _parse_ledger_rows()
    strict_rows = [row for row in rows if row["result_category"] in STRICT_CLASSES]
    assert len(strict_rows) == 38

    strict_counts = Counter(row["result_category"] for row in strict_rows)
    assert strict_counts["manual-verification-required"] == 25
    assert strict_counts["http-error"] == 2
    assert strict_counts["tls-failure"] == 1
    assert strict_counts["repository-archived"] == 10

    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    report_by_checked = {item["url"]: item for item in report["results"]}

    non_dash_candidates = [
        row["candidate_replacement_url"]
        for row in strict_rows
        if row["candidate_replacement_url"] != "-"
    ]

    for row in strict_rows:
        candidate = row["candidate_replacement_url"]
        if candidate == "-":
            continue
        parsed = urlparse(candidate)
        assert parsed.scheme in {"http", "https"}
        assert parsed.netloc
        assert not _is_machine_api_endpoint(candidate)

        report_item = report_by_checked.get(row["checked_url"])
        assert report_item is not None
        final_url = report_item.get("final_url")
        if isinstance(final_url, str) and _is_machine_api_endpoint(final_url):
            assert candidate != final_url

    # This fix intentionally clears unsupported replacement candidates.
    assert len(non_dash_candidates) == 0
