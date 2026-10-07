# Evidence review Wave 5 — 2026-10-07

Exactly ten existing canonical records were reviewed. All ten receive **CLEAR REVIEW**. Stable IDs and every previous provenance source are preserved. Canonical YAML is authoritative; generated pages were regenerated.

## Verified baseline and scope

- Main: `6be88be4ad7a386eb0a5cb511d3ebc20766c73a1` (post-#106).
- Branch: `maintenance/wave-5-evidence-review`.
- Before editing: clean working tree, zero open PRs, zero open CodeQL alerts; all five exact-main check runs passed (CodeQL actions/python, Plumber, gitleaks, catalogue validate).
- Issue #2 was read and states Wave 5 — NOT STARTED — READY TO SCOPE. It is not edited.
- Exactly these ten IDs differ from the pre-edit snapshot of all 1,425 records. Other record blocks remain byte-for-byte unchanged. k0rdent and Spinnaker move to their corrected primary-category files.
- No baseline, committed audit report, link ledger, issue, workflow, CodeQL configuration, dependency constraint or unrelated record changes; no Wave 4 retained records or Wave 6 work.

This fixed cohort balances core DevOps foundations, commercial parent-product boundaries, stale verification, identity/lifecycle corrections and direct primary-source availability. All ten initially had review flag/status debt, unknown maturity and missing documentation. The rank below is the user-specified order.

| Rank | ID | Initial name | Initial category | Initial debt |
|---:|---|---|---|---|
| 1 | `k0rdent` | k0rdent | `application-cloud-security` | needs-review; unknown maturity; missing docs |
| 2 | `nexus-repository` | Nexus Repository | `artifact-package-management` | needs-review; unknown maturity; missing docs |
| 3 | `teamcity` | TeamCity | `ci-build-testing` | needs-review; unknown maturity; missing docs; unknown licence; missing parent repository |
| 4 | `spacelift` | Spacelift | `infrastructure-as-code` | needs-review; unknown maturity; missing docs; unknown licence; missing parent repository |
| 5 | `cloudbees` | CloudBees | `ci-build-testing` | needs-review; unknown maturity; missing docs; missing parent repository |
| 6 | `helm` | Helm | `kubernetes-networking-storage-addons` | needs-review; unknown maturity; missing docs |
| 7 | `tekton` | Tekton | `ci-build-testing` | needs-review; unknown maturity; missing docs |
| 8 | `terragrunt` | Terragrunt | `infrastructure-as-code` | needs-review; unknown maturity; missing docs |
| 9 | `cdk8s` | cdk8s | `infrastructure-as-code` | needs-review; unknown maturity; missing docs |
| 10 | `spinnaker` | Spinnaker | `ci-build-testing` | needs-review; unknown maturity; missing docs |

## Evidence method and interpretation

Search results were discovery aids; official documents, upstream source/licence files, release feeds and legal terms were read directly. GitHub repository metadata (`archived`, default branch and update dates) and release JSON were checked through its API. Link-audit responses alone do not establish lifecycle. The review date records this review action, not a vendor statement.

Maturity is a reviewer judgement from maintenance history, stable interfaces, documented operations and governance, not GitHub stars. Categories, roles and lifecycle stages map documented capabilities to the existing taxonomy. Use/avoid guidance describes selection tradeoffs, not newly invented vendor restrictions. Empty alternatives/tags and absent optional offering booleans are deliberately retained without unsupported comparative or parent-wide claims. A proprietary product need not acquire a fabricated public repository to clear review.

## Decisions and complete material-field review

### k0rdent

**Identity boundary:** Community-governed multi-cloud/multi-cluster management project; Mirantis documents a separate Enterprise distribution. The old scanner identity is contradicted by architecture and governance.

**Licence boundary:** Apache-2.0 applies to the open-source project; Mirantis enterprise-only features are a separate commercial offering, not relicensing of the upstream project.

**Lifecycle boundary:** Active KCM v1.12.0 released 2026-10-07; management clusters provision and operate workload clusters/services.

**Repository boundary:** Keep the canonical k0rdent umbrella; k0rdent/kcm supplies implementation/release evidence and is not substituted for project identity. GitHub API archived=false for both.

**Maturity:** Growing is a reviewer judgement based on an evolving 1.x project and documented cluster/service architecture, not popularity or a claim of long-established support.

**Unresolved questions / limits:** None blocking the scoped record. Edition entitlements and future releases remain subject to their own current documentation.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Scope and architecture][k0rdent-e1], [Project umbrella][k0rdent-e2], [Software licence][k0rdent-e3], [Current KCM release][k0rdent-e4], [Community governance][k0rdent-e5], [Mirantis enterprise boundary][k0rdent-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | k0rdent | k0rdent | [Project umbrella][k0rdent-e2], [Scope and architecture][k0rdent-e1] | Preserve stable catalogue identity and history. |
| `name` | k0rdent | k0rdent | [Scope and architecture][k0rdent-e1] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Kubernetes security and compliance scanner. | Kubernetes-native platform for distributed cluster lifecycle and multi-cluster service management. | [Scope and architecture][k0rdent-e1] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://docs.k0rdent.io/latest | https://docs.k0rdent.io/latest | [Project umbrella][k0rdent-e2], [Scope and architecture][k0rdent-e1] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/k0rdent/k0rdent | https://github.com/k0rdent/k0rdent | [Project umbrella][k0rdent-e2], [Software licence][k0rdent-e3], [Mirantis enterprise boundary][k0rdent-e6] | Keep the canonical project/core pointer with its explicit boundary. |
| `documentation_url` | *absent* | https://docs.k0rdent.io/latest/ | [Scope and architecture][k0rdent-e1] | Add the directly identified official documentation entry point. |
| `categories` | application-cloud-security | kubernetes-distributions-operations<br>platform-engineering-idp | [Scope and architecture][k0rdent-e1] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Application Security (SAST, DAST, SCA) &amp; Vulnerability Scanning | Distributed Kubernetes Management<br>Cluster and Service Lifecycle Management | [Scope and architecture][k0rdent-e1] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devsecops-engineer<br>cloud-security-engineer | platform-engineer<br>kubernetes-engineer<br>cloud-engineer<br>infrastructure-systems-engineer | [Scope and architecture][k0rdent-e1] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | test<br>secure | plan<br>deploy<br>operate | [Scope and architecture][k0rdent-e1] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | Kubernetes-native compliance checks. | You need declarative provisioning and lifecycle management of Kubernetes clusters and services across multiple infrastructure providers. | [Scope and architecture][k0rdent-e1], [Software licence][k0rdent-e3], [Mirantis enterprise boundary][k0rdent-e6] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | You need broader cloud security posture beyond K8s. | You only need a vulnerability or compliance scanner, or a single cluster without a distributed management control plane. | [Scope and architecture][k0rdent-e1], [Software licence][k0rdent-e3], [Mirantis enterprise boundary][k0rdent-e6] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted | [Scope and architecture][k0rdent-e1] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][k0rdent-e3], [Mirantis enterprise boundary][k0rdent-e6] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Software licence][k0rdent-e3], [Mirantis enterprise boundary][k0rdent-e6] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Software licence][k0rdent-e3], [Mirantis enterprise boundary][k0rdent-e6] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | growing | [Current KCM release][k0rdent-e4], [Scope and architecture][k0rdent-e1] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Current KCM release][k0rdent-e4], [Scope and architecture][k0rdent-e1] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Project umbrella][k0rdent-e2] | GitHub API reports archived=false for the retained repository; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Scope and architecture][k0rdent-e1] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Scope and architecture][k0rdent-e1] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Scope and architecture][k0rdent-e1], [Project umbrella][k0rdent-e2], [Software licence][k0rdent-e3], [Current KCM release][k0rdent-e4], [Community governance][k0rdent-e5], [Mirantis enterprise boundary][k0rdent-e6] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:6_Security/README.md#L29<br>legacy:devopstools_final.md#L871 | legacy:6_Security/README.md#L29<br>legacy:devopstools_final.md#L871<br>https://docs.k0rdent.io/latest/<br>https://github.com/k0rdent/k0rdent<br>https://github.com/k0rdent/k0rdent/blob/main/LICENSE<br>https://github.com/k0rdent/kcm/releases/tag/v1.12.0<br>https://github.com/k0rdent/community/blob/main/GOVERNANCE.md<br>https://docs.mirantis.com/k0rdent-enterprise/latest/release-notes/release-notes-v1.4.1/ | [Scope and architecture][k0rdent-e1], [Project umbrella][k0rdent-e2], [Software licence][k0rdent-e3], [Current KCM release][k0rdent-e4], [Community governance][k0rdent-e5], [Mirantis enterprise boundary][k0rdent-e6] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Current KCM release][k0rdent-e4], [Scope and architecture][k0rdent-e1] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `categories`, `subcategories`, `roles`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[k0rdent-e1]: https://docs.k0rdent.io/latest/
[k0rdent-e2]: https://github.com/k0rdent/k0rdent
[k0rdent-e3]: https://github.com/k0rdent/k0rdent/blob/main/LICENSE
[k0rdent-e4]: https://github.com/k0rdent/kcm/releases/tag/v1.12.0
[k0rdent-e5]: https://github.com/k0rdent/community/blob/main/GOVERNANCE.md
[k0rdent-e6]: https://docs.mirantis.com/k0rdent-enterprise/latest/release-notes/release-notes-v1.4.1/

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/k0rdent/k0rdent) (`archived: false`).

