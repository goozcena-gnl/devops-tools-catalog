# Wave 41 post-merge follow-up — otel-gui OTLP protocol guidance

- Review date: **2026-11-15**.
- Parent integration: [Wave 41 PR #178](https://github.com/goozcena-gnl/devops-tools-catalog/pull/178), squash commit `424a718eb538eea1dba2387b3b883e20d426151d`.
- Reported issue: [Codex P2 inline finding](https://github.com/goozcena-gnl/devops-tools-catalog/pull/178#discussion_r4579259872) on `otel-gui.use_when`.
- Base `main`: `424a718eb538eea1dba2387b3b883e20d426151d`.
- Scope: one canonical YAML record, its one generated category-page sentence, and this dated evidence ledger. **No other canonical, generated, test or CI files are changed.**

## Primary-source findings and version boundary

| Check | Exact official evidence | Supported conclusion | Limitation |
| --- | --- | --- | --- |
| Latest tagged release as inspected on 2026-11-15 | [otel-gui v3.1.0](https://github.com/metafab/otel-gui/releases/tag/v3.1.0), published **2026-10-21**; [README at tag v3.1.0](https://github.com/metafab/otel-gui/blob/v3.1.0/README.md) | The tagged release documents OTLP/HTTP, port **4318**. The `src/lib/server/grpc.ts` file is absent at that tag. | Do not claim native gRPC ingestion for this tagged release. |
| New gRPC support on upstream default branch | [Official commit `459afc7`](https://github.com/metafab/otel-gui/commit/459afc7aa84ca4e61c9090a0121285e234a04381), **2026-11-09**; [current README](https://github.com/metafab/otel-gui/blob/459afc7aa84ca4e61c9090a0121285e234a04381/README.md); [gRPC server source](https://github.com/metafab/otel-gui/blob/459afc7aa84ca4e61c9090a0121285e234a04381/src/lib/server/grpc.ts); [gRPC unit tests](https://github.com/metafab/otel-gui/blob/459afc7aa84ca4e61c9090a0121285e234a04381/src/lib/server/grpc.test.ts) | The upstream code adds an OTLP/gRPC receiver on **4317**, using HTTP/2 with Protobuf ingestion. The code and README explicitly support it. | Upstream `main` capability is not proof that every previously released binary/container supports gRPC. Availability depends on the exact build and configuration. |

**Resolution:** Codex correctly identified a user-facing *version-ambiguity risk*, but its blanket claim that upstream has no native OTLP/gRPC receiver is not true for the 2026-11-09 upstream commit. Avoid conflating the latest tagged release (2026-10-21) with a newer development commit.

## Exact content correction

`data/tools/monitoring-metrics-logs-tracing.yaml`, stable canonical ID `otel-gui`, **only** the existing `use_when[0]` value changes:

- Previous: `Inspect local OTLP/HTTP or OTLP/gRPC traces, logs and metrics without a full telemetry backend.`
- Updated: `Inspect local OTLP/HTTP traces, logs and metrics without a full telemetry backend.`

`docs/categories/monitoring-metrics-logs-tracing.md` must be regenerated to reflect the identical one-sentence change. The repository generator renders `use_when` in category pages, while roles and lifecycle summaries use the unchanged `name`, `license_model`, `status` and `summary` fields.

## Preserved invariants and deferred work

- **99 canonical raw blocks** in this category; exactly **1** block is modified (the single `otel-gui.use_when` entry); **98 fully unchanged**. No tool IDs added/removed.
- `kwatcher` and `grove` remain **RETAIN**, each entire raw block unchanged. All unrelated Wave 41 records and other categories are protected.
- `otel-gui` retains `license_spdx: MIT` (source-scoped), `license_model: oss`, `status: needs-review`, `needs_review: true`, `maturity: unknown`, `verified_on` and all original `sources` / `legacy:` entries; 23 category records remain marked `needs_review: true`.
- Do not replace the canonical record with a different OTLP receiver, claim binary support for gRPC without release evidence, or promote any lifecycle/status values.
- Wave 39 PR #174, Wave 40 PR #176, and cross-wave verification PR #180 are not modified. No merge, auto-merge, Ready for Review, tag, release, or issue closure is authorized.

## Validation and publication gates

- Source/field guard: only the intended `otel-gui.use_when` phrase changes in YAML and the generated category page; 98 untouched canonical blocks protected. **Validated in the preparation preflight.**
- Generator proof is structural: [`scripts/generate_docs.py`](https://github.com/goozcena-gnl/devops-tools-catalog/blob/424a718eb538eea1dba2387b3b883e20d426151d/scripts/generate_docs.py) renders `use_when` in category pages; the one-line generated output is included for the repository's `--check` gate.
- **NOT RUN during preparation:** a local `python -m scripts.generate_docs` execution, locked dependency installation, Ruff, `pytest`, catalogue validation, `git diff --check`, and network strict link audit (the tooling for a local complete checkout is unavailable here).
- The new Draft PR must run and verify normal GitHub CI (including generator `--check`, catalogue validation, tests, format/lint and security). The strict full link audit is a **separate exact-HEAD manual gate**, not implied by CI green.
- **KEEP DRAFT / DO NOT MERGE:** respond to the Codex thread only with traceable resolution evidence; do not mark it resolved until a verified correction is integrated and policy allows closure.
