# Feuille de route à 90 jours, 6 mois et 12 mois

Audit Marwin Tech × GianLuca Carlone · livrable 8 sur 15 · 4 novembre 2026
Statut : interne (dates butoirs, capacité et rémunérations visées des associés, budget, probabilités : ne pas transmettre à GianLuca Carlone)
Sources principales : `travaux/strategie-retenue.md` (sections 3, 5, 10 à 13) ; `travaux/syn-capacite-ia.md` (section 6) ; `modele-financier/tresorerie-18-mois.md` ; `modele-financier/scenarios.md` ; `modele-financier/stress-tests.md` ; `travaux/syn-droit.md` (échéancier, lignes 62 à 79) ; 06-fonctionnement-a-deux.md (sections 3.7 et 10) ; 07-processus-ia-et-essais.md (section 6) ; pièces d'origine du dépôt Momolscode/Carlone (commit 7b46602), rouvertes en lecture seule le 4 nov. 2026.
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu. Sans autre précision, une [PR] vient de la stratégie retenue ; « [PR, ce livrable] » signale une proposition nouvelle.

**Conventions.** **JP** : journée-personne de 7 h ; deux personnes présentes une journée consomment 2 JP. Les codes d'offres (0, A, B0, B1, B2, C1 à C8, D, E) sont ceux de `travaux/strategie-retenue.md:194-203`, détaillés dans 04-catalogue-offres.md. **P1** (registre des décisions et comptes rendus), **P2** (qualification du CRM), **P3** (recherche documentaire) et **P4** (détection des incohérences) sont les essais d'IA de `travaux/syn-capacite-ia.md:695-755`, détaillés dans 07-processus-ia-et-essais.md. « Dépend de » sépare **Marwin** (Morgan Olsen, Mathys Couet), **GianLuca** (lui, son entité ou son délégué) et les **tiers** (avocat ou DPD, expert-comptable, greffe, banque, assureur, Région, Quali Contact, Medhi). Le calendrier de référence est le scénario central (mois 1 = janvier 2027). Toute date postérieure au 15 décembre 2026 est conditionnelle [HY].

---

## En bref

1. **C'est un plan de pilotage, pas une prévision.** Aucun contrat, aucune facture, aucune entité payeuse n'existe [FV négatif] (`travaux/syn-sources.md:39`). La feuille de route découpe l'objectif de la stratégie : 2 févr. 2027 (90 jours), 4 mai 2027 (6 mois), 4 nov. 2027 (12 mois) (`travaux/strategie-retenue.md:141-145`).
2. **L'ordre est imposé** : la fuite de données, puis les documents, puis l'accord écrit des deux associés, et seulement ensuite le client. Rien n'est encaissé avant l'immatriculation (`travaux/strategie-retenue.md:449-458`).
3. **Déroulé central** [PR] : novembre 2026, remise en ordre non facturée ; décembre, rendez-vous, engagement écrit, immatriculation ; janvier, cadrage ; février-mars, pilote de huit semaines dans une seule voie ; avril, socle récurrent au plus tôt ; juillet, exploitation d'un processus prouvé au plus tôt.
4. **Deux dates butoirs** : entité nommée et rendez-vous tenu au mardi **15 déc. 2026** ; cadrage commandé et payé au **31 janv. 2027**, un dimanche, donc en pratique le vendredi 29 janv. (`travaux/strategie-retenue.md:697-698`). Elles font partie de **quatorze jalons de décision** (section 7.1).
5. **Onze points de non-retour** (section 7.2). Les plus lourds : l'échéance de la CNIL (5 nov.), l'envoi du message de recadrage, l'immatriculation, la première donnée réelle dans un outil, un autre rôle accepté auprès de GianLuca, la baisse durable des autres revenus d'un associé. Chacun ne se franchit que sur une preuve écrite.
6. **Ce que Marwin contrôle** (qualité, délais, coût, refus) et **ce qui dépend de GianLuca** (entité, paiement, accès, décisions, adoption, ventes) se mesurent à part (section 8). La livraison déclenche le paiement ; l'adoption décide de la suite (`travaux/strategie-retenue.md:287`).
7. **Budget central** [ES] : apport de 10 000 € (fourchette 8 000 à 14 000 €) ; point bas de trésorerie de 3 100 € en déc. 2026 ; aucune rémunération avant avril 2027 ; ≈ 25 400 € HT facturés au 30 avril 2027 et ≈ 73 400 € HT au 31 oct. 2027. Pondéré par les probabilités de passage, le central ne vaut que ≈ 38 300 € HT encaissés sur douze mois, et seulement si le cadrage est vendu (`modele-financier/scenarios.md:20, 45`).
8. **Août, fin décembre, avril et octobre sont des mois réduits** (congés) [HY]. Aucune livraison de lot n'est prévue en août ni la dernière semaine de décembre ; en avril et en octobre, la capacité vendable baisse à 9,2 et 8,6 JP (06-fonctionnement-a-deux.md, section 3.7).
9. **Un écart avec la stratégie** : la réception du cadrage et la décision écrite de GianLuca ne peuvent tenir au 2 févr. que si l'engagement écrit arrive vers le 11 déc. Ce livrable propose une tolérance jusqu'au 31 mars, sans toucher à la règle d'arrêt du 31 janv. (encadré de la section 3.10).

---

## 1. Ce que ce livrable ajoute, et ce qu'il laisse aux autres

**Il ajoute** : chaque horizon découpé en livrables datés, avec un responsable, un critère de réception et une dépendance ; un calendrier semaine par semaine jusqu'au 1er janv. 2027, puis mois par mois jusqu'en novembre 2027 ; les jalons de décision et les points de non-retour ; les dates extérieures qui pèsent sur le calendrier ; la répartition entre Marwin, GianLuca et les tiers.

**Il ne refait pas** : le verdict et les cinq décisions (01-synthese-direction.md) ; les contradictions des sources (02-etat-des-sources.md) ; les offres, prix et réceptions (04-catalogue-offres.md) ; la trajectoire de valeur pour GianLuca (05-proposition-de-valeur.md) ; la capacité, les seuils de saturation et les rituels (06-fonctionnement-a-deux.md) ; les protocoles d'essai (07-processus-ia-et-essais.md) ; la trésorerie et les tests d'échec (09-modele-economique-tresorerie.md) ; les statuts, le pacte et les rôles (10-structures-et-relations.md) ; le contrat et la sortie (12-gouvernance-contrat-sortie.md) ; l'ordre du jour du rendez-vous (13-preparation-rendez-vous.md) ; le registre des risques (14-registre-risques-inconnues-decisions.md).

**Vérifications refaites le 4 nov. 2026.** Jours de la semaine des dates clés (le 11 nov. 2026 est un mercredi férié ; le 15 déc. 2026 un mardi ; le 31 janv. 2027 un dimanche ; le 2 févr. 2027 un mardi ; le 4 mai 2027 un mardi ; le 25 sept. 2027 un samedi ; le 4 nov. 2027 un jeudi). Lignes citées des pièces d'origine (offre écrite, page d'accompagnement du 29 oct., note de contexte, audit du 2 nov.). Tableaux mensuels du modèle financier. Les totaux de 25 400 € HT (janvier à avril 2027) et de 73 400 € HT (janvier à octobre 2027) sont des sommes faites pour ce livrable à partir de `modele-financier/scenarios.md:131-140` [ES].

---

## 2. Objectif et calendrier selon le scénario

### 2.1 Objectif principal [PR]

L'objectif est celui de `travaux/strategie-retenue.md:141-145`, repris dans 01-synthese-direction.md :
- **au 2 févr. 2027** : fuite traitée ; documents remis en ordre ; cadrage vendu, encaissé et réceptionné par une entité identifiée de GianLuca ; décision écrite de sa part sur la suite ;
- **au 4 mai 2027** : preuve sur pièces, par un pilote de huit semaines dans la voie qu'il a choisie, qu'un pilotage borné lui est utile et couvre le coût complet de Marwin, sans dépasser 10 JP facturables par mois ni 85 % d'occupation de chaque associé ;
- **au 4 nov. 2027** : socle récurrent renouvelé sur preuves ; gains mesurés sur au moins deux processus ; sortie testée ; second client payant, ou dépendance assumée par écrit.

### 2.2 Trois calendriers

Les dates des horizons sont fixes. Les scénarios déplacent le mois 1.

| Étape | Prudent | Central (référence) | Ambitieux |
| --- | --- | --- | --- |
| Rendez-vous avec GianLuca | Avant le 15 déc. 2026 ou, après report, en janvier | Avant le 15 déc. 2026 | En novembre 2026 |
| Engagement écrit, puis immatriculation | Janvier 2027 | Début ou mi-décembre ; immatriculation fin décembre ou début janvier | Novembre ; immatriculation début décembre |
| Mois 1 (acompte du cadrage) | Février 2027 (acompte au plus tard le 29 janv.) | Janvier 2027 | Mi-décembre 2026 |
| Restitution du cadrage | Fin février ou début mars | Fin janvier ou début février | Mi-janvier |
| Pilote | Aucun ; « socle + 1 projet » dès le mois 3 (avril) | Février et mars, une seule voie | Janvier et février, avec deux lots |
| Socle récurrent | Avril 2027 : 3 000 € HT par mois | Avril 2027 (mois 4) : B1 à 4 500 € HT par mois | Mars 2027 (mois 4) : « socle + 3 projets » à 5 700 € HT par mois |
| Première rémunération | Mai 2027 (mois 4) : 600 à 800 € nets par associé | Avril 2027 : 1 100 à 1 500 € nets par associé | Mars 2027 : 1 600 à 2 200 € nets par associé |
| Exploitation D | Non | Absente du modèle ; au plus tôt juillet 2027 | Juin 2027 (mois 7) |
| Second client | Non | Variante : dès juillet 2027 | Dès mai 2027, probabilité 50 % [HY] |
| Mois 12 | Janvier 2028 | Décembre 2027 | Novembre 2027 |

Sources : `travaux/strategie-retenue.md:494-516` ; `modele-financier/scenarios.md:34-35, 67, 96, 123, 149, 206`. Valeurs [PR] ou [ES] ; les nets sont ceux du modèle, en SAS, avant impôt sur le revenu. La stratégie annonçait 650 à 750 €, 1 350 à 1 550 € et 2 100 à 2 350 € (`travaux/strategie-retenue.md:511`) : le modèle ajoute l'IS et les délais d'encaissement, d'où des nets plus bas (`modele-financier/scenarios.md:209-221`).

**Lecture.** En prudent, l'objectif des 6 mois glisse d'environ un mois : un pilote ne peut pas être terminé le 4 mai 2027. **Révision vers le haut** : si GianLuca demande d'emblée un pilotage large et fournit entité, accès et acompte, le socle B1 peut suivre directement la restitution du cadrage, avec la même limite de projets actifs et le même plafond de 10 JP facturables par mois (`travaux/strategie-retenue.md:60`).

---

## 3. Horizon 90 jours : du 4 nov. 2026 au 2 févr. 2027

### 3.1 Objectifs

