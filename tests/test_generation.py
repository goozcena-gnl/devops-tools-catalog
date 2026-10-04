from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

import pytest

from scripts.catalog import ROOT, load_taxonomy, load_tools
from scripts.generate_docs import expected_outputs, generate, label_map, render_tool
from scripts.validate_catalog import (
    SECRET_PATTERNS,
    main,
    safe_diagnostic,
    scan_secrets,
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
def test_validator_redacts_credential_aliases_in_metadata(
    tmp_path, capsys, alias
) -> None:
    secret = "fixture-alias-credential"
    write_catalog(tmp_path, [minimal_record(id=f"{alias}={secret}")])

    assert main(validator_args(tmp_path)) == 1

    captured = capsys.readouterr()
    assert secret not in captured.out + captured.err
    assert f"{alias}=[REDACTED]" in captured.out
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
