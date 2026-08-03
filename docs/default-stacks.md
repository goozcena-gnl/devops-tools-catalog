# Reference stacks

These stacks are opinionated starting points, not universal standards. Each assumes one tool per concern unless an optional component adds a distinct capability.

## Personal lab or portfolio

**Assumptions:** One operator, limited budget, learning and demonstrability matter more than multi-region availability.

**Required:** GitHub, OpenTofu, Ansible, k3s, Helm, Flux, Prometheus, Grafana, Loki, SOPS, and Renovate.

**Optional:** Gitea for self-hosted Git, Cilium for networking experiments, Velero for recovery practice, and OpenCost for cost visibility.

**Alternatives:** Use Docker Compose instead of Kubernetes when orchestration is not part of the learning goal. Avoid running Argo CD and Flux together.

## Small engineering team

**Assumptions:** Fewer than 30 engineers, managed services are acceptable, and operational headcount is constrained.

**Required:** GitHub or GitLab, managed CI, OpenTofu or Terraform, a cloud-native secret store, managed Kubernetes or container platform, OpenTelemetry, managed metrics/logs, and incident paging.

**Optional:** Argo CD for Kubernetes GitOps, Backstage only after service ownership becomes difficult, and Infracost for pull-request estimates.

**Alternatives:** Prefer a managed observability service over operating several stateful backends. Use Pulumi when the team strongly prefers general-purpose languages.

## Kubernetes-first platform

**Assumptions:** Multiple teams deploy to Kubernetes and platform engineers own shared cluster capabilities.

**Required:** kubeadm or a managed distribution, Cilium, Gateway API, Helm plus Kustomize, Argo CD or Flux, External Secrets Operator, cert-manager, Kyverno, Prometheus, Grafana, Loki, Tempo, and Velero.

**Optional:** Backstage, Crossplane, Kargo, OpenCost, and Linkerd or Istio when service-mesh requirements are explicit.

**Alternatives:** Choose Flux for composable controller workflows and Argo CD for a stronger application UI. Do not add a service mesh only for ingress.

## Cloud-agnostic enterprise

**Assumptions:** Multiple clouds, centralized governance, formal change control, and dedicated platform/SRE teams.

**Required:** OpenTofu or Terraform, Terragrunt where hierarchy warrants it, Ansible, Kubernetes, Argo CD or Flux, Vault, OpenTelemetry, Prometheus-compatible metrics, centralized logs, OPA or Kyverno, SBOM generation, signing, and an enterprise artifact registry.

**Optional:** Crossplane for platform APIs, Backstage for service ownership, and commercial support for critical components.

**Alternatives:** Cloud-native services can replace self-hosted components per environment when portability is less important than operating cost.

## Azure-first environment

**Assumptions:** Microsoft Entra ID is authoritative and Azure Policy governs subscriptions.

**Required:** Azure DevOps or GitHub, Bicep or Terraform/OpenTofu, Azure Verified Modules, Azure Container Registry, AKS or Container Apps, Key Vault, Azure Monitor, Application Insights, Defender for Cloud, and Azure Policy.

**Optional:** Argo CD for AKS GitOps, Managed Grafana, Cost Management exports, and OpenTelemetry for portable instrumentation.

**Alternatives:** Choose Bicep for Azure-only native coverage; choose Terraform/OpenTofu for multi-cloud workflows. Avoid duplicating Key Vault with Vault unless cross-cloud policy requires it.

## AWS-first environment

**Assumptions:** AWS Organizations and IAM Identity Center provide account and identity boundaries.

**Required:** GitHub or CodeCommit replacement selected by policy, CloudFormation/CDK or Terraform/OpenTofu, ECR, EKS/ECS/Lambda, Secrets Manager, CloudWatch, CloudTrail, Config, Security Hub, and Cost Explorer/Budgets.

**Optional:** Argo CD for EKS, OpenTelemetry, Managed Prometheus/Grafana, and Infracost.

**Alternatives:** Use CDK for teams that value typed abstractions; use declarative HCL for cross-account consistency and ecosystem breadth.

## Regulated or high-security environment

**Assumptions:** Evidence, segregation of duties, provenance, and recovery objectives are mandatory.

**Required:** Self-hosted or policy-approved SCM/CI, isolated runners, immutable artifact storage, Syft, Cosign, SLSA provenance, Trivy or Grype, CodeQL or equivalent SAST, Vault or HSM-backed cloud secrets, OPA/Kyverno, audit logging, SIEM integration, and tested backup/restore.

**Optional:** Air-gapped mirrors, in-toto attestations, runtime detection with Falco, and chaos exercises in pre-production.

**Alternatives:** Managed services are valid when contracts, data residency, key ownership, and audit evidence meet controls. Do not overlap multiple scanners without assigning distinct coverage.

## OSS-first environment

**Assumptions:** Open governance, inspectable source, and self-hosting are preferred; operating capacity exists.

**Required:** Gitea or GitLab Community Edition, OpenTofu, Ansible, Kubernetes, Flux or Argo CD, Harbor, SOPS plus External Secrets Operator, Prometheus, Grafana, Loki, Tempo, OpenCost, and Renovate.

**Optional:** Woodpecker CI, Backstage, Crossplane, Keycloak, and Vault after licence and operational review.

**Alternatives:** A commercial managed service can reduce toil when its exit path and data portability are acceptable. Verify current licences rather than relying on historical OSS status.

## MLOps environment

**Assumptions:** Teams train, evaluate, deploy, and observe models with reproducibility and governance requirements.

**Required:** Git, DVC or object-versioning equivalent, MLflow, an orchestrator such as Argo Workflows or Kubeflow Pipelines, a container registry, Kubernetes or managed training, model serving, OpenTelemetry, and model/data quality monitoring.

**Optional:** KServe, Feast, Ray, GPU operators, prompt/evaluation tooling, and a model gateway.

**Alternatives:** Managed SageMaker, Vertex AI, or Azure Machine Learning reduces platform work. Avoid adopting Kubeflow wholesale when only experiment tracking and batch training are needed.
