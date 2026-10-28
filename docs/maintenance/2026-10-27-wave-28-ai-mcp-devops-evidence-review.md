# Wave 28 — AI, MCP & DevOps : première passe de preuves

**Date de consultation : 2026-10-27, Europe/Paris. État : documentaire uniquement.**
**Propositions : 6 CLEAR / 4 RETAIN REVIEW. Application : 0 fiche modifiée, 0 validation de fiche appliquée.**

Ce document prépare une seconde passe contrôlée. CLEAR signifie que les preuves documentaires suffisent pour proposer une correction ciblée des métadonnées dans le périmètre décrit. Il ne certifie ni la sécurité d'un déploiement, ni l'absence de vulnérabilités, ni les droits sur tous les composants, modèles, services ou extensions. Les décisions sont proposées individuellement, sans quota. Les dix fiches gardent réellement `status: needs-review` et `needs_review: true`.

## 1. Baseline vérifiée avant écriture

Le checkout initial était propre, sur `main`. Les valeurs suivantes ont été lues avant création de la branche locale et du présent document.

| Invariant | Attendu | Observé |
|---|---|---|
| Branche initiale | `main` | `main` |
| HEAD et ref locale main | `2cda6adb8c75d33dece85c4ec04e1b424bf5a38e` | identiques |
| main distant, via API GitHub | même SHA | identique lors de la consultation |
| Fiches canoniques | 1 425 | 1 425 |
| Statut active | 816 | 816 |
| Statut needs-review | 595 | 595 |
| Fiches requérant une revue, calcul review_debt | 595 | 595 |
| Catégories de taxonomie | 30 | 30 |
| `license_model: unknown` | 77 | 77 |
| Fichier cible | `data/tools/mlops-llmops-ai-infrastructure.yaml` | même fichier |
| Blob Git du fichier cible | `67b741277e52e51abb1f4e72c6b846b2edcdeb95` | identique |
| Fiches du fichier / requérant une revue | 80 / 58 | 80 / 58 |
| Blob baseline des liens | conservé | `a834e2af711693def40078a55e31dfeb29bee2c7` |

Les autres statuts observés sont 10 archived, 2 historical et 2 deprecated. Le compteur `unknown_license` mesure le **modèle de licence du logiciel**, pas les licences inconnues de poids de modèles IA. La date de référence de `review_debt` est le maximum des dates `verified_on`, ici 2026-10-26 ; elle n'est pas la date de consultation réseau.

Branche de travail créée : `maintenance/wave-28-ai-mcp-devops-evidence-review`, depuis le SHA ci-dessus. Aucun commit, push, PR, issue, merge ou release. La ref locale `main` reste inchangée.

**Règle d'arrêt :** à la seconde passe, comparer à nouveau SHA, blob, compteurs et propreté du checkout. Tout écart impose de documenter l'écart et d'arrêter l'application jusqu'à réconciliation. La correspondance actuelle ne vaut pas autorisation d'application ultérieure.

### Cohorte fermée, dans l'ordre de la mission

1. `azure-mcp-server`
2. `kubernetes-mcp-server`
3. `terraform-mcp-server`
4. `github-mcp-server`
5. `grafana-mcp`
6. `docker-mcp-gateway`
7. `k8sgpt`
8. `litellm`
9. `ollama`
10. `open-webui`

Ces dix IDs existent chacun une fois. Aucun nouvel ID. Les 70 autres fiches du fichier cible et les autres fichiers canoniques sont hors du lot et restent inchangés.

## 2. Méthode, provenance et limites de reproductibilité

Lectures effectuées : YAML, schéma et taxonomie locaux ; métadonnées des dépôts par le connecteur GitHub ; API Releases et résolution des tags en commits ; fichiers de licence et documentation aux commits indiqués ; documentation officielle des éditeurs. Les badges et extraits de moteurs de recherche ne servent pas de preuve de licence. Aucun outil de la cohorte n'a été installé, démarré ou connecté à un cluster, abonnement Azure, workspace Terraform, compte GitHub, Grafana ou fournisseur LLM.

Les URLs `blob/<SHA>/...` fixent les **textes lus**. Un tag seul peut être déplacé : la résolution ci-dessous prime pour reproduire cette passe. Les métadonnées `archived`, les releases et les pages de documentation hébergées sont des observations datées, susceptibles d'évoluer. Aucun inventaire complet de dépendances binaires/SBOM, scan de sécurité ou test d'intégration n'est revendiqué.

