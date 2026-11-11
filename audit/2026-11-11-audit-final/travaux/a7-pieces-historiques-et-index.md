# A7 — Pièces historiques et index du dossier pour-carlone

Document interne — ne pas transmettre à GianLuca Carlone · 11 novembre 2026

**Angle.** Les pièces anciennes de `pour-carlone/` et de `audit/2026-11-04-audit-strategique/pour-gianluca/` : ce qu’elles sont, leur statut, ce qu’elles contiennent de contraire au référentiel du 11 novembre (brief, § 4), et comment éviter d’en montrer une par erreur le vendredi 13 novembre 2026.

**Ce qui a été écrit.** Deux fichiers : ce rapport et le nouvel index `pour-carlone/README.md`. Aucun fichier existant n’a été modifié, renommé ni déplacé. Aucune page en ligne n’a été ouverte, `crm/` n’a pas été ouvert, aucune commande git n’a été lancée. Les noms d’un ancien partenaire, de son studio et de son œuvre n’apparaissent ici que dans des citations exactes, entre accents graves, parce qu’il faut pouvoir les retrouver ; l’index n’en écrit aucun.

## En bref

1. **Le compte.** Sans le nouvel index, `pour-carlone/` contient 137 fichiers au 11 novembre 2026 : 83 en vigueur (80 du 10 novembre, 3 du 11) ; 35 à ne pas montrer sans relecture (33 pièces du 9 novembre sur les sujets du rendez-vous, 2 planches périmées du 10) ; 19 d’un autre sujet, du 31 octobre au 4 novembre (vernissage, œuvre robotisée, œuvre cinétique, laboratoire).
2. **Aucune pièce ancienne n’est en vigueur pour le 13 novembre.** Dans `pour-carlone/` : six pièces sont remplacées, deux sont historiques sans remplaçante exacte, douze relèvent d’un autre sujet. Dans `pour-gianluca/` : deux propositions sont remplacées, le message de recadrage n’a pas de remplaçant.
3. **Huit constats bloquants avant vendredi** (§ 3, n° 1 à 8). Le plus sûr de se produire était la couverture de la version 12, qui affichait et faisait dire le nom d’un dossier retiré de l’offre : relevé aussi par les angles a1, a2 et a3, corrigé dans la source pendant l’audit ; il reste à republier la page et à refaire deux copies (n° 2). Les autres tiennent à une pièce ouverte par erreur : le guide du dossier de la présentation donne pour « version vivante » l’adresse de la version 11 (n° 3) ; le sommaire de la racine range le vernissage, la proposition artistique et les documents du 9 novembre sous « Les documents faits pour lui être montrés » (n° 4) ; ces pièces portent des noms retirés, l’ancien taux à la journée, l’ancienne formule mensuelle, des prix autres que le cadrage, un autre montant sous le mot « cadrage » et deux promesses d’attestation d’assurance (n° 5 à 8).
4. **Quinze textes de mention datée sont proposés**, prêts à coller : M1 à M13 au § 5, deux autres dans les constats n° 15 et n° 25. Aucun ne crée de ligne : les numéros de ligne cités ailleurs ne bougent pas. Aucun n’a été ajouté.
5. **Le sommaire de la racine** (`README.md`, « État au 4 novembre 2026 ») est faux ou périmé sur vingt points (§ 6).
6. **L’index est écrit** : `pour-carlone/README.md`, trois parties. Contrôles : `lint-doc.js --interne`, 0 erreur et 0 alerte ; les 67 chemins cités existent ; 5 pages en rendu compact. Il sert de liste datée des pièces marquées, demandée par les décisions D06 et D07 de l’audit du 4 novembre, dont l’échéance est le vendredi 13 novembre 2026.

## 1. Méthode et limites

- **Liste.** Tous les fichiers et dossiers de `pour-carlone/` listés par Glob, puis comptés. Le dossier a bougé pendant l’audit : trois pièces du 11 novembre sont apparues dans `offre-cadrage/`. Compte arrêté à 137 fichiers, sans l’index. Répartition : § 2.
- **Lus en entier.** `pour-carlone/vernissage-strates-idees.md` ; les quatre documents du 9 novembre et le guide de `pour-carlone/logiciels-et-automatisations/` ; `pour-carlone/presentation-ia/README.md` ; `deck.json` de la version 11 ; les trois fichiers de `pour-gianluca/` ; `README.md` de la racine ; `interne/contexte-projet-carlone.md` ; le sommaire du 10 novembre ; l’offre en une page ; la proposition du 10 novembre ; la feuille de décisions ; `audit/2026-11-04-audit-strategique/README.md`.
- **PDF.** Texte extrait par `pdftotext` (lecture seule), cité par page (« p. 4 »). Les pages ont aussi été regardées en vignettes.
- **Images et films.** Nom et dossier, comme demandé. En plus : une planche réduite de toutes les images, des recadrages à taille réelle des enseignes et des plaques, les bandes haute et basse à taille réelle de neuf images, les métadonnées des deux films, quatre images extraites des films, et les deux planches de la version 12. But : chercher une mention « généré par IA » dans l’image, des noms visibles et des états périmés.
- **Version 11.** Les 26 diapositives ont été parcourues par recherche de mots ; treize ont été lues en entier.
- **Contrôle mécanique.** `lint-doc.js` lancé en mode client, en lecture seule, sur les dix fichiers `.md` anciens (§ 4.9). Chiffres donnés avec la version de l’outil du 10 novembre à 23 h 55, qui contrôle en plus les noms des dossiers de création et le mot « fuite ».
- **Non fait.** Aucune page en ligne ouverte : ni la version 11, ni la version 12, ni la maquette. Le texte de la version 12 n’est pas audité ici, sauf sa couverture, parce que son image vient d’une pièce ancienne. Les pièces anciennes de `interne/` ont été regardées par leur titre, leur date et leurs premières lignes seulement (§ 2.4).
- **Portée des statuts.** « En vigueur » veut dire : préparé pour le rendez-vous. Tout document client reste un projet non envoyé tant que les décisions V1 à V5 ne sont pas prises. Les statuts sont un constat de cet audit, à confirmer par Morgan Olsen et Mathys Couet (D06, D07) : rien n’est tranché ici.
- **Pièces en mouvement.** La feuille de décisions a été retouchée pendant l’audit et ses lignes ont bougé : elle est citée ici par partie et par décision, jamais par numéro de ligne. Les autres numéros de ligne ont été contrôlés par script à la fin de l’audit : 147 citations justes ; trois ont changé parce que la pièce a été corrigée entre-temps (couverture de la version 12, outil de contrôle), ce que disent les constats n° 2 et n° 20. Les lignes des pièces du 10 et du 11 novembre peuvent encore bouger ; chaque citation donne le texte à retrouver.
- **Typographie.** Apostrophes et guillemets français ; espaces ordinaires avant les signes doubles, comme dans le brief et les pièces du 10 novembre, pour que les retouches par recherche exacte restent possibles.
- **Abréviation.** Dans les tableaux, « …/ » abrège `pour-carlone/logiciels-et-automatisations/`.

## 2. Tableau complet des pièces et de leur statut

### 2.1 En vigueur pour le 13 novembre (83 fichiers, datés du 10 ou du 11 novembre 2026)

| Dossier de `pour-carlone/` | Fichiers | Rôle |
| --- | --- | --- |
| `presentation-ia/2026-11-10-version-12-projet/` | 38 : `LISEZ-MOI.md`, `project/deck.json`, `project/slides/` (36 diapositives) | La présentation : version 12, 36 diapositives, 28 dans le fil, 8 en annexe |
| `offre-cadrage/` | 7 : `2026-11-10-offre-en-une-page.md`, `2026-11-10-une-page-pour-votre-administratrice.md`, `2026-11-10-proposition-de-cadrage-version-client.md`, `2026-11-10-projet-de-bon-de-commande.md`, `2026-11-11-tableau-qui-valide-quoi.md`, `2026-11-11-projet-de-formulaire-de-retractation.md`, `2026-11-11-projet-d-accord-sur-les-donnees.md` | L’offre et ses pièces jointes ; la page d’offre fait foi |
| `fiches/` | 12 : `2026-11-10-fiche-01-…` à `2026-11-10-fiche-12-…` | Les douze fiches |
| `developpement/` | 8 pages datées du 10 novembre | Pourquoi nous, jusqu’où, présence en ligne, moyens supplémentaires |
| `logiciels-et-automatisations/` | 1 sur 6 : `2026-11-10-vos-suites-un-logiciel-du-marche-bien-choisi.md` | La page sur le logiciel des neuf suites |
| `maquettes/2026-11-10-ecrans-d-exemple/` | 13 : `index.html`, `LISEZ-MOI.md`, `images/` (11 images) | La maquette du logiciel, onze écrans, données fictives |
| `cabaret-et-commerces/` | 2 : `2026-11-10-autorisations-et-echeances.md`, `2026-11-10-echeancier.xlsx` | Autorisations et échéances |
| `cadrage/` | 2 : `2026-11-10-questionnaire-preparatoire.md`, `2026-11-10-liste-des-pieces-a-rassembler.md` | Pour démarrer le cadrage |

Les trois pièces du 11 novembre figurent dans `outils/2026-11-11-dossier/manifeste.json`. Ce manifeste, qui construit le dossier relié du rendez-vous, ne cite aucune pièce ancienne : contrôlé.

