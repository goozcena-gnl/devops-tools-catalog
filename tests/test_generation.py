from __future__ import annotations

from scripts.catalog import ROOT, load_taxonomy, load_tools
from scripts.generate_docs import expected_outputs, generate, label_map, render_tool
from scripts.validate_catalog import (
    scan_secrets,
    validate_markdown_links,
    validate_sensitive_files,
)


def test_generation_is_deterministic_and_current() -> None:
    first = expected_outputs()
    second = expected_outputs()
    assert first == second
    assert generate(check=True) == []


def test_render_tool_uses_explicit_br_metadata_block() -> None:
    taxonomy = load_taxonomy()
    categories = label_map(taxonomy["categories"])
    roles = label_map(taxonomy["roles"])
    localstack = next(tool for tool in load_tools() if tool["id"] == "localstack")

    rendered = render_tool(localstack, categories, roles)
    lines = rendered.splitlines()

    assert lines[2] == (
        f"**Categories:** {', '.join(categories[item] for item in localstack['categories'])}<br>"
    )
    assert (
        lines[3]
        == f"**Roles:** {', '.join(roles[item] for item in localstack['roles'])}<br>"
    )
    assert (
        lines[4]
        == f"**Model:** {str(localstack['license_model']).replace('-', ' ').title()}<br>"
    )
    assert (
        lines[5]
        == f"**Status:** {str(localstack['status']).replace('-', ' ').title()}<br>"
    )
    assert lines[6] == "**Repository:** Archived"
    assert all(not line.endswith("  ") for line in lines[:7])
    assert "  \n" not in rendered


def test_markdown_internal_link_validation(tmp_path) -> None:
    (tmp_path / "README.md").write_text(
        "[Missing](docs/does-not-exist.md)\n", encoding="utf-8"
    )
    errors = validate_markdown_links(tmp_path)
    assert errors == ["README.md:1: broken link docs/does-not-exist.md"]


def test_repository_markdown_internal_links() -> None:
    assert validate_markdown_links(ROOT) == []


def test_generated_readme_explains_public_trust_model() -> None:
    readme = expected_outputs()[ROOT / "README.md"]
    assert "# DevOps Tools Catalog" in readme
    assert "Evidence-backed catalog" in readme
    assert "Records requiring review" in readme
    assert "not just a list of bookmarks" in readme
    assert "## Representative record" in readme
    assert "## Licence and attribution" in readme


def test_sensitive_file_detection(tmp_path) -> None:
    (tmp_path / ".env.production").write_text("SAFE_PLACEHOLDER=1\n", encoding="utf-8")
    assert validate_sensitive_files(tmp_path) == [
        ".env.production: sensitive file type must not be committed"
    ]


def test_high_confidence_secret_detection(tmp_path) -> None:
    (tmp_path / "config.txt").write_text(
        "endpoint=https://service.example\n"
        + "credential=https://user:"
        + "not-a-real-password@example.invalid\n",
        encoding="utf-8",
    )
    assert scan_secrets(tmp_path) == ["config.txt: possible credential in URL"]
