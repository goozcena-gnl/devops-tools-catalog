# Evidence review Wave 10 — Kubernetes networking, autoscaling and cluster services — 2026-10-08

Exactly the fixed ten existing records were individually reviewed across all 24 material fields. Each receives **CLEAR REVIEW** based on primary evidence. Stable IDs and historical provenance remain. Canonical YAML is authoritative; all generated pages were regenerated.

Execution and selected verified_on date: **2026-10-08, Europe/Paris**.

## Verified baseline and scope

- Expected and verified main: `79a45f4964ba671a2815529cfdd06fbbbb193652` (post-Wave-9).
- Branch: `maintenance/wave-10-kubernetes-services-evidence-review`.
- Before editing: clean tree, zero open PRs; five exact-main checks completed successfully: Analyze (actions), Analyze (python), Plumber audit, validate and gitleaks.
- Issue #2 read-only baseline: Wave 9 COMPLETED; Wave 10 NOT STARTED — READY TO SCOPE. Body and updated_at 2026-10-07T23:05:34Z saved for comparison.
- All initial counters and ten expected names/URLs/flags matched the request; no discrepancy found.
- No unrelated record or Wave 4–9 revisit, link baseline, committed audit output, ledger, workflow, CodeQL configuration or Python constraint changes. Wave 11 not started; no merge or release.

The cohort covers mesh, cluster DNS, external DNS automation, application gateways, bare-metal LoadBalancer Services, distributed block storage, resource metrics, autoscaling components, node provisioning and event-driven workload scaling.

| Rank | ID | Initial name | Initial category | Initial debt |
|---:|---|---|---|---|
| 1 | `istio` | Istio | `kubernetes-networking-storage-addons` | needs-review; unknown maturity; missing documentation; no SPDX |
| 2 | `coredns` | CoreDNS | `kubernetes-networking-storage-addons` | needs-review; unknown maturity; missing documentation; no SPDX |
| 3 | `metallb` | MetalLB | `kubernetes-networking-storage-addons` | needs-review; unknown maturity; missing documentation; no SPDX |
| 4 | `externaldns` | ExternalDNS | `kubernetes-networking-storage-addons` | needs-review; unknown maturity; missing documentation; no SPDX |
| 5 | `envoy-gateway` | Envoy Gateway | `kubernetes-networking-storage-addons` | needs-review; unknown maturity; missing documentation; no SPDX |
| 6 | `longhorn` | Longhorn | `kubernetes-networking-storage-addons` | needs-review; unknown maturity; missing documentation; no SPDX |
| 7 | `metrics-server` | Metrics Server | `kubernetes-networking-storage-addons` | needs-review; unknown maturity; missing documentation; no SPDX; missing official URL |
| 8 | `kubernetes-autoscaler` | Kubernetes Autoscaler | `kubernetes-networking-storage-addons` | needs-review; unknown maturity; missing documentation; no SPDX; missing official URL |
| 9 | `karpenter` | Karpenter | `kubernetes-networking-storage-addons` | needs-review; unknown maturity; missing documentation; no SPDX |
| 10 | `keda` | KEDA | `kubernetes-networking-storage-addons` | needs-review; unknown maturity; missing documentation; no SPDX |

## Evidence method and cross-record boundaries

Primary repositories/READMEs and actual LICENSE files were read directly through GitHub, alongside current official documentation, SIG inventories, project governance, CNCF project records, repository metadata and release feeds. Search snippets, stars and third-party summaries were not evidence. All ten canonical repositories were independently non-archived; release/maintenance evidence supports active status. Source-only URLs were read separately from the link audit.

Catalogue maturity is an editorial classification supported by documented operations, maintained releases and governance, not an automatic translation of foundation levels. Istio, CoreDNS and KEDA are currently CNCF Graduated; Longhorn is Incubating. MetalLB explicitly remains beta and maps to growing. Envoy Gateway is assessed independently of Envoy Proxy; the autoscaler umbrella does not assert every component is GA.

Each project/repository has its own directly read Apache-2.0 licence file. Kubernetes Autoscaler’s root grant covers that repository software, not every autoscaling mechanism; Karpenter’s core grant does not establish provider/service terms. Longhorn’s project and CSI-manager grants do not inherit Rancher commercial packaging. Optional commercial_offering remains absent; absence is not a claim that no commercial ecosystem exists.

Explicit distinctions: CoreDNS serves DNS; ExternalDNS reconciles provider records. Istio manages a mesh; Envoy Gateway manages an application-gateway dataplane; Envoy Proxy executes traffic handling; Gateway API is the standard. Metrics Server serves current resource metrics, distinct from Prometheus, kube-state-metrics and cAdvisor. KEDA scales event-driven workloads; Cluster Autoscaler adjusts nodes; Karpenter provisions nodes using provider implementations. MetalLB implements LoadBalancer Services, not ingress/mesh/CNI. Longhorn implements block storage with separate file-sharing support, not Rook/Ceph or an object store. The autoscaler repository does not own every Kubernetes autoscaling feature. These are scope distinctions, not rankings.

## Decisions and complete material-field review

### istio

**Identity boundary:** Istio is the service-mesh project, with Istiod managing its data plane. Sidecar uses Envoy alongside workloads; ambient uses node-level ztunnel and optional L7 waypoint proxies. These are modes of Istio, not separate canonical identities. Envoy Proxy, Envoy Gateway, Gateway API and vendor-managed meshes remain separate.

**Licence boundary:** Retain oss and add Apache-2.0 from the directly read istio/istio/LICENSE grant. This describes project/repository software; third-party dependencies, separate providers and vendor services keep their own terms.

**Execution/deployment and commercial boundary:** Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred.

**Repository boundary:** Retain verified istio/istio canonical project repository; documented related components remain separate.

**Governance:** CNCF records Istio as Graduated since 2023-07-12. The community repository links technical oversight, steering and working-group governance. No Envoy governance or foundation maturity is inherited.

**Maturity:** Established is an editorial assessment from maintained releases, documented production modes and project governance. Mode-specific feature limits remain; graduation does not establish every feature's stability.

**Lifecycle:** GitHub API reports archived=false; maintained release feed independently supports active lifecycle. Checked repository metadata and release history. No HTTP result or foundation status alone determines lifecycle.

