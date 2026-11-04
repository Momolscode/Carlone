# Lecteur C5-crm — CRM Entreprises Nièvre, Hermes360 et Quali Contact

Lecture du 4 novembre 2026, dépôt `Momolscode/Carlone` (branche main, commit 7b46602), dossier `crm/` = copie (git subtree) de FinanceScope/CRM-Carlone au commit b53a81c du 30 octobre 2026. Les effectifs ont été recalculés avec Python (`python3 -I`, lecture seule) sur `crm/site/companies.json`, `crm/site/culture.json` et le contenu des trois archives zip lu en mémoire. Aucun fichier du dépôt n'a été modifié, aucun service extérieur n'a été interrogé. Le client s'appelle GianLuca Carlone ; les pièces qui écrivent « John-Lucas » sont citées telles quelles avec [sic, lire GianLuca].

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ; [MM] résultat mesuré ; [IN] inconnu.

## 1. Pièces lues

| Chemin | Date de la pièce | Nature et auteur | Original ou copie | Ce qui n'a pas pu être lu |
| --- | --- | --- | --- | --- |
| `crm/README.md` | non datée ; état au commit b53a81c (30 oct.) | Mode d'emploi du dépôt CRM ; rédigé par l'agent « Claude » (tous les commits visibles du CRM sont signés Claude) | Copie (subtree du 4 nov.) | Rien |
| `crm/PASSATION.md` | rédigée le 22/10/2026 (l. 37), mises à jour jusqu'au 29/10, commit du 30/10 | Document de reprise « pour continuer le projet depuis un autre compte Claude » ; auteur : agent Claude ; donneur d'ordre nommé une fois : Mathys (l. 7) | Copie | L'archive `crm-nievre-projet.zip` citée l. 38 n'est pas dans le dépôt |
| `crm/docs/rapport/rapport-crm-hermes360.md` | 29 octobre 2026 | Rapport destiné à « M. Carlone » ; agent Claude | Copie ; source du PDF | Schéma `schema-crm-hermes360.png` non examiné ; version `.docx` non lue |
| `crm/docs/rapport/Rapport CRM Nièvre et Hermes360.pdf` (lu via `sources-txt/crm__docs__rapport__Rapport CRM Nièvre et Hermes360.txt`) | 29 octobre 2026, 7 pages | Export du rapport ci-dessus | Copie (export) | Texte extrait : parenthèses, puces et deux-points partiellement perdus ; contenu identique au .md |
| `crm/docs/hermes-vocalcom.md` | 22/10/2026, partie 3.4 mise à jour le 28/10 | Étude « pour les associés » ; agent Claude ; fondée sur des titres et extraits de recherche web, sans contact avec l'éditeur (l. 5) | Copie | PDF « Étude Hermes360 (Vocalcom) et alternatives » et `hermes.html` non lus (contenu présumé identique) |
| `crm/autonome/LISEZMOI.md` | 29–30 oct. 2026 | Guide d'installation de la version Firebase ; agent Claude | Copie | — |
| `crm/autonome/firestore.rules` (+ `firebase.json`, `public/config.js`, `public/index.html`, recherche dans `public/crm-firebase.js`) | 29 oct. 2026 | Règles de sécurité Firestore, valeurs d'exemple | Copie | `crm-firebase.js` seulement parcouru par recherche textuelle |
| `crm/site/companies.json` | données « au 29/10/2026 » | 500 fiches produites par scripts et agents de recherche | Copie | Exactitude des valeurs (numéros, noms, chiffres) non contrôlée à la source |
| `crm/site/culture.json` | idem | 97 prospects culture + « playbook » (formats, calendrier, cadre pratique, financements, communication, prospection) | Copie | Playbook survolé (titres et règles du cadre pratique) |
| `sources/chatgpt-pages/2026-11-04-complement/audit-crm-carlone.md` | source mise à jour le 28/10 17:33 UTC ; collecte du 4/11 | Page ChatGPT (espace de Morgan), audit du CRM à la révision 18c2080 du 28/10 | Copie (export) | Jumeau `.json` non lu ; page en ligne non consultée |
| `sources/crm-reference-2026-11-04.md` | 4 nov. 2026 | Note de référence ; auteur non indiqué (intégration du 4 nov.) | Original (dépôt Carlone) | — |
| `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md` (partie Quali Contact : l. 7, 13, 18, 20–51, 53–61, 67–69 ; lu en entier) | source mise à jour le 28/10 17:48 UTC ; export du 4/11 | Page ChatGPT ; propos rapportés de Morgan | Copie (export) | Jumeau `.json` non lu |
| `sources/archives-crm/` : `crm-entreprises-nievre-v1-2026-10-22.zip`, `-v2-2026-10-22.zip`, `-v3-2026-10-23.zip` | 22, 22 et 23 oct. 2026 | Paquets de la page CRM (index.html + companies.json, puis culture.json) | Originaux d'archive | Listés et comptés en mémoire ; les `index.html` archivés n'ont pas été lus |
| Vérifications ponctuelles hors liste | — | `README.md:35` (racine) ; `interne/contexte-projet-carlone.md:11` ; `interne/offres-de-carlone-catalogue-crm.md:96` ; `crm/art_merge.py:17-19,129` ; recherches textuelles dans `crm/site/index.html` et sur tout `crm/` ; `git log` | — | Lecture partielle, ciblée |
| Inaccessibles | — | Artefacts claude.ai 4UxtzQPwRBXPKNNYuDqFTG (ancienne page), CrKrSAuH9mUAaey2wN8uSV (page en service), 7YjrTj2xG7RVyTTE9H63ct (rapport), 7CxFvbouc5d9Y4Xcxq4wMk (étude) ; collection partagée « suivi » ; dépôt FinanceScope en ligne ; éventuel projet Firebase ; pages Qualicontact | — | Historique git antérieur au 27 oct. absent du clone (dépôt superficiel) |

## 2. Affirmations déterminantes