| Objectif | Sous le contrôle de | Preuve attendue |
| --- | --- | --- |
| Traiter la fuite ; ne plus utiliser aucune donnée réelle | Marwin, avec l'avocat ou le DPD | Décision datée et motivée ; fiche de violation ; capture du dépôt en « privé » (`travaux/strategie-retenue.md:715`) |
| Un seul jeu de documents, cohérent avec la décision du 4 nov. ; plus aucun travail gratuit | Marwin | 0 mention interdite dans les documents remis ; 0 JP hors remise en ordre (`travaux/strategie-retenue.md:716`) |
| Associés d'accord par écrit ; structure prête ; apport réuni | Marwin, avec l'expert-comptable et l'avocat | Fiche « rôles et disponibilités » signée ; statuts et pacte prêts ; fonds disponibles (`travaux/strategie-retenue.md:717-718`) |
| Vendre et livrer le cadrage à une entité identifiée | GianLuca (commande, paiement, accès, réception) ; Marwin (livraison) | Bon de commande ; acompte ; dossier remis ; restitution tenue |
| Obtenir sa décision écrite sur la suite | GianLuca | Demande écrite d'une suite, ou arrêt propre |

### 3.2 Livrables

| N° | Livrable | Responsable (contrôle) | Échéance [PR] | Critère de réception | Dépend de |
| --- | --- | --- | --- | --- | --- |
| 1 | Dépôt FinanceScope/CRM-Carlone rendu privé et vérifié ; copies contrôlées ; secrets révoqués ; fiche de violation ouverte | Mathys, titulaire présumé du dépôt (Morgan) | Jeu. 5 nov. 2026 | Capture « privé » datée ; liste des copies ; fiche ouverte | Marwin, si elle contrôle l'organisation FinanceScope [IN] (`travaux/strategie-retenue.md:733`) |
| 2 | Décision sur la notification à la CNIL, prise avec un avocat ou un DPD ; notification échelonnée [HY] ou en retard motivée si nécessaire | Mathys et Morgan | Avant l'échéance du jeu. 5 nov., heure inconnue (`travaux/syn-droit.md:623`) | Décision datée et motivée | Tiers |
| 3 | Rôles RGPD qualifiés par le conseil ; décision sur l'information des personnes (art. 34) ; texte d'information de GianLuca validé | Morgan (Mathys) | Jeu. 19 nov. au plus tard ; immédiatement si le conseil qualifie Marwin de sous-traitant (`travaux/syn-droit.md:624`) | Texte validé par écrit par le conseil | Tiers |
| 4 | Documents remis en ordre : une seule version de l'offre ; offre écrite du 2 nov., STRATES v1.1, vernissage et PDF de 13 diapositives marqués « historique, retiré le [date] » ; diaporama corrigé ; V5 jamais transmis ; correction d'identité tracée (annexes/correction-identite.md) | Morgan (Mathys) | Ven. 13 nov. 2026 | 0 mention de Medhi, BOJ.ART, STRATES, laboratoire, 750 €, 15 000 € ou de l'ancien prénom dans un document remis ; corrections de `travaux/strategie-retenue.md:814-828` appliquées | Marwin |
| 5 | CRM : hébergement privé ; oppositions appliquées ; simulateur d'économie d'impôt retiré ; dépôt BOJART vérifié | Mathys (Morgan) | Ven. 20 nov. 2026 [PR, ce livrable] | Les quatre points constatés et datés (`travaux/strategie-retenue.md:211`) | Marwin |
| 6 | Fiche « rôles et disponibilités » signée : JP par mois et par associé de décembre 2026 à juin 2027 ; autres activités déclarées ; projets que Morgan suspend ; congés décalés ; délégation de la validation technique à Mathys ; propriété du CRM ; rémunération cible ; apport | Les deux | Jeu. 19 nov. 2026 | Signée ; au moins 6 JP facturables par mois à deux (`travaux/strategie-retenue.md:55, 717`) | Marwin |
| 7 | Décision écrite sur la portée du retrait de Medhi ; message écrit à Medhi | Les deux ; envoi par Morgan | Jeu. 19 nov. 2026 | Décision signée ; message envoyé | Marwin ; la réaction de Medhi relève d'un tiers |
| 8 | Garde-fous écrits : dates du 15 déc. et du 31 janv. ; plafond de 10 JP facturables par mois ; occupation ≤ 85 % sur tout le temps ; prospection de 1,5 à 2,5 JP par mois | Les deux | Jeu. 19 nov. 2026, avant tout contact avec GianLuca | Inscrits au registre interne, puis au pacte (`travaux/strategie-retenue.md:719`) | Marwin |
| 9 | Message de recadrage d'une page, signé des deux (pour-gianluca/message-de-recadrage.md), et proposition de cadrage (pour-gianluca/proposition-de-cadrage.md) | Morgan (Mathys) | Signés le jeu. 19 nov. ; envoyés dès que les livrables 1 à 4, 6 et 7 sont tenus, au plus tard ven. 27 nov. [PR, ce livrable]. La stratégie prévoit le message au 19 nov. (`travaux/strategie-retenue.md:716`) ; la marge d'une semaine ne sert qu'à attendre le texte de l'incident validé par le conseil | Contenu conforme à `travaux/strategie-retenue.md:806-812` ; déclaration du lien de Morgan avec BOJ.ART incluse (`travaux/strategie-retenue.md:635`) | Marwin ; texte de l'incident validé par un tiers |
| 10 | Statuts et pacte prêts à signer ; contrat-cadre en relecture | Les deux, avec l'avocat | Lun. 30 nov. 2026 pour les statuts et le pacte ; contrat-cadre relu avant le bon de commande | Clauses de `travaux/strategie-retenue.md:556-560` et contenu du pacte de `travaux/strategie-retenue.md:619` présents | Tiers |
| 11 | Apport réuni (8 000 à 14 000 €) | Les deux | Lun. 30 nov. 2026 | Fonds disponibles | Marwin |
| 12 | Rendez-vous tenu ; entité nommée (dénomination, SIREN, signataire habilité, effectif) ; solvabilité consultée sur les registres publics | Morgan | Avant le mar. 15 déc. 2026 | Compte rendu ; fiche de l'entité (`travaux/strategie-retenue.md:566`) | GianLuca |
| 13 | Engagement écrit : lettre d'intention ou bon de commande signé au nom de « Marwin Tech, SAS en formation », avec un état des actes | GianLuca ; préparé par Morgan | Décembre 2026 ; vers le ven. 11 déc. pour tenir le 2 févr. (section 3.10) | Document signé (`travaux/strategie-retenue.md:452`) | GianLuca |
| 14 | SAS immatriculée ; compte professionnel ; RC professionnelle souscrite, fuite déclarée ; plateforme de réception des factures électroniques ; comptes techniques au nom de la société | Morgan (statuts, banque, assurance) ; Mathys (comptes techniques) | 1 à 3 semaines après l'engagement écrit [HY] | K-bis ou accusé de réception ; attestation d'assurance (`travaux/strategie-retenue.md:554`) | Tiers |
| 15 | K-bis et attestation de vigilance remis ; facture d'acompte (3 250 € HT, 3 900 € TTC) ; démarrage à l'encaissement | Morgan | Dès l'immatriculation ; acompte vers le ven. 8 janv. 2027 pour tenir le 2 févr. | Acompte encaissé ; délai de 7 jours respecté si la règle de rétractation s'applique (`travaux/strategie-retenue.md:466`) | GianLuca |
| 16 | Cadrage livré et restitué : inventaire, trois priorités chiffrées, carte des rôles, grille de délégation, décision sur le CRM, canal de travail, registre sur un compte de l'entité, mesure de référence de P1, comparaison des trois suites (`travaux/strategie-retenue.md:225`) | Morgan 5 JP, Mathys 3 JP (`travaux/strategie-retenue.md:229`) ; contrôle par l'autre | 3 à 4 semaines après l'acompte et les pièces | Réception expresse des livrables 1, 2 et 4 ; réserves motivées sous 10 jours ouvrés (`travaux/strategie-retenue.md:235`) | GianLuca : pièces, entretiens, réception, solde |
| 17 | Démonstrateurs internes : P1 sur les réunions des associés (registre tenu à la main dès la semaine 1, essai assisté dès la semaine 3) ; P2, format d'échange sur 10 entreprises fictives, et P3 sur un corpus filtré, en janvier | Mathys (Morgan) | P1 : novembre à janvier ; P2 et P3 : janvier, après la souscription d'une offre d'IA professionnelle au nom de Marwin | Critères du démonstrateur atteints, temps humain mesuré, procédure de secours écrite (`travaux/syn-capacite-ia.md:691`) ; au plus 8 JP non facturées avant le 2 févr. (07-processus-ia-et-essais.md, section 6.0) | Marwin |
| 18 | Relevé du temps, sur tout le temps de chacun | Les deux | Dès la semaine 1 | Relevé hebdomadaire clos (06-fonctionnement-a-deux.md, section 10.2) | Marwin |
| 19 | Trois conversations qualifiées avec d'autres clients | Morgan | Mar. 2 févr. 2027 | Trois comptes rendus datés (`travaux/strategie-retenue.md:171`) | Marwin, puis les prospects |

**Corpus du démonstrateur P3.** Il exclut `crm/`, `sources/archives-crm/` et toute pièce qui contient des coordonnées de personnes. Tant que l'offre professionnelle n'est pas souscrite au nom de Marwin, il se limite aux pièces sans nom de tiers, ou il attend (07-processus-ia-et-essais.md, section 6.0). Les démonstrateurs ne passent jamais avant la fuite, les documents et le cadrage (06-fonctionnement-a-deux.md, section 3.8).

### 3.3 Mesure de départ

| Mesure | Valeur au 4 nov. 2026 | Code | Source |
| --- | --- | --- | --- |
| Contrats, factures, entités payeuses | 0 | [FV négatif] | `travaux/syn-sources.md:39` |
| Paroles directes de GianLuca dans les pièces | 0 | [FV négatif] | `travaux/syn-sources.md:38` |
| Rendez-vous fixé avec GianLuca | Aucun dans l'agenda de Morgan les 4, 5 et 6 nov. ; agenda de Mathys inconnu | [FV] ; [IN] | `travaux/note-point-4-novembre-et-activites.md:5, 17` |
| Dépôt du CRM | « Vérifié le 4 novembre via l'API GitHub : « public » » ; heure de 16 h 19 rapportée par la note du 4 nov. ; non revérifié par l'audit | [DR] | `interne/contexte-projet-carlone.md:11` ; `travaux/note-point-4-novembre-et-activites.md:23` |
| Connaissance du problème | Au plus tard le 2 nov. 2026 | [FV] | `interne/audit-marwin-tech-carlone.md:3, 15` |
| Application de la décision du 4 nov. | 1 support sur au moins 5 | [FV] | `travaux/syn-capacite-ia.md:699` |
| CRM | 283 numéros sur 471 « à confirmer » ; 1 date de vérification ; aucun appel, rendez-vous ni vente | [FV] | `travaux/syn-capacite-ia.md:715` |
| Marwin Tech | « n'existe pas encore » : ni forme, ni capital, ni rémunération décidés | [DR] | `interne/offre-marwin-tech-remuneration-et-collaboration.md:153` |
| Disponibilités des associés | Non écrites | [IN] | `travaux/strategie-retenue.md:840` |
| Capacité d'apport | Inconnue ; signaux de tension : domiciliation de l'entreprise existante de Morgan résiliée, abonnements en échec de prélèvement | [IN] ; [DR] | `travaux/note-point-4-novembre-et-activites.md:6, 8` ; `travaux/strategie-retenue.md:776` |
| Prospection propre de Morgan (OLSEN) | 36 propositions et 72 brouillons d'e-mails préparés, aucun envoyé | [DR] | `travaux/note-point-4-novembre-et-activites.md:9` |
| Temps de référence d'une réunion (pour P1) | Inconnu ; aucun compte rendu de rendez-vous avec GianLuca dans le dépôt | [IN] ; [FV négatif] | `travaux/syn-capacite-ia.md:699` |
| Collecte des conversations ChatGPT | 169 lues sur 219 | [FV] | `sources/reprise-59-et-visuels-2026-11-04.md:13` |