### nexus-repository

**Identity boundary:** Family record includes Core, self-hosted CE/Pro and managed Cloud. Core supports a narrower set of formats and deployment capabilities than CE.

**Licence boundary:** Retain open-core as a family-level classification: public Core is EPL-1.0, while CE binaries are governed by an internal-use EULA and Pro is commercially licensed. No product-wide SPDX is assigned.

**Lifecycle boundary:** Current documentation and 2026 releases support active status; Core 3.96.4-01 was released on 2026-09-30.

**Repository boundary:** sonatype/nexus-public is the canonical public Core source mirror, not the complete CE/Pro/Cloud distribution. GitHub API archived=false.

**Maturity:** Established is an editorial judgement supported by sustained release history, operational documentation, and explicit enterprise support/HA/replication facilities.

**Unresolved questions / limits:** None blocking the scoped record. Edition entitlements and future releases remain subject to their own current documentation.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Product family][nexus-repository-e1], [Core versus CE and Pro][nexus-repository-e2], [Core licence][nexus-repository-e3], [Community distribution EULA][nexus-repository-e4], [Product documentation][nexus-repository-e5], [Edition feature matrix][nexus-repository-e6], [Core release history][nexus-repository-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | nexus-repository | nexus-repository | [Core versus CE and Pro][nexus-repository-e2], [Product documentation][nexus-repository-e5] | Preserve stable catalogue identity and history. |
| `name` | Nexus Repository | Nexus Repository | [Product documentation][nexus-repository-e5] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Universal artifact repository manager. | Sonatype artifact repository family with open-source Core, separately licensed Community and Professional editions, and managed Cloud hosting. | [Product documentation][nexus-repository-e5] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://www.sonatype.com/products/sonatype-nexus-repository | https://www.sonatype.com/products/sonatype-nexus-repository | [Core versus CE and Pro][nexus-repository-e2], [Product documentation][nexus-repository-e5] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/sonatype/nexus-public | https://github.com/sonatype/nexus-public | [Core versus CE and Pro][nexus-repository-e2], [Core licence][nexus-repository-e3], [Community distribution EULA][nexus-repository-e4] | Keep the canonical project/core pointer with its explicit boundary. |
| `documentation_url` | *absent* | https://help.sonatype.com/en/sonatype-nexus-repository.html | [Product documentation][nexus-repository-e5] | Add the directly identified official documentation entry point. |
| `categories` | artifact-package-management | artifact-package-management | [Product documentation][nexus-repository-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Artifact Management | Artifact Management | [Product documentation][nexus-repository-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>devsecops-engineer<br>release-engineer | devops-engineer<br>devsecops-engineer<br>release-engineer | [Product documentation][nexus-repository-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | build<br>release | build<br>release | [Product documentation][nexus-repository-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | * You need a self-hosted, multi-format artifact repository (especially strong for Java/Maven). | You need centralized storage and proxying of build artifacts, with self-hosted or managed Cloud deployment and edition-specific format support. | [Product documentation][nexus-repository-e5], [Product family][nexus-repository-e1], [Core licence][nexus-repository-e3], [Community distribution EULA][nexus-repository-e4] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | * You need advanced HA or replication features only in the Pro tier and can&#x27;t justify the cost. | You require unrestricted redistribution of the Community distribution, or enterprise HA and replication without a Professional licence. | [Product documentation][nexus-repository-e5], [Product family][nexus-repository-e1], [Core licence][nexus-repository-e3], [Community distribution EULA][nexus-repository-e4] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted<br>hosted-saas | [Product family][nexus-repository-e1], [Product documentation][nexus-repository-e5] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | open-core | open-core | [Core licence][nexus-repository-e3], [Community distribution EULA][nexus-repository-e4] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | *absent* | [Core licence][nexus-repository-e3], [Community distribution EULA][nexus-repository-e4] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Core licence][nexus-repository-e3], [Community distribution EULA][nexus-repository-e4], [Core versus CE and Pro][nexus-repository-e2] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [Core release history][nexus-repository-e7], [Product documentation][nexus-repository-e5] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Core release history][nexus-repository-e7], [Product documentation][nexus-repository-e5] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Core versus CE and Pro][nexus-repository-e2] | GitHub API reports archived=false for the retained repository; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Product documentation][nexus-repository-e5] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Product documentation][nexus-repository-e5] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Product family][nexus-repository-e1], [Core versus CE and Pro][nexus-repository-e2], [Core licence][nexus-repository-e3], [Community distribution EULA][nexus-repository-e4], [Product documentation][nexus-repository-e5], [Edition feature matrix][nexus-repository-e6], [Core release history][nexus-repository-e7] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:3_CI-CD-Automation/README.md#L124<br>legacy:devopstools_final.md#L379 | legacy:3_CI-CD-Automation/README.md#L124<br>legacy:devopstools_final.md#L379<br>https://www.sonatype.com/products/sonatype-nexus-repository<br>https://github.com/sonatype/nexus-public<br>https://github.com/sonatype/nexus-public/blob/main/LICENSE.txt<br>https://www.sonatype.com/dnt/usage/community-edition-eula<br>https://help.sonatype.com/en/sonatype-nexus-repository.html<br>https://help.sonatype.com/en/nexus-repository-feature-matrix.html<br>https://github.com/sonatype/nexus-public/releases | [Product family][nexus-repository-e1], [Core versus CE and Pro][nexus-repository-e2], [Core licence][nexus-repository-e3], [Community distribution EULA][nexus-repository-e4], [Product documentation][nexus-repository-e5], [Edition feature matrix][nexus-repository-e6], [Core release history][nexus-repository-e7] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Core release history][nexus-repository-e7], [Product documentation][nexus-repository-e5] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[nexus-repository-e1]: https://www.sonatype.com/products/sonatype-nexus-repository
[nexus-repository-e2]: https://github.com/sonatype/nexus-public
[nexus-repository-e3]: https://github.com/sonatype/nexus-public/blob/main/LICENSE.txt
[nexus-repository-e4]: https://www.sonatype.com/dnt/usage/community-edition-eula
[nexus-repository-e5]: https://help.sonatype.com/en/sonatype-nexus-repository.html
[nexus-repository-e6]: https://help.sonatype.com/en/nexus-repository-feature-matrix.html
[nexus-repository-e7]: https://github.com/sonatype/nexus-public/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/sonatype/nexus-public) (`archived: false`).

### teamcity

**Identity boundary:** JetBrains parent CI/CD product spans Cloud hosted services and the On-Premises server; downloadable agents are not a separate open-source parent.

**Licence boundary:** Professional is free within limits and Enterprise is paid, under the same proprietary On-Premises agreement. Cloud has free/paid subscription terms. The Open Source edition grants use to eligible projects; it does not publish the server under an OSS licence.

**Lifecycle boundary:** Current 2026.2 documentation and maintained licensing/support policies establish active operation; the configuration-as-code avoidance claim is removed.

**Repository boundary:** No verified public repository represents the full TeamCity server/Cloud product; repository_url, repository_archived and license_spdx remain absent.

**Maturity:** Established is a judgement grounded in long-running server editions, documented agent/HA operations and maintained current release documentation.

**Unresolved questions / limits:** None blocking the scoped record. Edition entitlements and future releases remain subject to their own current documentation.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Parent product][teamcity-e1], [On-Premises agreement][teamcity-e2], [Professional and Enterprise policy][teamcity-e3], [On-Premises documentation][teamcity-e4], [Cloud agreement][teamcity-e5], [Cloud documentation][teamcity-e6], [Kotlin configuration][teamcity-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | teamcity | teamcity | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6] | Preserve stable catalogue identity and history. |
| `name` | TeamCity | TeamCity | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | CI/CD server by JetBrains. | JetBrains commercial CI/CD product offered as TeamCity On-Premises and TeamCity Cloud. | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://www.jetbrains.com/teamcity | https://www.jetbrains.com/teamcity | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | *absent* | *absent* | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6], [On-Premises agreement][teamcity-e2], [Cloud agreement][teamcity-e5] | Leave absent: no public full parent-product source repository established; components are not substituted. |
| `documentation_url` | *absent* | https://www.jetbrains.com/help/teamcity/teamcity-documentation.html | [On-Premises documentation][teamcity-e4] | Add the directly identified official documentation entry point. |
| `categories` | ci-build-testing | ci-build-testing | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | CI/CD Platforms | CI/CD Platforms | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>developer-experience-engineer<br>release-engineer | devops-engineer<br>developer-experience-engineer<br>release-engineer | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | build<br>test | build<br>test | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | * You use JetBrains IDEs and want deep integration with excellent build configuration UI. | You need managed or self-hosted CI with build agents, a graphical configuration interface, and Kotlin configuration as code. | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6], [On-Premises agreement][teamcity-e2], [Cloud agreement][teamcity-e5] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | * You prefer pipeline-as-code or need a large open-source plugin ecosystem. | You require an open-source CI server or unrestricted use beyond the free Professional or Cloud subscription limits. | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6], [On-Premises agreement][teamcity-e2], [Cloud agreement][teamcity-e5] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted<br>hosted-saas | [On-Premises agreement][teamcity-e2], [On-Premises documentation][teamcity-e4], [Cloud agreement][teamcity-e5], [Cloud documentation][teamcity-e6] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | unknown | commercial | [On-Premises agreement][teamcity-e2], [Cloud agreement][teamcity-e5] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | *absent* | [On-Premises agreement][teamcity-e2], [Cloud agreement][teamcity-e5] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [On-Premises agreement][teamcity-e2], [Cloud agreement][teamcity-e5], [Parent product][teamcity-e1] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | *absent* | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6], [On-Premises agreement][teamcity-e2], [Cloud agreement][teamcity-e5], [Parent product][teamcity-e1] | Leave absent with the absent parent repository; do not invent an archival boolean. |
| `alternatives` | `[]` | `[]` | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Parent product][teamcity-e1], [On-Premises agreement][teamcity-e2], [Professional and Enterprise policy][teamcity-e3], [On-Premises documentation][teamcity-e4], [Cloud agreement][teamcity-e5], [Cloud documentation][teamcity-e6], [Kotlin configuration][teamcity-e7] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:3_CI-CD-Automation/README.md#L62<br>legacy:devopstools_final.md#L340 | legacy:3_CI-CD-Automation/README.md#L62<br>legacy:devopstools_final.md#L340<br>https://www.jetbrains.com/teamcity<br>https://www.jetbrains.com/legal/docs/teamcity/license/<br>https://www.jetbrains.com/help/teamcity/licensing-policy.html<br>https://www.jetbrains.com/help/teamcity/teamcity-documentation.html<br>https://www.jetbrains.com/legal/docs/teamcity/teamcity_cloud/<br>https://www.jetbrains.com/help/teamcity/cloud/teamcity-cloud-documentation.html<br>https://www.jetbrains.com/help/teamcity/kotlin-dsl.html | [Parent product][teamcity-e1], [On-Premises agreement][teamcity-e2], [Professional and Enterprise policy][teamcity-e3], [On-Premises documentation][teamcity-e4], [Cloud agreement][teamcity-e5], [Cloud documentation][teamcity-e6], [Kotlin configuration][teamcity-e7] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [On-Premises documentation][teamcity-e4], [Cloud documentation][teamcity-e6] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_model`, `commercial_offering`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`.

