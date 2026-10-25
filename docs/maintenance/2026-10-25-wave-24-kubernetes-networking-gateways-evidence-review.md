# Wave 24 — Kubernetes networking, CNI and gateways: evidence review

**Current Wave 24 decision (2026-10-25): 7 CLEAR / 3 RETAIN REVIEW.** The original first-pass triage remains below as historical evidence; the second-pass canonical edits and their field-level ledger are recorded later in this document. Current merged-`main` baseline: `bb9915c0edb093e32db9974ea26d73db189561b0`. **PR #140 remains Draft and unmerged**; independent review and a fresh strict Full link audit on the final PR HEAD remain pending.

**First pass observed:** 2026-10-25. **Historical stage: documentary triage only — 0 cleared; 10 pending at that time.** Selection contract: [issue #139](https://github.com/goozcena-gnl/devops-tools-catalog/issues/139). Pinned `main` baseline: `bb9915c0edb093e32db9974ea26d73db189561b0`.

This preliminary ledger reports **directly checked primary repository metadata, README files, releases and licence files**. The observations do *not* authorize automatic status clearance or assert that tags, hosted offerings, product editions, Kubernetes versions, or support have been comprehensively checked. A present `LICENSE` is evidence for the referenced source tree, not all services/dependencies/product tiers.

## First-pass inventory and scope (historical)

- Baseline: **1,425** canonical records, **785 active**, **626 needs-review**, 30 category files. No open PR at selection; URL tracker [#2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2) OPEN.
- Only permitted eventual canonical file: `data/tools/kubernetes-networking-storage-addons.yaml` (132 entries, 68 with both `status: needs-review` and `needs_review: true`).
- Exact ten pre-existing IDs: `flannel`, `kube-ovn`, `ovn-kubernetes`, `multus-cni`, `kgateway`, `nginx-gateway-fabric`, `cloudflare-kubernetes-gateway`, `project-contour`, `haproxy`, `chisel-operator`.
- All ten retain **`status: needs-review`** and **`needs_review: true`** at this stage. No canonical record or generated view changed in this first commit.
- Strict URL baseline `config/link-audit-baseline.json` holds six historical reviewed exceptions (blob SHA `a834e2af711693def40078a55e31dfeb29bee2c7`). Do not modify the baseline or close #2.

## First-pass versioned primary-source observations (historical)

| Canonical ID | Repository and directly inspected release | Inspected source licence | Proven scope and remaining questions |
|---|---|---|---|
| `flannel` | [flannel-io/flannel](https://github.com/flannel-io/flannel), [v0.28.10](https://github.com/flannel-io/flannel/releases/tag/v0.28.10), published 2026-10-08 | [v0.28.10 LICENSE: Apache-2.0](https://github.com/flannel-io/flannel/blob/v0.28.10/LICENSE) | README describes Kubernetes L3 inter-node fabric, **not native `flanneld` policy enforcement**; policy via optional Helm deployment/controller or other solutions. Confirm support matrix, compatibility, deploy modes and security before clearance. |
| `kube-ovn` | [kubeovn/kube-ovn](https://github.com/kubeovn/kube-ovn), [v1.16.15](https://github.com/kubeovn/kube-ovn/releases/tag/v1.16.15), published 2026-10-21 | [tagged LICENSE: Apache-2.0](https://github.com/kubeovn/kube-ovn/blob/v1.16.15/LICENSE) | README describes OVN/OVS-based CNI incl. VPC, KubeVirt and optional secondary-CNI mode. Verify feature/version support, licences of distributed pieces, migration/network-policy assumptions. **Distinct from OVN-Kubernetes.** |
| `ovn-kubernetes` | Historical catalogue [ovn-org/ovn-kubernetes](https://github.com/ovn-org/ovn-kubernetes) now GitHub API **301** to repository ID **65489927**, currently [ovn-kubernetes/ovn-kubernetes](https://github.com/ovn-kubernetes/ovn-kubernetes). [v1.4.0](https://github.com/ovn-kubernetes/ovn-kubernetes/releases/tag/v1.4.0), published 2026-09-04 | [v1.4.0 LICENSE: Apache-2.0](https://github.com/ovn-kubernetes/ovn-kubernetes/blob/v1.4.0/LICENSE) | Primary GitHub repository continuity is supported by ID, not merely a guessed URL. README describes OVN + OVS Kubernetes networking. Confirm deployment/support boundaries and record canonical migration before any field update. |
| `multus-cni` | [k8snetworkplumbingwg/multus-cni](https://github.com/k8snetworkplumbingwg/multus-cni), [v4.3.1](https://github.com/k8snetworkplumbingwg/multus-cni/releases/tag/v4.3.1), published 2026-09-08 | [v4.3.1 LICENSE: Apache-2.0](https://github.com/k8snetworkplumbingwg/multus-cni/blob/v4.3.1/LICENSE) | README establishes multi-interface **CNI meta-plugin** relying on a default CNI for primary pod networking; check NetworkAttachmentDefinition versions, delegation, security, host and Kubernetes support. |
| `kgateway` | [kgateway-dev/kgateway](https://github.com/kgateway-dev/kgateway); **stable v2.4.7** published 2026-10-16; [v2.5.0-beta.4](https://github.com/kgateway-dev/kgateway/releases/tag/v2.5.0-beta.4) published 2026-10-23 is a **prerelease** | [v2.5.0-beta.4 LICENSE: Apache-2.0](https://github.com/kgateway-dev/kgateway/blob/v2.5.0-beta.4/LICENSE); verify stable-tag identical grant | README describes Gateway API control plane and Envoy-based data plane. Avoid labeling beta stable. Verify Gateway API conformance versions, experimental AI functionality and community vs commercial support. |
| `nginx-gateway-fabric` | [nginx/nginx-gateway-fabric](https://github.com/nginx/nginx-gateway-fabric), [v2.8.0](https://github.com/nginx/nginx-gateway-fabric/releases/tag/v2.8.0), published 2026-10-14 | [v2.8.0 LICENSE: Apache-2.0](https://github.com/nginx/nginx-gateway-fabric/blob/v2.8.0/LICENSE) | README describes NGINX Gateway API implementation, with protocol/resource compatibility matrix in official docs. Distinguish this project from Ingress NGINX or NGINX Plus; verify edition boundary and route maturity. |
| `cloudflare-kubernetes-gateway` | [pl4nty/cloudflare-kubernetes-gateway](https://github.com/pl4nty/cloudflare-kubernetes-gateway), [v0.10.1](https://github.com/pl4nty/cloudflare-kubernetes-gateway/releases/tag/v0.10.1), published 2026-07-11 | [v0.10.1 LICENSE: MIT](https://github.com/pl4nty/cloudflare-kubernetes-gateway/blob/v0.10.1/LICENSE), copyright Tom Plant | README describes a third-party operator managing ingress via Cloudflare Tunnels and Gateway API; requires Cloudflare account API token and Kubernetes Secret. **Do not claim corporate Cloudflare ownership** of pl4nty repo; review RBAC/token scope and upstream stability. |
| `project-contour` | [projectcontour/contour](https://github.com/projectcontour/contour), [v1.33.7](https://github.com/projectcontour/contour/releases/tag/v1.33.7), published 2026-09-07 | [v1.33.7 LICENSE: Apache-2.0](https://github.com/projectcontour/contour/blob/v1.33.7/LICENSE) | README confirms Envoy-backed Kubernetes ingress, HTTPProxy CRD and Gateway API integration. Need official support/version matrix, controller permissions, security guidance and release maintenance assessment. |
| `haproxy` | [haproxy/haproxy](https://github.com/haproxy/haproxy), **development mirror** of [git.haproxy.org](https://git.haproxy.org/); GitHub releases API yielded no published releases | [upstream master LICENSE](https://github.com/haproxy/haproxy/blob/master/LICENSE) discusses GPL-2.0 and distinct licensing of certain headers; **not an Apache-2.0 blanket grant** | This is the core, generic TCP/HTTP proxy, **not HAProxy Kubernetes Ingress**. Verify official version-specific licence exceptions, release/version policy, hosted/enterprise boundaries and scope. Do not infer release inactivity from the empty GitHub Releases API on a mirror. |
| `chisel-operator` | [FyraLabs/chisel-operator](https://github.com/FyraLabs/chisel-operator), [v0.7.1](https://github.com/FyraLabs/chisel-operator/releases/tag/v0.7.1), published 2025-12-20 | [v0.7.1 LICENSE.md: GPL-3.0 text](https://github.com/FyraLabs/chisel-operator/blob/v0.7.1/LICENSE.md) — check exact SPDX version grant | README describes Kubernetes operator for exposing private cluster services via upstream [Chisel](https://github.com/jpillora/chisel) SSH tunnels, with external exit nodes. Not the upstream Chisel application itself. Review egress secrets, SSH trust, exposed-service risk and licence implications. |

Repository metadata inspection on 2026-10-25 reports all ten canonical source repositories as **unarchived**; this is an observation, *not* proof of sustained support, completed security review, GA stability or licence compatibility.

## First-pass evidence gaps (historical)

1. Read exact documentation/source **at pinned stable tags**, not only unversioned repository README. Link versioned compatibility matrices, architectural and authentication/security controls, first-party licence notices, release and governance/maintenance statements; record dated provenance per assertion. Pay special attention to product and controller identity (four CNI vs four Gateway API vs generic HAProxy vs Chisel).
2. Resolve whether OVN-Kubernetes repository URL should be updated to its current primary repository path; keep historic sources and stable catalogue ID. Confirm origin with immutable GitHub ID **65489927**, and do not conflate with Kube-OVN.
3. Independently inspect HAProxy versioned licensing, header exceptions, package/community vs enterprise boundaries, and official release policy; do not assign a simplistic SPDX label from a GitHub API badge.
4. Confirm kgateway latest **stable** tagged release and stable-tag licence separately from its current 2.5 prereleases.
5. For Cloudflare Kubernetes Gateway verify third-party maintainer/ownership, Cloudflare API token permissions/rotation and supported Gateway API surface; do not equate a Cloudflare API integration with Cloudflare company ownership.
6. For Chisel Operator determine whether the exact tagged licence grant is GPL-3.0-only or GPL-3.0-or-later, verify exposure/security assumptions, and whether Chisel dependencies or external exit nodes change adoption guidance.
7. For all ten, decide **CLEAR vs RETAIN REVIEW** on individually complete evidence, with no quota. Add field-level before/after/source rows only if canonical fields change; retain unresolved facts as explicit debt.
8. Preserve legacy sources, taxonomy, canonical IDs, all unrelated records, strict link exceptions, tests and generated views until official generator is run after any canonical change.

## First-pass execution contract (historical)

The next implementation stage may edit only these ten canonical records in `data/tools/kubernetes-networking-storage-addons.yaml`, keeping every other ID unchanged. Regenerate with `python -m scripts.generate_docs` (not direct Markdown edits) and verify `python -m scripts.generate_docs --check`; then locked Python 3.12 verification and `pip check`, Ruff lint/format, full pytest, `python -m scripts.validate_catalog`, `git diff --check`. Confirm expected counts, CI security gates and independent Codex/human P1/P2 review on final head. Manually run a **new strict Full link audit on the exact final SHA** and demand `blocking_new: 0`, `strict_result: PASS`, unchanged six known exception URL/classification pairs. No merge/auto-merge, release, tag, waived protections, or closing [#2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2). Close #139 only after explicit human merge and all post-merge `main` checks.

**Actions in that first-pass stage (historical):** evidence ledger only. Zero canonical changes; zero status flips; no generated docs touched; no tests or network audit run in this GitHub-only step.


## Second pass — evidence-scoped canonical decisions (2026-10-25)

**This section supersedes the initial documentary-triage count of 0/10 cleared above.**
**7 CLEAR / 3 RETAIN REVIEW** is the result proposed for this second pass, subject to
final generator checks, regression tests, CI, independent review, and strict link audit.
The original first-pass record remains above as dated evidence, not the current result.

| Decision | Stable canonical IDs |
|---|---|
| CLEAR (7) | `flannel`, `kube-ovn`, `ovn-kubernetes`, `multus-cni`, `kgateway`, `nginx-gateway-fabric`, `project-contour` |
| RETAIN REVIEW (3) | `cloudflare-kubernetes-gateway`, `haproxy`, `chisel-operator` |

**Important limits documented by primary sources:**

- Flannel v0.28.10 `flanneld` does not natively enforce NetworkPolicy; separate policy components are necessary.
- Kube-OVN and OVN-Kubernetes are different projects even though both use OVN/OVS.
  OVN-Kubernetes historical GitHub owner path redirects to `ovn-kubernetes/ovn-kubernetes`
  with immutable GitHub repository ID `65489927`.
- Multus v4.3.1 is a multi-interface **meta-plugin** which delegates to a default primary CNI.
- Kgateway v2.4.7 is a stable release; v2.5.0-beta.4 is a prerelease, not a GA upgrade.
- NGINX Gateway Fabric v2.8.0 and Contour v1.33.7 publish compatibility matrices;
  Gateway API extended routes/filters must not be presumed universally supported.
- The independently maintained `pl4nty/cloudflare-kubernetes-gateway` v0.10.1 has MIT
  source licensing but explicitly incomplete Gateway API v1 Core functionality and
  documented limitations around DNS cleanup. Cloudflare account tokens and Kubernetes
  Secrets need careful privilege management. **Retain review**.
- HAProxy generic core is not HAProxy Kubernetes Ingress. Its source LICENSE discusses
  GPL core, LGPL-exportable headers and an OpenSSL exception; the canonical SPDX grant
  cannot be guessed solely from GitHub metadata. **Retain review**.
- Chisel Operator's v0.7.1 source contains a GPL-3.0 licence document, but the precise
  `-only`/`-or-later` statement and external SSH tunnel/exit-node security require
  more review. Do not assign an unproven exact SPDX identifier. **Retain review**.

No `maturity` score has been invented; `active` is a reviewed catalogue status, not a
claim that every production deployment is suitable. Retained records remain
`status: needs-review` and `needs_review: true`, with specific usage warnings and
new primary evidence links. Legacy provenance is preserved. No unrelated IDs or
canonical fields were changed.

### Field-level before / after ledger (only changed fields)


#### `chisel-operator` — RETAIN REVIEW

| Canonical field | Before | After |
|---|---|---|
| `summary` | summary: Operator for managing Chisel tunnels in Kubernetes. | summary: "Kubernetes operator for exposing LoadBalancer services via Chisel SSH tunnels and external exit nodes." |
| `avoid_when` | avoid_when: ⏎   - You have proper ingress, VPN, or cloud load balancers available. | avoid_when: ⏎   - You have proper ingress, VPN, or cloud load balancers available. ⏎   - "You cannot secure SSH exit-node access, exposed service endpoints, or cloud API and operator credentials." ⏎   - "You require a verified exact GPL-3.0-only versus -or-later grant or confirmed long-term production support." |
| `repository_archived` | (absent) | repository_archived: false |
| `status` | status: needs-review | status: "needs-review" |
| `verified_on` | verified_on: '2026-08-03' | verified_on: "2026-10-25" |
| `sources` | sources: ⏎   - legacy:4_Kubernetes-Containers/README.md#L78 ⏎   - legacy:devopstools_final.md#L539 | sources: ⏎   - legacy:4_Kubernetes-Containers/README.md#L78 ⏎   - legacy:devopstools_final.md#L539 ⏎   - https://github.com/FyraLabs/chisel-operator/blob/v0.7.1/LICENSE.md ⏎   - https://github.com/FyraLabs/chisel-operator/blob/v0.7.1/README.md ⏎   - https://github.com/FyraLabs/chisel-operator/releases/tag/v0.7.1 |

#### `cloudflare-kubernetes-gateway` — RETAIN REVIEW

| Canonical field | Before | After |
|---|---|---|
| `summary` | summary: Cloudflare gateway for Kubernetes clusters. | summary: "Independently maintained Kubernetes Gateway API controller for exposing selected services via Cloudflare Tunnels." |
| `avoid_when` | avoid_when: ⏎   - You don't use Cloudflare or need a vendor-neutral ingress solution. | avoid_when: ⏎   - You don't use Cloudflare or need a vendor-neutral ingress solution. ⏎   - "You require full Gateway API v1 Core, weighted routes, or automatic cleanup of obsolete Cloudflare DNS records." ⏎   - "You cannot protect and rotate scoped Cloudflare Tunnel and DNS tokens stored in Kubernetes Secrets." |
| `repository_archived` | (absent) | repository_archived: false |
| `license_spdx` | (absent) | license_spdx: "MIT" |
| `status` | status: needs-review | status: "needs-review" |
| `verified_on` | verified_on: '2026-08-03' | verified_on: "2026-10-25" |
| `sources` | sources: ⏎   - legacy:4_Kubernetes-Containers/README.md#L80 ⏎   - legacy:devopstools_final.md#L543 | sources: ⏎   - legacy:4_Kubernetes-Containers/README.md#L80 ⏎   - legacy:devopstools_final.md#L543 ⏎   - https://github.com/pl4nty/cloudflare-kubernetes-gateway/blob/v0.10.1/LICENSE ⏎   - https://github.com/pl4nty/cloudflare-kubernetes-gateway/blob/v0.10.1/README.md ⏎   - https://github.com/pl4nty/cloudflare-kubernetes-gateway/releases/tag/v0.10.1 |

#### `flannel` — CLEAR

| Canonical field | Before | After |
|---|---|---|
| `summary` | summary: Simple Layer 3 network fabric (CNI) for Kubernetes. | summary: "Kubernetes layer-3 network fabric for pod traffic across nodes; network policy requires a separate controller." |
| `use_when` | use_when: [] | use_when: ⏎   - "You need straightforward layer-3 Kubernetes inter-node networking." |
| `avoid_when` | avoid_when: [] | avoid_when: ⏎   - "You require native NetworkPolicy enforcement in flanneld; deploy a compatible policy controller." |
| `repository_archived` | (absent) | repository_archived: false |
| `license_spdx` | (absent) | license_spdx: "Apache-2.0" |
| `status` | status: needs-review | status: "active" |
| `verified_on` | verified_on: '2026-08-03' | verified_on: "2026-10-25" |
| `sources` | sources: ⏎   - legacy:devopstools_final.md#L557 | sources: ⏎   - legacy:devopstools_final.md#L557 ⏎   - https://github.com/flannel-io/flannel/blob/v0.28.10/LICENSE ⏎   - https://github.com/flannel-io/flannel/blob/v0.28.10/README.md ⏎   - https://github.com/flannel-io/flannel/releases/tag/v0.28.10 |
| `needs_review` | needs_review: true | needs_review: false |

#### `haproxy` — RETAIN REVIEW

| Canonical field | Before | After |
|---|---|---|
| `summary` | summary: Reliable, high-performance TCP/HTTP load balancer. | summary: "General-purpose high-performance TCP/HTTP reverse proxy and load balancer, distinct from HAProxy Kubernetes Ingress." |
| `avoid_when` | avoid_when: ⏎   - Cloud-native load balancers or an ingress controller (NGINX/Envoy) already handle your traffic. | avoid_when: ⏎   - Cloud-native load balancers or an ingress controller (NGINX/Envoy) already handle your traffic. ⏎   - "You assume HAProxy core is the separate Kubernetes ingress-controller project." ⏎   - "You need a single SPDX conclusion without verifying GPL, LGPL header, and OpenSSL exceptions for a specific version." |
| `repository_archived` | (absent) | repository_archived: false |
| `status` | status: needs-review | status: "needs-review" |
| `verified_on` | verified_on: '2026-08-03' | verified_on: "2026-10-25" |
| `sources` | sources: ⏎   - legacy:4_Kubernetes-Containers/README.md#L90 ⏎   - legacy:devopstools_final.md#L560 | sources: ⏎   - legacy:4_Kubernetes-Containers/README.md#L90 ⏎   - legacy:devopstools_final.md#L560 ⏎   - https://github.com/haproxy/haproxy/blob/master/LICENSE ⏎   - https://github.com/haproxy/haproxy/blob/master/README.md |

#### `kgateway` — CLEAR

| Canonical field | Before | After |
|---|---|---|
| `summary` | summary: Kubernetes gateway networking. | summary: "Envoy-based Kubernetes Gateway API control plane for routing applications and API traffic." |
| `avoid_when` | avoid_when: ⏎   - Your existing ingress controller already supports Gateway API. | avoid_when: ⏎   - Your existing ingress controller already supports Gateway API. ⏎   - "You require unsupported Gateway API extensions or assume v2.5 prereleases have stable-series support." |
| `repository_archived` | (absent) | repository_archived: false |
| `license_spdx` | (absent) | license_spdx: "Apache-2.0" |
| `status` | status: needs-review | status: "active" |
| `verified_on` | verified_on: '2026-08-03' | verified_on: "2026-10-25" |
| `sources` | sources: ⏎   - legacy:4_Kubernetes-Containers/README.md#L109 ⏎   - legacy:devopstools_final.md#L585 | sources: ⏎   - legacy:4_Kubernetes-Containers/README.md#L109 ⏎   - legacy:devopstools_final.md#L585 ⏎   - https://github.com/kgateway-dev/kgateway/blob/v2.4.7/LICENSE ⏎   - https://github.com/kgateway-dev/kgateway/releases/tag/v2.4.7 ⏎   - https://kgateway.dev/docs/envoy/latest/reference/versions/ |
| `needs_review` | needs_review: true | needs_review: false |

#### `kube-ovn` — CLEAR

| Canonical field | Before | After |
|---|---|---|
| `summary` | summary: CloudNative Network for KubeVirt and Multi-Tenancy. | summary: "OVN and Open vSwitch-based Kubernetes CNI supporting VPCs, overlays, underlays, and KubeVirt networking." |
| `avoid_when` | avoid_when: ⏎   - A simpler CNI (Calico/Flannel/Cilium) provides sufficient network policy and performance. | avoid_when: ⏎   - A simpler CNI (Calico/Flannel/Cilium) provides sufficient network policy and performance. ⏎   - "You need a minimal pod network without the operational complexity of OVN and OVS." |
| `repository_archived` | (absent) | repository_archived: false |
| `license_spdx` | (absent) | license_spdx: "Apache-2.0" |
| `status` | status: needs-review | status: "active" |
| `verified_on` | verified_on: '2026-08-03' | verified_on: "2026-10-25" |
| `sources` | sources: ⏎   - legacy:4_Kubernetes-Containers/README.md#L117 ⏎   - legacy:devopstools_final.md#L596 | sources: ⏎   - legacy:4_Kubernetes-Containers/README.md#L117 ⏎   - legacy:devopstools_final.md#L596 ⏎   - https://github.com/kubeovn/kube-ovn/blob/v1.16.15/LICENSE ⏎   - https://github.com/kubeovn/kube-ovn/blob/v1.16.15/README.md ⏎   - https://github.com/kubeovn/kube-ovn/releases/tag/v1.16.15 |
| `needs_review` | needs_review: true | needs_review: false |

#### `multus-cni` — CLEAR

| Canonical field | Before | After |
|---|---|---|
| `summary` | summary: CNI meta-plugin for attaching multiple network interfaces to Kubernetes pods. | summary: "Kubernetes CNI meta-plugin that delegates to other CNIs to attach multiple network interfaces to pods." |
| `use_when` | use_when: [] | use_when: ⏎   - "Your Kubernetes workloads require multiple network attachments through delegated CNI plugins." |
| `avoid_when` | avoid_when: [] | avoid_when: ⏎   - "You need a standalone primary pod network; Multus requires a pre-existing default CNI." |
| `repository_archived` | (absent) | repository_archived: false |
| `license_spdx` | (absent) | license_spdx: "Apache-2.0" |
| `status` | status: needs-review | status: "active" |
| `verified_on` | verified_on: '2026-08-03' | verified_on: "2026-10-25" |
| `sources` | sources: ⏎   - legacy:devopstools_final.md#L608 | sources: ⏎   - legacy:devopstools_final.md#L608 ⏎   - https://github.com/k8snetworkplumbingwg/multus-cni/blob/v4.3.1/LICENSE ⏎   - https://github.com/k8snetworkplumbingwg/multus-cni/blob/v4.3.1/README.md ⏎   - https://github.com/k8snetworkplumbingwg/multus-cni/releases/tag/v4.3.1 |
| `needs_review` | needs_review: true | needs_review: false |

#### `nginx-gateway-fabric` — CLEAR

| Canonical field | Before | After |
|---|---|---|
| `summary` | summary: NGINX-powered implementation of the Kubernetes Gateway API for managing north-south traffic. | summary: "Kubernetes Gateway API controller using NGINX as data plane for HTTP, gRPC, and supported TCP/UDP traffic." |
| `documentation_url` | (absent) | documentation_url: "https://docs.nginx.com/nginx-gateway-fabric/" |
| `use_when` | use_when: [] | use_when: ⏎   - "You want Gateway API routing backed by NGINX with a published version compatibility matrix." |
| `avoid_when` | avoid_when: [] | avoid_when: ⏎   - "You require Ingress NGINX behavior or Gateway API features listed as unsupported in its compatibility matrix." |
| `repository_archived` | (absent) | repository_archived: false |
| `license_spdx` | (absent) | license_spdx: "Apache-2.0" |
| `status` | status: needs-review | status: "active" |
| `verified_on` | verified_on: '2026-08-03' | verified_on: "2026-10-25" |
| `sources` | sources: ⏎   - legacy:devopstools_final.md#L612 | sources: ⏎   - legacy:devopstools_final.md#L612 ⏎   - https://github.com/nginx/nginx-gateway-fabric/blob/v2.8.0/LICENSE ⏎   - https://github.com/nginx/nginx-gateway-fabric/blob/v2.8.0/README.md ⏎   - https://github.com/nginx/nginx-gateway-fabric/releases/tag/v2.8.0 ⏎   - https://docs.nginx.com/nginx-gateway-fabric/overview/technical-specifications/ ⏎   - https://docs.nginx.com/nginx-gateway-fabric/overview/gateway-api-compatibility/ |
| `needs_review` | needs_review: true | needs_review: false |

#### `ovn-kubernetes` — CLEAR

| Canonical field | Before | After |
|---|---|---|
| `summary` | summary: Networking for Kubernetes using OVN. | summary: "Kubernetes network plugin based on OVN and Open vSwitch; a separate project from Kube-OVN." |
| `repository_url` | repository_url: https://github.com/ovn-org/ovn-kubernetes | repository_url: "https://github.com/ovn-kubernetes/ovn-kubernetes" |
| `avoid_when` | avoid_when: ⏎   - Simpler CNI plugins provide adequate performance and policy enforcement. | avoid_when: ⏎   - Simpler CNI plugins provide adequate performance and policy enforcement. ⏎   - "You assume the separate Kube-OVN project or every Kubernetes distribution shares this implementation's support matrix." |
| `repository_archived` | (absent) | repository_archived: false |
| `license_spdx` | (absent) | license_spdx: "Apache-2.0" |
| `status` | status: needs-review | status: "active" |
| `verified_on` | verified_on: '2026-08-03' | verified_on: "2026-10-25" |
| `sources` | sources: ⏎   - legacy:4_Kubernetes-Containers/README.md#L128 ⏎   - legacy:devopstools_final.md#L618 | sources: ⏎   - legacy:4_Kubernetes-Containers/README.md#L128 ⏎   - legacy:devopstools_final.md#L618 ⏎   - https://github.com/ovn-kubernetes/ovn-kubernetes/blob/v1.4.0/LICENSE ⏎   - https://github.com/ovn-kubernetes/ovn-kubernetes/blob/v1.4.0/README.md ⏎   - https://github.com/ovn-kubernetes/ovn-kubernetes/releases/tag/v1.4.0 |
| `needs_review` | needs_review: true | needs_review: false |

#### `project-contour` — CLEAR

| Canonical field | Before | After |
|---|---|---|
| `summary` | summary: Envoy-powered Kubernetes ingress controller with the HTTPProxy API, dynamic reconfiguration, ⏎     and secure multi-team delegation. | summary: "Envoy-powered Kubernetes ingress controller supporting Ingress, HTTPProxy and Gateway API resources." |
| `documentation_url` | (absent) | documentation_url: "https://projectcontour.io/docs" |
| `use_when` | use_when: [] | use_when: ⏎   - "You need an Envoy-backed ingress controller with HTTPProxy delegation and documented support matrices." |
| `avoid_when` | avoid_when: [] | avoid_when: ⏎   - "You require Gateway API features beyond its documented support or an untested Kubernetes and Envoy combination." |
| `repository_archived` | (absent) | repository_archived: false |
| `license_spdx` | (absent) | license_spdx: "Apache-2.0" |
| `status` | status: needs-review | status: "active" |
| `verified_on` | verified_on: '2026-08-03' | verified_on: "2026-10-25" |
| `sources` | sources: ⏎   - legacy:devopstools_final.md#L620 | sources: ⏎   - legacy:devopstools_final.md#L620 ⏎   - https://github.com/projectcontour/contour/blob/v1.33.7/LICENSE ⏎   - https://github.com/projectcontour/contour/blob/v1.33.7/README.md ⏎   - https://github.com/projectcontour/contour/releases/tag/v1.33.7 ⏎   - https://projectcontour.io/resources/compatibility-matrix/ |
| `needs_review` | needs_review: true | needs_review: false |

### Current verification checkpoint and merge gate — 2026-10-25

**Canonical scope verified:** one YAML file (`data/tools/kubernetes-networking-storage-addons.yaml`), exactly the ten selected record IDs; 132 records and their ordering preserved. Seven records switched to `status: active` with `needs_review: false`; three remain `status: needs-review` with `needs_review: true`. Legacy sources and taxonomy remained intact, and all non-cohort records were unchanged. The six reviewed historical link baseline exceptions were preserved (blob SHA `a834e2af711693def40078a55e31dfeb29bee2c7`).

**Observed generated inventory on validated PR head `950760335268129fae33b79cc84078e7db572705`: 1,425 canonical records; 792 active; 619 needs-review; 30 categories.** This is a verified value, no longer a predicted figure.

The official generator `python -m scripts.generate_docs` was executed locally and its `--check` subsequently passed. Local `python -m scripts.validate_catalog`, Ruff lint/format, full pytest (8 skipped), `python -m pip check` and `git diff --check` passed. The local Windows Python 3.12 `--verify-locked` check reported **one extra platform package, `colorama`**, but no wrong or missing locked package versions; this is recorded as a platform-specific observation, **not** a change to or exemption from the lock file. Linux CI performed its own mandatory strict `--verify-locked` with a clean environment and passed. No Python constraints file was changed.

On that exact pre-documentation-correction commit `950760335268129fae33b79cc84078e7db572705`, **all PR quality/security gates PASSED**:

- [Catalogue quality #382](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40214453239): success, including locked dependency verification, pytest, documentation and catalogue validation.
- [Secret scan #210](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40214453220): success.
- [Plumber CI/CD Security #175](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40214453305): success.
- [CodeQL #219](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40214451796): success, Python and GitHub Actions.

**Independent-review limitation:** `@codex review` requested on PR #140 for `9507603` was **not completed** because Codex returned its usage-limit error; the bot failure is not an actionable code-review finding, and it must not be misrepresented as a successful P1/P2 review. Arrange a different independent maintainer/Work review or retry when quota permits. All substantive P1/P2 findings must be addressed with exact-SHA revalidation.

**Mandatory final-head gates remain pending:** this documentation-only checkpoint produces a **new SHA**, so confirm the four PR CI workflows on that new SHA and review its diff; then obtain an independent review and manually run a **fresh Full link audit** against that **same final SHA**. Require `strict_result: PASS`, `blocking_new: 0`, and all **six historical reviewed URL/classification pairs unchanged**. [Audit #37](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40198833224) belongs to Wave 23 and is **not** a Wave 24 full-audit pass.

Keep [PR #140](https://github.com/goozcena-gnl/devops-tools-catalog/pull/140) **Draft/unmerged** pending the review, fresh audit and human approval. Do not enable auto-merge, publish a release/tag, change historical URL baseline, or close [#139](https://github.com/goozcena-gnl/devops-tools-catalog/issues/139) or [#2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2). Close #139 only after an explicit human merge and successful post-merge checks on the new `main`.
