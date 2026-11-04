# Tests de résistance : scénario central, dix-huit mois

**Document interne.** Il contient des coûts, des marges, des rémunérations visées et des probabilités : il ne doit pas être transmis à GianLuca Carlone (audit-work/strategie-retenue.md:787-789).

Produit le 4 novembre 2026 par `modele_financier.py` (même dossier), qui contient tous les paramètres, leur code et leur source. Pour changer une hypothèse, modifier le paramètre en tête du script et le relancer. « audit-work/ » désigne le dossier de travail de l'audit (hors dépôt) ; les autres chemins renvoient au dépôt (commit 7b46602).

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] mesure ; [IN] inconnu. **Tous les résultats chiffrés sont des [ES]**, arrondis à la centaine d'euros (à la dizaine pour les prix par JP) : un total peut différer de 100 à 200 € de la somme de ses lignes arrondies. Les fourchettes combinent frais bas et coefficient social bas, puis frais hauts et coefficient haut.

**Impôt sur le revenu non calculé** : les situations fiscales des foyers de Morgan Olsen et de Mathys Couet sont [IN] (audit-work/rj-R1-structures.md:15 ; audit-work/syn-droit.md:93). Tous les nets sont « avant impôt sur le revenu ».


**Trois faits pris comme base** (audit-work/strategie-retenue.md:29-33) :
1. **Aucun contrat, aucune facture, aucune entité payeuse identifiée** [FV négatif]. Le « contrat certain » vaut donc **0 €** dans tous les scénarios : chaque euro de chiffre d'affaires ci-dessous est une hypothèse.
2. **Medhi et BOJ.ART retirés de l'offre** le 4 nov. 2026 à la demande de Morgan [DR] (audit-work/note-point-4-novembre-et-activites.md:25). Seul le diaporama client a été corrigé (11 diapositives) ; l'offre écrite, STRATES v1.1, le vernissage et le PDF de 13 diapositives de la PR n° 1 ne l'ont pas été [FV] (audit-work/strategie-retenue.md:31). Le modèle ne compte **aucune recette ni dépense** pour STRATES, la création, le laboratoire ou le vernissage « signature ».
3. **Fuite de données très probable** (dépôt public FinanceScope/CRM-Carlone) ; délai CNIL de 72 h possiblement échu le 5 nov. si la connaissance date du 2 nov. [ES] (audit-work/strategie-retenue.md:32). Le modèle compte le conseil (avocat ou DPD) dans les frais de démarrage de novembre 2026 [HY] ; une sanction, une action des personnes ou un refus d'assurance ne sont **pas chiffrés** [IN]. Rien ne démarre tant que la fuite n'est pas traitée (audit-work/strategie-retenue.md:53, 660).


## Méthode

- Base : scénario central (`tresorerie-18-mois.md`), novembre 2026 à avril 2028, apport de 10 000 €, enveloppe de rémunération de 4 700 € par mois dès le mois 4. Point bas de la trésorerie disponible de la base : 3 100 € en déc. 2026.
- **Besoin de financement maximal** = montant qu'il faudrait apporter en plus pour que la trésorerie disponible (banque − TVA due) ne devienne jamais négative sur les 18 mois. **Mois critique** = premier mois où la trésorerie disponible devient négative ; à défaut, mois où la perte par rapport à la base est maximale.
- Chaque test est calculé deux fois : **A, sans réaction** (on continue comme prévu) et **B, avec la règle de protection** prévue par la stratégie (audit-work/strategie-retenue.md:524-537). La différence entre A et B mesure ce que la règle protège.
- Objectif de réserve au mois 12 [PR] : 3 mois de frais fixes et 1 mois de rémunération, soit 10 700 € (audit-work/strategie-retenue.md:175).
- L'IS n'est pas payé dans l'horizon (exercice 2027 soldé en mai 2028) ; il baisse quand le résultat baisse.


## 1. Synthèse

