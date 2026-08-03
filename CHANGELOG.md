# Changelog

All notable catalogue architecture and governance changes are recorded here. Individual tool metadata changes remain visible in Git history and pull requests.

## Unreleased

### Notes

- No post-v0.2.0 changes recorded yet.

## [0.2.0] - Draft

### Planned release title

- DevOps Tools Catalogue v0.2.0 - Wave 1 Evidence Reconciliation and Strict Link Audit Refresh

### Scope

- Completes Wave 1 reconciliation for the immutable 100-ID review plan across Batch 01..05.
- Refreshes strict full-link audit artefacts and unresolved strict-item ledger.
- Prepares release-candidate metadata and governance updates without publishing a tag/release.

### Notes

- Final Wave 1 selected-ID outcomes: 94 active, 6 needs-review, 0 archived.
- Strict unresolved link classes total 38 (`manual-verification-required`, `http-error`, `tls-failure`, `repository-archived`).
- This is a draft entry; do not publish a tag or GitHub release without explicit owner approval.
- Issue #2 remains open for human verification of unresolved strict items.

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
