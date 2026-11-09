# Audit de la présentation v11 et de l'offre

**9 novembre 2026 — document interne — ne pas transmettre à GianLuca Carlone.**

Pour Morgan Olsen et Mathys Couet. Synthèse des cinq notes d'audit et des trois notes de recherche du dossier `audit/2026-11-09-audit-presentation-et-offre/travaux/`. Rien n'a été envoyé, modifié ni publié pour écrire ce document.

## Comment lire les sources

Chaque affirmation renvoie à sa source, entre parenthèses. Les chemins partent de la racine du dépôt.

| Abréviation | Fichier |
| --- | --- |
| BRIEF | `audit/2026-11-09-audit-presentation-et-offre/travaux/BRIEF.md` |
| a1 | `audit/2026-11-09-audit-presentation-et-offre/travaux/a1-point-de-vue-gianluca.md` |
| a2 | `audit/2026-11-09-audit-presentation-et-offre/travaux/a2-recit-et-persuasion.md` |
| a3 | `audit/2026-11-09-audit-presentation-et-offre/travaux/a3-exactitude-et-engagements.md` |
| a4 | `audit/2026-11-09-audit-presentation-et-offre/travaux/a4-offre-et-documents-clients.md` |
| a5 | `audit/2026-11-09-audit-presentation-et-offre/travaux/a5-forme-et-lisibilite.md` |
| r1, r2, r3 | `audit/2026-11-09-audit-presentation-et-offre/travaux/r1-nouveautes-ia-automatisation-2026.md`, `r2-applications-par-metier.md`, `r3-avenir-1-a-5-ans.md` |
| p0 | `audit/2026-11-09-audit-presentation-et-offre/travaux/p0-diapositives-proposees-logiciels.md` |
| v11, `id` | `pour-carlone/presentation-ia/2026-11-09-version-11/project/slides/<id>.html` (26 diapositives ; le texte de la balise `<aside>` est la note de l'orateur) |
| CADRAGE:n | `audit/2026-11-04-audit-strategique/pour-gianluca/2026-11-09-proposition-de-cadrage.md`, ligne n |
| LOGICIEL | `pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md` |
| FICHES | `pour-carlone/logiciels-et-automatisations/2026-11-09-automatisations-fiches-detaillees.md` |
| GARANTIES | `pour-carlone/logiciels-et-automatisations/2026-11-09-logiciels-sur-mesure-methode-et-garanties.md` |
| MAJ:n | `audit/2026-11-04-audit-strategique/interne/2026-11-09-mise-a-jour-faits-nouveaux.md`, ligne n |
| STRATÉGIE | `audit/2026-11-04-audit-strategique/annexes/travaux/strategie-retenue.md` |
| Rendez-vous | `audit/2026-11-04-audit-strategique/interne/13-preparation-rendez-vous.md` |
| Étude prix | `interne/logiciels-et-automatisations/2026-11-09-etude-gestion-proprietes-offre-accord-et-prix.md` (décisions DL1 à DL13) |

**Trois réserves sur les sources.**

1. r3 a reçu sa partie « Vérification du 9 novembre 2026 » et sa liste « sûr pour une diapositive » (douze phrases) pendant l'écriture de ce document. Seules ces douze phrases peuvent aller dans un texte montré au client, chacune avec sa source en note. Le reste de r3 sert ici seulement à cadrer ce qu'il ne faut pas annoncer (r3, « À ne pas reprendre sur une diapositive »).
2. Aucune parole directe de GianLuca Carlone n'est dans le dépôt (MAJ:348). Ce que nous savons de ses projets vient de Morgan (BRIEF § 2).
3. L'autre offre est connue par une seule déclaration : le groupe Accor, d'après Morgan Olsen, 9 novembre 2026. Aucune pièce écrite n'a été vue (BRIEF, additif). L'étude interne des prix écrit ce nom autrement (« Accord ») : le nom lui-même n'est pas vérifié.

---

## Conclusion en cinq lignes

1. **La v11 est honnête, mais c'est un exposé, pas une proposition.** Aucun prix, aucune date, aucune demande : GianLuca Carlone ne peut pas dire oui (a1 § 6 ; a2 § 1 ; a4 § 1).
2. **Elle ne répond pas à sa demande.** Il a demandé un outil pour gérer ses propriétés ; la v11 n'en parle pas pour lui et le promet à d'autres (BRIEF, additif ; v11, `logiciels` et `pour-dautres` ; a1 § 1).
3. **Elle ne peut pas partir aujourd'hui.** 14 affirmations à retirer, 67 à nuancer, 19 à prouver ; trois préalables non levés. Au plus tôt jeudi 19 novembre 2026 (a3 § 1 et § 7 ; MAJ:20).
4. **L'offre est bonne, mais elle n'est pas en état d'être acceptée.** Pas de bon de commande, pas de conditions, une proposition mêlée à sa note interne, 23 incohérences entre documents (a4 § 2.2 et § 3).
5. **La refonte tient en trois gestes** : 18 à 21 diapositives et 8 annexes au plus ; le prix du cadrage et une seule décision à l'écran ; trois décisions prises à deux avant tout (séparer le texte client de la note interne, nommer le signataire, trancher DL1) (a2 § 6 ; a5 ; a4 § 10).

---

## Les dix constats qui comptent

Du plus grave au moins grave.

### 1. Rien ne peut partir : trois préalables ne sont pas levés

- **Constat.** La règle interne interdit tout envoi, présentation comprise, avant le traitement de l'incident de données (D03, D08) et l'accord écrit des deux associés.
- **Preuve.** MAJ:20 : « Rien ne part au client, présentation comprise, avant D03, D08 et l'accord écrit des deux associés ». MAJ:65 : échéance du 5 novembre passée, décision inconnue. MAJ:240 : la présentation est signée des deux noms (v11, `echange`), l'accord de Mathys n'est pas établi (U07). Les notes de l'orateur sont lisibles par toute personne qui ouvre le lien (`pour-carlone/presentation-ia/README.md`) ; qui a déjà vu la présentation n'est pas établi (D45 ; a3 § 7.1).
- **Conséquence pour sa décision.** S'il apprend après coup un sujet qui touche à la confiance, c'est l'un des signaux d'un non (a1 § 4). La phrase « Vos données ne servent jamais à d'autres » (v11, `pour-dautres`) est fragile tant que l'incident n'est pas traité (a3 § 3, E36).
- **Correction.** Dans l'ordre : décision sur D03 ; information de GianLuca Carlone par un texte validé par un conseil (D08, échéance interne jeudi 19 novembre 2026) ; accord écrit de Mathys ; lien gardé privé et liste écrite de ceux qui l'ont vu avant vendredi 13 novembre 2026 ; notes de l'orateur vidées ou réécrites (a3 § 7.1 et § 7.5).

### 2. La présentation ne demande rien

- **Constat.** Aucun « € », aucune date, aucune question de décision. L'offre arrive après 23 diapositives.
- **Preuve.** v11, `cover` : « document de présentation, sans engagement ». v11, `premier-pas` : « La proposition chiffrée vous est remise à part. » v11, `echange` : quatre questions ouvertes, aucune sur la commande. a2 § 2 : 91 % du texte avant `etapes` ; la décision occupe 3 diapositives et 9 % des mots. a4 § 1, ce qu'il retiendrait : « Je ne sais pas combien il coûte, ni quand il commence. […] On ne m'a rien demandé de décider. »
- **Conséquence pour sa décision.** Il décide vite quand il voit du concret (BRIEF § 2). Sans prix ni question, la seule réponse possible est « je vais réfléchir » (a1 § 4).
- **Correction.** Deux diapositives nouvelles : l'offre chiffrée et la décision (a4 § 9). À l'écran, le prix du cadrage et lui seul : « 6 500 € hors taxes, soit 7 800 € toutes taxes comprises. Prix fixe, déplacements des deux rendez-vous compris. Moitié à la commande, moitié à la remise du dossier. » (a4 § 7). Une seule question : « Commandez-vous le cadrage ? », trois réponses possibles (a4 § 4 ; a2 § 4.4).

### 3. Sa demande reste sans réponse

- **Constat.** Il a demandé à Marwin Tech si elle pouvait créer un outil de gestion de ses propriétés (BRIEF, additif). La v11 ne lui répond pas, et annonce ces logiciels pour d'autres clients.
- **Preuve.** v11, `logiciels` : surtitre « Zoom · Logiciels sur mesure », alors que LOGICIEL, ligne 56, écrit du sur mesure complet : « Nous ne le proposons pas. » (a3 § 1, n° 82). v11, `pour-dautres` : « Des logiciels de gestion des lieux et des bâtiments », et « Galeries et marchands d'art » parmi les futurs clients, c'est-à-dire ses concurrents (a1 § 1).
- **Conséquence pour sa décision.** Il a une autre proposition sur la table. S'il ne voit pas son sujet, il compare un exposé à une offre. Il peut aussi croire qu'il finance un produit vendu ensuite à d'autres (a1 § 4).
- **Correction.** Remplacer `logiciels` par la diapositive « Un outil commun pour vos bâtiments et vos lieux » (p0, `proprietes`). Dire la phrase de liaison : « Votre logiciel de gestion des propriétés est l'une des priorités que le cadrage peut préparer. Si vous la retenez, il se construit ensuite par étapes, chacune commandée à part. » (a4 § 5). Montrer la grille neutre de comparaison (LOGICIEL § 8). Aucune promesse « mieux et moins cher » ; ne nommer ni l'autre prestataire ni son prix (BRIEF, additif et règle 3).

### 4. Quatorze affirmations contredisent nos propres règles

- **Constat.** Sur 143 affirmations relevées : 43 exactes, 67 à nuancer, 14 à retirer, 19 à prouver. Trois règles sur douze sont respectées sans réserve (3, 4 et 12) (a3 § 1 et § 2).
- **Preuve.** v11, `avancees` : « elle remplit des tableaux, prépare des dossiers et envoie, après validation » contredit la règle 5. v11, `modes` : « L'IA rédige, trie ou calcule » contredit FICHES, ligne 64 : « L'IA ne calcule jamais un montant. » v11, `cat-admin` : « Relances » et « paiements » sous l'étiquette Automatique. v11, `societe` (note) et `pour-dautres` : « garantie », « garantit » (règle 2). Liste complète plus bas.
- **Conséquence pour sa décision.** Une seule phrase fausse relevée par son administratrice, son expert-comptable ou son conseil suffit à faire douter de tout le reste.
- **Correction.** Retirer les 14 ; réécrire avec les formulations sûres d'a3 § 5 et les phrases « sûr pour une diapositive » de r1 et r2, sans rien y ajouter.

### 5. La proposition écrite n'est pas en état d'être remise

- **Constat.** La v11 annonce une proposition « remise à part ». Cette pièce n'est pas prête, et il n'existe ni bon de commande ni conditions.
- **Preuve.** CADRAGE:186 : la « Note interne — à retirer avant envoi » est dans le même fichier que le texte client, avec le prix plancher et la version réduite (a4 § 2.2, n° 23). CADRAGE:27 nomme un tiers, « un centre d'appels (Quali Contact) » (a4 § 2.2, n° 20). CADRAGE:104 écrit « relues par notre avocat » : ce n'est pas fait (a3 § 7.3). Deux versions du fichier coexistent dans `audit/2026-11-04-audit-strategique/pour-gianluca/` (a4 § 10, décision 2). Aucun bon de commande ni conditions trouvés dans le dépôt (a4, Limites). Environ 33 850 mots de documents clients, tous « PROJET non envoyé » (a4 § 3).
- **Conséquence pour sa décision.** Même s'il dit oui, il n'a rien à signer. Si le fichier part tel quel, il lit notre prix plancher.
- **Correction.** Un fichier client séparé (CADRAGE, lignes 15 à 182), une page d'offre d'environ 510 mots (a4 § 8), un bon de commande d'une page et ses conditions, relus par un avocat (a4 § 6 et § 10).

### 6. Les prix ne tiennent pas ensemble

- **Constat.** Seul le prix du cadrage est validé. Les autres montants existent dans les documents clients, mais une décision interne interdit de les donner, et le total n'est écrit nulle part.
- **Preuve.** Étude prix, DL1 : « Aucune contre-offre, aucun chiffre donné à GianLuca sur ce logiciel, aucune production » avant sa proposition écrite et avant D03 et D08. LOGICIEL § 7 porte pourtant une quinzaine de montants, et BRIEF § 4 cite « 15 700 à 18 700 € HT » jusqu'au bilan du pilote (a4 § 3, frein bloquant n° 5). Le total cadrage compris, 22 200 à 25 200 € HT, n'est dans aucun document (a4 § 2.2, n° 1). « 6 500 € » désigne deux choses ; deux règles d'acompte ; deux délais pour le solde ; trois ancrages sur trois ans (a4 § 2.2, n° 2, 4, 5, 6).
- **Conséquence pour sa décision.** Sa question « et mon logiciel, combien ? » est certaine (a1 § 3, objection 7). Aujourd'hui, nous n'avons pas le droit d'y répondre et nous avons écrit la réponse ailleurs.
- **Correction.** Trancher DL1 à deux, par écrit. Préparer les deux phrases d'a4 § 7, une pour chaque cas. Valider les prix par écrit au plus tard jeudi 26 novembre 2026 (Étude prix, DL5 et DL6).

### 7. Des promesses dépassent ce que deux personnes, sans société ni assurance, peuvent tenir

- **Constat.** 50 promesses relevées : 30 tenables sous conditions, 15 non tenables telles qu'écrites, 5 dépendantes d'un préalable non réglé, 16 nouvelles ou plus fortes que les documents internes (a3 § 3).
- **Preuve.** v11, `societe` : « une assurance » au présent, alors qu'aucune n'est souscrite (STRATÉGIE, lignes 172 et 506 ; a3 § 3, E46). v11, `trajectoire` : « Société créée et assurée » rangée à un an, alors que c'est un préalable. v11, `cat-admin` : « Sous 24 heures » ; v11, `administratrice` : « avec vous, chaque semaine » ; v11, `cat-marketing` : « Un site par lieu » (a3 § 3, E4, E5, E23). Cadre de capacité : dix journées facturables par mois au plus la première année ; le cadrage en prend huit et demie (a3 § 3).
- **Conséquence pour sa décision.** Il paierait la moitié d'avance à une société qui n'existe pas encore. Toute promesse non tenue ensuite se retourne contre la seule qui compte : « une étape et un essai à la fois ».
- **Correction.** La formule de statut d'a3 § 5.9, mot pour mot. Retirer les 16 promesses nouvelles ou plus fortes. Décider de l'assurance avant d'écrire qu'une attestation sera remise (Étude prix, DL10).

### 8. Il n'y a rien à montrer, et le fichier de prospection sert de vitrine

- **Constat.** Aucun outil n'est en service. La seule référence citée est un fichier qui ne doit pas être montré.
- **Preuve.** a3 § 4 : dossiers de création gelés, « Œuvre proposée, non fabriquée » ; fichier `crm/` non présentable (283 des 471 numéros à confirmer, 14 oppositions notées, incident en cours). v11, `societe` : « Nous avons déjà construit un outil de prospection des entreprises de la Nièvre ». v11, `crm` : titre « Vendre vos œuvres aux entreprises de la Nièvre » (a3 § 1, n° 74). La propriété du fichier n'est pas tranchée (D12).
- **Conséquence pour sa décision.** S'il demande à voir l'outil, il n'y a que deux réponses : refuser ou montrer des données de personnes réelles. Les deux coûtent.
- **Correction.** Retirer `crm`. Déplacer la preuve de « ce que nous avons fait » vers « ce que vous pourrez vérifier » : mesure avant et après, arrêt possible, comptes au nom de sa société (a3 § 4). Au plus une maquette fixe, marquée « Maquette — données fictives », si le gel de production est levé par écrit pour cet objet (a4 § 10, décision 20).

### 9. Tout repose sur des faits qu'il n'a pas confirmés, et son administratrice est mise en discussion

- **Constat.** Les bâtiments, le cabaret-spectacle, l'administratrice : rien ne vient de lui directement.
- **Preuve.** MAJ:348 ; BRIEF § 2 (déclarations de Morgan, non vérifiées). v11, `administratrice` décrit son poste (« Coordonne tous les projets », « Valide et envoie ») sans que ni elle ni son employeur l'aient confirmé (a3 § 2, règle 6). v11, `echange`, question 4 : « Quel rôle et quels pouvoirs donnez-vous à votre administratrice ? », peut-être posée devant elle (a1 § 1 et § 5).
- **Conséquence pour sa décision.** Une erreur sur ses projets dès la deuxième diapositive, ou une administratrice qui se sent visée, et la suite n'est plus écoutée (a1 § 4).
- **Correction.** Garder « Ce résumé reste à confirmer avec vous. » (v11, `compris` ; a3 § 1, n° 9) et présenter chaque fait comme une question (a3 § 7.3). Poser la question sur l'administratrice à GianLuca Carlone seul. Écrire « aidée, jamais remplacée ni surveillée » ; « on mesure la tâche, jamais la personne » (BRIEF, règle 6 ; a1 § 5).

### 10. Trop long, trop dense, et trois passages hors sujet

- **Constat.** Il décroche trois fois : aux avancées, au catalogue, à l'avenir de Marwin Tech (a1 § 2).
- **Preuve.** 26 diapositives ; 2 672 mots visibles selon a2, 2 888 selon a5 (méthodes de comptage différentes) ; 23 diapositives sur 26 dépassent 60 mots (a2 § 8) ; corps à 24 px sur une page de 1 080 px ; six tableaux de catalogue de suite, diapositives 9 à 14 ; `trajectoire` 173 mots ; `administratrice` déborde de 12 px (a5, Mesures). Image de bras robotisé en couverture et diapositive `robotique` entière, contre la règle 10 (a3 § 2).
- **Conséquence pour sa décision.** Le temps passé sur la robotique et sur notre avenir est pris sur le seul sujet qui le fait décider : son premier pas.
- **Correction.** 18 à 21 diapositives et 8 annexes au plus ; 80 mots au plus par diapositive, 60 visés ; corps à 28 px au moins ; titres de 55 caractères au plus (a2 § 6 ; a5, Recommandations). Retirer `domaines`, `crm`, `robotique`, `pour-dautres` ; passer le catalogue en annexe.

---

## Diapositive par diapositive

Une recommandation par diapositive, tirée des quatre lectures : a1 (ce qu'il ressent), a2 (le récit), a3 (l'exactitude), a5 (la forme). Bilan : 3 à garder, 4 à fusionner, 8 à réécrire, 7 à passer en annexe, 4 à retirer.

| N° | Diapositive (v11) | Décision | Pourquoi, en une ligne | Sources |
| --- | --- | --- | --- | --- |
| 1 | `cover` — « Ce que l'IA peut faire pour vos projets » | Réécrire | Parle de l'IA et de notre avenir, pas de lui ; « sans engagement » et image de robot à retirer | a1 § 1 ; a2 § 2 ; a3 n° 3 ; a4 § 9 |
| 2 | `compris` — « Ce que nous avons compris » | Réécrire | Bon principe, faits non confirmés par lui ; ajouter sa demande d'outil pour ses propriétés | a1 § 1 ; a3 § 7.3 ; MAJ:348 |
| 3 | `idee` — titre de 99 caractères | Fusionner | Même message que `administratrice` et `modes` ; titre trop long | a2 § 2 ; a5 |
| 4 | `avancees` — « Des avancées qui changent l'échelle du possible » | Réécrire | Titre et deux phrases à retirer ; trois nouveautés sourcées suffisent (a1 la couperait) | a3 n° 14 à 16 ; a2 § 2 ; r1, r2 |
| 5 | `ia-aujourdhui` — « Ce qu'elle fait bien, et ce qu'elle fait mal » | Garder | Les trois colonnes sont exactes ; à alléger | a3 n° 23 ; a2 § 2 |
| 6 | `administratrice` — « Elle coordonne, l'IA prépare, nous construisons » | Fusionner | Message fort, mais poste décrit sans confirmation ; déborde de 12 px | a1 § 1 ; a3 § 2, règle 6 ; a5 |
| 7 | `domaines` — « Douze domaines, de l'administration à la robotique » | Retirer | Sommaire d'un catalogue qui part en annexe ; remet la robotique en avant | a2 § 2 ; a3 § 2, règle 10 |
| 8 | `modes` — « Ce que l'IA fait seule, ce qu'elle prépare, ce qui reste à vous » | Garder | Clé de lecture utile ; corriger « L'IA rédige, trie ou calcule » et définir « Automatique » | a3 n° 43 et § 5.3 ; a2 § 2 |
| 9 | `cat-admin` — « Administration et pilotage, pour votre administratrice » | Annexe | Tableau dense ; « Sous 24 heures », « Relances » et « paiements » en automatique à corriger | a3 § 3, E4 ; a3 § 2, règle 5 ; a5 |
| 10 | `cat-batiments` — « Bâtiments, travaux et sécurité » | Annexe | Le sujet le plus proche de sa demande : en tirer la diapositive `proprietes` du corps | a1 § 1 ; p0 |
| 11 | `cat-galerie` — « Galerie, œuvres et ventes d'art » | Annexe | Fort pour lui ; un seul exemple remonte dans le corps (la fiche d'œuvre) | a1 § 1 ; a3 § 3, E11 ; r2 |
| 12 | `cat-cabaret` — « Cabaret-spectacle et commerces » | Annexe | Aucun commerce n'est ouvert ; « Rapprochement quotidien » n'est pas notre engagement | a3 § 3, E10 ; a2 § 2 |
| 13 | `cat-finance` — « Finance, équipes et conformité » | Annexe | Retirer « toujours à jour » ; garder le refus de noter candidats et salariés | a3 n° 67 et n° 69 |
| 14 | `cat-marketing` — « Marketing, contenus et événements » | Annexe | Seulement une fois retirés « Un site par lieu » et l'assistant qui répond seul ; sinon retirer | a3 § 3, E23 ; a1 § 1 |
| 15 | `crm` — « Vendre vos œuvres aux entreprises de la Nièvre » | Retirer | Fichier non présentable, propriété non tranchée, incident en cours | a3 n° 74 et n° 77 ; a3 § 4 ; Rendez-vous § 9 |
| 16 | `logiciels` — « Les bons outils, à votre nom, sans dépendre de nous » | Réécrire | Devient la réponse à sa demande ; surtitre « Logiciels sur mesure » à retirer | a3 n° 82 ; p0 ; a4 § 5 |
| 17 | `robotique` — titre de 70 caractères | Retirer | Contraire à la règle 10 ; une ligne « plus tard, sous conditions » suffit dans `etapes` | a3 n° 91 et § 5.7 ; a2 § 2 |
| 18 | `apports` — « Ce que vous pouvez en attendre » | Fusionner | À fondre dans un avant/après ; aucun gain avant la mesure de départ | a2 § 4.5 ; a3 n° 97 |
| 19 | `regles` — « Les risques de l'IA, et notre réponse » | Annexe | Utile en réponse aux questions ; les trois règles clés remontent dans la méthode | a2 § 2 ; a3 § 5.5 et § 5.6 |
| 20 | `methode` — « Vous décidez, nous préparons et nous rendons des comptes » | Fusionner | Affirmations exactes ; même sujet que `etapes` et `regles` | a3 n° 108 à 113 ; a2 § 2 |
| 21 | `societe` — « Marwin Tech, la société que nous créons » | Réécrire | « une assurance » au présent, fichier cité en référence, « garantie » en note | a3 n° 120 et § 5.9 ; a3 § 3, E46 |
| 22 | `pour-dautres` — « Ce que Marwin Tech apportera aussi à d'autres » | Retirer | Promet son outil à ses concurrents ; « garantit aussi la continuité » | a1 § 1 ; a3 n° 123 |
| 23 | `trajectoire` — « Dans un an, deux ans, cinq ans » | Réécrire | 173 mots, états écrits comme atteints ; une ambition courte, avec ses conditions (a1 la couperait) | a3 § 5.8 ; a2 § 5 ; a5 |
| 24 | `etapes` — « Chaque étape se gagne par des preuves » | Garder | La meilleure diapositive de décision ; à remonter, dater, et y inscrire son logiciel | a1 § 1 ; a2 § 2 ; a4 § 9 |
| 25 | `premier-pas` — « Un cadrage de trois à quatre semaines » | Réécrire | Devient l'offre chiffrée ; supprimer « remise à part » et les mots « carte des rôles », « grille de délégation » | a4 § 9 ; a3 n° 142 |
| 26 | `echange` — « Parlons de vos priorités » | Réécrire | Devient la décision ; la question 4 se pose à lui seul ; deux noms seulement si Mathys a signé | a4 § 9 ; a1 § 1 ; a3 n° 143 |