| Test | Besoin de financement maximal, A (sans réaction) | Besoin maximal, B (avec la règle) | Besoin pour garder un mois de charges en caisse, A ; B | Mois critique (A) | Perte maximale de trésorerie par rapport à la base, A ; B | Écart à 18 mois, A ; B | Réserve cible du mois 12 manquée (A) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Retard de paiement de 30 jours | 0 € | 0 € | 0 € ; 0 € | mai 2027 | 8 000 € ; 3 300 € | −8 000 € ; −3 300 € | non |
| Retard de paiement de 60 jours | 0 € | 0 € | 3 600 € ; 0 € | juin 2027 | 16 000 € ; 6 600 € | −16 000 € ; −6 600 € | oui |
| Retard de paiement de 90 jours | 3 400 € | 0 € | 10 400 € ; 0 € | juin 2027 (sous zéro) | 24 000 € ; 9 900 € | −24 000 € ; −9 900 € | oui |
| Rupture brutale à la fin du pilote (mois 3) | 21 300 € | 1 700 € | 22 500 € ; 2 800 € | juin 2027 (sous zéro) | 53 600 € ; 33 900 € | −53 600 € ; −33 900 € | oui |
| Rupture brutale après le premier trimestre de socle (mois 6) | 12 600 € | 0 € | 13 700 € ; 0 € | sept. 2027 (sous zéro) | 44 900 € ; 25 200 € | −44 900 € ; −25 200 € | oui |
| Pas de renouvellement après six mois de socle | 3 100 € | 0 € | 4 200 € ; 0 € | mars 2028 (sous zéro) | 35 300 € ; 15 600 € | −35 300 € ; −15 600 € | oui |
| Dépassement d'un développement de 50 % | 0 € | 0 € | 0 € ; 0 € | mars 2027 | 3 600 € ; 3 600 € | −3 000 € ; −800 € | non |
| Hausse des coûts d'IA | 0 € | 0 € | 0 € ; 0 € | avr. 2028 | 16 000 € ; 2 400 € | −16 000 € ; −2 400 € | non |
| Indisponibilité d'un associé pendant six semaines | 0 € | 0 € | 0 € ; 0 € | juil. 2027 | 9 000 € ; 4 300 € | −9 000 € ; −4 300 € | non |
| Plusieurs urgences simultanées | 0 € | 0 € | 0 € ; 0 € | juil. 2027 | 2 700 € ; 0 € | −2 700 € ; 2 700 € | non |
| Arrêt d'un fournisseur technique | 0 € | 0 € | 0 € ; 0 € | sept. 2027 | 3 500 € ; 1 100 € | −3 500 € ; −1 100 € | non |
| Abandon ou retard du projet artistique | 0 € | 0 € | 0 € ; 0 € | juin 2027 | 11 600 € ; 0 € | −11 600 € ; 0 € | non |
| Croissance commerciale plus lente | 0 € | 0 € | 0 € ; 0 € | avr. 2028 | 21 200 € ; 7 900 € | −21 200 € ; −4 000 € | non |


Lecture : le **besoin de financement** est l'apport supplémentaire qui empêche la trésorerie disponible de devenir négative ; le **besoin pour garder un mois de charges** est plus prudent (frais et rémunérations du mois toujours couverts). Un besoin de 0 € signifie que l'apport et le coussin du pilote suffisent : cela ne veut pas dire que le test est sans gravité. La **perte maximale** mesure la trésorerie perdue, au pire moment, par rapport à la base ; le **mois critique** est le premier mois sous zéro, ou à défaut le mois de cette perte maximale.


## 2. Détail des dix tests


### Retard de paiement de 30 jours

**Hypothèse** [HY] : À partir du mois 4 (avr. 2027), chaque paiement de l'entité de GianLuca arrive 30 jours après l'échéance, durablement. A : Marwin continue de travailler et de payer les associés. B : la rémunération n'est versée que sur les encaissements reçus (décalée du même retard).

| Mesure [ES] | A, sans réaction | B, avec la règle |
| --- | --- | --- |
| Besoin de financement maximal (trésorerie jamais négative) | 0 € | 0 € |
| Besoin pour garder un mois de charges en caisse | 0 € | 0 € |
| Point bas de la trésorerie disponible (mois) | 3 100 € (déc. 2026) | 3 100 € (déc. 2026) |
| Premier mois sous zéro | aucun | aucun |
| Perte maximale par rapport à la base (mois) | 8 000 € (mai 2027) | 3 300 € (mai 2027) |
| dont crédit de TVA au point bas (remboursable sur demande, non compté) | 1 100 € | 1 100 € |
| Trésorerie disponible au mois 12 | 19 000 € | 23 800 € |
| Manque par rapport à la réserve cible du mois 12 | 0 € | 0 € |
| Écart de trésorerie à 18 mois avec la base | −8 000 € | −3 300 € |


