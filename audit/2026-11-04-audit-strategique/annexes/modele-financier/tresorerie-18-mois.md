# Plan de trésorerie sur dix-huit mois : scénario central

**Document interne.** Il contient des coûts, des marges, des rémunérations visées et des probabilités : il ne doit pas être transmis à GianLuca Carlone (audit-work/strategie-retenue.md:787-789).

Produit le 4 novembre 2026 par `modele_financier.py` (même dossier), qui contient tous les paramètres, leur code et leur source. Pour changer une hypothèse, modifier le paramètre en tête du script et le relancer. « audit-work/ » désigne le dossier de travail de l'audit (hors dépôt) ; les autres chemins renvoient au dépôt (commit 7b46602).

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] mesure ; [IN] inconnu. **Tous les résultats chiffrés sont des [ES]**, arrondis à la centaine d'euros (à la dizaine pour les prix par JP) : un total peut différer de 100 à 200 € de la somme de ses lignes arrondies. Les fourchettes combinent frais bas et coefficient social bas, puis frais hauts et coefficient haut.

**Impôt sur le revenu non calculé** : les situations fiscales des foyers de Morgan Olsen et de Mathys Couet sont [IN] (audit-work/rj-R1-structures.md:15 ; audit-work/syn-droit.md:93). Tous les nets sont « avant impôt sur le revenu ».


Données mensuelles : `tresorerie-18-mois.csv` (séparateur « ; », même contenu que les tableaux ci-dessous). Les flux mensuels sont arrondis à la centaine en reportant l'arrondi d'un mois sur l'autre : les totaux de colonne sont justes, mais une même dépense de 2 224 € peut apparaître pour 2 200 € un mois et 2 300 € le suivant. Les soldes (trésorerie, réserve, TVA due) sont arrondis directement.


**Trois faits pris comme base** (audit-work/strategie-retenue.md:29-33) :
1. **Aucun contrat, aucune facture, aucune entité payeuse identifiée** [FV négatif]. Le « contrat certain » vaut donc **0 €** dans tous les scénarios : chaque euro de chiffre d'affaires ci-dessous est une hypothèse.
2. **Medhi et BOJ.ART retirés de l'offre** le 4 nov. 2026 à la demande de Morgan [DR] (audit-work/note-point-4-novembre-et-activites.md:25). Seul le diaporama client a été corrigé (11 diapositives) ; l'offre écrite, STRATES v1.1, le vernissage et le PDF de 13 diapositives de la PR n° 1 ne l'ont pas été [FV] (audit-work/strategie-retenue.md:31). Le modèle ne compte **aucune recette ni dépense** pour STRATES, la création, le laboratoire ou le vernissage « signature ».
3. **Fuite de données très probable** (dépôt public FinanceScope/CRM-Carlone) ; délai CNIL de 72 h possiblement échu le 5 nov. si la connaissance date du 2 nov. [ES] (audit-work/strategie-retenue.md:32). Le modèle compte le conseil (avocat ou DPD) dans les frais de démarrage de novembre 2026 [HY] ; une sanction, une action des personnes ou un refus d'assurance ne sont **pas chiffrés** [IN]. Rien ne démarre tant que la fuite n'est pas traitée (audit-work/strategie-retenue.md:53, 660).


## 0. Lecture rapide

- **Contrat certain : aucun.** Les encaissements « certains » valent 0 € chaque mois [FV négatif] (audit-work/strategie-retenue.md:33). Tout le reste est une hypothèse commerciale, à commencer par la vente du cadrage.
- Mois 1 = janv. 2027 [HY] : il suppose un rendez-vous avant le 15 décembre 2026, une entité payeuse nommée, une immatriculation fin décembre ou début janvier et l'acompte du cadrage encaissé en janvier (audit-work/strategie-retenue.md:44, 500).
- **Point bas de la trésorerie disponible** : 3 100 € en déc. 2026. L'apport de 10 000 € couvre le démarrage (6 000 € HT) ; sans apport, il manquerait 6 900 € à ce moment.
- **Fin du mois 12 (déc. 2027)** : trésorerie en banque 28 400 €, dont TVA due 1 400 €, réserve 8 900 € et IS de l'exercice 2027 à payer en mai 2028 2 600 € ; trésorerie libre 15 600 €.
- **Fin des 18 mois (avr. 2028)** : trésorerie en banque 33 600 € ; trésorerie libre 16 800 €. Rémunération versée à partir du mois 4 : enveloppe de 4 700 € par mois pour les deux associés, soit ≈ 1 300 € (1 100 à 1 500 €) nets par associé et par mois en SAS, avant IR.
- **Pondéré par les probabilités de passage** (pilote 60 %, socle 70 %, renouvellement trimestriel 80 %, audit-work/strategie-retenue.md:502), les encaissements des 18 mois tombent de 145 700 € à 54 100 € TTC, **à condition que le cadrage soit vendu** (probabilité [IN]). Le plan ci-dessous est donc un plan de pilotage, pas une prévision.


