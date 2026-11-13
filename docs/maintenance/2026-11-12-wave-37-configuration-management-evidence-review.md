# Wave 37 — Configuration Management evidence review (proposed)

**Review date:** 2026-11-12. **Issue:** https://github.com/goozcena-gnl/devops-tools-catalog/issues/169

**Frozen selection base:** `790acd54903b855e1a0ac5f37686f37f2cd16fed`

**Initial preparation state (historical snapshot; superseded for publication facts by the dated addendum below):** LOCAL PREPARATION ONLY. At drafting time, no Draft PR, branch push, merge, auto-merge, or CI result was claimed. Original CLEAR/RETAIN decisions were proposals pending validation and review. The post-publication addendum records checks on the first published HEAD; it does **not** authorize a merge.

## Exact cohort, primary evidence and disposition

| Canonical ID | Proposed decision | Primary sources / claims verified | Limits and treatment |
|---|---|---|---|
| `cfengine` | **CLEAR** | [Community repository and README](https://github.com/cfengine/core); [community source licence](https://github.com/cfengine/core/blob/master/LICENSE); [vendor edition comparison](https://cfengine.com/community-vs-enterprise-comparison/) | Core repository licence contains GPLv3, additional linking permissions and an optional commercial COSL route. Community and Enterprise have different entitlements. Preserve `open-core`; **do not infer a single product-wide SPDX**. |
| `etckeeper` | **RETAIN** | [Author's project README and GPLv2+ licensing statement](https://etckeeper.branchable.com/README/); [upstream change log with maintainer response dated 2026-10-23](https://etckeeper.branchable.com/recentchanges/) | Git is the default but not the only supported VCS; the author documents GPLv2-or-later. On 2026-10-22, a reporter said that the HTTPS `index.cgi` (cgit) viewer was unavailable. On 2026-10-23, maintainer Joey Hess marked the report **incorrect/done** and clarified that the `git://git.joeyh.name/etckeeper` repository remained accessible, although its cgit web interface was affected by scraper traffic. This review did **not independently test a Git clone** or establish current reachability. Keep `status: needs-review`, `needs_review: true`, the original repository URL and the absence of a new `license_spdx` under the N2a invariant; do not mark the project archived. |
| `kolla-ansible` | **CLEAR** | [OpenStack documentation](https://docs.openstack.org/kolla-ansible/latest/); [primary OpenDev repository](https://opendev.org/openstack/kolla-ansible); [OpenStack release history](https://releases.openstack.org/teams/kolla.html); [GitHub mirror LICENSE](https://github.com/openstack/kolla-ansible/blob/master/LICENSE) | GitHub is a mirror, OpenDev the canonical development origin. Apache-2.0 is supported by the repository. Kolla-Ansible deploys/operates OpenStack components, not a generic Ansible service. |
| `mitogen-for-ansible` | **CLEAR** | [Mitogen for Ansible docs](https://mitogen.networkgenomics.com/ansible_detailed.html); [changelog](https://mitogen.networkgenomics.com/changelog.html); [repo LICENSE](https://github.com/mitogen-hq/mitogen/blob/master/LICENSE); [releases](https://github.com/mitogen-hq/mitogen/releases) | BSD-3-Clause is supported directly. 2026 docs include Ansible 14 support, contradicting an unqualified blanket warning about recent Ansible versions. Third-party strategy plugins have a documented future deprecation risk; retain a targeted compatibility warning. |
| `puppet` | **CLEAR** | [OSS repository and README](https://github.com/puppetlabs/puppet); [OSS LICENSE](https://github.com/puppetlabs/puppet/blob/main/LICENSE); [edition comparison](https://www.puppet.com/resources/puppet-editions-guide); [vendor pricing](https://www.puppet.com/pricing) | Apache-2.0 is attached to the **source**, not a licence to redistribute enterprise binaries. Open Source Puppet, Puppet Core (including commercial and limited developer editions) and Puppet Enterprise are distinct offerings. Preserve broad `open-core` classification and add the commercial boundary. |
| `red-hat-ansible-automation-platform` | **CLEAR** | [Official pricing and subscriptions](https://www.redhat.com/en/technologies/management/ansible/pricing); [deployment options](https://www.redhat.com/en/technologies/management/ansible/ansible-deployment-options); [Red Hat subscription scope](https://access.redhat.com/articles/6057451) | Commercial subscription, distinct from community Ansible/AWX: **no OSS SPDX assigned to this product**. Red Hat distinguishes self-managed deployments, Red Hat-operated **managed applications deployed in the customer cloud**, and vendor-hosted managed services. The canonical `self-hosted` / `hosted-saas` tags describe product-family capabilities, not a claim that every managed deployment runs outside the customer environment. |
| `rudder` | **CLEAR** | [Vendor's canonical README](https://github.com/Normation/rudder/blob/master/README.md); [GPL licence](https://github.com/Normation/rudder/blob/master/LICENSE); [GPL exception for plugins](https://github.com/Normation/rudder/blob/master/LICENSE_EXCEPTION); [plugin access terms](https://docs.rudder.io/reference/9.1/plugins/index.html) | Rudder Core and subscription capabilities differ; some plugins and agents are proprietary. Main-repo GPLv3 and additional permissions do not imply every component's licence. Preserve `open-core` and **do not assign one product-wide SPDX**. |
| `salt` | **CLEAR** | [Salt upstream](https://github.com/saltstack/salt); [upstream LICENSE](https://github.com/saltstack/salt/blob/master/LICENSE); [official about page](https://docs.saltproject.io/en/master/topics/about_salt_project.html) | Apache-2.0 applies to Salt's principal project; embedded third-party components may have separate notices. Do not infer proprietary VMware/Broadcom product entitlements from Salt's repository licence. |

## Proposed field-level changes

- **All eight IDs:** update their descriptions where shown, add only record-specific official evidence to `sources`, and update `verified_on: '2026-11-12'` as the *evidence review date* (not a guarantee of timeless lifecycle status). Original legacy source strings remain unchanged.
- **Seven CLEAR:** move `status: needs-review` → `active` and `needs_review: true` → `false`, supported by currently maintained upstream/vendor evidence; set `repository_archived: false` only for checked GitHub repositories; set self-hosted deployment where directly applicable.
- `cfengine`: add `commercial_offering: true`, docs URL and precise Community/Enterprise summary; retain `license_model: open-core` and no unqualified `license_spdx`.
- `etckeeper`: retain the canonical absence of `license_spdx` to preserve the historical N2a protected-field invariant; document the upstream author's GPL-2.0-or-later statement in the evidence table only. Retain `status: needs-review` and `needs_review: true` pending a separately scoped licence-metadata authorization and the unresolved repository-access review.
- `kolla-ansible`: add `license_spdx: Apache-2.0`, current docs and OpenDev origin as evidence, preserve historical GitHub mirror URL in record.
- `mitogen-for-ansible`: add `license_spdx: BSD-3-Clause` and update the obsolete generic compatibility warning to the documented future strategy-plugin compatibility risk.
- `puppet`: add `license_spdx: Apache-2.0` for the upstream core, `commercial_offering: true`, while preserving `open-core`.
- `red-hat-ansible-automation-platform`: change `license_model: unknown` → `commercial`, set `commercial_offering: true` and supported deployment models; **no SPDX added**.
- `rudder`: add `commercial_offering: true`, self-hosted deployment and exact primary evidence, keep exception-aware SPDX undetermined.
- `salt`: add `license_spdx: Apache-2.0` and confirmed repository metadata.
- **Maturity:** leave `maturity: unknown` unchanged across the cohort; the evidence above does not require a subjective maturity upgrade.

## Isolation and accounting

- Exactly eight selected IDs, **no additional tools, additions, removals or category changes**.
- The other ten raw blocks in `data/tools/configuration-management.yaml` are required to match the frozen base **byte-for-byte**.
- All eight original `legacy:` source strings are required to remain **byte-for-byte identical** and in their original order.
- No baseline URL waivers, security or CI policy changes. PR #132 remains unrelated and untouched.
- Baseline inventory: **1,425 canonical / 30 categories / 867 active / 544 needs-review / 69 unknown licence model / 173 commercial licence model**.
- **Proposed** after seven CLEAR and one RETAIN (not actual until generated and validated): **1,425 canonical / 30 categories / 874 active / 537 needs-review / 68 unknown licence model / 174 commercial licence model**.

## Validation gates (not presumed PASS)

1. Preflight: clean separate worktree, exact `HEAD` and `origin/main` equal to frozen main SHA, canonical blob equal to `d682ecbdab4f2678edb1d36268a167495b1ccbdb`.
2. Local guard script: exactly eight changed blocks, ten byte-identical out-of-cohort blocks, all legacy strings preserved and no duplicate IDs; no invalid or unexpected change paths.
3. Generator: `python -m scripts.generate_docs`, then `python -m scripts.generate_docs --check`; compare the resulting `docs/catalog-statistics.json` with the proposed inventory.
4. `python -m scripts.validate_catalog`, `python -m scripts.review_debt --format json`, `python -m ruff check scripts tests`, `python -m ruff format --check scripts tests`, `python -m pytest`, `python -m pip check`, and `git diff --check`.
5. Human diff review, then **separate publication authorization** for commit/push/Draft PR. After publication require **exact-head CI**, independent strict Full link audit with `blocking_new: 0`, and another human review. **No Ready, merge or auto-merge**.

This report does not certify that any upstream URL was reachable from GitHub Actions or that every tool's current operational behaviour has been tested. The evidence is provenance-backed but integration checks are pending.

---

## 2026-11-12 — Post-publication validation checkpoint (first published HEAD)

This checkpoint **supersedes the initial “LOCAL PREPARATION ONLY” wording for publication status** while preserving the preparation history above.

- **Draft PR:** [#170](https://github.com/goozcena-gnl/devops-tools-catalog/pull/170), associated with [issue #169](https://github.com/goozcena-gnl/devops-tools-catalog/issues/169). At this checkpoint it was **OPEN / Draft**, not merged.
- **First published HEAD:** `0b2bdb15feed4e9ddf98c25a62e0e4de546c6198`; base `790acd54903b855e1a0ac5f37686f37f2cd16fed`.
- **First-HEAD CI/security checks:** Seven successful checks: `validate`, `gitleaks`, `Plumber audit`, `Analyze (actions)`, `Analyze (python)`, CodeQL scanning and Plumber scanning.
- **Strict full link audit:** [run 43241365997](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/43241365997) completed successfully on the first HEAD with `blocking_new: 0`, `blocking_known: 6`, `strict_result: PASS`; the `link-audit-report` artifact was produced. Historical known blockers remain tracked in [issue #2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2); no exception was waived.
- **Local checks reported PASS before publication:** documentation generation/check, catalogue validation, review-debt inventory, Ruff lint/format, targeted N2a regression, full pytest, pip check, Wave 37 scope guard and whitespace verification.
- **First-HEAD inventory:** 1,425 canonical records, 30 categories, 874 active, 537 needs-review, 68 unknown licence models, 174 commercial licence models. Exactly eight cohort records changed, ten out-of-cohort records unchanged and original `legacy:` strings preserved; disposition **7 CLEAR / 1 RETAIN (`etckeeper`)**.
- **Independent review follow-up:** This documentation-only correction addresses the reviewer findings about the etckeeper maintainer response, stale publication status and Red Hat deployment-model boundaries. It is not human maintainer approval.

**SHA scope:** the checks above apply only to the **first published HEAD**. This corrective commit changes the PR HEAD: repeat all applicable CI validations on the new SHA and run a new strict full link audit before any Ready-for-Review or merge decision. Keep the PR **Draft**; no merge, auto-merge or issue closure is authorized.