**Engagements devenus intenables** : Payer les associés à l'échéance prévue ; lancer un nouveau lot ; tout engagement de frais nouveau. 

**Mesure de protection** [PR] : Relance le lendemain de l'échéance ; suspension des travaux non urgents 8 jours après une relance sans effet ; résiliation possible à 30 jours ; pénalités ≥ 3 fois le taux légal et 40 € par facture [FV] (audit-work/strategie-retenue.md:463) ; socle payé d'avance ; aucune rémunération sans encaissement. La TVA, exigible à l'encaissement, n'est pas avancée [FV].


### Retard de paiement de 60 jours

**Hypothèse** [HY] : À partir du mois 4 (avr. 2027), chaque paiement de l'entité de GianLuca arrive 60 jours après l'échéance, durablement. A : Marwin continue de travailler et de payer les associés. B : la rémunération n'est versée que sur les encaissements reçus (décalée du même retard).

| Mesure [ES] | A, sans réaction | B, avec la règle |
| --- | --- | --- |
| Besoin de financement maximal (trésorerie jamais négative) | 0 € | 0 € |
| Besoin pour garder un mois de charges en caisse | 3 600 € | 0 € |
| Point bas de la trésorerie disponible (mois) | 3 100 € (déc. 2026) | 3 100 € (déc. 2026) |
| Premier mois sous zéro | aucun | aucun |
| Perte maximale par rapport à la base (mois) | 16 000 € (juin 2027) | 6 600 € (juin 2027) |
| dont crédit de TVA au point bas (remboursable sur demande, non compté) | 1 100 € | 1 100 € |
| Trésorerie disponible au mois 12 | 11 000 € | 20 500 € |
| Manque par rapport à la réserve cible du mois 12 | 2 200 € | 0 € |
| Écart de trésorerie à 18 mois avec la base | −16 000 € | −6 600 € |


**Engagements devenus intenables** : Payer les associés à l'échéance prévue ; lancer un nouveau lot ; tout engagement de frais nouveau. À 60 jours et plus, le contrat lui-même devient intenable.

**Mesure de protection** [PR] : Relance le lendemain de l'échéance ; suspension des travaux non urgents 8 jours après une relance sans effet ; résiliation possible à 30 jours ; pénalités ≥ 3 fois le taux légal et 40 € par facture [FV] (audit-work/strategie-retenue.md:463) ; socle payé d'avance ; aucune rémunération sans encaissement. La TVA, exigible à l'encaissement, n'est pas avancée [FV].


### Retard de paiement de 90 jours

**Hypothèse** [HY] : À partir du mois 4 (avr. 2027), chaque paiement de l'entité de GianLuca arrive 90 jours après l'échéance, durablement. A : Marwin continue de travailler et de payer les associés. B : la rémunération n'est versée que sur les encaissements reçus (décalée du même retard).

| Mesure [ES] | A, sans réaction | B, avec la règle |
| --- | --- | --- |
| Besoin de financement maximal (trésorerie jamais négative) | 3 400 € | 0 € |
| Besoin pour garder un mois de charges en caisse | 10 400 € | 0 € |
| Point bas de la trésorerie disponible (mois) | −3 400 € (juil. 2027) | 3 100 € (déc. 2026) |
| Premier mois sous zéro | juin 2027 | aucun |
| Perte maximale par rapport à la base (mois) | 24 000 € (juil. 2027) | 9 900 € (juil. 2027) |
| dont crédit de TVA au point bas (remboursable sur demande, non compté) | 0 € | 1 100 € |
| Trésorerie disponible au mois 12 | 3 000 € | 17 200 € |
| Manque par rapport à la réserve cible du mois 12 | 10 200 € | 0 € |
| Écart de trésorerie à 18 mois avec la base | −24 000 € | −9 900 € |


**Engagements devenus intenables** : Payer les associés à l'échéance prévue ; lancer un nouveau lot ; tout engagement de frais nouveau. À 60 jours et plus, le contrat lui-même devient intenable.

