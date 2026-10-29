# Wave 33 — Infrastructure as Code: evidence preparation (NOT a clearance)

**Date:** 2026-10-29 (Europe/Paris). **Status:** initial primary-source evidence pass, no canonical edits. **Human review and local deterministic verification still required.**

## Baseline / frozen scope

- Tracking issue: https://github.com/goozcena-gnl/devops-tools-catalog/issues/153
- Base `main`: `7c0e749a7454280b93d7f032af149153d363323b` (Wave 32 merged)
- Canonical YAML: `data/tools/infrastructure-as-code.yaml`, original Git blob `f49d39ebd8b3311bf63514fac811f7b41afcf3f0`.
- Exactly five selected existing IDs out of 35, 30 other records must remain untouched: `azurenamingtool`, `pluralith`, `scalr`, `terraform-aws-eks-operation-scheduler`, `terravision`.
- Main README reports 1,425 records / 567 `needs-review` before this review. No projected or verified post-patch counters.
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

This preparatory document records **reviewed official pointers and unresolved issues**, not a successful patch. The GitHub connector can write repository content but cannot execute the repository's Python 3.12 generator/tests. In the current container GitHub git transport could not resolve `github.com`, and only Python 3.13 was available. Therefore **no canonical YAML, generated documents or tests have been altered or claimed successful**. No Draft PR should be opened from this preparation-only commit.
