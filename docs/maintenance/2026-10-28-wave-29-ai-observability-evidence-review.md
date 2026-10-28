# Wave 29 — AI Observability & Evaluation: première passe de preuves

**Date de consultation : 2026-10-28 (Europe/Paris). Statut : documentaire, propositions uniquement.**

**Cohorte : 5 fiches existantes ; 0 CLEAR appliqué ; 0 fiche canonique modifiée.** Les verdicts ci-dessous sont des hypothèses pour une seconde passe indépendante, et non des certifications de sécurité ou des autorisations juridiques.

## 1. Baseline GitHub et périmètre

| Invariant | Valeur constatée |
|---|---|
| Dépôt | `goozcena-gnl/devops-tools-catalog` |
| `main` | `f8a4ba51f5c86a2385902082a3be6c7853115147` |
| Fiches canoniques | 1 425 |
| `active` | 826 |
| `needs-review` | 585 |
| Catégories | 30 |
| `license_model: unknown` | 77 |
| YAML cible | `data/tools/mlops-llmops-ai-infrastructure.yaml` |
| Blob Git YAML | `ceca52e94619af44df57aa0221129f56a51770f8` |
| Fiches YAML / en revue | 80 / 48 |
| Cohorte / fiches hors cohorte | 5 / 75 |
| PR ouvertes au démarrage | 0 |
| Issue historique #2 | ouverte |

L'ancienne déclaration `verified_on: '2026-08-03'` reste inchangée pour les cinq outils jusqu'à une application distincte approuvée. Les statistiques sont celles du `main` contrôlé ; elles ne préjugent pas des résultats d'une application future.

### Cohorte fermée

1. `arize-phoenix`
2. `evidently`
3. `langfuse`
4. `langsmith`
5. `promptfoo`

Ces cinq IDs existent dans la sous-catégorie `AI Observability & Evaluation`, chacun avec `status: needs-review` et `needs_review: true`. **Ne modifier aucun autre ID**, ni les 75 fiches voisines.

## 2. Méthode et limites

La première passe a lu les fiches de `main`, les dépôts officiels disponibles, les fichiers de licence et certains documents éditeurs. Les URL de dépôts ou documents accessibles au moment de la revue sont citées ci-dessous ; les commits de référence facilitent le gel des preuves. Les métadonnées d'un dépôt ne remplacent pas les clauses de sa licence. Une release de monorepo peut porter sur un sous-composant : ne pas l'assimiler automatiquement à une release du produit.

Aucun outil ni service n'a été installé, déployé, relié à un LLM ou soumis à des tests de transfert de données. Les conditions contractuelles LangSmith et les garanties de sécurité doivent être vérifiées dans les documents officiels actuels. Les conclusions **CLEAR** restent soumises à une seconde passe ; aucun seuil quantitatif de CLEAR n'est imposé.

## 3. Tableau de revue, propositions non appliquées

| ID | État de licence de la fiche | Première observation documentée | Proposition de seconde passe |
|---|---|---|---|
| `arize-phoenix` | `oss` | Le `LICENSE` du dépôt porte **Elastic License 2.0 (ELv2)**, avec restriction de service hébergé ; la documentation vendeur décrit un auto-hébergement autorisé, mais emploie aussi le terme « open-source ». | **RETAIN REVIEW provisoire** : examiner `source-available`, identifier le périmètre du produit, l'absence de service géré sous ELv2 et les sous-composants sous autres licences |
| `evidently` | `oss` | Dépôt `LICENSE` Apache-2.0 ; README distingue OSS auto-hébergé et Evidently Cloud avec fonctionnalités additionnelles. | **CLEAR conditionnel** après validation du champ `license_spdx: Apache-2.0`, du périmètre de licence et des données échangées avec Cloud |
| `langfuse` | `open-core` | `LICENSE` racine MIT hors répertoires Enterprise ; `ee/LICENSE` impose conditions distinctes, core MIT explicitement préservé. | **CLEAR conditionnel** en conservant `open-core`, sans attribuer MIT aux composants Enterprise, et après vérification de la portée actuelle des chemins de licence |
| `langsmith` | `open-core` | La fiche ne contient pas de `repository_url` et renvoie à une plateforme commerciale. L'existence d'intégrations / SDK open-source ne démontre pas que le service LangSmith lui-même est open-core. | **RETAIN REVIEW provisoire** : vérifier les contrats, l'offre cloud et self-hosted, puis décider `commercial` ou justification positive d'`open-core` |
| `promptfoo` | `oss` | Dépôt avec licence MIT ; documentation/README annoncent tests, évaluations et red teaming pilotables en CLI/CI. | **CLEAR conditionnel** après vérification des options réseau, de télémétrie, des fournisseurs LLM et du périmètre des offres commerciales |

