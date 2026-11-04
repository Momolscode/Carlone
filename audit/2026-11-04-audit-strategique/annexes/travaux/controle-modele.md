# Contrôle du modèle financier (audit Marwin Tech × GianLuca Carlone, 4 novembre 2026)

**Document interne.** Il porte sur des coûts, des rémunérations et des probabilités : rien de ce contrôle ne doit être transmis à GianLuca Carlone (strategie-retenue.md:787-789).

## 0. Objet, pièces et méthode

- **Objet contrôlé** : `audit/2026-11-04-audit-strategique/annexes/modele-financier/` : le script `modele_financier.py` et ses cinq sorties (`scenarios.md`, `tresorerie-18-mois.csv`, `tresorerie-18-mois.md`, `stress-tests.md`, `structures.md`).
- **Référence** : `audit-work/strategie-retenue.md` (sections 4 à 7), et les mémos qu'elle cite (rj-R1, ver-R1, ver-R6, syn-droit).
- **Version d'origine conservée** (avant correction) : `[dossier de travail] ctrl-modele/modele_financier_orig.py` (1 867 lignes) et ses sorties dans `[dossier de travail] ctrl-modele/orig-outputs/`. Les numéros de ligne « orig. l. N » renvoient à cette copie ; « l. N » renvoie au script corrigé (1 984 lignes).
- **Méthode** : lecture ligne à ligne ; nouvelle exécution de la version d'origine (sorties identiques, octet pour octet, aux fichiers déposés) ; calculs clés refaits à la main ou en Python indépendant ; corrections dans le script ; nouvelle exécution sur place ; comparaison des sorties avant et après.
- **Aucune action extérieure** : aucun contact, aucune dépense, aucun fichier modifié en dehors du dossier du modèle et de ce fichier. Le dossier `audit/` n'est pas suivi par Git (vérifié par `git status`, 4 nov. 2026).
- **Faits nouveaux intégrés** : (1) retrait de Medhi et de BOJ.ART le 4 nov. [DR] (note-point-4-novembre-et-activites.md:25), seul le diaporama de 11 diapositives étant corrigé, ni l'offre écrite, ni STRATES v1.1, ni le vernissage, ni le PDF de 13 diapositives de la PR n° 1 [FV] (strategie-retenue.md:31) ; (2) violation de données très probable (dépôt public FinanceScope/CRM-Carlone), délai CNIL de 72 h possiblement échu le 5 nov. [ES] (strategie-retenue.md:32 ; rj-R4) ; (3) aucun contrat, aucune facture, aucune entité payeuse [FV négatif] (strategie-retenue.md:33). Le modèle les reprend correctement : contrat certain à 0 € partout, aucune recette ni dépense pour STRATES, la création, le laboratoire ou le vernissage, conseil sur la fuite en novembre 2026 (orig. l. 188-199, 736-748).

## 1. Verdict

**Le cœur du modèle est juste** [ES contrôlée] : chiffre d'affaires, TVA, rémunération, IS, trésorerie et seuils se recalculent à l'identique, et les contrôles internes tiennent. **Six défauts ont été corrigés**, dont un qui faussait une conclusion (la comparaison salaire / dividendes). **Aucun chiffre principal ne change** : CA, enveloppe de rémunération, nets, IS, trésorerie et CSV restent identiques. Les corrections portent sur la comparaison des dividendes, un paramètre inopérant, l'affichage des prix par JP, la lecture des tests de résistance et des hypothèses présentées comme acquises. Les sorties ont été régénérées et revérifiées.

## 2. Calculs refaits à la main

