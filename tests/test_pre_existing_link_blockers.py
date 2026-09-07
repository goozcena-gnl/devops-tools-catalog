from pathlib import Path

import yaml

from scripts.catalog import load_tools

ROOT = Path(__file__).resolve().parents[1]
CURRENT_FIRECRACKER_DOCS = (
    "https://github.com/firecracker-microvm/firecracker/"
    "blob/main/docs/getting-started.md"
)


def test_firecracker_uses_current_official_documentation() -> None:
    firecracker = next(tool for tool in load_tools() if tool["id"] == "firecracker")

    assert firecracker["documentation_url"] == CURRENT_FIRECRACKER_DOCS
    assert CURRENT_FIRECRACKER_DOCS in firecracker["sources"]
    assert firecracker["repository_url"] == (
        "https://github.com/firecracker-microvm/firecracker"
    )
    assert firecracker["status"] == "active"
    assert firecracker["license_spdx"] == "Apache-2.0"


def test_firecracker_import_override_preserves_documentation_url() -> None:
    overrides = yaml.safe_load(
        (ROOT / "config" / "import-overrides.yaml").read_text(encoding="utf-8")
    )

    assert (
        overrides["record_overrides"]["https://firecracker-microvm.github.io"][
            "documentation_url"
        ]
        == CURRENT_FIRECRACKER_DOCS
    )


def test_transient_kubegui_record_is_unchanged() -> None:
    kubegui = next(tool for tool in load_tools() if tool["id"] == "kubegui")

    assert kubegui["official_url"] == "https://kubegui.net"
    assert kubegui["status"] == "needs-review"
    assert kubegui["needs_review"] is True
