# Présentation version 12 — sources du projet (non publiée)

PROJET non envoyé — à valider par Morgan Olsen et Mathys Couet

Document de travail. Sources de la version 12 au format de la présentation publiée (`project/deck.json` et `project/slides/<id>.html`). **Elle n’est pas publiée** : la version 11 est en ligne à une adresse dont on ne sait pas qui l’a vue (décision D45) ; publier la version 12 à la même adresse reviendrait à montrer au client un document que les deux associés n’ont pas validé. Publication seulement après la liste avant tout envoi (`interne/prealables/2026-11-10-liste-avant-tout-envoi.md`).

## Ordre (vingt minutes, texte d’orateur : `interne/rendez-vous/2026-11-10-deroule-et-texte-d-orateur.md`)

Fil principal : cover, compris, **demande**, **nouveautes**, **ecran-ensemble**, **ecran-batiment**, **ecran-devis**, administratrice, modes, cat-batiments, etapes, societe, **grille**, **proposition**, **garanties**, **decision**, **moyens**, **cloture**. Annexe : cat-galerie, cat-cabaret, cat-admin, cat-finance, robotique. En gras : diapositives nouvelles, écrites le 10 novembre ; les autres sont reprises de la version 11.

## État du contrôle (`outils/2026-11-10-orchestration/rendu/lint.js`)

- Les onze nouvelles diapositives : aucune erreur, aucun débordement (rendu vérifié) ; alertes de longueur légère (81 à 90 mots visibles sur quatre d’entre elles) à resserrer.
- Les diapositives reprises de la version 11 restent **à corriger selon l’audit** (`audit/2026-11-09-audit-presentation-et-offre/travaux/a1`, `a3`) : trop de mots sur `administratrice`, `societe`, `cat-cabaret`, `cat-admin`, `cat-finance`, `robotique` ; légende « générée par IA » manquante sur l’image de `robotique` ; couleur hors palette sur `cover`, `compris`, `societe`.
- La diapositive `moyens` ne se montre que si les deux associés le décident (feuille de décisions, partie 4).
- La diapositive `proposition` porte le prix « 6 500 € hors taxes, soit 7 800 € toutes taxes comprises » : à garder seulement si Marwin Tech opte pour la TVA (sinon « 6 500 €, TVA non applicable »).

## Publier, le moment venu

Avec l’outil Artifact : `url` de la présentation, `root` = ce dossier, `file_path` = `project/deck.json`, `files` = chaque diapositive modifiée ; les diapositives retirées de la version 11 (`avancees`, `ia-aujourdhui`, `domaines`, `cat-marketing`, `crm`, `logiciels`, `apports`, `regles`, `methode`, `pour-dautres`, `trajectoire`, `premier-pas`, `echange`, `idee`) passent à `null`.
