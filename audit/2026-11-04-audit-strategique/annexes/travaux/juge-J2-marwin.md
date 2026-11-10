# Juge « J2-marwin » : les stratégies S1, S2 et S3 vues depuis Marwin Tech

Rédigé le 4 novembre 2026 au soir par le juge J2-marwin de l'audit Marwin Tech × GianLuca Carlone.

**Document interne.** Il contient des coûts, des marges, des planchers et des rémunérations d'associés. Il ne doit pas être transmis à GianLuca Carlone.

**Angle de jugement.** Rentabilité et trésorerie de Marwin ; soutenabilité de la charge pour deux personnes ; risques juridiques (requalification, responsabilité, RGPD, IA) ; indépendance et capacité de sortie ; crédibilité du prix.

## Méthode, sources et conventions

- **Lu en entier** : `strat-S1-progressif.md` (603 lignes), `strat-S2-pilotage.md` (611 lignes), `strat-S3-contradicteur.md` (576 lignes). **Lu par sections utiles** : `syn-capacite-ia.md` (§ 0 à 4 et 6), `syn-droit.md` (§ 0 à 4, 9), `syn-portefeuille.md` (§ 0 à 2), `syn-sources.md` (§ 0, d.3, d.4, h.1), `rj-R3-travail-contrats.md` (f), `rj-R6-marche.md` et `ver-R6-marche.md` (n° 1 à 8).
- **Scripts des stratèges relus et réexécutés** (`python3 -I`) : `scratchpad/s1-calc/plan.py`, `scratchpad/s2-calc/s2.py` et `annee1.py`, `scratchpad/s3-calc/scenarios.py` et `tresorerie.py`. Leurs sorties correspondent aux chiffres publiés, sauf indication contraire en section 2.
- **Recalculs propres au juge** : `audit/2026-11-04-audit-strategique/annexes/travaux/calculs/j2-calc/verif.py`. Toutes ses sorties sont des estimations [ES].
- **Pièce d'origine rouverte** : `crm/art_merge.py:17-19, 127-131` (dépôt `Momolscode/Carlone`, commit 7b46602, lecture seule).
- **Règle des contrôleurs** : quand un contrôleur corrige un lecteur ou un chercheur, c'est la correction qui fait foi (en particulier ver-R6 n° 3 et n° 6, ver-R4 n° 7).
- **Aucune action extérieure** : aucun contact, aucune dépense, aucune modification hors de ce fichier et du script de vérification.
- **Codes** : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu.
- **Abréviations** : S1, S2, S3 désignent les trois fichiers `strat-*` ; « S1:172 » renvoie à `strat-S1-progressif.md:172`. JP = journée-personne de 7 h.

**Trois faits nouveaux, pris comme base.** Les trois propositions les intègrent correctement.
1. Le 4 nov., Morgan a demandé de retirer Medhi et BOJ.ART de l'offre [DR]. Seul le diaporama client a été corrigé (11 diapositives) ; l'offre écrite, STRATES v1.1, le vernissage et le PDF de 13 diapositives de la PR n° 1 ne le sont pas [FV] (`note-point-4-novembre-et-activites.md:25` ; `syn-droit.md:28-34`).
2. Le dépôt public FinanceScope/CRM-Carlone est très probablement une violation de données personnelles [HY fort]. Si la connaissance date du 2 nov., le délai de 72 h pour notifier la CNIL expire le 5 nov., à une heure inconnue [ES] (`syn-droit.md:620-623`, corr. ver-R4 n° 7).
3. Il n'existe aucun contrat, aucune facture et aucune entité payeuse identifiée [FV négatif] (`syn-sources.md:39`).

---

## 0. Verdict du juge

1. **Classement, du point de vue de Marwin : S1 (31/40), puis S3 (27/40), puis S2 (26/40).**
   - S1 expose le moins la trésorerie, se réceptionne le mieux et reste dans la capacité réelle du binôme.
   - S3 apporte l'argument de prix le plus crédible face à GianLuca (la comparaison avec un recrutement) et l'offre qui tient Marwin hors de l'exécution.
   - S2 apporte la seule échelle crédible vers l'ambition de Morgan. Mais son scénario central dépasse la capacité qu'il retient lui-même, et son prix ne résiste pas à la comparaison avec un salarié.
2. **Aucune des trois n'est publiable telle quelle.** Chacune contient au moins une erreur de calcul ou de cohérence qui touche le prix ou la trésorerie (section 2).
3. **Six manques sont communs aux trois**, tous dans le champ « responsabilité et trésorerie » (section 5) :
   - une clause de limitation de responsabilité ;
   - la déclaration de la fuite à l'assureur et l'exposition personnelle des associés ;
   - la notification échelonnée à la CNIL et l'effet d'une information des personnes sur la prospection ;
   - le droit de rétractation des petites entreprises appliqué au contrat de Marwin lui-même ;
   - un taux d'occupation qui compte les autres projets de Morgan ;
   - la capacité réelle des associés à apporter 8 000 à 14 000 €.
4. **Recommandation** : prendre le squelette de S1 et y greffer :
   - l'offre « outillage et passation » et la comparaison de coûts de S3, avec des chiffres corrigés ;
   - les paliers et la clause de partage des gains de S2, comme seule voie vers l'ambition, sous conditions mesurées.

   Les chiffres de pilotage sont donnés en section 6.

---

## 1. Notes (1 = très faible, 5 = très bon)

| Critère | S1 « progressif » | S2 « pilotage » | S3 « contradicteur » |
| --- | --- | --- | --- |
| Valeur pour GianLuca | 4 | 3 | 4 |
| Existence d'une demande solvable | 4 | 3 | 4 |
| Rentabilité pour Marwin | 3 | 3 | 2 |
| Soutenabilité à deux | 4 | 2 | 4 |
| Maîtrise des risques juridiques | 4 | 3 | 4 |
| Réceptionnabilité | 5 | 4 | 3 |
| Honnêteté face aux inconnues | 4 | 3 | 4 |
| Fidélité à l'ambition de Morgan | 3 | 5 | 2 |
| **Total sur 40** | **31** | **26** | **27** |

