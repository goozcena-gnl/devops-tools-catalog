## Summary

Describe the operational problem and the focused catalog or maintenance change.

## Evidence

- Official URL:
- Repository URL:
- Licence source:
- Maintenance/status source:

## Catalogue impact

- [ ] Categories and roles use existing taxonomy IDs.
- [ ] The record is not redundant with an existing tool.
- [ ] Unknown fields are marked for review rather than inferred.
- [ ] Aliases or merges preserve all provenance.
- [ ] I edited canonical YAML or its generator, not generated Markdown directly.
- [ ] Generated documentation was regenerated when applicable.

## Verification

- [ ] `python -m ruff check scripts tests`
- [ ] `python -m ruff format --check scripts tests`
- [ ] `python -m pytest`
- [ ] `python -m scripts.generate_docs --check`
- [ ] `python -m scripts.validate_catalog`
- [ ] `git diff --check`

## Risk and review focus

Call out licence ambiguity, identity/URL decisions, deprecation evidence, workflow changes, or unresolved links.
