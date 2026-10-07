# Evidence review Wave 6 — 2026-10-07

Exactly ten existing canonical records were reviewed. All ten receive **CLEAR REVIEW**. Stable IDs and every previous provenance source are preserved. Canonical YAML is authoritative; generated pages were regenerated.

## Verified baseline and scope

- Main: `71c199e6fbb78a9a0581bbb320d3dcb13952da5f` (post-Wave-5).
- Branch: `maintenance/wave-6-evidence-review`.
- Before editing: clean working tree, zero open PRs, zero open CodeQL alerts; all five exact-main check runs passed (CodeQL actions/python, Plumber, gitleaks, catalogue validate).
- Issue #2 was read: Wave 5 is COMPLETED; Wave 6 is NOT STARTED and READY TO SCOPE. It is not edited.
- Exactly these ten IDs differ from the pre-edit snapshot of all 1,425 records. Other record blocks remain byte-for-byte unchanged. All primary category files are preserved; KubeVirt adds a secondary virtualization category.
- No baseline, committed audit report, link ledger, issue, workflow, CodeQL configuration, dependency constraint or unrelated record changes; no Wave 4/Wave 5 revisits or Wave 7 work.

This fixed cohort balances core IaC, container builds, Kubernetes platforms, observability, workflow licensing and IAM with direct primary-source availability. All ten initially had review flag/status debt, unknown maturity and missing documentation. The rank below is the user-specified order.

| Rank | ID | Initial name | Initial category | Initial debt |
|---:|---|---|---|---|
| 1 | `opentofu` | OpenTofu | `infrastructure-as-code` | needs-review; unknown maturity; missing docs |
| 2 | `packer` | Packer | `infrastructure-as-code` | needs-review; unknown maturity; missing docs |
| 3 | `buildkit` | BuildKit | `containers-image-tooling` | needs-review; unknown maturity; missing docs |
| 4 | `buildah` | Buildah | `containers-image-tooling` | needs-review; unknown maturity; missing docs |
| 5 | `kubevirt` | KubeVirt | `kubernetes-distributions-operations` | needs-review; unknown maturity; missing docs |
| 6 | `vcluster` | vcluster | `kubernetes-distributions-operations` | needs-review; unknown maturity; missing docs |
| 7 | `cadvisor` | cAdvisor | `monitoring-metrics-logs-tracing` | needs-review; unknown maturity; missing docs; missing official URL |
| 8 | `uptime-kuma` | Uptime Kuma | `monitoring-metrics-logs-tracing` | needs-review; unknown maturity; missing docs |
| 9 | `camunda` | Camunda | `workflow-automation-chatops` | needs-review; unknown maturity; missing docs; missing parent repository |
| 10 | `passbolt` | passbolt | `iam-secrets-certificates` | needs-review; unknown maturity; missing docs; missing parent repository |

## Evidence method and interpretation

Search results were discovery aids; official documents, upstream source/licence files, release feeds and legal terms were read directly. GitHub repository metadata (`archived`, default branch and update dates) and release JSON were checked through its API. Link-audit responses alone do not establish lifecycle. The review date records this review action, not a vendor statement.

Maturity is a reviewer judgement from maintenance history, stable interfaces, documented operations and governance, not GitHub stars. Categories, roles and lifecycle stages map documented capabilities to the existing taxonomy. Use/avoid guidance describes selection tradeoffs, not newly invented vendor restrictions. Empty alternatives/tags and absent optional offering booleans are deliberately retained without unsupported comparative or parent-wide claims. Camunda and Passbolt receive directly verified core/server repository pointers with their component boundaries stated explicitly.

## Decisions and complete material-field review

### opentofu

**Identity boundary:** Independent community-governed IaC project established as OpenTofu, a Series of LF Projects, LLC; TSC oversight is directly documented. Its Terraform ancestry is historical context, not its complete identity.

**Licence boundary:** MPL-2.0 applies to OpenTofu source. Providers, commercial orchestration products and Terraform-specific offerings retain their own boundaries.

**Lifecycle boundary:** Non-archived repository, October 2026 maintenance and stable v1.13.1/v1.12.7 releases on 2026-10-01 support active status.

**Repository boundary:** Retain opentofu/opentofu. Local and CI execution is the CLI deployment model; foundation governance does not imply a hosted control plane.

**Maturity:** Established is an editorial judgement based on maintained stable release lines, documented state/provider migration and sustained foundation governance, not stars.

