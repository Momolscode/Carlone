# Catalogue des offres

Audit Marwin Tech × GianLuca Carlone · livrable 4 sur 15 · 4 novembre 2026
Statut : interne (contient coûts, marges et planchers ; ne pas transmettre à GianLuca Carlone)
Sources principales : `travaux/strategie-retenue.md` (sections 4, 5 et 9) ; `travaux/syn-portefeuille.md` ; `modele-financier/scenarios.md` ; `travaux/calculs/arbitre-calc/verif.py` ; pièces d'origine du dépôt Momolscode/Carlone (commit 7b46602) et copie du 4 nov. du diaporama client, rouvertes en lecture seule.
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu. Sauf mention, [PR] désigne une proposition de la stratégie retenue ; « [PR, précision] » signale une règle ajoutée par ce livrable. JP : journée-personne de 7 h ; deux associés présents une journée consomment 2 JP. Prix hors taxes (HT) ; TTC = HT × 1,2, la TVA étant facturée dès la première facture (`travaux/strategie-retenue.md:462`). Coûts, planchers dérivés et marges sont des [ES]. Les chemins `slides/…` renvoient à la copie du 4 nov. du diaporama client « Offre Marwin Tech pour Carlone », hors dépôt (11 vues).

**Ce que ce livrable ajoute** : une fiche complète par offre, y compris pour chaque lot ; les planchers tirés de la règle des 750 € ; les marges recalculées ; la compatibilité des offres avec le plafond de 10 JP par mois ; trois écarts avec la stratégie (deux de calcul, un de présentation) signalés en encadré. **Ce qu'il ne refait pas** : les chantiers et les acheteurs (03-cartographie-projets.md), la charge et la saturation (06-fonctionnement-a-deux.md), les protocoles d'essai (07-processus-ia-et-essais.md), la trésorerie (09-modele-economique-tresorerie.md), le texte commercial (11-proposition-commerciale-revisee.md ; pour-gianluca/proposition-de-cadrage.md), les clauses du contrat (12-gouvernance-contrat-sortie.md).

---

## En bref

1. **Pas d'abonnement général.** Marwin vend des prestations séparées : une remise en ordre interne (0), un cadrage (A), un socle de pilotage (B0, puis B1 ou B2), huit lots devisés (C1 à C8), une exploitation de processus (D) et des avenants (E). Chacune a son bon de commande, son entité, son prix, sa réception et sa sortie [PR] (`travaux/strategie-retenue.md:184-190`).
2. **Une seule offre se vend aujourd'hui : le cadrage A**, 6 500 € HT, moitié à la commande. Les autres dépendent de son résultat et de conditions écrites (`travaux/strategie-retenue.md:42-43`).
3. **Le temps sert à mesurer, pas à vendre.** Le taux de 750 € HT devient un plancher interne, jamais montré ni remisé. Le prix cible est de 800 à 950 € par JP estimée (`travaux/strategie-retenue.md:393-401`).
4. **Les marges de la première année sont minces.** Avec au plus 10 JP facturées par mois, une JP coûte 710 à 885 € [ES]. La plupart des offres vont d'une marge un peu négative à environ 30 %. Le cadrage est peu rentable par choix ; les offres récurrentes sont révisées au mois 6 sur le coût mesuré.
5. **Sont retirés** : les formules à 15 000 et 30 000 € HT, l'acompte de 7 500 €, l'engagement de six mois, l'« ancre » de 46 JP, les options laboratoire et création (section 6).
6. **Trois écarts avec la stratégie, deux de calcul et un de présentation** (encadrés des sections 3.2, 3.3 et 3.6) : le détail du cadrage fait 8,5 JP et non 8 ; le socle B1 peut demander 6 JP et non 5,5 ; l'avenant E montre un prix au temps alors que les documents client n'en montrent aucun. Aucun ne change un prix. Chacun change une règle de contrôle.

---

## 1. Principes

| N° | Principe [PR] | En pratique | Source |
| --- | --- | --- | --- |
| 1 | **Pas d'abonnement général** | Retour à l'architecture du 30 oct. : « Un contrat-cadre organise la collaboration ; des fiches de mission précisent les projets réellement engagés » [FV] (`interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 2). Le 2 nov., un abonnement de six mois l'avait remplacée et couvrait CRM, campagnes, catalogue, Jarvis, établissements, séjours et événements (`travaux/syn-sources.md:240`). Aucune prestation n'en absorbe une autre | `travaux/strategie-retenue.md:184` |
| 2 | **Un bon de commande par prestation et par entité** | Chaque bon nomme l'entité (dénomination, SIREN), le signataire, le payeur et le valideur. Rien n'est adressé « à Carlone » en général : aucune entité de GianLuca n'est nommée dans le dépôt [FV négatif] (`travaux/syn-portefeuille.md:280, 306`) | `travaux/strategie-retenue.md:185` |
| 3 | **Prix au livrable ou au périmètre** | Forfait par livrable (A, C) ; prix mensuel par périmètre (B) ; minimum plus prix par résultat accepté (D). Le relevé mensuel des JP est une preuve, pas une base de facture | `travaux/strategie-retenue.md:186` |
| 4 | **Marwin prépare, organise et coordonne** | Elle n'exécute ni l'administratif courant, ni la comptabilité, ni le conseil juridique ou fiscal, ni les obligations d'exploitant, d'organisateur ou de vendeur. Elle prépare les dossiers pour les professionnels | `travaux/strategie-retenue.md:187` ; `travaux/syn-droit.md:410-431` |
| 5 | **Marwin n'avance jamais d'argent** | Achats, abonnements, prestataires, photographe, appels : commandés et payés par l'entité cliente, à son nom. Ils ne sont pas dans le chiffre d'affaires de Marwin. Exposition de Marwin à ce titre : 0 € | `travaux/strategie-retenue.md:188, 445` |
| 6 | **Comptes au nom du client dès le premier jour** | Registre, tableau de bord, CRM, outils : comptes de l'entité ; Marwin y intervient comme collaborateur. C'est la condition d'une réversibilité réelle (`travaux/syn-droit.md:512`) | `travaux/strategie-retenue.md:189` |
| 7 | **Rien d'exploratoire sans financeur écrit** | STRATES, Éclosion, laboratoire, DGX Spark : hors catalogue (section 6) | `travaux/strategie-retenue.md:190, 639-654` |
| 8 | **Le paiement suit la nature de la prestation** | Temps réservé : d'avance. Livrables : acompte, puis solde à la livraison. Consommation variable : fin de mois. Le travail démarre à l'encaissement | `travaux/strategie-retenue.md:429-434` |
| 9 | **La livraison déclenche le paiement ; l'adoption décide de la suite** | Marwin est payée pour ce qu'elle contrôle (un livrable conforme), pas pour ce qui dépend du client (recruter, appeler, utiliser) | `travaux/strategie-retenue.md:113, 287` |
| 10 | **Le silence ne vaut ni accord ni approbation** | Sans réserve motivée sous 10 jours ouvrés, le solde devient exigible au plus tard 30 jours après la remise, pour la facturation seulement. La clause « réputé accepté » (`interne/offre-marwin-tech-remuneration-et-collaboration.md:206`) est retirée | `travaux/strategie-retenue.md:604` |

### 1.1 Comment lire les coûts et les marges

- **Coût complet d'une JP facturable** [ES] = (rémunération chargée des associés au prorata de leur temps pour Marwin, sur la base de 2 500 € nets par équivalent temps plein, coefficient SAS de 1,7 à 1,9 ; plus frais fixes de 1 500 à 2 500 € par mois) ÷ JP facturables ÷ 0,9 pour la réserve de 10 % (`travaux/strategie-retenue.md:359` ; `travaux/calculs/arbitre-calc/verif.py` § 1).

| Situation | JP facturables par mois | Coût complet par JP [ES] |
| --- | --- | --- |
| Prudent (Morgan 50 %, Mathys 25 %) | ≈ 7 | 744 à 962 € |
| Central, capacité pleine | ≈ 12 | 591 à 737 € |
| **Central, plafond de la première année** | **10** | **710 à 885 €** |
| Haut (90 % chacun) | ≈ 20 | 508 à 614 € |

- **Marge** = (prix − JP × coût complet) ÷ prix. À marge nulle, l'offre paie les associés 2 500 € nets par ETP, les frais fixes et la réserve, sans rien de plus. Une marge négative veut dire que les associés gagnent moins que ce repère. C'est le cas attendu de la première année : ≈ 1 100 à 1 500 € nets par associé et par mois en régime central, à partir du mois 4 et avant impôt sur le revenu [ES] (`modele-financier/scenarios.md:67`). La stratégie retenue indiquait 1 350 à 1 550 € ; le modèle financier est plus bas parce qu'il compte l'impôt sur les sociétés et les délais d'encaissement (`modele-financier/scenarios.md:21`).
- **La colonne « 10 JP » est la plus réaliste la première année**, puisque la capacité engagée est plafonnée à 10 JP facturables par mois (`travaux/strategie-retenue.md:485`).
- Une marge suppose que l'estimation en JP tient. Un dépassement de 50 % sur un lot de 6 000 € coûte ≈ 2 000 à 2 750 € de temps non payé (`travaux/strategie-retenue.md:531`).

---

## 2. Vue d'ensemble

| Code | Offre | Nature du prix | Prix proposé HT (TTC) [PR] | Plancher interne [ES] | JP [ES] | Durée | Paiement | Au plus tôt |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Remise en ordre | Non facturée | 0 € | — | 9 à 17 sur les mois 0 à 2 | Dès maintenant ; l'essentiel en novembre 2026 | — | Immédiat |
| A | Cadrage « inventaire, priorités, mandat » | Forfait | **6 500 €** (7 800 €) | 6 000 € | 8 (8,5 au détail, encadré 3.2) | 3 à 4 semaines | 50 % commande ; 50 % réception | Après l'offre 0 et l'immatriculation |
| A réduit | Cadrage réduit | Forfait | **4 800 €** (5 760 €) | 4 500 € | 6 | [IN] ; repère 2 à 3 semaines [HY] | Idem | Si le prix complet est refusé |
| B0 | Socle pilote | Mensuel au périmètre | **3 500 €** par mois (4 200 €), soit 7 000 € sur deux mois | 3 000 € | 3 à 4 par mois | 8 semaines, sans reconduction tacite | D'avance | Après réception du cadrage (voie b) |
| B1 | Socle + 2 projets actifs | Mensuel au périmètre | **4 500 €** par mois (5 400 €) ; + 1 200 € (1 440 €) par projet actif en plus | 4 125 € ; 1 125 € par projet en plus | 4,5 à 5,5 (jusqu'à 6, encadré 3.3) | 3 mois, renouvelables par écrit | D'avance | Mois 4 |
| B2 | Socle + 4 projets actifs | Mensuel au périmètre | **6 900 €** par mois (8 280 €) | 6 750 € | 6,5 à 9 | 3 mois, renouvelables sous conditions | D'avance | Après 3 mois de B1 aux critères |
| C1 à C8 | Lots devisés | Forfait par lot | JP × 800 € + 10 à 15 % ; **C2 : 6 000 €** (7 200 €) ; **C6 : 7 500 €** (9 000 €) | 750 € × borne haute des JP estimées | 3 à 9 par lot | Selon le lot | 40 % / 60 % ; 40 / 30 / 30 au-delà de 8 JP | Après le cadrage |
| D | Exploitation d'un processus prouvé | Minimum + prix par résultat accepté | **1 000 à 1 500 €** par mois (1 200 à 1 800 €) + variable fixé après mesure | Jamais sous le coût manuel mesuré | 1 à 4 par mois | 6 mois renouvelables | Minimum d'avance ; variable en fin de mois | Mois 7 |
| E | Avenant de capacité, urgences | Au temps, sur bon écrit préalable | **900 € par JP** (1 080 €), demi-journée minimale | Aucune remise | Capacité restante | Ponctuelle | Fin de mois, sous 15 jours | Toujours dans le plafond |

Sources : prix, JP et durées (`travaux/strategie-retenue.md:194-203`) ; paiement (`travaux/strategie-retenue.md:436-445`). **Règle des planchers [PR, précision]** : 750 € × la borne haute des JP estimées. C'est la règle que la stratégie applique elle-même au cadrage (8 × 750 = 6 000 €), à B0 (4 × 750 = 3 000 €), à C2 (7 × 750 = 5 250 €) et à C6 (9 × 750 = 6 750 €) ; ce livrable l'étend à A réduit, B1, B2, aux projets supplémentaires et aux autres lots.

### 2.1 Enchaînement

Remise en ordre (0), puis cadrage (A). Après la restitution, GianLuca choisit **une seule voie** sur pièces, pour un pilote de huit semaines au plus, sans reconduction tacite (`travaux/strategie-retenue.md:243-251`) :

| Voie | Besoin rapporté [DR] | Offres | Prix total HT [PR] | Préalables |
| --- | --- | --- | --- | --- |
| (a) Ventes d'œuvres | Vendre aux entreprises de la Nièvre (`sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:13`) | C2 | 6 000 € | Ceux de la fiche C2 |
| (b) Pilotage | Une équipe qui relie les sujets et prépare les décisions (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:13`) | B0 (deux mois) et un lot, C1 ou C4 d'abord | ≈ 7 000 € + 2 700 à 6 400 €, soit ≈ 9 700 à 13 400 € (la stratégie écrit « 3 500 à 6 500 € » pour le lot ; correction expliquée dans l'encadré de 03-cartographie-projets.md, section 5.2) | Délégué nommé ; décisions sous 5 jours ouvrés |
| (c) Organisation interne | « Ne pas gérer chaque détail », sans payer l'exécution au prix du conseil | C6 | 7 500 € | Décision de désigner ou de recruter une personne |

