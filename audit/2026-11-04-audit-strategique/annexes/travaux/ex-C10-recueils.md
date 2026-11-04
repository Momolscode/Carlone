# C10-recueils — Lecture des recueils ChatGPT (conversations et Pages) — audit Carlone, 4 novembre 2026

Lecteur : C10-recueils. Lecture seule ; aucune action extérieure ; aucune modification du dépôt. Le client s'appelle **GianLuca Carlone** ; les citations qui portent « John-Lucas » ou « John Lucas » sont reproduites telles quelles et suivies de [sic, lire GianLuca].

**Abréviations de citation (à conserver lors de toute fusion) :**
- **R:n** = `interne/recueil-sessions-chatgpt-2026-11-04.txt:n`. Ce fichier est **identique octet pour octet** à `livrables/collecte-chatgpt-2026-11-04/CARLONE_Sources_retrouvees_v2.txt` (SHA-256 e6de2d20edf9b048…0615b765 identique, 1 548 lignes) : les numéros de ligne valent pour les deux.
- **V1:n** = `livrables/collecte-chatgpt-2026-11-04/CARLONE_Sources_retrouvees.txt:n` (version 1, 1 154 lignes, fins de ligne CRLF).
- **H2:n** = ligne n de l'extrait texte `scratchpad/sources-txt/recueil-et-sources-v2.txt`, qui reproduit `livrables/collecte-chatgpt-2026-11-04/CARLONE_Recueil_et_sources_v2.html` (identique à `interne/recueil-sessions-chatgpt-2026-11-04.html`, SHA-256 25a16da2…). Citer l'HTML d'origine avec sa section (§).
- **H1 §n** = section n de `livrables/collecte-chatgpt-2026-11-04/CARLONE_Recueil_et_sources.html` (synthèse version 1), extraite pour comparaison.

---

## 1. Pièces lues

| Chemin | Date de la pièce | Nature et auteur | Original ou copie | Ce qui n'a pas pu être lu |
|---|---|---|---|---|
| `interne/recueil-sessions-chatgpt-2026-11-04.txt` (R) | Collecte du 4 nov. 2026 (commit 7b46602, 17:37) | Recueil compilé par un assistant IA de collecte pour Morgan Olsen (outil non nommé) : 3 conversations ChatGPT + copies de 11 documents (Pages ChatGPT et documents Claude du dépôt). Lu intégralement (1 548 lignes). | Copie/export. Les blocs copiés sont identiques aux fichiers du dépôt (vérifié par comparaison : contexte, offre, complément, Page « offres et projets ») | 59 conversations refusées sur 219 (R:11) ; anciens messages des 3 conversations (« lecture parfois limitée aux derniers échanges », R:11) ; contenus Library (PDF, xlsx, vidéos, images) cités par lien seulement (ex. R:38, R:96-97, R:167, R:213) ; aperçus `page-preview` (R:245, R:279, R:307, R:311) ; références `chatgpt-content-reference` non résolues ; une réponse d'assistant manquante entre R:139 et R:141 |
| `livrables/collecte-chatgpt-2026-11-04/CARLONE_Sources_retrouvees_v2.txt` | 4 nov. 2026 | Même pièce que ci-dessus | Copie strictement identique (même SHA-256) | Idem |
| `livrables/collecte-chatgpt-2026-11-04/CARLONE_Sources_retrouvees.txt` (V1) | 4 nov. 2026 (première collecte) | Version 1 du même recueil | Copie/export ; comparée ligne à ligne après normalisation des fins de ligne | Couverture déclarée 153 lues / 66 refusées (V1:11) |
| `scratchpad/sources-txt/recueil-et-sources-v2.txt` (H2) — reproduit `CARLONE_Recueil_et_sources_v2.html` | 4 nov. 2026 | Synthèse rédigée par l'assistant de collecte (§ 1 à 9, H2:1-105) + annexe des textes sources (H2:106-1593) | Extrait texte d'une copie HTML ; l'annexe est identique en substance à R (seuls les intitulés de liens diffèrent) | Liens « Ouvrir la source » non suivis ; mêmes limites que R |
| `livrables/collecte-chatgpt-2026-11-04/CARLONE_Recueil_et_sources.html` (H1), section de synthèse seulement | 4 nov. 2026 | Synthèse version 1 | Copie HTML ; extraite pour comparer v1/v2 | Annexe non relue en détail (identique à V1) |
| `livrables/collecte-chatgpt-2026-11-04/README.md` et `manifest.json` | 4 nov. 2026 | Métadonnées de la collecte | Original du dépôt | — |

**Composition de R (provenance de chaque bloc) :**

| Lignes de R | Contenu | Date de la source | Nature |
|---|---|---|---|
| R:1-11 | En-tête de collecte | 4 nov. | Déclaration de couverture |
| R:14-84 | Conversation « Structurer Marwin Tech » (chatgpt.com/c/6adf6332…) | 31 oct.–4 nov. (Éclosion P0, poussée GitHub) | Conversation ChatGPT, derniers échanges |
| R:86-213 | Conversation « Bras robotique précis » (c/6ae7c762…) | ≈ 2 nov. | Conversation ChatGPT, derniers échanges |
| R:215-366 | Conversation « Travail pour Marwin Studio » (c/6add7150…) | ≈ 24-25 oct. (rappels créés pour le 26 oct.) | Conversation ChatGPT, derniers échanges |
| R:368-410 | Copie de `sources/index-integration-chatgpt-2026-11-04.md` | 4 nov. | Document du dépôt |
| R:413-576 | Copie de `interne/contexte-projet-carlone.md` | 4 nov. (Claude, « @Olsen Morgan ») | Document Claude |
| R:579-876 | Copie de `interne/offre-marwin-tech-remuneration-et-collaboration.md` | 2 nov. (Claude) | Document Claude |
| R:879-949 | Page ChatGPT « [John-Lucas] Carlone Offre et projets en Nièvre » | mise à jour 28 oct. 17:48 Z | Page ChatGPT |
| R:953-1101 | Page ChatGPT « Marwin Tech Accompagnement de [John-Lucas] Carlone » | mise à jour 29 oct. 13:33 Z | Page ChatGPT |
| R:1105-1153 | Copie de `interne/complement-chatgpt-2026-11-04.md` | 4 nov. | Document du dépôt |
| R:1157-1228 | Page « Audit du CRM Carlone et enrichissement des données » | 28 oct. 17:33 Z | Page ChatGPT (v2 seulement) |
| R:1231-1388 | Page « Marwin Tech Structure et offres de la société » | 29 oct. 07:11 Z | Page ChatGPT (v2 seulement) |
| R:1391-1495 | Page « Marwin Tech Méthode de consulting et audits » | 28 oct. 17:33 Z | Page ChatGPT (v2 seulement) |
| R:1498-1523 | Page « Marwin Studio Pilotage et mémoire » — **extraits** des seuls blocs citant Carlone, John-Lucas [sic] ou Quali Contact | 31 oct. 07:54 Z | Page ChatGPT, sélection (v2 seulement) |
| R:1526-1548 | Page « Marwin Audit du pilotage et des outils » — **extraits** | 25 oct. 10:18 Z | Page ChatGPT, sélection (v2 seulement) |

**Vérification complémentaire faite pour cet audit [FV] :** les comptages du CRM cités par la Page d'audit (R:1177-1186) ont été recomptés sur `site/companies.json` à la révision 18c2080 (historique intégré au dépôt) : 500 fiches, 500 SIREN, 471 téléphones dont 283 « à confirmer », 109 e-mails, 283 sites, 60 `contacts_admin`, 3 `actualites`, 2 `declencheur`, opposition 14 vrai / 19 faux / 467 vide, date de vérification du standard absente pour 499 fiches. Le fichier `crm/site/companies.json` de main (7b46602) a la même empreinte que celui de 18c2080 : **les données d'entreprises n'ont pas changé depuis le 28 octobre**.

---

## 2. Affirmations déterminantes

(R = `interne/recueil-sessions-chatgpt-2026-11-04.txt`)

