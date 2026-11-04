# SAS ou SARL : comparaison sur les mêmes hypothèses économiques

**Document interne.** Il contient des coûts, des marges, des rémunérations visées et des probabilités : il ne doit pas être transmis à GianLuca Carlone (audit-work/strategie-retenue.md:787-789).

Produit le 4 novembre 2026 par `modele_financier.py` (même dossier), qui contient tous les paramètres, leur code et leur source. Pour changer une hypothèse, modifier le paramètre en tête du script et le relancer. « audit-work/ » désigne le dossier de travail de l'audit (hors dépôt) ; les autres chemins renvoient au dépôt (commit 7b46602).

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] mesure ; [IN] inconnu. **Tous les résultats chiffrés sont des [ES]**, arrondis à la centaine d'euros (à la dizaine pour les prix par JP) : un total peut différer de 100 à 200 € de la somme de ses lignes arrondies. Les fourchettes combinent frais bas et coefficient social bas, puis frais hauts et coefficient haut.

**Impôt sur le revenu non calculé** : les situations fiscales des foyers de Morgan Olsen et de Mathys Couet sont [IN] (audit-work/rj-R1-structures.md:15 ; audit-work/syn-droit.md:93). Tous les nets sont « avant impôt sur le revenu ».


## 0. Conclusion

- **Recommandation inchangée : SAS à l'IS** [PR] (audit-work/strategie-retenue.md:543 ; audit-work/syn-droit.md:209-235), à confirmer par une simulation officielle de l'expert-comptable.
- À enveloppe égale, la SARL (deux cogérants TNS) laisse plus de net : en central, 15 000 € contre 11 100 à 12 500 € par associé sur les neuf mois rémunérés, soit 2 600 à 3 900 € de plus [ES].
- Mais la SARL coûte des cotisations même sans rémunération (forfaits de première année, minimum ensuite), protège moins (indemnités, retraite complémentaire), gêne l'entrée d'un investisseur et bloque plus vite à 50/50. Or, au 4 novembre, **aucune rémunération n'est financée par un contrat signé** [FV] : c'est le cas où la SAS est la plus sûre (audit-work/syn-droit.md:216).
- La SARL ne redevient préférable que si les trois conditions de audit-work/strategie-retenue.md:562 sont réunies : aucun investisseur avant 24 mois, un contrat signé d'au moins 120 000 € par an, aucun associé salarié ailleurs.


## 1. Hypothèses identiques pour les deux formes

- Même chiffre d'affaires, mêmes frais, même démarrage, même réserve, même IS : l'**enveloppe de rémunération** (coût total pour la société) est celle que calcule le modèle pour chaque scénario (`scenarios.md`, section 3). Seul change le partage de cette enveloppe entre cotisations et net.
- Deux associés à 50/50, tous deux dirigeants. SARL : cogérants, donc TNS [FV] (audit-work/syn-droit.md:109) ; SAS : président et directeur général assimilés salariés [FV] (audit-work/rj-R1-structures.md:23).
- SAS : coût = 1,7 à 1,9 fois le net [HY] (audit-work/syn-droit.md:98). SARL : barème F38152 « revenus 2025 », assiette à 74 % du coût, plancher et plafond de l'abattement ignorés [ES] (audit-work/syn-droit.md:97 ; audit-work/ver-R1-structures.md:20).
- IS identique (rémunérations et cotisations déductibles dans les deux cas) : 15 % jusqu'à 42 500 € [FV] (audit-work/syn-droit.md:142).
- Pas d'ACRE, d'ARE, d'ARCE, de prévoyance ni de mutuelle ; **impôt sur le revenu non calculé** [IN].


## 2. Résultats par scénario (neuf mois rémunérés, mois 4 à 12)

| Scénario | Enveloppe mensuelle (deux associés) | SAS : net par associé sur 9 mois | SAS : net par mois | SARL : net par associé sur 9 mois | SARL : net par mois | Écart SARL − SAS (coefficient 1,8) | SARL : régularisation en année 2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Prudent | 2 100 à 2 700 € | 5 000 à 7 300 € | 600 à 800 € | 6 800 à 8 800 € | 800 à 1 000 € | 1 500 à 1 900 € | −800 à 0 € |
| Central | 4 300 à 5 100 € | 10 100 à 13 400 € | 1 100 à 1 500 € | 13 600 à 16 200 € | 1 500 à 1 800 € | 3 000 à 3 500 € | 1 900 à 3 000 € |
| Ambitieux | 6 200 à 7 300 € | 14 700 à 19 400 € | 1 600 à 2 200 € | 19 700 à 23 200 € | 2 200 à 2 600 € | 4 200 à 4 900 € | 4 600 à 6 200 € |


Fourchettes : frais hauts (× 1,25) et démarrage haut, puis frais bas (× 0,8) et démarrage bas ; pour la SAS, en plus, coefficient 1,9 puis 1,7. Une régularisation négative est un remboursement des forfaits trop payés [ES].


## 3. Sans rémunération : ce que coûte chaque forme

| Situation | SARL (deux cogérants TNS) | SAS (président et directeur général) | Source |
| --- | --- | --- | --- |
| Mois 1 à 3 (aucune rémunération) | Forfaits de début d'activité ≈ 3 600 € par gérant et par an, régularisés ensuite ; minimum ≈ 1 300 € par an et par gérant | 0 €, sans droit social | [FV/ES] audit-work/syn-droit.md:111 |
| Variante basse du prudent (arrêt après le cadrage) | Forfaits ≈ 7 200 € avancés pour les deux la première année, ramenés ensuite au minimum (≈ 2 500 € par an pour les deux), sans aucun revenu | 0 € | [ES] audit-work/syn-droit.md:182 |
| Associé salarié ailleurs | Le gérant reste redevable du minimum | Mandat non rémunéré possible sans cotisation | [FV] audit-work/syn-droit.md:159 |
| Trésorerie sociale | Forfaits l'année 1, régularisation l'année 2 : à provisionner | Cotisations payées chaque mois avec le salaire, pas de régularisation | [ES] audit-work/syn-droit.md:187-195 |