Ces propositions ne sont **pas** un registre final d'anciennes/nouvelles valeurs YAML. En seconde passe, produire une table champ par champ avec la valeur actuelle, la valeur proposée, la preuve correspondante et la liste explicite des champs conservés, puis exiger une autorisation distincte pour appliquer les corrections.

## 4. Sources primaires et commits de référence

### Arize Phoenix
- Dépôt : https://github.com/Arize-ai/phoenix
- Commit de documentation consulté : `0370188bcff193bdab02ca5f4b1b4ca8fb087051`.
- Licence : https://github.com/Arize-ai/phoenix/blob/0370188bcff193bdab02ca5f4b1b4ca8fb087051/LICENSE
- Documentation de licence : https://github.com/Arize-ai/phoenix/blob/0370188bcff193bdab02ca5f4b1b4ca8fb087051/docs/phoenix/self-hosting/license.mdx
- Points à résoudre : ELv2 versus usage marketing « open source » ; service géré, licence de sous-packages, clés de fonctionnalités, sécurité et télémétrie.

### Evidently
- Dépôt : https://github.com/evidentlyai/evidently
- Commit consulté : `34771fe41c08ca074d96a52aaf4a45cd640cbaf5`.
- Licence Apache : https://github.com/evidentlyai/evidently/blob/34771fe41c08ca074d96a52aaf4a45cd640cbaf5/LICENSE
- README : https://github.com/evidentlyai/evidently/blob/34771fe41c08ca074d96a52aaf4a45cd640cbaf5/README.md
- Release observée : https://github.com/evidentlyai/evidently/releases/tag/v0.7.23
- Distinguer framework local / service cloud et gestion des datasets et traces.

### Langfuse
- Dépôt : https://github.com/langfuse/langfuse
- Commit consulté : `7adf573f8e19a56ada72fd8e816122174c3c88ac`.
- Licence racine : https://github.com/langfuse/langfuse/blob/7adf573f8e19a56ada72fd8e816122174c3c88ac/LICENSE
- Enterprise : https://github.com/langfuse/langfuse/blob/7adf573f8e19a56ada72fd8e816122174c3c88ac/ee/LICENSE
- README : https://github.com/langfuse/langfuse/blob/7adf573f8e19a56ada72fd8e816122174c3c88ac/README.md
- Revoir déploiement Kubernetes / Helm et configurations de stockage, authentification, accès et rétention des traces.

### LangSmith
- Page officielle actuellement déclarée : https://smith.langchain.com
- Documentation à examiner : https://docs.langchain.com/langsmith/home et https://docs.langchain.com/langsmith/self-hosted
- **Preuve complémentaire obligatoire** : conditions juridiques applicables au service et à l'offre auto-hébergée, URLs officielles actuelles (ne pas inventer de dépôt source du service). Examiner les SDK séparément, sans les assimiler au produit.

### Promptfoo
- Dépôt : https://github.com/promptfoo/promptfoo
- Commit consulté : `bfe97095b6d9eabd424021f004b13038068881d3`.
- Licence : https://github.com/promptfoo/promptfoo/blob/bfe97095b6d9eabd424021f004b13038068881d3/LICENSE
- README : https://github.com/promptfoo/promptfoo/blob/bfe97095b6d9eabd424021f004b13038068881d3/README.md
- Release observée : https://github.com/promptfoo/promptfoo/releases/tag/0.125.1
- Vérifier options CLI/CI, service associé, limites du red teaming et traitement des prompts et secrets.

## 5. Risques conditionnels et travaux de seconde passe

