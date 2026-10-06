# Evidence review Wave 4 — 2026-10-06

Exactly ten existing canonical records were reviewed. Canonical YAML is authoritative; generated pages were regenerated. Stable IDs and legacy provenance were preserved. The review clears eight records and retains two with specific unresolved boundaries.

## Baseline and scope

- Main: `49a740f8fd704a393668348dd22fd6e93f552ac7`.
- Branch: `maintenance/wave-4-evidence-review`.
- Before editing: only remote main, zero open PRs and zero open CodeQL alerts.
- Full link audit #17, run `37490107565`: its downloaded report contains 2,605 results, zero new blockers, six known blockers and PASS.
- Issue #2 was read as the authoritative tracker: Wave 4 was NOT STARTED — READY TO SCOPE. It is not edited by this work.
- No changes to the audit baseline, committed link reports, historical ledger, workflow/CodeQL configuration, constraints or unrelated records.

The fixed cohort has direct DevOps relevance and four strong initial debt signals: unknown licence, unknown maturity, no product source repository and no documentation URL. All ten began with status `needs-review`, `needs_review: true`, and verification date `2026-08-03`. Absence of a proprietary parent repository is not itself evidence debt requiring an invented repository. Cohort rank below is the user-specified order, not an altered global priority ranking.

| Rank | ID | Initial name | Initial primary category | Initial signals |
|---:|---|---|---|---|
| 1 | `orbstack` | OrbStack | `virtualization-bare-metal-homelab` | unknown licence; unknown maturity; missing repository; missing docs |
| 2 | `octopus-deploy` | Octopus Deploy | `ci-build-testing` | unknown licence; unknown maturity; missing repository; missing docs |
| 3 | `mergify` | Mergify | `ci-build-testing` | unknown licence; unknown maturity; missing repository; missing docs |
| 4 | `nvidia-dgx-cloud` | NVIDIA DGX Cloud | `mlops-llmops-ai-infrastructure` | unknown licence; unknown maturity; missing repository; missing docs |
| 5 | `palo-alto-cortex-cloud` | Palo Alto Cortex Cloud | `application-cloud-security` | unknown licence; unknown maturity; missing repository; missing docs |
| 6 | `manageengine-network-configuration-manager` | ManageEngine Network Configuration Manager | `application-cloud-security` | unknown licence; unknown maturity; missing repository; missing docs |
| 7 | `gremlin` | Gremlin | `chaos-performance-engineering` | unknown licence; unknown maturity; missing repository; missing docs |
| 8 | `komodor` | Komodor | `monitoring-metrics-logs-tracing` | unknown licence; unknown maturity; missing repository; missing docs |
| 9 | `morpheus-data` | Morpheus Data | `cloud-platforms-management` | unknown licence; unknown maturity; missing repository; missing docs |
| 10 | `moogsoft` | Moogsoft | `sre-incident-response-on-call` | unknown licence; unknown maturity; missing repository; missing docs |

## Decisions and complete field review

Maturity is an explicit reviewer judgement from release/operational evidence, not a vendor-certified taxonomy or popularity score. Categories, roles and lifecycle stages are mappings of documented capabilities to repository taxonomy. Use/avoid statements are functional selection guidance; they do not invent product incompatibilities. Empty optional metadata is deliberately retained when it is unnecessary or no parent-wide claim is justified. Search snippets were only discovery aids; the cited product/docs/terms were read directly. A documentation transport restriction does not determine lifecycle.

### orbstack

**Identity boundary:** OrbStack is the macOS application, including Docker, Kubernetes and Linux machines. The public GitHub project is an issue/support surface with small integration files; it does not establish a source repository for the application.

**Licensing boundary:** The product terms grant restricted application rights. Personal, noncommercial use is free; professional/business use requires a commercial licence, subject to the published licensing conditions. Neither acknowledgements nor the integration repository MIT badge licenses the parent application.

**Lifecycle and maturity:** Stable application releases through 2026, a multiyear release history and operational documentation support active status and the reviewer judgement established; popularity was not used.

**Unresolved questions / limits:** No material canonical uncertainty. Eligibility and evaluation terms should be checked against the current licence; no prices or eligibility thresholds are asserted here.

**Disposition: CLEAR REVIEW**