**À ajouter, absent de la v11.**

- L'offre chiffrée et la décision : deux diapositives rédigées en projet (a4 § 9).
- « Un outil commun pour vos bâtiments et vos lieux », « Une automatisation à la fois, mesurée avant et après », « Cinq candidates, trois essais au plus » (p0).
- La grille neutre : « Six questions à poser à toute offre, la nôtre aussi » (a2 § 6.1 ; LOGICIEL § 8).
- « Si vous dites oui : quatre étapes d'ici janvier » (a2 § 6.1 ; CADRAGE:172 à 175).

**Là où les notes ne sont pas d'accord.**

| Sujet | Positions | Recommandation |
| --- | --- | --- |
| Longueur | a1 : dix à onze diapositives ; a2 : 21 et 8 annexes ; a5 : 18 à 22 et 8 annexes | 18 à 21 et 8 annexes au plus ; garder la version courte d'a1 comme repli si le rendez-vous est bref |
| `avancees` et `trajectoire` | a1 : couper ; a2 : réécrire | Réécrire en une diapositive chacune ; couper si le texte n'est pas vérifié à temps |
| Démonstrations | a1 § 7 : cinq démonstrations ; a3 § 4 : aucune ; a4 § 6 : une maquette suppose de lever le gel | Aucune démonstration en direct ; au plus une maquette fixe, décidée par écrit |
| Image de couverture | a5 : un visuel Strates avec la mention « vision générée par IA » ; a3 § 4 : aucune image générée | Une vraie photo fournie par lui, sinon une couverture sans image |
| Mots par diapositive | a2 : 60 ; a5 : 80 (120 avec une maquette) | Plafond à 80, cible à 60 |