| # | Affirmation | Code | Source | Remarque |
|---|---|---|---|---|
| 1 | Aucune pièce ne contient de propos directs de GianLuca Carlone : ses besoins, intentions et acquisitions sont toujours rapportés par Morgan (« selon Morgan », « Morgan précise »). | [FV] | R:443, R:887, R:894, R:945, R:961, R:1121 | Constat de lecture. Tout le volet « besoin client » repose sur une seule source indirecte. |
| 2 | Couverture déclarée de la v2 : 219 conversations, 160 lues, 59 refusées ; lectures parfois limitées aux derniers échanges ; seules 3 conversations accessibles citent Carlone. | [DR] | R:11 ; H2:7 | Le README de la collecte annonce ensuite 169 lues / 50 refusées : la v2 n'est pas le dernier état. |
| 3 | Morgan, vers le 25 oct. : « faut quand même qu'il me paye ce monsieur moi je peux lui faire une offre d accompagnement ». | [DR] | R:220 | Indique qu'aucune rémunération n'était convenue à cette date, alors que le CRM était déjà réalisé. |
| 4 | Morgan : GianLuca « a investis dans des bureaux pour du personnel ont en ferait partie ». | [DR] | R:220 | Première trace de l'offre de bureaux ; formulation qui évoque une intégration aux équipes du client (indice de salariat). |
| 5 | Morgan se projette à la « direction des opération de cosne cours sur Loire » ; l'assistant répond qu'une telle fonction « pourra se négocier » avec « John-Lucas » [sic, lire GianLuca]. | [DR] / [PR] | R:221 ; R:237 | Ambition de Morgan, aucune trace d'une offre de GianLuca pour ce poste. |
| 6 | Morgan : « Je préfère être prestataire ou salarié. Oui, mes pouvoirs fait en sorte d'être payé en plus par des missions de prestation. » | [DR] | R:248 ; reprise R:1299 | Choix non tranché ; il envisage salaire + prestations, montage que les documents Claude jugent exposé à requalification (R:508, R:706). |
| 7 | Morgan souhaite une DGX Spark (« déjà en matériel ça serait sympa ») ; la Page conclut que le besoin n'est pas établi pour le raccordement CRM. | [DR] / [HY] | R:220 ; R:1085 | Envie d'équipement antérieure à tout usage démontré. |
| 8 | Selon Morgan (25 oct.), GianLuca « prévoit d'engager Quali Contact » ; la construction des offres par Marwin est alors « mise de côté ». | [DR] | R:887 | Aucun contrat Quali Contact vu. |
| 9 | Le logiciel, le module et le format d'échange de Quali Contact sont inconnus ; aucun test d'intégration n'a été exécuté. | [IN] | R:929 ; R:931 ; R:949 ; R:1226 ; R:1545 | Toujours ouvert au 4 nov. (H2:99). |
| 10 | Les pages publiques de Qualicontact décrivent des campagnes et une activité de « relation donateurs » ; elles ne permettent pas d'identifier l'outil. | [DR] | R:931 (consultation ChatGPT du 25 oct.) | Adéquation d'un prestataire orienté collecte de dons à la vente d'œuvres aux entreprises non examinée. |
| 11 | GianLuca « a racheté, selon Morgan, un ancien bar restaurant hôtel avec cour pour en faire une galerie ». | [DR] | R:894 | Seule description du bâtiment de la galerie dans mes pièces ; aucune vérification immobilière (R:1121). |
| 12 | GianLuca « souhaite racheter « le M » » pour un cabaret. | [DR] | R:895 | Achat futur, pas acquis ; voir contradiction n° 9. |
| 13 | GianLuca « souhaite réunir des artistes et peintres dans la ville de Morgan ». | [DR] | R:896 | La ville n'est pas nommée. |
| 14 | GianLuca « vise les entreprises de la Nièvre ». | [DR] | R:893 | Cible commerciale du CRM. |
| 15 | Selon Morgan (28 oct.), GianLuca « souhaite déléguer le quotidien et envisage une disponibilité de vingt jours par mois, avec davantage de couverture si nécessaire ». | [DR] | R:945 | Seule trace d'une attente de disponibilité exprimée par le client. |
| 16 | Autre Page, même brief : c'est « Morgan [qui] envisage une implication de vingt jours par mois ». | [DR] | R:961 | L'auteur de l'attente des 20 jours diffère d'une Page à l'autre (contradiction n° 3). |
| 17 | Une version antérieure de l'offre était « limitée à quatre jours mensuels » ; elle est remplacée le 28-29 oct. | [PR] | R:961 | Passage de 4 jours à 20 journées-personnes en quelques jours, sans trace d'une demande du client. |
| 18 | Premier forfait proposé : « Cadrage et préparation du raccordement CRM » : entretien de 60 à 90 min, jusqu'à cinq pièces, un chantier prioritaire, un aller-retour ; livrables : feuille de route, fiche mission, cahier de passation ; prix non fixé. | [PR] | R:334 ; R:1469 | Offre d'entrée modeste, absente des documents de rémunération du 2 nov. |
| 19 | La méthode précise que ce forfait « n'élargit pas » le travail à l'ensemble des projets ; prospection, connecteur, productions marketing et lieux culturels sont des « lots distincts ». | [PR] | R:1471 | Contredit l'inclusion de ces volets dans l'abonnement de six mois (R:589, R:628-632). |
| 20 | Offre de six mois : 15 000 € HT/mois, 20 journées-personnes (140 h) cumulées pour l'équipe, acompte 7 500 € HT imputé sur le premier mois. | [PR] | R:977 ; R:1006-1010 ; R:593-599 | Aucun accord client (R:961, R:1093). |
| 21 | Variante : 40 journées-personnes (280 h) à 30 000 € HT/mois. | [PR] | R:1012 ; R:484-485 | Présentée comme « plein temps chacun ». |
| 22 | Le taux de 750 € HT par journée-personne est, dans la Page du 29 oct., une « hypothèse interne … base de négociation, à confirmer ». | [HY] | R:1018 | Le 2 nov., il devient « taux unique … on ajuste le périmètre, jamais le taux » (R:480, R:598, R:827) sans justification nouvelle. |
| 23 | Seul argument de prix avancé : deux salariés qualifiés coûteraient 1,6 à 1,9 fois leur net. | [ES] | R:834 ; R:876 | Ordre de grandeur « à simuler » (R:876) ; ne justifie pas 750 €. |
| 24 | Calendrier de paiement des mois 2 à 6 : « règlement sous sept jours après facture de fin de mois » (Page du 29 oct.). | [PR] | R:1011 | Contredit le paiement d'avance du 2 nov. (n° 25). |
| 25 | Calendrier de paiement des mois 2 à 6 : « d'avance, en début de mois » ; travail démarré à réception de l'acompte. | [PR] | R:489 ; R:599 ; R:773-775 ; R:838 | Divergence signalée mais non tranchée par la collecte (R:1131 ; H2:54). |
| 26 | Carlone est le « plus gros client de Morgan et Mathys ». | [DR] | R:419 | Alors qu'« au 30 octobre, aucune prestation n'avait été facturée » (R:609) : client principal sans chiffre d'affaires. |
| 27 | GianLuca « a racheté six bâtiments et l'ancienne affaire de Medhi ». | [DR] | R:438 | L'auteur précise : « je n'ai fait aucune recherche sur ces personnes » (R:443). |
| 28 | GianLuca « propose des bureaux, une bonne rémunération et envisage d'investir dans l'activité de Morgan et Mathys ». | [DR] | R:438 ; R:712 | Aucune trace écrite de GianLuca. Ne prouve aucune trésorerie disponible. |
| 29 | Morgan : « L'investisseur en question serait Carlone » (programme de peinture robotique). | [DR] / [HY] | R:104 | Confusion client / investisseur dès l'origine du projet robotique. |
| 30 | Programme R&D de 12 mois à 323 875 € HT, réserve comprise ; enveloppe investisseur de 325 000 €. | [ES] | R:99 ; R:111-118 | Classé « ancien scénario », à ne pas présenter (R:495, R:725, R:1129). |
| 31 | Le total 323 875 € est arithmétiquement exact ; le travail représente 77,1 % de la base hors réserve (199 850 / 259 100) ; la réserve vaut 25 % de cette base. | [FV] (recalcul) | R:113-118 ; R:205 | Le budget est surtout du temps humain, pas du matériel. |
| 32 | Hypothèse de 200 journées de robotique et d'IA à 650 €/jour (130 000 €). | [ES] | R:122 | Taux de spécialistes inférieur au taux Marwin de 750 € : incohérence de référentiel. |
| 33 | Démonstrateur ciblé : environ 25 000 € HT de matériel « avant le travail d'intégration ». | [ES] | R:134 | À rapprocher de la phase 1 STRATES « dans 10 000 € HT » (R:664) : périmètres différents, à ne pas confondre. |
| 34 | Le bras UFACTORY 850 avec contrôleur était affiché à 11 798,56 € TTC hors livraison. | [DR] | R:120 | Prix relevé par ChatGPT, date non précisée. |
| 35 | Aucun essai physique n'a validé STRATES ; la vidéo Higgsfield/Kling est « une visualisation IA, pas une démonstration du prototype ». | [FV] (déclaré par toutes les sources) | R:147 ; R:211 ; R:1141 ; H2:61 | Aucun résultat [MM] sur la robotique. |
| 36 | 19 réussites sur 20 ne prouvent pas 95 % de fiabilité (borne inférieure ≈ 78,4 %). | [ES] | R:199 | Calcul de l'audit, non refait ici. |
| 37 | Éclosion : contrôles numériques rapportés (aucune collision sur 61 positions) ; assemblage, résistance et moteur à éprouver ; script non exécuté lors de l'intégration. | [DR] | R:32 ; R:40 ; R:1139 | Aucun prototype physique. |
| 38 | CRM : 500 fiches, 500 SIREN, 471 téléphones dont 283 marqués « à confirmer », 109 e-mails, date de vérification du standard absente pour 499 fiches, opposition non renseignée pour 467. | [FV] (recompté sur 18c2080) | R:1177-1186 | 60 % des numéros sont à confirmer et la fraîcheur des données est inconnue. |
| 39 | « Aucun prospect, rendez-vous ou taux de conversion n'est encore constaté » (28 oct.). | [FV] (déclaré) / [IN] | R:937 | Aucun résultat commercial mesuré dans mes pièces. |
| 40 | « Aucun fichier de 500 prospects vérifié n'a été produit » (25 oct.). | [DR] | R:1548 | Antérieur à la livraison annoncée du CRM de 500 entreprises (R:469). |
| 41 | À la révision 18c2080, le suivi partagé du CRM reposait sur `window.claude.use("db")` ; hors de cet environnement, stockage local du navigateur. | [DR] | R:1194 | La version Firebase « qui ne dépend pas de Claude » (R:617) est postérieure (commit f9aa294 du 29 oct.) [FV]. |
| 42 | Jarvis : principes d'organisation seulement ; « ils ne déclarent pas un agent autonome ou une intégration déjà opérationnels ». | [PR] | R:1063-1067 ; R:994 | Démonstrateur prévu au premier mois (4 jours, R:641) sans périmètre précis. |
| 43 | Console « tour de contrôle » : 33 tests console et 20 tests du pilote mémoire passent, sur données fictives ; « le CRM réel reste à raccorder ». | [MM] (tests fonctionnels rapportés) | R:326 ; R:360 ; R:1352 ; R:1517 | Les tests ne mesurent ni gain de temps ni fiabilité en exploitation (R:1354). |
| 44 | Comparaison de productivité non réalisée ; cible proposée : −30 % de temps de préparation ; plafond d'essai 0 € et 2 h. | [HY] / [PR] | R:1354 ; R:1378-1380 | Aucun résultat d'essai consigné. |
| 45 | La version livrée de la console « emploie des canevas et des règles locales, sans génération par modèle d'IA ». | [DR] | R:1354 | L'« IA » vendue n'est pas encore dans l'outil testé. |
| 46 | Portefeuille de Morgan suivi dans la console : 24 dossiers ou périmètres, 22 dépôts, cinq films, huit missions. | [DR] | R:355 ; R:1517 ; R:1540 | Confirme la dispersion des activités (cf. note du 4 nov., partie B). |
| 47 | « Eaglemic, aussi appelé Michael Bach, est également un associé principal de Morgan et utilise @mtek_france. » | [DR] | R:1508 | Troisième « associé principal » absent de tous les autres documents de mes pièces ; enjeu de capital et de propriété. |
| 48 | Morgan écrit « moi et Matisse » à propos de la future société. | [DR] | R:249 ; R:1115 | Probablement Mathys (erreur de saisie) ; le complément refuse d'en déduire l'identité de l'associé. |
| 49 | Morgan veut ouvrir « la boutique et l'atelier d'impression 3D BOJ.ART » avec une personne que GianLuca connaît. | [DR] | R:975 ; R:1071 | Le contexte présente BOJ.ART comme le projet de Medhi (R:441) : propriété du projet ambiguë. |
| 50 | Morgan déclare avoir accès à un atelier d'environ dix imprimantes 3D ; ni propriété ni apport à Marwin ne sont établis. | [DR] | R:975 ; R:1073 ; R:1077 ; R:1332 | Le contexte l'attribue au « parc » de Medhi (R:441). |
| 51 | Lettre « Proposition à adresser à John Lucas » [sic, lire GianLuca] : « Vous m'avez expliqué vouloir développer vos projets sans avoir à en gérer chaque détail. » | [DR] | R:963-967 | Besoin rapporté par Morgan dans un brouillon ; envoi non établi. |
| 52 | La Page du 29 oct. exclut toute participation de GianLuca au capital et tout prêt de sa part. | [PR] | R:1097 | Le 2 nov., l'investissement est au contraire préparé comme sujet de négociation (R:720-729). |
| 53 | Délégation : « une absence de réponse ne vaut pas approbation » ; nouveaux contrats, recrutements, investissements réservés au client. | [PR] | R:1050-1057 | Le contrat du 2 nov. prévoit pourtant qu'un livrable non contesté dans le délai est « réputé accepté » (R:786). |
| 54 | Aucun engagement « 24 h/24 ou 30 jours/30 » avant organisation ; astreinte chiffrée séparément ; une disponibilité sur trente jours calendaires n'équivaut pas à trente journées de production. | [PR] | R:1013 ; R:1018 ; R:1059 | La mention des « trente jours » suggère qu'une attente de ce type a été exprimée, sans dire par qui. |
| 55 | Les économies d'automatisation servent à « réaffecter la capacité ou revoir le forfait » ; elles ne sont pas facturées comme heures fictives. | [PR] | R:1020 | Risque de baisse de prix à mesure de l'automatisation ; la valeur n'est pas rémunérée. |
| 56 | Objectif de 7 500 € nets chacun : suppose 30 000 € HT/mois pendant douze mois, alors que le contrat n'en couvre que six. | [ES] | R:497 ; R:698 ; R:701 | Simulation non validée par un expert-comptable (R:876). |
| 57 | Plancher : environ 10 300 € HT/mois pour 14 journées, calculé comme 123 332 € par an ÷ 12. | [ES] | R:691-694 ; R:828 | Recalcul : 10 277,67 € [FV arithmétique] ; repose sur douze mois de facturation. |
| 58 | « Mener les huit propositions de front demande plus de 20 journées par mois. » | [HY] | R:643 | Aucune estimation de charge par mission. |
| 59 | Réponse de Morgan à la ligne « part maximale des revenus venant de Carlone » : « 10 millions », réponse interrompue. | [DR] | R:543 | Sens inconnu ; révèle l'absence de seuil de dépendance décidé. |
| 60 | Le 4 nov., le dépôt FinanceScope/CRM-Carlone est public et contient 931 numéros, 206 e-mails, 63 profils LinkedIn. | [DR] | R:419 ; R:425 | Comptages de l'analyse du 2 nov. ; non revérifiés ici. |
| 61 | Le CRM, son historique et ses archives sont « maintenant intégrés dans crm/ du dépôt privé Carlone ». | [FV] | H2:32 (`CARLONE_Recueil_et_sources_v2.html` § 3) ; dossier `crm/` présent au commit 7b46602 | Contredit R:80 et R:1147 (« le CRM reste dans son dépôt »), devenus obsolètes deux minutes plus tard (commits b205005 puis 95de15f). |
| 62 | Huit rappels (26 oct.–4 nov., 15 h) et une veille chaque jeudi sont déclarés « actifs » ; toutes les étapes restent « À préparer » ; le premier jalon (rôles et disponibilité) reste ouvert. | [DR] | R:286-301 ; R:1315-1324 ; R:1388 | Au 4 nov., la disponibilité de chacun est toujours « à trancher » (R:534). |
| 63 | Les œuvres faites à la machine (impression 3D, bras peintre) sont « très probablement exclues » de la déduction 238 bis AB, qui vaut pour les achats faits avant le 31 déc. 2028. | [DR] | R:503-504 ; R:678 ; R:840 | Affirmation fiscale à faire valider ; la Page du 25 oct. cite l'article 238 bis (mécénat), un autre dispositif (R:914). |
| 64 | Licence n8n : une licence commerciale est requise si des personnes extérieures configurent les workflows (API, MCP, agent). | [DR] | R:1384 (vérifié par ChatGPT le 29 oct.) | Contrainte directe pour un « Jarvis » configurable par le client. |
| 65 | Aucun document signé, aucune facture, aucun paiement, aucune embauche ni transfert de pouvoir n'est établi. | [FV] (absence constatée dans mes pièces) | R:419 ; R:609 ; R:1093 ; R:1113 ; R:1356 | — |

