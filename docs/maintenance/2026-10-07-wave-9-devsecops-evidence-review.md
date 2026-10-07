# Evidence review Wave 9 — DevSecOps, identity and software supply chain foundations — 2026-10-07

Exactly the fixed ten canonical records receive **CLEAR REVIEW** after individual review of all 24 material fields. Stable IDs and every historical source are preserved. Canonical YAML remains authoritative; generated pages are regenerated.

**Date convention:** the report filename and selected records use the user-requested Wave 9 batch marker `2026-10-07`. Research, edits and validation were executed on 2026-10-08 (Europe/Paris); the batch marker is not claimed as the execution date.

## Verified baseline and scope

- Main: `a27c65c86e23c8b793172005c38b4117b3b53469` (post-Wave-8).
- Branch: `maintenance/wave-9-devsecops-evidence-review`.
- Before editing: clean tree, zero open PRs and all five exact-main check runs successful: Analyze (actions), Analyze (python), gitleaks, Plumber audit and validate.
- Issue #2 was read: Wave 8 COMPLETED; Wave 9 NOT STARTED — READY TO SCOPE. Its body and timestamp are preserved for comparison at handoff; it is not edited.
- Initial counters and all ten expected initial states matched the request. No baseline discrepancy was found.
- Exactly ten existing records change. No unrelated record, reviewed link baseline, committed audit output, ledger, workflow, CodeQL configuration or Python constraint changes. No Wave 4–8 revisit or Wave 10 work; no merge or release.

The fixed cohort balances signing/provenance, SBOM generation, vulnerability and secret scanning, encrypted files/secrets backends, IAM, Kubernetes PKI, policy enforcement and interoperable artifact trust. Initial review status/flag debt affects all ten. Nine have unknown maturity; Cosign is experimental. All lack documentation/SPDX; Syft/Grype lack official URLs and the Notary umbrella lacks a repository.

| Rank | ID | Initial name | Initial category | Initial debt |
|---:|---|---|---|---|
| 1 | `cosign-sigstore` | cosign (sigstore) | `emerging-experimental` | needs-review; experimental maturity; missing docs; no SPDX |
| 2 | `syft` | Syft | `application-cloud-security` | needs-review; unknown maturity; missing docs; no SPDX; missing official URL |
| 3 | `grype` | Grype | `application-cloud-security` | needs-review; unknown maturity; missing docs; no SPDX; missing official URL |
| 4 | `gitleaks` | Gitleaks | `application-cloud-security` | needs-review; unknown maturity; missing docs; no SPDX |
| 5 | `sops` | SOPS | `iam-secrets-certificates` | needs-review; unknown maturity; missing docs; no SPDX |
| 6 | `keycloak` | Keycloak | `iam-secrets-certificates` | needs-review; unknown maturity; missing docs; no SPDX |
| 7 | `hashicorp-vault` | HashiCorp Vault | `iam-secrets-certificates` | needs-review; unknown maturity; missing docs; no SPDX |
| 8 | `cert-manager` | cert-manager | `kubernetes-networking-storage-addons` | needs-review; unknown maturity; missing docs; no SPDX |
| 9 | `kyverno` | Kyverno | `kubernetes-networking-storage-addons` | needs-review; unknown maturity; missing docs; no SPDX |
| 10 | `notary-project` | Notary Project | `application-cloud-security` | needs-review; unknown maturity; missing docs; no SPDX; missing umbrella repository |

## Evidence method and interpretation

Primary sources were read directly: upstream repositories/READMEs, actual licence files, official documentation and product/support terms, governance/foundation records, repository metadata and release feeds. Search results were discovery only. The official Notary site/docs were read directly through Python urllib after the browsing service could not retrieve them; both returned actual HTTP 200 content. One HTTP result alone never determines licence, maturity or lifecycle.

All nine implementation repositories were independently confirmed non-archived. Release/activity and maintenance policies support their lifecycle. Gitleaks active means feature-complete security-patch maintenance, as declared upstream. Notary remains an active umbrella with no inherited component archival flag. Kyverno foundation status comes from current CNCF evidence (Graduated, 2026-03-16), while its stale README still says Incubating. Legacy Kyverno policy-type deprecation is not project deprecation.

Catalogue established maturity is an editorial judgement from maintained implementation/specification history, documented operations and governance. It is not inferred from stars, version numbering or CNCF status. Cosign changes from experimental; nine change from unknown. Categories, roles and lifecycle stages map documented workflows to the existing taxonomy. Cosign, Syft and Notary move to software-supply-chain-security; cert-manager and Kyverno retain their valid Kubernetes add-on placement. No taxonomy values are changed.

Apache/MIT/MPL grants are verified per implementation. Current Vault Community remains source-available under BUSL-1.1, distinct from historical MPL releases, MPL API/SDK modules and Enterprise/HCP product grants. Notary retains oss but no universal SPDX, repository or deployment model; verified core component Apache grants are not made universal. Commercial support/product offerings for Syft, Grype, Keycloak and Vault are recorded without inheriting their product terms or hosted execution. Other optional commercial fields and empty alternatives/tags remain absent/unchanged.

## Decisions and complete material-field review

### cosign-sigstore

**Identity boundary:** The stable ID represents Cosign, one Sigstore CLI component. Its signing/verification and attestation scope is distinct from Fulcio CA, Rekor transparency log, sigstore-go library and policy-controller admission enforcement. Move its primary category from emerging-experimental to software-supply-chain-security.

**Licence boundary:** Apache-2.0 follows the actual Cosign LICENSE. Do not transfer this grant to every Sigstore service, third-party KMS or dependent component.

**Product/service boundary:** Self-hosted describes CLI execution, not a hosted security service. Identity-based signing can use external Sigstore services; self-managed keys/custom infrastructure are separate configurations. Optional commercial_offering remains absent.

**Repository boundary:** Retain sigstore/cosign. Add Cosign-specific docs, not a whole-Sigstore replacement repository. Existing official docs pointer is preserved without bulk redirect cleanup.

**Governance:** Sigstore PROJECT-TIERS identifies Cosign among separately governed core projects under its technical steering committee; no CNCF level is invented or inherited.

**Maturity:** Established replaces experimental based on maintained stable major releases, production signing/verification documentation, maintenance/stability policy and core-project governance. Individual APIs/features may have different stability levels; stars are not evidence.

**Lifecycle:** GitHub reports non-archived upstream with 2026-10-07 activity. Stable v3.1.3 and v2.6.5 releases (2026-08-06), maintenance guidance and API stability policy establish active lifecycle independently of network responses.