---

## Ce qui est exact, ce qui est fragile, ce qui est à retirer

D'après a3. 143 affirmations : 43 exactes, 67 à nuancer, 14 à retirer, 19 à prouver.

### Exact : à garder tel quel

- « Ce résumé reste à confirmer avec vous. » (v11, `compris` ; a3 n° 9).
- Les trois colonnes de `ia-aujourdhui` (a3 n° 23).
- « Aucune IA pour trier ou noter des candidats ou des salariés. » (v11, `cat-finance` ; a3 n° 69).
- « Une cible à vérifier sur vos dossiers, pas une promesse : on mesure avant, puis après. » (v11, `apports` ; a3 n° 97).
- Les six affirmations de `methode` (a3 n° 108 à 113).
- « immatriculée avant toute facture et tout démarrage » et « Nous sommes deux : une étape et un essai à la fois. » (v11, `societe` et `etapes` ; a3 § 2, règle 8).
- « Arrêt possible à la fin de chaque étape : vous gardez ce qui est payé, vos comptes et vos données. » (v11, `etapes` ; a3 § 3, E32).

### Fragile : vrai sous condition, à réécrire

| Ce que dit la v11 | Pourquoi c'est fragile | Formulation sûre |
| --- | --- | --- |
| « sans engagement » (`cover`) | Une proposition suit ; le mot se contredit | « Rien ne vous engage avant le bon de commande. » (a4 § 9) |
| « Sous 24 heures » (`cat-admin`) | Pas d'astreinte le week-end | « le jour ouvré suivant », préparé par l'outil, envoyé par son administratrice (a3 § 3, E4) |
| « avec vous, chaque semaine » (`administratrice`) | Quatre rendez-vous par mois sur dix journées | Point hebdomadaire avec son administratrice, point mensuel avec lui (a3 § 3, E5) |
| « une assurance » (`societe`) ; « Société créée et assurée » (`trajectoire`) | Aucune assurance souscrite | a3 § 5.9, troisième phrase seulement si la décision de souscrire est prise |
| « remis en conformité avant tout usage » (`crm`, `societe`) | Formule juste, mais coût, durée et propriété inconnus (D12) | La garder en une phrase ; ne plus citer le fichier comme référence (a3 § 3, E26) |
| « à votre nom » (`logiciels`, `regles`, `societe`) | La règle 9 dit « au nom de votre société » ; « hébergement » manque | « Comptes, hébergement et données au nom de votre société » (BRIEF, règle 9) |
| « Deux à trois tâches » dans un an (`trajectoire`) | FICHES, ligne 24, dit « deux à quatre » | Un seul chiffre dans tous les documents (a3 § 3, E17) |
| Date de départ du suivi régulier | Trois versions : quatrième mois, six mois, juillet 2027 | Une seule date, à arrêter (a3 § 3, E3 ; a4 § 2.2, n° 9) |
| Faits de `compris` | Aucune parole directe de lui | Chaque fait présenté comme une question (a3 § 7.3) |
| Quatre besoins de `premier-pas` | Le cinquième manque : l'accord sur les données (CADRAGE:152) | L'ajouter |