Le socle récurrent B1 vient au plus tôt au mois 4, sur décision écrite. L'exploitation D vient au plus tôt au mois 7. Le calendrier est dans 08-feuille-de-route.md.

### 2.2 Compatibilité avec le plafond de 10 JP par mois

| Période | Combinaison | Charge [ES] | Sous 10 JP ? |
| --- | --- | --- | --- |
| Mois 1 | A seul | 8 à 8,5 JP sur 3 à 4 semaines | Oui ; rien d'autre pour ce client |
| Pilote (a) | C2 | 6 à 7 JP sur 6 à 8 semaines | Oui |
| Pilote (b) | B0 + un lot | 6 à 8 JP de socle et 3 à 7 JP de lot (C1 ou C4) sur deux mois, soit ≈ 4,5 à 7,5 JP par mois | Oui |
| Pilote (c) | C6 | 8 à 9 JP sur 4 à 6 semaines | Oui ; à la limite s'il est tenu en 4 semaines |
| Régime central (mois 4 à 12) | B1 + lots pour ≈ 3 500 € par mois | 4,5 à 6 JP + ≈ 4 JP, soit ≈ 8,5 à 10 JP | Oui, à la limite. Le modèle financier retient 8,9 JP vendues (`modele-financier/scenarios.md:38`) |
| Régime avec exploitation | B1 + 1 projet + D | 5,5 à 7,5 JP + 1 à 4 JP | Seulement si les lots s'arrêtent pendant ce temps |
| B2 + lots | B2 seul prend 6,5 à 9 JP | Il reste 1 à 3,5 JP pour les lots | Non en pratique la première année : B2 se vend sans lot, ou on propose C6 à la place |
| E | Avenants | Dans la capacité restante | Jamais au-delà de 10 JP sans révision écrite du plafond |

Alerte de capacité : au-delà de 90 % des JP réservées avant le 20 du mois, arrêt des travaux non urgents ; au-delà de 100 %, avenant ou report (`travaux/strategie-retenue.md:593`). Les seuils détaillés sont dans 06-fonctionnement-a-deux.md.

---

## 3. Fiches des offres

### 3.1 Offre 0 : remise en ordre (interne, non facturée)

| Rubrique | Contenu |
| --- | --- |
| **Client** | Aucun. C'est une obligation de Marwin et de ses associés |
| **Problème** | Violation de données probable : le dépôt FinanceScope/CRM-Carlone était public au 4 nov. selon une vérification par l'API GitHub [DR] (`interne/contexte-projet-carlone.md:11`), problème connu au plus tard le 2 nov. [FV] (`interne/audit-marwin-tech-carlone.md:3, 15`). Documents client contradictoires avec la décision du 4 nov. Structure, pacte et disponibilités non écrits. Travail gratuit qui s'accumule (`travaux/syn-portefeuille.md:304`) |
| **Résultat** | 1. **Fuite** : décision sur la notification à la CNIL avec un avocat ou un DPD avant l'échéance du 5 nov. (notification échelonnée ou retard motivé si nécessaire [HY]) ; dépôt rendu privé et vérifié ; copies contrôlées ; secrets révoqués ; fiche de violation ; décision sur l'information des personnes ; GianLuca informé par écrit dans des termes validés. 2. **Documents** : une seule version de l'offre ; pièces retirées marquées « historique » ; diaporama corrigé. 3. **CRM** : hébergement privé ; oppositions appliquées ; simulateur fiscal corrigé ou retiré : il applique un taux d'IS fixe de 25 % et calcule une « économie max » de 5 × plafond × 25 % [FV] (`crm/art_merge.py:19, 129`). 4. **Medhi** : décision écrite des deux associés et message à Medhi. 5. **Associés** : disponibilités nominatives, statuts et pacte prêts. 6. Aucun document de Marwin ou de Carlone dans le dépôt public BOJART. 7. Message de recadrage (pour-gianluca/message-de-recadrage.md) |
| **Périmètre** | Les sept points ci-dessus ; détail dans `travaux/strategie-retenue.md:211` |
| **Exclusions** | Toute nouvelle production pour GianLuca |
| **Dépendances** | Avocat ou DPD ; expert-comptable ; accord de Mathys |
| **Capacité** | 9 à 17 JP sur les mois 0 à 2, dont 3 à 6 pour la fuite et la conformité minimale [ES] (`travaux/syn-capacite-ia.md:216-220`) |
| **Durée** | Fuite : immédiat. Documents : au 13 nov. Message : au 19 nov. (`travaux/strategie-retenue.md:716`) |
| **Prix** | 0 €. L'exposition des données est de notre fait (`travaux/syn-portefeuille.md:115, 353`) |
| **Coûts** | Temps non rémunéré : ≈ 5 300 à 15 000 € au coût complet [ES, calculé ici : 9 × 591 à 17 × 885 €]. Sorties d'argent, payées sur l'apport des associés : conseil sur la fuite 1 000 à 3 000 € [HY] ; statuts et pacte 2 000 à 5 000 € HT [ES] ; formalités ; RC professionnelle [IN] (`travaux/strategie-retenue.md:214`) |
| **Marge** | Négative par construction |
| **Réception** | Dépôt privé vérifié ; fiche de violation ouverte ; décision datée et motivée ; documents conformes à la liste de `travaux/strategie-retenue.md:816-828` |
| **Paiement** | Aucun |
| **Conditions de poursuite** | Toutes les conditions minimales de `travaux/strategie-retenue.md:660-669`, sauf l'acompte. Si la fuite n'est pas traitée, rien ne démarre |

### 3.2 Offre A : cadrage « inventaire, priorités, mandat », et sa version réduite

