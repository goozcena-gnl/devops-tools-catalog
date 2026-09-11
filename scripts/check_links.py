#!/usr/bin/env python3
"""Check catalogue links with retries, caching, and non-binary classifications."""

from __future__ import annotations

import argparse
import concurrent.futures
import dataclasses
import http.cookiejar
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
from collections.abc import Mapping, Sequence
from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from typing import Any

from scripts.catalog import ROOT, load_tools, stable_json, write_if_changed

USER_AGENT = "DevOps-Tools-catalog-link-audit/1.0 (+https://github.com/goozcena-gnl/Devops-Tools)"
DEFAULT_CACHE = ROOT / "reports" / "link-cache.json"
DEFAULT_JSON_REPORT = ROOT / "reports" / "link-report.json"
DEFAULT_MARKDOWN_REPORT = ROOT / "reports" / "link-report.md"
DEFAULT_BASELINE = ROOT / "config" / "link-audit-baseline.json"
TRANSIENT_CODES = {408, 425, 429, 500, 502, 503, 504}
GET_FALLBACK_CODES = {404, 405, 501}
CACHE_VERSION = 4
BLOCKING_CLASSIFICATIONS = frozenset(
    {
        "manual-verification-required",
        "tls-failure",
        "http-error",
        "repository-archived-unexpected",
    }
)


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
    repository_archived_expected: bool | None = None
    request_method: str = "HEAD"
    head_status: int | None = None
    get_fallback: bool = False
    get_confirmation: bool = False
    checker_version: int = CACHE_VERSION


@dataclasses.dataclass(frozen=True)
class UrlContext:
    repository_record_ids: tuple[str, ...] = ()
    repository_archived_expected: bool = False


@dataclasses.dataclass(frozen=True)
class HttpOutcome:
    classification: str
    status: int | None
    final_url: str | None
    redirect_codes: tuple[int, ...]
    error: str | None
    retryable: bool = False


@dataclasses.dataclass(frozen=True)
class BaselineItem:
    url: str
    classification: str
    reason: str
    reference: str
    reviewed_on: str


@dataclasses.dataclass(frozen=True)
class StrictAssessment:
    blocking_known: tuple[LinkResult, ...]
    blocking_new: tuple[LinkResult, ...]
    baseline_changed: tuple[tuple[BaselineItem, LinkResult], ...]
    baseline_resolved: tuple[BaselineItem, ...]

    @property
    def passed(self) -> bool:
        return not self.blocking_new


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


def classify_repository_archival(archived: bool, expected: bool) -> str:
    if not archived:
        return "valid"
    return (
        "repository-archived-expected" if expected else "repository-archived-unexpected"
    )


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


def github_repository_result(
    url: str, timeout: float, *, repository_archived_expected: bool
) -> LinkResult | None:
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
                classification = classify_repository_archival(
                    archived, repository_archived_expected
                )
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
                repository_archived_expected=repository_archived_expected,
                request_method="GITHUB_API",
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
            repository_archived_expected=repository_archived_expected,
            request_method="GITHUB_API",
        )
    except (OSError, ValueError):
        return None


def _tls_outcome(error: ssl.SSLError) -> HttpOutcome:
    # Only explicit EOF transport conditions are retryable. Unknown SSL errors
    # and certificate validation failures remain immediate strict blockers.
    retryable = not isinstance(error, ssl.SSLCertVerificationError) and (
        isinstance(error, ssl.SSLEOFError)
        or getattr(error, "reason", None) == "UNEXPECTED_EOF_WHILE_READING"
    )
    return HttpOutcome(
        "tls-failure", None, None, (), f"{type(error).__name__}: {error}", retryable
    )