**Mesure de protection** [PR] : Relance le lendemain de l'échéance ; suspension des travaux non urgents 8 jours après une relance sans effet ; résiliation possible à 30 jours ; pénalités ≥ 3 fois le taux légal et 40 € par facture [FV] (audit-work/strategie-retenue.md:463) ; socle payé d'avance ; aucune rémunération sans encaissement. La TVA, exigible à l'encaissement, n'est pas avancée [FV].


### Rupture brutale à la fin du pilote (mois 3)

**Hypothèse** [HY] : L'entité de GianLuca arrête tout fin mars 2027 sans préavis et ne paie pas le dernier solde de lot ; aucun autre client avant avril 2028. A : réaction tardive, rémunération versée trois mois de plus, frais de 2 000 € maintenus six mois puis ramenés à 1 000 €. B : règle appliquée, rémunération arrêtée, frais ramenés à 1 000 € par mois après un mois.

| Mesure [ES] | A, sans réaction | B, avec la règle |
| --- | --- | --- |
| Besoin de financement maximal (trésorerie jamais négative) | 21 300 € | 1 700 € |
| Besoin pour garder un mois de charges en caisse | 22 500 € | 2 800 € |
| Point bas de la trésorerie disponible (mois) | −21 300 € (avr. 2028) | −1 700 € (avr. 2028) |
| Premier mois sous zéro | juin 2027 | mars 2028 |
| Perte maximale par rapport à la base (mois) | 53 600 € (avr. 2028) | 33 900 € (avr. 2028) |
| dont crédit de TVA au point bas (remboursable sur demande, non compté) | 2 100 € | 1 600 € |
| Trésorerie disponible au mois 12 | −16 900 € | 2 800 € |
| Manque par rapport à la réserve cible du mois 12 | 27 600 € | 7 900 € |
| Écart de trésorerie à 18 mois avec la base | −53 600 € | −33 900 € |


**Engagements devenus intenables** : Les frais fixes de 2 000 € par mois et toute rémunération ; un abonnement ou un engagement de plus de trois mois ; le revenu des associés tiré de Marwin.

**Mesure de protection** [PR] : Préavis d'un mois et mois en cours dû (audit-work/strategie-retenue.md:465) ; acompte et solde à la livraison ; réserve visant six mois de frais réduits (audit-work/strategie-retenue.md:529) ; revenus extérieurs maintenus ; abonnements résiliables au mois.


### Rupture brutale après le premier trimestre de socle (mois 6)

**Hypothèse** [HY] : L'entité de GianLuca arrête tout fin juin 2027 sans préavis et ne paie pas le dernier solde de lot ; aucun autre client avant avril 2028. A : réaction tardive, rémunération versée trois mois de plus, frais de 2 000 € maintenus six mois puis ramenés à 1 000 €. B : règle appliquée, rémunération arrêtée, frais ramenés à 1 000 € par mois après un mois.

| Mesure [ES] | A, sans réaction | B, avec la règle |
| --- | --- | --- |
| Besoin de financement maximal (trésorerie jamais négative) | 12 600 € | 0 € |
| Besoin pour garder un mois de charges en caisse | 13 700 € | 0 € |
| Point bas de la trésorerie disponible (mois) | −12 600 € (avr. 2028) | 3 100 € (déc. 2026) |
| Premier mois sous zéro | sept. 2027 | aucun |
| Perte maximale par rapport à la base (mois) | 44 900 € (avr. 2028) | 25 200 € (avr. 2028) |
| dont crédit de TVA au point bas (remboursable sur demande, non compté) | 1 800 € | 1 100 € |
| Trésorerie disponible au mois 12 | −8 200 € | 11 500 € |
| Manque par rapport à la réserve cible du mois 12 | 18 900 € | 0 € |
| Écart de trésorerie à 18 mois avec la base | −44 900 € | −25 200 € |


**Engagements devenus intenables** : Les frais fixes de 2 000 € par mois et toute rémunération ; un abonnement ou un engagement de plus de trois mois ; le revenu des associés tiré de Marwin.

**Mesure de protection** [PR] : Préavis d'un mois et mois en cours dû (audit-work/strategie-retenue.md:465) ; acompte et solde à la livraison ; réserve visant six mois de frais réduits (audit-work/strategie-retenue.md:529) ; revenus extérieurs maintenus ; abonnements résiliables au mois.


