from __future__ import annotations

import json
import re
import subprocess
import sys
from html import unescape
from pathlib import Path
from urllib.parse import quote

import pytest
from jsonschema import Draft202012Validator

from scripts.catalog import ROOT, load_taxonomy, load_tools
from scripts.generate_docs import (
    expected_outputs,
    generate,
    label_map,
    render_deprecated,
    render_lifecycle,
    render_role,
    render_tool,
)
from scripts.validate_catalog import (
    SECRET_PATTERNS,
    main,
    safe_diagnostic,
    scan_secrets,
    schema_error_diagnostics,
    validate_markdown_links,
    validate_sensitive_files,
)
from tests.conftest import minimal_record, write_catalog


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


# Construct synthetic credentials at runtime so fixtures cannot trigger scanners.
SYNTHETIC_SECRETS = {
    "AWS access key": "AK" + "IA" + "Z" * 16,
    "Azure storage key": "Account" + "Key=" + "Z" * 44,
    "Google API key": "AI" + "za" + "Z" * 35,
    "GitHub token": "gh" + "p_" + "Z" * 36,
    "GitLab token": "gl" + "pat-" + "Z" * 20,
    "npm token": "np" + "m_" + "Z" * 36,
    "OpenAI API key": "sk" + "-proj-" + "Z" * 32,
    "private key": "-----BEGIN "
    + "PRIVATE KEY-----\nsynthetic-key-body\n"
    + "-----END "
    + "PRIVATE KEY-----",
    "Slack token": "xo" + "xb-" + "Z" * 20,
    "credential in URL": "https://fixture-user:" + "fixture-password@example.invalid",
}


def validator_args(root: Path, *extra: str) -> list[str]:
    # Minimal catalogues have no generated docs; keep real validation/scanning on.
    return ["--root", str(root), "--skip-generated", "--skip-links", *extra]


@pytest.mark.parametrize("label", SYNTHETIC_SECRETS)
@pytest.mark.parametrize("skip_secrets", [False, True])
def test_validator_schema_diagnostics_hide_secrets(
    tmp_path, capsys, label, skip_secrets
) -> None:
    secret = SYNTHETIC_SECRETS[label]
    write_catalog(tmp_path, [minimal_record(status=secret)])
    extra = ["--skip-secrets"] if skip_secrets else []

    assert main(validator_args(tmp_path, *extra)) == 1

    captured = capsys.readouterr()
    assert secret not in captured.out + captured.err
    assert "synthetic-key-body" not in captured.out + captured.err
    assert "example-tool.status: invalid value (enum)" in captured.out
    assert "Catalogue validation failed" in captured.out
    assert captured.err == ""


@pytest.mark.parametrize(
    "value",
    ["Bearer fixture-bearer-value", "password=fixture-password-value", "opaque-value"],
)
def test_validator_schema_diagnostics_omit_unrecognized_values(
    tmp_path, capsys, value
) -> None:
    write_catalog(
        tmp_path,
        [minimal_record(status=value, summary={"password": "nested-password-value"})],
    )

    assert main(validator_args(tmp_path)) == 1

    captured = capsys.readouterr()
    assert value not in captured.out + captured.err
    assert "nested-password-value" not in captured.out + captured.err
    assert "example-tool.summary: invalid value (type)" in captured.out
    assert "example-tool.status: invalid value (enum)" in captured.out


@pytest.mark.parametrize("field", ["official_url", "repository_url"])
@pytest.mark.parametrize("form", ["userinfo", "query", "encoded"])
def test_validator_duplicate_url_diagnostics_hide_credentials(
    tmp_path, capsys, field, form
) -> None:
    secret = "fixture-duplicate-credential"
    if form == "userinfo":
        url = "https://" + f"{secret}:{secret}@example.invalid/tool"
    elif form == "query":
        url = f"https://example.invalid/tool?api_key={secret}"
    else:
        secret = SYNTHETIC_SECRETS["GitHub token"]
        encoded = "".join(f"%{ord(char):02X}" for char in secret)
        url = f"https://example.invalid/tool?value={encoded}"
    write_catalog(
        tmp_path,
        [
            minimal_record(**{field: url}),
            minimal_record(id="second-tool", **{field: url}),
        ],
    )

    assert main(validator_args(tmp_path)) == 1

    captured = capsys.readouterr()
    assert secret not in captured.out + captured.err
    assert url not in captured.out + captured.err
    assert (
        f"duplicate {field} detected for records example-tool, second-tool"
        in captured.out
    )
    assert captured.err == ""


