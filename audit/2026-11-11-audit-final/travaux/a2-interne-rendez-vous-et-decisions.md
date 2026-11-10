# Audit final — lot A2 : les documents internes du rendez-vous et la feuille de décisions

Document interne — ne pas transmettre à GianLuca Carlone · 11 novembre 2026

**Angle.** Ce que Morgan Olsen et Mathys Couet auront en main vendredi doit correspondre exactement à ce que GianLuca Carlone verra. **Lot** : `interne/rendez-vous/2026-11-10-deroule-et-texte-d-orateur.md` (« déroulé »), `…-antiseche-une-page.md` (« antisèche »), `…-reponses-aux-objections.md` (« objections »), `…-convaincre-de-miser-sur-nous.md` (« convaincre »), `…-a-relire-avec-mathys.md` (« à relire ») et `interne/decisions/2026-11-10-feuille-de-decisions.md` (« feuille »). **Références lues en entier** : le texte des 36 diapositives et `deck.json` ; les quatre pièces du 10 novembre de `pour-carlone/offre-cadrage/` ; les douze fiches ; les huit pages de `pour-carlone/developpement/` ; la page sur les suites ; le sommaire du 10 novembre. Les numéros de ligne sont ceux des fichiers après correction.

**Cadre tenu.** Aucun contact, aucun envoi, aucune commande git, aucun fichier de `crm/` ouvert. Seuls les six fichiers du lot et ce rapport sont écrits. Dans la feuille : aucune case cochée (62 cases avant, 62 après), aucune recommandation changée, rien de tranché.

## En bref

1. **L’ordre et les durées du déroulé sont exacts.** Vingt-huit lignes, mêmes identifiants et mêmes rangs que la clé « order » de `deck.json` ; somme refaite : 32 min 00 ; sous-totaux 7 min 00, 8 min 00, 4 min 00, 7 min 30, 5 min 30 ; variantes 31 min 15 et 29 min 45. Les huit diapositives d’annexe sont les bonnes, dans l’ordre (§ 1).
2. **Le texte à dire s’était écarté de l’écran et du référentiel sur neuf points**, tous corrigés : la mesure de METR sans ses trois limites ; « un bon de commande d’une page » (il en fait trois) ; le retard de plus de deux semaines oublié ; « cédé au paiement » ; « à un, deux et cinq ans » au lieu de 2027, 2028, 2030 ; la règle par défaut « V2 à V5 » au lieu de « V1 à V5 » ; les maquettes non dites à l’oral ; une liste d’écarts périmée ; un « après » qui promettait un envoi sous deux jours (§ 2).
3. **Deux points bloquants sont hors de mon lot**, dans la présentation : la couverture affiche « dossier Strates », nom interdit dans tout document client ; la diapositive `decision` affiche « Un bon de commande d’une page » (§ 4, H1 et H2). Le déroulé et l’antisèche disent maintenant quoi dire à la place.
4. **La feuille décrivait un état dépassé sur dix points** (V10, arbitrage B, n° 2, 6, 7, 20, 21, deux lignes de la partie 4, partie 6) : corrigés, sans toucher aux recommandations (§ 2, F1 à F11).
5. **Vingt-trois points restent à décider par les associés** (§ 3). Les plus lourds : que montre-t-on si l’accord écrit (V4) manque ; le délai tenable du bon de commande et la date des statuts ; une seule règle pour le solde ; les pièces du 9 novembre qui promettent une attestation d’assurance ; le nom « copilote » ; « Indépendants » et « Rapides et disponibles » ; l’option pour la TVA, dont dépend le prix affiché.
6. **Contrôles après retouches** : `lint-doc.js --interne`, 0 erreur et 0 alerte sur les six fichiers ; antisèche sur une page, pleine (§ 5).

## 1. Le déroulé : ordre, addition des durées, transitions, annexe

### 1.1 L’ordre et l’addition

Comparaison ligne à ligne avec `pour-carlone/presentation-ia/2026-11-10-version-12-projet/project/deck.json` (clé « order », rangs 1 à 28 ; clé « sections » pour les parties). Addition faite à la main, puis par un script qui relit le tableau du déroulé.

