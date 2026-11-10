# Stratégie retenue : la référence de l'audit Marwin Tech × GianLuca Carlone

Rédigée le 4 novembre 2026 au soir par l'arbitre final de l'audit. Tous les livrables de l'audit suivent ce document. Quand un livrable s'en écarte, il doit dire pourquoi.

**Document interne.** Il contient des coûts, des marges, des planchers de prix, des rémunérations visées, des probabilités et la stratégie des associés. Il ne doit pas être transmis à GianLuca Carlone. La section 17 dit ce qui peut passer dans un document qui lui est destiné, et sous quelle forme.

---

## Méthode, sources et conventions

**Pièces lues en entier** : les trois propositions `strat-S1-progressif.md` (S1), `strat-S2-pilotage.md` (S2) et `strat-S3-contradicteur.md` (S3) ; les deux jugements `juge-J1-client.md` (J1) et `juge-J2-marwin.md` (J2) ; les consignes `BRIEF-AGENTS.md`, `DEMANDE.md` et `note-point-4-novembre-et-activites.md` (NOTE). **Lues par sections utiles** : les quatre synthèses `syn-sources.md` (syn-S), `syn-portefeuille.md` (syn-P), `syn-capacite-ia.md` (syn-C) et `syn-droit.md` (syn-D) ; `rj-R3-travail-contrats.md` (f) et `ver-R6-marche.md` (n° 1 à 10). Tous ces fichiers sont dans `audit-work/`.

**Pièces d'origine rouvertes ce soir, en lecture seule** : dépôt `Momolscode/Carlone`, `origin/main` = 7b46602 (« Ajouter tous les livrables locaux Carlone… », 4 nov. 2026, 17:37 +0100), vérifié par `git log` ; lignes OFF:13-22, 110-120, 204-209 ; ACC:7, 13, 55-58, 64-66, 100-103 ; COP:13, 65 ; AUD:3, 15 ; CTX:5, 11. Diaporama client en ligne, copie locale `scratchpad/artifact-files/04f14ef8-a5fd-429b-9b3e-6d69b1d2ce5f/project/` (abrégée « deck/ ») : `deck.json:7` et les textes de `cover`, `livre`, `proposition`, `volets`, `premier-mois`, `formules`, `paiement`, `laboratoire`, `garanties`, `cadre`, `etapes`.

**Calculs.** Refaits en Python (`python3 -I`) dans `audit/2026-11-04-audit-strategique/annexes/travaux/calculs/arbitre-calc/verif.py` (abrégé « verif »). Ils couvrent le coût complet d'une journée, le seuil de comparaison avec un salarié, les marges par offre, les trois scénarios et l'exposition de trésorerie. Tous leurs résultats sont des estimations [ES].

**Règle d'arbitrage.** Quand un contrôleur corrige un lecteur, la correction fait foi. Quand un juge relève une erreur de calcul ou de cohérence, elle est corrigée ici (section 2.3). Quand les deux juges divergent, l'arbitre tranche et le dit.

**Aucune action extérieure.** Aucun contact, aucune dépense, aucune modification hors de ce fichier et du script de calcul. Les décisions décrites ici sont des recommandations à Morgan Olsen et Mathys Couet : rien n'a été fait.

**Nom du client.** Le client s'appelle **GianLuca Carlone**. Les pièces qui portent « John-Lucas » [sic, lire GianLuca] sont citées telles quelles.

**Codes.** [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] information inconnue. Sans autre précision, une [PR] est une proposition de ce document.

**Abréviations.** OFF = `interne/offre-marwin-tech-remuneration-et-collaboration.md` (2 nov.) ; ACC = `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md` (29 oct.) ; COP = `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md` (28 oct.) ; AUD = `interne/audit-marwin-tech-carlone.md` (2 nov.) ; CTX = `interne/contexte-projet-carlone.md` (4 nov.) ; V5 = `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf`. « S1:172 » renvoie à `strat-S1-progressif.md:172`, et ainsi de suite. **JP** = journée-personne de 7 h ; deux personnes présentes une journée consomment 2 JP.

---

## 0. Trois faits nouveaux pris comme base

1. **Retrait de Medhi et de BOJ.ART.** Le 4 nov., Morgan a demandé de les retirer de l'offre (« Va juste falloir enlever Medhi/boj art de l'offre ») [DR] (NOTE:25). Seul le diaporama client a été corrigé : 11 vues, sans `strates` ni `strates-phases` [FV] (deck/deck.json:7). Restent non corrigés [FV] : l'offre écrite (« Option création », OFF:22), STRATES v1.1, le diaporama du vernissage et le PDF de 13 diapositives de la PR n° 1 (syn-S:236). La décision n'est formalisée ni avec Mathys ni avec Medhi [IN].
2. **Violation de données très probable.** Le dépôt public FinanceScope/CRM-Carlone contient environ 800 à 931 numéros et 206 e-mails selon la copie et la méthode [ES] (syn-S h.1). Il était public le 4 nov. à 16 h 19 [DR] (CTX:11). La connaissance date au plus tard du 2 nov. [FV] (AUD:3, 15). Si elle date du 2 nov., le délai de 72 h pour notifier la CNIL **expire le 5 nov.**, à une heure inconnue [ES] (syn-D:623, corrigé par ver-R4 n° 7).
3. **Aucune base contractuelle.** Aucun contrat, aucune facture, aucune entité payeuse identifiée [FV négatif] (syn-S:39). Marwin Tech n'est pas immatriculée [DR] (OFF:153).

---

## 1. Verdict ferme et conditions de validité

### 1.1 Verdict

1. **Oui à une collaboration avec GianLuca Carlone, non à l'offre actuelle.** Marwin ne doit ni présenter ni signer l'accompagnement de six mois à 15 000 ou 30 000 € HT par mois (OFF:13-16). Aucune parole directe du client ne le demande [FV négatif] (syn-S:38). Aucune entité ne s'est engagée à payer. La formule de base demande 78 à 83 % du temps disponible des deux associés, et le renforcement 140 à 145 % [ES] (syn-C:228-229). Le seul actif livré, le CRM, est exposé dans un dépôt public.
2. **Une seule proposition commerciale : un cadrage court au forfait** (6 500 € HT, 3 à 4 semaines, moitié à la commande), vendu à une entité identifiée de GianLuca. Il est précédé d'une **remise en ordre non facturée** (fuite de données, documents, structure, pacte). Il est suivi, seulement s'il est payé et réceptionné, d'un **pilote de huit semaines dans une voie choisie par GianLuca** : ventes d'œuvres, pilotage, ou outillage remis à une personne qu'il désigne (section 4.4).
3. **Un pilotage récurrent borné vient au plus tôt au quatrième mois**, sur décision écrite de GianLuca prise sur pièces. Il est vendu au périmètre (un socle et N projets actifs), avec des lots devisés à part. La capacité engagée reste d'au plus 10 JP facturables par mois la première année.
4. **Reporter sans travail gratuit** si aucune entité payeuse n'est nommée avant le **15 décembre 2026**, ou si le cadrage n'est pas payé au **31 janvier 2027**. **Refuser** toute demande de 20 à 40 JP par mois sans entité, sans mandat ni accès, toute commission sur les ventes d'œuvres et tout paiement en bureaux, en emploi ou en capital.
5. **L'ambition de Morgan** (piloter le portefeuille de GianLuca, DEMANDE § 2) reste la cible à 12-24 mois. Elle s'atteint par paliers payés et mesurés, pas par un abonnement d'entrée.

### 1.2 Conditions de validité

Le verdict tient si **toutes** les conditions suivantes sont réunies. Si l'une manque, la section 12 dit s'il faut réduire, reporter ou refuser.

| N° | Condition | Comment on le vérifie | Si elle manque |
| --- | --- | --- | --- |
| V1 | La fuite est traitée sans conséquence qui interdise la relation | Décision de notification documentée avec un avocat ou un DPD ; dépôt privé vérifié ; GianLuca informé par écrit | Rien ne démarre ; aucune donnée réelle |
| V2 | Mathys approuve par écrit cette stratégie, le retrait de Medhi et la SAS, et engage une disponibilité nominative | Fiche signée « rôles et disponibilités » | Pas de proposition au client tant que le désaccord dure |
| V3 | Les deux associés engagent ensemble au moins 6 JP facturables par mois (8 à 10 pour le scénario central) | Fiche nominative ; relevé mensuel | Réduire au cadrage et à un lot (S1:530) |
| V4 | Les associés acceptent un revenu modeste la première année (≈ 1 350 à 1 550 € nets chacun en régime central, section 6) et peuvent apporter 8 000 à 14 000 € | Décision écrite ; fonds déposés | Reporter (J2:159, M7) |
| V5 | GianLuca nomme une entité payeuse, accepte de payer un cadrage, fournit accès et délégué | Bon de commande, acompte, accès sous 10 jours ouvrés | Reporter ou refuser |
| V6 | Aucune promesse déjà faite au client ne contredit ce parcours | Réponse de Morgan sur ce que GianLuca a vu, reçu ou accepté (U04, syn-S:352) | Message de recadrage (section 17.3) avant tout rendez-vous |

**Révision vers le haut.** Si GianLuca demande d'emblée un pilotage large **et** fournit entité, accès et acompte, on passe plus vite au socle récurrent (offre B1), en gardant la limite d'encours et le plafond de 10 JP (J1:230).

---

## 2. Comment cette stratégie a été construite

### 2.1 Classement des trois propositions

| Proposition | J1 (angle client) | J2 (angle Marwin) | Force principale | Faiblesse principale |
| --- | :---: | :---: | --- | --- |
| **S1 « progressif »** | **31/40** | **31/40** | La plus prudente, la plus honnête sur les inconnues ; calculs exacts au recalcul (J1:115 ; J2:84) | Ventes d'œuvres reléguées après d'autres lots ; planchers sous le coût (J2:95) |
| S2 « pilotage » | 28/40 | 26/40 | Seule échelle crédible vers l'ambition ; meilleure réception (J1:77) | Scénario central saturé ; trois erreurs de chiffrage (J1:102-105) |
| S3 « contradicteur » | 26/40 | 27/40 | Part du besoin rapporté du client ; offre « outillage et passation » (J2:67) | Coefficient de SARL sous une SAS ; réceptions dépendantes d'actes du client (J1:107-108) |

**Base retenue : S1**, classée première par les deux juges. On y greffe les mécanismes de réception, de paliers et de protection de S2, et les options centrées sur le besoin réel de S3 (J1:202 ; J2:169-179).

### 2.2 Greffes retenues

