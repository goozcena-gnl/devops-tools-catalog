# Wave 16 — IAM, secrets and certificates — final evidence-review handoff

- **Review date:** 2026-10-18; **baseline main:** [`013b7907be7a100f21c5d417e75dbe9e662f8506`](https://github.com/goozcena-gnl/devops-tools-catalog/commit/013b7907be7a100f21c5d417e75dbe9e662f8506); **reviewed HEAD:** [`a06425457b71abe0f16ca80a2076600a557f878f`](https://github.com/goozcena-gnl/devops-tools-catalog/commit/a06425457b71abe0f16ca80a2076600a557f878f) (before this reporting-only revision).
- **Fixed scope:** ten existing IDs in `data/tools/iam-secrets-certificates.yaml`; no other canonical file or review ID touched.
- **Disposition:** **6 CLEAR / 4 RETAIN**, inventory **1,425 unchanged**, review debt **679 → 673**, one original archived repository newly recorded, and stable IDs/legacy provenance retained.
- **PR:** [#122](https://github.com/goozcena-gnl/devops-tools-catalog/pull/122); **issue:** [#121](https://github.com/goozcena-gnl/devops-tools-catalog/issues/121); **URL maintenance tracker:** [#2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2) (do not close or overwrite historical observations).

## Recorded disposition and boundaries

| ID | Disposition | Rationale and unresolved fact |
|---|---|---|
| `hashicorp-boundary` | **RETAIN — archival recorded, product/licence boundary unresolved** | Upstream README explicitly says Community Edition was archived 2026-10-08 with no planned patches, while HCP/Enterprise continue. BSL-licensed CE source is not equivalent to supported Enterprise distributions. |
| `openbao` | **CLEAR** | OpenBao is a community-governed self-hosted secrets platform; official upstream and MPL-2.0 text, current release and documentation support identity, functionality and current lifecycle. |
| `teleport` | **RETAIN — component-specific licence boundaries** | Root source AGPL, API module Apache-2.0, Community binary with employee/revenue limits and documented exception; not safely reducible to one all-editions grant. |
| `dex` | **CLEAR** | Dex README documents OIDC federation via external identity connectors; Apache-2.0 licensed upstream with documented current releases. Not a standalone enterprise directory. |
| `jumpserver` | **CLEAR** | Official JumpServer repository GPL-3.0; current release supports self-hosted PAM. Core/community and separately paid Enterprise offerings distinguished. Historic N2a-owned official URL is preserved. |
| `openstack-barbican` | **CLEAR** | OpenStack Barbican is Apache-2.0 Key Manager service; OpenDev hosts upstream; GitHub explicitly identifies itself as a mirror. |
| `doppler` | **CLEAR** | Commercial Doppler-hosted secrets product differs from its Apache-2.0 CLI. Review models the hosted service, not the CLI code licence as licence of SaaS. |
| `boulder-let-s-encrypt` | **CLEAR** | Let's Encrypt Boulder repository implements an ACME CA server, not a general ACME client. MPL-2.0 via LICENSE.txt and dated release. |
| `mkcert` | **RETAIN — release/maintenance evidence inconclusive** | BSD-3-Clause tool creates local development CAs only. README warns about the generated root CA key. Latest GitHub release observed 2022-04-26 and push 2024-08-13; unarchived repo alone is not maintenance evidence. |
| `teller` | **RETAIN — ongoing maintenance/support inconclusive** | Rust CLI resolves secrets from external providers, Apache-2.0 licensed via LICENSE.txt. Last GitHub release observed 2024-05-20; provider/version maintenance still needs project support confirmation. |

## Complete field-level change ledger

The following tables compare the **exact changed fields** in canonical YAML against the fixed main baseline. Values are kept complete; `∅` denotes an absent field. Source lists include old legacy references plus added official evidence. The evidence URLs shown for each tool support the field-level decisions and are not network-reachability guarantees.

### `hashicorp-boundary` — RETAIN — archival recorded, product/licence boundary unresolved

**Primary evidence:** [github.com/hashicorp/boundary/blob/main/README.md](https://github.com/hashicorp/boundary/blob/main/README.md) · [github.com/hashicorp/boundary/blob/main/LICENSE](https://github.com/hashicorp/boundary/blob/main/LICENSE) · [developer.hashicorp.com/boundary/docs](https://developer.hashicorp.com/boundary/docs).

| Changed field | Before | After |
|---|---|---|
| `summary` | `Secure remote access to systems.` | `Identity-aware infrastructure access product; Boundary Community Edition (CE) repository was archived on 2026-10-08 and no further CE fixes, releases or security patches are planned. HCP Boundary and Boundary Enterprise continue separately.` |
| `official_url` | `https://boundaryproject.io` | `https://developer.hashicorp.com/boundary` |
| `use_when` | `Identity-based, zero-trust access to infrastructure without a traditional VPN.` | `You are maintaining a previously deployed Boundary CE estate and explicitly accept a frozen,` |
| `avoid_when` | `You need a full PAM solution with session recording out of the box (use Teleport or JumpServer).` | `You require community security patches, maintenance, ongoing feature development or supported; Do not mistake continued HCP Boundary or Boundary Enterprise development for active development` |
| `verified_on` | `'2026-08-03'` | `'2026-10-18'` |
| `sources` | `legacy:6_Security/README.md#L114; legacy:devopstools_final.md#L1007` | `legacy:6_Security/README.md#L114; legacy:devopstools_final.md#L1007; https://github.com/hashicorp/boundary; https://github.com/hashicorp/boundary/blob/main/README.md; https://github.com/hashicorp/boundary/blob/main/LICENSE; https://developer.hashicorp.com/boundary/docs` |
| `repository_archived` | ∅ | `true` |
| `documentation_url` | ∅ | `https://developer.hashicorp.com/boundary/docs` |

### `openbao` — CLEAR

**Primary evidence:** [github.com/openbao/openbao/blob/main/README.md](https://github.com/openbao/openbao/blob/main/README.md) · [github.com/openbao/openbao/blob/main/LICENSE](https://github.com/openbao/openbao/blob/main/LICENSE) · [github.com/openbao/openbao/releases](https://github.com/openbao/openbao/releases) · [openbao.org/docs/](https://openbao.org/docs/).

| Changed field | Before | After |
|---|---|---|
| `summary` | `Open-source secrets management and encryption platform.` | `Community-governed MPL-2.0 secrets service providing encrypted KV storage, dynamic credentials, leases, encryption and audit interfaces.` |
| `use_when` | `[]` | `You need an independent open-source secrets service with audited policies and managed encryption keys.; You can operate and secure the storage backend, authentication methods, unsealing and backup procedures.` |
| `avoid_when` | `[]` | `You only need a hosted secrets SaaS and cannot operate secure storage and disaster recovery.; You assume complete compatibility with every HashiCorp Vault Enterprise feature or plugin.` |
| `deployment_models` | `[]` | `self-hosted; container` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-18'` |
| `sources` | `legacy:devopstools_final.md#L980` | `legacy:devopstools_final.md#L980; https://github.com/openbao/openbao; https://github.com/openbao/openbao/blob/main/README.md; https://github.com/openbao/openbao/blob/main/LICENSE; https://github.com/openbao/openbao/releases; https://openbao.org/docs/` |
| `needs_review` | `true` | `false` |
| `repository_url` | ∅ | `https://github.com/openbao/openbao` |
| `documentation_url` | ∅ | `https://openbao.org/docs/` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `MPL-2.0` |

### `teleport` — RETAIN — component-specific licence boundaries

**Primary evidence:** [github.com/gravitational/teleport/blob/master/LICENSE](https://github.com/gravitational/teleport/blob/master/LICENSE) · [github.com/gravitational/teleport/blob/master/api/LICENSE](https://github.com/gravitational/teleport/blob/master/api/LICENSE) · [github.com/gravitational/teleport/blob/master/build.assets/LICENSE-community](https://github.com/gravitational/teleport/blob/master/build.assets/LICENSE-community) · [goteleport.com/docs/](https://goteleport.com/docs/).

| Changed field | Before | After |
|---|---|---|
| `summary` | `Secure access platform for SSH/Kubernetes/databases with OSS core and enterprise editions.` | `Infrastructure access platform for SSH Kubernetes databases and apps with separate AGPL source, Apache API module and restricted Community binary terms.` |
| `use_when` | `Unified, certificate-based access to SSH/K8s/DB with audit logging.` | `You evaluate certificate-backed infrastructure access with identity federation and audit logging.; You can confirm the licence and feature availability of the specific source build Community binary or Enterprise offering.` |
| `avoid_when` | `You only need simple SSH bastion functionality (JumpServer is lighter).` | `You treat AGPL-3.0 source code or Apache-2.0 API-module terms as granting unrestricted Community binary rights.; You need unrestricted distribution or business use but have not evaluated the Community size and revenue limitations.` |
| `deployment_models` | `[]` | `self-hosted; hosted-saas` |
| `maturity` | `unknown` | `established` |
| `verified_on` | `'2026-08-03'` | `'2026-10-18'` |
| `sources` | `legacy:6_Security/README.md#L117; legacy:devopstools_final.md#L1010` | `legacy:6_Security/README.md#L117; legacy:devopstools_final.md#L1010; https://github.com/gravitational/teleport; https://github.com/gravitational/teleport/blob/master/README.md; https://github.com/gravitational/teleport/blob/master/LICENSE; https://github.com/gravitational/teleport/blob/master/api/LICENSE; https://github.com/gravitational/teleport/blob/master/build.assets/LICENSE-community; https://goteleport.com/blog/teleport-community-license/; https://goteleport.com/docs/` |
| `documentation_url` | ∅ | `https://goteleport.com/docs/` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `AGPL-3.0-only` |
| `commercial_offering` | ∅ | `true` |

### `dex` — CLEAR

**Primary evidence:** [github.com/dexidp/dex/blob/master/README.md](https://github.com/dexidp/dex/blob/master/README.md) · [github.com/dexidp/dex/blob/master/LICENSE](https://github.com/dexidp/dex/blob/master/LICENSE) · [github.com/dexidp/dex/releases](https://github.com/dexidp/dex/releases) · [dexidp.io/](https://dexidp.io/).

| Changed field | Before | After |
|---|---|---|
| `summary` | `OpenID Connect identity provider for Kubernetes and beyond.` | `Apache-2.0 OpenID Connect provider and federation broker for applications using external identity connectors.` |
| `use_when` | `As a lightweight OIDC federation layer to bridge upstream IdPs into K8s and GitOps tools.` | `Applications or Kubernetes authentication integrations need federated OIDC tokens from upstream identity providers.` |
| `avoid_when` | `You need a full-featured IAM with user management (use Keycloak).` | `You require a complete employee directory, broad lifecycle governance or full enterprise identity management.; You cannot manage secure connectors, issuer configuration, client secrets and token verification.` |
| `deployment_models` | `[]` | `self-hosted; container` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-18'` |
| `sources` | `legacy:6_Security/README.md#L110; legacy:devopstools_final.md#L1001` | `legacy:6_Security/README.md#L110; legacy:devopstools_final.md#L1001; https://github.com/dexidp/dex; https://github.com/dexidp/dex/blob/master/README.md; https://github.com/dexidp/dex/blob/master/LICENSE; https://github.com/dexidp/dex/releases; https://dexidp.io/` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://dexidp.io/docs/` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

### `jumpserver` — CLEAR

**Primary evidence:** [github.com/jumpserver/jumpserver/blob/dev/README.md](https://github.com/jumpserver/jumpserver/blob/dev/README.md) · [github.com/jumpserver/jumpserver/blob/dev/LICENSE](https://github.com/jumpserver/jumpserver/blob/dev/LICENSE) · [github.com/jumpserver/jumpserver/releases](https://github.com/jumpserver/jumpserver/releases) · [www.jumpserver.com/pricing](https://www.jumpserver.com/pricing).

| Changed field | Before | After |
|---|---|---|
| `summary` | `Open-source bastion host / privileged access management (PAM) platform.` | `Self-hosted privileged access management and bastion platform with GPL-3.0 Community core and distinct paid Enterprise tiers.` |
| `use_when` | `A self-hosted bastion with session recording, RBAC, and asset management.` | `You need centralized controlled access and auditing for supported SSH RDP database or Kubernetes resources.; Community Edition capabilities and asset limits meet requirements or a separately licensed Enterprise plan is approved.` |
| `avoid_when` | `You prefer agent-based zero-trust access (use Teleport/Boundary).` | `You assume paid just-in-time access, enterprise SSO or high-availability features exist in the Community package.; You cannot enforce privileged access controls and protect recordings, audit data and administrative accounts.` |
| `deployment_models` | `[]` | `self-hosted` |
| `license_model` | `oss` | `open-core` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-18'` |
| `sources` | `legacy:6_Security/README.md#L116; legacy:devopstools_final.md#L1009` | `legacy:6_Security/README.md#L116; legacy:devopstools_final.md#L1009; https://github.com/jumpserver/jumpserver; https://github.com/jumpserver/jumpserver/blob/dev/README.md; https://github.com/jumpserver/jumpserver/blob/dev/LICENSE; https://github.com/jumpserver/jumpserver/releases; https://www.jumpserver.com/pricing` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://www.jumpserver.com/docs` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `GPL-3.0-only` |
| `commercial_offering` | ∅ | `true` |

### `openstack-barbican` — CLEAR

**Primary evidence:** [opendev.org/openstack/barbican](https://opendev.org/openstack/barbican) · [github.com/openstack/barbican/blob/master/LICENSE](https://github.com/openstack/barbican/blob/master/LICENSE) · [docs.openstack.org/barbican/latest/](https://docs.openstack.org/barbican/latest/).

| Changed field | Before | After |
|---|---|---|
| `summary` | `OpenStack secrets management.` | `Apache-2.0 OpenStack Key Manager service exposing REST APIs for encrypted secret, key and certificate material with pluggable backends.` |
| `official_url` | `https://wiki.openstack.org/wiki/Barbican` | `https://docs.openstack.org/barbican/latest/` |
| `use_when` | `Running OpenStack and need integrated key/secret management.` | `You operate an OpenStack environment requiring API-managed secrets and encryption-key material.; You can configure access policy, secret-store plugins and the backing service securely.` |
| `avoid_when` | `Outside OpenStack environments.` | `You need a drop-in general-purpose secret store without an OpenStack service deployment.; You assume GitHub is authoritative instead of the canonical OpenDev project.` |
| `deployment_models` | `[]` | `self-hosted` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-18'` |
| `sources` | `legacy:6_Security/README.md#L92; legacy:devopstools_final.md#L981` | `legacy:6_Security/README.md#L92; legacy:devopstools_final.md#L981; https://opendev.org/openstack/barbican; https://github.com/openstack/barbican/blob/master/LICENSE; https://docs.openstack.org/barbican/latest/; https://docs.openstack.org/barbican/latest/api/` |
| `needs_review` | `true` | `false` |
| `repository_url` | ∅ | `https://opendev.org/openstack/barbican` |
| `documentation_url` | ∅ | `https://docs.openstack.org/barbican/latest/` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

### `doppler` — CLEAR

**Primary evidence:** [www.doppler.com](https://www.doppler.com) · [docs.doppler.com/](https://docs.doppler.com/) · [github.com/DopplerHQ/cli/blob/master/README.md](https://github.com/DopplerHQ/cli/blob/master/README.md) · [github.com/DopplerHQ/cli/blob/master/LICENSE](https://github.com/DopplerHQ/cli/blob/master/LICENSE) · [github.com/DopplerHQ/cli/releases](https://github.com/DopplerHQ/cli/releases).

| Changed field | Before | After |
|---|---|---|
| `summary` | `Universal secrets management platform.` | `Hosted Doppler secrets and configuration service with a separately Apache-2.0 licensed CLI for retrieving and injecting configuration.` |
| `use_when` | `A SaaS-first, developer-friendly secrets platform across multiple environments.` | `Your team needs centrally managed secrets shared across development staging and production applications.; You can issue narrowly scoped Doppler service tokens for CI or runtime injection through its separate CLI.` |
| `avoid_when` | `You need self-hosted or air-gapped secret management.` | `You require a self-hosted service independent of the Doppler cloud control plane.; You assume the Apache-2.0 CLI licence also licenses the hosted service or your service tokens need no protection.` |
| `deployment_models` | `[]` | `hosted-saas; cli` |
| `license_model` | `unknown` | `commercial` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-18'` |
| `sources` | `legacy:6_Security/README.md#L89; legacy:devopstools_final.md#L976` | `legacy:6_Security/README.md#L89; legacy:devopstools_final.md#L976; https://www.doppler.com; https://docs.doppler.com/docs/root-configs; https://docs.doppler.com/docs/security-fact-sheet; https://docs.doppler.com/docs/kubernetes-doppler-cli-in-docker; https://github.com/DopplerHQ/cli; https://github.com/DopplerHQ/cli/blob/master/LICENSE; https://github.com/DopplerHQ/cli/releases` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://docs.doppler.com/` |
| `repository_archived` | ∅ | `false` |
| `commercial_offering` | ∅ | `true` |

### `boulder-let-s-encrypt` — CLEAR

**Primary evidence:** [github.com/letsencrypt/boulder/blob/main/README.md](https://github.com/letsencrypt/boulder/blob/main/README.md) · [github.com/letsencrypt/boulder/blob/main/LICENSE.txt](https://github.com/letsencrypt/boulder/blob/main/LICENSE.txt) · [github.com/letsencrypt/boulder/releases](https://github.com/letsencrypt/boulder/releases).

| Changed field | Before | After |
|---|---|---|
| `summary` | `ACME-based certificate authority server powering Let's Encrypt.` | `MPL-2.0 ACME certificate-authority server implementing issuance, validation and revocation for the Lets Encrypt infrastructure.` |
| `use_when` | `You need to run your own ACME CA internally.` | `You build or study the operations of an ACME certificate authority with its registration validation and issuance services.` |
| `avoid_when` | `You just need free public certs (use Let's Encrypt directly via cert-manager or Certbot).` | `You only need to request public TLS certificates as an ACME client; use a client such as Certbot instead.; You cannot operate a security-sensitive multi-service CA backend and required database infrastructure.` |
| `deployment_models` | `[]` | `self-hosted` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-18'` |
| `sources` | `legacy:6_Security/README.md#L97; legacy:devopstools_final.md#L987` | `legacy:6_Security/README.md#L97; legacy:devopstools_final.md#L987; https://github.com/letsencrypt/boulder; https://github.com/letsencrypt/boulder/blob/main/README.md; https://github.com/letsencrypt/boulder/blob/main/LICENSE.txt; https://github.com/letsencrypt/boulder/releases` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://github.com/letsencrypt/boulder/blob/main/README.md` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `MPL-2.0` |

### `mkcert` — RETAIN — release/maintenance evidence inconclusive

**Primary evidence:** [github.com/FiloSottile/mkcert/blob/master/README.md](https://github.com/FiloSottile/mkcert/blob/master/README.md) · [github.com/FiloSottile/mkcert/blob/master/LICENSE](https://github.com/FiloSottile/mkcert/blob/master/LICENSE) · [github.com/FiloSottile/mkcert/releases](https://github.com/FiloSottile/mkcert/releases).

| Changed field | Before | After |
|---|---|---|
| `summary` | `Local SSL certificate generation.` | `BSD-3-Clause CLI creating a locally trusted development CA and TLS certificates; current upstream maintenance remains unconfirmed.` |
| `use_when` | `Instant, trusted localhost TLS certs during development.` | `You need local HTTPS development certificates trusted by your workstation browsers and runtimes.` |
| `avoid_when` | `For production or any non-local use case.` | `You need a production public certificate authority or automated corporate PKI lifecycle.; You cannot protect the generated local rootCA-key.pem private key or require proven ongoing security maintenance.` |
| `deployment_models` | `[]` | `cli` |
| `verified_on` | `'2026-08-03'` | `'2026-10-18'` |
| `sources` | `legacy:6_Security/README.md#L104; legacy:devopstools_final.md#L994` | `legacy:6_Security/README.md#L104; legacy:devopstools_final.md#L994; https://github.com/FiloSottile/mkcert; https://github.com/FiloSottile/mkcert/blob/master/README.md; https://github.com/FiloSottile/mkcert/blob/master/LICENSE; https://github.com/FiloSottile/mkcert/releases` |
| `official_url` | ∅ | `https://mkcert.dev` |
| `documentation_url` | ∅ | `https://github.com/FiloSottile/mkcert#readme` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `BSD-3-Clause` |

### `teller` — RETAIN — ongoing maintenance/support inconclusive

**Primary evidence:** [github.com/tellerops/teller/blob/master/README.md](https://github.com/tellerops/teller/blob/master/README.md) · [github.com/tellerops/teller/blob/master/LICENSE.txt](https://github.com/tellerops/teller/blob/master/LICENSE.txt) · [github.com/tellerops/teller/releases](https://github.com/tellerops/teller/releases).

| Changed field | Before | After |
|---|---|---|
| `summary` | `Run processes with secrets from multiple providers and manage secret scanning, syncing, templating, and redaction.` | `Apache-2.0 Rust CLI for retrieving and injecting secrets from configured external providers; current release support remains inconclusive.` |
| `use_when` | `[]` | `You need to map external secret stores into local or CI processes without checking secrets into source control.` |
| `avoid_when` | `[]` | `You require a standalone secrets database; Teller reads from other providers.; You cannot verify provider compatibility and release maintenance or safely protect local credentials and exported secrets.` |
| `deployment_models` | `[]` | `cli` |
| `verified_on` | `'2026-08-03'` | `'2026-10-18'` |
| `sources` | `legacy:devopstools_final.md#L984` | `legacy:devopstools_final.md#L984; https://github.com/tellerops/teller; https://github.com/tellerops/teller/blob/master/README.md; https://github.com/tellerops/teller/blob/master/LICENSE.txt; https://github.com/tellerops/teller/releases` |
| `documentation_url` | ∅ | `https://github.com/tellerops/teller/blob/master/README.md` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

## Verification against reviewed HEAD

- GitHub Actions [Catalogue quality #304](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/39081944301): **PASS** on `a06425457b71abe0f16ca80a2076600a557f878f` — locked Python (19 pins), Ruff lint/format, **1,002 passed / 4 skipped**, generator `--check` current, catalogue validation passed, `git diff --check` passed.
- [Secret scan #131](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/39081944221): **PASS**; [Plumber CI/CD Security #97](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/39081944220): **PASS**. Four additional checks on the exact head: **CodeQL, Plumber, Analyze (python), Analyze (actions)**, all GitHub reported success; **seven green check runs total**.
- GitHub compare: **14 commits ahead, 0 behind** baseline, 11 changed files (10 generated/implementation files and this report). GitHub PR is mergeable with **no merge conflict**. No review submissions, review threads, or comments were found as of verification.
- The eight affected generated views (README, statistics JSON, IAM category, three role pages, operate/secure pages) are checked by the actual generator in CI, not just manually compared.
- Historic N2a JumpServer review-field protections gained a **narrowly scoped authorized current drift**; the earlier `official_url` decision is preserved. All original external URL exceptions in the six-item reviewed baseline remain untouched.

## Network audit and merge caveats

- **A fresh strict full-catalogue network URL audit has not been run for Wave 16.** The canonical URL set has changed, and strict link outcomes cannot be assumed from CI success; run `python -m scripts.check_links --strict --check-archived --workers 8 --cache-hours 0 --cache tmp/wave16/link-cache.json --json-report tmp/wave16/link-report.json --markdown-report tmp/wave16/link-report.md` before merge **where an authorized runnable network environment is available**. Preserve its dated results, including inconclusive/rate-limited URLs; the six reviewed baseline exceptions are unchanged without new primary evidence.
- The four **RETAIN** records remain `needs_review: true` with precise evidence gaps. The six CLEAR records reflect source-scoped descriptions and licence models, not a guarantee of production suitability or all paid-edition functionality.
- **Ready for human review is not permission to merge.** No merge, tag, release, or issue #121 closure is authorized by this report. The human reviewer can require further URL testing or tighten field evidence before accepting the PR.
