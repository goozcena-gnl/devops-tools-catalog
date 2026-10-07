"""Durable implementation, service and licensing boundaries reviewed in Wave 9."""

import pytest

from scripts.catalog import load_tools


@pytest.fixture(scope="module")
def catalogue() -> dict[str, dict]:
    return {tool["id"]: tool for tool in load_tools()}


@pytest.mark.parametrize(
    ("tool_id", "repository", "branch", "licence", "spdx"),
    [
        ("cosign-sigstore", "sigstore/cosign", "main", "LICENSE", "Apache-2.0"),
        ("syft", "anchore/syft", "main", "LICENSE", "Apache-2.0"),
        ("grype", "anchore/grype", "main", "LICENSE", "Apache-2.0"),
        ("gitleaks", "gitleaks/gitleaks", "master", "LICENSE", "MIT"),
        ("sops", "getsops/sops", "main", "LICENSE", "MPL-2.0"),
        ("keycloak", "keycloak/keycloak", "main", "LICENSE.txt", "Apache-2.0"),
        (
            "cert-manager",
            "cert-manager/cert-manager",
            "master",
            "LICENSE",
            "Apache-2.0",
        ),
        ("kyverno", "kyverno/kyverno", "main", "LICENSE", "Apache-2.0"),
    ],
)
def test_oss_implementations_have_their_own_licence_evidence(
    catalogue, tool_id, repository, branch, licence, spdx
) -> None:
    tool = catalogue[tool_id]
    assert tool["repository_url"] == f"https://github.com/{repository}"
    assert tool["license_model"] == "oss"
    assert tool["license_spdx"] == spdx
    assert f"https://github.com/{repository}/blob/{branch}/{licence}" in tool["sources"]


def test_cosign_remains_one_sigstore_component(catalogue) -> None:
    tool = catalogue["cosign-sigstore"]
    assert tool["repository_url"] == "https://github.com/sigstore/cosign"
    assert tool["documentation_url"].startswith("https://docs.sigstore.dev/cosign/")
    assert all(
        component in tool["summary"]
        for component in (
            "Fulcio",
            "Rekor",
            "sigstore-go",
            "policy-controller",
            "separate",
        )
    )
    assert "attestations" in tool["summary"]
    assert tool["categories"] == ["software-supply-chain-security"]


def test_syft_sbom_formats_are_not_scanner_or_software_licences(catalogue) -> None:
    syft, grype = catalogue["syft"], catalogue["grype"]
    assert syft["repository_url"] != grype["repository_url"]
    assert "SBOMs" in syft["summary"]
    assert all(standard in syft["summary"] for standard in ("SPDX", "CycloneDX"))
    assert "vulnerabilities" in " ".join(syft["avoid_when"])
    assert syft["license_spdx"] == "Apache-2.0"
    assert "SBOM generation" in syft["subcategories"]
    assert "vulnerability" in grype["summary"]
    assert "Syft" in grype["summary"] and "Trivy" in grype["summary"]
    assert "identical coverage" in " ".join(grype["avoid_when"])


@pytest.mark.parametrize("tool_id", ["syft", "grype"])
def test_anchore_oss_is_separate_from_enterprise(catalogue, tool_id) -> None:
    tool = catalogue[tool_id]
    assert tool["commercial_offering"] is True
    assert tool["deployment_models"] == ["self-hosted"]
    assert "Anchore Enterprise" in tool["summary"]
    assert tool["license_model"] == "oss"
    assert "/docs/guides/" in tool["documentation_url"]


def test_gitleaks_cli_does_not_inherit_hosted_or_action_terms(catalogue) -> None:
    tool = catalogue["gitleaks"]
    assert tool["license_spdx"] == "MIT"
    assert tool["deployment_models"] == ["self-hosted"]
    assert "Git history" in tool["summary"]
    assert "pre-commit" in tool["summary"] and "CI" in tool["summary"]
    assert "credential revocation" in " ".join(tool["avoid_when"])
    assert tool["documentation_url"].endswith("/master/README.md")