### Pas de renouvellement après six mois de socle

**Hypothèse** [HY] : Le socle n'est pas renouvelé après sept. 2027 (fin du deuxième trimestre) ; le dernier lot est livré et payé ; aucun autre client avant avril 2028. A : rémunération versée trois mois de plus, frais de 2 000 € maintenus six mois puis ramenés à 1 000 €. B : rémunération arrêtée à la fin du socle, frais ramenés à 1 000 € après un mois.

| Mesure [ES] | A, sans réaction | B, avec la règle |
| --- | --- | --- |
| Besoin de financement maximal (trésorerie jamais négative) | 3 100 € | 0 € |
| Besoin pour garder un mois de charges en caisse | 4 200 € | 0 € |
| Point bas de la trésorerie disponible (mois) | −3 100 € (avr. 2028) | 3 100 € (déc. 2026) |
| Premier mois sous zéro | mars 2028 | aucun |
| Perte maximale par rapport à la base (mois) | 35 300 € (avr. 2028) | 15 600 € (avr. 2028) |
| dont crédit de TVA au point bas (remboursable sur demande, non compté) | 1 200 € | 1 100 € |
| Trésorerie disponible au mois 12 | 4 700 € | 21 000 € |
| Manque par rapport à la réserve cible du mois 12 | 6 000 € | 0 € |
| Écart de trésorerie à 18 mois avec la base | −35 300 € | −15 600 € |


**Engagements devenus intenables** : Une rémunération régulière tirée de Marwin ; les frais de 2 000 € ; la dépendance à un seul client.

**Mesure de protection** [PR] : Pas de tacite reconduction, renouvellement écrit un mois avant ; prospection de 1,5 à 2,5 JP par mois dès le mois 1 (audit-work/strategie-retenue.md:719) ; bascule vers d'autres clients ; réserve.


### Dépassement d'un développement de 50 %

**Hypothèse** [HY] : Le lot du pilote (6 000 € HT, ≈ 6,7 JP) demande 3,3 JP de plus et est livré un mois plus tard ; le travail en plus prend, au mois 4, la place de lots pour ≈ 3 000 € HT (plafond de 10 JP). A : dépassement de notre fait, entièrement absorbé. B : la provision de risque (0,8 JP) est absorbée, le reste (2,5 JP) est facturé par avenant signé avant le travail (cause chez le client).

| Mesure [ES] | A, sans réaction | B, avec la règle |
| --- | --- | --- |
| Besoin de financement maximal (trésorerie jamais négative) | 0 € | 0 € |
| Besoin pour garder un mois de charges en caisse | 0 € | 0 € |
| Point bas de la trésorerie disponible (mois) | 3 100 € (déc. 2026) | 3 100 € (déc. 2026) |
| Premier mois sous zéro | aucun | aucun |
| Perte maximale par rapport à la base (mois) | 3 600 € (mars 2027) | 3 600 € (mars 2027) |
| dont crédit de TVA au point bas (remboursable sur demande, non compté) | 1 100 € | 1 100 € |
| Trésorerie disponible au mois 12 | 24 000 € | 26 300 € |
| Manque par rapport à la réserve cible du mois 12 | 0 € | 0 € |
| Écart de trésorerie à 18 mois avec la base | −3 000 € | −800 € |


**Engagements devenus intenables** : Temps non payé valant 2 000 à 2 500 € au coût complet central (audit-work/strategie-retenue.md:364) ; un pilote livré en retard compromet la décision de poursuivre.

**Mesure de protection** [PR] : Provision de risque de 10 à 15 % dans chaque devis ; jalon écrit au-delà de 8 JP ; avenant signé **avant** tout travail supplémentaire (audit-work/strategie-retenue.md:287) ; plafond de 10 JP.


### Hausse des coûts d'IA

**Hypothèse** [HY] : Les outils et API coûtent 150 € (B, plafond de consommation et modèle de repli) ou 1 000 € (A, sans garde-fou) de plus par mois dès janvier 2027 (doublements annoncés chez un fournisseur au 1er déc. 2026 et au 1er janv. 2027 [FV], audit-work/ver-R6-marche.md:33). Rémunération inchangée.

