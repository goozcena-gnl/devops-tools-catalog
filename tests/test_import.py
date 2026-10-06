from __future__ import annotations

import pytest

from scripts.import_archive import extract_details, parse_file


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
    assert entries[0].summary == "Declarative infrastructure."
    assert entries[0].badges == ("OSS",)
    assert entries[0].normalized_url == "https://example.com"
    assert entries[0].secondary_urls == ("https://github.com/example/tool",)
    assert entries[0].use_when == ("Automation is required.",)
    assert entries[0].avoid_when == ("Manual changes are mandatory.",)


@pytest.mark.parametrize(
    ("rest", "expected"),
    [
        pytest.param("visible <!-- hidden --> text", "Visible text.", id="single"),
        pytest.param(
            "visible <!--\nhidden\ncontent\n--> text", "Visible text.", id="multiline"
        ),
        pytest.param(
            "visible <!--\r\nhidden\r\n--> text", "Visible text.", id="multiline-crlf"
        ),
        pytest.param(
            "visible <!-- one --> middle <!-- two --> end",
            "Visible middle end.",
            id="multiple",
        ),
        pytest.param("before<!-- hidden -->after", "Before after.", id="adjacent"),
        pytest.param("before<!----><!---->after", "Before after.", id="empty-comments"),
        pytest.param("visible <!-- hidden content", "Visible.", id="unterminated"),
        pytest.param(
            "visible <!-- <script>alert(1)</script><img src=x><div>hidden</div> --> text",
            "Visible text.",
            id="html-inside-comment",
        ),
        pytest.param(
            "visible ordinary text", "Visible ordinary text.", id="no-comment"
        ),
        pytest.param(
            "<!-- hidden -->",
            "Legacy catalogue entry pending factual description review.",
            id="comment-only",
        ),
        pytest.param(
            "<!-- hidden",
            "Legacy catalogue entry pending factual description review.",
            id="unterminated-comment-only",
        ),
        pytest.param(
            "", "Legacy catalogue entry pending factual description review.", id="empty"
        ),
        pytest.param(
            "before<!-- one <!-- two -->after", "Before after.", id="first-closer"
        ),
        pytest.param("visible --> text", "Visible --> text.", id="unmatched-closer"),
        pytest.param(
            "visible <!-- hidden --!> text", "Visible.", id="nonstandard-closer"
        ),
        pytest.param(
            "before<!-- *Use when hidden; Avoid if hidden.* --> after",
            "Before after.",
            id="comment-before-guidance-filter",
        ),
        pytest.param(
            'before <sup><span title="<!--">OSS</span></sup> hidden payload --> after',
            'Before <sup><span title=" after.',
            id="comment-before-badge-filter",
        ),
    ],
)
def test_extract_details_comment_summaries(rest: str, expected: str) -> None:
    assert extract_details(rest)[0] == expected


@pytest.mark.parametrize(
    "rest",
    [
        "visible <script>alert(1)</script>",
        "visible <img src=x>",
        "visible <div>text</div>",
        "visible **Markdown** https://example.com",
        "visible &lt;!-- ordinary text --&gt; text",
    ],
    ids=["script", "img", "div", "markdown-and-url", "escaped-markers"],
)
def test_extract_details_preserves_non_comment_markup(rest: str) -> None:
    assert extract_details(rest) == (rest[0].upper() + rest[1:] + ".", (), (), ())


def test_parse_file_comment_continuations_preserve_details(tmp_path) -> None:
    source = tmp_path / "README.md"
    raw = (
        "- [Example](https://example.com/) <sup><span>OSS</span></sup> - before<!--\n"
        "hidden <script>alert(1)</script>\n"
        "-->after <!-- second --> summary.\n"
        "([GitHub](https://github.com/example/tool))\n"
        "*Use when automation is required; avoid if manual changes are mandatory.*"
    )
    source.write_text(
        "## Cloud\n### B. Infrastructure as Code (IaC)\n" + raw + "\n", encoding="utf-8"
    )
    entries = parse_file(source, tmp_path)
    assert len(entries) == 1
    entry = entries[0]
    assert entry.summary == "Before after summary."
    assert entry.badges == ("OSS",)
    assert entry.secondary_urls == ("https://github.com/example/tool",)
    assert entry.use_when == ("Automation is required.",)
    assert entry.avoid_when == ("Manual changes are mandatory.",)
    assert entry.source_file == "README.md"
    assert entry.line == 3
    assert entry.section == "Cloud"
    assert entry.subsection == "B. Infrastructure as Code (IaC)"
    assert entry.raw == raw


def test_parse_file_unclosed_comment_stops_at_entry_boundary(tmp_path) -> None:
    source = tmp_path / "README.md"
    source.write_text(
        "- [First](https://example.com/first) visible <!-- hidden\n"
        "still hidden\n"
        "- [Second](https://example.com/second) ordinary summary\n",
        encoding="utf-8",
    )
    entries = parse_file(source, tmp_path)
    assert [entry.summary for entry in entries] == ["Visible.", "Ordinary summary."]
