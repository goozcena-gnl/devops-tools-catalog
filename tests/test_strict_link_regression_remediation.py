import json
from pathlib import Path

from scripts.catalog import ROOT, load_tools


def tools_by_id() -> dict[str, dict]:
    return {tool["id"]: tool for tool in load_tools()}


def test_floci_az_uses_current_project_owned_documentation() -> None:
    tools = tools_by_id()
    floci_az = tools["floci-az"]

    assert floci_az["documentation_url"] == "https://floci.io/floci-az/"
    assert floci_az["status"] == "active"
    assert floci_az.get("repository_archived") is not True
    assert "https://floci.io/floci-az/getting-started/" not in {
        str(tool.get(field))
        for tool in tools.values()
        for field in ("official_url", "repository_url", "documentation_url")
    }


def test_datree_is_retained_as_an_archived_open_source_project() -> None:
    datree = tools_by_id()["datree"]

    assert datree["official_url"] == "https://github.com/datreeio/datree"
    assert datree["repository_url"] == "https://github.com/datreeio/datree"
    assert datree["repository_archived"] is True
    assert datree["status"] == "archived"
    assert datree["license_model"] == "oss"
    assert datree["license_spdx"] == "Apache-2.0"
    assert datree["needs_review"] is False


def test_cai_is_archived_separately_from_its_csi_successor() -> None:
    cai = tools_by_id()["cai-robotsec"]

    assert cai["repository_url"] == "https://github.com/aliasrobotics/cai"
    assert cai["repository_archived"] is True
    assert cai["status"] == "archived"
    assert cai["needs_review"] is False
    assert (
        "https://aliasrobotics.com/cybersecuritysuperintelligence.php" in cai["sources"]
    )


def test_new_regressions_are_not_added_to_reviewed_debt_baseline() -> None:
    baseline = json.loads(
        (Path(ROOT) / "config" / "link-audit-baseline.json").read_text(encoding="utf-8")
    )
    baselined_urls = {item["url"] for item in baseline["reviewed_blockers"]}

    assert not baselined_urls & {
        "https://floci.io/floci-az/getting-started/",
        "https://www.datree.io",
        "https://github.com/aliasrobotics/cai",
    }