| Calcul (scénario central sauf mention) | Recalcul indépendant | Sortie du modèle | Verdict |
| --- | --- | --- | --- |
| CA facturé, mois 1 à 12 | 6 500 (cadrage) + 7 000 (B0) + 6 000 (lot du pilote) + 9 × 4 500 (B1) + 9 × 1 400 (acomptes de lots) + 8 × 2 100 (soldes des mois 5 à 12) = **89 400 € HT** | 89 400 € | Exact |
| Enveloppe de rémunération E | Mois 4 à 12 : 69 900 × 0,9 − 9 × 2 000 = 44 910 € disponibles ; résultat sans rémunération 89 400 − 24 000 − 6 000 = 59 400 € ; 9E + 15 % × (59 400 − 9E) = 44 910 ⇒ **E = 4 706 €** par mois ; net = 4 706 ÷ 2 ÷ 1,8 = **1 307 €** par associé | 4 700 € ; ≈ 1 300 € | Exact |
| IS de l'exercice | 15 % × (59 400 − 42 353) = **2 557 €** (bénéfice sous 42 500 €) | 2 600 € | Exact |
| Trésorerie disponible et libre au mois 12 | 10 000 + 89 400 − 24 000 − 6 000 − 42 353 = **27 047 €** ; − réserve 8 940 − IS 2 557 = **15 550 €** | 27 000 € ; 15 600 € | Exact |
| TVA, nov. 2026 à déc. 2027 | Collectée 89 400 × 20 % = 17 880 € ; déductible 400 + 718 + 264 + 11 × 224 = 3 846 € ; due en décembre 1 600 − 224 = 1 376 € ; reversée 17 880 − 3 846 − 1 376 = **12 658 €** | 17 900 / 3 800 / 1 400 / 12 700 € | Exact |
| Point bas | 10 000 − 2 400 (conseil sur la fuite TTC) − 4 518 (statuts et formalités TTC) = **3 082 €** en déc. 2026 | 3 100 € | Exact |
| Prudent : E | Mois 4 à 12 : 40 500 × 0,9 − 13 500 = 22 950 € ; 9E + 15 % × (27 000 − 9E) = 22 950 ⇒ **E = 2 471 €** ; net 686 € | 2 500 € ; ≈ 700 € | Exact |
| Ambitieux : E | 115 600 × 0,9 − 25 200 − 13 500 = 65 340 € ; 9E + 15 % × (87 000 − 9E) = 65 340 ⇒ **E = 6 835 €** ; net 1 899 € | 6 800 € ; ≈ 1 900 € | Exact |
| Seuil de rentabilité | 69 900 € ÷ 80 JP = 873,75 € par JP ; 2 000 ÷ (873,75 × 0,9) = **2,54 JP** ; avec 2 500 € nets par ETP : 8,76 à 9,49 JP | 2,5 ; 8,8 à 9,5 | Exact |
| Dividendes à ressources égales | 9 × 4 706 = 42 353 € versés en dividendes ; IS supplémentaire 10 600 − 2 557 = 8 043 € ; (42 353 − 8 043) ÷ 2 × 0,686 = **11 768 €** par associé | Ancienne sortie : 13 700 € | **Erreur** (n° 1 ci-dessous) |

## 3. Cohérence avec la stratégie retenue

| Paramètre | Stratégie | Modèle | Verdict |
| --- | --- | --- | --- |
| Prix A, B0, B1, socle léger, socle + 3, lots, D, avenant | 6 500 (plancher 6 000) ; 3 500 ; 4 500 ; 3 000 ; 5 700 ; JP × 800 + 10 à 15 % ; 1 000 à 1 500 ; 900 € HT (strategie-retenue.md:194-203, 498) | orig. l. 124-141 | Conforme |
| Échéancier | 50/50 ; mensuel d'avance ; 40/60 (strategie-retenue.md:436-446) | orig. l. 433-467 | Conforme (solde le mois suivant [HY]) |
| Dates du mois 1 | févr. 2027 / janv. 2027 / déc. 2026 (strategie-retenue.md:500) | orig. l. 216, 224, 233 | Conforme |
| Probabilités | 40/60 ; 60/70/80 ; 80/80/90 et 50 % (strategie-retenue.md:502) | orig. l. 152-156 | Conforme ; le plan n'est pas pondéré, la pondération est affichée à part |
| Frais fixes | 1 500 / 2 000 / 2 800 € par mois et leur détail (strategie-retenue.md:504-508) | orig. l. 177-181 | Conforme |
| Démarrage, apport | 4 000-5 000 / 5 000-7 000 / 6 000-8 000 € ; 8 000 / 10 000 / 12 000-14 000 € (strategie-retenue.md:509-510) | 4 500 / 6 000 / 7 000 € ; 8 000 / 10 000 / 13 000 € | Conforme |
| Réserve, IS, coefficient SAS, plafond de 10 JP, rien avant le mois 4 | strategie-retenue.md:478-485, 511 | orig. l. 77-88, 106-108 | Conforme |
| Exploitation D au plus tôt au mois 7 | strategie-retenue.md:339 (texte) ; mois 4 dans le calcul de la stratégie | Mois 7 | Écart avec la stratégie signalé dans `scenarios.md` § 6 : le modèle suit la règle écrite |
| CA sur 12 mois | ≈ 50 000 / 90 000 / 150 000 € (strategie-retenue.md:513) | 49 500 / 89 400 / 141 100 € | Écarts expliqués (soldes décalés, D au mois 7) |
| Tests de résistance | Dix tests (strategie-retenue.md:524-537) | Dix tests, chacun avec et sans règle | Conforme |

