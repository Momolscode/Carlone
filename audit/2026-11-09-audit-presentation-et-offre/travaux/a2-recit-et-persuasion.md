# A2 — Le récit de la présentation et sa force de conviction

9 novembre 2026 · note de travail interne — ne pas transmettre au client

Objet : la présentation v11 (26 diapositives), lue en entier dans l'ordre du champ `order`, texte visible et notes de l'orateur. Cette note juge le récit, pas l'exactitude juridique ni le prix.

Sources abrégées dans la suite :

- **Cadrage** : `audit/2026-11-04-audit-strategique/pour-gianluca/2026-11-09-proposition-de-cadrage.md`
- **Logiciel** : `pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md`
- **Annexe logiciel** : `pour-carlone/logiciels-et-automatisations/2026-11-09-annexe-specification-logiciel-gestion-proprietes.md`
- **Fiches** : `pour-carlone/logiciels-et-automatisations/2026-11-09-automatisations-fiches-detaillees.md`
- **Rendez-vous** : `audit/2026-11-04-audit-strategique/interne/13-preparation-rendez-vous.md`
- **Commerciale** : `audit/2026-11-04-audit-strategique/interne/11-proposition-commerciale-revisee.md`
- **Mise à jour** : `audit/2026-11-04-audit-strategique/interne/2026-11-09-mise-a-jour-faits-nouveaux.md`

## Conclusion en cinq lignes

1. La v11 est un exposé, pas une proposition : 23 diapositives passent avant l'offre, qui arrive en 24e position sur 26, sans prix ; la dernière pose quatre questions ouvertes au lieu de demander une décision.
2. Elle montre tout ce que l'IA peut faire (47 aides, douze domaines, la robotique, cinq ans) et presque rien de ce que GianLuca Carlone a demandé : les mots « logiciel de gestion », « forfait », « maquette » et le signe « € » n'y figurent pas une seule fois.
3. Les meilleurs arguments honnêtes existent déjà dans le dépôt et ne sont pas à l'écran : le prix fixe de 6 500 € HT, « Il peut conclure qu'elle suffit », « L'approche A est la moins chère », le remboursement de la part non faite, la grille de questions à poser à toute offre.
4. Séquence proposée : 21 diapositives en cinq temps (vous, du concret, ce que l'IA apporte, l'offre, votre décision) et 8 en annexe ; la vision passe de 16 diapositives à 5, la décision de 3 à 9.
5. Longueur : 60 mots au plus par diapositive (la v11 en compte 103 en moyenne ; 23 sur 26 dépassent 60), un titre de 55 caractères au plus qui dit la conclusion, aucune promesse dans les notes.

## 1. La ligne de la présentation en une phrase

**La ligne de la v11, telle qu'elle ressort** : « Voici tout ce que l'IA peut faire pour vos lieux, les règles à respecter et ce que deviendra notre société ; rien de tout cela ne vous engage. »

Preuves :

- Présentation v11, diapositive `cover`, sous-titre : « Pour vos lieux, vos commerces et votre administration : les avancées, toutes les aides possibles, les enjeux, et ce que deviendra notre société dans un, deux et cinq ans. » Quatre sujets annoncés, aucun n'est sa décision.
- `cover` : « Novembre 2026 · document de présentation, sans engagement ». Notes : « Rien n'y est un engagement. » La présentation dit elle-même qu'il n'y a rien à décider.
- Les cinq parties de `deck.json` : vos projets et les avancées (5 diapositives) ; « Toutes les aides que nous pouvons apporter » (12) ; « Les enjeux » (3) ; « Notre société, ce qu'elle apportera à d'autres, et sa trajectoire » (4) ; « Pour commencer » (2). L'offre est la dernière partie et la plus courte, et `etapes`, qui décrit le chemin proposé, est rangée dans la partie sur notre société.
- `premier-pas` : « La proposition chiffrée vous est remise à part. » Le prix est renvoyé hors de l'écran.

**La ligne recommandée** : « Votre projet est large et vous avez une administratrice pour le coordonner : commençons par un premier pas court, à prix fixe, que vous jugez sur pièces ; vous pouvez vous arrêter ensuite et vous gardez ce que vous avez payé. »

Elle reprend la phrase déjà écrite pour lui dans **Cadrage** : « Nous vous proposons de commencer par un cadrage court, à prix fixe. Vous décidez ensuite sur pièces, avant tout engagement plus long. »

Règle de tri qui en découle : une diapositive reste dans la séquence principale si elle l'aide à dire oui ou non au premier pas. Sinon elle part en annexe ou elle est coupée.

## 2. Les 26 diapositives, une par une

Méthode de comptage : script python3 (`html.parser`) qui retire les balises et tout le contenu de la balise `<aside>`. Un mot = une suite de caractères sans espace qui contient au moins une lettre ou un chiffre. La ligne de pied de page (« Marwin Tech · pour GianLuca Carlone · novembre 2026 · N », 5 à 13 mots) n'est pas comptée. Total : 2 672 mots visibles, 103 en moyenne ; 1 839 mots de notes en plus.