| Mesure [ES] | A, sans réaction | B, avec la règle |
| --- | --- | --- |
| Besoin de financement maximal (trésorerie jamais négative) | 0 € | 0 € |
| Besoin pour garder un mois de charges en caisse | 0 € | 0 € |
| Point bas de la trésorerie disponible (mois) | 3 100 € (déc. 2026) | 3 100 € (déc. 2026) |
| Premier mois sous zéro | aucun | aucun |
| Perte maximale par rapport à la base (mois) | 16 000 € (avr. 2028) | 2 400 € (avr. 2028) |
| dont crédit de TVA au point bas (remboursable sur demande, non compté) | 1 100 € | 1 100 € |
| Trésorerie disponible au mois 12 | 15 000 € | 25 200 € |
| Manque par rapport à la réserve cible du mois 12 | 0 € | 0 € |
| Écart de trésorerie à 18 mois avec la base | −16 000 € | −2 400 € |


**Engagements devenus intenables** : À +1 000 € par mois, l'enveloppe soutenable tombe de 4 700 € à 3 800 € par mois : le net par associé baisse d'environ 300 € par mois.

**Mesure de protection** [PR] : Plafond de consommation mensuel ; deux fournisseurs configurés ; modèle moins cher par défaut ; clause de révision ; outils et licences du client à son nom et à sa charge (audit-work/rj-R6-marche.md:387-390).


### Indisponibilité d'un associé pendant six semaines

**Hypothèse** [HY] : Un associé est absent en mai 2027 et juin 2027 ; capacité ramenée à 4 à 8 JP. Le socle passe au palier B0 (3 500 € HT) sans pénalité ; les lots de ces deux mois ne sont pas commandés. A : rémunérations maintenues. B : la rémunération de l'associé absent est suspendue.

| Mesure [ES] | A, sans réaction | B, avec la règle |
| --- | --- | --- |
| Besoin de financement maximal (trésorerie jamais négative) | 0 € | 0 € |
| Besoin pour garder un mois de charges en caisse | 0 € | 0 € |
| Point bas de la trésorerie disponible (mois) | 3 100 € (déc. 2026) | 3 100 € (déc. 2026) |
| Premier mois sous zéro | aucun | aucun |
| Perte maximale par rapport à la base (mois) | 9 000 € (juil. 2027) | 4 300 € (juil. 2027) |
| dont crédit de TVA au point bas (remboursable sur demande, non compté) | 1 100 € | 1 100 € |
| Trésorerie disponible au mois 12 | 18 000 € | 22 800 € |
| Manque par rapport à la réserve cible du mois 12 | 0 € | 0 € |
| Écart de trésorerie à 18 mois avec la base | −9 000 € | −4 300 € |


**Engagements devenus intenables** : Les lots promis pendant l'absence ; les délais de réception ; le contrôle à quatre yeux, qui suppose deux personnes.

**Mesure de protection** [PR] : Binôme de secours et procédures écrites ; changement de palier sans pénalité au-delà de 10 jours ouvrés (audit-work/strategie-retenue.md:84, 533) ; prévoyance à souscrire (indemnités journalières plafonnées à 41,95 € en SAS [FV], audit-work/syn-droit.md:113) ; coffre partagé des accès.


### Plusieurs urgences simultanées

**Hypothèse** [HY] : Deux urgences de 1,5 JP chacune en juin 2027. A : absorbées gratuitement, elles prennent la place des lots du mois (≈ 2 700 € HT perdus). B : facturées par avenant à 900 € HT par JP, en fin de mois, sous 15 jours ; charge du mois portée à 11,9 JP pour un plafond de 10.

| Mesure [ES] | A, sans réaction | B, avec la règle |
| --- | --- | --- |
| Besoin de financement maximal (trésorerie jamais négative) | 0 € | 0 € |
| Besoin pour garder un mois de charges en caisse | 0 € | 0 € |
| Point bas de la trésorerie disponible (mois) | 3 100 € (déc. 2026) | 3 100 € (déc. 2026) |
| Premier mois sous zéro | aucun | aucun |
| Perte maximale par rapport à la base (mois) | 2 700 € (juil. 2027) | 0 € (nov. 2026) |
| dont crédit de TVA au point bas (remboursable sur demande, non compté) | 1 100 € | 1 100 € |
| Trésorerie disponible au mois 12 | 24 300 € | 29 700 € |
| Manque par rapport à la réserve cible du mois 12 | 0 € | 0 € |
| Écart de trésorerie à 18 mois avec la base | −2 700 € | 2 700 € |


