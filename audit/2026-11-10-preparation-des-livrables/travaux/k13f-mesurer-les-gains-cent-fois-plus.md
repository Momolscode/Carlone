# « Jusqu'à cent fois plus » : où l'IA multiplie vraiment la capacité, où elle ne la multiplie pas, et comment le mesurer

Note de travail interne — sources publiques consultées le 10 novembre 2026 — ce n'est pas un avis juridique, fiscal ou d'investissement

*Auteur : chercheur (note k13f) pour le dixième livrable (BRIEF-2, § 9.2). Ce n'est pas le livrable. Les faits rapportés par Morgan sur GianLuca Carlone ne sont pas vérifiés auprès du client. Étiquettes : [Officiel] page d'un éditeur ou d'une autorité ; [Prix public daté] ; [Mesure publiée] article de recherche ou mesure d'un laboratoire ; [Source professionnelle] presse, blog, agrégateur ; [Estimation] calcul de cette note ; [À confirmer].*

## En bref

(provisoire, complété en fin de rédaction)

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

