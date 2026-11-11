# GitLab MCP server — documentation URL recovery (2026-11-11)

## Incident and verified evidence

PR #161 updated the pinned `actions/upload-artifact` action to v7.0.2 and passed eight normal CI checks on `2b3b69aeaf634dea8f801a343bc52d8efb49d3ce`. Its [strict Full link audit #43035296051](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/43035296051) nevertheless failed: `blocking_new: 1`, `blocking_known: 6`, `strict_result: FAIL` across 2,816 checked URLs. The new blocking URL is `https://docs.gitlab.com/user/gitlab_duo/model_context_protocol/mcp_server` (HEAD and GET HTTP 404). The audit report was uploaded successfully by `actions/upload-artifact@cf430e030ddbb5b0abf93d22962f4752f3646cd9` (v7.0.2): [artifact #13863700176](https://github.com/goozcena-gnl/devops-tools-catalog/actions/runs/43035296051/artifacts/13863700176), ZIP 75,150 bytes, SHA-256 `8f7eb99bb409cb70718fdacfa045ca69a54e037dcb784b148ed0297c42fa9891`. The failure is an upstream documentation link, not an upload regression.

## Official replacement and restrained scope

GitLab's [current MCP server documentation](https://docs.gitlab.com/user/model_context_protocol/mcp_server/) is already cited under `sources` and stored in `documentation_url` of the `gitlab-mcp-server` canonical record. The [upstream relocation stub](https://gitlab.com/gitlab-org/gitlab/-/blob/master/doc/user/gitlab_duo/model_context_protocol/mcp_server.md) points to the new documentation location. Replace only that record's `official_url` with `https://docs.gitlab.com/user/model_context_protocol/mcp_server/` and regenerate seven affected Markdown docs using the repository generator.

This does not change the tool's ID, verified date, `legacy:` references, edition, OAuth or permission caveats, `license_model: documentation`, `status: needs-review`, or `needs_review: true`. The old URL remains **unchanged** in historical `migration/reconciliation.csv` to preserve provenance. The strict baseline `config/link-audit-baseline.json` must not be modified, weakened or extended.

Expected path allowlist (nine files): canonical `data/tools/mlops-llmops-ai-infrastructure.yaml`; generated category `docs/categories/mlops-llmops-ai-infrastructure.md`; three generated lifecycle files `docs/lifecycle/{build,deploy,operate}.md`; three generated role files `docs/roles/{cloud-engineer,platform-engineer,mlops-ai-infrastructure-engineer}.md`; this maintenance report. In the eight existing files, exactly one legacy URL is replaced per file. Do not touch any other record, generated page or file.

Baseline `main`: `1c336cfa78b961d9ca367d2b788d0dedc8805603` with 1,425 canonical records and 30 categories.

## Acceptance gates and disposition

Before human promotion from Draft: `python -m scripts.generate_docs --check`, `python -m scripts.validate_catalog`, Ruff lint/format, Python 3.12 dependency checks, full pytest, and exact-SHA GitHub Actions quality/security. Require one independent final-HEAD strict Full link audit with `blocking_new: 0`, `blocking_known: 6`, `strict_result: PASS` and an uploaded JSON/Markdown artifact. The baseline and migration records must remain untouched. Do not claim these gates have passed merely because the files are committed.

**Draft-only review:** preserve PR #161 unchanged/open, with no merge or auto-merge. This repair requires independent evidence review and a human merge decision. Only after authorized repair merge and successful post-merge checks may PR #161 be synchronized to new `main` and independently revalidated. Issue #2 continues tracking the six historic known link blockers.