**Engagements devenus intenables** : Le plafond de 10 JP et l'occupation à 85 % au plus ; les délais des lots en cours.

**Mesure de protection** [PR] : Liste fermée des urgences ; arrêt sans autorisation, tout travail en plus par avenant (audit-work/strategie-retenue.md:354, 597) ; au-delà de 90 % des JP réservées avant le 20 du mois, arrêt des travaux non urgents (audit-work/strategie-retenue.md:593).


### Arrêt d'un fournisseur technique

**Hypothèse** [HY] : Un outil central (registre, IA, hébergement) s'arrête en août 2027. A : sans export testé, 3 JP de reprise non facturables, deux mois de double abonnement (300 € par mois), deux engagements de service manqués (malus de 5 % du socle en avoir). B : exports mensuels testés et mode manuel écrit, 1 JP de bascule, un mois d'outil de remplacement.

| Mesure [ES] | A, sans réaction | B, avec la règle |
| --- | --- | --- |
| Besoin de financement maximal (trésorerie jamais négative) | 0 € | 0 € |
| Besoin pour garder un mois de charges en caisse | 0 € | 0 € |
| Point bas de la trésorerie disponible (mois) | 3 100 € (déc. 2026) | 3 100 € (déc. 2026) |
| Premier mois sous zéro | aucun | aucun |
| Perte maximale par rapport à la base (mois) | 3 500 € (sept. 2027) | 1 100 € (sept. 2027) |
| dont crédit de TVA au point bas (remboursable sur demande, non compté) | 1 100 € | 1 100 € |
| Trésorerie disponible au mois 12 | 23 500 € | 26 000 € |
| Manque par rapport à la réserve cible du mois 12 | 0 € | 0 € |
| Écart de trésorerie à 18 mois avec la base | −3 500 € | −1 100 € |


**Engagements devenus intenables** : Les engagements de service du socle (comptes rendus, registre) pendant la bascule ; la réversibilité promise si les exports ne sont pas testés.

**Mesure de protection** [PR] : Exports mensuels testés, restauration dans un espace neuf, mode manuel écrit ; comptes ouverts au nom du client (audit-work/strategie-retenue.md:189, 535).


### Abandon ou retard du projet artistique

**Hypothèse** [HY] : B (règle retenue) : STRATES, la création avec Medhi et le laboratoire sont hors du CA ; leur abandon ou leur retard ne change rien au plan. A (contre-épreuve, si Marwin avait gardé les options des archives) : Marwin avance un DGX Spark (≈ 6 200 € HT) au mois 2 et consacre 3 JP par mois aux mois 4 et 5 à STRATES, non facturés, à la place de lots ; le projet est ensuite abandonné.

| Mesure [ES] | A, sans réaction | B, avec la règle |
| --- | --- | --- |
| Besoin de financement maximal (trésorerie jamais négative) | 0 € | 0 € |
| Besoin pour garder un mois de charges en caisse | 0 € | 0 € |
| Point bas de la trésorerie disponible (mois) | 3 100 € (déc. 2026) | 3 100 € (déc. 2026) |
| Premier mois sous zéro | aucun | aucun |
| Perte maximale par rapport à la base (mois) | 11 600 € (juin 2027) | 0 € (nov. 2026) |
| dont crédit de TVA au point bas (remboursable sur demande, non compté) | 1 100 € | 1 100 € |
| Trésorerie disponible au mois 12 | 15 400 € | 27 000 € |
| Manque par rapport à la réserve cible du mois 12 | 0 € | 0 € |
| Écart de trésorerie à 18 mois avec la base | −11 600 € | 0 € |


**Engagements devenus intenables** : Toute avance de matériel, de fabrication ou de temps pour un projet sans financeur écrit ; les documents non corrigés (offre écrite, STRATES v1.1, vernissage, PDF de 13 diapositives) qui laissent croire à un engagement (audit-work/strategie-retenue.md:31).

**Mesure de protection** [PR] : Rien d'exploratoire sans financeur écrit, budget plafonné et critère d'arrêt (audit-work/strategie-retenue.md:190, 644-645) ; achats au nom du client ; décision écrite sur Medhi ; documents marqués « retirés ».


