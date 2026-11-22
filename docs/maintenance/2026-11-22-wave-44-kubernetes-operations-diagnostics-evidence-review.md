# Wave 44 — Kubernetes operational diagnostics and cluster inspection evidence review

- Issue: [#196](https://github.com/goozcena-gnl/devops-tools-catalog/issues/196); research date **2026-11-22**.
- Frozen source `main`: `37e7fa18e12c9344308b73e6b698f88405a2be85`; category original Git blob `b082153355b122b871a29d3d37d3b56e9b4868ec`.
- Exactly **142** raw records, **51** with `needs_review: true`; **nine** bounded documentation/evidence corrections. **133 protected raw blocks unchanged** (132 unselected and entire `k10ls` RETAIN).
- Protected all canonical ID/name/taxonomy/role/lifecycle/status/review/maturity/verification/identity/archive/licence fields; existing historical legacy sources remain intact.
- All nine official README and LICENSE source files were fetched directly at the immutable upstream revisions below. Their root licence texts support source-specific evidence, not blanket rights for third-party services or compatible deployments. No new `license_spdx` field added in this batch.

## Evidence and per-tool outcomes

| ID | Bounded documentary correction and caveat | Primary pinned evidence |
|---|---|---|
| `forecastle` | Namespace discovery, app URL visibility and end-user authorization; Apache-2.0 code | [README](https://github.com/stakater/Forecastle/blob/60137f4f3e190176f2434811385db240bfd23600/README.md), [LICENSE](https://github.com/stakater/Forecastle/blob/60137f4f3e190176f2434811385db240bfd23600/LICENSE) |
| `hanoi-cli` | Advisory simulation rather than automatic scheduling; Apache-2.0 code | [README](https://github.com/k-krew/hanoi-cli/blob/29c42b3675d3a3c2ee244eee6b9ead00b7d54a68/README.md), [LICENSE](https://github.com/k-krew/hanoi-cli/blob/29c42b3675d3a3c2ee244eee6b9ead00b7d54a68/LICENSE) |
| `k8s-d2` | D2 diagrams, optional remote SVG rendering and topology confidentiality; GPL v3 text exists but exact project only/or-later qualifier remains unverified | [README](https://github.com/vieitesss/k8s-d2/blob/6a31b5f6335c2a8f7d87d9700357294e8c94f703/README.md), [LICENSE](https://github.com/vieitesss/k8s-d2/blob/6a31b5f6335c2a8f7d87d9700357294e8c94f703/LICENSE) |
| `k8s-mechanic` | In-cluster agent and GitOps PR, scoped credentials/RBAC, human review and prompt-injection boundaries; existing Apache-2.0 unchanged | [README](https://github.com/lenaxia/k8s-mechanic/blob/a4cb60a8d911af568710ac43414410c40e5d7fe5/README.md), [LICENSE](https://github.com/lenaxia/k8s-mechanic/blob/a4cb60a8d911af568710ac43414410c40e5d7fe5/LICENSE) |
| `k8sql` | SQL/PRQL queries, multicluster/RBAC and PostgreSQL query endpoint; BSD-3-Clause code | [README](https://github.com/ndenev/k8sql/blob/9126a23daa29d35009a4f5e0363c1254c46854a1/README.md), [LICENSE](https://github.com/ndenev/k8sql/blob/9126a23daa29d35009a4f5e0363c1254c46854a1/LICENSE) |
| `k9sight` | TUI allows exec, delete, scale, restart and port-forward: NOT read-only; MIT code | [README](https://github.com/doganarif/k9sight/blob/00ce0851fac74e071987c113d8e82c2dcefdc904/README.md), [LICENSE](https://github.com/doganarif/k9sight/blob/00ce0851fac74e071987c113d8e82c2dcefdc904/LICENSE) |
| `kdash` | TUI permits delete/edit/restart/shell, requires appropriate RBAC; MIT code | [README](https://github.com/kdash-rs/kdash/blob/c30367346640266485ad4abdc662adb9c754dce2/README.md), [LICENSE](https://github.com/kdash-rs/kdash/blob/c30367346640266485ad4abdc662adb9c754dce2/LICENSE) |
| `kimspect` | Image inventory and namespace scope, NOT a CVE or SBOM scanner; Apache-2.0 code | [README](https://github.com/koithos/kimspect/blob/09df10ea59eeca64a8fe358e04f92c96e75d69be/README.md), [LICENSE](https://github.com/koithos/kimspect/blob/09df10ea59eeca64a8fe358e04f92c96e75d69be/LICENSE) |
| `kubetui` | Resource/log query surface, Kubernetes RBAC and sensitive logs; MIT code | [README](https://github.com/sarub0b0/kubetui/blob/352b08add9d8046c173ca195dd8a94a6e5100c50/README.md), [LICENSE](https://github.com/sarub0b0/kubetui/blob/352b08add9d8046c173ca195dd8a94a6e5100c50/LICENSE) |

## RETAIN: `k10ls`

- Official repository: [besrabasant/k10ls](https://github.com/besrabasant/k10ls), inspected at `f1a54a6096160d48f8bc16bc667b3b43625dd7f1`: README exists but no root LICENSE/COPYING; direct LICENSE fetch failed with 404.
- Entire canonical record frozen, including the preexisting `license_model: oss` and absent `license_spdx`. This freeze does not validate the old OSS assertion; a separate evidence/scope decision is needed to correct it.

## Checks performed versus pending

- **Verified statically in GitHub data:** exact frozen SHA and category blob, 142/51 record counts, nine precise changed IDs, strict changed-key allowlist, 133/133 byte-equal protected records, nine original generated category section exact-render parity checks, and 18 original generated deploy/operate line parity checks; all sources pinned to first-party upstream commits.
- Generated views were rewritten using the repository generator's verified string rendering rules; this is **not** a claim that the Python generator was executed locally.
- **NOT RUN locally:** `python -m scripts.review_debt --format json`, `python -m scripts.generate_docs`, `python -m scripts.generate_docs --check`, `python -m scripts.validate_catalog`, `python -m pytest`, Ruff lint and format, locked dependency verification, and `git diff --check`. The attempted local checkout could not resolve github.com DNS. No fabricated PASS.
- After Draft publication, require exact-SHA GitHub quality/security checks and independently dispatched strict Full Link Audit with `blocking_new: 0`, `strict_result: PASS`, known blockers recorded without baseline edits.
- No maturity, verified date, status, `needs_review` or licence promotion. Review/merge decisions remain for humans.

## Publication boundary

- Draft only; no merge, auto-merge, Ready promotion, tag, release, deleted branch, issue #196 closure, baseline issue #2 changes or alterations to external PR #132.
