# Catalogue methodology

## Purpose and scope

This repository is an evidence-backed, curated reference for operational
engineering work. It does not claim to list every product or project. Inclusion
requires a concrete use case for at least one defined role.

## Source of truth

Canonical records live in `data/tools/*.yaml`; `data/taxonomy.yaml` defines valid categories, roles, lifecycle stages, licence models, status values, and maturity values. Markdown category, role, lifecycle, reconciliation, and root pages are generated.

## Inclusion criteria

A record should demonstrate operational relevance, legitimate ownership, usable documentation, a defined audience, and a capability not already represented by an equivalent canonical record. Maintenance status, security posture, licence clarity, adoption, and deployment burden affect maturity and decision guidance.

Obscure or experimental projects require stronger evidence. Keyword overlap with “DevOps”, “AI”, “Kubernetes”, or “cloud” is not sufficient.

## Evidence order

Prefer, in order:

1. official documentation;
2. official project or product site;
3. official source repository;
4. official licence file;
5. official foundation or vendor announcement.

Third-party listicles, badges, star counts, and generated summaries are discovery aids, not authoritative evidence. Unknown facts remain `unknown`; records awaiting primary-source review use `needs_review: true` and status `needs-review`.

The `verified_on` date records when cited information was checked. It is not a guarantee that every imported claim is correct forever.

Review debt is a first-class catalog state. It must not be cleared because a
record appears plausible, because a URL currently responds, or to improve public
statistics. Use `python -m scripts.review_debt` to inspect and prioritize the
deterministic queue; resolve an item only when the canonical record captures the
required primary evidence.

## Identity and duplicates

Identity uses normalized official and repository URLs, canonical names, and versioned aliases. A tool spanning multiple domains has one record with multiple categories. Product suites, managed services, runtimes, plugins, and forks remain separate only when their operational decisions differ.

Aliases and reviewed exceptions live in `config/import-overrides.yaml`. Every legacy occurrence remains traceable through `migration/reconciliation.csv` and each record’s `sources`.

## Licence and offering model

`license_model` describes the reviewed distribution or offering: OSS, source-available, open-core, commercial, free SaaS, documentation, or unknown. `license_spdx` is added only when supported by reliable licence evidence. Source visibility alone never proves an OSS licence.

This upstream classification is distinct from the repository's own MIT licence.
Listed tools, names, linked content, and trademarks remain with their respective
owners. See [licensing and attribution](licensing.md).

## Lifecycle

Active tools require current primary-source evidence. Deprecated, archived, and historical tools are retained for migrations and context but excluded from default recommendations. Scheduled link checks can flag candidates; they do not autonomously mark a project dead after a transient HTTP failure.

## Migration status

The initial source was an already-extracted folder; no RAR file was available in the workspace. The importer supports traversal-checked temporary RAR extraction for reproducibility. The legacy consolidated file contained 1,109 occurrences, category files contained 785, and five reviewed alias groups reduced 1,097 normalized primary URLs to 1,092 canonical records.

All initially imported records remain marked for review because the legacy badges and descriptions were not treated as primary-source verification.