| Rubrique | A complet | A réduit |
| --- | --- | --- |
| **Client** | L'entité de GianLuca désignée comme chef de file (dénomination, SIREN, signataire habilité, effectif). Payeur et valideur : la même entité, ou celles qu'elle désigne par écrit | Idem |
| **Problème** | Le portefeuille n'est connu qu'à travers Morgan [DR] ; aucune pièce ne contient une parole directe de GianLuca [FV négatif] (`travaux/syn-sources.md:38`). Aucune liste d'entités, de lieux, de priorités, de budgets ni d'accès. Marwin ne peut ni dimensionner ni chiffrer ; GianLuca ne peut pas comparer | Idem, avec un budget plus serré ou un refus du prix complet |
| **Résultat** | 1. Inventaire **validé par écrit** des entités, lieux, projets, interlocuteurs et accès. 2. Trois priorités à 90 jours, chacune avec un objectif mesurable, un budget indicatif, un responsable côté client, le coût actuel estimé avec lui et le seuil au-delà duquel un lot se rentabilise pour lui. 3. Carte des rôles par projet (exploitant, organisateur, vendeur, responsable du traitement) et professionnels à consulter. 4. Grille de délégation et projet de mandat par entité. 5. Décision écrite sur le CRM (exploiter ou non, au nom de quelle structure, qui appelle). 6. Canal de travail réel et personnes qui utiliseront les outils. 7. Registre des décisions ouvert sur un compte de l'entité, et mesure de référence du pilote P1 (registre et comptes rendus, `travaux/syn-capacite-ia.md:695`). 8. Comparaison chiffrée des trois voies, avec le coût d'un coordinateur salarié (`travaux/strategie-retenue.md:225`) | Livrables 1 et 2. Sans grille de délégation ni mandat (4), sans mesure de référence (7) (`travaux/strategie-retenue.md:231`). Le sort des livrables 3, 5, 6 et 8 n'est pas fixé par la stratégie : à décider avant de proposer cette version [IN] |
| **Périmètre** | Deux entretiens (2 à 3 h sur place, puis une restitution d'1 h 30) ; jusqu'à 15 pièces fournies ; un aller-retour de corrections ; un associé mène, l'autre contrôle | À fixer ; repère : mêmes entretiens, analyse plus courte [HY] |
| **Exclusions** | Conseil juridique ou fiscal ; étude détaillée de rentabilité d'un établissement (lot C7) ; tout contact avec des tiers ; CRM sur données réelles ; production de supports, de catalogue ou d'outils ; visites de plus d'une journée | Idem, plus les livrables 4 et 7 |
| **Dépendances** | Offre 0 terminée ; Marwin immatriculée ; entité identifiée et bon de commande signé ; acompte encaissé ; pièces et accès fournis sous 10 jours ouvrés ; deux entretiens tenus. Si l'entité veut l'aide régionale au conseil : dépôt du dossier avant toute signature [DR] (voir ci-dessous) | Idem |
| **Capacité** | 8 JP [ES] : Morgan 5, Mathys 3 (`travaux/strat-S2-pilotage.md:176`). Le détail par tâche fait 8,5 JP (encadré ci-dessous) | 6 JP [ES] |
| **Durée** | 3 à 4 semaines à partir de l'acompte et des pièces ; congés de fin d'année non comptés | [IN] ; repère 2 à 3 semaines [HY] |
| **Prix** | **6 500 € HT** (7 800 € TTC), deux trajets compris, soit ≈ 810 € par JP | **4 800 € HT** (5 760 € TTC), soit 800 € par JP |
| **Plancher interne** | 6 000 € HT (8 × 750 €). Exception : si GianLuca a déjà vu le taux de 750 € [IN], on peut accepter 6 000 € en expliquant le passage au forfait (`travaux/strategie-retenue.md:231, 401`) | 4 500 € HT (6 × 750 €) [ES, dérivé ici] |
| **Justification** | *Coût* : 8 × 591 à 737 € ≈ 4 700 à 5 900 € [ES]. *Marché* : ≈ 810 € par JP, dans le haut de la fourchette d'un chef de projet senior en région (570 à 760 € [ES]) et sous les repères de direction à temps partagé (800 à 1 200 € [DR]) (`travaux/strategie-retenue.md:232, 368`). Le « Diag Data IA » ne sert pas de justification (`travaux/strategie-retenue.md:107`). *Valeur* : GianLuca évite d'engager 90 000 € HT à l'aveugle (`interne/offre-marwin-tech-remuneration-et-collaboration.md:16`) et garde l'inventaire, la carte des rôles et les priorités, même s'il s'arrête là | *Coût* : 6 × 591 à 737 € ≈ 3 550 à 4 400 € [ES] |
| **Coûts directs** | Déplacements [IN] : le lieu de résidence des associés est inconnu. Outils négligeables | Idem |
| **Marge** [ES] | À 8 JP : 9 à 27 % (coût à 12 JP) ; −9 à +13 % (coût à 10 JP) (`travaux/calculs/arbitre-calc/verif.py` § 8). À 8,5 JP : 4 à 23 % ; −16 à +7 % [ES, calculé ici]. **Faible par choix : c'est un test du besoin, vendu une seule fois** | 8 à 26 % ; −11 à +11 % (`travaux/calculs/arbitre-calc/verif.py` § 8) |
| **Réception** | Remise du dossier, puis restitution. Réception expresse demandée sur les livrables 1, 2 et 4. Réserves motivées sous 10 jours ouvrés, corrigées une fois. Sans réserve motivée, le solde devient exigible au plus tard 30 jours après la remise : livraison pour la facturation, jamais approbation d'une suite ni d'une dépense | Idem, sur les livrables 1 et 2 |
| **Paiement** | 50 % à la commande (le travail démarre à l'encaissement) ; 50 % à la réception, sous 8 jours. Exposition maximale ≤ 3 250 € HT (`travaux/strategie-retenue.md:440`) | 50 % / 50 % ; exposition ≤ 2 400 € HT |
| **Conditions de poursuite** | Cadrage payé à l'échéance ; inventaire validé par écrit ; au moins une priorité confiée avec un budget ; accès réellement fournis ; demande écrite d'une suite dans les 30 jours ; occupation de chaque associé ≤ 85 %. À défaut : arrêt propre, GianLuca garde le dossier (`travaux/strategie-retenue.md:237`) | Idem. Si GianLuca veut ensuite les livrables manquants, ils se vendent pour la différence, 1 700 € HT, jamais au prix d'un nouveau cadrage [PR, précision] |

**Aide régionale au conseil.** L'offre du 2 nov. la décrit ainsi : « 50 % jusqu'à 15 000 € sur deux ans, dépôt avant signature du devis », puis « Échéance annoncée : 31 décembre 2026, dans la limite des crédits » [DR] (`interne/offre-marwin-tech-remuneration-et-collaboration.md:175`). L'éligibilité d'un prestataire nouveau est [IN]. Ordre : dépôt, puis signature, puis acompte. On ne retarde pas le cadrage pour une aide incertaine (`travaux/strategie-retenue.md:239`).

> **Écart avec la stratégie retenue : capacité du cadrage.**
> La stratégie annonce 8 JP, mais son propre détail additionne 1 + 1,5 + 2 + 1 + 1,5 + 0,5 + 1 = **8,5 JP** (`travaux/strategie-retenue.md:229`). Ce détail vient de `travaux/strat-S1-progressif.md:170`, qui annonçait d'ailleurs « 7 à 9 JP » ; le chiffre de 8 JP vient de la répartition « Morgan 5, Mathys 3 » (`travaux/strat-S2-pilotage.md:176`).
> *Conséquence.* À 6 500 €, le prix reste au-dessus du plancher (≈ 765 € par JP à 8,5 JP). Mais l'exception à 6 000 € tomberait à ≈ 705 € par JP, sous la règle des 750 € que la stratégie déclare intangible (`travaux/strategie-retenue.md:396`).
> *Ce que ce livrable retient.* Prix inchangé. Planification interne sur 8,5 JP, mesurée (écart toléré ≤ 25 %, `travaux/strategie-retenue.md:171`). Si l'exception à 6 000 € est utilisée, on retire 0,5 JP du périmètre : la mesure de référence du pilote P1 passe dans les deux premières semaines du pilote, comme le prévoyait déjà `travaux/strat-S1-progressif.md:186`.
> *Décision* : Morgan et Mathys valident cette règle avant le rendez-vous.

### 3.3 Offre B : socle de pilotage (B0 pilote, puis B1 ou B2)

**Contenu du socle, liste fermée** [PR] (`travaux/strategie-retenue.md:255-264`) : un point hebdomadaire de 1 h 30 avec **un seul associé**, sauf décision qui demande les deux ; un compte rendu sous 24 h ouvrées ; un registre des décisions et des échéances et un tableau de bord mis à jour chaque semaine, sur un compte de l'entité ; un comité mensuel avec rapport (capacité consommée, livrables, décisions attendues, risques, indicateurs) ; deux à quatre dossiers de décision par mois au plus ; la coordination sous mandat des prestataires du client, sans commandement direct de leurs salariés ; un suivi budgétaire préparatoire remis à l'expert-comptable du client ; la veille des échéances réglementaires listées au cadrage ; sauvegardes, restauration testée, journal et réversibilité des outils du socle.

**Dossier de décision du socle** [PR, précision] : une à deux pages, sur des données fournies, sans scénarios. Une étude avec budget, seuil et trois scénarios est un lot C7. Sans cette limite, le socle absorberait les études (section 4).

| Rubrique | B0 socle pilote | B1 « socle + 2 projets actifs » | B2 « socle + 4 projets actifs » |
| --- | --- | --- | --- |
| **Client** | Entité chef de file ; une fiche de mission par entité s'il y en a plusieurs | Idem ; capacité répartie par entité, pour qu'aucune ne consomme le temps payé par une autre | Idem |
| **Problème** | Savoir, avant tout engagement récurrent, si un pilotage délégué fonctionne vraiment | Garder une vision claire du portefeuille et des décisions préparées, sans gérer chaque détail [DR] (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:13`) | Idem, sur un portefeuille plus large, après preuves |
| **Résultat** | Le socle sur les trois priorités du cadrage ; adoption mesurée selon les critères du pilote P1 | Le socle sur 2 projets actifs nommés et 1 en veille | Le socle sur 4 projets actifs et 2 en veille |
| **Périmètre** | Les trois priorités sont suivies dans le registre et le tableau de bord ; seule celle qui reçoit un lot compte comme projet actif [PR, précision : sans cette règle, 3 projets actifs demanderaient 5,5 à 7,5 JP, `travaux/syn-capacite-ia.md:245-246`] | Limite d'encours : une demande nouvelle remplace un projet actif ou devient un lot | Idem ; B3 (6 projets) n'est pas ouvert la première année |
| **Exclusions** | Toute production (lots C) ; exécution administrative ; astreinte ; tout engagement de dépense (mandat à 0 €) ; données personnelles réelles sans les préalables | Production ; urgences hors plages ; exécution administrative ; dépenses hors mandat ; obligations réglementées ; recherche | Idem |
| **Dépendances** | Cadrage reçu ; délégué nommé ; réponses sous 5 jours ouvrés ; accès | Pilote réussi ; mandat écrit par entité ; accès maintenus | Trois mois de B1 aux critères ; gains mesurés sur les pilotes P1 et P3 ; disponibilités nominatives écrites ; occupation de chaque associé < 85 % pendant trois mois, sur tout son temps |
| **Capacité** [ES] | 3 à 4 JP par mois | 4,5 à 5,5 JP par mois selon la stratégie ; jusqu'à 6 JP par sa propre formule (encadré ci-dessous) | 6,5 à 9 JP par mois |
| **Durée** | 8 semaines, sans reconduction tacite | 3 mois, renouvelables par accord écrit ; préavis réciproque d'un mois la première année, de deux mois ensuite | Idem |
| **Prix** [PR] | **3 500 € HT par mois** (4 200 € TTC) | **4 500 € HT par mois** (5 400 € TTC) ; + **1 200 € HT** par projet actif en plus | **6 900 € HT par mois** (8 280 € TTC) |
| **Plancher interne** | 3 000 € (4 × 750 €) | 4 125 € (5,5 × 750 €) ; 4 500 € si le socle demande 6 JP, donc aucune remise possible ; 1 125 € par projet en plus [ES, dérivé ici] | 6 750 € (9 × 750 €) [ES, dérivé ici] |
| **Justification** | Coût 3,5 JP × 591 à 737 € ≈ 2 070 à 2 580 € ; le temps partagé se vend en général 2 à 8 jours par mois [HY] | 818 à 1 000 € par JP de référence (750 € si le socle demande 6 JP). Le prix rémunère un périmètre et une responsabilité (binôme de secours, journal, restauration, réversibilité), pas des heures | 767 à 1 062 € par JP. **Au-delà de 6 à 8 JP stables, un coordinateur salarié coûte moins cher au client** (5 380 à 6 149 € de coût employeur [MM], `travaux/strategie-retenue.md:108` ; `travaux/ver-R6-marche.md:25`). B2 n'est proposé qu'avec cette comparaison et l'offre C6 en alternative |
| **Coûts directs** | Deux sièges d'IA professionnels et un espace de registre : ≈ 60 à 90 $ par mois [ES] ; déplacements [IN] | ≈ 60 à 150 € par mois ; outils du client à sa charge | Idem |
| **Marge** [ES] | 16 à 49 % (12 JP) ; −1 à +39 % (10 JP) | 10 à 41 % (12 JP) ; −8 à +29 % (10 JP) à 5,5 JP ; à 6 JP : 2 à 41 % ; −18 à +29 % [ES, calculé ici] | 4 à 44 % (12 JP) ; −15 à +33 % (10 JP) |
| **Réception** | Critères du pilote P1 : 100 % des décisions avec responsable, date et source ; compte rendu sous 24 h ouvrées dans ≥ 90 % des cas ; ≥ 80 % des comptes rendus commentés sous 3 jours ouvrés ; registre consulté chaque semaine | Rapport mensuel au 5e jour ouvré ; engagements de service (comptes rendus, registre, tableau de bord) ; **malus de 5 %** en avoir sur la facture suivante si deux engagements sont manqués dans le mois | Idem ; décisions préparées à temps ≥ 85 % |
| **Paiement** | D'avance ; premier mois à la signature ; travail démarré à l'encaissement | D'avance : facture le 25 du mois précédent, échéance le 1er. Exposition ≤ 15 jours de socle (≈ 2 250 € HT) | Idem |
| **Conditions de poursuite** | Critères tenus 4 semaines de suite ; aucune erreur critique ; paiements à l'heure ; demande écrite de poursuivre. **Abandon** : relecture et corrections > 50 % du temps de référence pendant 4 semaines, ou registre non consulté après 4 semaines | Bilan au 3e mois (maintien, passage à B2, réduction) ; **sortie à blanc** complète au 6e mois du socle ; changement de palier sans pénalité si un associé est indisponible plus de 10 jours ouvrés | Idem |

Sources du tableau, sauf mention : `travaux/strategie-retenue.md:266-281` ; marges : `travaux/calculs/arbitre-calc/verif.py` § 8.

**Règles propres au socle** [PR] (`travaux/strategie-retenue.md:283, 464`) : la capacité non consommée se reporte d'au plus 20 %, pour du pilotage seulement, et ne se convertit jamais en production ; pas de reconduction tacite ; le paiement en fin de mois (sous 7 jours) n'est concédé qu'après trois échéances payées à l'heure, avec suspension automatique 8 jours après l'échéance.

> **Écart avec la stratégie retenue : capacité de B1.**
> La stratégie calcule B1 comme « socle 2,5 à 3 JP + 1 à 1,5 JP par projet actif » (`travaux/strategie-retenue.md:273`). Avec deux projets, cela donne **4,5 à 6 JP**, et non 4,5 à 5,5. B2 utilise bien la fourchette complète (2,5 + 4 × 1 = 6,5 ; 3 + 4 × 1,5 = 9). La source de la formule est `travaux/syn-capacite-ia.md:245-246`, qui donne même 2 à 3 JP pour le socle ; la stratégie retient 2,5 à 3. La borne haute (6 JP) est la même dans les deux cas.
> *Conséquence.* À 6 JP, B1 vaut exactement 750 € par JP : le prix est au plancher, et la marge peut descendre à −18 % au coût de la première année.
> *Ce que ce livrable retient.* Prix inchangé (4 500 €). La fiche de mission fixe une capacité de référence de 5,5 JP. Si le relevé montre plus de 5,5 JP consommées sur le socle deux mois de suite, le bilan trimestriel choisit entre réduire le périmètre (moins de dossiers de décision, un projet en veille de moins) et relever le prix au renouvellement à au moins 750 € × JP mesurées. Aucun travail gratuit entre-temps.
> *Décision* : Morgan et Mathys valident ce déclencheur ; il est rappelé dans 06-fonctionnement-a-deux.md.

### 3.4 Offre C : lots de production devisés

**Règle commune** [PR] (`travaux/strategie-retenue.md:287`) :
- Prix = JP estimées × 800 € HT + provision de risque de 10 à 15 %, au forfait. **Plancher absolu : 750 € HT par JP estimée**, aléas compris.
- Chaque lot a son bon de commande, ses critères de réception écrits **avant** le démarrage, ses exclusions et le régime des droits : cession des développements propres au client au paiement complet ; licence gratuite, non exclusive et perpétuelle sur les composants génériques de Marwin (`travaux/syn-droit.md:486-514`).
- Un dépassement non causé par le client reste à la charge de Marwin dans la limite de la provision ; au-delà, un avenant signé **avant** le travail.
- Paiement : 40 % à la commande, 60 % à la livraison, sous 8 jours ; au-delà de 8 JP, 40 / 30 / 30 avec un jalon intermédiaire écrit. Exposition ≤ 60 % d'un lot.
- **Réception en deux temps** : la livraison déclenche le solde ; l'adoption décide de la suite et ne conditionne pas le paiement.
- Défauts de Marwin corrigés gratuitement pendant 60 jours après la réception (`travaux/strategie-retenue.md:384`).
- **Marge type** [ES, calculé ici] : à 880-920 € par JP (formule), 16 à 36 % au coût à 12 JP, −1 à +23 % au coût à 10 JP. Au plancher de 750 € : 2 à 21 %, et −18 à +5 %.
- Ordre recommandé dans la voie (b) : C1 ou C4 d'abord (concrets, peu risqués, sans données de prospects) ; C5 seulement si Quali Contact est engagé (`travaux/strategie-retenue.md:300`).
- Les durées des lots C1, C3, C4, C5, C7 et C8 ne sont pas fixées par la stratégie : celles indiquées ci-dessous sont des repères [HY].

#### C1 : catalogue privé des œuvres (20 à 30 œuvres réelles)

| Rubrique | Contenu |
| --- | --- |
| **Client** | L'entité qui détient les œuvres (structure vendeuse, future galerie). Si c'est la collection privée de GianLuca et qu'il signe à titre personnel, les règles applicables à un client non professionnel sont à vérifier [HY] (`travaux/syn-portefeuille.md:302`) |
| **Problème** | Aucune œuvre, aucun artiste, aucun prix ne sont documentés [IN] (`travaux/syn-portefeuille.md:433`). Sans inventaire, ni vente, ni pilote commercial, ni assurance ne se préparent. Proposé dès le 18 oct. : « Catalogue privé de vos œuvres d'art » [PR] (`sources/propositions-de-collaboration.pdf` p. 1) |
| **Résultat** | 20 à 30 fiches d'œuvres réelles : photo, provenance, emplacement, disponibilité, mouvements ; export ouvert ; base sur un compte de l'entité |
| **Périmètre** | Modèle de fiche validé par écrit avant la saisie ; un cycle de corrections |
| **Exclusions** | Expertise, authentification, photographie professionnelle (commandée et payée par le client), valorisation fiscale ; garde ou transport d'œuvres |
| **Dépendances** | Œuvres réelles accessibles ; photos ; provenance ; autorisations de reproduction des artistes (CPI L131-3, `travaux/syn-portefeuille.md:420`) ; inventaire du cadrage validé |
| **Capacité** | 4 à 7 JP [ES] |
| **Durée** | 3 à 5 semaines après l'acompte et les pièces [HY] |
| **Prix** | 3 500 à 6 400 € HT (4 200 à 7 680 € TTC) selon le nombre d'œuvres et l'état des pièces ; plancher 3 000 à 5 250 € |
| **Coûts** | Négligeables ; déplacements [IN] |
| **Marge** | Marge type des lots |
| **Réception** | *Livraison* : N fiches complètes (chaque champ rempli, ou marqué « inconnu » avec sa raison) et export remis (`travaux/syn-portefeuille.md:443`). *Adoption* : le catalogue sert à présenter des œuvres |
| **Paiement** | 40 % / 60 % |
| **Conditions de poursuite** | Un second lot d'œuvres se vend au prix unitaire du premier [PR, précision ; règle 1 de la section 7]. Si 5 à 10 œuvres sont disponibles à la vente, avec prix et artiste vivant, un préalable de C2 est rempli (`travaux/strategie-retenue.md:311`) |

#### C2 : pilote commercial sur 20 comptes

| Rubrique | Contenu |
| --- | --- |
| **Client** | La structure qui vend les œuvres, nommée dans chaque message ; elle est aussi responsable du traitement. Son existence est [IN] : son nom reste « à compléter » dans les mails du CRM (`travaux/syn-portefeuille.md:264`) |
| **Problème** | GianLuca veut vendre des œuvres aux entreprises de la Nièvre [DR] (`sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:13`). Le fichier existe mais n'est ni fiable (283 numéros sur 471 « à confirmer »), ni conforme [FV] (`travaux/syn-portefeuille.md:334`). Aucun appel, rendez-vous ni vente n'est rapporté [DR] (`travaux/syn-portefeuille.md:335`). On ignore si la cible achète |
| **Résultat** | 20 comptes qualifiés (source et date pour chaque champ) ; script et e-mail validés par le conseil de GianLuca ; outil de réimport des résultats d'appel ; rapport mesuré (joignabilité, rendez-vous, refus, oppositions, temps humain par fiche) [MM à produire] ; recommandation d'extension ou d'arrêt |
| **Périmètre** | 2 semaines de préparation ; appui pendant 4 semaines d'appels (réimport hebdomadaire, ajustement du script) ; bilan. Comptes tirés des 37 cibles et des 57 fiches de priorité haute |
| **Exclusions** | Les appels et les rendez-vous ; la vente ; toute commission ; tout encaissement ; le conseil fiscal ; tout agent vocal sortant ; tout connecteur Quali Contact sans modèle de fichier réel |
| **Dépendances (toutes requises)** | Offre 0 terminée ; responsable du traitement désigné et contrat de l'article 28 signé ; décision sur l'information des personnes (art. 34), et comptes choisis hors des fiches exposées si elle est due ; entreprises seulement, ni entrepreneurs individuels ni lignes personnelles avant l'avis de l'avocat ; structure vendeuse nommée ; 5 à 10 œuvres réellement disponibles, avec prix et artiste vivant ; avis fiscal écrit (238 bis AB valable pour les achats faits avant le 31 déc. 2028 [FV] ; pièces faites à la machine très probablement exclues [HY], `travaux/syn-droit.md:56`) ; appelant désigné, qui facture directement l'entité s'il est extérieur ; seuils de poursuite fixés avec GianLuca avant l'essai |
| **Capacité** | 6 à 7 JP : Mathys 4 (données, outil, réimport), Morgan 2 à 3 (kit, bilan) [ES] |
| **Durée** | 6 à 8 semaines |
| **Prix** | **6 000 € HT** (7 200 € TTC), ≈ 860 à 1 000 € par JP ; plancher 5 250 € (7 × 750 €) |
| **Justification** | *Coût* : 6 à 7 × 591 à 737 € ≈ 3 550 à 5 150 €. *Marché* : un téléprospecteur externalisé coûte 3 000 à 8 000 € par mois [DR] ; ici, Marwin ne fournit pas les appels. *Valeur* : une seule vente d'œuvre à une entreprise peut dépasser ce montant [HY] |
| **Coûts directs** | API de recherche : 10 à 50 € ; téléphonie à la charge du client |
| **Marge** [ES] | 14 à 41 % (12 JP) ; −3 à +29 % (10 JP) (`travaux/calculs/arbitre-calc/verif.py` § 11) |
| **Réception** | *Livraison* (déclenche le solde) : fiches sourcées et datées à au moins 90 % ; 100 % des numéros partagés signalés ; 100 % des oppositions respectées ; kit validé ; outil de réimport testé. *Mesure* (décide de la suite) : résultats d'au moins 90 % des appels réimportés. Si les appels n'ont pas commencé 15 jours ouvrés après la livraison, la mesure devient un lot optionnel. **[PR, précision]** Ce lot optionnel est devisé en déduisant les JP d'appui déjà payées dans C2 et non fournies |
| **Paiement** | 40 % / 60 % ; exposition ≤ 3 600 € HT |
| **Conditions de poursuite** | Seuils fixés d'avance (repère [HY] : joignabilité ≥ 50 % et quelques rendez-vous tenus). Atteints : extension par vagues de 50 à 100 comptes, en lot de 4 000 à 6 000 € HT. Non atteints : changer de source ou de cible, ou arrêter. Les ventes sont suivies à part : elles dépendent de GianLuca et des œuvres |

Source du tableau, sauf mention : `travaux/strategie-retenue.md:302-319`.

#### C3 : faisabilité d'un premier événement sans robot

| Rubrique | Contenu |
| --- | --- |
| **Client** | L'organisateur légal : l'entité de GianLuca ou l'exploitant du lieu (`travaux/syn-portefeuille.md:450`) |
| **Problème** | GianLuca souhaite réunir des artistes et des peintres [DR] (`sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:16`). Lieu, date, jauge et budget sont inconnus [IN]. Les obligations (demande GN 6 au moins deux mois avant, boissons, Sacem, spectacles, artistes présumés salariés) pèsent sur l'organisateur (`travaux/syn-portefeuille.md:457`) |
| **Résultat** | Dossier de faisabilité : lieu, date, jauge, organisateur désigné, autorisations avec leurs dates de dépôt, budget, devis |
| **Périmètre** | Un événement, un lieu, une date cible |
| **Exclusions** | L'organisation elle-même ; la sécurité du public ; tout robot ou format « signature » ; les contrats d'artistes ; toute démarche au nom du client sans mandat |
| **Dépendances** | Lieu et organisateur identifiés. Pas d'événement public en décembre 2026 dans un lieu non autorisé : 2 à 3 mois dans un établissement recevant du public déjà ouvert, 4 à 6 mois ou plus dans un bâtiment à aménager [ES] (`travaux/syn-droit.md:533`) |
| **Capacité** | 4 à 6 JP [ES] ; deux associés sur place comptent double |
| **Durée** | 3 à 4 semaines [HY] |
| **Prix** | 3 500 à 5 500 € HT (4 200 à 6 600 € TTC) ; plancher 3 000 à 4 500 € |
| **Coûts** | Déplacements [IN] ; aucun achat |
| **Marge** | Marge type des lots |
| **Réception** | *Livraison* : dossier complet, chaque autorisation avec son autorité et sa date limite de dépôt. *Adoption* : GianLuca décide par écrit de tenir ou d'abandonner l'événement (`travaux/syn-portefeuille.md:461`) |
| **Paiement** | 40 % / 60 % |
| **Conditions de poursuite** | Si l'événement est décidé : coordination sous mandat dans le socle, s'il est actif, ou nouveau lot. Marwin n'est jamais l'organisateur légal (`travaux/strategie-retenue.md:187, 646`) |

#### C4 : tableau des lieux et de leurs obligations

| Rubrique | Contenu |
| --- | --- |
| **Client** | L'entité chef de file ; ou, lieu par lieu, l'exploitant ou le propriétaire s'ils diffèrent [IN] (`travaux/syn-portefeuille.md:265-267`) |
| **Problème** | Aucun lieu n'a de propriétaire ni d'exploitant établi [FV négatif]. Licences, permis d'exploitation, classement ERP et autorisations sont nominatifs, au nom de l'exploitant (`travaux/syn-portefeuille.md:470-473`) |
| **Résultat** | Par lieu : propriétaire, exploitant, licences, classement ERP, calendrier des démarches ; chaque point marqué « à valider par » le professionnel compétent |
| **Périmètre** | Les lieux de l'inventaire validé au cadrage |
| **Exclusions** | Le rôle d'exploitant ; toute démarche au nom du client sans mandat ; tout avis juridique |
| **Dépendances** | Inventaire du cadrage validé ; actes, baux et licences fournis |
| **Capacité** | 3 à 5 JP [ES] |
| **Durée** | 2 à 4 semaines [HY] |
| **Prix** | 2 700 à 4 600 € HT (3 240 à 5 520 € TTC) ; plancher 2 250 à 3 750 € |
| **Coûts** | Déplacements [IN] |
| **Marge** | Marge type des lots |
| **Réception** | *Livraison* : tableau complet pour chaque lieu de l'inventaire. *Adoption* : validation écrite de GianLuca, puis des professionnels (mairie, commission de sécurité, avocat) (`travaux/syn-portefeuille.md:477`) |
| **Paiement** | 40 % / 60 % |
| **Conditions de poursuite** | C7 pour un lieu à racheter ou à aménager ; C3 pour un événement |

#### C5 : échange de fichiers avec Quali Contact

| Rubrique | Contenu |
| --- | --- |
| **Client** | L'entité qui a contracté Quali Contact (probablement la structure vendeuse [HY]) |
| **Problème** | Quali Contact est « prévu » [DR] (`sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:13`) ; contrat, logiciel et formats inconnus [IN]. Un module Hermes360 a déjà été développé sur une hypothèse non vérifiée (`travaux/syn-portefeuille.md:363-364`) |
| **Résultat** | Spécification d'échange dans les deux sens ; essai sur 10 fiches fictives ; correspondance des champs validée par écrit par Quali Contact |
| **Périmètre** | Un format d'import, un format de retour, une liste d'opposition |
| **Exclusions** | Tout développement avant de connaître le format ; toute consigne directe aux opératrices, qui passe par leur employeur (`travaux/strategie-retenue.md:584`) ; toute donnée réelle |
| **Dépendances** | Contrat entre l'entité et Quali Contact ; logiciel et modèle de fichier réel ; contrat de l'article 28 entre eux |
| **Capacité** | 3 à 4 JP [ES] |
| **Durée** | 2 à 3 semaines après réception du modèle de fichier [HY] |
| **Prix** | 2 700 à 3 700 € HT (3 240 à 4 440 € TTC) ; plancher 2 250 à 3 000 € |
| **Coûts** | Aucun ; Quali Contact facture directement l'entité |
| **Marge** | Marge type des lots |
| **Réception** | *Livraison* : fichier d'essai importé chez Quali Contact ; résultats réimportés sans perte sur 10 fiches fictives ; liste d'opposition appliquée (`travaux/syn-portefeuille.md:371`). *Adoption* : première campagne réelle au format convenu |
| **Paiement** | 40 % / 60 % |
| **Conditions de poursuite** | La maintenance du format ne se facture que dans une exploitation D |

#### C6 : outillage et passation, avec aide au recrutement

| Rubrique | Contenu |
| --- | --- |
| **Client** | L'entité de GianLuca qui emploiera la personne, ou qui désigne un salarié existant |
| **Problème** | « Ne pas gérer chaque détail » [DR] (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:13`), sans payer l'exécution administrative au prix du conseil. Un assistant non cadre coûte 2 249 à 2 808 € par mois à l'employeur [MM] (`travaux/ver-R6-marche.md:25`), soit ≈ 125 à 157 € par jour travaillé [ES] |
| **Résultat** | Registre des décisions et des échéances ; tableau de bord ; modèles d'ordre du jour et de compte rendu ; 5 à 8 procédures écrites pour les tâches récurrentes repérées au cadrage, chacune avec sa fiche de secours manuel ; tous les comptes au nom de l'entité ; fiche de poste et grille d'entretien ; deux séances de formation ; un test de restauration ; exports remis |
| **Périmètre** | Processus « réunions », « échéances » et « capitalisation », avec une organisation simple ou des outils existants bien configurés seulement |
| **Exclusions** | Le recrutement lui-même (sélection, contrat de travail, paie) ; **tout outil d'IA dans le recrutement** (haut risque, `travaux/syn-droit.md:665`) ; l'exécution des tâches ; la comptabilité ; tout développement spécifique ; le nom « Jarvis » |
| **Dépendances** | Décision de recruter ou de désigner une personne ; accès ; offres d'IA professionnelles avec clauses contractuelles types et analyse d'impact des transferts si des données personnelles sont traitées |
| **Capacité** | 8 à 9 JP : Mathys 5 (outils, comptes, restauration), Morgan 3 à 4 (procédures, formation, fiche de poste) [ES] |
| **Durée** | 4 à 6 semaines, puis 30 jours d'accompagnement compris |
| **Prix** | **7 500 € HT** (9 000 € TTC), ≈ 830 à 940 € par JP ; plancher 6 750 € (9 × 750 €) ; au-delà de 8 JP, paiement 40 / 30 / 30 |
| **Justification** | *Valeur* : GianLuca paie ensuite l'exécution au coût d'un assistant (≈ 27 000 à 34 000 € par an [ES]), pas au prix d'une prestation. *Coût* : 8 à 9 × 591 à 737 € ≈ 4 700 à 6 650 € |
| **Coûts directs** | Négligeables ; outils au nom et à la charge de l'entité |
| **Marge** [ES] | ≈ 12 à 37 % (12 JP) ; −6 à +24 % (10 JP) (`travaux/calculs/arbitre-calc/verif.py` § 11 : 11,6 à 37,0 % ; la stratégie arrondit à 11 %) |
| **Réception** | *Livraison* (déclenche le solde) : outils en service sur les comptes du client, procédures et fiches de secours remises, deux formations tenues, restauration réussie, exports remis. *Adoption* (décide de la suite) : la personne désignée utilise le registre quatre semaines de suite et traite au moins 80 % des comptes rendus. Si personne n'est désigné 15 jours ouvrés après la livraison, la livraison est prononcée et la mesure d'adoption devient un lot optionnel. **[PR, précision]** Ce lot ne refacture pas l'accompagnement de 30 jours déjà compris dans C6 |
| **Paiement** | 40 % / 30 % / 30 % avec un jalon intermédiaire écrit |
| **Conditions de poursuite** | Si personne n'est désigné, Marwin **ne reprend pas** l'exécution ; un socle éventuel reste limité au pilotage |

Source du tableau, sauf mention : `travaux/strategie-retenue.md:321-337`.

#### C7 : étude de rentabilité d'un rachat ou de travaux

| Rubrique | Contenu |
| --- | --- |
| **Client** | L'entité qui rachète ou qui fait les travaux |
| **Problème** | Des rachats sont évoqués (« six bâtiments », le cabaret « le M ») [DR] (`interne/contexte-projet-carlone.md:24` ; `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:15`), sans aucune donnée [IN]. L'étude était la deuxième des huit propositions du 18 oct. : budget prévisionnel, seuil, trois scénarios [PR] (`sources/propositions-de-collaboration.pdf` p. 1) |
| **Résultat** | Budget, seuil de rentabilité, trois scénarios, hypothèses écrites et sourcées. Calculs par formule vérifiable, jamais par le modèle de langage [PR, précision, sur le modèle de l'offre D : `travaux/strategie-retenue.md:343`] |
| **Périmètre** | Une opération par lot |
| **Exclusions** | Conseil fiscal ; évaluation immobilière réglementée ; la décision d'achat |
| **Dépendances** | Données du vendeur ou devis fournis |
| **Capacité** | 3 à 5 JP [ES] |
| **Durée** | 2 à 3 semaines après réception des données [HY] |
| **Prix** | 2 700 à 4 600 € HT (3 240 à 5 520 € TTC) ; plancher 2 250 à 3 750 € |
| **Coûts** | Négligeables |
| **Marge** | Marge type des lots |
| **Réception** | *Livraison* : modèle et note remis, chaque hypothèse sourcée, contrôle par l'autre associé. *Adoption* : décision écrite de GianLuca ; relecture conseillée par son expert-comptable |
| **Paiement** | 40 % / 60 % |
| **Conditions de poursuite** | Un lot par opération ; jamais dans le socle (voir « dossier de décision du socle », section 3.3) |

#### C8 : kit de campagne et supports commerciaux

| Rubrique | Contenu |
| --- | --- |
| **Client** | La structure vendeuse |
| **Problème** | Les supports ne sont pas validés. Trois discours incompatibles coexistent sur les lieux (`travaux/syn-portefeuille.md:422`). Le diaporama promet implicitement de « vendre vos œuvres avec le CRM » (diaporama client, copie du 4 nov., hors dépôt, `slides/proposition.html:3`) |
| **Résultat** | Script, e-mail, fiche d'offre, grille de conformité, pour l'extension après C2 |
| **Périmètre** | **[PR, précision]** C8 part du script et de l'e-mail validés dans C2 et ne les refacture pas : il les décline et ajoute la fiche d'offre et la grille |
| **Exclusions** | Toute promesse fiscale non validée ; le mot « mécénat » pour vendre une œuvre (`travaux/syn-droit.md:56`) ; l'envoi des messages ; l'achat d'espace |
| **Dépendances** | Pilote C2 concluant ; mentions fiscales validées par le conseil du client ; droits des visuels documentés |
| **Capacité** | 3 à 5 JP [ES] |
| **Durée** | 2 à 3 semaines [HY] |
| **Prix** | 2 700 à 4 600 € HT (3 240 à 5 520 € TTC) ; plancher 2 250 à 3 750 € |
| **Coûts** | Outils graphiques [IN] ; photographe à la charge du client |
| **Marge** | Marge type des lots |
| **Réception** | *Livraison* : chaque support validé par GianLuca et, pour la fiscalité, par son conseil ; mentions obligatoires présentes ; droits documentés (`travaux/syn-portefeuille.md:424`). *Adoption* : supports utilisés dans la première vague d'extension |
| **Paiement** | 40 % / 60 % |
| **Conditions de poursuite** | Mise à jour à chaque vague, en petit lot devisé |

### 3.5 Offre D : exploitation d'un processus prouvé (au plus tôt au mois 7)

| Rubrique | Contenu |
| --- | --- |
| **Client** | L'entité dont le processus est exploité (par exemple la structure vendeuse pour le CRM) |
| **Problème** | Un processus répétitif prouvé en pilote doit tourner chaque mois avec une qualité écrite, sans que GianLuca embauche pour lui et sans que Marwin le maintienne gratuitement |
| **Résultat** | Un service régulier : niveaux de qualité écrits, mode manuel testé, sauvegarde et restauration testées, journal, arrêt possible à tout moment |
| **Exemples** [PR] | Tenue et qualification du CRM (fiches à jour, résultats réimportés, oppositions appliquées, export et sauvegarde testés) ; recherche documentaire avec citations sur le corpus du client (pilote P3) ; rapprochement budgétaire mensuel calculé par formule, jamais par le modèle de langage |
| **Périmètre** | Un processus par fiche ; volume mensuel plafonné au contrat |
| **Exclusions** | Évolutions et nouveaux développements (lot C) ; toute action sortante sans approbation humaine (appel, envoi, achat) ; agent vocal ; données hors du registre des traitements |
| **Dépendances** | Un pilote réussi (critères tenus 4 semaines), puis 2 à 3 mois de critères tenus ; reprise manuelle et restauration testées ; responsable et maintenance chiffrés au contrat ; comptes au nom de l'entité |
| **Capacité** | 1 à 4 JP par mois [ES] ; maintenance ≤ 0,5 JP par mois et par processus (`travaux/strat-S2-pilotage.md:583`) |
| **Durée** | 6 mois, renouvelables par écrit ; prix figé 6 mois |
| **Prix** | Minimum de **1 000 à 1 500 € HT par mois** (1 200 à 1 800 € TTC) pour la maintenance, les sauvegardes et le journal, **plus un prix par résultat accepté** fixé après la mesure de référence. Aucun prix unitaire n'est publié avant cette mesure (`travaux/strategie-retenue.md:126`) |
| **Plancher** | Le prix unitaire n'est **jamais sous le coût manuel mesuré**. Une proposition antérieure à 12 à 18 € par fiche passait sous le coût manuel de 18 à 27 € (`travaux/juge-J2-marwin.md:94`). **[PR, précision]** Contrôle trimestriel : (minimum + variable) ÷ JP réellement consommées ≥ 750 € ; sinon révision au renouvellement |
| **Coûts directs** | API et hébergement sur les comptes du client, à sa charge ; repère pour la recherche documentaire : 40 à 130 € par mois selon l'option (`travaux/syn-capacite-ia.md:656`) |
| **Marge** | [IN] avant la mesure. Repère [ES, calculé ici] : si le minimum paie 1 JP de maintenance, sa marge va de ≈ 12 à 53 % au coût de la première année |
| **Réception** | Mensuelle : niveaux de qualité du contrat (pour le CRM : champs sourcés et datés, 100 % des oppositions appliquées, export testé) ; relevé des résultats acceptés |
| **Paiement** | Minimum d'avance, le 1er ; variable en fin de mois sur relevé, sous 15 jours. Exposition ≤ 1 mois de variable |
| **Conditions de poursuite** | Critères tenus ; aucun incident critique (sinon arrêt et retour au manuel) ; coût par résultat accepté connu ; maintenance dans la limite. Partage d'un tiers du gain au renouvellement, après la première année (section 7) |
| **Réversibilité** | Comptes au nom du client. Si Marwin hébergeait elle-même le service, les règles de changement de fournisseur du Data Act s'appliqueraient : préavis de 2 mois au plus, transition de 30 jours au plus, aucuns frais de changement à partir du 12 janv. 2027 [FV] (`travaux/syn-droit.md:507-510`) |

Source du tableau, sauf mention : `travaux/strategie-retenue.md:341-349`. Le modèle financier ne fait démarrer l'exploitation qu'au mois 7, dans le seul scénario ambitieux (`modele-financier/scenarios.md:82, 215`).

### 3.6 Offre E : avenant de capacité, urgences et astreinte

| Rubrique | Contenu |
| --- | --- |
| **Client** | L'entité signataire du bon de commande concerné |
| **Problème** | Un besoin ponctuel hors périmètre : pic de charge, demande qui ne remplace aucun projet actif, urgence |
| **Résultat** | Un travail en plus, décrit par écrit avant de commencer |
| **Périmètre** | *Avenant de capacité* : heures ouvrées, sur bon écrit du valideur **avant** le travail. *Urgences* : liste fermée (incident de données ou de sécurité ; échéance légale à moins de 48 h). *Astreinte* : aucune par défaut, jamais 24 h sur 24 ni 30 jours sur 30 ; sur demande seulement, un forfait chiffré à part, avec des relais nommés (`travaux/strategie-retenue.md:353-355` ; `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:105`) |
| **Exclusions** | **[PR, précision]** Un travail qui produit un livrable de plus de 2 JP se devise en lot C, au forfait, pas en avenant au temps |
| **Dépendances** | Capacité restante sous le plafond de 10 JP ; bon écrit préalable |
| **Capacité** | Résiduelle |
| **Durée** | Ponctuelle |
| **Prix** | **900 € HT par JP** (1 080 € TTC), demi-journée minimale (450 € HT). Arrêter un processus en incident ne demande aucune autorisation et ne se facture pas |
| **Coûts** | Négligeables |
| **Marge** [ES] | 18 à 34 % (12 JP) ; 2 à 21 % (10 JP) (`travaux/calculs/arbitre-calc/verif.py` § 8) |
| **Réception** | Travail décrit dans le bon, constaté dans le relevé mensuel |
| **Paiement** | Fin de mois, sous 15 jours |
| **Conditions de poursuite** | Deux urgences dans le même mois : avenant ou report, jamais d'absorption gratuite (`travaux/strategie-retenue.md:534`). Demandes hors périmètre au-delà de 20 % de la capacité pendant deux mois : signal de suspension (`travaux/strategie-retenue.md:679`). Avenants répétés sur un même sujet : en faire un lot ou un projet actif au renouvellement |

> **Écart avec la stratégie retenue : un prix au temps visible du client.**
> La stratégie dit que « le client ne voit aucun taux journalier » (`travaux/strategie-retenue.md:133`) et interdit tout taux journalier dans les documents client (`travaux/strategie-retenue.md:798`). Elle vend pourtant l'avenant E « 900 € HT par JP » (`travaux/strategie-retenue.md:203, 353`) et range le « taux d'avenant » parmi les éléments internes (`travaux/strategie-retenue.md:787`). Un avenant signé montre forcément son prix.
> *Ce que ce livrable retient.* Le contrat-cadre et les documents client disent : « Travaux hors périmètre : devis forfaitaire écrit avant tout travail » et « Intervention urgente de la liste fermée : par demi-journée, 450 € HT (540 € TTC) ». Le chiffre de 900 € par JP reste la base interne de calcul des devis d'avenant. C'est un prix au temps, mais limité aux urgences, et il ne sert de base à aucune autre offre.
> *Décision* : Morgan et Mathys valident cette formulation. 11-proposition-commerciale-revisee.md la reprend ; pour-gianluca/proposition-de-cadrage.md ne porte que sur le cadrage et ne mentionne pas les urgences, ce qui est cohérent.

---

## 4. Règle anti-double facturation

Les dix règles de la stratégie [PR] (`travaux/strategie-retenue.md:382-391`) :

1. **Une tâche, une ligne.** Chaque JP est imputée à un seul bon de commande, avec un code visible dans le relevé mensuel remis au client.
2. **Le socle ne produit pas, la production ne pilote pas.** Un lot ne s'exécute pas sur le temps du socle ; le socle n'absorbe pas un dépassement de lot ; la capacité du socle ne se convertit jamais en production.
3. **Un outil construit dans un lot n'est jamais refacturé.** Sa maintenance n'est facturée que si une exploitation D la prévoit. Les défauts de Marwin sont corrigés gratuitement pendant 60 jours après la réception.
4. **Le CRM déjà construit** n'est facturé ni rétroactivement ni dans un lot. Son régime (licence gratuite ou cession) est écrit avant tout lot CRM, une fois sa propriété réglée entre Morgan et Mathys. L'offre du 29 oct. le disait déjà : sa facturation passée « n'est pas ajoutée rétroactivement » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:70`).
5. **Jamais facturés** : la remise en ordre, la mise en conformité des données, la correction de nos erreurs, nos outils internes, notre administration, notre prospection.
6. **Outils et achats** : au nom du client et payés par lui, sans marge. Les débours ne sont refacturés que s'ils remplissent les quatre conditions du BOFiP (BOI-TVA-BASE-10-10-30, § 200) [FV] (`travaux/syn-droit.md:431`).
7. **Tiers** : Quali Contact, l'expert-comptable, l'avocat, le photographe et les artistes facturent directement l'entité de GianLuca.
8. **Deux associés en réunion** : deux JP seulement si le bon de commande le prévoit.
9. **Malus et refus** : un avoir sur la même commande, jamais du travail gratuit sur une autre.
10. **Aucun dépassement sans avenant signé avant le travail.** C'est la traduction de la promesse déjà affichée « Aucun travail facturé deux fois » [FV] (diaporama client, copie du 4 nov., hors dépôt, `slides/garanties.html:38`).

**Chevauchements repérés dans ce catalogue et règle appliquée** :

| Chevauchement | Risque | Règle |
| --- | --- | --- |
| Dossiers de décision du socle / étude C7 | Le socle absorbe une étude, ou une étude est payée deux fois | Dossier du socle : une à deux pages, sans scénarios ; au-delà, lot C7 (section 3.3) |
| Script et e-mail de C2 / kit C8 | Le kit est payé deux fois | C8 décline le kit de C2 sans le refacturer |
| Appui aux appels compris dans C2 / lot optionnel de mesure | Appui payé sans être fourni, puis refacturé | Lot optionnel devisé net des JP d'appui déjà payées |
| Accompagnement de 30 jours compris dans C6 / lot optionnel d'adoption | Idem | Lot optionnel sans l'accompagnement déjà payé |
| Cadrage réduit / livrables manquants | Un second cadrage complet | Livrables manquants vendus pour la différence (1 700 € HT) |
| Démonstrateurs internes des pilotes P1 et P3 / exploitation D | Faire payer au client la mise au point de nos outils | Démonstrateurs jamais facturés (règle 5) ; seule l'exploitation d'un processus prouvé se facture |
| Remise en conformité du CRM / lot C2 | Conformité payée dans le lot | Conformité dans l'offre 0, non facturée |
| Socle partagé entre plusieurs entités | Une entité consomme le temps payé par une autre | Capacité répartie par entité dans la fiche de mission (`travaux/strategie-retenue.md:268`) |
| Avenant E / lot C | Un livrable vendu au temps | Au-delà de 2 JP de livrable, lot au forfait (section 3.6) |

---

## 5. Sort du taux de 750 € HT

**Où il apparaît** [FV] : « Taux de référence : 750 € HT la journée-personne. On ajuste le périmètre et le nombre de jours, pas le taux » (`interne/offre-marwin-tech-remuneration-et-collaboration.md:18`) ; « Taux unique : 750 € HT la journée-personne » (diaporama client, copie du 4 nov., hors dépôt, `slides/formules.html:30`) ; « Hypothèse interne : vingt journées-personnes × 750 € HT = 15 000 € HT par mois. Ce calcul constitue une base de négociation, à confirmer selon les compétences mobilisées, les coûts, le budget du client et le mandat réel » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:64`) ; « Le repère de chiffrage est de 750 € HT par journée-personne » (`interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 3). Son origine n'est pas documentée [IN] ; l'idée d'un calcul à rebours reste une hypothèse non prouvée [HY] (`travaux/syn-portefeuille.md:633`).

**Ce qu'il vaut** [ES] :

| Repère | Valeur | Place du taux de 750 € |
| --- | --- | --- |
| Coût complet, central à pleine capacité (12 JP) | 591 à 737 € | Le couvre |
| **Coût complet, plafond de la première année (10 JP)** | **710 à 885 €** | **Ne couvre que le bas de la fourchette** |
| Coût complet, prudent (7 JP) | 744 à 962 € | Ne le couvre pas |
| Chef de projet senior en région | ≈ 570 à 760 € [ES] | Dans le haut de la fourchette |
| Moyenne « gestion de projets » des indépendants tech | 698 € [FV, étude privée] | Au-dessus |
| Direction financière à temps partagé | 800 à 1 200 € [DR] | En dessous |

Sources : `travaux/strategie-retenue.md:361-368`.

**Décision retenue** [PR] (`travaux/strategie-retenue.md:395-401`) :
- **Il disparaît du discours client.** On retire la mention du diaporama (`slides/formules.html:30`) et la phrase de `interne/offre-marwin-tech-remuneration-et-collaboration.md:18`. Le client voit des forfaits et des périmètres (sous réserve de l'encadré de la section 3.6).
- **Il devient le plancher interne**, jamais remisé, ni contre un volume ni contre une promesse d'investissement (« N'échangez jamais une baisse d'honoraires contre une promesse d'investissement », `interne/offre-marwin-tech-remuneration-et-collaboration.md:149`). En dessous, on réduit le périmètre ou on refuse.
- **Le prix cible est de 800 à 950 € par JP estimée**, aléas compris, parce qu'à 10 JP facturées le coût complet est de 710 à 885 €.
- **Il ne s'applique pas à l'exécution** : l'administratif vaut 125 à 157 € par jour chez un assistant salarié ; il est exclu ou transmis (C6). Le développement (405 à 585 € par jour en région [ES]) est vendu au livrable.
- **Il est révisé au mois 6** sur le coût complet mesuré.
- **Exception** : si GianLuca a déjà vu ce taux [IN], on l'applique au seul cadrage (6 000 € HT) et on explique le passage au forfait (voir l'encadré de la section 3.2).

---

## 6. Sort des formules, de l'acompte de 7 500 € et des options

| Élément des archives | Source [FV] | Décision [PR] | Raison | Retour possible |
| --- | --- | --- | --- | --- |
| Formule de base : 15 000 € HT par mois, 20 JP, « environ un mi-temps » | `interne/offre-marwin-tech-remuneration-et-collaboration.md:13-15` ; diaporama, `slides/formules.html:9` | **Retirée** comme offre d'entrée | 78 à 83 % du temps disponible des deux associés, pas un mi-temps [ES] (`travaux/syn-capacite-ia.md:228`) ; aucune demande directe du client [FV négatif] | Jamais comme abonnement. Un chiffre d'affaires de cet ordre ne revient que comme somme d'un socle, de lots et d'une exploitation, après un pilote réussi, avec une sous-traitance financée |
| Renforcement : 30 000 € HT par mois, 40 JP | `interne/offre-marwin-tech-remuneration-et-collaboration.md:13-15` ; diaporama, `slides/formules.html:20` | **Retiré** de toute présentation | 140 à 145 % du temps disponible [ES] (`travaux/syn-capacite-ia.md:229`) | Seulement avec un recrutement financé par un contrat renouvelé |
| « Ancre » : renforcement plus laboratoire, ≈ 46 JP par mois [ES : 40 JP plus 18 JP de R&D sur trois mois] | `interne/offre-marwin-tech-remuneration-et-collaboration.md:65, 246` | **Retirée** | Au-delà du plafond théorique de 35 JP bruts | Non |
| Plancher de négociation : ≈ 10 300 € HT pour ≈ 14 JP | `interne/offre-marwin-tech-remuneration-et-collaboration.md:248` | **Retiré** | Remplacé par les planchers par offre (section 2) | Non |
| Acompte de 7 500 € HT, six mois d'engagement | `interne/offre-marwin-tech-remuneration-et-collaboration.md:19, 193` ; diaporama, `slides/paiement.html:9-10` | **Retirés** | Ils accompagnaient la formule de six mois | Remplacés par l'acompte du cadrage (3 250 € HT), celui des lots (40 %) et le premier mois du socle payé à la signature. Le principe demeure : un acompte n'est ni du capital ni un prêt (`interne/offre-marwin-tech-remuneration-et-collaboration.md:142`) |
| Mois 2 à 6 payés d'avance, contre « sous sept jours après facture de fin de mois » | `interne/offre-marwin-tech-remuneration-et-collaboration.md:19` ; `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:57` | **Contradiction tranchée** | Le paiement suit la nature de la prestation | Fin de mois seulement pour la consommation variable, ou pour le socle après trois échéances payées à l'heure |
| Premier mois de 20 JP réparti 6 / 7 / 4 / 3 | `interne/offre-marwin-tech-remuneration-et-collaboration.md:54-61` | **Retiré** | Il supposait la formule de base | Remplacé par le cadrage (8 JP) |
| Démonstrateur Jarvis de 4 JP « inclus » | `interne/offre-marwin-tech-remuneration-et-collaboration.md:60, 65` | **Retiré** de l'offre | Propriété du code et du nom non réglée (`travaux/strategie-retenue.md:648`) | Démonstrateur interne P3, non facturé ; produit seulement après règlement des droits et gain mesuré |
| Option laboratoire : 30 000 € HT dont 13 500 € d'honoraires | `interne/offre-marwin-tech-remuneration-et-collaboration.md:21` ; diaporama, `slides/laboratoire.html:9-10` | **Retirée** | Son « geste robotique » devait être le premier trait de STRATES (`interne/offre-marwin-tech-remuneration-et-collaboration.md:84`) : plus d'objet ; aucun financement | Usage démontré, financeur écrit, achat par l'entité, au plus 10 % de la capacité, pas avant le mois 6 à 12 |
| Option création avec Medhi et STRATES (≈ 10 000 € HT) | `interne/offre-marwin-tech-remuneration-et-collaboration.md:22` | **Retirée** | Décision du 4 nov. [DR] (`travaux/note-point-4-novembre-et-activites.md:25`) | Contrat direct entre Medhi et l'entité de GianLuca, sans Marwin ; ou décision écrite des deux associés et contrat séparé |
| Investir « tout de suite » en finançant STRATES | `interne/offre-marwin-tech-remuneration-et-collaboration.md:144` | **Retiré** | Plus de ligne création ; un investissement ne se lie jamais aux honoraires | Pas de discussion avant 12 à 24 mois |
| Postes « hors forfait, sur devis séparés » | `interne/offre-marwin-tech-remuneration-et-collaboration.md:20` | **Conservé, renforcé** | Principe 5 | Payés directement par l'entité, jamais par Marwin |
| Astreinte « chiffrée séparément » | `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:59` | **Conservée**, sur demande | Non tenable à deux sans relais | Forfait séparé (offre E) |
| Livrable « réputé accepté » sans réponse | `interne/offre-marwin-tech-remuneration-et-collaboration.md:206` | **Retiré** | Contredit « une absence de réponse ne vaut pas approbation » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:103`) | Remplacé par le principe 10 |
| CRM « offert à ce jour » | `interne/offre-marwin-tech-remuneration-et-collaboration.md:227` | **Jamais facturé** | Règle 4 de la section 4 | Régime écrit avant tout lot CRM |

**Ce que le découpage change en montant** [ES] : l'offre des archives demandait 90 000 € HT sur six mois. Le scénario central du modèle financier facture ≈ 41 400 € HT sur les six premiers mois et ≈ 89 400 € HT sur douze (`modele-financier/scenarios.md:131-136, 41`). L'ambition n'est pas divisée. Elle est étalée et soumise à une réception à chaque palier. Le « contrat certain » reste de 0 € (`modele-financier/scenarios.md:46`).

---

## 7. Rémunérer l'organisation, la responsabilité et la valeur quand l'automatisation réduit le temps

**Le problème.** L'offre du 29 oct. prévoyait que « les économies issues de l'automatisation permettent de réaffecter la capacité ou de revoir le forfait » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:66`). La règle a disparu le 2 nov., alors que la facturation restait au temps (`travaux/syn-sources.md:266`). Au temps, chaque gain réduit le chiffre d'affaires. Et la première année, la capacité libérée est d'abord négative : la mise en place coûte 12 à 20 JP [ES] (`travaux/syn-capacite-ia.md:762`).

