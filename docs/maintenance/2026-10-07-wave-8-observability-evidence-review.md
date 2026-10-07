# Evidence review Wave 8 — observability foundations — 2026-10-07

Exactly the fixed ten canonical records receive **CLEAR REVIEW** after an individual review of all 24 material fields. Stable IDs and every historical source are preserved. Canonical YAML remains authoritative; generated pages are regenerated.

## Verified baseline and scope

- Main: `0578bacfa00160df890510c77d95514d7bf7c1fe` (post-Wave-7).
- Branch: `maintenance/wave-8-observability-evidence-review`.
- Before editing: clean tree, zero open PRs and all five exact-main check runs successful (Analyze actions/python, Plumber supply-chain audit, gitleaks and catalogue validation). Read-only code-scanning alert count was zero.
- Issue #2 was read: Wave 7 COMPLETED; Wave 8 NOT STARTED — READY TO SCOPE. Its body and timestamp are preserved for comparison at handoff; it is not edited.
- Exactly ten existing records in one category file change. No unrelated record, reviewed link baseline, committed audit output, ledger, workflow, CodeQL configuration or Python constraint changes. No Wave 4–7 revisit or Wave 9 work; no merge or release.

The fixed cohort covers metrics, visualization, logs, traces, portable instrumentation and Kubernetes object-state observability. Its main evidence risks are product-family versus software licensing, umbrella versus implementation repositories, and distinct storage/collection/query responsibilities. All ten initially had review flag/status debt, unknown maturity, no SPDX and no documentation URL.

| Rank | ID | Initial name | Initial category | Initial debt |
|---:|---|---|---|---|
| 1 | `prometheus` | Prometheus | `monitoring-metrics-logs-tracing` | needs-review; unknown maturity; missing docs; no SPDX |
| 2 | `grafana` | Grafana | `monitoring-metrics-logs-tracing` | needs-review; unknown maturity; missing docs; no SPDX |
| 3 | `grafana-loki` | Grafana Loki | `monitoring-metrics-logs-tracing` | needs-review; unknown maturity; missing docs; no SPDX |
| 4 | `grafana-tempo` | Grafana Tempo | `monitoring-metrics-logs-tracing` | needs-review; unknown maturity; missing docs; no SPDX |
| 5 | `grafana-mimir` | Grafana Mimir | `monitoring-metrics-logs-tracing` | needs-review; unknown maturity; missing docs; no SPDX |
| 6 | `opentelemetry` | OpenTelemetry | `monitoring-metrics-logs-tracing` | needs-review; unknown maturity; missing docs; no SPDX; missing umbrella repository |
| 7 | `opentelemetry-collector` | OpenTelemetry Collector | `monitoring-metrics-logs-tracing` | needs-review; unknown maturity; missing docs; no SPDX |
| 8 | `jaeger` | Jaeger | `monitoring-metrics-logs-tracing` | needs-review; unknown maturity; missing docs; no SPDX |
| 9 | `thanos` | Thanos | `monitoring-metrics-logs-tracing` | needs-review; unknown maturity; missing docs; no SPDX |
| 10 | `kube-state-metrics` | Kube State Metrics | `monitoring-metrics-logs-tracing` | needs-review; unknown maturity; missing docs; no SPDX; missing official URL |

## Evidence method and interpretation

Primary sources were read directly: official documentation, upstream READMEs, actual LICENSE/LICENSING files, governance and CNCF project pages, legal terms, repository metadata and release feeds. Search snippets were discovery only. GitHub metadata confirmed all nine implementation repositories are non-archived; release/activity evidence supports lifecycle independently of network responses. The OpenTelemetry umbrella deliberately receives no single repository or archival flag.

Catalogue maturity is an editorial judgement from maintained implementation/specification history, documented operations and governance. It is neither a GitHub popularity score nor a direct copy of CNCF maturity. Categories, roles and lifecycle stages are reviewer mappings to the existing taxonomy. All ten retain monitoring as primary category; Collector and instrumentation subcategories are corrected, and kube-state-metrics gains the Kubernetes engineer role. Use/avoid guidance expresses documented operating boundaries, not invented vendor restrictions.

Grafana remains an explicitly scoped open-core product family without a universal SPDX. Loki, Tempo and Mimir remain separate OSS implementations; AGPL-3.0-only describes their declared default software grant with documented component exceptions. commercial_offering records related commercial services without changing those OSS records into hosted SaaS. OpenTelemetry Apache-2.0 follows its explicit project-wide software policy, not CNCF affiliation. Other optional commercial booleans remain absent rather than denying third-party businesses. Empty alternatives/tags remain unchanged.

## Decisions and complete material-field review

### prometheus

**Identity boundary:** The stable ID represents the Prometheus monitoring server/toolkit entry, with server capabilities scoped explicitly. Exporters, client libraries, Pushgateway and Alertmanager are separately maintained ecosystem components; this is not one repository for the entire ecosystem.

**Licence boundary:** Apache-2.0 is verified from the server LICENSE. The software licence is not inferred from CNCF hosting and does not stand in for every third-party integration.

**Commercial/service boundary:** No vendor-hosted product is implied. Leave optional commercial_offering absent rather than claiming there are no commercial services around Prometheus.

**Repository boundary:** Retain prometheus/prometheus as the canonical server repository. Add the official overview documentation; official site remains prometheus.io.

**Governance:** Official governance defines a Steering Committee and contributor/maintainer roles. CNCF directly records graduation on 2018-08-09; this is foundation status, not a software licence or an automatic catalogue maturity mapping.

**Maturity:** Established is a reviewer judgement from long maintained release history, documented PromQL/storage/alerting operations and independent project governance.

**Lifecycle:** Non-archived server repository with 2026-10-07 activity and stable releases including v3.15.0 (2026-09-25) and v3.13.4 (2026-10-02). Activity and release history support active status independently of URL responses.