### 3.4 Indicateurs

| Indicateur | Cible au 2 févr. 2027 | Qui le fait bouger | Source |
| --- | --- | --- | --- |
| Décision de notification prise avant l'échéance | Oui | Marwin, avec le conseil | `travaux/strategie-retenue.md:715` |
| Mentions interdites dans les documents remis | 0 | Marwin | `travaux/strategie-retenue.md:175` |
| JP passées hors remise en ordre et hors bon de commande | 0 | Marwin | `travaux/strategie-retenue.md:171, 716` |
| JP facturables engagées par écrit à deux | ≥ 6 par mois (8 à 10 en central) | Marwin | `travaux/strategie-retenue.md:55` |
| Entité identifiée | Oui | GianLuca | `travaux/strategie-retenue.md:171` |
| Paiement de l'acompte et du solde | À l'échéance | GianLuca | Idem |
| Accès et pièces fournis | Sous 10 jours ouvrés | GianLuca | Idem |
| JP réelles du cadrage contre 8 estimées | Écart ≤ 25 % | Marwin | Idem |
| Occupation de chaque associé, sur tout son temps | ≤ 85 % | Marwin | `travaux/strategie-retenue.md:623` |
| Conversations qualifiées avec d'autres clients | 3 | Marwin | `travaux/strategie-retenue.md:171` |

### 3.5 Budget

| Poste | Scénario central [ES] | Source |
| --- | --- | --- |
| Encaissements certains | 0 € | `modele-financier/tresorerie-18-mois.md:23` |
| Encaissements hypothétiques | Acompte du cadrage, 3 900 € TTC en janvier ; solde, 3 900 € TTC en février | `modele-financier/tresorerie-18-mois.md:73-74` |
| Apport des associés | 10 000 € (8 000 à 14 000 €) | `travaux/strategie-retenue.md:510` |
| Frais de démarrage | 5 000 à 7 000 € HT : conseil sur la fuite 1 000 à 3 000 € [HY] ; statuts et pacte 2 000 à 5 000 € HT ; formalités, quelques centaines d'euros ; RC professionnelle [IN] | `travaux/strategie-retenue.md:214, 509` |
| Frais fixes | ≈ 2 000 € par mois à partir de janvier 2027 | `travaux/strategie-retenue.md:504` ; `modele-financier/tresorerie-18-mois.md:98` |
| Point bas de la trésorerie disponible | 3 100 € en déc. 2026 ; 700 € ou 100 € si une prime d'assurance annuelle de 2 400 ou 3 000 € est payée d'avance | `modele-financier/tresorerie-18-mois.md:25, 135` |
| Rémunérations | 0 € | `travaux/strategie-retenue.md:172` |
| Temps non facturable | 9 à 17 JP de remise en ordre sur les mois 0 à 2 ; démonstrateurs : 3 à 5 JP prévus, 8 JP au plus | `travaux/strategie-retenue.md:213` ; 06-fonctionnement-a-deux.md, section 3.8 ; 07-processus-ia-et-essais.md, section 6.0 |
| Temps facturable | 8 JP de cadrage | `travaux/strategie-retenue.md:229` |
| Prospection | 1,5 à 2,5 JP par mois | `travaux/strategie-retenue.md:719` |

**Règle de dépense.** Toute dépense de plus de 300 € HT, ou tout abonnement, demande l'accord des deux associés. Au-delà de 1 000 € HT ou de trois mois : unanimité du pacte (`travaux/strategie-retenue.md:592`). Si l'apport n'existe pas, les sorties de novembre se limitent au conseil sur la fuite et aux statuts (`travaux/strategie-retenue.md:776`). Une prime d'assurance se négocie en paiement fractionné (`modele-financier/tresorerie-18-mois.md:135`).

### 3.6 Responsables

| Sujet | Responsable | Contrôle |
| --- | --- | --- |
| Fuite, mesures techniques, CRM, comptes techniques, démonstrateurs | Mathys | Morgan |
| Documents, message de recadrage, relation avec GianLuca, message à Medhi, rendez-vous, prospection | Morgan | Mathys |
| Fiche « rôles et disponibilités », statuts, pacte, apport, garde-fous | Les deux | Avocat et expert-comptable |
| Engagement écrit, acompte, pièces, accès, réception, choix de la suite | GianLuca ou son entité | — |

Source : `travaux/strategie-retenue.md:173`. Tout document envoyé au client passe par l'autre associé, sous 2 jours ouvrés au plus (`travaux/strategie-retenue.md:577-578`).

### 3.7 Dépendances

