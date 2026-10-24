# Wave 23 — GitOps, Continuous Delivery & Release Promotion evidence review

Date: **2026-10-24**. Selection tracker: [issue #136](https://github.com/goozcena-gnl/devops-tools-catalog/issues/136). Baseline main: `b86cde61789b4d85abc3f55a25c50a4bff8e733c`.

> **INITIAL DOCUMENTARY TRIAGE ONLY. 0/10 CLEARED; 10 PENDING.** This report records independently inspected official repository/tag evidence and unresolved work. No canonical catalogue record has been changed. Do not infer final SPDX grants, operational safety or support from a GitHub license label alone.

## Baseline, scope and invariants

- Canonical inventory from generated statistics: **1,425** records, **779 active**, **632 needs-review**; 30 category YAML files.
- Single canonical review file: `data/tools/cd-gitops-release-promotion.yaml`, containing **31** records, ten of which are `status: needs-review` **and** `needs_review: true`.
- Ten fixed IDs: `argocd-agent`, `caddy`, `flux9s`, `gitops-bridge`, `kamal`, `kubechecks`, `porter`, `uncloud`, `waypoint`, `weaveworks-gitops`.
- The category includes differently scoped web servers, SSH deploy tools and Kubernetes GitOps UIs; classification is historical and must not be silently reassigned.
- The six historical strict-link exceptions belong to [issue #2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2), which must remain **OPEN**. Exact baseline `config/link-audit-baseline.json` blob SHA `a834e2af711693def40078a55e31dfeb29bee2c7` must remain unchanged.
- The four post-merge [Catalogue quality](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40018966506), [Secret scan](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40018966599), [Plumber](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40018966466), [CodeQL](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40018965977) runs on pinned main passed. They do **not** pre-approve Wave 23.

## Tagged upstream evidence — initial pass

These first-party files were read at the specified release tags where available. Source **LICENSE** existence can support a source repository grant but does not automatically license all dependencies, hosted services, extensions, historical versions or product tiers.

| Canonical ID | Evidence read | Preliminary finding | Critical remaining questions |
|---|---|---|---|
| `argocd-agent` | [v0.10.0 LICENSE](https://github.com/argoproj-labs/argocd-agent/blob/v0.10.0/LICENSE), [v0.10.0 README](https://github.com/argoproj-labs/argocd-agent/blob/v0.10.0/README.md), [release](https://github.com/argoproj-labs/argocd-agent/releases/tag/v0.10.0) | Apache-2.0 tagged source; v0.10.0 published **2026-08-26**; repository activity 2026-10-21 and not archived. | Confirm project status and Argo CD vs agent identity; versioned feature support, principal/agent auth and RBAC. Recent push ≠ GA or guaranteed maintenance. |
| `caddy` | [v2.11.7 LICENSE](https://github.com/caddyserver/caddy/blob/v2.11.7/LICENSE), [release](https://github.com/caddyserver/caddy/releases/tag/v2.11.7), [Caddy docs](https://caddyserver.com/docs/) | Apache-2.0 tagged source; v2.11.7 released **2026-10-03**, repository updated 2026-10-23. Web server/reverse proxy rather than GitOps reconciliation controller. | Document web proxy, automatic HTTPS, modules and commercial build boundary; category placement must not silently change. |
| `flux9s` | [v1.4.2 LICENSE](https://github.com/dgunzy/flux9s/blob/v1.4.2/LICENSE), [v1.4.2 README](https://github.com/dgunzy/flux9s/blob/v1.4.2/README.md), [release](https://github.com/dgunzy/flux9s/releases/tag/v1.4.2) | Apache-2.0 tagged source; v1.4.2 published **2026-10-21**; distinguishes Flux terminal UI from controller. | Confirm RBAC required for read/write operations and whether binaries, packages and integrations change source licence assumptions. |
| `gitops-bridge` | [v0.0.1 LICENSE](https://github.com/gitops-bridge-dev/gitops-bridge/blob/v0.0.1/LICENSE), [v0.0.1 README](https://github.com/gitops-bridge-dev/gitops-bridge/blob/v0.0.1/README.md), [repository](https://github.com/gitops-bridge-dev/gitops-bridge) | Apache-2.0 tagged source and 2023 example release; repo last pushed **2024-08-08**. README describes a community pattern, not a standalone controller. Existing canonical record already says Apache-2.0 but remains under review. | Check project ownership, current compatibility/support, whether archival or uncertain maintenance changes status, and sample/solution dependency boundaries. |
| `kamal` | [v2.12.0 MIT-LICENSE](https://github.com/basecamp/kamal/blob/v2.12.0/MIT-LICENSE), [README](https://github.com/basecamp/kamal/blob/v2.12.0/README.md), [release](https://github.com/basecamp/kamal/releases/tag/v2.12.0) | The named `MIT-LICENSE` file (not `LICENSE`) has MIT grant. v2.12.0 published **2026-06-18**, repo updated 2026-10-21. SSH/container deployment, not Kubernetes-native GitOps. | Establish authentication/registry/rollback/zero-downtime constraints, versioned features, software vs commercial offering boundary. |
| `kubechecks` | [v3.5.1 LICENSE](https://github.com/zapier/kubechecks/blob/v3.5.1/LICENSE), [v3.5.1 README](https://github.com/zapier/kubechecks/blob/v3.5.1/README.md), [release](https://github.com/zapier/kubechecks/releases/tag/v3.5.1) | MPL-2.0 tagged source, v3.5.1 released **2026-10-19**, repo updated 2026-10-22. This is a PR validation tool, not a reconciliation controller. | Assess Argo CD integration, API/RBAC scope, GitHub credentials, pre-merge blocking vs informational checks, potential SaaS components. |
| `porter` | [porter-dev organization](https://github.com/porter-dev), [historic catalogue official URL](https://github.com/porter-dev) | Catalogue currently describes a Kubernetes PaaS and has **no canonical repository_url**. Candidate `porter-dev/porter` returned 404. | **Identity blocker**: do NOT substitute [getporter/porter](https://github.com/getporter/porter), which is a different CNAB packaging tool. Find authoritative company/product source, licence model, maintenance and exact repo, or retain review. |
| `uncloud` | [v0.21.0 LICENSE](https://github.com/psviderski/uncloud/blob/v0.21.0/LICENSE), [v0.21.0 README](https://github.com/psviderski/uncloud/blob/v0.21.0/README.md), [release](https://github.com/psviderski/uncloud/releases/tag/v0.21.0) | Apache-2.0 tagged source; v0.21.0 published **2026-10-02**, repo updated 2026-10-14. Docker-host deployment tool without Kubernetes. | Security, secret/access management, cluster networking, persistence, operational maturity, product vs external components. |
| `waypoint` | [v0.11.4 LICENSE](https://github.com/hashicorp/waypoint/blob/v0.11.4/LICENSE), [main README](https://github.com/hashicorp/waypoint/blob/main/README.md), [releases](https://github.com/hashicorp/waypoint/releases) | **High priority:** original Waypoint Community Edition repository is **archived**; latest published release v0.11.4 on **2023-08-09**. Its current official README explicitly says Community Edition is **no longer actively maintained**. Tagged v0.11.4 LICENSE contains **MPL-2.0**, which must not be confused with later HashiCorp BSL-era products or HCP Waypoint. | Decide archival/lifecycle and version-scoped licence precisely. Differentiate archived CE from distinct HCP Waypoint offering; never mark original CE active from HCP docs. |
| `weaveworks-gitops` | [v0.39.1-rc.1 LICENSE](https://github.com/weaveworks/weave-gitops/blob/v0.39.1-rc.1/LICENSE), [v0.39.1-rc.1 README](https://github.com/weaveworks/weave-gitops/blob/v0.39.1-rc.1/README.md), [repo](https://github.com/weaveworks/weave-gitops) | Apache-2.0 tagged source; recent tag is a **prerelease** (2026-01-25), repository updated 2026-10-23. Unarchived and push activity do NOT establish stable support or Weaveworks commercial continuity. | Verify project's community-maintenance transition, latest stable release, operator security/Flux compatibility, old Enterprise boundaries and actual maintainer statements. |

## Decisions (not yet approved)

| ID | Decision | Status |
|---|---|---|
| `argocd-agent` | PENDING | Keep original review flag |
| `caddy` | PENDING | Keep original review flag |
| `flux9s` | PENDING | Keep original review flag |
| `gitops-bridge` | PENDING | Keep original review flag |
| `kamal` | PENDING | Keep original review flag |
| `kubechecks` | PENDING | Keep original review flag |
| `porter` | PENDING | Keep original review flag |
| `uncloud` | PENDING | Keep original review flag |
| `waypoint` | PENDING | Keep original review flag |
| `weaveworks-gitops` | PENDING | Keep original review flag |

**0 CLEAR, 10 PENDING.** These are preliminary facts, not verified final catalogue field decisions.

## Required follow-up before any clearance or merge

1. Study official tagged docs/feature boundaries, project licensing, historical vs current product identities, lifecycle, and source accuracy independently for each of the ten IDs. Document a **CLEAR** or **RETAIN REVIEW** per record, with unresolved facts and direct versioned evidence.
2. Restrict canonical YAML changes to exactly these ten existing IDs in **one** file, `data/tools/cd-gitops-release-promotion.yaml`, retaining every old legacy source and identity. Treat Caddy's taxonomy as a separate decision, preserve the Porter PaaS identity, and do not infer an exact SPDX grant from generic unversioned files or misleading GitHub metadata.
3. Record field-level before/after rows for every changed canonical field, including `sources`, repository URLs, licences, status, flags, archived state and versioned operational constraints. Do not target an artificial clearance quota.
4. Use a clean full checkout with isolated locked Python 3.12. Run official docs generator `python -m scripts.generate_docs` and `--check`, `python -m pip check`, locked constraint verification, Ruff lint/format, full pytest, `python -m scripts.validate_catalog`, and `git diff --check`. Commit only expected generated outputs. No generated file hand-edits.
5. On the final SHA, require all GitHub CI security/quality checks green plus independent Codex/human P1/P2 review. Only then run a new **strict Full link audit** on the same final SHA, requiring `strict_result: PASS`, `blocking_new: 0`, and six historic URL/classification pairs unchanged. Preserve baseline file blob `a834e2af711693def40078a55e31dfeb29bee2c7` and [issue #2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2) OPEN.
6. Draft PR must remain **unmerged** until explicit human approval. No auto-merge, protection bypass, release, tag, changes to unrelated work or issue closure before post-merge verification.

**This first pass changes one evidence document only. No canonical tool record, generated view or audit baseline was modified.**

## Second pass — provisional Wave 23 decision ledger (2026-10-24)

**6 PROVISIONAL CLEAR / 4 RETAIN REVIEW**, pending official generator, Python 3.12 full tests, independent P1/P2 reviewer validation and final-head link audit. Provisional CLEAR: `argocd-agent`, `caddy`, `flux9s`, `kamal`, `kubechecks`, `uncloud`. RETAIN REVIEW: `gitops-bridge`, `porter`, `waypoint`, `weaveworks-gitops`. No final merge authorization is implied.

- **Argo CD Agent:** versioned Apache-2.0 licence and multi-cluster authenticated mTLS project README justify the source attribution, NOT any assumed GA or privilege-free deployment.
- **Caddy:** Apache-2.0 tagged source is documented; scope remains a reverse proxy, not a GitOps controller; historical catalogue taxonomy is preserved pending a separate approved taxonomy review.
- **flux9s:** Apache-2.0 tagged source, Flux UI read/write actions and Kubernetes RBAC constraints clarified; not the Flux controller.
- **Kamal:** MIT grant specifically in tagged `MIT-LICENSE`; SSH/Docker and kamal-proxy operational distinctions preserved.
- **KubeChecks:** tagged MPL-2.0 source and GitOps pre-merge review purpose supported; API/cluster credentials still demand deployment-specific least privilege.
- **Uncloud:** tagged Apache-2.0 source, no Kubernetes requirement, and Docker-host operational privileges clarified.
- **GitOps Bridge retained:** example project with tagged Apache-2.0 known, but independently verified current maintenance and tested compatibility remain insufficient; do not call it a supported controller.
- **Porter retained:** product is historical Porter Kubernetes PaaS; `porter-dev/porter` is not an accessible documented canonical source and **getporter/porter is a different CNAB project**. Commercial/source model remains unverified.
- **Waypoint retained:** HashiCorp CE source repo is archived, and official README explicitly states active maintenance ended. The v0.11.4 **MPL-2.0** tagged grant does not authorize applying an HCP Waypoint product/licence to CE; the existing generic `source-available` model remains under review.
- **Weave GitOps retained:** tagged Apache-2.0 source is verified; prerelease activity is not adequate proof of stable support or organizational continuity.

**Expected inventory after official generation (not yet verified):** 1,425 canonical, **785 active**, **626 needs-review**. The historical `#2` six URL blockers and baseline must remain unchanged. Other canonical IDs must remain unchanged.

### Full changed-field matrix — pinned main to current Draft

| ID | Field | Before | Proposed after |
|---|---|---|---|
| `argocd-agent` | `summary` | Agent-based architecture for ArgoCD to manage remote clusters. | Agent and principal components for managing remote Argo CD clusters over authenticated mTLS connections; a separate project from Argo CD core. |
| `argocd-agent` | `avoid_when` |  ⏎   - '* Your clusters are reachable from ArgoCD and the standard model works fine.' |  ⏎   - '* Your clusters are reachable from ArgoCD and the standard model works fine.' ⏎   - Do not assume Argo CD core and argocd-agent share release maturity or Kubernetes privileges; verify principal/agent mTLS and RBAC. |
| `argocd-agent` | `status` | needs-review | active |
| `argocd-agent` | `verified_on` | '2026-08-03' | '2026-10-24' |
| `argocd-agent` | `sources` |  ⏎   - legacy:3_CI-CD-Automation/README.md#L136 ⏎   - legacy:devopstools_final.md#L386 |  ⏎   - legacy:3_CI-CD-Automation/README.md#L136 ⏎   - legacy:devopstools_final.md#L386 ⏎   - https://github.com/argoproj-labs/argocd-agent/blob/v0.10.0/LICENSE ⏎   - https://github.com/argoproj-labs/argocd-agent/blob/v0.10.0/README.md ⏎   - https://github.com/argoproj-labs/argocd-agent/releases/tag/v0.10.0 |
| `argocd-agent` | `needs_review` | true | false |
| `argocd-agent` | `repository_url` | (absent) | https://github.com/argoproj-labs/argocd-agent |
| `argocd-agent` | `repository_archived` | (absent) | false |
| `argocd-agent` | `license_spdx` | (absent) | Apache-2.0 |
| `caddy` | `summary` | Extensible web server and reverse proxy with automatic HTTPS. | Extensible web server, reverse proxy and HTTPS endpoint with automatic certificate management; not a GitOps reconciliation controller. |
| `caddy` | `avoid_when` | [] |  ⏎   - You need GitOps reconciliation; Caddy serves and proxies traffic rather than managing Kubernetes application state. |
| `caddy` | `status` | needs-review | active |
| `caddy` | `verified_on` | '2026-08-03' | '2026-10-24' |
| `caddy` | `sources` |  ⏎   - legacy:devopstools_final.md#L1131 |  ⏎   - legacy:devopstools_final.md#L1131 ⏎   - https://github.com/caddyserver/caddy/blob/v2.11.7/LICENSE ⏎   - https://github.com/caddyserver/caddy/releases/tag/v2.11.7 ⏎   - https://caddyserver.com/docs/ |
| `caddy` | `needs_review` | true | false |
| `caddy` | `repository_archived` | (absent) | false |
| `caddy` | `license_spdx` | (absent) | Apache-2.0 |
| `flux9s` | `summary` | K9s-inspired terminal UI for Flux resources, controller health, and GitOps state. | Terminal UI for inspecting Flux GitOps controllers and Kubernetes workloads, with RBAC-gated cluster operations. |
| `flux9s` | `avoid_when` | [] |  ⏎   - You expect a Flux controller or assume the terminal UI can change cluster resources without Kubernetes RBAC. |
| `flux9s` | `status` | needs-review | active |
| `flux9s` | `verified_on` | '2026-08-03' | '2026-10-24' |
| `flux9s` | `sources` |  ⏎   - legacy:devopstools_final.md#L392 |  ⏎   - legacy:devopstools_final.md#L392 ⏎   - https://github.com/dgunzy/flux9s/blob/v1.4.2/LICENSE ⏎   - https://github.com/dgunzy/flux9s/blob/v1.4.2/README.md ⏎   - https://github.com/dgunzy/flux9s/releases/tag/v1.4.2 |
| `flux9s` | `needs_review` | true | false |
| `flux9s` | `repository_archived` | (absent) | false |
| `flux9s` | `license_spdx` | (absent) | Apache-2.0 |
| `gitops-bridge` | `avoid_when` |  ⏎   - Do not treat the pattern as an installable platform or assume completed Flux integration; verify present ⏎     maintenance and example compatibility before production adoption. |  ⏎   - Do not treat the pattern as an installable platform or assume completed Flux integration; verify present ⏎   - You require an independently maintained and fully supported GitOps controller; this project publishes examples and maintenance is not established. ⏎     maintenance and example compatibility before production adoption. |
| `gitops-bridge` | `verified_on` | '2026-10-13' | '2026-10-24' |
| `gitops-bridge` | `sources` |  ⏎   - legacy:3_CI-CD-Automation/README.md#L148 ⏎   - legacy:devopstools_final.md#L393 ⏎   - https://github.com/gitops-bridge-dev/gitops-bridge ⏎   - https://github.com/gitops-bridge-dev/gitops-bridge/blob/main/README.md ⏎   - https://github.com/gitops-bridge-dev/gitops-bridge/blob/main/LICENSE ⏎   - https://github.com/gitops-bridge-dev/gitops-bridge/commits/main/ ⏎   - https://github.com/gitops-bridge-dev/gitops-bridge/releases |  ⏎   - legacy:3_CI-CD-Automation/README.md#L148 ⏎   - legacy:devopstools_final.md#L393 ⏎   - https://github.com/gitops-bridge-dev/gitops-bridge ⏎   - https://github.com/gitops-bridge-dev/gitops-bridge/blob/main/README.md ⏎   - https://github.com/gitops-bridge-dev/gitops-bridge/blob/main/LICENSE ⏎   - https://github.com/gitops-bridge-dev/gitops-bridge/commits/main/ ⏎   - https://github.com/gitops-bridge-dev/gitops-bridge/releases ⏎   - https://github.com/gitops-bridge-dev/gitops-bridge/blob/v0.0.1/LICENSE ⏎   - https://github.com/gitops-bridge-dev/gitops-bridge/releases/tag/v0.0.1 |
| `kamal` | `summary` | Deploy web apps anywhere with zero-downtime deploys over SSH using containers. | Deploy and roll containerized web applications onto remote servers over SSH using Kamal and kamal-proxy, without requiring Kubernetes. |
| `kamal` | `avoid_when` | [] |  ⏎   - You specifically need Kubernetes-native reconciliation or do not control SSH and Docker credentials on deployment hosts. |
| `kamal` | `status` | needs-review | active |
| `kamal` | `verified_on` | '2026-08-03' | '2026-10-24' |
| `kamal` | `sources` |  ⏎   - legacy:devopstools_final.md#L1134 |  ⏎   - legacy:devopstools_final.md#L1134 ⏎   - https://github.com/basecamp/kamal/blob/v2.12.0/MIT-LICENSE ⏎   - https://github.com/basecamp/kamal/blob/v2.12.0/README.md ⏎   - https://github.com/basecamp/kamal/releases/tag/v2.12.0 |
| `kamal` | `needs_review` | true | false |
| `kamal` | `repository_archived` | (absent) | false |
| `kamal` | `license_spdx` | (absent) | MIT |
| `kubechecks` | `summary` | Pre-merge validation for Kubernetes GitOps changes. | Pre-merge Kubernetes GitOps application change review that integrates with Kubernetes and Argo CD rather than reconciling deployments itself. |
| `kubechecks` | `avoid_when` |  ⏎   - '* You already have CI-based validation or don''t do PR-based GitOps.' |  ⏎   - '* You already have CI-based validation or don''t do PR-based GitOps.' ⏎   - Your review bot must have no access to cluster or GitOps API credentials; evaluate the required Kubernetes and Argo CD permissions. |
| `kubechecks` | `status` | needs-review | active |
| `kubechecks` | `verified_on` | '2026-08-03' | '2026-10-24' |
| `kubechecks` | `sources` |  ⏎   - legacy:3_CI-CD-Automation/README.md#L152 ⏎   - legacy:devopstools_final.md#L395 |  ⏎   - legacy:3_CI-CD-Automation/README.md#L152 ⏎   - legacy:devopstools_final.md#L395 ⏎   - https://github.com/zapier/kubechecks/blob/v3.5.1/LICENSE ⏎   - https://github.com/zapier/kubechecks/blob/v3.5.1/README.md ⏎   - https://github.com/zapier/kubechecks/releases/tag/v3.5.1 |
| `kubechecks` | `needs_review` | true | false |
| `kubechecks` | `repository_url` | (absent) | https://github.com/zapier/kubechecks |
| `kubechecks` | `repository_archived` | (absent) | false |
| `kubechecks` | `license_spdx` | (absent) | MPL-2.0 |
| `porter` | `summary` | PaaS for deploying apps to Kubernetes. | Porter cloud platform for deploying applications into user-owned Kubernetes clusters; current commercial and source-licence boundaries require review. |
| `porter` | `avoid_when` |  ⏎   - You don't need Kubernetes or prefer lower-level Helm/ArgoCD control. |  ⏎   - You don't need Kubernetes or prefer lower-level Helm/ArgoCD control. ⏎   - You require verified fully open-source code or confuse Porter PaaS with the unrelated getporter/porter CNAB tool. |
| `porter` | `verified_on` | '2026-08-03' | '2026-10-24' |
| `porter` | `sources` |  ⏎   - legacy:7_Development-Collaboration/README.md#L93 ⏎   - legacy:devopstools_final.md#L1137 |  ⏎   - legacy:7_Development-Collaboration/README.md#L93 ⏎   - legacy:devopstools_final.md#L1137 ⏎   - https://github.com/porter-dev ⏎   - https://www.porter.run/ ⏎   - https://www.porter.run/pricing |
| `uncloud` | `summary` | Multi-node Docker Compose for running containerized apps in production without Kubernetes. | Deploy and operate containerized workloads across Docker hosts with service discovery and HTTPS ingress, without a Kubernetes control plane. |
| `uncloud` | `avoid_when` | [] |  ⏎   - You need Kubernetes APIs or a mature managed control plane; evaluate host SSH access, Docker privileges and storage/network maturity. |
| `uncloud` | `status` | needs-review | active |
| `uncloud` | `verified_on` | '2026-08-03' | '2026-10-24' |
| `uncloud` | `sources` |  ⏎   - legacy:devopstools_final.md#L1139 |  ⏎   - legacy:devopstools_final.md#L1139 ⏎   - https://github.com/psviderski/uncloud/blob/v0.21.0/LICENSE ⏎   - https://github.com/psviderski/uncloud/blob/v0.21.0/README.md ⏎   - https://github.com/psviderski/uncloud/releases/tag/v0.21.0 |
| `uncloud` | `needs_review` | true | false |
| `uncloud` | `repository_archived` | (absent) | false |
| `uncloud` | `license_spdx` | (absent) | Apache-2.0 |
| `waypoint` | `summary` | Application build, deploy, and release workflow platform from HashiCorp. | Archived HashiCorp Waypoint Community Edition build, deploy and release CLI; distinct from the later HCP Waypoint SaaS platform. |
| `waypoint` | `avoid_when` | [] |  ⏎   - You require a supported Waypoint Community Edition; HashiCorp ended active development and archived the original repository. |
| `waypoint` | `verified_on` | '2026-08-03' | '2026-10-24' |
| `waypoint` | `sources` |  ⏎   - legacy:devopstools_final.md#L1140 |  ⏎   - legacy:devopstools_final.md#L1140 ⏎   - https://github.com/hashicorp/waypoint/blob/v0.11.4/LICENSE ⏎   - https://github.com/hashicorp/waypoint/blob/main/README.md ⏎   - https://www.hashicorp.com/en/blog/a-new-vision-for-hcp-waypoint |
| `waypoint` | `repository_url` | (absent) | https://github.com/hashicorp/waypoint |
| `waypoint` | `repository_archived` | (absent) | true |
| `weaveworks-gitops` | `summary` | GitOps automation for Kubernetes and cloud-native apps. | Flux-based Kubernetes GitOps management UI; the project advertises a transition to community stewardship and maintenance support remains under review. |
| `weaveworks-gitops` | `avoid_when` |  ⏎   - '* Weaveworks has shut down; consider long-term maintenance risks.' |  ⏎   - '* Weaveworks has shut down; consider long-term maintenance risks.' ⏎   - You need a documented enterprise maintenance commitment; community stewardship and repository activity alone do not prove support. |
| `weaveworks-gitops` | `verified_on` | '2026-08-03' | '2026-10-24' |
| `weaveworks-gitops` | `sources` |  ⏎   - legacy:3_CI-CD-Automation/README.md#L154 ⏎   - legacy:devopstools_final.md#L397 |  ⏎   - legacy:3_CI-CD-Automation/README.md#L154 ⏎   - legacy:devopstools_final.md#L397 ⏎   - https://github.com/weaveworks/weave-gitops/blob/v0.39.1-rc.1/LICENSE ⏎   - https://github.com/weaveworks/weave-gitops/releases/tag/v0.39.1-rc.1 ⏎   - https://github.com/weaveworks/weave-gitops |
| `weaveworks-gitops` | `repository_archived` | (absent) | false |

### Outstanding preparation and stop gates

The canonical YAML update was committed through GitHub, **without a local full-checkout build or official regeneration**. The Draft branch is not merge-ready. Run the official generator in a clean checkout, commit only its actual changed views, run locked Python 3.12 + Ruff + full pytest + validator + whitespace checks. If `test_generation_is_deterministic_and_current` fails in CI, do not waive it; synchronize the generated files. Re-review all source and license fields at the final SHA. Only after every CI check passes and independent review finds no unaddressed P1/P2, dispatch the strict link audit on that exact SHA; expect `strict_result: PASS`, `blocking_new: 0`, six historical classifications unchanged. Keep issue #2 and #136 open and PR #137 Draft until final verification. No merge, auto-merge, tag, release or protection bypass.

## Windows full-test regression repair (2026-10-24)

The first full Windows pytest attempt had **838 passed, 4 skipped, 2 failed and 165 setup errors**. The 165 setup errors all share a missing parent directory for the externally selected `--basetemp` path (`%LOCALAPPDATA%/DevOpsTools/pytest-wave23`): this is a test-run invocation setup error, not evidence of 165 source regressions. The rerun must first create the parent directory via `New-Item -ItemType Directory -Force`; keep pytest's generated files outside the git checkout.

Two actual catalogue-dependent test failures identified and corrected without disabling any assertion:

1. `tests/test_wave11_evidence_review.py::test_gitops_bridge_keeps_precise_maintenance_review_debt`: a multi-line YAML `avoid_when` scalar was accidentally split by an inserted list item. Restored the exact historical phrase **`verify present maintenance`** and moved the Wave 23 caution to a separate list element. This is a corrected representation of the original Wave 11 accepted value, not a waiver.
2. `tests/test_v022_n1a_access_retry.py::test_n1a_current_state_preserves_owned_decisions`: the Wave 23 tagged upstream evidence explicitly supplies `argocd-agent` `repository_url`, `license_spdx`, `status`, and `needs_review`, superseding N1a current-state protected fields. Added **only those four field-specific pairs** to the existing `N1A_CURRENT_STATE_SUPERSESSIONS` allowlist, matching the established Helmfile/mcp-server-kubernetes pattern. The pinned N1a result, historical decisions, core fixture comparisons and all other guarded fields remain unchanged. References: [tagged source grant](https://github.com/argoproj-labs/argocd-agent/blob/v0.10.0/LICENSE), [upstream release](https://github.com/argoproj-labs/argocd-agent/releases/tag/v0.10.0), [agent README](https://github.com/argoproj-labs/argocd-agent/blob/v0.10.0/README.md).

The previously stated blanket condition that no tests were changed is **superseded solely by the four-line, evidence-linked N1a allowlist extension above**. No historic N1a SHA, test expectations or historical evidence ledger was rewritten. This correction does not approve merge: the official generator, full clean tests, CI, independent review and strict link audit are still mandatory.

## Follow-up: frozen N1a exact-set contract (2026-10-24)

The subsequent full local run exposed three remaining failures: **998 passed, 8 skipped, 3 failed**. Two were N1a protections; the third was the stale generated GitOps category page after the `avoid_when` repair. The original N1a allowlist must remain byte-for-byte equivalent at the set level because `test_deferred_catalogue_corrections.py::test_n1a_supersession_is_exact_and_does_not_weaken_other_guards` deliberately pins it. The earlier extension of that original set was therefore replaced with a **separate eight-pair `WAVE23_CURRENT_STATE_SUPERSESSIONS`** covering exactly `argocd-agent` and `kubechecks` (`repository_url`, `license_spdx`, `status`, `needs_review` for each), with a new exact-set regression test and an explicit negative assertion on an unrelated `license_model` change. The N1a historical allowlist, original pinned SHAs, and all other protections are unchanged. This replaces the previous narrower Argo-only exception described above.

**Generation is still required after these changes**: run `python -m scripts.generate_docs` again, then `--check`, and rerun all tests with an existing external pytest parent directory. Do not skip `test_generation_is_deterministic_and_current` or commit manually edited generated pages. No merge authorization is implied.