**Unresolved questions / limits:** None blocking the server boundary. Long-term distributed storage, notifications and exporters require separately selected components; numeric monitoring is not a complete billing ledger.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical server repository and scope][prometheus-e1], [Server software licence][prometheus-e2], [Official overview documentation and ecosystem boundary][prometheus-e3], [Project governance][prometheus-e4], [CNCF foundation status][prometheus-e5], [Maintained release history][prometheus-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | prometheus | prometheus | [Canonical server repository and scope][prometheus-e1] | Preserve stable catalogue ID and history; no duplicate record. |
| `name` | Prometheus | Prometheus | [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Monitoring and alerting toolkit. | Open-source metrics monitoring server with a time-series database, PromQL and alerting rules; Alertmanager, exporters and client libraries are separate ecosystem components. | [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://prometheus.io | https://prometheus.io | [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3] | Reviewed; retained: official entry point identified by the upstream project; any boundary correction is explained above. |
| `repository_url` | https://github.com/prometheus/prometheus | https://github.com/prometheus/prometheus | [Canonical server repository and scope][prometheus-e1] | Retain the verified scoped implementation repository. |
| `documentation_url` | *absent* | https://prometheus.io/docs/introduction/overview/ | [Official overview documentation and ecosystem boundary][prometheus-e3] | Add the directly verified official documentation entry point. |
| `categories` | monitoring-metrics-logs-tracing | monitoring-metrics-logs-tracing | [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `subcategories` | Monitoring &amp; Observability Platforms | Metrics monitoring and alerting | [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3] | Changed: reviewer mapping of documented capability to the existing taxonomy. |
| `roles` | devops-engineer<br>site-reliability-engineer<br>observability-engineer | devops-engineer<br>site-reliability-engineer<br>observability-engineer | [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `lifecycle_stages` | operate<br>monitor | operate<br>monitor | [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `use_when` | Cloud-native/Kubernetes metrics with a pull model and PromQL. | You need labelled numeric time-series monitoring, PromQL and alerting rules with local storage and pull-based scraping of instrumented applications or exporters. | [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3], [Server software licence][prometheus-e2] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `avoid_when` | You need long-term storage out of the box or event/log-based monitoring. | You need log or trace storage, complete per-request billing data, or a distributed long-term metrics backend without adding separate components. | [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3], [Server software licence][prometheus-e2] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `deployment_models` | `[]` | self-hosted | [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3] | Record software self-hosting; only Grafana parent includes hosted-saas for its explicitly named Cloud edition. |
| `license_model` | oss | oss | [Server software licence][prometheus-e2] | Reviewed; retained: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Server software licence][prometheus-e2] | Changed: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Canonical server repository and scope][prometheus-e1] | Leave optional field absent; no blanket claim about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Maintained release history][prometheus-e6], [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3], [Project governance][prometheus-e4], [CNCF foundation status][prometheus-e5] | Editorial established judgement from maintained releases/specifications, documented operations and governance; component stability is explicitly bounded. |
| `status` | needs-review | active | [Maintained release history][prometheus-e6], [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical server repository and scope][prometheus-e1], [Maintained release history][prometheus-e6] | GitHub API reports archived=false; actual release/activity evidence supports lifecycle separately. |
| `alternatives` | `[]` | `[]` | [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `tags` | `[]` | `[]` | [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical server repository and scope][prometheus-e1], [Server software licence][prometheus-e2], [Official overview documentation and ecosystem boundary][prometheus-e3], [Project governance][prometheus-e4], [CNCF foundation status][prometheus-e5], [Maintained release history][prometheus-e6] | Actual review date, changed only for these ten records. |
| `sources` | legacy:5_Monitoring-Observability/README.md#L19<br>legacy:devopstools_final.md#L714 | legacy:5_Monitoring-Observability/README.md#L19<br>legacy:devopstools_final.md#L714<br>https://github.com/prometheus/prometheus<br>https://github.com/prometheus/prometheus/blob/main/LICENSE<br>https://prometheus.io/docs/introduction/overview/<br>https://prometheus.io/governance/<br>https://www.cncf.io/projects/prometheus/<br>https://github.com/prometheus/prometheus/releases | [Canonical server repository and scope][prometheus-e1], [Server software licence][prometheus-e2], [Official overview documentation and ecosystem boundary][prometheus-e3], [Project governance][prometheus-e4], [CNCF foundation status][prometheus-e5], [Maintained release history][prometheus-e6] | Preserve every legacy source and append checked primary sources, including the former OpenTelemetry organization pointer. |
| `needs_review` | `true` | `false` | [Maintained release history][prometheus-e6], [Canonical server repository and scope][prometheus-e1], [Official overview documentation and ecosystem boundary][prometheus-e3] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[prometheus-e1]: https://github.com/prometheus/prometheus
[prometheus-e2]: https://github.com/prometheus/prometheus/blob/main/LICENSE
[prometheus-e3]: https://prometheus.io/docs/introduction/overview/
[prometheus-e4]: https://prometheus.io/governance/
[prometheus-e5]: https://www.cncf.io/projects/prometheus/
[prometheus-e6]: https://github.com/prometheus/prometheus/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/prometheus/prometheus) (`archived: false`).

### grafana

**Identity boundary:** Keep the existing parent Grafana identity and stable ID. Scope the summary to visualization/alerting and name OSS, Enterprise and Cloud explicitly. Grafana Labs is the vendor, not the record identity; plugins are distinct components.

**Licence boundary:** Retain open-core for this mixed product family and leave license_spdx absent. The OSS source default is explicitly AGPL-3.0-only; LICENSING.md identifies Apache-2.0 and vendored/MIT exceptions. Enterprise object code and proprietary plugins have separate grants; the OSS default is not a family-wide licence.

**Commercial/service boundary:** commercial_offering=true follows the documented commercial Enterprise edition and hosted Cloud service. Self-hosted applies to OSS/Enterprise, hosted-saas to Cloud. Service use is governed by its agreement/order, not by the source repository grant. Free Enterprise features do not make its object-code licence OSS.

**Repository boundary:** Keep grafana/grafana as the explicitly scoped OSS development repository; it is not the full source of Enterprise, Cloud or all plugins. Add the OSS/Enterprise documentation entry point.

**Governance:** Grafana Labs leads the product family and upstream contributor process. CONTRIBUTING.md documents community participation; no CNCF project graduation claim is made for Grafana.

**Maturity:** Established is a reviewer judgement from maintained release/upgrade history, operational documentation and long-running OSS/commercial editions, independently of stars or vendor marketing.

**Lifecycle:** Non-archived OSS repository with 2026-10-07 activity and maintained release/security patch history, including v13.2.3 on 2026-09-29. Current edition documentation supports the continuing product family.

**Unresolved questions / limits:** None blocking this explicit family boundary. Enterprise and Cloud features depend on entitlement and plugin-specific terms. A single parent SPDX remains deliberately absent; the canonical summary and guidance prevent OSS licence inheritance.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical OSS repository and scope][grafana-e1], [OSS software licence][grafana-e2], [Exact OSS SPDX and component licence exceptions][grafana-e3], [Official OSS and Enterprise documentation][grafana-e4], [Commercial Enterprise edition boundary][grafana-e5], [Hosted Grafana Cloud product boundary][grafana-e6], [Enterprise object-code licence agreement][grafana-e7], [Enterprise plugin licence boundary][grafana-e8], [Commercial software and hosted-service agreement][grafana-e9], [Project contribution governance][grafana-e10], [Maintained release history][grafana-e11].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | grafana | grafana | [Canonical OSS repository and scope][grafana-e1] | Preserve stable catalogue ID and history; no duplicate record. |
| `name` | Grafana | Grafana | [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Visualization and analytics for metrics. | Grafana visualization and alerting product family: OSS dashboards query external data sources; Enterprise adds commercial features and plugins, and Grafana Cloud is the managed service. | [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://grafana.com | https://grafana.com | [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4] | Reviewed; retained: official entry point identified by the upstream project; any boundary correction is explained above. |
| `repository_url` | https://github.com/grafana/grafana | https://github.com/grafana/grafana | [Canonical OSS repository and scope][grafana-e1] | Retain the verified scoped implementation repository. |
| `documentation_url` | *absent* | https://grafana.com/docs/grafana/latest/ | [Official OSS and Enterprise documentation][grafana-e4] | Add the directly verified official documentation entry point. |
| `categories` | monitoring-metrics-logs-tracing | monitoring-metrics-logs-tracing | [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `subcategories` | Visualization, Metrics, and Tracing | Observability visualization and alerting | [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4] | Changed: reviewer mapping of documented capability to the existing taxonomy. |
| `roles` | devops-engineer<br>site-reliability-engineer<br>observability-engineer | devops-engineer<br>site-reliability-engineer<br>observability-engineer | [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `lifecycle_stages` | operate<br>monitor | operate<br>monitor | [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `use_when` | Building dashboards across heterogeneous data sources. | You want dashboards, exploration and alerting across metrics, logs and traces, choosing self-hosted OSS or Enterprise, or managed Grafana Cloud, according to required features and terms. | [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4], [OSS software licence][grafana-e2], [Exact OSS SPDX and component licence exceptions][grafana-e3], [Enterprise object-code licence agreement][grafana-e7], [Enterprise plugin licence boundary][grafana-e8], [Commercial software and hosted-service agreement][grafana-e9] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `avoid_when` | You need an all-in-one monitoring solution—Grafana is a frontend, not a backend. | You require the OSS repository licence to cover Enterprise binaries, proprietary plugins or Grafana Cloud, or expect self-hosted Grafana alone to store all telemetry without external backends. | [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4], [OSS software licence][grafana-e2], [Exact OSS SPDX and component licence exceptions][grafana-e3], [Enterprise object-code licence agreement][grafana-e7], [Enterprise plugin licence boundary][grafana-e8], [Commercial software and hosted-service agreement][grafana-e9] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `deployment_models` | `[]` | self-hosted<br>hosted-saas | [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4], [Commercial Enterprise edition boundary][grafana-e5], [Hosted Grafana Cloud product boundary][grafana-e6], [Enterprise object-code licence agreement][grafana-e7], [Enterprise plugin licence boundary][grafana-e8] | Record software self-hosting; only Grafana parent includes hosted-saas for its explicitly named Cloud edition. |
| `license_model` | open-core | open-core | [OSS software licence][grafana-e2], [Exact OSS SPDX and component licence exceptions][grafana-e3], [Enterprise object-code licence agreement][grafana-e7], [Enterprise plugin licence boundary][grafana-e8], [Commercial software and hosted-service agreement][grafana-e9] | Reviewed; retained: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `license_spdx` | *absent* | *absent* | [OSS software licence][grafana-e2], [Exact OSS SPDX and component licence exceptions][grafana-e3], [Enterprise object-code licence agreement][grafana-e7], [Enterprise plugin licence boundary][grafana-e8], [Commercial software and hosted-service agreement][grafana-e9] | Leave absent: Grafana family spans OSS, Enterprise, plugins and Cloud; the verified OSS default is not a universal family SPDX. |
| `commercial_offering` | *absent* | `true` | [Official OSS and Enterprise documentation][grafana-e4], [Commercial Enterprise edition boundary][grafana-e5], [Hosted Grafana Cloud product boundary][grafana-e6], [Enterprise object-code licence agreement][grafana-e7], [Enterprise plugin licence boundary][grafana-e8], [Commercial software and hosted-service agreement][grafana-e9] | Add true for the independently documented related commercial offering; OSS grant and software execution scope remain separate. |
| `maturity` | unknown | established | [Maintained release history][grafana-e11], [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4], [Project contribution governance][grafana-e10] | Editorial established judgement from maintained releases/specifications, documented operations and governance; component stability is explicitly bounded. |
| `status` | needs-review | active | [Maintained release history][grafana-e11], [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical OSS repository and scope][grafana-e1], [Maintained release history][grafana-e11] | GitHub API reports archived=false; actual release/activity evidence supports lifecycle separately. |
| `alternatives` | `[]` | `[]` | [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `tags` | `[]` | `[]` | [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical OSS repository and scope][grafana-e1], [OSS software licence][grafana-e2], [Exact OSS SPDX and component licence exceptions][grafana-e3], [Official OSS and Enterprise documentation][grafana-e4], [Commercial Enterprise edition boundary][grafana-e5], [Hosted Grafana Cloud product boundary][grafana-e6], [Enterprise object-code licence agreement][grafana-e7], [Enterprise plugin licence boundary][grafana-e8], [Commercial software and hosted-service agreement][grafana-e9], [Project contribution governance][grafana-e10], [Maintained release history][grafana-e11] | Actual review date, changed only for these ten records. |
| `sources` | legacy:5_Monitoring-Observability/README.md#L39<br>legacy:devopstools_final.md#L743 | legacy:5_Monitoring-Observability/README.md#L39<br>legacy:devopstools_final.md#L743<br>https://github.com/grafana/grafana<br>https://github.com/grafana/grafana/blob/main/LICENSE<br>https://github.com/grafana/grafana/blob/main/LICENSING.md<br>https://grafana.com/docs/grafana/latest/<br>https://grafana.com/docs/grafana/latest/introduction/grafana-enterprise/<br>https://grafana.com/docs/grafana/latest/introduction/grafana-cloud/<br>https://grafana.com/legal/grafana-labs-license/<br>https://grafana.com/legal/enterprise-plugins/<br>https://grafana.com/legal/msa/<br>https://github.com/grafana/grafana/blob/main/CONTRIBUTING.md<br>https://github.com/grafana/grafana/releases | [Canonical OSS repository and scope][grafana-e1], [OSS software licence][grafana-e2], [Exact OSS SPDX and component licence exceptions][grafana-e3], [Official OSS and Enterprise documentation][grafana-e4], [Commercial Enterprise edition boundary][grafana-e5], [Hosted Grafana Cloud product boundary][grafana-e6], [Enterprise object-code licence agreement][grafana-e7], [Enterprise plugin licence boundary][grafana-e8], [Commercial software and hosted-service agreement][grafana-e9], [Project contribution governance][grafana-e10], [Maintained release history][grafana-e11] | Preserve every legacy source and append checked primary sources, including the former OpenTelemetry organization pointer. |
| `needs_review` | `true` | `false` | [Maintained release history][grafana-e11], [Canonical OSS repository and scope][grafana-e1], [Official OSS and Enterprise documentation][grafana-e4] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[grafana-e1]: https://github.com/grafana/grafana
[grafana-e2]: https://github.com/grafana/grafana/blob/main/LICENSE
[grafana-e3]: https://github.com/grafana/grafana/blob/main/LICENSING.md
[grafana-e4]: https://grafana.com/docs/grafana/latest/
[grafana-e5]: https://grafana.com/docs/grafana/latest/introduction/grafana-enterprise/
[grafana-e6]: https://grafana.com/docs/grafana/latest/introduction/grafana-cloud/
[grafana-e7]: https://grafana.com/legal/grafana-labs-license/
[grafana-e8]: https://grafana.com/legal/enterprise-plugins/
[grafana-e9]: https://grafana.com/legal/msa/
[grafana-e10]: https://github.com/grafana/grafana/blob/main/CONTRIBUTING.md
[grafana-e11]: https://github.com/grafana/grafana/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/grafana/grafana) (`archived: false`).

### grafana-loki

**Identity boundary:** Loki is the log storage/query backend, not Grafana UI, its log-shipping agents or Grafana Cloud Logs. Label metadata is indexed; LogQL can still filter log content, so absence of a full-text index does not mean absence of content search.

**Licence boundary:** Retain oss and assign AGPL-3.0-only as the documented Loki backend default. Actual LICENSE and LICENSING.md were read; listed client/protobuf/tooling Apache-2.0 exceptions and vendored licences are not relabelled.

**Commercial/service boundary:** commercial_offering=true records related Grafana commercial services, not a hosted deployment of this OSS binary. Grafana Cloud and the separately licensed Enterprise backend are distinct offerings. The official GEL setup notice says GEL, GEM and GET are in LTS through 2029-02-01; that notice does not retire Loki, Mimir or Tempo OSS.

**Repository boundary:** Retain grafana/loki and its official OSS product URL. Add the directly verified Loki documentation, not Cloud Logs documentation.

**Governance:** Official governance identifies team/maintainer decisions and Grafana Labs authority for governance changes. OSS community contributors participate; no independent CNCF status is asserted.

**Maturity:** Established follows maintained releases, documented deployment/query/storage and access-control operations, and an explicit upstream governance process.

**Lifecycle:** Non-archived upstream with 2026-10-07 activity and stable v3.7.8 (2026-09-17). The README announces OSS Helm-chart maintenance moving to grafana-community/helm-charts on 2026-03-16; this packaging move does not archive the Loki backend.

**Unresolved questions / limits:** None blocking backend scope. Tenant separation is not user authentication. Current docs separately describe native mTLS; no blanket claim that Loki cannot authenticate transport clients is made.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical Loki backend repository and scope][grafana-loki-e1], [Backend software licence][grafana-loki-e2], [Exact SPDX and component licence exceptions][grafana-loki-e3], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5], [Project governance][grafana-loki-e6], [Maintained release history][grafana-loki-e7], [Hosted Grafana Cloud product boundary][grafana-loki-e8], [Separate Enterprise backend support lifecycle][grafana-loki-e9].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | grafana-loki | grafana-loki | [Canonical Loki backend repository and scope][grafana-loki-e1] | Preserve stable catalogue ID and history; no duplicate record. |
| `name` | Grafana Loki | Grafana Loki | [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Log aggregation system designed to work with Grafana; label-based indexing. | Open-source log aggregation backend that indexes log labels and queries log content with LogQL; Grafana provides a separate UI and Grafana Cloud Logs is a managed offering. | [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://grafana.com/oss/loki | https://grafana.com/oss/loki | [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5] | Reviewed; retained: official entry point identified by the upstream project; any boundary correction is explained above. |
| `repository_url` | https://github.com/grafana/loki | https://github.com/grafana/loki | [Canonical Loki backend repository and scope][grafana-loki-e1] | Retain the verified scoped implementation repository. |
| `documentation_url` | *absent* | https://grafana.com/docs/loki/latest/ | [Official backend documentation][grafana-loki-e4] | Add the directly verified official documentation entry point. |
| `categories` | monitoring-metrics-logs-tracing | monitoring-metrics-logs-tracing | [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `subcategories` | Log Management | Log Management | [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `roles` | devops-engineer<br>site-reliability-engineer<br>observability-engineer | devops-engineer<br>site-reliability-engineer<br>observability-engineer | [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `lifecycle_stages` | operate<br>monitor | operate<br>monitor | [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `use_when` | You want cost-effective logs tightly integrated with Grafana dashboards. | You need label-based log aggregation with LogQL content filtering and can operate the log shipping, storage and access-control components alongside Loki. | [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5], [Backend software licence][grafana-loki-e2], [Exact SPDX and component licence exceptions][grafana-loki-e3] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `avoid_when` | You need full-text indexing or complex ad-hoc log analytics. | You require a full-text index of every log line or expect Loki tenant headers alone to authenticate users; configure an authenticating proxy or appropriate client-certificate controls. | [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5], [Backend software licence][grafana-loki-e2], [Exact SPDX and component licence exceptions][grafana-loki-e3] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `deployment_models` | `[]` | self-hosted | [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5], [Hosted Grafana Cloud product boundary][grafana-loki-e8], [Separate Enterprise backend support lifecycle][grafana-loki-e9] | Record software self-hosting; only Grafana parent includes hosted-saas for its explicitly named Cloud edition. |
| `license_model` | oss | oss | [Backend software licence][grafana-loki-e2], [Exact SPDX and component licence exceptions][grafana-loki-e3] | Reviewed; retained: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `license_spdx` | *absent* | AGPL-3.0-only | [Backend software licence][grafana-loki-e2], [Exact SPDX and component licence exceptions][grafana-loki-e3] | Changed: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Hosted Grafana Cloud product boundary][grafana-loki-e8], [Separate Enterprise backend support lifecycle][grafana-loki-e9] | Add true for the independently documented related commercial offering; OSS grant and software execution scope remain separate. |
| `maturity` | unknown | established | [Maintained release history][grafana-loki-e7], [Separate Enterprise backend support lifecycle][grafana-loki-e9], [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5], [Project governance][grafana-loki-e6] | Editorial established judgement from maintained releases/specifications, documented operations and governance; component stability is explicitly bounded. |
| `status` | needs-review | active | [Maintained release history][grafana-loki-e7], [Separate Enterprise backend support lifecycle][grafana-loki-e9], [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical Loki backend repository and scope][grafana-loki-e1], [Maintained release history][grafana-loki-e7], [Separate Enterprise backend support lifecycle][grafana-loki-e9] | GitHub API reports archived=false; actual release/activity evidence supports lifecycle separately. |
| `alternatives` | `[]` | `[]` | [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `tags` | `[]` | `[]` | [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical Loki backend repository and scope][grafana-loki-e1], [Backend software licence][grafana-loki-e2], [Exact SPDX and component licence exceptions][grafana-loki-e3], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5], [Project governance][grafana-loki-e6], [Maintained release history][grafana-loki-e7], [Hosted Grafana Cloud product boundary][grafana-loki-e8], [Separate Enterprise backend support lifecycle][grafana-loki-e9] | Actual review date, changed only for these ten records. |
| `sources` | legacy:5_Monitoring-Observability/README.md#L57<br>legacy:devopstools_final.md#L764 | legacy:5_Monitoring-Observability/README.md#L57<br>legacy:devopstools_final.md#L764<br>https://github.com/grafana/loki<br>https://github.com/grafana/loki/blob/main/LICENSE<br>https://github.com/grafana/loki/blob/main/LICENSING.md<br>https://grafana.com/docs/loki/latest/<br>https://grafana.com/docs/loki/latest/operations/authentication/<br>https://grafana.com/docs/loki/latest/community/governance/<br>https://github.com/grafana/loki/releases<br>https://grafana.com/docs/grafana/latest/introduction/grafana-cloud/<br>https://grafana.com/docs/enterprise-logs/latest/setup/ | [Canonical Loki backend repository and scope][grafana-loki-e1], [Backend software licence][grafana-loki-e2], [Exact SPDX and component licence exceptions][grafana-loki-e3], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5], [Project governance][grafana-loki-e6], [Maintained release history][grafana-loki-e7], [Hosted Grafana Cloud product boundary][grafana-loki-e8], [Separate Enterprise backend support lifecycle][grafana-loki-e9] | Preserve every legacy source and append checked primary sources, including the former OpenTelemetry organization pointer. |
| `needs_review` | `true` | `false` | [Maintained release history][grafana-loki-e7], [Separate Enterprise backend support lifecycle][grafana-loki-e9], [Canonical Loki backend repository and scope][grafana-loki-e1], [Official backend documentation][grafana-loki-e4], [Authentication and tenant boundary documentation][grafana-loki-e5] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[grafana-loki-e1]: https://github.com/grafana/loki
[grafana-loki-e2]: https://github.com/grafana/loki/blob/main/LICENSE
[grafana-loki-e3]: https://github.com/grafana/loki/blob/main/LICENSING.md
[grafana-loki-e4]: https://grafana.com/docs/loki/latest/
[grafana-loki-e5]: https://grafana.com/docs/loki/latest/operations/authentication/
[grafana-loki-e6]: https://grafana.com/docs/loki/latest/community/governance/
[grafana-loki-e7]: https://github.com/grafana/loki/releases
[grafana-loki-e8]: https://grafana.com/docs/grafana/latest/introduction/grafana-cloud/
[grafana-loki-e9]: https://grafana.com/docs/enterprise-logs/latest/setup/

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/grafana/loki) (`archived: false`).

### grafana-tempo

**Identity boundary:** Tempo is an OSS tracing backend with TraceQL search, not merely trace-ID lookup. The current configuration reference explicitly supports configurable OTLP, Jaeger and Zipkin receivers; these are ingestion protocols, not claims of identical backend APIs or automatic receiver enablement.

**Licence boundary:** Retain oss; actual README/LICENSING.md explicitly identify AGPL-3.0-only. operations/ and pkg/tempopb Apache-2.0 exceptions remain scoped components. No inference from the Grafana parent licence or Tempo datasource plugin is used.

**Commercial/service boundary:** commercial_offering=true records related Grafana commercial services, not a hosted deployment of this OSS binary. Grafana Cloud and the separately licensed Enterprise backend are distinct offerings. The official GEL setup notice says GEL, GEM and GET are in LTS through 2029-02-01; that notice does not retire Loki, Mimir or Tempo OSS.

**Repository boundary:** Keep grafana/tempo and the OSS official URL; add the Tempo documentation entry point, distinct from the Cloud service and Grafana UI repository.

**Governance:** Grafana upstream lists Tempo maintainers. This is Grafana-led OSS maintenance, not a separately claimed CNCF graduated project.

**Maturity:** Established follows maintained stable releases and documented receiver, query, deployment and storage operations; it does not assert every optional TraceQL metrics feature is stable.

**Lifecycle:** Non-archived upstream with 2026-10-07 activity and stable v3.1.0 (2026-09-29). Current docs distinguish monolithic mode without Kafka from microservices requiring a Kafka-compatible durable queue; older object-storage-only wording is not generalized across architectures.

**Unresolved questions / limits:** None blocking tracing backend scope. Verify receiver configuration and architecture-specific dependencies. Optional trace-derived metric features have their own stability status.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Backend software licence][grafana-tempo-e2], [Exact SPDX and component licence exceptions][grafana-tempo-e3], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5], [Project maintainers and governance boundary][grafana-tempo-e6], [Maintained release history][grafana-tempo-e7], [Hosted Grafana Cloud product boundary][grafana-tempo-e8], [Separate Enterprise backend support lifecycle][grafana-tempo-e9].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | grafana-tempo | grafana-tempo | [Canonical Tempo backend repository and scope][grafana-tempo-e1] | Preserve stable catalogue ID and history; no duplicate record. |
| `name` | Grafana Tempo | Grafana Tempo | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Distributed tracing backend (compatible with Jaeger/Zipkin/OTLP). | Open-source distributed tracing backend with TraceQL search and configurable OTLP, Jaeger and Zipkin receivers; Grafana Cloud Traces is a separate managed offering. | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://grafana.com/oss/tempo | https://grafana.com/oss/tempo | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5] | Reviewed; retained: official entry point identified by the upstream project; any boundary correction is explained above. |
| `repository_url` | https://github.com/grafana/tempo | https://github.com/grafana/tempo | [Canonical Tempo backend repository and scope][grafana-tempo-e1] | Retain the verified scoped implementation repository. |
| `documentation_url` | *absent* | https://grafana.com/docs/tempo/latest/ | [Official tracing backend documentation][grafana-tempo-e4] | Add the directly verified official documentation entry point. |
| `categories` | monitoring-metrics-logs-tracing | monitoring-metrics-logs-tracing | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `subcategories` | Visualization, Metrics, and Tracing | Distributed tracing backends | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5] | Changed: reviewer mapping of documented capability to the existing taxonomy. |
| `roles` | devops-engineer<br>site-reliability-engineer<br>observability-engineer | devops-engineer<br>site-reliability-engineer<br>observability-engineer | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `lifecycle_stages` | operate<br>monitor | operate<br>monitor | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `use_when` | Cost-effective trace storage using object storage and tight Grafana integration. | You need trace storage, TraceQL search and correlation with Grafana metrics/logs, with receivers configured for the required tracing protocols and a deployment architecture you can operate. | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5], [Backend software licence][grafana-tempo-e2], [Exact SPDX and component licence exceptions][grafana-tempo-e3] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `avoid_when` | You need trace analytics/aggregation beyond trace-by-ID lookups. | You require an included managed service or an architecture-independent object-storage-only deployment; verify ingestion, query and storage dependencies for your chosen deployment mode. | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5], [Backend software licence][grafana-tempo-e2], [Exact SPDX and component licence exceptions][grafana-tempo-e3] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `deployment_models` | `[]` | self-hosted | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5], [Hosted Grafana Cloud product boundary][grafana-tempo-e8], [Separate Enterprise backend support lifecycle][grafana-tempo-e9] | Record software self-hosting; only Grafana parent includes hosted-saas for its explicitly named Cloud edition. |
| `license_model` | oss | oss | [Backend software licence][grafana-tempo-e2], [Exact SPDX and component licence exceptions][grafana-tempo-e3] | Reviewed; retained: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `license_spdx` | *absent* | AGPL-3.0-only | [Backend software licence][grafana-tempo-e2], [Exact SPDX and component licence exceptions][grafana-tempo-e3] | Changed: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Hosted Grafana Cloud product boundary][grafana-tempo-e8], [Separate Enterprise backend support lifecycle][grafana-tempo-e9] | Add true for the independently documented related commercial offering; OSS grant and software execution scope remain separate. |
| `maturity` | unknown | established | [Maintained release history][grafana-tempo-e7], [Separate Enterprise backend support lifecycle][grafana-tempo-e9], [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5], [Project maintainers and governance boundary][grafana-tempo-e6] | Editorial established judgement from maintained releases/specifications, documented operations and governance; component stability is explicitly bounded. |
| `status` | needs-review | active | [Maintained release history][grafana-tempo-e7], [Separate Enterprise backend support lifecycle][grafana-tempo-e9], [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Maintained release history][grafana-tempo-e7], [Separate Enterprise backend support lifecycle][grafana-tempo-e9] | GitHub API reports archived=false; actual release/activity evidence supports lifecycle separately. |
| `alternatives` | `[]` | `[]` | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `tags` | `[]` | `[]` | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Backend software licence][grafana-tempo-e2], [Exact SPDX and component licence exceptions][grafana-tempo-e3], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5], [Project maintainers and governance boundary][grafana-tempo-e6], [Maintained release history][grafana-tempo-e7], [Hosted Grafana Cloud product boundary][grafana-tempo-e8], [Separate Enterprise backend support lifecycle][grafana-tempo-e9] | Actual review date, changed only for these ten records. |
| `sources` | legacy:5_Monitoring-Observability/README.md#L42<br>legacy:devopstools_final.md#L747 | legacy:5_Monitoring-Observability/README.md#L42<br>legacy:devopstools_final.md#L747<br>https://github.com/grafana/tempo<br>https://github.com/grafana/tempo/blob/main/LICENSE<br>https://github.com/grafana/tempo/blob/main/LICENSING.md<br>https://grafana.com/docs/tempo/latest/<br>https://grafana.com/docs/tempo/latest/configuration/<br>https://github.com/grafana/tempo/blob/main/MAINTAINERS.md<br>https://github.com/grafana/tempo/releases<br>https://grafana.com/docs/grafana/latest/introduction/grafana-cloud/<br>https://grafana.com/docs/enterprise-logs/latest/setup/ | [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Backend software licence][grafana-tempo-e2], [Exact SPDX and component licence exceptions][grafana-tempo-e3], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5], [Project maintainers and governance boundary][grafana-tempo-e6], [Maintained release history][grafana-tempo-e7], [Hosted Grafana Cloud product boundary][grafana-tempo-e8], [Separate Enterprise backend support lifecycle][grafana-tempo-e9] | Preserve every legacy source and append checked primary sources, including the former OpenTelemetry organization pointer. |
| `needs_review` | `true` | `false` | [Maintained release history][grafana-tempo-e7], [Separate Enterprise backend support lifecycle][grafana-tempo-e9], [Canonical Tempo backend repository and scope][grafana-tempo-e1], [Official tracing backend documentation][grafana-tempo-e4], [Receiver protocols and deployment architecture documentation][grafana-tempo-e5] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[grafana-tempo-e1]: https://github.com/grafana/tempo
[grafana-tempo-e2]: https://github.com/grafana/tempo/blob/main/LICENSE
[grafana-tempo-e3]: https://github.com/grafana/tempo/blob/main/LICENSING.md
[grafana-tempo-e4]: https://grafana.com/docs/tempo/latest/
[grafana-tempo-e5]: https://grafana.com/docs/tempo/latest/configuration/
[grafana-tempo-e6]: https://github.com/grafana/tempo/blob/main/MAINTAINERS.md
[grafana-tempo-e7]: https://github.com/grafana/tempo/releases
[grafana-tempo-e8]: https://grafana.com/docs/grafana/latest/introduction/grafana-cloud/
[grafana-tempo-e9]: https://grafana.com/docs/enterprise-logs/latest/setup/

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/grafana/tempo) (`archived: false`).

### grafana-mimir

**Identity boundary:** Mimir is the current independently named Prometheus-compatible long-term metrics backend. Multi-tenant ingestion and global queries are software capabilities; Cloud Metrics is a distinct managed offering. No unsupported better-than-Thanos selection ranking remains.

**Licence boundary:** Retain oss and assign the explicitly documented AGPL-3.0-only default. cmd/mimir/main.go separately records historical Cortex Apache-2.0 provenance; that history does not replace the current software licence. LICENSING.md retains upstream licences in vendor/ and operations/.

**Commercial/service boundary:** commercial_offering=true records related Grafana commercial services, not a hosted deployment of this OSS binary. Grafana Cloud and the separately licensed Enterprise backend are distinct offerings. The official GEL setup notice says GEL, GEM and GET are in LTS through 2029-02-01; that notice does not retire Loki, Mimir or Tempo OSS.

**Repository boundary:** Retain grafana/mimir, not the historical Cortex repository or Grafana Cloud implementation. Add current Mimir documentation.

**Governance:** The upstream MAINTAINERS.md explicitly lists Grafana Labs maintainers. No CNCF foundation level is inherited from Cortex or Prometheus.

**Maturity:** Established follows maintained stable releases, documented operations and long-term/multi-tenant storage architecture. Individual ingest architectures and dependencies must be evaluated separately.

**Lifecycle:** Non-archived upstream with 2026-10-07 activity and stable mimir-3.2.2 (2026-10-07). Maintained release and architecture documentation support active status independently of Enterprise Metrics LTS.

**Unresolved questions / limits:** None blocking current backend identity. The backend requires deliberate storage/ingestion and tenant authentication configuration; Enterprise/Cloud support and entitlements are separate.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Backend software licence][grafana-mimir-e2], [Exact SPDX and vendored licence exceptions][grafana-mimir-e3], [Current executable SPDX and Cortex provenance][grafana-mimir-e4], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6], [Project maintainers and governance boundary][grafana-mimir-e7], [Maintained release history][grafana-mimir-e8], [Hosted Grafana Cloud product boundary][grafana-mimir-e9], [Separate Enterprise backend support lifecycle][grafana-mimir-e10].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | grafana-mimir | grafana-mimir | [Canonical Mimir backend repository and scope][grafana-mimir-e1] | Preserve stable catalogue ID and history; no duplicate record. |
| `name` | Grafana Mimir | Grafana Mimir | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Horizontally scalable, multi-tenant Prometheus-compatible time series database. | Open-source Prometheus-compatible metrics backend for multi-tenant ingestion, global PromQL queries and long-term object storage; Grafana Cloud Metrics is a separate managed offering. | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://grafana.com/oss/mimir | https://grafana.com/oss/mimir | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6] | Reviewed; retained: official entry point identified by the upstream project; any boundary correction is explained above. |
| `repository_url` | https://github.com/grafana/mimir | https://github.com/grafana/mimir | [Canonical Mimir backend repository and scope][grafana-mimir-e1] | Retain the verified scoped implementation repository. |
| `documentation_url` | *absent* | https://grafana.com/docs/mimir/latest/ | [Official backend documentation][grafana-mimir-e5] | Add the directly verified official documentation entry point. |
| `categories` | monitoring-metrics-logs-tracing | monitoring-metrics-logs-tracing | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `subcategories` | Visualization, Metrics, and Tracing | Long-term metrics storage | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6] | Changed: reviewer mapping of documented capability to the existing taxonomy. |
| `roles` | devops-engineer<br>site-reliability-engineer<br>observability-engineer | devops-engineer<br>site-reliability-engineer<br>observability-engineer | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `lifecycle_stages` | operate<br>monitor | operate<br>monitor | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `use_when` | You outgrow single-node Prometheus and need multi-tenant long-term storage. | You need Prometheus-compatible long-term metrics storage, multi-tenant isolation and queries across multiple metrics sources, and can operate the required storage and ingestion architecture. | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6], [Backend software licence][grafana-mimir-e2], [Exact SPDX and vendored licence exceptions][grafana-mimir-e3], [Current executable SPDX and Cortex provenance][grafana-mimir-e4] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `avoid_when` | Thanos already solves your HA/storage needs, or your scale is small. | You only need a standalone local metrics server or expect the OSS backend to include Grafana Cloud management, commercial entitlements or automatic tenant authentication. | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6], [Backend software licence][grafana-mimir-e2], [Exact SPDX and vendored licence exceptions][grafana-mimir-e3], [Current executable SPDX and Cortex provenance][grafana-mimir-e4] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `deployment_models` | `[]` | self-hosted | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6], [Hosted Grafana Cloud product boundary][grafana-mimir-e9], [Separate Enterprise backend support lifecycle][grafana-mimir-e10] | Record software self-hosting; only Grafana parent includes hosted-saas for its explicitly named Cloud edition. |
| `license_model` | oss | oss | [Backend software licence][grafana-mimir-e2], [Exact SPDX and vendored licence exceptions][grafana-mimir-e3], [Current executable SPDX and Cortex provenance][grafana-mimir-e4] | Reviewed; retained: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `license_spdx` | *absent* | AGPL-3.0-only | [Backend software licence][grafana-mimir-e2], [Exact SPDX and vendored licence exceptions][grafana-mimir-e3], [Current executable SPDX and Cortex provenance][grafana-mimir-e4] | Changed: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `commercial_offering` | *absent* | `true` | [Hosted Grafana Cloud product boundary][grafana-mimir-e9], [Separate Enterprise backend support lifecycle][grafana-mimir-e10] | Add true for the independently documented related commercial offering; OSS grant and software execution scope remain separate. |
| `maturity` | unknown | established | [Maintained release history][grafana-mimir-e8], [Separate Enterprise backend support lifecycle][grafana-mimir-e10], [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6], [Project maintainers and governance boundary][grafana-mimir-e7] | Editorial established judgement from maintained releases/specifications, documented operations and governance; component stability is explicitly bounded. |
| `status` | needs-review | active | [Maintained release history][grafana-mimir-e8], [Separate Enterprise backend support lifecycle][grafana-mimir-e10], [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Maintained release history][grafana-mimir-e8], [Separate Enterprise backend support lifecycle][grafana-mimir-e10] | GitHub API reports archived=false; actual release/activity evidence supports lifecycle separately. |
| `alternatives` | `[]` | `[]` | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `tags` | `[]` | `[]` | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Backend software licence][grafana-mimir-e2], [Exact SPDX and vendored licence exceptions][grafana-mimir-e3], [Current executable SPDX and Cortex provenance][grafana-mimir-e4], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6], [Project maintainers and governance boundary][grafana-mimir-e7], [Maintained release history][grafana-mimir-e8], [Hosted Grafana Cloud product boundary][grafana-mimir-e9], [Separate Enterprise backend support lifecycle][grafana-mimir-e10] | Actual review date, changed only for these ten records. |
| `sources` | legacy:5_Monitoring-Observability/README.md#L41<br>legacy:devopstools_final.md#L746 | legacy:5_Monitoring-Observability/README.md#L41<br>legacy:devopstools_final.md#L746<br>https://github.com/grafana/mimir<br>https://github.com/grafana/mimir/blob/main/LICENSE<br>https://github.com/grafana/mimir/blob/main/LICENSING.md<br>https://github.com/grafana/mimir/blob/main/cmd/mimir/main.go<br>https://grafana.com/docs/mimir/latest/<br>https://grafana.com/docs/mimir/latest/manage/secure/authentication-and-authorization/<br>https://github.com/grafana/mimir/blob/main/MAINTAINERS.md<br>https://github.com/grafana/mimir/releases<br>https://grafana.com/docs/grafana/latest/introduction/grafana-cloud/<br>https://grafana.com/docs/enterprise-logs/latest/setup/ | [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Backend software licence][grafana-mimir-e2], [Exact SPDX and vendored licence exceptions][grafana-mimir-e3], [Current executable SPDX and Cortex provenance][grafana-mimir-e4], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6], [Project maintainers and governance boundary][grafana-mimir-e7], [Maintained release history][grafana-mimir-e8], [Hosted Grafana Cloud product boundary][grafana-mimir-e9], [Separate Enterprise backend support lifecycle][grafana-mimir-e10] | Preserve every legacy source and append checked primary sources, including the former OpenTelemetry organization pointer. |
| `needs_review` | `true` | `false` | [Maintained release history][grafana-mimir-e8], [Separate Enterprise backend support lifecycle][grafana-mimir-e10], [Canonical Mimir backend repository and scope][grafana-mimir-e1], [Official backend documentation][grafana-mimir-e5], [Tenant authentication boundary documentation][grafana-mimir-e6] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `commercial_offering`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[grafana-mimir-e1]: https://github.com/grafana/mimir
[grafana-mimir-e2]: https://github.com/grafana/mimir/blob/main/LICENSE
[grafana-mimir-e3]: https://github.com/grafana/mimir/blob/main/LICENSING.md
[grafana-mimir-e4]: https://github.com/grafana/mimir/blob/main/cmd/mimir/main.go
[grafana-mimir-e5]: https://grafana.com/docs/mimir/latest/
[grafana-mimir-e6]: https://grafana.com/docs/mimir/latest/manage/secure/authentication-and-authorization/
[grafana-mimir-e7]: https://github.com/grafana/mimir/blob/main/MAINTAINERS.md
[grafana-mimir-e8]: https://github.com/grafana/mimir/releases
[grafana-mimir-e9]: https://grafana.com/docs/grafana/latest/introduction/grafana-cloud/
[grafana-mimir-e10]: https://grafana.com/docs/enterprise-logs/latest/setup/

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/grafana/mimir) (`archived: false`).

