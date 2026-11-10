# Gabarits de la présentation v12 — règles d'écriture des diapositives

Document de travail. À lire avant d'écrire ou de corriger une diapositive.

## 1. Le format (contrat strict de l'outil de présentation)

Une diapositive = un fichier `project/slides/<id>.html` qui contient **exactement une** balise `<section id="<id>" style="…">…</section>`, sur une page fixe de 1 920 × 1 080 px. Rien d'autre dans le fichier (pas de `<html>`, pas de `<style>`, pas de `<script>`, pas de classe CSS).

Tout le style est en ligne, dans l'attribut `style`, et seulement avec ce sous-ensemble :

- **Unités** : px ou nombre nu. Interdits : em, rem, vw, vh, %, `calc()`, `var()`. (Exceptions : `width:N%` sur les cellules d'un tableau ; les pourcentages d'un dégradé ; `border-radius:50%`.)
- **Couleurs** : hexadécimal (`#14181F`, ou `#14181F1F` avec transparence), `rgb()`, `hsl()`, nom. Interdit : `currentcolor`.
- **Mise en page** : `display:flex`, `flex-direction`, `gap`, `align-items`, `justify-content`, `flex`, `align-self`, `flex-wrap` ; `display:grid` avec `grid-template-columns` / `grid-template-rows` (px, fr, auto, `repeat`) ; `position:absolute` avec `left/top/right/bottom/width/height` en px ; `padding` (0 à 256) ; `width`, `height` ; `overflow`.
- **Texte** : `font-family`, `font-size` (jamais sous 24px), `font-weight` (centaines), `line-height`, `letter-spacing`, `text-align`, `text-transform`, `white-space`, `color`.
- **Décor** : `background` (une couleur ou un seul dégradé), `border` / `border-top`… (le mot `solid`, `dashed` ou `dotted` est obligatoire, épaisseur 16 au plus), `border-radius`, `box-shadow`, `opacity`.
- **Sans effet ou interdits** : `margin` (ignoré : utiliser `gap` et `padding`), `z-index`, `float`, `box-sizing`, `:hover`, animations, listes imbriquées, `colspan` / `rowspan`.
- **Balises permises** : `h1 h2 h3 p ul ol li br div table tr th td img hr aside`, et en ligne seulement `<b> <i> <u> <a> <span style="color:…">`. Balises propres à l'outil : `<x-shape kind="ellipse|diamond|arrow-right|arrow-left|arrow-up|arrow-down|line" style="width;height;background">`, `<x-icon name="…" style="color;width;height">` (32px au moins, 48px à côté d'un texte), `<x-connector>`.
- **Noms d'icônes permis** (aucun autre) : Activity Book Chart Chat Check CheckCircle Clock Cloud Code Database Globe GraduationCap Home Key Lightbulb Lightning Link Lock PaperPlane Play Search Settings Star ThumbsUp Tool Trust Users Verified Warning Wrench. À utiliser avec retenue.
- **Images** : seulement `<img src="/_blob/<identifiant>" alt="…">` avec un identifiant fourni dans votre mission. Ne jamais inventer d'image ni d'identifiant. Pas d'URL. Pas d'emoji.
- **Tableaux (règle stricte)** : `<table style="font-size:28px;color:#14181F">` — la taille, la police et la couleur se règlent **sur la balise `table`**, jamais sur une cellule. Sur `<td>` et `<th>`, **seulement** `width:N%` (répété sur chaque cellule de chaque ligne), et au besoin `text-align` ou `color`. Jamais de `font-size`, `line-height`, `border`, `background` ni `padding` sur une cellule : l'outil trace lui-même les filets et les marges. Un `<tr>` peut porter `background:#FFFDF9`. Le texte d'une cellule est simple (pas de liste, pas de `div`). Copier `g-tableau.html`.
- **Chaque propriété sur la bonne balise** : `font-size`, `line-height`, `font-weight` sur `h1 h2 h3 p ul ol` (et `font-weight` ou `color` sur un `span`) ; `display`, `gap`, `overflow` sur `div` ou `section` ; un `span` ne prend que `color` et `font-weight`.
- **Limites** : 200 éléments au plus par diapositive ; 15 `<div>` imbriqués au plus ; les cellules d'un tableau contiennent du texte simple.
- **Ordre de peinture = ordre du code** : un fond épinglé (`position:absolute`) s'écrit avant le texte qu'il porte.
- **Notes de l'orateur** : une balise `<aside>…</aside>`, dernier enfant de la section, texte simple, 4 000 caractères au plus. Elles sont visibles par toute personne qui ouvre le lien : elles respectent les mêmes règles que le texte affiché.
- **Typographie française** : apostrophe courbe « ’ », guillemets « », espace insécable avant « : ; ? ! » non exigée (espace simple acceptée), « € » après le montant (« 6 500 € HT »).

## 2. La grille commune

- Section claire : `background:#F6F3EE;color:#14181F;font-family:'DM Sans', Arial, sans-serif;padding:120px 128px 160px;display:flex;flex-direction:column;gap:40px` — ne pas changer le `padding` : il fixe le titre à la même hauteur partout.
- En-tête : surtitre 24px en capitales bronze `#7E5F31`, puis titre `h2` 64px Cormorant Garamond 600.
- Pied : **une seule** ligne épinglée, 24px : `Marwin Tech · pour GianLuca Carlone · novembre 2026 · <numéro>`.
- Couleurs : encre `#14181F` ; papier `#F6F3EE` ; carte `#FFFDF9` ; filet `#D9D2C5` ; bronze foncé `#7E5F31` (texte) ; bronze `#B08D57` (filets, flèches, texte sur fond sombre) ; texte courant `#3D4450` ; texte secondaire `#5F636C` ; sur fond sombre : `#F3EFE8` et `#E7E1D6`. Pastilles d'état d'une maquette : vert `#3F6B4F`, rouge brique `#8A3B2E`, bronze `#7E5F31`.
- Pas d'autre couleur, pas d'autre police.

