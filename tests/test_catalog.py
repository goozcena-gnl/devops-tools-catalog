from __future__ import annotations

import csv

from scripts.catalog import ROOT, load_tools
from scripts.validate_catalog import validate_records
from tests.conftest import minimal_record, write_catalog


def test_duplicate_id_detection(tmp_path) -> None:
    write_catalog(tmp_path, [minimal_record(), minimal_record()])
    assert any(
        "duplicate id example-tool" in error for error in validate_records(tmp_path)
    )


def test_duplicate_canonical_url_detection(tmp_path) -> None:
    records = [
        minimal_record(),
        minimal_record(id="another-tool", name="Another Tool"),
    ]
    write_catalog(tmp_path, records)
    assert any(
        "duplicate official_url" in error for error in validate_records(tmp_path)
    )


def test_invalid_category_detection(tmp_path) -> None:
    write_catalog(tmp_path, [minimal_record(categories=["not-a-category"])])
    assert any("invalid categories" in error for error in validate_records(tmp_path))


def test_invalid_role_detection(tmp_path) -> None:
    write_catalog(tmp_path, [minimal_record(roles=["not-a-role"])])
    assert any("invalid roles" in error for error in validate_records(tmp_path))


def test_multi_category_tool_is_preserved() -> None:
    trivy = next(tool for tool in load_tools() if tool["id"] == "trivy")
    assert set(trivy["categories"]) == {
        "kubernetes-networking-storage-addons",
        "application-cloud-security",
    }


def test_arm_templates_license_is_verified() -> None:
    arm_templates = next(tool for tool in load_tools() if tool["id"] == "arm-templates")
    assert arm_templates["license_model"] == "oss"
    assert arm_templates["license_spdx"] == "MIT"
    assert arm_templates["needs_review"] is False


def test_localstack_active_tool_with_archived_repository() -> None:
    localstack = next(tool for tool in load_tools() if tool["id"] == "localstack")
    assert localstack["status"] == "active"
    assert localstack["repository_archived"] is True
    assert localstack["needs_review"] is False


def test_capsule_uses_current_project_repository() -> None:
    capsule = next(tool for tool in load_tools() if tool["id"] == "capsule")
    assert capsule["official_url"] == "https://projectcapsule.dev/"
    assert capsule["repository_url"] == "https://github.com/projectcapsule/capsule"
    assert capsule["status"] == "active"


def test_cai_remains_under_review_for_license_boundary() -> None:
    cai = next(tool for tool in load_tools() if tool["id"] == "cai-robotsec")
    assert cai["license_model"] == "source-available"
    assert cai["status"] == "needs-review"
    assert cai["needs_review"] is True


def test_commercial_cloud_services_can_be_active() -> None:
    tools = load_tools()
    aws = next(tool for tool in tools if tool["id"] == "amazon-web-services-aws")
    storage_gateway = next(
        tool for tool in tools if tool["id"] == "aws-storage-gateway"
    )
    assert aws["license_model"] == "commercial"
    assert storage_gateway["license_model"] == "commercial"
    assert aws["status"] == "active"
    assert storage_gateway["status"] == "active"


def test_batch03_commercial_platforms_are_active() -> None:
    tools = load_tools()
    for tool_id in ["civo", "cloudfuze", "cloudzero", "dash0"]:
        tool = next(tool for tool in tools if tool["id"] == tool_id)
        assert tool["license_model"] == "commercial"
        assert tool["commercial_offering"] is True
        assert tool["status"] == "active"
        assert tool["needs_review"] is False


def test_batch03_open_source_ci_cd_tools_are_active() -> None:
    tools = load_tools()
    commitlint = next(tool for tool in tools if tool["id"] == "commitlint")
    concourse = next(tool for tool in tools if tool["id"] == "concourse")
    assert commitlint["license_model"] == "oss"
    assert commitlint["license_spdx"] == "MIT"
    assert commitlint["status"] == "active"
    assert concourse["license_model"] == "oss"
    assert concourse["license_spdx"] == "Apache-2.0"
    assert concourse["status"] == "active"


