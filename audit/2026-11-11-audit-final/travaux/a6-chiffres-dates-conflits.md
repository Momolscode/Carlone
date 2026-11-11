# Audit final — chiffres, dates, durées, comptes et références de droit : les conflits

Document interne — ne pas transmettre à GianLuca Carlone · 11 novembre 2026

Rapport de l’agent a6 pour le coordinateur de l’audit final (`audit/2026-11-11-audit-final/travaux/BRIEF-AUDIT-FINAL.md`). Angle : un même fait doit avoir une seule valeur dans tout le dossier. Ce rapport ne modifie aucun fichier existant et ne tranche aucune décision ouverte ; il est accompagné de `interne/rendez-vous/2026-11-11-referentiel-chiffres-dates-mots.md`.

## 1. En bref

- **56 constats** dans 16 conflits : **1 bloquant avant vendredi**, **32 importants**, **23 mineurs**. Aucun ne touche le prix, la validité ni les dates de l’offre. Une quinzaine d’autres écarts, vus pendant l’audit, ont été corrigés entre-temps par d’autres relectures (§ 6).
- **Ce qui tient partout** : 6 500 € hors taxes, soit 7 800 € toutes taxes comprises ; moitié à la commande ; trois à quatre semaines ; essai de huit semaines au plus ; offre valable jusqu’au jeudi 31 décembre 2026 ; démarrage visé début janvier 2027 ; 36 diapositives, 28 dans le fil, 32 minutes ; douze fiches, onze écrans, sept formules, quatre niveaux ; tous les jours de la semaine cités tombent juste ; toutes les références de droit et tous les tarifs publics des documents clients concordent avec les notes vérifiées (§ 7 et 8).
- **Bloquant tant que ce n’est pas constaté** : la diapositive `decision` disait « Un bon de commande d’une page » (le projet en fait trois) ; sa source a été corrigée pendant l’audit, mais la page publiée et la copie hors connexion restent à republier et à relire (C1).
- **À décider jeudi, hors des cases V1 à V14** : une seule règle pour le solde (C5) ; la date des statuts et le choix de l’avocat, dont dépend « commande signée avant la mi-décembre » (C12).
- **Avant tout envoi** : la proposition version client, qui garde le vocabulaire et les « trois suites » du 9 novembre (C7) ; les sept jours « ni demandé ni reçu » (C6) ; l’annexe et ses montants sans source (C15).
- **Pour la cohérence de ce qu’il verra** : la date de la mesure de METR (C4) ; la galerie en ligne en 2027 ou en 2028 (C8) ; trois ou quatre étapes (C9) ; quatre ou cinq questions (C10) ; l’ADAGP (C11).

## 2. Périmètre et méthode

- **Lu** : tous les fichiers Markdown du 10 novembre de `pour-carlone/` (offre, développement, douze fiches, cabaret et commerces, cadrage, suites, LISEZ-MOI de la maquette et de la version 12) ; le texte des 36 diapositives, de la maquette et des deux classeurs (extraits du bloc-notes de session, recoupés avec `pour-carlone/presentation-ia/2026-11-10-version-12-projet/project/slides/` et `pour-carlone/maquettes/2026-11-10-ecrans-d-exemple/index.html`) ; `interne/rendez-vous/` et `interne/decisions/` ; le sommaire `audit/2026-11-10-preparation-des-livrables/README.md` ; `REPRISE-2026-11-10.md`, partie « État le plus récent ». En plus, parce qu’ils sont apparus pendant l’audit : les pièces datées du 11 novembre de `interne/rendez-vous/` et de `pour-carlone/offre-cadrage/`. Le dossier `crm/` n’a pas été ouvert ; aucune commande git ; aucune recherche en ligne.
- **Méthode** : recherche par familles de motifs (montants ; durées ; dates et jours de la semaine ; comptes ; références de droit ; sources chiffrées), puis comparaison des occurrences. Les jours de la semaine, les sommes et les nombres de pages ont été recalculés. Pour un fait de droit ou un chiffre externe, la valeur de référence est celle de la partie « Vérification du 10 novembre 2026 » de la note `k…` correspondante ; pour l’offre, la page d’offre, puis le bon de commande, puis la feuille de décisions (brief, § 4).
- **État des fichiers** : d’autres relectures corrigeaient les documents internes pendant cet audit. Les lignes citées sont celles des fichiers le 11 novembre 2026 à 00 h 10 (heure de la machine de travail), au moment où ce rapport a été généré : chaque « texte actuel » y a été retrouvé mot pour mot, avec les espaces ordinaires des sources. Les écarts que ces relectures ont corrigés entre-temps sont listés au § 6.
- **Colonne « Fait »** : « non » : correction à faire, sans décision à prendre ; « à décider par les associés » : la correction dépend d’un choix qui leur revient ; « à vérifier par le coordinateur » : hors de portée de cet audit.

## 3. Conflits bloquants avant vendredi

**C1. La longueur du bon de commande, dite à l’écran : « d’une page ».** Fait foi : le projet de bon de commande lui-même, qui tient en trois pages avec ses conditions (rendu `md2pdf --compact` refait pour cet audit : PAGES=3 ; le bon seul, sans ses conditions : 2), et la page d’offre, qui dit « un bon de commande et ses conditions ». Pendant l’audit, la source de la diapositive `decision` a été corrigée (écran et note), comme le texte d’orateur, l’antisèche et la feuille de décisions. Ce que GianLuca Carlone verra vendredi, c’est la page publiée ou sa copie hors connexion : le dépôt ne dit pas qu’elles ont suivi.

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C1.1 | bloquant avant vendredi | Page privée de la présentation (adresse dans `audit/2026-11-10-preparation-des-livrables/README.md`, § 1) et copie hors connexion à préparer pour vendredi | Les sources `decision.html` et `cover.html` ont été corrigées dans le dépôt pendant l’audit ; rien n’y atteste que la page publiée et la copie hors connexion portent ces corrections. Tant que ce n’est pas constaté, l’écran peut encore dire « Un bon de commande d’une page » pendant que l’orateur dit autre chose | Republier depuis le dépôt, puis relire à l’écran la diapositive 26 : « Un bon de commande et ses conditions. Rien ne vous engage avant de le signer. » ; refaire ensuite la copie hors connexion | à vérifier par le coordinateur (page en ligne, hors de portée de cet audit) |
| C1.2 | mineur | `interne/rendez-vous/2026-11-11-presentation-texte-des-36-diapositives.md`, l. 169 | Copie de travail du texte des diapositives : elle porte encore l’ancien texte de `decision` et de `cover` | Relancer `outils/2026-11-11-dossier/extraire-le-texte-de-la-presentation.py` (aucune retouche à la main) | non |

## 4. Conflits importants

