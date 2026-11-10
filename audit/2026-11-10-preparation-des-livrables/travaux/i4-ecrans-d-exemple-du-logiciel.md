# Livrable 4 — Des écrans d’exemple du logiciel de gestion des propriétés, en données fictives — inventaire avant rédaction

Note de travail interne du 10 novembre 2026

Document interne — ne pas transmettre à GianLuca Carlone. Ce document n’est pas un avis juridique, fiscal ou d’assurance. Les chemins sont relatifs à la racine du dépôt. « Annexe » désigne `pour-carlone/logiciels-et-automatisations/2026-11-09-annexe-specification-logiciel-gestion-proprietes.md`. « Proposition » désigne `pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md`.

**En bref.** Les quatre écrans demandés sont déjà décrits, rubrique par rubrique, dans l’annexe du 9 novembre. La maquette les illustre ; elle n’invente aucune fonction. Le dépôt ne contient encore aucun écran dessiné du logiciel : seulement un gabarit de diapositive et des listes de rubriques. Le point le plus sensible : rien n’est construit, et l’étape « Maquette et essai sur données fictives » est une étape payante prévue en 2027. Les écrans d’exemple sont un avant-goût, pas cette étape.

## 1. Ce qui existe déjà

### 1.1 Les règles qui s’imposent à toute maquette

- `audit/2026-11-09-audit-presentation-et-offre/travaux/BRIEF.md`, l. 58 (§ 5, règle 2) : « Une maquette porte la mention « Maquette — données fictives ». » Réutilisable tel quel : c’est le libellé exact à écrire sur chaque écran.
- Même fichier, l. 60 à 62 (règles 4 à 6) : ni montant des bâtiments, ni codes de l’audit, ni prix plancher ; « Rien n’est envoyé, payé, signé ou supprimé sans la validation d’une personne habilitée » ; « L’administratrice est aidée, jamais remplacée ni surveillée ».
- Même fichier, l. 94 à 98 (additif) : jamais le nom ni le prix de l’autre prestataire. Phrase d’entrée : « Vous nous avez demandé si nous pouvions créer votre logiciel de gestion de vos propriétés. Voici comment nous le ferions. » Prix : « Seul le cadrage (6 500 € HT, 7 800 € TTC) est affiché ».
- `audit/2026-11-10-preparation-des-livrables/travaux/BRIEF-2.md`, l. 37 : emplacement prévu du livrable : `pour-carlone/maquettes/2026-11-10-ecrans-d-exemple/`, avec `index.html` (« maquette cliquable, un seul fichier »), `LISEZ-MOI.md` et les images des écrans ; lecteur : « client, seulement après décision des deux associés ».
- Même fichier, l. 66 à 75 (§ 5) : première ligne sous le titre d’un document client : « PROJET non envoyé — à valider par Morgan Olsen et Mathys Couet » ; aucune coordonnée réelle ; typographie française ; et la règle 10 : « toute maquette, tout exemple chiffré inventé porte « Maquette — données fictives » ou « Exemple fictif ». Les noms sont manifestement inventés (« Bâtiment A », « Entreprise 1 ») et ne ressemblent à aucun bien réel. »

### 1.2 Le gabarit de diapositive « maquette d’écran »

- Gabarits de la présentation v12 (copie de travail hors dépôt), `GABARITS.md`, l. 7 à 25 : une diapositive est une seule balise `section` de 1 920 × 1 080 px, sans texte sous 24 px. L. 32 : pastilles d’état d’une maquette : vert `#3F6B4F`, rouge brique `#8A3B2E`, bronze `#7E5F31`. L. 38 : 120 mots visibles au plus. L. 53 : gabarit `maquette-ecran` : « Texte court à gauche, fenêtre d’écran à droite (cinq lignes au plus), mention « Maquette — données fictives » obligatoire ».
- Même dossier, `project/slides/g-maquette.html` (52 lignes) : exemple testé. À gauche, une phrase en gras et trois puces (« Un bénéfice concret », « Qui valide quoi », « Ce qui reste à lui »). À droite, une fenêtre de cinq lignes à trois colonnes (libellé, détail, pastille « Dans 12 jours », « À valider », « À jour »), puis la mention. Réutilisable tel quel pour les images de la présentation.
- Limite : cinq lignes et trois colonnes. Une grille de trois devis ou une fiche complète n’y tient pas. Il faut un écran par diapositive, réduit à l’essentiel.

