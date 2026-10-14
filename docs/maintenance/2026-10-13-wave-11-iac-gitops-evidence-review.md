# Evidence review Wave 11 — IaC, Terraform and GitOps foundations — 2026-10-13

Exactly the fixed ten existing records were reviewed across all 24 material fields. Nine receive **CLEAR REVIEW**; GitOps Bridge receives **RETAIN REVIEW — SPECIFIC UNRESOLVED BOUNDARY**. Stable IDs and historical provenance remain. Canonical YAML is authoritative.

Actual execution and selected verified_on date: **2026-10-13, Europe/Paris**. The requested October 8 filename was adjusted to the actual date.

## Verified baseline and scope

- Main SHA: `19deb52ef1784056ec5dcb16a73ffc56f6ee5608`; Wave 10 PR #112 merged at this SHA.
- Branch: `maintenance/wave-11-iac-gitops-evidence-review`.
- Initial working tree clean; zero open PRs. Issue #2 open, Wave 10 COMPLETED and Wave 11 NOT STARTED — READY TO SCOPE; read-only snapshot updated_at 2026-10-08T10:23:10Z.
- All nine requested counters and all ten expected initial record states matched. Optional null descriptions in the mission correspond to absent YAML properties, not explicit null values.
- Baseline CI discrepancy: post-merge validate, Plumber audit, gitleaks and both Analyze jobs succeeded; later security reruns also succeeded. The [October 12 scheduled full audit](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/38247395703) failed: 2,675 URLs, blocking_new=1, blocking_known=6. Its artifact identifies https://github.com/hashicorp/boundary as repository-archived-unexpected. This pre-existing out-of-cohort observation does not invalidate the selected cohort or authorize another record/baseline change.
- Fresh Linux Python 3.12 dependency check also detects unrelated resolver drift: Ruff expected 0.16.10, resolved 0.17.0. Constraints and workflows remain unchanged; required CI may fail at the existing drift gate. Catalogue changes and pinned-environment verification proceed separately.
- No unrelated canonical record, Waves 4–10 decision, baseline, reports/, ledger, workflows, CodeQL configuration, Python constraints, Issue #2, settings, release or tag changed. No Wave 12 work or merge.

| Rank | ID | Initial name | Canonical file | Initial debt |
|---:|---|---|---|---|
| 1 | `azure-verified-modules-avm` | Azure Verified Modules (AVM) | `data/tools/infrastructure-as-code.yaml` | needs-review/true; unknown maturity; no SPDX; no docs; verified 2026-08-03 |
| 2 | `tflint` | TFLint | `data/tools/infrastructure-as-code.yaml` | needs-review/true; unknown maturity; no SPDX; no docs; verified 2026-08-03; no official URL |
| 3 | `terraform-docs` | terraform-docs | `data/tools/infrastructure-as-code.yaml` | needs-review/true; unknown maturity; no SPDX; no docs; verified 2026-08-03 |
| 4 | `terraform-plugin-docs` | terraform-plugin-docs | `data/tools/infrastructure-as-code.yaml` | needs-review/true; unknown maturity; no SPDX; no docs; verified 2026-08-03; no official URL |
| 5 | `terrateam` | Terrateam | `data/tools/infrastructure-as-code.yaml` | needs-review/true; unknown maturity; no SPDX; no docs; verified 2026-08-03 |
| 6 | `opentaco` | OpenTaco | `data/tools/infrastructure-as-code.yaml` | needs-review/true; unknown maturity; no SPDX; no docs; verified 2026-08-03 |
| 7 | `score` | Score | `data/tools/infrastructure-as-code.yaml` | needs-review/true; unknown maturity; no SPDX; no docs; verified 2026-08-03 |
| 8 | `tofu-controller` | Tofu Controller | `data/tools/cd-gitops-release-promotion.yaml` | needs-review/true; unknown maturity; no SPDX; no docs; verified 2026-08-03 |
| 9 | `flux-operator` | Flux Operator | `data/tools/cd-gitops-release-promotion.yaml` | needs-review/true; unknown maturity; no SPDX; no docs; verified 2026-08-03; no repository |
| 10 | `gitops-bridge` | GitOps Bridge | `data/tools/cd-gitops-release-promotion.yaml` | needs-review/true; unknown maturity; no SPDX; no docs; verified 2026-08-03; no official URL |

## Evidence method and cross-record boundaries

Actual primary README, LICENSE/component licences, documentation, repository metadata and release/history feeds were read. Source-only evidence links were checked independently of the catalogue link audit. Website fetching does not establish lifecycle; redirects were discovery aids and transition statements establish identity. No stars, search snippets or third-party summaries establish fields. Maturity is an explicit editorial assessment of documented processes and current maintained scope.

AVM coordinates standards/indexes and separate modules. TFLint statically analyses language with plugins rather than executing infrastructure. terraform-docs renders module documentation; tfplugindocs renders provider documentation and may invoke Terraform for schema extraction. Terrateam continues as Stategraph Orchestration, distinct from the commercial database engine; OpenTaco is renamed Digger software and remains a separate product/company. Score is a specification, not its CLIs or deployment platform. Tofu Controller executes IaC through runners; Flux Operator installs/configures/upgrades Flux. Neither integration nor shared maintainers merges those repositories with Flux CD core. GitOps Bridge supplies patterns/examples with only the evidenced integration status.

SPDX scopes are recorded in each licence boundary: TFLint releases include MPL and BUSL, OpenTaco public components include MIT and Apache while ee is proprietary, and Flux Operator declares AGPL independently of Flux-core Apache. No repository licence is silently extended to an Enterprise distribution or managed service.

## Decisions and complete material-field review

### azure-verified-modules-avm

**Identity boundary:** The Microsoft initiative and central coordination repository are the record boundary. Bicep/Terraform implementations and registries are reached through module indexes, not contained universally in this repository.

**Repository boundary:** Retain canonical upstream Azure/Azure-Verified-Modules, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence.

**Licence/product boundary:** MIT applies to the checked central repository. Indexed modules and third-party dependencies require their own licence checks; no umbrella SPDX grant is claimed.

**Deployment/execution boundary:** deployment_models=[] is intentional for the umbrella standards/index project; individual modules execute through their chosen IaC engine. No managed service entitlement is asserted.

**Governance:** Official portal explicitly identifies Microsoft ownership, development and support, with devolved module ownership and published triage responsibilities.

**Maturity:** Established is an editorial assessment of the central initiative's maintained standards, module indexes, contributor process and documented Microsoft support; it does not certify every module.

**Lifecycle:** Current portal content, support policy and repository maintenance support active central coordination; individual modules can be orphaned.

**Remaining uncertainty:** No material central-project claim remains open. Per-module suitability, licences and lifecycle must be checked individually.

