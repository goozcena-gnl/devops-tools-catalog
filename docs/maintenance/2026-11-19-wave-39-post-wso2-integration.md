# Wave 39 — post-WSO2 reconciliation (2026-11-19)

## Provenance and isolated scope

- Repository: `goozcena-gnl/devops-tools-catalog`.
- Frozen authoritative post-Ruff, post-WSO2 `main`: `7fc824af07a5394020b683895926400f70271e65`, squash merge of WSO2 PR [#187](https://github.com/goozcena-gnl/devops-tools-catalog/pull/187).
- Source integration Draft PR [#184](https://github.com/goozcena-gnl/devops-tools-catalog/pull/184), exact HEAD `e5d8cfa5f923f7f97d3b53ed46163de0affecce4`; original Wave 39 source Draft PR [#174](https://github.com/goozcena-gnl/devops-tools-catalog/pull/174), exact HEAD `34a4ae0a815885a4a802a6e13a93817ccbdd7e9d`.
- Original evidence and decisions: [Wave 39 issue #173](https://github.com/goozcena-gnl/devops-tools-catalog/issues/173) and `docs/maintenance/2026-11-13-wave-39-sre-incident-response-evidence-review.md`, retained from #184 verbatim.
- This is an integration-only Draft candidate. No tag, release, merge, auto-merge, issue closure, waiver, or change to original PRs.

## Field-level invariants

- The canonical `data/tools/sre-incident-response-on-call.yaml` Git blob is reproduced **identically** from PR #184: `fbdc84271ba47600459a0d3b52aa5f498f59613b`.
- Exactly **seven** reviewed canonical records change relative to this `main`: `combodo-itop`, `goalert`, `manageengine-netflow-analyzer`, `ntfy`, `server-pulse`, `wireshark`, `zenduty`. Their changes are bounded by the original evidence.
- Exactly **14/14 other raw YAML records stay byte-identical**, notably D1 `manageengine-it-operations-management`, D2 `moogsoft`, D3 `patchmon` (all RETAIN). No automatic CLEAR, `verified_on` refresh, lifecycle/status promotion, or unsupported product-wide SPDX classification.
- Canonical counts expected from frozen source YAML: 1,425 records / 30 categories; 874 active / 537 needs-review; licence-model counts commercial 178 / unknown 64 / open-core 111. These counts must be confirmed by the generator and validator after publication.

## Generated views and WSO2 collision

- Eight of the nine original PR #184 files, including the dated Wave 39 evidence ledger, reuse **exact source Git blob SHAs**, without rewriting source fields.
- The sole generated-file collision is `docs/lifecycle/operate.md`: carry over PR #184's Wave 39-derived lines and replace the one stale WSO2 rendered link with `https://github.com/wso2/api-platform`, the URL already present on merged `main`.
- This is a deterministic source-document reconciliation, **not a claim that the full documentation generator or test suite has been run locally**. GitHub CI must run `scripts.generate_docs --check` against the final exact PR commit and fail closed on any mismatch.
- `config/link-audit-baseline.json`, `config/python-constraints-3.12.txt`, `tests/test_wave4_candidate_reconciliation.py`, all WSO2 canonical records, and unrelated Wave 40/41 output remain unchanged from the frozen `main`.

## Required post-publication gates

1. Verify the actual new commit, parent, PR status Draft, exact 10-path allowlist, 7 changed / 14 preserved raw canonical records, protected files and WSO2 metadata untouched.
2. Require fresh exact-HEAD CI: Catalogue quality / Gitleaks / Plumber / CodeQL, full pytest, Ruff and generated-doc determinism; record results only after observed success.
3. Independently dispatch the strict Full link audit on this NEW branch/SHA; verify `blocking_new: 0`, `blocking_known: 6`, `strict_result: PASS`, `baseline_changed: []`, `baseline_resolved: []`, and retain JSON/Markdown evidence. Historical audit #85 on `main` is not a substitute.
4. Human field review and separate authorization before any transition to Ready for Review or merge; original Draft PRs #174/#184 and verification-only #180 remain untouched.

**Disposition: isolated Draft integration candidate only, no merger or review-state promotion.**
