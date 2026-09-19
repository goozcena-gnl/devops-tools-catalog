# Controlled access recheck Batch A — 2026-09-19

This review covers exactly the 13 URLs classified as `dns-inconclusive`,
`network-inconclusive`, `rate-limited`, or `transient-failure` in the committed
report at baseline `be14416b0832302b986252b8e3101a6108dca636`. The 16
`restricted-or-bot-blocked` URLs are excluded. Network behavior is triage
evidence, not lifecycle or canonical-identity evidence.

## Canonical mapping

| URL | Record | Canonical file | Field | Existing class |
| --- | --- | --- | --- | --- |
| `https://docs.k0sproject.io/` | `k0s` | `data/tools/kubernetes-distributions-operations.yaml` | `documentation_url` | `dns-inconclusive` |
| `https://getmantis.ai` | `mantis` | `data/tools/ci-build-testing.yaml` | `official_url` | `dns-inconclusive` |
| `https://hoji.ai` | `hoji-ai` | `data/tools/mlops-llmops-ai-infrastructure.yaml` | `official_url` | `dns-inconclusive` |
| `https://kuttl.dev` | `kuttl` | `data/tools/kubernetes-networking-storage-addons.yaml` | `official_url` | `dns-inconclusive` |
| `https://openkruise.io` | `openkruise` | `data/tools/kubernetes-networking-storage-addons.yaml` | `official_url` | `dns-inconclusive` |
| `https://ssoready.com/` | `ssoready` | `data/tools/iam-secrets-certificates.yaml` | `official_url` | `dns-inconclusive` |
| `https://ssoready.com/docs` | `ssoready` | `data/tools/iam-secrets-certificates.yaml` | `documentation_url` | `dns-inconclusive` |
| `https://criu.org/Main_Page` | `criu` | `data/tools/virtualization-bare-metal-homelab.yaml` | `official_url`; `documentation_url` | `network-inconclusive` |
| `https://docs.ansible.com/ansible/latest/collections/kubernetes/core/` | `ansible-kubernetes-core` | `data/tools/configuration-management.yaml` | `documentation_url` | `rate-limited` |
| `https://docs.ansible.com/projects/lint/` | `ansible-lint` | `data/tools/ci-build-testing.yaml` | `official_url`; `documentation_url` | `rate-limited` |
| `https://docs.ansible.com/projects/molecule/` | `ansible-molecule` | `data/tools/ci-build-testing.yaml` | `official_url`; `documentation_url` | `rate-limited` |
| `https://docs.cloudstack.apache.org` | `apache-cloudstack` | `data/tools/cloud-platforms-management.yaml` | `documentation_url` | `rate-limited` |
| `https://git.joeyh.name/index.cgi/etckeeper.git` | `etckeeper` | `data/tools/configuration-management.yaml` | `repository_url` | `transient-failure` |

The 13 URLs have 16 field consumers across 11 canonical records. All mapped
records and fields were reviewed mechanically; none changed.

## Controlled retry method

Three independent rounds ran between `2026-09-19T10:26:03+02:00` and
`2026-09-19T10:27:59+02:00`. Each round used normal system DNS resolution, a
bounded HEAD request, and a bounded GET with `Range: bytes=0-1023`. Requests
used the repository checker user agent, a 12-second timeout, at least two
seconds between requests to the same host, and eight seconds between rounds.
No credentials, IP rotation, aggressive browser impersonation, or protection
bypass was used.

## Targeted observations and decisions