**P1 si déploiement en production :** traces contenant prompts, messages, données personnelles et secrets ; envoi d'évaluations ou de jeux de données à des fournisseurs LLM ; accès non autorisé aux interfaces d'observabilité ; mauvaise isolation multi-tenant ; politique de rétention ; privilèges sur les intégrations et les pipelines CI. Il s'agit de points de sécurité à examiner, **pas** de vulnérabilités démontrées.

**P2 :** licence ELv2 et restrictions de service hébergé ; délimitation MIT / Enterprise chez Langfuse ; classification de LangSmith, en particulier la séparation entre SDK open-source et service propriétaire ; segmentation OSS / Cloud d'Evidently et Promptfoo ; stabilité des versions et chemins de documentation.

La seconde passe devra vérifier pour chaque ID : identité canonique, propriétaire, repo/archive, licence exacte du produit vs sous-composants, disponibilité et modalités de self-hosting, prérequis opérationnels, compatibilité, collecte et export des traces, secrets, ressources consommées, lifecycle, maturity, URLs et normalisation des liens.

## 6. Invariants et état de publication

- **Aucune modification de `data/tools/mlops-llmops-ai-infrastructure.yaml`.**
- Aucun outil nouveau, aucun changement de taxonomie, de fiche, de statistiques ou de documentation générée.
- `config/link-audit-baseline.json` et l'issue historique #2 restent inchangés.
- Ne pas marquer `status: active`, `needs_review: false`, ni renseigner un `license_spdx` sans justification couvrant exactement le code considéré.
- Cette branche peut faire l'objet d'une **seconde passe documentaire** ; l'application canonique et la décision de fusion demandent une autorisation ultérieure.

**État de cette étape : FIRST-PASS DOCUMENTED — SECOND PASS REQUIRED.**

---

# Wave 29 — Revue indépendante, passe 2 (28 octobre 2026)

**État : SECOND PASS COMPLETED — FROZEN YAML PROPOSALS ONLY — NO CANONICAL APPLICATION.**

La section de première passe ci-dessus est conservée comme instantané historique ; ses 3 CLEAR / 2 RETAIN provisoires sont **supplantés** par les décisions de seconde passe détaillées ici, à la lumière de sources additionnelles. Le projet n'a pas été installé, aucun transfert réseau runtime n'a été observé et l'équipe n'a pas approuvé d'application. Un CLEAR n'est **pas** une certification de déploiement sûr ou une conclusion juridique générale.

## 7. Baseline et contre-vérification

- Baseline `main`: `f8a4ba51f5c86a2385902082a3be6c7853115147` ; branche Wave 29 avant cet ajout : `2e6553593fa55e8c797c1a84507ccfffa0a1dc99`.
- Blob du fichier YAML canonique lu sur la branche : `ceca52e94619af44df57aa0221129f56a51770f8` ; 80 fiches, dont 48 avec `needs_review: true`, exactement 5 IDs sélectionnés, tous encore `status: needs-review`.
- Fichier cible : `data/tools/mlops-llmops-ai-infrastructure.yaml`. Les 75 fiches non sélectionnées ne sont pas concernées et le blob YAML doit rester inchangé pendant cette passe.
- Schéma contrôlé à `schema/tool.schema.json` (blob `df28c5c26dd967a911c36073902e82173762e261`) : les valeurs `oss`, `source-available`, `open-core` et `commercial` sont autorisées ; `license_spdx` est une chaîne optionnelle. L'identifiant `Elastic-2.0` figure dans le registre SPDX, sans être OSI-approved.
- Aucune PR ni modification de `main` prévue durant cette passe.

## 8. Matrice de décision finale proposée (0 appliqué)

| ID | Décision passe 1 | Seconde passe | Licence du périmètre pertinent | Réserve clé |
|---|---|---|---|---|
| `arize-phoenix` | RETAIN | **CLEAR** | `source-available` / `Elastic-2.0` | ELv2 interdit certaines offres de service managé et n'est pas OSI-approved ; authentication off par défaut selon la documentation |
| `evidently` | CLEAR conditionnel | **CLEAR** | `oss` / `Apache-2.0` | Bibliothèque Apache distincte des conditions Cloud |
| `langfuse` | CLEAR conditionnel | **CLEAR** | `open-core`, cœur MIT, Enterprise séparé | Aucun SPDX global proposé à cause des répertoires Enterprise ; télémétrie Enterprise non désactivable sous termes standard |
| `langsmith` | RETAIN | **CLEAR** | `commercial`, aucun SPDX produit | LangSmith Platform sous conditions contractuelles, auto-hébergement Enterprise avec clé |
| `promptfoo` | CLEAR conditionnel | **CLEAR** | `oss` / `MIT` pour le CLI | Génération et notation hébergées selon la configuration, parfois par défaut ; contrôles de réseau et sharing nécessaires |