def _http_request(
    url: str, *, method: str, timeout: float, ranged: bool = False
) -> HttpOutcome:
    handler = TrackingRedirectHandler()
    cookie_jar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(
        handler,
        urllib.request.HTTPCookieProcessor(cookie_jar),
    )
    headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if method == "GET":
        headers.update(
            {
                "Accept": "text/html,application/xhtml+xml,*/*;q=0.1",
            }
        )
        if ranged:
            headers["Range"] = "bytes=0-1023"
    request = urllib.request.Request(url, method=method, headers=headers)
    try:
        with opener.open(request, timeout=timeout) as response:
            status = int(response.status)
            return HttpOutcome(
                classification=classify_status(status, handler.codes),
                status=status,
                final_url=response.geturl(),
                redirect_codes=tuple(handler.codes),
                error=None,
            )
    except urllib.error.HTTPError as error:
        status = int(error.code)
        return HttpOutcome(
            classification=classify_status(status, handler.codes),
            status=status,
            final_url=error.geturl(),
            redirect_codes=tuple(handler.codes),
            error=f"HTTP {error.code}: {error.reason}",
        )
    except ssl.SSLError as error:
        return _tls_outcome(error)
    except TimeoutError as error:
        return HttpOutcome(
            "timeout-inconclusive", None, None, (), f"{type(error).__name__}: {error}"
        )
    except urllib.error.URLError as error:
        if isinstance(error.reason, ssl.SSLError):
            return _tls_outcome(error.reason)
        elif isinstance(error.reason, socket.gaierror):
            classification = "dns-inconclusive"
        else:
            classification = "network-inconclusive"
        return HttpOutcome(
            classification,
            None,
            None,
            (),
            f"{type(error.reason).__name__}: {error.reason}",
        )


def check_url(
    url: str,
    *,
    limiter: DomainRateLimiter,
    retries: int,
    timeout: float,
    check_archived: bool,
    repository_archived_expected: bool = False,
) -> LinkResult:
    if check_archived and repository_coordinates(url):
        limiter.wait(url)
        if repository_result := github_repository_result(
            url,
            timeout,
            repository_archived_expected=repository_archived_expected,
        ):
            return repository_result

    outcome = HttpOutcome("inconclusive", None, None, (), None)
    head_status: int | None = None
    request_method = "HEAD"
    get_fallback = False
    get_confirmation = False
    attempts = 0

    for attempt in range(retries + 1):
        attempts = attempt + 1
        limiter.wait(url)
        outcome = _http_request(url, method="HEAD", timeout=timeout)
        head_status = outcome.status
        request_method = "HEAD"
        get_fallback = False
        get_confirmation = False
        if outcome.status in GET_FALLBACK_CODES:
            limiter.wait(url)
            outcome = _http_request(url, method="GET", timeout=timeout, ranged=True)
            request_method = "GET"
            get_fallback = True
            if outcome.status == 206:
                # Confirm the ordinary resource status without downloading its body.
                limiter.wait(url)
                outcome = _http_request(
                    url, method="GET", timeout=timeout, ranged=False
                )
                get_confirmation = True

        should_retry = (
            outcome.retryable
            or outcome.classification
            in {
                "rate-limited",
                "transient-failure",
                "timeout-inconclusive",
                "dns-inconclusive",
                "network-inconclusive",
            }
        ) and attempt < retries
        if not should_retry:
            break
        time.sleep(0.5 * (2**attempt))

    return LinkResult(
        url=url,
        classification=outcome.classification,
        status=outcome.status,
        final_url=outcome.final_url,
        redirect_codes=outcome.redirect_codes,
        attempts=attempts,
        error=outcome.error,
        checked_at=datetime.now(UTC).isoformat(),
        repository_archived=None,
        repository_archived_expected=repository_archived_expected,
        request_method=request_method,
        head_status=head_status,
        get_fallback=get_fallback,
        get_confirmation=get_confirmation,
    )


def catalogue_url_contexts(root: Path) -> dict[str, UrlContext]:
    fields = ("official_url", "repository_url", "documentation_url")
    tools = load_tools(root)
    urls = {str(tool[field]) for tool in tools for field in fields if tool.get(field)}
    contexts: dict[str, UrlContext] = {}
    for url in sorted(urls):
        records = [tool for tool in tools if tool.get("repository_url") == url]
        contexts[url] = UrlContext(
            repository_record_ids=tuple(str(tool["id"]) for tool in records),
            repository_archived_expected=bool(records)
            and all(tool.get("repository_archived") is True for tool in records),
        )
    return contexts


