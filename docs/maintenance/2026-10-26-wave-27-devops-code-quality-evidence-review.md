# Wave 27 — DevOps code quality: selection and first-pass evidence

**2026-10-26. First-pass documentary triage only: 0 CLEAR applied / 10 RETAIN REVIEW pending deeper review.** This document also serves as a selection contract while issue creation awaits separate GitHub authorization. The repository's historical link-debt issue [#2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2) must remain open.

## Pinned baseline and invariants

- Base `main`: `33b4adadd16a74ed70816cc40861e9219ef9b3a6` (Wave 26 merged and four post-merge workflows passed).
- Generated totals: **1,425 canonical / 808 active / 603 needs-review** in 30 categories.
- Target single canonical file: `data/tools/developer-experience-local-environments.yaml`; original blob `b2bcf4e13e3732ed802a3e02df54200aabe77bcb`; **101 existing records, 54 needing review**. Exactly **10** IDs below are selected, and the **other 91** must remain logically unchanged and retain order.
- All selected IDs initially have `status: needs-review`, `needs_review: true`, `verified_on: 2026-08-03` and `license_model: oss`. **No canonical YAML edits are permitted in this initial documentary stage.**
- `config/link-audit-baseline.json` remains at `a834e2af711693def40078a55e31dfeb29bee2c7`, with six unchanged historical URL/classification exception pairs. Prior Wave 26 link audit #41 is not a substitute for a fresh Wave 27 audit on a final reviewed PR SHA.

## Fixed ten-tool cohort and primary-source evidence leads

The following checks were performed 2026-10-26 against upstream repositories and immutable tags. Source-file licences establish *candidate source-level grants*, not unconditional permissions for third-party plugins, binaries or bundled dependencies. **No CLEAR decisions are made here.**