### opentelemetry

**Identity boundary:** The umbrella includes specifications, APIs/SDKs, semantic conventions and instrumentation, with the Collector as a component. It is not one Collector distribution or a backend. Development-stage instrumentation belongs alongside operate/monitor in the taxonomy.

**Licence boundary:** Retain oss and assign Apache-2.0 to the umbrella software boundary: the community README explicitly states all OpenTelemetry projects ship under Apache 2.0, independently corroborated by the actual community LICENSE and specification grant. This is direct project software policy, not an inference from CNCF status, and does not license trademarks or third-party vendor products.

**Commercial/service boundary:** Leave optional commercial_offering absent: vendor distributions and telemetry backends may be commercial, but this umbrella is not one vendor service. Leave deployment_models empty because SDKs in applications and deployed Collector components do not define one umbrella control-plane deployment.

**Repository boundary:** Keep repository_url and repository_archived absent. The canonical specification repo defines cross-language requirements; community repo defines governance; Collector and language repos implement different parts. None represents all umbrella software. Change official_url from GitHub organization to the official project site and preserve the organization pointer in sources.

**Governance:** The community defines Governance and Technical Committees and component SIGs. CNCF directly records graduation on 2026-05-11; this does not make every SDK, signal or Collector component stable.

**Maturity:** Established is a reviewer judgement from maintained specifications, stable API/SDK signals documented across multiple languages and explicit operational/governance structure. The status matrix remains component- and signal-specific.