@pytest.mark.parametrize("label", SYNTHETIC_SECRETS)
def test_validator_scanner_retains_labels_without_payloads(
    tmp_path, capsys, label
) -> None:
    assert set(SYNTHETIC_SECRETS) == set(SECRET_PATTERNS)
    secret = SYNTHETIC_SECRETS[label]
    write_catalog(tmp_path, [minimal_record()])
    (tmp_path / "credential-fixture.txt").write_text(secret, encoding="utf-8")

    assert main(validator_args(tmp_path)) == 1

    captured = capsys.readouterr()
    assert secret not in captured.out + captured.err
    assert "synthetic-key-body" not in captured.out + captured.err
    assert f"credential-fixture.txt: possible {label}" in captured.out
    assert captured.err == ""


def test_validator_redacts_credential_metadata_and_link_targets(
    tmp_path, capsys
) -> None:
    secret = SYNTHETIC_SECRETS["GitHub token"]
    write_catalog(tmp_path, [minimal_record(id=secret, status="invalid-status")])
    (tmp_path / f"{secret}.txt").write_text(secret, encoding="utf-8")
    (tmp_path / "README.md").write_text(
        "[Missing](missing.md?password=link-password-value)\n", encoding="utf-8"
    )
    args = validator_args(tmp_path)
    args.remove("--skip-links")

    assert main(args) == 1

    captured = capsys.readouterr()
    assert secret not in captured.out + captured.err
    assert "link-password-value" not in captured.out + captured.err
    assert "[REDACTED].status: invalid value (enum)" in captured.out
    assert "[REDACTED].txt: possible GitHub token" in captured.out
    assert "README.md:1: broken link missing.md?password=[REDACTED]" in captured.out


def test_validator_retains_ordinary_diagnostics_and_success(tmp_path, capsys) -> None:
    write_catalog(tmp_path, [minimal_record(status="ordinary-invalid-status")])
    (tmp_path / ".env.production").write_text("SAFE_PLACEHOLDER=1\n", encoding="utf-8")

    assert main(validator_args(tmp_path)) == 1

    captured = capsys.readouterr()
    assert "example-tool.status: invalid value (enum)" in captured.out
    assert "example-tool: invalid value for field 'status'" in captured.out
    assert ".env.production: sensitive file type must not be committed" in captured.out
    assert captured.err == ""
    (tmp_path / ".env.production").unlink()
    record_path = tmp_path / "data/tools/foundations-linux-scripting.yaml"
    record_path.write_text(
        record_path.read_text(encoding="utf-8").replace(
            "ordinary-invalid-status", "active"
        ),
        encoding="utf-8",
    )

    assert main(validator_args(tmp_path)) == 0
    captured = capsys.readouterr()
    assert captured.out == "Catalogue validation passed.\n"
    assert captured.err == ""


@pytest.mark.parametrize(
    "label",
    [
        label
        for label in SYNTHETIC_SECRETS
        if label not in {"private key", "credential in URL"}
    ],
)
def test_validator_redacts_tokens_attached_to_metadata(tmp_path, capsys, label) -> None:
    secret = SYNTHETIC_SECRETS[label]
    write_catalog(tmp_path, [minimal_record(id=f"backup_{secret}")])
    (tmp_path / f"backup_{secret}.txt").write_text(secret, encoding="utf-8")

    assert main(validator_args(tmp_path)) == 1

    captured = capsys.readouterr()
    assert secret not in captured.out + captured.err
    assert "backup_[REDACTED]" in captured.out
    assert f"possible {label}" in captured.out
    assert "invalid value (pattern)" in captured.out
    assert captured.err == ""


@pytest.mark.parametrize("alias", ["db_password", "client_secret", "API_TOKEN"])
@pytest.mark.parametrize(
    "secret",
    ["fixture-alias-credential", "fixture password tail", '"fixture password tail'],
)
def test_validator_redacts_credential_aliases_in_metadata(
    tmp_path, capsys, alias, secret
) -> None:
    write_catalog(tmp_path, [minimal_record(id=f"{alias}={secret}")])

    assert main(validator_args(tmp_path)) == 1

    captured = capsys.readouterr()
    assert secret not in captured.out + captured.err
    assert "tail" not in captured.out + captured.err
    assert f"{alias}=[REDACTED]" in captured.out
    assert "invalid value (pattern)" in captured.out
    assert captured.err == ""