| Rang | Identifiant (déroulé et `deck.json`) | Durée | Cumul |
| --- | --- | --- | --- |
| 1 | `cover` | 0 min 30 | 0 min 30 |
| 2 | `compris` | 2 min 00 | 2 min 30 |
| 3 | `univers` | 1 min 00 | 3 min 30 |
| 4 | `nouveautes` | 1 min 00 | 4 min 30 |
| 5 | `evolution` | 1 min 00 | 5 min 30 |
| 6 | `enjeux` | 1 min 30 | **7 min 00** (partie 1 : 7 min 00) |
| 7 | `cat-galerie` | 1 min 15 | 8 min 15 |
| 8 | `hotel` | 2 min 00 | 10 min 15 |
| 9 | `cat-cabaret` | 1 min 00 | 11 min 15 |
| 10 | `cat-batiments` | 1 min 00 | 12 min 15 |
| 11 | `administratrice` | 1 min 30 | 13 min 45 |
| 12 | `presence` | 1 min 15 | **15 min 00** (partie 2 : 8 min 00) |
| 13 | `demande` | 0 min 45 | 15 min 45 |
| 14 | `ecran-ensemble` | 1 min 00 | 16 min 45 |
| 15 | `fonctions` | 1 min 15 | 18 min 00 |
| 16 | `ecran-devis` | 1 min 00 | **19 min 00** (partie 3 : 4 min 00) |
| 17 | `etapes` | 1 min 00 | 20 min 00 |
| 18 | `societe` | 1 min 00 | 21 min 00 |
| 19 | `pourquoi-nous` | 1 min 00 | 22 min 00 |
| 20 | `grille` | 0 min 45 | 22 min 45 |
| 21 | `ambition` | 1 min 30 | 24 min 15 |
| 22 | `avenir` | 0 min 45 | 25 min 00 |
| 23 | `offres` | 1 min 30 | **26 min 30** (partie 4 : 7 min 30) |
| 24 | `proposition` | 1 min 30 | 28 min 00 |
| 25 | `garanties` | 0 min 45 | 28 min 45 |
| 26 | `decision` | 1 min 15 | 30 min 00 |
| 27 | `moyens` | 0 min 45 | 30 min 45 |
| 28 | `cloture` | 1 min 15 | **32 min 00** (partie 5 : 5 min 30) |

- **Total** : 420 + 480 + 240 + 450 + 330 = 1 920 secondes, soit **32 min 00**. Conforme au total annoncé et aux sous-totaux de l’antisèche.
- **Variantes** : sans `moyens`, 32 min 00 − 0 min 45 = **31 min 15** ; sans `moyens` ni `ambition`, 31 min 15 − 1 min 30 = **29 min 45**. Conformes à V14. Cas que V14 ne liste pas : avec `moyens`, sans `ambition`, **30 min 30** (ajouté au déroulé ; point D14).
- **Temps du rendez-vous** : 10 minutes d’accueil, 32 minutes de présentation, 2 minutes de marge, soit 44 minutes ; puis 31 minutes d’échange et 15 minutes de clôture : 90 minutes. Exact.
- **Le texte tient-il dans le temps ?** Le texte à dire fait environ 2 350 mots, soit seize minutes de parole à 140 ou 150 mots à la minute : il reste seize minutes pour les silences, les écrans et les réponses courtes. Quatre diapositives sont denses (plus de 120 mots à la minute) : `cover` (66 mots en 30 secondes), `evolution` (131 mots en une minute, après correction), `pourquoi-nous` (122 mots) et `moyens` (95 mots en 45 secondes). La marge est sur `compris`, `hotel`, `proposition` et `cloture`. Aucune durée n’a été changée.

### 1.2 Les transitions

Les vingt-sept transitions ont été relues contre le titre de la diapositive suivante. Vingt-six l’annoncent bien. Une était inexacte et a été corrigée : de `ambition` vers `avenir`, « à un, deux et cinq ans » alors que l’écran affiche 2027, 2028, 2030 (correction A5). Les deux transitions de repli sont justes : sans `ambition`, « Et demain ? » mène à `avenir` (titre « Demain ») ; sans `moyens`, « Pour finir, une question. » mène à `cloture` (surtitre « Pour finir »).

### 1.3 L’annexe

Liste du déroulé : `fiches`, `ensuite`, `idees`, `ecran-batiment`, `modes`, `cat-admin`, `cat-finance`, `robotique`. Identique aux rangs 29 à 36 de `deck.json`, dans le même ordre. Exact.

## 2. Constats corrigés dans le lot (ancien texte → nouveau texte)

Fait : « oui » partout dans cette partie. Les lignes « important » touchent ce qui se dit ou se décide vendredi.

### 2.1 Déroulé et texte d’orateur

