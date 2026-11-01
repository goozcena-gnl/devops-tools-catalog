# Wave 36 - FinOps platforms and Kubernetes sizing calculators evidence review

**Reviewed 2026-10-31. Preliminary local evidence patch only; not a validated PR or merge authorization.**

- Issue: https://github.com/goozcena-gnl/devops-tools-catalog/issues/159
- Frozen main: `80109d5b83ec147f7c0c1556b269386aa7acf05c`
- Original category Git blob: `3c76a3cbc9783e306cd8244b4178566af6256178`
- Exact cohort: 8 of 29 `finops-sustainability` records; 21 other canonical record blocks preserved byte-for-byte.
- Results proposed for testing: **6 CLEAR / 2 RETAIN**. Decisions are contingent on the local test suite and human review. No `license_spdx` inferred for any of these eight.
- Keep original `legacy:` provenance in each reviewed block, without changing the order or rewriting historical source strings.

## Decision table

| ID | Decision | Primary evidence | Reason and blocker |
|---|---|---|---|
| `kubernetes-capacity-calculator` | CLEAR (documentation) | https://wintelguy.com/kubernetes-capacity-calculator.pl | Author-operated calculator explicitly details CPU/memory, DaemonSets, reservations and approximate sizing; not a source-license assertion. |
| `learnkube-kubernetes-instance-calculator` | CLEAR (documentation) | https://learnkube.com/kubernetes-instance-calculator | Creator-operated cloud-node comparator covers AWS/GCP/Azure/Linode; prices remain estimates. |
| `spot-finops` | RETAIN (unknown) | https://www.flexera.com/about-us/press-center/flexera-completes-acquisition-of-netapps-spot-finops-portfolio | Spot portfolio acquired from NetApp on 2025-03-03. Original generic record does not identify a standalone currently licensable SKU; vendor-specific products and contracts need reconciliation. |
| `ternary` | CLEAR (commercial) | https://ternary.app/ternary-cloud-finops/ ; https://docs.ternary.app/docs/administrator-quick-start ; https://docs.ternary.app/docs/ternary-self-hosted | Official multi-cloud integrations and SaaS/self-hosted *licensed* delivery; no claim of OSS rights. |
| `vegacloud-inform` | CLEAR (commercial) | https://docs.vegacloud.io/docs/intro ; https://www.vegacloud.io/aws | Inform is a managed cost visibility, budgets, forecasting and anomalies tier; do not conflate with Optimize or Operate. |
| `xosphere` | CLEAR (commercial) | https://www.xosphere.io/ ; https://www.xosphere.io/pricing/ | Xosphere IQ has SpotIQ/ClusterIQ/TokenIQ with differentiated services; TokenIQ is listed as early access. |
| `yotascale` | RETAIN (unknown) | https://yotascale.com/ | Original site reports acquisition by CoreStack; standalone SKU, licence/entitlements and migration scope require vendor confirmation. |
| `zesty` | CLEAR (commercial) | https://docs.zesty.co/docs ; https://docs.zesty.co/docs/commitment-manager | Current product includes Kubernetes optimization plus AWS/Azure financial commitments; SaaS offering rights are separate from Kubernetes agents. |

## Field-level scope manifest

The eight original YAML `id`, `name`, `categories`, `roles`, `lifecycle_stages`, `maturity`, original `sources`, and `legacy:` entries are preserved. For all eight, `summary`, `use_when`, `avoid_when`, `verified_on` and new official source citations are updated. The only other semantic edits are:

- `kubernetes-capacity-calculator`, `learnkube-kubernetes-instance-calculator`: `status: needs-review` -> `active`; `needs_review: true` -> `false`; keep `license_model: documentation` and `deployment_models: []`.
- `ternary`: `license_model: unknown` -> `commercial`; `deployment_models: []` -> `[hosted-saas, self-hosted]`; `status: needs-review` -> `active`; `needs_review: true` -> `false`.
- `vegacloud-inform`, `xosphere`, `zesty`: `license_model: unknown` -> `commercial`; `deployment_models: []` -> `[hosted-saas]`; `status: needs-review` -> `active`; `needs_review: true` -> `false`.
- `spot-finops`, `yotascale`: remain `license_model: unknown`, `status: needs-review`, `needs_review: true`; record acquisition evidence only and do not infer source license or commercially supported standalone identity.

## Expected deterministic inventory after local generator

- Canonical records: **1,425**, categories **30** (no inserts/deletions).
- Active **867** (from 861); needs-review **544** (from 550).
- Unknown license models **69** (from 73); commercial **173** (from 169).
- Out-of-cohort 21 raw blocks and all 8 original legacy source lines must remain identical.

## Guards and human gates

- Local precheck must pin main `80109d5b83ec147f7c0c1556b269386aa7acf05c`, require clean tree, reject branch drift and check exact old canonical blob.
- Re-run `python -m scripts.generate_docs` and `--check`, `python -m scripts.validate_catalog`, `python -m pip check`, Ruff lint and format, full `python -m pytest`, `python -m scripts.review_debt --format json`, and strict changed-path/record-count/provenance controls.
- Only after full validation: human-scoped commit/push; **Draft PR**. PR CI, independent strict Full link audit (zero new blockers), fresh review and manual Ready/merge gates are separate future steps.
- Never auto-merge, relax audit baselines, or close issue #159 before successful post-merge checks.
