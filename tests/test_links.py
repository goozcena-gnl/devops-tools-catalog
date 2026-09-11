import dataclasses
import http.server
import json
import ssl
import threading
import urllib.error
from collections import Counter
from datetime import UTC, datetime, timedelta
from pathlib import Path

import pytest

import scripts.check_links as check_links
from scripts.check_links import (
    CACHE_VERSION,
    BaselineItem,
    DomainRateLimiter,
    HttpOutcome,
    LinkResult,
    TrackingRedirectHandler,
    UrlContext,
    _http_request,
    assess_strict_results,
    catalogue_url_contexts,
    check_url,
    classify_repository_archival,
    classify_status,
    report_payload,
    repository_coordinates,
    run_audit,
    strict_exit_code,
)


def run_local_http_handler(handler: type[http.server.BaseHTTPRequestHandler]):
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def result(url: str, classification: str, **kwargs: object) -> LinkResult:
    return LinkResult(
        url=url,
        classification=classification,
        status=kwargs.get("status", 404),
        final_url=kwargs.get("final_url", url),
        redirect_codes=(),
        attempts=1,
        error=None,
        checked_at="2026-08-24T00:00:00+00:00",
        repository_archived=kwargs.get("repository_archived"),
        repository_archived_expected=kwargs.get("repository_archived_expected"),
        request_method=kwargs.get("request_method", "HEAD"),
        head_status=kwargs.get("head_status"),
        get_fallback=bool(kwargs.get("get_fallback", False)),
    )


def baseline_item(url: str, classification: str) -> BaselineItem:
    return BaselineItem(url, classification, "reviewed", "issue-2", "2026-08-24")


def archived_result(url: str, expected: bool) -> LinkResult:
    return result(
        url,
        (
            "repository-archived-expected"
            if expected
            else "repository-archived-unexpected"
        ),
        status=200,
        repository_archived=True,
        repository_archived_expected=expected,
        request_method="GITHUB_API",
    )


def run_with_cached_result(
    monkeypatch,
    tmp_path: Path,
    *,
    cached: LinkResult,
    current_expected: bool,
    check_archived: bool,
    fresh: LinkResult,
) -> tuple[LinkResult, list[dict[str, object]]]:
    context = UrlContext(("tool",), current_expected)
    calls: list[dict[str, object]] = []

    monkeypatch.setattr(
        check_links, "catalogue_url_contexts", lambda root: {cached.url: context}
    )
    monkeypatch.setattr(
        check_links, "load_cache", lambda path, max_age: {cached.url: cached}
    )
    monkeypatch.setattr(check_links, "write_if_changed", lambda path, content: False)

    def probe(url: str, **kwargs: object) -> LinkResult:
        calls.append({"url": url, **kwargs})
        return fresh

    monkeypatch.setattr(check_links, "check_url", probe)
    checked = run_audit(
        tmp_path,
        workers=1,
        retries=0,
        timeout=1,
        domain_interval=0,
        cache_path=tmp_path / "cache.json",
        cache_hours=24,
        check_archived=check_archived,
    )
    return checked[0], calls


def test_link_status_classification_is_non_binary() -> None:
    assert classify_status(204, []) == "valid"
    assert classify_status(200, [301]) == "permanent-redirect"
    assert classify_status(200, [302]) == "valid-redirect"
    assert classify_status(401, []) == "authentication-required"
    assert classify_status(403, []) == "restricted-or-bot-blocked"
    assert classify_status(429, []) == "rate-limited"
    assert classify_status(404, []) == "manual-verification-required"


def test_github_repository_coordinates_ignore_organization_pages() -> None:
    assert repository_coordinates("https://github.com/org/repository") == (
        "org",
        "repository",
    )
    assert repository_coordinates("https://github.com/org") is None
    assert repository_coordinates("https://github.com/features/actions") is None


def test_head_404_is_recovered_by_conservative_ranged_get(monkeypatch) -> None:
    outcomes = iter(
        [
            HttpOutcome("manual-verification-required", 404, None, (), "HTTP 404"),
            HttpOutcome("valid", 200, "https://example.test", (), None),
        ]
    )
    monkeypatch.setattr(
        check_links, "_http_request", lambda *args, **kwargs: next(outcomes)
    )

    checked = check_url(
        "https://example.test",
        limiter=DomainRateLimiter(0),
        retries=0,
        timeout=1,
        check_archived=False,
    )

    assert checked.classification == "valid"
    assert checked.head_status == 404
    assert checked.status == 200
    assert checked.request_method == "GET"
    assert checked.get_fallback is True