**Ce que chaque offre rémunère** [PR] :

| Ce qui est rémunéré | Offre | Comment | Si le temps baisse |
| --- | --- | --- | --- |
| **Organisation** : registre, comités, dossiers de décision, coordination | Socle B | Prix par périmètre (socle + N projets actifs) | Le prix ne baisse pas pendant la période ; le temps libéré peut absorber un projet de plus, sur proposition de Marwin |
| **Responsabilité** : binôme de secours, contrôle à quatre yeux, journal, sauvegarde et restauration testées, arrêt, réversibilité ; correction gratuite 60 jours | Socle B ; provision de 10 à 15 % des lots C | Inclus dans le prix, pas compté en heures | Inchangé : ces garanties restent dues |
| **Production** | Lots C | Forfait par livrable | Le gain sur le forfait revient à Marwin |
| **Résultat répété** | Exploitation D | Minimum + prix par résultat accepté, figé 6 mois | Le gain revient à Marwin pendant la période |
| **Valeur économique réelle** | Option à 12 mois | Prime de 20 à 30 % de l'économie de la première année, mesurée [MM] et validée par écrit, plafonnée | Seulement si une dépense que GianLuca payait vraiment disparaît |

**Règles** [PR] (`travaux/strategie-retenue.md:418-423`) :
1. Prix au livrable, au périmètre ou au résultat accepté, fixé pour la période à partir d'une **référence mesurée avant** l'automatisation. Le gain obtenu pendant la période revient à Marwin.
2. Le socle paie une responsabilité, pas des heures. Il ne baisse pas pendant le contrat si le temps baisse.
3. **Partage au renouvellement** : la première année, les gains restent à Marwin ; ensuite, un tiers du gain mesuré revient au client, en baisse du prix unitaire ou en volume en plus, avec le calcul joint au rapport (`travaux/strat-S2-pilotage.md:253-256`).
4. Prime sur économie réelle : option à 12 mois, plafonnée (`travaux/strat-S2-pilotage.md:306` ; `travaux/strat-S3-contradicteur.md:315`).
5. **Aucune variable sur les ventes d'œuvres** : statut d'intermédiaire, obligations de lutte contre le blanchiment dès 10 000 €, droit de suite [HY] (`travaux/syn-droit.md:525-526`). Un bonus éventuel ne porte que sur ce que Marwin contrôle (délais, réception au premier passage), au plus 10 à 15 % du socle, pas avant la deuxième année.
6. Transparence : les gains ne sont jamais présentés comme des heures manuelles fictives. L'indicateur « équivalent temps humain évité » est publié au client (`travaux/syn-capacite-ia.md:811`).

