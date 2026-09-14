#!/usr/bin/env python3
"""Generate a deterministic inventory of catalogue review debt."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from collections.abc import Sequence
from datetime import date
from pathlib import Path

from scripts.catalog import ROOT, load_taxonomy, load_tools

AGE_BUCKETS = ("0-30", "31-90", "91-180", "181+")


def _parse_date(value: object) -> date:
    return date.fromisoformat(str(value))


def _age_bucket(age_days: int) -> str:
    if age_days <= 30:
        return "0-30"
    if age_days <= 90:
        return "31-90"
    if age_days <= 180:
        return "91-180"
    return "181+"


def _requires_review(tool: dict[str, object]) -> bool:
    return bool(tool.get("needs_review")) or tool.get("status") == "needs-review"


def _priority_signals(tool: dict[str, object], *, age_days: int) -> list[str]:
    signals: list[str] = []
    if tool.get("license_model") == "unknown":
        signals.append("unknown-license")
    if tool.get("maturity", "unknown") == "unknown":
        signals.append("unknown-maturity")
    if not tool.get("repository_url"):
        signals.append("missing-repository-url")
    if not tool.get("documentation_url"):
        signals.append("missing-documentation-url")
    if not tool.get("sources"):
        signals.append("missing-sources")
    if age_days > 180:
        signals.append("verification-older-than-180-days")
    return signals


def _priority_score(signals: list[str]) -> int:
    weights = {
        "unknown-license": 5,
        "unknown-maturity": 3,
        "missing-repository-url": 2,
        "missing-documentation-url": 2,
        "missing-sources": 2,
        "verification-older-than-180-days": 1,
    }
    return sum(weights[item] for item in signals)


def _priority_candidate_sort_key(
    candidate: dict[str, object],
) -> tuple[int, date, str]:
    return (
        -int(candidate["priority_score"]),
        _parse_date(candidate["verified_on"]),
        str(candidate["id"]),
    )


def build_inventory(root: Path = ROOT) -> dict[str, object]:
    taxonomy = load_taxonomy(root)
    tools = load_tools(root)
    if not tools:
        raise ValueError("catalogue is empty")

    reference_date = max(_parse_date(tool["verified_on"]) for tool in tools)
    category_names = {item["id"]: item["name"] for item in taxonomy["categories"]}
    category_counts: dict[str, dict[str, object]] = {
        category_id: {
            "name": category_names[category_id],
            "total": 0,
            "requires_review": 0,
            "unknown_license": 0,
        }
        for category_id in category_names
    }
    review_license_models: Counter[str] = Counter()
    verification_age: Counter[str] = Counter()
    candidates: list[dict[str, object]] = []

    totals = Counter()
    totals["canonical_records"] = len(tools)

    for tool in tools:
        requires_review = _requires_review(tool)
        unknown_license = tool["license_model"] == "unknown"
        unknown_maturity = tool.get("maturity", "unknown") == "unknown"
        age_days = (reference_date - _parse_date(tool["verified_on"])).days
        verification_age[_age_bucket(age_days)] += 1

        totals["records_requiring_review"] += int(requires_review)
        totals["unknown_license"] += int(unknown_license)
        totals["unknown_maturity"] += int(unknown_maturity)
        totals["repository_archived"] += int(bool(tool.get("repository_archived")))
        totals["missing_repository_url"] += int(not bool(tool.get("repository_url")))
        totals["missing_documentation_url"] += int(
            not bool(tool.get("documentation_url"))
        )
        totals["missing_sources"] += int(not bool(tool.get("sources")))

        if requires_review:
            review_license_models[str(tool["license_model"])] += 1

        for category_id in tool["categories"]:
            counts = category_counts[str(category_id)]
            counts["total"] = int(counts["total"]) + 1
            counts["requires_review"] = int(counts["requires_review"]) + int(
                requires_review
            )
            counts["unknown_license"] = int(counts["unknown_license"]) + int(
                unknown_license
            )

        if requires_review:
            signals = _priority_signals(tool, age_days=age_days)
            candidates.append(
                {
                    "id": tool["id"],
                    "name": tool["name"],
                    "priority_score": _priority_score(signals),
                    "signals": signals,
                    "license_model": tool["license_model"],
                    "maturity": tool.get("maturity", "unknown"),
                    "verified_on": str(tool["verified_on"]),
                    "primary_category": tool["categories"][0],
                }
            )

    candidates.sort(key=_priority_candidate_sort_key)

    return {
        "schema_version": 1,
        "reference_date": reference_date.isoformat(),
        "totals": dict(sorted(totals.items())),
        "review_by_license_model": dict(sorted(review_license_models.items())),
        "verification_age_days": {
            bucket: verification_age[bucket] for bucket in AGE_BUCKETS
        },
        "by_category": dict(sorted(category_counts.items())),
        "priority_candidates": candidates,
    }


def render_markdown(inventory: dict[str, object], *, limit: int = 20) -> str:
    totals = inventory["totals"]
    by_category = inventory["by_category"]
    review_by_license = inventory["review_by_license_model"]
    age = inventory["verification_age_days"]
    candidates = inventory["priority_candidates"][:limit]

    rows = [
        "# Catalogue review-debt inventory",
        "",
        "Deterministic snapshot derived only from canonical YAML. The reference date is the latest `verified_on` date in the catalogue, so repeated runs against the same commit are byte-stable.",
        "",
        f"**Reference date:** {inventory['reference_date']}",
        "",
        "## Totals",
        "",
        "| Signal | Records |",
        "|---|---:|",
        f"| Canonical records | {totals['canonical_records']} |",
        f"| Records requiring review | {totals['records_requiring_review']} |",
        f"| Unknown licence model | {totals['unknown_license']} |",
        f"| Unknown maturity | {totals['unknown_maturity']} |",
        f"| Archived repositories | {totals['repository_archived']} |",
        f"| Missing repository URL | {totals['missing_repository_url']} |",
        f"| Missing documentation URL | {totals['missing_documentation_url']} |",
        f"| Missing sources | {totals['missing_sources']} |",
        "",
        "## Review debt by licence model",
        "",
        "| Licence model | Records requiring review |",
        "|---|---:|",
    ]
    rows.extend(
        f"| `{model}` | {count} |" for model, count in review_by_license.items()
    )
    rows.extend(
        [
            "",
            "## Verification age",
            "",
            "| Age from reference date | Records |",
            "|---|---:|",
        ]
    )
    rows.extend(f"| {bucket} days | {age[bucket]} |" for bucket in AGE_BUCKETS)
    rows.extend(
        [
            "",
            "## Review debt by category",
            "",
            "| Category | Total | Requires review | Unknown licence |",
            "|---|---:|---:|---:|",
        ]
    )
    for category_id, counts in by_category.items():
        rows.append(
            f"| {counts['name']} (`{category_id}`) | {counts['total']} | "
            f"{counts['requires_review']} | {counts['unknown_license']} |"
        )
    rows.extend(
        [
            "",
            f"## Top {len(candidates)} deterministic review candidates",
            "",
            "Priority is a triage aid, not an evidence decision. Scores favor unknown licensing first, then unknown maturity, missing repository/documentation/source evidence, and stale verification. Candidates are ordered by score, then oldest verification date, then stable canonical ID.",
            "",
            "| Score | Tool | Category | Licence | Verified | Signals |",
            "|---:|---|---|---|---|---|",
        ]
    )
    for item in candidates:
        signals = ", ".join(item["signals"]) or "review-state-only"
        rows.append(
            f"| {item['priority_score']} | {item['name']} (`{item['id']}`) | "
            f"`{item['primary_category']}` | `{item['license_model']}` | "
            f"{item['verified_on']} | {signals} |"
        )
    rows.append("")
    return "\n".join(rows)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")
    parser.add_argument("--limit", type=int, default=20)
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    inventory = build_inventory(args.root.resolve())
    if args.format == "json":
        print(json.dumps(inventory, indent=2, sort_keys=True))
    else:
        print(render_markdown(inventory, limit=args.limit), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