def test_head_and_get_404_remains_manual(monkeypatch) -> None:
    outcomes = iter(
        [
            HttpOutcome("manual-verification-required", 404, None, (), "HEAD 404"),
            HttpOutcome("manual-verification-required", 404, None, (), "GET 404"),
        ]
    )
    monkeypatch.setattr(
        check_links, "_http_request", lambda *args, **kwargs: next(outcomes)
    )

    checked = check_url(
        "https://example.test/missing",
        limiter=DomainRateLimiter(0),
        retries=0,
        timeout=1,
        check_archived=False,
    )

    assert checked.classification == "manual-verification-required"
    assert checked.head_status == checked.status == 404
    assert checked.get_fallback is True


def test_http_request_preserves_cookie_across_same_url_redirect() -> None:
    cookies: list[str | None] = []

    class CookieChallenge(http.server.BaseHTTPRequestHandler):
        def respond(self) -> None:
            cookie = self.headers.get("Cookie")
            cookies.append(cookie)
            if cookie == "milvus_challenge=accepted":
                self.send_response(200)
            else:
                self.send_response(302)
                self.send_header("Location", "/")
                self.send_header(
                    "Set-Cookie",
                    "milvus_challenge=accepted; Path=/; HttpOnly; SameSite=Lax",
                )
            self.end_headers()

        do_GET = respond
        do_HEAD = respond

        def log_message(self, format: str, *args: object) -> None:
            pass

    server, thread = run_local_http_handler(CookieChallenge)
    try:
        url = f"http://127.0.0.1:{server.server_port}/"
        outcome = _http_request(url, method="HEAD", timeout=2)
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)

    assert outcome.classification == "valid-redirect"
    assert outcome.status == 200
    assert outcome.redirect_codes == (302,)
    assert cookies == [None, "milvus_challenge=accepted"]
    assert CACHE_VERSION == 4


def test_http_request_builds_cookie_aware_bounded_opener(monkeypatch) -> None:
    handlers: list[object] = []

    class Response:
        status = 200

        def __enter__(self):
            return self

        def __exit__(self, *args: object) -> None:
            pass

        def geturl(self) -> str:
            return "https://example.test/"

    class Opener:
        def open(self, request: object, timeout: float) -> Response:
            return Response()

    def build_opener(*configured_handlers: object) -> Opener:
        handlers.extend(configured_handlers)
        return Opener()

    monkeypatch.setattr(check_links.urllib.request, "build_opener", build_opener)
    outcome = _http_request("https://example.test/", method="HEAD", timeout=2)

    redirect_handler = next(
        handler for handler in handlers if isinstance(handler, TrackingRedirectHandler)
    )
    assert any(
        isinstance(handler, check_links.urllib.request.HTTPCookieProcessor)
        for handler in handlers
    )
    assert redirect_handler.max_redirections == 10
    assert outcome.classification == "valid"


def test_cookie_support_does_not_accept_a_genuine_redirect_loop() -> None:
    request_count = 0

    class RedirectLoop(http.server.BaseHTTPRequestHandler):
        def respond(self) -> None:
            nonlocal request_count
            request_count += 1
            self.send_response(302)
            self.send_header("Location", "/")
            self.send_header("Set-Cookie", "challenge=never-satisfied; Path=/")
            self.end_headers()

        do_GET = respond
        do_HEAD = respond

        def log_message(self, format: str, *args: object) -> None:
            pass

    server, thread = run_local_http_handler(RedirectLoop)
    try:
        url = f"http://127.0.0.1:{server.server_port}/"
        outcome = _http_request(url, method="HEAD", timeout=2)
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)

    assert outcome.classification == "http-error"
    assert outcome.status == 302
    assert outcome.error and "redirect" in outcome.error.lower()
    assert 1 < request_count <= TrackingRedirectHandler.max_redirections