### 2.2 Pièces anciennes ou périmées de `pour-carlone/` (54 fichiers)

Statuts possibles : « en vigueur pour le 13 novembre » ; « remplacée par … » ; « historique : ne pas montrer sans relecture » ; « autre sujet, hors du rendez-vous ». Aucune de ces pièces n’a le premier.

| N° | Pièce (chemin depuis `pour-carlone/`) | Date | Ce qu’elle est | Statut | Remplaçante, ou raison |
| --- | --- | --- | --- | --- | --- |
| P1 | `vernissage-strates-diaporama.pdf` | 4 nov. 2026 (« Novembre 2026 », p. 1) | Diaporama de 12 pages « pour M. Carlone » : une soirée de vernissage en cinq temps, trois formats chiffrés | Autre sujet, hors du rendez-vous | Événement reporté sans date (`audit/2026-11-04-audit-strategique/annexes/travaux/strategie-retenue.md:646`) ; détail § 4.2 |
| P2 | `vernissage-strates-idees.md` | 4 nov. 2026 (l. 3) | Document de travail du même événement : parcours, vingt et une idées, trois formats, façon de l’ajouter à l’offre | Autre sujet, hors du rendez-vous | Ce n’est pas un document client : il tutoie Morgan Olsen (l. 104) ; détail § 4.1 |
| P3 | `visuels/` : `1-source.png`, `2-couche-par-couche.png`, `3-main-et-machine.png`, `4-devoilement.png`, `5-diner-des-strates.png`, `6-fossiles-de-la-loire.png` | 4 nov. 2026 (P2, l. 29) | Six visuels du vernissage, générés par IA | Autre sujet, hors du rendez-vous | Aucune mention dans l’image ; le premier sert de couverture à la version 12 (constat n° 2) |
| P4 | `strates-proposition-artistique-v1.1.pdf` | 2 nov. 2026, version 1.1 | Proposition artistique et technique de 8 pages : un relief peint par un bras robotisé | Autre sujet, hors du rendez-vous | Projet gelé (`strategie-retenue.md:644`), option retirée (`:412`) ; détail § 4.3 |
| P5 | `strates/bras-robotique-concept-ia-10s.mp4` | 2 nov. 2026 (film joint à P4, p. 8) | Film de concept de 10 secondes | Autre sujet, hors du rendez-vous | Généré par IA ; le bandeau incrusté porte le nom du projet |
| P6 | `strates/relief-mineral-bleu-galerie.png` | 2 nov. 2026 (image de P4, p. 2) | Mise en situation fictive du relief dans une galerie | Autre sujet, hors du rendez-vous | Générée par IA, sans mention dans l’image |
| P7 | `visuels-recuperes-pdf/riviere-ultramarine-extrait-pdf.png`, `visuels-recuperes-pdf/bras-peignant-relief-fluvial-extrait-pdf.png` | Extraites le 4 nov. 2026 de P4 (p. 1 et p. 3) | Deux images tirées du PDF | Autre sujet, hors du rendez-vous | Générées par IA, sans mention dans l’image |
| P8 | `visuels-recuperes-pdf/bras-educatif-cube-rouge-extrait-pdf.png` | Extraite le 4 nov. 2026 d’un PDF interne du 30 oct. (`interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf`, p. 9) | Bras robotisé sur un banc d’essai | Autre sujet, hors du rendez-vous | Plaque au nom de l’ancien partenaire ; origine interne. Une version recadrée, sans la plaque, illustre la diapositive `robotique` de la version 12 |
| P9 | `eclosion/concept-2026-10-31.pdf` | 31 oct. 2026, v0.1 | Concept d’une œuvre cinétique, 5 pages, « préparé pour Morgan Olsen » (p. 1) | Autre sujet, hors du rendez-vous | Document interne rangé dans le dossier client ; détail § 4.5 |
| P10 | `eclosion/animation-concept-1080p-2026-10-31.mp4` | 31 oct. 2026 | Animation de 8 secondes de la même œuvre | Autre sujet, hors du rendez-vous | Plaque au nom de l’ancien partenaire ; aucune mention IA dans les trois images regardées |
| P11 | `eclosion/visuel-fleur-cinetique.png` | Non daté (même concept) | Visuel de l’œuvre | Autre sujet, hors du rendez-vous | Même plaque ; aucune mention IA |
| P12 | `laboratoire-ia-robotique/visuels/atelier-pilote.png`, `laboratoire-ia-robotique/visuels/laboratoire-ia-art-robotique.png` | Non datés ; rangés le 4 nov. 2026 | Deux visuels d’un laboratoire | Autre sujet, hors du rendez-vous | Option retirée (`strategie-retenue.md:645`) ; locaux à l’enseigne de Marwin Tech qui n’existent pas ; détail § 4.4 |
| P13 | `logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md` | 9 nov. 2026 ; mention du 10 nov. (l. 179) | Proposition chiffrée « Votre logiciel de gestion des propriétés » | Remplacée par `fiches/2026-11-10-fiche-07-le-logiciel-de-gestion-de-vos-proprietes.md` et `logiciels-et-automatisations/2026-11-10-vos-suites-un-logiciel-du-marche-bien-choisi.md` | Ses prix ne se disent pas tant que V1 (arbitrage C) et V8 ne sont pas tranchées ; détail § 4.6 |
| P14 | `logiciels-et-automatisations/2026-11-09-annexe-specification-logiciel-gestion-proprietes.md` | 9 nov. 2026 | Spécification en neuf modules, sans prix | Historique : ne pas montrer sans relecture | Traite l’hébergement comme une option à confirmer et renvoie aux prix de P13 ; pour le rendez-vous, la fiche 7 et la maquette en tiennent lieu ; détail § 4.7 |
| P15 | `logiciels-et-automatisations/2026-11-09-logiciels-sur-mesure-methode-et-garanties.md` | 9 nov. 2026 | Méthode, propriété, maintenance, continuité | Remplacée par `fiches/2026-11-10-fiche-10-travailler-avec-nous.md`, `fiches/2026-11-10-fiche-08-vos-donnees-et-la-securite.md` et la fiche 7 | Attestation d’assurance promise (l. 110) ; détail § 4.8 |
| P16 | `logiciels-et-automatisations/2026-11-09-automatisations-fiches-detaillees.md` | 9 nov. 2026 | Quinze fiches d’automatisation chiffrées et les 47 aides de la version 11 | Remplacée par les douze fiches de `fiches/` et `developpement/2026-11-10-une-idee-pour-chacun-de-vos-projets.md` | Un prix par automatisation ; détail § 4.8 |
| P17 | `logiciels-et-automatisations/README.md` | 9 nov. 2026 ; ajout du 10 nov. (l. 34) | Guide des quatre documents du 9 novembre | Remplacée par `pour-carlone/README.md` | Présente encore P13 à P16 comme le dossier à lire |
| P18 | `presentation-ia/2026-11-09-version-11/` : `project/deck.json` et 26 diapositives (27 fichiers) | 9 nov. 2026 | Présentation « L’IA au service de vos projets », version 11 | Remplacée par `presentation-ia/2026-11-10-version-12-projet/` | Détail § 4.8 |
| P19 | `presentation-ia/README.md` | 9 nov. 2026 | Guide des sources de la présentation | Remplacée par `pour-carlone/README.md` et `presentation-ia/2026-11-10-version-12-projet/LISEZ-MOI.md` | Son lien « version vivante » ouvre la version 11 |
| P20 | `presentation-ia/2026-11-10-version-12-projet/planche-du-fil-principal.png`, `presentation-ia/2026-11-10-version-12-projet/planche-nouvelles-diapositives.png` | 10 nov. 2026, à 2 h 39 et à 0 h 51 (dates des fichiers) | Deux planches de contrôle d’états antérieurs de la version 12 | Historique : ne pas montrer sans relecture | Périmées le jour même par la refonte de la nuit ; la page en ligne et `project/` font foi ; détail : constat n° 14 |

D’après le brief du 9 novembre (`audit/2026-11-09-audit-presentation-et-offre/travaux/BRIEF.md:23`, rapporté, non vérifié), GianLuca Carlone aurait déjà reçu des dossiers de création (P1 à P12, en tout ou partie). La liste écrite de ce qu’il a vu ou reçu reste à dresser par Morgan Olsen (feuille de décisions, partie 4).

### 2.3 Pièces de `audit/2026-11-04-audit-strategique/pour-gianluca/` (3 fichiers)

| N° | Pièce | Date | Ce qu’elle est | Statut | Remplaçante, ou raison |
| --- | --- | --- | --- | --- | --- |
| G1 | `proposition-de-cadrage.md` | 4 nov. 2026 | Premier projet de proposition de cadrage, suivi d’une note interne (l. 120 à 151) | Remplacée par `pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md` (après l’étape G2) | Détail § 4.8 |
| G2 | `2026-11-09-proposition-de-cadrage.md` | 9 nov. 2026 | Proposition mise à jour (administratrice, quatre résultats), suivie d’une longue note interne (l. 186 à 407) | Remplacée par la même pièce du 10 novembre ; pour les clauses, `pour-carlone/offre-cadrage/2026-11-10-projet-de-bon-de-commande.md` ; pour ce qui fait foi, `pour-carlone/offre-cadrage/2026-11-10-offre-en-une-page.md` | Détail § 4.8 |
| G3 | `message-de-recadrage.md` | 4 nov. 2026 | Projet de message d’une page, signé des deux associés | Historique : ne pas montrer sans relecture | Aucune pièce ne le remplace ; il propose un premier rendez-vous à une date abandonnée ; détail § 4.8 |

