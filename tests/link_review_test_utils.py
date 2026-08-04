from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

STRICT_CLASSES = {
    "manual-verification-required",
    "http-error",
    "tls-failure",
    "repository-archived",
}

_REQUIRED_LEDGER_COLUMNS = {
    "tool_id",
    "checked_url",
    "result_category",
    "candidate_replacement_url",
}


@dataclass(frozen=True)
class StrictLedgerRow:
    tool_id: str
    checked_url: str
    result_category: str
    candidate_replacement_url: str


def _parse_markdown_table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_strict_ledger_rows(ledger_path: Path) -> list[StrictLedgerRow]:
    lines = ledger_path.read_text(encoding="utf-8").splitlines()

    header_line_idx = None
    header_cells: list[str] | None = None
    for idx, line in enumerate(lines):
        if not line.startswith("|"):
            continue
        cells = _parse_markdown_table_cells(line)
        if "tool_id" in cells and "result_category" in cells:
            header_line_idx = idx
            header_cells = cells
            break

    if header_line_idx is None or header_cells is None:
        raise AssertionError(
            f"{ledger_path}: could not find strict-ledger table header"
        )

    missing = sorted(_REQUIRED_LEDGER_COLUMNS - set(header_cells))
    if missing:
        raise AssertionError(
            f"{ledger_path}:{header_line_idx + 1}: missing required header columns: {missing}"
        )

    expected_count = len(header_cells)
    header_index = {name: i for i, name in enumerate(header_cells)}
    rows: list[StrictLedgerRow] = []

    for line_idx, line in enumerate(
        lines[header_line_idx + 2 :], start=header_line_idx + 3
    ):
        if not line.startswith("|"):
            if rows:
                break
            continue

        cells = _parse_markdown_table_cells(line)
        if len(cells) != expected_count:
            raise AssertionError(
                f"{ledger_path}:{line_idx}: malformed ledger row; "
                f"expected {expected_count} columns, got {len(cells)}"
            )

        rows.append(
            StrictLedgerRow(
                tool_id=cells[header_index["tool_id"]],
                checked_url=cells[header_index["checked_url"]],
                result_category=cells[header_index["result_category"]],
                candidate_replacement_url=cells[
                    header_index["candidate_replacement_url"]
                ],
            )
        )

    return rows


def is_machine_api_endpoint(url: str) -> bool:
    def _path_is_or_starts_with(path_value: str, prefix: str) -> bool:
        return path_value == prefix or path_value.startswith(f"{prefix}/")

    parsed = urlparse(url)
    host = (parsed.hostname or "").casefold()
    path = parsed.path.casefold().rstrip("/")

    if host == "api.github.com":
        return True

    if host == "api.githubcopilot.com" and _path_is_or_starts_with(path, "/graphql"):
        return True

    if _path_is_or_starts_with(path, "/api/v3"):
        return True

    return _path_is_or_starts_with(path, "/api/graphql")