**Unresolved questions / limits:** None blocking. Compatibility is an aim requiring configuration/provider/state checks, not an unconditional promise for every Terraform feature or version.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and identity][opentofu-e1], [Software licence][opentofu-e2], [Official documentation and scope][opentofu-e3], [Terraform migration boundary][opentofu-e4], [Foundation technical charter][opentofu-e5], [Community governance][opentofu-e6], [Stable release history][opentofu-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | opentofu | opentofu | [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3] | Preserve stable catalogue identity and history. |
| `name` | OpenTofu | OpenTofu | [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Open-source Terraform fork. | Community-governed infrastructure-as-code CLI for declaratively provisioning and managing cloud and on-premises resources. | [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://opentofu.org | https://opentofu.org | [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/opentofu/opentofu | https://github.com/opentofu/opentofu | [Canonical repository and identity][opentofu-e1], [Software licence][opentofu-e2] | Keep the verified project pointer/official alias with its explicit boundary. |
| `documentation_url` | *absent* | https://opentofu.org/docs/ | [Official documentation and scope][opentofu-e3] | Add the directly identified official documentation entry point. |
| `categories` | infrastructure-as-code | infrastructure-as-code | [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Infrastructure as Code (IaC) | Infrastructure as Code (IaC) | [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | plan<br>build<br>deploy | plan<br>deploy<br>operate | [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You want Terraform-compatible IaC under a truly open-source license. | You need community-governed, MPL-licensed infrastructure as code and can validate existing Terraform configurations, providers and state using the documented migration process. | [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3], [Software licence][opentofu-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | You rely on HashiCorp enterprise support or features exclusive to Terraform. | You require Terraform-specific commercial features or support, or cannot test configuration and state compatibility before migration. | [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3], [Software licence][opentofu-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | local | [Official documentation and scope][opentofu-e3] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][opentofu-e2] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | MPL-2.0 | [Software licence][opentofu-e2] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Software licence][opentofu-e2] | Leave optional field absent; no blanket assertion about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Foundation technical charter][opentofu-e5], [Stable release history][opentofu-e7], [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Foundation technical charter][opentofu-e5], [Stable release history][opentofu-e7], [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical repository and identity][opentofu-e1] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical repository and identity][opentofu-e1], [Software licence][opentofu-e2], [Official documentation and scope][opentofu-e3], [Terraform migration boundary][opentofu-e4], [Foundation technical charter][opentofu-e5], [Community governance][opentofu-e6], [Stable release history][opentofu-e7] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:2_Cloud-Infrastructure-Serverless/README.md#L52<br>legacy:devopstools_final.md#L179 | legacy:2_Cloud-Infrastructure-Serverless/README.md#L52<br>legacy:devopstools_final.md#L179<br>https://github.com/opentofu/opentofu<br>https://github.com/opentofu/opentofu/blob/main/LICENSE<br>https://opentofu.org/docs/<br>https://opentofu.org/docs/intro/migration/<br>https://github.com/opentofu/org/blob/main/CHARTER.md<br>https://github.com/opentofu/org/blob/main/GOVERNANCE.md<br>https://github.com/opentofu/opentofu/releases | [Canonical repository and identity][opentofu-e1], [Software licence][opentofu-e2], [Official documentation and scope][opentofu-e3], [Terraform migration boundary][opentofu-e4], [Foundation technical charter][opentofu-e5], [Community governance][opentofu-e6], [Stable release history][opentofu-e7] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Foundation technical charter][opentofu-e5], [Stable release history][opentofu-e7], [Canonical repository and identity][opentofu-e1], [Official documentation and scope][opentofu-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[opentofu-e1]: https://github.com/opentofu/opentofu
[opentofu-e2]: https://github.com/opentofu/opentofu/blob/main/LICENSE
[opentofu-e3]: https://opentofu.org/docs/
[opentofu-e4]: https://opentofu.org/docs/intro/migration/
[opentofu-e5]: https://github.com/opentofu/org/blob/main/CHARTER.md
[opentofu-e6]: https://github.com/opentofu/org/blob/main/GOVERNANCE.md
[opentofu-e7]: https://github.com/opentofu/opentofu/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/opentofu/opentofu) (`archived: false`).

### packer

**Identity boundary:** HashiCorp Packer CLI builds machine images. HCP Packer tracks image metadata; it is a separate service and does not make the CLI itself SaaS.

**Licence boundary:** Retain source-available. Current LICENSE covers Packer 1.10.0 or later under Business Source License 1.1, now naming IBM as licensor. Reviewed v1.9.4 used MPL-2.0 and v1.10.0 used BUSL. Each licensed version changes to MPL-2.0 after its specified four-year interval; this does not make current source MPL today. BUSL-1.1 is the applicable SPDX identifier. Plugins retain independent licences.

**Lifecycle boundary:** Current documentation and stable v1.16.1 released 2026-09-18 support active status; unmaintained plugin notices do not deprecate Packer.

**Repository boundary:** Retain hashicorp/packer. Image build/release is distinguished from managing deployed infrastructure; local/CI CLI execution remains separate from HCP.

**Maturity:** Established follows sustained multi-platform releases, image template/plugin documentation and maintained migration/install operations.

**Unresolved questions / limits:** None blocking. Competitive-use and per-version conversion conditions remain in the actual licence; no universal plugin licence or legal permission for a proposed business is asserted.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and identity][packer-e1], [Current software licence and version boundary][packer-e2], [Historical MPL licence][packer-e3], [First 1.10 licence][packer-e4], [Official documentation and image scope][packer-e5], [Plugin installation boundary][packer-e6], [Separate HCP offering][packer-e7], [Stable release history][packer-e8], [SPDX licence identifier][packer-e9].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | packer | packer | [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5] | Preserve stable catalogue identity and history. |
| `name` | Packer | Packer | [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Machine image creation. | HashiCorp machine-image build CLI that creates reproducible images for multiple platforms from one configuration, with separately licensed plugins and HCP image metadata services. | [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://www.packer.io | https://www.packer.io | [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/hashicorp/packer | https://github.com/hashicorp/packer | [Canonical repository and identity][packer-e1], [Current software licence and version boundary][packer-e2], [Historical MPL licence][packer-e3], [First 1.10 licence][packer-e4], [SPDX licence identifier][packer-e9] | Keep the verified project pointer/official alias with its explicit boundary. |
| `documentation_url` | *absent* | https://developer.hashicorp.com/packer/docs | [Official documentation and image scope][packer-e5] | Add the directly identified official documentation entry point. |
| `categories` | infrastructure-as-code | infrastructure-as-code | [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Infrastructure as Code (IaC) | Infrastructure as Code (IaC) | [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | plan<br>build<br>deploy | plan<br>build<br>release | [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You need reproducible, versioned machine images (AMIs, VM images). | You need repeatable machine-image builds across cloud or virtualization platforms and can comply with the current Business Source License and each plugin licence. | [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5], [Plugin installation boundary][packer-e6], [Current software licence and version boundary][packer-e2], [Historical MPL licence][packer-e3], [First 1.10 licence][packer-e4], [SPDX licence identifier][packer-e9] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | You use immutable containers and don&#x27;t need VM-level images. | You require an OSI-approved licence for current Packer source, or plan a competitive hosted or embedded offering outside the Additional Use Grant. | [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5], [Plugin installation boundary][packer-e6], [Current software licence and version boundary][packer-e2], [Historical MPL licence][packer-e3], [First 1.10 licence][packer-e4], [SPDX licence identifier][packer-e9] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | local | [Official documentation and image scope][packer-e5], [Plugin installation boundary][packer-e6] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | source-available | source-available | [Current software licence and version boundary][packer-e2], [Historical MPL licence][packer-e3], [First 1.10 licence][packer-e4], [SPDX licence identifier][packer-e9] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | BUSL-1.1 | [Current software licence and version boundary][packer-e2], [Historical MPL licence][packer-e3], [First 1.10 licence][packer-e4], [SPDX licence identifier][packer-e9] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Current software licence and version boundary][packer-e2], [Historical MPL licence][packer-e3], [First 1.10 licence][packer-e4], [SPDX licence identifier][packer-e9], [Separate HCP offering][packer-e7] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [Stable release history][packer-e8], [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Stable release history][packer-e8], [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical repository and identity][packer-e1] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical repository and identity][packer-e1], [Current software licence and version boundary][packer-e2], [Historical MPL licence][packer-e3], [First 1.10 licence][packer-e4], [Official documentation and image scope][packer-e5], [Plugin installation boundary][packer-e6], [Separate HCP offering][packer-e7], [Stable release history][packer-e8], [SPDX licence identifier][packer-e9] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:2_Cloud-Infrastructure-Serverless/README.md#L54<br>legacy:devopstools_final.md#L180 | legacy:2_Cloud-Infrastructure-Serverless/README.md#L54<br>legacy:devopstools_final.md#L180<br>https://github.com/hashicorp/packer<br>https://github.com/hashicorp/packer/blob/main/LICENSE<br>https://github.com/hashicorp/packer/blob/v1.9.4/LICENSE<br>https://github.com/hashicorp/packer/blob/v1.10.0/LICENSE<br>https://developer.hashicorp.com/packer/docs<br>https://developer.hashicorp.com/packer/docs/plugins/install<br>https://developer.hashicorp.com/packer/docs/hcp<br>https://github.com/hashicorp/packer/releases<br>https://spdx.org/licenses/BUSL-1.1.html | [Canonical repository and identity][packer-e1], [Current software licence and version boundary][packer-e2], [Historical MPL licence][packer-e3], [First 1.10 licence][packer-e4], [Official documentation and image scope][packer-e5], [Plugin installation boundary][packer-e6], [Separate HCP offering][packer-e7], [Stable release history][packer-e8], [SPDX licence identifier][packer-e9] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Stable release history][packer-e8], [Canonical repository and identity][packer-e1], [Official documentation and image scope][packer-e5] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[packer-e1]: https://github.com/hashicorp/packer
[packer-e2]: https://github.com/hashicorp/packer/blob/main/LICENSE
[packer-e3]: https://github.com/hashicorp/packer/blob/v1.9.4/LICENSE
[packer-e4]: https://github.com/hashicorp/packer/blob/v1.10.0/LICENSE
[packer-e5]: https://developer.hashicorp.com/packer/docs
[packer-e6]: https://developer.hashicorp.com/packer/docs/plugins/install
[packer-e7]: https://developer.hashicorp.com/packer/docs/hcp
[packer-e8]: https://github.com/hashicorp/packer/releases
[packer-e9]: https://spdx.org/licenses/BUSL-1.1.html

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/hashicorp/packer) (`archived: false`).

### buildkit

**Identity boundary:** BuildKit is the Moby builder toolkit/backend; Docker Buildx is a client and user interface. Standalone BuildKit comprises buildkitd and buildctl and supports other clients.

**Licence boundary:** Apache-2.0 applies to the upstream toolkit; this is not a licence claim about Docker Desktop subscriptions, external frontends or hosted build services.

**Lifecycle boundary:** Non-archived upstream, current commits and stable v0.33.1 released 2026-09-30 support active lifecycle; release candidates are distinguished from stable releases.

**Repository boundary:** Retain moby/buildkit. The backend can be operated on hosts or in containers/Kubernetes; a client CLI does not make the complete execution service a local-only tool.

**Maturity:** Established reflects sustained stable maintenance, Docker integration and documented standalone/caching/worker operations, not its 0.x numbering alone.

**Unresolved questions / limits:** None blocking. Windows-container support has documented experimental limits; no blanket platform support or hosted-service offering is asserted.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and execution architecture][buildkit-e1], [Software licence][buildkit-e2], [Official documentation and scope][buildkit-e3], [Buildx client versus BuildKit backend][buildkit-e4], [Stable release history][buildkit-e5].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | buildkit | buildkit | [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3] | Preserve stable catalogue identity and history. |
| `name` | BuildKit | BuildKit | [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Next-generation Docker image build engine used by Buildx. | Moby build-execution toolkit and backend for concurrent, cache-efficient builds, used by Docker Buildx and other clients. | [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://docs.docker.com/build/buildkit | https://docs.docker.com/build/buildkit | [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/moby/buildkit | https://github.com/moby/buildkit | [Canonical repository and execution architecture][buildkit-e1], [Software licence][buildkit-e2] | Keep the verified project pointer/official alias with its explicit boundary. |
| `documentation_url` | *absent* | https://docs.docker.com/build/buildkit/ | [Official documentation and scope][buildkit-e3] | Add the directly identified official documentation entry point. |
| `categories` | containers-image-tooling | containers-image-tooling | [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Build &amp; Image Tools | Build &amp; Image Tools | [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>platform-engineer<br>kubernetes-engineer | devops-engineer<br>platform-engineer<br>kubernetes-engineer | [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | build<br>release | build<br>release | [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | * You want faster Docker builds with better caching, parallelism, and build secrets. | You need low-level build execution, reusable caches and extensible frontends, accessed through buildctl, Docker Buildx or another BuildKit client. | [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3], [Software licence][buildkit-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | * You&#x27;re already using it (it&#x27;s the default in modern Docker); switching only matters on older Docker versions. | You only need a higher-level build interface and do not want to operate a standalone buildkitd backend; Docker integrations can manage it for you. | [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3], [Software licence][buildkit-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted | [Official documentation and scope][buildkit-e3] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][buildkit-e2] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Software licence][buildkit-e2] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Software licence][buildkit-e2] | Leave optional field absent; no blanket assertion about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Stable release history][buildkit-e5], [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Stable release history][buildkit-e5], [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical repository and execution architecture][buildkit-e1] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical repository and execution architecture][buildkit-e1], [Software licence][buildkit-e2], [Official documentation and scope][buildkit-e3], [Buildx client versus BuildKit backend][buildkit-e4], [Stable release history][buildkit-e5] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:3_CI-CD-Automation/README.md#L76<br>legacy:devopstools_final.md#L349 | legacy:3_CI-CD-Automation/README.md#L76<br>legacy:devopstools_final.md#L349<br>https://github.com/moby/buildkit<br>https://github.com/moby/buildkit/blob/master/LICENSE<br>https://docs.docker.com/build/buildkit/<br>https://docs.docker.com/build/concepts/overview/<br>https://github.com/moby/buildkit/releases | [Canonical repository and execution architecture][buildkit-e1], [Software licence][buildkit-e2], [Official documentation and scope][buildkit-e3], [Buildx client versus BuildKit backend][buildkit-e4], [Stable release history][buildkit-e5] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Stable release history][buildkit-e5], [Canonical repository and execution architecture][buildkit-e1], [Official documentation and scope][buildkit-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[buildkit-e1]: https://github.com/moby/buildkit
[buildkit-e2]: https://github.com/moby/buildkit/blob/master/LICENSE
[buildkit-e3]: https://docs.docker.com/build/buildkit/
[buildkit-e4]: https://docs.docker.com/build/concepts/overview/
[buildkit-e5]: https://github.com/moby/buildkit/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/moby/buildkit) (`archived: false`).

### buildah

**Identity boundary:** Buildah builds OCI images through CLI/library APIs without a daemon. Podman runs/manages containers and can use Buildah libraries; the products and their container concepts are distinct.

**Licence boundary:** Apache-2.0 applies to upstream Buildah. Images produced, base images and unrelated container products retain their own licences.

**Lifecycle boundary:** Non-archived project with October 2026 commits and stable v1.45.1 released 2026-09-15; official site also documents maintained release history.

**Repository boundary:** Preserve existing containers/buildah repository_url: the official site and upstream README still link it. GitHub resolves this same repository ID 80134675 to podman-container-tools/buildah, where current docs/licence/releases were checked. No duplicate record or redirect-only bulk replacement.

**Maturity:** Established reflects maintained releases since 2018, documented CLI/API operations and longstanding integration with Podman.

**Unresolved questions / limits:** None blocking. Rootless operation depends on host kernel/storage/user-namespace configuration; no universal privilege-free guarantee is asserted.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Official project site and upstream links][buildah-e1], [Canonical upstream and Podman boundary][buildah-e2], [Software licence][buildah-e3], [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5], [Stable release history][buildah-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | buildah | buildah | [Official project site and upstream links][buildah-e1], [Canonical upstream and Podman boundary][buildah-e2], [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5] | Preserve stable catalogue identity and history. |
| `name` | Buildah | Buildah | [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Build OCI images without a daemon. | Daemonless OCI image-building CLI and library, with Dockerfile and scripted workflows; complementary to the Podman container runtime. | [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://buildah.io | https://buildah.io | [Official project site and upstream links][buildah-e1], [Canonical upstream and Podman boundary][buildah-e2], [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/containers/buildah | https://github.com/containers/buildah | [Official project site and upstream links][buildah-e1], [Canonical upstream and Podman boundary][buildah-e2], [Software licence][buildah-e3] | Keep the verified project pointer/official alias with its explicit boundary. |
| `documentation_url` | *absent* | https://github.com/podman-container-tools/buildah/tree/main/docs | [Official documentation][buildah-e4] | Add the directly identified official documentation entry point. |
| `categories` | containers-image-tooling | containers-image-tooling | [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Build &amp; Image Tools | Build &amp; Image Tools | [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>platform-engineer<br>kubernetes-engineer | devops-engineer<br>platform-engineer<br>kubernetes-engineer | [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | build<br>release | build<br>release | [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | * You need daemonless, rootless container image builds (especially in CI or restricted environments). | You need daemonless OCI image builds from Dockerfiles or scripted working-container operations, including rootless Linux workflows where supported. | [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5], [Software licence][buildah-e3] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | * You&#x27;re happy with standard Docker builds and don&#x27;t have security constraints on the daemon. | You need a long-running container runtime rather than an image builder; Podman is complementary and can use Buildah libraries independently. | [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5], [Software licence][buildah-e3] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | local | [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][buildah-e3] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Software licence][buildah-e3] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Software licence][buildah-e3] | Leave optional field absent; no blanket assertion about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Stable release history][buildah-e6], [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Stable release history][buildah-e6], [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Official project site and upstream links][buildah-e1], [Canonical upstream and Podman boundary][buildah-e2] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Official project site and upstream links][buildah-e1], [Canonical upstream and Podman boundary][buildah-e2], [Software licence][buildah-e3], [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5], [Stable release history][buildah-e6] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:3_CI-CD-Automation/README.md#L74<br>legacy:devopstools_final.md#L348 | legacy:3_CI-CD-Automation/README.md#L74<br>legacy:devopstools_final.md#L348<br>https://buildah.io/<br>https://github.com/podman-container-tools/buildah<br>https://github.com/podman-container-tools/buildah/blob/main/LICENSE<br>https://github.com/podman-container-tools/buildah/tree/main/docs<br>https://github.com/podman-container-tools/buildah/blob/main/docs/buildah.1.md<br>https://github.com/podman-container-tools/buildah/releases | [Official project site and upstream links][buildah-e1], [Canonical upstream and Podman boundary][buildah-e2], [Software licence][buildah-e3], [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5], [Stable release history][buildah-e6] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Stable release history][buildah-e6], [Official documentation][buildah-e4], [CLI scope and operations][buildah-e5] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[buildah-e1]: https://buildah.io/
[buildah-e2]: https://github.com/podman-container-tools/buildah
[buildah-e3]: https://github.com/podman-container-tools/buildah/blob/main/LICENSE
[buildah-e4]: https://github.com/podman-container-tools/buildah/tree/main/docs
[buildah-e5]: https://github.com/podman-container-tools/buildah/blob/main/docs/buildah.1.md
[buildah-e6]: https://github.com/podman-container-tools/buildah/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/podman-container-tools/buildah) (`archived: false`).

### kubevirt

**Identity boundary:** KubeVirt extends Kubernetes with virtualization APIs/runtime to define and manage VMs alongside containers; it is not a general replacement for Kubernetes.

**Licence boundary:** Apache-2.0 applies to KubeVirt. Guest operating systems, VM images and vendor distributions have independent licences.

**Lifecycle boundary:** Current CNCF page states Incubating since 2022-04-19, not Graduated. Non-archived upstream, current commits and stable v1.9.0 release on 2026-07-30 support active status.

**Repository boundary:** Retain kubevirt/kubevirt; cluster-side deployment is self-hosted. Foundation status is verified directly rather than inferred from badges or maturity.

**Maturity:** Established is an editorial judgement based on maintained 1.x APIs and detailed VM/storage/network/migration operations; it does not assert CNCF graduation.

**Unresolved questions / limits:** None blocking. Hardware virtualization and supported node/storage/network configurations must be checked for each deployment.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Official project identity][kubevirt-e1], [Canonical repository][kubevirt-e2], [Software licence][kubevirt-e3], [Official documentation and operations][kubevirt-e4], [Current foundation status][kubevirt-e5], [Stable release history][kubevirt-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | kubevirt | kubevirt | [Canonical repository][kubevirt-e2], [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4] | Preserve stable catalogue identity and history. |
| `name` | KubeVirt | KubeVirt | [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Run VMs on Kubernetes. | Kubernetes virtualization API and runtime for defining and managing virtual-machine workloads alongside containers. | [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://kubevirt.io | https://kubevirt.io | [Canonical repository][kubevirt-e2], [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/kubevirt/kubevirt | https://github.com/kubevirt/kubevirt | [Canonical repository][kubevirt-e2], [Software licence][kubevirt-e3] | Keep the verified project pointer/official alias with its explicit boundary. |
| `documentation_url` | *absent* | https://kubevirt.io/user-guide/ | [Official documentation and operations][kubevirt-e4] | Add the directly identified official documentation entry point. |
| `categories` | kubernetes-distributions-operations | kubernetes-distributions-operations<br>virtualization-bare-metal-homelab | [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Kubernetes Management &amp; Operations | Kubernetes Virtual Machine Management | [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You need to run VM-based workloads alongside containers on the same platform. | You need to operate virtual machines and container workloads through Kubernetes APIs on infrastructure with the required virtualization, storage and networking support. | [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4], [Software licence][kubevirt-e3] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | All workloads are containerized—VMs add unnecessary complexity. | You only operate container workloads, or your Kubernetes nodes and operational model cannot support the required virtualization stack. | [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4], [Software licence][kubevirt-e3] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted | [Official documentation and operations][kubevirt-e4] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][kubevirt-e3] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Software licence][kubevirt-e3] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Software licence][kubevirt-e3] | Leave optional field absent; no blanket assertion about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Current foundation status][kubevirt-e5], [Stable release history][kubevirt-e6], [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Current foundation status][kubevirt-e5], [Stable release history][kubevirt-e6], [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical repository][kubevirt-e2] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Official project identity][kubevirt-e1], [Canonical repository][kubevirt-e2], [Software licence][kubevirt-e3], [Official documentation and operations][kubevirt-e4], [Current foundation status][kubevirt-e5], [Stable release history][kubevirt-e6] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L60<br>legacy:devopstools_final.md#L515 | legacy:4_Kubernetes-Containers/README.md#L60<br>legacy:devopstools_final.md#L515<br>https://kubevirt.io/<br>https://github.com/kubevirt/kubevirt<br>https://github.com/kubevirt/kubevirt/blob/main/LICENSE<br>https://kubevirt.io/user-guide/<br>https://www.cncf.io/projects/kubevirt/<br>https://github.com/kubevirt/kubevirt/releases | [Official project identity][kubevirt-e1], [Canonical repository][kubevirt-e2], [Software licence][kubevirt-e3], [Official documentation and operations][kubevirt-e4], [Current foundation status][kubevirt-e5], [Stable release history][kubevirt-e6] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Current foundation status][kubevirt-e5], [Stable release history][kubevirt-e6], [Official project identity][kubevirt-e1], [Official documentation and operations][kubevirt-e4] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `categories`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[kubevirt-e1]: https://kubevirt.io/
[kubevirt-e2]: https://github.com/kubevirt/kubevirt
[kubevirt-e3]: https://github.com/kubevirt/kubevirt/blob/main/LICENSE
[kubevirt-e4]: https://kubevirt.io/user-guide/
[kubevirt-e5]: https://www.cncf.io/projects/kubevirt/
[kubevirt-e6]: https://github.com/kubevirt/kubevirt/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/kubevirt/kubevirt) (`archived: false`).

### vcluster

**Identity boundary:** Scope the existing OSS record to tenant-cluster software with separate Kubernetes control planes and resource syncing. vCluster Platform and tier-gated capabilities are related commercial offerings, not the licence of this OSS record.

**Licence boundary:** Apache-2.0 applies to loft-sh/vcluster OSS. OSS needs neither a product licence nor Platform connectivity; even the no-cost Free tier adds separately activated features. Pro images and Platform entitlements are not inherited from the OSS licence.

**Lifecycle boundary:** Non-archived upstream, October 2026 maintenance and stable v0.37.3 released 2026-10-05 support active status; current docs explicitly describe OSS production usage.

**Repository boundary:** Retain loft-sh/vcluster and its OSS identity. Self-hosted tenant clusters run within customer infrastructure; no vendor-hosted OSS control plane is inferred.

**Maturity:** Established is a judgement grounded in maintained stable releases, operational tier/migration documentation and established tenant-cluster use; certification is not foundation graduation.

**Unresolved questions / limits:** None blocking the explicit OSS scope. Shared-host, private-node and other isolation modes have different resource/security/licensing requirements; no universal isolation guarantee is asserted.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical OSS repository][vcluster-e1], [Software licence][vcluster-e2], [Official documentation and scope][vcluster-e3], [OSS versus free and paid product boundary][vcluster-e4], [Platform licence management][vcluster-e5], [Stable release history][vcluster-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | vcluster | vcluster | [Canonical OSS repository][vcluster-e1], [Official documentation and scope][vcluster-e3] | Preserve stable catalogue identity and history. |
| `name` | vcluster | vCluster | [Official documentation and scope][vcluster-e3] | Changed: documented identity/capability; scoped boundary above applies. |
| `summary` | Run virtual Kubernetes clusters inside a host cluster (multi-tenancy / isolation). | Open-source Kubernetes tenant-cluster software with separate control planes and resource syncing; commercial Platform and tier-gated features have separate licensing. | [Official documentation and scope][vcluster-e3] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://www.vcluster.com | https://www.vcluster.com | [Canonical OSS repository][vcluster-e1], [Official documentation and scope][vcluster-e3] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/loft-sh/vcluster | https://github.com/loft-sh/vcluster | [Canonical OSS repository][vcluster-e1], [Software licence][vcluster-e2], [OSS versus free and paid product boundary][vcluster-e4], [Platform licence management][vcluster-e5] | Keep the verified project pointer/official alias with its explicit boundary. |
| `documentation_url` | *absent* | https://www.vcluster.com/docs/vcluster/ | [Official documentation and scope][vcluster-e3] | Add the directly identified official documentation entry point. |
| `categories` | kubernetes-distributions-operations | kubernetes-distributions-operations | [Official documentation and scope][vcluster-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Kubernetes Management &amp; Operations | Kubernetes Management &amp; Operations | [Official documentation and scope][vcluster-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Official documentation and scope][vcluster-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Official documentation and scope][vcluster-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You need isolated tenant clusters without provisioning physical infrastructure. | You need tenant Kubernetes APIs, CRDs and RBAC independent of a shared host control plane, and can choose documented OSS or separately licensed Platform capabilities. | [Official documentation and scope][vcluster-e3], [Software licence][vcluster-e2], [OSS versus free and paid product boundary][vcluster-e4], [Platform licence management][vcluster-e5] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | Namespace-level isolation with RBAC and network policies is sufficient. | Namespace isolation is sufficient, or you assume the Apache-licensed OSS image includes tier-gated Platform, private-node or enterprise features. | [Official documentation and scope][vcluster-e3], [Software licence][vcluster-e2], [OSS versus free and paid product boundary][vcluster-e4], [Platform licence management][vcluster-e5] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted | [Official documentation and scope][vcluster-e3] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][vcluster-e2], [OSS versus free and paid product boundary][vcluster-e4], [Platform licence management][vcluster-e5] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Software licence][vcluster-e2], [OSS versus free and paid product boundary][vcluster-e4], [Platform licence management][vcluster-e5] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Software licence][vcluster-e2], [OSS versus free and paid product boundary][vcluster-e4], [Platform licence management][vcluster-e5] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [Stable release history][vcluster-e6], [Official documentation and scope][vcluster-e3] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Stable release history][vcluster-e6], [Official documentation and scope][vcluster-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical OSS repository][vcluster-e1] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Official documentation and scope][vcluster-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Official documentation and scope][vcluster-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical OSS repository][vcluster-e1], [Software licence][vcluster-e2], [Official documentation and scope][vcluster-e3], [OSS versus free and paid product boundary][vcluster-e4], [Platform licence management][vcluster-e5], [Stable release history][vcluster-e6] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L65<br>legacy:devopstools_final.md#L525 | legacy:4_Kubernetes-Containers/README.md#L65<br>legacy:devopstools_final.md#L525<br>https://github.com/loft-sh/vcluster<br>https://github.com/loft-sh/vcluster/blob/main/LICENSE<br>https://www.vcluster.com/docs/vcluster/<br>https://www.vcluster.com/docs/vcluster/introduction/oss-vs-free<br>https://www.vcluster.com/docs/platform/understand/licensing<br>https://github.com/loft-sh/vcluster/releases | [Canonical OSS repository][vcluster-e1], [Software licence][vcluster-e2], [Official documentation and scope][vcluster-e3], [OSS versus free and paid product boundary][vcluster-e4], [Platform licence management][vcluster-e5], [Stable release history][vcluster-e6] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Stable release history][vcluster-e6], [Official documentation and scope][vcluster-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `name`, `summary`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[vcluster-e1]: https://github.com/loft-sh/vcluster
[vcluster-e2]: https://github.com/loft-sh/vcluster/blob/main/LICENSE
[vcluster-e3]: https://www.vcluster.com/docs/vcluster/
[vcluster-e4]: https://www.vcluster.com/docs/vcluster/introduction/oss-vs-free
[vcluster-e5]: https://www.vcluster.com/docs/platform/understand/licensing
[vcluster-e6]: https://github.com/loft-sh/vcluster/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/loft-sh/vcluster) (`archived: false`).

### cadvisor

**Identity boundary:** Google-hosted cAdvisor is a daemon that collects, aggregates and exports container resource/performance metrics. The existing precise summary is retained; scope is broader than Kubernetes-only observability.

**Licence boundary:** Actual LICENSE grants Apache-2.0 despite GitHub automated metadata reporting NOASSERTION; the licence file governs this decision.

**Lifecycle boundary:** Non-archived upstream, October 2026 commits and stable v0.60.6 released 2026-09-18 support active maintenance rather than relying on HTTP availability.

**Repository boundary:** Retain google/cadvisor and use that same stable official upstream as official_url instead of inventing a separate product site. Docs live in the upstream docs directory.

**Maturity:** Established follows maintenance since 2014, documented runtime/export/client interfaces and current stable releases.

**Unresolved questions / limits:** None blocking. Runtime/host-access requirements and metric support depend on the deployment; cAdvisor is not a complete hosted monitoring service.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical upstream identity and documentation links][cadvisor-e1], [Software licence][cadvisor-e2], [Official documentation][cadvisor-e3], [Daemon deployment and host access][cadvisor-e4], [Stable release history][cadvisor-e5].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | cadvisor | cadvisor | [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3] | Preserve stable catalogue identity and history. |
| `name` | cAdvisor | cAdvisor | [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Container Advisor daemon that collects, aggregates, and exports container resource usage and performance data. | Container Advisor daemon that collects, aggregates, and exports container resource usage and performance data. | [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `official_url` | *absent* | https://github.com/google/cadvisor | [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/google/cadvisor | https://github.com/google/cadvisor | [Canonical upstream identity and documentation links][cadvisor-e1], [Software licence][cadvisor-e2] | Keep the verified project pointer/official alias with its explicit boundary. |
| `documentation_url` | *absent* | https://github.com/google/cadvisor/tree/master/docs | [Official documentation][cadvisor-e3] | Add the directly identified official documentation entry point. |
| `categories` | monitoring-metrics-logs-tracing | monitoring-metrics-logs-tracing | [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Kubernetes Observability &amp; Troubleshooting | Container Resource Monitoring | [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>site-reliability-engineer<br>observability-engineer | devops-engineer<br>site-reliability-engineer<br>observability-engineer | [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | operate<br>monitor | operate<br>monitor | [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | `[]` | You need per-container and host resource/performance metrics from a cAdvisor daemon, including export to a separate monitoring backend. | [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3], [Software licence][cadvisor-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | `[]` | You need a complete alerting, tracing and long-term observability platform, or cannot provide the documented host/runtime visibility needed to collect metrics. | [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3], [Software licence][cadvisor-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted | [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][cadvisor-e2] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Software licence][cadvisor-e2] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Software licence][cadvisor-e2] | Leave optional field absent; no blanket assertion about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Stable release history][cadvisor-e5], [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Stable release history][cadvisor-e5], [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical upstream identity and documentation links][cadvisor-e1] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical upstream identity and documentation links][cadvisor-e1], [Software licence][cadvisor-e2], [Official documentation][cadvisor-e3], [Daemon deployment and host access][cadvisor-e4], [Stable release history][cadvisor-e5] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:devopstools_final.md#L723 | legacy:devopstools_final.md#L723<br>https://github.com/google/cadvisor<br>https://github.com/google/cadvisor/blob/master/LICENSE<br>https://github.com/google/cadvisor/tree/master/docs<br>https://github.com/google/cadvisor/blob/master/docs/running.md<br>https://github.com/google/cadvisor/releases | [Canonical upstream identity and documentation links][cadvisor-e1], [Software licence][cadvisor-e2], [Official documentation][cadvisor-e3], [Daemon deployment and host access][cadvisor-e4], [Stable release history][cadvisor-e5] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Stable release history][cadvisor-e5], [Canonical upstream identity and documentation links][cadvisor-e1], [Official documentation][cadvisor-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `official_url`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[cadvisor-e1]: https://github.com/google/cadvisor
[cadvisor-e2]: https://github.com/google/cadvisor/blob/master/LICENSE
[cadvisor-e3]: https://github.com/google/cadvisor/tree/master/docs
[cadvisor-e4]: https://github.com/google/cadvisor/blob/master/docs/running.md
[cadvisor-e5]: https://github.com/google/cadvisor/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/google/cadvisor) (`archived: false`).

### uptime-kuma

**Identity boundary:** Self-hosted monitoring application covering multiple service checks, notifications and status pages, rather than full infrastructure observability.

**Licence boundary:** MIT applies to upstream Uptime Kuma; sponsoring and third-party hosting do not establish a first-party commercial SaaS offering.

**Lifecycle boundary:** Non-archived upstream, current commits and stable 2.5.5 released 2026-09-16 support active status.

**Repository boundary:** Retain louislam/uptime-kuma. Its README directly points to the official wiki for installation/update documentation. Docker and Node installations both remain self-hosted.

**Maturity:** Established follows maintained 2.x releases, sustained development since 2021 and documented updates/install/notification workflows.

**Unresolved questions / limits:** None blocking. Third-party hosting services and notification integrations are outside this upstream offering/licence claim.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Official project site][uptime-kuma-e1], [Canonical repository and monitoring scope][uptime-kuma-e2], [Software licence][uptime-kuma-e3], [Official documentation wiki][uptime-kuma-e4], [Stable release history][uptime-kuma-e5].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | uptime-kuma | uptime-kuma | [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4] | Preserve stable catalogue identity and history. |
| `name` | Uptime Kuma | Uptime Kuma | [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Self-hosted uptime monitoring. | Self-hosted uptime-monitoring application with service checks, notifications and public status pages. | [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://uptime.kuma.pet | https://uptime.kuma.pet | [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/louislam/uptime-kuma | https://github.com/louislam/uptime-kuma | [Canonical repository and monitoring scope][uptime-kuma-e2], [Software licence][uptime-kuma-e3] | Keep the verified project pointer/official alias with its explicit boundary. |
| `documentation_url` | *absent* | https://github.com/louislam/uptime-kuma/wiki | [Official documentation wiki][uptime-kuma-e4] | Add the directly identified official documentation entry point. |
| `categories` | monitoring-metrics-logs-tracing | monitoring-metrics-logs-tracing | [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Monitoring &amp; Observability Platforms | Monitoring &amp; Observability Platforms | [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>site-reliability-engineer<br>observability-engineer | devops-engineer<br>site-reliability-engineer<br>observability-engineer | [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | operate<br>monitor | operate<br>monitor | [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | Simple, self-hosted uptime/status-page monitoring. | You need self-hosted service uptime checks, notifications and status pages using documented HTTP, TCP, DNS, ping or other supported monitors. | [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4], [Software licence][uptime-kuma-e3] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | You need full infrastructure observability beyond HTTP/TCP checks. | You need comprehensive metrics, logs and distributed tracing, or a first-party managed monitoring service rather than operating the application yourself. | [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4], [Software licence][uptime-kuma-e3] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted | [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][uptime-kuma-e3] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | MIT | [Software licence][uptime-kuma-e3] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Software licence][uptime-kuma-e3] | Leave optional field absent; no blanket assertion about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Stable release history][uptime-kuma-e5], [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Stable release history][uptime-kuma-e5], [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical repository and monitoring scope][uptime-kuma-e2] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Official project site][uptime-kuma-e1], [Canonical repository and monitoring scope][uptime-kuma-e2], [Software licence][uptime-kuma-e3], [Official documentation wiki][uptime-kuma-e4], [Stable release history][uptime-kuma-e5] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:5_Monitoring-Observability/README.md#L22<br>legacy:devopstools_final.md#L718 | legacy:5_Monitoring-Observability/README.md#L22<br>legacy:devopstools_final.md#L718<br>https://uptime.kuma.pet/<br>https://github.com/louislam/uptime-kuma<br>https://github.com/louislam/uptime-kuma/blob/master/LICENSE<br>https://github.com/louislam/uptime-kuma/wiki<br>https://github.com/louislam/uptime-kuma/releases | [Official project site][uptime-kuma-e1], [Canonical repository and monitoring scope][uptime-kuma-e2], [Software licence][uptime-kuma-e3], [Official documentation wiki][uptime-kuma-e4], [Stable release history][uptime-kuma-e5] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Stable release history][uptime-kuma-e5], [Canonical repository and monitoring scope][uptime-kuma-e2], [Official documentation wiki][uptime-kuma-e4] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[uptime-kuma-e1]: https://uptime.kuma.pet/
[uptime-kuma-e2]: https://github.com/louislam/uptime-kuma
[uptime-kuma-e3]: https://github.com/louislam/uptime-kuma/blob/master/LICENSE
[uptime-kuma-e4]: https://github.com/louislam/uptime-kuma/wiki
[uptime-kuma-e5]: https://github.com/louislam/uptime-kuma/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/louislam/uptime-kuma) (`archived: false`).

### camunda

**Identity boundary:** Preserve ID camunda, explicitly scope name/summary to current Camunda 8 parent platform. SaaS and Self-Managed share process-orchestration scope; Camunda 7 is a historical separate lifecycle boundary.

**Licence boundary:** Change open-core to commercial for the customer-facing platform: compiled core/platform components are proprietary and Self-Managed production requires an Enterprise licence. Public core source uses Camunda License 1.0, restricted to non-production, while specified SDKs/connectors/modeler components have separate Apache/MIT licences. Source-available describes that source subset, not the entire parent platform; open-core would incorrectly imply an OSS core. No product-wide SPDX.

**Lifecycle boundary:** Maintained Camunda 8 releases and current operations documentation support active status. Camunda 7 CE ended maintenance after its October 2025 final feature release; 7 Enterprise has a distinct extended support timeline. Neither determines Camunda 8 status.

**Repository boundary:** Add camunda/camunda as canonical source pointer for Orchestration Cluster components and Optimize, as its README specifies; it is not the full SaaS platform nor proprietary Console/Web Modeler source.

**Maturity:** Established follows maintained release/support policies, documented distributed deployment/upgrade operations and long-running process-orchestration capabilities.

**Unresolved questions / limits:** None blocking the explicit Camunda 8 parent scope. Non-production permissions, production entitlements and independently licensed components must not be conflated; no Camunda 7 or SDK licence is assigned to this parent.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Current parent platform and deployment boundary][camunda-e1], [Canonical core repository and component boundary][camunda-e2], [Current core source licence][camunda-e3], [Official documentation][camunda-e4], [Platform licence and component exceptions][camunda-e5], [Production installation and operations][camunda-e6], [Historical Camunda 7 lifecycle boundary][camunda-e7], [Current release history][camunda-e8].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | camunda | camunda | [Canonical core repository and component boundary][camunda-e2], [Official documentation][camunda-e4] | Preserve stable catalogue identity and history. |
| `name` | Camunda | Camunda 8 | [Official documentation][camunda-e4] | Changed: documented identity/capability; scoped boundary above applies. |
| `summary` | Workflow and process automation (BPMN/DMN). | Commercial process-orchestration platform for BPMN workflows and DMN decisions, offered as SaaS or Self-Managed with separate production licensing. | [Official documentation][camunda-e4] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://camunda.com | https://camunda.com | [Canonical core repository and component boundary][camunda-e2], [Official documentation][camunda-e4] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | *absent* | https://github.com/camunda/camunda | [Canonical core repository and component boundary][camunda-e2], [Current core source licence][camunda-e3], [Platform licence and component exceptions][camunda-e5] | Add the directly verified core/server pointer with its explicit boundary. |
| `documentation_url` | *absent* | https://docs.camunda.io/docs/ | [Official documentation][camunda-e4] | Add the directly identified official documentation entry point. |
| `categories` | workflow-automation-chatops | workflow-automation-chatops | [Official documentation][camunda-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Automation &amp; Workflow | Automation &amp; Workflow | [Official documentation][camunda-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>site-reliability-engineer<br>developer-experience-engineer | devops-engineer<br>site-reliability-engineer<br>developer-experience-engineer | [Official documentation][camunda-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | plan<br>operate | plan<br>develop<br>deploy<br>operate | [Official documentation][camunda-e4] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | * You need BPMN-based process orchestration with long-running workflows and human tasks. | You need distributed BPMN/DMN process orchestration with service integration and human tasks, and can select SaaS or license Self-Managed production deployment. | [Official documentation][camunda-e4], [Production installation and operations][camunda-e6], [Current core source licence][camunda-e3], [Platform licence and component exceptions][camunda-e5] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | * You need lightweight CI/CD or task automation without formal process modeling. | You require the entire current platform under an OSS licence, assume non-production permission allows production use, or only need lightweight task automation. | [Official documentation][camunda-e4], [Production installation and operations][camunda-e6], [Current core source licence][camunda-e3], [Platform licence and component exceptions][camunda-e5] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | hosted-saas<br>self-hosted | [Official documentation][camunda-e4], [Production installation and operations][camunda-e6] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | open-core | commercial | [Current core source licence][camunda-e3], [Platform licence and component exceptions][camunda-e5] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | *absent* | [Current core source licence][camunda-e3], [Platform licence and component exceptions][camunda-e5] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Current core source licence][camunda-e3], [Platform licence and component exceptions][camunda-e5], [Current parent platform and deployment boundary][camunda-e1] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [Historical Camunda 7 lifecycle boundary][camunda-e7], [Current release history][camunda-e8], [Official documentation][camunda-e4] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Historical Camunda 7 lifecycle boundary][camunda-e7], [Current release history][camunda-e8], [Official documentation][camunda-e4] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical core repository and component boundary][camunda-e2] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Official documentation][camunda-e4] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Official documentation][camunda-e4] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Current parent platform and deployment boundary][camunda-e1], [Canonical core repository and component boundary][camunda-e2], [Current core source licence][camunda-e3], [Official documentation][camunda-e4], [Platform licence and component exceptions][camunda-e5], [Production installation and operations][camunda-e6], [Historical Camunda 7 lifecycle boundary][camunda-e7], [Current release history][camunda-e8] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:3_CI-CD-Automation/README.md#L162<br>legacy:devopstools_final.md#L402 | legacy:3_CI-CD-Automation/README.md#L162<br>legacy:devopstools_final.md#L402<br>https://camunda.com/platform/<br>https://github.com/camunda/camunda<br>https://github.com/camunda/camunda/blob/main/licenses/CAMUNDA-LICENSE-1.0.txt<br>https://docs.camunda.io/docs/<br>https://docs.camunda.io/docs/reference/licenses/<br>https://docs.camunda.io/docs/self-managed/setup/overview/<br>https://camunda.com/blog/2025/02/camunda-7-enterprise-end-of-life-extension/<br>https://github.com/camunda/camunda/releases | [Current parent platform and deployment boundary][camunda-e1], [Canonical core repository and component boundary][camunda-e2], [Current core source licence][camunda-e3], [Official documentation][camunda-e4], [Platform licence and component exceptions][camunda-e5], [Production installation and operations][camunda-e6], [Historical Camunda 7 lifecycle boundary][camunda-e7], [Current release history][camunda-e8] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Historical Camunda 7 lifecycle boundary][camunda-e7], [Current release history][camunda-e8], [Official documentation][camunda-e4] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `name`, `summary`, `repository_url`, `documentation_url`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_model`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[camunda-e1]: https://camunda.com/platform/
[camunda-e2]: https://github.com/camunda/camunda
[camunda-e3]: https://github.com/camunda/camunda/blob/main/licenses/CAMUNDA-LICENSE-1.0.txt
[camunda-e4]: https://docs.camunda.io/docs/
[camunda-e5]: https://docs.camunda.io/docs/reference/licenses/
[camunda-e6]: https://docs.camunda.io/docs/self-managed/setup/overview/
[camunda-e7]: https://camunda.com/blog/2025/02/camunda-7-enterprise-end-of-life-extension/
[camunda-e8]: https://github.com/camunda/camunda/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/camunda/camunda) (`archived: false`).

### passbolt

**Identity boundary:** Scope the password-management record to the server-backed Community/Pro product and documented vendor Cloud offering. Browser, mobile, CLI and desktop clients are separate components, not interchangeable canonical server repositories.

**Licence boundary:** Correct open-core to oss. The server manifest declares AGPL-3.0-or-later, corroborated by source headers and Pro terms section 2.5. Current official announcement explicitly says Pro features are in the same AGPL codebase, not proprietary plugins. Pro subscription keys/services have separate contractual restrictions. No blanket licence for client code, third-party libraries, trademarks or hosted-service terms is asserted.

**Lifecycle boundary:** Non-archived upstream, September 2026 maintenance and stable server v5.16.0 released 2026-09-17 support active status; the unified-codebase announcement is current edition evidence.

**Repository boundary:** Add passbolt/passbolt_api as the directly verified first-party server repository. The README links separate client applications; aliases in its links do not justify inventing separate catalogue records.

**Maturity:** Established follows maintained 5.x server releases, documented updates/deployment and sustained product development since 2016.

**Unresolved questions / limits:** None blocking server/software scope. Subscription-key restrictions and service access are distinct from AGPL rights; future keys/features and separate client licences require their own evidence.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical server repository and client boundary][passbolt-e1], [Server software licence][passbolt-e2], [Server SPDX declaration][passbolt-e3], [Official documentation and deployment scope][passbolt-e4], [Pro software licence and subscription-key terms][passbolt-e5], [Community and Pro unified OSS codebase][passbolt-e6], [Current edition boundary][passbolt-e7], [Stable server release history][passbolt-e8].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | passbolt | passbolt | [Canonical server repository and client boundary][passbolt-e1], [Official documentation and deployment scope][passbolt-e4] | Preserve stable catalogue identity and history. |
| `name` | passbolt | passbolt | [Official documentation and deployment scope][passbolt-e4] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Password manager for teams with self-hosted and paid offerings. | Open-source team password-management server with Community and subscription-enabled Pro features, offered self-hosted or through Passbolt Cloud. | [Official documentation and deployment scope][passbolt-e4] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://www.passbolt.com | https://www.passbolt.com | [Canonical server repository and client boundary][passbolt-e1], [Official documentation and deployment scope][passbolt-e4] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | *absent* | https://github.com/passbolt/passbolt_api | [Canonical server repository and client boundary][passbolt-e1], [Server software licence][passbolt-e2], [Server SPDX declaration][passbolt-e3], [Pro software licence and subscription-key terms][passbolt-e5], [Community and Pro unified OSS codebase][passbolt-e6] | Add the directly verified core/server pointer with its explicit boundary. |
| `documentation_url` | *absent* | https://www.passbolt.com/docs/ | [Official documentation and deployment scope][passbolt-e4] | Add the directly identified official documentation entry point. |
| `categories` | iam-secrets-certificates | iam-secrets-certificates | [Official documentation and deployment scope][passbolt-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Secret Management | Secret Management | [Official documentation and deployment scope][passbolt-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | cloud-engineer<br>devsecops-engineer<br>cloud-security-engineer | cloud-engineer<br>devsecops-engineer<br>cloud-security-engineer | [Official documentation and deployment scope][passbolt-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | operate<br>secure | operate<br>secure | [Official documentation and deployment scope][passbolt-e4] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | Team password sharing with GPG-based encryption and self-hosting. | You need end-to-end encrypted team credential sharing through the AGPL-licensed server, choosing Community, subscription-enabled Pro or vendor-managed Cloud deployment. | [Official documentation and deployment scope][passbolt-e4], [Server software licence][passbolt-e2], [Server SPDX declaration][passbolt-e3], [Pro software licence and subscription-key terms][passbolt-e5], [Community and Pro unified OSS codebase][passbolt-e6] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | You need machine-to-machine secret management (use Vault). | You need machine-to-machine secret delivery instead of team credential collaboration, or assume software AGPL rights include unrestricted subscription-key transfer or hosted-service access. | [Official documentation and deployment scope][passbolt-e4], [Server software licence][passbolt-e2], [Server SPDX declaration][passbolt-e3], [Pro software licence and subscription-key terms][passbolt-e5], [Community and Pro unified OSS codebase][passbolt-e6] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted<br>hosted-saas | [Official documentation and deployment scope][passbolt-e4] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | open-core | oss | [Server software licence][passbolt-e2], [Server SPDX declaration][passbolt-e3], [Pro software licence and subscription-key terms][passbolt-e5], [Community and Pro unified OSS codebase][passbolt-e6] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | AGPL-3.0-or-later | [Server software licence][passbolt-e2], [Server SPDX declaration][passbolt-e3], [Pro software licence and subscription-key terms][passbolt-e5], [Community and Pro unified OSS codebase][passbolt-e6] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Server software licence][passbolt-e2], [Server SPDX declaration][passbolt-e3], [Pro software licence and subscription-key terms][passbolt-e5], [Community and Pro unified OSS codebase][passbolt-e6], [Current edition boundary][passbolt-e7] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [Stable server release history][passbolt-e8], [Official documentation and deployment scope][passbolt-e4] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Stable server release history][passbolt-e8], [Official documentation and deployment scope][passbolt-e4] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical server repository and client boundary][passbolt-e1] | GitHub API reports archived=false for the verified repository target; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Official documentation and deployment scope][passbolt-e4] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Official documentation and deployment scope][passbolt-e4] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical server repository and client boundary][passbolt-e1], [Server software licence][passbolt-e2], [Server SPDX declaration][passbolt-e3], [Official documentation and deployment scope][passbolt-e4], [Pro software licence and subscription-key terms][passbolt-e5], [Community and Pro unified OSS codebase][passbolt-e6], [Current edition boundary][passbolt-e7], [Stable server release history][passbolt-e8] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:6_Security/README.md#L93<br>legacy:devopstools_final.md#L982 | legacy:6_Security/README.md#L93<br>legacy:devopstools_final.md#L982<br>https://github.com/passbolt/passbolt_api<br>https://github.com/passbolt/passbolt_api/blob/master/LICENSE.txt<br>https://github.com/passbolt/passbolt_api/blob/master/composer.json<br>https://www.passbolt.com/docs/<br>https://www.passbolt.com/terms/pro<br>https://www.passbolt.com/blog/passbolt-5-13-one-open-source-codebase-for-community-and-pro-editions<br>https://www.passbolt.com/pricing/pro<br>https://github.com/passbolt/passbolt_api/releases | [Canonical server repository and client boundary][passbolt-e1], [Server software licence][passbolt-e2], [Server SPDX declaration][passbolt-e3], [Official documentation and deployment scope][passbolt-e4], [Pro software licence and subscription-key terms][passbolt-e5], [Community and Pro unified OSS codebase][passbolt-e6], [Current edition boundary][passbolt-e7], [Stable server release history][passbolt-e8] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Stable server release history][passbolt-e8], [Official documentation and deployment scope][passbolt-e4] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `repository_url`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_model`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[passbolt-e1]: https://github.com/passbolt/passbolt_api
[passbolt-e2]: https://github.com/passbolt/passbolt_api/blob/master/LICENSE.txt
[passbolt-e3]: https://github.com/passbolt/passbolt_api/blob/master/composer.json
[passbolt-e4]: https://www.passbolt.com/docs/
[passbolt-e5]: https://www.passbolt.com/terms/pro
[passbolt-e6]: https://www.passbolt.com/blog/passbolt-5-13-one-open-source-codebase-for-community-and-pro-editions
[passbolt-e7]: https://www.passbolt.com/pricing/pro
[passbolt-e8]: https://github.com/passbolt/passbolt_api/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/passbolt/passbolt_api) (`archived: false`).

## Review-debt accounting

`python -m scripts.review_debt --format markdown --limit 30` was captured before and after. Selected: **10**; cleared: **10**; retained: **0**.

| Counter | Before | After |
|---|---:|---:|
| canonical_records | 1,425 | 1,425 |
| needs_review | 776 | 766 |
| status_needs_review | 776 | 766 |
| mismatches | 0 | 0 |
| unknown_license | 81 | 81 |
| unknown_maturity | 913 | 903 |
| missing_repository | 394 | 392 |
| missing_documentation | 910 | 900 |
| missing_sources | 0 | 0 |

The invariant `needs_review == status needs-review` holds for every canonical record. Missing repositories decrease by two through verified Camunda core and Passbolt server pointers; missing documentation decreases by ten. Unknown licence debt is unchanged.

## Generated changes

Only generator output is listed here; the evidence report and focused regression test are authored files.

- `README.md`
- `docs/catalog-statistics.json`
- `docs/categories/containers-image-tooling.md`
- `docs/categories/iam-secrets-certificates.md`
- `docs/categories/infrastructure-as-code.md`
- `docs/categories/kubernetes-distributions-operations.md`
- `docs/categories/monitoring-metrics-logs-tracing.md`
- `docs/categories/virtualization-bare-metal-homelab.md`
- `docs/categories/workflow-automation-chatops.md`
- `docs/lifecycle/build.md`
- `docs/lifecycle/deploy.md`
- `docs/lifecycle/develop.md`
- `docs/lifecycle/monitor.md`
- `docs/lifecycle/operate.md`
- `docs/lifecycle/plan.md`
- `docs/lifecycle/release.md`
- `docs/lifecycle/secure.md`
- `docs/roles/cloud-engineer.md`
- `docs/roles/cloud-security-engineer.md`
- `docs/roles/developer-experience-engineer.md`
- `docs/roles/devops-engineer.md`
- `docs/roles/devsecops-engineer.md`
- `docs/roles/infrastructure-systems-engineer.md`
- `docs/roles/kubernetes-engineer.md`
- `docs/roles/observability-engineer.md`
- `docs/roles/platform-engineer.md`
- `docs/roles/site-reliability-engineer.md`

## Validation and full link audit

Required checks passed. Python 3.12.3 in the existing WSL Ubuntu constrained environment ran installation, fresh dependency resolution and the complete test suite. The Windows editable environment ran focused tests, lint/format, generation, catalogue validation and debt capture. `python` below denotes the selected environment interpreter.

| Command | Result |
|---|---|
| `python -m pip install -e '.[dev]' -c config/python-constraints-3.12.txt` | PASS; constrained editable install |
| `python -m scripts.python_constraints --check` | PASS; fresh resolver matches unchanged reviewed constraints |
| `python -m ruff check scripts tests` | PASS |
| `python -m ruff format --check scripts tests` | PASS; 59 files already formatted |
| `python -m pytest tests/test_wave6_evidence_review.py` | PASS; 17 tests |
| `python -m pytest` | PASS; 704 tests in 295.25 seconds |
| `python -m scripts.generate_docs` | PASS; regenerated after canonical changes |
| `python -m scripts.generate_docs --check` | PASS |
| `python -m scripts.validate_catalog` | PASS |
| `python -m scripts.review_debt --format markdown --limit 30` | PASS; before/after counters captured |
| `git diff --check` | PASS |

Both the focused Windows run and full Linux run emitted a non-failing pytest cache permission warning. WSL Git-dependent tests used process-only `GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=true` to interpret the Windows checkout line endings consistently; no repository or global Git configuration was changed. No checks or assertions were weakened.

The focused tests guard OSS upstream/SPDX boundaries, OpenTofu governance/migration evidence, current Packer BUSL versus historical MPL and HCP/plugins, BuildKit backend versus Buildx, daemonless Buildah versus Podman, KubeVirt VM/governance scope, vCluster OSS versus Platform entitlements, cAdvisor upstream documentation, Uptime Kuma self-hosting, Camunda parent versus component licences, and Passbolt AGPL software versus subscription keys. They do not assert prices, temporary release versions or marketing claims.

One full fresh strict link audit used the requested flags, ignored output paths and no cache reuse:

```bash
python -m scripts.check_links --strict --check-archived --workers 8 --cache tmp/wave6/link-cache.json --cache-hours 0 --json-report tmp/wave6/link-report.json --markdown-report tmp/wave6/link-report.md
```

| Audit counter | Result |
|---|---:|
| URLs | 2,636 |
| blocking_new | 0 |
| blocking_known observed | 4 |
| strict_result | PASS |

The six-entry reviewed baseline is unchanged. Each observed baseline response is recorded below; a nonblocking rate limit, access restriction or inconclusive response does not prove the historical defect was fixed.

| Existing baseline URL | Observed response | Classification / strict status |
|---|---|---|
| `https://github.com/hoji-ai/hoji` | HTTP 429 | rate-limited / nonblocking |
| `https://github.com/ophircloud/DevOps-Projects` | HTTP 429 | rate-limited / nonblocking |
| `https://hub.docker.com/r/soosio/dast` | HTTP 404 | manual-verification-required / blocking-known |
| `https://kubeflame.github.io` | HTTP 404 | manual-verification-required / blocking-known |
| `https://www.opentext.com/products/static-application-security-testing` | HTTP 444 | http-error / blocking-known |
| `https://www.yotascale.com` | HTTP 404 | manual-verification-required / blocking-known |

All ten documentation entry points were included in the final canonical inventory:

| ID | Documentation response | Classification |
|---|---|---|
| `opentofu` | HTTP 200 | valid |
| `packer` | HTTP 200 | valid |
| `buildkit` | HTTP 200 | valid |
| `buildah` | HTTP 403 | restricted-or-bot-blocked |
| `kubevirt` | HTTP 200 | valid |
| `vcluster` | HTTP 200 | valid |
| `cadvisor` | HTTP 429 | rate-limited |
| `uptime-kuma` | HTTP 429 | rate-limited |
| `camunda` | HTTP 200 | permanent-redirect |
| `passbolt` | HTTP 200 | valid |

All audit classifications (including network limits):

| Classification | Count |
|---|---:|
| dns-inconclusive | 5 |
| http-error | 1 |
| manual-verification-required | 3 |
| network-inconclusive | 1 |
| permanent-redirect | 206 |
| rate-limited | 758 |
| restricted-or-bot-blocked | 357 |
| timeout-inconclusive | 1 |
| transient-failure | 1 |
| valid | 1,267 |
| valid-redirect | 36 |

Strict PASS means no newly classified blockers, not successful verification of every endpoint. Upstream API archival metadata, actual licence files and directly read documentation/releases independently support the review decisions. Source-only evidence URLs were read separately; the checker inventories official/repository/documentation fields.

Raw audit/cache output remains in ignored `tmp/wave6/`. No output under `reports/` is committed. No additional full audit was run.

## Scope verification and review state

Comparison with the pre-edit snapshot and baseline Git tree confirms exactly ten changed IDs, ten changed verification dates, ten changed record blocks and 240 material-field rows. Stable IDs and every historical source are preserved. All other canonical records remain unchanged. Audited URLs match the final canonical inventory. The six-entry baseline is unchanged. Issue #2 body and updated_at (2026-10-07T16:43:15Z) match the pre-edit snapshot; it is checked again at handoff.

Material evidence corrections resolved within this cohort: independent OpenTofu governance and conditional migration; Packer current BUSL/version/plugin/HCP boundaries; BuildKit backend versus Buildx client; Buildah versus Podman and the existing official upstream alias; KubeVirt VM scope and directly confirmed CNCF Incubating status; vCluster OSS versus Free/Platform licensing; cAdvisor actual Apache licence versus automated NOASSERTION and stable official upstream; Uptime Kuma upstream self-hosting; commercial Camunda 8 parent versus non-production source, SDK exceptions and Camunda 7 history; Passbolt current unified AGPL server/Pro software versus contractual keys and separately licensed clients.

Camunda classification is an editorial application of the existing licence-model taxonomy to the customer-facing parent platform. `source-available` describes its public core-source subset; the platform includes proprietary binaries and privately sourced components and requires production licensing. Passbolt current primary evidence contradicts the older assumption that Pro features are proprietary: its unification announcement and Pro terms expressly cover the AGPL software, while keys/services retain separate terms.

CI/security outcomes and any subsequent automatic PR findings are reported against the final commit in the PR and final handoff. No merge or release is performed.