## 3. Les règles de fond de chaque diapositive

1. **Une idée par diapositive.** Le titre l'affirme en 55 caractères au plus (espaces compris). Lus à la suite, les titres racontent l'histoire.
2. **80 mots visibles au plus** (120 pour une maquette d'écran ou un tableau), surtitre, titre et pied compris. Le détail va dans les notes de l'orateur.
3. **Texte courant à 28px ou plus.** 26px toléré dans une maquette ou un tableau. 24px seulement pour le surtitre, le pied, une légende ou une pastille.
4. **La page doit être remplie sans déborder.** Hauteur naturelle visée : entre 880 et 1 020 px (sur 1 080). S'il reste plus de 200 px vides en bas, grossir le texte (30, 32, 34px) ou aérer (`gap`, `padding`), ne pas ajouter de mots. Si cela déborde, enlever des mots, ne pas réduire la taille.
5. **Aucun mot de remplissage.** Pas de formule creuse. Phrases courtes, mots simples, vouvoiement.

## 4. Les gabarits (exemples testés)

Dossier : `gabarits/project/slides/` (à côté de ce fichier). Chaque fichier est un exemple complet, rendu et mesuré. Copier la structure, remplacer le texte, garder les styles.

| Gabarit | Fichier | Usage |
|---|---|---|
| `couverture` | `g-couverture.html` | Première diapositive seulement : image plein cadre, voile sombre, titre de huit mots au plus |
| `enonce` | `g-enonce.html` | Fond sombre, une phrase forte (deux lignes au plus) et une phrase d'appui. Trois ou quatre fois dans la présentation, pas plus |
| `cartes-3` | `g-cartes-3.html` | Trois cartes numérotées (20 mots chacune) et un bandeau facultatif |
| `avant-apres` | `g-avant-apres.html` | Grille à trois colonnes : moment, aujourd'hui, avec l'aide. Quatre lignes |
| `maquette-ecran` | `g-maquette.html` | Texte court à gauche, fenêtre d'écran à droite (cinq lignes au plus), mention « Maquette — données fictives » obligatoire |
| `etapes-fleches` | `g-etapes.html` | Trois étapes reliées par des flèches, et un bandeau |
| `grand-chiffre` | `g-grand-chiffre.html` | Un chiffre en très grand à gauche, ce qu'il comprend à droite |
| `frise-3-horizons` | `g-frise.html` | Trois colonnes : un an, deux ans, cinq ans, chacune avec son degré de certitude et sa condition |
| `decision` | `g-decision.html` | À gauche la décision demandée (trois lignes cochées), à droite le calendrier par semaine |
| `tableau` | `g-tableau.html` | Tableau de cinq lignes au plus, trois colonnes |
| `deux-colonnes` | `g-deux-colonnes.html` | Un propos à gauche, un encadré sombre à droite |
| `image` | `g-image.html` | Texte à gauche, image à droite avec sa légende |
| `questions` | `g-questions.html` | Clôture sur fond sombre, trois ou quatre questions |

Vous pouvez combiner deux gabarits ou en adapter un si le contenu l'exige, en restant dans le contrat du § 1 et la grille du § 2.

## 5. Contrôle obligatoire

Depuis le dossier `render/` (à côté de `gabarits/`) :

```
node render.js <dossier project> <dossier de sortie> <id,id,…>
node lint.js <dossier project> <id,id,…>
```

La seconde commande relit le code et le texte : balises et propriétés permises, propriété sur la bonne balise, pied de page, notes, mots interdits, montants, guillemets. Une ligne `ERREUR` doit disparaître ; une ligne `ALERTE` doit être lue et, sauf raison écrite, corrigée.

La commande affiche, par diapositive : hauteur naturelle, `DÉBORDE +N` ou `marge N`, nombre de mots visibles, plus petite taille de texte, longueur du titre, et écrit une image `<id>.png` à regarder (outil Read). Une diapositive n'est pas terminée tant que : elle ne déborde pas ; la marge est entre 60 et 200 ; les mots sont sous le plafond ; aucune taille sous 24px ; le titre fait 55 caractères au plus ; l'image regardée est lisible et équilibrée. `SECTIONS=` suivi d'un nombre différent de 1 signale un fichier mal formé.

Les images hébergées (`/_blob/…`) apparaissent en gris dans ce rendu : c'est normal.

## 6. Images disponibles (aucune autre)

| Identifiant à écrire dans `src` | Ce que l'on voit | Usage prévu | Légende obligatoire |
|---|---|---|---|
| `/_blob/0da19f0843c584b5fda3b7136d3818a6` | Grande salle de pierre, mur peint aux couleurs du fleuve, invités de dos | Couverture | « Visuel : vision générée par IA — dossier Strates » |
| `/_blob/51a8be11835fa54a99fff4c0a99ac522` | Dévoilement d'un grand relief dans une galerie aux murs de pierre | Diapositive « ce que nous avons déjà préparé pour vous » | « Vision générée par IA — dossier Strates, déjà remis » |
| `/_blob/99f8d10e60b36c00c9a38334b5a95ee4` | Bras robotisé sur un banc d'essai, sous protection | Diapositive robotique seulement | « Vision générée par IA » |

Une image générée par IA n'est jamais présentée comme une photo d'un lieu ou d'un équipement réel.
