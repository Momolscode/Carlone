# Note interne — « Ce que des moyens supplémentaires nous permettraient d’accomplir »

Document interne — ne pas transmettre à GianLuca Carlone · 10 novembre 2026 · Ce document n’est pas un avis juridique, fiscal ou d’investissement.

## En bref

1. Deux projets client existent : la page (`pour-carlone/developpement/2026-11-10-ce-que-des-moyens-supplementaires-permettraient.md`, une page A4, contrôle sans erreur) et l’annexe chiffrée (`pour-carlone/developpement/2026-11-10-annexe-comparaisons-et-calculs.md`, contrôle sans erreur ; alertes = tarifs publics, chacun avec sa source sur la ligne). Les deux ont été relus et corrigés le 10 novembre d’après les vérifications de k13a, k13b, k13c, k13d et k13f (voir § 2) ; les fiches 09 et 12 ont été alignées le même soir (mêmes chiffres, mêmes formulations).
2. **État des sources** (`audit/2026-11-10-preparation-des-livrables/travaux/`) : k13a (matériel), k13b (location), k13c (abonnements, API), k13d (personnes) et k13f (études) ont une partie « Vérification du 10 novembre 2026 », qui l’emporte sur le reste de chaque note. k13b, k13d et k13f s’arrêtaient au milieu : leur vérification ajoute l’essentiel qui manquait. k13e (laboratoire, robotique) est à peine commencée. Les prix de location de l’annexe sont relus : OVHcloud sur sa page de tarifs ; Scaleway sur son catalogue public des prix, sa page de tarifs refusant les robots.
3. L’ambition « cent fois plus » est tenue honnêtement : un indicateur (documents lus par heure), une base (une personne qui les lit un par un, environ six devis par heure : estimation à mesurer), une limite (première lecture de documents répétitifs, traités en parallèle) ; cinq à dix fois sur la chaîne complète avec vérification humaine ; ailleurs, selon la tâche, de −19 % à +56 % dans les études publiées (METR 2025 ; Peng et al. 2023) ; rien sur la relation et la décision. Tout est « hypothèse à évaluer ». C’est cette distinction qui rend l’ambition crédible. La règle de calcul du « cinq à dix fois » (temps de vérification d’un devis) est dans k13f, vérification, « Compléments essentiels ».
4. **Recommandation matériel** : pas de DGX Station (90 000 à 171 500 € HT chez BuyZero, Allemagne, guide du 5 novembre 2026 ; 1 600 W) sans besoin mesuré ; le paiement à l’usage et la location suffisent au départ ; une machine de bureau de 128 Go se justifie seulement pour garder ses documents confidentiels chez lui, achetée au nom de sa société, avec les conditions de k13a § 6 (logiciels qui n’envoient rien en ligne, sécurité tenue).
5. **Le levier le plus fort est humain** : la continuité (aujourd’hui, si l’un de nous manque, tout s’arrête) et la capacité (une étape et un essai à la fois).
6. **Rendez-vous du vendredi 13 novembre 2026** (tout prêt le jeudi 12) : sans les préalables (incident de données, texte d’information validé, accord écrit des deux associés), la page et l’annexe se montrent à l’écran sans être remises (`audit/2026-11-10-preparation-des-livrables/travaux/BRIEF-2.md`, ligne 140).

## 1. Les formes possibles d’un soutien (jamais dans un document client)

| Forme | Avantage | Risque | À faire valider par |
| --- | --- | --- | --- |
| Commandes plus larges ou plus nombreuses | La plus simple ; aucune dépendance de capital | Dépendance à un seul client | — |
| Matériel acheté par sa société, installé chez lui, à son nom | Cohérent avec la règle « comptes, données et outils à son nom » ; ses données restent chez lui, sous les conditions de k13a § 6 | Entretien et sécurité à prévoir par contrat : quelques heures par mois au minimum, prises sur nos missions (k13a, ligne 193, estimation) | Expert-comptable (amortissement), avocat (contrat d’usage) |
| Avance sur un contrat de plusieurs mois | Trésorerie | Engagement de livrer ; remboursement si arrêt | Avocat, expert-comptable |
| Prise de participation dans Marwin Tech | Moyens durables | Conflit d’intérêts client et actionnaire ; perte d’indépendance ; statuts et pacte à revoir ; valorisation d’une société pas encore immatriculée | Avocat, expert-comptable |
| Aides publiques (Bpifrance, région, apprentissage) | Pas de dépendance au client | Délais, conditions ; les aides à l’innovation exigent de la vraie recherche ou un vrai prototype, documentés : la JEI demande au moins 20 % de dépenses de recherche et développement dans les charges et une société de moins de 8 ans (entreprendre.service-public.gouv.fr, F31188, vérifié) ; le CIR est un crédit d’impôt de 30 % des dépenses de recherche (F23533, page de février 2025) ; CII et Bourse French Tech non vérifiés (k13d, vérification) ; aide à l’apprentissage de 2 000 € à 5 000 € la première année (F23556, vérifié) | Expert-comptable ; organismes concernés |