@pytest.mark.parametrize(
    "credential",
    [
        "Bearer fixture-authorization-payload",
        'Bearer "fixture-authorization-payload"',
        'Bearer "fixture-authorization-payload',
        "Basic fixture-authorization-payload",
        "eyJ" + "header.eyJpayload.signature",
    ],
)
def test_validator_redacts_authorization_attached_to_metadata(
    tmp_path, capsys, credential
) -> None:
    write_catalog(tmp_path, [minimal_record(id=f"backup_{credential}")])

    assert main(validator_args(tmp_path)) == 1

    captured = capsys.readouterr()
    assert credential not in captured.out + captured.err
    assert "payload" not in captured.out + captured.err
    assert "[REDACTED]" in captured.out
    assert "invalid value (pattern)" in captured.out
    assert captured.err == ""


@pytest.mark.parametrize("username", ["fixture-user", "fixture-user%2Fname"])
def test_validator_redacts_scheme_relative_url_credentials(
    tmp_path, capsys, username
) -> None:
    secret = "fixture-relative-credential"
    write_catalog(tmp_path, [minimal_record()])
    (tmp_path / "README.md").write_text(
        f"[Missing](//{username}:{secret}@example.invalid/a.md)\n", encoding="utf-8"
    )
    args = validator_args(tmp_path)
    args.remove("--skip-links")

    assert main(args) == 1

    captured = capsys.readouterr()
    assert secret not in captured.out + captured.err
    assert "README.md:1: broken link //[REDACTED]@example.invalid/a.md" in captured.out
    assert captured.err == ""


def test_validator_retains_labels_after_incomplete_key_metadata(
    tmp_path, capsys
) -> None:
    header = SYNTHETIC_SECRETS["private key"].splitlines()[0]
    write_catalog(tmp_path, [minimal_record(id=header, status="invalid-status")])
    (tmp_path / f"{header}.pem").write_text(header, encoding="utf-8")

    assert main(validator_args(tmp_path)) == 1

    captured = capsys.readouterr()
    assert header not in captured.out + captured.err
    assert "[REDACTED].status: invalid value (enum)" in captured.out
    assert "[REDACTED]: possible private key" in captured.out
    assert "[REDACTED]: sensitive file type must not be committed" in captured.out
    assert captured.err == ""