### À retirer : les quatorze

| N° a3 | Diapositive | Ce qui part |
| --- | --- | --- |
| 3 | `cover`, `robotique` | L'image de bras robotisé |
| 14 | `avancees` | Le titre « Des avancées qui changent l'échelle du possible » |
| 15 | `avancees` | « L'IA ne fait plus que répondre : elle remplit des tableaux, prépare des dossiers et envoie, après validation. » |
| 16 | `avancees` (note) | « des agents savent agir dans des outils (remplir, préparer, envoyer) » |
| 29 | `administratrice` | « Retrouve n'importe quel document » |
| 30 | `administratrice` (note) | « nous lui donnons un assistant IA qui connaît tous vos projets » |
| 43 | `modes` | « L'IA rédige, trie ou calcule ; une personne vérifie […] » : le mot « calcule » |
| 67 | `cat-finance` | « toujours à jour » |
| 74 | `crm` | Le titre « Vendre vos œuvres aux entreprises de la Nièvre » |
| 77 | `crm` | « Suivre appels et rendez-vous, y compris avec un centre d'appels si vous en choisissez un. » |
| 82 | `logiciels` | Le surtitre « Zoom · Logiciels sur mesure » |
| 91 | `robotique` | Le plan en trois étapes |
| 120 | `societe` (texte et note) | Le mot « garantie » : « la garantie que vos outils et vos données restent à votre nom » ; le fond est juste |
| 123 | `pour-dautres` | « Travailler pour plusieurs clients garantit aussi la continuité de Marwin Tech. » |