- **Tiers** : avocat ou DPD (notification, art. 34, rôles RGPD, contrat-cadre, rétractation) ; expert-comptable (date de création et de clôture, TVA, CFE, simulation officielle) ; greffe (1 à 3 semaines [HY]) ; banque ; assureur, dont la couverture d'un incident déjà connu est douteuse [HY] (`travaux/strategie-retenue.md:554`) ; Région, si l'entité de GianLuca veut l'aide au conseil (dépôt avant signature [DR], `travaux/strategie-retenue.md:239`).
- **GianLuca** : rendez-vous (aucun n'est fixé) ; entité ; engagement écrit ; acompte ; pièces sous 10 jours ouvrés ; deux entretiens ; réception (`travaux/strategie-retenue.md:228`).
- **Marwin** : accord de Mathys ; apport ; capacité réelle des associés pendant les fêtes.

### 3.8 Critères de réception de l'horizon

L'horizon est tenu si toutes ces preuves existent (`travaux/strategie-retenue.md:175, 216, 660-669`) :
- dépôt privé vérifié, fiche de violation ouverte, décision de notification datée et motivée ;
- documents conformes à la liste de corrections ; 0 mention interdite dans un document remis ;
- les dix conditions de démarrage d'un travail payé réunies, dont l'immatriculation, le pacte signé, la RC professionnelle et l'acompte encaissé ;
- inventaire validé par écrit ; trois priorités signées ; solde du cadrage payé.

### 3.9 Conditions d'arrêt ou de révision

| Signal | Réponse | Source |
| --- | --- | --- |
| Fuite non traitée | Rien ne démarre ; aucune donnée réelle | `travaux/strategie-retenue.md:176, 660` |
| Désaccord de Mathys au 19 nov. | Aucune proposition au client tant que le désaccord dure ; puis médiation | `travaux/strategie-retenue.md:614` |
| Apport impossible | Report ; sorties réduites au conseil sur la fuite et aux statuts | `travaux/strategie-retenue.md:699, 776` |
| Ni entité ni rendez-vous au 15 déc. 2026 | Report à janvier, sans aucune production | `travaux/strategie-retenue.md:697` |
| Exigence de démarrer avant l'immatriculation | Travail reporté ; au plus une signature au nom de la société en formation, sans encaissement | `travaux/strategie-retenue.md:705` |
| Prix du cadrage refusé | Version réduite à 4 800 € HT ; jamais sous 750 € par JP estimée | `travaux/strategie-retenue.md:694` |
| Aide régionale demandée | Signature décalée le temps du dépôt, sans travailler | `travaux/strategie-retenue.md:700` |
| Cadrage non commandé et payé au 31 janv. 2027 | Report sans date ; temps réorienté vers d'autres clients | `travaux/strategie-retenue.md:698` |
| Refus de payer le cadrage | Pas de suite ; GianLuca reçoit ce qui lui revient, après avis sur les rôles RGPD | `travaux/strategie-retenue.md:701` |

### 3.10 Encadré

> **Écart avec la stratégie retenue : la réception du cadrage et la décision sur la suite au 2 février.**
> *Ce que dit la stratégie.* À 90 jours, le cadrage doit être « vendu, encaissé et réceptionné », avec la décision écrite de GianLuca sur la suite (`travaux/strategie-retenue.md:141`). Mais le report n'est déclenché que si le cadrage n'est pas payé au 31 janvier (`travaux/strategie-retenue.md:176, 698`).
> *Pourquoi ces deux dates ne tiennent pas ensemble.* Rien n'est encaissé avant l'immatriculation (`travaux/strategie-retenue.md:458`). Celle-ci prend 1 à 3 semaines après l'engagement écrit [HY] (`travaux/strategie-retenue.md:486`). Le cadrage dure ensuite 3 à 4 semaines à partir de l'acompte et des pièces, congés de fin d'année non comptés (`travaux/strategie-retenue.md:230`). Les réserves peuvent arriver 10 jours ouvrés après la remise (`travaux/strategie-retenue.md:235`), et la demande écrite d'une suite 30 jours après (`travaux/strategie-retenue.md:237`). Le modèle central encaisse d'ailleurs le solde en février (`modele-financier/tresorerie-18-mois.md:58, 74`). Une réception au 2 févr. suppose donc un engagement écrit vers le 11 déc. et un acompte vers le 8 janv. [ES, ce livrable]. Un acompte payé le 29 janv. respecte la règle d'arrêt, mais repousse la réception à mi-mars.
> *Ce que ce livrable retient [PR, ce livrable].* Le 2 févr. reste la date cible. À cette date, l'horizon est jugé tenu si l'entité est identifiée, le cadrage commandé, l'acompte encaissé et la remise prévue dans les 4 semaines. La réception et la décision écrite peuvent arriver jusqu'au 31 mars 2027 sans déclencher de report. Si la restitution a lieu après le 15 février, tout le calendrier suit le scénario prudent (mois 1 = février) et l'objectif des 6 mois glisse d'environ un mois. La règle d'arrêt du 31 janv. ne change pas.
> *Décision.* Morgan et Mathys valident ou refusent cette lecture le 19 nov. (jalon 2).

---

## 4. Horizon 6 mois : du 3 févr. au 4 mai 2027

### 4.1 Objectifs

1. Montrer sur pièces, par un pilote de huit semaines dans **une seule voie** choisie par GianLuca, qu'un pilotage borné lui est utile : décisions préparées et prises, un livrable réceptionné, un outil réellement utilisé (`travaux/strategie-retenue.md:143`).
2. Montrer que ce pilotage couvre le coût complet de Marwin, sous 10 JP facturables par mois et 85 % d'occupation de chaque associé.
3. Obtenir sa décision écrite sur le socle récurrent, prise sur pièces.
4. Commencer à réduire la dépendance : au moins une proposition payante envoyée à un autre client.

### 4.2 Le pilote selon la voie

GianLuca choisit la voie après la restitution, sur pièces. Une deuxième voie suppose la réception de la première (`travaux/strategie-retenue.md:243-251`).

| | Voie (a) Ventes d'œuvres | Voie (b) Pilotage | Voie (c) Organisation interne |
| --- | --- | --- | --- |
| Besoin rapporté [DR] | Vendre des œuvres aux entreprises de la Nièvre (`sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:13`) | Ne pas gérer chaque détail ; une équipe qui relie les sujets (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:13`) | Idem, sans payer l'exécution au prix du conseil |
| Offre et prix [PR] | C2 : 6 000 € HT | B0 (2 × 3 500 € HT) et un lot C1 ou C4 (3 500 à 6 500 € HT) | C6 : 7 500 € HT |
| JP [ES] | 6 à 7 ; Mathys 4, Morgan 2 à 3 | ≈ 4,5 à 7,5 par mois | 8 à 9 ; Mathys 5, Morgan 3 à 4 |
| Essai d'IA concerné | P2 | P1, puis P3 sur les documents du client | P1 (critère d'adoption de l'outillage) |
| Préalables, tous requis | Responsable du traitement et contrat de l'article 28 ; décision sur l'art. 34 ; entreprises seulement ; structure vendeuse nommée ; 5 à 10 œuvres disponibles ; avis fiscal écrit ; appelant désigné ; seuils fixés avec GianLuca (`travaux/strategie-retenue.md:311`) | Délégué nommé ; réponses sous 5 jours ouvrés ; mandat de dépense à 0 € (`travaux/strategie-retenue.md:248, 589`) | Décision de désigner ou de recruter une personne ; offres d'IA professionnelles (`travaux/strategie-retenue.md:330`) |
| Délai probable avant le démarrage [ES, ce livrable] | Plusieurs semaines : beaucoup de préalables dépendent de GianLuca et de son conseil | Quelques jours | Celui de la désignation de la personne |
| Déroulé | 2 semaines de préparation ; 4 semaines d'appels avec réimport hebdomadaire ; bilan | Point hebdomadaire, compte rendu sous 24 h ouvrées, registre et tableau de bord, comité mensuel ; un lot livré | Outils sur les comptes de l'entité, 5 à 8 procédures, deux formations, test de restauration, 30 jours d'accompagnement |
| Livraison (déclenche le solde) | Fiches sourcées et datées à au moins 90 % ; 100 % des numéros partagés signalés ; 100 % des oppositions respectées ; kit validé ; outil de réimport testé (`travaux/strategie-retenue.md:318`) | Critères de P1 tenus (`travaux/strategie-retenue.md:279`) ; lot livré selon ses critères écrits | Outils en service, procédures remises, formations tenues, restauration réussie, exports remis (`travaux/strategie-retenue.md:336`) |
| Adoption ou mesure (décide de la suite) | Résultats d'au moins 90 % des appels réimportés ; joignabilité ≥ 50 % [HY] ; rendez-vous et ventes suivis à part | ≥ 80 % des comptes rendus commentés sous 3 jours ouvrés ; registre consulté chaque semaine | La personne désignée utilise le registre quatre semaines de suite et traite au moins 80 % des comptes rendus |
| Suite naturelle | Vagues de 50 à 100 comptes (4 000 à 6 000 € HT), ou arrêt | Socle B1 au mois 4 | Pilotage léger éventuel ; Marwin ne reprend pas l'exécution (`travaux/strategie-retenue.md:337`) |

**Effet sur le calendrier.** Le modèle central retient la voie (b), la plus chère. Avec la voie (a) ou (c) seule, le chiffre d'affaires sur douze mois baisse d'environ 5 500 à 7 000 € HT, et la trésorerie libre du mois 12 passe de 15 600 € à 9 200 ou 10 600 € (`modele-financier/scenarios.md:232`). Le modèle garde le socle d'avril dans ces variantes ; rien ne le garantit.

### 4.3 Livrables

| N° | Livrable | Responsable (contrôle) | Échéance [PR] | Critère de réception | Dépend de |
| --- | --- | --- | --- | --- | --- |
| 1 | Choix écrit de la voie | GianLuca ; dossier préparé par Morgan | 30 jours au plus après la restitution ; cible : semaine du lun. 8 févr. | Demande écrite | GianLuca |
| 2 | Préalables de la voie réunis, dont les préalables RGPD avant toute donnée réelle (`travaux/strategie-retenue.md:669`) | Mathys (données) ; Morgan (mandat, délégué) | Avant le démarrage du pilote | Liste cochée et datée | GianLuca ; tiers |
| 3 | Mesure de référence : P1 (temps par réunion, part des décisions avec responsable et date) ; pour la voie (a), qualification manuelle de 5 fiches chronométrée | Mathys (Morgan) | Pendant le cadrage, sur 2 semaines (`travaux/syn-capacite-ia.md:699, 715`) | Mesure écrite avant l'essai | Marwin |
| 4 | Pilote exécuté (section 4.2) | Selon la voie | 8 semaines ; en central, de début février à début avril | Livraison selon la section 4.2 | Marwin pour la livraison ; GianLuca pour l'adoption |
| 5 | Revue de la 4e semaine : critères d'adoption tenus, ou abandon du processus | Les deux, avec le délégué | ≈ début mars | Décision écrite | Marwin ; GianLuca |
| 6 | Bilan mesuré remis à GianLuca : temps de référence et temps réel, critères, coût par résultat accepté, recommandation | Morgan (Mathys pour les mesures) | 6e semaine du pilote, vers le ven. 19 mars | Remis ; chiffres sourcés dans le registre | Marwin |
| 7 | Décision écrite sur le socle récurrent ; contrat B1 avec liste fermée, mandat de dépense et engagements de service | GianLuca ; proposition de Morgan | Avant le jeu. 25 mars pour un démarrage le jeu. 1er avril ; sinon le 1er mai | Bon de commande signé ; premier mois payé d'avance (`travaux/strategie-retenue.md:441`) | GianLuca |
| 8 | Première rémunération, par décision collective, selon une grille liée au temps engagé | Les deux | Avril 2027, seulement si B1 est payé | Décision écrite (`travaux/strategie-retenue.md:550`) | Marwin, sous condition d'encaissement |
| 9 | Restauration réussie dans un espace neuf | Mathys (Morgan) | Avril 2027 | Restauration complète, temps mesuré (`travaux/strategie-retenue.md:175`) | Marwin |
| 10 | Bilan des 6 mois avec l'expert-comptable : coût complet mesuré par JP, taux de référence révisé, écarts d'estimation | Les deux | Mar. 4 mai 2027 | Décisions écrites (`travaux/strategie-retenue.md:169, 400`) | Marwin ; tiers |
| 11 | Au moins une proposition payante à un autre client | Morgan | Mar. 4 mai 2027 | Proposition envoyée et datée | Marwin |

**Fenêtre serrée.** Pour un socle au 1er avril, la décision se prend sur six semaines de pilote. Si les critères n'ont pas tenu quatre semaines de suite au 19 mars, le socle démarre le 1er mai. Le modèle perd alors un mois de B1, soit 4 500 € HT [ES].

### 4.4 Mesure de départ

Le temps de référence relevé pendant le cadrage (P1 : temps par réunion, part des décisions avec responsable et date) ; l'état d'avancement des trois priorités choisies au cadrage ; pour la voie (a), le temps manuel par fiche ; pour la recherche documentaire, 30 questions types posées à la main (`travaux/strategie-retenue.md:170` ; `travaux/syn-capacite-ia.md:731`). Toutes ces valeurs sont aujourd'hui [IN].

### 4.5 Indicateurs

| Indicateur | Cible au 4 mai 2027 | Qui le fait bouger | Source |
| --- | --- | --- | --- |
| Décisions avec responsable, date et source | 100 %, quatre semaines de suite | Marwin | `travaux/syn-capacite-ia.md:702` |
| Comptes rendus envoyés sous 24 h ouvrées | ≥ 90 % | Marwin | Idem |
| Comptes rendus commentés sous 3 jours ouvrés ; registre consulté chaque semaine | ≥ 80 % ; oui | GianLuca | `travaux/syn-capacite-ia.md:706` |
| Réception des livrables | Au 1er ou au 2e passage | Marwin et GianLuca | `travaux/strategie-retenue.md:171` |
| Coût complet par résultat accepté | Calculé | Marwin | Idem |
| Équivalent temps humain évité sur les processus pilotés | 1,3 à 1,5 [HY] | Marwin | `travaux/strategie-retenue.md:163` |
| Décisions préparées à temps | Mesuré ; repère ≥ 70 % [HY, ce livrable] | Marwin | La stratégie vise ≥ 85 % à 12 mois (`travaux/strategie-retenue.md:171`) ; la synthèse capacité le visait dès 6 mois (`travaux/syn-capacite-ia.md:807`) : on suit la stratégie |
| Délai de décision de GianLuca | Mesuré | GianLuca | `travaux/syn-capacite-ia.md:806` |
| Paiements à l'heure | 100 % | GianLuca | `travaux/strategie-retenue.md:171` |
| Occupation de chaque associé, sur tout son temps | ≤ 85 % | Marwin | Idem |
| Propositions payantes à un autre client | ≥ 1 | Marwin | `travaux/strategie-retenue.md:169` |
| Voie (a) : joignabilité, rendez-vous, ventes | Suivis à part, jamais promis | GianLuca et l'appelant | `travaux/syn-capacite-ia.md:725` |

### 4.6 Budget

| Poste | Scénario central [ES] | Source |
| --- | --- | --- |
| Chiffre d'affaires facturé de janvier à avril 2027 | ≈ 25 400 € HT (la stratégie annonce 20 000 à 30 000 €) | `modele-financier/scenarios.md:131-134` ; `travaux/strategie-retenue.md:172` |
| Prix du pilote | 6 000 à ≈ 13 500 € HT selon la voie | `travaux/strategie-retenue.md:247-249` |
| Encaissements TTC | 11 000 € en février ; 8 500 € en mars ; 7 100 € en avril | `modele-financier/tresorerie-18-mois.md:74-76` |
| Rémunérations | Enveloppe de 4 700 € par mois (coût total, deux associés) dès avril, soit ≈ 1 100 à 1 500 € nets par associé | `modele-financier/tresorerie-18-mois.md:27` ; `modele-financier/scenarios.md:21` |
| Trésorerie fin avril 2027 | 16 700 € disponibles ; 13 200 € libres après réserve et IS | `modele-financier/tresorerie-18-mois.md:101` |
| Outils | P1 : deux sièges professionnels (≈ 40 à 50 $ par mois) et un espace de registre (≈ 20 à 40 $), mise en place 2 à 3 JP ; P3 : ≈ 40 à 50 $ par mois, 1 à 2 JP | `travaux/syn-capacite-ia.md:705, 737` |
| Capacité | Plafond de 10 JP facturables par mois ; 9,2 JP vendables en avril (congés) | `travaux/strategie-retenue.md:485` ; 06-fonctionnement-a-deux.md, section 3.7 |
| Probabilités de passage [HY] | Pilote après le cadrage : 60 % ; socle après le pilote : 70 % | `travaux/strategie-retenue.md:502` |

**Règle de protection.** Pas de rémunération sans encaissement ; frais ramenés à ≈ 1 000 € par mois un mois après une rupture. Sans cette règle, une rupture brutale à la fin du pilote demande 21 300 € d'apport en plus ; avec elle, ≈ 1 700 € (`modele-financier/stress-tests.md:34, 340-341`).

### 4.7 Responsables

Comité, relation avec GianLuca, bilans et propositions : Morgan. Outils, données, mesures et validation technique : Mathys. Contrôle à quatre yeux : l'autre associé (`travaux/strategie-retenue.md:173`). Le délégué de GianLuca constate l'adoption ; son signataire décide du socle (`travaux/strategie-retenue.md:576-577`).

### 4.8 Dépendances

- **GianLuca** : choix de la voie ; délégué ; décisions sous 5 jours ouvrés ; préalables RGPD (responsable du traitement, contrat de l'article 28) ; œuvres, structure vendeuse et appelant (voie a) ; personne désignée (voie c) ; adoption ; décision sur le socle ; paiements.
- **Tiers** : conseil fiscal de GianLuca (voie a) ; Quali Contact, s'il appelle, facturé directement à l'entité (`travaux/strategie-retenue.md:388`) ; fournisseurs d'IA (offres professionnelles, clauses types, analyse d'impact des transferts, `travaux/strategie-retenue.md:559`).
- **Marwin** : disponibilités tenues ; contrôle à quatre yeux ; mesures.

### 4.9 Critères de réception de l'horizon

100 % des décisions avec responsable, date et source ; compte rendu sous 24 h ouvrées dans au moins 90 % des cas ; au moins 80 % des comptes rendus commentés sous 3 jours ouvrés ; registre consulté chaque semaine ; restauration réussie dans un espace neuf (`travaux/strategie-retenue.md:175`). S'y ajoutent : bilan mesuré remis ; décision écrite de GianLuca sur le socle ; bilan des 6 mois tenu.

### 4.10 Conditions d'arrêt ou de révision

| Signal | Réponse | Source |
| --- | --- | --- |
| Critères d'adoption non tenus quatre semaines | Abandon du processus | `travaux/strategie-retenue.md:176` |
| Relecture et corrections > 50 % du temps de référence pendant quatre semaines | Retour au manuel | Idem |
| Registre non consulté par le client après quatre semaines | Abandon de P1 | `travaux/syn-capacite-ia.md:707` |
| Impayé 8 jours après relance | Suspension des travaux non urgents ; aucune rémunération sur ce montant | `travaux/strategie-retenue.md:463, 675` |
| Accès non fournis 10 jours ouvrés après le démarrage | Suspension | `travaux/strategie-retenue.md:676` |
| Deux décisions bloquantes en attente depuis plus de 15 jours ouvrés | Suspension ; revue du contrat | `travaux/strategie-retenue.md:677` |
| Occupation > 95 % pendant deux mois | Refus de tout nouveau projet | `travaux/strategie-retenue.md:176` |
| Voie (a) : appels non commencés 15 jours ouvrés après la livraison | Livraison prononcée ; la mesure devient un lot optionnel | `travaux/strategie-retenue.md:318` |
| Voie (c) : personne non désignée 15 jours ouvrés après la livraison | Idem ; Marwin ne reprend pas l'exécution | `travaux/strategie-retenue.md:336-337` |
| GianLuca ne veut confier qu'un projet | Un lot, sans socle | `travaux/strategie-retenue.md:693` |

---

## 5. Horizon 12 mois : du 5 mai au 4 nov. 2027

### 5.1 Objectifs

1. Tenir un socle récurrent **renouvelé sur preuves**, au moins deux fois, ou en sortir proprement avec réversibilité.
2. Mesurer des gains sur **au moins deux processus** : temps humain par résultat accepté en baisse d'environ 30 % [HY].
3. **Tester la sortie** : restitution complète en 15 jours ouvrés au plus.
4. Signer **un second client payant**, ou assumer par écrit une dépendance à 100 % (`travaux/strategie-retenue.md:145`).

**Précision.** La stratégie vise P1 et P3 (`travaux/strategie-retenue.md:171`). Si GianLuca a choisi la voie (a), P1 n'est jamais essayé chez lui : les deux processus mesurés seront P2 et un processus interne. Un gain interne prouve la capacité de Marwin, pas une valeur pour GianLuca ; le bilan annuel doit le dire (07-processus-ia-et-essais.md, section 6.0).

### 5.2 Livrables

| N° | Livrable | Responsable (contrôle) | Échéance [PR] | Critère de réception | Dépend de |
| --- | --- | --- | --- | --- | --- |
| 1 | Rapport mensuel au 5e jour ouvré : capacité consommée par bon de commande, livrables, décisions attendues, risques, indicateurs | Morgan (Mathys pour les mesures) | Chaque mois | Remis à l'heure ; malus de 5 % si deux engagements de service sont manqués dans le mois (`travaux/strategie-retenue.md:279`) | Marwin |
| 2 | Bilan du 3e mois du socle : maintien, passage à B2, ou réduction | Les deux, avec GianLuca | Fin juin 2027 | Décision écrite (`travaux/strategie-retenue.md:281`) | GianLuca |
| 3 | Premier renouvellement du socle, avec la comparaison des coûts d'un coordinateur salarié si sa dépense chez Marwin dépasse ce coût (05-proposition-de-valeur.md, section 4.4) | GianLuca ; proposition de Morgan | Signé avant le ven. 25 juin 2027 (facture de juillet) | Accord écrit ; pas de tacite reconduction (`travaux/strategie-retenue.md:605`) | GianLuca |
| 4 | Lots devisés et réceptionnés, un à la fois (≈ un toutes les six semaines) | Selon le lot | Aucune livraison en août ni la dernière semaine de décembre | Livraison selon les critères écrits avant le démarrage (`travaux/strategie-retenue.md:287`) | Marwin pour la livraison ; GianLuca pour l'adoption |
| 5 | Exploitation D d'un processus prouvé, si un pilote a tenu ses critères quatre semaines, puis deux à trois mois | Mathys (Morgan) | Au plus tôt juillet 2027 | Niveaux de qualité écrits ; mode manuel et restauration testés ; maintenance ≤ 0,5 JP par mois et par processus (`travaux/strategie-retenue.md:344, 349`) | Marwin ; GianLuca pour la commande |
| 6 | K-bis et attestation de vigilance remis à nouveau | Morgan | Six mois après la signature, vers juillet 2027 | Pièces remises (`travaux/strategie-retenue.md:87`) | Marwin ; tiers |
| 7 | Facturation électronique en émission | Mathys (outil) ; expert-comptable | Mer. 1er sept. 2027 | Première facture émise par la plateforme (`travaux/syn-droit.md:77`) | Marwin ; tiers |
| 8 | Exercice de sortie à blanc complet (6e mois du socle) : exports, accès, procédures, restauration | Mathys (Morgan) | Septembre 2027 | Restitution en 15 jours ouvrés au plus (`travaux/strategie-retenue.md:175, 281`) | Marwin |
| 9 | Second renouvellement du socle | GianLuca | Signé avant le ven. 24 sept. 2027 (le 25 est un samedi) | Accord écrit | GianLuca |
| 10 | Second client payant signé, ou dépendance assumée par écrit et cible « ≤ 80 % » reportée au mois 18 | Morgan | Septembre 2027 (mois 9) | Contrat signé, ou décision écrite des deux associés (`travaux/strategie-retenue.md:522`) | Marwin, puis le marché |
| 11 | Mesures des 12 mois : temps humain par résultat accepté sur deux processus, corrections, décisions à temps, incidents, coût complet réel par JP | Mathys (Morgan) | Octobre 2027 | Tableau sourcé dans le registre | Marwin |
| 12 | Calcul du partage des gains pour la deuxième année (un tiers du gain mesuré au client) ; prime sur économie réelle seulement si l'économie est mesurée et validée | Mathys (calcul) ; Morgan (proposition) | Octobre 2027 | Calcul remis avec le rapport (`travaux/strategie-retenue.md:420-421`) | Marwin ; GianLuca pour la validation |
| 13 | Bilan annuel : chiffre d'affaires, marge, temps, dépendance, réserve | Les deux, avec l'expert-comptable | Jeu. 4 nov. 2027 | Décisions écrites sur l'année 2 | Marwin ; tiers |

### 5.3 Mesure de départ

Le coût complet réel par JP mesuré au bilan du mois 6 ; le temps humain par résultat accepté relevé pendant le pilote ; la part de GianLuca dans le chiffre d'affaires, soit 100 % au départ [ES] (`travaux/strategie-retenue.md:170` ; `modele-financier/scenarios.md:44`).

### 5.4 Indicateurs

| Indicateur | Cible au 4 nov. 2027 | Qui le fait bouger | Source |
| --- | --- | --- | --- |
| Décisions préparées à temps | ≥ 85 % | Marwin | `travaux/strategie-retenue.md:171` |
| Livrables corrigés au premier passage | < 20 % | Marwin | Idem |
| Temps humain par résultat accepté, sur deux processus | −30 % [HY] | Marwin | Idem |
| Équivalent temps humain évité sur les processus pilotés | 1,5 à 2 [HY] | Marwin | `travaux/strategie-retenue.md:163` ; `travaux/syn-capacite-ia.md:811` |
| Incidents critiques | 0 | Marwin | `travaux/strategie-retenue.md:171` |
| Part de GianLuca dans le chiffre d'affaires | ≤ 80 %, ou dépendance assumée par écrit | Marwin (prospection) | Idem |
| Renouvellements du socle | 2 signés | GianLuca | `travaux/strategie-retenue.md:169` |
| Restitution testée | ≤ 15 jours ouvrés | Marwin | `travaux/strategie-retenue.md:175` |
| Réserve | ≥ 3 mois de frais fixes et 1 mois de rémunération (≈ 10 700 € en central) | Marwin | `modele-financier/stress-tests.md:23` |
| Occupation de chaque associé, sur tout son temps | ≤ 85 % | Marwin | `travaux/strategie-retenue.md:623` |
| Ventes d'œuvres, ouverture de la galerie, rachats de lieux | Suivis, jamais promis | GianLuca | `travaux/strategie-retenue.md:157` |

### 5.5 Budget

| Poste | Montant [ES] | Source |
| --- | --- | --- |
| Chiffre d'affaires facturé de janvier à octobre 2027 (central) | ≈ 73 400 € HT (dix mois de contrat au 4 nov. 2027) | Somme des mois de `modele-financier/scenarios.md:131-140` |
| Chiffre d'affaires sur les douze premiers mois de contrat | 49 500 € HT (prudent) ; 89 400 € HT (central) ; 141 100 € HT (ambitieux). La stratégie annonçait ≈ 50 000, 90 000 et 150 000 € | `modele-financier/scenarios.md:20` ; `travaux/strategie-retenue.md:513` |
| Valeur pondérée par les probabilités (central) | ≈ 38 300 € HT encaissés, si le cadrage est vendu | `modele-financier/scenarios.md:45` |
| Net par associé en régime (central, SAS, avant IR) | ≈ 1 100 à 1 500 € par mois (la stratégie annonçait 1 350 à 1 550 €) | `modele-financier/scenarios.md:21` ; `travaux/strategie-retenue.md:511` |
| Trésorerie fin octobre 2027 (central) | 25 800 € en banque ; 24 500 € disponibles ; 15 000 € libres | `modele-financier/tresorerie-18-mois.md:107` |
| Frais fixes | ≈ 2 000 € par mois, dont outils et IA ≈ 150 à 400 € | `travaux/strategie-retenue.md:504-505` |
| Capacité | ≈ 8,9 JP vendues par mois en régime ; ≈ 113 JP vendables de décembre 2026 à novembre 2027 sous le plafond | `modele-financier/scenarios.md:38` ; 06-fonctionnement-a-deux.md, section 3.7 |
| Probabilités de passage [HY] | Renouvellement trimestriel du socle : 80 % ; second client au mois 6 : 50 % (ambitieux) | `travaux/strategie-retenue.md:502` |

Les écarts entre la stratégie et le modèle viennent de l'IS, de la TVA et des délais d'encaissement. Ils sont expliqués dans `modele-financier/scenarios.md:209-221` et repris dans 09-modele-economique-tresorerie.md.

### 5.6 Responsables

Morgan et Mathys ensemble ; l'expert-comptable pour le bilan ; l'avocat pour les accords séparés éventuels (`travaux/strategie-retenue.md:173`). Morgan porte la prospection du second client. Mathys porte les mesures, la sortie à blanc et la facturation électronique.

### 5.7 Dépendances

- **GianLuca** : renouvellements écrits ; adoption durable ; demandes nouvelles traitées par la limite d'encours, une demande nouvelle remplaçant un projet actif ou devenant un lot (`travaux/strategie-retenue.md:283`).
- **Tiers** : expert-comptable (bilan, IS, date de clôture) ; avocat (accords séparés éventuels) ; prestataires du client ; pour un premier événement, l'organisateur légal et les autorités (demande GN 6 au moins deux mois avant, `travaux/strategie-retenue.md:293`).
- **Marwin** : prospection d'un second client ; disponibilités tenues ; congés décalés.

### 5.8 Critères de réception de l'horizon

Réserve d'au moins 3 mois de frais fixes et 1 mois de rémunération ; renouvellements signés ; restitution testée en 15 jours ouvrés au plus (`travaux/strategie-retenue.md:175`). S'y ajoutent : gains mesurés sur deux processus avec leur référence ; second client signé ou dépendance assumée par écrit ; bilan annuel tenu.

### 5.9 Conditions d'arrêt ou de révision

| Signal | Réponse | Source |
| --- | --- | --- |
| Impayés récurrents | Sortie | `travaux/strategie-retenue.md:176` |
| Dépendance à 100 % sans prospect | Réduire ; garder d'autres revenus | Idem |
| Incident critique | Arrêt du processus ; information écrite de GianLuca sous 24 h | `travaux/strategie-retenue.md:176, 585` |
| Coût réel non couvert | Relever les forfaits ou réduire le périmètre | `travaux/strategie-retenue.md:176` |
| Demandes hors périmètre > 20 % de la capacité pendant deux mois | Suspension ; revue du contrat | `travaux/strategie-retenue.md:679` |
| Besoin stable au-delà de 6 à 8 JP par mois | Comparaison avec un coordinateur salarié ; offre C6 en alternative | `travaux/strategie-retenue.md:276, 378` ; 05-proposition-de-valeur.md, section 4.4 |
| Occupation > 85 % pendant trois mois et contrat renouvelé qui le finance | Recrutement envisageable ; sinon sous-traitance d'un lot | `travaux/strategie-retenue.md:623` |
| Indices de subordination (horaires imposés, ordres directs, exclusivité de fait) | Suspension ; revue | `travaux/strategie-retenue.md:683` |

---

## 6. Calendrier daté

### 6.1 Les huit premières semaines

La semaine 1 commence le jour de l'audit. La semaine 8 couvre les deux semaines des fêtes.

| Semaine | Dates (jours ouvrés) | Marwin : actions et responsables | GianLuca ou tiers | Preuve attendue | Jalon |
| --- | --- | --- | --- | --- | --- |
| 1 | Mer. 4 au ven. 6 nov. 2026 (3) | **Mathys et Morgan** : dépôt du CRM rendu privé et vérifié ; copies listées ; secrets révoqués ; fiche de violation ouverte ; décision sur la notification avant l'échéance du jeu. 5. **Les deux** : gel immédiat de toute production non commandée ; relevé du temps ouvert ; registre interne des décisions tenu à la main (référence de P1). **Morgan** : liste de ce que GianLuca a vu, reçu ou accepté (`travaux/strategie-retenue.md:736`) | **Avocat ou DPD** : avis sur la notification, échelonnée ou en retard motivée [HY]. Contrôle de l'organisation FinanceScope : [IN] | Décision datée ; capture « privé » ; 0 JP hors remise en ordre | 1 |
| 2 | Lun. 9 au ven. 13 nov. (4 ; mer. 11 férié) | **Morgan** (contrôle Mathys) : documents remis en ordre pour le ven. 13 ; PR n° 1 fermée ou PDF marqué « historique ». **Mathys** : CRM en hébergement privé, oppositions, simulateur retiré ; dépôt BOJART vérifié. **Les deux** : projet de fiche « rôles et disponibilités » ; demande de devis de RC professionnelle (volets IA, cyber, données ; fuite déclarée) ; premier contact avec un expert-comptable | **Conseil** : rôles RGPD, art. 34, texte d'information de GianLuca. Si Marwin est sous-traitant, GianLuca est informé sans délai (`travaux/syn-droit.md:624`) | 0 mention interdite ; devis demandés | — |
| 3 | Lun. 16 au ven. 20 nov. (5) | **Les deux**, jeu. 19 : fiche signée ; décision écrite sur Medhi ; garde-fous écrits ; décision sur l'encadré de la section 3.10. **Morgan** : message à Medhi ; message de recadrage et proposition de cadrage signés ; envoi le 19 si le texte de l'incident est validé. **Mathys** : fin des corrections du CRM le ven. 20 ; essai P1 assisté sur les réunions internes, avec une offre professionnelle si des noms de tiers sont traités | **Conseil** : texte de l'incident validé. **Medhi** : reçoit le message | Fiche signée ; décision sur Medhi ; message prêt | 2 ; 3 |
| 4 | Lun. 23 au ven. 27 nov. (5) | **Morgan** : envoi du message de recadrage au plus tard le ven. 27, avec la déclaration du lien avec BOJ.ART, et demande de rendez-vous ; préparation (13-preparation-rendez-vous.md) ; première conversation qualifiée avec un autre client. **Les deux, avec l'avocat** : statuts et pacte prêts le lun. 30 ; apport réuni ; contrat-cadre en relecture | **GianLuca** : réponse et date de rendez-vous. *Ambitieux* : rendez-vous cette semaine | Message envoyé ; projets de statuts et de pacte ; fonds disponibles | 3 (au plus tard) |
| 5 | Lun. 30 nov. au ven. 4 déc. (5) | **Morgan** : rendez-vous (fenêtre centrale : semaines 5 à 7) sur les questions 1 à 5 (`travaux/strategie-retenue.md:726-730`) ; registres publics consultés dès que l'entité est nommée. **Mathys** : choix des outils des démonstrateurs, en tenant compte des hausses de prix annoncées chez un fournisseur d'IA au 1er déc. et au 1er janv. (`travaux/ver-R6-marche.md:33`) | **GianLuca** : rendez-vous ; entité nommée ; s'il veut l'aide régionale, dépôt du dossier par son entité avant toute signature [DR] | Compte rendu ; fiche de l'entité | — |
| 6 | Lun. 7 au ven. 11 déc. (5) | **Les deux**, dès l'engagement reçu : statuts et pacte signés ; capital déposé ; dossier d'immatriculation déposé ; RC professionnelle souscrite ; compte professionnel ; plateforme de réception des factures électroniques. **Morgan, avec l'avocat** : règle de rétractation (contrat hors établissement, entité de 5 salariés au plus) [HY] | **GianLuca** : engagement écrit (cible : ven. 11 déc.). **Greffe, banque, assureur** | Engagement signé ; dossier déposé | 5 |
| 7 | Lun. 14 au ven. 18 déc. (5) | **Les deux**, mar. 15 déc. : constat du jalon 4 ; sans entité ni rendez-vous, report à janvier sans production. **Mathys** : bilan du démonstrateur P1 dans le registre | **Expert-comptable** : date de création et de clôture ; déclaration de CFE 1447-C-SD avant le 31 déc. si la société est créée en 2026 (`travaux/syn-droit.md:302`) | Constat écrit du jalon | 4 |
| 8 | Lun. 21 déc. 2026 au ven. 1er janv. 2027 (8 ; 25 déc. et 1er janv. fériés) | **Congés décalés** : un associé joignable chaque semaine. **Morgan** : à réception du K-bis ou de l'accusé, envoi du K-bis, de l'attestation de vigilance et de la facture d'acompte ; démarrage à l'encaissement seulement. *Ambitieux* : cadrage commencé mi-décembre | **Greffe** : K-bis [HY : 1 à 3 semaines]. **Entité de GianLuca** : échéance annoncée de l'aide régionale le 31 déc. [DR] (`travaux/syn-droit.md:71`) | Facture d'acompte émise | — |

En scénario prudent, les semaines 5 à 8 glissent en janvier 2027. En ambitieux, le rendez-vous a lieu en semaine 4 et l'immatriculation début décembre (`travaux/strategie-retenue.md:500`).

### 6.2 Mois par mois, de janvier à novembre 2027

Capacité vendable : binôme, scénario central, sous le plafond de 10 JP (06-fonctionnement-a-deux.md, section 3.7) [ES]. JP vendues et encaissements TTC : modèle central (`modele-financier/scenarios.md:131-141` ; `modele-financier/tresorerie-18-mois.md:73-83`) [ES]. Probabilité cumulée : paramètre de jugement, conditionnel à la vente du cadrage (`modele-financier/tresorerie-18-mois.md:146`) [HY].

| Mois (mois de contrat) | Marwin : actions et responsables | GianLuca ou tiers | Jalons | Capacité vendable | JP vendues (modèle) | Encaissements TTC | Probabilité cumulée |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Janv. 2027 (1) | **Morgan** (5 JP) **et Mathys** (3 JP) : cadrage dès l'encaissement ; mesure de référence de P1 sur deux semaines ; comparaison avec un salarié refaite aux règles de 2027 (`travaux/ver-R6-marche.md:72`). **Mathys** : démonstrateurs P2 (format, données fictives) et P3 (corpus filtré), dans le plafond de 8 JP. **Morgan** : prospection | **GianLuca** : acompte (cible : ven. 8 janv.) ; pièces et accès sous 10 jours ouvrés ; entretien de 2 à 3 h sur place. **Expert-comptable** : simulations refaites avec les lois de finances et de financement de la sécurité sociale pour 2027 (`travaux/syn-droit.md:72`). **Chaque associé éligible** : demande d'ACRE sous 60 jours [IN] (`travaux/syn-droit.md:73`) | Ven. 29 janv. : cadrage payé, sinon report sans date (6) | 10 | 6,0 | 3 900 € | 1,00 |
| Févr. 2027 (2) | **Morgan** : remise du dossier ; restitution de 1 h 30 ; réception expresse demandée ; revue des 90 jours le mar. 2 févr. **Les deux** : préalables de la voie, puis pilote, semaines 1 à 3 | **GianLuca** : solde sous 8 jours ; réserves éventuelles sous 10 jours ouvrés ; choix écrit de la voie ; délégué nommé ; préalables (voie a : contrat de l'article 28, art. 34, œuvres, avis fiscal, appelant) | Revue des 90 jours (7) ; choix de la voie (8) | 10 | 8,8 | 11 000 € | 0,60 |
| Mars 2027 (3) | **Les deux** : pilote, semaines 4 à 7 ; revue de la 4e semaine ; bilan mesuré vers le ven. 19 mars. **Morgan** : proposition du socle B1 ; facture du premier mois le jeu. 25 mars si elle est acceptée | **GianLuca** : décisions sous 5 jours ouvrés ; adoption (comptes rendus commentés, registre consulté) ; décision écrite sur le socle avant le 25 mars | Revue de la 4e semaine (9) ; décision sur le socle (10) | 10 | 6,8 | 8 500 € | 0,60 |
| Avr. 2027 (4) | **Les deux** : fin du pilote et livraison du lot ; B1 démarre le jeu. 1er avril (mandat de 500 € HT par acte et 1 500 € HT par mois et par entité, `travaux/strategie-retenue.md:590`) ; première rémunération si B1 est payé. **Mathys** : restauration dans un espace neuf. Congés décalés : 5 jours | **GianLuca** : B1 payé d'avance ; mandat écrit par entité | — | 9,2 | 8,9 | 7 100 € | 0,42 |
| Mai 2027 (5) | **Les deux, avec l'expert-comptable** : bilan des 6 mois le mar. 4 mai ; taux de référence révisé. **Morgan** : rapport mensuel ; un lot devisé ; proposition payante à un autre client envoyée au plus tard le 4 mai | **GianLuca** : commande éventuelle d'un lot. Les autres rôles (bureaux, emploi) ne se discutent qu'après ce bilan, par accord séparé (`travaux/strategie-retenue.md:629-631`) | Bilan des 6 mois (11) | 10 | 8,9 | 9 600 € | 0,42 |
| Juin 2027 (6) | **Les deux** : bilan du 3e mois du socle ; choix d'un processus candidat à l'exploitation. **Morgan** : proposition de renouvellement, avec la comparaison des coûts d'un coordinateur salarié si elle s'impose | **GianLuca** : premier renouvellement signé avant le ven. 25 juin | Renouvellement 1 ; B2 ou D ouverts ? (12) | 10 | 8,9 | 9 600 € | 0,42 |
| Juil. 2027 (7) | **Mathys** : exploitation D au plus tôt, si ses conditions sont réunies. **Morgan** : variante du second client (2 000 € HT par mois à partir du mois 7) ; K-bis et attestation de vigilance remis à nouveau. **Les deux** : août planifié sans livraison de lot | **Entité qui vend** (voie a) : règlement européen anti-blanchiment, marchands d'art dès 10 000 €, le 10 juil. (`travaux/syn-droit.md:76`) | — | 10 | 8,9 | 9 600 € | 0,34 |
| Août 2027 (8) | **Les deux** : socle seul ; congés décalés (10 jours) ; aucune livraison de lot | — | — | 6,2 | 8,9 | 9 600 € | 0,34 |
| Sept. 2027 (9) | **Mathys** : facturation électronique en émission le mer. 1er sept. ; exercice de sortie à blanc complet. **Morgan** : second client signé, sinon dépendance assumée par écrit | **GianLuca** : second renouvellement signé avant le ven. 24 sept. **Expert-comptable** : plateforme d'émission | Second client ; renouvellement 2 ; sortie testée (13) | 10 | 8,9 | 9 600 € | 0,34 |
| Oct. 2027 (10) | **Mathys** : mesures des 12 mois ; calcul du partage des gains. **Morgan** : préparation du bilan annuel. Congés décalés : 5 jours | — | — | 8,6 | 8,9 | 9 600 € | 0,27 |
| Nov. 2027 (11) | **Les deux, avec l'expert-comptable** : bilan annuel le jeu. 4 nov. ; tarifs de l'année 2 ; préparation de la clôture prévue au 31 déc. 2027 [HY]. Aucune discussion d'investissement avant deux renouvellements, et pas avant 12 à 24 mois (`travaux/strategie-retenue.md:632`) | **GianLuca** : décision sur l'année 2 | Bilan annuel (14) | 10 | 8,9 | 9 600 € | 0,27 |

**Août et octobre.** Le modèle compte 8,9 JP vendues ces mois-là, pour 6,2 et 8,6 JP vendables. Le socle se tient ; le travail d'un lot passe à juillet ou à septembre. Le total annuel ne change presque pas [ES]. Le décalage se règle dans la revue mensuelle de capacité de juin, pas en août.

### 6.3 Dates extérieures qui pèsent sur le calendrier

| Date | Échéance | Qui | Effet sur la feuille de route | Source |
| --- | --- | --- | --- | --- |
| 5 nov. 2026, heure inconnue | Fin du délai de 72 h pour notifier la CNIL, si la connaissance date du 2 nov. | Responsable du traitement, non désigné [IN] | Jalon 1 ; s'il est passé, notification en retard motivée | `travaux/syn-droit.md:66, 623` |
| 1er déc. 2026 et 1er janv. 2027 | Doublements de prix annoncés chez un fournisseur d'IA | Marwin | Choix des outils ; deux fournisseurs configurés | `travaux/ver-R6-marche.md:33` ; `travaux/strategie-retenue.md:532` |
| 2 déc. 2026 | AI Act : marquage des contenus générés pour les systèmes déjà sur le marché | Fournisseurs ; Marwin si elle livre un assistant à son nom | À vérifier avant tout outil livré sous le nom de Marwin | `travaux/syn-droit.md:67` ; `travaux/strategie-retenue.md:559` |
| 31 déc. 2026 | Déclaration de CFE 1447-C-SD si la société est créée en 2026 | Marwin, avec l'expert-comptable | Semaine 7 ou 8 | `travaux/syn-droit.md:70` |
| 31 déc. 2026 | Échéance annoncée des aides régionales, « dans la limite des crédits » | Entité de GianLuca | Dossier déposé avant la signature du cadrage [DR] | `travaux/syn-droit.md:71` |
| Janvier 2027 | Nouvelles règles d'IS, de cotisations et d'ACRE (lois de 2027) | Expert-comptable | Simulations à refaire | `travaux/syn-droit.md:72` |
| 60 jours après le début d'activité | Demande d'ACRE, si l'un des associés est éligible [IN] | Chaque associé | Janvier ou février 2027 | `travaux/syn-droit.md:73` |
| Tous les six mois | K-bis et attestation de vigilance remis au client | Marwin | À la signature, puis vers juillet 2027 | `travaux/strategie-retenue.md:87` |
| 10 juil. 2027 | Règlement européen anti-blanchiment : marchands d'art dès 10 000 € | Entité qui vend | Voie (a) : Marwin n'encaisse jamais pour la galerie | `travaux/syn-droit.md:76` ; `travaux/strategie-retenue.md:649` |
| 1er sept. 2027 | Émission des factures électroniques pour les PME | Marwin | Livrable 7 de l'horizon 12 mois | `travaux/syn-droit.md:77` |
| Décembre 2027 | Première CFE réduite possible si la société est créée en décembre 2026 | Marwin | Non modélisée [IN] | `modele-financier/tresorerie-18-mois.md:142` |

---

## 7. Jalons de décision et points de non-retour

### 7.1 Jalons de décision

| N° | Date | Question | Qui décide | Sur quelles pièces | Si oui | Si non |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Jeu. 5 nov. 2026 | Notifier la CNIL, et comment ? | Le responsable du traitement [IN] ; en pratique Mathys et Morgan, avec l'avocat ou le DPD | Fiche de violation ; capture du dépôt | Notification, échelonnée si le dossier est incomplet [HY] | Non-notification motivée et documentée ; échéance passée : notification en retard motivée (`travaux/syn-droit.md:623`) |
| 2 | Jeu. 19 nov. 2026 | Les associés s'engagent-ils par écrit : stratégie, Medhi, SAS, CRM, au moins 6 JP facturables à deux, revenu modeste, apport ? | Morgan et Mathys | Fiche « rôles et disponibilités » | On prépare le client | Rien n'est proposé au client ; report (`travaux/strategie-retenue.md:54-56`) |
| 3 | Du jeu. 19 au ven. 27 nov. 2026 | Peut-on écrire à GianLuca ? | Morgan, validé par Mathys | Jalons 1 et 2 tenus ; documents conformes ; texte de l'incident validé | Message de recadrage envoyé ; rendez-vous demandé | Rien ne part ; on attend la pièce manquante |
| 4 | Mar. 15 déc. 2026 | Entité nommée et rendez-vous tenu ? | Constat des deux associés | Compte rendu ; fiche de l'entité | Engagement écrit demandé | Report à janvier, sans production (`travaux/strategie-retenue.md:697`) |
| 5 | À l'engagement écrit (au plus tôt fin novembre) | Immatriculer ? | Morgan et Mathys | Engagement d'une entité identifiée ; statuts et pacte ; apport | Signature, dépôt, assurance, banque | Statuts et pacte restent prêts, non signés (`travaux/strategie-retenue.md:552`) |
| 6 | Ven. 29 janv. 2027 | Cadrage commandé et payé ? | Constat | Acompte encaissé | Cadrage en cours | Report sans date ; temps réorienté (`travaux/strategie-retenue.md:698`) |
| 7 | Mar. 2 févr. 2027 | L'horizon des 90 jours est-il tenu ? Calendrier central ou prudent ? | Les deux associés | Livrables de la section 3.2 ; date de restitution | Calendrier central | Calendrier prudent (section 3.10) |
| 8 | 30 jours au plus après la restitution | Quelle suite ? | GianLuca, par écrit | Dossier de cadrage ; comparaison chiffrée des trois suites | Pilote de la voie choisie | Arrêt propre ; il garde le dossier (`travaux/strategie-retenue.md:237`) |
| 9 | 4e semaine du pilote | Critères d'adoption tenus ? | Les deux associés ; le délégué de GianLuca pour l'adoption | Mesures hebdomadaires | On poursuit | Abandon du processus ; retour au manuel |
| 10 | Avant le jeu. 25 mars 2027 | Socle récurrent au 1er avril ? | GianLuca, par écrit | Bilan mesuré du pilote | B1 au 1er avril | Lot seul, ou fin propre ; socle au 1er mai si le bilan n'est complet qu'en avril |
| 11 | Mar. 4 mai 2027 | Le pilotage borné est-il utile et rentable ? | Les deux, avec l'expert-comptable ; GianLuca pour la suite | Bilan du pilote ; relevé du temps ; coût complet mesuré | Poursuite ; taux révisé ; autres rôles discutables par accord séparé | Réduire, sortir, garder d'autres revenus |
| 12 | Ven. 25 juin 2027 | Premier renouvellement ; B2 ou D ? | GianLuca (renouvellement) ; Marwin (proposition) | Trois rapports mensuels ; critères | Renouvellement ; D ou B2 si leurs conditions sont réunies (`travaux/strategie-retenue.md:272, 344`) | Réduction de palier ou fin, avec réversibilité |
| 13 | Ven. 24 sept. 2027 | Second renouvellement ? Second client ? Sortie testée ? | GianLuca ; Morgan et Mathys | Contrat d'un autre client ; test de restitution | Dépendance en baisse | Dépendance assumée par écrit ; cible ≤ 80 % au mois 18 (`travaux/strategie-retenue.md:522`) |
| 14 | Jeu. 4 nov. 2027 | Continuer, réduire ou arrêter ; à quel prix l'année 2 ? | Les deux ; GianLuca ; expert-comptable | Bilan annuel ; gains mesurés | Année 2, avec un tiers des gains mesurés rendu au client | Relever les forfaits, réduire le périmètre ou sortir |

À chaque jalon, les probabilités de passage du modèle sont remplacées par le fait observé (`travaux/strategie-retenue.md:502`).

### 7.2 Points de non-retour

Un point de non-retour est un acte après lequel revenir en arrière coûte cher ou devient impossible. Chacun a une condition préalable écrite.

| Acte | Ce qui devient irréversible | Au plus tôt | Condition préalable | Comment limiter le risque |
| --- | --- | --- | --- | --- |
| Laisser passer l'échéance de la CNIL sans décision | Retard à motiver ; crédibilité entamée auprès du client et de l'assureur | 5 nov. 2026 | — | Décision documentée, même si le dossier est incomplet |
| Informer GianLuca de l'incident | Déclaration écrite opposable | Semaines 2 à 4 | Termes validés par le conseil | Pas de reconnaissance de responsabilité non pesée (`travaux/strategie-retenue.md:809`) |
| Envoyer le message de recadrage | L'offre de six mois est retirée aux yeux du client ; revenir à 15 000 € par mois n'est plus crédible | 19 nov. 2026 | Jalons 1 et 2 ; texte de l'incident validé | Message signé des deux ; il propose aussitôt le cadrage |
| Signer les statuts, déposer le capital, immatriculer | Apport immobilisé ; 5 000 à 7 000 € HT de démarrage dépensés ; obligations comptables, fiscales et de facturation électronique | Dès l'engagement écrit | Jalon 5 | Statuts prêts mais non signés avant l'engagement ; abonnements et frais résiliables au mois (`modele-financier/scenarios.md:205`) |
| Signer le bon de commande du cadrage | Aide régionale perdue si le dossier n'a pas été déposé avant [DR] ; délai de rétractation de 14 jours possible [HY] | Décembre 2026 | Dossier d'aide déposé si l'entité le veut ; contrat-cadre relu | Signature à distance, ou délai de 7 jours prévu au calendrier (`travaux/strategie-retenue.md:466`) |
| Encaisser un acompte | Obligation de livrer ; responsabilité de Marwin engagée | À l'immatriculation | RC professionnelle souscrite, fuite déclarée | Travail démarré à l'encaissement seulement |
| Mettre une donnée personnelle réelle dans un outil | Exposition et transfert non réversibles | Pilote, février 2027 | Les préalables de `travaux/strategie-retenue.md:669` | Offres professionnelles, clauses types, comptes au nom de l'entité |
| Signer un socle récurrent | Trois mois de capacité nominative réservée ; préavis d'un mois | Avril 2027 | Pilote réussi ; disponibilités écrites | Pas de tacite reconduction ; changement de palier sans pénalité si un associé est absent plus de 10 jours ouvrés (`travaux/strategie-retenue.md:281`) |
| Réduire durablement ses autres revenus (Morgan : OLSEN et autres projets ; Mathys : situation [IN]) | Revenu personnel dépendant à 100 % d'un client, ≈ 1 100 à 1 500 € nets par mois en central [ES] (`modele-financier/scenarios.md:67`) | Pas avant le second renouvellement du socle (fin sept. 2027) et un second client | Bilan du mois 6 ; second client | Les associés « doivent garder d'autres revenus » jusqu'au deuxième renouvellement (`modele-financier/stress-tests.md:343`) |
| Accepter un autre rôle de GianLuca (bailleur, employeur, investisseur) | Dépendance croisée ; le capital est le plus difficile à défaire | Bureaux ou emploi : après le bilan du mois 6 ; capital : après deux renouvellements, 12 à 24 mois | Accord séparé pour chaque rôle | Jamais contre une baisse d'honoraires (`travaux/strategie-retenue.md:629-632`) |
| Recruter | Masse salariale fixe | Après trois mois au-delà de 85 % d'occupation | Contrat renouvelé qui finance le poste | Sous-traitance d'un lot d'abord (`travaux/strategie-retenue.md:623`) |

L'exploitation d'un processus (offre D) n'est pas un point de non-retour : le mode manuel est toujours conservé et testé (`travaux/strategie-retenue.md:344`).

---

## 8. Ce qui dépend de Marwin, de GianLuca et des tiers

| Horizon | Sous le contrôle de Marwin | Dépend de GianLuca ou de son entité | Dépend de tiers |
| --- | --- | --- | --- |
| 90 jours | Mesures techniques sur la fuite, si Marwin contrôle l'organisation FinanceScope [IN] ; documents ; arrêt du travail gratuit ; accord des associés ; apport ; statuts prêts ; message de recadrage ; prix ; prospection | Rendez-vous ; entité ; engagement écrit ; acompte ; pièces et accès sous 10 jours ouvrés ; entretiens ; réception ; choix de la suite | Avocat ou DPD ; expert-comptable ; greffe ; banque ; assureur ; Région ; Medhi (réaction au retrait) |
| 6 mois | Qualité et délais des livrables ; mesures ; contrôle à quatre yeux ; coût par résultat accepté ; restauration ; occupation ; proposition à un autre client | Voie ; délégué ; décisions sous 5 jours ouvrés ; préalables RGPD ; œuvres, structure vendeuse et appelant (voie a) ; personne désignée (voie c) ; adoption ; socle ; paiements | Conseil fiscal du client ; Quali Contact ; fournisseurs d'IA |
| 12 mois | Rapports ; renouvellements proposés sur preuves ; gains mesurés ; sortie testée ; facturation électronique ; second client ; bilan | Renouvellements ; adoption durable ; arbitrages entre projets ; ventes d'œuvres, galerie, lieux (suivis, jamais promis) | Expert-comptable ; avocat ; prestataires du client ; organisateur légal et autorités pour un événement |

**Règle de lecture** [PR]. Les indicateurs qui dépendent de GianLuca (ventes, rendez-vous, décisions prises, adoption) sont suivis à part de ceux que Marwin contrôle (qualité, délais, coût par résultat accepté) (`travaux/strategie-retenue.md:159`). Ils ne retardent jamais un paiement : la livraison déclenche le solde, l'adoption décide de la suite (`travaux/strategie-retenue.md:287`). Le silence de GianLuca ne vaut pas accord : relance à 5 jours ouvrés, report des jalons à 10, revue du contrat à 15 (`travaux/strategie-retenue.md:603`).

**Ce qu'un retard de GianLuca change.** Le calendrier glisse, sans dépense. La capacité réservée va à la prospection ou à la capitalisation, jamais à une production non commandée.

---

## 9. Comment tenir la feuille de route

- **Point du lundi** (30 min) et **revue mensuelle de capacité** (avant le 5e jour ouvré) : rituels de 06-fonctionnement-a-deux.md, section 10.1. La feuille de route y est relue ligne par ligne : fait, en retard, bloqué, et par qui.
- **Une version datée à chaque jalon**, avec la liste des dates déplacées et leur raison. Les versions précédentes sont gardées.
- **Registre « décision → documents touchés »** : chaque décision de jalon met à jour les documents concernés (`travaux/strategie-retenue.md:86`).
- **Obligations récurrentes de Marwin** : déclaration de TVA, mensuelle dans le modèle [HY, régime à arrêter avec l'expert-comptable] (`modele-financier/tresorerie-18-mois.md:62`) ; K-bis et attestation de vigilance tous les six mois ; revue trimestrielle du pacte.
- **Comité mensuel avec GianLuca** à partir du pilote. Il ne voit que les jalons qui le concernent (choix de la voie, socle, renouvellements), jamais les probabilités, les marges ni les dates butoirs internes (`travaux/strategie-retenue.md:785-791`).

---

## 10. Recommandations : preuve, hypothèse, limite, décision

| Recommandation [PR] | Preuve | Hypothèse | Limite | Décision correspondante |
| --- | --- | --- | --- | --- |
| Suivre strictement l'ordre : fuite, documents, accord des associés, puis client | Dépôt public le 4 nov. [DR] (`interne/contexte-projet-carlone.md:11`) ; problème connu au plus tard le 2 nov. [FV] (`interne/audit-marwin-tech-carlone.md:3, 15`) ; décision du 4 nov. appliquée à 1 support sur au moins 5 [FV] (`travaux/syn-capacite-ia.md:699`) | Il s'agit d'une violation au sens du RGPD [HY] | Visibilité du dépôt non revérifiée par l'audit ; responsable du traitement [IN] | Jalons 1 à 3 |
| Immatriculer seulement sur engagement écrit d'une entité identifiée | Marwin « n'existe pas encore » [DR] (`interne/offre-marwin-tech-remuneration-et-collaboration.md:153`) ; aucune entité payeuse [FV négatif] (`travaux/syn-sources.md:39`) | Délai de 1 à 3 semaines [HY] | Date de création et CFE à arrêter avec l'expert-comptable | Jalon 5 |
| Tenir les dates butoirs du 15 déc. et du 31 janv. | Aucun rendez-vous fixé [FV, agenda de Morgan] (`travaux/note-point-4-novembre-et-activites.md:5`) ; 36 propositions OLSEN jamais envoyées [DR] (`travaux/note-point-4-novembre-et-activites.md:9`) | Un rendez-vous peut être obtenu en décembre | Agenda de GianLuca [IN] | Jalons 4 et 6 |
| Tolérer la réception du cadrage jusqu'au 31 mars, sans toucher à la règle du 31 janv. | Enchaînement immatriculation, acompte, 3 à 4 semaines de cadrage, réserves (`travaux/strategie-retenue.md:230, 235, 458, 486`) | Délais du greffe et des fêtes [HY] | Ce n'est qu'une lecture de ce livrable | Jalon 2, puis jalon 7 |
| Un pilote de huit semaines dans une seule voie, critères fixés avant | Besoins rapportés, jamais entendus directement [DR] (`sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:13` ; `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:13`) ; aucune parole directe [FV négatif] (`travaux/syn-sources.md:38`) | GianLuca choisira sur pièces | L'adoption dépend de lui et de ses équipes | Jalons 8 à 10 |
| Socle au plus tôt en avril 2027, plafonné à 10 JP facturables par mois | 20 JP par mois prenaient 78 à 83 % du temps des deux associés [ES] (`travaux/strategie-retenue.md:41`) ; capacité centrale ≈ 10 JP [ES] (06-fonctionnement-a-deux.md, section 3.9) | Disponibilités de 65 % et 50 % | Disponibilités non écrites [IN] | Jalons 10 et 11 |
| Aucune décision personnelle irréversible avant le second renouvellement et un second client | Net central ≈ 1 100 à 1 500 € [ES] (`modele-financier/scenarios.md:21`) ; valeur pondérée ≈ 38 300 € HT [ES] (`modele-financier/scenarios.md:45`) | Probabilités de passage [HY] | Situations personnelles et fiscales [IN] | Jalons 11 et 13 |
| Aucune livraison de lot en août ni fin décembre | Capacité ≈ 6,2 JP en août [ES] (06-fonctionnement-a-deux.md, section 3.7) | Congés pris aux mêmes périodes | Dates de congés à écrire dans la fiche | Fiche « rôles et disponibilités » (jalon 2) |

---

## 11. Limites et inconnues

- **Toutes les dates après le 15 déc. 2026 sont conditionnelles.** Elles supposent un rendez-vous, une entité et un acompte que rien ne garantit [IN].
- **Aucune parole directe de GianLuca** dans les pièces : les voies du pilote répondent à des besoins rapportés par Morgan [DR]. 50 conversations ChatGPT restent non lues (`sources/reprise-59-et-visuels-2026-11-04.md:14`) ; des promesses faites au client peuvent exister hors du corpus (`travaux/strategie-retenue.md:835`).
- **Disponibilités de Morgan et de Mathys non écrites** [IN]. Sans fiche signée, seul le scénario prudent est défendable (`travaux/strategie-retenue.md:840`).
- **Délais des tiers** (greffe, avocat, assureur, Région) estimés, non mesurés [HY]. La couverture d'assurance d'un incident déjà connu est douteuse [HY].
- **Points juridiques marqués [HY]** (rétractation appliquée au contrat de Marwin, notification échelonnée, rôles RGPD) : à soumettre à l'avocat ou au DPD (`travaux/strategie-retenue.md:839`).
- **Montants** : estimations du modèle financier, sans simulation officielle. IS, TVA et cotisations sont à refaire en janvier 2027 avec l'expert-comptable (`modele-financier/scenarios.md:227`).
- **Les totaux de 25 400 € HT et de 73 400 € HT** sont des sommes faites pour ce livrable à partir du modèle ; ils ne sont pas pondérés par les probabilités.
- **Les tests d'échec sont appliqués un par un** dans le modèle ; un cumul (retard de paiement et absence d'un associé, par exemple) aggraverait les besoins (`modele-financier/stress-tests.md`, section 4).

Relu et contrôlé le 4 novembre 2026 : 34 vérifications, 8 corrections.