### 1.3 Les écrans déjà décrits dans l’annexe (la source qui fait foi)

L’annexe est un document client, en lecture seule. Chaque écran de la maquette doit pouvoir se rattacher à l’une de ces lignes.

- **Fiche bâtiment** — annexe, l. 131 à 157 (module 1, Patrimoine). L. 135 : « Fiche bâtiment : identité, adresse, références cadastrales, société propriétaire, date d’acquisition, surfaces, usages, établissement recevant du public (ERP) ou non, lots, plans, diagnostics, assurances, échéances, travaux en cours. » L. 138 : « Tableau des diagnostics et des assurances : type, date, fin de validité, prochaine action. » L. 154 (critère 1) : un champ est rempli « ou marqué « inconnu » avec une personne chargée de le compléter ». Liste réutilisable telle quelle. Le champ « inconnu » est à montrer.
- **Trois devis comparés** — annexe, l. 220 : « Comparaison des devis : grille commune, postes manquants et écarts signalés. » L. 236 : niveau « Assistée » ; garde-fou : « Vérifiée par une personne ; le choix revient à vous ou à votre administratrice ». L. 238 : l’acceptation d’un devis est « Préparée pour signature », « Dans les budgets validés (module 6) ». L. 252 (critère 4) : « Sur trois devis comparés pendant le pilote, chaque poste chiffré se retrouve dans la grille, contrôle fait par votre administratrice. » C’est de là que vient le chiffre « trois ».
- **Échéancier** — annexe, l. 291 : « Calendrier des échéances : vue par liste, par mois, par société, par personne chargée. » L. 294 : types d’échéances (contrats, assurances, baux, diagnostics, autorisations). L. 301 : rappels « par défaut deux mois, un mois et une semaine avant, réglables », « Aux utilisateurs de l’outil seulement ; jamais à une personne extérieure ». L. 310 : « Une échéance sans personne chargée est signalée ».
- **Tableau de bord** — annexe, l. 350 à 373 (module 7). L. 353 : « Vue d’ensemble, par société : budget et réel, trésorerie prévue, loyers attendus et encaissés, échéances proches, décisions en attente, incidents ouverts. » L. 355 : « Liste « à décider » : décisions et validations attendues, avec leur date limite. » L. 364 : « chaque chiffre mène à sa source ». L. 371 : indicateurs « choisis et validés par écrit par vous avant d’être construits : douze au plus par vue ».
- **Export** — annexe, l. 492 à 496 : « Vous ou votre administratrice lancez l’export vous-mêmes, sans nous le demander. » Contenu : « toutes les données en formats ouverts (CSV et JSON), avec la description de chaque champ ; tous les documents d’origine ; le journal des actions ; les réglages des automatisations et les modèles de documents. » Proposition, l. 93 : même promesse. C’est la base du bouton « Exporter » de la fiche bâtiment.
- **Rôles** — annexe, l. 87 à 107 : cinq rôles, dont l’administratrice, « utilisatrice principale » (l. 90). Utile pour le bandeau « connecté en tant que », sans nom de personne.
- **Niveaux d’aide** — annexe, l. 73 à 79 : « Automatique après essai », « Assistée », « Préparée pour signature ». L. 79 : « Jamais automatique, même après essai : un envoi à une personne extérieure à vos sociétés, une publication, une commande, un paiement, une signature, une suppression, un changement de droits d’accès. »
- **Mots interdits à l’écran** — annexe, l. 244 : « L’outil ne dit jamais qu’un lieu est « conforme ». […] L’outil dit ce qui est fait, ce qui manque et ce qui arrive. » L. 34 : « L’intelligence artificielle (IA) ne calcule jamais un montant. » L. 583 à 594 : ce que le logiciel ne fait pas (il n’encaisse rien, ne paie rien, ne décide pas).
- **Modèle de données** — annexe, l. 451 à 468 : une société possède un bâtiment, qui contient des lots, occupés par un lieu. Le jeu de données fictives respecte ces liens.

