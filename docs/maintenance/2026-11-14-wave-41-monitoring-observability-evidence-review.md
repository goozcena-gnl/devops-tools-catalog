# Wave 41 — monitoring/observability evidence review

- Evidence date: **2026-11-14**; frozen selection: [issue #177](https://github.com/goozcena-gnl/devops-tools-catalog/issues/177).
- `main`: `62e33cfc0d4b682a65799e0b73d1c2c8bc71c154`; baseline canonical Git blob: `272b0e322c08e8bd94557d811a41aab39686b075`.
- **99** canonical raw blocks, **23** `needs_review: true`; exactly **8 corrected**, **2 RETAIN** (`kwatcher`, `grove`), **89 nonselected raw blocks protected**. The entire set of **91 protected blocks** is byte-for-byte unchanged.
- All `id`, `name`, `official_url`, `repository_url`, `categories`, `roles`, `lifecycle_stages`, `license_model`, `status`, `needs_review`, `maturity`, `verified_on`, historical legacy provenance and prior sources are preserved.
- Three new source-scoped SPDX values: `kube-binpacking-exporter` MIT, `cardamon` Apache-2.0, and `otel-gui` MIT, confirmed by upstream root LICENSE files. No invented aggregate licences for documentation, Munin plugins, Nagios products or mixed-license syslog-ng.

## Evidence-by-ID

| ID | Decision | Upstream proof |
|---|---|---|
| `awesome-prometheus` | Curated documentation and external references, not a software distribution; CC0 does not cover linked projects | [README](https://github.com/roaldnefs/awesome-prometheus/blob/main/README.md), [LICENSE](https://github.com/roaldnefs/awesome-prometheus/blob/main/LICENSE) |
| `grafana-alloy-deploy` | Alloy deployment documentation, not separate software; Alloy repository has file-level licensing exceptions | [README](https://github.com/grafana/alloy/blob/main/README.md), [LICENSING](https://github.com/grafana/alloy/blob/main/LICENSING.md) |
| `kube-binpacking-exporter` | Pod resource requests vs allocatable, not actual usage; source MIT | [README](https://github.com/procore-oss/kube-binpacking-exporter/blob/main/README.md), [LICENSE](https://github.com/procore-oss/kube-binpacking-exporter/blob/main/LICENSE) |
| `cardamon` | Cross-check Prometheus stored series against queries, rules and dashboards; source Apache-2.0; no blind drop rules | [README](https://github.com/dominikhei/cardamon/blob/main/README.md), [LICENSE](https://github.com/dominikhei/cardamon/blob/main/LICENSE) |
| `otel-gui` | Local OTLP viewer for traces, logs and metrics; source MIT and telemetry privacy risk | [README](https://github.com/metafab/otel-gui/blob/main/README.md), [LICENSE](https://github.com/metafab/otel-gui/blob/main/LICENSE) |
| `munin` | Master/node/plugin graphing; GNU GPLv2 core, contributed plugin boundaries unresolved | [README](https://github.com/munin-monitoring/munin/blob/master/README.rst), [COPYING](https://github.com/munin-monitoring/munin/blob/master/COPYING) |
| `nagios` | Nagios Core checks/plugins vs separately licensed Nagios XI; no automatic aggregate SPDX | [README](https://github.com/NagiosEnterprises/nagioscore/blob/master/README.md), [LICENSE](https://github.com/NagiosEnterprises/nagioscore/blob/master/LICENSE) |
| `syslog-ng` | Parsing/routing logs; upstream COPYING distinguishes LGPL core and GPL modules; no single SPDX | [README](https://github.com/syslog-ng/syslog-ng/blob/develop/README.md), [COPYING](https://github.com/syslog-ng/syslog-ng/blob/develop/COPYING) |

## RETAIN

- `kwatcher`: current [upstream](https://github.com/Berg-it/Kwatcher) is a ConfigMap sync/redeploy operator, not event watcher; root licensing and taxonomy require a separate review.
- `grove`: current [upstream](https://github.com/ai-dynamo/grove) is an AI inference gang-scheduling operator, not a Kubernetes troubleshooting agent; taxonomy requires a separate review.

## Merge gate

The PR remains **Draft, unmerged**, without auto-merge, tag, release or issue closure. Tests, Ruff, catalogue/schema checks, generated-doc check, review-debt, exact-SHA CI and strict full link audit must be recorded **PASS only if actually run**. Wave 39/40 Draft PRs stay untouched.