**Unresolved questions / limits:** None blocking CLI identity. Trust roots, expected signing identities/issuers, external services and feature stability must be configured for the actual workflow.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical implementation repository and scope][cosign-sigstore-e1], [Implementation software licence][cosign-sigstore-e2], [Maintained release history][cosign-sigstore-e3], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6], [Sigstore API stability policy][cosign-sigstore-e7], [Sigstore core-component governance tiers][cosign-sigstore-e8].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | cosign-sigstore | cosign-sigstore | [Canonical implementation repository and scope][cosign-sigstore-e1] | Preserve stable catalogue ID and provenance; no duplicate. |
| `name` | cosign (sigstore) | Cosign | [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6] | Changed: documented capability/identity; the scoped boundary above applies. |
| `summary` | Container/artifact signing and verification. | Sigstore CLI for signing and verifying container images, other artifacts and attestations using identity-based or self-managed keys; Fulcio, Rekor, sigstore-go and policy-controller are separate components. | [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://docs.sigstore.dev/cosign | https://docs.sigstore.dev/cosign | [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6] | Reviewed; retained: upstream-declared official entry point; any former pointer remains in sources. |
| `repository_url` | https://github.com/sigstore/cosign | https://github.com/sigstore/cosign | [Canonical implementation repository and scope][cosign-sigstore-e1] | Retain verified implementation repository. |
| `documentation_url` | *absent* | https://docs.sigstore.dev/cosign/ | [Official Cosign documentation][cosign-sigstore-e4] | Add directly checked official documentation for this record scope. |
| `categories` | emerging-experimental | software-supply-chain-security | [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `subcategories` | Other | Artifact signing and verification | [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `roles` | devops-engineer<br>platform-engineer | devops-engineer<br>platform-engineer<br>devsecops-engineer<br>release-engineer | [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `lifecycle_stages` | develop<br>learn | release<br>deploy<br>secure | [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `use_when` | You need keyless or key-based signing for container images in your supply chain. | You need artifact signatures or attestations in release and deployment workflows, with verification constrained to expected identities, issuers or trusted keys. | [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6], [Implementation software licence][cosign-sigstore-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `avoid_when` | You have no container supply-chain security requirements yet. | You expect the CLI alone to provide a certificate authority, transparency log, Kubernetes admission controller or vulnerability scanner. | [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6], [Implementation software licence][cosign-sigstore-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `deployment_models` | `[]` | self-hosted | [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6] | Record documented local/CI/server/controller self-hosted execution; external services are integrations or separate products. |
| `license_model` | oss | oss | [Implementation software licence][cosign-sigstore-e2] | Reviewed; retained: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Implementation software licence][cosign-sigstore-e2] | Changed: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Canonical implementation repository and scope][cosign-sigstore-e1] | Leave optional field absent; no denial of all third-party businesses is implied. |
| `maturity` | experimental | established | [Maintained release history][cosign-sigstore-e3], [Sigstore API stability policy][cosign-sigstore-e7], [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6], [Sigstore core-component governance tiers][cosign-sigstore-e8] | Editorial established judgement from maintained releases/specifications, documented operations and governance, with feature/component limits stated above. |
| `status` | needs-review | active | [Maintained release history][cosign-sigstore-e3], [Sigstore API stability policy][cosign-sigstore-e7], [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical implementation repository and scope][cosign-sigstore-e1], [Maintained release history][cosign-sigstore-e3], [Sigstore API stability policy][cosign-sigstore-e7] | GitHub API independently reports archived=false; lifecycle follows release/maintenance evidence. |
| `alternatives` | `[]` | `[]` | [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `tags` | `[]` | `[]` | [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical implementation repository and scope][cosign-sigstore-e1], [Implementation software licence][cosign-sigstore-e2], [Maintained release history][cosign-sigstore-e3], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6], [Sigstore API stability policy][cosign-sigstore-e7], [Sigstore core-component governance tiers][cosign-sigstore-e8] | Requested Wave 9 batch marker 2026-10-07, changed only for these ten; execution on 2026-10-08 is disclosed above. |
| `sources` | legacy:10_Miscellaneous/README.md#L64<br>legacy:devopstools_final.md#L1312 | legacy:10_Miscellaneous/README.md#L64<br>legacy:devopstools_final.md#L1312<br>https://github.com/sigstore/cosign<br>https://github.com/sigstore/cosign/blob/main/LICENSE<br>https://github.com/sigstore/cosign/releases<br>https://docs.sigstore.dev/cosign/<br>https://docs.sigstore.dev/cosign/signing/overview/<br>https://docs.sigstore.dev/cosign/verifying/verify/<br>https://docs.sigstore.dev/about/api-stability/<br>https://github.com/sigstore/community/blob/main/PROJECT-TIERS.md | [Canonical implementation repository and scope][cosign-sigstore-e1], [Implementation software licence][cosign-sigstore-e2], [Maintained release history][cosign-sigstore-e3], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6], [Sigstore API stability policy][cosign-sigstore-e7], [Sigstore core-component governance tiers][cosign-sigstore-e8] | Preserve all legacy sources and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][cosign-sigstore-e3], [Sigstore API stability policy][cosign-sigstore-e7], [Canonical implementation repository and scope][cosign-sigstore-e1], [Official Cosign documentation][cosign-sigstore-e4], [Identity-based signing documentation][cosign-sigstore-e5], [Signature and attestation verification documentation][cosign-sigstore-e6] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `name`, `summary`, `documentation_url`, `categories`, `subcategories`, `roles`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[cosign-sigstore-e1]: https://github.com/sigstore/cosign
[cosign-sigstore-e2]: https://github.com/sigstore/cosign/blob/main/LICENSE
[cosign-sigstore-e3]: https://github.com/sigstore/cosign/releases
[cosign-sigstore-e4]: https://docs.sigstore.dev/cosign/
[cosign-sigstore-e5]: https://docs.sigstore.dev/cosign/signing/overview/
[cosign-sigstore-e6]: https://docs.sigstore.dev/cosign/verifying/verify/
[cosign-sigstore-e7]: https://docs.sigstore.dev/about/api-stability/
[cosign-sigstore-e8]: https://github.com/sigstore/community/blob/main/PROJECT-TIERS.md

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/sigstore/cosign) (`archived: false`).

### syft

**Identity boundary:** Syft is the SBOM-generating CLI/Go library for supported images, filesystems and archives. It does not itself perform Grype vulnerability matching. SPDX and CycloneDX are output standards, not Syft licence names. Move primary category to software-supply-chain-security.

**Licence boundary:** Apache-2.0 is verified in Syft LICENSE; neither SPDX/CycloneDX output nor commercial Anchore product terms change its software grant.

**Product/service boundary:** The README explicitly offers commercial support options through Anchore, supporting commercial_offering=true. Execution remains self-hosted OSS; Anchore Enterprise is a separate product, not this repository licence.

**Repository boundary:** Retain anchore/syft. Use the official Syft SBOM guide as its distinct official/docs entry point; the shared Anchore OSS site is additional evidence, not a duplicate official_url. Do not use an Enterprise repository or Grype as its repository.

**Governance:** Anchore upstream organization and contribution/maintainer guidance provide the project context. No foundation status or exclusive legal ownership is inferred from the organization name.

**Maturity:** Established follows maintained 1.x releases, documented catalogers, target/format support and integrations as CLI/library; it does not promise complete discovery for every ecosystem.

**Lifecycle:** Non-archived upstream with 2026-10-07 activity and stable v1.54.1 release (2026-10-06). Maintained catalogue/format guidance and release history support active lifecycle.

**Unresolved questions / limits:** None blocking Syft identity. Supported catalogers, target selection and emitted SBOM format determine coverage; Enterprise functionality is separate.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical implementation repository and scope][syft-e1], [Implementation software licence][syft-e2], [Maintained release history][syft-e3], [Official Anchore OSS site and tool identities][syft-e4], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | syft | syft | [Canonical implementation repository and scope][syft-e1] | Preserve stable catalogue ID and provenance; no duplicate. |
| `name` | Syft | Syft | [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Generate SBOMs for containers and filesystems. | Anchore open-source CLI and Go library generating SBOMs from container images, filesystems and supported archives in formats including SPDX and CycloneDX; Grype scanning and Anchore Enterprise are separate. | [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | *absent* | https://oss.anchore.com/docs/guides/sbom/ | [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | Changed: upstream-declared official entry point; any former pointer remains in sources. |
| `repository_url` | https://github.com/anchore/syft | https://github.com/anchore/syft | [Canonical implementation repository and scope][syft-e1] | Retain verified implementation repository. |
| `documentation_url` | *absent* | https://oss.anchore.com/docs/guides/sbom/ | [Official SBOM documentation][syft-e5] | Add directly checked official documentation for this record scope. |
| `categories` | application-cloud-security | software-supply-chain-security | [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `subcategories` | Application Security (SAST, DAST, SCA) &amp; Vulnerability Scanning | SBOM generation | [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `roles` | devsecops-engineer<br>cloud-security-engineer | devsecops-engineer<br>cloud-security-engineer | [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `lifecycle_stages` | test<br>secure | build<br>test<br>secure | [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `use_when` | Produce SPDX/CycloneDX SBOMs for compliance and supply chain visibility. | You need package inventories and SBOM output for supported container images, filesystems or archives, optionally passing the resulting SBOM to a separate vulnerability scanner. | [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6], [Implementation software licence][syft-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `avoid_when` | You only need vulnerability counts (pipe Syft output into Grype). | You need Syft alone to match known vulnerabilities or provide the commercial Anchore Enterprise service; SBOM completeness depends on supported catalogers and the selected target. | [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6], [Implementation software licence][syft-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `deployment_models` | `[]` | self-hosted | [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | Record documented local/CI/server/controller self-hosted execution; external services are integrations or separate products. |
| `license_model` | oss | oss | [Implementation software licence][syft-e2] | Reviewed; retained: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Implementation software licence][syft-e2] | Changed: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Scope, supported formats and commercial support][syft-e6] | Add true for explicitly documented related commercial support/product; reviewed software licence and self-hosted execution remain separate. |
| `maturity` | unknown | established | [Maintained release history][syft-e3], [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | Editorial established judgement from maintained releases/specifications, documented operations and governance, with feature/component limits stated above. |
| `status` | needs-review | active | [Maintained release history][syft-e3], [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical implementation repository and scope][syft-e1], [Maintained release history][syft-e3] | GitHub API independently reports archived=false; lifecycle follows release/maintenance evidence. |
| `alternatives` | `[]` | `[]` | [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `tags` | `[]` | `[]` | [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical implementation repository and scope][syft-e1], [Implementation software licence][syft-e2], [Maintained release history][syft-e3], [Official Anchore OSS site and tool identities][syft-e4], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | Requested Wave 9 batch marker 2026-10-07, changed only for these ten; execution on 2026-10-08 is disclosed above. |
| `sources` | legacy:6_Security/README.md#L50<br>legacy:devopstools_final.md#L914 | legacy:6_Security/README.md#L50<br>legacy:devopstools_final.md#L914<br>https://github.com/anchore/syft<br>https://github.com/anchore/syft/blob/main/LICENSE<br>https://github.com/anchore/syft/releases<br>https://oss.anchore.com/<br>https://oss.anchore.com/docs/guides/sbom/<br>https://github.com/anchore/syft/blob/main/README.md | [Canonical implementation repository and scope][syft-e1], [Implementation software licence][syft-e2], [Maintained release history][syft-e3], [Official Anchore OSS site and tool identities][syft-e4], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | Preserve all legacy sources and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][syft-e3], [Canonical implementation repository and scope][syft-e1], [Official SBOM documentation][syft-e5], [Scope, supported formats and commercial support][syft-e6] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `official_url`, `documentation_url`, `categories`, `subcategories`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[syft-e1]: https://github.com/anchore/syft
[syft-e2]: https://github.com/anchore/syft/blob/main/LICENSE
[syft-e3]: https://github.com/anchore/syft/releases
[syft-e4]: https://oss.anchore.com/
[syft-e5]: https://oss.anchore.com/docs/guides/sbom/
[syft-e6]: https://github.com/anchore/syft/blob/main/README.md

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/anchore/syft) (`archived: false`).

### grype

**Identity boundary:** Grype matches package metadata against known vulnerabilities in supported images/filesystems/SBOMs. It uses Syft for cataloging but remains the scanner, distinct from the SBOM producer, Anchore Enterprise and Trivy; no identical-coverage comparison is retained.

**Licence boundary:** Apache-2.0 follows Grype LICENSE, independently of Syft output formats and Enterprise licensing.

**Product/service boundary:** README commercial support options justify commercial_offering=true, while the reviewed CLI remains self-hosted OSS. Enterprise packaging/services are separate.

**Repository boundary:** Retain anchore/grype, add the official OSS site and vulnerability guide. Syft and Enterprise repositories are not substituted.

**Governance:** Anchore organization/contribution context applies to this maintained upstream scanner; no unsupported CNCF or exclusive ownership claim is added.

**Maturity:** Established follows years of maintained releases, documented package matching/SBOM interoperability and operational database configuration, with coverage limits stated explicitly.

**Lifecycle:** Non-archived upstream with 2026-10-07 activity and stable v0.120.1 (2026-10-06). Current release and scanner/database documentation support active lifecycle; a 0.x version alone does not establish experimental status.

**Unresolved questions / limits:** None blocking scanner identity. Coverage varies by package ecosystem, metadata and database currency; no blanket offline guarantee or parity with Trivy is claimed.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical implementation repository and scope][grype-e1], [Implementation software licence][grype-e2], [Maintained release history][grype-e3], [Official Anchore OSS site and tool identities][grype-e4], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | grype | grype | [Canonical implementation repository and scope][grype-e1] | Preserve stable catalogue ID and provenance; no duplicate. |
| `name` | Grype | Grype | [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Vulnerability scanner for container images and filesystems. | Anchore open-source vulnerability scanner for supported container images, filesystems and SBOMs; it uses Syft package cataloging and is distinct from SBOM generation, Anchore Enterprise and Trivy. | [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | *absent* | https://oss.anchore.com/ | [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | Changed: upstream-declared official entry point; any former pointer remains in sources. |
| `repository_url` | https://github.com/anchore/grype | https://github.com/anchore/grype | [Canonical implementation repository and scope][grype-e1] | Retain verified implementation repository. |
| `documentation_url` | *absent* | https://oss.anchore.com/docs/guides/vulnerability/ | [Official vulnerability documentation][grype-e5] | Add directly checked official documentation for this record scope. |
| `categories` | application-cloud-security | application-cloud-security | [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `subcategories` | Application Security (SAST, DAST, SCA) &amp; Vulnerability Scanning | Vulnerability scanning | [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `roles` | devsecops-engineer<br>cloud-security-engineer | devsecops-engineer<br>cloud-security-engineer | [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `lifecycle_stages` | test<br>secure | test<br>secure | [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `use_when` | You want a fast, offline-capable CVE scanner that pairs with Syft SBOMs. | You need known-vulnerability matching for supported image/filesystem packages or an existing SBOM, including Syft-generated SBOMs, with a suitable vulnerability database. | [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6], [Implementation software licence][grype-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `avoid_when` | You need a single tool covering IaC + secrets + vulnerabilities (use Trivy). | You expect identical coverage to another scanner, application penetration testing, or vulnerability matches without a suitable database and supported package metadata. | [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6], [Implementation software licence][grype-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `deployment_models` | `[]` | self-hosted | [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | Record documented local/CI/server/controller self-hosted execution; external services are integrations or separate products. |
| `license_model` | oss | oss | [Implementation software licence][grype-e2] | Reviewed; retained: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Implementation software licence][grype-e2] | Changed: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Scanner scope, Syft relationship and commercial support][grype-e6] | Add true for explicitly documented related commercial support/product; reviewed software licence and self-hosted execution remain separate. |
| `maturity` | unknown | established | [Maintained release history][grype-e3], [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | Editorial established judgement from maintained releases/specifications, documented operations and governance, with feature/component limits stated above. |
| `status` | needs-review | active | [Maintained release history][grype-e3], [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical implementation repository and scope][grype-e1], [Maintained release history][grype-e3] | GitHub API independently reports archived=false; lifecycle follows release/maintenance evidence. |
| `alternatives` | `[]` | `[]` | [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `tags` | `[]` | `[]` | [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical implementation repository and scope][grype-e1], [Implementation software licence][grype-e2], [Maintained release history][grype-e3], [Official Anchore OSS site and tool identities][grype-e4], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | Requested Wave 9 batch marker 2026-10-07, changed only for these ten; execution on 2026-10-08 is disclosed above. |
| `sources` | legacy:6_Security/README.md#L28<br>legacy:devopstools_final.md#L868 | legacy:6_Security/README.md#L28<br>legacy:devopstools_final.md#L868<br>https://github.com/anchore/grype<br>https://github.com/anchore/grype/blob/main/LICENSE<br>https://github.com/anchore/grype/releases<br>https://oss.anchore.com/<br>https://oss.anchore.com/docs/guides/vulnerability/<br>https://github.com/anchore/grype/blob/main/README.md | [Canonical implementation repository and scope][grype-e1], [Implementation software licence][grype-e2], [Maintained release history][grype-e3], [Official Anchore OSS site and tool identities][grype-e4], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | Preserve all legacy sources and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][grype-e3], [Canonical implementation repository and scope][grype-e1], [Official vulnerability documentation][grype-e5], [Scanner scope, Syft relationship and commercial support][grype-e6] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `official_url`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[grype-e1]: https://github.com/anchore/grype
[grype-e2]: https://github.com/anchore/grype/blob/main/LICENSE
[grype-e3]: https://github.com/anchore/grype/releases
[grype-e4]: https://oss.anchore.com/
[grype-e5]: https://oss.anchore.com/docs/guides/vulnerability/
[grype-e6]: https://github.com/anchore/grype/blob/main/README.md

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/anchore/grype) (`archived: false`).

### gitleaks

**Identity boundary:** Gitleaks is the local/CI secret-scanning CLI for Git history, directories and stdin. Pre-commit and GitHub Action integrations are distinct execution wrappers; it is not GitHub Secret Scanning or another hosted triage service.

**Licence boundary:** MIT is verified from the actual master/LICENSE. Any organization licence-key requirement for the separate GitHub Action is not a replacement licence for the upstream CLI.

**Product/service boundary:** Self-hosted describes local/CI execution. No managed triage/revocation service is included and no blanket commercial_offering boolean is inferred from Action licence-key instructions.

**Repository boundary:** Retain gitleaks/gitleaks and official gitleaks.io; its default branch is master. Add its actual master/README.md as CLI documentation rather than a hosted-service page.

**Governance:** Official site says maintained by Truffle Security; upstream README documents the maintainer development focus. This does not establish a hosted product identity or foundation status.

**Maturity:** Established follows maintained releases since a 2018 repository origin, documented configurable scanning and pre-commit/CI workflows. Feature freeze is a lifecycle qualification, not a return to experimental maturity.

**Lifecycle:** Non-archived repository with 2026-09-30 activity and v8.30.1 (2026-03-21). Current README explicitly declares feature-complete status, no new features and future security-patch releases, with new development focused on Betterleaks. Retain active as qualified security maintenance, not ongoing feature development; no project retirement is asserted.

**Unresolved questions / limits:** None blocking CLI identity. Security-patch maintenance is narrower than feature development, and Action/service terms must be checked separately.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical implementation repository and scope][gitleaks-e1], [Implementation software licence][gitleaks-e2], [Maintained release history][gitleaks-e3], [Official project site and Action boundary][gitleaks-e4], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | gitleaks | gitleaks | [Canonical implementation repository and scope][gitleaks-e1] | Preserve stable catalogue ID and provenance; no duplicate. |
| `name` | Gitleaks | Gitleaks | [Canonical implementation repository and scope][gitleaks-e1], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Detect hardcoded secrets in code. | MIT-licensed CLI detecting secrets in Git history, files and standard input for local, pre-commit and CI use; upstream is feature-complete with future releases limited to security patches, distinct from hosted secret-scanning services. | [Canonical implementation repository and scope][gitleaks-e1], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://gitleaks.io | https://gitleaks.io | [Canonical implementation repository and scope][gitleaks-e1], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5] | Reviewed; retained: upstream-declared official entry point; any former pointer remains in sources. |
| `repository_url` | https://github.com/gitleaks/gitleaks | https://github.com/gitleaks/gitleaks | [Canonical implementation repository and scope][gitleaks-e1] | Retain verified implementation repository. |
| `documentation_url` | *absent* | https://github.com/gitleaks/gitleaks/blob/master/README.md | [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5] | Add directly checked official documentation for this record scope. |
| `categories` | application-cloud-security | application-cloud-security | [Canonical implementation repository and scope][gitleaks-e1], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `subcategories` | Application Security (SAST, DAST, SCA) &amp; Vulnerability Scanning | Secret scanning | [Canonical implementation repository and scope][gitleaks-e1], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `roles` | devsecops-engineer<br>cloud-security-engineer | devsecops-engineer<br>cloud-security-engineer | [Canonical implementation repository and scope][gitleaks-e1], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `lifecycle_stages` | test<br>secure | develop<br>test<br>secure | [Canonical implementation repository and scope][gitleaks-e1], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `use_when` | As a fast, CI-friendly secret scanner for Git history. | You need configurable secret detection in Git history/diffs, directories or standard input, integrated into local pre-commit or CI checks. | [Canonical implementation repository and scope][gitleaks-e1], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5], [Implementation software licence][gitleaks-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `avoid_when` | You need a managed platform with triage workflows (consider TruffleHog Enterprise or Snyk). | You require hosted triage and credential revocation from the CLI itself, or ongoing new CLI features beyond upstream security-patch maintenance. | [Canonical implementation repository and scope][gitleaks-e1], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5], [Implementation software licence][gitleaks-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `deployment_models` | `[]` | self-hosted | [Canonical implementation repository and scope][gitleaks-e1], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5] | Record documented local/CI/server/controller self-hosted execution; external services are integrations or separate products. |
| `license_model` | oss | oss | [Implementation software licence][gitleaks-e2] | Reviewed; retained: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `license_spdx` | *absent* | MIT | [Implementation software licence][gitleaks-e2] | Changed: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Canonical implementation repository and scope][gitleaks-e1] | Leave optional field absent; no denial of all third-party businesses is implied. |
| `maturity` | unknown | established | [Maintained release history][gitleaks-e3], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5], [Canonical implementation repository and scope][gitleaks-e1] | Editorial established judgement from maintained releases/specifications, documented operations and governance, with feature/component limits stated above. |
| `status` | needs-review | active | [Maintained release history][gitleaks-e3], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5], [Canonical implementation repository and scope][gitleaks-e1] | CLEAR REVIEW: active maintenance with resolved material boundaries; status/flag remain consistent. Gitleaks maintenance is explicitly security-patch-only. |
| `repository_archived` | *absent* | `false` | [Canonical implementation repository and scope][gitleaks-e1], [Maintained release history][gitleaks-e3], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5] | GitHub API independently reports archived=false; lifecycle follows release/maintenance evidence. |
| `alternatives` | `[]` | `[]` | [Canonical implementation repository and scope][gitleaks-e1], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `tags` | `[]` | `[]` | [Canonical implementation repository and scope][gitleaks-e1], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical implementation repository and scope][gitleaks-e1], [Implementation software licence][gitleaks-e2], [Maintained release history][gitleaks-e3], [Official project site and Action boundary][gitleaks-e4], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5] | Requested Wave 9 batch marker 2026-10-07, changed only for these ten; execution on 2026-10-08 is disclosed above. |
| `sources` | legacy:6_Security/README.md#L27<br>legacy:devopstools_final.md#L865 | legacy:6_Security/README.md#L27<br>legacy:devopstools_final.md#L865<br>https://github.com/gitleaks/gitleaks<br>https://github.com/gitleaks/gitleaks/blob/master/LICENSE<br>https://github.com/gitleaks/gitleaks/releases<br>https://gitleaks.io/<br>https://github.com/gitleaks/gitleaks/blob/master/README.md | [Canonical implementation repository and scope][gitleaks-e1], [Implementation software licence][gitleaks-e2], [Maintained release history][gitleaks-e3], [Official project site and Action boundary][gitleaks-e4], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5] | Preserve all legacy sources and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][gitleaks-e3], [Official CLI documentation and feature-complete lifecycle notice][gitleaks-e5], [Canonical implementation repository and scope][gitleaks-e1] | CLEAR REVIEW: active maintenance with resolved material boundaries; status/flag remain consistent. Gitleaks maintenance is explicitly security-patch-only. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[gitleaks-e1]: https://github.com/gitleaks/gitleaks
[gitleaks-e2]: https://github.com/gitleaks/gitleaks/blob/master/LICENSE
[gitleaks-e3]: https://github.com/gitleaks/gitleaks/releases
[gitleaks-e4]: https://gitleaks.io/
[gitleaks-e5]: https://github.com/gitleaks/gitleaks/blob/master/README.md

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/gitleaks/gitleaks) (`archived: false`).

### sops

**Identity boundary:** SOPS edits encrypted configuration files with supported recipient/key providers. GitOps/IaC can store those files in version control. It is not a secret-serving backend, dynamic credential issuer, cloud KMS or External Secrets operator.

**Licence boundary:** MPL-2.0 is verified from the current getsops/sops LICENSE, not inferred from historical Mozilla sponsorship or CNCF affiliation.

**Product/service boundary:** The editor executes self-hosted. Cloud KMS, Vault/OpenBao transit and other providers remain separate key-service integrations; no service offering is assigned to SOPS.

**Repository boundary:** Use getsops/sops, not an obsolete Mozilla repository. Existing official getsops.io remains; add official docs and retain historical provenance.

**Governance:** Upstream README.rst states Mozilla launched SOPS in 2015 and donated it to CNCF in 2023, with new maintainers. CNCF directly records Sandbox entry on 2023-05-17; current getsops community MAINTAINERS identifies maintainers. Do not imply current Mozilla ownership.

**Maturity:** Established follows long maintained file-encryption releases, documented multi-provider workflows and current maintainer continuity, independently of CNCF Sandbox status.

**Lifecycle:** Non-archived getsops/sops with 2026-10-05 activity and v3.13.3 (2026-07-23). Current documentation and maintained release history support active lifecycle.

**Unresolved questions / limits:** None blocking editor identity. File format/key-provider support and authorization/decryption delivery must be configured; the editor does not provide a general secrets backend.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical implementation repository and scope][sops-e1], [Implementation software licence][sops-e2], [Maintained release history][sops-e3], [Official encrypted-file documentation][sops-e4], [Mozilla history, current maintainers and CNCF donation][sops-e5], [Current maintainer governance list][sops-e6], [CNCF foundation status][sops-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | sops | sops | [Canonical implementation repository and scope][sops-e1] | Preserve stable catalogue ID and provenance; no duplicate. |
| `name` | SOPS | SOPS | [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Secrets management tool for GitOps/IaC (encrypt YAML/JSON/env). | SOPS encrypted-file editor for YAML, JSON, ENV, INI and binary files, using age, PGP or supported KMS/key services; GitOps/IaC file encryption is distinct from a secrets backend such as Vault. | [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://getsops.io | https://getsops.io | [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4] | Reviewed; retained: upstream-declared official entry point; any former pointer remains in sources. |
| `repository_url` | https://github.com/getsops/sops | https://github.com/getsops/sops | [Canonical implementation repository and scope][sops-e1] | Retain verified implementation repository. |
| `documentation_url` | *absent* | https://getsops.io/docs/ | [Official encrypted-file documentation][sops-e4] | Add directly checked official documentation for this record scope. |
| `categories` | iam-secrets-certificates | iam-secrets-certificates | [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `subcategories` | Secret Management | Secret Management | [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `roles` | cloud-engineer<br>devsecops-engineer<br>cloud-security-engineer | cloud-engineer<br>devsecops-engineer<br>cloud-security-engineer | [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `lifecycle_stages` | operate<br>secure | deploy<br>operate<br>secure | [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `use_when` | Encrypt secrets in Git alongside your IaC for GitOps workflows. | You need encrypted configuration files in GitOps or IaC workflows while retaining supported structured-file keys for review and controlling decryption through selected recipients/key services. | [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4], [Implementation software licence][sops-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `avoid_when` | You need dynamic secrets or centralized access control (use Vault). | You need SOPS itself to serve a secrets API, issue dynamic credentials or act as a Kubernetes External Secrets operator; KMS and Vault integrations provide key services separately. | [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4], [Implementation software licence][sops-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `deployment_models` | `[]` | self-hosted | [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4] | Record documented local/CI/server/controller self-hosted execution; external services are integrations or separate products. |
| `license_model` | oss | oss | [Implementation software licence][sops-e2] | Reviewed; retained: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `license_spdx` | *absent* | MPL-2.0 | [Implementation software licence][sops-e2] | Changed: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Canonical implementation repository and scope][sops-e1] | Leave optional field absent; no denial of all third-party businesses is implied. |
| `maturity` | unknown | established | [Maintained release history][sops-e3], [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4], [Mozilla history, current maintainers and CNCF donation][sops-e5], [Current maintainer governance list][sops-e6], [CNCF foundation status][sops-e7] | Editorial established judgement from maintained releases/specifications, documented operations and governance, with feature/component limits stated above. |
| `status` | needs-review | active | [Maintained release history][sops-e3], [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical implementation repository and scope][sops-e1], [Maintained release history][sops-e3] | GitHub API independently reports archived=false; lifecycle follows release/maintenance evidence. |
| `alternatives` | `[]` | `[]` | [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `tags` | `[]` | `[]` | [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical implementation repository and scope][sops-e1], [Implementation software licence][sops-e2], [Maintained release history][sops-e3], [Official encrypted-file documentation][sops-e4], [Mozilla history, current maintainers and CNCF donation][sops-e5], [Current maintainer governance list][sops-e6], [CNCF foundation status][sops-e7] | Requested Wave 9 batch marker 2026-10-07, changed only for these ten; execution on 2026-10-08 is disclosed above. |
| `sources` | legacy:6_Security/README.md#L94<br>legacy:devopstools_final.md#L983 | legacy:6_Security/README.md#L94<br>legacy:devopstools_final.md#L983<br>https://github.com/getsops/sops<br>https://github.com/getsops/sops/blob/main/LICENSE<br>https://github.com/getsops/sops/releases<br>https://getsops.io/docs/<br>https://github.com/getsops/sops/blob/main/README.rst<br>https://github.com/getsops/community/blob/main/MAINTAINERS.md<br>https://www.cncf.io/projects/sops/ | [Canonical implementation repository and scope][sops-e1], [Implementation software licence][sops-e2], [Maintained release history][sops-e3], [Official encrypted-file documentation][sops-e4], [Mozilla history, current maintainers and CNCF donation][sops-e5], [Current maintainer governance list][sops-e6], [CNCF foundation status][sops-e7] | Preserve all legacy sources and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][sops-e3], [Canonical implementation repository and scope][sops-e1], [Official encrypted-file documentation][sops-e4] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `documentation_url`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[sops-e1]: https://github.com/getsops/sops
[sops-e2]: https://github.com/getsops/sops/blob/main/LICENSE
[sops-e3]: https://github.com/getsops/sops/releases
[sops-e4]: https://getsops.io/docs/
[sops-e5]: https://github.com/getsops/sops/blob/main/README.rst
[sops-e6]: https://github.com/getsops/community/blob/main/MAINTAINERS.md
[sops-e7]: https://www.cncf.io/projects/sops/

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/getsops/sops) (`archived: false`).

### keycloak

**Identity boundary:** Keycloak remains the upstream IAM/SSO server for applications/services, OIDC/OAuth 2.0/SAML and identity federation. It is not merely Kubernetes IAM and not an unrelated OIDC proxy.

**Licence boundary:** Apache-2.0 is verified from upstream LICENSE.txt. Red Hat build packaging, commercial support and any managed IAM services must be evaluated separately; this grant is scoped to upstream source.

**Product/service boundary:** Self-hosted is the upstream server deployment. Red Hat explicitly describes its build as a commercial offering based on the upstream community project, supporting related commercial_offering=true without changing the record to a vendor package or managed service.

**Repository boundary:** Retain keycloak/keycloak and keycloak.org. Add the upstream documentation index; vendor-build documentation is evidence of a separate boundary, not its canonical documentation URL.

**Governance:** CNCF directly records Incubating entry on 2023-04-10. Upstream GOVERNANCE defines maintainer voting/authority; MAINTAINERS lists multiple affiliations, including IBM, Bosch and Hitachi. Do not describe the present project as exclusively owned by Red Hat.

**Maturity:** Established follows years of maintained server releases, documented production operations/protocols and explicit upstream maintainer governance, independently of CNCF incubation.

**Lifecycle:** Non-archived upstream with 2026-10-07 activity and stable 26.8.0 (2026-10-01). Current production/administration guides and release history establish active lifecycle independently of vendor support schedules.

**Unresolved questions / limits:** None blocking upstream identity. Feature/version compatibility, production operations and vendor support entitlements require separately selected deployment and packaging.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical implementation repository and scope][keycloak-e1], [Implementation software licence][keycloak-e2], [Maintained release history][keycloak-e3], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5], [Project governance][keycloak-e6], [Current upstream maintainer affiliations][keycloak-e7], [CNCF foundation status][keycloak-e8], [Red Hat build packaging boundary][keycloak-e9], [Related commercial offering and separate support policy][keycloak-e10].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | keycloak | keycloak | [Canonical implementation repository and scope][keycloak-e1], [Current upstream maintainer affiliations][keycloak-e7] | Preserve stable catalogue ID and provenance; no duplicate. |
| `name` | Keycloak | Keycloak | [Canonical implementation repository and scope][keycloak-e1], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Open source identity and access management. | Upstream open-source identity and access-management server providing SSO, identity federation and OpenID Connect, OAuth 2.0 and SAML for applications and services; Red Hat build packaging and managed IAM services are separate. | [Canonical implementation repository and scope][keycloak-e1], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://www.keycloak.org | https://www.keycloak.org | [Canonical implementation repository and scope][keycloak-e1], [Current upstream maintainer affiliations][keycloak-e7], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5] | Reviewed; retained: upstream-declared official entry point; any former pointer remains in sources. |
| `repository_url` | https://github.com/keycloak/keycloak | https://github.com/keycloak/keycloak | [Canonical implementation repository and scope][keycloak-e1], [Current upstream maintainer affiliations][keycloak-e7] | Retain verified implementation repository. |
| `documentation_url` | *absent* | https://www.keycloak.org/documentation | [Official IAM documentation][keycloak-e4] | Add directly checked official documentation for this record scope. |
| `categories` | iam-secrets-certificates | iam-secrets-certificates | [Canonical implementation repository and scope][keycloak-e1], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `subcategories` | Identity &amp; Access Management | Identity &amp; Access Management | [Canonical implementation repository and scope][keycloak-e1], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `roles` | cloud-engineer<br>devsecops-engineer<br>cloud-security-engineer | cloud-engineer<br>devsecops-engineer<br>cloud-security-engineer | [Canonical implementation repository and scope][keycloak-e1], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `lifecycle_stages` | operate<br>secure | operate<br>secure | [Canonical implementation repository and scope][keycloak-e1], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `use_when` | Self-hosted SSO/OIDC/SAML with user federation and fine-grained authorization. | You need a self-hosted IAM/SSO server for applications and services using supported OIDC, OAuth 2.0 or SAML integrations and identity federation. | [Canonical implementation repository and scope][keycloak-e1], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5], [Implementation software licence][keycloak-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `avoid_when` | You only need IdP federation without user management (use Dex) or want a managed service. | You require a managed IAM service from upstream itself, vendor-product support terms inherited automatically, or only a narrow reverse-proxy authentication layer. | [Canonical implementation repository and scope][keycloak-e1], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5], [Implementation software licence][keycloak-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `deployment_models` | `[]` | self-hosted | [Canonical implementation repository and scope][keycloak-e1], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5] | Record documented local/CI/server/controller self-hosted execution; external services are integrations or separate products. |
| `license_model` | oss | oss | [Implementation software licence][keycloak-e2] | Reviewed; retained: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Implementation software licence][keycloak-e2] | Changed: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Red Hat build packaging boundary][keycloak-e9], [Related commercial offering and separate support policy][keycloak-e10] | Add true for explicitly documented related commercial support/product; reviewed software licence and self-hosted execution remain separate. |
| `maturity` | unknown | established | [Maintained release history][keycloak-e3], [Canonical implementation repository and scope][keycloak-e1], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5], [Project governance][keycloak-e6], [Current upstream maintainer affiliations][keycloak-e7], [CNCF foundation status][keycloak-e8] | Editorial established judgement from maintained releases/specifications, documented operations and governance, with feature/component limits stated above. |
| `status` | needs-review | active | [Maintained release history][keycloak-e3], [Canonical implementation repository and scope][keycloak-e1], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical implementation repository and scope][keycloak-e1], [Current upstream maintainer affiliations][keycloak-e7], [Maintained release history][keycloak-e3] | GitHub API independently reports archived=false; lifecycle follows release/maintenance evidence. |
| `alternatives` | `[]` | `[]` | [Canonical implementation repository and scope][keycloak-e1], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `tags` | `[]` | `[]` | [Canonical implementation repository and scope][keycloak-e1], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical implementation repository and scope][keycloak-e1], [Implementation software licence][keycloak-e2], [Maintained release history][keycloak-e3], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5], [Project governance][keycloak-e6], [Current upstream maintainer affiliations][keycloak-e7], [CNCF foundation status][keycloak-e8], [Red Hat build packaging boundary][keycloak-e9], [Related commercial offering and separate support policy][keycloak-e10] | Requested Wave 9 batch marker 2026-10-07, changed only for these ten; execution on 2026-10-08 is disclosed above. |
| `sources` | legacy:6_Security/README.md#L111<br>legacy:devopstools_final.md#L1003 | legacy:6_Security/README.md#L111<br>legacy:devopstools_final.md#L1003<br>https://github.com/keycloak/keycloak<br>https://github.com/keycloak/keycloak/blob/main/LICENSE.txt<br>https://github.com/keycloak/keycloak/releases<br>https://www.keycloak.org/documentation<br>https://www.keycloak.org/docs/latest/server_admin/index.html<br>https://github.com/keycloak/keycloak/blob/main/GOVERNANCE.md<br>https://github.com/keycloak/keycloak/blob/main/MAINTAINERS.md<br>https://www.cncf.io/projects/keycloak/<br>https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/release_notes/overview<br>https://access.redhat.com/support/policy/updates/red_hat_build_of_keycloak_notes | [Canonical implementation repository and scope][keycloak-e1], [Implementation software licence][keycloak-e2], [Maintained release history][keycloak-e3], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5], [Project governance][keycloak-e6], [Current upstream maintainer affiliations][keycloak-e7], [CNCF foundation status][keycloak-e8], [Red Hat build packaging boundary][keycloak-e9], [Related commercial offering and separate support policy][keycloak-e10] | Preserve all legacy sources and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][keycloak-e3], [Canonical implementation repository and scope][keycloak-e1], [Official IAM documentation][keycloak-e4], [Protocol and administration documentation][keycloak-e5] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[keycloak-e1]: https://github.com/keycloak/keycloak
[keycloak-e2]: https://github.com/keycloak/keycloak/blob/main/LICENSE.txt
[keycloak-e3]: https://github.com/keycloak/keycloak/releases
[keycloak-e4]: https://www.keycloak.org/documentation
[keycloak-e5]: https://www.keycloak.org/docs/latest/server_admin/index.html
[keycloak-e6]: https://github.com/keycloak/keycloak/blob/main/GOVERNANCE.md
[keycloak-e7]: https://github.com/keycloak/keycloak/blob/main/MAINTAINERS.md
[keycloak-e8]: https://www.cncf.io/projects/keycloak/
[keycloak-e9]: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.4/html/release_notes/overview
[keycloak-e10]: https://access.redhat.com/support/policy/updates/red_hat_build_of_keycloak_notes

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/keycloak/keycloak) (`archived: false`).

### hashicorp-vault

**Identity boundary:** Explicitly scope the stable hashicorp-vault record to current Vault Community Edition source. Enterprise and HCP products remain related commercial offerings rather than one shared software grant. This is the secret-serving backend, distinct from SOPS encrypted-file editing.

**Licence boundary:** Retain source-available; assign BUSL-1.1 from current main/LICENSE, whose licensor is IBM. Its Additional Use Grant restricts competing paid hosted/embedded offerings and defines MPL-2.0 conversion four years per version. Historical v1.14.8/LICENSE is MPL-2.0, but v1.14.10/LICENSE is BUSL: do not blanket-label every 1.14 patch MPL. api/LICENSE and sdk/LICENSE separately remain MPL-2.0; plugins/dependencies require their own grants. Community BUSL does not cover Enterprise object code or HCP service terms.

**Product/service boundary:** Enterprise documentation requires a commercial licence/EULA; HCP Vault Dedicated uses Enterprise binaries and service-specific operation. Set commercial_offering=true for these related offerings, while reviewed Community execution is self-hosted.

**Repository boundary:** Retain hashicorp/vault. Current upstream README explicitly declares developer.hashicorp.com/vault as its website; add its docs and preserve former vaultproject.io in sources. This is an identity/documentation correction, not a redirect-only bulk replacement.

**Governance:** HashiCorp upstream project and IBM licence notice provide current vendor/licensor context. No foundation ownership or licence of separately packaged products is inferred.

**Maturity:** Established follows maintained releases and documented secrets, dynamic-credential and encryption operations since the 2015 repository origin; source-available licensing does not imply experimental maturity.

**Lifecycle:** Non-archived upstream with 2026-10-07 activity and stable v2.1.2 (2026-10-07). Maintained operational docs and releases support active Community lifecycle separately from Enterprise/HCP support contracts.

**Unresolved questions / limits:** None blocking current Community licence. Additional Use Grant, per-version conversion dates, separately licensed modules and Enterprise/HCP/plugin terms must be assessed for the actual use case.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical implementation repository and scope][hashicorp-vault-e1], [Implementation software licence][hashicorp-vault-e2], [Maintained release history][hashicorp-vault-e3], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault product entry point][hashicorp-vault-e5], [Official Vault documentation][hashicorp-vault-e6], [Separately licensed API module][hashicorp-vault-e7], [Separately licensed SDK module][hashicorp-vault-e8], [Historical MPL release licence][hashicorp-vault-e9], [Later historical patch BUSL licence][hashicorp-vault-e10], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12], [HCP Vault hosted product boundary][hashicorp-vault-e13].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | hashicorp-vault | hashicorp-vault | [Canonical implementation repository and scope][hashicorp-vault-e1] | Preserve stable catalogue ID and provenance; no duplicate. |
| `name` | HashiCorp Vault | HashiCorp Vault Community Edition | [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | Changed: documented capability/identity; the scoped boundary above applies. |
| `summary` | Secure secret storage and access. | Source-available Vault Community Edition for secrets storage, dynamic credentials and encryption services under BUSL-1.1; Vault Enterprise and HCP Vault offerings have separate commercial product terms. | [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://www.vaultproject.io | https://developer.hashicorp.com/vault | [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | Changed: upstream-declared official entry point; any former pointer remains in sources. |
| `repository_url` | https://github.com/hashicorp/vault | https://github.com/hashicorp/vault | [Canonical implementation repository and scope][hashicorp-vault-e1] | Retain verified implementation repository. |
| `documentation_url` | *absent* | https://developer.hashicorp.com/vault/docs | [Official Vault documentation][hashicorp-vault-e6] | Add directly checked official documentation for this record scope. |
| `categories` | iam-secrets-certificates | iam-secrets-certificates | [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `subcategories` | Secret Management | Secret Management | [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `roles` | cloud-engineer<br>devsecops-engineer<br>cloud-security-engineer | cloud-engineer<br>devsecops-engineer<br>cloud-security-engineer | [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `lifecycle_stages` | operate<br>secure | operate<br>secure | [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `use_when` | Centralized, multi-cloud secrets with dynamic credentials and encryption-as-a-service. | You need a self-hosted secrets backend, dynamic credentials or encryption services and can comply with the applicable Community Edition BUSL grant, or choose separately licensed Enterprise/hosted offerings. | [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12], [Implementation software licence][hashicorp-vault-e2], [Separately licensed API module][hashicorp-vault-e7], [Separately licensed SDK module][hashicorp-vault-e8], [Historical MPL release licence][hashicorp-vault-e9], [Later historical patch BUSL licence][hashicorp-vault-e10] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `avoid_when` | For simple single-cloud setups where the native secrets manager suffices. | You require the current Community source to have an OSI open-source grant or expect its BUSL licence to cover Enterprise, HCP services or every plugin/SDK; evaluate each product/component grant separately. | [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12], [Implementation software licence][hashicorp-vault-e2], [Separately licensed API module][hashicorp-vault-e7], [Separately licensed SDK module][hashicorp-vault-e8], [Historical MPL release licence][hashicorp-vault-e9], [Later historical patch BUSL licence][hashicorp-vault-e10] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `deployment_models` | `[]` | self-hosted | [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | Record documented local/CI/server/controller self-hosted execution; external services are integrations or separate products. |
| `license_model` | source-available | source-available | [Implementation software licence][hashicorp-vault-e2], [Separately licensed API module][hashicorp-vault-e7], [Separately licensed SDK module][hashicorp-vault-e8], [Historical MPL release licence][hashicorp-vault-e9], [Later historical patch BUSL licence][hashicorp-vault-e10], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | Reviewed; retained: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `license_spdx` | *absent* | BUSL-1.1 | [Implementation software licence][hashicorp-vault-e2], [Separately licensed API module][hashicorp-vault-e7], [Separately licensed SDK module][hashicorp-vault-e8], [Historical MPL release licence][hashicorp-vault-e9], [Later historical patch BUSL licence][hashicorp-vault-e10], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | Changed: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12], [HCP Vault hosted product boundary][hashicorp-vault-e13] | Add true for explicitly documented related commercial support/product; reviewed software licence and self-hosted execution remain separate. |
| `maturity` | unknown | established | [Maintained release history][hashicorp-vault-e3], [Historical MPL release licence][hashicorp-vault-e9], [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | Editorial established judgement from maintained releases/specifications, documented operations and governance, with feature/component limits stated above. |
| `status` | needs-review | active | [Maintained release history][hashicorp-vault-e3], [Historical MPL release licence][hashicorp-vault-e9], [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical implementation repository and scope][hashicorp-vault-e1], [Maintained release history][hashicorp-vault-e3], [Historical MPL release licence][hashicorp-vault-e9] | GitHub API independently reports archived=false; lifecycle follows release/maintenance evidence. |
| `alternatives` | `[]` | `[]` | [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `tags` | `[]` | `[]` | [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical implementation repository and scope][hashicorp-vault-e1], [Implementation software licence][hashicorp-vault-e2], [Maintained release history][hashicorp-vault-e3], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault product entry point][hashicorp-vault-e5], [Official Vault documentation][hashicorp-vault-e6], [Separately licensed API module][hashicorp-vault-e7], [Separately licensed SDK module][hashicorp-vault-e8], [Historical MPL release licence][hashicorp-vault-e9], [Later historical patch BUSL licence][hashicorp-vault-e10], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12], [HCP Vault hosted product boundary][hashicorp-vault-e13] | Requested Wave 9 batch marker 2026-10-07, changed only for these ten; execution on 2026-10-08 is disclosed above. |
| `sources` | legacy:6_Security/README.md#L91<br>legacy:devopstools_final.md#L978 | legacy:6_Security/README.md#L91<br>legacy:devopstools_final.md#L978<br>https://github.com/hashicorp/vault<br>https://github.com/hashicorp/vault/blob/main/LICENSE<br>https://github.com/hashicorp/vault/releases<br>https://github.com/hashicorp/vault/blob/main/README.md<br>https://developer.hashicorp.com/vault<br>https://developer.hashicorp.com/vault/docs<br>https://github.com/hashicorp/vault/blob/main/api/LICENSE<br>https://github.com/hashicorp/vault/blob/main/sdk/LICENSE<br>https://github.com/hashicorp/vault/blob/v1.14.8/LICENSE<br>https://github.com/hashicorp/vault/blob/v1.14.10/LICENSE<br>https://developer.hashicorp.com/vault/docs/enterprise<br>https://developer.hashicorp.com/vault/docs/license<br>https://developer.hashicorp.com/vault/cloud<br>https://www.vaultproject.io | [Canonical implementation repository and scope][hashicorp-vault-e1], [Implementation software licence][hashicorp-vault-e2], [Maintained release history][hashicorp-vault-e3], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault product entry point][hashicorp-vault-e5], [Official Vault documentation][hashicorp-vault-e6], [Separately licensed API module][hashicorp-vault-e7], [Separately licensed SDK module][hashicorp-vault-e8], [Historical MPL release licence][hashicorp-vault-e9], [Later historical patch BUSL licence][hashicorp-vault-e10], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12], [HCP Vault hosted product boundary][hashicorp-vault-e13] | Preserve all legacy sources and append directly checked primary evidence. Preserve the former official pointer https://www.vaultproject.io as provenance. |
| `needs_review` | `true` | `false` | [Maintained release history][hashicorp-vault-e3], [Historical MPL release licence][hashicorp-vault-e9], [Canonical implementation repository and scope][hashicorp-vault-e1], [Official current Community product identity and documentation links][hashicorp-vault-e4], [Official Vault documentation][hashicorp-vault-e6], [Enterprise commercial product documentation][hashicorp-vault-e11], [Enterprise licence and EULA documentation][hashicorp-vault-e12] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `name`, `summary`, `official_url`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[hashicorp-vault-e1]: https://github.com/hashicorp/vault
[hashicorp-vault-e2]: https://github.com/hashicorp/vault/blob/main/LICENSE
[hashicorp-vault-e3]: https://github.com/hashicorp/vault/releases
[hashicorp-vault-e4]: https://github.com/hashicorp/vault/blob/main/README.md
[hashicorp-vault-e5]: https://developer.hashicorp.com/vault
[hashicorp-vault-e6]: https://developer.hashicorp.com/vault/docs
[hashicorp-vault-e7]: https://github.com/hashicorp/vault/blob/main/api/LICENSE
[hashicorp-vault-e8]: https://github.com/hashicorp/vault/blob/main/sdk/LICENSE
[hashicorp-vault-e9]: https://github.com/hashicorp/vault/blob/v1.14.8/LICENSE
[hashicorp-vault-e10]: https://github.com/hashicorp/vault/blob/v1.14.10/LICENSE
[hashicorp-vault-e11]: https://developer.hashicorp.com/vault/docs/enterprise
[hashicorp-vault-e12]: https://developer.hashicorp.com/vault/docs/license
[hashicorp-vault-e13]: https://developer.hashicorp.com/vault/cloud

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/hashicorp/vault) (`archived: false`).

### cert-manager

**Identity boundary:** cert-manager is the Kubernetes controller/resource workflow for X.509 issuance and renewal through configured issuers. ACME/Let's Encrypt, certbot, external CA vendors and general secrets backends remain distinct. Retain Kubernetes add-ons as the existing primary taxonomy placement; refine the certificate subcategory.

**Licence boundary:** Apache-2.0 follows the actual master/LICENSE, independently of issuer/vendor terms or CNCF hosting.

**Product/service boundary:** The controller is self-hosted in Kubernetes; external issuers/PKI services are integrations with their own operation and terms. No commercial service is assigned to the controller.

**Repository boundary:** Retain cert-manager/cert-manager (default master), not certbot or an issuer vendor. Add the official cert-manager docs index.

**Governance:** CNCF directly records graduation on 2024-09-29. Community governance/maintainers define project roles and responsibilities. Graduation is neither software licence evidence nor an automatic catalogue maturity rule.

**Maturity:** Established follows maintained stable controller releases and documented certificate/issuer operations under current governance, independently of graduation. Not every feature or Go module carries the same stability promise.

**Lifecycle:** Non-archived repository with 2026-10-07 activity and maintained stable v1.20.4 (2026-09-16) and v1.21.2 (2026-09-11). Release and operational documentation support active lifecycle; Go-module/feature compatibility remains separately bounded.

**Unresolved questions / limits:** None blocking controller identity. Issuer credentials, CA policies, Kubernetes compatibility and feature/module support must be checked for the deployed version.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical implementation repository and scope][cert-manager-e1], [Implementation software licence][cert-manager-e2], [Maintained release history][cert-manager-e3], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5], [Current project governance][cert-manager-e6], [Current maintainer governance list][cert-manager-e7], [CNCF foundation status][cert-manager-e8].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | cert-manager | cert-manager | [Canonical implementation repository and scope][cert-manager-e1] | Preserve stable catalogue ID and provenance; no duplicate. |
| `name` | cert-manager | cert-manager | [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | X.509 certificate management for Kubernetes. | Kubernetes X.509 certificate-management controller issuing and renewing certificates through configured issuers such as ACME and external CAs; it is distinct from Let&#x27;s Encrypt, certbot and general secrets backends. | [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://cert-manager.io | https://cert-manager.io | [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5] | Reviewed; retained: upstream-declared official entry point; any former pointer remains in sources. |
| `repository_url` | https://github.com/cert-manager/cert-manager | https://github.com/cert-manager/cert-manager | [Canonical implementation repository and scope][cert-manager-e1] | Retain verified implementation repository. |
| `documentation_url` | *absent* | https://cert-manager.io/docs/ | [Official certificate-management documentation][cert-manager-e4] | Add directly checked official documentation for this record scope. |
| `categories` | kubernetes-networking-storage-addons | kubernetes-networking-storage-addons | [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `subcategories` | Kubernetes Ecosystem &amp; Add-ons | Certificate management | [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `use_when` | You need automated TLS certificate issuance and renewal (Let&#x27;s Encrypt, Vault, etc.). | You need Kubernetes certificate resources with automated issuance and renewal through a configured ACME or other supported issuer. | [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5], [Implementation software licence][cert-manager-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `avoid_when` | Your ingress controller or service mesh already handles certificate lifecycle. | You need a general secrets backend, non-Kubernetes certbot workflow or expect the controller itself to be Let&#x27;s Encrypt or an external PKI vendor. | [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5], [Implementation software licence][cert-manager-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `deployment_models` | `[]` | self-hosted | [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5] | Record documented local/CI/server/controller self-hosted execution; external services are integrations or separate products. |
| `license_model` | oss | oss | [Implementation software licence][cert-manager-e2] | Reviewed; retained: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Implementation software licence][cert-manager-e2] | Changed: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Canonical implementation repository and scope][cert-manager-e1] | Leave optional field absent; no denial of all third-party businesses is implied. |
| `maturity` | unknown | established | [Maintained release history][cert-manager-e3], [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5], [Current project governance][cert-manager-e6], [Current maintainer governance list][cert-manager-e7], [CNCF foundation status][cert-manager-e8] | Editorial established judgement from maintained releases/specifications, documented operations and governance, with feature/component limits stated above. |
| `status` | needs-review | active | [Maintained release history][cert-manager-e3], [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical implementation repository and scope][cert-manager-e1], [Maintained release history][cert-manager-e3] | GitHub API independently reports archived=false; lifecycle follows release/maintenance evidence. |
| `alternatives` | `[]` | `[]` | [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `tags` | `[]` | `[]` | [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical implementation repository and scope][cert-manager-e1], [Implementation software licence][cert-manager-e2], [Maintained release history][cert-manager-e3], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5], [Current project governance][cert-manager-e6], [Current maintainer governance list][cert-manager-e7], [CNCF foundation status][cert-manager-e8] | Requested Wave 9 batch marker 2026-10-07, changed only for these ten; execution on 2026-10-08 is disclosed above. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L77<br>legacy:devopstools_final.md#L538 | legacy:4_Kubernetes-Containers/README.md#L77<br>legacy:devopstools_final.md#L538<br>https://github.com/cert-manager/cert-manager<br>https://github.com/cert-manager/cert-manager/blob/master/LICENSE<br>https://github.com/cert-manager/cert-manager/releases<br>https://cert-manager.io/docs/<br>https://cert-manager.io/docs/configuration/<br>https://github.com/cert-manager/community/blob/main/GOVERNANCE.md<br>https://github.com/cert-manager/community/blob/main/MAINTAINERS.md<br>https://www.cncf.io/projects/cert-manager/ | [Canonical implementation repository and scope][cert-manager-e1], [Implementation software licence][cert-manager-e2], [Maintained release history][cert-manager-e3], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5], [Current project governance][cert-manager-e6], [Current maintainer governance list][cert-manager-e7], [CNCF foundation status][cert-manager-e8] | Preserve all legacy sources and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][cert-manager-e3], [Canonical implementation repository and scope][cert-manager-e1], [Official certificate-management documentation][cert-manager-e4], [Issuer and ACME configuration documentation][cert-manager-e5] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[cert-manager-e1]: https://github.com/cert-manager/cert-manager
[cert-manager-e2]: https://github.com/cert-manager/cert-manager/blob/master/LICENSE
[cert-manager-e3]: https://github.com/cert-manager/cert-manager/releases
[cert-manager-e4]: https://cert-manager.io/docs/
[cert-manager-e5]: https://cert-manager.io/docs/configuration/
[cert-manager-e6]: https://github.com/cert-manager/community/blob/main/GOVERNANCE.md
[cert-manager-e7]: https://github.com/cert-manager/community/blob/main/MAINTAINERS.md
[cert-manager-e8]: https://www.cncf.io/projects/cert-manager/

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/cert-manager/cert-manager) (`archived: false`).

### kyverno

**Identity boundary:** The record represents the core Kubernetes policy engine, not OPA/Gatekeeper, Sigstore policy-controller or a signing CLI. Validation/mutation/generation/cleanup/image verification are documented; Kyverno JSON, Envoy and Chainsaw are separate upstream projects. Retain Kubernetes add-ons primary placement and refine the policy subcategory.

**Licence boundary:** Apache-2.0 is verified from kyverno/kyverno LICENSE. CNCF graduation does not supply a software grant or terms for external registries/signers.

**Product/service boundary:** Core policy-controller deployment is self-hosted. Artifact signing/key management and other ecosystem services are external; optional commercial_offering remains absent.

**Repository boundary:** Retain kyverno/kyverno, add official kyverno.io/docs. Do not replace it with a companion project or another admission controller.

**Governance:** Current CNCF primary page records graduation on 2026-03-16. Upstream README still says Incubating: disclose that publication discrepancy and prefer the current foundation record for foundation status. Community GOVERNANCE independently documents project contributor/maintainer authority.

**Maturity:** Established follows maintained releases, documented Kubernetes operation/policy enforcement and explicit community governance, independently of the 2026 graduation. Supported policy types and feature stability remain version-specific.

**Lifecycle:** Non-archived upstream with 2026-10-07 activity and stable v1.19.1 (2026-09-10). Current docs describe new policy types and mark legacy ClusterPolicy/CleanupPolicy types deprecated; that is not deprecation of Kyverno itself.

**Unresolved questions / limits:** None blocking core identity. Migration from deprecated policy types and trust/signing configuration must be checked separately; enforcement does not replace RBAC or API-server security.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical implementation repository and scope][kyverno-e1], [Implementation software licence][kyverno-e2], [Maintained release history][kyverno-e3], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5], [Project community governance][kyverno-e6], [Current CNCF foundation status][kyverno-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | kyverno | kyverno | [Canonical implementation repository and scope][kyverno-e1] | Preserve stable catalogue ID and provenance; no duplicate. |
| `name` | Kyverno | Kyverno | [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Kubernetes policy engine. | Kubernetes policy engine for validation, mutation, generation, cleanup and image verification with YAML/CEL policies; signing tools, OPA/Gatekeeper and other Kyverno subprojects remain separate. | [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://kyverno.io | https://kyverno.io | [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5] | Reviewed; retained: upstream-declared official entry point; any former pointer remains in sources. |
| `repository_url` | https://github.com/kyverno/kyverno | https://github.com/kyverno/kyverno | [Canonical implementation repository and scope][kyverno-e1] | Retain verified implementation repository. |
| `documentation_url` | *absent* | https://kyverno.io/docs/ | [Official policy documentation][kyverno-e4] | Add directly checked official documentation for this record scope. |
| `categories` | kubernetes-networking-storage-addons | kubernetes-networking-storage-addons | [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `subcategories` | Kubernetes Ecosystem &amp; Add-ons | Policy validation, mutation and verification | [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate<br>secure | [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `use_when` | You need Kubernetes-native policy enforcement without learning Rego (validate, mutate, generate). | You need Kubernetes policy validation, mutation, generation, cleanup or image verification using supported policy types, with signing and trust configuration supplied separately. | [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5], [Implementation software licence][kyverno-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `avoid_when` | You already have OPA Gatekeeper deployed and your team knows Rego. | You expect policy enforcement to replace Kubernetes RBAC/API-server security, generate artifact signatures itself or inherit every capability of OPA, Gatekeeper or companion Kyverno projects. | [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5], [Implementation software licence][kyverno-e2] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `deployment_models` | `[]` | self-hosted | [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5] | Record documented local/CI/server/controller self-hosted execution; external services are integrations or separate products. |
| `license_model` | oss | oss | [Implementation software licence][kyverno-e2] | Reviewed; retained: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Implementation software licence][kyverno-e2] | Changed: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Canonical implementation repository and scope][kyverno-e1] | Leave optional field absent; no denial of all third-party businesses is implied. |
| `maturity` | unknown | established | [Maintained release history][kyverno-e3], [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5], [Project community governance][kyverno-e6], [Current CNCF foundation status][kyverno-e7] | Editorial established judgement from maintained releases/specifications, documented operations and governance, with feature/component limits stated above. |
| `status` | needs-review | active | [Maintained release history][kyverno-e3], [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical implementation repository and scope][kyverno-e1], [Maintained release history][kyverno-e3] | GitHub API independently reports archived=false; lifecycle follows release/maintenance evidence. |
| `alternatives` | `[]` | `[]` | [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `tags` | `[]` | `[]` | [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical implementation repository and scope][kyverno-e1], [Implementation software licence][kyverno-e2], [Maintained release history][kyverno-e3], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5], [Project community governance][kyverno-e6], [Current CNCF foundation status][kyverno-e7] | Requested Wave 9 batch marker 2026-10-07, changed only for these ten; execution on 2026-10-08 is disclosed above. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L118<br>legacy:devopstools_final.md#L599 | legacy:4_Kubernetes-Containers/README.md#L118<br>legacy:devopstools_final.md#L599<br>https://github.com/kyverno/kyverno<br>https://github.com/kyverno/kyverno/blob/main/LICENSE<br>https://github.com/kyverno/kyverno/releases<br>https://kyverno.io/docs/<br>https://github.com/kyverno/kyverno/blob/main/README.md<br>https://github.com/kyverno/community/blob/main/GOVERNANCE.md<br>https://www.cncf.io/projects/kyverno/ | [Canonical implementation repository and scope][kyverno-e1], [Implementation software licence][kyverno-e2], [Maintained release history][kyverno-e3], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5], [Project community governance][kyverno-e6], [Current CNCF foundation status][kyverno-e7] | Preserve all legacy sources and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][kyverno-e3], [Canonical implementation repository and scope][kyverno-e1], [Official policy documentation][kyverno-e4], [Core scope, companion projects and security limitations][kyverno-e5] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[kyverno-e1]: https://github.com/kyverno/kyverno
[kyverno-e2]: https://github.com/kyverno/kyverno/blob/main/LICENSE
[kyverno-e3]: https://github.com/kyverno/kyverno/releases
[kyverno-e4]: https://kyverno.io/docs/
[kyverno-e5]: https://github.com/kyverno/kyverno/blob/main/README.md
[kyverno-e6]: https://github.com/kyverno/community/blob/main/GOVERNANCE.md
[kyverno-e7]: https://www.cncf.io/projects/kyverno/

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/kyverno/kyverno) (`archived: false`).

### notary-project

**Identity boundary:** Keep Notary Project as an umbrella, not a silent rename to Notation. It contains signing/verification specifications, Notation CLI/libraries and other subprojects, with OCI interoperability and trust policies. Historical Notary TUF/server architecture is not the modern Notation workflow; Cosign/Sigstore is separate. Move primary category to software-supply-chain-security.

**Licence boundary:** Retain oss based on the official open-source umbrella and directly inspected Apache-2.0 grants in common/specifications/notation/notation-go/notation-core-go repositories. Leave license_spdx absent: those verified component grants do not establish a universal umbrella grant for every subproject/plugin/service. No missing licence model is hidden or inferred from CNCF incubation.

**Product/service boundary:** Leave deployment_models empty: specifications and CLI/libraries are not one umbrella control plane. No managed service/commercial entitlement is inherited by the umbrella; evaluate chosen components and key/registry providers.

**Repository boundary:** Leave repository_url and repository_archived absent. .github contains common governance; specifications covers standards; notation covers a CLI; none is the whole umbrella. The historical notaryproject/notaryproject URL now points to specifications, not an umbrella implementation. Replace organization-only official_url with the actual umbrella site while preserving the organization pointer in sources.

**Governance:** CNCF directly records Notary Project as Incubating since 2017-10-24. Common GOVERNANCE defines organization and subproject maintainers, voting and employer balance; implementation governance is nested rather than replaced with one CLI identity.

**Maturity:** Established is a scoped umbrella judgement from maintained specifications, documented interoperable trust/signing workflows, explicit governance and stable Notation implementation history. It does not declare every subproject/version/plugin production-stable.

**Lifecycle:** Current umbrella site/docs, active non-archived specifications/Notation repositories and Notation v1.3.2 stable release support an active umbrella. Notation upstream activity on 2026-09-25 and its release policy distinguish stable 1.x from prerelease 2.x; no universal component stability or historical server lifecycle is asserted.

**Unresolved questions / limits:** None blocking umbrella identity. Deliberate repository/SPDX/deployment absences are resolved scope decisions, not claims of universal licensing or deployment; users must choose and assess a particular implementation.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Umbrella governance][notary-project-e4], [Common repository licence][notary-project-e5], [Specifications software licence][notary-project-e6], [Notation CLI scope documentation][notary-project-e7], [Notation CLI software licence][notary-project-e8], [Notation library software licence][notary-project-e9], [Notation core library software licence][notary-project-e10], [Notation release stability and support policy][notary-project-e11], [Maintained Notation release history][notary-project-e12], [Current CNCF foundation status][notary-project-e13].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | notary-project | notary-project | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Umbrella governance][notary-project-e4], [Common repository licence][notary-project-e5] | Preserve stable catalogue ID and provenance; no duplicate. |
| `name` | Notary Project | Notary Project | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Notation CLI scope documentation][notary-project-e7] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Supply chain signing and verification for artifacts (CNCF). | Notary Project umbrella for OCI artifact-signing and verification specifications and tools, including Notation CLI/libraries; component grants and deployment differ, and legacy Notary workflows and Sigstore/Cosign remain distinct. | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Notation CLI scope documentation][notary-project-e7] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://github.com/notaryproject | https://notaryproject.dev/ | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Umbrella governance][notary-project-e4], [Common repository licence][notary-project-e5], [Notation CLI scope documentation][notary-project-e7] | Changed: upstream-declared official entry point; any former pointer remains in sources. |
| `repository_url` | *absent* | *absent* | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Umbrella governance][notary-project-e4], [Common repository licence][notary-project-e5] | Leave absent: common governance, specifications and Notation repositories cover only parts of the Notary umbrella. |
| `documentation_url` | *absent* | https://notaryproject.dev/docs/ | [Official umbrella documentation][notary-project-e2] | Add directly checked official documentation for this record scope. |
| `categories` | application-cloud-security | software-supply-chain-security | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Notation CLI scope documentation][notary-project-e7] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `subcategories` | Application Security (SAST, DAST, SCA) &amp; Vulnerability Scanning | Artifact trust specifications and tooling | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Notation CLI scope documentation][notary-project-e7] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `roles` | devsecops-engineer<br>cloud-security-engineer | devsecops-engineer<br>cloud-security-engineer | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Notation CLI scope documentation][notary-project-e7] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `lifecycle_stages` | test<br>secure | release<br>deploy<br>secure | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Notation CLI scope documentation][notary-project-e7] | Changed: reviewer mapping of documented workflows to existing taxonomy; no new taxonomy value. |
| `use_when` | Sign and verify container images/artifacts in your supply chain. | You need portable OCI artifact signature/trust workflows and can choose the relevant Notary specifications, Notation implementation, libraries and trust-policy/key integrations. | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Notation CLI scope documentation][notary-project-e7], [Common repository licence][notary-project-e5], [Specifications software licence][notary-project-e6], [Notation CLI software licence][notary-project-e8], [Notation library software licence][notary-project-e9], [Notation core library software licence][notary-project-e10] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `avoid_when` | You only need image scanning without signature verification. | You need one umbrella executable/control plane, one repository or a universal licence/stability guarantee for every component, plugin and vendor service; evaluate selected implementations separately. | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Notation CLI scope documentation][notary-project-e7], [Common repository licence][notary-project-e5], [Specifications software licence][notary-project-e6], [Notation CLI software licence][notary-project-e8], [Notation library software licence][notary-project-e9], [Notation core library software licence][notary-project-e10] | Changed: selection guidance expresses documented capabilities and scoped component/service limits, not unsupported product rankings. |
| `deployment_models` | `[]` | `[]` | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Notation CLI scope documentation][notary-project-e7] | Leave empty: Notary specifications and implementations do not form one umbrella deployment. |
| `license_model` | oss | oss | [Common repository licence][notary-project-e5], [Specifications software licence][notary-project-e6], [Notation CLI software licence][notary-project-e8], [Notation library software licence][notary-project-e9], [Notation core library software licence][notary-project-e10] | Reviewed; retained: actual software grant and scoped component exceptions; no foundation or commercial-service licence inheritance. |
| `license_spdx` | *absent* | *absent* | [Common repository licence][notary-project-e5], [Specifications software licence][notary-project-e6], [Notation CLI software licence][notary-project-e8], [Notation library software licence][notary-project-e9], [Notation core library software licence][notary-project-e10] | Leave absent: verified Apache grants for Notary core repositories do not establish one universal umbrella/plugin/service grant. |
| `commercial_offering` | *absent* | *absent* | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Umbrella governance][notary-project-e4], [Common repository licence][notary-project-e5] | Leave optional field absent; no denial of all third-party businesses is implied. |
| `maturity` | unknown | established | [Notation release stability and support policy][notary-project-e11], [Maintained Notation release history][notary-project-e12], [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Notation CLI scope documentation][notary-project-e7], [Umbrella governance][notary-project-e4], [Current CNCF foundation status][notary-project-e13] | Editorial established judgement from maintained releases/specifications, documented operations and governance, with feature/component limits stated above. |
| `status` | needs-review | active | [Notation release stability and support policy][notary-project-e11], [Maintained Notation release history][notary-project-e12], [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Notation CLI scope documentation][notary-project-e7] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | *absent* | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Umbrella governance][notary-project-e4], [Common repository licence][notary-project-e5], [Notation release stability and support policy][notary-project-e11], [Maintained Notation release history][notary-project-e12] | Leave absent with umbrella repository; do not inherit a component archival flag. |
| `alternatives` | `[]` | `[]` | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Notation CLI scope documentation][notary-project-e7] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `tags` | `[]` | `[]` | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Notation CLI scope documentation][notary-project-e7] | Retain empty optional metadata; do not add unsupported rankings or tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Umbrella governance][notary-project-e4], [Common repository licence][notary-project-e5], [Specifications software licence][notary-project-e6], [Notation CLI scope documentation][notary-project-e7], [Notation CLI software licence][notary-project-e8], [Notation library software licence][notary-project-e9], [Notation core library software licence][notary-project-e10], [Notation release stability and support policy][notary-project-e11], [Maintained Notation release history][notary-project-e12], [Current CNCF foundation status][notary-project-e13] | Requested Wave 9 batch marker 2026-10-07, changed only for these ten; execution on 2026-10-08 is disclosed above. |
| `sources` | legacy:6_Security/README.md#L37<br>legacy:devopstools_final.md#L888 | legacy:6_Security/README.md#L37<br>legacy:devopstools_final.md#L888<br>https://notaryproject.dev/<br>https://notaryproject.dev/docs/<br>https://github.com/notaryproject/.github/blob/main/README.md<br>https://github.com/notaryproject/.github/blob/main/GOVERNANCE.md<br>https://github.com/notaryproject/.github/blob/main/LICENSE<br>https://github.com/notaryproject/specifications/blob/main/LICENSE<br>https://github.com/notaryproject/notation/blob/main/README.md<br>https://github.com/notaryproject/notation/blob/main/LICENSE<br>https://github.com/notaryproject/notation-go/blob/main/LICENSE<br>https://github.com/notaryproject/notation-core-go/blob/main/LICENSE<br>https://github.com/notaryproject/notation/blob/main/RELEASE_MANAGEMENT.md<br>https://github.com/notaryproject/notation/releases<br>https://www.cncf.io/projects/notary-project/<br>https://github.com/notaryproject | [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Umbrella governance][notary-project-e4], [Common repository licence][notary-project-e5], [Specifications software licence][notary-project-e6], [Notation CLI scope documentation][notary-project-e7], [Notation CLI software licence][notary-project-e8], [Notation library software licence][notary-project-e9], [Notation core library software licence][notary-project-e10], [Notation release stability and support policy][notary-project-e11], [Maintained Notation release history][notary-project-e12], [Current CNCF foundation status][notary-project-e13] | Preserve all legacy sources and append directly checked primary evidence. Preserve the former official pointer https://github.com/notaryproject as provenance. |
| `needs_review` | `true` | `false` | [Notation release stability and support policy][notary-project-e11], [Maintained Notation release history][notary-project-e12], [Official umbrella project identity][notary-project-e1], [Official umbrella documentation][notary-project-e2], [Umbrella scope and subproject repositories][notary-project-e3], [Notation CLI scope documentation][notary-project-e7] | CLEAR REVIEW: active project with resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `official_url`, `documentation_url`, `categories`, `subcategories`, `lifecycle_stages`, `use_when`, `avoid_when`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`.

[notary-project-e1]: https://notaryproject.dev/
[notary-project-e2]: https://notaryproject.dev/docs/
[notary-project-e3]: https://github.com/notaryproject/.github/blob/main/README.md
[notary-project-e4]: https://github.com/notaryproject/.github/blob/main/GOVERNANCE.md
[notary-project-e5]: https://github.com/notaryproject/.github/blob/main/LICENSE
[notary-project-e6]: https://github.com/notaryproject/specifications/blob/main/LICENSE
[notary-project-e7]: https://github.com/notaryproject/notation/blob/main/README.md
[notary-project-e8]: https://github.com/notaryproject/notation/blob/main/LICENSE
[notary-project-e9]: https://github.com/notaryproject/notation-go/blob/main/LICENSE
[notary-project-e10]: https://github.com/notaryproject/notation-core-go/blob/main/LICENSE
[notary-project-e11]: https://github.com/notaryproject/notation/blob/main/RELEASE_MANAGEMENT.md
[notary-project-e12]: https://github.com/notaryproject/notation/releases
[notary-project-e13]: https://www.cncf.io/projects/notary-project/

## Review-debt accounting

Selected **10**, cleared **10**, retained **0**. Before/after `python -m scripts.review_debt --format markdown --limit 30` output is captured.

| Counter | Before | After |
|---|---:|---:|
| canonical_records | 1,425 | 1,425 |
| needs_review | 746 | 736 |
| status_needs_review | 746 | 736 |
| mismatches | 0 | 0 |
| unknown_license | 80 | 80 |
| unknown_maturity | 883 | 874 |
| missing_repository | 391 | 391 |
| missing_documentation | 880 | 870 |
| missing_sources | 0 | 0 |

Status/flag mismatches remain zero. Documentation debt decreases by ten and unknown maturity by nine; Cosign was experimental, not unknown. Repository debt remains unchanged because Notary umbrella absence is deliberate. Unknown licence model count remains unchanged.

## Generated changes

Only generator output is listed here; the evidence report and focused tests are authored files.

- `README.md`
- `docs/catalog-statistics.json`
- `docs/categories/application-cloud-security.md`
- `docs/categories/emerging-experimental.md`
- `docs/categories/iam-secrets-certificates.md`
- `docs/categories/kubernetes-networking-storage-addons.md`
- `docs/categories/software-supply-chain-security.md`
- `docs/lifecycle/build.md`
- `docs/lifecycle/deploy.md`
- `docs/lifecycle/develop.md`
- `docs/lifecycle/learn.md`
- `docs/lifecycle/operate.md`
- `docs/lifecycle/release.md`
- `docs/lifecycle/secure.md`
- `docs/lifecycle/test.md`
- `docs/roles/cloud-engineer.md`
- `docs/roles/cloud-security-engineer.md`
- `docs/roles/devops-engineer.md`
- `docs/roles/devsecops-engineer.md`
- `docs/roles/kubernetes-engineer.md`
- `docs/roles/platform-engineer.md`
- `docs/roles/release-engineer.md`
- `docs/roles/site-reliability-engineer.md`

## Validation and full link audit

Required checks passed. Python 3.12.3 in the existing WSL Ubuntu constrained environment ran installation, fresh dependency resolution, the complete suite and the network audit. The Windows editable environment ran focused tests, lint/format, generation, catalogue validation and debt capture. `python` below denotes the selected interpreter.

| Command | Result |
|---|---|
| `python -m pip install -e '.[dev]' -c config/python-constraints-3.12.txt` | PASS; constrained editable install |
| `python -m scripts.python_constraints --check` | PASS; fresh resolver matches unchanged constraints |
| `python -m ruff check scripts tests` | PASS |
| `python -m ruff format --check scripts tests` | PASS; 62 files already formatted |
| `python -m pytest tests/test_wave9_evidence_review.py` | PASS; 23 tests |
| `python -m pytest` | PASS; 771 tests in 266.59 seconds |
| `python -m scripts.generate_docs` | PASS; regenerated after canonical changes |
| `python -m scripts.generate_docs --check` | PASS |
| `python -m scripts.validate_catalog` | PASS |
| `python -m scripts.review_debt --format markdown --limit 30` | PASS; before/after output captured |
| `git diff --check` | PASS |

Pytest cache permission warnings, where emitted, were non-failing. WSL Git-dependent tests used process-only `GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=true` to interpret the Windows checkout consistently. No repository/global Git setting, constraint, assertion or workflow was weakened.

The 23 focused cases guard project-specific licence evidence; Cosign versus other Sigstore components; Syft SBOM generation versus Grype matching and output formats versus software licensing; Anchore OSS versus Enterprise/support; Gitleaks local CLI versus hosted/Action terms; SOPS encrypted-file editing versus secret-serving/key services; current Vault Community BUSL versus Enterprise/HCP and separately licensed API/SDK; upstream Keycloak versus vendor packaging; cert-manager versus issuers/certbot/secrets backends; Kyverno policy enforcement versus signing/RBAC; Notary umbrella versus Notation/component licences; and foundation status versus licence evidence. No prices, temporary versions or release dates are asserted.

Exactly one fresh full strict audit used no cache reuse and ignored output paths:

```bash
python -m scripts.check_links --strict --check-archived --workers 8 --cache tmp/wave9/link-cache.json --cache-hours 0 --json-report tmp/wave9/link-report.json --markdown-report tmp/wave9/link-report.md
```

| Audit counter | Result |
|---|---:|
| URLs | 2,666 |
| blocking_new | 0 |
| blocking_known observed | 4 |
| strict_result | PASS |

**Reviewed baseline changed: NO.** All six existing exceptions remain untouched. Runtime rate limits, access/transport restrictions and inconclusive responses do not establish a historical defect repaired or a project retired.

| Existing baseline URL | Observed response | Classification / strict status |
|---|---|---|
| `https://github.com/hoji-ai/hoji` | HTTP 429 | rate-limited / nonblocking |
| `https://github.com/ophircloud/DevOps-Projects` | HTTP 429 | rate-limited / nonblocking |
| `https://hub.docker.com/r/soosio/dast` | HTTP 404 | manual-verification-required / blocking-known |
| `https://kubeflame.github.io` | HTTP 404 | manual-verification-required / blocking-known |
| `https://www.opentext.com/products/static-application-security-testing` | HTTP 444 | http-error / blocking-known |
| `https://www.yotascale.com` | HTTP 404 | manual-verification-required / blocking-known |