| N° | Gravité | Fichier et ligne | Ce qui n’allait pas | Texte d’avant → texte d’aujourd’hui | Fait |
| --- | --- | --- | --- | --- | --- |
| A1 | important | déroulé, l. 38 (`evolution`) | La mesure de METR était dite sans ses trois limites, renvoyées à « si on demande » ; le référentiel et la note de la diapositive les donnent toujours | « la durée des tâches que l’IA accomplit seule double environ tous les sept mois depuis 2019 » → « sur des tâches de logiciel, la durée des tâches que les meilleurs agents d’IA réussissent une fois sur deux double environ tous les sept mois depuis 2019. C’est une mesure du passé, pas une prévision. » ; la consigne donne la source seulement (arXiv 2503.14499, mars 2025 ; mise à jour du 29 janvier 2026) | oui |
| A2 | important | déroulé, l. 79 (`decision`) et l. 105 (§ 4) | « d’une page » est faux : le projet de bon de commande fait trois pages en rendu compact, le bon seul déborde sur la deuxième ; la page d’offre dit « un bon de commande et ses conditions » | « Nous vous envoyons ensuite un bon de commande d’une page » → « Nous vous envoyons ensuite un bon de commande et ses conditions » ; consigne ajoutée : « Ne pas dire “d’une page” » ; § 4 : « bon de commande d’une page et conditions » → « bon de commande et ses conditions (trois pages) » | oui |
| A3 | important | déroulé, l. 78 (`garanties`) | L’engagement sur le retard, dans la note de la diapositive et dans l’offre, manquait | ajout : « ; de même si vous arrêtez parce que nous avons plus de deux semaines de retard, de notre fait » | oui |
| A4 | important | déroulé, l. 12 | Règle par défaut : la feuille dit « V1 à V5 » (l. 13) | « tant que les décisions V2 à V5 ne sont pas cochées » → « tant qu’une case de V1 à V5 reste vide (feuille de décisions, règle par défaut ; BRIEF-2, § 10.4) » | oui |
| A5 | mineur | déroulé, l. 69 (transition vers `avenir`) | Horizons du référentiel : 2027, 2028, 2030 ; 2030 n’est pas « cinq ans » | « Concrètement, à un, deux et cinq ans. » → « Concrètement : 2027, 2028, 2030. » | oui |
| A6 | important | déroulé, l. 45 (`cat-galerie`) | Les diapositives 7 à 11 montrent une capture de la maquette ; leurs notes commencent par « Maquette, données fictives » ; le texte à dire ne le disait qu’à partir de la diapositive 14 | ajout en tête : « L’image est une maquette, avec des données fictives : œuvres et artistes inventés. » ; consigne : le redire d’un mot aux diapositives 8 à 11 | oui |
| A7 | mineur | déroulé, l. 67 (`pourquoi-nous`) | Cession : forme du référentiel ; renvoi faux à V9 pour les commissions d’éditeurs | « vous est cédé au paiement » → « vous est cédé une fois le prix dû payé » ; « (V9 ; lien de Morgan…) » → « aucune décision écrite ne le dit encore (V9 ne vise que ses collaborateurs ; lien de Morgan…) » ; « disponibles » : rappel que l’écran affiche « Rapides et disponibles » | oui |
| A8 | mineur | déroulé, l. 50 (`presence`) | La consigne renvoyait à un écart que la présentation a corrigé | « Ne pas dire “sans commission” (écart n° 2 ci-dessous) » → « … : la diapositive, corrigée, affiche “Vos suites réservables en direct, sur votre propre site” » | oui |
| A9 | important | déroulé, l. 92 à 99 (écarts de la présentation) | Deux des trois écarts listés sont corrigés dans la présentation (note de `cover`, « sans commission » sur `presence`) ; quatre écarts d’aujourd’hui manquaient | liste refaite : 1. `cover` et « dossier Strates » ; 2. `decision` et « d’une page » ; 3. `pourquoi-nous` (« Indépendants », « Rapides et disponibles », développements « à votre nom ») ; 4. noms des programmes, dont « copilote » ; 5. date de la mesure de METR ; puis les deux écarts corrigés | oui |
| A10 | important | déroulé, l. 103 à 107 (§ 4) | « Compte rendu sous 24 heures ouvrées » et « laisser la grille de questions » contredisent la liste avant tout envoi (« ni message », premier envoi le 19 novembre) et la règle V1 à V5 ; aucune page « grille » n’existe | ajout d’un rappel en tête du § 4 ; « compte rendu sous 24 heures ouvrées » → « compte rendu écrit sous 24 heures ouvrées, envoyé une fois la liste cochée » ; « laisser la grille de questions » → « redire les quatre questions de la diapositive `grille` », avec le constat qu’aucune page n’existe | oui |
| A11 | mineur | déroulé, l. 34 (`cover`) | Le texte à dire évitait déjà le nom du dossier, sans le signaler | consigne ajoutée : « Ne pas nommer le dossier d’où vient l’image (écart n° 1 ci-dessous) » | oui |
| A12 | mineur | déroulé, l. 77 (`proposition`) | Le prix toutes taxes comprises se dit sans sa réserve, qui est dans les documents détaillés | consigne ajoutée : « Si la TVA vient : le prix toutes taxes comprises suppose une TVA de 20 %, si Marwin Tech y est soumise à la date de la facture ; sinon, 6 500 €, TVA non applicable (franchise en base). » | oui |
| A13 | mineur | déroulé, l. 81 (`cloture`) | La diapositive est un texte fixe : rien ne s’y écrit en séance | « Mathys note les trois projets sur la diapositive » → « Mathys note les trois projets (sur papier, si la diapositive ne se modifie pas à l’écran : à essayer jeudi) » | oui |
| A14 | mineur | déroulé, l. 14 et 15 (§ 1) | V12 ne vise que les fiches ; les rôles étaient donnés comme arrêtés alors que V4 les compte parmi ce qui est à écrire ; aucune copie de la présentation ne s’ouvre sans connexion | « seulement si V12 dit “laisser” » → « les pages imprimées seulement si V2 dit “laisser”, les fiches seulement si V12 dit “laisser” » ; « Rôles : » → « Rôles (proposition, à confirmer jeudi dans l’accord écrit, V4) : » ; ajout sur la copie hors connexion à préparer et à essayer jeudi | oui |
| A15 | mineur | déroulé, l. 83 et 88 | Aucune indication de densité ; cas « avec `moyens`, sans `ambition` » sans durée | ajouts : nombre de mots, quatre diapositives denses ; « Cas que V14 ne liste pas : … 30 min 30 » | oui |
| A16 | mineur | déroulé, l. 3 et 5 | Date de la relecture | ligne d’en-tête complétée ; paragraphe « Relecture du 11 novembre 2026 (audit final) » | oui |