**Lifecycle:** Active umbrella with maintained specification/SDK documentation and status matrices; current Collector component releases corroborate ongoing implementation work without substituting Collector identity. CNCF directly records a 2026 graduation milestone.

**Unresolved questions / limits:** None blocking umbrella scope. Repository absence is deliberate rather than unresolved identity debt. Language/signal/component stability varies; vendor terms and external storage/UI remain outside the Apache software-policy assertion.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Canonical community repository and project-wide software licence policy][opentelemetry-e4], [Community software licence][opentelemetry-e5], [Governance Committee charter][opentelemetry-e6], [Specification repository and implementation boundary][opentelemetry-e7], [Component maturity and stability documentation][opentelemetry-e8], [CNCF foundation status][opentelemetry-e9].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | opentelemetry | opentelemetry | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Canonical community repository and project-wide software licence policy][opentelemetry-e4], [Specification repository and implementation boundary][opentelemetry-e7] | Preserve stable catalogue ID and history; no duplicate record. |
| `name` | OpenTelemetry | OpenTelemetry | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Component maturity and stability documentation][opentelemetry-e8] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Observability framework for traces/metrics/logs. | Vendor-neutral observability umbrella project defining specifications, APIs, SDKs and instrumentation for traces, metrics and logs; the Collector is a separate implementation component, and storage/UI backends are external. | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Component maturity and stability documentation][opentelemetry-e8] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://github.com/open-telemetry | https://opentelemetry.io/ | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Canonical community repository and project-wide software licence policy][opentelemetry-e4], [Specification repository and implementation boundary][opentelemetry-e7], [Component maturity and stability documentation][opentelemetry-e8] | Changed: official entry point identified by the upstream project; any boundary correction is explained above. |
| `repository_url` | *absent* | *absent* | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Canonical community repository and project-wide software licence policy][opentelemetry-e4], [Specification repository and implementation boundary][opentelemetry-e7] | Leave absent: specification, community, SDK and Collector repositories each cover only part of the umbrella; none is substituted to reduce debt. |
| `documentation_url` | *absent* | https://opentelemetry.io/docs/ | [Official umbrella documentation][opentelemetry-e2] | Add the directly verified official documentation entry point. |
| `categories` | monitoring-metrics-logs-tracing | monitoring-metrics-logs-tracing | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Component maturity and stability documentation][opentelemetry-e8] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `subcategories` | Visualization, Metrics, and Tracing | Telemetry instrumentation and standards | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Component maturity and stability documentation][opentelemetry-e8] | Changed: reviewer mapping of documented capability to the existing taxonomy. |
| `roles` | devops-engineer<br>site-reliability-engineer<br>observability-engineer | devops-engineer<br>site-reliability-engineer<br>observability-engineer | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Component maturity and stability documentation][opentelemetry-e8] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `lifecycle_stages` | operate<br>monitor | develop<br>operate<br>monitor | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Component maturity and stability documentation][opentelemetry-e8] | Changed: reviewer mapping of documented capability to the existing taxonomy. |
| `use_when` | You want vendor-neutral instrumentation and backend flexibility. | You need portable instrumentation and telemetry APIs/SDKs across services, with an independently chosen Collector pipeline and observability backend. | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Component maturity and stability documentation][opentelemetry-e8], [Canonical community repository and project-wide software licence policy][opentelemetry-e4], [Community software licence][opentelemetry-e5] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `avoid_when` | Your team isn&#x27;t ready to learn OTel&#x27;s configuration surface and maturity varies per language SDK. | You need an included telemetry storage/UI backend or uniform stability across every language, signal and component; check the relevant specification and implementation status first. | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Component maturity and stability documentation][opentelemetry-e8], [Canonical community repository and project-wide software licence policy][opentelemetry-e4], [Community software licence][opentelemetry-e5] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `deployment_models` | `[]` | `[]` | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Component maturity and stability documentation][opentelemetry-e8] | Leave empty: application SDKs and deployed components do not form a single umbrella control-plane deployment. |
| `license_model` | oss | oss | [Canonical community repository and project-wide software licence policy][opentelemetry-e4], [Community software licence][opentelemetry-e5] | Reviewed; retained: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Canonical community repository and project-wide software licence policy][opentelemetry-e4], [Community software licence][opentelemetry-e5] | Changed: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Canonical community repository and project-wide software licence policy][opentelemetry-e4], [Specification repository and implementation boundary][opentelemetry-e7] | Leave optional field absent; no blanket claim about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Component maturity and stability documentation][opentelemetry-e8], [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Governance Committee charter][opentelemetry-e6], [CNCF foundation status][opentelemetry-e9] | Editorial established judgement from maintained releases/specifications, documented operations and governance; component stability is explicitly bounded. |
| `status` | needs-review | active | [Component maturity and stability documentation][opentelemetry-e8], [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | *absent* | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Canonical community repository and project-wide software licence policy][opentelemetry-e4], [Specification repository and implementation boundary][opentelemetry-e7], [Component maturity and stability documentation][opentelemetry-e8] | Leave absent with the umbrella repository; do not inherit a component archival flag. |
| `alternatives` | `[]` | `[]` | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Component maturity and stability documentation][opentelemetry-e8] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `tags` | `[]` | `[]` | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Component maturity and stability documentation][opentelemetry-e8] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Canonical community repository and project-wide software licence policy][opentelemetry-e4], [Community software licence][opentelemetry-e5], [Governance Committee charter][opentelemetry-e6], [Specification repository and implementation boundary][opentelemetry-e7], [Component maturity and stability documentation][opentelemetry-e8], [CNCF foundation status][opentelemetry-e9] | Actual review date, changed only for these ten records. |
| `sources` | legacy:5_Monitoring-Observability/README.md#L46<br>legacy:devopstools_final.md#L751 | legacy:5_Monitoring-Observability/README.md#L46<br>legacy:devopstools_final.md#L751<br>https://opentelemetry.io/<br>https://opentelemetry.io/docs/<br>https://opentelemetry.io/docs/what-is-opentelemetry/<br>https://github.com/open-telemetry/community/blob/main/README.md<br>https://github.com/open-telemetry/community/blob/main/LICENSE<br>https://github.com/open-telemetry/community/blob/main/governance-charter.md<br>https://github.com/open-telemetry/opentelemetry-specification/blob/main/README.md<br>https://opentelemetry.io/status/<br>https://www.cncf.io/projects/opentelemetry/<br>https://github.com/open-telemetry | [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3], [Canonical community repository and project-wide software licence policy][opentelemetry-e4], [Community software licence][opentelemetry-e5], [Governance Committee charter][opentelemetry-e6], [Specification repository and implementation boundary][opentelemetry-e7], [Component maturity and stability documentation][opentelemetry-e8], [CNCF foundation status][opentelemetry-e9] | Preserve every legacy source and append checked primary sources, including the former OpenTelemetry organization pointer. |
| `needs_review` | `true` | `false` | [Component maturity and stability documentation][opentelemetry-e8], [Official umbrella project site and identity][opentelemetry-e1], [Official umbrella documentation][opentelemetry-e2], [Umbrella scope and external backend documentation][opentelemetry-e3] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `official_url`, `documentation_url`, `subcategories`, `lifecycle_stages`, `use_when`, `avoid_when`, `license_spdx`, `maturity`, `status`, `verified_on`, `sources`, `needs_review`.

