# « Jusqu'à cent fois plus » : où l'IA multiplie vraiment la capacité, où elle ne la multiplie pas, et comment le mesurer

Note de travail interne — sources publiques consultées le 10 novembre 2026 — ce n'est pas un avis juridique, fiscal ou d'investissement

*Auteur : chercheur (note k13f) pour le dixième livrable (BRIEF-2, § 9.2). Ce n'est pas le livrable. Les faits rapportés par Morgan sur GianLuca Carlone ne sont pas vérifiés auprès du client. Étiquettes : [Officiel] page d'un éditeur ou d'une autorité ; [Prix public daté] ; [Mesure publiée] article de recherche ou mesure d'un laboratoire ; [Source professionnelle] presse, blog, agrégateur ; [Estimation] calcul de cette note ; [À confirmer].*

## En bref

(provisoire, jamais complété : voir à la fin « Vérification du 10 novembre 2026 », dont la conclusion tient lieu de résumé et qui l’emporte sur le reste de la note)

## 1. Ce que mesurent les études sérieuses sur les gains de productivité

**Règle de lecture.** Chaque étude mesure une tâche précise, avec un outil précis, à une date précise. Aucune ne mesure « la productivité » en général. Les gains publiés vont de −19 % à +56 % sur le temps ou le débit d'une tâche. Aucune étude sérieuse lue ne mesure un « × 10 » ou un « × 100 » sur un travail humain complet.

### 1.1 Assistance clientèle : Brynjolfsson, Li et Raymond

- **Chiffre.** +14 % de demandes résolues par heure en moyenne (version de travail NBER) ; +15 % de discussions résolues par heure dans la version publiée. +34 % pour les débutants et les moins qualifiés. Presque rien pour les plus expérimentés, avec une petite baisse de qualité chez les meilleurs. Avec l'outil, un agent de deux mois d'ancienneté fait aussi bien qu'un agent de plus de six mois sans l'outil. (Brynjolfsson, Li, Raymond, « Generative AI at Work », Quarterly Journal of Economics, vol. 140, n° 2, 2025, p. 889-942 ; NBER w31161 ; communiqué EurekAlert sur la version publiée) [Mesure publiée]
- **Population et tâche.** 5 172 agents d'assistance clientèle d'une entreprise de logiciels de la liste Fortune 500. Discussions écrites avec des clients. (mêmes sources) [Mesure publiée]
- **Méthode.** Un assistant fondé sur GPT-3 propose des réponses en temps réel. L'outil arrive par vagues ; on compare les agents avant et après, et entre eux. (mêmes sources) [Mesure publiée]
- **Limites.** Une seule entreprise. Une seule tâche, très répétitive. Un modèle de 2020-2022, dépassé. Le gain porte sur un débit horaire, pas sur le résultat de l'entreprise.
- **Leçon pour nous.** Le gain est le plus fort pour une personne nouvelle dans le métier. Cela parle à l'administratrice centrale récemment engagée (fait rapporté par Morgan, à confirmer) : l'outil peut l'aider à apprendre vite les dossiers. Ce n'est pas un multiplicateur : c'est +14 % à +34 %.

### 1.2 Consultants du BCG : Dell'Acqua et al., la « frontière irrégulière »

