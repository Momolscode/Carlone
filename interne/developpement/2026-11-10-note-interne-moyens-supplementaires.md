# Note interne — « Ce que des moyens supplémentaires nous permettraient d’accomplir »

Document interne — ne pas transmettre à GianLuca Carlone · 10 novembre 2026 · Ce document n’est pas un avis juridique, fiscal ou d’investissement.

## En bref

1. Deux projets client existent : la page (`pour-carlone/developpement/2026-11-10-ce-que-des-moyens-supplementaires-permettraient.md`, une page A4, contrôle sans erreur) et l’annexe chiffrée (`pour-carlone/developpement/2026-11-10-annexe-comparaisons-et-calculs.md`).
2. **Les chiffres viennent de notes de recherche pas encore vérifiées** (`audit/2026-11-10-preparation-des-livrables/travaux/k13a` à `k13f`, interrompues le 10 novembre). Avant de montrer quoi que ce soit, revérifier chaque prix sur sa page d’origine.
3. L’ambition « cent fois plus » est tenue honnêtement : vraie seulement pour la première lecture de documents répétitifs traités en parallèle ; cinq à dix fois sur la chaîne complète avec vérification humaine ; quelques dizaines de pour cent ailleurs (études publiées) ; rien sur la relation et la décision. Toute la page repose sur cette distinction : c’est elle qui rend l’ambition crédible.
4. **Recommandation matériel** : pas de DGX Station (90 000 à 170 000 € HT, 1 600 W) sans besoin mesuré ; le paiement à l’usage et la location suffisent au départ ; une machine de type DGX Spark (environ 5 500 à 7 500 € HT relevés en France) se justifie seulement pour garder ses documents confidentiels chez lui, achetée au nom de sa société.
5. **Le levier le plus fort est humain** : la continuité (aujourd’hui, si l’un de nous manque, tout s’arrête) et la capacité (une étape et un essai à la fois).

## 1. Les formes possibles d’un soutien (jamais dans un document client)

| Forme | Avantage | Risque | À faire valider par |
| --- | --- | --- | --- |
| Commandes plus larges ou plus nombreuses | La plus simple ; aucune dépendance de capital | Dépendance à un seul client | — |
| Matériel acheté par sa société, installé chez lui, à son nom | Cohérent avec la règle « comptes, données et outils à son nom » ; ses données restent chez lui | Entretien et sécurité à prévoir par contrat | Expert-comptable (amortissement), avocat (contrat d’usage) |
| Avance sur un contrat de plusieurs mois | Trésorerie | Engagement de livrer ; remboursement si arrêt | Avocat, expert-comptable |
| Prise de participation dans Marwin Tech | Moyens durables | Conflit d’intérêts client et actionnaire ; perte d’indépendance ; statuts et pacte à revoir ; valorisation d’une société pas encore immatriculée | Avocat, expert-comptable |
| Aides publiques (Bpifrance, région, apprentissage) | Pas de dépendance au client | Délais, conditions | Expert-comptable ; organismes concernés |

La proposition de cadrage du 9 novembre dit déjà : « Toute autre relation (locaux, emploi, participation) ferait l’objet d’un accord séparé, sans lien avec nos honoraires. » Cette règle tient.

## 2. Repères relevés (non vérifiés, à revérifier)

- DGX Spark : 128 Go de mémoire unifiée, 240 W ; prix relevés en France de 5 500 € HT à 9 000 € TTC selon le revendeur ; prix en forte hausse depuis le lancement (note k13a, § 1).
- DGX Station GB300 : 748 Go de mémoire, 1 600 W ; aucun prix français ; 90 000 à 170 000 € HT chez des revendeurs européens (k13a, § 2).
- Station avec une carte RTX PRO 6000 : environ 18 000 à 25 000 € HT au total (k13a, § 3, estimation).
- Location en France : 0,75 € HT de l’heure (L4) à 2,80 € HT (H100) chez OVHcloud ; 0,79 € HT (L4) chez Scaleway (k13b, § 1).
- Abonnements : offres individuelles supérieures 100 à 200 dollars par mois ; offres d’équipe renforcées 100 à 125 dollars par personne et par mois (k13c, § 1).
- Personnes : environ 26 900 € par an de coût employeur pour 2 000 € brut par mois, 43 900 € pour 2 800 € ; apprenti environ 1 000 € par mois la première année, aide de 2 000 à 4 500 € selon le diplôme ; président de SAS : environ 3 500 € de coût pour 2 000 € net, sans droit au chômage (k13d, estimations).
- Études sur les gains : +14 % à +34 % (assistance clientèle), +25 % à +56 % (tâches définies), −19 % (développeurs expérimentés, 2025) ; aucune étude ne mesure « dix fois » ou « cent fois » en général (k13f, § 1).

## 3. Décisions pour Morgan et Mathys

1. Montrer la diapositive dans la version 12 : ☐ oui, après le prix et la décision ☐ en annexe seulement ☐ non. Recommandation : oui, après la décision, comme une perspective, sans parler d’argent en séance (feuille de décisions, partie 4).
2. Valider la phrase « jusqu’à cent fois plus vite, sur la première lecture de documents répétitifs » et l’engagement de la mesurer pendant l’essai.
3. Faire revérifier les prix de l’annexe avant toute remise.

## 4. Reste à faire

- Terminer et vérifier les notes k13a à k13f (outil : `outils/2026-11-10-orchestration/workflows/prep-moyens.js`).
- Écrire la diapositive de la version 12 (gabarit `g-tableau` ou `g-cartes-3`, titre de 55 signes au plus).
