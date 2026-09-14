from __future__ import annotations

from scripts.catalog import load_taxonomy, load_tools
from scripts.review_debt import (
    AGE_BUCKETS,
    _priority_candidate_sort_key,
    build_inventory,
    render_markdown,
)


def _candidate(candidate_id: str, *, score: int, verified_on: str) -> dict[str, object]:
    return {
        "id": candidate_id,
        "priority_score": score,
        "verified_on": verified_on,
    }


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
        key=_priority_candidate_sort_key,
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


def test_priority_score_dominates_verification_recency() -> None:
    candidates = [
        _candidate("older-lower-score", score=10, verified_on="2026-08-03"),
        _candidate("newer-higher-score", score=12, verified_on="2026-09-13"),
    ]

    ordered = sorted(candidates, key=_priority_candidate_sort_key)

    assert [item["id"] for item in ordered] == [
        "newer-higher-score",
        "older-lower-score",
    ]


def test_oldest_verification_breaks_equal_priority_scores() -> None:
    candidates = [
        _candidate("recent", score=12, verified_on="2026-09-13"),
        _candidate("older", score=12, verified_on="2026-08-03"),
    ]

    ordered = sorted(candidates, key=_priority_candidate_sort_key)

    assert [item["id"] for item in ordered] == ["older", "recent"]


def test_canonical_id_breaks_equal_score_and_verification_date() -> None:
    candidates = [
        _candidate("zulu", score=12, verified_on="2026-08-03"),
        _candidate("alpha", score=12, verified_on="2026-08-03"),
    ]

    ordered = sorted(candidates, key=_priority_candidate_sort_key)

    assert [item["id"] for item in ordered] == ["alpha", "zulu"]


def test_recent_unresolved_candidates_remain_visible_below_older_equal_debt() -> None:
    candidates = build_inventory()["priority_candidates"]
    positions = {item["id"]: index for index, item in enumerate(candidates)}
    by_id = {item["id"]: item for item in candidates}

    for recent_id in {"everydev-ai", "filigran"}:
        assert recent_id in positions
        assert (
            by_id[recent_id]["priority_score"]
            == by_id["git-push-no-mistakes"]["priority_score"]
        )
        assert by_id[recent_id]["verified_on"] == "2026-09-13"
        assert positions["git-push-no-mistakes"] < positions[recent_id]
