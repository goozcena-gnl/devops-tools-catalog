from __future__ import annotations

import shutil
from pathlib import Path
from typing import Any

import yaml

from scripts.catalog import ROOT


def minimal_record(**changes: Any) -> dict[str, Any]:
    record: dict[str, Any] = {
        "id": "example-tool",
        "name": "Example Tool",
        "summary": "A representative operational tool.",
        "official_url": "https://example.com/tool",
        "categories": ["foundations-linux-scripting"],
        "subcategories": [],
        "roles": ["devops-engineer"],
        "lifecycle_stages": ["develop"],
        "use_when": [],
        "avoid_when": [],
        "deployment_models": [],
        "license_model": "unknown",
        "maturity": "unknown",
        "status": "needs-review",
        "alternatives": [],
        "tags": [],
        "verified_on": "2026-08-03",
        "sources": ["test-fixture"],
        "needs_review": True,
    }
    record.update(changes)
    return record


def write_catalog(root: Path, records: list[dict[str, Any]]) -> None:
    (root / "data" / "tools").mkdir(parents=True)
    (root / "schema").mkdir(parents=True)
    shutil.copy(ROOT / "data" / "taxonomy.yaml", root / "data" / "taxonomy.yaml")
    shutil.copy(
        ROOT / "schema" / "tool.schema.json", root / "schema" / "tool.schema.json"
    )
    (root / "data" / "tools" / "foundations-linux-scripting.yaml").write_text(
        yaml.safe_dump(records, sort_keys=False), encoding="utf-8"
    )
    (root / "migration").mkdir()
    (root / "migration" / "source-entries.json").write_text("[]\n", encoding="utf-8")
    (root / "migration" / "reconciliation.csv").write_text(
        "source_file,line,source_name,source_url,canonical_id,disposition,reason\n",
        encoding="utf-8",
    )
