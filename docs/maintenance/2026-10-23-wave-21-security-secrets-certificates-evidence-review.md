# Wave 21 — Security, Secrets and Certificates evidence review

Reviewed: 2026-10-23. Baseline main: `f50a239e7dff2f782e4e413bbf80846cabd62e09`. Tracker: [#131](https://github.com/goozcena-gnl/devops-tools-catalog/issues/131).

**Revised decisions following Codex P1: 5 CLEAR, 5 RETAIN REVIEW.** All 10 IDs unchanged; review debt 640 → 635, active 771 → 776 once the official generator is rerun. These are **proposals**, not acceptance to merge. There is a concurrent unrelated contributor PR #132 that this branch must not touch.

## Decisions and remaining uncertainties

| ID | Decision | Evidence and unresolved issue |
|---|---|---|
| `certmate` | **CLEAR** | MIT self-hosted TLS certificate inventory and ACME automation; v2.52.0 Oct 2026. Safeguard credentials, private keys, administrative API. |
| `keystore-explorer` | **RETAIN REVIEW** | GPLv3 family confirmed, but no authoritative grant establishes GPL-3.0-only versus GPL-3.0-or-later. Codex P1; no exact SPDX asserted. |
| `lade` | **CLEAR** | Tagged v0.19.2 MPL-2.0 CLI using per-command ephemeral secret resolution, agent shell hooks and network forwarding; do not imply it is a vault. |
| `mkcert` | **RETAIN REVIEW** | BSD-3-Clause local development CA. Stable GitHub release v1.4.4 from April 2022; no verified security-maintenance guarantee. |
| `teleport` | **RETAIN REVIEW** | Source AGPLv3 and API Apache licensing differ from restrictive Community binary licence (<100 employees and <$10m annual revenue with narrow emergency exception). Need versioned distribution/entitlement verification. |
| `teller` | **RETAIN REVIEW** | Apache CLI reads secrets from external providers, last stable GitHub release v2.0.7 May 2024. Support cadence uncertain. |
| `detect-secrets` | **CLEAR** | Yelp Apache-2.0 baseline and triage driven secret detector; repository activity April 2026 but last GitHub stable v1.5.0 May 2024. |
| `pip-audit` | **CLEAR** | PyPA Apache-2.0 dependency advisory scans, optional --fix and June 2026 v2.10.1 release. |
| `trufflehog` | **RETAIN REVIEW** | AGPLv3 family confirmed, but explicit upstream variant AGPL-3.0-only versus AGPL-3.0-or-later unresolved, as noted by Codex P1. |
| `testssl-sh` | **CLEAR** | Original drwetter repository redirects to testssl/testssl.sh; stable v3.2.4 July 2026, GPLv2 terms, Bash-based authorized TLS probing. |

## Complete changed-field baseline → proposed final ledger

All changed canonical fields, including complete sources and legacy provenance, are listed. Unlisted fields are identical. `∅` means absent.

### `certmate` — data/tools/iam-secrets-certificates.yaml

| Field | Before | After |
|---|---|---|
| `summary` | summary: Certificate management automation. | summary: Self-hosted TLS certificate inventory and lifecycle management for issuance, renewals and deployment hooks using ACME, with operator-controlled CA credentials and private keys. |
| `use_when` | use_when:; Lightweight cert lifecycle automation. | use_when:; You need inventory, ACME automation and repeatable certificate deployment across self-managed infrastructure. |
| `avoid_when` | avoid_when:; You're on Kubernetes (use cert-manager instead). | avoid_when:; You cannot protect DNS API credentials, private keys, backup secrets or access to the management API.; You require Kubernetes-native Secret/cert issuance integration directly rather than a separate certificate service. |
| `maturity` | maturity: unknown | maturity: growing |
| `status` | status: needs-review | status: active |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-23' |
| `sources` | sources:; legacy:6_Security/README.md#L98; legacy:devopstools_final.md#L988 | sources:; legacy:6_Security/README.md#L98; legacy:devopstools_final.md#L988; https://github.com/fabriziosalmi/certmate/blob/main/LICENSE; https://github.com/fabriziosalmi/certmate/blob/v2.52.0/README.md; https://github.com/fabriziosalmi/certmate/releases/tag/v2.52.0 |
| `needs_review` | needs_review: true | needs_review: false |
| `license_spdx` | ∅ | license_spdx: MIT |
| `repository_archived` | ∅ | repository_archived: false |
| `documentation_url` | ∅ | documentation_url: https://github.com/fabriziosalmi/certmate/blob/main/README.md |

### `keystore-explorer` — data/tools/iam-secrets-certificates.yaml

| Field | Before | After |
|---|---|---|
| `summary` | summary: GUI for managing keystores. | summary: Desktop Java KeyStore and certificate manager for PKCS#12, JKS and related formats, with JRE 17+ required and GPLv3 project licensing. |
| `use_when` | use_when:; Visual inspection/editing of JKS/PKCS#12 keystores during development. | use_when:; You need a local GUI to inspect or manage Java trust stores, private keys and PKCS#12 certificates. |
| `avoid_when` | avoid_when:; For automated cert management in CI/CD. | avoid_when:; You need headless automated certificate issuance, fleet-scale PKI or centralized key custody.; You cannot securely handle exported private keys, workstation access and password-protected keystores. |
| `maturity` | maturity: unknown | maturity: established |
| `status` | status: needs-review | status: needs-review |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-23' |
| `sources` | sources:; legacy:6_Security/README.md#L103; legacy:devopstools_final.md#L993 | sources:; legacy:6_Security/README.md#L103; legacy:devopstools_final.md#L993; https://github.com/kaikramer/keystore-explorer/blob/main/LICENSE; https://github.com/kaikramer/keystore-explorer/blob/v5.7.0/README.md; https://github.com/kaikramer/keystore-explorer/releases/tag/v5.7.0 |
| `needs_review` | needs_review: true | needs_review: true |
| `documentation_url` | ∅ | documentation_url: https://github.com/kaikramer/keystore-explorer/blob/main/README.md |
| `repository_archived` | ∅ | repository_archived: false |

### `lade` — data/tools/iam-secrets-certificates.yaml

| Field | Before | After |
|---|---|---|
| `summary` | summary: Auto-load secrets from vaults into environment variables or files for shell commands with minimal exposure. | summary: MPL-2.0 command-scoped secret and private-network access wrapper using provider-resolved environment variables, short-lived tunnels, shell hooks and agent harness hooks. |
| `use_when` | use_when: [] | use_when:; You need secrets or private tunnels injected only while a matching local command, CI command or agent harness step runs. |
| `avoid_when` | avoid_when: [] | avoid_when:; You cannot audit shell pre-exec hooks, provider CLI privileges, temporary files or agent tool execution boundaries.; You need a managed secrets database rather than just-in-time retrieval from external providers. |
| `maturity` | maturity: unknown | maturity: emerging |
| `status` | status: needs-review | status: active |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-23' |
| `sources` | sources:; legacy:devopstools_final.md#L979 | sources:; legacy:devopstools_final.md#L979; https://github.com/zifeo/lade/blob/v0.19.2/LICENSE; https://github.com/zifeo/lade/blob/v0.19.2/README.md; https://github.com/zifeo/lade/releases/tag/v0.19.2 |
| `needs_review` | needs_review: true | needs_review: false |
| `license_spdx` | ∅ | license_spdx: MPL-2.0 |
| `documentation_url` | ∅ | documentation_url: https://github.com/zifeo/lade/blob/v0.19.2/README.md |
| `repository_archived` | ∅ | repository_archived: false |

### `mkcert` — data/tools/iam-secrets-certificates.yaml

| Field | Before | After |
|---|---|---|
| `summary` | summary: BSD-3-Clause CLI creating a locally trusted development CA and TLS certificates; current upstream maintenance remains unconfirmed. | summary: BSD-3-Clause local development certificate authority and TLS certificate CLI; the local rootCA-key.pem is highly sensitive and recent security maintenance remains unproven. |
| `avoid_when` | avoid_when:; You need a production public certificate authority or automated corporate PKI lifecycle.; You cannot protect the generated local rootCA-key.pem private key or require proven ongoing security maintenance. | avoid_when:; You need publicly trusted production certificates or automated enterprise PKI; mkcert is for development environments.; You cannot protect the local rootCA-key.pem or require verified ongoing releases and security support. |
| `verified_on` | verified_on: '2026-10-18' | verified_on: '2026-10-23' |
| `sources` | sources:; legacy:6_Security/README.md#L104; legacy:devopstools_final.md#L994; https://github.com/FiloSottile/mkcert; https://github.com/FiloSottile/mkcert/blob/master/README.md; https://github.com/FiloSottile/mkcert/blob/master/LICENSE; https://github.com/FiloSottile/mkcert/releases | sources:; legacy:6_Security/README.md#L104; legacy:devopstools_final.md#L994; https://github.com/FiloSottile/mkcert; https://github.com/FiloSottile/mkcert/blob/master/README.md; https://github.com/FiloSottile/mkcert/blob/master/LICENSE; https://github.com/FiloSottile/mkcert/releases; https://github.com/FiloSottile/mkcert/blob/v1.4.4/LICENSE; https://github.com/FiloSottile/mkcert/blob/v1.4.4/README.md; https://github.com/FiloSottile/mkcert/releases/tag/v1.4.4 |

### `teleport` — data/tools/iam-secrets-certificates.yaml

| Field | Before | After |
|---|---|---|
| `summary` | summary: Infrastructure access platform for SSH Kubernetes databases and apps with separate AGPL source, Apache API module and restricted Community binary terms. | summary: Teleport manages audited SSH, Kubernetes, database and application access; AGPL source/API module licences differ from the restricted Community binary and commercial Enterprise offerings. |
| `avoid_when` | avoid_when:; You treat AGPL-3.0 source code or Apache-2.0 API-module terms as granting unrestricted Community binary rights.; You need unrestricted distribution or business use but have not evaluated the Community size and revenue limitations. | avoid_when:; You assume the source AGPL or API Apache grant permits unrestricted use or redistribution of Community binaries.; Your organization exceeds Community employee or revenue limits or cannot verify Enterprise/HCP eligibility and critical-patch exception conditions. |
| `verified_on` | verified_on: '2026-10-18' | verified_on: '2026-10-23' |
| `sources` | sources:; legacy:6_Security/README.md#L117; legacy:devopstools_final.md#L1010; https://github.com/gravitational/teleport; https://github.com/gravitational/teleport/blob/master/README.md; https://github.com/gravitational/teleport/blob/master/LICENSE; https://github.com/gravitational/teleport/blob/master/api/LICENSE; https://github.com/gravitational/teleport/blob/master/build.assets/LICENSE-community; https://goteleport.com/blog/teleport-community-license/; https://goteleport.com/docs/ | sources:; legacy:6_Security/README.md#L117; legacy:devopstools_final.md#L1010; https://github.com/gravitational/teleport; https://github.com/gravitational/teleport/blob/master/README.md; https://github.com/gravitational/teleport/blob/master/LICENSE; https://github.com/gravitational/teleport/blob/master/api/LICENSE; https://github.com/gravitational/teleport/blob/master/build.assets/LICENSE-community; https://goteleport.com/blog/teleport-community-license/; https://goteleport.com/docs/; https://github.com/gravitational/teleport/releases/tag/v18.10.0 |

### `teller` — data/tools/iam-secrets-certificates.yaml

| Field | Before | After |
|---|---|---|
| `summary` | summary: Apache-2.0 Rust CLI for retrieving and injecting secrets from configured external providers; current release support remains inconclusive. | summary: Apache-2.0 CLI for accessing secrets from external stores and injecting them into local and CI commands; fresh stable release support remains unverified. |
| `avoid_when` | avoid_when:; You require a standalone secrets database; Teller reads from other providers.; You cannot verify provider compatibility and release maintenance or safely protect local credentials and exported secrets. | avoid_when:; You need a standalone encrypted secrets database; Teller retrieves secrets from other provider services.; You cannot restrict shell environment exposure and credentials or require a verified current security release cadence. |
| `verified_on` | verified_on: '2026-10-18' | verified_on: '2026-10-23' |
| `sources` | sources:; legacy:devopstools_final.md#L984; https://github.com/tellerops/teller; https://github.com/tellerops/teller/blob/master/README.md; https://github.com/tellerops/teller/blob/master/LICENSE.txt; https://github.com/tellerops/teller/releases | sources:; legacy:devopstools_final.md#L984; https://github.com/tellerops/teller; https://github.com/tellerops/teller/blob/master/README.md; https://github.com/tellerops/teller/blob/master/LICENSE.txt; https://github.com/tellerops/teller/releases; https://github.com/tellerops/teller/releases/tag/v2.0.7 |

### `detect-secrets` — data/tools/application-cloud-security.yaml

| Field | Before | After |
|---|---|---|
| `summary` | summary: Secrets detection with baseline support (reduce false positives). | summary: Apache-2.0 repository secret detector using configurable plugins, baselines and manual triage to prevent new credentials entering version control. |
| `use_when` | use_when:; As a pre-commit hook to prevent secret leaks with manageable false-positive rates. | use_when:; You need pre-commit and CI checks with a reviewed secret baseline that helps control false positives. |
| `avoid_when` | avoid_when:; You need historical repo scanning (use TruffleHog/Gitleaks). | avoid_when:; You need guaranteed detection of all leaked credentials or verified live validity without additional tools.; You require repository-wide secret history triage beyond a configured baseline-only pre-commit process. |
| `maturity` | maturity: unknown | maturity: established |
| `status` | status: needs-review | status: active |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-23' |
| `sources` | sources:; legacy:6_Security/README.md#L21; legacy:devopstools_final.md#L857 | sources:; legacy:6_Security/README.md#L21; legacy:devopstools_final.md#L857; https://github.com/Yelp/detect-secrets/blob/master/LICENSE; https://github.com/Yelp/detect-secrets/releases/tag/v1.5.0; https://github.com/Yelp/detect-secrets/blob/master/README.md |
| `needs_review` | needs_review: true | needs_review: false |
| `license_spdx` | ∅ | license_spdx: Apache-2.0 |
| `documentation_url` | ∅ | documentation_url: https://github.com/Yelp/detect-secrets/blob/master/README.md |
| `repository_archived` | ∅ | repository_archived: false |

### `pip-audit` — data/tools/application-cloud-security.yaml

| Field | Before | After |
|---|---|---|
| `summary` | summary: Audit Python environments/dependencies for known vulnerabilities. | summary: Apache-2.0 Python dependency vulnerability auditor using packaging advisory data, with requirements or environment scans and optional remediation via --fix. |
| `use_when` | use_when:; Python-specific SCA in CI. | use_when:; You need vulnerability checking for installed Python packages or requirements in CI and want advisory-backed findings. |
| `avoid_when` | avoid_when:; You already run Trivy/Grype which also cover Python packages. | avoid_when:; You need malicious package discovery, a complete security assessment or proof that packages without advisories are safe.; Automatic --fix updates would be applied without dependency-lock review, regression tests and change control. |
| `maturity` | maturity: unknown | maturity: established |
| `status` | status: needs-review | status: active |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-23' |
| `sources` | sources:; legacy:6_Security/README.md#L45; legacy:devopstools_final.md#L900 | sources:; legacy:6_Security/README.md#L45; legacy:devopstools_final.md#L900; https://github.com/pypa/pip-audit/blob/main/LICENSE; https://github.com/pypa/pip-audit/releases/tag/v2.10.1; https://github.com/pypa/pip-audit/blob/v2.10.1/README.md |
| `needs_review` | needs_review: true | needs_review: false |
| `license_spdx` | ∅ | license_spdx: Apache-2.0 |
| `documentation_url` | ∅ | documentation_url: https://github.com/pypa/pip-audit/blob/main/README.md |
| `repository_archived` | ∅ | repository_archived: false |

### `trufflehog` — data/tools/application-cloud-security.yaml

| Field | Before | After |
|---|---|---|
| `summary` | summary: Secret scanning tool; OSS core with enterprise features and integrations. | summary: AGPLv3 TruffleHog v3 scans Git repositories and other sources for secrets and can verify selected credentials; enterprise monitoring is a separate commercial product. |
| `use_when` | use_when:; Deep Git history scanning with credential verification. | use_when:; You need permissioned scans for leaked credentials with verified findings and controlled remediation workflows. |
| `avoid_when` | avoid_when:; You only need pre-commit hooks (use detect-secrets or Gitleaks). | avoid_when:; You cannot authorize scanning of repositories or provider API verification that could contact external services.; You assume all detectors verify secrets or the v2 GPL code and v3 AGPL code have identical licence terms. |
| `maturity` | maturity: unknown | maturity: established |
| `status` | status: needs-review | status: needs-review |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-23' |
| `sources` | sources:; legacy:6_Security/README.md#L55; legacy:devopstools_final.md#L919 | sources:; legacy:6_Security/README.md#L55; legacy:devopstools_final.md#L919; https://github.com/trufflesecurity/trufflehog/blob/main/LICENSE; https://github.com/trufflesecurity/trufflehog/blob/main/README.md; https://github.com/trufflesecurity/trufflehog/releases/tag/v3.99.4 |
| `needs_review` | needs_review: true | needs_review: true |
| `commercial_offering` | ∅ | commercial_offering: true |
| `documentation_url` | ∅ | documentation_url: https://github.com/trufflesecurity/trufflehog/blob/main/README.md |
| `repository_archived` | ∅ | repository_archived: false |

### `testssl-sh` — data/tools/application-cloud-security.yaml

| Field | Before | After |
|---|---|---|
| `summary` | summary: Command-line tool for testing TLS/SSL ciphers, protocols, and vulnerabilities. | summary: GPL-2.0-only Bash TLS/SSL endpoint configuration scanner reporting protocols, cipher suites and selected cryptographic flaws, with stable upstream v3.2.4 and machine-readable output. |
| `repository_url` | repository_url: https://github.com/drwetter/testssl.sh | repository_url: https://github.com/testssl/testssl.sh |
| `use_when` | use_when:; Quick, scriptable TLS configuration audits. | use_when:; You have authorization to assess TLS versions, cipher suites, certificates and known protocol weaknesses on owned endpoints. |
| `avoid_when` | avoid_when:; You need continuous monitoring (use a TLS observatory or Qualys SSL Labs API). | avoid_when:; You need passive, continuous certificate inventory or cannot obtain authorization to actively probe endpoints.; You assume the stable 3.2.x release and the separate 3.3 development snapshots provide identical tested capabilities. |
| `maturity` | maturity: unknown | maturity: established |
| `status` | status: needs-review | status: active |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-23' |
| `sources` | sources:; legacy:6_Security/README.md#L52; legacy:devopstools_final.md#L916 | sources:; legacy:6_Security/README.md#L52; legacy:devopstools_final.md#L916; https://github.com/testssl/testssl.sh/blob/v3.2.4/LICENSE; https://github.com/testssl/testssl.sh/blob/v3.2.4/Readme.md; https://github.com/testssl/testssl.sh/releases/tag/v3.2.4 |
| `needs_review` | needs_review: true | needs_review: false |
| `license_spdx` | ∅ | license_spdx: GPL-2.0-only |
| `documentation_url` | ∅ | documentation_url: https://github.com/testssl/testssl.sh/blob/v3.2.4/Readme.md |
| `repository_archived` | ∅ | repository_archived: false |

## Codex P1 corrections — exact licence grant remains unverified

The Codex review on PR #133 identified two material errors in premature clearance. `keystore-explorer` has standard GPLv3 boilerplate but no verified project-specific `-only` / `-or-later` grant. `trufflehog` has AGPLv3 boilerplate without a verified exact variant, including an upstream licence ambiguity discussion. Both records now **retain** `needs_review: true` and `status: needs-review` and **omit** `license_spdx` entirely; version, maintenance and general licence-family context are preserved. No claim of fully resolved licensing is made. This replaces the initial seven-cleared/five-retained projection with **five cleared/five retained**. Regenerate all derived statistics and pages, then re-run CI and a strict link audit on the updated SHA. Do not resolve P1 threads until the updates and evidence are checked. The earlier audit #29 applies only to the superseded SHA `10178d8eb4930d029797fb1549a28f6ba6d60fae`.

## Required validation and blockers

- Canonical changes limited to the 10 selected IDs in two files. Existing provenance retained. For cases kept in review, unchanged `needs_review: true` and `status: needs-review` do not signify clearance.
- **Generated views still require the repository's actual `python -m scripts.generate_docs`**. Until exact outputs are committed, the Draft PR is intentionally blocked. Never manually modify generated Markdown.
- Recheck source-level licences and especially KeyStore Explorer's exact GPL grant, testssl.sh's exact GPL identifier, Teleport binary rights and TruffleHog v3 scope. Repository license badges and COPYING boilerplate alone cannot prove SPDX scope.
- In a full checkout run Python 3.12 with 19 locked constraints, `pip check`, Ruff, pytest, `python -m scripts.generate_docs`, `python -m scripts.generate_docs --check`, `python -m scripts.validate_catalog`, `git diff --check` and all security workflows. Correct any failure, without downgrading checks.
- On **final** PR head after CI success, manually dispatch strict Full link audit; require `strict_result: PASS`, `blocking_new: 0`, unchanged historical 6 exceptions. Separately verify evidence-only `sources` URLs.
- Do not merge, release, alter URL baseline or close #131 or #2. No automatic lifecycle conclusion from transient HTTP failures.
