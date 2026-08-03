#!/usr/bin/env python3
"""Audit and import the legacy DevOps tools catalogue without losing provenance."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import tempfile
import urllib.parse
from collections import defaultdict
from collections.abc import Sequence
from dataclasses import asdict, dataclass
from io import StringIO
from pathlib import Path

import yaml

from scripts.catalog import ROOT, dump_yaml, stable_json, write_if_changed

TOOL_RE = re.compile(r"^\s*-\s+\[(?P<name>[^]]+)]\((?P<url>[^)]+)\)(?P<rest>.*)$")
HEADING_RE = re.compile(r"^(?P<level>#{1,6})\s+(?P<title>.+?)\s*$")
SECONDARY_LINK_RE = re.compile(r"\[(?P<label>[^]]+)]\((?P<url>[^)]+)\)")
BADGE_RE = re.compile(r"<sup><span\b[^>]*>(?P<label>[^<]+)</span></sup>", re.I)
HTML_COMMENT_RE = re.compile(r"\s*<!--.*?-->\s*")
GUIDANCE_RE = re.compile(
    r"\*{1,2}Use(?: when| for| to)?(?:\*{1,2}|:)?\s*"
    r"(?P<use>.*?)(?:;|\.)\s*\*{0,2}Avoid(?: when| if)?"
    r"(?:\*{1,2}|:)?\s*(?P<avoid>.*?)(?:\*{1,2})?$",
    re.I,
)
HEADING_PREFIX_RE = re.compile(r"^[A-Z]\.\s*")


@dataclass(frozen=True)
class SourceEntry:
    source_file: str
    line: int
    name: str
    primary_url: str
    normalized_url: str
    secondary_urls: tuple[str, ...]
    section: str
    subsection: str
    summary: str
    badges: tuple[str, ...]
    use_when: tuple[str, ...]
    avoid_when: tuple[str, ...]
    raw: str


def normalize_url(value: str) -> str:
    """Return a stable URL identity while preserving meaningful path casing."""
    value = value.strip().rstrip(".,;")
    parsed = urllib.parse.urlsplit(value)
    scheme = parsed.scheme.lower() or "https"
    host = parsed.netloc.lower()
    if scheme == "http" and host.endswith(":80"):
        host = host[:-3]
    if scheme == "https" and host.endswith(":443"):
        host = host[:-4]
    path = parsed.path.rstrip("/")
    query = urllib.parse.parse_qsl(parsed.query, keep_blank_values=True)
    query = [(key, item) for key, item in query if not key.lower().startswith("utm_")]
    return urllib.parse.urlunsplit(
        (scheme, host, path, urllib.parse.urlencode(query, doseq=True), "")
    )


def normalize_heading(value: str) -> str:
    return HEADING_PREFIX_RE.sub("", value).strip()


def normalize_sentence(value: str) -> str:
    value = re.sub(r"\s+", " ", value).strip(" -.;")
    if not value:
        return "Legacy catalogue entry pending factual description review."
    return value[0].upper() + value[1:] + "."


def extract_details(
    rest: str,
) -> tuple[str, tuple[str, ...], tuple[str, ...], tuple[str, ...]]:
    badges = tuple(
        re.sub(r"\s+", " ", match.group("label").strip())
        for match in BADGE_RE.finditer(rest)
    )
    guidance = GUIDANCE_RE.search(rest)
    use_when: tuple[str, ...] = ()
    avoid_when: tuple[str, ...] = ()
    if guidance:
        use_when = (normalize_sentence(guidance.group("use")),)
        avoid_when = (normalize_sentence(guidance.group("avoid")),)

    summary_text = GUIDANCE_RE.sub("", rest)
    summary_text = BADGE_RE.sub("", summary_text)
    summary_text = HTML_COMMENT_RE.sub("", summary_text)
    summary_text = SECONDARY_LINK_RE.sub("", summary_text)
    summary_text = summary_text.replace("()", "")
    return normalize_sentence(summary_text), badges, use_when, avoid_when


def source_files(source_dir: Path) -> list[Path]:
    consolidated = source_dir / "devopstools_final.md"
    category_files = sorted(source_dir.glob("[0-9]*_*/README.md"))
    if not consolidated.is_file():
        raise FileNotFoundError(f"Missing consolidated catalogue: {consolidated}")
    if len(category_files) != 10:
        raise ValueError(
            f"Expected 10 category README files, found {len(category_files)}"
        )
    return [consolidated, *category_files]


def parse_file(path: Path, source_dir: Path) -> list[SourceEntry]:
    section = ""
    subsection = ""
    entries: list[SourceEntry] = []
    relative_path = path.relative_to(source_dir).as_posix()

    lines = path.read_text(encoding="utf-8").splitlines()
    index = 0
    while index < len(lines):
        raw_line = lines[index]
        line_number = index + 1
        heading = HEADING_RE.match(raw_line)
        if heading:
            level = len(heading.group("level"))
            if level == 2:
                section = heading.group("title").strip()
                subsection = ""
            elif level == 3:
                subsection = heading.group("title").strip()
            index += 1
            continue

        match = TOOL_RE.match(raw_line)
        if not match:
            index += 1
            continue
        continuation: list[str] = []
        next_index = index + 1
        while next_index < len(lines):
            candidate = lines[next_index]
            if TOOL_RE.match(candidate) or HEADING_RE.match(candidate):
                break
            stripped = candidate.strip()
            if stripped:
                continuation.append(stripped.removeprefix("- "))
            next_index += 1
        rest = " ".join([match.group("rest"), *continuation])
        secondary_urls = tuple(
            item.group("url").strip() for item in SECONDARY_LINK_RE.finditer(rest)
        )
        primary_url = match.group("url").strip()
        summary, badges, use_when, avoid_when = extract_details(rest)
        entries.append(
            SourceEntry(
                source_file=relative_path,
                line=line_number,
                name=match.group("name").strip(),
                primary_url=primary_url,
                normalized_url=normalize_url(primary_url),
                secondary_urls=secondary_urls,
                section=section,
                subsection=subsection,
                summary=summary,
                badges=badges,
                use_when=use_when,
                avoid_when=avoid_when,
                raw="\n".join(lines[index:next_index]),
            )
        )
        index = next_index

    return entries


def inventory(source_dir: Path, paths: Sequence[Path]) -> list[dict[str, object]]:
    result: list[dict[str, object]] = []
    for path in sorted(item for item in source_dir.rglob("*") if item.is_file()):
        text = path.read_text(encoding="utf-8", errors="replace")
        headings = [
            match.group("title")
            for line in text.splitlines()
            if (match := HEADING_RE.match(line))
        ]
        parsed_count = len(parse_file(path, source_dir)) if path in paths else 0
        result.append(
            {
                "path": path.relative_to(source_dir).as_posix(),
                "bytes": path.stat().st_size,
                "tool_entries": parsed_count,
                "headings": headings,
            }
        )
    return result


def build_audit(source_dir: Path) -> dict[str, object]:
    paths = source_files(source_dir)
    entries = [entry for path in paths for entry in parse_file(path, source_dir)]
    consolidated = [
        entry for entry in entries if entry.source_file == "devopstools_final.md"
    ]
    categories = [
        entry for entry in entries if entry.source_file != "devopstools_final.md"
    ]
    consolidated_urls = {entry.normalized_url for entry in consolidated}
    category_urls = {entry.normalized_url for entry in categories}
    groups: dict[str, list[SourceEntry]] = defaultdict(list)
    for entry in entries:
        groups[entry.normalized_url].append(entry)

    return {
        "inventory": inventory(source_dir, paths),
        "counts": {
            "raw_occurrences": len(entries),
            "consolidated_raw": len(consolidated),
            "category_raw": len(categories),
            "canonical_url_records": len(groups),
            "merged_occurrences": len(entries) - len(groups),
            "consolidated_missing_from_categories": len(
                consolidated_urls - category_urls
            ),
            "categories_missing_from_consolidated": len(
                category_urls - consolidated_urls
            ),
            "duplicate_url_groups": sum(len(group) > 1 for group in groups.values()),
        },
        "entries": [asdict(entry) for entry in entries],
    }


def safe_extract_rar(archive: Path, destination: Path) -> None:
    """Extract a RAR after rejecting absolute, traversal, and link members."""
    import rarfile

    destination = destination.resolve()
    with rarfile.RarFile(archive) as handle:
        for member in handle.infolist():
            member_path = Path(member.filename)
            target = (destination / member_path).resolve()
            if member_path.is_absolute() or not target.is_relative_to(destination):
                raise ValueError(f"Unsafe archive member: {member.filename}")
            if member.is_symlink():
                raise ValueError(f"Archive links are not permitted: {member.filename}")
        handle.extractall(destination)


def locate_source_dir(extracted_root: Path) -> Path:
    candidates = [path.parent for path in extracted_root.rglob("devopstools_final.md")]
    if len(candidates) != 1:
        raise ValueError(
            f"Expected one devopstools_final.md in archive, found {len(candidates)}"
        )
    return candidates[0]


def load_overrides(path: Path) -> dict[str, object]:
    with path.open(encoding="utf-8") as handle:
        result = yaml.safe_load(handle)
    if not isinstance(result, dict):
        raise TypeError(f"{path} must contain a YAML mapping")
    return result


def canonical_url(value: str, aliases: dict[str, str]) -> str:
    normalized = normalize_url(value)
    normalized_aliases = {
        normalize_url(source): normalize_url(target)
        for source, target in aliases.items()
    }
    return normalized_aliases.get(normalized, normalized)


def slugify(value: str) -> str:
    value = value.casefold().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "unnamed-tool"


def is_repository_url(value: str) -> bool:
    parsed = urllib.parse.urlsplit(value)
    parts = [part for part in parsed.path.split("/") if part]
    return (
        parsed.netloc.casefold()
        in {
            "github.com",
            "gitlab.com",
            "codeberg.org",
            "bitbucket.org",
        }
        and len(parts) >= 2
    )


def license_model(entries: list[SourceEntry]) -> str:
    badges = {badge.casefold() for entry in entries for badge in entry.badges}
    if "docs / learning" in badges:
        return "documentation"
    if "source-available" in badges:
        return "source-available"
    if "open-core / saas" in badges:
        return "open-core"
    if "oss" in badges:
        return "oss"
    return "unknown"


def ordered_values(values: set[str], order: list[str]) -> list[str]:
    position = {value: index for index, value in enumerate(order)}
    return sorted(values, key=lambda value: (position.get(value, len(order)), value))


def build_records(
    entries: list[SourceEntry],
    taxonomy: dict[str, object],
    overrides: dict[str, object],
    verified_on: str,
) -> tuple[list[dict[str, object]], dict[str, list[SourceEntry]]]:
    aliases = dict(overrides.get("url_aliases", {}))
    groups: dict[str, list[SourceEntry]] = defaultdict(list)
    for entry in entries:
        groups[canonical_url(entry.primary_url, aliases)].append(entry)

    heading_categories = dict(overrides["heading_categories"])
    category_roles = dict(overrides["category_roles"])
    category_lifecycle = dict(overrides["category_lifecycle"])
    record_overrides = dict(overrides.get("record_overrides", {}))
    category_order = [item["id"] for item in taxonomy["categories"]]
    role_order = [item["id"] for item in taxonomy["roles"]]
    lifecycle_order = list(taxonomy["lifecycle_stages"])

    preferred: dict[str, SourceEntry] = {}
    for url, group in groups.items():
        preferred[url] = sorted(
            group,
            key=lambda item: (
                item.source_file != "devopstools_final.md",
                item.line,
                item.name.casefold(),
            ),
        )[0]

    base_ids = {url: slugify(entry.name) for url, entry in preferred.items()}
    id_counts: dict[str, int] = defaultdict(int)
    for base_id in base_ids.values():
        id_counts[base_id] += 1

    records: list[dict[str, object]] = []
    for url in sorted(groups):
        group = groups[url]
        representative = preferred[url]
        base_id = base_ids[url]
        tool_id = base_id
        if id_counts[base_id] > 1:
            digest = hashlib.sha256(url.encode()).hexdigest()[:8]
            tool_id = f"{base_id}-{digest}"

        categories = set()
        subcategories = set()
        for entry in group:
            heading = normalize_heading(entry.subsection)
            category = heading_categories.get(heading)
            if category:
                categories.add(category)
            if heading:
                subcategories.add(heading)
        if not categories:
            categories.add("emerging-experimental")

        roles = {
            role for category in categories for role in category_roles.get(category, [])
        }
        lifecycle_stages = {
            stage
            for category in categories
            for stage in category_lifecycle.get(category, [])
        }
        all_urls = [
            item
            for entry in group
            for item in (entry.primary_url, *entry.secondary_urls)
            if item.startswith(("http://", "https://"))
        ]
        repositories = sorted(
            {
                normalize_url(item)
                for item in all_urls
                if is_repository_url(item)
                and (
                    canonical_url(item, aliases) not in groups
                    or canonical_url(item, aliases) == url
                )
            }
        )
        official_urls = sorted(
            {normalize_url(item) for item in all_urls if not is_repository_url(item)}
        )
        summaries = [
            entry.summary
            for entry in sorted(group, key=lambda item: len(item.summary), reverse=True)
            if "pending factual description review" not in entry.summary
        ]

        record: dict[str, object] = {
            "id": tool_id,
            "name": representative.name,
            "summary": summaries[0] if summaries else representative.summary,
        }
        if official_urls:
            record["official_url"] = official_urls[0]
        if repositories:
            record["repository_url"] = repositories[0]
        if not official_urls and not repositories:
            record["official_url"] = normalize_url(representative.primary_url)
        record.update(
            {
                "categories": ordered_values(categories, category_order),
                "subcategories": sorted(subcategories),
                "roles": ordered_values(roles, role_order),
                "lifecycle_stages": ordered_values(lifecycle_stages, lifecycle_order),
                "use_when": sorted(
                    {item for entry in group for item in entry.use_when}
                ),
                "avoid_when": sorted(
                    {item for entry in group for item in entry.avoid_when}
                ),
                "deployment_models": [],
                "license_model": license_model(group),
                "maturity": (
                    "experimental"
                    if "emerging-experimental" in categories
                    else "unknown"
                ),
                "status": "needs-review",
                "alternatives": [],
                "tags": [],
                "verified_on": verified_on,
                "sources": sorted(
                    {f"legacy:{entry.source_file}#L{entry.line}" for entry in group}
                ),
                "needs_review": True,
            }
        )
        if url in record_overrides:
            record.update(record_overrides[url])
        records.append(record)

    return sorted(records, key=lambda item: item["id"]), groups


def classify_inventory_item(item: dict[str, object]) -> dict[str, object]:
    path = str(item["path"])
    if path == "devopstools_final.md":
        purpose, disposition = "Consolidated legacy catalogue", "authoritative"
    elif re.match(r"[0-9]+_.+/README\.md$", path):
        purpose, disposition = "Enriched legacy category catalogue", "supporting"
    elif path == "optimized_devops_tools.md":
        purpose, disposition = "Conceptual taxonomy proposal", "obsolete"
    elif path == "linter_fixer.py":
        purpose, disposition = "Legacy Markdown linter", "supporting"
    elif path == "report.json":
        purpose, disposition = (
            "Legacy linter output reporting 614 entries",
            "generated-stale",
        )
    elif path.startswith("badge_audit_recommendations_full"):
        purpose, disposition = "Legacy badge audit", "generated-stale"
    else:
        purpose, disposition = "Unclassified source material", "needs-review"
    return {**item, "purpose": purpose, "disposition": disposition}


def csv_text(rows: list[dict[str, object]], fieldnames: list[str]) -> str:
    output = StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=fieldnames, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def write_import(
    source_dir: Path,
    output_root: Path,
    overrides_path: Path,
    verified_on: str,
) -> dict[str, int]:
    audit = build_audit(source_dir)
    entries = [
        SourceEntry(
            **{
                **item,
                "secondary_urls": tuple(item["secondary_urls"]),
                "badges": tuple(item["badges"]),
                "use_when": tuple(item["use_when"]),
                "avoid_when": tuple(item["avoid_when"]),
            }
        )
        for item in audit["entries"]
    ]
    taxonomy = yaml.safe_load(
        (output_root / "data" / "taxonomy.yaml").read_text(encoding="utf-8")
    )
    overrides = load_overrides(overrides_path)
    records, groups = build_records(entries, taxonomy, overrides, verified_on)
    disposition_overrides = dict(overrides.get("disposition_overrides", {}))
    category_ids = [item["id"] for item in taxonomy["categories"]]

    tools_dir = output_root / "data" / "tools"
    tools_dir.mkdir(parents=True, exist_ok=True)
    for category_id in category_ids:
        category_records = [
            record for record in records if record["categories"][0] == category_id
        ]
        write_if_changed(tools_dir / f"{category_id}.yaml", dump_yaml(category_records))

    record_by_url = {
        canonical_url(
            str(record.get("official_url") or record.get("repository_url")),
            dict(overrides.get("url_aliases", {})),
        ): record
        for record in records
    }
    # A secondary repository URL can be selected ahead of the primary URL. Resolve
    # identity directly from the source groups so reconciliation remains exact.
    record_by_url = {}
    for record in records:
        for source in record["sources"]:
            source_file, line_text = source.removeprefix("legacy:").split("#L")
            match = next(
                entry
                for entry in entries
                if entry.source_file == source_file and entry.line == int(line_text)
            )
            record_by_url[
                canonical_url(match.primary_url, dict(overrides.get("url_aliases", {})))
            ] = record

    reconciliation: list[dict[str, object]] = []
    for url in sorted(groups):
        group = sorted(
            groups[url],
            key=lambda item: (
                item.source_file != "devopstools_final.md",
                item.source_file,
                item.line,
            ),
        )
        record = record_by_url[url]
        for index, entry in enumerate(group):
            disposition_override = disposition_overrides.get(url)
            if index == 0 and disposition_override:
                disposition = disposition_override["disposition"]
                reason = disposition_override["reason"]
            elif index == 0:
                disposition = "kept"
                reason = "Canonical occurrence retained"
            else:
                disposition = "merged"
                reason = "Merged by normalized canonical URL; provenance preserved"
            reconciliation.append(
                {
                    "source_file": entry.source_file,
                    "line": entry.line,
                    "source_name": entry.name,
                    "source_url": entry.primary_url,
                    "canonical_id": record["id"],
                    "disposition": disposition,
                    "reason": reason,
                }
            )

    migration_dir = output_root / "migration"
    write_if_changed(
        migration_dir / "source-inventory.json",
        stable_json([classify_inventory_item(item) for item in audit["inventory"]]),
    )
    write_if_changed(
        migration_dir / "source-entries.json",
        stable_json(audit["entries"]),
    )
    write_if_changed(
        migration_dir / "reconciliation.csv",
        csv_text(
            reconciliation,
            [
                "source_file",
                "line",
                "source_name",
                "source_url",
                "canonical_id",
                "disposition",
                "reason",
            ],
        ),
    )
    return {
        **audit["counts"],
        "normalized_url_merges": audit["counts"]["merged_occurrences"],
        "reviewed_alias_merges": audit["counts"]["canonical_url_records"]
        - len(records),
        "merged_occurrences": len(entries) - len(records),
        "canonical_records": len(records),
        "reconciliation_rows": len(reconciliation),
    }


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "source", type=Path, help="Extracted source folder or RAR archive"
    )
    parser.add_argument(
        "--summary-only",
        action="store_true",
        help="Print inventory and counts without all parsed source entries",
    )
    parser.add_argument("--output-root", type=Path, default=ROOT)
    parser.add_argument(
        "--overrides",
        type=Path,
        default=ROOT / "config" / "import-overrides.yaml",
    )
    parser.add_argument("--verified-on", default="2026-08-03")
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write canonical data and migration artefacts",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    source = args.source.resolve()
    if source.is_dir():
        source_dir = source
        temporary_directory = None
    elif source.suffix.casefold() == ".rar":
        temporary_directory = tempfile.TemporaryDirectory(prefix="devops-tools-import-")
        extracted_root = Path(temporary_directory.name)
        safe_extract_rar(source, extracted_root)
        source_dir = locate_source_dir(extracted_root)
    else:
        raise ValueError("Source must be an extracted directory or .rar archive")

    try:
        if args.write:
            result = write_import(
                source_dir,
                args.output_root.resolve(),
                args.overrides.resolve(),
                args.verified_on,
            )
        else:
            result = build_audit(source_dir)
            if args.summary_only:
                result.pop("entries")
        print(json.dumps(result, indent=2, ensure_ascii=False))
    finally:
        if temporary_directory is not None:
            temporary_directory.cleanup()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