def test_batch03_open_core_monitoring_docs_are_present() -> None:
    tools = load_tools()
    centreon = next(tool for tool in tools if tool["id"] == "centreon")
    checkmk = next(tool for tool in tools if tool["id"] == "checkmk")
    assert centreon["license_model"] == "open-core"
    assert centreon["documentation_url"] == "https://docs.centreon.com/"
    assert centreon["status"] == "active"
    assert checkmk["license_model"] == "open-core"
    assert checkmk["documentation_url"] == "https://docs.checkmk.com/latest/en/"
    assert checkmk["status"] == "active"


def test_batch03_conftest_has_authoritative_apache_license() -> None:
    conftest = next(tool for tool in load_tools() if tool["id"] == "conftest")
    assert conftest["license_model"] == "oss"
    assert conftest["license_spdx"] == "Apache-2.0"
    assert conftest["status"] == "active"


def test_batch03_ctop_remains_under_review_pending_maintenance_signal() -> None:
    ctop = next(tool for tool in load_tools() if tool["id"] == "ctop")
    assert ctop["license_model"] == "oss"
    assert ctop["license_spdx"] == "MIT"
    assert ctop["status"] == "needs-review"
    assert ctop["needs_review"] is True


def test_batch04_verified_tools_are_active_with_expected_metadata() -> None:
    tools = load_tools()

    coraza = next(tool for tool in tools if tool["id"] == "coraza")
    assert coraza["license_model"] == "oss"
    assert coraza["license_spdx"] == "Apache-2.0"
    assert coraza["status"] == "active"
    assert coraza["needs_review"] is False

    crowdsec = next(tool for tool in tools if tool["id"] == "crowdsec")
    assert crowdsec["license_model"] == "open-core"
    assert crowdsec["license_spdx"] == "MIT"
    assert crowdsec["commercial_offering"] is True
    assert crowdsec["status"] == "active"
    assert crowdsec["needs_review"] is False

    for tool_id, spdx in [
        ("flux", "Apache-2.0"),
        ("kargo", "Apache-2.0"),
        ("crossplane", "Apache-2.0"),
        ("gateway-api", "Apache-2.0"),
        ("litmuschaos", "Apache-2.0"),
        ("trivy", "Apache-2.0"),
        ("firecracker", "Apache-2.0"),
        ("flatcar-container-linux", "Apache-2.0"),
    ]:
        tool = next(tool for tool in tools if tool["id"] == tool_id)
        assert tool["license_model"] == "oss"
        assert tool["license_spdx"] == spdx
        assert tool["status"] == "active"
        assert tool["needs_review"] is False

    infracost = next(tool for tool in tools if tool["id"] == "infracost")
    assert infracost["license_model"] == "open-core"
    assert infracost["license_spdx"] == "Apache-2.0"
    assert infracost["commercial_offering"] is True
    assert infracost["status"] == "active"
    assert infracost["needs_review"] is False

    cypress = next(tool for tool in tools if tool["id"] == "cypress")
    assert cypress["license_model"] == "open-core"
    assert cypress["license_spdx"] == "MIT"
    assert cypress["commercial_offering"] is True
    assert cypress["status"] == "active"
    assert cypress["needs_review"] is False

    dagger = next(tool for tool in tools if tool["id"] == "dagger")
    assert dagger["license_model"] == "open-core"
    assert dagger["license_spdx"] == "Apache-2.0"
    assert dagger["commercial_offering"] is True
    assert dagger["status"] == "active"
    assert dagger["needs_review"] is False

    for tool_id in [
        "concierto-cloud",
        "digitalocean",
        "datadog-cloud-cost-management",
        "finout",
    ]:
        tool = next(tool for tool in tools if tool["id"] == tool_id)
        assert tool["license_model"] == "commercial"
        assert tool["commercial_offering"] is True
        assert tool["status"] == "active"
        assert tool["needs_review"] is False

    freelens = next(tool for tool in tools if tool["id"] == "freelens")
    assert freelens["license_model"] == "oss"
    assert freelens["license_spdx"] == "MIT"
    assert freelens["status"] == "active"
    assert freelens["needs_review"] is False

    coroot = next(tool for tool in tools if tool["id"] == "coroot")
    assert coroot["license_model"] == "oss"
    assert coroot["license_spdx"] == "AGPL-3.0-only"
    assert coroot["status"] == "active"
    assert coroot["needs_review"] is False