**Fidèle sans retouche.** Le texte à dire des diapositives 2, 3, 4, 6, 8, 9, 10, 11, 13 à 18, 20 à 23, 27 et 28 reprend les notes et l’écran d’aujourd’hui (à la ligne 21, seule la transition change ; à la ligne 28, seule la consigne). Contrôle par script sur les vingt-huit lignes : aucun nombre dit qui ne soit sur la diapositive ou dans sa note, sauf « neuf suites » (`ambition`), « nous sommes deux » (`offres`) et « trois à quatre semaines » (`cloture`), pris dans les pages « Une ambition » et « Nos offres » et dans les phrases de clôture.

### 2.2 Antisèche (une page)

| N° | Gravité | Fichier et ligne | Ce qui n’allait pas | Texte d’avant → texte d’aujourd’hui | Fait |
| --- | --- | --- | --- | --- | --- |
| S1 | important | antisèche, l. 5 | Règle par défaut de la feuille : V1 à V5 | « Sans les préalables (V2 à V5) : tout à l’écran… » → « Sans V1 à V5 cochées : tout à l’écran… » | oui |
| S2 | important | antisèche, l. 11 et 12 | L’essai n’était pas dit comme dans le référentiel ; le délai de trente jours manquait | « un essai de huit semaines au plus, commandé à part. Une suite à la fois. » → « un essai de huit semaines au plus, sur une seule tâche, mesurée avant et après, commandé à part. » ; fin de la ligne « Durée » : « Suite choisie dans les trente jours, ou aucune ; une à la fois. » | oui |
| S3 | mineur | antisèche, l. 15 | Forme du référentiel | « …, à confirmer avec elle. » → « …, sur ses heures de travail, à confirmer. » | oui |
| S4 | mineur | antisèche, l. 17 | Le démarrage est un objectif (« visé ») ; année retirée pour tenir sur deux lignes | « offre valable jusqu’au 31 décembre 2026 ; démarrage début janvier 2027 » → « offre valable jusqu’au 31 décembre ; démarrage visé début janvier 2027 » | oui |
| S5 | important | antisèche, l. 24 | « Vous gardez ce que vous avez payé » peut s’entendre comme un remboursement, alors que l’acompte nous reste ; la diapositive `etapes` dit « à la fin de chaque étape » et « ce qui est payé » | « vous pouvez vous arrêter à chaque étape et vous gardez ce que vous avez payé » → « vous pouvez vous arrêter à la fin de chaque étape et vous gardez ce qui est payé » | oui |
| S6 | mineur | antisèche, l. 27 | Forme de l’offre | « sans la validation d’une personne » → « sans la validation d’une personne habilitée » | oui |
| S7 | important | antisèche, l. 39 | Les noms interdits manquaient, alors que la couverture en affiche un | « “Nos clients”, une référence ou un témoignage. » → « … ; les noms Medhi, BOJ.ART, Strates. » | oui |
| S8 | important | antisèche, l. 42 | Même contradiction qu’en A10 ; « bon de commande dans le délai décidé (V10) » était dit deux fois sur la page (il reste l. 5) | « bon de commande dans le délai décidé (V10) ; compte rendu sous 24 heures ouvrées » → « compte rendu écrit sous 24 heures ouvrées, envoyé une fois la liste avant tout envoi cochée » ; « laisser la grille de questions » → « redire les quatre questions » | oui |
| S9 | mineur | antisèche, l. 3 | Date de la correction, sur une seule ligne | « · 10 novembre 2026 · rendez-vous le 13 novembre » → « · 10 novembre 2026, corrigé le 11 · rendez-vous le 13 » | oui |

