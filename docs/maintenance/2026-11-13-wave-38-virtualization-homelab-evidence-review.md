# Wave 38 — Virtualization, bare metal and homelab evidence review

Primary sources were checked on **2026-11-13** for the corrections listed below. The local patch follows the [field decisions](https://github.com/goozcena-gnl/devops-tools-catalog/issues/171#issuecomment-6853948635) and the [D1 and D2 checkpoint](https://github.com/goozcena-gnl/devops-tools-catalog/issues/171#issuecomment-6854323997) in issue #171. The branch is `maintenance/wave-38-virtualization-homelab-evidence-review`. The frozen commit and verified remote `main` are `554b522610038c6cdff1ef3833363d36c1675997`, with canonical YAML blob `fc1f29e7c7afab1a0104e75dc4894ceb98dbb20e`.

All ten records retain `status: needs-review`, `needs_review: true`, `maturity: unknown`, and `verified_on: '2026-08-03'`. The date above records the scope of this field review. The canonical date remains the historical date because the patch does not establish a complete record-level review. Existing source entries are preserved in their original order. SPDX values below describe the named upstream source, with edition and component limits documented per record.

## Dispositions and remaining uncertainties

| Record | Proposed disposition | Primary evidence and remaining uncertainties |
| --- | --- | --- |
| `incus-os` | CLEAR candidate | The project documents an immutable Incus host OS managed through an authenticated API, with atomic A/B updates. Secure Boot and TPM 2.0 are the standard configuration. For homelab/evaluation, degraded-security configurations permit either Secure Boot disabled or a software TPM, but never both simultaneously; both weaken security. Enterprise deployment without Secure Boot is not recommended, and use without a physical TPM is unsupported there. The build repository's Apache-2.0 licence covers its own code. The installed OS includes separately licensed components, so product-level SPDX remains unset. The upstream maintainer's 2026-08-27 notice supplies dated project context. The upstream image index and download guide describe stable and testing delivery. See [documentation](https://linuxcontainers.org/incus-os/docs/main/), [requirements](https://linuxcontainers.org/incus-os/docs/main/getting-started/requirements/), [licence inventory](https://linuxcontainers.org/incus-os/docs/main/reference/licenses/), [source](https://github.com/lxc/incus-os), [download guide](https://linuxcontainers.org/incus-os/docs/main/getting-started/download/), and [maintainer notice](https://discuss.linuxcontainers.org/t/upcoming-changes-to-incusos/27161), [no-Secure-Boot procedure](https://linuxcontainers.org/incus-os/docs/main/reference/installing-without-secureboot/), and [software-TPM procedure](https://linuxcontainers.org/incus-os/docs/main/reference/installing-without-tpm/). |
| `libvirt` | CLEAR candidate | The official download page identifies GitLab as the upstream and GitHub as a read-only mirror. The C library and daemon tooling span LGPL and GPL code, so a single SPDX remains unset. Supported virtualization drivers depend on the installation. Upstream lists v12.9.0 on 2026-11-02. See [downloads and origins](https://libvirt.org/downloads.html), [driver list](https://libvirt.org/drivers.html), [mirror and licence files](https://github.com/libvirt/libvirt), and [release history](https://libvirt.org/news.html#v12-9-0-2026-11-02). |
| `lima` | CLEAR candidate | macOS and Linux are documented hosts. The installation page marks Windows, NetBSD, and DragonFlyBSD untested. Apache-2.0 covers Lima's source, with guest images and dependencies outside that claim. The v2.3.0 release was published on 2026-11-06 and introduces experimental Windows-host support through the HCS driver; this does not override the installation page's 'untested' classification or establish general Windows support. See [project documentation](https://lima-vm.io/docs/), [installation](https://lima-vm.io/docs/installation/), [source licence](https://github.com/lima-vm/lima/blob/master/LICENSE), and [release](https://github.com/lima-vm/lima/releases/tag/v2.3.0). |
| `portainer` | CLEAR candidate | The vendor distinguishes open-source CE from key-licensed BE. Zlib applies to the CE repository, with BE binaries, entitlements, and support outside that licence claim. The CE 2.45.3 LTS release was published on 2026-10-21. Edition-specific platform and support coverage remains subject to the vendor's documentation. See [edition and support documentation](https://docs.portainer.io/), [CE installation](https://docs.portainer.io/start/install-ce), [CE licence](https://github.com/portainer/portainer/blob/release/2.45/LICENSE), and [CE release](https://github.com/portainer/portainer/releases/tag/2.45.3). |
| `proxmox-datacenter-manager` | CLEAR candidate | Version 1.1.9 documentation is dated 2026-10-14. Proxmox's product-specific repository and its copyright file explicitly confirm AGPL-3.0-or-later for the source. The FAQ ties support and enterprise-repository eligibility to qualifying remote subscriptions and specifies no dedicated PDM subscription. The patch leaves the standalone commercial-offering flag unset. See [versioned manual](https://pdm.proxmox.com/docs/), [scope and licence](https://pdm.proxmox.com/docs/introduction.html), [subscription FAQ](https://pdm.proxmox.com/docs/faq.html), [source repository](https://git.proxmox.com/?p=proxmox-datacenter-manager.git;a=summary), and [source copyright](https://git.proxmox.com/?p=proxmox-datacenter-manager.git;a=blob_plain;f=debian/copyright;hb=HEAD). |
| `proxmox-virtual-environment-ve` | CLEAR candidate | The product includes KVM and LXC in a web-managed self-hosted platform. Subscriptions provide support and enterprise repository access. The vendor identifies the source as GNU AGPLv3. A single product-wide SPDX modifier and repository remain unresolved for this packaged, multi-component platform. The vendor published VE 9.2 on 2026-05-21. See [product](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview), [features and source licence](https://www.proxmox.com/en/products/proxmox-virtual-environment/features), [subscriptions](https://www.proxmox.com/en/products/proxmox-virtual-environment/pricing/), and [release](https://www.proxmox.com/en/about/company-details/press-releases/proxmox-virtual-environment-9-2). |
| `rancher-desktop` | CLEAR candidate | Windows, macOS, and Linux are documented desktop hosts. The Windows installer requires WSL. Kubernetes can be disabled while running containerd or dockerd. Apache-2.0 covers the project source. The v1.25.0 release was published on 2026-11-05. The patch leaves desktop deployment taxonomy and any cross-version support commitment open. See [documentation](https://docs.rancherdesktop.io/), [installation](https://docs.rancherdesktop.io/getting-started/installation/), [Kubernetes preference](https://docs.rancherdesktop.io/ui/preferences/kubernetes/), [source licence](https://github.com/rancher-sandbox/rancher-desktop/blob/main/LICENSE), and [release](https://github.com/rancher-sandbox/rancher-desktop/releases/tag/v1.25.0). |
| `unraid` | CLEAR candidate | Lime Technology licenses the packaged Unraid OS commercially. Bundled open-source components retain their own licences. Starter and Unleashed are perpetual purchases with one year of updates and optional extensions. Lifetime includes updates for the life of the product. Product-wide OSS SPDX and a product source repository remain unset. The vendor's 7.4.0 release notes are dated 2026-11-10. See [EULA](https://unraid.net/policies), [licensing FAQ](https://docs.unraid.net/unraid-os/faq/licensing-faq/), [VM and container documentation](https://docs.unraid.net/unraid-os/using-unraid-to/create-virtual-machines/overview-and-system-prep/), and [release](https://docs.unraid.net/unraid-os/release-notes/7.4.0/). |
| `linux-containers-lxc-lxd` | RETAIN (D1) | LXC is the Linux container userspace tooling, with an LGPL-2.1-or-later default and GPL/BSD exceptions. LXD moved to Canonical in 2023. Canonical's LXD contributions default to AGPL-3.0-only with marked exceptions. Incus is a separate community fork with Apache-2.0 source. The historical umbrella ID requires an explicit decision on whether to keep umbrella scope or create distinct entries. Both repository identity and a single SPDX remain unresolved. See [LXC licensing](https://linuxcontainers.org/lxc/#licensing), [LXD transfer](https://linuxcontainers.org/lxd/), [LXD contribution licence](https://raw.githubusercontent.com/canonical/lxd/main/CONTRIBUTING.md), and [Incus source licence](https://github.com/lxc/incus/blob/main/COPYING). |
| `vates-vms` | RETAIN (D2) | Vates sells a VMS subscription that combines XCP-ng and Xen Orchestra Appliance with professional support. XCP-ng licences grant support for the open-source hypervisor. XOA licences unlock commercial appliance features. The catalogue still needs an explicit choice between the paid VMS bundle and the broader stack family. A product-wide SPDX and single repository remain unresolved. See [bundle](https://docs.vates.tech/pricing-licencing/vms-bundle-overview/), [XCP-ng support licences](https://docs.vates.tech/pricing-licencing/applying-xcpng-licences/), and [XOA entitlements](https://docs.vates.tech/pricing-licencing/applying-xo-licences/). |

## Exact field changes

Each entry gives the baseline and worktree value. The appended `sources` are listed in their YAML order.

### `incus-os`

- `summary` changed from `"Operating system images and distribution tooling for Incus environments."` to `"Immutable, API-managed host OS dedicated to Incus, with UEFI Secure Boot, TPM 2.0, and atomic A/B updates."`.
- `repository_url` changed from `absent` to `"https://github.com/lxc/incus-os"`.
- `documentation_url` changed from `absent` to `"https://linuxcontainers.org/incus-os/docs/main/"`.
- `use_when` changed from `[]` to `["You want an immutable host dedicated to running Incus."]`.
- `avoid_when` changed from `[]` to `["You need host shell access, or require enterprise-supported security but cannot provide Secure Boot and a physical TPM 2.0; degraded homelab/evaluation modes weaken security."]`.
- `deployment_models` changed from `[]` to `["self-hosted"]`.

Appended `sources`

- <https://linuxcontainers.org/incus-os/docs/main/>
- <https://linuxcontainers.org/incus-os/docs/main/getting-started/requirements/>
- <https://linuxcontainers.org/incus-os/docs/main/reference/installing-without-secureboot/>
- <https://linuxcontainers.org/incus-os/docs/main/reference/installing-without-tpm/>
- <https://linuxcontainers.org/incus-os/docs/main/reference/licenses/>
- <https://github.com/lxc/incus-os>
- <https://discuss.linuxcontainers.org/t/upcoming-changes-to-incusos/27161>

### `libvirt`

- `summary` changed from `"API/daemon for managing virtualization platforms."` to `"C library, API, and daemons for managing virtualization through drivers such as QEMU/KVM and Xen."`.
- `repository_url` changed from `"https://github.com/libvirt/libvirt"` to `"https://gitlab.com/libvirt/libvirt"`.
- `documentation_url` changed from `absent` to `"https://libvirt.org/docs.html"`.

Appended `sources`

- <https://libvirt.org/docs.html>
- <https://libvirt.org/downloads.html>
- <https://libvirt.org/drivers.html>
- <https://gitlab.com/libvirt/libvirt>
- <https://github.com/libvirt/libvirt>
- <https://libvirt.org/news.html#v12-9-0-2026-11-02>

### `lima`

- `summary` changed from `"Linux VMs on macOS (and more)."` to `"Runs Linux virtual machines on macOS and Linux hosts for local container and development workflows."`.
- `use_when` changed from `["You need lightweight Linux VMs on macOS for container development without Docker Desktop."]` to `["You need local Linux VMs for container development on macOS or Linux."]`.
- `avoid_when` changed from `["You're on Linux or prefer a more integrated solution like OrbStack."]` to `["You require a tested host platform and plan to run Lima on Windows, NetBSD, or DragonFlyBSD."]`.
- `license_spdx` changed from `absent` to `"Apache-2.0"`.

Appended `sources`

- <https://lima-vm.io/docs/>
- <https://lima-vm.io/docs/installation/>
- <https://github.com/lima-vm/lima/blob/master/LICENSE>
- <https://github.com/lima-vm/lima/releases/tag/v2.3.0>

### `portainer`

- `summary` changed from `"Container management platform."` to `"Self-hosted Docker and Kubernetes management with an open-source Community Edition and a separately licensed Business Edition."`.
- `documentation_url` changed from `absent` to `"https://docs.portainer.io/"`.
- `deployment_models` changed from `[]` to `["self-hosted"]`.
- `license_spdx` changed from `absent` to `"Zlib"`.
- `commercial_offering` changed from `absent` to `true`.

Appended `sources`

- <https://docs.portainer.io/>
- <https://docs.portainer.io/start/install-ce>
- <https://github.com/portainer/portainer/blob/release/2.45/LICENSE>
- <https://github.com/portainer/portainer/releases/tag/2.45.3>

### `proxmox-datacenter-manager`

- `summary` changed from `"Proxmox datacenter management product."` to `"Centralizes inventory, monitoring, and operations across independent Proxmox VE and Proxmox Backup Server remotes."`.
- `repository_url` changed from `absent` to `"https://git.proxmox.com/?p=proxmox-datacenter-manager.git;a=summary"`.
- `documentation_url` changed from `absent` to `"https://pdm.proxmox.com/docs/"`.
- `deployment_models` changed from `[]` to `["self-hosted"]`.
- `license_model` changed from `"unknown"` to `"oss"`.
- `license_spdx` changed from `absent` to `"AGPL-3.0-or-later"`.

Appended `sources`

- <https://pdm.proxmox.com/docs/>
- <https://pdm.proxmox.com/docs/introduction.html>
- <https://pdm.proxmox.com/docs/faq.html>
- <https://git.proxmox.com/?p=proxmox-datacenter-manager.git;a=summary>
- <https://git.proxmox.com/?p=proxmox-datacenter-manager.git;a=blob_plain;f=debian/copyright;hb=HEAD>

### `proxmox-virtual-environment-ve`

- `summary` changed from `"Open source virtualization platform (KVM + LXC) with optional enterprise subscription."` to `"Open-source server virtualization platform with a web UI for KVM VMs and LXC containers. Optional subscriptions provide enterprise repository access and support."`.
- `official_url` changed from `"https://github.com/proxmox"` to `"https://www.proxmox.com/en/products/proxmox-virtual-environment/overview"`.
- `avoid_when` changed from `["You need VMware-level enterprise support or advanced vSAN features."]` to `["You require a vendor-hosted virtualization service."]`.
- `deployment_models` changed from `[]` to `["self-hosted"]`.
- `license_model` changed from `"open-core"` to `"oss"`.
- `commercial_offering` changed from `absent` to `true`.

Appended `sources`

- <https://www.proxmox.com/en/products/proxmox-virtual-environment/overview>
- <https://www.proxmox.com/en/products/proxmox-virtual-environment/features>
- <https://www.proxmox.com/en/products/proxmox-virtual-environment/pricing/>
- <https://www.proxmox.com/en/about/company-details/press-releases/proxmox-virtual-environment-9-2>

### `rancher-desktop`

- `summary` changed from `"Desktop Kubernetes and container management."` to `"Local container management on Windows, macOS, and Linux, with optional Kubernetes."`.
- `documentation_url` changed from `absent` to `"https://docs.rancherdesktop.io/"`.
- `use_when` changed from `["You want a free, open-source Docker Desktop alternative with built-in K8s."]` to `["You need a local Docker or containerd workflow, with or without Kubernetes."]`.
- `avoid_when` changed from `["You don't need local Kubernetes and just want a simple Docker environment."]` to `["You need a platform to operate remote production clusters."]`.
- `license_spdx` changed from `absent` to `"Apache-2.0"`.

Appended `sources`

- <https://docs.rancherdesktop.io/>
- <https://docs.rancherdesktop.io/getting-started/installation/>
- <https://docs.rancherdesktop.io/ui/preferences/kubernetes/>
- <https://github.com/rancher-sandbox/rancher-desktop/blob/main/LICENSE>
- <https://github.com/rancher-sandbox/rancher-desktop/releases/tag/v1.25.0>

### `unraid`

- `summary` changed from `"Operating system for network-attached storage and virtualization."` to `"Commercial, self-hosted operating system for network-attached storage, Docker containers, and virtual machines."`.
- `documentation_url` changed from `absent` to `"https://docs.unraid.net/"`.
- `deployment_models` changed from `[]` to `["self-hosted"]`.
- `license_model` changed from `"unknown"` to `"commercial"`.
- `commercial_offering` changed from `absent` to `true`.

Appended `sources`

- <https://docs.unraid.net/>
- <https://unraid.net/policies>
- <https://docs.unraid.net/unraid-os/faq/licensing-faq/>
- <https://docs.unraid.net/unraid-os/using-unraid-to/create-virtual-machines/overview-and-system-prep/>
- <https://docs.unraid.net/unraid-os/release-notes/7.4.0/>


## Inventory impact

| Metric | Frozen baseline | Worktree |
| --- | ---: | ---: |
| Canonical records | 1,425 | 1,425 |
| Taxonomy categories | 30 | 30 |
| Active status | 874 | 874 |
| Needs-review status | 537 | 537 |
| Records requiring review | 537 | 537 |
| Unknown licence model | 68 | 66 |
| Commercial licence model | 174 | 175 |
| OSS licence model | 929 | 931 |
| Open-core licence model | 113 | 112 |
| Scoped YAML blocks | 68 | 68 |
| Scoped blocks requiring review | 33 | 33 |
| Scoped blocks with unknown licence model | 2 | 0 |

The review-debt report counts 72 records tagged with this category across all YAML files, including four stored in other canonical files. It reports 33 requiring review and zero with an unknown licence model for the category. The global review-debt reference date is 2026-11-12, the latest canonical verification date.

## Local changed-file allowlist

- `data/tools/virtualization-bare-metal-homelab.yaml`
- `docs/maintenance/2026-11-13-wave-38-virtualization-homelab-evidence-review.md`
- `README.md` (generated)
- `docs/catalog-statistics.json` (generated)
- `docs/categories/virtualization-bare-metal-homelab.md` (generated)
- `docs/lifecycle/deploy.md` (generated)
- `docs/lifecycle/operate.md` (generated)
- `docs/roles/devops-engineer.md` (generated)
- `docs/roles/infrastructure-systems-engineer.md` (generated)


## Local validation

| Check | Result |
| --- | --- |
| Clean worktree, exact branch and HEAD, live remote main, frozen blob, and 68/10/58 inventory | PASS |
| `python -m pip install -e '.[dev]'` | PASS in an isolated Python 3.12 environment |
| `python -m scripts.generate_docs` and `python -m scripts.generate_docs --check` | PASS |
| `python -m scripts.validate_catalog` | PASS |
| `python -m scripts.review_debt --format json` | PASS |
| `python -m ruff check scripts tests` and `python -m ruff format --check scripts tests` | PASS |
| `python -m pytest` | PASS, 1,004 passed and 8 skipped on the full rerun with a dedicated Windows temporary directory |
| `python -m pip check` | PASS |
| Wave 38 v2 guard with `--source worktree --check-remote` | PASS, exactly eight modified blocks |
| Raw protected blocks, original provenance, generator allowlist, and clean index | PASS |
| `git diff --check` | PASS |
| Strict Full link audit and GitHub CI | NOT RUN |

The first pytest invocation hit Windows temporary-directory setup errors and was stopped after the full rerun began passing. The two RETAIN blocks and 58 out-of-cohort blocks match their original Windows checkout bytes, and the v2 guard also verifies them against the frozen Git blob after CRLF normalization.