[teamcity-e1]: https://www.jetbrains.com/teamcity
[teamcity-e2]: https://www.jetbrains.com/legal/docs/teamcity/license/
[teamcity-e3]: https://www.jetbrains.com/help/teamcity/licensing-policy.html
[teamcity-e4]: https://www.jetbrains.com/help/teamcity/teamcity-documentation.html
[teamcity-e5]: https://www.jetbrains.com/legal/docs/teamcity/teamcity_cloud/
[teamcity-e6]: https://www.jetbrains.com/help/teamcity/cloud/teamcity-cloud-documentation.html
[teamcity-e7]: https://www.jetbrains.com/help/teamcity/kotlin-dsl.html

### spacelift

**Identity boundary:** The IaC product was renamed Spacelift Deploy; self-hosted installs retain Spacelift. Spacelift Flows is a separate product and is outside this record.

**Licence boundary:** Vendor terms grant limited subscription access/use and self-hosted licence keys. Public SDK/provider/CLI licences are not the control-plane licence; no SPDX or parent repository is asserted.

**Lifecycle boundary:** Active changelog includes September 2026 updates. Lifecycle covers planning, applying and maintaining infrastructure, rather than compiling application code.

**Repository boundary:** Workers run IaC in vendor or customer infrastructure; private workers do not move the SaaS control plane. Full self-hosted deployment is independently documented.

**Maturity:** Established is a reviewer judgement based on mature policy/RBAC/state/worker documentation, continued release history, and supported full self-hosted deployments.

**Unresolved questions / limits:** None blocking the scoped record. Edition entitlements and future releases remain subject to their own current documentation.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Deploy identity and engine scope][spacelift-e1], [Control-plane legal terms][spacelift-e2], [Worker boundary][spacelift-e3], [Full self-hosted deployment][spacelift-e4], [Edition structure][spacelift-e5], [Maintained product history][spacelift-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | spacelift | spacelift | [Deploy identity and engine scope][spacelift-e1] | Preserve stable catalogue identity and history. |
| `name` | Spacelift | Spacelift Deploy | [Deploy identity and engine scope][spacelift-e1] | Changed: documented identity/capability; scoped boundary above applies. |
| `summary` | IaC automation with policy-as-code and collaboration. | Commercial infrastructure-as-code orchestration control plane with worker pools and Open Policy Agent governance, available as SaaS or self-hosted Spacelift. | [Deploy identity and engine scope][spacelift-e1] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://spacelift.io | https://spacelift.io | [Deploy identity and engine scope][spacelift-e1] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | *absent* | *absent* | [Deploy identity and engine scope][spacelift-e1], [Control-plane legal terms][spacelift-e2] | Leave absent: no public full parent-product source repository established; components are not substituted. |
| `documentation_url` | *absent* | https://docs.spacelift.io/ | [Deploy identity and engine scope][spacelift-e1] | Add the directly identified official documentation entry point. |
| `categories` | infrastructure-as-code | infrastructure-as-code | [Deploy identity and engine scope][spacelift-e1] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Collaborative Infrastructure<br>Infrastructure as Code (IaC) | Infrastructure as Code (IaC)<br>IaC Orchestration and Policy | [Deploy identity and engine scope][spacelift-e1] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | [Deploy identity and engine scope][spacelift-e1] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | plan<br>build<br>deploy | plan<br>deploy<br>operate | [Deploy identity and engine scope][spacelift-e1] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You need enterprise-grade IaC orchestration with drift detection and policies.<br>You need enterprise-grade IaC orchestration with multi-tool support (Terraform, Pulumi, CloudFormation). | You need governed IaC workflows for OpenTofu/Terraform, Terragrunt, Pulumi, CloudFormation, Kubernetes or Ansible, with Rego policies and public or private workers. | [Deploy identity and engine scope][spacelift-e1], [Control-plane legal terms][spacelift-e2], [Worker boundary][spacelift-e3], [Full self-hosted deployment][spacelift-e4] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | Budget is limited and simpler tooling covers your workflow.<br>Budget is tight and Atlantis or native CI covers your needs. | You only need a simple CI job, or assume private workers make the SaaS control plane self-hosted; a full self-hosted installation is a separate deployment. | [Deploy identity and engine scope][spacelift-e1], [Control-plane legal terms][spacelift-e2], [Worker boundary][spacelift-e3], [Full self-hosted deployment][spacelift-e4] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | hosted-saas<br>self-hosted | [Deploy identity and engine scope][spacelift-e1], [Control-plane legal terms][spacelift-e2], [Worker boundary][spacelift-e3], [Full self-hosted deployment][spacelift-e4] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | unknown | commercial | [Control-plane legal terms][spacelift-e2] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | *absent* | [Control-plane legal terms][spacelift-e2] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Control-plane legal terms][spacelift-e2] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [Maintained product history][spacelift-e6], [Deploy identity and engine scope][spacelift-e1] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Maintained product history][spacelift-e6], [Deploy identity and engine scope][spacelift-e1] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | *absent* | [Deploy identity and engine scope][spacelift-e1], [Control-plane legal terms][spacelift-e2] | Leave absent with the absent parent repository; do not invent an archival boolean. |
| `alternatives` | `[]` | `[]` | [Deploy identity and engine scope][spacelift-e1] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Deploy identity and engine scope][spacelift-e1] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Deploy identity and engine scope][spacelift-e1], [Control-plane legal terms][spacelift-e2], [Worker boundary][spacelift-e3], [Full self-hosted deployment][spacelift-e4], [Edition structure][spacelift-e5], [Maintained product history][spacelift-e6] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:2_Cloud-Infrastructure-Serverless/README.md#L122<br>legacy:2_Cloud-Infrastructure-Serverless/README.md#L58<br>legacy:devopstools_final.md#L184<br>legacy:devopstools_final.md#L223 | legacy:2_Cloud-Infrastructure-Serverless/README.md#L122<br>legacy:2_Cloud-Infrastructure-Serverless/README.md#L58<br>legacy:devopstools_final.md#L184<br>legacy:devopstools_final.md#L223<br>https://docs.spacelift.io/<br>https://docs.spacelift.io/legal/terms<br>https://docs.spacelift.io/concepts/worker-pools<br>https://docs.spacelift.io/self-hosted<br>https://spacelift.io/pricing<br>https://docs.spacelift.io/product/changelog | [Deploy identity and engine scope][spacelift-e1], [Control-plane legal terms][spacelift-e2], [Worker boundary][spacelift-e3], [Full self-hosted deployment][spacelift-e4], [Edition structure][spacelift-e5], [Maintained product history][spacelift-e6] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Maintained product history][spacelift-e6], [Deploy identity and engine scope][spacelift-e1] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `name`, `summary`, `documentation_url`, `subcategories`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_model`, `commercial_offering`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`.

