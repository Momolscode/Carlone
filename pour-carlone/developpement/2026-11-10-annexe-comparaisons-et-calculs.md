# Annexe — comparaisons et calculs

PROJET non envoyé — à valider par Morgan Olsen et Mathys Couet

Annexe de la page « Ce que des moyens supplémentaires nous permettraient d’accomplir ». Prix et caractéristiques lus sur des pages publiques le 10 novembre 2026 (chaque prix porte sa source et sa date), à revérifier avant toute décision : les prix du matériel ont fortement varié en 2025 et 2026. Les totaux sont des estimations à valider. Ce document n’est ni un devis ni un conseil d’investissement.

## 1. Le calcul : cinq manières de faire

| Option | Ce que c’est | Prix public relevé | Contraintes | Pour quoi faire |
| --- | --- | --- | --- | --- |
| Paiement à l’usage d’un modèle en ligne | On paie au volume traité | Claude Opus 5.5 : 4 $ en entrée et 20 $ en sortie par million de jetons, hors taxes ; Claude Sonnet 5.5 : 2 $ et 10 $ (claude.com/pricing, 10 novembre 2026). Soit environ 0,02 $ à 0,04 $ pour lire un devis de trois pages (estimation à valider) | Les documents partent chez l’éditeur, parfois hors de l’Union européenne : à encadrer par contrat | Petits et moyens volumes ; en général le moins cher au début |
| Location d’une carte de calcul à l’heure, en France | Une machine puissante louée, sans engagement | hors taxes, de l’heure : de 0,75 € (carte L4) à 2,80 € (carte H100) chez OVHcloud (page « Tarifs Public Cloud ») ; environ 0,79 € (L4) à 2,87 € (H100) chez Scaleway, facturés à la minute (catalogue public des prix) ; lus le 10 novembre 2026 | Il faut la piloter ; les données partent chez l’hébergeur | Pointes de travail, essais, réglage d’un modèle |
| NVIDIA DGX Spark (ou machine équivalente d’un autre constructeur) | Petit ordinateur d’IA de bureau (15 × 15 cm), 128 Go de mémoire ; NVIDIA indique des modèles jusqu’à 200 milliards de paramètres | prix conseillé par NVIDIA passé de 3 999 $ au lancement (octobre 2025) à 4 699 $ le 23 février 2026, hors taxes américaines (forum développeurs NVIDIA) ; prix actuel en euros à demander à un revendeur | Modèles ouverts seulement, moins performants que les modèles de pointe en ligne ; installation, sécurité et entretien | Traiter vos documents confidentiels chez vous |
| Autres machines de bureau (Apple Mac Studio M5 Ultra ; station avec une carte NVIDIA RTX PRO 6000 de 96 Go) | Mêmes usages, avec plus de mémoire ou de vitesse selon le modèle | Mac Studio M5 Ultra : à partir de 6 599 € toutes taxes comprises, avec 96 Go (Apple, 25 août 2026) ; station RTX PRO 6000 : prix à confirmer | Carte RTX PRO 6000 : 600 W à elle seule (fiche NVIDIA) ; mêmes limites de modèles | À comparer sur vos documents avant tout achat |
| NVIDIA DGX Station | Station de calcul très puissante, 748 Go de mémoire, jusqu’à 1 600 W | environ 90 000 à 171 500 € hors taxes chez un revendeur allemand, selon le constructeur (guide d’achat BuyZero, 5 novembre 2026) | Ligne électrique dédiée conseillée (à faire valider par un électricien), chaleur d’un radiateur électrique, compétences | Recherche et réglage de grands modèles ; surdimensionnée pour les usages décrits ici |

Un jeton est l’unité de texte que facturent les éditeurs : un fragment de mot.

**Notre lecture.** Au début, le paiement à l’usage et la location suffisent pour les usages envisagés (lire, classer, résumer, comparer, rappeler) ; à qualité égale, leur coût baisse vite (§ 3). Une machine de bureau se justifie si des documents confidentiels doivent rester chez vous. Une DGX Station ne se justifie qu’après un besoin mesuré qu’une machine plus petite ne couvre pas.

- **Données.** Pour des données personnelles ou des documents sensibles, la CNIL juge « généralement plus opportun et plus sécurisé » un déploiement sur site (CNIL, questions-réponses sur l’IA générative, 18 juillet 2024). À deux conditions : les logiciels installés n’envoient rien en ligne, et la sécurité de la machine est tenue.
- **Qualité.** Selon l’indice indépendant Artificial Analysis (version 5, 27 octobre 2026), les modèles ouverts téléchargeables les mieux notés obtiennent 32 points, contre 58 pour le premier modèle fermé au lancement de l’indice. Une machine locale convient au tri, à l’extraction et au résumé ; le raisonnement difficile reste mieux fait en ligne.
- **Énergie et bruit.** Une DGX Spark consomme environ 160 W en pleine charge (mesure de Tom’s Hardware, 27 janvier 2026). Jour et nuit, cela ferait environ 1 400 kWh par an, soit moins de 300 € toutes taxes comprises à 0,2001 € le kWh (tarif Bleu, option Base, 1er août 2026 ; Selectra, 17 juillet 2026) : estimation à valider selon le contrat du lieu. NVIDIA déclare pour elle une puissance acoustique de 35 dB(A) en pleine charge et de 19 dB(A) au repos (fiche NVIDIA, norme ECMA-109).

## 2. Les outils d’IA