def test_batch04_elastic_apm_server_remains_under_review_for_license_boundary() -> None:
    elastic_apm = next(
        tool for tool in load_tools() if tool["id"] == "elastic-apm-server"
    )
    assert elastic_apm["license_model"] == "source-available"
    assert elastic_apm["status"] == "needs-review"
    assert elastic_apm["needs_review"] is True
    assert (
        elastic_apm["documentation_url"]
        == "https://www.elastic.co/guide/en/apm/server/current/index.html"
    )


def test_batch05_verified_tools_are_active_with_expected_metadata() -> None:
    tools = load_tools()

    for tool_id, spdx in [
        ("dependencycheck", "Apache-2.0"),
        ("dockle", "Apache-2.0"),
        ("linkerd", "Apache-2.0"),
        ("aralez", "Apache-2.0"),
        ("k0s", "Apache-2.0"),
        ("k3s", "Apache-2.0"),
        ("fluent-bit", "Apache-2.0"),
        ("kics", "Apache-2.0"),
        ("kusionstack", "Apache-2.0"),
        ("incus", "Apache-2.0"),
        ("kata-containers", "Apache-2.0"),
    ]:
        tool = next(tool for tool in tools if tool["id"] == tool_id)
        assert tool["license_model"] == "oss"
        assert tool["license_spdx"] == spdx
        assert tool["status"] == "active"
        assert tool["needs_review"] is False

    fitnesse = next(tool for tool in tools if tool["id"] == "fitnesse")
    assert fitnesse["license_model"] == "oss"
    assert fitnesse["license_spdx"] == "CPL-1.0"
    assert fitnesse["status"] == "active"
    assert fitnesse["needs_review"] is False

    keel = next(tool for tool in tools if tool["id"] == "keel")
    assert keel["license_model"] == "oss"
    assert keel["license_spdx"] == "MPL-2.0"
    assert keel["status"] == "active"
    assert keel["needs_review"] is False

    piku = next(tool for tool in tools if tool["id"] == "piku")
    assert piku["license_model"] == "oss"
    assert piku["license_spdx"] == "MIT"
    assert piku["status"] == "active"
    assert piku["needs_review"] is False

    drone = next(tool for tool in tools if tool["id"] == "drone")
    assert drone["license_model"] == "open-core"
    assert drone["license_spdx"] == "Apache-2.0"
    assert drone["commercial_offering"] is True
    assert drone["status"] == "active"
    assert drone["needs_review"] is False

    for tool_id in [
        "google-cloud-platform",
        "flexera-one",
        "ibm-turbonomic-cloud-optimization",
    ]:
        tool = next(tool for tool in tools if tool["id"] == tool_id)
        assert tool["license_model"] == "commercial"
        assert tool["commercial_offering"] is True
        assert tool["status"] == "active"
        assert tool["needs_review"] is False

    exoway = next(tool for tool in tools if tool["id"] == "exoway")
    assert exoway["license_model"] == "commercial"
    assert exoway["commercial_offering"] is True
    assert exoway["status"] == "needs-review"
    assert exoway["needs_review"] is True


def test_batch05_elastic_stack_remains_under_review_for_license_boundary() -> None:
    elastic_stack = next(
        tool for tool in load_tools() if tool["id"] == "elastic-stack-elk"
    )
    assert elastic_stack["license_model"] == "source-available"
    assert elastic_stack["commercial_offering"] is True
    assert elastic_stack["status"] == "needs-review"
    assert elastic_stack["needs_review"] is True
    assert (
        elastic_stack["documentation_url"]
        == "https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html"
    )


def test_every_source_occurrence_has_a_disposition() -> None:
    with (ROOT / "migration" / "reconciliation.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 1894
    assert all(row["disposition"] and row["reason"] for row in rows)