def catalogue_urls(root: Path) -> list[str]:
    return list(catalogue_url_contexts(root))


def load_cache(path: Path, max_age: timedelta) -> dict[str, LinkResult]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        results = {}
        for url, item in payload.items():
            if item.get("checker_version") != CACHE_VERSION:
                continue
            checked = datetime.fromisoformat(item["checked_at"])
            if datetime.now(UTC) - checked <= max_age:
                item["redirect_codes"] = tuple(item.get("redirect_codes", []))
                results[url] = LinkResult(**item)
        return results
    except (KeyError, TypeError, ValueError, json.JSONDecodeError):
        return {}


def cache_result_matches_context(
    result: LinkResult, context: UrlContext, *, check_archived: bool
) -> bool:
    if repository_coordinates(result.url) is None:
        return True
    if check_archived:
        return (
            result.request_method == "GITHUB_API"
            and result.repository_archived_expected
            == context.repository_archived_expected
        )
    return result.request_method != "GITHUB_API"


def load_baseline(path: Path) -> dict[str, BaselineItem]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("version") != 1:
        raise ValueError(f"{path}: unsupported baseline version")
    items: dict[str, BaselineItem] = {}
    for raw_item in payload.get("reviewed_blockers", []):
        item = BaselineItem(**raw_item)
        if item.url in items:
            raise ValueError(f"{path}: duplicate baseline URL: {item.url}")
        if item.classification not in BLOCKING_CLASSIFICATIONS:
            raise ValueError(
                f"{path}: nonblocking baseline classification: {item.classification}"
            )
        date.fromisoformat(item.reviewed_on)
        items[item.url] = item
    return items


def assess_strict_results(
    results: Sequence[LinkResult], baseline: Mapping[str, BaselineItem]
) -> StrictAssessment:
    result_by_url = {result.url: result for result in results}
    blocking_known: list[LinkResult] = []
    blocking_new: list[LinkResult] = []
    baseline_changed: list[tuple[BaselineItem, LinkResult]] = []
    baseline_resolved: list[BaselineItem] = []

    for url, item in baseline.items():
        result = result_by_url.get(url)
        if result is None or result.classification not in BLOCKING_CLASSIFICATIONS:
            baseline_resolved.append(item)
        elif result.classification == item.classification:
            blocking_known.append(result)
        else:
            baseline_changed.append((item, result))
            blocking_new.append(result)

    for result in results:
        if (
            result.classification in BLOCKING_CLASSIFICATIONS
            and result.url not in baseline
        ):
            blocking_new.append(result)

    return StrictAssessment(
        blocking_known=tuple(sorted(blocking_known, key=lambda item: item.url)),
        blocking_new=tuple(sorted(blocking_new, key=lambda item: item.url)),
        baseline_changed=tuple(sorted(baseline_changed, key=lambda item: item[0].url)),
        baseline_resolved=tuple(sorted(baseline_resolved, key=lambda item: item.url)),
    )


def result_strict_status(
    result: LinkResult, baseline: Mapping[str, BaselineItem]
) -> str:
    if result.classification not in BLOCKING_CLASSIFICATIONS:
        return "nonblocking"
    item = baseline.get(result.url)
    if item and item.classification == result.classification:
        return "blocking-known"
    return "blocking-new"


def strict_exit_code(strict: bool, assessment: StrictAssessment) -> int:
    return int(strict and not assessment.passed)


def report_payload(
    results: Sequence[LinkResult],
    baseline: Mapping[str, BaselineItem],
    assessment: StrictAssessment,
) -> dict[str, Any]:
    return {
        "generated_at": datetime.now(UTC).isoformat(),
        "summary": dict(
            sorted(Counter(item.classification for item in results).items())
        ),
        "strict": {
            "blocking_new": len(assessment.blocking_new),
            "blocking_known": len(assessment.blocking_known),
            "strict_result": "PASS" if assessment.passed else "FAIL",
            "baseline_changed": [
                {
                    "url": item.url,
                    "baseline_classification": item.classification,
                    "current_classification": result.classification,
                }
                for item, result in assessment.baseline_changed
            ],
            "baseline_resolved": [
                dataclasses.asdict(item) for item in assessment.baseline_resolved
            ],
        },
        "results": [
            {
                **dataclasses.asdict(item),
                "strict_status": result_strict_status(item, baseline),
                "baseline_classification": (
                    baseline[item.url].classification if item.url in baseline else None
                ),
            }
            for item in results
        ],
    }