| N° | Id | Titre | Rôle dans le récit | Mots | Verdict | Raison |
|---|---|---|---|---|---|---|
| 1 | `cover` | Ce que l'IA peut faire pour vos projets | Ouverture : annonce un panorama | 48 | réécrire | Le sous-titre annonce quatre sujets et pas l'offre ; « sans engagement » dit qu'il n'y a rien à décider ; l'image générée montre un « bras robotisé sous protection ». |
| 2 | `compris` | Ce que nous avons compris | Reformulation de son projet | 77 | réécrire | Seule diapositive qui parle de lui, mais sa demande de logiciel de gestion de propriété n'y est pas et le titre ne l'invite pas à corriger. |
| 3 | `idee` | Votre administratrice et vos équipes, outillées par l'IA, pour faire davantage sous votre contrôle. | Principe général | 53 | fusionner avec `administratrice` et `modes` | Titre de 99 caractères ; ses trois principes (vous décidez, une personne contrôle, on mesure) reviennent sur sept autres diapositives. |
| 4 | `avancees` | Des avancées qui changent l'échelle du possible | Nouveautés 2025-2026 | 118 | réécrire | Six affirmations sans source et un titre d'effet ; à ramener à trois nouveautés utiles à ses affaires, chacune avec sa source. |
| 5 | `ia-aujourdhui` | Ce qu'elle fait bien, et ce qu'elle fait mal | Limites de l'IA | 94 | garder (alléger) | La diapositive la plus honnête du jeu : elle fonde la confiance ; passer de trois colonnes à deux. |
| 6 | `administratrice` | Elle coordonne, l'IA prépare, nous construisons | Place de son administratrice | 138 | fusionner avec `modes` et `idee` | Idée juste et bon titre, mais 138 mots et une promesse de trop (« Retrouve n'importe quel document »). |
| 7 | `domaines` | Douze domaines, de l'administration à la robotique | Sommaire du catalogue | 98 | couper | Douze domaines contredisent sa propre dernière ligne (« nous avançons un domaine à la fois ») ; sans catalogue dans le fil principal, le sommaire n'a plus d'objet. |
| 8 | `modes` | Ce que l'IA fait seule, ce qu'elle prépare, ce qui reste à vous | Trois niveaux d'aide | 97 | garder (réécrire le titre) | Cadre décidé et rassurant ; titre de 63 caractères et deuxième classement de suite après `ia-aujourdhui`. |
| 9 | `cat-admin` | Administration et pilotage, pour votre administratrice | Catalogue 1 sur 6 | 111 | passer en annexe | Ses deux lignes fortes (échéances, comptes rendus) deviennent l'exemple et la maquette ; « en quelques secondes » et « Sous 24 heures » sont des délais sans source. |
| 10 | `cat-batiments` | Bâtiments, travaux et sécurité | Catalogue 2 sur 6 | 88 | passer en annexe | C'est le sujet de sa demande de logiciel : le traiter dans la diapositive sur le logiciel, garder le tableau pour répondre à une question. |
| 11 | `cat-galerie` | Galerie, œuvres et ventes d'art | Catalogue 3 sur 6 | 104 | passer en annexe | Utile seulement si la vente d'œuvres fait partie de ses priorités (ordre du jour de **Rendez-vous** : « Seulement si c'est une de ses priorités »). |
| 12 | `cat-cabaret` | Cabaret-spectacle et commerces | Catalogue 4 sur 6 | 111 | passer en annexe | Le cabaret n'est pas ouvert : huit aides hypothétiques, à montrer s'il le place en tête. |
| 13 | `cat-finance` | Finance, équipes et conformité | Catalogue 5 sur 6 | 116 | passer en annexe | Tableau le plus chargé du catalogue ; « toujours à jour » est une promesse. |
| 14 | `cat-marketing` | Marketing, contenus et événements | Catalogue 6 sur 6 | 98 | passer en annexe | Sixième tableau de suite ; la prospection y dépend d'un fichier à remettre en conformité, donc rien à montrer comme prêt. |
| 15 | `crm` | Vendre vos œuvres aux entreprises de la Nièvre | Gros plan sur la prospection | 122 | couper | Met en avant un fichier inutilisable en l'état (« il sera remis en conformité avant tout usage ») et un chiffre sans source (« 500 entreprises ») ; **Rendez-vous** exclut toute démonstration du CRM. |
| 16 | `logiciels` | Les bons outils, à votre nom, sans dépendre de nous | Gros plan sur les logiciels | 132 | réécrire | C'est la réponse à sa demande, mais le surtitre dit « Logiciels sur mesure » (option écartée par le brief) et les mots « gestion de propriété » n'y sont pas. |
| 17 | `robotique` | La robotique, pour la galerie et la scène : plus tard, sous conditions | Gros plan sur la robotique | 131 | couper (une ligne dans « Plus tard, sous conditions ») | 131 mots et 118 mots de notes pour un sujet sans date ni financement, que les notes appellent « la partie la plus spectaculaire ». |
| 18 | `apports` | Ce que vous pouvez en attendre | Bénéfices | 94 | fusionner avec la nouvelle diapositive avant/après | Quatre noms abstraits (« Du temps », « Une seule source », « De la réactivité », « Une image soignée ») sans situation de départ. |
| 19 | `regles` | Les risques de l'IA, et notre réponse | Risques et parades | 113 | passer en annexe | Tableau de sept lignes utile en réponse à une question ; trois garanties seulement montent dans le fil principal. |
| 20 | `methode` | Vous décidez, nous préparons et nous rendons des comptes | Façon de travailler | 109 | fusionner avec `etapes` et `regles` | Bon titre ; quatre de ses six cartes redisent `logiciels`, `regles` ou `etapes`. |
| 21 | `societe` | Marwin Tech, la société que nous créons | Qui nous sommes | 107 | réécrire | La seule preuve de savoir-faire citée est un outil qui n'est pas en règle ; rien sur qui fait quoi ni sur son interlocuteur. |
| 22 | `pour-dautres` | Ce que Marwin Tech apportera aussi à d'autres | Avenir de Marwin Tech | 102 | couper | Parle de nos futurs clients, pas de lui ; « garantit aussi la continuité de Marwin Tech » est une garantie sans fondement pour une société non créée. |
| 23 | `trajectoire` | Dans un an, deux ans, cinq ans | Avenir à un, deux, cinq ans | 160 | réécrire (fusionner avec `robotique`) | La plus longue ; une ligne sur deux décrit l'avenir de Marwin Tech ; garder la seule ligne « Pour vos projets », avec ses conditions. |
| 24 | `etapes` | Chaque étape se gagne par des preuves | Le chemin, étape par étape | 95 | garder (remonter, dater) | Meilleur titre du jeu et vrai retournement du risque, mais en 24e position et sans date. |
| 25 | `premier-pas` | Un cadrage de trois à quatre semaines | L'offre | 113 | réécrire (scinder en deux) | L'offre sans son prix (« La proposition chiffrée vous est remise à part ») et sans le mot « forfait ». |
| 26 | `echange` | Parlons de vos priorités | Clôture | 43 | réécrire (scinder) | Quatre questions ouvertes à la place d'une décision ; trois d'entre elles ouvrent la nouvelle séquence, la fin devient « oui, à ajuster, ou non ». |

Bilan des verdicts : 3 à garder, 8 à réécrire, 4 à fusionner, 4 à couper, 7 à passer en annexe.

Trois constats transversaux :

- **Les notes pèsent 69 % du texte visible** (1 839 mots pour 2 672) et sont lisibles par toute personne qui ouvre le lien. Elles portent les formules les plus fortes : `administratrice`, « un assistant IA qui connaît tous vos projets » ; `cat-admin`, « C'est là que les gains de temps sont les plus rapides et les plus faciles à mesurer. » ; `avancees`, « sont devenus fiables » ; `societe`, « la garantie que vos outils et vos données restent à votre nom ». **Mise à jour** le disait déjà : « Elles portent les promesses les plus fortes. »
- **Les seuls visuels montrent ce qui n'existe pas** : deux images générées par IA (`cover`, `robotique`), toutes deux avec un bras robotisé. Aucun écran, aucune maquette, aucun document type.
- **Le catalogue est exact mais mal placé** : 47 aides (7 automatiques, 30 assistées, 10 préparées, comptage vérifié dans les six fichiers `cat-*`), montrées en six tableaux de suite, alors que **Fiches** écrit : « La première année, nous visons deux à quatre automatisations en service et mesurées, pas quinze. »

## 3. Les 26 titres lus seuls

Lus à la suite, les titres donnent ceci :

1. Ce que l'IA peut faire pour vos projets — 2. Ce que nous avons compris — 3. Votre administratrice et vos équipes, outillées par l'IA, pour faire davantage sous votre contrôle. — 4. Des avancées qui changent l'échelle du possible — 5. Ce qu'elle fait bien, et ce qu'elle fait mal — 6. Elle coordonne, l'IA prépare, nous construisons — 7. Douze domaines, de l'administration à la robotique — 8. Ce que l'IA fait seule, ce qu'elle prépare, ce qui reste à vous — 9. Administration et pilotage, pour votre administratrice — 10. Bâtiments, travaux et sécurité — 11. Galerie, œuvres et ventes d'art — 12. Cabaret-spectacle et commerces — 13. Finance, équipes et conformité — 14. Marketing, contenus et événements — 15. Vendre vos œuvres aux entreprises de la Nièvre — 16. Les bons outils, à votre nom, sans dépendre de nous — 17. La robotique, pour la galerie et la scène : plus tard, sous conditions — 18. Ce que vous pouvez en attendre — 19. Les risques de l'IA, et notre réponse — 20. Vous décidez, nous préparons et nous rendons des comptes — 21. Marwin Tech, la société que nous créons — 22. Ce que Marwin Tech apportera aussi à d'autres — 23. Dans un an, deux ans, cinq ans — 24. Chaque étape se gagne par des preuves — 25. Un cadrage de trois à quatre semaines — 26. Parlons de vos priorités

**Racontent-ils une histoire ?** Non : ils donnent le plan d'un exposé (l'IA, ses usages, ses risques, notre société, puis un cadrage). Quelqu'un qui ne lit que les titres apprend ce que l'IA sait faire, pas ce qu'on lui propose ni ce qu'il doit décider.

