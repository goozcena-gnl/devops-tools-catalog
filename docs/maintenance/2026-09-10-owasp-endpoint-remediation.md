# OWASP project endpoint remediation

Reviewed on 2026-09-10 against post-Wave-4 main
`62a6cd841f0db0eea9b5ef93ef6b878f50fa9db8` (1,423 records, version 0.4.0).

## Direct diagnosis

Two serial curl rounds followed redirects with certificate verification enabled.
All three old URLs returned HEAD 404 on the first attempt. Ranged GET returned
206, but complete GET returned 404 and the response contained the site's
not-found content. A partial-response status alone therefore did not establish
project-page recovery. The repository checker also observed HEAD 404 and GET
fallback 404 for DockSec and Dependency-Check; one Amass fallback returned 206.
These are stale route observations, not project retirement or TLS failures.

| Project | Historical active URL | Current official URL |
|---|---|---|
| DockSec | https://owasp.org/DockSec/ | https://owasp.org/projects/docksec |
| Amass | https://owasp.org/www-project-amass/ | https://owasp.org/projects/amass |
| Dependency-Check | https://owasp.org/www-project-dependency-check | https://owasp.org/projects/dependency-check |

Each current official URL returned HEAD 200 and ranged GET 200 in both serial
rounds, on the first attempt without TLS errors. Complete responses contain the
correct project heading and links to the corresponding canonical repository.
The pages reside on the established OWASP foundation domain, rather than relying
on branding or an unverified relationship to another domain.

## Independent project decisions

DockSec's repository is `OWASP/DockSec`, neither archived nor disabled, with MIT
licence text and a README identifying it as an OWASP Lab Project. Its homepage
still references the old route. The proposed `/www-project-docksec/` alternative
also returned 404 on repeated live requests, although web retrieval exposed older
content. The healthy current `/projects/docksec` route is selected instead.

Amass's `owasp-amass/amass` repository is neither archived nor disabled and has
2026 activity. Its actual licence text identifies Apache 2.0 despite GitHub's
generic `Other` metadata. The community-domain page was available, but the same
project is available directly at `owasp.org/projects/amass`; the primary-domain
endpoint avoids a separate ownership inference. No licence change is required.

Dependency-Check did not recover: both slash variants returned full GET 404.
Its current OWASP project page links to `dependency-check/DependencyCheck`, whose
repository is neither archived nor disabled and has Apache-2.0 licence text.
The existing project-maintained GitHub Pages documentation remains healthy and
unchanged. A healthy official project page makes a documentation fallback
unnecessary.

## Scope and provenance

Only `official_url`, endpoint verification date and source evidence change for
these three records. Repositories, documentation URLs, licences, lifecycle,
operational guidance and cardinality are preserved. Old URLs remain in sources;
Dependency-Check also retains the slash form found in its historical inputs.
No aliases are added. Migration and Wave 2/Wave 4 ledgers remain byte-for-byte
unchanged. The Wave 4 metadata test now explicitly checks both DockSec's original
ledger URL and its repaired current URL, preserving the historical assertion.

The checker, blocker baseline, taxonomy, schema, version and release history are
unchanged. This maintenance does not revise any other Wave 4 decision.
