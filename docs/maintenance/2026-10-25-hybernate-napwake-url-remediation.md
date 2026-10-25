# 2026-10-25 — Hybernate to Napwake canonical identity / URL remediation

## Scope and incident

- Canonical record: `hybernate` in `data/tools/kubernetes-networking-storage-addons.yaml` only.
- The stable catalogue ID `hybernate` and original legacy provenance remain unchanged.
- This is an **out-of-Wave-23**, independently reviewable remediation. No other canonical record, URL baseline, link-audit checker or workflow is changed.
- Full link audit [#34](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40132520765) on 2026-10-24 and [#35](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40179979202) on 2026-10-25 both returned HTTP 404 for `https://okedeji.io/hybernate` on HEAD and GET. [#33](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40015972574) returned HTTP 301 → 200 for this URL on 2026-10-23. This is dated endpoint evidence, not proof of project abandonment.
- Audit #35 also detected a separate transient-looking TLS failure on Spot FinOps; this PR **does not** change Spot metadata. The original six strict-baseline exceptions remain unchanged; [tracker #2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2) stays open.

## Primary-source identity evidence

1. The historical GitHub repository `okedeji/hybernate` resolved by immutable GitHub repository ID **1184648040**. The GitHub REST metadata for repository ID **1184648040** now identifies [`napwake/napwake`](https://github.com/napwake/napwake) with `name: napwake`, `owner: napwake`, and `homepage: https://napwake.dev`. Identical repository identity establishes continuity despite owner/name changes; it does not depend on a search snippet.
2. The [upstream README](https://github.com/napwake/napwake/blob/main/README.md) describes a Kubernetes operator for scaling idle workloads to zero and waking them on demand, including Helm installation and the `kubectl napwake` plugin. [Upstream docs](https://docs.napwake.dev/) are explicitly linked by that README. This substantiates the updated name, summary, repository, and docs URLs.
3. The repository [LICENSE](https://github.com/napwake/napwake/blob/main/LICENSE) and GitHub metadata identify the source repository licence as Apache-2.0. **This pertains to the source repository, not a blanket guarantee about every external service.**

## Changes and conservative decision

| Field | Before | After | Decision |
|---|---|---|---|
| `id` | `hybernate` | unchanged | Preserve stable historical identity |
| `name` | Hybernate | Napwake (formerly Hybernate) | Source-verified rename |
| `summary` | Scheduled pod hibernation | Idle-workload pause and on-demand wake | Match current upstream README |
| `official_url` | `https://okedeji.io/hybernate` | `https://github.com/napwake/napwake` | Canonical upstream chosen as stable verifiable landing page; do not guess redirect |
| `repository_url` | absent | `https://github.com/napwake/napwake` | Verified canonical source |
| `documentation_url` | absent | `https://docs.napwake.dev/` | Upstream-linked docs |
| `license_spdx` | absent | `Apache-2.0` | GitHub repository metadata / upstream licence |
| `sources` | legacy only | original legacy + upstream repository/licence/docs | Preserve lineage and add primary proof |
| `verified_on` | 2026-08-03 | 2026-10-25 | Date of limited identity evidence review |
| `status`, `needs_review`, `maturity` | needs-review / true / unknown | **unchanged** | Maintenance maturity and full support boundaries not independently cleared |

## Verification and handoff

- This PR is intentionally **Draft** and **not merge-ready** until a full checkout regenerates all generated navigation using `python -m scripts.generate_docs` and commits exact generator output, followed by `python -m scripts.generate_docs --check`, `python -m scripts.validate_catalog`, locked Python 3.12 checks, Ruff, pytest and `git diff --check`.
- The ChatGPT GitHub connector can commit canonical files but does not execute the repository's generator or the network audit. **These tests are not represented as having run.**
- Run a new strict full audit on the final commit. Require `blocking_new: 0`, `strict_result: PASS`, and unchanged six historical baseline URL/classification pairs; a separate Spot TLS incident could still block this gate.
- No merge, auto-merge, release, baseline waiver or change to Wave 23 PR #137 is authorized by this draft.
