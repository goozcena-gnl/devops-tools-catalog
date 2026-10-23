# Wave 22 — Container image and reproducible build evidence review

Date of preliminary triage: 2026-10-23. Tracker: [#134](https://github.com/goozcena-gnl/devops-tools-catalog/issues/134). Pinned baseline main: `d5686944f9125809bb0b239889c0c833b4feaf8b`.

> **PRELIMINARY EVIDENCE ONLY — 0/10 CLEARED.** None of the ten records is modified or approved yet. Every one retains `status: needs-review`, `needs_review: true`. This ledger is the preparatory evidence and outstanding work for a Draft PR; not a licence/legal assessment or maintenance guarantee.

## Scope and baseline

- Exactly ten existing selected IDs in `data/tools/containers-image-tooling.yaml`: `cek`, `distroless`, `docker-build`, `docker-buildx`, `earthly`, `ko`, `nix`, `shipwright`, `skopeo`, `werf`.
- Exclude `gradle` and `sbt`, all other canonical IDs, the N2a historical test and all existing generated files at this stage.
- Baseline: **1,425** canonical records, **774 active**, **637 needs-review**, **30** categories; no PR open before the Wave 22 branch was created.
- Last post-merge main gates all green ([quality](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/39990441093), [secret scan](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/39990440998), [Plumber](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/39990440867), [CodeQL](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/39990440089)).
- Six known URL blockers and their classifications are governed by [#2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2); baseline `config/link-audit-baseline.json` MUST remain unchanged. Prior [strict audit #32](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/39988339034) applies to the preceding Wave 21 PR head, **not to any future Wave 22 final SHA**.

## Preliminary source observations and mandatory follow-up

The checks below inspected upstream repository metadata as of 2026-10-23, and, where available, a specific official tagged `LICENSE` plus release. A GitHub API licence label or boilerplate text **does not by itself establish** a final complete source/binary distribution grant, exception set, maintenance commitment, commercial rights, or full licence scope.

| ID | Source evidence checked | Preliminary evidence, not a decision | Required independent verification before CLEAR |
|---|---|---|---|
| `cek` | [v0.3.0 LICENSE](https://github.com/bschaatsbergen/cek/blob/v0.3.0/LICENSE), [release](https://github.com/bschaatsbergen/cek/releases/tag/v0.3.0) | Explicit MIT text checked; v0.3.0 published 2026-09-13; repo not archived and pushed 2026-10-15. | Actual release binaries/source match, tool behavior/security of OCI layer processing, provenance, supported platforms, any vendored assets. |
| `distroless` | [main LICENSE](https://github.com/GoogleContainerTools/distroless/blob/main/LICENSE), [repository](https://github.com/GoogleContainerTools/distroless) | Apache-2.0 source LICENSE; repository active 2026-10-22. This says **nothing** about every image layer/dependency. | Determine precisely which variants exist, base image provenance, image-level licences, SBOM/signing, release and runtime/debug distinctions. |
| `docker-build` | [official Docker Build guide](https://docs.docker.com/build/), [Buildx repo](https://github.com/docker/buildx), [BuildKit repo](https://github.com/moby/buildkit) | Docker Build is an umbrella build capability; Buildx plugin and BuildKit backend are separate existing components. | Retain an honest umbrella description rather than copying a component's licence or repo identity; verify edition/service and builder capabilities independently. |
| `docker-buildx` | [Buildx v0.38.1 LICENSE](https://github.com/docker/buildx/blob/v0.38.1/LICENSE), [release](https://github.com/docker/buildx/releases/tag/v0.38.1), [BuildKit v0.34.1 LICENSE](https://github.com/moby/buildkit/blob/v0.34.1/LICENSE) | Apache-2.0 source grant; Buildx v0.38.1 and BuildKit v0.34.1 released 2026-10-20, different projects and version streams. | Builders/drivers, multi-arch and cache/security boundaries, tags and backends supported, commercial Docker service dependencies. |
| `earthly` | [v0.8.16 LICENSE](https://github.com/earthly/earthly/blob/v0.8.16/LICENSE), [release](https://github.com/earthly/earthly/releases/tag/v0.8.16), [upstream service shutdown announcement](https://earthly.dev/blog/shutting-down-earthfiles-cloud/) | MPL-2.0 at tagged source; v0.8.16 published 2025-07-16. An upstream maintenance/service-sunset announcement requires **priority lifecycle verification**; repo not archived is insufficient evidence of support. | Re-read official dated statement, identify affected services vs local OSS CLI and ongoing security support. Avoid automatic `active` or `archived` inference; decide status from primary evidence. |
| `ko` | [v0.19.1 LICENSE](https://github.com/ko-build/ko/blob/v0.19.1/LICENSE), [release](https://github.com/ko-build/ko/releases/tag/v0.19.1) | Apache-2.0 source licence, published 2026-06-29; repository changes 2026-10-15. | Go-only scope, registry/credential permissions, SBOM, reproducible image claims, actual tagged features. |
| `nix` | [Nix COPYING](https://github.com/NixOS/nix/blob/master/COPYING), [upstream](https://github.com/NixOS/nix) | LGPL v2.1 boilerplate is present; GitHub metadata says `LGPL-2.1` but does **not** settle exact SPDX variant; repo active 2026-10-23. | Source headers, explicit `-only`/`-or-later` grant, experimental flakes semantics, difference between Nix, nixpkgs, NixOS and OCI integrations. |
| `shipwright` | [shipwright-io/build README](https://github.com/shipwright-io/build/blob/main/README.md), [v0.21.10 LICENSE](https://github.com/shipwright-io/build/blob/v0.21.10/LICENSE), [release](https://github.com/shipwright-io/build/releases/tag/v0.21.10) | README explicitly identifies Kubernetes image building; Apache-2.0 source; published v0.21.10 on 2026-10-21. | Verify ownership/relationship to website, supported build CRDs and strategy controllers, privileges/RBAC, versioned security support and maturity. |
| `skopeo` | [old repository](https://github.com/containers/skopeo), [new repository](https://github.com/podman-container-tools/skopeo), [v1.24.1 LICENSE](https://github.com/podman-container-tools/skopeo/blob/v1.24.1/LICENSE) | Old API request returned a *Moved Permanently* response to GitHub repository ID 53356367; newer upstream repo was created 2016-03-07, not archived, v1.24.1 published 2026-09-16; Apache-2.0 tagged license. **Redirect alone is not enough** to finalize canonical migration. | Verify repository ID and owner-approved transfer with original maintained historical provenance; check docs/releases and exact inspect/copy/sync/sign operations; no migration until proved. |
| `werf` | [v2.81.4 LICENSE](https://github.com/werf/werf/blob/v2.81.4/LICENSE), [release](https://github.com/werf/werf/releases/tag/v2.81.4), [website](https://werf.io) | Apache-2.0 tagged source and 2026-10-09 release; repository updated 2026-10-23. | Verify build vs deploy responsibilities, Helm/Kubernetes release boundary, provenance/secrets and supported version range before changing metadata. |

## Decision ledger (not yet started)

| ID | Decision | Reason |
|---|---|---|
| `cek` | PENDING | Full primary-source capability/release review outstanding |
| `distroless` | PENDING | Distributed image/component licensing and SBOM review outstanding |
| `docker-build` | PENDING | Umbrella identity and licence boundary unresolved |
| `docker-buildx` | PENDING | Backend/driver/version boundaries outstanding |
| `earthly` | PENDING | Upstream maintenance/sunset boundary outstanding — high priority |
| `ko` | PENDING | Tagged feature/security boundaries outstanding |
| `nix` | PENDING | Licence grant exact variant and product boundaries outstanding |
| `shipwright` | PENDING | Product identity and Kubernetes security boundaries outstanding |
| `skopeo` | PENDING | Official relocation/owner continuity — high priority |
| `werf` | PENDING | Version and distribution/CI boundaries outstanding |

## Completion gates (no bypass)

1. Re-check exact baseline and ten IDs before every canonical edit. Never infer identity or rewrite legacy sources from similar names or redirects.
2. For each ID provide field-level before/after ledger, tagged primary links, legal/version/operation conclusions and **CLEAR** or **RETAIN REVIEW**. If insufficient, keep both `status: needs-review` and `needs_review: true`. Avoid a target clearance quota.
3. Restrict canonical edits to these ten existing IDs in the one named YAML. Generated pages must be generated with `python -m scripts.generate_docs`, never manually edited. Keep the historical N2a tests and URL audit baseline unchanged.
4. Run a clean locked Python 3.12 checkout: `pip check`, constraint verification, Ruff check/format, full pytest, `python -m scripts.generate_docs --check`, catalogue validation and `git diff --check`. Record exact SHA and the output list.
5. Independent P1/P2 review; all GitHub CI checks green on the **final PR SHA**, followed by a fresh strict Full link audit on that SHA with `strict_result: PASS`, `blocking_new: 0`, unchanged six historic blocker URL/classification pairs. Audit report/source URLs independently as needed.
6. Keep PR **Draft, not merged** until explicit human merge decision. No auto-merge, tag/release, branch-protection bypass or closure of #2; after approved merge, verify four `main` workflows before closing #134.

**Status: evidence triage prepared, no canonical approvals and no authoritative lifecycle decisions yet.**
