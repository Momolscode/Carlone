# Juge « J1-client » : évaluation des trois stratégies S1, S2 et S3 du point de vue de GianLuca Carlone

Rédigé le 4 novembre 2026 au soir par le juge J1 de l'audit Marwin Tech × GianLuca Carlone. **Document interne** : il contient des coûts, des marges et des rémunérations. Il ne doit pas être transmis à GianLuca Carlone.

**Angle du juge.** La valeur réelle et vérifiable pour GianLuca Carlone ; l'existence d'une demande solvable ; l'adoption par ses équipes ; la possibilité de réceptionner les livrables ; le respect de ses décisions et de ses entités. Les autres angles (rentabilité, soutenabilité, droit) sont notés, mais lus avec ce filtre.

**Méthode.**
- Pièces évaluées : `strat-S1-progressif.md` (S1), `strat-S2-pilotage.md` (S2), `strat-S3-contradicteur.md` (S3), lues en entier ; synthèses `syn-sources.md`, `syn-portefeuille.md`, `syn-capacite-ia.md`, `syn-droit.md` (sections utiles) ; contrôle `ver-R6-marche.md` et mémo `rj-R6-marche.md` pour les repères de prix. Quand un contrôleur corrige un lecteur, la correction fait foi.
- Pièces d'origine rouvertes ce soir, en lecture seule : dépôt `Momolscode/Carlone`, `origin/main` = 7b46602 (vérifié par `git log`) ; diaporama client en ligne (copie locale `scratchpad/artifact-files/04f14ef8-a5fd-429b-9b3e-6d69b1d2ce5f/project/`, abrégée « deck/ »).
- Calculs refaits en Python (`python3 -I`) : `audit/2026-11-04-audit-strategique/annexes/travaux/calculs/j1-calc/verif.py`. Tous ses résultats sont des estimations [ES].
- Aucune action extérieure : aucun contact, aucune dépense, aucune modification hors de ce fichier et du script de calcul.

**Codes.** [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] information inconnue.

**Abréviations.** OFF = `interne/offre-marwin-tech-remuneration-et-collaboration.md` ; ACC = `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md` ; COP = `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md` ; syn-S, syn-P, syn-C, syn-D = les quatre synthèses ; JP = journée-personne de 7 h.

---

## 0. Verdict du juge en six points

1. **Les trois stratégies convergent sur l'essentiel** et ont raison de le faire : traiter la fuite de données avant toute autre chose, ne plus présenter l'offre de 20 ou 40 JP par mois, vendre d'abord un **cadrage court et payé** à une entité identifiée, ne rien encaisser avant l'immatriculation, geler STRATES, Éclosion et le laboratoire, refuser toute commission sur les ventes d'œuvres [PR, convergent].
2. **Classement J1** (notes au § 2) : **S1 = 31/40**, **S2 = 28/40**, **S3 = 26/40**. S1 est la meilleure base : la plus prudente, la plus honnête sur les inconnues, sans erreur de calcul notable. S2 est la plus fidèle à l'ambition et la meilleure sur la réception, mais son scénario central est saturé et contient trois erreurs de chiffrage. S3 pose les meilleures questions sur le besoin réel de GianLuca, mais elle surestime sa rentabilité et rend certaines réceptions dépendantes d'actes du client.
3. **Erreurs à corriger avant tout usage** (§ 4) : S2 présente le Diag Data IA à 1 250 € par jour comme un « prix public » alors que c'est un plafond de devis ; S2 situe à 15 JP par mois le seuil où un recrutement devient moins cher pour GianLuca, alors qu'il est d'environ 6 à 8 JP ; S3 calcule ses coûts avec un coefficient de SARL tout en recommandant une SAS, ce qui gonfle sa marge sur 750 € (23 à 34 % annoncés, 2 à 21 % recalculés).
4. **Aucune des trois ne vérifie la solvabilité au-delà du SIREN et de l'acompte**, aucune ne regarde le régime du contrat si GianLuca signe à titre personnel ou par une petite entité hors établissement, aucune ne tient compte de l'échéance du 31 décembre 2026 annoncée pour l'aide régionale au conseil, et aucune ne prépare le message qui annoncera à GianLuca le recadrage de l'offre (§ 7).
5. **Recommandation de synthèse** (§ 8) : partir du parcours de S1, y greffer les mécanismes de réception et de protection de S2 et les options centrées sur le client de S3, puis laisser **GianLuca choisir après le cadrage** entre trois suites : un pilote de vente d'œuvres, un pilote de pilotage, ou un outillage remis à une personne qu'il désigne.
6. **Vérité économique à dire aux associés** : à 12 JP facturés par mois, entre 750 et 900 € par JP, chacun touche environ **1 500 à 2 400 € nets par mois** en SAS, réserve comprise [ES] (§ 5). L'objectif de 7 500 € nets chacun (OFF:118) n'est atteignable par aucune des trois stratégies la première année.

---

## 1. Ce que le juge a vérifié lui-même ce soir