**À prouver avant de le dire** (19 affirmations, dont) : les faits de `compris` ; « Nous savons concevoir des logiciels » (note de `logiciels`, a3 n° 88) ; « La proposition chiffrée vous est remise à part » (a3 n° 142) ; les deux noms sur `echange` (a3 n° 143).

**Ce qui peut entrer dans la refonte.** Les formulations sûres d'a3 § 5 (5.1 à 5.9), les dix phrases « sûr pour une diapositive » de r1 et les douze de r2. Rien d'autre des notes de recherche : ni marque, ni prix d'éditeur, ni pourcentage de temps gagné (r1 et r2, « à ne pas reprendre »). De r3, seulement ses douze phrases « sûr pour une diapositive », chacune avec sa source : ni prix de robot, ni date d'humanoïde, ni échéance légale présentée comme « la vôtre » (r3, « À ne pas reprendre sur une diapositive »). La liste complète des quinze choses à ne jamais dire est dans a3 § 6.

---

## L'offre et les documents clients

D'après a4.

### Ce qui est prêt

- **Une offre d'entrée claire, à un seul prix validé** : le cadrage, 6 500 € HT, soit 7 800 € TTC, moitié à la commande, trois à quatre semaines (BRIEF § 4 ; a4 § 2.1).
- **Des clauses qui retournent le risque** : arrêt en cours de route, remboursement de la part non faite, dépassement de plus de deux semaines (CADRAGE:108) ; bon de commande caduc sans frais si la société n'est pas immatriculée sous deux mois (CADRAGE:98).
- **Une réponse écrite à sa demande de logiciel** : logiciels du marché au nom de sa société, reliés par un outil commun, par étapes ; tout sur mesure écarté (LOGICIEL § 3 à § 6).
- **Une grille neutre de seize critères** pour comparer toute proposition, la nôtre comprise (LOGICIEL § 8).
- **Deux diapositives et une page d'offre en projet** (a4 § 8 et § 9), à valider.