### 2.4 Pièces anciennes de `interne/` (pour mémoire : jamais montrées)

| Pièce | Date | Ce qu’elle est | À savoir |
| --- | --- | --- | --- |
| `interne/contexte-projet-carlone.md` | 4 nov. | Contexte réuni : personnes, chronologie, chantiers | Décrit l’offre du 2 novembre comme prête (l. 57, 64 à 83) ; le sommaire de la racine en fait encore « le point de départ » |
| `interne/offre-marwin-tech-remuneration-et-collaboration.md` | 2 nov. | Offre de six mois, abandonnée | Sa ligne 7 dit que des sections « peuvent servir de base à la proposition écrite » : ne jamais en extraire (constat n° 25) |
| `interne/audit-marwin-tech-carlone.md` | 2 nov. | Audit de l’offre de six mois | Verdict « L’offre tient » (l. 7), contredit par l’audit du 4 novembre |
| `interne/offres-de-carlone-catalogue-crm.md` | 2 nov. | Catalogue d’offres de vente d’œuvres | Argument fiscal ; brouillon à valider par un expert-comptable |
| `interne/state-of-the-art-note-de-vision.md` | 2 nov. | Note de vision | Projet commun avec l’ancien partenaire |
| `interne/complement-chatgpt-2026-11-04.md`, `interne/recueil-sessions-chatgpt-2026-11-04.html`, `interne/recueil-sessions-chatgpt-2026-11-04.txt` | 4 nov. | Complément et recueil de conversations | Portent l’ancien prénom erroné du client (règles : `audit/2026-11-04-audit-strategique/annexes/correction-identite.md`) |
| `interne/strates-audit-robotique-ia.pdf` | 2 nov. | Audit robotique de l’œuvre, 12 pages | Projet gelé |
| `interne/archives-marwin-tech/` (3 fichiers) | 29 et 30 oct. | Choix de structure (7 pages) ; options de structure et de rémunération, version 5 (26 pages) et son original compressé | La version 5 a la forme d’une proposition au client, avec l’ancien prénom en page 1 : jamais transmise |
| `interne/eclosion/` (26 fichiers) | 31 oct. | Ébauche mécanique, sources, prototype numérique | Aucun essai physique |
| `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` | 31 oct. | Audit du laboratoire, 11 pages | Option retirée |
| `interne/strates/archives-investisseur/` (2 fichiers) | 2 nov. | Dossier investisseur (23 pages) et budget | Ancien scénario : « 10 000 EUR pour cadrer et mesurer », « 325 000 EUR en trois tranches » (p. 1) |
| `interne/logiciels-et-automatisations/README.md`, `2026-11-09-etude-gestion-proprietes-offre-accord-et-prix.md`, `2026-11-09-mise-a-jour-accor-et-comparaison.md`, `travaux/` (3 fichiers) | 9 nov. | Étude interne du logiciel et de l’autre proposition | Nomment l’autre prestataire et son prix ; la mise à jour porte « Rédaction en cours » (l. 12) |

Aucune des six pièces `.md` de la racine de `interne/` ne porte la mention « Document interne — ne pas transmettre à GianLuca Carlone » (brief, § 3) : elles datent d’avant cette règle.

## 3. Constats

Colonne « Fait » : « oui » si la correction est faite par cet audit ; « non » si elle reste à faire par le coordinateur ; « à décider par les associés » si elle dépend d’un choix. Les mentions M1 à M13 sont au § 5.

