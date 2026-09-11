# Link checker transport hardening — 2026-09-11

## Observed incidents and previous behavior

During September Wave 4 validation, Headlamp, kOps, MetalLB, Conftest and
Open Notebook failed together with TLS EOF errors. Subsequent direct checks
and independent conservative audits recovered. The original cause was not
established; these observations do not prove a server or client root cause.

The checker classified all direct or URL-error-wrapped SSL errors as blocking
`tls-failure`. Its retry set covered rate limits, transient HTTP failures,
timeouts, DNS and network inconclusive results, but excluded TLS failures.
The existing certificate-failure regression expected one HEAD even with two retries.

The OWASP incident independently exposed HEAD 404, ranged GET 206, then ordinary
GET 404/not-found content. Previously HEAD 404/405/501 triggered GET with
`Range: bytes=0-1023`, and any successful 2xx (including 206) could end fallback
as valid. PR #56 repaired the catalogue endpoints; this change hardens the checker.

## New behavior and security boundaries

Internal `HttpOutcome.retryable` marks only `ssl.SSLEOFError` or the exact OpenSSL
`reason` code `UNEXPECTED_EOF_WHILE_READING` as retryable TLS transport failures.
Direct and `URLError.reason`-wrapped SSL exceptions use the same helper.
`SSLCertVerificationError` takes precedence and is never retried. Other SSL
errors remain non-retryable. Exception message substrings are not used.

The existing retry loop and exponential backoff are preserved: two retries
allow three attempts, with 0.5 and 1.0 second backoff. Exhausted EOF errors
remain `tls-failure` and strict blockers. Certificate verification remains enabled
through urllib's normal HTTPS handling. There is no unverified SSL context,
insecure fallback or HTTPS-to-HTTP retry.

Only a ranged fallback returning 206 triggers an ordinary GET without Range.
The confirming response supplies final status, URL, redirects and classification.
A normal 404 stays `manual-verification-required`; 200 can recover the link.
206 itself remains legitimate. The checker opens and closes the response without
reading an arbitrarily large body. Successful HEAD and ranged-200 probes do not
incur a confirmation request.

`get_confirmation` records this final-attempt request path in JSON/cache and the
Markdown fallback table; existing request metadata remains available. Attempts
count bounded probe cycles, each of which may include HEAD and two GET requests.
Cache version increases from 3 to 4: old partial-response successes must be
re-evaluated, not reused under the new semantics.

## Scope and validation

Deterministic fault injection covers direct/wrapped EOF recovery and exhaustion,
certificate errors, unknown SSL failures, exact EOF reason handling and existing
retry classifications. Local HTTP servers cover fallback statuses, partial
confirmation success/failure and redirects. Tests also protect bounded body
handling and rejection of version-3 cache entries with version-4 round trips.

Catalogue data, migration and reconciliation ledgers, aliases, schema, taxonomy,
reviewed blocker baseline and generated catalogue documentation are unchanged.
The catalogue remains 1,423 records and package version remains 0.4.0. No release
artifacts are prepared. Live audit results are recorded in the Draft PR; public
endpoints are not used as deterministic TLS fault injection.

### Completed validation

- Full suite: 428 passed (baseline 398); checker-specific suite: 52 passed.
- Dependency installation, ruff, formatting, generated-doc check, catalogue
  validation and `git diff --check`: PASS.
- Two independent fresh strict archive audits with eight workers, two retries,
  default 12-second timeout and 0.2-second domain interval: 2,407 URLs each,
  nine known blockers, zero new blockers, zero baseline resolutions, PASS.
- Immediate compatible cached audit: identical results, all cache version 4,
  nine known blockers, zero new blockers, PASS.
- Fresh durations: 309.44 and 306.33 seconds; cached: 2.85 seconds. Only one
  ordinary-GET confirmation occurred per fresh pass (PortSwigger documentation,
  HEAD 404, ranged 206, ordinary 200). No comparable pre-change eight-worker
  timing is available; the earlier serial audit is not a controlled comparison.
- The five incident projects were reachable and nonblocking in both fresh runs.
  Seven other URL classifications drifted between nonblocking states (DNS,
  transient HTTP or access restriction); there was no blocking-classification
  drift. No baseline entry was changed or removed.
