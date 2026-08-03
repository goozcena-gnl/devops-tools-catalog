#!/usr/bin/env python3
"""Check catalogue links with retries, caching, and non-binary classifications."""

from __future__ import annotations

import argparse
import concurrent.futures
import dataclasses
import json
import os
import socket
import ssl
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from collections.abc import Sequence
from datetime import UTC, datetime, timedelta
from pathlib import Path

from scripts.catalog import ROOT, load_tools, stable_json, write_if_changed

USER_AGENT = "DevOps-Tools-catalog-link-audit/1.0 (+https://github.com/goozcena-gnl/Devops-Tools)"
DEFAULT_CACHE = ROOT / "reports" / "link-cache.json"
DEFAULT_JSON_REPORT = ROOT / "reports" / "link-report.json"
DEFAULT_MARKDOWN_REPORT = ROOT / "reports" / "link-report.md"
TRANSIENT_CODES = {408, 425, 429, 500, 502, 503, 504}


@dataclasses.dataclass(frozen=True)
class LinkResult:
    url: str
    classification: str
    status: int | None
    final_url: str | None
    redirect_codes: tuple[int, ...]
    attempts: int
    error: str | None
    checked_at: str
    repository_archived: bool | None = None


class TrackingRedirectHandler(urllib.request.HTTPRedirectHandler):
    def __init__(self) -> None:
        super().__init__()
        self.codes: list[int] = []

    def redirect_request(self, request, file_pointer, code, message, headers, new_url):
        self.codes.append(code)
        return super().redirect_request(
            request, file_pointer, code, message, headers, new_url
        )


class DomainRateLimiter:
    def __init__(self, interval_seconds: float) -> None:
        self.interval_seconds = interval_seconds
        self._last_request: dict[str, float] = {}
        self._locks: dict[str, threading.Lock] = {}
        self._guard = threading.Lock()

    def wait(self, url: str) -> None:
        domain = urllib.parse.urlsplit(url).netloc.casefold()
        with self._guard:
            lock = self._locks.setdefault(domain, threading.Lock())
        with lock:
            elapsed = time.monotonic() - self._last_request.get(domain, 0.0)
            delay = self.interval_seconds - elapsed
            if delay > 0:
                time.sleep(delay)
            self._last_request[domain] = time.monotonic()


def classify_status(status: int, redirects: list[int]) -> str:
    if 200 <= status < 300:
        if redirects:
            return (
                "permanent-redirect"
                if any(code in {301, 308} for code in redirects)
                else "valid-redirect"
            )
        return "valid"
    if status == 401:
        return "authentication-required"
    if status == 403:
        return "restricted-or-bot-blocked"
    if status == 429:
        return "rate-limited"
    if status in {404, 410}:
        return "manual-verification-required"
    if status in TRANSIENT_CODES:
        return "transient-failure"
    return "http-error"


def repository_coordinates(url: str) -> tuple[str, str] | None:
    parsed = urllib.parse.urlsplit(url)
    if parsed.netloc.casefold() != "github.com":
        return None
    parts = [part for part in parsed.path.split("/") if part]
    reserved_routes = {
        "about",
        "collections",
        "customer-stories",
        "enterprise",
        "features",
        "marketplace",
        "orgs",
        "security",
        "settings",
        "sponsors",
        "topics",
    }
    if len(parts) < 2 or parts[0].casefold() in reserved_routes:
        return None
    return parts[0], parts[1].removesuffix(".git")


