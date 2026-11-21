# D1 ManageEngine portfolio — integration on post-AutoGen main (2026-11-21)

## Identity and immutable sources

- Repository: `goozcena-gnl/devops-tools-catalog`.
- Exact new integration parent (protected post-AutoGen `main`): `77664da7d93440a40a4f8ca7474f1dfb0af6974c`; [AutoGen archival PR #190](https://github.com/goozcena-gnl/devops-tools-catalog/pull/190) is merged on that SHA.
- Old [D1 source Draft PR #189](https://github.com/goozcena-gnl/devops-tools-catalog/pull/189): exact HEAD `06874e20f6ef3642f6bccec594607b48c9cbdbf3`, built from previous base `fb5890e09fedfea1b2032c1289d75d0bc1a9e2c3`. **Keep source PR #189 open and Draft as preserved review/evidence history, never merge it separately.**
- All seven D1 source paths are reproduced by **exact original Git blob SHA**, including `docs/maintenance/2026-11-20-d1-manageengine-itom-portfolio-identity.md`. That earlier ledger's old parent is preserved as *historical provenance*, not incorrectly relabeled as the current base.
- The **eighth and only new path** is this integration ledger documenting the post-AutoGen parent and fresh validation requirements.
- The 7 source paths and 11 previously merged AutoGen paths are **disjoint**. Source D1 data and generated views have not been manually merged with or overwritten from an older common file: these six existing paths on new `main` still match the earlier D1 base blobs byte-for-byte.

## Canonical invariants and field allowlist

- Canonical path: `data/tools/sre-incident-response-on-call.yaml`; exactly one changed record of 21: `manageengine-it-operations-management`.
- Exactly five authorized fields change: `summary`, `official_url`, `use_when`, `avoid_when`, `sources`, using unchanged source PR #189 blob `8eb3af5aa0c5e4486c5905d01b531652381133c7`.
- `official_url`: product-specific `https://www.manageengine.com/it-operations-management` becomes vendor ITOM portfolio `https://www.manageengine.com/it-operations-management.html`.
- Preserve `id`, `name`, `license_model: unknown`, `status: needs-review`, `needs_review: true`, original `verified_on`, all other record fields. All **20 other SRE blocks are byte-identical**; D2 `moogsoft`, D3 `patchmon` RETAIN.
- No standalone OpManager Nexus, Site24x7 or other vendor product is added or reclassified in this PR.

## Derived documentation and protected concurrent work

- Source PR #189's generated views are reused by blob: SRE category, monitor/operate lifecycle and observability/SRE roles.
- Preserve post-AutoGen `data/tools/mlops-llmops-ai-infrastructure.yaml`, `docs/deprecated-tools.md`, MLOps generated views and all status counts: 1,425 total / 30 categories / 873 active / 11 archived / 537 needs-review; 538 flagged for review.
- Preserve the Microsoft AutoGen archived metadata and source-scoped MIT licence, post-Ruff Python constraints, WSO2 canonical URL fix, historic `otel-gui` correction and `config/link-audit-baseline.json`.
- No README or `docs/catalog-statistics.json` changes are expected from D1's documentation-only / unknown-license-preserving correction.

## Independent audit provenance

- [AutoGen post-merge Full Link Audit #90, run 44895143030](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/44895143030): `workflow_dispatch`, exact parent `77664da7d93440a40a4f8ca7474f1dfb0af6974c`, completed SUCCESS, `blocking_new: 0`, `blocking_known: 6`, `strict_result: PASS`, `repository-archived-expected: 15`. Local maintainer post-merge validation reports `baseline_changed: []` and `baseline_resolved: []`; those two arrays are sourced from local script output, not independently decoded in this ledger.
- Prior [D1 PR #189 strict Full Link Audit #88](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/44775708655) reported FAIL with exactly one **unrelated** new `microsoft/autogen` archived-repository blocker; the D1 portfolio URL was valid. That historic failure must **not** be erased or described as PASS.
- Prior [AutoGen PR #190 strict Full Link Audit #89](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/44793726749) PASS was on an older branch SHA, **not** this newly prepared D1 integration SHA.

## Required acceptance gates — no preemptive PASS

1. Verify parent, branch and one-commit / **eight-path exact allowlist**; seven source blobs retained byte-identically, one new dated ledger.
2. Verify one changed D1 record / 20 untouched, five allowed fields only; untouched D2/D3, AutoGen, WSO2, stats and audit baseline.
3. Fresh **exact-HEAD CI**: full pytest, catalogue/schema checks, `python -m scripts.generate_docs --check`, Ruff, Gitleaks, Plumber and CodeQL. Observe actual results before marking SUCCESS.
4. Fresh independent **strict Full Link Audit on this new exact SHA** with expected `blocking_new: 0`, `blocking_known: 6`, `strict_result: PASS`, `baseline_changed: []`, `baseline_resolved: []`; preserve JSON and Markdown report artifacts. #90 and #89 are NOT substitutes for this PR's audit.
5. Obtain independent human field review; separately authorize any Draft to Ready transition or eventual merge.

**KEEP the new integration PR OPEN / DRAFT. No merge, auto-merge, release, tag, branch deletion, issue closure or baseline waiver. Keep PR #189 OPEN / DRAFT as historical evidence and issues #2 / #173 OPEN.**