**C2. La règle par défaut de vendredi : quelles cases vides imposent « écran seulement ».** Fait foi : la feuille de décisions, partie « Avant vendredi 13 novembre » (« si une case de V1 à V5 reste vide jeudi soir, la présentation est montrée à l’écran seulement »), référence pour ce qui est à décider. L’antisèche et le texte d’orateur disaient « V2 à V5 » ; ils ont été corrigés le 11 novembre. Reste le sommaire.

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C2.1 | important | `audit/2026-11-10-preparation-des-livrables/README.md`, l. 5 | Le sommaire, point d’entrée du dossier, donne « V2 à V5 » ; la règle écrite est « V1 à V5 » | « Sans les préalables (feuille de décisions, V2 à V5), la présentation est montrée à l’écran seulement » → « Si une case de V1 à V5 reste vide (feuille de décisions, règle par défaut), la présentation est montrée à l’écran seulement » | non |

**C3. Le délai des écrits après le rendez-vous : « sous deux jours ».** Fait foi : la feuille de décisions, « Priorités » (premier envoi possible : jeudi 19 novembre 2026) et V10 (délai à fixer jeudi) ; depuis le 11 novembre, le texte d’orateur (§ 4), l’antisèche et la liste du jour J disent : on écrit dans les deux jours, on n’envoie qu’une fois la liste avant tout envoi cochée. Trois restes de « sous deux jours ».

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C3.1 | important | `interne/decisions/2026-11-10-feuille-de-decisions.md`, l. 99 | Décision n° 13 : une réponse écrite au client « sous deux jours » partirait avant le premier envoi possible | « réponse écrite sous deux jours, jamais en séance » → « réponse écrite dans le délai fixé en V10 (pas avant le premier envoi possible), jamais en séance » | non |
| C3.2 | important | `interne/decisions/2026-11-10-feuille-de-decisions.md`, l. 26 | V10 : la case « sous deux jours » reste proposée alors que la recommandation de la même ligne l’écarte | « ☐ sous deux jours ☐ autre délai : ……… » → « ☐ après relecture par l’avocat, au plus tôt le jeudi 19 novembre ☐ autre délai : ……… » | à décider par les associés |
| C3.3 | important | `interne/rendez-vous/2026-11-10-reponses-aux-objections.md`, l. 7 | Règles de réponse : même délai, que la ligne 17 du même document corrige déjà | « réponse écrite sous deux jours, jamais en séance » → « réponse écrite dans le délai fixé en V10, jamais en séance » | non |
| C3.4 | mineur | `interne/rendez-vous/2026-11-10-convaincre-de-miser-sur-nous.md`, l. 36 | Le compte rendu d’après rendez-vous est un écrit au client : il ne part pas avant la liste avant tout envoi (texte d’orateur, § 4) | « un compte rendu sous 24 heures ouvrées » → « un compte rendu écrit sous 24 heures ouvrées (après vendredi : envoyé une fois la liste avant tout envoi cochée) » | non |

**C4. La mesure de METR : une seule phrase, une seule source, une seule date.** Fait foi : la note `k13f`, partie « Vérification du 10 novembre 2026 » (contrôle n° 13 et phrase sûre n° 5) : doublement environ tous les sept mois depuis 2019, confirmé sur la page de METR du 29 janvier 2026 ; la première publication est de mars 2025 (arXiv 2503.14499 ; audit du 9 novembre, note `r3`). Les deux dates sont justes ; le dossier en cite tantôt l’une, tantôt l’autre. La phrase du brief (« la durée des tâches que les meilleurs agents d’IA réussissent une fois sur deux ») est celle du texte d’orateur depuis le 11 novembre.

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C4.1 | important | `pour-carlone/presentation-ia/2026-11-10-version-12-projet/project/slides/evolution.html`, l. 9 | À l’écran : « METR, 2025 » ; la fiche 12 date la même mesure du 29 janvier 2026 | « (METR, 2025) » → « (METR, 2025, mise à jour le 29 janvier 2026) » (ligne plus longue : à contrôler au rendu de la diapositive) | non |
| C4.2 | important | `pour-carlone/presentation-ia/2026-11-10-version-12-projet/project/slides/evolution.html`, l. 11 | Note de l’orateur : même date seule | « publiée en 2025, est nette » → « publiée en 2025 et mise à jour en janvier 2026, est nette » | non |
| C4.3 | important | `pour-carlone/developpement/2026-11-10-votre-interet-a-travailler-avec-nous.md`, l. 5 | Page « Votre intérêt » : même date seule | « … METR en 2025 » → « … METR en 2025, mises à jour le 29 janvier 2026 » | non |
| C4.4 | important | `pour-carlone/fiches/2026-11-10-fiche-12-les-enjeux-de-l-ia-pour-vous.md`, l. 11 | Fiche 12 : autre date, et autres mots (« longueur », « un agent d’IA ») que la phrase de référence | « la longueur des tâches qu’un agent d’IA réussit seul une fois sur deux double environ tous les sept mois depuis 2019 (METR, 29 janvier 2026) » → « la durée des tâches que les meilleurs agents d’IA réussissent une fois sur deux double environ tous les sept mois depuis 2019 (METR, 2025, mise à jour le 29 janvier 2026) » | non |
| C4.5 | mineur | `pour-carlone/developpement/2026-11-10-annexe-comparaisons-et-calculs.md`, l. 48 | Annexe : mêmes mots divergents ; ses dates (29 janvier et 19 mai 2026) couvrent deux mesures et sont justes | « la longueur des tâches qu’un agent d’IA réussit seul une fois sur deux » → « la durée des tâches que les meilleurs agents d’IA réussissent une fois sur deux » | non |

**C5. Le solde : dû « à la remise », « à la réception », « sous huit jours » ou « au plus tard trente jours après la remise ».** Fait foi, selon l’ordre du brief : la page d’offre (« moitié à la remise du dossier »), reprise à l’identique par la diapositive `proposition`, la fiche 10, l’antisèche, le texte d’orateur et la page sur les suites ; puis le bon de commande pour les clauses. Or le bon dit autre chose, et se contredit : huit jours après la facture, c’est avant la fin des dix jours ouvrés laissés pour les réserves. Le sommaire du 10 novembre le signale déjà (« une seule règle pour le solde ») ; ce n’est dans aucune case V1 à V14.

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C5.1 | important | `pour-carlone/offre-cadrage/2026-11-10-projet-de-bon-de-commande.md`, l. 40 | Le bon fait partir le solde de la réception (signée, avec dix jours ouvrés de réserves), la page d’offre de la remise | Deux voies. A, garder la page d’offre : « Solde, moitié à la réception du dossier » → « Solde, moitié à la remise du dossier ». B, garder le bon : écrire « à la réception du dossier » dans la page d’offre, la fiche 10, la diapositive `proposition` et sa note, l’antisèche et le texte d’orateur | à décider par les associés |
| C5.2 | important | `pour-carlone/offre-cadrage/2026-11-10-projet-de-bon-de-commande.md`, l. 73 | Trois délais pour le même paiement dans la même pièce : « sous huit jours » (§ 5), dix jours ouvrés de réserves, trente jours (condition 4) | Une seule phrase, à arrêter avec l’avocat, par exemple : « La facture du solde est payable sous huit jours après la réception ; sans réserve écrite dans les dix jours ouvrés, la réception est acquise, et le solde est dû au plus tard trente jours après la remise. » | à décider par les associés |
| C5.3 | important | `pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md`, l. 91 | La proposition suit le bon, pas la page d’offre | À aligner sur la voie retenue (A : « Solde, moitié à la remise du dossier, payable sous huit jours ») | à décider par les associés |