| N° | Gravité | Fichier et ligne | Ce qui ne va pas | Texte actuel → texte proposé | Fait |
| --- | --- | --- | --- | --- | --- |
| 1 | Bloquant avant vendredi | `pour-carlone/` (137 fichiers) | Rien ne disait, au même endroit, ce qui est en vigueur : 54 pièces anciennes ou périmées côtoient 83 pièces à jour | Aucun index → `pour-carlone/README.md`, en trois parties | Oui |
| 2 | Bloquant avant vendredi | `pour-carlone/presentation-ia/2026-11-10-version-12-projet/project/slides/cover.html:11` et `:12` ; repris par `interne/rendez-vous/2026-11-11-presentation-texte-des-36-diapositives.md:11` et `:13` | La première diapositive affichait le nom d’un dossier retiré de l’offre, et la note le faisait dire à voix haute : nom interdit dans un document client (brief, § 4 ; `strategie-retenue.md:661`). Relevé aussi par a1 (n° 1), a2 (D2) et a3 (H5) ; la source a été corrigée le 10 novembre à 23 h 56, pendant cet audit. Ce que cet angle ajoute : l’image est le premier visuel du vernissage (`pour-carlone/visuels/1-source.png` ; même fichier dans la copie de rendu de la session, contrôlé à l’œil), que l’audit du 9 novembre recommandait d’écarter (`audit/2026-11-09-audit-presentation-et-offre/01-audit-de-la-presentation.md:319`) ; l’ancien libellé reste dans le texte des 36 diapositives (l. 11 et 13), sur la planche périmée (constat n° 14) et, cité, dans le mode d’emploi de la version 12 (l. 18) | Dans la source, c’est fait : `Visuel : vision générée par IA — dossier Strates` → `Visuel : vision générée par IA`. Reste : republier la page en ligne (non vérifiable ici) ; régénérer `interne/rendez-vous/2026-11-11-presentation-texte-des-36-diapositives.md` ; refaire ou écarter la planche | Oui dans la source (par le coordinateur) ; non pour la page en ligne et les deux copies ; choix de l’image : à décider par les associés (feuille de décisions, partie 4, ligne « Structure de la version 12 » : « image de couverture encore ouverte ») |
| 3 | Bloquant avant vendredi | `pour-carlone/presentation-ia/README.md:3` et `:9` | Ce guide du dossier de la présentation donne pour « version vivante » l’adresse de la version 11 : 26 diapositives, dont celle sur le fichier de prospection, et deux mentions d’assurance (§ 4.8). Son tableau n’a ni ligne ni adresse pour la version 12 | Fin de la ligne 3 : ajouter M8 | Non |
| 4 | Bloquant avant vendredi | `README.md:11` et `:15` à `:19` (racine) | Le sommaire range sous `Les documents faits pour lui être montrés.` le vernissage, la proposition artistique et les documents du 9 novembre ; aucune pièce en vigueur n’y est décrite | Fin des lignes 3 et 11 : ajouter M1 et M2 | Non |
| 5 | Bloquant avant vendredi | `pour-carlone/vernissage-strates-diaporama.pdf`, p. 1, 6, 7, 9, 10, 11, 12 | Diaporama d’aspect proche de la présentation, posé à la racine du dossier client : noms retirés de l’offre, taux à la journée (p. 10), trois formats chiffrés (p. 10), ancienne formule mensuelle (p. 11), promesse d’un devis par format (p. 12) | Un PDF ne reçoit pas de mention : statut inscrit dans l’index (partie 3) et dans M1, M2 ; option M10 | Oui pour l’index ; non pour les mentions |
| 6 | Bloquant avant vendredi | `pour-carlone/strates-proposition-artistique-v1.1.pdf`, p. 4 | Un autre montant sous le mot « cadrage » : `Les 10 000 EUR envisagés pour le cadrage restent une enveloppe de discussion, non engagée.` Le référentiel ne connaît qu’un cadrage, à 6 500 € hors taxes. Même page : `323 875 EUR HT` et `25 000 EUR HT` | Statut inscrit dans l’index (partie 3) et dans M1, M2 ; option M10 | Oui pour l’index ; non pour les mentions |
| 7 | Bloquant avant vendredi | `…/2026-11-09-logiciel-gestion-proprietes-proposition.md:10`, `:44`, `:109` à `:116`, `:124` à `:126`, `:132`, `:133`, `:139` ; `…/2026-11-09-automatisations-fiches-detaillees.md:22`, `:98`, `:128` à `:142` et les quinze lignes « Coût indicatif » | Prix autres que le cadrage, contre la règle « seul le cadrage a un prix » (brief, § 4 ; DL1). Deux lignes se recouvrent pour le choix du logiciel : 3 000 € HT (l. 109) et 2 300 € HT (l. 116), objet de V8 | Fin de la ligne 3 de chaque pièce : ajouter M3 et M6 | Non ; sort de ces prix : à décider par les associés (V1, arbitrage C ; V8) |
| 8 | Bloquant avant vendredi | `…/2026-11-09-logiciel-gestion-proprietes-proposition.md:99` ; `…/2026-11-09-logiciels-sur-mesure-methode-et-garanties.md:110` | Deux promesses d’attestation d’assurance, alors qu’aucune n’existe (feuille de décisions, E5, et partie 4, ligne « Souscrire l’assurance »). Le sommaire du 10 novembre les laissait « à trancher » (`audit/2026-11-10-preparation-des-livrables/README.md:55`) | l. 99 : `Avant la première commande, nous vous remettons l'attestation de notre responsabilité civile professionnelle.` ; l. 110 : `Avant tout démarrage, nous vous remettons […] l'attestation de notre assurance de responsabilité civile professionnelle` → texte conservé, corrigé par M3 et M5 | Non |
| 9 | Important | Treize images et un film de `pour-carlone/visuels/`, `strates/`, `visuels-recuperes-pdf/`, `eclosion/`, `laboratoire-ia-robotique/visuels/` | Générés par IA, sans mention dans l’image : montrés seuls, ils passent pour des photos. Quatre portent le nom de l’ancien partenaire ; deux montrent des locaux à l’enseigne de Marwin Tech qui n’existent pas (§ 4.4) | Statut inscrit dans l’index (partie 3) : ne jamais les montrer seuls | Oui |
| 10 | Important | `pour-carlone/vernissage-strates-idees.md:3`, `:104` | Document de travail interne rangé dans le dossier client : tutoiement (`c'est à toi de fixer les prix`), taux à la journée, aucune mention « PROJET non envoyé » (seul `.md` ancien du dossier dans ce cas) | Fin de la ligne 3 : ajouter M9 | Non |
| 11 | Important | `pour-carlone/eclosion/concept-2026-10-31.pdf`, p. 1 et p. 5 | `préparé pour Morgan Olsen` : pièce interne rangée dans le dossier client ; taux à la journée en page 5 | Statut inscrit dans l’index (partie 3) | Oui |
| 12 | Important | `…/2026-11-09-annexe-specification-logiciel-gestion-proprietes.md:9`, `:22`, `:413` à `:415`, `:600`, `:632` | L’hébergement y est une option à confirmer (`Seulement si une activité d'hébergement reprend`), alors que les neuf suites sont le fait de départ depuis le 10 novembre ; la ligne 600 renvoie aux « dates » et aux « prix » de P13 | Fin de la ligne 3 : ajouter M4 | Non |
| 13 | Important | `pour-carlone/logiciels-et-automatisations/README.md:7`, `:13`, `:16`, `:20` à `:23` | Le guide présente encore les quatre pièces du 9 novembre comme le dossier à lire, avec « le prix indicatif » et « les 47 aides de la présentation » | Fin de la ligne 3 : ajouter M7 | Non |
| 14 | Important | `pour-carlone/presentation-ia/2026-11-10-version-12-projet/planche-du-fil-principal.png` ; `…-version-12-projet/planche-nouvelles-diapositives.png` | Deux images d’états antérieurs de la version 12, rangées à côté des sources en vigueur. La première : 26 diapositives dans le fil au lieu de 28, et `avenir` en « 1 an, 2 ans, 5 ans » au lieu de 2027, 2028, 2030. La seconde : `decision` avec « sous deux jours » (délai que V10 remet en cause) et `proposition` avec « trois tâches prêtes à essayer ». Aucun de ces textes n’est plus dans les diapositives | Refaire les deux planches à partir des sources publiées, ou ne plus s’en servir ; inscrites en partie 2 de l’index | Oui pour l’index ; non pour les planches |
| 15 | Important | `pour-carlone/presentation-ia/2026-11-10-version-12-projet/LISEZ-MOI.md:1`, `:9`, `:38`, `:44`, `:46` | Pièce du 10 novembre, donc retouchable : son titre dit « (non publiée) » alors que la ligne 5 dit qu’elle est publiée, et quatre listes d’ordre périmées (19, 26, 31, 34 diapositives) précèdent la bonne (l. 48 : 36 diapositives) | Fin de la ligne 5, ajouter : `[Mention du 11 novembre 2026 : seuls project/deck.json et le dernier paragraphe de ce fichier (36 diapositives : 28 dans le fil, 8 en annexe) décrivent la présentation publiée. Les listes d’ordre qui précèdent sont des états antérieurs du 10 novembre.]` | Non |
| 16 | Important | `audit/2026-11-04-audit-strategique/pour-gianluca/2026-11-09-proposition-de-cadrage.md:27`, `:104`, `:172`, `:186` et suivantes | Tiers nommé (l. 27) ; `relues par notre avocat` (l. 104), ce qui n’est pas fait ; date abandonnée (l. 172) ; note interne avec prix plancher et version réduite dans le même fichier (objet de l’arbitrage A) | Fin de la ligne 5 : ajouter M12 | Non ; arbitrage A : à décider par les associés (V1) |
| 17 | Important | `audit/2026-11-04-audit-strategique/pour-gianluca/proposition-de-cadrage.md:25`, `:66`, `:68`, `:106` | Tiers nommé (l. 25) ; mot interne « voie » (l. 66, 68) ; date abandonnée (l. 106) ; écrit avant l’administratrice et les neuf suites | Fin de la ligne 5 : ajouter M11 | Non |
| 18 | Important | `audit/2026-11-04-audit-strategique/pour-gianluca/message-de-recadrage.md:28`, `:34`, `:38` | Le message propose un premier rendez-vous `au plus tard le vendredi 11 décembre 2026` (l. 34) et parle de `l'embauche d'un coordinateur` (l. 28). La feuille de décisions prévoit toujours son envoi (partie 4, ligne « Message de recadrage et proposition signés, puis envoyés »), mais aucune version à jour n’existe | Fin de la ligne 5 : ajouter M13 ; écrire une nouvelle version datée après le rendez-vous | Non ; nouvelle version : à décider par les associés |
| 19 | Important | `audit/2026-11-10-preparation-des-livrables/README.md:52` | « 0 erreur sur tous les documents clients » ne vaut que pour les pièces du 10 novembre : les pièces anciennes de `pour-carlone/` donnent 89 erreurs en mode client (§ 4.9) | `0 erreur sur tous les documents clients et les 36 diapositives` → `0 erreur sur tous les documents clients datés du 10 novembre 2026 et les 36 diapositives ; les pièces antérieures de pour-carlone/ ne sont pas couvertes (voir pour-carlone/README.md)` | Non |
| 20 | Important | `outils/2026-11-10-orchestration/rendu/lint-doc.js:53` (liste `PRICE_DOC`) | L’outil a été complété pendant l’audit (noms des dossiers de création, mot « fuite »), mais il laisse toujours passer en simple alerte les prix des pièces du 9 novembre (« figure dans un document client du 9 novembre »). Avec la règle du 11 novembre, ce sont des écarts | Tant que la décision DL1 tient : lire chaque alerte de prix comme une erreur dans un document client ; changer l’outil seulement après V1 et V8 | À décider par les associés |
| 21 | Important | `audit/2026-11-04-audit-strategique/interne/14-registre-risques-inconnues-decisions.md:274` et `:275` ; `interne/decisions/2026-11-10-feuille-de-decisions.md`, partie 4, ligne « Une seule offre » | D06 et D07 (« anciennes pièces marquées “historique” ») ont pour échéance le vendredi 13 novembre 2026 ; rien n’était marqué | L’index tient lieu de liste datée ; les mentions du § 5 marquent les pièces ; les associés cochent cette ligne | Oui pour l’index ; le reste : à décider par les associés |
| 22 | Mineur | `…/2026-11-09-automatisations-fiches-detaillees.md:292` | Le mot interdit par la règle de l’audit du 4 novembre apparaît dans un autre sens (cloisonnement des accès) : `cloisonnement testé, aucune fuite sur dix essais`. L’outil le signale désormais en alerte | Pièce historique : texte conservé ; si la phrase est reprise un jour : `aucune information d’un autre lieu sur dix essais` | Non |
| 23 | Mineur | `…/2026-11-09-logiciel-gestion-proprietes-proposition.md:179` | La mention du 10 novembre ne corrige que la date du 15 décembre ; elle laisse croire que le reste tient | Complétée par M3 en ligne 3 | Non |
| 24 | Mineur | Les cinq pièces de `pour-carlone/logiciels-et-automatisations/` datées du 9 novembre | Le mot « pilote » y revient 42 fois ; le vocabulaire retenu est « un essai de huit semaines au plus » | Pièces historiques : texte conservé ; aucune reprise sans ce changement de mot | Non |
| 25 | Mineur | `interne/offre-marwin-tech-remuneration-et-collaboration.md:7` | La ligne invite à tirer de l’offre abandonnée « la proposition écrite » | Fin de la ligne 3, ajouter : `[Mention du 11 novembre 2026 : offre du 2 novembre 2026 abandonnée ; pièce historique. Ne rien en extraire pour un document client. Seule offre en vigueur : pour-carlone/offre-cadrage/2026-11-10-offre-en-une-page.md.]` | Non |
| 26 | Mineur | `sources/index-integration-chatgpt-2026-11-04.md:17` à `:20` ; `sources/reprise-59-et-visuels-2026-11-04.md:27` à `:48` | Ces index pointent vers les pièces anciennes de `pour-carlone/` ; des copies de trois visuels existent aussi dans `livrables/collecte-chatgpt-2026-11-04/`. Déplacer les pièces casserait ces liens | Ne rien déplacer ; marquer (index et mentions). La règle du 10 novembre l’impose déjà (`audit/2026-11-10-preparation-des-livrables/travaux/BRIEF-2.md:28`) | Oui (rien n’est déplacé) |
| 27 | Mineur, à vérifier | `pour-carlone/maquettes/2026-11-10-ecrans-d-exemple/images/` | Dix des onze images datent du 10 novembre à 1 h 46 ; `index.html` a été retouché à 22 h 34 (dates des fichiers). Une image comparée au texte actuel de la maquette, `ecran-accueil.png` : identique. Les neuf autres n’ont pas été comparées | Comparer à l’œil les neuf autres, ou refaire les captures à partir de `index.html` | Non |

## 4. Contenus risqués, pièce par pièce