### Ce qui ne l'est pas

- **Rien n'est en état de partir.** Tous les documents clients portent « PROJET non envoyé » (a4 § 3, frein bloquant n° 4).
- **Pas de bon de commande ni de conditions** dans le dépôt (a4 § 3, frein bloquant n° 3).
- **Texte client et note interne dans le même fichier** (CADRAGE:186).
- **Aucune relecture d'avocat**, alors que CADRAGE:104 l'affirme.
- **Trop à lire** : environ 33 850 mots (cadrage 3 232 ; logiciel 3 284 ; annexe 10 401 ; méthode 2 781 ; fiches 13 633 ; guide 519). La phrase d'achat est enfouie dans un texte d'environ 3 200 mots (a4 § 1 et § 3).
- **Société inexistante et moitié d'avance** : le frein est réel, les garanties existent mais sont dispersées (a4 § 3).
- **Aucune date ferme** : ni démarrage, ni restitution (a4 § 2.2, n° 10).

### Les incohérences entre documents

Vingt-trois relevées (a4 § 2.2). Les douze qui se voient le plus :

| N° a4 | Incohérence | Correction proposée |
| --- | --- | --- |
| 1 | Le total n'existe nulle part (22 200 à 25 200 € HT, cadrage compris) | L'écrire dans le document remis à part, ou décider de ne jamais l'additionner |
| 2 | « 6 500 € » désigne deux choses | Réserver ce montant au cadrage |
| 3, 11 | « essai » et « pilote » changent de sens ; le pilote du logiciel dépasse l'essai de huit semaines | Un seul mot : « essai de huit semaines » |
| 4 | Trois ancrages sur trois ans, jusqu'à 240 000 € | Un seul tableau, dans un seul document |
| 5 | Deux règles d'acompte (moitié ; 40/30/30) | Une règle, ou une phrase qui explique |
| 6 | Deux délais pour le solde (8 jours ; 30 jours) | Un délai |
| 8 | Deux dates limites de rendez-vous (vendredi 11 décembre ; mardi 15 décembre 2026) | Une date |
| 9, 14 | Deux rythmes et trois noms pour le service mensuel | « suivi régulier », revu chaque trimestre |
| 15 | Quatre formules pour la propriété | « au paiement complet de chaque étape » |
| 18 | Le logiciel n'est pas l'une des suites du cadrage | La phrase de liaison d'a4 § 5 |
| 20 | Un tiers nommé dans le texte client (CADRAGE:27) | Retirer le nom |
| 23 | Texte client et note interne ensemble (CADRAGE:186) | Deux fichiers |

