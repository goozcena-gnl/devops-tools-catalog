# Known hard URL review — 2026-09-18

This review covers only the seven `manual-verification-required` and two
`http-error` URLs recorded in the committed strict-link report before this
work. Network observations are triage evidence; each canonical decision below
also requires current, field-appropriate primary-source evidence.

## Decision table

| Record | Field | Old URL | Fresh observation | Primary evidence | Decision | New URL/value | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `gremlin` | `repository_url` | `https://github.com/gremlin-io/gremlin` | Unauthenticated audit: GitHub API HTTP 429 at `2026-09-18T10:31:56+02:00`; authenticated API: HTTP 404. | [Gremlin installation documentation](https://www.gremlin.com/docs/getting-started-installing-gremlin) describes the vendor agent and service; the current [Gremlin GitHub organization](https://github.com/gremlin) publishes SDKs, agents, examples, integrations, and tooling, but no exact parent-product source repository. | REMOVE | field absent | high |
| `hoji-ai` | `repository_url` | `https://github.com/hoji-ai/hoji` | Unauthenticated audit: GitHub API HTTP 429 at `2026-09-18T10:32:04+02:00`; authenticated API: HTTP 404. | The current [Hoji application](https://app.hoji.ai/) and [Hoji documentation](https://app.hoji.ai/docs) establish the product, but do not identify a public successor repository or state that the selected repository was retired. | INCONCLUSIVE | retain old URL | medium |
| `komodor` | `repository_url` | `https://github.com/komodorio/komodor` | Unauthenticated audit: GitHub API HTTP 403 rate-limit response at `2026-09-18T10:32:19+02:00`; authenticated API: HTTP 404. | Komodor's verified [GitHub organization](https://github.com/komodorio) links the vendor application and publishes charts, integrations, providers, CLIs, and other components, but no exact repository for the commercial parent product. | REMOVE | field absent | high |
| `devops-projects` | `repository_url` | `https://github.com/ophircloud/DevOps-Projects` | Unauthenticated audit: GitHub API HTTP 429 at `2026-09-18T10:33:01+02:00`; authenticated API: HTTP 451. | GitHub's official [DMCA notice](https://github.com/github/dmca/blob/master/2026/02/2026-02-24-devops-projects.md) names this exact repository as the restricted repository. No owner-controlled transfer or successor was found. | RETAIN | retain old URL | high |
| `certmate` | `repository_url` | `https://github.com/usual2970/certmate` | Unauthenticated audit: GitHub API HTTP 429 at `2026-09-18T10:33:49+02:00`; authenticated API: HTTP 404. | The existing [CertMate official site](https://www.certmate.org/) identifies [fabriziosalmi/certmate](https://github.com/fabriziosalmi/certmate), and the [official getting-started guide](https://www.certmate.org/docs/getting-started.html) gives that exact clone URL. The similarly named `usual2970` project is Certimate, a different identity. | REPLACE | `https://github.com/fabriziosalmi/certmate` | high |
| `soos-dast` | `official_url` | `https://hub.docker.com/r/soosio/dast` | HEAD and bounded GET: HTTP 404 at `2026-09-18T10:34:04+02:00`. | SOOS-owned indexed material identifies the exact product at [the DAST product page](https://soos.io/products/dast) and [DAST getting-started documentation](https://kb.soos.io/getting-started-with-dast), but fresh HEAD and bounded GET requests to both candidates return HTTP 410, and the documentation's linked `soos-io/soos-dast` repository returns HTTP 404. No live durable successor is proven. | INCONCLUSIVE | retain old URL | medium |
| `kubeflame` | `official_url` | `https://kubeflame.github.io` | HEAD and bounded GET: HTTP 404 at `2026-09-18T10:34:09+02:00`. | The owner-controlled [KubeFlame organization](https://github.com/kubeflame), [site repository](https://github.com/kubeflame/kubeflame.github.io), and [Lutho repository](https://github.com/kubeflame/lutho) still designate the selected Pages URL. They do not document a move, archive, or exact replacement for the catalogue identity. | INCONCLUSIVE | retain old URL | medium |
| `fortify-static-code-analyzer` | `official_url` | `https://www.opentext.com/products/static-application-security-testing` | HEAD: HTTP 444 at `2026-09-18T10:34:50+02:00`. | The selected live [OpenText Fortify SAST page](https://www.opentext.com/products/static-application-security-testing) remains the exact vendor product root, supported by current [Fortify Static Code Analyzer documentation](https://www.microfocus.com/documentation/fortify-static-code/). | RETAIN | retain old URL | high |
| `yotascale` | `official_url` | `https://www.yotascale.com` | HEAD and bounded GET: HTTP 404 at `2026-09-18T10:34:57+02:00`. | Current owner-controlled [Yotascale leadership](https://www.yotascale.com/leadership), [Yota Copilot](https://www.yotascale.com/product/yota-copilot), and [terms](https://www.yotascale.com/terms-of-use) pages establish the domain and product continuity. No IBM or Apptio source maps the product one-to-one to a replacement URL. | RETAIN | retain old URL | high |

## Baseline reconciliation

The baseline contained nine reviewed blockers. Three entries are removed only
because the corresponding old URLs are no longer canonical after one
evidence-supported replacement and two evidence-supported optional-field
removals. Six entries remain because their canonical values remain selected
and their access behavior is still either a known blocker or unresolved. No
entry is added, and no entry is removed merely because a fresh audit produced
a non-blocking transient classification.

## Scope and unresolved boundaries

Only the nine selected URL fields were reviewed. Three changed and six did
not. No lifecycle, status, license, maturity, category, summary, role, or other
URL field was changed. Hoji still lacks owner-controlled repository migration
or retirement evidence. SOOS still lacks a live, durable exact replacement.
KubeFlame's owner-controlled repositories continue to
name the unavailable Pages URL but do not establish a field-appropriate
successor. The DevOps Projects URL remains the exact legally restricted
repository. Fortify remains a correct vendor URL with automated-access
behavior. Yotascale lacks an authoritative one-to-one migration destination.