Types cherchés : prix autre que le cadrage ; montant interne ; nom ou prix de l’autre proposition ; date abandonnée ; promesse (attestation d’assurance, résultat) ; « votre hôtel » ; nom interdit dans un document client ; visuel généré par IA non signalé.

**Résultat commun à toutes les pièces anciennes de `pour-carlone/` et de `pour-gianluca/`.** Aucune ne nomme l’autre proposition ni son prix : recherche faite dans les `.md`, les `.html`, les `.json` et le texte des trois PDF. Aucune n’écrit « votre hôtel » ; trois traitent l’hébergement comme une hypothèse (§ 4.6, § 4.7, P16 l. 116).

### 4.1 `pour-carlone/vernissage-strates-idees.md` (4 novembre)

| Type | Lignes | Citation |
| --- | --- | --- |
| Nom interdit | 5, 13, 20, 21, 22, 57, 61, 70, 90, 100, 122, 127 (prénom de l’ancien partenaire, 12 lignes) ; 9, 20, 22, 45, 65, 69, 73, 83, 88, 89, 102, 112, 127 (nom de l’œuvre) ; 13 et 129 (autres noms internes) | l. 5 : `peinte par le bras et par la main de Medhi` |
| Montant interne | 98, 111 ; 110 | `Honoraires à 750 € HT la journée` ; `au même taux de 750 € HT la journée` ; `s'il tient dans les 20 journées` |
| Prix autre que le cadrage | 100, 101, 102 | `4 500 à 7 500 €` ; `9 000 à 13 500 €` ; `15 000 à 22 500 €` |
| Offre abandonnée | 5, 108, 110, 112, 113 | `dès la formule de base` ; `le volet Piloter` ; `l'option création` ; `offre 7`, `offre 5`, `offre 8` |
| Promesse | 81 ; 112 ; 127 | `Oui, sans risque pour le public` ; `promise à la galerie de Carlone en échange du financement` ; argument fiscal : `peuvent servir l'offre aux entreprises` |
| Visuel IA | 29 | Signalés dans le texte : `générés par IA le 4 novembre : ce sont des intentions, pas des photos` |
| Forme | 3, 104, 129 | Aucune mention « PROJET non envoyé » ; `c'est à toi de fixer les prix` ; trois liens vers des pages internes |
| Fichier de contacts | 25, 87, 114 | Envois et invitations « par le CRM », alors que la feuille de décisions recommande de geler ce fichier jusqu’à l’avis de l’avocat |

### 4.2 `pour-carlone/vernissage-strates-diaporama.pdf` (4 novembre, 12 pages)

| Type | Page | Citation |
| --- | --- | --- |
| Nom interdit | 1, 6, 7, 9, 11, 12 | p. 1 : `Marwin Tech et BOJ.ART, pour M. Carlone` ; p. 6 : `À côté, Medhi peint le même trait à la main` ; p. 7 : `Le dévoilement de STRATES` ; p. 12 : `avec Medhi, BOJ.ART` |
| Montant interne | 10, 11 | `Honoraires Marwin Tech, estimation à 750 € HT la journée` ; `sans supplément s’il tient dans les 20 journées` ; `Au même taux, si le mois est déjà plein` |
| Prix autre que le cadrage | 10 | `4 500 à 7 500 € HT` ; `9 000 à 13 500 € HT` ; `15 000 à 22 500 € HT` |
| Promesse | 12 ; 7 et 11 | `nous vous remettons un devis par format et le calendrier de préparation` ; `La première présentation de l’œuvre, dans votre galerie` |
| Visuel IA | 4 à 9 | Signalés : `Visuel généré par IA : une intention, pas une photo. Lieu imaginaire.` |
| Fichier de contacts | 10, 11 | `Invitations par le CRM` ; `invitations et suivi par le CRM` |
| Forme | 1 | `State Of The Art · Proposition d’événement` ; aucune mention « PROJET non envoyé » |

### 4.3 `pour-carlone/strates-proposition-artistique-v1.1.pdf` (2 novembre, 8 pages)

| Type | Page | Citation |
| --- | --- | --- |
| Prix autre que le cadrage | 4 | `Les 10 000 EUR envisagés pour le cadrage restent une enveloppe de discussion, non engagée.` ; `Le budget initial de 323 875 EUR HT` ; `provisionné à 25 000 EUR HT` |
| Nom interdit | 1 à 8 | En-tête de chaque page : `BOJ.ART / MARWIN TECH` et `PROPOSITION POUR CARLONE` ; titre : `STRATES — mémoire d’un fleuve` ; auteur dans les propriétés du fichier |
| Visuel IA | 1, 3, 4, 8 ; 2 | Signalés p. 1 (`Visualisation générée par IA`), p. 3, p. 4 et p. 8 ; p. 2 : `Mise en situation fictive`, sans le mot IA |
| Promesse | Aucune | Le texte est prudent : `Aucun prix de vente, engagement de Carlone ou intérêt de collectionneur n’est acquis` (p. 2) |
| Forme | 1 à 8 | Aucune mention « PROJET non envoyé » |

### 4.4 Images et films (15 fichiers)

| Fichier (depuis `pour-carlone/`) | Ce que montre l’image | Mention IA dans l’image | Nom ou enseigne visible |
| --- | --- | --- | --- |
| `visuels/1-source.png` | Salle de pierre, projection du fleuve, invités | Non | Aucun |
| `visuels/2-couche-par-couche.png` | Imprimantes 3D, fragments, invités | Non | Aucun |
| `visuels/3-main-et-machine.png` | Bras robotisé derrière une vitre, artiste au chevalet, public | Non | Aucun |
| `visuels/4-devoilement.png` | Dévoilement d’un relief devant des invités | Non | Aucun |
| `visuels/5-diner-des-strates.png` | Dîner sous des voûtes | Non | Aucun |
| `visuels/6-fossiles-de-la-loire.png` | Vitrine d’objets | Non | Aucun |
| `strates/relief-mineral-bleu-galerie.png` | Relief accroché dans une galerie, une visiteuse | Non | Aucun |
| `strates/bras-robotique-concept-ia-10s.mp4` | Bras qui peint un trait bleu | Oui : bandeau `STRATES - CONCEPT GÉNÉRÉ PAR IA` et commentaire du fichier | Nom de l’œuvre dans le bandeau et le titre |
| `visuels-recuperes-pdf/riviere-ultramarine-extrait-pdf.png` | Relief seul | Non | Aucun |
| `visuels-recuperes-pdf/bras-peignant-relief-fluvial-extrait-pdf.png` | Bras qui peint le relief | Non | Aucun |
| `visuels-recuperes-pdf/bras-educatif-cube-rouge-extrait-pdf.png` | Bras et cubes sur un banc d’essai | Non | Plaque `BOJ.ART × MARWIN TECH` |
| `eclosion/visuel-fleur-cinetique.png` | Fleur à pétales sur un socle | Non | Plaque `ÉCLOSION`, puis `MARWIN TECH × BOJ.ART` |
| `eclosion/animation-concept-1080p-2026-10-31.mp4` | La même fleur qui s’ouvre | Non (images à 0,2 s, 4 s et 7,6 s) | Même plaque |
| `laboratoire-ia-robotique/visuels/atelier-pilote.png` | Atelier avec postes de travail et bras robotisé | Non | Enseigne murale `MARWIN TECH LAB` |
| `laboratoire-ia-robotique/visuels/laboratoire-ia-art-robotique.png` | Grand atelier-galerie | Non | Enseignes `MARWIN TECH` et `BOJ.ART` |

Lecture : « Non » veut dire qu’aucune mention n’a été vue aux examens décrits au § 1. Les six visuels du vernissage sont signalés dans les documents qui les emploient (P1, P2), pas dans les fichiers. D’après `sources/reprise-59-et-visuels-2026-11-04.md:60`, ce sont « des illustrations IA, pas des photographies de réalisations ».

### 4.5 `pour-carlone/eclosion/concept-2026-10-31.pdf` (31 octobre, 5 pages)

| Type | Page | Citation |
| --- | --- | --- |
| Forme | 1 | `Concept de travail v0.1 - 31 octobre 2026 - préparé pour Morgan Olsen` : pièce interne |
| Montant interne | 5 | `six journées-personnes au repère de 750 € HT donnent 4 500 € HT d’honoraires` |
| Nom interdit | 1, 5 | `Le laboratoire, BOJ.ART et Jarvis conservent leurs périmètres.` ; `BOJ.ART et les autres contributeurs conservent leurs droits` |
| Visuel IA | 1 | `Deux états illustratifs : repos et ouverture.` : rien ne dit comment les images ont été faites |

### 4.6 `pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md`

