# Wave 25 — CI testing and pull-request quality: first-pass primary-source triage

**Observed:** 2026-10-26. **Documentary stage ONLY: 10 reviewed for evidence leads; 0 CLEAR decisions applied; all 10 RETAIN needs-review pending full field-by-field review.** Selection contract: [issue #141](https://github.com/goozcena-gnl/devops-tools-catalog/issues/141). Pinned `main` baseline: `86f83146f03062d7b7da88efd51ecc56fc6367fa`.

This is the **first-pass evidence ledger**, not a completed field-level clearance, maintenance support certification, legal advice or result of executing source/tests locally. GitHub repository metadata and tagged licence files were read directly. A GitHub licence badge, repo unarchived status or an HTTP-successful URL is NOT sufficient to change a catalogue status. Preserve uncertainty and product/edition boundaries.

## Baseline and bounded scope

- **1,425** canonical records, **792 active**, **619 needs-review**, 30 categories, according to the existing `main` generated statistics.
- `data/tools/ci-build-testing.yaml` has **80 records**, **21** with `status: needs-review` and `needs_review: true`; this fixed cohort is **10 of those records**. Other **70** canonical records must stay unchanged.
- Exact IDs: `k6`, `playwright`, `pytest`, `pytest-cov`, `selenium`, `serverspec`, `test-kitchen`, `testcontainers`, `vitest`, `semantic-pull-request-github-action`.
- All ten are **still needs-review in catalogue data**. This commit changes **only this dated Markdown evidence ledger**. Do not assume successful tests, new generated views or cleared fields.
- URL baseline `config/link-audit-baseline.json` with **six** historical URL/classification exceptions is unchanged (blob SHA `a834e2af711693def40078a55e31dfeb29bee2c7`). Keep [issue #2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2) OPEN. Prior [strict audit #38](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/40230711589) was for **Wave 24 PR HEAD** and cannot satisfy Wave 25 final-head verification.

## Tagged upstream primary-source observations (candidate evidence, NOT final decisions)

| ID | Repository, tagged release and upstream licence inspected | Evidence interpretation and open review questions |
|---|---|---|
| `k6` | [grafana/k6](https://github.com/grafana/k6), [v1.8.2](https://github.com/grafana/k6/releases/tag/v1.8.2) (2026-10-12) and [v2.3.0](https://github.com/grafana/k6/releases/tag/v2.3.0) (2026-09-21); tagged [v1.8.2 LICENSE.md](https://github.com/grafana/k6/blob/v1.8.2/LICENSE.md) and [v2.3.0 LICENSE.md](https://github.com/grafana/k6/blob/v2.3.0/LICENSE.md) contain **AGPL version 3 text** | Two **concurrent-looking release lines, v1.8.2 and v2.3.0** both marked non-prerelease in GitHub; **do not claim that v1.8.2 is the globally latest stable version**. Independently verify lifecycle, documented support, edition/licence grant and cloud k6 service boundaries. AGPL licence file alone does not establish `-only` vs `-or-later` SPDX terms. |
| `playwright` | [microsoft/playwright](https://github.com/microsoft/playwright), [v1.64.1](https://github.com/microsoft/playwright/releases/tag/v1.64.1) (2026-10-14); [tagged LICENSE](https://github.com/microsoft/playwright/blob/v1.64.1/LICENSE) is **Apache-2.0** | Confirm browser-binary, browser-driver and test-runner licence boundaries separately. Verify documented cross-browser/OS versions, test isolation in CI and stable API compatibility. |
| `pytest` | [pytest-dev/pytest](https://github.com/pytest-dev/pytest), [9.1.1](https://github.com/pytest-dev/pytest/releases/tag/9.1.1) (2026-06-19); [tagged LICENSE](https://github.com/pytest-dev/pytest/blob/9.1.1/LICENSE) is **MIT** | Confirm supported Python versions, test framework core vs plugins, security and maintainer/release signals. |
| `pytest-cov` | [pytest-dev/pytest-cov](https://github.com/pytest-dev/pytest-cov), [master LICENSE](https://github.com/pytest-dev/pytest-cov/blob/master/LICENSE) is **MIT**; upstream GitHub Releases endpoint gave **no releases** | Do not infer inactivity or no release from GitHub Releases being empty. Find immutable PyPI release/tag and versioned licence, coverage.py compatibility, pytest versions and official changelog before any clearance. |
| `selenium` | [SeleniumHQ/selenium](https://github.com/SeleniumHQ/selenium), stable [selenium-4.51.0](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.51.0) (2026-10-09); [tagged LICENSE](https://github.com/SeleniumHQ/selenium/blob/selenium-4.51.0/LICENSE) is **Apache-2.0** | A [nightly prerelease](https://github.com/SeleniumHQ/selenium/releases/tag/nightly) also exists: do not conflate it with GA. Verify WebDriver/Grid/IDE module boundaries, supported browser drivers and Grid network security. |
| `serverspec` | [mizzy/serverspec](https://github.com/mizzy/serverspec), [v2.43.0](https://github.com/mizzy/serverspec/releases/tag/v2.43.0) (2025-04-24); [tagged LICENSE.txt](https://github.com/mizzy/serverspec/blob/v2.43.0/LICENSE.txt) is **MIT** | Server-state RSpec-based infrastructure assertions; verify Ruby/runtime compatibility, SSH/WinRM transport/security, and maintainer/project support. Repo unarchived does not imply frequent releases. |
| `test-kitchen` | [test-kitchen/test-kitchen](https://github.com/test-kitchen/test-kitchen), [v4.1.5](https://github.com/test-kitchen/test-kitchen/releases/tag/v4.1.5) (2026-10-01); [tagged LICENSE](https://github.com/test-kitchen/test-kitchen/blob/v4.1.5/LICENSE) explicitly grants **Apache-2.0** | GitHub auto-classification returned `NOASSERTION`: the actual tagged LICENSE takes precedence. Check Test Kitchen gem runtime, drivers, transport privilege, Chef/other provisioner boundaries, and whether optional integrations have independent licences. |
| `testcontainers` | Umbrella [Testcontainers organization](https://github.com/testcontainers); representative [testcontainers-java 2.0.5](https://github.com/testcontainers/testcontainers-java/releases/tag/2.0.5), tagged [Java LICENSE](https://github.com/testcontainers/testcontainers-java/blob/2.0.5/LICENSE) **MIT**; [Go LICENSE](https://github.com/testcontainers/testcontainers-go/blob/main/LICENSE) **MIT**, [Node LICENSE](https://github.com/testcontainers/testcontainers-node/blob/main/LICENSE) **MIT**; GitHub's Python repository metadata lists **Apache-2.0** but the licence file path was **not yet verified** | **Organization/multi-library product**, not a single canonical repo or uniform SPDX. Do not copy the Java MIT conclusion to Python or a paid Testcontainers Cloud/Desktop service. Confirm Python licence at immutable tag, other languages, product/service ownership/edition terms and whether catalogue's existing `open-core` label reflects a verifiable mixed offering. |
| `vitest` | [vitest-dev/vitest](https://github.com/vitest-dev/vitest), stable [v5.0.5](https://github.com/vitest-dev/vitest/releases/tag/v5.0.5) (2026-10-15); [tagged LICENSE](https://github.com/vitest-dev/vitest/blob/v5.0.5/LICENSE) **MIT** | GitHub also lists [v5.1.0-beta.1](https://github.com/vitest-dev/vitest/releases/tag/v5.1.0-beta.1) prerelease; don't label beta stable. Confirm Vite/Node/TypeScript compatibility, runner vs browser mode, related paid-services boundary (if any). |
| `semantic-pull-request-github-action` | [amannn/action-semantic-pull-request](https://github.com/amannn/action-semantic-pull-request), [v6.1.1](https://github.com/amannn/action-semantic-pull-request/releases/tag/v6.1.1) (2025-08-22); [tagged LICENSE](https://github.com/amannn/action-semantic-pull-request/blob/v6.1.1/LICENSE) **MIT** | PR title Conventional Commits enforcement GitHub Action; check safe event triggers, least-privilege `pull-requests: read`, token/external contributor caveats and immutable SHA pinning guidance; no claim it tests application code or signs supply-chain artefacts. |

Directly inspected GitHub repo metadata on 2026-10-26 shows all ten upstream candidate repositories above as **unarchived**, including the representative Java repo for the Testcontainers organization. This is a **dated metadata signal only**, not certification of supported production use.

## Specific constraints for next evidence pass

1. **No clearance quota:** individually decide CLEAR/RETAIN REVIEW from tagged source, first-party licences and support docs. `k6` license/release-line nuance, `pytest-cov` non-GitHub release process, `Test Kitchen` SPDX auto-classification and `Testcontainers` multi-language OSS vs commercial services need explicit judgement and tagged evidence.
2. **Versioned evidence over memory:** verify release tags, latest stable support and runtime/browser/driver compatibility, security and operational caveats for all ten. Never equate an upstream repo with a hosted paid product.
3. **Field-level diff per tool:** for any canonical edits, record original/new values, primary URL or immutable tag, confidence, reasons and unresolved evidence gaps. Keep prior `sources` and project IDs, categories, lifecycle/roles and all 70 non-cohort records. Where licensing cannot be proven precisely, retain review, do not invent SPDX.
4. **Bounded implementation later:** restrict canonical edits to the selected ten IDs in `data/tools/ci-build-testing.yaml`, plus official `scripts.generate_docs` outputs and this ledger. Do not change constraints, baseline exceptions, unrelated Python scripts/tests/workflows or GitHub settings to make a checker green.
5. **Actual local and PR CI:** clean pinned Python 3.12 environment, `python -m scripts.generate_docs` and `--check`, `python -m scripts.validate_catalog`, `python -m scripts.python_constraints --verify-locked` in supported CI context, `python -m pip check`, Ruff check/format, full pytest, `git diff --check`. Always verify expected canonical counts and exact modified IDs, no unreviewed status flips. Local Windows-only `colorama` extra package is not a reason to alter `config/python-constraints-3.12.txt`.
6. **Independent review and network audit on exact final SHA:** Draft PR, no merge. Require all standard CI and a completed independent Codex/human P1/P2 review (no quota-failure-as-pass), and then a **fresh manually triggered strict Full link audit** on the same final Wave 25 SHA. Require `strict_result: PASS`, `blocking_new: 0`, unchanged **six** historical URL/classification pairs, and save report artefact. No TLS bypass, no baseline waivers.
7. **Human merge boundary:** Only after explicit human decision may this PR transition to Ready then be manually squash-merged. After merge, verify exact new `main` SHA and four green post-merge gates; only then close #141. Keep historical URL [issue #2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2) OPEN.

## Actions actually executed in this first pass

This ledger is a **documentation-only first commit**. No catalogue YAML, statuses, generated views, lockfiles, tests, workflows, URL baseline, releases or issues have been modified, and **no local pytest/ruff or fresh Wave 25 full link audit has run**. The next step is a bounded, independent second evidence pass prior to any proposed `active` clearances.


---

## Second-pass decisions proposed — 2026-10-26 (not yet applied to catalogue)

**Outcome proposed for canonical implementation: 8 CLEAR / 2 RETAIN REVIEW.** These are independent primary-evidence **recommendations**, not a claim that canonical YAML has already changed or that the PR can be merged. The first-pass "0 CLEAR" statement above remains a historical statement about the original triage commit; do not interpret it as the current recommendation. The remaining production/compatibility caveats do not imply all products or plugins share the same source licence.

| Decision | IDs | Rationale |
|---|---|---|
| **CLEAR** (8) | `playwright`, `pytest`, `pytest-cov`, `selenium`, `serverspec`, `test-kitchen`, `vitest`, `semantic-pull-request-github-action` | Identified canonical single-project upstreams, tagged primary source licence evidence, specific operational boundaries below; explicit narrow catalogue summary/avoid guidance. |
| **RETAIN REVIEW** (2) | `k6`, `testcontainers` | k6 has concurrent observed 1.x patch and 2.x minor release streams and AGPL-3 source without an independently established precise `AGPL-3.0-only` versus `-or-later` expression; hosted Grafana Cloud offering separate. Testcontainers umbrella has multiple language repositories with *different* grants and separately offered paid services; a one-repo/SPDX assertion would mislead. |

### Versioned support/licence evidence and adoption boundaries

| ID | Explicit verified tagged evidence | Decisions, cautions, remaining unknowns |
|---|---|---|
| `playwright` | [v1.64.1 LICENSE Apache-2.0](https://github.com/microsoft/playwright/blob/v1.64.1/LICENSE), [release](https://github.com/microsoft/playwright/releases/tag/v1.64.1), [official docs](https://playwright.dev/) | CLEAR: upstream runner automates Chromium, Firefox and WebKit; browser binaries, operating-system packages, and container-image availability have independent licensing/support/compatibility. Do not claim the browser vendors' licences are Apache-2.0. |
| `pytest` | [9.1.1 LICENSE MIT](https://github.com/pytest-dev/pytest/blob/9.1.1/LICENSE), [9.1.1 pyproject.toml](https://github.com/pytest-dev/pytest/blob/9.1.1/pyproject.toml) explicitly `requires-python >=3.10`, [release](https://github.com/pytest-dev/pytest/releases/tag/9.1.1) | CLEAR: Python runner/fixtures/plugins; not itself a coverage collector or a general cross-language test framework. Avoid incompatible older Python installations, and pin plugins/versions in CI. |
| `pytest-cov` | Verified **immutable [v7.1.0 LICENSE MIT](https://github.com/pytest-dev/pytest-cov/blob/v7.1.0/LICENSE)**, [v7.1.0 pyproject.toml](https://github.com/pytest-dev/pytest-cov/blob/v7.1.0/pyproject.toml) explicitly `requires-python >=3.9`, `pytest >=7`, `coverage[toml] >=7.10.6`, `pluggy >=1.2`, [upstream changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst) shows 7.1.0 released 2026-03-21 | CLEAR: this is a pytest plugin using coverage.py; distributed support uses pytest-xdist. **GitHub Releases being empty does not mean the project lacks tagged releases**. Beware coverage.py minimum versions and changed subprocess support in v7. |
| `selenium` | [selenium-4.51.0 LICENSE Apache-2.0](https://github.com/SeleniumHQ/selenium/blob/selenium-4.51.0/LICENSE), [stable release](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.51.0), [official docs](https://www.selenium.dev/documentation/) | CLEAR: browser WebDriver/Grid ecosystem, not a single browser or guaranteed all-browser version combination. Prefer least-privilege and authentication/network isolation for Grid, match browser/driver versions; latest GitHub `nightly` is prerelease, **not GA**. |
| `serverspec` | [v2.43.0 LICENSE.txt MIT](https://github.com/mizzy/serverspec/blob/v2.43.0/LICENSE.txt), [release](https://github.com/mizzy/serverspec/releases/tag/v2.43.0), [tagged README](https://github.com/mizzy/serverspec/blob/v2.43.0/README.md) explicitly describes RSpec-based tests and **maintainer policy that accepts fixes/features primarily via PRs with tests** | CLEAR as a tool record, not a promise of vendor SLA. Use specifically for Ruby/RSpec server-state assertions; understand its contributor-driven maintenance and secure SSH/WinRM access. Avoid if you require commercial/vendor-backed SLA or cross-language runtime. |
| `test-kitchen` | [v4.1.5 LICENSE explicitly Apache-2.0](https://github.com/test-kitchen/test-kitchen/blob/v4.1.5/LICENSE), [tagged README](https://github.com/test-kitchen/test-kitchen/blob/v4.1.5/README.md) identifies RubyGem integration testing with isolated drivers and explicit same licence, [release](https://github.com/test-kitchen/test-kitchen/releases/tag/v4.1.5) | CLEAR: test infra code on isolated targets. GitHub auto-license badge says `NOASSERTION`, **actual tagged file proves Apache-2.0 for this source**. Drivers, Chef/Cinc integrations, container/VM images and cloud providers need separate licence and privileged-runner review. |
| `vitest` | [v5.0.5 LICENSE MIT](https://github.com/vitest-dev/vitest/blob/v5.0.5/LICENSE), [tagged README](https://github.com/vitest-dev/vitest/blob/v5.0.5/README.md), [tagged package.json](https://github.com/vitest-dev/vitest/blob/v5.0.5/package.json) declares monorepo Node `^22.12.0 || ^24.0.0 || >=26.0.0`, [stable release](https://github.com/vitest-dev/vitest/releases/tag/v5.0.5) | CLEAR: Vite-compatible testing/Browser Mode is separate from general end-to-end Playwright/Selenium. Use supported Node/Vite peer dependency combinations and do not adopt experimental `v5.1.0-beta.1` as GA; monorepo runtime declaration alone is not a guarantee for every package/integration. |
| `semantic-pull-request-github-action` | [v6.1.1 LICENSE MIT](https://github.com/amannn/action-semantic-pull-request/blob/v6.1.1/LICENSE), [tagged action.yml](https://github.com/amannn/action-semantic-pull-request/blob/v6.1.1/action.yml) uses Node24, [tagged README](https://github.com/amannn/action-semantic-pull-request/blob/v6.1.1/README.md) documents Conventional Commits PR titles and `pull_request_target` example with `pull-requests: read` | CLEAR: **PR title lint, not code quality scanning**. Use least-privilege token, pin immutable action SHA in production, never execute untrusted PR source with privileged `pull_request_target`. The optional `wip: true` feature requires write permission and deserves separate security review. |
| `k6` | [v1.8.2 LICENSE.md](https://github.com/grafana/k6/blob/v1.8.2/LICENSE.md) and [v2.3.0 LICENSE.md](https://github.com/grafana/k6/blob/v2.3.0/LICENSE.md) both contain AGPL version 3 licence, [tagged README](https://github.com/grafana/k6/blob/v2.3.0/README.md) says distributed under AGPL-3.0 and distinguishes Grafana Cloud k6 SaaS | RETAIN: no invented precise SPDX `-only/-or-later`, don't collapse 1.x backport and 2.x stable release lines, and don't silently transfer source licence to paid Grafana Cloud services. This is an **evidence-boundary decision**, not a declaration that k6 is insecure or unsupported. |
| `testcontainers` | Verified different upstream source licences: [Java 2.0.5 LICENSE MIT](https://github.com/testcontainers/testcontainers-java/blob/2.0.5/LICENSE), [Go main LICENSE MIT](https://github.com/testcontainers/testcontainers-go/blob/main/LICENSE), [Node main LICENSE MIT](https://github.com/testcontainers/testcontainers-node/blob/main/LICENSE), [Python main LICENSE.txt Apache-2.0](https://github.com/testcontainers/testcontainers-python/blob/main/LICENSE.txt), [Python pyproject.toml](https://github.com/testcontainers/testcontainers-python/blob/main/pyproject.toml) itself declares `license = "Apache-2.0"` | RETAIN: umbrella organization is not equal to a single source tree. Exact licence depends on language; hosting products/paid cloud or desktop integration need separate documented offers, tenancy and support rules. Keep catalogue `license_model: open-core` only as an unverified prior assertion until specific product taxonomy decision is sourced. |

### Proposed canonical field changes — NOT YET APPLIED

Bounded changes, conditional on a clean local check of the pinned branch:
- Change **only 8 selected IDs** from `status: needs-review` to `status: active` and `needs_review: false`.
- Preserve `k6` and `testcontainers` at `status: needs-review`, `needs_review: true` and add a narrowly scoped warning/usage evidence for both; **10/10 records** may receive evidence-grounded summary, `avoid_when`, date and `sources` changes.
- For eight single-codebase source records, set `license_spdx` based on the immutable licence files: `playwright`, `selenium`, `test-kitchen` → `Apache-2.0`; `pytest`, `pytest-cov`, `serverspec`, `vitest`, `semantic-pull-request-github-action` → `MIT`. **Do not set a single `license_spdx` for retained k6 or multi-language Testcontainers.** Do not change `license_model` unilaterally.
- Add *only official first-party tagged sources* plus documented reasons (include `v7.1.0` for pytest-cov, tagged Apache-2.0 despite the GitHub Test Kitchen licence badge, different grants for Testcontainers by language). Preserve every legacy source and all existing category/roles/lifecycle identities.
- Expected counts **if official generator and strict record-scope checks agree**: 1,425 canonical, **800 active**, **611 needs-review**, 80 records and 13 needs-review within `ci-build-testing.yaml`. **These are projections, not current GitHub inventory observations.** No forced clearance quota.

### Next mandatory local/checkpoint gates

Use the verified local PowerShell/Python 3.12 environment only after a clean checkout of this PR head. Run official generator then `generate_docs --check`, `validate_catalog`, `ruff check scripts tests`, `ruff format --check scripts tests`, full `pytest -q`, `pip check`, `git diff --check`; CI `python_constraints --verify-locked` on Linux must pass. Windows extra `colorama` remains a local-environment observation, never a reason to update repository lockfiles. Before commit, check **exactly 10** changed YAML records, unchanged other 70, preserved source list and taxonomy, and only documented official generated views. The first-pass PR CI cannot substitute for final generated-doc QA.

After actual application, **append an observed field-by-field before/after log and verified command results here**; do not leave unperformed QA described as successful or a projected inventory presented as achieved. Then rerun all PR CI, obtain **completed independent Codex/human P1/P2 review on exact final SHA**, fresh manually triggered strict Full link audit with `blocking_new: 0`, `strict_result: PASS`, unchanged six known baseline exceptions. Maintain Draft/strict human merge boundary; [issue #141](https://github.com/goozcena-gnl/devops-tools-catalog/issues/141) stays OPEN and [issue #2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2) stays OPEN.

<!-- WAVE25_APPLIED_CANONICAL_CHANGELOG_START -->
## Local canonical application — Wave 25 field-level evidence log

**Status:** Canonical changes applied locally, official regeneration/QA and fresh PR CI pending until actually observed. The first-pass and second-pass recommendations above are historical checkpoints.

**Decisions applied to local canonical records:** 8 CLEAR / 2 RETAIN REVIEW. The catalogue-level expected inventory after official generation is 1,425 canonical, 800 active, 611 needs-review, subject to generator and CI validation.

| Decision | IDs |
|---|---|
| CLEAR | `playwright`, `pytest`, `pytest-cov`, `selenium`, `semantic-pull-request-github-action`, `serverspec`, `test-kitchen`, `vitest` |
| RETAIN REVIEW | `k6`, `testcontainers` |

All 70 non-cohort YAML records are unchanged byte-for-byte after line-ending normalization; original historical sources, taxonomy, role and lifecycle fields are preserved. No constraints or URL audit baseline update is authorized.

### `k6` — RETAIN REVIEW

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["You need a GUI-based test builder or non-HTTP protocol support without extensions."]</code> | <code>["You need a GUI-based test builder or non-HTTP protocol support without extensions.", "You assume Grafana Cloud k6 has the same AGPL licence as the standalone CLI.", "You require a single unambiguous latest stable line or exact AGPL-3.0-only versus -or-later grant without additional licence research."]</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L12", "legacy:devopstools_final.md#L1034"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L12", "legacy:devopstools_final.md#L1034", "https://github.com/grafana/k6/blob/v1.8.2/LICENSE.md", "https://github.com/grafana/k6/blob/v2.3.0/LICENSE.md", "https://github.com/grafana/k6/blob/v2.3.0/README.md", "https://github.com/grafana/k6/releases/tag/v2.3.0", "https://github.com/grafana/k6/releases/tag/v1.8.2"]</code> |
| `summary` | <code>"Load testing tool for performance testing."</code> | <code>"Open-source JavaScript-based load testing CLI with HTTP, WebSocket, gRPC and browser test capabilities; Grafana Cloud k6 is a separate service."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/grafana/k6/blob/v1.8.2/LICENSE.md
- https://github.com/grafana/k6/blob/v2.3.0/LICENSE.md
- https://github.com/grafana/k6/blob/v2.3.0/README.md
- https://github.com/grafana/k6/releases/tag/v2.3.0
- https://github.com/grafana/k6/releases/tag/v1.8.2


### `playwright` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["Your team is already productive with Cypress and doesn't need the extra browser coverage."]</code> | <code>["Your team is already productive with Cypress and doesn't need the extra browser coverage.", "You assume browser binaries and external OS dependencies share the test runner Apache-2.0 source licence or do not need CI version pinning."]</code> |
| `license_spdx` | <code>null</code> | <code>"Apache-2.0"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L14", "legacy:devopstools_final.md#L1036"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L14", "legacy:devopstools_final.md#L1036", "https://github.com/microsoft/playwright/blob/v1.64.1/LICENSE", "https://github.com/microsoft/playwright/releases/tag/v1.64.1", "https://playwright.dev/docs/intro"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"End-to-end testing for web apps."</code> | <code>"Cross-browser web test runner and browser automation framework supporting Chromium, Firefox and WebKit."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/microsoft/playwright/blob/v1.64.1/LICENSE
- https://github.com/microsoft/playwright/releases/tag/v1.64.1
- https://playwright.dev/docs/intro


### `pytest` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["Only if you're in a non-Python stack."]</code> | <code>["Only if you're in a non-Python stack.", "You require a cross-language test runner or need support for Python versions below the upstream pytest 9.1.1 minimum of 3.10."]</code> |
| `license_spdx` | <code>null</code> | <code>"MIT"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L15", "legacy:devopstools_final.md#L1037"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L15", "legacy:devopstools_final.md#L1037", "https://github.com/pytest-dev/pytest/blob/9.1.1/LICENSE", "https://github.com/pytest-dev/pytest/blob/9.1.1/pyproject.toml", "https://github.com/pytest-dev/pytest/releases/tag/9.1.1"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Python testing framework."</code> | <code>"Python test runner with fixtures, parametrization and an extensible plugin ecosystem."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/pytest-dev/pytest/blob/9.1.1/LICENSE
- https://github.com/pytest-dev/pytest/blob/9.1.1/pyproject.toml
- https://github.com/pytest-dev/pytest/releases/tag/9.1.1


### `pytest-cov` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>[]</code> | <code>["You need a standalone test runner or cannot meet pytest-cov v7.1.0 dependencies including coverage.py 7.10.6 or newer."]</code> |
| `license_spdx` | <code>null</code> | <code>"MIT"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:devopstools_final.md#L1038"]</code> | <code>["legacy:devopstools_final.md#L1038", "https://github.com/pytest-dev/pytest-cov/blob/v7.1.0/LICENSE", "https://github.com/pytest-dev/pytest-cov/blob/v7.1.0/pyproject.toml", "https://github.com/pytest-dev/pytest-cov/blob/v7.1.0/README.rst", "https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Pytest plugin for coverage reporting, including support for distributed test runs."</code> | <code>"pytest plugin for measuring Python test coverage through coverage.py, including optional distributed-test integration."</code> |
| `use_when` | <code>[]</code> | <code>["You want reproducible Python coverage reports as part of pytest in CI."]</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/pytest-dev/pytest-cov/blob/v7.1.0/LICENSE
- https://github.com/pytest-dev/pytest-cov/blob/v7.1.0/pyproject.toml
- https://github.com/pytest-dev/pytest-cov/blob/v7.1.0/README.rst
- https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst


### `selenium` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["For new greenfield projects where Playwright or Cypress offer better DX out of the box."]</code> | <code>["For new greenfield projects where Playwright or Cypress offer better DX out of the box.", "You cannot isolate and secure Selenium Grid endpoints or coordinate the browser and driver versions used by CI."]</code> |
| `license_spdx` | <code>null</code> | <code>"Apache-2.0"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L16", "legacy:devopstools_final.md#L1039"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L16", "legacy:devopstools_final.md#L1039", "https://github.com/SeleniumHQ/selenium/blob/selenium-4.51.0/LICENSE", "https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.51.0", "https://www.selenium.dev/documentation/"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Browser automation for testing web applications."</code> | <code>"Browser WebDriver automation and Selenium Grid ecosystem for cross-browser application testing."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/SeleniumHQ/selenium/blob/selenium-4.51.0/LICENSE
- https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.51.0
- https://www.selenium.dev/documentation/


### `semantic-pull-request-github-action` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["You use per-commit linting (commitlint) and don't squash."]</code> | <code>["You use per-commit linting (commitlint) and don't squash.", "You need application code scanning rather than PR title linting or would run untrusted PR code with privileged pull_request_target access."]</code> |
| `license_spdx` | <code>null</code> | <code>"MIT"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L61", "legacy:devopstools_final.md#L1098"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L61", "legacy:devopstools_final.md#L1098", "https://github.com/amannn/action-semantic-pull-request/blob/v6.1.1/LICENSE", "https://github.com/amannn/action-semantic-pull-request/blob/v6.1.1/README.md", "https://github.com/amannn/action-semantic-pull-request/blob/v6.1.1/action.yml", "https://github.com/amannn/action-semantic-pull-request/releases/tag/v6.1.1"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Enforce semantic PR titles in GitHub Actions."</code> | <code>"GitHub Action validating pull request titles against Conventional Commits naming conventions."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/amannn/action-semantic-pull-request/blob/v6.1.1/LICENSE
- https://github.com/amannn/action-semantic-pull-request/blob/v6.1.1/README.md
- https://github.com/amannn/action-semantic-pull-request/blob/v6.1.1/action.yml
- https://github.com/amannn/action-semantic-pull-request/releases/tag/v6.1.1


### `serverspec` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["You prefer a language-agnostic approach (consider InSpec or Goss)."]</code> | <code>["You prefer a language-agnostic approach (consider InSpec or Goss).", "You require a commercial maintenance SLA or cannot secure Ruby execution and SSH or other remote test access."]</code> |
| `license_spdx` | <code>null</code> | <code>"MIT"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L17", "legacy:devopstools_final.md#L1040"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L17", "legacy:devopstools_final.md#L1040", "https://github.com/mizzy/serverspec/blob/v2.43.0/LICENSE.txt", "https://github.com/mizzy/serverspec/blob/v2.43.0/README.md", "https://github.com/mizzy/serverspec/releases/tag/v2.43.0"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Test server configurations using RSpec."</code> | <code>"Ruby/RSpec-based server-state assertions for installed packages, services, ports and configuration."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/mizzy/serverspec/blob/v2.43.0/LICENSE.txt
- https://github.com/mizzy/serverspec/blob/v2.43.0/README.md
- https://github.com/mizzy/serverspec/releases/tag/v2.43.0


### `test-kitchen` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["Your IaC tooling (Terraform, Ansible) has its own mature testing story."]</code> | <code>["Your IaC tooling (Terraform, Ansible) has its own mature testing story.", "You cannot isolate test drivers, virtualization or cloud credentials; their dependencies and images carry separate licences."]</code> |
| `license_spdx` | <code>null</code> | <code>"Apache-2.0"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L18", "legacy:devopstools_final.md#L1041"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L18", "legacy:devopstools_final.md#L1041", "https://github.com/test-kitchen/test-kitchen/blob/v4.1.5/LICENSE", "https://github.com/test-kitchen/test-kitchen/blob/v4.1.5/README.md", "https://github.com/test-kitchen/test-kitchen/releases/tag/v4.1.5"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Test infrastructure code on various platforms."</code> | <code>"Ruby integration testing framework that provisions and verifies infrastructure code on isolated test targets."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/test-kitchen/test-kitchen/blob/v4.1.5/LICENSE
- https://github.com/test-kitchen/test-kitchen/blob/v4.1.5/README.md
- https://github.com/test-kitchen/test-kitchen/releases/tag/v4.1.5


### `testcontainers` — RETAIN REVIEW

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["Your CI runners can't run Docker (rootless or DinD) or tests are purely unit-level."]</code> | <code>["Your CI runners can't run Docker (rootless or DinD) or tests are purely unit-level.", "You assume one licence covers every Testcontainers language library and commercial service.", "Your CI cannot safely run a supported container runtime or isolate privileged containers and external resources."]</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L19", "legacy:devopstools_final.md#L1043"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L19", "legacy:devopstools_final.md#L1043", "https://github.com/testcontainers/testcontainers-java/blob/2.0.5/LICENSE", "https://github.com/testcontainers/testcontainers-go/blob/main/LICENSE", "https://github.com/testcontainers/testcontainers-node/blob/main/LICENSE", "https://github.com/testcontainers/testcontainers-python/blob/main/LICENSE.txt", "https://github.com/testcontainers/testcontainers-python/blob/main/pyproject.toml"]</code> |
| `summary` | <code>"Libraries for integration tests using disposable containers; OSS core with paid cloud add-ons."</code> | <code>"Multi-language libraries for integration testing with disposable containers; language libraries and paid cloud offerings have separate licences."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/testcontainers/testcontainers-java/blob/2.0.5/LICENSE
- https://github.com/testcontainers/testcontainers-go/blob/main/LICENSE
- https://github.com/testcontainers/testcontainers-node/blob/main/LICENSE
- https://github.com/testcontainers/testcontainers-python/blob/main/LICENSE.txt
- https://github.com/testcontainers/testcontainers-python/blob/main/pyproject.toml


### `vitest` — CLEAR

| Modified field | Original | Proposed local value |
|---|---|---|
| `avoid_when` | <code>["You're not in the Vite ecosystem and Jest works fine."]</code> | <code>["You're not in the Vite ecosystem and Jest works fine.", "You cannot satisfy the Node and Vite compatibility requirements or plan to use v5.1 prereleases as stable versions."]</code> |
| `license_spdx` | <code>null</code> | <code>"MIT"</code> |
| `needs_review` | <code>true</code> | <code>false</code> |
| `sources` | <code>["legacy:7_Development-Collaboration/README.md#L23", "legacy:devopstools_final.md#L1047"]</code> | <code>["legacy:7_Development-Collaboration/README.md#L23", "legacy:devopstools_final.md#L1047", "https://github.com/vitest-dev/vitest/blob/v5.0.5/LICENSE", "https://github.com/vitest-dev/vitest/blob/v5.0.5/package.json", "https://github.com/vitest-dev/vitest/releases/tag/v5.0.5"]</code> |
| `status` | <code>"needs-review"</code> | <code>"active"</code> |
| `summary` | <code>"Blazing fast Vite-native unit testing framework."</code> | <code>"Vite-native JavaScript and TypeScript test runner with component, watch and optional browser testing modes."</code> |
| `verified_on` | <code>"2026-08-03"</code> | <code>"2026-10-26"</code> |

**Primary upstream evidence retained in updated `sources`:**

- https://github.com/vitest-dev/vitest/blob/v5.0.5/LICENSE
- https://github.com/vitest-dev/vitest/blob/v5.0.5/package.json
- https://github.com/vitest-dev/vitest/releases/tag/v5.0.5


**Publication checkpoint:** This local change log is not itself evidence of test/CI completion. After the official local generator and full QA pass, review the final diff, push through an explicit human-authorized commit, obtain fresh PR CI + independent P1/P2 review and a new strict full URL audit on the exact final SHA before a human merge decision.
<!-- WAVE25_APPLIED_CANONICAL_CHANGELOG_END -->
