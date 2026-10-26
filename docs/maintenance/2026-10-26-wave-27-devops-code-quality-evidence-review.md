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


---

## Second-pass proposed decisions — 2026-10-26 (NOT YET APPLIED)

**Evidence-based proposal: eight CLEAR and two RETAIN REVIEW.** The above first-pass `0 CLEAR` text is historical. This second-pass **has not changed the canonical YAML, generated documents or active counts**; the eight decisions below remain proposals pending controlled local application, official generation, independent QA and fresh final-SHA CI.

| Decision | ID | Primary source, verified licence boundary, technical adoption caveat |
|---|---|---|
| **CLEAR** | `actionlint` | [v1.7.12 MIT licence](https://github.com/rhysd/actionlint/blob/v1.7.12/LICENSE.txt), [v1.7.12 release](https://github.com/rhysd/actionlint/releases/tag/v1.7.12), [official project](https://github.com/rhysd/actionlint). Statically analyses **GitHub Actions workflows** (syntax, expressions, action metadata); it cannot execute workflows or guarantee security. ShellCheck and other optional external checks have their own dependencies and licences. |
| **CLEAR** | `black` | [26.10.1 MIT licence](https://github.com/psf/black/blob/26.10.1/LICENSE), [PEP 621 metadata](https://github.com/psf/black/blob/26.10.1/pyproject.toml) confirms MIT and Python `>=3.10`, [release](https://github.com/psf/black/releases/tag/26.10.1). Python **formatter** (not a static type checker), Black-versus-Ruff output/configuration compatibility must be checked before replacing one with the other. |
| **CLEAR** | `eslint` | [v10.13.0 MIT licence](https://github.com/eslint/eslint/blob/v10.13.0/LICENSE) and [package.json](https://github.com/eslint/eslint/blob/v10.13.0/package.json) state MIT and Node `^20.19.0 || ^22.13.0 || >=24`; [release](https://github.com/eslint/eslint/releases/tag/v10.13.0). Core parses **JavaScript**; TypeScript support depends on external parsers/plugins. **Missing canonical `repository_url`: add `https://github.com/eslint/eslint` only after repository-wide normalized duplicate-URL check**. Warn about ESLint v10 flat config and plugin ecosystem compatibility. |
| **RETAIN REVIEW** | `golangci-lint` | [v2.15.0 tagged LICENSE](https://github.com/golangci/golangci-lint/blob/v2.15.0/LICENSE) contains **GPL version 3 full text**. [v2.15.0 .goreleaser.yml](https://github.com/golangci/golangci-lint/blob/v2.15.0/.goreleaser.yml) declares distributions as `GPL-3.0` / `GPLv3` without unambiguously confirming current SPDX **`GPL-3.0-only` versus `GPL-3.0-or-later`** for all relevant files. Runner bundles or invokes many separately licensed linters; [Go module](https://github.com/golangci/golangci-lint/blob/v2.15.0/go.mod) has a declared Go 1.26 requirement and v2 config format. Keep `needs-review: true`, record licence ambiguity, **no invented precise SPDX**. |
| **RETAIN REVIEW** | `hadolint` | [v2.15.1 LICENSE](https://github.com/hadolint/hadolint/blob/v2.15.1/LICENSE) full **GPL version 3 text**, [hadolint.cabal](https://github.com/hadolint/hadolint/blob/v2.15.1/hadolint.cabal) reports `license: GPL-3` but does not settle `-only` vs `-or-later`; [tagged README](https://github.com/hadolint/hadolint/blob/v2.15.1/README.md) states GPLv3 and documents ShellCheck integration. Keep in review pending precise grant and redistribution scope; do not generalize a source grant to all Docker images/plugins. |
| **CLEAR** | `mypy` | [v1.19.1 LICENSE](https://github.com/python/mypy/blob/v1.19.1/LICENSE) expressly confirms **MIT for main mypy/mypyc source** while identifying **additional PSF-2.0/CNRI/BSD-like file-specific grants**; [v1.19.1 pyproject](https://github.com/python/mypy/blob/v1.19.1/pyproject.toml) describes `MIT` primary package, Python `>=3.9`; GitHub `NOASSERTION` alone does not override these source declarations. `license_spdx: MIT` is scoped to the **primary mypy package only**, not the entire source tree/stubs/plugins. mypy performs static type checking, not formatting; untyped code needs incremental adoption. |
| **CLEAR** | `prettier` | [3.9.10 LICENSE](https://github.com/prettier/prettier/blob/3.9.10/LICENSE) and [package.json](https://github.com/prettier/prettier/blob/3.9.10/package.json) MIT, Node `>=22`; [release](https://github.com/prettier/prettier/releases/tag/3.9.10). Opinionated **formatter**, does not lint runtime quality or support Python; third-party parsers/plugins are separately versioned/licensed. |
| **CLEAR** | `ruff` | [0.17.2 main LICENSE](https://github.com/astral-sh/ruff/blob/0.17.2/LICENSE) and [tagged README](https://github.com/astral-sh/ruff/blob/0.17.2/README.md) establish MIT **main project**; [release](https://github.com/astral-sh/ruff/releases/tag/0.17.2). Ruff includes Python linter and formatter, but does **not** implement all plugins/rules of Flake8, isort and Black. Avoid blanket drop-in replacement/performance guarantees; check selected rules and preview/target-version differences. |
| **CLEAR** | `shfmt` | [mvdan/sh v3.14.1 LICENSE](https://github.com/mvdan/sh/blob/v3.14.1/LICENSE) clearly matches **BSD-3-Clause**; [Go module](https://github.com/mvdan/sh/blob/v3.14.1/go.mod) declares module `mvdan.cc/sh/v3` and Go 1.26; [release](https://github.com/mvdan/sh/releases/tag/v3.14.1). shfmt is the CLI formatter inside this repo; **not** ShellCheck, no shell security lint guarantee. Preserve canonical repository URL. |
| **CLEAR** | `yamllint` | [v1.38.0 pyproject.toml](https://github.com/adrienverge/yamllint/blob/v1.38.0/pyproject.toml) **explicitly declares `license = "GPL-3.0-or-later"` and Python `>=3.10`**; [tagged LICENSE](https://github.com/adrienverge/yamllint/blob/v1.38.0/LICENSE) contains GPLv3 full text; [release](https://github.com/adrienverge/yamllint/releases/tag/v1.38.0). Unlike the other two GPL candidates, the exact SPDX branch **is supported by package metadata**. YAML syntax/style linter ≠ Kubernetes API schema, Helm/Kustomize or policy validator. |

### Canonical changes proposed for controlled local application

- **Eight CLEAR**: `status: active`, `needs_review: false`, `license_spdx: MIT` for `actionlint`, `black`, `eslint`, `mypy`, `prettier`, `ruff`; `BSD-3-Clause` for `shfmt`; `GPL-3.0-or-later` for `yamllint`; set accurate summary/avoid_when, append immutable evidence URLs to (never replace) historical `sources`, `verified_on: '2026-10-26'`.
- **Two RETAIN REVIEW**: `golangci-lint` and `hadolint` remain `status: needs-review`, `needs_review: true`, existing `license_model: oss`, and **no unsupported tool-wide `license_spdx`**. Update documented caution, verification date and immutable tagged `sources`.
- **ESLint identity remediation**: add `repository_url: https://github.com/eslint/eslint` (after independent global normalized-URL duplicate check). Do not change `official_url` or any other tool's repository URL.
- Preserve all **101 original IDs, order and 91 non-cohort records (including text)**, all existing legacy sources and immutable taxonomy/role/lifecycle assignments. No lockfile, workflows, historical six-URL baseline or issue changes; **no edits to main**.
- **Expected only after official regeneration and QA:** **1,425 canonical, 816 active, 595 needs-review**; in the target category **101 total, 46 remaining review**. These are *predictions*, not current repository statistics.

### Next QA and publication gates

Apply the exact ten IDs locally from the pinned documentary branch after a dry-run; generate the official Markdown/stats views using `scripts.generate_docs`, run `--check` and the full catalogue validation, Ruff, pytest, pip check, Python 3.12 lock verification in Linux CI and an independent 10/91 record comparison. Append actual old→new field-level tables, preserving this historical first-pass section.

**Do not commit or push automatically from the application script.** Inspect changed-file allowlist, revalidate the PR HEAD, then explicitly decide to commit/push. Require all seven new checks, completed independent P1/P2 Codex review and fresh manually dispatched full strict link audit of the *exact final PR SHA* before any human Ready/Squash-and-merge decision. Keep historical [issue #2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2) OPEN.

<!-- WAVE27_APPLIED_CANONICAL_CHANGELOG_START -->
## Local canonical application — Wave 27 field-level evidence log

**Status:** Canonical changes applied locally, official regeneration/QA and fresh PR CI pending until actually observed. The first-pass and second-pass recommendations above are historical checkpoints.

**Decisions applied to local canonical records:** 8 CLEAR / 2 RETAIN REVIEW. The catalogue-level expected inventory after official generation is 1,425 canonical, 816 active, 595 needs-review, subject to generator and CI validation.

| Decision | IDs |
|---|---|
| CLEAR | `actionlint`, `black`, `eslint`, `mypy`, `prettier`, `ruff`, `shfmt`, `yamllint` |
| RETAIN REVIEW | `golangci-lint`, `hadolint` |

All 91 non-cohort YAML records are unchanged byte-for-byte after line-ending normalization; original historical sources, taxonomy, role and lifecycle fields are preserved. No constraints or URL audit baseline update is authorized.

### `actionlint` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["Only if you don't use GitHub Actions."]</code> | <code>["Only if you don't use GitHub Actions.", "Does not execute workflows or replace dedicated secret scanning; optional ShellCheck has separate dependencies."]</code> |
| `license_spdx` | <code>null</code> | <code>"MIT"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L70", "legacy:devopstools_final.md#L1109"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L70", "legacy:devopstools_final.md#L1109", "https://github.com/rhysd/actionlint/blob/v1.7.12/LICENSE.txt", "https://github.com/rhysd/actionlint/releases/tag/v1.7.12"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Lint GitHub Actions workflows locally (catches many YAML/runtime mistakes early)."</code> | <code>"Static checker for GitHub Actions workflow syntax, expressions and referenced actions."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/rhysd/actionlint/blob/v1.7.12/LICENSE.txt
- https://github.com/rhysd/actionlint/releases/tag/v1.7.12


### `black` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["Ruff's formatter (which is Black-compatible and faster) already covers your needs."]</code> | <code>["Ruff's formatter (which is Black-compatible and faster) already covers your needs.", "Formatting does not detect type errors; evaluate Ruff formatter compatibility before switching."]</code> |
| `license_spdx` | <code>null</code> | <code>"MIT"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L71", "legacy:devopstools_final.md#L1110"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L71", "legacy:devopstools_final.md#L1110", "https://github.com/psf/black/blob/26.10.1/LICENSE", "https://github.com/psf/black/releases/tag/26.10.1"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Python code formatter."</code> | <code>"Opinionated Python source formatter with configurable target-version rules."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/psf/black/blob/26.10.1/LICENSE
- https://github.com/psf/black/releases/tag/26.10.1


### `eslint` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>[]</code> | <code>["TypeScript-specific analysis requires separately installed parser/plugins; ESLint 10 requires supported Node versions."]</code> |
| `license_spdx` | <code>null</code> | <code>"MIT"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `repository_url` | <code>null</code> | <code>"https://github.com/eslint/eslint"</code> |
| `sources` | <code>["legacy:devopstools_final.md#L1111"]</code> | <code>["legacy:devopstools_final.md#L1111", "https://github.com/eslint/eslint/blob/v10.13.0/LICENSE", "https://github.com/eslint/eslint/releases/tag/v10.13.0"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Pluggable JavaScript and TypeScript linter."</code> | <code>"Pluggable JavaScript linting engine with optional parsers and rule plugins."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/eslint/eslint/blob/v10.13.0/LICENSE
- https://github.com/eslint/eslint/releases/tag/v10.13.0


### `golangci-lint` — RETAIN REVIEW

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["Only if you intentionally want a single specific linter in isolation."]</code> | <code>["Only if you intentionally want a single specific linter in isolation.", "Exact GPLv3-only versus GPLv3-or-later grant and bundled linter licenses remain unverified; Go 1.26 and v2 configuration require compatibility checks."]</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L72", "legacy:devopstools_final.md#L1112"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L72", "legacy:devopstools_final.md#L1112", "https://github.com/golangci/golangci-lint/blob/v2.15.0/LICENSE", "https://github.com/golangci/golangci-lint/releases/tag/v2.15.0", "https://github.com/golangci/golangci-lint/blob/v2.15.0/.goreleaser.yml", "https://github.com/golangci/golangci-lint/blob/v2.15.0/go.mod"]</code> |
| `summary` | <code>"Go lint aggregator (fast, many linters)."</code> | <code>"Go linters aggregation runner with configurable analyzers and CI integration."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/golangci/golangci-lint/blob/v2.15.0/LICENSE
- https://github.com/golangci/golangci-lint/releases/tag/v2.15.0
- https://github.com/golangci/golangci-lint/blob/v2.15.0/.goreleaser.yml
- https://github.com/golangci/golangci-lint/blob/v2.15.0/go.mod


### `hadolint` — RETAIN REVIEW

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["Only if you use Buildpacks or other non-Dockerfile build methods."]</code> | <code>["Only if you use Buildpacks or other non-Dockerfile build methods.", "Exact GPLv3-only versus GPLv3-or-later grant and dependency redistribution terms remain unverified."]</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L73", "legacy:devopstools_final.md#L1113"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L73", "legacy:devopstools_final.md#L1113", "https://github.com/hadolint/hadolint/blob/v2.15.1/LICENSE", "https://github.com/hadolint/hadolint/releases/tag/v2.15.1", "https://github.com/hadolint/hadolint/blob/v2.15.1/hadolint.cabal"]</code> |
| `summary` | <code>"Dockerfile linter (best practices + common pitfalls)."</code> | <code>"Haskell-based Dockerfile linter with ShellCheck-derived shell diagnostics."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/hadolint/hadolint/blob/v2.15.1/LICENSE
- https://github.com/hadolint/hadolint/releases/tag/v2.15.1
- https://github.com/hadolint/hadolint/blob/v2.15.1/hadolint.cabal


### `mypy` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["Your code is untyped and the team isn't ready to adopt gradual typing."]</code> | <code>["Your code is untyped and the team isn't ready to adopt gradual typing.", "Main source is MIT but includes separately licensed portions; typing support depends on annotations and stubs."]</code> |
| `license_spdx` | <code>null</code> | <code>"MIT"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L81", "legacy:devopstools_final.md#L1121"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L81", "legacy:devopstools_final.md#L1121", "https://github.com/python/mypy/blob/v1.19.1/LICENSE", "https://github.com/python/mypy/tree/v1.19.1", "https://github.com/python/mypy/blob/v1.19.1/pyproject.toml"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Static type checker for Python."</code> | <code>"Gradual static type checker for Python with type stubs, plugins and optional mypyc acceleration."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/python/mypy/blob/v1.19.1/LICENSE
- https://github.com/python/mypy/tree/v1.19.1
- https://github.com/python/mypy/blob/v1.19.1/pyproject.toml


### `prettier` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["For Python (use Black/Ruff) or languages Prettier doesn't support."]</code> | <code>["For Python (use Black/Ruff) or languages Prettier doesn't support.", "Formatting is not linting or code security analysis; optional plugins carry separate licenses and runtime constraints."]</code> |
| `license_spdx` | <code>null</code> | <code>"MIT"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L75", "legacy:devopstools_final.md#L1115"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L75", "legacy:devopstools_final.md#L1115", "https://github.com/prettier/prettier/blob/3.9.10/LICENSE", "https://github.com/prettier/prettier/releases/tag/3.9.10"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Opinionated formatter for JSON/YAML/Markdown and more."</code> | <code>"Opinionated formatter for JavaScript, TypeScript, JSON, YAML, Markdown and other supported languages."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/prettier/prettier/blob/3.9.10/LICENSE
- https://github.com/prettier/prettier/releases/tag/3.9.10


### `ruff` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["You depend on niche Flake8 plugins Ruff hasn't yet reimplemented."]</code> | <code>["You depend on niche Flake8 plugins Ruff hasn't yet reimplemented.", "Not a universal drop-in for Black, Flake8 and isort plugins; check supported rules and preview settings."]</code> |
| `license_spdx` | <code>null</code> | <code>"MIT"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L76", "legacy:devopstools_final.md#L1116"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L76", "legacy:devopstools_final.md#L1116", "https://github.com/astral-sh/ruff/blob/0.17.2/LICENSE", "https://github.com/astral-sh/ruff/releases/tag/0.17.2"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Ultra-fast Python linter/formatter."</code> | <code>"Python linter and formatter implemented in Rust with configurable rule sets."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/astral-sh/ruff/blob/0.17.2/LICENSE
- https://github.com/astral-sh/ruff/releases/tag/0.17.2


### `shfmt` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["Only if you have no shell scripts."]</code> | <code>["Only if you have no shell scripts.", "Formatting does not replace ShellCheck security lint; validate shell dialect and Go runtime version."]</code> |
| `license_spdx` | <code>null</code> | <code>"BSD-3-Clause"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L77", "legacy:devopstools_final.md#L1117"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L77", "legacy:devopstools_final.md#L1117", "https://github.com/mvdan/sh/blob/v3.14.1/LICENSE", "https://github.com/mvdan/sh/releases/tag/v3.14.1"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Shell formatter (`shfmt`)."</code> | <code>"Shell script formatter from the mvdan/sh parser and toolchain."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/mvdan/sh/blob/v3.14.1/LICENSE
- https://github.com/mvdan/sh/releases/tag/v3.14.1


### `yamllint` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["Prettier already handles your YAML formatting needs."]</code> | <code>["Prettier already handles your YAML formatting needs.", "Does not validate Kubernetes resource schemas or Helm/Kustomize policies."]</code> |
| `license_spdx` | <code>null</code> | <code>"GPL-3.0-or-later"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L78", "legacy:devopstools_final.md#L1118"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L78", "legacy:devopstools_final.md#L1118", "https://github.com/adrienverge/yamllint/blob/v1.38.0/LICENSE", "https://github.com/adrienverge/yamllint/releases/tag/v1.38.0", "https://github.com/adrienverge/yamllint/blob/v1.38.0/pyproject.toml"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"YAML linter (structure + style checks)."</code> | <code>"YAML syntax and style linter with configurable formatting and validation rules."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/adrienverge/yamllint/blob/v1.38.0/LICENSE
- https://github.com/adrienverge/yamllint/releases/tag/v1.38.0
- https://github.com/adrienverge/yamllint/blob/v1.38.0/pyproject.toml


**Publication checkpoint:** This local change log is not itself evidence of test/CI completion. After the official local generator and full QA pass, review the final diff, push through an explicit human-authorized commit, obtain fresh PR CI + independent P1/P2 review and a new strict full URL audit on the exact final SHA before a human merge decision.
<!-- WAVE27_APPLIED_CANONICAL_CHANGELOG_END -->


## Wave 27 N1a current-state regression guard follow-up — 2026-10-26

A full local pytest run after the bounded Wave 27 YAML application initially
failed in `test_n1a_current_state_preserves_owned_decisions`: the frozen N1a
current-state checker still compared Black's `license_spdx` against the old
accepted `None`, whereas the independently tagged
[Black 26.10.1 MIT LICENSE](https://github.com/psf/black/blob/26.10.1/LICENSE)
and [project metadata](https://github.com/psf/black/blob/26.10.1/pyproject.toml)
support `MIT`. The same evidence review intentionally changed Black from
`needs-review` to `active` with `needs_review: false`.

The follow-up patch extends only the **current-state supersession mechanism**
for precisely three pairs: `(black, license_spdx)=MIT`,
`(black, status)=active`, `(black, needs_review)=false` in
`tests/test_v022_n1a_access_retry.py`. It adds a regression test asserting
the exact approved values and rejects an unauthorized change of Black's
`repository_url`. It **does not alter** the frozen N1a historical baseline,
original N1a or Wave 23 allowlist, immutable N1a accepted historical result,
or any other tool's protected fields/URLs. The existing exact allowlist test
in `tests/test_deferred_catalogue_corrections.py` remains untouched.

Only the N1a test and this maintenance ledger are new changes on top of the
already-applied ten-ID Wave 27 YAML and official generated views. Verification
results must be taken from the repair command output; no PASS is claimed
until tests have actually completed locally. No commit, push or merge here.
