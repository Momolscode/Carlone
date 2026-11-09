# A5 — Forme et lisibilité de la présentation v11

9 novembre 2026 · note de travail interne (ne pas transmettre à GianLuca Carlone)

## Conclusion

La version 11 est propre et régulière, mais elle se lit comme un dossier, pas comme une présentation. Trois défauts de forme freinent la décision :

1. **Trop de texte, trop petit.** 26 diapositives, 2 888 mots visibles, soit 111 mots par diapositive en moyenne. Le corps de texte est presque partout à 24 px sur une page de 1 080 px de haut : c'est la taille d'une note de bas de page une fois projeté.
2. **Rien à regarder.** Deux images seulement (couverture et robotique), aucune maquette d'écran, aucun exemple concret montré. Six diapositives de suite sont des tableaux de catalogue.
3. **Pas de moment de décision.** Aucun prix, aucune diapositive « ce que nous vous proposons de décider ». La présentation finit sur quatre questions ouvertes.

## Méthode

Chaque diapositive de la v11 a été rendue dans un navigateur (Chromium, page de 1 920 × 1 080, polices du jeu : Cormorant Garamond et DM Sans). Pour chacune : hauteur naturelle du contenu, marge restante avant le bas de la page, nombre de mots visibles (notes de l'orateur exclues), plus petite taille de texte, longueur du titre. Le rendu est une approximation de l'outil de présentation : un écart de quelques pixels est possible.

## Mesures

| N° | Diapositive | Mots visibles | Marge basse (px) | Titre (caractères) | Remarque |
|---|---|---|---|---|---|
| 1 | cover | 57 | 315 | 39 | Image hors sujet (bras robotisé, imprimante 3D) pour un propos sur ses lieux et son administration |
| 2 | compris | 90 | 86 | — | |
| 3 | idee | 66 | 377 | 99 | Titre de 99 caractères : trois lignes |
| 4 | avancees | 125 | 79 | — | Dense |
| 5 | ia-aujourdhui | 105 | 107 | — | |
| 6 | administratrice | 152 | **déborde de 12** | — | Seule diapositive qui dépasse la page |
| 7 | domaines | 98 | 62 | — | |
| 8 | modes | 112 | 200 | — | |
| 9 | cat-admin | 106 | 82 | — | Tableau de catalogue |
| 10 | cat-batiments | 85 | 210 | — | Tableau de catalogue |
| 11 | cat-galerie | 100 | 166 | — | Tableau de catalogue |
| 12 | cat-cabaret | 108 | 138 | — | Tableau de catalogue |
| 13 | cat-finance | 110 | 96 | — | Tableau de catalogue |
| 14 | cat-marketing | 93 | 166 | — | Tableau de catalogue |
| 15 | crm | 138 | 203 | — | Dense |
| 16 | logiciels | 146 | 203 | — | Dense |
| 17 | robotique | 152 | 17 | 70 | Titre sur deux lignes, page pleine |
| 18 | apports | 108 | 108 | — | |
| 19 | regles | 109 | 168 | — | |
| 20 | methode | 123 | 165 | — | |
| 21 | societe | 126 | 205 | — | |
| 22 | pour-dautres | 114 | 82 | — | |
| 23 | trajectoire | 173 | 117 | — | La plus chargée |
| 24 | etapes | 112 | 68 | — | |
| 25 | premier-pas | 125 | 66 | — | « La proposition chiffrée vous est remise à part » : pas de prix |
| 26 | echange | 55 | 389 | 24 | Quatre questions, pas de demande de décision |

Constats mesurés :

- Plus petite taille de texte : 24 px sur toutes les diapositives (aucune en dessous).
- Le titre commence à la même hauteur (165 px) sur toutes les diapositives de contenu : la grille est régulière.
- Aucun débordement en largeur détecté.
- 17 diapositives sur 26 dépassent 105 mots. 9 laissent plus de 160 px vides en bas alors que leur texte est à 24 ou 26 px : la place existe pour écrire plus gros.

## Ce que l'œil voit

- **Un mur de cartes.** Presque chaque diapositive est une grille de trois à six cartes de texte. Au bout de cinq diapositives, elles se ressemblent toutes. Rien ne signale ce qui compte le plus.
- **Le catalogue au milieu.** Les six tableaux (47 aides) arrivent de la diapositive 9 à la 14. C'est le moment où l'attention tombe, juste avant les sujets qui l'intéressent (logiciels, société, premier pas).
- **Des titres qui décrivent au lieu d'affirmer.** Plusieurs titres nomment un sujet (« Un cadrage de trois à quatre semaines ») sans dire ce qu'il y gagne.
- **Une couverture qui parle de robots.** Le premier écran montre un bras robotisé alors que la robotique est annoncée « plus tard, sous conditions ».
- **Aucune preuve visible.** Le CRM, les dossiers Strates et Éclosion, les fiches d'automatisation existent dans le dépôt : rien n'en est montré.

## Recommandations de forme pour la nouvelle version

1. **18 à 22 diapositives dans le fil principal**, le catalogue des 47 aides en annexe (huit diapositives au plus), consultable à la demande.
2. **80 mots visibles au plus par diapositive** (120 pour une maquette d'écran). Une idée par diapositive. Le détail passe dans les notes de l'orateur ou dans les documents remis.
3. **Corps de texte à 28 px ou plus**, jamais sous 24 px. Les chiffres clés en grand (80 px et plus).
4. **Titre de 55 caractères au plus**, qui affirme un bénéfice ou une décision. Lus à la suite, les titres doivent raconter l'histoire seuls.
5. **Varier les formes** : un énoncé seul sur fond sombre pour les trois ou quatre moments forts ; un « avant / après » pour la journée de l'administratrice ; des maquettes d'écran portant la mention « Maquette — données fictives » ; une frise pour un, deux et cinq ans ; un grand chiffre pour le prix du cadrage.
6. **Une couverture qui parle de lui** : ses lieux, la galerie, la Loire. Par exemple un visuel du dossier Strates déjà remis (`pour-carlone/visuels/1-source.png` ou `4-devoilement.png`), avec la mention « vision générée par IA ». Ne pas utiliser `pour-carlone/visuels-recuperes-pdf/bras-educatif-cube-rouge-extrait-pdf.png` (plaque portant un nom de partenaire retiré de l'offre).
7. **Une diapositive de prix et une diapositive de décision** en fin de fil principal, avant les questions.
8. **Contrôle systématique** : chaque diapositive nouvelle est rendue et mesurée avant publication (débordement, taille minimale, nombre de mots, longueur du titre).

## Limites

- Le rendu local n'affiche pas les deux images hébergées par l'outil de présentation ; elles ont été vues dans la version publiée.
- La lisibilité réelle dépend de l'écran utilisé le jour du rendez-vous (ordinateur portable, téléviseur, projecteur), inconnu à ce jour.
