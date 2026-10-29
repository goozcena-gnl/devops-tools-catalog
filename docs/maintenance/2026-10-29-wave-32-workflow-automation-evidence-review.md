# Wave 32 — Workflow Automation — evidence review

**2026-10-29 (Europe/Paris). Status: canonical evidence patch on isolated branch; generated docs and CI unverified. Human merge only.**

## 1. Frozen scope and expected inventory

- Repository: https://github.com/goozcena-gnl/devops-tools-catalog
- Baseline `main`: `3cb9db403092a24e85b8c0a3ac3ae9ac219138eb`; no open PRs at preflight.
- Canonical file: `data/tools/workflow-automation-chatops.yaml`, original Git blob `959714adf2e482d797b23245335fdffece1a197f`; 17 records total, 10 initially needs-review.
- Exactly 5 targeted IDs: `activepieces`, `n8n`, `numaflow`, `rundeck`, `windmill` in **Automation & Workflow**. Other **12 records unchanged byte-for-byte**. Five non-target needs-review remain.
- **5 CLEAR / 0 RETAIN; 58 changed canonical fields**, and no records added or removed. All five `maturity: unknown` values intentionally retained.
- Expected stats (must be regenerated and verified): **1425** total, **844 active** (from 839), **567 needs-review** (from 572), **76 unknown license models** unchanged; license-model totals unchanged (OSS 930, open-core 112, source-available 31, commercial 165).
- No schema, taxonomy, CI, requirements, baseline or historical issue edits. Link baseline blob: `a834e2af711693def40078a55e31dfeb29bee2c7`.

## 2. Official primary evidence inspected

GitHub repository metadata was checked (each repo is not archived); license files were read at frozen repository SHAs; current upstream releases and README documentation were checked. The release numbers are snapshots, not promises of ongoing support.