**Illustration** [ES, chiffres fictifs pour montrer le mécanisme] : B1 à 4 500 € par mois pour une référence de 5 JP, soit 900 € par JP de référence. Si l'outillage ramène le socle à 3,5 JP, le gain vaut 1,5 JP × 900 € = 1 350 € par mois. La première année, Marwin le garde (≈ 1 290 € par JP réellement passée). Au renouvellement de la deuxième année, un tiers, soit 450 €, revient à GianLuca : socle à 4 050 €, ou même prix avec un suivi supplémentaire de valeur équivalente. Les gains réels sont [IN] : aucun n'est mesuré à ce jour (`travaux/syn-capacite-ia.md:761`).

---

## 8. Comparaison des modèles de prix, et pourquoi ce choix

| Modèle | Exemple | Ce que paie GianLuca | Effet d'un gain d'automatisation | Risques principaux | Place retenue |
| --- | --- | --- | --- | --- | --- |
| **Journées ou capacité réservée** (régie) | Formules de 15 000 et 30 000 € HT ; 750 € la JP | Du temps bloqué, utilisé ou non | Baisse le chiffre d'affaires de Marwin, ou pousse à compter des heures fictives | Client : paie des jours, pas des résultats. Marwin : capacité promise au-delà du possible (78 à 145 % du temps) ; tout finit dans l'abonnement ; volume et présence sont des indices de subordination (`travaux/strategie-retenue.md:683`) | Retirée comme offre. Ne survit que pour les avenants E, et comme mesure interne (relevé) |
| **Forfait par livrable** | A ; lots C | Un résultat défini et réceptionné | Le gain revient à Marwin pendant la période | Marwin porte le dépassement (provision de 10 à 15 %) ; exige des critères écrits avant | **Retenu** pour tout ce qui produit un livrable |
| **Accompagnement récurrent au périmètre** | B0, B1, B2 | Un périmètre (socle + N projets) et un niveau de service | Prix stable pendant la période ; partage au renouvellement | Dérive vers l'abonnement général sans liste fermée ni limite d'encours ; au-delà de 6 à 8 JP stables, un salarié coûte moins cher au client | **Retenu**, au plus tôt au mois 4, après un pilote |
| **Exploitation d'un processus** | D | Un service régulier : minimum + prix par résultat accepté | Le gain revient à Marwin pendant 6 mois, puis se partage | Prix fixé avant mesure, donc sous le coût manuel (`travaux/juge-J2-marwin.md:94`) ; maintenance sous-estimée | **Retenu** au plus tôt au mois 7, après preuve |
| **Lots complémentaires** | C attachés au socle | La production, hors du socle | Comme le forfait | Plus de bons de commande à gérer ; en échange, rien n'est absorbé | **Retenu**, avec la règle « le socle ne produit pas » |
| **Variable** | Commission sur les ventes ; prime sur économie ; bonus de délais | Une part du résultat | Aligne le prix sur la valeur, si elle se mesure | Commission sur les œuvres : statut d'intermédiaire, blanchiment, droit de suite [HY] ; dépend d'actes du client ; trésorerie incertaine | Commission **refusée** ; prime sur économie réelle **en option à 12 mois** ; bonus de délais pas avant la deuxième année |

