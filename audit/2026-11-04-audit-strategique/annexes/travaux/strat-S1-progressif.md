# Stratégie S1 « progressif » : la plus petite collaboration payante, puis des preuves

Stratège « S1-progressif » de l'audit Marwin Tech × GianLuca Carlone. Rédigé le 4 novembre 2026 au soir, indépendamment des autres stratèges.

**Document interne.** Il contient des coûts, des marges, des planchers de prix et des hypothèses de rémunération des associés. Il ne doit pas être transmis à GianLuca Carlone. Seuls les contenus des offres (sans coûts ni marges), le calendrier de paiement (§ 5) et les principes de gouvernance (§ 8) peuvent servir de base à une proposition client, après validation par Morgan et Mathys.

**Posture.** Démarrage progressif et prudent : chercher la plus petite collaboration payante qui produit vite des preuves, protège Marwin (trésorerie, indépendance, responsabilité) et laisse GianLuca Carlone juger sur pièces avant tout engagement large.

## Méthode, sources et conventions

**Bases.** Les quatre synthèses `syn-sources.md` (syn-S), `syn-portefeuille.md` (syn-P), `syn-capacite-ia.md` (syn-C) et `syn-droit.md` (syn-D) ; le mémo de marché `rj-R6-marche.md` et son contrôle `ver-R6-marche.md` ; `rj-R2-fiscal.md` pour les règles de facturation ; `rj-R4-donnees-ia.md` et `ver-R4-donnees-ia.md` pour la fuite de données. Quand un contrôleur corrige un lecteur ou un chercheur, c'est la correction qui est retenue.

**Pièces d'origine rouvertes ce soir** (dépôt `Momolscode/Carlone`, `origin/main` = 7b46602, lecture seule) : OFF:9-22, 56-65, 84, 100-215 ; ACC:7, 40-66, 90-110 ; AUD:3-16, 50-64, 96-104 ; METH:77 ; R:220, 1469 ; CTX:95 ; diaporama client (`deck.json:7` ; `slides/paiement.html`, `formules.html`, `garanties.html`, `laboratoire.html`, `proposition.html`, `etapes.html`, `livre.html`).

