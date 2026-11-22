# Wave 43 — container runtimes and local virtualization evidence review

- Scope freeze: **2026-11-22**, [issue #194](https://github.com/goozcena-gnl/devops-tools-catalog/issues/194).
- Baseline protected `main`: `896502dfd60a4d961f556999fa9aeacc5da1d266`; category blob: `041f28e9b0d102fde38b6433cd8bc859791bcd6e`.
- Exactly **68** canonical records, **33** flagged `needs_review: true`; **eight** evidence/documentation candidates updated, **58** raw YAML records preserved byte-for-byte (56 unselected + RETAIN `dockur-windows` / `dockur-macos`).
- No canonical status, `needs_review`, maturity, `verified_on`, licence model, roles, taxonomy, lifecycle assignments, official site URL, or historical `legacy:` source changed.
- Exactly five code-scoped SPDX additions: `lazydocker` = MIT; `nerdctl`, `podman`, `rootlesskit`, `runc` = Apache-2.0. `kcli` retains an unset canonical `license_spdx` under the historical N1a test-protected decision; its Apache-2.0 upstream LICENSE is recorded as evidence, not promoted into the canonical field. `ctop` retains existing MIT. **gVisor retains NO product-wide SPDX**, because its official root LICENSE explicitly provides Apache-2.0 alongside MIT/BSD exceptions for individually marked files.
- The original `google/gvisor` and `containers/podman` repository URLs have moved to the verified upstream paths `gvisor/gvisor` and `podman-container-tools/podman`; this change updates only their canonical `repository_url` and appends pinned first-party evidence.

## Eight review outcomes and primary sources

| Canonical ID | Bounded correction | Direct evidence at exact upstream commit |
|---|---|---|
| `ctop` | Docker/runc metrics TUI; documented runtime connector and socket access; source MIT already set | [README](https://github.com/bcicen/ctop/blob/59f00dd6aaebf48f3bc501e174f75f815c2619f0/README.md), [LICENSE](https://github.com/bcicen/ctop/blob/59f00dd6aaebf48f3bc501e174f75f815c2619f0/LICENSE) |
| `gvisor` | userspace application kernel/runsc isolation and workload compatibility; mixed Apache/MIT/BSD source exceptions; no global SPDX | [README](https://github.com/gvisor/gvisor/blob/eb263e1f414d0bceaf10decea6c73e2c77332112/README.md), [LICENSE](https://github.com/gvisor/gvisor/blob/eb263e1f414d0bceaf10decea6c73e2c77332112/LICENSE) |
| `lazydocker` | Docker/Compose TUI; daemon access and known in-container metric/log limits; MIT source | [README](https://github.com/jesseduffield/lazydocker/blob/596fd59df6b088bb1e38c5bb08cd4fbf28b3ebfb/README.md), [LICENSE](https://github.com/jesseduffield/lazydocker/blob/596fd59df6b088bb1e38c5bb08cd4fbf28b3ebfb/LICENSE) |
| `nerdctl` | CLI for containerd, Compose; optional BuildKit/rootless dependencies; Apache-2.0 source | [README](https://github.com/containerd/nerdctl/blob/52b705e52dc873da6db3b1d05c4ea352f7c167ab/README.md), [LICENSE](https://github.com/containerd/nerdctl/blob/52b705e52dc873da6db3b1d05c4ea352f7c167ab/LICENSE) |
| `podman` | Linux daemonless/rootless engine with VM-backed non-Linux clients; Apache-2.0 source; repository relocation | [README](https://github.com/podman-container-tools/podman/blob/06bc48f486720aa5d6ea6d24e22a0bec325d49a5/README.md), [LICENSE](https://github.com/podman-container-tools/podman/blob/06bc48f486720aa5d6ea6d24e22a0bec325d49a5/LICENSE) |
| `rootlesskit` | Linux user/mount/network namespace plumbing for rootless engines, not full engine; Apache-2.0 source | [README](https://github.com/rootless-containers/rootlesskit/blob/5ee9a26bc30ac5ca5b13928eede9ad4168fb053a/README.md), [LICENSE](https://github.com/rootless-containers/rootlesskit/blob/5ee9a26bc30ac5ca5b13928eede9ad4168fb053a/LICENSE) |
| `runc` | Linux-only OCI runtime CLI, not orchestrator; Apache-2.0 source | [README](https://github.com/opencontainers/runc/blob/e86228d9034ffde0c11296eeb31bd781cd2db86f/README.md), [LICENSE](https://github.com/opencontainers/runc/blob/e86228d9034ffde0c11296eeb31bd781cd2db86f/LICENSE) |
| `kcli` | VM and Kubernetes environment provisioning across libvirt/vSphere/cloud providers; Apache-2.0 source | [README](https://github.com/karmab/kcli/blob/1fdde9a5c03ade3eae7fcc2d6942df5cb387d3f8/README.md), [LICENSE](https://github.com/karmab/kcli/blob/1fdde9a5c03ade3eae7fcc2d6942df5cb387d3f8/LICENSE) |

## RETAIN — entire canonical blocks protected

- `dockur-windows` — code licence in the Dockur repository does not determine Windows guest OS licensing, activation or permitted deployment; no field changed.
- `dockur-macos` — code licence in the Dockur repository does not determine macOS guest OS/host-virtualization rights; no field changed.

## Validation evidence and explicit missing steps

- **Historical N1a guard repaired after first CI:** Catalogue quality run [45004391589](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/45004391589) reported two related pytest failures in `tests/test_v022_n1a_access_retry.py`: `kcli.license_spdx` was originally unset and remains N1a-protected. Fixed the proposed YAML by removing only that new SPDX assignment; no test guard was weakened, no other raw record edited. Revalidate on the new exact PR SHA; this paragraph alone is not a PASS claim.
- **Performed before publication using the exact GitHub source blobs:** 68/33 preflight; eight selected IDs; eight field allowlists; 58/58 untouched raw YAML blocks; generated category section parity and deploy/operate summary parity against the repository's `scripts.generate_docs` renderer; exact source-commit README and LICENSE fetches for all eight upstreams. These are static checks, **not a substitute for the actual Python validation commands**.
- The exact command `python -m scripts.review_debt --format json` has **NOT RUN** in a local pinned repository worktree; the GitHub connection is a read/write API connector, not a Python runner. Do not assert review-debt PASS based on category counts or the existing `docs/catalog-statistics.json`.
- Also **NOT RUN locally**: `python -m scripts.generate_docs`, `python -m scripts.validate_catalog`, `python -m scripts.generate_docs --check`, `python -m pytest`, `python -m ruff check scripts tests`, `python -m ruff format --check scripts tests`, `git diff --check`. Require actual execution records before human review; GitHub's `Catalogue quality` workflow provides independent checks when the Draft PR is published.
- Strict Full Link Audit must be independently dispatched on the **exact Wave 43 PR HEAD**, with `blocking_new: 0` and `strict_result: PASS`; do not reuse Wave 42's previous run. Retain baseline blockers explicitly.

## Publication and decision gate

**DRAFT ONLY.** No code/status uplift, merge, auto-merge, Ready-for-Review promotion, tag, release, branch deletion, issue closure, or action on open external PR #132. Human approval is a separate decision.
