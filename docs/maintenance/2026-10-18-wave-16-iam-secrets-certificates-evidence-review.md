# Wave 16 — IAM, secrets and certificates: primary-source evidence and scope
Date: 2026-10-18
Baseline main: `013b7907be7a100f21c5d417e75dbe9e662f8506`
Issue: https://github.com/goozcena-gnl/devops-tools-catalog/issues/121

## Status

**Partial evidence review, not a completed clearance or ready-to-merge approval.** The ten existing records below are the full fixed scope. The baseline inventory is 1,425 canonical records, 679 review flags, and zero open pull requests. Avoid inventing post-review counts before canonical edits and regeneration.

## Primary-source observations (2026-10-18)

| Canonical ID | Primary evidence inspected | Observations and unresolved boundaries | Planned disposition |
| --- | --- | --- | --- |
| `hashicorp-boundary` | [archived upstream](https://github.com/hashicorp/boundary), [repository README](https://github.com/hashicorp/boundary/blob/main/README.md), [BSL LICENSE](https://github.com/hashicorp/boundary/blob/main/LICENSE) | README explicitly dates **Community Edition archive to 2026-10-08**, with no planned CE security patches, bug fixes or releases; enterprise/HCP development continues. Repository BSL with additional grant; do **not** infer OSI SPDX from licence-model field. Distinguish CE from active product. Also reconcile historical tracker #2 observation. | P0 targeted lifecycle correction; CE archived, product offerings separate |
| `openbao` | [upstream](https://github.com/openbao/openbao), [licence](https://github.com/openbao/openbao/blob/main/LICENSE), [docs](https://openbao.org/docs/) | Nonarchived canonical upstream; GitHub reports MPL-2.0. Currently missing `repository_url` and `documentation_url`. Upstream sources do not imply the HashiCorp Vault commercial licence model. | Candidate for evidence-supported clearance after field-level verification |
| `teleport` | [upstream](https://github.com/gravitational/teleport), [root licence](https://github.com/gravitational/teleport/blob/master/LICENSE), [API licence](https://github.com/gravitational/teleport/blob/master/api/LICENSE), [Community binary licence](https://github.com/gravitational/teleport/blob/master/build.assets/LICENSE-community) | Root AGPL-3.0; API Apache-2.0; Community binary licence has separate organization size/revenue restrictions and security exception; Enterprise differs. Do **not** represent all artifacts as uniformly AGPL or OSI-OSS. | Retain review until distribution boundary and licence-model/clearance evidence fully reconciled |
| `dex` | [upstream](https://github.com/dexidp/dex), [README](https://github.com/dexidp/dex/blob/master/README.md), [official project](https://dexidp.io) | GitHub reports Apache-2.0; federated OIDC provider/connector, not a complete IAM directory. Upstream nonarchived and recently pushed. | Candidate for clearance after release/docs verification |
| `jumpserver` | [upstream](https://github.com/jumpserver/jumpserver), [website](https://www.jumpserver.com) | GitHub reports GPL-3.0 for repository, product PAM access, enterprise capabilities need separate review; nonarchived. | Retain review pending edition-specific source grants and exact capability matrix |
| `openstack-barbican` | [canonical OpenDev](https://opendev.org/openstack/barbican), [GitHub mirror](https://github.com/openstack/barbican), [official docs](https://docs.openstack.org/barbican/latest/), [mirrored LICENSE](https://github.com/openstack/barbican/blob/master/LICENSE) | Apache-2.0, maintained OpenStack secret storage API; GitHub repo self-identifies as **mirror** of code at OpenDev. Existing record lacks canonical repository/documentation URLs. | Candidate for clearance after canonical-source links are recorded |
| `doppler` | [SaaS product](https://www.doppler.com), [CLI upstream](https://github.com/DopplerHQ/cli), [CLI LICENSE](https://github.com/DopplerHQ/cli/blob/master/LICENSE), [docs](https://docs.doppler.com/) | CLI Apache-2.0 does **not** license the managed secret service. Record currently `license_model: unknown`; product is SaaS and CLI is a separate component. | Retain review pending precise service licensing/edition, no inherited OSS claim |
| `boulder-let-s-encrypt` | [upstream](https://github.com/letsencrypt/boulder), [licence](https://github.com/letsencrypt/boulder/blob/main/LICENSE) | GitHub reports MPL-2.0; ACME **CA server**, not certbot/client and not equivalent to issuance from Let's Encrypt. Nonarchived with current activity. | Candidate for clearance after ops/support docs and caveats are checked |
| `mkcert` | [upstream](https://github.com/FiloSottile/mkcert), [README](https://github.com/FiloSottile/mkcert/blob/master/README.md) | BSD-3-Clause; local trusted development CA, **never public/production PKI**; README warns rootCA private key grants interception ability. Repo nonarchived but last pushed 2024-08-13; visibility alone does not prove maintenance. | **RETAIN REVIEW — INCONCLUSIVE** ongoing maintenance |
| `teller` | [upstream](https://github.com/tellerops/teller), [actual LICENSE.txt](https://github.com/tellerops/teller/blob/master/LICENSE.txt) | Apache-2.0; repository uses **LICENSE.txt**, not LICENSE. Nonarchived, last pushed 2026-01-27; check current Rust implementation, providers and release cadence instead of assuming ongoing support. | Retain review pending provider/release/maintenance verification |

## Remaining work before ready-for-human-review

- Update exactly these ten YAML records with supported per-field changes; preserve all legacy sources and stable identifiers. Do not clear `needs_review` based solely on GitHub licence badges and timestamps.
- Include full field-decision ledger (before / after / official URL / rationale) for **all ten**; explicitly document any retained `needs_review: true` cases. Boundary CE archival deserves independent, precise lifecycle representation.
- Regenerate all docs from canonical YAML (`python -m scripts.generate_docs`) and verify (`--check`), not manual edits to generated pages. Ensure README, category, role, lifecycle pages and statistics remain synchronized.
- Run pinned Python 3.12 environment, focused and complete tests, Ruff lint and formatting, catalog validation, review-debt inventory and `git diff --check`. Run strict URL audit with a fresh cache if URLs changed; preserve the six historically reviewed exceptions absent primary evidence for remediation.
- Record exact final SHA, actual before/after counts, required checks, CI and network limitations. Keep PR **draft** until these items are complete; never merge without human decision.

This dated report is a transparent work-in-progress evidence checkpoint, **not** a claim that Wave 16 is finished.


## Canonical follow-up — 2026-10-18 (commit `102ddd02c84194a1e5be20a4e38fa42297d01695`)

Nine additional canonical entries have been edited in `data/tools/iam-secrets-certificates.yaml` and the initial Boundary CE change is retained, making ten selected records touched overall.

| ID | Canonical outcome in working branch | Material edits | Remaining caution |
|---|---|---|---|
| `hashicorp-boundary` | RETAIN (P0 facts updated) | CE archival, separate active commercial editions, official docs and README | Product-versus-community lifecycle, BSL boundary; status kept needs-review |
| `openbao` | CLEAR (provisional pending CI) | Official upstream, MPL-2.0, docs, self-hosting and usage limits | HashiCorp Enterprise plugin parity not claimed |
| `dex` | CLEAR (provisional pending CI) | OIDC connector boundary, Apache-2.0, docs, upstream | Not a complete IAM directory |
| `jumpserver` | CLEAR (provisional pending CI) | Core GPL-3.0-only, open-core/paid tiers, privileged access boundaries | Features of paid modules not inherited |
| `openstack-barbican` | CLEAR (provisional pending CI) | OpenDev canonical upstream, official OpenStack docs and Apache-2.0 | GitHub is an upstream mirror |
| `doppler` | CLEAR (provisional pending CI) | Commercial SaaS vs independent Apache CLI, deployment scope and sources | No SaaS licence inferred from CLI |
| `boulder-let-s-encrypt` | CLEAR (provisional pending CI) | MPL-2.0, ACME CA **server** vs clients, docs, maintenance sources | High-risk production CA deployment not assumed safe |
| `teleport` | RETAIN | Root AGPL-3.0-only, Apache API module, restricted Community binary, deployment source distinctions | No single SPDX for all deliverables; clarification remains necessary |
| `mkcert` | RETAIN | BSD-3-Clause, development CA only, private CA key warning and dated releases | Last observed release v1.4.4 (2022-04-26); maintenance not proved |
| `teller` | RETAIN | Apache-2.0 from LICENSE.txt, Rust provider CLI and available releases | Last observed release v2.0.7 (2024-05-20); ongoing support not proved |

The proposed catalogue review debt would be **679 → 673** if the six provisional clearances survive schema validation and full tests. All ten retain their original stable IDs and legacy source entries.

Official upstream GitHub API (2026-10-18) showed OpenBao v2.7.1 (2026-10-01), Dex v2.46.0 (2026-10-07), JumpServer v5.1.0 (2026-10-15), Boulder v0.20261013.0 (2026-10-13), Doppler CLI 3.77.0 (2026-10-07). Those facts support dated activity, not product-wide security guarantees.

**Blocker / implementation limitation**: remote connector edits do not run the local Python generator or pinned test environment. README/category/role/lifecycle outputs are stale following canonical changes; Ruff, complete pytest, catalogue validator, the review-debt executable and strict network link audit were not run here. No green validation is claimed. The branch and PR must remain **draft**, pending regeneration, tests, CI and a final evidence review. No six-entry reviewed link baseline changes were made.
