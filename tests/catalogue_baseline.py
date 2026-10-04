"""Protect the v0.5 catalogue's identities while permitting later additions."""

from __future__ import annotations

import subprocess
from functools import cache

from scripts.catalog import ROOT

V050_BASELINE = "fb234f4798400b75e0d106fe6e4b2f7ca8c389df"


@cache
def baseline_ids() -> frozenset[str]:
    output = subprocess.check_output(
        ["git", "grep", "-h", "^- id: ", V050_BASELINE, "--", "data/tools/*.yaml"],
        cwd=ROOT,
        encoding="utf-8",
    )
    ids = [line.removeprefix("- id: ") for line in output.splitlines()]
    assert len(ids) == len(set(ids)) == 1423
    return frozenset(ids)


def assert_baseline_preserved(ids: list[str]) -> None:
    current = set(ids)
    assert len(ids) == len(current), "Duplicate canonical IDs"
    missing = baseline_ids() - current
    assert not missing, f"Missing baseline canonical IDs: {sorted(missing)}"