@pytest.mark.parametrize(
    ("relative_path", "content", "error_class"),
    [
        (
            "data/tools/foundations-linux-scripting.yaml",
            "- *{secret}\n",
            "ComposerError",
        ),
        (
            "data/tools/foundations-linux-scripting.yaml",
            "- unexpected: {secret}\n",
            "KeyError",
        ),
        ("schema/tool.schema.json", '{{"{secret}":', "JSONDecodeError"),
        ("schema/tool.schema.json", '{{"type": "{secret}"}}', "UnknownType"),
    ],
)
def test_validator_module_parser_errors_do_not_leak(
    tmp_path, relative_path, content, error_class
) -> None:
    secret = SYNTHETIC_SECRETS["GitHub token"]
    write_catalog(tmp_path, [minimal_record()])
    (tmp_path / relative_path).write_text(
        content.format(secret=secret), encoding="utf-8"
    )

    result = subprocess.run(
        [sys.executable, "-m", "scripts.validate_catalog", *validator_args(tmp_path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 1
    assert secret not in result.stdout + result.stderr
    assert "Traceback" not in result.stdout + result.stderr
    assert result.stdout == ""
    assert f"Catalogue validation could not complete ({error_class})" in result.stderr


@pytest.mark.parametrize("argument", ["--unknown={secret}", "--password={secret}"])
def test_validator_argument_errors_are_secret_safe(capsys, argument) -> None:
    secret = SYNTHETIC_SECRETS["GitHub token"]
    with pytest.raises(SystemExit, match="2"):
        main([argument.format(secret=secret)])
    captured = capsys.readouterr()
    assert secret not in captured.out + captured.err
    assert "unrecognized arguments" in captured.err
    assert "[REDACTED]" in captured.err
    assert captured.out == ""


@pytest.mark.parametrize("label", ["GitHub token", "private key"])
def test_validator_help_redacts_program_name(monkeypatch, capsys, label) -> None:
    secret = SYNTHETIC_SECRETS[label].splitlines()[0]
    monkeypatch.setattr(sys, "argv", [f"{secret}.py"])
    with pytest.raises(SystemExit, match="0"):
        main(["--help"])
    captured = capsys.readouterr()
    assert secret not in captured.out + captured.err
    assert "[REDACTED]" in captured.out
    assert "--skip-generated" in captured.out
    assert captured.err == ""


@pytest.mark.parametrize(
    "credential",
    [
        "Bearer bearer-payload",
        "Basic basic-payload",
        "api_key=query-payload",
        'password="quoted password payload"',
        "https://username-payload@example.invalid",
        "ftp://user-payload:password-payload@example.invalid",
        "https://" + "user%2Fname:password-payload@example.invalid",
        "eyJ" + "header.eyJpayload.signature",
        SYNTHETIC_SECRETS["private key"],
    ],
)
def test_safe_diagnostic_handles_encoded_credentials_and_is_idempotent(
    credential,
) -> None:
    for message in (
        credential,
        quote(credential, safe=""),
        quote(quote(credential, safe=""), safe=""),
    ):
        safe = safe_diagnostic(f"fixture.txt: {message}")
        assert credential not in safe
        assert message not in safe
        assert "payload" not in safe
        assert "synthetic-key-body" not in safe
        assert "[REDACTED]" in safe
        assert safe.startswith("fixture.txt: ")
        assert safe_diagnostic(safe) == safe


def test_safe_diagnostic_handles_mixed_encoded_url_and_token() -> None:
    secret = SYNTHETIC_SECRETS["GitHub token"]
    message = secret + " https://" + "user%2Fname:password-payload@example.invalid"
    safe = safe_diagnostic(message)
    assert secret not in safe
    assert "password-payload" not in safe
    assert safe == "[REDACTED] https://[REDACTED]@example.invalid"


def test_safe_diagnostic_preserves_ordinary_encoded_paths() -> None:
    message = "README.md:1: broken link docs/a%20file.md"
    assert safe_diagnostic(message) == message


def test_safe_diagnostic_preserves_ordinary_dotted_names() -> None:
    message = "README.md:1: broken link docs/a%20file.library.py"
    assert safe_diagnostic(message) == message


def test_safe_diagnostic_handles_repeated_jwt_prefixes() -> None:
    message = "eyJ" * 10_000
    assert safe_diagnostic(message) == message


def test_safe_diagnostic_preserves_filename_around_jwt() -> None:
    credential = "eyJ" + "header.eyJpayload.signature"
    message = f"docs/backup_{credential}.txt: invalid value"
    assert safe_diagnostic(message) == "docs/backup_[REDACTED].txt: invalid value"


def test_validator_schema_missing_required_field_has_context(tmp_path, capsys) -> None:
    record = minimal_record(summary="opaque-object-value")
    del record["name"]
    write_catalog(tmp_path, [record])

    assert main(validator_args(tmp_path)) == 1

    captured = capsys.readouterr()
    assert "example-tool['name']: missing required field" in captured.out
    assert "opaque-object-value" not in captured.out + captured.err
    assert str(record) not in captured.out + captured.err
    assert captured.err == ""


def test_validator_schema_multiple_required_fields_are_distinct(
    tmp_path, capsys
) -> None:
    record = minimal_record()
    del record["name"]
    del record["summary"]
    write_catalog(tmp_path, [record])

    assert main(validator_args(tmp_path)) == 1

    captured = capsys.readouterr()
    for field in ("name", "summary"):
        assert (
            captured.out.count(f"example-tool['{field}']: missing required field") == 1
        )
    assert "example-tool: invalid value (required)" not in captured.out
    assert str(record) not in captured.out + captured.err
    assert captured.err == ""


@pytest.mark.parametrize(
    "field", ["password", "extra", "quoted'field", "first, second"]
)
def test_validator_schema_unexpected_property_has_context(
    tmp_path, capsys, field
) -> None:
    value = "opaque-unexpected-value"
    write_catalog(tmp_path, [minimal_record(**{field: value})])

    assert main(validator_args(tmp_path, "--skip-secrets")) == 1

    captured = capsys.readouterr()
    assert f"example-tool[{field!r}]: unexpected property" in captured.out
    assert value not in captured.out + captured.err
    assert captured.err == ""


@pytest.mark.parametrize("label", SYNTHETIC_SECRETS)
@pytest.mark.parametrize("placement", ["name", "value", "both"])
def test_validator_schema_unexpected_property_hides_secrets(
    tmp_path, capsys, label, placement
) -> None:
    secret = SYNTHETIC_SECRETS[label]
    field = secret if placement in {"name", "both"} else "password"
    value = secret if placement in {"value", "both"} else "opaque-property-value"
    write_catalog(tmp_path, [minimal_record(**{field: value})])

    assert main(validator_args(tmp_path, "--skip-secrets")) == 1

    captured = capsys.readouterr()
    assert secret not in captured.out + captured.err
    assert "synthetic-key-body" not in captured.out + captured.err
    assert value not in captured.out + captured.err
    context = "[REDACTED]" if placement in {"name", "both"} else "password"
    if label == "credential in URL" and placement in {"name", "both"}:
        context = "https://[REDACTED]@example.invalid"
    assert f"example-tool[{context!r}]: unexpected property" in captured.out
    assert captured.err == ""


def test_schema_object_errors_keep_nested_context_and_pattern_properties() -> None:
    schema = {
        "properties": {
            "metadata": {
                "type": "object",
                "properties": {"name": {"type": "string"}},
                "patternProperties": {"^allowed_": {"type": "string"}},
                "required": ["name", "summary"],
                "additionalProperties": False,
            }
        }
    }
    instance = {
        "metadata": {
            "allowed_label": "opaque-allowed-value",
            "first": "opaque-first-value",
            "second": "opaque-second-value",
        }
    }

    messages = list(
        dict.fromkeys(
            message
            for issue in Draft202012Validator(schema).iter_errors(instance)
            for message in schema_error_diagnostics("example-tool", issue)
        )
    )

    assert messages == [
        "example-tool.metadata['name']: missing required field",
        "example-tool.metadata['summary']: missing required field",
        "example-tool.metadata['first']: unexpected property",
        "example-tool.metadata['second']: unexpected property",
    ]
    assert "opaque-" not in "\n".join(messages)
    assert "allowed_label" not in "\n".join(messages)


@pytest.mark.parametrize("quote_marker", ['"', "'"])
def test_validator_argument_errors_redact_unterminated_quotes(
    capsys, quote_marker
) -> None:
    secret = "unterminated-" + "synthetic-value"

    with pytest.raises(SystemExit, match="2"):
        main(["--password=" + quote_marker + secret])

    captured = capsys.readouterr()
    assert secret not in captured.out + captured.err
    assert "password=[REDACTED]" in captured.err
    assert "unrecognized arguments" in captured.err
    assert captured.out == ""


def test_independent_review_visibility_issue204() -> None:
    taxonomy = load_taxonomy()
    categories = label_map(taxonomy["categories"])
    roles = label_map(taxonomy["roles"])
    records = {tool["id"]: tool for tool in load_tools()}
    openlens = records["openlens"]
    autogen = records["autogen"]
    grove = records["grove"]
    role = {"id": "platform-engineer", "name": "Platform Engineer"}

    category = render_tool(openlens, categories, roles)
    assert "**Status:** Historical" in category
    assert "**Review:** Required" in category
    assert "Oss (recorded; not a licence attestation)" in category
    assert "distributed-binary licensing still unverified" in category
    table = render_role(role, [openlens, autogen], categories)
    assert "oss (recorded; not a licence attestation)" in table
    assert "historical (review required)" in table
    assert "distributed-binary licensing still unverified" in table
    assert (
        "| oss (recorded; SPDX scope not established by this label) | "
        f"archived (review required) — {autogen['summary']} |"
    ) in table
    assert autogen["license_spdx"] == "MIT"
    assert autogen["status"] == "archived"
    assert "(review required)" in render_lifecycle("deploy", [openlens])
    assert "(historical) (review required)" in render_deprecated([openlens])
    assert "**Review:** Required" in render_tool(autogen, categories, roles)
    assert "not a licence attestation" not in render_tool(autogen, categories, roles)
    assert "Oss (recorded; SPDX scope not established by this label)" in render_tool(
        autogen, categories, roles
    )
    reviewed = {**openlens, "needs_review": False}
    assert "**Review:** Required" not in render_tool(reviewed, categories, roles)
    assert "review required" not in render_role(role, [reviewed], categories)
    assert "**Status:** Needs Review" in render_tool(grove, categories, roles)
    assert "**Review:** Required" not in render_tool(grove, categories, roles)
    assert openlens["license_model"] == "oss"
    assert "license_spdx" not in openlens
    assert openlens["status"] == "historical"
    assert openlens["needs_review"] is True


@pytest.fixture
def role_row():
    schema = json.loads((ROOT / "schema/tool.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    role = {"id": "devops-engineer", "name": "DevOps Engineer"}
    categories = {"foundations-linux-scripting": "Foundations"}
    separator = "|---|---|---|"

    def render(record):
        validator.validate(record)
        _, _, table = render_role(role, [record], categories).partition(
            separator + "\n"
        )
        rows = table.split("\n\n", 1)[0].splitlines()
        assert len(rows) == 1
        left, *cells, right = rows[0].split("|")
        assert left == right == ""
        assert len(cells) == 4
        link, category, model, status = (cell.strip() for cell in cells)
        assert link == "[Example Tool](https://example.com/tool)"
        assert category == "Foundations"
        return model, status

    return render


@pytest.mark.parametrize(
    "summary",
    [
        "first\rsecond",
        "first\nsecond",
        "first\r\nsecond",
        "first\r\n\n\rsecond",
        "  first\t  second   ",
        "first | second",
        r"first \| second",
        r"first \\\| second",
        "`code` **bold** *italic* _em_ ~~strike~~ [link](target) ![image](target)",
        "R&D &lt; &#124; &amp;",
        "<em>literal</em> <!-- comment -->",
        "Équipe déploiement — 雀",
        "www.example.com WWW.example.com https://example.com a@example.com",
        "Café\t  " + r"\||\\| &lt; <em>x</em> **littéral**" + "\r\n\r\n fin",
    ],
    ids=[
        "cr",
        "lf",
        "crlf",
        "consecutive",
        "tabs-and-spaces",
        "pipe",
        "one-backslash",
        "multiple-backslashes",
        "markdown",
        "entities",
        "html",
        "unicode",
        "autolinks",
        "combined",
    ],
)
def test_role_summary_is_plain_text_in_one_cell(role_row, summary) -> None:
    _, status = role_row(minimal_record(status="historical", summary=summary))
    prefix = "historical (review required) — "
    assert status.startswith(prefix)
    context = status.removeprefix(prefix)
    markup = re.sub(r"&#[0-9]+;", "", context)
    assert not set("&\\|<>[]`*_~:@").intersection(markup)
    assert "www." not in markup.lower()
    assert unescape(context) == " ".join(summary.split())


@pytest.mark.parametrize(
    ("status", "review", "spdx", "summary", "qualification", "expected_status"),
    [
        (
            "historical",
            True,
            None,
            "Historical package.",
            " (recorded; not a licence attestation)",
            "historical (review required) — Historical package.",
        ),
        (
            "historical",
            True,
            "Apache-2.0",
            "Apache-2.0 applies to source only. Distributed-binary licensing remains unverified.",
            " (recorded; SPDX scope not established by this label)",
            "historical (review required) — Apache-2.0 applies to source only. "
            "Distributed-binary licensing remains unverified.",
        ),
        (
            "archived",
            True,
            "MIT",
            "Project archived after development moved upstream.",
            " (recorded; SPDX scope not established by this label)",
            "archived (review required) — Project archived after development moved upstream.",
        ),
        ("historical", False, None, "Historical package.", "", "historical"),
        ("needs-review", True, None, "Needs review.", "", "needs-review"),
        (
            "active",
            True,
            None,
            "Active service.",
            " (recorded; not a licence attestation)",
            "active (review required) — Active service.",
        ),
        ("historical", None, None, "Review flag omitted.", "", "historical"),
    ],
    ids=[
        "historical-no-spdx",
        "source-only-spdx",
        "archived-mit",
        "review-not-required",
        "needs-review-status",
        "active-review",
        "missing-review-field",
    ],
)
def test_role_review_context_and_licence_scope(
    role_row, status, review, spdx, summary, qualification, expected_status
) -> None:
    record = minimal_record(status=status, summary=summary, license_model="oss")
    if review is None:
        del record["needs_review"]
    else:
        record["needs_review"] = review
    if spdx is not None:
        record["license_spdx"] = spdx

    model, rendered_status = role_row(record)

    assert unescape(rendered_status) == expected_status
    assert model == f"oss{qualification}"
    assert record["license_model"] == "oss"
    assert record.get("license_spdx") == spdx
    assert record["status"] == status