| Type | Lignes | Citation |
| --- | --- | --- |
| Prix autre que le cadrage | 10 ; 44 ; 109 à 116 ; 124 à 126 ; 132, 133 ; 139 | `comptez 15 700 à 18 700 € HT` ; `46 300 à 68 500 €`, `79 000 à 97 700 €`, `57 000 à 240 000 €` ; `3 000 €`, `5 300 €`, `10 400 €`, `7 500 €`, `6 400 €`, `1 200 €`, `2 300 €` ; `700 à 1 000 €`, `1 200 €` par mois ; `10 300 à 37 000 €` |
| Recouvrement de deux prix (V8) | 109 et 116 | `Choix des logiciels et comparaison écrite (facultatif)` à 3 000 € ; `Option hôtellerie (choix du logiciel, reprise des totaux)` à 2 300 € |
| Promesse | 99 ; 73 ; 95 | `nous vous remettons l'attestation de notre responsabilité civile professionnelle` ; `un tiers du gain mesuré vous revient` ; `remise en service le jour ouvré suivant au plus tard` |
| Hébergement en hypothèse | 21 ; 116 ; 175 | `Seulement si l'ancien bar-restaurant-hôtel reprend un hébergement` ; `Option hôtellerie` ; `Votre réponse sur la reprise d'un hébergement` |
| Date abandonnée ou hors référentiel | 179 ; 45, 81 à 86, 124 | `si possible avant le 15 décembre 2026`, déjà corrigée par la mention du 10 novembre ; calendrier estimé jusqu’en février 2028 |
| Temps de l’administratrice | 171 | `environ 6 à 10 jours pendant la mise en place, puis trois quarts de jour à un jour et demi par mois` : autre chiffre que celui du cadrage (une à deux journées), pour un autre travail ; risque de confusion |
| Juste et conforme | 137 | `le cadrage général (6 500 € HT)` |

### 4.7 `pour-carlone/logiciels-et-automatisations/2026-11-09-annexe-specification-logiciel-gestion-proprietes.md`

| Type | Lignes | Citation |
| --- | --- | --- |
| Prix | Aucun | La ligne 7 le dit : `Elle ne contient ni prix ni délai de réalisation` ; mais la ligne 600 renvoie à P13, `avec leurs dates et leurs prix` |
| Hébergement en hypothèse | 9 ; 22 ; 413, 415 ; 632 | `Nous ignorons aussi si une activité d'hébergement reprendra` ; `si l'ancien bar-restaurant-hôtel reprend une activité d'hébergement` ; `Module 9 — Hôtellerie (en option)` ; `Combien de chambres ?` |
| Le mot « hôtel » pour son établissement | 91, 257, 430, 456 | `hôtel s'il y a lieu` ; `Tableau de l'hôtel` |
| Présentation périmée | 71 | `notre présentation du 9 novembre` : c’est la version 11 |
| Autre proposition | 651 | Question neutre, sans nom : `Avez-vous reçu d'autres offres pour un logiciel de ce type ?` |

### 4.8 Les autres pièces du 9 novembre, la version 11 et `pour-gianluca/`

| Pièce | Type | Lignes | Citation |
| --- | --- | --- | --- |
| P15, `…/2026-11-09-logiciels-sur-mesure-methode-et-garanties.md` | Promesse | 110 ; 105 ; 133 | `l'attestation de notre assurance de responsabilité civile professionnelle, avec ses garanties et ses montants` ; partenaire de secours vérifié `Chaque année, à nos frais` ; `un tiers du gain mesuré vous revient` |
| P15 | Fichier de contacts | 123 | `CRM déjà construit` : `Fichier de 500 fiches de prospection` |
| P15 | Paiement | 128 | `40 % à la commande` : autre règle que la moitié à la commande du cadrage, pour d’autres étapes |
| P16, `…/2026-11-09-automatisations-fiches-detaillees.md` | Prix autre que le cadrage | 22 ; 98 ; 104 ; 128 à 142 ; 183, 222, 260, 297, 336, 377, 415, 452, 489, 526, 563, 600, 638, 675, 712 | `1 400 à 6 500 € HT par automatisation` ; `1 000 à 1 500 € HT par mois pour suivre un processus` ; `80 à 430 € HT par mois` ; un prix par fiche |
| P16 | Tarifs publics sans source | 83 à 92 | `Prix publics relevés en novembre 2026` : ni éditeur ni page cités |
| P16 | Présentation périmée | 7, 716, 774 | `Il reprend les 47 aides de la présentation` : la version 12 n’a plus ces 47 aides |
| P16 | Hébergement en hypothèse | 116 | `si une activité d'hébergement reprend` |
| P16 | Mot interdit | 292 | Constat n° 22 |
| P17, guide du dossier | Prix annoncé | 13 | `le prix indicatif` |
| P17 | Présentation périmée | 7, 16 | `des automatisations présentées le 9 novembre` : renvoi à la version 11, non envoyée à notre connaissance (`audit/2026-11-04-audit-strategique/README.md:168`) |
| P19, `presentation-ia/README.md` | Lien périmé | 3 | Constat n° 3 |
| P19 | Nom interdit | 15 | `des visions générées par IA du dossier Strates` |
| P18, version 11 | Promesse | `project/slides/trajectoire.html:12` ; `project/slides/societe.html:14` | `Société créée et assurée.` ; `une assurance et une responsabilité claires` |
| P18 | Fichier de contacts | `project/slides/crm.html:9` ; `project/slides/societe.html:10` | `Un fichier de 500 entreprises de la Nièvre existe` ; `Nous avons déjà construit un outil de prospection` : sujet à ne pas aborder de notre initiative si V3 n’est pas validée |
| P18 | Vocabulaire périmé | `project/slides/etapes.html:17` ; `project/slides/trajectoire.html:4` ; `project/slides/cover.html:6`, `:7` | `Un pilote de huit semaines` ; `Dans un an, deux ans, cinq ans` ; `toutes les aides possibles` ; `sans engagement` |
| P18 | Visuel IA | `project/slides/cover.html:2`, `:8` ; `project/slides/robotique.html:16` | Signalés ; la couverture montre un bras robotisé, ce que l’audit du 9 novembre relevait déjà (`01-audit-de-la-presentation.md:119`) |
| G1, 4 novembre | Nom de tiers | 25 | `un centre d'appels (Quali Contact)` |
| G1 | Date abandonnée | 106 | `au plus tard le vendredi 11 décembre 2026` |
| G1 | Vocabulaire périmé | 46 ; 66, 68 ; 108 | `l'embauche d'un coordinateur salarié` ; `Une seule voie à la fois` ; `extrait K-bis` |
| G2, 9 novembre | Promesse | 104 | `nos conditions (responsabilité, assurance, confidentialité, données), relues par notre avocat` |
| G2 | Nom de tiers | 27 | `un centre d'appels (Quali Contact)` |
| G2 | Date abandonnée | 172 | `au plus tard le vendredi 11 décembre 2026` |
| G2 | Règles revues le 10 novembre | 98, 100 | Signature au nom de la `SAS en formation` ; rétractation sous condition `hors de nos locaux` (inexacte : feuille de décisions, partie 3, décision n° 11) |
| G2 | Montants internes et noms interdits, dans la note interne | 224, 265, 282, 303, 305, 319 | Prix plancher à la journée (l. 265) ; exception à 6 000 € HT (l. 282) ; version réduite à 4 800 € HT (l. 319) ; noms de l’ancien partenaire (l. 224, 303) |
| G3, message de recadrage | Date abandonnée | 34 ; 55 | `le dernier au plus tard le vendredi 11 décembre 2026` ; `sans rendez-vous avant le 15 déc., report à janvier` |
| G3 | Contenu périmé | 28, 38 | `y compris l'embauche d'un coordinateur` ; question 3 sur `la personne qui travaillerait avec nous au quotidien` |

### 4.9 Contrôle mécanique en mode client (`lint-doc.js`, lecture seule)

| Fichier | Erreurs | Alertes | Ce que le contrôle relève |
| --- | --- | --- | --- |
| `pour-carlone/vernissage-strates-idees.md` | 33 | 6 | 12 lignes au nom du partenaire retiré ; 16 au nom d’un dossier de création ; 5 erreurs de prix ; tutoiement (l. 104) |
| `…/2026-11-09-logiciel-gestion-proprietes-proposition.md` | 1 | 26 | Mot « maquette » sans la mention exacte ; 19 alertes de prix « à valider » |
| `…/2026-11-09-logiciels-sur-mesure-methode-et-garanties.md` | 2 | 8 | Idem ; un faux positif (l. 64, `un correctif urgent`) |
| `…/2026-11-09-annexe-specification-logiciel-gestion-proprietes.md` | 2 | 35 | Idem ; un faux positif (l. 427, `totaux journaliers`) |
| `…/2026-11-09-automatisations-fiches-detaillees.md` | 50 | 40 | 49 prix absents des documents clients ; le mot « fuite » (l. 292) |
| `pour-carlone/logiciels-et-automatisations/README.md` | 0 | 6 | Rien de bloquant |
| `pour-carlone/presentation-ia/README.md` | 1 | 2 | Nom d’un dossier de création (l. 15) |
| `pour-gianluca/proposition-de-cadrage.md` | 6 | 5 | Tiers nommé (l. 25) ; mots internes |
| `pour-gianluca/message-de-recadrage.md` | 0 | 5 | Rien de bloquant |
| `pour-gianluca/2026-11-09-proposition-de-cadrage.md` | 136 | 30 | Texte client (l. 15 à 182) : 1 erreur, le tiers nommé (l. 27) ; en-tête : 2 ; note interne : 133 |

Total des pièces anciennes de `pour-carlone/` : 89 erreurs. Le contrôle ne lit ni les PDF ni les images.

## 5. Mentions datées à ajouter

**Règles suivies.** Aucune n’a été ajoutée par cet audit. Chaque mention se colle à la fin d’une ligne existante, sur la même ligne, précédée d’une espace (M10 : à la fin d’une cellule). Aucune ligne n’est créée, donc aucun numéro de ligne cité ailleurs ne bouge : la feuille de décisions cite les lignes 15 à 182 et 186 de G2 ; le sommaire du 10 novembre cite les lignes 99 et 110 ; le mode d’emploi de la version 12 cite la ligne 53 de P13. Les mentions placées dans une pièce à voix de client n’emploient aucun code interne, aucun nom retiré, aucun montant autre que le cadrage. Elles disent « sauf décision écrite » : le sort de ces pièces reste aux associés. Contrôle : les six mentions destinées à une pièce à voix de client (M3 à M7 et M9) passent `lint-doc.js` en mode client sans erreur ni alerte.

