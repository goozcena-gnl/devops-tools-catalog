# Changelog

All notable catalogue architecture and governance changes are recorded here. Individual tool metadata changes remain visible in Git history and pull requests.

## Unreleased

### Notes

- No post-v0.2.0 changes recorded yet.

## [0.2.0] - 2026-08-04

Publication metadata finalized; tag and GitHub Release remain pending explicit owner approval.

### Scope

- Completed five Wave 1 evidence-verification batches (PRs #9, #10, #11, #12, #13) following the approved plan (PR #8).
- Reconciled all 100 immutable planned records with conservative, evidence-backed lifecycle, licensing/SPDX, documentation, and URL metadata updates.
- Finalized Wave 1 completion and release-candidate metadata in PR #14, then hardened machine-API detection behavior in PR #15.

### Highlights

- Wave 1 selected-record outcomes are 94 active, 6 needs-review, and 0 archived.
- Applied project/repository identity corrections and authoritative-source URL/documentation normalization.
- Preserved explicit product-boundary treatment for OSS, open-core, source-available, and commercial offerings.
- Corrected Markdown metadata rendering details (including explicit `<br>` handling) in generated documentation paths.
- Added focused lifecycle and regression coverage for verification decisions and link-review safety guards.
- Refreshed strict link-audit artefacts and reconciled unresolved strict-item tracking.
- Sanitized `candidate_replacement_url` semantics to keep machine/API probe endpoints as evidence only.
- Hardened link-review machine-API endpoint detection to avoid hostname-boundary false positives.

### Remaining verification debt

- Issue #2 remains open for unresolved strict and manual link verification follow-up.
- Strict unresolved classes remain: `manual-verification-required: 25`, `http-error: 2`, `tls-failure: 1`, `repository-archived: 10` (total 38).
- Additional unresolved classes remain tracked: `rate-limited: 19`, `restricted-or-bot-blocked: 11`, plus transient and DNS-inconclusive cases.
- `elastic-stack-elk` and `exoway` remain under conservative `needs-review` lifecycle status.
- Additional catalogue records outside the Wave 1 immutable scope remain under progressive evidence review.

## [0.1.0] - Draft

### Planned release title

- DevOps Tools Catalogue v0.1.0 - Canonical Model and Deterministic Docs Baseline

### Scope

- First baseline release of canonical catalogue architecture and deterministic documentation pipeline.
- Includes post-bootstrap dependency maintenance updates from merged Dependabot PRs #3, #4, #5, and #6.

### Added

- Canonical YAML catalogue and normalized taxonomy.
- Deterministic category, role, lifecycle, and root documentation generation.
- Legacy source inventory and occurrence-level reconciliation ledger.
- Schema, catalogue, link, drift, and secret validation.
- Secure pull-request quality and scheduled link-audit workflows.
- Contribution, security, decision-guide, and default-stack documentation.

### Notes

- This is a pre-release preparation entry; do not publish a tag or GitHub release until owner approval.
- Unresolved URL and lifecycle follow-up remains tracked in issue #2.
