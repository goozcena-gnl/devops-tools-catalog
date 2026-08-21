# Changelog

All notable catalogue architecture and governance changes are recorded here. Individual tool metadata changes remain visible in Git history and pull requests.

## [0.3.0] - 2026-08-21

### Scope

- Expanded the canonical catalogue from the v0.2.2 baseline to 1,229 records.
- Incorporated two major evidence-reviewed candidate waves.
- Preserved deterministic documentation generation and schema compatibility.

### Catalogue expansion

- Added 54 canonical records through PR #39.
- Added 83 canonical records through PR #40.
- Incorporated evidence-backed updates to existing records.
- Reconciled duplicate, alias, hosted-service, OSS/open-core, commercial, and lifecycle classifications explicitly.

### Quality and governance

- Completed independent semantic review and remediation before merge.
- Incorporated SPDX licence and offering-model corrections.
- Aligned contributor documentation with both Ruff lint and format CI checks through PR #41.
- Kept catalogue generation and validation deterministic.

### Remaining evidence boundaries

- The RepoD candidate remains held as `NEEDS_REVIEW` because authoritative upstream repository, licence, and ownership evidence is insufficient.
- Repository issue #2 remains open for unresolved catalogue URL review.
- Branch-protection controls remain unavailable for this private repository on the current GitHub plan.

This release does not claim that all catalogue evidence debt is resolved.

## [0.2.2] - 2026-08-12

Publication metadata finalized on 2026-08-12 after the approved v0.2.2 carryover review sequence. Tag and GitHub Release publication remain deferred until this release commit is merged and the repository owner separately approves publication.

### Scope

- Reconciled all 82 frozen planning rows across 63 unique IDs: 64 reviewed rows across 58 IDs and 18 N4 HOLD rows across 5 IDs.
- Confirmed zero lost IDs, zero new IDs, and zero non-selected changed IDs between the immutable v0.2.1 source and accepted v0.2.2 implementation result.
- Completed approved N1a, N1b, N2a, N2b, and N3a review workstreams. N4 was not executed and remains `HOLD_NO_NEW_EVIDENCE`.

### Canonical changes

- Changed 15 selected canonical fields across 14 IDs.
- Reviewed but retained 49 selected rows across 44 IDs.
- Regenerated 23 deterministic category, role, and lifecycle documents from the accepted canonical changes.
- Machine/API canonical replacement candidates remain 0.

### Remaining evidence boundaries

- Issue #2 remains open.
- N4 remains unresolved and on HOLD for `autopwn-suite`, `cai-robotsec`, `ctop`, `elastic-apm-server`, and `elastic-stack-elk` (18 field-level rows).
- Executed ledgers retain explicit access/retry, URL identity or migration, product/lifecycle/name, and archived-source governance follow-up boundaries where the approved evidence did not support broader changes.

This release does not claim complete catalogue URL, lifecycle, licence, or evidence-debt resolution.

## [0.2.1] - 2026-08-05

Publication metadata finalized on 2026-08-05 after completion of the v0.2.1 remediation sequence. Tag and GitHub Release publication follow from this release commit after explicit owner approval.

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

This release does not claim that all catalogue URL or lifecycle debt is resolved.

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
