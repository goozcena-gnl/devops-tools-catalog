# Garage WebUI — archival metadata and URL fragments (2026-11-23)

## Evidence and baseline

- Exact integration base: `f3ce11da35969d9ff917cd6903e1e678dfcb223f`, original canonical YAML blob `99b53c66f96c33ff84c4fbe0769484b5606e0c9a`.
- Official [Garage WebUI repository](https://github.com/khairul169/garage-webui) and [GitHub REST API](https://api.github.com/repos/khairul169/garage-webui) report `archived: true` (checked 2026-11-23). This establishes repository archiving only, not the current status of upstream Garage or every deployed copy of the UI.
- [Wave 45 PR #199](https://github.com/goozcena-gnl/devops-tools-catalog/pull/199), exact HEAD `889b4b47235266d314a7f9cc7da52c01206c7b28`, stays Draft and untouched; its canonical databases file is byte-identical to this correction base.
- [Strict Full Link Audit #101](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/45067928860): `blocking_new: 2`, `blocking_known: 6`, `strict_result: FAIL`, `baseline_changed: []`, `baseline_resolved: []`. The new blockers are the repository URL and the same URL with `#readme`.

## Exact correction scope

- Only `garage-webui.repository_archived` changes: `false` to `true`. Preserve all other tools, identity fields, `status: active`, `needs_review: false`, `verified_on`, existing `license_model: oss` and `license_spdx: MIT`. No new inference about product lifecycle or licence.
- Update `scripts/check_links.py` so a GitHub URL with a **nonempty fragment** can inherit `repository_archived` only where the URL without its fragment exactly matches a canonical `repository_url`. This must not introduce owner-wide, host-wide or arbitrary subpath waivers.
- Add targeted `tests/test_links.py` cases for matching `#readme`, absent archive metadata, mixed canonical metadata and unrelated GitHub subpaths.
- The generator also requires two derived outputs: `README.md` (archived source repository count 15 → 16) and `docs/categories/databases-caching-data-infrastructure.md` (Garage WebUI archive label). These are deterministic `scripts.generate_docs` outputs from the canonical YAML change. This evidence note remains the only newly created path. The six-path combined PR scope is: canonical YAML, link checker, link tests, these two generated outputs and this note. Do not modify `config/link-audit-baseline.json`, unrelated lifecycle/role views, licence fields or catalogue statistics.

## CI follow-up

- Initial PR #200 CI run [Catalogue quality #490](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/45140711396) failed solely at `ruff format --check scripts tests`, reporting two long assertions in `tests/test_links.py`. No tests or generated-doc checks ran in that failed job. The follow-up commit reformats only those assertions and updates the two deterministic generated views. Fresh CI on the new SHA is mandatory.

## Required independent gates (not preemptively PASS)

1. Confirm the initial exact-base commit plus the follow-up formatting/generated-doc correction commit, with the six-path combined PR allowlist; all unrelated blobs unchanged.
2. Run locked Python 3.12 dependency checks, Ruff check/format, full pytest, generated documentation validation, catalogue validation and Git whitespace checks on the exact correction SHA.
3. Run independent strict `link-check.yml` on correction SHA, inspect published JSON and Markdown: expect `blocking_new: 0` and `strict_result: PASS` if no other external link drift; independently examine `blocking_known`, `baseline_changed`, `baseline_resolved`.
4. Human review before any merge. Keep correction PR and Wave 45 PR #199 OPEN/DRAFT, no merge, auto-merge, tag, release, baseline waiver or branch deletion.