| Niveau | Prix public relevé | Ce que cela ajoute |
| --- | --- | --- |
| Offres individuelles d’entrée | environ 15 à 20 dollars hors taxes par personne et par mois (Mistral Pro 14,99 $ ; Claude Pro 17 $ en paiement annuel, 20 $ en mensuel) | Accès aux assistants, limites d’usage serrées |
| Offres individuelles supérieures | 100 à 200 dollars hors taxes par personne et par mois (Claude Max et Ultra) | Cinq à dix fois plus d’usage que l’offre d’entrée, sessions de travail plus longues |
| Offres d’équipe | place simple : 20 $ hors taxes par personne et par mois en paiement annuel, 25 $ en mensuel ; place renforcée : 100 $, ou 125 $ en mensuel (Claude Team) | Administration des comptes ; vos contenus ne servent pas, par défaut, à entraîner les modèles |

Sources : pages de tarifs des éditeurs (claude.com/pricing, mistral.ai/pricing), lues le 10 novembre 2026.

## 3. Les gains : ce qui est mesuré, ce qui est à mesurer

| Tâche | Indicateur | Base de comparaison | Gain | Statut |
| --- | --- | --- | --- | --- |
| Première lecture d’un devis de trois pages et saisie dans un tableau | devis lus et saisis par heure | une personne seule, qui les lit un par un : environ six par heure (estimation à mesurer) | jusqu’à cent fois plus, en traitement parallèle | hypothèse à évaluer sur vos documents |
| La même chaîne, vérification par une personne comprise | devis lus et vérifiés par heure | une personne seule | cinq à dix fois plus | hypothèse à évaluer |
| Tâche courte et bien définie (conseil, programmation) | temps passé | même tâche sans IA | de 25 % à 56 % plus vite | mesuré (Dell’Acqua et al., 2023, publié en 2026 ; Peng et al., 2023) |
| Réponses écrites à des clients (assistance) | demandes résolues par heure | sans l’outil | +14 % en moyenne, +34 % pour les débutants | mesuré (Brynjolfsson, Li et Raymond, 2023, publié en 2025) |
| Tâche choisie hors de portée de l’outil (conseil) | solutions correctes | même tâche sans IA | 19 % de solutions correctes en moins | mesuré (Dell’Acqua et al., publié en 2026) |
| Développeurs expérimentés, sur leurs propres projets | temps passé | sans IA | 19 % de temps en plus en 2025, en croyant en avoir gagné 20 % ; gain possible mais mal mesuré en 2026 | mesuré (METR, juillet 2025) ; mesure de 2026 jugée peu fiable par ses auteurs (METR, février 2026) |

**La leçon.** Les grands multiplicateurs existent seulement sur des tâches répétitives que l’on peut traiter en parallèle. Ailleurs, selon la tâche, les études publiées mesurent de −19 % (19 % de temps en plus) à +56 % (une tâche finie 56 % plus vite) : quelques dizaines de pour cent, parfois un recul. C’est pourquoi nous mesurerons chaque tâche avant et après l’essai.

**Deux tendances mesurées, sans promesse.** Sur des tâches de logiciel, la longueur des tâches qu’un agent d’IA réussit seul une fois sur deux double environ tous les sept mois depuis 2019 ; début 2026, il réussissait seul, quatre fois sur cinq, une tâche d’environ une heure et demie de travail d’expert (METR, 29 janvier et 19 mai 2026). À qualité égale, le coût d’usage de l’IA a baissé d’environ 47 % par trimestre depuis 2023, soit environ treize fois par an (Epoch AI, 22 septembre 2026). Ces rythmes ne sont pas garantis et la baisse ralentit avec le temps. D’où notre règle : des tâches courtes et vérifiables, relues par une personne.

## 4. Trois chemins, en ordre de grandeur

| | Moyens actuels | Renforcement ciblé | Développement ambitieux |
| --- | --- | --- | --- |
| Équipe | deux associés | deux associés rémunérés, un collaborateur ou un apprenti | quatre à six personnes |
| Calcul | paiement à l’usage | paiement à l’usage, location ponctuelle, une machine de bureau chez vous si elle est utile | station de calcul dédiée, si un besoin mesuré le justifie |
| Investissement de départ | aucun | environ 6 000 à 10 000 € hors taxes (une machine de bureau et sa mise en service, si elle est utile) | environ 11 000 à 25 000 € hors taxes pour une station de calcul ; une DGX Station reste hors de proportion |
| Dépenses courantes, outils | quelques dizaines d’euros par mois | quelques centaines d’euros par mois | environ un à deux milliers d’euros par mois, selon le calcul loué |
| Dépenses courantes, personnes | — | l’essentiel du coût | l’essentiel du coût |
| Ce que cela permet | une étape et un essai à la fois | plusieurs chantiers en parallèle, relève assurée | un laboratoire, des prototypes, plusieurs clients |
| Première priorité | le cadrage | mesurer les premiers gains, former | ce que les mesures auront montré |

**Laboratoire.** Applications proches (quelques mois) : des prototypes d’outils pour vos lieux, construits à partir de vos documents. Pistes de recherche, sans date : un outil qui jugerait seul l’état d’une œuvre ou d’un bâtiment, un agent qui agirait sans validation humaine. La robotique reste « plus tard, sous conditions » (financement, sécurité, partenaires).

Toutes ces sommes sont des estimations à valider. Ce qui touche à la fiscalité, à l’amortissement d’un matériel ou à l’emploi est à faire valider par vos professionnels (expert-comptable, avocat).