## 1. Trois blocs distincts

| Bloc | Contenu | Encaissements sur 18 mois (TTC) |
| --- | --- | --- |
| 1. Contrat certain | Aucun contrat, aucune facture, aucune entité payeuse [FV négatif] | 0 € |
| 2. Hypothèses de vente et de renouvellement | Cadrage (première vente, probabilité [IN]) ; pilote (60 %) ; socle B1 par trimestres renouvelés (70 %, puis 80 % par trimestre) ; lots liés au socle [HY] (audit-work/strategie-retenue.md:502) | 145 700 € |
| 3. Projets non financés | Laboratoire, création avec Medhi et STRATES, vernissage « signature », DGX Spark : aucune recette et aucune dépense ; Marwin n'avance rien pour le client (audit-work/strategie-retenue.md:188, 639-654) | 0 € |


**Projets non financés, pour mémoire** (montants des archives, jamais inscrits au plan) :

| Projet | Montant évoqué | Statut |
| --- | --- | --- |
| Option laboratoire IA et robotique | 30 000 € HT, dont 13 500 € d'honoraires Marwin et 16 500 € d'achats au nom de l'entité du client [PR des archives] (interne/offre-marwin-tech-remuneration-et-collaboration.md:21 ; audit-work/syn-portefeuille.md:530) | Retirée (audit-work/strategie-retenue.md:411, 645) |
| Option création avec Medhi (BOJ.ART), STRATES | ≈ 10 000 € HT pour une première phase [PR des archives] (interne/offre-marwin-tech-remuneration-et-collaboration.md:22) | Retirée le 4 nov. [DR] (audit-work/note-point-4-novembre-et-activites.md:25 ; audit-work/strategie-retenue.md:31, 412) ; offre écrite non corrigée |
| STRATES, Éclosion | aucun budget propre : les 323 875 € portent sur un ancien scénario de figurines (audit-work/syn-portefeuille.md:511) | Gelés (audit-work/strategie-retenue.md:644) |
| Vernissage « signature » avec bras robotisé | 4 500 à 22 500 € HT d'honoraires selon le format [PR/ES] (audit-work/syn-portefeuille.md:452) | Reporté sans date (audit-work/strategie-retenue.md:646) |
| DGX Spark, IA locale | ≈ 6 200 € HT (128 Go) [ES] (audit-work/ver-R6-marche.md:34) | Retiré ; achat par le client seulement (audit-work/strategie-retenue.md:645) |
| Remise en ordre (offre 0) | 9 à 17 JP non facturés sur les mois 0 à 2 [ES] (audit-work/strategie-retenue.md:196, 213) | Interne ; ses sorties d'argent sont dans les frais de démarrage |


## 2. Calendrier de paiement retenu et traduction dans le modèle