**Bilan de décisions proposées : 5 CLEAR / 0 RETAIN ; APPLIED: 0.** La requalification de Phoenix et LangSmith est une clarification de licence, pas un jugement de qualité ou de sécurité. Les cinq fiches peuvent être proposées comme actives à condition de **reproduire intégralement les avertissements de `avoid_when`**.

## 9. Sources primaires additionnelles et arbitrages

- **phoenix**: [P1] https://github.com/Arize-ai/phoenix/blob/0370188bcff193bdab02ca5f4b1b4ca8fb087051/LICENSE; [P2] https://github.com/Arize-ai/phoenix/blob/0370188bcff193bdab02ca5f4b1b4ca8fb087051/docs/phoenix/self-hosting/license.mdx; [P3] https://github.com/Arize-ai/phoenix/blob/0370188bcff193bdab02ca5f4b1b4ca8fb087051/README.md; [P4] https://arize.com/docs/phoenix/self-hosting/features/authentication; [P5] https://arize.com/docs/phoenix/self-hosting; [P6] https://spdx.org/licenses/Elastic-2.0.html
- **evidently**: [E1] https://github.com/evidentlyai/evidently/blob/34771fe41c08ca074d96a52aaf4a45cd640cbaf5/LICENSE; [E2] https://github.com/evidentlyai/evidently/blob/34771fe41c08ca074d96a52aaf4a45cd640cbaf5/README.md; [E3] https://docs.evidentlyai.com/introduction
- **langfuse**: [L1] https://github.com/langfuse/langfuse/blob/7adf573f8e19a56ada72fd8e816122174c3c88ac/LICENSE; [L2] https://github.com/langfuse/langfuse/blob/7adf573f8e19a56ada72fd8e816122174c3c88ac/ee/LICENSE; [L3] https://langfuse.com/self-hosting; [L4] https://langfuse.com/self-hosting/security/telemetry; [L5] https://langfuse.com/self-hosting/license-key
- **langsmith**: [L1] https://www.langchain.com/terms-of-service; [L2] https://www.langchain.com/pricing; [L3] https://docs.langchain.com/langsmith/observability; [L4] https://support.langchain.com/articles/7011309930-how-do-i-obtain-a-self-hosted-langsmith-license-key
- **promptfoo**: [P1] https://github.com/promptfoo/promptfoo/blob/bfe97095b6d9eabd424021f004b13038068881d3/LICENSE; [P2] https://github.com/promptfoo/promptfoo/blob/bfe97095b6d9eabd424021f004b13038068881d3/README.md; [P3] https://www.promptfoo.dev/docs/red-team/troubleshooting/data-handling/; [P4] https://www.promptfoo.dev/docs/usage/sharing/; [P5] https://www.promptfoo.dev/docs/configuration/telemetry/; [P6] https://www.promptfoo.dev/docs/red-team/quickstart/

**Points discriminants** : (a) Phoenix, texte ELv2 et restriction explicite de managed service ; auto-hébergement permis mais licence non approuvée par l'OSI ; (b) Phoenix auth désactivée initialement, `PHOENIX_ENABLE_AUTH` documenté ; (c) Langfuse root MIT exclut les chemins Enterprise, et la télémétrie Enterprise self-hosted a une obligation différente d'OSS ; (d) LangSmith Terms of Service mis à jour le 2 juin 2026 définit Cloud, Hybrid et Self-Hosted sous licence à durée limitée et clé d'autorisation ; (e) Promptfoo documente que sans clé/provider adapté, certaines générations et notations red-team empruntent `api.promptfoo.app`, avec des plugins exclusivement distants, et que les données des evals peuvent être partagées.

