from scripts.catalog import load_tools

BATCH_07_IDS = {
    "actions-runner-controller",
    "ansible",
    "artifact-hub",
    "atmos",
    "easykube",
    "koreo",
    "openfeature",
    "pulse-relay",
    "robusta",
    "rsyslog",
}


def _tools_by_id() -> dict[str, dict[str, object]]:
    return {tool["id"]: tool for tool in load_tools()}


def test_batch_07_records_are_current_and_fully_accounted() -> None:
    tools = _tools_by_id()

    assert len(BATCH_07_IDS) == 10
    for tool_id in BATCH_07_IDS:
        tool = tools[tool_id]
        assert tool["verified_on"] == "2026-09-22"
        assert tool["status"] == "active"
        assert tool["maturity"] != "unknown"
        assert tool["license_model"] != "unknown"
        assert tool["needs_review"] is False


def test_batch_07_repository_and_license_boundaries_are_explicit() -> None:
    tools = _tools_by_id()

    assert tools["actions-runner-controller"]["repository_url"] == (
        "https://github.com/actions/actions-runner-controller"
    )
    assert tools["actions-runner-controller"]["license_spdx"] == "Apache-2.0"

    assert tools["ansible"]["license_spdx"] == "GPL-3.0-or-later"
    assert tools["artifact-hub"]["license_spdx"] == "Apache-2.0"
    assert tools["atmos"]["license_spdx"] == "Apache-2.0"
    assert tools["koreo"]["license_spdx"] == "Apache-2.0"
    assert tools["openfeature"]["repository_url"] == "https://github.com/open-feature/spec"
    assert tools["openfeature"]["license_spdx"] == "Apache-2.0"
    assert tools["rsyslog"]["license_spdx"] == "LGPL-3.0-only"


def test_batch_07_nonstandard_and_commercial_boundaries_stay_explicit() -> None:
    tools = _tools_by_id()

    easykube = tools["easykube"]
    assert easykube["repository_url"] == "https://github.com/torloejborg/easykube"
    assert easykube["license_model"] == "source-available"
    assert "license_spdx" not in easykube

    pulse = tools["pulse-relay"]
    assert pulse["name"] == "Pulse"
    assert pulse["license_model"] == "oss"
    assert pulse["commercial_offering"] is True
    assert pulse["repository_url"] == "https://github.com/rcourtman/Pulse"

    robusta = tools["robusta"]
    assert robusta["license_model"] == "open-core"
    assert robusta["commercial_offering"] is True
    assert robusta["license_spdx"] == "MIT"
