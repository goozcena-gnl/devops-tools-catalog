import pytest

from tests.catalogue_baseline import assert_baseline_preserved, baseline_ids


def test_baseline_allows_an_unrelated_addition() -> None:
    assert_baseline_preserved([*baseline_ids(), "future-catalogue-tool"])


def test_addition_cannot_hide_a_removed_baseline_identity() -> None:
    ids = set(baseline_ids())
    removed = min(ids)
    ids.remove(removed)
    ids.add("future-catalogue-tool")
    with pytest.raises(AssertionError, match=removed):
        assert_baseline_preserved(list(ids))


def test_baseline_rejects_duplicate_identities() -> None:
    ids = list(baseline_ids())
    with pytest.raises(AssertionError, match="Duplicate canonical IDs"):
        assert_baseline_preserved([*ids, ids[0]])