### 1.4 Ce que les pièces promettent, étape par étape

- Annexe, l. 600 à 607 : quatre étapes, chacune commandée à part. L. 605, étape 2 : « Maquette cliquable : écrans des modules retenus, sans vrais calculs, pour vérifier l’usage avant de construire ; essais par votre administratrice. » « Données fictives seulement ». Conditions de fin : dix scénarios réalisés sans aide, « vous validez par écrit les écrans », export testé sur les données fictives.
- Proposition, l. 77 à 86 : calendrier. Cadrage en janvier 2027 ; maquette et essai en février et mars 2027 (« Écrans de l’outil commun ») ; pilote de mi-mars à mi-mai 2027 ; bilan mi-mai ; mise en service de juin 2027 à janvier 2028 (« tableau de bord et assistant »). L. 110 : maquette et essai, 5 300 € HT.
- Proposition, l. 37 : « Le pilote couvre un bâtiment et un lieu. Les finances, le tableau de bord complet, l’assistant et vos autres bâtiments et lieux viennent ensuite, seulement si vous les commandez ». C’est la phrase qui borne ce que la maquette peut montrer sans avertissement.
- `pour-carlone/logiciels-et-automatisations/2026-11-09-logiciels-sur-mesure-methode-et-garanties.md`, l. 34 : même promesse : « Les écrans, sans vraies données, avant tout code ».
- `interne/logiciels-et-automatisations/2026-11-09-etude-gestion-proprietes-offre-accord-et-prix.md`, l. 328 : contenu interne du lot payant : « Maquette cliquable de la couche commune (fiches, échéances, registre, tableau) ». Les quatre écrans demandés recouvrent donc presque tout ce lot.

### 1.5 Ce que les audits et les notes ont déjà écrit sur une maquette

- `audit/2026-11-09-audit-presentation-et-offre/travaux/a1-point-de-vue-gianluca.md`, l. 258 à 284 : deux démonstrations déjà scénarisées. L. 271 : trois devis fictifs « pour la même réfection de toiture d’un immeuble fictif », avec « une erreur placée exprès, et annoncée ». L. 279 : fiche d’un bâtiment fictif, échéances des 90 prochains jours pour trois bâtiments, puis « le bouton d’export : un tableur s’ouvre, sans Marwin Tech ». L. 283 : « Ce sont deux écrans de maquette, pas l’outil. » L. 284 : rester « en deçà » de l’étape payante.
- `…/travaux/a4-offre-et-documents-clients.md`, l. 281 à 284 et l. 500 : on ne dit pas « démonstration gratuite » ; une maquette au rendez-vous coûte « une demi-journée à une journée non payée » et « contredit le gel de toute production non commandée ». « Morgan et Mathys seuls peuvent lever ce gel, pour cet objet et ce temps-là, par écrit. »
- `…/01-audit-de-la-presentation.md`, l. 318 (décision 15) et `…/03-objections-et-conditions-d-acceptation.md`, l. 106 : « Au plus une maquette fixe », « Aucune démonstration en direct ». L. 77 du même fichier 03 : phrase prête pour « Qui sont vos clients ? » : « Nous n’avons pas encore d’outil en service chez un client ».
- `audit/2026-11-04-audit-strategique/annexes/travaux/strategie-retenue.md`, l. 716 : « arrêter immédiatement toute production non commandée ». Étude interne, l. 658 (DL1) : « aucune production, avant sa proposition écrite (ou son résumé) ».
- `audit/2026-11-10-preparation-des-livrables/travaux/k6-logiciels-gestion-patrimoine-ecrans.md`, l. 135 à 142 : recommandations d’écran (états en mots avec une date ; « À décider » en haut du tableau de bord ; une colonne par entreprise, une ligne par poste). L. 146 : phrase d’orateur « Ce sont des exemples dessinés pour vous. Rien n’est encore construit. » Cette note n’a pas de section « Vérification du 10 novembre 2026 » : ses points « à confirmer » ne vont pas à l’écran.
- `…/travaux/k8-registre-des-batiments.md`, l. 164 : libellés d’échéances réalistes pour la maquette ; l’amiante s’affiche « sans date de fin — à tenir à jour », pas « valide ».
- `…/travaux/k5-rendez-vous-de-decision.md`, l. 130 : une maquette montrée comme un produit existant « tromperait sur l’existence du service ». `…/travaux/k1b-clauses-contrat-court.md`, l. 192 : « Les écrans ne sont cédés que si le bon de commande les nomme. »
- `audit/2026-11-09-audit-presentation-et-offre/travaux/p0-diapositives-proposees-logiciels.md`, l. 13 à 15 et l. 39 : textes courts déjà écrits pour la colonne de gauche des diapositives.

