# Wave 18 — Observability, telemetry and SRE evidence review

**Review date:** 2026-10-21. **Baseline main:** `bf2ebbb154ca0b389d28f4658617ff2d88942701`. **Issue:** [#125](https://github.com/goozcena-gnl/devops-tools-catalog/issues/125). **Implementation branch:** `maintenance/wave-18-observability-sre-evidence-review`.

**Provisional result:** 10 existing records reviewed; **9 CLEAR, 1 RETAIN** (Tracetest); catalogue 1,425 unchanged; review debt 665 → 656 subject to generated docs and CI. No other canonical record changed. The original legacy source references remain intact.

## Per-record decisions

| ID | Decision | Key evidence boundary |
|---|---|---|
| `beszel` | **CLEAR (provisional)** | MIT hub/agent metrics platform; not full distributed tracing |
| `dozzle` | **CLEAR (provisional)** | MIT live container log viewer with no historical storage |
| `gatus` | **CLEAR (provisional)** | Apache-2.0 health/status checks; not APM |
| `holmesgpt` | **CLEAR (provisional)** | Apache-2.0 SRE investigation; govern LLM cost, data permissions and autonomous actions |
| `hyperdx` | **CLEAR (provisional)** | MIT ClickStack/ClickHouse integration; CLI release must not be mistaken for platform release |
| `opensearch` | **CLEAR (provisional)** | Apache-2.0 core search engine, distinct from dashboards and ingestion; NOTICE/third-party scope |
| `quickwit` | **CLEAR (provisional)** | Apache-2.0 object-store logs/traces search; third-party grants remain independent |
| `signoz` | **CLEAR (provisional)** | MIT Community source with separately restricted ee/ and cmd/enterprise/ components; open-core model maintained |
| `tracetest` | **RETAIN REVIEW** | Mixed Tracetest Community and MIT file-level grants; latest stable 2024-10-10, support unclear |
| `zipkin` | **CLEAR (provisional)** | Apache-2.0 tracing backend, published releases and active repository |

## Complete changed-field before/after ledger

YAML folded list values are represented completely, with list items separated by `; `. `∅` denotes absent properties. All direct LICENSE URLs are preserved under canonical `sources` and therefore may not be covered by the standard link-audit field selection.

### `beszel`

| Field | Before | After |
|---|---|---|
| `summary` | `Lightweight self-hosted server and container monitoring with alerts, OAuth/OIDC, backups, and REST API.` | `Lightweight self-hosted hub-and-agent monitoring for hosts and Docker/Podman containers, with metric history and alerting.` |
| `use_when` | `[]` | `You need lightweight host and container metrics, alerts and simple multi-system dashboards without a full observability pipeline.` |
| `avoid_when` | `[]` | `You require full distributed tracing or centralized long-term log analytics; verify agent permissions and hub authentication.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:devopstools_final.md#L697` | `legacy:devopstools_final.md#L697; https://github.com/henrygd/beszel; https://github.com/henrygd/beszel/blob/main/LICENSE; https://github.com/henrygd/beszel/releases; https://beszel.dev/guide/getting-started` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://beszel.dev/guide/getting-started` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `MIT` |

### `dozzle`

| Field | Before | After |
|---|---|---|
| `summary` | `Self-hosted real-time Docker and container log viewer with alerting, remote hosts, and Kubernetes support.` | `Real-time container log viewer for Docker, Swarm and supported Kubernetes deployments; it does not persist logs.` |
| `use_when` | `[]` | `You need immediate live container log inspection on trusted Docker hosts or Kubernetes environments.` |
| `avoid_when` | `[]` | `You need log retention, offline historical search or can not safely expose the Docker socket or sensitive log contents.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:devopstools_final.md#L760` | `legacy:devopstools_final.md#L760; https://github.com/amir20/dozzle; https://github.com/amir20/dozzle/blob/main/LICENSE; https://github.com/amir20/dozzle/releases; https://dozzle.dev/guide/getting-started` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://dozzle.dev/guide/getting-started` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `MIT` |

### `gatus`

| Field | Before | After |
|---|---|---|
| `summary` | `Developer-oriented health dashboard and status page for monitoring endpoints and services.` | `Self-hosted endpoint health dashboard with HTTP, TCP, ICMP and DNS checks, status pages and alert integrations.` |
| `use_when` | `[]` | `You want declarative synthetic health checks and alert routing for endpoints and basic service status.` |
| `avoid_when` | `[]` | `You require full infrastructure metrics, distributed traces or application profiling; protect probe credentials.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:devopstools_final.md#L704` | `legacy:devopstools_final.md#L704; https://github.com/TwiN/gatus; https://github.com/TwiN/gatus/blob/master/LICENSE; https://github.com/TwiN/gatus/releases; https://github.com/TwiN/gatus/blob/master/README.md` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://github.com/TwiN/gatus/blob/master/README.md` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

### `holmesgpt`

| Field | Before | After |
|---|---|---|
| `summary` | `Open-source SRE AI agent for investigating production incidents across Kubernetes, VMs, cloud services, and databases with operator mode for 24/7 background monitoring (CNCF).` | `Open-source AI SRE investigation agent integrating Kubernetes, cloud and observability data sources; operator mode needs explicit permissions.` |
| `use_when` | `[]` | `You need assisted incident investigation across connected telemetry and Kubernetes resources with reviewed LLM access.` |
| `avoid_when` | `[]` | `You cannot govern model data sharing, API-token costs, tool permissions or autonomous incident responses.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:devopstools_final.md#L726` | `legacy:devopstools_final.md#L726; https://github.com/HolmesGPT/holmesgpt; https://github.com/HolmesGPT/holmesgpt/blob/master/LICENSE; https://github.com/HolmesGPT/holmesgpt/releases; https://holmesgpt.dev/` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://holmesgpt.dev/` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

### `hyperdx`

| Field | Before | After |
|---|---|---|
| `summary` | `Observability and troubleshooting platform.` | `ClickHouse-backed observability interface for correlating logs, traces, metrics and session replay within ClickStack deployments.` |
| `use_when` | `You want a self-hosted Datadog-like experience with session replay.` | `You want correlated telemetry exploration on ClickHouse with OpenTelemetry collection and session replay.` |
| `avoid_when` | `You need proven large-scale production deployments.` | `You expect the most recent CLI tag to validate server support or cannot maintain the required ClickHouse and collector stack.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:5_Monitoring-Observability/README.md#L43; legacy:devopstools_final.md#L748` | `legacy:5_Monitoring-Observability/README.md#L43; legacy:devopstools_final.md#L748; https://github.com/hyperdxio/hyperdx; https://github.com/hyperdxio/hyperdx/blob/main/LICENSE; https://github.com/hyperdxio/hyperdx/releases; https://clickhouse.com/docs/use-cases/observability/clickstack/overview` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://clickhouse.com/docs/use-cases/observability/clickstack/overview` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `MIT` |

### `opensearch`

| Field | Before | After |
|---|---|---|
| `summary` | `Search/analytics engine commonly used for logs (Elastic-alternative fork).` | `Apache-licensed distributed search and analytics engine used for log indexing and observability, distinct from Dashboards and ingestion components.` |
| `use_when` | `You need ELK-like capabilities under a true open-source license.` | `You need a distributed search and analytics backend for logs with controllable deployment and storage.` |
| `avoid_when` | `You're happy with Elastic's licensing, as plugin/feature parity may lag.` | `You assume full Elasticsearch or plugin feature compatibility or cannot manage storage, cluster security and upgrades.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:5_Monitoring-Observability/README.md#L60; legacy:devopstools_final.md#L768` | `legacy:5_Monitoring-Observability/README.md#L60; legacy:devopstools_final.md#L768; https://github.com/opensearch-project/OpenSearch; https://github.com/opensearch-project/OpenSearch/blob/main/LICENSE.txt; https://github.com/opensearch-project/OpenSearch/releases; https://docs.opensearch.org/latest/` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://docs.opensearch.org/latest/` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

### `quickwit`

| Field | Before | After |
|---|---|---|
| `summary` | `Distributed log search/indexing built around fast ingestion and cost control.` | `Cloud-native distributed log and trace search engine using object storage and decoupled indexing and search.` |
| `use_when` | `Cost-efficient log search on object storage with sub-second latency.` | `You need logs or traces search on object storage and can operate its ingestion and query components.` |
| `avoid_when` | `You need the broad ecosystem and maturity of Elasticsearch/OpenSearch.` | `You need a turnkey metrics platform, universal Elasticsearch compatibility or unverified latency/availability guarantees.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:5_Monitoring-Observability/README.md#L61; legacy:devopstools_final.md#L769` | `legacy:5_Monitoring-Observability/README.md#L61; legacy:devopstools_final.md#L769; https://github.com/quickwit-oss/quickwit; https://github.com/quickwit-oss/quickwit/blob/main/LICENSE; https://github.com/quickwit-oss/quickwit/releases; https://quickwit.io/docs/main-branch; https://github.com/quickwit-oss/quickwit/blob/main/LICENSE-3rdparty.csv` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://quickwit.io/docs/main-branch` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

### `signoz`

| Field | Before | After |
|---|---|---|
| `summary` | `Open-source observability platform.` | `OpenTelemetry-native observability platform for logs, metrics and traces, with MIT community code and separately restricted Enterprise components.` |
| `use_when` | `Self-hosted Datadog alternative with OTel-native traces, metrics, and logs.` | `You need self-hosted correlated metrics, logs, tracing and dashboards and can manage ClickHouse-based infrastructure.` |
| `avoid_when` | `You lack capacity to run ClickHouse-based infra.` | `You assume Enterprise features are MIT licensed or need a small-footprint stack without ClickHouse operations.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:5_Monitoring-Observability/README.md#L47; legacy:devopstools_final.md#L753` | `legacy:5_Monitoring-Observability/README.md#L47; legacy:devopstools_final.md#L753; https://github.com/SigNoz/signoz; https://github.com/SigNoz/signoz/blob/main/LICENSE; https://github.com/SigNoz/signoz/releases; https://signoz.io/docs/install/self-host/; https://github.com/SigNoz/signoz/blob/main/ee/LICENSE` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://signoz.io/docs/install/self-host/` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `MIT` |
| `commercial_offering` | ∅ | `true` |

### `tracetest`

| Field | Before | After |
|---|---|---|
| `summary` | `Trace-based testing for distributed systems.` | `Trace-based integration testing using OpenTelemetry, with mixed MIT/Tracetest Community licensing and unclear current support.` |
| `use_when` | `Writing integration tests that assert on distributed trace structure.` | `You are evaluating assertions against distributed traces for integration and end-to-end tests.` |
| `avoid_when` | `Traditional API/contract testing already gives sufficient coverage.` | `You require a clearly maintained and uniformly permissive production tool; source files have different license grants.` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:5_Monitoring-Observability/README.md#L74; legacy:devopstools_final.md#L783` | `legacy:5_Monitoring-Observability/README.md#L74; legacy:devopstools_final.md#L783; https://github.com/kubeshop/tracetest; https://github.com/kubeshop/tracetest/blob/main/LICENSE; https://github.com/kubeshop/tracetest/releases; https://docs.tracetest.io/` |
| `documentation_url` | ∅ | `https://docs.tracetest.io/` |
| `repository_archived` | ∅ | `false` |

### `zipkin`

| Field | Before | After |
|---|---|---|
| `summary` | `Distributed tracing system.` | `Open-source distributed tracing collector and UI for investigating service latency and dependencies using pluggable storage.` |
| `use_when` | `Simple, lightweight distributed tracing for Java-centric stacks.` | `You need a distributed trace collector and query UI with supported Zipkin ingestion and storage.` |
| `avoid_when` | `Jaeger or OTel Collector already serves as your tracing backend.` | `You expect automatic application instrumentation or guaranteed parity with Jaeger and OpenTelemetry-native backends.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:5_Monitoring-Observability/README.md#L51; legacy:devopstools_final.md#L757` | `legacy:5_Monitoring-Observability/README.md#L51; legacy:devopstools_final.md#L757; https://github.com/openzipkin/zipkin; https://github.com/openzipkin/zipkin/blob/master/LICENSE; https://github.com/openzipkin/zipkin/releases; https://zipkin.io/pages/quickstart` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://zipkin.io/pages/quickstart` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

## Wave 18 strict link audit #23 — corrective evidence (2026-10-21)

- [Attempt #23](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/39656251469) checked 2,756 URLs on the earlier Wave 18 HEAD `9233cc509f453694f0fc05d160dc985dad41c465`: `strict_result: FAIL`, `blocking_new: 1`, `blocking_known: 6`, and no baseline changes/resolutions. [Artifact](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/39656251469/artifacts/12371982970).
- The sole new failure was `https://quickwit.io/docs/` (HEAD 404 and fallback GET 404 at 2026-10-21T18:55:36Z).
- Replaced that obsolete docs root with the official Quickwit documentation home [`https://quickwit.io/docs/main-branch`](https://quickwit.io/docs/main-branch), confirmed to serve the documentation page. The correction is limited to Quickwit's canonical `documentation_url`, its evidence `sources` entry, the generated category documentation link, and this report ledger; no review/lifecycle/licence decision changed.
- Run a **new strict full link audit on the corrected branch HEAD** before Ready for review. The preceding failed report remains preserved as historical evidence.

## Remaining uncertainty

- Tracetest retains `needs_review: true`, `status: needs-review`, and `maturity: unknown`. Its root LICENSE combines MIT and a community licence; upstream support and component-level grants still require review. No single SPDX grant is asserted for the whole repository.
- SigNoz core MIT and Enterprise restricted source boundaries must not be conflated; Enterprise source is not uniformly MIT.
- HyperDX latest public GitHub release includes a CLI tag, which does not by itself verify the self-hosted server version.

## Required validation

- Regenerate all derived views with `python -m scripts.generate_docs` and confirm `--check`.
- Execute locked Python 3.12 checks, Ruff, complete pytest, catalogue validation, debt inventory, `git diff --check`. Treat historical test drift as scoped and explicitly authorized only with independent proof.
- Execute a new strict URL audit on the final PR HEAD; require `strict_result: PASS`, `blocking_new: 0`, and reconcile the six historical blockers in tracker #2; never weaken TLS or baseline.
- Review Codex/human findings, keep the PR Draft until green CI, and do not merge without human authorization.