Les autres : seuil « au-delà de huit jours de travail estimés » (n° 7), absence de date de fin (n° 10), nombre d'étapes (n° 12), deux jeux de lettres (n° 13), libellés des niveaux d'aide (n° 16), mots sans explication (n° 17), société en formation découverte à la lecture (n° 19), deux statistiques sans source dans GARANTIES (n° 21), aide publique citée mais invisible (n° 22).

---

## Ce qui manque pour qu'il dise oui

1. **Une question.** « Commandez-vous le cadrage ? », avec trois réponses : oui ; oui, à ajuster ; non (a4 § 4 ; a2 § 4.4).
2. **Un prix à l'écran.** Celui du cadrage, et lui seul (a4 § 7 ; BRIEF, règle 12).
3. **Deux dates.** Démarrage début janvier 2027 si la commande est signée avant la mi-décembre (CADRAGE:175) ; une date de restitution écrite (a4 § 6).
4. **Une page.** L'offre en une page, au lieu de 33 850 mots (a4 § 8).
5. **Un papier à signer.** Un bon de commande d'une page et ses conditions, relus par un avocat (a4 § 6).
6. **Une réponse à sa demande.** Son logiciel de gestion des propriétés, nommé comme priorité possible du cadrage (a4 § 5 ; p0).
7. **De quoi comparer sans nous croire sur parole.** La grille neutre, remise sans condition (LOGICIEL § 8 ; a2, décisions réservées).
8. **De quoi croire à une société qui n'existe pas encore.** Immatriculation avant toute facture, caducité sans frais, attestation d'assurance si elle est décidée (a3 § 5.9 ; CADRAGE:98).
9. **La vérité dite avant.** L'incident de données et l'état réel du fichier, par un texte validé, avant la présentation (MAJ:20 ; a3 § 5.6).
10. **La clause d'arrêt en trois lignes**, visible, pas en page 6 (CADRAGE:108 ; a4 § 6).
11. **Une administratrice rassurée.** Aidée, jamais remplacée ni surveillée ; son temps chiffré honnêtement (a1 § 5).
12. **Trois informations de son côté** : la société qui commande et paie, la personne qui signe, la date du premier entretien (a4 § 4 et § 6).

Un point reste hors de notre main : un non peut être la bonne réponse, par exemple si son administratrice suffit (a1 § 4). L'offre doit pouvoir l'entendre.

---

## Décisions à prendre par Morgan et Mathys avant tout envoi

Chaque décision se prend à deux, par écrit. L'option recommandée est celle des notes d'audit ; là où elles divergent, c'est dit.

### A. Avant tout

1. **Lever ou non l'interdit d'envoi (D03, D08).** Option recommandée : ne rien envoyer et ne proposer aucune date tant que la décision sur D03 n'est pas prise et que GianLuca Carlone n'a pas été informé de l'incident par un texte validé par un conseil. Échéance interne : jeudi 19 novembre 2026 (MAJ:20 ; a3 § 7.1 ; Rendez-vous § 2.2).
2. **Accord écrit de Mathys** sur la présentation, la proposition et les prix (U07). Option recommandée : un écrit daté des deux associés ; sans lui, aucun envoi et un seul nom sur la dernière diapositive (MAJ:240 ; a3 n° 143).
3. **Le lien et les notes de l'orateur (D45).** Option recommandée : lien gardé privé ; liste écrite de ceux qui ont vu la présentation avant vendredi 13 novembre 2026 ; notes vidées ou réécrites comme si le client les lisait (a3 § 7.1).
4. **Quelle proposition de cadrage part, et sous quelle forme.** Option recommandée : une seule version désignée, celle du 9 novembre ; texte client (lignes 15 à 182) et note interne dans deux fichiers ; nom du tiers retiré à la ligne 27 (a4 § 10, décisions 2 et 3).
5. **Le signataire.** Option recommandée : nommer par écrit l'associé qui signe « au nom et pour le compte de Marwin Tech, SAS en formation », en sachant qu'il est tenu personnellement jusqu'à la reprise par la société (CADRAGE:98 et 318) ; lancer l'immatriculation tout de suite pour raccourcir cette période (a4 § 10, décision 4 ; a3 § 7.2).
6. **L'assurance de responsabilité civile professionnelle.** Option recommandée : demander le devis maintenant et décider avant d'écrire qu'une attestation sera remise ; d'ici là, retirer « une assurance » de `societe` et « assurée » de `trajectoire` (Étude prix, DL10 ; a3 § 7.2).
7. **La relecture par un avocat** : bon de commande, conditions, cession, accord sur les données, rétractation, texte sur l'incident. Option recommandée : la commander avant tout envoi ; ne pas écrire « relues par notre avocat » avant (a4 § 10, décision 5 ; a3 § 7.3).
8. **Le lien de Morgan avec le studio partenaire.** Option recommandée : le déclarer par écrit à GianLuca Carlone avec le message de recadrage (a3 § 7.2 ; Rendez-vous § 2.1).

### B. La présentation