def github_repository_result(url: str, timeout: float) -> LinkResult | None:
    coordinates = repository_coordinates(url)
    if not coordinates:
        return None
    owner, repository = coordinates
    request = urllib.request.Request(
        f"https://api.github.com/repos/{owner}/{repository}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": USER_AGENT,
            **(
                {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}
                if os.environ.get("GITHUB_TOKEN")
                else {}
            ),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.load(response)
            final_url = str(payload.get("html_url") or url)
            archived = bool(payload.get("archived"))
            if archived:
                classification = "repository-archived"
            elif final_url.rstrip("/") != url.rstrip("/"):
                classification = "permanent-redirect"
            else:
                classification = "valid"
            return LinkResult(
                url=url,
                classification=classification,
                status=int(response.status),
                final_url=final_url,
                redirect_codes=(),
                attempts=1,
                error=None,
                checked_at=datetime.now(UTC).isoformat(),
                repository_archived=archived,
            )
    except urllib.error.HTTPError as error:
        classification = classify_status(int(error.code), [])
        return LinkResult(
            url=url,
            classification=classification,
            status=int(error.code),
            final_url=error.geturl(),
            redirect_codes=(),
            attempts=1,
            error=f"HTTP {error.code}: {error.reason}",
            checked_at=datetime.now(UTC).isoformat(),
            repository_archived=None,
        )
    except (OSError, ValueError):
        return None


def check_url(
    url: str,
    *,
    limiter: DomainRateLimiter,
    retries: int,
    timeout: float,
    check_archived: bool,
) -> LinkResult:
    if check_archived and repository_coordinates(url):
        limiter.wait(url)
        if repository_result := github_repository_result(url, timeout):
            return repository_result

    last_status: int | None = None
    last_error: str | None = None
    final_url: str | None = None
    redirect_codes: list[int] = []
    classification = "inconclusive"
    attempts = 0

    for attempt in range(retries + 1):
        attempts = attempt + 1
        limiter.wait(url)
        handler = TrackingRedirectHandler()
        opener = urllib.request.build_opener(handler)
        request = urllib.request.Request(
            url,
            method="HEAD",
            headers={"User-Agent": USER_AGENT, "Accept": "*/*"},
        )
        try:
            with opener.open(request, timeout=timeout) as response:
                last_status = int(response.status)
                final_url = response.geturl()
                redirect_codes = handler.codes
                classification = classify_status(last_status, redirect_codes)
                last_error = None
        except urllib.error.HTTPError as error:
            last_status = int(error.code)
            final_url = error.geturl()
            redirect_codes = handler.codes
            classification = classify_status(last_status, redirect_codes)
            last_error = f"HTTP {error.code}: {error.reason}"
            if error.code in {405, 501}:
                request = urllib.request.Request(
                    url,
                    method="GET",
                    headers={
                        "User-Agent": USER_AGENT,
                        "Accept": "text/html,application/xhtml+xml,*/*;q=0.1",
                        "Range": "bytes=0-1023",
                    },
                )
                try:
                    with opener.open(request, timeout=timeout) as response:
                        last_status = int(response.status)
                        final_url = response.geturl()
                        redirect_codes = handler.codes
                        classification = classify_status(last_status, redirect_codes)
                        last_error = None
                except urllib.error.HTTPError as get_error:
                    last_status = int(get_error.code)
                    classification = classify_status(last_status, handler.codes)
                    last_error = f"HTTP {get_error.code}: {get_error.reason}"
        except ssl.SSLError as error:
            classification = "tls-failure"
            last_error = f"{type(error).__name__}: {error}"
        except TimeoutError as error:
            classification = "timeout-inconclusive"
            last_error = f"{type(error).__name__}: {error}"
        except urllib.error.URLError as error:
            if isinstance(error.reason, ssl.SSLError):
                classification = "tls-failure"
            elif isinstance(error.reason, socket.gaierror):
                classification = "dns-inconclusive"
            else:
                classification = "network-inconclusive"
            last_error = f"{type(error.reason).__name__}: {error.reason}"

        should_retry = (
            classification
            in {
                "rate-limited",
                "transient-failure",
                "timeout-inconclusive",
                "dns-inconclusive",
                "network-inconclusive",
            }
            and attempt < retries
        )
        if not should_retry:
            break
        time.sleep(0.5 * (2**attempt))

    return LinkResult(
        url=url,
        classification=classification,
        status=last_status,
        final_url=final_url,
        redirect_codes=tuple(redirect_codes),
        attempts=attempts,
        error=last_error,
        checked_at=datetime.now(UTC).isoformat(),
        repository_archived=None,
    )


def catalogue_urls(root: Path) -> list[str]:
    fields = ("official_url", "repository_url", "documentation_url")
    return sorted(
        {
            str(tool[field])
            for tool in load_tools(root)
            for field in fields
            if tool.get(field)
        }
    )


def load_cache(path: Path, max_age: timedelta) -> dict[str, LinkResult]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        results = {}
        for url, item in payload.items():
            checked = datetime.fromisoformat(item["checked_at"])
            if datetime.now(UTC) - checked <= max_age:
                item["redirect_codes"] = tuple(item.get("redirect_codes", []))
                results[url] = LinkResult(**item)
        return results
    except (KeyError, TypeError, ValueError, json.JSONDecodeError):
        return {}


def markdown_report(results: list[LinkResult]) -> str:
    counts = Counter(result.classification for result in results)
    rows = [
        "# Link audit summary",
        "",
        f"Checked {len(results)} unique catalogue URLs.",
        "",
        "| Classification | Count |",
        "|---|---:|",
    ]
    rows.extend(f"| {name} | {count} |" for name, count in sorted(counts.items()))
    rows.extend(
        [
            "",
            "## Follow-up",
            "",
            "| URL | Classification | Status | Detail |",
            "|---|---|---:|---|",
        ]
    )
    routine = {"valid", "valid-redirect"}
    for result in results:
        if result.classification in routine:
            continue
        detail = result.error or result.final_url or ""
        rows.append(
            f"| {result.url} | {result.classification} | {result.status or ''} | {detail} |"
        )
    rows.append("")
    return "\n".join(rows)


def run_audit(
    root: Path,
    *,
    workers: int,
    retries: int,
    timeout: float,
    domain_interval: float,
    cache_path: Path,
    cache_hours: int,
    check_archived: bool,
) -> list[LinkResult]:
    urls = catalogue_urls(root)
    cache = load_cache(cache_path, timedelta(hours=cache_hours))
    limiter = DomainRateLimiter(domain_interval)
    results = dict(cache)
    pending = [url for url in urls if url not in cache]
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(
                check_url,
                url,
                limiter=limiter,
                retries=retries,
                timeout=timeout,
                check_archived=check_archived,
            ): url
            for url in pending
        }
        for future in concurrent.futures.as_completed(futures):
            results[futures[future]] = future.result()
    selected = [results[url] for url in urls]
    write_if_changed(
        cache_path,
        stable_json({result.url: dataclasses.asdict(result) for result in selected}),
    )
    return selected


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--retries", type=int, default=2)
    parser.add_argument("--timeout", type=float, default=12.0)
    parser.add_argument("--domain-interval", type=float, default=0.2)
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--cache-hours", type=int, default=24)
    parser.add_argument("--json-report", type=Path, default=DEFAULT_JSON_REPORT)
    parser.add_argument("--markdown-report", type=Path, default=DEFAULT_MARKDOWN_REPORT)
    parser.add_argument("--check-archived", action="store_true")
    parser.add_argument("--strict", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    root = args.root.resolve()
    results = run_audit(
        root,
        workers=max(1, min(args.workers, 16)),
        retries=max(0, min(args.retries, 5)),
        timeout=args.timeout,
        domain_interval=max(0.0, args.domain_interval),
        cache_path=args.cache,
        cache_hours=args.cache_hours,
        check_archived=args.check_archived,
    )
    payload = {
        "generated_at": datetime.now(UTC).isoformat(),
        "summary": dict(
            sorted(Counter(item.classification for item in results).items())
        ),
        "results": [dataclasses.asdict(item) for item in results],
    }
    write_if_changed(args.json_report, stable_json(payload))
    write_if_changed(args.markdown_report, markdown_report(results))
    print(json.dumps(payload["summary"], indent=2))
    blocking = {
        "manual-verification-required",
        "tls-failure",
        "http-error",
        "repository-archived",
    }
    return int(args.strict and any(item.classification in blocking for item in results))


if __name__ == "__main__":
    raise SystemExit(main())