[spacelift-e1]: https://docs.spacelift.io/
[spacelift-e2]: https://docs.spacelift.io/legal/terms
[spacelift-e3]: https://docs.spacelift.io/concepts/worker-pools
[spacelift-e4]: https://docs.spacelift.io/self-hosted
[spacelift-e5]: https://spacelift.io/pricing
[spacelift-e6]: https://docs.spacelift.io/product/changelog

### cloudbees

**Identity boundary:** Stable ID cloudbees now explicitly represents CloudBees CI, part of Software Delivery Automation. Unify and CD/RO are separate products; Jenkins is the underlying open-source project.

**Licence boundary:** Commercial subscription product with proprietary additions and required trial/standard licence. Jenkins MIT does not license the CloudBees CI distribution; no product-wide SPDX or Jenkins repository is assigned.

**Lifecycle boundary:** Active monthly stable releases and current product documentation; self-hosted traditional and Kubernetes deployments do not imply a hosted SaaS CI service.

**Repository boundary:** No public repository for the complete CloudBees CI product was established. Official URL uses its product-specific documentation landing page because current marketing CI URLs broaden to portfolio workflows.

**Maturity:** Established is a judgement based on documented monthly stable releases and mature controller/plugin/support operations.

**Unresolved questions / limits:** None blocking the scoped record. Edition entitlements and future releases remain subject to their own current documentation.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Product-specific documentation][cloudbees-e1], [Jenkins and proprietary feature boundary][cloudbees-e2], [Subscription licence][cloudbees-e3], [Current CI release history][cloudbees-e4].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | cloudbees | cloudbees | [Product-specific documentation][cloudbees-e1] | Preserve stable catalogue identity and history. |
| `name` | CloudBees | CloudBees CI | [Product-specific documentation][cloudbees-e1] | Changed: documented identity/capability; scoped boundary above applies. |
| `summary` | Enterprise CI/CD built around Jenkins. | Commercial Jenkins-based continuous integration product with proprietary controller management, governance and enterprise support. | [Product-specific documentation][cloudbees-e1] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://www.cloudbees.com | https://docs.cloudbees.com/docs/cloudbees-ci/latest/ | [Product-specific documentation][cloudbees-e1] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | *absent* | *absent* | [Product-specific documentation][cloudbees-e1], [Jenkins and proprietary feature boundary][cloudbees-e2], [Subscription licence][cloudbees-e3] | Leave absent: no public full parent-product source repository established; components are not substituted. |
| `documentation_url` | *absent* | https://docs.cloudbees.com/docs/cloudbees-ci/latest/ | [Product-specific documentation][cloudbees-e1] | Add the directly identified official documentation entry point. |
| `categories` | ci-build-testing | ci-build-testing | [Product-specific documentation][cloudbees-e1] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | CI/CD Platforms | Enterprise Continuous Integration | [Product-specific documentation][cloudbees-e1] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>developer-experience-engineer<br>release-engineer | devops-engineer<br>developer-experience-engineer<br>release-engineer | [Product-specific documentation][cloudbees-e1] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | build<br>test | build<br>test | [Product-specific documentation][cloudbees-e1] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | * You need enterprise Jenkins with governance, RBAC, and support. | You need enterprise governance, supported plugins and centralized management of Jenkins controllers on Kubernetes or traditional infrastructure. | [Product-specific documentation][cloudbees-e1], [Jenkins and proprietary feature boundary][cloudbees-e2], [Subscription licence][cloudbees-e3] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | * You want to avoid Jenkins complexity or vendor lock-in. | You need the open-source Jenkins licence for the entire product, or are selecting CloudBees Unify or CD/RO rather than CloudBees CI. | [Product-specific documentation][cloudbees-e1], [Jenkins and proprietary feature boundary][cloudbees-e2], [Subscription licence][cloudbees-e3] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted | [Product-specific documentation][cloudbees-e1] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | open-core | commercial | [Jenkins and proprietary feature boundary][cloudbees-e2], [Subscription licence][cloudbees-e3] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | *absent* | [Jenkins and proprietary feature boundary][cloudbees-e2], [Subscription licence][cloudbees-e3] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Jenkins and proprietary feature boundary][cloudbees-e2], [Subscription licence][cloudbees-e3] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [Current CI release history][cloudbees-e4], [Product-specific documentation][cloudbees-e1] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Current CI release history][cloudbees-e4], [Product-specific documentation][cloudbees-e1] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | *absent* | [Product-specific documentation][cloudbees-e1], [Jenkins and proprietary feature boundary][cloudbees-e2], [Subscription licence][cloudbees-e3] | Leave absent with the absent parent repository; do not invent an archival boolean. |
| `alternatives` | `[]` | `[]` | [Product-specific documentation][cloudbees-e1] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Product-specific documentation][cloudbees-e1] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Product-specific documentation][cloudbees-e1], [Jenkins and proprietary feature boundary][cloudbees-e2], [Subscription licence][cloudbees-e3], [Current CI release history][cloudbees-e4] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:3_CI-CD-Automation/README.md#L24<br>legacy:devopstools_final.md#L318 | legacy:3_CI-CD-Automation/README.md#L24<br>legacy:devopstools_final.md#L318<br>https://docs.cloudbees.com/docs/cloudbees-ci/latest/<br>https://docs.cloudbees.com/docs/cloudbees-ci/latest/traditional-onboarding<br>https://docs.cloudbees.com/docs/cloudbees-common/latest/subscription-agreement/<br>https://docs.cloudbees.com/docs/release-notes/latest/cloudbees-ci/ | [Product-specific documentation][cloudbees-e1], [Jenkins and proprietary feature boundary][cloudbees-e2], [Subscription licence][cloudbees-e3], [Current CI release history][cloudbees-e4] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Current CI release history][cloudbees-e4], [Product-specific documentation][cloudbees-e1] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `name`, `summary`, `official_url`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_model`, `commercial_offering`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`.

[cloudbees-e1]: https://docs.cloudbees.com/docs/cloudbees-ci/latest/
[cloudbees-e2]: https://docs.cloudbees.com/docs/cloudbees-ci/latest/traditional-onboarding
[cloudbees-e3]: https://docs.cloudbees.com/docs/cloudbees-common/latest/subscription-agreement/
[cloudbees-e4]: https://docs.cloudbees.com/docs/release-notes/latest/cloudbees-ci/

### helm

**Identity boundary:** Kubernetes package/release manager; the existing Kubernetes ecosystem/addons classification is appropriate to chart deployment and is retained.

**Licence boundary:** Apache-2.0 licenses Helm software; the documentation footer CC-BY-4.0 is not substituted for it. Third-party charts have their own licences.

**Lifecycle boundary:** Active stable v4 line (v4.3.0 reviewed). The June 2026 notice supersedes the older v4 announcement: v3 feature work ended September 2026, security support extends to 2027-02-10. v3 support state is not parent-project deprecation.

**Repository boundary:** Keep helm/helm; GitHub API archived=false. Helm runs as a local/CI CLI against clusters, not as a hosted vendor control plane.

**Maturity:** Established is supported by CNCF graduation, maintained major-version migration/support policies and sustained release history.