[opentelemetry-e1]: https://opentelemetry.io/
[opentelemetry-e2]: https://opentelemetry.io/docs/
[opentelemetry-e3]: https://opentelemetry.io/docs/what-is-opentelemetry/
[opentelemetry-e4]: https://github.com/open-telemetry/community/blob/main/README.md
[opentelemetry-e5]: https://github.com/open-telemetry/community/blob/main/LICENSE
[opentelemetry-e6]: https://github.com/open-telemetry/community/blob/main/governance-charter.md
[opentelemetry-e7]: https://github.com/open-telemetry/opentelemetry-specification/blob/main/README.md
[opentelemetry-e8]: https://opentelemetry.io/status/
[opentelemetry-e9]: https://www.cncf.io/projects/opentelemetry/

### opentelemetry-collector

**Identity boundary:** Collector is the receive/process/export implementation for multiple signals, distinct from the OpenTelemetry umbrella and storage/UI backends. Replace the tracing-only subcategory with telemetry collection/processing.

**Licence boundary:** Apache-2.0 is verified from the core repository LICENSE. The core grant is not asserted as the licence of every external vendor distribution or telemetry backend.

**Commercial/service boundary:** Leave optional commercial_offering absent; third-party vendor distributions/services are not the upstream core implementation. Agent and gateway execution are self-hosted pipeline modes, not a hosted storage service.

**Repository boundary:** Keep open-telemetry/opentelemetry-collector for the core framework and components. opentelemetry-collector-contrib is separate; prebuilt core/contrib/custom distributions use different component manifests. No substitution of contrib for core.

**Governance:** The Collector SIG and documented upstream maintainers operate within OpenTelemetry governance. It is a component of OpenTelemetry, not a separately claimed CNCF graduation.

**Maturity:** Established is a reviewer judgement for the maintained pipeline/framework and documented operations. Per-component and per-signal stability levels override any assumption that established means uniformly stable.

**Lifecycle:** Non-archived core upstream with 2026-10-07 activity and release v0.162.0 (2026-09-28). Regular releases and explicit stability/versioning policy support active maintenance; not every module or signal is stable.