9. **La structure.** Option recommandée : 18 à 21 diapositives et 8 annexes au plus, selon le tableau ci-dessus ; plafond de 80 mots, corps à 28 px au moins (a2 § 6 ; a5).
10. **Le sort de `robotique`, `pour-dautres`, `trajectoire` et des images de robot.** Option recommandée : retirer les deux premières et les images ; garder une ligne « plus tard, sous conditions » dans `etapes` ; réécrire `trajectoire` en ambition courte (a3 § 5.7 et § 5.8 ; a3 § 7.2).
11. **Le sort de `crm` et la propriété du fichier (D12).** Option recommandée : retirer la diapositive ; garder une phrase, « remis en conformité avant tout usage » ; trancher D12 avant d'en reparler (a3 § 7.2).
12. **Une seule description du cadrage (D46, D51).** Option recommandée : les quatre résultats de BRIEF § 4, mot pour mot, partout.
13. **La réponse écrite à « tout gérer avec l'IA » (D47).** Option recommandée : la formulation d'a3 § 5.2.
14. **Le rôle de l'administratrice (D49, U62).** Option recommandée : retirer la question 4 de `echange` ; la poser à GianLuca Carlone seul ; ne décrire son poste qu'après sa confirmation (a1 § 5 ; a3 § 7.4).
15. **Maquette ou non.** Option recommandée : aucune démonstration en direct ; une seule maquette fixe marquée « Maquette — données fictives », si le gel de production est levé par écrit pour cet objet avec un temps plafonné ; sinon y renoncer (a4 § 10, décision 20 ; a3 § 4).
16. **La couverture.** Option recommandée : une vraie photo de ses lieux, fournie par lui ; à défaut, aucune image (a3 § 4). a5 propose un visuel du dossier Strates : à écarter.

### C. L'offre et les prix

17. **Montrer le prix du cadrage à l'écran.** Option recommandée : oui, sur la diapositive d'offre, avec la phrase d'a4 § 7 ; « prix fixe » annoncé dès l'ouverture (a4 § 10, décision 6 ; a2, décisions réservées).
18. **Maintenir ou lever DL1.** C'est la décision qui change le plus le rendez-vous (a4 § 10, décision 14). Option recommandée : la maintenir tant que D03 et D08 ne sont pas levés et que les prix ne sont pas validés par écrit ; d'ici là, le document LOGICIEL n'est pas remis et la réponse orale est : « Nous vous remettons un prix par étape après le cadrage, sur vos volumes réels. » (a4 § 7). Décider de la lever, ou non, au plus tard jeudi 26 novembre 2026, avec DL5 et DL6.
19. **Le total.** Option recommandée : l'écrire (22 200 à 25 200 € HT, cadrage compris) dans le document remis à part une fois DL1 levée ; jamais à l'écran (a4 § 5 et § 10, décision 18).
20. **La frontière cadrage / « choix des logiciels » (DL5), le prix et le nom de la maintenance (DL6), le logiciel comme priorité du cadrage (DL7).** Option recommandée : DL7 oui, avec la phrase d'a4 § 5 et la règle « aucune autre suite en parallèle » ; DL5 et DL6 tranchées par écrit avant jeudi 26 novembre 2026, pour ne rien facturer deux fois (a4 § 10, décisions 15 à 17).
21. **Une seule règle d'acompte, un seul délai pour le solde.** Option recommandée : moitié à la commande pour le cadrage, et une phrase qui explique toute autre règle (a4 § 10, décision 19).
22. **La page d'offre et le bon de commande d'une page.** Option recommandée : adopter la page d'a4 § 8 après relecture ; faire rédiger le bon de commande (a4 § 10, décision 7).
23. **Sept jours sans paiement pour tous, formulaire de rétractation joint.** Option recommandée : oui, dans tous les cas (a4 § 10, décision 11).
24. **La version réduite du cadrage.** Option recommandée : elle ne sort qu'en cas de refus du prix, décidée à deux la veille, jamais proposée d'emblée (a4 § 10, décision 13 ; Rendez-vous § 8.7).
25. **L'aide publique au conseil.** Option recommandée : ne pas en parler tant que personne n'a vérifié qu'une société nouvelle peut être retenue et que le dépôt avant signature tient dans le calendrier (a4 § 10, décision 12).

### D. Le rendez-vous

26. **Signer en séance ou non.** a4 § 4 prévoit un « oui aujourd'hui » ; Rendez-vous § 9, ligne rouge 1, interdit toute signature pendant le rendez-vous. Option recommandée : rien n'est signé en séance ; un oui vaut accord de principe et trois informations ; le bon de commande part sous deux jours, à signer à distance.
27. **Une seule date limite pour le rendez-vous.** Option recommandée : vendredi 11 décembre 2026, celle des textes clients (CADRAGE:172) ; corriger le mardi 15 décembre 2026 des autres documents (a4 § 10, décision 8).
28. **Une date de restitution écrite.** Option recommandée : oui, liée à la réception des documents ; les dates du lundi 4 et du vendredi 29 janvier 2027 sont des exemples d'a4, pas des dates convenues (a4 § 6).
29. **Les documents remis au rendez-vous.** Option recommandée : la page d'offre, le bon de commande et la proposition de cadrage ; rien d'autre sans demande de sa part (a4 § 10, décision 21).
30. **Le vocabulaire.** Option recommandée : un seul mot par chose dans les quatre documents en relecture (« essai de huit semaines », « suivi régulier », « au paiement complet de chaque étape ») ; plus de lettres pour les suites et les approches (a4 § 10, décision 21).

**Les trois qui commandent tout le reste** : la 4 (séparer le texte client de la note interne), la 5 (le signataire) et la 18 (DL1) (a4 § 10).

---

## Limites de ce document

- C'est une synthèse : aucune affirmation de la v11 n'a été revérifiée au-delà de ce que les notes a1 à a5 rapportent, sauf les citations de huit diapositives et les lignes de CADRAGE, LOGICIEL, FICHES et MAJ citées ici, relues dans les fichiers.
- Le fichier `pour-carlone/presentation-ia/README.md` annonce une version 12 ; seule la version 11 est dans le dépôt et a été auditée.
- r3 a été vérifiée pendant l'écriture de ce document : sa liste « sûr pour une diapositive » n'a servi à aucune formulation proposée ici. Les notes sur l'autre offre (`travaux/x1`, `x2`, `x3`) sont hors de la liste de lecture de la mission ; elles n'ont servi à aucune formulation destinée au client.
- Les recommandations sur les décisions 5, 18, 26 et 27 arbitrent entre des notes qui ne concluent pas de la même façon. Elles restent à trancher par Morgan et Mathys.