**Unresolved questions / limits:** None blocking. No project-wide commercial_offering boolean is asserted; this review does not survey all third-party chart/support businesses.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Current documentation and CNCF status][helm-e1], [Canonical software repository][helm-e2], [Software licence][helm-e3], [Stable releases][helm-e4], [v4 release][helm-e5], [Updated v3 support notice][helm-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | helm | helm | [Canonical software repository][helm-e2], [Current documentation and CNCF status][helm-e1] | Preserve stable catalogue identity and history. |
| `name` | Helm | Helm | [Current documentation and CNCF status][helm-e1] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Kubernetes package manager. | Kubernetes package manager. | [Current documentation and CNCF status][helm-e1] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://helm.sh | https://helm.sh | [Canonical software repository][helm-e2], [Current documentation and CNCF status][helm-e1] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/helm/helm | https://github.com/helm/helm | [Canonical software repository][helm-e2], [Software licence][helm-e3] | Keep the canonical project/core pointer with its explicit boundary. |
| `documentation_url` | *absent* | https://helm.sh/docs/ | [Current documentation and CNCF status][helm-e1] | Add the directly identified official documentation entry point. |
| `categories` | kubernetes-networking-storage-addons | kubernetes-networking-storage-addons | [Current documentation and CNCF status][helm-e1] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Kubernetes Ecosystem &amp; Add-ons | Kubernetes Ecosystem &amp; Add-ons | [Current documentation and CNCF status][helm-e1] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Current documentation and CNCF status][helm-e1] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Current documentation and CNCF status][helm-e1] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You need templated, versioned, reusable Kubernetes application packages. | You need reusable, versioned Kubernetes charts with installation, upgrades and rollback through Helm. | [Current documentation and CNCF status][helm-e1], [Software licence][helm-e3] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | Simple apps with static manifests work fine with Kustomize or plain kubectl. | Your application only needs a few static manifests and chart templating or release management adds unnecessary complexity. | [Current documentation and CNCF status][helm-e1], [Software licence][helm-e3] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | local | [Current documentation and CNCF status][helm-e1] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][helm-e3] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Software licence][helm-e3] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Software licence][helm-e3] | Leave optional field absent; no blanket assertion about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Stable releases][helm-e4], [v4 release][helm-e5], [Updated v3 support notice][helm-e6], [Current documentation and CNCF status][helm-e1] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Stable releases][helm-e4], [v4 release][helm-e5], [Updated v3 support notice][helm-e6], [Current documentation and CNCF status][helm-e1] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical software repository][helm-e2] | GitHub API reports archived=false for the retained repository; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Current documentation and CNCF status][helm-e1] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Current documentation and CNCF status][helm-e1] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Current documentation and CNCF status][helm-e1], [Canonical software repository][helm-e2], [Software licence][helm-e3], [Stable releases][helm-e4], [v4 release][helm-e5], [Updated v3 support notice][helm-e6] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L91<br>legacy:devopstools_final.md#L563 | legacy:4_Kubernetes-Containers/README.md#L91<br>legacy:devopstools_final.md#L563<br>https://helm.sh/docs/<br>https://github.com/helm/helm<br>https://github.com/helm/helm/blob/main/LICENSE<br>https://github.com/helm/helm/releases<br>https://helm.sh/blog/helm-4-released/<br>https://helm.sh/blog/helm-v3-end-of-life/ | [Current documentation and CNCF status][helm-e1], [Canonical software repository][helm-e2], [Software licence][helm-e3], [Stable releases][helm-e4], [v4 release][helm-e5], [Updated v3 support notice][helm-e6] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Stable releases][helm-e4], [v4 release][helm-e5], [Updated v3 support notice][helm-e6], [Current documentation and CNCF status][helm-e1] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[helm-e1]: https://helm.sh/docs/
[helm-e2]: https://github.com/helm/helm
[helm-e3]: https://github.com/helm/helm/blob/main/LICENSE
[helm-e4]: https://github.com/helm/helm/releases
[helm-e5]: https://helm.sh/blog/helm-4-released/
[helm-e6]: https://helm.sh/blog/helm-v3-end-of-life/

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/helm/helm) (`archived: false`).

### tekton

**Identity boundary:** Framework/ecosystem record, with Pipelines as its execution core. Triggers, CLI, Catalog and supply-chain components are complementary, not all contained in the Pipelines repository.

**Licence boundary:** Apache-2.0 is directly evidenced for Pipelines, CLI, Triggers and Chains through their complete upstream licence files. External catalog tasks, integrations and vendor distributions require their own licence review.

**Lifecycle boundary:** Current foundation is CNCF Incubating, accepted 2026-03-13; former CDF graduation is historical. Pipelines stable v1.17.0 (2026-10-01) and ongoing LTS releases support active status.

**Repository boundary:** Keep tektoncd/pipeline as the canonical core source pointer and explicitly document the broader ecosystem boundary. GitHub API archived=false.

**Maturity:** Established is a catalogue judgement based on stable core APIs, LTS release history and documented production ecosystem adoption; it is not a claim of CNCF graduation.

**Unresolved questions / limits:** None blocking this first-party framework/core boundary. No blanket licence or commercial-offering claim is made for external tasks/vendor products.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Ecosystem documentation][tekton-e1], [Core Pipelines repository][tekton-e2], [Core software licence][tekton-e3], [CLI software licence][tekton-e4], [Triggers software licence][tekton-e5], [Chains software licence][tekton-e6], [Core release history][tekton-e7], [Current foundation status][tekton-e8], [CDF to CNCF transition][tekton-e9].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | tekton | tekton | [Core Pipelines repository][tekton-e2], [Ecosystem documentation][tekton-e1] | Preserve stable catalogue identity and history. |
| `name` | Tekton | Tekton | [Ecosystem documentation][tekton-e1] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Kubernetes-native CI/CD framework. | Kubernetes-native CI/CD framework and ecosystem built around Tekton Pipelines, with complementary triggers, tooling and supply-chain components. | [Ecosystem documentation][tekton-e1] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://tekton.dev | https://tekton.dev | [Core Pipelines repository][tekton-e2], [Ecosystem documentation][tekton-e1] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/tektoncd/pipeline | https://github.com/tektoncd/pipeline | [Core Pipelines repository][tekton-e2], [Core software licence][tekton-e3], [CLI software licence][tekton-e4], [Triggers software licence][tekton-e5], [Chains software licence][tekton-e6] | Keep the canonical project/core pointer with its explicit boundary. |
| `documentation_url` | *absent* | https://tekton.dev/docs/ | [Ecosystem documentation][tekton-e1] | Add the directly identified official documentation entry point. |
| `categories` | ci-build-testing | ci-build-testing<br>cd-gitops-release-promotion | [Ecosystem documentation][tekton-e1] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | CI/CD Platforms | Kubernetes-native CI/CD | [Ecosystem documentation][tekton-e1] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>developer-experience-engineer<br>release-engineer | devops-engineer<br>developer-experience-engineer<br>release-engineer<br>platform-engineer<br>kubernetes-engineer | [Ecosystem documentation][tekton-e1] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | build<br>test | build<br>test<br>release<br>deploy | [Ecosystem documentation][tekton-e1] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | * You want a composable, Kubernetes-native CI/CD building block. | You operate Kubernetes and need composable CI/CD tasks and pipelines, adding other Tekton components where required. | [Ecosystem documentation][tekton-e1], [Core software licence][tekton-e3], [CLI software licence][tekton-e4], [Triggers software licence][tekton-e5], [Chains software licence][tekton-e6] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | * You don&#x27;t run Kubernetes or want a batteries-included CI/CD experience. | You do not operate Kubernetes or need a complete managed CI service without assembling and maintaining pipeline components. | [Ecosystem documentation][tekton-e1], [Core software licence][tekton-e3], [CLI software licence][tekton-e4], [Triggers software licence][tekton-e5], [Chains software licence][tekton-e6] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted | [Ecosystem documentation][tekton-e1] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Core software licence][tekton-e3], [CLI software licence][tekton-e4], [Triggers software licence][tekton-e5], [Chains software licence][tekton-e6] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Core software licence][tekton-e3], [CLI software licence][tekton-e4], [Triggers software licence][tekton-e5], [Chains software licence][tekton-e6] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Core software licence][tekton-e3], [CLI software licence][tekton-e4], [Triggers software licence][tekton-e5], [Chains software licence][tekton-e6] | Leave optional field absent; no blanket assertion about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Core release history][tekton-e7], [Current foundation status][tekton-e8], [CDF to CNCF transition][tekton-e9], [Ecosystem documentation][tekton-e1] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Core release history][tekton-e7], [Current foundation status][tekton-e8], [CDF to CNCF transition][tekton-e9], [Ecosystem documentation][tekton-e1] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Core Pipelines repository][tekton-e2] | GitHub API reports archived=false for the retained repository; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Ecosystem documentation][tekton-e1] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Ecosystem documentation][tekton-e1] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Ecosystem documentation][tekton-e1], [Core Pipelines repository][tekton-e2], [Core software licence][tekton-e3], [CLI software licence][tekton-e4], [Triggers software licence][tekton-e5], [Chains software licence][tekton-e6], [Core release history][tekton-e7], [Current foundation status][tekton-e8], [CDF to CNCF transition][tekton-e9] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:3_CI-CD-Automation/README.md#L64<br>legacy:devopstools_final.md#L341 | legacy:3_CI-CD-Automation/README.md#L64<br>legacy:devopstools_final.md#L341<br>https://tekton.dev/docs/<br>https://github.com/tektoncd/pipeline<br>https://github.com/tektoncd/pipeline/blob/main/LICENSE<br>https://github.com/tektoncd/cli/blob/main/LICENSE<br>https://github.com/tektoncd/triggers/blob/main/LICENSE<br>https://github.com/tektoncd/chains/blob/main/LICENSE<br>https://github.com/tektoncd/pipeline/releases<br>https://www.cncf.io/projects/tekton/<br>https://tekton.dev/blog/2026/03/25/tekton-joins-the-cncf-as-an-incubating-project/ | [Ecosystem documentation][tekton-e1], [Core Pipelines repository][tekton-e2], [Core software licence][tekton-e3], [CLI software licence][tekton-e4], [Triggers software licence][tekton-e5], [Chains software licence][tekton-e6], [Core release history][tekton-e7], [Current foundation status][tekton-e8], [CDF to CNCF transition][tekton-e9] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Core release history][tekton-e7], [Current foundation status][tekton-e8], [CDF to CNCF transition][tekton-e9], [Ecosystem documentation][tekton-e1] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `categories`, `subcategories`, `roles`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[tekton-e1]: https://tekton.dev/docs/
[tekton-e2]: https://github.com/tektoncd/pipeline
[tekton-e3]: https://github.com/tektoncd/pipeline/blob/main/LICENSE
[tekton-e4]: https://github.com/tektoncd/cli/blob/main/LICENSE
[tekton-e5]: https://github.com/tektoncd/triggers/blob/main/LICENSE
[tekton-e6]: https://github.com/tektoncd/chains/blob/main/LICENSE
[tekton-e7]: https://github.com/tektoncd/pipeline/releases
[tekton-e8]: https://www.cncf.io/projects/tekton/
[tekton-e9]: https://tekton.dev/blog/2026/03/25/tekton-joins-the-cncf-as-an-incubating-project/

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/tektoncd/pipeline) (`archived: false`).