- Quatre titres sur 26 sont des phrases qui affirment quelque chose : `administratrice`, `methode`, `etapes`, `echange`. Ce sont les meilleurs.
- Six titres commencent par « Ce que » ou « Ce qu' » (`cover`, `compris`, `ia-aujourdhui`, `modes`, `apports`, `pour-dautres`) : ils annoncent un contenu au lieu de le dire. « Ce que vous pouvez en attendre » ne dit pas ce qu'il peut en attendre.
- Dix titres sont des étiquettes de rubrique (`domaines`, les six `cat-*`, `regles`, `societe`, `trajectoire`).
- Le mot « cadrage » apparaît pour la première fois au titre 25. Aucun titre ne contient un prix, une date ou le mot « décision ».
- Quatre titres dépassent 55 caractères : `idee` (99), `robotique` (70), `modes` (63), `methode` (56).

**Où cela se répète.**

- « Une personne valide » : l'idée figure dans le texte visible de 14 diapositives sur 26 (recherche de « valid », « relecture », « vérifi », « contrôle »). « On mesure » : 10 diapositives. Une fois bien dite, puis rappelée dans l'offre, elle suffit.
- « À votre nom » : `domaines`, `logiciels`, `regles`, `methode`, `societe`, `pour-dautres`.
- Deux classements de suite pour la même idée : `ia-aujourdhui` (fait bien, à surveiller, à ne pas confier) puis `modes` (automatique, assistée, préparée), séparés par `administratrice` et `domaines` qui en proposent encore deux autres (trois colonnes, douze tuiles).
- La robotique, annoncée « plus tard, sous conditions », revient dans le texte de cinq diapositives (`avancees`, `domaines`, `robotique`, `societe`, `etapes`) et sur l'image d'ouverture. Elle prend plus de place que le premier pas.
- Marwin Tech parle d'elle-même sur trois diapositives de suite (`societe`, `pour-dautres`, `trajectoire`), juste avant de demander de l'argent.

