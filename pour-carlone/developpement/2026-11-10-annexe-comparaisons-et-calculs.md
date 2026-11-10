# Annexe — comparaisons et calculs

PROJET non envoyé — à valider par Morgan Olsen et Mathys Couet

Annexe de la page « Ce que des moyens supplémentaires nous permettraient d’accomplir ». Prix et caractéristiques relevés sur des pages publiques le 10 novembre 2026, à revérifier avant toute décision : les prix du matériel ont fortement varié en 2025 et 2026. Les totaux sont des estimations à valider. Ce document n’est ni un devis ni un conseil d’investissement.

## 1. Le calcul : quatre manières de faire

| Option | Ce que c’est | Prix relevé | Contraintes | Pour quoi faire |
| --- | --- | --- | --- | --- |
| Paiement à l’usage d’un modèle hébergé en Europe | On paie au volume traité | de 0,04 € à 7,50 € hors taxes par million de jetons selon le modèle (pages de tarifs d’hébergeurs européens) | Les documents partent chez l’hébergeur, sous contrat | Petits et moyens volumes ; c’est presque toujours le moins cher |
| Location d’une carte de calcul à l’heure, en France | Une machine puissante louée, sans engagement | de 0,75 € à 2,80 € hors taxes de l’heure selon la carte (pages « tarifs » d’OVHcloud et de Scaleway) | Il faut la piloter ; les données partent chez l’hébergeur | Pointes de travail, essais, réglage d’un modèle |
| NVIDIA DGX Spark (ou modèle équivalent d’un autre constructeur) | Petit ordinateur d’IA de bureau, 128 Go de mémoire, environ 240 W | environ 5 500 à 7 500 € hors taxes selon le revendeur (prix relevés en France) | Modèles ouverts seulement, moins forts que les meilleurs modèles en ligne ; installation et entretien | Traiter vos documents confidentiels chez vous |
| NVIDIA DGX Station | Station de calcul très puissante, 748 Go de mémoire, 1 600 W | environ 90 000 à 170 000 € hors taxes (revendeurs européens ; aucun prix français relevé) | Ligne électrique dédiée, bruit, chaleur, compétences | Recherche et réglage de grands modèles ; surdimensionnée pour vos besoins actuels |

**Notre lecture.** Pour vos usages (lire, classer, résumer, comparer, rappeler), le paiement à l’usage et la location suffisent au début. Une machine de type DGX Spark se justifie si vos documents confidentiels doivent rester chez vous. Une DGX Station ne se justifie qu’après un besoin mesuré qu’une machine plus petite ne couvre pas.

## 2. Les outils d’IA

| Niveau | Prix public relevé | Ce que cela ajoute |
| --- | --- | --- |
| Offres individuelles d’entrée | environ 15 à 25 dollars par personne et par mois | Accès aux assistants, limites d’usage serrées |
| Offres individuelles supérieures | 100 à 200 dollars par personne et par mois | Cinq à dix fois plus d’usage, tâches longues, agents de programmation |
| Offres d’équipe (place renforcée) | environ 100 à 125 dollars par personne et par mois | Administration, données non utilisées pour l’entraînement par défaut, accord de traitement des données |

Sources : pages de tarifs des éditeurs (claude.com/pricing, chatgpt.com/pricing, mistral.ai/pricing), lues le 10 novembre 2026.

## 3. Les gains : ce qui est mesuré, ce qui est à mesurer

| Tâche | Indicateur | Base de comparaison | Gain | Statut |
| --- | --- | --- | --- | --- |
| Première lecture d’un devis de deux pages et saisie dans un tableau | devis traités par heure | une personne seule, environ six par heure | jusqu’à cent fois plus, en traitement parallèle | hypothèse à évaluer sur vos documents |
| La même chaîne, vérification par une personne comprise | devis traités et vérifiés par heure | une personne seule | cinq à dix fois plus | hypothèse à évaluer |
| Tâche de rédaction ou d’analyse bien définie | temps passé | même tâche sans IA | de 25 % à 56 % plus vite | mesuré par des études publiées (2023) |
| Tâche répétitive faite par une personne nouvelle dans le métier | dossiers traités par heure | sans l’outil | de 14 % à 34 % | mesuré (étude publiée, 2025) |
| Travail d’expert dans un contexte qu’il connaît bien | temps passé | sans IA | de −19 % à légèrement positif | mesuré (études publiées, 2025 et 2026) |

**La leçon.** Les grands multiplicateurs existent seulement sur des tâches répétitives que l’on peut traiter en parallèle. Le reste progresse de quelques dizaines de pour cent, parfois pas du tout. C’est pourquoi nous mesurons chaque tâche avant et après.

## 4. Trois chemins, en ordre de grandeur

| | Moyens actuels | Renforcement ciblé | Développement ambitieux |
| --- | --- | --- | --- |
| Équipe | deux associés | deux associés rémunérés, un collaborateur ou un apprenti | quatre à six personnes |
| Calcul | paiement à l’usage | paiement à l’usage, location ponctuelle, une machine de type DGX Spark chez vous si utile | station de calcul dédiée, si un besoin mesuré le justifie |
| Investissement de départ | aucun | environ 6 000 à 10 000 € hors taxes | environ 25 000 € hors taxes et plus selon la machine |
| Dépenses courantes, outils | quelques dizaines d’euros par mois | quelques centaines d’euros par mois | environ un à deux milliers d’euros par mois |
| Dépenses courantes, personnes | — | l’essentiel du coût | l’essentiel du coût |
| Ce que cela permet | une étape et un essai à la fois | plusieurs chantiers en parallèle, relève assurée | un laboratoire, des prototypes, plusieurs clients |
| Première priorité | le cadrage | mesurer les premiers gains, former | ce que les mesures auront montré |

Toutes ces sommes sont des estimations à valider. Ce qui touche à la fiscalité, à l’amortissement d’un matériel ou à l’emploi est à faire valider par vos professionnels (expert-comptable, avocat).