**Exact sans retouche** : 6 500 € hors taxes, 7 800 € toutes taxes comprises, 3 250 € et 3 900 € ; trois à quatre semaines ; deux à trois heures ; une heure trente ; 40 € hors taxes à environ 190 € par mois (pages lues le 10 novembre) ; 13 novembre, 19 novembre, mi-décembre, début janvier 2027 ; les durées des cinq parties et des deux variantes ; les sept phrases 1, 2, 4, 5 et 7 ; les trois phrases de clôture, identiques dans le déroulé, « convaincre » et la fiche 10 (phrase 1). **Non ajouté, faute de place** : la règle d’arrêt et de retard (elle est à l’écran sur `garanties` et dans le déroulé, l. 78) ; « aucun paiement pendant les sept jours qui suivent la signature ».

### 2.3 Réponses aux objections

Les treize réponses ont été relues contre l’offre, le bon de commande, les fiches et les diapositives. Les réponses 2, 3, 5, 7, 9, 10, 11, 12 et 13 sont encore vraies mot pour mot (prix du cadrage, tarifs publics des éditeurs avec source et date, phrases de l’arbitrage C, calendrier, logiciel des suites, sites de réservation) ; les réponses 1, 4, 6 et 8 ont été complétées ; les autres retouches portent sur les preuves et les consignes.

