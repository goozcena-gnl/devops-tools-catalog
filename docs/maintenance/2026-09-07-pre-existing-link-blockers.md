# Pre-existing strict-link blockers — 2026-09-07

PR #52's exact-head audit and a matching audit of its `main` base both reported the same unbaselined
Firecracker documentation failure, proving that PR #52 did not introduce it. The earlier KubeGUI failure
did not reproduce.

## Findings

| URL | Revalidation | Classification | Action |
|---|---|---|---|
| `https://kubegui.net` | Fresh unrestricted audits returned HTTP 200. | `TRANSIENT` | No catalogue change. |
| Firecracker `docs/README.md` | The path returns HTTP 404. The maintained [Firecracker README](https://github.com/firecracker-microvm/firecracker/blob/main/README.md) links to the current [getting-started guide](https://github.com/firecracker-microvm/firecracker/blob/main/docs/getting-started.md). | `PRE_EXISTING` | Replace the canonical documentation URL and historical evidence link with the official getting-started guide; retain the removed path as non-link provenance text. |

The canonical Firecracker repository, project status, licence, and all unrelated catalogue metadata remain
unchanged. The strict-link baseline is not modified.

## Validation

- Fresh strict audit before correction: one new blocker (Firecracker) and nine known/baselined blockers.
- KubeGUI: valid, HTTP 200.
- `python -m pytest`: 369 passed.
- `python -m scripts.generate_docs --check`: pass.
- `python -m scripts.validate_catalog`: pass.
- `python -m ruff check scripts tests`: pass.
- `python -m ruff format --check scripts tests`: pass.
- `git diff --check`: pass.
- Fresh unrestricted strict audit after correction: `blocking_new: 0`, `blocking_known: 9`, `strict_result: PASS`.
- Cached strict audit: the same blocker counts and `strict_result: PASS`.
