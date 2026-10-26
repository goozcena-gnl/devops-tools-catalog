# Wave 26 — Kubernetes cluster lifecycle: first-pass evidence triage

**Observed 2026-10-26. Documentary triage only: 0 CLEAR, 10 pending.** This is the first-pass historic checkpoint, **not** a completed clearance decision. [Selection issue #143](https://github.com/goozcena-gnl/devops-tools-catalog/issues/143). Base `main` `77f844cadcb9c95d464925d33675700a8883ceab`.

## Pinned baseline and scope
- **1,425** canonical records, **800 active**, **611 needs-review**, 30 categories.
- Category YAML `data/tools/kubernetes-distributions-operations.yaml`, initial blob `0e61450d22befbd7a8aba7b0ac0da3ed603ccc3d`: **142 existing records**, of which **59** are `needs-review`. Selection is exactly **10** existing IDs, leaving 132 nonselected records intact in any later update.
- All ten remain `status: needs-review`, `needs_review: true`, initially verified 2026-08-03. This commit adds **only this Markdown file**; no canonical YAML, generated files, lockfiles, workflows or baseline modified.
- Historical `config/link-audit-baseline.json`: **six** reviewed URL/classification exceptions; SHA `a834e2af711693def40078a55e31dfeb29bee2c7`. Keep issue #2 open. Prior Wave 25 audit #39 does **not** qualify as Wave 26 final-head evidence.

## Source checks at immutable release tags

These tagged licence-file observations establish **candidate source grants**, not product/edition-wide licensing or supported compatibility matrices. All ten candidates need independent review before any CLEAR decision.

| Canonical ID | Directly checked first-party evidence | Open issue / operational boundary |
|---|---|---|
| `cluster-api-provider-aws` | [CAPA v2.13.1 LICENSE](https://github.com/kubernetes-sigs/cluster-api-provider-aws/blob/v2.13.1/LICENSE) contains Apache-2.0; [release](https://github.com/kubernetes-sigs/cluster-api-provider-aws/releases/tag/v2.13.1), [docs](https://cluster-api-aws.sigs.k8s.io/) | Cluster API core/provider compatibility; AWS IAM and privilege boundaries, self-managed vs EKS deployment distinction, tenancy and cloud cost |
| `k0smotron` | [v2.3.0 LICENSE](https://github.com/k0sproject/k0smotron/blob/v2.3.0/LICENSE) expressly states **Apache-2.0 software**, **CC-BY-SA-4.0 under docs/**; [release v2.3.0](https://github.com/k0sproject/k0smotron/releases/tag/v2.3.0), concurrent older [v1.10.10](https://github.com/k0sproject/k0smotron/releases/tag/v1.10.10) | GitHub badge `NOASSERTION` is not decisive; **cannot use one SPDX for entire tree**. Confirm whether docs licence file and release artefacts preserve distinction; CAPI/k0s compatibility, hosted control-plane isolation and supported v1/v2 branches |
| `k3d` | [v5.9.0 LICENSE](https://github.com/k3d-io/k3d/blob/v5.9.0/LICENSE) is MIT; [release v5.9.0](https://github.com/k3d-io/k3d/releases/tag/v5.9.0), [docs](https://k3d.io/) | Local k3s-in-Docker wrapper rather than a separate upstream Kubernetes distribution; Docker socket privileges and host resource isolation; not inherently HA production |
| `kubeadm` | [kubernetes/kubeadm README](https://github.com/kubernetes/kubeadm/blob/main/README.md) explicitly says **issue aggregator**, points to actual [Kubernetes cmd/kubeadm](https://github.com/kubernetes/kubernetes/tree/v1.35.0/cmd/kubeadm); tagged [kubeadm source file](https://github.com/kubernetes/kubernetes/blob/v1.35.0/cmd/kubeadm/kubeadm.go) plus [root v1.35.0 LICENSE](https://github.com/kubernetes/kubernetes/blob/v1.35.0/LICENSE) are Apache-2.0 | **Current canonical `repository_url` points to issue-only tracker**. Confirm and, if supported, change to authentic upstream code without losing historical source; verify upstream Kubernetes versions, bootstrap vs lifecycle, secure join/token/certificate operations |
| `microk8s` | [Canonical v1.36 LICENSE](https://github.com/canonical/microk8s/blob/v1.36/LICENSE) is Apache-2.0, [release](https://github.com/canonical/microk8s/releases/tag/v1.36), [site](https://microk8s.io/) | Snap channel vs Kubernetes version support, hardware/OS architecture and add-on dependencies; not automatic full control-plane production HA |
| `rancher-k3k` | [stable v1.2.0 LICENSE](https://github.com/rancher/k3k/blob/v1.2.0/LICENSE) is Apache-2.0; [v1.2.0 README](https://github.com/rancher/k3k/blob/v1.2.0/README.md) describes hosted/shared/virtual clusters; newer `v1.2.1-rc2` and `chart-1.2.1-rc2` must not be called GA from release flags alone | Virtual-mode agent pods can run privileged on host; verify underlying K3s/container/runtime host-boundary and management cluster permissions; chart tag is not same thing as stable application version |
| `typhoon` | [v1.36.1 LICENSE](https://github.com/poseidon/typhoon/blob/v1.36.1/LICENSE) MIT; [release](https://github.com/poseidon/typhoon/releases/tag/v1.36.1), [docs](https://typhoon.psdn.io/) | Terraform-driven Kubernetes provisioning; provider/runtime support, secrets/IAM/state security and upgrade matrix; tool's license is not provider license |
| `kubeedge` | [v1.23.1 LICENSE](https://github.com/kubeedge/kubeedge/blob/v1.23.1/LICENSE) Apache-2.0; [release](https://github.com/kubeedge/kubeedge/releases/tag/v1.23.1), [site](https://kubeedge.io/) | Edge/cloud trust, offline autonomy semantics, cert/identity/IoT-device risk, Kubernetes API compatibility; not equivalent to single-node distro |
| `kubesphere` | [v4.1.3 LICENSE](https://github.com/kubesphere/kubesphere/blob/v4.1.3/LICENSE) says Apache-2.0 **with extra commercial restrictions requiring explicit approval** for listed third-party commercial service/distribution; distinguishes v4.x from 3.4.x and earlier | **CRITICAL:** existing `license_model: oss` for current 4.x may misrepresent licensing. Need exact source-available, open-core or mixed-version taxonomy decision and commercial edition details. Do not assign plain `Apache-2.0` SPDX or CLEAR without evidence of rights and edition boundaries |
| `kubesolo` | [v1.2.2 LICENSE](https://github.com/portainer/kubesolo/blob/v1.2.2/LICENSE) MIT; [tagged README](https://github.com/portainer/kubesolo/blob/v1.2.2/README.md) describes OCI-compatible **single-node Kubernetes for edge, servers and developer environments** rather than macOS GUI; [release](https://github.com/portainer/kubesolo/releases/tag/v1.2.2) | **CRITICAL stale canonical summary** currently asserts native macOS desktop app; validate what platform/OS support is actually maintained, clarify single-node/non-HA limits and compatibility claims (do not repeat upstream marketing as empirically proven) |

## Required second pass and implementation contract

1. Review all ten independently against **first-party versioned** release, licence/notice, compatibility, security, docs and legal edition sources. Report final per-ID **CLEAR** or **RETAIN REVIEW** without a forced quota. In particular, resolve: kubeadm issue tracker vs source; KubeSphere v4 non-OSI-commercial conditions; KubeSolo changed identity; k0smotron software/documentation dual grants; k3k chart/RC and privileged virtual cluster agents.
2. Create a dated field-by-field before/after record for any proposed canonical edit. Constrain all edits to these ten IDs within `data/tools/kubernetes-distributions-operations.yaml`, plus official generated views and this ledger. All **132** other records must be logically identical, in same ordering. Keep all legacy `sources` and category/roles/lifecycle assignments, avoid inappropriate licence/model conflations and overconfident `maturity`.
3. Use clean pinned Python 3.12 environment. Run official `python -m scripts.generate_docs` / `--check`, `python -m scripts.validate_catalog`, `python -m ruff check scripts tests`, `python -m ruff format --check scripts tests`, `python -m pytest -q`, `python -m pip check`, `git diff --check`, plus exact cohort scope audit and statistics check. Mandatory clean Linux `scripts.python_constraints --verify-locked` in CI; do not rewrite constraints to accommodate Windows-only extra `colorama`.
4. Keep PR **Draft**. Once an actual canonical commit exists, update historic triage text and PR body to distinguish first pass from applied state; verify all exact-final-HEAD CI checks; obtain completed independent P1/P2 Codex or human review; manually dispatch fresh strict Full link audit on the **same** final SHA, inspect JSON/Markdown and require `strict_result: PASS`, `blocking_new: 0`, six identical exception pairs.
5. **Human decision only** for Ready and manual Squash and merge. No auto-merge, force-push, baseline waiver, release/tag, security bypass or issue closure. After explicit merge, verify new `main` SHA and four post-merge workflows, then close selection [issue #143](https://github.com/goozcena-gnl/devops-tools-catalog/issues/143). Keep historical [issue #2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2) open.

## First-pass actual actions

Initial documentary evidence only, **0 CLEAR**, **10 pending**. This stage did not change canonical status or count, generated Markdown, license constraints, link exception baseline, issue state or release. No local pytest/Ruff or new strict Wave 26 network audit has been performed.


---

## Second-pass proposed decisions — 2026-10-26 (NOT YET APPLIED)

**Proposed decisions: 8 CLEAR / 2 RETAIN REVIEW.** The 0-clear triage above is retained as a *historical first-pass snapshot*, **not** the current proposed outcome. No YAML or generated view was altered by this documentation-only review. Final clearance remains conditional on a clean local patch, full tests and fresh GitHub CI.

| Decision | Canonical ID | Evidence and specific boundary |
|---|---|---|
| **CLEAR** | `cluster-api-provider-aws` | [Tagged v2.13.1 LICENSE Apache-2.0](https://github.com/kubernetes-sigs/cluster-api-provider-aws/blob/v2.13.1/LICENSE), [release](https://github.com/kubernetes-sigs/cluster-api-provider-aws/releases/tag/v2.13.1), [CAPI version compatibility](https://cluster-api-aws.sigs.k8s.io/topics/reference/versions) and [AWS quick start](https://cluster-api-aws.sigs.k8s.io/quick-start). This is an AWS infrastructure provider, not generic Kubernetes provisioning or an authorization shortcut for EKS; least-privilege IAM, released CAPI/CAPA compatibility and VPC/AMI costs must be assessed. |
| **RETAIN REVIEW** | `k0smotron` | [Tagged v2.3.0 LICENSE](https://github.com/k0sproject/k0smotron/blob/v2.3.0/LICENSE) expressly splits code **Apache-2.0** from `docs/` **CC-BY-SA-4.0**, and the expected `docs/LICENCE` could not be directly resolved at that tag during review. [v2.3.0 installation doc](https://docs.k0smotron.io/v2.3.0/install/) defines standalone vs CAPI integration and cert-manager/control-plane service prerequisites; [ingress doc](https://docs.k0smotron.io/v2.3.0/ingress-support/) requires TLS passthrough. Do not set a single tool-wide SPDX or assume both current v1.10.10/v2.3.0 release lines share deployment/upgrade compatibility. Keep `needs-review`; avoid undocumented support assertions. |
| **CLEAR** | `k3d` | [v5.9.0 LICENSE MIT](https://github.com/k3d-io/k3d/blob/v5.9.0/LICENSE), [v5.9.0 release](https://github.com/k3d-io/k3d/releases/tag/v5.9.0), [upstream docs](https://k3d.io/). This is a local **k3s-in-Docker wrapper**, not a distinct hardened production cluster implementation. Protect Docker socket and credential exposure; verify k3s/Kubernetes versions before specifying images. |
| **CLEAR** | `kubeadm` | Current `kubernetes/kubeadm` [README](https://github.com/kubernetes/kubeadm/blob/main/README.md) confirms **issue-only aggregator**; immutable [Kubernetes v1.35.0 source](https://github.com/kubernetes/kubernetes/blob/v1.35.0/cmd/kubeadm/kubeadm.go) and [v1.35.0 LICENSE Apache-2.0](https://github.com/kubernetes/kubernetes/blob/v1.35.0/LICENSE) establish ownership and source. [Official kubeadm docs](https://kubernetes.io/docs/reference/setup-tools/kubeadm/) explicitly delimit `init`, `join`, `upgrade` and exclude provisioning machines/add-ons. Propose updating canonical `repository_url` to **https://github.com/kubernetes/kubernetes** and recording precise source path + former issue aggregator as evidence; preserve all legacy `sources`. |
| **CLEAR** | `microk8s` | [Canonical v1.36 LICENSE Apache-2.0](https://github.com/canonical/microk8s/blob/v1.36/LICENSE), [release](https://github.com/canonical/microk8s/releases/tag/v1.36), [official MicroK8s](https://microk8s.io/). Lightweight packaged Kubernetes; actual Snap tracks, OS support, HA/worker layout and add-on privileges depend on installations, not solely the GitHub tag. |
| **CLEAR** | `rancher-k3k` | [Stable application v1.2.0 LICENSE Apache-2.0](https://github.com/rancher/k3k/blob/v1.2.0/LICENSE), [tagged README](https://github.com/rancher/k3k/blob/v1.2.0/README.md) and [official 1.2.0 architecture/security docs](https://rancher.github.io/k3k-product-docs/k3k/1.2.0/en/architecture.html). GitHub `v1.2.1-rc2` and chart-prefixed `chart-1.2.1-rc2` are **not** production-stable releases merely because a chart object has `prerelease:false`. Shared-mode isolation depends on NetworkPolicy/PSA/CNI enforcement; virtual agents may carry host privileges. SUSE Rancher Prime enterprise management is a **separate commercial product**, not part of this OSS source-grant decision. |
| **CLEAR** | `typhoon` | [v1.36.1 LICENSE MIT](https://github.com/poseidon/typhoon/blob/v1.36.1/LICENSE), [release](https://github.com/poseidon/typhoon/releases/tag/v1.36.1), [official docs](https://typhoon.psdn.io/). Terraform-managed provisioning of Kubernetes is distinct from upstream core kubeadm and from AWS CAPA; secure Terraform state, provider permissions and versions. |
| **CLEAR** | `kubeedge` | [v1.23.1 LICENSE Apache-2.0](https://github.com/kubeedge/kubeedge/blob/v1.23.1/LICENSE), [release](https://github.com/kubeedge/kubeedge/releases/tag/v1.23.1), [upstream docs](https://kubeedge.io/). Edge/cloud Kubernetes framework, **not a stand-alone one-node distro**; cloud-edge identity, trusted devices, certificate lifecycle and offline/cloud sync security require explicit deployment design. |
| **RETAIN REVIEW** | `kubesphere` | [v4.1.3 LICENSE](https://github.com/kubesphere/kubesphere/blob/v4.1.3/LICENSE) adds **specific restrictions to Apache-2.0** for third-party commercial/on-prem/cloud services and distribution, distinguishing 4.x from earlier 3.4.x. GitHub `NOASSERTION` cannot override that primary text. Existing `license_model: oss` is **misleading for v4.x**; propose **`license_model: source-available`** with clear edition/version warnings, but **no exact OSS SPDX** and **retain needs-review** pending ownership/grant/support confirmation. Do not infer a licence blessing from source availability. |
| **CLEAR** | `kubesolo` | [v1.2.2 LICENSE MIT](https://github.com/portainer/kubesolo/blob/v1.2.2/LICENSE), [tagged README](https://github.com/portainer/kubesolo/blob/v1.2.2/README.md), [release](https://github.com/portainer/kubesolo/releases/tag/v1.2.2). **Fix outdated catalogue description:** modern KubeSolo is a **minimal single-node Kubernetes implementation for Linux-based edge and servers**, also providing a **container mode** for development hosts including macOS/WSL2 — not a macOS-native Kubernetes IDE. Strict single-node, no multi-node/HA, do not assert marketing performance or conformance claims as independently measured. |

**License/edition interpretation:** `license_spdx` identifies *verified, scoped software source* of the eight CLEAR records, not bundled third-party dependencies or vendors' managed offerings: `Apache-2.0` for CAPA, kubeadm (upstream Kubernetes code), MicroK8s, Rancher k3k and KubeEdge; `MIT` for k3d, Typhoon and KubeSolo. No `license_spdx` for k0smotron/KubeSphere while retained. `license_model` remains `oss` for the eight clear records; KubeSphere changes to `source-available` only because tagged 4.x adds commercially restrictive conditions, and stays in review.

### Explicit planned canonical edits (subject to LOCAL VERIFICATION)

- **Eight CLEAR IDs**: `status: active`, `needs_review: false`, source-verified software `license_spdx` as above, precise `summary` and `avoid_when`, `verified_on: '2026-10-26'`, additive versioned primary source URLs.
- **Two RETAIN REVIEW IDs**: `status: needs-review`, `needs_review: true`, no `license_spdx` added. Add verified caveats and official URLs, date. For **KubeSphere** correct the outdated `license_model: oss` to `source-available` with a version-specific explanation and explicit restrictions. For **k0smotron**, describe code/docs licence split but do not flatten into a tool-wide SPDX.
- **Identity correction**: `kubeadm.repository_url` changes from the GitHub **issue aggregator** `https://github.com/kubernetes/kubeadm` to the actual source repository `https://github.com/kubernetes/kubernetes`; add links to both current source and former tracker in its `sources`. The canonical `id` stays `kubeadm`.
- **Product correction**: `kubesolo.summary` moves away from a macOS-native application to the verified single-node implementation and developer container mode. Do not invent OS conformance or performance claims.
- **No other canonical changes**: preserve all **142** record IDs/order, all **132** nonselected records, all historical source entries and existing categories/subcategories/roles/lifecycle. No Python constraints, URL baseline or security workflow edits.
- **Predicted, NOT observed until official generation + QA:** **1,425** canonical, **808 active**, **603 needs-review**, 142 in this category, **51** remaining needs-review in this category. Licence-model category total may change one `oss` → `source-available` because of KubeSphere; validate via generator.

### Next gates

Apply in clean branch `maintenance/wave-26-kubernetes-cluster-lifecycle-evidence-review` from this documentation checkpoint. Verify exact original YAML at pinned `main` and branch base. Before writing, present a dry-run field-level diff covering precisely the selected ten. Generate official views and append **actual** pre/post canonical data and local QA outcomes to the ledger. Run `python -m scripts.generate_docs`/`--check`, `validate_catalog`, Ruff lint/format, full pytest, pip check, git diff --check and strict 10/132 cohort comparison. Preserve 3.12 lock and the six historic URL exceptions. Commit/push only after verification and explicit human action; never alter main directly.

After push, require fresh all-7-check PR CI, completed independent Codex P1/P2 review on final SHA, and a fresh manually triggered strict Full link audit with `strict_result: PASS`, `blocking_new: 0`, six historic exception pairs unchanged. PR remains Draft, #143 open, #2 open. Only explicit human squash merge after all gates and post-merge verification may close #143.

### Duplicate repository URL correction — 2026-10-26

The original second-pass proposal pointed `kubeadm.repository_url` to the repository root
`https://github.com/kubernetes/kubernetes`. Local `scripts.validate_catalog` correctly rejected it: the existing
independent `kubernetes` record already owns this canonical root, and duplicate
`repository_url` values are forbidden. This follow-up chooses the accurate, unique
**source subdirectory link** `https://github.com/kubernetes/kubernetes/tree/master/cmd/kubeadm` for kubeadm. Both records still
refer to one Kubernetes upstream repository (not two different repositories).
The former `kubernetes/kubeadm` issue-tracker URL and immutable tagged
`v1.35.0/cmd/kubeadm` source remain documented in kubeadm `sources`.
The 8 CLEAR / 2 RETAIN decisions, original IDs, licences, 132 untouched records,
counts, baseline exceptions and date remain unchanged. The prior proposal is kept
above as historical context; the regenerated applied field-level table below is
now authoritative for the actual local values.

<!-- WAVE26_APPLIED_CANONICAL_CHANGELOG_START -->
## Local canonical application — Wave 26 field-level evidence log

**Status:** Canonical changes applied locally, official regeneration/QA and fresh PR CI pending until actually observed. The first-pass and second-pass recommendations above are historical checkpoints.

**Decisions applied to local canonical records:** 8 CLEAR / 2 RETAIN REVIEW. The catalogue-level expected inventory after official generation is 1,425 canonical, 808 active, 603 needs-review, subject to generator and CI validation.

| Decision | IDs |
|---|---|
| CLEAR | `cluster-api-provider-aws`, `k3d`, `kubeadm`, `kubeedge`, `kubesolo`, `microk8s`, `rancher-k3k`, `typhoon` |
| RETAIN REVIEW | `k0smotron`, `kubesphere` |

All 132 non-cohort YAML records are unchanged byte-for-byte after line-ending normalization; original historical sources, taxonomy, role and lifecycle fields are preserved. No constraints or URL audit baseline update is authorized.

### `cluster-api-provider-aws` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>[]</code> | <code>["You cannot secure AWS IAM, network provisioning costs or align CAPI/CAPA compatibility versions."]</code> |
| `license_spdx` | <code>null</code> | <code>"Apache-2.0"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:devopstools_final.md#L454"]</code> | <code>["legacy:devopstools_final.md#L454", "https://github.com/kubernetes-sigs/cluster-api-provider-aws/blob/v2.13.1/LICENSE", "https://github.com/kubernetes-sigs/cluster-api-provider-aws/releases/tag/v2.13.1", "https://cluster-api-aws.sigs.k8s.io/"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Kubernetes-native declarative infrastructure provider for creating and operating self-managed and EKS clusters on AWS."</code> | <code>"Kubernetes Cluster API infrastructure provider for AWS self-managed Kubernetes clusters and EKS integrations."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/kubernetes-sigs/cluster-api-provider-aws/blob/v2.13.1/LICENSE
- https://github.com/kubernetes-sigs/cluster-api-provider-aws/releases/tag/v2.13.1
- https://cluster-api-aws.sigs.k8s.io/


### `k0smotron` — RETAIN REVIEW

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>[]</code> | <code>["You need one confirmed licence for software and documentation or have not validated k0s/CAPI compatibility and hosted control-plane isolation."]</code> |
| `sources` | <code>["legacy:devopstools_final.md#L464"]</code> | <code>["legacy:devopstools_final.md#L464", "https://github.com/k0sproject/k0smotron/blob/v2.3.0/LICENSE", "https://github.com/k0sproject/k0smotron/releases/tag/v2.3.0", "https://docs.k0smotron.io/"]</code> |
| `summary` | <code>"Kubernetes operator and Cluster API provider for managing hosted k0s control planes and child clusters inside Kubernetes."</code> | <code>"Hosted k0s control-plane operator and Cluster API integration with separate software and documentation licences."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/k0sproject/k0smotron/blob/v2.3.0/LICENSE
- https://github.com/k0sproject/k0smotron/releases/tag/v2.3.0
- https://docs.k0smotron.io/


### `k3d` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>[]</code> | <code>["You require production high availability or cannot secure the local Docker socket and host resources."]</code> |
| `license_spdx` | <code>null</code> | <code>"MIT"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:devopstools_final.md#L434"]</code> | <code>["legacy:devopstools_final.md#L434", "https://github.com/k3d-io/k3d/blob/v5.9.0/LICENSE", "https://github.com/k3d-io/k3d/releases/tag/v5.9.0", "https://k3d.io/"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Lightweight wrapper to run k3s (Rancher Lab's minimal Kubernetes distribution) in Docker."</code> | <code>"Docker-based local cluster wrapper running the lightweight k3s Kubernetes distribution."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/k3d-io/k3d/blob/v5.9.0/LICENSE
- https://github.com/k3d-io/k3d/releases/tag/v5.9.0
- https://k3d.io/


### `kubeadm` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["A managed service (EKS/GKE/AKS) or lightweight distro (k3s) would reduce operational burden."]</code> | <code>["A managed service (EKS/GKE/AKS) or lightweight distro (k3s) would reduce operational burden.", "You expect kubeadm alone to provision machines, networking, storage or a complete managed Kubernetes service."]</code> |
| `license_spdx` | <code>null</code> | <code>"Apache-2.0"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `repository_url` | <code>"https://github.com/kubernetes/kubeadm"</code> | <code>"https://github.com/kubernetes/kubernetes/tree/master/cmd/kubeadm"</code> |
| `sources` | <code>["legacy:4_Kubernetes-Containers/README.md#L7", "legacy:devopstools_final.md#L436"]</code> | <code>["legacy:4_Kubernetes-Containers/README.md#L7", "legacy:devopstools_final.md#L436", "https://github.com/kubernetes/kubeadm/blob/main/README.md", "https://github.com/kubernetes/kubernetes/blob/v1.35.0/cmd/kubeadm/kubeadm.go", "https://github.com/kubernetes/kubernetes/blob/v1.35.0/LICENSE", "https://kubernetes.io/docs/reference/setup-tools/kubeadm/"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Tool for bootstrapping Kubernetes clusters."</code> | <code>"Upstream Kubernetes bootstrap and upgrade CLI for creating and managing control-plane and worker node configuration."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/kubernetes/kubeadm/blob/main/README.md
- https://github.com/kubernetes/kubernetes/blob/v1.35.0/cmd/kubeadm/kubeadm.go
- https://github.com/kubernetes/kubernetes/blob/v1.35.0/LICENSE
- https://kubernetes.io/docs/reference/setup-tools/kubeadm/


### `kubeedge` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["Your edge devices are too resource-constrained or a simpler agent model (e.g., k3s) suffices."]</code> | <code>["Your edge devices are too resource-constrained or a simpler agent model (e.g., k3s) suffices.", "You cannot manage cloud-edge identities, certificate lifecycle, connectivity loss and device trust boundaries."]</code> |
| `license_spdx` | <code>null</code> | <code>"Apache-2.0"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:4_Kubernetes-Containers/README.md#L10", "legacy:devopstools_final.md#L439"]</code> | <code>["legacy:4_Kubernetes-Containers/README.md#L10", "legacy:devopstools_final.md#L439", "https://github.com/kubeedge/kubeedge/blob/v1.23.1/LICENSE", "https://github.com/kubeedge/kubeedge/releases/tag/v1.23.1", "https://kubeedge.io/"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Extend Kubernetes to edge computing."</code> | <code>"Kubernetes-native edge computing framework connecting cloud control planes with edge devices and nodes."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/kubeedge/kubeedge/blob/v1.23.1/LICENSE
- https://github.com/kubeedge/kubeedge/releases/tag/v1.23.1
- https://kubeedge.io/


### `kubesolo` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>[]</code> | <code>["You need multi-node scheduling or high availability, or assume a native macOS IDE rather than a single-node Kubernetes runtime."]</code> |
| `license_spdx` | <code>null</code> | <code>"MIT"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:devopstools_final.md#L442"]</code> | <code>["legacy:devopstools_final.md#L442", "https://github.com/portainer/kubesolo/blob/v1.2.2/LICENSE", "https://github.com/portainer/kubesolo/blob/v1.2.2/README.md", "https://github.com/portainer/kubesolo/releases/tag/v1.2.2"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Native macOS application to run a local Kubernetes cluster."</code> | <code>"Lightweight single-node Kubernetes implementation for edge and server hosts, with container-mode use for development."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/portainer/kubesolo/blob/v1.2.2/LICENSE
- https://github.com/portainer/kubesolo/blob/v1.2.2/README.md
- https://github.com/portainer/kubesolo/releases/tag/v1.2.2


### `kubesphere` — RETAIN REVIEW

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["You prefer composing best-of-breed tools (ArgoCD + Grafana + etc.)."]</code> | <code>["You prefer composing best-of-breed tools (ArgoCD + Grafana + etc.).", "You require unmodified OSI Apache-2.0 licence permissions for KubeSphere v4.x or intend third-party commercial redistribution without authorization."]</code> |
| `license_model` | <code>"oss"</code> | <code>"source-available"</code> |
| `sources` | <code>["legacy:4_Kubernetes-Containers/README.md#L57", "legacy:devopstools_final.md#L511"]</code> | <code>["legacy:4_Kubernetes-Containers/README.md#L57", "legacy:devopstools_final.md#L511", "https://github.com/kubesphere/kubesphere/blob/v4.1.3/LICENSE", "https://github.com/kubesphere/kubesphere/releases/tag/v4.1.3", "https://kubesphere.io/"]</code> |
| `summary` | <code>"Kubernetes multi-tenant management platform."</code> | <code>"Kubernetes multi-tenant management platform; KubeSphere 4.x imposes additional commercial-use and distribution restrictions."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/kubesphere/kubesphere/blob/v4.1.3/LICENSE
- https://github.com/kubesphere/kubesphere/releases/tag/v4.1.3
- https://kubesphere.io/


### `microk8s` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["You need wider community tooling compatibility or prefer non-snap packaging."]</code> | <code>["You need wider community tooling compatibility or prefer non-snap packaging.", "You assume every Snap track or optional add-on offers identical version, architecture or production HA support."]</code> |
| `license_spdx` | <code>null</code> | <code>"Apache-2.0"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:4_Kubernetes-Containers/README.md#L163", "legacy:devopstools_final.md#L665"]</code> | <code>["legacy:4_Kubernetes-Containers/README.md#L163", "legacy:devopstools_final.md#L665", "https://github.com/canonical/microk8s/blob/v1.36/LICENSE", "https://github.com/canonical/microk8s/releases/tag/v1.36", "https://microk8s.io/"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Lightweight Kubernetes by Canonical."</code> | <code>"Canonical-packaged lightweight Kubernetes distribution with Snap tracks and optional add-ons."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/canonical/microk8s/blob/v1.36/LICENSE
- https://github.com/canonical/microk8s/releases/tag/v1.36
- https://microk8s.io/


### `rancher-k3k` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["Vcluster or Kamaji already handles your virtual cluster needs."]</code> | <code>["Vcluster or Kamaji already handles your virtual cluster needs.", "You need a hard tenant security boundary without verifying privileged agent pods, host isolation and the shared-mode policy model.", "You plan to treat chart 1.2.1 release candidates as a stable GA application version."]</code> |
| `license_spdx` | <code>null</code> | <code>"Apache-2.0"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:4_Kubernetes-Containers/README.md#L167", "legacy:devopstools_final.md#L669"]</code> | <code>["legacy:4_Kubernetes-Containers/README.md#L167", "legacy:devopstools_final.md#L669", "https://github.com/rancher/k3k/blob/v1.2.0/LICENSE", "https://github.com/rancher/k3k/blob/v1.2.0/README.md", "https://github.com/rancher/k3k/releases/tag/v1.2.0"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Run and manage k3s clusters via Kubernetes (see docs)."</code> | <code>"Kubernetes-in-Kubernetes control-plane tooling for shared or virtual k3s guest clusters."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/rancher/k3k/blob/v1.2.0/LICENSE
- https://github.com/rancher/k3k/blob/v1.2.0/README.md
- https://github.com/rancher/k3k/releases/tag/v1.2.0


### `typhoon` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>[]</code> | <code>["You cannot safeguard Terraform state and provider credentials or verify cloud provider and Kubernetes version compatibility."]</code> |
| `license_spdx` | <code>null</code> | <code>"MIT"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:devopstools_final.md#L672"]</code> | <code>["legacy:devopstools_final.md#L672", "https://github.com/poseidon/typhoon/blob/v1.36.1/LICENSE", "https://github.com/poseidon/typhoon/releases/tag/v1.36.1", "https://typhoon.psdn.io/"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Minimal, Terraform-based Kubernetes distribution for cloud and bare-metal platforms."</code> | <code>"Minimal Kubernetes distribution and Terraform provisioning toolkit for cloud and bare-metal clusters."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/poseidon/typhoon/blob/v1.36.1/LICENSE
- https://github.com/poseidon/typhoon/releases/tag/v1.36.1
- https://typhoon.psdn.io/


**Publication checkpoint:** This local change log is not itself evidence of test/CI completion. After the official local generator and full QA pass, review the final diff, push through an explicit human-authorized commit, obtain fresh PR CI + independent P1/P2 review and a new strict full URL audit on the exact final SHA before a human merge decision.
<!-- WAVE26_APPLIED_CANONICAL_CHANGELOG_END -->
