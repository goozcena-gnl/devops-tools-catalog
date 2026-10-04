#!/usr/bin/env python3
"""Validate catalogue schema, taxonomy, provenance, docs, and repository hygiene."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from collections.abc import Iterable, Sequence
from pathlib import Path
from typing import TextIO
from urllib.parse import unquote

from jsonschema import Draft202012Validator, FormatChecker

from scripts.catalog import ROOT, iter_tool_files, load_taxonomy, load_tools
from scripts.generate_docs import generate
from scripts.import_archive import normalize_url

MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^]]*]\((?P<target>[^)]+)\)")
SECRET_PATTERNS = {
    "AWS access key": re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
    "Azure storage key": re.compile(
        r"(?i)\b(?:AccountKey|SharedAccessKey)=[A-Za-z0-9+/]{40,}={0,2}"
    ),
    "Google API key": re.compile(r"\bAIza[A-Za-z0-9_-]{35}\b"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{36,}\b"),
    "GitLab token": re.compile(r"\bglpat-[A-Za-z0-9_-]{20,}\b"),
    "npm token": re.compile(r"\bnpm_[A-Za-z0-9]{36}\b"),
    "OpenAI API key": re.compile(r"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{32,}\b"),
    "private key": re.compile(
        r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY(?: BLOCK)?-----"
    ),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    "credential in URL": re.compile(r"https?://[^\s/:]+:[^\s/@]+@"),
}

SENSITIVE_FILE_PATTERNS = (
    re.compile(r"(?i)(?:^|/)\.env(?:\.|$)"),
    re.compile(r"(?i)(?:^|/)(?:id_rsa|id_dsa|id_ecdsa|id_ed25519)(?:\.pub)?$"),
    re.compile(r"(?i)(?:^|/)kubeconfig(?:\.|$)"),
    re.compile(r"(?i)\.(?:key|pem|p12|pfx|jks|keystore|tfstate|tfplan)$"),
    re.compile(r"(?i)(?:^|/)terraform\.tfstate(?:\.|$)"),
)

PRIVATE_KEY_BLOCK_RE = re.compile(
    r"-----BEGIN (?P<kind>(?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY(?: BLOCK)?)-----"
    r".*?(?:-----END (?P=kind)-----|$)",
    re.S,
)
URL_USERINFO_RE = re.compile(r"(//)[^/?#\s]*@")
AUTHORIZATION_RE = re.compile(r"(?i)\b(Bearer\s+|Basic\s+)[A-Za-z0-9._~+/=-]+")
JWT_RE = re.compile(r"\beyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\b")
CREDENTIAL_ASSIGNMENT_RE = re.compile(
    r"(?i)(?<![a-z0-9])(password|passwd|pwd|api[_-]?key|api[_-]?token|"
    r"access[_-]?token|auth[_-]?token|token|secret|authorization)"
    r"([\"']?\s*[:=]\s*)"
    r"(?:\"[^\"]*\"|'[^']*'|\[REDACTED\]|[^\s,;&\"'\]\})]+)"
)
# Detection keeps its confidence boundaries; output must also protect tokens
# attached to other filename/ID characters, such as an underscore prefix.
DIAGNOSTIC_SECRET_PATTERNS = tuple(
    re.compile(pattern.pattern.replace(r"\b", ""), pattern.flags)
    for pattern in SECRET_PATTERNS.values()
)


def safe_diagnostic(message: str) -> str:
    """Protect each diagnostic, including encoded credentials in metadata."""
    patterns = (
        PRIVATE_KEY_BLOCK_RE,
        URL_USERINFO_RE,
        AUTHORIZATION_RE,
        JWT_RE,
        CREDENTIAL_ASSIGNMENT_RE,
        *DIAGNOSTIC_SECRET_PATTERNS,
    )
    decoded = message
    sensitive = False
    while True:
        sensitive |= any(pattern.search(decoded) for pattern in patterns)
        # Strip userinfo before decoding can turn an encoded '/' into a delimiter.
        decoded = URL_USERINFO_RE.sub(r"\1[REDACTED]@", decoded)
        candidate = unquote(decoded)
        if candidate == decoded:
            break
        decoded = candidate
    # Keep ordinary encoded paths unchanged; decode only to remove credentials.
    if sensitive:
        message = decoded
    message = PRIVATE_KEY_BLOCK_RE.sub("[REDACTED]", message)
    message = URL_USERINFO_RE.sub(r"\1[REDACTED]@", message)
    message = AUTHORIZATION_RE.sub(r"\1[REDACTED]", message)
    message = CREDENTIAL_ASSIGNMENT_RE.sub(r"\1\2[REDACTED]", message)
    message = JWT_RE.sub("[REDACTED]", message)
    for pattern in DIAGNOSTIC_SECRET_PATTERNS:
        message = pattern.sub("[REDACTED]", message)
    return message


def safe_diagnostics(messages: Iterable[str]) -> list[str]:
    return [safe_diagnostic(message) for message in messages]


class DiagnosticArgumentParser(argparse.ArgumentParser):
    def _print_message(self, message: str | None, file: TextIO | None = None) -> None:
        if message:
            super()._print_message(safe_diagnostic(message), file)


def duplicate_field_errors(tools: list[dict[str, object]], field: str) -> list[str]:
    groups: dict[str, list[str]] = defaultdict(list)
    for tool in tools:
        if value := tool.get(field):
            groups[normalize_url(str(value))].append(safe_diagnostic(str(tool["id"])))
    return safe_diagnostics(
        f"duplicate {field} detected for records {', '.join(ids)}"
        for _, ids in sorted(groups.items())
        if len(ids) > 1
    )


def validate_records(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    taxonomy = load_taxonomy(root)
    tools = load_tools(root)
    schema = json.loads(
        (root / "schema" / "tool.schema.json").read_text(encoding="utf-8")
    )
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    category_ids = {item["id"] for item in taxonomy["categories"]}
    role_ids = {item["id"] for item in taxonomy["roles"]}
    stages = set(taxonomy["lifecycle_stages"])
    statuses = set(taxonomy["statuses"])
    ids = Counter(str(tool.get("id")) for tool in tools)

    for tool_id, count in sorted(ids.items()):
        if count > 1:
            errors.append(f"duplicate id {safe_diagnostic(tool_id)}: {count} records")
    errors.extend(duplicate_field_errors(tools, "official_url"))
    errors.extend(duplicate_field_errors(tools, "repository_url"))

    for tool in tools:
        tool_id = safe_diagnostic(str(tool.get("id", "<missing>")))
        for issue in validator.iter_errors(tool):
            location = ".".join(str(item) for item in issue.absolute_path)
            errors.append(
                f"{tool_id}{'.' + location if location else ''}: "
                f"invalid value ({issue.validator})"
            )
        invalid_categories = set(tool.get("categories", [])) - category_ids
        invalid_roles = set(tool.get("roles", [])) - role_ids
        invalid_stages = set(tool.get("lifecycle_stages", [])) - stages
        if invalid_categories:
            errors.append(f"{tool_id}: invalid categories")
        if invalid_roles:
            errors.append(f"{tool_id}: invalid roles")
        if invalid_stages:
            errors.append(f"{tool_id}: invalid lifecycle stages")
        if tool.get("status") not in statuses:
            errors.append(f"{tool_id}: invalid value for field 'status'")

    for path in iter_tool_files(root):
        payload = __import__("yaml").safe_load(path.read_text(encoding="utf-8")) or []
        file_ids = [item["id"] for item in payload]
        if file_ids != sorted(file_ids):
            errors.append(
                f"{safe_diagnostic(str(path.relative_to(root)))} is not sorted by id"
            )
        for item in payload:
            if item["categories"][0] != path.stem:
                errors.append(
                    f"{safe_diagnostic(str(item['id']))}: primary category does not match "
                    f"{safe_diagnostic(path.name)}"
                )
    return safe_diagnostics(errors)


def validate_reconciliation(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    source_entries = json.loads(
        (root / "migration" / "source-entries.json").read_text(encoding="utf-8")
    )
    with (root / "migration" / "reconciliation.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != len(source_entries):
        errors.append(
            f"reconciliation has {len(rows)} rows for {len(source_entries)} source entries"
        )
    allowed = {
        "kept",
        "merged",
        "renamed",
        "moved",
        "deprecated",
        "archived",
        "rejected",
        "needs-review",
    }
    for index, row in enumerate(rows, start=2):
        if row["disposition"] not in allowed:
            errors.append(f"migration/reconciliation.csv:{index}: invalid disposition")
        if row["disposition"] in {"rejected", "archived"} and not row["reason"]:
            errors.append(
                f"migration/reconciliation.csv:{index}: missing disposition reason"
            )
    return safe_diagnostics(errors)


def validate_markdown_links(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    ignored_parts = {".git", ".venv", ".pytest_cache", ".ruff_cache"}
    for path in sorted(root.rglob("*.md")):
        if ignored_parts.intersection(path.parts):
            continue
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in MARKDOWN_LINK_RE.finditer(line):
                raw_target = match.group("target").strip().strip("<>")
                target = raw_target.split(maxsplit=1)[0]
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                file_target = unquote(target.split("#", maxsplit=1)[0])
                if not file_target:
                    continue
                resolved = (path.parent / file_target).resolve()
                if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                    errors.append(
                        f"{safe_diagnostic(str(path.relative_to(root)))}:{line_number}: "
                        f"broken link {safe_diagnostic(raw_target)}"
                    )
    return safe_diagnostics(errors)


def scan_secrets(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    excluded = {".git", ".venv", ".pytest_cache", ".ruff_cache", "__pycache__"}
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        if excluded.intersection(path.parts) or path.stat().st_size > 5_000_000:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(
                    f"{safe_diagnostic(str(path.relative_to(root)))}: possible {label}"
                )
    return safe_diagnostics(errors)


def validate_sensitive_files(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    excluded = {".git", ".venv", ".pytest_cache", ".ruff_cache", "__pycache__"}
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        if excluded.intersection(path.parts):
            continue
        relative = path.relative_to(root).as_posix()
        if any(pattern.search(relative) for pattern in SENSITIVE_FILE_PATTERNS):
            errors.append(
                f"{safe_diagnostic(relative)}: sensitive file type must not be committed"
            )
    return safe_diagnostics(errors)


def collect_errors(
    root: Path = ROOT,
    *,
    check_links: bool = True,
    check_generated: bool = True,
    check_secrets: bool = True,
) -> list[str]:
    errors = validate_records(root)
    errors.extend(validate_reconciliation(root))
    if check_links:
        errors.extend(validate_markdown_links(root))
    if check_generated:
        errors.extend(f"generated drift: {path}" for path in generate(root, check=True))
    if check_secrets:
        errors.extend(scan_secrets(root))
        errors.extend(validate_sensitive_files(root))
    return sorted(safe_diagnostics(errors))


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = DiagnosticArgumentParser(
        description=__doc__, prog=safe_diagnostic(Path(sys.argv[0]).name)
    )
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--skip-links", action="store_true")
    parser.add_argument("--skip-generated", action="store_true")
    parser.add_argument("--skip-secrets", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        errors = collect_errors(
            args.root.resolve(),
            check_links=not args.skip_links,
            check_generated=not args.skip_generated,
            check_secrets=not args.skip_secrets,
        )
    except Exception as error:
        # Parser exceptions can contain input excerpts: never emit their text.
        print(
            f"Catalogue validation could not complete ({type(error).__name__}); "
            "check catalogue input files and record structure.",
            file=sys.stderr,
        )
        return 1
    if errors:
        print(f"Catalogue validation failed with {len(errors)} issue(s):")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("Catalogue validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
