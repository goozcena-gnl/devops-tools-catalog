# Wave 35 — Cloud AI, MCP and MLOps evidence review

**2026-10-30. CANONICAL EVIDENCE PATCH ONLY; docs generator, tests, CI and strict audit have NOT run. NOT READY FOR PR.**

- Tracking: https://github.com/goozcena-gnl/devops-tools-catalog/issues/157
- Frozen base SHA: `8c5cb45ff2ee0bd3245bc619beaa39008b4467e6`
- Original canonical file Git blob SHA: `a820dacfa7b1acf8c47bab47cc89ae0422fee661`.
- Exactly **10** existing records revised; **70** out-of-cohort record blocks preserved byte-for-byte. All original source strings including `legacy:` values retained exactly and in order. No ID renames, new records, other categories, schemas, workflow or link-baseline changes.
- **7 preliminary CLEAR / 3 RETAIN**. CLEAR is metadata review completion, not production security approval.

## Preliminary decisions and caveats

| Record | Proposed decision | Source and limitations |
|---|---|---|
| aws-mcp | CLEAR | [AWS Labs Apache-2.0 source](https://github.com/awslabs/mcp/blob/7a06f09f1acd21e0ac78acc3ac11d2edcfa93bec/LICENSE). Individual MCP servers need IAM, network and package review. |
| aws-billing-and-cost-management-mcp-server | CLEAR | [Specific package](https://github.com/awslabs/mcp/blob/7a06f09f1acd21e0ac78acc3ac11d2edcfa93bec/src/billing-cost-management-mcp-server/pyproject.toml) has explicit Apache-2.0 and AWS credential/billing API caveats; not merely the blog article. |
| azure-ai-foundry | CLEAR | [Current Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry). Commercial Azure platform vs open-source SDKs; legacy canonical ID preserved. |
| docker-hub-mcp | RETAIN | [Docker MCP catalog](https://hub.docker.com/mcp) is a catalog, not an MIT-licensed MCP Gateway/registry or a single installable server. Hosted-product licence entitlement boundary remains unresolved. |
| github-copilot | CLEAR | [GitHub managed Copilot product](https://github.com/features/copilot) and [plans](https://docs.github.com/en/copilot/get-started/plans). Do not assign OSS SPDX from extension/SDK. |
| gitlab-mcp-server | RETAIN | [GitLab MCP server docs](https://docs.gitlab.com/user/model_context_protocol/mcp_server/); licensing/tier/instance rights and OAuth permission scope require separate edition reconciliation. |
| composio | CLEAR | [MIT source](https://github.com/ComposioHQ/composio/blob/4694de1fcd0d57e67490dfb8df936aafae78b915/LICENSE) vs separately operated managed auth/cloud features. Source MIT is not a platform-wide service licence. |
| kserve | CLEAR | [Apache-2.0 source](https://github.com/kserve/kserve/blob/77ef35c12c26dd9ba69efc81b00446420bd84014/LICENSE); cluster/inference-runtime and model licences need independent reviews. |
| mlflow | CLEAR | [Apache-2.0 source](https://github.com/mlflow/mlflow/blob/bdb94c654505e8d02249b4895b75b0c1ff61bb75/LICENSE.txt); secure tracking server, artifact store, traces and third-party model rights separately. |
| sim | RETAIN | [Apache-2.0 repository](https://github.com/simstudioai/sim/blob/a52fc509b5b8a18df519ff0781f00c8d45711164/LICENSE) is evidenced, but specific hosted/connector/enterprise obligations and pricing boundaries need source-by-source confirmation. Preserve review debt; `open-core` is preliminary. |

**Provenance safeguard:** Wave 34 exposed an erroneous literal `- ` prefix in historical `legacy:` sources. This patch explicitly retains every historical string and compares all ten original `sources` prefixes using exact semantic equality; 70 unrelated raw blocks stay untouched.

## Exact OLD → NEW selected-field audit

### `aws-billing-and-cost-management-mcp-server` — 11 fields

**`summary`**

OLD:
```yaml
  summary: MCP server for AWS Billing & Cost Management use cases (announced by AWS).
```
NEW:
```yaml
  summary: "Apache-2.0 AWS Labs MCP server wrapping Billing and Cost Management APIs using caller AWS credentials; API quotas and charges still apply."
```

**`repository_url`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  repository_url: "https://github.com/awslabs/mcp/tree/main/src/billing-cost-management-mcp-server"
```

**`license_model`**

OLD:
```yaml
  license_model: documentation
```
NEW:
```yaml
  license_model: "oss"
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

**`use_when`**

OLD:
```yaml
  use_when:
  - You want AI assistants to query and reason over your AWS billing data via MCP.
```
NEW:
```yaml
  use_when:
  - "You want cost, Free Tier, anomaly and budget insights through a locally configured AWS Billing MCP server using scoped IAM credentials."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when:
  - You don't use AWS or already have FinOps tooling that meets your needs.
```
NEW:
```yaml
  avoid_when:
  - "You cannot protect billing-account information, restrict MCP tool access, or account for paid Cost Explorer and other API calls."
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:9_AI-MLOps/README.md#L42
  - legacy:devopstools_final.md#L1213
```
NEW:
```yaml
  sources:
  - "legacy:9_AI-MLOps/README.md#L42"
  - "legacy:devopstools_final.md#L1213"
  - "https://github.com/awslabs/mcp/tree/7a06f09f1acd21e0ac78acc3ac11d2edcfa93bec/src/billing-cost-management-mcp-server"
  - "https://github.com/awslabs/mcp/blob/7a06f09f1acd21e0ac78acc3ac11d2edcfa93bec/src/billing-cost-management-mcp-server/pyproject.toml"
  - "https://github.com/awslabs/mcp/blob/7a06f09f1acd21e0ac78acc3ac11d2edcfa93bec/src/billing-cost-management-mcp-server/README.md"
  - "https://github.com/awslabs/mcp/blob/7a06f09f1acd21e0ac78acc3ac11d2edcfa93bec/src/billing-cost-management-mcp-server/LICENSE"
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

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

### `aws-mcp` — 10 fields

**`summary`**

OLD:
```yaml
  summary: AWS implementation of Model Context Protocol.
```
NEW:
```yaml
  summary: "AWS Labs collection of Apache-2.0 MCP servers for AWS services; individual servers require separate IAM and runtime configuration."
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

**`license_spdx`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  license_spdx: "Apache-2.0"
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

**`use_when`**

OLD:
```yaml
  use_when:
  - You want AI agents to interact with AWS services through a standardized context protocol.
```
NEW:
```yaml
  use_when:
  - "You need reviewed AWS-specific MCP tools and can constrain IAM roles, AWS regions, tool execution and API charges."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when:
  - Your infrastructure isn't on AWS or you don't use MCP-compatible clients.
```
NEW:
```yaml
  avoid_when:
  - "You expect one server to implement the entire AWS MCP collection or to bypass IAM, request quotas or usage charges."
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:9_AI-MLOps/README.md#L44
  - legacy:devopstools_final.md#L1214
```
NEW:
```yaml
  sources:
  - "legacy:9_AI-MLOps/README.md#L44"
  - "legacy:devopstools_final.md#L1214"
  - "https://github.com/awslabs/mcp/tree/7a06f09f1acd21e0ac78acc3ac11d2edcfa93bec"
  - "https://github.com/awslabs/mcp/blob/7a06f09f1acd21e0ac78acc3ac11d2edcfa93bec/LICENSE"
  - "https://awslabs.github.io/mcp"
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

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

### `azure-ai-foundry` — 10 fields

**`summary`**

OLD:
```yaml
  summary: Azure platform for building, deploying, and operating AI solutions (models, agents, evaluation,
    safety).
```
NEW:
```yaml
  summary: "Microsoft Foundry (formerly Azure AI Foundry) is an Azure-managed platform for models, agents and AI application operations, billed separately from its SDKs."
```

**`license_model`**

OLD:
```yaml
  license_model: documentation
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

**`use_when`**

OLD:
```yaml
  use_when:
  - You're already on Azure and need an integrated AI lifecycle platform.
```
NEW:
```yaml
  use_when:
  - "You operate AI workloads in Azure and need managed models, evaluations, agents and Azure access controls."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when:
  - You need cloud-agnostic tooling or aren't building production AI workloads.
```
NEW:
```yaml
  avoid_when:
  - "You require a self-hosted OSS platform or presume all Foundry models, regions and project interfaces share the same pricing or API surface."
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:9_AI-MLOps/README.md#L4
  - legacy:devopstools_final.md#L1179
```
NEW:
```yaml
  sources:
  - "legacy:9_AI-MLOps/README.md#L4"
  - "legacy:devopstools_final.md#L1179"
  - "https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry"
  - "https://learn.microsoft.com/en-us/azure/ai-foundry/what-is-azure-ai-foundry"
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

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

### `composio` — 10 fields

**`summary`**

OLD:
```yaml
  summary: Agent tooling platform for managed auth, app connectors, triggers, and sandboxed tool execution
    across developer and business apps.
```
NEW:
```yaml
  summary: "MIT-licensed Composio SDK for agent tool integrations alongside distinct managed authentication, connectors and hosted workbench services."
```

**`repository_url`**

OLD:
```yaml
  repository_url: https://github.com/composiohq/composio
```
NEW:
```yaml
  repository_url: "https://github.com/ComposioHQ/composio"
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

**`deployment_models`**

OLD:
```yaml
  deployment_models: []
```
NEW:
```yaml
  deployment_models:
  - "hosted-saas"
  - "self-hosted"
```

**`use_when`**

OLD:
```yaml
  use_when: []
```
NEW:
```yaml
  use_when:
  - "You need agent tool integrations and can manage connector OAuth consent, tokens, permissions and managed-service billing."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when: []
```
NEW:
```yaml
  avoid_when:
  - "You assume the open-source SDK's MIT license also covers all commercial hosted connectors and authentication services."
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:devopstools_final.md#L1234
```
NEW:
```yaml
  sources:
  - "legacy:devopstools_final.md#L1234"
  - "https://github.com/ComposioHQ/composio/tree/4694de1fcd0d57e67490dfb8df936aafae78b915"
  - "https://github.com/ComposioHQ/composio/blob/4694de1fcd0d57e67490dfb8df936aafae78b915/LICENSE"
  - "https://composio.dev"
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

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

### `docker-hub-mcp` — 7 fields

**`summary`**

OLD:
```yaml
  summary: Docker Hub surface for discovering the containerized servers in Docker's MCP Catalog.
```
NEW:
```yaml
  summary: "Docker Hub's discovery catalog for container-packaged MCP servers; it is distinct from the MIT-licensed Docker MCP Gateway and registry repositories."
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

**`use_when`**

OLD:
```yaml
  use_when:
  - You want to discover Docker-packaged MCP servers through the catalog integrated into Docker Hub.
```
NEW:
```yaml
  use_when:
  - "You need to discover MCP server container images and evaluate their publishers, permissions and provenance."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when:
  - You need a standalone licensable product or source repository; reconcile this catalog feature separately from Docker Hub, Docker MCP Gateway, and Docker Hub MCP Server.
```
NEW:
```yaml
  avoid_when:
  - "You need one standalone open-source MCP server or assume the Docker MCP Gateway MIT license covers Docker Hub or listed server images."
```

**`sources`**

OLD:
```yaml
  sources:
  - https://hub.docker.com/mcp
  - https://docs.docker.com/ai/mcp-catalog-and-toolkit/
  - https://docs.docker.com/docker-hub/image-library/catalogs/
  - legacy:9_AI-MLOps/README.md#L48
  - legacy:devopstools_final.md#L1216
```
NEW:
```yaml
  sources:
  - "https://hub.docker.com/mcp"
  - "https://docs.docker.com/ai/mcp-catalog-and-toolkit/"
  - "https://docs.docker.com/docker-hub/image-library/catalogs/"
  - "legacy:9_AI-MLOps/README.md#L48"
  - "legacy:devopstools_final.md#L1216"
  - "https://github.com/docker/mcp-gateway"
  - "https://github.com/docker/mcp-registry"
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

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-09-13'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

### `github-copilot` — 11 fields

**`summary`**

OLD:
```yaml
  summary: AI-powered code completion assistant.
```
NEW:
```yaml
  summary: "GitHub's managed AI coding assistant and agent offerings with account- and feature-dependent plans, usage quotas and data policies."
```

**`official_url`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  official_url: "https://github.com/features/copilot"
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

**`use_when`**

OLD:
```yaml
  use_when:
  - You want inline code suggestions tightly integrated with VS Code, JetBrains, or GitHub workflows.
```
NEW:
```yaml
  use_when:
  - "You need GitHub-integrated AI coding assistance under approved plan, repository and organization data policies."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when:
  - Your organization prohibits sending code to external AI services.
```
NEW:
```yaml
  avoid_when:
  - "You require fully local inference or assume Copilot's managed service is open-source because an extension or SDK is available."
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:9_AI-MLOps/README.md#L24
  - legacy:devopstools_final.md#L1200
```
NEW:
```yaml
  sources:
  - "legacy:9_AI-MLOps/README.md#L24"
  - "legacy:devopstools_final.md#L1200"
  - "https://github.com/features/copilot"
  - "https://docs.github.com/en/copilot/get-started/plans"
  - "https://docs.github.com/en/copilot"
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

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

### `gitlab-mcp-server` — 7 fields

**`summary`**

OLD:
```yaml
  summary: GitLab MCP server documentation.
```
NEW:
```yaml
  summary: "GitLab's documented MCP server interface for authorized GitLab-project tools; editions, account entitlements, OAuth scopes and instance configuration must be checked."
```

**`documentation_url`**

OLD:
```yaml
<absent>
```
NEW:
```yaml
  documentation_url: "https://docs.gitlab.com/user/model_context_protocol/mcp_server/"
```

**`use_when`**

OLD:
```yaml
  use_when:
  - You're on GitLab and want MCP-compatible AI agents to interact with your projects.
```
NEW:
```yaml
  use_when:
  - "You need to connect approved MCP clients to authorized GitLab resources using least-privilege tokens or OAuth."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when:
  - You don't use GitLab or aren't adopting MCP-based tooling.
```
NEW:
```yaml
  avoid_when:
  - "You cannot validate GitLab tier or instance availability, client permissions, and the distinction from GitLab Duo MCP clients."
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:9_AI-MLOps/README.md#L52
  - legacy:devopstools_final.md#L1219
```
NEW:
```yaml
  sources:
  - "legacy:9_AI-MLOps/README.md#L52"
  - "legacy:devopstools_final.md#L1219"
  - "https://docs.gitlab.com/user/model_context_protocol/mcp_server/"
  - "https://docs.gitlab.com/user/model_context_protocol/"
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

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

### `kserve` — 9 fields

**`summary`**

OLD:
```yaml
  summary: Model serving on Kubernetes.
```
NEW:
```yaml
  summary: "Apache-2.0 Kubernetes inference platform for predictive and generative models, requiring cluster, model-runtime and networking operations."
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

**`use_when`**

OLD:
```yaml
  use_when:
  - You need scalable, standardized model inference on existing Kubernetes clusters.
```
NEW:
```yaml
  use_when:
  - "You operate Kubernetes and need standardized inference controllers and scalable model serving with vetted runtimes."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when:
  - You don't run Kubernetes or only need simple batch predictions.
```
NEW:
```yaml
  avoid_when:
  - "You need a hosted inference service without Kubernetes operations or expect all upstream runtime images and models to share KServe's license."
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:9_AI-MLOps/README.md#L6
  - legacy:devopstools_final.md#L1181
```
NEW:
```yaml
  sources:
  - "legacy:9_AI-MLOps/README.md#L6"
  - "legacy:devopstools_final.md#L1181"
  - "https://github.com/kserve/kserve/tree/77ef35c12c26dd9ba69efc81b00446420bd84014"
  - "https://github.com/kserve/kserve/blob/77ef35c12c26dd9ba69efc81b00446420bd84014/LICENSE"
  - "https://kserve.github.io/website"
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

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

### `mlflow` — 9 fields

**`summary`**

OLD:
```yaml
  summary: Platform for managing ML lifecycles.
```
NEW:
```yaml
  summary: "Apache-2.0 open-source AI engineering platform for ML experiments, model lifecycle, LLM evaluation and tracing; hosted offerings are separate."
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

**`use_when`**

OLD:
```yaml
  use_when:
  - You need experiment tracking, model registry, and reproducibility across ML projects.
```
NEW:
```yaml
  use_when:
  - "You need experiment tracking, model artifacts, evaluations or agent/LLM traces with controlled backend storage."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when:
  - You have no ML model training workflows or already use a tightly integrated managed platform.
```
NEW:
```yaml
  avoid_when:
  - "You cannot secure MLflow tracking servers, model artifacts or authentication, or assume third-party hosted deployments are Apache licensed."
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:9_AI-MLOps/README.md#L8
  - legacy:devopstools_final.md#L1184
```
NEW:
```yaml
  sources:
  - "legacy:9_AI-MLOps/README.md#L8"
  - "legacy:devopstools_final.md#L1184"
  - "https://github.com/mlflow/mlflow/tree/bdb94c654505e8d02249b4895b75b0c1ff61bb75"
  - "https://github.com/mlflow/mlflow/blob/bdb94c654505e8d02249b4895b75b0c1ff61bb75/LICENSE.txt"
  - "https://mlflow.org"
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

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```

### `sim` — 9 fields

**`summary`**

OLD:
```yaml
  summary: AI workspace for building, deploying, and monitoring agentic workflows.
```
NEW:
```yaml
  summary: "Apache-2.0 source for Sim's AI-agent and workflow builder, with separately operated hosted services, connectors and inference billing."
```

**`license_model`**

OLD:
```yaml
  license_model: unknown
```
NEW:
```yaml
  license_model: "open-core"
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

**`deployment_models`**

OLD:
```yaml
  deployment_models: []
```
NEW:
```yaml
  deployment_models:
  - "self-hosted"
  - "hosted-saas"
```

**`use_when`**

OLD:
```yaml
  use_when: []
```
NEW:
```yaml
  use_when:
  - "You want a visual agent workflow builder and can review workflow actions, provider data flow and hosting costs."
```

**`avoid_when`**

OLD:
```yaml
  avoid_when: []
```
NEW:
```yaml
  avoid_when:
  - "You assume the source license includes hosted Sim services, model credits, connectors or enterprise support without separate terms."
```

**`sources`**

OLD:
```yaml
  sources:
  - legacy:devopstools_final.md#L1246
```
NEW:
```yaml
  sources:
  - "legacy:devopstools_final.md#L1246"
  - "https://github.com/simstudioai/sim/tree/a52fc509b5b8a18df519ff0781f00c8d45711164"
  - "https://github.com/simstudioai/sim/blob/a52fc509b5b8a18df519ff0781f00c8d45711164/LICENSE"
  - "https://www.sim.ai"
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

**`verified_on`**

OLD:
```yaml
  verified_on: '2026-08-03'
```
NEW:
```yaml
  verified_on: "2026-10-30"
```


## Mandatory blocked gates

- Repeat source/edition/licence review and check URLs on publication day; unknown claims remain RETAIN. Check licence models against repo taxonomy. Do not blindly change any other field or record.
- On user's Windows PowerShell 5.1 checkout, use a **new** SHA-pinned guarded verifier (not Wave 34 V2/V3) with Python 3.12 and reliable command invocation `& $PythonExe @PythonArgs` (never a PowerShell parameter named `Args`).
- Regenerate docs deterministically, then `scripts.generate_docs --check`, `scripts.validate_catalog`, `scripts.review_debt --format json`, Ruff check/format, `pip check`, full `pytest`, `git diff --check`; assert 1,425 records, 10 selected / 70 non-selected untouched and exact original `legacy:` strings. Derive status/licence totals from generated JSON only; **not yet validated**.
- Allowlist only canonical YAML, this evidence report, and genuinely affected generated docs. Push only on successful local validation, no force; create Draft PR only after regenerated outputs pass and source scope is verified.
- Final PR SHA requires all security/quality checks plus separate strict Full link audit: `blocking_new: 0`, `strict_result: PASS`, historical blockers separately disclosed; no audit baseline edits.
- Distinct human gates: approval for Ready for Review, **separate** approval for squash merge; post-merge verification precedes issue closure.

**Execution boundary:** This is source-evidence staging, not a tested or merge-ready patch. No local Python execution, generated docs, CI, strict link audit, Draft PR, Ready transition or merge is claimed.
