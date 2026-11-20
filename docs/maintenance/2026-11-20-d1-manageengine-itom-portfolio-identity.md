# D1 — ManageEngine ITOM portfolio identity correction (2026-11-20)

## Intent and frozen provenance

- Repository: `goozcena-gnl/devops-tools-catalog`; authoritative `main` parent: `fb5890e09fedfea1b2032c1289d75d0bc1a9e2c3`.
- Original Wave 39 candidate: PR #174; integrated through merged PR #188; post-merge strict Full Link Audit #87 passed on the base exact SHA.
- Research and maintainer decision: [Issue #173 audit](https://github.com/goozcena-gnl/devops-tools-catalog/issues/173#issuecomment-7042064378) establishes that `manageengine-it-operations-management` is an ITOM **vendor portfolio** identity, not automatically a synonym of OpManager Nexus. The maintainer explicitly chose Option A on 2026-11-20.
- This Draft PR is limited to correcting that existing portfolio record and its deterministic generated views. It neither creates a Nexus record nor replaces other ManageEngine or Site24x7 identities.

## Primary vendor evidence

1. [ManageEngine ITOM and observability portfolio](https://www.manageengine.com/it-operations-management.html) lists separately marketed OpManager Nexus, OpManager, Site24x7, Applications Manager, NetFlow Analyzer, Network Configuration Manager and other products.
2. [OpManager Nexus landing](https://www.manageengine.com/it-operations-management/) is a **single product identity** and is not an appropriate `official_url` for the aggregate catalogue record.
3. [Official rename announcement](https://www.manageengine.com/fr/it-operations-management/product-announcement.html) says OpManager Plus became OpManager Nexus; it does **not** rename the entire portfolio.

## Field-level allowlist and invariants

Canonical file: `data/tools/sre-incident-response-on-call.yaml`. Exact allowed record ID: `manageengine-it-operations-management`.

| Canonical field | Bounded change |
| --- | --- |
| `official_url` | From product landing `https://www.manageengine.com/it-operations-management` to portfolio `https://www.manageengine.com/it-operations-management.html` |
| `summary` | Describe separate network, infrastructure, application and digital-experience products |
| `use_when` | Use the portfolio to compare concrete offerings before selecting one |
| `avoid_when` | Do not treat portfolio as a purchasable SKU with unified licence/support |
| `sources` | Append the three dated official vendor evidence pages above; preserve both legacy provenance references |

**Frozen**: `id`, `name`, `categories`, `subcategories`, `roles`, `lifecycle_stages`, `deployment_models: []`, `license_model: unknown`, `maturity: unknown`, `status: needs-review`, `needs_review: true`, `verified_on: '2026-08-03'`, `alternatives`, `tags`. Exactly 20/21 remaining raw SRE record blocks must remain byte-identical. In particular D2 `moogsoft` and D3 `patchmon` are still **RETAIN**, with no licence/SPDX assumption.

## Derived documentation

Five generated views alone are expected to change alongside the canonical YAML:
- `docs/categories/sre-incident-response-on-call.md`
- `docs/lifecycle/operate.md`
- `docs/lifecycle/monitor.md`
- `docs/roles/site-reliability-engineer.md`
- `docs/roles/observability-engineer.md`

Preserve counts and licence/status statistics, WSO2 official URL remediation, `otel-gui` correction, link-audit baseline, code generation, Python constraints, and other historical sources. No README/statistics changes are expected because totals are unchanged.

## Validation and human gate

- Prepublication guard: confirm exact single-parent commit, 7-path allowlist (1 YAML + 5 generated + this ledger), 1/21 changed blocks, only five allowed canonical fields, source URL separated from Nexus, untouched frozen metadata, and generated-view changes bounded to D1.
- **Fresh exact-HEAD CI remains REQUIRED**: full pytest, catalogue/schema validation, `scripts.generate_docs --check`, Ruff and repository hygiene; record actual results after GitHub workflow execution.
- Independently run **strict Full Link Audit on this new exact SHA**, with `blocking_new: 0`, `blocking_known: 6`, `strict_result: PASS`, `baseline_changed: []` and `baseline_resolved: []`. Preserve JSON/Markdown artifacts; the earlier main audit #87 cannot substitute.
- **Keep the PR OPEN/DRAFT, NO MERGE / AUTO-MERGE / TAG / RELEASE / BASELINE WAIVER / ISSUE CLOSURE.** Human independent review and a separately authorized status change/integration are necessary. D1 remains `needs-review` after this identity correction; any future Nexus standalone addition is a **different proposal**.

**Disposition: bounded identity reconciliation only; licence and lifecycle unknown deliberately retained.**