**Primary sources read:** [product][orbstack-product], [docs][orbstack-docs], [licence][orbstack-licence], [editions][orbstack-editions], [releases][orbstack-releases], [repository][orbstack-repository].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | orbstack | orbstack | [product][orbstack-product], [docs][orbstack-docs] | Reviewed; preserve stable identity and history. |
| `name` | OrbStack | OrbStack | [product][orbstack-product], [docs][orbstack-docs], [licence][orbstack-licence] | Reviewed; retained: exact current parent identity/capabilities; boundaries explained above. |
| `summary` | Fast Docker & Linux VM environment for macOS. | Local macOS environment for Docker containers, Kubernetes and Linux virtual machines. | [product][orbstack-product], [docs][orbstack-docs], [licence][orbstack-licence] | Changed: exact current parent identity/capabilities; boundaries explained above. |
| `official_url` | https://orbstack.dev | https://orbstack.dev | [product][orbstack-product], [docs][orbstack-docs] | Reviewed current identity; retain official-domain entry point. |
| `repository_url` | *absent* | *absent* | [repository][orbstack-repository], [docs][orbstack-docs], [licence][orbstack-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `documentation_url` | *absent* | https://docs.orbstack.dev/ | [docs][orbstack-docs] | Add the directly identified product documentation entry point; scope caveat above applies. |
| `categories` | virtualization-bare-metal-homelab | virtualization-bare-metal-homelab<br>developer-experience-local-environments | [product][orbstack-product], [docs][orbstack-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `subcategories` | Virtualization & Containerization | Virtualization & Containerization | [product][orbstack-product], [docs][orbstack-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `roles` | devops-engineer<br>infrastructure-systems-engineer | devops-engineer<br>infrastructure-systems-engineer | [product][orbstack-product], [docs][orbstack-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `lifecycle_stages` | deploy<br>operate | develop<br>build<br>test<br>deploy<br>operate | [product][orbstack-product], [docs][orbstack-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `use_when` | You want a faster, lower-resource Docker Desktop alternative on macOS. | You need a local Docker, Kubernetes and Linux development environment on macOS. | [product][orbstack-product], [docs][orbstack-docs], [licence][orbstack-licence], [editions][orbstack-editions] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `avoid_when` | You need cross-platform support or a fully open-source tool. | You need cross-platform support or a fully open-source tool. | [product][orbstack-product], [docs][orbstack-docs], [licence][orbstack-licence], [editions][orbstack-editions] | Reviewed; retained: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `deployment_models` | `[]` | local | [docs][orbstack-docs], [editions][orbstack-editions], [licence][orbstack-licence] | Record only documented deployment modes; edition/beta qualifications above apply. |
| `license_model` | unknown | commercial | [licence][orbstack-licence], [editions][orbstack-editions] | Commercial product rights established independently of pricing alone. |
| `license_spdx` | *absent* | *absent* | [licence][orbstack-licence] | Reviewed; no parent OSS grant established. Leave absent; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [licence][orbstack-licence], [editions][orbstack-editions] | Commercial product rights established independently of pricing alone. |
| `maturity` | unknown | established | [releases][orbstack-releases], [docs][orbstack-docs], [product][orbstack-product], [licence][orbstack-licence] | Reviewer judgement explained above from maintained releases/operational documentation. |
| `status` | needs-review | active | [product][orbstack-product], [docs][orbstack-docs], [releases][orbstack-releases], [licence][orbstack-licence] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |
| `repository_archived` | *absent* | *absent* | [repository][orbstack-repository], [docs][orbstack-docs], [licence][orbstack-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `alternatives` | `[]` | `[]` | [product][orbstack-product], [docs][orbstack-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `tags` | `[]` | `[]` | [product][orbstack-product], [docs][orbstack-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `verified_on` | 2026-08-03 | 2026-10-06 | [product][orbstack-product], [docs][orbstack-docs], [licence][orbstack-licence], [editions][orbstack-editions], [releases][orbstack-releases], [repository][orbstack-repository] | Date of this actual primary-source review, including retained records; not a ranking adjustment. |
| `sources` | legacy:2_Cloud-Infrastructure-Serverless/README.md#L170<br>legacy:devopstools_final.md#L257 | legacy:2_Cloud-Infrastructure-Serverless/README.md#L170<br>legacy:devopstools_final.md#L257<br>https://orbstack.dev/<br>https://docs.orbstack.dev/<br>https://docs.orbstack.dev/legal/terms<br>https://docs.orbstack.dev/licensing<br>https://docs.orbstack.dev/release-notes<br>https://github.com/orbstack/orbstack | [product][orbstack-product], [docs][orbstack-docs], [licence][orbstack-licence], [editions][orbstack-editions], [releases][orbstack-releases], [repository][orbstack-repository] | Preserve every historical provenance entry and append the primary sources actually reviewed. |
| `needs_review` | `true` | `false` | [product][orbstack-product], [docs][orbstack-docs], [releases][orbstack-releases], [licence][orbstack-licence] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |

**Changed fields:** `summary`, `categories`, `lifecycle_stages`, `use_when`, `deployment_models`, `license_model`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`, `documentation_url`, `commercial_offering`.

### octopus-deploy

**Identity boundary:** Octopus Deploy is deployment/release automation. Cloud is vendor-hosted Octopus Server software; Server is customer-managed. Kubernetes is supported, so the historical Kubernetes-native exclusion is removed.

**Licensing boundary:** Free, Professional and Enterprise are licensed editions of the product. The FAQ describes licence keys and the customer agreement; a Free edition does not establish OSS rights.

**Lifecycle and maturity:** Current recommended Server releases and continuously shipped Cloud releases, alongside deployment and runbook documentation, support active and established.

**Unresolved questions / limits:** No material canonical uncertainty. Commercial agreement and edition entitlements govern the selected deployment; no fixed quotas are recorded.

**Disposition: CLEAR REVIEW**

**Primary sources read:** [product][octopus-deploy-product], [docs][octopus-deploy-docs], [licence][octopus-deploy-licence], [editions][octopus-deploy-editions], [releases][octopus-deploy-releases].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | octopus-deploy | octopus-deploy | [product][octopus-deploy-product], [docs][octopus-deploy-docs] | Reviewed; preserve stable identity and history. |
| `name` | Octopus Deploy | Octopus Deploy | [product][octopus-deploy-product], [docs][octopus-deploy-docs], [licence][octopus-deploy-licence] | Reviewed; retained: exact current parent identity/capabilities; boundaries explained above. |
| `summary` | Deployment automation platform. | Deployment and release automation for applications and infrastructure across environments, including Kubernetes. | [product][octopus-deploy-product], [docs][octopus-deploy-docs], [licence][octopus-deploy-licence] | Changed: exact current parent identity/capabilities; boundaries explained above. |
| `official_url` | https://octopus.com | https://octopus.com | [product][octopus-deploy-product], [docs][octopus-deploy-docs] | Reviewed current identity; retain official-domain entry point. |
| `repository_url` | *absent* | *absent* | [docs][octopus-deploy-docs], [licence][octopus-deploy-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `documentation_url` | *absent* | https://octopus.com/docs | [docs][octopus-deploy-docs] | Add the directly identified product documentation entry point; scope caveat above applies. |
| `categories` | ci-build-testing | cd-gitops-release-promotion | [product][octopus-deploy-product], [docs][octopus-deploy-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `subcategories` | CI/CD Platforms | Deployment & Release Automation | [product][octopus-deploy-product], [docs][octopus-deploy-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `roles` | devops-engineer<br>developer-experience-engineer<br>release-engineer | devops-engineer<br>developer-experience-engineer<br>release-engineer | [product][octopus-deploy-product], [docs][octopus-deploy-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `lifecycle_stages` | build<br>test | release<br>deploy<br>operate | [product][octopus-deploy-product], [docs][octopus-deploy-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `use_when` | * You need release management and deployment orchestration across multiple environments. | You need governed release promotion, deployment orchestration and operational runbooks across environments. | [product][octopus-deploy-product], [docs][octopus-deploy-docs], [licence][octopus-deploy-licence], [editions][octopus-deploy-editions] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `avoid_when` | * You only need CI (Octopus focuses on CD) or you're fully Kubernetes-native. | You only need CI builds and tests without deployment or release orchestration. | [product][octopus-deploy-product], [docs][octopus-deploy-docs], [licence][octopus-deploy-licence], [editions][octopus-deploy-editions] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `deployment_models` | `[]` | hosted-saas<br>self-hosted | [docs][octopus-deploy-docs], [editions][octopus-deploy-editions], [licence][octopus-deploy-licence] | Record only documented deployment modes; edition/beta qualifications above apply. |
| `license_model` | unknown | commercial | [licence][octopus-deploy-licence], [editions][octopus-deploy-editions] | Commercial product rights established independently of pricing alone. |
| `license_spdx` | *absent* | *absent* | [licence][octopus-deploy-licence] | Reviewed; no parent OSS grant established. Leave absent; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [licence][octopus-deploy-licence], [editions][octopus-deploy-editions] | Commercial product rights established independently of pricing alone. |
| `maturity` | unknown | established | [releases][octopus-deploy-releases], [docs][octopus-deploy-docs], [product][octopus-deploy-product], [licence][octopus-deploy-licence] | Reviewer judgement explained above from maintained releases/operational documentation. |
| `status` | needs-review | active | [product][octopus-deploy-product], [docs][octopus-deploy-docs], [releases][octopus-deploy-releases], [licence][octopus-deploy-licence] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |
| `repository_archived` | *absent* | *absent* | [docs][octopus-deploy-docs], [licence][octopus-deploy-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `alternatives` | `[]` | `[]` | [product][octopus-deploy-product], [docs][octopus-deploy-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `tags` | `[]` | `[]` | [product][octopus-deploy-product], [docs][octopus-deploy-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `verified_on` | 2026-08-03 | 2026-10-06 | [product][octopus-deploy-product], [docs][octopus-deploy-docs], [licence][octopus-deploy-licence], [editions][octopus-deploy-editions], [releases][octopus-deploy-releases] | Date of this actual primary-source review, including retained records; not a ranking adjustment. |
| `sources` | legacy:3_CI-CD-Automation/README.md#L54<br>legacy:devopstools_final.md#L336 | legacy:3_CI-CD-Automation/README.md#L54<br>legacy:devopstools_final.md#L336<br>https://octopus.com/docs<br>https://octopus.com/legal/customer-agreement<br>https://octopus.com/pricing/faq<br>https://octopus.com/downloads/previous | [product][octopus-deploy-product], [docs][octopus-deploy-docs], [licence][octopus-deploy-licence], [editions][octopus-deploy-editions], [releases][octopus-deploy-releases] | Preserve every historical provenance entry and append the primary sources actually reviewed. |
| `needs_review` | `true` | `false` | [product][octopus-deploy-product], [docs][octopus-deploy-docs], [releases][octopus-deploy-releases], [licence][octopus-deploy-licence] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |

**Changed fields:** `summary`, `categories`, `subcategories`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_model`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`, `documentation_url`, `commercial_offering`.

### mergify

**Identity boundary:** The parent product includes all four named products. The SaaS contract explicitly identifies proprietary Mergify software. Historical/public components do not prove a current source repository for this parent product.

**Licensing boundary:** The proprietary SaaS terms establish commercial rights independently of prices. The Free / Open Source usage plan concerns who can use the service; it is not an OSS grant for Mergify. The current changelog also documents self-hosted Enterprise releases.

**Lifecycle and maturity:** Current 2026 updates across the four products and versioned Enterprise releases support active and established, rather than treating a deprecated configuration option as product deprecation.

**Unresolved questions / limits:** No material canonical uncertainty. Self-hosting is an Enterprise offering; free service eligibility and exact entitlements remain governed by vendor terms.

**Disposition: CLEAR REVIEW**

**Primary sources read:** [product][mergify-product], [docs][mergify-docs], [licence][mergify-licence], [editions][mergify-editions], [releases][mergify-releases].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | mergify | mergify | [product][mergify-product], [docs][mergify-docs] | Reviewed; preserve stable identity and history. |
| `name` | Mergify | Mergify | [product][mergify-product], [docs][mergify-docs], [licence][mergify-licence] | Reviewed; retained: exact current parent identity/capabilities; boundaries explained above. |
| `summary` | Merge queue and pull-request automation to keep CI green and streamline merges. | GitHub workflow platform combining Merge Queue, CI Insights, Test Insights and Merge Protections. | [product][mergify-product], [docs][mergify-docs], [licence][mergify-licence] | Changed: exact current parent identity/capabilities; boundaries explained above. |
| `official_url` | https://mergify.com | https://mergify.com | [product][mergify-product], [docs][mergify-docs] | Reviewed current identity; retain official-domain entry point. |
| `repository_url` | *absent* | *absent* | [docs][mergify-docs], [licence][mergify-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `documentation_url` | *absent* | https://docs.mergify.com/ | [docs][mergify-docs] | Add the directly identified product documentation entry point; scope caveat above applies. |
| `categories` | ci-build-testing | ci-build-testing<br>source-control-repository-management | [product][mergify-product], [docs][mergify-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `subcategories` | CI/CD Platforms | Merge Queues & CI/Test Automation | [product][mergify-product], [docs][mergify-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `roles` | devops-engineer<br>developer-experience-engineer<br>release-engineer | devops-engineer<br>developer-experience-engineer<br>release-engineer | [product][mergify-product], [docs][mergify-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `lifecycle_stages` | build<br>test | develop<br>build<br>test | [product][mergify-product], [docs][mergify-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `use_when` | `[]` | You need governed GitHub merge queues, CI visibility and flaky-test management across pull requests. | [product][mergify-product], [docs][mergify-docs], [licence][mergify-licence], [editions][mergify-editions] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `avoid_when` | `[]` | You need a platform independent of GitHub or only basic manual pull-request merging. | [product][mergify-product], [docs][mergify-docs], [licence][mergify-licence], [editions][mergify-editions] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `deployment_models` | `[]` | hosted-saas<br>self-hosted | [docs][mergify-docs], [editions][mergify-editions], [licence][mergify-licence] | Record only documented deployment modes; edition/beta qualifications above apply. |
| `license_model` | unknown | commercial | [licence][mergify-licence], [editions][mergify-editions] | Commercial product rights established independently of pricing alone. |
| `license_spdx` | *absent* | *absent* | [licence][mergify-licence] | Reviewed; no parent OSS grant established. Leave absent; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [licence][mergify-licence], [editions][mergify-editions] | Commercial product rights established independently of pricing alone. |
| `maturity` | unknown | established | [releases][mergify-releases], [docs][mergify-docs], [product][mergify-product], [licence][mergify-licence] | Reviewer judgement explained above from maintained releases/operational documentation. |
| `status` | needs-review | active | [product][mergify-product], [docs][mergify-docs], [releases][mergify-releases], [licence][mergify-licence] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |
| `repository_archived` | *absent* | *absent* | [docs][mergify-docs], [licence][mergify-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `alternatives` | `[]` | `[]` | [product][mergify-product], [docs][mergify-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `tags` | `[]` | `[]` | [product][mergify-product], [docs][mergify-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `verified_on` | 2026-08-03 | 2026-10-06 | [product][mergify-product], [docs][mergify-docs], [licence][mergify-licence], [editions][mergify-editions], [releases][mergify-releases] | Date of this actual primary-source review, including retained records; not a ranking adjustment. |
| `sources` | legacy:devopstools_final.md#L333 | legacy:devopstools_final.md#L333<br>https://mergify.com/<br>https://docs.mergify.com/<br>https://mergify.com/tos<br>https://mergify.com/pricing<br>https://docs.mergify.com/changelog/ | [product][mergify-product], [docs][mergify-docs], [licence][mergify-licence], [editions][mergify-editions], [releases][mergify-releases] | Preserve every historical provenance entry and append the primary sources actually reviewed. |
| `needs_review` | `true` | `false` | [product][mergify-product], [docs][mergify-docs], [releases][mergify-releases], [licence][mergify-licence] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |

**Changed fields:** `summary`, `categories`, `subcategories`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_model`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`, `documentation_url`, `commercial_offering`.

### nvidia-dgx-cloud

**Identity boundary:** The current product page leads with NVIDIA internal AI infrastructure and a proving ground, while retaining managed-training links. Run:ai on DGX Cloud documentation describes customer clusters and subscriptions. DGX Cloud, Lepton and DSX are not interchangeable parent identities.

**Licensing boundary:** DGX Cloud service-specific terms require paid per-node subscriptions. They establish the documented service boundary, but do not license the internal environment or establish the availability of the historical parent offering. Parent license_model and maturity remain unknown; no DSX/component OSS licence is inherited.

**Lifecycle and maturity:** Operational service documentation and an internal-environment description coexist. No primary retirement notice was established, so neither active customer availability nor deprecation is asserted for the ambiguous parent record.

**Unresolved questions / limits:** Resolve whether this stable record denotes the internal environment or a currently orderable managed service, and obtain a current offering/availability or migration notice from NVIDIA. The documentation URL is specifically Run:ai on DGX Cloud, not proof that it covers the entire DGX Cloud identity.

**Disposition: RETAIN REVIEW — SPECIFIC UNRESOLVED BOUNDARY**

**Primary sources read:** [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs], [licence][nvidia-dgx-cloud-licence].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | nvidia-dgx-cloud | nvidia-dgx-cloud | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs] | Reviewed; preserve stable identity and history. |
| `name` | NVIDIA DGX Cloud | NVIDIA DGX Cloud | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs], [licence][nvidia-dgx-cloud-licence] | Reviewed; retained: exact current parent identity/capabilities; boundaries explained above. |
| `summary` | Cloud platform for AI and ML workloads. | NVIDIA AI cloud environment, currently described as an internal proving ground, with separately documented Run:ai on DGX Cloud managed subscriptions. | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs], [licence][nvidia-dgx-cloud-licence] | Changed: exact current parent identity/capabilities; boundaries explained above. |
| `official_url` | https://www.nvidia.com/en-us/data-center/dgx-cloud | https://www.nvidia.com/en-us/data-center/dgx-cloud | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs] | Reviewed current identity; retain official-domain entry point. |
| `repository_url` | *absent* | *absent* | [docs][nvidia-dgx-cloud-docs], [licence][nvidia-dgx-cloud-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `documentation_url` | *absent* | https://docs.nvidia.com/dgx-cloud/run-ai/latest/overview.html | [docs][nvidia-dgx-cloud-docs] | Add the directly identified product documentation entry point; scope caveat above applies. |
| `categories` | mlops-llmops-ai-infrastructure | mlops-llmops-ai-infrastructure | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `subcategories` | MLOps Platforms | MLOps Platforms | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `roles` | cloud-engineer<br>platform-engineer<br>mlops-ai-infrastructure-engineer | cloud-engineer<br>platform-engineer<br>mlops-ai-infrastructure-engineer | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `lifecycle_stages` | build<br>deploy<br>operate | build<br>deploy<br>operate | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `use_when` | You need massive GPU compute for large-scale model training or fine-tuning. | You are evaluating NVIDIA-managed GPU training infrastructure and can confirm the current DGX Cloud offering and customer availability. | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs], [licence][nvidia-dgx-cloud-licence] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `avoid_when` | Your workloads are inference-only or fit comfortably on commodity cloud GPUs. | You require a confirmed customer-facing service boundary without reconciling the internal DGX Cloud identity and managed-service documentation. | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs], [licence][nvidia-dgx-cloud-licence] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `deployment_models` | `[]` | `[]` | [docs][nvidia-dgx-cloud-docs], [licence][nvidia-dgx-cloud-licence] | Reviewed; leave empty rather than assert an unsupported parent-wide deployment boundary. |
| `license_model` | unknown | unknown | [licence][nvidia-dgx-cloud-licence] | Reviewed service terms; parent scope remains unresolved. Retain unknown/absent rather than inherit service-only rights. |
| `license_spdx` | *absent* | *absent* | [licence][nvidia-dgx-cloud-licence] | Reviewed; no parent OSS grant established. Leave absent; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [licence][nvidia-dgx-cloud-licence] | Reviewed service terms; parent scope remains unresolved. Retain unknown/absent rather than inherit service-only rights. |
| `maturity` | unknown | unknown | [docs][nvidia-dgx-cloud-docs], [product][nvidia-dgx-cloud-product], [licence][nvidia-dgx-cloud-licence] | Reviewed; unknown retained because current parent identity/lifecycle is unresolved. |
| `status` | needs-review | needs-review | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs], [licence][nvidia-dgx-cloud-licence] | RETAIN REVIEW — SPECIFIC UNRESOLVED BOUNDARY; unresolved identity prevents clearing; no unsupported deprecation. |
| `repository_archived` | *absent* | *absent* | [docs][nvidia-dgx-cloud-docs], [licence][nvidia-dgx-cloud-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `alternatives` | `[]` | `[]` | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `tags` | `[]` | `[]` | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `verified_on` | 2026-08-03 | 2026-10-06 | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs], [licence][nvidia-dgx-cloud-licence] | Date of this actual primary-source review, including retained records; not a ranking adjustment. |
| `sources` | legacy:9_AI-MLOps/README.md#L10<br>legacy:devopstools_final.md#L1186 | legacy:9_AI-MLOps/README.md#L10<br>legacy:devopstools_final.md#L1186<br>https://www.nvidia.com/en-us/data-center/dgx-cloud/<br>https://docs.nvidia.com/dgx-cloud/run-ai/latest/overview.html<br>https://www.nvidia.com/en-us/agreements/cloud-services/service-specific-terms-for-nvidia-dgx-cloud/ | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs], [licence][nvidia-dgx-cloud-licence] | Preserve every historical provenance entry and append the primary sources actually reviewed. |
| `needs_review` | `true` | `true` | [product][nvidia-dgx-cloud-product], [docs][nvidia-dgx-cloud-docs], [licence][nvidia-dgx-cloud-licence] | RETAIN REVIEW — SPECIFIC UNRESOLVED BOUNDARY; unresolved identity prevents clearing; no unsupported deprecation. |

**Changed fields:** `summary`, `use_when`, `avoid_when`, `verified_on`, `sources`, `documentation_url`.

### palo-alto-cortex-cloud

**Identity boundary:** Palo Alto Networks identifies Cortex Cloud as a CNAPP extending application security through cloud runtime and SOC workflows. The product-specific documentation portal separates Runtime Security, Posture Management and Application Security; unrelated Cortex XDR/XSIAM products are not substituted.

**Licensing boundary:** Cortex Cloud-specific licence documentation describes annual subscriptions, purchased protected-workload capacity and separately purchased add-ons. This establishes commercial licensing without inferring it from another Cortex product.

**Lifecycle and maturity:** Current configuration, runtime/posture and API documentation with explicit operational licence plans establishes an active product. Growing is a conservative reviewer judgement for this evolving consolidated platform, not a claim that every feature is generally available.

**Unresolved questions / limits:** No material canonical uncertainty. Entitlements vary by plan/add-on and some add-ons are beta; the record makes no universal entitlement or blanket deployment assertion. The new portal was read directly; raw Markdown retrieval was sometimes bot-blocked, which is not lifecycle evidence.

**Disposition: CLEAR REVIEW**

**Primary sources read:** [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs], [licence][palo-alto-cortex-cloud-licence].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | palo-alto-cortex-cloud | palo-alto-cortex-cloud | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs] | Reviewed; preserve stable identity and history. |
| `name` | Palo Alto Cortex Cloud | Palo Alto Cortex Cloud | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs], [licence][palo-alto-cortex-cloud-licence] | Reviewed; retained: exact current parent identity/capabilities; boundaries explained above. |
| `summary` | Cloud-native security operations platform. | Commercial CNAPP unifying application security, cloud posture and runtime protection with SOC workflows. | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs], [licence][palo-alto-cortex-cloud-licence] | Changed: exact current parent identity/capabilities; boundaries explained above. |
| `official_url` | https://www.paloaltonetworks.com/cortex/cloud | https://www.paloaltonetworks.com/cortex/cloud | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs] | Reviewed current identity; retain official-domain entry point. |
| `repository_url` | *absent* | *absent* | [docs][palo-alto-cortex-cloud-docs], [licence][palo-alto-cortex-cloud-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `documentation_url` | *absent* | https://cortex-docs.paloaltonetworks.com/cortex-cloud-docs | [docs][palo-alto-cortex-cloud-docs] | Add the directly identified product documentation entry point; scope caveat above applies. |
| `categories` | application-cloud-security | application-cloud-security | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `subcategories` | Application Security (SAST, DAST, SCA) & Vulnerability Scanning | Cloud-Native Application Protection Platforms (CNAPP) | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `roles` | devsecops-engineer<br>cloud-security-engineer | devsecops-engineer<br>cloud-security-engineer | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `lifecycle_stages` | test<br>secure | develop<br>test<br>operate<br>monitor<br>secure | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `use_when` | Unified CSPM/CWPP across multi-cloud with SOC integration. | You need code-to-cloud risk visibility, cloud posture management and runtime protection integrated with security operations. | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs], [licence][palo-alto-cortex-cloud-licence] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `avoid_when` | You need lightweight, single-concern tooling. | You need lightweight, single-concern tooling. | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs], [licence][palo-alto-cortex-cloud-licence] | Reviewed; retained: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `deployment_models` | `[]` | `[]` | [docs][palo-alto-cortex-cloud-docs], [licence][palo-alto-cortex-cloud-licence] | Reviewed; leave empty rather than assert an unsupported parent-wide deployment boundary. |
| `license_model` | unknown | commercial | [licence][palo-alto-cortex-cloud-licence] | Commercial product rights established independently of pricing alone. |
| `license_spdx` | *absent* | *absent* | [licence][palo-alto-cortex-cloud-licence] | Reviewed; no parent OSS grant established. Leave absent; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [licence][palo-alto-cortex-cloud-licence] | Commercial product rights established independently of pricing alone. |
| `maturity` | unknown | growing | [docs][palo-alto-cortex-cloud-docs], [product][palo-alto-cortex-cloud-product], [licence][palo-alto-cortex-cloud-licence] | Reviewer judgement explained above from maintained releases/operational documentation. |
| `status` | needs-review | active | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs], [licence][palo-alto-cortex-cloud-licence] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |
| `repository_archived` | *absent* | *absent* | [docs][palo-alto-cortex-cloud-docs], [licence][palo-alto-cortex-cloud-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `alternatives` | `[]` | `[]` | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `tags` | `[]` | `[]` | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `verified_on` | 2026-08-03 | 2026-10-06 | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs], [licence][palo-alto-cortex-cloud-licence] | Date of this actual primary-source review, including retained records; not a ranking adjustment. |
| `sources` | legacy:6_Security/README.md#L44<br>legacy:devopstools_final.md#L899 | legacy:6_Security/README.md#L44<br>legacy:devopstools_final.md#L899<br>https://www.paloaltonetworks.com/cortex/cloud<br>https://cortex-docs.paloaltonetworks.com/cortex-cloud-docs<br>https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/get-started/understand-license-plans | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs], [licence][palo-alto-cortex-cloud-licence] | Preserve every historical provenance entry and append the primary sources actually reviewed. |
| `needs_review` | `true` | `false` | [product][palo-alto-cortex-cloud-product], [docs][palo-alto-cortex-cloud-docs], [licence][palo-alto-cortex-cloud-licence] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |

**Changed fields:** `summary`, `subcategories`, `lifecycle_stages`, `use_when`, `license_model`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`, `documentation_url`, `commercial_offering`.

### manageengine-network-configuration-manager

**Identity boundary:** ManageEngine Network Configuration Manager is Zoho/ManageEngine network-device configuration software, with a customer-installed server and database on Windows or Linux. Its primary function is configuration management, with security/compliance capabilities.

**Licensing boundary:** The product EULA grants restricted binary rights and defines free and paid commercial licences, including subscription/perpetual rights. Neither the free edition nor bundled components establish an OSS parent licence.

**Lifecycle and maturity:** A long versioned release history, current 2026 security fixes and operational installation/administration documentation support active and established.

**Unresolved questions / limits:** Official EULA and installation help disagree on the free-edition device limit (ten versus two). The record asserts no quota, price or entitlement amount; the commercial/free licence distinction is consistent. Confirm the current order-specific free limit before relying on it.

**Disposition: CLEAR REVIEW**

**Primary sources read:** [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs], [licence][manageengine-network-configuration-manager-licence], [editions][manageengine-network-configuration-manager-editions], [releases][manageengine-network-configuration-manager-releases].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | manageengine-network-configuration-manager | manageengine-network-configuration-manager | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs] | Reviewed; preserve stable identity and history. |
| `name` | ManageEngine Network Configuration Manager | ManageEngine Network Configuration Manager | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs], [licence][manageengine-network-configuration-manager-licence] | Reviewed; retained: exact current parent identity/capabilities; boundaries explained above. |
| `summary` | Network device configuration management. | Multi-vendor network configuration management with backups, change tracking, automation and compliance auditing. | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs], [licence][manageengine-network-configuration-manager-licence] | Changed: exact current parent identity/capabilities; boundaries explained above. |
| `official_url` | https://www.manageengine.com/network-configuration-manager | https://www.manageengine.com/network-configuration-manager | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs] | Reviewed current identity; retain official-domain entry point. |
| `repository_url` | *absent* | *absent* | [docs][manageengine-network-configuration-manager-docs], [licence][manageengine-network-configuration-manager-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `documentation_url` | *absent* | https://www.manageengine.com/network-configuration-manager/help/ | [docs][manageengine-network-configuration-manager-docs] | Add the directly identified product documentation entry point; scope caveat above applies. |
| `categories` | application-cloud-security | configuration-management<br>application-cloud-security | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `subcategories` | Network Security | Network Configuration Management & Compliance | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `roles` | devsecops-engineer<br>cloud-security-engineer | infrastructure-systems-engineer<br>devsecops-engineer<br>cloud-security-engineer | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `lifecycle_stages` | test<br>secure | operate<br>monitor<br>secure | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `use_when` | Managing multi-vendor network device configs with change tracking. | You manage supported routers, switches and firewalls and need configuration backups, change control and compliance checks. | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs], [licence][manageengine-network-configuration-manager-licence], [editions][manageengine-network-configuration-manager-editions] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `avoid_when` | Your infrastructure is fully software-defined or cloud-native. | You only need application configuration or cloud resource provisioning without managing supported network devices. | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs], [licence][manageengine-network-configuration-manager-licence], [editions][manageengine-network-configuration-manager-editions] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `deployment_models` | `[]` | self-hosted | [docs][manageengine-network-configuration-manager-docs], [editions][manageengine-network-configuration-manager-editions], [licence][manageengine-network-configuration-manager-licence] | Record only documented deployment modes; edition/beta qualifications above apply. |
| `license_model` | unknown | commercial | [licence][manageengine-network-configuration-manager-licence], [editions][manageengine-network-configuration-manager-editions] | Commercial product rights established independently of pricing alone. |
| `license_spdx` | *absent* | *absent* | [licence][manageengine-network-configuration-manager-licence] | Reviewed; no parent OSS grant established. Leave absent; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [licence][manageengine-network-configuration-manager-licence], [editions][manageengine-network-configuration-manager-editions] | Commercial product rights established independently of pricing alone. |
| `maturity` | unknown | established | [releases][manageengine-network-configuration-manager-releases], [docs][manageengine-network-configuration-manager-docs], [product][manageengine-network-configuration-manager-product], [licence][manageengine-network-configuration-manager-licence] | Reviewer judgement explained above from maintained releases/operational documentation. |
| `status` | needs-review | active | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs], [releases][manageengine-network-configuration-manager-releases], [licence][manageengine-network-configuration-manager-licence] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |
| `repository_archived` | *absent* | *absent* | [docs][manageengine-network-configuration-manager-docs], [licence][manageengine-network-configuration-manager-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `alternatives` | `[]` | `[]` | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `tags` | `[]` | `[]` | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `verified_on` | 2026-08-03 | 2026-10-06 | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs], [licence][manageengine-network-configuration-manager-licence], [editions][manageengine-network-configuration-manager-editions], [releases][manageengine-network-configuration-manager-releases] | Date of this actual primary-source review, including retained records; not a ranking adjustment. |
| `sources` | legacy:6_Security/README.md#L80<br>legacy:devopstools_final.md#L954 | legacy:6_Security/README.md#L80<br>legacy:devopstools_final.md#L954<br>https://www.manageengine.com/network-configuration-manager/<br>https://www.manageengine.com/network-configuration-manager/help/<br>https://www.manageengine.com/network-configuration-manager/license.html<br>https://www.manageengine.com/network-configuration-manager/help/installation-getting-started.html<br>https://www.manageengine.com/network-configuration-manager/release-notes.html | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs], [licence][manageengine-network-configuration-manager-licence], [editions][manageengine-network-configuration-manager-editions], [releases][manageengine-network-configuration-manager-releases] | Preserve every historical provenance entry and append the primary sources actually reviewed. |
| `needs_review` | `true` | `false` | [product][manageengine-network-configuration-manager-product], [docs][manageengine-network-configuration-manager-docs], [releases][manageengine-network-configuration-manager-releases], [licence][manageengine-network-configuration-manager-licence] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |

**Changed fields:** `summary`, `categories`, `subcategories`, `roles`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_model`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`, `documentation_url`, `commercial_offering`.

### gremlin

**Identity boundary:** The current Gremlin parent platform includes reliability management, resilience and disaster-recovery tests alongside fault injection. Private Edition is a request-only isolated deployment of the same platform, not a separate OSS product.

**Licensing boundary:** Enterprise terms describe a subscribed, licensed solution comprising the platform, agents and hosted dashboard, with retained proprietary rights. No exact public source repository for the parent product is established or reintroduced.

**Lifecycle and maturity:** Current operational/safety documentation and platform updates through 2026 with a multiyear history support active and established.

**Unresolved questions / limits:** No material canonical uncertainty. Private Edition requires a vendor arrangement; tests require an authorized target and health checks. Budget and vendor-lock-in slogans were replaced by functional selection boundaries.

**Disposition: CLEAR REVIEW**

**Primary sources read:** [product][gremlin-product], [docs][gremlin-docs], [licence][gremlin-licence], [editions][gremlin-editions], [releases][gremlin-releases], [resilience][gremlin-resilience].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | gremlin | gremlin | [product][gremlin-product], [docs][gremlin-docs] | Reviewed; preserve stable identity and history. |
| `name` | Gremlin | Gremlin | [product][gremlin-product], [docs][gremlin-docs], [licence][gremlin-licence] | Reviewed; retained: exact current parent identity/capabilities; boundaries explained above. |
| `summary` | Chaos engineering platform for proactive reliability testing. ✅ **Use when** you need enterprise-grade chaos with built-in safety controls, team collaboration, and guided scenarios. ❌ **Avoid when** budget is tight or you prefer fully open-source tooling without vendor lock-in. | Reliability management and resilience testing platform with controlled fault injection and disaster-recovery validation. | [product][gremlin-product], [docs][gremlin-docs], [licence][gremlin-licence] | Changed: exact current parent identity/capabilities; boundaries explained above. |
| `official_url` | https://www.gremlin.com | https://www.gremlin.com | [product][gremlin-product], [docs][gremlin-docs] | Reviewed current identity; retain official-domain entry point. |
| `repository_url` | *absent* | *absent* | [docs][gremlin-docs], [licence][gremlin-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `documentation_url` | *absent* | https://www.gremlin.com/docs | [docs][gremlin-docs] | Add the directly identified product documentation entry point; scope caveat above applies. |
| `categories` | chaos-performance-engineering | chaos-performance-engineering<br>backup-disaster-recovery-resilience | [product][gremlin-product], [docs][gremlin-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `subcategories` | Chaos Engineering Platforms | Reliability Management & Resilience Testing | [product][gremlin-product], [docs][gremlin-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `roles` | devops-engineer<br>site-reliability-engineer | devops-engineer<br>site-reliability-engineer | [product][gremlin-product], [docs][gremlin-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `lifecycle_stages` | test<br>operate | test<br>operate | [product][gremlin-product], [docs][gremlin-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `use_when` | `[]` | You need controlled fault injection, service reliability tests and disaster-recovery exercises with health-check safety controls. | [product][gremlin-product], [docs][gremlin-docs], [licence][gremlin-licence], [editions][gremlin-editions] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `avoid_when` | `[]` | You require a fully open-source parent platform or cannot authorize controlled failure experiments on the target systems. | [product][gremlin-product], [docs][gremlin-docs], [licence][gremlin-licence], [editions][gremlin-editions] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `deployment_models` | `[]` | hosted-saas<br>self-hosted | [docs][gremlin-docs], [editions][gremlin-editions], [licence][gremlin-licence] | Record only documented deployment modes; edition/beta qualifications above apply. |
| `license_model` | unknown | commercial | [licence][gremlin-licence], [editions][gremlin-editions] | Commercial product rights established independently of pricing alone. |
| `license_spdx` | *absent* | *absent* | [licence][gremlin-licence] | Reviewed; no parent OSS grant established. Leave absent; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [licence][gremlin-licence], [editions][gremlin-editions] | Commercial product rights established independently of pricing alone. |
| `maturity` | unknown | established | [releases][gremlin-releases], [docs][gremlin-docs], [product][gremlin-product], [licence][gremlin-licence] | Reviewer judgement explained above from maintained releases/operational documentation. |
| `status` | needs-review | active | [product][gremlin-product], [docs][gremlin-docs], [releases][gremlin-releases], [licence][gremlin-licence] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |
| `repository_archived` | *absent* | *absent* | [docs][gremlin-docs], [licence][gremlin-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `alternatives` | `[]` | `[]` | [product][gremlin-product], [docs][gremlin-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `tags` | `[]` | `[]` | [product][gremlin-product], [docs][gremlin-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `verified_on` | 2026-08-03 | 2026-10-06 | [product][gremlin-product], [docs][gremlin-docs], [licence][gremlin-licence], [editions][gremlin-editions], [releases][gremlin-releases], [resilience][gremlin-resilience] | Date of this actual primary-source review, including retained records; not a ranking adjustment. |
| `sources` | legacy:8_Chaos-Engineering/README.md#L14<br>legacy:devopstools_final.md#L1165 | legacy:8_Chaos-Engineering/README.md#L14<br>legacy:devopstools_final.md#L1165<br>https://www.gremlin.com/<br>https://www.gremlin.com/docs<br>https://www.gremlin.com/terms<br>https://www.gremlin.com/docs/platform-gremlin-private-edition<br>https://www.gremlin.com/release-notes/general<br>https://www.gremlin.com/docs/reliabillity-management-disaster-recovery-tests | [product][gremlin-product], [docs][gremlin-docs], [licence][gremlin-licence], [editions][gremlin-editions], [releases][gremlin-releases], [resilience][gremlin-resilience] | Preserve every historical provenance entry and append the primary sources actually reviewed. |
| `needs_review` | `true` | `false` | [product][gremlin-product], [docs][gremlin-docs], [releases][gremlin-releases], [licence][gremlin-licence] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |

**Changed fields:** `summary`, `categories`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_model`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`, `documentation_url`, `commercial_offering`.

### komodor

**Identity boundary:** Current official overview defines the Agentic Operation Platform: AI SRE, cost optimization and AI software operations. Control plane, SDK and agent workers are distinct. SDK/agent repositories are not the parent platform repository.

**Licensing boundary:** The official product support page explicitly refers to paid product licences; deployment docs require agreement for control-plane self-hosting; plan documentation identifies commercial platform access. Together they establish a commercial product independently of a pricing-only inference. Website Terms of Use were checked but are not treated as the platform licence.

**Lifecycle and maturity:** Detailed current production workflow, identity, approvals and deployment documentation supports an active platform. Growing is the reviewer judgement for the broadened agentic platform; control-plane self-hosting is explicitly beta, so established/blanket-GA is not asserted.

**Unresolved questions / limits:** No unresolved canonical licensing-model boundary. Exact contractual grants and deployment entitlements depend on the customer agreement, which is not public. Self-hosted workers do not mean a self-hosted control plane; the latter is beta and available only under agreement.

**Disposition: CLEAR REVIEW**

**Primary sources read:** [product][komodor-product], [docs][komodor-docs], [licence][komodor-licence], [editions][komodor-editions], [plans][komodor-plans].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | komodor | komodor | [product][komodor-product], [docs][komodor-docs] | Reviewed; preserve stable identity and history. |
| `name` | Komodor | Komodor | [product][komodor-product], [docs][komodor-docs], [licence][komodor-licence] | Reviewed; retained: exact current parent identity/capabilities; boundaries explained above. |
| `summary` | Kubernetes troubleshooting and monitoring. | Agentic operations platform for production, covering AI SRE, cost optimization and software operations with governed agent workflows. | [product][komodor-product], [docs][komodor-docs], [licence][komodor-licence] | Changed: exact current parent identity/capabilities; boundaries explained above. |
| `official_url` | https://komodor.com | https://komodor.com | [product][komodor-product], [docs][komodor-docs] | Reviewed current identity; retain official-domain entry point. |
| `repository_url` | *absent* | *absent* | [docs][komodor-docs], [licence][komodor-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `documentation_url` | *absent* | https://docs.komodor.com/ | [docs][komodor-docs] | Add the directly identified product documentation entry point; scope caveat above applies. |
| `categories` | monitoring-metrics-logs-tracing | sre-incident-response-on-call<br>monitoring-metrics-logs-tracing<br>finops-sustainability | [product][komodor-product], [docs][komodor-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `subcategories` | Kubernetes Observability & Troubleshooting | Agentic Operations & Production Reliability | [product][komodor-product], [docs][komodor-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `roles` | devops-engineer<br>site-reliability-engineer<br>observability-engineer | devops-engineer<br>site-reliability-engineer<br>observability-engineer<br>platform-engineer<br>finops-engineer | [product][komodor-product], [docs][komodor-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `lifecycle_stages` | operate<br>monitor | operate<br>monitor<br>optimize | [product][komodor-product], [docs][komodor-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `use_when` | Your team spends too much time correlating K8s events, deploys, and config changes. | You need governed AI workflows for production incidents, cloud or Kubernetes costs and software operations. | [product][komodor-product], [docs][komodor-docs], [licence][komodor-licence], [editions][komodor-editions] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `avoid_when` | A simple `kubectl` + Prometheus setup is sufficient. | You only need basic Kubernetes telemetry, or require generally available self-service installation of the entire control plane; self-hosting the control plane is beta and requires agreement. | [product][komodor-product], [docs][komodor-docs], [licence][komodor-licence], [editions][komodor-editions] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `deployment_models` | `[]` | hosted-saas<br>self-hosted | [docs][komodor-docs], [editions][komodor-editions], [licence][komodor-licence] | Record only documented deployment modes; edition/beta qualifications above apply. |
| `license_model` | unknown | commercial | [licence][komodor-licence], [editions][komodor-editions], [plans][komodor-plans] | Commercial product rights established independently of pricing alone. |
| `license_spdx` | *absent* | *absent* | [licence][komodor-licence] | Reviewed; no parent OSS grant established. Leave absent; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [licence][komodor-licence], [editions][komodor-editions], [plans][komodor-plans] | Commercial product rights established independently of pricing alone. |
| `maturity` | unknown | growing | [docs][komodor-docs], [product][komodor-product], [licence][komodor-licence] | Reviewer judgement explained above from maintained releases/operational documentation. |
| `status` | needs-review | active | [product][komodor-product], [docs][komodor-docs], [licence][komodor-licence] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |
| `repository_archived` | *absent* | *absent* | [docs][komodor-docs], [licence][komodor-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `alternatives` | `[]` | `[]` | [product][komodor-product], [docs][komodor-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `tags` | `[]` | `[]` | [product][komodor-product], [docs][komodor-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `verified_on` | 2026-08-03 | 2026-10-06 | [product][komodor-product], [docs][komodor-docs], [licence][komodor-licence], [editions][komodor-editions], [plans][komodor-plans] | Date of this actual primary-source review, including retained records; not a ranking adjustment. |
| `sources` | legacy:5_Monitoring-Observability/README.md#L28<br>legacy:devopstools_final.md#L727 | legacy:5_Monitoring-Observability/README.md#L28<br>legacy:devopstools_final.md#L727<br>https://komodor.com/<br>https://docs.komodor.com/<br>https://komodor.com/contact-us/<br>https://docs.komodor.com/get-started/deployment-methods<br>https://komodor.com/platform/pricing-and-plans/ | [product][komodor-product], [docs][komodor-docs], [licence][komodor-licence], [editions][komodor-editions], [plans][komodor-plans] | Preserve every historical provenance entry and append the primary sources actually reviewed. |
| `needs_review` | `true` | `false` | [product][komodor-product], [docs][komodor-docs], [licence][komodor-licence] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |

**Changed fields:** `summary`, `categories`, `subcategories`, `roles`, `lifecycle_stages`, `use_when`, `avoid_when`, `deployment_models`, `license_model`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`, `documentation_url`, `commercial_offering`.

### morpheus-data

**Identity boundary:** Current HPE product material supplies HPE Morpheus Software as the name, with Enterprise, Advanced and VM Essentials editions. The HPE developer portal explicitly identifies Morpheus as an HPE company. Stable id morpheus-data remains; SDKs/providers and GreenLake are not substituted for the software.

**Licensing boundary:** Current QuickSpecs expressly defines term-based licensed software rather than a fully managed SaaS deployment, with edition-specific rights and support. Public-cloud provisioning is an Enterprise capability; a component licence or community edition does not relicense the parent.

**Lifecycle and maturity:** Current versioned QuickSpecs, software release references, appliance/HA architecture and support provisions establish active and established. The current name is supported by product material, not inferred merely from acquisition news.

**Unresolved questions / limits:** No material canonical uncertainty. The old docs entry redirects to the HPE Enterprise documentation target, also linked by QuickSpecs. HPE support content requires client-side rendering, so no claim is made about unread page details. The record intentionally describes Enterprise capabilities within the current software family.

**Disposition: CLEAR REVIEW**

**Primary sources read:** [product][morpheus-data-product], [docs][morpheus-data-docs], [licence][morpheus-data-licence], [ownership][morpheus-data-ownership], [legacy_docs][morpheus-data-legacy_docs].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | morpheus-data | morpheus-data | [product][morpheus-data-product], [docs][morpheus-data-docs] | Reviewed; preserve stable identity and history. |
| `name` | Morpheus Data | HPE Morpheus Software | [product][morpheus-data-product], [docs][morpheus-data-docs], [ownership][morpheus-data-ownership], [licence][morpheus-data-licence] | Changed: exact current parent identity/capabilities; boundaries explained above. |
| `summary` | Hybrid cloud management platform. | HPE hybrid-cloud management software, with Enterprise capabilities for self-service provisioning, orchestration and governance across private and public clouds. | [product][morpheus-data-product], [docs][morpheus-data-docs], [ownership][morpheus-data-ownership], [licence][morpheus-data-licence] | Changed: exact current parent identity/capabilities; boundaries explained above. |
| `official_url` | https://morpheusdata.com | https://www.hpe.com/us/en/products/software/morpheus-software.html | [product][morpheus-data-product], [docs][morpheus-data-docs] | Use current vendor product entry point. |
| `repository_url` | *absent* | *absent* | [docs][morpheus-data-docs], [licence][morpheus-data-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `documentation_url` | *absent* | https://support.hpe.com/hpesc/public/docDisplay?docId=sd00008433en_us | [docs][morpheus-data-docs], [legacy_docs][morpheus-data-legacy_docs] | Add the directly identified product documentation entry point; scope caveat above applies. |
| `categories` | cloud-platforms-management | cloud-platforms-management | [product][morpheus-data-product], [docs][morpheus-data-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `subcategories` | Cloud Management & Migration | Hybrid Cloud Management & Orchestration | [product][morpheus-data-product], [docs][morpheus-data-docs] | Changed: reviewer taxonomy mapping of documented product capabilities. |
| `roles` | devops-engineer<br>cloud-engineer<br>platform-engineer | devops-engineer<br>cloud-engineer<br>platform-engineer | [product][morpheus-data-product], [docs][morpheus-data-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `lifecycle_stages` | deploy<br>operate<br>optimize | deploy<br>operate<br>optimize | [product][morpheus-data-product], [docs][morpheus-data-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `use_when` | You need a single pane of glass for provisioning across private and public clouds. | You need self-service hybrid-cloud provisioning and governance; select the Enterprise edition for public-cloud and broader orchestration capabilities. | [product][morpheus-data-product], [docs][morpheus-data-docs], [licence][morpheus-data-licence] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `avoid_when` | You're cloud-native with existing IaC pipelines. | You require a fully managed SaaS control plane or expect every Enterprise capability in VM Essentials. | [product][morpheus-data-product], [docs][morpheus-data-docs], [licence][morpheus-data-licence] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `deployment_models` | `[]` | self-hosted | [docs][morpheus-data-docs], [licence][morpheus-data-licence] | Record only documented deployment modes; edition/beta qualifications above apply. |
| `license_model` | unknown | commercial | [licence][morpheus-data-licence] | Commercial product rights established independently of pricing alone. |
| `license_spdx` | *absent* | *absent* | [licence][morpheus-data-licence] | Reviewed; no parent OSS grant established. Leave absent; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | `true` | [licence][morpheus-data-licence] | Commercial product rights established independently of pricing alone. |
| `maturity` | unknown | established | [docs][morpheus-data-docs], [product][morpheus-data-product], [licence][morpheus-data-licence] | Reviewer judgement explained above from maintained releases/operational documentation. |
| `status` | needs-review | active | [product][morpheus-data-product], [docs][morpheus-data-docs], [licence][morpheus-data-licence], [ownership][morpheus-data-ownership] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |
| `repository_archived` | *absent* | *absent* | [docs][morpheus-data-docs], [licence][morpheus-data-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `alternatives` | `[]` | `[]` | [product][morpheus-data-product], [docs][morpheus-data-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `tags` | `[]` | `[]` | [product][morpheus-data-product], [docs][morpheus-data-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `verified_on` | 2026-08-03 | 2026-10-06 | [product][morpheus-data-product], [docs][morpheus-data-docs], [licence][morpheus-data-licence], [ownership][morpheus-data-ownership], [legacy_docs][morpheus-data-legacy_docs] | Date of this actual primary-source review, including retained records; not a ranking adjustment. |
| `sources` | legacy:2_Cloud-Infrastructure-Serverless/README.md#L232<br>legacy:devopstools_final.md#L302 | legacy:2_Cloud-Infrastructure-Serverless/README.md#L232<br>legacy:devopstools_final.md#L302<br>https://www.hpe.com/us/en/products/software/morpheus-software.html<br>https://support.hpe.com/hpesc/public/docDisplay?docId=sd00008433en_us<br>https://www.hpe.com/us/en/collaterals/collateral.a50009231enw.html<br>https://developer.hpe.com/platform/morpheus/home/<br>https://docs.morpheusdata.com/en/latest/ | [product][morpheus-data-product], [docs][morpheus-data-docs], [licence][morpheus-data-licence], [ownership][morpheus-data-ownership], [legacy_docs][morpheus-data-legacy_docs] | Preserve every historical provenance entry and append the primary sources actually reviewed. |
| `needs_review` | `true` | `false` | [product][morpheus-data-product], [docs][morpheus-data-docs], [licence][morpheus-data-licence], [ownership][morpheus-data-ownership] | CLEAR REVIEW; keep status and review flag consistent. Active is supported by current operational/release evidence. |

**Changed fields:** `name`, `summary`, `official_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_model`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`, `documentation_url`, `commercial_offering`.

### moogsoft

**Identity boundary:** The official Moogsoft domain has Dell AIOps branding plus an HCL Moogsoft sales contact. Its documentation separates Incident Management, Moogsoft Onprem/Hosted v9 and Enterprise v8. Dell confirms a cloud-service rename. None of these facts proves that every Moogsoft edition transferred to HCL or was renamed together.

The dedicated Dell product/legal page establishes the word order **Dell APEX AIOps Incident Management**. The hosting index transposes those words; the canonical summary uses the dedicated product name. Its linked service-offering page was read directly.

**Licensing boundary:** Dell hosting/legal material establishes commercial terms for the renamed cloud/hosting services. It does not establish a single current licence/vendor boundary for the entire ambiguous Moogsoft parent record. Parent license_model and maturity remain unknown; no SPDX or repository is assigned.

**Lifecycle and maturity:** The acquisition notice establishes a completed Dell acquisition in 2023, not the current ownership of every edition. Branding changes, HTTP success and HCL contact text do not establish retirement; status remains needs-review rather than deprecated.

**Unresolved questions / limits:** Obtain an explicit current vendor/transfer and support notice for Moogsoft Onprem/Hosted and reconcile it with the renamed Dell cloud service. Until then retain the stable Moogsoft identity and official-domain entry point, with the product-family documentation portal.

**Disposition: RETAIN REVIEW — SPECIFIC UNRESOLVED BOUNDARY**

**Primary sources read:** [name][moogsoft-name], [product][moogsoft-product], [docs][moogsoft-docs], [licence][moogsoft-licence], [ownership][moogsoft-ownership], [cloud][moogsoft-cloud].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | moogsoft | moogsoft | [product][moogsoft-product], [docs][moogsoft-docs] | Reviewed; preserve stable identity and history. |
| `name` | Moogsoft | Moogsoft | [product][moogsoft-product], [docs][moogsoft-docs], [ownership][moogsoft-ownership], [licence][moogsoft-licence] | Reviewed; retained: exact current parent identity/capabilities; boundaries explained above. |
| `summary` | AI-powered incident management and observability platform. | AIOps alert-correlation and incident-management product family; its cloud service is renamed Dell APEX AIOps Incident Management, while on-premises and hosted Moogsoft boundaries remain under review. | [product][moogsoft-product], [docs][moogsoft-docs], [licence][moogsoft-licence], [ownership][moogsoft-ownership], [cloud][moogsoft-cloud], [name][moogsoft-name] | Changed: use the dedicated Dell product name; retain the unresolved parent boundary. |
| `official_url` | https://www.moogsoft.com | https://www.moogsoft.com | [product][moogsoft-product], [docs][moogsoft-docs] | Reviewed current identity; retain official-domain entry point. |
| `repository_url` | *absent* | *absent* | [docs][moogsoft-docs], [licence][moogsoft-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `documentation_url` | *absent* | https://docs.moogsoft.com/ | [docs][moogsoft-docs] | Add the directly identified product documentation entry point; scope caveat above applies. |
| `categories` | sre-incident-response-on-call | sre-incident-response-on-call | [product][moogsoft-product], [docs][moogsoft-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `subcategories` | IT Operations & Incident Management | IT Operations & Incident Management | [product][moogsoft-product], [docs][moogsoft-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `roles` | site-reliability-engineer<br>observability-engineer | site-reliability-engineer<br>observability-engineer | [product][moogsoft-product], [docs][moogsoft-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `lifecycle_stages` | operate<br>monitor | operate<br>monitor | [product][moogsoft-product], [docs][moogsoft-docs] | Reviewed; retained: reviewer taxonomy mapping of documented product capabilities. |
| `use_when` | AI-driven alert correlation and noise reduction across large alert volumes. | You need alert correlation and incident management and can confirm the applicable Moogsoft on-premises, hosted or renamed Dell cloud product. | [product][moogsoft-product], [docs][moogsoft-docs], [licence][moogsoft-licence] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `avoid_when` | Your alert volume is manageable with simple routing rules. | You require an unambiguous current supplier, product edition and support lifecycle before procurement. | [product][moogsoft-product], [docs][moogsoft-docs], [licence][moogsoft-licence] | Changed: functional selection guidance from scope and licence/deployment boundaries; not a vendor prohibition. |
| `deployment_models` | `[]` | `[]` | [docs][moogsoft-docs], [licence][moogsoft-licence] | Reviewed; leave empty rather than assert an unsupported parent-wide deployment boundary. |
| `license_model` | unknown | unknown | [licence][moogsoft-licence] | Reviewed service terms; parent scope remains unresolved. Retain unknown/absent rather than inherit service-only rights. |
| `license_spdx` | *absent* | *absent* | [licence][moogsoft-licence] | Reviewed; no parent OSS grant established. Leave absent; no component/free-tier licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [licence][moogsoft-licence] | Reviewed service terms; parent scope remains unresolved. Retain unknown/absent rather than inherit service-only rights. |
| `maturity` | unknown | unknown | [docs][moogsoft-docs], [product][moogsoft-product], [licence][moogsoft-licence] | Reviewed; unknown retained because current parent identity/lifecycle is unresolved. |
| `status` | needs-review | needs-review | [product][moogsoft-product], [docs][moogsoft-docs], [licence][moogsoft-licence], [ownership][moogsoft-ownership] | RETAIN REVIEW — SPECIFIC UNRESOLVED BOUNDARY; unresolved identity prevents clearing; no unsupported deprecation. |
| `repository_archived` | *absent* | *absent* | [docs][moogsoft-docs], [licence][moogsoft-licence] | Reviewed; no parent source repository established. Leave absent; do not invent an archival boolean or substitute a component. |
| `alternatives` | `[]` | `[]` | [product][moogsoft-product], [docs][moogsoft-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `tags` | `[]` | `[]` | [product][moogsoft-product], [docs][moogsoft-docs] | Reviewed; retain empty optional metadata. No comparative substitution or tag claim is needed for this evidence batch. |
| `verified_on` | 2026-08-03 | 2026-10-06 | [product][moogsoft-product], [docs][moogsoft-docs], [licence][moogsoft-licence], [ownership][moogsoft-ownership], [cloud][moogsoft-cloud], [name][moogsoft-name] | Date of this actual primary-source review, including the retained parent boundary. |
| `sources` | legacy:5_Monitoring-Observability/README.md#L104<br>legacy:devopstools_final.md#L821 | legacy:5_Monitoring-Observability/README.md#L104<br>legacy:devopstools_final.md#L821<br>https://www.moogsoft.com/<br>https://docs.moogsoft.com/<br>https://www.dell.com/en-us/legal/lp/cloud-and-hosting-services<br>https://www.moogsoft.com/dell-technologies-acquires-moogsoft/<br>https://www.dell.com/en-us/legal/lp/dell-apex-aiops-incident-management<br>https://www.dell.com/en-us/lp/legal/apex-ai-ops | [product][moogsoft-product], [docs][moogsoft-docs], [licence][moogsoft-licence], [ownership][moogsoft-ownership], [cloud][moogsoft-cloud], [name][moogsoft-name] | Preserve legacy provenance and append the primary product/terms/naming evidence actually read. |
| `needs_review` | `true` | `true` | [product][moogsoft-product], [docs][moogsoft-docs], [licence][moogsoft-licence], [ownership][moogsoft-ownership] | RETAIN REVIEW — SPECIFIC UNRESOLVED BOUNDARY; unresolved identity prevents clearing; no unsupported deprecation. |

**Changed fields:** `summary`, `use_when`, `avoid_when`, `verified_on`, `sources`, `documentation_url`.

## Review-debt accounting

| Signal | Before | After |
|---|---:|---:|
| canonical_records | 1425 | 1425 |
| needs_review | 794 | 786 |
| status_needs_review | 794 | 786 |
| unknown_license | 91 | 83 |
| unknown_maturity | 931 | 923 |
| missing_repository_url | 394 | 394 |
| missing_documentation_url | 930 | 920 |
| mismatches | 0 | 0 |

Selected: **10**. Cleared: **8**. Retained: **2**. Review flags and needs-review statuses both move from **794 to 786**; mismatches remain **0**. Repository absence remains unchanged and justified for these parent products. Both unknown licensing and unknown maturity decrease by eight; all ten receive scoped documentation pointers.

## Validation and full audit

The historical N2a regression test is updated only to acknowledge the authorized Gremlin/Komodor licence and review-state changes and Komodor primary-category file move. Its pinned commits, historical URL decisions and immutable ledger remain unchanged. The initial full suite exposed this stale protection (669 passed, one failure); the corrected combined Wave 4/N2a run passed all 34 tests.

Local validation commands and the fresh full strict audit figures are recorded below. Audit caches and raw reports are ignored scratch output, never committed under `reports/`.

| Exact local command | Result |
|---|---|
| `.\.venv\Scripts\python.exe -m pip install -e '.[dev]'` | PASS |
| `.\.venv\Scripts\python.exe -m scripts.python_constraints --check` | Windows: FAIL, only added colorama==0.4.6; constraints unchanged. Ubuntu CI runs this same check and its final result is reported in the PR. |
| `.\.venv\Scripts\python.exe -m ruff check scripts tests` | PASS |
| `.\.venv\Scripts\python.exe -m ruff format --check scripts tests` | PASS; 57 files formatted |
| `.\.venv\Scripts\python.exe -m pytest tests/test_wave4_evidence_review.py` | PASS; 14 tests |
| `.\.venv\Scripts\python.exe -m pytest tests/test_wave4_evidence_review.py tests/test_v022_n2a_hard_url.py` | PASS; 34 tests |
| `.\.venv\Scripts\python.exe -m pytest` | PASS; 670 tests after the historical regression correction |
| `.\.venv\Scripts\python.exe -m scripts.validate_catalog` | PASS |
| `.\.venv\Scripts\python.exe -m scripts.generate_docs` | PASS; generated from canonical data |
| `.\.venv\Scripts\python.exe -m scripts.generate_docs --check` | PASS |
| `.\.venv\Scripts\python.exe -m scripts.review_debt --root tmp/wave-4-20261006/baseline-catalog --format markdown --limit 30` | PASS; byte-identical to preserved pre-edit inventory |
| `.\.venv\Scripts\python.exe -m scripts.review_debt --format markdown --limit 30` | PASS; after inventory |
| `git diff --check` | PASS |

The constraints check first failed in the network-restricted sandbox; the network-enabled rerun isolated the Windows-only `colorama` addition. No constraints/configuration changes were made.

Fresh full audit command (cache disabled and output redirected only to protect committed reports):

```powershell
.\.venv\Scripts\python.exe -m scripts.check_links --strict --check-archived --workers 8 --cache-hours 0 --cache tmp/wave-4-20261006/final-link-cache.json --json-report tmp/wave-4-20261006/final-link-report.json --markdown-report tmp/wave-4-20261006/final-link-report.md
```

- URLs checked: **2615**.
- `blocking_new`: **0**.
- `blocking_known`: **4**.
- `strict_result`: **PASS**.
- Cache reuse: **none**; `--cache-hours 0`.
- Baseline: **unchanged**.
- Inconclusive coverage: 753 rate-limited, 356 bot-blocked, six DNS-inconclusive, two network-inconclusive, one timeout and one transient failure. This audit is not primary lifecycle evidence.
- Two historical blockers (`hoji-ai/hoji` and `ophircloud/DevOps-Projects`) returned HTTP 429. The checker calls these nonblocking; this report does not claim their underlying issues are resolved.
- The audited URL set is asserted identical to the final canonical URL set. Primary evidence URLs in `sources` were reviewed separately; the checker audits canonical official/documentation/repository pointers.

Issue #2 was read back unchanged, including timestamp `2026-10-06T16:30:40Z`. Final PR-head CI/security and review-thread state are reported in the PR and final response; this report does not assert a future CI outcome.

## Deterministic inventory snapshots

The following are the before/after `scripts.review_debt --format markdown --limit 30` snapshots. The baseline uses the preserved pre-edit canonical snapshot; no verification date is altered merely to affect ranking.

<details><summary>Before</summary>

# Catalogue review-debt inventory

Deterministic snapshot derived only from canonical YAML. The reference date is the latest `verified_on` date in the catalogue, so repeated runs against the same commit are byte-stable.

**Reference date:** 2026-10-06

## Totals

| Signal | Records |
|---|---:|
| Canonical records | 1425 |
| Records requiring review | 794 |
| Unknown licence model | 91 |
| Unknown maturity | 931 |
| Archived repositories | 11 |
| Missing repository URL | 394 |
| Missing documentation URL | 930 |
| Missing sources | 0 |

## Review debt by licence model

| Licence model | Records requiring review |
|---|---:|
| `commercial` | 2 |
| `documentation` | 97 |
| `open-core` | 55 |
| `oss` | 535 |
| `source-available` | 14 |
| `unknown` | 91 |

## Verification age

| Age from reference date | Records |
|---|---:|
| 0-30 days | 322 |
| 31-90 days | 1103 |
| 91-180 days | 0 |
| 181+ days | 0 |

## Review debt by category

| Category | Total | Requires review | Unknown licence |
|---|---:|---:|---:|
| Application and cloud security (`application-cloud-security`) | 188 | 90 | 12 |
| Artifact and package management (`artifact-package-management`) | 21 | 7 | 2 |
| Backup, disaster recovery and resilience (`backup-disaster-recovery-resilience`) | 15 | 5 | 1 |
| CD, GitOps, release and promotion (`cd-gitops-release-promotion`) | 34 | 13 | 1 |
| Chaos and performance engineering (`chaos-performance-engineering`) | 25 | 19 | 3 |
| CI, build and testing (`ci-build-testing`) | 88 | 37 | 10 |
| Cloud platforms and cloud management (`cloud-platforms-management`) | 26 | 3 | 2 |
| Configuration management (`configuration-management`) | 18 | 8 | 1 |
| Containers and image tooling (`containers-image-tooling`) | 24 | 16 | 1 |
| Databases, caching and data infrastructure (`databases-caching-data-infrastructure`) | 30 | 14 | 1 |
| Deprecated and historical tools (`deprecated-historical`) | 8 | 0 | 0 |
| Developer experience and local environments (`developer-experience-local-environments`) | 108 | 54 | 6 |
| Documentation, learning and career resources (`documentation-learning-career`) | 64 | 51 | 3 |
| Emerging and experimental tools (`emerging-experimental`) | 58 | 46 | 11 |
| FinOps and sustainability (`finops-sustainability`) | 31 | 8 | 6 |
| Foundations, Linux and scripting (`foundations-linux-scripting`) | 56 | 18 | 0 |
| IAM, secrets and certificate management (`iam-secrets-certificates`) | 44 | 23 | 3 |
| Infrastructure as Code (`infrastructure-as-code`) | 37 | 19 | 4 |
| Kubernetes distributions and operations (`kubernetes-distributions-operations`) | 151 | 74 | 2 |
| Kubernetes networking, storage and add-ons (`kubernetes-networking-storage-addons`) | 136 | 98 | 1 |
| MLOps, LLMOps and AI infrastructure (`mlops-llmops-ai-infrastructure`) | 83 | 58 | 8 |
| Monitoring, metrics, logs and tracing (`monitoring-metrics-logs-tracing`) | 102 | 62 | 6 |
| Platform engineering and internal developer platforms (`platform-engineering-idp`) | 12 | 0 | 0 |
| Policy, governance and compliance (`policy-governance-compliance`) | 5 | 0 | 0 |
| Serverless, edge and WebAssembly (`serverless-edge-webassembly`) | 10 | 3 | 0 |
| Software supply-chain security (`software-supply-chain-security`) | 17 | 4 | 0 |
| Source control and repository management (`source-control-repository-management`) | 16 | 5 | 0 |
| SRE, incident response and on-call (`sre-incident-response-on-call`) | 23 | 14 | 4 |
| Virtualization, bare metal and homelab (`virtualization-bare-metal-homelab`) | 71 | 34 | 3 |
| Workflow automation and ChatOps (`workflow-automation-chatops`) | 18 | 11 | 0 |

## Top 30 deterministic review candidates

Priority is a triage aid, not an evidence decision. Scores favor unknown licensing first, then unknown maturity, missing repository/documentation/source evidence, and stale verification. Candidates are ordered by score, then oldest verification date, then stable canonical ID.

| Score | Tool | Category | Licence | Verified | Signals |
|---:|---|---|---|---|---|
| 12 | Gremlin (`gremlin`) | `chaos-performance-engineering` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Komodor (`komodor`) | `monitoring-metrics-logs-tracing` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Kubesearch (`kubesearch`) | `artifact-package-management` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | M/Monit (`m-monit`) | `monitoring-metrics-logs-tracing` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Maintenant (`maintenant`) | `monitoring-metrics-logs-tracing` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | ManageEngine IT Operations Management (`manageengine-it-operations-management`) | `sre-incident-response-on-call` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | ManageEngine NetFlow Analyzer (`manageengine-netflow-analyzer`) | `sre-incident-response-on-call` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | ManageEngine Network Configuration Manager (`manageengine-network-configuration-manager`) | `application-cloud-security` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | MEDUSA (`medusa`) | `application-cloud-security` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | MemTest86 (`memtest86`) | `chaos-performance-engineering` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Mergify (`mergify`) | `ci-build-testing` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Migratowl (`migratowl`) | `mlops-llmops-ai-infrastructure` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Moogsoft (`moogsoft`) | `sre-incident-response-on-call` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Morpheus Data (`morpheus-data`) | `cloud-platforms-management` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Ninite (`ninite`) | `developer-experience-local-environments` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | NVIDIA DGX Cloud (`nvidia-dgx-cloud`) | `mlops-llmops-ai-infrastructure` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | OCCT (`occt`) | `chaos-performance-engineering` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Octopus Deploy (`octopus-deploy`) | `ci-build-testing` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | OrbStack (`orbstack`) | `virtualization-bare-metal-homelab` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Palo Alto Cortex Cloud (`palo-alto-cortex-cloud`) | `application-cloud-security` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | PatchMon (`patchmon`) | `sre-incident-response-on-call` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | peerd (`peerd`) | `mlops-llmops-ai-infrastructure` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Pluralith (`pluralith`) | `infrastructure-as-code` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Porter (`porter`) | `cd-gitops-release-promotion` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Portworx (`portworx`) | `kubernetes-networking-storage-addons` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | ProGet (`proget`) | `artifact-package-management` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Proxmox Datacenter Manager (`proxmox-datacenter-manager`) | `virtualization-bare-metal-homelab` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | PyCharm (`pycharm`) | `developer-experience-local-environments` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Red Hat Ansible Automation Platform (`red-hat-ansible-automation-platform`) | `configuration-management` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | RTK AI (`rtk-ai`) | `developer-experience-local-environments` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |

</details>

<details><summary>After</summary>

# Catalogue review-debt inventory

Deterministic snapshot derived only from canonical YAML. The reference date is the latest `verified_on` date in the catalogue, so repeated runs against the same commit are byte-stable.

**Reference date:** 2026-10-06

## Totals

| Signal | Records |
|---|---:|
| Canonical records | 1425 |
| Records requiring review | 786 |
| Unknown licence model | 83 |
| Unknown maturity | 923 |
| Archived repositories | 11 |
| Missing repository URL | 394 |
| Missing documentation URL | 920 |
| Missing sources | 0 |

## Review debt by licence model

| Licence model | Records requiring review |
|---|---:|
| `commercial` | 2 |
| `documentation` | 97 |
| `open-core` | 55 |
| `oss` | 535 |
| `source-available` | 14 |
| `unknown` | 83 |

## Verification age

| Age from reference date | Records |
|---|---:|
| 0-30 days | 332 |
| 31-90 days | 1093 |
| 91-180 days | 0 |
| 181+ days | 0 |

## Review debt by category

| Category | Total | Requires review | Unknown licence |
|---|---:|---:|---:|
| Application and cloud security (`application-cloud-security`) | 188 | 88 | 10 |
| Artifact and package management (`artifact-package-management`) | 21 | 7 | 2 |
| Backup, disaster recovery and resilience (`backup-disaster-recovery-resilience`) | 16 | 5 | 1 |
| CD, GitOps, release and promotion (`cd-gitops-release-promotion`) | 35 | 13 | 1 |
| Chaos and performance engineering (`chaos-performance-engineering`) | 25 | 18 | 2 |
| CI, build and testing (`ci-build-testing`) | 87 | 35 | 8 |
| Cloud platforms and cloud management (`cloud-platforms-management`) | 26 | 2 | 1 |
| Configuration management (`configuration-management`) | 19 | 8 | 1 |
| Containers and image tooling (`containers-image-tooling`) | 24 | 16 | 1 |
| Databases, caching and data infrastructure (`databases-caching-data-infrastructure`) | 30 | 14 | 1 |
| Deprecated and historical tools (`deprecated-historical`) | 8 | 0 | 0 |
| Developer experience and local environments (`developer-experience-local-environments`) | 109 | 54 | 6 |
| Documentation, learning and career resources (`documentation-learning-career`) | 64 | 51 | 3 |
| Emerging and experimental tools (`emerging-experimental`) | 58 | 46 | 11 |
| FinOps and sustainability (`finops-sustainability`) | 32 | 8 | 6 |
| Foundations, Linux and scripting (`foundations-linux-scripting`) | 56 | 18 | 0 |
| IAM, secrets and certificate management (`iam-secrets-certificates`) | 44 | 23 | 3 |
| Infrastructure as Code (`infrastructure-as-code`) | 37 | 19 | 4 |
| Kubernetes distributions and operations (`kubernetes-distributions-operations`) | 151 | 74 | 2 |
| Kubernetes networking, storage and add-ons (`kubernetes-networking-storage-addons`) | 136 | 98 | 1 |
| MLOps, LLMOps and AI infrastructure (`mlops-llmops-ai-infrastructure`) | 83 | 58 | 8 |
| Monitoring, metrics, logs and tracing (`monitoring-metrics-logs-tracing`) | 102 | 61 | 5 |
| Platform engineering and internal developer platforms (`platform-engineering-idp`) | 12 | 0 | 0 |
| Policy, governance and compliance (`policy-governance-compliance`) | 5 | 0 | 0 |
| Serverless, edge and WebAssembly (`serverless-edge-webassembly`) | 10 | 3 | 0 |
| Software supply-chain security (`software-supply-chain-security`) | 17 | 4 | 0 |
| Source control and repository management (`source-control-repository-management`) | 17 | 5 | 0 |
| SRE, incident response and on-call (`sre-incident-response-on-call`) | 24 | 14 | 4 |
| Virtualization, bare metal and homelab (`virtualization-bare-metal-homelab`) | 71 | 33 | 2 |
| Workflow automation and ChatOps (`workflow-automation-chatops`) | 18 | 11 | 0 |

## Top 30 deterministic review candidates

Priority is a triage aid, not an evidence decision. Scores favor unknown licensing first, then unknown maturity, missing repository/documentation/source evidence, and stale verification. Candidates are ordered by score, then oldest verification date, then stable canonical ID.

| Score | Tool | Category | Licence | Verified | Signals |
|---:|---|---|---|---|---|
| 12 | Kubesearch (`kubesearch`) | `artifact-package-management` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | M/Monit (`m-monit`) | `monitoring-metrics-logs-tracing` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Maintenant (`maintenant`) | `monitoring-metrics-logs-tracing` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | ManageEngine IT Operations Management (`manageengine-it-operations-management`) | `sre-incident-response-on-call` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | ManageEngine NetFlow Analyzer (`manageengine-netflow-analyzer`) | `sre-incident-response-on-call` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | MEDUSA (`medusa`) | `application-cloud-security` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | MemTest86 (`memtest86`) | `chaos-performance-engineering` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Migratowl (`migratowl`) | `mlops-llmops-ai-infrastructure` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Ninite (`ninite`) | `developer-experience-local-environments` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | OCCT (`occt`) | `chaos-performance-engineering` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | PatchMon (`patchmon`) | `sre-incident-response-on-call` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | peerd (`peerd`) | `mlops-llmops-ai-infrastructure` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Pluralith (`pluralith`) | `infrastructure-as-code` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Porter (`porter`) | `cd-gitops-release-promotion` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Portworx (`portworx`) | `kubernetes-networking-storage-addons` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | ProGet (`proget`) | `artifact-package-management` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Proxmox Datacenter Manager (`proxmox-datacenter-manager`) | `virtualization-bare-metal-homelab` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | PyCharm (`pycharm`) | `developer-experience-local-environments` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Red Hat Ansible Automation Platform (`red-hat-ansible-automation-platform`) | `configuration-management` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | RTK AI (`rtk-ai`) | `developer-experience-local-environments` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Sauce Labs Real Device Cloud (`sauce-labs-real-device-cloud`) | `ci-build-testing` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Scalr (`scalr`) | `infrastructure-as-code` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Semaphore CI (`semaphore-ci`) | `ci-build-testing` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Sematext (`sematext`) | `monitoring-metrics-logs-tracing` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Site24x7 (`site24x7`) | `monitoring-metrics-logs-tracing` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Socket (`socket`) | `application-cloud-security` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Spacelift (`spacelift`) | `infrastructure-as-code` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | Spot FinOps (`spot-finops`) | `finops-sustainability` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | StrongKey (`strongkey`) | `iam-secrets-certificates` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |
| 12 | TeamCity (`teamcity`) | `ci-build-testing` | `unknown` | 2026-08-03 | unknown-license, unknown-maturity, missing-repository-url, missing-documentation-url |

</details>

[orbstack-product]: https://orbstack.dev/
[orbstack-docs]: https://docs.orbstack.dev/
[orbstack-licence]: https://docs.orbstack.dev/legal/terms
[orbstack-editions]: https://docs.orbstack.dev/licensing
[orbstack-releases]: https://docs.orbstack.dev/release-notes
[orbstack-repository]: https://github.com/orbstack/orbstack
[octopus-deploy-product]: https://octopus.com/docs
[octopus-deploy-docs]: https://octopus.com/docs
[octopus-deploy-licence]: https://octopus.com/legal/customer-agreement
[octopus-deploy-editions]: https://octopus.com/pricing/faq
[octopus-deploy-releases]: https://octopus.com/downloads/previous
[mergify-product]: https://mergify.com/
[mergify-docs]: https://docs.mergify.com/
[mergify-licence]: https://mergify.com/tos
[mergify-editions]: https://mergify.com/pricing
[mergify-releases]: https://docs.mergify.com/changelog/
[nvidia-dgx-cloud-product]: https://www.nvidia.com/en-us/data-center/dgx-cloud/
[nvidia-dgx-cloud-docs]: https://docs.nvidia.com/dgx-cloud/run-ai/latest/overview.html
[nvidia-dgx-cloud-licence]: https://www.nvidia.com/en-us/agreements/cloud-services/service-specific-terms-for-nvidia-dgx-cloud/
[palo-alto-cortex-cloud-product]: https://www.paloaltonetworks.com/cortex/cloud
[palo-alto-cortex-cloud-docs]: https://cortex-docs.paloaltonetworks.com/cortex-cloud-docs
[palo-alto-cortex-cloud-licence]: https://cortex-docs.paloaltonetworks.com/cortex-cloud-runtime-security/get-started/understand-license-plans
[manageengine-network-configuration-manager-product]: https://www.manageengine.com/network-configuration-manager/
[manageengine-network-configuration-manager-docs]: https://www.manageengine.com/network-configuration-manager/help/
[manageengine-network-configuration-manager-licence]: https://www.manageengine.com/network-configuration-manager/license.html
[manageengine-network-configuration-manager-editions]: https://www.manageengine.com/network-configuration-manager/help/installation-getting-started.html
[manageengine-network-configuration-manager-releases]: https://www.manageengine.com/network-configuration-manager/release-notes.html
[gremlin-product]: https://www.gremlin.com/
[gremlin-docs]: https://www.gremlin.com/docs
[gremlin-licence]: https://www.gremlin.com/terms
[gremlin-editions]: https://www.gremlin.com/docs/platform-gremlin-private-edition
[gremlin-releases]: https://www.gremlin.com/release-notes/general
[gremlin-resilience]: https://www.gremlin.com/docs/reliabillity-management-disaster-recovery-tests
[komodor-product]: https://komodor.com/
[komodor-docs]: https://docs.komodor.com/
[komodor-licence]: https://komodor.com/contact-us/
[komodor-editions]: https://docs.komodor.com/get-started/deployment-methods
[komodor-plans]: https://komodor.com/platform/pricing-and-plans/
[morpheus-data-product]: https://www.hpe.com/us/en/products/software/morpheus-software.html
[morpheus-data-docs]: https://support.hpe.com/hpesc/public/docDisplay?docId=sd00008433en_us
[morpheus-data-licence]: https://www.hpe.com/us/en/collaterals/collateral.a50009231enw.html
[morpheus-data-ownership]: https://developer.hpe.com/platform/morpheus/home/
[morpheus-data-legacy_docs]: https://docs.morpheusdata.com/en/latest/
[moogsoft-product]: https://www.moogsoft.com/
[moogsoft-docs]: https://docs.moogsoft.com/
[moogsoft-licence]: https://www.dell.com/en-us/legal/lp/cloud-and-hosting-services
[moogsoft-ownership]: https://www.moogsoft.com/dell-technologies-acquires-moogsoft/
[moogsoft-cloud]: https://www.dell.com/en-us/legal/lp/dell-apex-aiops-incident-management

## Generated changes

Only the following generated files changed, all through `scripts.generate_docs`:

- `README.md`
- `docs/catalog-statistics.json`
- `docs/categories/application-cloud-security.md`
- `docs/categories/backup-disaster-recovery-resilience.md`
- `docs/categories/cd-gitops-release-promotion.md`
- `docs/categories/chaos-performance-engineering.md`
- `docs/categories/ci-build-testing.md`
- `docs/categories/cloud-platforms-management.md`
- `docs/categories/configuration-management.md`
- `docs/categories/developer-experience-local-environments.md`
- `docs/categories/finops-sustainability.md`
- `docs/categories/mlops-llmops-ai-infrastructure.md`
- `docs/categories/monitoring-metrics-logs-tracing.md`
- `docs/categories/source-control-repository-management.md`
- `docs/categories/sre-incident-response-on-call.md`
- `docs/categories/virtualization-bare-metal-homelab.md`
- `docs/lifecycle/build.md`
- `docs/lifecycle/deploy.md`
- `docs/lifecycle/develop.md`
- `docs/lifecycle/monitor.md`
- `docs/lifecycle/operate.md`
- `docs/lifecycle/optimize.md`
- `docs/lifecycle/release.md`
- `docs/lifecycle/secure.md`
- `docs/lifecycle/test.md`
- `docs/roles/cloud-engineer.md`
- `docs/roles/cloud-security-engineer.md`
- `docs/roles/developer-experience-engineer.md`
- `docs/roles/devops-engineer.md`
- `docs/roles/devsecops-engineer.md`
- `docs/roles/finops-engineer.md`
- `docs/roles/infrastructure-systems-engineer.md`
- `docs/roles/observability-engineer.md`
- `docs/roles/platform-engineer.md`
- `docs/roles/release-engineer.md`
- `docs/roles/site-reliability-engineer.md`

[moogsoft-name]: https://www.dell.com/en-us/lp/legal/apex-ai-ops

## PR review correction

The automated P2 naming comment on PR #105 was confirmed against Dell's dedicated legal/product pages. Moogsoft's cloud-product name and its current service-offering evidence URL were corrected in canonical YAML; the affected generated pages were regenerated. Parent ownership/lifecycle uncertainty remains held. The audited canonical URL set is unchanged. Focused validation was rerun; final-head CI runs the full suite again.