## 2. Décisions prises et décisions ouvertes qui conditionnent ce livrable

**Prises.**

- La mention « Maquette — données fictives » figure sur chaque écran (BRIEF, l. 58 ; BRIEF-2, règle 10).
- Le dossier, les trois pièces (`index.html`, `LISEZ-MOI.md`, images) et le lecteur sont fixés (BRIEF-2, l. 37).
- La voie retenue : logiciels du marché reliés par un outil commun, par étapes (BRIEF, l. 51).
- Un seul prix peut paraître : celui du cadrage (BRIEF, l. 98). La maquette n’en affiche aucun.
- Jamais sur mesure : caisse, billetterie, logiciel hôtelier, facturation électronique, comptabilité, paiement (BRIEF, l. 97). Aucun écran ne les simule.

**Ouvertes.**

- **Montrer ou non.** Le BRIEF-2 commande la préparation. Il ne dit pas que le gel est levé. Montrer les écrans exige une décision écrite des deux associés, « pour cet objet et ce temps-là » (a4, l. 284).
- **Combien d’écrans en séance.** Les audits disent « au plus une maquette fixe » (fichier 01, l. 318). La note a1 en prévoit deux. Le BUT en demande quatre.
- **Images seules ou maquette cliquable.** La note k6 (l. 136 et l. 152) recommande les images seules et renvoie le choix aux associés.
- **Le tableau de bord.** Il relève de la dernière étape. Le montrer, ou non, reste à trancher.
- **Les modules retenus.** Le cadrage les choisit. L’annexe (l. 650) suggère de commencer par les modules 5 et 1.
- **Laisser la maquette.** La note a1 (l. 248) écrit « On lui laisse la maquette vue ». Rien n’est décidé. La cession suppose un bon de commande (k1b, l. 192).

## 3. Contradictions et écarts entre les pièces (chiffres, dates, durées, formulations) — avec la version à retenir et pourquoi

1. **Images ou maquette cliquable.** k6, l. 136 : « Quatre images fixes, pas de maquette cliquable. » BRIEF-2, l. 37 : `index.html` cliquable. **À retenir** : le BRIEF-2, qui commande. Les images vont dans la présentation. Le fichier cliquable reste interne jusqu’à décision. La mise en garde de k6 justifie ce verrou.
2. **Nombre d’écrans.** Un (fichier 01), deux (a1), quatre (BUT). **À retenir** : quatre écrans préparés ; le nombre montré est une décision des associés. Par défaut, deux en séance : fiche bâtiment et trois devis.
3. **Tableau de bord.** L’étude interne (l. 328) le met dans la maquette payante. La proposition (l. 37 et l. 114) place « le tableau de bord complet » après le pilote. **À retenir** : la proposition, document client. L’écran porte un bandeau « Étape ultérieure, commandée à part ».
4. **« Première étape ».** Le cadrage (annexe, l. 604) ; ou maquette et pilote « jusqu’au bilan » (proposition, l. 112). **À retenir** dans la maquette : ne pas écrire « première étape ». Écrire « pendant le pilote » ou « après le bilan ».
5. **Le mot « maquette ».** Il désigne déjà l’étape payante de 2027 (5 300 € HT). **À retenir** : « écrans d’exemple » dans les titres et à l’oral ; « Maquette — données fictives » comme mention seulement.
6. **« Essai ».** Quatre sens relevés (a4, l. 118). **À retenir** : « essai sur données fictives », puis « pilote sur un bâtiment et un lieu ».
7. **Rappels.** Annexe, l. 301 : deux mois, un mois, une semaine. Gabarit : « Dans 12 jours », « Dans 45 jours ». **À retenir** : l’annexe. Les dates fictives s’y accordent.
8. **Noms fictifs.** a1 : entreprises « A », « B », « C ». BRIEF-2 : « Entreprise 1 ». **À retenir** : le BRIEF-2, plus récent. Lettres pour les bâtiments, chiffres pour les entreprises.
9. **Taille de la grille.** k6 (l. 141) liste neuf lignes fixes pour les devis. Le gabarit en porte cinq. **À retenir** : cinq lignes sur la diapositive ; la grille entière dans `index.html`.
10. **Assurance.** La proposition (l. 99) annonce une attestation. Le BRIEF-2 (règle 5) interdit de la promettre. **À retenir** : le `LISEZ-MOI.md` n’en parle pas.

