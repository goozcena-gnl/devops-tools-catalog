# Changelog

All notable catalogue architecture and governance changes are recorded here. Individual tool metadata changes remain visible in Git history and pull requests.

## [0.2.1] - Draft

Release-candidate metadata for the merged v0.2.1 remediation sequence. Tag and GitHub Release publication remain pending explicit owner approval after this finalization PR is merged.

### Scope

- Completed all approved remediation batches A1, A2, B, C1, C2, and D across immutable plan scope.
- Reconciled 80 planned rows and 80 reviewed rows with 73 unique IDs.
- Confirmed zero unreviewed rows, zero lost IDs, zero new IDs, and zero non-selected changed IDs.

### Canonical changes

- Total changed canonical IDs: 10.
- Total changed canonical fields: 10.
- URL/documentation/repository replacements (5): `deeptutor.official_url`, `odysseus.official_url`, `terraform-cloud.official_url`, `trivy.documentation_url`, `yokecd.repository_url`.
- Batch B `needs_review` resolutions (5): `cdktf`, `kaniko`, `keptn`, `kubeapps`, `tnu` changed from `true` to `false`.
- Reviewed-but-unchanged unique IDs: 63.
- Machine/API canonical replacement candidates remain 0.

### Governance and regression hardening

- Preserved evidence-first governance and immutable-scope batch accounting.
- Included pinned-baseline regression hardening in PR #22 without changing canonical batch decisions.
- Retained unresolved boundaries rather than guessing replacements when evidence remained inconclusive.

### Remaining evidence boundaries

- Issue #2 remains open.
- Archived-governance boundaries remain for `grafana-oncall`, `juju`, `kubernetes-dashboard`, and `minio`.
- Access/retry-dependent boundaries remain across retained C1/C2 unresolved records.
- Licence/lifecycle ambiguity boundaries remain for `autopwn-suite`, `cai-robotsec`, `ctop`, `elastic-apm-server`, and `elastic-stack-elk`.

This draft entry does not claim that all catalogue URL or lifecycle debt is resolved.

## [0.2.0] - 2026-08-04

Publication metadata finalized on 2026-08-04. Tag and GitHub Release publication will follow after this release commit is merged and explicitly approved.

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
