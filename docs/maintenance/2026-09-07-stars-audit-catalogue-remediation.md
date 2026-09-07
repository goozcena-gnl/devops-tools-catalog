# GitHub Stars audit catalogue remediation — 2026-09-07

## Context

These findings originated in the full GitHub Stars audit of 1,305 catalogue records and 880 repository
URLs. This focused remediation reverified only the four P0 and ten P1 leads against current primary
sources. Adding the missing Headlamp core project increases the canonical catalogue to 1,306 records;
the existing official plugins record remains separate.

## Finding dispositions

| Priority | Tool | Finding | Primary verification | Action | Final state |
| --- | --- | --- | --- | --- | --- |
| P0 | Talos Node Updater (`tnu`) | Record incorrectly described a Node.js test runner. | The [archived upstream README](https://github.com/jfroy/tnu) identifies a Go-based Talos node updater, marks it deprecated, and directs users to `home-operations/tuppr`. | FIXED | Corrected identity, Kubernetes category, roles, guidance, Apache-2.0 metadata, and sources; retained archived status. |
| P0 | Headlamp | Catalogue represented official plugins but omitted the core application. | The [Kubernetes SIG UI repository](https://github.com/kubernetes-sigs/headlamp) identifies the maintained core UI and its move into `kubernetes-sigs`; the [plugins repository](https://github.com/headlamp-k8s/plugins) explicitly describes itself as official plugins. | FIXED | Added canonical Headlamp core record and independently verified/enriched the separate plugins record. |
| P0 | LocalStack | Active product and archived Community repository boundary lacked current licensing context. | The [archived repository notice](https://github.com/localstack/localstack), [official plan documentation](https://docs.localstack.cloud/aws/licensing/), and [pricing page](https://www.localstack.cloud/pricing) distinguish the retired Community distribution from the licensed unified product. | FIXED | Preserved `status: active` plus `repository_archived: true`; updated summary, conditions, licensing model, evidence, and verification date. |
| P0 | MinIO Community Server | Record blurred the archived AGPL community server with separately licensed AIStor products. | The [upstream repository](https://github.com/minio/minio) is archived and explicitly unmaintained; [AIStor licensing docs](https://docs.min.io/aistor/operations/licenses/) describe the separate Free and Enterprise licences. | FIXED | Renamed and moved the community server record to deprecated/historical, set archived lifecycle and AGPL-3.0-only, and documented the product boundary. |
| P1 | Velero | Repository still used the pre-move `vmware-tanzu` URL. | The old URL redirects to the active [Velero organization repository](https://github.com/velero-io/velero), whose README links official docs and CNCF context. | FIXED | Updated canonical repository/docs URL, active state, Apache-2.0 metadata, sources, and verification date. |
| P1 | Juju | `repository_archived: true` was stale. | The active [Canonical Juju repository](https://github.com/juju/juju) contains current source, issues, pull requests, and links to [official documentation](https://documentation.ubuntu.com/juju/). | FIXED | Cleared archived/review flags and updated active maturity, description, docs, sources, and verification date. |
| P1 | Grafana OnCall OSS | Old repository URL redirected to cold storage and the record blurred archived OSS with Cloud IRM. | [Official Grafana documentation](https://grafana.com/docs/oncall/latest/intro/) states that OnCall OSS is archived and development continues in Cloud IRM; the repository now lives in [Grafana cold storage](https://github.com/grafana-cold-storage/oncall). | FIXED | Renamed OSS record, updated canonical cold-storage URL/docs, AGPL-3.0-only metadata, lifecycle guidance, sources, and review state. |
| P1 | CAI (RobotSec) | Recheck frozen/archive status and successor boundary. | The [official archived repository](https://github.com/aliasrobotics/cai) calls the code a read-only research artifact and separately identifies CSI as successor. | ALREADY_CORRECT | Existing archived repository/status, research boundary, successor source, and cleared review flag are correct. |
| P1 | CDKTF | Archived status existed but licence and migration guidance were stale. | HashiCorp's [official sunset notice](https://github.com/hashicorp/terraform-cdk) confirms archival, MPL licensing, and recommends migration to standard Terraform/HCL. | FIXED | Corrected licence model/SPDX, maintenance guidance, Terraform alternative, source, and verification date. |
| P1 | Datree | Recheck archive state and retained historical record. | The [official Datree repository](https://github.com/datreeio/datree) is archived. | ALREADY_CORRECT | Existing archive flag/status, Apache-2.0 metadata, primary sources, and cleared review flag are correct. |
| P1 | Kaniko | Recheck archive state. | The [official GoogleContainerTools repository](https://github.com/GoogleContainerTools/kaniko) is archived and read-only. | ALREADY_CORRECT | Existing deprecated/historical placement, retire lifecycle, archive flag/status, and cleared review flag are correct. |
| P1 | Keptn classic | Recheck the classic repository lifecycle. | The [official classic Keptn repository](https://github.com/keptn/keptn) is archived and read-only. | ALREADY_CORRECT | Existing deprecated/historical placement, retire lifecycle, archive flag/status, and cleared review flag are correct. |
| P1 | Kubeapps | Recheck deprecation and archive state. | The [official Kubeapps repository](https://github.com/vmware-tanzu/kubeapps) states that the project was deprecated and archived. | ALREADY_CORRECT | Existing deprecated/historical placement, retire lifecycle, archive flag/status, and cleared review flag are correct. |
| P1 | Kubernetes Dashboard | Retired record still required review and lacked its official successor guidance. | The [retired upstream repository](https://github.com/kubernetes-retired/dashboard) states that it is no longer maintained and explicitly recommends [Headlamp](https://github.com/kubernetes-sigs/headlamp). | FIXED | Updated summary and maintenance guidance, linked Headlamp as alternative, added sources, refreshed verification date, and cleared review. |

## Validation

- `python -m scripts.generate_docs` — pass.
- `python -m scripts.generate_docs --check` — pass; generated output is deterministic.
- `python -m scripts.validate_catalog` — pass.
- `python -m pytest` — 366 tests passed after incorporating the latest `main` branch and updating its catalogue-count invariant.
- `python -m ruff check scripts tests` — pass.
- `python -m ruff format --check scripts tests` — pass.
- `python -m scripts.check_links --strict` — strict result `FAIL`: 1,835 valid, 31 valid redirects,
  218 permanent redirects, nine known/baselined blockers, and two new blockers. At the time, the unrelated
  pre-existing failures were `https://kubegui.net` and Firecracker's removed `docs/README.md` path. All links
  introduced or changed by this remediation passed. The unrelated records and strict baseline were intentionally
  not changed. Post-merge revalidation later classified the KubeGUI result as transient and repaired the
  Firecracker link separately.

## Scope and non-goals

- No GitHub Stars were added, removed, or otherwise modified.
- No B-tier repository was starred.
- No GitHub List was created or modified.
- No unrelated catalogue record was intentionally changed.
- The five `ALREADY_CORRECT` findings were left unchanged after re-verification.
- The remediation pull request was merged only after human review and exact-HEAD revalidation.
