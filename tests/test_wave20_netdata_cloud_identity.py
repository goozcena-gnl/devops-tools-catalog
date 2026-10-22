"""Protect the Wave 20 Netdata Cloud versus Agent source boundary."""

from scripts.catalog import ROOT, load_tools


def test_netdata_cloud_has_no_agent_source_repository() -> None:
    tools = {item["id"]: item for item in load_tools()}
    cloud = tools["netdata-cloud"]
    assert cloud["official_url"] == "https://www.netdata.cloud"
    assert cloud["documentation_url"] == "https://learn.netdata.cloud/"
    assert cloud.get("repository_url") is None
    assert cloud.get("repository_archived") is None
    assert cloud["license_model"] == "free-saas"
    assert cloud["commercial_offering"] is True
    assert cloud["status"] == "active"
    assert cloud["needs_review"] is False
    assert "https://github.com/netdata/netdata/blob/master/LICENSE" in cloud["sources"]


def test_netdata_cloud_generated_page_has_no_agent_source_link() -> None:
    rendered = (ROOT / "docs/categories/monitoring-metrics-logs-tracing.md").read_text(
        encoding="utf-8"
    )
    cloud_section = rendered.split("### Netdata Cloud\n", 1)[1].split("\n### ", 1)[0]
    assert "[Official site](https://www.netdata.cloud)" in cloud_section
    assert "[Documentation](https://learn.netdata.cloud/)" in cloud_section
    assert "[Source repository]" not in cloud_section
