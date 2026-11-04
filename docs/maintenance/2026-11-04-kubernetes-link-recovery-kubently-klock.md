# 2026-11-04 — Kubernetes link recovery: Kubently and kubectl-klock

## Frozen baseline and isolation

- Base `main`: `80109d5b83ec147f7c0c1556b269386aa7acf05c`.
- Branch: `maintenance/kubernetes-link-recovery-kubently-klock`. Independent from Wave 36 PR #163.
- Existing exact record cohort: `kubently`, `kubectl-klock`; no ID additions/deletions or other record changes.
- Do not edit the link-audit baseline, ignore statuses, the checker, legacy provenance, unverified licence, or status flags.

## Motivation: reproducible failed-link evidence

- Full link audit runs [#41821969124](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/41821969124) and [#41824803975](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/41824803975) at Wave36 SHA `b8d93738f389e822ab2172f3ea0e4a0a2cdab04b`: `blocking_new: 3`, `blocking_known: 6`, `strict_result: FAIL`.
- `https://kubently.io`: HEAD 526, GET 526; `https://kubently.io/guides/quick-start/`: HEAD 526, GET 526.
- `https://software.opensuse.org/package/kubectl-klock`: HEAD 400, GET 403.
- These are observed transient/service-dependent failures, not evidence of project discontinuation. No blanket link-check suppression.

## Authoritative primary sources and scoped edits

### `kubently`

- [Canonical upstream project](https://github.com/kubently/kubently) remains an active, unarchived source.
- [Upstream quick start](https://github.com/kubently/kubently/blob/main/docs/QUICK_START.md) provides current instructions.
- Set `official_url` to the maintained canonical GitHub project and `documentation_url` to its maintainer-authored Quick Start. Preserve `repository_url` and historic original domain references in `sources`; they are retained for evidence/history, not current navigation.
- Do not change its Apache-2.0 licence evidence, deployment models, status or review flag.

### `kubectl-klock`

- [Original maintainer's README](https://github.com/applejag/kubectl-klock/blob/main/README.md) describes a kubectl plugin that makes the `kubectl get ... --watch` stream easier to read; it does not lock Kubernetes resources or prevent deletion.
- Set `official_url` to its maintainer's existing GitHub project and correct `summary`, `use_when`, and `avoid_when` to reflect watch display, not admission controls. Add maintainer README to `sources`.
- Keep `status: needs-review`, `needs_review: true`, `license_model: oss` and missing `license_spdx`; README's CC-BY-4.0 comment describes README document, not a sufficient basis to infer software licence.
- Preserve original `legacy:` sources and existing `repository_url`.

## Deterministic output and inventory invariants

- Regenerate category, role and lifecycle Markdown from canonical YAML, never hand-edit generated Markdown as source-of-truth.
- Expected generated changed paths are the two category pages, lifecycle `deploy`/`operate`, and role `kubernetes-engineer`/`platform-engineer`/`site-reliability-engineer`.
- Canonical inventory remains **1,425**; `README.md` and `docs/catalog-statistics.json` are invariant. Review debt, licences, statuses, all other raw YAML records and each original `legacy:` line remain unchanged.

## Validation and human gates

- Before Ready: run `python -m scripts.generate_docs --check`, `python -m scripts.validate_catalog`, `python -m ruff check scripts tests`, `python -m ruff format --check scripts tests`, `python -m pytest`, `python -m pip check`, and `git diff --check`. Compare regenerated paths, all unaffected record blocks, and inventory.
- Run a fresh strict link audit on this branch's **final SHA** and retain artifact digest, `blocking_new`, `blocking_known`, `strict_result`.
- Any failures: stop, no Ready or merge. PR starts **Draft**. Do not merge without separate explicit authorization. Wave 36 #163 stays unchanged; even if this fix later merges, its changes must first be integrated/revalidated in Wave36 before considering Wave36 merge.