**Calculs.** Refaits en Python (`python3 -I`) : `audit/2026-11-04-audit-strategique/annexes/travaux/calculs/s1-calc/cout.py` (coût complet d'une journée facturable) et `audit/2026-11-04-audit-strategique/annexes/travaux/calculs/s1-calc/plan.py` (scénarios à 12 mois et tests de trésorerie). Tous leurs résultats sont des estimations [ES].

**Aucune action extérieure** : aucun contact, aucune démarche, aucune dépense, aucune modification du dépôt. Les recommandations ci-dessous décrivent ce que Morgan et Mathys pourraient décider ; rien n'a été fait.

**Nom du client.** Le client s'appelle **GianLuca Carlone**. Dans les pièces citées, « Carlone » désigne tantôt la personne, tantôt une entité non identifiée.

**Codes.** [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] information inconnue.

**Unité.** JP = journée-personne de 7 h (définition de l'offre : 20 JP = 140 h, OFF:13-16). Deux personnes présentes une journée consomment 2 JP.

| Abréviation | Pièce |
| --- | --- |
| OFF | `interne/offre-marwin-tech-remuneration-et-collaboration.md` (2 nov.) |
| ACC | `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md` (29 oct.) |
| CTX | `interne/contexte-projet-carlone.md` (4 nov.) |
| AUD | `interne/audit-marwin-tech-carlone.md` (2 nov.) |
| METH | `sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md` |
| R | `interne/recueil-sessions-chatgpt-2026-11-04.txt` |
| V5 | `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` |
| deck/ | diaporama client en ligne, copie locale `scratchpad/artifact-files/04f14ef8-a5fd-429b-9b3e-6d69b1d2ce5f/project/` |
| NOTE | `audit-work/note-point-4-novembre-et-activites.md` |
| syn-S, syn-P, syn-C, syn-D | les quatre synthèses de `audit-work/` |

**Trois faits nouveaux intégrés.**
1. **Retrait de Medhi et de BOJ.ART** : demandé oralement par Morgan le 4 nov. [DR] (NOTE § C). Seul le diaporama client a été corrigé : 11 vues, sans `strates` ni `strates-phases` [FV] (`deck.json:7`). Restent non corrigés [FV] : l'offre écrite (« Option création », OFF:22), STRATES v1.1, le diaporama du vernissage (signé « avec Medhi, BOJ.ART », p. 12) et le PDF de 13 diapositives de la PR n° 1 (syn-S:65-69).
2. **Fuite de données probable** : le dépôt public FinanceScope/CRM-Carlone est très probablement une violation de données personnelles [HY fort] (rj-R4:200). Si la connaissance date du 2 nov. (AUD:3, 15), le délai de 72 heures pour notifier la CNIL expire le **5 nov.**, à une heure inconnue [ES] (rj-R4:207, corr. ver-R4 n° 7).
3. **Aucune base contractuelle** : aucun contrat, aucune facture, aucune entité payeuse identifiée [FV négatif] (OFF:29 ; syn-P:101-104).

---

## 1. Verdict en trois phrases

1. Marwin ne doit pas proposer aujourd'hui l'accompagnement de six mois à 15 000 ou 30 000 € HT par mois : aucune parole directe de GianLuca Carlone, aucune entité payeuse et aucun contrat ne l'appuient, la formule renforcée demande 140 à 145 % du temps disponible des deux associés, et le seul actif livré, le CRM, est exposé dans un dépôt public.
2. La bonne entrée est un **cadrage court vendu au forfait** (environ 6 000 € HT, 3 à 4 semaines, moitié à la commande) à une entité identifiée, précédé d'une remise en ordre non facturée (fuite de données, documents, structure, pacte) et suivi, seulement si le cadrage est payé et validé, d'un **pilote de huit semaines** (un socle de pilotage et un seul lot) qui mesure l'adoption et les résultats.
3. Un **pilotage récurrent borné** (un socle facturé au périmètre, des lots devisés à part, environ 8 000 à 10 000 € HT par mois et au plus 12 JP facturables dans le scénario central) ne vient qu'au quatrième mois, sur décision écrite de GianLuca prise sur pièces ; sans entité payeuse, acompte et accès dans les délais, Marwin reporte ou refuse plutôt que de continuer à travailler gratuitement.

---

## 2. Diagnostic en dix points

| N° | Constat | Code | Source | Ce que cela impose à la stratégie |
| --- | --- | --- | --- | --- |
| 1 | **Le besoin n'est pas démontré.** Aucune pièce ne contient une parole directe de GianLuca Carlone. Les « vingt jours par mois » lui sont attribués dans une version et à Morgan dans l'autre, issues du même brief. L'offre est passée d'une version « limitée à quatre jours mensuels » à 20 puis 40 JP en une semaine, sans demande tracée. | [DR] ; [FV négatif] | syn-S:38 ; ACC:7 ; syn-S PER-1 (:235) et DIS-1 (:254) ; syn-P:227 | Vendre d'abord un **test du besoin**, et le faire payer : un refus de payer un cadrage est déjà une réponse. |
| 2 | **Il n'y a ni acheteur ni base contractuelle.** Aucun contrat, aucune facture, aucune entité payeuse. Les lieux (Vieux Relais, le M, « six bâtiments ») n'ont ni propriétaire ni exploitant établis. Un patrimoine déclaré n'est pas une trésorerie. | [FV négatif] ; [DR] | OFF:29 ; syn-P:101-104, 280 ; syn-S U01 (:349) | Toute proposition nomme l'entité, le signataire, le payeur et le valideur (règle de prudence, syn-P:306). |
| 3 | **La capacité est plus faible que l'offre.** Capacité facturable réaliste : 7 à 12 JP par mois, 20 au mieux. La base de 20 JP demande environ 80 % du temps disponible des deux associés (« pas un mi-temps »). Le renforcement à 40 JP en demande 140 à 145 %. L'« ancre » à 46 JP est impossible. | [ES] | syn-C:69-70, 228-230 | Plafonner l'engagement de la première année à environ **12 JP facturables par mois**. |
| 4 | **Ce qui est démontré, c'est la production, pas la vente.** Le CRM (500 fiches) et le dépôt BOJART (933 fichiers) prouvent une production rapide avec l'IA. Vente, encaissement, maintenance dans la durée et coordination de prestataires ne sont démontrés par aucune réalisation. Côté OLSEN : 36 propositions et 72 brouillons préparés, aucun envoyé. | [FV] ; [DR] | syn-C:67, 97 ; NOTE:9 | Le premier objectif est **un encaissement et une réception**, pas un nouveau livrable. Arrêter toute production non commandée. |
| 5 | **Une fuite de données probable pèse sur le seul actif livré.** Dépôt FinanceScope/CRM-Carlone public au 4 nov. à 16 h 19 [DR] ; ≈ 800 à 931 numéros et 206 e-mails selon la copie et la méthode [ES] ; responsable de traitement non désigné [IN] ; délai de 72 h expirant le 5 nov. si la connaissance date du 2 nov. [ES]. | [HY fort] ; [ES] ; [IN] | syn-D:614-637 ; rj-R4:200, 207 ; ver-R4 n° 7 ; syn-S AVA-11 (:311) | **Préalable absolu**, traité sans facturation (l'exposition est de notre fait). Aucune donnée réelle dans un processus tant que ce n'est pas réglé. |
| 6 | **Les documents destinés au client se contredisent.** Le retrait de Medhi et de BOJ.ART n'est appliqué qu'au diaporama en ligne. Restent : l'option création (OFF:22), STRATES v1.1, le vernissage, le PDF de 13 pages de la PR n° 1. L'option laboratoire reste dans le diaporama, alors que son geste robotique « devient ce premier trait » de STRATES (OFF:84). V5 et une lettre portent l'ancienne erreur de prénom. | [FV] ; décision [DR] | `deck.json:7` ; syn-S:40, 65-69 ; syn-P:487-496 ; syn-D:309 | Une seule version de l'offre, datée, **avant tout rendez-vous**. |
| 7 | **Le prix n'est pas justifié, et il est proche du coût.** Le taux de 750 € HT s'est durci (« On ajuste le périmètre […] pas le taux », OFF:18) sans justification nouvelle. Recalcul : le coût complet d'une JP facturable vaut environ 590 à 740 € dans le scénario central et 750 à 960 € dans le prudent, pour une rémunération modeste. Le marché du temps partagé vend 2 à 8 jours par mois, pas 20. | [ES] ; [HY] | syn-S REM-1 (:263) ; § 4.1 ; rj-R6:404, 445 | Vendre au **forfait** (par livrable, par périmètre) ; garder 750 € comme référence interne de chiffrage, sans remise. |
| 8 | **Le calendrier de paiement se contredit.** Mois 2 à 6 : « règlement sous sept jours après facture de fin de mois » (ACC:57, 29 oct.) contre « d'avance, en début de mois » (OFF:19, 195 ; `paiement.html:26`). Le titre « payé d'avance » (`paiement.html:4`) couvre un premier mois soldé à terme échu (`paiement.html:18`). | [FV] | syn-S PAY-2 et PAY-3 (:279-280) | Trancher **par type de prestation** (§ 5). |
| 9 | **La structure n'est pas prête.** Marwin n'est pas immatriculée. La SARL, référence « provisoire » du 30 oct., est traitée en aval comme une décision. Ni pacte, ni parts, ni rôles écrits. Rien ne montre que Mathys ait validé l'offre ni le retrait de Medhi. | [FV] ; [IN] | V5 p. 17 ; syn-D:44-47 ; syn-S ASS-5 (:326), U07 (:355) | Aucun encaissement avant l'immatriculation ; pacte signé avant le contrat client. |
| 10 | **Le risque est concentré sur deux personnes.** GianLuca serait client, bailleur, employeur, investisseur et financeur de R&D [DR]. Morgan est le point de défaillance unique et mène en parallèle une dizaine d'autres projets [FV pour la liste]. La disponibilité de Mathys est inconnue [IN]. | [DR] ; [FV] ; [IN] | syn-P:308-320 ; NOTE § A-B ; syn-C:73, 118 | Un accord par sujet ; **seulement « client » pendant au moins 12 mois** ; disponibilités nominatives écrites ; second client. |

---

## 3. Objectifs possibles et objectif principal recommandé

### 3.1 Cinq objectifs possibles

| Objectif | Description | Ce qui le rend attractif | Ce qui le fragilise | Verdict S1 |
| --- | --- | --- | --- | --- |
| **O1. Pilotage global tout de suite** | L'ambition des archives : 20 ou 40 JP par mois, six mois, 90 000 à 180 000 € HT [PR] (OFF:13-16) | Revenu rapide et élevé, si le client signe | Besoin, payeur et capacité non établis (diagnostic 1 à 3) ; tout est dépendant d'une seule décision de GianLuca | **Écarté pour l'instant.** Reste une cible à 12-24 mois, à atteindre par paliers. |
| **O2. Démarrage progressif payé** | Cadrage payé, puis pilote de 8 semaines, puis socle récurrent et lots | Chaque palier est petit, payé, réceptionné et réversible ; GianLuca décide sur pièces | Revenu modeste la première année ; demande de la discipline (ne plus rien produire gratuitement) | **Recommandé** (§ 3.2). |
| **O3. Monétiser d'abord le CRM** | Faire vendre des œuvres aux entreprises de la Nièvre grâce au CRM et à l'article 238 bis AB | Actif déjà construit ; besoin rapporté le plus précis (COP:13) [DR] | Fuite à traiter ; structure vendeuse, avis fiscal écrit et appelant inconnus ; ventes hors du contrôle de Marwin ; une commission sur ventes ferait de Marwin un intermédiaire (LCB-FT, droit de suite) [HY] (syn-P:351) | **Lot possible du pilote**, jamais une rémunération sur les ventes. |
| **O4. Indépendance d'abord** | Construire une offre reproductible et trouver un second client ; GianLuca comme référence | Réduit la dépendance (diagnostic 10) | Sans première relation payante, pas de référence à montrer | **Objectif secondaire obligatoire** : plancher de prospection protégé de 1,5 à 2,5 JP par mois (syn-C:185, 267). |
| **O5. Salariat chez GianLuca** | Souhait exprimé par Morgan (« Je préfère être prestataire ou salarié », R:248) [DR] | Revenu stable | Intention du client inconnue [IN] ; risque de requalification et conflit d'intérêts si cumul avec Marwin (syn-D:332-348, 395-408) | **Écarté pendant au moins six mois.** |

### 3.2 Objectif principal recommandé [PR]

> **D'ici début février 2027 (90 jours)**, signer et encaisser un premier contrat avec une entité identifiée de GianLuca Carlone, livrer un cadrage accepté par écrit et obtenir sa décision sur un pilote de huit semaines. **D'ici début mai 2027 (6 mois)**, démontrer sur pièces qu'un pilotage borné lui est utile (décisions préparées et prises, un lot réceptionné, outil réellement utilisé) et qu'il couvre le coût complet de Marwin, sans dépasser 12 JP facturables par mois ni 85 % d'occupation des associés.

Il réunit les quatre exigences de la demande (DEMANDE § 10) : résultat utile pour GianLuca (vision et décisions préparées), activité rentable pour Marwin (prix au moins égal au coût complet, § 4.1), capacité soutenable (plafond de JP), preuves pour poursuivre (critères de réception et indicateurs, § 9).

### 3.3 Ce qui dépend de Marwin, de GianLuca et de tiers

| Sous le contrôle de Marwin | Dépend de GianLuca Carlone | Dépend de tiers |
| --- | --- | --- |
| Traiter la fuite (avec un avocat ou un DPD) et en documenter la décision | Désigner l'entité qui signe, paie et valide | Avocat ou DPD : avis sur la notification |
| Mettre en cohérence les documents et arrêter le travail gratuit | Accepter de payer un cadrage, et le payer à l'échéance | Expert-comptable : simulation SAS / SARL, TVA, paie |
| Constituer la SAS, signer le pacte, souscrire la RC professionnelle | Fournir accès, documents et un délégué dans les 10 jours ouvrés | Greffe : délai d'immatriculation [HY] |
| Écrire les disponibilités nominatives et les tenir | Choisir trois priorités et répondre aux demandes de décision | Quali Contact, si un lot CRM est choisi |
| Qualité, délais et contrôle des livrables ; mesure des temps | Adopter les outils (registre, comptes rendus) | Conseil fiscal de GianLuca pour tout argument 238 bis AB |
| Prix, plafonds de capacité, refus des demandes hors périmètre | Décider de la suite (pilote, socle) | Région : aide au conseil éventuelle, à déposer avant signature [DR] |
| Prospection d'un second client | Ventes d'œuvres, ouverture de la galerie, rachats de lieux | Medhi : réponse au retrait |

Les indicateurs de résultat qui dépendent de GianLuca (ventes, décisions, rendez-vous obtenus) sont suivis à part de ceux que Marwin contrôle (qualité, délais, coût par résultat accepté), comme le propose syn-C:812.

---

## 4. Architecture des offres

### 4.0 Six principes

1. **Pas d'abonnement général.** On revient à l'architecture « contrat-cadre et fiches de mission » du 30 oct. (V5 p. 2, 4), perdue le 2 nov. (syn-S PER-6, :240). Chaque prestation a son bon de commande, son prix, sa réception et sa sortie.
2. **Un bon de commande par lot et par entité** cliente (scénarios S1 à S4 de syn-P:296-304).
3. **Le prix est fixé au livrable ou au périmètre ; le temps sert à mesurer, pas à vendre.** Le relevé des JP reste remis chaque mois, comme preuve et comme base de révision.
4. **Rien d'exploratoire sans financeur écrit**, budget plafonné et critère d'arrêt (STRATES, Éclosion, laboratoire : gelés, § 4.8).
5. **Marwin prépare, organise et coordonne ; elle n'exécute pas** l'administratif courant, la comptabilité, le conseil juridique ou fiscal, ni les obligations d'exploitant, d'organisateur ou de vendeur (syn-D:410-431 ; AUD:100).
6. **Marwin n'avance jamais d'argent pour le client** : achats, abonnements et prestataires sont commandés et payés par l'entité cliente, à son nom.

### 4.1 Coût complet d'une JP facturable et repères de marché

**Méthode [ES].** Coût complet d'une JP facturable = (rémunération chargée des associés au prorata de leur temps Marwin + frais fixes) ÷ JP facturables ÷ 0,9 (réserve de 10 % du chiffre d'affaires).
- Disponibilité de 17,5 JP par mois et par personne ; parts du temps consacrées à Marwin et JP facturables des scénarios de syn-C:170-190.
- Rémunération cible de 2 500 € nets avant IR par équivalent temps plein Marwin (le « plancher » de OFF:112-114), ou 3 660 € (base « tout en rémunération », OFF:110).
- Coefficient coût / net : 1,70 à 1,90 en SAS (assimilé salarié) ; 1,40 à 1,46 en SARL (TNS) (syn-D:98, 112) [HY].
- Frais fixes de Marwin : 1 500 à 2 500 € par mois (expert-comptable, RC professionnelle, logiciels et IA de 150 à 1 000 € par mois selon rj-R6:505, banque, déplacements, conseil ponctuel) [HY].

| Scénario de disponibilité | JP facturables / mois | Coût complet par JP (SAS, 2 500 € nets / ETP) | Idem, 3 660 € nets / ETP | CA mensuel HT qui couvre ce coût (SAS, 2 500 €) |
| --- | --- | --- | --- | --- |
| Prudent : Morgan 50 %, Mathys 25 % | ≈ 7 | ≈ 750 à 960 € | ≈ 980 à 1 230 € | ≈ 5 200 à 6 700 € |
| Central : Morgan 65 %, Mathys 50 % | ≈ 12 | ≈ 590 à 740 € | ≈ 800 à 970 € | ≈ 7 100 à 8 800 € |
| Haut : 90 % chacun | ≈ 20 | ≈ 510 à 610 € | ≈ 710 à 830 € | ≈ 10 200 à 12 300 € |

En SARL, le coût par JP baisse d'environ 10 à 15 % (central : ≈ 510 à 620 € à 2 500 € nets). Sans aucune rémunération, le seuil de couverture des seuls frais et de la réserve est d'environ 1 700 à 2 800 € HT par mois [ES].

**Lecture.** Le taux de 750 € HT n'est pas une marge confortable : il couvre le coût complet dans le scénario central avec une rémunération modeste, et à peine dans le scénario prudent. Toute remise sur ce taux fait travailler à perte. C'est l'inverse de ce que suggérait « l'ancre » de négociation.

**Repères de marché** (aucun organisme officiel ne publie de prix de conseil ; statut de chaque source indiqué) :

| Repère | Valeur | Statut | Source |
| --- | --- | --- | --- |
| Chef de projet senior en région | ≈ 570 à 760 € HT / jour | [ES] transposé d'une étude Hays relayée (secondaire) | rj-R6:54-62, 107-108 |
| Moyenne « gestion de projets », freelances tech | 698 € ; seniors tous métiers : 643 € | [FV] étude privée Kicklox (663 réponses) | ver-R6 n° 5 |
| Développeur en région | ≈ 405 à 585 € | [ES] | rj-R6:62 |
| DAF à temps partagé / management de transition | 800 à 1 200 € / jour ; ≈ 1 330 € / jour | [DR] sources de vendeurs ou secondaires | rj-R6:412-414 |
| Format courant du temps partagé | 2 à 8 jours par mois | [HY] d'après ces sources | rj-R6:404 |
| Diag Data IA (dispositif public) | Devis plafonné à 10 000 € HT pour 8 jours ; 6 000 € HT à la charge de l'entreprise (40 % pris en charge) ; 1 250 € / jour est un **maximum calculé**, pas un prix constaté | [FV] ; [ES] | ver-R6 n° 6 |
| Assistant non cadre dans la Nièvre | Coût employeur 2 250 à 2 810 € par mois, soit ≈ 125 à 160 € par jour travaillé | [ES] API URSSAF recalculée | rj-R6:126 ; ver-R6 n° 3 ; calcul S1 |
| Chef de projet cadre salarié en région | ≈ 340 à 360 € par jour (coût employeur) | [ES] | rj-R6:167 |

**Conséquences.** Le prix d'une journée de **coordination et de préparation des décisions** se défend entre 750 et 900 € HT, si Marwin montre des références de niveau senior [HY] (rj-R6, question 1). Celui d'une journée d'**exécution administrative** ne se défend pas (125 à 160 € pour un assistant salarié) : elle est exclue. Le **volume** de 20 JP par mois est atypique : le marché soutient mieux un cadrage court, puis quelques jours de pilotage par mois et des lots séparés (rj-R6:445).

### 4.2 Préalable non facturé : remise en ordre (semaines 0 à 4)

| Rubrique | Contenu |
| --- | --- |
| Bénéficiaires | Marwin, et indirectement GianLuca Carlone et les personnes dont les données sont exposées |
| Problème | Fuite de données probable ; documents contradictoires ; structure, pacte et disponibilités non écrits ; travail gratuit qui s'accumule (scénario S5, syn-P:304) |
| Résultat | (1) Décision sur la notification à la CNIL prise **avant le 5 nov.** avec un avocat ou un DPD, ou retard motivé ; dépôt rendu privé et vérifié ; copies contrôlées ; fiche de violation ; GianLuca informé par écrit (syn-D:631-637). (2) Une seule version de l'offre ; PR n° 1 fermée ou son PDF marqué « historique » ; offre écrite, STRATES v1.1, vernissage et diapositive laboratoire marqués « retirés » ; aucune occurrence de l'ancienne erreur de prénom (« John-Lucas » [sic, lire GianLuca]) dans un document client. (3) Décision écrite de Morgan et Mathys sur Medhi et BOJ.ART ; message écrit à Medhi. (4) Fiche des disponibilités nominatives et principes du pacte. (5) Statuts et pacte prêts à signer. (6) Vérification qu'aucun document de Marwin ou de Carlone ne reste dans le dépôt public BOJART (syn-C:829). |
| Capacité | 9 à 17 JP sur les mois 0 à 2 (syn-C:216-220), dont 3 à 6 pour la fuite et la conformité minimale |
| Coût | Temps des associés non rémunéré : ≈ 5 300 à 12 600 € au coût complet central [ES]. Sorties d'argent : statuts et pacte 2 000 à 5 000 € HT, formalités quelques centaines d'euros, RC professionnelle [IN], conseil sur la fuite [IN] ; soit environ 3 000 à 7 000 € à financer par le capital [ES] (syn-D:180-185) |
| Facturation | **Aucune.** La conformité du CRM ne se facture pas : l'exposition est de notre fait (syn-P:353) |
| Condition de sortie | Toutes les conditions du § 10.1 sont remplies, sauf l'acompte |

### 4.3 Offre A : cadrage « Inventaire, priorités, mandat »

| Rubrique | Contenu |
| --- | --- |
| **Client** | L'entité de GianLuca Carlone désignée comme « chef de file » (dénomination, SIREN, signataire habilité). Payeur et valideur : la même entité, ou celles qu'elle désigne par écrit |
| **Problème** | Le portefeuille n'est connu qu'à travers Morgan ; aucune liste d'entités, de lieux, de priorités, de budgets ou d'accès ; Marwin ne peut ni dimensionner ni chiffrer ; GianLuca ne peut pas comparer |
| **Résultat** | 1. Inventaire **validé par écrit** des entités, lieux, projets, interlocuteurs et accès. 2. Trois priorités à 90 jours, choisies par GianLuca, chacune avec un objectif mesurable, un budget indicatif et un responsable côté client. 3. Carte des rôles par projet : qui est exploitant, organisateur, vendeur, responsable de traitement ; quels professionnels consulter (syn-D:516-518). 4. Proposition chiffrée de pilote (socle et un lot) et projet de mandat écrit (actes, plafonds, délégué). 5. Registre des décisions ouvert pendant le cadrage (premier essai du pilote P1, syn-C:695-708) |
| **Périmètre** | Deux entretiens (un de 2 à 3 h sur place, une restitution d'1 h 30) ; jusqu'à 15 pièces fournies par le client ; un aller-retour de corrections. Un associé mène, l'autre contrôle. C'est la reprise du « premier forfait » borné du 25 oct. (METH:77 ; R:1469) |
| **Exclusions** | Conseil juridique ou fiscal ; étude de rentabilité détaillée d'un établissement ; tout contact avec des tiers ; usage du CRM sur des données réelles ; production de supports, de catalogue ou d'outils ; visites de plusieurs lieux au-delà d'une journée |
| **Dépendances** | Entité identifiée et bon de commande signé ; Marwin immatriculée ; acompte encaissé ; pièces et accès fournis sous 10 jours ouvrés ; GianLuca disponible pour deux entretiens ; préalable du § 4.2 terminé |
| **Capacité** | 7 à 9 JP [ES] : préparation 1 ; entretien sur place et trajet 1,5 ; analyse des pièces et inventaire 2 ; carte des rôles 1 ; priorités, proposition de pilote et mandat 1,5 ; restitution 0,5 ; contrôle et corrections 1 |
| **Durée** | 3 à 4 semaines à partir de l'acompte et des pièces |
| **Prix proposé** | **6 000 € HT forfaitaire** (7 200 € TTC), deux trajets compris. Plancher interne : 5 000 € HT ; en dessous, on réduit le périmètre, pas le prix |
| **Justification** | *Coût complet* : 8 JP × 590 à 740 € ≈ 4 700 à 5 900 € (central) ; le prix couvre le coût, sans plus. *Marché* : du même ordre que le reste à charge du Diag Data IA (6 000 € HT pour 8 jours, devis plafonné à 10 000 €) [FV] ; effectivement ≈ 670 à 860 € par JP, dans la fourchette d'un chef de projet senior en région [ES]. *Valeur* : évite d'engager 90 000 € HT à l'aveugle ; GianLuca garde l'inventaire, la carte des rôles et les priorités, même s'il s'arrête là |
| **Coûts directs** | Déplacements [IN] ; outils négligeables (abonnements professionnels déjà comptés dans les frais) |
| **Marge** | ≈ 0 à 20 % pour 8 JP au coût central [ES] ; négative si le cadrage dépasse 8 JP ou au coût prudent. **Volontairement faible : c'est un test du besoin, vendu une seule fois** |
| **Réception** | Remise du dossier, puis restitution. Réserves écrites sous 10 jours ouvrés, corrigées une fois. Le silence vaut livraison pour la facturation du solde, **jamais** approbation d'une suite (§ 8.3) |
| **Paiement** | 50 % à la commande (le travail démarre à l'encaissement) ; 50 % à la remise, payable sous 8 jours |
| **Conditions de poursuite** | Cadrage payé à l'échéance ; inventaire validé par écrit ; au moins une priorité confiée avec un budget ; accès réellement fournis ; occupation des associés ≤ 85 %. À défaut : arrêt propre, GianLuca garde le dossier |

### 4.4 Offre B : pilote de huit semaines « un socle et un lot »

| Rubrique | Contenu |
| --- | --- |
| **Client** | L'entité chef de file pour le socle ; l'entité concernée pour le lot (bon de commande séparé si elle diffère) |
| **Problème** | Savoir, avant tout engagement récurrent, si un pilotage délégué fonctionne vraiment : décisions préparées, suivies et prises ; outil utilisé ; un résultat concret livré sur une priorité |
| **Résultat** | *Socle pilote* : registre des décisions et échéances ; compte rendu en moins de 24 h ouvrées ; point hebdomadaire (un seul associé, syn-C:210) ; deux comités mensuels ; tableau de bord des trois priorités. *Lot* : un livrable du catalogue C (§ 4.5), réceptionné. *Mesure* : référence de temps relevée pendant les deux premières semaines, puis temps humain total, corrections et adoption |
| **Périmètre** | Socle : 3 à 4 JP par mois. Lot : 5 à 7 JP |
| **Exclusions** | Exécution administrative ; astreinte ; tout engagement de dépense (mandat de dépense à 0 €) ; données personnelles réelles sans les préalables (syn-C:678-685) ; second lot sans bon de commande |
| **Dépendances** | Délégué nommé côté client ; réponse aux demandes de décision sous 5 jours ouvrés ; accès ; préalables propres au lot (pour un lot CRM : conformité, structure vendeuse, avis fiscal écrit, appelant désigné) |
| **Capacité** | ≈ 13 JP sur 8 semaines, soit 6 à 7 JP par mois [ES] |
| **Durée** | 8 semaines, sans tacite reconduction |
| **Prix proposé** | **Socle pilote : 3 500 € HT par mois** (deux mois, 7 000 € HT ; plancher 3 000 €). **Lot : au devis** (≈ 4 500 à 6 000 € HT). Total ≈ 11 500 à 13 000 € HT |
| **Justification** | *Coût* : 3,5 JP × 590 à 740 € ≈ 2 100 à 2 600 € par mois. *Marché* : temps partagé de quelques jours par mois, 4 000 à 8 000 € pour un DAF [DR] (rj-R6:412-413). *Valeur* : décisions préparées et tracées ; adoption mesurée avant d'engager davantage |
| **Coûts directs** | Deux sièges d'IA professionnels et un espace de registre : ≈ 60 à 90 $ par mois [ES] (syn-C:705) ; déplacements [IN] |
| **Marge** | Socle : ≈ 25 à 40 % ; lot : ≈ 15 à 35 % si l'estimation tient [ES] |
| **Réception** | Critères du pilote P1 (syn-C:702-707) : 100 % des décisions avec responsable, date et source ; compte rendu en moins de 24 h ouvrées dans au moins 90 % des cas ; au moins 80 % des comptes rendus commentés sous 3 jours ouvrés ; registre consulté chaque semaine. Lot : critères écrits du devis |
| **Paiement** | Socle d'avance, le 1er du mois (premier mois à la signature) ; lot 40 % à la commande, 60 % à la réception sous 8 jours |
| **Conditions de poursuite** | Critères d'adoption tenus 4 semaines de suite ; aucune erreur critique ; paiements à l'heure ; demande écrite de GianLuca de poursuivre ; occupation ≤ 85 %. Critères d'abandon : relecture et corrections au-delà de 50 % du temps de référence pendant 4 semaines, ou registre non consulté après 4 semaines (syn-C:707) |

### 4.5 Offre C : lots de production devisés

**Règle de devis [PR].** Prix = JP estimées × 800 € HT + provision de risque de 10 à 15 %, au forfait ; plancher de 700 € HT par JP estimée. Paiement 40 % à la commande, 60 % à la réception (jalons 40 / 30 / 30 au-delà de 8 JP). Tout dépassement non causé par le client reste à la charge de Marwin dans la limite de la provision ; au-delà, un avenant signé **avant** le travail. Chaque lot porte ses critères de réception, ses exclusions et le régime des droits (cession des livrables propres au client au paiement complet, syn-D:498).

| Lot candidat | Résultat | JP [ES] | Prix indicatif HT [ES] | Préalables | Exclusions |
| --- | --- | --- | --- | --- | --- |
| **C1. Catalogue privé des œuvres** (20 à 30 œuvres réelles) | Fiches complètes et exportables (photo, provenance, emplacement, mouvements) | 4 à 7 | 3 500 à 6 000 € | Œuvres réelles, photos et provenance fournies (syn-P:443-444) | Expertise, authentification, photographie professionnelle (sous-traitée et payée par le client), valorisation fiscale |
| **C2. Pilote CRM sur 20 comptes** | Fiches qualifiées et sourcées, script validé, résultats d'appel réimportés, mesures de joignabilité et de rendez-vous | 5 à 7 | 4 500 à 6 000 € | Fuite traitée ; responsable de traitement ; contrat de l'article 28 ; structure vendeuse nommée ; avis fiscal écrit ; appelant désigné (syn-C:714) | Les appels eux-mêmes, toute promesse fiscale non validée, toute commission sur les ventes |
| **C3. Faisabilité d'un premier événement sans robot** | Lieu, date, jauge, organisateur désigné, autorisations avec dates de dépôt, budget, devis | 4 à 6 | 3 500 à 5 000 € | Lieu et organisateur identifiés ; délai de deux mois pour une demande GN 6 (syn-P:457) | L'organisation elle-même, la sécurité du public, le format « signature » avec bras robotisé |
| **C4. Tableau des lieux et de leurs obligations** | Par lieu : propriétaire, exploitant, licences, classement ERP, calendrier des démarches, à faire valider par les professionnels | 3 à 5 | 2 500 à 4 000 € | Inventaire du cadrage validé | Le rôle d'exploitant ; toute démarche au nom du client sans mandat |
| **C5. Échange de fichiers avec Quali Contact** | Spécification dans les deux sens ; essai sur 10 fiches fictives ; correspondance des champs validée par Quali Contact | 3 à 4 | 2 500 à 3 500 € | Contrat entre l'entité de GianLuca et Quali Contact ; logiciel et format connus (syn-P:372) | Tout développement avant de connaître le format (leçon du module Hermes360) |

**Ordre recommandé pour le lot du pilote** : C1 ou C4 d'abord (concrets, peu risqués, sans données de prospects) ; C2 seulement quand tous ses préalables sont réunis ; C5 seulement si Quali Contact est engagé.

### 4.6 Offre D : socle de pilotage récurrent (à partir du mois 4)

| Rubrique | Contenu |
| --- | --- |
| **Client** | Entité chef de file ; refacturation interne entre entités de GianLuca à faire valider par son expert-comptable [HY] (syn-P:300) |
| **Problème** | Garder une vision claire du portefeuille et des décisions préparées sans gérer chaque détail (ACC:13) [DR] |
| **Résultat** | Registre des décisions et échéances à jour ; tableau de bord ; point hebdomadaire ; comité mensuel ; 2 à 4 dossiers de décision par mois ; coordination des prestataires sans commandement direct (syn-D:360-362) ; suivi de **N projets actifs** (N = 2 inclus) ; rapport mensuel avec le relevé des JP |
| **Périmètre** | « Un socle et N projets » : la limite d'encours est écrite au contrat (syn-C:256). Toute demande nouvelle remplace un projet actif ou devient un lot |
| **Exclusions** | Production (lots C), urgences hors plages (astreinte à chiffrer à part si un jour elle est demandée), exécution administrative, dépenses hors mandat, obligations réglementées |
| **Dépendances** | Pilote réussi ; mandat écrit signé ; délégué nommé ; accès maintenus |
| **Capacité** | 4 à 5 JP par mois, plus 1 à 1,5 JP par projet supplémentaire (syn-C:245-248) |
| **Durée** | 3 mois, renouvelables par accord écrit ; préavis réciproque d'un mois ; révision trimestrielle |
| **Prix proposé** | **4 500 € HT par mois pour « socle + 2 projets »** ; + 1 000 € HT par projet suivi en plus. Plancher : 3 500 € HT |
| **Justification** | *Coût* : 4,5 JP × 590 à 740 € ≈ 2 650 à 3 350 € par mois. *Marché* : temps partagé de 2 à 8 jours par mois, 4 000 à 8 000 € par mois [DR]. *Valeur et responsabilité* : continuité (binôme de secours), traçabilité, sécurité des outils, réversibilité ; le prix porte sur un périmètre et un niveau de service, pas sur des heures |
| **Coûts directs** | Sièges d'IA et outils de registre (≈ 60 à 150 € par mois) [ES] ; les abonnements du client sont à son nom et à sa charge |
| **Marge** | ≈ 25 à 40 % [ES] |
| **Réception** | Rapport mensuel ; indicateurs : décisions préparées à temps ≥ 70 % à 90 jours puis ≥ 85 % à 6 mois ; délai de compte rendu ; délai de décision suivi (syn-C:802-811) |
| **Paiement** | D'avance, le 1er du mois |
| **Conditions de poursuite** | Indicateurs tenus ; paiements à l'heure ; aucun incident critique ; occupation ≤ 85 % ; plancher de prospection respecté |

### 4.7 Offre E : exploitation d'un processus (à partir du mois 7, si un pilote l'a prouvé)

| Rubrique | Contenu |
| --- | --- |
| **Exemples** | Tenue et qualification du CRM (fiches à jour, résultats d'appels réimportés, oppositions appliquées, export et sauvegarde testés) ; recherche documentaire avec citations sur le corpus du client (pilote P3, syn-C:727-740) |
| **Résultat** | Un service régulier avec des niveaux de qualité écrits et une reprise manuelle testée |
| **Capacité** | 1 à 4 JP par mois selon le volume [ES] |
| **Prix proposé** | Forfait minimum mensuel de 1 000 à 1 500 € HT (maintenance, sauvegardes, journal), plus un **prix par résultat accepté** (par exemple de l'ordre de 40 à 70 € HT par fiche qualifiée acceptée [HY]), fixé après la mesure de référence du pilote, figé pour 6 mois |
| **Justification** | Le client paie un résultat contrôlé, pas des heures ; Marwin garde le gain d'automatisation pendant la période et le partage au renouvellement (§ 4.11) |
| **Paiement** | Minimum d'avance ; variable en fin de mois sur relevé, sous 15 jours |
| **Conditions** | Critères du pilote tenus 2 à 3 mois ; sauvegarde et restauration testées ; responsable et maintenance chiffrés au contrat (syn-C:693) |

### 4.8 Ce qui est retiré, gelé ou exclu

| Élément des archives | Décision S1 | Raison | Source |
| --- | --- | --- | --- |
| Renforcement à 40 JP (30 000 € HT) et « ancre » à 46 JP | **Retiré** de toute présentation | 140 à 145 % du temps disponible des deux associés | syn-C:229-230 |
| Formule de base « 20 JP, environ un mi-temps » | **Retirée** comme offre d'entrée | Environ 80 % du temps de chacun, pas un mi-temps | syn-C:228 ; `formules.html:13` |
| Option laboratoire (30 000 € HT, 13 500 € d'honoraires) | **Retirée** du diaporama | Plus d'objet depuis le retrait de STRATES (OFF:84) ; aucun financement acté | syn-P:528-541 |
| Option création et STRATES ; Éclosion | **Gelées** | Retrait de Medhi ; aucun budget propre ; aucune compétence robotique démontrée | syn-P:505-522 |
| Vernissage « signature » avec bras robotisé | **Reporté sans date** | Robot au contact du public ; dépendance à Medhi ; délais administratifs | syn-P:446-462 |
| « Copilote Jarvis » comme produit nommé | **Suspendu** | Propriété du code et du nom non réglée | syn-S PRO-2 (:290) |
| DGX Spark, IA locale | **Exclues** | Aucun des onze processus ne la demande | syn-C:670 |
| Exploitation du cabaret et des lieux | **Exclue** | Obligations nominatives de l'exploitant | syn-P:473 |
| Exécution administrative, comptabilité, conseil fiscal ou juridique | **Exclus** | Activités réglementées ; prix non défendable | syn-D:410-421 ; AUD:100 |
| Astreinte 24 h / 24, couverture 30 jours sur 30 | **Exclue** | Non tenable à deux | ACC:105 |
| Rémunération sur les ventes d'œuvres | **Exclue** | Statut d'intermédiaire, LCB-FT, droit de suite [HY] | syn-P:351, 561 |
| « Mener les huit propositions de front » | **Exclu** | 1 à 1,5 JP de production par proposition et par mois | syn-C:231 |

### 4.9 Règle anti-double facturation [PR]

1. **Chaque JP est imputée à un seul bon de commande** (cadrage, socle, lot ou exploitation), avec un code visible dans le relevé mensuel remis au client.
2. **Le socle ne contient aucune production** ; un lot ne peut pas être exécuté sur le temps du socle, et le socle ne peut pas absorber un dépassement de lot.
3. **Un outil construit dans un lot n'est jamais refacturé** dans le socle ou dans un autre lot ; sa maintenance n'est facturée que si un contrat d'exploitation (offre E) la prévoit.
4. **Les composants génériques de Marwin** (méthodes, modèles, briques réutilisables) sont concédés sous licence gratuite pour l'usage interne du client ; ils ne sont pas facturés comme développement (syn-D:497).
5. **Le CRM déjà construit** n'est facturé ni rétroactivement, ni à nouveau dans un lot. Son régime (licence d'usage gratuite ou cession) est écrit avant tout lot CRM, une fois la propriété réglée entre Morgan et Mathys (syn-D:494 ; syn-S REM-5).
6. **La remise en conformité des données** et la correction des non-conformités relevées à la réception ne sont jamais facturées.
7. **Aucun dépassement sans avenant signé avant le travail** ; aucun travail gratuit au-delà.
8. Cela rend opérationnelle la promesse déjà affichée « Aucun travail facturé deux fois » (`garanties.html:38` ; OFF:65).

### 4.10 Ce que devient le taux de 750 € HT

- **Il devient un taux de référence interne de chiffrage** : il sert à construire les devis, les avenants et le relevé. Il n'est plus l'unité de vente ni un « taux unique » affiché (`formules.html:30`) ; la phrase « On ajuste le périmètre et le nombre de jours, pas le taux » (OFF:18) disparaît du discours client.
- **Sa justification est d'abord le coût** : il correspond au coût complet d'une JP facturable dans le scénario central, avec une rémunération modeste (≈ 590 à 740 €, § 4.1). Il se situe dans le haut de la fourchette d'un chef de projet senior en région, sous les repères de direction à temps partagé et de management de transition [ES/DR].
- **Il ne s'applique pas à l'exécution** : administratif (125 à 160 € par jour pour un assistant salarié) exclu ; développement (405 à 585 € en région) vendu au livrable.
- **Il n'est jamais remisé**, ni contre un volume, ni contre une promesse d'investissement (OFF:149).
- **Il est révisé au mois 6** à partir du coût complet mesuré (JP réellement consommées, occupation, frais). S'il ne couvre pas le coût, on réduit le périmètre ou on relève les forfaits.
- **Il n'est défendable devant GianLuca qu'avec des références** démontrables des deux associés (rj-R6, question 1). Faute de références, le forfait protège mieux que le taux.

### 4.11 Rémunérer la responsabilité et la valeur quand l'automatisation réduit le temps

La règle du 29 oct. (« Les économies issues de l'automatisation permettent de réaffecter la capacité ou de revoir le forfait », ACC:66) a disparu le 2 nov., alors que la facturation restait au temps (syn-S REM-4, :266). Dans un modèle au temps, chaque gain réduit le chiffre d'affaires. Cinq mécanismes [PR] :

1. **Prix au livrable, au périmètre ou au résultat accepté, fixé pour la période contractuelle** (3 à 6 mois) à partir d'une référence mesurée **avant** l'automatisation (syn-C:757-763). Le gain obtenu pendant la période revient à Marwin.
2. **Partage du gain au renouvellement** : sur le gain mesuré (temps humain total par résultat accepté, corrections comprises), la moitié revient au client (baisse du prix unitaire ou volume en plus), la moitié reste à Marwin. Le calcul est remis avec le rapport trimestriel.
3. **Le socle paie une responsabilité, pas des heures** : continuité avec un binôme de secours, journal, sauvegarde et restauration testées, bouton d'arrêt, réversibilité (syn-C:833-884). Ces garanties ont un coût, même quand l'outil fait gagner du temps.
4. **Pas de variable sur les ventes d'œuvres**, ni sur des « économies » non mesurées. Aucun bonus la première année ; ensuite, un bonus éventuel ne porterait que sur des indicateurs que Marwin contrôle (délais, taux de réception au premier passage).
5. **Transparence** : les gains ne sont jamais présentés comme des heures manuelles fictives (ACC:66) ; l'indicateur « équivalent temps humain évité » est publié au client (syn-C:811).

---

## 5. Calendrier de paiement

### 5.1 La contradiction tranchée

Les deux versions des archives visaient un abonnement de six mois que S1 ne recommande pas. La règle retenue sépare trois logiques [PR] :
- **Capacité réservée** (socle de pilotage) : **payée d'avance**, le 1er du mois. Marwin réserve des personnes nommées ; le paiement d'avance protège contre une rupture et finance le mois. C'est la version du 30 oct. et du 2 nov. (OFF:19, 195), limitée au socle.
- **Livrables** (cadrage, lots) : **acompte à la commande, solde à la réception**. Le client paie ce qu'il reçoit ; Marwin n'est exposée que sur le solde d'un livrable.
- **Consommation variable** (prix unitaires, avenants) : **fin de mois sur relevé**, sous 15 jours. C'est le seul usage conservé de la version du 29 oct. (ACC:57).

Le titre « Un calendrier simple, payé d'avance » (`paiement.html:4`) et l'acompte de 7 500 € disparaissent avec la formule de six mois.

### 5.2 Échéancier par prestation

| Prestation | Facturation | Échéance | Le travail démarre | Exposition maximale de Marwin [ES] |
| --- | --- | --- | --- | --- |
| A. Cadrage | 50 % à la commande ; 50 % à la remise | Acompte : à réception de la facture ; solde : 8 jours | À l'encaissement de l'acompte | ≤ 3 000 € HT |
| B. Socle pilote | Mensuel, à échoir | Le 1er du mois (premier mois : à la signature) | À l'encaissement du premier mois | ≈ 0, ou ≤ 15 jours de socle en cas de retard |
| C. Lots | 40 % à la commande ; 60 % à la réception (40 / 30 / 30 au-delà de 8 JP) | 8 jours | À l'encaissement de l'acompte | ≤ 60 % d'un lot, soit ≈ 2 500 à 3 600 € HT |
| D. Socle récurrent | Mensuel, à échoir ; préavis d'un mois | Le 1er du mois | — | ≤ 15 jours de socle |
| E. Exploitation | Minimum à échoir ; variable en fin de mois | Minimum : le 1er ; variable : 15 jours | — | ≤ 1 mois de variable |
| Avenants, dépassements | Fin de mois | 15 jours | Après signature de l'avenant | — |
| Achats, abonnements, prestataires | **Jamais par Marwin** : au nom et aux frais de l'entité cliente | — | — | 0 |

**Exposition totale** dans le régime central : au plus ≈ 5 000 à 6 000 € HT de travail non payé à un instant donné (le solde d'un lot et quinze jours de socle) [ES].

### 5.3 Règles communes

- **Ordre** : immatriculation → contrat-cadre et bon de commande signés → facture d'acompte → encaissement → début du travail. Rien n'est encaissé avant l'immatriculation (syn-D:48, 260-261). Si l'entité de GianLuca veut utiliser l'aide régionale au conseil, le dossier doit être déposé **avant** la signature [DR] (R:755, 809) : on décale alors la signature, sans commencer le travail.
- **TVA** facturée dès la première facture ; elle est exigible à l'encaissement de chaque acompte (syn-D:299-300). Le cadrage coûte donc 7 200 € TTC au client.
- **Retard** : relance écrite le lendemain de l'échéance ; suspension des travaux non urgents 8 jours après une relance restée sans effet (OFF:207) ; résiliation possible à 30 jours. Pénalités d'au moins trois fois le taux légal (8,25 % au second semestre 2026) et indemnité de 40 € par facture ; escompte : néant (rj-R2:19, 393).
- **Sortie** : les mois payés d'avance non commencés sont remboursés au prorata ; les travaux engagés et la réversibilité sont dus (syn-S PAY-5 : cette règle manquait).
- **Ce qu'on ignore** : comment GianLuca paie, et quels délais pratique son entité [IN]. Le calendrier est une proposition à négocier, pas une hypothèse sur sa trésorerie.

### 5.4 Tests d'échec de trésorerie (scénario central, `plan.py`) [ES]

Hypothèses : capital libéré de 3 000 € ; frais de démarrage de 4 500 € ; frais fixes de 2 000 € par mois ; rémunération des associés à partir du mois 4 seulement (SAS, coefficient 1,8). Impôt sur les sociétés et TVA non modélisés.

| Test | Résultat simulé | Réponse prévue |
| --- | --- | --- |
| Référence (1 200 à 1 500 € nets chacun à partir du mois 4) | Point bas ≈ −1 500 € au mois 0 (les frais de démarrage dépassent le capital) ; trésorerie ≈ 21 000 à 31 000 € à la fin du mois 12 | Porter le capital ou l'apport en compte courant à 5 000 à 7 000 €, ou décaler une partie des frais |
| Retard de paiement de 30 jours à partir du mois 4 | Fin du mois 12 ≈ 22 000 € | Absorbé |
| Retard de 60 jours | Fin du mois 12 ≈ 14 000 € | Absorbé, à condition de suspendre comme prévu |
| Retard de 90 jours, si l'on continuait à travailler et à se payer | Point bas ≈ −8 000 € | **Interdit par la règle** : suspension à 8 jours après relance, arrêt de la rémunération |
| Rupture après le mois 4 | Trésorerie positive jusqu'au mois 8 environ, puis négative si les frais restent à 2 000 € | Arrêt de la rémunération à la fin du préavis ; frais ramenés à ≈ 1 000 € ; la réserve couvre alors environ six mois |
| Hausse des coûts d'IA (doublement Gemini au 1er déc. 2026 et au 1er janv. 2027, rj-R6:315-316 ; ver-R6 n° 11) | + 150 à + 1 000 € par mois au pire | Clause de révision ; deux fournisseurs configurés |
| Associé indisponible plusieurs semaines | Capacité facturable ramenée à ≈ 4 à 8 JP (syn-C:865) | Le socle est tenu par l'autre ; les lots sont reportés sans pénalité au-delà de 10 jours ouvrés |
| Dépassement d'un lot de 50 % | ≈ 2 000 à 2 500 € de temps non payé | Provision de risque, puis avenant ; pas de nouveau lot du même type avant correction |
| Abandon du projet artistique | Sans effet | STRATES et le laboratoire sont hors du chiffre d'affaires dans S1 |

---

## 6. Trois scénarios

Mois 1 = mois de signature du cadrage, au plus tôt décembre 2026, plus probablement janvier 2027 [HY]. Montants HT, hors TVA, avant impôt sur les sociétés. Simulations `plan.py` [ES].

| | **Prudent** | **Central** (recommandé comme base de pilotage) | **Ambitieux** |
| --- | --- | --- | --- |
| **Périmètre** | Cadrage ; puis socle léger « socle + 1 projet » à partir du mois 3 ; un lot par trimestre | Cadrage ; pilote de 8 semaines (socle et un lot) ; à partir du mois 4, socle « + 2 projets » et lots (≈ un lot de 5 000 à 6 000 € toutes les six semaines) | Cadrage élargi ; pilote avec deux lots ; à partir du mois 4, socle « + 3 projets », deux lots par mois et une exploitation (offre E) |
| **Capacité facturable** | 4 à 6 JP par mois | 10 à 11 JP par mois (plafond 12) | 17 à 19 JP par mois |
| **Disponibilité requise** | Morgan 50 %, Mathys 25 % | Morgan 65 %, Mathys 50 % | Environ 90 % chacun : Morgan arrête l'essentiel de ses autres projets ; 2 à 4 JP par mois sous-traités |
| **Prix et modalités** | Cadrage 6 000 € ; socle 3 000 € par mois ; lot ≈ 4 500 € | Cadrage 6 000 € ; socle pilote 3 500 € ; socle 4 500 € ; lots ≈ 4 000 € par mois en moyenne | Cadrage 7 500 € ; socle 5 500 € ; lots et exploitation ≈ 9 000 € par mois |
| **CA mensuel en régime** (mois 4 à 12) | ≈ 4 500 € | ≈ 8 500 € | ≈ 14 500 € |
| **CA sur 12 mois** | ≈ 50 000 € (variante basse : 6 000 € si GianLuca s'arrête après le cadrage) | ≈ 95 000 € | ≈ 155 000 € |
| **Rémunération possible** (nets avant IR, chacun, SAS, à partir du mois 4) | 0 à 600 € : Marwin est un complément de revenu | ≈ 1 200 à 1 600 €, selon la réserve | ≈ 2 400 à 2 650 €, après sous-traitance et réserve |
| **Seuil de rentabilité** (2 500 € nets par ETP) | ≈ 5 200 à 6 700 € par mois : non atteint | ≈ 7 100 à 8 800 € par mois : atteint de justesse | ≈ 10 200 à 12 300 € par mois : dépassé |
| **Réserve fin du mois 12** (avant IS) | ≈ 9 000 à 25 000 € selon la rémunération | ≈ 21 000 à 31 000 € | ≈ 35 000 à 50 000 € selon la sous-traitance |
| **Hypothèses clés** | GianLuca veut une aide limitée, sur une priorité ; Quali Contact non engagé ; associés gardant leurs autres revenus | Cadrage puis pilote payés à l'heure ; trois priorités réelles ; accès fournis ; second client en préparation | Plusieurs entités clientes ; adoption rapide ; un processus prouvé en exploitation ; second client signé |
| **Dépendance à GianLuca** | Faible en montant, forte en part si rien d'autre | Forte : à compenser par le second client | **Très forte** : le scénario ambitieux augmente la concentration du risque s'il n'est pas accompagné d'un second client |

**Lecture.** Le scénario central produit sur douze mois à peu près le chiffre d'affaires de l'offre de six mois des archives (90 000 € HT), mais en quatre paliers payés, avec une sortie possible à chaque palier. L'ambitieux ne rejoint le niveau de la « formule de base » (15 000 € par mois) qu'après le pilote et au prix d'un changement complet d'organisation de Morgan. Aucun scénario ne finance l'objectif de 7 500 € nets chacun (OFF:118) la première année.

---

## 7. Structure recommandée et principes des relations

### 7.1 Forme juridique : SAS à l'IS par défaut, sous conditions [PR]

- **Pourquoi une SAS** : le démarrage se fait sans rémunération régulière (0 € de cotisation sans rémunération en SAS, contre environ 1 255 € par an et par gérant en SARL, plus les forfaits de début d'activité) ; les associés gardent d'autres activités ; une entrée d'investisseur reste évoquée (syn-D:209-226).
- **Conditions** : président et directeur général, chacun avec au moins un tiers du capital (condition de l'ACRE) ; capital modeste **entièrement libéré** (taux réduit d'IS) ; statuts qui organisent le blocage ; pacte signé **avant** le contrat client ; rémunération nulle jusqu'au socle récurrent, puis fixée par décision collective (syn-D:221-225, 293).
- **Quand immatriculer** : statuts et pacte préparés tout de suite ; immatriculation déclenchée à réception d'un bon de commande ou d'une lettre d'intention écrite d'une entité identifiée de GianLuca (syn-D:233). Délai d'immatriculation [HY] : une à trois semaines.
- **À ne pas faire** : faire porter le contrat par l'entreprise existante de Morgan, dont la domiciliation est résiliée (syn-D:283) ; micro-entreprise (syn-D:228-232) ; encaisser sur un compte personnel (syn-D:313).
- **Repasser à la SARL** seulement si les conditions changent : contrat signé d'au moins 120 000 € par an, aucun investisseur avant 24 mois, aucun associé salarié ailleurs (syn-D:227). Ce n'est pas le cas de S1 la première année.
- **Dès la création** : compte professionnel ; RC professionnelle avant la première prestation, en vérifiant les exclusions IA, cyber et données ; plateforme de réception des factures électroniques (obligatoire depuis le 1er sept. 2026) ; déclaration de CFE 1447-C-SD avant le 31 déc. si la société est créée en 2026 ; comptes techniques au nom de la société (syn-D:288-308).
- **À valider par l'expert-comptable** : simulation officielle SAS et SARL sur les trois niveaux de CA de S1 ; date de clôture du premier exercice ; ACRE ; rescrit FRR seulement si des bureaux sont réellement utilisés en zone (syn-D:198-207, 305).

### 7.2 Entre Morgan et Mathys : ce que le pacte doit régler avant le contrat client

| Thème | Principe S1 [PR] | Source |
| --- | --- | --- |
| Disponibilité | Nombre minimal de JP par mois par associé, relevé mensuel, déclaration écrite des autres activités (OLSEN, Shelby, BOJ.ART, etc.) et règle de priorité pour les clients de Marwin | syn-D:470 ; NOTE § B |
| Travail existant | Inventaire daté : CRM (co-écrit, dépôt FinanceScope), Jarvis (périmètre BOJ.ART et Morgan), catalogue, études ; licence non exclusive à Marwin par défaut, ou cession écrite | syn-D:472 |
| Rôles | Morgan : relation client, prix ; Mathys : technique, données ; **délégation écrite de la validation technique à Mathys** pour supprimer le point de passage unique | syn-C:265, 274 |
| Rémunérations | Liées au temps engagé ; grille écrite ; rien avant le socle récurrent | syn-D:474 |
| Décisions à l'unanimité | Contrat avec GianLuca ; engagement de plus de 1 500 € ; entrée d'un associé ; recrutement ; sous-traitance | syn-D:475 |
| Conflits d'intérêts | Déclaration écrite des liens avec BOJ.ART, Medhi, OLSEN et toute entité de GianLuca ; abstention ; information du client | syn-D:481 |
| Départ, incapacité | Préavis, transmission des accès, coffre-fort partagé, rachat des parts | syn-D:477-478 |

### 7.3 Relations avec GianLuca Carlone : un rôle à la fois

| Rôle évoqué | Principe S1 | Quand | Conditions |
| --- | --- | --- | --- |
| **Client** | Seul rôle accepté pendant au moins douze mois | Dès le cadrage | Entité identifiée ; un bon de commande par lot et par entité ; un valideur nommé, distinct d'un éventuel salarié (syn-D:442) |
| **Bailleur** (bureaux) | Refusé pendant le cadrage et le pilote | Au plus tôt au mois 6, si utile | Convention séparée (gratuite ou avec loyer, accès sans horaires imposés, assurance, restitution) ; aucun lien avec les honoraires ; bureaux réellement utilisés si l'on invoque le FRR (syn-D:437-439) |
| **Employeur** | Refusé pendant au moins six mois | Pas avant le bilan du mois 6 | Une seule personne ; fonctions non couvertes par Marwin ; temps séparés ; validation des livrables Marwin par une autre personne ; jamais un argument de négociation des honoraires (syn-D:405-408) |
| **Investisseur** | Pas de discussion avant 12 à 24 mois | Après au moins deux renouvellements du socle | Minoritaire ; sans veto opérationnel ; contrat client résiliable indépendamment ; jamais contre une baisse d'honoraires ; l'acompte n'est ni du capital ni un prêt (syn-D:440 ; OFF:149) |
| **Financeur de R&D ou de création** | Aucun | — | Tout projet futur fait l'objet d'une convention séparée, avec financeur écrit, budget plafonné, jalons et critère d'arrêt |

**Plafond de dépendance** [PR] : la part du chiffre d'affaires venant des entités de GianLuca est suivie chaque mois ; cible ≤ 80 % au mois 12 et ≤ 60 % au mois 24. Un préavis gradué et réciproque protège mieux qu'un engagement long (syn-D:374-378).

### 7.4 Relations avec Medhi et BOJ.ART

- **Hors de l'offre Marwin**, par décision écrite de Morgan et Mathys qui formalise le retrait oral du 4 nov. (syn-P:503).
- **Morgan informe Medhi par écrit** de ce qui est retiré (STRATES, exclusivité de vente, usage des films, vernissage) et vérifie ce qui lui a été dit ou promis [IN].
- **Aucune promesse au nom de Medhi** : Marwin ne peut pas céder ce qu'elle ne détient pas (syn-D:500). Si la galerie veut vendre ses pièces, c'est un contrat de dépôt-vente direct entre Medhi et l'entité de GianLuca, sans Marwin.
- **Conflit d'intérêts déclaré** : Morgan se présente comme co-porteur de BOJ.ART (ACC:21) ; il s'abstient de toute recommandation d'achat ou de vente qui concerne Medhi, et le dit au client si le sujet vient (syn-S ASS-4, :325).
- **Aucun moyen de BOJ.ART dans les livrables Carlone** : ni parc d'impression, ni tour RTX 4060 Ti, ni code Jarvis tant que la propriété n'est pas réglée (syn-C:105-106 ; syn-S PRO-2).
- La relation préexistante entre GianLuca et Medhi (rachat de son ancienne affaire, [DR] CTX:24) rend le sujet sensible : en parler seulement si GianLuca l'aborde.

---

## 8. Gouvernance minimale

### 8.1 Qui propose, autorise, exécute, contrôle et valide

| Acte | Propose | Autorise | Exécute | Contrôle | Valide le résultat |
| --- | --- | --- | --- | --- | --- |
| Choix des priorités, arbitrage entre projets | Marwin (Morgan) | GianLuca ou son délégué, en comité mensuel | Marwin | Délégué du client | GianLuca |
| Commande d'un lot | Marwin (devis écrit) | Signataire de l'entité concernée | Un associé | L'autre associé (« quatre yeux ») | Délégué du client (réception) |
| Dépense pour un projet | Marwin (devis comparés) | GianLuca, par écrit | **L'entité cliente** commande et paie | Marwin tient le registre des engagements | Délégué du client |
| Engagement récurrent (abonnement, prestataire) | Marwin | Signataire de l'entité | L'entité, à son nom | Marwin | GianLuca |
| Contrat, recrutement, emprunt, investissement, changement stratégique | Marwin prépare le dossier | **Réservé à GianLuca** ou à un mandataire habilité (ACC:100-102) | L'entité | Professionnel compétent | GianLuca |
| Mise en service d'une automatisation | Mathys, après essai | GianLuca, par écrit | Mathys | Morgan et le journal | Délégué, sur critères |
| Message à un tiers au nom du client | Marwin rédige | Délégué, message par message | L'entité, sous son nom | — | — |
| Incident de sécurité ou de données | Quiconque le constate | Pas d'autorisation préalable pour **arrêter** (couper un accès, suspendre un automatisme) | Marwin | Fiche d'incident | Le responsable du traitement décide des notifications |
| Changement de périmètre, dépassement | Marwin (avenant) | Signataire | — | — | — |
| Dépense interne de Marwin > 300 € HT ou tout abonnement | L'un des associés | Les deux associés | — | Expert-comptable | — |

### 8.2 Plafonds

- **Pendant le cadrage et le pilote** : mandat de dépense à **0 €**. Marwin prépare et compare ; l'entité commande et paie.
- **Avec le socle récurrent** : plafond de 500 € HT par acte et de 1 500 € HT cumulés par mois, sur une liste fermée d'actes, dans des budgets déjà approuvés, factures au nom de l'entité cliente et payées par elle ; registre des engagements tenu à jour (syn-D:424-429). Au-delà : accord écrit à chaque fois.
- **Engagements récurrents, contrats, recrutements** : jamais délégués.
- **Urgences** : liste fermée (incident de données ou de sécurité, échéance légale). Marwin peut arrêter, jamais dépenser ni engager ; information du client sous 24 h.
- **Capacité** : au-delà de 90 % des JP réservées avant le 20 du mois, arrêt des travaux non urgents ; au-delà de 100 %, avenant ou report (syn-C:298).

### 8.3 Le silence ne vaut pas accord

| Situation | Règle [PR] |
| --- | --- |
| Demande de décision ou d'autorisation sans réponse | **L'engagement attend** (ACC:103). Relance à 5 jours ouvrés ; à 10 jours, les jalons concernés sont reportés et consignés ; à 15 jours, revue du contrat (syn-C:293) |
| Livrable remis sans réserve sous 10 jours ouvrés | Réputé **livré pour la facturation du solde** uniquement. Cela ne vaut ni approbation d'une suite, ni autorisation d'une dépense. La contradiction entre OFF:206 et ACC:103 (syn-S PER-14) est ainsi tranchée |
| Socle arrivé à échéance | **Pas de tacite reconduction** : renouvellement par accord écrit (ACC:51) |
| Désaccord sur un livrable | Réserves écrites ; un cycle de correction gratuit ; au-delà, médiation en comité, puis réduction du périmètre |
| Désaccord entre associés | Décisions de la liste du pacte à l'unanimité ; à défaut, rien n'est proposé au client ; médiation, puis mécanismes du pacte |

---

## 9. Feuille de route

### 9.0 Phase 0 : du 4 au 19 novembre 2026 (non facturée)

| Livrable | Responsable proposé | Indicateur | Échéance |
| --- | --- | --- | --- |
| Décision sur la notification à la CNIL, avec un avocat ou un DPD ; dépôt privé et vérifié ; fiche de violation ; information écrite de GianLuca | Mathys (titulaire présumé du dépôt) et Morgan | Décision datée et motivée | **5 nov.** (ou retard motivé) |
| Arrêt de toute production nouvelle pour GianLuca | Morgan et Mathys | 0 JP produite hors remise en ordre | Immédiat |
| Mise en cohérence : une seule offre, PR n° 1 fermée ou PDF marqué « historique », documents retirés marqués, aucune occurrence de l'ancienne erreur de prénom dans un document client | Morgan | 0 mention de Medhi, BOJ.ART, STRATES, laboratoire ou de l'ancien prénom dans les documents remis | 13 nov. |
| Décision écrite sur Medhi et BOJ.ART ; message à Medhi | Morgan, validé par Mathys | Décision signée par les deux | 13 nov. |
| Fiche des disponibilités nominatives ; principes du pacte ; accord de Mathys sur la stratégie | Morgan et Mathys | Fiche signée | 19 nov. |
| Proposition de cadrage d'une page ; liste des questions bloquantes (§ 13) | Morgan | Document prêt | 19 nov. |

### 9.1 À 90 jours : jusqu'au 2 février 2027

| Livrables | Indicateurs | Dépendances | Critère de passage |
| --- | --- | --- | --- |
| Rendez-vous tenu avec GianLuca ; réponses aux questions 1 à 5 du § 13 | Entité payeuse identifiée (oui / non) | GianLuca | — |
| Bon de commande ou lettre d'intention ; SAS immatriculée ; pacte signé ; compte ; RC professionnelle ; plateforme de factures | Date d'immatriculation ; aucun encaissement avant | Greffe, banque, assureur | — |
| Cadrage vendu, acompte encaissé, cadrage livré et restitué | Délais de paiement de l'acompte et du solde ; JP réelles contre 8 estimées (écart ≤ 25 %) ; accès fournis sous 10 jours ouvrés ; réception au premier passage | GianLuca, son délégué | Inventaire validé par écrit |
| Démonstrateurs internes P1 (registre) et P3 (recherche documentaire) sur données fictives ou internes ; mesure de référence | Temps de référence relevé ; qualité selon les protocoles (syn-C:695-740) | Outils professionnels avec contrat de traitement | — |
| Prospection : trois conversations qualifiées avec d'autres clients possibles | 1,5 à 2,5 JP par mois consacrées à la prospection | — | — |
| **Décision du jour 90** : pilote oui ou non | Décision écrite de GianLuca | GianLuca | Conditions de poursuite de l'offre A |

Budget : ≈ 6 000 € HT de CA ; ≈ 3 000 à 7 000 € de frais de démarrage ; aucune rémunération [ES].

### 9.2 À 6 mois : jusqu'au 4 mai 2027

| Livrables | Indicateurs | Critère de passage |
| --- | --- | --- |
| Pilote de 8 semaines terminé : registre en usage réel, un lot réceptionné | Critères P1 tenus 4 semaines de suite ; réception du lot au premier ou au second passage ; aucune erreur critique | — |
| Bilan mesuré remis à GianLuca : temps humain total, corrections, délais de décision, coût complet par résultat accepté | Coût complet par résultat accepté calculé ; occupation ≤ 85 % | — |
| Exercice de réversibilité à blanc : exports, comptes au nom de l'entité, procédures de secours | Restauration réussie dans un espace neuf (syn-C:857) | — |
| Décision écrite de GianLuca sur le socle récurrent ; si oui, contrat de trois mois signé | Paiements à l'heure ; CA cumulé ≈ 15 000 à 30 000 € HT début mai 2027 si le cadrage est signé en janvier [ES] | Conditions de poursuite de l'offre B |
| Second client : au moins une proposition payante envoyée | Nombre de propositions ; taux de réponse | — |
| Révision du taux de référence à partir du coût mesuré | Coût complet réel par JP | — |

### 9.3 À 12 mois : jusqu'au 4 novembre 2027

| Livrables | Indicateurs (cibles [HY] à fixer avec GianLuca après la mesure de référence) |
| --- | --- |
| Socle récurrent renouvelé au moins deux fois ; lots livrés ; une exploitation (offre E) si un pilote l'a prouvé | CA sur les 12 premiers mois de contrat (qui se terminent fin 2027 si le cadrage est signé en janvier) : ≈ 50 000 / 95 000 / 155 000 € HT selon le scénario ; décisions préparées à temps ≥ 85 % ; taux de corrections < 20 % |
| Gains mesurés sur les processus pilotés | Temps humain par résultat accepté −30 % sur P1 et P3 (syn-C:803) ; facteur de 1,3 à 1,5 sur les processus pilotés (syn-C:811) |
| Second client signé et payé | Part du CA venant des entités de GianLuca ≤ 80 % |
| Émission des factures électroniques au 1er sept. 2027 | Conformité (syn-D:77) |
| Bilan annuel : CA, marge, temps, dépendance ; réexamen de la forme sociale ; trésorerie | Réserve ≥ 3 mois de frais et 1 mois de rémunération ; 0 incident critique ; occupation ≤ 85 % |
| Seulement alors : discussion éventuelle des bureaux, du salariat ou d'un investissement | Accords séparés, chacun avec sa sortie |

---

## 10. Conditions pour commencer, signaux de suspension, réduire, reporter ou refuser

### 10.1 Conditions minimales pour commencer un travail payé (toutes requises)

1. **Fuite traitée** : dépôt privé vérifié, fiche de violation, décision de notification documentée avec un avocat ou un DPD, GianLuca informé par écrit.
2. **Entité cliente identifiée** (dénomination, SIREN, signataire habilité) et bon de commande signé.
3. **Marwin immatriculée** (SAS), avec compte professionnel, RC professionnelle et outil de facturation ; pacte signé.
4. **Disponibilités nominatives écrites** de Morgan et de Mathys, et accord écrit de Mathys sur l'offre et sur le retrait de Medhi.
5. **Documents client cohérents** : une seule version ; ni Medhi, ni BOJ.ART, ni STRATES, ni laboratoire, ni ancien prénom ; V5 jamais transmis (syn-D:315).
6. **Acompte encaissé.**
7. **Délégué et accès** désignés côté client.

### 10.2 Signaux de suspension

- Impayé non régularisé 8 jours après relance.
- Aucun accès fourni dans les 10 jours ouvrés.
- Décisions bloquantes en attente depuis plus de 15 jours ouvrés.
- Occupation des associés au-delà de 95 % pendant deux mois, ou prospection sous 50 % du plancher pendant deux mois (syn-C:299-301).
- Incident critique (fuite, action non autorisée, envoi erroné).
- Demande de travailler sans bon de commande, sur des comptes personnels, ou d'avancer des achats pour le client.
- Indices de subordination : horaires imposés, place dans l'organigramme, exclusivité de fait (syn-D:444).
- Promesse d'investissement liée à une baisse d'honoraires.

### 10.3 Quand réduire, reporter ou refuser

| Situation | Réponse | Pourquoi |
| --- | --- | --- |
| GianLuca ne veut confier qu'un seul projet (par exemple les ventes d'œuvres) | **Réduire** : un lot, sans socle | Le pilotage global n'est pas le besoin ; un lot reste rentable |
| Les associés ne peuvent pas engager ensemble au moins 6 JP facturables par mois | **Réduire** au cadrage et à un lot, ou **reporter** | Sous ce seuil, un socle et un projet ne tiennent pas (syn-C:252) |
| Entité payeuse non identifiée ou aucun rendez-vous avant mi-décembre 2026 | **Reporter**, sans travail gratuit | Le scénario S5 « personne ne paie » (syn-P:304) |
| Aide régionale demandée par le client | **Reporter** la signature le temps du dépôt | Dépôt avant signature [DR] |
| Refus de payer le cadrage | **Refuser** la suite ; remettre gratuitement à GianLuca ce qui lui revient (données du CRM, documents) | Hypothèse du besoin infirmée (syn-P:246-250) |
| Rémunération demandée sur les ventes d'œuvres | **Refuser** | Statut d'intermédiaire, LCB-FT, droit de suite [HY] |
| Demande de porter des obligations d'exploitant (licences, ERP, sécurité du public) ou de signer des attestations fiscales | **Refuser** | Activités réglementées et responsabilités sans pouvoir |
| Demande de 20 à 40 JP par mois avec présence quotidienne dans ses bureaux | **Refuser** sous cette forme ; proposer socle et lots | Capacité et risque de requalification |
| Salariat d'un associé combiné au contrat Marwin dès le départ | **Refuser** avant le bilan du mois 6 | Conflit d'intérêts, requalification (syn-D:395-408) |
| Exigence de démarrer avant l'immatriculation | **Reporter** le travail ; au plus, signature au nom de la société en formation, sans encaissement | syn-D:282 |

---

## 11. Cinq décisions prioritaires

| N° | Décision | Qui | Quand |
| --- | --- | --- | --- |
| 1 | **Traiter la fuite** : rendre le dépôt privé, ouvrir la fiche de violation, décider de la notification à la CNIL avec un avocat ou un DPD, informer GianLuca par écrit | Mathys et Morgan | **Avant l'échéance du 5 nov.**, ou retard motivé |
| 2 | **Remplacer l'offre de six mois par le cadrage au forfait** (≈ 6 000 € HT, moitié à la commande) comme seule proposition commerciale ; retirer le renforcement, l'ancre, le laboratoire et la ligne création ; arrêter tout travail non commandé | Morgan et Mathys | Avant tout rendez-vous |
| 3 | **Formaliser le retrait de Medhi et de BOJ.ART** : décision écrite validée par Mathys, message à Medhi, PR n° 1 fermée ou PDF marqué « historique », documents retirés marqués | Morgan | Sous 10 jours |
| 4 | **Choisir la SAS à l'IS**, préparer statuts et pacte, n'immatriculer qu'à réception d'un engagement écrit d'une entité identifiée, ne rien encaisser avant, ne pas utiliser l'entreprise existante de Morgan | Morgan et Mathys, avec l'expert-comptable | Préparation immédiate ; immatriculation sur engagement écrit |
| 5 | **Écrire les disponibilités nominatives et les rôles** : JP par mois de chacun, projets que Morgan suspend, délégation de la validation technique à Mathys, plancher de prospection | Morgan et Mathys | Avant le rendez-vous |

---

## 12. Principaux risques et preuve qui lèverait chaque objection

| Risque ou objection | Gravité [HY] | Preuve qui la lèverait | Échéance | Si la preuve ne vient pas |
| --- | --- | --- | --- | --- |
| Le pilotage global n'est pas le besoin prioritaire de GianLuca | Élevée | Cadrage signé et payé ; trois priorités choisies par lui ; demande écrite d'un suivi après le cadrage | Jour 90 | Réduire à des lots |
| Solvabilité ou volonté de payer inconnues | Élevée | Acompte et solde payés à l'échéance par une entité identifiée | Jour 60 | Reporter ou refuser |
| Délégation sans accès ni décisions | Élevée | Accès fournis sous 10 jours ouvrés ; délégué nommé ; décisions sous 5 jours ouvrés | Pendant le cadrage | Suspendre |
| Les deux associés deviennent le goulot (dispersion de Morgan, disponibilité de Mathys inconnue) | Élevée | Relevé mensuel : occupation ≤ 85 % ; file de validation ≤ 2 jours ouvrés ; JP réelles proches des estimations | Chaque mois | Réduire le périmètre ; refuser les nouveaux projets |
| Le travail gratuit continue | Élevée | 0 JP hors bon de commande dans le relevé | Chaque mois | Arrêt |
| Conséquences de la fuite (CNIL, réputation, confiance du client) | Élevée | Décision de notification documentée ; dépôt privé vérifié ; information écrite de GianLuca ; aucune nouvelle exposition | 5 nov., puis chaque trimestre | Gel de tout lot CRM |
| Documents contradictoires entre les mains du client | Moyenne à élevée | Liste de ce que GianLuca a vu ou reçu (U04) ; version unique remise et datée | Avant le rendez-vous | Correction écrite adressée au client |
| Requalification ou dépendance (client, bailleur, employeur, investisseur) | Moyenne | Un accord par sujet ; aucun horaire imposé ; second client ; part de CA ≤ 80 % au mois 12 | Mois 12 | Différer bureaux, salariat et capital |
| L'exploratoire absorbe la marge (STRATES, laboratoire, Jarvis) | Moyenne | 0 JP imputée à l'exploratoire sans financeur écrit | Chaque mois | Arrêt du projet exploratoire |
| L'automatisation ne fait pas gagner de temps, ou fait baisser le CA | Moyenne | Mesure de référence puis temps humain total par résultat accepté en baisse ; prix au forfait | Mois 6 | Retour au mode assisté simple ; prix inchangé |
| Les équipes du client n'adoptent pas les outils | Moyenne | ≥ 80 % des comptes rendus commentés sous 3 jours ; registre consulté chaque semaine | Fin du pilote | Abandon du processus |
| Responsabilités plus larges que les pouvoirs | Moyenne | Mandat écrit avec actes, plafonds et délégué signé avant toute exécution | Avant le pilote | Pas d'exécution |
| Les prix ne couvrent pas la maintenance | Moyenne | Maintenance chiffrée par outil ; coût complet par résultat accepté connu | Mois 6 | Offre E ou arrêt de l'outil |
| Désaccord entre associés ou avec Medhi | Moyenne | Pacte signé ; décision écrite sur Medhi ; message à Medhi sans contestation | Jour 30 | Pas de proposition au client tant que le désaccord dure |

---

## 13. Questions bloquantes (dix)

**À GianLuca Carlone**
1. Quelle entité signe, paie et valide nos travaux (dénomination, SIREN, personne habilitée) ? Une seule, ou une par projet ?
2. Quelles sont vos trois priorités pour les 90 prochains jours, et que vous coûte chacune aujourd'hui ? Les « vingt jours par mois », est-ce votre demande ?
3. Accepteriez-vous un cadrage de trois à quatre semaines au forfait, payé moitié à la commande ? Quels délais de paiement pratique votre entité ?
4. Quels documents et accès nous donnerez-vous, sous quel délai, et qui sera votre délégué ?
5. Voulez-vous exploiter le CRM ? Au nom de quelle structure vendez-vous les œuvres, et qui appellera les entreprises (Quali Contact est-il engagé) ?

**À Morgan et Mathys**
6. Depuis quand savez-vous que le dépôt FinanceScope/CRM-Carlone est public, qui en est le titulaire, et qui décide de la notification à la CNIL (U08) ?
7. Combien de JP par mois chacun peut-il engager par écrit, et quels projets Morgan suspend-il ? Quelle est la situation de Mathys (emploi, études) ?
8. Mathys approuve-t-il le remplacement de l'offre, le retrait de Medhi, la SAS et le régime de propriété du CRM ?
9. Qu'a vu ou reçu GianLuca (version à quatre jours, lettre du 29 oct., V5, diaporama de 13 ou de 11 diapositives, rapport CRM, vernissage), et qu'a-t-on promis à Medhi (U04, U10) ?
10. Quel apport de trésorerie pouvez-vous mettre au départ (≈ 3 000 à 7 000 €), et pouvez-vous vivre trois à quatre mois sans rémunération de Marwin ?

---

## Annexe : détail des calculs et corrections retenues

**Coût complet** (`cout.py`) : (part du temps Marwin × rémunération nette cible par ETP × coefficient coût / net + frais fixes) ÷ JP facturables ÷ 0,9. Parts du temps et JP facturables : prudent 0,75 ETP et 7 JP ; central 1,15 ETP et 12 JP ; haut 1,8 ETP et 20 JP (syn-C:170-190). Coefficient SAS 1,70 à 1,90 et SARL 1,40 à 1,46 [HY] (syn-D:98, 112). Frais fixes 1 500 à 2 500 € par mois [HY].

**Scénarios et trésorerie** (`plan.py`) : encaissements mensuels HT selon les échéanciers du § 5 ; capital de 3 000 € ; frais de démarrage de 4 500 € ; frais fixes de 2 000 € par mois ; rémunération à partir du mois 4 avec un coefficient de 1,8 ; retards appliqués à partir du mois 4. Ni IS, ni TVA, ni régularisation sociale. Les résultats sont des ordres de grandeur à faire refaire par l'expert-comptable sur des bases officielles.

**Coût d'une journée d'assistant** : 2 249 à 2 808 € de coût employeur mensuel (ver-R6 n° 3) ÷ ≈ 17,9 jours travaillés par mois [HY] ≈ 125 à 157 € par jour [ES].

**Corrections des contrôleurs retenues ici** : délai CNIL au 5 nov. si la connaissance date du 2 nov. (ver-R4 n° 7) ; « vingt jours » à attribution contradictoire (ver-C1 n° 4) ; plancher de 10 278 € = seuil de coûts, pas une remise (ver-C1 n° 8) ; origine du taux de 750 € et des 15 000 € [HY] / [IN] (ver-C2 n° 2) ; 1 250 € par jour du Diag Data IA = maximum calculé, pas un prix de marché (ver-R6 n° 6) ; DGX Spark de 128 Go ≈ 6 200 à 8 100 € HT (ver-R6 n° 12) ; Ringover à revérifier (ver-R6) ; prospection téléphonique B2B hors consentement préalable, fondée sur l'intérêt légitime si l'objet est en rapport avec la profession (ver-R6 n° 9) ; démonstrateur Jarvis dans le forfait, pas dans l'option laboratoire (ver-C8 n° 9) ; option laboratoire « en vigueur », pas « envoyée » (ver-C8 n° 8) ; parc d'impression « probablement celui de Medhi » [HY] (ver-C2 n° 11).

**Limites.** Aucune parole directe de GianLuca Carlone n'est disponible : tous les prix proposés sont à confronter à sa réponse. La disponibilité de Mathys, les frais réels de Marwin, le coût de la RC professionnelle et du conseil sur la fuite sont inconnus [IN]. La collecte ChatGPT reste incomplète (169 conversations lues sur 219) : des promesses faites au client peuvent exister hors du corpus. La visibilité du dépôt FinanceScope n'a pas été revérifiée par cet audit.