| Point | Constat | Code | Source |
| --- | --- | --- | --- |
| Commit de référence | `origin/main` = 7b46602, 4 nov. 2026 à 17:37 +0100 | [FV] | `git log -1 origin/main` |
| Diaporama client en vigueur | 11 vues ; `strates` et `strates-phases` hors de l'ordre, mais leurs fichiers restent dans `slides/` et sont les seuls à citer Medhi | [FV] | deck/deck.json:7 ; deck/slides/strates-phases.html:10, 28 ; deck/slides/strates.html:12 |
| Ce que le diaporama « corrigé » promet encore | « Six mois pour suivre vos établissements, vendre vos œuvres avec le CRM… » ; « Votre CRM de prospection est prêt à servir » ; consigne « Montrer le CRM en direct » ; formules à 15 000 et 30 000 € et « Taux unique : 750 € HT » ; option laboratoire à 30 000 € HT, « matériel acheté et possédé par votre entité » ; « Le travail démarre à réception » de l'acompte | [FV] | deck/slides/proposition.html:3 ; livre.html:4, 26 ; formules.html:20, 30 ; laboratoire.html:9, 14 ; paiement.html:10, 32 |
| Formules et taux de l'offre écrite | 15 000 € HT pour 20 JP, 30 000 € HT pour 40 JP ; « On ajuste le périmètre et le nombre de jours, pas le taux » ; option création avec Medhi toujours présente | [FV] | OFF:13-22 |
| Origine des « vingt jours » | Attribués à GianLuca dans COP:65 et à Morgan dans ACC:7 (« Morgan envisage une implication de vingt jours par mois »), tous deux à partir d'un brief de Morgan | [FV] pour les textes ; [DR] pour le fond | COP:65 ; ACC:7 |
| Règle sur les gains d'automatisation | « Les économies issues de l'automatisation permettent de réaffecter la capacité ou de revoir le forfait » | [FV] | ACC:66 |
| Paiement | Mois 2 à 6 « sous sept jours après facture de fin de mois » (29 oct.) contre « payés d'avance, en début de mois » (2 nov.) | [FV] | ACC:57 ; OFF:19 |
| Silence du client | « une absence de réponse ne vaut pas approbation » contre « le livrable est réputé accepté » | [FV] | ACC:103 ; OFF:206 |
| Base du plancher de 10 278 € | Modèle SARL à l'IS, « nets après cotisations et impôt sur le revenu » : 60 000 € nets + 33 332 € de cotisations et d'impôt + 30 000 € de frais | [FV] | OFF:114 |
| Diag Data IA | Plafond de devis de 10 000 € HT pour 8 jours, 40 % pris en charge ; « 1 250 € par jour » = maximum calculé, pas un prix ; réservé aux entités de 10 à 2 000 salariés et d'au moins 1 M€ de chiffre d'affaires | [FV] (contrôleur) | ver-R6-marche.md:28, 68 |
| Coût d'un salarié | Assistant non cadre : 2 249 à 2 808 € par mois (2 000 à 2 300 € brut) ; chef de projet cadre : 6 149 € (4 333 € brut) | [MM] (contrôleur, API URSSAF) | ver-R6-marche.md:25 ; rj-R6-marche.md:126-128 |

