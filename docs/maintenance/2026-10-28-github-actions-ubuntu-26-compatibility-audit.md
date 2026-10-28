# GitHub Actions — Ubuntu 26.04 compatibility audit (first canary)

**Date:** 2026-10-28 (Europe/Paris). **Phase:** isolated CI experiment, no production workflow migration. **Baseline `main`:** `ccfaac6fcdba0305066420ffbdee0cac0b2f7043`.

## Goal and official migration notice

GitHub announced that the `ubuntu-latest` x64 label will gradually move from Ubuntu 24.04 to 26.04 **between 2026-10-19 and 2026-11-19**. GitHub's `ubuntu-26.04` hosted runner is generally available, and the migration notice explicitly recommends testing using that label or pinning `ubuntu-24.04` temporarily if regressions occur.

Primary sources:
- https://github.com/actions/runner-images/issues/14748
- https://github.com/actions/runner-images/issues/14747
- https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2604-Readme.md
- https://github.com/actions/runner-images/blob/main/README.md

Last known post-Wave-29 `Catalogue quality` post-merge workflow used Ubuntu **24.04.5 LTS**, from its own runner logs, with successful tests. This is *not* evidence of compatibility with Ubuntu 26.04.

## Exact workflow inventory

| Workflow | Runner observed in YAML | Trigger / exposure | Main dependency or risk |
|---|---|---|---|
| `quality.yml` | `ubuntu-latest` | PR + push to main | Python 3.12, pinned wheels, full pytest, docs and schema tools; OS ABI and pip compatibility |
| `secret-scan.yml` | `ubuntu-latest` | PR + push + weekly schedule | Docker daemon and immutable Gitleaks container digest |
| `link-check.yml` | `ubuntu-latest` | workflow_dispatch + weekly schedule | Python 3.12; external DNS, TLS, HTTP and token rate limits; network variability |
| `python-freshness.yml` | `ubuntu-latest` | path-filtered PR + weekly schedule + dispatch | Fresh PyPI resolution under Python 3.12, which may drift independently of OS |
| `plumber.yml` | `ubuntu-24.04` | PR + push + dispatch | Intentionally pinned; **not** impacted by the moving `ubuntu-latest` label |

All five workflows retain pinned action commit hashes and least-privilege permissions. `actions/setup-python` selects Python 3.12 explicitly in the relevant Python workflows; do not accidentally test the runner's default system Python version instead.

## Risk assessment before canary

**Highest operational exposure:** quality and Gitleaks run on every PR and push, so a runner migration could break required status checks. **Medium:** scheduled full network link audit may be sensitive to OpenSSL/TLS and host network behaviour; its six historical blocking links do not imply new OS failures. **Medium:** dependency freshness can fail for genuine upstream release drift on either OS. **Low:** Plumber is explicitly pinned to `ubuntu-24.04` and should not be changed without an independent reason.

Packages with compiled artifacts such as `rpds-py`, `PyYAML`, and `ruff` can be affected by platform compatibility despite identical Python 3.12 pins. Gitleaks is a digest-pinned OCI image but relies on a working Docker host and volume mount.

## Canary experiment

**New and only executable addition:** `.github/workflows/ubuntu26-canary.yml`. It uses a strict GitHub-hosted runner matrix:

- `ubuntu-24.04` — control.
- `ubuntu-26.04` — explicit new image (not `ubuntu-latest`).

On each runner, the canary checks the actual host OS, Docker access, installs the exact CI constraints, verifies all **19** locked Python dependencies, checks Ruff and formatting, runs the **full pytest suite**, validates generated documentation, the catalogue and the review-debt report, smoke-tests link-audit CLI import, runs the **same digest-pinned Gitleaks container command** as `secret-scan.yml`, then checks PR whitespace.

The canary runs on PR changes to its workflow/report or via `workflow_dispatch` after inclusion on the default branch. It has `contents: read` only, no secret tokens, no write permissions, no maintenance of production runners, no external scan of catalogue websites, and no authentication against other systems.

**Not covered by canary:** end-to-end external link audit with real remote website requests; the fresh PyPI dependency resolver operation (as opposed to validating existing pins); Plumber (already pinned to 24.04); GitHub's built-in CodeQL analysis action; all behaviour of external services. Their existing CI and weekly workflows still apply. Do not infer they passed under 26.04 merely because this canary passes.

## Decision gate

1. Open a Draft PR from the canary branch only. Confirm two-file diff and no canonical YAML, generated docs, link baseline, secrets, issues or production workflow changes.
2. Confirm **both** OS matrix jobs run to completion on the expected `ubuntu-24.04` and `ubuntu-26.04` images; inspect runner-image and Python version logs, full tests, locked dependency validation and Docker/Gitleaks.
3. Any Ubuntu-26-only failure => retain production `ubuntu-latest` temporarily **or** explicitly pin affected jobs to `ubuntu-24.04` in a separate, reviewed mitigation PR; investigate failure first. Never suppress meaningful checks to make the matrix green.
4. If both pass, document compatibility within the tested scope. No immediate switch to 26.04 is necessary: the intended `ubuntu-latest` migration can proceed; optionally plan a follow-up that pins OS versions if reproducibility requires it.
5. Merge only after human review and normal security/quality CI. No direct merge, no automatic issue closure, no baseline modification.

**Initial status: CANARY PREPARED — WAITING FOR GITHUB ACTIONS EVIDENCE.** Do not report Ubuntu 26.04 PASS until the run finishes successfully on the explicit label.