Additional first-party licence corroboration: the complete upstream [CLI LICENSE](https://github.com/tektoncd/cli/blob/main/LICENSE), [Triggers LICENSE](https://github.com/tektoncd/triggers/blob/main/LICENSE), and [Chains LICENSE](https://github.com/tektoncd/chains/blob/main/LICENSE) were read through the GitHub contents API and each grants Apache-2.0. This supports the first-party ecosystem boundary without inferring a licence for external catalog tasks or vendor products.

### terragrunt

**Identity boundary:** Gruntwork Terragrunt orchestrates both OpenTofu and Terraform. The upstream README points to terragrunt.com and docs.terragrunt.com, supporting the deliberate official URL update.

**Licence boundary:** MIT applies to Terragrunt, not the separate engines it invokes. Upstream links commercial support and Gruntwork documents separate paid Scale capabilities; commercial_offering=true does not change the CLI OSS licence.

**Lifecycle boundary:** Active stable 1.x with explicit backwards-compatibility guarantee and September 2026 releases. Ordinary OpenTofu/Terraform support is distinguished from experimental engine-plugin APIs.

**Repository boundary:** Keep gruntwork-io/terragrunt; GitHub API archived=false. CLI runs locally or inside CI runners; Scale automation is not conflated with a hosted Terragrunt control plane.

**Maturity:** Established is supported by nearly a decade of development and the explicit 1.x backwards-compatibility commitment.

**Unresolved questions / limits:** None blocking the scoped record. Edition entitlements and future releases remain subject to their own current documentation.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and project website links][terragrunt-e1], [Software licence][terragrunt-e2], [Current project site][terragrunt-e3], [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5], [Stable 1.x and separate Scale offering][terragrunt-e6], [Release history][terragrunt-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | terragrunt | terragrunt | [Canonical repository and project website links][terragrunt-e1], [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5] | Preserve stable catalogue identity and history. |
| `name` | Terragrunt | Terragrunt | [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Terraform wrapper for DRY configurations. | Gruntwork open-source orchestration CLI for scaling OpenTofu and Terraform infrastructure with reusable configuration, units and dependencies. | [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://terragrunt.gruntwork.io | https://terragrunt.com/ | [Canonical repository and project website links][terragrunt-e1], [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/gruntwork-io/terragrunt | https://github.com/gruntwork-io/terragrunt | [Canonical repository and project website links][terragrunt-e1], [Software licence][terragrunt-e2] | Keep the canonical project/core pointer with its explicit boundary. |
| `documentation_url` | *absent* | https://docs.terragrunt.com/ | [Current documentation][terragrunt-e4] | Add the directly identified official documentation entry point. |
| `categories` | infrastructure-as-code | infrastructure-as-code | [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Infrastructure as Code (IaC) | Infrastructure as Code (IaC) | [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | plan<br>build<br>deploy | plan<br>build<br>deploy | [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | You manage many Terraform modules/environments and want to keep configs DRY. | You manage multiple OpenTofu or Terraform units and environments and need reusable configuration, dependency ordering and coordinated runs. | [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5], [Software licence][terragrunt-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | You have a simple, single-environment setup. | You have a simple standalone OpenTofu or Terraform configuration that does not need an additional orchestration layer. | [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5], [Software licence][terragrunt-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | local | [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][terragrunt-e2] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | MIT | [Software licence][terragrunt-e2] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Software licence][terragrunt-e2], [Stable 1.x and separate Scale offering][terragrunt-e6] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `maturity` | unknown | established | [Release history][terragrunt-e7], [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Release history][terragrunt-e7], [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Canonical repository and project website links][terragrunt-e1] | GitHub API reports archived=false for the retained repository; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical repository and project website links][terragrunt-e1], [Software licence][terragrunt-e2], [Current project site][terragrunt-e3], [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5], [Stable 1.x and separate Scale offering][terragrunt-e6], [Release history][terragrunt-e7] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:2_Cloud-Infrastructure-Serverless/README.md#L62<br>legacy:devopstools_final.md#L189 | legacy:2_Cloud-Infrastructure-Serverless/README.md#L62<br>legacy:devopstools_final.md#L189<br>https://github.com/gruntwork-io/terragrunt<br>https://github.com/gruntwork-io/terragrunt/blob/main/LICENSE.txt<br>https://terragrunt.com/<br>https://docs.terragrunt.com/<br>https://docs.terragrunt.com/getting-started/quick-start/<br>https://www.gruntwork.io/blog/terragrunt-1-0-released<br>https://github.com/gruntwork-io/terragrunt/releases | [Canonical repository and project website links][terragrunt-e1], [Software licence][terragrunt-e2], [Current project site][terragrunt-e3], [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5], [Stable 1.x and separate Scale offering][terragrunt-e6], [Release history][terragrunt-e7] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Release history][terragrunt-e7], [Current documentation][terragrunt-e4], [OpenTofu and Terraform quick start][terragrunt-e5] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `official_url`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[terragrunt-e1]: https://github.com/gruntwork-io/terragrunt
[terragrunt-e2]: https://github.com/gruntwork-io/terragrunt/blob/main/LICENSE.txt
[terragrunt-e3]: https://terragrunt.com/
[terragrunt-e4]: https://docs.terragrunt.com/
[terragrunt-e5]: https://docs.terragrunt.com/getting-started/quick-start/
[terragrunt-e6]: https://www.gruntwork.io/blog/terragrunt-1-0-released
[terragrunt-e7]: https://github.com/gruntwork-io/terragrunt/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/gruntwork-io/terragrunt) (`archived: false`).

### cdk8s

**Identity boundary:** CNCF Sandbox project originally built at AWS. Apps generate standard manifests and do not apply them; four supported languages are evidenced by current API references.

**Licence boundary:** Apache-2.0 applies to cdk8s; it is not a licence for arbitrary generated application code, Kubernetes workloads or third-party constructs.

**Lifecycle boundary:** Active 2.x toolchain; 1.x reached EOL on 2025-01-01. Core v2.70.109 released 2026-10-05. Lifecycle deploy is removed because another tool performs deployment.

**Repository boundary:** Keep cdk8s-team/cdk8s as the documented umbrella. cdk8s-core owns the core package/release stream; the umbrella historical releases do not imply inactivity. GitHub API archived=false for both.

**Maturity:** Established is an editorial judgement based on sustained 2.x maintenance since the documented migration and stable language/API tooling; CNCF Sandbox is recorded separately, not inflated to graduation.

**Unresolved questions / limits:** None blocking this synthesis/toolchain boundary. Third-party constructs and any support businesses are outside the record licence/offering claims.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Umbrella identity and synthesis-only scope][cdk8s-e1], [Software licence][cdk8s-e2], [Current 2.x documentation and languages][cdk8s-e3], [1.x to 2.x lifecycle boundary][cdk8s-e4], [Current core library][cdk8s-e5], [Core release history][cdk8s-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | cdk8s | cdk8s | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3] | Preserve stable catalogue identity and history. |
| `name` | cdk8s | cdk8s | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Define Kubernetes applications and reusable abstractions in general-purpose programming languages and synthesize them to YAML. | Open-source framework that synthesizes Kubernetes YAML from TypeScript, Python, Java or Go; deployment is performed by separate tools. | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://cdk8s.io | https://cdk8s.io | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/cdk8s-team/cdk8s | https://github.com/cdk8s-team/cdk8s | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Software licence][cdk8s-e2] | Keep the canonical project/core pointer with its explicit boundary. |
| `documentation_url` | *absent* | https://cdk8s.io/docs/latest/ | [Current 2.x documentation and languages][cdk8s-e3] | Add the directly identified official documentation entry point. |
| `categories` | infrastructure-as-code | infrastructure-as-code | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | Infrastructure as Code (IaC) | Infrastructure as Code (IaC) | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3] | Reviewed; retained: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer<br>infrastructure-systems-engineer | devops-engineer<br>platform-engineer<br>kubernetes-engineer<br>developer-experience-engineer | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | plan<br>build<br>deploy | plan<br>develop<br>build | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | `[]` | You want reusable Kubernetes abstractions in TypeScript, Python, Java or Go and will apply the synthesized manifests with kubectl or a GitOps tool. | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3], [Software licence][cdk8s-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | `[]` | You need a deployment controller rather than manifest synthesis, or plain YAML is sufficient without a programming-language toolchain. | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3], [Software licence][cdk8s-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | local | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][cdk8s-e2] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Software licence][cdk8s-e2] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Software licence][cdk8s-e2] | Leave optional field absent; no blanket assertion about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [1.x to 2.x lifecycle boundary][cdk8s-e4], [Core release history][cdk8s-e6], [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [1.x to 2.x lifecycle boundary][cdk8s-e4], [Core release history][cdk8s-e6], [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Umbrella identity and synthesis-only scope][cdk8s-e1] | GitHub API reports archived=false for the retained repository; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Software licence][cdk8s-e2], [Current 2.x documentation and languages][cdk8s-e3], [1.x to 2.x lifecycle boundary][cdk8s-e4], [Current core library][cdk8s-e5], [Core release history][cdk8s-e6] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:devopstools_final.md#L172 | legacy:devopstools_final.md#L172<br>https://github.com/cdk8s-team/cdk8s<br>https://github.com/cdk8s-team/cdk8s/blob/master/LICENSE<br>https://cdk8s.io/docs/latest/<br>https://cdk8s.io/docs/latest/migrating-from-1.x/<br>https://github.com/cdk8s-team/cdk8s-core<br>https://github.com/cdk8s-team/cdk8s-core/releases | [Umbrella identity and synthesis-only scope][cdk8s-e1], [Software licence][cdk8s-e2], [Current 2.x documentation and languages][cdk8s-e3], [1.x to 2.x lifecycle boundary][cdk8s-e4], [Current core library][cdk8s-e5], [Core release history][cdk8s-e6] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [1.x to 2.x lifecycle boundary][cdk8s-e4], [Core release history][cdk8s-e6], [Umbrella identity and synthesis-only scope][cdk8s-e1], [Current 2.x documentation and languages][cdk8s-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `roles`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[cdk8s-e1]: https://github.com/cdk8s-team/cdk8s
[cdk8s-e2]: https://github.com/cdk8s-team/cdk8s/blob/master/LICENSE
[cdk8s-e3]: https://cdk8s.io/docs/latest/
[cdk8s-e4]: https://cdk8s.io/docs/latest/migrating-from-1.x/
[cdk8s-e5]: https://github.com/cdk8s-team/cdk8s-core
[cdk8s-e6]: https://github.com/cdk8s-team/cdk8s-core/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/cdk8s-team/cdk8s) (`archived: false`).

### spinnaker

**Identity boundary:** Multi-cloud continuous delivery project, not a build/test CI server. Existing stable ID and project repository are preserved.

**Licence boundary:** Apache-2.0 applies to the project; vendor distributions and integrations have independent boundaries.

**Lifecycle boundary:** Active CDF project with 2026.3 release and 2026.2 patches. Halyard was removed; native Kustomize is the documented supported installation. Installer removal does not deprecate the project.

**Repository boundary:** Keep spinnaker/spinnaker; GitHub API archived=false and October 2026 commits. Release/install documentation independently corroborates lifecycle.

**Maturity:** Established is supported by sustained multi-cloud release capabilities, supported release policy and documented current maintenance.

**Unresolved questions / limits:** None blocking the active project. Operators must select a supported release and follow current security/installation guidance; this review is not a security audit.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical project][spinnaker-e1], [Software licence][spinnaker-e2], [Official documentation][spinnaker-e3], [Native Kustomize installation][spinnaker-e4], [Supported releases][spinnaker-e5], [Current CDF activity and Halyard removal][spinnaker-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | spinnaker | spinnaker | [Official documentation][spinnaker-e3] | Preserve stable catalogue identity and history. |
| `name` | Spinnaker | Spinnaker | [Official documentation][spinnaker-e3] | Reviewed; retained: documented identity/capability; scoped boundary above applies. |
| `summary` | Multi-cloud continuous delivery platform. | Open-source multi-cloud continuous delivery platform for orchestrating application releases and deployment strategies. | [Official documentation][spinnaker-e3] | Changed: documented identity/capability; scoped boundary above applies. |
| `official_url` | https://spinnaker.io | https://spinnaker.io | [Official documentation][spinnaker-e3] | Verified official product/project entry point; any deliberate scope/identity change is explained above. |
| `repository_url` | https://github.com/spinnaker/spinnaker | https://github.com/spinnaker/spinnaker | [Official documentation][spinnaker-e3], [Software licence][spinnaker-e2] | Keep the canonical project/core pointer with its explicit boundary. |
| `documentation_url` | *absent* | https://spinnaker.io/docs/ | [Official documentation][spinnaker-e3] | Add the directly identified official documentation entry point. |
| `categories` | ci-build-testing | cd-gitops-release-promotion | [Official documentation][spinnaker-e3] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `subcategories` | CI/CD Platforms | Multi-cloud Continuous Delivery | [Official documentation][spinnaker-e3] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `roles` | devops-engineer<br>developer-experience-engineer<br>release-engineer | devops-engineer<br>release-engineer<br>platform-engineer<br>site-reliability-engineer | [Official documentation][spinnaker-e3] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `lifecycle_stages` | build<br>test | release<br>deploy<br>operate | [Official documentation][spinnaker-e3] | Changed: reviewer taxonomy mapping of documented capabilities. |
| `use_when` | * You deploy across multiple clouds and need advanced deployment strategies (canary, blue/green). | You need multi-cloud delivery pipelines with canary or blue-green strategies and can operate Spinnaker using the documented native Kustomize installation. | [Official documentation][spinnaker-e3], [Native Kustomize installation][spinnaker-e4], [Software licence][spinnaker-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `avoid_when` | * You have a single small cluster; Spinnaker&#x27;s operational overhead is significant. | You only need a small single-cluster deployment workflow, or require the removed Halyard installation mechanism instead of native Kustomize. | [Official documentation][spinnaker-e3], [Native Kustomize installation][spinnaker-e4], [Software licence][spinnaker-e2] | Changed: functional guidance from documented capability, licence and deployment boundaries. |
| `deployment_models` | `[]` | self-hosted | [Official documentation][spinnaker-e3], [Native Kustomize installation][spinnaker-e4] | Record documented execution/control-plane modes only; workers, CLIs and vendor services are distinguished above. |
| `license_model` | oss | oss | [Software licence][spinnaker-e2] | Reviewed; retained: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Software licence][spinnaker-e2] | Changed: actual software/legal grant and scoped offering boundary; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Software licence][spinnaker-e2] | Leave optional field absent; no blanket assertion about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Supported releases][spinnaker-e5], [Current CDF activity and Halyard removal][spinnaker-e6], [Official documentation][spinnaker-e3] | Reviewer judgement explained above; foundation level is not automatically mapped to catalogue maturity. |
| `status` | needs-review | active | [Supported releases][spinnaker-e5], [Current CDF activity and Halyard removal][spinnaker-e6], [Official documentation][spinnaker-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |
| `repository_archived` | *absent* | `false` | [Official documentation][spinnaker-e3] | GitHub API reports archived=false for the retained repository; activity/release evidence is reviewed separately. |
| `alternatives` | `[]` | `[]` | [Official documentation][spinnaker-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `tags` | `[]` | `[]` | [Official documentation][spinnaker-e3] | Retain empty optional metadata; no unsupported comparison, substitute record or additional tag claim. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical project][spinnaker-e1], [Software licence][spinnaker-e2], [Official documentation][spinnaker-e3], [Native Kustomize installation][spinnaker-e4], [Supported releases][spinnaker-e5], [Current CDF activity and Halyard removal][spinnaker-e6] | Date of this actual primary-source review, set only for these ten records. |
| `sources` | legacy:3_CI-CD-Automation/README.md#L60<br>legacy:devopstools_final.md#L339 | legacy:3_CI-CD-Automation/README.md#L60<br>legacy:devopstools_final.md#L339<br>https://github.com/spinnaker/spinnaker<br>https://github.com/spinnaker/spinnaker/blob/main/LICENSE<br>https://spinnaker.io/docs/<br>https://spinnaker.io/docs/setup/install/<br>https://spinnaker.io/docs/releases/<br>https://cd.foundation/blog/2026/09/30/project-updates-sept-2026/ | [Canonical project][spinnaker-e1], [Software licence][spinnaker-e2], [Official documentation][spinnaker-e3], [Native Kustomize installation][spinnaker-e4], [Supported releases][spinnaker-e5], [Current CDF activity and Halyard removal][spinnaker-e6] | Preserve every historical source and append the primary sources checked. |
| `needs_review` | `true` | `false` | [Supported releases][spinnaker-e5], [Current CDF activity and Halyard removal][spinnaker-e6], [Official documentation][spinnaker-e3] | CLEAR REVIEW; current release/operational evidence supports active status and consistent false review flag. |

**Changed fields:** `summary`, `documentation_url`, `categories`, `subcategories`, `roles`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[spinnaker-e1]: https://github.com/spinnaker/spinnaker
[spinnaker-e2]: https://github.com/spinnaker/spinnaker/blob/main/LICENSE
[spinnaker-e3]: https://spinnaker.io/docs/
[spinnaker-e4]: https://spinnaker.io/docs/setup/install/
[spinnaker-e5]: https://spinnaker.io/docs/releases/
[spinnaker-e6]: https://cd.foundation/blog/2026/09/30/project-updates-sept-2026/

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/spinnaker/spinnaker) (`archived: false`).