| ID | Tagged primary-source observations | Required investigation before CLEAR |
|---|---|---|
| `actionlint` | [rhysd/actionlint](https://github.com/rhysd/actionlint), [v1.7.12](https://github.com/rhysd/actionlint/releases/tag/v1.7.12), [`LICENSE.txt` at v1.7.12](https://github.com/rhysd/actionlint/blob/v1.7.12/LICENSE.txt) **MIT** | Static GitHub Actions YAML/expression checker, not dynamic execution or complete security scanner. Verify feature coverage, third-party action metadata and ShellCheck integrations. |
| `black` | [psf/black](https://github.com/psf/black), [26.10.1](https://github.com/psf/black/releases/tag/26.10.1), [tagged LICENSE](https://github.com/psf/black/blob/26.10.1/LICENSE) **MIT** | Formatter versus linter distinction, Python grammar target, stability of formatting, interoperability with Ruff. |
| `eslint` | [eslint/eslint](https://github.com/eslint/eslint), [v10.13.0](https://github.com/eslint/eslint/releases/tag/v10.13.0), [tagged LICENSE](https://github.com/eslint/eslint/blob/v10.13.0/LICENSE) **MIT** | Catalogue lacks `repository_url`; add only after global uniqueness check. ESLint core primarily handles JavaScript; TypeScript needs appropriate parser/plugin/configuration. Check Node and flat config version support. |
| `golangci-lint` | [golangci/golangci-lint](https://github.com/golangci/golangci-lint), [v2.15.0](https://github.com/golangci/golangci-lint/releases/tag/v2.15.0), [tagged LICENSE](https://github.com/golangci/golangci-lint/blob/v2.15.0/LICENSE) full **GPL v3 text** | Exact `GPL-3.0-only` vs `GPL-3.0-or-later` not established from boilerplate alone; runner license versus included linters/plugins; v2 config migration and Go version support. |
| `hadolint` | [hadolint/hadolint](https://github.com/hadolint/hadolint), [v2.15.1](https://github.com/hadolint/hadolint/releases/tag/v2.15.1), [LICENSE](https://github.com/hadolint/hadolint/blob/v2.15.1/LICENSE) **GPL v3 text** | Confirm precise GPL scope/version, ShellCheck-related dependencies, Dockerfile syntax support and CI security practices. |
| `mypy` | [python/mypy](https://github.com/python/mypy), [v1.19.1 LICENSE](https://github.com/python/mypy/blob/v1.19.1/LICENSE): **MIT principal mypy/mypyc code**, with expressly separate PSF-2 and other licensed portions; repository metadata shows `NOASSERTION` | Scoped rather than blanket SPDX for the full tree; Python version, stubs/plugins and incremental/daemon behavior. GitHub Releases empty ≠ abandoned, version tag exists. |
| `prettier` | [prettier/prettier](https://github.com/prettier/prettier), [3.9.10](https://github.com/prettier/prettier/releases/tag/3.9.10), [tagged LICENSE](https://github.com/prettier/prettier/blob/3.9.10/LICENSE) **MIT** | Formatting not linting; supported parsers/Node runtime, plugin version and separately licensed ecosystem. |
| `ruff` | [astral-sh/ruff](https://github.com/astral-sh/ruff), [0.17.2](https://github.com/astral-sh/ruff/releases/tag/0.17.2), [tagged LICENSE](https://github.com/astral-sh/ruff/blob/0.17.2/LICENSE) **MIT principal code** | Rule/formatter coverage vs Flake8/Black/isort, plugin limitations, compatibility/preview mode and pinning. |
| `shfmt` | [mvdan/sh](https://github.com/mvdan/sh), [v3.14.1](https://github.com/mvdan/sh/releases/tag/v3.14.1), [tagged LICENSE](https://github.com/mvdan/sh/blob/v3.14.1/LICENSE) **BSD-3-Clause** | `shfmt` resides inside the `mvdan/sh` module, not an independent repository. Distinguish shell formatting from ShellCheck linting and support for POSIX/Bash/mksh/zsh variants. |
| `yamllint` | [adrienverge/yamllint](https://github.com/adrienverge/yamllint), [v1.38.0](https://github.com/adrienverge/yamllint/releases/tag/v1.38.0), [tagged LICENSE](https://github.com/adrienverge/yamllint/blob/v1.38.0/LICENSE) **GPL v3 text** | Precise GPL only/later determination, Python compatibility and config, YAML syntax/style checks **not** Kubernetes API/Helm/policy validation. |

## Required second-pass review and implementation gates

1. Verify first-party tagged licences, related NOTICE/source exceptions, releases/compatible runtimes, official docs, maintenance and adoption/security boundaries **for each ten ID independently**. Propose `CLEAR` or `RETAIN REVIEW` without quota. Explicitly adjudicate the GPL version, mypy multi-licence source scopes, ESLint core/TypeScript distinction and `repository_url` uniqueness.
2. Later modify **only these ten** existing YAML records after approved evidence decisions, leaving the **other 91 untouched**, original 101 ID set/order and historical sources/taxonomy preserved. Record exact per-field old/new values with tagged primary URLs and avoid claims exceeding evidence. Add official generated views **only from** `python -m scripts.generate_docs`.
3. Run Python 3.12: `python -m scripts.generate_docs --check`, `python -m scripts.validate_catalog`, `python -m ruff check scripts tests`, `python -m ruff format --check scripts tests`, `python -m pytest -q`, `python -m pip check`, `git diff --check` plus independent 10/91 cohort check and catalogue counts. Linux CI must verify pinned 3.12 dependencies; do not change lock constraints for Windows-only extra `colorama`.
4. Keep the PR **Draft** until final reviewed SHA has all seven PR CI checks, a **completed independent Codex P1/P2 review**, and a fresh **manually dispatched Full link audit** on that exact SHA with downloaded JSON/Markdown report establishing `strict_result: PASS`, `blocking_new: 0`, `blocking_known: 6`, `baseline_changed: []`, `baseline_resolved: []`. No bypass or URL baseline edits.
5. No force-push, auto-merge, release/tag or premature closure. Require explicit human Ready/Squash-and-merge decision, verify four post-merge workflows and exact main inventory before closing any Wave 27 tracker; **issue #2 remains open**.

## First-pass actual actions

Selection frozen and evidence leads documented. **0/10 cleared, 10/10 still in canonical review.** This stage only adds this Markdown ledger. No canonical YAML, generated pages, Python constraints, GitHub workflow, or historical URL baseline changed. No claim of local full test completion or Wave27 strict network audit.
