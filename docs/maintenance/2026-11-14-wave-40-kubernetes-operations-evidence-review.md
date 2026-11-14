# Wave 40 — Kubernetes operations evidence review

Inspected: **2026-11-14**. Planning and exact field freeze: [issue #175](https://github.com/goozcena-gnl/devops-tools-catalog/issues/175#issuecomment-6876017954).

- Frozen main: `62e33cfc0d4b682a65799e0b73d1c2c8bc71c154`; canonical blob: `e02f30ce3b90de0fcadbbb7b2e9f847239644613`.
- **142 canonical raw records**, **51 needing review** before and after. Nine bounded corrections; one selected RETAIN (`openlens`); 132 nonselected records remain byte-for-byte unchanged.
- All original `status`, `needs_review`, `maturity`, `verified_on`, IDs, names, categories, roles, stages, and `legacy:` entries are preserved. No lifecycle promotion.
- Source-scoped `license_spdx` is not a grant for hosted services, historical editions or paid binaries.
- Model counts after patch: 176 commercial / 65 unknown. Only the `lens` product classification changed.

## Field-level evidence

| ID | Limited decision | Primary source |
| --- | --- | --- |
| `kubectl` | Kubernetes CLI, GitOps-compatible manifests and client version skew; Apache-2.0 source | [Official docs](https://kubernetes.io/docs/reference/kubectl/), [LICENSE](https://github.com/kubernetes/kubernetes/blob/master/LICENSE) |
| `eks-node-viewer` | Pod **requests** vs allocatable capacity; optional cloud pricing IAM; Apache-2.0 source | [README](https://github.com/awslabs/eks-node-viewer), [LICENSE](https://github.com/awslabs/eks-node-viewer/blob/main/LICENSE) |
| `ingress2gateway` | Conversion is not automatically lossless; Apache-2.0 source | [README](https://github.com/kubernetes-sigs/ingress2gateway), [LICENSE](https://github.com/kubernetes-sigs/ingress2gateway/blob/main/LICENSE) |
| `k0smotron` | Hosted k0s control-plane/CAPI; software Apache-2.0, `docs/` CC-BY-SA-4.0 | [LICENSE](https://github.com/k0sproject/k0smotron/blob/main/LICENSE) |
| `k8s-cleaner-sveltos` | Controller can delete/transform; dry-run, RBAC; Apache-2.0 source | [README](https://github.com/gianlucam76/k8s-cleaner), [LICENSE](https://github.com/gianlucam76/k8s-cleaner/blob/main/LICENSE) |
| `khi-kubernetes-history-inspector` | Agentless log-derived timeline; clean canonical repository URL; Apache-2.0 | [README](https://github.com/GoogleCloudPlatform/khi), [LICENSE](https://github.com/GoogleCloudPlatform/khi/blob/main/LICENSE) |
| `kubectl-df-pv` | Compatible storage metrics/node RBAC required; AKS/EKS support not established; Apache-2.0 | [README](https://github.com/yashbhutwala/kubectl-df-pv), [LICENSE](https://github.com/yashbhutwala/kubectl-df-pv/blob/master/LICENSE) |
| `seabird` | MPL-2.0 source, separately described paid software/free trial, support cadence uncertain | [README](https://github.com/getseabird/seabird), [LICENSE](https://github.com/getseabird/seabird/blob/main/LICENSE) |
| `lens` | Current Mirantis Lens Desktop commercially licensed; retired MIT historical code distinct; no proprietary product SPDX inferred | [README](https://github.com/lensapp/lens), [Docs](https://docs.k8slens.dev/) |

## RETAIN

`openlens` fully unchanged. [Build repository](https://github.com/MuhammedKalkan/OpenLens) states no more updates; [latest examined release](https://github.com/MuhammedKalkan/OpenLens/releases/tag/v6.5.2-366) published 2023-06-30. Do not conflate binary releases with historical MIT source code, current commercial Lens, or another community fork.

## Verification gates

The staged change preserves the 133 protected raw blocks (132 unselected + OpenLens). Full local `generate_docs --check`, `validate_catalog`, review-debt, pytest, Ruff, strict exact-SHA link audit and GitHub CI are **NOT RUN** at authoring time; no PASS claim is made. Keep PR Draft, without merge/auto-merge/tag or issue closure, and leave PR #174 untouched.