- **Chiffre.** Sur 18 tâches réalistes de conseil *dans* la frontière de l'IA : +12,2 % de tâches terminées, tâches finies 25,1 % plus vite, qualité jugée plus de 40 % supérieure à celle du groupe témoin. Gain de +43 % pour les consultants sous la moyenne, +17 % pour ceux au-dessus. Sur une tâche choisie *hors* de la frontière : 19 points de pourcentage de bonnes réponses en moins avec l'IA. (Dell'Acqua, McFowland, Mollick et al., « Navigating the Jagged Technological Frontier », Harvard Business School, document de travail 24-013, 22 septembre 2023, résumé lu dans le PDF) [Mesure publiée]
- **Population et méthode.** 758 consultants du Boston Consulting Group, environ 7 % des consultants de ce niveau. Expérience préenregistrée. Tirage au sort en trois groupes : sans IA, avec GPT-4, avec GPT-4 et une courte formation. Mesure de départ sur une tâche voisine. (même source) [Mesure publiée]
- **Publication en revue.** Une version publiée serait parue dans Organization Science, vol. 37, n° 2, p. 403-423 (DOI 10.1287/orsc.2025.21838), selon des notices lues dans les résultats de recherche. [À confirmer]
- **Limites.** Tâches d'expérience, pas un vrai dossier client. Modèle de 2023. La frontière est invisible à l'œil nu : deux tâches de même difficulté apparente peuvent tomber de part et d'autre.
- **Leçon pour nous.** L'IA peut *dégrader* un travail quand on l'emploie hors de sa frontière. La carte des tâches (partie 5) sert à cela : savoir où l'on est.

### 1.3 Programmation, tâche fermée : Peng et al. (GitHub Copilot)

- **Chiffre.** Le groupe avec Copilot a écrit un serveur web en JavaScript 55,8 % plus vite que le groupe sans. Intervalle de confiance à 95 % : 21 % à 89 %. (Peng, Kalliamvakou, Cihon, Demirer, « The Impact of AI on Developer Productivity: Evidence from GitHub Copilot », arXiv 2302.06590, 13 février 2023) [Mesure publiée]
- **Population et méthode.** Développeurs recrutés en ligne, tirés au sort ; essai du 15 mai au 20 juin 2022. Effectif : 95 selon un résumé secondaire, non lu dans l'article [À confirmer].
- **Limites.** Une seule tâche, courte, bien définie, choisie pour l'expérience. Auteurs liés à Microsoft et GitHub (éditeur de l'outil). Le gain est le plus fort sur une tâche neuve et fermée : ce n'est pas le cas d'un travail réel dans un grand projet (voir 1.4).

### 1.4 Développeurs expérimentés sur leurs propres projets : l'essai de METR (juillet 2025) et sa suite (février 2026)

- **Chiffre de 2025.** Avec l'IA autorisée, les tâches ont pris 19 % de temps *en plus*. Avant l'essai, les développeurs prévoyaient 24 % de temps en moins ; après l'essai, ils croyaient encore avoir gagné 20 %. Des experts en économie prévoyaient 39 % de temps en moins, des experts en apprentissage automatique 38 %. (Becker, Rush, Barnes, Rein, « Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity », arXiv 2507.09089, 12 juillet 2025, révisé le 25 juillet 2025) [Mesure publiée]
- **Population et méthode.** 16 développeurs expérimentés, 246 tâches réelles dans des projets mûrs qu'ils connaissaient depuis environ cinq ans. Chaque tâche est tirée au sort : IA permise ou non. Outils : surtout Cursor Pro avec Claude 3.5 et 3.7 Sonnet. Intervalle de confiance à 95 % : +2 % à +39 % de temps. (même source ; METR, 24 février 2026, ci-dessous) [Mesure publiée]
- **Suite en 2026.** Nouvelle expérience à partir d'août 2025 : 57 développeurs (10 anciens, 47 nouveaux), plus de 800 tâches dans 143 projets. Estimation : −18 % de temps pour les anciens (intervalle −38 % à +9 %), −4 % pour les nouveaux (−15 % à +9 %). METR juge ces données **peu fiables** : beaucoup de développeurs ont refusé de travailler sans IA ; 30 % à 50 % disent avoir écarté des tâches qu'ils ne voulaient pas faire sans IA ; la rémunération est passée de 150 à 50 dollars de l'heure ; le temps est difficile à compter quand un agent travaille pendant qu'on fait autre chose. METR pense que le vrai gain est probablement plus élevé que mesuré, mais parle d'une preuve « très faible ». Il change de méthode. (METR, « We are Changing our Developer Productivity Experiment Design », https://metr.org/blog/2026-02-24-uplift-update/, 24 février 2026) [Mesure publiée] — **changement 2026 : le « −19 % » n'est plus le dernier mot, mais aucun gain fiable ne le remplace.**
- **Leçon pour nous.** (a) Le ressenti trompe : on croit gagner 20 % quand on perd 19 %. Il faut chronométrer. (b) Sur un travail réel, dans un contexte riche que l'on connaît bien, le gain peut être nul. (c) Même METR ne sait plus mesurer proprement en 2026 : nous ne ferons pas mieux sans une mesure de départ simple, posée avant l'essai.

