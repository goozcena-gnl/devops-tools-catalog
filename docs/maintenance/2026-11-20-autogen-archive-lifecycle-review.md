# AutoGen — upstream archival evidence review (2026-11-20)

## Scope and provenance

- Base: protected `main` `fb5890e09fedfea1b2032c1289d75d0bc1a9e2c3`; source AutoGen YAML blob `74daa9ef338fdd31a301f2d2f10de1f5cd617676`.
- Independent regression: [Full Link Audit #88](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/44775708655) on Draft PR #189, exact SHA `06874e20f6ef3642f6bccec594607b48c9cbdbf3`.
- Audit #88 reported `blocking_new: 1`, `blocking_known: 6`, `strict_result: FAIL`. The new blocker was `https://github.com/microsoft/autogen` (`repository-archived-unexpected`); the new ManageEngine D1 portfolio URL was HTTP 200 / valid.
- This is a **separate AutoGen lifecycle correction**. PR #189 is untouched, open and Draft. Do not waive link-audit checks or rewrite `config/link-audit-baseline.json`.

## Official upstream evidence and license scope

1. [AutoGen upstream](https://github.com/microsoft/autogen) reports `archived: true` in GitHub repository metadata.
2. [AutoGen README](https://github.com/microsoft/autogen/blob/main/README.md) states Microsoft has archived AutoGen and supplies **no security fixes, bug fixes, new features or support**; production use is discouraged.
3. The README points newcomers to [Microsoft Agent Framework](https://github.com/microsoft/agent-framework) and existing users to the [AutoGen migration guide](https://learn.microsoft.com/en-us/agent-framework/migration-guide/from-autogen/).
4. [AutoGen source-code licence](https://github.com/microsoft/autogen/blob/main/LICENSE-CODE) is MIT. GitHub repository-level licence detection reports CC-BY-4.0 for a different scope; it is **not a basis to relicense the source code or every repository file**.

## Exact canonical field boundaries

Only `autogen` in `data/tools/mlops-llmops-ai-infrastructure.yaml` changes:
- Add `repository_archived: true` (expected archive classification in strict GitHub API link checks).
- Change `status: active` to `status: archived`.
- Change `needs_review: false` to `needs_review: true` to retain migration/production-safety review debt.
- Update `summary`, `use_when`, `avoid_when`, and append primary-source `sources`.
- Preserve `id`, `name`, `official_url`, `documentation_url`, `repository_url`, `categories`, `roles`, `lifecycle_stages`, `deployment_models`, `license_model: oss`, `license_spdx: MIT`, and historical `verified_on: '2026-08-12'`.
- All other raw YAML records are unchanged. No new Microsoft Agent Framework record or unrelated lifecycle migration.

## Regenerated outputs and expected deterministic counts

- Expected allowlist: canonical YAML; generated README, statistics JSON, MLOps category page, archived/deprecated list, 2 roles and 3 lifecycle pages; this maintenance ledger (**11 total paths**).
- Counts: 1,425 tools, 30 categories; `active: 873`, `archived: 11`, `needs-review: 537` (unchanged status count); not-flagged 887, review-required 538, deprecated/archived/historical 15, archived source repositories 15.
- Licence model totals are unchanged: OSS code scope remains MIT. No changes to the WSO2 fix, D1 branch, existing historical PRs, Python constraints or link-audit baseline.
- Source docs are generated via `scripts/generate_docs.py` and must pass `python -m scripts.generate_docs --check` on exact candidate SHA.

## Required validation before any integration

1. Exact parent/branch/11-path allowlist, one changed canonical record, immutable source licence and historic date, and no baseline mutation.
2. Fresh exact-SHA CI (pytest, schema/catalogue, generator, Ruff, Gitleaks, Plumber and CodeQL); do not assert success until observed.
3. Independent **strict Full Link Audit** on candidate SHA: `blocking_new: 0`, `blocking_known: 6`, `strict_result: PASS`, `baseline_changed: []`, `baseline_resolved: []`. Preserve report JSON/Markdown.
4. Independent human field-level review and separately authorized Ready-for-Review/merge decision.

**KEEP THIS PR OPEN/DRAFT. No merge, auto-merge, tag, release, branch deletion, baseline waiver, closure of issues #2/#173, or change to Draft PR #189.**
