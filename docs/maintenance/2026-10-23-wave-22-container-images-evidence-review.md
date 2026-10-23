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

## Second-pass upstream cross-check (2026-10-23)

This supplements, but does not replace, the original ten PENDING decisions. The narrower conclusions below are supported by identified primary sources; they do **not** clear any canonical record or authorize generated documentation edits.

### High-priority provenance and lifecycle evidence

**Earthly — confirmed sunset, but classification not yet finalized.** In its [2025-04-16 first-party announcement](https://earthly.dev/blog/shutting-down-earthfiles-cloud/), the company expressly states that active maintenance of Earthly OSS is ending, that normal contributions/PRs cease apart from critical fixes, and that Earthly Cloud/Satellite/Secrets/Logs services shut down by 2025-07-16. Its [official changelog](https://github.com/earthly/earthly/blob/main/CHANGELOG.md) identifies v0.8.16 (2025-07-16) as removing Cloud commands and dependencies while preserving local build capability (v0.8.15 may still emit Cloud errors). **Do not automatically mark archived, deprecated, or active solely from an unarchived GitHub repository or historical release.** Before any canonical edit, distinguish maintained security builds, usable local OSS features, and sunset proprietary services; retain `needs-review` until these are scoped.

**Skopeo — repository transfer identity now strongly verified.** The old [`containers/skopeo`](https://github.com/containers/skopeo) GitHub REST API endpoint responds `Moved Permanently` toward **repository ID `53356367`**. The API object for [`podman-container-tools/skopeo`](https://github.com/podman-container-tools/skopeo) has **the same immutable repository ID `53356367`**, with original creation timestamp `2016-03-07T20:23:29Z`. This is evidence of a transfer/rename of the **same GitHub repository**, not merely a matching project name. Its [current first-party README](https://github.com/podman-container-tools/skopeo/blob/main/README.md) documents remote inspect, copy, sync and registry authentication; tagged [v1.24.1 LICENSE](https://github.com/podman-container-tools/skopeo/blob/v1.24.1/LICENSE) contains Apache-2.0. This supports an eventual canonical URL correction while preserving historical source references, subject to the field-level review, correct source link attribution, and final independent CI/audit.

**Docker Build / Buildx / BuildKit — distinct scopes verified.** [Docker's official overview](https://docs.docker.com/build/concepts/overview/) states that Buildx is the build **client**, BuildKit is the execution **backend**, and `docker build` uses the default builder. The [builders reference](https://docs.docker.com/build/builders/) documents behavioral differences for `docker buildx build` when selecting custom builders. Both tagged Buildx v0.38.1 and BuildKit v0.34.1 source repos have Apache-2.0 LICENSE files; these are **not** proof of an umbrella `docker-build` item's standalone SPDX grant. A canonical summary can cite the technical boundary without merging existing IDs.

### Supply-chain and Kubernetes operation boundaries

- **Distroless:** [upstream README](https://github.com/GoogleContainerTools/distroless) describes keyless Cosign signatures and specifies the identity/issuer needed for verification. Images generally lack a shell and require JSON-vector entrypoints. Licence and SBOM of image constituents remain a **distinct** task from the repository's Apache-2.0 LICENSE.
- **ko:** [official guide](https://ko.build/) explicitly limits its strongest use case to Go applications without OS dependency/cgo-heavy needs; `ko` uses local `go build` and does not require a Docker daemon. [Official SBOM documentation](https://ko.build/features/sboms/) confirms SBOM generation/upload by default from v0.9, with `--sbom=none` available. [Authentication guidance](https://ko.build/get-started/) explains credentials via Docker config and cloud provider environments. Verify the exact selected release before putting new feature claims into a canonical record.
- **Shipwright:** [v0.20 BuildRun documentation](https://shipwright.io/docs/build/buildrun/) describes namespaced `BuildRun` resources and service-account secrets; the controller creates a Tekton `TaskRun`. [Strategy reference](https://shipwright.io/docs/build/buildstrategies) documents cluster-wide versus namespace strategy boundaries, and calls out privilege, AppArmor, Seccomp and `allowPrivilegeEscalation` restrictions for its BuildKit strategy. Documentation currently indicates version 0.20; do not infer all statements necessarily hold for the separately observed v0.21.10 tagged release without comparing their versioned CRDs/docs.
- **Nix:** `NixOS/nix` upstream `COPYING` is LGPL v2.1 boilerplate; the precise `LGPL-2.1-only` vs `LGPL-2.1-or-later` grant cannot be inferred from that alone. Require explicit upstream copyright or SPDX source headers.
- **cek, werf:** Official versioned licence files and releases were inspected during initial triage; capability, security, maintenance and commercial-edition details still need a separate full review before any clearance.

### Decision gate after second pass

**Initial second-pass position (superseded by the provisional decision section below): 0 CLEAR / 0 RETAIN finalized / 10 PENDING.** Evidence is strengthened for Earthly's announced maintenance sunset and Skopeo's repository transfer but neither finding alone proves every canonical field. No changes have yet been made to canonical YAML, generated outputs, the strict-link baseline, or the historical N2a test. Proceed in a full checkout with a ten-ID field-level matrix, conservative status decisions, official docs generation, locked Python 3.12 pytest/Ruff/validator, independent review, and strict URL audit on the final SHA.

## Provisional Wave 22 canonical decision ledger — 2026-10-23

**5 PROVISIONAL CLEAR / 5 RETAIN REVIEW**, subject to clean generation, complete Python 3.12 test suite, CI and independent reviewer scrutiny. This is a proposal, not approval to merge. Provisional clear: `cek`, `docker-buildx`, `ko`, `skopeo`, `werf`. Retain review: `distroless`, `docker-build`, `earthly`, `nix`, `shipwright`.

The five provisional clears have tagged primary upstream licence files and release/repository evidence, canonical identity and bounded technical descriptions; this **does not** certify product or package security. They are suitable for independent scrutiny of their source-licence/maintenance and product boundaries. The other five remain under review for material unresolved assertions (image-layer grants, umbrella product identity, ceased active OSS maintenance, LGPL `-only` vs `-or-later`, versioned Kubernetes operator privilege/strategy claims).

**Preliminary inventory after official generator (unverified until regeneration):** 1,425 total, 779 active, 632 needs-review. Existing records outside the exact ten IDs remain untouched; original legacy source lines are retained. No new canonical IDs, no URL baseline edits, no historical N2a changes. Skopeo points to the transferred GitHub repository of the same immutable repository ID; the old URL is retained as a source.

### Canonical changed-field matrix (previous `main` → Draft PR)

The following matrix is generated from a complete comparison of each selected ID's YAML block. `sources` field displays official primary URLs and original historical provenance; `status` and `needs_review` stay unchanged for retained records. This full ledger must be rechecked after any subsequent data correction.

| ID | Field | Before | Proposed after |
|---|---|---|---|
| `cek` | `summary` | Inspect OCI image filesystems and layers without running containers.;  | Read-only exploration of OCI container-image filesystem contents and layers without executing containers.;  |
| `cek` | `status` | needs-review;  | active;  |
| `cek` | `verified_on` | '2026-08-03';  | '2026-10-23';  |
| `cek` | `sources` | ;   - legacy:devopstools_final.md#L350;  | ;   - https://github.com/bschaatsbergen/cek/blob/v0.3.0/LICENSE;   - https://github.com/bschaatsbergen/cek/releases/tag/v0.3.0;   - https://github.com/bschaatsbergen/cek;   - legacy:devopstools_final.md#L350;  |
| `cek` | `needs_review` | true | false |
| `cek` | `license_spdx` | (absent) | MIT;  |
| `distroless` | `summary` | Minimal container images for secure deployments.;  | Minimal runtime container images without a shell or package manager in standard variants; separately published debug variants support troubleshooting.;  |
| `distroless` | `avoid_when` | ;   - '* You need to exec into containers for debugging or require OS-level packages at runtime.';  | ;   - '* You need to exec into containers for debugging or require OS-level packages at runtime.';   - You assume the source repository's Apache-2.0 licence covers every image layer and runtime dependency.;  |
| `distroless` | `verified_on` | '2026-08-03';  | '2026-10-23';  |
| `distroless` | `sources` | ;   - legacy:3_CI-CD-Automation/README.md#L78;   - legacy:devopstools_final.md#L351;  | ;   - https://github.com/GoogleContainerTools/distroless;   - https://github.com/GoogleContainerTools/distroless/blob/main/LICENSE;   - https://github.com/GoogleContainerTools/distroless/blob/main/SUPPORT_POLICY.md;   - legacy:3_CI-CD-Automation/README.md#L78;   - legacy:devopstools_final.md#L351;  |
| `docker-build` | `summary` | Umbrella Docker image-build feature implemented through the separately catalogued Docker Buildx client and BuildKit backend.;  | Documentation umbrella for Docker image building: Buildx is the CLI client and BuildKit its execution backend; not a separate source repository or licence grant.;  |
| `docker-build` | `verified_on` | '2026-09-13';  | '2026-10-23';  |
| `docker-build` | `sources` | ;   - https://docs.docker.com/build/;   - https://docs.docker.com/build/concepts/overview/;   - https://github.com/docker/buildx;   - https://github.com/moby/buildkit;   - legacy:3_CI-CD-Automation/README.md#L80;   - legacy:devopstools_final.md#L352;  | ;   - https://docs.docker.com/build/builders/;   - https://docs.docker.com/build/;   - https://docs.docker.com/build/concepts/overview/;   - https://github.com/docker/buildx;   - https://github.com/moby/buildkit;   - legacy:3_CI-CD-Automation/README.md#L80;   - legacy:devopstools_final.md#L352;  |
| `docker-buildx` | `summary` | Docker CLI plugin for extended build capabilities.;  | Docker CLI build client for BuildKit, supporting configurable builders, multi-platform images and external build caches.;  |
| `docker-buildx` | `status` | needs-review;  | active;  |
| `docker-buildx` | `verified_on` | '2026-08-03';  | '2026-10-23';  |
| `docker-buildx` | `sources` | ;   - legacy:3_CI-CD-Automation/README.md#L82;   - legacy:devopstools_final.md#L353;  | ;   - https://github.com/docker/buildx/blob/v0.38.1/LICENSE;   - https://github.com/docker/buildx/releases/tag/v0.38.1;   - https://docs.docker.com/build/concepts/overview/;   - https://docs.docker.com/build/builders/;   - legacy:3_CI-CD-Automation/README.md#L82;   - legacy:devopstools_final.md#L353;  |
| `docker-buildx` | `needs_review` | true | false |
| `docker-buildx` | `license_spdx` | (absent) | Apache-2.0;  |
| `earthly` | `summary` | Build automation framework.;  | Dockerfile-like build orchestration CLI; upstream ended active OSS maintenance in April 2025 and retired its Cloud/Satellite services in July 2025.;  |
| `earthly` | `avoid_when` | ;   - '* Your team already has a well-tuned build system and doesn''t need another abstraction layer.';  | ;   - '* Your team already has a well-tuned build system and doesn''t need another abstraction layer.';   - You require actively maintained OSS builds or the discontinued Earthly Cloud/Satellite services.;  |
| `earthly` | `verified_on` | '2026-08-03';  | '2026-10-23';  |
| `earthly` | `sources` | ;   - legacy:3_CI-CD-Automation/README.md#L86;   - legacy:devopstools_final.md#L355;  | ;   - https://earthly.dev/blog/shutting-down-earthfiles-cloud/;   - https://github.com/earthly/earthly/blob/v0.8.16/LICENSE;   - https://github.com/earthly/earthly/releases/tag/v0.8.16;   - legacy:3_CI-CD-Automation/README.md#L86;   - legacy:devopstools_final.md#L355;  |
| `earthly` | `license_spdx` | (absent) | MPL-2.0;  |
| `ko` | `summary` | Build Go apps into container images.;  | Build and publish Go application OCI images without writing Dockerfiles; publishes SBOMs by default in supported releases.;  |
| `ko` | `status` | needs-review;  | active;  |
| `ko` | `verified_on` | '2026-08-03';  | '2026-10-23';  |
| `ko` | `sources` | ;   - legacy:3_CI-CD-Automation/README.md#L92;   - legacy:devopstools_final.md#L358;  | ;   - https://github.com/ko-build/ko/blob/v0.19.1/LICENSE;   - https://github.com/ko-build/ko/releases/tag/v0.19.1;   - https://ko.build/features/sboms/;   - https://ko.build/;   - legacy:3_CI-CD-Automation/README.md#L92;   - legacy:devopstools_final.md#L358;  |
| `ko` | `needs_review` | true | false |
| `ko` | `license_spdx` | (absent) | Apache-2.0;  |
| `nix` | `summary` | Reproducible build and package manager.;  | Functional, reproducible package manager and build system; distinct from NixOS/nixpkgs and not a standalone OCI image builder.;  |
| `nix` | `verified_on` | '2026-08-03';  | '2026-10-23';  |
| `nix` | `sources` | ;   - legacy:3_CI-CD-Automation/README.md#L94;   - legacy:devopstools_final.md#L359;  | ;   - https://github.com/NixOS/nix;   - https://github.com/NixOS/nix/blob/master/COPYING;   - legacy:3_CI-CD-Automation/README.md#L94;   - legacy:devopstools_final.md#L359;  |
| `shipwright` | `summary` | Framework for building container images on Kubernetes.;  | Kubernetes-native image-build orchestration using Build and BuildRun resources and pluggable build strategies backed by Tekton.;  |
| `shipwright` | `verified_on` | '2026-08-03';  | '2026-10-23';  |
| `shipwright` | `sources` | ;   - legacy:3_CI-CD-Automation/README.md#L96;   - legacy:devopstools_final.md#L361;  | ;   - https://github.com/shipwright-io/build;   - https://github.com/shipwright-io/build/blob/v0.21.10/LICENSE;   - https://github.com/shipwright-io/build/releases/tag/v0.21.10;   - https://shipwright.io/docs/build/buildrun/;   - legacy:3_CI-CD-Automation/README.md#L96;   - legacy:devopstools_final.md#L361;  |
| `skopeo` | `summary` | Daemonless tool to inspect, copy, sign, and sync container images across registries and local;     stores.;  | Daemonless tool to inspect, copy and synchronize remote OCI/container images and registries without building or running images.;  |
| `skopeo` | `repository_url` | https://github.com/containers/skopeo;  | https://github.com/podman-container-tools/skopeo;  |
| `skopeo` | `status` | needs-review;  | active;  |
| `skopeo` | `verified_on` | '2026-08-03';  | '2026-10-23';  |
| `skopeo` | `sources` | ;   - legacy:devopstools_final.md#L363;  | ;   - https://github.com/containers/skopeo;   - https://github.com/podman-container-tools/skopeo/blob/main/README.md;   - https://github.com/podman-container-tools/skopeo/blob/v1.24.1/LICENSE;   - https://github.com/podman-container-tools/skopeo/releases/tag/v1.24.1;   - legacy:devopstools_final.md#L363;  |
| `skopeo` | `needs_review` | true | false |
| `skopeo` | `license_spdx` | (absent) | Apache-2.0;  |
| `werf` | `summary` | GitOps tool for building and deploying containers.;  | Git-driven Kubernetes delivery tool combining container-image builds, deployment and Helm-based release workflows.;  |
| `werf` | `status` | needs-review;  | active;  |
| `werf` | `verified_on` | '2026-08-03';  | '2026-10-23';  |
| `werf` | `sources` | ;   - legacy:3_CI-CD-Automation/README.md#L98;   - legacy:devopstools_final.md#L364;  | ;   - https://github.com/werf/werf/blob/v2.81.4/LICENSE;   - https://github.com/werf/werf/releases/tag/v2.81.4;   - https://werf.io/;   - legacy:3_CI-CD-Automation/README.md#L98;   - legacy:devopstools_final.md#L364;  |
| `werf` | `needs_review` | true | false |
| `werf` | `license_spdx` | (absent) | Apache-2.0;  |

### Validation pending

The canonical YAML modification was committed to the Draft branch **without locally executing** Python 3.12 tests or the official generator: the available GitHub connector edits source files but cannot run repository-side commands. CI is expected to fail generated-output consistency until official regeneration. **Do not merge, mark Ready for review, or treat any CLEAR as final yet.** Regenerate with `python -m scripts.generate_docs`, verify output list and stats; then run locked deps, full pytest, Ruff, catalogue validator and a final-HEAD strict link audit only after the checks are green. If a source is not actually sufficient, reverse only that record's clearance and update this matrix.