**Pourquoi ce choix.**
1. **Le besoin n'est pas prouvé.** Aucune parole directe de GianLuca [FV négatif] (`travaux/syn-sources.md:38`). Un forfait court et payé sert de test ; un abonnement suppose le besoin acquis.
2. **Aucune entité ne paie encore.** Aucun contrat, aucune facture [FV négatif] (`travaux/syn-sources.md:39`). Des engagements courts, payés selon leur nature, limitent l'exposition à ≈ 5 500 à 6 000 € HT de travail non payé à un instant donné [ES] (`travaux/strategie-retenue.md:447`).
3. **La capacité est rare.** Le binôme tient au plus 10 JP facturables par mois la première année. Un prix au périmètre avec limite d'encours protège ce plafond ; un volume de jours vendu l'expose.
4. **L'automatisation doit profiter aux deux.** Au temps, elle appauvrit Marwin. Au livrable et au périmètre, elle l'enrichit d'abord, puis se partage.
5. **La réception doit être possible.** Un livrable se réceptionne ; « vingt journées de pilotage » ne se réceptionnent pas.
6. **La requalification et la dépendance** sont plus faibles quand Marwin vend des livrables avec ses propres méthodes que quand elle vend du temps de présence (`travaux/strategie-retenue.md:777`).

**Ce que ce choix coûte** [ES] : moins de chiffre d'affaires garanti au départ (≈ 41 400 € HT sur six mois en central, contre 90 000 € promis par les archives) ; plus de bons de commande, de devis et de réceptions à gérer ; une dépendance à la qualité des estimations. Le seuil de rentabilité reste bas (≈ 2,5 JP vendues par mois pour couvrir frais et réserve), mais payer 2 500 € nets par ETP demande 8,8 à 9,5 JP vendues, au bord du plafond (`modele-financier/scenarios.md:24, 196`).

