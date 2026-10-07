# Evidence review Wave 7 — 2026-10-07

Exactly ten existing canonical records were reviewed. All ten receive **CLEAR REVIEW**. Stable IDs and every previous provenance source are preserved. Canonical YAML is authoritative; generated pages were regenerated.

## Verified baseline and scope

- Main: `e1d0a68f418b06078932b6dac544f4298a39f5de` (post-Wave-6).
- Branch: `maintenance/wave-7-evidence-review`.
- Before editing: clean working tree and zero open PRs; all five exact-main check runs passed (CodeQL actions/python, Plumber, gitleaks, catalogue validate). The CodeQL alert count read during this review was zero.
- Issue #2 was read: Wave 6 is COMPLETED; Wave 7 is NOT STARTED and READY TO SCOPE. It is not edited.
- Exactly these ten IDs differ from the pre-edit snapshot of all 1,425 records. Other record blocks remain byte-for-byte unchanged. Bazel, Renovate and kube-bench move to better-fitting existing primary category files; selected records also add documented secondary categories.
- No baseline, committed audit report, link ledger, issue, workflow, CodeQL configuration, dependency constraint or unrelated record changes; no Wave 4/Wave 5/Wave 6 revisits or Wave 8 work.

This fixed cohort balances core IaC, workload/platform orchestration, Kubernetes, SCM and CI/CD, with a hosted-product rename and sensitive source-available/open-core/OSS boundaries backed by direct primary sources. All ten initially had review flag/status debt, unknown maturity and missing documentation. The rank below is the user-specified order.

| Rank | ID | Initial name | Initial category | Initial debt |
|---:|---|---|---|---|
| 1 | `terraform-cloud` | Terraform Cloud | `infrastructure-as-code` | needs-review; unknown maturity; missing docs; unknown licence; missing parent repository |
| 2 | `terraform` | Terraform | `infrastructure-as-code` | needs-review; unknown maturity; missing docs |
| 3 | `nomad` | Nomad | `kubernetes-distributions-operations` | needs-review; unknown maturity; missing docs |
| 4 | `rancher` | Rancher | `kubernetes-distributions-operations` | needs-review; unknown maturity; missing docs; missing parent repository |
| 5 | `gitlab` | GitLab | `source-control-repository-management` | needs-review; unknown maturity; missing docs |
| 6 | `renovate` | Renovate | `cd-gitops-release-promotion` | needs-review; unknown maturity; missing docs |
| 7 | `bazel` | Bazel | `containers-image-tooling` | needs-review; unknown maturity; missing docs |
| 8 | `skaffold` | Skaffold | `containers-image-tooling` | needs-review; unknown maturity; missing docs |
| 9 | `rke2` | RKE2 | `kubernetes-distributions-operations` | needs-review; unknown maturity; missing docs |
| 10 | `kube-bench` | kube-bench | `kubernetes-distributions-operations` | needs-review; unknown maturity; missing docs |

## Evidence method and interpretation

Search results were discovery aids; official documents, upstream source/licence files, release feeds and legal terms were read directly. GitHub repository metadata (`archived`, default branch and update dates) and release JSON were checked through its API. GitLab canonical project metadata and actual raw licence files were read separately; its public metadata omitted an archival flag. Link-audit responses alone do not establish lifecycle. The review date records this review action, not a vendor statement.

Maturity is a reviewer judgement from maintenance history, stable interfaces, documented operations and governance, not GitHub stars. Categories, roles and lifecycle stages map documented capabilities to the existing taxonomy. Use/avoid guidance describes selection tradeoffs, not newly invented vendor restrictions. Empty alternatives/tags and absent optional offering booleans are retained without unsupported parent-wide claims. Rancher receives its directly verified Manager repository; GitLab receives its declared canonical development upstream. HCP Terraform receives no invented source repository or SPDX. Skaffold is currently active with an explicitly announced future archive, reflected in selection guidance.

## Decisions and complete material-field review

### terraform-cloud

**Identity boundary:** Terraform Cloud was renamed HCP Terraform on 2024-04-22. Preserve terraform-cloud as the stable catalogue ID and its history; update the displayed product name. The existing official URL is already the current HCP documentation entry point and is retained.

**Licence boundary:** Commercial hosted service under its user agreement, including a limited subscription right to access/use the service. Neither the Terraform CLI BUSL nor historical MPL grants license this service; no single software SPDX is assigned.

**Commercial/product boundary:** Free and paid service plans do not make the service OSS. Terraform Enterprise is a separately offered self-hosted distribution. Private-network agents are execution/connectivity components, not a self-hosted HCP control plane.

**Lifecycle boundary:** Active service: official changelog records changes on 2026-10-02 and 2026-10-01. Rename evidence and current operational documentation independently support identity/activity.

**Repository boundary:** Leave repository_url and repository_archived absent: no public repository representing the hosted product was established. Do not substitute hashicorp/terraform or an agent/component repository.

**Maturity:** Established is an editorial judgement from the maintained service, documented state/runs/access operations and multi-edition history.

