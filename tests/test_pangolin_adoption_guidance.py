"""Regression coverage for Pangolin Community and Enterprise adoption guidance."""

from __future__ import annotations

from collections import Counter

from scripts.catalog import load_tools

EXPECTED_EXISTING_SOURCES = {
    "legacy:devopstools_final.md#L960",
    "https://pangolin.net",
    "https://docs.pangolin.net",
    "https://github.com/fosrl/pangolin",
}
EXPECTED_EVIDENCE_SOURCES = {
    "https://github.com/fosrl/pangolin/blob/main/LICENSE",
    "https://docs.pangolin.net/development/contributing",
    "https://docs.pangolin.net/self-host/enterprise-edition",
}
EXPECTED_AVOID_WHEN = [
    "You need a conventional site-to-site VPN without application-aware access controls.",
    "Your organization cannot comply with the AGPLv3 terms applicable to the Community Edition.",
    "You require Enterprise-only features but cannot accept Pangolin's separate commercial licence.",
]


def _pangolin() -> dict:
    tools = load_tools()
    counts = Counter(tool["id"] for tool in tools)
    assert len(tools) == 1306
    assert counts["pangolin"] == 1
    return next(tool for tool in tools if tool["id"] == "pangolin")


def test_pangolin_identity_licensing_and_provenance_are_preserved() -> None:
    pangolin = _pangolin()
    assert pangolin["official_url"] == "https://pangolin.net"
    assert pangolin["repository_url"] == "https://github.com/fosrl/pangolin"
    assert pangolin["documentation_url"] == "https://docs.pangolin.net"
    assert pangolin["license_model"] == "open-core"
    assert pangolin["license_spdx"] == "AGPL-3.0-only"
    assert pangolin["commercial_offering"] is True
    assert pangolin["status"] == "active"
    assert pangolin["needs_review"] is False
    assert pangolin["verified_on"] == "2026-09-05"
    assert (
        set(pangolin["sources"])
        == EXPECTED_EXISTING_SOURCES | EXPECTED_EVIDENCE_SOURCES
    )
    assert len(pangolin["sources"]) == len(set(pangolin["sources"]))


def test_pangolin_guidance_distinguishes_community_and_enterprise_terms() -> None:
    pangolin = _pangolin()
    assert pangolin["use_when"] == [
        "You need identity-aware access to private web and network resources without opening inbound ports."
    ]
    assert pangolin["avoid_when"] == EXPECTED_AVOID_WHEN
    functional, community, enterprise = pangolin["avoid_when"]
    assert "site-to-site VPN" in functional
    assert "commercial licence" not in functional
    assert "AGPLv3" in community
    assert "Community Edition" in community
    assert "Enterprise-only" in enterprise
    assert "commercial licence" in enterprise
    assert "commercial licence" not in community