**C6. Les sept jours sans paiement : « demandé » ou « demandé ni reçu ».** Fait foi : la note `k1b`, « Vérification du 10 novembre 2026 », correction n° 6 et phrase sûre (« Aucun paiement n’est demandé ni reçu pendant les sept jours qui suivent la signature », code de la consommation, art. L221-10) ; le bon de commande et le projet de formulaire de rétractation l’écrivent ainsi.

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C6.1 | important | `pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md`, l. 93 | La proposition ne vise que le paiement demandé | « aucun paiement n’est demandé pendant les sept jours qui suivent la signature » → « aucun paiement n’est demandé ni reçu pendant les sept jours qui suivent la signature » | non |
| C6.2 | important | `pour-carlone/fiches/2026-11-10-fiche-10-travailler-avec-nous.md`, l. 34 | La fiche 10 aussi | « Aucun paiement n’est demandé dans les sept jours suivant la signature. » → « Aucun paiement n’est demandé ni reçu pendant les sept jours qui suivent la signature. » | non |

**C7. La proposition de cadrage, version client : ce qui suit le cadrage, et quelques mots.** Fait foi : la page d’offre (« une seule à la fois : un essai de huit semaines au plus, commandé à part, avec son prix ») et le brief, § 4 (essai « sur une seule tâche, mesurée avant et après » ; suivi régulier seulement après un essai réussi ; cession « une fois le prix dû payé » ; l’administratrice « gère tout l’administratif »). La proposition reprend le texte du 9 novembre : elle n’a pas suivi. Elle ne se laisse pas vendredi (V2) ; elle part au plus tard le vendredi 27 novembre.

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C7.1 | important | `pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md`, l. 114 | Trois « suites possibles », dont un « pilotage » de deux mois proposé sans essai préalable, alors que la ligne 117 de la même pièce ne l’admet qu’après un essai concluant ; « deux mois » dépasse « huit semaines au plus » | Réécrire le § 3 sur le modèle de la fiche 10 (« Notre méthode ») ; à défaut : « **(b) Pilotage** \| Deux mois : » → « **(b) Suivi de vos projets, à l’essai** \| Huit semaines au plus : » | à décider par les associés |
| C7.2 | important | `pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md`, l. 109 | « un seul processus » au lieu de « une seule tâche, mesurée avant et après » | « sur un seul processus, sans reconduction automatique » → « sur une seule tâche, mesurée avant et après, sans reconduction automatique » | non |
| C7.3 | important | `pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md`, l. 117 | « pilotage régulier » : le seul nom retenu est « suivi régulier » (feuille de décisions, n° 16 et 21) | « Un pilotage régulier ne vient qu’après un essai concluant » → « Un suivi régulier ne vient qu’après un essai concluant » | non |
| C7.4 | important | `pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md`, l. 105 | Cession « au paiement du solde » : le cas de l’arrêt manque | « Ces documents appartiennent à votre société au paiement du solde » → « Ces documents appartiennent à votre société une fois le prix dû payé (le solde ; en cas d’arrêt, l’acompte) » | non |
| C7.5 | important | `pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md`, l. 26 | « coordonne tous vos projets » (aussi lignes 11 et 34) : le fait rapporté le 10 novembre au soir est qu’elle gère tout l’administratif | « Une administratrice coordonne tous vos projets. » → « Votre administratrice gère tout l’administratif de vos projets. » ; lignes 11 et 34 : même verbe à remplacer (« la personne qui gère l’administratif de vos projets » ; « si votre administratrice gère déjà l’administratif ») | non |
| C7.6 | mineur | `pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md`, l. 21 | Date donnée comme comprise ; la fiche 1 et le questionnaire laissent ouvert « galerie ouverte ou non » | « Prévue pour 2027 dans un ancien bar-restaurant-hôtel avec cour » → « Prévue pour 2027, d’après nos échanges (à confirmer), dans un ancien bar-restaurant-hôtel avec cour » | non |
| C7.7 | mineur | `pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md`, l. 167 | Première « prochaine étape » : un rendez-vous « [date à fixer] », alors qu’il a lieu le vendredi 13 novembre | À l’envoi : « 1. Notre rendez-vous du vendredi 13 novembre 2026 a servi à corriger ce résumé ; un second échange reste possible, chez vous ou à distance : [date à fixer]. » | à décider par les associés |
| C7.8 | mineur | `pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md`, l. 60 | « Douze fiches » désigne ici les fiches d’inventaire du cadrage ; ailleurs, « les douze fiches » sont les fiches thématiques 1 à 12 | « Douze fiches courtes au plus » → « Douze fiches d’inventaire au plus » | non |
| C7.9 | mineur | `pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md`, l. 117 | « renouvelables » ; la diapositive `etapes` et le brief disent « renouvelées par écrit » (même mot à corriger dans la fiche 10, ligne « Un suivi régulier ») | « renouvelables par écrit » → « renouvelées par écrit » | non |

**C8. Les horizons : une même idée, deux dates.** Fait foi : pour les années, la page « Une ambition pour votre établissement », à laquelle renvoie la diapositive `ambition` ; pour la règle, le brief (horizons 2027, 2028, 2030 ; colonne « Quand ? » : essai, ensuite, plus tard) et la fiche 11, qui dit comment les deux se concilient (« plus tard, sans date promise ; dans notre ambition, d’ici 2030 »). Aucun agent ne tranche une date de la vision : chaque ligne est une proposition.

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C8.1 | important | `pour-carlone/developpement/2026-11-10-une-ambition-pour-votre-etablissement.md`, l. 12 | La galerie en ligne : 2027 ici ; 2028 sur la diapositive `avenir` (« 2028 — Galerie, suites et cabaret en ligne »), dans sa note et dans le texte d’orateur ; « ensuite, une fois les droits réglés » dans la fiche 6 | Le moins coûteux : « sans quitter la galerie \| 2027 \| » → « sans quitter la galerie \| 2028 \| » (la diapositive, déjà publiée, ne change pas) | à décider par les associés |
| C8.2 | important | `pour-carlone/presentation-ia/2026-11-10-version-12-projet/project/slides/avenir.html`, l. 28 | Les partenaires : 2028 dans la note de `avenir` et le texte d’orateur ; 2030 dans la page « Une ambition » (« Le réseau de vos partenaires ») ; « plus tard, sous conditions » dans la fiche 6 | « présents en ligne, vos partenaires accompagnés. » → « présents en ligne. » (même retrait dans le texte d’orateur, diapositive 22) | à décider par les associés |
| C8.3 | important | `pour-carlone/developpement/2026-11-10-une-idee-pour-chacun-de-vos-projets.md`, l. 7 | « Plus tard : sans date » pour le laboratoire de la Nièvre et la machine d’IA ; la page « Une ambition », la fiche 9, la fiche 11 et la diapositive `avenir` disent 2030 | « *Plus tard* : sous conditions, sans date. » → « *Plus tard* : sous conditions, sans date promise (dans notre ambition : d’ici 2030). » ; ligne 25 : « aucune date pour ce qui est marqué « plus tard » » → « aucune date promise pour ce qui est marqué « plus tard » » | non |
| C8.4 | important | `pour-carlone/fiches/2026-11-10-fiche-09-l-ia-en-2026-et-demain.md`, l. 30 | La machine d’IA chez lui : « d’ici 2030 » ici ; « plus tard, sous conditions » dans la fiche 8, la page des idées et la maquette ; la même fiche dit plus bas « aucune date pour ce qui est plus tard » | Retirer ce membre de phrase de la ligne « D’ici 2030 », et ajouter avant la ligne de la robotique : « - **Une machine d’IA chez vous : plus tard, sous conditions**, si vos documents confidentiels le demandent. » (essayé : la fiche reste sur deux pages) | non |
| C8.5 | mineur | `pour-carlone/developpement/2026-11-10-une-idee-pour-chacun-de-vos-projets.md`, l. 17 | Cabaret : « ensuite » pour tout ; la fiche 3 met le quotidien du cabaret ouvert en « plus tard » | « … sans oubli administratif \| Ensuite \| » → « … sans oubli administratif \| Ensuite ; plus tard pour le quotidien du cabaret ouvert \| » | non |
| C8.6 | mineur | `pour-carlone/developpement/2026-11-10-une-ambition-pour-votre-etablissement.md`, l. 7 | La colonne « Horizon » a quatre valeurs : 2027, 2028, 2030 et « plus tard, sous conditions » (robotique) | « ## Douze idées, trois horizons » → « ## Douze idées : trois horizons, et un « plus tard » » | non |

