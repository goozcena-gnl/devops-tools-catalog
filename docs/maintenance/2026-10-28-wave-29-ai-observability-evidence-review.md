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