### Croissance commerciale plus lente

**Hypothèse** [HY] : Le cadrage n'est payé qu'à la date butoir (mois 1 = févr. 2027) ; les lots ne représentent que 1 750 € HT par mois ; aucun second client. A : rémunération du scénario central maintenue. B : rémunération recalculée sur le chiffre d'affaires réel.

| Mesure [ES] | A, sans réaction | B, avec la règle |
| --- | --- | --- |
| Besoin de financement maximal (trésorerie jamais négative) | 0 € | 0 € |
| Besoin pour garder un mois de charges en caisse | 0 € | 0 € |
| Point bas de la trésorerie disponible (mois) | 3 100 € (janv. 2027) | 3 100 € (janv. 2027) |
| Premier mois sous zéro | aucun | aucun |
| Perte maximale par rapport à la base (mois) | 21 200 € (avr. 2028) | 7 900 € (févr. 2027) |
| dont crédit de TVA au point bas (remboursable sur demande, non compté) | 1 100 € | 1 100 € |
| Trésorerie disponible au mois 12 | 12 300 € | 25 300 € |
| Manque par rapport à la réserve cible du mois 12 | 0 € | 0 € |
| Écart de trésorerie à 18 mois avec la base | −21 200 € | −4 000 € |


**Engagements devenus intenables** : La rémunération centrale : l'enveloppe soutenable tombe à 3 300 € par mois, soit 900 à 1 000 € nets par associé ; la cible de dépendance (80 % au plus) ; la sortie des autres revenus des associés.

**Mesure de protection** [PR] : Plancher de prospection de 1,5 à 2,5 JP par mois ; dates butoirs du 15 déc. 2026 et du 31 janv. 2027 (audit-work/strategie-retenue.md:44, 719) ; revenus extérieurs maintenus ; dépendance à assumer par écrit [PR].


## 3. Ce que montrent ces tests

- Le test le plus coûteux sans réaction est « Rupture brutale à la fin du pilote (mois 3) » : besoin de 21 300 €, trésorerie sous zéro à partir de juin 2027. Avec la règle, le besoin tombe à 1 700 €.
- La protection principale n'est pas la réserve, mais **la règle « pas de rémunération sans encaissement »** et l'arrêt rapide des frais : elles transforment un besoin de financement en baisse de revenu des associés.
- Sans réaction, 4 situations rendent la trésorerie négative : retard de paiement de 90 jours, 3 400 € ; rupture brutale à la fin du pilote (mois 3), 21 300 € ; rupture brutale après le premier trimestre de socle (mois 6), 12 600 € ; pas de renouvellement après six mois de socle, 3 100 €. Avec la règle, un besoin ne subsiste que pour : rupture brutale à la fin du pilote (mois 3), 1 700 €, dont 1 600 € de crédit de TVA qu'un remboursement demandé à temps couvrirait.
- Dans tous ces cas, la règle protège la société en reportant le choc sur le revenu des associés : **Morgan et Mathys doivent garder d'autres revenus** jusqu'au deuxième renouvellement du socle (audit-work/strategie-retenue.md:771).
- Le projet artistique est sans effet tant qu'il reste hors du chiffre d'affaires et qu'aucune avance n'est faite ; il redevient le premier risque si Marwin avance du matériel ou du temps.


## 4. Limites

- Les tests sont appliqués un par un ; leur cumul (par exemple un retard et une absence) aggraverait les besoins.
- Les retards sont supposés durables à partir du mois 4 ; un retard ponctuel coûte moins.
- Les comportements de paiement de l'entité de GianLuca sont [IN] (audit-work/strategie-retenue.md:467).
- Les règles B sont des propositions [PR] ; elles ne protègent que si elles sont écrites au contrat et au pacte, et appliquées.
- Le crédit de TVA (TVA payée sur les frais quand plus rien n'est encaissé) n'est pas compté dans la trésorerie disponible : les besoins sont donc légèrement surestimés quand l'activité s'arrête ; la ligne « dont crédit de TVA » de chaque test le chiffre. Un remboursement se demande auprès du service des impôts des entreprises.
- L'IS n'est jamais payé dans l'horizon (mai 2028) : une rupture n'en économise que la provision.