## 4. Erreurs trouvées et corrections faites

| N° | Gravité | Constat (version d'origine) | Effet | Correction (script corrigé) |
| --- | --- | --- | --- | --- |
| 1 | **Élevée** (conclusion fausse) | Le tableau des dividendes distribuait **tout le bénéfice de l'année**, réserve conservée, y compris l'excédent des mois 1 à 3 que les scénarios « salaire » laissent dans la société (orig. l. 1670-1684). Il comparait donc des ressources inégales, et concluait : « le dividende laisse pourtant plus de net, faute de cotisations sociales » (orig. l. 1684) | Dividende surestimé par rapport au salaire de **1 900 € par associé en central** (13 700 € contre 11 800 € à ressources égales) et de 2 600 € en ambitieux. **À ressources égales**, le dividende net après PFU (donc après IR) est égal au salaire net de SAS avant IR au coefficient 1,8 (11 768 € contre 11 765 € en central) ; il est **inférieur** en ambitieux (16 400 € contre 17 100 €), car une partie du bénéfice passe à 25 % d'IS [ES] | Nouvelle ligne principale « à ressources égales » (l. 1726-1762). L'ancien calcul reste, marqué « variante non comparable ». Lecture réécrite (`structures.md` § 4, l. 51-60) |
| 2 | Moyenne (paramètre trompeur) | `TVA_DECALAGE = 1` est présenté comme un paramètre (orig. l. 72), mais le décalage d'un mois est écrit en dur (orig. l. 584-590) : changer le paramètre ne changeait rien, alors que l'en-tête invite à modifier les paramètres | Variante « autre régime de TVA » impossible sans retoucher le code | Décalage réellement paramétré (l. 565, 599-605) ; textes adaptés (l. 358) ; **nouveau contrôle** : l'identité de TVA tient et la trésorerie disponible ne change pas à 0, 1 ou 2 mois de décalage (l. 1835-1849). Vérifié : à 2 mois, seule la trésorerie en banque bouge |
| 3 | Moyenne (lecture trompeuse) | Le crédit de TVA n'est pas compté dans la trésorerie disponible (prudent), mais les sorties ne le disaient pas (orig. l. 1210-1232, 1576) | Le seul besoin « avec la règle » (rupture à la fin du pilote : 1 700 €) est fait à **1 600 €** de crédit de TVA remboursable ; la variante basse du prudent (−10 300 €) en compte 1 800 € | Ligne « dont crédit de TVA au point bas » dans chaque test (l. 1280) ; phrase de synthèse complétée (`stress-tests.md`:342) ; limite ajoutée ; variante basse annotée (`scenarios.md` § 5) |
| 4 | Faible (arrondi) | Le prix moyen par JP était arrondi à la centaine (orig. l. 886, 949) : « 900 € » dans les trois scénarios | Il masquait 871, 874 et 856 € par JP, donc l'écart avec le prix cible de 900 € par JP | Arrondi à la dizaine (`eur10`, l. 351) : 870 / 870 / 860 € |
| 5 | Faible (hypothèse présentée comme acquise) | « Dépendance à un seul client : 100 %… **assumée par écrit** » (orig. l. 1192, 1501) | Un écrit qui n'existe pas [IN] était présenté comme fait | « **à assumer par écrit** entre les associés [PR], ce qui n'est pas fait [IN] » (l. 1219, 1550) |
| 6 | Faible (oubli de lecture) | Aucune sensibilité au paiement d'avance de l'assurance ni à la voie du pilote | Point bas (3 100 €) et trésorerie libre (15 600 €) présentés sans leurs deux principales fragilités | Deux calculs ajoutés (l. 1921-1949) : prime de RC professionnelle payée d'avance ⇒ point bas de **700 € (2 400 € par an) à 100 € (3 000 € par an)** en déc. 2026 (`tresorerie-18-mois.md`:135) ; pilote C2 seul ou C6 seul au lieu de B0 + lot ⇒ CA de 82 400 à 83 900 € HT et trésorerie libre de **9 200 à 10 600 €** au mois 12 (`scenarios.md`:232) |

Limites ajoutées dans les sorties : seuil d'IS non proratisé, CFE, frais engagés avant l'immatriculation, TVA des déplacements, sens de la probabilité 1,00, matériel informatique (voir la section 7).

**Après correction** : tous les contrôles internes passent, plus le nouveau contrôle du décalage de TVA ; CA, enveloppes, nets, IS, trésorerie et CSV **identiques** à la version d'origine. Ont changé `structures.md` § 4, les prix par JP, les lignes et limites ajoutées dans les trois fichiers Markdown, et aucune valeur du CSV.

## 5. Points vérifiés sans erreur

- **TVA** : collectée à l'encaissement, y compris pour les acomptes [FV] (rj-R2-fiscal.md:385) ; déductible sur les frais, le démarrage et la sous-traitance ; crédit reporté ; reversée le mois suivant au réel normal mensuel [HY]. La TVA autoliquidée des outils étrangers est neutre. Assurances et banque sont exonérées. L'identité « collectée − déductible = reversée + due − crédit » tient dans les trois scénarios et dans les variantes.
- **Décalages d'encaissement** : socle encaissé le mois du service, solde du cadrage et soldes de lots le mois suivant [HY]. Dans les tests de retard, la TVA suit l'encaissement. Le CA facturé est égal au CA encaissé sur les mois 1 à 12, car toutes les lignes sont encaissées à leur date de facture dans le scénario de base.
- **Cotisations** : SAS au coefficient 1,7 à 1,9 du net [HY] (syn-droit.md:98), payées le mois même. Brut indicatif net ÷ 0,75, cohérent avec la source (rj-R1-structures.md:50). TNS : barème F38152 « revenus 2025 » appliqué à 74 % du coût, conforme aux taux contrôlés (ver-R1-structures.md:20). Le modèle reproduit la synthèse juridique à ± 2 %.
- **IS** : 15 % jusqu'à 42 500 € puis 25 % [FV] (ver-R1-structures.md:21). Pas d'acompte la première année. Solde payé le 15 mai 2028 pour une clôture au 31 déc. 2027, hors de l'horizon de 18 mois, donc provisionné. Avec un IS inférieur à 3 000 € en central, aucun acompte n'est dû en 2028 [HY].
- **Arrondis** : flux arrondis à la centaine avec report (les totaux de colonne sont justes, vérifié par contrôle) ; soldes arrondis directement ; arrondi symétrique pour les montants négatifs.
- **Unités** : JP par mois, € HT par mois, TTC = HT × 1,2. La sous-traitance est retirée des JP des associés et comptée en coût. Aucune confusion HT / TTC trouvée.
- **Double comptage** : aucun. Le socle et les lots ont des JP séparées. La réserve et l'IS ne sont pas déduits deux fois (la réserve n'est pas une sortie). Le conseil sur la fuite au démarrage est distinct du conseil ponctuel mensuel. La mise en place de la facturation électronique est un coût unique ; l'abonnement est dans « divers ». Les achats du client sont hors CA.
- **Tests de résistance** : la logique des dix tests est conforme à la stratégie (strategie-retenue.md:524-537). La règle B ne coûte jamais plus que A dans les tests où elle réduit les sorties.

