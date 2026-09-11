from __future__ import annotations

from scripts.catalog import load_taxonomy, load_tools
from scripts.review_debt import AGE_BUCKETS, build_inventory, render_markdown


def test_review_debt_inventory_reconciles_with_catalogue() -> None:
    tools = load_tools()
    taxonomy = load_taxonomy()
    inventory = build_inventory()
    totals = inventory["totals"]

    assert totals["canonical_records"] == len(tools)
    assert totals["records_requiring_review"] == sum(
        bool(tool.get("needs_review")) or tool["status"] == "needs-review"
        for tool in tools
    )
    assert totals["unknown_license"] == sum(
        tool["license_model"] == "unknown" for tool in tools
    )
    assert totals["unknown_maturity"] == sum(
        tool.get("maturity", "unknown") == "unknown" for tool in tools
    )
    assert sum(inventory["verification_age_days"].values()) == len(tools)
    assert tuple(inventory["verification_age_days"]) == AGE_BUCKETS
    assert set(inventory["by_category"]) == {
        item["id"] for item in taxonomy["categories"]
    }


def test_review_debt_category_accounting_matches_membership() -> None:
    tools = load_tools()
    inventory = build_inventory()

    for category_id, counts in inventory["by_category"].items():
        selected = [tool for tool in tools if category_id in tool["categories"]]
        assert counts["total"] == len(selected)
        assert counts["requires_review"] == sum(
            bool(tool.get("needs_review")) or tool["status"] == "needs-review"
            for tool in selected
        )
        assert counts["unknown_license"] == sum(
            tool["license_model"] == "unknown" for tool in selected
        )


def test_priority_candidates_are_review_only_and_stably_sorted() -> None:
    inventory = build_inventory()
    candidates = inventory["priority_candidates"]
    tools = {tool["id"]: tool for tool in load_tools()}

    assert candidates == sorted(
        candidates,
        key=lambda item: (-int(item["priority_score"]), str(item["id"])),
    )
    assert all(
        bool(tools[item["id"]].get("needs_review"))
        or tools[item["id"]]["status"] == "needs-review"
        for item in candidates
    )


def test_review_debt_output_is_deterministic() -> None:
    first = build_inventory()
    second = build_inventory()

    assert first == second
    assert render_markdown(first, limit=20) == render_markdown(second, limit=20)
    assert "# Catalogue review-debt inventory" in render_markdown(first, limit=20)
    assert "## Top 20 deterministic review candidates" in render_markdown(
        first, limit=20
    )