## Review-debt accounting

`python -m scripts.review_debt --format markdown --limit 30` was captured before and after. Selected: **10**; cleared: **10**; retained: **0**.

| Counter | Before | After |
|---|---:|---:|
| canonical_records | 1,425 | 1,425 |
| needs_review | 786 | 776 |
| status_needs_review | 786 | 776 |
| mismatches | 0 | 0 |
| unknown_license | 83 | 81 |
| unknown_maturity | 923 | 913 |
| missing_repository | 394 | 394 |
| missing_documentation | 920 | 910 |
| missing_sources | 0 | 0 |

The invariant `needs_review == status needs-review` holds for every canonical record. Missing repository count remains unchanged because proprietary parent repositories are not invented.

## Generated changes

Only generator output is listed here; the evidence report and focused regression test are authored files.

- `README.md`
- `docs/catalog-statistics.json`
- `docs/categories/application-cloud-security.md`
- `docs/categories/artifact-package-management.md`
- `docs/categories/cd-gitops-release-promotion.md`
- `docs/categories/ci-build-testing.md`
- `docs/categories/infrastructure-as-code.md`
- `docs/categories/kubernetes-distributions-operations.md`
- `docs/categories/kubernetes-networking-storage-addons.md`
- `docs/categories/platform-engineering-idp.md`
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

