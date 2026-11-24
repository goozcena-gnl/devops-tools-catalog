# Issue #204 — Three-record taxonomy and lifecycle corrections (2026-11-24)

**Status: IMPLEMENTATION CANDIDATE, NOT MERGED.** Proposed on `maintenance/issue-204-three-retain-taxonomy-evidence-review` from baseline `76927d27c79cc17ada435e65924d01a28a86c8aa`. Maintainer confirmed individual decisions in [issue #204](https://github.com/goozcena-gnl/devops-tools-catalog/issues/204#issuecomment-7125495634). This ledger documents *only approved* changes; publication requires local/CI/exact-SHA gates.

## Field-level decision ledger

| ID | Decisions | Changes | Still unresolved |
| --- | --- | --- | --- |
| `kwatcher` | K01/K02/K04 APPROVE; K03/K05 DEFER | Correct ConfigMap synchronization/Deployment rollout guidance; move from monitoring to `kubernetes-networking-storage-addons` / `Kubernetes Ecosystem & Add-ons`; append [upstream README pinned to d31e98aa](https://github.com/Berg-it/Kwatcher/blob/d31e98aafb39878dab12fc97fa65b0b80ad0fbfe/README.md) | `license_model: oss` retained unchanged under DEFER; pinned README mentions MIT; no standalone licence file identified in the frozen tree; no SPDX claim (K03 deferred); roles and stages unchanged, `status: needs-review`, `needs_review: true` |
| `grove` | G01/G02/G03/G04 APPROVE; G05 DEFER | Correct distributed AI inference/gang scheduling guidance; move to `mlops-llmops-ai-infrastructure` / `MLOps Platforms`; `license_spdx: Apache-2.0` *source-only*; append [README](https://github.com/ai-dynamo/grove/blob/3bd8096742d83ce2e3c4e27e7ee78b329f3a88be/README.md), [install](https://github.com/ai-dynamo/grove/blob/3bd8096742d83ce2e3c4e27e7ee78b329f3a88be/docs/installation.md), [LICENSE](https://github.com/ai-dynamo/grove/blob/3bd8096742d83ce2e3c4e27e7ee78b329f3a88be/LICENSE) | Beta state and Kubernetes/scheduler compatibility require review; third-party models/containers not covered by source licence; roles and stages unchanged; `status: needs-review`, `needs_review: true` |
| `openlens` | O01/O02/O04/O05 APPROVE; O03 DEFER | Correct historical third-party signed binary-build guidance; `status: historical`; preserve Kubernetes category, append [publisher README](https://github.com/MuhammedKalkan/OpenLens/blob/a7d44fba75e1a35087fe592ed77d51d6d260797b/README.md) and [historical release](https://github.com/MuhammedKalkan/OpenLens/releases/tag/v6.5.2-366) | Binary-specific licence not established; `license_model: oss` remains unchanged solely because O03 DEFER, **not confirmed**; no SPDX; `needs_review: true`; not synonymous with existing FreeLens |

## Invariants and proof

- Four category source blobs before patch: monitoring `6b463ba2ec5638d6eca6179b5e46fc49bd772f4d`; Kubernetes operations `a127d4e74b6df3903c601cb60e1658ce1e78e5ea`; Kubernetes add-ons `ad676f63ef76ffa70a21f12c8c39fd560f6109f1`; MLOps `17d5a2892b8ac09987a416a04d19ef041eb62fc5`.
- Preserved exactly 1,425 canonical IDs, all 1,422 unrelated records, and existing legacy provenance; migration counts: monitoring 99→97, Kubernetes operations 142→142, Kubernetes add-ons 132→133, MLOps 80→81.
- Deferred K03/K05/G05/O03: licenses, roles/lifecycle, product-rights are **not authorized** to be changed. `verified_on` and `maturity` must not be changed by this bounded patch; source examination timestamp belongs in this dated ledger.
- `freelens`, issue #2, issue #173, unrelated PR #132, constraints/workflows/tests/schema/link baseline were not changed.

## Validation record (to be filled only after actual execution)

| Gate | Result | Evidence / exact SHA |
| --- | --- | --- |
| Preflight exact `main` and worktree | PASS | Frozen base and remote branch rechecked; candidate worktree intentionally modified. |
| Canonical migration script and independent guard | PASS | Dry-run/apply; verifier v1.1: 1,425 unique IDs; 1,422 protected; 18 approved field changes. |
| Generator and generator check | PASS | Generator output current; rechecked against uncommitted candidate. |
| Locked Python 3.12 dependencies and `pip check` | PASS | Windows 3.12.10, 20 pins using external overlay; original Linux lock unchanged. |
| Ruff check and format | PASS | Ruff check and format; 70 files formatted in supplied log. |
| Full pytest | PASS (reported local run) | 1,004 passed, 8 skipped, 407.54s; operator log on uncommitted candidate, not a CI or exact-commit result. |
| `validate_catalog`, `review_debt`, whitespace | PASS | 533 review records, 65 unknown licences; git diff --check exit 0. |
| Seven GitHub CI/security checks on candidate SHA | NOT RUN | |
| Separately dispatched strict Full Link Audit and JSON baseline | NOT RUN | |

The table above must **never** be updated to PASS before actual execution. Stop on any failed gate, especially when category migration leads to generated-file changes outside the explicitly reviewed generator impact. Draft PR only; no Ready transition, merge or auto-merge.

## Local validation recovery

- Windows-specific `colorama==0.4.6` overlay: SHA256 `1fa7250a3c56b64e73e704417097167b5146439be515a1b08d0002566c42cd09`; no changes to committed Linux pins or verifier.
- Independent verifier v1.1 allows the official generated historical index `docs/deprecated-tools.md`; external verifier SHA256 `915d44862bc8e1a19fb4f2d4a4442e6abc67180d96bfbea8e5886a040c71a326`.
- The earlier LF/CRLF warnings were captured separately; Git returned exit 0. No configuration change or baseline waiver.
- Full pytest result supplied by the operator in the 2026-11-24 validation transcript (SHA256 `36d1c9c89c3ae17fd3593bfa2b4913a638f882ba0320f5142e07a61a866080ab`). Eight skips retained as skips; Linux CI and strict audit remain NOT RUN.
