# Wave 19 — Kubernetes operators and fleet operations: primary-source review

**Date:** 2026-10-22. **Main baseline:** `07bd19f4b37683197c9d36d6869d837816c0655b`. **Issue:** [#127](https://github.com/goozcena-gnl/devops-tools-catalog/issues/127).

Ten existing canonical entries were reviewed, with **ten provisional CLEAR decisions**. Global count 1,425 unchanged. Proposed remaining review debt 656 → 646, pending independent generator output, full pytest, strict links, CodeQL and human review.

## Decision notes

| Record | Decision | Boundary |
|---|---|---|
| `azure-service-operator` | **CLEAR (provisional)** | MIT core, Azure ARM/identity CRDs; does not replace Terraform/Bicep in all lifecycles |
| `cloudnativepg` | **CLEAR (provisional)** | Apache core; HA and backups still require restoration tests and storage planning |
| `crossplane-provider-upjet` | **CLEAR (provisional)** | Canonical source relocated to crossplane/upjet; generates providers rather than itself provisioning ready-made cloud resources |
| `descheduler` | **CLEAR (provisional)** | Apache core; policy-based evictions, respect budgets and disruption risk |
| `mariadb-operator` | **CLEAR (provisional)** | MIT operator code, separate database/runtime terms and recovery responsibilities |
| `openkruise` | **CLEAR (provisional)** | Direct LICENSE.md contains Apache-2.0 despite API NOASSERTION; validate workload controller versions |
| `project-sveltos` | **CLEAR (provisional)** | Apache-2.0 management/controller; protect multi-cluster credentials |
| `reloader` | **CLEAR (provisional)** | Apache-2.0 rollout trigger, not in-process hot reload |
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

| Field | Before | After |
|---|---|---|
| `summary` | `Build Crossplane providers from Terraform.` | `Upjet generates Crossplane provider implementations from Terraform provider schemas and supports provider runtime integration.` |
| `repository_url` | `https://github.com/upbound/upjet` | `https://github.com/crossplane/upjet` |
| `use_when` | `You want to reuse existing Terraform providers as Crossplane managed resources.` | `You need to author or maintain Crossplane providers based on supported Terraform provider schemas.` |
| `avoid_when` | `A native Crossplane provider already exists for your target service.` | `You need an already packaged Crossplane provider rather than a provider code-generation framework.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-22'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L82; legacy:devopstools_final.md#L546` | `legacy:4_Kubernetes-Containers/README.md#L82; legacy:devopstools_final.md#L546; https://github.com/crossplane/upjet; https://github.com/crossplane/upjet/blob/main/LICENSE; https://github.com/crossplane/upjet/releases` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://github.com/crossplane/upjet` |
| `license_spdx` | ∅ | `Apache-2.0` |
| `repository_archived` | ∅ | `false` |

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
| `summary` | `Kubernetes controller that watches ConfigMap/Secret changes and triggers rolling upgrades.` | `Stakater Reloader watches selected ConfigMap and Secret updates and triggers workload rollouts so pods pick up changed configuration.` |
| `use_when` | `Your apps don't support hot-reloading config and need pod restarts on ConfigMap/Secret changes.` | `You need automatic rollout restarts for workloads that do not reload ConfigMaps or Secrets at runtime.` |
| `avoid_when` | `Your apps watch config files natively or you use k8s-sidecar for file syncing.` | `You need real hot reload without restarts or cannot tolerate automatically triggered workload rollouts.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-22'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L131; legacy:devopstools_final.md#L624` | `legacy:4_Kubernetes-Containers/README.md#L131; legacy:devopstools_final.md#L624; https://github.com/stakater/Reloader; https://github.com/stakater/Reloader/blob/master/LICENSE; https://github.com/stakater/Reloader/releases; https://docs.stakater.com/reloader/latest/` |
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

## Outstanding gates and qualifications

- The current branch includes canonical edits only; derived documentation must be generated using the repository's own `python -m scripts.generate_docs`, committed and verified by `--check`. Do not manually guess generated pages.
- Locked Python dependencies, Ruff, full pytest, catalogue schema/metadata, historical N1a/N2a constraints and whitespace checks are pending.
- Full link audit must run on the **final branch SHA** with `strict_result: PASS`, `blocking_new: 0`, six known blockers reconciled and no TLS/baseline suppression.
- `scripts.check_links` validates canonical `official_url`, `repository_url`, `documentation_url` but not `sources`; source-only license files require independent direct evidence.
- If CI or Codex reveals a material gap, keep the affected record flagged for review rather than forcing ten clearances.
- No merge, release or closure of issue #127/#2 before human maintainer approval and post-merge verification.
