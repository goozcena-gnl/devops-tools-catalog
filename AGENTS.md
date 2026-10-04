# Agent Instructions

## Repository purpose

This repository is an evidence-backed DevOps tooling knowledge base. Canonical YAML is the source of truth; generated Markdown is not.

## Sources of truth

- `data/tools/*.yaml` contains canonical records.
- `data/taxonomy.yaml` defines allowed taxonomy values.
- `schema/tool.schema.json` defines the machine-readable contract.
- `config/import-overrides.yaml` contains reviewed aliases and migration exceptions.
- `migration/` preserves historical reconciliation context.
- Files carrying the generated notice must not be edited directly.

## Evidence rules

For tool metadata, prefer primary sources in this order:

1. official documentation;
2. canonical upstream repository;
3. official project/vendor website;
4. official licence file;
5. official release, archive, deprecation, or ownership notice.

Do not infer licence, ownership, lifecycle, or canonical identity from search snippets, blogs, aggregators, or another AI's summary. If evidence is incomplete, keep `needs_review: true`.

## Mandatory validation

```bash
python -m pip install -e '.[dev]'
python -m ruff check scripts tests
python -m ruff format --check scripts tests
python -m pytest
python -m scripts.generate_docs --check
python -m scripts.validate_catalog
git diff --check
```

After canonical data changes, regenerate documentation before checking it:

```bash
python -m scripts.generate_docs
python -m scripts.generate_docs --check
```

Network link audits are separate and must not be treated as authoritative lifecycle evidence by themselves.

## Engineering rules

- Change canonical YAML, not generated pages.
- Keep evidence-review batches bounded and reviewable.
- Do not clear review debt merely to improve metrics.
- Do not bulk-replace URLs because they redirect.
- Preserve aliases/history instead of creating duplicates.
- Never commit credentials, cookies, private URLs, caches, archive files, Terraform state, kubeconfigs, or generated audit output under `reports/`.

## Pull request discipline

State:
- record IDs changed;
- primary sources checked;
- unresolved claims left open;
- generation/validation commands executed;
- network-dependent checks that were not run.

Do not merge or publish releases on behalf of the user.