### 1.5 Études 2025-2026 à l'échelle des entreprises et des emplois

- **Danemark (salariés).** Deux enquêtes sur 11 métiers exposés, reliées aux registres danois. Gain de temps moyen déclaré : environ 3 % du temps de travail. Aucun effet significatif sur les salaires ni sur les heures ; les intervalles de confiance excluent un effet moyen supérieur à 1 %. (Humlum et Vestergaard, NBER w33777, mai 2025 ; version renommée « Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI », RFBerlin, 13 mars 2026, non lue) [Mesure publiée ; chiffre de 3 % lu dans un résumé, le chiffre exact est à confirmer dans l'article]
- **Dirigeants d'entreprise (2026).** Près de 6 000 dirigeants aux États-Unis, au Royaume-Uni, en Allemagne et en Australie, interrogés de novembre 2025 à janvier 2026 : 89 % ne voient aucun effet de l'IA sur la productivité (ventes par salarié) de leur entreprise depuis trois ans ; ils attendent +1,4 % sur les trois ans à venir. Une version plus récente (sept pays, été 2026) parle de +0,2 % par an de productivité depuis trois ans et de +0,6 % par an attendu. (Yotzov, Barrero, Bloom, Bunn, Davis et al., « Firm Data on AI », NBER w34836, février 2026, révisé ensuite ; lu dans les résultats de recherche, page de l'article non ouverte) [Mesure publiée ; détail des versions à confirmer]
- **Leçon pour nous.** À l'échelle d'une entreprise entière, le gain mesuré en 2026 est de l'ordre de quelques dixièmes de point par an. Les gains forts existent sur des *tâches* ; ils se diluent dans le *métier* et dans l'*entreprise*. C'est exactement ce que la page client doit dire.

### 1.6 Synthèse de la partie 1

| Niveau | Gain mesuré | Exemple |
|---|---|---|
| Tâche fermée, neuve, bien définie | +25 % à +56 % de vitesse | Peng 2023 ; BCG 2023 |
| Tâche répétitive, personne débutante | +14 % à +34 % de débit horaire | Brynjolfsson et al. 2025 |
| Travail réel d'expert dans son propre contexte | −19 % à « peut-être positif » | METR 2025 et 2026 |
| Tâche hors frontière | −19 points de bonnes réponses | BCG 2023 |
| Entreprise entière | +0,2 % à +1,4 % de productivité, déclaré | NBER w34836, 2026 |

## Vérification du 10 novembre 2026

Relecture sceptique, 10 novembre 2026 (vérification commune aux notes k13b, k13d et k13f). Pour cette note : aucune recherche par moteur ; sept pages d’origine lues directement (arXiv ×2, METR ×3, NBER, notice Crossref de la version publiée de Dell’Acqua et al.) et une page d’Epoch AI ; la page de Harvard Business School a refusé l’accès (erreur 403). La note s’arrêtait à la fin de la partie 1 : la carte des tâches (« partie 5 »), la durée des tâches menées par les agents, la baisse du coût et la méthode de mesure manquaient ; l’essentiel est ajouté ci-dessous. Cette partie l’emporte sur le reste de la note.

**Conclusion.** Les chiffres qui portent la partie 1 sont justes : METR 2025 (19 % de temps en plus, 16 développeurs, 246 tâches), METR 2026 (−18 % et −4 %, données jugées peu fiables par METR), Peng et al. (55,8 % plus vite), Dell’Acqua et al. (758 consultants, 12,2 % de tâches en plus, 25,1 % plus vite), Brynjolfsson et al. (+14 %, +34 % pour les débutants). Trois points sont à corriger : l’effectif de Brynjolfsson et al. (5 179 dans la version de travail), la publication de Dell’Acqua et al. (confirmée : Organization Science, mars 2026) et la tâche « hors frontière » (« 19 % » de solutions correctes en moins dans la version publiée, pas « 19 points »). La fourchette « de −19 % à +56 % selon la tâche » tient, à condition de dire qu’elle réunit des mesures différentes. La durée des tâches menées par un agent et la baisse du coût, absentes de la note, sont vérifiées chez METR et Epoch AI.

### Tableau des contrôles

| # | Affirmation | Verdict | Source et date |
|---|---|---|---|
| 1 | Brynjolfsson, Li, Raymond : +14 % de demandes résolues par heure, +34 % pour les débutants et les moins qualifiés, effet minime pour les plus expérimentés ; publié au Quarterly Journal of Economics, vol. 140, n° 2, p. 889-942, 2025 | Confirmé | NBER, page du document w31161 (résumé et « Published Versions »), lue le 10 novembre 2026 |
| 2 | « 5 172 agents » ; « +15 % dans la version publiée » ; « deux mois d’ancienneté valent plus de six mois » ; « petite baisse de qualité chez les meilleurs » | **Corrigé** pour l’effectif (5 179 dans la version de travail) ; le reste **non relu** (page de la revue non ouverte) | NBER w31161 |
| 3 | Dell’Acqua et al. : 758 consultants, expérience préenregistrée, mesure de départ, trois groupes (sans IA, GPT-4, GPT-4 et formation), 18 tâches dans la frontière, 12,2 % de tâches en plus, 25,1 % plus vite | Confirmé | Résumé de la version publiée, notice Crossref (doi 10.1287/orsc.2025.21838), lue le 10 novembre 2026 |
| 4 | Version publiée « à confirmer » : Organization Science, vol. 37, n° 2, p. 403-423 | **Confirmé** (numéro de mars 2026) | Même notice |
| 5 | « Qualité plus de 40 % supérieure » ; « +43 % sous la moyenne, +17 % au-dessus » ; « environ 7 % des consultants de ce niveau » | **Non relu** : la version publiée dit seulement « significantly improved quality » ; le document de travail (hbs.edu) a refusé l’accès | Même notice |
| 6 | « 19 points de pourcentage de bonnes réponses en moins » hors de la frontière | **Nuancé** : la version publiée écrit « 19% less likely to produce correct solutions » | Même notice |
| 7 | Peng et al. : serveur web en JavaScript, développeurs recrutés, groupe aidé 55,8 % plus vite ; arXiv 2302.06590 du 13 février 2023 | Confirmé | arXiv, page du résumé, lue le 10 novembre 2026 |
| 8 | Peng et al. : intervalle de 21 % à 89 % ; 95 développeurs ; essai du 15 mai au 20 juin 2022 ; auteurs liés à Microsoft et GitHub | **Non relu** (absent du résumé) | — |
| 9 | METR 2025 : 16 développeurs, 246 tâches, environ cinq ans de pratique des projets, tirage au sort par tâche, surtout Cursor Pro avec Claude 3.5 et 3.7 Sonnet ; 19 % de temps en plus ; prévision −24 %, ressenti −20 %, experts −39 % et −38 % ; 12 juillet 2025, révisé le 25 juillet 2025 | Confirmé | arXiv 2507.09089, résumé et historique, lus le 10 novembre 2026 |
| 10 | Intervalle de confiance de +2 % à +39 % | Confirmé | METR, 24 février 2026 |
| 11 | METR 2026 : 57 développeurs (10 anciens, 47 nouveaux), 143 projets, plus de 800 tâches ; −18 % (−38 % à +9 %) et −4 % (−15 % à +9 %) ; refus de travailler sans IA ; 30 % à 50 % écartent des tâches ; paie passée de 150 à 50 $ de l’heure ; temps mal compté avec plusieurs agents ; preuve « very weak » ; changement de méthode | Confirmé | METR, « We are Changing our Developer Productivity Experiment Design », 24 février 2026, lu le 10 novembre 2026 |
| 12 | Humlum et Vestergaard (environ 3 % de temps gagné) ; « Firm Data on AI » (89 %, +1,4 %, +0,2 % par an) | **Non relus** : interne seulement | — |
| 13 | Complément : la durée des tâches qu’un agent réussit seul une fois sur deux double environ tous les sept mois (196 jours) de 2019 à 2025 ; tous les 131 jours depuis 2023 ; tous les 89 jours depuis 2024 ; 228 tâches, dont 31 de 8 h ou plus, 5 seulement chronométrées sur des personnes | Confirmé | METR, « Time Horizon 1.1 », 29 janvier 2026, lu le 10 novembre 2026 |
| 14 | Complément : modèles publics de février-mars 2026 : environ 12 h de travail d’expert réussies une fois sur deux (intervalle de 5 h à 61 h), environ 1 h 30 quatre fois sur cinq (50 min à 2 h 40) ; mesure non fiable au-dessus de 16 h | Confirmé | METR, « Frontier Risk Report (February to March 2026) », 19 mai 2026, lu le 10 novembre 2026 |
| 15 | Complément : à qualité égale, le coût d’usage baisse d’environ 47 % par trimestre depuis 2023, soit 13 fois par an ; plus vite juste après qu’un niveau est atteint (66 % par trimestre), deux fois moins vite deux ans après (32 %) ; cinq bancs d’essai (mathématiques, sciences, jeux) | Confirmé | Epoch AI, « The plunging price of thought », 22 septembre 2026, lu le 10 novembre 2026 |

### Corrections à appliquer

1. § 1.1, « 5 172 agents » → « 5 179 agents dans la version de travail (NBER w31161) ; l’effectif de la version publiée n’a pas été relu ».
2. § 1.1, « +15 % … dans la version publiée » : interne seulement, « non relu ». Dans un document client : « +14 % en moyenne (NBER, 2023 ; publié en 2025) ».
3. § 1.2, « Publication en revue … [À confirmer] » → « Version publiée : Organization Science, vol. 37, n° 2, mars 2026, p. 403-423 (notice Crossref) ».
4. § 1.2, « 19 points de pourcentage de bonnes réponses en moins » → « 19 % de chances en moins de produire une solution correcte (résumé de la version publiée) ».
5. § 1.2, « qualité jugée plus de 40 % supérieure » → « qualité nettement meilleure (version publiée) ; le chiffre de 40 % vient du document de travail, non relu ».
6. § 1.6, ligne « Tâche hors frontière » : « −19 points de bonnes réponses » → « 19 % de solutions correctes en moins ».
7. « Règle de lecture » (§ 1) : dire ce que sont les deux bornes. « −19 % » : 19 % de temps en plus (METR 2025) ; « +56 % » : tâche finie 55,8 % plus vite (Peng et al. 2023). Ce ne sont pas les mêmes mesures : la fourchette dit l’étendue, ce n’est pas une moyenne.
8. « En bref » : vide ; la conclusion ci-dessus le remplace.

### Compléments essentiels (parties manquantes)

**Durée des tâches menées par les agents.** METR mesure la longueur, en temps de travail d’un expert humain, des tâches qu’un modèle réussit seul une fois sur deux. Elle double environ tous les sept mois depuis 2019, plus vite depuis 2024 (89 jours). Début 2026 : environ 12 h à 50 % de réussite, environ 1 h 30 à 80 % (lignes 13 et 14). Limites dites par METR : tâches de logiciel et de recherche, bien définies, faciles à noter ; peu de longues tâches chronométrées sur des personnes ; au-dessus de 16 h, la mesure ne tient plus. Ce n’est ni une mesure sur un travail d’administration, ni le temps pendant lequel une IA travaille seule chez un client. Pour nous : confier à l’agent des tâches courtes et vérifiables, relues par une personne.

**Baisse du coût.** Epoch AI : à qualité égale, environ 13 fois moins cher par an depuis 2023 ; la baisse est la plus forte juste après qu’un niveau est atteint, puis ralentit (ligne 15). Elle ne vaut ni pour « le meilleur modèle du moment », ni pour le matériel (k13a relève des hausses de prix en 2026). Pour nous : le paiement à l’usage devient moins cher chaque année ; c’est une raison de plus de ne pas acheter de matériel avant un besoin mesuré, sauf pour la confidentialité.

**Comment mesurer le « jusqu’à cent fois »** [Estimation ; méthode proposée] :
- Indicateurs : documents lus et saisis par heure (première lecture) ; documents vérifiés par heure de travail d’une personne (chaîne complète) ; erreurs trouvées à la vérification ; coût par document.
- Base : une personne qui lit et saisit les mêmes documents un par un, chronométrée sur un lot représentatif (par exemple 20 à 30 devis) avant l’essai. L’hypothèse « environ six devis par heure » (dix minutes par devis) est remplacée par cette mesure.
- Machine : le même lot traité en parallèle ; on note le temps total, le coût et les erreurs.
- Chaîne : le gain réel est le rapport entre documents vérifiés par heure de personne, avec et sans l’outil. Si vérifier un devis lu par la machine prend deux minutes, contre dix pour une lecture complète, le gain plafonne à cinq fois ; à une minute, à dix fois. D’où « cinq à dix fois ».
- Limite : « cent fois » ne vaut que pour la première lecture, sur des documents répétitifs, traités en parallèle. Il dépend des plafonds d’usage du fournisseur (k13c) et de la qualité de lecture sur les pièces réelles.

### Sûr à reprendre

1. « Selon la tâche, les études publiées mesurent de −19 % (des développeurs expérimentés ralentis sur leurs propres projets) à +56 % (une tâche de programmation courte et bien définie). » — METR, juillet 2025 ; Peng et al., février 2023. **Page « moyens », annexe, fiche 09.**
2. « Des développeurs expérimentés ont mis 19 % de temps en plus avec l’IA, tout en croyant en avoir gagné 20 %. » — METR, arXiv 2507.09089, juillet 2025. **Annexe ; oral.**
3. « En assistance clientèle : +14 % de demandes résolues par heure en moyenne, +34 % pour les débutants, presque rien pour les plus expérimentés. » — Brynjolfsson, Li et Raymond, NBER 2023, publié en 2025. **Annexe.**
4. « Des consultants aidés par l’IA ont terminé 12 % de tâches en plus, 25 % plus vite ; sur une tâche choisie hors de portée de l’outil, ils ont produit 19 % de solutions correctes en moins. » — Dell’Acqua et al., Organization Science, mars 2026. **Annexe.**
5. « Sur des tâches de logiciel, la longueur des tâches qu’un agent d’IA réussit seul une fois sur deux double environ tous les sept mois depuis 2019. C’est une mesure, pas une promesse. » — METR, 29 janvier 2026. **Fiche 12, annexe.**
6. « Début 2026, un agent réussissait seul, quatre fois sur cinq, une tâche de logiciel d’environ une heure et demie de travail d’expert. Une personne relit. » — METR, 19 mai 2026. **Annexe.**
7. « À qualité égale, le coût d’usage de l’IA a baissé d’environ 47 % par trimestre depuis 2023, soit environ treize fois par an ; la baisse ralentit avec le temps et n’est pas garantie. » — Epoch AI, 22 septembre 2026. **Annexe.**
8. **Interne seulement** : les chiffres d’entreprise (89 %, +0,2 % à +1,4 %) ; l’étude danoise ; « 12 h une fois sur deux » (il se lit facilement « l’IA travaille douze heures seule ») ; le +15 % de la version publiée ; les +43 % et +17 %.

### Ce qui reste inconnu

- Aucune étude lue ne mesure « dix fois » ou « cent fois » sur un travail humain complet : « cent fois » reste une hypothèse de débit sur la première lecture.
- Le temps réel de lecture et de vérification d’un devis par une personne, chez GianLuca Carlone : à chronométrer pendant l’essai.
- La qualité de lecture des outils sur ses pièces (scans, écritures à la main, tableaux) et leur taux d’erreurs.
- Les chiffres de la version publiée de Brynjolfsson et al. (15 %, 5 172) ; l’intervalle et l’effectif de Peng et al. ; les chiffres du document de travail de Dell’Acqua et al.
- Une mesure de durée des tâches sur un travail d’administration : aucune trouvée.
- La suite des tendances de METR et d’Epoch AI.

