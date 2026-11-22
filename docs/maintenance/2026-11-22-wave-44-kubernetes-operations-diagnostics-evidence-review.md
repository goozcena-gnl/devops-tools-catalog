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
- Generated views were **originally reconstructed using the generator's rendering rules** (before publishing the first Wave 44 commit). **Codex P1 correctly flagged the missing mandatory actual generator execution in that original process.** The maintainer subsequently executed `python -m scripts.generate_docs` and `python -m scripts.generate_docs --check` on an isolated, clean, detached Windows worktree at exact PR HEAD `5fc8702b1193bf52b9f20952320a33420e18ea18`. Both commands exited successfully and printed `Generated documentation is current.`; `git diff --check` also succeeded. `git status --short` and `git diff --stat` remained empty: **the actual canonical generator produced zero tracked-file changes**, including to the three previously reconstructed generated Markdown views. This evidence is taken from the maintainer-supplied terminal log, not a GitHub Actions artifact.
- **Locally executed on exact PR HEAD and reported PASS by the maintainer:** `python -m scripts.review_debt --format json` (1,425 canonical; 538 requiring review; 64 unknown licences; Kubernetes 152 memberships / 51 requiring review), `python -m scripts.generate_docs`, `python -m scripts.generate_docs --check`, and `git diff --check`. Exact remote SHA, detached worktree HEAD and clean initial state were verified before generator invocation. The earlier API-session attempt to clone failed due to GitHub DNS, but that does **not** negate the subsequent successful maintainer-side worktree execution.
- **Local generator evidence** (outside the Git repository): `C:\Users\bgian\Documents\ChatGPT\DevOps-Audit-Evidence\Wave44\generate-docs.log` and `generate-docs-check.log`; both show `Generated documentation is current.`. These local files were not uploaded as GitHub artifacts; GitHub independently validates the generated outputs with its `--check` CI gate.
- **Executed by the exact-head CI, not independently on the maintainer's worktree:** `python -m scripts.validate_catalog`, `python -m pytest` (1,008 passed / 4 skipped), Ruff lint and format and locked dependency checks; Catalogue quality run [#45021694549](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/45021694549) succeeded.
- **Original exact-HEAD verification completed:** 8/8 GitHub checks SUCCESS and independently dispatched [Full Link Audit #45022740184](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/45022740184), `blocking_new: 0`, `blocking_known: 6`, `strict_result: PASS`. **A new exact-HEAD CI and strict Full Link Audit are required after this ledger-only follow-up commit**, before resolving the Codex P1 and considering a merge.
- No maturity, verified date, status, `needs_review` or licence promotion. Review/merge decisions remain for humans.

## Publication boundary

- Originally published as a Draft; the maintainer subsequently promoted the PR to **Ready for Review**. This evidence-only correction does not alter that status. No merge, auto-merge, ruleset bypass, tag, release, branch deletion, issue #196 closure, baseline issue #2 changes or alterations to external PR #132.
