# Présentation version 12 — sources du projet (non publiée)

PROJET non envoyé — à valider par Morgan Olsen et Mathys Couet

Document de travail. Sources de la version 12 au format de la présentation publiée (`project/deck.json` et `project/slides/<id>.html`). **Elle n’est pas publiée** : la version 11 est en ligne à une adresse dont on ne sait pas qui l’a vue (décision D45) ; publier la version 12 à la même adresse reviendrait à montrer au client un document que les deux associés n’ont pas validé. Publication seulement après la liste avant tout envoi (`interne/prealables/2026-11-10-liste-avant-tout-envoi.md`).

## Ordre (vingt minutes, texte d’orateur : `interne/rendez-vous/2026-11-10-deroule-et-texte-d-orateur.md`)

Fil principal (19) : 1 cover, 2 compris, 3 **demande**, 4 **nouveautes**, 5 **ecran-ensemble**, 6 **ecran-batiment**, 7 **ecran-devis**, 8 **hotel**, 9 administratrice, 10 modes, 11 cat-batiments, 12 etapes, 13 societe, 14 **grille**, 15 **proposition**, 16 **garanties**, 17 **decision**, 18 **moyens**, 19 **cloture**. Annexe : 20 cat-galerie, 21 cat-cabaret, 22 cat-admin, 23 cat-finance, 24 robotique. En gras : diapositives nouvelles, écrites le 10 novembre ; les autres sont reprises de la version 11 et corrigées. Les pieds de page suivent ces rangs.

La diapositive `hotel` (ajoutée le 10 novembre au soir, après `ecran-devis`) répond au sens de « gestion de propriété » : un logiciel de gestion hôtelière. Titre : « Un logiciel du marché, bien choisi et relié au reste » ; surtitre « Vos neuf suites et l’espace bien-être » (vocabulaire du § 11 du brief complémentaire : jamais « votre hôtel »). Nous ne construisons pas de logiciel hôtelier ; nous aidons à le choisir, le paramétrer, le relier au reste, former votre administratrice ; aucun prix ; aucune mention de l’autre proposition. L’identifiant reste `hotel`. Le bandeau « Il doit gérer : réservations, taxe de séjour, fiches de police, caisse certifiée, créneaux du sauna et du jacuzzi » reprend le document client du 9 novembre (`pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md`, ligne 53) et le § 11.3 ; les obligations elles-mêmes sont « à faire valider par vos professionnels » (notes de l’orateur).

## État du contrôle (10 novembre 2026, `lint.js` et `render.js` de l’orchestration)

Dernière ligne de `lint.js` sur les 24 diapositives : **« Total : 0 erreur(s), 8 alerte(s) sur 24 diapositive(s). »** Rendu des 24 diapositives : **aucun débordement**.

- **Reprises de la version 11, corrigées selon l’audit** (`audit/2026-11-09-audit-presentation-et-offre/travaux/a1-point-de-vue-gianluca.md`, `a3-exactitude-et-engagements.md`) : `cover`, `compris`, `administratrice`, `modes`, `cat-batiments`, `etapes`, `societe`. Aucune alerte ; 80 mots visibles au plus ; titres de 55 caractères au plus ; texte courant à 28 px au moins ; couleurs de la palette seulement ; marge du bas entre 61 et 192 px (couverture : 240 px, attendu pour ce gabarit).
  - `cover` : plus de « sans engagement », de « toutes les aides possibles » ni de « ce que deviendra notre société » ; « seul un bon de commande signé engage, vous comme nous » ; image du dossier Strates (salle de pierre, pas de robot) avec la légende « Visuel : vision générée par IA — dossier Strates ». La décision sur l’image (01 n° 16 : photo fournie par lui, sinon aucune image) reste ouverte dans la feuille de décisions.
  - `compris` : titre « Ce que nous avons compris, à corriger avec vous » ; faits présentés comme des projets (« Une galerie d’art », « Un projet de cabaret-spectacle ») ; ajout des neuf suites et de l’espace bien-être ; votre administratrice « gère l’administratif ».
  - `administratrice` : « Nous ne remplaçons pas votre administratrice. On mesure une tâche, jamais une personne. » ; « Valide dans les pouvoirs que vous lui donnez » ; « Rappelle les échéances saisies » ; « Retrouve un document rangé » ; plus de « tous les projets », « n’importe quel document », « chaque semaine avec vous » ; son temps pendant le cadrage dans les notes (repris de `pour-carlone/offre-cadrage/2026-11-10-une-page-pour-votre-administratrice.md`).
  - `modes` : titre de 45 caractères ; « L’IA rédige, trie ou résume » (plus « calcule ») ; ligne « Jamais automatique : un envoi, une publication, une commande, un paiement, une signature, une suppression ».
  - `cat-batiments` : trois aides seulement ; « Énergie et capteurs » retiré ; contrôles « d’après la liste validée par votre bureau de contrôle » ; « Nous ne déclarons jamais un lieu conforme ».
  - `etapes` : « À chaque étape, vous jugez sur un résultat » ; « Choisir, Essayer, Suivre, Étendre » ; « Robotique : plus tard, sous conditions » ; point de départ du délai dans les notes.
  - `societe` : plus d’outil de prospection, plus d’assurance, plus de « garantie » ni d’« interlocuteur unique » ; « immatriculée avant toute facture et tout démarrage » et « Nous sommes deux : une étape et un essai à la fois » ; passée sur fond clair (couleurs hors palette retirées).
- **Nouvelles diapositives resserrées** : `nouveautes` et `garanties` ramenées sous 80 mots (une phrase redondante retirée de l’écran, gardée dans les notes) et agrandies.
- **Alertes restantes, lues** :
  - `ecran-devis` (84 mots) : maquette d’écran, plafond de 120 mots.
  - `proposition` (« tutoiement possible ») : faux positif sur « prêtes ».
  - `moyens` (90 mots) : texte du dixième livrable, à resserrer seulement si les deux associés décident de la montrer.
  - `cat-galerie`, `cat-cabaret`, `cat-admin`, `cat-finance` (104 à 114 mots) : tableaux d’annexe, plafond de 120 mots ; leur correction est suivie à part.
- La diapositive `moyens` ne se montre que si les deux associés le décident (feuille de décisions, partie 4).
- La diapositive `proposition` porte le prix « 6 500 € hors taxes, soit 7 800 € toutes taxes comprises » : à garder seulement si Marwin Tech opte pour la TVA (sinon « 6 500 €, TVA non applicable »).

## Publier, le moment venu

Avec l’outil Artifact : `url` de la présentation, `root` = ce dossier, `file_path` = `project/deck.json`, `files` = chaque diapositive modifiée ; les diapositives retirées de la version 11 (`avancees`, `ia-aujourdhui`, `domaines`, `cat-marketing`, `crm`, `logiciels`, `apports`, `regles`, `methode`, `pour-dautres`, `trajectoire`, `premier-pas`, `echange`, `idee`) passent à `null`.
