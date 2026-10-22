# Wave 19 — Kubernetes operators and fleet operations: primary-source review

**Date:** 2026-10-22. **Main baseline:** `07bd19f4b37683197c9d36d6869d837816c0655b`. **Issue:** [#127](https://github.com/goozcena-gnl/devops-tools-catalog/issues/127).

Ten existing canonical entries were reviewed, with **nine provisional CLEAR decisions, one RETAIN REVIEW due to duplicate identity**. Global count 1,425 unchanged. Proposed remaining review debt 656 → 647, pending independent generator output, full pytest, strict links, CodeQL and human review.

## Decision notes

| Record | Decision | Boundary |
|---|---|---|
| `azure-service-operator` | **CLEAR (provisional)** | MIT core, Azure ARM/identity CRDs; does not replace Terraform/Bicep in all lifecycles |
| `cloudnativepg` | **CLEAR (provisional)** | Apache core; HA and backups still require restoration tests and storage planning |
| `crossplane-provider-upjet` | **RETAIN REVIEW — duplicate canonical identity** | Canonical source relocated to crossplane/upjet; generates providers rather than itself provisioning ready-made cloud resources |
| `descheduler` | **CLEAR (provisional)** | Apache core; policy-based evictions, respect budgets and disruption risk |
| `mariadb-operator` | **CLEAR (provisional)** | MIT operator code, separate database/runtime terms and recovery responsibilities |
| `openkruise` | **CLEAR (provisional)** | Direct LICENSE.md contains Apache-2.0 despite API NOASSERTION; validate workload controller versions |
| `project-sveltos` | **CLEAR (provisional)** | Apache-2.0 management/controller; protect multi-cluster credentials |
| `reloader` | **CLEAR (provisional)** | Open-core offering: Apache-2.0 OSS rollout controller; separate subscription Enterprise distribution and guarantees |
| `security-profiles-operator` | **CLEAR (provisional)** | Apache core; node/OS profile and privileges must match |
| `strimzi` | **CLEAR (provisional)** | Apache core; Kafka/KRaft/cluster storage compatibility and maintenance matter |

## Complete changed-field ledger

All list items and folded YAML strings are represented in full, with list entries joined using `; `. `∅` denotes absence.

### `azure-service-operator`

| Field | Before | After |
|---|---|---|
| `summary` | `Kubernetes operator for Azure resources.` | `Azure Service Operator reconciles Azure resources from Kubernetes custom resources using Azure Resource Manager.` |
| `use_when` | `You want to provision Azure resources (databases, storage, etc.) via Kubernetes CRDs.` | `Use Kubernetes custom resources to manage supported Azure resources with explicit identity and permission controls.` |
| `avoid_when` | `You already manage Azure infra through Terraform/Bicep or don't run on Azure.` | `Prefer Terraform/Bicep if resources must be managed independently of a Kubernetes control plane.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-22'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L72; legacy:devopstools_final.md#L533` | `legacy:4_Kubernetes-Containers/README.md#L72; legacy:devopstools_final.md#L533; https://github.com/Azure/azure-service-operator; https://github.com/Azure/azure-service-operator/blob/main/LICENSE; https://github.com/Azure/azure-service-operator/releases; https://azure.github.io/azure-service-operator/` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://azure.github.io/azure-service-operator/` |
| `license_spdx` | ∅ | `MIT` |
| `repository_archived` | ∅ | `false` |

### `cloudnativepg`

| Field | Before | After |
|---|---|---|
| `summary` | `Kubernetes operator for managing PostgreSQL clusters with high availability, backups, and day-2 operations.` | `CloudNativePG operator manages PostgreSQL clusters on Kubernetes, including HA, backups, failover and recovery workflows.` |
| `use_when` | `[]` | `Operate PostgreSQL on Kubernetes with provisioned persistent storage, tested restore plans and operator lifecycle management.` |
| `avoid_when` | `[]` | `Use managed PostgreSQL if running database HA, storage, disaster recovery and upgrades yourself is unsuitable.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-22'` |
| `sources` | `legacy:devopstools_final.md#L541` | `legacy:devopstools_final.md#L541; https://github.com/cloudnative-pg/cloudnative-pg; https://github.com/cloudnative-pg/cloudnative-pg/blob/main/LICENSE; https://github.com/cloudnative-pg/cloudnative-pg/releases; https://cloudnative-pg.io/documentation/current/` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://cloudnative-pg.io/documentation/current/` |
| `license_spdx` | ∅ | `Apache-2.0` |
| `repository_archived` | ∅ | `false` |

### `crossplane-provider-upjet`

No current-state field change is applied to this historical alias. The prior draft inadvertently assigned the already used `https://github.com/crossplane/upjet` to `crossplane-provider-upjet`, causing the schema duplicate-URL failure. All its baseline fields are restored, and the already active canonical `crossplane-upjet` in `data/tools/infrastructure-as-code.yaml` remains unchanged. Further alias reconciliation must follow the repository's migration procedure rather than creating two approved canonical records.

### `descheduler`

| Field | Before | After |
|---|---|---|
| `summary` | `Rebalance pods in Kubernetes clusters.` | `Kubernetes Descheduler evicts selected pods under configured policies to enable improved subsequent scheduling.` |
| `use_when` | `Pods become unevenly distributed after node additions, taints, or affinity changes.` | `You need policy-driven pod eviction after topology, node or placement conditions change, with disruption budgets validated.` |
| `avoid_when` | `Workloads are stateful or disruption-sensitive and can't tolerate evictions.` | `Your stateful or latency-sensitive workloads cannot tolerate the eviction risks or your use case requires immediate placement guarantees.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-22'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L84; legacy:devopstools_final.md#L549` | `legacy:4_Kubernetes-Containers/README.md#L84; legacy:devopstools_final.md#L549; https://github.com/kubernetes-sigs/descheduler; https://github.com/kubernetes-sigs/descheduler/blob/master/LICENSE; https://github.com/kubernetes-sigs/descheduler/releases` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://github.com/kubernetes-sigs/descheduler` |
| `license_spdx` | ∅ | `Apache-2.0` |
| `repository_archived` | ∅ | `false` |

### `mariadb-operator`

| Field | Before | After |
|---|---|---|
| `summary` | `Kubernetes operator for managing MariaDB lifecycle, replication, Galera clustering, backups, and upgrades.` | `MariaDB Operator reconciles MariaDB custom resources for database deployment, high availability and backup operations on Kubernetes.` |
| `use_when` | `[]` | `Run MariaDB with explicit storage, backup, recovery and upgrade procedures on Kubernetes.` |
| `avoid_when` | `[]` | `A managed MariaDB service better meets availability requirements or you lack tested database recovery processes.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-22'` |
| `sources` | `legacy:devopstools_final.md#L605` | `legacy:devopstools_final.md#L605; https://github.com/mariadb-operator/mariadb-operator; https://github.com/mariadb-operator/mariadb-operator/blob/main/LICENSE; https://github.com/mariadb-operator/mariadb-operator/releases` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://github.com/mariadb-operator/mariadb-operator` |
| `license_spdx` | ∅ | `MIT` |
| `repository_archived` | ∅ | `false` |

### `openkruise`

| Field | Before | After |
|---|---|---|
| `summary` | `Enhanced workloads for Kubernetes.` | `OpenKruise adds advanced Kubernetes workload controllers and lifecycle operations such as in-place updates and sidecar management.` |
| `use_when` | `You need advanced deployment strategies (in-place updates, canary, sidecar management) beyond native Deployments.` | `You need documented advanced rollout and workload capabilities not available from native Deployments or StatefulSets.` |
| `avoid_when` | `Standard Deployments/StatefulSets with a service mesh handle your rollout needs.` | `Standard Kubernetes workload controllers suffice or additional CRDs and webhooks exceed your operational security budget.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-22'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L127; legacy:devopstools_final.md#L616` | `legacy:4_Kubernetes-Containers/README.md#L127; legacy:devopstools_final.md#L616; https://github.com/openkruise/kruise; https://github.com/openkruise/kruise/blob/master/LICENSE.md; https://github.com/openkruise/kruise/releases; https://openkruise.io/` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://openkruise.io/` |
| `license_spdx` | ∅ | `Apache-2.0` |
| `repository_archived` | ∅ | `false` |

### `project-sveltos`

| Field | Before | After |
|---|---|---|
| `summary` | `Kubernetes add-on controller for deploying and managing Helm charts, Kustomize, and raw YAML across multi-cluster fleets from a management cluster.` | `Project Sveltos distributes and reconciles cluster add-ons, Helm charts, Kustomize resources and manifests across Kubernetes fleets.` |
| `use_when` | `[]` | `Manage add-ons across multiple clusters with protected management-cluster credentials and explicit rollout policy.` |
| `avoid_when` | `[]` | `You cannot securely grant remote cluster access or an existing GitOps controller already satisfies fleet reconciliation.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-22'` |
| `sources` | `legacy:devopstools_final.md#L621` | `legacy:devopstools_final.md#L621; https://github.com/projectsveltos/addon-controller; https://github.com/projectsveltos/addon-controller/blob/main/LICENSE; https://github.com/projectsveltos/addon-controller/releases; https://projectsveltos.io/latest/` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://projectsveltos.io/latest/` |
| `license_spdx` | ∅ | `Apache-2.0` |
| `repository_archived` | ∅ | `false` |

### `reloader`

| Field | Before | After |
|---|---|---|
| `summary` | `Kubernetes controller that watches ConfigMap/Secret changes and triggers rolling upgrades.` | `Stakater Reloader's Apache-2.0 OSS controller triggers workload rollouts on ConfigMap and Secret updates; its subscription Enterprise distribution adds hardened images, validated integrations, long-term maintenance and commercial support with SLA.` |
| `use_when` | `Your apps don't support hot-reloading config and need pod restarts on ConfigMap/Secret changes.` | `You need automatic rollout restarts for workloads that do not reload ConfigMaps or Secrets at runtime.` |
| `avoid_when` | `Your apps watch config files natively or you use k8s-sidecar for file syncing.` | `You need real hot reload without restarts or cannot tolerate automatically triggered workload rollouts.; You require Enterprise-only hardened images (standard or UBI), continuously validated Vault/OpenBao/Conjur integrations, backported fixes or SLA-backed support without an Enterprise subscription; these guarantees do not apply to the OSS controller.` |
| `license_model` | `oss` | `open-core` |
| `commercial_offering` | ∅ | `true` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-22'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L131; legacy:devopstools_final.md#L624` | `legacy:4_Kubernetes-Containers/README.md#L131; legacy:devopstools_final.md#L624; https://github.com/stakater/Reloader; https://github.com/stakater/Reloader/blob/master/LICENSE; https://github.com/stakater/Reloader/releases; https://docs.stakater.com/reloader/latest/; https://docs.stakater.com/reloader/latest/about/editions.html; https://docs.stakater.com/reloader/latest/installation/install-oss.html; https://docs.stakater.com/reloader/latest/installation/install.html` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://docs.stakater.com/reloader/latest/` |
| `license_spdx` | ∅ | `Apache-2.0` |
| `repository_archived` | ∅ | `false` |

### `security-profiles-operator`

| Field | Before | After |
|---|---|---|
| `summary` | `Kubernetes operator for managing seccomp, SELinux, and AppArmor security profiles.` | `Security Profiles Operator manages and optionally records Linux seccomp, SELinux and AppArmor profiles for Kubernetes workloads.` |
| `use_when` | `[]` | `Manage supported node security profiles across clusters with compatible Linux kernels and carefully controlled operator permissions.` |
| `avoid_when` | `[]` | `Your nodes or container runtime do not support the profile types or you cannot approve required privileged components.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-22'` |
| `sources` | `legacy:devopstools_final.md#L627` | `legacy:devopstools_final.md#L627; https://github.com/kubernetes-sigs/security-profiles-operator; https://github.com/kubernetes-sigs/security-profiles-operator/blob/main/LICENSE; https://github.com/kubernetes-sigs/security-profiles-operator/releases` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://github.com/kubernetes-sigs/security-profiles-operator` |
| `license_spdx` | ∅ | `Apache-2.0` |
| `repository_archived` | ∅ | `false` |

### `strimzi`

| Field | Before | After |
|---|---|---|
| `summary` | `Apache Kafka on Kubernetes operator.` | `Strimzi manages Apache Kafka clusters and related resources on Kubernetes via custom resources and controllers.` |
| `use_when` | `You need to run and manage Kafka clusters on Kubernetes with automated operations.` | `Run Kafka with supported Kafka/KRaft versions, tested upgrades, persistent storage and capacity planning.` |
| `avoid_when` | `A managed Kafka service (Confluent Cloud/MSK/Event Hubs) better fits your operational model.` | `Managed Kafka better meets your reliability needs or the team cannot operate broker upgrades and storage recovery.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-22'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L134; legacy:devopstools_final.md#L629` | `legacy:4_Kubernetes-Containers/README.md#L134; legacy:devopstools_final.md#L629; https://github.com/strimzi/strimzi-kafka-operator; https://github.com/strimzi/strimzi-kafka-operator/blob/main/LICENSE; https://github.com/strimzi/strimzi-kafka-operator/releases; https://strimzi.io/docs/operators/latest/overview` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://strimzi.io/docs/operators/latest/overview` |
| `license_spdx` | ∅ | `Apache-2.0` |
| `repository_archived` | ∅ | `false` |

## Corrected identity decision after initial CI

- The initial CI detected duplicate `repository_url`: `crossplane-provider-upjet` and the older active `crossplane-upjet` both resolving to `https://github.com/crossplane/upjet`.
- Reverted all edits to the Wave 19 `crossplane-provider-upjet` record to its original main version. **Retain `status: needs-review` / `needs_review: true`** pending canonical alias reconciliation. Keep its legacy source pointers unchanged.
- The reviewed active `crossplane-upjet` in Infrastructure as Code is preserved; neither deleted nor edited. The total canonical inventory remains 1,425.
- Corrected proposed review debt: **656 → 647 (9 clear / 1 retained)**.

## Reloader P2 correction — 2026-10-22

Addresses [Codex's P2 comment in PR #128](https://github.com/goozcena-gnl/devops-tools-catalog/pull/128#discussion_r4349865665), against pre-fix HEAD `1f74692873021cab1a7c0aba463803de471b85f9`. Only canonical ID `reloader` changes in this correction.

Primary sources checked directly:

- [Upstream LICENSE](https://github.com/stakater/Reloader/blob/master/LICENSE): Apache License version 2.0 for the OSS controller; retain `license_spdx: Apache-2.0`.
- [OSS installation](https://docs.stakater.com/reloader/latest/installation/install-oss.html): freely available controller via public Helm chart, manifests or Kustomize.
- [Official edition comparison](https://docs.stakater.com/reloader/latest/about/editions.html): shared reload functionality; Enterprise adds standard/UBI hardened images, vulnerability scanning, continuously validated Vault/OpenBao/Conjur integrations, maintenance with backports, and commercial support with SLA. OSS integration compatibility does not include these Enterprise guarantees.
- [Enterprise installation](https://docs.stakater.com/reloader/latest/installation/install.html): active subscription and private image registry access; uses the OSS chart with Enterprise image overrides.

Following [catalogue methodology](../methodology.md#licence-and-offering-model) and existing NGINX distribution records, `license_model: open-core` classifies the combined offering; `commercial_offering: true` records the subscription distribution. This is supported by a separately distributed Enterprise image, not merely paid support for the unchanged OSS artifact. Apache-2.0 applies to the upstream OSS code; no Enterprise image licence or contractual SLA duration is inferred. The summary and selection guidance now state that boundary explicitly, so `needs_review: false` remains justified. Crossplane alias reconciliation stays open and review-debt counts remain unchanged.

### Correction validation and scope

- Used Python 3.12.14 and the existing Windows virtual environment. `python -m pip install -e '.[dev]'` and `python -m pip check` passed. The optional lock verifier found that this Windows environment differs from CI's locked package set; no dependency or lock files were changed. Locked Linux verification remains a CI gate.
- Ran `python -m scripts.generate_docs`; only the expected eight derived views changed: README, category, three roles, two lifecycle views and JSON statistics. Model totals change from OSS 934 / open-core 114 to OSS 933 / open-core 115. Total records, active records and review debt stay unchanged.
- `python -m ruff check scripts tests`, `python -m ruff format --check scripts tests` (69 files), `python -m scripts.generate_docs --check`, `python -m scripts.validate_catalog` and `git diff --check` passed on a clean local checkout containing byte-identical corrected files. The isolated checkout avoids pre-existing ignored `tmp/` artifacts in the original workspace; nothing in those artifacts was changed. Local `origin/main` was refreshed to the actual PR base for historical scope checks.
- Full `python -m pytest` with explicit external `--basetemp` and `-o cache_dir` paths passed: **999 passed, 8 skipped** in 326.90 seconds. All tests were collected; no test selection or skip override was used. Temporary/cache paths were supplied to avoid Windows ACL failures and the scanner's intentionally ignored directory names.
- Scope inspection confirms exactly five changed fields on canonical ID `reloader`: `summary`, `avoid_when`, `license_model`, `commercial_offering`, `sources`. The complete correction contains ten files: that YAML file, this report and eight generated views. No workflow, taxonomy, schema, migration, audit baseline, test or other canonical record changes.
- Network checks: the four Reloader primary sources above were inspected directly. The full network link audit was not rerun for this correction; the prior successful audit applies to pre-fix SHA `1f74692873021cab1a7c0aba463803de471b85f9`. Audited `official_url`, `repository_url` and `documentation_url` values are unchanged; newly added evidence-only `sources` URLs are outside the link audit's scope. The six known blockers in issue #2 remain open.

## Historical outstanding gates and qualifications (before initial PR validation)

- The current branch includes canonical edits only; derived documentation must be generated using the repository's own `python -m scripts.generate_docs`, committed and verified by `--check`. Do not manually guess generated pages.
- Locked Python dependencies, Ruff, full pytest, catalogue schema/metadata, historical N1a/N2a constraints and whitespace checks are pending.
- Full link audit must run on the **final branch SHA** with `strict_result: PASS`, `blocking_new: 0`, six known blockers reconciled and no TLS/baseline suppression.
- `scripts.check_links` validates canonical `official_url`, `repository_url`, `documentation_url` but not `sources`; source-only license files require independent direct evidence.
- If CI or Codex reveals a material gap, keep the affected record flagged for review rather than forcing ten clearances.
- No merge, release or closure of issue #127/#2 before human maintainer approval and post-merge verification.