La contradiction des archives (« règlement sous sept jours après facture de fin de mois », sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:57, contre « mois 2 à 6 payés d'avance, en début de mois », interne/offre-marwin-tech-remuneration-et-collaboration.md:19) est tranchée par la stratégie : **le paiement suit la nature de la prestation** [PR] (audit-work/strategie-retenue.md:429-434).

| Prestation | Règle retenue [PR] | Dans le modèle [HY] |
| --- | --- | --- |
| A. Cadrage | 50 % à la commande ; 50 % à la réception, sous 8 jours | Acompte au mois 1 ; solde au mois 2 |
| B0, B1. Socle | D'avance : facture le 25 du mois précédent, échéance le 1er | Encaissé le mois du service |
| C. Lots | 40 % à la commande ; 60 % à la livraison, sous 8 jours | Tranches mensuelles : 40 % le mois de commande, 60 % le mois suivant |
| Achats et prestataires du client | Jamais par Marwin | 0 € |
| TVA | Exigible à l'encaissement [FV] (audit-work/rj-R2-fiscal.md:385) | Collectée à l'encaissement ; reversée le mois suivant (réel normal mensuel [HY]) |
| Rémunérations | Rien avant le mois 4 [PR] | Enveloppe constante dès le mois 4, cotisations comprises le mois même |
| IS | 15 % puis 25 % [FV] | Exercice 2027 clos le 31 déc. [HY] ; solde payé en mai 2028, hors horizon : provisionné |


## 3. Encaissements par bloc (TTC)

| Mois | M | Contrat certain | Cadrage | Pilote | Socle B1 | Lots | Total TTC | dont TVA | Probabilité cumulée la plus faible du mois [HY] | Pondéré TTC [ES] | Projets non financés |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nov. 2026 | avant | 0 € | 0 € | 0 € | 0 € | 0 € | 0 € | 0 € | 0,00 | 0 € | 0 € |
| déc. 2026 | avant | 0 € | 0 € | 0 € | 0 € | 0 € | 0 € | 0 € | 0,00 | 0 € | 0 € |
| janv. 2027 | M1 | 0 € | 3 900 € | 0 € | 0 € | 0 € | 3 900 € | 700 € | 1,00 | 3 900 € | 0 € |
| févr. 2027 | M2 | 0 € | 3 900 € | 7 100 € | 0 € | 0 € | 11 000 € | 1 800 € | 0,60 | 8 100 € | 0 € |
| mars 2027 | M3 | 0 € | 0 € | 8 500 € | 0 € | 0 € | 8 500 € | 1 400 € | 0,60 | 5 200 € | 0 € |
| avr. 2027 | M4 | 0 € | 0 € | 0 € | 5 400 € | 1 700 € | 7 100 € | 1 200 € | 0,42 | 2 900 € | 0 € |
| mai 2027 | M5 | 0 € | 0 € | 0 € | 5 400 € | 4 200 € | 9 600 € | 1 600 € | 0,42 | 4 100 € | 0 € |
| juin 2027 | M6 | 0 € | 0 € | 0 € | 5 400 € | 4 200 € | 9 600 € | 1 600 € | 0,42 | 4 000 € | 0 € |
| juil. 2027 | M7 | 0 € | 0 € | 0 € | 5 400 € | 4 200 € | 9 600 € | 1 600 € | 0,34 | 3 400 € | 0 € |
| août 2027 | M8 | 0 € | 0 € | 0 € | 5 400 € | 4 200 € | 9 600 € | 1 600 € | 0,34 | 3 300 € | 0 € |
| sept. 2027 | M9 | 0 € | 0 € | 0 € | 5 400 € | 4 200 € | 9 600 € | 1 600 € | 0,34 | 3 200 € | 0 € |
| oct. 2027 | M10 | 0 € | 0 € | 0 € | 5 400 € | 4 200 € | 9 600 € | 1 600 € | 0,27 | 2 700 € | 0 € |
| nov. 2027 | M11 | 0 € | 0 € | 0 € | 5 400 € | 4 200 € | 9 600 € | 1 600 € | 0,27 | 2 600 € | 0 € |
| déc. 2027 | M12 | 0 € | 0 € | 0 € | 5 400 € | 4 200 € | 9 600 € | 1 600 € | 0,27 | 2 600 € | 0 € |
| janv. 2028 | M13 | 0 € | 0 € | 0 € | 5 400 € | 4 200 € | 9 600 € | 1 600 € | 0,22 | 2 200 € | 0 € |
| févr. 2028 | M14 | 0 € | 0 € | 0 € | 5 400 € | 4 200 € | 9 600 € | 1 600 € | 0,22 | 2 100 € | 0 € |
| mars 2028 | M15 | 0 € | 0 € | 0 € | 5 400 € | 4 200 € | 9 600 € | 1 600 € | 0,22 | 2 000 € | 0 € |
| avr. 2028 | M16 | 0 € | 0 € | 0 € | 5 400 € | 4 200 € | 9 600 € | 1 600 € | 0,17 | 1 800 € | 0 € |
| **Total** |  | 0 € | 7 800 € | 15 600 € | 70 200 € | 52 100 € | 145 700 € | 24 300 € |  | 54 100 € | 0 € |


## 4. Décaissements et trésorerie

| Mois | M | Apport | Démarrage TTC | Frais fixes TTC | Rémunérations (coût total) | TVA reversée | Flux net | Trésorerie en banque | TVA due | Trésorerie disponible | Réserve cumulée | IS à provisionner | Trésorerie libre | JP vendues |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nov. 2026 | avant | 10 000 € | 2 400 € | 0 € | 0 € | 0 € | 7 600 € | 7 600 € | 0 € | 7 600 € | 0 € | 0 € | 7 600 € | 0,0 |
| déc. 2026 | avant | 0 € | 4 500 € | 0 € | 0 € | 0 € | −4 500 € | 3 100 € | 0 € | 3 100 € | 0 € | 0 € | 3 100 € | 0,0 |
| janv. 2027 | M1 | 0 € | 300 € | 2 200 € | 0 € | 0 € | 1 400 € | 4 500 € | 0 € | 4 500 € | 300 € | 0 € | 4 200 € | 6,0 |
| févr. 2027 | M2 | 0 € | 0 € | 2 200 € | 0 € | 0 € | 8 800 € | 13 300 € | 900 € | 12 400 € | 1 200 € | 400 € | 10 800 € | 8,8 |
| mars 2027 | M3 | 0 € | 0 € | 2 300 € | 0 € | 900 € | 5 400 € | 18 700 € | 1 200 € | 17 500 € | 2 000 € | 1 100 € | 14 400 € | 6,8 |
| avr. 2027 | M4 | 0 € | 0 € | 2 200 € | 4 700 € | 1 200 € | −1 000 € | 17 700 € | 1 000 € | 16 700 € | 2 500 € | 1 000 € | 13 200 € | 8,9 |
| mai 2027 | M5 | 0 € | 0 € | 2 200 € | 4 700 € | 900 € | 1 700 € | 19 400 € | 1 400 € | 18 000 € | 3 300 € | 1 200 € | 13 500 € | 8,9 |
| juin 2027 | M6 | 0 € | 0 € | 2 200 € | 4 700 € | 1 400 € | 1 300 € | 20 700 € | 1 400 € | 19 300 € | 4 100 € | 1 400 € | 13 800 € | 8,9 |
| juil. 2027 | M7 | 0 € | 0 € | 2 300 € | 4 700 € | 1 400 € | 1 300 € | 22 000 € | 1 400 € | 20 600 € | 4 900 € | 1 600 € | 14 100 € | 8,9 |
| août 2027 | M8 | 0 € | 0 € | 2 200 € | 4 700 € | 1 400 € | 1 200 € | 23 200 € | 1 400 € | 21 900 € | 5 700 € | 1 800 € | 14 400 € | 8,9 |
| sept. 2027 | M9 | 0 € | 0 € | 2 200 € | 4 700 € | 1 300 € | 1 300 € | 24 500 € | 1 400 € | 23 200 € | 6 500 € | 2 000 € | 14 700 € | 8,9 |
| oct. 2027 | M10 | 0 € | 0 € | 2 200 € | 4 700 € | 1 400 € | 1 300 € | 25 800 € | 1 400 € | 24 500 € | 7 300 € | 2 200 € | 15 000 € | 8,9 |
| nov. 2027 | M11 | 0 € | 0 € | 2 300 € | 4 700 € | 1 400 € | 1 300 € | 27 100 € | 1 400 € | 25 800 € | 8 100 € | 2 400 € | 15 300 € | 8,9 |
| déc. 2027 | M12 | 0 € | 0 € | 2 200 € | 4 800 € | 1 400 € | 1 300 € | 28 400 € | 1 400 € | 27 000 € | 8 900 € | 2 600 € | 15 600 € | 8,9 |
| janv. 2028 | M13 | 0 € | 0 € | 2 200 € | 4 700 € | 1 300 € | 1 300 € | 29 700 € | 1 400 € | 28 300 € | 9 700 € | 2 800 € | 15 900 € | 8,9 |
| févr. 2028 | M14 | 0 € | 0 € | 2 200 € | 4 700 € | 1 400 € | 1 300 € | 31 000 € | 1 400 € | 29 600 € | 10 500 € | 2 900 € | 16 200 € | 8,9 |
| mars 2028 | M15 | 0 € | 0 € | 2 300 € | 4 700 € | 1 400 € | 1 300 € | 32 300 € | 1 400 € | 30 900 € | 11 300 € | 3 100 € | 16 500 € | 8,9 |
| avr. 2028 | M16 | 0 € | 0 € | 2 200 € | 4 700 € | 1 400 € | 1 300 € | 33 600 € | 1 400 € | 32 200 € | 12 100 € | 3 300 € | 16 800 € | 8,9 |
| **Total** |  | 10 000 € | 7 200 € | 35 600 € | 61 200 € | 18 200 € | 33 600 € | 33 600 € |  |  |  |  |  |  |


Définitions : trésorerie disponible = trésorerie en banque − TVA collectée non encore reversée ; trésorerie libre = disponible − réserve (10 % du CA encaissé) − IS à provisionner. JP vendues : plafond engagé de 10 JP par mois la première année (audit-work/strategie-retenue.md:485).


## 5. TVA : ce qui entre n'est pas à Marwin

- Sur les 18 mois, Marwin collecte 24 300 € de TVA, en déduit 4 700 € et en reverse 18 200 € ; 1 400 € restent dus fin avr. 2028.
- Un retard de paiement du client ne fait pas avancer la TVA : elle n'est exigible qu'à l'encaissement [FV] (audit-work/rj-R2-fiscal.md:19, 385).
- **Variante « réel simplifié »** [HY, à confirmer par l'expert-comptable] : sans acompte la première année, la TVA nette de 2027 (≈ 14 000 €) resterait sur le compte jusqu'à la déclaration annuelle de mai 2028. Elle gonflerait la trésorerie apparente sans jamais être disponible. Le modèle retient la déclaration mensuelle, plus lisible pour deux associés qui découvrent la gestion.
- Franchise en base : sans intérêt ici ; facturer la TVA dès la première facture (audit-work/syn-droit.md:299).


## 6. Points d'attention

- **Démarrage financé par l'apport.** Le conseil sur la fuite (novembre 2026) et les statuts et le pacte (décembre 2026) sont payés avant tout encaissement. Si l'apport n'existe pas, la stratégie prévoit de réduire les sorties de la phase 0 au conseil sur la fuite et aux statuts (audit-work/strategie-retenue.md:776).
- **Le surplus des mois 1 à 3** (pilote payé, aucune rémunération) constitue l'essentiel du coussin : un pilote non vendu le supprime (voir `stress-tests.md`).
- **L'IS de l'exercice 2027** (2 600 €) est dû en mai 2028, juste après l'horizon : il ne doit pas être dépensé.
- **Dépendance à un seul client : 100 %** pendant 18 mois, **à assumer par écrit** entre les associés [PR], ce qui n'est pas fait [IN] (audit-work/strategie-retenue.md:514) ; la variante avec un second client est dans `scenarios.md`.
- **Cotisations des dirigeants** : en SAS, aucune sans rémunération ; versées avec chaque paie ensuite (audit-work/syn-droit.md:195).
- **Prime d'assurance payée d'avance** [ES] : si la RC professionnelle est payée en une fois avant la première prestation, le point bas de la trésorerie disponible tombe à 700 € en déc. 2026 pour une prime de 2 400 € par an ; 100 € en déc. 2026 pour une prime de 3 000 € par an (montant de la prime [IN], hypothèse de 200 à 250 € par mois, audit-work/strategie-retenue.md:506). L'apport de 10 000 € ne laisse alors presque aucune marge : obtenir un paiement fractionné de la prime, ou viser le haut de la fourchette d'apport (8 000 à 14 000 €, audit-work/strategie-retenue.md:172).


## 7. Limites

- Pratiques de paiement de l'entité de GianLuca inconnues [IN] (audit-work/strategie-retenue.md:467) ; le plan suppose des paiements à l'échéance.
- Les renouvellements trimestriels du socle et le rythme des lots sont des hypothèses ; ils sont présentés en clair, avec leur probabilité cumulée, pour ne jamais être lus comme acquis.
- Date de création, date de clôture et régime de TVA à arrêter avec l'expert-comptable ; CFE non due l'année de création, puis base réduite si la déclaration 1447-C-SD est déposée à temps (audit-work/syn-droit.md:302) : non modélisée ; son montant est [IN] (quelques centaines d'euros par an au plus [HY]) et la ligne « imprévus » le couvre. Si la société est créée en décembre 2026, une première CFE réduite peut tomber en décembre 2027, dans l'horizon.
- **Frais engagés avant l'immatriculation** (conseil sur la fuite, statuts) : supposés repris par la société, TVA récupérée et charges déductibles [HY]. La fuite concerne un traitement antérieur à Marwin : si le conseil n'est pas un acte de la société en formation, il reste à la charge des associés, sans TVA récupérable ni déduction (question 5 de `structures.md`).
- **Crédit de TVA** : il n'est pas compté dans la trésorerie disponible (prudence) ; il se récupère par imputation ou sur demande de remboursement.
- **Déplacements** : TVA récupérée sur la moitié [HY] ; elle ne l'est pas sur les billets de transport de personnes ni sur des indemnités kilométriques. La TVA déductible affichée est donc un peu surévaluée ; l'effet sur la trésorerie est négligeable.
- **Colonne « probabilité cumulée »** : la valeur 1,00 des mois du cadrage est **conditionnelle à la vente du cadrage**, dont la probabilité est [IN] ; ce n'est pas une certitude.