**C9. Le nombre d’étapes de la méthode : trois ou quatre.** Fait foi : la diapositive `etapes`, montrée vendredi (1 Choisir, 2 Essayer, 3 Suivre, 4 Étendre), et le texte d’orateur. À ne pas confondre avec les quatre niveaux d’offre (commencer, prouver, construire, rayonner) ni avec les trois niveaux d’aide (automatique, assistée, préparée).

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C9.1 | important | `pour-carlone/fiches/2026-11-10-fiche-10-travailler-avec-nous.md`, l. 18 | La fiche 10 compte trois étapes ; la diapositive 17 en montre quatre | « ## Notre méthode : trois étapes, une à la fois » → « ## Notre méthode : par étapes, une à la fois », et finir le point 3 par : « Puis d’autres domaines, un à la fois. » (essayé : la fiche reste sur deux pages ; un quatrième point numéroté la ferait passer à trois) | non |
| C9.2 | mineur | `pour-carlone/fiches/2026-11-10-fiche-10-travailler-avec-nous.md`, l. 7 | Même compte dans « En bref » | « cadrage, essai de huit semaines au plus, puis suivi. » → « cadrage, essai de huit semaines au plus, suivi, puis d’autres domaines. » | non |

**C10. La grille de questions pour comparer les offres : quatre ou cinq.** Fait foi : la diapositive `grille` (« Quatre questions pour toute offre, la nôtre comprise »), que citent le texte d’orateur, l’antisèche et les réponses aux objections. La page sur les suites propose, sous un titre presque identique, cinq autres questions.

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C10.1 | important | `pour-carlone/logiciels-et-automatisations/2026-11-10-vos-suites-un-logiciel-du-marche-bien-choisi.md`, l. 17 | Deux listes au même titre, de longueur et de contenu différents : laquelle est « la grille » ? | « ## Cinq questions à poser à tout prestataire, nous compris » → « ## Pour vos suites : cinq questions à poser à tout prestataire, nous compris » (essayé : la page reste sur une page ; une phrase de plus la ferait passer à deux) | non |

**C11. Les droits de reproduction gérés par l’ADAGP.** Fait foi : la note `k9`, « Vérification du 10 novembre 2026 », contrôle n° 10 et correction n° 9 : la règle générale est confirmée (code de la propriété intellectuelle, art. L122-4) ; le passage par l’ADAGP n’a pas été lu sur une page de l’ADAGP, et « la fiche 1 le dit prudemment ». La fiche 6 l’affirme, sur la foi de la note interne « présence en ligne ».

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C11.1 | important | `pour-carlone/fiches/2026-11-10-fiche-06-votre-presence-en-ligne.md`, l. 38 | Même règle, deux degrés de certitude : affirmée ici, « à confirmer avec elle » dans la fiche 1 ; le lecteur est marchand d’art | Une seule formule dans les deux fiches : « Si l’artiste a confié ses droits à l’ADAGP, la demande passe par elle : circuit à confirmer avec l’ADAGP (page « droits de reproduction et de représentation », consultée le 10 novembre 2026). » | à décider par les associés |

**C12. Les statuts de la société et l’avocat : lundi 16 ou lundi 30 novembre.** Fait foi : le calendrier unique du sommaire (lundi 16 novembre : statuts signés, si ce calendrier est retenu ; lundi 30 novembre : avocat choisi, dossier d’immatriculation déposé) et `interne/prealables/2026-11-10-demarches-immatriculation-et-assurance.md` (étapes 1 et 4 : lundi 16 novembre ; étape 6 : au plus tard lundi 30 novembre ; immatriculation probable entre fin novembre et la mi-décembre). La chaîne est courte : avec la signature après l’immatriculation (variante A, recommandée), « commande signée avant la mi-décembre » ne tient que si les statuts sont signés le 16.

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C12.1 | important | `interne/decisions/2026-11-10-feuille-de-decisions.md`, l. 123 | La feuille de décisions donne le lundi 30 novembre pour décider des statuts ; le sommaire et la note des démarches, le lundi 16 pour les signer | « P1, lundi 30 nov. » → « P1 : statuts signés lundi 16 nov. ; dossier déposé au plus tard lundi 30 nov. » | à décider par les associés |
| C12.2 | important | `interne/decisions/2026-11-10-feuille-de-decisions.md`, l. 91 | L’avocat est « à choisir » pour le lundi 30 novembre, alors que les statuts se décident avec lui le lundi 16 et qu’il relit le bon avant tout envoi | « P1, lundi 30 nov. » → « P1 : avocat choisi avant le lundi 16 nov. ; relecture du bon de commande rendue au plus tard lundi 30 nov. » | à décider par les associés |
| C12.3 | mineur | `interne/decisions/2026-11-10-feuille-de-decisions.md`, l. 7 | P1 est défini « avant le jeudi 19 novembre », mais trois lignes P1 portent le 27 ou le 30 novembre | « P1 : avant le jeudi 19 novembre 2026, premier jour possible d’un envoi. » → « P1 : avant le premier envoi, possible au plus tôt le jeudi 19 novembre 2026 (date propre à chaque ligne). » | non |

