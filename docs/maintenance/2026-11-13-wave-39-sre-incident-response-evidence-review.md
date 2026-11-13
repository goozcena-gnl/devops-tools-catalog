# Wave 39 — SRE, incident response and on-call evidence review

- Inspected: **2026-11-13**.
- Issue: [#173](https://github.com/goozcena-gnl/devops-tools-catalog/issues/173).
- Frozen `main`: `62e33cfc0d4b682a65799e0b73d1c2c8bc71c154`.
- Frozen canonical YAML Git blob: `d8b847e4e367d911f24857db52b41742963f3cf6`.
- Category file: `data/tools/sre-incident-response-on-call.yaml`.
- **21** canonical raw records / **14** needs-review before and after.
- **7** evidence-bounded metadata corrections; **3** selected RETAIN and **11** nonselected raw blocks unchanged.
- The generated category page may include cross-category records; it is not the raw canonical record count.
- All 10 selected records retain `status: needs-review`, `needs_review: true`, `maturity: unknown` and their historical `verified_on` values. **No CLEAR/active promotion.**
- The original `legacy:` source entries are preserved byte-for-byte.

## Seven field-level changes (source/edition boundaries)

| Canonical ID | Boundary and decision | Primary dated evidence |
| --- | --- | --- |
| `combodo-itop` | Self-hosted ITSM/CMDB; `AGPL-3.0-only` refers specifically to the iTop source package's declared licence in `composer.json`, not commercial extensions; open-core model retained | [iTop source package](https://github.com/Combodo/iTop/blob/develop/composer.json), [upstream](https://github.com/Combodo/iTop), [Combodo offers](https://combodo.com/fr/offres-services/) |
| `goalert` | Apache-2.0 upstream on-call scheduling, escalations and self-hosted deployment; no claim that external telecom services are free | [GoAlert upstream](https://github.com/target/goalert), [official documentation](https://goalert.me/docs/) |
| `manageengine-netflow-analyzer` | Vendor-proprietary commercial licence with a separately documented free **two-interface** tier; not OSS; distinct from ManageEngine ITOM umbrella | [Product](https://www.manageengine.com/products/netflow/), [licensing](https://www.manageengine.com/products/netflow/help/licensing.html), [EULA](https://www.manageengine.com/eu/products/netflow/license.html) |
| `ntfy` | OSS upstream, separate hosted paid service; upstream README explicitly dual-licenses source Apache-2.0/GPLv2. No single product-wide SPDX was assigned | [upstream README](https://github.com/binwiederhier/ntfy/blob/main/README.md), [FAQ](https://docs.ntfy.sh/faq/), [configuration](https://docs.ntfy.sh/config/) |
| `server-pulse` | Linux terminal utility, Docker required for documented container capabilities, GPLv3 family from source LICENSE; no unsupported SPDX only/or-later suffix | [upstream README](https://github.com/Server-Pulse/server-pulse/blob/main/README.md), [LICENSE](https://github.com/Server-Pulse/server-pulse/blob/main/LICENSE) |
| `wireshark` | Source-scoped `GPL-2.0-or-later` documented by the project's developer guide; not a claim for every bundled library | [official upstream](https://gitlab.com/wireshark/wireshark), [developer guide](https://www.wireshark.org/docs/wsdg_html/), [documentation](https://www.wireshark.org/docs/) |
| `zenduty` | Historical ID preserved, public name updated to Xurrent IMR; vendor-documented commercial hosted offering, without invented OSS source | [rename announcement 2025-11-13](https://www.xurrent.com/blog/zenduty-is-rebranding-to-xurrent-imr), [product](https://www.xurrent.com/incident-management-response), [pricing](https://www.xurrent.com/pricing/incident-management-response) |

## D1/D2/D3 — RETAIN unchanged

- **D1 `manageengine-it-operations-management`**: vendor umbrella vs single OpManager Nexus remains a separate taxonomy decision. Sources: [ITOM products](https://www.manageengine.com/it-operations-management.html), [Nexus](https://www.manageengine.com/it-operations-management/itom.html). **Full raw YAML block frozen; licence model unknown.**
- **D2 `moogsoft`**: current product boundaries between legacy Onprem/Hosted v9.x and Dell's renamed APEX AIOps cloud offering remain unresolved. Sources: [acquisition announcement](https://www.moogsoft.com/dell-technologies-acquires-moogsoft/), [Dell hosting terms](https://www.dell.com/en-us/legal/lp/cloud-and-hosting-services), [documentation portal](https://docs.moogsoft.com/). **Full raw YAML block frozen; licence model unknown.**
- **D3 `patchmon`**: Community source AGPLv3 confirmed by [repo LICENSE](https://github.com/PatchMon/PatchMon/blob/main/LICENSE), but PRO marketed as services in the [PRO page](https://patchmon.net/pro) versus licensed edition under the [2026 terms](https://patchmon.net/legal/terms-of-service). **Full raw YAML block frozen; licence model unknown** pending vendor reconciliation.

## Exact scope and future decision gates

- Canonical modified IDs: `combodo-itop`, `goalert`, `manageengine-netflow-analyzer`, `ntfy`, `server-pulse`, `wireshark`, `zenduty`.
- The **14** other raw YAML blocks, including all three selected RETAIN records, remain byte-identical.
- Exact per-record field allowlist and previous human decisions: [Wave 39 planning checkpoint](https://github.com/goozcena-gnl/devops-tools-catalog/issues/173#issuecomment-6864425423).
- No licence assigned from a third-party integration repo or hosted plan; no inferred service subscription rights from a source LICENSE.
- Generated-file allowlist is derived **only from the actual `scripts.generate_docs` diff**, not guessed in advance.
- Locally validate with locked Python 3.12 dependencies (Windows may require separate `colorama` platform pin for strict installed-package comparison), `generate_docs` and `--check`, `validate_catalog`, `review_debt`, Ruff check and format check, full pytest, whitespace and index guard.
- Record CI and strict link audit outcomes only **after** exact-SHA runs; this ledger makes no fabricated PASS claim for future CI.
- A separate maintainer decision is required before merging; keep any PR **Draft**, no auto-merge, no tag/release, and leave unrelated PR #132 and issue #2 untouched.
