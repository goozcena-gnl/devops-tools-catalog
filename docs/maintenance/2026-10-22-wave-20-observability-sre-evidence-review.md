# Wave 20 — Observability and SRE evidence review

Date: 2026-10-22. Baseline `main`: `0af956384ed33211352b249cf4c1f0d84795e168`. Scope: [issue #129](https://github.com/goozcena-gnl/devops-tools-catalog/issues/129).

## Proposed decisions

**7 cleared, 3 retained.** Review debt 647 → **640** and active 764 → **771**, provisional until independent CI and review. Canonical count remains 1,425. The licence-model classifications shift Netdata Cloud to `free-saas` and Sentry to `source-available`. Exactly ten canonical IDs in `data/tools/monitoring-metrics-logs-tracing.yaml` are in scope.

| ID | Decision | Main boundary |
|---|---|---|
| `elastic-stack-elk` | **RETAIN REVIEW** | RETAIN: combined Elastic Stack covers several separately licensed components; Elasticsearch source has per-file AGPL/SSPL/ELv2 options, not a universal Stack SPDX. |
| `icinga` | **CLEAR (provisional)** | CLEAR: Icinga 2 core (GPL-3.0-or-later in recent 2.16.x) separated from Web/Director and distributed monitoring prerequisites. |
| `influxdata` | **CLEAR (provisional)** | CLEAR: InfluxDB 3 vs older Flux-based versions and separate Core/Enterprise/Cloud offerings, without asserting one universal SPDX. |
| `krr` | **CLEAR (provisional)** | CLEAR: MIT CLI uses historical Prometheus telemetry for recommendations; changes to resources are not automatic. |
| `kubewatch` | **CLEAR (provisional)** | CLEAR: Apache-2.0 watcher and notifications with RBAC and external data-delivery boundaries. |
| `netdata-cloud` | **CLEAR (provisional)** | CLEAR: distinguish proprietary hosted Netdata Cloud from GPL Agent source; `free-saas` + commercial tiers. |
| `rsyslog` | **RETAIN REVIEW** | RETAIN: active upstream and recent releases verified, but precise GPL/LGPL coverage per file/component is unresolved. |
| `sentry` | **CLEAR (provisional)** | CLEAR: self-hosted server FSL-1.1-Apache-2.0 (source-available), with commercial cloud offer distinct. |
| `tracetest` | **RETAIN REVIEW** | RETAIN: per-file mixed MIT/TCL, last stable checked release in October 2024, current support unverified. |
| `zabbix` | **CLEAR (provisional)** | CLEAR: current AGPLv3 licensing distinguished from older GPLv2 versions and server/proxy/agent responsibilities. |

## Complete before/after changed-field ledger

The table below includes each changed canonical field, including complete source lists. Nonlisted fields are preserved. Folded YAML values and lists are flattened solely for readability; no raw source links are dropped.

### `elastic-stack-elk`

| Field | Before | After |
|---|---|---|
| `summary` | summary: Search/analytics/log platform; source licensing varies by component (Elastic License/SSPL and AGPL option for parts). | summary: Elastic Stack combines Elasticsearch search and analytics with separate Kibana and Logstash components; Elasticsearch source has file-dependent AGPLv3, SSPL and Elastic License terms, not one Stack-wide licence. |
| `use_when` | use_when:; Powerful full-text search and analytics over logs. | use_when:; You need full-text search and log analytics and can check each deployed component and distribution. |
| `avoid_when` | avoid_when:; Licensing concerns, high cost of running Elasticsearch, or you only need label-based log queries (Loki is simpler). | avoid_when:; You require one permissive Stack-wide licence; source options, x-pack files and shipped distributions have different terms.; A simpler log or metrics stack meets the requirement. |
| `maturity` | maturity: unknown | maturity: established |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-22' |
| `sources` | sources:; legacy:5_Monitoring-Observability/README.md#L54; legacy:devopstools_final.md#L761 | sources:; legacy:5_Monitoring-Observability/README.md#L54; legacy:devopstools_final.md#L761; https://github.com/elastic/elasticsearch/blob/main/LICENSE.txt; https://github.com/elastic/elasticsearch/releases/tag/v9.5.5; https://www.elastic.co/pricing/faq/licensing |
| `repository_archived` | ∅ | repository_archived: false |

### `icinga`

| Field | Before | After |
|---|---|---|
| `summary` | summary: Open source monitoring system derived from Nagios. | summary: Icinga 2 monitors hosts and services using checks, notifications, an API and distributed zones; Web, DB and Director are separate components. |
| `use_when` | use_when:; You want Nagios-style host/service checks with a modern API and HA. | use_when:; You need distributed host and service checks with managed API access, certificates and alerting. |
| `avoid_when` | avoid_when:; You need metrics-first or tracing-centric observability. | avoid_when:; You expect Icinga 2 alone to contain Icinga Web, DB and Director.; You cannot secure API users, certificates and cluster trust zones. |
| `maturity` | maturity: unknown | maturity: established |
| `status` | status: needs-review | status: active |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-22' |
| `sources` | sources:; legacy:5_Monitoring-Observability/README.md#L12; legacy:devopstools_final.md#L706 | sources:; legacy:5_Monitoring-Observability/README.md#L12; legacy:devopstools_final.md#L706; https://github.com/Icinga/icinga2/blob/master/README.md; https://github.com/Icinga/icinga2/blob/master/LICENSE.md; https://github.com/Icinga/icinga2/releases/tag/v2.16.5; https://icinga.com/docs/icinga-2/latest/doc/06-distributed-monitoring/ |
| `needs_review` | needs_review: true | needs_review: false |
| `license_spdx` | ∅ | license_spdx: GPL-3.0-or-later |
| `documentation_url` | ∅ | documentation_url: https://icinga.com/docs/icinga-2/latest/ |
| `repository_archived` | ∅ | repository_archived: false |

### `influxdata`

| Field | Before | After |
|---|---|---|
| `summary` | summary: Time series platform with OSS components and commercial cloud/enterprise offerings. | summary: InfluxData offers InfluxDB time-series products; InfluxDB 3 Core is open source, while Enterprise and Cloud offerings differ in price and deployment. Version 3 supports SQL and InfluxQL, not Flux. |
| `use_when` | use_when:; IoT/sensor-heavy time series with Flux query language. | use_when:; You need time-series ingest and analytics and can select the specific version, topology and supported query language. |
| `avoid_when` | avoid_when:; Prometheus-compatible ecosystem or PromQL is your standard. | avoid_when:; You rely on Flux without migrating InfluxDB 2 queries to InfluxDB 3 SQL or InfluxQL.; You expect free single-node Core to provide Enterprise HA or managed cloud capabilities. |
| `maturity` | maturity: unknown | maturity: established |
| `status` | status: needs-review | status: active |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-22' |
| `sources` | sources:; legacy:5_Monitoring-Observability/README.md#L44; legacy:devopstools_final.md#L749 | sources:; legacy:5_Monitoring-Observability/README.md#L44; legacy:devopstools_final.md#L749; https://github.com/influxdata/influxdb/blob/main/LICENSE-MIT; https://github.com/influxdata/influxdb/blob/main/LICENSE-APACHE; https://github.com/influxdata/influxdb/releases/tag/v3.12.1; https://docs.influxdata.com/platform/identify-version/; https://docs.influxdata.com/influxdb3/which-influxdb-3/ |
| `needs_review` | needs_review: true | needs_review: false |
| `commercial_offering` | ∅ | commercial_offering: true |
| `documentation_url` | ∅ | documentation_url: https://docs.influxdata.com/platform/ |
| `repository_archived` | ∅ | repository_archived: false |

### `krr`

| Field | Before | After |
|---|---|---|
| `summary` | summary: Kubernetes Resource Recommendations by Robusta. | summary: Robusta KRR analyzes Prometheus-compatible telemetry and recommends Kubernetes CPU and memory requests and limits; automatic application requires separate tools. |
| `use_when` | use_when:; Right-sizing pod requests/limits based on real usage data. | use_when:; You have representative Prometheus-compatible resource usage history and want to review pod right-sizing proposals. |
| `avoid_when` | avoid_when:; VPA already handles your resource tuning needs. | avoid_when:; You assume the KRR CLI safely changes workloads itself or do not have representative metrics.; You cannot review recommendation accuracy and disruption risks before applying changes. |
| `maturity` | maturity: unknown | maturity: established |
| `status` | status: needs-review | status: active |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-22' |
| `sources` | sources:; legacy:5_Monitoring-Observability/README.md#L29; legacy:devopstools_final.md#L729 | sources:; legacy:5_Monitoring-Observability/README.md#L29; legacy:devopstools_final.md#L729; https://github.com/robusta-dev/krr/blob/main/LICENSE; https://github.com/robusta-dev/krr/releases/tag/v1.31.1; https://github.com/robusta-dev/krr/blob/main/README.md |
| `needs_review` | needs_review: true | needs_review: false |
| `license_spdx` | ∅ | license_spdx: MIT |
| `documentation_url` | ∅ | documentation_url: https://github.com/robusta-dev/krr/blob/main/README.md |
| `repository_archived` | ∅ | repository_archived: false |

### `kubewatch`

| Field | Before | After |
|---|---|---|
| `summary` | summary: Kubernetes event watcher and notifier. | summary: Robusta-maintained Kubewatch watches selected Kubernetes resource changes and sends notifications to configured handlers and collaboration channels. |
| `use_when` | use_when:; You want Slack/webhook alerts on K8s resource changes. | use_when:; You need lightweight Kubernetes event notifications with limited watch permissions and approved delivery endpoints. |
| `avoid_when` | avoid_when:; You already have event routing via Robusta or a full observability platform. | avoid_when:; You need a full incident-management or telemetry correlation platform rather than object-change alerts.; You cannot restrict RBAC scope or protect metadata sent to external channels. |
| `maturity` | maturity: unknown | maturity: established |
| `status` | status: needs-review | status: active |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-22' |
| `sources` | sources:; legacy:5_Monitoring-Observability/README.md#L31; legacy:devopstools_final.md#L732 | sources:; legacy:5_Monitoring-Observability/README.md#L31; legacy:devopstools_final.md#L732; https://github.com/robusta-dev/kubewatch/blob/master/LICENSE; https://github.com/robusta-dev/kubewatch/blob/master/README.md; https://github.com/robusta-dev/kubewatch/releases/tag/v2.16.1 |
| `needs_review` | needs_review: true | needs_review: false |
| `license_spdx` | ∅ | license_spdx: Apache-2.0 |
| `documentation_url` | ∅ | documentation_url: https://github.com/robusta-dev/kubewatch/blob/master/README.md |
| `repository_archived` | ∅ | repository_archived: false |

### `netdata-cloud`

| Field | Before | After |
|---|---|---|
| `summary` | summary: SaaS control plane for Netdata (Netdata Agent is open-source; Cloud adds centralized management/collaboration). | summary: Netdata Cloud is a proprietary hosted control plane with free and paid tiers; the separate GPLv3+ Agent collects and stores metrics, and the browser UI has a distinct licence. |
| `use_when` | use_when:; You want per-second granularity with near-zero config. | use_when:; You need hosted access and collaborative monitoring across agents and accept Netdata Cloud account and network dependencies. |
| `avoid_when` | avoid_when:; Long-term storage or complex cross-service correlation is the main goal. | avoid_when:; You require the Cloud service and UI to be fully open source or self-hosted.; You cannot approve cloud data flows or subscription limits; the linked source repo contains the Agent, not Cloud. |
| `license_model` | license_model: open-core | license_model: free-saas |
| `maturity` | maturity: unknown | maturity: established |
| `status` | status: needs-review | status: active |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-22' |
| `sources` | sources:; legacy:5_Monitoring-Observability/README.md#L16; legacy:devopstools_final.md#L711 | sources:; legacy:5_Monitoring-Observability/README.md#L16; legacy:devopstools_final.md#L711; https://github.com/netdata/netdata/blob/master/README.md; https://github.com/netdata/netdata/blob/master/LICENSE; https://github.com/netdata/netdata/releases/tag/v2.12.1; https://www.netdata.cloud/ |
| `needs_review` | needs_review: true | needs_review: false |
| `commercial_offering` | ∅ | commercial_offering: true |
| `documentation_url` | ∅ | documentation_url: https://learn.netdata.cloud/ |
| `repository_archived` | ∅ | repository_archived: false |

### `rsyslog`

| Field | Before | After |
|---|---|---|
| `summary` | summary: High-performance syslog daemon with flexible routing (often used as a log edge forwarder). | summary: rsyslog is a high-throughput syslog daemon and routing engine; its repository contains GPLv3 and LGPLv3 texts whose exact component applicability still needs review. |
| `use_when` | use_when:; High-throughput syslog forwarding on Linux hosts. | use_when:; You need configurable syslog collection, filtering and reliable forwarding on Linux systems. |
| `avoid_when` | avoid_when:; You need structured log parsing or container-native log collection. | avoid_when:; You need downstream log indexing, search and dashboards rather than a forwarding engine.; You require one verified SPDX for the full project before checking file-level licensing. |
| `verified_on` | verified_on: '2026-10-04' | verified_on: '2026-10-22' |
| `sources` | sources:; legacy:5_Monitoring-Observability/README.md#L62; legacy:devopstools_final.md#L770; https://www.rsyslog.com; https://docs.rsyslog.com/doc/; https://github.com/rsyslog/rsyslog; https://github.com/rsyslog/rsyslog/blob/main/README.md; https://github.com/rsyslog/rsyslog/blob/main/COPYING.LESSER; https://github.com/rsyslog/rsyslog/blob/main/runtime/rsyslog.h; https://github.com/rsyslog/rsyslog/blob/main/tools/rsyslogd.c | sources:; legacy:5_Monitoring-Observability/README.md#L62; legacy:devopstools_final.md#L770; https://www.rsyslog.com; https://docs.rsyslog.com/doc/; https://github.com/rsyslog/rsyslog; https://github.com/rsyslog/rsyslog/blob/main/README.md; https://github.com/rsyslog/rsyslog/blob/main/COPYING.LESSER; https://github.com/rsyslog/rsyslog/blob/main/runtime/rsyslog.h; https://github.com/rsyslog/rsyslog/blob/main/tools/rsyslogd.c; https://github.com/rsyslog/rsyslog/blob/main/COPYING; https://github.com/rsyslog/rsyslog/releases/tag/v8.2610.0 |

### `sentry`

| Field | Before | After |
|---|---|---|
| `summary` | summary: Error monitoring with performance/tracing features (popular for app-level APM signals). | summary: Sentry monitors application errors, releases and performance; its main self-hosted server source uses Functional Source License 1.1 with a future Apache-2.0 grant, distinct from hosted commercial plans. |
| `use_when` | use_when:; Developer-facing error tracking with stack traces and release health. | use_when:; You need application error diagnostics, performance telemetry and release-linked troubleshooting with controlled ingestion. |
| `avoid_when` | avoid_when:; Infrastructure-level tracing or metrics monitoring is the goal. | avoid_when:; You require immediate unrestricted OSI-licensed commercial redistribution or infrastructure-wide metrics.; You cannot govern captured data, self-hosted service dependencies or subscription limits. |
| `license_model` | license_model: open-core | license_model: source-available |
| `maturity` | maturity: unknown | maturity: established |
| `status` | status: needs-review | status: active |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-22' |
| `sources` | sources:; legacy:5_Monitoring-Observability/README.md#L73; legacy:devopstools_final.md#L782 | sources:; legacy:5_Monitoring-Observability/README.md#L73; legacy:devopstools_final.md#L782; https://github.com/getsentry/sentry/blob/master/LICENSE.md; https://github.com/getsentry/sentry/releases/tag/26.10.0; https://docs.sentry.io/ |
| `needs_review` | needs_review: true | needs_review: false |
| `commercial_offering` | ∅ | commercial_offering: true |
| `documentation_url` | ∅ | documentation_url: https://docs.sentry.io/ |
| `repository_archived` | ∅ | repository_archived: false |

### `tracetest`

| Field | Before | After |
|---|---|---|
| `summary` | summary: Trace-based integration testing using OpenTelemetry, with mixed MIT/Tracetest Community licensing and unclear current support. | summary: Tracetest provides OpenTelemetry trace-based integration testing; source files have mixed MIT and Tracetest Community terms and current support remains unverified. |
| `use_when` | use_when:; You are evaluating assertions against distributed traces for integration and end-to-end tests. | use_when:; You are testing distributed traces in a controlled evaluation and can check edition-specific and per-file licensing. |
| `avoid_when` | avoid_when:; You require a clearly maintained and uniformly permissive production tool; source files have different license grants. | avoid_when:; You require established current maintenance or a uniformly permissive licence; the last checked stable release is from 2024. |
| `verified_on` | verified_on: '2026-10-21' | verified_on: '2026-10-22' |
| `sources` | sources:; legacy:5_Monitoring-Observability/README.md#L74; legacy:devopstools_final.md#L783; https://github.com/kubeshop/tracetest; https://github.com/kubeshop/tracetest/blob/main/LICENSE; https://github.com/kubeshop/tracetest/releases; https://docs.tracetest.io/ | sources:; legacy:5_Monitoring-Observability/README.md#L74; legacy:devopstools_final.md#L783; https://github.com/kubeshop/tracetest; https://github.com/kubeshop/tracetest/blob/main/LICENSE; https://github.com/kubeshop/tracetest/releases; https://docs.tracetest.io/; https://github.com/kubeshop/tracetest/releases/tag/v1.7.1; https://github.com/kubeshop/tracetest/blob/main/README.md |

### `zabbix`

| Field | Before | After |
|---|---|---|
| `summary` | summary: Enterprise-grade monitoring platform (metrics, triggers, dashboards). | summary: Zabbix monitors infrastructure with server, proxy, agent and alerting components; software from version 7.0 uses AGPLv3 while older releases used GPLv2 terms. |
| `use_when` | use_when:; Large-scale traditional infra monitoring with templates and agent support. | use_when:; You need broad distributed agent or agentless infrastructure monitoring, templates and configurable alerts. |
| `avoid_when` | avoid_when:; Your workload is fully cloud-native and you prefer PromQL/OTel standards. | avoid_when:; You assume older GPLv2 releases and current AGPLv3 have identical sharing obligations.; You need native tracing instead of infrastructure monitoring or cannot manage Zabbix storage and access. |
| `maturity` | maturity: unknown | maturity: established |
| `status` | status: needs-review | status: active |
| `verified_on` | verified_on: '2026-08-03' | verified_on: '2026-10-22' |
| `sources` | sources:; legacy:5_Monitoring-Observability/README.md#L24; legacy:devopstools_final.md#L720 | sources:; legacy:5_Monitoring-Observability/README.md#L24; legacy:devopstools_final.md#L720; https://github.com/zabbix/zabbix/blob/master/README.md; https://github.com/zabbix/zabbix/blob/master/COPYING; https://www.zabbix.com/license; https://www.zabbix.com/documentation/current/en/manual |
| `needs_review` | needs_review: true | needs_review: false |
| `license_spdx` | ∅ | license_spdx: AGPL-3.0-only |
| `documentation_url` | ∅ | documentation_url: https://www.zabbix.com/documentation/current/en/manual |
| `repository_archived` | ∅ | repository_archived: false |

## Evidence controls and limitations

- Each modified record includes upstream repository / original licence / release or documentation sources; existing legacy source pointers are retained.
- The upstream releases and licences were checked via GitHub primary repositories on 2026-10-22, supplemented by vendor documentation. GitHub's repository-level licence metadata was **not** taken as sufficient for complex per-file licensing.
- Three unresolved records explicitly remain `needs_review: true` / `status: needs-review`: `elastic-stack-elk`, `rsyslog`, `tracetest`. Retained cases are not represented as verified current offerings.
- The **generated README, category, roles, lifecycle and statistics files have not yet been regenerated by the project's actual generator**. This is a known blocking step; do not mark the Draft PR ready or interpret a stale generator check as acceptable. Run `python -m scripts.generate_docs` in a complete repository checkout; commit exact outputs, then run `--check`.
- Other pending gates: locked Linux Python 3.12 environment, Ruff lint and format, full pytest, `python -m scripts.validate_catalog`, `git diff --check`, PR security scans, CodeQL review and the fresh strict full link audit on the final PR head. The last audit #26 belongs to Wave 19, not to Wave 20.
- No URL baseline changes, TLS workarounds, migration edits or waiver changes are authorized. Keep [issue #2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2) open for six historical blockers.
- This is a **provisional evidence pass**. Licensing classification, especially Icinga and Zabbix version applicability, InfluxDB product boundaries, and Sentry's future grant must receive independent review before `needs_review: false` can be accepted.
- Do not merge, release, tag, close issue #129 or alter `main` without explicit human authorization.