### Justification des notes

| Critère | S1 | S2 | S3 |
| --- | --- | --- | --- |
| **Valeur pour GianLuca** | **4.** Pour 6 000 € HT, il garde un inventaire, une carte des rôles et trois priorités, même s'il s'arrête là (S1:173). Il décide sur pièces à chaque palier (S1:76-77). La valeur reste modeste tant qu'aucun lot n'a produit un résultat chez lui. | **3.** C'est l'offre la plus riche : vision du portefeuille, 4 à 6 projets coordonnés, engagements de service avec malus (S2:201-205, 221). Mais le palier B2 (8 000 € HT pour 9 JP) coûte environ 30 % de plus qu'un chef de projet cadre salarié à temps plein (6 149 € de coût employeur [MM], `ver-R6-marche.md:25`). Le suivi de « 4 projets actifs » suppose aussi des exécutants de son côté, dont l'existence est [IN]. | **4.** C'est la meilleure valeur par euro : une organisation qui tourne chez lui sans Marwin au quotidien, et une comparaison de coûts qu'il peut refaire lui-même (S3:95-103, 107-112). Elle cible le seul chantier qui peut créer du chiffre d'affaires chez lui, la vente d'œuvres (S3:88). Mais elle suppose qu'il accepte de recruter ou de désigner un assistant [IN]. Et elle prospecte des entreprises dont les données ont fuité (section 5, M4). |
| **Demande solvable** | **4.** La demande est testée par un cadrage payé moitié à la commande (S1:177), avec report si aucune entité n'est identifiée à la mi-décembre (S1:531). Un refus de payer le cadrage vaut réponse (S1:533). | **3.** Le cadrage sert aussi de test (S2:183). Mais toute la trajectoire repose sur un pilotage commandé dès février 2027 et sur un premier encaissement en décembre 2026 (S2:355, 372). Or sa propre feuille de route place l'immatriculation entre les semaines 3 et 6 (S2:488). Le budget mensuel que suppose B2 est [IN]. | **4.** S3 s'appuie sur les besoins les mieux documentés, même s'ils restent rapportés [DR] : vendre des œuvres, « ne pas gérer chaque détail » (S3:75). La date butoir du 31 janvier 2027 coupe court au travail gratuit (S3:508). Mais l'offre commerciale dépend d'une structure vendeuse, d'œuvres disponibles et d'un avis fiscal, tous [IN] (S3:191). |
| **Rentabilité pour Marwin** | **3.** Le scénario central SAS donne 10 à 40 % de marge sur le coût complet (S1:175, 195, 229). Il couvre de justesse le seuil de 2 500 € nets par ETP (S1:359). Deux points l'affaiblissent : des planchers sous le coût (V12) et un apport de départ sous-estimé (V13). | **3.** C'est le prix unitaire le plus élevé (≈ 890 à 940 € par JP, S2:178, 203-205). Mais le volume central n'est pas livrable dans la capacité retenue (V9). L'exploitation D1 est vendue sous son coût manuel (V11). Et le prix est exposé à la comparaison avec un salarié dès environ 7 JP par mois (V7). | **2.** C'est le prix unitaire le plus bas (≈ 780 à 810 € par JP, S3:176, 194, 212, 229). Sur la base de coût SAS qu'il recommande pourtant, cela laisse une marge d'environ 5 à 25 % [ES]. Le seuil de 2 500 € nets par ETP, annoncé comme « atteint », ne l'est pas sur l'année 1 en SAS (V5). Enfin, 15 % du chiffre d'affaires de l'année 1 vient d'un second client qui n'existe pas encore (S3:302). |
| **Soutenabilité à deux** | **4.** S1 plafonne à 12 JP facturables, avec un socle et deux projets, conformément à `syn-capacite-ia.md:253`. Il refuse la présence quotidienne et le format 20-40 JP (S1:536). Limite : 12 JP représentent déjà environ 101 % du temps que les associés consacrent à Marwin dans le scénario central (V9, et section 5, M6). | **2.** Le scénario central demande 12,9 à 15,3 JP pour 12 JP de capacité (V9). B2 suit 4 projets actifs, là où la synthèse capacité en juge 2 soutenables. Le scénario ambitieux demande environ 27 JP pour 22 à 24 de capacité (V10). | **4.** Le scénario central reste entre 8 et 10,5 JP (`s3-calc/scenarios.py`). L'offre « outillage et passation » réduit l'exécution portée par Marwin (S3:200-216). Point de tension : deux lots en parallèle aux mois 2 et 3, pendant la charge de démarrage non facturable de 9 à 17 JP (`syn-capacite-ia.md:220`). |
| **Risques juridiques** | **4.** S1 coche l'essentiel : SAS, rien encaissé avant l'immatriculation, mandat de dépense à 0 € pendant le cadrage et le pilote (S1:434), « client seulement » pendant 12 mois (S1:396), bureaux refusés avant le mois 6 (S1:397), aucune commission sur les ventes. Il manque la limitation de responsabilité, les transferts hors UE et la correction du simulateur fiscal du CRM (section 3, E7 ; section 5). | **3.** S2 cumule le plus d'indices de requalification relevés par `syn-droit.md:338-343` : abonnement mensuel à capacité nominative chez un client unique (S2:201-205), bureaux possibles dès le départ par convention (S2:418). Il qualifie mal le Diag Data IA (E1) et inverse l'ordre de dépôt de l'aide régionale (E2). Il ne corrige pas le simulateur fiscal. | **4.** S3 présente le moins d'indices de requalification : livrables au forfait, exécution confiée à un salarié du client, pas de bureaux pendant 3 mois (S3:421). C'est la seule à corriger le simulateur fiscal du CRM (S3:155). Mais sa vente principale prospecte les fiches exposées par la fuite (section 5, M4). L'aide au recrutement n'exclut pas l'IA (section 5, M9). |
| **Réceptionnabilité** | **5.** Chaque offre a ses critères de réception. Surtout, S1 sépare « livré pour la facturation du solde » et « approbation d'une suite » (S1:176, 445). Ce qui dépend de GianLuca est suivi à part (S1:100). | **4.** Les critères du cadrage sont signés (S2:182). Le solde est exigible au plus tard 30 jours après la remise (S2:316). Le pilotage a des engagements de service mensuels (S2:221). Mais la valeur d'un « suivi de 4 projets » se réceptionne mal. | **3.** Les critères sont bien écrits, mais le paiement du solde de 60 % (S3:328) dépend d'un comportement du client. La réception de C exige que la personne désignée utilise le registre 4 semaines (S3:215). Celle de B exige que l'appelant réimporte 90 % des résultats (S3:197). La réception tacite « pour le paiement » (S3:336) n'atténue cela qu'en partie. |
| **Honnêteté face aux inconnues** | **4.** Les dates sont réalistes (« au plus tôt décembre, plus probablement janvier », S1:348). S1 reconnaît qu'aucun scénario ne finance 7 500 € nets (S1:364). Mais sa cible de dépendance (≤ 80 %) n'est pas dans ses chiffres (V14). | **3.** S2 classe en [FV officiel] un chiffre que le contrôleur a requalifié en [ES] (E1). Il annonce une marge de 0 à 15 % qui va en fait de −14 à +14 % (V8), et un seuil de recrutement deux fois trop haut (V7). Ses objectifs de dépendance ne figurent pas dans ses chiffres (V14). | **4.** S3 est le seul à consacrer une section aux risques de sa propre stratégie (S3:547-553). Il refuse des notes chiffrées qui seraient une précision artificielle (S3:83). Mais il chiffre le coût d'une SAS avec un coefficient de SARL (V3 à V5). |
| **Fidélité à l'ambition** | **3.** Le pilotage global reste une cible à 12-24 mois, atteinte par paliers (S1:76). | **5.** S2 construit « la version la plus forte possible » de l'ambition, bornée et découpée (S2:7, 70-83). Il traduit « le travail de 100 personnes » en couverture mesurable (S2:126-130). | **2.** S3 assume de s'en éloigner : Marwin devient « outilleur et pilote léger » (S3:114). La porte n'est rouverte au mois 6 que sur preuves. |

