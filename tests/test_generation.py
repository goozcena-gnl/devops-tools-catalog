from __future__ import annotations

from scripts.catalog import ROOT
from scripts.generate_docs import expected_outputs, generate
from scripts.validate_catalog import validate_markdown_links


def test_generation_is_deterministic_and_current() -> None:
    first = expected_outputs()
    second = expected_outputs()
    assert first == second
    assert generate(check=True) == []


def test_markdown_internal_link_validation(tmp_path) -> None:
    (tmp_path / "README.md").write_text(
        "[Missing](docs/does-not-exist.md)\n", encoding="utf-8"
    )
    errors = validate_markdown_links(tmp_path)
    assert errors == ["README.md:1: broken link docs/does-not-exist.md"]


def test_repository_markdown_internal_links() -> None:
    assert validate_markdown_links(ROOT) == []
