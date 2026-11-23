# Wave 45 — post-Garage WebUI integration provenance (2026-11-23)

## Scope and immutable inputs

- Integration target: protected `main` at `0d2b72cd037cce9efd6e44a7a26dfdb2c5b013b7` (single parent of this integration commit).
- Original Wave 45 evidence source: [PR #199](https://github.com/goozcena-gnl/devops-tools-catalog/pull/199), OPEN/DRAFT at `889b4b47235266d314a7f9cc7da52c01206c7b28`. Its original parent is `f3ce11da35969d9ff917cd6903e1e678dfcb223f`.
- Independent Garage WebUI correction: [PR #200](https://github.com/goozcena-gnl/devops-tools-catalog/pull/200), merged by squash into `main` as `0d2b72cd037cce9efd6e44a7a26dfdb2c5b013b7`.
- The four Wave 45 files already on `main` have the same Git blob IDs as on the original parent of PR #199. The original Wave 45 maintenance note is absent from `main`.
- This integration reuses **exactly** the five original Wave 45 Git blobs, without rewriting them. This new provenance note is the only additional changed path.

| Preserved Wave 45 path | Exact original Git blob SHA |
| --- | --- |
| `data/tools/application-cloud-security.yaml` | `8a4c4315e05578196175c6735cacf03422751401` |
| `docs/categories/application-cloud-security.md` | `e651baae16a4e32db9c92385087bb71d7fe3edb7` |
| `docs/lifecycle/secure.md` | `855518ffd3b3822de5b4feddee054f4b13feb81e` |
| `docs/lifecycle/test.md` | `8ad1c39c0a3e14518b077f76d2b95cb2cb8081bd` |
| `docs/maintenance/2026-11-22-wave-45-cloud-native-security-evidence-review.md` | `7aa19eb1daf6507e4248cea3a2ad67109d25a73c` |

## Evidence retained, boundaries not relaxed

The [original Wave 45 evidence ledger](2026-11-22-wave-45-cloud-native-security-evidence-review.md) retains the nine-record cohort, pinned official sources and 164 byte-identical protected YAML blocks. The nine selected records change only `summary`, `use_when`, `avoid_when`, `deployment_models`, `documentation_url` and `sources`. The `tetragon` record is RETAIN. No inferred SPDX, licence change, verification-date refresh, lifecycle/status revision or baseline waiver is added by this integration.

The [Wave 45 Full Link Audit #101](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/45067928860) on the original PR #199 SHA returned `blocking_new: 2` and `strict_result: FAIL` solely for the Garage WebUI repository URL and its `#readme` fragment. The source Wave 45 files did not touch Garage WebUI.

The independent [Garage WebUI audit #102](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/45142680826) and post-merge [main audit #103](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/45148421140) both reported `blocking_new: 0`, `blocking_known: 6`, `strict_result: PASS`. These results validate the correction and the new base separately; **neither is a substitute for a strict Full Link Audit on the new combined Wave 45 integration SHA**.

## Validation gates — pending until demonstrated on this exact commit

1. Confirm this is a single-parent commit on the frozen `main` SHA with a six-file allowlist; verify the five preserved blobs and all unrelated files remain byte-identical to the integration base.
2. On Python 3.12 with `config/python-constraints-3.12.txt`, run `python -m scripts.python_constraints --verify-locked`, `python -m pip check`, Ruff check/format, the complete pytest suite, `python -m scripts.generate_docs --check` and `python -m scripts.validate_catalog`.
3. Verify all seven exact-SHA CI check runs (validate, gitleaks, Plumber audit, Plumber, CodeQL, Analyze (python), Analyze (actions)).
4. Dispatch and inspect `link-check.yml` on the integration branch and exact SHA. Require `blocking_new: 0`, `strict_result: PASS`, and independently inspect `blocking_known`, `baseline_changed`, `baseline_resolved` and published JSON/Markdown artifacts.
5. Request an independent human review. Preserve original [PR #199](https://github.com/goozcena-gnl/devops-tools-catalog/pull/199) OPEN/DRAFT at its original SHA. Keep this new integration PR OPEN/DRAFT until explicit approval. No merge, auto-merge, tag, release, branch deletion or baseline change.

Any future `main` drift requires a new exact-base assessment; passing CI on an older SHA is not transferable.