**Où il manque une marche.**

- Entre 2 et 3 : sa demande. Il a parlé d'un « logiciel de gestion de propriété » ; aucune diapositive ne reprend ces mots.
- Entre 8 et 9 : un exemple. On passe des trois niveaux d'aide à 47 lignes de tableau sans montrer une seule aide en situation.
- Entre 18 et 19 : un avant et un après.
- Entre 23 et 24 : le passage de « dans cinq ans » à « trois à quatre semaines » se fait sans transition ; rien ne dit « tout cela commence par un pas ».
- Entre 25 et 26 : le prix, le calendrier, la comparaison avec une autre offre, et la question « que décidez-vous ? ».
- Les questions sur ses priorités arrivent en dernier (`echange`), alors que **Rendez-vous** fixe l'ordre : « Questions d'abord, proposition ensuite ».

## 4. Les leviers de persuasion légitimes, absents ou sous-exploités

### 4.1 La preuve par l'exemple (démonstration, maquette)

- **État dans la v11** : absente. Zéro occurrence de « maquette » ; aucun écran. Le brief dit pourtant de lui : « Il décide vite quand il voit du concret. »
- **Façon honnête de s'en servir** : deux écrans fixes, construits sur son cas mais avec des données inventées, chacun portant « Maquette — données fictives ». Le premier pour votre administratrice : le résumé du lundi des échéances de toutes les sociétés (**Fiches**, fiche 3). Le second pour lui : la liste « à décider » et la vue d'ensemble par société (**Annexe logiciel**, module 7, « douze au plus par vue »). Dire à voix haute : « Ceci n'existe pas encore. C'est ce que nous construirions si vous choisissez cette priorité. » Ne pas montrer le CRM (**Rendez-vous** : « aucune démonstration du CRM »).
- **Place** : diapositives 6 et 7 de la séquence, avant toute explication sur l'IA.

### 4.2 La réciprocité (ce qui a déjà été préparé pour lui)

- **État dans la v11** : absente. Rien ne dit ce qui a été préparé pour ce rendez-vous.
- **Façon honnête de s'en servir** : remettre, sans condition, ce qui lui sert même s'il dit non : la grille de seize critères pour comparer toute offre (**Logiciel**, section 8) et le résumé corrigé de ses projets. Le dire simplement : « Cette grille est pour vous, quelle que soit votre décision. » Ne pas rappeler les dossiers de création ni le prototype de CRM comme une dette : **Commerciale** range « Le CRM déjà livré justifie le prix » parmi les arguments à ne pas employer, et **Rendez-vous** place Strates, Éclosion et les visuels générés parmi les pièces à ne pas montrer.
- **Place** : diapositive 19 (la grille) et dernière minute.

### 4.3 Le risque retourné (forfait, arrêt à chaque étape, il garde ce qui est payé)

- **État dans la v11** : présent mais tardif et dispersé. `etapes` (24e) : « Arrêt possible à la fin de chaque étape : vous gardez ce qui est payé, vos comptes et vos données. » `premier-pas` (25e) : « Le dossier est à vous une fois réglé, même si vous vous arrêtez là. » Le mot « forfait » n'apparaît nulle part.
- **Façon honnête de s'en servir** : une diapositive à trois cartes, avec les clauses déjà écrites dans **Cadrage** : « Si vous arrêtez en cours de route, l'acompte reste acquis, le solde n'est pas dû, et vous recevez le travail fait. » ; « Si nous ne pouvons pas finir, vous recevez le travail fait et nous remboursons la part non faite. » ; « Sans immatriculation dans les deux mois qui suivent la signature, le bon de commande tombe, sans frais pour vous. » Et la phrase la plus désarmante du dossier : le cadrage « peut conclure qu'elle suffit » (votre administratrice, sans nous).
- **Précision à tenir** : écrire « vous gardez ce qui est payé », pas « vous gardez tout ». **Mise à jour** a déjà relevé la formule sans condition : la cession se fait au paiement.
- **Place** : diapositive 18, juste après le prix et les étapes.

### 4.4 La clarté de la décision

- **État dans la v11** : absente. `cover` : « sans engagement ». `premier-pas` : « La proposition chiffrée vous est remise à part. » `echange` : quatre questions, dont « Par quel domaine voulez-vous commencer ? ». On ne lui demande rien de précis.
- **Façon honnête de s'en servir** : une seule décision, dite dès la première diapositive et redemandée à la dernière, avec trois réponses possibles (oui ; oui, à ajuster ; non) et la suite concrète si c'est oui (**Cadrage**, section 7, « Prochaines étapes » : rendez-vous, bon de commande, immatriculation, acompte et démarrage). **Rendez-vous** : « Une réponse sur le cadrage et une date pour l'engagement écrit, sans signature en séance » ; « Un « non » est un résultat. »
- **Place** : diapositives 1, 20 et 21.

### 4.5 Le contraste avant/après

- **État dans la v11** : absent. `apports` donne quatre bénéfices sans point de départ.
- **Façon honnête de s'en servir** : un seul contraste, sur une tâche qu'il reconnaît. Avant (**Fiches**, fiche 3) : les échéances « dispersées entre les contrats, les e-mails et la mémoire de chacun ». Après : une liste unique, un résumé chaque lundi, des rappels internes. Le « avant » est une hypothèse : l'écrire « si c'est votre cas » et le faire confirmer. Aucun gain chiffré : **Logiciel** écrit « Le temps gagné n'est pas promis : il est mesuré pendant le pilote. »
- **Place** : diapositive 5.