**Unresolved questions / limits:** None blocking core pipeline identity. Required components must be checked in the selected distribution manifest, and stability assessed per component/signal.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Core software licence][opentelemetry-collector-e2], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5], [Component stability policy][opentelemetry-collector-e6], [SIG and maintainer governance][opentelemetry-collector-e7], [Maintained release history][opentelemetry-collector-e8].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | opentelemetry-collector | opentelemetry-collector | [Canonical core implementation repository and scope][opentelemetry-collector-e1] | Preserve stable catalogue ID and history; no duplicate record. |
| `name` | OpenTelemetry Collector | OpenTelemetry Collector | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Vendor-neutral collector to receive/process/export traces (and also logs/metrics) to backends. | Vendor-neutral telemetry pipeline implementation using receivers, processors and exporters for traces, metrics and logs; the core framework repository and the contrib component repository are distinct. | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://opentelemetry.io/docs/collector | https://opentelemetry.io/docs/collector | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5] | Reviewed; retained: official entry point identified by the upstream project; any boundary correction is explained above. |
| `repository_url` | https://github.com/open-telemetry/opentelemetry-collector | https://github.com/open-telemetry/opentelemetry-collector | [Canonical core implementation repository and scope][opentelemetry-collector-e1] | Retain the verified scoped implementation repository. |
| `documentation_url` | *absent* | https://opentelemetry.io/docs/collector/ | [Official Collector documentation][opentelemetry-collector-e3] | Add the directly verified official documentation entry point. |
| `categories` | monitoring-metrics-logs-tracing | monitoring-metrics-logs-tracing | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `subcategories` | Tracing &amp; APM | Telemetry collection and processing | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5] | Changed: reviewer mapping of documented capability to the existing taxonomy. |
| `roles` | devops-engineer<br>site-reliability-engineer<br>observability-engineer | devops-engineer<br>site-reliability-engineer<br>observability-engineer | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `lifecycle_stages` | operate<br>monitor | operate<br>monitor | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `use_when` | You want a single, vendor-agnostic telemetry pipeline. | You need a configurable agent or gateway to receive, process and export telemetry to separately selected backends, using a distribution containing the required components. | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5], [Core software licence][opentelemetry-collector-e2] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `avoid_when` | A simpler agent (Fluent Bit, Telegraf) already covers your single-signal needs. | You need a telemetry storage/UI backend or assume the core distribution includes every contrib receiver/exporter and that all components and signals have equal stability. | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5], [Core software licence][opentelemetry-collector-e2] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `deployment_models` | `[]` | self-hosted | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5] | Record software self-hosting; only Grafana parent includes hosted-saas for its explicitly named Cloud edition. |
| `license_model` | oss | oss | [Core software licence][opentelemetry-collector-e2] | Reviewed; retained: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Core software licence][opentelemetry-collector-e2] | Changed: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Canonical core implementation repository and scope][opentelemetry-collector-e1] | Leave optional field absent; no blanket claim about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Component stability policy][opentelemetry-collector-e6], [Maintained release history][opentelemetry-collector-e8], [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5], [SIG and maintainer governance][opentelemetry-collector-e7] | Editorial established judgement from maintained releases/specifications, documented operations and governance; component stability is explicitly bounded. |
| `status` | needs-review | active | [Component stability policy][opentelemetry-collector-e6], [Maintained release history][opentelemetry-collector-e8], [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Component stability policy][opentelemetry-collector-e6], [Maintained release history][opentelemetry-collector-e8] | GitHub API reports archived=false; actual release/activity evidence supports lifecycle separately. |
| `alternatives` | `[]` | `[]` | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `tags` | `[]` | `[]` | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Core software licence][opentelemetry-collector-e2], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5], [Component stability policy][opentelemetry-collector-e6], [SIG and maintainer governance][opentelemetry-collector-e7], [Maintained release history][opentelemetry-collector-e8] | Actual review date, changed only for these ten records. |
| `sources` | legacy:5_Monitoring-Observability/README.md#L72<br>legacy:devopstools_final.md#L780 | legacy:5_Monitoring-Observability/README.md#L72<br>legacy:devopstools_final.md#L780<br>https://github.com/open-telemetry/opentelemetry-collector<br>https://github.com/open-telemetry/opentelemetry-collector/blob/main/LICENSE<br>https://opentelemetry.io/docs/collector/<br>https://opentelemetry.io/docs/collector/configuration/<br>https://opentelemetry.io/docs/collector/distributions/<br>https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/component-stability.md<br>https://github.com/open-telemetry/opentelemetry-collector/blob/main/README.md<br>https://github.com/open-telemetry/opentelemetry-collector/releases | [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Core software licence][opentelemetry-collector-e2], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5], [Component stability policy][opentelemetry-collector-e6], [SIG and maintainer governance][opentelemetry-collector-e7], [Maintained release history][opentelemetry-collector-e8] | Preserve every legacy source and append checked primary sources, including the former OpenTelemetry organization pointer. |
| `needs_review` | `true` | `false` | [Component stability policy][opentelemetry-collector-e6], [Maintained release history][opentelemetry-collector-e8], [Canonical core implementation repository and scope][opentelemetry-collector-e1], [Official Collector documentation][opentelemetry-collector-e3], [Receiver, processor and exporter pipeline documentation][opentelemetry-collector-e4], [Core versus contrib distribution documentation][opentelemetry-collector-e5] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[opentelemetry-collector-e1]: https://github.com/open-telemetry/opentelemetry-collector
[opentelemetry-collector-e2]: https://github.com/open-telemetry/opentelemetry-collector/blob/main/LICENSE
[opentelemetry-collector-e3]: https://opentelemetry.io/docs/collector/
[opentelemetry-collector-e4]: https://opentelemetry.io/docs/collector/configuration/
[opentelemetry-collector-e5]: https://opentelemetry.io/docs/collector/distributions/
[opentelemetry-collector-e6]: https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/component-stability.md
[opentelemetry-collector-e7]: https://github.com/open-telemetry/opentelemetry-collector/blob/main/README.md
[opentelemetry-collector-e8]: https://github.com/open-telemetry/opentelemetry-collector/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/open-telemetry/opentelemetry-collector) (`archived: false`).

### jaeger

**Identity boundary:** Jaeger remains the distributed tracing backend and UI. Current Jaeger is built on the OpenTelemetry Collector framework with Jaeger storage/query components; this integration does not deprecate Jaeger or make it the OpenTelemetry umbrella.

**Licence boundary:** Apache-2.0 is verified from the canonical Jaeger source LICENSE, independently of CNCF hosting and OpenTelemetry implementation relationships.

**Commercial/service boundary:** No vendor-hosted product is implied; leave optional commercial_offering absent rather than assigning all third-party tracing services to the project. Self-hosted supports both all-in-one and separated roles.

**Repository boundary:** Retain jaegertracing/jaeger. Add the stable official docs index; the architecture/deployment pages read during this review are 2.21, the version selected by the official index, while the API already lists v2.22.0. This publication lag does not imply archival.

**Governance:** Project GOVERNANCE.md defines maintainer authority and decisions. CNCF directly confirms graduation on 2019-10-31; this does not replace source licensing or release evidence.

**Maturity:** Established follows long maintained release history, current supported tracing architecture and documented storage/deployment/operations, with explicit maintainer governance.

**Lifecycle:** Non-archived repository with 2026-10-07 activity and stable v2.22.0 (2026-10-06). Official docs index selects the current 2.x line while 1.76 is an archive; historical v1 archive is not retirement of current Jaeger.

