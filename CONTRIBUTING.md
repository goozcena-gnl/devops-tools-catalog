# Contributing

Thank you for improving the catalog. Canonical YAML under `data/tools/` is the
source of truth. Files beginning with the generated notice must not be edited
directly; change the generator or canonical data and regenerate them instead.

## Repository map

| Path | Purpose | Edit directly? |
|---|---|---|
| `data/tools/*.yaml` | Canonical tool records, grouped by primary category | Yes |
| `data/taxonomy.yaml` | Allowed categories, roles, lifecycle stages, and enums | With maintainer review |
| `schema/tool.schema.json` | Machine-readable record contract | With tests and maintainer review |
| `scripts/` and `tests/` | Generation, validation, import, auditing, and coverage | Yes |
| `config/import-overrides.yaml` | Reviewed aliases and migration exceptions | Yes, with evidence |
| `migration/` | Historical source inventory and reconciliation | Preserve; change only for a traceable correction |
| `README.md`, `docs/categories/`, `docs/roles/`, `docs/lifecycle/` | Generated navigation | **No** |
| `docs/decision-guides/`, `docs/maintenance/`, `docs/releases/` | Maintained engineering guidance and evidence records | Yes |

## Before proposing a tool

Confirm that the tool has a concrete operational use case for at least one catalogue role. A proposal must include:

- canonical tool name;
- official URL and, when available, repository URL;
- relevant roles and taxonomy categories;
- a practical use case and decision guidance;
- licence model and primary-source evidence;
- evidence of active maintenance;
- an explanation of why an existing record is not equivalent.

Search IDs, names, official URLs, repository URLs, and aliases before adding a
record. `python -m scripts.validate_catalog` rejects duplicate canonical IDs and
normalized official or repository URLs. If two names represent the same
operational product, update the existing record and preserve the alternate name
or URL in `config/import-overrides.yaml` rather than creating a duplicate.

Do not infer a licence from public source availability. Use `license_model: unknown` and `needs_review: true` when an official licence file or vendor statement is unavailable.

## Record conventions

- Use a stable lowercase kebab-case `id`; do not rename an ID only for style.
- Use taxonomy IDs from `data/taxonomy.yaml`.
- Keep summaries factual, neutral, and one sentence long.
- Put adoption conditions in `use_when` and constraints in `avoid_when`.
- Use official documentation, project sites, repositories, licence files, foundation pages, or vendor announcements as `sources`.
- Set `verified_on` to the date on which those sources were checked.
- Use `status: active` only when current primary-source evidence supports active maintenance.
- Use `needs_review: true` and the appropriate unresolved value when evidence is incomplete; do not clear review debt for presentation.
- Preserve renamed, archived, or historically important tools with an appropriate status instead of deleting context.
- Add URL/name aliases to `config/import-overrides.yaml`; do not hide exceptions in parser code.

## Local workflow

Use Python 3.11 or later. Create and activate a virtual environment, then install
the declared development dependencies:

```bash
python -m venv .venv
python -m pip install -e '.[dev]'
python -m scripts.generate_docs
python -m scripts.validate_catalog
python -m pytest
python -m ruff check scripts tests
python -m ruff format --check scripts tests
```

On POSIX shells activate with `source .venv/bin/activate`; on PowerShell use
`.\.venv\Scripts\Activate.ps1` before running the commands above.

Run `python -m scripts.generate_docs --check` after generation to confirm
deterministic output. Full network link audits are intentionally separate:

```bash
.venv/bin/python -m scripts.check_links --strict
```

## Working a scoped evidence-review issue

Review issues turn the catalogue's visible review debt into bounded work. Choose
one issue, keep to its listed record IDs, and use this sequence:

1. locate each canonical record under `data/tools/`;
2. check primary evidence without inferring missing facts;
3. update canonical metadata and `verified_on` only for claims actually checked;
4. leave `needs_review: true` when any required claim remains uncertain;
5. run `python -m scripts.generate_docs`, then the validation commands above;
6. open one focused pull request and link the issue.

Use evidence in this order:

1. official project documentation;
2. the canonical upstream GitHub or GitLab repository;
3. the official vendor or project website;
4. the official licence file for licence claims;
5. an official release, archive, deprecation, or ownership notice.

Blogs, generated summaries, catalogue aggregators, and search-result snippets
can help discovery but are not authoritative evidence. Never guess a licence,
lifecycle state, project owner, or canonical identity. If primary sources
conflict or remain incomplete, document the uncertainty and retain the review
flag.

Maintainers scope review batches using the
[review-batch playbook](docs/maintenance/review-batch-playbook.md). It defines
the expected issue contents and keeps the public queue small enough to remain
reviewable.

## Pull requests

Keep changes focused. Explain primary-source evidence, unresolved fields,
aliases or merges, generated-document changes, and the commands you ran. A
single record or one coherent evidence batch is easier to verify than an
unrelated bulk edit.

Never commit archive files, caches, generated audit output under `reports/`,
credentials, tokens, cookies, private URLs, Terraform state, kubeconfigs, or
environment files. If sensitive data may have entered Git history, stop and
follow [SECURITY.md](SECURITY.md); deleting only the current file is not enough.

## Repository licence

Repository-owned code, documentation, and original catalog metadata are
available under the [MIT License](LICENSE). Third-party projects and linked
content retain their own rights and licences; see
[docs/licensing.md](docs/licensing.md).