All ten final documentation entry points were included:

| ID | Documentation response | Classification |
|---|---|---|
| `cosign-sigstore` | HTTP 200 | valid |
| `syft` | HTTP 200 | valid |
| `grype` | HTTP 200 | valid |
| `gitleaks` | HTTP 429 | rate-limited |
| `sops` | HTTP 200 | valid |
| `keycloak` | HTTP 200 | valid |
| `hashicorp-vault` | HTTP 200 | valid |
| `cert-manager` | HTTP 200 | valid |
| `kyverno` | HTTP 200 | permanent-redirect |
| `notary-project` | HTTP 200 | valid |

All classifications, including network-dependent limitations:

| Classification | Count |
|---|---:|
| dns-inconclusive | 5 |
| http-error | 1 |
| manual-verification-required | 3 |
| network-inconclusive | 1 |
| permanent-redirect | 206 |
| rate-limited | 761 |
| restricted-or-bot-blocked | 360 |
| timeout-inconclusive | 1 |
| transient-failure | 1 |
| valid | 1,291 |
| valid-redirect | 36 |

Strict PASS means no newly classified blockers, not successful verification of every endpoint. Directly read licences, official documentation/terms, governance, upstream metadata and release/maintenance evidence independently support decisions. Source-only links were read separately: the audit inventories official/repository/documentation fields. No required network audit was omitted. Raw cache/output stays ignored under `tmp/wave9/`; nothing under `reports/` is committed. No second full audit was run.

