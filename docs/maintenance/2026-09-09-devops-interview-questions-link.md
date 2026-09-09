# DevOps Interview Questions endpoint repair

Reviewed on 2026-09-09 against main
`57fa10b737077c0d1c5b0f0f7aecb05df63ec05a`, independently of Wave 4 PR #54.

The repository auditor returned HTTP 404 for
`https://interview.devopscommunity.in`, first with HEAD and then with its supported
GET fallback. Web retrieval separately exposed the interview page, so the
checker-visible failure is not evidence that the project has retired.

The interview page's GitHub link identifies
[rohitg00/devops-interview-questions](https://github.com/rohitg00/devops-interview-questions).
That repository's homepage points back to the interview site, and its README
contains the actual questions across Docker, Kubernetes, CI/CD, cloud, Linux and
other operational topics. The same owner's
[DevOpsCommunity resource list](https://github.com/rohitg00/DevOpsCommunity)
links to this interview repository; the broader community is not a replacement
identity. No official superseding interview site was found.

GitHub reports the interview repository as neither archived nor disabled, with
default branch `main`. The latest commit is `487d03ae6c` from 2025-05-28; open
issues and pull requests have activity through 2026-05-17. Those observations
establish an available upstream with contribution activity, not a guarantee of
active maintainer response or current accuracy of every answer.

The repository has no root licence file, its licence metadata is null, and the
licence API returns 404. The MIT licence of the separate DevOpsCommunity
repository must not be applied to these interview questions. Preserve
`license_model: documentation`, no SPDX, `status: needs-review`,
`needs_review: true`, and unknown maturity. The verification date records this
endpoint review, not a full content or licensing approval.

Use the interview repository for both `official_url` and `repository_url`, with
its README as `documentation_url`, following existing repository-endpoint
conventions. Record `repository_archived: false`. Keep the old site URL in
`sources` and preserve both legacy pointers and both migration reconciliation
rows unchanged. No alias is needed to preserve these existing historical rows.

This repair changes one canonical record and no cardinality, taxonomy, schema,
release metadata, link-audit baseline or Wave 4 content.
