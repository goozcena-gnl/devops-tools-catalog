import json
from collections import Counter
from pathlib import Path

import scripts.check_links as check_links
from scripts.check_links import (
    BaselineItem,
    DomainRateLimiter,
    HttpOutcome,
    LinkResult,
    assess_strict_results,
    catalogue_url_contexts,
    check_url,
    classify_repository_archival,
    classify_status,
    report_payload,
    repository_coordinates,
    strict_exit_code,
)


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
        head_status=kwargs.get("head_status"),
        get_fallback=bool(kwargs.get("get_fallback", False)),
    )


def baseline_item(url: str, classification: str) -> BaselineItem:
    return BaselineItem(url, classification, "reviewed", "issue-2", "2026-08-24")


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