## 4. Règles et lignes rouges propres à ce livrable (issues du BRIEF et des audits)

- La mention est écrite dans l’image elle-même, sur chaque écran (a3, l. 298).
- Rien de réel : ni nom, ni adresse, ni société, ni œuvre. Rien qui évoque un ancien hôtel, une galerie, un cabaret ou une ville de bord de fleuve.
- Aucun prix de Marwin Tech, aucune valeur de bâtiment, aucun nom d’autre prestataire.
- Jamais « conforme », « valide », « garanti », « accessible », ni un taux de TVA (annexe, l. 244 ; k6, l. 158 à 167).
- Aucun bouton qui envoie, paie, signe ou supprime. L’IA ne calcule pas et ne choisit pas.
- Aucun nom de personne : des rôles seulement. Aucune coordonnée.
- Un état n’est jamais donné par la couleur seule : toujours un mot et une date.
- On ne dit ni « démonstration gratuite », ni « le logiciel fait déjà ».
- Le `LISEZ-MOI.md` commence par « PROJET non envoyé — à valider par Morgan Olsen et Mathys Couet ».

## 5. Plan détaillé proposé du ou des livrables (titres, blocs, longueur, format de fichier, document client ou interne)

Dossier : `pour-carlone/maquettes/2026-11-10-ecrans-d-exemple/` (à créer ; il n’existe pas).

**A. `LISEZ-MOI.md`** — projet de document client, 300 mots au plus. Titres : « Ce que vous voyez » ; « Ce que ce n’est pas encore » ; « Les quatre écrans » ; « Ce qui vient à quelle étape » ; « Des données inventées ».

**B. Quatre images** (1 920 × 1 080) et quatre diapositives au gabarit `maquette-ecran` : cinq lignes, 120 mots au plus. Pied possible : « Exemple d’écran. Le logiciel n’existe pas encore. » (k6, l. 136).

**C. `index.html`** — interne jusqu’à décision. Un seul fichier, sans appel au réseau. Bandeau fixe « Maquette — données fictives ». Rôle affiché : « Administratrice (exemple) ».

| Écran | Rubriques | Ce qu’il doit prouver | Étape |
|---|---|---|---|
| 1. Fiche bâtiment | Identité, société propriétaire, lots, diagnostics et assurances (type, date, fin de validité, prochaine action), un champ « inconnu — à compléter par… », bouton « Exporter » | Tout sur un bâtiment au même endroit. L’inconnu est dit. Vous repartez avec vos données sans nous | Pilote |
| 2. Échéancier | Échéance, bâtiment, société, personne chargée, état en mots ; une ligne « sans personne chargée » signalée | Aucune échéance oubliée ; chacun sait ce qui lui revient | Pilote, pour un bâtiment et un lieu |
| 3. Trois devis comparés | Une colonne par entreprise ; périmètre, postes non chiffrés, total HT, délai, durée de validité ; écarts signalés ; pied « L’outil signale les écarts. Il ne choisit pas. » | L’outil prépare, une personne décide | Pilote, si le module 3 est retenu |
| 4. Tableau de bord | « À décider » en haut, avec date limite ; échéances proches ; incidents ouverts ; douze indicateurs au plus | Une vue de toutes les sociétés, chaque chiffre menant à sa source | Après le bilan : bandeau « Étape ultérieure, commandée à part » |

**Jeu de données fictives proposé.**