**Confiance :** élevée pour les licences textuelles et leurs conditions documentées ; moyenne pour les conséquences opérationnelles qui dépendent de chaque configuration, du plan et de la version. Pas de validation runtime ni de benchmark.

## 10. Gel OLD/NEW des champs de la cohorte — manifeste destiné à une application future

Les cartes ci-dessous couvrent **59 modifications de champs proposées**. Le manifeste traite explicitement les champs ajoutés (`expected: null`) comme absents dans l'état initial. Les valeurs d'`sources` concatènent les références historiques aux preuves primaires ; aucun lien historique n'est supprimé. Les champs `maturity: unknown`, `categories`, `subcategories`, `roles`, `lifecycle_stages`, `alternatives`, `tags` et les autres éléments de `preserve` restent intacts.

### `arize-phoenix` — CLEAR proposed, not applied

**Evidence decision:** ELv2 explicit (not OSI-approved) and supported self-hosting; UI/OTLP security and default disabled authentication are documented. Distinguish app server from SDK licences and Arize AX. Source refs: [P1-P6] below.

**Exact YAML field patch manifest:** `expected` contains the original value or `null` for an absent field. `set` supplies the complete replacement value; arrays replace the entire original array. `preserve` lists fields that must remain exactly as they are. JSON below is valid YAML 1.2 and uses JSON quoting to remove scalar ambiguity.

```yaml
{
  "id": "arize-phoenix",
  "expected": {
    "summary": "LLM observability and evaluation platform.",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "You need tracing, evaluation, and debugging for LLM applications with a self-hosted option."
    ],
    "avoid_when": [
      "You're not running LLM workloads or already have sufficient observability through your existing stack."
    ],
    "deployment_models": [],
    "license_model": "oss",
    "license_spdx": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:9_AI-MLOps/README.md#L64",
      "legacy:devopstools_final.md#L1251"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Self-hostable AI and LLM observability platform for OpenTelemetry/OpenInference tracing, evaluations and experiments; Phoenix server is ELv2 licensed.",
    "repository_archived": false,
    "documentation_url": "https://arize.com/docs/phoenix/self-hosting",
    "use_when": [
      "You need to self-host LLM traces, evaluations or experiments and accept the Elastic License 2.0 restrictions."
    ],
    "avoid_when": [
      "You need an OSI-approved open-source licence or intend to offer Phoenix functionality to third parties as a managed service; ELv2 restricts that use.",
      "You cannot protect trace payloads and Phoenix UI/OTLP endpoints; self-hosted Phoenix documentation says authentication is disabled by default, so enable authentication and restrict network access.",
      "You require assurances that traced prompts, responses or integrations never reach an external model or service without verifying exporters, evaluations and telemetry."
    ],
    "deployment_models": [
      "self-hosted",
      "container"
    ],
    "license_model": "source-available",
    "license_spdx": "Elastic-2.0",
    "status": "active",
    "verified_on": "2026-10-28",
    "sources": [
      "legacy:9_AI-MLOps/README.md#L64",
      "legacy:devopstools_final.md#L1251",
      "https://github.com/Arize-ai/phoenix/blob/0370188bcff193bdab02ca5f4b1b4ca8fb087051/LICENSE",
      "https://github.com/Arize-ai/phoenix/blob/0370188bcff193bdab02ca5f4b1b4ca8fb087051/docs/phoenix/self-hosting/license.mdx",
      "https://github.com/Arize-ai/phoenix/blob/0370188bcff193bdab02ca5f4b1b4ca8fb087051/README.md",
      "https://arize.com/docs/phoenix/self-hosting/features/authentication",
      "https://arize.com/docs/phoenix/self-hosting",
      "https://spdx.org/licenses/Elastic-2.0.html"
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
    "maturity",
    "alternatives",
    "tags"
  ]
}
```

### `evidently` — CLEAR proposed, not applied

**Evidence decision:** GitHub LICENSE Apache-2.0; official docs confirm Python library and self-hosted framework with distinct commercial Cloud. Source refs [E1-E3].