**Unresolved questions / limits:** None blocking identity/licence. Ambient L7 features require suitable waypoints; mode and feature compatibility must be checked for the chosen release.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and identity][istio-e1], [Project software licence][istio-e2], [Maintained release history][istio-e3], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5], [Project governance][istio-e6], [Current CNCF foundation status][istio-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | istio | istio | [Canonical repository and identity][istio-e1] | Preserve existing stable ID; no split, duplicate or substitution. |
| `name` | Istio | Istio | [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5] | Reviewed; retained: documented capability and scoped identity; the boundaries above apply. |
| `summary` | Service mesh for managing microservices traffic. | Service mesh with an Istiod control plane and sidecar or ambient data planes for service traffic, security and telemetry; distinct from Envoy Proxy, Envoy Gateway and the Gateway API specification. | [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5] | Changed: documented capability and scoped identity; the boundaries above apply. |
| `official_url` | https://istio.io | https://istio.io | [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5] | Reviewed; retained: upstream-declared entry point for this identity. Former pointers remain in sources where changed. |
| `repository_url` | https://github.com/istio/istio | https://github.com/istio/istio | [Canonical repository and identity][istio-e1] | Retain directly verified canonical project/repository identity; do not inherit a different component identity. |
| `documentation_url` | *absent* | https://istio.io/latest/docs/overview/what-is-istio/ | [Official documentation and service-mesh scope][istio-e4] | Add directly checked official documentation at the record boundary; parent/umbrella README used where component guides would misrepresent scope. |
| `categories` | kubernetes-networking-storage-addons | kubernetes-networking-storage-addons | [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `subcategories` | Service Mesh | Service Mesh | [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `use_when` | You need advanced traffic management, mTLS, and observability at scale. | You need service-to-service traffic policies, mutual TLS and mesh telemetry, with sidecar or ambient mode selected for the documented workload and feature requirements. | [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `avoid_when` | For small clusters where the complexity and resource overhead aren&#x27;t justified. | You need only an application gateway or expect ambient and sidecar modes to have identical capabilities without checking waypoint and feature requirements. | [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `deployment_models` | `[]` | self-hosted | [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5] | Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred. |
| `license_model` | oss | oss | [Project software licence][istio-e2] | Reviewed; retained: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `license_spdx` | *absent* | Apache-2.0 | [Project software licence][istio-e2] | Changed: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `commercial_offering` | *absent* | *absent* | [Canonical repository and identity][istio-e1] | Leave optional field absent; this software review does not deny or infer third-party commercial offerings. |
| `maturity` | unknown | established | [Maintained release history][istio-e3], [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5], [Project governance][istio-e6], [Current CNCF foundation status][istio-e7] | Established is an editorial assessment from maintained releases, documented production modes and project governance. Mode-specific feature limits remain; graduation does not establish every feature's stability. |
| `status` | needs-review | active | [Maintained release history][istio-e3], [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5], [Project governance][istio-e6], [Current CNCF foundation status][istio-e7] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |
| `repository_archived` | *absent* | `false` | [Canonical repository and identity][istio-e1], [Maintained release history][istio-e3] | GitHub API independently reports archived=false; active status is separately supported by maintained releases. |
| `alternatives` | `[]` | `[]` | [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `tags` | `[]` | `[]` | [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `verified_on` | 2026-08-03 | 2026-10-08 | [Canonical repository and identity][istio-e1], [Project software licence][istio-e2], [Maintained release history][istio-e3], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5], [Project governance][istio-e6], [Current CNCF foundation status][istio-e7] | Actual execution date 2026-10-08, changed only for the fixed ten records. |
| `sources` | legacy:6_Security/README.md#L121<br>legacy:devopstools_final.md#L1016 | legacy:6_Security/README.md#L121<br>legacy:devopstools_final.md#L1016<br>https://github.com/istio/istio<br>https://github.com/istio/istio/blob/master/LICENSE<br>https://github.com/istio/istio/releases<br>https://istio.io/latest/docs/overview/what-is-istio/<br>https://istio.io/latest/docs/overview/dataplane-modes/<br>https://github.com/istio/community/blob/master/README.md<br>https://www.cncf.io/projects/istio/ | [Canonical repository and identity][istio-e1], [Project software licence][istio-e2], [Maintained release history][istio-e3], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5], [Project governance][istio-e6], [Current CNCF foundation status][istio-e7] | Preserve every historical source and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][istio-e3], [Canonical repository and identity][istio-e1], [Official documentation and service-mesh scope][istio-e4], [Official sidecar and ambient documentation][istio-e5], [Project governance][istio-e6], [Current CNCF foundation status][istio-e7] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |

**Changed fields:** `summary`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[istio-e1]: https://github.com/istio/istio
[istio-e2]: https://github.com/istio/istio/blob/master/LICENSE
[istio-e3]: https://github.com/istio/istio/releases
[istio-e4]: https://istio.io/latest/docs/overview/what-is-istio/
[istio-e5]: https://istio.io/latest/docs/overview/dataplane-modes/
[istio-e6]: https://github.com/istio/community/blob/master/README.md
[istio-e7]: https://www.cncf.io/projects/istio/

Archival metadata independently checked: [GitHub repository API](https://api.github.com/repos/istio/istio), archived=false.

### coredns

**Identity boundary:** CoreDNS is independently maintained DNS server/forwarder software built around plugins. Its Kubernetes plugin provides cluster service discovery. It is not Kubernetes itself, the older kube-dns implementation, ExternalDNS or a managed DNS provider; it can also serve DNS outside Kubernetes.

**Licence boundary:** Retain oss and add Apache-2.0 from the directly read coredns/coredns/LICENSE grant. This describes project/repository software; third-party dependencies, separate providers and vendor services keep their own terms.

**Execution/deployment and commercial boundary:** Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred.

**Repository boundary:** Retain verified coredns/coredns canonical project repository; documented related components remain separate.

**Governance:** CNCF records CoreDNS as Graduated since 2019-01-24. Its own governance defines a maintainer-elected steering committee and consensus decisions.

**Maturity:** Established follows maintained release history, documented DNS operations and Kubernetes cluster integration, with explicit project governance. Old manual example versions are not current support claims.

**Lifecycle:** GitHub API reports archived=false; maintained release feed independently supports active lifecycle. Checked repository metadata and release history. No HTTP result or foundation status alone determines lifecycle.

**Unresolved questions / limits:** None blocking identity/licence. Actual DNS functions depend on enabled plugins and configuration; no managed-provider entitlement is asserted.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and identity][coredns-e1], [Project software licence][coredns-e2], [Maintained release history][coredns-e3], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5], [Project governance][coredns-e6], [Current CNCF foundation status][coredns-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | coredns | coredns | [Canonical repository and identity][coredns-e1] | Preserve existing stable ID; no split, duplicate or substitution. |
| `name` | CoreDNS | CoreDNS | [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5] | Reviewed; retained: documented capability and scoped identity; the boundaries above apply. |
| `summary` | Flexible, plugin-based DNS server used as the default cluster DNS in Kubernetes. | Plugin-based DNS server and forwarder used for Kubernetes cluster service discovery through its Kubernetes plugin; separate from kube-dns and ExternalDNS record automation. | [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5] | Changed: documented capability and scoped identity; the boundaries above apply. |
| `official_url` | https://coredns.io | https://coredns.io | [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5] | Reviewed; retained: upstream-declared entry point for this identity. Former pointers remain in sources where changed. |
| `repository_url` | https://github.com/coredns/coredns | https://github.com/coredns/coredns | [Canonical repository and identity][coredns-e1] | Retain directly verified canonical project/repository identity; do not inherit a different component identity. |
| `documentation_url` | *absent* | https://coredns.io/manual/toc/ | [Official DNS-server documentation][coredns-e4] | Add directly checked official documentation at the record boundary; parent/umbrella README used where component guides would misrepresent scope. |
| `categories` | kubernetes-networking-storage-addons | kubernetes-networking-storage-addons | [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `subcategories` | Kubernetes Ecosystem &amp; Add-ons | Cluster DNS | [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5] | Changed: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `use_when` | `[]` | You need a configurable DNS server for Kubernetes service discovery or DNS serving and forwarding with the appropriate CoreDNS plugins. | [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `avoid_when` | `[]` | You need a controller that publishes Kubernetes resource addresses into an external DNS provider rather than a DNS server. | [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `deployment_models` | `[]` | self-hosted | [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5] | Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred. |
| `license_model` | oss | oss | [Project software licence][coredns-e2] | Reviewed; retained: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `license_spdx` | *absent* | Apache-2.0 | [Project software licence][coredns-e2] | Changed: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `commercial_offering` | *absent* | *absent* | [Canonical repository and identity][coredns-e1] | Leave optional field absent; this software review does not deny or infer third-party commercial offerings. |
| `maturity` | unknown | established | [Maintained release history][coredns-e3], [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5], [Project governance][coredns-e6], [Current CNCF foundation status][coredns-e7] | Established follows maintained release history, documented DNS operations and Kubernetes cluster integration, with explicit project governance. Old manual example versions are not current support claims. |
| `status` | needs-review | active | [Maintained release history][coredns-e3], [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5], [Project governance][coredns-e6], [Current CNCF foundation status][coredns-e7] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |
| `repository_archived` | *absent* | `false` | [Canonical repository and identity][coredns-e1], [Maintained release history][coredns-e3] | GitHub API independently reports archived=false; active status is separately supported by maintained releases. |
| `alternatives` | `[]` | `[]` | [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `tags` | `[]` | `[]` | [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `verified_on` | 2026-08-03 | 2026-10-08 | [Canonical repository and identity][coredns-e1], [Project software licence][coredns-e2], [Maintained release history][coredns-e3], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5], [Project governance][coredns-e6], [Current CNCF foundation status][coredns-e7] | Actual execution date 2026-10-08, changed only for the fixed ten records. |
| `sources` | legacy:devopstools_final.md#L545 | legacy:devopstools_final.md#L545<br>https://github.com/coredns/coredns<br>https://github.com/coredns/coredns/blob/master/LICENSE<br>https://github.com/coredns/coredns/releases<br>https://coredns.io/manual/toc/<br>https://kubernetes.io/docs/tasks/administer-cluster/coredns/<br>https://github.com/coredns/coredns/blob/master/GOVERNANCE.md<br>https://www.cncf.io/projects/coredns/ | [Canonical repository and identity][coredns-e1], [Project software licence][coredns-e2], [Maintained release history][coredns-e3], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5], [Project governance][coredns-e6], [Current CNCF foundation status][coredns-e7] | Preserve every historical source and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][coredns-e3], [Canonical repository and identity][coredns-e1], [Official DNS-server documentation][coredns-e4], [Kubernetes cluster DNS documentation][coredns-e5], [Project governance][coredns-e6], [Current CNCF foundation status][coredns-e7] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[coredns-e1]: https://github.com/coredns/coredns
[coredns-e2]: https://github.com/coredns/coredns/blob/master/LICENSE
[coredns-e3]: https://github.com/coredns/coredns/releases
[coredns-e4]: https://coredns.io/manual/toc/
[coredns-e5]: https://kubernetes.io/docs/tasks/administer-cluster/coredns/
[coredns-e6]: https://github.com/coredns/coredns/blob/master/GOVERNANCE.md
[coredns-e7]: https://www.cncf.io/projects/coredns/

Archival metadata independently checked: [GitHub repository API](https://api.github.com/repos/coredns/coredns), archived=false.

### metallb

**Identity boundary:** MetalLB implements Kubernetes LoadBalancer Services: address allocation plus L2/BGP announcement. kube-proxy or the cluster's service datapath handles delivery after packets reach a node. It is not a cloud-provider LB service, HTTP ingress controller, CNI or service mesh. Router/mode limitations prevent an all-BGP-implementations compatibility promise.

**Licence boundary:** Retain oss and add Apache-2.0 from the directly read metallb/metallb/LICENSE grant. This describes project/repository software; third-party dependencies, separate providers and vendor services keep their own terms.

**Execution/deployment and commercial boundary:** Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred.

**Repository boundary:** Retain metallb/metallb. Replace the historical universe.tf official entry with metallb.io because the current README explicitly designates that project site, not merely because a URL redirects; preserve the old entry in sources.

**Governance:** The repository CODEOWNERS explicitly identifies the MetalLB maintainers team. No unsupported CNCF level or vendor ownership claim is added.

**Maturity:** Growing preserves the upstream's explicit beta qualification despite documented production adoption and maintained releases. This is the catalogue's editorial mapping, not a claim that beta means unstable or that all features are GA.

**Lifecycle:** GitHub API reports archived=false; maintained release feed independently supports active lifecycle. Checked repository metadata and release history. No HTTP result or foundation status alone determines lifecycle.

**Unresolved questions / limits:** None blocking identity/licence. Upstream beta status, L2/BGP mode limits and router compatibility remain operational qualifications.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and identity][metallb-e1], [Project software licence][metallb-e2], [Maintained release history][metallb-e3], [Official documentation and LoadBalancer scope][metallb-e4], [Official BGP operations and limitations][metallb-e5], [Official project maturity][metallb-e6], [Project maintainers][metallb-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | metallb | metallb | [Canonical repository and identity][metallb-e1] | Preserve existing stable ID; no split, duplicate or substitution. |
| `name` | MetalLB | MetalLB | [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4] | Reviewed; retained: documented capability and scoped identity; the boundaries above apply. |
| `summary` | Load balancer implementation for bare metal. | Kubernetes LoadBalancer-service implementation for bare-metal clusters that allocates service IPs and advertises them through Layer 2 or BGP; separate from ingress controllers, CNIs and service meshes. | [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4] | Changed: documented capability and scoped identity; the boundaries above apply. |
| `official_url` | https://metallb.universe.tf | https://metallb.io | [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4] | Changed: upstream-declared entry point for this identity. Former pointers remain in sources where changed. |
| `repository_url` | https://github.com/metallb/metallb | https://github.com/metallb/metallb | [Canonical repository and identity][metallb-e1] | Retain directly verified canonical project/repository identity; do not inherit a different component identity. |
| `documentation_url` | *absent* | https://metallb.io/concepts/ | [Official documentation and LoadBalancer scope][metallb-e4] | Add directly checked official documentation at the record boundary; parent/umbrella README used where component guides would misrepresent scope. |
| `categories` | kubernetes-networking-storage-addons | kubernetes-networking-storage-addons | [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `subcategories` | Kubernetes Ecosystem &amp; Add-ons | LoadBalancer services | [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4] | Changed: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `use_when` | You run Kubernetes on bare metal and need LoadBalancer-type services. | You need external IP allocation and Layer 2 or BGP advertisement for Kubernetes LoadBalancer Services on networks you control. | [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `avoid_when` | You&#x27;re on a cloud provider with native load balancer integration. | You need HTTP ingress routing, a service mesh or a CNI, or cannot meet the documented network, router and BGP-mode requirements. | [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `deployment_models` | `[]` | self-hosted | [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4] | Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred. |
| `license_model` | oss | oss | [Project software licence][metallb-e2] | Reviewed; retained: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `license_spdx` | *absent* | Apache-2.0 | [Project software licence][metallb-e2] | Changed: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `commercial_offering` | *absent* | *absent* | [Canonical repository and identity][metallb-e1] | Leave optional field absent; this software review does not deny or infer third-party commercial offerings. |
| `maturity` | unknown | growing | [Maintained release history][metallb-e3], [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4], [Official project maturity][metallb-e6], [Project maintainers][metallb-e7] | Growing preserves the upstream's explicit beta qualification despite documented production adoption and maintained releases. This is the catalogue's editorial mapping, not a claim that beta means unstable or that all features are GA. |
| `status` | needs-review | active | [Maintained release history][metallb-e3], [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4], [Official project maturity][metallb-e6], [Project maintainers][metallb-e7] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |
| `repository_archived` | *absent* | `false` | [Canonical repository and identity][metallb-e1], [Maintained release history][metallb-e3] | GitHub API independently reports archived=false; active status is separately supported by maintained releases. |
| `alternatives` | `[]` | `[]` | [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `tags` | `[]` | `[]` | [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `verified_on` | 2026-08-03 | 2026-10-08 | [Canonical repository and identity][metallb-e1], [Project software licence][metallb-e2], [Maintained release history][metallb-e3], [Official documentation and LoadBalancer scope][metallb-e4], [Official BGP operations and limitations][metallb-e5], [Official project maturity][metallb-e6], [Project maintainers][metallb-e7] | Actual execution date 2026-10-08, changed only for the fixed ten records. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L123<br>legacy:devopstools_final.md#L606 | legacy:4_Kubernetes-Containers/README.md#L123<br>legacy:devopstools_final.md#L606<br>https://github.com/metallb/metallb<br>https://github.com/metallb/metallb/blob/main/LICENSE<br>https://github.com/metallb/metallb/releases<br>https://metallb.io/concepts/<br>https://metallb.io/concepts/bgp/<br>https://metallb.io/concepts/maturity/<br>https://github.com/metallb/metallb/blob/main/CODEOWNERS<br>https://metallb.universe.tf | [Canonical repository and identity][metallb-e1], [Project software licence][metallb-e2], [Maintained release history][metallb-e3], [Official documentation and LoadBalancer scope][metallb-e4], [Official BGP operations and limitations][metallb-e5], [Official project maturity][metallb-e6], [Project maintainers][metallb-e7] | Preserve every historical source and append directly checked primary evidence. Preserve former official_url https://metallb.universe.tf as provenance. |
| `needs_review` | `true` | `false` | [Maintained release history][metallb-e3], [Canonical repository and identity][metallb-e1], [Official documentation and LoadBalancer scope][metallb-e4], [Official project maturity][metallb-e6], [Project maintainers][metallb-e7] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |

**Changed fields:** `summary`, `official_url`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[metallb-e1]: https://github.com/metallb/metallb
[metallb-e2]: https://github.com/metallb/metallb/blob/main/LICENSE
[metallb-e3]: https://github.com/metallb/metallb/releases
[metallb-e4]: https://metallb.io/concepts/
[metallb-e5]: https://metallb.io/concepts/bgp/
[metallb-e6]: https://metallb.io/concepts/maturity/
[metallb-e7]: https://github.com/metallb/metallb/blob/main/CODEOWNERS

Archival metadata independently checked: [GitHub repository API](https://api.github.com/repos/metallb/metallb), archived=false.

### externaldns

**Identity boundary:** ExternalDNS watches Kubernetes resources and reconciles DNS records through provider APIs. Current README/docs explicitly say it is not a DNS server. It neither serves CoreDNS queries nor forwards ingress traffic nor provides hosted DNS. Current docs distinguish in-tree integrations from webhook providers; no frozen provider list or universal support promise is added.

**Licence boundary:** Retain oss and add Apache-2.0 from the directly read kubernetes-sigs/external-dns/LICENSE.md grant. This describes project/repository software; third-party dependencies, separate providers and vendor services keep their own terms.

**Execution/deployment and commercial boundary:** Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred.

**Repository boundary:** Retain verified kubernetes-sigs/external-dns canonical project repository; documented related components remain separate.

**Governance:** Kubernetes SIG Network's current subproject inventory names external-dns and its repository ownership. Kubernetes SIG hosting is not a separate CNCF maturity classification.

**Maturity:** Established is an editorial judgement from maintained software/chart releases and documented operational controls, provider setup and governance. Provider-specific support is deliberately not generalized.

**Lifecycle:** GitHub API reports archived=false; maintained release feed independently supports active lifecycle. Checked repository metadata and release history. No HTTP result or foundation status alone determines lifecycle.

**Unresolved questions / limits:** None blocking identity/licence. Provider maturity and webhook maintenance vary; users must read the selected integration's current documentation.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and identity][externaldns-e1], [Project software licence][externaldns-e2], [Maintained release history][externaldns-e3], [Official documentation and provider integration scope][externaldns-e4], [SIG Network governance][externaldns-e5].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | externaldns | externaldns | [Canonical repository and identity][externaldns-e1] | Preserve existing stable ID; no split, duplicate or substitution. |
| `name` | ExternalDNS | ExternalDNS | [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4] | Reviewed; retained: documented capability and scoped identity; the boundaries above apply. |
| `summary` | Kubernetes add-on that configures public DNS servers with information about exposed Kubernetes services. | Kubernetes controller that observes resources such as Services and Ingresses and synchronizes DNS records through configured provider integrations; it is not a DNS server, ingress controller or DNS provider. | [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4] | Changed: documented capability and scoped identity; the boundaries above apply. |
| `official_url` | https://kubernetes-sigs.github.io/external-dns/latest | https://kubernetes-sigs.github.io/external-dns/latest | [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4] | Reviewed; retained: upstream-declared entry point for this identity. Former pointers remain in sources where changed. |
| `repository_url` | https://github.com/kubernetes-sigs/external-dns | https://github.com/kubernetes-sigs/external-dns | [Canonical repository and identity][externaldns-e1] | Retain directly verified canonical project/repository identity; do not inherit a different component identity. |
| `documentation_url` | *absent* | https://kubernetes-sigs.github.io/external-dns/latest/ | [Official documentation and provider integration scope][externaldns-e4] | Add directly checked official documentation at the record boundary; parent/umbrella README used where component guides would misrepresent scope. |
| `categories` | kubernetes-networking-storage-addons | kubernetes-networking-storage-addons | [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `subcategories` | Kubernetes Ecosystem &amp; Add-ons | DNS record automation | [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4] | Changed: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `use_when` | `[]` | You need Kubernetes resource changes to drive DNS record updates through a supported provider integration with appropriate zone filters and record ownership configuration. | [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `avoid_when` | `[]` | You need cluster DNS query serving, an ingress dataplane or a DNS hosting provider, or have not checked the chosen provider&#x27;s documented support and configuration. | [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `deployment_models` | `[]` | self-hosted | [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4] | Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred. |
| `license_model` | oss | oss | [Project software licence][externaldns-e2] | Reviewed; retained: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `license_spdx` | *absent* | Apache-2.0 | [Project software licence][externaldns-e2] | Changed: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `commercial_offering` | *absent* | *absent* | [Canonical repository and identity][externaldns-e1] | Leave optional field absent; this software review does not deny or infer third-party commercial offerings. |
| `maturity` | unknown | established | [Maintained release history][externaldns-e3], [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4], [SIG Network governance][externaldns-e5] | Established is an editorial judgement from maintained software/chart releases and documented operational controls, provider setup and governance. Provider-specific support is deliberately not generalized. |
| `status` | needs-review | active | [Maintained release history][externaldns-e3], [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4], [SIG Network governance][externaldns-e5] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |
| `repository_archived` | *absent* | `false` | [Canonical repository and identity][externaldns-e1], [Maintained release history][externaldns-e3] | GitHub API independently reports archived=false; active status is separately supported by maintained releases. |
| `alternatives` | `[]` | `[]` | [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `tags` | `[]` | `[]` | [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `verified_on` | 2026-08-03 | 2026-10-08 | [Canonical repository and identity][externaldns-e1], [Project software licence][externaldns-e2], [Maintained release history][externaldns-e3], [Official documentation and provider integration scope][externaldns-e4], [SIG Network governance][externaldns-e5] | Actual execution date 2026-10-08, changed only for the fixed ten records. |
| `sources` | legacy:devopstools_final.md#L554 | legacy:devopstools_final.md#L554<br>https://github.com/kubernetes-sigs/external-dns<br>https://github.com/kubernetes-sigs/external-dns/blob/master/LICENSE.md<br>https://github.com/kubernetes-sigs/external-dns/releases<br>https://kubernetes-sigs.github.io/external-dns/latest/<br>https://github.com/kubernetes/community/blob/main/sig-network/README.md | [Canonical repository and identity][externaldns-e1], [Project software licence][externaldns-e2], [Maintained release history][externaldns-e3], [Official documentation and provider integration scope][externaldns-e4], [SIG Network governance][externaldns-e5] | Preserve every historical source and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][externaldns-e3], [Canonical repository and identity][externaldns-e1], [Official documentation and provider integration scope][externaldns-e4], [SIG Network governance][externaldns-e5] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[externaldns-e1]: https://github.com/kubernetes-sigs/external-dns
[externaldns-e2]: https://github.com/kubernetes-sigs/external-dns/blob/master/LICENSE.md
[externaldns-e3]: https://github.com/kubernetes-sigs/external-dns/releases
[externaldns-e4]: https://kubernetes-sigs.github.io/external-dns/latest/
[externaldns-e5]: https://github.com/kubernetes/community/blob/main/sig-network/README.md

Archival metadata independently checked: [GitHub repository API](https://api.github.com/repos/kubernetes-sigs/external-dns), archived=false.

### envoy-gateway

**Identity boundary:** Envoy Gateway is a distinct control-plane/API implementation that dynamically provisions/configures managed Envoy Proxy instances. Request routing, TLS processing and traffic telemetry execute in the Envoy dataplane under that configuration. Gateway API is the upstream API standard, not the implementation; Istio is a service mesh. No identity is collapsed into a generic ingress controller.

**Licence boundary:** Retain oss and add Apache-2.0 from the directly read envoyproxy/gateway/LICENSE grant. This describes project/repository software; third-party dependencies, separate providers and vendor services keep their own terms.

**Execution/deployment and commercial boundary:** Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred.

**Repository boundary:** Retain verified envoyproxy/gateway canonical project repository; documented related components remain separate.

**Governance:** Its own GOVERNANCE.md assigns direction and oversight to the Envoy Gateway steering committee, including an Envoy core-proxy maintainer seat. The document's dated membership roster is not asserted as current individuals; no parent Envoy CNCF graduation is copied into Gateway's maturity.

**Maturity:** Established is independently supported by maintained 1.x releases, documented Kubernetes deployment and an explicit version compatibility matrix and governance charter. No inherited Envoy Proxy maturity is used.

**Lifecycle:** GitHub API reports archived=false; maintained release feed independently supports active lifecycle. Checked repository metadata and release history. No HTTP result or foundation status alone determines lifecycle.

**Unresolved questions / limits:** None blocking identity/licence. Check the release compatibility matrix; the dated governance roster is not evidence of current officeholders.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and identity][envoy-gateway-e1], [Project software licence][envoy-gateway-e2], [Maintained release history][envoy-gateway-e3], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5], [Project governance][envoy-gateway-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | envoy-gateway | envoy-gateway | [Canonical repository and identity][envoy-gateway-e1] | Preserve existing stable ID; no split, duplicate or substitution. |
| `name` | Envoy Gateway | Envoy Gateway | [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5] | Reviewed; retained: documented capability and scoped identity; the boundaries above apply. |
| `summary` | Gateway API implementation for Envoy with traffic management, security, and observability features. | Application-gateway control plane that provisions and configures Envoy Proxy using Kubernetes Gateway API resources; Envoy Proxy supplies the traffic dataplane and Gateway API defines the configuration standard. | [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5] | Changed: documented capability and scoped identity; the boundaries above apply. |
| `official_url` | https://gateway.envoyproxy.io | https://gateway.envoyproxy.io | [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5] | Reviewed; retained: upstream-declared entry point for this identity. Former pointers remain in sources where changed. |
| `repository_url` | https://github.com/envoyproxy/gateway | https://github.com/envoyproxy/gateway | [Canonical repository and identity][envoy-gateway-e1] | Retain directly verified canonical project/repository identity; do not inherit a different component identity. |
| `documentation_url` | *absent* | https://gateway.envoyproxy.io/latest/tasks/quickstart/ | [Official documentation and deployment][envoy-gateway-e4] | Add directly checked official documentation at the record boundary; parent/umbrella README used where component guides would misrepresent scope. |
| `categories` | kubernetes-networking-storage-addons | kubernetes-networking-storage-addons | [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `subcategories` | Kubernetes Ecosystem &amp; Add-ons | Gateway API implementation | [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5] | Changed: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `use_when` | `[]` | You need a Kubernetes Gateway API implementation that manages Envoy Proxy deployments and routing, with compatible Gateway API and Envoy versions. | [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `avoid_when` | `[]` | You need the Gateway API specification alone, a standalone proxy binary or a service mesh rather than an application-gateway control plane. | [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `deployment_models` | `[]` | self-hosted | [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5] | Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred. |
| `license_model` | oss | oss | [Project software licence][envoy-gateway-e2] | Reviewed; retained: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `license_spdx` | *absent* | Apache-2.0 | [Project software licence][envoy-gateway-e2] | Changed: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `commercial_offering` | *absent* | *absent* | [Canonical repository and identity][envoy-gateway-e1] | Leave optional field absent; this software review does not deny or infer third-party commercial offerings. |
| `maturity` | unknown | established | [Maintained release history][envoy-gateway-e3], [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5], [Project governance][envoy-gateway-e6] | Established is independently supported by maintained 1.x releases, documented Kubernetes deployment and an explicit version compatibility matrix and governance charter. No inherited Envoy Proxy maturity is used. |
| `status` | needs-review | active | [Maintained release history][envoy-gateway-e3], [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5], [Project governance][envoy-gateway-e6] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |
| `repository_archived` | *absent* | `false` | [Canonical repository and identity][envoy-gateway-e1], [Maintained release history][envoy-gateway-e3] | GitHub API independently reports archived=false; active status is separately supported by maintained releases. |
| `alternatives` | `[]` | `[]` | [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `tags` | `[]` | `[]` | [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `verified_on` | 2026-08-03 | 2026-10-08 | [Canonical repository and identity][envoy-gateway-e1], [Project software licence][envoy-gateway-e2], [Maintained release history][envoy-gateway-e3], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5], [Project governance][envoy-gateway-e6] | Actual execution date 2026-10-08, changed only for the fixed ten records. |
| `sources` | legacy:devopstools_final.md#L555 | legacy:devopstools_final.md#L555<br>https://github.com/envoyproxy/gateway<br>https://github.com/envoyproxy/gateway/blob/main/LICENSE<br>https://github.com/envoyproxy/gateway/releases<br>https://gateway.envoyproxy.io/latest/tasks/quickstart/<br>https://gateway.envoyproxy.io/news/releases/matrix/<br>https://github.com/envoyproxy/gateway/blob/main/GOVERNANCE.md | [Canonical repository and identity][envoy-gateway-e1], [Project software licence][envoy-gateway-e2], [Maintained release history][envoy-gateway-e3], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5], [Project governance][envoy-gateway-e6] | Preserve every historical source and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][envoy-gateway-e3], [Canonical repository and identity][envoy-gateway-e1], [Official documentation and deployment][envoy-gateway-e4], [Official compatibility and support documentation][envoy-gateway-e5], [Project governance][envoy-gateway-e6] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[envoy-gateway-e1]: https://github.com/envoyproxy/gateway
[envoy-gateway-e2]: https://github.com/envoyproxy/gateway/blob/main/LICENSE
[envoy-gateway-e3]: https://github.com/envoyproxy/gateway/releases
[envoy-gateway-e4]: https://gateway.envoyproxy.io/latest/tasks/quickstart/
[envoy-gateway-e5]: https://gateway.envoyproxy.io/news/releases/matrix/
[envoy-gateway-e6]: https://github.com/envoyproxy/gateway/blob/main/GOVERNANCE.md

Archival metadata independently checked: [GitHub repository API](https://api.github.com/repos/envoyproxy/gateway), archived=false.

### longhorn

**Identity boundary:** Longhorn is its own cloud-native distributed block-storage project. Its main README identifies manager/CSI, engines, replicas and the separate share-manager, which exposes Longhorn block volumes as RWX through NFS. Backup targets such as S3/NFS do not turn Longhorn into a generic object store. It remains distinct from Rook/Ceph and Rancher Manager/Prime; do not erase supported file-sharing behavior while preserving the block-storage foundation.

**Licence boundary:** Retain oss and add Apache-2.0 from the directly read longhorn/longhorn/LICENSE grant. This describes project/repository software; third-party dependencies, separate providers and vendor services keep their own terms.

**Execution/deployment and commercial boundary:** Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred.

**Repository boundary:** Retain verified longhorn/longhorn canonical project repository; documented related components remain separate.

**Governance:** CNCF records Longhorn as Incubating since 2021-11-04. Its governance defines community maintainer responsibilities, consensus decisions and vendor neutrality; current corporate employment does not grant sole project ownership.

**Maturity:** Established is an editorial assessment from supported/stable release history, documented CSI/storage operations and community governance. CNCF Incubating is recorded separately, not equated to the catalogue maturity enum.

**Lifecycle:** GitHub API reports archived=false; maintained release feed independently supports active lifecycle. Checked repository metadata and release history. No HTTP result or foundation status alone determines lifecycle.

**Unresolved questions / limits:** None blocking identity/licence. Volume mode, host prerequisites, backups and feature-specific stability need release-specific assessment; no unsupported IOPS ranking is retained.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and identity][longhorn-e1], [Project software licence][longhorn-e2], [Maintained release history][longhorn-e3], [Official storage documentation][longhorn-e4], [Project governance][longhorn-e5], [Current CNCF foundation status][longhorn-e6], [CSI manager software licence][longhorn-e7].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | longhorn | longhorn | [Canonical repository and identity][longhorn-e1] | Preserve existing stable ID; no split, duplicate or substitution. |
| `name` | Longhorn | Longhorn | [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4] | Reviewed; retained: documented capability and scoped identity; the boundaries above apply. |
| `summary` | Cloud native distributed block storage for Kubernetes. | Distributed block storage for Kubernetes persistent volumes, with replication, snapshots, backups and CSI integration; file-sharing components expose those block volumes and do not make it an object-storage system. | [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4] | Changed: documented capability and scoped identity; the boundaries above apply. |
| `official_url` | https://longhorn.io | https://longhorn.io | [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4] | Reviewed; retained: upstream-declared entry point for this identity. Former pointers remain in sources where changed. |
| `repository_url` | https://github.com/longhorn/longhorn | https://github.com/longhorn/longhorn | [Canonical repository and identity][longhorn-e1] | Retain directly verified canonical project/repository identity; do not inherit a different component identity. |
| `documentation_url` | *absent* | https://longhorn.io/docs/latest/ | [Official storage documentation][longhorn-e4] | Add directly checked official documentation at the record boundary; parent/umbrella README used where component guides would misrepresent scope. |
| `categories` | kubernetes-networking-storage-addons | kubernetes-networking-storage-addons | [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `subcategories` | Storage | Storage | [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `use_when` | You want easy-to-deploy distributed block storage with built-in backup and DR. | You need replicated Kubernetes persistent block volumes with CSI integration, snapshots and documented backup or recovery workflows. | [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `avoid_when` | You need high-IOPS workloads or enterprise-scale storage (consider Ceph/Portworx). | You need an object-store service or assume Longhorn is Rancher Manager, Rancher Prime or Rook/Ceph; assess storage prerequisites and the chosen volume access mode. | [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `deployment_models` | `[]` | self-hosted | [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4] | Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred. |
| `license_model` | oss | oss | [Project software licence][longhorn-e2], [CSI manager software licence][longhorn-e7] | Reviewed; retained: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `license_spdx` | *absent* | Apache-2.0 | [Project software licence][longhorn-e2], [CSI manager software licence][longhorn-e7] | Changed: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `commercial_offering` | *absent* | *absent* | [Canonical repository and identity][longhorn-e1] | Leave optional field absent; this software review does not deny or infer third-party commercial offerings. |
| `maturity` | unknown | established | [Maintained release history][longhorn-e3], [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4], [Project governance][longhorn-e5], [Current CNCF foundation status][longhorn-e6] | Established is an editorial assessment from supported/stable release history, documented CSI/storage operations and community governance. CNCF Incubating is recorded separately, not equated to the catalogue maturity enum. |
| `status` | needs-review | active | [Maintained release history][longhorn-e3], [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4], [Project governance][longhorn-e5], [Current CNCF foundation status][longhorn-e6] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |
| `repository_archived` | *absent* | `false` | [Canonical repository and identity][longhorn-e1], [Maintained release history][longhorn-e3] | GitHub API independently reports archived=false; active status is separately supported by maintained releases. |
| `alternatives` | `[]` | `[]` | [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `tags` | `[]` | `[]` | [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `verified_on` | 2026-08-03 | 2026-10-08 | [Canonical repository and identity][longhorn-e1], [Project software licence][longhorn-e2], [Maintained release history][longhorn-e3], [Official storage documentation][longhorn-e4], [Project governance][longhorn-e5], [Current CNCF foundation status][longhorn-e6], [CSI manager software licence][longhorn-e7] | Actual execution date 2026-10-08, changed only for the fixed ten records. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L173<br>legacy:devopstools_final.md#L677 | legacy:4_Kubernetes-Containers/README.md#L173<br>legacy:devopstools_final.md#L677<br>https://github.com/longhorn/longhorn<br>https://github.com/longhorn/longhorn/blob/master/LICENSE<br>https://github.com/longhorn/longhorn/releases<br>https://longhorn.io/docs/latest/<br>https://github.com/longhorn/longhorn/blob/master/GOVERNANCE.md<br>https://www.cncf.io/projects/longhorn/<br>https://github.com/longhorn/longhorn-manager/blob/master/LICENSE | [Canonical repository and identity][longhorn-e1], [Project software licence][longhorn-e2], [Maintained release history][longhorn-e3], [Official storage documentation][longhorn-e4], [Project governance][longhorn-e5], [Current CNCF foundation status][longhorn-e6], [CSI manager software licence][longhorn-e7] | Preserve every historical source and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][longhorn-e3], [Canonical repository and identity][longhorn-e1], [Official storage documentation][longhorn-e4], [Project governance][longhorn-e5], [Current CNCF foundation status][longhorn-e6] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |

**Changed fields:** `summary`, `documentation_url`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[longhorn-e1]: https://github.com/longhorn/longhorn
[longhorn-e2]: https://github.com/longhorn/longhorn/blob/master/LICENSE
[longhorn-e3]: https://github.com/longhorn/longhorn/releases
[longhorn-e4]: https://longhorn.io/docs/latest/
[longhorn-e5]: https://github.com/longhorn/longhorn/blob/master/GOVERNANCE.md
[longhorn-e6]: https://www.cncf.io/projects/longhorn/
[longhorn-e7]: https://github.com/longhorn/longhorn-manager/blob/master/LICENSE

Archival metadata independently checked: [GitHub repository API](https://api.github.com/repos/longhorn/longhorn), archived=false.

### metrics-server

**Identity boundary:** Metrics Server is the resource-metrics collection/API component, not the Metrics API definitions repository itself. It reads kubelets and serves resource metrics consumed by HPA/VPA and kubectl top. The README cautions against using it as a monitoring source. Prometheus, kube-state-metrics and cAdvisor are separate systems; the in-memory current-metrics cache is not long-term time-series storage.

**Licence boundary:** Retain oss and add Apache-2.0 from the directly read kubernetes-sigs/metrics-server/LICENSE grant. This describes project/repository software; third-party dependencies, separate providers and vendor services keep their own terms.

**Execution/deployment and commercial boundary:** Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred.

**Repository boundary:** Retain the implementation repository and use it as official_url; its README is the authoritative project/installation documentation. Do not substitute the metrics API definition repository or a broad Kubernetes observability page.

**Governance:** The implementation README and current Kubernetes SIG Instrumentation inventory independently identify SIG Instrumentation maintenance.

**Maturity:** Established is supported by maintained releases/chart, documented compatibility and operational requirements, and SIG ownership. Metrics API beta version numbering is not a universal experimental-project judgement.

**Lifecycle:** GitHub API reports archived=false; maintained release feed independently supports active lifecycle. Checked repository metadata and release history. No HTTP result or foundation status alone determines lifecycle.

**Unresolved questions / limits:** None blocking identity/licence. Kubernetes version skew and cluster prerequisites apply; installing Prometheus alone does not supply the same resource Metrics API.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and identity][metrics-server-e1], [Project software licence][metrics-server-e2], [Maintained release history][metrics-server-e3], [Official implementation documentation][metrics-server-e4], [SIG Instrumentation governance][metrics-server-e5].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | metrics-server | metrics-server | [Canonical repository and identity][metrics-server-e1] | Preserve existing stable ID; no split, duplicate or substitution. |
| `name` | Metrics Server | Metrics Server | [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4] | Reviewed; retained: documented capability and scoped identity; the boundaries above apply. |
| `summary` | Resource usage metrics for Kubernetes. | Collects current CPU and memory resource metrics from kubelets and exposes the Kubernetes Metrics API for HPA, VPA and kubectl top; it is not historical time-series storage or a general monitoring platform. | [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4] | Changed: documented capability and scoped identity; the boundaries above apply. |
| `official_url` | *absent* | https://github.com/kubernetes-sigs/metrics-server | [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4] | Changed: upstream-declared entry point for this identity. Former pointers remain in sources where changed. |
| `repository_url` | https://github.com/kubernetes-sigs/metrics-server | https://github.com/kubernetes-sigs/metrics-server | [Canonical repository and identity][metrics-server-e1] | Retain directly verified canonical project/repository identity; do not inherit a different component identity. |
| `documentation_url` | *absent* | https://github.com/kubernetes-sigs/metrics-server/blob/master/README.md | [Official implementation documentation][metrics-server-e4] | Add directly checked official documentation at the record boundary; parent/umbrella README used where component guides would misrepresent scope. |
| `categories` | kubernetes-networking-storage-addons | kubernetes-networking-storage-addons | [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `subcategories` | Kubernetes Ecosystem &amp; Add-ons | Resource metrics | [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4] | Changed: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `use_when` | You need `kubectl top` and HPA/VPA to function—it&#x27;s a baseline requirement. | You need Kubernetes resource metrics for CPU/memory autoscaling consumers or kubectl top and can meet the aggregation-layer, kubelet and network requirements. | [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `avoid_when` | Your managed Kubernetes already includes it or you rely solely on Prometheus for metrics. | You need historical monitoring, accurate monitoring exports or external/custom metrics; Prometheus, kube-state-metrics and cAdvisor have different roles and are not this implementation. | [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `deployment_models` | `[]` | self-hosted | [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4] | Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred. |
| `license_model` | oss | oss | [Project software licence][metrics-server-e2] | Reviewed; retained: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `license_spdx` | *absent* | Apache-2.0 | [Project software licence][metrics-server-e2] | Changed: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `commercial_offering` | *absent* | *absent* | [Canonical repository and identity][metrics-server-e1] | Leave optional field absent; this software review does not deny or infer third-party commercial offerings. |
| `maturity` | unknown | established | [Maintained release history][metrics-server-e3], [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4], [SIG Instrumentation governance][metrics-server-e5] | Established is supported by maintained releases/chart, documented compatibility and operational requirements, and SIG ownership. Metrics API beta version numbering is not a universal experimental-project judgement. |
| `status` | needs-review | active | [Maintained release history][metrics-server-e3], [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4], [SIG Instrumentation governance][metrics-server-e5] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |
| `repository_archived` | *absent* | `false` | [Canonical repository and identity][metrics-server-e1], [Maintained release history][metrics-server-e3] | GitHub API independently reports archived=false; active status is separately supported by maintained releases. |
| `alternatives` | `[]` | `[]` | [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `tags` | `[]` | `[]` | [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `verified_on` | 2026-08-03 | 2026-10-08 | [Canonical repository and identity][metrics-server-e1], [Project software licence][metrics-server-e2], [Maintained release history][metrics-server-e3], [Official implementation documentation][metrics-server-e4], [SIG Instrumentation governance][metrics-server-e5] | Actual execution date 2026-10-08, changed only for the fixed ten records. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L124<br>legacy:devopstools_final.md#L607 | legacy:4_Kubernetes-Containers/README.md#L124<br>legacy:devopstools_final.md#L607<br>https://github.com/kubernetes-sigs/metrics-server<br>https://github.com/kubernetes-sigs/metrics-server/blob/master/LICENSE<br>https://github.com/kubernetes-sigs/metrics-server/releases<br>https://github.com/kubernetes-sigs/metrics-server/blob/master/README.md<br>https://github.com/kubernetes/community/blob/main/sig-instrumentation/README.md | [Canonical repository and identity][metrics-server-e1], [Project software licence][metrics-server-e2], [Maintained release history][metrics-server-e3], [Official implementation documentation][metrics-server-e4], [SIG Instrumentation governance][metrics-server-e5] | Preserve every historical source and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][metrics-server-e3], [Canonical repository and identity][metrics-server-e1], [Official implementation documentation][metrics-server-e4], [SIG Instrumentation governance][metrics-server-e5] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |

**Changed fields:** `summary`, `official_url`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[metrics-server-e1]: https://github.com/kubernetes-sigs/metrics-server
[metrics-server-e2]: https://github.com/kubernetes-sigs/metrics-server/blob/master/LICENSE
[metrics-server-e3]: https://github.com/kubernetes-sigs/metrics-server/releases
[metrics-server-e4]: https://github.com/kubernetes-sigs/metrics-server/blob/master/README.md
[metrics-server-e5]: https://github.com/kubernetes/community/blob/main/sig-instrumentation/README.md

Archival metadata independently checked: [GitHub repository API](https://api.github.com/repos/kubernetes-sigs/metrics-server), archived=false.

### kubernetes-autoscaler

**Identity boundary:** Keep the stable record as the repository umbrella, with Cluster Autoscaler, VPA and Addon Resizer identified by the root README. Cluster Autoscaler changes cluster size, VPA recommends/updates pod resource requests, Addon Resizer changes resources proportionally to node count. HPA is a Kubernetes-core API/controller, separately listed by SIG Autoscaling under kubernetes/api and kubernetes/kubernetes. The umbrella does not own KEDA, Karpenter or every Kubernetes autoscaling feature; no record split is made.

**Licence boundary:** Retain oss and add Apache-2.0 from the directly read kubernetes/autoscaler/LICENSE grant. This describes project/repository software; third-party dependencies, separate providers and vendor services keep their own terms.

**Execution/deployment and commercial boundary:** Leave deployment_models empty: the repository is not one deployable umbrella controller. CA, VPA and Addon Resizer have distinct deployment/configuration paths. No vendor-managed autoscaling entitlement or commercial licence is inherited.

**Repository boundary:** Retain kubernetes/autoscaler as the canonical existing repository boundary, and use its root README as documentation and repository as official entry. Its actual root Apache-2.0 grant supports repository software, not every autoscaling project in Kubernetes.

**Governance:** SIG Autoscaling's current subproject inventory lists this repository's components and separately lists HPA core ownership and Karpenter. Sharing a SIG does not imply one implementation repository.

**Maturity:** Established applies to the maintained repository umbrella and documented component operations. Root README describes Cluster Autoscaler as GA and VPA/Addon Resizer as beta; those component stages are not flattened into universal GA. Component-specific releases and compatibility remain separate.

**Lifecycle:** GitHub API reports archived=false; maintained release feed independently supports active lifecycle. Checked repository metadata and release history. No HTTP result or foundation status alone determines lifecycle.

**Unresolved questions / limits:** None blocking the bounded repository identity/licence. Component stability, cloud integration and deployment differ; empty umbrella deployment is an intentional scope decision.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and identity][kubernetes-autoscaler-e1], [Project software licence][kubernetes-autoscaler-e2], [Maintained release history][kubernetes-autoscaler-e3], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [SIG Autoscaling governance and HPA ownership][kubernetes-autoscaler-e8], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | kubernetes-autoscaler | kubernetes-autoscaler | [Canonical repository and identity][kubernetes-autoscaler-e1] | Preserve existing stable ID; no split, duplicate or substitution. |
| `name` | Kubernetes Autoscaler | Kubernetes Autoscaler | [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9] | Reviewed; retained: documented capability and scoped identity; the boundaries above apply. |
| `summary` | Autoscaling components (HPA/VPA/Cluster Autoscaler). | Repository of Kubernetes autoscaling components including Cluster Autoscaler, Vertical Pod Autoscaler and Addon Resizer; Horizontal Pod Autoscaler is a separate Kubernetes-core API and controller. | [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9] | Changed: documented capability and scoped identity; the boundaries above apply. |
| `official_url` | *absent* | https://github.com/kubernetes/autoscaler | [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9] | Changed: upstream-declared entry point for this identity. Former pointers remain in sources where changed. |
| `repository_url` | https://github.com/kubernetes/autoscaler | https://github.com/kubernetes/autoscaler | [Canonical repository and identity][kubernetes-autoscaler-e1] | Retain directly verified canonical project/repository identity; do not inherit a different component identity. |
| `documentation_url` | *absent* | https://github.com/kubernetes/autoscaler/blob/master/README.md | [Official umbrella documentation][kubernetes-autoscaler-e4] | Add directly checked official documentation at the record boundary; parent/umbrella README used where component guides would misrepresent scope. |
| `categories` | kubernetes-networking-storage-addons | kubernetes-networking-storage-addons | [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `subcategories` | Kubernetes Ecosystem &amp; Add-ons | Autoscaling components | [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9] | Changed: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `use_when` | You need standard pod or node autoscaling based on resource utilization. | You need to select a repository component for node-count adjustment, pod CPU/memory request recommendations or updates, or cluster-proportional addon resource resizing. | [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `avoid_when` | Karpenter (for nodes) or KEDA (for event-driven scaling) better fits your workload patterns. | You expect one installed controller to implement every Kubernetes autoscaling mechanism, or assume this repository owns HPA, KEDA or Karpenter. | [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `deployment_models` | `[]` | `[]` | [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9] | Leave deployment_models empty: the repository is not one deployable umbrella controller. CA, VPA and Addon Resizer have distinct deployment/configuration paths. No vendor-managed autoscaling entitlement or commercial licence is inherited. |
| `license_model` | oss | oss | [Project software licence][kubernetes-autoscaler-e2] | Reviewed; retained: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `license_spdx` | *absent* | Apache-2.0 | [Project software licence][kubernetes-autoscaler-e2] | Changed: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `commercial_offering` | *absent* | *absent* | [Canonical repository and identity][kubernetes-autoscaler-e1] | Leave optional field absent; this software review does not deny or infer third-party commercial offerings. |
| `maturity` | unknown | established | [Maintained release history][kubernetes-autoscaler-e3], [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9], [SIG Autoscaling governance and HPA ownership][kubernetes-autoscaler-e8] | Established applies to the maintained repository umbrella and documented component operations. Root README describes Cluster Autoscaler as GA and VPA/Addon Resizer as beta; those component stages are not flattened into universal GA. Component-specific releases and compatibility remain separate. |
| `status` | needs-review | active | [Maintained release history][kubernetes-autoscaler-e3], [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9], [SIG Autoscaling governance and HPA ownership][kubernetes-autoscaler-e8] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |
| `repository_archived` | *absent* | `false` | [Canonical repository and identity][kubernetes-autoscaler-e1], [Maintained release history][kubernetes-autoscaler-e3] | GitHub API independently reports archived=false; active status is separately supported by maintained releases. |
| `alternatives` | `[]` | `[]` | [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `tags` | `[]` | `[]` | [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `verified_on` | 2026-08-03 | 2026-10-08 | [Canonical repository and identity][kubernetes-autoscaler-e1], [Project software licence][kubernetes-autoscaler-e2], [Maintained release history][kubernetes-autoscaler-e3], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [SIG Autoscaling governance and HPA ownership][kubernetes-autoscaler-e8], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9] | Actual execution date 2026-10-08, changed only for the fixed ten records. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L115<br>legacy:devopstools_final.md#L594 | legacy:4_Kubernetes-Containers/README.md#L115<br>legacy:devopstools_final.md#L594<br>https://github.com/kubernetes/autoscaler<br>https://github.com/kubernetes/autoscaler/blob/master/LICENSE<br>https://github.com/kubernetes/autoscaler/releases<br>https://github.com/kubernetes/autoscaler/blob/master/README.md<br>https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/README.md<br>https://github.com/kubernetes/autoscaler/blob/master/vertical-pod-autoscaler/README.md<br>https://github.com/kubernetes/autoscaler/blob/master/addon-resizer/README.md<br>https://github.com/kubernetes/community/blob/main/sig-autoscaling/README.md<br>https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/ | [Canonical repository and identity][kubernetes-autoscaler-e1], [Project software licence][kubernetes-autoscaler-e2], [Maintained release history][kubernetes-autoscaler-e3], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [SIG Autoscaling governance and HPA ownership][kubernetes-autoscaler-e8], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9] | Preserve every historical source and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][kubernetes-autoscaler-e3], [Canonical repository and identity][kubernetes-autoscaler-e1], [Official umbrella documentation][kubernetes-autoscaler-e4], [Cluster Autoscaler component documentation][kubernetes-autoscaler-e5], [Vertical Pod Autoscaler component documentation][kubernetes-autoscaler-e6], [Addon Resizer component documentation][kubernetes-autoscaler-e7], [Kubernetes-core HPA documentation][kubernetes-autoscaler-e9], [SIG Autoscaling governance and HPA ownership][kubernetes-autoscaler-e8] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |

**Changed fields:** `summary`, `official_url`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[kubernetes-autoscaler-e1]: https://github.com/kubernetes/autoscaler
[kubernetes-autoscaler-e2]: https://github.com/kubernetes/autoscaler/blob/master/LICENSE
[kubernetes-autoscaler-e3]: https://github.com/kubernetes/autoscaler/releases
[kubernetes-autoscaler-e4]: https://github.com/kubernetes/autoscaler/blob/master/README.md
[kubernetes-autoscaler-e5]: https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/README.md
[kubernetes-autoscaler-e6]: https://github.com/kubernetes/autoscaler/blob/master/vertical-pod-autoscaler/README.md
[kubernetes-autoscaler-e7]: https://github.com/kubernetes/autoscaler/blob/master/addon-resizer/README.md
[kubernetes-autoscaler-e8]: https://github.com/kubernetes/community/blob/main/sig-autoscaling/README.md
[kubernetes-autoscaler-e9]: https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/

Archival metadata independently checked: [GitHub repository API](https://api.github.com/repos/kubernetes/autoscaler), archived=false.

### karpenter

**Identity boundary:** Parent Karpenter comprises shared APIs/controllers and separate provider implementations. The canonical core README explicitly describes a multi-cloud project and lists AWS among implementations; its CloudProvider interface defines integration with provider-specific provisioning. Node provisioning is distinct from CA node-group sizing, KEDA workload/event scaling and cloud autoscaling groups. No transient provider list becomes catalogue metadata.

**Licence boundary:** Retain oss and add Apache-2.0 from the directly read kubernetes-sigs/karpenter/LICENSE grant. This describes project/repository software; third-party dependencies, separate providers and vendor services keep their own terms.

**Execution/deployment and commercial boundary:** Record self-hosted controller execution through a chosen provider implementation. Shared core is not a standalone ready-to-install provider. Cloud resources and provider-specific services/permissions are external; no managed-service or AWS-product licensing is inherited.

**Repository boundary:** Change repository_url from aws/karpenter-provider-aws to kubernetes-sigs/karpenter based on explicit core README/provider-interface and SIG inventory evidence, not recency. Change official_url to the shared project repository and documentation_url to its README so the generic record enters at the parent boundary. Preserve the former AWS repository and karpenter.sh site in sources; karpenter.sh installation documentation checked here is AWS-specific and remains explicitly qualified evidence.

**Governance:** Current SIG Autoscaling inventory explicitly owns kubernetes-sigs/karpenter and separately names provider subprojects. This establishes shared-core project ownership independently of the AWS implementation.

**Maturity:** Established is assessed for the maintained core from its own releases, scheduling/provisioning interfaces and SIG governance. AWS release history or provider maturity is not silently transferred to all implementations.

**Lifecycle:** GitHub API reports archived=false; maintained release feed independently supports active lifecycle. Checked repository metadata and release history. No HTTP result or foundation status alone determines lifecycle.

**Unresolved questions / limits:** None blocking parent/core identity/licence. Installation, cloud permissions and feature/support maturity depend on the selected provider; the core entry links implementations rather than pretending one AWS guide covers all.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and identity][karpenter-e1], [Project software licence][karpenter-e2], [Maintained release history][karpenter-e3], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [SIG Autoscaling governance][karpenter-e6], [Separate AWS provider repository][karpenter-e7], [AWS-provider installation documentation][karpenter-e8].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | karpenter | karpenter | [Canonical repository and identity][karpenter-e1], [Separate AWS provider repository][karpenter-e7] | Preserve existing stable ID; no split, duplicate or substitution. |
| `name` | Karpenter | Karpenter | [Canonical repository and identity][karpenter-e1], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8] | Reviewed; retained: documented capability and scoped identity; the boundaries above apply. |
| `summary` | Kubernetes node autoscaler. | Kubernetes node autoscaling project with shared APIs and controllers plus separate provider implementations; provisions nodes for unschedulable pods and manages node lifecycle rather than workload replica counts. | [Canonical repository and identity][karpenter-e1], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8] | Changed: documented capability and scoped identity; the boundaries above apply. |
| `official_url` | https://karpenter.sh | https://github.com/kubernetes-sigs/karpenter | [Canonical repository and identity][karpenter-e1], [Separate AWS provider repository][karpenter-e7], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8] | Changed: upstream-declared entry point for this identity. Former pointers remain in sources where changed. |
| `repository_url` | https://github.com/aws/karpenter-provider-aws | https://github.com/kubernetes-sigs/karpenter | [Canonical repository and identity][karpenter-e1], [Separate AWS provider repository][karpenter-e7] | Change repository_url from aws/karpenter-provider-aws to kubernetes-sigs/karpenter based on explicit core README/provider-interface and SIG inventory evidence, not recency. Change official_url to the shared project repository and documentation_url to its README so the generic record enters at the parent boundary. Preserve the former AWS repository and karpenter.sh site in sources; karpenter.sh installation documentation checked here is AWS-specific and remains explicitly qualified evidence. |
| `documentation_url` | *absent* | https://github.com/kubernetes-sigs/karpenter/blob/main/README.md | [Official shared-core documentation and provider identities][karpenter-e4] | Add directly checked official documentation at the record boundary; parent/umbrella README used where component guides would misrepresent scope. |
| `categories` | kubernetes-networking-storage-addons | kubernetes-networking-storage-addons | [Canonical repository and identity][karpenter-e1], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `subcategories` | Kubernetes Ecosystem &amp; Add-ons | Node provisioning | [Canonical repository and identity][karpenter-e1], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8] | Changed: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Canonical repository and identity][karpenter-e1], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Canonical repository and identity][karpenter-e1], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `use_when` | You need fast, flexible node provisioning with workload-aware instance selection (primarily AWS). | You need node provisioning driven by pod scheduling constraints and a compatible provider implementation with its documented infrastructure permissions and lifecycle behavior. | [Canonical repository and identity][karpenter-e1], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `avoid_when` | The standard Cluster Autoscaler works well enough or you&#x27;re on a cloud without Karpenter support. | You need event-driven workload replica scaling or assume the shared core alone installs a cloud provider, replaces every cloud autoscaling service or gives all providers identical support. | [Canonical repository and identity][karpenter-e1], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `deployment_models` | `[]` | self-hosted | [Canonical repository and identity][karpenter-e1], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8] | Record self-hosted controller execution through a chosen provider implementation. Shared core is not a standalone ready-to-install provider. Cloud resources and provider-specific services/permissions are external; no managed-service or AWS-product licensing is inherited. |
| `license_model` | oss | oss | [Project software licence][karpenter-e2] | Reviewed; retained: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `license_spdx` | *absent* | Apache-2.0 | [Project software licence][karpenter-e2] | Changed: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `commercial_offering` | *absent* | *absent* | [Canonical repository and identity][karpenter-e1], [Separate AWS provider repository][karpenter-e7] | Leave optional field absent; this software review does not deny or infer third-party commercial offerings. |
| `maturity` | unknown | established | [Maintained release history][karpenter-e3], [Canonical repository and identity][karpenter-e1], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8], [SIG Autoscaling governance][karpenter-e6] | Established is assessed for the maintained core from its own releases, scheduling/provisioning interfaces and SIG governance. AWS release history or provider maturity is not silently transferred to all implementations. |
| `status` | needs-review | active | [Maintained release history][karpenter-e3], [Canonical repository and identity][karpenter-e1], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8], [SIG Autoscaling governance][karpenter-e6] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |
| `repository_archived` | *absent* | `false` | [Canonical repository and identity][karpenter-e1], [Separate AWS provider repository][karpenter-e7], [Maintained release history][karpenter-e3] | GitHub API independently reports archived=false; active status is separately supported by maintained releases. |
| `alternatives` | `[]` | `[]` | [Canonical repository and identity][karpenter-e1], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `tags` | `[]` | `[]` | [Canonical repository and identity][karpenter-e1], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `verified_on` | 2026-08-03 | 2026-10-08 | [Canonical repository and identity][karpenter-e1], [Project software licence][karpenter-e2], [Maintained release history][karpenter-e3], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [SIG Autoscaling governance][karpenter-e6], [Separate AWS provider repository][karpenter-e7], [AWS-provider installation documentation][karpenter-e8] | Actual execution date 2026-10-08, changed only for the fixed ten records. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L106<br>legacy:devopstools_final.md#L581 | legacy:4_Kubernetes-Containers/README.md#L106<br>legacy:devopstools_final.md#L581<br>https://github.com/kubernetes-sigs/karpenter<br>https://github.com/kubernetes-sigs/karpenter/blob/main/LICENSE<br>https://github.com/kubernetes-sigs/karpenter/releases<br>https://github.com/kubernetes-sigs/karpenter/blob/main/README.md<br>https://github.com/kubernetes-sigs/karpenter/blob/main/pkg/cloudprovider/types.go<br>https://github.com/kubernetes/community/blob/main/sig-autoscaling/README.md<br>https://github.com/aws/karpenter-provider-aws<br>https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/<br>https://karpenter.sh | [Canonical repository and identity][karpenter-e1], [Project software licence][karpenter-e2], [Maintained release history][karpenter-e3], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [SIG Autoscaling governance][karpenter-e6], [Separate AWS provider repository][karpenter-e7], [AWS-provider installation documentation][karpenter-e8] | Preserve every historical source and append directly checked primary evidence. Preserve former official_url https://karpenter.sh as provenance. Preserve former repository_url https://github.com/aws/karpenter-provider-aws as provenance. |
| `needs_review` | `true` | `false` | [Maintained release history][karpenter-e3], [Canonical repository and identity][karpenter-e1], [Official shared-core documentation and provider identities][karpenter-e4], [Shared provider API and interface][karpenter-e5], [AWS-provider installation documentation][karpenter-e8], [SIG Autoscaling governance][karpenter-e6] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |

**Changed fields:** `summary`, `official_url`, `repository_url`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[karpenter-e1]: https://github.com/kubernetes-sigs/karpenter
[karpenter-e2]: https://github.com/kubernetes-sigs/karpenter/blob/main/LICENSE
[karpenter-e3]: https://github.com/kubernetes-sigs/karpenter/releases
[karpenter-e4]: https://github.com/kubernetes-sigs/karpenter/blob/main/README.md
[karpenter-e5]: https://github.com/kubernetes-sigs/karpenter/blob/main/pkg/cloudprovider/types.go
[karpenter-e6]: https://github.com/kubernetes/community/blob/main/sig-autoscaling/README.md
[karpenter-e7]: https://github.com/aws/karpenter-provider-aws
[karpenter-e8]: https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/

Archival metadata independently checked: [GitHub repository API](https://api.github.com/repos/kubernetes-sigs/karpenter), archived=false.

### keda

**Identity boundary:** KEDA manages workload/event autoscaling: operator activation between zero and one, HPA-driven scaling beyond one using its external-metrics API, and event-triggered Jobs. Its metrics adapter is not the resource Metrics Server implementation. It integrates with HPA and event sources rather than becoming them; node provisioning belongs to other systems such as CA/Karpenter.

**Licence boundary:** Retain oss and add Apache-2.0 from the directly read kedacore/keda/LICENSE grant. This describes project/repository software; third-party dependencies, separate providers and vendor services keep their own terms.

**Execution/deployment and commercial boundary:** Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred.

**Repository boundary:** Retain verified kedacore/keda canonical project repository; documented related components remain separate.

**Governance:** CNCF records KEDA as Graduated since 2023-08-22. Its own governance defines repository/organization maintainers and voting, independently of Kubernetes HPA ownership.

**Maturity:** Established is supported by maintained releases, documented architecture/operations and project governance; no support guarantees for every event source/scaler are inferred from graduation.

**Lifecycle:** GitHub API reports archived=false; maintained release feed independently supports active lifecycle. Checked repository metadata and release history. No HTTP result or foundation status alone determines lifecycle.

**Unresolved questions / limits:** None blocking identity/licence. Scaler behavior, credential requirements and workload handling depend on the selected integration and release.

**Disposition: CLEAR REVIEW**

**Primary sources checked:** [Canonical repository and identity][keda-e1], [Project software licence][keda-e2], [Maintained release history][keda-e3], [Official architecture and HPA documentation][keda-e4], [Project governance][keda-e5], [Current CNCF foundation status][keda-e6].

| Field | Before | After | Primary evidence | Decision |
|---|---|---|---|---|
| `id` | keda | keda | [Canonical repository and identity][keda-e1] | Preserve existing stable ID; no split, duplicate or substitution. |
| `name` | KEDA | KEDA | [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4] | Reviewed; retained: documented capability and scoped identity; the boundaries above apply. |
| `summary` | Kubernetes-based Event Driven Autoscaler. | Event-driven Kubernetes workload autoscaling that manages HPA resources and supplies external metrics, with workload activation from zero and event-driven Jobs; separate from node provisioning and the Metrics Server resource pipeline. | [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4] | Changed: documented capability and scoped identity; the boundaries above apply. |
| `official_url` | https://keda.sh | https://keda.sh | [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4] | Reviewed; retained: upstream-declared entry point for this identity. Former pointers remain in sources where changed. |
| `repository_url` | https://github.com/kedacore/keda | https://github.com/kedacore/keda | [Canonical repository and identity][keda-e1] | Retain directly verified canonical project/repository identity; do not inherit a different component identity. |
| `documentation_url` | *absent* | https://keda.sh/docs/latest/concepts/ | [Official architecture and HPA documentation][keda-e4] | Add directly checked official documentation at the record boundary; parent/umbrella README used where component guides would misrepresent scope. |
| `categories` | kubernetes-networking-storage-addons | kubernetes-networking-storage-addons | [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `subcategories` | Kubernetes Ecosystem &amp; Add-ons | Event-driven workload autoscaling | [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4] | Changed: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `roles` | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | platform-engineer<br>site-reliability-engineer<br>kubernetes-engineer | [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `lifecycle_stages` | deploy<br>operate | deploy<br>operate | [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4] | Reviewed; retained: reviewer mapping of documented workflows to existing taxonomy. Category, roles and lifecycle remain valid; no taxonomy changes. |
| `use_when` | You need to scale workloads based on external event sources (queues, streams, custom metrics). | You need workload replica activation or scaling from event-source signals, or event-triggered Kubernetes Jobs, with a documented KEDA scaler and credentials. | [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `avoid_when` | Standard HPA with CPU/memory metrics is sufficient. | You need Kubernetes node provisioning or assume KEDA replaces HPA, resource Metrics Server or the event-source system itself. | [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4] | Changed: documented selection and operational limits; unsupported rankings removed. |
| `deployment_models` | `[]` | self-hosted | [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4] | Record self-hosted software/server/controller execution supported by upstream documentation. Leave optional commercial_offering absent; no third-party support, provider subscription or vendor product term is inferred. |
| `license_model` | oss | oss | [Project software licence][keda-e2] | Reviewed; retained: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `license_spdx` | *absent* | Apache-2.0 | [Project software licence][keda-e2] | Changed: actual project/repository software grant, not foundation membership or provider/vendor terms. |
| `commercial_offering` | *absent* | *absent* | [Canonical repository and identity][keda-e1] | Leave optional field absent; this software review does not deny or infer third-party commercial offerings. |
| `maturity` | unknown | established | [Maintained release history][keda-e3], [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4], [Project governance][keda-e5], [Current CNCF foundation status][keda-e6] | Established is supported by maintained releases, documented architecture/operations and project governance; no support guarantees for every event source/scaler are inferred from graduation. |
| `status` | needs-review | active | [Maintained release history][keda-e3], [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4], [Project governance][keda-e5], [Current CNCF foundation status][keda-e6] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |
| `repository_archived` | *absent* | `false` | [Canonical repository and identity][keda-e1], [Maintained release history][keda-e3] | GitHub API independently reports archived=false; active status is separately supported by maintained releases. |
| `alternatives` | `[]` | `[]` | [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `tags` | `[]` | `[]` | [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4] | Retain empty optional metadata; do not add rankings or unsupported tags. |
| `verified_on` | 2026-08-03 | 2026-10-08 | [Canonical repository and identity][keda-e1], [Project software licence][keda-e2], [Maintained release history][keda-e3], [Official architecture and HPA documentation][keda-e4], [Project governance][keda-e5], [Current CNCF foundation status][keda-e6] | Actual execution date 2026-10-08, changed only for the fixed ten records. |
| `sources` | legacy:4_Kubernetes-Containers/README.md#L108<br>legacy:devopstools_final.md#L583 | legacy:4_Kubernetes-Containers/README.md#L108<br>legacy:devopstools_final.md#L583<br>https://github.com/kedacore/keda<br>https://github.com/kedacore/keda/blob/main/LICENSE<br>https://github.com/kedacore/keda/releases<br>https://keda.sh/docs/latest/concepts/<br>https://github.com/kedacore/governance/blob/main/GOVERNANCE.md<br>https://www.cncf.io/projects/keda/ | [Canonical repository and identity][keda-e1], [Project software licence][keda-e2], [Maintained release history][keda-e3], [Official architecture and HPA documentation][keda-e4], [Project governance][keda-e5], [Current CNCF foundation status][keda-e6] | Preserve every historical source and append directly checked primary evidence. |
| `needs_review` | `true` | `false` | [Maintained release history][keda-e3], [Canonical repository and identity][keda-e1], [Official architecture and HPA documentation][keda-e4], [Project governance][keda-e5], [Current CNCF foundation status][keda-e6] | CLEAR REVIEW: primary evidence resolves material boundaries and supports active maintenance; status and needs_review stay consistent. |

**Changed fields:** `summary`, `documentation_url`, `subcategories`, `use_when`, `avoid_when`, `deployment_models`, `license_spdx`, `maturity`, `status`, `repository_archived`, `verified_on`, `sources`, `needs_review`.

[keda-e1]: https://github.com/kedacore/keda
[keda-e2]: https://github.com/kedacore/keda/blob/main/LICENSE
[keda-e3]: https://github.com/kedacore/keda/releases
[keda-e4]: https://keda.sh/docs/latest/concepts/
[keda-e5]: https://github.com/kedacore/governance/blob/main/GOVERNANCE.md
[keda-e6]: https://www.cncf.io/projects/keda/

Archival metadata independently checked: [GitHub repository API](https://api.github.com/repos/kedacore/keda), archived=false.

## Review-debt accounting

Selected **10**, cleared **10**, retained **0**. Before/after review-debt command output captured.

| Counter | Before | After |
|---|---:|---:|
| canonical_records | 1,425 | 1,425 |
| needs_review | 736 | 726 |
| status_needs_review | 736 | 726 |
| mismatches | 0 | 0 |
| unknown_license | 80 | 80 |
| unknown_maturity | 874 | 864 |
| missing_repository | 391 | 391 |
| missing_documentation | 870 | 860 |
| missing_sources | 0 | 0 |

Mismatches remain zero. Unknown maturity and missing documentation each decrease by ten. Missing repository and unknown licence-model counts remain unchanged. Nine records are established; MetalLB is growing with its beta qualification preserved.

## Generated changes

Only generator output is listed; this report and focused regression tests are authored.

- `README.md`
- `docs/catalog-statistics.json`
- `docs/categories/kubernetes-networking-storage-addons.md`
- `docs/lifecycle/deploy.md`
- `docs/lifecycle/operate.md`
- `docs/roles/kubernetes-engineer.md`
- `docs/roles/platform-engineer.md`
- `docs/roles/site-reliability-engineer.md`

## Validation and full link audit

Required checks passed. Python 3.12.3 in the existing constrained WSL environment ran installation, fresh resolution, the full suite and the network audit. The Windows editable environment ran focused tests, lint/format, generation, catalogue validation and debt capture. In commands below, python denotes the selected interpreter.

| Command | Result |
|---|---|
| `python -m pip install -e '.[dev]' -c config/python-constraints-3.12.txt` | PASS; constrained editable install |
| `python -m scripts.python_constraints --check` | PASS; fresh resolver matches unchanged constraints |
| `python -m ruff check scripts tests` | PASS |
| `python -m ruff format --check scripts tests` | PASS; 63 files already formatted |
| `python -m pytest tests/test_wave10_evidence_review.py` | PASS; 28 tests |
| `python -m pytest` | PASS; 804 tests in 257.34 seconds |
| `python -m scripts.generate_docs` | PASS; regenerated after canonical changes |
| `python -m scripts.generate_docs --check` | PASS |
| `python -m scripts.validate_catalog` | PASS |
| `python -m scripts.review_debt --format markdown --limit 30` | PASS; before and after captured |
| `git diff --check` | PASS |

The 28 focused cases protect project-specific licence evidence; server/controller execution versus repository umbrella deployment; CoreDNS versus ExternalDNS; mesh versus gateway/proxy/API; MetalLB LoadBalancer and network limits; Longhorn block storage, file-sharing and independent software licence; Metrics Server resource API and monitoring limits; autoscaler components versus core HPA; Karpenter core/provider identity and preserved AWS provenance; KEDA workload/HPA/events versus node provisioning; and maturity/foundation evidence versus software licensing. Tests do not assert prices, current release numbers, provider lists or transient HTTP behavior.

Focused Windows tests and the full WSL suite each emitted one non-failing pytest cache-permission warning. Full WSL Git-dependent tests used process-only GIT_CONFIG_COUNT=1, GIT_CONFIG_KEY_0=core.autocrlf and GIT_CONFIG_VALUE_0=true to interpret the Windows checkout consistently. No repository/global Git setting, constraint, assertion or workflow was weakened.

Exactly one fresh full strict audit, with cache reuse disabled and ignored output paths:

```bash
python -m scripts.check_links --strict --check-archived --workers 8 --cache tmp/wave10/link-cache.json --cache-hours 0 --json-report tmp/wave10/link-report.json --markdown-report tmp/wave10/link-report.md
```

| Audit counter | Result |
|---|---:|
| URLs | 2,675 |
| blocking_new | 0 |
| blocking_known observed | 4 |
| strict_result | PASS |

**Reviewed baseline changed: NO.** All six reviewed exceptions remain. Runtime responses do not establish a baseline shrink, repaired defect, licence or project lifecycle.

| Existing baseline URL | Observed response | Classification / strict status |
|---|---|---|
| `https://github.com/hoji-ai/hoji` | HTTP 429 | rate-limited / nonblocking |
| `https://github.com/ophircloud/DevOps-Projects` | HTTP 429 | rate-limited / nonblocking |
| `https://hub.docker.com/r/soosio/dast` | HTTP 404 | manual-verification-required / blocking-known |
| `https://kubeflame.github.io` | HTTP 404 | manual-verification-required / blocking-known |
| `https://www.opentext.com/products/static-application-security-testing` | HTTP 444 | http-error / blocking-known |
| `https://www.yotascale.com` | HTTP 404 | manual-verification-required / blocking-known |

All final documentation entry points were included:

| ID | Documentation response | Classification |
|---|---|---|
| `istio` | HTTP 200 | valid |
| `coredns` | HTTP 200 | valid |
| `metallb` | HTTP 200 | valid |
| `externaldns` | HTTP 200 | valid |
| `envoy-gateway` | HTTP 200 | valid |
| `longhorn` | HTTP 200 | permanent-redirect |
| `metrics-server` | HTTP 429 | rate-limited |
| `kubernetes-autoscaler` | HTTP 429 | rate-limited |
| `karpenter` | HTTP 403 | restricted-or-bot-blocked |
| `keda` | HTTP 200 | valid-redirect |

All observed classifications, including network limitations:

| Classification | Count |
|---|---:|
| dns-inconclusive | 5 |
| http-error | 1 |
| manual-verification-required | 3 |
| permanent-redirect | 205 |
| rate-limited | 785 |
| restricted-or-bot-blocked | 358 |
| timeout-inconclusive | 1 |
| transient-failure | 1 |
| valid | 1,293 |
| valid-redirect | 23 |

Strict PASS means no newly classified blockers, not successful verification of every endpoint. Direct primary licence, documentation, governance and release evidence independently support the decisions. The audit inventories canonical official/repository/documentation URLs; source-only evidence was read separately. No required network-dependent check was omitted. Raw audit/cache outputs remain ignored under tmp/wave10; no reports output is committed.

## Scope verification and review state

Before/after snapshots and the baseline Git tree prove exactly ten changed canonical IDs, verified_on dates and record blocks, and 240 complete material-field rows. Every historical source remains; all other record blocks are unchanged. Final canonical URLs equal the single audited set. The six-entry link baseline, committed audit output/ledger, workflows, CodeQL configuration and Python constraints are unchanged. Issue #2 is read-only and compared with its saved body/timestamp at handoff. Wave 4–9 records are not revisited; Wave 11 is not started; no merge or release.

Material evidence findings resolved: Karpenter now enters through its shared-core project rather than silently inheriting AWS-provider identity; former AWS repository and site remain provenance. Kubernetes Autoscaler stays a repository umbrella, identifies CA/VPA/Addon Resizer and separates Kubernetes-core HPA. Metrics Server official entry points at its implementation, with current resource metrics separate from historical monitoring. Envoy Gateway control plane, Envoy dataplane, Gateway API standard and Istio mesh remain separate. CoreDNS and ExternalDNS serve different DNS roles. MetalLB remains beta-qualified growing LoadBalancer software, with network compatibility limits. Longhorn preserves block storage and separate file-sharing semantics without Rancher commercial inheritance. KEDA event/workload/HPA architecture does not become node provisioning. Current governance and licence evidence are independently checked.

No blocking material identity/licence claim remains unresolved. Provider/feature compatibility, component stages, upstream beta qualification, volume access modes and the dated Envoy Gateway governance roster remain explicit limitations. Current officeholders or universal provider compatibility are not asserted. Final-head GitHub checks and review resolution states are reported in the PR and final handoff.