def test_tls_failure_remains_blocking_without_insecure_fallback(monkeypatch) -> None:
    methods: list[str] = []

    def tls_failure(url: str, *, method: str, timeout: float) -> HttpOutcome:
        methods.append(method)
        return HttpOutcome("tls-failure", None, None, (), "certificate failure")

    monkeypatch.setattr(check_links, "_http_request", tls_failure)
    checked = check_url(
        "https://invalid.test",
        limiter=DomainRateLimiter(0),
        retries=2,
        timeout=1,
        check_archived=False,
    )

    assert methods == ["HEAD"]
    assert checked.classification == "tls-failure"
    assert checked.get_fallback is False
    assert strict_exit_code(True, assess_strict_results([checked], {})) == 1


def test_archive_classification_requires_explicit_expectation() -> None:
    assert classify_repository_archival(True, True) == "repository-archived-expected"
    assert classify_repository_archival(True, False) == "repository-archived-unexpected"
    assert classify_repository_archival(False, False) == "valid"


def test_repository_archive_expectation_comes_only_from_repository_records(
    tmp_path: Path,
) -> None:
    tools_dir = tmp_path / "data" / "tools"
    tools_dir.mkdir(parents=True)
    (tools_dir / "test.yaml").write_text(
        """- id: expected
  official_url: https://product.test
  repository_url: https://github.com/org/expected
  repository_archived: true
- id: active-product
  status: active
  official_url: https://active.test
  repository_url: https://github.com/org/active-archived-code
  repository_archived: true
- id: missing-metadata
  repository_url: https://github.com/org/unexpected
- id: shared-with-mixed-metadata
  repository_url: https://github.com/org/shared
  repository_archived: true
- id: shared-without-metadata
  repository_url: https://github.com/org/shared
""",
        encoding="utf-8",
    )

    contexts = catalogue_url_contexts(tmp_path)

    assert contexts["https://github.com/org/expected"].repository_archived_expected
    assert contexts[
        "https://github.com/org/active-archived-code"
    ].repository_archived_expected
    assert not contexts[
        "https://github.com/org/unexpected"
    ].repository_archived_expected
    assert not contexts["https://github.com/org/shared"].repository_archived_expected
    assert not contexts["https://product.test"].repository_archived_expected


def test_cache_reprobes_when_expected_archive_metadata_is_removed(
    monkeypatch, tmp_path: Path
) -> None:
    url = "https://github.com/org/repository"
    fresh = archived_result(url, False)

    checked, calls = run_with_cached_result(
        monkeypatch,
        tmp_path,
        cached=archived_result(url, True),
        current_expected=False,
        check_archived=True,
        fresh=fresh,
    )

    assert checked is fresh
    assert len(calls) == 1
    assert calls[0]["repository_archived_expected"] is False


def test_cache_reprobes_when_unexpected_archive_metadata_is_added(
    monkeypatch, tmp_path: Path
) -> None:
    url = "https://github.com/org/repository"
    fresh = archived_result(url, True)

    checked, calls = run_with_cached_result(
        monkeypatch,
        tmp_path,
        cached=archived_result(url, False),
        current_expected=True,
        check_archived=True,
        fresh=fresh,
    )

    assert checked is fresh
    assert len(calls) == 1
    assert calls[0]["repository_archived_expected"] is True


def test_archive_enabled_run_rejects_ordinary_head_cache(
    monkeypatch, tmp_path: Path
) -> None:
    url = "https://github.com/org/repository"
    cached = result(url, "valid", status=200, request_method="HEAD")
    fresh = archived_result(url, False)

    checked, calls = run_with_cached_result(
        monkeypatch,
        tmp_path,
        cached=cached,
        current_expected=False,
        check_archived=True,
        fresh=fresh,
    )

    assert checked is fresh
    assert len(calls) == 1
    assert calls[0]["check_archived"] is True


def test_archive_disabled_run_rejects_github_api_cache(
    monkeypatch, tmp_path: Path
) -> None:
    url = "https://github.com/org/repository"
    fresh = result(url, "valid", status=200, request_method="HEAD")

    checked, calls = run_with_cached_result(
        monkeypatch,
        tmp_path,
        cached=archived_result(url, False),
        current_expected=False,
        check_archived=False,
        fresh=fresh,
    )

    assert checked is fresh
    assert len(calls) == 1
    assert calls[0]["check_archived"] is False