**C13. Le LISEZ-MOI de la version 12 : trois durées et quatre comptes périmés.** Fait foi : `pour-carlone/presentation-ia/2026-11-10-version-12-projet/project/deck.json` (36 diapositives : 28 dans le fil, 8 en annexe) et le texte d’orateur (trente-deux minutes). Le sommaire renvoie à ce LISEZ-MOI pour l’ordre ; qui le lit par le haut trouve « non publiée », « vingt minutes », 19 puis 21 puis 26 diapositives dans le fil.

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C13.1 | important | `pour-carlone/presentation-ia/2026-11-10-version-12-projet/LISEZ-MOI.md`, l. 1 | Titre « non publiée » ; la ligne 5 dit « Publiée le 10 novembre 2026 comme nouvelle présentation privée » | « (non publiée) » → « (publiée en privé le 10 novembre 2026, non partagée) » | non |
| C13.2 | important | `pour-carlone/presentation-ia/2026-11-10-version-12-projet/LISEZ-MOI.md`, l. 7 | Durées : « vingt minutes » (l. 7), « environ 28 à 30 minutes » (l. 44), « environ 30 minutes » (l. 46) ; aucune n’est 32. Comptes : 19 + 5, puis 26, 31, 34 ; seule la dernière ligne dit 36 | Ajouter sous la ligne 5 : « [Mention du 11 novembre 2026 : l’état qui fait foi est celui de la dernière ligne et de `deck.json` : 36 diapositives, 28 dans le fil (trente-deux minutes, d’après le texte d’orateur), 8 en annexe. Les ordres et les durées donnés plus bas (vingt minutes ; 28 à 30 minutes ; 30 minutes) décrivent des états antérieurs.] » | non |

**C14. Le compte des notes de recherche vérifiées : k7 n’en est pas.** Fait foi : la note `k7` elle-même (« La partie « Vérification du 10 novembre 2026 » demandée par le brief complémentaire n’est pas dans cette note », rubrique « Ce qui n’a pas pu être vérifié ») ; quinze notes portent cette partie (k1a, k1b, k2, k3, k4, k8, k9, k10, k11, k12, k13a, k13b, k13c, k13d, k13f), pas seize.

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C14.1 | important | `audit/2026-11-10-preparation-des-livrables/README.md`, l. 53 | Le sommaire range k7 parmi les notes vérifiées | « k1a, k1b, k2, k3, k4, k7, k8, » → « k1a, k1b, k2, k3, k4, k8, » ; et « **Non vérifiées** : k5, k6, k7b » → « **Non vérifiées** : k5, k6, k7, k7b » | non |
| C14.2 | important | `REPRISE-2026-11-10.md`, l. 15 | La note de reprise aussi (partie « État le plus récent ») | « Notes vérifiées : k1a, k4, k7, k8 » → « Notes vérifiées : k1a, k4, k8 » (k7 : non vérifiée) | non |

**C15. L’annexe « comparaisons et calculs » : des montants sans source dans un document client.** Fait foi : le brief, § 4 (« Aucun autre prix dans un document client, sauf un tarif public cité avec sa source et sa date ») et la note `k13a`, « Vérification du 10 novembre 2026 » (prix des revendeurs français : non relus, « interne seulement »). L’annexe annonce elle-même que « chaque prix porte sa source et sa date ». Les prix publics de ses § 1 et 2 sont tous conformes aux notes k13a, k13b et k13c.

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C15.1 | important | `pour-carlone/developpement/2026-11-10-annexe-comparaisons-et-calculs.md`, l. 56 | § 4 : trois fourchettes en euros sans source ni date (6 000 à 10 000 € ; 11 000 à 25 000 € ; « un à deux milliers d’euros par mois »), bâties sur des prix de revendeurs non relus | Soit retirer les montants : « environ 6 000 à 10 000 € hors taxes (une machine de bureau et sa mise en service, si elle est utile) » → « le prix d’une machine de bureau (§ 1) et sa mise en service, si elle est utile » ; « environ 11 000 à 25 000 € hors taxes pour une station de calcul » → « le prix d’une station de calcul, à chiffrer sur devis » ; « environ un à deux milliers d’euros par mois » → « davantage, selon le calcul loué ». Soit les garder, et corriger la ligne 5 : « (chaque prix porte sa source et sa date) » → « (chaque prix public porte sa source et sa date ; les ordres de grandeur du § 4 sont nos estimations) » | à décider par les associés |

## 5. Conflits mineurs

**C16. Mineurs : comptes, mots et dates sans effet sur vendredi.** Chaque ligne dit ce qui fait foi.

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| C16.1 | mineur | `pour-carlone/maquettes/2026-11-10-ecrans-d-exemple/index.html`, l. 88 | Maquette, vue d’ensemble (image de la diapositive 14) : « À traiter dans les 30 jours : 4 » ; l’écran « Échéances » liste six dates, dont deux au plus tiennent dans une même fenêtre de trente jours (15/01/2027 et 01/02/2027). Fait foi : l’écran « Échéances » | « 4 » → « 2 », puis refaire l’image `ecran-accueil.png` ; à défaut, ne rien changer et dire « données fictives » | à décider par les associés |
| C16.2 | mineur | `pour-carlone/maquettes/2026-11-10-ecrans-d-exemple/index.html`, l. 289 | Maquette, « Votre semaine » : deux échéances de la même semaine, l’assurance du Bâtiment B (01/02/2027) et le retour de l’Œuvre 4 (30/03/2027), sont à huit semaines l’une de l’autre | « retour le 30/03/2027 » → « retour le 05/02/2027 » (un vendredi, même semaine que le lundi 01/02/2027) | à décider par les associés |
| C16.3 | mineur | `interne/decisions/2026-11-10-feuille-de-decisions.md`, l. 30 | V14 ne liste pas le cas « avec moyens, sans ambition » (V7 « montrer », V11 « sans ambition ») : 30 min 30, déjà calculé dans le texte d’orateur. Fait foi : le texte d’orateur, § 3 | Ajouter la case « ☐ 30 min 30 (avec « moyens », sans « ambition ») » ; la liste du jour J la porte déjà | non |
| C16.4 | mineur | `interne/decisions/2026-11-10-feuille-de-decisions.md`, l. 99 | La ligne 32 dit que les n° 6, 13, 20 et 21 passent en P0 ; le tableau garde « P2 » ou « P1 » pour les n° 13, 20 et 21, et « P1 » pour les n° 3 et 4, que les arbitrages A et B ont passés en P0. Fait foi : la partie « Avant vendredi » | Dans la colonne « Priorité, date » des n° 3, 4, 13, 20 et 21 : écrire « P0, jeudi 12 nov. » | non |
| C16.5 | mineur | `interne/decisions/2026-11-10-feuille-de-decisions.md`, l. 76 | Phrase « mot pour mot » qui dit « pilote » ; le mot retenu est « essai » (décision n° 21). Même phrase dans les réponses aux objections, n° 3 | « Jusqu’au bilan du pilote » → « Jusqu’au bilan de l’essai » | non |
| C16.6 | mineur | `pour-carlone/developpement/2026-11-10-une-ambition-pour-votre-etablissement.md`, l. 32 | La phrase de référence est « Rien n’est envoyé, payé, signé ou supprimé sans la validation d’une personne habilitée » (page d’offre, bon de commande) ; trois pages remplacent « supprimé » par « publié » | → « Rien n’est envoyé, publié, payé, signé ou supprimé sans la validation d’une personne habilitée. » | non |
| C16.7 | mineur | `pour-carlone/developpement/2026-11-10-ce-que-nous-pourrions-faire-ensuite.md`, l. 27 | Même écart | → « Rien n’est envoyé, publié, payé, signé ou supprimé sans la validation d’une personne habilitée. » | non |
| C16.8 | mineur | `pour-carlone/developpement/2026-11-10-nos-offres-de-la-premiere-marche-aux-grands-projets.md`, l. 47 | Même écart | « avant tout envoi, paiement, signature ou publication » → « avant tout envoi, publication, paiement, signature ou suppression » | non |
| C16.9 | mineur | `pour-carlone/fiches/2026-11-10-fiche-10-travailler-avec-nous.md`, l. 22 | « renouvelables » ; la diapositive `etapes` et le brief disent « renouvelées par écrit » | « renouvelables par écrit » → « renouvelées par écrit » | non |
| C16.10 | mineur | `audit/2026-11-10-preparation-des-livrables/README.md`, l. 14 | « Six parties » dans le sommaire ; « cinq parties » dans l’antisèche et le texte d’orateur (l’annexe est la sixième section de `deck.json`) | « Six parties : » → « Cinq parties et une annexe : » | non |
| C16.11 | mineur | `REPRISE-2026-11-10.md`, l. 21 | Sous ce titre et les suivants, des chiffres périmés : 26 diapositives et 21 dans le fil, « vingt minutes », « V1 à V10 », « quatre écrans », « sous deux jours ». La ligne 5 dit que la première partie l’emporte ; rien ne le rappelle plus bas | Ajouter sous ce titre : « [Mention du 11 novembre 2026 : les chiffres de cette partie et des suivantes (26 diapositives, vingt minutes, V1 à V10, quatre écrans) sont périmés ; voir « État le plus récent ».] » | non |
| C16.12 | mineur | `interne/cadrage/2026-11-10-kit/06-tableau-d-inventaire.xlsx`, feuille « 9 Rôles », E2:E9 | Tableau d’inventaire du cadrage, feuille « 9 Rôles », cellules E2 à E9 : la source citée est « proposition du 9 novembre » ; la pièce client est la version du 10 novembre | « proposition du 9 novembre » → « proposition de cadrage, version client (10 novembre) » | non |