## Scope verification and review state

Snapshot and baseline Git tree establish exactly ten changed IDs, dates and record blocks and 240 complete material-field rows. All legacy provenance remains. Every other record block is unchanged. The final canonical URL set equals the audited set. The six-entry baseline, committed audit output/ledger, workflows, CodeQL configuration and Python constraints remain unchanged.

Issue #2 remains read-only; body and updated_at (2026-10-07T21:57:09Z) are compared with the pre-edit snapshot at handoff. No Wave 4–8 records are revisited; Wave 10 is not started. No merge or release is performed.

Resolved review findings: Cosign is an established signing/verification component rather than the entire Sigstore project; Syft generates SBOMs while Grype matches known vulnerabilities and neither inherits Enterprise licensing; Gitleaks is feature-complete with security-patch-only maintenance and its CLI MIT grant does not inherit Action terms; SOPS current getsops/CNCF maintainership and encrypted-file boundary replace historical Mozilla/backend ambiguity; Keycloak upstream IAM is separate from vendor packaging/managed IAM; current Vault Community BUSL is separate from historical MPL, MPL SDK/API and Enterprise/HCP; cert-manager controls certificate resources through issuers rather than becoming those issuers; current CNCF Kyverno graduation supersedes stale README Incubating wording while catalogue maturity is independent; Notary remains an umbrella with deliberate repository/SPDX/deployment absences.

Early local validation also caught a duplicate shared Anchore official_url for Syft/Grype. It was resolved within the selected cohort by using the directly checked Syft SBOM guide as its official/docs entry point; no validator or alias configuration changed. This preserves the same distinct canonical URL set covered by the one audit. Documentation was regenerated and validation passed afterward.

No material identity/licence boundary remains unresolved. Optional-field absences, component stability, Gitleaks feature freeze, deprecated Kyverno policy-type migrations and product-specific terms remain documented limitations. Requested batch date and actual execution date are explicitly distinguished.

Final-head CI/security checks and any automatic PR findings are recorded in the PR and final handoff.