**Faits nouveaux, bien intégrés par les trois stratégies** : retrait de Medhi et de BOJ.ART demandé le 4 nov. et appliqué au seul diaporama en ligne [DR pour la décision, FV pour l'application partielle] (note-point-4-novembre-et-activites.md:25) ; violation de données très probable sur le dépôt public FinanceScope/CRM-Carlone, avec une échéance CNIL au 5 nov. si la connaissance date du 2 nov. [HY fort ; ES pour le délai] (syn-droit.md:614-636) ; aucun contrat, aucune facture, aucune entité payeuse [FV négatif] (syn-sources.md:39). Aucune des trois ne se trompe sur ces trois faits.

---

## 2. Tableau des notes

### 2.1 Notes (1 = très faible, 5 = très bon)

| Critère | S1 progressif | S2 pilotage | S3 contradicteur |
| --- | :---: | :---: | :---: |
| Valeur pour GianLuca | 4 | 3 | 4 |
| Existence d'une demande solvable | 4 | 3 | 3 |
| Rentabilité pour Marwin | 3 | 3 | 2 |
| Soutenabilité à deux | 4 | 2 | 4 |
| Maîtrise des risques juridiques | 4 | 4 | 4 |
| Réceptionnabilité | 4 | 5 | 3 |
| Honnêteté face aux inconnues | 5 | 3 | 4 |
| Fidélité à l'ambition de Morgan | 3 | 5 | 2 |
| **Total sur 40** | **31** | **28** | **26** |

Ces notes sont un jugement [HY], appuyé sur les justifications ci-dessous et sur les vérifications du § 4. Elles ne mesurent pas la qualité rédactionnelle, qui est bonne pour les trois.

### 2.2 Justification des notes

| Critère | S1 | S2 | S3 |
| --- | --- | --- | --- |
| **Valeur pour GianLuca** | **4.** Le cadrage lui laisse un inventaire validé, trois priorités, une carte des rôles par entité et un projet de mandat, même s'il s'arrête là (strat-S1:166, 173). Le pilote de huit semaines mesure l'adoption avant tout engagement (strat-S1:186-198). Coût annuel le plus bas pour un pilotage réel (≈ 94 500 € HT en central) [ES]. Faiblesse : le seul besoin rapporté qui crée du chiffre d'affaires chez lui, la vente d'œuvres (COP:13) [DR], passe après les lots « catalogue » et « lieux » (strat-S1:212). | **3.** Le cadrage est le plus riche (sept livrables, registre ouvert sur un compte de son entité, mesure de référence ; strat-S2:173) et le pilotage offre un malus de 5 % et une sortie à blanc (strat-S2:221-222). Mais la valeur centrale vendue, un bureau de pilotage, suppose un portefeuille dont l'existence n'est pas établie (syn-P:88-100), pour un coût annuel supérieur d'environ 18 % à S1 (≈ 112 000 € HT) [ES]. La « comparaison honnête » avec un salarié est mal chiffrée (§ 4, E2). | **4.** C'est la seule stratégie qui part de ce que GianLuca est censé vouloir : vendre des œuvres et ne pas gérer chaque détail (strat-S3:65, 75). Elle mesure des résultats chez lui [MM à produire] et lui laisse une organisation qu'il peut faire tourner sans Marwin (strat-S3:107-112). Réserve : son coût total pour GianLuca (≈ 80 000 € HT de Marwin plus 27 000 à 40 000 € d'assistant, plus les appels) n'est comparé qu'à l'offre d'archives, pas aux autres options ; il est du même ordre que S1 ou supérieur [ES]. |
| **Demande solvable** | **4.** Plus petit premier engagement (6 000 € HT), « un refus de payer un cadrage est déjà une réponse » (strat-S1:57), report si aucun rendez-vous avant mi-décembre ou aucune entité payeuse (strat-S1:531). Ne vérifie pas la solvabilité au-delà du SIREN et de l'acompte (§ 7). | **3.** Même porte d'entrée, mais au prix le plus haut (7 500 € HT) sans référence démontrable à montrer, avec un repli tactique à 6 000 € « seulement si GianLuca a déjà vu le taux » (strat-S2:178). Le scénario central suppose un cadrage payé dès décembre et un abonnement commandé en février (strat-S2:355, 372), alors qu'aucun rendez-vous n'est fixé (note:5) [DR]. | **3.** Date butoir nette (six semaines après le rendez-vous, au plus tard le 31 janvier 2027 ; strat-S3:56). Mais le scénario central exige plus d'actes de GianLuca que les autres : structure vendeuse, 5 à 10 œuvres disponibles, avis fiscal écrit, appelant désigné, recrutement d'un assistant (strat-S3:191, 379). S3 classe elle-même l'échec du pilote faute d'œuvres comme « élevé » (strat-S3:549). |
| **Rentabilité pour Marwin** | **3.** Calculs justes et prudents : le taux de 750 € couvre de justesse le coût complet central (590 à 740 € par JP ; strat-S1:123-131, recalculé). Revenu modeste assumé : ≈ 1 200 à 1 600 € nets chacun en central (strat-S1:358). | **3.** Les prix les plus élevés (880 à 950 € par JP estimée) et l'exploitation au volume (offre D) donnent le meilleur potentiel. Mais le revenu moyen de la première année reste ≈ 1 500 € nets chacun (strat-S2:367), le régime de croisière suppose une capacité saturée (§ 4, E4) et la marge du cadrage est surestimée (E3). | **2.** Prix les plus bas (≈ 780 à 810 € par JP ; régie à 750 €). La marge annoncée sur 750 € (23 à 34 %) repose sur un coefficient de SARL net d'impôt, alors que S3 recommande une SAS : recalculée, elle tombe à 2 à 21 % (E6). « Plancher atteint » en central n'est vrai qu'avec ce coefficient. |
| **Soutenabilité à deux** | **4.** Plafond écrit de 12 JP facturables, 10 à 11 utilisés en central, occupation ≤ 85 %, plancher de prospection, un seul associé par réunion, validation technique déléguée à Mathys (strat-S1:59, 353, 386). La disponibilité de Mathys reste [IN]. | **2.** Bons mécanismes (capacité nominative, limite d'encours, report de 20 % pour le seul pilotage, réduction de palier sans pénalité ; strat-S2:215-216). Mais le central consomme 12,7 à 13,2 JP pour 12 disponibles [ES] et ne laisse aucune place au second client que S2 exige pour ramener la part de GianLuca sous 85 % (E4). L'ambitieux suppose deux associés à 90 % et un sous-traitant. | **4.** Charge centrale de 8 à 10,5 JP pour 12 ; seuil minimal de 8 JP par mois à deux pour démarrer ; transfert de l'exécution quotidienne vers une personne de GianLuca (strat-S3:371, 489). L'ambitieux est « à la limite » et S3 le dit. |
| **Risques juridiques** | **4.** Mandat de dépense à 0 € pendant le cadrage et le pilote, un seul rôle (client) affiché, refus des bureaux pendant le pilote, aucune exécution réglementée, correction du prénom dans les documents client (strat-S1:154, 434). Deux incohérences internes mineures (E8, E9). | **4.** Le plus complet : vigilance Urssaf (K-bis et attestation remis au client), débours selon le BOFiP, consignes aux opératrices de Quali Contact passant par leur employeur, « enchères » réservées aux opérateurs habilités (strat-S2:267, 280, 462, 502). Omet la correction du prénom dans les pièces destinées au client (E11). | **4.** Le plus exigeant sur les données du pilote commercial (entreprises seulement, ni entrepreneurs individuels ni lignes personnelles avant l'avis de l'avocat ; strat-S3:189) et corrige le simulateur fiscal du CRM dans la remise en ordre (strat-S3:155). Omet la correction du prénom (E11) ; incohérence entre « seul rôle client pendant 6 mois » et « bureaux après 3 mois » (E8). |
| **Réceptionnabilité** | **4.** Critères écrits pour chaque offre ; le silence vaut livraison pour le seul paiement du solde, jamais approbation d'une suite (strat-S1:176, 445). Le pilote CRM dépend, comme chez les autres, d'appels passés par un tiers (§ 7, point 9). | **5.** Réception **expresse** du cadrage (livrables 1, 3 et 4 signés), solde exigible à 30 jours faute de réserve motivée, cession des droits seulement à la réception expresse et au paiement complet, engagements de service mensuels avec avoir en cas de manquement (strat-S2:182, 221, 316). | **3.** Critères précis, mais la réception de l'offre C exige que la personne désignée par GianLuca utilise le registre quatre semaines de suite, et celle de l'offre B que 90 % des appels soient réimportés (strat-S3:197, 215), alors que 60 % du prix est payé à la réception (strat-S3:328). Si GianLuca ne recrute pas ou n'appelle pas, Marwin ne peut ni réceptionner ni se faire payer (E7). |
| **Honnêteté face aux inconnues** | **5.** Codes rigoureux, limites écrites (strat-S1:603), « ce qu'on ignore : comment GianLuca paie » (strat-S1:326), variante basse à 6 000 € si GianLuca s'arrête au cadrage (strat-S1:357), calculs exacts au recalcul. | **3.** Bonne posture générale, mais un repère présenté comme [FV officiel] qui est un maximum calculé (E1), un seuil de recrutement faux (E2), une marge de cadrage arrondie vers le haut (E3) et un objectif de dépendance affiché sans être modélisé (E4). | **4.** Refuse les notes chiffrées de pure apparence (strat-S3:83), consacre une section aux risques de sa propre stratégie (strat-S3:547-553), dit d'où vient son coefficient (strat-S3:273). Mais elle tire de ce coefficient une conclusion trop favorable (E6). |
| **Fidélité à l'ambition de Morgan** | **3.** Garde le pilotage du portefeuille comme cible à 12-24 mois, atteinte par paliers payés (strat-S1:76). | **5.** C'est l'ambition elle-même, bornée et traduite en couverture mesurable (projets suivis par JP de pilotage ; strat-S2:126-130). | **2.** S'en éloigne explicitement : Marwin devient « outilleur et pilote léger », la porte d'un pilotage plus large ne se rouvre qu'au 6e mois sur preuves (strat-S3:114). |

---

## 3. Respect des décisions et des entités de GianLuca

| Exigence | S1 | S2 | S3 |
| --- | --- | --- | --- |
| Une offre adressée à une entité nommée, pas « à Carlone » en général (syn-P:306) | Oui : entité « chef de file », un bon de commande par lot et par entité (strat-S1:164, 109) | **Le mieux traité** : fiche de mission par entité et capacité répartie par entité, pour qu'aucune ne consomme le temps payé par une autre (strat-S2:209) | Oui : contrat-cadre et fiches de mission par entité ; la structure qui vend est nommée dans chaque message (strat-S3:186, 420) |
| Décisions réservées au client | Contrats, recrutements, emprunts, investissements, priorités (strat-S1:421-425) | Idem, plus arbitrage en comité (strat-S2:440-444) | Idem ; « par défaut, Marwin n'engage aucune dépense au nom du client » (strat-S3:448) |
| Le silence ne vaut pas accord | Oui, et la contradiction OFF:206 / ACC:103 est tranchée (strat-S1:445) | Oui ; « réputé accepté » retiré (strat-S2:459) | Oui ; limité au paiement d'un livrable (strat-S3:462) |
| Ses comptes et ses données à son nom | Oui (strat-S1:113, 316) | Oui, dès le cadrage (strat-S2:173) | Oui, dès le premier jour (strat-S3:493) |
| Déclarer le lien de Morgan avec BOJ.ART | **Ambigu** : « information du client » dans le pacte, mais « le dit au client si le sujet vient » plus loin (E9) | Déclaration proactive (strat-S2:428) | Déclaration écrite proactive (strat-S3:431) |
| Corriger le prénom dans ce qu'il a pu recevoir | Oui (strat-S1:154, 460) | Non traité (E11) | Non traité (E11) |

---

## 4. Erreurs de fait ou de calcul relevées

Recalculs : `j1-calc/verif.py` [ES]. « Gravité » vue de l'angle client.

| N° | Stratégie | Affirmation | Vérification | Correction | Gravité |
| --- | --- | --- | --- | --- | --- |
| E1 | S2 | Le Diag Data IA est « le seul prix public solide », « 1 250 € par jour [FV officiel] » ; le prix cible de Marwin « reste sous le prix public d'un jour d'expert IA (1 250 €) » (strat-S2:179, 291) | Le contrôleur a établi que 10 000 € est un **plafond de devis** et que 1 250 € est un maximum calculé [ES], pas un prix constaté ; il demande de ne pas s'en servir pour dire que Marwin est bon marché (ver-R6-marche.md:28, 68). Le dispositif est en outre réservé aux entités de 10 à 2 000 salariés et d'au moins 1 M€ de chiffre d'affaires ; les entités de GianLuca n'y sont probablement pas éligibles [HY] | Retirer cet argument de la justification du prix ; au plus, citer le Diag Data IA comme format de référence (8 jours, devis plafonné), sans en tirer un prix par jour | Moyenne : argument de prix trompeur si répété au client |
| E2 | S2 | « Si le besoin stable dépasse 15 JP par mois pendant plus de 12 mois, un recrutement est moins cher pour GianLuca » (strat-S2:218) | Un chef de projet cadre coûte 5 380 à 6 150 € par mois (rj-R6-marche.md:128 ; ver-R6-marche.md:25). Au prix S2 de 900 € par JP, cela équivaut à **6,0 à 6,8 JP** ; à 750 €, à 7,2 à 8,2 JP [ES] | Le seuil est d'environ **6 à 8 JP par mois** de besoin stable, pas 15. Le dire tel quel à GianLuca, et en faire un argument pour l'offre d'aide au recrutement (C7) | **Élevée** : la « comparaison honnête » sous-estime l'alternative d'un facteur 2 |
| E3 | S2 | Marge du cadrage à 7 500 € « de 0 à 15 % selon la rémunération visée » (strat-S2:181) | Avec ses propres coûts (810 à 1 065 € par JP × 8 JP = 6 480 à 8 520 €), la marge va de **−14 % à +14 %** [ES] | Écrire « −14 % à +14 % » ; le cadrage est à perte si la cible est de 2 500 € nets par associé avec réserve | Faible à moyenne |
| E4 | S2 | Scénario central : B2 (9 JP), un lot par mois (≈ 2 500 €) et D1 (≈ 1 500 €), avec un objectif de part de GianLuca « ≤ 85 % » au mois 12 (strat-S2:361-369) | 9 + 2 500 / ≈ 925 € + 1 à 1,5 JP = **12,7 à 13,2 JP** pour 12 JP facturables disponibles (syn-capacite-ia.md:190) [ES]. Tout le chiffre d'affaires central vient de GianLuca : tenir 85 % suppose ≈ **2 100 € par mois** d'un autre client, non modélisé et sans capacité pour le servir [ES] | Ramener le central à B1 ou B2 sans D1, ou inscrire le second client dans les chiffres en réduisant les lots ; ne pas afficher 85 % sans le modéliser | **Élevée** : le scénario recommandé dépasse la capacité qu'il s'impose |
| E5 | S2 | « Premier encaissement en décembre 2026 » ; chiffre d'affaires de la première année ≈ 112 000 € (strat-S2:355, 364) | Le recalcul retrouve 112 300 € si B2 démarre en avril, et 109 700 € si l'on respecte la condition « trois mois de B1 » (strat-S2:204) [ES]. Aucun rendez-vous n'est fixé (note:5) [DR] ; chaque mois de retard retire un mois de régime (≈ 12 000 €) de la fenêtre décembre-novembre | Présenter 112 000 € comme le haut de la fourchette ; décaler le mois 1 en janvier comme S1 et S3 | Faible |
| E6 | S3 | Le coût complet central vaut 500 à 580 € par JP, donc 750 € couvre le coût « avec une marge de 23 à 34 % » ; le plancher de 2 500 € nets par ETP est « atteint » en central (strat-S3:270, 277, 380) | Le coût par ETP est tiré de OFF:114, un modèle **SARL** à nets **après impôt sur le revenu** (3 889 € pour 2 500 € nets, coefficient ≈ 1,56), sans la réserve de 10 % (strat-S3:273). Or S3 recommande une **SAS** (strat-S3:396), où le coefficient est de 1,7 à 1,9 (syn-droit.md:98). Avec la SAS et la réserve, le coût central est de **590 à 740 €** par JP et la marge sur 750 € de **2 à 21 %**. Le disponible central (≈ 4 550 € par mois) donne 2 395 € nets à deux au coefficient 1,9, sous les 2 875 € qu'exige le plancher (1,15 ETP × 2 500 €) [ES] | Recalculer avec le coefficient de la forme recommandée et la réserve ; écrire « plancher atteint seulement en SARL ou avec une rémunération réduite » | **Moyenne à élevée** : surestime la rentabilité de la stratégie la moins chère |
| E7 | S3 | Réception de l'offre C : « la personne désignée utilise le registre pendant 4 semaines consécutives » ; offre B : « résultats d'au moins 90 % des appels réimportés » ; lots payés 40 % à la commande et 60 % à la réception (strat-S3:197, 215, 328) | Ces conditions dépendent d'actes de GianLuca (recruter, faire appeler) que Marwin ne contrôle pas [FV, lecture du texte] | Séparer la réception des livrables de Marwin (outils, procédures, fiches, kit) de la mesure d'usage ; si le client n'a pas désigné de personne ou lancé les appels sous 15 jours ouvrés, la réception des livrables est prononcée et la mesure devient un lot optionnel | Moyenne |
| E8 | S1, S3 | S1 : « seul rôle accepté [client] pendant au moins douze mois », mais bureaux « au plus tôt au mois 6 » et salariat « pas avant le bilan du mois 6 » (strat-S1:396-398). S3 : « seul rôle accepté pendant les 6 premiers mois », mais bureaux après 3 mois (strat-S3:420-421) | Incohérence interne [FV, lecture du texte] | Une seule règle : client seul jusqu'au bilan qui sert de déclencheur (6 mois proposé), chaque autre rôle par accord séparé ensuite | Faible |
| E9 | S1 | Pacte : « déclaration écrite des liens […] ; information du client » (strat-S1:389) ; plus loin, Morgan « le dit au client si le sujet vient » (strat-S1:409) | Incohérence interne ; vu du client, un conflit d'intérêts se déclare avant d'être découvert (syn-sources.md:325, ASS-4) | Déclaration écrite proactive, comme S2 et S3 | Moyenne |
| E10 | S1 | Objectif « part de GianLuca ≤ 80 % au mois 12 » avec un second client « signé et payé » (strat-S1:402, 495), sans que ce client figure dans le chiffre d'affaires central | Le central utilise 10 à 11 JP sur 12 : il reste 1 à 2 JP pour servir un autre client [ES] | Inscrire le second client dans les chiffres, ou viser ≤ 80 % au mois 18 | Faible |
| E11 | S2, S3 | Aucune mesure pour corriger le prénom du client dans les pièces qui lui étaient destinées (zéro occurrence du sujet dans les deux fichiers) | Deux pièces rédigées pour lui portent « John-Lucas » [sic, lire GianLuca] : V5 p. 1 et 5, et la lettre ACC:9-11 (syn-sources.md:43) [FV] | Reprendre la mesure de S1 : aucune occurrence de l'ancien prénom dans un document remis ; correction mentionnée sobrement si une pièce erronée a été reçue | Moyenne (relation) |
| E12 | S3 | Quali Contact « est établi à Cosne [FV] » et « spécialisé dans la collecte de dons [FV] » (strat-S3:91) | Siège à Clichy ; établissement secondaire à Cosne-Cours-sur-Loire (10 à 19 salariés) ; code NAF 73.20Z ; la collecte de dons est l'**activité affichée**, pas une spécialité enregistrée (ver-R6-marche.md:30-31) | « Établissement à Cosne ; activité affichée de collecte de dons, qui relève d'un régime de prospection différent » | Faible |

**S1 : aucun écart de calcul significatif.** Le juge retrouve son coût complet (591 à 737 € par JP en central, 744 à 962 € en prudent), la marge du cadrage (1 à 21 %), le chiffre d'affaires central sur 12 mois (94 500 €) et l'exposition maximale (≈ 5 250 €) [ES].

---

## 5. Repères recalculés par le juge, communs aux trois stratégies

**Revenu net par associé à 12 JP facturés par mois** (SAS, coefficient 1,7 à 1,9, réserve de 10 % du chiffre d'affaires, frais fixes de 1 500 à 2 500 € par mois, avant impôt sur le revenu) [ES] :

| Prix moyen par JP | Chiffre d'affaires mensuel HT | Net par associé et par mois |
| --- | --- | --- |
| 750 € | 9 000 € | ≈ 1 470 à 1 940 € |
| 800 € | 9 600 € | ≈ 1 620 à 2 100 € |
| 900 € | 10 800 € | ≈ 1 900 à 2 420 € |

Les trois stratégies paraissent se contredire sur le taux de 750 € (« trop bas » pour S2, « proche du coût » pour S1, « couvre avec marge » pour S3). En réalité, elles ne visent pas la même rémunération : S2 paie 2 000 à 2 500 € nets **à chaque associé** pour un temps partiel, S1 paie 2 500 € **par équivalent temps plein**, S3 utilise un coefficient de SARL (E6). La question à trancher n'est donc pas le taux, mais la **rémunération cible** des associés (inconnue U19, syn-sources.md:367).

**Coût annuel pour GianLuca, scénario central** [ES] :

| Stratégie | HT | Si la TVA n'est pas récupérable par son entité |
| --- | --- | --- |
| S1 | ≈ 94 500 € | ≈ 113 400 € |
| S2 | ≈ 112 000 € | ≈ 134 400 € |
| S3 | ≈ 80 000 € de Marwin + 27 000 à 40 000 € d'assistant + appels | ≈ 123 000 à 136 000 € + appels (la TVA ne porte que sur la part Marwin) |
| Rappel : offre des archives, formule de base | 90 000 € sur six mois (OFF:16) | 108 000 € sur six mois |

---

## 6. Meilleures idées à greffer

### 6.1 De S1

1. **Le cadrage comme test du besoin, vendu une seule fois, à marge volontairement faible**, avec un plancher interne : en dessous, on réduit le périmètre, pas le prix (strat-S1:172-175).
2. **Le pilote de huit semaines « un socle et un lot »**, sans tacite reconduction, avec des critères d'adoption et d'abandon chiffrés (strat-S1:186-198).
3. **Un échéancier par type de prestation** (capacité réservée d'avance, livrables par acompte et solde, variable à terme échu) et l'exposition maximale chiffrée à ≈ 5 000 à 6 000 € (strat-S1:299-318).
4. **Mandat de dépense à 0 € pendant le cadrage et le pilote** (strat-S1:434).
5. **« Le silence vaut livraison pour la facturation du solde, jamais approbation d'une suite »** (strat-S1:445).
6. **Report si aucun rendez-vous ou aucune entité payeuse avant mi-décembre** (strat-S1:531).
7. **En cas de refus du cadrage, remettre à GianLuca ce qui lui revient**, sans contrepartie (strat-S1:533) : un geste qui préserve la relation. À exécuter seulement après avis sur le rôle de chacun au regard des données personnelles [HY].
8. **Vérifier qu'aucun document de Marwin ou de Carlone ne reste dans le dépôt public BOJART** (strat-S1:154).

### 6.2 De S2

1. **Réception expresse et cession des droits à la réception expresse et au paiement complet**, avec un solde exigible à 30 jours faute de réserve motivée (strat-S2:182, 316).
2. **Engagements de service mensuels et malus de 5 % versé en avoir**, jamais en travail gratuit (strat-S2:221, 283).
3. **Paliers du pilotage définis par le nombre de projets suivis** (limite d'encours), lisibles pour le client, avec une capacité nominative répartie par entité (strat-S2:201-215).
4. **Registre et tableau de bord ouverts dès le cadrage sur un compte de l'entité cliente**, et mesure de référence des pilotes faite pendant le cadrage (strat-S2:173).
5. **Aide au recrutement d'un coordinateur local (lot C7)**, à proposer dès que le besoin stable dépasse 6 à 8 JP par mois (seuil corrigé, E2) (strat-S2:238).
6. **K-bis et attestation Urssaf remis au client** à la signature puis tous les six mois : un signe de sérieux qui protège aussi le payeur (strat-S2:502 ; syn-droit.md:385-393).
7. **Exercice de sortie à blanc** et restitution complète en 15 jours ouvrés au plus (strat-S2:222, 510).
8. **Retirer « vendre vos œuvres avec le CRM »** du diaporama, qui se lit comme une obligation de résultat (strat-S2:584 ; deck/slides/proposition.html:3).
9. **Registre « décision → documents touchés »** pour qu'une décision comme celle du 4 nov. ne soit plus appliquée à un seul support (strat-S2:442).

### 6.3 De S3

1. **Le diagnostic « l'offre est née du besoin du vendeur »** (strat-S3:65) : c'est la bonne question à se poser avant le rendez-vous.
2. **Montrer à GianLuca la comparaison de coûts** (Marwin, assistant salarié, rendez-vous payés à l'unité) plutôt que de la lui laisser découvrir (strat-S3:95-103).
3. **Les préalables du pilote commercial** : 5 à 10 œuvres réellement disponibles avec leur prix, structure vendeuse nommée, avis fiscal écrit, appelant désigné, entreprises seulement ; seuils de poursuite fixés **avec** GianLuca **avant** l'essai ; les ventes suivies à part, jamais promises (strat-S3:189-198).
4. **L'outillage remis à une personne qu'il désigne** (procédures avec secours manuel, formation, comptes à son nom), qui répond à « ne pas gérer chaque détail » sans payer d'exécution à 750 € (strat-S3:200-216), avec un critère de réception corrigé (E7). C'est aussi la seule proposition qui traite concrètement la formation et la transition de ses équipes (DEMANDE.md § 8).
5. **Corriger le simulateur fiscal du CRM dans la remise en ordre** (strat-S3:155), puisqu'il surestime l'économie d'impôt présentée aux prospects.
6. **Le socle comme liste fermée** dont le prix ne baisse pas quand l'automatisation réduit le temps (strat-S3:224-229, 313).
7. **La concession de paiement encadrée** : facturation de fin de mois seulement après trois échéances payées à l'heure (strat-S3:344-346).
8. **Refuser d'être payé en bureaux, en emploi ou en capital** (strat-S3:515).
9. **Une section « risques de la présente stratégie »** (strat-S3:547-553) : à reprendre dans la synthèse finale.

---

## 7. Ce qu'aucune proposition ne traite

| N° | Sujet manquant | Pourquoi c'est important pour GianLuca ou pour Marwin | Ce qu'il faudrait faire [PR] |
| --- | --- | --- | --- |
| 1 | **Vérifier l'existence et la solvabilité de l'entité au-delà du SIREN.** | La demande interdit de prendre un patrimoine supposé pour une trésorerie (DEMANDE.md § 3). Les trois stratégies se contentent d'un SIREN et d'un acompte. | Une fois l'entité nommée par GianLuca, consulter sans contact les registres publics : statut actif, dirigeant habilité, comptes déposés, annonces de procédure collective. Proportionner l'acompte et la durée du premier engagement au résultat. |
| 2 | **Régime du contrat si GianLuca signe à titre personnel ou par une entité de cinq salariés au plus, hors établissement.** | Le scénario « GianLuca signe à titre personnel » existe (syn-portefeuille.md:302). Pour une vente d'œuvres, syn-droit rappelle le délai de rétractation de 14 jours et l'interdiction de tout paiement avant 7 jours hors établissement (syn-droit.md:530). Les mêmes règles pourraient s'appliquer au contrat de Marwin elle-même [HY] et contredire « 50 % à la commande, travail à l'encaissement ». | Question à l'avocat avant le rendez-vous ; à défaut, signer dans les locaux de Marwin ou à distance, avec l'entité commerciale de GianLuca. |
| 3 | **Échéance de l'aide régionale au conseil.** | Toutes notent le dépôt avant signature (strat-S1:322 ; strat-S2:185 ; strat-S3:173), aucune l'échéance annoncée au **31 décembre 2026**, « dans la limite des crédits » [DR] (syn-droit.md:71). Si l'aide compte pour GianLuca (jusqu'à 50 % du cadrage), la fenêtre peut se fermer avant la signature. L'éligibilité d'un prestataire nouveau, sans références, est [IN]. | Poser la question dès le premier contact et vérifier l'échéance auprès de la Région ; ne pas retarder le cadrage pour une aide incertaine. |
| 4 | **Coût réel selon la situation de TVA de l'entité cliente.** | Les prix sont donnés hors taxes. Si GianLuca signe à titre personnel, par une société civile immobilière ou par une entité dont les opérations ne sont pas taxées, la TVA de 20 % est un coût réel [HY]. | Question à poser au rendez-vous ; montrer les prix HT et TTC. |
| 5 | **Le message à GianLuca sur le recadrage.** | Il a peut-être vu l'offre à 15 000 €, la lettre au mauvais prénom ou le diaporama de 13 diapositives avec STRATES (U04, syn-sources.md:352). Aucune stratégie ne traite le cas où il aurait **déjà accepté oralement** l'offre de six mois, ni ne prévoit le texte qui lui annonce le recadrage, la fuite et la correction du prénom. S1 prévoit seulement une « correction écrite » en repli (strat-S1:564). | Une page datée, signée des deux associés : ce qui change et pourquoi (en commençant par l'intérêt du client), ce qui est retiré, ce qui reste à lui, l'incident de données et les mesures prises (après avis de l'avocat), la proposition de cadrage. |
| 6 | **Le canal de travail réel de GianLuca et l'identité de ses équipes.** | Les critères d'adoption (registre consulté chaque semaine, 80 % des comptes rendus commentés) supposent qu'il travaille sur un outil écrit. On ignore s'il préfère le téléphone, la messagerie ou le papier, et qui sont ses collaborateurs [IN]. | Inscrire dans le cadrage : canal préféré, personnes qui utiliseront les outils, résistances prévisibles. Mesurer l'adoption dans le canal qu'il emploie déjà. |
| 7 | **La valeur chiffrée pour GianLuca.** | Les mesures de référence portent sur les processus de Marwin. Aucune stratégie ne chiffre le **coût du statu quo** pour lui (ses heures, les ventes manquées, les lieux inoccupés), ni le résultat qu'un lot doit produire pour payer son prix. S3 s'en tient à une phrase (strat-S3:194). | Un livrable du cadrage : pour chaque priorité, coût actuel estimé avec lui, résultat attendu, seuil au-delà duquel le lot se rentabilise pour lui. |
| 8 | **Les conséquences de la fuite déjà survenue.** | Une assurance de responsabilité civile professionnelle souscrite après coup ne couvre en général pas un fait antérieur déjà connu [HY]. Aucune stratégie n'évalue l'exposition de Morgan et Mathys (sanction, réclamation d'une personne, perte de confiance de GianLuca), ni ne dit qu'il faut un avis avant toute formule écrite qui reconnaîtrait une responsabilité. | Question à l'avocat ou au délégué à la protection des données, en même temps que la décision de notification ; déclaration exacte de l'incident à l'assureur au moment de la souscription. |
| 9 | **Une réception du pilote commercial qui ne dépend pas des appels.** | Dans les trois stratégies, la réception du pilote CRM suppose que d'autres appellent (strat-S1:207 ; strat-S2:232 ; strat-S3:197). | Deux temps : livrables de Marwin réceptionnés à la remise (fiches sourcées, kit validé, outil de réimport) ; mesure des appels facturée seulement si les appels ont lieu. |
| 10 | **La liste exacte des corrections du diaporama de 11 diapositives.** | Le seul support « corrigé » promet encore un CRM « prêt à servir » alors que 283 numéros sur 471 restent à confirmer (syn-sources.md:508), prévoit de « montrer le CRM en direct » pendant une violation probable (syn-droit.md:636), annonce les formules à 15 000 et 30 000 € et l'option laboratoire, et fait démarrer le travail « à réception » d'un acompte impossible à encaisser (deck/slides/livre.html:4, 26 ; formules.html:20, 30 ; laboratoire.html:9 ; paiement.html:10). S2 en relève deux points, S1 et S3 un seul. | Une liste de retrait diapositive par diapositive, jointe à la décision écrite sur Medhi et BOJ.ART. |

---

## 8. Recommandation de synthèse

### 8.1 Principe

**Base : le parcours de S1** (remise en ordre non facturée, cadrage au forfait, pilote court, récurrent seulement sur demande écrite), parce qu'il expose le moins GianLuca et Marwin à une promesse non tenue et qu'il est le seul sans erreur de calcul notable. **Greffes** : les mécanismes de réception et de protection du client de S2 (§ 6.2), les options centrées sur le besoin réel de S3 (§ 6.3). **Corrections** : les erreurs E1 à E12, avant toute réutilisation d'un chiffre. **Ajouts** : les dix points du § 7.

### 8.2 Le parcours recommandé [PR]

| Étape | Contenu | Prix et paiement [PR] | Condition de passage |
| --- | --- | --- | --- |
| **0. Remise en ordre** (4 au 19 nov. 2026), non facturée | Décision sur la notification à la CNIL avec un avocat ou un délégué à la protection des données, avant l'échéance du 5 nov. ou avec un retard motivé ; dépôt rendu privé et vérifié ; fiche de violation. Décision écrite sur Medhi et BOJ.ART validée par Mathys ; PR n° 1 fermée ou son PDF marqué « historique » ; offre écrite, STRATES v1.1, vernissage marqués « retirés » ; diaporama corrigé selon la liste du § 7, point 10. Simulateur fiscal corrigé. Fiche des disponibilités nominatives ; principes du pacte. Message d'une page à GianLuca (§ 7, point 5). Questions à l'avocat (§ 7, points 2 et 8). | 0 € | Toutes les conditions de S1 (strat-S1:504-512), sauf l'acompte |
| **1. Rendez-vous** (avant mi-décembre, sinon report) | Une seule proposition : le cadrage. Questions bloquantes : entité, signataire, payeur, valideur ; trois priorités et leur coût actuel ; budget et mode de paiement ; canal de travail ; aide régionale ; situation de TVA ; ce qu'il a vu ou accepté. | — | Entité nommée ; lettre d'intention ou bon de commande « en formation » |
| **2. Cadrage** (3 à 4 semaines après l'acompte) | Livrables de S1 et de S2 : inventaire validé des entités, lieux, projets et accès ; trois priorités avec **coût du statu quo** et seuil de rentabilité pour lui ; carte des rôles (exploitant, vendeur, responsable du traitement) ; grille de délégation ; registre ouvert à son nom ; décision écrite sur le CRM (S3). Réception expresse (S2). | **6 000 € HT** (fourchette 6 000 à 6 500 € ; plancher 5 000 €), 50 % à la commande, 50 % à la réception ou à 30 jours sans réserve motivée. Pas de 7 500 € tant qu'aucune référence n'est démontrable. | Cadrage payé à l'échéance ; inventaire validé par écrit ; au plus tard le 31 janvier 2027 (S2, S3), sinon report sans date |
| **3. Suite choisie par GianLuca**, une à la fois | **(a) Ventes d'œuvres** : pilote commercial de S3, avec ses préalables, au prix de S1 (4 500 à 6 000 € HT), réception en deux temps (§ 7, point 9). **(b) Pilotage** : pilote de huit semaines de S1 (socle de 3 500 € HT par mois et un lot), engagements de service et malus de S2. **(c) Embauche** : outillage et passation de S3 ou aide au recrutement C7 de S2, avec une réception qui ne dépend pas du recrutement (E7). | Lots : JP estimées × 800 € + 10 à 15 % de provision, plancher de 750 € par JP (S1) ; 40 % à la commande, 60 % à la réception | Critères du pilote tenus quatre semaines ; paiements à l'heure ; demande écrite de poursuivre |
| **4. Récurrent** (au plus tôt au mois 4) | Socle par paliers de S2 (limite d'encours, capacité nominative par entité), avec des prix proches de S1 tant que Marwin n'a pas de références (≈ 4 500 € HT pour le socle et deux projets). Exploitation au volume (offre D de S2) seulement après un pilote réussi. | Socle d'avance le 1er du mois ; fin de mois seulement après trois échéances à l'heure (S3) | Bilan au mois 6 avec sortie à blanc ; occupation ≤ 85 % ; second client inscrit dans les chiffres |

### 8.3 Règles qui ne se négocient pas [PR]

- Aucun travail, aucun encaissement avant l'immatriculation et l'acompte ; aucune donnée personnelle réelle avant la désignation du responsable du traitement et le contrat de l'article 28.
- Aucun taux journalier affiché au client : des forfaits par résultat ; 750 € reste un plancher interne de chiffrage, jamais remisé.
- Aucune commission sur les ventes, aucun encaissement pour la galerie, aucune obligation d'exploitant, aucun robot devant le public, aucune R&D sans financeur écrit.
- Client seul jusqu'au bilan du mois 6 ; bureaux, emploi et capital ensuite, chacun dans un accord séparé, jamais contre une baisse d'honoraires.
- Lien de Morgan avec BOJ.ART déclaré par écrit à GianLuca dès le premier document remis.

### 8.4 Ce qui va à GianLuca et ce qui reste interne

| Destiné à GianLuca (après accord écrit de Morgan et de Mathys) | Interne |
| --- | --- |
| Le message de recadrage d'une page ; la proposition de cadrage (objet, livrables, réception, prix HT et TTC, paiement) ; les principes de gouvernance (décisions réservées, silence, plafonds) ; la comparaison de coûts entre Marwin, un salarié et des prestataires (S3, corrigée par E2) | Coûts complets, marges, planchers, rémunérations des associés, scénarios de trésorerie, présent jugement et les trois stratégies |

### 8.5 Conditions de validité de cette recommandation

Elle tient si : la fuite est traitée sans conséquence qui interdise la relation ; Mathys approuve le parcours et donne une disponibilité écrite ; les deux associés acceptent un revenu de l'ordre de 1 500 à 2 400 € nets chacun en régime (§ 5) en gardant d'autres revenus la première année. Elle est à revoir si GianLuca demande d'emblée un pilotage large **et** fournit entité, accès et acompte : on passerait alors plus vite à l'étape 4, en gardant la limite d'encours de S2. Elle conduit à **reporter** sans travail gratuit si aucune entité n'est nommée avant mi-décembre ou si le cadrage n'est pas payé au 31 janvier 2027, et à **refuser** toute demande de 20 à 40 JP sans entité, mandat ni accès.

---

## 9. Limites du jugement

- Aucune parole directe de GianLuca Carlone n'existe dans les pièces (syn-sources.md:38) : toute note sur la « valeur pour lui » reste une hypothèse [HY] fondée sur des besoins rapportés par Morgan [DR].
- Les coefficients de coût en SAS (1,7 à 1,9) viennent d'une source secondaire (syn-droit.md:98) ; les frais fixes de Marwin sont des hypothèses [HY] ; aucune simulation officielle n'a été faite.
- Les points 2, 4 et 8 du § 7 sont des hypothèses juridiques ou fiscales [HY] à soumettre à un avocat ou à un expert-comptable ; le juge ne les a pas vérifiées dans les textes.
- Les calculs des stratèges ont été refaits indépendamment ; leurs scripts (`s1-calc/`, `s2-calc/`, `s3-calc/`) n'ont pas été exécutés.
- La visibilité actuelle du dépôt FinanceScope/CRM-Carlone n'a pas été revérifiée par le juge [IN]. La collecte ChatGPT reste incomplète (169 conversations lues sur 219) : des promesses faites au client peuvent exister hors du corpus.