---

## 3. Chiffres, engagements et dates

(R = `interne/recueil-sessions-chatgpt-2026-11-04.txt`)

### Rémunération et capacité de Marwin Tech

| Élément | Valeur | Code | Source |
|---|---|---|---|
| Version antérieure de l'offre | 4 jours par mois (montant non indiqué) | [PR] | R:961 |
| Forfait de cadrage d'entrée | Entretien 60-90 min, ≤ 5 pièces, 1 chantier, 1 aller-retour ; prix non fixé | [PR] | R:1469 |
| Formule de base | 15 000 € HT/mois ; 20 journées-personnes ; 140 h ; 6 mois = 90 000 € HT | [PR] | R:977 ; R:1008 ; R:593-596 |
| Renforcement | 30 000 € HT/mois ; 40 journées-personnes ; 280 h ; 6 mois = 180 000 € HT | [PR] | R:1012 ; R:593-596 |
| Taux journalier | 750 € HT/journée-personne (« hypothèse interne » le 29 oct. ; « taux unique » le 2 nov.) | [HY] puis [PR] | R:1018 ; R:480 ; R:598 |
| Journée-personne | 7 heures ; deux personnes une journée = deux journées-personnes | [PR] | R:1006-1007 |
| Acompte | 7 500 € HT, imputé sur le premier mois (= 10 journées-personnes) | [PR] | R:599 ; R:977 ; R:1009 |
| Solde du mois 1 | 7 500 € HT, fin du mois 1, sous 7 jours | [PR] | R:774 ; R:1010 |
| Mois 2 à 6 | 15 000 € HT/mois : d'avance (2 nov.) ou après facture de fin de mois sous 7 jours (29 oct.) | [PR] (contradictoires) | R:775 ; R:1011 |
| Premier mois réparti | Cadrage 6 j / 42 h ; CRM et campagne pilote 7 j / 49 h ; Jarvis 4 j / 28 h ; coordination 3 j / 21 h (total 20 j / 140 h, vérifié) | [PR] | R:636-641 |
| Plancher | ≈ 10 300 € HT/mois pour ≈ 14 journées (123 332 € / 12 = 10 277,67 €) | [ES] | R:691-694 ; R:828 |
| Ancre / cible / plancher | 30 000 € + pilote laboratoire / 15 000 € sur 6 mois / ≈ 10 300 € | [PR] | R:826-828 ; R:491 |
| Nets simulés par personne | ≈ 7 500 € (renforcement), ≈ 3 660 € (base sans réserve), 2 500 € (base avec réserve ou plancher) | [ES] | R:689-692 |
| Net par jour travaillé | ≈ 370 € (recalcul : 3 660 / 10 = 366 € ; 7 500 / 20 = 375 €) | [ES] | R:699 |
| Laissé dans Marwin | ≈ 3 900 €/mois, ≈ 46 750 €/an (base avec réserve) | [ES] | R:691 ; R:700 |
| Hypothèses du modèle | 30 000 € de frais/an ; foyer d'une part ; sans ACRE ni FRR ; 60 000 € nets + 33 332 € de cotisations et impôt | [ES] | R:694 |
| Scénario 180 000 € HT de CA/an | SARL IS 43 875 € ; SARL IR 42 272 € (51 408 € avec FRR) ; SAS IS 41 080 € (43 430 € avec FRR), nets par personne | [ES] | R:737-741 |
| SARL IR avec FRR | ≈ 4 280 €/mois au lieu de 3 660 € | [ES] | R:702 |
| Coût employeur d'un salarié | 1,6 à 1,9 fois le net | [ES] | R:706 ; R:834 |
| Option laboratoire | Pilote 90 jours ; 30 000 € HT dont 13 500 € d'honoraires (18 journées) ; matériel acheté par l'entité de GianLuca | [PR] | R:492 ; R:601 |
| Option création STRATES | Phase 1 ≈ 10 000 € HT dont 6 journées Marwin (4 500 €) | [PR] | R:493 ; R:664 |
| Pénalités de retard | Pénalités légales + 40 € forfaitaires ; travaux suspendus après une relance | [PR] | R:787 |

