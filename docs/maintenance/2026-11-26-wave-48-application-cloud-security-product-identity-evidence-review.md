# Wave 48 — Application & Cloud Security product identity evidence review

Selection issue [#210](https://github.com/goozcena-gnl/devops-tools-catalog/issues/210).

Base: `069596beaa98cd7bab823dc9b2297ad67c2111aa`. Contract SHA-256: `f576e54d35472e60134a794365fb34dbf6f6471879f0d9cf05582b1b9efba04a`.

Scope: nine reclassifications; one full RETAIN; 74 authorized field differences. Review flags, verification dates and taxonomy remain unchanged. The accepted historical transport report recorded 37 successful responses; reachability is not a licence attestation. The original response samples were not available for independent hashing.

| ID | Before | After | Decision | Changed keys |
| --- | --- | --- | --- | ---: |
| `wiz` | `unknown` | `commercial` | RECLASSIFY | 8 |
| `socket` | `unknown` | `commercial` | RECLASSIFY | 8 |
| `tenable-one` | `unknown` | `commercial` | RECLASSIFY | 8 |
| `virustotal` | `unknown` | `commercial` | RECLASSIFY | 8 |
| `threatlocker` | `unknown` | `commercial` | RECLASSIFY | 7 |
| `medusa` | `unknown` | `oss` | RECLASSIFY | 11 |
| `valqore` | `unknown` | `commercial` | RECLASSIFY | 8 |
| `aikido` | `open-core` | `commercial` | RECLASSIFY | 8 |
| `calico-cloud` | `open-core` | `commercial` | RECLASSIFY | 8 |
| `soos-dast` | `open-core` | `open-core` | RETAIN | 0 |

## Evidence and residual uncertainty

### wiz

Official platform, technical FAQ and modular pricing establish the commercial platform and distinguish agentless scanning from sensor-based runtime features.

Module-specific coverage, contract terms, data residency and sensor requirements need procurement and architecture review; no platform-wide source licence established.

Authorized source additions:
- `https://www.wiz.io/platform`
- `https://www.wiz.io/academy/cloud-security/how-to-evaluate-wiz-faq`
- `https://www.wiz.io/pricing`

### socket

Official FAQ and CLI documentation distinguish hosted analysis from the local client; the terms index distinguishes free and contractual service offerings.

Component licences, exact plan coverage and the full contract were not audited; no platform-wide SPDX or source repository is asserted.

Authorized source additions:
- `https://docs.socket.dev/docs/faq`
- `https://docs.socket.dev/docs/socket-cli-faq`
- `https://socket.dev/terms`

### tenable-one

Product page, platform deployment guide and current Foundation/Advanced licensing establish the exact commercial suite, not a vendor-wide GitHub organization.

Components have distinct hosted and self-managed deployment boundaries and licence entitlements. A global deployment model remains unset; no platform-wide source licence asserted.

Authorized source additions:
- `https://www.tenable.com/products/tenable-one`
- `https://docs.tenable.com/quick-reference/tenable-one-deployment-guide/Content/Welcome.htm`
- `https://docs.tenable.com/exposure-management/Content/getting-started/t1-foundation-advanced-licensing.htm`

### virustotal

Official service and API documentation establish public and paid offerings, sharing boundaries and the distinct paid Private Scanning service.

Private Scanning has different retention and analysis capabilities, including no antivirus verdicts according to its documentation. No confidentiality certification or platform-wide SPDX.

Authorized source additions:
- `https://docs.virustotal.com/docs/how-it-works`
- `https://docs.virustotal.com/docs/difference-public-private`
- `https://docs.virustotal.com/docs/private-scanning`

### threatlocker

Official allowlisting description, Linux agent installation guide and enterprise agreement establish commercial endpoint controls and specific Linux kernel support.

No blanket OS compatibility or feature parity claim. Global deployment model remains unset; kernel upgrades require vendor compatibility review.

Authorized source additions:
- `https://www.threatlocker.com/capabilities/allowlisting`
- `https://threatlocker.kb.help/linux-agent-installing-and-uninstalling-process/`
- `https://www.threatlocker.com/terms-and-conditions`

### medusa

Annotated tag object 5e02dfd1c74474d2b05bb2a403eac8ca2bddae8b resolves to release commit 5f217edf8b09b960a32311982754dd2717a70c9b. Pinned README and pyproject identify scanner package and AGPL-3.0-or-later; root LICENSE contains AGPL v3 text. README separates paid runtime offering; API reports repository not archived.

Tag unsigned; no binary/release signature or complete dependency/rule licence audit. commercial_offering=true records documented commercial licensing and separate runtime offering, not an assertion that the scanner itself is proprietary. Product homepage and rendered docs were not retrievable via the web tool, so retain existing vendor URL and use pinned README.

Authorized source additions:
- `https://github.com/Pantheon-Security/medusa/blob/5f217edf8b09b960a32311982754dd2717a70c9b/README.md`
- `https://github.com/Pantheon-Security/medusa/blob/5f217edf8b09b960a32311982754dd2717a70c9b/LICENSE`
- `https://github.com/Pantheon-Security/medusa/blob/5f217edf8b09b960a32311982754dd2717a70c9b/pyproject.toml`
- `https://github.com/Pantheon-Security/medusa/releases/tag/v2026.7.0`
- `https://github.com/Pantheon-Security/medusa`

### valqore

Pinned README and LICENSE at 7858a749905225720a94163a5e23403c147ec6a9 establish free public proprietary engine images and separately licensed AI image; pricing identifies commercial enterprise offering.

Pricing and FAQ do not establish that the AI licence is necessarily paid; no price claim. Public repository contains documentation/examples, not the engine source: repository_url and SPDX remain absent. Binary terms and signatures are not independently verified.

Authorized source additions:
- `https://github.com/valqore/valqore/blob/7858a749905225720a94163a5e23403c147ec6a9/README.md`
- `https://github.com/valqore/valqore/blob/7858a749905225720a94163a5e23403c147ec6a9/LICENSE`
- `https://www.valqore.io/pricing`
- `https://www.valqore.io/faq`

### aikido

Official pricing documents free and commercial plans; local scanner documentation requires a compatible account/workspace. Scope is the platform, not individual scanners.

No complete platform licence or exact scanner source correspondence established; local execution does not imply autonomous operation. Individual open-source components remain distinct.

Authorized source additions:
- `https://www.aikido.dev/pricing`
- `https://help.aikido.dev/code-scanning/local-code-scanning`

### calico-cloud

Official edition comparison and vendor pricing distinguish Calico Open Source, free tier, commercial SaaS and self-managed Enterprise.

No parent service SPDX or repository asserted; verify cluster support and connected data handling before adoption. Paid tier and free tier are distinct entitlements.

Authorized source additions:
- `https://docs.tigera.io/calico-cloud/about/calico-product-editions`
- `https://docs.tigera.io/calico/latest/about/calico-product-editions`
- `https://www.tigera.io/tigera-products/calico-cloud-pricing/`

### soos-dast

Existing URL is blocking-known in exact-SHA audit #116. Historical reviews document HTTP 404 Docker Hub, HTTP 410 vendor product/docs and HTTP 404 repository. Current web fetch also reported product HTTP 410 and GitHub API reported repository HTTP 404. No durable successor or wrapper licence established.

Entire original raw block must remain byte-identical. Retained open-core value is unresolved historical metadata, not an endorsement. No new SOOS URL in canonical data, no baseline waiver or closure of issue #2.

Authorized source additions:
- None.

## Validation requirements

Exact contract values, 164 byte-identical protected blocks, seven regenerated views and this maintenance report; 1,425 records in 30 categories. The external local evidence bundle records actual command outcomes and hashes. No CI, strict remote link audit, merge or issue closure is asserted by this report. SOOS DAST remains unresolved and the link baseline is unchanged.
