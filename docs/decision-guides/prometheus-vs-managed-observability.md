# Prometheus-based versus managed observability

| Consideration | Self-managed Prometheus ecosystem | Managed observability |
|---|---|---|
| Control and portability | High | Vendor-dependent |
| Operating burden | Storage, upgrades, scaling, and on-call | Mostly delegated |
| Cost shape | Infrastructure plus engineering time | Ingest, retention, query, and seat pricing |
| Integration | Open ecosystem and PromQL | Often broad, with proprietary features |

Self-manage when control, data locality, custom retention, or portability justifies an observability team. Use managed services when reduced operational load outweighs ingest cost and lock-in. OpenTelemetry can preserve instrumentation portability in either model.
