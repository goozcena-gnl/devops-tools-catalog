"""Shared loading and deterministic serialization for catalogue scripts."""

from __future__ import annotations

import json
from collections.abc import Iterable
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
TOOLS_DIR = DATA_DIR / "tools"


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def dump_yaml(value: Any) -> str:
    return yaml.safe_dump(
        value,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=100,
    )


def load_taxonomy(root: Path = ROOT) -> dict[str, Any]:
    return load_yaml(root / "data" / "taxonomy.yaml")


def iter_tool_files(root: Path = ROOT) -> Iterable[Path]:
    yield from sorted((root / "data" / "tools").glob("*.yaml"))


def load_tools(root: Path = ROOT) -> list[dict[str, Any]]:
    tools: list[dict[str, Any]] = []
    for path in iter_tool_files(root):
        payload = load_yaml(path)
        if payload is None:
            continue
        if not isinstance(payload, list):
            raise TypeError(f"{path} must contain a YAML list")
        tools.extend(payload)
    return sorted(tools, key=lambda item: item["id"])


def write_if_changed(path: Path, content: str) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.read_text(encoding="utf-8") == content:
        return False
    path.write_text(content, encoding="utf-8")
    return True


def stable_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