| N° | Gravité | Fichier et ligne | Ce qui n’allait pas | Texte d’avant → texte d’aujourd’hui | Fait |
| --- | --- | --- | --- | --- | --- |
| O1 | mineur | objections, l. 13 (§ 1) | « Vous savez exactement ce que vous recevez » ne citait que trois des quatre résultats | « …, et trois tâches au plus à essayer. » → « …, trois tâches au plus à essayer, et le choix argumenté de la suite. » | oui |
| O2 | mineur | objections, l. 16 (§ 1) | Durée du cadrage | « ces trois semaines » → « ces trois à quatre semaines » | oui |
| O3 | important | objections, l. 17 (§ 1) | La version réduite « proposée par écrit sous deux jours » serait un envoi avant le 19 novembre | ajout : « Un écrit au client est un envoi : il ne part qu’une fois la liste avant tout envoi cochée, donc pas avant le jeudi 19 novembre ; ne pas annoncer “sous deux jours” tant que ce n’est pas tranché (comme V10). » | oui |
| O4 | important | objections, l. 23 (§ 2) | Preuve « la méthode écrite » : la seule pièce de ce nom est du 9 novembre et promet une attestation d’assurance (ligne 110) | « … ; la méthode écrite. » → « la diapositive `pourquoi-nous` (six raisons) ; la méthode écrite, c’est-à-dire la fiche 10 (…), à l’écran s’il la demande (V12) ; … Ne pas montrer la pièce “méthode et garanties” du 9 novembre : elle promet une attestation d’assurance (…, ligne 110). » | oui |
| O5 | mineur | objections, l. 42 et 43 (§ 4) | La diapositive `grille` pose quatre questions ; la réponse en donnait trois | « …, à qui appartiennent les données. » → « …, à qui appartiennent les données, qui décide. » ; ajout : « Preuve : la diapositive `grille` » | oui |
| O6 | mineur | objections, l. 56 et 57 (§ 6) | Forme du référentiel ; preuves d’aujourd’hui ; une page ne se remet que si V2 le permet | ajout de « sur ses heures de travail » ; preuve : « la diapositive `administratrice` ; la fiche 5 ; la page qui lui est destinée (…), à remettre par lui seul, et seulement si V2 permet de la laisser » | oui |
| O7 | mineur | objections, l. 67 et 68 (§ 8) | L’accord se signe avant tout document qui contient des données personnelles (bon de commande, condition 9), pas avant tout document | « avant d’en recevoir » → « avant de recevoir des documents qui contiennent des données personnelles » ; ajout : « Preuve : la fiche 8 » | oui |
| O8 | mineur | objections, l. 86 (§ 11) | Preuves d’aujourd’hui | « diapositive `hotel` » → « diapositives `hotel` et `fonctions` ; fiches 2 et 7, à l’écran s’il les demande (V12) » | oui |
| O9 | important | objections, l. 98 (§ 12) | « Laisser la grille de questions » : aucune page de ce nom, et rien ne se laisse sans V1 à V5 | « laisser la grille de questions » → « redire les quatre questions de la diapositive `grille`. Aucune page “grille de questions” n’existe à ce jour dans `pour-carlone/` ; rien ne se laisse tant qu’une case de V1 à V5 reste vide. » | oui |
| O10 | mineur | objections, l. 103 et 105 (§ 13) | L’objection naît aujourd’hui de `ambition` et `offres` ; `idees` et `ensuite` sont en annexe | « Diapositives `idees` et `ensuite`. » → « Diapositives `ambition` et `offres`, dans le fil ; `idees` et `ensuite`, en annexe. » ; ajout d’une réponse aux dates 2027, 2028, 2030, mot pour mot celle de la diapositive `ambition` | oui |
| O11 | mineur | objections, l. 3 et 5 | Date et portée de la relecture | en-tête complété ; phrase « Relecture du 11 novembre 2026 (audit final) : … » | oui |

### 2.4 Convaincre de miser sur nous

| N° | Gravité | Fichier et ligne | Ce qui n’allait pas | Texte d’avant → texte d’aujourd’hui | Fait |
| --- | --- | --- | --- | --- | --- |
| C1 | important | convaincre, l. 21 | La preuve citait « ensuite », passée en annexe ; `ambition` et `offres` portent aujourd’hui ce message | « Les diapositives “ensuite” et “moyens supplémentaires”, chiffres honnêtes » → « Les diapositives “ambition” (2030) et “offres” (quatre niveaux), selon V11, puis “moyens”, selon V7 ; “ensuite” est passée en annexe ; chiffres honnêtes, aucun gain promis » | oui |
| C2 | important | convaincre, l. 28 | L’essai : « au plus » et « une seule tâche » ; l’exemple réunissait deux tâches | « Un essai de huit semaines sur la priorité n° 1 (par exemple : le registre des bâtiments et le choix du logiciel des suites) » → « Un essai de huit semaines au plus, sur une seule tâche de la priorité n° 1 (par exemple : le registre des bâtiments, ou le choix du logiciel des suites), commandé à part » ; troisième colonne alignée sur la fiche 10 | oui |
| C3 | important | convaincre, l. 43 et 44 | « Trois horizons » désignait essai, ensuite, plus tard ; dans le référentiel, les horizons sont 2027, 2028, 2030 | « Trois horizons : essai (dans les huit semaines), … » → « Trois temps (colonne “Quand ?” des fiches et des pages) : essai (dans un essai de huit semaines au plus, après le cadrage), … » ; ligne ajoutée : « Trois horizons pour l’ambition : 2027, 2028, 2030, dits comme une vision, jamais comme un calendrier ; aucune date pour la robotique. » | oui |
| C4 | mineur | convaincre, l. 19 | « Il garde tout » : l’acompte nous reste en cas d’arrêt | « il garde tout ; comptes à son nom » → « il garde le travail fait, le dossier une fois le prix dû payé, ses comptes et ses données » | oui |
| C5 | mineur | convaincre, l. 16 et 20 | Une diapositive ne se corrige pas en direct ; preuves d’aujourd’hui | « Diapositive “compris” corrigée avec lui en direct » → « Diapositives “compris” et “univers”, corrigées avec lui à voix haute (Mathys note) » ; ligne « administratrice » : ajout de la diapositive et de la fiche 5 | oui |
| C6 | mineur | convaincre, l. 3 | Date et portée de la relecture | en-tête complété | oui |