def markdown_report(
    results: list[LinkResult],
    baseline: Mapping[str, BaselineItem],
    assessment: StrictAssessment,
) -> str:
    counts = Counter(result.classification for result in results)
    rows = [
        "# Link audit summary",
        "",
        f"Checked {len(results)} unique catalogue URLs.",
        "",
        f"- `blocking_new`: **{len(assessment.blocking_new)}**",
        f"- `blocking_known`: **{len(assessment.blocking_known)}**",
        f"- `strict_result`: **{'PASS' if assessment.passed else 'FAIL'}**",
        "",
        "| Classification | Count |",
        "|---|---:|",
    ]
    rows.extend(f"| {name} | {count} |" for name, count in sorted(counts.items()))
    rows.extend(
        [
            "",
            "## Strict blockers",
            "",
            "| URL | Raw classification | Baseline | Strict status |",
            "|---|---|---|---|",
        ]
    )
    blockers = sorted(
        (*assessment.blocking_new, *assessment.blocking_known),
        key=lambda item: item.url,
    )
    for result in blockers:
        baseline_classification = (
            baseline[result.url].classification if result.url in baseline else ""
        )
        rows.append(
            f"| {result.url} | {result.classification} | "
            f"{baseline_classification} | {result_strict_status(result, baseline)} |"
        )
    if not blockers:
        rows.append("| _None_ |  |  |  |")

    rows.extend(
        [
            "",
            "## HEAD to GET fallbacks",
            "",
            "| URL | HEAD status | GET status | Ordinary GET confirmation | Raw classification |",
            "|---|---:|---:|---|---|",
        ]
    )
    recoveries = [result for result in results if result.get_fallback]
    for result in recoveries:
        rows.append(
            f"| {result.url} | {result.head_status or ''} | "
            f"{result.status or ''} | {'yes' if result.get_confirmation else 'no'} | "
            f"{result.classification} |"
        )
    if not recoveries:
        rows.append("| _None_ |  |  |  |  |")

    rows.extend(
        [
            "",
            "## Non-routine results",
            "",
            "| URL | Raw classification | Archive expectation | Status | Detail |",
            "|---|---|---|---:|---|",
        ]
    )
    routine = {"valid", "valid-redirect", "permanent-redirect"}
    for result in results:
        if result.classification in routine:
            continue
        detail = result.error or result.final_url or ""
        archive_expectation = ""
        if result.repository_archived:
            archive_expectation = (
                "expected" if result.repository_archived_expected else "unexpected"
            )
        rows.append(
            f"| {result.url} | {result.classification} | {archive_expectation} | "
            f"{result.status or ''} | {detail} |"
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
    contexts = catalogue_url_contexts(root)
    urls = list(contexts)
    loaded_cache = load_cache(cache_path, timedelta(hours=cache_hours))
    cache = {
        url: result
        for url, result in loaded_cache.items()
        if url in contexts
        and cache_result_matches_context(
            result, contexts[url], check_archived=check_archived
        )
    }
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
                repository_archived_expected=contexts[url].repository_archived_expected,
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
    parser.add_argument("--baseline", type=Path, default=DEFAULT_BASELINE)
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
    baseline = load_baseline(args.baseline)
    assessment = assess_strict_results(results, baseline)
    payload = report_payload(results, baseline, assessment)
    write_if_changed(args.json_report, stable_json(payload))
    write_if_changed(
        args.markdown_report, markdown_report(results, baseline, assessment)
    )
    print(json.dumps(payload["summary"], indent=2))
    print(f"blocking_new: {len(assessment.blocking_new)}")
    print(f"blocking_known: {len(assessment.blocking_known)}")
    print(f"strict_result: {'PASS' if assessment.passed else 'FAIL'}")
    return strict_exit_code(args.strict, assessment)


if __name__ == "__main__":
    raise SystemExit(main())
