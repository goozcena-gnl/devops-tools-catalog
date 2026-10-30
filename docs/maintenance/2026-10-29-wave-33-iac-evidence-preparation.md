# Wave 33 — Infrastructure as Code: evidence preparation (NOT a clearance)

**Date:** 2026-10-29 (Europe/Paris). **Status:** evidence-backed canonical patch staged on isolated branch; generated documentation, Python checks and PR gates NOT YET RUN. **Not ready for merge.**

> **Chronology note (2026-10-29):** The preparation and execution-boundary statements below describe the state **when this report was drafted**. They are retained verbatim as historical evidence, not current execution status. The final validation checkpoint at the end records subsequent tests, publication and audit results. A later documentation-only commit creates a new HEAD that requires renewed checks before Ready or merge.

## Baseline / frozen scope

- Tracking issue: https://github.com/goozcena-gnl/devops-tools-catalog/issues/153
- Base `main`: `7c0e749a7454280b93d7f032af149153d363323b` (Wave 32 merged)
- Canonical YAML: `data/tools/infrastructure-as-code.yaml`, original Git blob `f49d39ebd8b3311bf63514fac811f7b41afcf3f0`.
- Exactly five selected existing IDs out of 35, 30 other records must remain untouched: `azurenamingtool`, `pluralith`, `scalr`, `terraform-aws-eks-operation-scheduler`, `terravision`.
- Main README reports 1,425 records / 567 `needs-review` before this review. Proposed 3 CLEAR / 2 RETAIN; projected global needs-review count 564, not regenerated/validated. No verified post-patch counters.
- Strict link baseline, issue #2, schemas, workflows, and existing documentation may change **only** through the standard process; never manipulate link exceptions to obtain a passing result.

## Initial primary-source evidence (review snapshot, not final approval)