## 6. Oublis de coûts : vérification ligne par ligne (central)

| Poste | Dans le modèle | Verdict |
| --- | --- | --- |
| Assurance (RC professionnelle, volets IA, cyber, données) | 200 € par mois, montant [IN] (orig. l. 168) | Présent ; **échéancier non modélisé** : une prime annuelle payée d'avance amène le point bas à 100-700 € (correction n° 6) |
| Expert-comptable et paie | 350 € par mois (4 200 € par an) | Présent, dans la fourchette de 2 000 à 5 000 € |
| Banque | 30 € par mois | Présent |
| Outils et IA | 300 € par mois ; hausse de +150 à +1 000 € testée | Présent |
| Déplacements | 500 € par mois, montant [IN] (lieu de résidence inconnu) | Présent ; TVA récupérable surévaluée, effet négligeable (limite ajoutée) |
| CFE | Non modélisée | **Oubli mineur** : montant [IN], probablement quelques centaines d'euros par an au plus [HY] ; une CFE réduite peut tomber en déc. 2027 si la société est créée en déc. 2026 ; couverte par « imprévus » (200 € par mois). Limite précisée |
| Frais de création (statuts, pacte, formalités, bénéficiaires effectifs) | 3 500 € + 300 € (central) | Présent |
| Facture électronique | Mise en place (200 €) + abonnement dans « divers » (220 € par mois) | Présent ; réception obligatoire depuis le 1er sept. 2026 [FV] (syn-droit.md:297) |
| Conseil sur la fuite | 2 000 € en nov. 2026 [HY] | Présent ; **reprise par la société incertaine**, puisque la fuite précède Marwin (limite ajoutée). Sanction, réclamations et franchise d'assurance [IN] non chiffrées |
| Matériel informatique | 200 à 700 € de mise en place seulement | Associés équipés supposés [HY] (limite ajoutée) |
| Mutuelle, prévoyance, ACRE, IR | Exclus | Exclusion signalée dans les sorties |