**Official/documentation URLs:** https://azure.github.io/Azure-Verified-Modules and https://azure.github.io/Azure-Verified-Modules/; checked upstream links and documentation establish the scoped entry points.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Repository identity][azure-verified-modules-avm-e1], [Identity and scope documentation][azure-verified-modules-avm-e2], [Project licence][azure-verified-modules-avm-e3], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5], [Standards and maturity][azure-verified-modules-avm-e6], [Support and lifecycle][azure-verified-modules-avm-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | azure-verified-modules-avm | azure-verified-modules-avm | [Repository identity][azure-verified-modules-avm-e1], [Identity and scope documentation][azure-verified-modules-avm-e2] | Preserve existing stable ID and imported provenance; no split or duplicate. |
| `name` | Azure Verified Modules (AVM) | Azure Verified Modules (AVM) | [Repository identity][azure-verified-modules-avm-e1], [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | Reviewed; retained: The Microsoft initiative and central coordination repository are the record boundary. Bicep/Terraform implementations and registries are reached through module indexes, not contained universally in this repository. |
| `summary` | Microsoft-curated, consistently designed Bicep and Terraform modules for Azure resources. | Microsoft-led Azure Verified Modules initiative defining standards and indexes for Bicep and Terraform resource and pattern modules; the central repository hosts governance and documentation, while implementations live in separate module repositories and registries. | [Repository identity][azure-verified-modules-avm-e1], [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | Changed: The Microsoft initiative and central coordination repository are the record boundary. Bicep/Terraform implementations and registries are reached through module indexes, not contained universally in this repository. |
| `official_url` | https://azure.github.io/Azure-Verified-Modules | https://azure.github.io/Azure-Verified-Modules | [Repository identity][azure-verified-modules-avm-e1], [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | Reviewed; retained: upstream-declared scoped entry point; preserve former pointer in sources if changed. |
| `repository_url` | https://github.com/Azure/Azure-Verified-Modules | https://github.com/Azure/Azure-Verified-Modules | [Repository identity][azure-verified-modules-avm-e1], [Identity and scope documentation][azure-verified-modules-avm-e2] | Retain canonical upstream Azure/Azure-Verified-Modules, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence. |
| `documentation_url` | *absent* | https://azure.github.io/Azure-Verified-Modules/ | [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | Add directly checked official documentation at this record boundary. |
| `categories` | infrastructure-as-code | infrastructure-as-code | [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | Reviewed; retained: editorial taxonomy mapping. Azure module standards and selection belong in infrastructure-as-code. |
| `subcategories` | Infrastructure as Code (IaC) | IaC module standards and indexes | [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | Changed: IaC module standards and indexes narrows the documented scope of Azure Verified Modules (AVM); no taxonomy contract change. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | Reviewed; retained: editorial audience mapping. Cloud and infrastructure roles select and author Azure modules using these standards. |
| `lifecycle_stages` | plan<br>build<br>deploy | plan<br>build<br>deploy | [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | Reviewed; retained: editorial workflow mapping. Module selection supports plan, module composition supports build, and separate module implementations support deploy; the central index does not execute deployments. |
| `use_when` | `[]` | Use AVM standards and indexes to select reusable Azure resource or pattern modules and review each implementation&#x27;s lifecycle, licence and support. | [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `avoid_when` | `[]` | Do not treat the central standards repository as a deployable module, or extend its MIT licence and support status to every indexed implementation. | [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `deployment_models` | `[]` | `[]` | [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | deployment_models=[] is intentional for the umbrella standards/index project; individual modules execute through their chosen IaC engine. No managed service entitlement is asserted. |
| `license_model` | oss | oss | [Project licence][azure-verified-modules-avm-e3], [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | MIT applies to the checked central repository. Indexed modules and third-party dependencies require their own licence checks; no umbrella SPDX grant is claimed. |
| `license_spdx` | *absent* | MIT | [Project licence][azure-verified-modules-avm-e3], [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | MIT applies to the checked central repository. Indexed modules and third-party dependencies require their own licence checks; no umbrella SPDX grant is claimed. |
| `commercial_offering` | *absent* | *absent* | [Project licence][azure-verified-modules-avm-e3], [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | Optional field remains absent; absence is not a denial of commercial ecosystems. |
| `maturity` | unknown | established | [Support and lifecycle][azure-verified-modules-avm-e7], [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5], [Standards and maturity][azure-verified-modules-avm-e6] | Established is an editorial assessment of the central initiative's maintained standards, module indexes, contributor process and documented Microsoft support; it does not certify every module. |
| `status` | needs-review | active | [Support and lifecycle][azure-verified-modules-avm-e7], [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5], [Standards and maturity][azure-verified-modules-avm-e6] | CLEAR REVIEW: Current portal content, support policy and repository maintenance support active central coordination; individual modules can be orphaned. |
| `repository_archived` | *absent* | `false` | [Repository identity][azure-verified-modules-avm-e1], [Identity and scope documentation][azure-verified-modules-avm-e2], [Support and lifecycle][azure-verified-modules-avm-e7] | GitHub repository API independently reports archived=false; archival observation is separate from maintenance evidence. Current portal content, support policy and repository maintenance support active central coordination; individual modules can be orphaned. |
| `alternatives` | `[]` | `[]` | [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | Retain empty optional metadata; no unsupported rankings/tags. |
| `tags` | `[]` | `[]` | [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5] | Retain empty optional metadata; no unsupported rankings/tags. |
| `verified_on` | 2026-08-03 | 2026-10-13 | [Repository identity][azure-verified-modules-avm-e1], [Identity and scope documentation][azure-verified-modules-avm-e2], [Project licence][azure-verified-modules-avm-e3], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5], [Standards and maturity][azure-verified-modules-avm-e6], [Support and lifecycle][azure-verified-modules-avm-e7] | Actual date 2026-10-13; changed only for the fixed ten records, including the reviewed inconclusive boundary. |
| `sources` | legacy:devopstools_final.md#L167 | legacy:devopstools_final.md#L167<br>https://github.com/Azure/Azure-Verified-Modules<br>https://github.com/Azure/Azure-Verified-Modules/blob/main/README.md<br>https://github.com/Azure/Azure-Verified-Modules/blob/main/LICENSE<br>https://azure.github.io/Azure-Verified-Modules/<br>https://azure.github.io/Azure-Verified-Modules/specs/<br>https://azure.github.io/Azure-Verified-Modules/help-support/module-support/ | [Repository identity][azure-verified-modules-avm-e1], [Identity and scope documentation][azure-verified-modules-avm-e2], [Project licence][azure-verified-modules-avm-e3], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5], [Standards and maturity][azure-verified-modules-avm-e6], [Support and lifecycle][azure-verified-modules-avm-e7] | Preserve all 1 existing provenance entries for Azure Verified Modules (AVM); append the primary sources linked in this row. |
| `needs_review` | `true` | `false` | [Support and lifecycle][azure-verified-modules-avm-e7], [Identity and scope documentation][azure-verified-modules-avm-e2], [Official documentation][azure-verified-modules-avm-e4], [Governance and documentation][azure-verified-modules-avm-e5], [Standards and maturity][azure-verified-modules-avm-e6] | CLEAR REVIEW: Current portal content, support policy and repository maintenance support active central coordination; individual modules can be orphaned. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[azure-verified-modules-avm-e1]: https://github.com/Azure/Azure-Verified-Modules
[azure-verified-modules-avm-e2]: https://github.com/Azure/Azure-Verified-Modules/blob/main/README.md
[azure-verified-modules-avm-e3]: https://github.com/Azure/Azure-Verified-Modules/blob/main/LICENSE
[azure-verified-modules-avm-e4]: https://azure.github.io/Azure-Verified-Modules/
[azure-verified-modules-avm-e5]: https://azure.github.io/Azure-Verified-Modules/
[azure-verified-modules-avm-e6]: https://azure.github.io/Azure-Verified-Modules/specs/
[azure-verified-modules-avm-e7]: https://azure.github.io/Azure-Verified-Modules/help-support/module-support/

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/Azure/Azure-Verified-Modules), archived=false.

### tflint

**Identity boundary:** CLI/framework for static Terraform-language analysis; provider rules are implemented by separately installed plugins. It can parse without Terraform installed.

**Repository boundary:** Retain canonical upstream terraform-linters/tflint, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence.

**Licence/product boundary:** Root LICENSE is MPL-2.0, but upstream README explicitly binds executable releases to MPL-2.0 and BUSL-1.1; LICENSE-BUSL confirms the additional grant. source-available classifies that reviewed release distribution. The conjunction does not mean interchangeable licences or apply to external plugins.

**Deployment/execution boundary:** Local/CI CLI and optional ephemeral container execution; deployment_models=[] avoids inventing a persistent server/service classification. Commercial offering is not inferred from BUSL.

**Governance:** Maintained by the terraform-linters project, with documented plugin integration and upstream release maintenance; not a HashiCorp-owned product merely because parser files derive from Terraform.

**Maturity:** Established editorial classification: documented installations, CI integration, compatibility promises, plugin architecture and maintained releases; no star-count inference.

**Lifecycle:** Current non-archived upstream and 2026 release feed support active status.

**Remaining uncertainty:** No material scoped claim remains open. Official compatibility guidance concerns Terraform syntax, not blanket support for every OpenTofu extension or every provider plugin.

**Official/documentation URLs:** https://github.com/terraform-linters/tflint and https://github.com/terraform-linters/tflint/blob/master/docs/README.md; checked upstream links and documentation establish the scoped entry points.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Repository identity][tflint-e1], [Identity and scope documentation][tflint-e2], [Project licence][tflint-e3], [Official documentation][tflint-e4], [Bundled BUSL licence][tflint-e5], [Parser licence][tflint-e6], [Parser BUSL licence][tflint-e7], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9], [Release maintenance][tflint-e10].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | tflint | tflint | [Repository identity][tflint-e1], [Identity and scope documentation][tflint-e2] | Preserve existing stable ID and imported provenance; no split or duplicate. |
| `name` | TFLint | TFLint | [Repository identity][tflint-e1], [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Reviewed; retained: CLI/framework for static Terraform-language analysis; provider rules are implemented by separately installed plugins. It can parse without Terraform installed. |
| `summary` | Terraform linter (style + provider-specific rules). | Pluggable Terraform-language linter for local and CI static analysis, including provider-specific rules. Much of the core is MPL-2.0; release binaries also include BUSL-1.1 Terraform-derived files, and external plugins have separate licences. | [Repository identity][tflint-e1], [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Changed: CLI/framework for static Terraform-language analysis; provider rules are implemented by separately installed plugins. It can parse without Terraform installed. |
| `official_url` | *absent* | https://github.com/terraform-linters/tflint | [Repository identity][tflint-e1], [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Changed: upstream-declared scoped entry point; preserve former pointer in sources if changed. |
| `repository_url` | https://github.com/terraform-linters/tflint | https://github.com/terraform-linters/tflint | [Repository identity][tflint-e1], [Identity and scope documentation][tflint-e2] | Retain canonical upstream terraform-linters/tflint, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence. |
| `documentation_url` | *absent* | https://github.com/terraform-linters/tflint/blob/master/docs/README.md | [Official documentation][tflint-e4] | Add directly checked official documentation at this record boundary. |
| `categories` | infrastructure-as-code | infrastructure-as-code | [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Reviewed; retained: editorial taxonomy mapping. Static Terraform-language analysis belongs in infrastructure-as-code. |
| `subcategories` | Infrastructure as Code (IaC) | Terraform static analysis | [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Changed: Terraform static analysis narrows the documented scope of TFLint; no taxonomy contract change. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Reviewed; retained: editorial audience mapping. Infrastructure roles use static rules to review IaC configuration. |
| `lifecycle_stages` | plan<br>build<br>deploy | develop<br>test | [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Changed: editorial workflow mapping. Develop/test captures authoring and static checks; linting does not execute infrastructure deployment. |
| `use_when` | You want to catch Terraform errors and enforce conventions before `plan`. | Run local or CI static checks for Terraform-language conventions, deprecated syntax and provider-specific errors using reviewed ruleset plugins. | [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `avoid_when` | You already have comprehensive CI validation covering the same rules. | Do not substitute linting for plan/apply, provider execution or security testing; verify syntax compatibility for OpenTofu and licences of binaries and each plugin. | [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `deployment_models` | `[]` | `[]` | [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Local/CI CLI and optional ephemeral container execution; deployment_models=[] avoids inventing a persistent server/service classification. Commercial offering is not inferred from BUSL. |
| `license_model` | oss | source-available | [Project licence][tflint-e3], [Bundled BUSL licence][tflint-e5], [Parser licence][tflint-e6], [Parser BUSL licence][tflint-e7], [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Root LICENSE is MPL-2.0, but upstream README explicitly binds executable releases to MPL-2.0 and BUSL-1.1; LICENSE-BUSL confirms the additional grant. source-available classifies that reviewed release distribution. The conjunction does not mean interchangeable licences or apply to external plugins. |
| `license_spdx` | *absent* | MPL-2.0 AND BUSL-1.1 | [Project licence][tflint-e3], [Bundled BUSL licence][tflint-e5], [Parser licence][tflint-e6], [Parser BUSL licence][tflint-e7], [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Root LICENSE is MPL-2.0, but upstream README explicitly binds executable releases to MPL-2.0 and BUSL-1.1; LICENSE-BUSL confirms the additional grant. source-available classifies that reviewed release distribution. The conjunction does not mean interchangeable licences or apply to external plugins. |
| `commercial_offering` | *absent* | *absent* | [Project licence][tflint-e3], [Bundled BUSL licence][tflint-e5], [Parser licence][tflint-e6], [Parser BUSL licence][tflint-e7], [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Optional field remains absent; absence is not a denial of commercial ecosystems. |
| `maturity` | unknown | established | [Release maintenance][tflint-e10], [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Established editorial classification: documented installations, CI integration, compatibility promises, plugin architecture and maintained releases; no star-count inference. |
| `status` | needs-review | active | [Release maintenance][tflint-e10], [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | CLEAR REVIEW: Current non-archived upstream and 2026 release feed support active status. |
| `repository_archived` | *absent* | `false` | [Repository identity][tflint-e1], [Identity and scope documentation][tflint-e2], [Release maintenance][tflint-e10] | GitHub repository API independently reports archived=false; archival observation is separate from maintenance evidence. Current non-archived upstream and 2026 release feed support active status. |
| `alternatives` | `[]` | `[]` | [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Retain empty optional metadata; no unsupported rankings/tags. |
| `tags` | `[]` | `[]` | [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | Retain empty optional metadata; no unsupported rankings/tags. |
| `verified_on` | 2026-08-03 | 2026-10-13 | [Repository identity][tflint-e1], [Identity and scope documentation][tflint-e2], [Project licence][tflint-e3], [Official documentation][tflint-e4], [Bundled BUSL licence][tflint-e5], [Parser licence][tflint-e6], [Parser BUSL licence][tflint-e7], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9], [Release maintenance][tflint-e10] | Actual date 2026-10-13; changed only for the fixed ten records, including the reviewed inconclusive boundary. |
| `sources` | legacy:2_Cloud-Infrastructure-Serverless/README.md#L64<br>legacy:devopstools_final.md#L191 | legacy:2_Cloud-Infrastructure-Serverless/README.md#L64<br>legacy:devopstools_final.md#L191<br>https://github.com/terraform-linters/tflint<br>https://github.com/terraform-linters/tflint/blob/master/README.md<br>https://github.com/terraform-linters/tflint/blob/master/LICENSE<br>https://github.com/terraform-linters/tflint/blob/master/docs/README.md<br>https://github.com/terraform-linters/tflint/blob/master/LICENSE-BUSL<br>https://github.com/terraform-linters/tflint/blob/master/terraform/LICENSE<br>https://github.com/terraform-linters/tflint/blob/master/terraform/LICENSE-BUSL<br>https://github.com/terraform-linters/tflint/blob/master/docs/user-guide/compatibility.md<br>https://github.com/terraform-linters/tflint/blob/master/docs/user-guide/plugins.md<br>https://github.com/terraform-linters/tflint/releases | [Repository identity][tflint-e1], [Identity and scope documentation][tflint-e2], [Project licence][tflint-e3], [Official documentation][tflint-e4], [Bundled BUSL licence][tflint-e5], [Parser licence][tflint-e6], [Parser BUSL licence][tflint-e7], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9], [Release maintenance][tflint-e10] | Preserve all 2 existing provenance entries for TFLint; append the primary sources linked in this row. |
| `needs_review` | `true` | `false` | [Release maintenance][tflint-e10], [Identity and scope documentation][tflint-e2], [Official documentation][tflint-e4], [Compatibility documentation][tflint-e8], [Plugin documentation][tflint-e9] | CLEAR REVIEW: Current non-archived upstream and 2026 release feed support active status. |

**Changed fields:** `summary`, `official_url`, `documentation_url`, `subcategories`, `lifecycle_stages`, `use_when`, `avoid_when`, `license_model`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[tflint-e1]: https://github.com/terraform-linters/tflint
[tflint-e2]: https://github.com/terraform-linters/tflint/blob/master/README.md
[tflint-e3]: https://github.com/terraform-linters/tflint/blob/master/LICENSE
[tflint-e4]: https://github.com/terraform-linters/tflint/blob/master/docs/README.md
[tflint-e5]: https://github.com/terraform-linters/tflint/blob/master/LICENSE-BUSL
[tflint-e6]: https://github.com/terraform-linters/tflint/blob/master/terraform/LICENSE
[tflint-e7]: https://github.com/terraform-linters/tflint/blob/master/terraform/LICENSE-BUSL
[tflint-e8]: https://github.com/terraform-linters/tflint/blob/master/docs/user-guide/compatibility.md
[tflint-e9]: https://github.com/terraform-linters/tflint/blob/master/docs/user-guide/plugins.md
[tflint-e10]: https://github.com/terraform-linters/tflint/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/terraform-linters/tflint), archived=false.

### terraform-docs

**Identity boundary:** Module documentation generator, distinct from HashiCorp tfplugindocs for provider documentation.

**Repository boundary:** Retain canonical upstream terraform-docs/terraform-docs, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence.

**Licence/product boundary:** Actual repository LICENSE grants MIT to terraform-docs software; no Terraform engine or external action licence is inherited.

**Deployment/execution boundary:** Local/CI CLI, library and one-shot container; deployment_models=[] avoids describing CLI execution as a hosted server.

**Governance:** The terraform-docs Authors and project maintain software and documentation; project release feed corroborates maintenance.

**Maturity:** Established editorial classification supported by documented formats, configurable rendering, CI/pre-commit integrations and maintained releases.

**Lifecycle:** Current README, official documentation and 2026 stable releases support active status.

**Remaining uncertainty:** No material scoped claim remains open. Generated content does not prove the correctness of an infrastructure configuration.

**Official/documentation URLs:** https://terraform-docs.io and https://terraform-docs.io/user-guide/introduction/; checked upstream links and documentation establish the scoped entry points.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Repository identity][terraform-docs-e1], [Identity and scope documentation][terraform-docs-e2], [Project licence][terraform-docs-e3], [Official documentation][terraform-docs-e4], [Release maintenance][terraform-docs-e5].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | terraform-docs | terraform-docs | [Repository identity][terraform-docs-e1], [Identity and scope documentation][terraform-docs-e2] | Preserve existing stable ID and imported provenance; no split or duplicate. |
| `name` | terraform-docs | terraform-docs | [Repository identity][terraform-docs-e1], [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Reviewed; retained: Module documentation generator, distinct from HashiCorp tfplugindocs for provider documentation. |
| `summary` | Generate documentation from Terraform modules in various output formats. | CLI and library generating Terraform module documentation from module configuration in multiple formats, with CI and pre-commit integration; it does not execute infrastructure or generate provider reference documentation. | [Repository identity][terraform-docs-e1], [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Changed: Module documentation generator, distinct from HashiCorp tfplugindocs for provider documentation. |
| `official_url` | https://terraform-docs.io | https://terraform-docs.io | [Repository identity][terraform-docs-e1], [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Reviewed; retained: upstream-declared scoped entry point; preserve former pointer in sources if changed. |
| `repository_url` | https://github.com/terraform-docs/terraform-docs | https://github.com/terraform-docs/terraform-docs | [Repository identity][terraform-docs-e1], [Identity and scope documentation][terraform-docs-e2] | Retain canonical upstream terraform-docs/terraform-docs, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence. |
| `documentation_url` | *absent* | https://terraform-docs.io/user-guide/introduction/ | [Official documentation][terraform-docs-e4] | Add directly checked official documentation at this record boundary. |
| `categories` | infrastructure-as-code | infrastructure-as-code | [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Reviewed; retained: editorial taxonomy mapping. Terraform module documentation belongs in infrastructure-as-code. |
| `subcategories` | Infrastructure as Code (IaC) | Terraform module documentation | [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Changed: Terraform module documentation narrows the documented scope of terraform-docs; no taxonomy contract change. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Reviewed; retained: editorial audience mapping. Infrastructure roles document module interfaces for consumers. |
| `lifecycle_stages` | plan<br>build<br>deploy | develop<br>build | [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Changed: editorial workflow mapping. Develop/build captures module reference preparation and CI rendering; documentation generation does not deploy infrastructure. |
| `use_when` | `[]` | Generate and check module inputs, outputs, requirements and other reference documentation locally, in CI or with pre-commit. | [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `avoid_when` | `[]` | Use separate tools for Terraform provider/plugin documentation, provider validation, security checks and infrastructure plan/apply. | [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `deployment_models` | `[]` | `[]` | [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Local/CI CLI, library and one-shot container; deployment_models=[] avoids describing CLI execution as a hosted server. |
| `license_model` | oss | oss | [Project licence][terraform-docs-e3], [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Actual repository LICENSE grants MIT to terraform-docs software; no Terraform engine or external action licence is inherited. |
| `license_spdx` | *absent* | MIT | [Project licence][terraform-docs-e3], [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Actual repository LICENSE grants MIT to terraform-docs software; no Terraform engine or external action licence is inherited. |
| `commercial_offering` | *absent* | *absent* | [Project licence][terraform-docs-e3], [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Optional field remains absent; absence is not a denial of commercial ecosystems. |
| `maturity` | unknown | established | [Release maintenance][terraform-docs-e5], [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Established editorial classification supported by documented formats, configurable rendering, CI/pre-commit integrations and maintained releases. |
| `status` | needs-review | active | [Release maintenance][terraform-docs-e5], [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | CLEAR REVIEW: Current README, official documentation and 2026 stable releases support active status. |
| `repository_archived` | *absent* | `false` | [Repository identity][terraform-docs-e1], [Identity and scope documentation][terraform-docs-e2], [Release maintenance][terraform-docs-e5] | GitHub repository API independently reports archived=false; archival observation is separate from maintenance evidence. Current README, official documentation and 2026 stable releases support active status. |
| `alternatives` | `[]` | `[]` | [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Retain empty optional metadata; no unsupported rankings/tags. |
| `tags` | `[]` | `[]` | [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | Retain empty optional metadata; no unsupported rankings/tags. |
| `verified_on` | 2026-08-03 | 2026-10-13 | [Repository identity][terraform-docs-e1], [Identity and scope documentation][terraform-docs-e2], [Project licence][terraform-docs-e3], [Official documentation][terraform-docs-e4], [Release maintenance][terraform-docs-e5] | Actual date 2026-10-13; changed only for the fixed ten records, including the reviewed inconclusive boundary. |
| `sources` | legacy:devopstools_final.md#L185 | legacy:devopstools_final.md#L185<br>https://github.com/terraform-docs/terraform-docs<br>https://github.com/terraform-docs/terraform-docs/blob/master/README.md<br>https://github.com/terraform-docs/terraform-docs/blob/master/LICENSE<br>https://terraform-docs.io/user-guide/introduction/<br>https://github.com/terraform-docs/terraform-docs/releases | [Repository identity][terraform-docs-e1], [Identity and scope documentation][terraform-docs-e2], [Project licence][terraform-docs-e3], [Official documentation][terraform-docs-e4], [Release maintenance][terraform-docs-e5] | Preserve all 1 existing provenance entries for terraform-docs; append the primary sources linked in this row. |
| `needs_review` | `true` | `false` | [Release maintenance][terraform-docs-e5], [Identity and scope documentation][terraform-docs-e2], [Official documentation][terraform-docs-e4] | CLEAR REVIEW: Current README, official documentation and 2026 stable releases support active status. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `lifecycle_stages`, `use_when`, `avoid_when`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[terraform-docs-e1]: https://github.com/terraform-docs/terraform-docs
[terraform-docs-e2]: https://github.com/terraform-docs/terraform-docs/blob/master/README.md
[terraform-docs-e3]: https://github.com/terraform-docs/terraform-docs/blob/master/LICENSE
[terraform-docs-e4]: https://terraform-docs.io/user-guide/introduction/
[terraform-docs-e5]: https://github.com/terraform-docs/terraform-docs/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/terraform-docs/terraform-docs), archived=false.

### terraform-plugin-docs

**Identity boundary:** HashiCorp's provider/plugin documentation tooling, primarily tfplugindocs; not Terraform module docs or a provider validation runtime.

**Repository boundary:** Retain canonical upstream hashicorp/terraform-plugin-docs, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence.

**Licence/product boundary:** Direct LICENSE is MPL-2.0 with IBM copyright. It is not BUSL simply because other HashiCorp products use BUSL; Terraform invoked for schema extraction has its own terms.

**Deployment/execution boundary:** Local/CI CLI; default operation builds provider code and calls Terraform init/providers schema, or accepts pre-generated schema. deployment_models=[] is intentional.

**Governance:** HashiCorp upstream repository and IBM copyright establish project/vendor scope without inferring ownership of unrelated terraform-docs.

**Maturity:** Established editorial assessment: maintained provider documentation tooling with generation, migration, validation and Registry guidance; current stable releases.

**Lifecycle:** 2026 release and current non-archived maintained repository support active status.

**Remaining uncertainty:** No material scoped claim remains open. This does not promise arbitrary OpenTofu schema compatibility or validate provider behaviour.

**Official/documentation URLs:** https://github.com/hashicorp/terraform-plugin-docs and https://github.com/hashicorp/terraform-plugin-docs/blob/main/README.md; checked upstream links and documentation establish the scoped entry points.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Repository identity][terraform-plugin-docs-e1], [Identity and scope documentation][terraform-plugin-docs-e2], [Project licence][terraform-plugin-docs-e3], [Official documentation][terraform-plugin-docs-e4], [Release maintenance][terraform-plugin-docs-e5].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | terraform-plugin-docs | terraform-plugin-docs | [Repository identity][terraform-plugin-docs-e1], [Identity and scope documentation][terraform-plugin-docs-e2] | Preserve existing stable ID and imported provenance; no split or duplicate. |
| `name` | terraform-plugin-docs | terraform-plugin-docs | [Repository identity][terraform-plugin-docs-e1], [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Reviewed; retained: HashiCorp's provider/plugin documentation tooling, primarily tfplugindocs; not Terraform module docs or a provider validation runtime. |
| `summary` | Generate and validate Terraform provider/plugin documentation from source. | HashiCorp tfplugindocs CLI and packages generate, migrate and validate Terraform provider/plugin documentation using examples, templates and provider schema; distinct from terraform-docs for modules. | [Repository identity][terraform-plugin-docs-e1], [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Changed: HashiCorp's provider/plugin documentation tooling, primarily tfplugindocs; not Terraform module docs or a provider validation runtime. |
| `official_url` | *absent* | https://github.com/hashicorp/terraform-plugin-docs | [Repository identity][terraform-plugin-docs-e1], [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Changed: upstream-declared scoped entry point; preserve former pointer in sources if changed. |
| `repository_url` | https://github.com/hashicorp/terraform-plugin-docs | https://github.com/hashicorp/terraform-plugin-docs | [Repository identity][terraform-plugin-docs-e1], [Identity and scope documentation][terraform-plugin-docs-e2] | Retain canonical upstream hashicorp/terraform-plugin-docs, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence. |
| `documentation_url` | *absent* | https://github.com/hashicorp/terraform-plugin-docs/blob/main/README.md | [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Add directly checked official documentation at this record boundary. |
| `categories` | infrastructure-as-code | infrastructure-as-code | [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Reviewed; retained: editorial taxonomy mapping. Terraform provider documentation belongs in infrastructure-as-code. |
| `subcategories` | Infrastructure as Code (IaC) | Terraform provider documentation | [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Changed: Terraform provider documentation narrows the documented scope of terraform-plugin-docs; no taxonomy contract change. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Reviewed; retained: editorial audience mapping. Infrastructure roles author and maintain provider references. |
| `lifecycle_stages` | plan<br>build<br>deploy | develop<br>build | [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Changed: editorial workflow mapping. Develop/build captures provider documentation generation and validation; schema extraction is distinct from infrastructure deployment. |
| `use_when` | `[]` | Maintain Terraform provider reference documentation from templates, examples and provider schema, and validate Registry documentation structure. | [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `avoid_when` | `[]` | Do not use provider documentation generation as module documentation generation, provider correctness testing or infrastructure deployment; default schema extraction builds the provider and invokes Terraform. | [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `deployment_models` | `[]` | `[]` | [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Local/CI CLI; default operation builds provider code and calls Terraform init/providers schema, or accepts pre-generated schema. deployment_models=[] is intentional. |
| `license_model` | oss | oss | [Project licence][terraform-plugin-docs-e3], [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Direct LICENSE is MPL-2.0 with IBM copyright. It is not BUSL simply because other HashiCorp products use BUSL; Terraform invoked for schema extraction has its own terms. |
| `license_spdx` | *absent* | MPL-2.0 | [Project licence][terraform-plugin-docs-e3], [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Direct LICENSE is MPL-2.0 with IBM copyright. It is not BUSL simply because other HashiCorp products use BUSL; Terraform invoked for schema extraction has its own terms. |
| `commercial_offering` | *absent* | *absent* | [Project licence][terraform-plugin-docs-e3], [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Optional field remains absent; absence is not a denial of commercial ecosystems. |
| `maturity` | unknown | established | [Release maintenance][terraform-plugin-docs-e5], [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Established editorial assessment: maintained provider documentation tooling with generation, migration, validation and Registry guidance; current stable releases. |
| `status` | needs-review | active | [Release maintenance][terraform-plugin-docs-e5], [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | CLEAR REVIEW: 2026 release and current non-archived maintained repository support active status. |
| `repository_archived` | *absent* | `false` | [Repository identity][terraform-plugin-docs-e1], [Identity and scope documentation][terraform-plugin-docs-e2], [Release maintenance][terraform-plugin-docs-e5] | GitHub repository API independently reports archived=false; archival observation is separate from maintenance evidence. 2026 release and current non-archived maintained repository support active status. |
| `alternatives` | `[]` | `[]` | [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Retain empty optional metadata; no unsupported rankings/tags. |
| `tags` | `[]` | `[]` | [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | Retain empty optional metadata; no unsupported rankings/tags. |
| `verified_on` | 2026-08-03 | 2026-10-13 | [Repository identity][terraform-plugin-docs-e1], [Identity and scope documentation][terraform-plugin-docs-e2], [Project licence][terraform-plugin-docs-e3], [Official documentation][terraform-plugin-docs-e4], [Release maintenance][terraform-plugin-docs-e5] | Actual date 2026-10-13; changed only for the fixed ten records, including the reviewed inconclusive boundary. |
| `sources` | legacy:devopstools_final.md#L186 | legacy:devopstools_final.md#L186<br>https://github.com/hashicorp/terraform-plugin-docs<br>https://github.com/hashicorp/terraform-plugin-docs/blob/main/README.md<br>https://github.com/hashicorp/terraform-plugin-docs/blob/main/LICENSE<br>https://github.com/hashicorp/terraform-plugin-docs/releases | [Repository identity][terraform-plugin-docs-e1], [Identity and scope documentation][terraform-plugin-docs-e2], [Project licence][terraform-plugin-docs-e3], [Official documentation][terraform-plugin-docs-e4], [Release maintenance][terraform-plugin-docs-e5] | Preserve all 1 existing provenance entries for terraform-plugin-docs; append the primary sources linked in this row. |
| `needs_review` | `true` | `false` | [Release maintenance][terraform-plugin-docs-e5], [Identity and scope documentation][terraform-plugin-docs-e2], [Official documentation][terraform-plugin-docs-e4] | CLEAR REVIEW: 2026 release and current non-archived maintained repository support active status. |

**Changed fields:** `summary`, `official_url`, `documentation_url`, `subcategories`, `lifecycle_stages`, `use_when`, `avoid_when`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[terraform-plugin-docs-e1]: https://github.com/hashicorp/terraform-plugin-docs
[terraform-plugin-docs-e2]: https://github.com/hashicorp/terraform-plugin-docs/blob/main/README.md
[terraform-plugin-docs-e3]: https://github.com/hashicorp/terraform-plugin-docs/blob/main/LICENSE
[terraform-plugin-docs-e4]: https://github.com/hashicorp/terraform-plugin-docs/blob/main/README.md
[terraform-plugin-docs-e5]: https://github.com/hashicorp/terraform-plugin-docs/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/hashicorp/terraform-plugin-docs), archived=false.

### terrateam

**Identity boundary:** The official About page says Terrateam's orchestration engine lives on as Stategraph Orchestration. Stable id terrateam remains; current display name scopes that continuing component rather than all Stategraph database functionality.

**Repository boundary:** The old terrateamio/terrateam pointer resolves to stategraph/stategraph. Official transition history and current README independently corroborate continuity. Preserve both old repository and terrateam.io in sources.

**Licence/product boundary:** Open-core remains accurate: actual upstream grant MPL-2.0 for source; official edition documentation distinguishes commercial Enterprise and Infrastructure as a Database. Software grant does not extend to hosted service entitlements.

**Deployment/execution boundary:** self-hosted and saas describe the orchestration control plane; plans/applies run on GitHub Actions/GitLab CI runners. Commercial database engine is separately adopted and not included in this record's OSS claim.

**Governance:** Stategraph official history names the Terrateam founders and continuing orchestration engine; README links the current project and edition docs.

**Maturity:** Established editorial classification for the continuing orchestration engine, supported by official operating history, documented workflows/editions and current releases; no maturity claim for the entire newer database product.

**Lifecycle:** Current release feed and maintained orchestration documentation support active continuation, not archival of Terrateam merely because URLs redirect.

**Remaining uncertainty:** No material orchestration identity/licence boundary remains open. Current edition limits and enterprise entitlements must be assessed at adoption time.

**Official/documentation URLs:** https://stategraph.com and https://stategraph.com/docs/orchestration; checked upstream links and documentation establish the scoped entry points.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Repository identity][terrateam-e1], [Identity and scope documentation][terrateam-e2], [Project licence][terrateam-e3], [Official documentation][terrateam-e4], [Official identity transition and governance][terrateam-e5], [Edition licence and execution boundaries][terrateam-e6], [Historical open-core notice][terrateam-e7], [Release maintenance][terrateam-e8].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | terrateam | terrateam | [Repository identity][terrateam-e1], [Identity and scope documentation][terrateam-e2], [Official identity transition and governance][terrateam-e5] | Preserve existing stable ID and imported provenance; no split or duplicate. |
| `name` | Terrateam | Stategraph Orchestration (formerly Terrateam) | [Repository identity][terrateam-e1], [Identity and scope documentation][terrateam-e2], [Official identity transition and governance][terrateam-e5], [Official documentation][terrateam-e4] | Changed: The official About page says Terrateam's orchestration engine lives on as Stategraph Orchestration. Stable id terrateam remains; current display name scopes that continuing component rather than all Stategraph database functionality. |
| `summary` | GitOps-style Terraform pull-request automation with collaboration features. | Stategraph Orchestration, formerly Terrateam, automates Terraform/OpenTofu plans and applies through GitHub or GitLab pull requests and CI runners. Its MPL-2.0 open-source core is distinct from commercial Enterprise, hosted services and Stategraph Infrastructure as a Database. | [Repository identity][terrateam-e1], [Identity and scope documentation][terrateam-e2], [Official identity transition and governance][terrateam-e5], [Official documentation][terrateam-e4] | Changed: The official About page says Terrateam's orchestration engine lives on as Stategraph Orchestration. Stable id terrateam remains; current display name scopes that continuing component rather than all Stategraph database functionality. |
| `official_url` | https://terrateam.io | https://stategraph.com | [Repository identity][terrateam-e1], [Identity and scope documentation][terrateam-e2], [Official identity transition and governance][terrateam-e5], [Official documentation][terrateam-e4] | Changed: upstream-declared scoped entry point; preserve former pointer in sources if changed. |
| `repository_url` | https://github.com/terrateamio/terrateam | https://github.com/stategraph/stategraph | [Repository identity][terrateam-e1], [Identity and scope documentation][terrateam-e2], [Official identity transition and governance][terrateam-e5] | The old terrateamio/terrateam pointer resolves to stategraph/stategraph. Official transition history and current README independently corroborate continuity. Preserve both old repository and terrateam.io in sources. |
| `documentation_url` | *absent* | https://stategraph.com/docs/orchestration | [Official documentation][terrateam-e4] | Add directly checked official documentation at this record boundary. |
| `categories` | infrastructure-as-code | infrastructure-as-code | [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4] | Reviewed; retained: editorial taxonomy mapping. IaC pull-request orchestration belongs in infrastructure-as-code. |
| `subcategories` | Collaborative Infrastructure | Collaborative Infrastructure | [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4] | Reviewed; retained: Collaborative Infrastructure narrows the documented scope of Stategraph Orchestration (formerly Terrateam); no taxonomy contract change. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4] | Reviewed; retained: editorial audience mapping. Cloud/infrastructure roles coordinate reviewed infrastructure workflows. |
| `lifecycle_stages` | plan<br>build<br>deploy | plan<br>build<br>deploy | [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4] | Reviewed; retained: editorial workflow mapping. Plan/build/deploy describes pull-request planning, CI workflow processing and IaC applies on separate CI runners. |
| `use_when` | You want GitHub-native Terraform automation with access controls and apply locks. | Coordinate IaC pull-request plans, applies, locking and drift on your CI runners using a self-hosted orchestration server or the hosted offering. | [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `avoid_when` | You use GitLab/Bitbucket or prefer a fully self-hosted solution. | Do not assume MPL-2.0 covers Enterprise or Infrastructure as a Database, or that open-source editions include every governance feature; review current edition and service terms. | [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `deployment_models` | `[]` | self-hosted<br>saas | [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4] | self-hosted and saas describe the orchestration control plane; plans/applies run on GitHub Actions/GitLab CI runners. Commercial database engine is separately adopted and not included in this record's OSS claim. |
| `license_model` | open-core | open-core | [Project licence][terrateam-e3], [Edition licence and execution boundaries][terrateam-e6], [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4] | Open-core remains accurate: actual upstream grant MPL-2.0 for source; official edition documentation distinguishes commercial Enterprise and Infrastructure as a Database. Software grant does not extend to hosted service entitlements. |
| `license_spdx` | *absent* | MPL-2.0 | [Project licence][terrateam-e3], [Edition licence and execution boundaries][terrateam-e6], [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4] | Open-core remains accurate: actual upstream grant MPL-2.0 for source; official edition documentation distinguishes commercial Enterprise and Infrastructure as a Database. Software grant does not extend to hosted service entitlements. |
| `commercial_offering` | *absent* | `true` | [Project licence][terrateam-e3], [Edition licence and execution boundaries][terrateam-e6], [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4] | Commercial/Enterprise offering directly documented; software SPDX does not establish service entitlements. |
| `maturity` | unknown | established | [Release maintenance][terrateam-e8], [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4], [Official identity transition and governance][terrateam-e5] | Established editorial classification for the continuing orchestration engine, supported by official operating history, documented workflows/editions and current releases; no maturity claim for the entire newer database product. |
| `status` | needs-review | active | [Release maintenance][terrateam-e8], [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4], [Official identity transition and governance][terrateam-e5] | CLEAR REVIEW: Current release feed and maintained orchestration documentation support active continuation, not archival of Terrateam merely because URLs redirect. |
| `repository_archived` | *absent* | `false` | [Repository identity][terrateam-e1], [Identity and scope documentation][terrateam-e2], [Official identity transition and governance][terrateam-e5], [Release maintenance][terrateam-e8] | GitHub repository API independently reports archived=false; archival observation is separate from maintenance evidence. Current release feed and maintained orchestration documentation support active continuation, not archival of Terrateam merely because URLs redirect. |
| `alternatives` | `[]` | `[]` | [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4] | Retain empty optional metadata; no unsupported rankings/tags. |
| `tags` | `[]` | `[]` | [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4] | Retain empty optional metadata; no unsupported rankings/tags. |
| `verified_on` | 2026-08-03 | 2026-10-13 | [Repository identity][terrateam-e1], [Identity and scope documentation][terrateam-e2], [Project licence][terrateam-e3], [Official documentation][terrateam-e4], [Official identity transition and governance][terrateam-e5], [Edition licence and execution boundaries][terrateam-e6], [Historical open-core notice][terrateam-e7], [Release maintenance][terrateam-e8] | Actual date 2026-10-13; changed only for the fixed ten records, including the reviewed inconclusive boundary. |
| `sources` | legacy:2_Cloud-Infrastructure-Serverless/README.md#L126<br>legacy:devopstools_final.md#L225 | legacy:2_Cloud-Infrastructure-Serverless/README.md#L126<br>legacy:devopstools_final.md#L225<br>https://github.com/stategraph/stategraph<br>https://github.com/stategraph/stategraph/blob/main/README.md<br>https://github.com/stategraph/stategraph/blob/main/LICENSE<br>https://stategraph.com/docs/orchestration<br>https://stategraph.com/about<br>https://stategraph.com/docs/get-started/editions<br>https://stategraph.com/blog/terrateam-open-source<br>https://github.com/stategraph/stategraph/releases<br>https://terrateam.io<br>https://github.com/terrateamio/terrateam | [Repository identity][terrateam-e1], [Identity and scope documentation][terrateam-e2], [Project licence][terrateam-e3], [Official documentation][terrateam-e4], [Official identity transition and governance][terrateam-e5], [Edition licence and execution boundaries][terrateam-e6], [Historical open-core notice][terrateam-e7], [Release maintenance][terrateam-e8] | Preserve all 2 existing provenance entries for Terrateam; append the primary sources linked in this row. Preserve former official_url https://terrateam.io as historical provenance. Preserve former repository_url https://github.com/terrateamio/terrateam as historical provenance. |
| `needs_review` | `true` | `false` | [Release maintenance][terrateam-e8], [Identity and scope documentation][terrateam-e2], [Official documentation][terrateam-e4], [Official identity transition and governance][terrateam-e5] | CLEAR REVIEW: Current release feed and maintained orchestration documentation support active continuation, not archival of Terrateam merely because URLs redirect. |

**Changed fields:** `name`, `summary`, `official_url`, `repository_url`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[terrateam-e1]: https://github.com/stategraph/stategraph
[terrateam-e2]: https://github.com/stategraph/stategraph/blob/main/README.md
[terrateam-e3]: https://github.com/stategraph/stategraph/blob/main/LICENSE
[terrateam-e4]: https://stategraph.com/docs/orchestration
[terrateam-e5]: https://stategraph.com/about
[terrateam-e6]: https://stategraph.com/docs/get-started/editions
[terrateam-e7]: https://stategraph.com/blog/terrateam-open-source
[terrateam-e8]: https://github.com/stategraph/stategraph/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/stategraph/stategraph), archived=false.

### opentaco

**Identity boundary:** Upstream README explicitly rebrands the software from Digger to OpenTaco while the company remains Digger; current documentation confirms the expanded platform. Keep stable id opentaco and current diggerhq/digger upstream.

**Repository boundary:** Retain canonical upstream diggerhq/digger, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence.

**Licence/product boundary:** MIT root grant and Apache-2.0 backend grant apply to public core components; ee/LICENSE has separate proprietary production subscription terms. open-core replaces blanket oss; MIT AND Apache-2.0 scopes public components and excludes ee and service terms.

**Deployment/execution boundary:** self-hosted is directly documented for the platform. PR jobs run in existing CI with an orchestrator backend; beta remote runs use separate sandbox environments. Hosted/commercial material does not establish an identical licence or execution location for every service; no global saas claim added.

**Governance:** Digger remains the company per its own rebrand notice; the current upstream README/docs and separate Digger Enterprise grant establish maintainer/product continuity.

**Maturity:** Growing editorial assessment for the broader OpenTaco platform: maintained releases and documented PR/state/drift architecture, while remote runs remain explicitly beta. PR engine history does not make every new component established.

**Lifecycle:** Recent 2026 releases and current documentation support active project; legacy digger naming remains during the documented transition.

**Remaining uncertainty:** No material rebrand or core/Enterprise claim remains open. Deployment and maturity vary by component; beta remote runs and service terms must be checked separately.

**Official/documentation URLs:** https://opentaco.dev and https://github.com/diggerhq/digger/blob/develop/docs/introduction/introduction.mdx; checked upstream links and documentation establish the scoped entry points.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Repository identity][opentaco-e1], [Identity and scope documentation][opentaco-e2], [Project licence][opentaco-e3], [Official documentation][opentaco-e4], [Backend licence][opentaco-e5], [Enterprise licence][opentaco-e6], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8], [Release maintenance][opentaco-e9].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | opentaco | opentaco | [Repository identity][opentaco-e1], [Identity and scope documentation][opentaco-e2] | Preserve existing stable ID and imported provenance; no split or duplicate. |
| `name` | OpenTaco | OpenTaco | [Repository identity][opentaco-e1], [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | Reviewed; retained: Upstream README explicitly rebrands the software from Digger to OpenTaco while the company remains Digger; current documentation confirms the expanded platform. Keep stable id opentaco and current diggerhq/digger upstream. |
| `summary` | Terraform/OpenTofu CI orchestration and pull-request automation. | OpenTaco, the renamed Digger software project, combines Terraform/OpenTofu PR plan/apply automation with state management, drift workflows and beta remote runs. CI orchestration uses a backend and CI workers; public core and backend licences are distinct from Digger Enterprise terms. | [Repository identity][opentaco-e1], [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | Changed: Upstream README explicitly rebrands the software from Digger to OpenTaco while the company remains Digger; current documentation confirms the expanded platform. Keep stable id opentaco and current diggerhq/digger upstream. |
| `official_url` | https://opentaco.dev | https://opentaco.dev | [Repository identity][opentaco-e1], [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | Reviewed; retained: upstream-declared scoped entry point; preserve former pointer in sources if changed. |
| `repository_url` | https://github.com/diggerhq/digger | https://github.com/diggerhq/digger | [Repository identity][opentaco-e1], [Identity and scope documentation][opentaco-e2] | Retain canonical upstream diggerhq/digger, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence. |
| `documentation_url` | *absent* | https://github.com/diggerhq/digger/blob/develop/docs/introduction/introduction.mdx | [Official documentation][opentaco-e4] | Add directly checked official documentation at this record boundary. |
| `categories` | infrastructure-as-code | infrastructure-as-code | [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | Reviewed; retained: editorial taxonomy mapping. Terraform/OpenTofu orchestration and state workflows belong in infrastructure-as-code. |
| `subcategories` | Collaborative Infrastructure | Collaborative Infrastructure | [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | Reviewed; retained: Collaborative Infrastructure narrows the documented scope of OpenTaco; no taxonomy contract change. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | Reviewed; retained: editorial audience mapping. Cloud/infrastructure roles manage IaC workflows and state. |
| `lifecycle_stages` | plan<br>build<br>deploy | plan<br>build<br>deploy | [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | Reviewed; retained: editorial workflow mapping. Plan/build/deploy describes plans, CI orchestration and applies; beta remote runs have a separate execution path. |
| `use_when` | You want open-source PR automation that runs in your own CI (no separate server). | Adopt PR automation in your CI, or selected state-management and drift services, with a hosted or self-hosted orchestrator as documented; review the architecture for your chosen components. | [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `avoid_when` | You need an all-in-one platform with state management and a dashboard. | Do not assume there is no backend server, that every remote-run path executes in existing CI, or that MIT/Apache-2.0 cover Enterprise code and managed-service terms. | [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `deployment_models` | `[]` | self-hosted | [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | self-hosted is directly documented for the platform. PR jobs run in existing CI with an orchestrator backend; beta remote runs use separate sandbox environments. Hosted/commercial material does not establish an identical licence or execution location for every service; no global saas claim added. |
| `license_model` | oss | open-core | [Project licence][opentaco-e3], [Backend licence][opentaco-e5], [Enterprise licence][opentaco-e6], [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | MIT root grant and Apache-2.0 backend grant apply to public core components; ee/LICENSE has separate proprietary production subscription terms. open-core replaces blanket oss; MIT AND Apache-2.0 scopes public components and excludes ee and service terms. |
| `license_spdx` | *absent* | MIT AND Apache-2.0 | [Project licence][opentaco-e3], [Backend licence][opentaco-e5], [Enterprise licence][opentaco-e6], [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | MIT root grant and Apache-2.0 backend grant apply to public core components; ee/LICENSE has separate proprietary production subscription terms. open-core replaces blanket oss; MIT AND Apache-2.0 scopes public components and excludes ee and service terms. |
| `commercial_offering` | *absent* | `true` | [Project licence][opentaco-e3], [Backend licence][opentaco-e5], [Enterprise licence][opentaco-e6], [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | Commercial/Enterprise offering directly documented; software SPDX does not establish service entitlements. |
| `maturity` | unknown | growing | [Release maintenance][opentaco-e9], [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | Growing editorial assessment for the broader OpenTaco platform: maintained releases and documented PR/state/drift architecture, while remote runs remain explicitly beta. PR engine history does not make every new component established. |
| `status` | needs-review | active | [Release maintenance][opentaco-e9], [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | CLEAR REVIEW: Recent 2026 releases and current documentation support active project; legacy digger naming remains during the documented transition. |
| `repository_archived` | *absent* | `false` | [Repository identity][opentaco-e1], [Identity and scope documentation][opentaco-e2], [Release maintenance][opentaco-e9] | GitHub repository API independently reports archived=false; archival observation is separate from maintenance evidence. Recent 2026 releases and current documentation support active project; legacy digger naming remains during the documented transition. |
| `alternatives` | `[]` | `[]` | [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | Retain empty optional metadata; no unsupported rankings/tags. |
| `tags` | `[]` | `[]` | [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | Retain empty optional metadata; no unsupported rankings/tags. |
| `verified_on` | 2026-08-03 | 2026-10-13 | [Repository identity][opentaco-e1], [Identity and scope documentation][opentaco-e2], [Project licence][opentaco-e3], [Official documentation][opentaco-e4], [Backend licence][opentaco-e5], [Enterprise licence][opentaco-e6], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8], [Release maintenance][opentaco-e9] | Actual date 2026-10-13; changed only for the fixed ten records, including the reviewed inconclusive boundary. |
| `sources` | legacy:2_Cloud-Infrastructure-Serverless/README.md#L118<br>legacy:devopstools_final.md#L221 | legacy:2_Cloud-Infrastructure-Serverless/README.md#L118<br>legacy:devopstools_final.md#L221<br>https://github.com/diggerhq/digger<br>https://github.com/diggerhq/digger/blob/develop/README.md<br>https://github.com/diggerhq/digger/blob/develop/LICENSE<br>https://github.com/diggerhq/digger/blob/develop/docs/introduction/introduction.mdx<br>https://github.com/diggerhq/digger/blob/develop/backend/LICENSE<br>https://github.com/diggerhq/digger/blob/develop/ee/LICENSE<br>https://github.com/diggerhq/digger/blob/develop/docs/self-host-and-develop/system-architecture.mdx<br>https://github.com/diggerhq/digger/blob/develop/docs/ce/state-management/overview.mdx<br>https://github.com/diggerhq/digger/releases | [Repository identity][opentaco-e1], [Identity and scope documentation][opentaco-e2], [Project licence][opentaco-e3], [Official documentation][opentaco-e4], [Backend licence][opentaco-e5], [Enterprise licence][opentaco-e6], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8], [Release maintenance][opentaco-e9] | Preserve all 2 existing provenance entries for OpenTaco; append the primary sources linked in this row. |
| `needs_review` | `true` | `false` | [Release maintenance][opentaco-e9], [Identity and scope documentation][opentaco-e2], [Official documentation][opentaco-e4], [Architecture documentation][opentaco-e7], [State documentation][opentaco-e8] | CLEAR REVIEW: Recent 2026 releases and current documentation support active project; legacy digger naming remains during the documented transition. |

**Changed fields:** `summary`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_model`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[opentaco-e1]: https://github.com/diggerhq/digger
[opentaco-e2]: https://github.com/diggerhq/digger/blob/develop/README.md
[opentaco-e3]: https://github.com/diggerhq/digger/blob/develop/LICENSE
[opentaco-e4]: https://github.com/diggerhq/digger/blob/develop/docs/introduction/introduction.mdx
[opentaco-e5]: https://github.com/diggerhq/digger/blob/develop/backend/LICENSE
[opentaco-e6]: https://github.com/diggerhq/digger/blob/develop/ee/LICENSE
[opentaco-e7]: https://github.com/diggerhq/digger/blob/develop/docs/self-host-and-develop/system-architecture.mdx
[opentaco-e8]: https://github.com/diggerhq/digger/blob/develop/docs/ce/state-management/overview.mdx
[opentaco-e9]: https://github.com/diggerhq/digger/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/diggerhq/digger), archived=false.

### score

**Identity boundary:** The workload specification and its schema are the selected record; CLIs, provisioners and deployment platforms remain implementation boundaries.

**Repository boundary:** Retain canonical upstream score-spec/spec, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence.

**Licence/product boundary:** Actual specification repository LICENSE is Apache-2.0. Retain oss for the upstream open-source specification/schema distribution, not a universal grant over implementation integrations.

**Deployment/execution boundary:** deployment_models=[] is intentional for a specification. Implementation CLIs generate target configuration and the target platform executes it.

**Governance:** Project GOVERNANCE defines maintainer oversight across score-spec repositories; official CNCF record confirms Sandbox membership, not automatic GA of implementations.

**Maturity:** Growing editorial assessment supported by evolving specification releases, maintained governance, documentation and CNCF Sandbox participation; Sandbox is not equated to established.

**Lifecycle:** 2026 schema releases and current official documentation support active specification development.

**Remaining uncertainty:** No material specification claim remains open. Target platform and provisioner behaviour belong to the selected implementation.

**Official/documentation URLs:** https://score.dev and https://docs.score.dev/docs/; checked upstream links and documentation establish the scoped entry points.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Repository identity][score-e1], [Identity and scope documentation][score-e2], [Project licence][score-e3], [Official documentation][score-e4], [Governance][score-e5], [Foundation maturity][score-e6], [Release maintenance][score-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | score | score | [Repository identity][score-e1], [Identity and scope documentation][score-e2] | Preserve existing stable ID and imported provenance; no split or duplicate. |
| `name` | Score | Score | [Repository identity][score-e1], [Identity and scope documentation][score-e2], [Official documentation][score-e4] | Reviewed; retained: The workload specification and its schema are the selected record; CLIs, provisioners and deployment platforms remain implementation boundaries. |
| `summary` | Developer-centric, platform-agnostic workload specification for defining runtime requirements once in `score.yaml` and targeting multiple environments. | Score is a platform-agnostic container workload specification expressed in score.yaml; separate implementations such as score-compose and score-k8s translate it into platform configuration. The specification repository is not a Kubernetes deployment platform. | [Repository identity][score-e1], [Identity and scope documentation][score-e2], [Official documentation][score-e4] | Changed: The workload specification and its schema are the selected record; CLIs, provisioners and deployment platforms remain implementation boundaries. |
| `official_url` | https://score.dev | https://score.dev | [Repository identity][score-e1], [Identity and scope documentation][score-e2], [Official documentation][score-e4] | Reviewed; retained: upstream-declared scoped entry point; preserve former pointer in sources if changed. |
| `repository_url` | https://github.com/score-spec/spec | https://github.com/score-spec/spec | [Repository identity][score-e1], [Identity and scope documentation][score-e2] | Retain canonical upstream score-spec/spec, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence. |
| `documentation_url` | *absent* | https://docs.score.dev/docs/ | [Official documentation][score-e4] | Add directly checked official documentation at this record boundary. |
| `categories` | infrastructure-as-code | infrastructure-as-code | [Identity and scope documentation][score-e2], [Official documentation][score-e4] | Reviewed; retained: editorial taxonomy mapping. A workload configuration specification fits the existing infrastructure-as-code taxonomy. |
| `subcategories` | Infrastructure as Code (IaC) | Workload specification | [Identity and scope documentation][score-e2], [Official documentation][score-e4] | Changed: Workload specification narrows the documented scope of Score; no taxonomy contract change. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | [Identity and scope documentation][score-e2], [Official documentation][score-e4] | Reviewed; retained: editorial audience mapping. Platform and infrastructure roles define workload contracts and implement environment translation. |
| `lifecycle_stages` | plan<br>build<br>deploy | plan<br>build<br>deploy | [Identity and scope documentation][score-e2], [Official documentation][score-e4] | Reviewed; retained: editorial workflow mapping. Plan/build/deploy describes workload declaration, translated configuration generation and target-platform deployment; the specification itself does not execute those stages. |
| `use_when` | `[]` | Define developer-owned workload requirements once and select a Score implementation and platform-specific provisioners for each target environment. | [Identity and scope documentation][score-e2], [Official documentation][score-e4] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `avoid_when` | `[]` | Do not assume the specification executes deployments, provisions every resource, or guarantees that all implementations support the same integrations. | [Identity and scope documentation][score-e2], [Official documentation][score-e4] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `deployment_models` | `[]` | `[]` | [Identity and scope documentation][score-e2], [Official documentation][score-e4] | deployment_models=[] is intentional for a specification. Implementation CLIs generate target configuration and the target platform executes it. |
| `license_model` | oss | oss | [Project licence][score-e3], [Identity and scope documentation][score-e2], [Official documentation][score-e4] | Actual specification repository LICENSE is Apache-2.0. Retain oss for the upstream open-source specification/schema distribution, not a universal grant over implementation integrations. |
| `license_spdx` | *absent* | Apache-2.0 | [Project licence][score-e3], [Identity and scope documentation][score-e2], [Official documentation][score-e4] | Actual specification repository LICENSE is Apache-2.0. Retain oss for the upstream open-source specification/schema distribution, not a universal grant over implementation integrations. |
| `commercial_offering` | *absent* | *absent* | [Project licence][score-e3], [Identity and scope documentation][score-e2], [Official documentation][score-e4] | Optional field remains absent; absence is not a denial of commercial ecosystems. |
| `maturity` | unknown | growing | [Release maintenance][score-e7], [Identity and scope documentation][score-e2], [Official documentation][score-e4], [Governance][score-e5], [Foundation maturity][score-e6] | Growing editorial assessment supported by evolving specification releases, maintained governance, documentation and CNCF Sandbox participation; Sandbox is not equated to established. |
| `status` | needs-review | active | [Release maintenance][score-e7], [Identity and scope documentation][score-e2], [Official documentation][score-e4], [Governance][score-e5], [Foundation maturity][score-e6] | CLEAR REVIEW: 2026 schema releases and current official documentation support active specification development. |
| `repository_archived` | *absent* | `false` | [Repository identity][score-e1], [Identity and scope documentation][score-e2], [Release maintenance][score-e7] | GitHub repository API independently reports archived=false; archival observation is separate from maintenance evidence. 2026 schema releases and current official documentation support active specification development. |
| `alternatives` | `[]` | `[]` | [Identity and scope documentation][score-e2], [Official documentation][score-e4] | Retain empty optional metadata; no unsupported rankings/tags. |
| `tags` | `[]` | `[]` | [Identity and scope documentation][score-e2], [Official documentation][score-e4] | Retain empty optional metadata; no unsupported rankings/tags. |
| `verified_on` | 2026-08-03 | 2026-10-13 | [Repository identity][score-e1], [Identity and scope documentation][score-e2], [Project licence][score-e3], [Official documentation][score-e4], [Governance][score-e5], [Foundation maturity][score-e6], [Release maintenance][score-e7] | Actual date 2026-10-13; changed only for the fixed ten records, including the reviewed inconclusive boundary. |
| `sources` | legacy:devopstools_final.md#L183 | legacy:devopstools_final.md#L183<br>https://github.com/score-spec/spec<br>https://github.com/score-spec/spec/blob/main/README.md<br>https://github.com/score-spec/spec/blob/main/LICENSE<br>https://docs.score.dev/docs/<br>https://github.com/score-spec/spec/blob/main/GOVERNANCE.md<br>https://www.cncf.io/projects/score/<br>https://github.com/score-spec/spec/releases | [Repository identity][score-e1], [Identity and scope documentation][score-e2], [Project licence][score-e3], [Official documentation][score-e4], [Governance][score-e5], [Foundation maturity][score-e6], [Release maintenance][score-e7] | Preserve all 1 existing provenance entries for Score; append the primary sources linked in this row. |
| `needs_review` | `true` | `false` | [Release maintenance][score-e7], [Identity and scope documentation][score-e2], [Official documentation][score-e4], [Governance][score-e5], [Foundation maturity][score-e6] | CLEAR REVIEW: 2026 schema releases and current official documentation support active specification development. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[score-e1]: https://github.com/score-spec/spec
[score-e2]: https://github.com/score-spec/spec/blob/main/README.md
[score-e3]: https://github.com/score-spec/spec/blob/main/LICENSE
[score-e4]: https://docs.score.dev/docs/
[score-e5]: https://github.com/score-spec/spec/blob/main/GOVERNANCE.md
[score-e6]: https://www.cncf.io/projects/score/
[score-e7]: https://github.com/score-spec/spec/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/score-spec/spec), archived=false.

### tofu-controller

**Identity boundary:** Independent flux-iac project previously Weave TF-Controller; Flux integration does not establish membership in Flux CD core or ControlPlane Flux Operator.

**Repository boundary:** Retain canonical upstream flux-iac/tofu-controller, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence.

**Licence/product boundary:** Actual controller repository LICENSE grants Apache-2.0; selected Terraform/OpenTofu engines, providers and remote services retain separate terms.

**Deployment/execution boundary:** Self-hosted Kubernetes controller/runner architecture. Runner Pods execute plans/applies; ServiceAccount/namespace selection scopes credentials and default state is a Kubernetes Secret. Remote backend and approval configuration change the operational boundary.

**Governance:** Current flux-iac MAINTAINERS list and upstream release feed establish community maintainership without assigning Flux-core governance.

**Maturity:** Growing editorial classification: maintained controller releases and documented operating models, while Branch Planner is a Technology Preview and version compatibility must follow the support matrix.

**Lifecycle:** Current 2026 controller/runner releases and non-archived maintained upstream support active status.

**Remaining uncertainty:** No material identity/licence claim remains open. Support matrix and custom runner image govern actual engine versions; reconciliation is not a promise of universal Terraform/OpenTofu compatibility.

**Official/documentation URLs:** https://flux-iac.github.io/tofu-controller and https://flux-iac.github.io/tofu-controller/; checked upstream links and documentation establish the scoped entry points.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Repository identity][tofu-controller-e1], [Identity and scope documentation][tofu-controller-e2], [Project licence][tofu-controller-e3], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5], [Maintainers][tofu-controller-e6], [Release maintenance][tofu-controller-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | tofu-controller | tofu-controller | [Repository identity][tofu-controller-e1], [Identity and scope documentation][tofu-controller-e2] | Preserve existing stable ID and imported provenance; no split or duplicate. |
| `name` | Tofu Controller | Tofu Controller | [Repository identity][tofu-controller-e1], [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Reviewed; retained: Independent flux-iac project previously Weave TF-Controller; Flux integration does not establish membership in Flux CD core or ControlPlane Flux Operator. |
| `summary` | Flux controller for managing Terraform and OpenTofu resources the GitOps way. | Tofu Controller is the flux-iac Kubernetes controller integrating Flux with OpenTofu/Terraform reconciliation, plans, applies and drift detection through runner Pods; it is separate from Flux CD core, Flux Operator and either IaC CLI. | [Repository identity][tofu-controller-e1], [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Changed: Independent flux-iac project previously Weave TF-Controller; Flux integration does not establish membership in Flux CD core or ControlPlane Flux Operator. |
| `official_url` | https://flux-iac.github.io/tofu-controller | https://flux-iac.github.io/tofu-controller | [Repository identity][tofu-controller-e1], [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Reviewed; retained: upstream-declared scoped entry point; preserve former pointer in sources if changed. |
| `repository_url` | https://github.com/flux-iac/tofu-controller | https://github.com/flux-iac/tofu-controller | [Repository identity][tofu-controller-e1], [Identity and scope documentation][tofu-controller-e2] | Retain canonical upstream flux-iac/tofu-controller, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence. |
| `documentation_url` | *absent* | https://flux-iac.github.io/tofu-controller/ | [Official documentation][tofu-controller-e4] | Add directly checked official documentation at this record boundary. |
| `categories` | cd-gitops-release-promotion | cd-gitops-release-promotion | [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Reviewed; retained: editorial taxonomy mapping. Flux-integrated IaC reconciliation fits cd-gitops-release-promotion. |
| `subcategories` | GitOps | IaC reconciliation with Flux | [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Changed: IaC reconciliation with Flux narrows the documented scope of Tofu Controller; no taxonomy contract change. |
| `roles` | devops-engineer<br>platform-engineer<br>release-engineer | devops-engineer<br>platform-engineer<br>release-engineer | [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Reviewed; retained: editorial audience mapping. DevOps/platform/release roles operate GitOps reconciliation and approvals. |
| `lifecycle_stages` | release<br>deploy | release<br>deploy | [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Reviewed; retained: editorial workflow mapping. Release/deploy describes promotion of desired IaC configuration and runner execution driven by Flux sources. |
| `use_when` | `[]` | Reconcile Terraform/OpenTofu resources from Flux sources with explicit approvals, scoped runner credentials and a reviewed state-backend strategy. | [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `avoid_when` | `[]` | Do not assume this controller is Flux CD core or a managed Terraform service; review runner ServiceAccounts, cloud credentials, sensitive Kubernetes state Secrets and engine compatibility before automatic applies. | [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `deployment_models` | `[]` | self-hosted | [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Self-hosted Kubernetes controller/runner architecture. Runner Pods execute plans/applies; ServiceAccount/namespace selection scopes credentials and default state is a Kubernetes Secret. Remote backend and approval configuration change the operational boundary. |
| `license_model` | oss | oss | [Project licence][tofu-controller-e3], [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Actual controller repository LICENSE grants Apache-2.0; selected Terraform/OpenTofu engines, providers and remote services retain separate terms. |
| `license_spdx` | *absent* | Apache-2.0 | [Project licence][tofu-controller-e3], [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Actual controller repository LICENSE grants Apache-2.0; selected Terraform/OpenTofu engines, providers and remote services retain separate terms. |
| `commercial_offering` | *absent* | *absent* | [Project licence][tofu-controller-e3], [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Optional field remains absent; absence is not a denial of commercial ecosystems. |
| `maturity` | unknown | growing | [Release maintenance][tofu-controller-e7], [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5], [Maintainers][tofu-controller-e6] | Growing editorial classification: maintained controller releases and documented operating models, while Branch Planner is a Technology Preview and version compatibility must follow the support matrix. |
| `status` | needs-review | active | [Release maintenance][tofu-controller-e7], [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5], [Maintainers][tofu-controller-e6] | CLEAR REVIEW: Current 2026 controller/runner releases and non-archived maintained upstream support active status. |
| `repository_archived` | *absent* | `false` | [Repository identity][tofu-controller-e1], [Identity and scope documentation][tofu-controller-e2], [Release maintenance][tofu-controller-e7] | GitHub repository API independently reports archived=false; archival observation is separate from maintenance evidence. Current 2026 controller/runner releases and non-archived maintained upstream support active status. |
| `alternatives` | `[]` | `[]` | [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Retain empty optional metadata; no unsupported rankings/tags. |
| `tags` | `[]` | `[]` | [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5] | Retain empty optional metadata; no unsupported rankings/tags. |
| `verified_on` | 2026-08-03 | 2026-10-13 | [Repository identity][tofu-controller-e1], [Identity and scope documentation][tofu-controller-e2], [Project licence][tofu-controller-e3], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5], [Maintainers][tofu-controller-e6], [Release maintenance][tofu-controller-e7] | Actual date 2026-10-13; changed only for the fixed ten records, including the reviewed inconclusive boundary. |
| `sources` | legacy:devopstools_final.md#L396 | legacy:devopstools_final.md#L396<br>https://github.com/flux-iac/tofu-controller<br>https://github.com/flux-iac/tofu-controller/blob/main/README.md<br>https://github.com/flux-iac/tofu-controller/blob/main/LICENSE<br>https://flux-iac.github.io/tofu-controller/<br>https://github.com/flux-iac/tofu-controller/blob/main/docs/getting_started.md<br>https://github.com/flux-iac/tofu-controller/blob/main/MAINTAINERS<br>https://github.com/flux-iac/tofu-controller/releases | [Repository identity][tofu-controller-e1], [Identity and scope documentation][tofu-controller-e2], [Project licence][tofu-controller-e3], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5], [Maintainers][tofu-controller-e6], [Release maintenance][tofu-controller-e7] | Preserve all 1 existing provenance entries for Tofu Controller; append the primary sources linked in this row. |
| `needs_review` | `true` | `false` | [Release maintenance][tofu-controller-e7], [Identity and scope documentation][tofu-controller-e2], [Official documentation][tofu-controller-e4], [Getting-started architecture][tofu-controller-e5], [Maintainers][tofu-controller-e6] | CLEAR REVIEW: Current 2026 controller/runner releases and non-archived maintained upstream support active status. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[tofu-controller-e1]: https://github.com/flux-iac/tofu-controller
[tofu-controller-e2]: https://github.com/flux-iac/tofu-controller/blob/main/README.md
[tofu-controller-e3]: https://github.com/flux-iac/tofu-controller/blob/main/LICENSE
[tofu-controller-e4]: https://flux-iac.github.io/tofu-controller/
[tofu-controller-e5]: https://github.com/flux-iac/tofu-controller/blob/main/docs/getting_started.md
[tofu-controller-e6]: https://github.com/flux-iac/tofu-controller/blob/main/MAINTAINERS
[tofu-controller-e7]: https://github.com/flux-iac/tofu-controller/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/flux-iac/tofu-controller), archived=false.

### flux-operator

**Identity boundary:** Official project site links the ControlPlane upstream and names its maintainers. Operator manages Flux installations; Tofu Controller reconciles IaC through runners.

**Repository boundary:** Retain canonical upstream controlplaneio-fluxcd/flux-operator, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence.

**Licence/product boundary:** Actual LICENSE and source SPDX header declare AGPL-3.0; preserve upstream identifier without inventing an only/or-later grant. This copyleft software grant is not Flux core Apache-2.0 or commercial distribution/support terms.

**Deployment/execution boundary:** Self-hosted Kubernetes operator, including when installed on a managed Kubernetes cluster. ControlPlane enterprise distribution/support is an optional commercial boundary, not a claim that the operator is a SaaS.

**Governance:** Official site identifies Flux core maintainers at ControlPlane as builders; shared people do not make this separate repository subject to identical Flux-core governance.

**Maturity:** Growing editorial classification supported by maintained releases, documented CRDs and installation/configuration procedures and upstream end-to-end enterprise distribution testing; no GA parity inferred from Flux CD.

**Lifecycle:** Current 2026 releases, maintained official site and non-archived upstream support active status.

**Remaining uncertainty:** No material scoped claim remains open. Upstream uses the legacy SPDX spelling AGPL-3.0; this review does not invent a later-version permission or certify every enterprise extension.

**Official/documentation URLs:** https://fluxoperator.dev and https://fluxoperator.dev/docs/; checked upstream links and documentation establish the scoped entry points.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Repository identity][flux-operator-e1], [Identity and scope documentation][flux-operator-e2], [Project licence][flux-operator-e3], [Official documentation][flux-operator-e4], [Source licence declaration][flux-operator-e5], [Official identity and governance][flux-operator-e6], [Release maintenance][flux-operator-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | flux-operator | flux-operator | [Repository identity][flux-operator-e1], [Identity and scope documentation][flux-operator-e2], [Official identity and governance][flux-operator-e6] | Preserve existing stable ID and imported provenance; no split or duplicate. |
| `name` | Flux Operator | Flux Operator | [Repository identity][flux-operator-e1], [Identity and scope documentation][flux-operator-e2], [Official identity and governance][flux-operator-e6], [Official documentation][flux-operator-e4] | Reviewed; retained: Official project site links the ControlPlane upstream and names its maintainers. Operator manages Flux installations; Tofu Controller reconciles IaC through runners. |
| `summary` | Kubernetes operator for managing Flux CD instances. | ControlPlane-maintained Kubernetes operator installing, configuring and upgrading Flux CD instances through FluxInstance resources, with additional self-service APIs. Its AGPL-3.0 software is separate from Flux CD core and commercial ControlPlane distribution/support terms. | [Repository identity][flux-operator-e1], [Identity and scope documentation][flux-operator-e2], [Official identity and governance][flux-operator-e6], [Official documentation][flux-operator-e4] | Changed: Official project site links the ControlPlane upstream and names its maintainers. Operator manages Flux installations; Tofu Controller reconciles IaC through runners. |
| `official_url` | https://fluxoperator.dev | https://fluxoperator.dev | [Repository identity][flux-operator-e1], [Identity and scope documentation][flux-operator-e2], [Official identity and governance][flux-operator-e6], [Official documentation][flux-operator-e4] | Reviewed; retained: upstream-declared scoped entry point; preserve former pointer in sources if changed. |
| `repository_url` | *absent* | https://github.com/controlplaneio-fluxcd/flux-operator | [Repository identity][flux-operator-e1], [Identity and scope documentation][flux-operator-e2], [Official identity and governance][flux-operator-e6] | Retain canonical upstream controlplaneio-fluxcd/flux-operator, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence. |
| `documentation_url` | *absent* | https://fluxoperator.dev/docs/ | [Official documentation][flux-operator-e4] | Add directly checked official documentation at this record boundary. |
| `categories` | cd-gitops-release-promotion | cd-gitops-release-promotion | [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4] | Reviewed; retained: editorial taxonomy mapping. Declarative Flux installation lifecycle fits cd-gitops-release-promotion. |
| `subcategories` | GitOps | Flux installation lifecycle | [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4] | Changed: Flux installation lifecycle narrows the documented scope of Flux Operator; no taxonomy contract change. |
| `roles` | devops-engineer<br>platform-engineer<br>release-engineer | devops-engineer<br>platform-engineer<br>release-engineer | [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4] | Reviewed; retained: editorial audience mapping. DevOps/platform/release roles configure and upgrade Flux installations. |
| `lifecycle_stages` | release<br>deploy | release<br>deploy | [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4] | Reviewed; retained: editorial workflow mapping. Release/deploy describes Flux version rollout, installation and upgrades through FluxInstance; it does not describe Terraform execution. |
| `use_when` | * You manage multiple Flux installations and want operator-driven lifecycle management. | Manage declarative Flux installation, configuration and upgrades across Kubernetes clusters using FluxInstance and the operator&#x27;s documented APIs. | [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `avoid_when` | * You run a single Flux instance and don&#x27;t need operator abstraction. | Do not inherit Flux CD core&#x27;s Apache-2.0 licence or governance, assume Enterprise distribution/support entitlements, or use Flux lifecycle management as a Terraform/OpenTofu execution controller. | [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `deployment_models` | `[]` | self-hosted | [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4] | Self-hosted Kubernetes operator, including when installed on a managed Kubernetes cluster. ControlPlane enterprise distribution/support is an optional commercial boundary, not a claim that the operator is a SaaS. |
| `license_model` | oss | oss | [Project licence][flux-operator-e3], [Source licence declaration][flux-operator-e5], [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4] | Actual LICENSE and source SPDX header declare AGPL-3.0; preserve upstream identifier without inventing an only/or-later grant. This copyleft software grant is not Flux core Apache-2.0 or commercial distribution/support terms. |
| `license_spdx` | *absent* | AGPL-3.0 | [Project licence][flux-operator-e3], [Source licence declaration][flux-operator-e5], [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4] | Actual LICENSE and source SPDX header declare AGPL-3.0; preserve upstream identifier without inventing an only/or-later grant. This copyleft software grant is not Flux core Apache-2.0 or commercial distribution/support terms. |
| `commercial_offering` | *absent* | `true` | [Project licence][flux-operator-e3], [Source licence declaration][flux-operator-e5], [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4] | Commercial/Enterprise offering directly documented; software SPDX does not establish service entitlements. |
| `maturity` | unknown | growing | [Release maintenance][flux-operator-e7], [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4], [Official identity and governance][flux-operator-e6] | Growing editorial classification supported by maintained releases, documented CRDs and installation/configuration procedures and upstream end-to-end enterprise distribution testing; no GA parity inferred from Flux CD. |
| `status` | needs-review | active | [Release maintenance][flux-operator-e7], [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4], [Official identity and governance][flux-operator-e6] | CLEAR REVIEW: Current 2026 releases, maintained official site and non-archived upstream support active status. |
| `repository_archived` | *absent* | `false` | [Repository identity][flux-operator-e1], [Identity and scope documentation][flux-operator-e2], [Official identity and governance][flux-operator-e6], [Release maintenance][flux-operator-e7] | GitHub repository API independently reports archived=false; archival observation is separate from maintenance evidence. Current 2026 releases, maintained official site and non-archived upstream support active status. |
| `alternatives` | `[]` | `[]` | [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4] | Retain empty optional metadata; no unsupported rankings/tags. |
| `tags` | `[]` | `[]` | [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4] | Retain empty optional metadata; no unsupported rankings/tags. |
| `verified_on` | 2026-08-03 | 2026-10-13 | [Repository identity][flux-operator-e1], [Identity and scope documentation][flux-operator-e2], [Project licence][flux-operator-e3], [Official documentation][flux-operator-e4], [Source licence declaration][flux-operator-e5], [Official identity and governance][flux-operator-e6], [Release maintenance][flux-operator-e7] | Actual date 2026-10-13; changed only for the fixed ten records, including the reviewed inconclusive boundary. |
| `sources` | legacy:3_CI-CD-Automation/README.md#L146<br>legacy:devopstools_final.md#L391 | legacy:3_CI-CD-Automation/README.md#L146<br>legacy:devopstools_final.md#L391<br>https://github.com/controlplaneio-fluxcd/flux-operator<br>https://github.com/controlplaneio-fluxcd/flux-operator/blob/main/README.md<br>https://github.com/controlplaneio-fluxcd/flux-operator/blob/main/LICENSE<br>https://fluxoperator.dev/docs/<br>https://github.com/controlplaneio-fluxcd/flux-operator/blob/main/cmd/operator/main.go<br>https://fluxoperator.dev/<br>https://github.com/controlplaneio-fluxcd/flux-operator/releases | [Repository identity][flux-operator-e1], [Identity and scope documentation][flux-operator-e2], [Project licence][flux-operator-e3], [Official documentation][flux-operator-e4], [Source licence declaration][flux-operator-e5], [Official identity and governance][flux-operator-e6], [Release maintenance][flux-operator-e7] | Preserve all 2 existing provenance entries for Flux Operator; append the primary sources linked in this row. |
| `needs_review` | `true` | `false` | [Release maintenance][flux-operator-e7], [Identity and scope documentation][flux-operator-e2], [Official documentation][flux-operator-e4], [Official identity and governance][flux-operator-e6] | CLEAR REVIEW: Current 2026 releases, maintained official site and non-archived upstream support active status. |

**Changed fields:** `summary`, `repository_url`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[flux-operator-e1]: https://github.com/controlplaneio-fluxcd/flux-operator
[flux-operator-e2]: https://github.com/controlplaneio-fluxcd/flux-operator/blob/main/README.md
[flux-operator-e3]: https://github.com/controlplaneio-fluxcd/flux-operator/blob/main/LICENSE
[flux-operator-e4]: https://fluxoperator.dev/docs/
[flux-operator-e5]: https://github.com/controlplaneio-fluxcd/flux-operator/blob/main/cmd/operator/main.go
[flux-operator-e6]: https://fluxoperator.dev/
[flux-operator-e7]: https://github.com/controlplaneio-fluxcd/flux-operator/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/controlplaneio-fluxcd/flux-operator), archived=false.

### gitops-bridge

**Identity boundary:** Community architecture pattern and examples/templates, not an executable platform. README distinguishes Terraform/Argo CD stable example from Flux work in progress.

**Repository boundary:** Retain canonical upstream gitops-bridge-dev/gitops-bridge, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence.

**Licence/product boundary:** Actual example repository LICENSE grants Apache-2.0 to its content/code; that grant does not license Terraform, Helm charts, Argo CD/Flux or commercial services universally.

**Deployment/execution boundary:** deployment_models=[] is intentional: a pattern has no independent control plane to deploy. Examples provision clusters and hand metadata to a selected GitOps engine.

**Governance:** README identifies a community project. Checked upstream history does not establish a current maintainer/support commitment; no vendor or CNCF ownership is inferred from Argo/Flux usage.

**Maturity:** Retain unknown. Stable label for one 2023/2024-era Terraform/Argo example is insufficient for current project-wide established maturity or a current maintained-software classification.

**Lifecycle:** Repository reports archived=false, but latest checked commits date to July 2024 and only release to November 2023. These observations do not prove abandonment; active maintenance remains unresolved.

**Remaining uncertainty:** Material remaining boundary: current maintenance/support and project-wide maturity, including compatibility of examples and unfinished Flux path. Keep needs-review/true rather than force active or archived.

**Official/documentation URLs:** https://github.com/gitops-bridge-dev/gitops-bridge and https://github.com/gitops-bridge-dev/gitops-bridge/blob/main/README.md; checked upstream links and documentation establish the scoped entry points.

**Disposition: RETAIN REVIEW — SPECIFIC UNRESOLVED BOUNDARY**

**Primary sources checked:** [Repository identity][gitops-bridge-e1], [Identity and scope documentation][gitops-bridge-e2], [Project licence][gitops-bridge-e3], [Official documentation][gitops-bridge-e4], [Commit-history maintenance evidence][gitops-bridge-e5], [Release maintenance][gitops-bridge-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | gitops-bridge | gitops-bridge | [Repository identity][gitops-bridge-e1], [Identity and scope documentation][gitops-bridge-e2] | Preserve existing stable ID and imported provenance; no split or duplicate. |
| `name` | GitOps Bridge | GitOps Bridge | [Repository identity][gitops-bridge-e1], [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Reviewed; retained: Community architecture pattern and examples/templates, not an executable platform. README distinguishes Terraform/Argo CD stable example from Flux work in progress. |
| `summary` | GitOps bridge for Kubernetes deployments. | GitOps Bridge is a community pattern and example repository passing cluster-provisioning metadata from IaC to GitOps-managed Kubernetes addons and workloads. Its Terraform/Argo CD example is described as stable; Flux integration is listed as in progress, not universal executable-platform support. | [Repository identity][gitops-bridge-e1], [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Changed: Community architecture pattern and examples/templates, not an executable platform. README distinguishes Terraform/Argo CD stable example from Flux work in progress. |
| `official_url` | *absent* | https://github.com/gitops-bridge-dev/gitops-bridge | [Repository identity][gitops-bridge-e1], [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Changed: upstream-declared scoped entry point; preserve former pointer in sources if changed. |
| `repository_url` | https://github.com/gitops-bridge-dev/gitops-bridge | https://github.com/gitops-bridge-dev/gitops-bridge | [Repository identity][gitops-bridge-e1], [Identity and scope documentation][gitops-bridge-e2] | Retain canonical upstream gitops-bridge-dev/gitops-bridge, independently linked by project documentation and checked README. Repository archived=false is an observation, not the sole lifecycle evidence. |
| `documentation_url` | *absent* | https://github.com/gitops-bridge-dev/gitops-bridge/blob/main/README.md | [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Add directly checked official documentation at this record boundary. |
| `categories` | cd-gitops-release-promotion | cd-gitops-release-promotion | [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Reviewed; retained: editorial taxonomy mapping. IaC-to-GitOps bootstrap patterns fit cd-gitops-release-promotion. |
| `subcategories` | GitOps | IaC to GitOps bootstrap patterns | [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Changed: IaC to GitOps bootstrap patterns narrows the documented scope of GitOps Bridge; no taxonomy contract change. |
| `roles` | devops-engineer<br>platform-engineer<br>release-engineer | devops-engineer<br>platform-engineer<br>release-engineer | [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Reviewed; retained: editorial audience mapping. DevOps/platform/release roles adapt bootstrap examples and GitOps metadata handoffs. |
| `lifecycle_stages` | release<br>deploy | release<br>deploy | [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Reviewed; retained: editorial workflow mapping. Release/deploy describes example bootstrap handoff to a GitOps engine; this pattern has no independent deployment runtime. |
| `use_when` | * You want to connect Terraform/IaC provisioning with ArgoCD/Flux bootstrapping. | Study and adapt the Terraform/Argo CD bootstrap examples to pass cloud resource and workload-identity metadata into GitOps configuration. | [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `avoid_when` | * You don&#x27;t use Terraform for cluster provisioning or have your own bootstrap scripts. | Do not treat the pattern as an installable platform or assume completed Flux integration; verify present maintenance and example compatibility before production adoption. | [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Changed: selection guidance derived from documented capability and limits; no ranking or blanket compatibility. |
| `deployment_models` | `[]` | `[]` | [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | deployment_models=[] is intentional: a pattern has no independent control plane to deploy. Examples provision clusters and hand metadata to a selected GitOps engine. |
| `license_model` | oss | oss | [Project licence][gitops-bridge-e3], [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Actual example repository LICENSE grants Apache-2.0 to its content/code; that grant does not license Terraform, Helm charts, Argo CD/Flux or commercial services universally. |
| `license_spdx` | *absent* | Apache-2.0 | [Project licence][gitops-bridge-e3], [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Actual example repository LICENSE grants Apache-2.0 to its content/code; that grant does not license Terraform, Helm charts, Argo CD/Flux or commercial services universally. |
| `commercial_offering` | *absent* | *absent* | [Project licence][gitops-bridge-e3], [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Optional field remains absent; absence is not a denial of commercial ecosystems. |
| `maturity` | unknown | unknown | [Commit-history maintenance evidence][gitops-bridge-e5], [Release maintenance][gitops-bridge-e6], [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Retain unknown. Stable label for one 2023/2024-era Terraform/Argo example is insufficient for current project-wide established maturity or a current maintained-software classification. |
| `status` | needs-review | needs-review | [Commit-history maintenance evidence][gitops-bridge-e5], [Release maintenance][gitops-bridge-e6], [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | RETAIN REVIEW — SPECIFIC UNRESOLVED BOUNDARY: Repository reports archived=false, but latest checked commits date to July 2024 and only release to November 2023. These observations do not prove abandonment; active maintenance remains unresolved. |
| `repository_archived` | *absent* | `false` | [Repository identity][gitops-bridge-e1], [Identity and scope documentation][gitops-bridge-e2], [Commit-history maintenance evidence][gitops-bridge-e5], [Release maintenance][gitops-bridge-e6] | GitHub repository API independently reports archived=false; archival observation is separate from maintenance evidence. Repository reports archived=false, but latest checked commits date to July 2024 and only release to November 2023. These observations do not prove abandonment; active maintenance remains unresolved. |
| `alternatives` | `[]` | `[]` | [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Retain empty optional metadata; no unsupported rankings/tags. |
| `tags` | `[]` | `[]` | [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | Retain empty optional metadata; no unsupported rankings/tags. |
| `verified_on` | 2026-08-03 | 2026-10-13 | [Repository identity][gitops-bridge-e1], [Identity and scope documentation][gitops-bridge-e2], [Project licence][gitops-bridge-e3], [Official documentation][gitops-bridge-e4], [Commit-history maintenance evidence][gitops-bridge-e5], [Release maintenance][gitops-bridge-e6] | Actual date 2026-10-13; changed only for the fixed ten records, including the reviewed inconclusive boundary. |
| `sources` | legacy:3_CI-CD-Automation/README.md#L148<br>legacy:devopstools_final.md#L393 | legacy:3_CI-CD-Automation/README.md#L148<br>legacy:devopstools_final.md#L393<br>https://github.com/gitops-bridge-dev/gitops-bridge<br>https://github.com/gitops-bridge-dev/gitops-bridge/blob/main/README.md<br>https://github.com/gitops-bridge-dev/gitops-bridge/blob/main/LICENSE<br>https://github.com/gitops-bridge-dev/gitops-bridge/commits/main/<br>https://github.com/gitops-bridge-dev/gitops-bridge/releases | [Repository identity][gitops-bridge-e1], [Identity and scope documentation][gitops-bridge-e2], [Project licence][gitops-bridge-e3], [Official documentation][gitops-bridge-e4], [Commit-history maintenance evidence][gitops-bridge-e5], [Release maintenance][gitops-bridge-e6] | Preserve all 2 existing provenance entries for GitOps Bridge; append the primary sources linked in this row. |
| `needs_review` | `true` | `true` | [Commit-history maintenance evidence][gitops-bridge-e5], [Release maintenance][gitops-bridge-e6], [Identity and scope documentation][gitops-bridge-e2], [Official documentation][gitops-bridge-e4] | RETAIN REVIEW — SPECIFIC UNRESOLVED BOUNDARY: Repository reports archived=false, but latest checked commits date to July 2024 and only release to November 2023. These observations do not prove abandonment; active maintenance remains unresolved. |

**Changed fields:** `summary`, `official_url`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `license_spdx`, `repository_archived`, `verified_on`, `sources`.

[gitops-bridge-e1]: https://github.com/gitops-bridge-dev/gitops-bridge
[gitops-bridge-e2]: https://github.com/gitops-bridge-dev/gitops-bridge/blob/main/README.md
[gitops-bridge-e3]: https://github.com/gitops-bridge-dev/gitops-bridge/blob/main/LICENSE
[gitops-bridge-e4]: https://github.com/gitops-bridge-dev/gitops-bridge/blob/main/README.md
[gitops-bridge-e5]: https://github.com/gitops-bridge-dev/gitops-bridge/commits/main/
[gitops-bridge-e6]: https://github.com/gitops-bridge-dev/gitops-bridge/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/gitops-bridge-dev/gitops-bridge), archived=false.

## Review-debt accounting

Selected **10**, cleared **9**, retained **1**. GitOps Bridge retains unknown maturity and consistent review status/flag.

| Counter | Before | After |
|---|---:|---:|
| canonical_records | 1,425 | 1,425 |
| needs_review | 726 | 717 |
| status_needs_review | 726 | 717 |
| mismatches | 0 | 0 |
| unknown_license | 80 | 80 |
| unknown_maturity | 864 | 855 |
| missing_repository | 391 | 390 |
| missing_documentation | 860 | 850 |
| missing_sources | 0 | 0 |

Review flags/statuses decrease by nine, unknown maturity by nine, missing docs by ten and missing repositories by one; mismatches remain zero. TFLint release distribution becomes source-available and OpenTaco becomes open-core, without changing the unknown-licence counter.

## Generated changes

Only generator output appears here; this report and regression tests are authored.

- `README.md`
- `docs/catalog-statistics.json`
- `docs/categories/cd-gitops-release-promotion.md`
- `docs/categories/infrastructure-as-code.md`
- `docs/lifecycle/build.md`
- `docs/lifecycle/deploy.md`
- `docs/lifecycle/develop.md`
- `docs/lifecycle/plan.md`
- `docs/lifecycle/release.md`
- `docs/lifecycle/test.md`
- `docs/roles/cloud-engineer.md`
- `docs/roles/devops-engineer.md`
- `docs/roles/infrastructure-systems-engineer.md`
- `docs/roles/platform-engineer.md`
- `docs/roles/release-engineer.md`

## Validation and full link audit

Linux Python 3.12.3 with the committed dependency pins ran the constrained editable install, fresh resolver check, Ruff, focused/full tests, generated check, catalogue validation and debt command. Windows Python 3.12.14 with pinned Ruff 0.16.10 also ran generation, catalogue validation, debt snapshots, lint/format and focused tests. In commands below, python denotes the selected interpreter.

The fresh dependency check failed; all pinned-environment code/catalogue checks passed. No check was skipped or weakened. The full Linux suite uses process-only Git CRLF interpretation (`GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=true`) for the Windows checkout, without changing Git configuration. Both test environments emitted one non-failing pytest cache-permission warning.

| Command | Outcome |
|---|---|
| `python -m pip install -e '.[dev]' -c config/python-constraints-3.12.txt` | PASS; constrained editable install |
| `python -m scripts.python_constraints --check` | FAIL; fresh Linux resolver selects Ruff 0.17.0 against committed 0.16.10; protected constraints untouched |
| `python -m ruff check scripts tests` | PASS; all checks passed |
| `python -m ruff format --check scripts tests` | PASS; 64 files already formatted |
| `python -m pytest tests/test_wave11_evidence_review.py` | PASS; 30 tests; final Linux focused run recorded |
| `python -m pytest` | PASS; 834 tests in 295.14s |
| `python -m scripts.generate_docs` | PASS; regenerated after canonical changes |
| `python -m scripts.generate_docs --check` | PASS; generated documentation current |
| `python -m scripts.validate_catalog` | PASS; catalogue validation passed |
| `python -m scripts.review_debt --format markdown --limit 30` | PASS; before/after captured; all nine counters reconciled |
| `git diff --check` | PASS; no whitespace errors |

The 30 focused cases protect the exact report cohort, review flag/status consistency and legacy provenance, directly evidenced per-project licences, AVM umbrella/module scope, TFLint release/plugin terms, module/provider documentation distinction, Stategraph/Terrateam transition and commercial boundaries, OpenTaco/Digger component licences and beta scope, Score specification/implementation boundary, distinct Flux-related controllers and retained GitOps Bridge maintenance debt. A further regression case checks record-specific workflow and provenance rationale. No prices, release counts or temporary HTTP outcomes are asserted.

`python -m scripts.check_links --strict --check-archived --workers 8 --cache-hours 0 --cache tmp/wave11/link-cache.json --json-report tmp/wave11/link-report.json --markdown-report tmp/wave11/link-report.md`

Exactly **one** fresh complete strict audit, cache-hours=0, covered **2,686 unique catalogue URLs**. `blocking_new: 0`, `blocking_known: 4`, `strict_result: PASS`. The exact final canonical URL set was compared with the result set. Source-only evidence was read separately. Raw JSON/Markdown/cache stay ignored under tmp/wave11. No generated reports/ output was committed.

The six historical exceptions remain byte-for-byte unchanged after line-ending normalization. Observed known blockers do not change that six-entry baseline. A strict result describes blocker policy, not universal URL reachability or project lifecycle.

| Classification | Count |
|---|---:|
| dns-inconclusive | 5 |
| http-error | 1 |
| manual-verification-required | 3 |
| network-inconclusive | 1 |
| permanent-redirect | 225 |
| rate-limited | 490 |
| restricted-or-bot-blocked | 574 |
| timeout-inconclusive | 1 |
| transient-failure | 1 |
| valid | 1349 |
| valid-redirect | 36 |

| URL | Raw classification | Strict status |
|---|---|---|
| https://hub.docker.com/r/soosio/dast | manual-verification-required | blocking-known |
| https://kubeflame.github.io | manual-verification-required | blocking-known |
| https://www.opentext.com/products/static-application-security-testing | http-error | blocking-known |
| https://www.yotascale.com | manual-verification-required | blocking-known |

This fresh audit received HTTP 429 (rate-limited, nonblocking) for Boundary. Its strict PASS does not resolve the earlier scheduled archived=true observation, independently confirmed through the read-only upstream API. The two historical exceptions absent from blocking_known remain in the unchanged six-entry baseline. No unrelated record was changed and no baseline entry was added to suppress the finding.

## Outstanding questions and review readiness

GitOps Bridge retains review for current maintenance/support and maturity; archived=false and a stable label on one old example do not settle those questions. Remaining component compatibility, beta status and commercial entitlements are explicitly bounded in the nine cleared records.

Local readiness is blocked by unrelated Ruff resolver drift; this fresh strict audit passed with recorded network limitations. Independent review found copied cross-record rationale in the evidence table; each taxonomy, archival and provenance row was corrected to its own record, and a focused regression check was added. Final-head CI/security and review resolution are reported in the PR and final handoff. The PR remains open and unmerged; protected-scope remedies require separate maintenance work.
