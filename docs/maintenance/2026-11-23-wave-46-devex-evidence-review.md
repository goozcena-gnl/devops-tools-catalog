# Wave 46 — DevEx terminals, AI tools, and local environments

Publisher material was checked on **2026-11-23 UTC** under [issue #202](https://github.com/goozcena-gnl/devops-tools-catalog/issues/202).
The baseline commit was `86cfc5befe9bd1318a90100562aa0d4ea0f22f1b` and the category Git blob was `a65613c2632e4e40c3ffb6e3ad1e278285167da5`.
The 101 IDs retain their original order. The 91 records outside the cohort match the baseline byte for byte.

The ten IDs, names, categories, subcategories, roles, lifecycle stages, alternatives, and tags retain their original values. Each source list keeps all original entries in order. The raw diff and validation logs are stored in the external Wave 46 evidence directory.

## Decisions

| ID | Decision | Changed keys |
| --- | --- | --- |
| `ghostty` | CLEAR | `avoid_when`, `deployment_models`, `documentation_url`, `license_spdx`, `needs_review`, `sources`, `status`, `summary`, `use_when`, `verified_on` |
| `tabby` | RECLASSIFY | `avoid_when`, `deployment_models`, `documentation_url`, `license_model`, `sources`, `summary`, `use_when` |
| `ramalama` | CLEAR | `avoid_when`, `deployment_models`, `documentation_url`, `license_spdx`, `needs_review`, `sources`, `status`, `summary`, `use_when`, `verified_on` |
| `markitdown` | CLEAR | `avoid_when`, `deployment_models`, `documentation_url`, `license_spdx`, `needs_review`, `sources`, `status`, `summary`, `use_when`, `verified_on` |
| `open-interpreter` | RETAIN | `avoid_when`, `deployment_models`, `sources`, `summary`, `use_when` |
| `play-with-docker` | RETAIN | `avoid_when`, `deployment_models`, `documentation_url`, `sources`, `summary`, `use_when` |
| `asp-net-aspire` | CLEAR | `avoid_when`, `deployment_models`, `documentation_url`, `license_spdx`, `needs_review`, `repository_url`, `sources`, `status`, `summary`, `use_when`, `verified_on` |
| `tabby-terminal` | CLEAR | `avoid_when`, `deployment_models`, `documentation_url`, `license_spdx`, `needs_review`, `sources`, `status`, `summary`, `use_when`, `verified_on` |
| `omarchy` | RETAIN | `avoid_when`, `deployment_models`, `documentation_url`, `repository_url`, `sources`, `summary`, `use_when` |
| `azure-storage-explorer` | RECLASSIFY | `avoid_when`, `deployment_models`, `documentation_url`, `license_model`, `sources`, `summary`, `use_when` |

### `ghostty` — CLEAR

The pinned repository and publisher’s macOS/Linux documentation establish the desktop application's scope. The publisher released Ghostty 1.4.0 on 2026-10-27 and documents terminal integration security fixes. The MIT conclusion covers the reviewed repository source. Downstream packaging and libghostty API stability are separate.

Confidence. High for the desktop platforms, current release and repository MIT grant. Downstream packages and library compatibility remain separate.

Publisher revision `3e9b1cca3775bc31dcc055b5172832a3dcd1d66c`. [Pinned README](https://github.com/ghostty-org/ghostty/blob/3e9b1cca3775bc31dcc055b5172832a3dcd1d66c/README.md) · [Pinned root licence](https://github.com/ghostty-org/ghostty/blob/3e9b1cca3775bc31dcc055b5172832a3dcd1d66c/LICENSE)

| Field | Baseline | Candidate | Evidence and scope |
| --- | --- | --- | --- |
| `summary` | `Fast, cross-platform GPU-accelerated terminal emulator with native desktop integration.` | `GPU-accelerated terminal emulator with native macOS and Linux interfaces built on the shared libghostty terminal core.` | Pinned README and publisher architecture notes distinguish the GUI from the shared core. |
| `use_when` | `[]` | `["You want local terminal tabs, splits, and native desktop integration on macOS or Linux."]` | The pinned README and publisher docs describe tabs, splits, and platform-specific integration. |
| `avoid_when` | `[]` | `["You require a first-party Windows desktop app, a stable standalone libghostty API, or guaranteed isolation from untrusted terminal output."]` | The dated release notes distinguish the GUI platforms from library compatibility and document security fixes for terminal interactions. |
| `deployment_models` | `[]` | `["local"]` | Publisher docs distribute or document a locally installed terminal. |
| `official_url` | [https://ghostty.org](https://ghostty.org) | Unchanged | Current record value retained. |
| `repository_url` | [https://github.com/ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | Unchanged | Current record value retained. |
| `documentation_url` | Absent | [https://ghostty.org/docs](https://ghostty.org/docs) | The pinned README directs readers to this publisher documentation. |
| `license_model` | `oss` | Unchanged | The existing model remains; see the scope and unresolved questions above. |
| `license_spdx` | Absent | `MIT` | The pinned licence gives the reviewed project source an MIT grant. |
| `maturity` | `unknown` | Unchanged | The evidence does not establish the catalogue's maturity class. |
| `status` | `needs-review` | `active` | Dated first-party release, documentation, repository identity and source licence support clearance in the documented scope. |
| `needs_review` | `true` | `false` | Dated first-party release, documentation, repository identity and source licence support clearance in the documented scope. |
| `verified_on` | `2026-08-03` | `2026-11-23` | The material canonical claims were reviewed together on this date. |
| `repository_archived` | Absent | Unchanged | Repository metadata is tracked separately from the review decision or hosted service lifecycle. |

The `sources` field retains the following original entries in order.

- `legacy:devopstools_final.md#L1062`

The candidate appends these entries in order.

- [Publisher README with capabilities and operational boundaries](https://github.com/ghostty-org/ghostty/blob/3e9b1cca3775bc31dcc055b5172832a3dcd1d66c/README.md)
- [Pinned repository licence text](https://github.com/ghostty-org/ghostty/blob/3e9b1cca3775bc31dcc055b5172832a3dcd1d66c/LICENSE)
- [Publisher documentation for the desktop app](https://ghostty.org/docs)
- [Native UI and desktop app versus library scope](https://ghostty.org/docs/about)
- [Publisher's dated release notes and terminal security fixes](https://ghostty.org/docs/install/release-notes/1-4-0)

### `tabby` — RECLASSIFY

The Apache-2.0 source grant expressly excludes ee/ and applicable third-party components. The pinned Enterprise licence requires a qualifying subscription or agreement and the correct seats for production use. The two grants establish open-core. Deployment-specific edition, model, and code privacy conclusions remain under review. The administration guide confirms a free Community tier and paid Team and Enterprise tiers. The licence for a specific production deployment still depends on the applicable agreement. The public terms page linked from the Enterprise licence currently presents the FOSS grant. The edition documentation and pinned Enterprise licence establish the split while deployment-specific subscription terms still need review.

Confidence. High for the source and Enterprise split. Rights and privacy for specific deployed editions and model configurations remain unresolved.

Publisher revision `21b29048d7bcf6b94f9f482f2d0fd05efadfd19f`. [Pinned README](https://github.com/TabbyML/tabby/blob/21b29048d7bcf6b94f9f482f2d0fd05efadfd19f/README.md) · [Pinned root licence](https://github.com/TabbyML/tabby/blob/21b29048d7bcf6b94f9f482f2d0fd05efadfd19f/LICENSE)

| Field | Baseline | Candidate | Evidence and scope |
| --- | --- | --- | --- |
| `summary` | `Self-hosted AI coding assistant.` | `Self-hosted AI coding assistant from TabbyML with a code completion server and IDE extensions, including separately licensed Enterprise components.` | The README identifies the TabbyML assistant and the pinned licence files establish the separate Enterprise component. |
| `use_when` | `["* You want a self-hosted GitHub Copilot alternative with full control over your data and model."]` | `["You can operate a coding-assistant server and review which code context, model backends, and credentials are used."]` | The publisher docs link the self-hosted server, IDE extensions, and configured model backends. |
| `avoid_when` | `["* You lack GPU infrastructure for self-hosting or want zero-maintenance AI code completion."]` | `["You need a managed service or cannot govern source-code egress, model rights, and Enterprise terms for your deployment."]` | The feature and model documentation plus the Enterprise carve-out support distinct privacy, model and edition checks. |
| `deployment_models` | `[]` | `["self-hosted"]` | The pinned README and publisher docs document on-premises server operation. |
| `official_url` | [https://www.tabbyml.com](https://www.tabbyml.com) | Unchanged | Current record value retained. |
| `repository_url` | [https://github.com/TabbyML/tabby](https://github.com/TabbyML/tabby) | Unchanged | Current record value retained. |
| `documentation_url` | Absent | [https://tabby.tabbyml.com/docs/welcome/](https://tabby.tabbyml.com/docs/welcome/) | The pinned README directs users to the TabbyML documentation. |
| `license_model` | `oss` | `open-core` | The pinned root and Enterprise texts establish separate grants. Publisher administration docs confirm a free Community tier and paid Team and Enterprise tiers. |
| `license_spdx` | Absent | Unchanged | Edition, implementation, package or binary terms do not support a new SPDX assignment for this record. |
| `maturity` | `unknown` | Unchanged | The evidence does not establish the catalogue's maturity class. |
| `status` | `needs-review` | Unchanged | The unresolved question above remains in the review queue. |
| `needs_review` | `true` | Unchanged | The unresolved question above remains in the review queue. |
| `verified_on` | `2026-08-03` | Unchanged | Retained pending completion of the outstanding review. |
| `repository_archived` | Absent | Unchanged | Repository metadata is tracked separately from the review decision or hosted service lifecycle. |

The `sources` field retains the following original entries in order.

- `legacy:3_CI-CD-Automation/README.md#L184`
- `legacy:devopstools_final.md#L424`

The candidate appends these entries in order.

- [Publisher README with capabilities and operational boundaries](https://github.com/TabbyML/tabby/blob/21b29048d7bcf6b94f9f482f2d0fd05efadfd19f/README.md)
- [Pinned repository licence text](https://github.com/TabbyML/tabby/blob/21b29048d7bcf6b94f9f482f2d0fd05efadfd19f/LICENSE)
- [Supplementary publisher evidence at the same revision](https://github.com/TabbyML/tabby/blob/21b29048d7bcf6b94f9f482f2d0fd05efadfd19f/ee/LICENSE)
- [TabbyML documentation and server/IDE boundaries](https://tabby.tabbyml.com/docs/welcome/)
- [Publisher administration reference for Community, Team, and Enterprise tiers](https://tabby.tabbyml.com/docs/administration/license/)
- [Public terms endpoint currently describing the FOSS grant](https://tabby.tabbyml.com/terms/)

### `ramalama` — CLEAR

The publisher released v0.26.0 on 2026-11-04. The pinned README and MIT licence cover the RamaLama tooling for local inference and serving. Model weights, registry trust, GPU images and effective isolation are deployment-specific. The README explicitly documents an attempted host fallback when neither container engine is installed.

Confidence. High for CLI capabilities, host fallback, the dated release and the MIT source grant. Actual runtime isolation remains deployment-specific.

Publisher revision `58c808965f181c3b7c3fa9c3f6061d25811c053a`. [Pinned README](https://github.com/containers/ramalama/blob/58c808965f181c3b7c3fa9c3f6061d25811c053a/README.md) · [Pinned root licence](https://github.com/containers/ramalama/blob/58c808965f181c3b7c3fa9c3f6061d25811c053a/LICENSE)

| Field | Baseline | Candidate | Evidence and scope |
| --- | --- | --- | --- |
| `summary` | `AI-powered development assistant.` | `CLI for fetching, running, and serving AI models with OCI-oriented workflows. It uses Podman or Docker when available and attempts host execution when neither engine is installed.` | The pinned README documents the Podman and Docker execution path and explicitly says it attempts host execution when neither engine is installed. |
| `use_when` | `["* You want to run LLMs locally in containers with OCI-native tooling."]` | `["You want to manage models from registries and run inference locally or serve a model through an API."]` | The pinned README describes model transports and serving via an API. |
| `avoid_when` | `["* You prefer cloud-hosted AI or don't need containerized LLM management."]` | `["You require container-only execution and cannot ensure that a supported engine is available, or cannot verify model and image provenance, GPU access, and effective runtime permissions."]` | The pinned README distinguishes host fallback from container-only protections. Actual device access and isolation depend on deployment. |
| `deployment_models` | `[]` | `["local", "self-hosted"]` | The pinned README covers local CLI inference and user-operated API serving. |
| `official_url` | [https://ramalama.ai](https://ramalama.ai) | Unchanged | Current record value retained. |
| `repository_url` | [https://github.com/containers/ramalama](https://github.com/containers/ramalama) | Unchanged | Current record value retained. |
| `documentation_url` | Absent | [https://github.com/containers/ramalama/blob/58c808965f181c3b7c3fa9c3f6061d25811c053a/README.md](https://github.com/containers/ramalama/blob/58c808965f181c3b7c3fa9c3f6061d25811c053a/README.md) | The pinned README contains runtime, install, registry, and security documentation. |
| `license_model` | `oss` | Unchanged | The existing model remains; see the scope and unresolved questions above. |
| `license_spdx` | Absent | `MIT` | The pinned licence gives the reviewed project source an MIT grant. |
| `maturity` | `unknown` | Unchanged | The evidence does not establish the catalogue's maturity class. |
| `status` | `needs-review` | `active` | Dated first-party release, documentation, repository identity and source licence support clearance in the documented scope. |
| `needs_review` | `true` | `false` | Dated first-party release, documentation, repository identity and source licence support clearance in the documented scope. |
| `verified_on` | `2026-08-03` | `2026-11-23` | The material canonical claims were reviewed together on this date. |
| `repository_archived` | Absent | Unchanged | Repository metadata is tracked separately from the review decision or hosted service lifecycle. |

The `sources` field retains the following original entries in order.

- `legacy:3_CI-CD-Automation/README.md#L180`
- `legacy:devopstools_final.md#L421`

The candidate appends these entries in order.

- [Publisher README with capabilities and operational boundaries](https://github.com/containers/ramalama/blob/58c808965f181c3b7c3fa9c3f6061d25811c053a/README.md)
- [Pinned repository licence text](https://github.com/containers/ramalama/blob/58c808965f181c3b7c3fa9c3f6061d25811c053a/LICENSE)
- [Publisher release from 2026-11-04](https://github.com/containers/ramalama/releases/tag/v0.26.0)

### `markitdown` — CLEAR

Microsoft published v0.1.9 on 2026-10-21. The pinned MIT licence covers the converter source. Optional plugins, cloud OCR or model backends, and input-data handling require separate evaluation.

Confidence. High for the release, MIT source grant and current-process I/O boundary. Plugin and provider handling require separate review.

Publisher revision `ed178952a6672abdfd35b5f9e76a80b6cefc086e`. [Pinned README](https://github.com/microsoft/markitdown/blob/ed178952a6672abdfd35b5f9e76a80b6cefc086e/README.md) · [Pinned root licence](https://github.com/microsoft/markitdown/blob/ed178952a6672abdfd35b5f9e76a80b6cefc086e/LICENSE)

| Field | Baseline | Candidate | Evidence and scope |
| --- | --- | --- | --- |
| `summary` | `Python tool for converting files and Office documents to Markdown.` | `Python library and CLI that convert Office documents, PDFs, and other supported inputs into Markdown.` | The pinned README documents supported formats and Python and CLI entry points. |
| `use_when` | `[]` | `["You need Markdown extraction from supported files and can control file access, optional plugins, and any external document or model requests."]` | The README documents narrow conversion modes, optional plugins, and cloud integrations. |
| `avoid_when` | `[]` | `["You need to accept untrusted files or URLs without validation and isolation. Conversion uses the current process's file and network privileges."]` | The README security section explains current-process I/O privileges and validation for untrusted input. |
| `deployment_models` | `[]` | `["local"]` | The README documents local library and command-line use. |
| `official_url` | Absent | Unchanged | Current record value retained. |
| `repository_url` | [https://github.com/microsoft/markitdown](https://github.com/microsoft/markitdown) | Unchanged | Current record value retained. |
| `documentation_url` | Absent | [https://github.com/microsoft/markitdown/blob/ed178952a6672abdfd35b5f9e76a80b6cefc086e/README.md](https://github.com/microsoft/markitdown/blob/ed178952a6672abdfd35b5f9e76a80b6cefc086e/README.md) | The pinned README documents installation, supported inputs, plugins and security. |
| `license_model` | `oss` | Unchanged | The existing model remains; see the scope and unresolved questions above. |
| `license_spdx` | Absent | `MIT` | The pinned licence gives the reviewed project source an MIT grant. |
| `maturity` | `unknown` | Unchanged | The evidence does not establish the catalogue's maturity class. |
| `status` | `needs-review` | `active` | Dated first-party release, documentation, repository identity and source licence support clearance in the documented scope. |
| `needs_review` | `true` | `false` | Dated first-party release, documentation, repository identity and source licence support clearance in the documented scope. |
| `verified_on` | `2026-08-03` | `2026-11-23` | The material canonical claims were reviewed together on this date. |
| `repository_archived` | Absent | Unchanged | Repository metadata is tracked separately from the review decision or hosted service lifecycle. |

The `sources` field retains the following original entries in order.

- `legacy:devopstools_final.md#L1088`

The candidate appends these entries in order.

- [Publisher README with capabilities and operational boundaries](https://github.com/microsoft/markitdown/blob/ed178952a6672abdfd35b5f9e76a80b6cefc086e/README.md)
- [Pinned repository licence text](https://github.com/microsoft/markitdown/blob/ed178952a6672abdfd35b5f9e76a80b6cefc086e/LICENSE)
- [Publisher release from 2026-10-21](https://github.com/microsoft/markitdown/releases/tag/v0.1.9)

### `open-interpreter` — RETAIN

GitHub resolves the former and current URLs to repository ID 666299222, but the publisher documents a Rust/Codex reimplementation and a separate community-maintained Python fork. Retain the existing identity URL and review state pending a compatibility and licensing decision per generation.

Confidence. High for repository continuity and the publisher-described Rust/Python split. Original Python compatibility and licence coverage remain unresolved.

Publisher revision `a786d8474b0d7289320c16f00e852679fae7866e`. [Pinned README](https://github.com/openinterpreter/openinterpreter/blob/a786d8474b0d7289320c16f00e852679fae7866e/README.md) · [Pinned root licence](https://github.com/openinterpreter/openinterpreter/blob/a786d8474b0d7289320c16f00e852679fae7866e/LICENSE)

| Field | Baseline | Candidate | Evidence and scope |
| --- | --- | --- | --- |
| `summary` | `Run AI that can execute tasks locally.` | `Terminal coding agent with local command execution. The publisher's current Rust agent and the original Python implementation have separate compatibility and execution boundaries.` | The pinned README identifies the Rust version and points readers to the separate original Python line. |
| `use_when` | `["* You want an AI that can execute code, manage files, and control your computer via natural language."]` | `["You can identify the installed implementation and review its command, file, network, model-provider, and approval controls."]` | The pinned README and security policy identify release-specific sandbox, approval, and provider boundaries. |
| `avoid_when` | `["* You're uncomfortable with AI having system-level access or need isolated sandboxed execution."]` | `["You rely on original Python behavior or require execution isolation that you have not verified for the chosen release."]` | The upstream README explicitly distinguishes the original Python lineage; the security policy scopes protections to the inherited runtime. |
| `deployment_models` | `[]` | `["local"]` | The pinned docs describe a locally run terminal agent, with model providers reviewed separately. |
| `official_url` | [https://openinterpreter.com](https://openinterpreter.com) | Unchanged | Current record value retained. |
| `repository_url` | [https://github.com/KillianLucas/open-interpreter](https://github.com/KillianLucas/open-interpreter) | Unchanged | The redirect is established. Product-generation compatibility and coverage of the original implementation are unresolved. |
| `documentation_url` | Absent | Unchanged | The current docs describe the Rust version. The historical record has no verified shared docs endpoint. |
| `license_model` | `oss` | Unchanged | The existing model remains; see the scope and unresolved questions above. |
| `license_spdx` | Absent | Unchanged | Edition, implementation, package or binary terms do not support a new SPDX assignment for this record. |
| `maturity` | `unknown` | Unchanged | The evidence does not establish the catalogue's maturity class. |
| `status` | `needs-review` | Unchanged | The unresolved question above remains in the review queue. |
| `needs_review` | `true` | Unchanged | The unresolved question above remains in the review queue. |
| `verified_on` | `2026-08-03` | Unchanged | Retained pending completion of the outstanding review. |
| `repository_archived` | Absent | Unchanged | Repository metadata is tracked separately from the review decision or hosted service lifecycle. |

The `sources` field retains the following original entries in order.

- `legacy:3_CI-CD-Automation/README.md#L178`
- `legacy:devopstools_final.md#L418`

The candidate appends these entries in order.

- [Publisher README with capabilities and operational boundaries](https://github.com/openinterpreter/openinterpreter/blob/a786d8474b0d7289320c16f00e852679fae7866e/README.md)
- [Pinned repository licence text](https://github.com/openinterpreter/openinterpreter/blob/a786d8474b0d7289320c16f00e852679fae7866e/LICENSE)
- [Supplementary publisher evidence at the same revision](https://github.com/openinterpreter/openinterpreter/blob/a786d8474b0d7289320c16f00e852679fae7866e/SECURITY.md)
- [Publisher Rust release from 2026-11-11](https://github.com/openinterpreter/openinterpreter/releases/tag/rust-v0.0.61)

### `play-with-docker` — RETAIN

The pinned README and the hosted endpoint both announce unavailability starting 2026-03-01. The endpoint served the notice on 2026-11-23; the HTTP 200 documents a notice, with no evidence of a runnable hosted lab. The canonical block historically describes both the hosted offering and the surviving MIT repository. It remains under review pending a lifecycle and licence decision for that mixed scope.

Confidence. High for the publisher’s hosted unavailability notice and the MIT repository text. Mixed offering status and applicability of the historical catalogue classification remain open.

Publisher revision `62cb0727cab93cf4273017d33e965a5f26c83b05`. [Pinned README](https://github.com/play-with-docker/play-with-docker/blob/62cb0727cab93cf4273017d33e965a5f26c83b05/README.md) · [Pinned root licence](https://github.com/play-with-docker/play-with-docker/blob/62cb0727cab93cf4273017d33e965a5f26c83b05/LICENSE)

| Field | Baseline | Candidate | Evidence and scope |
| --- | --- | --- | --- |
| `summary` | `Interactive Docker playground; open-source platform with hosted labs site.` | `Source for a browser-based Docker playground. The publisher announced that hosted Play with Docker and Play with Kubernetes labs would become unavailable starting 2026-03-01.` | The pinned README documents both the historical implementation and the dated hosted-service notice. |
| `use_when` | `["Quick Docker experiments, workshops, or demos without installing anything."]` | `["You need the historical playground source or want to review its documented self-hosted development setup."]` | The pinned README documents a local development setup and the source remains available. |
| `avoid_when` | `["For persistent work—sessions are ephemeral."]` | `["You need an available publisher-hosted lab or persistent Docker infrastructure."]` | The dated publisher notice appears in the README and on the former lab landing page. |
| `deployment_models` | `[]` | `["self-hosted"]` | The pinned README documents running the repository in a development environment. |
| `official_url` | [https://labs.play-with-docker.com](https://labs.play-with-docker.com) | Unchanged | The existing endpoint now displays the publisher's dated unavailability notice. |
| `repository_url` | [https://github.com/play-with-docker/play-with-docker](https://github.com/play-with-docker/play-with-docker) | Unchanged | Current record value retained. |
| `documentation_url` | Absent | [https://github.com/play-with-docker/play-with-docker/blob/62cb0727cab93cf4273017d33e965a5f26c83b05/README.md](https://github.com/play-with-docker/play-with-docker/blob/62cb0727cab93cf4273017d33e965a5f26c83b05/README.md) | The pinned README contains the dated notice and repository development instructions. |
| `license_model` | `documentation` | Unchanged | The existing model remains; see the scope and unresolved questions above. |
| `license_spdx` | Absent | Unchanged | Edition, implementation, package or binary terms do not support a new SPDX assignment for this record. |
| `maturity` | `unknown` | Unchanged | The evidence does not establish the catalogue's maturity class. |
| `status` | `needs-review` | Unchanged | The unresolved question above remains in the review queue. |
| `needs_review` | `true` | Unchanged | The unresolved question above remains in the review queue. |
| `verified_on` | `2026-08-03` | Unchanged | Retained pending completion of the outstanding review. |
| `repository_archived` | Absent | Unchanged | Repository metadata is tracked separately from the review decision or hosted service lifecycle. |

The `sources` field retains the following original entries in order.

- `legacy:7_Development-Collaboration/README.md#L40`
- `legacy:devopstools_final.md#L1070`

The candidate appends these entries in order.

- [Publisher README with capabilities and operational boundaries](https://github.com/play-with-docker/play-with-docker/blob/62cb0727cab93cf4273017d33e965a5f26c83b05/README.md)
- [Pinned repository licence text](https://github.com/play-with-docker/play-with-docker/blob/62cb0727cab93cf4273017d33e965a5f26c83b05/LICENSE)

### `asp-net-aspire` — CLEAR

Both repository URLs resolve to GitHub repository ID 696529789. The publisher documents Aspire 17.0.0, the AppHost and CLI, and the MIT licence of Aspire software. The licence and verification scope covers Aspire tooling. Resource integrations, external services, and third-party containers retain their own terms.

Confidence. High for the publisher transfer, AppHost and CLI scope, release and MIT software grant. Third-party deployment resources require review.

Publisher revision `f9da20e55ed248cb56e4235772fb415b24551fe3`. [Pinned README](https://github.com/microsoft/aspire/blob/f9da20e55ed248cb56e4235772fb415b24551fe3/README.md) · [Pinned root licence](https://github.com/microsoft/aspire/blob/f9da20e55ed248cb56e4235772fb415b24551fe3/LICENSE.TXT)

| Field | Baseline | Candidate | Evidence and scope |
| --- | --- | --- | --- |
| `summary` | `Orchestration + tooling for building cloud-native .NET distributed applications.` | `Multi-language, code-first orchestration and observability toolchain that uses Aspire AppHost and CLI to run distributed applications locally and support deployment.` | The pinned README describes a multi-language AppHost, CLI, local execution, OpenTelemetry and deployment. |
| `use_when` | `["Building .NET distributed apps and you want built-in service discovery, telemetry, and health checks."]` | `["You want to describe service dependencies in code, run the application locally, and carry the model into a supported deployment workflow."]` | The publisher docs describe modelling resources, local execution, and supported deployment workflows. |
| `avoid_when` | `["You're not in the .NET ecosystem."]` | `["You need preapproved third-party images or managed services and cannot verify their terms, security, and compatibility independently."]` | The pinned README calls for independent evaluation of third-party containers used by integrations. |
| `deployment_models` | `[]` | `["local"]` | The pinned README documents the local tooling. Workload deployment targets are separate. |
| `official_url` | [https://aspire.dev](https://aspire.dev) | Unchanged | Current record value retained. |
| `repository_url` | [https://github.com/dotnet/aspire](https://github.com/dotnet/aspire) | [https://github.com/microsoft/aspire](https://github.com/microsoft/aspire) | The former URL redirects to the pinned publisher repository with the same GitHub ID. No other canonical record uses the normalized target. |
| `documentation_url` | Absent | [https://aspire.dev/docs/](https://aspire.dev/docs/) | The pinned README points to the Aspire documentation. |
| `license_model` | `oss` | Unchanged | The existing model remains; see the scope and unresolved questions above. |
| `license_spdx` | Absent | `MIT` | The pinned licence gives the reviewed project source an MIT grant. |
| `maturity` | `unknown` | Unchanged | The evidence does not establish the catalogue's maturity class. |
| `status` | `needs-review` | `active` | Dated first-party release, documentation, repository identity and source licence support clearance in the documented scope. |
| `needs_review` | `true` | `false` | Dated first-party release, documentation, repository identity and source licence support clearance in the documented scope. |
| `verified_on` | `2026-08-03` | `2026-11-23` | The material canonical claims were reviewed together on this date. |
| `repository_archived` | Absent | Unchanged | Repository metadata is tracked separately from the review decision or hosted service lifecycle. |

The `sources` field retains the following original entries in order.

- `legacy:7_Development-Collaboration/README.md#L85`
- `legacy:devopstools_final.md#L1125`

The candidate appends these entries in order.

- [Publisher README with capabilities and operational boundaries](https://github.com/microsoft/aspire/blob/f9da20e55ed248cb56e4235772fb415b24551fe3/README.md)
- [Pinned repository licence text](https://github.com/microsoft/aspire/blob/f9da20e55ed248cb56e4235772fb415b24551fe3/LICENSE.TXT)
- [Publisher docs for the AppHost, CLI, SDK and deployment](https://aspire.dev/docs/)
- [Publisher release from 2026-11-18 UTC on GitHub](https://github.com/microsoft/aspire/releases/tag/v17.0.0)

### `tabby-terminal` — CLEAR

Eugeny's desktop terminal published v1.0.238 on 2026-10-07 and provides a pinned MIT licence. Optional plugins and the separate web implementation require their own approval and licence review.

Confidence. High for desktop capabilities, release and MIT source grant. Plugin and web implementation terms remain separate.

Publisher revision `467ce8ebfa467fb88cf6d154c9a5891e3d3647f0`. [Pinned README](https://github.com/Eugeny/tabby/blob/467ce8ebfa467fb88cf6d154c9a5891e3d3647f0/README.md) · [Pinned root licence](https://github.com/Eugeny/tabby/blob/467ce8ebfa467fb88cf6d154c9a5891e3d3647f0/LICENSE)

| Field | Baseline | Candidate | Evidence and scope |
| --- | --- | --- | --- |
| `summary` | `Cross-platform terminal emulator with built-in SSH, serial, and theming/plugins.` | `Desktop terminal emulator and SSH and serial client for Windows, macOS, and Linux, with plugin support including optional SFTP.` | The pinned terminal README documents the desktop platforms, SSH, serial and available SFTP plugin. |
| `use_when` | `["You want a modern, extensible terminal with SSH management built in."]` | `["You want to manage local shells, remote SSH sessions, or serial connections from one desktop client."]` | The pinned README describes the integrated desktop terminal and connection manager. |
| `avoid_when` | `["You prefer lightweight, native terminals (iTerm2, Windows Terminal) and manage SSH via config files."]` | `["You cannot govern third-party plugins or how SSH keys, agent forwarding, and synchronized connection profiles are handled."]` | The pinned README documents third-party plugins, agent forwarding and profile sync features. |
| `deployment_models` | `[]` | `["local"]` | The pinned README covers installed desktop builds. The separately linked web app is outside this record. |
| `official_url` | [https://tabby.sh](https://tabby.sh) | Unchanged | Current record value retained. |
| `repository_url` | [https://github.com/eugeny/tabby](https://github.com/eugeny/tabby) | Unchanged | Current record value retained. |
| `documentation_url` | Absent | [https://github.com/Eugeny/tabby/blob/467ce8ebfa467fb88cf6d154c9a5891e3d3647f0/README.md](https://github.com/Eugeny/tabby/blob/467ce8ebfa467fb88cf6d154c9a5891e3d3647f0/README.md) | The pinned README documents desktop and plugin capabilities for the Eugeny project. |
| `license_model` | `oss` | Unchanged | The existing model remains; see the scope and unresolved questions above. |
| `license_spdx` | Absent | `MIT` | The pinned licence gives the reviewed project source an MIT grant. |
| `maturity` | `unknown` | Unchanged | The evidence does not establish the catalogue's maturity class. |
| `status` | `needs-review` | `active` | Dated first-party release, documentation, repository identity and source licence support clearance in the documented scope. |
| `needs_review` | `true` | `false` | Dated first-party release, documentation, repository identity and source licence support clearance in the documented scope. |
| `verified_on` | `2026-08-03` | `2026-11-23` | The material canonical claims were reviewed together on this date. |
| `repository_archived` | Absent | Unchanged | Repository metadata is tracked separately from the review decision or hosted service lifecycle. |

The `sources` field retains the following original entries in order.

- `legacy:7_Development-Collaboration/README.md#L41`
- `legacy:devopstools_final.md#L1071`

The candidate appends these entries in order.

- [Publisher README with capabilities and operational boundaries](https://github.com/Eugeny/tabby/blob/467ce8ebfa467fb88cf6d154c9a5891e3d3647f0/README.md)
- [Pinned repository licence text](https://github.com/Eugeny/tabby/blob/467ce8ebfa467fb88cf6d154c9a5891e3d3647f0/LICENSE)
- [Publisher release from 2026-10-07](https://github.com/Eugeny/tabby/releases/tag/v1.0.238)

### `omarchy` — RETAIN

The former URL redirects to the current publisher repository with ID 994093166. The pinned quattro manual and 4.5.0 release identify the distribution. The root permission text applies to repository material. Distribution images, Arch packages, optional packages, and host hardening require separate review.

Confidence. High for the publisher move and stated distribution components. Whole-image terms and effective machine settings remain open.

Publisher revision `6a7e265491d655abe0a658e435b14dd3895d703f`. [Pinned README](https://github.com/omacom/omarchy/blob/6a7e265491d655abe0a658e435b14dd3895d703f/README.md) · [Pinned root licence](https://github.com/omacom/omarchy/blob/6a7e265491d655abe0a658e435b14dd3895d703f/LICENSE)

| Field | Baseline | Candidate | Evidence and scope |
| --- | --- | --- | --- |
| `summary` | `Beautiful, opinionated Linux workstation environment focused on a curated desktop setup.` | `Arch Linux-based workstation distribution with a curated Hyprland desktop, bundled applications, and its own installer and package repository.` | The pinned welcome and security manuals describe Arch, Hyprland, the setup, and package sources. |
| `use_when` | `[]` | `["You want an opinionated local Linux workstation and can review installation, hardware, package sources, and actual security settings."]` | The pinned manual describes installation, optional settings and dependence on Arch and Omarchy packages. |
| `avoid_when` | `[]` | `["You require a separately validated workstation security baseline or cannot review the installer and third-party package sources."]` | The pinned manual describes publisher defaults and exceptions, including optional encryption settings and package sources. |
| `deployment_models` | `[]` | `["local"]` | The pinned manual describes a user-installed workstation OS. |
| `official_url` | [https://omarchy.org](https://omarchy.org) | Unchanged | Current record value retained. |
| `repository_url` | [https://github.com/basecamp/omarchy](https://github.com/basecamp/omarchy) | [https://github.com/omacom/omarchy](https://github.com/omacom/omarchy) | The former and current upstream URLs resolve to the same GitHub repository ID. The normalized target is unique in the catalogue. |
| `documentation_url` | Absent | [https://github.com/omacom/omarchy/blob/6a7e265491d655abe0a658e435b14dd3895d703f/manual/01-welcome-to-omarchy.md](https://github.com/omacom/omarchy/blob/6a7e265491d655abe0a658e435b14dd3895d703f/manual/01-welcome-to-omarchy.md) | The pinned README identifies the repository manual as authoritative. |
| `license_model` | `oss` | Unchanged | The existing model remains; see the scope and unresolved questions above. |
| `license_spdx` | Absent | Unchanged | Edition, implementation, package or binary terms do not support a new SPDX assignment for this record. |
| `maturity` | `unknown` | Unchanged | The evidence does not establish the catalogue's maturity class. |
| `status` | `needs-review` | Unchanged | The unresolved question above remains in the review queue. |
| `needs_review` | `true` | Unchanged | The unresolved question above remains in the review queue. |
| `verified_on` | `2026-08-03` | Unchanged | Retained pending completion of the outstanding review. |
| `repository_archived` | Absent | Unchanged | Repository metadata is tracked separately from the review decision or hosted service lifecycle. |

The `sources` field retains the following original entries in order.

- `legacy:devopstools_final.md#L1069`

The candidate appends these entries in order.

- [Publisher README with capabilities and operational boundaries](https://github.com/omacom/omarchy/blob/6a7e265491d655abe0a658e435b14dd3895d703f/README.md)
- [Pinned repository licence text](https://github.com/omacom/omarchy/blob/6a7e265491d655abe0a658e435b14dd3895d703f/LICENSE)
- [Supplementary publisher evidence at the same revision](https://github.com/omacom/omarchy/blob/6a7e265491d655abe0a658e435b14dd3895d703f/manual/48-security.md)
- [Publisher's pinned manual covering the distribution and desktop stack](https://github.com/omacom/omarchy/blob/6a7e265491d655abe0a658e435b14dd3895d703f/manual/01-welcome-to-omarchy.md)
- [Publisher release from 2026-11-05](https://github.com/omacom/omarchy/releases/tag/v4.5.0)

### `azure-storage-explorer` — RECLASSIFY

The publisher's docs and distributed release establish the GUI's identity. The pinned README limits the CC BY 4.0 and MIT grants to documentation and code in the issue-report repository. The distributed application's terms were not established from those sources or the product landing page, so the historical OSS classification becomes unknown and remains under review.

Confidence. High for the separate repository grants and documented app scope. The binary licence remains unverified.

Publisher revision `4ff5933cf52342bca125e0a0b80d15a69ad34901`. [Pinned README](https://github.com/microsoft/AzureStorageExplorer/blob/4ff5933cf52342bca125e0a0b80d15a69ad34901/README.md) · [Pinned root licence](https://github.com/microsoft/AzureStorageExplorer/blob/4ff5933cf52342bca125e0a0b80d15a69ad34901/LICENSE)

| Field | Baseline | Candidate | Evidence and scope |
| --- | --- | --- | --- |
| `summary` | `GUI tool for managing Azure Storage accounts, blobs, queues, and tables.` | `Microsoft desktop client for browsing and managing Azure Storage resources, including blobs, file shares, queues, and tables.` | The Microsoft Learn product guide identifies the standalone application, supported platforms and resources. |
| `use_when` | `["You need a visual way to browse/manage Azure Storage during development."]` | `["You want interactive storage operations and can grant the required permissions for the connection mode. Full subscription browsing requires management- and data-layer permissions."]` | Microsoft Learn distinguishes full subscription browsing from direct attachment to supported resources with data-layer permissions only. |
| `avoid_when` | `["CLI scripts or IaC already handle your storage operations."]` | `["You need unattended reproducible storage changes or must establish redistribution rights for the application before adoption."]` | The guide documents interactive operation. The pinned legal notice scopes the repository grants and leaves binary rights unestablished. |
| `deployment_models` | `[]` | `["local"]` | Microsoft Learn describes an installed standalone desktop app. |
| `official_url` | [https://azure.microsoft.com/en-us/products/storage/storage-explorer](https://azure.microsoft.com/en-us/products/storage/storage-explorer) | Unchanged | Current record value retained. |
| `repository_url` | [https://github.com/microsoft/AzureStorageExplorer](https://github.com/microsoft/AzureStorageExplorer) | Unchanged | Current record value retained. |
| `documentation_url` | Absent | [https://learn.microsoft.com/en-us/azure/storage/storage-explorer/vs-azure-tools-storage-manage-with-storage-explorer](https://learn.microsoft.com/en-us/azure/storage/storage-explorer/vs-azure-tools-storage-manage-with-storage-explorer) | The legacy Microsoft Learn article redirects to this publisher-managed canonical guide. |
| `license_model` | `oss` | `unknown` | The pinned README, documentation licence and repository code licence do not establish rights for the separately distributed desktop binary. |
| `license_spdx` | Absent | Unchanged | Edition, implementation, package or binary terms do not support a new SPDX assignment for this record. |
| `maturity` | `unknown` | Unchanged | The evidence does not establish the catalogue's maturity class. |
| `status` | `needs-review` | Unchanged | The unresolved question above remains in the review queue. |
| `needs_review` | `true` | Unchanged | The unresolved question above remains in the review queue. |
| `verified_on` | `2026-08-03` | Unchanged | Retained pending completion of the outstanding review. |
| `repository_archived` | Absent | Unchanged | Repository metadata is tracked separately from the review decision or hosted service lifecycle. |

The `sources` field retains the following original entries in order.

- `legacy:7_Development-Collaboration/README.md#L32`
- `legacy:devopstools_final.md#L1056`

The candidate appends these entries in order.

- [Publisher README with capabilities and operational boundaries](https://github.com/microsoft/AzureStorageExplorer/blob/4ff5933cf52342bca125e0a0b80d15a69ad34901/README.md)
- [Pinned repository licence text](https://github.com/microsoft/AzureStorageExplorer/blob/4ff5933cf52342bca125e0a0b80d15a69ad34901/LICENSE)
- [Supplementary publisher evidence at the same revision](https://github.com/microsoft/AzureStorageExplorer/blob/4ff5933cf52342bca125e0a0b80d15a69ad34901/LICENSE-CODE)
- [Microsoft Learn guide for the supported desktop client and permissions](https://learn.microsoft.com/en-us/azure/storage/storage-explorer/vs-azure-tools-storage-manage-with-storage-explorer)
- [Microsoft's release and support policy](https://learn.microsoft.com/en-us/azure/storage/common/storage-explorer-support-policy-lifecycle)
- [Publisher distribution release from 2026-11-06](https://github.com/microsoft/AzureStorageExplorer/releases/tag/v1.47.1)

## Generated outputs

- `README.md`
- `docs/catalog-statistics.json`
- `docs/categories/developer-experience-local-environments.md`
- `docs/lifecycle/develop.md`
- `docs/lifecycle/test.md`
- `docs/roles/developer-experience-engineer.md`
- `docs/roles/devops-engineer.md`

Generated views come from the canonical source using `python -m scripts.generate_docs`. The publication gate uses the full checks and structural verification from the Wave 46 kit.