**M1. `README.md` (racine), fin de la ligne 3**, après `État au 4 novembre 2026.` :

```
[Mention du 11 novembre 2026 : ce sommaire décrit l’état au 4 novembre 2026, complété le 9 ; il ne fait plus foi. Le partenaire cité ci-dessus n’est plus dans l’offre. Point d’entrée à jour : audit/2026-11-10-preparation-des-livrables/README.md. Ce qui peut être montré à GianLuca Carlone le vendredi 13 novembre 2026 est listé dans pour-carlone/README.md. Seule offre en vigueur : le cadrage (pour-carlone/offre-cadrage/2026-11-10-offre-en-une-page.md) ; l’offre du 2 novembre 2026 est abandonnée. Aucune commande de ce fichier n’est à lancer, et rien n’est à modifier dans crm/, sans décision écrite des deux associés.]
```

**M2. `README.md` (racine), fin de la ligne 11**, après `Les documents faits pour lui être montrés.` :

```
[Mention du 11 novembre 2026 : plus vrai. Les cinq lignes de ce tableau sont des pièces historiques ou hors du rendez-vous du 13 novembre 2026 : ne pas les montrer. Liste à jour : pour-carlone/README.md.]
```

**M3. `pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md`, fin de la ligne 3**, après `à valider par Morgan Olsen et Mathys Couet` :

```
· [Mention du 11 novembre 2026 : pièce historique du 9 novembre 2026 ; elle n’est ni montrée ni remise au rendez-vous du 13 novembre 2026, sauf décision écrite de Morgan Olsen et Mathys Couet. Seul le cadrage a un prix à ce jour (6 500 € hors taxes) : les autres montants de cette pièce ne sont ni proposés ni confirmés ; un prix par étape sera établi après le cadrage, sur vos volumes réels. Aucune attestation d’assurance n’est promise à ce jour. L’hébergement n’est plus une hypothèse : pour vos neuf suites et l’espace bien-être, la pièce à jour est 2026-11-10-vos-suites-un-logiciel-du-marche-bien-choisi.md ; pour le logiciel, la fiche 7 du 10 novembre 2026.]
```

**M4. `pour-carlone/logiciels-et-automatisations/2026-11-09-annexe-specification-logiciel-gestion-proprietes.md`, fin de la ligne 3** :

```
· [Mention du 11 novembre 2026 : pièce historique du 9 novembre 2026 ; elle n’est ni montrée ni remise au rendez-vous du 13 novembre 2026, sauf décision écrite de Morgan Olsen et Mathys Couet. L’hébergement n’est plus une option à confirmer : il s’agit de neuf suites et d’un espace bien-être dans l’établissement de la galerie, pour lesquels nous conseillons un logiciel du marché (pièce du 10 novembre 2026 : 2026-11-10-vos-suites-un-logiciel-du-marche-bien-choisi.md). La proposition chiffrée à laquelle cette annexe renvoie n’est pas en vigueur : seul le cadrage a un prix à ce jour. Pièces à jour : la fiche 7 du 10 novembre 2026 et les écrans d’exemple (Maquette — données fictives).]
```

**M5. `pour-carlone/logiciels-et-automatisations/2026-11-09-logiciels-sur-mesure-methode-et-garanties.md`, fin de la ligne 3** :

```
· [Mention du 11 novembre 2026 : pièce historique du 9 novembre 2026 ; elle n’est ni montrée ni remise au rendez-vous du 13 novembre 2026, sauf décision écrite de Morgan Olsen et Mathys Couet. La phrase de la section 7 sur l’attestation d’assurance n’est pas un engagement à ce jour. Les règles de paiement et de suivi de la section 9 valent pour des étapes qui ne sont pas proposées aujourd’hui : seul le cadrage a un prix (6 500 € hors taxes, moitié à la commande, moitié à la remise du dossier). Pièces à jour : les fiches 7, 8 et 10 du 10 novembre 2026.]
```

**M6. `pour-carlone/logiciels-et-automatisations/2026-11-09-automatisations-fiches-detaillees.md`, fin de la ligne 3** :

```
· [Mention du 11 novembre 2026 : pièce historique du 9 novembre 2026 ; elle n’est ni montrée ni remise au rendez-vous du 13 novembre 2026, sauf décision écrite de Morgan Olsen et Mathys Couet. Les fourchettes de prix de cette pièce (sections 1.5 et 2.0, et chaque « Coût indicatif ») ne sont ni proposées ni confirmées : seul le cadrage a un prix à ce jour ; chaque essai se commande à part, avec son prix, après le cadrage. « La présentation du 9 novembre » et ses 47 aides ne sont plus la présentation en vigueur. Pièces à jour : les douze fiches du 10 novembre 2026 et la page 2026-11-10-une-idee-pour-chacun-de-vos-projets.md.]
```

**M7. `pour-carlone/logiciels-et-automatisations/README.md`, fin de la ligne 3** :

```
· [Mention du 11 novembre 2026 : ce guide du 9 novembre 2026 n’est plus à jour. Les quatre documents du 9 novembre qu’il présente sont des pièces historiques, ni montrées ni remises au rendez-vous du 13 novembre 2026, sauf décision écrite de Morgan Olsen et Mathys Couet ; dans ce dossier, seule la pièce du 10 novembre 2026 sur vos suites est en vigueur. Ce qui vaut pour le rendez-vous est listé dans pour-carlone/README.md.]
```

**M8. `pour-carlone/presentation-ia/README.md`, fin de la ligne 3**, après l’adresse qui finit par `HMK1t6YnXQVNvQCw8YZEzx` :

```
[Mention du 11 novembre 2026 : cette adresse ouvre la version 11, pièce historique du 9 novembre 2026 : ne pas l’ouvrir au rendez-vous du 13 novembre 2026. La présentation en vigueur est la version 12 (projet privé, 36 diapositives : 28 dans le fil, 8 en annexe) : https://claude.ai/artifact/NGWE17VQB7zDfTtvKHDFSg ; ses sources sont dans 2026-11-10-version-12-projet/ et project/deck.json fait foi pour l’ordre.]
```

**M9. `pour-carlone/vernissage-strates-idees.md`, fin de la ligne 3**, après `Nov 4, 2026 · @Olsen Morgan` :

```
· [Mention du 11 novembre 2026 : pièce historique, hors du rendez-vous du 13 novembre 2026 ; ni montrée ni remise à GianLuca Carlone. Document de travail du 4 novembre 2026 : il cite un partenaire qui n’est plus dans l’offre, un taux à la journée et une formule mensuelle abandonnés. Seule offre en vigueur : le cadrage (pour-carlone/offre-cadrage/2026-11-10-offre-en-une-page.md). Index du dossier : pour-carlone/README.md.]
```

**M10. Les deux PDF et les médias (P1, P3 à P12).** Un PDF ou une image ne reçoit pas de mention sans être refait, ce que la règle interdit. Leur statut est inscrit dans l’index `pour-carlone/README.md` (partie 3), qui s’affiche sous la liste des fichiers du dossier, et dans M1 et M2. Option, si les associés veulent une marque dans le tableau de la racine : dans la dernière cellule des lignes 15 à 18 du `README.md`, ajouter après la date :

```
[Mention du 11 novembre 2026 : hors du rendez-vous, à ne pas montrer.]
```

**M11. `audit/2026-11-04-audit-strategique/pour-gianluca/proposition-de-cadrage.md`, fin de la ligne 5** (ligne « Statut », déjà à retirer avant tout envoi) :

```
[Mention du 11 novembre 2026 : pièce historique, à ne plus utiliser. Ce projet du 4 novembre 2026 a été repris le 9 novembre (2026-11-09-proposition-de-cadrage.md), puis le 10 novembre dans le texte client en vigueur : pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md. Sa date limite de rendez-vous (vendredi 11 décembre 2026, section 7) est abandonnée : le rendez-vous a lieu le vendredi 13 novembre 2026. Il nomme un tiers (section 1).]
```

**M12. `audit/2026-11-04-audit-strategique/pour-gianluca/2026-11-09-proposition-de-cadrage.md`, fin de la ligne 5** (ligne « Statut ») :

```
[Mention du 11 novembre 2026 : pièce historique, à ne plus utiliser pour un envoi. Le texte client (de « Projet du 9 novembre 2026 — non envoyé » à la signature) a été repris seul et corrigé le 10 novembre : pour-carlone/offre-cadrage/2026-11-10-proposition-de-cadrage-version-client.md (tiers retiré ; « relues par notre avocat » retiré, car ce n’est pas fait ; date du 11 décembre abandonnée ; neuf suites ajoutées ; rétractation et signature revues). La note interne qui suit la signature reste ici : ne rien montrer ni envoyer à partir de ce fichier.]
```

**M13. `audit/2026-11-04-audit-strategique/pour-gianluca/message-de-recadrage.md`, fin de la ligne 5** (ligne « Statut ») :

