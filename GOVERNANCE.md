# Governance

DevOps Tools Catalog is maintained by `goozcena-gnl` with evidence-first review
and a lightweight contribution process suitable for a single-maintainer
project.

## Decision model

The maintainer is responsible for releases, repository settings, taxonomy and
schema changes, and final merge decisions. Contributors can propose records,
corrections, lifecycle changes, decision guidance, tests, and maintenance-tool
improvements through focused issues and pull requests.

Review decisions prioritize:

1. primary-source evidence and accurate ownership boundaries;
2. canonical identity, duplicate prevention, and preserved provenance;
3. explicit uncertainty rather than inferred maturity or licensing;
4. deterministic generation and passing automated validation;
5. operational usefulness across the catalog's engineering roles.

Disagreement is resolved against the documented
[methodology](docs/methodology.md). When evidence is incomplete, the record
remains under review or the proposal is held; merge speed is not a reason to
weaken the evidence standard.

## Changes and releases

Meaningful changes are reviewed through pull requests. Generated documentation
must match canonical YAML before merge. Releases follow the version already
declared in `pyproject.toml` and `CHANGELOG.md`; repository publication or a
branding change does not by itself justify a new semantic version.

Security reports follow [SECURITY.md](SECURITY.md). Repository licensing and
third-party boundaries are documented in
[docs/licensing.md](docs/licensing.md).
