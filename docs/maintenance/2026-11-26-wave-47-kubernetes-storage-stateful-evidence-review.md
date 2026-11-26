# Wave 47 — Kubernetes storage and stateful workloads evidence review

Evidence reviewed on 2026-11-25 and 2026-11-26. Local candidate derived from accepted [selection issue #208](https://github.com/goozcena-gnl/devops-tools-catalog/issues/208), body SHA-256 `4f81a5bf499076038f438961e321eac02ca49f148c5a94040c6122ea90db271e`. Baseline `a8043c452cfe0e626860f4aebb9567e0e3b5c21c`.

Scope: ten selected IDs, 67 semantic field changes, 123 protected raw blocks. Three CLEAR candidates, two RECLASSIFY candidates and five RETAIN. No new records or global licence inference.

The following exact field contract records the primary evidence and scope boundaries. Source availability is rechecked before local implementation; runtime support, third-party licensing and artifact signatures are not certified. Local validation results are recorded separately in the execution evidence directory; this ledger does not attest to remote CI or a merge.

## Per-record evidence and changes
The following tables specify exact proposed semantic values. YAML quoting and line wrapping may follow the existing serialization convention, but unselected raw record blocks must not be reserialized.

For `use_when` and `avoid_when`, each nonempty proposed value represents a single-element YAML list.

For every `sources` change:

- The original list must remain the exact ordered prefix.
- Append only the exact URLs explicitly listed for that record below.
- Do not replace, reorder or remove legacy provenance.
- Do not automatically append other research URLs.

All fields not explicitly listed as changed must retain their original values.

### 4.1. ceph — RETAIN

**Evidence boundary:** distributed block, file and object storage; component-specific licences rather than a single project-wide licence expression.

| Field | Before | After |
| --- | --- | --- |
| `use_when` | You need battle-tested, unified distributed storage at scale with multi-protocol support. | You need unified distributed block, file and object storage and can operate the underlying storage cluster. |
| `avoid_when` | Your team lacks the expertise to manage Ceph's operational complexity or cloud-native storage suffices. | A simpler managed storage service meets your requirements, or your team cannot operate storage failure domains, capacity and recovery. |
| `documentation_url` | Absent | https://github.com/ceph/ceph/blob/b060042deb05d33e6cc358970cfb8221240bcf3e/doc/index.rst |
| `sources` | Original two legacy entries | Original ordered prefix plus four URLs below |

Original source prefix:

- `legacy:4_Kubernetes-Containers/README.md#L171`
- `legacy:devopstools_final.md#L675`

Append:

- https://github.com/ceph/ceph/blob/b060042deb05d33e6cc358970cfb8221240bcf3e/README.md
- https://github.com/ceph/ceph/blob/b060042deb05d33e6cc358970cfb8221240bcf3e/COPYING
- https://github.com/ceph/ceph/blob/b060042deb05d33e6cc358970cfb8221240bcf3e/doc/index.rst
- https://github.com/ceph/ceph/blob/e8559c00d218beab20d0f516710299454f9bb631/doc/releases/releases.yml

The stable source COPYING inventory identifies multiple licence families. Root-level or default licensing must not be extrapolated into a universal SPDX expression.

V3.1 transport correction: the rendered releases index returned HTTP 429 on three spaced attempts; the Umbrella documentation URL was deferred without a reachability result. The remaining 41 unique contract URLs were observed reachable in the independent Windows diagnostic. Replace the two rendered-document URLs with official Git source files: `doc/index.rst` at the stable release commit (blob `a59bcf657e7a52fcb5923e61596a8350338ecd03`) and `doc/releases/releases.yml` at the 2026-11-25 upstream snapshot (blob `33cc95287bc55a4ecd174c3d1c9ed8ac65876215`). The latter records Umbrella 21.2.0 released on 2026-10-28 with target EOL 2028-06-01. The target is not a support guarantee. Rendered-site accessibility remains unverified; do not classify the previous URLs as reachable or permanently broken. The source snapshot is not the release tag commit.

Preserve `summary`, `license_model: oss`, absent SPDX, `maturity: unknown`, `status: needs-review`, `needs_review: true` and the original verification date.

Exact changed-key allowlist:

`use_when`, `avoid_when`, `documentation_url`, `sources`.

**4 keys.**

### 4.2. rook — CLEAR candidate

**Evidence boundary:** Kubernetes-native orchestration of Ceph, not a generic independent NFS storage backend.

| Field | Before | After |
| --- | --- | --- |
| `summary` | Storage orchestrator for Kubernetes. | Kubernetes operator for deploying, provisioning, monitoring and managing Ceph storage clusters. |
| `use_when` | You want Kubernetes-native orchestration of Ceph (or NFS) with operator-managed lifecycle. | You need operator-managed Ceph block, file or object storage in Kubernetes. |
| `avoid_when` | You don't need distributed storage or a managed storage service (EBS/PD) is simpler. | Managed storage meets your requirements, or the cluster cannot satisfy Ceph and Rook storage, host and privilege prerequisites. |
| `documentation_url` | Absent | https://rook.io/docs/rook/v1.21/Getting-Started/Prerequisites/prerequisites/ |
| `license_spdx` | Absent | Apache-2.0 |
| `maturity` | unknown | established |
| `status` | needs-review | active |
| `needs_review` | true | false |
| `verified_on` | 2026-08-03 | 2026-11-26 |
| `sources` | Original two legacy entries | Original ordered prefix plus four URLs below |

Original source prefix:

- `legacy:4_Kubernetes-Containers/README.md#L175`
- `legacy:devopstools_final.md#L679`

Append:

- https://github.com/rook/rook/blob/0338330b484066be277e7d2ac34edec99435dd6d/README.md
- https://github.com/rook/rook/blob/0338330b484066be277e7d2ac34edec99435dd6d/LICENSE
- https://github.com/rook/rook/releases/tag/v1.21.3
- https://rook.io/docs/rook/v1.21/Getting-Started/Prerequisites/prerequisites/

The stable README establishes Ceph orchestration and CNCF graduated project status. The actual root licence is Apache-2.0.

The `established` maturity judgement is based on sustained release activity, documented operational scope and project history, not certification of production readiness.

Apache-2.0 describes the reviewed Rook source. Ceph, CSI components and bundled third-party software retain independent legal boundaries.

Exact changed-key allowlist:

`summary`, `use_when`, `avoid_when`, `documentation_url`, `license_spdx`, `maturity`, `status`, `needs_review`, `verified_on`, `sources`.

**10 keys.**

### 4.3. linstor — RECLASSIFY candidate

**Evidence boundary:** LINSTOR open-source storage management server, separate commercial support and optional products.

| Field | Before | After |
| --- | --- | --- |
| `summary` | Distributed storage management (DRBD-based) with community and enterprise support. | Open-source software-defined block storage management with controller and satellite services, including DRBD integration. |
| `use_when` | You need synchronous replication with DRBD for low-latency block storage on bare metal. | You need managed Linux block storage and optional DRBD replication across storage nodes. |
| `avoid_when` | Longhorn or Ceph (via Rook) provides sufficient performance with simpler operations. | The environment cannot satisfy LINSTOR and DRBD host, network or quorum requirements, or simpler storage meets your needs. |
| `documentation_url` | Absent | https://linbit.com/drbd-user-guide/linstor-guide-1_0-en/ |
| `license_model` | open-core | oss |
| `sources` | Original two legacy entries | Original ordered prefix plus five URLs below |

Original source prefix:

- `legacy:4_Kubernetes-Containers/README.md#L172`
- `legacy:devopstools_final.md#L676`

Append:

- https://github.com/LINBIT/linstor-server/blob/75d5fa72d504ccfe55c421ccccda9505af8371f8/README.md
- https://github.com/LINBIT/linstor-server/blob/75d5fa72d504ccfe55c421ccccda9505af8371f8/LICENSE
- https://github.com/LINBIT/linstor-server/blob/75d5fa72d504ccfe55c421ccccda9505af8371f8/debian/copyright
- https://github.com/LINBIT/linstor-server/releases/tag/v1.35.3
- https://linbit.com/drbd-user-guide/linstor-guide-1_0-en/

The root LICENSE and COPYING files contain GPL version 3, while the Debian copyright file declares GPL-2.0-or-later for `Files: *`.

This is a source-licensing discrepancy requiring clarification, not evidence supporting an invented global SPDX.

The stable README explicitly identifies LINSTOR as open source and distinguishes professional support and official binaries. Paid support alone does not establish an open-core licence model.

The proposed OSS classification applies to the existing server-backed record. It does not classify the complete LINBIT product portfolio or DRBD Proxy.

Retain review debt, unknown maturity, original verification date and absent SPDX.

Exact changed-key allowlist:

`summary`, `use_when`, `avoid_when`, `documentation_url`, `license_model`, `sources`.

**6 keys.**

### 4.4. portworx — RECLASSIFY candidate

**Evidence boundary:** the existing generic record is proposed to represent the Portworx Enterprise storage platform.

Explicit maintainer acceptance of this product scope is required before implementation.

| Field | Before | After |
| --- | --- | --- |
| `summary` | Kubernetes data services platform. | Commercial Kubernetes storage platform providing persistent storage and data services through Portworx Enterprise. |
| `use_when` | You need enterprise-grade persistent storage with advanced features (encryption, migration, disaster recovery). | You need enterprise Kubernetes storage and data services supported by the selected Portworx licence and deployment configuration. |
| `avoid_when` | Open-source alternatives (Longhorn/Rook-Ceph) meet your requirements and budget is a concern. | Open-source or managed storage meets your requirements, or the required Portworx licences and supported infrastructure are unavailable. |
| `documentation_url` | Absent | https://docs.portworx.com/portworx-enterprise |
| `license_model` | unknown | commercial |
| `sources` | Original two legacy entries | Original ordered prefix plus four URLs below |

Original source prefix:

- `legacy:4_Kubernetes-Containers/README.md#L174`
- `legacy:devopstools_final.md#L678`

Append:

- https://docs.portworx.com/portworx-enterprise/platform/license
- https://docs.portworx.com/portworx-enterprise/platform/license/features-supported
- https://docs.portworx.com/portworx-enterprise/support/support-policy
- https://docs.portworx.com/portworx-enterprise/release-notes

The vendor documents commercial licence activation, different feature entitlements and version-specific support policies.

No parent-wide public source repository has been established. Do not substitute an open-source integration or SDK.

No complete executed commercial agreement was inspected.

Keep the canonical name and official URL unchanged. Preserve absent repository URL and SPDX, unknown maturity, original verification date and review debt.

If the proposed Enterprise identity boundary is rejected, STOP and revise the scope rather than reclassifying the generic product automatically.

Exact changed-key allowlist:

`summary`, `use_when`, `avoid_when`, `documentation_url`, `license_model`, `sources`.

**6 keys.**

### 4.5. hwameistor — RETAIN

**Evidence boundary:** local CSI storage with distinct HA and non-HA configurations.

| Field | Before | After |
| --- | --- | --- |
| `summary` | Cloud-native local storage system. | Kubernetes CSI local storage system providing local LVM and disk volumes, including replicated HA configurations. |
| `use_when` | You need high-performance local persistent storage with HA and volume migration on bare metal. | You need local persistent storage and can select suitable non-HA or replicated HA volume configurations. |
| `avoid_when` | Cloud-provided block storage (EBS/PD) or distributed storage (Ceph/Longhorn) is available. | Workloads require unsupported platforms, storage configurations or host kernel capabilities, or simpler managed storage meets the requirements. |
| `documentation_url` | Absent | https://hwameistor.io/docs/install/prereq |
| `license_spdx` | Absent | Apache-2.0 |
| `sources` | Original two legacy entries | Original ordered prefix plus five URLs below |

Original source prefix:

- `legacy:4_Kubernetes-Containers/README.md#L102`
- `legacy:devopstools_final.md#L576`

Append:

- https://github.com/hwameistor/hwameistor/blob/1d2d50ccf095a8a8a54aecac677cd6441269e4f1/README.md
- https://github.com/hwameistor/hwameistor/blob/1d2d50ccf095a8a8a54aecac677cd6441269e4f1/LICENSE
- https://github.com/hwameistor/hwameistor/blob/1d2d50ccf095a8a8a54aecac677cd6441269e4f1/docs/docs/modules/ls.md
- https://github.com/hwameistor/hwameistor/releases/tag/v1.1.2
- https://hwameistor.io/docs/install/prereq

Apache-2.0 applies to the reviewed upstream repository, not automatically to third-party DRBD kernel modules.

The stable documentation distinguishes local HA and non-HA volumes. Current compatibility evidence is insufficient for a comprehensive support assertion across recent Kubernetes and host-kernel versions.

Retain unknown maturity, original verification date and review debt.

Exact changed-key allowlist:

`summary`, `use_when`, `avoid_when`, `documentation_url`, `license_spdx`, `sources`.

**6 keys.**

### 4.6. truenas — RETAIN

**Evidence boundary:** complete TrueNAS storage distribution, not only its middleware repository.

| Field | Before | After |
| --- | --- | --- |
| `summary` | Storage platform/OS for NAS and SAN with community and enterprise editions. | ZFS-based NAS and SAN storage platform with Community and licensed Enterprise functionality. |
| `use_when` | You need a feature-rich NAS/SAN platform with ZFS for home lab or enterprise file storage. | You need ZFS-based file or block storage and can select hardware and features appropriate to the TrueNAS edition. |
| `avoid_when` | You need Kubernetes-native distributed block storage (use Longhorn/Rook instead). | You require an independently managed Kubernetes-native distributed storage backend rather than an external storage platform. |
| `documentation_url` | Absent | https://www.truenas.com/docs/scale/25.10/ |
| `sources` | Original two legacy entries | Original ordered prefix plus five URLs below |

Original source prefix:

- `legacy:4_Kubernetes-Containers/README.md#L176`
- `legacy:devopstools_final.md#L680`

Append:

- https://github.com/truenas/middleware/blob/29ed02b8082f38494b0d2896bada8151f0d59716/README.md
- https://github.com/truenas/middleware/blob/29ed02b8082f38494b0d2896bada8151f0d59716/LICENSE
- https://github.com/truenas/middleware/blob/29ed02b8082f38494b0d2896bada8151f0d59716/LICENSE.IX
- https://www.truenas.com/docs/scale/26/gettingstarted/useragreements/softwaredevelopmentlifecycle/
- https://www.truenas.com/docs/scale/25.10/

The middleware tag TS-25.10.8 resolves to the reviewed source revision. LGPL v3 and separately licensed Enterprise portions are documented.

The vendor explicitly describes an open-core product model.

Do not interpret the 25.10 documentation URL as the latest recommended version for every hardware or Enterprise support scenario.

Do not equate middleware licensing with the entire distribution, OpenZFS, third-party packages or all Enterprise features.

Preserve `open-core`, absent repository URL and SPDX, unknown maturity, original verification date and review debt.

Exact changed-key allowlist:

`summary`, `use_when`, `avoid_when`, `documentation_url`, `sources`.

**5 keys.**

### 4.7. k8s-csi-s3 — RETAIN

**Evidence boundary:** CSI/FUSE access to S3 object storage, not native POSIX block storage.

| Field | Before | After |
| --- | --- | --- |
| `summary` | CSI driver for mounting S3-compatible object storage as Kubernetes persistent volumes. | Kubernetes CSI driver that exposes S3-compatible object storage through FUSE-mounted persistent volumes. |
| `use_when` | Empty list | Applications require mounted access to S3-compatible objects and tolerate the selected mounter's documented filesystem semantics. |
| `avoid_when` | Empty list | Workloads require native block storage, strict POSIX or transactional consistency guarantees, or privileged CSI containers are prohibited. |
| `documentation_url` | Absent | https://github.com/yandex-cloud/k8s-csi-s3/blob/cd2d29f0e655e30812c75fa5fb4c212cc04631b4/README.md |
| `license_spdx` | Absent | Apache-2.0 |
| `sources` | Original legacy entry | Original ordered prefix plus three URLs below |

Original source prefix:

- `legacy:devopstools_final.md#L578`

Append:

- https://github.com/yandex-cloud/k8s-csi-s3/blob/cd2d29f0e655e30812c75fa5fb4c212cc04631b4/README.md
- https://github.com/yandex-cloud/k8s-csi-s3/blob/cd2d29f0e655e30812c75fa5fb4c212cc04631b4/LICENSE
- https://github.com/yandex-cloud/k8s-csi-s3/releases/tag/v0.43.7

The actual licence file grants Apache-2.0 rights for the reviewed driver.

The README documents privileged-container requirements, S3 credentials, FUSE limitations and deletion consequences.

A historical Kubernetes minimum-version statement does not establish tested support for all newer releases.

Do not generalize the driver licence to every mounter, backend or external service.

Preserve unknown maturity, original verification date and review debt.

Exact changed-key allowlist:

`summary`, `use_when`, `avoid_when`, `documentation_url`, `license_spdx`, `sources`.

**6 keys.**

### 4.8. pv-migrate — CLEAR candidate

**Evidence boundary:** PVC data migration and object-storage backup/restore, not an application-consistent backup platform.

| Field | Before | After |
| --- | --- | --- |
| `summary` | CLI tool for migrating data between Kubernetes Persistent Volumes. | CLI and kubectl plugin for copying Kubernetes PVC data and backing up or restoring PVC contents through object storage. |
| `use_when` | You need to move PV data across storage classes, namespaces, or clusters. | You need PVC-to-PVC data migration across supported storage, namespace or cluster boundaries, or file-level backup and restore through object storage. |
| `avoid_when` | Your storage backend supports native volume cloning or VolSync handles replication. | You require application-consistent backups, managed retention, restore verification or continuous replication without additional controls. |
| `documentation_url` | Absent | https://github.com/utkuozdemir/pv-migrate/blob/7ba089ec1d0dd2b202952ba183d0c4a2198c4323/README.md |
| `license_spdx` | Absent | Apache-2.0 |
| `maturity` | unknown | growing |
| `status` | needs-review | active |
| `needs_review` | true | false |
| `verified_on` | 2026-08-03 | 2026-11-26 |
| `sources` | Original two legacy entries | Original ordered prefix plus four URLs below |

Original source prefix:

- `legacy:4_Kubernetes-Containers/README.md#L130`
- `legacy:devopstools_final.md#L623`

Append:

- https://github.com/utkuozdemir/pv-migrate/blob/7ba089ec1d0dd2b202952ba183d0c4a2198c4323/README.md
- https://github.com/utkuozdemir/pv-migrate/blob/7ba089ec1d0dd2b202952ba183d0c4a2198c4323/LICENSE
- https://github.com/utkuozdemir/pv-migrate/blob/7ba089ec1d0dd2b202952ba183d0c4a2198c4323/docs/backup-restore.md
- https://github.com/utkuozdemir/pv-migrate/releases/tag/v3.8.0

Both migration and bucket backup/restore workflows are confirmed at the stable release commit.

The documentation explicitly excludes automatic application consistency, retention management and comprehensive restore verification.

Operational review must preserve RBAC, network exposure, destination deletion and credential-handling caveats.

The maintainer identifies this as a spare-time project. The proposed `growing` maturity is an editorial judgement based on sustained releases and expanding documented functionality, not adoption statistics or a commercial support guarantee.

Exact changed-key allowlist:

`summary`, `use_when`, `avoid_when`, `documentation_url`, `license_spdx`, `maturity`, `status`, `needs_review`, `verified_on`, `sources`.

**10 keys.**

### 4.9. moco — CLEAR candidate

**Evidence boundary:** MySQL GTID-based semi-synchronous replication, explicitly not Group Replication.

| Field | Before | After |
| --- | --- | --- |
| `summary` | MySQL Operator for Kubernetes by Cybozu. | Kubernetes operator for MySQL clusters using GTID-based semi-synchronous replication, with primary failover and backup/PITR support. |
| `use_when` | You need automated MySQL InnoDB Cluster management on Kubernetes with GTID-based replication. | You need automated management of MySQL primary and replica instances using GTID-based semi-synchronous replication on Kubernetes. |
| `avoid_when` | A managed MySQL service (RDS/Cloud SQL) reduces your operational burden. | You specifically require MySQL InnoDB Cluster or Group Replication, or a managed database service better meets your operational needs. |
| `documentation_url` | Absent | https://cybozu-go.github.io/moco/ |
| `license_spdx` | Absent | Apache-2.0 |
| `maturity` | unknown | growing |
| `status` | needs-review | active |
| `needs_review` | true | false |
| `verified_on` | 2026-08-03 | 2026-11-26 |
| `sources` | Original two legacy entries | Original ordered prefix plus four URLs below |

Original source prefix:

- `legacy:4_Kubernetes-Containers/README.md#L125`
- `legacy:devopstools_final.md#L609`

Append:

- https://github.com/cybozu-go/moco/blob/acb2716d1ef13a8953dd18d55cf230c0edf90f04/README.md
- https://github.com/cybozu-go/moco/blob/acb2716d1ef13a8953dd18d55cf230c0edf90f04/LICENSE
- https://github.com/cybozu-go/moco/releases/tag/v0.38.0
- https://cybozu-go.github.io/moco/

The stable README explicitly excludes Group Replication. This resolves the canonical architectural conflation.

The reviewed root licence is Apache-2.0. It does not establish the licence of MySQL Server, all container images or third-party components.

The `growing` maturity judgement reflects sustained releases, documented failover and recovery workflows and maintained compatibility documentation. It does not assert increasing adoption.

Exact changed-key allowlist:

`summary`, `use_when`, `avoid_when`, `documentation_url`, `license_spdx`, `maturity`, `status`, `needs_review`, `verified_on`, `sources`.

**10 keys.**

### 4.10. mysql-operator-for-kubernetes — RETAIN

**Evidence boundary:** reviewed Community operator source versus broader commercial and distribution-specific rights.

| Field | Before | After |
| --- | --- | --- |
| `use_when` | Empty list | You need operator-managed MySQL InnoDB Cluster deployment, maintenance, upgrades and backups on Kubernetes. |
| `avoid_when` | Empty list | You require a GTID-based semi-synchronous replication architecture instead of Group Replication, or prefer a managed database service. |
| `documentation_url` | Absent | https://dev.mysql.com/doc/mysql-operator/en/ |
| `sources` | Original legacy entry | Original ordered prefix plus four URLs below |

Original source prefix:

- `legacy:devopstools_final.md#L610`

Append:

- https://github.com/mysql/mysql-operator/blob/e21334e9179ccea6c8a12205dd5a708a46fbad26/README.md
- https://github.com/mysql/mysql-operator/blob/e21334e9179ccea6c8a12205dd5a708a46fbad26/LICENSE
- https://dev.mysql.com/doc/mysql-operator/en/
- https://dev.mysql.com/downloads/operator/

The reviewed Community LICENSE explicitly identifies UPL version 1.0.

The newer release note for 26.10.0.1-2.3.2 does not establish correspondence with the reviewed source. Its attempted GitHub commit resolution returned HTTP 422. The official downloads page inspected on 2026-11-26 still presented 26.10.0-2.3.1 archives.

Do not assign UPL-1.0 to the entire generic product entry until the distribution scope is explicitly resolved and accepted.

Preserving the pre-existing OSS classification is not independent validation of a universal product-wide licence.

Preserve the original summary, existing licence model, absent SPDX, unknown maturity, original verification date and review debt.

Exact changed-key allowlist:

`use_when`, `avoid_when`, `documentation_url`, `sources`.

**4 keys.**

## Residual limitations
The following uncertainties are intentionally retained rather than concealed:

- Ceph: full component/distribution licensing inventory not established.
- LINSTOR: GPL v3 root files versus GPL-2.0-or-later Debian copyright declaration.
- Portworx: no complete commercial agreement or parent-wide source repository established.
- HwameiStor: comprehensive current Kubernetes and host-kernel support matrix not established.
- TrueNAS: complete distribution and Enterprise component licence inventory not established.
- k8s-csi-s3: current compatibility and all mounter/backend guarantees not established.
- MySQL Operator: newer-release source correspondence and generic Community/Commercial identity boundary remain unresolved.

For Rook, pv-migrate and MOCO, source-licence conclusions are scoped to the examined upstream source. Third-party dependencies and distributed artifacts require independent legal assessment where relevant.

No complete CVE audit, runtime deployment test, binary verification or cryptographic release-signature verification was performed.

The maturity classifications and the Portworx/LINSTOR identity boundaries remain subject to the accepted contract and its explicit scope restrictions; no implementation is authorized.

## Validation boundary

Local validation and exact-SHA remote checks are separate gates. No remote publication or merge is authorized by this ledger. Preserve the existing PyYAML temporary hold and strict link audit baseline.