## 6. Écarts constatés pendant l’audit et déjà corrigés par une autre relecture

Ils figurent ici pour que l’on sache qu’ils ont été vus, puis vérifiés corrigés dans le fichier ; rien n’est à refaire.

| Fichier et ligne (texte corrigé) | Ce qui n’allait pas |
| --- | --- |
| `interne/rendez-vous/2026-11-10-deroule-et-texte-d-orateur.md`, l. 38 | Texte d’orateur, diapositive 5 : la mesure de METR était dite sans « sur des tâches de logiciel », « une fois sur deux » ni « mesure du passé » ; elle est dite en entier |
| `interne/rendez-vous/2026-11-10-deroule-et-texte-d-orateur.md`, l. 69 | Texte d’orateur, transition vers `avenir` : « à un, deux et cinq ans » ne tombait pas sur 2027, 2028 et 2030 (un, deux et quatre ans) |
| `interne/rendez-vous/2026-11-10-deroule-et-texte-d-orateur.md`, l. 5 | Texte d’orateur, diapositive 26 et § 4 : « un bon de commande d’une page » |
| `interne/rendez-vous/2026-11-10-deroule-et-texte-d-orateur.md`, l. 12 | Texte d’orateur, § 1 : « V2 à V5 » |
| `interne/rendez-vous/2026-11-10-deroule-et-texte-d-orateur.md`, l. 88 | Texte d’orateur : le cas « avec moyens, sans ambition » manquait |
| `interne/rendez-vous/2026-11-10-deroule-et-texte-d-orateur.md`, l. 98 | Texte d’orateur : la liste des écarts citait deux défauts déjà corrigés dans la présentation (note de `cover`, « sans commission » sur `presence`) |
| `interne/rendez-vous/2026-11-10-antiseche-une-page.md`, l. 5 | Antisèche : « V2 à V5 » |
| `pour-carlone/presentation-ia/2026-11-10-version-12-projet/project/slides/decision.html`, l. 12 | Diapositive `decision`, à l’écran et dans la note : « Un bon de commande d’une page » (source corrigée ; voir C1 pour la page publiée) |
| `pour-carlone/presentation-ia/README.md`, l. 3 | Guide des versions de la présentation : il ne connaissait que la version 11 (26 diapositives) ; une mention datée donne la version 12 et ses 36 diapositives |
| `pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md`, l. 3 | Pièce historique du 9 novembre sur le logiciel : prix, « pilote » et calendrier (essai de mi-mars à mi-mai 2027) contraires aux pièces du 10 novembre ; une mention datée en tête dit qu’elle n’est ni montrée ni remise |
| `interne/decisions/2026-11-10-feuille-de-decisions.md`, l. 71 | Feuille de décisions, arbitrage B et V10 : « sous deux jours », délai que la diapositive `decision` ne porte plus |
| `interne/decisions/2026-11-10-feuille-de-decisions.md`, l. 93 | Feuille de décisions, n° 7 : « bon de commande d’une page » |
| `interne/decisions/2026-11-10-feuille-de-decisions.md`, l. 106 | Feuille de décisions, n° 20 : écrans cités (« fiche bâtiment, échéances, trois devis ») qui ne sont pas ceux de la version 12 |
| `interne/decisions/2026-11-10-feuille-de-decisions.md`, l. 107 | Feuille de décisions, n° 21 : « essai de huit semaines », sans « au plus » |
| `interne/rendez-vous/2026-11-10-reponses-aux-objections.md`, l. 16 | Réponses aux objections, n° 1 : « ces trois semaines » |
| `interne/rendez-vous/2026-11-10-convaincre-de-miser-sur-nous.md`, l. 28 | Stratégie du rendez-vous : un essai sur « le registre des bâtiments et le choix du logiciel » (deux tâches) ; « huit semaines » sans « au plus » ; « trois horizons » pour essai, ensuite, plus tard |
| `interne/rendez-vous/2026-11-10-a-relire-avec-mathys.md`, l. 33 | Plan de relecture : « essai de huit semaines » ; « dix choix » quand la note en comptait onze (la note dit désormais dix) |

## 7. Faits contrôlés sans conflit

Une ligne par fait. « Occurrences » : nombre de lignes où le fait est écrit, et nombre de fichiers, dans le périmètre lu (texte des diapositives, de la maquette et des classeurs compris ; la copie interne du texte des diapositives et le référentiel joint à ce rapport ne sont pas comptés).

**L’offre**

