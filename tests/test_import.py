from __future__ import annotations

from scripts.import_archive import parse_file


def test_imports_representative_legacy_entry(tmp_path) -> None:
    source = tmp_path / "README.md"
    source.write_text(
        "## Cloud\n"
        "### B. Infrastructure as Code (IaC)\n"
        "- [Example](https://example.com/) <sup><span>OSS</span></sup> - Declarative infrastructure. "
        "([GitHub](https://github.com/example/tool)) *Use when automation is required; avoid if manual changes are mandatory.*\n",
        encoding="utf-8",
    )
    entries = parse_file(source, tmp_path)
    assert len(entries) == 1
    assert entries[0].name == "Example"
    assert entries[0].normalized_url == "https://example.com"
    assert entries[0].secondary_urls == ("https://github.com/example/tool",)
    assert entries[0].use_when == ("Automation is required.",)
    assert entries[0].avoid_when == ("Manual changes are mandatory.",)