def test_archive_cache_is_reused_for_unchanged_expected_context(
    monkeypatch, tmp_path: Path
) -> None:
    url = "https://github.com/org/repository"
    cached = archived_result(url, True)

    checked, calls = run_with_cached_result(
        monkeypatch,
        tmp_path,
        cached=cached,
        current_expected=True,
        check_archived=True,
        fresh=result(url, "http-error"),
    )

    assert checked is cached
    assert calls == []


def test_archive_cache_is_reused_for_unchanged_unexpected_context(
    monkeypatch, tmp_path: Path
) -> None:
    url = "https://github.com/org/repository"
    cached = archived_result(url, False)

    checked, calls = run_with_cached_result(
        monkeypatch,
        tmp_path,
        cached=cached,
        current_expected=False,
        check_archived=True,
        fresh=result(url, "http-error"),
    )

    assert checked is cached
    assert calls == []


def test_archive_api_fallback_is_not_authoritative_on_next_checked_run(
    monkeypatch, tmp_path: Path
) -> None:
    url = "https://github.com/org/repository"
    cached_fallback = result(
        url,
        "valid",
        status=200,
        repository_archived_expected=True,
        request_method="GET",
    )
    fresh = archived_result(url, True)

    checked, calls = run_with_cached_result(
        monkeypatch,
        tmp_path,
        cached=cached_fallback,
        current_expected=True,
        check_archived=True,
        fresh=fresh,
    )

    assert checked is fresh
    assert len(calls) == 1
    assert calls[0]["check_archived"] is True


def test_non_github_cache_reuse_ignores_archive_mode(
    monkeypatch, tmp_path: Path
) -> None:
    cached = result("https://example.test", "valid", status=200)

    checked, calls = run_with_cached_result(
        monkeypatch,
        tmp_path,
        cached=cached,
        current_expected=False,
        check_archived=True,
        fresh=result(cached.url, "http-error"),
    )

    assert checked is cached
    assert calls == []


def test_strict_assessment_separates_known_new_and_changed_blockers() -> None:
    known = result("https://known.test", "manual-verification-required")
    new = result("https://new.test", "http-error")
    changed = result("https://changed.test", "tls-failure")
    expected_archive = result(
        "https://github.com/org/expected",
        "repository-archived-expected",
        repository_archived=True,
        repository_archived_expected=True,
    )
    baseline = {
        known.url: baseline_item(known.url, known.classification),
        changed.url: baseline_item(changed.url, "http-error"),
        "https://resolved.test": baseline_item(
            "https://resolved.test", "manual-verification-required"
        ),
    }

    assessment = assess_strict_results(
        [known, new, changed, expected_archive], baseline
    )

    assert [item.url for item in assessment.blocking_known] == [known.url]
    assert [item.url for item in assessment.blocking_new] == [
        changed.url,
        new.url,
    ]
    assert assessment.baseline_changed[0][0].url == changed.url
    assert assessment.baseline_resolved[0].url == "https://resolved.test"
    assert assessment.passed is False
    assert strict_exit_code(True, assessment) == 1


def test_known_blocker_and_clean_run_have_zero_strict_exit() -> None:
    known = result("https://known.test", "manual-verification-required")
    baseline = {known.url: baseline_item(known.url, known.classification)}

    known_assessment = assess_strict_results([known], baseline)
    clean_assessment = assess_strict_results(
        [result("https://valid.test", "valid", status=200)], {}
    )

    assert strict_exit_code(True, known_assessment) == 0
    assert strict_exit_code(True, clean_assessment) == 0
    assert strict_exit_code(False, assess_strict_results([known], {})) == 0


def test_machine_report_exposes_strict_and_recovery_fields() -> None:
    recovered = result(
        "https://recovered.test",
        "valid",
        status=200,
        head_status=404,
        get_fallback=True,
    )
    blocker = result("https://new.test", "manual-verification-required")
    assessment = assess_strict_results([recovered, blocker], {})

    payload = report_payload([recovered, blocker], {}, assessment)

    assert payload["strict"] == {
        "blocking_new": 1,
        "blocking_known": 0,
        "strict_result": "FAIL",
        "baseline_changed": [],
        "baseline_resolved": [],
    }
    by_url = {item["url"]: item for item in payload["results"]}
    assert by_url[recovered.url]["head_status"] == 404
    assert by_url[recovered.url]["get_fallback"] is True
    assert by_url[blocker.url]["strict_status"] == "blocking-new"