| Fait, valeur unique | Occurrences | Remarque |
| --- | --- | --- |
| Prix du cadrage : 6 500 € hors taxes | 26 dans 19 fichiers |  |
| Soit 7 800 € toutes taxes comprises | 20 dans 17 fichiers |  |
| Acompte et solde : 3 250 € hors taxes, 3 900 € toutes taxes comprises ; TVA 1 300 € et 650 € | 7 dans 4 fichiers | bon de commande, fiche 10, proposition, antisèche |
| Réserve de TVA : « TVA de 20 % … sinon 6 500 €, TVA non applicable (franchise en base) » | 6 dans 6 fichiers | même phrase partout |
| « déplacements des deux rendez-vous compris » | 8 dans 7 fichiers |  |
| Durée du cadrage : trois à quatre semaines | 33 dans 16 fichiers |  |
| Premier entretien : deux à trois heures, chez lui | 5 dans 5 fichiers |  |
| Restitution : une heure trente | 5 dans 5 fichiers | bon de commande, proposition, antisèche, page de l’administratrice, fiche 5 |
| Pièces attendues sous dix jours ouvrés après la commande ; réserves sous dix jours ouvrés | 7 dans 5 fichiers |  |
| Rétractation : quatorze jours ; pas de travail avant le quinzième jour sans demande écrite | 4 dans 3 fichiers | entre crochets : à arrêter avec l’avocat |
| Documents rendus ou effacés sous quinze jours ouvrés | 4 dans 4 fichiers |  |
| Réponses de l’administratrice sous cinq jours ouvrés | 7 dans 3 fichiers |  |
| Retard de notre fait : plus de deux semaines | 7 dans 6 fichiers |  |
| Suite choisie dans les trente jours après la restitution | 4 dans 3 fichiers |  |
| Trois priorités à 90 jours | 8 dans 7 fichiers |  |
| Trois tâches au plus à essayer | 16 dans 14 fichiers |  |
| Essai : huit semaines au plus | 31 dans 22 fichiers | les formes sans « au plus » ont été corrigées le 11 novembre ; il en reste une, dans le rappel « Déjà décidé » de la feuille de décisions |
| Suivi régulier : périodes de trois mois, par écrit | 8 dans 7 fichiers | « renouvelées » ou « renouvelables » : C7, C16 |
| Temps de l’administratrice : environ une à deux journées sur trois à quatre semaines | 11 dans 10 fichiers | somme du détail refaite : six à douze heures |
| Validité : jusqu’au jeudi 31 décembre 2026 | 13 dans 11 fichiers |  |
| Démarrage visé début janvier 2027, si la commande est signée avant la mi-décembre | 11 dans 10 fichiers |  |
| « immatriculée avant toute facture et tout démarrage » | 15 dans 15 fichiers |  |
| Cession « une fois le prix dû payé » | 14 dans 11 fichiers | une exception : C7 |
| « une étape et un essai à la fois » | 15 dans 13 fichiers |  |
| Indemnité forfaitaire de 40 € ; pénalités au taux de la Banque centrale européenne majoré de dix points | 1 dans 1 fichier | bon de commande ; note k1b |
| Autre proposition reçue : 6 000 € par trimestre (rapporté par Morgan Olsen, non vérifié) | 1 dans 1 fichier | interne seulement ; absente de tout document client ; même valeur dans la note interne sur les questions à poser |

**Les dates et les jours de la semaine**

| Fait, valeur unique | Occurrences | Remarque |
| --- | --- | --- |
| Rendez-vous : vendredi 13 novembre 2026 | 25 dans 11 fichiers |  |
| Décisions : jeudi 12 novembre 2026, au soir | 17 dans 5 fichiers |  |
| Premier envoi possible : jeudi 19 novembre 2026 | 22 dans 9 fichiers |  |
| Dernier jour pour envoyer la proposition : vendredi 27 novembre 2026 | 2 dans 2 fichiers |  |
| Démarrage possible : lundi 4 janvier 2027 | 2 dans 2 fichiers |  |
| Restitution au plus tard : vendredi 29 janvier 2027 (proposition, à décider) | 7 dans 5 fichiers |  |
| Règles du jacuzzi : 1er janvier 2027 | 8 dans 5 fichiers |  |

**Les comptes du dossier**

| Fait, valeur unique | Occurrences | Remarque |
| --- | --- | --- |
| Neuf suites (jamais « votre hôtel », qui ne figure que dans les listes de mots à éviter) | 64 dans 35 fichiers |  |
| Présentation : 36 diapositives | 10 dans 7 fichiers | compté dans `deck.json` : 36 |
| Dont 28 dans le fil et 8 en annexe | 9 dans 6 fichiers | compté : 28 et 8 |
| Durée : 32 minutes | 15 dans 6 fichiers | somme des 28 temps refaite : 32 min 00 |
| Variantes : 31 min 15 et 29 min 45 | 6 dans 4 fichiers | 30 min 30 : C16 |
| Douze fiches thématiques | 9 dans 7 fichiers | compté : 12 fichiers, 2 pages chacun en rendu compact |
| Maquette : onze écrans | 9 dans 6 fichiers | compté : 11 entrées de menu, 11 images |
| Présence en ligne : sept formules | 4 dans 4 fichiers | compté : 7 |
| Offres : quatre niveaux | 9 dans 7 fichiers | compté : 8 programmes, 4 grands projets |
| Aide : trois niveaux (automatique, assistée, préparée) | 6 dans 5 fichiers |  |
| Décisions : V1 à V14 | 7 dans 5 fichiers | compté : 14 lignes |
| Vingt et une décisions de l’audit de l’offre ; trois arbitrages | 4 dans 3 fichiers | compté : 21 lignes ; A, B, C |
| Treize objections préparées | 1 dans 1 fichier | compté : 13 rubriques |
| Trois projets prioritaires pour les trois prochains mois (question de clôture) | 11 dans 6 fichiers |  |

**Le droit et les chiffres externes**