### Robotique, STRATES, Éclosion

| Élément | Valeur | Code | Source |
|---|---|---|---|
| Programme R&D 12 mois | 323 875 € HT (bras 10 500 ; capteurs et outils 26 000 ; travail 199 850 ; essais 22 750 ; réserve 64 775) ; enveloppe 325 000 € | [ES] | R:99 ; R:111-118 |
| Entrée du programme | 10 000 € pour mesures et cadrage | [ES] | R:99 |
| Journées de spécialistes | 200 j × 650 € = 130 000 € | [ES] | R:122 |
| Matériel du démonstrateur ciblé | ≈ 25 000 € HT, avant intégration | [ES] | R:134 |
| Bras UFACTORY 850 | 11 798,56 € TTC hors livraison | [DR] | R:120 |
| Critères du premier essai STRATES | Trait de 7 mm sur 10-15 cm ; largeur 6-8 mm sur 90 % ; débordement ≤ 1 mm | [PR] | R:660 ; R:163 |
| Planning STRATES | 6 semaines après accès au matériel | [PR] | R:165 |
| Format STRATES | 90 × 65 cm (audit) ou 90 × 56 cm (simulation) | [DR] (divergent) | R:472 ; R:540 |
| Fiabilité | 19/20 → borne basse ≈ 78,4 % | [ES] | R:199 |
| Part du budget | 77,1 % travail humain ; 0,87 % calcul GPU | [ES] (77,1 % vérifié) | R:205 |
| Éclosion P0 | Pétale 150 × 54 mm ; axe 3 mm ; socle 100 × 90 mm ; couple cible 0,08 N·m pour 35 g ; animation 8 s | [DR] | R:27-29 ; R:64 |
| Documents | Proposition STRATES 8 p. ; audit 12 p. ; dossier investisseur 23 p. ; budget 53 postes | [DR] | R:96-97 ; R:165 ; R:211 |

### CRM, Quali Contact, outils

| Élément | Valeur | Code | Source |
|---|---|---|---|
| CRM à la révision 18c2080 | 500 fiches / 500 SIREN ; 471 tél. dont 283 à confirmer ; 109 e-mails ; 283 sites ; 60 contacts admin ; 499 sans date de vérification ; opposition 14/19/467 | [FV] (recompté) | R:1177-1186 |
| Branche de travail | 621 fichiers ; la branche main ne contenait qu'un README | [DR] | R:1173 |
| Dépôt public (2 nov.) | 931 numéros, 206 e-mails, 63 profils LinkedIn | [DR] | R:425 |
| Autres comptages | 125 fiches d'appel ; 97 artistes et structures (onglet Culture) ; ancien Artefact à 100 entreprises | [DR] | R:430 ; R:469 |
| Prospection de départ proposée | 20 comptes qualifiés ; recette sur 10 entreprises fictives | [PR] | R:937 ; R:1218 |
| Console | 15 puis 33 tests console ; 20 tests pilote mémoire ; 106 tests (paquet 0.2.0) ; 5 cas fictifs | [MM] (rapportés) | R:326 ; R:360 ; R:1352 ; R:1516 |
| Langfuse Core | 29 $/mois | [DR] | R:1366 |
| DGX Spark | 64 ou 128 Go selon fabricant ; aucun prix | [DR] | R:1081 |
| Film R02 (Marwin Studio) | Devis 70 / plafond 80 crédits | [DR] | R:1514 |

### Dates et échéances

| Date | Fait ou échéance | Code | Source |
|---|---|---|---|
| 18 oct. 2026 | PDF « Propositions de collaboration » (8 missions) | [DR] | R:459 |
| 21 oct. | Dossier de Mathys « Le Vieux Relais & le M » | [DR] | R:458 |
| 25 oct. | Morgan : le client prévoit d'engager Quali Contact ; pages Qualicontact consultées | [DR] | R:887 ; R:931 |
| 26 oct.–4 nov. | Huit rappels de lancement, autour de 15 h | [DR] | R:286-297 ; R:1313 |
| Chaque jeudi dès le 29 oct. | Veille « innovation appliquée », vers 8 h | [DR] | R:301 ; R:1338 |
| 28 oct. | Dépôt CRM fourni par Morgan ; brief élargi (délégation, 20 jours) ; audit CRM | [DR] | R:898 ; R:945 ; R:1167 |
| 29 oct. | Offre « Accompagnement » 20 journées-personnes ; SAS privilégiée (dossier du 29) | [PR] | R:961 ; R:735 |
| 30 oct. | SARL à l'IS retenue comme référence ; aucune prestation facturée à cette date | [DR] | R:735 ; R:609 |
| 2 nov. | Offre Claude 15 000 / 30 000 € ; audit et proposition STRATES | [PR] | R:452 ; R:583 |
| 4 nov. | Dépôt CRM toujours public (16 h 19) ; aucun rendez-vous jusqu'au 6 nov. | [DR] | R:419 ; R:429 |
| 31 déc. 2026 | Échéance annoncée des aides régionales Bourgogne-Franche-Comté | [DR] | R:755 |
| 2027 | Galerie | [DR] | R:419 |
| 20 janv. 2027 | Application du règlement machines (UE) 2023/1230 | [DR] | R:511 |
| Mois 3 / mois 4 | Bilan ; recherche d'un deuxième client | [PR] | R:791 ; R:509 |
| 31 déc. 2028 | Fin annoncée du dispositif 238 bis AB | [DR] | R:503 |
| 31 déc. 2029 | Fin de la fenêtre FRR | [DR] | R:749 |