---

## 9. Recommandations : preuve, hypothèse, limite, décision

| Recommandation | Preuve | Hypothèse | Limite | Décision correspondante |
| --- | --- | --- | --- | --- |
| Vendre par bons de commande séparés, sans abonnement général | Abonnement de six mois couvrant tout (`travaux/syn-sources.md:240`) ; formule de base à 78-83 % du temps [ES] (`travaux/syn-capacite-ia.md:228`) | GianLuca accepte plusieurs bons de commande | Plus de gestion ; dépend de l'organisation de ses entités [IN] | Décision n° 2 de 01-synthese-direction.md |
| Le cadrage A est la seule première vente | Aucune entité, aucun contrat [FV négatif] ; coût 4 700 à 5 900 € [ES] | GianLuca paie un test | Aucune référence démontrable ; s'il a vu 750 €, 6 000 € | Décision n° 2 ; encadré 3.2 |
| 750 € = plancher interne ; prix cible 800 à 950 € | Coût 710 à 885 € par JP à 10 JP [ES] (`travaux/calculs/arbitre-calc/verif.py` § 1) | Coefficient 1,7 à 1,9 ; frais 1 500 à 2 500 € [HY] | Aucune simulation officielle ; repères de marché secondaires | Décision n° 5 (garde-fous) ; révision au mois 6 |
| Socle au périmètre, liste fermée, limite d'encours | Socle 2 à 3 JP + 1 à 1,5 JP par projet actif [ES] (`travaux/syn-capacite-ia.md:245-246`) ; salarié moins cher au-delà de 6 à 8 JP stables [ES] | Délégué nommé ; décisions sous 5 jours ouvrés | Disponibilités des associés [IN] | Décision écrite de GianLuca après le pilote ; encadré 3.3 |
| Lots au forfait, réception en deux temps | Erreur corrigée : paiement suspendu à des actes du client (`travaux/strategie-retenue.md:113`) | Les estimations tiennent à ± 25 % | Un dépassement de 50 % coûte 2 000 à 2 750 € | Contrat-cadre (12-gouvernance-contrat-sortie.md) |
| Exploitation seulement après preuve, jamais sous le coût manuel | Prix antérieur sous le coût manuel (`travaux/juge-J2-marwin.md:94`) | Un pilote réussit | Aucun gain mesuré [IN] (`travaux/syn-capacite-ia.md:761`) | Au mois 7 au plus tôt |
| Anti-double facturation par codes dans le relevé, et règles de chevauchement | Promesse affichée « Aucun travail facturé deux fois » [FV] (diaporama client, `slides/garanties.html:38`) | Le client lit le relevé | Chevauchements C2/C8 et socle/C7 à surveiller | Contrat-cadre |
| Gains d'automatisation : prix fixe sur la période, un tiers au client après un an | Règle disparue le 2 nov. (`travaux/syn-sources.md:266`) | Référence mesurée avant l'automatisation | Gains [IN] | Clause de prix du contrat-cadre |
| Aucune variable sur les ventes d'œuvres | Obligations d'intermédiaire (`travaux/syn-droit.md:525-526`) | — | Avis d'avocat non obtenu | Refus (`travaux/strategie-retenue.md:703`) |
| Retirer formules, acompte de 7 500 €, ancre et options | Laboratoire sans objet (`interne/offre-marwin-tech-remuneration-et-collaboration.md:84`) ; décision du 4 nov. [DR] | Mathys est d'accord [IN] | Ce que GianLuca a vu ou accepté [IN] | Décisions n° 2 et n° 3 de 01-synthese-direction.md |