| Fait, valeur unique | Occurrences | Remarque |
| --- | --- | --- |
| Factures électroniques : réception depuis le 1er septembre 2026, toute entreprise soumise à la TVA | 6 dans 4 fichiers | notes k1a et k1b |
| Émission par les PME et micro-entreprises : 1er septembre 2027 | 1 dans 1 fichier | note k1a |
| Règlement européen sur l’IA, art. 4 : « favoriser la maîtrise de l’IA » ; règlement 2026/1744 du 8 juillet 2026 | 6 dans 5 fichiers | note k4 ; aucun « obligation de former » |
| Règlement européen sur l’IA, art. 50 : depuis le 2 août 2026 | 4 dans 3 fichiers | audit du 9 novembre ; note k13c |
| Jacuzzi : déclaration à la mairie, au plus tard deux mois avant (ARS, 19 juin 2025) | 4 dans 4 fichiers | note k14 |
| Jacuzzi : quinze minutes au plus, déconseillé aux moins de dix ans | 3 dans 3 fichiers | note k14 |
| Jacuzzi : analyses par un laboratoire accrédité, décret n° 2026-118 du 20 février 2026 | 3 dans 3 fichiers | note k14 |
| Fiche de police : conservée six mois (F17452, vérifiée le 21 mai 2026) | 3 dans 3 fichiers | note k12 |
| Récépissé d’entrepreneur de spectacles : trente jours, cinq ans (F22365) | 4 dans 3 fichiers | note k10 |
| Taxe sur les spectacles : 3,5 % de la billetterie, dernier jour du troisième mois | 3 dans 3 fichiers | note k10 |
| Autorisation de travaux : quatre mois avec une déclaration préalable, cinq avec un permis (F31687) | 4 dans 3 fichiers | note k11 (k10 ne l’avait pas vérifié) |
| Déclaration préalable : un mois, deux en secteur protégé (F17578) | 4 dans 3 fichiers | note k11 |
| 5e catégorie : vérifications tous les trois ans au plus, depuis le 1er juillet 2026 (art. PE 4) | 3 dans 3 fichiers | notes k8 et k11 |
| Bail dérogatoire : trois ans au plus ; dépôt de garantie : un trimestre, baux depuis fin mai 2026 | 3 dans 3 fichiers | notes k8 et k11 |
| Galerie : TVA de 5,5 % depuis le 1er janvier 2025 ; droit de suite dès 750 € ; vigilance dès 10 000 € | 3 dans 2 fichiers | note k9 ; l’article 278-0 bis du CGI change de numéro au 1er janvier 2027 |
| Accord sur les données : article 28 du RGPD | 5 dans 4 fichiers |  |
| Logiciels des suites : eviivo à partir de 40 € hors taxes par mois | 4 dans 4 fichiers | pages lues le 10 novembre 2026 |
| Sirvoy, formule Pro : 79 € par mois | 4 dans 4 fichiers |  |
| Thaïs : 65 € hors taxes, plus moteur et canaux, soit 130 à 190 € par mois | 3 dans 3 fichiers | somme refaite : 65 + 35 + 30 à 90 |
| Mesure de METR : « environ tous les sept mois depuis 2019 » | 7 dans 6 fichiers | source et date : C4 |
| Études de gains : de −19 % à +56 % | 3 dans 3 fichiers | note k13f |
| « Jusqu’à cent fois » : hypothèse, première lecture seulement ; « cinq à dix fois » sur toute la chaîne | 10 dans 9 fichiers | note k13f |
| IA dans les TPE et PME : 40 %, contre 26 % en 2025 (baromètre France Num 2026) | 1 dans 1 fichier | source lue pour l’audit du 9 novembre (note r2) |
| Prix publics de l’annexe (jetons, location de cartes, machines, abonnements) | 5 dans 1 fichier | notes k13a, k13b, k13c ; reste non vérifié : le caractère hors taxes des prix de Scaleway |

## 8. Calculs, calendrier et comptes refaits

- **Jours de la semaine** (calcul) : jeudi 5, jeudi 12, vendredi 13, lundi 16, jeudi 19, vendredi 27 et lundi 30 novembre 2026 ; vendredi 11 et jeudi 31 décembre 2026 ; vendredi 1er, lundi 4 et vendredi 29 janvier 2027 : tous justes. Le compte rendu interne « sous 24 heures ouvrées » après le vendredi 13 tombe bien le lundi 16 novembre.
- **Restitution** : lundi 4 janvier 2027 plus 25 jours donne le vendredi 29 janvier 2027, dans la quatrième semaine : cohérent avec « trois à quatre semaines ».
- **Prix** : 6 500 × 20 % = 1 300 ; 6 500 + 1 300 = 7 800 ; moitiés de 3 250, 650 et 3 900 : justes. En interne : 5 300 + 10 400 = 15 700 ; 15 700 + 3 000 = 18 700 ; 15 700 + 6 500 = 22 200 ; 18 700 + 6 500 = 25 200 : justes.
- **Présentation** : 28 temps, somme 32 min 00 ; parties de 7 min, 8 min, 4 min, 7 min 30 et 5 min 30 ; repères à 7, 15, 19, 26 min 30 et 32 min ; variantes de 31 min 15 (moins 45 s), 29 min 45 (moins 45 s et 1 min 30) et 30 min 30 (moins 1 min 30) : justes. Rendez-vous : 10 + 34 + 31 + 15 = 90 minutes.
- **Plan de relecture** : 1 h + 1 h 30 + 1 h = 3 h 30.
- **Temps de l’administratrice** : une à trois heures, deux à quatre heures, une à deux heures, quelques minutes par jour sur dix jours ouvrés et une heure trente font environ six à douze heures : « une à deux journées » tient.
- **Tarifs et estimations** : Thaïs, 65 + 35 + 30 à 90 = 130 à 190 € ; électricité, 160 W × 8 760 h ≈ 1 400 kWh, soit environ 280 € à 0,2001 € le kWh (« moins de 300 € » tient) ; coût de l’IA, 47 % de baisse par trimestre, soit environ treize fois moins par an (0,53 à la puissance 4 ≈ 0,08) : juste.
- **Pages** (rendu `md2pdf --compact` refait pour cet audit) : page d’offre, page de l’administratrice, « Votre intérêt », « moyens », « présence en ligne », « ensuite », page sur les suites, questionnaire, liste des pièces et antisèche : 1 page ; les douze fiches : 2 pages chacune ; « Nos offres », « Une ambition », « Une idée » : 2 ; bon de commande : 3 (2 sans ses conditions) ; annexe : 4 ; autorisations : 5 ; proposition : 6.
- **Corrections proposées, essayées sur des copies de travail** (bloc-notes de session) : avec les textes proposés aux § 4 et 5, les fiches 6, 9, 10 et 12 restent sur 2 pages ; « Votre intérêt », « ensuite » et la page sur les suites sur 1 page ; « Une ambition », « Une idée » et « Nos offres » sur 2 pages ; contrôle des lignes rouges : 0 erreur. Les diapositives n’ont pas été rendues.
- **Comptes vérifiés dans les fichiers** : 36 identifiants dans `deck.json` et 36 fichiers de diapositives ; 12 fiches ; 11 écrans ; 7 formules ; 8 programmes et 4 grands projets ; 12 idées (page « Une ambition ») ; 13 idées (page « Une idée », d’où « treize projets » dans la stratégie) ; 6 raisons (`pourquoi-nous`) ; 7 chantiers (`univers`) ; 14 lignes V ; 21 décisions ; 5 décisions échues ; 13 objections ; 34 lignes dans l’échéancier ; 12 feuilles dans le tableau d’inventaire.

## 9. Limites

- Les images (captures de la maquette dans les diapositives, planches) n’ont pas été lues : seul leur texte source l’a été.
- Le texte des diapositives extrait dans le bloc-notes de session date d’avant la correction de `decision.html` et de `cover.html` : ces deux fichiers ont été relus à la source ; les autres diapositives sont citées d’après leur source, inchangée.
- Les pièces d’avant le 10 novembre n’ont été ouvertes que pour vérifier un chiffre cité (prix et calendrier du document « logiciel » du 9 novembre).
- Aucune source externe n’a été rouverte : la concordance est établie avec les notes `k…`, pas avec les pages officielles.
- Les documents internes changeaient pendant l’audit : un écart corrigé après l’heure indiquée au § 2 peut encore figurer aux § 3 à 5. Le script qui a produit ce rapport retrouve chaque texte dans son fichier et peut être relancé (`/tmp/claude-0/-home-user-Carlone/5dd15790-6933-5e33-ba7c-b9089896b9b3/scratchpad/a6-final/bin/gen_rapport.py`).
- Aucune décision n’est tranchée ici : les lignes « à décider par les associés » décrivent un choix, avec la voie la moins coûteuse quand il y en a une.