| Idée | Origine | Où elle s'applique ici |
| --- | --- | --- |
| Réception expresse demandée ; cession des droits au paiement complet ; solde exigible faute de réserve motivée | S2:182, 316 | Sections 4.3, 5 |
| Paliers du socle définis par le nombre de projets suivis (limite d'encours), capacité nominative répartie par entité | S2:201-215 | Section 4.5 |
| La capacité du pilotage ne se convertit jamais en production ; report limité à 20 %, pour du pilotage | S2:215 | Sections 4.5, 4.10 |
| Engagements de service mensuels, malus de 5 % versé en avoir | S2:221, 283 | Section 4.5 |
| Changement de palier sans pénalité si un associé est absent plus de 10 jours ouvrés | S2:216 | Sections 4.5, 8 |
| Exercice de sortie à blanc et restitution en 15 jours ouvrés | S2:222 ; syn-C:870 | Sections 3, 4.5 |
| Registre « décision → documents touchés » | S2:442 | Section 8.1 |
| K-bis et attestation Urssaf remis au client à la signature, puis tous les six mois | S2:502 ; syn-D:382-393 | Sections 7, 10 |
| Consignes aux opératrices de Quali Contact via leur employeur | S2:462 | Section 8.1 |
| Partage des gains d'automatisation (un tiers au client après la première année) ; prime sur économie réelle mesurée | S2:252-256, 306 | Section 4.13 |
| Le diagnostic « l'offre est née du besoin du vendeur » | S3:65 | Sections 4.4, 16 |
| Comparaison de coûts présentée au client (Marwin, salarié, appels au rendez-vous), avec des chiffres corrigés | S3:95-103 ; J2:202 | Sections 4.9, 17 |
| Offre « outillage et passation » à une personne désignée ou recrutée par GianLuca | S3:200-216 | Section 4.6 (C6) |
| Préalables du pilote commercial (œuvres disponibles, structure vendeuse, avis fiscal, appelant, entreprises seulement) | S3:189-191 | Section 4.6 (C2) |
| Correction du simulateur fiscal du CRM dans la remise en ordre | S3:155 ; J2:115 | Section 4.2 |
| Socle en liste fermée, dont le prix ne baisse pas quand l'automatisation réduit le temps | S3:224-229 | Sections 4.5, 4.13 |
| Concession sur le paiement du socle seulement après trois échéances payées à l'heure | S3:344-346 | Section 5 |
| Les tiers facturent directement l'entité de GianLuca | S3:296 | Section 4.10 |
| Date butoir du 31 janvier 2027 | S3:508 | Sections 1, 12 |
| Section « risques de la présente stratégie » | S3:547-553 | Section 16 |
| Dix manques communs relevés par J1 (solvabilité, rétractation, aide régionale, TVA, message de recadrage, canal de travail, coût du statu quo, assurance et fuite, réception du pilote commercial, liste des corrections du diaporama) | J1:185-194 | Sections 4, 5, 10, 14, 17 |
| Onze manques relevés par J2 (limitation de responsabilité, assurance, notification échelonnée, art. 34 et prospection, rétractation, occupation sur tout le temps, liquidité, salariat chiffré, transferts IA, conflit avec la prospection propre, IS et TVA) | J2:153-163 | Sections 5, 6, 7, 8, 10, 12 |

### 2.3 Erreurs relevées et corrections retenues

| N° | Erreur | Correction retenue ici | Source |
| --- | --- | --- | --- |
| C1 | « 1 250 € par jour » du Diag Data IA présenté comme un prix public (S2:179, 291) | C'est un plafond de devis divisé par 8 [ES]. Il ne sert à justifier aucun prix. Les entités de GianLuca n'y sont probablement pas éligibles [HY] | J1:102 ; ver-R6 n° 6 |
| C2 | Recrutement moins cher au-delà de 15 JP par mois (S2:218) | Le seuil est d'environ **6 à 8 JP par mois** de besoin stable : un chef de projet cadre coûte 5 380 à 6 149 € par mois [MM], soit 6,0 à 8,2 JP à 750-900 € (verif § 2) | J1:103 ; J2:90 |
| C3 | Marge du cadrage S2 « de 0 à 15 % » | −14 % à +14 % avec les coûts de S2 ; le prix retenu ici est différent (section 4.3) | J1:104 ; J2:91 |
| C4 | Scénario central de S2 (B2 + lots + exploitation) dans 12 JP | Il demande 12,9 à 15,3 JP : rejeté. Le central retenu reste sous 10 JP facturables | J1:105 ; J2:92 |
| C5 | Premier encaissement en décembre 2026 (S2:355) | Mois 1 central = janvier 2027 ; décembre seulement dans le scénario ambitieux | J1:106 |
| C6 | Coût S3 calculé avec un coefficient de SARL sous une SAS | Coefficient SAS de 1,7 à 1,9 partout ; plancher de 2 500 € nets par ETP **non atteint** la première année | J1:107 ; J2:86-88 |
| C7 | Paiement des lots S3 dépendant d'actes du client (recruter, appeler) | **Livraison** (que Marwin contrôle) déclenche le paiement ; **adoption** (qui dépend du client) décide de la suite | J1:108 ; J2:112 |
| C8 | « Client seul » pendant 12 mois mais bureaux au mois 6 (S1) ; 6 mois mais bureaux au mois 3 (S3) | Une seule règle : client seul jusqu'au bilan du mois 6 ; chaque autre rôle ensuite, par accord séparé | J1:109 |
| C9 | Lien de Morgan avec BOJ.ART déclaré « si le sujet vient » (S1:409) | Déclaration écrite **proactive** dès le premier document remis | J1:110 |
| C10 | Cibles de dépendance (≤ 80 ou 85 %) absentes des chiffres de S1 et S2 | Central à 100 % assumé par écrit ; variante chiffrée avec un second client (section 6) ; cible ≤ 80 % reportée au mois 18 si la variante ne se réalise pas | J1:111 ; J2:97 |
| C11 | Pas de correction du prénom du client dans S2 et S3 | Aucune occurrence de l'ancien prénom dans un document remis ; correction mentionnée sobrement si une pièce erronée a été reçue | J1:112 |
| C12 | Quali Contact « établi à Cosne » et « spécialisé dans la collecte de dons » [FV] (S3:91) | Siège à Clichy ; établissement à Cosne-Cours-sur-Loire (10 à 19 salariés) ; collecte de dons = activité **affichée**, régime de prospection différent | J1:113 ; ver-R6 n° 8-9 |
| C13 | Planchers S1 sous le coût : cadrage à 5 000 € (625 € par JP), lots à 700 € par JP | Plancher absolu de **750 € par JP estimée** ; cadrage complet jamais sous 6 000 € HT | J2:95 |
| C14 | Apport de départ de 3 000 à 7 000 € (S1) | **8 000 à 14 000 €** | J2:96 |
| C15 | Projet supplémentaire du socle à + 1 000 € (S1:226), soit 667 € par JP à 1,5 JP | **+ 1 200 € HT** par projet actif en plus (800 à 1 200 € par JP) | verif § 4 (arbitre) |
| C16 | Coût complet retenu pour 12 JP facturables alors que la capacité engagée est plafonnée à 10 JP | À 10 JP facturés, le coût complet pour 2 500 € nets par ETP monte à **710 à 885 € par JP** : d'où un prix cible de 800 à 950 € et un revenu de première année sous ce plancher | verif § 1 (arbitre) ; J2:195 |
| C17 | Gel de la production gratuite « à partir du 15 nov. » (S3:477) | Gel **immédiat** | J2:113 |
| C18 | Pas de solution si l'échéance CNIL est dépassée (S3) | Notification échelonnée si le dossier est incomplet [HY], ou notification en retard motivée | J2:114 ; syn-D:623 |
| C19 | Bon de commande signé avant le dépôt de l'aide régionale (S2:331-337) | Dépôt du dossier, puis signature, puis acompte | J2:110 |
| C20 | Exploitation CRM de S2 à 12-18 € par fiche, sous le coût manuel (18 à 27 €) ; S1 à 40-70 € [HY] | Aucun prix par fiche publié avant la mesure de référence ; jamais sous le coût manuel mesuré | J2:94 |

### 2.4 Idées écartées

- Le cadrage à 7 500 € HT (S2:178) : aucune référence démontrable ne le justifie aujourd'hui (J1:210).
- Le palier « portefeuille étendu » (B3, S2:205) la première année : il demande les deux associés à 80 % ou plus et un sous-traitant (J2:93).
- Les bureaux « dès le départ par convention » (S2:418) : indice de requalification (J2:111).
- Le taux de 750 € comme taux de régie affiché (S3:249) : le client ne voit aucun taux journalier ; l'avenant de capacité est vendu à 900 € HT par JP (section 4.8).

---

## 3. Objectif principal

### 3.1 Énoncé [PR]

> **D'ici le 2 février 2027 (90 jours)** : avoir traité la fuite et remis en ordre tous les documents ; avoir vendu, encaissé et fait réceptionner un cadrage par une entité identifiée de GianLuca Carlone ; avoir obtenu sa décision écrite sur la suite.
>
> **D'ici le 4 mai 2027 (6 mois)** : avoir démontré sur pièces, par un pilote de huit semaines dans la voie qu'il a choisie, qu'un pilotage borné lui est utile (décisions préparées et prises, un livrable réceptionné, un outil réellement utilisé) et qu'il couvre le coût complet de Marwin, sans dépasser 10 JP facturables par mois ni 85 % d'occupation de chaque associé.
>
> **D'ici le 4 novembre 2027 (12 mois)** : tenir un socle récurrent renouvelé sur preuves, avec des gains mesurés sur au moins deux processus, une sortie testée, et un second client payant ou, à défaut, une dépendance assumée par écrit.

Cet objectif réunit les quatre exigences de la demande : résultat utile pour GianLuca, activité rentable pour Marwin, capacité soutenable, preuves pour poursuivre (DEMANDE § 10).

### 3.2 Ce que Marwin contrôle, ce qui dépend des autres

| Sous le contrôle de Marwin | Dépend de GianLuca Carlone | Dépend de tiers |
| --- | --- | --- |
| Traiter la fuite et documenter la décision ; corriger les documents ; arrêter le travail gratuit | Nommer l'entité qui signe, paie et valide ; payer à l'échéance | Avocat ou DPD : avis sur la notification et sur le contrat |
| Constituer la SAS, signer le pacte, souscrire la RC professionnelle | Fournir accès, pièces et délégué sous 10 jours ouvrés | Expert-comptable : simulations officielles, TVA, date de création |
| Qualité, délais, contrôle à quatre yeux, mesure des temps | Choisir trois priorités et décider dans les délais | Greffe : délai d'immatriculation [HY : 1 à 3 semaines] |
| Prix, plafonds de capacité, refus des demandes hors périmètre | Adopter les outils ; désigner ou recruter une personne qui exécute | Quali Contact, si une voie commerciale est choisie |
| Prospection d'un second client | Ventes d'œuvres, ouverture de la galerie, rachats de lieux : **suivis, jamais promis** | Région : aide au conseil, à déposer avant signature [DR] |

Les indicateurs qui dépendent de GianLuca (ventes, rendez-vous, décisions prises) sont suivis à part de ceux que Marwin contrôle (qualité, délais, coût par résultat accepté) (syn-C:796-816).

### 3.3 Ce que devient « le travail de 100 personnes »

Cent personnes représentent environ 1 750 JP par mois. Il faudrait que chaque journée de Morgan ou de Mathys produise 50 à 85 fois une journée ordinaire, contrôle compris [ES] (syn-C:769-773). Aucune pièce ne l'approche. L'ambition se mesure donc en **résultats acceptés par JP**, en **projets couverts par JP de pilotage** et en **temps humain par résultat accepté**, pas en nombre d'agents. Cibles [HY], à fixer avec GianLuca après la mesure de référence : facteur 1,3 à 1,5 sur les processus pilotés à 6 mois, 1,5 à 2 à 12 mois (syn-C:796-816).

### 3.4 Déclinaison à 90 jours, 6 mois et 12 mois

| Rubrique | 90 jours (au 2 févr. 2027) | 6 mois (au 4 mai 2027) | 12 mois (au 4 nov. 2027) |
| --- | --- | --- | --- |
| **Livrables** | Fiche de violation et décision de notification ; documents client cohérents ; décision écrite sur Medhi ; pacte et statuts ; SAS immatriculée sur engagement écrit ; message de recadrage ; cadrage livré et restitué ; démonstrateurs internes P1 et P3 sur données fictives ou internes | Pilote de 8 semaines terminé dans la voie choisie ; bilan mesuré remis à GianLuca ; exercice de sortie à blanc ; décision écrite sur le socle récurrent ; taux de référence révisé sur le coût mesuré ; au moins une proposition payante à un autre client | Socle renouvelé au moins deux fois, ou fin propre avec réversibilité ; lots réceptionnés ; une exploitation si un pilote l'a prouvé ; bilan annuel (CA, marge, temps, dépendance) ; facturation électronique en émission au 1er sept. 2027 (syn-D:77) |
| **Mesure de départ** | 0 contrat, 0 facture, 0 entité payeuse [FV] ; 0 parole directe du client [FV] ; décision du 4 nov. appliquée à 1 support sur au moins 5 [FV] (syn-C:697) ; CRM : 283 numéros sur 471 « à confirmer », 1 date de vérification, 0 appel constaté [FV] (syn-S h.1) ; disponibilités [IN] | Temps de référence relevé pendant le cadrage (P1 : temps par réunion, part des décisions avec responsable et date) ; état d'avancement des trois priorités | Coût complet réel par JP ; temps humain par résultat accepté (référence du pilote) ; part de GianLuca dans le CA |
| **Indicateurs** | Entité identifiée (oui/non) ; délai de paiement de l'acompte et du solde ; JP réelles du cadrage contre 8 estimées (écart ≤ 25 %) ; accès fournis sous 10 jours ouvrés ; 0 JP hors bon de commande ; 3 conversations qualifiées avec d'autres clients | Critères P1 tenus 4 semaines de suite ; réception au 1er ou au 2e passage ; coût complet par résultat accepté ; occupation ≤ 85 % par personne sur **tout** son temps ; 100 % des paiements à l'heure | Décisions préparées à temps ≥ 85 % ; corrections au premier passage < 20 % ; temps humain par résultat accepté −30 % sur P1 et P3 [HY] ; 0 incident critique ; part de GianLuca ≤ 80 % ou dépendance assumée par écrit |
| **Budget** [ES] | CA : 6 500 € HT (cadrage) ; sorties : 8 000 à 14 000 € apportés par les associés (statuts et pacte 2 000 à 5 000 € HT, conseil sur la fuite 1 000 à 3 000 € [HY], formalités, RC professionnelle [IN], deux mois de frais) ; aucune rémunération | CA cumulé ≈ 20 000 à 30 000 € HT si le cadrage est signé en janvier ; première rémunération au plus tôt au mois 4 | CA sur les 12 premiers mois de contrat : ≈ 50 000 / 90 000 / 150 000 € HT selon le scénario (section 6) ; net ≈ 1 350 à 1 550 € par associé en régime central |
| **Responsables** | Fuite : Mathys (titulaire présumé du dépôt) et Morgan ; documents, Medhi, relation client : Morgan ; comptes techniques : Mathys ; pacte : les deux | Comité et relation : Morgan ; outils, données, mesures, validation technique : Mathys ; contrôle à quatre yeux : l'autre associé | Les deux ; expert-comptable pour le bilan ; avocat pour les accords séparés éventuels |
| **Dépendances** | Avocat ou DPD ; expert-comptable ; greffe ; banque ; assureur ; rendez-vous avec GianLuca (aucun n'est fixé, NOTE:5) | Délégué nommé côté client ; réponses aux décisions sous 5 jours ouvrés ; préalables propres à la voie (section 4.6) | Renouvellements écrits ; prospection d'un second client |
| **Critères de réception** | Inventaire validé par écrit ; trois priorités signées ; solde du cadrage payé ; 0 mention de Medhi, BOJ.ART, STRATES, laboratoire, 750 €, 15 000 € ou de l'ancien prénom dans les documents remis | 100 % des décisions avec responsable, date et source ; compte rendu sous 24 h ouvrées dans ≥ 90 % des cas ; ≥ 80 % des comptes rendus commentés sous 3 jours ouvrés ; registre consulté chaque semaine (syn-C:695-708) ; restauration réussie dans un espace neuf | Réserve ≥ 3 mois de frais fixes et 1 mois de rémunération ; renouvellements signés ; restitution testée en 15 jours ouvrés au plus |
| **Conditions d'arrêt ou de révision** | Pas d'entité au 15 déc. 2026 ou cadrage non payé au 31 janv. 2027 : **report sans date** ; fuite non traitée : rien ne démarre ; désaccord de Mathys : aucune proposition ; apport impossible : report | Critères d'adoption non tenus 4 semaines : abandon du processus ; relecture et corrections > 50 % du temps de référence pendant 4 semaines : retour au manuel ; impayé 8 jours après relance : suspension ; occupation > 95 % deux mois : refus de tout nouveau projet | Impayés récurrents : sortie ; dépendance à 100 % sans prospect : réduire et garder d'autres revenus ; incident critique : arrêt du processus ; coût réel non couvert : relever les forfaits ou réduire le périmètre |

---

## 4. Architecture définitive des offres

### 4.0 Principes

1. **Pas d'abonnement général.** Retour à l'architecture « contrat-cadre et fiches de mission » du 30 oct. (V5 p. 2, 4), perdue le 2 nov. (syn-S:240). Chaque prestation a son bon de commande, son prix, sa réception et sa sortie.
2. **Un bon de commande par prestation et par entité.** Aucune offre n'est adressée « à Carlone » en général : elle nomme l'entité, le signataire, le payeur et le valideur (syn-P:306).
3. **Le prix est fixé au livrable ou au périmètre.** Le temps sert à mesurer, pas à vendre. Le relevé des JP est remis chaque mois comme preuve.
4. **Marwin prépare, organise et coordonne ; elle n'exécute pas** l'administratif courant, la comptabilité, le conseil juridique ou fiscal, ni les obligations d'exploitant, d'organisateur ou de vendeur (syn-D:410-431).
5. **Marwin n'avance jamais d'argent pour le client.** Achats, abonnements et prestataires sont commandés et payés par l'entité cliente, à son nom.
6. **Les comptes et outils du client sont ouverts à son nom dès le premier jour** ; Marwin y intervient comme collaborateur (syn-D:512).
7. **Rien d'exploratoire sans financeur écrit**, budget plafonné et critère d'arrêt (section 9).

### 4.1 Vue d'ensemble

| Code | Offre | Nature du prix | Capacité [ES] | Durée | Prix proposé [PR] | TTC (TVA 20 %) |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Remise en ordre | Non facturée | 9 à 17 JP sur les mois 0 à 2 | Novembre 2026 | 0 € | — |
| A | Cadrage « inventaire, priorités, mandat » | Forfait | 8 JP | 3 à 4 semaines | **6 500 € HT** (version réduite : 4 800 € HT pour 6 JP) | 7 800 € |
| B0 | Socle pilote (pilotage, 8 semaines) | Mensuel d'avance | 3 à 4 JP par mois | 2 mois, sans reconduction tacite | **3 500 € HT par mois** | 4 200 € |
| B1 | Socle récurrent « socle + 2 projets actifs » | Mensuel d'avance | 4,5 à 5,5 JP par mois | 3 mois renouvelables | **4 500 € HT par mois** ; + 1 200 € HT par projet actif en plus | 5 400 € |
| B2 | Socle récurrent « socle + 4 projets actifs » | Mensuel d'avance | 6,5 à 9 JP par mois | 3 mois renouvelables, sous conditions | **6 900 € HT par mois** | 8 280 € |
| C | Lots devisés (dont C2 pilote commercial et C6 outillage et passation) | Forfait par lot | 3 à 9 JP par lot | Selon le lot | JP estimées × 800 € + 10 à 15 % ; C2 : **6 000 € HT** ; C6 : **7 500 € HT** | 7 200 € ; 9 000 € |
| D | Exploitation d'un processus prouvé | Minimum mensuel + prix par résultat accepté | 1 à 4 JP par mois | 6 mois renouvelables | 1 000 à 1 500 € HT par mois + variable fixé après mesure | — |
| E | Avenant de capacité et urgences | Au temps, sur bon écrit préalable | Résiduelle | — | **900 € HT par JP**, demi-journée minimale | 1 080 € |

### 4.2 Offre 0 : remise en ordre (interne, non facturée)

| Rubrique | Contenu |
| --- | --- |
| **Client** | Aucun : obligation de Marwin et de ses associés |
| **Problème** | Fuite de données probable ; documents client contradictoires avec la décision du 4 nov. ; structure, pacte et disponibilités non écrits ; travail gratuit qui s'accumule (scénario S5, syn-P:304) |
| **Résultat** | (1) **Fuite** : décision sur la notification à la CNIL prise **avant l'échéance du 5 nov.** avec un avocat ou un DPD ; si le dossier est incomplet, notification échelonnée [HY, à confirmer par le conseil] ou notification en retard motivée (syn-D:623 ; J2:155) ; dépôt rendu privé et vérifié ; copies (forks) contrôlées ; secrets révoqués ; fiche de violation ; décision sur l'information des personnes (art. 34) ; GianLuca informé par écrit, dans des termes validés par le conseil (J1:192). (2) **Documents** : une seule version de l'offre ; PR n° 1 fermée ou son PDF marqué « historique » ; offre écrite, STRATES v1.1, vernissage et diapositive laboratoire marqués « retirés » ; diaporama corrigé selon la liste de la section 17.4 ; aucune occurrence de l'ancien prénom dans un document client ; V5 jamais transmis. (3) **CRM** : hébergement privé ; oppositions appliquées ; simulateur fiscal corrigé ou retiré (`crm/art_merge.py:19, 129` : taux d'IS fixe de 25 %, sans le bénéfice ni le taux PME ; jusqu'à 1 043 750 € affichés pour une entreprise) (J2:115 ; syn-S h.1). (4) **Medhi** : décision écrite de Morgan et Mathys sur la portée du retrait ; message écrit à Medhi. (5) **Associés** : fiche des disponibilités nominatives ; principes du pacte ; statuts et pacte prêts à signer. (6) Vérification qu'aucun document de Marwin ou de Carlone ne reste dans le dépôt public BOJART (S1:154). (7) Message de recadrage d'une page (section 17.3) |
| **Exclusions** | Toute nouvelle production pour GianLuca |
| **Capacité** | 9 à 17 JP sur les mois 0 à 2, dont 3 à 6 pour la fuite et la conformité minimale [ES] (syn-C:212-222) |
| **Coût** | Temps non rémunéré ; sorties d'argent : conseil sur la fuite 1 000 à 3 000 € [HY], statuts et pacte 2 000 à 5 000 € HT [ES], formalités quelques centaines d'euros, RC professionnelle [IN] |
| **Facturation** | **Aucune.** L'exposition des données est de notre fait (syn-P:115) |
| **Réception** | Dépôt privé vérifié ; fiche de violation ouverte ; décision datée et motivée ; documents conformes à la liste de la section 17.4 |
| **Condition de sortie** | Toutes les conditions de la section 10, sauf l'acompte |

### 4.3 Offre A : cadrage « inventaire, priorités, mandat »

| Rubrique | Contenu |
| --- | --- |
| **Client** | L'entité de GianLuca désignée comme chef de file (dénomination, SIREN, signataire habilité, effectif). Payeur et valideur : la même entité, ou celles qu'elle désigne par écrit |
| **Problème** | Le portefeuille n'est connu qu'à travers Morgan [DR] (syn-S:38). Aucune liste d'entités, de lieux, de priorités, de budgets ni d'accès. Marwin ne peut ni dimensionner ni chiffrer ; GianLuca ne peut pas comparer |
| **Résultat** | 1. Inventaire **validé par écrit** des entités, lieux, projets, interlocuteurs et accès. 2. Trois priorités à 90 jours choisies par GianLuca, chacune avec un objectif mesurable, un budget indicatif, un responsable côté client, **le coût actuel estimé avec lui et le seuil au-delà duquel un lot se rentabilise pour lui** (J1:191). 3. Carte des rôles par projet : exploitant, organisateur, vendeur, responsable du traitement ; professionnels à consulter. 4. Grille de délégation et projet de mandat par entité (actes, plafonds, délégué). 5. Décision écrite sur le CRM : exploiter ou non, au nom de quelle structure, qui appelle (S3:170). 6. Canal de travail réel de GianLuca et personnes qui utiliseront les outils (J1:190). 7. Registre des décisions ouvert **sur un compte au nom de l'entité** et mesure de référence du pilote P1 (S2:173). 8. Comparaison chiffrée des trois suites possibles (section 4.4), avec le coût d'un coordinateur salarié |
| **Périmètre** | Deux entretiens (2 à 3 h sur place, puis une restitution d'1 h 30) ; jusqu'à 15 pièces fournies ; un aller-retour de corrections ; un associé mène, l'autre contrôle |
| **Exclusions** | Conseil juridique ou fiscal ; étude détaillée de rentabilité d'un établissement ; tout contact avec des tiers ; usage du CRM sur des données réelles ; production de supports, de catalogue ou d'outils ; visites de plus d'une journée |
| **Dépendances** | Offre 0 terminée ; Marwin immatriculée ; entité identifiée et bon de commande signé ; acompte encaissé ; pièces et accès fournis sous 10 jours ouvrés ; deux entretiens tenus |
| **Capacité** | 8 JP [ES] : préparation 1 ; entretien et trajet 1,5 ; analyse et inventaire 2 ; carte des rôles 1 ; priorités, mandat et comparaison 1,5 ; restitution 0,5 ; contrôle et corrections 1 (S1:170). Morgan 5, Mathys 3 (S2:176) |
| **Durée** | 3 à 4 semaines à partir de l'acompte et des pièces ; congés de fin d'année non comptés |
| **Prix proposé** | **6 500 € HT forfaitaires** (7 800 € TTC), deux trajets compris. **Plancher** : 6 000 € HT pour ce périmètre (8 × 750 €). En dessous, on vend la **version réduite** (6 JP : inventaire et trois priorités, sans grille de délégation ni mesure de référence) à **4 800 € HT**. Si GianLuca a déjà vu le taux de 750 € [IN], on peut accepter 6 000 € HT en l'expliquant |
| **Justification** | *Coût* : 8 JP × 591 à 737 € = 4 700 à 5 900 € au coût central [ES] (verif § 1). *Marché* : un cadrage court au forfait est le format que le marché soutient (rj-R6 (e)) ; ≈ 810 € par JP, dans le haut de la fourchette d'un chef de projet senior en région (570 à 760 € [ES]) et sous les repères de direction à temps partagé (800 à 1 200 € [DR]) (S1:135-146). Le Diag Data IA **ne sert pas** de justification (C1). *Valeur* : GianLuca évite d'engager 90 000 € HT à l'aveugle et garde l'inventaire, la carte des rôles et les priorités, même s'il s'arrête là |
| **Coûts directs** | Déplacements [IN] (lieu de résidence des associés inconnu) ; outils négligeables |
| **Marge** [ES] | 9 à 27 % au coût central (12 JP) ; −9 à +13 % si la capacité facturée reste à 10 JP (verif § 8). **Volontairement faible : c'est un test du besoin, vendu une seule fois** |
| **Réception** | Remise du dossier, puis restitution. Réception **expresse** demandée sur les livrables 1, 2 et 4. Réserves motivées par écrit sous 10 jours ouvrés, corrigées une fois. Sans réserve motivée, le solde devient exigible au plus tard 30 jours après la remise : c'est une livraison pour la facturation, **jamais** une approbation d'une suite ni d'une dépense |
| **Paiement** | 50 % à la commande (le travail démarre à l'encaissement) ; 50 % à la réception, payable sous 8 jours |
| **Conditions de poursuite** | Cadrage payé à l'échéance ; inventaire validé par écrit ; au moins une priorité confiée avec un budget ; accès réellement fournis ; demande écrite d'une suite dans les 30 jours ; occupation ≤ 85 %. À défaut : arrêt propre, GianLuca garde le dossier |

**Aide régionale au conseil.** Elle couvrirait 50 % jusqu'à 15 000 € sur deux ans, à condition de **déposer le dossier avant la signature** [DR] (syn-P:252). Son échéance est annoncée au **31 décembre 2026**, « dans la limite des crédits » [DR] (syn-D:71). L'éligibilité d'un prestataire nouveau est [IN]. La question se pose dès le premier contact. On ne retarde pas le cadrage pour une aide incertaine (J1:187).

### 4.4 Après le cadrage : trois voies, une seule à la fois

GianLuca choisit la suite sur pièces, après la restitution (J1:211). Chaque voie est un pilote de huit semaines au plus, sans tacite reconduction, avec une mesure de référence et des critères d'adoption et d'abandon fixés **avant** l'essai.

| Voie | Pour quel besoin rapporté | Offres | Prix total [PR] | Préalables |
| --- | --- | --- | --- | --- |
| **(a) Ventes d'œuvres** | Vendre des œuvres aux entreprises de la Nièvre [DR] (COP:13) | C2 pilote commercial sur 20 comptes | 6 000 € HT | Section 4.6, C2 |
| **(b) Pilotage** | Disposer d'une équipe qui relie les sujets et prépare les décisions [DR] (ACC:13) | B0 socle pilote (2 mois) et un lot C (C1 ou C4 d'abord) | ≈ 7 000 € HT + 3 500 à 6 500 € HT | Délégué nommé ; décisions sous 5 jours ouvrés |
| **(c) Organisation interne** | « Ne pas gérer chaque détail », sans payer d'exécution à 800 € par JP (S3:205) | C6 outillage et passation (avec aide au recrutement) | 7 500 € HT | Décision de désigner ou de recruter une personne |

Le registre des décisions de la voie (b) peut accompagner les voies (a) et (c) seulement si GianLuca le commande en plus. Le passage à une deuxième voie suppose la réception de la première.

### 4.5 Offre B : socle de pilotage (B0 pilote, puis B1 ou B2 récurrent)

**Contenu du socle, liste fermée** [PR] (S2:189-197 ; S3:224) :
- un point hebdomadaire de 1 h 30 avec **un seul associé**, sauf décision qui demande les deux ;
- un compte rendu sous 24 h ouvrées ;
- un registre des décisions et des échéances, et un tableau de bord mis à jour chaque semaine, sur un compte de l'entité ;
- un comité mensuel avec rapport : capacité consommée, livrables, décisions attendues, risques, indicateurs ;
- deux à quatre dossiers de décision par mois au plus (comparaison de devis, rentabilité simple) ;
- la coordination, sous mandat, des prestataires et professionnels du client, **sans commandement direct de leurs salariés** ;
- un suivi budgétaire préparatoire par projet, remis à l'expert-comptable du client ;
- la veille des échéances réglementaires listées au cadrage ;
- les sauvegardes, la restauration testée, le journal et la réversibilité des outils du socle.

| Rubrique | B0 socle pilote | B1 « socle + 2 projets actifs » | B2 « socle + 4 projets actifs » |
| --- | --- | --- | --- |
| **Client** | Entité chef de file ; fiche de mission par entité si plusieurs | Idem ; capacité répartie par entité, pour qu'aucune ne consomme le temps payé par une autre (S2:209) | Idem |
| **Problème** | Savoir, avant tout engagement récurrent, si un pilotage délégué fonctionne vraiment | Garder une vision claire du portefeuille et des décisions préparées, sans gérer chaque détail [DR] (ACC:13) | Idem, sur un portefeuille plus large et prouvé |
| **Résultat** | Socle ci-dessus sur les trois priorités du cadrage ; mesure de l'adoption | Socle sur 2 projets actifs nommés et 1 en veille | Socle sur 4 projets actifs et 2 en veille |
| **Exclusions** | Toute production (lots C) ; exécution administrative ; astreinte ; tout engagement de dépense (mandat à 0 €) ; données personnelles réelles sans les préalables | Production ; urgences hors plages ; exécution administrative ; dépenses hors mandat ; obligations réglementées ; recherche | Idem |
| **Dépendances** | Cadrage reçu ; délégué ; réponses sous 5 jours ouvrés ; accès | Pilote réussi ; mandat écrit par entité ; accès maintenus | Trois mois de B1 aux critères ; gains mesurés sur P1 et P3 ; disponibilités nominatives écrites ; occupation de chaque associé < 85 % pendant trois mois, sur tout son temps (J2:177-181) |
| **Capacité** [ES] | 3 à 4 JP par mois | 4,5 à 5,5 JP par mois (socle 2,5 à 3 JP + 1 à 1,5 JP par projet actif, syn-C:242-256) | 6,5 à 9 JP par mois |
| **Durée** | 8 semaines, sans tacite reconduction | 3 mois, renouvelables par accord écrit ; préavis réciproque d'un mois la première année, deux mois ensuite | Idem |
| **Prix proposé** | **3 500 € HT par mois** ; plancher 3 000 € | **4 500 € HT par mois** ; + **1 200 € HT** par projet actif en plus ; plancher 750 € par JP de capacité de référence | **6 900 € HT par mois** |
| **Justification** | Coût 3,5 JP × 591-737 € ≈ 2 070 à 2 580 € ; temps partagé vendu 2 à 8 jours par mois (rj-R6 (e)) | 818 à 1 000 € par JP de référence (verif § 4) ; le prix rémunère un périmètre et une responsabilité (binôme de secours, journal, restauration, réversibilité), pas des heures | 767 à 1 062 € par JP ; **au-delà de 6 à 8 JP stables, un coordinateur salarié coûte moins cher au client** : B2 n'est proposé qu'avec cette comparaison, et avec l'offre C6 en alternative |
| **Coûts directs** | Deux sièges d'IA professionnels et un espace de registre : ≈ 60 à 90 $ par mois [ES] (syn-C:705) ; déplacements [IN] | ≈ 60 à 150 € par mois ; outils du client à sa charge | Idem |
| **Marge** [ES] | 16 à 49 % (12 JP) ; −1 à 39 % (10 JP) | 10 à 41 % (12 JP) ; −8 à 29 % (10 JP) | 4 à 44 % (12 JP) ; −15 à 33 % (10 JP) (verif § 8) |
| **Réception** | Critères P1 (syn-C:695-708) : 100 % des décisions avec responsable, date et source ; compte rendu sous 24 h ouvrées dans ≥ 90 % des cas ; ≥ 80 % des comptes rendus commentés sous 3 jours ouvrés ; registre consulté chaque semaine | Rapport mensuel au 5e jour ouvré ; engagements de service : comptes rendus, registre, tableau de bord ; **malus de 5 %** en avoir sur la facture suivante si deux engagements sont manqués dans le mois (S2:221) | Idem ; décisions préparées à temps ≥ 85 % |
| **Paiement** | D'avance ; premier mois à la signature | D'avance, le 1er du mois | Idem |
| **Conditions de poursuite** | Critères d'adoption tenus 4 semaines ; aucune erreur critique ; paiements à l'heure ; demande écrite de poursuivre. **Abandon** : relecture et corrections > 50 % du temps de référence pendant 4 semaines, ou registre non consulté après 4 semaines | Bilan au 3e mois (maintien, passage à B2, réduction) ; **sortie à blanc** au 6e mois ; changement de palier sans pénalité si un associé est indisponible plus de 10 jours ouvrés | Idem ; B3 (6 projets) n'est pas ouvert la première année |

**Règles propres au socle.** Une demande nouvelle remplace un projet actif ou devient un lot (limite d'encours). La capacité non consommée se reporte d'au plus 20 %, pour du pilotage seulement. Elle ne se convertit jamais en production.

### 4.6 Offre C : lots de production devisés

**Règle de devis [PR].** Prix = JP estimées × 800 € HT + provision de risque de 10 à 15 %, au forfait. **Plancher absolu : 750 € HT par JP estimée**, aléas compris (C13). Chaque lot a son bon de commande, ses critères de réception écrits **avant** le démarrage, ses exclusions et le régime des droits : cession des développements propres au client au paiement complet ; licence gratuite, non exclusive et perpétuelle sur les composants génériques de Marwin (syn-D:486-514). Tout dépassement non causé par le client reste à la charge de Marwin dans la limite de la provision ; au-delà, un avenant signé **avant** le travail. **Paiement** : 40 % à la commande, 60 % à la livraison ; au-delà de 8 JP, 40 / 30 / 30 avec un jalon intermédiaire écrit. **Réception en deux temps** (J1:193) : la **livraison** des livrables de Marwin déclenche le paiement du solde ; l'**adoption** (usage par les équipes du client, appels passés) décide de la suite et ne conditionne pas le paiement.

| Lot | Résultat | JP [ES] | Prix indicatif HT [PR] | Préalables | Exclusions |
| --- | --- | --- | --- | --- | --- |
| **C1** Catalogue privé des œuvres (20 à 30 œuvres réelles) | Fiches complètes et exportables : photo, provenance, emplacement, mouvements | 4 à 7 | 3 500 à 6 400 € | Œuvres réelles, photos, provenance et autorisations de reproduction fournies | Expertise, authentification, photographie professionnelle (payée par le client), valorisation fiscale |
| **C2** Pilote commercial sur 20 comptes | Voir la fiche ci-dessous | 6 à 7 | **6 000 €** | Voir la fiche | Voir la fiche |
| **C3** Faisabilité d'un premier événement **sans robot** | Lieu, date, jauge, organisateur désigné, autorisations avec dates de dépôt (GN 6 au moins deux mois avant), budget, devis | 4 à 6 | 3 500 à 5 500 € | Lieu et organisateur identifiés ; aucun événement public en décembre 2026 dans un lieu non autorisé [ES] (syn-D:533) | L'organisation elle-même ; la sécurité du public ; le format « signature » avec bras |
| **C4** Tableau des lieux et de leurs obligations | Par lieu : propriétaire, exploitant, licences, classement ERP, calendrier des démarches, à valider par les professionnels | 3 à 5 | 2 700 à 4 600 € | Inventaire du cadrage validé | Le rôle d'exploitant ; toute démarche au nom du client sans mandat |
| **C5** Échange de fichiers avec Quali Contact | Spécification dans les deux sens ; essai sur 10 fiches fictives ; correspondance des champs validée par Quali Contact | 3 à 4 | 2 700 à 3 700 € | Contrat entre l'entité de GianLuca et Quali Contact ; logiciel et format connus | Tout développement avant de connaître le format |
| **C6** Outillage et passation, avec aide au recrutement | Voir la fiche ci-dessous | 8 à 9 | **7 500 €** | Voir la fiche | Voir la fiche |
| **C7** Étude de rentabilité d'un rachat ou de travaux | Budget, seuil, trois scénarios | 3 à 5 | 2 700 à 4 600 € | Données du vendeur ou devis | Conseil fiscal ; évaluation immobilière réglementée |
| **C8** Kit de campagne et supports commerciaux | Script, e-mail, fiche d'offre, grille de conformité | 3 à 5 | 2 700 à 4 600 € | Pilote C2 concluant ; mentions fiscales validées par le conseil du client | Toute promesse fiscale non validée ; le mot « mécénat » pour vendre une œuvre (syn-D:56) |

**Ordre recommandé** dans la voie (b) : C1 ou C4 d'abord (concrets, peu risqués, sans données de prospects) ; C5 seulement si Quali Contact est engagé.

#### Fiche C2 : pilote commercial sur 20 comptes

| Rubrique | Contenu |
| --- | --- |
| **Client** | La structure qui vend les œuvres, nommée dans chaque message (U11, syn-S) ; elle est aussi responsable du traitement |
| **Problème** | GianLuca veut vendre des œuvres aux entreprises de la Nièvre [DR] (COP:13). Le fichier existe mais n'est ni fiable (283 numéros sur 471 à confirmer), ni conforme, ni utilisé [FV]. On ignore si la cible achète |
| **Résultat** | 20 comptes qualifiés (source et date pour chaque champ) ; script et e-mail validés par le conseil de GianLuca ; outil de réimport des résultats d'appel ; rapport mesuré (joignabilité, rendez-vous, refus, oppositions, temps humain par fiche) [MM à produire] ; recommandation d'extension ou d'arrêt |
| **Périmètre** | 2 semaines de préparation ; appui pendant 4 semaines d'appels (réimport hebdomadaire, ajustement du script) ; bilan. Comptes tirés des 37 cibles et des 57 fiches de priorité haute (syn-S h.1) |
| **Exclusions** | Les appels et les rendez-vous eux-mêmes ; la vente ; toute commission ; tout encaissement ; le conseil fiscal ; tout agent vocal sortant ; tout connecteur Quali Contact sans modèle de fichier réel |
| **Préalables, tous requis** | Offre 0 terminée ; responsable du traitement désigné et contrat de l'article 28 signé ; **décision sur l'information des personnes (art. 34)** et comptes choisis **hors des fiches exposées** si cette information est due (J2:156) ; entreprises seulement, ni entrepreneurs individuels ni lignes personnelles avant l'avis de l'avocat ; structure vendeuse nommée ; **5 à 10 œuvres réellement disponibles**, avec prix et artiste vivant ; avis fiscal écrit (238 bis AB valable pour les achats faits avant le 31 déc. 2028 [FV] ; pièces faites à la machine et exposition chez le vendeur non validées [HY], syn-D:56) ; appelant désigné (GianLuca, un assistant ou Quali Contact, qui facture directement l'entité) ; seuils de poursuite fixés **avec** GianLuca avant l'essai |
| **Capacité** | 6 à 7 JP : Mathys 4 (données, outil, réimport), Morgan 2 à 3 (kit, bilan) [ES] |
| **Durée** | 6 à 8 semaines |
| **Prix** | **6 000 € HT** (≈ 860 à 1 000 € par JP) ; plancher 5 250 € HT (7 JP × 750 €) |
| **Justification** | *Coût* : 6 à 7 JP × 591-737 € ≈ 3 550 à 5 150 €. *Marché* : un téléprospecteur externalisé coûte 3 000 à 8 000 € par mois [DR] ; ici, Marwin ne fournit pas les appels. *Valeur* : une seule vente d'œuvre à une entreprise peut dépasser ce montant [HY] |
| **Coûts directs** | API de recherche : 10 à 50 € ; téléphonie à la charge du client |
| **Marge** [ES] | 14 à 41 % (12 JP) ; −3 à +29 % (10 JP) (verif § 11) |
| **Réception** | *Livraison* (déclenche le solde) : fiches sourcées et datées à au moins 90 % ; 100 % des numéros partagés signalés ; 100 % des oppositions respectées ; kit validé ; outil de réimport testé. *Mesure* (décide de la suite, ne conditionne pas le paiement) : résultats d'au moins 90 % des appels réimportés. Si les appels n'ont pas commencé 15 jours ouvrés après la livraison, la mesure devient un lot optionnel |
| **Conditions de poursuite** | Seuils fixés d'avance (repère [HY] : joignabilité ≥ 50 % et quelques rendez-vous tenus). Atteints : extension par vagues de 50 à 100 comptes (lot de 4 000 à 6 000 € HT). Non atteints : changer de source ou de cible, ou arrêter. Les ventes sont suivies à part : elles dépendent de GianLuca et des œuvres |

#### Fiche C6 : outillage et passation, avec aide au recrutement

| Rubrique | Contenu |
| --- | --- |
| **Client** | L'entité de GianLuca qui emploiera la personne, ou qui désigne un salarié existant |
| **Problème** | « Ne pas gérer chaque détail » [DR] (ACC:13), sans payer d'exécution administrative à 800 € par JP. Un assistant non cadre coûte 2 249 à 2 808 € par mois à l'employeur [MM] (ver-R6 n° 3), soit environ 125 à 157 € par jour travaillé [ES] |
| **Résultat** | Registre des décisions et des échéances ; tableau de bord ; modèles d'ordre du jour et de compte rendu ; 5 à 8 procédures écrites pour les tâches récurrentes repérées au cadrage, chacune avec sa fiche de secours manuel ; tous les comptes ouverts **au nom de l'entité** ; fiche de poste et grille d'entretien ; deux séances de formation ; un test de restauration ; exports remis |
| **Périmètre** | Processus « réunions », « échéances » et « capitalisation » (syn-C:652-666), avec l'option « organisation simple » ou « outils existants configurés » seulement |
| **Exclusions** | Le recrutement lui-même (sélection, contrat de travail, paie) ; **tout outil d'IA dans le recrutement** (haut risque, syn-D:665) ; l'exécution des tâches ; la comptabilité ; tout développement spécifique ; le nom « Jarvis » |
| **Dépendances** | Décision de GianLuca de recruter ou de désigner une personne ; accès ; offres d'IA professionnelles avec clauses contractuelles types et analyse d'impact des transferts si des données personnelles sont traitées (syn-D:667-681) |
| **Capacité** | 8 à 9 JP : Mathys 5 (outils, comptes, restauration), Morgan 3 à 4 (procédures, formation, fiche de poste) [ES] |
| **Durée** | 4 à 6 semaines, puis 30 jours d'accompagnement compris |
| **Prix** | **7 500 € HT** (≈ 830 à 940 € par JP) ; plancher 6 750 € |
| **Justification** | *Valeur* : GianLuca paie ensuite l'exécution au coût d'un assistant (≈ 27 000 à 34 000 € par an [ES]) et non au prix d'une prestation ; *coût* : 8 à 9 JP × 591-737 € ≈ 4 700 à 6 650 € |
| **Marge** [ES] | ≈ 11 à 37 % (12 JP) ; ≈ −6 à +24 % (10 JP) (verif § 11) |
| **Réception** | *Livraison* (déclenche le solde) : outils en service sur les comptes du client, procédures et fiches de secours remises, deux formations tenues, restauration réussie, exports remis. *Adoption* (décide de la suite) : la personne désignée utilise le registre quatre semaines de suite et traite au moins 80 % des comptes rendus. Si personne n'est désigné 15 jours ouvrés après la livraison, la livraison est prononcée et la mesure d'adoption devient un lot optionnel (J1:108) |
| **Conditions de poursuite** | Si personne n'est désigné, Marwin **ne reprend pas** l'exécution ; le socle éventuel reste limité au pilotage (S3:216) |

### 4.7 Offre D : exploitation d'un processus prouvé (au plus tôt au mois 7)

| Rubrique | Contenu |
| --- | --- |
| **Exemples** | Tenue et qualification du CRM (fiches à jour, résultats réimportés, oppositions appliquées, export et sauvegarde testés) ; recherche documentaire avec citations sur le corpus du client (pilote P3) ; rapprochement budgétaire mensuel (calcul par formule, jamais par le modèle de langage) |
| **Condition d'entrée** | Un pilote réussi (critères tenus 4 semaines), puis 2 à 3 mois de critères tenus ; reprise manuelle et restauration testées ; responsable et maintenance chiffrés au contrat (syn-C:676-693) |
| **Résultat** | Un service régulier avec des niveaux de qualité écrits et un mode manuel testé |
| **Capacité** | 1 à 4 JP par mois [ES] |
| **Prix** | Minimum de **1 000 à 1 500 € HT par mois** (maintenance, sauvegardes, journal) **plus un prix par résultat accepté**, fixé après la mesure de référence et **jamais sous le coût manuel mesuré** (C20) ; figé 6 mois |
| **Paiement** | Minimum d'avance ; variable en fin de mois sur relevé, sous 15 jours |
| **Conditions** | Critères tenus ; aucun incident critique ; coût par résultat accepté connu ; maintenance ≤ 0,5 JP par mois et par processus (S2:583) |

### 4.8 Offre E : avenant de capacité, urgences et astreinte

- **Avenant de capacité** : 900 € HT par JP, en heures ouvrées, sur bon écrit du valideur **avant** le travail ; demi-journée minimale [PR] (S2:292).
- **Urgences** : liste fermée (incident de données ou de sécurité, échéance légale à moins de 48 h). L'arrêt d'un processus se fait sans autorisation ; tout travail en plus passe par un avenant.
- **Astreinte** : aucune par défaut, jamais 24 h sur 24 ni 30 jours sur 30 (ACC:105). Sur demande seulement, un forfait chiffré à part, avec des relais nommés.

### 4.9 Justification d'ensemble des prix

**Coût complet d'une JP facturable** [ES] (verif § 1). Méthode de S1 : (rémunération chargée des associés au prorata de leur temps pour Marwin + frais fixes) ÷ JP facturables ÷ 0,9. SAS, coefficient coût/net de 1,7 à 1,9 [HY] (syn-D:98), 2 500 € nets par équivalent temps plein (plancher d'OFF:112-114), frais fixes de 1 500 à 2 500 € par mois [HY].

| Disponibilité | JP facturables par mois | Coût complet par JP |
| --- | --- | --- |
| Prudent : Morgan 50 %, Mathys 25 % | ≈ 7 | ≈ 744 à 962 € |
| Central : Morgan 65 %, Mathys 50 %, capacité pleine | ≈ 12 | ≈ 591 à 737 € |
| Central, capacité engagée plafonnée la première année | 10 | ≈ 710 à 885 € |
| Haut : 90 % chacun | ≈ 20 | ≈ 508 à 614 € |

**Repères de marché** (aucun organisme officiel ne publie de prix de conseil) : chef de projet senior en région ≈ 570 à 760 € HT par jour [ES] ; moyenne « gestion de projets » des freelances tech 698 € [FV, étude privée Kicklox] ; DAF à temps partagé 800 à 1 200 € et management de transition ≈ 1 330 € par jour [DR, sources secondaires] ; format courant du temps partagé : 2 à 8 jours par mois [HY] (S1:135-146 ; ver-R6 n° 5).

**Comparaison avec un salarié, à présenter au client** (S3:95-103, corrigée) [ES] :

| Formule | Coût mensuel pour son entité |
| --- | --- |
| Offre des archives, base | 15 000 € HT (OFF:13) |
| Socle B1 + assistant non cadre salarié | 4 500 € HT + 2 249 à 2 808 € [MM] ≈ 6 750 à 7 300 € par mois, plus des lots ponctuels |
| Chef de projet cadre salarié en région | 5 380 à 6 149 € de coût employeur [MM] (ver-R6 n° 3) |

**Conséquence.** Pour un besoin **stable** d'environ 6 à 8 JP par mois ou plus, un coordinateur salarié coûte moins cher que Marwin (C2). L'offre durable de Marwin vend donc le pilotage et la préparation des décisions, l'outillage, la responsabilité (sauvegardes, réversibilité, contrôle à quatre yeux) et la passation, **pas un volume de journées** (J2:202). Le recrutement a des coûts cachés (sélection, encadrement, risque) que l'audit n'a pas chiffrés [IN].

### 4.10 Règle anti-double facturation

1. **Une tâche, une ligne.** Chaque JP est imputée à un seul bon de commande (cadrage, socle, lot, exploitation, avenant), avec un code visible dans le relevé mensuel remis au client.
2. **Le socle ne produit pas, la production ne pilote pas.** Un lot ne s'exécute pas sur le temps du socle ; le socle n'absorbe pas un dépassement de lot ; la capacité du socle ne se convertit jamais en production.
3. **Un outil construit dans un lot n'est jamais refacturé.** Sa maintenance n'est facturée que si une exploitation (offre D) la prévoit. Les défauts de Marwin sont corrigés gratuitement pendant 60 jours après la réception (S3:293).
4. **Le CRM déjà construit** n'est facturé ni rétroactivement ni dans un lot. Son régime (licence gratuite ou cession) est écrit avant tout lot CRM, une fois la propriété réglée entre Morgan et Mathys (syn-D:494).
5. **Jamais facturés** : la remise en ordre, la mise en conformité des données, la correction de nos erreurs, nos outils internes, notre administration, notre prospection.
6. **Outils et achats** : au nom du client et payés par lui, sans marge. Les débours ne sont refacturés que s'ils remplissent les quatre conditions du BOFiP (BOI-TVA-BASE-10-10-30, § 200) [FV] (syn-D:431).
7. **Tiers** : Quali Contact, l'expert-comptable, l'avocat, le photographe et les artistes facturent directement l'entité de GianLuca (S3:296).
8. **Deux associés en réunion** : deux JP seulement si le bon de commande le prévoit.
9. **Malus et refus** : un avoir sur la même commande, jamais du travail gratuit sur une autre.
10. **Aucun dépassement sans avenant signé avant le travail.** C'est la traduction opérationnelle de la promesse déjà affichée « Aucun travail facturé deux fois » [FV] (deck/slides/garanties.html:38).

### 4.11 Sort du taux de 750 € HT

- **Il disparaît du discours client.** On retire « Taux unique : 750 € HT la journée-personne » [FV] (deck/slides/formules.html:30) et « On ajuste le périmètre et le nombre de jours, pas le taux » [FV] (OFF:18). Le client voit des forfaits et des périmètres.
- **Il devient le plancher interne de chiffrage**, jamais remisé, ni contre un volume ni contre une promesse d'investissement (OFF:149). En dessous, on réduit le périmètre ou on refuse.
- **Le prix cible interne est de 800 à 950 € par JP estimée**, aléas compris (J2:191). Raison : à 10 JP facturés, le coût complet pour 2 500 € nets par ETP est de 710 à 885 € (C16).
- **Sa justification est d'abord le coût** : il couvre le coût central à pleine capacité (591 à 737 €) avec une rémunération modeste. Il se situe dans le haut de la fourchette d'un chef de projet senior en région et sous les repères de direction à temps partagé [ES/DR].
- **Il ne s'applique pas à l'exécution** : l'administratif (125 à 157 € par jour pour un assistant salarié) est exclu ; le développement (405 à 585 € en région [ES]) est vendu au livrable.
- **Il est révisé au mois 6** sur le coût complet mesuré.
- **Exception** : si GianLuca a déjà vu ce taux [IN], on l'applique au seul cadrage (6 000 € HT) et on explique le passage au forfait.

### 4.12 Sort des formules de 15 000 et 30 000 € HT, de l'acompte de 7 500 € et des options

| Élément des archives | Décision | Raison | Retour possible |
| --- | --- | --- | --- |
| Formule de base : 20 JP, 15 000 € HT par mois, « environ un mi-temps » (OFF:13-15) | **Retirée** comme offre d'entrée | 78 à 83 % du temps disponible des deux associés, pas un mi-temps (syn-C:228) ; aucune demande tracée (syn-S:235) | Jamais comme abonnement global. Un chiffre d'affaires de cet ordre ne revient que dans le scénario ambitieux, comme **somme** d'un socle, de lots et d'une exploitation, après un pilote réussi, avec une sous-traitance financée |
| Renforcement : 40 JP, 30 000 € HT par mois | **Retiré** de toute présentation | 140 à 145 % du temps disponible (syn-C:229) | Seulement avec un recrutement financé par un contrat renouvelé (syn-C:309) |
| « Ancre » de 46 JP (OFF:246) | **Retirée** | Au-delà même du plafond théorique de 35 JP bruts | Non |
| Acompte de 7 500 € HT, six mois d'engagement | **Retirés** | Ils accompagnaient la formule de six mois | Remplacés par le calendrier de la section 5 |
| Option laboratoire, 30 000 € HT dont 13 500 € d'honoraires | **Retirée** du diaporama | Plus d'objet depuis le retrait de STRATES (OFF:84) ; aucun financement acté | Section 9 |
| Option création avec Medhi et STRATES (≈ 10 000 € HT) | **Retirée** | Décision du 4 nov. [DR] | Section 9 |

### 4.13 Rémunérer la responsabilité et la valeur quand l'automatisation réduit le temps

La règle du 29 oct. (« Les économies issues de l'automatisation permettent de réaffecter la capacité ou de revoir le forfait », ACC:66) a disparu le 2 nov. alors que la facturation restait au temps (syn-S:266). Dans un modèle au temps, chaque gain réduit le chiffre d'affaires. Règles retenues [PR] :

1. **Prix au livrable, au périmètre ou au résultat accepté**, fixé pour la période contractuelle à partir d'une référence mesurée **avant** l'automatisation. Le gain obtenu pendant la période revient à Marwin.
2. **Le socle paie une responsabilité, pas des heures** : binôme de secours, journal, sauvegarde et restauration testées, bouton d'arrêt, réversibilité. Il ne baisse pas pendant le contrat si le temps baisse ; le temps libéré peut absorber un projet de plus, sur proposition de Marwin.
3. **Partage visible au renouvellement** : la première année, les gains restent à Marwin ; ensuite, un tiers du gain mesuré revient au client (baisse du prix unitaire ou volume en plus), calcul remis avec le rapport (S2:252-256).
4. **Prime sur économie réelle, en option à 12 mois** : si une automatisation supprime une dépense que GianLuca payait réellement, 20 à 30 % de l'économie de la première année, mesurée [MM] et validée par écrit, plafonnée (S2:306 ; S3:315).
5. **Aucune variable sur les ventes d'œuvres** (statut d'intermédiaire, LCB-FT, droit de suite [HY], syn-D:525-526) ni sur des « économies » non mesurées. Un bonus éventuel ne porte que sur ce que Marwin contrôle (délais, réception au premier passage), au plus 10 à 15 % du socle, pas avant la deuxième année.
6. **Transparence** : les gains ne sont jamais présentés comme des heures manuelles fictives (ACC:66) ; l'indicateur « équivalent temps humain évité » est publié au client (syn-C:811).

---

## 5. Calendrier de paiement retenu

### 5.1 La contradiction tranchée

Les archives se contredisent sur les mois 2 à 6 : « règlement sous sept jours après facture de fin de mois » (ACC:57, 29 oct.) contre « payés d'avance, en début de mois » (OFF:19, 2 nov.) [FV] (syn-S:279). Le titre « Un calendrier simple, payé d'avance » [FV] (deck/slides/paiement.html:4) couvre un premier mois soldé à terme échu. **Règle retenue [PR] : le paiement suit la nature de la prestation** (S1:297-304).
- **Capacité réservée** (socles B0, B1, B2 ; minimum de D) : **d'avance**. Marwin bloque des personnes nommées.
- **Livrables** (cadrage, lots) : **acompte à la commande, solde à la livraison**. Le client paie ce qu'il reçoit.
- **Consommation variable** (prix unitaires de D, avenants) : **fin de mois sur relevé**, sous 15 jours. C'est le seul usage conservé de la version du 29 oct.

### 5.2 Échéancier par prestation

| Prestation | Facturation | Échéance | Le travail démarre | Exposition maximale de Marwin [ES] |
| --- | --- | --- | --- | --- |
| A. Cadrage | 50 % à la commande ; 50 % à la réception | Acompte à réception de facture ; solde sous 8 jours, exigible au plus tard 30 jours après la remise sans réserve motivée | À l'encaissement de l'acompte | ≤ 3 250 € HT |
| B0, B1, B2. Socle | Mensuel à échoir : facture le 25 du mois précédent | Le 1er du mois ; premier mois à la signature | À l'encaissement du premier mois | ≤ 15 jours de socle (≈ 2 250 € HT pour B1) |
| C. Lots | 40 % à la commande ; 60 % à la livraison ; 40 / 30 / 30 au-delà de 8 JP | 8 jours | À l'encaissement de l'acompte | ≤ 60 % d'un lot (≈ 3 300 à 4 500 € HT) |
| D. Exploitation | Minimum à échoir ; variable en fin de mois | Minimum le 1er ; variable sous 15 jours | — | ≤ 1 mois de variable |
| E. Avenants | Fin de mois | 15 jours | Après signature de l'avenant | — |
| Achats, abonnements, prestataires | **Jamais par Marwin** : au nom et aux frais de l'entité cliente | — | — | 0 |

**Exposition totale** dans le régime central : ≈ 5 500 à 6 000 € HT de travail non payé à un instant donné (le solde d'un lot et quinze jours de socle) [ES] (verif § 7). Ce travail non payé n'est pas une sortie de trésorerie tant que les associés ne se paient pas sur ce montant (J2:89).

### 5.3 Ordre des opérations

1. Fuite traitée ; documents cohérents ; statuts et pacte prêts.
2. Rendez-vous avec GianLuca : entité, signataire, valideur ; lettre d'intention ou bon de commande du cadrage, signé au nom de « Marwin Tech, SAS en formation », avec un état des actes annexé aux statuts (syn-D:272-286).
3. Si son entité veut l'aide régionale : **dépôt du dossier avant toute signature définitive** [DR] (C19).
4. Immatriculation, compte bancaire, RC professionnelle, plateforme de réception des factures électroniques.
5. K-bis (ou accusé de réception de l'immatriculation) et attestation de vigilance remis au client.
6. Facture d'acompte ; **démarrage à l'encaissement**.

Rien n'est encaissé avant l'immatriculation, ni sur un compte personnel, ni par l'entreprise existante de Morgan (syn-D:48).

### 5.4 Règles communes

- **TVA** facturée dès la première facture, sans compter sur la franchise ; exigible à l'encaissement de chaque acompte (syn-D:288-309). Les devis montrent le HT **et** le TTC : si l'entité de GianLuca ne récupère pas la TVA, elle est un coût réel pour lui [HY] (J1:188).
- **Retard** : relance le lendemain de l'échéance ; **suspension** des travaux non urgents 8 jours après une relance restée sans effet (OFF:207) ; résiliation possible à 30 jours de retard. Pénalités d'au moins trois fois le taux de l'intérêt légal et indemnité forfaitaire de 40 € [FV] (syn-D:288-309).
- **Concession possible** : facturation du socle en fin de mois, payable sous 7 jours, seulement après trois échéances payées à l'heure, avec suspension automatique à J+8 (S3:344-346).
- **Sortie** : préavis d'un mois la première année. Si Marwin interrompt de son fait, les jours non fournis sont remboursés au prorata ; sinon, le mois en cours reste dû. Travaux engagés et réversibilité dus dans tous les cas.
- **Rétractation des petites entreprises** [HY, à trancher par l'avocat] : si le contrat est signé **hors établissement** avec une entité de 5 salariés au plus dont l'activité principale ne couvre pas ce service, la règle des 14 jours de rétractation et « aucun paiement avant 7 jours » pourrait s'appliquer au contrat de Marwin lui-même (syn-D:530 ; J1:186 ; J2:157). Parades : signature à distance, ou délai de 7 jours prévu dans le calendrier. On refuse toute exigence de démarrer avant ce délai si la règle s'applique.
- **Ce qu'on ignore** : comment GianLuca paie et quels délais pratique son entité [IN]. Ce calendrier est une proposition à négocier, pas une hypothèse sur sa trésorerie.

---

## 6. Paramètres des trois scénarios pour le modèle financier

### 6.1 Hypothèses communes [HY sauf mention]

| Paramètre | Valeur à utiliser | Source |
| --- | --- | --- |
| Forme | SAS à l'IS ; président et directeur général | Section 7 |
| Coût d'une rémunération | 1,7 à 1,9 fois le net (central : 1,8) [HY, source secondaire unique] | syn-D:98 |
| Réserve | 10 % du CA encaissé, avant IS | S1:117 ; S2:352 |
| IS | 15 % jusqu'à 42 500 € de bénéfice si le capital est entièrement libéré, 25 % au-delà [FV] | syn-D § 1.4 |
| TVA | 20 %, collectée à l'encaissement, reversée selon le régime choisi ; à modéliser à part (elle n'est pas du CA) | syn-D § 3.2 |
| Capacité par personne | ≈ 17,5 JP par mois (253 jours ouvrés de déc. 2026 à nov. 2027, moins congés, maladie, formation) [ES] | syn-C:146-156 |
| Non facturable | Administration 2 JP, prospection 1,5 à 3,5 JP, maintenance interne 1 à 2 JP, capitalisation 0,5 à 1 JP, aléas 8 % | syn-C:177-190 |
| Charge de démarrage | 9 à 17 JP non facturables sur les mois 0 à 2 | syn-C:212-222 |
| Plafond de capacité engagée | 10 JP facturables par mois la première année (central), quelle que soit la demande | J2:195 |
| Délai d'immatriculation | 1 à 3 semaines après l'engagement écrit [HY] | S1:374 |
| Horizon du modèle | 18 mois à partir de novembre 2026 (DEMANDE § 12) | — |
| Ce qui n'est **pas** dans le CA | Achats du client, prestations de tiers, matériel, aides (aucune n'est acquise) | Section 4.10 |

### 6.2 Paramètres par scénario

| Paramètre | **Prudent** | **Central** (base de pilotage) | **Ambitieux** |
| --- | --- | --- | --- |
| **Périmètre** | Cadrage ; puis socle léger « socle + 1 projet » à partir du mois 3 ; un lot par trimestre. Variante basse : GianLuca s'arrête au cadrage | Cadrage ; pilote de 8 semaines (B0 et un lot, ou C2, ou C6) ; à partir du mois 4, B1 et un lot de 5 000 à 6 000 € toutes les six semaines environ | Cadrage ; pilote avec deux lots ; à partir du mois 4, B1 + 1 projet (« socle + 3 »), lots, une exploitation D à partir du mois 7 ; second client à partir du mois 6 |
| **Disponibilité des associés** | Morgan 50 %, Mathys 25 % ; Morgan garde ses autres projets | Morgan 65 %, Mathys 50 % ; Morgan réduit fortement ses autres projets | 90 % chacun ; Morgan arrête l'essentiel du reste |
| **JP vendues par mois** (régime) | 4 à 6 (capacité ≈ 7) | 8,5 à 10 (plafond 10 ; capacité ≈ 12) | 12 à 15 par les associés + 2 à 4 sous-traitées (capacité ≈ 20) |
| **JP vendues, démarrage** | Mois 1 à 2 : 8 JP de cadrage au total | Mois 1 à 2 : cadrage 8 JP ; mois 2 à 3 : 6 à 7 JP par mois | Mois 1 : 8 JP ; mois 2 à 3 : 10 à 12 JP par mois |
| **Prix** | Cadrage 6 000 € (plancher) ; socle léger 3 000 € par mois ; lot ≈ 4 500 € | Cadrage 6 500 € ; B0 3 500 € par mois ; lot ≈ 6 000 € ; B1 4 500 € ; lots ≈ 3 500 € par mois en moyenne | Cadrage 6 500 € ; B0 3 500 € ; socle + 3 projets 5 700 € ; lots ≈ 4 500 € par mois ; exploitation ≈ 1 500 € par mois ; second client ≈ 2 500 € par mois |
| **CA mensuel en régime** [ES] | ≈ 4 500 € | ≈ 8 000 € | ≈ 11 700 € de GianLuca + 2 500 € d'un autre client |
| **Date de début (mois 1)** | Février 2027 (acompte encaissé au plus tard le 31 janvier) | Janvier 2027 | Mi-décembre 2026 (suppose un rendez-vous en novembre et une immatriculation début décembre) |
| **Durée** | Cadrage 1 mois ; socle par périodes de 3 mois | Cadrage 1 mois ; pilote 2 mois ; socle par périodes de 3 mois ; exploitation par 6 mois | Idem |
| **Probabilités de passage** [HY, paramètres de jugement à remplacer par les faits observés à chaque étape] | Suite après le cadrage : 40 % ; renouvellement trimestriel du socle : 60 % | Pilote après le cadrage : 60 % ; socle après le pilote : 70 % ; renouvellement trimestriel : 80 % | 80 % ; 80 % ; 90 % ; second client signé au mois 6 : 50 % |
| **Sous-traitance** | 0 | 0 (photographe, appels et professionnels facturés directement au client) | 2 à 4 JP par mois à 450 à 550 € par JP [HY] (≈ 900 à 2 200 € par mois), sur lots délimités ; attestation de vigilance dès 5 000 € HT cumulés |
| **Frais fixes mensuels de Marwin** (hors démarrage, hors sous-traitance) | ≈ 1 500 € | ≈ 2 000 € | ≈ 2 800 € |
| dont **outils et IA** | ≈ 150 € | ≈ 150 à 400 € | ≈ 400 à 600 € |
| dont **assurances** (RC professionnelle avec volets IA, cyber, données) | [IN] ; hypothèse de modélisation 100 à 250 € par mois, à remplacer par un devis | Idem | Idem, plafond plus élevé |
| dont **expert-comptable et paie** | ≈ 170 à 420 € par mois (2 000 à 5 000 € HT par an) [ES fondée sur HY] | Idem | Idem |
| dont banque, déplacements, conseil ponctuel | ≈ 20 à 40 € ; 200 à 600 € [IN : lieu de résidence] ; 100 à 300 € | Idem | Déplacements plus nombreux |
| **Frais de démarrage** (une fois) | ≈ 4 000 à 5 000 € | ≈ 5 000 à 7 000 € | ≈ 6 000 à 8 000 € |
| **Apport des associés** (capital libéré et comptes courants) | ≈ 8 000 € | ≈ 10 000 € (fourchette 8 000 à 14 000 €) | ≈ 12 000 à 14 000 € |
| **Rémunérations visées** | Aucune régulière ; au mieux ≈ 650 à 750 € nets par associé à partir du mois 4 [ES] : Marwin reste un complément de revenu | Rien avant le mois 4 ; puis ≈ **1 350 à 1 550 € nets par associé** en régime [ES] ; le plancher de 2 500 € nets par ETP n'est pas atteint la première année | Rien avant le mois 4 ; puis ≈ 2 100 à 2 350 € nets par associé [ES] |
| **Réserve** | 10 % du CA ; viser 3 mois de frais fixes | 10 % du CA ; viser au mois 12 au moins 3 mois de frais fixes et 1 mois de rémunération | Idem |
| **CA sur 12 mois** [ES] | ≈ 50 000 € HT (variante basse : 6 000 €) | ≈ 90 000 € HT | ≈ 150 000 € HT, dont ≈ 17 500 € hors GianLuca |
| **Part de GianLuca dans le CA** | 100 % | 100 %, assumée par écrit (voir la variante 6.3) | ≈ 88 % sur 12 mois, ≈ 82 % au mois 12 |
| **Trésorerie à la fin du mois 12** [ES, avant IS et décalages de TVA, apport compris] | ≈ 11 000 à 12 000 € | ≈ 25 000 € | ≈ 34 000 € |
| **Condition d'entrée** | Cadrage payé | Disponibilités nominatives écrites ; pilote aux critères | Engagement à 90 % inscrit au pacte ; sous-traitant identifié ; pilote réussi |

Calculs : verif § 10 [ES]. Les rémunérations sont des moyennes sur les mois 4 à 12, aux coefficients 1,7 et 1,9. Le modèle simplifié encaisse les factures le mois même ; il ne modélise ni l'IS, ni le décalage de TVA, ni les délais réels d'encaissement (J2:98, 163). Le modèle financier doit les ajouter.

### 6.3 Variante centrale avec un second client

Pour tenir l'objectif de dépendance **sans dépasser 10 JP**, la variante remplace une partie des lots de GianLuca par un second client à partir du mois 7 (S3:376 ; J2:200) : GianLuca 6 500 € HT par mois (B1 + 2 000 € de lots), second client 2 000 € HT par mois. Résultat [ES] (verif § 10) : CA sur 12 mois ≈ 94 500 € HT ; part de GianLuca ≈ 87 % sur 12 mois et ≈ 76 % au mois 12 ; net ≈ 1 450 à 1 600 € par associé en régime. Si le second client n'est pas signé au mois 9, la cible « ≤ 80 % » passe au mois 18 et les associés gardent d'autres revenus.

### 6.4 Tests de résistance à modéliser (DEMANDE § 12)

| Test | Paramètre | Règle de réponse à appliquer dans le modèle |
| --- | --- | --- |
| Retard de paiement de 30, 60 et 90 jours | À partir du mois 4 | Suspension 8 jours après relance ; rémunération arrêtée ; aucun nouveau lot. S1 trouve un point bas ≈ −8 000 € à 90 jours si l'on continuait à travailler et à se payer [ES] (S1:337) : c'est interdit par la règle |
| Rupture après trois mois | Fin du pilote ou du premier trimestre de socle | Préavis d'un mois ; frais ramenés à ≈ 1 000 € ; la réserve doit couvrir environ six mois de frais |
| Non-renouvellement après six mois | Fin du deuxième trimestre de socle | Idem ; bascule vers d'autres clients |
| Dépassement d'un lot de 50 % | Un lot de 6 000 € | ≈ 2 000 à 2 750 € de temps non payé ; provision de risque, puis avenant |
| Hausse des coûts d'IA | + 150 à + 1 000 € par mois (doublements de prix annoncés chez un fournisseur au 1er déc. 2026 et au 1er janv. 2027, ver-R6) | Clause de révision ; deux fournisseurs configurés |
| Indisponibilité d'un associé plusieurs semaines | Capacité ramenée à 4 à 8 JP | Socle tenu par l'autre ; lots reportés sans pénalité au-delà de 10 jours ouvrés |
| Plusieurs urgences simultanées | 2 urgences dans le même mois | Avenant ou report ; aucune absorption gratuite |
| Arrêt d'un fournisseur technique | Un mois de bascule | Exports mensuels testés ; mode manuel |
| Abandon ou retard du projet artistique | — | Sans effet : STRATES et le laboratoire sont hors du CA |
| Croissance commerciale plus lente | Pas de second client | Dépendance à 100 % ; revenus extérieurs maintenus |

---

## 7. Structure juridique recommandée et conditions

**Recommandation [PR] : une SAS à l'IS**, à confirmer par une simulation officielle de l'expert-comptable (syn-D:209-235). Raisons : aucune rémunération régulière n'est financée par un contrat signé [FV] ; une SAS ne coûte aucune cotisation sans rémunération, contre environ 1 255 € par an et par gérant en SARL, plus les forfaits de début d'activité [ES/FV] (syn-D § 1.2) ; un associé peut garder un emploi extérieur ; une entrée de GianLuca au capital est évoquée [DR]. Coût de ce choix : environ 5 000 à 12 000 € de net par personne et par an de moins qu'une SARL à 120 000-180 000 € de CA [ES].

**Conditions.**
- Un président et un directeur général, chacun avec au moins un tiers du capital (condition de l'ACRE, si l'un y est éligible [IN]).
- Un capital modeste, **entièrement libéré** (taux réduit d'IS).
- Des statuts qui organisent le blocage à 50/50 (médiation, tiers expert, offre alternative).
- **Pacte signé avant le contrat client** (section 8.6).
- Rémunération nulle jusqu'au premier socle récurrent, puis fixée par décision collective selon une grille liée au temps engagé.

**Quand immatriculer.** Statuts et pacte préparés tout de suite ; immatriculation déclenchée par un engagement écrit d'une entité identifiée de GianLuca (lettre d'intention ou bon de commande « en formation »). Date de création, date de clôture et déclaration de CFE 1447-C-SD (avant le 31 décembre si la société est créée en 2026) à arrêter avec l'expert-comptable (syn-D:62-81).

**Dès la création.** Compte professionnel ; RC professionnelle **avant la première prestation**, en demandant les exclusions IA, cyber et données, et en **déclarant sincèrement la fuite** à l'assureur : une assurance souscrite après coup ne couvre probablement pas un incident déjà connu [HY] (J1:192 ; J2:154) ; plateforme de réception des factures électroniques (obligatoire depuis le 1er sept. 2026 [FV], syn-D:288-309) ; comptes techniques au nom de la société ; coffre partagé des accès.

**Contrat-cadre, à faire relire par l'avocat avant le premier bon de commande** [PR] :
- limitation de responsabilité : plafond lié aux honoraires des douze derniers mois, aligné sur le plafond assuré ; exclusion des dommages indirects (ventes manquées, économies d'impôt espérées par les prospects) ; obligation de moyens pour le pilotage, la préparation des décisions et les sorties d'IA ; obligation de résultat seulement pour des livrables précis réceptionnés. Un plafond ne joue pas en cas de faute lourde et ne doit pas vider l'obligation essentielle [FV] (C. civ. 1231-3, 1170, 1171 ; rj-R3:264-279 ; J2:153) ;
- séparation entre livraison et adoption ; mandat de dépense ; traitement de la rétractation ; exclusion de l'IA dans tout recrutement ;
- clauses contractuelles types et analyse d'impact des transferts pour les outils d'IA, Anthropic et OpenAI n'étant pas inscrits au Data Privacy Framework [MM] (syn-D:667-681) ; précision du rôle de Marwin (déployeur, ou fournisseur si elle livre un assistant à son nom : AI Act, art. 50) (J2:161) ;
- réversibilité : comptes au nom du client dès le premier jour ; restitution en 15 jours ouvrés ; licence perpétuelle sur les composants génériques.

**SARL en cogérance 50/50 seulement si** toutes ces conditions sont réunies : aucun investisseur avant 24 mois ; un contrat signé d'au moins 120 000 € par an qui finance une rémunération régulière ; aucun associé salarié ailleurs. Il faut alors provisionner la régularisation des cotisations de la deuxième année (syn-D § 1.8).

**À ne pas faire.** Facturer par l'entreprise existante de Morgan, dont la domiciliation est résiliée [DR] (NOTE:6) ; micro-entreprise ; encaisser sur un compte personnel ; présenter l'ACRE, l'ARE, l'ARCE, le FRR ou une aide régionale comme acquis (syn-D:311-315).

**Solvabilité du client** (J1:185). Une fois l'entité nommée, consulter sans contact les registres publics : statut actif, dirigeant habilité, comptes déposés, annonces de procédure collective. L'acompte et la durée du premier engagement sont proportionnés au résultat. Un patrimoine déclaré n'est pas une trésorerie (DEMANDE § 3).

---

## 8. Principes de gouvernance

### 8.1 Rôles

| Acte | Propose | Autorise | Exécute | Contrôle | Valide le résultat |
| --- | --- | --- | --- | --- | --- |
| Priorités du mois, arbitrage entre projets | Marwin (Morgan) | GianLuca ou son délégué écrit, en comité mensuel | Marwin | Mathys (capacité et limite d'encours) | GianLuca |
| Commande d'un lot | Marwin (devis écrit) | Signataire de l'entité concernée | L'associé responsable | **L'autre associé** (quatre yeux, au plus 2 jours ouvrés) | Valideur nommé de l'entité |
| Document envoyé au client | L'auteur | — | L'auteur | L'autre associé, avec le registre « décision → documents touchés » | Morgan, ou Mathys par délégation écrite |
| Dépense pour un projet | Marwin (devis comparés) | GianLuca, par écrit, selon les plafonds | **L'entité cliente** commande et paie | Marwin tient le registre des engagements | Expert-comptable de l'entité |
| Contrat, recrutement, emprunt, investissement, bail, travaux | Marwin prépare le dossier | **Réservé à GianLuca** ou au signataire habilité (ACC:100) | L'entité | Ses conseils | GianLuca |
| Questions fiscales, juridiques, comptables, d'exploitation | Marwin prépare le dossier | — | Le professionnel compétent | — | Le professionnel, puis GianLuca |
| Automatisation sur données réelles | Mathys, après essai | Le responsable du traitement, par écrit, après les préalables RGPD | Mathys | Morgan et le journal | Délégué, sur critères |
| Message à un tiers au nom du client | Marwin rédige | Délégué, message par message | L'entité, sous son nom | — | — |
| Consignes à un prestataire du client (Quali Contact, artisans) | Marwin prépare | Délégué | **Via l'employeur du prestataire**, jamais en direct à ses salariés (syn-D:350-362) | — | — |
| Incident (données, envoi erroné, action non autorisée) | Quiconque le constate **arrête** | Aucune autorisation préalable pour arrêter | Mathys (mesures techniques) | Avocat ou DPD si nécessaire | Morgan informe GianLuca par écrit sous 24 h ; le responsable du traitement décide des notifications |

### 8.2 Plafonds

- **Pendant le cadrage et le pilote : mandat de dépense à 0 €.** Marwin prépare et compare ; l'entité commande et paie (S1:434).
- **Avec un socle récurrent** : 500 € HT par acte et 1 500 € HT cumulés par mois **et par entité**, sur une liste fermée d'actes, dans des budgets déjà approuvés, factures au nom de l'entité et payées par elle ; registre des engagements tenu à jour (syn-D:410-431).
- **Engagement récurrent** (abonnement, location) de plus de 50 € par mois ou de plus de 3 mois : accord écrit préalable. **Contrats, recrutements, emprunts** : jamais délégués.
- **Interne à Marwin** : toute dépense de plus de 300 € HT ou tout abonnement, accord des deux associés ; plus de 1 000 € HT ou plus de 3 mois, décision du pacte à l'unanimité.
- **Capacité** : au-delà de 90 % des JP réservées avant le 20 du mois, arrêt des travaux non urgents ; au-delà de 100 %, avenant ou report (syn-C:285-311).

### 8.3 Urgences

Liste fermée : incident de données ou de sécurité, échéance légale à moins de 48 h. Marwin peut **arrêter** (couper un accès, suspendre un automatisme) sans autorisation. Elle ne dépense ni n'engage. Avec un socle récurrent seulement, une mesure conservatoire d'au plus 300 € HT, prévue au mandat et payée par l'entité, est possible, avec information écrite sous 24 h (S2:453). Tout travail en plus passe par un avenant (offre E).

### 8.4 Silence

| Situation | Règle [PR] |
| --- | --- |
| Demande de décision ou d'autorisation sans réponse | **L'engagement attend** (ACC:103). Relance à 5 jours ouvrés ; à 10 jours, les jalons concernés sont reportés, consignés, et la capacité est réaffectée ; à 15 jours, revue du contrat (réduction de palier) |
| Livrable remis sans réserve motivée sous 10 jours ouvrés | Le solde devient exigible au plus tard 30 jours après la remise : livraison **pour la facturation seulement**. Cela ne vaut ni approbation d'une suite, ni autorisation d'une dépense. La clause « réputé accepté » [FV] (OFF:206) est retirée ; la contradiction avec ACC:103 est tranchée (syn-S:248) |
| Socle arrivé à échéance | **Pas de tacite reconduction** : renouvellement par accord écrit |
| GianLuca injoignable | Seuls les travaux déjà autorisés continuent ; aucune dépense |

### 8.5 Désaccords

| Désaccord | Règle |
| --- | --- |
| Sur un livrable | Réserves motivées sous 10 jours ouvrés ; un cycle de correction compris ; arbitrage en comité ; puis avenant ou arrêt du lot avec avoir |
| Entre deux projets du client | Arbitrage de GianLuca en comité ; entre deux comités, par écrit de son délégué ; la limite d'encours s'applique toujours |
| Entre associés | Liste des décisions prises à l'unanimité au pacte : contrat avec GianLuca, prix et remises, engagement de plus de 1 000 € HT, entrée d'un associé, recrutement, sous-traitance. Tant que le désaccord dure, **rien n'est proposé au client**. Puis médiation, tiers expert, offre alternative |
| Avec Medhi ou un tiers | Aucune action au nom de Marwin sans décision écrite des deux associés |

### 8.6 Ce que le pacte règle avant le contrat client

Disponibilité minimale en JP par mois et par associé, relevé mensuel, **déclaration écrite des autres activités** (OLSEN, Shelby, BOJ.ART, vente en ligne personnelle…) et règle de priorité ; inventaire daté des actifs préexistants (CRM, Jarvis, catalogue, études) avec licence non exclusive à Marwin par défaut ou cession écrite ; rôles (Morgan : relation client et prix ; Mathys : technique et données, avec **délégation écrite de la validation technique**) ; rémunérations liées au temps ; décisions à l'unanimité ; déclaration des conflits d'intérêts ; départ, incapacité, coffre partagé des accès ; **non-réutilisation des données de GianLuca** pour la prospection propre de Marwin ou d'OLSEN, et kit CRM vendu à d'autres construit sur des composants génériques seulement (J2:162) (syn-D:464-484).

### 8.7 Seuils de saturation et occupation

Les seuils de syn-C § 4 s'appliquent (tâches en attente, retards, décisions bloquantes, charge de contrôle, file de validation, incidents, corrections, dépassement, urgences, prospection, impayés). **Correction** : l'occupation se mesure **par personne, sur tout son temps de travail**, y compris OLSEN, Shelby et BOJ.ART ; alerte à 85 % ; au-delà de 95 % pendant deux mois, refus de tout nouveau projet, puis sous-traitance d'un lot ; recrutement seulement après trois mois au-delà de 85 % et un contrat renouvelé qui le finance (J2:158 ; syn-C:299).

### 8.8 Un rôle à la fois avec GianLuca Carlone

| Rôle évoqué | Règle | Quand | Conditions |
| --- | --- | --- | --- |
| **Client** | Seul rôle accepté jusqu'au bilan du mois 6 (C8) | Dès le cadrage | Entité identifiée ; un bon de commande par prestation et par entité ; valideur nommé, distinct d'un éventuel salarié |
| **Bailleur** (bureaux) | Refusé pendant le cadrage et le pilote | Au plus tôt après le bilan du mois 6 | Convention séparée (accès sans horaires imposés, usage partagé, assurance, restitution) ; aucun lien avec les honoraires |
| **Employeur** | Refusé avant le bilan du mois 6 ; jamais des deux associés | Ensuite, par accord séparé | Une seule personne ; fonctions non couvertes par Marwin ; temps séparés ; validation des livrables de Marwin par une autre personne ; jamais un argument de prix (syn-D:395-408) |
| **Investisseur** | Pas de discussion avant 12 à 24 mois | Après au moins deux renouvellements du socle | Minoritaire, sans veto opérationnel ; contrat client résiliable indépendamment ; jamais contre une baisse d'honoraires ; l'acompte n'est ni du capital ni un prêt (OFF:149) |
| **Financeur de R&D ou de création** | Aucun | — | Section 9 |

**Lien de Morgan avec BOJ.ART.** Déclaration écrite **proactive** à GianLuca dès le premier document remis ; abstention de toute recommandation d'achat ou de vente qui concerne Medhi (C9 ; syn-S:325).

---

## 9. Ce qui sort du périmètre, et à quelles conditions cela pourrait revenir

| Sujet | Décision | Raison | Conditions d'un retour |
| --- | --- | --- | --- |
| **Medhi et BOJ.ART** | Hors de l'offre Marwin | Décision du 4 nov. [DR] (NOTE:25) ; aucun accord écrit avec Medhi [IN] ; conflit d'intérêts (syn-S:325) | Si la galerie veut vendre ses pièces : **contrat de dépôt-vente direct** entre Medhi et l'entité de GianLuca, sans Marwin ni commission. Une collaboration de Marwin avec Medhi ne revient que par décision écrite des deux associés, contrat séparé (prix, propriété intellectuelle, attestation de vigilance), conflit déclaré au client. Marwin ne promet jamais ce qu'elle ne détient pas (œuvres, films, exclusivité, parc d'impression, code de Jarvis) (syn-D:500) |
| **STRATES, Éclosion et autres créations** | Gelés | Aucun budget propre (les 323 875 € portent sur les figurines) ; plus d'artiste ; rien de fabriqué ni mesuré (syn-P:505-522) | Financeur écrit ; budget plafonné ; artiste sous contrat ; banc fermé sans public ; intégrateur tiers pour toute machine ; droits réglés ; au plus 10 % de la capacité, hors socle ; pas avant le mois 6 |
| **Laboratoire IA et robotique, DGX Spark, IA locale** | Retirés | Option sans objet depuis le retrait de STRATES (OFF:84) ; aucun des onze processus ne demande de calcul local (syn-C:666-672) ; DGX Spark de 128 Go ≈ 6 170 € HT [ES] (ver-R6) | Un usage démontré (contrainte mesurée de confidentialité ou de volume), un financeur écrit, un achat par l'entité cliente, au plus 10 % de la capacité, pas avant le mois 6 à 12 |
| **Vernissage « signature » avec bras robotisé** | Reporté sans date | Machine au contact du public ; dépendance à Medhi ; délais administratifs | Jamais de robot devant le public sans intégrateur, analyse de risques et exploitant responsable. Un **premier événement sans robot** reste possible via le lot C3, l'organisateur légal étant l'entité de GianLuca, et pas avant 2 à 3 mois dans un lieu autorisé |
| **Cabaret et exploitation des lieux** | Exclus | Licences et autorisations nominatives, au nom de l'exploitant (syn-P:575-584) | Seulement comme dossiers (C3, C4, C7) et coordination sous mandat écrit ; l'exploitant reste l'entité de GianLuca |
| **« Copilote Jarvis » comme produit et nom** | Suspendu | Propriété du code et du nom non réglée ; dépôt BOJART sans licence (syn-S:290) | Propriété et licences réglées par écrit ; gain mesuré sur le pilote P3 |
| **Intermédiation de vente, commission, encaissement, garde ou transport d'œuvres, « enchères »** | Refusés | LCB-FT, droit de suite, statut d'intermédiaire ; « enchères » réservées aux opérateurs habilités (S2:267) | Pas la première année ; ensuite seulement après avis écrit d'un avocat |
| **Exécution administrative, comptabilité, conseil juridique ou fiscal, gestion immobilière, séjours des invités, recouvrement** | Exclus | Activités réglementées ; prix non défendable (syn-D:410-431) | Jamais exercés par Marwin : elle prépare les dossiers pour les professionnels ; l'exécution peut passer à une personne du client (C6) |
| **Astreinte 24 h sur 24, couverture 30 jours sur 30** | Exclue | Non tenable à deux (ACC:105) | Forfait d'astreinte séparé, avec relais nommés, sur demande |
| **Agents vocaux sortants, outils RH ou de notation, automatisations sans approbation humaine** | Exclus | AI Act, risques d'automate d'appel, recommandations de l'ANSSI (syn-D:649-699) | Avis de l'avocat ou du DPD ; grille de sécurité des agents appliquée |
| **Simulateur d'« économie d'impôt » du CRM** | Retiré | Il surestime l'économie (taux fixe de 25 %, cumul non plafonné) (J2:115) | Corrigé et validé par écrit par un professionnel |
| **Bureaux, salariat, capital** | Différés | Requalification, dépendance, blocage croisé (syn-D:319-446) | Section 8.8 |

---

## 10. Conditions minimales pour démarrer un travail payé (toutes requises)

1. **Fuite traitée** : dépôt privé vérifié ; fiche de violation ; décision de notification documentée avec un avocat ou un DPD ; décision sur l'information des personnes ; GianLuca informé par écrit.
2. **Documents client cohérents** : une seule version ; ni Medhi, ni BOJ.ART, ni STRATES, ni laboratoire, ni taux de 750 €, ni formules de 15 000 ou 30 000 €, ni ancien prénom ; V5 jamais transmis ; PR n° 1 fermée ou PDF marqué « historique ».
3. **Accord écrit de Mathys** sur cette stratégie, le retrait de Medhi, la SAS et le régime du CRM ; **disponibilités nominatives** écrites d'au moins 6 JP facturables par mois à deux.
4. **Marwin immatriculée** (SAS), avec compte professionnel, RC professionnelle souscrite (fuite déclarée), plateforme de facturation électronique, comptes techniques à son nom ; **pacte signé**.
5. **Apport des associés déposé** (8 000 à 14 000 €).
6. **Entité cliente identifiée** (dénomination, SIREN, signataire habilité, effectif), solvabilité vérifiée sur les registres publics, et **bon de commande signé**.
7. **Contrat-cadre relu par l'avocat** : limitation de responsabilité, séparation livraison/adoption, mandat de dépense, rétractation, transferts IA.
8. **Acompte encaissé**, et délai de 7 jours respecté si la règle de rétractation s'applique.
9. **Délégué et accès** désignés côté client ; comptes et outils ouverts à son nom.
10. **Aucune donnée personnelle réelle** avant la désignation du responsable du traitement, le contrat de l'article 28, le registre, des offres d'IA professionnelles avec clauses contractuelles types et analyse d'impact des transferts.

---

## 11. Signaux pour suspendre

- Impayé non régularisé 8 jours après relance.
- Accès non fournis 10 jours ouvrés après le démarrage.
- Deux décisions bloquantes en attente depuis plus de 15 jours ouvrés.
- Occupation d'un associé au-delà de 95 % pendant deux mois, ou prospection sous 50 % du plancher pendant deux mois.
- Demandes hors périmètre dépassant 20 % de la capacité pendant deux mois.
- Incident critique : nouvelle exposition de données, action non autorisée, envoi erroné.
- Demande d'agir hors mandat : signer, payer, engager pour le client ; travailler sans bon de commande, sur des comptes personnels, ou avancer des achats.
- Pression pour travailler avant le paiement, ou avant le délai de 7 jours si la règle de rétractation s'applique.
- Indices de subordination : horaires imposés, ordres directs, place dans un organigramme, exclusivité de fait (syn-D:332-348).
- Proposition d'échanger des honoraires contre des bureaux, un emploi ou du capital ; investissement lié à une baisse d'honoraires.
- Demande de rémunération sur les ventes d'œuvres, d'encaissement pour la galerie ou de robot au contact du public.

---

## 12. Réduire, reporter ou refuser

| Situation | Réponse | Pourquoi |
| --- | --- | --- |
| GianLuca ne veut confier qu'un projet (par exemple les ventes d'œuvres) | **Réduire** : un lot (C2 ou C1), sans socle | Le pilotage global n'est pas le besoin ; un lot reste rentable |
| Il refuse le prix du cadrage complet | **Réduire** : version réduite à 4 800 € HT ; jamais de remise sous 750 € par JP | Un refus de payer un cadrage est déjà une réponse (S1:57) |
| Il préfère embaucher | **Réduire** : C6 outillage et passation, puis socle de pilotage léger éventuel | Au-delà de 6 à 8 JP stables, le salarié est moins cher pour lui (C2) |
| Les associés ne peuvent pas engager ensemble au moins 6 JP facturables par mois | **Réduire** au cadrage et à un lot, ou **reporter** | Sous ce seuil, un socle et un projet ne tiennent pas (syn-C:253) |
| Aucune entité nommée ou aucun rendez-vous avant le **15 décembre 2026** | **Reporter** à janvier, sans aucune production | Scénario S5 « personne ne paie » (syn-P:304) |
| Cadrage non commandé et payé au **31 janvier 2027** | **Reporter sans date** ; réorienter le temps vers d'autres clients ; rester joignable | Limite le travail gratuit (S3:508) |
| Fuite non traitée, apport impossible, désaccord de Mathys | **Reporter** | Conditions de validité V1, V2, V4 |
| Aide régionale demandée par le client | **Décaler** la signature le temps du dépôt, sans travailler | Dépôt avant signature [DR] |
| Refus de payer le cadrage | **Refuser** la suite ; remettre gratuitement à GianLuca ce qui lui revient (documents, données du CRM), après avis sur les rôles RGPD | Hypothèse du besoin infirmée ; geste qui préserve la relation (J1:152) |
| Demande de 20 à 40 JP par mois avec présence quotidienne, sans entité, mandat ni accès | **Refuser** sous cette forme ; proposer le cadrage | Capacité et requalification |
| Paiement en bureaux, en emploi ou en capital ; commission sur les ventes ; obligations d'exploitant ; robot devant le public ; R&D sans financeur écrit | **Refuser** cette partie, en expliquant pourquoi | Sections 8.8 et 9 |
| Salariat d'un associé combiné au contrat Marwin dès le départ | **Refuser** avant le bilan du mois 6 | Conflit d'intérêts, requalification |
| Exigence de démarrer avant l'immatriculation | **Reporter** le travail ; au plus une signature au nom de la société en formation, sans encaissement | syn-D:272-286 |

**L'alternative du salariat, chiffrée avant le rendez-vous** (J2:160). Un poste de cadre chez GianLuca (≈ 3 400 € nets pour 6 149 € de coût employeur [MM]) rapporterait davantage que tous les scénarios centraux de Marwin la première année (≈ 1 350 à 1 550 € nets en régime). C'est le principal risque pour l'indépendance de Marwin pendant la négociation. Règle : cette option n'est pas discutée avant le bilan du mois 6 ; si GianLuca la propose, Morgan et Mathys la traitent comme une décision séparée (revenu contre indépendance), jamais combinée avec une prestation de Marwin sur les mêmes sujets.

---

## 13. Cinq décisions prioritaires

| N° | Décision | Qui | Quand | Preuve d'exécution |
| --- | --- | --- | --- | --- |
| 1 | **Traiter la fuite** : rendre le dépôt privé et le vérifier ; ouvrir la fiche de violation ; décider de la notification à la CNIL avec un avocat ou un DPD (notification échelonnée ou retard motivé si nécessaire) ; décider de l'information des personnes ; informer GianLuca par écrit dans des termes validés ; ne plus utiliser aucune donnée réelle | Mathys et Morgan | **Avant l'échéance du 5 nov.** | Décision datée et motivée ; fiche de violation ; capture de la visibilité « privé » |
| 2 | **Remplacer l'offre de six mois par le seul cadrage** (6 500 € HT, moitié à la commande) ; retirer formules, taux affiché, ancre, laboratoire, création, Medhi, BOJ.ART ; corriger le diaporama (section 17.4) ; **arrêter immédiatement** toute production non commandée ; préparer le message de recadrage | Morgan, validé par Mathys | Arrêt immédiat ; documents au 13 nov. ; message au 19 nov. | 0 mention interdite dans les documents remis ; 0 JP hors remise en ordre |
| 3 | **Accord écrit des associés** : stratégie ; portée du retrait de Medhi et message à Medhi ; disponibilités nominatives (JP par mois, projets que Morgan suspend) ; délégation de la validation technique à Mathys ; propriété du CRM ; rémunération cible acceptée | Morgan et Mathys | Au 19 nov. | Fiche « rôles et disponibilités » signée ; décision écrite sur Medhi |
| 4 | **Choisir la SAS à l'IS** ; préparer statuts et pacte ; immatriculer seulement sur engagement écrit d'une entité identifiée ; ne rien encaisser avant ; réunir l'apport de 8 000 à 14 000 € ; ne pas utiliser l'entreprise existante de Morgan | Morgan et Mathys, avec l'expert-comptable et l'avocat | Préparation en novembre ; immatriculation sur engagement écrit | Projets de statuts et de pacte ; fonds disponibles |
| 5 | **Fixer les garde-fous** : rendez-vous avant le 15 déc. 2026 ; cadrage payé au 31 janv. 2027 sinon report sans date ; plafond de 10 JP facturables par mois la première année ; occupation ≤ 85 % mesurée sur tout le temps de chacun ; plancher de prospection de 1,5 à 2,5 JP par mois | Morgan et Mathys | Avant le rendez-vous | Règles écrites dans le pacte et dans le registre interne |

---

## 14. Questions bloquantes (dix)

**À GianLuca Carlone**
1. Quelle entité signe, paie et valide nos travaux (dénomination, SIREN, personne habilitée, nombre de salariés) ? Une seule, ou une par projet ?
2. Quelles sont vos trois priorités pour les 90 prochains jours, et que vous coûte chacune aujourd'hui ? Les « vingt jours par mois » viennent-ils de vous ?
3. Quel budget, quel mode et quel délai de paiement votre entité pratique-t-elle ? Récupère-t-elle la TVA ? Envisagez-vous l'aide régionale au conseil (dépôt avant signature, échéance annoncée au 31 déc. 2026) ?
4. Qui, chez vous, exécutera au quotidien (une personne existante, un recrutement), quels accès nous donnerez-vous, et par quel canal préférez-vous travailler ?
5. Pour les ventes d'œuvres : au nom de quelle structure vendez-vous, quelles œuvres sont disponibles, quel conseil fiscal vous suit, et qui appellera les entreprises (Quali Contact est-il engagé) ?

**À Morgan et Mathys**
6. Depuis quand savez-vous que le dépôt FinanceScope/CRM-Carlone est public ? Qui contrôle cette organisation ? Le dépôt est-il encore public ? Des copies existent-elles ? Qui décide de la notification ?
7. Combien de JP par mois chacun engage-t-il par écrit de décembre 2026 à juin 2027, et quels projets Morgan suspend-il ? Quelle est la situation de Mathys (emploi, études) ?
8. Mathys approuve-t-il cette stratégie, le retrait de Medhi, la SAS et le régime de propriété du CRM ?
9. Qu'a vu, reçu ou accepté GianLuca (version à quatre jours, lettre du 29 oct. au prénom erroné, V5, diaporama de 13 ou de 11 diapositives, taux de 750 €, rapport CRM, vernissage) ? Qu'a-t-on promis à Medhi ?
10. Quel apport pouvez-vous déposer (8 000 à 14 000 €), quelle rémunération cible acceptez-vous (≈ 1 350 à 1 550 € nets chacun en régime central), et pouvez-vous vivre trois à quatre mois sans rémunération de Marwin ?

**Questions aux professionnels** (non bloquantes pour cette stratégie, bloquantes pour le contrat) : à l'avocat ou au DPD, rôles RGPD, notification et art. 34 (syn-D:758-764) ; à l'avocat en contrats, limitation de responsabilité, rétractation appliquée au contrat de Marwin, cession par livrable, régime du CRM « offert » (syn-D:747-756) ; à l'avocat en droit du travail, indices de subordination et salariat éventuel (syn-D:740-745) ; à l'expert-comptable, simulations SAS et SARL officielles, date de création, TVA, CFE (syn-D:703-729) ; à l'assureur, couverture IA, cyber et données, et traitement de l'incident connu.

---

## 15. Tableau « recommandation | preuve | hypothèse | limite | décision correspondante »

| Recommandation | Preuve | Hypothèse | Limite | Décision |
| --- | --- | --- | --- | --- |
| Ne pas présenter l'offre de 15 000 / 30 000 € HT par mois | Aucune parole directe du client [FV] (syn-S:38) ; « vingt jours » attribués tantôt au client, tantôt à Morgan [FV] (COP:65 ; ACC:7) ; 20 JP = 78 à 83 % du temps, 40 JP = 140 à 145 % [ES] (syn-C:228-229) | Un besoin de coordination est plausible [HY] (syn-P:227) | 50 conversations ChatGPT non lues ; GianLuca a pu accepter oralement [IN] | n° 2 |
| Vendre d'abord un cadrage de 6 500 € HT | Format soutenu par le marché [HY] (rj-R6 (e)) ; coût 4 700 à 5 900 € [ES] | GianLuca accepte de payer un test | Aucune référence démontrable ; s'il a vu 750 €, 6 000 € | n° 2 |
| Traiter la fuite avant tout | Dépôt public le 4 nov. [DR] (CTX:11) ; connaissance au plus tard le 2 nov. [FV] (AUD:3, 15) ; ≈ 800 à 931 numéros [ES] | Violation au sens de l'art. 4 ; Morgan et Mathys responsables de fait [HY] (syn-D:593-599) | Visibilité non revérifiée par l'audit ; date de connaissance [IN] | n° 1 |
| Trois voies au choix après le cadrage | Besoins rapportés : ventes d'œuvres (COP:13), « ne pas gérer chaque détail » (ACC:13) [DR] | Le client choisira sur pièces | Aucune parole directe | Cadrage |
| Plafond de 10 JP et occupation ≤ 85 % sur tout le temps | Capacité 7 / 12 / 20 JP [ES] (syn-C:190) ; Morgan mène une dizaine d'autres projets [FV pour la liste] (NOTE:17) | Disponibilités 65 / 50 % | Disponibilité de Mathys [IN] | n° 3 et n° 5 |
| 750 € = plancher interne ; prix cible 800 à 950 € ; forfaits | Coût 591 à 737 € (12 JP) et 710 à 885 € (10 JP) [ES] ; coût d'un cadre salarié 6 149 € [MM] (ver-R6 n° 3) | Coefficient 1,7 à 1,9 ; frais 1 500 à 2 500 € [HY] | Repères de marché secondaires ; aucune simulation officielle | n° 2 |
| Paiement selon la nature de la prestation | Contradiction ACC:57 / OFF:19 [FV] (syn-S:279) | Le client accepte l'avance sur le temps réservé | Pratiques de paiement [IN] ; règle de rétractation [HY] | n° 2 et n° 5 |
| Medhi, STRATES, laboratoire hors périmètre | Décision du 4 nov. [DR] ; STRATES sans budget propre [FV] (syn-P:505-522) ; laboratoire sans objet (OFF:84) [FV] | Mathys est d'accord | Ce qui a été promis à Medhi [IN] | n° 3 |
| SAS à l'IS, immatriculation conditionnelle | Aucun contrat [FV] ; 0 € de cotisation sans rémunération en SAS (syn-D § 1.2) | Investisseur et emploi extérieur évoqués [DR] | Coefficient d'une source secondaire ; pas de simulation officielle | n° 4 |
| Pilote commercial seulement avec ses préalables | 283 numéros sur 471 à confirmer, 0 appel [FV] ; 238 bis AB valable jusqu'aux achats faits avant le 31 déc. 2028 [FV] | Les entreprises de la Nièvre achètent des œuvres [HY] | Structure vendeuse [IN] ; art. 34 [IN] ; pièces faites à la machine non validées | Voie (a) |
| Le silence ne vaut pas accord ; mandat à 0 € au départ | Contradiction OFF:206 / ACC:103 [FV] (syn-S:248) | Le client accepte des décisions écrites | Canal de travail réel [IN] | Contrat-cadre |
| Dates butoirs du 15 déc. et du 31 janv. | Travail gratuit depuis le 18 oct. (syn-P:304) ; OLSEN : 36 propositions, 0 envoi [DR] (NOTE:9) | Un rendez-vous peut être obtenu | Aucun rendez-vous fixé (NOTE:5) | n° 5 |
| Limitation de responsabilité et traitement de la rétractation au contrat | C. civ. 1231-3, 1170, 1171 [FV] (rj-R3:264-279) ; règle L221-3 pour les ventes [FV] (syn-D:530) | La règle s'applique au contrat de Marwin [HY] | Non tranché par un avocat | Condition 7 |
| Dépendance à 100 % assumée, variante avec second client | Aucun autre client [FV négatif] ; cibles de S1 et S2 non chiffrées (J2:97) | Un second client vers le mois 7 [HY] | Prospection de Morgan non démontrée (0 envoi OLSEN) | n° 5 |
| Comparaison de coûts montrée au client | Coûts URSSAF d'un assistant et d'un cadre [MM] (ver-R6 n° 3) | Elle renforce la confiance plus qu'elle ne fait perdre la vente [HY] | Coûts cachés d'un recrutement non chiffrés | Documents client |

---

## 16. Risques propres à cette stratégie

| Risque | Probabilité [HY] | Parade |
| --- | --- | --- |
| GianLuca voulait « une équipe » tout de suite et va voir ailleurs | Moyenne | Montrer la voie (b) et le socle comme suite naturelle ; mesurer sa réaction au cadrage ; révision vers le haut prévue (section 1.2) |
| Il a déjà accepté oralement l'offre de six mois | Faible à moyenne [IN] | Message de recadrage d'une page, signé des deux, avant tout rendez-vous |
| Le revenu des associés reste trop faible la première année | Élevée | Revenus extérieurs maintenus ; scénario prudent assumé ; second client avant de quitter toute autre source |
| La voie commerciale échoue faute d'œuvres ou de structure vendeuse | Élevée | Préalables écrits avant de vendre C2 ; sinon voie (b) ou (c) |
| Aucune personne n'est désignée et Marwin glisse vers l'exécution | Moyenne | Règle de C6 : pas de reprise de l'exécution ; socle limité au pilotage |
| Les conséquences de la fuite abîment la confiance | Moyenne | Transparence écrite validée par le conseil ; aucune donnée réelle avant les préalables |
| Morgan reste dispersé sur ses autres projets | Élevée | Occupation mesurée sur tout son temps ; plafond de 10 JP ; validation déléguée à Mathys |
| L'apport n'existe pas | Moyenne [IN] (NOTE:6, 8) | Réduire les sorties de la phase 0 au conseil sur la fuite et aux statuts ; décaler le reste après l'acompte |
| Requalification malgré tout | Faible à moyenne | Pas de bureaux avant le mois 6 ; prix au livrable ; liste des livrables avant la liste des heures ; autres clients réels |

---

## 17. Ce qui va dans les documents destinés à GianLuca, et ce qui reste interne

### 17.1 Répartition

| Destiné à GianLuca (après accord écrit de Morgan et de Mathys) | Interne |
| --- | --- |
| Le message de recadrage d'une page (17.3) | Coûts complets, marges, planchers (6 000 €, 750 € par JP, prix cible), taux d'avenant interne |
| La proposition de cadrage : objet, livrables, exclusions, dépendances, réception, prix HT et TTC, paiement | Rémunérations visées, apport, capacités et disponibilités des associés, autres projets de Morgan |
| La présentation des trois voies possibles après le cadrage, sans coûts ni marges | Paramètres des scénarios, probabilités, trésorerie, tests de résistance |
| La comparaison de **ses** coûts : Marwin, un assistant ou un coordinateur salarié, des prestataires au rendez-vous (section 4.9) | Le présent document, les trois stratégies, les deux jugements, les synthèses |
| Le calendrier de paiement (section 5, sans les colonnes d'exposition) | Pacte, désaccords éventuels entre associés, alternative du salariat |
| Les principes de gouvernance : décisions qu'il garde, plafonds, urgences, silence, réversibilité, « un sujet, un accord » | Analyse détaillée des risques juridiques de Marwin et questions aux professionnels |
| La déclaration écrite du lien de Morgan avec BOJ.ART | Détail de la décision sur Medhi et de ce qui lui avait été dit |
| L'information sur l'incident de données et les mesures prises, dans des termes validés par le conseil | La fiche de violation elle-même et l'évaluation de l'exposition des associés |
| Le K-bis et l'attestation de vigilance, le moment venu | Liste des corrections (17.4), qui sert à préparer les documents |
| Les questions 1 à 5 de la section 14, sous forme d'ordre du jour | — |

**Règles d'écriture des documents client.** Toujours « GianLuca Carlone » ; aucune occurrence de l'ancien prénom ; aucune pièce historique fautive (V5, lettre ACC:9-11) renvoyée ; aucun taux journalier ; prix HT et TTC ; aucun résultat promis (ventes, rendez-vous) ; aucune aide présentée comme acquise ; aucune image générée par IA présentée comme réelle sans mention.

### 17.2 Pièces historiques

Les pièces d'origine restent intactes (DEMANDE § 1). Les nouvelles versions sont datées. L'offre écrite du 2 nov., STRATES v1.1, le vernissage et le PDF de 13 diapositives de la PR n° 1 sont marqués « historique, retiré le [date] », jamais réécrits en silence.

### 17.3 Contenu du message de recadrage (une page, signée des deux associés)

1. Ce qui change et pourquoi, en commençant par l'intérêt de GianLuca : un cadrage court et payé avant tout engagement long, pour qu'il décide sur pièces.
2. Ce qui est retiré : la formule de six mois, l'option laboratoire, la création avec Medhi et BOJ.ART.
3. Ce qui reste à lui : les documents et données qui le concernent, sous un régime écrit.
4. L'incident de données et les mesures prises, dans les termes validés par le conseil, sans reconnaissance de responsabilité non pesée (J1:192).
5. La déclaration du lien de Morgan avec BOJ.ART.
6. La proposition de cadrage et les questions de l'ordre du jour.
7. Si une pièce au prénom erroné lui a été remise : une correction sobre.

### 17.4 Corrections du diaporama de 11 diapositives (avant toute remise)

| Vue | Texte actuel [FV] | Correction |
| --- | --- | --- |
| `cover` | Note : « Puis montrer ce qui est déjà livré » | Retirer tant que la fuite n'est pas traitée |
| `livre` | « Votre CRM de prospection est prêt à servir » (:4) ; « Montrer le CRM en direct » (:26) | « Un CRM de 500 fiches existe ; il sera remis en conformité avant tout usage » ; ne pas le montrer en direct (syn-D:636) |
| `proposition` | « Six mois pour […] vendre vos œuvres avec le CRM » (:3) | Retirer (promesse de résultat) ; présenter le cadrage |
| `volets` | « Copilote Jarvis » ; « Séjours des invités » | Retirer Jarvis (propriété non réglée) et les séjours (vente de voyages réglementée) ; garder « Marwin organise ; l'exécution peut revenir à votre équipe » |
| `premier-mois` | « 20 journées » réparties 6 / 7 / 4 / 3 | Retirer ; remplacer par le contenu du cadrage |
| `formules` | 15 000 € (:9), 30 000 € (:20), « Taux unique : 750 € HT » (:30) | Retirer ; remplacer par l'offre de cadrage et la suite possible |
| `paiement` | « Un calendrier simple, payé d'avance » (:4) ; « Le travail démarre à réception » (:10) ; 15 000 € (:25) | « Le temps réservé se paie d'avance, les livrables à la livraison » ; démarrage après immatriculation, signature et encaissement |
| `laboratoire` | « Option laboratoire », 30 000 € HT (:9), « acheté et possédé par votre entité » (:14) | Retirer la vue |
| `garanties` | « Réversibilité : fichiers, configurations, documentations et accès remis » (:30) | Garder seulement avec « comptes ouverts au nom de votre entité dès le premier jour » ; garder « Aucun travail facturé deux fois » (:38) |
| `cadre` | « Formule, livrables, réception, paiement d'avance, réversibilité » | « Prestations, livrables, réception, paiement selon la nature, réversibilité » ; garder « Un sujet, un accord » |
| `etapes` | « Choisir la formule, avec ou sans l'option laboratoire » ; « Verser l'acompte : le travail démarre » | « Désigner l'entité ; commander le cadrage ; acompte après immatriculation » |

---

## 18. Limites

- **Aucune parole directe de GianLuca Carlone** n'existe dans les pièces (syn-S:38). La valeur pour lui, ses priorités et sa solvabilité restent des hypothèses fondées sur des déclarations rapportées par Morgan.
- **La collecte est incomplète** : 169 conversations ChatGPT lues sur 219 ; des promesses faites au client peuvent exister hors du corpus (syn-S h.1).
- **La visibilité actuelle du dépôt FinanceScope/CRM-Carlone n'a pas été revérifiée** par cet audit ; la date exacte de connaissance de la fuite est [IN]. Si elle est antérieure au 2 nov., le délai de la CNIL est déjà dépassé et la notification doit être motivée.
- **Les coûts de Marwin sont des hypothèses** : coefficient SAS d'une source secondaire, frais fixes, RC professionnelle, conseil, déplacements. Aucune simulation officielle n'a été faite ; l'expert-comptable doit refaire les calculs, IS et TVA compris.
- **Les probabilités de passage** sont des paramètres de jugement [HY], à remplacer par les faits observés à chaque étape.
- **Les points juridiques marqués [HY]** (rétractation appliquée au contrat de Marwin, notification échelonnée, assurance d'un incident connu, rôles RGPD) n'ont pas été vérifiés dans les textes par l'arbitre ; ils sont à soumettre à l'avocat ou au DPD.
- **Les disponibilités de Morgan et de Mathys** ne sont documentées nulle part ; sans engagement écrit, seul le scénario prudent est défendable (J2:245).
