# Wave 42 — databases, caching and data infrastructure evidence review

- Evidence date: **2026-11-21**. Scope contract: [issue #192](https://github.com/goozcena-gnl/devops-tools-catalog/issues/192).
- Baseline `main`: `836cff55af3148e8b98f859da847a98cd22f521b`. Baseline canonical Git blob: `eaa892749a98d0f9c9fac4c3eebeee9153ea35d0`.
- The category has **27 raw canonical blocks**, including **14 marked `needs_review: true`**. Exactly **8 selected raw blocks** receive limited documentation and evidence changes; **2 RETAIN** (`redis`, `juicefs`) and **17 nonselected** blocks remain **byte-for-byte unchanged** (19 protected).
- All records retain their exact IDs, names, official URLs, categories, roles, lifecycle stages, licence model, status, `needs_review`, maturity, verification date and prior legacy provenance. All new official source URLs are append-only.
- Six code-scoped `license_spdx` additions: Apache Kafka (Apache-2.0), bbolt (MIT), etcd (Apache-2.0), Memcached (BSD-3-Clause), SeaweedFS (Apache-2.0), TiKV (Apache-2.0). **No overall SPDX** for RabbitMQ (MPL-2.0 with Apache-2.0 OCF exceptions) or Garage (AGPLv3 terms, no precise `-only`/`-or-later` assertion).

## Primary evidence and exact boundaries

| Canonical ID | Scoped decision | First-party evidence |
|---|---|---|
| `apache-kafka` | Distributed retained events, partitions and replay; not equivalent to a one-off task queue. | [README](https://github.com/apache/kafka/blob/trunk/README.md), [LICENSE](https://github.com/apache/kafka/blob/trunk/LICENSE) |
| `bbolt` | Embedded single-writer transactional Go store; no server or distributed replication. | [README](https://github.com/etcd-io/bbolt/blob/main/README.md), [LICENSE](https://github.com/etcd-io/bbolt/blob/main/LICENSE) |
| `etcd` | Replicated consistent KV, quorum, client/peer security, backup/restore responsibilities. | [Operations guide](https://etcd.io/docs/v3.6/op-guide/), [LICENSE](https://github.com/etcd-io/etcd/blob/main/LICENSE) |
| `garage` | Small/medium self-hosted geo-distributed S3-compatible object store; GitHub repo is a mirror of Deuxfleurs upstream. | [README](https://github.com/deuxfleurs-org/garage/blob/984cb2afe7b40e4818c727a2d1b0b017b7dadff1/README.md), [LICENSE](https://github.com/deuxfleurs-org/garage/blob/984cb2afe7b40e4818c727a2d1b0b017b7dadff1/LICENSE) |
| `memcached` | Disposable in-memory cache with eviction and expiration, not durable data storage. | [Docs](https://docs.memcached.org/), [LICENSE](https://github.com/memcached/memcached/blob/master/LICENSE) |
| `rabbitmq` | Routed messaging, quorum/stream choices and delivery semantics; core MPL-2.0 and OCF Apache-2.0 exceptions; separate commercial editions. | [Root LICENSE](https://github.com/rabbitmq/rabbitmq-server/blob/main/LICENSE), [Quorum queues](https://www.rabbitmq.com/docs/quorum-queues) |
| `seaweedfs` | Filer, volumes, S3, Docker and Helm; open source versus separately licensed Enterprise offerings. | [README](https://github.com/seaweedfs/seaweedfs/blob/master/README.md), [LICENSE](https://github.com/seaweedfs/seaweedfs/blob/master/LICENSE) |
| `tikv` | Raft and Placement Driver transactional key/value system, not TiDB SQL. | [README](https://github.com/tikv/tikv/blob/master/README.md), [Architecture](https://tikv.org/docs/7.1/reference/architecture/overview/), [LICENSE](https://github.com/tikv/tikv/blob/master/LICENSE) |

## Strict RETAIN

- `redis`: version-dependent BSD / RSAL / SSPL / AGPL licensing is not collapsed into one SPDX. [Official version matrix](https://redis.io/legal/licenses/).
- `juicefs`: Apache-2.0 community source is not a licence grant for Cloud/Enterprise. Keep the complete open-core record unchanged. [Community repository](https://github.com/juicedata/juicefs).

## Verification and human gate

Only the canonical YAML, its generated category page, its generated deploy/operate lifecycle summaries and this dated ledger are in scope. No README, statistics, role or taxonomy change is justified by these stable statuses.

Run and record **actual** outcomes for `python -m scripts.generate_docs`, `python -m scripts.validate_catalog`, `python -m scripts.generate_docs --check`, `python -m scripts.review_debt`, `python -m pytest`, `python -m ruff check scripts tests`, `python -m ruff format --check scripts tests`, `git diff --check`, exact-SHA required CI and an independent strict Full Link Audit. **Never claim PASS for unexecuted checks.** No merge, auto-merge, tag/release, status promotion or issue closure; retain the Draft PR for human review.