Required checks passed. Python 3.12.3 on WSL Ubuntu used the constrained development environment for installation, dependency drift and the complete suite. The Windows editable environment also ran focused tests, generation, catalogue validation and debt capture. `python` below denotes the selected environment interpreter.

| Command | Result |
|---|---|
| `python -m pip install -e '.[dev]' -c config/python-constraints-3.12.txt` | PASS; editable install, reviewed constraints unchanged |
| `python -m scripts.python_constraints --check` | PASS; fresh resolver matches `config/python-constraints-3.12.txt` |
| `python -m ruff check scripts tests` | PASS |
| `python -m ruff format --check scripts tests` | PASS; 58 files already formatted |
| `python -m pytest tests/test_wave5_evidence_review.py` | PASS; 17 tests |
| `python -m pytest` | PASS; 687 tests in 256.97 seconds |
| `python -m scripts.generate_docs` | PASS; regenerated after canonical edits |
| `python -m scripts.generate_docs --check` | PASS |
| `python -m scripts.validate_catalog` | PASS |
| `python -m scripts.review_debt --format markdown --limit 30` | PASS; before/after counters captured above |
| `git diff --check` | PASS |

The initial lint check found one reversed equality in the new test; it was corrected before the passing check. An initial Windows constraint-check bootstrap hit sandbox temporary-directory permissions; the complete fresh resolver check passed on the supported Linux environment. Pytest emitted a cache-directory permission warning; all tests passed. No checks or assertions were weakened.

The focused test covers commercial parent/component licensing, Nexus Core versus CE, k0rdent management taxonomy, worker/control-plane deployment, CloudBees CI identity, OSS upstreams, Tekton ecosystem/governance, OpenTofu/Terraform support, cdk8s synthesis-only scope, and Spinnaker versus Halyard lifecycle. It does not pin release versions, support dates or pricing amounts.

One full fresh strict audit was run with the requested settings plus ignored output paths and disabled cache reuse:

```bash
python -m scripts.check_links --strict --check-archived --workers 8 --cache tmp/wave5/link-cache.json --cache-hours 0 --json-report tmp/wave5/link-report.json --markdown-report tmp/wave5/link-report.md
```

| Audit counter | Result |
|---|---:|
| URLs | 2,624 |
| blocking_new | 0 |
| blocking_known observed | 4 |
| strict_result | PASS |

All audited URL contexts match the final canonical catalogue. All ten new documentation entry points returned HTTP 200 (Terragrunt's docs entry point follows a documented redirect). The six reviewed baseline entries remain unchanged:

| Existing baseline URL | Observed response | Strict classification |
|---|---|---|
| `https://github.com/hoji-ai/hoji` | HTTP 429; rate-limited | nonblocking |
| `https://github.com/ophircloud/DevOps-Projects` | HTTP 429; rate-limited | nonblocking |
| `https://hub.docker.com/r/soosio/dast` | HTTP 404 | blocking-known |
| `https://kubeflame.github.io` | HTTP 404 | blocking-known |
| `https://www.opentext.com/products/static-application-security-testing` | HTTP 444 | blocking-known |
| `https://www.yotascale.com` | HTTP 404 | blocking-known |

The checker labels the two nonblocking baseline observations `baseline_resolved`; HTTP 429 does **not** establish that either historical defect was fixed. They remain in the baseline. Across the entire run there were 752 rate-limited, 358 restricted/bot-blocked, five DNS-inconclusive, three network-inconclusive, one timeout-inconclusive and one transient-failure result. PASS means no newly classified blockers, not successful verification of every endpoint. Authenticated upstream API metadata and directly read releases were used independently for reviewed lifecycle/archive claims.

Raw audit/cache output stays in ignored `tmp/wave5/`; nothing under `reports/` is committed. No additional full audit was run. The checker inventories official/repository/documentation fields; source-only evidence links were read separately rather than treated as part of that inventory.

## Scope verification and review state

The pre-edit versus final comparison found exactly ten changed IDs, exactly ten changed verification dates, and exactly ten changed record blocks (line endings normalized for comparison). All other records and their provenance remain unchanged. The report contains exactly 240 material-field rows with resolved evidence references. The audit's 2,624 URLs match final canonical URL contexts. The baseline still has six unchanged entries. Issue #2's body and `updated_at` (`2026-10-07T11:37:41Z`) match the pre-edit snapshot.

Material evidence corrections are resolved in the canonical data and documented above: k0rdent scanner misidentification; Nexus Core/CE licence separation; free versus OSS TeamCity; Spacelift workers versus control plane and Deploy rename; CloudBees CI versus portfolio/Jenkins; superseded Helm v3 support notice; Tekton's CNCF transfer and ecosystem boundary; Terragrunt's OpenTofu support; cdk8s synthesis-only and 2.x boundary; Spinnaker installer removal versus active project lifecycle.

CI/security outcomes and any subsequent PR review findings are reported in the PR and final handoff against the final commit. No merge or release is performed.
