# Contributing

Thank you for improving the catalogue. The YAML under `data/tools/` is the source of truth; generated Markdown must not be edited directly.

## Before proposing a tool

Confirm that the tool has a concrete operational use case for at least one catalogue role. A proposal must include:

- canonical tool name;
- official URL and, when available, repository URL;
- relevant roles and taxonomy categories;
- a practical use case and decision guidance;
- licence model and primary-source evidence;
- evidence of active maintenance;
- an explanation of why an existing record is not equivalent.

Do not infer a licence from public source availability. Use `license_model: unknown` and `needs_review: true` when an official licence file or vendor statement is unavailable.

## Record conventions

- Use a stable lowercase kebab-case `id`; do not rename an ID only for style.
- Use taxonomy IDs from `data/taxonomy.yaml`.
- Keep summaries factual, neutral, and one sentence long.
- Put adoption conditions in `use_when` and constraints in `avoid_when`.
- Use official documentation, project sites, repositories, licence files, foundation pages, or vendor announcements as `sources`.
- Set `verified_on` to the date on which those sources were checked.
- Preserve renamed, archived, or historically important tools with an appropriate status instead of deleting context.
- Add URL/name aliases to `config/import-overrides.yaml`; do not hide exceptions in parser code.

## Local workflow

Use Python 3.11 or later:

```bash
python -m venv .venv
.venv/bin/python -m pip install -e '.[dev]'
.venv/bin/python -m scripts.generate_docs
.venv/bin/python -m scripts.validate_catalog
.venv/bin/python -m pytest
.venv/bin/python -m ruff check scripts tests
```

Run `python -m scripts.generate_docs --check` a second time to confirm deterministic output. Full network link audits are intentionally separate:

```bash
.venv/bin/python -m scripts.check_links --strict
```

## Pull requests

Keep changes focused. Explain primary-source evidence, unresolved fields, aliases or merges, generated-document changes, and the commands you ran. Never include archive files, caches, audit output under `reports/`, credentials, tokens, cookies, or private URLs.

## Repository licence

This private repository currently has no owner-selected software or documentation licence. Do not add one as part of an unrelated contribution. The owner must make that policy decision explicitly.