### 4.6 Le coût réel de l'attente (sans dramatiser)

- **État dans la v11** : absent.
- **Façon honnête de s'en servir** : trois faits, dits une fois, sans adjectif. Un : les bâtiments acquis ont déjà des contrats, des assurances et des contrôles qui courent ; **Fiches** : « Une échéance manquée coûte : contrat reconduit sans le vouloir, assurance expirée, pénalité. » Deux : votre administratrice prend ses habitudes de travail maintenant ; choisir les outils avec elle au début évite de les changer ensuite (c'est un raisonnement, pas un chiffre : le dire comme tel). Trois : les vraies dates, et elles seules : proposition « valable jusqu'au jeudi 31 décembre 2026 », démarrage « début janvier 2027 si la commande est signée avant la mi-décembre » (**Cadrage**).
- **Place** : diapositive 5 (une ligne) et diapositive 20 (les dates).

### 4.7 L'ancrage dans son projet à lui

- **État dans la v11** : faible. Une diapositive sur 26 (`compris`) parle de lui ; le catalogue pourrait être montré tel quel à un autre client. Ni ses mots (« logiciel de gestion de propriété »), ni sa ville, ni un de ses lieux ne figurent à l'écran.
- **Façon honnête de s'en servir** : reprendre ses mots dans un titre ; lui faire choisir entre les trois sens de sa demande (**Logiciel**, section 1 : « Merci de nous dire lesquels comptent pour vous, et dans quel ordre. ») ; bâtir les maquettes sur sa situation (une galerie, un cabaret-spectacle, des commerces, plusieurs sociétés) avec des noms et des montants inventés et signalés. Tout ce qui vient des déclarations du 9 novembre reste marqué « à confirmer avec vous ».
- **Place** : diapositives 2, 3, 4, 6, 7.

### 4.8 La personne (qui sont Morgan et Mathys, pourquoi eux)

- **État dans la v11** : une phrase, dans `societe` : « Morgan Olsen et Mathys Couet, associés. Nous avons déjà construit un outil de prospection des entreprises de la Nièvre, qui sera remis en conformité avant tout usage. » La seule preuve citée est un outil à corriger.
- **Façon honnête de s'en servir** : dire qui fait quoi et qui est son interlocuteur ; faire de la petite taille une règle de travail plutôt qu'une excuse : « L'un de nous mène le travail, l'autre le relit. » (**Cadrage**) ; « Nous sommes deux : une étape et un essai à la fois. » (`etapes`). Dire le statut sans détour : société en cours de création, immatriculée avant toute facture et tout démarrage. Le parcours de chacun est à écrire par Morgan et Mathys, avec des faits vérifiables seulement : aucune référence client, aucun témoignage.
- **Place** : diapositive 14, avant le prix.

### 4.9 Les techniques à ne pas employer