**Unresolved questions / limits:** None blocking the hosted-product boundary. Feature entitlements and agent limits depend on the service plan; no blanket entitlement or CLI-provider licence claim is made.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Official documentation and rename][terraform-cloud-e1], [Product editions and deployment boundary][terraform-cloud-e2], [Hosted-service user agreement][terraform-cloud-e3], [Agent versus control-plane documentation][terraform-cloud-e4], [Current service changelog][terraform-cloud-e5].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | terraform-cloud | terraform-cloud | [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4] | Preserve stable catalogue identity and history. |
| `name` | Terraform Cloud | HCP Terraform | [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4] | Changed: documented identity/capability; scoped boundary above applies. |
| `summary` | Managed service for Terraform workflows and state management. | HashiCorp-hosted infrastructure-as-code service for collaborative Terraform runs, state, access control and policy; Terraform Enterprise is the separate self-hosted offering. | [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://developer.hashicorp.com/terraform/cloud-docs | https://developer.hashicorp.com/terraform/cloud-docs | [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | *absent* | *absent* | [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4], [Hosted-service user agreement][terraform-cloud-e3] | Leave absent: no public full parent-product source repository established; components are not substituted. |
| `documentation_url` | *absent* | https://developer.hashicorp.com/terraform/cloud-docs | [Official documentation and rename][terraform-cloud-e1] | Add the directly identified official documentation entry point. |
| `categories` | infrastructure-as-code | infrastructure-as-code | [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Collaborative Infrastructure | Collaborative Infrastructure | [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | plan<br>build<br>deploy | plan<br>deploy<br>operate | [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You want HashiCorp-managed remote state, runs, and Sentinel policies. | You want a vendor-managed Terraform control plane for shared state, runs and governance, with agents where private infrastructure requires them. | [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4], [Hosted-service user agreement][terraform-cloud-e3] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | You want open-source tooling or need to avoid vendor dependency on HashiCorp. | You require a fully self-hosted control plane or an OSS service licence; evaluate Terraform Enterprise separately for self-hosting. | [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4], [Hosted-service user agreement][terraform-cloud-e3] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | hosted-saas | [Official documentation and rename][terraform-cloud-e1], [Hosted-service user agreement][terraform-cloud-e3], [Agent versus control-plane documentation][terraform-cloud-e4] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | unknown | commercial | [Hosted-service user agreement][terraform-cloud-e3] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | *absent* | [Hosted-service user agreement][terraform-cloud-e3] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Hosted-service user agreement][terraform-cloud-e3], [Product editions and deployment boundary][terraform-cloud-e2] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [Current service changelog][terraform-cloud-e5], [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4] | Reviewer judgement from maintained releases/service history and documented operations, explained above. |
| `status` | needs-review | active | [Current service changelog][terraform-cloud-e5], [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | *absent* | [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4], [Hosted-service user agreement][terraform-cloud-e3], [Product editions and deployment boundary][terraform-cloud-e2] | Leave absent: no verified public parent repository for HCP Terraform, or canonical GitLab metadata did not expose the flag. Do not inherit a component/mirror archival boolean. |
| `alternatives` | `[]` | `[]` | [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Official documentation and rename][terraform-cloud-e1], [Product editions and deployment boundary][terraform-cloud-e2], [Hosted-service user agreement][terraform-cloud-e3], [Agent versus control-plane documentation][terraform-cloud-e4], [Current service changelog][terraform-cloud-e5] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:2_Cloud-Infrastructure-Serverless/README.md#L124<br>legacy:devopstools_final.md#L224 | legacy:2_Cloud-Infrastructure-Serverless/README.md#L124<br>legacy:devopstools_final.md#L224<br>https://developer.hashicorp.com/terraform/cloud-docs<br>https://developer.hashicorp.com/terraform/intro/terraform-editions<br>https://www.hashicorp.com/en/hcp-terraform<br>https://developer.hashicorp.com/terraform/cloud-docs/agents<br>https://developer.hashicorp.com/terraform/cloud-docs/changelog | [Official documentation and rename][terraform-cloud-e1], [Product editions and deployment boundary][terraform-cloud-e2], [Hosted-service user agreement][terraform-cloud-e3], [Agent versus control-plane documentation][terraform-cloud-e4], [Current service changelog][terraform-cloud-e5] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Current service changelog][terraform-cloud-e5], [Official documentation and rename][terraform-cloud-e1], [Agent versus control-plane documentation][terraform-cloud-e4] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `name`, `summary`, `documentation_url`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_model`, `commercial_offering`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`.

[terraform-cloud-e1]: https://developer.hashicorp.com/terraform/cloud-docs
[terraform-cloud-e2]: https://developer.hashicorp.com/terraform/intro/terraform-editions
[terraform-cloud-e3]: https://www.hashicorp.com/en/hcp-terraform
[terraform-cloud-e4]: https://developer.hashicorp.com/terraform/cloud-docs/agents
[terraform-cloud-e5]: https://developer.hashicorp.com/terraform/cloud-docs/changelog

### terraform

**Identity boundary:** Scope explicitly to Terraform Community Edition, the downloadable CLI. Stable terraform ID and official terraform.io entry point are retained. Providers/plugins and HCP/Enterprise control planes are distinct.

**Licence boundary:** Current LICENSE identifies Terraform 1.6.0 or later as BUSL-1.1, with an additional production-use grant restricted for competitive paid hosted/embedded offerings and a per-version four-year change to MPL-2.0. Direct historical v1.5.7 licence is MPL; v1.6.0 is BUSL. Do not assign historical MPL to current source or providers.

**Commercial/product boundary:** commercial_offering=true records related official HCP Terraform and Terraform Enterprise editions, not a claim that the free downloadable CE CLI is itself a paid SaaS or that Enterprise is covered by this SPDX.

**Lifecycle boundary:** Non-archived upstream, 2026-10-07 repository activity and stable v1.16.5 on 2026-10-02 support current active maintenance. No Enterprise support entitlement is inherited.

**Repository boundary:** Retain hashicorp/terraform as the CLI graph/core source repository. Plugin implementations and their licences are separate.

**Maturity:** Established follows maintained stable CLI release lines and documented configuration/provider/state workflows, not popularity.

**Unresolved questions / limits:** None blocking CE scope. The BUSL additional-use grant and per-version conversion must be checked for the intended offering/version; separate providers retain their own licences.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical CLI repository and scope][terraform-e1], [Current source licence][terraform-e2], [Historical MPL source licence][terraform-e3], [BUSL transition source licence][terraform-e4], [Official documentation][terraform-e5], [Product editions and commercial boundary][terraform-e6], [Stable release history][terraform-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | terraform | terraform | [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5] | Preserve stable catalogue identity and history. |
| `name` | Terraform | Terraform Community Edition | [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5] | Changed: documented identity/capability; scoped boundary above applies. |
| `summary` | Infrastructure provisioning tool. | HashiCorp infrastructure-as-code CLI for provisioning and managing infrastructure and state, with separately licensed providers; HCP Terraform and Terraform Enterprise are distinct offerings. | [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://www.terraform.io | https://www.terraform.io | [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/hashicorp/terraform | https://github.com/hashicorp/terraform | [Canonical CLI repository and scope][terraform-e1], [Current source licence][terraform-e2], [Historical MPL source licence][terraform-e3], [BUSL transition source licence][terraform-e4] | Keep the verified scoped project repository. |
| `documentation_url` | *absent* | https://developer.hashicorp.com/terraform/docs | [Official documentation][terraform-e5] | Add the directly identified official documentation entry point. |
| `categories` | infrastructure-as-code | infrastructure-as-code | [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Infrastructure as Code (IaC) | Infrastructure as Code (IaC) | [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | plan<br>build<br>deploy | plan<br>deploy<br>operate | [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You need the largest provider ecosystem and industry-standard HCL workflows. | You need declarative infrastructure provisioning and state management through the CLI and can satisfy the current BUSL additional-use conditions and provider licences. | [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5], [Current source licence][terraform-e2], [Historical MPL source licence][terraform-e3], [BUSL transition source licence][terraform-e4] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | The BSL license is incompatible with your organization&#x27;s policies. | You require OSI-approved licensing for current source, cannot satisfy BUSL competitive-offering restrictions, or need a hosted collaboration control plane rather than the CLI. | [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5], [Current source licence][terraform-e2], [Historical MPL source licence][terraform-e3], [BUSL transition source licence][terraform-e4] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | local | [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | source-available | source-available | [Current source licence][terraform-e2], [Historical MPL source licence][terraform-e3], [BUSL transition source licence][terraform-e4] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | BUSL-1.1 | [Current source licence][terraform-e2], [Historical MPL source licence][terraform-e3], [BUSL transition source licence][terraform-e4] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Current source licence][terraform-e2], [Historical MPL source licence][terraform-e3], [BUSL transition source licence][terraform-e4], [Product editions and commercial boundary][terraform-e6] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [BUSL transition source licence][terraform-e4], [Stable release history][terraform-e7], [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5] | Reviewer judgement from maintained releases/service history and documented operations, explained above. |
| `status` | needs-review | active | [BUSL transition source licence][terraform-e4], [Stable release history][terraform-e7], [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical CLI repository and scope][terraform-e1] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical CLI repository and scope][terraform-e1], [Current source licence][terraform-e2], [Historical MPL source licence][terraform-e3], [BUSL transition source licence][terraform-e4], [Official documentation][terraform-e5], [Product editions and commercial boundary][terraform-e6], [Stable release history][terraform-e7] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:2_Cloud-Infrastructure-Serverless/README.md#L60<br>legacy:devopstools_final.md#L187 | legacy:2_Cloud-Infrastructure-Serverless/README.md#L60<br>legacy:devopstools_final.md#L187<br>https://github.com/hashicorp/terraform<br>https://github.com/hashicorp/terraform/blob/main/LICENSE<br>https://github.com/hashicorp/terraform/blob/v1.5.7/LICENSE<br>https://github.com/hashicorp/terraform/blob/v1.6.0/LICENSE<br>https://developer.hashicorp.com/terraform/docs<br>https://developer.hashicorp.com/terraform/intro/terraform-editions<br>https://github.com/hashicorp/terraform/releases | [Canonical CLI repository and scope][terraform-e1], [Current source licence][terraform-e2], [Historical MPL source licence][terraform-e3], [BUSL transition source licence][terraform-e4], [Official documentation][terraform-e5], [Product editions and commercial boundary][terraform-e6], [Stable release history][terraform-e7] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [BUSL transition source licence][terraform-e4], [Stable release history][terraform-e7], [Canonical CLI repository and scope][terraform-e1], [Official documentation][terraform-e5] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `name`, `summary`, `documentation_url`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[terraform-e1]: https://github.com/hashicorp/terraform
[terraform-e2]: https://github.com/hashicorp/terraform/blob/main/LICENSE
[terraform-e3]: https://github.com/hashicorp/terraform/blob/v1.5.7/LICENSE
[terraform-e4]: https://github.com/hashicorp/terraform/blob/v1.6.0/LICENSE
[terraform-e5]: https://developer.hashicorp.com/terraform/docs
[terraform-e6]: https://developer.hashicorp.com/terraform/intro/terraform-editions
[terraform-e7]: https://github.com/hashicorp/terraform/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/hashicorp/terraform) (`archived: false`).

### nomad

**Identity boundary:** Nomad schedules containers and other workloads and does not require Kubernetes. Retain the platform/orchestration category and roles, with a precise workload-orchestration subcategory.

**Licence boundary:** CE current LICENSE covers Nomad 1.7.0 or later under BUSL-1.1 with competitive-offering additional-use conditions and per-version four-year MPL conversion. Historical v1.6.3 is MPL. Source-available remains correct; documentation wording about open source does not supersede the actual grant.

**Commercial/product boundary:** Nomad Enterprise features require a valid separate licence, including IBM PAO entitlements where applicable. CE source licence and base backports do not grant Enterprise features or extended/ongoing support.

**Lifecycle boundary:** Current CE 2.0+ policy provides two years of base security/bug-fix backports under the April 2026 IBM-aligned lifecycle, with spring/fall feature releases and monthly updates. October modification does not restart that lifecycle; extended support is Enterprise-only. Non-archived upstream and stable v2.0.7 on 2026-09-18 support active status.

**Repository boundary:** Retain hashicorp/nomad; server/client agents form a self-hosted orchestrator, not a vendor-managed SaaS control plane.

**Maturity:** Established follows stable release history, documented workload operations and an explicit maintained CE lifecycle.

**Unresolved questions / limits:** None blocking CE scope. Version-specific CE base windows and Enterprise contractual entitlements must be checked independently; CE is not OSI-open-source.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and workload scope][nomad-e1], [Current CE source licence][nomad-e2], [Historical MPL source licence][nomad-e3], [Official documentation][nomad-e4], [CE versus Enterprise licence and support lifecycle][nomad-e5], [Enterprise licensing and entitlement documentation][nomad-e6], [Stable release history][nomad-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | nomad | nomad | [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6] | Preserve stable catalogue identity and history. |
| `name` | Nomad | Nomad | [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | HashiCorp scheduler. | HashiCorp workload orchestrator for containerized and non-containerized jobs; Community Edition is source-available and Enterprise features and support require separate entitlements. | [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://www.nomadproject.io | https://www.nomadproject.io | [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/hashicorp/nomad | https://github.com/hashicorp/nomad | [Canonical repository and workload scope][nomad-e1], [Current CE source licence][nomad-e2], [Historical MPL source licence][nomad-e3], [CE versus Enterprise licence and support lifecycle][nomad-e5] | Keep the verified scoped project repository. |
| `documentation_url` | *absent* | https://developer.hashicorp.com/nomad/docs | [Official documentation][nomad-e4] | Add the directly identified official documentation entry point. |
| `categories` | kubernetes-distributions-operations | kubernetes-distributions-operations | [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Kubernetes Alternatives &amp; Platforms | Workload orchestration | [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You need a simpler orchestrator that handles containers, VMs, and binaries without Kubernetes complexity. | You need a self-hosted scheduler for mixed workload types, can satisfy CE BUSL conditions and plan upgrades within the current CE backport lifecycle. | [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6], [Current CE source licence][nomad-e2], [Historical MPL source licence][nomad-e3], [CE versus Enterprise licence and support lifecycle][nomad-e5] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | You need the Kubernetes ecosystem, CRDs, or operator model. | You require an OSI-approved current source licence, Kubernetes APIs, or Enterprise features and extended support without Enterprise entitlements. | [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6], [Current CE source licence][nomad-e2], [Historical MPL source licence][nomad-e3], [CE versus Enterprise licence and support lifecycle][nomad-e5] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted | [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | source-available | source-available | [Current CE source licence][nomad-e2], [Historical MPL source licence][nomad-e3], [CE versus Enterprise licence and support lifecycle][nomad-e5] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | BUSL-1.1 | [Current CE source licence][nomad-e2], [Historical MPL source licence][nomad-e3], [CE versus Enterprise licence and support lifecycle][nomad-e5] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Current CE source licence][nomad-e2], [Historical MPL source licence][nomad-e3], [CE versus Enterprise licence and support lifecycle][nomad-e5] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [CE versus Enterprise licence and support lifecycle][nomad-e5], [Stable release history][nomad-e7], [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6] | Reviewer judgement from maintained releases/service history and documented operations, explained above. |
| `status` | needs-review | active | [CE versus Enterprise licence and support lifecycle][nomad-e5], [Stable release history][nomad-e7], [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical repository and workload scope][nomad-e1] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical repository and workload scope][nomad-e1], [Current CE source licence][nomad-e2], [Historical MPL source licence][nomad-e3], [Official documentation][nomad-e4], [CE versus Enterprise licence and support lifecycle][nomad-e5], [Enterprise licensing and entitlement documentation][nomad-e6], [Stable release history][nomad-e7] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L164<br>legacy:devopstools_final.md#L666 | legacy:4_Kubernetes-Containers/README.md#L164<br>legacy:devopstools_final.md#L666<br>https://github.com/hashicorp/nomad<br>https://github.com/hashicorp/nomad/blob/main/LICENSE<br>https://github.com/hashicorp/nomad/blob/v1.6.3/LICENSE<br>https://developer.hashicorp.com/nomad/docs<br>https://developer.hashicorp.com/nomad/docs/ce-license-support<br>https://developer.hashicorp.com/nomad/commands/license/inspect<br>https://github.com/hashicorp/nomad/releases | [Canonical repository and workload scope][nomad-e1], [Current CE source licence][nomad-e2], [Historical MPL source licence][nomad-e3], [Official documentation][nomad-e4], [CE versus Enterprise licence and support lifecycle][nomad-e5], [Enterprise licensing and entitlement documentation][nomad-e6], [Stable release history][nomad-e7] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [CE versus Enterprise licence and support lifecycle][nomad-e5], [Stable release history][nomad-e7], [Canonical repository and workload scope][nomad-e1], [Official documentation][nomad-e4], [Enterprise licensing and entitlement documentation][nomad-e6] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[nomad-e1]: https://github.com/hashicorp/nomad
[nomad-e2]: https://github.com/hashicorp/nomad/blob/main/LICENSE
[nomad-e3]: https://github.com/hashicorp/nomad/blob/v1.6.3/LICENSE
[nomad-e4]: https://developer.hashicorp.com/nomad/docs
[nomad-e5]: https://developer.hashicorp.com/nomad/docs/ce-license-support
[nomad-e6]: https://developer.hashicorp.com/nomad/commands/license/inspect
[nomad-e7]: https://github.com/hashicorp/nomad/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/hashicorp/nomad) (`archived: false`).

### rancher

**Identity boundary:** Scope the stable rancher record to Rancher Manager, the SUSE Rancher cluster management project. A manager provisioning/importing distributions is not itself interchangeable with RKE2/K3s or downstream hosted clusters.

**Licence boundary:** Correct open-core to oss: actual source LICENSE is Apache-2.0 and current Prime documentation explicitly says the Rancher project remains fully open source using the same code. Dependencies, add-ons, images and services are separate boundaries.

**Commercial/product boundary:** commercial_offering=true reflects optional Prime support, longer lifecycles and trusted distribution assets. Subscription/service benefits do not make Manager code proprietary or grant all add-on licences.

**Lifecycle boundary:** Non-archived upstream, 2026-10-07 activity and stable v2.15.2 on 2026-09-23 support active status.

**Repository boundary:** Add first-party rancher/rancher Manager meta-repository. Packaging links to other modules do not make their licences automatically identical. Manager is self-hosted even when downstream clusters are hosted.

**Maturity:** Established follows maintained 2.x releases and documented cluster provisioning/import, access and upgrade operations.

**Unresolved questions / limits:** None blocking Manager scope. Prime registry/support entitlements and separately licensed ecosystem products remain separate; no blanket support entitlement is asserted.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical Manager repository and identity][rancher-e1], [Manager source licence][rancher-e2], [Official Manager documentation][rancher-e3], [Rancher OSS versus Prime commercial boundary][rancher-e4], [Stable release history][rancher-e5].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | rancher | rancher | [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3] | Preserve stable catalogue identity and history. |
| `name` | Rancher | Rancher Manager | [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3] | Changed: documented identity/capability; scoped boundary above applies. |
| `summary` | Kubernetes management platform by SUSE. | SUSE Rancher open-source Kubernetes cluster management platform for provisioning, importing and governing clusters; Rancher Prime adds commercial support and distribution services. | [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://rancher.com | https://rancher.com | [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | *absent* | https://github.com/rancher/rancher | [Canonical Manager repository and identity][rancher-e1], [Manager source licence][rancher-e2], [Rancher OSS versus Prime commercial boundary][rancher-e4] | Add the verified Manager project repository. |
| `documentation_url` | *absent* | https://ranchermanager.docs.rancher.com/ | [Official Manager documentation][rancher-e3] | Add the directly identified official documentation entry point. |
| `categories` | kubernetes-distributions-operations | kubernetes-distributions-operations | [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Kubernetes Alternatives &amp; Platforms | Kubernetes cluster management | [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You need multi-cluster management with a unified UI, RBAC, and catalog across on-prem and cloud. | You need a self-hosted central management plane for Kubernetes clusters across distributions and environments, with optional Rancher Prime support. | [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3], [Manager source licence][rancher-e2], [Rancher OSS versus Prime commercial boundary][rancher-e4] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | You manage a single cluster or already use Cluster API/ArgoCD for fleet management. | You only need a Kubernetes distribution without a management plane, or expect Prime support, trusted registry access or separately licensed add-ons from the OSS licence alone. | [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3], [Manager source licence][rancher-e2], [Rancher OSS versus Prime commercial boundary][rancher-e4] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted | [Official Manager documentation][rancher-e3] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | open-core | oss | [Manager source licence][rancher-e2], [Rancher OSS versus Prime commercial boundary][rancher-e4] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Manager source licence][rancher-e2], [Rancher OSS versus Prime commercial boundary][rancher-e4] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Manager source licence][rancher-e2], [Rancher OSS versus Prime commercial boundary][rancher-e4] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [Stable release history][rancher-e5], [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3] | Reviewer judgement from maintained releases/service history and documented operations, explained above. |
| `status` | needs-review | active | [Stable release history][rancher-e5], [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical Manager repository and identity][rancher-e1] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical Manager repository and identity][rancher-e1], [Manager source licence][rancher-e2], [Official Manager documentation][rancher-e3], [Rancher OSS versus Prime commercial boundary][rancher-e4], [Stable release history][rancher-e5] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L166<br>legacy:devopstools_final.md#L668 | legacy:4_Kubernetes-Containers/README.md#L166<br>legacy:devopstools_final.md#L668<br>https://github.com/rancher/rancher<br>https://github.com/rancher/rancher/blob/main/LICENSE<br>https://ranchermanager.docs.rancher.com/<br>https://ranchermanager.docs.rancher.com/getting-started/quick-start-guides/deploy-rancher-manager/prime<br>https://github.com/rancher/rancher/releases | [Canonical Manager repository and identity][rancher-e1], [Manager source licence][rancher-e2], [Official Manager documentation][rancher-e3], [Rancher OSS versus Prime commercial boundary][rancher-e4], [Stable release history][rancher-e5] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Stable release history][rancher-e5], [Canonical Manager repository and identity][rancher-e1], [Official Manager documentation][rancher-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `name`, `summary`, `repository_url`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_model`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[rancher-e1]: https://github.com/rancher/rancher
[rancher-e2]: https://github.com/rancher/rancher/blob/main/LICENSE
[rancher-e3]: https://ranchermanager.docs.rancher.com/
[rancher-e4]: https://ranchermanager.docs.rancher.com/getting-started/quick-start-guides/deploy-rancher-manager/prime
[rancher-e5]: https://github.com/rancher/rancher/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/rancher/rancher) (`archived: false`).

### gitlab

**Identity boundary:** Retain GitLab as the parent SCM/CI/CD family. Free is a feature tier rather than a synonym for the historical/current CE package. CE/EE packages and SaaS/Self-Managed offerings are distinct axes.

**Licence boundary:** open-core remains correct. Canonical root LICENSE applies MIT to base software/client JavaScript, with EE/JH and other content/component exceptions. Actual ee/LICENSE restricts EE production use to a valid subscription and agreement while allowing development/testing under its terms. A repository MIT badge or CE mirror cannot represent the parent; leave license_spdx absent.

**Commercial/product boundary:** GitLab.com SaaS, Dedicated single-tenant SaaS and Self-Managed have distinct service/subscription terms; Free/Premium/Ultimate tiers and add-ons do not collapse to one licence or transferable entitlement. commercial_offering=true is explicit.

**Lifecycle boundary:** Current policy maintains 19.4 for bugs/security and 19.3/19.2 for security, with monthly minors and twice-monthly patches. Canonical project metadata reports last activity 2026-10-06. These current primary signals support active status without transferring a mirror archival flag.

**Repository boundary:** Replace gitlabhq/gitlabhq CE read-only mirror with gitlab.com/gitlab-org/gitlab, directly identified by the mirror README as development upstream. Preserve the former mirror as provenance. Public GitLab API response did not expose archived: leave optional repository_archived absent rather than copying GitHub mirror metadata.

**Maturity:** Established follows maintained platform releases, documented scalable packaging and current operational/upgrade policy.

**Unresolved questions / limits:** None blocking the mixed-licence parent boundary. The optional canonical archival boolean remains unasserted because public metadata omitted it. Feature-specific licences, tiers and service entitlements require their own terms.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Former CE mirror declares canonical upstream][gitlab-e1], [Canonical product-family repository][gitlab-e2], [Base and component licence boundaries][gitlab-e3], [Actual Enterprise source licence][gitlab-e4], [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [Commercial tiers and deployment offerings][gitlab-e7], [CE and EE installation documentation][gitlab-e8], [Release and maintenance policy][gitlab-e9], [Canonical repository activity metadata][gitlab-e10].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | gitlab | gitlab | [Former CE mirror declares canonical upstream][gitlab-e1], [Canonical product-family repository][gitlab-e2], [Canonical repository activity metadata][gitlab-e10], [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8] | Preserve stable catalogue identity and history. |
| `name` | GitLab | GitLab | [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Git repository management with CI/CD. | GitLab source-control and CI/CD product family, offered as GitLab.com SaaS and Self-Managed deployments, with MIT base code and separately licensed Enterprise features and subscriptions. | [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://about.gitlab.com | https://about.gitlab.com | [Former CE mirror declares canonical upstream][gitlab-e1], [Canonical product-family repository][gitlab-e2], [Canonical repository activity metadata][gitlab-e10], [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/gitlabhq/gitlabhq | https://gitlab.com/gitlab-org/gitlab | [Former CE mirror declares canonical upstream][gitlab-e1], [Canonical product-family repository][gitlab-e2], [Canonical repository activity metadata][gitlab-e10], [Base and component licence boundaries][gitlab-e3], [Actual Enterprise source licence][gitlab-e4] | Correct to the explicitly declared canonical development upstream; preserve the former CE mirror in sources. |
| `documentation_url` | *absent* | https://docs.gitlab.com/ | [Official documentation][gitlab-e6] | Add the directly identified official documentation entry point. |
| `categories` | source-control-repository-management | source-control-repository-management | [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Version Control &amp; Code Repository | Version Control &amp; Code Repository | [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>developer-experience-engineer<br>release-engineer | devops-engineer<br>developer-experience-engineer<br>release-engineer | [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | plan<br>develop | plan<br>develop<br>build<br>test<br>release<br>deploy<br>secure | [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You want an all-in-one DevOps platform (SCM + CI/CD + registry + planning). | You want integrated repositories, planning and CI/CD, and can select a deployment offering and Free, Premium or Ultimate feature tier under its applicable terms. | [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8], [Base and component licence boundaries][gitlab-e3], [Actual Enterprise source licence][gitlab-e4] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | Your team only needs simple repo hosting — the complexity overhead may not be justified. | You require one OSS licence for every parent-product feature, assume Free means CE packaging, or cannot operate and upgrade a Self-Managed instance within the maintenance policy. | [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8], [Base and component licence boundaries][gitlab-e3], [Actual Enterprise source licence][gitlab-e4] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | hosted-saas<br>self-hosted | [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | open-core | open-core | [Base and component licence boundaries][gitlab-e3], [Actual Enterprise source licence][gitlab-e4] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | *absent* | [Base and component licence boundaries][gitlab-e3], [Actual Enterprise source licence][gitlab-e4] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Base and component licence boundaries][gitlab-e3], [Actual Enterprise source licence][gitlab-e4], [Commercial tiers and deployment offerings][gitlab-e7] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [Release and maintenance policy][gitlab-e9], [Canonical repository activity metadata][gitlab-e10], [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8] | Reviewer judgement from maintained releases/service history and documented operations, explained above. |
| `status` | needs-review | active | [Release and maintenance policy][gitlab-e9], [Canonical repository activity metadata][gitlab-e10], [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | *absent* | [Former CE mirror declares canonical upstream][gitlab-e1], [Canonical product-family repository][gitlab-e2], [Canonical repository activity metadata][gitlab-e10], [Base and component licence boundaries][gitlab-e3], [Actual Enterprise source licence][gitlab-e4], [Commercial tiers and deployment offerings][gitlab-e7] | Leave absent: no verified public parent repository for HCP Terraform, or canonical GitLab metadata did not expose the flag. Do not inherit a component/mirror archival boolean. |
| `alternatives` | `[]` | `[]` | [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Former CE mirror declares canonical upstream][gitlab-e1], [Canonical product-family repository][gitlab-e2], [Base and component licence boundaries][gitlab-e3], [Actual Enterprise source licence][gitlab-e4], [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [Commercial tiers and deployment offerings][gitlab-e7], [CE and EE installation documentation][gitlab-e8], [Release and maintenance policy][gitlab-e9], [Canonical repository activity metadata][gitlab-e10] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:1_Foundational-Skills/README.md#L8<br>legacy:devopstools_final.md#L86 | legacy:1_Foundational-Skills/README.md#L8<br>legacy:devopstools_final.md#L86<br>https://github.com/gitlabhq/gitlabhq<br>https://gitlab.com/gitlab-org/gitlab<br>https://gitlab.com/gitlab-org/gitlab/-/raw/master/LICENSE<br>https://gitlab.com/gitlab-org/gitlab/-/raw/master/ee/LICENSE<br>https://docs.gitlab.com/development/licensing/<br>https://docs.gitlab.com/<br>https://docs.gitlab.com/subscriptions/choosing_subscription/<br>https://docs.gitlab.com/install/package/<br>https://docs.gitlab.com/policy/maintenance/<br>https://gitlab.com/api/v4/projects/gitlab-org%2Fgitlab | [Former CE mirror declares canonical upstream][gitlab-e1], [Canonical product-family repository][gitlab-e2], [Base and component licence boundaries][gitlab-e3], [Actual Enterprise source licence][gitlab-e4], [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [Commercial tiers and deployment offerings][gitlab-e7], [CE and EE installation documentation][gitlab-e8], [Release and maintenance policy][gitlab-e9], [Canonical repository activity metadata][gitlab-e10] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Release and maintenance policy][gitlab-e9], [Canonical repository activity metadata][gitlab-e10], [Official licensing documentation][gitlab-e5], [Official documentation][gitlab-e6], [CE and EE installation documentation][gitlab-e8] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `repository_url`, `documentation_url`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `commercial_offering`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`.

[gitlab-e1]: https://github.com/gitlabhq/gitlabhq
[gitlab-e2]: https://gitlab.com/gitlab-org/gitlab
[gitlab-e3]: https://gitlab.com/gitlab-org/gitlab/-/raw/master/LICENSE
[gitlab-e4]: https://gitlab.com/gitlab-org/gitlab/-/raw/master/ee/LICENSE
[gitlab-e5]: https://docs.gitlab.com/development/licensing/
[gitlab-e6]: https://docs.gitlab.com/
[gitlab-e7]: https://docs.gitlab.com/subscriptions/choosing_subscription/
[gitlab-e8]: https://docs.gitlab.com/install/package/
[gitlab-e9]: https://docs.gitlab.com/policy/maintenance/
[gitlab-e10]: https://gitlab.com/api/v4/projects/gitlab-org%2Fgitlab

### renovate

**Identity boundary:** Retain Renovate as the upstream dependency-update bot/CLI, currently branded Mend Renovate CLI upstream. Move functional placement from deployment/release orchestration to developer workflow and supply-chain maintenance.

**Licence boundary:** Actual lowercase license file is AGPLv3; package manifest and official documentation explicitly declare AGPL-3.0-only. Retain oss. Do not infer or-later from the generic licence appendix or transfer the software grant to the hosted service.

**Commercial/product boundary:** Mend-hosted Community and Enterprise services and commercial scheduling/support/platform capabilities are separately offered. commercial_offering=true records that relationship; local/self-hosted modes describe the OSS CLI, not service rights.

**Lifecycle boundary:** Non-archived upstream, 2026-10-07 activity and stable releases including 44.144.1 on 2026-10-07 support active status.

**Repository boundary:** Retain renovatebot/renovate. The package/container runs locally, in CI or on an operator-managed scheduler; hosted applications are distinct from this source repository.

**Maturity:** Established follows maintained releases and documented configuration, package managers, platforms and bot operations.

**Unresolved questions / limits:** None blocking OSS scope. Supported managers/platforms and Mend service entitlements must be checked separately; dependency updates do not constitute deployment or full vulnerability certification.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical CLI repository and product boundary][renovate-e1], [Software licence][renovate-e2], [Exact SPDX package manifest][renovate-e3], [Official documentation and self-hosted scope][renovate-e4], [Mend-hosted service and commercial boundary][renovate-e5], [Stable release history][renovate-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | renovate | renovate | [Canonical CLI repository and product boundary][renovate-e1], [Official documentation and self-hosted scope][renovate-e4] | Preserve stable catalogue identity and history. |
| `name` | Renovate | Renovate | [Official documentation and self-hosted scope][renovate-e4] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Automated dependency updates. | Renovate dependency-update automation that proposes repository changes as pull requests; its AGPL CLI is distinct from Mend-hosted services and commercial platform capabilities. | [Official documentation and self-hosted scope][renovate-e4] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://www.mend.io/renovate | https://www.mend.io/renovate | [Canonical CLI repository and product boundary][renovate-e1], [Official documentation and self-hosted scope][renovate-e4] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/renovatebot/renovate | https://github.com/renovatebot/renovate | [Canonical CLI repository and product boundary][renovate-e1], [Software licence][renovate-e2], [Exact SPDX package manifest][renovate-e3] | Keep the verified scoped project repository. |
| `documentation_url` | *absent* | https://docs.renovatebot.com/ | [Official documentation and self-hosted scope][renovate-e4] | Add the directly identified official documentation entry point. |
| `categories` | cd-gitops-release-promotion | developer-experience-local-environments<br>software-supply-chain-security | [Official documentation and self-hosted scope][renovate-e4] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Release Management | Dependency update automation | [Official documentation and self-hosted scope][renovate-e4] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>platform-engineer<br>release-engineer | devops-engineer<br>platform-engineer<br>release-engineer<br>developer-experience-engineer | [Official documentation and self-hosted scope][renovate-e4] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | release<br>deploy | develop<br>secure | [Official documentation and self-hosted scope][renovate-e4] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You manage many repos with diverse package ecosystems and want highly configurable auto-PRs. | You need configurable dependency-update pull requests across supported package managers and can run the OSS bot yourself or separately select a Mend-hosted service. | [Official documentation and self-hosted scope][renovate-e4], [Software licence][renovate-e2], [Exact SPDX package manifest][renovate-e3] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | Your project has very few dependencies and manual updates are trivial. | You need deployment orchestration or assume the OSS licence includes Mend-hosted scheduling, support and commercial platform capabilities. | [Official documentation and self-hosted scope][renovate-e4], [Software licence][renovate-e2], [Exact SPDX package manifest][renovate-e3] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | local<br>self-hosted | [Official documentation and self-hosted scope][renovate-e4] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][renovate-e2], [Exact SPDX package manifest][renovate-e3] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | AGPL-3.0-only | [Software licence][renovate-e2], [Exact SPDX package manifest][renovate-e3] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Software licence][renovate-e2], [Exact SPDX package manifest][renovate-e3], [Canonical CLI repository and product boundary][renovate-e1], [Mend-hosted service and commercial boundary][renovate-e5] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [Stable release history][renovate-e6], [Official documentation and self-hosted scope][renovate-e4] | Reviewer judgement from maintained releases/service history and documented operations, explained above. |
| `status` | needs-review | active | [Stable release history][renovate-e6], [Official documentation and self-hosted scope][renovate-e4] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical CLI repository and product boundary][renovate-e1] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Official documentation and self-hosted scope][renovate-e4] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Official documentation and self-hosted scope][renovate-e4] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical CLI repository and product boundary][renovate-e1], [Software licence][renovate-e2], [Exact SPDX package manifest][renovate-e3], [Official documentation and self-hosted scope][renovate-e4], [Mend-hosted service and commercial boundary][renovate-e5], [Stable release history][renovate-e6] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:10_Miscellaneous/README.md#L10<br>legacy:devopstools_final.md#L1269 | legacy:10_Miscellaneous/README.md#L10<br>legacy:devopstools_final.md#L1269<br>https://github.com/renovatebot/renovate<br>https://github.com/renovatebot/renovate/blob/main/license<br>https://github.com/renovatebot/renovate/blob/main/package.json<br>https://docs.renovatebot.com/<br>https://docs.renovatebot.com/mend-hosted/overview/<br>https://github.com/renovatebot/renovate/releases | [Canonical CLI repository and product boundary][renovate-e1], [Software licence][renovate-e2], [Exact SPDX package manifest][renovate-e3], [Official documentation and self-hosted scope][renovate-e4], [Mend-hosted service and commercial boundary][renovate-e5], [Stable release history][renovate-e6] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Stable release history][renovate-e6], [Official documentation and self-hosted scope][renovate-e4] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `categories`, `subcategories`, `roles`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[renovate-e1]: https://github.com/renovatebot/renovate
[renovate-e2]: https://github.com/renovatebot/renovate/blob/main/license
[renovate-e3]: https://github.com/renovatebot/renovate/blob/main/package.json
[renovate-e4]: https://docs.renovatebot.com/
[renovate-e5]: https://docs.renovatebot.com/mend-hosted/overview/
[renovate-e6]: https://github.com/renovatebot/renovate/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/renovatebot/renovate) (`archived: false`).

### bazel

**Identity boundary:** Bazel is a general build/test system, not a container image engine. Move its primary category to CI/build/testing, remove Kubernetes-specific role and add developer-experience/release roles.

**Licence boundary:** Apache-2.0 applies to Bazel source. Language rules, toolchains, dependencies and commercial remote services retain their own licences.

**Commercial/product boundary:** No blanket commercial_offering assertion for third-party build services. Bazel can use remote execution/caching backends without itself becoming a hosted CI service.

**Lifecycle boundary:** Non-archived upstream and current stable releases, including 9.3.0 on 2026-10-07, support active status. Official release model distinguishes rolling releases from supported LTS lines; the policy page still lists 9.2.0, so it is not treated as a synchronized latest-version feed.

**Repository boundary:** Retain bazelbuild/bazel. Use the directly read documentation home rather than /docs, which currently lands on a C++-specific page. Local describes the CLI, with external backends separately scoped.

**Maturity:** Established follows sustained multi-platform stable releases and explicit LTS/rolling support policy, not stars.

**Unresolved questions / limits:** None blocking core scope. Hermeticity depends on rules, toolchains and action inputs; remote service terms and language-rule licences are separate.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and build/test identity][bazel-e1], [Software licence][bazel-e2], [Official documentation home][bazel-e3], [Rolling and LTS release/support model][bazel-e4], [Stable release history][bazel-e5].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | bazel | bazel | [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3] | Preserve stable catalogue identity and history. |
| `name` | Bazel | Bazel | [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Fast, scalable, multi-language build system. | Extensible build and test system for multi-language, multi-platform software, with incremental execution and local or remote caching. | [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://bazel.build | https://bazel.build | [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/bazelbuild/bazel | https://github.com/bazelbuild/bazel | [Canonical repository and build/test identity][bazel-e1], [Software licence][bazel-e2] | Keep the verified scoped project repository. |
| `documentation_url` | *absent* | https://bazel.build/ | [Official documentation home][bazel-e3] | Add the directly identified official documentation entry point. |
| `categories` | containers-image-tooling | ci-build-testing | [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Build &amp; Image Tools | Build systems | [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>platform-engineer<br>kubernetes-engineer | devops-engineer<br>platform-engineer<br>developer-experience-engineer<br>release-engineer | [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | build<br>release | build<br>test | [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | * You have a large monorepo and need hermetic, incremental builds at scale. | You need scalable, repeatable incremental builds and tests and can maintain explicit build rules, toolchains and dependency inputs. | [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3], [Software licence][bazel-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | * You have a small project; Bazel&#x27;s complexity is not worth it for simple builds. | You cannot invest in build rules and toolchain migration, or need a container runtime, hosted CI service or automatic hermeticity for arbitrary build actions. | [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3], [Software licence][bazel-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | local | [Official documentation home][bazel-e3] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][bazel-e2] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Software licence][bazel-e2] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Software licence][bazel-e2] | Leave optional field absent; no blanket assertion about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Rolling and LTS release/support model][bazel-e4], [Stable release history][bazel-e5], [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3] | Reviewer judgement from maintained releases/service history and documented operations, explained above. |
| `status` | needs-review | active | [Rolling and LTS release/support model][bazel-e4], [Stable release history][bazel-e5], [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical repository and build/test identity][bazel-e1] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical repository and build/test identity][bazel-e1], [Software licence][bazel-e2], [Official documentation home][bazel-e3], [Rolling and LTS release/support model][bazel-e4], [Stable release history][bazel-e5] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:3_CI-CD-Automation/README.md#L72<br>legacy:devopstools_final.md#L347 | legacy:3_CI-CD-Automation/README.md#L72<br>legacy:devopstools_final.md#L347<br>https://github.com/bazelbuild/bazel<br>https://github.com/bazelbuild/bazel/blob/master/LICENSE<br>https://bazel.build/<br>https://bazel.build/release<br>https://github.com/bazelbuild/bazel/releases | [Canonical repository and build/test identity][bazel-e1], [Software licence][bazel-e2], [Official documentation home][bazel-e3], [Rolling and LTS release/support model][bazel-e4], [Stable release history][bazel-e5] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Rolling and LTS release/support model][bazel-e4], [Stable release history][bazel-e5], [Canonical repository and build/test identity][bazel-e1], [Official documentation home][bazel-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `categories`, `subcategories`, `roles`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[bazel-e1]: https://github.com/bazelbuild/bazel
[bazel-e2]: https://github.com/bazelbuild/bazel/blob/master/LICENSE
[bazel-e3]: https://bazel.build/
[bazel-e4]: https://bazel.build/release
[bazel-e5]: https://github.com/bazelbuild/bazel/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/bazelbuild/bazel) (`archived: false`).

### skaffold

**Identity boundary:** Skaffold is a client-side continuous-development workflow, covering build/test/push/deploy/debug rather than deployment alone. Kubernetes is a major target; current docs also cover local Docker and Cloud Run.

**Licence boundary:** Actual source licence is Apache-2.0. Supported builders/deployers and hosted backends retain separate licences and service terms.

**Commercial/product boundary:** Leave optional commercial_offering absent: no blanket assertion about every Google Cloud service using this OSS CLI. A remote build/deploy target does not change the client into SaaS.

**Lifecycle boundary:** Current repository archived=false, activity on 2026-10-05 and stable v2.25.0 on 2026-09-16 support active on the review date. Official docs AND repository documentation source announce gcloud removal after 2027-01-15 and repository archival on 2027-01-29. Preserve present active status while making planned retirement prominent; do not preemptively claim it is already archived.

**Repository boundary:** Retain GoogleContainerTools/skaffold; upstream explicitly states there is no cluster-side component. Local deployment refers to the CLI even when targets/builders are remote.

**Maturity:** Established follows maintained stable releases and documented client workflows; maturity does not promise continuing maintenance after the announced archive.

**Unresolved questions / limits:** None blocking current identity/licence/lifecycle. Archival is an announced future event; the actual archival flag and maintenance state will require review when it occurs. New long-lived adoption should account for that plan.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical client-side repository and scope][skaffold-e1], [Software licence][skaffold-e2], [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4], [Stable release history][skaffold-e5].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | skaffold | skaffold | [Canonical client-side repository and scope][skaffold-e1], [Upstream documentation source and planned archival announcement][skaffold-e4], [Official documentation and planned archival announcement][skaffold-e3] | Preserve stable catalogue identity and history. |
| `name` | Skaffold | Skaffold | [Canonical client-side repository and scope][skaffold-e1], [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Command-line workflow tool for fast, repeatable Kubernetes development across build, push, deploy, and debug loops. | Client-side container-development CLI for build, test, push, deploy and debug loops with Kubernetes and other supported targets; upstream plans repository archival on 29 January 2027. | [Canonical client-side repository and scope][skaffold-e1], [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://skaffold.dev | https://skaffold.dev | [Canonical client-side repository and scope][skaffold-e1], [Upstream documentation source and planned archival announcement][skaffold-e4], [Official documentation and planned archival announcement][skaffold-e3] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/GoogleContainerTools/skaffold | https://github.com/GoogleContainerTools/skaffold | [Canonical client-side repository and scope][skaffold-e1], [Upstream documentation source and planned archival announcement][skaffold-e4], [Software licence][skaffold-e2] | Keep the verified scoped project repository. |
| `documentation_url` | *absent* | https://skaffold.dev/docs/ | [Official documentation and planned archival announcement][skaffold-e3] | Add the directly identified official documentation entry point. |
| `categories` | containers-image-tooling | containers-image-tooling<br>developer-experience-local-environments | [Canonical client-side repository and scope][skaffold-e1], [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Build &amp; Image Tools | Container development workflows | [Canonical client-side repository and scope][skaffold-e1], [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>platform-engineer<br>kubernetes-engineer | devops-engineer<br>platform-engineer<br>kubernetes-engineer<br>developer-experience-engineer | [Canonical client-side repository and scope][skaffold-e1], [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | build<br>release | develop<br>build<br>test<br>deploy | [Canonical client-side repository and scope][skaffold-e1], [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | `[]` | You maintain a container-development workflow needing configurable build, test and deployment feedback and can plan for the announced repository archival on 29 January 2027. | [Canonical client-side repository and scope][skaffold-e1], [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4], [Software licence][skaffold-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | `[]` | You need upstream maintenance beyond the announced archive date, or rely on gcloud CLI bundling after 15 January 2027 rather than standalone installation. | [Canonical client-side repository and scope][skaffold-e1], [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4], [Software licence][skaffold-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | local | [Canonical client-side repository and scope][skaffold-e1], [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][skaffold-e2] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Software licence][skaffold-e2] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Software licence][skaffold-e2] | Leave optional field absent; no blanket assertion about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4], [Stable release history][skaffold-e5], [Canonical client-side repository and scope][skaffold-e1] | Reviewer judgement from maintained releases/service history and documented operations, explained above. |
| `status` | needs-review | active | [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4], [Stable release history][skaffold-e5], [Canonical client-side repository and scope][skaffold-e1] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical client-side repository and scope][skaffold-e1], [Upstream documentation source and planned archival announcement][skaffold-e4] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Canonical client-side repository and scope][skaffold-e1], [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Canonical client-side repository and scope][skaffold-e1], [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical client-side repository and scope][skaffold-e1], [Software licence][skaffold-e2], [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4], [Stable release history][skaffold-e5] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:devopstools_final.md#L362 | legacy:devopstools_final.md#L362<br>https://github.com/GoogleContainerTools/skaffold<br>https://github.com/GoogleContainerTools/skaffold/blob/main/LICENSE<br>https://skaffold.dev/docs/<br>https://github.com/GoogleContainerTools/skaffold/blob/main/docs-v2/content/en/docs/_index.md<br>https://github.com/GoogleContainerTools/skaffold/releases | [Canonical client-side repository and scope][skaffold-e1], [Software licence][skaffold-e2], [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4], [Stable release history][skaffold-e5] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Official documentation and planned archival announcement][skaffold-e3], [Upstream documentation source and planned archival announcement][skaffold-e4], [Stable release history][skaffold-e5], [Canonical client-side repository and scope][skaffold-e1] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `categories`, `subcategories`, `roles`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[skaffold-e1]: https://github.com/GoogleContainerTools/skaffold
[skaffold-e2]: https://github.com/GoogleContainerTools/skaffold/blob/main/LICENSE
[skaffold-e3]: https://skaffold.dev/docs/
[skaffold-e4]: https://github.com/GoogleContainerTools/skaffold/blob/main/docs-v2/content/en/docs/_index.md
[skaffold-e5]: https://github.com/GoogleContainerTools/skaffold/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/GoogleContainerTools/skaffold) (`archived: false`).

### rke2

**Identity boundary:** RKE2 is SUSE Rancher Kubernetes Engine 2, also historically RKE Government. Official docs distinguish it from RKE1 and K3s: K3s-derived operations/deployment, upstream alignment and containerd/static-pod control plane rather than RKE1 Docker mechanics.

**Licence boundary:** Actual Apache-2.0 source licence makes RKE2 OSS. Enterprise-ready security positioning and Prime support do not make the distribution proprietary. Bundled component licences remain separate.

**Commercial/product boundary:** commercial_offering=true reflects documented Prime support/lifecycle services for RKE2, not automatic Prime entitlement or a proprietary runtime licence.

**Lifecycle boundary:** Non-archived repository, 2026-10-07 activity and maintained stable Kubernetes patch-line releases, including v1.33.13+rke2r3 on 2026-10-02, support active status. This patch is not presented as the newest Kubernetes minor.

**Repository boundary:** Retain rancher/rke2 and docs.rke2.io; standalone self-hosted distribution and Rancher integration are explicitly supported.

**Maturity:** Established follows maintained Kubernetes-aligned releases, documented upgrades and operator security guidance.

**Unresolved questions / limits:** None blocking distribution scope. CIS requires host/runtime/operator configuration; FIPS coverage is component/configuration dependent (the docs distinguish Canal from alternative CNIs). No blanket certification or Prime support entitlement is claimed.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical distribution repository][rke2-e1], [Software licence][rke2-e2], [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5], [SUSE ownership and Prime commercial support boundary][rke2-e6], [Stable release history][rke2-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | rke2 | rke2 | [Canonical distribution repository][rke2-e1], [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5] | Preserve stable catalogue identity and history. |
| `name` | RKE2 | RKE2 | [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Rancher Kubernetes Engine 2 (hardened Kubernetes). | SUSE Rancher Kubernetes Engine 2, an Apache-licensed Kubernetes distribution focused on security and compliance, with documented CIS hardening and FIPS component boundaries. | [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://docs.rke2.io | https://docs.rke2.io | [Canonical distribution repository][rke2-e1], [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/rancher/rke2 | https://github.com/rancher/rke2 | [Canonical distribution repository][rke2-e1], [Software licence][rke2-e2] | Keep the verified scoped project repository. |
| `documentation_url` | *absent* | https://docs.rke2.io | [Official documentation, identity and RKE1/K3s relationship][rke2-e3] | Add the directly identified official documentation entry point. |
| `categories` | kubernetes-distributions-operations | kubernetes-distributions-operations | [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Kubernetes Core Concepts | Kubernetes distributions | [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate<br>secure | [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You need a FIPS-compliant, CIS-hardened Kubernetes distro for regulated environments. | You need a self-hosted Kubernetes distribution with security-focused defaults and can apply the version-appropriate CIS hardening guide and validate FIPS component choices for your environment. | [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5], [Software licence][rke2-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | A lightweight distro or managed service meets your compliance needs. | You require a managed Kubernetes control plane or assume installing RKE2 alone certifies compliance or grants Rancher Prime support entitlements. | [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5], [Software licence][rke2-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted | [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][rke2-e2] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Software licence][rke2-e2] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Software licence][rke2-e2], [SUSE ownership and Prime commercial support boundary][rke2-e6] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [SUSE ownership and Prime commercial support boundary][rke2-e6], [Stable release history][rke2-e7], [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5] | Reviewer judgement from maintained releases/service history and documented operations, explained above. |
| `status` | needs-review | active | [SUSE ownership and Prime commercial support boundary][rke2-e6], [Stable release history][rke2-e7], [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical distribution repository][rke2-e1] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical distribution repository][rke2-e1], [Software licence][rke2-e2], [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5], [SUSE ownership and Prime commercial support boundary][rke2-e6], [Stable release history][rke2-e7] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L15<br>legacy:devopstools_final.md#L444 | legacy:4_Kubernetes-Containers/README.md#L15<br>legacy:devopstools_final.md#L444<br>https://github.com/rancher/rke2<br>https://github.com/rancher/rke2/blob/master/LICENSE<br>https://docs.rke2.io<br>https://docs.rke2.io/security/hardening_guide<br>https://docs.rke2.io/security/fips_support<br>https://ranchermanager.docs.rancher.com/getting-started/quick-start-guides/deploy-rancher-manager/prime<br>https://github.com/rancher/rke2/releases | [Canonical distribution repository][rke2-e1], [Software licence][rke2-e2], [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5], [SUSE ownership and Prime commercial support boundary][rke2-e6], [Stable release history][rke2-e7] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [SUSE ownership and Prime commercial support boundary][rke2-e6], [Stable release history][rke2-e7], [Official documentation, identity and RKE1/K3s relationship][rke2-e3], [CIS hardening documentation and operator requirements][rke2-e4], [FIPS component boundary documentation][rke2-e5] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[rke2-e1]: https://github.com/rancher/rke2
[rke2-e2]: https://github.com/rancher/rke2/blob/master/LICENSE
[rke2-e3]: https://docs.rke2.io
[rke2-e4]: https://docs.rke2.io/security/hardening_guide
[rke2-e5]: https://docs.rke2.io/security/fips_support
[rke2-e6]: https://ranchermanager.docs.rancher.com/getting-started/quick-start-guides/deploy-rancher-manager/prime
[rke2-e7]: https://github.com/rancher/rke2/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/rancher/rke2) (`archived: false`).

### kube-bench

**Identity boundary:** Aqua Security kube-bench implements configuration checks against CIS Kubernetes and platform-specific profiles. Put security auditing first with Kubernetes operations as a secondary category; it does not provision a distribution.

**Licence boundary:** Apache-2.0 applies to kube-bench implementation. CIS develops the consensus benchmark; its content/distribution terms are distinct. Aqua is not the benchmark policy owner and the software licence does not license every benchmark document.

**Commercial/product boundary:** Leave optional commercial_offering absent: no parent-wide inference about Aqua commercial platform features or CIS assessment products from this implementation.

**Lifecycle boundary:** Non-archived upstream, 2026-10-05 activity and stable v0.16.0 on 2026-08-05 support active maintenance. Supported platform mappings independently bound the checks.

**Repository boundary:** Retain aquasecurity/kube-bench and use its verified first-party repository/documentation as official entry points. The previous GitHub Pages URL is preserved in provenance; its inaccessible response alone is not the reason or lifecycle evidence. Upstream README directly points to the repository docs.

**Maturity:** Established follows maintained stable releases, platform mappings and documented node/job execution requirements.

**Unresolved questions / limits:** None blocking implementation scope. Platform/Kubernetes/CIS versions are not one-to-one; inaccessible provider control planes and manual checks prevent blanket compliance claims. Supported managed worker checks remain valid.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical Aqua implementation repository and scope][kube-bench-e1], [Implementation software licence][kube-bench-e2], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5], [Stable release history][kube-bench-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | kube-bench | kube-bench | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5] | Preserve stable catalogue identity and history. |
| `name` | kube-bench | kube-bench | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | CIS Kubernetes benchmark tool. | Aqua Security tool that checks Kubernetes node configuration against selected CIS benchmark profiles; it implements checks and does not define the CIS standard or certify full compliance. | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://aquasecurity.github.io/kube-bench | https://github.com/aquasecurity/kube-bench | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/aquasecurity/kube-bench | https://github.com/aquasecurity/kube-bench | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [Implementation software licence][kube-bench-e2] | Keep the verified scoped project repository. |
| `documentation_url` | *absent* | https://github.com/aquasecurity/kube-bench/tree/main/docs | [Official upstream documentation][kube-bench-e3] | Add the directly identified official documentation entry point. |
| `categories` | kubernetes-distributions-operations | application-cloud-security<br>kubernetes-distributions-operations | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Kubernetes Management &amp; Operations | Kubernetes benchmark auditing | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer<br>devsecops-engineer<br>cloud-security-engineer | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | deploy<br>operate | test<br>operate<br>secure | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You need to audit cluster nodes against CIS benchmarks for compliance. | You need configuration checks on accessible Kubernetes nodes using a benchmark matched to the platform/version, including supported managed-cluster worker-node profiles. | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5], [Implementation software licence][kube-bench-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | Running managed Kubernetes where the provider handles control-plane hardening. | You require full CIS certification, audit access to an inaccessible provider-managed control plane, or a benchmark/profile not supported for your platform and Kubernetes version. | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5], [Implementation software licence][kube-bench-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | local | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Implementation software licence][kube-bench-e2] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Implementation software licence][kube-bench-e2] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Implementation software licence][kube-bench-e2] | Leave optional field absent; no blanket assertion about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Supported platform and benchmark documentation][kube-bench-e4], [Stable release history][kube-bench-e6], [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [CIS benchmark policy owner and scope][kube-bench-e5] | Reviewer judgement from maintained releases/service history and documented operations, explained above. |
| `status` | needs-review | active | [Supported platform and benchmark documentation][kube-bench-e4], [Stable release history][kube-bench-e6], [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [CIS benchmark policy owner and scope][kube-bench-e5] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Implementation software licence][kube-bench-e2], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5], [Stable release history][kube-bench-e6] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L36<br>legacy:devopstools_final.md#L483 | legacy:4_Kubernetes-Containers/README.md#L36<br>legacy:devopstools_final.md#L483<br>https://github.com/aquasecurity/kube-bench<br>https://github.com/aquasecurity/kube-bench/blob/main/LICENSE<br>https://github.com/aquasecurity/kube-bench/tree/main/docs<br>https://github.com/aquasecurity/kube-bench/blob/main/docs/platforms.md<br>https://www.cisecurity.org/benchmark/kubernetes<br>https://github.com/aquasecurity/kube-bench/releases<br>https://aquasecurity.github.io/kube-bench | [Canonical Aqua implementation repository and scope][kube-bench-e1], [Implementation software licence][kube-bench-e2], [Official upstream documentation][kube-bench-e3], [Supported platform and benchmark documentation][kube-bench-e4], [CIS benchmark policy owner and scope][kube-bench-e5], [Stable release history][kube-bench-e6] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Supported platform and benchmark documentation][kube-bench-e4], [Stable release history][kube-bench-e6], [Canonical Aqua implementation repository and scope][kube-bench-e1], [Official upstream documentation][kube-bench-e3], [CIS benchmark policy owner and scope][kube-bench-e5] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `official_url`, `documentation_url`, `categories`, `subcategories`, `roles`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[kube-bench-e1]: https://github.com/aquasecurity/kube-bench
[kube-bench-e2]: https://github.com/aquasecurity/kube-bench/blob/main/LICENSE
[kube-bench-e3]: https://github.com/aquasecurity/kube-bench/tree/main/docs
[kube-bench-e4]: https://github.com/aquasecurity/kube-bench/blob/main/docs/platforms.md
[kube-bench-e5]: https://www.cisecurity.org/benchmark/kubernetes
[kube-bench-e6]: https://github.com/aquasecurity/kube-bench/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/aquasecurity/kube-bench) (`archived: false`).

## Review-debt accounting

`python -m scripts.review_debt --format markdown --limit 30` was captured before and after. Selected: **10**; cleared: **10**; retained: **0**.

| Counter | Before | After |
|---|---:|---:|
| canonical_records | 1,425 | 1,425 |
| needs_review | 766 | 756 |
| status_needs_review | 766 | 756 |
| mismatches | 0 | 0 |
| unknown_license | 81 | 80 |
| unknown_maturity | 903 | 893 |
| missing_repository | 392 | 391 |
| missing_documentation | 900 | 890 |
| missing_sources | 0 | 0 |

The invariant `needs_review == status needs-review` holds for every canonical record. Missing repositories decrease by one through the verified Rancher Manager pointer; missing documentation decreases by ten. Unknown licence debt decreases by one through HCP Terraform commercial service terms. GitLab mixed parent licensing retains no single SPDX; HCP Terraform retains no software repository.

## Generated changes

Only generator output is listed here; the evidence report and focused regression test are authored files.

- `README.md`
- `docs/catalog-statistics.json`
- `docs/categories/application-cloud-security.md`
- `docs/categories/cd-gitops-release-promotion.md`
- `docs/categories/ci-build-testing.md`
- `docs/categories/containers-image-tooling.md`
- `docs/categories/developer-experience-local-environments.md`
- `docs/categories/infrastructure-as-code.md`
- `docs/categories/kubernetes-distributions-operations.md`
- `docs/categories/software-supply-chain-security.md`
- `docs/categories/source-control-repository-management.md`
- `docs/lifecycle/build.md`
- `docs/lifecycle/deploy.md`
- `docs/lifecycle/develop.md`
- `docs/lifecycle/operate.md`
- `docs/lifecycle/plan.md`
- `docs/lifecycle/release.md`
- `docs/lifecycle/secure.md`
- `docs/lifecycle/test.md`
- `docs/roles/cloud-engineer.md`
- `docs/roles/cloud-security-engineer.md`
- `docs/roles/developer-experience-engineer.md`
- `docs/roles/devops-engineer.md`
- `docs/roles/devsecops-engineer.md`
- `docs/roles/infrastructure-systems-engineer.md`
- `docs/roles/kubernetes-engineer.md`
- `docs/roles/platform-engineer.md`
- `docs/roles/release-engineer.md`
- `docs/roles/site-reliability-engineer.md`

## Validation and full link audit

Required checks passed. Python 3.12.3 in the existing WSL Ubuntu constrained environment ran installation, fresh dependency resolution and the complete suite. The Windows editable environment ran focused tests, lint/format, generation, catalogue validation and debt capture. `python` below denotes the selected interpreter.

| Command | Result |
|---|---|
| `python -m pip install -e '.[dev]' -c config/python-constraints-3.12.txt` | PASS; constrained editable install |
| `python -m scripts.python_constraints --check` | PASS; fresh resolver matches unchanged reviewed constraints |
| `python -m ruff check scripts tests` | PASS |
| `python -m ruff format --check scripts tests` | PASS; 60 files already formatted |
| `python -m pytest tests/test_wave7_evidence_review.py` | PASS; 19 tests |
| `python -m pytest` | PASS; 723 tests in 277.23 seconds |
| `python -m scripts.generate_docs` | PASS; regenerated after canonical changes |
| `python -m scripts.generate_docs --check` | PASS |
| `python -m scripts.validate_catalog` | PASS |
| `python -m scripts.review_debt --format markdown --limit 30` | PASS; before/after counters captured |
| `git diff --check` | PASS |

Focused Windows and full Linux pytest emitted a non-failing cache permission warning. WSL Git-dependent tests used process-only `GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=true` to interpret the Windows checkout line endings consistently. No repository/global Git setting, constraint, test assertion or workflow was weakened.

Focused coverage guards the HCP stable ID/rename, service-versus-CLI licence and private-agent control-plane boundary; current Terraform/Nomad BUSL versus historical MPL; CE versus Enterprise support; Rancher OSS versus Prime; GitLab canonical upstream and mixed parent licences/tiers; Renovate AGPL-only versus Mend hosting; Bazel build/test scope; Skaffold broader loop and announced future archival; RKE2 conditional CIS/FIPS scope; and kube-bench implementation versus CIS policy and managed worker checks. No prices, temporary release versions or marketing claims are asserted.

One full fresh strict audit used no cache reuse and ignored output paths:

```bash
python -m scripts.check_links --strict --check-archived --workers 8 --cache tmp/wave7/link-cache.json --cache-hours 0 --json-report tmp/wave7/link-report.json --markdown-report tmp/wave7/link-report.md
```

| Audit counter | Result |
|---|---:|
| URLs | 2,644 |
| blocking_new | 0 |
| blocking_known observed | 4 |
| strict_result | PASS |

**Reviewed baseline changed: NO.** The six existing exceptions remain untouched. Observed nonblocking rate limits/access restrictions or inconclusive responses do not independently prove a historical defect fixed.

| Existing baseline URL | Observed response | Classification / strict status |
|---|---|---|
| `https://github.com/hoji-ai/hoji` | HTTP 429 | rate-limited / nonblocking |
| `https://github.com/ophircloud/DevOps-Projects` | HTTP 429 | rate-limited / nonblocking |
| `https://hub.docker.com/r/soosio/dast` | HTTP 404 | manual-verification-required / blocking-known |
| `https://kubeflame.github.io` | HTTP 404 | manual-verification-required / blocking-known |
| `https://www.opentext.com/products/static-application-security-testing` | HTTP 444 | http-error / blocking-known |
| `https://www.yotascale.com` | HTTP 404 | manual-verification-required / blocking-known |

All ten final documentation entry points were included:

| ID | Documentation response | Classification |
|---|---|---|
| `terraform-cloud` | HTTP 200 | valid |
| `terraform` | HTTP 200 | valid |
| `nomad` | HTTP 200 | valid |
| `rancher` | HTTP 200 | valid |
| `gitlab` | HTTP 200 | valid |
| `renovate` | HTTP 200 | valid |
| `bazel` | HTTP 200 | valid |
| `skaffold` | HTTP 200 | valid |
| `rke2` | HTTP 200 | valid |
| `kube-bench` | HTTP 429 | rate-limited |

All audit classifications, including network-dependent limitations:

| Classification | Count |
|---|---:|
| dns-inconclusive | 5 |
| http-error | 1 |
| manual-verification-required | 3 |
| network-inconclusive | 1 |
| permanent-redirect | 207 |
| rate-limited | 756 |
| restricted-or-bot-blocked | 357 |
| timeout-inconclusive | 1 |
| transient-failure | 1 |
| valid | 1,277 |
| valid-redirect | 35 |

Strict PASS means no newly classified blockers, not successful verification of every endpoint. Actual licence files, official terms/docs, upstream metadata and release/support evidence independently support review decisions. Source-only URLs were read separately; the checker inventories official/repository/documentation fields. No network-dependent required audit was omitted. Access/rate-limit/transport observations remain inconclusive where listed above.

Raw cache/audit output stays in ignored `tmp/wave7/`. Nothing under `reports/` is committed. No additional full audit was run.

## Scope verification and review state

The pre-edit snapshot and baseline Git tree establish exactly ten changed IDs, dates and record blocks and 240 complete material-field rows. All legacy provenance is preserved. Other record blocks remain unchanged. Final canonical URL contexts match the audit. Six-entry baseline, committed audit output/ledger, workflows, CodeQL configuration and Python constraints remain unchanged.

Issue #2 is read-only: its body and updated_at (2026-10-07T18:26:31Z) are compared with the pre-edit snapshot again at handoff. No Wave 4/Wave 5/Wave 6 record is revisited; Wave 8 is not started. No merge or release is performed.

Material evidence corrections resolved within the exact cohort: HCP Terraform rename and commercial SaaS identity without a CLI repository/SPDX; Terraform CE current BUSL versus historical MPL/providers and HCP/Enterprise; Nomad CE BUSL and IBM-aligned base lifecycle versus Enterprise entitlements; Rancher Manager Apache OSS versus Prime; GitLab mixed parent licences, Free tier versus CE/EE packaging and declared GitLab.com upstream; Renovate AGPL-3.0-only versus Mend services and dependency-update scope; Bazel build/test placement and rolling/LTS policy; Skaffold broader client workflow with present activity and planned 2027 archival; RKE2 Apache OSS with conditional operator/component CIS/FIPS boundaries; kube-bench Apache implementation versus CIS standards and supported managed worker checks.

No material identity/licence boundary remains unresolved. GitLab optional repository_archived is deliberately unasserted because the public canonical metadata omitted it; current release/maintenance evidence supports active status. HCP has no invented parent-source repository. Skaffold future archival is an announced plan rather than an already-observed archived state. Product/service/component entitlements remain explicitly bounded per record.

CI/security and any subsequent automatic PR findings are reported against the final commit in the PR and final handoff.