La proposition de cadrage du 9 novembre dit déjà : « Toute autre relation (locaux, emploi, participation) ferait l’objet d’un accord séparé, sans lien avec nos honoraires. » (`audit/2026-11-04-audit-strategique/pour-gianluca/2026-11-09-proposition-de-cadrage.md`, ligne 134). Cette règle tient.

## 2. Repères chiffrés : vérifié ou non

Chemins relatifs à `audit/2026-11-10-preparation-des-livrables/travaux/`.

**Vérifié ou « sûr à reprendre » le 10 novembre 2026** (peut aller dans l’annexe client, avec sa source et sa date) :

- DGX Spark : 128 Go, alimentation de 240 W, 160 W mesurés en charge ; prix conseillé NVIDIA passé de 3 999 $ (octobre 2025) à 4 699 $ le 23 février 2026, « applies to all regions » (k13a, lignes 253 et 255 ; Tom’s Hardware, ligne 171).
- DGX Station : 748 Go, 1 600 W ; 90 000 à 171 500 € HT chez BuyZero (Allemagne), guide du 5 novembre 2026 ; aucun prix français (k13a, lignes 257 et 260).
- Mac Studio M5 Ultra : à partir de 6 599 € TTC avec 96 Go (Apple Newsroom France, 25 août 2026 ; k13a, ligne 262).
- Indice Artificial Analysis v5 : 32 points pour les modèles ouverts téléchargeables les mieux notés, 58 pour le premier fermé au 27 octobre 2026 ; depuis le 28 octobre, Gemini 4 Carbon (non public) est premier à 59 (k13a, ligne 264).
- Abonnements, hors taxes : Claude Pro 17 $ (annuel) ou 20 $ ; Max 100 $ ; Ultra 200 $ ; Team 20 $ / 25 $ la place simple, 100 $ / 125 $ la place renforcée ; Mistral Pro 14,99 $ (k13c, lignes 181, 182 et 198).
- API Anthropic, par million de jetons, hors taxes : Opus 5.5 4 $ / 20 $ ; Sonnet 5.5 2 $ / 10 $ ; Haiku 5.5 0,10 $ / 0,50 $ (k13c, ligne 184). Un devis de trois pages : environ 0,02 $ (Sonnet) à 0,04 $ (Opus), estimation (k13c, ligne 235). Premier frein : au niveau Start, le plafond de 500 $ par mois arrête l’API après environ 12 500 devis lus par Opus ; ensuite vient la relecture humaine (k13c, ligne 210).
- Électricité d’une DGX Spark jour et nuit : environ 1 400 kWh, moins de 300 € TTC par an (k13a, ligne 299, estimation).
- Location en France, hors taxes, à l’heure : OVHcloud L4 0,75 €, L40S 1,40 €, A100 2,75 €, H100 2,80 € (page « Tarifs Public Cloud », relue en entier) ; Scaleway L4 environ 0,79 €, L40S 1,47 €, H100 2,87 €, facturés à la minute (catalogue public des prix ; la mention « avant taxes » de la page n’a pas pu être relue) (k13b, vérification). Les prix mensuels d’OVHcloud ne sont pas le prix horaire × 730 : citer le prix horaire.
- Études (k13f, vérification) : METR 2025, 19 % de temps en plus (16 développeurs, 246 tâches), en croyant avoir gagné 20 % ; METR 2026, −18 % et −4 %, jugé « very weak » par METR ; Peng et al. 2023, 55,8 % plus vite ; Dell’Acqua et al. (Organization Science, mars 2026), 12,2 % de tâches en plus, 25,1 % plus vite, 19 % de solutions correctes en moins hors de portée de l’outil ; Brynjolfsson et al. (NBER 2023, publié en 2025), +14 % en moyenne, +34 % pour les débutants. D’où la formule commune aux documents client : « selon la tâche, de −19 % à +56 % ».
- Tendances (k13f, vérification) : la longueur des tâches de logiciel qu’un agent réussit seul une fois sur deux double environ tous les sept mois depuis 2019, tous les 89 jours depuis 2024 (METR, 29 janvier 2026) ; début 2026, environ 1 h 30 réussie quatre fois sur cinq (METR, 19 mai 2026). À qualité égale, le coût d’usage baisse d’environ 47 % par trimestre depuis 2023, soit 13 fois par an, en ralentissant ensuite (Epoch AI, 22 septembre 2026).
- Personnes, faits officiels seulement (k13d, vérification) : Smic 1 867,02 € brut par mois depuis le 1er juin 2026 (F2300) ; aide à l’embauche d’un apprenti, moins de 250 salariés : 5 000 € jusqu’au bac, 4 500 € bac + 2, 2 000 € bac + 3 à bac + 5, la première année, contrats conclus depuis le 8 mars 2026 et, pour les deux derniers montants, commencés avant le 1er janvier 2027 (F23556). Jamais dans un document client.