def test_committed_link_report_counts_are_self_consistent() -> None:
    report_path = Path(__file__).resolve().parents[1] / "reports" / "link-report.json"
    payload = json.loads(report_path.read_text(encoding="utf-8"))
    results = payload["results"]

    assert payload["summary"] == dict(
        sorted(Counter(item["classification"] for item in results).items())
    )
    strict_counts = Counter(item["strict_status"] for item in results)
    assert payload["strict"]["blocking_new"] == strict_counts["blocking-new"]
    assert payload["strict"]["blocking_known"] == strict_counts["blocking-known"]
    assert payload["strict"]["strict_result"] == (
        "FAIL" if strict_counts["blocking-new"] else "PASS"
    )


@pytest.mark.parametrize("wrapped", [False, True], ids=["direct", "wrapped"])
@pytest.mark.parametrize("recovers", [False, True], ids=["exhausted", "recovers"])
def test_tls_eof_uses_bounded_retries(monkeypatch, wrapped, recovers) -> None:
    calls = []
    sleeps = []

    class Response:
        status = 200

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def geturl(self):
            return "https://example.test/"

    class Opener:
        def open(self, request, timeout):
            calls.append(request.get_method())
            if recovers and len(calls) == 2:
                return Response()
            error = ssl.SSLEOFError(ssl.SSL_ERROR_EOF, "unexpected EOF")
            raise urllib.error.URLError(error) if wrapped else error

    monkeypatch.setattr(
        check_links.urllib.request, "build_opener", lambda *args: Opener()
    )
    monkeypatch.setattr(check_links.time, "sleep", sleeps.append)
    checked = check_url(
        "https://example.test/",
        limiter=DomainRateLimiter(0),
        retries=2,
        timeout=1,
        check_archived=False,
    )
    assert checked.attempts == (2 if recovers else 3)
    assert calls == ["HEAD"] * checked.attempts
    assert sleeps == ([0.5] if recovers else [0.5, 1.0])
    assert checked.classification == ("valid" if recovers else "tls-failure")
    assert strict_exit_code(True, assess_strict_results([checked], {})) == (
        0 if recovers else 1
    )
    assert not checked.get_fallback


@pytest.mark.parametrize("wrapped", [False, True], ids=["direct", "wrapped"])
@pytest.mark.parametrize(
    "error",
    [
        ssl.SSLCertVerificationError(1, "certificate verify failed: hostname mismatch"),
        ssl.SSLCertVerificationError(
            1, "certificate verify failed: expired certificate"
        ),
        ssl.SSLCertVerificationError(1, "certificate verify failed: untrusted chain"),
        ssl.SSLError(1, "unknown TLS failure"),
    ],
)
def test_certificate_and_unknown_tls_errors_fail_immediately(
    monkeypatch, wrapped, error
) -> None:
    calls = []

    class Opener:
        def open(self, request, timeout):
            calls.append((request.full_url, request.get_method()))
            raise urllib.error.URLError(error) if wrapped else error

    def build_opener(*handlers):
        # No custom HTTPS handler or SSL context bypasses urllib's verified defaults.
        assert not any(
            isinstance(h, check_links.urllib.request.HTTPSHandler) for h in handlers
        )
        return Opener()

    monkeypatch.setattr(check_links.urllib.request, "build_opener", build_opener)
    monkeypatch.setattr(
        check_links.time, "sleep", lambda _: pytest.fail("security failure retried")
    )
    checked = check_url(
        "https://invalid.test/",
        limiter=DomainRateLimiter(0),
        retries=2,
        timeout=1,
        check_archived=False,
    )
    assert calls == [("https://invalid.test/", "HEAD")]
    assert checked.attempts == 1
    assert checked.classification == "tls-failure"
    assert strict_exit_code(True, assess_strict_results([checked], {})) == 1