- Sociétés : « Société Exemple 1 » (propriétaire), « Société Exemple 2 » (exploitante).
- Bâtiments : « Bâtiment A — 1, rue de l’Exemple », « Bâtiment B — 2, rue du Modèle », « Bâtiment C — 3, place de l’Essai », à « Ville-Exemple », code postal 00000.
- Lots A1 (commerce), A2 (bureau), A3 (logement). « Lieu 1 » occupe le lot A1.
- Devis : « Réfection de la toiture du bâtiment A ». Entreprise 1 : 40 000 € HT. Entreprise 2 : 45 000 € HT, un poste non chiffré. Entreprise 3 : 50 000 € HT, délai non indiqué.
- Date fictive du jour : 1er mars 2027. Échéances à une semaine, un mois et deux mois. Une échéance « En retard de 12 jours ». Une autre « Fait le 15 février 2027 ».

**Ce que la spécification promet, étape par étape.**

| Étape | Promesse | Conséquence pour la maquette |
|---|---|---|
| 1. Cadrage (janvier 2027) | Choix des modules et des logiciels | Aucun écran promis. Le texte dit : « les écrans définitifs seront décidés avec vous » |
| 2. Maquette et essai (février et mars 2027) | Écrans des modules retenus, sans vrais calculs, essayés par l’administratrice | Les écrans d’exemple en sont un avant-goût, pas un acompte |
| 3. Pilote (mi-mars à mi-mai 2027) | Un bâtiment et un lieu ; export complet | Écrans 1 à 3, limités au bâtiment A et au lieu 1 |
| 4. Mise en service (juin 2027 à janvier 2028) | Finances, tableau de bord complet, assistant, autres bâtiments | Écran 4 et toute vue de plusieurs bâtiments : bandeau obligatoire |

Hors maquette : loyers, quittances, finances, assistant, hôtellerie, caisse.

## 6. Connaissances manquantes (questions de recherche précises, par ordre d’importance)

1. La mention suffit-elle à écarter le reproche de présentation trompeuse, quand le client est une société ? Le texte cité par k5 (l. 130) est à confirmer ; la question relève d’un avocat.
2. Que doit contenir un devis de travaux remis à une société ? Les lignes de la grille en dépendent (k6, l. 99 à 113 : « à confirmer »).
3. Quelles durées de validité afficher pour les diagnostics d’exemple, sans écrire une règle fausse (k8) ?
4. Les trois couleurs de pastille atteignent-elles un contraste de 4,5 pour 1 sur le fond de carte ? À calculer.
5. L’outil de présentation accepte-t-il une image d’écran ? Aucun des trois identifiants d’image fournis n’en est une. Sinon, les écrans sont écrits en diapositives.
6. Sur quel appareil la présentation sera-t-elle montrée, avec ou sans réseau ? Inconnu.

## 7. Questions pour Morgan (non bloquantes ; pour chacune, l’hypothèse par défaut si la réponse ne vient pas)

1. Les deux associés lèvent-ils par écrit le gel pour cet objet, avec un temps plafonné ? *Par défaut : on prépare, on ne montre rien.*
2. Combien d’écrans en séance ? *Par défaut : deux (fiche bâtiment, trois devis) ; les autres en réserve.*
3. Le tableau de bord est-il montré ? *Par défaut : en réserve, avec son bandeau.*
4. Le fichier cliquable est-il montré ? *Par défaut : non ; des images seulement.*
5. Laisse-t-on les images après le rendez-vous ? *Par défaut : non.*
6. L’administratrice sera-t-elle présente, et prend-elle la main ? *Par défaut : inconnu ; l’un des deux associés présente.*

## 8. Risques si ce livrable est mal fait

- GianLuca Carlone croit que le logiciel existe (« c’est donc prêt ? »). La confiance tombe au premier retard.
- L’étape payante de 2027 paraît déjà faite : son prix ne se défend plus.
- Une donnée inventée ressemble à l’un de ses biens : il pense que ses données ont servi.
- Un écran montre une fonction d’une étape ultérieure, sans le dire : il l’attendra dès le pilote.
- Un mot de droit (« conforme », « valide ») engage Marwin Tech.
- Un texte trop petit ou une grille trop dense : illisible en séance.
- Du temps non payé, passé sans décision écrite, contre la règle de l’audit stratégique (aucune production non commandée).