---

## 4. Contradictions et divergences

(R = `interne/recueil-sessions-chatgpt-2026-11-04.txt`)

| # | Sujet | Version A + source | Version B + source | Portée pour l'audit |
|---|---|---|---|---|
| 1 | Calendrier de paiement | Mois 2-6 « d'avance, en début de mois » (2 nov.) — R:599, R:775 | Mois 2-6 « règlement sous sept jours après facture de fin de mois » (29 oct.) — R:1011 | Trésorerie : écart d'environ 37 jours sur chaque échéance. Aucune version validée (R:1131, H2:54). |
| 2 | Déclenchement du travail | « Le travail démarre à sa réception [de l'acompte] » — R:489, R:773, R:838 | Acompte « à la commande après validation du contrat et du cadre d'encaissement » ; lancement « après formalisation du contrat » — R:977, R:1009 | Ordre contrat / immatriculation / acompte / démarrage non fixé ; Marwin n'est pas immatriculée (R:733). |
| 3 | Qui attend 20 jours par mois | GianLuca « envisage une disponibilité de vingt jours par mois » — R:945 | « Morgan envisage une implication de vingt jours par mois » — R:961 | On ne sait pas si l'attente de disponibilité vient du client ou de Morgan : la base de l'offre n'est pas un besoin établi. |
| 4 | Volume de la base | 20 journées-personnes cumulées pour l'équipe — R:961, R:1006 | « 20 jours par personne » envisagé, = 40 journées-personnes — R:945, R:1012 ; « un plein temps chacun » — R:485 | Facteur 2 sur le prix et la charge ; non tranché (R:1093). |
| 5 | Taille de l'offre au fil du temps | 4 jours/mois — R:961 ; forfait de cadrage borné — R:1469 | 20 puis 40 journées-personnes, + laboratoire 30 000 € + STRATES 10 000 € comme ancre — R:826 | Escalade de l'offre en une semaine (25 oct.–2 nov.) sans nouvelle demande documentée du client. |
| 6 | Périmètre de l'abonnement | Prospection, connecteur, marketing et lieux culturels = « lots distincts » — R:1471 ; refonte au-delà de la capacité = lot complémentaire — R:1034 | Volets Produire et Piloter de l'abonnement incluent CRM, campagnes, catalogue, Jarvis, établissements, séjours, événements — R:589, R:628-632 | Risque d'abonnement qui absorbe tout (DEMANDE § 4). |
| 7 | Investissement de GianLuca | « Cette offre ne prévoit ni participation … au capital ni prêt » — R:1097 | GianLuca « envisage d'investir » ; SAS si entrée au capital ; règles de négociation — R:426, R:438, R:720-729 ; « l'investisseur … serait Carlone » — R:104 | Mélange client / bailleur / investisseur ; l'investissement n'est attesté que par Morgan. |
| 8 | Forme juridique | SAS privilégiée (29 oct.) — R:735 ; aucune forme retenue par défaut — R:1274 | SARL à l'IS de référence (30 oct.) — R:426, R:735 | Recommandations successives, aucune décision des associés. |
| 9 | Statut du « M » | GianLuca « souhaite racheter « le M » » pour un cabaret — R:895 | CRM pensé pour « amener les entreprises au Vieux Relais et au M » — R:461 ; propriété non établie — R:574 | On ignore si le M est un lieu existant exploité, un achat en projet ou un tiers. |
| 10 | Biens de GianLuca | Un « ancien bar restaurant hôtel avec cour » racheté — R:894 | « Six bâtiments et l'ancienne affaire de Medhi » rachetés — R:438 | Patrimoine décrit différemment, toujours sur déclaration de Morgan ; ne prouve aucun budget (R:1121). |
| 11 | Lieu du CRM | « Le CRM reste dans son dépôt actuel » — R:80 ; « restent dans FinanceScope/CRM-Carlone » — R:393, R:1147 | « Maintenant intégrés dans crm/ du dépôt privé » — H2:32 ; vérifié (dossier `crm/` présent) | Données de prospects désormais dupliquées (dépôt privé + dépôt public non revérifié) : registre RGPD et suppression à prévoir. |
| 12 | Dépendance du CRM à Claude | Suivi partagé via `window.claude.use("db")` (rév. 18c2080, 28 oct.) — R:1194 | Version Firebase « ne dépend pas de Claude », « prête à installer » — R:617, R:469 | Écart chronologique (commit f9aa294 du 29 oct.) ; le suivi réellement utilisé est inconnu (R:1171). |
| 13 | Données du CRM | 471 téléphones, 109 e-mails (fichier versionné) — R:1180-1181 | 931 numéros, 206 e-mails, 63 profils LinkedIn (dépôt entier) — R:425 | Périmètres de comptage différents : à ne pas présenter comme un même indicateur. |
| 14 | CRM « livré » | « Aucun fichier de 500 prospects vérifié n'a été produit » (25 oct.) — R:1548 ; 283 numéros « à confirmer » — R:1180 | « Livré : 500 entreprises … 471 numéros » — R:469 ; « Prêt à servir » — R:613 | « Livré » ne veut pas dire « vérifié » ni « utilisé ». |
| 15 | Silence du client | « Une absence de réponse ne vaut pas approbation » — R:1057 | Livrable non contesté dans le délai « réputé accepté » — R:786 | Objets différents (autorisation / réception), mais la réception tacite doit être encadrée. |
| 16 | Statut de Morgan | « Prestataire ou salarié … payé en plus par des missions » — R:248 | Être salariés et prestataires du même client « expose à une requalification » — R:508, R:706 | Intention personnelle contraire au garde-fou retenu. |
| 17 | Associés de Marwin | Morgan et Mathys, « trois pôles, quatre personnes » — R:434-441 | « Eaglemic, aussi appelé Michael Bach, est également un associé principal » — R:1508 ; « moi et Matisse » — R:249 | Composition réelle du groupe inconnue ; risque sur le capital et la propriété du travail. |
| 18 | Rôle de chacun | « Morgan garde les arbitrages commerciaux et la validation du travail livré » — R:1407 | Morgan programme et prix ; Mathys technique et CRM — R:534, R:804 ; rôle de Mathys « tout comme moi » — R:543 | Gouvernance interne non écrite. |
| 19 | BOJ.ART | « BOJ.ART est son projet [Medhi] » — R:441 ; ses machines lui restent — R:670 | Morgan veut « ouvrir la boutique et l'atelier » avec Medhi ; « J'ai accès à un atelier d'environ dix imprimantes » — R:975 | Propriété du projet et des machines ambiguë. De plus, l'offre et la lettre citent encore BOJ.ART et Medhi (R:602, R:647-681, R:975, R:988, R:995), alors que la note du 4 nov. rapporte la décision de les retirer [DR]. |
| 20 | Laboratoire | « Le financement général du laboratoire n'est pas ajouté d'office » ; « aucun achat ni financement … n'est acté » — R:1077, R:1334 | Option laboratoire 30 000 € HT dans l'ancre de négociation — R:492, R:826 | L'exploratoire entre dans l'offre commerciale. |
| 21 | Taux journalier | 650 €/jour pour des spécialistes en robotique et IA — R:122 | 750 € HT/journée-personne pour Marwin, « jamais le taux » — R:480 | Le taux Marwin dépasse celui retenu pour des spécialistes dans leur propre budget, sans justification. |
| 22 | Client principal | « Plus gros client de Morgan et Mathys » — R:419 | Aucune prestation facturée au 30 oct. — R:609 | Dépendance commerciale sans revenu. |
| 23 | Format de STRATES | 90 × 65 cm (audit) — R:472, R:660 | 90 × 56 cm (simulation) — R:540 | Mineur, mais l'œuvre n'a pas de spécification arrêtée. |
| 24 | Couverture de la collecte | V1 : 153 lues / 66 refusées — V1:11 | V2 : 160 / 59 — R:11 ; README : 169 / 50 | Les recueils ne sont pas le dernier état ; leurs chiffres datent de leur constitution. |
| 25 | Fiscalité citée | Déduction art. 238 bis AB (achat d'œuvres) — R:503 | Art. 238 bis (mécénat), « dispositif distinct » — R:914 | À distinguer dans l'offre ; à faire valider. |

**Écarts entre la version 1 et la version 2 des recueils (constatés) :**
1. Texte : V1 et R sont identiques sur les lignes 1 à 1 154, à une ligne près : la couverture passe de « 153 lectures réussies, 66 refusées » (V1:11) à « 160 lectures réussies, 59 refusées » (R:11).
2. R ajoute les lignes 1155 à 1548 : cinq exports de Pages (audit CRM, structure et offres, méthode, pilotage, audit du pilotage), dont deux réduits aux blocs citant Carlone, « John-Lucas » [sic] ou Quali Contact (R:1504, R:1532), ce qui crée un biais de sélection.
3. Format : V1 en CRLF avec espaces de fin de ligne ; V2 en LF.
4. Synthèse HTML : la v2 ajoute « Cette seconde collecte a récupéré 7 lectures précédemment refusées et ajouté cinq exports de Pages » (H2:7) et « le CRM … est maintenant intégré dans crm/ » (H2:32) ; elle remplace « Aucun fichier n'a été envoyé au client ou ajouté au dépôt par cette collecte » (H1 § 8) par « Les nouveaux exports et ce recueil constituent le complément demandé pour le dépôt privé » (H2:86).
5. Aucune des deux versions ne corrige le nom du client, ne reflète la décision rapportée du 4 nov. de retirer Medhi/BOJ.ART, ni le dernier bilan de 169 conversations lues.
6. Les copies `interne/recueil-sessions-chatgpt-2026-11-04.{txt,html}` sont des doublons exacts de la v2 : elles n'apportent rien de plus.

---

## 5. Informations inconnues et questions

**Sur le besoin réel de GianLuca**
1. Qu'a dit GianLuca lui-même ? Existe-t-il un message, un compte rendu ou une note de sa main sur la délégation du quotidien, les 20 jours par mois, les bureaux ou l'investissement (R:945, R:961, R:438) ?
2. Les « vingt jours par mois » sont-ils une demande de GianLuca ou une proposition de Morgan (R:945 contre R:961) ? Parle-t-on de 20 journées pour l'équipe ou par personne ? Qui a évoqué une disponibilité sur « trente jours » (R:1018) ?
3. Quels problèmes GianLuca veut-il résoudre en priorité, et lesquels accepterait-il de payer ? La lettre « Vous m'avez expliqué… » (R:967) a-t-elle été envoyée, et qu'a-t-il répondu ?
4. La proposition « limitée à quatre jours mensuels » (R:961) a-t-elle été présentée au client ? À quel prix ? Le forfait de cadrage (R:1469) a-t-il été chiffré ou présenté ?

**Sur les entités et l'argent**
5. Quelle entité de GianLuca signe, paie et valide (dénomination, SIREN) ? Qui est son expert-comptable ?
6. Quels biens sont réellement détenus, et par quelle entité : l'ancien bar-restaurant-hôtel (R:894), « six bâtiments » (R:438), l'ancienne affaire de Medhi, le Vieux Relais, le M (R:574, R:895) ?
7. « Le M » est-il un lieu existant, un achat en projet, ou un établissement d'un tiers ?
8. Le CRM réalisé « sans facture » sera-t-il payé, offert ou cédé ? Qui en détient les droits et les données (R:807, R:862) ?

**Sur Quali Contact**
9. GianLuca a-t-il signé avec Quali Contact ? Pour quel périmètre, quelles campagnes, quel budget ? Quel logiciel, quel module, quel format d'import et de retour (R:949, R:1226) ?
10. Un prestataire dont les pages publiques décrivent la « relation donateurs » (R:931) est-il adapté à la vente d'œuvres aux entreprises de la Nièvre ?

**Sur Marwin Tech**
11. Qui sont les associés : Morgan et Mathys seulement, ou aussi « Eaglemic / Michael Bach » (R:1508) ? « Matisse » (R:249) désigne-t-il bien Mathys Couet ?
12. Combien de jours par mois Morgan et Mathys peuvent-ils réellement consacrer à GianLuca, compte tenu des 24 dossiers et 22 dépôts suivis (R:1517) et des autres projets de Morgan ?
13. Morgan veut-il être salarié de GianLuca, prestataire, ou les deux (R:248) ? GianLuca propose-t-il réellement un emploi ?
14. Les rappels et la veille hebdomadaire ChatGPT ont-ils produit des décisions (R:286-301) ? Le premier jalon « rôles et disponibilité » a-t-il été rempli (R:1388) ?
15. Que signifie la réponse « 10 millions » à la question sur la part maximale de revenus venant de GianLuca (R:543) ?

**Sur les outils et la robotique**
16. Quel suivi du CRM est réellement utilisé aujourd'hui (Artefact Claude, Firebase, aucun) ? Des appels ont-ils été passés ?
17. Le dépôt FinanceScope/CRM-Carlone est-il toujours public ? Les données dupliquées dans `crm/` ont-elles une base légale et une durée de conservation ?
18. Où est hébergée la « tour de contrôle » (domaine chatgpt.site) et quelles données y figurent ?
19. Qui possède l'atelier d'environ dix imprimantes 3D et à quelles conditions Morgan y accède-t-il (R:975, R:1332) ?
20. Que contiennent les 50 à 59 conversations non lues et les échanges anciens non restitués des trois conversations lues ? Pourquoi « John-Lucas » apparaît-il dans les réponses des assistants alors qu'aucun message visible de Morgan n'emploie ce nom ?

---

## 6. Par chantier

(R = `interne/recueil-sessions-chatgpt-2026-11-04.txt`)

**1. CRM et développement commercial.** GianLuca « vise les entreprises de la Nièvre » [DR] (R:893). CRM de 500 fiches et 500 SIREN, enrichi, avec 283 numéros sur 471 « à confirmer » et des dates de vérification presque toutes absentes [FV recompté] (R:1177-1186). L'audit du 28 oct. propose un lot de consolidation : dictionnaire de données, registre d'enrichissement, spécification d'échange, recette sur 10 entreprises fictives, prix non fixé [PR] (R:1216-1222). Proposition de commencer par 20 comptes qualifiés ; « aucun prospect, rendez-vous ou taux de conversion n'est encore constaté » (R:937). But initial du CRM : amener les entreprises au Vieux Relais et au M, puis vendre des œuvres avec avantage fiscal (R:461). Règles de prospection : coordonnées professionnelles, opposition, mention de l'émetteur (R:941, R:506). Données dupliquées dans `crm/` (H2:32) et dépôt public signalé (R:425).

**2. Quali Contact.** Selon Morgan, le client « prévoit d'engager Quali Contact » (25 oct.) [DR] (R:887). Cahier de raccordement proposé, dans les deux sens (offres et contacts vers l'outil ; résultats d'appel, rendez-vous et oppositions vers le CRM), avec critères de réception non testés [PR] (R:916-929). Logiciel, module et formats inconnus [IN] (R:931, R:949, R:1226). La note Hermes/Vocalcom ne prouve pas que Quali Contact utilise cet outil (R:1147, R:1226). Rappel du 3 nov. « CRM et Quali Contact » resté « À préparer » (R:1323). Le rôle de chacun dans la validation des offres présentées aux opératrices reste à fixer (R:912).

**3. Organisation et pilotage.** Brief rapporté : GianLuca veut déléguer le quotidien [DR] (R:945, R:961, R:967). Mission proposée : piloter le portefeuille, préparer les décisions, coordonner, livrer dans la capacité réservée [PR] (R:988-997). Démarrage proposé : inventaire en 10 jours, feuille de route à 90 jours, tableau de bord, revues à 30 et 90 jours (R:1026-1032). Règles de mandat écrites, plafonds, absence de réponse ≠ accord (R:1048-1057) ; pas de 24 h/24 ni de 30 j/30 sans organisation (R:1059). Morgan aspire à une « direction des opérations » à Cosne-Cours-sur-Loire [DR] (R:221). Méthode d'audit en 7 étapes et 5 états de mission, non éprouvée sur une mission réelle (R:1419-1457).

**4. Jarvis, mémoire et automatisations.** Jarvis = copilote « à construire progressivement » ; principes de journal, doublons, contrôle humain, arrêt ; aucun agent autonome opérationnel [PR] (R:1061-1067, R:971). Démonstrateur Jarvis de 4 jours au premier mois (R:641). Console privée avec module « Offres et missions » : 33 tests sur données fictives, règles locales sans modèle d'IA (R:351-360, R:1352-1354). Essai de productivité préparé (−30 % visé), non exécuté (R:1368-1380). Pilote mémoire : 20 tests ; reprise entre sessions et appareils à prouver (R:360, R:1546). Veille : n8n 3.0 en bêta, licence commerciale si des tiers configurent les workflows ; Langfuse à 29 $/mois (R:1366, R:1384). DGX Spark : option non justifiée à ce stade (R:1081-1085). Automatisations ChatGPT déclarées actives : 8 rappels, veille du jeudi, rappel quotidien Studio Marwin (R:286-301, R:1326).

**5. Marketing et contenus.** Morgan veut vendre « consultant, studio marketing » (R:220) ; pôle « Studio marketing » proposé (R:258, R:1250). Offre : supports commerciaux, communication et campagnes (R:969, R:993). Fiches d'offre versionnées pour les opératrices (R:902-910). Marwin Studio : films (R02), compte Instagram à créer par Morgan, aucune publication attestée (R:1513-1515) ; sans lien établi avec GianLuca.

**6. Galerie, œuvres et artistes.** Selon Morgan, GianLuca a racheté un ancien bar-restaurant-hôtel avec cour pour en faire une galerie [DR] (R:894) ; galerie annoncée pour 2027 (R:419). Catalogue de neuf offres pour vendre des œuvres aux entreprises, brouillon à valider par l'expert-comptable (R:470, R:620). Déduction 238 bis AB et exclusion probable des œuvres faites à la machine [DR à valider] (R:503-504, R:678) ; mise en garde de la Page du 25 oct. sur le mécénat (R:914). Questions sur les artistes, les œuvres disponibles et la structure qui vend (R:525-526). « Parcours commercial, catalogue, présentoirs, scénographie » proposés (R:995).

**7. Événements et vernissage.** GianLuca « souhaite réunir des artistes et peintres dans la ville de Morgan » [DR] (R:896). Vernissage « Strates » du 4 nov. : cinq temps, 21 idées, trois formats de 6 à 30 journées, honoraires « à fixer » (R:473, R:494) ; questions sur le lieu, la date, les invités, le budget (R:529). « Événements art et restauration » et « séjours des invités » parmi les huit missions du 18 oct. (R:459, R:632). Robot en public interdit sans intégrateur ni normes (R:511, R:680).

**8. Cabaret et autres lieux.** GianLuca « souhaite racheter « le M » » [DR] (R:895) ; « le cabaret tient-il toujours ? » (R:528) ; « le cabaret plus tard » (R:474). Dossier de faisabilité proposé (R:996). Le Vieux Relais et le M : propriété non établie, à ne pas citer dans la prospection (R:506, R:574). Bureaux proposés à Cosne-Cours-sur-Loire (zone FRR à vérifier) (R:220, R:522, R:716).

**9. Medhi et BOJ.ART.** Dossier investisseur « peinture robotique BOJ.ART » (R:94). Medhi : création, signature, atelier, parc d'impression, Jarvis ; garde ses œuvres et ses machines [PR] (R:668-672). Accord à trois à écrire avant de présenter STRATES (R:428, R:806). Morgan veut ouvrir BOJ.ART avec Medhi [DR] (R:975, R:1071) ; ni Jarvis, ni BOJ.ART, ni UNUM ne sont des apports à Marwin (R:1254, R:1115). Les pièces ne reflètent pas la décision rapportée du 4 nov. de retirer Medhi/BOJ.ART de l'offre.

**10. STRATES, Éclosion et créations.** STRATES : relief d'environ 90 × 65 cm peint au pinceau par un bras, phase 1 d'environ 10 000 € HT, exclusivité et films pour la galerie en contrepartie [PR] (R:472, R:493, R:660-674) ; aucun essai physique [FV déclaré] (R:211). Morgan recentre : « Carlone vend des œuvre d'art il est moins figurine » [DR] (R:139). Éclosion : fleur cinétique, étude numérique P0, animation de 8 s, non construite (R:23-64, R:1139). Questions de droits et d'éligibilité fiscale des œuvres faites à la machine (R:504, R:678).

**11. Laboratoire IA et robotique.** Souhait de Morgan d'un laboratoire de recherche appliquée « en parallèle » [DR] (R:1330) ; non opérationnel, financement non ajouté d'office (R:1077, R:1334). Option : pilote de 90 jours à 30 000 € HT, matériel possédé par l'entité de GianLuca [PR] (R:492, R:601, R:645). Programme R&D de 323 875 € classé ancien scénario (R:495, R:1129). DGX Spark : option non validée (R:1085, R:1143).

---

## 7. Erreurs d'identité

**Nom du client.** Aucune occurrence de « GianLuca », « Gianluca », « Gian Luca » ou « Jean-Luc » dans mes pièces [FV].

| Variante | Nombre | Emplacements (R = `interne/recueil-sessions-chatgpt-2026-11-04.txt`) |
|---|---|---|
| « John-Lucas Carlone » (nom complet erroné) | 7 dans R (+2 dans la synthèse HTML) | R:881, R:887, R:898, R:955, R:1121, R:1508, R:1523 ; H2:14, H2:33 |
| « John-Lucas » seul | 24 dans R | R:237, R:243, R:273, R:295, R:334, R:893, R:894, R:895, R:896, R:912, R:945, R:961, R:965 (« Bonjour John-Lucas »), R:988, R:999, R:1042, R:1063, R:1071, R:1097, R:1303, R:1356, R:1473, R:1504, R:1532 |
| « John Lucas » (sans trait d'union) | 1 | R:963 (titre « Proposition à adresser à John Lucas ») |
| « Carlone » seul | ≈ 85 comme nom de personne (132 occurrences de la chaîne « Carlone » au total, dont ≈ 39 dans des noms de dépôts ou de fichiers : FinanceScope/CRM-Carlone, Momolscode/Carlone) | Conversations (R:104, R:126, R:136, R:139, R:165, R:203, R:207) et documents Claude (R:415-876) |
| « M. Carlone » | 2 | R:551, R:552 |
| « ce monsieur » | 1 | R:220 (Morgan) |
| « l'investisseur » | 1 | R:104 (« L'investisseur en question serait Carlone ») |

**Totaux :** R et `CARLONE_Sources_retrouvees_v2.txt` : 31 « John-Lucas » + 1 « John Lucas » = **32 occurrences sur 32 lignes**. V1 : 24 + 1 = 25. Extrait HTML v2 : 33 + 1 = 34 (deux de plus dans la synthèse). Les noms de fichiers et titres de Pages copiés dans le dépôt (`carlone-offres-et-projets.md`, `marwin-offre-accompagnement.md`) portent la même erreur.

**Origine probable :** l'erreur se trouve dans les réponses des assistants et les Pages ChatGPT (25-31 oct.), jamais dans les messages visibles de Morgan, qui écrit « Carlone » ou « ce monsieur » (R:104, R:139, R:220). Les messages plus anciens n'ont pas été restitués : l'origine exacte est [IN]. Les documents Claude (R:415-876) n'utilisent que « Carlone ».

**Autres erreurs ou variantes de nom :**
- « Matisse » pour Mathys (probable) : R:249 ; reprise R:1115. « Mathys » : 29 occurrences.
- « Medhi » : 21 occurrences, toujours sous cette forme (aucun « Mehdi ») ; orthographe à confirmer auprès de l'intéressé.
- « Quali Contact » (39) / « Qualicontact » (1, R:931, nom du site) : même entité supposée.
- « Marwin Tech » (65) / « Marwin Studio » (3 : R:215, R:1500, R:1515) / « Studio Marwin » (R:1326) / « MARWIN TECH » (R:400) / « Marwin » seul : Marwin Studio semble désigner l'activité de films et Instagram de Morgan, distincte de Marwin Tech ; non clarifié.
- « BOJ.ART » (24) / « BOJART » (nom du dépôt, 3).
- « Eaglemic » = « Michael Bach » (@mtek_france) : R:1508.

---

## 8. Instructions trouvées dans les pièces

Aucune n'a été exécutée. Aucune instruction n'est adressée à un auditeur ; les pièces contiennent des demandes de Morgan à des assistants, des actions annoncées comme faites par ces assistants, et des consignes de travail.

| Type | Contenu | Source |
|---|---|---|
| Demandes de Morgan à ChatGPT | « fais moi cette ébauche » ; « Fais moi voir un visuel » ; « Anime la moi » ; « Pousse sur le github de Carlone tout ce qui lui concerne » | R:19, R:53, R:61, R:75 |
| Idem | Dossier investisseur ; visuels « state of the art » ; « vidéo higgfield » ; « Audit ce projet comme un ingénieur … 220 à son test de QI » | R:91, R:139, R:142, R:170 |
| Idem | « faut tu me crées des rappels » ; « Continue ta contribution » ; « je te laisse auditer tout ce qui à étais fais » | R:282, R:314, R:347 |
| Actions déclarées faites par des assistants | Poussée GitHub de 48 fichiers (commit b205005, existant [FV]) ; huit rappels et veille du jeudi « actifs » ; console déployée ; rappel quotidien Studio Marwin conservé | R:78-84 ; R:286-301 ; R:317-351 ; R:1326 |
| Liste de tâches (contexte du 4 nov.) | Passer FinanceScope/CRM-Carlone en privé ; immatriculer ; RC pro, compte pro ; accord à trois avec Medhi ; fixer le rendez-vous « argent » | R:425-430 ; R:808 |
| Consignes de négociation | Ancre / cible / plancher ; réponses types « S'il dit… » ; « ne pas lui faire signer le volet Cadrer avant le dépôt du dossier » d'aide régionale | R:822-841 ; R:809 |
| Brouillon de message au client | « Proposition à adresser à John Lucas » [sic, lire GianLuca], signée Morgan Olsen | R:963-984 |
| Consignes de diffusion | « ne pas remettre ce dossier au client » (dossier `interne/`) ; documents de rémunération à ne pas remettre | R:380 ; H2:94 |
| Consignes techniques | « imprimer uniquement le coupon d'alésages » ; lire `prototype-p0/LIRE_AVANT_ESSAI.txt` avant toute fabrication ; script `tools/restaurer-archives.py` | R:42 ; R:1139 ; R:410 |
| Consignes à des sessions ChatGPT | « ne pas … lancer une génération depuis la veille » ; « Aucun appel supplémentaire ou publication autorisé » | R:1512 ; R:1514 |
| Prochaines actions proposées | Bloc de 20 min avec Mathys ; récupérer le modèle d'import Quali Contact ; préparer la fiche d'entrée du premier audit | R:336 ; R:366 ; R:1228 ; R:1473 |

Point de vigilance : des automatisations ChatGPT (rappels, veille) sont déclarées actives sur le compte de Morgan. Leur état réel n'est pas vérifiable ici ; elles ne doivent pas être confondues avec des décisions.

---

## 9. Points d'audit

1. **Le besoin du client n'est documenté qu'au second degré.** Les seules informations sur ce que veut GianLuca viennent de Morgan, résumées par des assistants (R:887, R:945, R:961, R:967). Les deux Pages du même brief se contredisent sur l'auteur de l'attente des « vingt jours par mois » (R:945 contre R:961). L'hypothèse d'un pilotage global reste à tester avec lui.
2. **L'offre a grossi sans demande nouvelle documentée.** On passe de 4 jours par mois (R:961) et d'un forfait de cadrage borné (R:1469) à 20, puis 40 journées-personnes, plus laboratoire et STRATES comme ancre (R:826), entre le 25 oct. et le 2 nov. Les moteurs visibles sont les souhaits de Morgan (direction des opérations, DGX Spark, laboratoire, R:220-223, R:1330), pas des besoins exprimés par le client.
3. **Le taux de 750 € HT n'est pas justifié.** Le 29 oct., il était une « hypothèse interne … à confirmer » (R:1018) ; le 2 nov., il devient intangible (R:480). Le seul argument est un ratio salarié de 1,6 à 1,9 « à simuler » (R:834, R:876). Leur propre budget robotique valorise des spécialistes à 650 €/jour (R:122).
4. **Les revenus visés supposent une capacité irréaliste.** 7 500 € nets chacun exigent 40 journées-personnes facturées pendant douze mois (R:698), soit environ 240 jours facturés par personne et par an, sans temps pour l'administration, la prospection, les congés ou la maladie. Le contrat ne couvre que six mois (R:701). Le plancher (≈ 10 300 €/mois) est lui aussi calculé sur douze mois de facturation (R:694).
5. **La disponibilité réelle de Morgan et Mathys n'est fixée nulle part.** Le premier jalon « rôles et disponibilité », prévu pour le 26 oct., était toujours ouvert (R:1388) et l'est encore le 4 nov. (R:534). Pendant ce temps, la console suit 24 dossiers, 22 dépôts et cinq films (R:1517). Un « plein temps chacun » (R:485) n'est pas compatible avec cette dispersion.
6. **Les engagements de paiement ne sont pas cohérents.** D'avance contre fin de mois (R:599 contre R:1011) ; démarrage à l'acompte contre démarrage après contrat (R:489 contre R:977). Une société non immatriculée ne peut facturer l'acompte (R:733). Ce point est un préalable, pas un détail.
7. **Mélange de rôles du client.** GianLuca serait client, bailleur, employeur éventuel et investisseur (R:438, R:104, R:248). Morgan envisage salaire et prestations (R:248), ce que les documents eux-mêmes jugent exposé à requalification (R:508). La Page du 29 oct. excluait l'investissement (R:1097) ; le document du 2 nov. le négocie (R:720-729).
8. **Aucun résultat mesuré qui justifie la promesse de démultiplication.** Les tests (33 + 20 + 106) portent sur des données fictives et des règles locales « sans génération par modèle d'IA » (R:1354) ; la comparaison de productivité n'a pas été faite (R:1354, R:1380). Aucun prospect, rendez-vous ou vente n'est constaté (R:937). Jarvis n'existe pas comme agent opérationnel (R:1067).
9. **Qualité et conformité des données CRM.** 60 % des numéros sont « à confirmer », 499 fiches sur 500 n'ont pas de date de vérification et l'opposition est inconnue pour 467 (recompté, R:1180-1186). Les données sont désormais aussi dans `crm/` (H2:32), alors que le dépôt d'origine était public au 4 nov. (R:425). Avant toute campagne Quali Contact : base légale, oppositions, durée de conservation, sous-traitance (R:790, R:1548).
10. **Quali Contact est une dépendance non qualifiée.** On ne connaît ni le contrat, ni l'outil, ni le format (R:949). Ses pages publiques parlent de relation donateurs (R:931). La passerelle CRM ne doit pas être vendue comme livrable daté (R:1036).
11. **Biens et projets du client non vérifiés.** Galerie dans un ancien bar-restaurant-hôtel (R:894), six bâtiments (R:438), le M à racheter (R:895) : versions différentes, toutes de Morgan, sans aucune vérification (R:443, R:1121). Elles ne prouvent ni budget ni trésorerie.
12. **Gouvernance de Marwin incertaine.** Un troisième « associé principal », Eaglemic/Michael Bach (R:1508), n'apparaît dans aucun autre document ; « Matisse » (R:249) reste ambigu ; la répartition des rôles varie (R:1407 contre R:534). À clarifier avant tout capital, pacte ou cession de droits sur le CRM.
13. **Propriété de BOJ.ART et de l'atelier ambiguë.** Projet de Medhi (R:441) ou boutique à ouvrir avec Morgan (R:975) ? Atelier de « Morgan » (R:975) ou parc de Medhi (R:441) ? Les pièces citent encore Medhi et BOJ.ART dans l'offre et la lettre, malgré la décision rapportée de les retirer.
14. **Réception tacite.** La clause « réputé accepté » sans réponse (R:786) va à l'encontre du principe « l'absence de réponse ne vaut pas approbation » (R:1057) et de la DEMANDE (§ 8). Elle doit être encadrée : délai, liste de contrôle, interlocuteur nommé.
15. **Automatisation et prix.** La Page prévoit que les gains d'automatisation « permettent de … revoir le forfait » (R:1020). Sans rémunération de l'organisation et de la responsabilité, Marwin finance elle-même la baisse de son chiffre d'affaires.
16. **Affirmations fiscales et réglementaires non revalidées.** 238 bis AB jusqu'au 31 déc. 2028, exclusion des œuvres faites à la machine, contribution AMF de 8 000 €, FRR, ACRE, aides régionales (R:503-505, R:749-755) : déclarations d'archives à faire vérifier par des professionnels avec les sources officielles en vigueur. La Page du 25 oct. cite un autre article (238 bis, mécénat) (R:914).
17. **Robotique : estimations de budget fragiles.** 323 875 € dont 25 % de réserve et 77 % de travail humain (R:111-118, R:205) ; 25 000 € de matériel pour un démonstrateur (R:134) contre une phase 1 à 10 000 € (R:664). Aucun devis ni essai physique (R:122, R:211). « L'investisseur … serait Carlone » (R:104) n'est appuyé par aucune pièce.
18. **Les recueils ne sont ni complets ni neutres.** Couverture partielle (160/219 en v2, 169/219 au dernier bilan), lectures limitées aux derniers échanges (R:11), deux Pages réduites aux blocs qui citent Carlone (R:1504, R:1532), une réponse d'assistant manquante (R:139-141), documents Library non lus. Le nom du client y est faux 32 fois. Ils doivent être cités comme copies d'archives, pas comme preuves.
19. **Licences et coûts récurrents des automatisations non intégrés au prix.** Licence n8n en cas de configuration par le client (R:1384), Langfuse (R:1366), abonnements (cf. note du 4 nov. : prélèvements en échec), DGX Spark (R:1085) : aucun coût complet ni propriétaire du matériel n'est fixé.
20. **Signal d'alerte sur l'exposition au client.** « Plus gros client » sans facture (R:419, R:609), part maximale de revenus « 10 millions » (R:543), recherche d'un deuxième client repoussée au quatrième mois (R:509) : la dépendance à GianLuca est déjà forte avant toute signature.
