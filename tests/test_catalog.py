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


def test_every_source_occurrence_has_a_disposition() -> None:
    with (ROOT / "migration" / "reconciliation.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 1894
    assert all(row["disposition"] and row["reason"] for row in rows)
