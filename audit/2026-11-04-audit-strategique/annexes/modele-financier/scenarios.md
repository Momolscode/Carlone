# Modèle financier : trois scénarios sur douze mois

**Document interne.** Il contient des coûts, des marges, des rémunérations visées et des probabilités : il ne doit pas être transmis à GianLuca Carlone (audit-work/strategie-retenue.md:787-789).

Produit le 4 novembre 2026 par `modele_financier.py` (même dossier), qui contient tous les paramètres, leur code et leur source. Pour changer une hypothèse, modifier le paramètre en tête du script et le relancer. « audit-work/ » désigne le dossier de travail de l'audit (hors dépôt) ; les autres chemins renvoient au dépôt (commit 7b46602).

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] mesure ; [IN] inconnu. **Tous les résultats chiffrés sont des [ES]**, arrondis à la centaine d'euros (à la dizaine pour les prix par JP) : un total peut différer de 100 à 200 € de la somme de ses lignes arrondies. Les fourchettes combinent frais bas et coefficient social bas, puis frais hauts et coefficient haut.

**Impôt sur le revenu non calculé** : les situations fiscales des foyers de Morgan Olsen et de Mathys Couet sont [IN] (audit-work/rj-R1-structures.md:15 ; audit-work/syn-droit.md:93). Tous les nets sont « avant impôt sur le revenu ».


**Trois faits pris comme base** (audit-work/strategie-retenue.md:29-33) :
1. **Aucun contrat, aucune facture, aucune entité payeuse identifiée** [FV négatif]. Le « contrat certain » vaut donc **0 €** dans tous les scénarios : chaque euro de chiffre d'affaires ci-dessous est une hypothèse.
2. **Medhi et BOJ.ART retirés de l'offre** le 4 nov. 2026 à la demande de Morgan [DR] (audit-work/note-point-4-novembre-et-activites.md:25). Seul le diaporama client a été corrigé (11 diapositives) ; l'offre écrite, STRATES v1.1, le vernissage et le PDF de 13 diapositives de la PR n° 1 ne l'ont pas été [FV] (audit-work/strategie-retenue.md:31). Le modèle ne compte **aucune recette ni dépense** pour STRATES, la création, le laboratoire ou le vernissage « signature ».
3. **Fuite de données très probable** (dépôt public FinanceScope/CRM-Carlone) ; délai CNIL de 72 h possiblement échu le 5 nov. si la connaissance date du 2 nov. [ES] (audit-work/strategie-retenue.md:32). Le modèle compte le conseil (avocat ou DPD) dans les frais de démarrage de novembre 2026 [HY] ; une sanction, une action des personnes ou un refus d'assurance ne sont **pas chiffrés** [IN]. Rien ne démarre tant que la fuite n'est pas traitée (audit-work/strategie-retenue.md:53, 660).


## 0. L'essentiel

- **Chiffre d'affaires facturé sur les mois 1 à 12** [ES] : 49 500 € HT (prudent), 89 400 € HT (central), 141 100 € HT (ambitieux, dont 17 500 € encaissés d'un second client). Pondéré par les probabilités de passage, et à condition que le cadrage soit vendu, le central ne vaut plus que 38 300 € HT encaissés.
- **Rémunération soutenable à partir du mois 4**, en SAS, avant IR : ≈ 700 € (600 à 800 €) nets par associé et par mois en prudent, ≈ 1 300 € (1 100 à 1 500 €) en central, ≈ 1 900 € (1 600 à 2 200 €) en ambitieux. Le central est inférieur d'environ 100 € au milieu de la fourchette de la stratégie (1 350 à 1 550 €, audit-work/strategie-retenue.md:511), qui ne comptait ni l'IS ni les délais d'encaissement (audit-work/strategie-retenue.md:518).
- **Même enveloppe en SARL** (deux cogérants TNS) : 1 700 € nets par associé et par mois en central, soit 3 300 € de plus sur les neuf mois rémunérés qu'en SAS (coefficient central), contre une protection sociale moindre et des cotisations dues même sans rémunération (voir `structures.md`).
- **Trésorerie disponible à la fin du mois 12** (apport compris, TVA due déduite) : 12 800 € (prudent), 27 000 € (central), 38 500 € (ambitieux). Une fois la réserve et l'IS mis de côté, il reste 7 100 €, 15 600 € et 20 600 €.
- **Seuil de rentabilité** (frais couverts, réserve comprise, sans rémunération) : 1,9 JP vendues par mois (prudent), 2,5 (central), 4,2 (ambitieux). Pour payer **2 500 € nets par ETP engagé** (soit 2 900 € nets à deux en central), il faudrait 8,8 à 9,5 JP vendues par mois en régime, pour 8,9 prévues et un plafond de 10 : à la limite en régime. Sur l'année, il n'est pas atteint, puisque rien n'est versé avant le mois 4 (audit-work/strategie-retenue.md:511).
- **La TVA n'est jamais du chiffre d'affaires** : elle est collectée à l'encaissement et reversée le mois suivant ; de novembre 2026 au mois 12, le central collecte 17 900 € de TVA, en déduit 3 800 € sur ses achats, en reverse 12 700 € et en doit encore 1 400 €.