**Unresolved questions / limits:** None blocking current Jaeger scope. Storage support and configuration compatibility are version-dependent; the documentation index and latest release publication can lag one another.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical tracing backend repository and scope][jaeger-e1], [Backend software licence][jaeger-e2], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6], [Project governance][jaeger-e7], [CNCF foundation status][jaeger-e8], [Maintained release history][jaeger-e9].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | jaeger | jaeger | [Canonical tracing backend repository and scope][jaeger-e1] | Preserve stable catalogue ID and history; no duplicate record. |
| `name` | Jaeger | Jaeger | [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Open source distributed tracing platform. | Open-source distributed tracing backend with trace storage, query APIs and UI; current Jaeger builds on the OpenTelemetry Collector framework and accepts OpenTelemetry instrumentation. | [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://www.jaegertracing.io | https://www.jaegertracing.io | [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6] | Reviewed; retained: official entry point identified by the upstream project; any boundary correction is explained above. |
| `repository_url` | https://github.com/jaegertracing/jaeger | https://github.com/jaegertracing/jaeger | [Canonical tracing backend repository and scope][jaeger-e1] | Retain the verified scoped implementation repository. |
| `documentation_url` | *absent* | https://www.jaegertracing.io/docs/ | [Official documentation index][jaeger-e3] | Add the directly verified official documentation entry point. |
| `categories` | monitoring-metrics-logs-tracing | monitoring-metrics-logs-tracing | [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `subcategories` | Tracing &amp; APM | Tracing &amp; APM | [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `roles` | devops-engineer<br>site-reliability-engineer<br>observability-engineer | devops-engineer<br>site-reliability-engineer<br>observability-engineer | [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `lifecycle_stages` | operate<br>monitor | operate<br>monitor | [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `use_when` | CNCF-native distributed tracing with mature UI and backend options. | You need a self-hosted tracing backend with query/UI and supported storage backends, accepting OTLP from OpenTelemetry-instrumented applications or collectors. | [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6], [Backend software licence][jaeger-e2] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `avoid_when` | You need an all-in-one observability platform—Jaeger is tracing-only. | You require a single backend for storing logs, metrics and traces, or durable production retention while using only the temporary in-memory tracing configuration. | [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6], [Backend software licence][jaeger-e2] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `deployment_models` | `[]` | self-hosted | [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6] | Record software self-hosting; only Grafana parent includes hosted-saas for its explicitly named Cloud edition. |
| `license_model` | oss | oss | [Backend software licence][jaeger-e2] | Reviewed; retained: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Backend software licence][jaeger-e2] | Changed: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Canonical tracing backend repository and scope][jaeger-e1] | Leave optional field absent; no blanket claim about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Maintained release history][jaeger-e9], [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6], [Project governance][jaeger-e7], [CNCF foundation status][jaeger-e8] | Editorial established judgement from maintained releases/specifications, documented operations and governance; component stability is explicitly bounded. |
| `status` | needs-review | active | [Maintained release history][jaeger-e9], [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical tracing backend repository and scope][jaeger-e1], [Maintained release history][jaeger-e9] | GitHub API reports archived=false; actual release/activity evidence supports lifecycle separately. |
| `alternatives` | `[]` | `[]` | [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `tags` | `[]` | `[]` | [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical tracing backend repository and scope][jaeger-e1], [Backend software licence][jaeger-e2], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6], [Project governance][jaeger-e7], [CNCF foundation status][jaeger-e8], [Maintained release history][jaeger-e9] | Actual review date, changed only for these ten records. |
| `sources` | legacy:5_Monitoring-Observability/README.md#L71<br>legacy:devopstools_final.md#L779 | legacy:5_Monitoring-Observability/README.md#L71<br>legacy:devopstools_final.md#L779<br>https://github.com/jaegertracing/jaeger<br>https://github.com/jaegertracing/jaeger/blob/main/LICENSE<br>https://www.jaegertracing.io/docs/<br>https://www.jaegertracing.io/docs/2.21/architecture/<br>https://www.jaegertracing.io/docs/2.21/deployment/<br>https://www.jaegertracing.io/docs/2.21/storage/memory/<br>https://github.com/jaegertracing/jaeger/blob/main/GOVERNANCE.md<br>https://www.cncf.io/projects/jaeger/<br>https://github.com/jaegertracing/jaeger/releases | [Canonical tracing backend repository and scope][jaeger-e1], [Backend software licence][jaeger-e2], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6], [Project governance][jaeger-e7], [CNCF foundation status][jaeger-e8], [Maintained release history][jaeger-e9] | Preserve every legacy source and append checked primary sources, including the former OpenTelemetry organization pointer. |
| `needs_review` | `true` | `false` | [Maintained release history][jaeger-e9], [Canonical tracing backend repository and scope][jaeger-e1], [Official documentation index][jaeger-e3], [Current architecture and OpenTelemetry relationship][jaeger-e4], [Deployment roles and backend documentation][jaeger-e5], [In-memory storage limits documentation][jaeger-e6] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[jaeger-e1]: https://github.com/jaegertracing/jaeger
[jaeger-e2]: https://github.com/jaegertracing/jaeger/blob/main/LICENSE
[jaeger-e3]: https://www.jaegertracing.io/docs/
[jaeger-e4]: https://www.jaegertracing.io/docs/2.21/architecture/
[jaeger-e5]: https://www.jaegertracing.io/docs/2.21/deployment/
[jaeger-e6]: https://www.jaegertracing.io/docs/2.21/storage/memory/
[jaeger-e7]: https://github.com/jaegertracing/jaeger/blob/main/GOVERNANCE.md
[jaeger-e8]: https://www.cncf.io/projects/jaeger/
[jaeger-e9]: https://github.com/jaegertracing/jaeger/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/jaegertracing/jaeger) (`archived: false`).

### thanos

**Identity boundary:** Thanos is a composable metrics component stack extending Prometheus, with global queries, HA deduplication and object storage. Keep it distinct from Prometheus, Mimir and managed services; remove unsupported product-superiority comparisons.

**Licence boundary:** Apache-2.0 is verified from the actual Thanos LICENSE; CNCF incubation is governance evidence, not a licence.

**Commercial/service boundary:** Leave optional commercial_offering absent. Self-hosted components require operators and external storage; third-party managed products are not the upstream Thanos implementation.

**Repository boundary:** Retain thanos-io/thanos and thanos.io. Add the upstream-linked getting-started documentation. The tip path follows development docs; operators should select documentation appropriate to the deployed release.

**Governance:** Upstream MAINTAINERS.md names maintainers across multiple organizations. CNCF directly records incubation since 2020-08-19, not graduation.

**Maturity:** Established is a reviewer judgement from years of maintained releases, documented sidecar/receive/query/storage architecture and active multi-organization maintainers; it is independent of the CNCF Incubating label.

**Lifecycle:** Non-archived upstream with 2026-10-07 activity and stable v0.42.4 (2026-07-30). Its README documents regular release practice and maintained deployment architecture.

**Unresolved questions / limits:** None blocking component scope. Storage capacity, retention and access controls remain operator concerns; no claim of inherently unlimited physical storage or superiority over Mimir is made.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical component repository and scope][thanos-e1], [Software licence][thanos-e2], [Official getting-started documentation][thanos-e3], [Project maintainers and governance boundary][thanos-e4], [CNCF foundation status][thanos-e5], [Maintained release history][thanos-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | thanos | thanos | [Canonical component repository and scope][thanos-e1] | Preserve stable catalogue ID and history; no duplicate record. |
| `name` | Thanos | Thanos | [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3] | Reviewed; retained: documented capability/identity; the scoped boundary above applies. |
| `summary` | Highly available Prometheus setup with long-term storage. | Open-source components extending Prometheus with high availability, deduplicated global queries and long-term metrics storage in object stores; it is distinct from Prometheus and Grafana Mimir. | [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | https://thanos.io | https://thanos.io | [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3] | Reviewed; retained: official entry point identified by the upstream project; any boundary correction is explained above. |
| `repository_url` | https://github.com/thanos-io/thanos | https://github.com/thanos-io/thanos | [Canonical component repository and scope][thanos-e1] | Retain the verified scoped implementation repository. |
| `documentation_url` | *absent* | https://thanos.io/tip/thanos/getting-started.md/ | [Official getting-started documentation][thanos-e3] | Add the directly verified official documentation entry point. |
| `categories` | monitoring-metrics-logs-tracing | monitoring-metrics-logs-tracing | [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `subcategories` | Visualization, Metrics, and Tracing | Long-term metrics storage | [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3] | Changed: reviewer mapping of documented capability to the existing taxonomy. |
| `roles` | devops-engineer<br>site-reliability-engineer<br>observability-engineer | devops-engineer<br>site-reliability-engineer<br>observability-engineer | [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `lifecycle_stages` | operate<br>monitor | operate<br>monitor | [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `use_when` | Extending Prometheus with global querying and cheap object-store retention. | You need a global query view across Prometheus instances, deduplication of HA pairs and long-term object storage through the appropriate Thanos components. | [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3], [Software licence][thanos-e2] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `avoid_when` | Mimir&#x27;s multi-tenancy or Cortex is a better fit, or you only have one small Prometheus instance. | You need only a standalone Prometheus server or expect the component stack to include managed operations, object-store capacity or every tenant access policy automatically. | [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3], [Software licence][thanos-e2] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `deployment_models` | `[]` | self-hosted | [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3] | Record software self-hosting; only Grafana parent includes hosted-saas for its explicitly named Cloud edition. |
| `license_model` | oss | oss | [Software licence][thanos-e2] | Reviewed; retained: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Software licence][thanos-e2] | Changed: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Canonical component repository and scope][thanos-e1] | Leave optional field absent; no blanket claim about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Maintained release history][thanos-e6], [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3], [Project maintainers and governance boundary][thanos-e4], [CNCF foundation status][thanos-e5] | Editorial established judgement from maintained releases/specifications, documented operations and governance; component stability is explicitly bounded. |
| `status` | needs-review | active | [Maintained release history][thanos-e6], [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical component repository and scope][thanos-e1], [Maintained release history][thanos-e6] | GitHub API reports archived=false; actual release/activity evidence supports lifecycle separately. |
| `alternatives` | `[]` | `[]` | [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `tags` | `[]` | `[]` | [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical component repository and scope][thanos-e1], [Software licence][thanos-e2], [Official getting-started documentation][thanos-e3], [Project maintainers and governance boundary][thanos-e4], [CNCF foundation status][thanos-e5], [Maintained release history][thanos-e6] | Actual review date, changed only for these ten records. |
| `sources` | legacy:5_Monitoring-Observability/README.md#L49<br>legacy:devopstools_final.md#L755 | legacy:5_Monitoring-Observability/README.md#L49<br>legacy:devopstools_final.md#L755<br>https://github.com/thanos-io/thanos<br>https://github.com/thanos-io/thanos/blob/main/LICENSE<br>https://thanos.io/tip/thanos/getting-started.md/<br>https://github.com/thanos-io/thanos/blob/main/MAINTAINERS.md<br>https://www.cncf.io/projects/thanos/<br>https://github.com/thanos-io/thanos/releases | [Canonical component repository and scope][thanos-e1], [Software licence][thanos-e2], [Official getting-started documentation][thanos-e3], [Project maintainers and governance boundary][thanos-e4], [CNCF foundation status][thanos-e5], [Maintained release history][thanos-e6] | Preserve every legacy source and append checked primary sources, including the former OpenTelemetry organization pointer. |
| `needs_review` | `true` | `false` | [Maintained release history][thanos-e6], [Canonical component repository and scope][thanos-e1], [Official getting-started documentation][thanos-e3] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[thanos-e1]: https://github.com/thanos-io/thanos
[thanos-e2]: https://github.com/thanos-io/thanos/blob/main/LICENSE
[thanos-e3]: https://thanos.io/tip/thanos/getting-started.md/
[thanos-e4]: https://github.com/thanos-io/thanos/blob/main/MAINTAINERS.md
[thanos-e5]: https://www.cncf.io/projects/thanos/
[thanos-e6]: https://github.com/thanos-io/thanos/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/thanos-io/thanos) (`archived: false`).

### kube-state-metrics

**Identity boundary:** Use upstream spelling kube-state-metrics while preserving the stable ID. It exposes Kubernetes API object-state metrics, not runtime resource-usage metrics and not a metrics storage/query service. Retain monitoring as primary category and add the Kubernetes engineer role.

**Licence boundary:** Apache-2.0 is verified from its own canonical LICENSE. Kubernetes ownership and SIG sponsorship do not substitute for licence evidence.

**Commercial/service boundary:** No vendor-hosted product is implied; optional commercial_offering remains absent. Self-hosted is the documented service deployment in a Kubernetes environment.

**Repository boundary:** Retain kubernetes/kube-state-metrics. Add the official Kubernetes concept page as official_url and upstream docs as documentation_url, both identified directly by the upstream project.

**Governance:** Kubernetes SIG Instrumentation README explicitly lists kube-state-metrics as an owned subproject, and its OWNERS file identifies reviewers/approvers. It is not asserted to have its own CNCF graduated status.

**Maturity:** Established follows maintained releases, explicit Kubernetes compatibility/support guidance, documented state metrics and deployment/scaling operations under SIG ownership.

**Lifecycle:** Non-archived upstream with 2026-10-07 activity and stable v2.20.0 (2026-08-18). README documents Kubernetes/client-go compatibility and support for the latest release; alpha API metrics carry separate stability limits. Custom-resource-state is feature-frozen toward resource-state-metrics, not retirement of kube-state-metrics.

**Unresolved questions / limits:** None blocking object-state identity. API/resource versions and alpha metrics have their own stability constraints; the custom-resource-state feature transition does not deprecate the whole service.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Software licence][kube-state-metrics-e2], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [SIG Instrumentation ownership and governance][kube-state-metrics-e6], [Repository reviewer and approver ownership][kube-state-metrics-e7], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8], [Maintained release history][kube-state-metrics-e9].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | kube-state-metrics | kube-state-metrics | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official upstream metrics documentation][kube-state-metrics-e4], [Repository reviewer and approver ownership][kube-state-metrics-e7] | Preserve stable catalogue ID and history; no duplicate record. |
| `name` | Kube State Metrics | kube-state-metrics | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8] | Changed: documented capability/identity; the scoped boundary above applies. |
| `summary` | Exposes Kubernetes cluster state as metrics. | Kubernetes SIG Instrumentation service exposing Prometheus-format metrics derived from Kubernetes API object state; resource-usage collection by metrics-server or cAdvisor and storage/query by Prometheus are separate. | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8] | Changed: documented capability/identity; the scoped boundary above applies. |
| `official_url` | *absent* | https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/ | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official upstream metrics documentation][kube-state-metrics-e4], [Repository reviewer and approver ownership][kube-state-metrics-e7], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8] | Changed: official entry point identified by the upstream project; any boundary correction is explained above. |
| `repository_url` | https://github.com/kubernetes/kube-state-metrics | https://github.com/kubernetes/kube-state-metrics | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official upstream metrics documentation][kube-state-metrics-e4], [Repository reviewer and approver ownership][kube-state-metrics-e7] | Retain the verified scoped implementation repository. |
| `documentation_url` | *absent* | https://github.com/kubernetes/kube-state-metrics/tree/main/docs | [Official upstream metrics documentation][kube-state-metrics-e4] | Add the directly verified official documentation entry point. |
| `categories` | monitoring-metrics-logs-tracing | monitoring-metrics-logs-tracing | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `subcategories` | Kubernetes Observability &amp; Troubleshooting | Kubernetes Observability &amp; Troubleshooting | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `roles` | devops-engineer<br>site-reliability-engineer<br>observability-engineer | devops-engineer<br>site-reliability-engineer<br>observability-engineer<br>kubernetes-engineer | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8] | Changed: reviewer mapping of documented capability to the existing taxonomy. |
| `lifecycle_stages` | operate<br>monitor | operate<br>monitor | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8] | Reviewed; retained: reviewer mapping of documented capability to the existing taxonomy. |
| `use_when` | You need K8s object-level metrics (deployments, pods, nodes) in Prometheus. | You need scrapeable metrics for Kubernetes API object state, such as deployment replicas, pod phases and node conditions, for a separate monitoring system. | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8], [Software licence][kube-state-metrics-e2] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `avoid_when` | You only care about node/container resource metrics (use cAdvisor/metrics-server instead). | You need CPU/memory resource-usage metrics from metrics-server or cAdvisor, or expect kube-state-metrics to store, query or alert on the collected time series like Prometheus. | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8], [Software licence][kube-state-metrics-e2] | Changed: documented functionality, deployment and scoped licensing support this selection guidance. |
| `deployment_models` | `[]` | self-hosted | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8] | Record software self-hosting; only Grafana parent includes hosted-saas for its explicitly named Cloud edition. |
| `license_model` | oss | oss | [Software licence][kube-state-metrics-e2] | Reviewed; retained: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `license_spdx` | *absent* | Apache-2.0 | [Software licence][kube-state-metrics-e2] | Changed: actual software grant/project policy and scoped component exceptions; no foundation or service licence inheritance. |
| `commercial_offering` | *absent* | *absent* | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official upstream metrics documentation][kube-state-metrics-e4], [Repository reviewer and approver ownership][kube-state-metrics-e7] | Leave optional field absent; no blanket claim about all third-party support/distribution businesses. |
| `maturity` | unknown | established | [Maintained release history][kube-state-metrics-e9], [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8], [SIG Instrumentation ownership and governance][kube-state-metrics-e6] | Editorial established judgement from maintained releases/specifications, documented operations and governance; component stability is explicitly bounded. |
| `status` | needs-review | active | [Maintained release history][kube-state-metrics-e9], [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |
| `repository_archived` | *absent* | `false` | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official upstream metrics documentation][kube-state-metrics-e4], [Repository reviewer and approver ownership][kube-state-metrics-e7], [Maintained release history][kube-state-metrics-e9] | GitHub API reports archived=false; actual release/activity evidence supports lifecycle separately. |
| `alternatives` | `[]` | `[]` | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `tags` | `[]` | `[]` | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8] | Retain empty optional metadata without unsupported alternatives or extra tags. |
| `verified_on` | 2026-08-03 | 2026-10-07 | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Software licence][kube-state-metrics-e2], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [SIG Instrumentation ownership and governance][kube-state-metrics-e6], [Repository reviewer and approver ownership][kube-state-metrics-e7], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8], [Maintained release history][kube-state-metrics-e9] | Actual review date, changed only for these ten records. |
| `sources` | legacy:5_Monitoring-Observability/README.md#L30<br>legacy:devopstools_final.md#L730 | legacy:5_Monitoring-Observability/README.md#L30<br>legacy:devopstools_final.md#L730<br>https://github.com/kubernetes/kube-state-metrics<br>https://github.com/kubernetes/kube-state-metrics/blob/main/LICENSE<br>https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/<br>https://github.com/kubernetes/kube-state-metrics/tree/main/docs<br>https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/<br>https://github.com/kubernetes/community/blob/main/sig-instrumentation/README.md<br>https://github.com/kubernetes/kube-state-metrics/blob/main/OWNERS<br>https://github.com/kubernetes/kube-state-metrics/blob/main/README.md<br>https://github.com/kubernetes/kube-state-metrics/releases | [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Software licence][kube-state-metrics-e2], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [SIG Instrumentation ownership and governance][kube-state-metrics-e6], [Repository reviewer and approver ownership][kube-state-metrics-e7], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8], [Maintained release history][kube-state-metrics-e9] | Preserve every legacy source and append checked primary sources, including the former OpenTelemetry organization pointer. |
| `needs_review` | `true` | `false` | [Maintained release history][kube-state-metrics-e9], [Canonical object-state implementation repository and scope][kube-state-metrics-e1], [Official Kubernetes identity and object-state documentation][kube-state-metrics-e3], [Official upstream metrics documentation][kube-state-metrics-e4], [Kubernetes resource-usage pipeline documentation][kube-state-metrics-e5], [Scope, resource-usage comparison and support documentation][kube-state-metrics-e8] | CLEAR REVIEW: active project evidence and resolved material boundaries; status/flag remain consistent. |

