# Wave 30 — Git hooks et hygiène des commits — revue de preuves

**Revue : 2026-10-29 (Europe/Paris). Statut : changements canoniques sur branche isolée ; génération documentaire, tests et CI encore en attente.**

## Baseline et périmètre

- Repo : https://github.com/goozcena-gnl/devops-tools-catalog
- Base `main` : `7a109d36a468503193bd3c0f07a08964e0d6f371`. Aucune PR ouverte au lancement.
- Canonical YAML : `data/tools/software-supply-chain-security.yaml`, blob initial `d925ed801956fe6ea42360305dd2f2cbd45ec5b1`.
- Baseline liens : `config/link-audit-baseline.json`, blob `a834e2af711693def40078a55e31dfeb29bee2c7` — ne pas modifier.
- Cohorte : `husky`, `lefthook`, `pre-commit`, `simple-git-hooks`, précisément les 4 `needs-review` sur 19 fiches de la catégorie.
- **44 modifications de champs** proposées ; les **15 autres fiches sont préservées strictement**. Taxonomie, CI, schéma et URL historiques inchangés.
- Projection après validation : 1 425 records, 835 active (au lieu de 831), 576 needs-review (au lieu de 580), 77 modèles de licence inconnus inchangés.

## Sources primaires vérifiées

Dépôts non archivés, licences réellement lues, documentation officielle et releases consultées.

