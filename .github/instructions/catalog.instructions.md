---
applyTo: "data/**,schema/**,config/import-overrides.yaml,scripts/**,tests/**"
---

# Catalog Data and Validation Instructions

- Treat `data/tools/*.yaml` as canonical catalog data and `data/taxonomy.yaml` as the allowed vocabulary.
- Do not clear `needs_review` unless the required claims are supported by current primary sources.
- Preserve aliases and migration history when identities or URLs change.
- Avoid bulk edits that mix unrelated records or evidence classes.
- Regenerate derived documentation after canonical data changes and verify deterministic output.
- A network response alone is not authoritative evidence of project lifecycle, licence, or ownership.
