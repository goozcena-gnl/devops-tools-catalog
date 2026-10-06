# Aralez and Pandora FMS URL regression review

Reviewed on 2026-10-06. This is a bounded two-record maintenance change.

## Baseline and incident

- Starting main and branch base: `a9150d8f785afc6e1d850f41445d9c8a3f896b95` (PR #100 included).
- Branch: `maintenance/resolve-aralez-pandora-urls`.
- Working tree was clean before both edits; fetched main matched the supplied SHA exactly.
- P2 follow-up starts from PR HEAD `8326f604ca7a374afe0ee6cf641b1b3aee947cd4`; only `aralez.status` changes in canonical data, from `active` to `needs-review`. Pandora FMS and all canonical URLs remain unchanged.
- The supplied fresh Full link audit checked 2,605 URLs: `blocking_known: 6`, `blocking_new: 2`, strict FAIL.
- New blockers: `https://aralez.rs` and `https://pandorafms.com/community/pandora-fms-downloads`, each HEAD/GET 404 and `manual-verification-required`.
- A missing URL is not lifecycle evidence. No known baseline blocker is changed.

## Primary evidence

Aralez upstream is pinned to commit `a8dc98f636980b32613fb201f365bd905cbd3549`
(2026-10-05); its documentation is pinned to
`413fdeb8c75c56de50f6fc3035179eb87cad2585` (2026-10-04).

- A1: [Upstream README](https://github.com/sadoyan/aralez/blob/a8dc98f636980b32613fb201f365bd905cbd3549/README.md).
- A2: [Official documentation homepage source](https://github.com/sadoyan/aralez-docs/blob/413fdeb8c75c56de50f6fc3035179eb87cad2585/content/_index.md).
- A3: [Official Kubernetes documentation](https://github.com/sadoyan/aralez-docs/blob/413fdeb8c75c56de50f6fc3035179eb87cad2585/content/docs/kubernetes.md).
- A4: [Upstream licence](https://github.com/sadoyan/aralez/blob/a8dc98f636980b32613fb201f365bd905cbd3549/LICENSE).
- A5: [Release v.0.94.4](https://github.com/sadoyan/aralez/releases/tag/v.0.94.4), published 2026-10-05.
- A6: [Documentation repository README](https://github.com/sadoyan/aralez-docs/blob/413fdeb8c75c56de50f6fc3035179eb87cad2585/README.md) and [site configuration](https://github.com/sadoyan/aralez-docs/blob/413fdeb8c75c56de50f6fc3035179eb87cad2585/hugo.toml).
- P1: [Vendor landing page](https://pandorafms.com/en/) and [Pandora FMS product overview](https://pandorafms.com/en/product-overview/).
- P2: [Community page](https://pandorafms.com/en/community/).
- P3: [Downloads](https://pandorafms.com/en/downloads/).
- P4: [Releases](https://pandorafms.com/en/releases/).
- P5: [Current documentation](https://pandorafms.com/manual/!current/en/documentation/start).
- P6: [Historical upstream migration notice](https://github.com/pandorafms/pandorafms).
- P7: [Pandora OPEN upstream](https://github.com/pandorafms/pandora-open) and [project website](https://pandoraopen.io/).
- P8: [Vendor licence/version comparison](https://pandorafms.com/en/versions-comparative/).
- P9: [Vendor FAQ](https://pandorafms.com/en/faq/) and [vendor licence terms](https://pandorafms.com/downloads/PandoraFMS_License.pdf), sections 1 and 2.

The Aralez code and documentation repositories have the same upstream owner;
A6 identifies the documentation project and links back to the canonical code.
A1 and the repository homepage still advertise `aralez.rs` despite the incident's
404 results. The documentation configuration does not establish a replacement
hosted domain. GitHub is the evidence-backed fallback; no replacement domain is
invented. Both repositories are unarchived according to current GitHub metadata.

P2 identifies the original open-source branch as an independent Pandora OPEN
project after version 777. P6 says the old repository is no longer maintained
and directs active development to P7. GitHub's `archived` flag on the old
repository remains false: the maintainer's historical-archive wording must not
be confused with GitHub's technical archive state. P3 distinguishes the
agent-limited FMS Free edition from the commercial ONE trial; P8 describes
commercial on-premise/subscription licensing. No GPL grant from Pandora OPEN
is applied to the current Pandora FMS commercial product.
P9 independently confirms the Free/ONE versus OPEN distinction and a restricted
commercial use grant: the vendor licence reserves reproduction/distribution
rights and excludes its third-party open-source components from those claims.
Customer access to Enterprise source code in the FAQ is not an OSS grant.

## Aralez field review

| Field | Before | After | Primary evidence and reason |
|---|---|---|---|
| `id`, `name` | `aralez`, Aralez | Retained | A1/A2: same canonical project; no new identity or alias. |
| `summary` | Kubernetes operator (see docs). | Rust reverse proxy built on Cloudflare Pingora, with TLS, authentication, load balancing, and dynamic discovery through Consul and Kubernetes. | A1/A2: current identity and documented capabilities supersede the operator description. |
| `categories` | `kubernetes-networking-storage-addons` | Verified and retained | A3: ingress and Kubernetes discovery remain a valid taxonomy fit; the category does not imply that all uses require Kubernetes. |
| `subcategories` | Kubernetes Ecosystem & Add-ons | Reverse proxies & Kubernetes ingress | A1/A3: specific current function replaces generic operator-era grouping. |
| `roles` | platform-engineer, site-reliability-engineer, kubernetes-engineer | Retained, plus infrastructure-systems-engineer | A1/A3: Kubernetes integration supports existing roles; standalone proxy/systemd operation supports the additional role. Role mapping is maintainer judgment from those workflows. |
| `lifecycle_stages` | deploy, operate | Verified and retained | A1/A3: deployment, configuration, routing and ongoing operation. |
| `use_when` | You need its specific operator capabilities (consult docs). | HTTP reverse proxying with TLS, authentication and health-checked load balancing; dynamic Consul/Kubernetes discovery for ingress-style routing. | A1/A2/A3: adoption guidance now describes proxy capabilities. |
| `avoid_when` | A more established operator covers your use case. | You need a Kubernetes operator to reconcile application or infrastructure resources rather than proxy traffic. | A1/A3: maintainer boundary derived from the documented proxy role; no comparative maturity assertion. |
| `official_url` | `https://aralez.rs` | `https://github.com/sadoyan/aralez` | A1: canonical upstream fallback while the advertised website is unavailable. |
| `repository_url` | `https://github.com/sadoyan/aralez` | Verified and retained | A1/A6: canonical code repository. |
| `documentation_url` | `https://aralez.rs` | `https://github.com/sadoyan/aralez-docs/tree/main/content/docs` | A2/A3/A6: maintained official documentation source; hosted-domain replacement not established. |
| `license_model`, `license_spdx` | oss, Apache-2.0 | Verified and retained | A4: explicit Apache licence. |
| `maturity` | unknown | Retained as unresolved | A5 establishes releases, not adoption or production maturity. |
| `status` | active | needs-review | A5 and upstream commit history still evidence an active project. The catalogue methodology requires `status: needs-review` with `needs_review: true` while metadata remains unresolved. |
| `deployment_models`, `alternatives`, `tags` | Empty lists | Retained | No new comparative or deployment taxonomy claims added in this bounded repair. |
| `sources` | Two legacy references | Legacy references retained; A1, A2, A3, A4, A5 added | Preserve provenance and add current, pinned primary evidence. |
| `verified_on` | 2026-08-03 | 2026-10-06 | Date of this primary-source review. |
| `needs_review` | false | true | Website/documentation inconsistency and unverified maturity remain open; review debt is restored. |

Classification comparison: **Kubernetes operator** becomes **Rust/Pingora reverse
proxy with Kubernetes ingress/discovery integration**. Categories, roles and
adoption guidance now match that identity. Performance is an upstream claim,
not an independently measured benchmark in this review.

Upstream lifecycle evidence and catalogue review status are distinct. Release
and code activity on 2026-10-05 support active Aralez development. The catalogue
record uses `status: needs-review` because the advertised domain inconsistency
and maturity remain unresolved, following [catalogue methodology](../methodology.md).
Generated status views therefore expose the review debt. This does not assert
that Aralez itself is inactive, deprecated or archived.

## Pandora FMS field review

The entry represents the **Pandora FMS vendor monitoring product**, including
commercial and agent-limited free editions. It is not renamed to Pandora OPEN.
Historical identity and legacy provenance remain intact.

| Field | Before | After | Primary evidence and reason |
|---|---|---|---|
| `id`, `name` | `pandora-fms`, Pandora FMS | Retained | P1/P2: preserve the vendor product identity. |
| `summary` | Monitoring platform with community and enterprise editions. | Monitoring platform with commercial and agent-limited free editions; the former open-source branch continues independently as Pandora OPEN. | P2/P3/P7: explicitly distinguish current vendor editions from the independent continuation. |
| `official_url` | `https://pandorafms.com/community/pandora-fms-downloads` | `https://pandorafms.com/en/product-overview/` | P1: product-specific landing page matches this entry, rather than selecting a download endpoint solely for HTTP success. |
| `repository_url` | `https://github.com/pandorafms/pandorafms` | Removed; retained in `sources` | P6/P7: historical code is not the current commercial product repository; the replacement repository belongs to Pandora OPEN. |
| `documentation_url` | Absent | `https://pandorafms.com/manual/!current/en/documentation/start` | P2/P5: vendor-linked current documentation entry point. |
| `categories` | monitoring-metrics-logs-tracing | Verified and retained | P1/P5: monitoring/observability product. |
| `subcategories` | Monitoring & Observability Platforms | Verified and retained | P1/P5: platform scope. |
| `roles` | devops-engineer, site-reliability-engineer, observability-engineer | Verified and retained | P1/P5: monitoring and operations workflows; taxonomy mapping is maintainer judgment. |
| `lifecycle_stages` | operate, monitor | Verified and retained | P1/P5: ongoing infrastructure monitoring. |
| `use_when` | You need a single tool covering network, servers, and apps in traditional environments. | Verified and retained | P1/P5: supported monitoring scope. |
| `avoid_when` | Kubernetes-native or open-standards (OTel) alignment is required. | You require an entirely open-source platform; evaluate the independent Pandora OPEN project. | P2/P3/P7/P8: supported licence boundary replaces an unverified Kubernetes/OTel exclusion. |
| `license_model` | open-core | commercial | P2/P3/P8/P9: vendor commercial/free product editions and restricted commercial licence; open-source continuation is independent. This is an explicit boundary correction, not relicensing historical source. |
| `license_spdx` | Absent | Retained absent | No open-source SPDX grant asserted for the vendor product. |
| `maturity` | unknown | Retained as unresolved | No adoption/maturity reassessment attempted. |
| `status` | needs-review | Retained | Product is available (P1/P4), but unresolved record-level maturity keeps review debt open. No inference of deprecation from 404. |
| `deployment_models`, `alternatives`, `tags` | Empty lists | Retained | No new claims added outside the product/URL repair. |
| `sources` | Two legacy references | Legacy references retained; P1 product overview, P2, P3, P4, P5, P6, P7 upstream, P8, P9 added | Document the split and preserve the historical repository relationship. |
| `verified_on` | 2026-08-03 | 2026-10-06 | Date of this primary-source review. |
| `needs_review` | true | Retained true | Unverified maturity remains open; this repair does not claim complete review. |

## Scope and validation

Canonical dataset comparison against the starting SHA proves that exactly
`aralez` and `pandora-fms` changed; no record was added, removed or renamed.
The existing batch-05 test retains Aralez's licence coverage and explicitly
requires both `status: needs-review` and `needs_review: true`. Other fully
reviewed batch-05 tools retain `status: active` and `needs_review: false`.

Documentation was regenerated with `python -m scripts.generate_docs` and its
determinism checked with `python -m scripts.generate_docs --check`. Generated
changes are README statistics, catalogue statistics, the two category pages,
deploy/operate/monitor lifecycle pages, and the affected role pages.

The mandatory local `python -m scripts.python_constraints --check` detects only
Windows-specific `colorama==0.4.6` added by pytest relative to the Linux CI
constraints. Constraints are deliberately unchanged; the Linux CI check is
the authoritative platform-matched verification. Other validation results and
GitHub checks are reported in the PR/session final report.

## Initial URL-repair targeted strict link audit

The unchanged checker was run against an ignored temporary catalogue containing
only the two final records, with the unchanged default reviewed baseline:

```text
python -m scripts.check_links --root tmp/aralez-pandora-audit --strict --check-archived --workers 8 --cache-hours 0 --cache tmp/aralez-pandora-audit/cache.json --json-report tmp/aralez-pandora-audit/report.json --markdown-report tmp/aralez-pandora-audit/report.md
```

Four unique canonical URLs checked freshly: 3 `valid`, 1 `permanent-redirect`,
`blocking_new: 0`, strict PASS. The documentation repository path is normalized
to its repository root by the existing GitHub API checker; its actual content
was independently inspected through the GitHub file API. Both obsolete URLs
are absent from the entire catalogue's checked-URL set.

Before: `blocking_new: 2` in the supplied full audit. After: `blocking_new: 0`
in this targeted audit. No remaining blocker in the reviewed records. During
the initial URL repair, no full audit was run and no catalogue-wide total was claimed.
The six known blockers were outside the targeted sample; the report's
`baseline_resolved` entries reflect that omission, not actual resolution.
Raw audit output remains ignored and is not committed.

Supplemental direct HTTP checks in this session confirmed Aralez HEAD/GET 404
and the replacement documentation directory HEAD/GET 200. The obsolete Pandora
URL returned HEAD/GET 403 to this client, unlike the supplied full-audit 404;
that access difference is recorded without claiming the old URL recovered.
Its replacement is selected from the vendor's current navigation and product
boundary evidence, not from this response code.

`config/link-audit-baseline.json`: unchanged. Checker, link workflow, CodeQL
configuration, Python constraints and unrelated catalogue records: unchanged.
CodeQL alert #2 is excluded. No merge or release is performed.