def test_explicit_openssl_eof_reason_without_subclass_is_retryable() -> None:
    error = ssl.SSLError(1, "transport interrupted")
    error.reason = "UNEXPECTED_EOF_WHILE_READING"
    assert check_links._tls_outcome(error).retryable
    certificate = ssl.SSLCertVerificationError(1, "certificate failed")
    certificate.reason = "UNEXPECTED_EOF_WHILE_READING"
    assert not check_links._tls_outcome(certificate).retryable
    # A message alone is not sufficient evidence of transport EOF.
    assert not check_links._tls_outcome(
        ssl.SSLError(1, "UNEXPECTED_EOF_WHILE_READING")
    ).retryable


@pytest.mark.parametrize(
    "head,partial,ordinary,redirect",
    [
        (404, 206, 404, None),
        (404, 206, 200, None),
        (405, 206, 200, None),
        (501, 206, 200, None),
        (404, 200, None, None),
        (404, 404, None, None),
        (404, 206, 200, 301),
        (405, 206, 200, 302),
        (200, None, None, None),
        (404, 206, 206, None),
    ],
)
def test_get_fallback_confirms_only_partial_responses(
    head, partial, ordinary, redirect
) -> None:
    requests = []

    class Handler(http.server.BaseHTTPRequestHandler):
        def respond(self):
            ranged = self.headers.get("Range")
            requests.append((self.command, ranged, self.path))
            if self.command == "HEAD":
                status = head
            elif ranged:
                status = partial
            elif redirect and self.path == "/":
                status = redirect
                self.send_response(status)
                self.send_header("Location", "/confirmed")
                self.end_headers()
                return
            else:
                status = ordinary
            self.send_response(status)
            self.end_headers()

        do_GET = respond
        do_HEAD = respond

        def log_message(self, format, *args):
            pass

    server, thread = run_local_http_handler(Handler)
    try:
        url = f"http://127.0.0.1:{server.server_port}/"
        checked = check_url(
            url,
            limiter=DomainRateLimiter(0),
            retries=0,
            timeout=2,
            check_archived=False,
        )
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
    expected = [("HEAD", None, "/")]
    if partial is not None:
        expected.append(("GET", "bytes=0-1023", "/"))
    if partial == 206:
        expected.append(("GET", None, "/"))
    if redirect:
        expected.append(("GET", None, "/confirmed"))
    assert requests == expected
    status = ordinary if partial == 206 else partial if partial is not None else head
    assert checked.status == status
    assert checked.head_status == head
    assert checked.classification == classify_status(
        status, [redirect] if redirect else []
    )
    assert checked.final_url == url + ("confirmed" if redirect else "")
    assert checked.redirect_codes == ((redirect,) if redirect else ())
    assert checked.get_confirmation == (partial == 206)
    assert checked.get_fallback == (partial is not None)
    assert checked.attempts == 1  # One attempt can contain HEAD and both GET probes.
    payload = report_payload([checked], {}, assess_strict_results([checked], {}))
    assert payload["results"][0]["get_confirmation"] == (partial == 206)
    if ordinary == 206:
        # A successful partial status is retained, never relabeled as a full 200.
        assert checked.classification == "valid"
        assert payload["results"][0]["status"] == 206
    markdown = check_links.markdown_report(
        [checked], {}, assess_strict_results([checked], {})
    )
    assert "| Final GET status | Ordinary GET confirmation |" in markdown
    if partial is not None:
        assert (
            f"| {head} | {status} | {'yes' if partial == 206 else 'no'} |" in markdown
        )
    assert (checked.error is not None) == (status == 404)


def test_confirmation_get_closes_response_without_reading_body(monkeypatch) -> None:
    closed = []

    class Response:
        status = 200

        def __enter__(self):
            return self

        def __exit__(self, *args):
            closed.append(True)

        def geturl(self):
            return "https://example.test/large"

        def read(self, *args):
            pytest.fail("confirmation must not download the body")

    class Opener:
        def open(self, request, timeout):
            assert request.get_method() == "GET"
            assert request.get_header("Range") is None
            return Response()

    monkeypatch.setattr(
        check_links.urllib.request, "build_opener", lambda *args: Opener()
    )
    assert (
        _http_request(
            "https://example.test/large", method="GET", timeout=1, ranged=False
        ).status
        == 200
    )
    assert closed == [True]