| URL | Previous class | Attempt 1 | Attempt 2 | Attempt 3 | Final assessment | Canonical change |
| --- | --- | --- | --- | --- | --- | --- |
| `https://docs.k0sproject.io/` | DNS | `10:26:03`; DNS resolved; HEAD 200; GET 206 | `10:26:46`; DNS resolved; HEAD 200; GET 206 | `10:27:27`; DNS resolved; HEAD 200; GET 206 | RECOVERED | none |
| `https://getmantis.ai` | DNS | `10:26:05`; direct DNS resolved; HTTP resolver failed | `10:26:48`; direct DNS resolved; HTTP resolver failed | `10:27:29`; direct DNS resolved; HTTP resolver failed | ENVIRONMENT-DEPENDENT | none |
| `https://hoji.ai` | DNS | `10:26:07`; DNS/HEAD/GET resolution failed | `10:26:50`; DNS/HEAD/GET resolution failed | `10:27:32`; DNS/HEAD/GET resolution failed | REPRODUCED | none |
| `https://kuttl.dev` | DNS | `10:26:10`; DNS/HEAD/GET resolution failed | `10:26:52`; DNS/HEAD/GET resolution failed | `10:27:34`; DNS/HEAD/GET resolution failed | REPRODUCED | none |
| `https://openkruise.io` | DNS | `10:26:12`; DNS resolved; HEAD 200; GET 206 | `10:26:54`; DNS resolved; HEAD 200; GET 206 | `10:27:36`; DNS resolved; HEAD 200; GET 206 | RECOVERED | none |
| `https://ssoready.com/` | DNS | `10:26:14`; DNS/HEAD/GET resolution failed | `10:26:56`; DNS/HEAD/GET resolution failed | `10:27:38`; DNS/HEAD/GET resolution failed | REPRODUCED | none |
| `https://ssoready.com/docs` | DNS | `10:26:18`; DNS/HEAD/GET resolution failed | `10:27:00`; DNS/HEAD/GET resolution failed | `10:27:42`; DNS/HEAD/GET resolution failed | REPRODUCED | none |
| `https://criu.org/Main_Page` | network | `10:26:20`; DNS resolved; HEAD/GET 200 | `10:27:02`; DNS resolved; HEAD/GET 200 | `10:27:44`; DNS resolved; HEAD/GET 200 | RECOVERED | none |
| `https://docs.ansible.com/ansible/latest/collections/kubernetes/core/` | rate limit | `10:26:23`; HEAD/GET 200; official redirect | `10:27:04`; HEAD/GET 200; official redirect | `10:27:46`; HEAD/GET 200; official redirect | RECOVERED | none |
| `https://docs.ansible.com/projects/lint/` | rate limit | `10:26:27`; HEAD/GET 200 | `10:27:08`; HEAD/GET 200 | `10:27:50`; HEAD/GET 200 | RECOVERED | none |
| `https://docs.ansible.com/projects/molecule/` | rate limit | `10:26:31`; HEAD/GET 200 | `10:27:12`; HEAD/GET 200 | `10:27:54`; HEAD/GET 200 | RECOVERED | none |
| `https://docs.cloudstack.apache.org` | rate limit | `10:26:33`; HEAD/GET 429 | `10:27:15`; HEAD/GET 429 | `10:27:56`; HEAD/GET 429 | REPRODUCED | none |
| `https://git.joeyh.name/index.cgi/etckeeper.git` | transient | `10:26:35`; HEAD/GET 500 | `10:27:17`; HEAD/GET 500 | `10:27:59`; HEAD/GET 500 | REPRODUCED | none |

The Ansible Kubernetes collection URL redirects to the owner-controlled
`/projects/ansible/latest/` path, but redirect behavior alone does not authorize
a canonical rewrite. The [etckeeper install page](https://etckeeper.branchable.com/install/)
continues to identify Joey Hess's git service and gitweb as the authoritative
source, so the repeated HTTP 500 is an access outcome rather than repository
identity evidence.

## Fresh full-audit comparison

Both audits checked 2,586 catalogue URLs with authenticated GitHub repository
checks, archived-repository inspection, strict mode, and independent fresh
external caches.

| URL | Previous | Fresh A | Fresh B | Human assessment |
| --- | --- | --- | --- | --- |
| `https://docs.k0sproject.io/` | `dns-inconclusive` | `valid` | `valid` | RECOVERED |
| `https://getmantis.ai` | `dns-inconclusive` | `dns-inconclusive` | `dns-inconclusive` | ENVIRONMENT-DEPENDENT |
| `https://hoji.ai` | `dns-inconclusive` | `dns-inconclusive` | `dns-inconclusive` | REPRODUCED |
| `https://kuttl.dev` | `dns-inconclusive` | `dns-inconclusive` | `dns-inconclusive` | REPRODUCED |
| `https://openkruise.io` | `dns-inconclusive` | `valid` | `valid` | RECOVERED |
| `https://ssoready.com/` | `dns-inconclusive` | `dns-inconclusive` | `dns-inconclusive` | REPRODUCED |
| `https://ssoready.com/docs` | `dns-inconclusive` | `dns-inconclusive` | `dns-inconclusive` | REPRODUCED |
| `https://criu.org/Main_Page` | `network-inconclusive` | `valid` | `valid` | RECOVERED |
| `https://docs.ansible.com/ansible/latest/collections/kubernetes/core/` | `rate-limited` | `permanent-redirect` | `permanent-redirect` | RECOVERED |
| `https://docs.ansible.com/projects/lint/` | `rate-limited` | `valid` | `valid` | RECOVERED |
| `https://docs.ansible.com/projects/molecule/` | `rate-limited` | `valid` | `valid` | RECOVERED |
| `https://docs.cloudstack.apache.org` | `rate-limited` | `rate-limited` | `rate-limited` | REPRODUCED |
| `https://git.joeyh.name/index.cgi/etckeeper.git` | `transient-failure` | `transient-failure` | `transient-failure` | REPRODUCED |

Fresh A: `blocking_new: 0`, `blocking_known: 6`, strict PASS. Fresh B:
`blocking_new: 0`, `blocking_known: 6`, strict PASS. The immediate cached repeat
of B reproduced B exactly. Fresh A and B agree for every selected URL. Their
small aggregate differences came from unrelated non-strict access fluctuations,
including the excluded restricted cohort, and were not used as canonical
evidence.

The final tracked report is fresh B because every target classification agreed
between A and B and its cached repeat was identical. The six-entry reviewed
strict-blocker baseline is unchanged.

## Scope result

- Target URLs: `13`
- Canonical IDs changed: `0`
- Canonical fields changed: `0`
- Added or removed canonical IDs: `0`
- Generated catalogue documents changed: `0`
- Test files changed: `0`
- Baseline entries changed: `0`
- Restricted/bot-blocked URLs reviewed: `0`
- Tracker mutations: `0`

