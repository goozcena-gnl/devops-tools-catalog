from scripts.catalog import load_tools


def tools_by_id() -> dict[str, dict]:
    return {tool["id"]: tool for tool in load_tools()}


def test_p0_identity_and_lifecycle_corrections() -> None:
    tools = tools_by_id()

    tnu = tools["tnu"]
    assert tnu["name"] == "Talos Node Updater (tnu)"
    assert "Talos Linux node upgrades" in tnu["summary"]
    assert tnu["categories"] == [
        "deprecated-historical",
        "kubernetes-distributions-operations",
    ]
    assert tnu["status"] == "archived"

    headlamp = tools["headlamp"]
    assert headlamp["repository_url"] == "https://github.com/kubernetes-sigs/headlamp"
    assert headlamp["repository_archived"] is False
    assert headlamp["status"] == "active"
    assert tools["headlamp-plugins"]["repository_url"] == (
        "https://github.com/headlamp-k8s/plugins"
    )

    localstack = tools["localstack"]
    assert localstack["status"] == "active"
    assert localstack["repository_archived"] is True
    assert localstack["license_model"] == "commercial"

    minio = tools["minio"]
    assert minio["name"] == "MinIO Community Server"
    assert minio["categories"][0] == "deprecated-historical"
    assert minio["repository_archived"] is True
    assert minio["status"] == "archived"


def test_p1_upstream_and_review_state_corrections() -> None:
    tools = tools_by_id()

    velero = tools["velero"]
    assert velero["repository_url"] == "https://github.com/velero-io/velero"
    assert velero["repository_archived"] is False
    assert velero["status"] == "active"
    assert velero["needs_review"] is False

    juju = tools["juju"]
    assert juju["repository_archived"] is False
    assert juju["status"] == "active"
    assert juju["needs_review"] is False

    oncall = tools["grafana-oncall"]
    assert oncall["name"] == "Grafana OnCall OSS"
    assert oncall["repository_url"] == (
        "https://github.com/grafana-cold-storage/oncall"
    )
    assert oncall["repository_archived"] is True
    assert oncall["status"] == "archived"
    assert oncall["needs_review"] is False

    cdktf = tools["cdktf"]
    assert cdktf["status"] == "archived"
    assert cdktf["license_model"] == "oss"
    assert cdktf["license_spdx"] == "MPL-2.0"
    assert cdktf["alternatives"] == ["terraform"]

    dashboard = tools["kubernetes-dashboard"]
    assert dashboard["repository_url"] == (
        "https://github.com/kubernetes-retired/dashboard"
    )
    assert dashboard["alternatives"] == ["headlamp"]
    assert dashboard["needs_review"] is False


def test_reverified_archived_records_remain_correct() -> None:
    tools = tools_by_id()

    for tool_id in ("cai-robotsec", "datree", "kaniko", "keptn", "kubeapps"):
        tool = tools[tool_id]
        assert tool["repository_archived"] is True
        assert tool["status"] == "archived"
        assert tool["needs_review"] is False