```
[Mention du 11 novembre 2026 : pièce historique, à ne pas envoyer en l’état. Ce projet du 4 novembre 2026 propose un premier rendez-vous « au plus tard le vendredi 11 décembre 2026 » : date abandonnée, le rendez-vous a lieu le vendredi 13 novembre 2026. Il est écrit avant les faits rapportés le 9 et le 10 novembre (administratrice, neuf suites) : la question 3 et « l’embauche d’un coordinateur » ne tiennent plus. Une nouvelle version datée est à écrire après le rendez-vous ; référence : pour-carlone/offre-cadrage/2026-11-10-offre-en-une-page.md.]
```

**Une précision pour la liste de contrôle du jour du rendez-vous.** `interne/rendez-vous/2026-11-11-jour-j-liste-de-controle.md` dit déjà « rien d’ouvert hors la présentation et la maquette ». Cette liste doit tenir sur une page : une seule phrase, à ajouter à la fin de cette ligne-là :

```
La présentation est la version 12 (adresse finissant par NGWE17VQB7zDfTtvKHDFSg), jamais la version 11 (adresse finissant par HMK1t6YnXQVNvQCw8YZEzx) ; le dossier pour-carlone/ ne s’affiche pas à l’écran.
```

## 6. Ce que le sommaire de la racine dit de faux aujourd’hui

`README.md` (racine), daté « État au 4 novembre 2026 », complété le 9 novembre par les lignes 19 et 33. Vingt points.

| Ligne | Ce que dit le sommaire | Pourquoi c’est faux ou périmé le 11 novembre |
| --- | --- | --- |
| 3 | `avec Medhi (BOJ.ART). État au 4 novembre 2026.` | L’ancien partenaire créatif est retiré de l’offre : décidé à l’oral par Morgan Olsen, écrit à faire (feuille de décisions, partie 0, et partie 4, ligne « Retrait de l’ancien partenaire par écrit »). L’état décrit a sept jours |
| 3 | `M. Carlone` | Le nom s’écrit « GianLuca Carlone » (feuille de décisions, partie 0) |
| 5 | « Le point de départ est » `interne/contexte-projet-carlone.md` | Le point d’entrée est `audit/2026-11-10-preparation-des-livrables/README.md` (`REPRISE-2026-11-10.md:7`). Le contexte du 4 novembre décrit encore l’offre mensuelle comme prête |
| 11 | `Les documents faits pour lui être montrés.` | Aucune des cinq lignes du tableau n’est à montrer le 13 novembre (§ 2.2) |
| 13 à 19 | Le tableau « Pour Carlone » entier | Il ne cite aucun dossier en vigueur : `offre-cadrage/`, `fiches/`, `developpement/`, `cadrage/`, `cabaret-et-commerces/`, `maquettes/`, `presentation-ia/`. Il ne cite pas non plus `eclosion/`, `strates/`, `laboratoire-ia-robotique/`, `visuels-recuperes-pdf/` |
| 15 | Diaporama du vernissage, 12 diapositives | Hors du rendez-vous ; noms retirés, taux à la journée, ancienne formule (§ 4.2) |
| 16 | `vernissage-strates-idees.md` | Document de travail adressé à Morgan Olsen, pas un document client (§ 4.1) |
| 17 | `Six visuels du vernissage, générés par IA` | Exact, mais les images ne portent aucune mention ; la première sert de couverture à la version 12 |
| 18 | Proposition artistique, 8 pages | Projet gelé, option retirée ; autre montant sous le mot « cadrage » (§ 4.3) |
| 19 | `projets non envoyés`, datés du 9 novembre | Le dossier contient aussi la pièce du 10 novembre, seule en vigueur ; les quatre pièces du 9 novembre sont remplacées ou historiques |
| 25 à 33 | Le tableau « Interne » | Il ne cite aucun dossier du 10 novembre : `decisions/`, `prealables/`, `rendez-vous/`, `offre-cadrage/`, `developpement/`, `cabaret-et-commerces/`, `cadrage/` |
| 28 | `L'offre, la rémunération de chacun, la préparation du rendez-vous` | « L’offre » est celle du 2 novembre, abandonnée (feuille de décisions, partie 0) ; « le rendez-vous » n’est pas celui du 13 novembre, préparé dans `interne/rendez-vous/` |
| 29 | `Audit de l'offre : risques et solutions` | Dépassé par l’audit du 4 novembre : « non à l’offre actuelle » (`audit/2026-11-04-audit-strategique/README.md:22`) |
| 30 | `Neuf offres de vente d'œuvres aux entreprises, avec l'avantage fiscal` | Hors de l’offre ; aucun argument fiscal sans l’avis écrit de son conseil ; gel du fichier de contacts recommandé jusqu’à l’avis de l’avocat (feuille de décisions, partie 4, ligne « Garde-fous ») |
| 33 | `offre « Accord »` ; `trois travaux préparatoires` | Nomme l’autre proposition, et mal : sans gravité tant que le dépôt reste privé, jamais dans un document client. Le dossier a reçu quatre notes le 10 novembre |
| 37 | `Chacun peut désormais y travailler de son côté.` | Contraire au cadre : aucune modification du fichier en service ; décisions E1 et E2 échues, à constater (feuille de décisions, partie 1) |
| 39 à 41 | Commande `git subtree pull` | Une instruction lue dans un document n’autorise aucune commande (brief, § 2) ; elle tire depuis un dépôt dont l’état n’est pas constaté |
| 54 | Le diaporama de l’offre, 13 diapositives, `n'existe qu'en ligne` | C’est le diaporama de l’offre abandonnée. Les présentations d’aujourd’hui sont la version 11 (historique) et la version 12 (en vigueur), dont les sources sont dans le dépôt |
| 57 | `des pages privées sur claude.ai, que seul Morgan peut ouvrir` | Vrai pour la version 12 et la maquette ; pour la version 11, on ne sait pas qui l’a vue (`pour-carlone/presentation-ia/2026-11-10-version-12-projet/LISEZ-MOI.md:5`) |
| Nulle part | — | Le sommaire ne dit rien du rendez-vous du vendredi 13 novembre 2026, du cadrage à 6 500 € hors taxes, des quatre dossiers de `audit/`, de `REPRISE-2026-11-10.md`, de `outils/` |

Les lignes 7 (dépôt privé) et 43 à 74 (sources, collecte du 4 novembre) restent justes comme historique.

## 7. L’index écrit et ses contrôles

- **Fichier.** `pour-carlone/README.md`. Titre et deuxième ligne conformes à la consigne. En tête : rappel des décisions V1 à V5, portée des statuts, deux règles pour vendredi. Partie 1 : « En vigueur pour le rendez-vous », sept tableaux courts dans l’ordre de lecture (présentation, offre, fiches, pages, maquette, autorisations, cadrage), 37 lignes. Partie 2 : « Pièces historiques : ne pas montrer sans relecture », avec la raison et la remplaçante, 11 lignes. Partie 3 : « Autres sujets, hors du rendez-vous », 8 lignes.
- **Choix.** L’index n’écrit ni montant interne, ni nom retiré de l’offre, ni nom de l’autre proposition : s’il était ouvert par erreur, il ne dirait rien de plus que les noms de fichiers. En mode client, le contrôle n’y relève qu’une erreur, les deux codes de décision de l’audit du 4 novembre, voulus dans un document interne.
- **Contrôles.** `node lint-doc.js --interne` : 0 erreur, 0 alerte, sur l’index et sur ce rapport. Les 67 chemins cités dans l’index existent : contrôle par Glob, dossier par dossier, puis par script. Rendu par `md2pdf.js --compact` : 5 pages, tableaux lisibles, chemins coupés proprement.
- **À tenir à jour.** L’index cite les trois pièces du 11 novembre de `offre-cadrage/`. Toute nouvelle pièce de `pour-carlone/` doit y entrer le jour où elle est écrite. Le manifeste du dossier relié le cite déjà sous le titre « Index du dossier pour-carlone : ce qui vaut pour le 13 novembre ».

## 8. Ce qui reste aux associés

1. **Confirmer les statuts de l’index** et faire ajouter les mentions du § 5 (D06, D07 ; échéance : vendredi 13 novembre 2026 ; feuille de décisions, partie 4, ligne « Une seule offre »).
2. **La couverture de la version 12** : garder le visuel sans le nom du dossier, prendre une photo fournie par GianLuca Carlone, ou n’avoir aucune image (constat n° 2 ; feuille de décisions, partie 4, ligne « Structure de la version 12 »).
3. **Le sort des documents du 9 novembre après le rendez-vous** : ils portent les seuls prix du logiciel écrits pour le client (V1, arbitrage C ; V8).
4. **Le message de recadrage** : une nouvelle version datée, ou son abandon (constat n° 18).
5. **L’écrit sur le retrait de l’ancien partenaire** et la déclaration du lien de Morgan Olsen avec son studio (feuille de décisions, partie 4, ligne « Retrait de l’ancien partenaire par écrit ») : tant qu’ils manquent, les pièces P1 à P12 restent sans réponse écrite si GianLuca Carlone en parle. Réponses orales préparées : `interne/rendez-vous/2026-11-11-sujets-hors-presentation-que-repondre.md` (sujets 3, 5 et 6).
6. **Ranger ailleurs les pièces anciennes** : non proposé avant vendredi (la règle du 10 novembre interdit de renommer une pièce, et des index de `sources/` pointent vers elles). Si les associés veulent un dossier client sans pièces anciennes, c’est une décision à part, après le rendez-vous.