**Décisions à prendre par Morgan et Mathys sur ce catalogue** (avant le rendez-vous) :
1. Valider la règle des planchers (750 € × borne haute des JP estimées) et le tableau de la section 2.
2. Valider la règle de l'encadré 3.2 (cadrage planifié sur 8,5 JP ; périmètre réduit si l'exception à 6 000 € est utilisée).
3. Valider le déclencheur de l'encadré 3.3 (B1 au-delà de 5,5 JP deux mois de suite).
4. Valider la présentation de l'avenant E (encadré 3.6).
5. Fixer le contenu exact du cadrage réduit (livrables 3, 5, 6 et 8).

---

## 10. Inconnues qui peuvent changer ce catalogue

| Inconnue [IN] | Ce qu'elle change | Où elle se lève |
| --- | --- | --- |
| Entité ou entités de GianLuca, effectif | Nombre de bons de commande ; règle de rétractation possible si le contrat est signé hors établissement avec une entité de 5 salariés au plus [HY] (`travaux/strategie-retenue.md:466`) | Rendez-vous (13-preparation-rendez-vous.md) ; avocat |
| TVA récupérable ou non par l'entité | Coût réel pour lui : le TTC si elle ne la récupère pas | Rendez-vous |
| Éligibilité à l'aide régionale | Ordre des signatures ; coût net du cadrage pour lui | Dossier régional, avant signature |
| Ce que GianLuca a vu (taux de 750 €, formules, lettre au prénom erroné) | Exception à 6 000 € ; message de recadrage | Morgan |
| Disponibilités nominatives des associés | Scénario tenable ; plafond de 10 JP | Fiche « rôles et disponibilités » |
| JP réelles du cadrage | Toutes les estimations suivantes | Relevé du cadrage (écart toléré ≤ 25 %) |
| Œuvres disponibles, structure vendeuse, Quali Contact | Faisabilité de C1, C2, C5, C8 | Cadrage |
| Lieu de résidence des associés | Coût des déplacements de chaque offre | Morgan et Mathys |
| Prix de la RC professionnelle | Frais fixes, donc coût complet par JP | Devis d'assureur |

---

## Renvois

- Chantiers, acheteurs, priorités : 03-cartographie-projets.md.
- Valeur pour GianLuca et comparaison de ses coûts : 05-proposition-de-valeur.md.
- Capacité, seuils de saturation, occupation : 06-fonctionnement-a-deux.md.
- Pilotes P1 et P3, protocoles d'essai : 07-processus-ia-et-essais.md.
- Calendrier des offres : 08-feuille-de-route.md.
- Scénarios, trésorerie, tests de résistance : 09-modele-economique-tresorerie.md.
- Version commerciale du catalogue : 11-proposition-commerciale-revisee.md ; pour-gianluca/proposition-de-cadrage.md.
- Clauses de réception, de paiement, de droits et de sortie : 12-gouvernance-contrat-sortie.md.
- Risques et décisions : 14-registre-risques-inconnues-decisions.md.

Relu et contrôlé le 4 novembre 2026 : 32 vérifications, 15 corrections.