def test_cache_version_three_is_ignored_and_four_round_trips(tmp_path) -> None:
    current = dataclasses.replace(
        result("https://example.test/", "valid", status=200),
        checked_at=datetime.now(UTC).isoformat(),
        get_confirmation=True,
    )
    item = dataclasses.asdict(current)
    path = tmp_path / "cache.json"
    item["checker_version"] = 3
    path.write_text(json.dumps({current.url: item}), encoding="utf-8")
    assert check_links.load_cache(path, timedelta(hours=1)) == {}
    item["checker_version"] = 4
    path.write_text(json.dumps({current.url: item}), encoding="utf-8")
    assert check_links.load_cache(path, timedelta(hours=1)) == {current.url: current}


@pytest.mark.parametrize(
    "classification",
    [
        "rate-limited",
        "transient-failure",
        "timeout-inconclusive",
        "dns-inconclusive",
        "network-inconclusive",
    ],
)
def test_existing_retry_classifications_keep_bounded_backoff(
    monkeypatch, classification
) -> None:
    calls = []
    sleeps = []

    def probe(*args, **kwargs):
        calls.append(kwargs["method"])
        return HttpOutcome(classification, None, None, (), "injected")

    monkeypatch.setattr(check_links, "_http_request", probe)
    monkeypatch.setattr(check_links.time, "sleep", sleeps.append)
    checked = check_url(
        "https://example.test/",
        limiter=DomainRateLimiter(0),
        retries=2,
        timeout=1,
        check_archived=False,
    )
    assert calls == ["HEAD"] * 3
    assert sleeps == [0.5, 1.0]
    assert checked.attempts == 3
    assert checked.classification == classification


@pytest.mark.parametrize(
    "certificate", [False, True], ids=["EOF-recovery", "certificate-stop"]
)
def test_confirmation_tls_failure_preserves_cycle_metadata(
    monkeypatch, certificate
) -> None:
    calls = []
    sleeps = []

    class Response:
        def __init__(self, status):
            self.status = status

        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def geturl(self):
            return (
                "https://example.test/recovered"
                if self.status == 200
                else "https://example.test/probe"
            )

    class Opener:
        def __init__(self, handler):
            self.handler = handler

        def open(self, request, timeout):
            calls.append((request.get_method(), request.get_header("Range")))
            if len(calls) == 1:
                return Response(404)
            if len(calls) == 2:
                self.handler.codes.append(301)
                return Response(206)
            if len(calls) == 3:
                error = (
                    ssl.SSLCertVerificationError(1, "certificate rejected")
                    if certificate
                    else ssl.SSLEOFError(ssl.SSL_ERROR_EOF, "EOF")
                )
                raise urllib.error.URLError(error)
            return Response(200)

    monkeypatch.setattr(
        check_links.urllib.request,
        "build_opener",
        lambda handler, *args: Opener(handler),
    )
    monkeypatch.setattr(check_links.time, "sleep", sleeps.append)
    checked = check_url(
        "https://example.test/",
        limiter=DomainRateLimiter(0),
        retries=2,
        timeout=1,
        check_archived=False,
    )
    expected = [("HEAD", None), ("GET", "bytes=0-1023"), ("GET", None)]
    if certificate:
        assert checked.attempts == 1
        assert checked.classification == "tls-failure"
        assert checked.head_status == 404
        assert checked.request_method == "GET"
        assert checked.get_fallback and checked.get_confirmation
        assert checked.status is None and checked.final_url is None
        assert checked.error is not None
        assert strict_exit_code(True, assess_strict_results([checked], {})) == 1
        assert sleeps == []
    else:
        expected.append(("HEAD", None))
        assert checked.attempts == 2
        assert checked.classification == "valid"
        assert checked.head_status == checked.status == 200
        assert checked.request_method == "HEAD"
        assert not checked.get_fallback and not checked.get_confirmation
        assert checked.final_url == "https://example.test/recovered"
        assert checked.error is None
        assert sleeps == [0.5]
    assert checked.redirect_codes == ()  # Earlier ranged-probe redirects do not leak.
    assert calls == expected