**Exact YAML field patch manifest:** `expected` contains the original value or `null` for an absent field. `set` supplies the complete replacement value; arrays replace the entire original array. `preserve` lists fields that must remain exactly as they are. JSON below is valid YAML 1.2 and uses JSON quoting to remove scalar ambiguity.

```yaml
{
  "id": "evidently",
  "expected": {
    "summary": "Open-source evaluation and monitoring framework for ML and AI systems.",
    "official_url": null,
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [],
    "avoid_when": [],
    "deployment_models": [],
    "license_spdx": null,
    "commercial_offering": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:devopstools_final.md#L1252"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Apache-2.0 Python framework for data quality, drift monitoring and ML/LLM evaluations; separate Evidently Cloud offers managed capabilities.",
    "official_url": "https://www.evidentlyai.com/",
    "repository_archived": false,
    "documentation_url": "https://docs.evidentlyai.com/introduction",
    "use_when": [
      "You need reproducible data-quality, ML-drift or LLM evaluation checks in Python, locally or within a self-hosted workflow."
    ],
    "avoid_when": [
      "You assume Evidently Cloud features, hosted collaboration, alerting or enterprise services are part of the Apache-2.0 Python-library licence.",
      "Your datasets or evaluation results are sensitive and you have not reviewed deployment boundaries, storage, hosted endpoints and LLM judge providers."
    ],
    "deployment_models": [
      "software-library",
      "self-hosted",
      "hosted-saas"
    ],
    "license_spdx": "Apache-2.0",
    "commercial_offering": true,
    "status": "active",
    "verified_on": "2026-10-28",
    "sources": [
      "legacy:devopstools_final.md#L1252",
      "https://github.com/evidentlyai/evidently/blob/34771fe41c08ca074d96a52aaf4a45cd640cbaf5/LICENSE",
      "https://github.com/evidentlyai/evidently/blob/34771fe41c08ca074d96a52aaf4a45cd640cbaf5/README.md",
      "https://docs.evidentlyai.com/introduction"
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

### `langfuse` — CLEAR proposed, not applied

**Evidence decision:** Root LICENSE scopes MIT outside Enterprise directories, ee/LICENSE separately applies, and self-hosting/telemetry documentation defines enterprise limits. Source refs [L1-L5].

**Exact YAML field patch manifest:** `expected` contains the original value or `null` for an absent field. `set` supplies the complete replacement value; arrays replace the entire original array. `preserve` lists fields that must remain exactly as they are. JSON below is valid YAML 1.2 and uses JSON quoting to remove scalar ambiguity.

```yaml
{
  "id": "langfuse",
  "expected": {
    "summary": "LLM observability and analytics; OSS self-hosted core with commercial cloud offering.",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "You want detailed LLM trace analytics with the option to self-host or use managed cloud."
    ],
    "avoid_when": [
      "You have minimal LLM usage and don't need per-request cost/latency tracking."
    ],
    "deployment_models": [],
    "commercial_offering": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:9_AI-MLOps/README.md#L66",
      "legacy:devopstools_final.md#L1253"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Open-core LLM tracing and evaluation platform with a self-hostable MIT core, separately licensed Enterprise modules and managed Cloud offering.",
    "repository_archived": false,
    "documentation_url": "https://langfuse.com/self-hosting",
    "use_when": [
      "You want self-hosted or managed LLM traces, evaluations, prompt management and operational analytics with explicit hosting and licence boundaries."
    ],
    "avoid_when": [
      "You require all Langfuse features or all repository files to be MIT-licensed; Enterprise directories and paid features have separate terms.",
      "Your deployment cannot protect prompts, traces, ClickHouse/Postgres data and access tokens, or you need retention and security features without checking plan-specific restrictions.",
      "You require zero telemetry: OSS can disable application telemetry with TELEMETRY_ENABLED=false; Enterprise self-hosted telemetry used for licence compliance cannot be disabled under standard terms."
    ],
    "deployment_models": [
      "self-hosted",
      "container",
      "hosted-saas"
    ],
    "commercial_offering": true,
    "status": "active",
    "verified_on": "2026-10-28",
    "sources": [
      "legacy:9_AI-MLOps/README.md#L66",
      "legacy:devopstools_final.md#L1253",
      "https://github.com/langfuse/langfuse/blob/7adf573f8e19a56ada72fd8e816122174c3c88ac/LICENSE",
      "https://github.com/langfuse/langfuse/blob/7adf573f8e19a56ada72fd8e816122174c3c88ac/ee/LICENSE",
      "https://langfuse.com/self-hosting",
      "https://langfuse.com/self-hosting/security/telemetry",
      "https://langfuse.com/self-hosting/license-key"
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

### `langsmith` — CLEAR proposed, not applied

**Evidence decision:** LangChain terms explicitly license LangSmith Platform (Cloud, Hybrid, Self-Hosted) contractually; Enterprise licence key required for self-hosting. No source repository for whole platform inferred from open SDKs. Source refs [S1-S4].

**Exact YAML field patch manifest:** `expected` contains the original value or `null` for an absent field. `set` supplies the complete replacement value; arrays replace the entire original array. `preserve` lists fields that must remain exactly as they are. JSON below is valid YAML 1.2 and uses JSON quoting to remove scalar ambiguity.

```yaml
{
  "id": "langsmith",
  "expected": {
    "summary": "LLM application development platform with observability, testing, and evaluation (LangChain-affiliated).",
    "documentation_url": null,
    "use_when": [
      "You're already using LangChain and want tightly integrated tracing, testing, and prompt management."
    ],
    "avoid_when": [
      "You don't use LangChain—vendor lock-in to the LangChain ecosystem may not be worth it."
    ],
    "deployment_models": [],
    "license_model": "open-core",
    "commercial_offering": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:9_AI-MLOps/README.md#L68",
      "legacy:devopstools_final.md#L1254"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "Commercial LangSmith platform for LLM and agent observability, evaluations and debugging, with Cloud, Hybrid and Enterprise-licensed self-hosted deployment options.",
    "documentation_url": "https://docs.langchain.com/langsmith/observability",
    "use_when": [
      "You need managed or contractually licensed tracing and evaluations for agents across LLM frameworks, and can meet LangSmith billing, access and data-governance requirements."
    ],
    "avoid_when": [
      "You require a redistributable open-source platform; LangSmith is commercially licensed even though LangChain SDKs and integrations may be open-source.",
      "You want self-hosted LangSmith without an Enterprise agreement and authorised licence key, or cannot approve trace storage, data residency or contractual restrictions."
    ],
    "deployment_models": [
      "hosted-saas",
      "hybrid",
      "enterprise-self-hosted"
    ],
    "license_model": "commercial",
    "commercial_offering": true,
    "status": "active",
    "verified_on": "2026-10-28",
    "sources": [
      "legacy:9_AI-MLOps/README.md#L68",
      "legacy:devopstools_final.md#L1254",
      "https://www.langchain.com/terms-of-service",
      "https://www.langchain.com/pricing",
      "https://docs.langchain.com/langsmith/observability",
      "https://support.langchain.com/articles/7011309930-how-do-i-obtain-a-self-hosted-langsmith-license-key"
    ],
    "needs_review": false
  },
  "preserve": [
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

### `promptfoo` — CLEAR proposed, not applied

**Evidence decision:** MIT LICENSE; official data-handling docs detail provider-configured target evaluation, hosted red-team generation and grading defaults when credentials absent, remote-only plugins, sharing and telemetry. Source refs [F1-F6].

**Exact YAML field patch manifest:** `expected` contains the original value or `null` for an absent field. `set` supplies the complete replacement value; arrays replace the entire original array. `preserve` lists fields that must remain exactly as they are. JSON below is valid YAML 1.2 and uses JSON quoting to remove scalar ambiguity.

```yaml
{
  "id": "promptfoo",
  "expected": {
    "summary": "Test and evaluate LLM prompts.",
    "repository_archived": null,
    "documentation_url": null,
    "use_when": [
      "You want CI-friendly, automated prompt regression testing and red-teaming."
    ],
    "avoid_when": [
      "You're still in early prototyping and prompt stability isn't yet a concern."
    ],
    "deployment_models": [],
    "license_spdx": null,
    "commercial_offering": null,
    "status": "needs-review",
    "verified_on": "2026-08-03",
    "sources": [
      "legacy:9_AI-MLOps/README.md#L70",
      "legacy:devopstools_final.md#L1255"
    ],
    "needs_review": true
  },
  "set": {
    "summary": "MIT-licensed CLI for LLM regression evaluation and red-team testing in CI; generation, grading, sharing and telemetry may use external services.",
    "repository_archived": false,
    "documentation_url": "https://www.promptfoo.dev/docs/red-team/quickstart/",
    "use_when": [
      "You need reproducible local or CI-based LLM prompt evaluations or authorised red-team tests with configured attack and grading providers."
    ],
    "avoid_when": [
      "You cannot permit sensitive application context, prompts or target responses to leave your environment: without suitable local credentials or providers, some red-team generation and grading uses Promptfoo-hosted inference.",
      "You treat PROMPTFOO_DISABLE_REMOTE_GENERATION as a complete network isolation control; remote-only plugins, explicitly configured providers, telemetry, sharing and Cloud features require separate checks.",
      "You share evaluations, target setup forms or provider configuration containing secrets without reviewing hosted upload destinations and telemetry settings."
    ],
    "deployment_models": [
      "local-cli",
      "on-premises",
      "hosted-saas"
    ],
    "license_spdx": "MIT",
    "commercial_offering": true,
    "status": "active",
    "verified_on": "2026-10-28",
    "sources": [
      "legacy:9_AI-MLOps/README.md#L70",
      "legacy:devopstools_final.md#L1255",
      "https://github.com/promptfoo/promptfoo/blob/bfe97095b6d9eabd424021f004b13038068881d3/LICENSE",
      "https://github.com/promptfoo/promptfoo/blob/bfe97095b6d9eabd424021f004b13038068881d3/README.md",
      "https://www.promptfoo.dev/docs/red-team/troubleshooting/data-handling/",
      "https://www.promptfoo.dev/docs/usage/sharing/",
      "https://www.promptfoo.dev/docs/configuration/telemetry/",
      "https://www.promptfoo.dev/docs/red-team/quickstart/"
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


## 11. Impact prévisionnel et barrières avant toute application

| Mesure | Main actuel | Si **5 CLEAR** sont appliqués après autorisation |
|---|---:|---:|
| Catalogue total | 1 425 | 1 425 |
| Active | 826 | 831 |
| Needs-review | 585 | 580 |
| Needs-review dans le YAML cible | 48 | 43 |
| `license_model: unknown` | 77 | 77 |
| OSS | 932 | 931 |
| Source-available | 29 | 30 |
| Open-core | 113 | 112 |
| Commercial | 163 | 164 |

**P1 conditionnels (adoption, non incidents démontrés)** : (1) protection UI/auth Phoenix et ingestions OTLP ; (2) contenus de traces/prompts et RBAC/rétention ; (3) exfiltration possible de contenus red-team dans des appels explicitement hébergés/configurés ; (4) politiques d'accès et de résidence des données. **P2** : restrictions ELv2, produits commerciaux et EE, télémétrie de licence obligatoire Langfuse EE, incompatibilités éventuelles de fonctionnalités ou déploiement.

Pour l'application future, imposer :

1. Re-vérifier le SHA `main`, les blobs du YAML et de la baseline des liens, l'absence de modifications locales imprévues, et le statut des cinq fiches ; arrêter au moindre écart.
2. Appliquer **uniquement** les clés `set` sur les cinq IDs si chaque clé `expected` correspond exactement ; ne pas réécrire les 75 fiches voisines et les champs `preserve` ; vérifier le schéma complet et l'unicité des URLs normalisées.
3. Régénérer uniquement les sorties déterministes, exécuter `python -m scripts.review_debt --format json`, `python -m scripts.generate_docs --check`, `python -m scripts.validate_catalog`, Ruff, Pytest, `git diff --check` et les contrôles de périmètre SHA.
4. Publier les modifications canoniques dans **une étape explicitement autorisée distincte** ; préparer une Draft PR et exiger le succès de la CI et de l'audit strict des liens au HEAD final avant fusion humaine.
5. Ne pas modifier l'issue historique #2, les exceptions du link audit, `main`, les workflows ou le schéma pendant cette seconde passe.

**Livrable : READY FOR CONTROLLED CANONICAL APPLICATION, NON APPLIQUÉ.**
