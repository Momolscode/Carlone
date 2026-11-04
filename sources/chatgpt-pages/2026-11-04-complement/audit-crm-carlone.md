# Audit du CRM Carlone et enrichissement des données

Source : https://chatgpt.com/space/page_e138620f745481919453e0cec121871d

Collecte complémentaire du 4 novembre 2026. Dernière mise à jour source : 2026-10-28T17:33:10.925238Z. Séquence de la liste : 0. Copie des blocs Markdown de la page entière.

Archive documentaire : les propositions et validations rapportées restent attribuées à la source. Ce document ne prouve ni signature, paiement ni intégration en exploitation.

Conserver le CRM existant et renforcer la traçabilité de ses enrichissements est le prochain lot proposé. Le dépôt fourni par Morgan permet d’identifier le code et son modèle de données ; l’intégration à l’outil utilisé par Quali Contact reste à spécifier. Analyse du 28 octobre 2026 sur la branche `claude/new-session-utninu`, révision `18c2080cac09993bffa426b39d20b765f8413c4f`.

# Périmètre examiné

Lecture de l’arborescence complète, de [README.md](https://github.com/FinanceScope/CRM-Carlone/blob/18c2080cac09993bffa426b39d20b765f8413c4f/README.md), [PASSATION.md](https://github.com/FinanceScope/CRM-Carlone/blob/18c2080cac09993bffa426b39d20b765f8413c4f/PASSATION.md), des scripts de fusion et d’enrichissement, des sections de stockage et d’export de [site/index.html](https://github.com/FinanceScope/CRM-Carlone/blob/18c2080cac09993bffa426b39d20b765f8413c4f/site/index.html) et de la note Hermès. Les 500 fiches de [site/companies.json](https://github.com/FinanceScope/CRM-Carlone/blob/18c2080cac09993bffa426b39d20b765f8413c4f/site/companies.json) ont été analysées pour produire les comptes ci-dessous. Le suivi partagé de l’application en service n’a pas été consulté ; les essais d’interface mentionnés dans la passation n’ont pas été rejoués. Aucun script de fusion, envoi, enrichissement externe ou changement du dépôt n’a été exécuté.

La branche par défaut `main` ne contient que le README initial. La branche de travail contient 621 fichiers, dont les sources, les lots de recherche et l’application. Toute reprise doit indiquer la branche et la révision étudiées pour éviter d’évaluer un dépôt apparemment vide.

# Résultats sur les données versionnées

| Contrôle | Résultat au 28 octobre 2026 |
| --- | --- |
| Entreprises et identifiants | 500 fiches et 500 SIREN distincts, aucun SIREN vide |
| Téléphones | 471 renseignés ; 283 portent le drapeau « à confirmer » |
| E-mails et sites | 109 e-mails renseignés et 283 sites web |
| Enrichissement | 500 fiches avec les champs `fiab` et `completude` |
| Actualités et motifs de contact | 3 fiches avec `actualites`, 2 avec `declencheur` |
| Comptes liés et interlocuteurs | 124 fiches avec comptes liés, 60 avec `contacts_admin` |
| Date de vérification du standard | Absente dans `fiab.standard` pour 499 fiches sur 500 |
| Opposition issue des recherches | 14 valeurs vraies, 19 fausses et 467 non renseignées |

Un champ renseigné ne prouve ni sa justesse ni sa fraîcheur. Ces nombres décrivent le fichier versionné, pas les données saisies depuis dans le suivi partagé. Les décomptes successifs de la passation sont un historique ; ils ne se cumulent pas. La base combine un classement initial, des chiffres de différents exercices et des entreprises sélectionnées par effectif : sa présence ne prouve pas un classement homogène des 500 plus grandes entreprises.

# Ce qui existe déjà

[enrich.py](https://github.com/FinanceScope/CRM-Carlone/blob/18c2080cac09993bffa426b39d20b765f8413c4f/enrich.py) ajoute des vérifications de standards, des comptes liés, des actualités, un motif de contact et un indice de complétude. Il préserve un autre numéro publié à côté de l’existant et conserve des réserves. L’interface propose les fiches entreprises, les appels, le suivi, les refus, les exports CSV et l’agenda. Ces fonctions sont présentes dans le code ; leur fonctionnement partagé en service reste à vérifier dans l’environnement concerné.

Le partage s’appuie sur `window.claude.use("db")` et la collection `suivi` ([initialisation](https://github.com/FinanceScope/CRM-Carlone/blob/18c2080cac09993bffa426b39d20b765f8413c4f/site/index.html#L2518-L2544)). Hors de cet environnement, l’application utilise le stockage local du navigateur. Une publication sur un autre hébergement ne fournit donc pas à elle seule le même suivi partagé.

# Améliorations prioritaires

1. **Stabiliser tous les identifiants avant une actualisation du classement.** L’initialisation utilise le SIREN pour les fiches étendues et le rang pour les autres ([code](https://github.com/FinanceScope/CRM-Carlone/blob/18c2080cac09993bffa426b39d20b765f8413c4f/site/index.html#L2508)). Si un rang est réaffecté à une autre entreprise, le suivi peut être rattaché au mauvais compte. Préparer une correspondance entre anciennes clés et SIREN, sauvegarder le suivi, puis vérifier sa migration sur données fictives avant tout changement.

2. **Enregistrer la preuve et la date par valeur.** La majorité des dates de `fiab` sont nulles ; plusieurs niveaux « haute » sont déduits de catégories générales ([fonction fiab](https://github.com/FinanceScope/CRM-Carlone/blob/18c2080cac09993bffa426b39d20b765f8413c4f/enrich.py#L180-L216)). Conserver URL exacte, date d’observation, date du contrôle, méthode et réserve, puis afficher distinctement présence, fiabilité et fraîcheur. L’absence de date doit rester visible.

3. **Préparer les changements avant leur application.** L’enrichissement peut remplacer le site web en gardant l’ancienne valeur ([code](https://github.com/FinanceScope/CRM-Carlone/blob/18c2080cac09993bffa426b39d20b765f8413c4f/enrich.py#L146-L151)), mais ce passage n’expose pas de validation humaine. Ajouter un journal de propositions avec ancienne valeur, valeur proposée, source et décision. Les informations confirmées par l’équipe doivent avoir une priorité explicite ; leur remplacement doit être signalé.

4. **Spécifier un export et un retour de campagne pour le logiciel réel.** Le CSV existant ne prouve pas sa compatibilité avec Quali Contact. Les exports « appels » et « entreprises » ne sélectionnent pas exactement le téléphone de la même manière ([exports](https://github.com/FinanceScope/CRM-Carlone/blob/18c2080cac09993bffa426b39d20b765f8413c4f/site/index.html#L2434-L2450)). Définir l’identifiant stable, le numéro à utiliser, les exclusions, les champs de retour et la gestion des doublons selon le format accepté par le prestataire.

5. **Rendre la reconstruction reproductible.** Le [README](https://github.com/FinanceScope/CRM-Carlone/blob/18c2080cac09993bffa426b39d20b765f8413c4f/README.md) omet `enrich.py` dans sa commande, alors que la [passation](https://github.com/FinanceScope/CRM-Carlone/blob/18c2080cac09993bffa426b39d20b765f8413c4f/PASSATION.md) le prévoit. Aligner les consignes et produire un manifeste avec révision, fichiers d’entrée, date et résultat des contrôles. Une reconstruction ne doit pas modifier les données saisies dans le suivi partagé.

# Apport de la compétence fournie

La [compétence crm-enrichment de Panaversity](https://github.com/panaversity/agentfactory-business-plugins/blob/main/sales-revops-marketing/skills/crm-enrichment/SKILL.md), fichier lu à la révision de contenu `fa4f34ccc2eecef26443235a07c17274ed739d93`, apporte une grille de champs, un rapport des changements et la protection des valeurs saisies manuellement. Elle est utilisée ici comme référence ; aucune installation ni planification n’a été effectuée.

Adaptation au dossier : garder le SIREN comme ancrage d’entreprise, distinguer les contacts personnels et les comptes, limiter la collecte aux coordonnées professionnelles pertinentes et conserver les données inconnues comme telles. Une source publiée pour un e-mail ne prouve pas sa délivrabilité. Le contrôle syntaxique et de provenance présent dans le script ne doit pas être présenté comme une vérification de boîte mail. Les changements sensibles et les conflits vont dans une file de revue, sans alerte ou message envoyé automatiquement au titre de cet audit.

L’indice actuel pondère notamment téléphone, dirigeant, chiffres, interlocuteurs, site et opposition. Il est utile pour ordonner le travail mais ne correspond pas au pourcentage de tous les champs remplis. Prévoir trois lectures séparées : couverture des champs utiles, niveau de preuve et ancienneté.

# Premier lot à chiffrer

Livrables proposés : un dictionnaire des données et des sources ; un registre de propositions d’enrichissement ; une spécification d’échange avec Quali Contact ; une recette sur dix entreprises fictives. Ce lot consolide l’existant. Son prix attend l’effort de chaque intervenant, les accès disponibles et le format cible.

Chaque proposition de changement porte : SIREN, contact éventuel, champ, valeur actuelle ou empreinte, valeur proposée, URL source, dates, méthode de vérification, niveau de preuve, motif, état de revue et décision humaine. L’historique permet de retrouver et d’annuler une modification acceptée. Le rafraîchissement des données de référence et le suivi commercial sont traités séparément.

Recette proposée : deux imports identiques ne créent aucun doublon ; un changement de rang conserve le suivi du SIREN ; une valeur confirmée manuellement n’est pas écrasée ; un refus reste prioritaire ; une source périmée reste signalée ; un échec d’import se reprend sans perte ; le téléphone exporté suit la règle convenue ; un retour d’appel crée une seule activité sur le bon compte. Ce sont des critères à tester, pas des contrôles déjà exécutés.

# Information qui conditionne le raccordement

La [note Hermès](https://github.com/FinanceScope/CRM-Carlone/blob/18c2080cac09993bffa426b39d20b765f8413c4f/docs/hermes-vocalcom.md) existe, mais précise elle-même reposer sur des titres et extraits de recherche et présenter un format d’import proposé. Elle n’établit pas que Quali Contact utilise ce logiciel ou accepte ce format. Il faut obtenir le nom, la version et le module réellement utilisés, ainsi qu’un modèle d’import et de retour ou la documentation officielle de l’API. Aucun choix de fournisseur, coût ou connecteur n’est validé par cet audit.

Prochaine action : récupérer un modèle de fichier d’import et de retour de l’outil effectivement utilisé par Quali Contact afin de compléter la correspondance avec les champs du CRM déjà identifié.