## 1. Tableau de synthèse (douze mois de contrat, période préalable comprise)

Lecture : une valeur seule est la valeur centrale ; une plage est la fourchette « frais hauts et coefficient 1,9 » à « frais bas et coefficient 1,7 ». Les coûts et la trésorerie couvrent la période de novembre 2026 à la fin du mois 12 ; le chiffre d'affaires couvre les mois 1 à 12.

| Rubrique | Prudent | Central | Ambitieux |
| --- | --- | --- | --- |
| Mois 1 [HY] | févr. 2027 | janv. 2027 | déc. 2026 |
| Mois 12 | janv. 2028 | déc. 2027 | nov. 2027 |
| Disponibilité des associés [HY] | Morgan 50 %, Mathys 25 % ; Morgan garde ses autres projets | Morgan 65 %, Mathys 50 % ; Morgan réduit fortement ses autres projets | 90 % chacun ; Morgan arrête l'essentiel du reste |
| Capacité facturable (JP par mois) [ES] | 7 | 12 (plafond engagé 10) | 20 |
| JP vendues par mois, mois 4 à 12 (moyenne) [ES] | 5,2 | 8,9 | 15,0 dont 3,0 sous-traitées |
| JP réalisées par les associés, mois le plus chargé | 6,0 | 8,9 | 13,2 |
| Occupation de la capacité facturable (mois 4 à 12) | 74 % | 74 % | 60 % |
| **CA facturé HT, mois 1 à 12** | **49 500 €** | **89 400 €** | **141 100 €** |
| CA encaissé HT, mois 1 à 12 | 49 500 € | 89 400 € | 141 100 € |
| dont hors GianLuca Carlone | 0 € | 0 € | 17 500 € |
| Part de GianLuca Carlone (12 mois ; mois 12) | 100 % ; 100 % | 100 % ; 100 % | 88 % ; 82 % |
| CA encaissé pondéré par les probabilités [ES], si le cadrage est vendu | 16 800 € | 38 300 € | 87 000 € |
| Contrat certain | 0 € | 0 € | 0 € |
| TVA collectée (à l'encaissement) | 9 900 € | 17 900 € | 28 200 € |
| TVA déductible (frais, démarrage, sous-traitance) | 3 000 € | 3 800 € | 7 600 € |
| TVA reversée au Trésor | 6 400 € | 12 700 € | 18 400 € |
| TVA restant due fin du mois 12 (reversée le mois suivant) | 400 € | 1 400 € | 2 200 € |
| Coûts directs HT (outils et IA, déplacements) | 4 300 à 6 800 € | 7 700 à 12 000 € | 12 500 à 19 500 € |
| Sous-traitance HT | 0 € | 0 € | 13 500 € |
| Frais généraux HT (assurances, comptable, banque, conseil, divers) | 10 100 à 15 800 € | 11 500 à 18 000 € | 14 400 à 22 500 € |
| Frais de démarrage HT (une fois) | 4 000 à 5 000 € | 5 000 à 7 000 € | 6 000 à 8 000 € |
| Rémunérations, coût total pour la société | 19 100 à 24 700 € | 38 300 à 45 600 € | 55 800 à 66 100 € |
| Résultat avant IS | 2 900 à 6 400 € | 14 100 à 19 600 € | 21 800 à 28 600 € |
| IS (15 % jusqu'à 42 500 €) [FV pour le taux] | 400 à 1 000 € | 2 100 à 2 900 € | 3 300 à 4 300 € |
| Résultat net | 2 400 à 5 500 € | 12 000 à 16 700 € | 18 600 à 24 300 € |
| Apport des associés [HY] | 8 000 € | 10 000 € | 13 000 € |
| Trésorerie en banque fin du mois 12 | 11 200 à 14 900 € | 25 400 à 31 100 € | 37 000 à 43 900 € |
| Trésorerie disponible (TVA due déduite) | 10 900 à 14 400 € | 24 100 à 29 600 € | 34 800 à 41 600 € |
| dont réserve (10 % du CA encaissé) | 5 000 € | 8 900 € | 14 100 € |
| dont IS à payer après la clôture | 400 à 1 000 € | 2 100 à 2 900 € | 3 300 à 4 300 € |
| Trésorerie libre (après réserve et IS) | 5 500 à 8 500 € | 13 000 à 17 700 € | 17 500 à 23 200 € |
| Point bas de la trésorerie disponible (mois) | 2 900 € (janv. 2027) | 3 100 € (déc. 2026) | 5 400 € (déc. 2026) |
| Objectif de réserve au mois 12 : 3 mois de frais + 1 mois de rémunération [PR] (audit-work/strategie-retenue.md:512) | 7 000 € : **non atteint** par la seule réserve de 10 % (5 000 €) ; atteint avec l'apport restant et l'excédent des mois 1 à 3 (12 100 € hors TVA et IS) | 10 700 € : **non atteint** par la seule réserve de 10 % (8 900 €) ; atteint avec l'apport restant et l'excédent des mois 1 à 3 (24 500 € hors TVA et IS) | 15 200 € : **non atteint** par la seule réserve de 10 % (14 100 €) ; atteint avec l'apport restant et l'excédent des mois 1 à 3 (34 700 € hors TVA et IS) |
| Net mensuel par associé, SAS, mois 4 à 12 (avant IR) | 600 à 800 € | 1 100 à 1 500 € | 1 600 à 2 200 € |
| Net mensuel par associé, SARL, même enveloppe (avant IR) | 800 à 1 000 € | 1 500 à 1 800 € | 2 200 à 2 600 € |
| Pour comparaison, stratégie retenue (audit-work/strategie-retenue.md:511-515) : CA sur 12 mois ; net par associé ; trésorerie M12 | ≈ 50 000 € ; 650 à 750 € ; 11 000 à 12 000 € | ≈ 90 000 € ; 1 350 à 1 550 € ; ≈ 25 000 € | ≈ 150 000 € ; 2 100 à 2 350 € ; ≈ 34 000 € |


## 2. Périmètre, capacité, prix et modalités

Prix proposés [PR] et calendrier de paiement retenu (audit-work/strategie-retenue.md:194-203, 427-446). Le paiement suit la nature de la prestation : capacité réservée payée d'avance ; livrables payés par acompte puis solde à la livraison ; consommation variable payée en fin de mois. Rien n'est encaissé avant l'immatriculation (audit-work/strategie-retenue.md:458).

| Offre | Prudent | Central | Ambitieux | Modalités |
| --- | --- | --- | --- | --- |
| A. Cadrage (8 JP, 3 à 4 semaines) | 6 000 € HT (plancher) | 6 500 € HT | 6 500 € HT | 50 % à la commande, 50 % à la réception sous 8 jours ; travail démarré à l'encaissement |
| B0. Socle pilote (3 à 4 JP par mois, 2 mois) | — | 3 500 € HT par mois | 3 500 € HT par mois | D'avance : facture le 25, échéance le 1er ; 1er mois à la signature |
| Socle récurrent (périodes de 3 mois) | Socle + 1 projet : 3 000 € HT par mois dès le mois 3 | B1 : 4 500 € HT par mois dès le mois 4 | Socle + 3 : 5 700 € HT par mois dès le mois 4 | D'avance, le 1er du mois |
| C. Lots devisés (JP × 800 € + 10 à 15 %) | 4 500 € HT par trimestre | Lot du pilote 6 000 € HT ; puis ≈ 3 500 € HT par mois | Deux lots du pilote à 6 000 € HT ; puis ≈ 4 500 € HT par mois | 40 % à la commande, 60 % à la livraison sous 8 jours |
| D. Exploitation d'un processus prouvé | — | — | 1 500 € HT par mois dès le mois 7 | Minimum d'avance ; variable en fin de mois sous 15 jours (non modélisé) |
| Second client | — | — (variante : 2 000 € HT par mois dès le mois 7) | 2 500 € HT par mois dès le mois 6 (probabilité 50 %) | [HY] mensuel d'avance |
| Sous-traitance | 0 | 0 (tiers facturés au client) | 3 JP par mois à 450 à 550 € HT | Attestation de vigilance dès 5 000 € HT cumulés |
| E. Avenant, urgences | 900 € HT par JP | 900 € HT par JP | 900 € HT par JP | Fin de mois, sous 15 jours ; seulement sur bon écrit préalable |


Tous les prix sont HT ; TTC = HT × 1,2. Si l'entité de GianLuca ne récupère pas la TVA, la TVA est un coût réel pour elle [HY] (audit-work/strategie-retenue.md:462). Achats, abonnements et prestataires du client ne passent jamais par Marwin et ne sont pas dans le CA (audit-work/strategie-retenue.md:188, 445, 488).


**Hypothèses de modélisation propres au script** [HY] : le solde du cadrage est encaissé le mois suivant l'acompte ; le socle est encaissé le mois du service ; les lots en régime sont représentés par des tranches mensuelles (40 % encaissés le mois de commande, 60 % le mois suivant) ; les lots du pilote et du prudent ont leur solde le mois suivant la commande ; JP d'un lot = prix ÷ 900 €.


### Prudent

**Périmètre** [PR] : Cadrage (6 000 € HT, plancher) ; « socle + 1 projet » à 3 000 € HT par mois à partir du mois 3 ; un lot de 4 500 € HT par trimestre. Variante basse : arrêt après le cadrage.

**Capacité** [ES] : Morgan 50 %, Mathys 25 % ; Morgan garde ses autres projets ; capacité facturable ≈ 7 JP par mois (audit-work/strategie-retenue.md:361-366, 495-496). JP vendues en moyenne sur les mois 4 à 12 : 5,2 ; prix moyen encaissé par JP vendue : 870 €.

| Mois | M | Facturé HT | Encaissé TTC | TVA collectée | TVA reversée | Frais, démarrage, sous-traitance TTC | Rémunérations (coût) | Trésorerie en banque | Trésorerie disponible | JP vendues |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nov. 2026 | avant | 0 € | 0 € | 0 € | 0 € | 1 800 € | 0 € | 6 200 € | 6 200 € | 0,0 |
| déc. 2026 | avant | 0 € | 0 € | 0 € | 0 € | 0 € | 0 € | 6 200 € | 6 200 € | 0,0 |
| janv. 2027 | avant | 0 € | 0 € | 0 € | 0 € | 3 300 € | 0 € | 2 900 € | 2 900 € | 0,0 |
| févr. 2027 | M1 | 3 000 € | 3 600 € | 600 € | 0 € | 1 900 € | 0 € | 4 600 € | 4 600 € | 6,0 |
| mars 2027 | M2 | 3 000 € | 3 600 € | 600 € | 0 € | 1 700 € | 0 € | 6 500 € | 6 500 € | 2,0 |
| avr. 2027 | M3 | 3 000 € | 3 600 € | 600 € | 0 € | 1 700 € | 0 € | 8 400 € | 8 000 € | 3,5 |
| mai 2027 | M4 | 4 800 € | 5 800 € | 1 000 € | 400 € | 1 700 € | 2 500 € | 9 600 € | 8 800 € | 6,0 |
| juin 2027 | M5 | 5 700 € | 6 800 € | 1 100 € | 800 € | 1 700 € | 2 400 € | 11 500 € | 10 600 € | 6,0 |
| juil. 2027 | M6 | 3 000 € | 3 600 € | 600 € | 900 € | 1 700 € | 2 500 € | 10 000 € | 9 600 € | 3,5 |
| août 2027 | M7 | 4 800 € | 5 800 € | 1 000 € | 400 € | 1 600 € | 2 500 € | 11 200 € | 10 400 € | 6,0 |
| sept. 2027 | M8 | 5 700 € | 6 800 € | 1 100 € | 800 € | 1 700 € | 2 500 € | 13 100 € | 12 100 € | 6,0 |
| oct. 2027 | M9 | 3 000 € | 3 600 € | 600 € | 1 000 € | 1 700 € | 2 400 € | 11 600 € | 11 200 € | 3,5 |
| nov. 2027 | M10 | 4 800 € | 5 800 € | 1 000 € | 400 € | 1 700 € | 2 500 € | 12 800 € | 12 000 € | 6,0 |
| déc. 2027 | M11 | 5 700 € | 6 800 € | 1 100 € | 800 € | 1 700 € | 2 500 € | 14 700 € | 13 700 € | 6,0 |
| janv. 2028 | M12 | 3 000 € | 3 600 € | 600 € | 900 € | 1 600 € | 2 400 € | 13 200 € | 12 800 € | 3,5 |
| **Total** |  | 49 500 € | 59 400 € | 9 900 € | 6 400 € | 25 500 € | 22 200 € |  |  |  |



### Central

**Périmètre** [PR] : Cadrage (6 500 € HT) ; pilote de 8 semaines (B0 à 3 500 € HT par mois et un lot de 6 000 € HT) ; à partir du mois 4, B1 à 4 500 € HT par mois et des lots pour ≈ 3 500 € HT par mois en moyenne.

**Capacité** [ES] : Morgan 65 %, Mathys 50 % ; Morgan réduit fortement ses autres projets ; capacité facturable ≈ 12 JP par mois (audit-work/strategie-retenue.md:361-366, 495-496). JP vendues en moyenne sur les mois 4 à 12 : 8,9 ; prix moyen encaissé par JP vendue : 870 €.

| Mois | M | Facturé HT | Encaissé TTC | TVA collectée | TVA reversée | Frais, démarrage, sous-traitance TTC | Rémunérations (coût) | Trésorerie en banque | Trésorerie disponible | JP vendues |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nov. 2026 | avant | 0 € | 0 € | 0 € | 0 € | 2 400 € | 0 € | 7 600 € | 7 600 € | 0,0 |
| déc. 2026 | avant | 0 € | 0 € | 0 € | 0 € | 4 500 € | 0 € | 3 100 € | 3 100 € | 0,0 |
| janv. 2027 | M1 | 3 300 € | 3 900 € | 700 € | 0 € | 2 500 € | 0 € | 4 500 € | 4 500 € | 6,0 |
| févr. 2027 | M2 | 9 100 € | 11 000 € | 1 800 € | 0 € | 2 200 € | 0 € | 13 300 € | 12 400 € | 8,8 |
| mars 2027 | M3 | 7 100 € | 8 500 € | 1 400 € | 900 € | 2 200 € | 0 € | 18 700 € | 17 500 € | 6,8 |
| avr. 2027 | M4 | 5 900 € | 7 100 € | 1 200 € | 1 200 € | 2 300 € | 4 700 € | 17 700 € | 16 700 € | 8,9 |
| mai 2027 | M5 | 8 000 € | 9 600 € | 1 600 € | 900 € | 2 200 € | 4 700 € | 19 400 € | 18 000 € | 8,9 |
| juin 2027 | M6 | 8 000 € | 9 600 € | 1 600 € | 1 400 € | 2 200 € | 4 700 € | 20 700 € | 19 300 € | 8,9 |
| juil. 2027 | M7 | 8 000 € | 9 600 € | 1 600 € | 1 400 € | 2 200 € | 4 700 € | 22 000 € | 20 600 € | 8,9 |
| août 2027 | M8 | 8 000 € | 9 600 € | 1 600 € | 1 400 € | 2 300 € | 4 700 € | 23 200 € | 21 900 € | 8,9 |
| sept. 2027 | M9 | 8 000 € | 9 600 € | 1 600 € | 1 300 € | 2 200 € | 4 700 € | 24 500 € | 23 200 € | 8,9 |
| oct. 2027 | M10 | 8 000 € | 9 600 € | 1 600 € | 1 400 € | 2 200 € | 4 700 € | 25 800 € | 24 500 € | 8,9 |
| nov. 2027 | M11 | 8 000 € | 9 600 € | 1 600 € | 1 400 € | 2 200 € | 4 700 € | 27 100 € | 25 800 € | 8,9 |
| déc. 2027 | M12 | 8 000 € | 9 600 € | 1 600 € | 1 400 € | 2 200 € | 4 800 € | 28 400 € | 27 000 € | 8,9 |
| **Total** |  | 89 400 € | 107 300 € | 17 900 € | 12 700 € | 33 800 € | 42 400 € |  |  |  |



### Ambitieux

**Périmètre** [PR] : Cadrage (6 500 € HT) ; pilote avec deux lots de 6 000 € HT ; à partir du mois 4, « socle + 3 projets » à 5 700 € HT par mois et des lots pour ≈ 4 500 € HT par mois ; exploitation D à 1 500 € HT par mois à partir du mois 7 ; second client à 2 500 € HT par mois à partir du mois 6 ; sous-traitance de 3 JP par mois.

**Capacité** [ES] : 90 % chacun ; Morgan arrête l'essentiel du reste ; capacité facturable ≈ 20 JP par mois (audit-work/strategie-retenue.md:361-366, 495-496). JP vendues en moyenne sur les mois 4 à 12 : 15,0 ; prix moyen encaissé par JP vendue : 860 €.

| Mois | M | Facturé HT | Encaissé TTC | TVA collectée | TVA reversée | Frais, démarrage, sous-traitance TTC | Rémunérations (coût) | Trésorerie en banque | Trésorerie disponible | JP vendues |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nov. 2026 | avant | 0 € | 0 € | 0 € | 0 € | 7 500 € | 0 € | 5 500 € | 5 500 € | 0,0 |
| déc. 2026 | M1 | 3 300 € | 3 900 € | 700 € | 0 € | 4 000 € | 0 € | 5 400 € | 5 400 € | 6,0 |
| janv. 2027 | M2 | 11 500 € | 13 900 € | 2 300 € | 0 € | 3 100 € | 0 € | 16 200 € | 15 200 € | 12,2 |
| févr. 2027 | M3 | 10 700 € | 12 800 € | 2 100 € | 1 000 € | 3 000 € | 0 € | 24 900 € | 23 100 € | 10,2 |
| mars 2027 | M4 | 7 500 € | 9 000 € | 1 500 € | 1 900 € | 4 900 € | 6 800 € | 20 400 € | 19 500 € | 11,5 |
| avr. 2027 | M5 | 10 200 € | 12 200 € | 2 000 € | 900 € | 4 900 € | 6 900 € | 20 000 € | 18 500 € | 11,5 |
| mai 2027 | M6 | 12 700 € | 15 300 € | 2 600 € | 1 400 € | 4 900 € | 6 800 € | 22 000 € | 20 100 € | 14,5 |
| juin 2027 | M7 | 14 200 € | 17 000 € | 2 800 € | 1 900 € | 4 900 € | 6 800 € | 25 400 € | 23 200 € | 16,2 |
| juil. 2027 | M8 | 14 200 € | 17 100 € | 2 900 € | 2 300 € | 4 900 € | 6 900 € | 28 500 € | 26 200 € | 16,2 |
| août 2027 | M9 | 14 200 € | 17 000 € | 2 800 € | 2 200 € | 4 900 € | 6 800 € | 31 500 € | 29 300 € | 16,2 |
| sept. 2027 | M10 | 14 200 € | 17 000 € | 2 800 € | 2 300 € | 4 900 € | 6 800 € | 34 600 € | 32 400 € | 16,2 |
| oct. 2027 | M11 | 14 200 € | 17 100 € | 2 900 € | 2 200 € | 4 900 € | 6 900 € | 37 700 € | 35 400 € | 16,2 |
| nov. 2027 | M12 | 14 200 € | 17 000 € | 2 800 € | 2 300 € | 4 900 € | 6 800 € | 40 700 € | 38 500 € | 16,2 |
| **Total** |  | 141 100 € | 169 300 € | 28 200 € | 18 400 € | 61 700 € | 61 500 € |  |  |  |



## 3. Rémunérations : brut, cotisations et net par associé (SAS et SARL)

**Hypothèses explicites.** Deux associés à parts égales, tous deux dirigeants ; même enveloppe pour les deux ; rien avant le mois 4 (audit-work/strategie-retenue.md:511) ; enveloppe constante ensuite, calculée par le script (règle en tête du script). SAS : coût total = 1,7 à 1,9 fois le net [HY] (audit-work/syn-droit.md:98) ; brut indicatif = net ÷ 0,75 [HY] (audit-work/rj-R1-structures.md:50). SARL : deux cogérants à 50/50, donc TNS [FV] (audit-work/syn-droit.md:109) ; barème F38152 « revenus 2025 » appliqué à 74 % du coût total [ES] (audit-work/syn-droit.md:97) ; forfaits de première année ≈ 3 591 € puis régularisation [FV/ES] (audit-work/syn-droit.md:111, 189-195). Pas d'ACRE, d'ARE, de mutuelle ni de prévoyance ; **pas d'impôt sur le revenu** [IN].

| Scénario | Enveloppe mensuelle (deux associés, coût total) | Coût total par associé sur 9 mois | SAS : brut indicatif | SAS : cotisations (salariales et patronales) | SAS : net sur 9 mois | SAS : net par mois | SARL : cotisations TNS définitives | SARL : net sur 9 mois | SARL : net par mois | SARL : régularisation en année 2 (+ à payer, − rendu) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Prudent | 2 500 € | 11 100 € | 7 800 à 8 700 € | 4 600 à 5 300 € | 5 900 à 6 500 € | ≈ 700 € | 3 200 € | 7 900 € | 900 € | −400 € |
| Central | 4 700 € | 21 200 € | 14 900 à 16 600 € | 8 700 à 10 000 € | 11 100 à 12 500 € | 1 200 à 1 400 € | 6 100 € | 15 000 € | 1 700 € | 2 500 € |
| Ambitieux | 6 800 € | 30 800 € | 21 600 à 24 100 € | 12 700 à 14 600 € | 16 200 à 18 100 € | 1 800 à 2 000 € | 9 100 € | 21 700 € | 2 400 € | 5 500 € |


Lecture : frais et démarrage à leur valeur centrale ; les plages SAS ne reflètent que le coefficient 1,7 à 1,9 (la synthèse de la section 1 y ajoute les frais bas et hauts). En SARL, la première année se paie sur les forfaits (≈ 3 600 € par gérant), même pendant les mois sans rémunération ; l'écart est régularisé l'année suivante (audit-work/syn-droit.md:189-192). Les dividendes ne sont pas un levier la première année : aucun bénéfice n'est distribuable avant la clôture et l'approbation des comptes (voir `structures.md`).


**Comparaison avec un emploi salarié chez le client** (pour mémoire) : un poste de cadre ≈ 3 400 € nets pour 6 149 € de coût employeur [MM] (audit-work/ver-R6-marche.md:25) rapporterait plus que tous les scénarios centraux de Marwin la première année (audit-work/strategie-retenue.md:707). C'est le principal risque pour l'indépendance de Marwin pendant la négociation.


## 4. Seuil de rentabilité en journées vendues

Méthode [ES] : JP vendues par mois nécessaires pour couvrir, au prix moyen par JP du régime (mois 4 à 12), les frais fixes, la réserve de 10 % et, selon la ligne, une rémunération. La sous-traitance est comptée comme coût variable par JP. L'IS est négligé (il ne porte que sur la réserve).

| Scénario | Prix moyen par JP vendue | Frais fixes par mois | Seuil : frais et réserve | Seuil : + rémunération du scénario | Seuil : + 2 500 € nets par ETP engagé | JP vendues prévues (mois 4 à 12) | Capacité facturable |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Prudent | 870 € | 1 500 € | 1,9 | 5,1 | 6,0 à 6,5 | 5,2 | 7 |
| Central | 870 € | 2 000 € | 2,5 | 8,5 | 8,8 à 9,5 | 8,9 | 12 (plafond 10) |
| Ambitieux | 860 € | 2 800 € | 4,2 | 14,4 | 15,6 à 16,9 | 15,0 | 20 |


ETP engagés [HY] : 0,75 (prudent), 1,15 (central), 1,8 (ambitieux) (audit-work/strategie-retenue.md:363-366).


## 5. Variantes

- **Prudent, variante basse** (GianLuca s'arrête au cadrage, probabilité 60 % selon audit-work/strategie-retenue.md:502) : CA 6 000 € HT ; résultat avant IS −16 500 € ; trésorerie disponible à la fin du mois 12 −10 300 € (dont 1 800 € de crédit de TVA remboursable, non compté) sur un apport de 8 000 €, si rien n'est arrêté. Aucune rémunération. Sans arrêt des frais fixes de 1 500 € par mois, la trésorerie devient négative en juil. 2027 : les abonnements et l'assurance doivent être résiliables au mois et arrêtés dès l'échec constaté.
- **Central avec un second client** (audit-work/strategie-retenue.md:522) : CA 93 300 € HT ; part de GianLuca 87 % sur douze mois et 76 % au mois 12 ; net par associé 1 200 à 1 600 € par mois en SAS ; trésorerie disponible fin du mois 12 27 500 €. Si le second client n'est pas signé au mois 9, la cible de dépendance « 80 % au plus » passe au mois 18.


## 6. Écarts avec la stratégie retenue et leurs causes

La stratégie (audit-work/strategie-retenue.md:492-518) utilisait un modèle simplifié qui encaisse les factures le mois même et ne modélise ni l'IS ni la TVA. Ce modèle les ajoute, ce qui explique les écarts :
- **IS** : il réduit la rémunération soutenable d'environ 1/9 de l'IS annuel par mois ;
- **TVA** : neutre sur l'année, elle gonfle la trésorerie en banque d'un mois de TVA nette (à ne jamais dépenser) et coûte un peu de trésorerie au démarrage (TVA payée sur les frais avant d'en collecter) ;
- **délais d'encaissement** : les soldes de lots arrivent le mois suivant ; le dernier solde des mois 1 à 12 tombe au mois 13 ;
- **exploitation D (ambitieux)** : la stratégie la fait commencer au mois 7 dans son texte (audit-work/strategie-retenue.md:494) mais au mois 4 dans son calcul (verif § 10 : 1 500 € par mois sur les mois 4 à 12). Le modèle suit la règle écrite (« au plus tôt au mois 7 », audit-work/strategie-retenue.md:339), d'où un CA ambitieux inférieur d'environ 4 500 €.

| Scénario | CA 12 mois (stratégie) | CA 12 mois (modèle) | Net par associé (stratégie) | Net par associé (modèle, SAS) | Trésorerie M12 (stratégie, avant IS et TVA) | Trésorerie disponible M12 (modèle) |
| --- | --- | --- | --- | --- | --- | --- |
| Prudent | ≈ 50 000 € | 49 500 € | 650 à 750 € | ≈ 700 € (600 à 800 €) | 11 000 à 12 000 € | 12 800 € |
| Central | ≈ 90 000 € | 89 400 € | 1 350 à 1 550 € | ≈ 1 300 € (1 100 à 1 500 €) | ≈ 25 000 € | 27 000 € |
| Ambitieux | ≈ 150 000 € | 141 100 € | 2 100 à 2 350 € | ≈ 1 900 € (1 600 à 2 200 €) | ≈ 34 000 € | 38 500 € |


## 7. Limites

- Les probabilités de passage sont des paramètres de jugement [HY] (audit-work/strategie-retenue.md:502) ; celle de vendre le cadrage est inconnue [IN].
- Le coefficient SAS vient d'une source secondaire unique ; le barème TNS est celui des revenus 2025 ; les lois de finances et de financement de la sécurité sociale pour 2027 sont en discussion : **tout refaire en janvier 2027** avec l'expert-comptable et le simulateur officiel (audit-work/syn-droit.md:22-23, 198-207).
- Les frais (assurance, déplacements, conseil) sont des hypothèses [HY/IN] à remplacer par des devis (audit-work/strategie-retenue.md:837).
- L'IS est calculé comme si les douze mois formaient un exercice, avec le seuil de 42 500 € non proratisé ; un premier exercice de 13 ou 14 mois relèverait ce seuil au prorata (sans effet ici : aucun bénéfice n'atteint 42 500 €) ; en prudent, le mois 12 (janv. 2028) appartient déjà au deuxième exercice. La date de clôture réelle est à arrêter avec l'expert-comptable (audit-work/syn-droit.md:143).
- Les comportements de paiement de l'entité de GianLuca sont inconnus [IN] (audit-work/strategie-retenue.md:467) : voir `stress-tests.md`.
- Aucun coût lié à la fuite au-delà du conseil (sanction, réclamations, franchise d'assurance) n'est chiffré [IN].
- Le central retient la voie de pilote la plus chère (B0 et un lot, 13 000 € HT ; voies du pilote : audit-work/strategie-retenue.md:247-249). Avec un pilote C2 seul (6 000 € HT), le CA sur 12 mois tombe à 82 400 € HT et la trésorerie libre du mois 12 à 9 200 € ; avec un pilote C6 seul (7 500 € HT), le CA sur 12 mois tombe à 83 900 € HT et la trésorerie libre du mois 12 à 10 600 € (contre 15 600 €). La règle de rémunération, qui ne regarde que les mois 4 à 12, ne baisse pas : c'est le coussin qui absorbe l'écart.
- Matériel informatique non budgété au-delà de la mise en place (200 à 700 €) : les associés utilisent leur propre matériel [HY].
