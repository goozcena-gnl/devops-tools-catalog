# Wave 20 — Observability and SRE independent evidence review

**Reviewed:** 2026-10-22. **Main baseline:** `0af956384ed33211352b249cf4c1f0d84795e168`. **PR:** [#130](https://github.com/goozcena-gnl/devops-tools-catalog/pull/130). **Issue:** [#129](https://github.com/goozcena-gnl/devops-tools-catalog/issues/129).

The initial draft at `ba21b208b921b341e85af992119ade8756875bdf` was independently rechecked against official documentation, upstream licence grants and source headers, and release metadata. All ten existing canonical IDs remain in scope; no IDs were added or removed. **Seven CLEAR decisions, three RETAIN REVIEW decisions.** Canonical inventory remains 1,425 across 30 categories; review debt 647 → 640 and active records 764 → 771. CLEAR describes the evidence decision, not permission to merge: **PR #130 must remain unmerged until human approval.**

## Independent field-level decisions and evidence

| ID | Decision | Offering and SPDX boundary |
|---|---|---|
| `elastic-stack-elk` | RETAIN REVIEW | `source-available`, commercial; no universal Stack SPDX; component/distribution mapping remains open |
| `icinga` | CLEAR | `oss`; `GPL-3.0-or-later` for Icinga 2 releases from 2.16.0, not a retrospective grant for every file/component |
| `influxdata` | CLEAR | `open-core`, commercial; no brand-wide SPDX; InfluxDB 3 Core uses MIT OR Apache-2.0 |
| `krr` | CLEAR | `oss`, `MIT` CLI; explicitly separate optional mutation by KRR Enforcer |
| `kubewatch` | CLEAR | `oss`, `Apache-2.0`; Robusta-maintained event notification tool |
| `netdata-cloud` | CLEAR | `free-saas`, commercial; no Agent SPDX copied onto the proprietary Cloud/UI |
| `rsyslog` | RETAIN REVIEW | `oss`; verified Apache daemon / LGPL runtime headers, aggregate SPDX unresolved |
| `sentry` | CLEAR | `source-available`, commercial; current server FSL with a version-specific future Apache grant |
| `tracetest` | RETAIN REVIEW | `open-core`; per-file MIT/TCL and current support remain unresolved |
| `zabbix` | CLEAR | `oss`, `AGPL-3.0-only` for software from 7.0; older GPL-2.0-or-later and documentation terms are distinct |

### Icinga — version and file applicability

The [v2.16.5 README licence section](https://github.com/Icinga/icinga2/blob/v2.16.5/README.md#license) expressly grants GPL version 3 or later for Icinga 2 and its documentation, effective from 2.16.0 because of Apache-2.0 dependencies. It also expressly preserves GPLv2+ for earlier releases and existing source files. The [tagged GPLv3 text](https://github.com/Icinga/icinga2/blob/v2.16.5/LICENSE.md) is corroborating evidence; the grant in the README, rather than GPL boilerplate alone, supports `GPL-3.0-or-later`. The [application.cpp header](https://github.com/Icinga/icinga2/blob/v2.16.5/lib/base/application.cpp) confirms `GPL-2.0-or-later` still appears on individual files. The summary now states this boundary. Web, DB and Director are separately deployed components, not relicensed by this record. [Distributed-monitoring documentation](https://icinga.com/docs/icinga-2/latest/doc/06-distributed-monitoring/) supports the API, certificate and trust-zone cautions. Upstream [v2.16.5 release](https://github.com/Icinga/icinga2/releases/tag/v2.16.5) and non-archived repository support active status.

### Zabbix — AGPL-only grant and historical GPL versions

The [official licensing policy](https://www.zabbix.com/license) scopes AGPLv3 to software from 7.0 and distinguishes versions through 6.4; its FAQ explicitly describes the historical GPLv2-or-later grant. The [current README](https://github.com/zabbix/zabbix/blob/master/README.md#license) explicitly names `AGPL-3.0-only`; both the [7.0.0 server header](https://github.com/zabbix/zabbix/blob/7.0.0/src/zabbix_server/server.c) and [current server header](https://github.com/zabbix/zabbix/blob/master/src/zabbix_server/server.c) grant version 3 without an or-later clause. This supports `AGPL-3.0-only`, not `AGPL-3.0-or-later`. The same policy gives documentation separate terms, now stated in the summary. [Current 7.4 documentation](https://www.zabbix.com/documentation/current/en/manual/introduction/about) supports server/proxy/agent scope and current product status; the GitHub repository is not archived. GitHub has no latest-release object, so that absence is not treated as inactivity or used to invent a release date.

### InfluxData — Core, commercial products and query generations

The [v3.12.1 README](https://github.com/influxdata/influxdb/blob/v3.12.1/README.md), [MIT licence](https://github.com/influxdata/influxdb/blob/v3.12.1/LICENSE-MIT) and [Apache licence](https://github.com/influxdata/influxdb/blob/v3.12.1/LICENSE-APACHE) establish the Core dual choice. This broad InfluxData record also covers separate Enterprise/Cloud products, so no universal `license_spdx` is added. [Which InfluxDB 3](https://docs.influxdata.com/influxdb3/which-influxdb-3/) distinguishes single-node Core from Enterprise HA, maintenance/support and managed offerings, and describes v1/v2 as previous generations in maintenance. [Identify version](https://docs.influxdata.com/platform/identify-version/) confirms different API surfaces. The identification table mentions Flux for Cloud Serverless, while the product guide says it is not officially supported or optimized for v3; the summary therefore says **no official Flux support**, rather than claiming every compatibility path cannot execute it. v2 Flux queries require migration planning. [v3.12.1](https://github.com/influxdata/influxdb/releases/tag/v3.12.1) was published 2026-10-15; repository not archived.

### Netdata Cloud — service, Agent, UI and On-Premises

The [tagged architecture and licence table](https://github.com/netdata/netdata/blob/v2.12.1/README.md) assigns GPLv3+ to the Agent, identifies Cloud separately, and links the [NCUL1 UI terms](https://app.netdata.cloud/LICENSE.txt), which restrict use to Netdata components and do not grant a general open-source UI licence. [Cloud SaaS](https://www.netdata.cloud/product/netdata-cloud-saas/) documents a control plane with telemetry retained on Agents/Parents. [Pricing](https://www.netdata.cloud/pricing/) confirms a personal/non-commercial Community free tier and paid plans; `free-saas` plus `commercial_offering: true` describes the hosted entry, without applying Agent GPL to Cloud. The initial statement implying Cloud cannot be self-hosted was incorrect: [commercial Cloud On-Premises](https://www.netdata.cloud/product/cloud-on-premises/) explicitly supports private and air-gapped deployment. Summary and avoidance criteria now acknowledge that separate option. No single Cloud SPDX is asserted. Agent [v2.12.1](https://github.com/netdata/netdata/releases/tag/v2.12.1) and its archive flag apply to the distinct Agent repository, cited only as primary supporting evidence instead of the Cloud service's canonical source.

### Sentry — current restriction and version-specific future grant

The [26.10.0 server licence](https://github.com/getsentry/sentry/blob/26.10.0/LICENSE.md) names FSL-1.1-Apache-2.0. It permits internal use, restricts competing commercial uses, and grants Apache-2.0 to each covered version on the second anniversary of its availability. A future grant does not make the current server immediately Apache-licensed; `source-available` is retained and the competing-use/two-year boundary is explicit. Hosted commercial plans and self-hosted dependencies are separate concerns. No universal server/dependency `license_spdx` is inferred. SPDX calls the corresponding standard text [FSL-1.1-ALv2](https://spdx.org/licenses/FSL-1.1-ALv2.html); the upstream abbreviation is preserved in prose rather than incorrectly writing it as a standardized SPDX identifier. [26.10.0](https://github.com/getsentry/sentry/releases/tag/26.10.0) was published 2026-10-16; repository not archived.

### KRR and Kubewatch — verify actual operational behavior

KRR's [v1.31.1 MIT grant](https://github.com/robusta-dev/krr/blob/v1.31.1/LICENSE) and [README](https://github.com/robusta-dev/krr/blob/v1.31.1/README.md) support the recommendation CLI and Prometheus-compatible data requirements. The [KRR Enforcer README](https://github.com/robusta-dev/krr/blob/v1.31.1/enforcer/README.md) shows optional automatic mutation of pod requests/limits at creation. Guidance now names this upstream component instead of implying automation only exists outside KRR. Optional Robusta SaaS is not mistaken for the CLI licence. Kubewatch's [v2.16.1 README](https://github.com/robusta-dev/kubewatch/blob/v2.16.1/README.md) explicitly identifies Robusta as maintainer after Bitnami, resource-change notifications and channel handlers; the [tagged licence](https://github.com/robusta-dev/kubewatch/blob/v2.16.1/LICENSE) is Apache-2.0. RBAC and delivery-endpoint cautions reflect those data flows. [KRR v1.31.1](https://github.com/robusta-dev/krr/releases/tag/v1.31.1) was published 2026-10-19; [Kubewatch v2.16.1](https://github.com/robusta-dev/kubewatch/releases/tag/v2.16.1) on 2026-08-24. Both repositories are not archived.

### Retained cases — uncertainty remains explicit

- **Elastic Stack:** [Elasticsearch LICENSE](https://github.com/elastic/elasticsearch/blob/main/LICENSE.txt), [Kibana LICENSE](https://github.com/elastic/kibana/blob/main/LICENSE.txt), [Logstash LICENSE](https://github.com/elastic/logstash/blob/main/LICENSE.txt) and the [vendor FAQ](https://www.elastic.co/pricing/faq/licensing) establish per-file AGPL-3.0-only/SSPL/ELv2 and Apache-compatible or Apache portions, with different x-pack and distribution boundaries. Elasticsearch [v9.5.5](https://github.com/elastic/elasticsearch/releases/tag/v9.5.5), published 2026-10-06, proves a current release but does not establish one Stack-wide SPDX or distribution map. Preserve `needs_review: true`, `status: needs-review`; no aggregate SPDX.
- **rsyslog:** [v8.2610.0 daemon header](https://github.com/rsyslog/rsyslog/blob/v8.2610.0/tools/rsyslogd.c) is Apache-2.0, [runtime header](https://github.com/rsyslog/rsyslog/blob/v8.2610.0/runtime/rsyslog.h) is LGPL-3.0-or-later, and [COPYING.ASL20](https://github.com/rsyslog/rsyslog/blob/v8.2610.0/COPYING.ASL20), GPL COPYING and LGPL COPYING.LESSER coexist. The summary corrects the initial GPL/LGPL-only implication. [README](https://github.com/rsyslog/rsyslog/blob/v8.2610.0/README.md) and [2026-10-20 release](https://github.com/rsyslog/rsyslog/releases/tag/v8.2610.0) support operation and recent upstream activity, but no complete per-component licensing inventory was established. Preserve review debt and omit aggregate SPDX.
- **Tracetest:** the [root licence](https://github.com/kubeshop/tracetest/blob/main/LICENSE) specifies per-file MIT/TCL applicability, overriding any broad MIT badge in the [README](https://github.com/kubeshop/tracetest/blob/main/README.md). The latest stable release returned by the upstream release API remains [v1.7.1, 2024-10-10](https://github.com/kubeshop/tracetest/releases/tag/v1.7.1). The repository is not archived, but this alone does not prove current support. Preserve review debt and omit aggregate SPDX; a successful URL audit would not clear this lifecycle uncertainty.

## Complete baseline-to-final changed-field ledger

Every changed canonical field is represented below, with full list values and no dropped legacy pointers. `∅` means absent. Fields not listed are unchanged from the main baseline. The before/after values are computed from parsed canonical YAML, not manually copied summaries.

### `elastic-stack-elk`

| Field | Before | After |
|---|---|---|
| `summary` | `"Search/analytics/log platform; source licensing varies by component (Elastic License/SSPL and AGPL option for parts)."` | `"Elastic Stack combines Elasticsearch search and analytics with separate Kibana and Logstash components; Elasticsearch source has file-dependent AGPLv3, SSPL and Elastic License terms, not one Stack-wide licence."` |
| `use_when` | `["Powerful full-text search and analytics over logs."]` | `["You need full-text search and log analytics and can check each deployed component and distribution."]` |
| `avoid_when` | `["Licensing concerns, high cost of running Elasticsearch, or you only need label-based log queries (Loki is simpler)."]` | `["You require one permissive Stack-wide licence; source options, x-pack files and shipped distributions have different terms.", "A simpler log or metrics stack meets the requirement."]` |
| `maturity` | `"unknown"` | `"established"` |
| `verified_on` | `"2026-08-03"` | `"2026-10-22"` |
| `sources` | `["legacy:5_Monitoring-Observability/README.md#L54", "legacy:devopstools_final.md#L761"]` | `["legacy:5_Monitoring-Observability/README.md#L54", "legacy:devopstools_final.md#L761", "https://github.com/elastic/elasticsearch/blob/main/LICENSE.txt", "https://github.com/elastic/elasticsearch/releases/tag/v9.5.5", "https://www.elastic.co/pricing/faq/licensing", "https://github.com/elastic/kibana/blob/main/LICENSE.txt", "https://github.com/elastic/logstash/blob/main/LICENSE.txt"]` |
| `repository_archived` | ∅ | `false` |

### `icinga`

| Field | Before | After |
|---|---|---|
| `summary` | `"Open source monitoring system derived from Nagios."` | `"Icinga 2 monitors hosts and services with checks, notifications, an API and distributed zones. Releases from 2.16.0 use GPL-3.0-or-later; earlier releases and existing file-level grants retain GPL-2.0-or-later. Web, DB and Director are separate components."` |
| `use_when` | `["You want Nagios-style host/service checks with a modern API and HA."]` | `["You need distributed host and service checks with managed API access, certificates and alerting."]` |
| `avoid_when` | `["You need metrics-first or tracing-centric observability."]` | `["You expect Icinga 2 alone to contain Icinga Web, DB and Director.", "You cannot secure API users, certificates and cluster trust zones."]` |
| `maturity` | `"unknown"` | `"established"` |
| `status` | `"needs-review"` | `"active"` |
| `verified_on` | `"2026-08-03"` | `"2026-10-22"` |
| `sources` | `["legacy:5_Monitoring-Observability/README.md#L12", "legacy:devopstools_final.md#L706"]` | `["legacy:5_Monitoring-Observability/README.md#L12", "legacy:devopstools_final.md#L706", "https://github.com/Icinga/icinga2/blob/master/README.md", "https://github.com/Icinga/icinga2/blob/master/LICENSE.md", "https://github.com/Icinga/icinga2/releases/tag/v2.16.5", "https://icinga.com/docs/icinga-2/latest/doc/06-distributed-monitoring/", "https://github.com/Icinga/icinga2/blob/v2.16.5/README.md", "https://github.com/Icinga/icinga2/blob/v2.16.5/LICENSE.md", "https://github.com/Icinga/icinga2/blob/v2.16.5/lib/base/application.cpp"]` |
| `needs_review` | `true` | `false` |
| `license_spdx` | ∅ | `"GPL-3.0-or-later"` |
| `documentation_url` | ∅ | `"https://icinga.com/docs/icinga-2/latest/"` |
| `repository_archived` | ∅ | `false` |

### `influxdata`

| Field | Before | After |
|---|---|---|
| `summary` | `"Time series platform with OSS components and commercial cloud/enterprise offerings."` | `"InfluxData offers InfluxDB 3 Core under MIT or Apache-2.0 and separate commercial Enterprise and Cloud products. Version 3 supports SQL and InfluxQL without official Flux support; older v1/v2 products have different APIs and query-language support."` |
| `use_when` | `["IoT/sensor-heavy time series with Flux query language."]` | `["You need time-series ingest and analytics and can select the specific version, topology and supported query language."]` |
| `avoid_when` | `["Prometheus-compatible ecosystem or PromQL is your standard."]` | `["You rely on Flux without migrating InfluxDB 2 queries to InfluxDB 3 SQL or InfluxQL.", "You expect free single-node Core to provide Enterprise HA or managed cloud capabilities."]` |
| `maturity` | `"unknown"` | `"established"` |
| `status` | `"needs-review"` | `"active"` |
| `verified_on` | `"2026-08-03"` | `"2026-10-22"` |
| `sources` | `["legacy:5_Monitoring-Observability/README.md#L44", "legacy:devopstools_final.md#L749"]` | `["legacy:5_Monitoring-Observability/README.md#L44", "legacy:devopstools_final.md#L749", "https://github.com/influxdata/influxdb/blob/main/LICENSE-MIT", "https://github.com/influxdata/influxdb/blob/main/LICENSE-APACHE", "https://github.com/influxdata/influxdb/releases/tag/v3.12.1", "https://docs.influxdata.com/platform/identify-version/", "https://docs.influxdata.com/influxdb3/which-influxdb-3/", "https://github.com/influxdata/influxdb/blob/v3.12.1/README.md", "https://github.com/influxdata/influxdb/blob/v3.12.1/LICENSE-MIT", "https://github.com/influxdata/influxdb/blob/v3.12.1/LICENSE-APACHE"]` |
| `needs_review` | `true` | `false` |
| `commercial_offering` | ∅ | `true` |
| `documentation_url` | ∅ | `"https://docs.influxdata.com/platform/"` |
| `repository_archived` | ∅ | `false` |

### `krr`

| Field | Before | After |
|---|---|---|
| `summary` | `"Kubernetes Resource Recommendations by Robusta."` | `"Robusta KRR's MIT-licensed CLI analyzes Prometheus-compatible telemetry and recommends Kubernetes CPU and memory requests and limits; the optional KRR Enforcer webhook automatically applies recommendations when pods are created."` |
| `use_when` | `["Right-sizing pod requests/limits based on real usage data."]` | `["You have representative Prometheus-compatible resource usage history and want to review pod right-sizing proposals."]` |
| `avoid_when` | `["VPA already handles your resource tuning needs."]` | `["You lack representative metrics or cannot approve the resource mutations introduced by the optional KRR Enforcer.", "You cannot review recommendation accuracy and disruption risks before applying changes."]` |
| `maturity` | `"unknown"` | `"established"` |
| `status` | `"needs-review"` | `"active"` |
| `verified_on` | `"2026-08-03"` | `"2026-10-22"` |
| `sources` | `["legacy:5_Monitoring-Observability/README.md#L29", "legacy:devopstools_final.md#L729"]` | `["legacy:5_Monitoring-Observability/README.md#L29", "legacy:devopstools_final.md#L729", "https://github.com/robusta-dev/krr/blob/main/LICENSE", "https://github.com/robusta-dev/krr/releases/tag/v1.31.1", "https://github.com/robusta-dev/krr/blob/main/README.md", "https://github.com/robusta-dev/krr/blob/v1.31.1/LICENSE", "https://github.com/robusta-dev/krr/blob/v1.31.1/README.md", "https://github.com/robusta-dev/krr/blob/v1.31.1/enforcer/README.md"]` |
| `needs_review` | `true` | `false` |
| `license_spdx` | ∅ | `"MIT"` |
| `documentation_url` | ∅ | `"https://github.com/robusta-dev/krr/blob/main/README.md"` |
| `repository_archived` | ∅ | `false` |

### `kubewatch`

| Field | Before | After |
|---|---|---|
| `summary` | `"Kubernetes event watcher and notifier."` | `"Robusta-maintained Kubewatch watches selected Kubernetes resource changes and sends notifications to configured handlers and collaboration channels."` |
| `use_when` | `["You want Slack/webhook alerts on K8s resource changes."]` | `["You need lightweight Kubernetes event notifications with limited watch permissions and approved delivery endpoints."]` |
| `avoid_when` | `["You already have event routing via Robusta or a full observability platform."]` | `["You need a full incident-management or telemetry correlation platform rather than object-change alerts.", "You cannot restrict RBAC scope or protect metadata sent to external channels."]` |
| `maturity` | `"unknown"` | `"established"` |
| `status` | `"needs-review"` | `"active"` |
| `verified_on` | `"2026-08-03"` | `"2026-10-22"` |
| `sources` | `["legacy:5_Monitoring-Observability/README.md#L31", "legacy:devopstools_final.md#L732"]` | `["legacy:5_Monitoring-Observability/README.md#L31", "legacy:devopstools_final.md#L732", "https://github.com/robusta-dev/kubewatch/blob/master/LICENSE", "https://github.com/robusta-dev/kubewatch/blob/master/README.md", "https://github.com/robusta-dev/kubewatch/releases/tag/v2.16.1", "https://github.com/robusta-dev/kubewatch/blob/v2.16.1/LICENSE", "https://github.com/robusta-dev/kubewatch/blob/v2.16.1/README.md"]` |
| `needs_review` | `true` | `false` |
| `license_spdx` | ∅ | `"Apache-2.0"` |
| `documentation_url` | ∅ | `"https://github.com/robusta-dev/kubewatch/blob/master/README.md"` |
| `repository_archived` | ∅ | `false` |

### `netdata-cloud`

| Field | Before | After |
|---|---|---|
| `repository_url` | `"https://github.com/netdata/netdata"` | ∅ |
| `summary` | `"SaaS control plane for Netdata (Netdata Agent is open-source; Cloud adds centralized management/collaboration)."` | `"Netdata Cloud's proprietary hosted control plane has a personal non-commercial free tier and paid plans; telemetry stays on separate GPL-3.0-or-later Agents and Parents. The UI uses NCUL1, and commercial Cloud On-Premises is a separate deployment option."` |
| `use_when` | `["You want per-second granularity with near-zero config."]` | `["You need hosted access and collaborative monitoring across agents and accept Netdata Cloud account and network dependencies."]` |
| `avoid_when` | `["Long-term storage or complex cross-service correlation is the main goal."]` | `["You require an entirely OSI-licensed Cloud service and UI; the Agent's GPL licence does not cover either.", "You need an air-gapped control plane without evaluating commercial Cloud On-Premises, or cannot approve Cloud data flows and plan limits; Netdata Agent's repository is cited only as supporting evidence, not as the source for Cloud."]` |
| `license_model` | `"open-core"` | `"free-saas"` |
| `maturity` | `"unknown"` | `"established"` |
| `status` | `"needs-review"` | `"active"` |
| `verified_on` | `"2026-08-03"` | `"2026-10-22"` |
| `sources` | `["legacy:5_Monitoring-Observability/README.md#L16", "legacy:devopstools_final.md#L711"]` | `["legacy:5_Monitoring-Observability/README.md#L16", "legacy:devopstools_final.md#L711", "https://github.com/netdata/netdata/blob/master/README.md", "https://github.com/netdata/netdata/blob/master/LICENSE", "https://github.com/netdata/netdata/releases/tag/v2.12.1", "https://www.netdata.cloud/", "https://github.com/netdata/netdata/blob/v2.12.1/README.md", "https://www.netdata.cloud/pricing/", "https://www.netdata.cloud/product/netdata-cloud-saas/", "https://www.netdata.cloud/product/cloud-on-premises/", "https://app.netdata.cloud/LICENSE.txt"]` |
| `needs_review` | `true` | `false` |
| `commercial_offering` | ∅ | `true` |
| `documentation_url` | ∅ | `"https://learn.netdata.cloud/"` |

### `rsyslog`

| Field | Before | After |
|---|---|---|
| `summary` | `"High-performance syslog daemon with flexible routing (often used as a log edge forwarder)."` | `"rsyslog collects and routes syslog data; the checked daemon source is Apache-2.0 and its runtime header is LGPL-3.0-or-later, while aggregate component licensing still needs review."` |
| `use_when` | `["High-throughput syslog forwarding on Linux hosts."]` | `["You need configurable syslog collection, filtering and reliable forwarding on Linux systems."]` |
| `avoid_when` | `["You need structured log parsing or container-native log collection."]` | `["You need downstream log indexing, search and dashboards rather than a forwarding engine.", "You require one verified SPDX for the full project before checking file-level licensing."]` |
| `verified_on` | `"2026-10-04"` | `"2026-10-22"` |
| `sources` | `["legacy:5_Monitoring-Observability/README.md#L62", "legacy:devopstools_final.md#L770", "https://www.rsyslog.com", "https://docs.rsyslog.com/doc/", "https://github.com/rsyslog/rsyslog", "https://github.com/rsyslog/rsyslog/blob/main/README.md", "https://github.com/rsyslog/rsyslog/blob/main/COPYING.LESSER", "https://github.com/rsyslog/rsyslog/blob/main/runtime/rsyslog.h", "https://github.com/rsyslog/rsyslog/blob/main/tools/rsyslogd.c"]` | `["legacy:5_Monitoring-Observability/README.md#L62", "legacy:devopstools_final.md#L770", "https://www.rsyslog.com", "https://docs.rsyslog.com/doc/", "https://github.com/rsyslog/rsyslog", "https://github.com/rsyslog/rsyslog/blob/main/README.md", "https://github.com/rsyslog/rsyslog/blob/main/COPYING.LESSER", "https://github.com/rsyslog/rsyslog/blob/main/runtime/rsyslog.h", "https://github.com/rsyslog/rsyslog/blob/main/tools/rsyslogd.c", "https://github.com/rsyslog/rsyslog/blob/main/COPYING", "https://github.com/rsyslog/rsyslog/releases/tag/v8.2610.0", "https://github.com/rsyslog/rsyslog/blob/v8.2610.0/tools/rsyslogd.c", "https://github.com/rsyslog/rsyslog/blob/v8.2610.0/runtime/rsyslog.h", "https://github.com/rsyslog/rsyslog/blob/v8.2610.0/COPYING.ASL20", "https://github.com/rsyslog/rsyslog/blob/v8.2610.0/README.md"]` |

### `sentry`

| Field | Before | After |
|---|---|---|
| `summary` | `"Error monitoring with performance/tracing features (popular for app-level APM signals)."` | `"Sentry monitors application errors, releases and performance. Its main server source uses FSL-1.1-Apache-2.0 with a competing-use restriction and an Apache-2.0 grant effective two years after each version is made available; hosted plans are separate commercial offerings."` |
| `use_when` | `["Developer-facing error tracking with stack traces and release health."]` | `["You need application error diagnostics, performance telemetry and release-linked troubleshooting with controlled ingestion."]` |
| `avoid_when` | `["Infrastructure-level tracing or metrics monitoring is the goal."]` | `["You require an immediately OSI-licensed current server or a competing commercial service; the FSL permits internal use but restricts competing uses before each version's future Apache grant.", "You cannot govern captured data, self-hosted service dependencies or subscription limits."]` |
| `license_model` | `"open-core"` | `"source-available"` |
| `maturity` | `"unknown"` | `"established"` |
| `status` | `"needs-review"` | `"active"` |
| `verified_on` | `"2026-08-03"` | `"2026-10-22"` |
| `sources` | `["legacy:5_Monitoring-Observability/README.md#L73", "legacy:devopstools_final.md#L782"]` | `["legacy:5_Monitoring-Observability/README.md#L73", "legacy:devopstools_final.md#L782", "https://github.com/getsentry/sentry/blob/master/LICENSE.md", "https://github.com/getsentry/sentry/releases/tag/26.10.0", "https://docs.sentry.io/", "https://github.com/getsentry/sentry/blob/26.10.0/LICENSE.md"]` |
| `needs_review` | `true` | `false` |
| `commercial_offering` | ∅ | `true` |
| `documentation_url` | ∅ | `"https://docs.sentry.io/"` |
| `repository_archived` | ∅ | `false` |

### `tracetest`

| Field | Before | After |
|---|---|---|
| `summary` | `"Trace-based integration testing using OpenTelemetry, with mixed MIT/Tracetest Community licensing and unclear current support."` | `"Tracetest provides OpenTelemetry trace-based integration testing; source files have mixed MIT and Tracetest Community terms and current support remains unverified."` |
| `use_when` | `["You are evaluating assertions against distributed traces for integration and end-to-end tests."]` | `["You are testing distributed traces in a controlled evaluation and can check edition-specific and per-file licensing."]` |
| `avoid_when` | `["You require a clearly maintained and uniformly permissive production tool; source files have different license grants."]` | `["You require established current maintenance or a uniformly permissive licence; the last checked stable release is from 2024."]` |
| `verified_on` | `"2026-10-21"` | `"2026-10-22"` |
| `sources` | `["legacy:5_Monitoring-Observability/README.md#L74", "legacy:devopstools_final.md#L783", "https://github.com/kubeshop/tracetest", "https://github.com/kubeshop/tracetest/blob/main/LICENSE", "https://github.com/kubeshop/tracetest/releases", "https://docs.tracetest.io/"]` | `["legacy:5_Monitoring-Observability/README.md#L74", "legacy:devopstools_final.md#L783", "https://github.com/kubeshop/tracetest", "https://github.com/kubeshop/tracetest/blob/main/LICENSE", "https://github.com/kubeshop/tracetest/releases", "https://docs.tracetest.io/", "https://github.com/kubeshop/tracetest/releases/tag/v1.7.1", "https://github.com/kubeshop/tracetest/blob/main/README.md"]` |

### `zabbix`

| Field | Before | After |
|---|---|---|
| `summary` | `"Enterprise-grade monitoring platform (metrics, triggers, dashboards)."` | `"Zabbix monitors infrastructure with server, proxy, agent and alerting components. Software from 7.0 uses AGPL-3.0-only; releases through 6.4 use GPL-2.0-or-later. Documentation has separate terms."` |
| `use_when` | `["Large-scale traditional infra monitoring with templates and agent support."]` | `["You need broad distributed agent or agentless infrastructure monitoring, templates and configurable alerts."]` |
| `avoid_when` | `["Your workload is fully cloud-native and you prefer PromQL/OTel standards."]` | `["You assume older GPLv2 releases and current AGPLv3 have identical sharing obligations.", "You need native tracing instead of infrastructure monitoring or cannot manage Zabbix storage and access."]` |
| `maturity` | `"unknown"` | `"established"` |
| `status` | `"needs-review"` | `"active"` |
| `verified_on` | `"2026-08-03"` | `"2026-10-22"` |
| `sources` | `["legacy:5_Monitoring-Observability/README.md#L24", "legacy:devopstools_final.md#L720"]` | `["legacy:5_Monitoring-Observability/README.md#L24", "legacy:devopstools_final.md#L720", "https://github.com/zabbix/zabbix/blob/master/README.md", "https://github.com/zabbix/zabbix/blob/master/COPYING", "https://www.zabbix.com/license", "https://www.zabbix.com/documentation/current/en/manual", "https://github.com/zabbix/zabbix/blob/7.0.0/src/zabbix_server/server.c", "https://github.com/zabbix/zabbix/blob/master/src/zabbix_server/server.c", "https://www.zabbix.com/documentation/current/en/manual/introduction/about"]` |
| `needs_review` | `true` | `false` |
| `license_spdx` | ∅ | `"AGPL-3.0-only"` |
| `documentation_url` | ∅ | `"https://www.zabbix.com/documentation/current/en/manual"` |
| `repository_archived` | ∅ | `false` |

## Codex P2 — Netdata Cloud canonical-source identity correction (2026-10-22)

The [Codex P2 review](https://github.com/goozcena-gnl/devops-tools-catalog/pull/130#discussion_r4352753900) identified a product/component identity mismatch: `netdata-cloud` describes proprietary Netdata Cloud but its historical `repository_url` linked the separate GPL-licensed Netdata Agent repository. Since generated docs label `repository_url` as **Source repository**, the original entry misidentified Cloud's source.

**Correction:** remove `repository_url: https://github.com/netdata/netdata` and remove `repository_archived: false` from the Cloud product record. The Netdata Agent README, licence and release references are **retained in `sources`** with their existing URLs because they explain the Agent dependency and grant. The Cloud `official_url`, `documentation_url`, `free-saas` licence offering, commercial flag and reviewed status remain intact, and the `avoid_when` text now accurately describes the Agent evidence boundary. No unsupported Cloud source repository or licensing grant is invented. The category detail no longer includes an Agent **Source repository** link.

The full baseline-to-final ledger above includes the removal of `repository_url` (baseline Agent link to absent), while omitting the introduced-then-removed `repository_archived` field; this keeps the ledger consistent with canonical YAML. Changes to other nine Wave 20 IDs, review debt, baseline URL exceptions and any historic migration artefacts are prohibited. Run the *real* generator and full validation independently; this corrective commit invalidates the earlier exact-SHA audit and CI as final-head evidence.

## CI correction, generation and validation

The initial CI run failed on two demonstrated issues: generated documentation was stale, and `tests/test_v060_review_batch_07.py` froze rsyslog's review date at 2026-10-04. The historical test now permits exactly rsyslog's evidenced 2026-10-22 follow-up while preserving all other dates, licence assertions and retained uncertainty. No validation was disabled or generalized to accept arbitrary future dates.

Generated views must come only from `python -m scripts.generate_docs`; none are hand-edited. Local validation uses a clean Linux checkout with identical corrected files, avoiding unrelated ignored workspace artifacts, and a dedicated Python 3.12 virtual environment installed with committed constraints. The final validation and CI results, exact commit, and strict network audit artifact are recorded in PR #130 so recording those results does not invalidate the audited SHA.

Required commands:

```bash
python -m pip install -c config/python-constraints-3.12.txt hatchling editables
python -m pip install --no-build-isolation -c config/python-constraints-3.12.txt -e '.[dev]'
python -m scripts.python_constraints --verify-locked
python -m pip check
python -m scripts.generate_docs
python -m ruff check scripts tests
python -m ruff format --check scripts tests
python -m pytest
python -m scripts.generate_docs --check
python -m scripts.validate_catalog
git diff --check
```

After all CI checks pass, dispatch the existing strict Full link audit on the final branch SHA. Verify `strict_result: PASS`, `blocking_new: 0`, `blocking_known: 6`, and reconcile all six unchanged baseline URLs. `scripts.check_links` audits `official_url`, `repository_url` and `documentation_url`, not evidence-only `sources`; primary licence and source URLs were checked separately above. Audit output and caches stay out of commits. No baseline edits, waivers, TLS bypasses or lifecycle decisions based solely on link health.

## Unresolved blockers and handoff

- Elastic Stack component/distribution licensing, rsyslog aggregate licensing and Tracetest current support/per-file terms remain open, with `needs_review: true` and `status: needs-review` on all three records.
- Six historical URL blockers remain tracked by [issue #2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2): `https://github.com/hoji-ai/hoji`, `https://github.com/ophircloud/DevOps-Projects`, `https://hub.docker.com/r/soosio/dast`, `https://kubeflame.github.io`, `https://www.opentext.com/products/static-application-security-testing`, `https://www.yotascale.com`. The baseline is unchanged.
- Keep PR #130 **unmerged** until human approval, and issues #129 and #2 open. Do not merge, auto-merge, tag, release or alter branch protections. Completion of technical gates does not authorize any of those actions.
