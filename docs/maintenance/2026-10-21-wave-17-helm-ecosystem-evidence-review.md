# Wave 17 — Helm delivery, testing and supply chain: evidence review

**Review date:** 2026-10-21 · **Base main:** `7abf9625affd7652ef173f0c4d2c924dae12b6b9` · **Branch:** `maintenance/wave-17-helm-delivery-evidence-review` · **Issue:** [#123](https://github.com/goozcena-gnl/devops-tools-catalog/issues/123).

**Provisional result:** 10 reviewed, **8 cleared / 2 retained**, total canonical records 1,425 unchanged, review flags **673 → 665** pending generated documentation and CI. This is an evidence review in progress, not completed validation.

The ten records below are the only canonical data changes. They retain their stable IDs and legacy provenance. Licence boundaries and upstream status were checked against GitHub upstream repository metadata, README, the actual upstream LICENSE text (all ten records), and releases on 2026-10-21. Nelm's LICENSE explicitly distinguishes Apache-2.0 core code from CC BY-SA 4.0 documentation and separately licensed third-party components; `license_spdx` applies only to the core code. Repo visibility and last-push dates do not alone prove lifecycle support.

## Decisions

| Record | Decision | Key concern |
|---|---|---|
| `helm-chart-testing` | **CLEAR (provisional)** | Corrected confusion with helm.sh built-in chart test hooks; ct CLI has independent releases and CI docs |
| `helm-diff` | **CLEAR (provisional)** | Official upstream source, bounded functionality and recent release evidence reviewed |
| `helm-secrets` | **CLEAR (provisional)** | Plugin decrypts SOPS values or resolves secret references, not a secrets database; secrets exposure caveats |
| `helm-mapkubeapis` | **CLEAR (provisional)** | Mutates Helm 3 release metadata, not source charts or arbitrary cluster objects |
| `helmfile` | **CLEAR (provisional)** | Official upstream source, bounded functionality and recent release evidence reviewed |
| `nelm` | **CLEAR (provisional)** | Apache-2.0 code, CC BY-SA 4.0 docs and third-party component grants; license_spdx represents core code only |
| `helm-unittest` | **CLEAR (provisional)** | Official upstream source, bounded functionality and recent release evidence reviewed |
| `helm-docs` | **CLEAR (provisional)** | Core GPL-3.0 grant differs from other Helm utilities; last published release 2024-07 but source activity in 2026 |
| `helmper` | **RETAIN REVIEW** | Upstream still labels beta; last release 2025-10-31 and last push 2026-02-26; stable production support not established |
| `helm-chart-generator` | **RETAIN REVIEW** | Alpha v1.0.0-alpha released 2024-06-27, last push 2025-03-01; active maintenance not established |

## Complete changed-field ledger

Multi-line YAML arrays below are serialized by joining the full folded items with `; `. A before/after value is not shortened. `∅` means absent in source.

### `helm-chart-testing`

Sources: [https://github.com/helm/chart-testing](https://github.com/helm/chart-testing) · [https://github.com/helm/chart-testing/releases](https://github.com/helm/chart-testing/releases) · [https://github.com/helm/chart-testing/blob/main/README.md](https://github.com/helm/chart-testing/blob/main/README.md) · [https://github.com/helm/chart-testing/blob/main/LICENSE](https://github.com/helm/chart-testing/blob/main/LICENSE).

| Field | Before | After |
|---|---|---|
| `summary` | `Tooling for testing Helm charts.` | `Helm chart-testing (ct) CLI lints changed charts and optionally tests chart installation in Kubernetes CI; separate from Helm chart test hooks.` |
| `official_url` | `https://helm.sh/docs/topics/chart_tests` | `https://github.com/helm/chart-testing` |
| `use_when` | `You maintain Helm chart repositories and need CI-based lint and install testing.` | `You maintain Helm chart repositories and need CI lint checks and optional Kubernetes installation tests on changed charts.` |
| `avoid_when` | `You only consume upstream charts without modification.` | `You require only Helm's built-in chart test hook support; ct is a separate CLI.; You cannot provision a safe test cluster for install tests or verify the version-specific CI prerequisites.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L95; legacy:devopstools_final.md#L567` | `legacy:4_Kubernetes-Containers/README.md#L95; legacy:devopstools_final.md#L567; https://github.com/helm/chart-testing; https://github.com/helm/chart-testing/releases; https://github.com/helm/chart-testing/blob/main/README.md; https://github.com/helm/chart-testing/blob/main/LICENSE` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://github.com/helm/chart-testing/blob/main/README.md` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

### `helm-diff`

Sources: [https://github.com/databus23/helm-diff](https://github.com/databus23/helm-diff) · [https://github.com/databus23/helm-diff/releases](https://github.com/databus23/helm-diff/releases) · [https://github.com/databus23/helm-diff/blob/master/README.md](https://github.com/databus23/helm-diff/blob/master/README.md) · [https://github.com/databus23/helm-diff/blob/master/LICENSE](https://github.com/databus23/helm-diff/blob/master/LICENSE).

| Field | Before | After |
|---|---|---|
| `summary` | `Helm plugin to show differences between releases.` | `Helm plugin showing a diff between a deployed release and rendered upgrade manifests, including revision comparisons.` |
| `use_when` | `You want to preview changes before \`helm upgrade\` to catch unexpected diffs.` | `You need to preview manifest changes before upgrading a Helm release and can review sensitive output carefully.` |
| `avoid_when` | `You use GitOps tools (ArgoCD/Flux) that already show diffs before sync.` | `You assume a textual diff guarantees a safe live deployment or that redaction prevents all secrets from leaking.; Your GitOps process already performs authoritative controller-side diff and approval checks.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L96; legacy:devopstools_final.md#L568` | `legacy:4_Kubernetes-Containers/README.md#L96; legacy:devopstools_final.md#L568; https://github.com/databus23/helm-diff; https://github.com/databus23/helm-diff/releases; https://github.com/databus23/helm-diff/blob/master/README.md; https://github.com/databus23/helm-diff/blob/master/LICENSE` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://github.com/databus23/helm-diff/blob/master/README.md` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

### `helm-secrets`

Sources: [https://github.com/jkroepke/helm-secrets](https://github.com/jkroepke/helm-secrets) · [https://github.com/jkroepke/helm-secrets/releases](https://github.com/jkroepke/helm-secrets/releases) · [https://github.com/jkroepke/helm-secrets/wiki/Usage](https://github.com/jkroepke/helm-secrets/wiki/Usage) · [https://github.com/jkroepke/helm-secrets/blob/main/LICENSE](https://github.com/jkroepke/helm-secrets/blob/main/LICENSE).

| Field | Before | After |
|---|---|---|
| `summary` | `Manage secrets with Helm charts.` | `Helm plugin that decrypts encrypted values using SOPS or resolves secret references via supported external backends; not a secrets store.` |
| `use_when` | `You need to encrypt secrets in Helm values files using SOPS/Vault for GitOps.` | `You need to supply encrypted Helm values through SOPS or supported secret-manager integrations during controlled deployment.; You can manage plugin permissions, backend credentials and plaintext handling in CI or Argo CD integrations.` |
| `avoid_when` | `You use External Secrets Operator or Sealed Secrets for secret management.` | `You need a standalone secret storage service or guaranteed prevention of plaintext exposure during rendering.; You cannot protect temporary decrypted content, debug output or credentials consumed by the deployment process.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L99; legacy:devopstools_final.md#L571` | `legacy:4_Kubernetes-Containers/README.md#L99; legacy:devopstools_final.md#L571; https://github.com/jkroepke/helm-secrets; https://github.com/jkroepke/helm-secrets/releases; https://github.com/jkroepke/helm-secrets/wiki/Usage; https://github.com/jkroepke/helm-secrets/blob/main/LICENSE` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://github.com/jkroepke/helm-secrets/wiki/Usage` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

### `helm-mapkubeapis`

Sources: [https://github.com/helm/helm-mapkubeapis](https://github.com/helm/helm-mapkubeapis) · [https://github.com/helm/helm-mapkubeapis/releases](https://github.com/helm/helm-mapkubeapis/releases) · [https://github.com/helm/helm-mapkubeapis/blob/main/README.md](https://github.com/helm/helm-mapkubeapis/blob/main/README.md) · [https://github.com/helm/helm-mapkubeapis/blob/main/LICENSE](https://github.com/helm/helm-mapkubeapis/blob/main/LICENSE).

| Field | Before | After |
|---|---|---|
| `summary` | `Helm plugin for API version migration.` | `Helm 3 plugin migrating deprecated Kubernetes API references stored in Helm release metadata; source charts must be migrated separately.` |
| `use_when` | `Upgrading Kubernetes and Helm releases reference deprecated/removed API versions.` | `You must repair Helm release metadata that references removed Kubernetes APIs before a compatible upgrade.` |
| `avoid_when` | `Your charts already target current API versions.` | `You expect the plugin to update source charts, arbitrary Kubernetes resources or all unsupported API versions.; You cannot inspect and back up the release state before an in-place metadata rewrite.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L98; legacy:devopstools_final.md#L570` | `legacy:4_Kubernetes-Containers/README.md#L98; legacy:devopstools_final.md#L570; https://github.com/helm/helm-mapkubeapis; https://github.com/helm/helm-mapkubeapis/releases; https://github.com/helm/helm-mapkubeapis/blob/main/README.md; https://github.com/helm/helm-mapkubeapis/blob/main/LICENSE` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://github.com/helm/helm-mapkubeapis/blob/main/README.md` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

### `helmfile`

Sources: [https://github.com/helmfile/helmfile](https://github.com/helmfile/helmfile) · [https://github.com/helmfile/helmfile/releases](https://github.com/helmfile/helmfile/releases) · [https://helmfile.readthedocs.io/en/latest/](https://helmfile.readthedocs.io/en/latest/) · [https://github.com/helmfile/helmfile/blob/main/LICENSE](https://github.com/helmfile/helmfile/blob/main/LICENSE).

| Field | Before | After |
|---|---|---|
| `summary` | `Declarative Helm deployments.` | `Declarative Helm release orchestration using state files and environments, with integrations for charts and Kustomize; not itself a GitOps reconciliation controller.` |
| `use_when` | `You manage multiple Helm releases across environments and want declarative, diff-able state.` | `You coordinate Helm releases across environments through reviewed declarative state and diffable deployment commands.` |
| `avoid_when` | `You deploy a single chart or already use ArgoCD/Flux for Helm release management.` | `You expect continuous cluster reconciliation without external automation such as Argo CD, Flux or CI.; You have one simple chart and do not need additional orchestration state or templating.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L93; legacy:devopstools_final.md#L565` | `legacy:4_Kubernetes-Containers/README.md#L93; legacy:devopstools_final.md#L565; https://github.com/helmfile/helmfile; https://github.com/helmfile/helmfile/releases; https://helmfile.readthedocs.io/en/latest/; https://github.com/helmfile/helmfile/blob/main/LICENSE` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://helmfile.readthedocs.io/en/latest/` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `MIT` |

### `nelm`

Sources: [https://github.com/werf/nelm](https://github.com/werf/nelm) · [https://github.com/werf/nelm/releases](https://github.com/werf/nelm/releases) · [https://github.com/werf/nelm/blob/main/README.md](https://github.com/werf/nelm/blob/main/README.md) · [https://github.com/werf/nelm/blob/main/LICENSE](https://github.com/werf/nelm/blob/main/LICENSE).

| Field | Before | After |
|---|---|---|
| `summary` | `Helm-compatible Kubernetes deployment tool and Helm 4 alternative with plan previews, improved CRD handling, and secret workflows.` | `Helm-compatible Kubernetes deployment tool and Helm alternative with release planning and resource lifecycle management; not proven a drop-in replacement for every Helm plugin.` |
| `use_when` | `[]` | `You want to evaluate modern Helm-compatible release deployment and planning with a controlled compatibility pilot.` |
| `avoid_when` | `[]` | `You assume universal Helm plugin or chart interoperability without testing current Nelm and Helm versions.; You infer that all documentation and bundled third-party components are Apache-2.0 licensed; repository docs use CC BY-SA 4.0.` |
| `maturity` | `unknown` | `growing` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:devopstools_final.md#L611` | `legacy:devopstools_final.md#L611; https://github.com/werf/nelm; https://github.com/werf/nelm/releases; https://github.com/werf/nelm/blob/main/README.md; https://github.com/werf/nelm/blob/main/LICENSE` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://github.com/werf/nelm/blob/main/README.md` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

### `helm-unittest`

Sources: [https://github.com/helm-unittest/helm-unittest](https://github.com/helm-unittest/helm-unittest) · [https://github.com/helm-unittest/helm-unittest/releases](https://github.com/helm-unittest/helm-unittest/releases) · [https://github.com/helm-unittest/helm-unittest/blob/main/DOCUMENT.md](https://github.com/helm-unittest/helm-unittest/blob/main/DOCUMENT.md) · [https://github.com/helm-unittest/helm-unittest/blob/main/LICENSE](https://github.com/helm-unittest/helm-unittest/blob/main/LICENSE).

| Field | Before | After |
|---|---|---|
| `summary` | `Unit test framework for Helm charts.` | `Helm plugin for YAML-defined unit and snapshot tests of rendered chart templates without deploying resources to a Kubernetes cluster.` |
| `use_when` | `You want to test rendered Helm templates without deploying to a cluster.` | `You need repeatable Helm template assertions and snapshot checks without provisioning a Kubernetes cluster.` |
| `avoid_when` | `Simple \`helm template\` + diff checks are sufficient for your CI pipeline.` | `You require actual deployment, admission, network, runtime or integration testing in a live cluster.; You disable Helm 4 plugin provenance checks without verifying the release artifact and its signing instructions.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L100; legacy:devopstools_final.md#L572` | `legacy:4_Kubernetes-Containers/README.md#L100; legacy:devopstools_final.md#L572; https://github.com/helm-unittest/helm-unittest; https://github.com/helm-unittest/helm-unittest/releases; https://github.com/helm-unittest/helm-unittest/blob/main/DOCUMENT.md; https://github.com/helm-unittest/helm-unittest/blob/main/LICENSE` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://github.com/helm-unittest/helm-unittest/blob/main/DOCUMENT.md` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `MIT` |

### `helm-docs`

Sources: [https://github.com/norwoodj/helm-docs](https://github.com/norwoodj/helm-docs) · [https://github.com/norwoodj/helm-docs/releases](https://github.com/norwoodj/helm-docs/releases) · [https://github.com/norwoodj/helm-docs/blob/master/README.md](https://github.com/norwoodj/helm-docs/blob/master/README.md) · [https://github.com/norwoodj/helm-docs/blob/master/LICENSE](https://github.com/norwoodj/helm-docs/blob/master/LICENSE).

| Field | Before | After |
|---|---|---|
| `summary` | `Generate documentation for Helm charts.` | `GPL-3.0 Helm chart documentation generator deriving README tables and descriptions from chart metadata, values and comments.` |
| `use_when` | `You want auto-generated README docs from \`values.yaml\` comments.` | `You maintain Helm charts and want templated Markdown documentation derived from values.yaml and chart metadata.` |
| `avoid_when` | `Your charts are internal with minimal consumers and hand-written docs suffice.` | `You expect documentation generation to validate Kubernetes resource semantics or test Helm chart behavior.; You need redistribution rights incompatible with the GPL-3.0 licence of the tool.` |
| `maturity` | `unknown` | `established` |
| `status` | `needs-review` | `active` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L97; legacy:devopstools_final.md#L569` | `legacy:4_Kubernetes-Containers/README.md#L97; legacy:devopstools_final.md#L569; https://github.com/norwoodj/helm-docs; https://github.com/norwoodj/helm-docs/releases; https://github.com/norwoodj/helm-docs/blob/master/README.md; https://github.com/norwoodj/helm-docs/blob/master/LICENSE` |
| `needs_review` | `true` | `false` |
| `documentation_url` | ∅ | `https://github.com/norwoodj/helm-docs/blob/master/README.md` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `GPL-3.0-only` |

### `helmper`

Sources: [https://github.com/ChristofferNissen/helmper](https://github.com/ChristofferNissen/helmper) · [https://github.com/ChristofferNissen/helmper/releases](https://github.com/ChristofferNissen/helmper/releases) · [https://christoffernissen.github.io/helmper/](https://christoffernissen.github.io/helmper/) · [https://github.com/ChristofferNissen/helmper/blob/main/LICENSE](https://github.com/ChristofferNissen/helmper/blob/main/LICENSE).

| Field | Before | After |
|---|---|---|
| `summary` | `Helm helper for mirroring charts and images to OCI registries.` | `Beta-stage tool for mirroring Helm charts and container images to OCI registries, with optional vulnerability scanning, patching and signing integrations.` |
| `use_when` | `You need to mirror Helm charts and their images into air-gapped or private registries.` | `You are piloting Helm chart and container-image mirroring into private or air-gapped OCI registries.` |
| `avoid_when` | `You pull charts directly from public registries without mirroring requirements.` | `You require stable production support guarantees from a project that still describes itself as beta.; You assume optional Trivy, Copacetic and Cosign integrations automatically establish supply-chain safety.; You cannot protect registry credentials or validate imported and rewritten artifacts.` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L94; legacy:devopstools_final.md#L566` | `legacy:4_Kubernetes-Containers/README.md#L94; legacy:devopstools_final.md#L566; https://github.com/ChristofferNissen/helmper; https://github.com/ChristofferNissen/helmper/releases; https://christoffernissen.github.io/helmper/; https://github.com/ChristofferNissen/helmper/blob/main/LICENSE` |
| `documentation_url` | ∅ | `https://christoffernissen.github.io/helmper/` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

### `helm-chart-generator`

Sources: [https://github.com/ravaga/helm-chart-generator](https://github.com/ravaga/helm-chart-generator) · [https://github.com/ravaga/helm-chart-generator/releases](https://github.com/ravaga/helm-chart-generator/releases) · [https://github.com/ravaga/helm-chart-generator/blob/main/README.md](https://github.com/ravaga/helm-chart-generator/blob/main/README.md) · [https://github.com/ravaga/helm-chart-generator/blob/main/LICENSE](https://github.com/ravaga/helm-chart-generator/blob/main/LICENSE).

| Field | Before | After |
|---|---|---|
| `summary` | `Tool for generating Helm charts from templates.` | `Alpha-stage interactive generator scaffolding customizable Helm charts; current maintenance and Kubernetes compatibility need confirmation.` |
| `use_when` | `You want to scaffold new Helm charts quickly with consistent structure.` | `You want to experiment with generating starter Helm charts through an interactive CLI or container.` |
| `avoid_when` | `'\`helm create\` or an existing chart boilerplate covers your needs.'` | `You require verified current Kubernetes/Helm compatibility or a stable maintenance and security release process.; The supported helm create command or an existing chart template already covers your scaffolding needs.` |
| `maturity` | `unknown` | `experimental` |
| `verified_on` | `'2026-08-03'` | `'2026-10-21'` |
| `sources` | `legacy:4_Kubernetes-Containers/README.md#L92; legacy:devopstools_final.md#L564` | `legacy:4_Kubernetes-Containers/README.md#L92; legacy:devopstools_final.md#L564; https://github.com/ravaga/helm-chart-generator; https://github.com/ravaga/helm-chart-generator/releases; https://github.com/ravaga/helm-chart-generator/blob/main/README.md; https://github.com/ravaga/helm-chart-generator/blob/main/LICENSE` |
| `documentation_url` | ∅ | `https://github.com/ravaga/helm-chart-generator/blob/main/README.md` |
| `repository_archived` | ∅ | `false` |
| `license_spdx` | ∅ | `Apache-2.0` |

## Inconclusive outcomes

- `helmper` remains `needs_review: true`: beta feature guarantees, supported release/maintenance and security implications of optional signing and patching have not been established.
- `helm-chart-generator` remains `needs_review: true`: prerelease/alpha version and stale upstream activity do not support production maturity and compatibility claims.

## Required pre-merge gates

1. Run `python -m scripts.generate_docs` and commit regenerated README, category/role/lifecycle/statistics views; verify generator `--check`.
2. Run locked Python 3.12 environment, Ruff lint/format, full pytest, catalogue validation, debt inventory and `git diff --check`; reconcile actual counters and any historically pinned regression expectations.
3. Check **fresh strict full-catalogue links** on final head. Keep the six reviewed baseline exceptions unchanged, require `blocking_new: 0`, `strict_result: PASS`. HTTP/TLS/rate-limit observations are dated, not lifecycle changes.
4. Inspect all CI/security checks, fix reviewer comments, update PR with exact final head and audit artifacts. **Do not merge** without explicit human decision.