---

## 2. Vérification des chiffres

Recalculs dans `scratchpad/j2-calc/verif.py`, sauf mention contraire. Tous les résultats sont des [ES].

| N° | Proposition et ligne | Affirmation | Recalcul du juge | Verdict |
| --- | --- | --- | --- | --- |
| V1 | S1:123-127 | Coût complet central (SAS, 2 500 € nets par ETP) : 590 à 740 € par JP | (1,15 ETP × 2 500 × 1,7 à 1,9 + 1 500 à 2 500) ÷ 12 ÷ 0,9 = **591 à 737 €** | **Exact.** C'est la meilleure base des trois, car elle est cohérente avec la SAS recommandée. |
| V2 | S2:151-155 | Coût complet central : 810 € (900 € avec réserve) pour 2 000 € nets ; 960 € (1 065 €) pour 2 500 € nets | (2 × net × 1,8 + 2 500) ÷ 12, puis ÷ 0,9 : **808 / 898 / 958 / 1 065 €** | **Exact**, mais sur une base différente : 2 000 € nets **par associé** pour 1,15 ETP, soit ≈ 3 480 € par ETP. Les coûts de S2 ne se comparent donc pas à ceux de S1 et de S3. |
| V3 | S3:270, 273 | Coût complet central : 500 à 580 € par JP | Exact avec l'hypothèse de S3 : 3 889 € par ETP, soit le modèle SARL de V5, impôt sur le revenu compris (coefficient ≈ 1,56). En **SAS** (1,7 à 1,9, `syn-droit.md:98`) : **532 à 664 €** hors réserve | **Erreur d'hypothèse.** S3 recommande la SAS (S3:396) mais calcule son coût comme une SARL. Le coût est sous-estimé d'environ 7 à 13 %. |
| V4 | S3:385 | « Environ 1 200 à 1 600 € nets par associé » (scénario central) | Disponible de 4 550 € par mois ÷ 1,7 à 1,9 ÷ 2 = **1 197 à 1 338 €** en SAS. Les 1 591 € ne s'obtiennent qu'avec le coefficient SARL de 1,43 | **Borne haute fausse** pour la structure recommandée. |
| V5 | S3:380 | « Le plancher de 2 500 € nets par ETP au prorata du temps est atteint » | Besoin en SAS : 1,15 × 2 500 × 1,7 à 1,9 = **4 888 à 5 462 €** chargés par mois. Disponible moyen de l'année 1 : 4 550 € → **non atteint**. En régime (mois 7 à 12) : 5 650 € → atteint | **Erreur.** Il faut écrire : « atteint en régime, pas sur l'année 1 en SAS ». |
| V6 | S3:348-351 | La réserve de 8 000 à 12 000 € couvre la création, deux mois de frais et l'exposition maximale sur les lots | 2 000 à 5 000 + 3 000 à 5 000 + 9 000 = **14 000 à 19 000 €** | **Incohérence.** Ou bien la réserve est sous-estimée, ou bien l'exposition (valorisée au prix de vente) n'est pas une sortie de trésorerie tant que les associés ne se paient pas. Il faut le dire. |
| V7 | S2:218 | « Si le besoin stable dépasse 15 JP par mois […], un recrutement est moins cher » | Un chef de projet cadre coûte 6 149 € par mois à son employeur [MM] (`ver-R6-marche.md:25`). À 900 € par JP, l'équivalence est atteinte à **6,8 JP par mois**. B1 (6 JP, 5 400 €) coûte déjà autant qu'un cadre à temps plein (5 380 à 6 150 €) ; B2 (8 000 €) coûte 30 % de plus | **Erreur matérielle, environ deux fois trop haut.** Elle touche directement la crédibilité du prix (section 6). Le recrutement a des coûts cachés (sélection, encadrement, risque), mais S2 ne les chiffre pas. |
| V8 | S2:179-181 | Cadrage à 7 500 € pour 8 JP : « marge sur coût complet de 0 à 15 % » | Avec les coûts de S2 lui-même (810 à 1 065 € par JP) : **−14 % à +14 %** | **Erreur de signe** sur la borne basse. Le cadrage est à perte si la cible est de 2 500 € nets avec réserve. |
| V9 | S2:360-363 ; `s2-calc/s2.py` | Central : B2 + 1 lot par mois + D1, pour ≈ 12 JP de capacité | Le script de S2 compte lui-même 12,25 JP, avec D1 à 0,75 JP (soit 3 minutes par fiche). Avec l'hypothèse de S2 (5 à 15 minutes par fiche, S2:248) : **12,9 à 15,3 JP**, soit **106 à 118 %** du temps des associés pour Marwin (20,1 JP bruts, dont 8,4 non facturables : `syn-capacite-ia.md:183-190`). B2 suit 4 projets actifs, alors que la synthèse capacité en juge 2 soutenables (`syn-capacite-ia.md:253`) | **Erreur de faisabilité.** Elle contredit la règle de S2 lui-même : « occupation ≤ 85 % » (S2:490, 502). |
| V10 | S2:360-363 | Ambitieux : B3 + lots de 7 000 € + D de 3 000 € + second client de 3 000 € | ≈ **27,3 JP** pour 18 à 20 JP plus 4 JP sous-traités (22 à 24 JP) | **Dépassement de capacité** non signalé. |
| V11 | S2:248 | D1 : 1 200 à 1 800 € par mois pour 100 fiches, puis 12 à 18 € par fiche acceptée | Coût interne d'une fiche : **18 à 27 €** à 10 à 15 minutes (chiffre de S2 lui-même), **9 à 11 €** à 5 minutes. S1 propose 40 à 70 € par fiche (S1:241) [HY] | **Prix sous le coût manuel.** D1 n'est rentable que si un gain encore non mesuré se réalise, et le prix est figé 12 mois (S2:253). L'écart entre S1 et S2 va de 3 à 6 fois : il faut le trancher par la mesure de référence du pilote P2. |
| V12 | S1:172, 202, 131 | Plancher du cadrage : 5 000 € ; plancher des lots : 700 € par JP ; « toute remise sur ce taux fait travailler à perte » | 5 000 € ÷ 8 JP = **625 €** par JP, sous le coût central de 591 à 737 €. 700 € reste sous la borne haute | **Incohérence interne.** Le plancher doit être au moins égal au coût haut, soit environ 740 € par JP : un cadrage de 8 JP ne peut pas descendre sous ≈ 6 000 €. |
| V13 | S1:156, 334 | Apport de départ : 3 000 à 7 000 € (puis 5 000 à 7 000 €) | Ce montant exclut le conseil sur la fuite [IN] et les mois de frais sans recette. S2 (S2:380, 1 000 à 3 000 € d'avocat compris) et S3 (S3:348) arrivent à **8 000 à 14 000 €** | **Sous-estimation probable.** Retenir 8 000 à 14 000 €. |
| V14 | S1:402 ; S2:369, 422 ; S3:376 | Cibles de dépendance à 12 mois : ≤ 80 % (S1), ≤ 85 % (S2), ≈ 75 % (S3) | Dans les modèles de S1 (`plan.py`) et de S2 (`annee1.py`), tout le chiffre d'affaires central vient de GianLuca, soit 100 %. Pour tenir la cible, il faut ≈ **2 100 € par mois** d'un autre client au mois 12. S3 le modélise (2 000 € à partir du mois 6 ; 76 %) | **S1 et S2 : cible non chiffrée.** S3 est cohérent, mais avec un second client hypothétique. |
| V15 | S1:330-342 ; S2:341-345 ; S3:342, 357-360 | Tests de retard, de rupture et d'exposition | Les scripts reproduisent les chiffres (central S1 à 90 jours : point bas −7 960 € ; S3 : exposition maximale de 9 000 € au mois 3). Aucun ne modélise l'impôt sur les sociétés, ni le décalage de TVA, ni le délai réel d'encaissement (S1 encaisse le mois même) | **Exact sur ses hypothèses**, mais optimiste sur les délais. |
| V16 | S2:364, 371, 366 | Chiffre d'affaires de l'année 1 ≈ 112 000 € ; seuils de 10 800 et 12 800 € ; net de 2 200 à 2 450 € en régime | Reproduits (112 300 € ; 10 778 € et 12 778 € ; 2 184 à 2 441 €) | **Exact sur ses hypothèses.** Mais il compte un premier encaissement en décembre 2026 (S2:355) et le volume de V9. |
| V17 | S3:69 | « 15 000 € HT par mois = 5,3 assistants ou 2,4 chefs de projet cadres » | 15 000 ÷ 2 808 à 2 249 = **5,3 à 6,7** assistants ; 15 000 ÷ 6 149 à 5 380 = **2,4 à 2,8** cadres | **Exact en borne basse.** Donner la fourchette. |
| V18 | S1:599 ; S1:143 | Assistant à 125 à 157 € par jour travaillé | 2 249 à 2 808 € ÷ 17,9 jours (ver-R6 n° 3) | **Exact.** S3 utilise une borne haute de 3 340 € (S3:101, d'après `rj-R6-marche.md:126`), que le contrôleur n'a pas recalculée : elle est plausible, mais [ES] non vérifiée. |

---

## 3. Erreurs de fait, de qualification ou de cohérence (hors calcul)

| N° | Proposition | Erreur | Pièce qui fait foi | Gravité pour Marwin |
| --- | --- | --- | --- | --- |
| E1 | S2:179, 291 | Le Diag Data IA « vaut » 1 250 € par jour [FV officiel] ; c'est le « prix public d'un jour d'expert IA » | Le contrôleur a corrigé : c'est un **plafond de devis divisé par 8** [ES], pas un prix constaté (`ver-R6-marche.md:28, 68`). Les entités de GianLuca ne sont probablement pas éligibles (10 à 2 000 salariés, au moins 1 M€ de chiffre d'affaires) [HY] | **Moyenne.** C'est un argument de prix fragile devant le client : il peut le démonter. S1 (S1:142) et S3 (S3:176) emploient correctement la correction. |
| E2 | S2:331-337 contre S2:185 | L'« ordre des opérations » fait signer le bon de commande (étape 3) **avant** de déposer le dossier d'aide régionale (étape 4). Or S2 écrit lui-même plus haut : « dépôt du dossier, puis signature, puis acompte » | Le dépôt doit précéder la signature [DR] (`syn-portefeuille.md:252`) | **Moyenne.** GianLuca pourrait perdre une aide de 50 % (jusqu'à 15 000 € sur deux ans [DR]), ce qui serait reproché à Marwin. S1 (S1:322) et S3 (S3:173) ont le bon ordre. |
| E3 | S2:201-205, 418 | Abonnement mensuel à « capacité réservée nominative » chez un client unique, avec des bureaux possibles dès le départ par convention | `syn-droit.md:338-343` : client unique, bureaux du client, prix au temps et « s'occuper de tout » sont des indices de requalification | **Moyenne.** S2 cumule le plus d'indices. S1 refuse les bureaux avant le mois 6 (S1:397), S3 pendant 3 mois (S3:421). |
| E4 | S3:197, 215, 328 | Le solde de 60 % des lots B et C dépend d'actes du client : l'appelant réimporte les résultats, l'assistant utilise le registre | Règle de S1 : « livré pour la facturation du solde » n'est pas « approbation » (S1:445) | **Élevée pour la trésorerie.** Si GianLuca ne recrute pas, 4 200 € du lot C ne deviennent jamais exigibles. Il faut séparer les critères de **livraison**, que Marwin contrôle et qui déclenchent le paiement, des indicateurs d'**adoption**, qui dépendent du client et décident de la suite. |
| E5 | S3:477 | « Gel de toute production gratuite à partir du 15 nov. » | `syn-portefeuille.md:304` (scénario S5) ; S1 : « immédiat » (S1:459) | **Faible à moyenne.** Cela fait 11 jours de travail gratuit en plus, sans raison donnée. |
| E6 | S3:524 | Pour la CNIL, pas de solution prévue si l'échéance du 5 nov. est dépassée | « Notifier en retard en expliquant pourquoi vaut mieux que ne pas notifier » (`syn-droit.md:623`) ; S1:458 et S2:485 prévoient un « retard motivé » | **Faible**, mais le délai expire demain. |
| E7 | S1 et S2 (absent) | Aucun des deux ne traite le simulateur fiscal du CRM | `crm/art_merge.py:19` fixe `TAUX_IS = 0.25` ; `crm/art_merge.py:129` calcule `economie_max = round(5 * plafond * TAUX_IS)`, sans tenir compte du bénéfice ni du taux PME de 15 % [FV]. Le CRM affiche ainsi 1 043 750 € pour une entreprise (`syn-sources.md:512`) | **Élevée en responsabilité.** C'est une affirmation fiscale erronée, déjà produite par les associés, dans un outil destiné à la prospection. Seul S3 la corrige (S3:155). |
| E8 | S2:201-205 | « 4 projets actifs » en B2 avec 2 à 3 JP de lots par mois, sans dire qui produit | Un projet n'avance qu'avec 2 à 3 JP de production par mois (`syn-capacite-ia.md:247`) | **Moyenne.** S2 suppose implicitement que des exécutants existent côté client [HY non dit]. |
| E9 | S2:490 | Au jour 90 : « CA encaissé ≈ 7 500 € » et « commande de B1 ou B2 signée ; premier mois payé » | Si le premier mois est payé, l'encaissement est de 12 900 à 15 500 € | **Faible** (incohérence de tableau). |

---

## 4. Meilleures idées à greffer

| Proposition | Idée | Pourquoi elle sert Marwin | Source |
| --- | --- | --- | --- |
| **S1** | Le taux de 750 € devient une **référence interne de chiffrage**, jamais remisée. On vend des forfaits, révisés au mois 6 sur le coût mesuré | Protège la marge sans afficher un taux journalier que GianLuca comparerait à un salaire | S1:274-281 |
| S1 | **Paiement par nature de prestation** : la capacité réservée se paie d'avance ; les livrables se paient par acompte et solde ; le variable se paie en fin de mois. Exposition maximale ≈ 5 000 à 6 000 € | Tranche la contradiction PAY-2 (`syn-sources.md:279`) au plus près du risque réel | S1:297-318 |
| S1 | **Le silence vaut livraison pour facturer le solde, jamais approbation d'une suite ni d'une dépense** | Encaisser sans engager la responsabilité de Marwin sur des décisions du client | S1:176, 445 |
| S1 | **Mandat de dépense à 0 €** pendant le cadrage et le pilote ; ensuite, 500 € par acte et 1 500 € cumulés, sur une liste fermée | Marwin n'avance jamais d'argent et ne détient pas les fonds du client | S1:113, 434-437 |
| S1 | **Un seul rôle à la fois** : « client » pendant 12 mois ; bureaux pas avant le mois 6 ; investissement pas avant 12 à 24 mois | Réduit la requalification et la dépendance croisée | S1:392-400 |
| S1 | **Règle de devis des lots** : provision de risque de 10 à 15 %, avenant signé avant tout dépassement | Le dépassement est la première cause de perte d'un forfait | S1:202 |
| S1 | **Sept conditions minimales pour commencer** et une question explicite sur l'apport des associés | Fait des préalables une liste vérifiable | S1:504-512, 589 |
| **S2** | **Paliers B1, B2, B3 avec limite d'encours** et conditions d'accès écrites (B3 seulement avec un engagement de 80 % de chacun et un sous-traitant identifié) | Seule traduction mesurable de l'ambition de Morgan. À reprendre avec des volumes corrigés (V9) | S2:201-205 |
| S2 | **La capacité du pilotage ne se convertit jamais en production.** Report limité à 20 %, pour du pilotage seulement | Évite que l'abonnement absorbe les lots | S2:215, 275 |
| S2 | **Changement de palier sans pénalité** si un associé est indisponible plus de 10 jours ouvrés | Rend la promesse soutenable face à la maladie ou à l'absence | S2:216 |
| S2 | **Partage des gains** : la première année, les gains restent à Marwin ; ensuite, un tiers va au client. **Prime de 20 à 30 % sur une économie réelle**, mesurée | Rémunère la valeur quand l'automatisation réduit le temps (DEMANDE § 11) | S2:252-256, 306 |
| S2 | **Lot C7 : aider GianLuca à recruter un coordinateur local** | Assume la comparaison avec un recrutement au lieu de la subir | S2:218, 238 |
| S2 | **Exercice de sortie à blanc** au mois 6 | Prouve la réversibilité promise dans le diaporama | S2:222 |
| S2 | **Tableau des seuils** (frais seuls ; 2 000 € nets ; 2 500 € nets) par scénario | Un repère simple pour piloter le prix | S2:371 |
| **S3** | **Comparaison de coûts présentée au client** : socle Marwin + assistant salarié + appels au rendez-vous, contre 15 000 € par mois. « Mieux vaut le lui présenter que le lui laisser découvrir » | C'est l'argument de prix le plus crédible. À corriger avec les fourchettes de V17 | S3:95-103 |
| S3 | **Offre C, « outillage et passation »** à une personne désignée ou recrutée par le client. Marwin ne reprend pas l'exécution au taux de 750 € | Sort Marwin de l'exécution administrative (qui ne vaut que 125 à 157 € par jour), réduit la saturation et la requalification | S3:200-216 |
| S3 | **La remise en ordre inclut la correction du simulateur fiscal du CRM** | Supprime une source de responsabilité déjà présente (E7) | S3:155 |
| S3 | **Second client modélisé dans le chiffre d'affaires**, avec une sanction : aucun nouveau lot pour GianLuca au-delà de 90 % au mois 6 ou de 80 % au mois 12 | La seule cible de dépendance qui figure dans les chiffres | S3:376, 424 |
| S3 | **Date butoir du 31 janvier 2027** pour reporter ; **concession sur les conditions de paiement** seulement après trois échéances payées à l'heure | Limite le travail gratuit et garde une marge de négociation | S3:344-346, 508 |
| S3 | **Les tiers facturent directement l'entité de GianLuca** ; Marwin ne revend ni ne refacture leurs prestations | Pas de débours, pas de risque de mandat de paiement | S3:296 |
| S3 | **Section « risques de la présente stratégie »** | Discipline d'honnêteté à garder dans le document final | S3:547-553 |

---

## 5. Ce qu'aucune proposition ne traite (ou traite à peine)

| N° | Manque | Pourquoi il compte pour Marwin | Pièce, code et piste |
| --- | --- | --- | --- |
| M1 | **Clause de limitation de responsabilité** : plafond lié aux honoraires des 12 derniers mois, exclusion des dommages indirects (ventes manquées, économies d'impôt espérées par les prospects), obligation de moyens pour le pilotage et les sorties d'IA | Les livrables touchent des arguments fiscaux et des décisions d'investissement. Sans plafond, la responsabilité de deux associés débutants n'est pas bornée. S2 évoque « au même plafond que le contrat » (S2:581) sans le définir. | `rj-R3-travail-contrats.md:264-279` [FV pour les textes : C. civ. 1231-3, 1170, 1171] ; à rédiger avec l'avocat [PR] |
| M2 | **La fuite et l'assurance** : une RC professionnelle souscrite après la découverte ne couvrira probablement pas un incident connu avant la souscription. La fuite doit être déclarée sincèrement à l'assureur. Morgan et Mathys sont peut-être **personnellement** responsables du traitement de fait | L'exposition (conseil, éventuelle procédure CNIL, information des personnes) n'est ni chiffrée ni budgétée. S2 seul prévoit 1 000 à 3 000 € d'avocat (S2:163). | Rôles : `syn-droit.md:597, 624` [HY] ; règle d'assurance sur le risque connu et la déclaration sincère [HY, Code des assurances non rouvert] |
| M3 | **Notification échelonnée** : l'article 33 du RGPD permet, si toutes les informations ne sont pas disponibles, de notifier dans le délai puis de compléter | C'est l'outil pratique pour tenir l'échéance du 5 nov. sans dossier complet | RGPD, art. 33 [HY : paragraphe sur la notification échelonnée non rouvert dans cet audit ; à confirmer par l'avocat ou le DPD] |
| M4 | **Information des personnes (art. 34) et prospection des mêmes fiches.** Si le risque est élevé pour les artistes et les lignes personnelles, il faudra les informer. Prospecter ensuite ces mêmes entreprises (S3, lot B ; S1, lot C2 ; S2, lot C1) est délicat, commercialement et juridiquement | La vente principale de S3 et un lot de S1 et de S2 reposent sur ce fichier | `syn-droit.md:622, 625` [FV pour la règle ; HY pour le niveau de risque]. Piste [PR] : démarrer le pilote sur des comptes **non exposés** ou après la décision sur l'art. 34 |
| M5 | **Rétractation des petites entreprises appliquée au contrat de Marwin.** Signé hors établissement avec une entité de 5 salariés au plus, dont l'activité principale (le commerce d'art) ne couvre pas un service de pilotage, le contrat ouvrirait 14 jours de rétractation, sans aucun paiement avant 7 jours | Cela contredit « 50 % à la commande, démarrage à l'encaissement » dans les trois propositions | Règle : `syn-droit.md:530` [FV via R5, examinée pour les ventes d'œuvres seulement]. Application au contrat de Marwin : [HY], à faire trancher par l'avocat. Pistes : signature à distance (« vente à distance non visée », même ligne) ou délai de 7 jours prévu dans le calendrier |
| M6 | **Taux d'occupation mal défini pour des associés à temps partiel.** Les trois propositions reprennent le seuil de 85 % (`syn-capacite-ia.md:299`) sans dire sur quel temps il se calcule | Sur le temps consacré à Marwin, le scénario central atteint 94 % à 10,5 JP (S1, S3) et 101 % à 12 JP. Sur 2 × 17,5 JP, le seuil ne se déclenche jamais, alors que Morgan mène une dizaine d'autres projets (`note-point-4-novembre-et-activites.md:12-17`) | [PR] : mesurer l'occupation **par personne, sur tout son temps de travail**, y compris OLSEN, Shelby et BOJ.ART. Seuil d'alerte à 85 % |
| M7 | **Liquidité personnelle des associés.** L'apport nécessaire est de 8 000 à 14 000 € (V13). Or la note du 4 nov. signale 144 € de domiciliation impayés depuis le 12 oct. et des prélèvements en échec depuis fin octobre | Si l'apport n'existe pas, aucun des trois calendriers ne tient | `note-point-4-novembre-et-activites.md:6, 8` [DR]. S1 pose la question (S1:589) ; personne ne prévoit de repli [IN]. Piste [HY, aucune aide acquise] : réduire les sorties d'argent de la phase 0 à l'avocat de la fuite et aux statuts, et décaler le reste après l'acompte |
| M8 | **Le salariat de Morgan comme alternative chiffrée.** Un poste de cadre chez GianLuca (≈ 3 400 € nets pour 6 149 € de coût employeur [MM], `ver-R6-marche.md:25`) rapporterait plus que tous les scénarios centraux de l'année 1 (1 200 à 2 450 € nets) | C'est le principal risque pour l'indépendance de Marwin pendant la négociation. Les trois propositions renvoient le sujet à 6 mois sans chiffres | Souhait de Morgan [DR] (`syn-droit.md:257`). [PR] : préparer la réponse chiffrée avant le rendez-vous |
| M9 | **IA : transferts, transparence, recrutement.** S1 ne mentionne pas les clauses contractuelles types ni l'analyse d'impact des transferts (Anthropic et OpenAI hors DPF). Aucune proposition ne mentionne l'article 50 de l'AI Act si Marwin livre un assistant à son nom (S2, D2 ; S1, E). S2 (C7) et S3 (offre C) ne retirent pas l'IA de l'aide au recrutement | Une sanction ou un incident sur ces points retombe sur Marwin en tant que fournisseur ou sous-traitant | `syn-droit.md:660-675` [FV / MM] ; les outils RH sont à exclure, car à haut risque (`syn-droit.md:665`) |
| M10 | **Conflit entre prospection propre et données du client.** Le « kit CRM » vendu à d'autres entreprises de la Nièvre (S3:93) et la prospection d'OLSEN visent le même territoire que la campagne de GianLuca | Risque de conflit d'intérêts et de réutilisation de ses données de prospects | [PR] : kit construit sur des composants génériques seulement ; aucune donnée Carlone réutilisée ; règle écrite au pacte et au contrat |
| M11 | **Impôt sur les sociétés, décalage de TVA et délais réels d'encaissement** absents des plans de trésorerie de S1 et de S2 | Les réserves annoncées à 12 mois (S1 : 21 000 à 31 000 €) sont avant IS et sans décalage | [ES] ; à faire refaire par l'expert-comptable |

---

## 6. Recommandation de synthèse (angle Marwin)

### 6.1 Architecture retenue

- **Squelette de S1** :
  - remise en ordre non facturée ;
  - cadrage au forfait, payé moitié à la commande ;
  - pilote de huit semaines (un socle et un lot) ;
  - socle récurrent borné au mois 4, sur décision écrite ;
  - lots devisés, et une exploitation au résultat seulement après preuve.
- **Greffe de S3** : l'offre « outillage et passation » devient le **lot par défaut** dès que GianLuca veut « ne pas gérer chaque détail ». Marwin outille, forme et pilote, et une personne de son côté exécute. Les critères de réception sont réécrits : la livraison déclenche le paiement, l'adoption décide de la suite (E4).
- **Greffe de S2** : les paliers B1, B2 et B3 deviennent la **seule voie vers l'ambition de Morgan**. B2 n'est ouvert qu'à trois conditions :
  - des gains mesurés sur les pilotes P1 et P3 ;
  - une disponibilité nominative écrite ;
  - une occupation de chaque associé, sur tout son temps de travail, inférieure à 85 % pendant trois mois.

  On garde aussi de S2 la non-conversion du pilotage en production, le partage des gains et l'exercice de sortie à blanc.

### 6.2 Chiffres de pilotage internes [ES]

| Élément | Valeur recommandée | Fondement |
| --- | --- | --- |
| Coût complet d'une JP facturable (SAS, scénario central, réserve de 10 % comprise) | **≈ 590 à 740 €** | V1 |
| Plancher absolu de vente | **750 € par JP estimée**, au-dessus de la borne haute du coût. Aucun plancher de S1 sous ce seuil | V12 |
| Prix cible des forfaits | **800 à 950 € par JP estimée**, plus 10 à 15 % d'aléas sur les lots | S1:202 ; S2:226 |
| Cadrage | **6 500 à 7 500 € HT** pour ≈ 8 JP ; plancher de 6 000 € (ou périmètre réduit) | S2:178 ; S3:176 ; V8, V12 |
| Socle « un socle et deux projets » | **≈ 4 500 € HT par mois** pour 4 à 5 JP (fourchette des trois : 4 000 à 5 400 €) | S1:226 ; S2:203 ; S3:229 |
| Exploitation au résultat | Prix par fiche fixé **après** la mesure de référence du pilote P2 ; jamais sous le coût manuel mesuré | V11 |
| Capacité engagée pendant l'année 1 | **≤ 10 JP facturables par mois** (≈ 94 % du temps central consacré à Marwin), même si 12 JP est le plafond théorique | V9 ; M6 |
| Chiffre d'affaires de l'année 1 venant de GianLuca (central) | **≈ 80 000 à 95 000 € HT** | S1:357 ; S3:302, 375 |
| Rémunération | Rien avant le socle récurrent ; ensuite ≈ 1 200 à 1 600 € nets par associé en SAS. Aucun scénario ne paie 7 500 € | S1:358 ; V4 |
| Apport de départ | **8 000 à 14 000 €** (capital entièrement libéré et comptes courants), à confirmer face à M7 | V13 ; M7 |
| Exposition maximale de trésorerie | ≤ 6 000 € HT de travail non payé à tout moment | S1:318 |
| Dépendance | Soit ≥ 2 100 € par mois d'un autre client au mois 12, soit l'aveu écrit que Marwin restera à ≈ 100 % dépendante, et que les associés gardent leurs autres revenus | V14 |

**Crédibilité du prix, à dire au client.** Pour un besoin **stable** d'environ 7 JP par mois ou plus, un coordinateur salarié lui coûte moins cher que Marwin à 900 € par JP (V7). L'offre durable de Marwin doit donc vendre :
- le pilotage et la préparation des décisions ;
- l'outillage, la responsabilité (sauvegardes, réversibilité, contrôle à quatre yeux) et la passation ;
- et non un volume de journées.

Il faut présenter cette comparaison, corrigée, comme le propose S3.

### 6.3 À corriger avant tout document destiné à GianLuca

1. **Ce soir ou demain matin**, décider de la notification à la CNIL avec un avocat ou un DPD. Notification échelonnée si le dossier est incomplet (M3), ou retard motivé. Ouvrir la fiche de violation. Vérifier que le dépôt est privé. Informer GianLuca par écrit. Déclarer sincèrement l'incident à l'assureur au moment de la souscription (M2).
2. **Arrêter immédiatement** toute production non commandée, et non à partir du 15 nov. (E5).
3. **Corriger le simulateur fiscal du CRM** (E7), et ne plus montrer de chiffres d'« économie d'impôt » sans validation écrite d'un professionnel.
4. **Insérer au contrat-cadre** :
   - une limitation de responsabilité (M1) ;
   - la séparation entre livraison et adoption (E4) ;
   - le mandat de dépense à 0 € ;
   - le traitement de la rétractation des petites entreprises (M5) ;
   - l'exclusion de l'IA dans tout recrutement (M9) ;
   - les clauses contractuelles types et l'analyse d'impact des transferts pour les outils d'IA (M9).
5. **Retirer de tout argumentaire** :
   - le « 1 250 € par jour » présenté comme un prix (E1) ;
   - le « 15 JP » de S2 (V7) ;
   - toute marge ou tout seuil calculé avec un coefficient de SARL sous une SAS (V3 à V5).
6. **Remettre l'aide régionale dans le bon ordre** : dépôt du dossier, puis signature, puis acompte (E2).

### 6.4 Conditions pour réduire, reporter ou refuser (synthèse de S1 et de S3)

- **Reporter, sans travail gratuit**, dans les cas suivants :
  - pas d'entité identifiée à la mi-décembre (S1:531), et au plus tard pas de cadrage payé au 31 janvier 2027 (S3:508) ;
  - fuite non traitée ;
  - apport des associés impossible (M7) ;
  - désaccord de Mathys.
- **Réduire** à un cadrage et un lot si GianLuca ne confie qu'un projet, ou si les associés n'engagent pas ensemble au moins 6 à 8 JP facturables par mois (S1:530 ; S3:510).
- **Refuser** dans les cas suivants :
  - 20 à 40 JP avec présence quotidienne ;
  - paiement en bureaux, en emploi ou en capital ;
  - commission sur les ventes d'œuvres ;
  - obligations d'exploitant ;
  - salariat simultané avec le contrat de Marwin (S1:534-537 ; S3:513-518) ;
  - et, en plus, toute exigence de démarrer avant le délai de 7 jours si la règle M5 s'applique.

### 6.5 Ce qui reste inconnu et change le verdict

- **Disponibilité réelle de Morgan et de Mathys** [IN]. Sans engagement écrit, seul le scénario prudent est défendable (4 000 à 6 000 € de chiffre d'affaires par mois).
- **Entité, budget et mode de paiement de GianLuca** [IN]. Sans eux, les trois propositions restent au stade du cadrage.
- **Ce que GianLuca a déjà vu** : taux de 750 €, 13 ou 11 diapositives [IN]. Cela décide du prix du cadrage (S2:295).
- **Effectif de ses entités** [IN]. Il décide de l'application de M5 et de l'éligibilité au Diag Data IA.
- **Date réelle de connaissance de la fuite** [IN]. Si elle est antérieure au 2 nov., le délai de la CNIL est déjà dépassé, et la notification doit être motivée.