| ID | Publisher-origin primary evidence and licensing boundary | Decision pending |
| --- | --- | --- |
| `azurenamingtool` | Microsoft Azure [source commit](https://github.com/Azure/AzureNamingTool/tree/99353c223cdf2e0254f102b5b2ed2c92f5ec2d96) and [MIT licence file](https://github.com/Azure/AzureNamingTool/blob/99353c223cdf2e0254f102b5b2ed2c92f5ec2d96/LICENSE); [official wiki](https://github.com/mspnp/AzureNamingTool/wiki). Source not archived; GitHub metadata reported v5.0.3 release 2026-09-15. Code MIT does not imply that Azure itself or every dependency is MIT. | Candidate CLEAR subject to verified functions, security caveats, URLs and full manifest |
| `pluralith` | [Pluralith CLI source](https://github.com/Pluralith/pluralith-cli/tree/2c03ddb60e97fcd858071b6b1190bd376be860e5) with [MPL-2.0 CLI licence](https://github.com/Pluralith/pluralith-cli/blob/2c03ddb60e97fcd858071b6b1190bd376be860e5/LICENSE). README explicitly says product is Alpha and requires Pluralith UI and/or an API key. Last observed CLI commit 2023-03-23; latest observed CLI release v0.2.2 (2023-03-23); not archived. Neither the CLI licence nor an unarchived repository confirms licence of the hosted UI, present-day service availability or active development. | **RETAIN** `needs-review` unless contemporary first-party information resolves product availability and offering |
| `scalr` | [Vendor documentation](https://docs.scalr.io/docs/introduction) describes remote run execution and state/policy management for Terraform/OpenTofu. [Vendor product](https://scalr.com/) and [pricing](https://scalr.com/pricing) show a commercial, per-run SaaS offering with a free usage allowance and self-hosted **agents**, which must not be described as a fully self-hosted control plane. Separately, [Scalr provider source](https://github.com/Scalr/terraform-provider-scalr) has MPL-2.0; that source licence is **not** a product-wide Scalr platform SPDX. Current canonical `official_url` points to a GitHub organisation; consider vendor product URL only after canonical uniqueness and ownership checks. | Candidate CLEAR for commercial offering; **do not** assign provider SPDX to product |
| `terraform-aws-eks-operation-scheduler` | [Pinned source](https://github.com/gianniskt/terraform-aws-eks-operation-scheduler/tree/e8e9ed38c27bd76c1f2b3e308dd37aaec9c04f6d). [Tagged v1.0.4 LICENSE](https://github.com/gianniskt/terraform-aws-eks-operation-scheduler/blob/v1.0.4/LICENSE) says Apache License 2.0, while [the same tag's README license heading](https://github.com/gianniskt/terraform-aws-eks-operation-scheduler/blob/v1.0.4/README.md#license) explicitly says **MIT License**. Last observed release 2025-12-15. The module schedules **EKS node-group** scaling via Lambda/EventBridge and does not shut off the charged EKS control plane. A licence conflict is not solved by choosing the license scanner's answer. | **RETAIN** review; no SPDX until upstream resolves inconsistency or exact legally authoritative scope is established |
| `terravision` | [Pinned source](https://github.com/patrickchugh/terravision/tree/849bf43b8bbe074c0f798777e4eb1e7cc825dda2) and [root licence](https://github.com/patrickchugh/terravision/blob/849bf43b8bbe074c0f798777e4eb1e7cc825dda2/LICENSE) AGPLv3; [pyproject.toml](https://github.com/patrickchugh/terravision/blob/849bf43b8bbe074c0f798777e4eb1e7cc825dda2/pyproject.toml) specifies **AGPL-3.0-only**. GitHub release v0.56.0 observed 2026-10-19. Terraform-to-diagram, AI/MCP diagram features are described in upstream package metadata; optional model requests and infrastructure data disclosure must be assessed separately, not treated as automatically offline. | Candidate CLEAR for AGPL-3.0-only *source* pending full review |

### Risk / correctness guardrails

- `status: active` is a review classification, never proof of production safety, uptime or tested compatibility.
- Terraform plan/state, graph/diagrams and repository code can contain hostnames, identifiers, network topology, policy design and secrets. Evaluate data paths to external services before recommending hosted visualisation or LLM integrations.
- For Scalr, separate managed execution and state control plane from **self-hosted execution agents**. Distinguish free-tier SaaS pricing from OSS/open-core licensing. Do not copy the provider's MPL-2.0 into product licence metadata.
- For Pluralith, separate MPL-2.0 CLI from UI/service legal availability; no current-maintenance inference from `archived: false`.
- For EKS scheduler, validate which AWS resource and IAM actions are touched, idempotence, time zones, existing Karpenter/autoscaler interaction, EKS cluster fixed costs and Lambda/EventBridge permissions; do not propagate an unverified cost-saving percentage.
- For TerraVision, verify exact AGPL `-only` source scope and deployment-model/tool-call claims; do not assume optional MCP or LLM features never exfiltrate data.

## Before canonical modification (required)

1. Do a second independent primary-evidence pass. Freeze per-record **OLD / NEW** decisions and sources, distinguish confirmed changes from retained unknowns, and prove IDs and order stable.
2. Revalidate `main` SHA, file blob SHA, issue/PR state, documentation-link ownership and normalized uniqueness, repo taxonomy allowed values and allowable deployment models.
3. Apply **only** approved fields to selected canonical IDs; preserve original `legacy:` provenance. There is no obligation to clear all five. Preserve each unresolved item's `needs_review: true` / `status: needs-review`.
4. Run deterministic generator; include only generated outputs actually changed and the canonical YAML / evidence report. Validate every changed path against a frozen allowlist; do not hand-edit generated files.
5. On configured Python 3.12 environment: `python -m scripts.generate_docs`, `python -m scripts.generate_docs --check`, `python -m scripts.validate_catalog`, `python -m scripts.review_debt --format json`, Ruff lint/format, `pip check`, full `pytest`, `git diff --check` and source identity/scope checks.
6. Only after validated implementation, publish a Draft PR; on its final SHA check mandatory remote CI and strict Full link audit (`blocking_new: 0`; `strict_result: PASS`; historical `blocking_known` disclosed). No automatic Ready or merge.

## Execution boundary / unverified work

The five-record canonical patch has been staged on the isolated branch. Generated Markdown has NOT been regenerated; full Python validation and tests have NOT run; no Draft PR or merge has been created. GitHub transport fails DNS in the execution container, which only has Python 3.13 instead of the repo's pinned Python 3.12.

## Canonical patch — exact OLD/NEW field manifest

### `azurenamingtool` — 11 changed fields

`summary` — OLD:
```yaml
  summary: NET Blazor app with REST API for generating and validating Azure resource names with SQLite-backed
    configuration.
```
NEW:
```yaml
  summary: "Microsoft Azure Naming Tool web app and REST API for generating Azure resource names from administrator-defined conventions."
```

`documentation_url` — OLD:
```yaml
<absent>
```
NEW:
```yaml
  documentation_url: "https://github.com/mspnp/AzureNamingTool/wiki"
```

`use_when` — OLD:
```yaml
  use_when: []
```
NEW:
```yaml
  use_when:
  - "You want a self-hosted naming convention generator and API for Azure resources."
```

`avoid_when` — OLD:
```yaml
  avoid_when: []
```
NEW:
```yaml
  avoid_when:
  - "You need enforcement of Azure naming policy: generating names is not a replacement for Azure Policy."
  - "You cannot secure the application's administrative configuration, access and API."
```

`deployment_models` — OLD:
```yaml
  deployment_models: []
```
NEW:
```yaml
  deployment_models:
  - "self-hosted"
```

`license_spdx` — OLD:
```yaml
<absent>
```
NEW:
```yaml
  license_spdx: "MIT"
```

`repository_archived` — OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_archived: false
```

`status` — OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "active"
```

`needs_review` — OLD:
```yaml
  needs_review: true
```
NEW:
```yaml
  needs_review: false
```

`sources` — OLD:
```yaml
  sources:
  - legacy:devopstools_final.md#L168
```
NEW:
```yaml
  sources:
  - "legacy:devopstools_final.md#L168"
  - "https://github.com/Azure/AzureNamingTool/tree/99353c223cdf2e0254f102b5b2ed2c92f5ec2d96"
  - "https://github.com/Azure/AzureNamingTool/blob/99353c223cdf2e0254f102b5b2ed2c92f5ec2d96/LICENSE"
  - "https://github.com/Azure/AzureNamingTool/blob/99353c223cdf2e0254f102b5b2ed2c92f5ec2d96/README.md"
  - "https://github.com/mspnp/AzureNamingTool/wiki"
  - "https://github.com/Azure/AzureNamingTool/releases/tag/v5.0.3"
```

`verified_on` — OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-29"
```

### `pluralith` — 8 changed fields

`summary` — OLD:
```yaml
  summary: Visualize and document Terraform infrastructure with automatically generated architecture diagrams.
```
NEW:
```yaml
  summary: "Terraform plan and state diagramming CLI with a separately accessed UI/API; service licensing and current CLI maintenance still require verification."
```

`repository_url` — OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_url: "https://github.com/Pluralith/pluralith-cli"
```

`use_when` — OLD:
```yaml
  use_when: []
```
NEW:
```yaml
  use_when:
  - "You can verify current access and terms for the Pluralith UI/API and want Terraform infrastructure diagrams."
```

`avoid_when` — OLD:
```yaml
  avoid_when: []
```
NEW:
```yaml
  avoid_when:
  - "You require evidence of continuing CLI maintenance: last observed release was March 2023."
  - "You need an entirely open-source and offline Pluralith product: only the separate CLI's MPL-2.0 licence was established."
```

`repository_archived` — OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_archived: false
```

`status` — OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "needs-review"
```

`sources` — OLD:
```yaml
  sources:
  - legacy:devopstools_final.md#L181
```
NEW:
```yaml
  sources:
  - "legacy:devopstools_final.md#L181"
  - "https://github.com/Pluralith/pluralith-cli/tree/2c03ddb60e97fcd858071b6b1190bd376be860e5"
  - "https://github.com/Pluralith/pluralith-cli/blob/2c03ddb60e97fcd858071b6b1190bd376be860e5/LICENSE"
  - "https://github.com/Pluralith/pluralith-cli/blob/2c03ddb60e97fcd858071b6b1190bd376be860e5/README.md"
  - "https://github.com/Pluralith/pluralith-cli/releases/tag/v0.2.2"
  - "https://www.pluralith.com/"
```

`verified_on` — OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-29"
```

### `scalr` — 12 changed fields

`summary` — OLD:
```yaml
  summary: Terraform automation and collaboration software.
```
NEW:
```yaml
  summary: "Commercial Terraform/OpenTofu remote operations platform for central runs, state, policy and drift detection, with optional private run agents."
```

`official_url` — OLD:
```yaml
  official_url: https://github.com/Scalr
```
NEW:
```yaml
  official_url: "https://scalr.com/"
```

`documentation_url` — OLD:
```yaml
<absent>
```
NEW:
```yaml
  documentation_url: "https://docs.scalr.io/docs/introduction"
```

`use_when` — OLD:
```yaml
  use_when:
  - You need a Terraform Cloud alternative with OPA policy enforcement and hierarchical configs.
```
NEW:
```yaml
  use_when:
  - "You need hosted Terraform/OpenTofu remote execution, state, policy-as-code and pull-request workflows."
  - "You want optional private self-hosted agents while using a managed control plane."
```

`avoid_when` — OLD:
```yaml
  avoid_when:
  - Atlantis or native CI pipelines suffice.
```
NEW:
```yaml
  avoid_when:
  - "You need an open-source or fully self-hosted control plane; self-hosted agents do not make the platform OSS."
  - "You cannot entrust Terraform state, run logs, credentials or VCS integration to an external service."
```

`deployment_models` — OLD:
```yaml
  deployment_models: []
```
NEW:
```yaml
  deployment_models:
  - "hosted-saas"
```

`license_model` — OLD:
```yaml
  license_model: unknown
```
NEW:
```yaml
  license_model: "commercial"
```

`commercial_offering` — OLD:
```yaml
<absent>
```
NEW:
```yaml
  commercial_offering: true
```

`status` — OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "active"
```

`needs_review` — OLD:
```yaml
  needs_review: true
```
NEW:
```yaml
  needs_review: false
```

`sources` — OLD:
```yaml
  sources:
  - legacy:2_Cloud-Infrastructure-Serverless/README.md#L120
  - legacy:devopstools_final.md#L222
```
NEW:
```yaml
  sources:
  - "legacy:2_Cloud-Infrastructure-Serverless/README.md#L120"
  - "legacy:devopstools_final.md#L222"
  - "https://scalr.com/"
  - "https://scalr.com/pricing"
  - "https://docs.scalr.io/docs/introduction"
  - "https://docs.scalr.io/docs/agent-pools"
  - "https://docs.scalr.io/docs/requirements"
  - "https://github.com/Scalr/terraform-provider-scalr"
```

`verified_on` — OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-29"
```

### `terraform-aws-eks-operation-scheduler` — 7 changed fields

`summary` — OLD:
```yaml
  summary: Terraform module that schedules AWS EKS node groups to scale up and down with Lambda and EventBridge
    for cost savings.
```
NEW:
```yaml
  summary: "Terraform module scheduling Amazon EKS worker-node capacity using Lambda and EventBridge; does not pause EKS control-plane billing."
```

`use_when` — OLD:
```yaml
  use_when: []
```
NEW:
```yaml
  use_when:
  - "You need scheduled EKS worker-node capacity changes and can test IAM, time zones and cluster-autoscaler interactions."
```

`avoid_when` — OLD:
```yaml
  avoid_when: []
```
NEW:
```yaml
  avoid_when:
  - "You need resolved SPDX terms: v1.0.4 LICENSE says Apache-2.0 but v1.0.4 README says MIT."
  - "You expect to suspend EKS control-plane charges by scaling worker nodes to zero."
  - "You have not tested workloads and recovery during scheduled node scaling."
```

`repository_archived` — OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_archived: false
```

`status` — OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "needs-review"
```

`sources` — OLD:
```yaml
  sources:
  - legacy:devopstools_final.md#L188
```
NEW:
```yaml
  sources:
  - "legacy:devopstools_final.md#L188"
  - "https://github.com/gianniskt/terraform-aws-eks-operation-scheduler/tree/e8e9ed38c27bd76c1f2b3e308dd37aaec9c04f6d"
  - "https://github.com/gianniskt/terraform-aws-eks-operation-scheduler/blob/v1.0.4/LICENSE"
  - "https://github.com/gianniskt/terraform-aws-eks-operation-scheduler/blob/v1.0.4/README.md"
  - "https://github.com/gianniskt/terraform-aws-eks-operation-scheduler/releases/tag/v1.0.4"
```

`verified_on` — OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-29"
```

### `terravision` — 10 changed fields

`summary` — OLD:
```yaml
  summary: Generate professional cloud architecture diagrams automatically from Terraform code (AWS, Google,
    Azure).
```
NEW:
```yaml
  summary: "Cloud architecture diagram generator from Terraform for AWS, Azure and Google Cloud, with optional AI/MCP integration."
```

`use_when` — OLD:
```yaml
  use_when: []
```
NEW:
```yaml
  use_when:
  - "You want cloud infrastructure diagrams from Terraform code for local documentation or CI review."
  - "You can constrain optional AI/MCP tools and review their architecture-data flows."
```

`avoid_when` — OLD:
```yaml
  avoid_when: []
```
NEW:
```yaml
  avoid_when:
  - "Architecture details or Terraform state may be sent to third-party AI services without approved data controls."
  - "You need a guarantee that generated diagrams or AI-assisted IaC are complete or deployment-safe without review."
```

`deployment_models` — OLD:
```yaml
  deployment_models: []
```
NEW:
```yaml
  deployment_models:
  - "local"
```

`license_spdx` — OLD:
```yaml
<absent>
```
NEW:
```yaml
  license_spdx: "AGPL-3.0-only"
```

`repository_archived` — OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_archived: false
```

`status` — OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "active"
```

`needs_review` — OLD:
```yaml
  needs_review: true
```
NEW:
```yaml
  needs_review: false
```

`sources` — OLD:
```yaml
  sources:
  - legacy:devopstools_final.md#L190
```
NEW:
```yaml
  sources:
  - "legacy:devopstools_final.md#L190"
  - "https://github.com/patrickchugh/terravision/tree/849bf43b8bbe074c0f798777e4eb1e7cc825dda2"
  - "https://github.com/patrickchugh/terravision/blob/849bf43b8bbe074c0f798777e4eb1e7cc825dda2/LICENSE"
  - "https://github.com/patrickchugh/terravision/blob/849bf43b8bbe074c0f798777e4eb1e7cc825dda2/pyproject.toml"
  - "https://github.com/patrickchugh/terravision/releases/tag/v0.56.0"
```

`verified_on` — OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-29"
```


## Mandatory completion gates

- Exact five IDs changed and 30 untouched ID blocks; retain status/flag alignment; no made-up SPDX; original legacy provenance preserved.
- Regenerate documentation from the exact canonical YAML using Python 3.12 pinned dependencies. Do not manually change generated files.
- Verify `python -m scripts.generate_docs --check`, `python -m scripts.validate_catalog`, `python -m scripts.review_debt --format json`, Ruff lint/format, `python -m pip check`, full pytest, `git diff --check`.
- Confirm official URL uniqueness and actual link audit before clearing status. Check `main` SHA and strict scope before Draft PR.
- After successful deterministic checks, commit generated docs and open Draft PR. Check remote quality, CodeQL, Gitleaks, Plumber and strict Full link audit at final SHA. Human approval before Ready or squash merge; never auto-merge.

## Final validation and review checkpoint (2026-10-29)

> **Historical checkpoints vs. current HEAD:** All successful checks below are attached to the **previous**, fully validated Wave 33 SHA `2f76f13d2734b873978d58796bb1b48cd51ca0e0`. This section is being added in a later documentation-only commit; **do not** claim the preceding checks validate its new SHA. The PR must remain Draft until the new SHA has fresh passing checks and a separately run strict link audit.

### Frozen source and scope

- Base `main` at pre-commit check: `7c0e749a7454280b93d7f032af149153d363323b` (unchanged).
- Prior validated branch HEAD: `2f76f13d2734b873978d58796bb1b48cd51ca0e0`.
- [PR #154](https://github.com/goozcena-gnl/devops-tools-catalog/pull/154) was opened in **Draft** against `main` and remained open, unmerged, without auto-merge at review time.
- The prior reviewed diff changed exactly **12 paths**: `data/tools/infrastructure-as-code.yaml`, this report, and **10 deterministically generated** documentation/statistics files. Exactly five canonical IaC IDs changed semantically; the other 30 records and historical `legacy:` entries remained intact.
- Three evidence-cleared records: `azurenamingtool` (source MIT), `terravision` (source AGPL-3.0-only), and `scalr` (commercial SaaS; **no** product-wide SPDX inherited from its separately licensed provider). `pluralith` and `terraform-aws-eks-operation-scheduler` remain `needs-review` with their unresolved support/licence boundaries. Do not claim operational runtime qualification from `active` status.

### Local and automated validation — prior SHA only

| Gate | Observed result | Provenance |
| --- | --- | --- |
| Guarded PowerShell 5.1 preflight, exact scope and provenance | **PASS** | User-provided local run log |
| Python 3.12 dependencies | **PASS**: 19 exact CI pins, Windows-only `colorama==0.4.6`, `pip check` | User-provided isolated `wave33-py312` environment log |
| Documentation generation + `--check` | **PASS**: 10 generated files | User-provided local run log |
| Catalogue validation; Ruff lint/format | **PASS** | User-provided local run log |
| Full `pytest` | **1,004 passed; 8 skipped** | User-provided local run log |
| Regenerated global inventory | **1,425** records; **847** `active`; **564** `needs-review`; **75** unknown licensing models | Generated `README.md` and `docs/catalog-statistics.json` on prior SHA |
| GitHub checks | **8/8 success** including strict audit, Catalogue quality, Gitleaks, Plumber and CodeQL jobs | [PR #154 checks](https://github.com/goozcena-gnl/devops-tools-catalog/pull/154/checks) at `2f76f13d2734b873978d58796bb1b48cd51ca0e0` |
| Separately dispatched strict Full link audit | **PASS**: `blocking_new: 0`; `blocking_known: 6`; `strict_result: PASS` | [Workflow run #40956748698](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40956748698) and [report artifact #12933948377](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40956748698/artifacts/12933948377) |
| Independent evidence/diff review | **Completed with documentary follow-up** | [Maintainer review on PR #154](https://github.com/goozcena-gnl/devops-tools-catalog/pull/154) |

The six `blocking_known` URLs were pre-existing baseline blockers; **no** exceptions were added, removed or reclassified to obtain PASS. The licence discrepancy between the EKS scheduler's tagged `LICENSE` (Apache-2.0) and same-tag README (MIT) was intentionally left unresolved. The Pluralith CLI MPL-2.0 licence does not establish the UI/API's legal terms or current maintenance.

### Post-documentation-commit release gates (not yet satisfied by this historical report)

1. Verify **only this maintenance report** changed relative to the previously validated branch HEAD; retain the 12-path overall PR allowlist and exactly five amended canonical records.
2. Record the resulting **new full commit SHA** and confirm `main` remains at the authorized base (or stop and reassess if it changed).
3. Re-run deterministic documentation check, catalogue validation, dependency/format/lint checks and full `pytest` on the **new HEAD**, or provide trustworthy CI results for the equivalent checks and note any local gates not rerun.
4. Run the **separate** `.github/workflows/link-check.yml` strict Full link audit on the new HEAD. Verify `blocking_new: 0`, `strict_result: PASS`, and separately disclose `blocking_known` from the logs/artifact. A successful check on the preceding SHA is **not** sufficient.
5. Update [PR #154](https://github.com/goozcena-gnl/devops-tools-catalog/pull/154) with links to results on the final SHA; obtain **explicit human authorization** before Ready for Review and a separate explicit decision before any merge. **Never enable auto-merge.**