| ID | Repository | Frozen legal evidence | Main licensing distinction | Upstream frozen SHA | Latest release observed |
|---|---|---|---|---|---|
| `activepieces` | [repo](https://github.com/activepieces/activepieces) | [license](https://github.com/activepieces/activepieces/blob/b2080e13d89b826a408a9f4c5736dbf490e00541/LICENSE) | MIT core + enterprise proprietary | `b2080e13d89b826a408a9f4c5736dbf490e00541` | `0.92.3-hotfix.2` |
| `n8n` | [repo](https://github.com/n8n-io/n8n) | [license](https://github.com/n8n-io/n8n/blob/d93f6130fa3f488c0ccc045fee7c3c507de3c999/LICENSE.md) | SUL + Enterprise | `d93f6130fa3f488c0ccc045fee7c3c507de3c999` | `n8n@2.45.6` |
| `numaflow` | [repo](https://github.com/numaproj/numaflow) | [license](https://github.com/numaproj/numaflow/blob/d2545229b37718b6e39565237922c2cb416ae66f/LICENSE) | Apache-2.0 | `d2545229b37718b6e39565237922c2cb416ae66f` | `v1.9.0` |
| `rundeck` | [repo](https://github.com/rundeck/rundeck) | [license](https://github.com/rundeck/rundeck/blob/9573b48d5658d71e37d8387e0dacee3a0cfe2047/LICENSE) | Apache-2.0 | `9573b48d5658d71e37d8387e0dacee3a0cfe2047` | `v6.3.0` |
| `windmill` | [repo](https://github.com/windmill-labs/windmill) | [license](https://github.com/windmill-labs/windmill/blob/30c544eba8ab71a7f803c4c425849f8b47530ca8/LICENSE) | AGPL core / Apache clients + proprietary | `30c544eba8ab71a7f803c4c425849f8b47530ca8` | `v1.853.1` |

### Activepieces — CLEAR

- Core outside `packages/ee/` and `packages/server/api/src/app/ee` is MIT; enterprise directories use separate commercial license. Primary: https://github.com/activepieces/activepieces/blob/b2080e13d89b826a408a9f4c5736dbf490e00541/LICENSE and https://github.com/activepieces/activepieces/blob/b2080e13d89b826a408a9f4c5736dbf490e00541/packages/ee/LICENSE ; publisher: https://www.activepieces.com/docs/about/license
- Documentation supports cloud, Docker Compose / PostgreSQL / Redis, Kubernetes Helm: https://www.activepieces.com/docs/install/overview . `license_spdx: MIT` describes **only the open core**, not every packaged feature.
- Review install scripts before running, restrict connectors, webhooks, tokens and AI tool actions. Source repository release `0.92.3-hotfix.2` observed.

### n8n — CLEAR

- **Sustainable Use License (SUL)** restricts use to internal-business/personal and limited noncommercial distribution; not an OSI-approved open source license. `.ee` files require the separately defined Enterprise license. Primary: https://github.com/n8n-io/n8n/blob/d93f6130fa3f488c0ccc045fee7c3c507de3c999/LICENSE.md and https://github.com/n8n-io/n8n/blob/d93f6130fa3f488c0ccc045fee7c3c507de3c999/LICENSE_EE.md ; product description: https://docs.n8n.io/
- Keep `license_model: source-available` and **do not invent SPDX** for SUL; `commercial_offering: true` reflects separately paid features/cloud. License of non-master branches needs separate attention according to the repository terms.
- Review code nodes, third-party connectors, credential scopes, exposed webhooks and outbound network access. Latest observed release `n8n@2.45.6`.

### Numaflow — CLEAR

- Source code uses **Apache-2.0**, verified from https://github.com/numaproj/numaflow/blob/d2545229b37718b6e39565237922c2cb416ae66f/LICENSE . Its README describes Kubernetes-native stream processing, decoupled sources/sinks, and delivery semantics: https://github.com/numaproj/numaflow/blob/d2545229b37718b6e39565237922c2cb416ae66f/README.md ; docs https://numaflow.numaproj.io .
- **Not** a generic CI automation / low-code app or runbook tool. Enforce namespaces/RBAC, network boundaries, metrics and tests of replay / at-least-once vs exactly-once paths before relying on data-processing guarantees.

### Rundeck — CLEAR

- Community source in https://github.com/rundeck/rundeck/blob/9573b48d5658d71e37d8387e0dacee3a0cfe2047/LICENSE is **Apache-2.0**; official README https://github.com/rundeck/rundeck/blob/9573b48d5658d71e37d8387e0dacee3a0cfe2047/README.md and ACL docs https://docs.rundeck.com/docs/learning/getting-started/acl-overview.html .
- Open-source Rundeck runbook automation is distinct from separate PagerDuty commercial Runbook Automation product and seat/feature entitlements. `commercial_offering: true` indicates adjacent paid services, not that the OSS core is proprietary.
- Operations scripts require reviewed ACLs, job permissions, least-privilege credentials and secrets isolation; do not equate a successful job with approved change management.

### Windmill — CLEAR with material packaging caveat

- The root https://github.com/windmill-labs/windmill/blob/30c544eba8ab71a7f803c4c425849f8b47530ca8/LICENSE is a **multi-license statement**: source binary built **without the enterprise flag** is AGPLv3, clients and OpenAPI are Apache-2.0, and enterprise code is proprietary. The `license_spdx: AGPL-3.0-only` field is restricted to the primary **open-source runtime source**, not all components. License evidence: https://github.com/windmill-labs/windmill/blob/30c544eba8ab71a7f803c4c425849f8b47530ca8/LICENSE-AGPL and https://github.com/windmill-labs/windmill/blob/30c544eba8ab71a7f803c4c425849f8b47530ca8/LICENSE-APACHE
- Crucially, the published **Community Edition Docker images/binaries include proprietary non-public features**, under restrictions on resale, managed hosting, modifications or embedding. Do not call the distributed Community image wholly OSS. `license_model: open-core` remains a broad model for the product; it does not supersede those license terms.
- Production docs https://www.windmill.dev/docs/advanced/self_host ; overview https://www.windmill.dev/docs/intro . Sandbox worker code execution, limit outbound egress, protect PostgreSQL and credentials, and review Git-synced scripts before execution.

## 3. Exact old/new field manifest — 58 fields

`expected: null` means absent canonical field before review, **not** a literal YAML null to write. Complete arrays in `set` preserve prior `legacy:` evidence at the start. `preserved` lists other keys maintained.

### `activepieces` — CLEAR

```json
{
  "id": "activepieces",
  "expected": {
    "summary": "Workflow automation platform; OSS core with commercial cloud/enterprise features.",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "* You want a self-hostable, open-core alternative to Zapier for integrating apps and automating tasks."
    ],
    "avoid_when": [
      "* You need deep DevOps-specific workflows; it''s more suited for business automation."
    ],
    "deployment_models": [],
    "license_spdx": null,
    "commercial_offering": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:3_CI-CD-Automation/README.md#L160",
      "legacy:devopstools_final.md#L401"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Self-hostable visual workflow and AI automation platform with MIT-licensed core and separately licensed enterprise features.",
    "repository_archived": false,
    "documentation_url": "https://www.activepieces.com/docs/install/overview",
    "use_when": [
      "You need integration workflows or AI-driven automations with a self-hostable builder, reviewed third-party connectors and a defined edition/license."
    ],
    "avoid_when": [
      "You need enterprise or cloud-edition capabilities under the MIT core license; enterprise directories require separate licensing.",
      "You cannot isolate workflow execution from production credentials and untrusted webhooks or audit connector permissions.",
      "You assume one-click installation or remote setup scripts are safe without reviewing their content, secrets and infrastructure prerequisites."
    ],
    "deployment_models": [
      "self-hosted",
      "hosted-saas",
      "container",
      "kubernetes"
    ],
    "license_spdx": "MIT",
    "commercial_offering": true,
    "status": "active",
    "verified_on": "2026-10-29",
    "sources": [
      "legacy:3_CI-CD-Automation/README.md#L160",
      "legacy:devopstools_final.md#L401",
      "https://github.com/activepieces/activepieces",
      "https://github.com/activepieces/activepieces/blob/b2080e13d89b826a408a9f4c5736dbf490e00541/LICENSE",
      "https://www.activepieces.com/docs/install/overview",
      "https://github.com/activepieces/activepieces/blob/b2080e13d89b826a408a9f4c5736dbf490e00541/packages/ee/LICENSE",
      "https://www.activepieces.com/docs/about/license"
    ],
    "needs_review": false
  },
  "preserved": [
    "name",
    "official_url",
    "repository_url",
    "categories",
    "subcategories",
    "roles",
    "lifecycle_stages",
    "license_model",
    "maturity",
    "alternatives",
    "tags"
  ]
}
```

### `n8n` — CLEAR

```json
{
  "id": "n8n",
  "expected": {
    "summary": "Workflow automation platform (fair-code / Sustainable Use License; not OSI open source).",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "* You want a self-hostable, visual workflow automation tool with many integrations."
    ],
    "avoid_when": [
      "* You need a truly OSS-licensed tool or enterprise-scale orchestration."
    ],
    "deployment_models": [],
    "commercial_offering": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:3_CI-CD-Automation/README.md#L164",
      "legacy:devopstools_final.md#L404"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Self-hostable visual and code-based workflow/AI automation platform under the restrictive Sustainable Use License, with separately licensed enterprise modules.",
    "repository_archived": false,
    "documentation_url": "https://docs.n8n.io/",
    "use_when": [
      "You need internal-business or personal automations with integration nodes and can comply with the Sustainable Use License and secure your deployment."
    ],
    "avoid_when": [
      "You require OSI-open-source rights or want to sell, rebrand, provide or distribute a hosted automation service beyond the license restrictions.",
      "You want to use .ee modules in production without the applicable n8n Enterprise license.",
      "You cannot restrict arbitrary workflow code, third-party nodes, external network access and access to stored credentials."
    ],
    "deployment_models": [
      "self-hosted",
      "hosted-saas",
      "container"
    ],
    "commercial_offering": true,
    "status": "active",
    "verified_on": "2026-10-29",
    "sources": [
      "legacy:3_CI-CD-Automation/README.md#L164",
      "legacy:devopstools_final.md#L404",
      "https://github.com/n8n-io/n8n",
      "https://github.com/n8n-io/n8n/blob/d93f6130fa3f488c0ccc045fee7c3c507de3c999/LICENSE.md",
      "https://docs.n8n.io/",
      "https://github.com/n8n-io/n8n/blob/d93f6130fa3f488c0ccc045fee7c3c507de3c999/LICENSE_EE.md",
      "https://github.com/n8n-io/n8n/blob/d93f6130fa3f488c0ccc045fee7c3c507de3c999/README.md"
    ],
    "needs_review": false
  },
  "preserved": [
    "name",
    "official_url",
    "repository_url",
    "categories",
    "subcategories",
    "roles",
    "lifecycle_stages",
    "license_model",
    "maturity",
    "alternatives",
    "tags"
  ]
}
```

### `numaflow` — CLEAR

```json
{
  "id": "numaflow",
  "expected": {
    "summary": "Kubernetes-native data/stream processing platform.",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "* You need Kubernetes-native stream processing for event-driven data pipelines."
    ],
    "avoid_when": [
      "* You need a general-purpose workflow engine or are not on Kubernetes."
    ],
    "deployment_models": [],
    "license_spdx": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:3_CI-CD-Automation/README.md#L166",
      "legacy:devopstools_final.md#L405"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Apache-2.0 Kubernetes-native stream-processing platform for event-driven, parallel data pipelines with independent sources and sinks.",
    "repository_archived": false,
    "documentation_url": "https://numaflow.numaproj.io",
    "use_when": [
      "You operate Kubernetes and need scalable data stream pipelines with decoupled sources, processing vertices and sinks."
    ],
    "avoid_when": [
      "You need a low-code business workflow or incident runbook engine rather than Kubernetes-native streaming infrastructure.",
      "You cannot provide cluster RBAC, storage and observability or validate delivery, ordering and replay semantics with your chosen sources and sinks."
    ],
    "deployment_models": [
      "kubernetes"
    ],
    "license_spdx": "Apache-2.0",
    "status": "active",
    "verified_on": "2026-10-29",
    "sources": [
      "legacy:3_CI-CD-Automation/README.md#L166",
      "legacy:devopstools_final.md#L405",
      "https://github.com/numaproj/numaflow",
      "https://github.com/numaproj/numaflow/blob/d2545229b37718b6e39565237922c2cb416ae66f/LICENSE",
      "https://numaflow.numaproj.io",
      "https://github.com/numaproj/numaflow/blob/d2545229b37718b6e39565237922c2cb416ae66f/README.md"
    ],
    "needs_review": false
  },
  "preserved": [
    "name",
    "official_url",
    "repository_url",
    "categories",
    "subcategories",
    "roles",
    "lifecycle_stages",
    "license_model",
    "maturity",
    "alternatives",
    "tags"
  ]
}
```

### `rundeck` — CLEAR

```json
{
  "id": "rundeck",
  "expected": {
    "summary": "Runbook automation and self-service operations platform.",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [],
    "avoid_when": [],
    "deployment_models": [],
    "license_spdx": null,
    "commercial_offering": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:devopstools_final.md#L407"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Apache-2.0 runbook and self-service operations automation server with CLI and API; PagerDuty commercial Runbook Automation is a separate offering.",
    "repository_archived": false,
    "documentation_url": "https://docs.rundeck.com/docs/learning/getting-started/acl-overview.html",
    "use_when": [
      "You need audited operator runbooks and delegated execution of repeatable infrastructure tasks using ACL-protected jobs and nodes."
    ],
    "avoid_when": [
      "You expect the OSS Rundeck server to include the separate commercial PagerDuty Runbook Automation features or licensing entitlements.",
      "You cannot design least-privilege ACLs, segregate job credentials or control who may execute privileged scripts and commands."
    ],
    "deployment_models": [
      "self-hosted",
      "container"
    ],
    "license_spdx": "Apache-2.0",
    "commercial_offering": true,
    "status": "active",
    "verified_on": "2026-10-29",
    "sources": [
      "legacy:devopstools_final.md#L407",
      "https://github.com/rundeck/rundeck",
      "https://github.com/rundeck/rundeck/blob/9573b48d5658d71e37d8387e0dacee3a0cfe2047/LICENSE",
      "https://docs.rundeck.com/docs/learning/getting-started/acl-overview.html",
      "https://github.com/rundeck/rundeck/blob/9573b48d5658d71e37d8387e0dacee3a0cfe2047/README.md"
    ],
    "needs_review": false
  },
  "preserved": [
    "name",
    "official_url",
    "repository_url",
    "categories",
    "subcategories",
    "roles",
    "lifecycle_stages",
    "license_model",
    "maturity",
    "alternatives",
    "tags"
  ]
}
```

### `windmill` — CLEAR

```json
{
  "id": "windmill",
  "expected": {
    "summary": "Developer platform to build internal tools and automations.",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "* You want to build internal tools, scripts, and automations with a code-first approach."
    ],
    "avoid_when": [
      "* You need a no-code platform or already have a mature internal tools framework."
    ],
    "deployment_models": [],
    "license_spdx": null,
    "commercial_offering": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:3_CI-CD-Automation/README.md#L170",
      "legacy:devopstools_final.md#L408"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Code-first self-hostable workflow, app and AI-agent execution platform with AGPL/Apache open-source components and separately licensed enterprise and distributed-image features.",
    "repository_archived": false,
    "documentation_url": "https://www.windmill.dev/docs/intro",
    "use_when": [
      "You want Git-integrated scripts, scheduled workflows or internal tools with controlled worker execution, self-hosted infrastructure and edition-aware licensing."
    ],
    "avoid_when": [
      "You assume published Community Edition containers are entirely AGPL open source; images also contain proprietary/non-public features under separate restrictions.",
      "You intend resale, embedding, white-labelling or managed service use without checking Windmill's commercial license conditions and AGPL obligations.",
      "You cannot isolate workers executing arbitrary code, protect database credentials or apply roles, network boundaries and secret controls."
    ],
    "deployment_models": [
      "self-hosted",
      "hosted-saas",
      "container",
      "kubernetes"
    ],
    "license_spdx": "AGPL-3.0-only",
    "commercial_offering": true,
    "status": "active",
    "verified_on": "2026-10-29",
    "sources": [
      "legacy:3_CI-CD-Automation/README.md#L170",
      "legacy:devopstools_final.md#L408",
      "https://github.com/windmill-labs/windmill",
      "https://github.com/windmill-labs/windmill/blob/30c544eba8ab71a7f803c4c425849f8b47530ca8/LICENSE",
      "https://www.windmill.dev/docs/intro",
      "https://github.com/windmill-labs/windmill/blob/30c544eba8ab71a7f803c4c425849f8b47530ca8/LICENSE-AGPL",
      "https://github.com/windmill-labs/windmill/blob/30c544eba8ab71a7f803c4c425849f8b47530ca8/LICENSE-APACHE",
      "https://www.windmill.dev/docs/advanced/self_host"
    ],
    "needs_review": false
  },
  "preserved": [
    "name",
    "official_url",
    "repository_url",
    "categories",
    "subcategories",
    "roles",
    "lifecycle_stages",
    "license_model",
    "maturity",
    "alternatives",
    "tags"
  ]
}
```


## 4. Validation and publication gates

1. At the candidate HEAD verify exactly five changed canonical IDs and the other 12 records byte-for-byte, historical link baseline unchanged.
2. On local Windows checkout, run `python -m scripts.generate_docs`, `python -m scripts.generate_docs --check`, `python -m scripts.validate_catalog`, `python -m scripts.review_debt --format json`, `python -m ruff check scripts tests`, `python -m ruff format --check scripts tests`, `python -m pip check`, `python -m pytest`, `git diff --check`.
3. Require generated counts **1425 / 844 / 567 / 76**, inspect exact generated doc paths; commit only expected docs as a second distinct commit.
4. Open **Draft PR** only after final-docs commit; require PR CI (quality, CodeQL, Gitleaks, Plumber) on final HEAD. For **Full link audit strict** check `blocking_new: 0`, `strict_result: PASS`, and separate historical `blocking_known`. No baseline exemptions.
5. Trigger `@codex review` after readiness and verify review completion without findings, rather than inferring it from a green check. Human approval of final diff and **squash merge only**, followed by post-merge CI and local sync. Do not modify historical issue #2.

**Status: CANONICAL PATCH ONLY; GENERATED DOCUMENTATION AND CI NOT YET VERIFIED.**

## 5.1. Link-audit #48 failure and evidence-only corrective change (2026-10-29)

- Strict audit #48 ran against PR SHA `14ec11298eaa2a1a3147228a6df5db204b0f65f5`: `blocking_new: 2`, `blocking_known: 6`, `strict_result: FAIL`.
- New n8n docs path `/sustainable-use-license/` returned HTTP 404 (both HEAD and fallback GET); replaced with the functioning official documentation root in the `n8n` record (`documentation_url` and `sources`) and the above OLD/NEW evidence manifest. The exact immutable upstream `LICENSE.md` and `LICENSE_EE.md` citations remain the primary legal evidence for SUL and Enterprise terms.
- Separate, pre-existing Prometheus documentation path `/docs/introduction/overview/` returned HTTP 520 during #48; it returned 200 in audit #47 and is accessible through independent web verification. This is consistent with an intermittent upstream or network error, **not a reason to change the catalogue or whitelist the link**.
- Old/current YAML field count and fixed review cohort remain unchanged: five reviewed IDs, 58 originally changed canonical fields. This repair changes **two fields within the same `n8n` record**, with no taxonomy, license, status or other tool modification.
- The affected generated category page must be regenerated deterministically from canonical YAML; check its exact diff before staging. CI, a new strict link audit on the final HEAD, and human review are still blocking. No claim of a passing strict audit has been made.
