# Wave 31 — Backup & Disaster Recovery — revue de preuves

**2026-10-29 (Europe/Paris). Statut : première application de métadonnées, documentation générée / CI / audit strict NON encore exécutés sur le HEAD final. Aucune fusion autorisée par cette note.**

## 1. Baseline, sélection et invariants

- Dépôt : https://github.com/goozcena-gnl/devops-tools-catalog
- `main` vérifié à `92abd441202370c58eada3c9af5c628928507349`, aucune PR ouverte au lancement.
- Fichier canonique : `data/tools/backup-disaster-recovery-resilience.yaml`, blob d'origine `b54925feac971115fa70c33766dcaa0aa53b392f`; exactement **13** entrées, **5** initialement à revoir.
- Baseline des liens : `config/link-audit-baseline.json`, SHA blob `a834e2af711693def40078a55e31dfeb29bee2c7`, **inchangée**.
- Cohorte fermée : `borgbackup`, `kube-dump`, `stash`, `trilio`, `volsync`. Les **8 autres entrées sont strictement inchangées**.
- Décision : **4 CLEAR**, **1 RETAIN** (`kube-dump`), **54 champs** modifiés parmi ces cinq fiches. `maturity: unknown` demeure pour les cinq fiches ; aucune évaluation de maturité arbitraire.
- Projection (non validée tant que la CI / génération ne le confirme pas) : **1425** fiches, **839 active**, **572 needs-review**, **76 unknown licence models** ; licences modèles **oss 930**, **source-available 31**, **commercial 165**.
- Aucun ajout/suppression de fiche. Aucun changement de taxonomie, schéma, workflow, dépendance Python, baseline de lien, ou issue #2.

## 2. Sources primaires vérifiées

Dépôts canoniques, fichiers de licence **figés par commit**, documentation officielle, releases amont, et pages éditeur. `GitHub archived: false` ne prouve pas à lui seul la maintenance. `pushed_at` ne correspond pas forcément à la date du dernier commit sur la branche par défaut.