## 4. Dividendes

| Scénario (SAS) | Enveloppe des mois 4 à 12 versée en dividendes au lieu de salaires (deux associés) | IS supplémentaire | Dividende net par associé après PFU de 31,4 % (donc après IR) | Pour comparaison : salaire net SAS par associé, avant IR (coefficient 1,9 à 1,7) | Variante non comparable : tout le bénéfice distribué, réserve conservée, net après PFU |
| --- | --- | --- | --- | --- | --- |
| Prudent | 22 200 € | 3 300 € | 6 500 € | 5 900 à 6 500 € | 6 200 € |
| Central | 42 400 € | 8 000 € | 11 800 € | 11 100 à 12 500 € | 13 700 € |
| Ambitieux | 61 500 € | 13 700 € | 16 400 € | 16 200 à 18 100 € | 19 000 € |


Lecture [ES] : **à ressources égales**, le dividende net après PFU (qui comprend 12,8 % d'IR) est à peu près égal au salaire net de SAS **avant** IR au coefficient central de 1,8 (central : 11 800 € contre 11 800 €) ; il ne gagne que l'IR que supporterait le salaire. En ambitieux, où une partie du bénéfice passe à 25 % d'IS, il fait moins bien (16 400 € contre 17 100 €). La dernière colonne distribue en plus l'excédent des mois 1 à 3 que les scénarios « salaire » laissent dans la société : elle ne compare pas des ressources égales et ne doit pas servir d'argument. Le dividende n'est versé qu'**après la clôture et l'approbation des comptes** (au plus tôt au printemps 2028 pour l'exercice 2027 [HY]), il n'ouvre **aucun droit social** (ni retraite, ni indemnités) et il dépend du bénéfice (audit-work/syn-droit.md:129-132, 144). Il ne finance donc pas la vie des associés pendant la première année ; un mélange « petit salaire et dividendes » est à faire simuler par l'expert-comptable. IS calculé avec le seuil de 42 500 € sur douze mois : un premier exercice de 13 ou 14 mois relèverait ce seuil au prorata et réduirait l'IS de ce tableau de 350 à 700 € [ES]. En SARL, les dividendes des cogérants au-delà de 10 % du capital, des primes et des comptes courants supportent les cotisations TNS : pas de levier avec un petit capital [FV] (audit-work/syn-droit.md:145).


## 5. Contrôle : reproduction de la synthèse juridique

| CA HT annuel (frais = 1/6) | SARL, tout en rémunération (modèle) | SARL (audit-work/syn-droit.md:123-124) | SAS, tout en salaire (modèle) | SAS (audit-work/syn-droit.md:123-124) |
| --- | --- | --- | --- | --- |
| 120 000 € | 34 500 € | ≈ 34 500 € | 26 300 à 29 400 € | 26 300 à 29 400 € |
| 180 000 € | 51 400 € | ≈ 51 400 € | 39 500 à 44 100 € | 39 500 à 44 100 € |


Le modèle reproduit les fourchettes de la synthèse juridique : les deux calculs reposent sur les mêmes barèmes et la même méthode.


## 6. Ce que les chiffres ne disent pas

| Critère | SARL | SAS | Source |
| --- | --- | --- | --- |
| Indemnités journalières maladie | Plafond 65,84 € par jour, 3 jours de carence | Plafond 41,95 € par jour | [FV] audit-work/syn-droit.md:113 |
| Retraite | Régimes des indépendants | Régime général et Agirc-Arrco : en général plus de droits à coût égal | [FV/IN] audit-work/syn-droit.md:114 |
| Chômage | Aucun | Aucun | [FV] audit-work/syn-droit.md:115 |
| Blocage à 50/50 | Décisions ordinaires bloquées sans accord | Médiation, tiers expert, offre alternative prévues aux statuts | [HY] audit-work/syn-droit.md:155 |
| Entrée d'un investisseur (dont GianLuca) | Agrément ; droits de cession de 3 % après abattement | Libre selon les statuts ; 0,1 % | [FV] audit-work/syn-droit.md:165-166 |
| Coût de création (statuts, pacte) | ≈ 1 500 à 4 000 € HT | ≈ 2 000 à 5 000 € HT | [ES] audit-work/syn-droit.md:180 |


## 7. Questions à l'expert-comptable (avant toute décision)

1. Simulations officielles SAS et SARL sur les trois scénarios de `scenarios.md`, avec les taux 2026 définitifs, puis ceux de 2027 (audit-work/syn-droit.md:200).
2. Coût réel d'un président et d'un directeur général rémunérés : taux, réduction dégressive unique, AT/MP (audit-work/syn-droit.md:201).
3. Forfaits TNS de première année si la société est créée fin 2026 ou début 2027, et montant de la régularisation.
4. Régime de TVA (réel normal mensuel ou réel simplifié), date de création et date de clôture.
5. Déductibilité, dans la société, des frais engagés avant l'immatriculation (dont le conseil sur la fuite).
6. ACRE, si l'un des deux associés est éligible (audit-work/syn-droit.md:205).