**Non vérifié** (interne seulement, à relire avant tout usage client) :

- DGX Spark 128 Go à 6 950 $ (presse du 8 octobre 2026 ; k13a, ligne 256) ; revendeurs français de 5 500 à 7 500 € HT, jusqu’à 9 000 € TTC (k13a, lignes 41 et 271) ; suivi magicprices.fr de 5 608 € à 9 960 € entre septembre et novembre 2026 (k13a, ligne 38). Ne jamais écrire dans un document client qu’une machine coûte « à peu près le prix du cadrage » (k13a, ligne 300).
- Station RTX PRO 6000 complète : environ 18 000 à 25 000 € HT (k13a, ligne 85, estimation sur des prix de revendeurs non relus) ; mini-PC AMD 128 Go : environ 2 800 à 3 600 € HT (k13a, ligne 102). Pour nos propres essais, sans données de clients, un mini-PC AMD ou un Mac Studio M5 Max suffisent (k13a, ligne 219, estimation).
- Location en France : 0,75 € HT de l’heure (L4) à 2,80 € HT (H100) chez OVHcloud ; 0,79 € HT (L4) chez Scaleway (k13b, lignes 23 et 32 ; pages lues le 10 novembre, sans relecture croisée). Ces prix sont dans l’annexe client : à relire avant toute remise.
- Personnes : environ 26 900 € par an de coût employeur pour 2 000 € brut par mois, 43 900 € pour 2 800 € ; apprenti environ 1 000 € par mois la première année, aide de 2 000 à 4 500 € selon le diplôme ; président de SAS : environ 3 500 € de coût pour 2 000 € net, sans droit au chômage (k13d, lignes 11 à 13, estimations). Jamais dans un document client.
- Études : +14 % à +34 % (assistance clientèle), +25 % à +56 % (tâches définies), 19 % de temps en plus pour des développeurs expérimentés (2025 ; la mesure de 2026 est jugée peu fiable par METR) ; aucune étude lue ne mesure « dix fois » ou « cent fois » sur un travail humain complet (k13f, lignes 13 à 58).
- Totaux de l’annexe, § 4 (estimations à valider) : « 6 000 à 10 000 € HT » pour une machine de bureau et sa mise en service, au-dessus de la fourchette de k13a (2 800 à 7 500 € HT, ligne 214) parce qu’une machine chez GianLuca Carlone serait une DGX Spark ou un Mac Studio (ligne 220) ; « 11 000 à 25 000 € HT » (k13a, ligne 215) ; outils « un à deux milliers d’euros par mois » pour quatre à six personnes, dont la location (H100 en continu : 1 940 € HT par mois, k13b, ligne 23 ; places d’équipe : k13c, ligne 164).

## 3. Décisions pour Morgan et Mathys

1. Montrer la diapositive dans la version 12 : ☐ oui, après le prix et la décision ☐ en annexe seulement ☐ non. Recommandation : oui, après la décision, comme une perspective, sans parler d’argent en séance (décision V7 : `interne/decisions/2026-11-10-feuille-de-decisions.md`, lignes 21 et 126).
2. Valider la phrase « Jusqu’à cent fois plus de documents lus par heure, pour la première lecture de documents répétitifs, par rapport à une personne qui les lit un par un » et l’engagement de la mesurer pendant l’essai.
3. Garder ou retirer « Si l’un de nous manque, le travail s’arrête » (page client) : c’est vrai et cela justifie la page, mais cela peut nourrir l’objection de légitimité.
4. Valider les estimations de l’annexe, § 4 (investissement de départ, dépenses courantes), ou les retirer.
5. Garder ou remplacer l’exemple de tarifs d’Anthropic dans l’annexe (§ 1 et § 2). Ils sont vérifiés (k13c, ligne 184), mais Anthropic ne propose qu’un traitement « global » ou aux États-Unis (k13c, ligne 258). Autre exemple possible : Mistral (tarifs vérifiés, ligne 198 ; lieu de traitement par défaut non lu).
6. Faire relire avant toute remise : les prix de location (k13b) et le prix actuel de la DGX Spark en euros.

## 4. Reste à faire

- Vérifier k13b, k13d et k13f ; terminer k13e (outil : `outils/2026-11-10-orchestration/workflows/prep-moyens.js`).
- Aligner la diapositive `moyens` de la version 12 (`pour-carlone/presentation-ia/2026-11-10-version-12-projet/project/slides/moyens.html`) sur la page corrigée : « Jusqu’à cent fois plus vite » (ligne 4) n’a ni indicateur ni base ; « Vos documents chez vous » (ligne 5) et la note de l’orateur (ligne 10, lisible par qui ouvre le lien) disent que ses archives restent chez lui sans les deux conditions (logiciels qui n’envoient rien en ligne, sécurité tenue). Même remarque pour le déroulé (`interne/rendez-vous/2026-11-10-deroule-et-texte-d-orateur.md`, ligne 46).
