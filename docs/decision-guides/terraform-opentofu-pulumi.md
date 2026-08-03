# Terraform versus OpenTofu versus Pulumi

| Consideration | Terraform | OpenTofu | Pulumi |
|---|---|---|---|
| Authoring | HCL and provider ecosystem | HCL-compatible community-governed engine | General-purpose languages or YAML |
| Governance | Vendor-led, source-available core | Linux Foundation, OSS | Vendor-led OSS SDK with commercial service |
| Migration | Existing enterprise workflows and integrations | Strong Terraform-language compatibility | Code and state migration effort varies |
| Team fit | Broad IaC familiarity | OSS governance priority | Strong software-engineering preference |

Choose based on required providers, state/automation services, policy controls, licence policy, and team skills. Test critical modules and state migration before switching engines. Avoid mixing engines against the same state.