Les dates des « cent premiers jours » (janvier, février et mars, avril 2027) sont celles de la fiche 10. Les trois phrases de clôture sont identiques dans les trois documents.

### 2.5 À relire avec Mathys

| N° | Gravité | Fichier et ligne | Ce qui n’allait pas | Texte d’avant → texte d’aujourd’hui | Fait |
| --- | --- | --- | --- | --- | --- |
| R1 | important | à relire, l. 7 | Les durées ne tiennent pas si la lecture se fait en séance : environ 11 000 mots pour la séance 1 et 26 000 pour la séance 2 | paragraphe ajouté : « Ces durées ne tiennent que si chacun a lu avant, seul … Sans cette lecture, compter plutôt six à sept heures à deux. » | oui |
| R2 | mineur | à relire, l. 16 | Compte et objet des choix (note interne, § 3, points 1 à 10 depuis sa mise à jour du 11 novembre) | « Les dix choix sur le bon de commande » → « Les dix choix qui restent sur l’offre et le bon de commande (§ 3, points 1 à 10 : …) » | oui |
| R3 | mineur | à relire, l. 17 | Deux pièces du sommaire manquaient à la séance 1 | ligne ajoutée : questions pour l’avocat ; démarches d’immatriculation et d’assurance (avocat, deux devis d’assurance avant vendredi, date des statuts) | oui |
| R4 | mineur | à relire, l. 23 et 31 | Comptes à écrire | « les 28 diapositives du fil et les 8 de l’annexe » → « 36 diapositives : les 28 du fil et les 8 de l’annexe, avec leurs notes d’orateur » ; maquette : « (onze écrans) », et la question de la décision n° 20 | oui |
| R5 | mineur | à relire, l. 33 | L’essai | « dans un essai de huit semaines » → « dans un essai de huit semaines au plus, sur une seule tâche » | oui |
| R6 | mineur | à relire, l. 34, 36 et 38 | L’annexe de la page « moyens », l’échéancier et les deux pages du cadrage manquaient ; les pièces du 9 novembre n’étaient pas écartées | annexe ajoutée à la ligne « moyens » ; « À ne relire que si vous laissez ou envoyez des documents » avec les chemins du bon de commande (trois pages), de la proposition, du document sur le cabaret et de son échéancier, des deux pages du cadrage ; ligne « À ne pas montrer vendredi : les pièces du 9 novembre … » | oui |
| R7 | mineur | à relire, l. 51 | Trois faits rapportés manquaient à la question | ajout : « une galerie d’art », « plusieurs bâtiments et commerces », « administratrice engagée récemment » | oui |
| R8 | mineur | à relire, l. 3 | Date de la relecture | en-tête complété | oui |

**Les durées annoncées.** Séance 3 (une heure) : une répétition de trente-deux minutes et treize objections à deux minutes chacune font cinquante-huit minutes ; elle tient, sans reprise. Séances 1 et 2 : elles ne tiennent qu’avec la lecture faite avant (R1 ; point D18). Aucun renvoi à un fichier daté du 11 novembre n’a été ajouté.

### 2.6 Feuille de décisions (faits et renvois seulement)

