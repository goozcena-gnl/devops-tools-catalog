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