| N° | Affirmation | Code | Source | Remarque |
| --- | --- | --- | --- | --- |
| 1 | Le dépôt canonique du CRM est FinanceScope/CRM-Carlone, branche `claude/new-session-utninu` ; la branche main ne contient que le README. | [DR] | `sources/crm-reference-2026-11-04.md:3-6` ; `sources/chatgpt-pages/2026-11-04-complement/audit-crm-carlone.md:15` | Non revérifié en ligne (hors périmètre d'accès). |
| 2 | FinanceScope/CRM-Carlone est « le dépôt de Mathys ». | [DR] | `README.md:35` | Seule mention ; titulaire du compte et éventuelle personne morale inconnus. |
| 3 | Les comptes GitHub de Morgan consultés n'ont qu'un accès en lecture à FinanceScope ; une copie a été intégrée dans `crm/` le 4 nov. | [DR] + [FV] | `sources/crm-reference-2026-11-04.md:10,14` ; commit 95de15f (Morgan Olsen, 4 nov. 16:57) | « Historique compris » non vérifiable ici : le clone est superficiel et l'historique visible commence le 27 oct. |
| 4 | Les 48 commits visibles du CRM (27–30 oct.) sont tous signés « Claude <noreply@anthropic.com> ». | [FV] | `git log b53a81c` | La recherche de données et le code ont été produits par des agents IA ; les relectures et décisions humaines ne sont pas tracées. |
| 5 | Le CRM contient 500 fiches et 500 SIREN distincts. | [FV] | `crm/site/companies.json` (calcul) | Concorde avec `audit-crm-carlone.md:21`. |
| 6 | Les 500 ne forment pas un classement homogène : rangs 1–100 = classement Pappers du 02/09/2026 ; 101–432 = CA du dernier exercice publié ; 433–500 = sociétés sans comptes publiés d'au moins 10 salariés, classées par effectif. | [DR] | `crm/PASSATION.md:62-64` ; `audit-crm-carlone.md:30` | Parler des « 500 plus grandes entreprises de la Nièvre » serait inexact. |
| 7 | 485 entreprises sont en campagne : 11 en procédure collective, 3 hors campagne (SAEMAN Nièvre, ENEA, Circuit de Nevers Magny-Cours), 1 activité peut-être cessée (Wilson). | [FV] | `companies.json` (champs statut, exclue, cessation) ; `rapport-crm-hermes360.md:62` | Concorde. |
| 8 | 471 fiches ont un numéro de téléphone. | [FV] | `companies.json` | Chiffre de présence, pas de joignabilité (voir 9–10). |
| 9 | Parmi les 471 numéros : 283 portent « à confirmer » (un seul annuaire ou source ancienne), 29 sont le standard d'une autre société du groupe, 1 seul est marqué « vérifié » ; 188 n'ont pas le drapeau « à confirmer », dont ces 29. | [FV] | `companies.json` (telephone_a_confirmer, telephone_groupe, telephone_verifie, fiab.standard) | 60 % des numéros sont à confirmer au premier appel. |
| 10 | La date de vérification n'est renseignée que pour 1 fiche sur 500 ; toutes les autres dates de fiabilité sont vides. | [FV] | `companies.json` (fiab.*[2]) ; `audit-crm-carlone.md:27` | Fraîcheur des données non traçable. |
| 11 | 34 numéros sont partagés par 73 fiches (sociétés d'un groupe, holdings, mêmes dirigeants), dont 2 numéros mobiles. | [FV] | `companies.json` | La passation annonçait 16 cas (`PASSATION.md:17`). |
| 12 | Classement des 485 : priorité haute 57 (vague 1 : 10, vague 2 : 13, vague 3 : 34), moyenne 296, basse 132. | [FV] | `companies.json` ; `rapport-crm-hermes360.md:66` | Sur les 500 : 147 basses (les 15 écartées sont en basse). |
| 13 | Les « 37 cibles prioritaires » sont les priorités hautes du top 100 ; toutes ont un numéro, dont 7 « à confirmer » ; sur les 57 hautes, 21 sont « à confirmer ». | [FV] | `companies.json` ; `rapport-crm-hermes360.md:62,67` | — |
| 14 | 60 entreprises ont des interlocuteurs finance, RH ou administration (78 personnes) ; aucune ligne directe, 3 e-mails, 52 profils LinkedIn. | [FV] | `companies.json` (contacts_admin) | Ce sont surtout des noms à demander au standard. |
| 15 | Un responsable finance est nommé pour 28 entreprises, dont 4 confirmés. | [DR] | `rapport-crm-hermes360.md:69` ; `PASSATION.md:79` | Le champ contact_finance (420 fiches) contient surtout le dirigeant (409 « dirigeant », 2 « DAF/RAF », 9 « autre »). |
| 16 | 125 fiches d'appel approfondies existent : 97 du top 100 et 28 des rangs 101–500. | [FV] | `companies.json` (champ fiche) ; `rapport-crm-hermes360.md:51` ; `PASSATION.md:9,14` | Concorde. |
| 17 | « 97 » désigne deux ensembles distincts : les 97 entreprises actives du top 100 et les 97 prospects culture. | [FV] | `companies.json` ; `culture.json` ; `PASSATION.md:7,56` | Source de confusion dans les présentations. |
| 18 | Les 97 prospects culture se répartissent en 38 « Artistes », 30 associations, 17 lieux et institutions, 12 réseaux et événements ; 22 sont de type « Artiste ». | [FV] | `culture.json` | `PASSATION.md:56` parle de « 97 artistes » : inexact. |
| 19 | Aucun champ de suivi (statut de prospection, responsable, relance, historique, rendez-vous) n'existe dans `companies.json` ni dans les trois archives zip. | [FV] | `companies.json` ; `sources/archives-crm/*.zip` (calcul) | Le suivi vit dans la collection « suivi » de l'artefact claude.ai ou dans le stockage local du navigateur (`crm/site/index.html:1132-1133`) : inaccessible à l'audit. |
| 20 | « Aucun prospect, rendez-vous ou taux de conversion n'est encore constaté. » | [DR] | `carlone-offres-et-projets.md:57` (28 oct.) | Aucune pièce plus récente ne fait état d'un appel, d'un rendez-vous ou d'une vente. Aucun [MM] commercial. |
| 21 | Le suivi saisi sur l'ancienne page n'a pas été repris lors de la republication depuis le nouveau compte (22 oct.). | [DR] | `PASSATION.md:4,57` | Un éventuel suivi est dispersé entre deux artefacts et des navigateurs. |
| 22 | La page CRM en service est un artefact claude.ai privé (CrKrSAuH9mUAaey2wN8uSV) avec base partagée, identité des utilisateurs et export CSV. | [DR] | `PASSATION.md:4` | Compte titulaire non nommé ; la note B liste « CRM Entreprises Nièvre (22 oct.) » parmi les artefacts de Morgan. |
| 23 | Dans le dépôt, la version autonome n'est pas configurée : `config.js` contient « A_REMPLACER » et les règles listent des adresses d'exemple ; l'installation figure parmi les décisions à prendre. | [FV] (dépôt) / [IN] (déploiement réel) | `crm/autonome/public/config.js:6-9` ; `crm/autonome/firestore.rules:16-24` ; `rapport-crm-hermes360.md:140` | Le rapport décrit pourtant au présent un CRM « hébergé sur Firebase » (`rapport-crm-hermes360.md:12`). |
| 24 | Les règles Firestore exigent une connexion Google, un e-mail vérifié et une adresse listée ; seul le propriétaire écrit dans `/donnees`. | [FV] | `firestore.rules:10-30` | Conception correcte pour la lecture ; tout autre chemin est refusé par défaut. |
| 25 | Tout associé autorisé peut créer, modifier et supprimer n'importe quel document de `/suivi` et `/reglages`, sans contrôle de format ni historique côté serveur. | [FV] | `firestore.rules:32-37` | Un compte compromis ou une erreur de code peut effacer le suivi de toute l'équipe. |
| 26 | Le code du CRM (index.html) est chargé par le propriétaire dans Firestore puis exécuté chez chaque associé par `document.write`. | [FV] | `crm/autonome/public/crm-firebase.js:142` ; `LISEZMOI.md:11` | Confiance totale dans un seul compte Google ; pas d'en-tête de sécurité du contenu dans `firebase.json`. |
| 27 | Sauvegarde : export CSV manuel ; « les données restent aussi dans votre projet Firebase ». | [DR] | `LISEZMOI.md:65` | Ni sauvegarde automatique, ni restauration testée, ni journal immuable. |
| 28 | Le CRM a été testé (30 parcours Playwright, émulateurs Firebase) et relu (22, 19, 43, 23, 30 et 13 défauts corrigés). | [DR] | `PASSATION.md:18-24,81,83,87` ; `LISEZMOI.md:12` | Aucun fichier de test versionné dans `crm/` (recherche « test », « spec », « playwright » : rien). |
| 29 | L'offre gratuite de Firebase suffit pour 2 à 4 associés ; installation d'environ 30 minutes. | [ES] | `rapport-crm-hermes360.md:18` ; `LISEZMOI.md:14,70` | Quotas « connus au moment de l'écriture » ; installation en ligne de commande pour un non-technicien. |
| 30 | « Propriété : le code, les données et le suivi restent chez les associés, dans leur dépôt GitHub et leur projet Firebase. » | [DR] | `rapport-crm-hermes360.md:19` ; PDF p. 1 | Le dépôt est au compte de Mathys ; GianLuca Carlone n'y figure que comme adresse « à autoriser » (`rapport-crm-hermes360.md:140`) ; aucun contrat. |
| 31 | Le dépôt FinanceScope/CRM-Carlone est public (contrôle par l'API GitHub le 4 nov., dernier envoi le 30 oct.). | [DR] | `interne/contexte-projet-carlone.md:11` ; `interne/offres-de-carlone-catalogue-crm.md:96` | Non revérifié par cet audit ; à traiter comme urgent. |
| 32 | La copie `crm/` (645 fichiers) contient environ 940 chaînes distinctes au format d'un numéro français, 206 adresses e-mail distinctes et 63 fichiers avec des profils LinkedIn (87 profils distincts). | [FV] | Recherche textuelle sur `crm/` | Cohérent avec « 931 numéros, 206 e-mails, 63 fichiers » (`interne/contexte-projet-carlone.md:11`). Si le dépôt source est public, ces données sont exposées. |
| 33 | `companies.json` contient des données de personnes physiques : 740 mentions de dirigeants (468 fiches), 78 interlocuteurs, 184 « autres contacts », 24 standards en 06/07, 25 e-mails de messageries grand public. | [FV] | `companies.json` | Le cadre B2B n'exclut pas le RGPD. |
| 34 | `culture.json` contient pour 97 prospects 21 numéros mobiles et 26 e-mails de messageries grand public ; 38 fiches concernent des artistes, souvent des personnes physiques. | [FV] | `culture.json` | Démarchage de particuliers ou d'artistes-auteurs : régime plus strict que le B2B. |
| 35 | Base légale retenue : l'intérêt légitime, avec droit d'opposition géré par la colonne `opposition_prospection`. | [DR] | `crm/docs/hermes-vocalcom.md:290,312` | Interprétation de l'agent, non validée par un juriste ; responsable de traitement non désigné. |
| 36 | 14 entreprises sont notées opposées à la prospection ; l'opposition n'a été vérifiée que pour 33 fiches. | [FV] | `companies.json` ; `rapport-crm-hermes360.md:73` | 467 fiches non vérifiées. |
| 37 | « Un prospect sans réponse est supprimé 3 ans après le dernier contact. » | [DR] | `rapport-crm-hermes360.md:90` ; `crm/site/index.html:859` | Aucune fonction de suppression repérée dans `index.html` (recherche « supprim », « purge », « 3 ans ») : règle affichée, application non démontrée [HY]. |
| 38 | La structure qui vend les œuvres n'est pas choisie ; elle doit figurer dans chaque mail et au téléphone. | [FV] (décision manquante) | `PASSATION.md:31` ; `rapport-crm-hermes360.md:141` | Bloque l'envoi conforme des mails et la désignation du responsable de traitement. |
| 39 | Consigne : ne jamais citer Le Vieux Relais ni le M aux entreprises ; un filtre (regex « INTERDIT ») bloque ces mentions. | [FV] | `PASSATION.md:49-50` | Le prospect ignore l'intérêt du vendeur à l'exposition des œuvres. |
| 40 | Le dispositif de l'article 238 bis AB du CGI est prorogé jusqu'au 31/12/2028 (article 89 de la loi de finances pour 2026, actualité BOFiP du 15/04/2026). | [DR] | `PASSATION.md:44` | À vérifier sur Légifrance/BOFiP. |
| 41 | L'exposition d'œuvres achetées par une entreprise dans un lieu tiers ouvert au public (piste du Vieux Relais) n'est pas explicitement prévue par le BOFiP. | [DR] | `PASSATION.md:35` | Hypothèse centrale du modèle commercial, non validée. |
| 42 | L'économie d'impôt affichée vaut 5 × plafond × 25 %, sans limitation par le bénéfice ni taux réduit des PME. | [FV] | `crm/art_merge.py:17-19,129` | Ex. Textilot : bénéfice 130 000 €, plafond 835 000 €, « économie max » 1 043 750 €. 58 entreprises bénéficiaires ont un plafond annuel supérieur à leur bénéfice. |
| 43 | Plafond annuel de déduction des 37 cibles : de 28 639 € à 835 000 €, médiane 84 840 €. | [FV] (calcul) / [ES] (données) | `companies.json` ; `rapport-crm-hermes360.md:77` | Somme théorique ≈ 4,6 M€ par an : un plafond fiscal, pas un marché. |
| 44 | « Hermès Pro », conseillé aux associés, est l'ancien nom de Vocalcom Hermes360. | [DR] | `hermes-vocalcom.md:3,13,50` | Qui l'a conseillé : inconnu. |
| 45 | Hermes360 est jugé surdimensionné pour 2 à 4 associés ; recommandation : CRM + téléphones, puis éventuellement Aircall ou Ringover. | [PR] | `hermes-vocalcom.md:17,268-273` ; `PASSATION.md:33` | Étude du 22/10. |
| 46 | Le module Hermes360 du CRM (export de campagne, liste d'exclusion, levée de fiche, import du rapport d'appels) est « prêt, testé sur des fichiers d'essai ». | [DR] | `rapport-crm-hermes360.md:102` ; PDF p. 5 ; `PASSATION.md:83` | Aucun fichier Hermes360 réel ; format non public (`hermes-vocalcom.md:116`). |
| 47 | « Import de campagne en CSV (confirmé par Vocalcom) ». | [DR] | `rapport-crm-hermes360.md:102` ; PDF p. 5 | « Confirmé » = discours commercial du site (`hermes-vocalcom.md:114`) ; aucun contact avec Vocalcom (`rapport-crm-hermes360.md:149`). |
| 48 | Vocalcom ne publie ni API, ni webhooks, ni connecteur Zapier/Make ; son connecteur HUCC ne vise que Salesforce, Dynamics et Zendesk. | [DR] | `hermes-vocalcom.md:16,167` ; `rapport-crm-hermes360.md:117` | Fondé sur des extraits de recherche web. |
| 49 | Prix Hermes360 : sur devis ; 55 à 190 $ par poste et par mois selon des tiers ; offre « Hermes Essentials » à 175 200 $ sur 12 mois pour 200 agents. | [DR] / [ES] | `hermes-vocalcom.md:15,167,201` ; `rapport-crm-hermes360.md:117` | Non confirmé. |
| 50 | « Le client prévoit d'engager Quali Contact » (Morgan, 25 oct.). | [DR] | `carlone-offres-et-projets.md:7,13` | Aucune trace contractuelle ; Quali Contact n'est cité nulle part dans `crm/`. |
| 51 | Le logiciel, le module, les droits d'accès, le format d'import et de retour et les conditions de traitement de Quali Contact sont inconnus. | [IN] | `sources/crm-reference-2026-11-04.md:12` ; `carlone-offres-et-projets.md:18,51,69` ; `audit-crm-carlone.md:66-70` | Bloquant pour toute passerelle. |
| 52 | Les pages publiques de Qualicontact décrivent ses campagnes et une activité de relation donateurs ; elles ne permettent pas d'identifier l'outil. | [DR] | `carlone-offres-et-projets.md:51` (consultation du 25 oct.) | Adéquation à la vente d'œuvres en B2B non établie. |
| 53 | Une passerelle CRM ↔ Quali Contact est décrite comme cahier de raccordement, avec critères de réception ; aucun test n'a été exécuté. | [PR] | `carlone-offres-et-projets.md:38-49` | — |
| 54 | Méthode proposée : commencer par 20 comptes bien qualifiés avant d'élargir. | [PR] | `carlone-offres-et-projets.md:57` | « Pas un objectif commercial convenu ». |
| 55 | Premier lot proposé : dictionnaire des données, registre des propositions d'enrichissement, spécification d'échange avec Quali Contact, recette sur dix entreprises fictives ; prix non fixé. | [PR] | `audit-crm-carlone.md:58-64` | — |
| 56 | Le suivi est indexé par SIREN pour les fiches étendues et par rang pour les autres : une réaffectation de rang peut rattacher le suivi à la mauvaise entreprise. | [DR] | `audit-crm-carlone.md:40` | Analyse de la révision 18c2080 (28 oct.) ; non revérifiée sur b53a81c. |
| 57 | Le README omet `enrich.py` dans la chaîne de régénération que la passation prévoit. | [FV] | `crm/README.md:20` ; `PASSATION.md:81` | Reproductibilité fragile. |
| 58 | Hypothèse Marwin : 20 journées-personnes, 15 000 € HT par mois, 6 mois, acompte de 7 500 € HT ; « Le CRM réalisé sert de point de départ ; aucun contrat ni paiement n'est acquis. » | [PR] / [HY] | `carlone-offres-et-projets.md:65` | Le CRM a été produit avant tout contrat. |
| 59 | Mathys a demandé le recentrage sur les 100 premières entreprises (23/10). | [DR] | `PASSATION.md:7` | Seul donneur d'ordre nommé dans les pièces du CRM. |
| 60 | « John-Lucas [sic, lire GianLuca] souhaite déléguer le quotidien » et envisage une disponibilité de vingt jours par mois. | [DR] | `carlone-offres-et-projets.md:65` | Propos de Morgan, non confirmés par le client. |
| 61 | « Un associé rachète deux établissements à Cosne-Cours-sur-Loire : Le Vieux Relais (hôtel-restaurant) et le M (bar). » | [DR] | `PASSATION.md:41` | Diverge de `carlone-offres-et-projets.md:14-15` (voir section 4). |
| 62 | 15 entreprises actives en campagne n'ont aucun numéro publié (holdings, micro-structures). | [FV] | `companies.json` ; `rapport-crm-hermes360.md:67` ; `PASSATION.md:77` | Concorde. |
| 63 | Le volet culture comprend un guide pratique (spectacles, Sacem, Guso, droit de présentation publique, assurance « clou à clou », vente d'œuvres facturée par l'artiste, sécurité incendie, vente au déballage). | [DR] | `crm/site/culture.json:3202-3312` | Recherches web de l'agent ; à valider par des professionnels. |
| 64 | L'évolution des archives : v1 (22 oct.) 100 entreprises, 33 numéros ; v2 ajoute 97 prospects culture ; v3 (23 oct.) 500 entreprises, 194 numéros, 96 priorités hautes (vagues 16/18/62). | [FV] | `sources/archives-crm/*.zip` (calcul) | Concorde avec `PASSATION.md:5-6`. |

## 3. Chiffres, engagements et dates

### Chiffres annoncés et recalcul (4 novembre 2026)

| Chiffre annoncé | Où | Recalcul | Code | Lecture |
| --- | --- | --- | --- | --- |
| 500 entreprises | `rapport-crm-hermes360.md:8` ; PDF p. 1 | 500 fiches, 500 SIREN ; 485 en campagne | [FV] | Exact ; périmètre hétérogène (affirmation 6). |
| 471 numéros | `rapport-crm-hermes360.md:8,67` | 471 renseignés ; 283 à confirmer ; 29 de groupe ; 1 vérifié ; 188 sans drapeau | [FV] | Exact en présence ; la qualité réelle est inconnue avant les premiers appels. |
| 60 entreprises avec interlocuteurs | `rapport-crm-hermes360.md:8,69` | 60 fiches, 78 personnes, 0 ligne directe, 3 e-mails | [FV] | Exact ; ce sont des noms, pas des contacts directs. |
| 125 fiches approfondies | `rapport-crm-hermes360.md:51` ; PDF p. 2 | 125 (97 + 28) | [FV] | Exact. Autre « 125 » : 125 à 250 fiches par associé (`hermes-vocalcom.md:17`), soit 500 ÷ 4 et 500 ÷ 2. |
| 97 | `rapport-crm-hermes360.md:30` ; `PASSATION.md:7,56` | 97 actives du top 100 ; 97 prospects culture dont 38 artistes | [FV] | Deux ensembles différents ; « 97 artistes » inexact. |
| 37 cibles, toutes avec standard | `rapport-crm-hermes360.md:62,67` | 37/37 ; 7 à confirmer | [FV] | Exact. |
| Haute 57 (10/13/34), moyenne 296, basse 132 | `rapport-crm-hermes360.md:66` | Identique sur 485 | [FV] | — |
| Dirigeants 458 | `rapport-crm-hermes360.md:68` | 456 fiches en campagne avec au moins un dirigeant ; 468 sur 500 | [FV] | Écart de 2, sans portée. |
| 107 e-mails, 281 sites | `rapport-crm-hermes360.md:72` | 107 / 281 sur 485 ; 109 / 283 sur 500 | [FV] | `audit-crm-carlone.md:23` compte sur 500 : les deux sont justes. |
| Comptes 2025 : 142 ; 2024 : 177 ; 2023 : 46 ; non publiés : 119 | `rapport-crm-hermes360.md:70` | Identique (+ 1 exercice 2026) | [FV] | — |
| 86 en perte | idem | 86 | [FV] | — |
| IS 298, probable 151, à vérifier 36 | `rapport-crm-hermes360.md:71` | Identique | [FV] | — |
| Opposition 14, vérifiée pour 33 | `rapport-crm-hermes360.md:73` | 14 / 33 | [FV] | La passation disait 13 et 32. |
| Comptes liés 124 | `rapport-crm-hermes360.md:74` | 124 | [FV] | — |
| Complétude 52 (60 pour les cibles) | `rapport-crm-hermes360.md:75` | 52,4 / 59,6 | [FV] | Indice pondéré, pas un taux de remplissage (`audit-crm-carlone.md:56`). |
| Standards partagés : 16 cas | `PASSATION.md:17` ; `hermes-vocalcom.md:173` | 34 numéros, 73 fiches | [FV] | Sous-estimé. |
| Champs de suivi d'appel remplis | — | 0 (aucun champ) dans les données versionnées et les archives | [FV] | Activité réelle [IN]. |

### Montants, volumes, durées et échéances

| Élément | Valeur | Code | Source |
| --- | --- | --- | --- |
| Plafond de déduction 238 bis AB | le plus élevé de 20 000 € ou 5 ‰ du CA, minoré du mécénat | [DR] | `PASSATION.md:5,45` ; `rapport-crm-hermes360.md:54` |
| Déduction | par cinquièmes sur 5 ans | [DR] | `PASSATION.md:45` |
| Achats éligibles | jusqu'au 31/12/2028 | [DR] | `PASSATION.md:28,44` |
| Taux d'IS utilisé | 25 % (le taux réduit de 15 % des PME n'est pas appliqué) | [FV] | `crm/art_merge.py:19` |
| Plafond des 37 cibles | 28 639 € à 835 000 €, médiane 84 840 € ; somme ≈ 4,6 M€/an | [FV] calcul / [ES] | `companies.json` ; `rapport-crm-hermes360.md:77` |
| Rythme d'appel | 4 appels au plus en 30 jours ; rappel au jour ouvré suivant ; relance à 3 jours ; verrou « en appel » de 20 minutes | [DR] | `rapport-crm-hermes360.md:40,43` |
| Conservation | refus gardés 3 ans ; prospects sans réponse supprimés après 3 ans | [DR] | `rapport-crm-hermes360.md:83,90` |
| Vente hors établissement à une entreprise de 5 salariés au plus | 14 jours de rétractation ; aucun paiement avant 7 jours | [DR] | `rapport-crm-hermes360.md:88` ; `hermes-vocalcom.md:331-333` |
| Consentement préalable au démarchage téléphonique des consommateurs | depuis le 11/08/2026 (loi n° 2025-594, décret n° 2026-662) | [DR] | `hermes-vocalcom.md:281` |
| Préfixes ARCEP des plateformes | depuis le 01/01/2023 | [DR] | `hermes-vocalcom.md:300` |
| Sanction démarchage | jusqu'à 375 000 € pour une personne morale | [DR] | `hermes-vocalcom.md:285` |
| Hermes360 | sur devis ; 55–190 $/poste/mois ; 110–760 $/mois pour 2 à 4 postes ; Essentials 175 200 $/12 mois/200 agents | [ES] / [DR] | `hermes-vocalcom.md:15,201,167` |
| Alternatives | Aircall Professional ≥ 150 €/mois (3 licences) ; Ringover Business 88 à 132 €/mois ; second numéro Onoff ≈ 9 €/mois | [DR] | `hermes-vocalcom.md:255-256,270-271` |
| Temps réel Hermes360 | 1 à 2 jours de mise en place (webhook + relais) | [ES] | `hermes-vocalcom.md:179` ; `rapport-crm-hermes360.md:104` |
| Import du rapport du soir | environ 2 minutes | [ES] | `rapport-crm-hermes360.md:102` |
| Firebase gratuit | 50 000 lectures, 20 000 écritures/jour, 1 Go | [DR] | `LISEZMOI.md:70` |
| Installation autonome | environ 30 minutes | [ES] | `LISEZMOI.md:14` |
| Quota des agents de recherche | 200 recherches web par tour | [DR] | `PASSATION.md:32` |
| Volume de travail des agents | 82 puis 119 recherches web pour les responsables financiers des cibles ; 293 entreprises recherchées pour les décideurs ; 645 fichiers dans `crm/`, dont 546 de données brutes | [DR] / [FV] | `PASSATION.md:12,75,79` ; `git ls-files` |
| Proposition Marwin | 15 000 € HT/mois, 20 journées-personnes, 6 mois, acompte 7 500 € HT | [PR] / [HY] | `carlone-offres-et-projets.md:65` |
| Premier essai | 20 comptes qualifiés | [PR] | `carlone-offres-et-projets.md:57` |
| Dates clés | 02/09 classement Pappers ; 22/10 passation, étude Hermès, archives v1–v2 ; 23/10 archive v3 et recentrage ; 25/10 annonce de Quali Contact ; 27–28/10 refonte, décideurs, enrichissement, Hermes360 ; 28/10 audit ChatGPT (révision 18c2080) ; 29/10 rapport et version autonome ; 30/10 dernier commit (b53a81c) ; 4/11 copie dans `crm/` | [FV] / [DR] | Pièces citées ; `git log` |
| Coût de développement du CRM, temps humain passé, coût de maintenance | aucun chiffre | [IN] | — |

## 4. Contradictions et divergences

| Sujet | Version A + source | Version B + source | Portée pour l'audit |
| --- | --- | --- | --- |
| État de l'hébergement | « Il est hébergé sur Firebase … à une adresse du type crm-nievre.web.app » (`rapport-crm-hermes360.md:12` ; PDF p. 1) | Configuration « A_REMPLACER » et adresses d'exemple (`config.js:6-9`, `firestore.rules:16-24`) ; installation encore à faire (`rapport-crm-hermes360.md:140`) | Avancement présenté au client comme acquis alors qu'il est conditionnel. |
| Confidentialité | « Personne d'autre ne lit les fiches ni le suivi » (`rapport-crm-hermes360.md:15`) | Dépôt FinanceScope public avec numéros, e-mails et profils LinkedIn (`interne/contexte-projet-carlone.md:11`) | Exposition de données personnelles ; promesse inexacte. |
| Propriété | « Le code, les données et le suivi restent chez les associés » (`rapport-crm-hermes360.md:19`) | Dépôt de Mathys (`README.md:35`), lecture seule pour Morgan (`crm-reference-2026-11-04.md:14`), GianLuca Carlone simple utilisateur (`rapport-crm-hermes360.md:140`) | Propriété du CRM et des données non définie entre Marwin, Mathys, Morgan et GianLuca Carlone. |
| Qui appelle | 2 à 4 associés appellent eux-mêmes avec leurs téléphones (`hermes-vocalcom.md:17,270`) ; choisir entre Hermes360, Aircall, Ringover ou le téléphone seul (`rapport-crm-hermes360.md:143`) | Les opératrices de Quali Contact, engagées par le client (`carlone-offres-et-projets.md:7,20-22,38`) | Le CRM a été conçu pour un usage interne ; le modèle réel (externalisé) n'est pas tranché. |
| Hermes360 | « Hermès / Vocalcom : non, sauf à devenir un vrai centre d'appels » (`hermes-vocalcom.md:273`) | Module d'intégration Hermes360 développé et 30 défauts corrigés (`PASSATION.md:83`) ; « compatible » (`rapport-crm-hermes360.md:8`) | Effort consacré à une option que la propre étude écartait. |
| Compatibilité | « Le CRM fonctionne avec Hermes360 dans tous les cas » (`rapport-crm-hermes360.md:94`) | Format d'import non public (`hermes-vocalcom.md:116`) ; « le CSV existant ne prouve pas sa compatibilité avec Quali Contact » (`audit-crm-carlone.md:46`) | Compatibilité affirmée sans fichier réel. |
| Source Vocalcom | « Import de campagne en CSV (confirmé par Vocalcom) » (`rapport-crm-hermes360.md:102`) | « sans contact avec Vocalcom » (`rapport-crm-hermes360.md:149`) ; « discours commercial, non recoupé » (`hermes-vocalcom.md:114`) | Surinterprétation d'une page commerciale. |
| Prêt à l'emploi | « Le CRM est prêt à servir » (`rapport-crm-hermes360.md:8,138`) | Fonctionnement partagé en service à vérifier (`audit-crm-carlone.md:34`) ; vendeur non choisi (`PASSATION.md:31`) ; 283 numéros à confirmer | « Prêt » techniquement, pas opérationnellement ni juridiquement. |
| Nombre de décisions | « trois décisions restent à prendre » (`rapport-crm-hermes360.md:138`) | six cases listées (`rapport-crm-hermes360.md:140-145`) | Incohérence de rédaction dans un document client. |
| Standards partagés | 16 cas (`PASSATION.md:17` ; `hermes-vocalcom.md:173`) | 34 numéros, 73 fiches (calcul) | Risque de doublons d'appel et de mauvais rattachement des retours. |
| Oppositions | 13 opposées (`PASSATION.md:51`), vérifiées pour 32 (`PASSATION.md:26`) | 14 / 33 (`rapport-crm-hermes360.md:73` ; données) | Couches successives non harmonisées. |
| Culture | « 97 artistes » (`PASSATION.md:56`) | 97 structures, dont 38 artistes (`culture.json`) ; « artistes et structures culturelles » (`rapport-crm-hermes360.md:30`) | Volume d'artistes surestimé. |
| Téléphones | « Aujourd'hui 54 fiches sur 500 ont un téléphone » (`PASSATION.md:90`, section « À faire » du 22/10) | 471 sur 500 (`PASSATION.md:77`) | La section « À faire » de la passation est périmée. |
| Vagues | 25 / 22 / 22 (`PASSATION.md:69`, ancienne logique) ; 96 cibles 16 / 18 / 62 (`PASSATION.md:5`) | 57 cibles 10 / 13 / 34 (`PASSATION.md:14` ; `rapport-crm-hermes360.md:66`) | Les chiffres changent à chaque passe ; citer la date. |
| Principe du CRM | « pas encore intégré dans la page » (`PASSATION.md:43`) | « Réorientation vers la vente d'œuvres d'art faite » (`PASSATION.md:5`) | Document stratifié : l'ordre de lecture compte. |
| Plancher de 20 000 € | « à vérifier » (`PASSATION.md:45`) | « confirmé par le BOFiP » (`PASSATION.md:5`) | Idem. |
| Lieux | « Un associé rachète » Le Vieux Relais (hôtel-restaurant) et le M (bar) (`PASSATION.md:41`) | « John-Lucas [sic, lire GianLuca] a racheté » un ancien bar-restaurant-hôtel pour une galerie ; il « souhaite racheter le M » pour un cabaret (`carlone-offres-et-projets.md:14-15`) | Statut des acquisitions et nature du M incertains. |
| Suivi hors claude.ai | Hors claude.ai, stockage local seulement (`audit-crm-carlone.md:36`) | Raccord Firebase du 29/10 (`PASSATION.md:87`) | L'audit ChatGPT porte sur 18c2080 (28/10) ; il ne couvre ni Hermes360, ni Firebase, ni le rapport. |
| Mails | « Envoyons les e-mails depuis nos messageries » (`hermes-vocalcom.md:270`) | Le vendeur doit figurer dans chaque mail et n'est pas choisi (`PASSATION.md:31`) | Aucun mail conforme possible en l'état. |
| Économie d'impôt | Chiffres « grisés quand l'économie est théorique » (entreprise en perte) (`rapport-crm-hermes360.md:54`) | Économie non plafonnée par le bénéfice : Textilot 1 043 750 € pour 130 000 € de bénéfice (`art_merge.py:129`) | Argument chiffré trompeur au téléphone. |
| Conservation | « supprimé 3 ans après le dernier contact » (`rapport-crm-hermes360.md:90`) | Aucune purge repérée dans `index.html` | Règle RGPD affichée, non outillée. |

## 5. Informations inconnues et questions

1. Le CRM a-t-il servi ? Combien d'entrées contient la collection « suivi » de l'artefact CrKrSAuH9mUAaey2wN8uSV (appels, rendez-vous, refus, « Œuvre achetée »), avec quelles dates et quels auteurs ? Et l'ancienne page 4UxtzQPwRBXPKNNYuDqFTG ?
2. Sur quel compte claude.ai cet artefact est-il publié (Morgan, Mathys, autre) ? Qui peut l'ouvrir ?
3. Qui sont exactement « les associés » du CRM ? GianLuca Carlone, ses associés dans les lieux, Morgan, Mathys ? Qui appelle ?
4. La version Firebase a-t-elle été installée ? Sur quel compte Google ? Qui en est « propriétaire » ?
5. Le dépôt FinanceScope/CRM-Carlone est-il toujours public ce soir ? Depuis quand ? A-t-il été cloné ou dupliqué ? Faudra-t-il purger l'historique ?
6. Qui est responsable de traitement (quelle entité) ? Existe-t-il un registre des traitements, une analyse de l'intérêt légitime, une mention d'information des personnes, une liste des sous-traitants (Anthropic, GitHub, Google, Quali Contact) ?
7. Quelle structure vend les œuvres ? Quelles œuvres, de quels artistes, à quel prix, avec quel stock ?
8. Un expert-comptable ou un avocat fiscaliste a-t-il validé l'exposition des œuvres dans un lieu tiers ouvert au public ?
9. Quali Contact : contrat signé ou non ? Qui paie (GianLuca Carlone, quelle société) ? Quel volume (opératrices, heures, appels) ? Quel logiciel et quel module ? Quel format d'import et de retour ? Quelle date de début ? Qui valide les scripts et les offres ? Existe-t-il un contrat de sous-traitance RGPD ?
10. Qui a conseillé « Hermès Pro » ? Est-ce l'outil de Quali Contact ?
11. Les douze questions ont-elles été envoyées à Vocalcom ? Quelles réponses ?
12. Si Quali Contact appelle avec son outil, à quoi sert le module Hermes360 et le suivi partagé du CRM ? Quel outil est la référence ?
13. Qui maintient le CRM après le 30 octobre (code, données, mises à jour de comptes annuels, contrôles des numéros), avec quel budget et quel abonnement ?
14. À qui appartiennent le code et la base de 500 fiches et 97 prospects ? Le travail réalisé avant contrat sera-t-il facturé, cédé ou licencié ?
15. Quel taux de numéros faux ou périmés au premier appel ? Aucun échantillon n'a été appelé.
16. Les deux entrepreneurs individuels et les 24 lignes mobiles relèvent-ils du consentement préalable du Code de la consommation ?
17. La règle ARCEP des préfixes s'applique-t-elle à Quali Contact ou à des appels manuels ?
18. Les 97 prospects culture ont-ils été contactés ? Par qui ?
19. Que contient l'historique du dépôt avant le 27 octobre (absent du clone local) ?

## 6. Par chantier

| Chantier | Ce que disent mes pièces |
| --- | --- |
| CRM et développement commercial | Outil abouti techniquement : 500 fiches (485 en campagne), 471 numéros dont 283 à confirmer, 125 fiches d'appel, mémo d'appel, simulation fiscale, refus, exports, vue « Aujourd'hui » (`rapport-crm-hermes360.md`). Produit par des agents IA du 22 au 30 oct. (`git log`). Aucun appel, rendez-vous ni vente constaté (`carlone-offres-et-projets.md:57`). Offre commerciale fondée sur l'article 238 bis AB, avec deux validations manquantes : structure vendeuse (`PASSATION.md:31`) et exposition en lieu tiers (`PASSATION.md:35`). Économie d'impôt surévaluée pour 58 bénéficiaires (`art_merge.py:129`). |
| Quali Contact | Connu : annonce rapportée par Morgan le 25 oct. (`carlone-offres-et-projets.md:7`) ; activité publique de campagnes et de relation donateurs (`:51`) ; passerelle proposée avec critères de réception non testés (`:38-49`). Inconnu : contrat, payeur, volume, logiciel, format, date, rôle dans la validation des offres (`:32`), cadre RGPD (`crm-reference-2026-11-04.md:12`). Aucune mention dans `crm/`. |
| Organisation et pilotage | Hypothèse de 20 journées-personnes à 15 000 € HT par mois (`carlone-offres-et-projets.md:65`) ; souhait rapporté de déléguer le quotidien (`:65`) ; décisions ouvertes listées dans le rapport (`rapport-crm-hermes360.md:140-145`) ; seul donneur d'ordre nommé dans le CRM : Mathys (`PASSATION.md:7`). |
| Jarvis, mémoire et automatisations | Pas de mention de Jarvis. La passation sert de mémoire entre comptes Claude (`PASSATION.md:37`) ; chaîne de scripts et de lots d'agents avec contre-vérification (`crm/README.md:9-22`) ; temps réel envisagé via Make, Zapier ou n8n (`hermes-vocalcom.md:179`) ; référence à la compétence « crm-enrichment » de Panaversity, non installée (`audit-crm-carlone.md:52`). |
| Marketing et contenus | Mail d'approche, discours, objections, note pour l'expert-comptable (`PASSATION.md:27`) ; fiche d'offre à préparer pour les opératrices (`carlone-offres-et-projets.md:20-30`) ; plan de communication locale (presse, offices de tourisme) dans `culture.json:2881` (playbook). |
| Galerie, œuvres et artistes | Vente d'œuvres originales d'artistes vivants aux entreprises (`hermes-vocalcom.md:3`) ; 97 prospects culture dont 38 artistes (`culture.json`) ; règles pratiques : convention d'exposition, assurance « clou à clou », vente facturée par l'artiste, commission et contribution diffuseur (`culture.json:3252-3282`) ; galerie dans un ancien bar-restaurant-hôtel racheté (`carlone-offres-et-projets.md:14`). |
| Événements et vernissage | Dix formats (dont « Expo tournante et vernissage avec l'artiste », `culture.json:2884`), calendrier de 20 événements locaux, financements (pass Culture, Région, Département) et une idée d'événement par prospect (`culture.json`) ; événement artistique à cadrer (`carlone-offres-et-projets.md:16`). |
| Cabaret et autres lieux | Le M (bar) jamais nommé aux entreprises ni aux artistes (`PASSATION.md:49-50`) ; projet de cabaret (`carlone-offres-et-projets.md:15`) ; règles spectacles (6 représentations sans formalité), Sacem, Guso, sécurité incendie GN 6, bruit (`culture.json:3202-3312`). |
| Medhi et BOJ.ART | Rien. |
| STRATES, Éclosion et créations | Rien. |
| Laboratoire IA et robotique | Rien. |

## 7. Erreurs d'identité

- « John-Lucas » [sic, lire GianLuca] : 9 occurrences, toutes dans `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md`, lignes 1, 7, 13, 14, 15, 16, 18, 32 et 65.
- Aucune occurrence de « John-Lucas », « John Lucas » ou d'une autre variante dans `crm/` (645 fichiers), `sources/crm-reference-2026-11-04.md` et `audit-crm-carlone.md`.
- Les pièces du CRM écrivent « M. Carlone » sans prénom : `crm/PASSATION.md:85,87` ; `crm/docs/rapport/rapport-crm-hermes360.md:140` ; PDF p. 7. Le CRM lui-même (`crm/site/index.html`) ne nomme pas le client.
- Aucune pièce lue n'écrit « GianLuca ».

## 8. Instructions trouvées dans les pièces

Aucune n'a été exécutée.

- `crm/PASSATION.md:37-38` : document adressé à « un autre compte Claude », « à joindre dans la nouvelle conversation ».
- `crm/PASSATION.md:32` : consigne aux agents : « Travailler par paquets de moins de 180 recherches, un par tour, et terminer le tour aussitôt le paquet lancé. »
- `crm/PASSATION.md:34` : « Élargir l'accès réseau dans les réglages de l'environnement. »
- `crm/PASSATION.md:21,73,77,81` : lots prêts « à relancer » (`zr08`–`zr10`, `python3 restants_lots.py zs`, décideurs `m04`–`m15`, `b01`–`b09`, `ext/enr_in_r05`…).
- `crm/PASSATION.md:89-93` : liste « À faire » (coordonnées, réorientation, export Hermès Pro, contacter artistes et associations).
- `crm/README.md:20-21` : commandes de régénération des données (`python3 -I merge.py && …`).
- `crm/README.md:15` et dossier `crm/scratch/` (21 fichiers, non lus) : consignes réutilisables destinées aux agents de recherche.
- `crm/autonome/LISEZMOI.md:38-44,62` : commandes d'installation et de déploiement (`npm install -g firebase-tools`, `firebase deploy …`).
- `crm/docs/rapport/rapport-crm-hermes360.md:140-145` : actions demandées (installer, autoriser l'adresse de M. Carlone, commencer les appels par la vague 1, envoyer les douze questions à Vocalcom, faire valider par un expert-comptable, vérifier sur Légifrance).
- `crm/docs/hermes-vocalcom.md:270` : « Envoyons les e-mails depuis nos messageries ».
- `sources/crm-reference-2026-11-04.md:12` : « Premier essai à prévoir sur données fictives, sans toucher à la production. »
- `sources/chatgpt-pages/2026-11-04-complement/audit-crm-carlone.md:70` et `carlone-offres-et-projets.md:67-69` : « Prochaine action : récupérer un modèle de fichier d'import et de retour » ; tester une campagne fictive.
- `interne/contexte-projet-carlone.md:11` (vérification ponctuelle) : passer le dépôt FinanceScope en privé.

## 9. Points d'audit

1. **Le CRM est un actif technique sans usage démontré.** Aucune donnée de suivi n'est versionnée, aucune pièce ne fait état d'un appel, d'un rendez-vous ou d'une vente ; le rapport au client dit pourtant « prêt à servir ». Tant que la collection « suivi » n'a pas été lue, la valeur commerciale du CRM est [IN]. La note B du 4 novembre montre le même schéma sur le CRM OLSEN (503 prospects tous « À faire »).
2. **Les chiffres annoncés sont exacts mais flatteurs.** 471 numéros, dont 60 % à confirmer et une seule date de vérification ; 60 entreprises avec interlocuteurs, sans ligne directe ; « 97 artistes » qui sont 38. Il faut présenter ces chiffres avec leur niveau de preuve.
3. **L'argument fiscal est surévalué.** L'« économie max » ignore le bénéfice et le taux réduit PME (`art_merge.py:19,129`). Le simulateur affiché pendant l'appel peut induire un prospect en erreur ; à corriger avant tout appel.
4. **La validité juridique du modèle n'est pas établie.** L'exposition en lieu tiers n'est pas prévue par le BOFiP (`PASSATION.md:35`) ; la structure vendeuse n'existe pas (`PASSATION.md:31`) ; le lien caché avec Le Vieux Relais (`PASSATION.md:49`) pose une question de loyauté commerciale. Sans ces trois points, aucune campagne ne peut démarrer.
5. **Le modèle d'exploitation est incohérent.** Le CRM a été conçu pour 2 à 4 associés qui appellent eux-mêmes ; le client parlerait d'externaliser à Quali Contact, dont on ignore l'outil. Le module Hermes360 a été développé avant de connaître cet outil et contre la recommandation de l'étude.
6. **Le risque RGPD est immédiat.** Si le dépôt FinanceScope est public, des centaines de numéros, d'e-mails et de profils LinkedIn sont exposés, dont des mobiles et messageries personnelles et des artistes particuliers. Il n'existe ni responsable de traitement, ni registre, ni mention d'information. La règle de purge à 3 ans n'est pas outillée. La promesse « Personne d'autre ne lit les fiches » est fausse dans ce cas.
7. **La sécurité de la version autonome est correcte pour la lecture, faible pour l'intégrité.** Écriture et suppression libres sur `/suivi` et `/reglages`, pas de validation, pas d'historique serveur, pas de sauvegarde automatique, code exécuté depuis Firestore sous la seule responsabilité du propriétaire, SDK copié (10.14.1) à mettre à jour à la main. Les adresses autorisées seraient écrites dans un dépôt potentiellement public.
8. **La propriété n'est réglée nulle part.** Code sur le compte de Mathys, copie chez Morgan, données issues de Pappers, du registre, d'annuaires et de LinkedIn, client simple utilisateur, travail réalisé avant contrat. Il faut un écrit sur la propriété, la licence et la réversibilité avant toute facturation.
9. **La maintenance est un coût caché.** Environ 645 fichiers, une page de 278 Ko, une chaîne de scripts dont le README est incomplet, des données qui vieillissent (comptes annuels, dirigeants, numéros), une dépendance aux quotas d'agents IA. Aucun coût ni responsable de maintenance n'est chiffré.
10. **Les preuves de qualité sont déclaratives.** Les relectures « défauts corrigés » et les 30 parcours Playwright ne sont pas versionnés ; aucun test n'est rejouable par un tiers.
11. **Hermes360 : beaucoup d'analyse, aucune réponse.** Aucun contact avec Vocalcom, « confirmé par Vocalcom » abusif, prix non confirmés. La question utile est le format d'échange de Quali Contact, pas l'achat de Hermes360.
12. **Chiffres stratifiés.** La passation empile des états successifs (54 → 185 → 342 → 388 → 437 → 461 → 471 numéros ; 96 → 57 cibles). Toute reprise doit dater ses chiffres et citer la révision (b53a81c), pas l'audit ChatGPT sur 18c2080.
13. **Dépendance aux personnes.** Le seul donneur d'ordre nommé est Mathys ; les associés-appelants ne sont pas identifiés ; la disponibilité réelle de Morgan pour Carlone n'est documentée nulle part (note B).
14. **Le CRM ne prouve pas une demande solvable.** Le CRM sert la vente d'œuvres de GianLuca Carlone, pas une prestation payée à Marwin. Le présenter comme « point de départ » de l'offre à 15 000 € HT par mois suppose une valeur que rien ne mesure encore. Premier critère proposé : 20 comptes appelés, avec taux de joignabilité, de rendez-vous et de vente mesurés [MM] avant tout élargissement.