| N° | Gravité | Fichier et ligne | Ce qui n’allait pas | Texte d’avant → texte d’aujourd’hui | Fait |
| --- | --- | --- | --- | --- | --- |
| F1 | important | feuille, l. 26 (V10) | La diapositive `decision` ne dit plus « sous deux jours » | « (“sous deux jours”, diapositive `decision`) » → « (“sous deux jours” dans la version précédente ; aujourd’hui, la diapositive `decision` affiche “Après ce rendez-vous”, sans délai, et “Un bon de commande d’une page”, alors que le projet en compte trois avec ses conditions) » ; recommandation et cases inchangées | oui |
| F2 | important | feuille, l. 71 (arbitrage B) | La parenthèse annonçait encore « sous deux jours », que V10 juge intenable | « bon de commande envoyé sous deux jours » → « bon de commande envoyé dans le délai fixé en V10, et non plus “sous deux jours” » | oui |
| F3 | mineur | feuille, l. 88 (n° 2) | Le texte « nettoyé » existe ; son chemin manquait | ajout : « Le texte nettoyé existe en projet : `pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md` » | oui |
| F4 | mineur | feuille, l. 92 (n° 6) | « Avant la v12 » : la version 12 existe et affiche le prix ; la ligne 32 la passe en P0 | « P2, avant la v12 » → « P0, jeudi 12 nov. (était P2, avant la v12 : la version 12 existe, et sa diapositive `proposition` affiche déjà ce prix) » | oui |
| F5 | important | feuille, l. 93 (n° 7) | Le bon de commande ne tient pas sur une page | « le bon de commande d’une page » → « le bon de commande (le projet fait trois pages avec ses conditions, et non une) » | oui |
| F6 | mineur | feuille, l. 106 (n° 20) | Les écrans cités ne sont plus ceux de la présentation ; la maquette est passée de trois à onze écrans | « (fiche bâtiment, échéances, trois devis) » → « (dans la version 12 : vue d’ensemble, carte des fonctions et trois devis dans le fil, captures sur les diapositives des projets, fiche d’un bâtiment en annexe ; la maquette compte aujourd’hui onze écrans, et non trois) » | oui |
| F7 | mineur | feuille, l. 107 (n° 21) | Les documents clients disent partout « au plus » | « “essai de huit semaines” » → « “essai de huit semaines au plus” (forme des documents clients d’aujourd’hui) » ; à défaire si cette retouche est jugée toucher à la recommandation | oui |
| F8 | mineur | feuille, l. 123 (partie 4, statuts) | Le livrable 7 est écrit | « Voir `interne/prealables/` (livrable 7, à écrire) » → « Voir `interne/prealables/2026-11-10-demarches-immatriculation-et-assurance.md` (livrable 7, écrit le 10 novembre) » | oui |
| F9 | mineur | feuille, l. 132 (partie 4, « moyens ») | Le titre cité est celui de la page, pas celui de la diapositive | « Montrer la diapositive “Ce que des moyens supplémentaires nous permettraient d’accomplir” » → « Montrer la diapositive `moyens`, titrée aujourd’hui “Ce que plus de moyens nous permettraient” (la page client garde le titre …) » | oui |
| F10 | mineur | feuille, l. 150 (partie 6) | Renvoi faux : les n° 12 et 26 du document 01 ne sont pas en partie 4 | « reprises en partie 4 : n° 3, 6, 8, 9, 10, 11, 12, 13, 14, 16, 26 » → « n° 3, 6, 8, 9, 10, 11, 13, 14 et 16 sont reprises en partie 4 (les n° 11 et 13 sous leurs codes D12 et D47) ; la n° 26 … est dans l’arbitrage B, partie 2 ; la n° 12 (une seule description du cadrage : D46, D51) n’a pas de ligne dans cette feuille » | oui |
| F11 | mineur | feuille, l. 3 et 9 | Date et portée de la mise à jour | en-tête complété ; paragraphe « Mise à jour du 11 novembre 2026 (audit final). Aucune case n’est cochée, aucune recommandation n’est changée, rien n’est tranché. … » | oui |

**Vérifié et laissé tel quel dans la feuille.** Les lignes V6, V7, V8, V9, V11, V12, V13 et V14 décrivent l’état réel : `ensuite` est en annexe (rang 30) ; `moyens` est après `decision` (rang 27, 45 secondes) ; `enjeux`, `ambition` et `offres` sont dans le fil (rangs 6, 21, 23) ; les durées de V14 sont celles du déroulé. Les deux lignes de V8 sont bien aux lignes 109 et 116 du document du 9 novembre (3 000 € HT et 2 300 € HT). L’arbitrage A cite juste : texte client aux lignes 15 à 182, note interne à partir de la ligne 186, tiers nommé ligne 27. L’arbitrage C cite juste : 15 700 à 18 700 € HT ; 22 200 à 25 200 € HT avec le cadrage (15 700 + 6 500 ; 18 700 + 6 500). Les vingt et une décisions suivent la note a4, § 10 (lignes 469 à 512). Les jours de la semaine sont exacts (12, 13, 16, 19, 27 et 30 novembre, 31 décembre 2026, 4 et 29 janvier 2027). Les quinze chemins cités existent. La table de la partie 6 couvre bien les trente décisions du document 01.

@@SUITE@@