| ID | Source officielle | Licence | SHA amont immuable | Release GitHub observée |
|---|---|---|---|---|
| `husky` | [dépôt](https://github.com/typicode/husky) | [MIT](https://github.com/typicode/husky/blob/3f0023dc10d7003d70f2e31aa56300eab80e76d6/LICENSE) | `3f0023dc10d7003d70f2e31aa56300eab80e76d6` | `v9.1.7` |
| `lefthook` | [dépôt](https://github.com/evilmartians/lefthook) | [MIT](https://github.com/evilmartians/lefthook/blob/13d66a090ac6e73f3ff44652761facb02b00e91c/LICENSE) | `13d66a090ac6e73f3ff44652761facb02b00e91c` | `v2.2.2` |
| `pre-commit` | [dépôt](https://github.com/pre-commit/pre-commit) | [MIT](https://github.com/pre-commit/pre-commit/blob/8cb5845c835b1ff72240eb2484239411ec481d92/LICENSE) | `8cb5845c835b1ff72240eb2484239411ec481d92` | `v4.7.0` |
| `simple-git-hooks` | [dépôt](https://github.com/toplenboren/simple-git-hooks) | [MIT](https://github.com/toplenboren/simple-git-hooks/blob/39b29bb8797a29bd62985976975d0751878d36b4/LICENSE.txt) | `39b29bb8797a29bd62985976975d0751878d36b4` | `2.14.0` |

- Husky : https://typicode.github.io/husky/get-started.html et https://typicode.github.io/husky/how-to.html (hooks sous `.husky/`, `prepare`, `HUSKY=0`, problème PATH/GUI).
- Lefthook : https://lefthook.dev et https://lefthook.dev/configuration/parallel/ (binaire Go, orchestration optionnellement parallèle ; **séquentiel par défaut**).
- pre-commit : https://pre-commit.com/ (langages multiples, environnements gérés, `rev` à épingler, `pre-commit run --all-files`).
- simple-git-hooks : https://github.com/toplenboren/simple-git-hooks/blob/39b29bb8797a29bd62985976975d0751878d36b4/README.md (une commande par hook, installation manuelle ou via `prepare`, `postinstall` parfois bloqué) ; sa licence réelle se trouve dans `LICENSE.txt`.
- Git : https://git-scm.com/docs/githooks et https://git-scm.com/docs/gitfaq : **les hooks locaux sont contournables et ne remplacent pas les contrôles CI/serveur**.

## Décisions documentaires

| ID | Décision proposée | Licence | Réserve |
|---|---|---|---|
| `husky` | CLEAR | `oss` / MIT | Local, désactivable ; shell et environnement Node |
| `lefthook` | CLEAR | `oss` / MIT | Parallélisme facultatif, collisions possibles ; hook non bloquant côté serveur |
| `pre-commit` | CLEAR | `oss` / MIT | Scripts de dépôts tiers, installation des environnements, doublage CI |
| `simple-git-hooks` | CLEAR | `oss` / MIT | `postinstall` / `prepare`, limite d'une commande par hook et dépendance CI |

**Confiance :** forte pour l'identité, les licences et les fonctionnalités publiées ; aucune exécution runtime ni audit de sécurité technique effectués. Les quatre `maturity: unknown` restent en l'état plutôt que de déduire une maturité de releases ponctuelles.

## Manifeste exact OLD / NEW

`expected: null` signifie « champ absent », et non valeur YAML à écrire. `set` contient les nouvelles valeurs complètes ; `preserve` désigne les champs non touchés. Les références historiques sont conservées au début des nouvelles listes `sources`.

### `husky`

```json
{
  "id": "husky",
  "expected": {
    "summary": "Git hooks for Node.js projects (commonly paired with lint-staged).",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "In Node.js projects where pairing with lint-staged is the idiomatic approach."
    ],
    "avoid_when": [
      "In polyglot repos—pre-commit or Lefthook handle multiple languages better."
    ],
    "deployment_models": [],
    "license_spdx": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:7_Development-Collaboration/README.md#L66",
      "legacy:devopstools_final.md#L1104"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Node.js Git hooks manager that installs project-local scripts for pre-commit and other Git lifecycle events.",
    "repository_archived": false,
    "documentation_url": "https://typicode.github.io/husky/get-started.html",
    "use_when": [
      "You maintain a Node.js project and want versioned local Git hook scripts to run linting or tests before commits."
    ],
    "avoid_when": [
      "You require enforceable commit policy: local hooks can be bypassed with --no-verify or HUSKY=0; enforce critical checks in server-side CI.",
      "You cannot review installed shell commands or control package-manager prepare scripts during CI and production installation.",
      "Your team uses GUI Git clients or Node version managers without arranging a compatible shell PATH for hooks."
    ],
    "deployment_models": [
      "local-cli"
    ],
    "license_spdx": "MIT",
    "status": "active",
    "verified_on": "2026-10-29",
    "sources": [
      "legacy:7_Development-Collaboration/README.md#L66",
      "legacy:devopstools_final.md#L1104",
      "https://github.com/typicode/husky",
      "https://github.com/typicode/husky/blob/3f0023dc10d7003d70f2e31aa56300eab80e76d6/LICENSE",
      "https://typicode.github.io/husky/get-started.html",
      "https://typicode.github.io/husky/how-to.html",
      "https://git-scm.com/docs/gitfaq",
      "https://git-scm.com/docs/githooks"
    ],
    "needs_review": false
  },
  "preserve": [
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

### `lefthook`

```json
{
  "id": "lefthook",
  "expected": {
    "summary": "Fast Git hooks manager (parallel execution, cross-platform).",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "You need fast, parallel hook execution without a runtime dependency (single Go binary)."
    ],
    "avoid_when": [
      "Pre-commit's massive hook repository already covers your needs."
    ],
    "deployment_models": [],
    "license_spdx": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:7_Development-Collaboration/README.md#L65",
      "legacy:devopstools_final.md#L1103"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Cross-platform Go-based Git hooks manager with configurable file selection, commands and optional parallel execution.",
    "repository_archived": false,
    "documentation_url": "https://lefthook.dev",
    "use_when": [
      "You want declarative, cross-language Git hooks, file-aware execution or optional parallel commands with a standalone binary."
    ],
    "avoid_when": [
      "You need mandatory compliance checks: local hooks can be skipped, so duplicate release and security gates in CI.",
      "You run parallel hooks that write to the same files without coordination, or execute commands from untrusted repository configuration.",
      "You expect hook installation alone to verify the provenance or safety of third-party scripts and package-manager commands."
    ],
    "deployment_models": [
      "local-cli"
    ],
    "license_spdx": "MIT",
    "status": "active",
    "verified_on": "2026-10-29",
    "sources": [
      "legacy:7_Development-Collaboration/README.md#L65",
      "legacy:devopstools_final.md#L1103",
      "https://github.com/evilmartians/lefthook",
      "https://github.com/evilmartians/lefthook/blob/13d66a090ac6e73f3ff44652761facb02b00e91c/LICENSE",
      "https://lefthook.dev",
      "https://lefthook.dev/configuration/parallel/",
      "https://git-scm.com/docs/gitfaq",
      "https://git-scm.com/docs/githooks"
    ],
    "needs_review": false
  },
  "preserve": [
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

### `pre-commit`

```json
{
  "id": "pre-commit",
  "expected": {
    "summary": "Multi-language Git hook framework (config-driven, reproducible hooks across teams).",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "Your repo spans multiple languages and you want a single, declarative hook config."
    ],
    "avoid_when": [
      "You're in a pure Node.js project where Husky + lint-staged is simpler."
    ],
    "deployment_models": [],
    "license_spdx": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:7_Development-Collaboration/README.md#L64",
      "legacy:devopstools_final.md#L1102"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Multi-language Git hook framework using declarative configuration and managed hook environments for repeatable local or CI checks.",
    "repository_archived": false,
    "documentation_url": "https://pre-commit.com/",
    "use_when": [
      "You need cross-language linting, formatting or validation with pinned hook revisions and repeatable developer and CI execution."
    ],
    "avoid_when": [
      "You assume local hooks enforce server-side policy: users can bypass them; run pre-commit run --all-files in CI for required gates.",
      "You cannot review and pin remote hook repositories or allow first-run downloads and execution of third-party hook code.",
      "You require offline setup without a pre-populated cache, hook runtimes or approved dependencies."
    ],
    "deployment_models": [
      "local-cli",
      "ci"
    ],
    "license_spdx": "MIT",
    "status": "active",
    "verified_on": "2026-10-29",
    "sources": [
      "legacy:7_Development-Collaboration/README.md#L64",
      "legacy:devopstools_final.md#L1102",
      "https://github.com/pre-commit/pre-commit",
      "https://github.com/pre-commit/pre-commit/blob/8cb5845c835b1ff72240eb2484239411ec481d92/LICENSE",
      "https://pre-commit.com/",
      "https://git-scm.com/docs/gitfaq",
      "https://git-scm.com/docs/githooks"
    ],
    "needs_review": false
  },
  "preserve": [
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

### `simple-git-hooks`

```json
{
  "id": "simple-git-hooks",
  "expected": {
    "summary": "Lightweight Git hooks manager for Node.js.",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "You need a zero-dependency, minimal hooks setup for a small Node.js project."
    ],
    "avoid_when": [
      "You need parallel execution or per-file staged filtering."
    ],
    "deployment_models": [],
    "license_spdx": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:7_Development-Collaboration/README.md#L67",
      "legacy:devopstools_final.md#L1105"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Minimal Node.js Git hooks manager using package.json or local configuration, with one command per hook.",
    "repository_archived": false,
    "documentation_url": "https://github.com/toplenboren/simple-git-hooks/blob/39b29bb8797a29bd62985976975d0751878d36b4/README.md",
    "use_when": [
      "You need a lightweight, low-dependency hook setup for a small Node.js project and can manage explicit installation."
    ],
    "avoid_when": [
      "You need built-in parallel tasks, multiple independent commands per hook or native staged-file filtering; use a complementary tool or another manager.",
      "Your package manager blocks install scripts and you have not configured a supported prepare command or manual installation.",
      "You rely on local hooks as mandatory security controls, or cannot review postinstall and hook commands from dependencies."
    ],
    "deployment_models": [
      "local-cli"
    ],
    "license_spdx": "MIT",
    "status": "active",
    "verified_on": "2026-10-29",
    "sources": [
      "legacy:7_Development-Collaboration/README.md#L67",
      "legacy:devopstools_final.md#L1105",
      "https://github.com/toplenboren/simple-git-hooks",
      "https://github.com/toplenboren/simple-git-hooks/blob/39b29bb8797a29bd62985976975d0751878d36b4/LICENSE.txt",
      "https://github.com/toplenboren/simple-git-hooks/blob/39b29bb8797a29bd62985976975d0751878d36b4/README.md",
      "https://github.com/toplenboren/simple-git-hooks/blob/39b29bb8797a29bd62985976975d0751878d36b4/package.json",
      "https://git-scm.com/docs/gitfaq",
      "https://git-scm.com/docs/githooks"
    ],
    "needs_review": false
  },
  "preserve": [
    "name",
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


## Contrôles obligatoires avant publication finale

1. Récupérer le SHA exact de cette branche, contrôler le périmètre : 4 IDs modifiés, 15 autres fiches inchangées, pas de changement de baseline de liens, `main` intact.
2. Exécuter `python -m scripts.generate_docs` puis `python -m scripts.generate_docs --check` ; la documentation générée ne doit pas être éditée à la main.
3. Exécuter `python -m scripts.validate_catalog`, `python -m scripts.review_debt --format json`, Ruff lint/format, `pip check`, Pytest complet, `git diff --check`. Vérifier les statistiques projetées.
4. Committer/pousser uniquement les documents générés attendus, ouvrir une **Draft PR**, puis vérifier Quality, Plumber, Secret scan et CodeQL au HEAD final.
5. Lancer un **Full link audit strict** sur le HEAD final ; exiger `blocking_new: 0` et `strict_result: PASS`, sans modifier la baseline. Ne pas fermer l'issue historique #2.
6. **Fusion manuelle seulement**, après revue du diff et de la sécurité des hooks.

**État : CANONICAL EVIDENCE PATCH APPLIED ON A BRANCH; GENERATED DOCS AND CI NOT YET VALIDATED.**