| ID | Dépôt officiel actuel / éditeur observé | Release observée, date UTC | Commit des textes lus |
|---|---|---|---|
| azure-mcp-server | Microsoft, `microsoft/mcp`, sous-répertoire Azure.Mcp.Server | [Azure.Mcp.Server-3.0.0](https://github.com/microsoft/mcp/releases/tag/Azure.Mcp.Server-3.0.0), 2026-10-12 | `61715e6a9054d7922809b01e08a2efa85e032a6d` |
| kubernetes-mcp-server | projet `containers/kubernetes-mcp-server` ; ne pas confondre avec un serveur homonyme | [v0.0.69](https://github.com/containers/kubernetes-mcp-server/releases/tag/v0.0.69), 2026-10-23 | `bcadfee0e724836da2657ba609ff25c27ab35f58` |
| terraform-mcp-server | HashiCorp / IBM, `hashicorp/terraform-mcp-server` | [v1.4.1](https://github.com/hashicorp/terraform-mcp-server/releases/tag/v1.4.1), 2026-10-23 | `3781509a674482ca7e2821fab8159a25e3b29bdf` |
| github-mcp-server | GitHub, `github/github-mcp-server` | [v2.0.3](https://github.com/github/github-mcp-server/releases/tag/v2.0.3), 2026-10-21 | `b98d115bbb080e9555466a96656ec4df605aea21` |
| grafana-mcp | Grafana, `grafana/mcp-grafana` | [v2.1.1](https://github.com/grafana/mcp-grafana/releases/tag/v2.1.1), 2026-10-20 | `244d1adde04194ecad15125cb17159a1db50626b` |
| docker-mcp-gateway | Docker, `docker/mcp-gateway` | [v0.44.3](https://github.com/docker/mcp-gateway/releases/tag/v0.44.3), 2026-10-26, **prerelease** | `7e0f34277c91855ad861eeff536b4fdc77420593` |
| k8sgpt | K8sGPT Authors, `k8sgpt-ai/k8sgpt` | [v0.4.41](https://github.com/k8sgpt-ai/k8sgpt/releases/tag/v0.4.41), 2026-10-21 | `3644ecfd4f932be3901838b35e250a95f7732114` |
| litellm | BerriAI ; licence Enterprise nomme Berrie AI Inc. | [v1.106.4](https://github.com/BerriAI/litellm/releases/tag/v1.106.4), 2026-10-25 | `ea7ca16dbc3904d9e59a9505f379a2ca3091821f` |
| ollama | Ollama, `ollama/ollama` | [v0.40.11](https://github.com/ollama/ollama/releases/tag/v0.40.11), 2026-10-24 | `675150d6ad2747df1e218ef59de9194bc4a7e538` |
| open-webui | Open WebUI Inc., créé par Timothy Jaeryang Baek | [v0.12.4](https://github.com/open-webui/open-webui/releases/tag/v0.12.4), 2026-10-25 | `33c1978d5bad52a31df75ea55143025dfad18d16` |

Les huit releases hors Azure/Docker ont été recoupées avec l'endpoint `releases/latest` : `prerelease=false`. Pour Azure, le monorepo publie plusieurs produits : filtrer **Azure.Mcp.Server** et exclure les suffixes alpha/beta/rc. L'endpoint latest du monorepo désigne un Template alpha et ne prouve pas la dernière stable Azure. La stable Azure observée est 3.0.0 ; 4.0.0-beta.3 est une beta même si son drapeau API prerelease vaut false. Pour Docker, les 74 releases retournées sur une page de 100 sont toutes marquées prerelease ; aucune release stable n'a été établie. L'absence de stable n'est pas une preuve d'abandon.

**Archivage :** le connecteur a retourné `archived=false` pour chacun des dix dépôts actuels, dont [microsoft/mcp](https://api.github.com/repos/microsoft/mcp). Il a retourné `archived=true` pour [Azure/azure-mcp](https://api.github.com/repos/Azure/azure-mcp). Reproduire avec `GET /repos/{owner}/{repo}` pour les noms du tableau ; ne pas déduire l'archivage d'un lien qui fonctionne ou redirige.

## 3. Décisions provisoires

| ID | Proposition | Preuve décisive / réserve significative |
|---|---|---|
| azure-mcp-server | **CLEAR** | Migration explicitement annoncée ; serveur Microsoft MIT ; stable propre au sous-produit établie. Corriger la classification documentation. |
| kubernetes-mcp-server | **CLEAR** | Identité containers, Apache-2.0, opérations et configuration TOML documentées ; avertissement RBAC et mutations nécessaire. |
| terraform-mcp-server | **CLEAR** | Serveur HashiCorp MPL-2.0, distinct du moteur Terraform ; surface Registry et HCP/TFE, filtrage et gates lus dans le code. |
| github-mcp-server | **CLEAR** | Serveur officiel MIT, release et modes local/distant, permissions et filtres documentés. |
| grafana-mcp | **CLEAR** | Apache-2.0 du serveur ; versions et permissions par outils ; écritures explicitement documentées. |
| docker-mcp-gateway | **RETAIN REVIEW** | MIT établi ; seulement des prereleases observées, correspondance Desktop/plugin et périmètre AI Governance à stabiliser. |
| k8sgpt | **RETAIN REVIEW** | Apache-2.0 établi ; contradiction confidentialité/logs et portée limitée de l'anonymisation à résoudre pour la fiche. |
| litellm | **RETAIN REVIEW** | Proxy/SDK OSS MIT établi, Enterprise sous licence distincte ; termes de souscription non disponibles dans le texte public et périmètre du paquet/image à préciser. |
| ollama | **CLEAR** | Runtime MIT établi ; modèles et services cloud explicitement séparés ; retirer la promesse absolue zero cloud dependency. |
| open-webui | **RETAIN REVIEW** | Licence actuelle personnalisée avec branding, historique MIT/BSD ; classification et représentation de licence à faire valider humainement. |

**Réel après cette passe : 0 CLEAR appliqué / 10 fiches toujours en revue.** Les six propositions ne modifient aucun compteur.

## 4. Dossiers indépendants

### 4.1 azure-mcp-server — CLEAR proposé

**Preuves lues.** Le [README historique](https://github.com/Azure/azure-mcp/blob/54f04ab1ade20b4adc4955cffea0833788307596/README.md) au commit `54f04ab1ade20b4adc4955cffea0833788307596` annonce l'archivage au 25 août 2025 et le transfert du code et des issues vers `microsoft/mcp`. Le [README du monorepo](https://github.com/microsoft/mcp/blob/61715e6a9054d7922809b01e08a2efa85e032a6d/README.md) identifie le sous-produit Azure ; [LICENSE](https://github.com/microsoft/mcp/blob/61715e6a9054d7922809b01e08a2efa85e032a6d/LICENSE) accorde MIT au code principal. Le [README Azure](https://github.com/microsoft/mcp/blob/61715e6a9054d7922809b01e08a2efa85e032a6d/servers/Azure.Mcp.Server/README.md) et la release 3.0.0 fixée ci-dessus documentent les outils Azure. Pas de nouveau projet à créer sous un autre ID.

**Fonctions, compatibilité, maintenance.** Serveur MCP donnant accès aux services Azure et à des opérations de développement/exploitation via des outils dédiés ; ce n'est pas une simple collection de documentation. Les chemins d'installation décrivent Node.js LTS pour npm/npx et .NET 10 SDK pour dnx, à distinguer des prérequis de chaque hôte. Le README conserve une mention GA 2.0 et le changelog de ce commit ne contient pas encore une entrée finale 3.0.0 : la preuve de version est la release 3.0.0, pas ces mentions restées en retard. Maintenance observée : stable récente et betas 4.0 ; pas de garantie de support à long terme. [Présentation officielle](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/overview).

**Licence et adoption.** `MIT` pour le serveur ; consommation Azure, client IA et composants tiers ont leurs conditions propres. La migration ne transforme pas le dépôt historique archivé en produit abandonné. Pertinent pour Cloud/Platform Engineering, diagnostic et contexte Azure.

**Risques / limites.** Les [consignes de sécurité Microsoft](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security) imposent de limiter RBAC, outils et identités ; elles déconseillent données et identifiants de production pour le serveur local. Recommandation : identités dédiées, scopes minimaux, validation TLS/audience pour le distant, contrôle humain des mutations. Ne pas confondre authentification Entra et autorisation individuelle ; sorties d'outils et ressources cloud peuvent alimenter le contexte du LLM. **P1 conditionnel :** identité sur-privilégiée ou endpoint détourné ; **P2 :** mise à jour automatique non épinglée.

**Composants et notices.** Le [NOTICE.txt](https://github.com/microsoft/mcp/blob/61715e6a9054d7922809b01e08a2efa85e032a6d/NOTICE.txt) a aussi été consulté : il agrège des notices tierces (notamment 0BSD et Apache-2.0) et prévoit la rétro-ingénierie nécessaire au débogage de bibliothèques LGPL lorsqu'applicable. Ce n'est pas une exception SPDX globale à ajouter à MIT, ni une preuve que tous ces composants sont livrés dans chaque paquet Azure. Une redistribution doit conserver les notices du livrable effectivement choisi.

**Champs proposés.** Ajouter `repository_url: https://github.com/microsoft/mcp` et la documentation officielle, `license_model: oss`, `license_spdx: MIT`, résumé précis et limites ci-dessus. Préserver `official_url` et les sources historiques ; ajouter les deux preuves de migration et la licence au SHA. L'archivage proposé est false pour le dépôt **actuel**, pas pour l'ancien.

### 4.2 kubernetes-mcp-server — CLEAR proposé

**Preuves lues.** [README et inventaire des outils](https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/README.md), [LICENSE Apache-2.0](https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/LICENSE), [référence TOML](https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/docs/configuration.md), [changements de configuration](https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/docs/configuration-changes.md) et [guide ServiceAccount](https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/docs/getting-started-kubernetes.md), tous au commit du tableau. L'identité canonique actuelle est bien le projet Go de l'organisation containers ; aucune migration n'a été établie dans ces lectures. Ne pas attribuer ce serveur à Kubernetes/CNCF comme produit officiel sur la seule base de son nom.

**Fonctions et compatibilité.** Accès direct API Kubernetes/OpenShift, kubeconfigs multiclusters, outils ressources/pods/logs et toolsets Helm/Tekton selon configuration et APIs présentes. `pods_exec`, `pods_run`, `resources_create_or_update`, `resources_delete`, scale et Helm sont des opérations actives. L'apply utilise l'état désiré complet : omettre un champ précédemment géré peut l'effacer. Les toolsets spécialisés nécessitent les APIs/CRDs correspondantes ; aucune compatibilité universelle entre versions de clusters n'est démontrée. [go.mod](https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/go.mod) fixe Go 1.26.10 pour compiler, ce n'est pas un prérequis Go pour utiliser le binaire.

**Licence / maintenance / pertinence.** `Apache-2.0` du serveur, licences des dépendances et charts séparées ; release v0.0.69 et dépôt non archivé. Utile pour diagnostic Platform/SRE et assistance aux opérations, sous contrôle de changement.

**Risques et garde-fous.** Dans cette version, utiliser TOML `read_only = true`, pas recopier un ancien `--read-only` supprimé. `disable_destructive` n'est pas équivalent à lecture seule. Le filtrage par annotations d'outils ne remplace pas un ServiceAccount RBAC dédié, namespaces limités, interdiction Secrets/ConfigMaps et restriction des clusters dans le kubeconfig. Le guide propose un compte de lecture et un token borné ; lire peut tout de même révéler des données. En HTTP, authentification du client, identité Kubernetes effective et restrictions réseau doivent être examinées séparément. **P1 conditionnel :** cluster-admin partagé, exec ou endpoint exposé ; **P2 :** logs sensibles et configuration devenue incompatible après upgrade.

**Champs proposés.** Conserver le dépôt et `license_model: oss` ; ajouter `license_spdx: Apache-2.0`, URL documentation du README au SHA, `use_when` et `avoid_when` pour RBAC/mutations. Déplacer la mention de licence du résumé vers son champ dédié ; ne pas promettre la sûreté automatique du cluster.

### 4.3 terraform-mcp-server — CLEAR proposé

**Preuves lues.** [README](https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/README.md), [LICENSE MPL-2.0](https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/LICENSE), [go.mod](https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/go.mod), [registre des outils et gates](https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/pkg/toolsets/registry.go) et [filtrage](https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/pkg/toolsets/filter.go). Le module est `github.com/hashicorp/terraform-mcp-server` ; le copyright du LICENSE est HashiCorp et les fichiers Go lus indiquent IBM avec SPDX MPL-2.0. Ne pas lui appliquer par association la licence du moteur Terraform ni l'identité d'un autre serveur MCP Terraform.

**Fonctions et contraintes.** Documentation providers/modules/policies du Registry public ; registries privés et opérations HCP Terraform/Terraform Enterprise après authentification. Le toolset par défaut est Registry ; activer `terraform` ou `all` élargit la surface. Les flags `--toolsets` et `--tools` sont mutuellement exclusifs. Stdio local et Streamable HTTP ; l'ancienne valeur de transport http est encore décrite comme compatible. Le README distingue les instructions des versions >=0.3.0 et <=0.2.3. À v1.4.1, compilation Go 1.26.10 ; Docker en marche pour le chemin conteneur. Ce serveur ne garantit pas l'exécution arbitraire d'un projet via le CLI local `terraform plan/apply`. Les versions du CLI/providers dans le workspace et la compatibilité de l'API TFE doivent être vérifiées pour l'installation retenue ; aucune borne TFE universelle n'a été établie ici. [Référence officielle courante](https://developer.hashicorp.com/terraform/mcp-server/reference).

**Limite cruciale des gates.** `ENABLE_TF_OPERATIONS=false` ne signifie pas read-only. Le registre exige ce gate pour delete_project/delete_team/delete_workspace_safely, force_unlock et action_run ; create_workspace, update_workspace, create_workspace_variable, grant_team_access et d'autres écritures sont enregistrées sans ce gate, sous réserve de toolset et session TFE. `create_run` porte en plus un commentaire de cas spécial : ne pas généraliser son comportement sans lire son handler. Les opérations HCP de run peuvent aboutir à un apply selon options/politiques du workspace ; conserver les gates et approbations serveur/client.

**Licence / maintenance / usage professionnel.** `MPL-2.0` pour le serveur ; HCP/TFE et providers/modules séparés. Release v1.4.1 et dépôt actif au sens non archivé. Pertinent pour IaC assistée, recherche de documentation et workflows HCP, sans remplacement du contrôle Git/plan/policy.

**Risques.** Les variables, plans, logs et états peuvent contenir des secrets. Préférer tokens utilisateurs/équipes limités, allowlist d'organisations, TLS et `TFE_ADDRESS` fixé côté serveur. Le README interdit le passthrough d'adresse client et les tokens en query string. Les headers individuels ne rendent pas automatiquement un serveur partagé sûr. **P1 conditionnel :** token administrateur ou actions de runs non maîtrisées ; **P2 :** confusion version du serveur / moteur / providers et données sensibles envoyées au LLM.

**Champs proposés.** Conserver dépôt et `oss`, ajouter `license_spdx: MPL-2.0`, documentation et résumé Registry/HCP/TFE ; ajouter une limite explicite sur écritures, secrets et absence de plan/apply local générique.

### 4.4 github-mcp-server — CLEAR proposé

**Preuves lues.** [LICENSE MIT](https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/LICENSE), [README officiel](https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/README.md), [configuration](https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/docs/server-configuration.md) et [module Go v2](https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/go.mod). La release v2.0.3 est marquée `immutable=true` par l'API. L'API Go exportée est explicitement décrite comme instable, ce qui n'annule pas la release du serveur. Pas de migration de dépôt établie par ces lectures.

**Fonctions / compatibilité.** Lecture et écriture de dépôts, issues, PRs et outils GitHub selon droits/toolsets ; déploiement distant officiel et exécution locale stdio/binaire/conteneur. OAuth/PAT et parcours Enterprise dépendent de l'hôte et de GitHub.com/GHES/ghe.com ; ne pas supposer que l'endpoint distant fonctionne pour toutes les instances GHES. Le module v2 demande Go 1.27.3 à la compilation ; les anciens clients gardent des réponses compatibles selon la version MCP négociée.

**Licence / pertinence.** MIT du code serveur ; droits d'accès, abonnements et conditions du service GitHub/Copilot demeurent séparés. Pertinent pour revue de PR, triage et exploration DevOps/CI, sans accorder automatiquement un droit de push ou de merge.

**Risques et limites.** `--read-only` / `GITHUB_READ_ONLY`, allowlists d'outils et PAT fine-grained réduisent la surface. Lockdown filtre certains contenus d'auteurs sans accès push, mais ne constitue pas une protection générale contre l'injection de prompt. Dépôts, commentaires et PR externes restent des données non fiables ; séparer lecture, écriture et droits Actions/secrets. **P1 conditionnel :** jeton trop large et modification de workflow/code ; **P2 :** exfiltration de code privé via le modèle. Aucun compte ou token utilisateur n'a été utilisé pour tester ces accès.

**Composants.** Les inventaires amont [linux](https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/third-party-licenses.linux.md), [windows](https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/third-party-licenses.windows.md), [darwin](https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/third-party-licenses.darwin.md) ont été lus : ils distinguent les dépendances et leurs licences MIT, BSD-3-Clause et Apache-2.0, dont les notices du SDK MCP. MIT est donc le SPDX du projet principal, pas une licence unique de toutes les dépendances. Aucun contrôle exhaustif de leurs textes amont ou du contenu de chaque binaire n'est revendiqué.

**Champs proposés.** Conserver URL et `oss`, ajouter `MIT`, documentation officielle fixée, résumé précis, limites permissions/injection et déploiements local/distant décrits sans présumer l'éligibilité commerciale.

### 4.5 grafana-mcp — CLEAR proposé

**Preuves lues.** [LICENSE Apache-2.0](https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/LICENSE), [README, RBAC et outils](https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/README.md), [go.mod](https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/go.mod), release v2.1.1. Le serveur appartient au dépôt Grafana actuel non archivé ; aucune migration d'identité établie. Ne pas lui attribuer automatiquement AGPL sur la base de la licence d'autres produits Grafana.

**Fonctions / compatibilité / maintenance.** Interroge dashboards, métriques/logs/datasources, alertes et intégrations ; peut aussi créer/modifier dashboards et alertes. Le README pose Grafana >=9.0 pour les APIs de base, avec des exigences plus élevées pour certains outils/plugins. Exemples : rendu et plugins Cloud/Assistant à examiner par fonction ; Grafana 9 n'est pas une garantie de toutes les fonctions. Go 1.26.9 pour compiler. La release v2.1.1 corrige un comportement dashboards v1/v2 : épingler le serveur et vérifier la version Grafana.

**Licence / adoption.** Apache-2.0 du serveur ; Grafana Cloud, plugins, OnCall/Incident/Assistant et services connectés ont disponibilité et conditions séparées. Pertinent pour SRE, exploration d'incidents et observabilité, sans garantie de disponibilité des fonctions commerciales.

**Risques.** Token de ServiceAccount limité aux actions **et scopes** de chaque outil ; ne pas choisir Editor par commodité. `--disable-write` réduit les écritures, mais `--enable-write-tools` et `--enable-query` peuvent réactiver des outils ; les requêtes SQL brutes nécessitent aussi des identifiants datasource réellement en lecture seule. `--disable-query` désactive les outils de requête tout en conservant les métadonnées. Sécuriser le transport HTTP séparément de l'authentification à Grafana ; logs/dashboards peuvent révéler secrets et données métier. **P1 conditionnel :** changements d'alertes ou datasource sur-privilégiée ; **P2 :** coût et volume des requêtes/contexte.

**Champs proposés.** Conserver dépôt et `oss`, ajouter `Apache-2.0`, documentation au README fixé, résumé lecture/écriture et limites versions/scopes/coûts. L'actuel use_when de consultation ne suffit pas à décrire le périmètre.

### 4.6 docker-mcp-gateway — RETAIN REVIEW proposé

**Preuves lues.** [LICENSE MIT](https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/LICENSE), [README](https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/README.md), [guide Gateway](https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/docs/mcp-gateway.md), [modèle de sécurité](https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/docs/security.md) et [go.mod](https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/go.mod). Le commit de main lu correspond à v0.44.3. L'[API releases](https://api.github.com/repos/docker/mcp-gateway/releases?per_page=100) contient 74 releases, toutes prerelease, dernière v0.44.3. La page HTML consultée via latest affichait encore v0.44.2 ; privilégier la liste API datée et le SHA résolu, sans prétendre à une stable.

**Périmètre / compatibilité.** Plugin `docker mcp`, profils/catalogues, cycle de vie des serveurs conteneurisés, routage, secrets/OAuth, stdio et HTTP. README : Docker Desktop 4.59+ avec Toolkit pour ce parcours, options Docker CE/WSL indépendantes ; son indication Go 1.24+ pour le développement est moins précise que le go.mod 1.26.10 du commit. La [documentation Docker](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/) distingue aussi le Gateway OSS et l'offre AI Governance sur invitation. Aucun droit Desktop ou Governance n'est déduit de MIT.

**Risques / utilité.** Utile à Platform Engineering pour centraliser et isoler les serveurs ; le daemon Docker, OS, configuration et credential store demeurent de confiance. Le modèle documente Bearer par défaut en HTTP, contrôles d'URL, signatures pour le namespace mcp et secrets par serveur. Ces garanties ont une portée précise : images tierces non couvertes par ces signatures, egress réseau non interdit globalement, opt-outs possibles. Un serveur autorisé peut accéder aux ressources explicitement accordées ; conteneurisation ne prouve pas l'absence d'exfiltration. **P1 conditionnel :** mounts/daemon/secrets trop larges ; **P2 :** adoption d'une prerelease et drift Desktop/plugin.

**Réserve à lever.** Fixer le canal de distribution approuvé, la relation version Desktop/plugin, et l'acceptation explicite de la maturité prerelease ; ne pas fabriquer une version stable. Garder review. Proposer malgré cela `license_spdx: MIT` pour le gateway, conserver `oss`, ajouter les limites et preuves ; ne pas inclure catalogues/serveurs/images ou offre Governance dans cette licence.

### 4.7 k8sgpt — RETAIN REVIEW proposé

**Preuves lues.** [LICENSE Apache-2.0](https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/LICENSE), [README](https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/README.md), [politique de support](https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/SECURITY.md), [go.mod](https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/go.mod) et [analyseur de logs](https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/analyzer/log.go). [Documentation](https://docs.k8sgpt.ai/) et [confidentialité](https://docs.k8sgpt.ai/reference/guidelines/privacy/) également lues. Support de sécurité annoncé pour la dernière release, pas de promesse LTS.

**Périmètre / compatibilité.** Analyseurs Kubernetes, diagnostic/triage et explications via backend IA choisi ; CLI, mode serveur/MCP et opérateur distinct. Le README donne MCP >=0.4.14 ; version examinée v0.4.41. Compilation Go 1.26.3 avec toolchain 1.26.5. Les dépendances client-go ne prouvent pas une matrice complète de versions Kubernetes. Usage SRE d'assistance au diagnostic ; ce n'est pas une preuve d'auto-remédiation fiable ou d'autorisation de changement.

**Incohérence constatée.** La page privacy affirme ne pas collecter de logs, tandis que le README propose un logAnalyzer optionnel. Le code fixé `LogAnalyzer` liste les pods, lit leurs logs (100 dernières lignes) et produit des erreurs contenant une ligne de log ; le champ Sensitive masque ici le nom de pod, sans démontrer une suppression générale des secrets contenus dans la ligne. L'option `--explain` transmet des résultats au backend selon la documentation. L'option `--anonymize` ne doit donc pas être présentée comme une garantie complète de confidentialité. C'est une contradiction documentaire et une analyse statique de flux potentiel, pas une vulnérabilité reproduite.

**Risques / réserve.** RBAC lecture minimale et accès pods/log seulement si nécessaire ; désactiver les analyseurs inutiles et valider backend, données transmises, cache et politique de rétention. `--explain` vers un backend externe peut exporter du contexte cluster ; backend local possible, mais licences de modèles et isolation séparées. **P1 conditionnel :** secrets de logs transmis ; **P2 :** diagnostic erroné et politique privacy trop générale. Lever l'ambiguïté de la formulation et faire relire le périmètre de données avant CLEAR ; aucun contact amont créé.

**Champs proposés.** `license_model: oss` conservé, `license_spdx: Apache-2.0` recommandé ; ajouter documentation, limites d'anonymisation, contexte externe et absence de garantie de remédiation. Remplacer l'actuel avoid_when sur l'expertise de l'équipe par une limite objective de confidentialité. Conserver review.

### 4.8 litellm — RETAIN REVIEW proposé

**Preuves lues.** [LICENSE principal](https://github.com/BerriAI/litellm/blob/ea7ca16dbc3904d9e59a9505f379a2ca3091821f/LICENSE), [licence Enterprise réelle](https://github.com/BerriAI/litellm/blob/ea7ca16dbc3904d9e59a9505f379a2ca3091821f/enterprise/LICENSE.md), [README](https://github.com/BerriAI/litellm/blob/ea7ca16dbc3904d9e59a9505f379a2ca3091821f/README.md) et [métadonnées paquet](https://github.com/BerriAI/litellm/blob/ea7ca16dbc3904d9e59a9505f379a2ca3091821f/pyproject.toml), release v1.106.4. La référence `enterprise/LICENSE` dans la licence racine renvoie en pratique au fichier `enterprise/LICENSE.md` du tree consulté ; ce dernier a bien été lu, sans se limiter au badge ou à `license = MIT` du pyproject.

**Licence et limites commerciales.** Le code hors enterprise est MIT, y compris la partie OSS du proxy ; `enterprise/` relève d'une licence propriétaire. La production de ces composants requiert souscription/accord et licence Enterprise valide au bon nombre de sièges ; développement/test bénéficie d'une permission distincte, sans droit général de redistribution. Les conditions complètes de souscription sont à obtenir auprès de BerriAI : elles n'ont pas été consultées. Les composants tiers conservent leurs licences.

**Fonctions / compatibilité / maintenance.** SDK et passerelle/proxy multi-fournisseur, clés virtuelles, routage, budgets, rate limits et suivi de coûts ; Python >=3.10 et <3.15 au commit. [Documentation Enterprise](https://docs.litellm.ai/docs/enterprise) : SSO/SCIM, audit, rôles et certaines intégrations de secrets/guardrails sont soumis à des conditions Enterprise ; ne pas promettre toutes ces fonctions sous MIT. Cette page décrit SSO gratuit jusqu'à cinq utilisateurs, pas une permission globale Enterprise. Stable GitHub observée v1.106.4 ; ne pas confondre avec un alias d'image de canal de production.

**Risques / pertinence.** Utile à Platform/FinOps pour gouverner plusieurs fournisseurs. Centralise clés, prompts, réponses, logs/callbacks et coûts ; séparer clé master et clés virtuelles, limiter admins, destinations, budgets et rétention. Héberger le proxy dans son VPC n'empêche pas la transmission au fournisseur choisi ; ne pas reprendre une promesse générale « aucune donnée ne sort ». **P1 conditionnel :** clés providers ou master compromises ; **P2 :** dépassement budgétaire, mélange de données locataires ou fonctionnalité commerciale présumée OSS.

**Réserve / champs.** Garder `license_model: open-core`, proposer `commercial_offering: true`. `license_spdx: MIT` n'est acceptable que comme **licence du cœur OSS**, avec limitation explicite dans summary/avoid_when et sources ; ce n'est pas un SPDX du produit/image entier. Fixer le paquet/image et ses composants activés et obtenir les conditions commerciales nécessaires avant de clore cette revue. Garder needs-review ; prix et droits de souscription non inventés.

### 4.9 ollama — CLEAR proposé

**Preuves lues.** [LICENSE MIT](https://github.com/ollama/ollama/blob/675150d6ad2747df1e218ef59de9194bc4a7e538/LICENSE), [README](https://github.com/ollama/ollama/blob/675150d6ad2747df1e218ef59de9194bc4a7e538/README.md) et release v0.40.11 ; [FAQ officielle](https://docs.ollama.com/faq) et [authentification API](https://docs.ollama.com/api/authentication). Identité Ollama, dépôt actuel non archivé ; pas de migration établie par cette passe.

**Licence / périmètre.** MIT du runtime principal, **aucune licence uniforme pour les modèles téléchargés**. Les poids, modèles dérivés, conditions d'usage et services cloud se vérifient modèle par modèle avant adoption ; aucun modèle n'est sélectionné ou autorisé ici. Le runtime fournit gestion et exécution de modèles et API ; le projet actuel inclut également des capacités cloud. Conserver cette distinction dans les métadonnées et les avertissements.

**Compatibilité / maintenance / pertinence.** Parcours macOS, Linux, Windows et conteneurs ; capacité GPU, VRAM/RAM et support de l'accélération dépendent du matériel et du modèle. Une API compatible ne signifie pas parité complète de toutes les fonctions de fournisseurs. Release récente, pas de garantie de capacité multi-nœud/SLA. Pertinent pour laboratoire Platform/DevOps, assistants locaux et données confinées avec un déploiement réellement local.

**Risques / corrections.** L'API locale n'exige pas d'authentification ; bind par défaut 127.0.0.1:11434. Étendre le bind nécessite protection réseau/authentification appropriée. La FAQ décrit `OLLAMA_NO_CLOUD=1` pour désactiver fonctions cloud ; poids et dépendances doivent aussi être disponibles localement pour un mode sans réseau. **P1 conditionnel :** API sans authentification exposée ; **P2 :** licence des poids non revue, consommation GPU et transfert cloud involontaire. Corriger « zero cloud dependency » en capacité locale conditionnelle. L'actuel « enterprise support » ne doit pas être une négation absolue d'offres commerciales non examinées.

**Champs proposés.** Conserver `oss`, ajouter `MIT` limité au runtime, documentation, use_when/avoid_when corrigés ; aucune licence de modèle déduite et aucun droit cloud assimilé à MIT.

### 4.10 open-webui — RETAIN REVIEW proposé

**Preuves lues.** [licence actuelle](https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/LICENSE), [historique](https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/LICENSE_HISTORY), [README](https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/README.md) et [pyproject](https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/pyproject.toml), release v0.12.4. La [page licence officielle](https://docs.openwebui.com/license/) situe le changement à v0.6.6 en avril 2025 ; le LICENSE_HISTORY conserve les grants historiques BSD-3-Clause et MIT suivant les contributions/commits. Le nom historique n'est pas une raison de créer un nouvel ID.

**Licence exacte.** La licence actuelle se nomme **Open WebUI License**, avec clause additionnelle de branding. Elle interdit de modifier/retirer/masquer/remplacer les marques sauf : au plus 50 personnes physiques ayant accès sur toute fenêtre glissante de 30 jours, permission écrite du titulaire, ou licence Enterprise l'autorisant expressément. La borne exacte du texte de licence prime sur les résumés : 50 entre dans l'exception, 51 n'y entre pas. Le maintien du branding permet des usages que le rebranding ne permet pas ; ne pas inventer une interdiction générale d'usage commercial.

**Classification proposée, non appliquée.** `license_model: oss` est trop large pour caractériser le produit actuel complet comme BSD/MIT sans restriction. Proposer `source-available` au sens de la taxonomie du catalogue, en précisant que c'est notre classification. Aucun SPDX standard simple n'est établi pour l'ensemble actuel ; laisser `license_spdx` absent jusqu'à décision humaine sur un éventuel LicenseRef documenté. Ne pas fabriquer `BSD-3-Clause` comme licence globale ni écraser les droits historiques. `commercial_offering: true` est étayé par l'offre Enterprise ; conditions contractuelles non consultées.

**Fonctions / compatibilité / maintenance.** Plateforme web auto-hébergée, utilisateurs/RBAC, RAG, outils et connexions Ollama/API compatibles, locales ou distantes ; pas un moteur d'inférence en soi. Python >=3.11 et <3.13.0a1 pour le paquet examiné ; conteneurs/stockage/GPU selon le chemin retenu. Release récente, migrations base/plugins/backends à contrôler avant upgrade.

**Risques / pertinence / réserve.** [Politique de sécurité](https://docs.openwebui.com/security/security-policy/) : Tools/Functions/Pipelines peuvent exécuter du Python avec les droits du backend et accéder aux fichiers, réseau, variables et base. Limiter ces permissions à des utilisateurs de confiance, isoler le service, contrôler sauvegardes, rétention de conversations/documents et providers externes. Les sandboxes de certaines fonctions ne rendent pas toutes les extensions sûres. Usage utile comme portail IA interne pour Platform Engineering, sous gouvernance. **P1 conditionnel :** extension non fiable ou permission équivalente à admin ; **P2 :** branding/redistribution non conformes et confidentialité. Faire valider la représentation de licence, l'agrégat d'utilisateurs et le scénario de branding avant CLEAR.

## 5. Valeurs anciennes et corrections recommandées — aucune appliquée

### Champs communs et invariants d'application future

| Champ | Valeur réellement présente sur les dix fiches | Recommandation documentaire |
|---|---|---|
| status / needs_review | `needs-review` / `true` | inchangés pendant cette passe ; seules des décisions expressément approuvées à la seconde passe pourront changer ces champs |
| verified_on | `2026-08-03` | ne pas rafraîchir maintenant ; utiliser la date de la seconde vérification effective si une modification canonique est autorisée |
| maturity | `unknown` | conserver tant qu'un niveau précis n'a pas été justifié ; release stable et dépôt non archivé ne suffisent pas à « established » |
| license_spdx | absent | MIT : Azure, GitHub, Docker et runtime Ollama ; Apache-2.0 : Kubernetes, Grafana, K8sGPT ; MPL-2.0 : Terraform ; LiteLLM MIT seulement au périmètre OSS ; Open WebUI absent en attente |
| repository_archived | absent | candidat `false` pour le dépôt actuel de chaque fiche, après nouvelle lecture API ; ne pas coder false pour l'ancien Azure |
| documentation_url | absent | ajouter la documentation primaire lue par outil, indiquée dans les dossiers ; Azure Learn, README fixés pour Kubernetes/Terraform/GitHub/Grafana/Docker, docs K8sGPT/LiteLLM/Ollama/Open WebUI |
| sources | uniquement références `legacy:` | **ajouter** les URLs effectivement lues de licence, README, release et limites de chaque dossier ; conserver intégralement les anciennes sources |
| deployment_models | `[]` | ne pas remplir par un vocabulaire inventé ; mapper les parcours démontrés à la taxonomie avant proposition finale |
| categories / subcategories / roles / lifecycle_stages / alternatives / tags | valeurs existantes | conserver ; ce lot ne justifie pas de reclassement global ni d'extension du schéma |

Ne pas ajouter de champ version, publisher ou security inventé : le schéma n'en expose pas. Versions, périmètres et réserves restent dans ce ledger et, si approuvé, dans summary/use_when/avoid_when/sources.

### Résumés : anciennes valeurs exactes et formulations candidates

| ID | summary actuel | summary recommandé |
|---|---|---|
| azure-mcp-server | Azure MCP server implementation. | Microsoft MCP server connecting agents to Azure services and resource operations; developed in microsoft/mcp. |
| kubernetes-mcp-server | Go-native MCP server for Kubernetes and OpenShift with direct API server integration, multi-cluster support, Helm/Tekton toolsets, and no external CLI dependencies (Apache-2.0). | Go-native MCP server for Kubernetes and OpenShift with direct API access, multi-cluster configuration and optional ecosystem toolsets. |
| terraform-mcp-server | MCP server for Terraform automation and infrastructure-as-code workflows. | HashiCorp MCP server for Terraform Registry discovery and authenticated HCP Terraform/Terraform Enterprise workspace and run workflows. |
| github-mcp-server | GitHub's MCP server implementation. | Official GitHub MCP server exposing repository, issue and pull-request operations through local or hosted connections. |
| grafana-mcp | Model Context Protocol for Grafana. | MCP server for Grafana observability queries and permission-controlled dashboard and alerting operations. |
| docker-mcp-gateway | Docker CLI plugin and gateway for discovering, running, and routing MCP servers in containers. | conserver le résumé ; ajouter la maturité prerelease et les limites d'isolation dans avoid_when |
| k8sgpt | AI-powered Kubernetes troubleshooting. | Kubernetes analyzers for diagnostic triage with optional explanations from a configured AI backend. |
| litellm | Gateway and proxy for 100+ LLM providers with budgets, rate limiting, logging, and spend tracking. | LLM SDK and gateway with an MIT-licensed OSS proxy core and separately licensed Enterprise components. |
| ollama | Local LLM runtime and model manager; open-source core (model licenses vary). | Model runtime and manager supporting local inference and optional cloud features; model licenses are separate. |
| open-webui | Self-hosted web UI for running and managing local AI model backends (e.g., Ollama). | Self-hosted AI web platform for Ollama and compatible APIs, under the Open WebUI License with branding conditions and separately licensed legacy code. |

### Autres corrections par champ

| ID | Ancienne valeur / manque | Correction recommandée et justification |
|---|---|---|
| azure-mcp-server | `license_model: documentation` ; repository_url absent ; avoid_when limité à absence Azure/MCP | `oss`, dépôt microsoft/mcp, MIT ; ajouter risque identité Azure, mutations et usage local hors production selon Microsoft |
| kubernetes-mcp-server | `oss` ; use_when/avoid_when vides | conserver oss ; assistance Kubernetes/OpenShift ; limiter RBAC, secrets, exec, apply et exposition HTTP ; TOML read_only pour cette version |
| terraform-mcp-server | `oss` ; use_when/avoid_when vides | conserver oss, MPL-2.0 ; Registry et opérations HCP/TFE sélectionnées ; avertir que le gate TF_OPERATIONS ne bloque pas toutes les écritures |
| github-mcp-server | `oss` ; avoid_when ne traite que GitLab/Bitbucket ou absence de besoin | conserver oss ; ajouter permissions minimales, contenu externe non fiable, contrôle humain des écritures et limites GHES |
| grafana-mcp | `oss` ; use_when décrit uniquement query dashboards/alerts/datasources | conserver oss ; expliciter également écritures, scopes, versions/plugins et droits datasource |
| docker-mcp-gateway | `oss` ; use_when/avoid_when vides | conserver oss ; centralisation MCP ; MIT du gateway seulement, prereleases et conditions Desktop/Governance distinctes |
| k8sgpt | `oss` ; avoid_when actuel déconseille l'outil si expertise K8s/runbooks déjà présents | conserver oss ; remplacer cette opinion par limites de données, logs, anonymisation et besoin de validation humaine des recommandations |
| litellm | `open-core` ; commercial_offering absent ; avoid_when vide | conserver open-core ; proposer commercial_offering true, scope MIT cœur OSS seulement et Enterprise non autorisé globalement ; risques clés/prompts/budgets |
| ollama | `oss` ; use_when promet « zero cloud dependency » ; avoid_when mentionne besoin multi-nœud ou enterprise support | conserver oss ; usage local après téléchargement et cloud désactivé si requis ; limites capacité/GPU/contrôle d'accès, sans négation générale des offres commerciales |
| open-webui | `oss` ; commercial_offering absent ; avoid_when uniquement absence de besoin web | proposer source-available et commercial_offering true ; pas de BSD/MIT global ; branding <=50/30 jours ou permission/licence, plugins de confiance et données |

Aucune redirection d'URL ne justifie de remplacement global. Pour Azure, conserver l'URL officielle existante et l'historique de migration. Une vérification globale de collisions de repository_url reste obligatoire avant tout ajout canonique, en particulier pour le monorepo Microsoft.

## 6. Risques P1/P2 et sujets ouverts

Ces priorités sont des **risques d'adoption conditionnels**, pas des vulnérabilités démontrées ni un résultat de scan.

| Priorité | Risque | Outils / résolution attendue |
|---|---|---|
| P1 | Mutations d'infrastructure ou de code avec une identité trop large | Azure, Kubernetes, Terraform, GitHub, Grafana : RBAC minimal, liste positive d'outils, lecture seule réelle et approbation séparée pour actions |
| P1 | Secrets ou données sensibles envoyés au client/LLM | K8sGPT logs, Terraform états/plans, Grafana logs, LiteLLM clés/prompts, tous MCP : tracer les données, destinations et rétention |
| P1 | Exécution de code avec droits du backend/hôte | Open WebUI extensions, Kubernetes exec, Docker permissions : limiter les personnes de confiance, isoler et réduire accès |
| P1 | Endpoint sans authentification ou identité partagée exposé | Ollama API locale ; MCP distants : authentifier, limiter réseau, vérifier TLS et identité effective |
| P2 | Licence/branding/composants commerciaux mal représentés | Open WebUI et LiteLLM : arbitrage humain et périmètre explicite avant CLEAR |
| P2 | Prerelease ou drift de versions/packages/tool schemas | Docker ; Azure beta/Template ; Kubernetes TOML ; Terraform >=0.3.0 ; épingler serveur, paquet et configuration |
| P2 | Compatibilité insuffisamment caractérisée | Matrice cluster/API TFE/plugins Grafana/GHES/GPU : à vérifier pour le déploiement retenu, sans en déduire un support universel |
| P2 | Source privacy K8sGPT dépassée pour les logs | Réconcilier page privacy et analyseur fixé ; documenter les données autorisées avant retrait de review |

Blocages documentaires explicites : Docker stable/canal Desktop non établi ; LiteLLM conditions de souscription et composition exacte du livrable ; K8sGPT périmètre logs/confidentialité ; Open WebUI représentation de licence et scénario branding. Ces points restent ouverts. Les autres outils ont des limites d'adoption connues qui doivent figurer dans une éventuelle correction, sans exiger de tests réels dans cette première passe.

## 7. Contrôles réellement exécutés

Environnement utilisé : `.venv/Scripts/python.exe`, **Python 3.12.14**. L'alias système `python.exe` WindowsApps a échoué au lancement ; les commandes Python ont été relancées avec le chemin du venv. Aucun changement des contraintes Python ou des dépendances du dépôt.

| Commande / lecture | Résultat |
|---|---|
| git status --short ; git branch --show-current ; git rev-parse HEAD/main ; git ls-tree | checkout initial propre, main et blobs attendus |
| GET API GitHub commits/main | SHA distant attendu observé |
| python -m scripts.review_debt --format json | succès avec venv ; 1 425 / 595 / 77 ; inventaire filtré en mémoire, aucun rapport sous reports/ |
| Lecture YAML + Counter des status + taxonomie | 816 actives, 595 needs-review, 30 catégories, cible 80/58 et dix IDs présents |
| python -m pip install -e '.[dev]' | succès après relance autorisée hors restriction des temporaires Windows ; mêmes contraintes, aucune mise à jour de fichier de dépendances |
| python -m ruff check scripts tests | succès |
| python -m ruff format --check scripts tests | succès, 70 fichiers déjà formatés ; avertissement d'écriture du cache Windows |
| python -m scripts.generate_docs --check | succès, documentation générée à jour ; génération en écriture non exécutée, aucun changement canonique |
| python -m scripts.validate_catalog | succès avant rédaction ; contrôle final consigné ci-dessous |
| python -m pip check | succès, aucune dépendance cassée |
| python -m pytest | essais interrompus après erreurs de fixtures temporaires Windows ; diagnostic -x -vv : création du répertoire numéroté pytest impossible |
| Relance pytest avec --basetemp=tmp/wave28-pytest-20261027-a -o cache_dir=tmp/wave28-pytest-cache-a -x | 36 passed / 1 failed : le scan Markdown du dépôt découvre une fixture volontairement invalide dans tmp/ ; ces seuls temporaires ont été supprimés, puis la suite a été relancée hors du dépôt |
| git diff --check et contrôle exact du périmètre | résultat final consigné ci-dessous |

Les consultations réseau documentaires ont été réalisées ; **Full link audit / strict link audit non exécuté**, aucun workflow distant déclenché, aucun scan automatique ni test runtime des dix outils. Un audit de liens ne remplacerait pas les preuves de licence ou de maintenance. Les échecs de chemins documentaires exploratoires ont été remplacés par les fichiers effectivement résolus ci-dessus ; aucune conclusion n'est tirée d'un 404.

## 8. Seconde passe contrôlée : critères et prochaine action

1. Relire le ledger et statuer humainement sur chacune des six propositions CLEAR et sur les quatre réserves ; documenter les réponses manquantes sans objectif de quota. Première action précise : préparer une matrice d'application champ par champ pour ces seuls dix IDs, en commençant par migration/classification Azure et frontière de licence Open WebUI, **sans exécuter l'application**.
2. Recontrôler main/SHA, blob cible, 80 IDs dans leur ordre, 70 fiches hors lot, inventaire et blob baseline liens. Arrêter en cas d'écart. Vérifier l'unicité globale des identités et URLs normalisées ; garder les aliases et sources historiques.
3. Obtenir l'autorisation explicite d'application canonique. Conserver review pour tout point non résolu ; ne rafraîchir verified_on qu'après vérification effective. Ne pas transformer les six propositions en validations automatiques.
4. Appliquer uniquement les champs approuvés, puis générer les pages officielles avec `python -m scripts.generate_docs` et `--check`. Comparer les dix fiches et les 70 autres ; les autres fiches doivent être inchangées, ainsi que schéma, taxonomy, overrides, workflows, dépendances et baseline liens.
5. Réexécuter installation dev, Ruff, format check, pytest, validate_catalog, review_debt, génération check et diff check ; relever les compteurs réels sans les prédire comme acquis. Une seconde revue des preuves et du patch doit précéder toute livraison externe.
6. Commit, push, PR, issues et workflows distants nécessitent une autorisation séparée. Aucune fusion, release, force-push, modification de baseline liens ni clôture de l'[issue #2](https://github.com/goozcena-gnl/devops-tools-catalog/issues/2) dans cette mission.

## 9. Modifications réellement appliquées et vérification finale

Un seul fichier de travail est créé : `docs/maintenance/2026-10-27-wave-28-ai-mcp-devops-evidence-review.md`. La création de branche est locale et n'ajoute aucun commit. Les caches du venv et des contrôles ne sont pas des livrables ; les fixtures de la relance finale sont placées hors du dépôt. Les résultats finaux et empreintes de préservation sont consignés après les contrôles terminés.

### Préservation et reproduction locale

Le contrôle de périmètre a asserté que HEAD et main valent encore le SHA de baseline, que le diff de tous les fichiers suivis contre ce SHA est vide et que le seul chemin non suivi est ce document. Comparaison des objets YAML : mêmes 80 fiches, même ordre, mêmes dix IDs en revue, mêmes 70 autres objets. Les blobs du YAML cible et de la baseline des liens restent ceux de la section 1. Une comparaison brute aux blobs Git diffère à cause de CRLF dans le checkout Windows et LF dans Git ; la comparaison après normalisation CRLF est identique pour les deux fichiers. Aucun de ces deux fichiers n'a été réécrit.

Pour reproduire les contrôles de catalogue depuis cette branche, utiliser le Python du venv. Les commandes ci-dessous ne valident aucune décision d'outil et ne génèrent aucun fichier canonique :

```powershell
$wave28Python = (Resolve-Path .venv/Scripts/python.exe).Path
& $wave28Python -m scripts.review_debt --format json
& $wave28Python -m scripts.validate_catalog
& $wave28Python -m scripts.generate_docs --check
& $wave28Python -m ruff check scripts tests
& $wave28Python -m ruff format --check scripts tests
& $wave28Python -m pip check
git diff --check
git status --short --untracked-files=all
git rev-parse main
git hash-object data/tools/mlops-llmops-ai-infrastructure.yaml
git hash-object config/link-audit-baseline.json
```

Placer les fixtures pytest **hors du dépôt** : le validateur Markdown parcourt même les sous-répertoires ignorés par Git. La relance finale a utilisé :

```powershell
& .venv/Scripts/python.exe -m pytest --basetemp=C:/Users/bgian/.codex/visualizations/2026/10/27/01a17aa8-d52d-79d2-8837-a078bd5889bb/wave28-pytest-b -o cache_dir=C:/Users/bgian/.codex/visualizations/2026/10/27/01a17aa8-d52d-79d2-8837-a078bd5889bb/wave28-pytest-cache-b -x
```

Pour une reproduction indépendante, choisir un nouveau répertoire temporaire hors dépôt autorisé en écriture ; pytest peut nettoyer son basetemp, il ne faut pas lui donner un répertoire contenant des fichiers à conserver.

### Résultats de clôture de cette passe

- **pytest final : 1 004 passed, 8 skipped, 428,75 secondes, code de sortie 0.** Les huit skips sont conservés ; aucun test n'a été retiré ni modifié. Les erreurs Windows et l'échec lié aux fixtures internes sont les tentatives antérieures décrites en section 7.
- **validate_catalog : PASS** sur le document ; **generate_docs --check : PASS** ; Ruff lint et format check : PASS ; pip check : PASS. Aucun outil de la cohorte n'a été exécuté et aucune décision n'a été appliquée.
- **review_debt / compteurs et périmètre : PASS** : 1 425 fiches, 816 actives, 595 needs-review, 77 unknown, 30 catégories ; cible 80/58 ; les dix fiches et les 70 autres restent identiques. Tous les fichiers suivis ont un diff vide contre la baseline.
- **git diff --check : PASS**. Le nouveau fichier, non suivi, fait en plus l'objet d'une comparaison no-index contre NUL avec --check : aucun diagnostic d'espacement. Pour cette comparaison d'un ajout, le code 1 de no-index indique la différence attendue avec le fichier vide.
- **Livrable unique : ce Markdown**, non committé. Aucun fichier canonique, généré, workflow, contrainte, dépendance déclarée, alias ou baseline de liens modifié. main et HEAD restent sur le SHA attendu ; la branche locale dédiée est sélectionnée.
- **Non exécutés :** Full/strict link audit, CI distante, tests d'intégration des outils, scan de vulnérabilités, vérification exhaustive des licences des binaires/modèles et examen des contrats privés Enterprise.

Les six CLEAR et quatre RETAIN REVIEW sont des propositions documentées. La prochaine étape est la revue humaine des décisions et la préparation des valeurs YAML exactes à soumettre à autorisation pour une seconde passe, en conservant les réserves non levées.

---

# Wave 28 — Independent second pass and frozen canonical change proposal

**Reviewed: 2026-10-28, Europe/Paris. Documentary changes only.**
**Independent outcome: 10 CLEAR / 0 RETAIN REVIEW proposals; 0 applied.**
The first-pass text above is historical and is preserved byte for byte. Where conclusions differ, this second-pass section governs the proposed future patch. CLEAR means the bounded catalogue description is adequately evidenced. It does not approve a production installation, confer commercial rights, certify a binary or model, or assert absence of vulnerabilities.

## 10. Baseline and preservation gate

| Check | Second-pass observation |
|---|---|
| Branch | maintenance/wave-28-ai-mcp-devops-evidence-review |
| HEAD and local main | 2cda6adb8c75d33dece85c4ec04e1b424bf5a38e |
| Remote main, read through GitHub API | Same SHA; no fetch or ref update |
| Target Git blob | 67b741277e52e51abb1f4e72c6b846b2edcdeb95 |
| Link-audit baseline blob | a834e2af711693def40078a55e31dfeb29bee2c7 |
| Canonical records / active / needs-review | 1,425 / 816 / 595 |
| Other statuses | archived 10, historical 2, deprecated 2 |
| Target file | 80 records, 58 requiring review |
| Selected cohort | All ten IDs exist once, with status needs-review and needs_review true |
| Initial working tree | No tracked changes; this existing first-pass report was the sole untracked path |
| First-pass prefix | 57,087 bytes; SHA-256 ad4fc5ae529d1695e868daddbe6af48a930d90411e92e3739270c7daa2c69863 |
| Global normalized repository URLs | No duplicates, using the repository's normalize_url function |
| Proposed microsoft/mcp repository | No collision with any existing repository_url |
| Historical issue 2 | Observed open; no mutation |

“Exactly the selected ten remain unresolved” is interpreted as a cohort constraint: the file actually has 58 unresolved records, as the first pass already recorded. The other 48 unresolved records and all 70 out-of-cohort records must stay untouched. If the phrase instead requires only ten unresolved records in the entire file, that expectation conflicts with the baseline; no bulk correction is authorized.

The untracked report is expected local work, not a clean-checkout discrepancy. No baseline exception was needed. All source files, schema, taxonomy, config, dependencies, generated pages, refs and ordering remain unchanged. The final verification below checks both raw preservation of the prefix and canonical equivalence to Git.

## 11. Independent evidence revalidation

The ten original release tags were independently resolved through GET /repos/{owner}/{repo}/commits/{tag}; every SHA matched the first-pass table. Licences and READMEs were fetched again from those immutable commits, not accepted from the first-pass conclusions. Repository metadata returned archived=false for all ten current repositories; Azure/azure-mcp returned archived=true and its pinned README explicitly names microsoft/mcp as successor.

Release lists were read on this review date. Azure was filtered by the Azure.Mcp.Server product and semantic prerelease suffix: the API still flags 4.0.0-beta.3 as prerelease=false, which does not make it stable. Docker returned 74 releases, all prerelease=true. For other repositories, five recent releases were inspected; no claim of exhaustive release-history coverage is made.

| Record | Revalidated version and pinned text | Licence scope | Operational boundary and independent verdict |
|---|---|---|---|
| azure-mcp-server | Azure.Mcp.Server-3.0.0, original pinned commit | MIT for server code | Migration verified; Entra authentication and RBAC do not remove mutation or data-disclosure risks. Local use must exclude production credentials/data. CLEAR. |
| kubernetes-mcp-server | v0.0.69, original pinned commit | Apache-2.0 for this containers project | TOML read_only and disable_destructive are different controls. Dedicated RBAC and HTTP caller authentication are needed. This is not an official Kubernetes/CNCF attribution. CLEAR. |
| terraform-mcp-server | v1.4.1, original pinned commit | MPL-2.0 for the MCP server | Registry is default; optional authenticated workflows can write. ENABLE_TF_OPERATIONS is not a universal read-only switch. CLEAR. |
| github-mcp-server | v2.0.3, original pinned commit | MIT for server code | Local and hosted paths differ; GHES requires local hosting. Lockdown is a content filter, not authorization. CLEAR. |
| grafana-mcp | v2.1.1, original pinned commit | Apache-2.0 for server code | Writes and raw SQL require separate attention; HTTP caller authentication is optional and distinct from Grafana credentials. CLEAR. |
| docker-mcp-gateway | v0.44.3, original pinned commit; all 74 releases prerelease | MIT for gateway implementation | Official manual Engine distribution and Desktop Toolkit exist; Toolkit is Beta. emerging plus explicit scope cautions is sufficient for catalogue CLEAR. |
| k8sgpt | v0.4.41, original pinned commit | Apache-2.0 for project code | Complete CLI log-to-provider path established statically; limited masking and optional analyzer defaults documented below. CLEAR with explicit warning. |
| litellm | New v1.106.5, 2569eb88694ce148dea5f324f240f79d256af8ae | MIT outside enterprise/; separate Enterprise terms | Root and Enterprise licence blobs are unchanged from v1.106.4. open-core retained; no product-wide SPDX. CLEAR for descriptive catalogue scope. |
| ollama | New v0.40.12, f067033f9126993b6172bdfffa71a74ad693fda4 | MIT runtime; weights/services separate | Licence and README blobs unchanged from v0.40.11. Local API has no auth; optional cloud means “zero cloud dependency” needs qualification. CLEAR. |
| open-webui | v0.12.4, original pinned commit; current main licence blob also checked | Custom current terms plus legacy BSD/MIT | source-available is the catalogue classification; no whole-product SPDX. Branding and executable extensions expressly bounded. CLEAR. |

Ollama v0.40.12 was published 2026-10-27 00:07:12 UTC. LiteLLM v1.106.5 was published 2026-10-27 19:58:45 UTC; v1.109.0-dev.1 is a prerelease, not the stable being reviewed. These update the evidence snapshot rather than changing any canonical version field: the schema contains no such field. The first-pass version observations remain historical.

The six original CLEAR proposals survive independent challenge because their identities, principal licences, maintained repositories, documented capabilities and important cautions are established. None is described as intrinsically safe, universally compatible, or licensed together with its external services. Mature production support is not inferred from an active repository or a release.

## 12. Resolution of the four formerly retained decisions

### 12.1 Docker MCP Gateway: CLEAR with maturity emerging

The pinned README identifies this repository as the implementation of the docker-mcp CLI plugin underlying Desktop's MCP Toolkit and explicitly supports independent use. Docker's official Gateway page directs Docker Engine users to install a GitHub release binary manually; it also says the Desktop Toolkit runs the gateway automatically. This independently establishes a supported documentation/distribution path despite the release labels. The official Toolkit page identifies availability as Beta and describes its UI for Desktop 4.62+, while the pinned gateway README gives a Desktop 4.59+ prerequisite. Those statements describe different documentation/version scopes and do not establish a Desktop-to-plugin version mapping.

No production-supported gateway version or GA/LTS commitment was found in the reviewed sources. AI Governance is an invite-only commercial context, not evidence that every OSS gateway release is a production-supported commercial distribution. Neither prerelease labels nor beta distribution imply abandonment.

MIT plainly covers the gateway implementation. Desktop, Governance, catalog entries, MCP servers, images and their dependencies have separate terms. The pinned security model describes HTTP Bearer authentication by default, scoped secrets, signing checks restricted to Docker's mcp namespace and container restrictions. It also explicitly says network egress is not globally denied by default. Opt-outs and granted mounts/permissions matter. These documented limitations are sufficient for accurate metadata with emerging maturity; they are not a reason to require a production support contract before listing the project as active.

**Disposition:** formerly retained release/support ambiguity is resolved by narrowing the claim. No GA or production guarantee is proposed. Unresolved Desktop/plugin mapping and private Governance terms remain deployment due diligence, not prerequisites of these exact metadata values.

### 12.2 K8sGPT: CLI logs-to-provider path and actual masking

All source links below use commit 3644ecfd4f932be3901838b35e250a95f7732114. This is static evidence, with no cluster access, synthetic secret transmission or live provider invocation.

1. pkg/analyzer/analyzer.go places Log in additionalAnalyzerMap, not coreAnalyzerMap. pkg/analysis/analysis.go RunAnalysis uses core analyzers when neither explicit filters nor persisted active_filters are selected. An explicit Log filter or persisted active Log filter can enable it. The CLI defaults --explain=false, --anonymize=false, an empty --filter list, --custom-analysis=false and --no-cache=false. README shorthand saying all filters run must not be read as enabling every additional analyzer.
2. pkg/analyzer/log.go LogAnalyzer.Analyze lists pods in the selected namespace scope and loops their regular containers. Despite the comment about non-running pods, no non-running field selector is imposed by this function. It requests the last 100 lines for the current container; if its status has RestartCount greater than zero, it also requests previous-instance logs. This is not evidence of collecting all historical logs or init-container logs.
3. analyzeLogs calls Pods(namespace).GetLogs(...).DoRaw(context). It tests case-insensitive error/exception/fail matches and printErrorLines returns the first matching line from each fetched current/previous log text. That whole line becomes Failure.Text; previous logs get a textual prefix. Log retrieval errors can instead produce a failure with the Kubernetes error message and pod name.
4. The log analyzer declares pod.Name in Failure.Sensitive and keys Result.Name as namespace/pod/container. executeAnalyzer appends results to Analysis.Results. cmd/analyze/analyze.go calls GetAIResults only for --explain.
5. GetAIResults merges analyzer-declared Sensitive pairs with resourceSensitive(Result.Name). Thus --anonymize also covers the nonempty namespace, pod and container segments, not only the pod name as the first-pass wording could imply. Pairs are deduplicated and ordered longest first; maskText substitutes literal matches with a trailing word boundary. util.MaskString generates random replacement text encoded as base64; this is pseudonym substitution, not general PII detection, encryption or secret removal. AI replies are subsequently unmasked locally.
6. Arbitrary credentials, email addresses, customer data, URLs, identifiers not in those mappings and the remaining message content are not generically removed from Failure.Text. Coincidental matches may replace text, but no complete sanitizer is established. CLI help still says anonymization does not apply to events; the actual shared code now masks result identity segments within failure text, so this help is not a complete description either.
7. getAIResultForSanitizedFailures joins the failure text, incorporates the prompt template and language, and checks a provider/language/input-dependent cache. A nonempty cache hit returns without a new AI call. On a miss it calls AIClient.GetCompletion(context, prompt). pkg/ai/openai.go sends prompt as message Content in CreateChatCompletion, with a configurable base URL. Therefore, with Log plus --explain, relevant RBAC, matching text and an external provider endpoint, sensitive text remaining in the line can leave the cluster. A local backend is a different destination choice. No claim is made that any user's logs actually left a cluster.
8. The privacy page's blanket statement that logs are not collected is inconsistent with this optional source path. The catalogue must use the pinned implementation and explicit conditional warning. The CLI path is proven here; operator, MCP/server defaults, custom analyzers and every provider are not extrapolated from it.

**Disposition:** CLEAR for the explicitly bounded description. The information required to warn users is now established. The upstream privacy/help discrepancy remains a P2 documentation issue, not an unresolved essential catalogue claim. Disabling Log does not itself guarantee all other analyzers or integrations are free of sensitive data.

### 12.3 LiteLLM: CLEAR as open-core, no whole-product SPDX

The root licence at both reviewed releases explicitly carves out enterprise/ and grants MIT to the remaining community code. The actual Enterprise text is enterprise/LICENSE.md, despite the root reference naming enterprise/LICENSE. Production use of Enterprise code requires applicable Subscription Terms or another agreement and a valid licence for the correct user seats. Development/testing permission and patch provisions are distinct from a general production or redistribution grant; no missing agreement is assumed accepted.

Official Enterprise documentation identifies commercial features such as SSO/SCIM, audit and delegated administration, and says a licence key enables them in the same Gateway image. A shared image is not a shared licence. Feature entitlement and artifact composition must be checked for a chosen deployment; a root MIT declaration or package classifier cannot establish whole-image MIT coverage. Self-hosting also does not prove providers or callbacks receive no data.

**Disposition:** open-core is accurate and remains unchanged. Add commercial_offering=true and explicit scope warnings. Leave license_spdx absent because the schema offers a single product-level field without a scope qualifier; writing MIT there would invite a misleading product-wide reading. Private commercial terms remain unreviewed, but the catalogue does not promise Enterprise usage rights or certify any selected artifact. Those absent contracts do not prevent this descriptive CLEAR.

### 12.4 Open WebUI: CLEAR as source-available, no global SPDX

The current main licence has the same blob as the pinned v0.12.4 text. The v0.6.5 licence was independently fetched and its tag resolved to 07d8460126a686de9a99e2662d06106e22c3f6b6: its licence is BSD-3-Clause. Official history retains still older MIT rights and BSD rights for code before the indicated transition commit. The official licence documentation dates the custom regime to v0.6.6, 2025-04-19. New terms do not retroactively eliminate the grants on historical code.

The current custom Open WebUI License adds branding conditions. Without an exception, licensees must preserve branding; it does not impose a blanket prohibition on commercial use. Branding alteration is excepted for at most 50 natural persons with direct application access in any rolling 30-day period, specific prior written permission, or an executed Enterprise licence expressly permitting it. The binding licence wording prevails over the web summary's ambiguous “50+” shorthand: 50 is within the numerical exception, and 51 is outside it. Written permission in the licence is not limited by a requirement inferred only from contributor marketing text. Users should not reset the limit per tenant/replica to evade an aggregate deployment obligation; any complex aggregation or redistribution scenario needs its own contract review.

BSD-3-Clause and MIT are OSI-approved licences. The custom current Open WebUI licence is not listed in the OSI approved-licence inventory reviewed; it must not inherit BSD's approval by similarity. source-available is the appropriate local catalogue classification for this restricted, mixed-history product. Neither BSD-3-Clause nor MIT alone describes the whole current product, and no invented SPDX or LicenseRef is proposed.

**Disposition:** the restrictions are documented well enough for CLEAR with source-available, commercial_offering=true, absent license_spdx and exact branding cautions. A particular rebranding rollout's user count, permission letter or Enterprise agreement is not approved here. Tools, Functions and Pipelines run Python with backend rights; the official security policy treats tool-creation permission as administrator-level trust.

## 13. Conflict checks, findings and risk register

Priorities identify catalogue defects or conditional adoption risks, not demonstrated vulnerabilities or legal determinations about a user's installation.

| ID / priority | Finding and consequence | Frozen resolution / residual boundary |
|---|---|---|
| P1-01, conditional adoption | MCP actions can modify cloud, cluster, source-control, workspace or monitoring resources with the effective identity. | Explicit least privilege, positive tool selection and mutation review. Terraform's operations gate is not universal read-only. No live exploit claimed. |
| P1-02, conditional adoption | Sensitive tool/log output can reach clients/providers; K8sGPT log text has a proven conditional outbound path. | K8sGPT defaults and incomplete masking described exactly; all data destinations, retention and credentials require deployment review. |
| P1-03, conditional adoption | Unauthenticated endpoints or executable extensions can expose privileged services. | Ollama's local API and Grafana's optional caller auth are explicitly called out; Open WebUI extensions require trusted administrator privileges. |
| P2-01, catalogue defect | Azure software is classified documentation and has no canonical repository. | Propose oss, MIT and microsoft/mcp; preserve historical identity and official URL. |
| P2-02, catalogue defect | Current Open WebUI is classified oss without its custom restriction. | Propose source-available, licence-scope summary and branding warning; leave SPDX absent. |
| P2-03, first-pass correction | K8sGPT wording understated shared identifier masking; privacy/help text is too broad or stale. | Trace the shared code, warn about arbitrary remaining log text and distinguish optional Log from default core analyzers. |
| P2-04, scope hazard | MIT could be misunderstood as covering LiteLLM Enterprise or all Ollama weights. | Omit LiteLLM product-wide SPDX; qualify runtime MIT for Ollama and separate model/provider terms. |
| P2-05, support ambiguity | Docker prerelease and Desktop Beta do not establish abandonment or production support. | emerging plus explicit beta/support limits; no fabricated stable version. |
| P2-06, catalogue defect | Ollama use_when promises zero cloud dependency without conditions. | Make offline artifacts and disabled cloud explicit; remove unsupported blanket enterprise-support exclusion. |
| P2-07, deployment drift | Defaults/toolsets, Grafana versions/plugins, cluster APIs and package channels can change. | Pinned source links and dated evidence; no universal compatibility or permanent support claim. |
| Info-01 | All 1,425 repository URLs normalized with the repository helper have zero collisions; proposed Azure URL has no existing owner. | No deduplication, ID changes, alias replacement or history deletion. |
| Info-02 | The target has 58 unresolved records, not ten total. | Only the selected ten may change after future authorization; 70 other records are immutable. |
| Info-03 | Existing K8sGPT avoid_when contains a replacement character. | Exact old value retained in the ledger as a JSON escape; full field replacement is explicit. |
| Info-04 | No runtime version/deployment taxonomy values are invented. | Preserve categories, roles, lifecycle_stages, deployment_models and ordering. No generic hosting claim that every tool is local-only. |

Terraform's pinned registry contains ordinary writes without RequiresTFOps. The create_run source has both restricted and broader variants: both default plan_and_apply to AutoApply=false, while the broader variant includes auto_approve and is_destroy. These source observations do not prove that all variants are registered in every configuration. The safe catalogue statement is that the gate is not a universal read-only policy and enabled run options/approval paths must be reviewed; it does not claim automatic applies are the default.

Grafana's README warns that non-loopback HTTP without a caller token starts with a security error log rather than refusing startup in this version; do not claim secure-by-default remote serving. --disable-write may be overridden for named tools or raw query tools, whose actual datasource permissions remain decisive. GitHub's lockdown does not change token authorization and some withheld content can still be reached through other tools. Kubernetes read-only annotations likewise do not make sensitive reads harmless.

## 14. Exact patch format and implementation boundary

The following ten YAML blocks are a **field-level preview only**, using id plus set. They are not replacement catalogue records and must never be pasted over the whole file. Each sources list is the complete proposed list, with all old legacy entries first and evidence URLs appended without duplicates. Unspecified fields remain exactly as currently stored. No remove operation is proposed.

For each changed field the ledger states the exact old and new values in JSON notation; decoding those JSON values gives the canonical YAML values. ABSENT means the key does not exist and is not a YAML null. Every evidence identifier links to its primary URL in section 15. High confidence means the primary text supports the stated claim; Medium means an explicit catalogue classification or cautious editorial judgement. “None” in the condition column means no unresolved essential evidence dependency for this exact value; every application still requires separate explicit authorization and a fresh baseline gate. A deployment approval is never implied.

The nine unknown maturity values remain unknown. Docker alone changes unknown to emerging because official Beta distribution and prerelease versioning support that cautious category. CLEAR is independent of that maturity choice; no record is promoted to established merely because it has a release.


### 14.1 azure-mcp-server - CLEAR

```yaml
id: azure-mcp-server
set:
  summary: Microsoft MCP server connecting AI agents to Azure services and resource operations; maintained in microsoft/mcp.
  repository_url: https://github.com/microsoft/mcp
  repository_archived: false
  documentation_url: https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/overview
  license_model: oss
  license_spdx: MIT
  status: active
  needs_review: false
  use_when:
  - You need MCP-assisted Azure discovery or operations with a dedicated least-privilege identity and an explicit
    tool allowlist.
  avoid_when:
  - Do not use a local Azure MCP server with production data or production credentials; Microsoft documents the
    local deployment for development use.
  - Avoid broad Azure roles, unreviewed mutations or untrusted endpoints; authenticate callers, validate tokens
    and TLS, and review tool outputs before sending them to a model.
  verified_on: '2026-10-28'
  sources:
  - legacy:9_AI-MLOps/README.md#L46
  - legacy:devopstools_final.md#L1215
  - https://github.com/microsoft/mcp/blob/61715e6a9054d7922809b01e08a2efa85e032a6d/LICENSE
  - https://github.com/microsoft/mcp/blob/61715e6a9054d7922809b01e08a2efa85e032a6d/servers/Azure.Mcp.Server/README.md
  - https://github.com/microsoft/mcp/releases/tag/Azure.Mcp.Server-3.0.0
  - https://api.github.com/repos/microsoft/mcp
  - https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/overview
  - https://github.com/Azure/azure-mcp/blob/54f04ab1ade20b4adc4955cffea0833788307596/README.md
  - https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security
```

| Field | Exact existing value | Exact proposed value | Primary evidence | Reason | Confidence | Unresolved condition |
|---|---|---|---|---|---|---|
| summary | `"Azure MCP server implementation."` | `"Microsoft MCP server connecting AI agents to Azure services and resource operations; maintained in microsoft/mcp."` | [AZURE-README], [AZURE-LIC] | Describe the demonstrated project and its licence or runtime scope without a safety guarantee. | High | None |
| repository_url | **ABSENT** | `"https://github.com/microsoft/mcp"` | [AZURE-MIG], [AZURE-README], [AZURE-META] | Use the explicit Azure successor repository, preserving the same catalogue identity. | High | None |
| repository_archived | **ABSENT** | `false` | [AZURE-META] | Record the current repository archive flag observed on the review date. | High | None |
| documentation_url | **ABSENT** | `"https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/overview"` | [AZURE-DOC], [AZURE-README] | Add the primary documentation entry or pinned project reference actually examined. | High | None |
| license_model | `"documentation"` | `"oss"` | [AZURE-LIC] | Classify software as oss rather than documentation. | High | None |
| license_spdx | **ABSENT** | `"MIT"` | [AZURE-LIC] | Identify the principal project-code licence; external services, third-party components and model weights are outside this grant. | High | None |
| status | `"needs-review"` | `"active"` | [AZURE-LIC], [AZURE-README], [AZURE-REL], [AZURE-DOC], [AZURE-SEC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | High | None |
| needs_review | `true` | `false` | [AZURE-LIC], [AZURE-README], [AZURE-REL], [AZURE-DOC], [AZURE-SEC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | High | None |
| use_when | `["You want AI tools to interact with Azure resources via the MCP standard."]` | `["You need MCP-assisted Azure discovery or operations with a dedicated least-privilege identity and an explicit tool allowlist."]` | [AZURE-README], [AZURE-DOC], [AZURE-LIC] | Describe an evidenced use case with minimum deployment and permission context. | High | None |
| avoid_when | `["You're not on Azure or your AI tooling doesn't support MCP."]` | `["Do not use a local Azure MCP server with production data or production credentials; Microsoft documents the local deployment for development use.", "Avoid broad Azure roles, unreviewed mutations or untrusted endpoints; authenticate callers, validate tokens and TLS, and review tool outputs before sending them to a model."]` | [AZURE-SEC], [AZURE-README], [AZURE-LIC] | Replace incomplete or opinion-based guidance with demonstrated security, data, licence and runtime limits. | High | None |
| verified_on | `"2026-08-03"` | `"2026-10-28"` | [AZURE-LIC], [AZURE-README], [AZURE-META] | Date of this actual primary-source revalidation, not a future application date. | High | None |
| sources | `["legacy:9_AI-MLOps/README.md#L46", "legacy:devopstools_final.md#L1215"]` | `["legacy:9_AI-MLOps/README.md#L46", "legacy:devopstools_final.md#L1215", "https://github.com/microsoft/mcp/blob/61715e6a9054d7922809b01e08a2efa85e032a6d/LICENSE", "https://github.com/microsoft/mcp/blob/61715e6a9054d7922809b01e08a2efa85e032a6d/servers/Azure.Mcp.Server/README.md", "https://github.com/microsoft/mcp/releases/tag/Azure.Mcp.Server-3.0.0", "https://api.github.com/repos/microsoft/mcp", "https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/overview", "https://github.com/Azure/azure-mcp/blob/54f04ab1ade20b4adc4955cffea0833788307596/README.md", "https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security"]` | [AZURE-LIC], [AZURE-README], [AZURE-REL], [AZURE-META], [AZURE-DOC], [AZURE-MIG], [AZURE-SEC] | Append reviewed primary evidence after all original legacy provenance; preserve source order and uniqueness. | High | None |

**Explicitly unchanged fields (exact values):**

```yaml
id: azure-mcp-server
name: Azure MCP Server
official_url: https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server
categories:
- mlops-llmops-ai-infrastructure
subcategories:
- Model Context Protocol (MCP) Servers
roles:
- cloud-engineer
- platform-engineer
- mlops-ai-infrastructure-engineer
lifecycle_stages:
- build
- deploy
- operate
deployment_models: []
maturity: unknown
alternatives: []
tags: []
```

### 14.2 kubernetes-mcp-server - CLEAR

```yaml
id: kubernetes-mcp-server
set:
  summary: Go-native MCP server for Kubernetes and OpenShift with direct API access, multi-cluster configuration
    and optional ecosystem toolsets.
  repository_archived: false
  documentation_url: https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/README.md
  license_spdx: Apache-2.0
  status: active
  needs_review: false
  use_when:
  - You need MCP-assisted Kubernetes or OpenShift diagnostics with scoped kubeconfigs or a dedicated ServiceAccount,
    minimal RBAC and reviewed tool selection.
  avoid_when:
  - Avoid cluster-admin credentials, unnecessary Secret or log access, unreviewed exec or resource mutations, and
    HTTP endpoints without caller authentication and network controls.
  - For the reviewed version, set TOML read_only = true when needed; disable_destructive is not equivalent to read-only,
    and tool filtering does not replace Kubernetes RBAC.
  verified_on: '2026-10-28'
  sources:
  - legacy:devopstools_final.md#L1221
  - https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/LICENSE
  - https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/README.md
  - https://github.com/containers/kubernetes-mcp-server/releases/tag/v0.0.69
  - https://api.github.com/repos/containers/kubernetes-mcp-server
  - https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/docs/configuration.md
  - https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/docs/getting-started-kubernetes.md
```

| Field | Exact existing value | Exact proposed value | Primary evidence | Reason | Confidence | Unresolved condition |
|---|---|---|---|---|---|---|
| summary | `"Go-native MCP server for Kubernetes and OpenShift with direct API server integration, multi-cluster support, Helm/Tekton toolsets, and no external CLI dependencies (Apache-2.0)."` | `"Go-native MCP server for Kubernetes and OpenShift with direct API access, multi-cluster configuration and optional ecosystem toolsets."` | [KUBERNETES-README], [KUBERNETES-LIC] | Describe the demonstrated project and its licence or runtime scope without a safety guarantee. | High | None |
| repository_archived | **ABSENT** | `false` | [KUBERNETES-META] | Record the current repository archive flag observed on the review date. | High | None |
| documentation_url | **ABSENT** | `"https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/README.md"` | [KUBERNETES-DOC], [KUBERNETES-README] | Add the primary documentation entry or pinned project reference actually examined. | High | None |
| license_spdx | **ABSENT** | `"Apache-2.0"` | [KUBERNETES-LIC] | Identify the principal project-code licence; external services, third-party components and model weights are outside this grant. | High | None |
| status | `"needs-review"` | `"active"` | [KUBERNETES-LIC], [KUBERNETES-README], [KUBERNETES-REL], [KUBERNETES-DOC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | High | None |
| needs_review | `true` | `false` | [KUBERNETES-LIC], [KUBERNETES-README], [KUBERNETES-REL], [KUBERNETES-DOC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | High | None |
| use_when | `[]` | `["You need MCP-assisted Kubernetes or OpenShift diagnostics with scoped kubeconfigs or a dedicated ServiceAccount, minimal RBAC and reviewed tool selection."]` | [KUBERNETES-README], [KUBERNETES-DOC], [KUBERNETES-LIC] | Describe an evidenced use case with minimum deployment and permission context. | High | None |
| avoid_when | `[]` | `["Avoid cluster-admin credentials, unnecessary Secret or log access, unreviewed exec or resource mutations, and HTTP endpoints without caller authentication and network controls.", "For the reviewed version, set TOML read_only = true when needed; disable_destructive is not equivalent to read-only, and tool filtering does not replace Kubernetes RBAC."]` | [KUBERNETES-CFG], [KUBERNETES-README], [KUBERNETES-LIC] | Replace incomplete or opinion-based guidance with demonstrated security, data, licence and runtime limits. | High | None |
| verified_on | `"2026-08-03"` | `"2026-10-28"` | [KUBERNETES-LIC], [KUBERNETES-README], [KUBERNETES-META] | Date of this actual primary-source revalidation, not a future application date. | High | None |
| sources | `["legacy:devopstools_final.md#L1221"]` | `["legacy:devopstools_final.md#L1221", "https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/LICENSE", "https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/README.md", "https://github.com/containers/kubernetes-mcp-server/releases/tag/v0.0.69", "https://api.github.com/repos/containers/kubernetes-mcp-server", "https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/docs/configuration.md", "https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/docs/getting-started-kubernetes.md"]` | [KUBERNETES-LIC], [KUBERNETES-README], [KUBERNETES-REL], [KUBERNETES-META], [KUBERNETES-DOC], [KUBERNETES-CFG], [KUBERNETES-RBAC] | Append reviewed primary evidence after all original legacy provenance; preserve source order and uniqueness. | High | None |

**Explicitly unchanged fields (exact values):**

```yaml
id: kubernetes-mcp-server
name: Kubernetes MCP Server
repository_url: https://github.com/containers/kubernetes-mcp-server
categories:
- mlops-llmops-ai-infrastructure
subcategories:
- Model Context Protocol (MCP) Servers
roles:
- cloud-engineer
- platform-engineer
- mlops-ai-infrastructure-engineer
lifecycle_stages:
- build
- deploy
- operate
deployment_models: []
license_model: oss
maturity: unknown
alternatives: []
tags: []
```

### 14.3 terraform-mcp-server - CLEAR

```yaml
id: terraform-mcp-server
set:
  summary: HashiCorp MCP server for Terraform Registry discovery and authenticated HCP Terraform/Terraform Enterprise
    workspace and run workflows.
  repository_archived: false
  documentation_url: https://developer.hashicorp.com/terraform/mcp-server/reference
  license_spdx: MPL-2.0
  status: active
  needs_review: false
  use_when:
  - You need Terraform Registry context or selected authenticated HCP Terraform/Terraform Enterprise workflows under
    existing plan, policy and approval controls.
  avoid_when:
  - 'Do not treat ENABLE_TF_OPERATIONS=false as a read-only policy: selected workspace, variable and other writes
    remain available; allowlist tools and scope HCP/TFE tokens.'
  - Review run options, workspace policies and approval paths before enabling run workflows; plans, logs, variables
    and state may expose sensitive data to clients or models.
  - Do not assume generic local Terraform CLI plan/apply support or that the server's MPL-2.0 license covers Terraform,
    providers or hosted services.
  verified_on: '2026-10-28'
  sources:
  - legacy:devopstools_final.md#L1226
  - https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/LICENSE
  - https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/README.md
  - https://github.com/hashicorp/terraform-mcp-server/releases/tag/v1.4.1
  - https://api.github.com/repos/hashicorp/terraform-mcp-server
  - https://developer.hashicorp.com/terraform/mcp-server/reference
  - https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/pkg/toolsets/registry.go
  - https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/pkg/tools/tfe/create_run.go
  - https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/pkg/toolsets/filter.go
```

| Field | Exact existing value | Exact proposed value | Primary evidence | Reason | Confidence | Unresolved condition |
|---|---|---|---|---|---|---|
| summary | `"MCP server for Terraform automation and infrastructure-as-code workflows."` | `"HashiCorp MCP server for Terraform Registry discovery and authenticated HCP Terraform/Terraform Enterprise workspace and run workflows."` | [TERRAFORM-README], [TERRAFORM-LIC] | Describe the demonstrated project and its licence or runtime scope without a safety guarantee. | High | None |
| repository_archived | **ABSENT** | `false` | [TERRAFORM-META] | Record the current repository archive flag observed on the review date. | High | None |
| documentation_url | **ABSENT** | `"https://developer.hashicorp.com/terraform/mcp-server/reference"` | [TERRAFORM-DOC], [TERRAFORM-README] | Add the primary documentation entry or pinned project reference actually examined. | High | None |
| license_spdx | **ABSENT** | `"MPL-2.0"` | [TERRAFORM-LIC] | Identify the principal project-code licence; external services, third-party components and model weights are outside this grant. | High | None |
| status | `"needs-review"` | `"active"` | [TERRAFORM-LIC], [TERRAFORM-README], [TERRAFORM-REL], [TERRAFORM-DOC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | High | None |
| needs_review | `true` | `false` | [TERRAFORM-LIC], [TERRAFORM-README], [TERRAFORM-REL], [TERRAFORM-DOC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | High | None |
| use_when | `[]` | `["You need Terraform Registry context or selected authenticated HCP Terraform/Terraform Enterprise workflows under existing plan, policy and approval controls."]` | [TERRAFORM-README], [TERRAFORM-DOC], [TERRAFORM-LIC] | Describe an evidenced use case with minimum deployment and permission context. | High | None |
| avoid_when | `[]` | `["Do not treat ENABLE_TF_OPERATIONS=false as a read-only policy: selected workspace, variable and other writes remain available; allowlist tools and scope HCP/TFE tokens.", "Review run options, workspace policies and approval paths before enabling run workflows; plans, logs, variables and state may expose sensitive data to clients or models.", "Do not assume generic local Terraform CLI plan/apply support or that the server's MPL-2.0 license covers Terraform, providers or hosted services."]` | [TERRAFORM-REG], [TERRAFORM-RUN], [TERRAFORM-README], [TERRAFORM-LIC] | Replace incomplete or opinion-based guidance with demonstrated security, data, licence and runtime limits. | High | None |
| verified_on | `"2026-08-03"` | `"2026-10-28"` | [TERRAFORM-LIC], [TERRAFORM-README], [TERRAFORM-META] | Date of this actual primary-source revalidation, not a future application date. | High | None |
| sources | `["legacy:devopstools_final.md#L1226"]` | `["legacy:devopstools_final.md#L1226", "https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/LICENSE", "https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/README.md", "https://github.com/hashicorp/terraform-mcp-server/releases/tag/v1.4.1", "https://api.github.com/repos/hashicorp/terraform-mcp-server", "https://developer.hashicorp.com/terraform/mcp-server/reference", "https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/pkg/toolsets/registry.go", "https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/pkg/tools/tfe/create_run.go", "https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/pkg/toolsets/filter.go"]` | [TERRAFORM-LIC], [TERRAFORM-README], [TERRAFORM-REL], [TERRAFORM-META], [TERRAFORM-DOC], [TERRAFORM-REG], [TERRAFORM-RUN], [TERRAFORM-FILTER] | Append reviewed primary evidence after all original legacy provenance; preserve source order and uniqueness. | High | None |

**Explicitly unchanged fields (exact values):**

```yaml
id: terraform-mcp-server
name: Terraform MCP Server
repository_url: https://github.com/hashicorp/terraform-mcp-server
categories:
- mlops-llmops-ai-infrastructure
subcategories:
- Model Context Protocol (MCP) Servers
roles:
- cloud-engineer
- platform-engineer
- mlops-ai-infrastructure-engineer
lifecycle_stages:
- build
- deploy
- operate
deployment_models: []
license_model: oss
maturity: unknown
alternatives: []
tags: []
```

### 14.4 github-mcp-server - CLEAR

```yaml
id: github-mcp-server
set:
  summary: Official GitHub MCP server exposing repository, issue and pull-request operations through local or GitHub-hosted
    connections.
  repository_archived: false
  documentation_url: https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/README.md
  license_spdx: MIT
  status: active
  needs_review: false
  use_when:
  - You need AI-assisted GitHub repository exploration, issue triage or pull-request work with narrowly scoped credentials
    and reviewed tool permissions.
  avoid_when:
  - Avoid broad tokens or unreviewed repository, workflow and issue mutations; treat repository content and tool
    results as untrusted model inputs.
  - Read-only mode and tool allowlists reduce the exposed tool surface; lockdown is a best-effort content filter,
    not an authorization boundary or a prompt-injection guarantee.
  - Verify the deployment path for GitHub Enterprise Server; the GitHub-hosted remote server is not available for
    GHES.
  verified_on: '2026-10-28'
  sources:
  - legacy:9_AI-MLOps/README.md#L50
  - legacy:devopstools_final.md#L1218
  - https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/LICENSE
  - https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/README.md
  - https://github.com/github/github-mcp-server/releases/tag/v2.0.3
  - https://api.github.com/repos/github/github-mcp-server
  - https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/docs/server-configuration.md
```

| Field | Exact existing value | Exact proposed value | Primary evidence | Reason | Confidence | Unresolved condition |
|---|---|---|---|---|---|---|
| summary | `"GitHub's MCP server implementation."` | `"Official GitHub MCP server exposing repository, issue and pull-request operations through local or GitHub-hosted connections."` | [GITHUB-README], [GITHUB-LIC] | Describe the demonstrated project and its licence or runtime scope without a safety guarantee. | High | None |
| repository_archived | **ABSENT** | `false` | [GITHUB-META] | Record the current repository archive flag observed on the review date. | High | None |
| documentation_url | **ABSENT** | `"https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/README.md"` | [GITHUB-DOC], [GITHUB-README] | Add the primary documentation entry or pinned project reference actually examined. | High | None |
| license_spdx | **ABSENT** | `"MIT"` | [GITHUB-LIC] | Identify the principal project-code licence; external services, third-party components and model weights are outside this grant. | High | None |
| status | `"needs-review"` | `"active"` | [GITHUB-LIC], [GITHUB-README], [GITHUB-REL], [GITHUB-DOC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | High | None |
| needs_review | `true` | `false` | [GITHUB-LIC], [GITHUB-README], [GITHUB-REL], [GITHUB-DOC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | High | None |
| use_when | `["You want AI assistants to read/write GitHub repos, issues, and PRs via MCP."]` | `["You need AI-assisted GitHub repository exploration, issue triage or pull-request work with narrowly scoped credentials and reviewed tool permissions."]` | [GITHUB-README], [GITHUB-DOC], [GITHUB-LIC] | Describe an evidenced use case with minimum deployment and permission context. | High | None |
| avoid_when | `["You use GitLab/Bitbucket or don't need AI-driven GitHub interactions."]` | `["Avoid broad tokens or unreviewed repository, workflow and issue mutations; treat repository content and tool results as untrusted model inputs.", "Read-only mode and tool allowlists reduce the exposed tool surface; lockdown is a best-effort content filter, not an authorization boundary or a prompt-injection guarantee.", "Verify the deployment path for GitHub Enterprise Server; the GitHub-hosted remote server is not available for GHES."]` | [GITHUB-CFG], [GITHUB-README], [GITHUB-LIC] | Replace incomplete or opinion-based guidance with demonstrated security, data, licence and runtime limits. | High | None |
| verified_on | `"2026-08-03"` | `"2026-10-28"` | [GITHUB-LIC], [GITHUB-README], [GITHUB-META] | Date of this actual primary-source revalidation, not a future application date. | High | None |
| sources | `["legacy:9_AI-MLOps/README.md#L50", "legacy:devopstools_final.md#L1218"]` | `["legacy:9_AI-MLOps/README.md#L50", "legacy:devopstools_final.md#L1218", "https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/LICENSE", "https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/README.md", "https://github.com/github/github-mcp-server/releases/tag/v2.0.3", "https://api.github.com/repos/github/github-mcp-server", "https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/docs/server-configuration.md"]` | [GITHUB-LIC], [GITHUB-README], [GITHUB-REL], [GITHUB-META], [GITHUB-DOC], [GITHUB-CFG] | Append reviewed primary evidence after all original legacy provenance; preserve source order and uniqueness. | High | None |

**Explicitly unchanged fields (exact values):**

```yaml
id: github-mcp-server
name: GitHub MCP Server
repository_url: https://github.com/github/github-mcp-server
categories:
- mlops-llmops-ai-infrastructure
subcategories:
- Model Context Protocol (MCP) Servers
roles:
- cloud-engineer
- platform-engineer
- mlops-ai-infrastructure-engineer
lifecycle_stages:
- build
- deploy
- operate
deployment_models: []
license_model: oss
maturity: unknown
alternatives: []
tags: []
```

### 14.5 grafana-mcp - CLEAR

```yaml
id: grafana-mcp
set:
  summary: MCP server for Grafana observability queries and permission-controlled dashboard and alerting operations.
  repository_archived: false
  documentation_url: https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/README.md
  license_spdx: Apache-2.0
  status: active
  needs_review: false
  use_when:
  - You need AI-assisted Grafana investigation or reviewed dashboard and alerting changes with scoped service-account
    and datasource permissions.
  avoid_when:
  - Avoid exposing HTTP transports without caller authentication and TLS or granting broader Grafana and datasource
    permissions than the selected tools need.
  - Do not treat --disable-write as sufficient when --enable-query or --enable-write-tools restores tools; raw SQL
    can mutate a datasource if its credentials allow it.
  - Review logs and dashboards for sensitive data, query costs, and each tool's Grafana version and plugin requirements.
  verified_on: '2026-10-28'
  sources:
  - legacy:9_AI-MLOps/README.md#L54
  - legacy:devopstools_final.md#L1220
  - https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/LICENSE
  - https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/README.md
  - https://github.com/grafana/mcp-grafana/releases/tag/v2.1.1
  - https://api.github.com/repos/grafana/mcp-grafana
```

| Field | Exact existing value | Exact proposed value | Primary evidence | Reason | Confidence | Unresolved condition |
|---|---|---|---|---|---|---|
| summary | `"Model Context Protocol for Grafana."` | `"MCP server for Grafana observability queries and permission-controlled dashboard and alerting operations."` | [GRAFANA-README], [GRAFANA-LIC] | Describe the demonstrated project and its licence or runtime scope without a safety guarantee. | High | None |
| repository_archived | **ABSENT** | `false` | [GRAFANA-META] | Record the current repository archive flag observed on the review date. | High | None |
| documentation_url | **ABSENT** | `"https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/README.md"` | [GRAFANA-DOC], [GRAFANA-README] | Add the primary documentation entry or pinned project reference actually examined. | High | None |
| license_spdx | **ABSENT** | `"Apache-2.0"` | [GRAFANA-LIC] | Identify the principal project-code licence; external services, third-party components and model weights are outside this grant. | High | None |
| status | `"needs-review"` | `"active"` | [GRAFANA-LIC], [GRAFANA-README], [GRAFANA-REL], [GRAFANA-DOC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | High | None |
| needs_review | `true` | `false` | [GRAFANA-LIC], [GRAFANA-README], [GRAFANA-REL], [GRAFANA-DOC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | High | None |
| use_when | `["You want AI assistants to query dashboards, alerts, and data sources in Grafana."]` | `["You need AI-assisted Grafana investigation or reviewed dashboard and alerting changes with scoped service-account and datasource permissions."]` | [GRAFANA-README], [GRAFANA-DOC], [GRAFANA-LIC] | Describe an evidenced use case with minimum deployment and permission context. | High | None |
| avoid_when | `["You don't use Grafana or prefer direct API integrations over MCP."]` | `["Avoid exposing HTTP transports without caller authentication and TLS or granting broader Grafana and datasource permissions than the selected tools need.", "Do not treat --disable-write as sufficient when --enable-query or --enable-write-tools restores tools; raw SQL can mutate a datasource if its credentials allow it.", "Review logs and dashboards for sensitive data, query costs, and each tool's Grafana version and plugin requirements."]` | [GRAFANA-README], [GRAFANA-LIC] | Replace incomplete or opinion-based guidance with demonstrated security, data, licence and runtime limits. | High | None |
| verified_on | `"2026-08-03"` | `"2026-10-28"` | [GRAFANA-LIC], [GRAFANA-README], [GRAFANA-META] | Date of this actual primary-source revalidation, not a future application date. | High | None |
| sources | `["legacy:9_AI-MLOps/README.md#L54", "legacy:devopstools_final.md#L1220"]` | `["legacy:9_AI-MLOps/README.md#L54", "legacy:devopstools_final.md#L1220", "https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/LICENSE", "https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/README.md", "https://github.com/grafana/mcp-grafana/releases/tag/v2.1.1", "https://api.github.com/repos/grafana/mcp-grafana"]` | [GRAFANA-LIC], [GRAFANA-README], [GRAFANA-REL], [GRAFANA-META], [GRAFANA-DOC] | Append reviewed primary evidence after all original legacy provenance; preserve source order and uniqueness. | High | None |

**Explicitly unchanged fields (exact values):**

```yaml
id: grafana-mcp
name: Grafana MCP
repository_url: https://github.com/grafana/mcp-grafana
categories:
- mlops-llmops-ai-infrastructure
subcategories:
- Model Context Protocol (MCP) Servers
roles:
- cloud-engineer
- platform-engineer
- mlops-ai-infrastructure-engineer
lifecycle_stages:
- build
- deploy
- operate
deployment_models: []
license_model: oss
maturity: unknown
alternatives: []
tags: []
```

### 14.6 docker-mcp-gateway - CLEAR

```yaml
id: docker-mcp-gateway
set:
  repository_archived: false
  documentation_url: https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/
  license_spdx: MIT
  maturity: emerging
  status: active
  needs_review: false
  use_when:
  - You need a Docker CLI gateway to manage containerized MCP servers, profiles, credentials and routing, and can
    accept an emerging release channel.
  avoid_when:
  - The reviewed GitHub releases are prereleases and Docker Desktop's MCP Toolkit is documented as Beta; no production-supported
    gateway version or Desktop-to-plugin version mapping is established here.
  - MIT covers the gateway implementation, not Docker Desktop, AI Governance, catalog servers or third-party images;
    check their separate terms.
  - 'Container isolation and secret scanning do not guarantee confidentiality: review mounts, Docker daemon access,
    allowed servers, secrets and network egress, which is not globally denied by default.'
  verified_on: '2026-10-28'
  sources:
  - legacy:devopstools_final.md#L1217
  - https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/LICENSE
  - https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/README.md
  - https://github.com/docker/mcp-gateway/releases/tag/v0.44.3
  - https://api.github.com/repos/docker/mcp-gateway
  - https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/
  - https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/docs/security.md
  - https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/docs/mcp-gateway.md
  - https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/
```

| Field | Exact existing value | Exact proposed value | Primary evidence | Reason | Confidence | Unresolved condition |
|---|---|---|---|---|---|---|
| repository_archived | **ABSENT** | `false` | [DOCKER-META] | Record the current repository archive flag observed on the review date. | High | None |
| documentation_url | **ABSENT** | `"https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/"` | [DOCKER-DOC], [DOCKER-README] | Add the primary documentation entry or pinned project reference actually examined. | High | None |
| license_spdx | **ABSENT** | `"MIT"` | [DOCKER-LIC] | Identify the principal project-code licence; external services, third-party components and model weights are outside this grant. | High | None |
| maturity | `"unknown"` | `"emerging"` | [DOCKER-REL], [DOCKER-TOOLKIT], [DOCKER-README] | Use a cautious maturity category consistent with documented Beta and prerelease distribution; no production support claim. | Medium | None |
| status | `"needs-review"` | `"active"` | [DOCKER-LIC], [DOCKER-README], [DOCKER-REL], [DOCKER-DOC], [DOCKER-SEC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | Medium | None |
| needs_review | `true` | `false` | [DOCKER-LIC], [DOCKER-README], [DOCKER-REL], [DOCKER-DOC], [DOCKER-SEC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | Medium | None |
| use_when | `[]` | `["You need a Docker CLI gateway to manage containerized MCP servers, profiles, credentials and routing, and can accept an emerging release channel."]` | [DOCKER-README], [DOCKER-DOC], [DOCKER-LIC] | Describe an evidenced use case with minimum deployment and permission context. | High | None |
| avoid_when | `[]` | `["The reviewed GitHub releases are prereleases and Docker Desktop's MCP Toolkit is documented as Beta; no production-supported gateway version or Desktop-to-plugin version mapping is established here.", "MIT covers the gateway implementation, not Docker Desktop, AI Governance, catalog servers or third-party images; check their separate terms.", "Container isolation and secret scanning do not guarantee confidentiality: review mounts, Docker daemon access, allowed servers, secrets and network egress, which is not globally denied by default."]` | [DOCKER-SEC], [DOCKER-TOOLKIT], [DOCKER-README], [DOCKER-LIC] | Replace incomplete or opinion-based guidance with demonstrated security, data, licence and runtime limits. | High | None |
| verified_on | `"2026-08-03"` | `"2026-10-28"` | [DOCKER-LIC], [DOCKER-README], [DOCKER-META] | Date of this actual primary-source revalidation, not a future application date. | High | None |
| sources | `["legacy:devopstools_final.md#L1217"]` | `["legacy:devopstools_final.md#L1217", "https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/LICENSE", "https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/README.md", "https://github.com/docker/mcp-gateway/releases/tag/v0.44.3", "https://api.github.com/repos/docker/mcp-gateway", "https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/", "https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/docs/security.md", "https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/docs/mcp-gateway.md", "https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/"]` | [DOCKER-LIC], [DOCKER-README], [DOCKER-REL], [DOCKER-META], [DOCKER-DOC], [DOCKER-SEC], [DOCKER-GUIDE], [DOCKER-TOOLKIT] | Append reviewed primary evidence after all original legacy provenance; preserve source order and uniqueness. | High | None |

**Explicitly unchanged fields (exact values):**

```yaml
id: docker-mcp-gateway
name: Docker MCP Gateway
summary: Docker CLI plugin and gateway for discovering, running, and routing MCP servers in containers.
repository_url: https://github.com/docker/mcp-gateway
categories:
- mlops-llmops-ai-infrastructure
subcategories:
- Model Context Protocol (MCP) Servers
roles:
- cloud-engineer
- platform-engineer
- mlops-ai-infrastructure-engineer
lifecycle_stages:
- build
- deploy
- operate
deployment_models: []
license_model: oss
alternatives: []
tags: []
```

### 14.7 k8sgpt - CLEAR

```yaml
id: k8sgpt
set:
  summary: Kubernetes analyzers for diagnostic triage with optional explanations from a configured AI backend.
  repository_archived: false
  documentation_url: https://docs.k8sgpt.ai/
  license_spdx: Apache-2.0
  status: active
  needs_review: false
  use_when:
  - You need Kubernetes diagnostic triage and can approve the analyzers, AI backend, data destinations and cache
    policy before requesting explanations.
  avoid_when:
  - When the optional Log analyzer and --explain are enabled, a matching log line can be sent to the configured
    AI backend on a cache miss; secrets in that text are not generically scrubbed by --anonymize.
  - In the reviewed CLI version, Log is not a default core analyzer and --explain and --anonymize default to false;
    configured active filters can change the analyzer selection.
  - Do not rely on the privacy page's blanket no-logs statement; scope pod/log RBAC and approve external data transfer,
    cache retention and human review of AI advice.
  verified_on: '2026-10-28'
  sources:
  - legacy:9_AI-MLOps/README.md#L28
  - legacy:devopstools_final.md#L1202
  - https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/LICENSE
  - https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/README.md
  - https://github.com/k8sgpt-ai/k8sgpt/releases/tag/v0.4.41
  - https://api.github.com/repos/k8sgpt-ai/k8sgpt
  - https://docs.k8sgpt.ai/
  - https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/analyzer/log.go
  - https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/analyzer/analyzer.go
  - https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/analysis/analysis.go
  - https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/cmd/analyze/analyze.go
  - https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/ai/openai.go
  - https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/util/util.go
  - https://docs.k8sgpt.ai/reference/guidelines/privacy/
```

| Field | Exact existing value | Exact proposed value | Primary evidence | Reason | Confidence | Unresolved condition |
|---|---|---|---|---|---|---|
| summary | `"AI-powered Kubernetes troubleshooting."` | `"Kubernetes analyzers for diagnostic triage with optional explanations from a configured AI backend."` | [K8SGPT-README], [K8SGPT-LIC] | Describe the demonstrated project and its licence or runtime scope without a safety guarantee. | High | None |
| repository_archived | **ABSENT** | `false` | [K8SGPT-META] | Record the current repository archive flag observed on the review date. | High | None |
| documentation_url | **ABSENT** | `"https://docs.k8sgpt.ai/"` | [K8SGPT-DOC], [K8SGPT-README] | Add the primary documentation entry or pinned project reference actually examined. | High | None |
| license_spdx | **ABSENT** | `"Apache-2.0"` | [K8SGPT-LIC] | Identify the principal project-code licence; external services, third-party components and model weights are outside this grant. | High | None |
| status | `"needs-review"` | `"active"` | [K8SGPT-LIC], [K8SGPT-README], [K8SGPT-REL], [K8SGPT-DOC], [K8SGPT-ANALYSIS] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | High | None |
| needs_review | `true` | `false` | [K8SGPT-LIC], [K8SGPT-README], [K8SGPT-REL], [K8SGPT-DOC], [K8SGPT-ANALYSIS] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | High | None |
| use_when | `["You want natural-language diagnostics for Kubernetes cluster issues."]` | `["You need Kubernetes diagnostic triage and can approve the analyzers, AI backend, data destinations and cache policy before requesting explanations."]` | [K8SGPT-README], [K8SGPT-DOC], [K8SGPT-LIC] | Describe an evidenced use case with minimum deployment and permission context. | High | None |
| avoid_when | `["Your team already has strong K8s expertise and established runbooks\u2014AI triage adds little value."]` | `["When the optional Log analyzer and --explain are enabled, a matching log line can be sent to the configured AI backend on a cache miss; secrets in that text are not generically scrubbed by --anonymize.", "In the reviewed CLI version, Log is not a default core analyzer and --explain and --anonymize default to false; configured active filters can change the analyzer selection.", "Do not rely on the privacy page's blanket no-logs statement; scope pod/log RBAC and approve external data transfer, cache retention and human review of AI advice."]` | [K8SGPT-ANALYSIS], [K8SGPT-LOG], [K8SGPT-MAP], [K8SGPT-CLI], [K8SGPT-PROVIDER], [K8SGPT-PRIVACY], [K8SGPT-README], [K8SGPT-LIC] | Replace incomplete or opinion-based guidance with demonstrated security, data, licence and runtime limits. | High | None |
| verified_on | `"2026-08-03"` | `"2026-10-28"` | [K8SGPT-LIC], [K8SGPT-README], [K8SGPT-META] | Date of this actual primary-source revalidation, not a future application date. | High | None |
| sources | `["legacy:9_AI-MLOps/README.md#L28", "legacy:devopstools_final.md#L1202"]` | `["legacy:9_AI-MLOps/README.md#L28", "legacy:devopstools_final.md#L1202", "https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/LICENSE", "https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/README.md", "https://github.com/k8sgpt-ai/k8sgpt/releases/tag/v0.4.41", "https://api.github.com/repos/k8sgpt-ai/k8sgpt", "https://docs.k8sgpt.ai/", "https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/analyzer/log.go", "https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/analyzer/analyzer.go", "https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/analysis/analysis.go", "https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/cmd/analyze/analyze.go", "https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/ai/openai.go", "https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/util/util.go", "https://docs.k8sgpt.ai/reference/guidelines/privacy/"]` | [K8SGPT-LIC], [K8SGPT-README], [K8SGPT-REL], [K8SGPT-META], [K8SGPT-DOC], [K8SGPT-LOG], [K8SGPT-MAP], [K8SGPT-ANALYSIS], [K8SGPT-CLI], [K8SGPT-PROVIDER], [K8SGPT-MASK], [K8SGPT-PRIVACY] | Append reviewed primary evidence after all original legacy provenance; preserve source order and uniqueness. | High | None |

**Explicitly unchanged fields (exact values):**

```yaml
id: k8sgpt
name: K8sGPT
official_url: https://k8sgpt.ai
repository_url: https://github.com/k8sgpt-ai/k8sgpt
categories:
- mlops-llmops-ai-infrastructure
subcategories:
- AI Ops & AI Tooling for DevOps
roles:
- cloud-engineer
- platform-engineer
- mlops-ai-infrastructure-engineer
lifecycle_stages:
- build
- deploy
- operate
deployment_models: []
license_model: oss
maturity: unknown
alternatives: []
tags: []
```

### 14.8 litellm - CLEAR

```yaml
id: litellm
set:
  summary: LLM SDK and gateway with an MIT-licensed community core and separately licensed Enterprise components;
    MIT does not cover the whole product.
  repository_archived: false
  documentation_url: https://docs.litellm.ai/
  commercial_offering: true
  status: active
  needs_review: false
  use_when:
  - You need a multi-provider LLM SDK or gateway with routing, virtual keys, budgets and spend tracking, and can
    separately review Enterprise features and provider terms.
  avoid_when:
  - MIT applies to community code outside enterprise/; Enterprise production use requires the applicable agreement
    and a valid license for the required seats, and is not authorized by this catalog entry.
  - The product can ship community and Enterprise functionality in the same image; inspect the selected artifact
    and enabled features before commercial deployment or redistribution.
  - Self-hosting does not prevent configured providers or logging callbacks from receiving prompts and responses;
    protect provider and master keys, tenant boundaries, retention and budgets.
  verified_on: '2026-10-28'
  sources:
  - legacy:devopstools_final.md#L1194
  - https://github.com/BerriAI/litellm/blob/2569eb88694ce148dea5f324f240f79d256af8ae/LICENSE
  - https://github.com/BerriAI/litellm/blob/2569eb88694ce148dea5f324f240f79d256af8ae/README.md
  - https://github.com/BerriAI/litellm/releases/tag/v1.106.5
  - https://api.github.com/repos/BerriAI/litellm
  - https://docs.litellm.ai/
  - https://github.com/BerriAI/litellm/blob/2569eb88694ce148dea5f324f240f79d256af8ae/enterprise/LICENSE.md
  - https://docs.litellm.ai/docs/enterprise
```

| Field | Exact existing value | Exact proposed value | Primary evidence | Reason | Confidence | Unresolved condition |
|---|---|---|---|---|---|---|
| summary | `"Gateway and proxy for 100+ LLM providers with budgets, rate limiting, logging, and spend tracking."` | `"LLM SDK and gateway with an MIT-licensed community core and separately licensed Enterprise components; MIT does not cover the whole product."` | [LITELLM-README], [LITELLM-LIC] | Describe the demonstrated project and its licence or runtime scope without a safety guarantee. | High | None |
| repository_archived | **ABSENT** | `false` | [LITELLM-META] | Record the current repository archive flag observed on the review date. | High | None |
| documentation_url | **ABSENT** | `"https://docs.litellm.ai/"` | [LITELLM-DOC], [LITELLM-README] | Add the primary documentation entry or pinned project reference actually examined. | High | None |
| commercial_offering | **ABSENT** | `true` | [LITELLM-ENT], [LITELLM-COMMERCIAL], [LITELLM-LIC] | The vendor documents a separately contracted Enterprise offering; no entitlement is granted. | High | None |
| status | `"needs-review"` | `"active"` | [LITELLM-LIC], [LITELLM-README], [LITELLM-REL], [LITELLM-DOC], [LITELLM-ENT] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | Medium | None |
| needs_review | `true` | `false` | [LITELLM-LIC], [LITELLM-README], [LITELLM-REL], [LITELLM-DOC], [LITELLM-ENT] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | Medium | None |
| use_when | `[]` | `["You need a multi-provider LLM SDK or gateway with routing, virtual keys, budgets and spend tracking, and can separately review Enterprise features and provider terms."]` | [LITELLM-README], [LITELLM-DOC], [LITELLM-LIC] | Describe an evidenced use case with minimum deployment and permission context. | High | None |
| avoid_when | `[]` | `["MIT applies to community code outside enterprise/; Enterprise production use requires the applicable agreement and a valid license for the required seats, and is not authorized by this catalog entry.", "The product can ship community and Enterprise functionality in the same image; inspect the selected artifact and enabled features before commercial deployment or redistribution.", "Self-hosting does not prevent configured providers or logging callbacks from receiving prompts and responses; protect provider and master keys, tenant boundaries, retention and budgets."]` | [LITELLM-ENT], [LITELLM-COMMERCIAL], [LITELLM-README], [LITELLM-LIC] | Replace incomplete or opinion-based guidance with demonstrated security, data, licence and runtime limits. | High | None |
| verified_on | `"2026-08-03"` | `"2026-10-28"` | [LITELLM-LIC], [LITELLM-README], [LITELLM-META] | Date of this actual primary-source revalidation, not a future application date. | High | None |
| sources | `["legacy:devopstools_final.md#L1194"]` | `["legacy:devopstools_final.md#L1194", "https://github.com/BerriAI/litellm/blob/2569eb88694ce148dea5f324f240f79d256af8ae/LICENSE", "https://github.com/BerriAI/litellm/blob/2569eb88694ce148dea5f324f240f79d256af8ae/README.md", "https://github.com/BerriAI/litellm/releases/tag/v1.106.5", "https://api.github.com/repos/BerriAI/litellm", "https://docs.litellm.ai/", "https://github.com/BerriAI/litellm/blob/2569eb88694ce148dea5f324f240f79d256af8ae/enterprise/LICENSE.md", "https://docs.litellm.ai/docs/enterprise"]` | [LITELLM-LIC], [LITELLM-README], [LITELLM-REL], [LITELLM-META], [LITELLM-DOC], [LITELLM-ENT], [LITELLM-COMMERCIAL] | Append reviewed primary evidence after all original legacy provenance; preserve source order and uniqueness. | High | None |

**Explicitly unchanged fields (exact values):**

```yaml
id: litellm
name: LiteLLM
official_url: https://www.litellm.ai
repository_url: https://github.com/BerriAI/litellm
categories:
- mlops-llmops-ai-infrastructure
subcategories:
- LLM & Application Frameworks
roles:
- cloud-engineer
- platform-engineer
- mlops-ai-infrastructure-engineer
lifecycle_stages:
- build
- deploy
- operate
deployment_models: []
license_model: open-core
maturity: unknown
alternatives: []
tags: []
```

### 14.9 ollama - CLEAR

```yaml
id: ollama
set:
  summary: MIT-licensed model runtime and manager supporting local inference and optional cloud features; model
    licenses are separate.
  repository_archived: false
  documentation_url: https://docs.ollama.com/
  license_spdx: MIT
  status: active
  needs_review: false
  use_when:
  - You need local model inference after downloading the required artifacts, with sufficient RAM or GPU capacity
    and cloud features disabled when local-only operation is required.
  avoid_when:
  - Do not expose the unauthenticated local API directly to untrusted networks; the default bind is 127.0.0.1:11434,
    and wider access needs network and authentication controls.
  - For local-only operation, disable cloud features with OLLAMA_NO_CLOUD=1 or the documented server setting, restart
    the service and provision required model artifacts locally.
  - Review every model's license and hardware requirements separately; the runtime's MIT license grants no uniform
    rights to model weights or cloud services.
  verified_on: '2026-10-28'
  sources:
  - legacy:9_AI-MLOps/README.md#L34
  - legacy:devopstools_final.md#L1207
  - https://github.com/ollama/ollama/blob/f067033f9126993b6172bdfffa71a74ad693fda4/LICENSE
  - https://github.com/ollama/ollama/blob/f067033f9126993b6172bdfffa71a74ad693fda4/README.md
  - https://github.com/ollama/ollama/releases/tag/v0.40.12
  - https://api.github.com/repos/ollama/ollama
  - https://docs.ollama.com/
  - https://docs.ollama.com/faq
  - https://docs.ollama.com/api/authentication
```

| Field | Exact existing value | Exact proposed value | Primary evidence | Reason | Confidence | Unresolved condition |
|---|---|---|---|---|---|---|
| summary | `"Local LLM runtime and model manager; open-source core (model licenses vary)."` | `"MIT-licensed model runtime and manager supporting local inference and optional cloud features; model licenses are separate."` | [OLLAMA-README], [OLLAMA-LIC] | Describe the demonstrated project and its licence or runtime scope without a safety guarantee. | High | None |
| repository_archived | **ABSENT** | `false` | [OLLAMA-META] | Record the current repository archive flag observed on the review date. | High | None |
| documentation_url | **ABSENT** | `"https://docs.ollama.com/"` | [OLLAMA-DOC], [OLLAMA-README] | Add the primary documentation entry or pinned project reference actually examined. | High | None |
| license_spdx | **ABSENT** | `"MIT"` | [OLLAMA-LIC] | Identify the principal project-code licence; external services, third-party components and model weights are outside this grant. | High | None |
| status | `"needs-review"` | `"active"` | [OLLAMA-LIC], [OLLAMA-README], [OLLAMA-REL], [OLLAMA-DOC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | High | None |
| needs_review | `true` | `false` | [OLLAMA-LIC], [OLLAMA-README], [OLLAMA-REL], [OLLAMA-DOC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | High | None |
| use_when | `["You need a lightweight CLI/API to run LLMs locally with zero cloud dependency."]` | `["You need local model inference after downloading the required artifacts, with sufficient RAM or GPU capacity and cloud features disabled when local-only operation is required."]` | [OLLAMA-README], [OLLAMA-DOC], [OLLAMA-LIC] | Describe an evidenced use case with minimum deployment and permission context. | High | None |
| avoid_when | `["You need production-scale multi-node inference or enterprise support."]` | `["Do not expose the unauthenticated local API directly to untrusted networks; the default bind is 127.0.0.1:11434, and wider access needs network and authentication controls.", "For local-only operation, disable cloud features with OLLAMA_NO_CLOUD=1 or the documented server setting, restart the service and provision required model artifacts locally.", "Review every model's license and hardware requirements separately; the runtime's MIT license grants no uniform rights to model weights or cloud services."]` | [OLLAMA-FAQ], [OLLAMA-AUTH], [OLLAMA-README], [OLLAMA-LIC] | Replace incomplete or opinion-based guidance with demonstrated security, data, licence and runtime limits. | High | None |
| verified_on | `"2026-08-03"` | `"2026-10-28"` | [OLLAMA-LIC], [OLLAMA-README], [OLLAMA-META] | Date of this actual primary-source revalidation, not a future application date. | High | None |
| sources | `["legacy:9_AI-MLOps/README.md#L34", "legacy:devopstools_final.md#L1207"]` | `["legacy:9_AI-MLOps/README.md#L34", "legacy:devopstools_final.md#L1207", "https://github.com/ollama/ollama/blob/f067033f9126993b6172bdfffa71a74ad693fda4/LICENSE", "https://github.com/ollama/ollama/blob/f067033f9126993b6172bdfffa71a74ad693fda4/README.md", "https://github.com/ollama/ollama/releases/tag/v0.40.12", "https://api.github.com/repos/ollama/ollama", "https://docs.ollama.com/", "https://docs.ollama.com/faq", "https://docs.ollama.com/api/authentication"]` | [OLLAMA-LIC], [OLLAMA-README], [OLLAMA-REL], [OLLAMA-META], [OLLAMA-DOC], [OLLAMA-FAQ], [OLLAMA-AUTH] | Append reviewed primary evidence after all original legacy provenance; preserve source order and uniqueness. | High | None |

**Explicitly unchanged fields (exact values):**

```yaml
id: ollama
name: Ollama
official_url: https://ollama.com
repository_url: https://github.com/ollama/ollama
categories:
- mlops-llmops-ai-infrastructure
subcategories:
- AI Ops & AI Tooling for DevOps
roles:
- cloud-engineer
- platform-engineer
- mlops-ai-infrastructure-engineer
lifecycle_stages:
- build
- deploy
- operate
deployment_models: []
license_model: oss
maturity: unknown
alternatives: []
tags: []
```

### 14.10 open-webui - CLEAR

```yaml
id: open-webui
set:
  summary: Self-hosted AI web platform for Ollama and compatible APIs; current code uses the custom Open WebUI License
    with branding conditions, alongside legacy BSD-3-Clause and MIT code.
  repository_archived: false
  documentation_url: https://docs.openwebui.com/
  license_model: source-available
  commercial_offering: true
  status: active
  needs_review: false
  use_when:
  - You need a self-hosted multi-user AI portal and can meet the current branding conditions, review external providers
    and restrict executable extensions to trusted administrators.
  avoid_when:
  - Current licensing from v0.6.6 adds branding restrictions; it is not a project-wide BSD-3-Clause or MIT grant.
    Legacy rights through v0.6.5 remain under their original licenses.
  - Branding changes require no more than 50 natural persons with direct access in any rolling 30-day period, specific
    prior written permission, or an executed Enterprise license expressly permitting the change; otherwise preserve
    the branding.
  - Tools, Functions and Pipelines can execute Python with backend privileges; grant creation and installation rights
    only to trusted administrators and review provider data flows, stored conversations and documents.
  verified_on: '2026-10-28'
  sources:
  - legacy:9_AI-MLOps/README.md#L36
  - legacy:devopstools_final.md#L1208
  - https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/LICENSE
  - https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/README.md
  - https://github.com/open-webui/open-webui/releases/tag/v0.12.4
  - https://api.github.com/repos/open-webui/open-webui
  - https://docs.openwebui.com/
  - https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/LICENSE_HISTORY
  - https://github.com/open-webui/open-webui/blob/07d8460126a686de9a99e2662d06106e22c3f6b6/LICENSE
  - https://docs.openwebui.com/license/
  - https://docs.openwebui.com/security/security-policy/
```

| Field | Exact existing value | Exact proposed value | Primary evidence | Reason | Confidence | Unresolved condition |
|---|---|---|---|---|---|---|
| summary | `"Self-hosted web UI for running and managing local AI model backends (e.g., Ollama)."` | `"Self-hosted AI web platform for Ollama and compatible APIs; current code uses the custom Open WebUI License with branding conditions, alongside legacy BSD-3-Clause and MIT code."` | [WEBUI-README], [WEBUI-LIC], [WEBUI-HISTORY] | Describe the demonstrated project and its licence or runtime scope without a safety guarantee. | High | None |
| repository_archived | **ABSENT** | `false` | [WEBUI-META] | Record the current repository archive flag observed on the review date. | High | None |
| documentation_url | **ABSENT** | `"https://docs.openwebui.com/"` | [WEBUI-DOC], [WEBUI-README] | Add the primary documentation entry or pinned project reference actually examined. | High | None |
| license_model | `"oss"` | `"source-available"` | [WEBUI-LIC], [WEBUI-HISTORY], [WEBUI-TERMS] | Represent the restricted current licence and mixed history as source-available in this catalogue. | Medium | None |
| commercial_offering | **ABSENT** | `true` | [WEBUI-LIC], [WEBUI-TERMS] | The vendor documents a separately contracted Enterprise offering; no entitlement is granted. | High | None |
| status | `"needs-review"` | `"active"` | [WEBUI-LIC], [WEBUI-README], [WEBUI-REL], [WEBUI-DOC], [WEBUI-HISTORY], [WEBUI-SEC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | Medium | None |
| needs_review | `true` | `false` | [WEBUI-LIC], [WEBUI-README], [WEBUI-REL], [WEBUI-DOC], [WEBUI-HISTORY], [WEBUI-SEC] | Apply the independent CLEAR verdict only with this complete bounded patch; active describes catalogue lifecycle, not deployment approval. | Medium | None |
| use_when | `["You want a ChatGPT-like interface for self-hosted models with multi-user support."]` | `["You need a self-hosted multi-user AI portal and can meet the current branding conditions, review external providers and restrict executable extensions to trusted administrators."]` | [WEBUI-README], [WEBUI-DOC], [WEBUI-LIC] | Describe an evidenced use case with minimum deployment and permission context. | High | None |
| avoid_when | `["You only interact with models programmatically and don't need a web frontend."]` | `["Current licensing from v0.6.6 adds branding restrictions; it is not a project-wide BSD-3-Clause or MIT grant. Legacy rights through v0.6.5 remain under their original licenses.", "Branding changes require no more than 50 natural persons with direct access in any rolling 30-day period, specific prior written permission, or an executed Enterprise license expressly permitting the change; otherwise preserve the branding.", "Tools, Functions and Pipelines can execute Python with backend privileges; grant creation and installation rights only to trusted administrators and review provider data flows, stored conversations and documents."]` | [WEBUI-SEC], [WEBUI-HISTORY], [WEBUI-TERMS], [WEBUI-README], [WEBUI-LIC] | Replace incomplete or opinion-based guidance with demonstrated security, data, licence and runtime limits. | High | None |
| verified_on | `"2026-08-03"` | `"2026-10-28"` | [WEBUI-LIC], [WEBUI-README], [WEBUI-META] | Date of this actual primary-source revalidation, not a future application date. | High | None |
| sources | `["legacy:9_AI-MLOps/README.md#L36", "legacy:devopstools_final.md#L1208"]` | `["legacy:9_AI-MLOps/README.md#L36", "legacy:devopstools_final.md#L1208", "https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/LICENSE", "https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/README.md", "https://github.com/open-webui/open-webui/releases/tag/v0.12.4", "https://api.github.com/repos/open-webui/open-webui", "https://docs.openwebui.com/", "https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/LICENSE_HISTORY", "https://github.com/open-webui/open-webui/blob/07d8460126a686de9a99e2662d06106e22c3f6b6/LICENSE", "https://docs.openwebui.com/license/", "https://docs.openwebui.com/security/security-policy/"]` | [WEBUI-LIC], [WEBUI-README], [WEBUI-REL], [WEBUI-META], [WEBUI-DOC], [WEBUI-HISTORY], [WEBUI-HISTORICAL], [WEBUI-TERMS], [WEBUI-SEC] | Append reviewed primary evidence after all original legacy provenance; preserve source order and uniqueness. | High | None |

**Explicitly unchanged fields (exact values):**

```yaml
id: open-webui
name: Open WebUI
official_url: https://openwebui.com
repository_url: https://github.com/open-webui/open-webui
categories:
- mlops-llmops-ai-infrastructure
subcategories:
- AI Ops & AI Tooling for DevOps
roles:
- cloud-engineer
- platform-engineer
- mlops-ai-infrastructure-engineer
lifecycle_stages:
- build
- deploy
- operate
deployment_models: []
maturity: unknown
alternatives: []
tags: []
```

## 15. Primary-source URL ledger

Every label used above resolves here. GitHub blob links are commit-specific unless explicitly described as a live observation. API repository and release metadata and hosted documentation are date-sensitive observations from 2026-10-28. They are not permanent lifecycle guarantees.

### azure-mcp-server

Reviewed release: Azure.Mcp.Server-3.0.0; source commit: 61715e6a9054d7922809b01e08a2efa85e032a6d.

- [AZURE-LIC](https://github.com/microsoft/mcp/blob/61715e6a9054d7922809b01e08a2efa85e032a6d/LICENSE)
[AZURE-LIC]: https://github.com/microsoft/mcp/blob/61715e6a9054d7922809b01e08a2efa85e032a6d/LICENSE
- [AZURE-README](https://github.com/microsoft/mcp/blob/61715e6a9054d7922809b01e08a2efa85e032a6d/servers/Azure.Mcp.Server/README.md)
[AZURE-README]: https://github.com/microsoft/mcp/blob/61715e6a9054d7922809b01e08a2efa85e032a6d/servers/Azure.Mcp.Server/README.md
- [AZURE-REL](https://github.com/microsoft/mcp/releases/tag/Azure.Mcp.Server-3.0.0)
[AZURE-REL]: https://github.com/microsoft/mcp/releases/tag/Azure.Mcp.Server-3.0.0
- [AZURE-META](https://api.github.com/repos/microsoft/mcp)
[AZURE-META]: https://api.github.com/repos/microsoft/mcp
- [AZURE-DOC](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/overview)
[AZURE-DOC]: https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/overview
- [AZURE-MIG](https://github.com/Azure/azure-mcp/blob/54f04ab1ade20b4adc4955cffea0833788307596/README.md)
[AZURE-MIG]: https://github.com/Azure/azure-mcp/blob/54f04ab1ade20b4adc4955cffea0833788307596/README.md
- [AZURE-SEC](https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security)
[AZURE-SEC]: https://learn.microsoft.com/en-us/azure/developer/azure-mcp-server/security

### kubernetes-mcp-server

Reviewed release: v0.0.69; source commit: bcadfee0e724836da2657ba609ff25c27ab35f58.

- [KUBERNETES-LIC](https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/LICENSE)
[KUBERNETES-LIC]: https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/LICENSE
- [KUBERNETES-README](https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/README.md)
[KUBERNETES-README]: https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/README.md
- [KUBERNETES-REL](https://github.com/containers/kubernetes-mcp-server/releases/tag/v0.0.69)
[KUBERNETES-REL]: https://github.com/containers/kubernetes-mcp-server/releases/tag/v0.0.69
- [KUBERNETES-META](https://api.github.com/repos/containers/kubernetes-mcp-server)
[KUBERNETES-META]: https://api.github.com/repos/containers/kubernetes-mcp-server
- [KUBERNETES-DOC](https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/README.md)
[KUBERNETES-DOC]: https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/README.md
- [KUBERNETES-CFG](https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/docs/configuration.md)
[KUBERNETES-CFG]: https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/docs/configuration.md
- [KUBERNETES-RBAC](https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/docs/getting-started-kubernetes.md)
[KUBERNETES-RBAC]: https://github.com/containers/kubernetes-mcp-server/blob/bcadfee0e724836da2657ba609ff25c27ab35f58/docs/getting-started-kubernetes.md

### terraform-mcp-server

Reviewed release: v1.4.1; source commit: 3781509a674482ca7e2821fab8159a25e3b29bdf.

- [TERRAFORM-LIC](https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/LICENSE)
[TERRAFORM-LIC]: https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/LICENSE
- [TERRAFORM-README](https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/README.md)
[TERRAFORM-README]: https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/README.md
- [TERRAFORM-REL](https://github.com/hashicorp/terraform-mcp-server/releases/tag/v1.4.1)
[TERRAFORM-REL]: https://github.com/hashicorp/terraform-mcp-server/releases/tag/v1.4.1
- [TERRAFORM-META](https://api.github.com/repos/hashicorp/terraform-mcp-server)
[TERRAFORM-META]: https://api.github.com/repos/hashicorp/terraform-mcp-server
- [TERRAFORM-DOC](https://developer.hashicorp.com/terraform/mcp-server/reference)
[TERRAFORM-DOC]: https://developer.hashicorp.com/terraform/mcp-server/reference
- [TERRAFORM-REG](https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/pkg/toolsets/registry.go)
[TERRAFORM-REG]: https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/pkg/toolsets/registry.go
- [TERRAFORM-RUN](https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/pkg/tools/tfe/create_run.go)
[TERRAFORM-RUN]: https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/pkg/tools/tfe/create_run.go
- [TERRAFORM-FILTER](https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/pkg/toolsets/filter.go)
[TERRAFORM-FILTER]: https://github.com/hashicorp/terraform-mcp-server/blob/3781509a674482ca7e2821fab8159a25e3b29bdf/pkg/toolsets/filter.go

### github-mcp-server

Reviewed release: v2.0.3; source commit: b98d115bbb080e9555466a96656ec4df605aea21.

- [GITHUB-LIC](https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/LICENSE)
[GITHUB-LIC]: https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/LICENSE
- [GITHUB-README](https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/README.md)
[GITHUB-README]: https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/README.md
- [GITHUB-REL](https://github.com/github/github-mcp-server/releases/tag/v2.0.3)
[GITHUB-REL]: https://github.com/github/github-mcp-server/releases/tag/v2.0.3
- [GITHUB-META](https://api.github.com/repos/github/github-mcp-server)
[GITHUB-META]: https://api.github.com/repos/github/github-mcp-server
- [GITHUB-DOC](https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/README.md)
[GITHUB-DOC]: https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/README.md
- [GITHUB-CFG](https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/docs/server-configuration.md)
[GITHUB-CFG]: https://github.com/github/github-mcp-server/blob/b98d115bbb080e9555466a96656ec4df605aea21/docs/server-configuration.md

### grafana-mcp

Reviewed release: v2.1.1; source commit: 244d1adde04194ecad15125cb17159a1db50626b.

- [GRAFANA-LIC](https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/LICENSE)
[GRAFANA-LIC]: https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/LICENSE
- [GRAFANA-README](https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/README.md)
[GRAFANA-README]: https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/README.md
- [GRAFANA-REL](https://github.com/grafana/mcp-grafana/releases/tag/v2.1.1)
[GRAFANA-REL]: https://github.com/grafana/mcp-grafana/releases/tag/v2.1.1
- [GRAFANA-META](https://api.github.com/repos/grafana/mcp-grafana)
[GRAFANA-META]: https://api.github.com/repos/grafana/mcp-grafana
- [GRAFANA-DOC](https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/README.md)
[GRAFANA-DOC]: https://github.com/grafana/mcp-grafana/blob/244d1adde04194ecad15125cb17159a1db50626b/README.md

### docker-mcp-gateway

Reviewed release: v0.44.3; source commit: 7e0f34277c91855ad861eeff536b4fdc77420593.

- [DOCKER-LIC](https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/LICENSE)
[DOCKER-LIC]: https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/LICENSE
- [DOCKER-README](https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/README.md)
[DOCKER-README]: https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/README.md
- [DOCKER-REL](https://github.com/docker/mcp-gateway/releases/tag/v0.44.3)
[DOCKER-REL]: https://github.com/docker/mcp-gateway/releases/tag/v0.44.3
- [DOCKER-META](https://api.github.com/repos/docker/mcp-gateway)
[DOCKER-META]: https://api.github.com/repos/docker/mcp-gateway
- [DOCKER-DOC](https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/)
[DOCKER-DOC]: https://docs.docker.com/ai/mcp-catalog-and-toolkit/mcp-gateway/
- [DOCKER-SEC](https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/docs/security.md)
[DOCKER-SEC]: https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/docs/security.md
- [DOCKER-GUIDE](https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/docs/mcp-gateway.md)
[DOCKER-GUIDE]: https://github.com/docker/mcp-gateway/blob/7e0f34277c91855ad861eeff536b4fdc77420593/docs/mcp-gateway.md
- [DOCKER-TOOLKIT](https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/)
[DOCKER-TOOLKIT]: https://docs.docker.com/ai/mcp-catalog-and-toolkit/toolkit/

### k8sgpt

Reviewed release: v0.4.41; source commit: 3644ecfd4f932be3901838b35e250a95f7732114.

- [K8SGPT-LIC](https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/LICENSE)
[K8SGPT-LIC]: https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/LICENSE
- [K8SGPT-README](https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/README.md)
[K8SGPT-README]: https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/README.md
- [K8SGPT-REL](https://github.com/k8sgpt-ai/k8sgpt/releases/tag/v0.4.41)
[K8SGPT-REL]: https://github.com/k8sgpt-ai/k8sgpt/releases/tag/v0.4.41
- [K8SGPT-META](https://api.github.com/repos/k8sgpt-ai/k8sgpt)
[K8SGPT-META]: https://api.github.com/repos/k8sgpt-ai/k8sgpt
- [K8SGPT-DOC](https://docs.k8sgpt.ai/)
[K8SGPT-DOC]: https://docs.k8sgpt.ai/
- [K8SGPT-LOG](https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/analyzer/log.go)
[K8SGPT-LOG]: https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/analyzer/log.go
- [K8SGPT-MAP](https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/analyzer/analyzer.go)
[K8SGPT-MAP]: https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/analyzer/analyzer.go
- [K8SGPT-ANALYSIS](https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/analysis/analysis.go)
[K8SGPT-ANALYSIS]: https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/analysis/analysis.go
- [K8SGPT-CLI](https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/cmd/analyze/analyze.go)
[K8SGPT-CLI]: https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/cmd/analyze/analyze.go
- [K8SGPT-PROVIDER](https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/ai/openai.go)
[K8SGPT-PROVIDER]: https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/ai/openai.go
- [K8SGPT-MASK](https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/util/util.go)
[K8SGPT-MASK]: https://github.com/k8sgpt-ai/k8sgpt/blob/3644ecfd4f932be3901838b35e250a95f7732114/pkg/util/util.go
- [K8SGPT-PRIVACY](https://docs.k8sgpt.ai/reference/guidelines/privacy/)
[K8SGPT-PRIVACY]: https://docs.k8sgpt.ai/reference/guidelines/privacy/

### litellm

Reviewed release: v1.106.5; source commit: 2569eb88694ce148dea5f324f240f79d256af8ae.

- [LITELLM-LIC](https://github.com/BerriAI/litellm/blob/2569eb88694ce148dea5f324f240f79d256af8ae/LICENSE)
[LITELLM-LIC]: https://github.com/BerriAI/litellm/blob/2569eb88694ce148dea5f324f240f79d256af8ae/LICENSE
- [LITELLM-README](https://github.com/BerriAI/litellm/blob/2569eb88694ce148dea5f324f240f79d256af8ae/README.md)
[LITELLM-README]: https://github.com/BerriAI/litellm/blob/2569eb88694ce148dea5f324f240f79d256af8ae/README.md
- [LITELLM-REL](https://github.com/BerriAI/litellm/releases/tag/v1.106.5)
[LITELLM-REL]: https://github.com/BerriAI/litellm/releases/tag/v1.106.5
- [LITELLM-META](https://api.github.com/repos/BerriAI/litellm)
[LITELLM-META]: https://api.github.com/repos/BerriAI/litellm
- [LITELLM-DOC](https://docs.litellm.ai/)
[LITELLM-DOC]: https://docs.litellm.ai/
- [LITELLM-ENT](https://github.com/BerriAI/litellm/blob/2569eb88694ce148dea5f324f240f79d256af8ae/enterprise/LICENSE.md)
[LITELLM-ENT]: https://github.com/BerriAI/litellm/blob/2569eb88694ce148dea5f324f240f79d256af8ae/enterprise/LICENSE.md
- [LITELLM-COMMERCIAL](https://docs.litellm.ai/docs/enterprise)
[LITELLM-COMMERCIAL]: https://docs.litellm.ai/docs/enterprise

### ollama

Reviewed release: v0.40.12; source commit: f067033f9126993b6172bdfffa71a74ad693fda4.

- [OLLAMA-LIC](https://github.com/ollama/ollama/blob/f067033f9126993b6172bdfffa71a74ad693fda4/LICENSE)
[OLLAMA-LIC]: https://github.com/ollama/ollama/blob/f067033f9126993b6172bdfffa71a74ad693fda4/LICENSE
- [OLLAMA-README](https://github.com/ollama/ollama/blob/f067033f9126993b6172bdfffa71a74ad693fda4/README.md)
[OLLAMA-README]: https://github.com/ollama/ollama/blob/f067033f9126993b6172bdfffa71a74ad693fda4/README.md
- [OLLAMA-REL](https://github.com/ollama/ollama/releases/tag/v0.40.12)
[OLLAMA-REL]: https://github.com/ollama/ollama/releases/tag/v0.40.12
- [OLLAMA-META](https://api.github.com/repos/ollama/ollama)
[OLLAMA-META]: https://api.github.com/repos/ollama/ollama
- [OLLAMA-DOC](https://docs.ollama.com/)
[OLLAMA-DOC]: https://docs.ollama.com/
- [OLLAMA-FAQ](https://docs.ollama.com/faq)
[OLLAMA-FAQ]: https://docs.ollama.com/faq
- [OLLAMA-AUTH](https://docs.ollama.com/api/authentication)
[OLLAMA-AUTH]: https://docs.ollama.com/api/authentication

### open-webui

Reviewed release: v0.12.4; source commit: 33c1978d5bad52a31df75ea55143025dfad18d16.

- [WEBUI-LIC](https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/LICENSE)
[WEBUI-LIC]: https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/LICENSE
- [WEBUI-README](https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/README.md)
[WEBUI-README]: https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/README.md
- [WEBUI-REL](https://github.com/open-webui/open-webui/releases/tag/v0.12.4)
[WEBUI-REL]: https://github.com/open-webui/open-webui/releases/tag/v0.12.4
- [WEBUI-META](https://api.github.com/repos/open-webui/open-webui)
[WEBUI-META]: https://api.github.com/repos/open-webui/open-webui
- [WEBUI-DOC](https://docs.openwebui.com/)
[WEBUI-DOC]: https://docs.openwebui.com/
- [WEBUI-HISTORY](https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/LICENSE_HISTORY)
[WEBUI-HISTORY]: https://github.com/open-webui/open-webui/blob/33c1978d5bad52a31df75ea55143025dfad18d16/LICENSE_HISTORY
- [WEBUI-HISTORICAL](https://github.com/open-webui/open-webui/blob/07d8460126a686de9a99e2662d06106e22c3f6b6/LICENSE)
[WEBUI-HISTORICAL]: https://github.com/open-webui/open-webui/blob/07d8460126a686de9a99e2662d06106e22c3f6b6/LICENSE
- [WEBUI-TERMS](https://docs.openwebui.com/license/)
[WEBUI-TERMS]: https://docs.openwebui.com/license/
- [WEBUI-SEC](https://docs.openwebui.com/security/security-policy/)
[WEBUI-SEC]: https://docs.openwebui.com/security/security-policy/

- [OSI approved licence inventory](https://opensource.org/licenses)


## 16. Proposed statistics, allowlists and rollback

These are predictions for applying the entire ten-record patch, not current achievements. Partial application requires fresh arithmetic.

| Metric | Current actual | Expected after future complete application |
|---|---:|---:|
| Canonical records | 1,425 | 1,425 |
| active | 816 | 826 |
| needs-review / records requiring review | 595 | 585 |
| archived / historical / deprecated | 10 / 2 / 2 | 10 / 2 / 2 |
| Target records | 80 | 80 |
| Target requiring review | 58 | 48 |
| Selected cohort requiring review | 10 | 0 |
| license_model unknown | 77 | 77 |
| Missing documentation_url, globally | 755 | 745 |
| Missing repository_url, globally | 383 | 382 |
| Unknown maturity, globally | 769 | 768 |
| Taxonomy categories | 30 | 30 |
| Records marked repository_archived true | 14 | 14 |

The review-debt reference_date would become 2026-10-28 because the script uses the maximum verified_on, not wall-clock time. The category inventory includes multi-category records: its mlops-llmops-ai-infrastructure total is 83, while the canonical target file has 80. Do not confuse the two counts. Changes to licence-model totals are documentation minus one (Azure), oss plus one (Azure) minus one (Open WebUI), source-available plus one, and no open-core change; unknown licences remain 77.

**Current write allowlist:** only docs/maintenance/2026-10-27-wave-28-ai-mcp-devops-evidence-review.md, append-only after the original 57,087-byte prefix. No canonical application is authorized by this document.

**Prepared future canonical allowlist:** data/tools/mlops-llmops-ai-infrastructure.yaml; exactly azure-mcp-server, kubernetes-mcp-server, terraform-mcp-server, github-mcp-server, grafana-mcp, docker-mcp-gateway, k8sgpt, litellm, ollama and open-webui; exactly the set keys above. No deletion. No name/ID changes. All 70 other records, their order and all unspecified fields must be identical.

Future documentation regeneration is required after an authorized canonical change. Generated files may then change only as the deterministic consequence of these records, including shared indices and counts. Determine their exact path set from the repository generator and review it during that separately authorized implementation; no generated path is writable in this review. No changes to schema, taxonomy, overrides, constraints, workflows, link-audit baseline, repository metadata, aliases or historical sources are included. Commit, push, PR, external workflows, merge and release remain outside scope; historical issue 2 stays open.

Before application, independently assert branch, HEAD/main SHA, target blob, all 80 IDs/order, exact old values and absence of unexpected local work. Stop if any differs. Apply only after an explicit user instruction; this READY assessment, if issued below, is not such an instruction. Apply each set mapping by ID without rewriting out-of-cohort data. Preserve key style/order of existing fields where practical and append new keys consistently with local conventions.

For rollback of this documentary work, remove only the appended second-pass bytes after verifying the saved prefix length/hash; never discard the untracked report or replace its first-pass content with the committed tree (the report does not exist in HEAD).

For rollback after a later authorized canonical application, first preserve that application's work and inspect intervening edits. Restore only the allowlisted field values from the exact old ledger: remove keys marked ABSENT and restore old scalar/list values and source lists. Do not issue a blanket checkout/reset over local work. Regenerate documentation from the restored canonical source and compare it to the pre-application generated snapshot. Recheck all 80 records and the target blob, then run the validation sequence below.

Future implementation verification, when separately authorized:

```powershell
& .venv/Scripts/python.exe -m pip install -e '.[dev]'
& .venv/Scripts/python.exe -m ruff check scripts tests
& .venv/Scripts/python.exe -m ruff format --check scripts tests
& .venv/Scripts/python.exe -m pytest
& .venv/Scripts/python.exe -m scripts.generate_docs
& .venv/Scripts/python.exe -m scripts.generate_docs --check
& .venv/Scripts/python.exe -m scripts.validate_catalog
& .venv/Scripts/python.exe -m scripts.review_debt --format json
git diff --check
```

Use a fresh, writable pytest basetemp outside the repository; never place intentionally invalid fixture Markdown in the repository, even under ignored paths. Compare actual resulting statistics to the predictions and inspect every generated difference. A network link audit is separate, not evidence of production readiness or lifecycle by itself.

## 17. Validation of this documentary pass

The exact field patch was merged with baseline records **in memory only** and validated against tool.schema.json with URI/date format checking. Complete proposed records preserve all unspecified values. Normalized repository URL uniqueness, source uniqueness and preservation of original source prefixes were checked. This does not claim generated documentation was produced for unapplied values.

The dependency installation required for an implementation was not repeated in this explicitly read-only review: the existing editable development environment was used, with Python 3.12.14 and a successful pip check. No dependency file or constraint was changed. The bare Windows python alias failed before execution; all subsequent Python commands use .venv/Scripts/python.exe. An exploratory pytest command used a nonexistent test_generate_docs.py filename and collected zero tests; the actual module is test_generation.py and was then used for diagnosis. These are not reported as test passes.

Final actual commands, results and preservation assertions follow after all checks complete. No full or strict network link audit, CI, external workflow, vulnerability scan, live tool/cluster/provider test, binary SBOM review, exhaustive model-weight licence review or private Enterprise contract approval is claimed.

Frozen patch size: **103 field changes across exactly ten records**, including complete source-list replacements that preserve every historical entry. Eight principal-code SPDX values are added; LiteLLM and Open WebUI SPDX remain absent.

### 17.1 Actual results and final freeze verification

| Check actually executed | Result |
|---|---|
| .venv/Scripts/python.exe -m scripts.review_debt --format json | PASS; 1,425 canonical, 595 requiring review, 77 unknown licences; reference_date 2026-10-26 |
| .venv/Scripts/python.exe -m scripts.validate_catalog | PASS before append and after the complete second-pass patch/ledger was appended |
| .venv/Scripts/python.exe -m scripts.generate_docs --check | PASS before and after append; generated documentation is current for the unchanged real YAML |
| .venv/Scripts/python.exe -m ruff check scripts tests --no-cache | PASS |
| .venv/Scripts/python.exe -m ruff format --check scripts tests --no-cache | PASS; 70 files already formatted |
| .venv/Scripts/python.exe -m pip check | PASS; no broken requirements |
| Full pytest invocation, with external basetemp/cache | 1,012 tests collected in a separate collection check; full run had 14 local-socket failures and 8 skips, with the remaining 990 tests passing |
| Diagnosis of local HTTP fixture failures | A direct localhost request through _http_request returned PermissionError / WinError 10013; fixture handlers received no requests. No repository defect was inferred from these blocked requests |
| Retry of all 14 failures with localhost-capable execution | PASS: 14 passed, 57 deselected in 7.71 seconds, exit code 0. This was an existing fixture-test retry, not a real catalogue link audit |
| Focused test_generation.py diagnostic | PASS: 134 passed in 20.67 seconds, exit code 0 |
| Embedded YAML preview parsed and merged in memory | PASS: ten unique record IDs, exactly 103 differing fields; all ten proposed merged records schema-valid, including URI/date formats |
| Unchanged-fields YAML blocks compared with actual old records | PASS: all unspecified field values match exactly |
| In-memory future catalogue | PASS: 1,425 schema-valid records, no normalized repository collisions, preserved legacy source prefixes, unique source lists; active 826 and needs-review 585 |
| First-pass prefix and canonical preservation | PASS: original 57,087-byte prefix hash preserved; all 80 canonical objects and order equal baseline, including all 70 out-of-cohort records |
| git diff --check | PASS; no tracked changes |
| Untracked report whitespace check using git diff --no-index --check -- NUL | No whitespace diagnostics; exit 1 indicates the expected added-file difference. Git also printed its normal LF-to-CRLF working-copy notice |

Full test command used:

```powershell
& .venv/Scripts/python.exe -m pytest --basetemp=C:/Users/bgian/.codex/visualizations/2026/10/28/01a18229-6dd4-7263-aa01-90e104385fb6/wave28-second-pass-pytest -o cache_dir=C:/Users/bgian/.codex/visualizations/2026/10/28/01a18229-6dd4-7263-aa01-90e104385fb6/wave28-second-pass-pytest-cache -q
```

Retry command, with permission to access localhost sockets:

```powershell
& .venv/Scripts/python.exe -m pytest tests/test_links.py --lf --basetemp=C:/Users/bgian/.codex/visualizations/2026/10/28/01a18229-6dd4-7263-aa01-90e104385fb6/retry -o cache_dir=C:/Users/bgian/.codex/visualizations/2026/10/28/01a18229-6dd4-7263-aa01-90e104385fb6/wave28-second-pass-pytest-cache -o addopts= -q
```

The first full invocation did not pass under the original socket restriction. The separate retry resolved every recorded failure; a second entire suite was not run or claimed. Eight skips remain skips. Temporary fixtures and helper material were kept outside the repository, not under reports/. Two append-launch attempts failed before any report write (JavaScript template parsing, then the Windows command-length limit); a temporary external helper performed the single successful append.

### 17.2 Gate decision

**READY FOR CONTROLLED CANONICAL APPLICATION**, for exactly the ten frozen record proposals and 103 field changes above, subject to a fresh matching baseline and a subsequent explicit user authorization.

There are **10 CLEAR and 0 RETAIN REVIEW proposals**. The four first-pass retentions are resolved by established source flow or bounded licence/support descriptions, not by assuming production readiness or accepting unexamined commercial terms. Known operational hazards and deployment-specific contract questions remain explicit. No outstanding essential evidence condition blocks these exact catalogue descriptions.

**Actual application remains zero.** All ten real records are still needs-review with needs_review true. Actual counts remain 816 active and 595 needs-review. The only repository path changed during this task is this existing Markdown report; the first-pass prefix is intact. No YAML, generated document, constraint, workflow, link-audit exception, schema, taxonomy, migration history, alias or repository metadata was changed. No commit, push, PR, issue write, external workflow, merge or release was performed. Local main and HEAD still equal the expected SHA and issue 2 remains open.

This gate is documentary readiness, not an implementation instruction. Stop here.