## 7. Hypothèses présentées comme des faits

- **Corrigé** : « dépendance assumée par écrit » (n° 5).
- **Signalé** : la colonne « probabilité cumulée » vaut 1,00 les mois du cadrage. Cette valeur est conditionnelle à la vente du cadrage, dont la probabilité est [IN] (limite ajoutée à `tresorerie-18-mois.md`).
- **Conforme** : tous les [FV] du script et des sorties renvoient à une pièce contrôlée : taux de TVA, IS, PFU de 31,4 % (ver-R1-structures.md:22), PASS 48 060 €, forfaits TNS (ver-R1-structures.md:20), plafonds d'indemnités journalières, doublements de prix d'un fournisseur d'IA (ver-R6-marche.md:33), facture électronique. Le coefficient SAS, les frais, l'apport, les dates, les disponibilités des associés et les probabilités sont bien codés [HY] ou [IN].
- **À noter** : le coût employeur d'un cadre (6 149 €) est codé [MM] parce que l'API de l'Urssaf a été interrogée (ver-R6-marche.md:25). Il s'agit d'un résultat de simulateur, plus proche d'une [ES] : à lire comme tel.

## 8. Limites restantes

1. **Tout le chiffre d'affaires est une hypothèse** : contrat certain à 0 € [FV négatif]. Le plan n'est pas pondéré : il suppose que chaque étape est vendue. Pondéré, le central tombe à 38 300 € HT sur 12 mois, **à condition que le cadrage soit vendu** (probabilité [IN]).
2. **Le central retient le pilote le plus cher** (B0 et un lot, 13 000 € HT). Les voies C2 ou C6 réduisent la trésorerie libre du mois 12 d'environ 5 000 à 6 300 €. La règle de rémunération, qui ne regarde que les mois 4 à 12, ne baisse pas : le coussin absorbe l'écart.
3. **Point bas fragile** : 3 100 € en décembre 2026 grâce à un apport de 10 000 € dont l'existence est [IN] (strategie-retenue.md:776). Il tombe à 100-700 € si l'assurance est payée d'avance.
4. **Coefficient SAS** de source secondaire unique ; éligibilité du mandataire à la réduction dégressive [IN] ; barème TNS « revenus 2025 » ; lois de finances 2027 à venir. À refaire par l'expert-comptable avec le simulateur officiel.
5. **IS** : seuil de 42 500 € non proratisé pour un premier exercice de 13 ou 14 mois. C'est sans effet sur les scénarios ; dans `structures.md`, l'IS du tableau des dividendes serait de 350 à 700 € plus bas. En prudent, le mois 12 appartient au deuxième exercice.
6. **Crédit de TVA** non compté dans la trésorerie disponible : c'est prudent, mais selon les tests, le point bas omet de 0 à 2 100 € de crédit remboursable.
7. **Retards de paiement** : le modèle suppose des paiements à l'échéance. Les retards ne figurent que dans les tests, un par un, sans cumul.
8. **Coûts de la fuite** au-delà du conseil [IN] ; reprise du conseil par la société [HY].
9. **Saisonnalité** (août, fêtes de fin d'année) non modélisée : les lots sont lissés.
10. **Impôt sur le revenu** des associés non calculé [IN] : tous les salaires sont avant IR, les dividendes après PFU.

## 9. À reporter dans les livrables

- Ne jamais citer « 13 700 € de dividende par associé » ni « le dividende laisse plus de net » : utiliser la ligne « à ressources égales » de `structures.md` § 4.
- Le prix moyen réalisé par JP vendue est de **≈ 870 €**, pas de 900 € : il reste sous le prix cible interne de 900 € par JP (strategie-retenue.md:397, 800 à 950 €).
- Le point bas et la trésorerie libre doivent être présentés avec leurs deux sensibilités (assurance payée d'avance, voie du pilote).