**Changed fields:** `name`, `summary`, `official_url`, `documentation_url`, `roles`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[kube-state-metrics-e1]: https://github.com/kubernetes/kube-state-metrics
[kube-state-metrics-e2]: https://github.com/kubernetes/kube-state-metrics/blob/main/LICENSE
[kube-state-metrics-e3]: https://kubernetes.io/docs/concepts/cluster-administration/kube-state-metrics/
[kube-state-metrics-e4]: https://github.com/kubernetes/kube-state-metrics/tree/main/docs
[kube-state-metrics-e5]: https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/
[kube-state-metrics-e6]: https://github.com/kubernetes/community/blob/main/sig-instrumentation/README.md
[kube-state-metrics-e7]: https://github.com/kubernetes/kube-state-metrics/blob/main/OWNERS
[kube-state-metrics-e8]: https://github.com/kubernetes/kube-state-metrics/blob/main/README.md
[kube-state-metrics-e9]: https://github.com/kubernetes/kube-state-metrics/releases

Archival metadata checked: [GitHub repository API](https://api.github.com/repos/kubernetes/kube-state-metrics) (`archived: false`).

## Review-debt accounting

Selected **10**, cleared **10**, retained **0**. Before/after `python -m scripts.review_debt --format markdown --limit 30` output is captured.

| Counter | Before | After |
|---|---:|---:|
| canonical_records | 1,425 | 1,425 |
| needs_review | 756 | 746 |
| status_needs_review | 756 | 746 |
| mismatches | 0 | 0 |
| unknown_license | 80 | 80 |
| unknown_maturity | 893 | 883 |
| missing_repository | 391 | 391 |
| missing_documentation | 890 | 880 |
| missing_sources | 0 | 0 |

The status/flag invariant holds for every record. Documentation debt decreases by ten and unknown maturity by ten. Repository debt remains unchanged: deliberate umbrella absence is not filled to improve the counter. No unknown licence model is forced into a new classification.

## Generated changes

Only generator output is listed here; the evidence report and focused tests are authored files.

- `README.md`
- `docs/catalog-statistics.json`
- `docs/categories/monitoring-metrics-logs-tracing.md`
- `docs/lifecycle/develop.md`
- `docs/lifecycle/monitor.md`
- `docs/lifecycle/operate.md`
- `docs/roles/devops-engineer.md`
- `docs/roles/kubernetes-engineer.md`
- `docs/roles/observability-engineer.md`
- `docs/roles/site-reliability-engineer.md`

## Validation and full link audit

Required checks passed. Python 3.12.3 in the existing WSL Ubuntu constrained environment ran installation, fresh dependency resolution and the complete suite. The Windows editable environment ran focused tests, lint/format, generation, catalogue validation and debt capture. `python` below denotes the selected interpreter.

| Command | Result |
|---|---|
| `python -m pip install -e '.[dev]' -c config/python-constraints-3.12.txt` | PASS; constrained editable install |
| `python -m scripts.python_constraints --check` | PASS; fresh resolver matches unchanged reviewed constraints |
| `python -m ruff check scripts tests` | PASS |
| `python -m ruff format --check scripts tests` | PASS; 61 files already formatted |
| `python -m pytest tests/test_wave8_evidence_review.py` | PASS; 25 tests |
| `python -m pytest` | PASS; 748 tests in 254.68 seconds |
| `python -m scripts.generate_docs` | PASS; regenerated after canonical changes |
| `python -m scripts.generate_docs --check` | PASS |
| `python -m scripts.validate_catalog` | PASS |
| `python -m scripts.review_debt --format markdown --limit 30` | PASS; before/after counters captured |
| `git diff --check` | PASS |

Pytest cache permission warnings, where emitted, were non-failing. WSL Git-dependent tests used process-only `GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=true` to interpret the Windows checkout line endings consistently. No repository/global Git setting, constraint, test assertion or workflow was weakened.

The 25 focused cases guard the Grafana mixed OSS/Enterprise/Cloud parent licence; Loki/Tempo/Mimir software versus services; project-specific Apache/AGPL grants; the OpenTelemetry umbrella versus Collector and core versus contrib distributions; Prometheus versus Alertmanager/exporters; Loki label indexing, content queries and tenant authentication boundaries; Tempo TraceQL and configured receiver interoperability; Jaeger current tracing architecture; Thanos global HA metrics scope; kube-state-metrics SIG ownership and object-state versus resource metrics; and governance versus licence evidence. No prices or transient release versions are asserted.

Exactly one fresh full strict audit used no cache reuse and ignored output paths:

```bash
python -m scripts.check_links --strict --check-archived --workers 8 --cache tmp/wave8/link-cache.json --cache-hours 0 --json-report tmp/wave8/link-report.json --markdown-report tmp/wave8/link-report.md
```

| Audit counter | Result |
|---|---:|
| URLs | 2,655 |
| blocking_new | 0 |
| blocking_known observed | 4 |
| strict_result | PASS |

**Reviewed baseline changed: NO.** All six existing exceptions remain untouched. Observed rate limits, restrictions or inconclusive responses do not independently prove a historical defect fixed.

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
| `prometheus` | HTTP 200 | valid |
| `grafana` | HTTP 200 | valid |
| `grafana-loki` | HTTP 200 | valid |
| `grafana-tempo` | HTTP 200 | valid |
| `grafana-mimir` | HTTP 200 | valid |
| `opentelemetry` | HTTP 200 | valid |
| `opentelemetry-collector` | HTTP 200 | valid |
| `jaeger` | HTTP 200 | valid |
| `thanos` | HTTP 200 | valid |
| `kube-state-metrics` | HTTP 429 | rate-limited |

All audit classifications, including network-dependent limitations:

| Classification | Count |
|---|---:|
| dns-inconclusive | 6 |
| http-error | 1 |
| manual-verification-required | 3 |
| network-inconclusive | 1 |
| permanent-redirect | 205 |
| rate-limited | 760 |
| restricted-or-bot-blocked | 358 |
| timeout-inconclusive | 1 |
| transient-failure | 1 |
| valid | 1,283 |
| valid-redirect | 36 |

Strict PASS means no newly classified blockers, not successful verification of every endpoint. Actual licence files, official terms/docs, upstream metadata and release/support evidence independently support the review decisions. Source-only URLs were read separately; the checker inventories official/repository/documentation fields. No network-dependent required audit was omitted. Access/rate-limit/transport observations remain inconclusive where listed above.

Raw cache/audit output stays in ignored `tmp/wave8/`. Nothing under `reports/` is committed. No additional full audit was run.

## Scope verification and review state

The pre-edit snapshot and baseline Git tree establish exactly ten changed IDs, dates and record blocks and 240 complete material-field rows. All legacy provenance is preserved. Every other record block remains unchanged. Final canonical URL contexts match the audit. The six-entry baseline, committed audit output/ledger, workflows, CodeQL configuration and Python constraints remain unchanged.

Issue #2 is read-only: its body and updated_at (2026-10-07T20:03:16Z) are compared with the pre-edit snapshot again at handoff. No Wave 4–7 record is revisited; Wave 9 is not started. No merge or release is performed.

Resolved material findings: Prometheus server versus separate Alertmanager/exporters; Grafana mixed OSS/Enterprise/Cloud/plugin family without an inherited single SPDX; Loki label index versus content queries and tenant authentication; Tempo TraceQL/configured receiver support and architecture beyond an ID-only lookup claim; Mimir current Prometheus-compatible identity versus historical Cortex and hosted Cloud Metrics; OpenTelemetry umbrella without an invented implementation repository and with explicit project-wide Apache policy; Collector core framework versus contrib/distributions and per-component stability; Jaeger current 2.x tracing backend using Collector components without being deprecated or collapsed into OpenTelemetry; Thanos HA/global query/long-term metrics versus Prometheus/Mimir; kube-state-metrics SIG Instrumentation ownership and object-state metrics versus metrics-server/cAdvisor resource usage.

No material identity/licence boundary remains unresolved. Deliberate optional-field absences and component/service limitations are documented per record. Catalogue maturity is an editorial established judgement from current maintenance, operational documentation and governance, not a promise of universal component stability or a deduction from stars/foundation status. Grafana Enterprise Logs/Metrics/Traces support notices are bounded to those commercial products, not applied to OSS lifecycle.

CI/security and subsequent automatic PR findings are reported against the final commit in the PR and final handoff.
