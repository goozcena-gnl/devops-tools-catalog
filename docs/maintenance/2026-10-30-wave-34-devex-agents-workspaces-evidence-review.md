# Wave 34 — DevEx coding agents and workspaces: bounded evidence patch

**Prepared:** 2026-10-30. **Status: CANONICAL PATCH STAGED; generator, Python 3.12 tests, CI and strict link audit NOT EXECUTED. NO Draft PR, Ready transition or merge approved.**

## Baseline and scope

- Tracking issue: https://github.com/goozcena-gnl/devops-tools-catalog/issues/155
- Frozen base `main`: `6c0f8235bb87795961c86834187f0969ca1ee25d`
- Original category YAML blob: `fab2ae8505afa6ecbdacd232e48b4c50200db10b`
- Exactly **10** selected existing IDs; **91** other record blocks preserved byte-for-byte and in order. No category, schema, workflow or link audit baseline changes.
- Global baseline: 1,425 canonical records, 847 active, 564 needs-review, 75 unknown license models. After 7 proposed clears and 3 retains, projected **854 active / 557 needs-review**, **not generator-verified**. Unknown licensing count may change; recompute from authoritative canonical data, never predict it as fact.

## Evidence-backed decisions (subject to independent review)

| ID | Proposed disposition | Primary evidence and boundary |
| --- | --- | --- |
| `aider` | **RETAIN** | [Aider-AI official source](https://github.com/Aider-AI/aider/tree/5dc9490bb35f9729ef2c95d00a19ccd30c26339c), [Apache LICENSE.txt](https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/LICENSE.txt), [v0.86.0](https://github.com/Aider-AI/aider/releases/tag/v0.86.0) dated 2025-08-09. Historic repo URL redirects. Root licence established; current stable security maintenance not proven. |
| `coder` | **CLEAR candidate** | [Coder source](https://github.com/coder/coder/tree/d5a03911dad4c0294e50581a97a7ee65bcf9b258), [AGPL root](https://github.com/coder/coder/blob/d5a03911dad4c0294e50581a97a7ee65bcf9b258/LICENSE), [README](https://github.com/coder/coder/blob/d5a03911dad4c0294e50581a97a7ee65bcf9b258/README.md) and [pricing](https://coder.com/pricing). Open-core commercial feature boundary: **do not** add a guessed exact SPDX suffix. |
| `codex` | **CLEAR candidate** | [Codex CLI source](https://github.com/openai/codex/tree/f752c97f7d0be0cbef5cece327f52a16ad6fb1c6), [Apache-2.0 LICENSE](https://github.com/openai/codex/blob/f752c97f7d0be0cbef5cece327f52a16ad6fb1c6/LICENSE), [README](https://github.com/openai/codex/blob/f752c97f7d0be0cbef5cece327f52a16ad6fb1c6/README.md). **Source is CLI**, not hosted Codex Web, model inference or subscription. |
| `continue` | **RETAIN** | [Publisher README](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/README.md) calls repo read-only/no longer actively maintained and describes final 2.0.0 despite GitHub unarchived metadata; [Apache licence](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/LICENSE). Do not imply active upstream support; lifecycle status review warranted separately. |
| `development-containers` | **CLEAR candidate** | [CC-BY-4.0 specification](https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/LICENSE), distinct [MIT reference CLI](https://github.com/devcontainers/cli/blob/d807cb27c195b6bc0e89d893fc20f44a30bf27ee/LICENSE.txt). Catalog identity is **specification**, not all devcontainer implementations. Set model documentation without assigning a conflated product SPDX. |
| `devpod` | **RETAIN** | [DevPod source](https://github.com/loft-sh/devpod/tree/5a0efcbff6610ab114b421f68a890739a452e66b), [MPL-2.0](https://github.com/loft-sh/devpod/blob/5a0efcbff6610ab114b421f68a890739a452e66b/LICENSE), [release history](https://github.com/loft-sh/devpod/releases); recently observed releases were prereleases from 2025, and current maintenance cadence remains unverified. |
| `github-codespaces` | **CLEAR candidate** | [GitHub product overview](https://docs.github.com/en/codespaces/overview), [billing](https://docs.github.com/en/billing/concepts/product-billing/github-codespaces), [official product page](https://github.com/features/codespaces). Hosted commercial SaaS with metered compute/storage and possible quotas; no product SPDX. Existing repository_url points to marketing page, do not promote that to source repository. |
| `hashicorp-vagrant` | **CLEAR candidate** | [Vagrant pinned source](https://github.com/hashicorp/vagrant/tree/dc55920a284544919340b975098b4ac9005b08b0), [BSL 1.1](https://github.com/hashicorp/vagrant/blob/dc55920a284544919340b975098b4ac9005b08b0/LICENSE) for versions >=2.4.3, with separate HCP Vagrant EOL notice in [README](https://github.com/hashicorp/vagrant/blob/dc55920a284544919340b975098b4ac9005b08b0/README.md). CLI remains distinct from HCP service and BSL is not OSI open-source. |
| `opencode` | **CLEAR candidate** | [OpenCode pinned source](https://github.com/anomalyco/opencode/tree/92b2ca0dd727942e00aba3523ed141d53e78ea28), [MIT LICENSE](https://github.com/anomalyco/opencode/blob/92b2ca0dd727942e00aba3523ed141d53e78ea28/LICENSE), [official README](https://github.com/anomalyco/opencode/blob/92b2ca0dd727942e00aba3523ed141d53e78ea28/README.md). Model/provider usage is separately billed/licensed. |
| `spec-kit` | **CLEAR candidate** | [GitHub source](https://github.com/github/spec-kit/tree/2a23a848f888de05f0107061d45232c485d6bae0), [MIT LICENSE](https://github.com/github/spec-kit/blob/2a23a848f888de05f0107061d45232c485d6bae0/LICENSE), [docs](https://github.github.com/spec-kit/). Templates/workflows, not a model or unreviewed autonomous executor. |

## Security and provenance controls

- AI agents: shell, filesystem and Git privileges, secret handling, third-party inference, model and token billing, prompt/plan/log exposure, sandbox and approval controls.
- Workspaces: cloud/Kubernetes credentials, devcontainer base-image supply chain, remote secrets, IAM/sandbox, idle shutdown/billing and guest/host access boundaries.
- Licences never extrapolated from specification to CLI, source to SaaS, or open-core to Premium. No synthetic licence models, unknown licensing remains unknown where evidence incomplete.
- The ten selected records preserve their `legacy:` source values **byte for byte** and in original order, and only append new primary-source references. The other 91 canonical record blocks remain unchanged.
- The implementation records `status: active` only for source-backed catalog classifications and is **not a claim of runtime security or production support**.

## Exact OLD / NEW field-level manifest

### `aider` — 10 raw field changes

**`repository_url`**

OLD:
```yaml
  repository_url: https://github.com/paul-gauthier/aider
```
NEW:
```yaml
  repository_url: "https://github.com/Aider-AI/aider"
```

**`summary`**

OLD:
```yaml
  summary: AI pair programming in the terminal.
```
NEW:
```yaml
  summary: "Apache-2.0 terminal AI pair programmer that edits Git-tracked code using separately configured model providers; latest identified stable release dates from August 2025."
```

**`use_when`**

OLD:
```yaml
  use_when:
  - '* You want terminal-based AI coding assistance that works with your existing editor and git workflow.'
```
NEW:
```yaml
  use_when:
  - "You want terminal-based AI assistance for reviewed Git changes and can control model-provider data access."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when:
  - '* You prefer IDE-integrated AI or need a visual interface.'
```
NEW:
```yaml
  avoid_when:
  - "You cannot send source code or prompts to selected model providers under your organization's data policy."
  - "You require independently verified frequent security fixes and recent stable releases; the most recent identified stable release is v0.86.0 from August 2025."
```

**`deployment_models`**

OLD:
```yaml
  deployment_models: []
```
NEW:
```yaml
  deployment_models:
  - "cli"
```

**`license_spdx`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  license_spdx: "Apache-2.0"
```

**`repository_archived`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_archived: false
```

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

**`status`**

OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "needs-review"
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:3_CI-CD-Automation/README.md#L174
  - legacy:devopstools_final.md#L411
```
NEW:
```yaml
  sources:
  - "legacy:3_CI-CD-Automation/README.md#L174"
  - "legacy:devopstools_final.md#L411"
  - "https://github.com/Aider-AI/aider/tree/5dc9490bb35f9729ef2c95d00a19ccd30c26339c"
  - "https://github.com/Aider-AI/aider/blob/5dc9490bb35f9729ef2c95d00a19ccd30c26339c/LICENSE.txt"
  - "https://github.com/Aider-AI/aider/releases/tag/v0.86.0"
  - "https://aider.chat/"
```

### `coder` — 10 raw field changes

**`summary`**

OLD:
```yaml
  summary: Self-hosted cloud development environments and AI development infrastructure with governance.
```
NEW:
```yaml
  summary: "Self-hosted Terraform-defined development workspaces and AI agent infrastructure, with AGPL-3.0 source and separate paid Premium features."
```

**`use_when`**

OLD:
```yaml
  use_when: []
```
NEW:
```yaml
  use_when:
  - "You need centrally governed cloud development workspaces defined with Terraform and optional coding agents on infrastructure you control."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when: []
```
NEW:
```yaml
  avoid_when:
  - "You assume paid Coder Premium features are included under the public source licence."
  - "You cannot isolate workspace privileges, provider credentials, model access or agents that execute untrusted code."
```

**`deployment_models`**

OLD:
```yaml
  deployment_models: []
```
NEW:
```yaml
  deployment_models:
  - "self-hosted"
```

**`license_model`**

OLD:
```yaml
  license_model: oss
```
NEW:
```yaml
  license_model: "open-core"
```

**`repository_archived`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_archived: false
```

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

**`status`**

OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "active"
```

**`needs_review`**

OLD:
```yaml
  needs_review: true
```
NEW:
```yaml
  needs_review: false
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:devopstools_final.md#L1057
```
NEW:
```yaml
  sources:
  - "legacy:devopstools_final.md#L1057"
  - "https://github.com/coder/coder/tree/d5a03911dad4c0294e50581a97a7ee65bcf9b258"
  - "https://github.com/coder/coder/blob/d5a03911dad4c0294e50581a97a7ee65bcf9b258/LICENSE"
  - "https://github.com/coder/coder/blob/d5a03911dad4c0294e50581a97a7ee65bcf9b258/README.md"
  - "https://coder.com/pricing"
```

### `codex` — 10 raw field changes

**`summary`**

OLD:
```yaml
  summary: Lightweight coding agent from OpenAI that runs in your terminal.
```
NEW:
```yaml
  summary: "Apache-2.0 open-source Codex CLI coding agent; model inference, IDE integrations and hosted Codex services have separate account and service terms."
```

**`use_when`**

OLD:
```yaml
  use_when: []
```
NEW:
```yaml
  use_when:
  - "You want an AI coding assistant in the terminal with explicit command approvals, sandbox boundaries and reviewed Git changes."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when: []
```
NEW:
```yaml
  avoid_when:
  - "You assume the Codex CLI Apache-2.0 licence covers hosted Codex services or third-party models."
  - "You cannot review model data flows, command permissions or secrets exposure before executing agent-generated changes."
```

**`deployment_models`**

OLD:
```yaml
  deployment_models: []
```
NEW:
```yaml
  deployment_models:
  - "cli"
```

**`license_spdx`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  license_spdx: "Apache-2.0"
```

**`repository_archived`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_archived: false
```

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

**`status`**

OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "active"
```

**`needs_review`**

OLD:
```yaml
  needs_review: true
```
NEW:
```yaml
  needs_review: false
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:devopstools_final.md#L414
```
NEW:
```yaml
  sources:
  - "legacy:devopstools_final.md#L414"
  - "https://github.com/openai/codex/tree/f752c97f7d0be0cbef5cece327f52a16ad6fb1c6"
  - "https://github.com/openai/codex/blob/f752c97f7d0be0cbef5cece327f52a16ad6fb1c6/LICENSE"
  - "https://github.com/openai/codex/blob/f752c97f7d0be0cbef5cece327f52a16ad6fb1c6/README.md"
```

### `continue` — 9 raw field changes

**`summary`**

OLD:
```yaml
  summary: Open-source AI code assistant.
```
NEW:
```yaml
  summary: "Apache-2.0 CLI and IDE coding assistant whose publisher declares the repository read-only and no longer actively maintained following its final 2.0.0 release."
```

**`use_when`**

OLD:
```yaml
  use_when:
  - '* You want an open-source, IDE-integrated AI assistant with flexibility to choose your own LLM backend.'
```
NEW:
```yaml
  use_when:
  - "You maintain a previously deployed Continue installation and can accept the publisher's end-of-maintenance statement."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when:
  - '* You want a polished, turnkey AI coding experience without setup.'
```
NEW:
```yaml
  avoid_when:
  - "You need an actively maintained assistant with reliable future fixes or vulnerability patches."
  - "You infer ongoing support from GitHub's unarchived status or recent repository metadata despite the explicit read-only statement."
```

**`deployment_models`**

OLD:
```yaml
  deployment_models: []
```
NEW:
```yaml
  deployment_models:
  - "cli"
```

**`license_spdx`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  license_spdx: "Apache-2.0"
```

**`repository_archived`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_archived: false
```

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

**`status`**

OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "needs-review"
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:3_CI-CD-Automation/README.md#L176
  - legacy:devopstools_final.md#L415
```
NEW:
```yaml
  sources:
  - "legacy:3_CI-CD-Automation/README.md#L176"
  - "legacy:devopstools_final.md#L415"
  - "https://github.com/continuedev/continue/tree/5522c6f44ca0ac3528b37244818fbfa39b5af470"
  - "https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/LICENSE"
  - "https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/README.md"
  - "https://github.com/continuedev/continue/releases"
```

### `development-containers` — 9 raw field changes

**`summary`**

OLD:
```yaml
  summary: Open specification for defining reproducible, containerized development environments (devcontainers).
```
NEW:
```yaml
  summary: "Open development-container specification for reproducible dev environments; the specification is CC-BY-4.0 and its separately licensed reference CLI is MIT."
```

**`documentation_url`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  documentation_url: "https://containers.dev/"
```

**`use_when`**

OLD:
```yaml
  use_when: []
```
NEW:
```yaml
  use_when:
  - "You need a portable devcontainer.json definition usable with compatible tools, editors and container runtimes."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when: []
```
NEW:
```yaml
  avoid_when:
  - "You expect the specification alone to supply a working runtime or guaranteed sandbox isolation."
  - "You assume that the CC-BY-4.0 specification, MIT reference CLI and third-party images all share the same licence."
```

**`license_model`**

OLD:
```yaml
  license_model: oss
```
NEW:
```yaml
  license_model: "documentation"
```

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

**`status`**

OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "active"
```

**`needs_review`**

OLD:
```yaml
  needs_review: true
```
NEW:
```yaml
  needs_review: false
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:devopstools_final.md#L1058
```
NEW:
```yaml
  sources:
  - "legacy:devopstools_final.md#L1058"
  - "https://github.com/devcontainers/spec/tree/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421"
  - "https://github.com/devcontainers/spec/blob/c95ffeed1d059abfe9ffbe79762dc2fa4e7c2421/LICENSE"
  - "https://github.com/devcontainers/cli/tree/d807cb27c195b6bc0e89d893fc20f44a30bf27ee"
  - "https://github.com/devcontainers/cli/blob/d807cb27c195b6bc0e89d893fc20f44a30bf27ee/LICENSE.txt"
  - "https://containers.dev/"
```

### `devpod` — 9 raw field changes

**`summary`**

OLD:
```yaml
  summary: Open-source dev environments that can run locally or on remote providers.
```
NEW:
```yaml
  summary: "MPL-2.0 devcontainer workspace client connecting local IDEs to local Docker, remote SSH, Kubernetes and cloud providers; recent release support remains uncertain."
```

**`use_when`**

OLD:
```yaml
  use_when:
  - You want reproducible dev containers across local Docker, SSH hosts, or cloud VMs without vendor lock-in.
```
NEW:
```yaml
  use_when:
  - "You want provider-agnostic containerized development environments across local and remote infrastructure."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when:
  - Your team is already standardized on GitHub Codespaces or Gitpod.
```
NEW:
```yaml
  avoid_when:
  - "You rely on guaranteed current upstream security maintenance; recent stable release support was not established."
  - "You cannot protect cloud or Kubernetes provider credentials and enforce workspace image trust."
```

**`deployment_models`**

OLD:
```yaml
  deployment_models: []
```
NEW:
```yaml
  deployment_models:
  - "local"
  - "self-hosted"
```

**`license_spdx`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  license_spdx: "MPL-2.0"
```

**`repository_archived`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_archived: false
```

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

**`status`**

OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "needs-review"
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:7_Development-Collaboration/README.md#L33
  - legacy:devopstools_final.md#L1059
```
NEW:
```yaml
  sources:
  - "legacy:7_Development-Collaboration/README.md#L33"
  - "legacy:devopstools_final.md#L1059"
  - "https://github.com/loft-sh/devpod/tree/5a0efcbff6610ab114b421f68a890739a452e66b"
  - "https://github.com/loft-sh/devpod/blob/5a0efcbff6610ab114b421f68a890739a452e66b/LICENSE"
  - "https://github.com/loft-sh/devpod/releases"
  - "https://github.com/loft-sh/devpod/blob/5a0efcbff6610ab114b421f68a890739a452e66b/README.md"
```

### `github-codespaces` — 11 raw field changes

**`summary`**

OLD:
```yaml
  summary: Hosted cloud development environments integrated with GitHub.
```
NEW:
```yaml
  summary: "GitHub-hosted cloud development environments billed for compute and storage, with account-specific included quotas and no product-wide open-source licence."
```

**`official_url`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  official_url: "https://github.com/features/codespaces"
```

**`use_when`**

OLD:
```yaml
  use_when:
  - Your team is on GitHub and wants zero-setup, cloud-based dev environments.
```
NEW:
```yaml
  use_when:
  - "You need GitHub-integrated hosted development environments with standardized devcontainer configuration and approved spending controls."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when:
  - You need self-hosted control or want to minimize per-seat cloud costs.
```
NEW:
```yaml
  avoid_when:
  - "You require a self-hosted control plane or zero-cost unlimited compute and storage."
  - "You cannot grant GitHub cloud workspaces the needed repository, network or secrets access under approved organization policies."
```

**`deployment_models`**

OLD:
```yaml
  deployment_models: []
```
NEW:
```yaml
  deployment_models:
  - "hosted-saas"
```

**`license_model`**

OLD:
```yaml
  license_model: unknown
```
NEW:
```yaml
  license_model: "commercial"
```

**`commercial_offering`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  commercial_offering: true
```

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

**`status`**

OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "active"
```

**`needs_review`**

OLD:
```yaml
  needs_review: true
```
NEW:
```yaml
  needs_review: false
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:7_Development-Collaboration/README.md#L34
  - legacy:devopstools_final.md#L1061
```
NEW:
```yaml
  sources:
  - "legacy:7_Development-Collaboration/README.md#L34"
  - "legacy:devopstools_final.md#L1061"
  - "https://docs.github.com/en/codespaces/overview"
  - "https://docs.github.com/en/billing/concepts/product-billing/github-codespaces"
  - "https://github.com/features/codespaces"
```

### `hashicorp-vagrant` — 10 raw field changes

**`summary`**

OLD:
```yaml
  summary: Tool for building and managing virtual machine environments (BUSL-1.1).
```
NEW:
```yaml
  summary: "Version-dependent source-available VM development environment CLI: Vagrant 2.4.3+ uses IBM Business Source License 1.1; HCP Vagrant service deprecation is separate."
```

**`use_when`**

OLD:
```yaml
  use_when:
  - You need full VM-based dev environments (e.g., kernel work, multi-node clusters).
```
NEW:
```yaml
  use_when:
  - "You need portable, provider-backed local or remote virtual machine development and test environments."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when:
  - Containers suffice—VMs are heavier and slower to provision.
```
NEW:
```yaml
  avoid_when:
  - "You assume Business Source License 1.1 is OSI-approved open source or that all historic Vagrant versions share the same terms."
  - "You confuse the HCP Vagrant service deprecation with the continuing Vagrant CLI."
  - "Containers are adequate and you cannot justify VM overhead or privileged hypervisor access."
```

**`deployment_models`**

OLD:
```yaml
  deployment_models: []
```
NEW:
```yaml
  deployment_models:
  - "cli"
```

**`license_model`**

OLD:
```yaml
  license_model: source-available
```
NEW:
```yaml
  license_model: "source-available"
```

**`repository_archived`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_archived: false
```

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

**`status`**

OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "active"
```

**`needs_review`**

OLD:
```yaml
  needs_review: true
```
NEW:
```yaml
  needs_review: false
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:7_Development-Collaboration/README.md#L35
  - legacy:devopstools_final.md#L1063
```
NEW:
```yaml
  sources:
  - "legacy:7_Development-Collaboration/README.md#L35"
  - "legacy:devopstools_final.md#L1063"
  - "https://github.com/hashicorp/vagrant/tree/dc55920a284544919340b975098b4ac9005b08b0"
  - "https://github.com/hashicorp/vagrant/blob/dc55920a284544919340b975098b4ac9005b08b0/LICENSE"
  - "https://github.com/hashicorp/vagrant/blob/dc55920a284544919340b975098b4ac9005b08b0/README.md"
  - "https://developer.hashicorp.com/hcp/docs/vagrant/hcp-vagrant-eol"
```

### `opencode` — 11 raw field changes

**`summary`**

OLD:
```yaml
  summary: Open-source AI coding agent.
```
NEW:
```yaml
  summary: "MIT-licensed open-source coding agent with independently billed or licensed model providers and optional online services."
```

**`repository_url`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_url: "https://github.com/anomalyco/opencode"
```

**`use_when`**

OLD:
```yaml
  use_when: []
```
NEW:
```yaml
  use_when:
  - "You want an open-source coding agent and can evaluate model provider, shell tools and repository permissions."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when: []
```
NEW:
```yaml
  avoid_when:
  - "You equate the agent's MIT source licence with free inference, private cloud services or unrestricted third-party model rights."
  - "You cannot approve prompt/code disclosure and restrict the agent's file, shell and credential access."
```

**`deployment_models`**

OLD:
```yaml
  deployment_models: []
```
NEW:
```yaml
  deployment_models:
  - "cli"
```

**`license_spdx`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  license_spdx: "MIT"
```

**`repository_archived`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_archived: false
```

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

**`status`**

OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "active"
```

**`needs_review`**

OLD:
```yaml
  needs_review: true
```
NEW:
```yaml
  needs_review: false
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:devopstools_final.md#L417
```
NEW:
```yaml
  sources:
  - "legacy:devopstools_final.md#L417"
  - "https://github.com/anomalyco/opencode/tree/92b2ca0dd727942e00aba3523ed141d53e78ea28"
  - "https://github.com/anomalyco/opencode/blob/92b2ca0dd727942e00aba3523ed141d53e78ea28/LICENSE"
  - "https://github.com/anomalyco/opencode/blob/92b2ca0dd727942e00aba3523ed141d53e78ea28/README.md"
  - "https://opencode.ai"
```

### `spec-kit` — 11 raw field changes

**`summary`**

OLD:
```yaml
  summary: Toolkit from GitHub for getting started with Spec-Driven Development.
```
NEW:
```yaml
  summary: "MIT-licensed GitHub toolkit for specification-driven development workflows and templates that integrate with independently operated coding agents."
```

**`documentation_url`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  documentation_url: "https://github.github.com/spec-kit/"
```

**`use_when`**

OLD:
```yaml
  use_when: []
```
NEW:
```yaml
  use_when:
  - "You want a repeatable specification-to-plan-to-task workflow before delegating coding to an AI agent."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when: []
```
NEW:
```yaml
  avoid_when:
  - "You expect Spec Kit to run, validate or secure generated application code autonomously."
  - "You assume external coding agents, models and hosted providers share Spec Kit's MIT licence."
```

**`deployment_models`**

OLD:
```yaml
  deployment_models: []
```
NEW:
```yaml
  deployment_models:
  - "cli"
```

**`license_spdx`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  license_spdx: "MIT"
```

**`repository_archived`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_archived: false
```

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

**`status`**

OLD:
```yaml
  status: needs-review
```
NEW:
```yaml
  status: "active"
```

**`needs_review`**

OLD:
```yaml
  needs_review: true
```
NEW:
```yaml
  needs_review: false
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:devopstools_final.md#L423
```
NEW:
```yaml
  sources:
  - "legacy:devopstools_final.md#L423"
  - "https://github.com/github/spec-kit/tree/2a23a848f888de05f0107061d45232c485d6bae0"
  - "https://github.com/github/spec-kit/blob/2a23a848f888de05f0107061d45232c485d6bae0/LICENSE"
  - "https://github.com/github/spec-kit/blob/2a23a848f888de05f0107061d45232c485d6bae0/README.md"
  - "https://github.github.com/spec-kit/"
```


## Mandatory execution gates (NOT YET PASSED)

1. Independently review every exact OLD/NEW field and current publisher evidence, including URL uniqueness and expiry/redirect effects. Preserve 91 unrelated source records verbatim.
2. In a locally accessible Python 3.12 isolated pinned environment, regenerate docs: `python -m scripts.generate_docs`, `python -m scripts.generate_docs --check`; validate catalog: `python -m scripts.validate_catalog`, `python -m scripts.review_debt --format json`; run `python -m ruff check scripts tests`, `python -m ruff format --check scripts tests`, `python -m pip check`, full `python -m pytest`; `git diff --check`.
3. Validate count 1,425 and derived counters, expected statuses and all 10 changed IDs, preserve 91 untouched, exact SHA preflight and allowlist limited to YAML, this evidence report and generator-created files only.
4. **Do not** create Draft PR until tests and generator succeed. When they do, commit generated outputs, push without force; open **Draft PR only**.
5. Require 8 checks (Catalogue quality, Gitleaks, Plumber, CodeQL where applicable) and separately dispatched strict Full link audit on **final PR SHA**; `blocking_new: 0`, `strict_result: PASS`, report `blocking_known` separately. Do not modify baseline to force green.
6. Human review and explicit authorization before Ready; separate explicit approval before merge; never enable auto-merge. Post-merge CI before issue closure.

**Execution boundary:** GitHub connector can commit repository files, but cannot run local Windows/Python 3.12 validation. No generated docs or passing tests claimed. This stage is intentionally **not merge-ready**.

## Provenance serialization repair (2026-10-30)

The initial Wave 34 staging commit accidentally serialized the **first** `legacy:` source of each selected record as `- legacy:...` inside the YAML string. The guarded PowerShell 5.1 preflight correctly blocked both read-only validation and `-Apply` (`legacy provenance changed: continue`). This commit corrects **exactly ten** first-source values back to their original string content, preserving every pre-existing `legacy:` source in order. The exact OLD/NEW field manifest above is corrected to match the new YAML. None of the 91 out-of-scope records, status decisions or additional primary evidence is altered. The local deterministic generator, lint, pytest and strict link audit still have **NOT** been executed on this repaired HEAD; do not open a Draft PR before their successful completion.