def test_sops_is_encrypted_file_editor_not_secret_serving_backend(catalogue) -> None:
    tool = catalogue["sops"]
    assert "encrypted-file editor" in tool["summary"]
    assert "Vault" in tool["summary"]
    assert all(
        boundary in " ".join(tool["avoid_when"])
        for boundary in ("secrets API", "dynamic credentials", "External Secrets")
    )
    assert tool["repository_url"] == "https://github.com/getsops/sops"
    assert "https://github.com/getsops/sops/blob/main/README.rst" in tool["sources"]


def test_vault_current_community_grant_is_not_enterprise_hcp_or_sdk(catalogue) -> None:
    tool = catalogue["hashicorp-vault"]
    assert "Community Edition" in tool["name"]
    assert tool["license_model"] == "source-available"
    assert tool["license_spdx"] == "BUSL-1.1"
    assert tool["commercial_offering"] is True
    assert tool["deployment_models"] == ["self-hosted"]
    assert "separate commercial product terms" in tool["summary"]
    assert "Vault Enterprise" in tool["summary"] and "HCP Vault" in tool["summary"]
    assert all(
        f"https://github.com/hashicorp/vault/blob/main/{component}/LICENSE"
        in tool["sources"]
        for component in ("api", "sdk")
    )
    assert "https://developer.hashicorp.com/vault/docs/license" in tool["sources"]
    assert "https://developer.hashicorp.com/vault/cloud" in tool["sources"]
    assert "https://www.vaultproject.io" in tool["sources"]


def test_keycloak_upstream_is_iam_not_vendor_package(catalogue) -> None:
    tool = catalogue["keycloak"]
    assert all(
        protocol in tool["summary"]
        for protocol in ("OpenID Connect", "OAuth 2.0", "SAML")
    )
    assert "Red Hat build" in tool["summary"]
    assert tool["documentation_url"].startswith("https://www.keycloak.org/")
    assert tool["deployment_models"] == ["self-hosted"]
    assert tool["commercial_offering"] is True
    assert any(
        source.startswith("https://docs.redhat.com/") for source in tool["sources"]
    )


def test_cert_manager_controls_certificates_not_issuer_identity(catalogue) -> None:
    tool = catalogue["cert-manager"]
    assert "X.509" in tool["summary"] and "ACME" in tool["summary"]
    assert "Let's Encrypt" in tool["summary"] and "certbot" in tool["summary"]
    assert "general secrets backends" in tool["summary"]
    assert tool["repository_url"] == "https://github.com/cert-manager/cert-manager"
    assert tool["deployment_models"] == ["self-hosted"]


def test_kyverno_policy_enforcement_is_not_artifact_signing(catalogue) -> None:
    tool = catalogue["kyverno"]
    assert all(
        capability in tool["summary"]
        for capability in ("validation", "mutation", "generation", "image verification")
    )
    assert "signatures itself" in " ".join(tool["avoid_when"])
    assert "RBAC/API-server" in " ".join(tool["avoid_when"])
    assert "OPA/Gatekeeper" in tool["summary"]
    assert "https://www.cncf.io/projects/kyverno/" in tool["sources"]
    assert "https://github.com/kyverno/kyverno/blob/main/LICENSE" in tool["sources"]


def test_notary_umbrella_does_not_become_notation_or_one_licence(catalogue) -> None:
    tool = catalogue["notary-project"]
    assert tool["name"] == "Notary Project"
    assert "umbrella" in tool["summary"] and "Notation" in tool["summary"]
    assert "repository_url" not in tool and "repository_archived" not in tool
    assert "license_spdx" not in tool
    assert tool["license_model"] == "oss"
    assert tool["deployment_models"] == []
    assert tool["official_url"] == "https://notaryproject.dev/"
    assert "https://github.com/notaryproject" in tool["sources"]
    assert all(
        f"https://github.com/notaryproject/{repo}/blob/main/LICENSE" in tool["sources"]
        for repo in ("specifications", "notation", "notation-go", "notation-core-go")
    )
    assert tool["official_url"] != catalogue["cosign-sigstore"]["official_url"]


@pytest.mark.parametrize("tool_id", ["sops", "keycloak", "cert-manager", "kyverno"])
def test_foundation_status_is_separate_from_licence(catalogue, tool_id) -> None:
    tool = catalogue[tool_id]
    assert f"https://www.cncf.io/projects/{tool_id}/" in tool["sources"]
    assert any(
        source.endswith(("/LICENSE", "/LICENSE.txt")) for source in tool["sources"]
    )