- La fausse urgence (« offre valable cette semaine ») et la fausse rareté (« une seule place »). La capacité limitée à deux personnes est vraie : elle se dit comme une règle de travail, pas comme une pression.
- Une référence client, un témoignage ou un logo : il n'y en a pas.
- Un chiffre de gain de temps ou d'économie avant la mesure de départ. Les délais non sourcés de `cat-admin` (« en quelques secondes », « Sous 24 heures ») sont à retirer.
- Une garantie de résultat, y compris dans les notes (« garantit », « toujours à jour », « n'importe quel document »).
- Nommer l'autre prestataire, citer son prix, le critiquer, ou ancrer notre prix sur le sien. La comparaison passe par la grille neutre, que nous remplissons aussi pour nous.
- « Le CRM déjà livré justifie le prix » et toute réciprocité qui culpabilise (**Commerciale**).
- « Avec l'IA, nous faisons le travail de dizaines de personnes » (**Commerciale**) et la peur de « rater le train de l'IA ».
- L'avantage fiscal des achats d'œuvres comme argument de vente.
- Le spectaculaire pour vendre de l'administratif : images de robots, titre « Des avancées qui changent l'échelle du possible ».
- Le catalogue comme démonstration de force : 47 lignes ne prouvent pas qu'une seule marche.
- Le prix caché jusqu'à la fin. **Rendez-vous** : « Cacher le prix abîme la confiance ».
- L'avenir de Marwin Tech présenté comme un bénéfice pour lui (`pour-dautres`, moitié de `trajectoire`).

## 5. Vision et décision : le rapport

Classement des 26 diapositives de la v11 :

| Famille | Diapositives | Nombre | Mots visibles | Part des mots |
|---|---|---|---|---|
| Lui et son projet | `cover`, `compris`, `idee`, `administratrice` | 4 | 316 | 12 % |
| Vision : ce que l'IA peut faire, l'avenir | `avancees`, `ia-aujourdhui`, `domaines`, `modes`, six `cat-*`, `crm`, `logiciels`, `robotique`, `apports`, `pour-dautres`, `trajectoire` | 16 | 1 776 | 66 % |
| Confiance : règles, méthode, société | `regles`, `methode`, `societe` | 3 | 329 | 12 % |
| Décision : l'offre | `etapes`, `premier-pas`, `echange` | 3 | 251 | 9 % |

Lecture : 16 diapositives de vision pour 3 de décision, et `echange` ne demande pas de décision. Deux tiers des mots décrivent des possibilités ; moins d'un dixième décrit ce qu'il achète. 91 % du texte visible (2 421 mots sur 2 672) passe avant `etapes`, première diapositive de l'offre ; le mot « cadrage » n'apparaît à l'écran qu'à la 25e.

Équilibre recommandé, sur 21 diapositives :

| Famille | Diapositives de la séquence | Nombre | Part |
|---|---|---|---|
| Lui et son projet | 2, 3, 4 | 3 | 14 % |
| Du concret : avant/après et maquettes | 5, 6, 7 | 3 | 14 % |
| Vision : nouveautés, limites, niveaux d'aide, avenir | 8, 9, 10, 11, 12 | 5 | 24 % |
| Qui nous sommes | 14 | 1 | 5 % |
| Décision : l'offre, le prix, les étapes, les garanties, la comparaison, la suite | 1, 13, 15, 16, 17, 18, 19, 20, 21 | 9 | 43 % |

La demande de Morgan (« les dernières nouveautés », « ce qu'on pourra apporter à l'avenir ») garde ses deux diapositives (8 et 12). Elles servent la décision au lieu de la retarder : la 12 se termine sur « tout cela commence par un premier pas ». Le catalogue complet reste disponible en annexe pour toute question.

## 6. La séquence idéale

Règles communes : vouvoiement ; un titre = une phrase de 55 caractères au plus ; 60 mots au plus ; pied de page inchangé ; aucune image générée de robot ; toute maquette porte « Maquette — données fictives » ; tout ce qui vient des déclarations du 9 novembre porte « à confirmer avec vous ».

### 6.1 Séquence principale : 21 diapositives

**Temps 1 — Vous**

| N° | Titre de travail | But | D'où vient le contenu | Mise en page |
|---|---|---|---|---|
| 1 | Un premier pas court, à prix fixe, jugé sur pièces | Dire la proposition dès l'ouverture. Sous-titre : cadrage de trois à quatre semaines, 6 500 € HT au forfait, rien à signer aujourd'hui. | v11 `cover`, réécrite ; **Cadrage** (introduction) | énoncé |
| 2 | Voici ce que nous avons compris : corrigez-nous | Montrer qu'on l'a écouté ; le faire parler tout de suite. Trois cartes : vos lieux, votre organisation, votre demande de logiciel. | v11 `compris` ; brief, section 2 (faits à confirmer) | trois cartes |
| 3 | Vos priorités d'abord : trois questions | Recueillir ses priorités avant de proposer. | v11 `echange` (questions 1, 2 et 4), remontée | questions |
| 4 | « Gestion de propriété » : trois sens, lequel compte ? | Reprendre ses mots et lui faire choisir : bâtiments, logiciel hôtelier, pilotage de plusieurs lieux. | **Logiciel**, section 1 | trois cartes |

**Temps 2 — Du concret**

| N° | Titre de travail | But | D'où vient le contenu | Mise en page |
|---|---|---|---|---|
| 5 | Avant : des échéances dispersées. Après : une liste | Un seul contraste, sur une tâche qu'il reconnaît ; une ligne sur ce que coûte une échéance manquée. | **Fiches**, fiche 3 ; **Logiciel**, section 2 ; v11 `apports` | avant/après |
| 6 | Chaque lundi, les échéances de toutes vos sociétés | Faire voir l'aide du point de vue de votre administratrice. | À écrire, d'après **Fiches**, fiche 3 (résumé du lundi) | maquette d'écran |
| 7 | Une seule liste pour ce que vous devez décider | Faire voir l'aide de son point de vue à lui : liste « à décider », vue d'ensemble par société. | À écrire, d'après **Annexe logiciel**, module 7 | maquette d'écran |

**Temps 3 — Ce que l'IA apporte, et ses limites**

| N° | Titre de travail | But | D'où vient le contenu | Mise en page |
|---|---|---|---|---|
| 8 | Trois nouveautés de 2026 qui servent vos affaires | Répondre à « quoi de neuf ? » par trois faits utiles (lire des documents, préparer des dossiers, rendre compte d'une réunion), chacun avec sa source datée. | v11 `avancees`, réduite de six à trois ; sources à écrire | trois cartes |
| 9 | L'IA prépare bien ; elle ne décide ni ne signe | Fonder la confiance par les limites. | v11 `ia-aujourdhui` (colonnes 1 et 3) | deux colonnes |
| 10 | Votre administratrice coordonne, l'IA prépare | Les trois niveaux d'aide ; votre administratrice est aidée, jamais remplacée ; rien ne part sans validation. | v11 `modes`, `administratrice`, `idee` | trois cartes |
| 11 | Cinq aides à examiner, trois retenues au plus | Remplacer le catalogue par un choix court et montrer la retenue. Renvoi : « Les 47 aides sont en annexe. » | **Fiches**, section 4 ; v11 `cat-admin` | tableau |
| 12 | Plus tard, sous conditions : ce qui pourra s'ajouter | Dire l'avenir comme une ambition, avec ses conditions ; la robotique en une ligne, sans date. Dernière ligne : « Tout cela commence par un premier pas. » | v11 `trajectoire` (lignes « Pour vos projets »), `robotique`, `etapes` (étape 4) | frise |

**Temps 4 — L'offre**

| N° | Titre de travail | But | D'où vient le contenu | Mise en page |
|---|---|---|---|---|
| 13 | Votre logiciel : acheter, relier, construire peu | Répondre à sa demande : trois approches, notre recommandation par étapes, et la phrase « L'approche A est la moins chère. » Aucun montant ici. | **Logiciel**, sections 3 et 4 ; v11 `logiciels` | tableau |
| 14 | Nous sommes deux : une étape et un essai à la fois | Qui fait quoi, qui est son interlocuteur, statut de la société, relecture à deux. | v11 `societe` ; **Cadrage** ; parcours à écrire par Morgan et Mathys | deux colonnes |
| 15 | Le premier pas : un cadrage à 6 500 € HT, au forfait | Montrer le prix en grand : 7 800 € TTC, moitié à la commande, trois à quatre semaines. | **Cadrage**, section 2 (prix et paiement) | grand chiffre |
| 16 | En trois à quatre semaines, quatre livrables à vous | Ce qu'il reçoit ; ce dont nous avons besoin. | v11 `premier-pas` | deux colonnes |
| 17 | Chaque étape se gagne par des preuves | Le chemin daté : cadrage, essai de huit semaines, bilan, suivi revu chaque trimestre ; un arrêt possible à chaque jonction. | v11 `etapes` ; dates de **Logiciel**, section 5 (à valider) | frise |
| 18 | Arrêt à chaque étape : vous gardez ce qui est payé | Retourner le risque : prix fixe ; arrêt et remboursement de la part non faite ; comptes et données à votre nom. Bande : le cadrage peut conclure que votre administratrice suffit. | **Cadrage** (« En cas d'arrêt ou de retard ») ; v11 `etapes`, `methode`, `regles`, `logiciels` | trois cartes |
| 19 | Six questions à poser à toute offre, la nôtre aussi | Donner une grille neutre : durée d'engagement, coût sur trois ans, propriété des données, sortie, temps de votre administratrice, interlocuteur. La grille complète est remise sur papier. | **Logiciel**, section 8 (seize critères) | questions |

**Temps 5 — Votre décision**

| N° | Titre de travail | But | D'où vient le contenu | Mise en page |
|---|---|---|---|---|
| 20 | Si vous dites oui : quatre étapes d'ici janvier | Rendre le oui facile : rendez-vous, bon de commande signé par sa société, immatriculation de Marwin Tech, acompte et démarrage début janvier 2027. | **Cadrage**, section 7 | étapes |
| 21 | Votre décision : oui, à ajuster, ou non | Demander la décision ; trois réponses possibles ; quelle société signe, qui est notre interlocuteur, quelle date. | À écrire, d'après **Rendez-vous**, section 1 | énoncé |

### 6.2 Annexe : 8 diapositives

| N° | Titre de travail | But | D'où vient le contenu | Mise en page |
|---|---|---|---|---|
| A1 | Administration : huit aides, dont deux automatiques | Répondre à une question sur le quotidien de votre administratrice. | v11 `cat-admin`, sans les délais non sourcés | tableau |
| A2 | Bâtiments et travaux : sept aides, trois automatiques | Détail du domaine lié à sa demande de logiciel. | v11 `cat-batiments` | tableau |
| A3 | Galerie et œuvres : huit aides, aucune automatique | Si la vente d'œuvres est une priorité. | v11 `cat-galerie` | tableau |
| A4 | Cabaret et commerces : huit aides, aucune automatique | Si le cabaret-spectacle est une priorité. | v11 `cat-cabaret` | tableau |
| A5 | Finance et équipes : huit aides, dont deux automatiques | Si la gestion et la conformité sont une priorité. | v11 `cat-finance`, sans « toujours à jour » | tableau |
| A6 | Communication : huit aides, aucune automatique | Si la communication est une priorité. | v11 `cat-marketing` | tableau |
| A7 | Sept risques de l'IA, et notre réponse à chacun | Répondre à une objection sur les données, la fiabilité ou la dépendance. | v11 `regles` | tableau |
| A8 | Votre logiciel, étape par étape : contenu et prix | Seulement s'il demande les prix de la suite : jusqu'au bilan du pilote, 15 700 à 18 700 € HT, commandés et payés étape par étape. Prix à valider par Morgan et Mathys avant tout affichage. | **Logiciel**, sections 5 et 7 | tableau |

### 6.3 Ce qui disparaît

- `domaines` : remplacée par la diapositive 11 et par l'annexe.
- `crm` : rien à montrer tant que le fichier n'est pas remis en conformité ; la ligne « Prospection d'entreprises » de `cat-marketing` (A6) suffit.
- `robotique` : une ligne dans la diapositive 12.
- `pour-dautres` : une seule phrase gardée, dans la diapositive 14 : « Vos données ne servent jamais à d'autres. »
- La moitié « Pour Marwin Tech » de `trajectoire`.

## 7. Les deux premières et les deux dernières minutes

Ces minutes sont celles de la présentation elle-même. L'accueil et le point sur l'incident de données, prévus avant dans **Rendez-vous**, se font sans diapositive.

### 7.1 Les deux premières minutes

**Ce qui est montré** : la diapositive 1 pendant quarante secondes environ, puis la diapositive 2. Pas d'image de robot ; une photo d'un de ses lieux si nous en avons une que nous avons le droit d'utiliser, sinon aucun visuel.

**Ce qui est dit** (à adapter, phrases courtes) :

> « Aujourd'hui, il n'y a rien à signer. Nous venons avec une seule proposition : un premier pas court, à prix fixe. Trois à quatre semaines, 6 500 euros hors taxes. À la fin, vous jugez sur pièces et vous décidez de la suite. Vous pouvez aussi décider de vous arrêter là.
>
> Avant d'en parler, nous voulons vérifier que nous avons bien compris. Voici ce que nous avons noté : des bâtiments à aménager, la galerie, un cabaret-spectacle juste à côté, des commerces à ouvrir, et votre administratrice qui coordonne l'ensemble. Vous avez aussi parlé d'un logiciel de gestion de propriété.
>
> Qu'est-ce qui est faux ? Qu'est-ce qui manque ? »

Puis se taire et noter. La diapositive 3 (ses priorités) reste à l'écran pendant qu'il parle. **Rendez-vous** : « Écouter plus que parler dans les 50 premières minutes ».

Pourquoi ainsi : il connaît le prix et la taille de la décision dès la première minute, donc il écoute la suite sans attendre le piège ; et la première chose qu'on lui demande est de corriger, pas d'approuver.

### 7.2 Les deux dernières minutes

**Ce qui est montré** : la diapositive 20 (quatre étapes d'ici janvier), puis la diapositive 21, qui reste à l'écran. Sur la table : la proposition de cadrage en deux exemplaires papier (**Rendez-vous**, section 7.1) et la grille de questions (**Logiciel**, section 8).

**Ce qui est dit** :

> « Pour résumer : un cadrage de trois à quatre semaines, 6 500 euros hors taxes, au forfait, moitié à la commande. Vous recevez l'inventaire de vos structures et de vos lieux, trois priorités à 90 jours, trois tâches à essayer au plus, et notre avis argumenté sur la suite. Ce dossier est à vous une fois réglé, même si vous vous arrêtez là.
>
> Trois réponses sont possibles : oui ; oui, mais autrement ; non. Un non nous convient aussi : dites-le-nous simplement.
>
> Si c'est oui : quelle société signerait le bon de commande ? Qui sera notre interlocuteur ? Quelle date vous convient pour nous répondre par écrit ?
>
> Nous vous laissons la proposition et la grille de questions. La proposition est valable jusqu'au 31 décembre. Si la commande est signée avant la mi-décembre, nous commençons début janvier. »

Ce qui n'est pas dit : aucune relance sur l'autre offre, aucune remise « si vous signez aujourd'hui », aucune signature en séance. Les deux dates citées sont celles de **Cadrage** ; elles se disent une fois.

## 8. La longueur

**Maximum recommandé** (texte visible, pied de page non compté) :

| Type de diapositive | Maximum |
|---|---|
| Énoncé, grand chiffre | 30 mots |
| Trois cartes, deux colonnes, avant/après, étapes, frise, questions | 60 mots |
| Maquette d'écran | 25 mots hors de l'écran simulé |
| Tableau (principal ou annexe) | 80 mots |
| Titre | 55 caractères |
| Notes de l'orateur | 80 mots, sans rien qu'on n'écrirait pas sur la diapositive |

Repère interne plutôt que règle importée : les trois diapositives de la v11 qui se lisent d'un coup d'œil sont `cover` (48 mots), `idee` (53) et `echange` (43). Avec ces plafonds, les 21 diapositives principales tiennent en 1 260 mots au plus, contre 2 672 pour la v11 : moins de la moitié.

**Diapositives de la v11 qui dépassent 60 mots** : 23 sur 26, toutes sauf `cover`, `idee` et `echange`.

- De 61 à 80 mots (1) : `compris` 77.
- De 81 à 100 mots (7) : `cat-batiments` 88, `ia-aujourdhui` 94, `apports` 94, `etapes` 95, `modes` 97, `domaines` 98, `cat-marketing` 98.
- Plus de 100 mots (15) : `pour-dautres` 102, `cat-galerie` 104, `societe` 107, `methode` 109, `cat-admin` 111, `cat-cabaret` 111, `regles` 113, `premier-pas` 113, `cat-finance` 116, `avancees` 118, `crm` 122, `robotique` 131, `logiciels` 132, `administratrice` 138, `trajectoire` 160.

Même avec le plafond de 80 mots réservé aux tableaux, les six `cat-*` et `regles` dépassent : chaque fiche d'annexe est à resserrer (une ligne par aide, huit mots au plus par ligne).

**Notes de plus de 80 mots** (8) : `regles` 150, `avancees` 124, `robotique` 118, `trajectoire` 103, `methode` 97, `etapes` 93, `administratrice` 85, `crm` 81.

**Mots à remplacer** (règle 1 du brief) : « CRM » (fichier de contacts), « RGPD » (règles sur les données personnelles), « QR codes », « Zoom · » en surtitre, « pilote » sans explication (dire « essai de huit semaines »), « Marketing » (communication), « administratrice centrale » dans `compris` (dire « votre administratrice »).

## Ce que seuls Morgan, Mathys ou GianLuca peuvent trancher

Morgan et Mathys :

1. Le prix du cadrage dès la diapositive 1 (recommandé ici) ou seulement à la diapositive 15.
2. Les prix de la suite du logiciel (15 700 à 18 700 € HT jusqu'au bilan du pilote) : montrés en annexe A8, ou seulement dits s'il les demande. Ils restent à valider.
3. Les deux maquettes : qui les construit, pour quand, et avec quels noms fictifs.
4. Ce qu'on dit, ou non, des dossiers de création déjà remis et du prototype de CRM ; et si l'information sur l'incident de données part avant le rendez-vous, par un message écrit relu par l'avocat.
5. Ce qui s'écrit de vrai sur le parcours de chacun, qui est l'interlocuteur habituel, qui signe pour Marwin Tech.
6. Le contenu d'une réponse « oui, à ajuster » : une version réduite du cadrage est déjà prévue en interne (**Rendez-vous**, section 8, réponse à « C'est trop cher » ; **Commerciale**, section 3.2). Reste-t-elle valable après les faits du 9 novembre, et la dit-on seulement s'il la demande ? Son prix ne s'affiche pas à l'écran.
7. Les notes de l'orateur : gardées (réécrites, 80 mots au plus) ou vidées avant tout partage du lien.
8. La grille de seize critères remise sans condition, même s'il dit non.
9. Les dates de la frise (diapositive 17) et la date du rendez-vous.

GianLuca Carlone :

1. Lequel des trois sens de « logiciel de gestion de propriété » compte pour lui, et dans quel ordre.
2. Ses trois priorités pour les trois prochains mois.
3. Le rôle et les pouvoirs de son administratrice, et sa présence au rendez-vous.
4. La société qui signerait le bon de commande.
5. Sa réponse : oui, à ajuster, ou non.