| Identifiant | Décision | Dépôt / éditeur | Source juridique principale | SHA amont examiné |
|---|---|---|---|---|
| `borgbackup` | **CLEAR** | [`borgbackup/borg`](https://github.com/borgbackup/borg) | [licence figée](https://github.com/borgbackup/borg/blob/62051de6a0f90eab5f18a55871f9881542800e6c/LICENSE) | `62051de6a0f90eab5f18a55871f9881542800e6c` |
| `kube-dump` | **RETAIN** | [`WoozyMasta/kube-dump`](https://github.com/WoozyMasta/kube-dump) | [licence figée](https://github.com/WoozyMasta/kube-dump/blob/f1ae560a8b9da8dba1c28619f38089d40d0d2357/LICENSE) | `f1ae560a8b9da8dba1c28619f38089d40d0d2357` |
| `stash` | **CLEAR** | [`stashed/stash`](https://github.com/stashed/stash) | [licence figée](https://github.com/stashed/stash/blob/1c655538dd4fa50ec1af1f322300758990940125/LICENSE.md) | `1c655538dd4fa50ec1af1f322300758990940125` |
| `trilio` | **CLEAR** | [Trilio officiel](https://trilio.io/products/kubernetes-backup-and-recovery/) | [conditions d'abonnement](https://trilio.io/resources/kubernetes-backup-frequently-asked-questions/) | N/A |
| `volsync` | **CLEAR** | [`backube/volsync`](https://github.com/backube/volsync) | [licence figée](https://github.com/backube/volsync/blob/7ba1990e0b2233a1bf6bb47466bee3ef1de1881f/LICENSE) | `7ba1990e0b2233a1bf6bb47466bee3ef1de1881f` |

## 3. Justification par outil

### BorgBackup — CLEAR

- Release stable GitHub **1.4.5** publiée en juillet 2026. Le fichier `LICENSE` fournit les clauses de **BSD-3-Clause** ; la documentation versionnée `stable` présente les backups dédupliqués, l'encryption optionnelle, la restauration et les dépôts distants via SSH.
- La branche `master` est actuellement consacrée à **Borg2 beta instable** ; ne pas recommander un binaire ou une syntaxe Borg2 comme solution de production stable.
- Limites : filesystem/VM sans coordination applicative ≠ backup transactionnel, stockage des clés de chiffrement indispensable, tests de restauration. `maturity` conservée `unknown`.

### kube-dump — RETAIN

- Le dépôt officiel `WoozyMasta/kube-dump` contient un texte GPL v3 (GNU GPL-3.0-only) ; l'inventaire GitHub renvoie GPL-3.0. Le registre Docker peut afficher d'autres métadonnées de licence : la licence du dépôt figé est la preuve retenue pour le code.
- Dernière release GitHub **1.1.2** et dernier commit de la branche par défaut observés le **2022-05-19**, même si le dépôt n'est pas archivé. **Maintenance et compatibilité Kubernetes moderne non établies** : conserver `status: needs-review`, `needs_review: true`.
- Le README explique l'export d'objets en manifests YAML, **pas** la sauvegarde de données PVC ; une possibilité de pousser le dump sur Git est décrite et **git-crypt est un projet**, pas une protection actuelle garantie. Éviter les Secrets non chiffrés dans les dépôts ou artefacts.
- Cette fiche n'est pas « cleared » uniquement parce que sa licence est connue.

### Stash — CLEAR, licence corrigée

- Le README amont distingue Community et Enterprise. Cependant le fichier **`stashed/stash/LICENSE.md`** présent au commit examiné soumet les sources, binaires, images et charts à **AppsCode Community License 1.0.0** : https://github.com/appscode/licenses/blob/1.0.0/AppsCode-Community-1.0.0.md
- La licence limite entre autres redistribution, œuvres dérivées et usage concurrentiel. **Elle n'est pas une licence open-source OSI**, même si du contenu marketing utilise les mots « open source community ». Classification : **`source-available`**, pas `oss` ni `open-core` au sens standard.
- Pas de valeur `license_spdx` inventée pour ce texte juridique non standard ; la source exacte fait foi. Edition Enterprise payante/fonctions spécifiques (sauvegarde bases de données, configuration avancée). Vérifier l'édition et son droit d'usage avant production.
- Documents versionnés Stash : https://stash.run/docs/v2025.10.17/welcome/ ; https://stash.run/docs/v2025.10.17/concepts/what-is-stash/overview/

### Trilio — CLEAR, commercial

- Le fournisseur décrit une solution Kubernetes et KubeVirt installée chez le client, et **non** un SaaS obligatoire ; sauvegarde/restauration des objets applicatifs et volumes, avec prérequis CSI et politique de restauration.
- Le FAQ éditeur précise **une licence par abonnement basée sur les vCPU des workers** : https://trilio.io/resources/kubernetes-backup-frequently-asked-questions/ ; essais limités : https://trilio.io/kubernetes-backup-trial/
- Classifier `commercial` ; `commercial_offering: true` ; aucune `license_spdx` open source inventée. Document officiel : https://docs.trilio.io/kubernetes
- Ne pas extrapoler les tarifs historiques ni les limitations des anciennes éditions gratuites aux offres 2026.

### VolSync — CLEAR, AGPL précise

- Projet `backube/volsync` actif, release GitHub **v0.17.0** du 21 octobre 2026. Le LICENSE du cœur est **AGPL-3.0-only** (pas Apache-2.0 ni MIT).
- Exception explicitement indiquée dans le README : fichiers `api/*` **aussi sous Apache-2.0**, documentation **CC BY-SA 4.0**. Le champ `license_spdx` de la fiche pointe la licence principale et les exceptions sont documentées ici.
- Opérateur Kubernetes de réplication PVC asynchrone (rsync/rclone, ainsi que sauvegarde Restic), pas un substitut universel à Velero ni une garantie de restauration de ressources et applications complètes. Certains modes nécessitent StorageClass, CSI snapshots ou clones ; protocole, secrets et RPO/RTO doivent être testés.
- Documentation : https://volsync.readthedocs.io/en/stable/ et https://volsync.readthedocs.io/en/stable/usage/

## 4. Journal OLD / NEW exact — 54 champs

Chaque champ `expected` correspond à l'ancienne valeur ou `null` si absent. `set` contient la nouvelle valeur complète. `preserved` recense les champs maintenus ; les références `legacy:` sont conservées à l'identique en tête de `sources`.

### `borgbackup` (CLEAR)

```json
{
  "id": "borgbackup",
  "expected": {
    "summary": "Deduplicating backup program (often used for cluster/VM backups).",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "You need efficient, deduplicated backups with encryption for filesystems or VM/node-level data."
    ],
    "avoid_when": [
      "You need Kubernetes-native backup of resources and PVs (use Velero/Kasten instead)."
    ],
    "deployment_models": [],
    "license_spdx": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:4_Kubernetes-Containers/README.md#L179",
      "legacy:devopstools_final.md#L683"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Deduplicating backup CLI with optional compression and authenticated encryption for filesystem data and off-site repositories.",
    "repository_archived": false,
    "documentation_url": "https://borgbackup.readthedocs.io/en/stable/",
    "use_when": [
      "You need efficient, encrypted, deduplicated filesystem backups to local or SSH-accessible repositories, with regular restore testing."
    ],
    "avoid_when": [
      "You need application-consistent backups for live databases or running VMs without coordinating quiescence or snapshots.",
      "You cannot protect and separately recover the repository key and passphrase, or have not tested restores.",
      "You require Kubernetes resource or PVC orchestration from the backup CLI alone."
    ],
    "deployment_models": [
      "local-cli"
    ],
    "license_spdx": "BSD-3-Clause",
    "status": "active",
    "verified_on": "2026-10-29",
    "sources": [
      "legacy:4_Kubernetes-Containers/README.md#L179",
      "legacy:devopstools_final.md#L683",
      "https://github.com/borgbackup/borg",
      "https://github.com/borgbackup/borg/blob/62051de6a0f90eab5f18a55871f9881542800e6c/LICENSE",
      "https://borgbackup.readthedocs.io/en/stable/",
      "https://github.com/borgbackup/borg/releases/tag/1.4.5",
      "https://borgbackup.readthedocs.io/en/stable/quickstart.html"
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

### `kube-dump` (RETAIN)

```json
{
  "id": "kube-dump",
  "expected": {
    "summary": "Backup tool for Kubernetes cluster resources.",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "You need a simple export of Kubernetes resource definitions for disaster recovery or auditing."
    ],
    "avoid_when": [
      "You also need persistent volume data backup (use Velero/Kasten)."
    ],
    "deployment_models": [],
    "license_spdx": null,
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:4_Kubernetes-Containers/README.md#L182",
      "legacy:devopstools_final.md#L686"
    ]
  },
  "set": {
    "summary": "CLI and container scripts exporting readable Kubernetes API resources as YAML manifests; not a persistent-volume data backup.",
    "repository_archived": false,
    "documentation_url": "https://github.com/WoozyMasta/kube-dump/blob/f1ae560a8b9da8dba1c28619f38089d40d0d2357/README.md",
    "use_when": [
      "You need an export of readable Kubernetes resource manifests for inspection or recovery planning, and can independently validate restored objects."
    ],
    "avoid_when": [
      "You need backup of PV contents, application-consistent database state or a complete cluster recovery procedure.",
      "You cannot protect exported Secrets, kubeconfigs or pushed Git repositories; README lists git-crypt protection as a future plan, not a guaranteed feature.",
      "You require confirmed recent upstream code maintenance or a tested compatibility claim for current Kubernetes versions."
    ],
    "deployment_models": [
      "local-cli",
      "container",
      "kubernetes"
    ],
    "license_spdx": "GPL-3.0-only",
    "verified_on": "2026-10-29",
    "sources": [
      "legacy:4_Kubernetes-Containers/README.md#L182",
      "legacy:devopstools_final.md#L686",
      "https://github.com/WoozyMasta/kube-dump",
      "https://github.com/WoozyMasta/kube-dump/blob/f1ae560a8b9da8dba1c28619f38089d40d0d2357/LICENSE",
      "https://github.com/WoozyMasta/kube-dump/blob/f1ae560a8b9da8dba1c28619f38089d40d0d2357/README.md",
      "https://github.com/WoozyMasta/kube-dump/releases/tag/1.1.2",
      "https://github.com/WoozyMasta/kube-dump/blob/f1ae560a8b9da8dba1c28619f38089d40d0d2357/docs/cronjob.md"
    ]
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
    "status",
    "alternatives",
    "tags",
    "needs_review"
  ]
}
```

### `stash` (CLEAR)

```json
{
  "id": "stash",
  "expected": {
    "summary": "Backup operator for Kubernetes.",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "You want a Kubernetes-native backup operator with support for databases, volumes, and scheduled backups."
    ],
    "avoid_when": [
      "Velero's ecosystem and community adoption better fits your support needs."
    ],
    "deployment_models": [],
    "license_model": "oss",
    "commercial_offering": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:4_Kubernetes-Containers/README.md#L183",
      "legacy:devopstools_final.md#L687"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Kubernetes backup and restore operator for workload volumes; database backup and some advanced capabilities depend on its licensed edition.",
    "repository_archived": false,
    "documentation_url": "https://stash.run/docs/v2025.10.17/welcome/",
    "use_when": [
      "You need Kubernetes-native, policy-driven volume backup and recovery, and can validate the current operator edition and license entitlements."
    ],
    "avoid_when": [
      "You require OSI-approved open-source redistribution and modification rights: current repository artifacts are under a restrictive AppsCode Community License.",
      "You expect database backup and enterprise features to be included in the free/community entitlement without checking the product edition.",
      "You cannot test restore consistency, protect storage credentials or apply least-privilege RBAC to backup controllers."
    ],
    "deployment_models": [
      "kubernetes-operator"
    ],
    "license_model": "source-available",
    "commercial_offering": true,
    "status": "active",
    "verified_on": "2026-10-29",
    "sources": [
      "legacy:4_Kubernetes-Containers/README.md#L183",
      "legacy:devopstools_final.md#L687",
      "https://github.com/stashed/stash",
      "https://github.com/stashed/stash/blob/1c655538dd4fa50ec1af1f322300758990940125/LICENSE.md",
      "https://stash.run/docs/v2025.10.17/welcome/",
      "https://github.com/appscode/licenses/blob/1.0.0/AppsCode-Community-1.0.0.md",
      "https://stash.run/docs/v2025.10.17/concepts/what-is-stash/overview/",
      "https://stash.run/"
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
    "maturity",
    "alternatives",
    "tags"
  ]
}
```

### `trilio` (CLEAR)

```json
{
  "id": "trilio",
  "expected": {
    "summary": "Kubernetes backup and recovery platform.",
    "documentation_url": null,
    "use_when": [
      "You need enterprise backup with application-consistent snapshots and multi-cloud recovery."
    ],
    "avoid_when": [
      "Velero or Kasten already covers your backup requirements."
    ],
    "deployment_models": [],
    "license_model": "unknown",
    "commercial_offering": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:4_Kubernetes-Containers/README.md#L184",
      "legacy:devopstools_final.md#L688"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Commercial subscription-licensed Kubernetes backup and disaster recovery platform for application resources, persistent volumes and KubeVirt workloads.",
    "documentation_url": "https://docs.trilio.io/kubernetes",
    "use_when": [
      "You need vendor-supported application-centric Kubernetes backup, recovery or cross-cluster migration with commercial licensing and verified CSI integration."
    ],
    "avoid_when": [
      "You need a fully open-source, license-free backup platform or cannot accept a subscription license.",
      "You assume a time-limited evaluation license provides perpetual production rights, or have not validated worker vCPU pricing and edition terms.",
      "You need tested application-consistent recovery but have not configured hooks, storage prerequisites and restore drills."
    ],
    "deployment_models": [
      "kubernetes-operator",
      "self-hosted"
    ],
    "license_model": "commercial",
    "commercial_offering": true,
    "status": "active",
    "verified_on": "2026-10-29",
    "sources": [
      "legacy:4_Kubernetes-Containers/README.md#L184",
      "legacy:devopstools_final.md#L688",
      "https://trilio.io/products/kubernetes-backup-and-recovery/",
      "https://trilio.io/resources/kubernetes-backup-frequently-asked-questions/",
      "https://trilio.io/kubernetes-backup-trial/",
      "https://docs.trilio.io/kubernetes"
    ],
    "needs_review": false
  },
  "preserved": [
    "name",
    "official_url",
    "categories",
    "subcategories",
    "roles",
    "lifecycle_stages",
    "maturity",
    "alternatives",
    "tags"
  ]
}
```

### `volsync` (CLEAR)

```json
{
  "id": "volsync",
  "expected": {
    "summary": "Kubernetes volume data replication.",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "You need asynchronous PV replication across clusters or storage backends for DR."
    ],
    "avoid_when": [
      "Your storage backend has native replication or you only need full-cluster backup (use Velero)."
    ],
    "deployment_models": [],
    "license_spdx": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:4_Kubernetes-Containers/README.md#L186",
      "legacy:devopstools_final.md#L690"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Kubernetes operator for asynchronous PVC replication using rsync or rclone, with Restic-based volume backup.",
    "repository_archived": false,
    "documentation_url": "https://volsync.readthedocs.io/en/stable/",
    "use_when": [
      "You need storage-independent asynchronous replication of Kubernetes PVC data across namespaces or clusters, or Restic-backed volume copies."
    ],
    "avoid_when": [
      "You expect automatic backup of every Kubernetes object, application-consistent databases or zero-RPO/zero-RTO failover without independent orchestration.",
      "Your CSI storage lacks the snapshot or clone capabilities required by the chosen copy method, or replicated data and keys are not protected.",
      "You cannot satisfy AGPL-3.0 obligations for the operator; API directory files additionally permit Apache-2.0 use."
    ],
    "deployment_models": [
      "kubernetes-operator"
    ],
    "license_spdx": "AGPL-3.0-only",
    "status": "active",
    "verified_on": "2026-10-29",
    "sources": [
      "legacy:4_Kubernetes-Containers/README.md#L186",
      "legacy:devopstools_final.md#L690",
      "https://github.com/backube/volsync",
      "https://github.com/backube/volsync/blob/7ba1990e0b2233a1bf6bb47466bee3ef1de1881f/LICENSE",
      "https://volsync.readthedocs.io/en/stable/",
      "https://github.com/backube/volsync/blob/7ba1990e0b2233a1bf6bb47466bee3ef1de1881f/README.md",
      "https://volsync.readthedocs.io/en/stable/usage/"
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


## 5. Conditions de validation et publication

1. Vérifier la branche et son SHA ; comparer les IDs et **8 fiches conservées byte-for-byte**, le blob baseline des liens inchangé et aucun changement de fichiers inattendu.
2. Sur le checkout Windows propre, exécuter `python -m scripts.generate_docs` puis `--check`, `validate_catalog`, `review_debt --format json`, Ruff check/format, `pip check`, `pytest` et `git diff --check`. Vérifier **1425 / 839 / 572 / 76**.
3. Contrôler et pousser **seulement** les pages déterministes générées, dans un deuxième commit séparé de la présente revue.
4. Créer une **Draft PR** limitée aux cinq fiches, à la présente note, et aux documents générés. Inspecter CI Quality, Plumber, Secret scan, CodeQL.
5. Exécuter un **Full link audit --strict --check-archived** sur **le HEAD final**. Gate : `blocking_new: 0` et `strict_result: PASS`, avec les historiques `blocking_known` conservés, sans éditer baseline/issue #2.
6. **Revue et fusion squash humaines seulement**, jamais automatique. Après fusion, vérification post-merge et synchronisation locale.

**Etat : EVIDENCE PATCH ON ISOLATED BRANCH — GENERATED DOCS, LOCAL VALIDATION AND PR PENDING.**
