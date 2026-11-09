# Mise à jour de l'audit après les faits nouveaux du 9 novembre 2026

Audit Marwin Tech × GianLuca Carlone · note de mise à jour (hors des 15 livrables) · 9 novembre 2026, revue le même jour après relecture contradictoire
Statut : interne (ne pas transmettre à GianLuca Carlone). **À lire juste après `interne/01-synthese-direction.md`** ; le README ne référence pas encore cette note (décision D55).
Sources principales : déclarations de Morgan Olsen du 9 nov. 2026, non vérifiées ; présentation « L'IA au service de vos projets — Marwin Tech » du 9 nov. 2026 (copie de travail, abrégée PIA) ; `README.md` ; `annexes/travaux/BRIEF-AGENTS.md` ; `annexes/travaux/strategie-retenue.md` ; `annexes/travaux/rj-R5-art-lieux.md` ; `annexes/travaux/syn-droit.md` ; livrables `interne/01` à `interne/15` ; projets de `pour-gianluca/`, dont `pour-gianluca/2026-11-09-proposition-de-cadrage.md`, relu pour cette version ; textes officiels consultés le 9 nov. 2026 (Légifrance : code du travail, art. L8221-6 et L7122-22 ; service-public : fiches F22365 et F3094).
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ; [MM] mesuré ; [IN] inconnu. « [PR, cette note] » signale une proposition nouvelle. JP : journée-personne de 7 h.

Conventions. Chemins relatifs au dossier de l'audit. Les pièces d'origine du dépôt gardent leur chemin depuis la racine du dépôt (`README.md`, section 6) et sont citées à travers le livrable qui les cite (« via »). **PIA** = copie de travail de la présentation du 9 nov. (`PIA/deck.json`, `PIA/slides/<id>.html`), hors dépôt et hors dossier de l'audit, lue sans modification ; dans les tableaux, `idee:21` se lit `PIA/slides/idee.html:21`. Les « notes de l'orateur » sont le contenu des balises `<aside>`. « L'administratrice » : Morgan a dit « une administrative centrale » ; le genre reste à confirmer. Les numéros de ligne de cette note cités par `pour-gianluca/2026-11-09-proposition-de-cadrage.md` (« 78-82 », « ligne 292 ») renvoient à sa version d'avant relecture : l'encadré C6 est à la fin de la section 2, D51 en section 10.

Codes repris d'autres fichiers. Registre (`interne/14-registre-risques-inconnues-decisions.md`) : **D03** décider de notifier ou non la CNIL, et comment (ligne 271 ; échéance du 5 nov. passée, état [IN]) ; **D05** arrêter toute production non commandée (273) ; **D08** informer les personnes concernées (art. 34) et GianLuca, par un texte validé par le conseil (276 ; au plus tard le 19 nov.) ; **D11** accord écrit de Mathys sur la stratégie (279) ; **D12** régime du CRM et de Jarvis entre associés (280) ; **D13** garde-fous : 15 déc., 31 janv., 10 JP, 85 % (281) ; **D14** envoi du message de recadrage et de la proposition (282) ; **D24** GianLuca désigne l'entité, le signataire, le valideur et le délégué (297) ; **U07** accord de Mathys (179) ; **U46** points juridiques non tranchés : rôles RGPD, notification, rétractation, rôle au sens du règlement sur l'IA (201). Contre-analyse (`interne/15-contre-analyse.md`) : **R1** le pilotage global n'est pas le besoin prioritaire (81) ; **R10** promesse trop large pour être réceptionnée (90), distinct du R10 du registre ; **4a** GianLuca recrute et **4b** un associé devient salarié (303-304).

---

## En bref

1. **Le verdict, le prix du cadrage (6 500 € HT), les dates de report et le plafond de 10 JP ne changent pas** [PR] (`annexes/travaux/strategie-retenue.md:41-44`). Le contenu du cadrage, lui, doit être fixé par écrit : section 8.
2. **Tout gérer avec l'IA : non, ni aujourd'hui ni dans un an** [PR, cette note]. Décider, signer et payer restent humains (`interne/07-processus-ia-et-essais.md`, section 2.1). Cible : 1,5 à 2 fois plus de travail utile sur deux à quatre processus outillés, à un an, à fixer avec GianLuca après la mesure de départ [HY] (`annexes/travaux/strategie-retenue.md:163`).
3. **Rien ne part au client, présentation comprise, avant D03, D08 et l'accord écrit des deux associés** [PR] (`interne/01-synthese-direction.md:68`).
4. **Le portefeuille déclaré grossit [DR], la capacité de Marwin non** : la règle « une voie, deux projets actifs » devient plus nécessaire [HY] (`interne/06-fonctionnement-a-deux.md:21`).
5. **L'administratrice renforce la voie « outillage et passation »**, mais rend plausible que GianLuca juge Marwin inutile pour le quotidien [HY].
6. **Les 1,5 M€ de bâtiments, déclarés par Morgan [DR], ne font ni un budget pour Marwin, ni une entité qui signe** [PR] (`annexes/travaux/strategie-retenue.md:566`).
7. **La présentation du 9 nov. ne doit pas partir en l'état, ni après une correction rapide** [PR, cette note]. Elle promet trop, y compris dans les notes de l'orateur, visibles par toute personne qui a le lien. Elle présente comme un atout le CRM, exposé au 4 nov. [DR] (`README.md:91`). Elle décrit un autre cadrage (section 7). Corrigée, elle reste soumise au point 3.
8. **Une seule description du cadrage, décidée par écrit avant le 19 nov.** La proposition du 9 nov. (9 à 10,5 JP [ES]) passerait sous le plancher de 750 € par JP à 6 500 € HT. Cette note recommande l'option A : 8,5 JP [ES], sous plafond écrit (section 8 ; D51) [PR, cette note].

---

## 1. Les faits nouveaux et leurs inconnues

| N° | Fait déclaré le 9 nov. | Code | Lien avec l'audit |
| --- | --- | --- | --- |
| 1 | GianLuca a engagé « une administrative centrale » pour gérer tous ses projets | [DR] | Répond en partie à U41, « personne qui exécutera au quotidien » (`interne/02-etat-des-sources.md:319`) |
| 2 | Il a racheté pour 1,5 M€ de bâtiments | [DR] | Aucun lieu n'est établi [FV négatif] (`annexes/travaux/ex-C9-lieux.md:219`, repris par `interne/03-cartographie-projets.md:276`) |
| 3 | Plusieurs commerces prévus, dont un cabaret-spectacle à côté de la galerie, et « plein d'autres projets » | [DR] | Cabaret « peut-être », « plus tard » au 4 nov. (`interne/03-cartographie-projets.md:276`) |
| 4 | « On veut et peut tout gérer avec l'IA aujourd'hui » (Morgan) | [DR] pour la phrase ; [HY] pour son contenu | Aucun gain de l'IA mesuré [IN] (`interne/07-processus-ia-et-essais.md:20`) |
| 5 | Présentation de 26 diapositives, privée, non envoyée à notre connaissance | [FV] pour le contenu lu ; [DR] pour « non envoyée » | Document client absent de la liste prévue (`annexes/travaux/strategie-retenue.md:785-796`) |

**Numérotation.** `interne/02-etat-des-sources.md` s'arrête à U45 (ligne 345), mais le registre a déjà ajouté U46 à U50 (`interne/14-registre-risques-inconnues-decisions.md:10`). Les nouvelles inconnues vont donc de **U51 à U62**.

| N° | Information inconnue | Qui peut répondre | Ce qu'elle bloque |
| --- | --- | --- | --- |
| U51 | Identité de l'administratrice (et genre du mot) | GianLuca | Tout échange avec elle |
| U52 | Statut : salariée ou prestataire, de quelle entité ; date d'arrivée | GianLuca | Rôles RGPD ; consignes (section 3) ; client de C6 |
| U53 | Périmètre (projets, lieux, entités) et temps disponible | GianLuca ; elle | Taille du cadrage et de C6 |
| U54 | Pouvoirs écrits : signature, dépense, accès aux données | GianLuca | Rôle de déléguée ou de valideuse |
| U55 | Outils et IA déjà utilisés ; documents de Marwin qu'elle a vus (CRM, diaporamas) | Elle ; Morgan | Préalables RGPD ; recadrage |
| U56 | Bâtiments rachetés : lesquels, adresses, usages | GianLuca | Inventaire ; lots C4, C7 |
| U57 | Entité propriétaire ; date ; financement ; actes | GianLuca ; son notaire | Qui commande quoi |
| U58 | Lien avec « six bâtiments », ancien bar-restaurant-hôtel, le M, le Vieux Relais, « l'ancienne affaire de Medhi » | GianLuca | Section 4.2 |
| U59 | Commerces : nature, lieux, exploitants, calendrier ; contenu des « autres projets » | GianLuca | Carte des rôles |
| U60 | Cabaret : lieu exact, exploitant, jauge, licences existantes | GianLuca | Section 5 ; lots C3, C4 |
| U61 | Présentation : qui a le lien, qui l'a vue, qui l'a validée (Mathys ?) | Morgan | D45 |
| U62 | Si elle est prestataire ou salariée d'une autre société : ce que Marwin peut lui demander directement, sans prêt de main-d'œuvre illicite ni marchandage (`annexes/travaux/syn-droit.md:350-362`) | Avocat en droit du travail | R56 ; D49 ; client de C6 |

U01 (entité qui signe) et U03 (budget) restent ouvertes.

---

## 2. Ce qui change et ce qui ne change pas

| Référence | Après les faits du 9 nov. | Effet |
| --- | --- | --- |
| Verdict (`annexes/travaux/strategie-retenue.md:41-43`) | Aucun fait ne nomme une entité, ne paie ni ne rapporte une parole directe de GianLuca | **Inchangé** |
| Remise en ordre, fuite d'abord | Échéance CNIL du 5 nov. passée ; décision [IN] (`README.md:18`). Rien ne part au client avant D03, D08 et l'accord écrit des associés (`interne/01-synthese-direction.md:68`), présentation comprise | **Inchangé** |
| Cadrage : 6 500 € HT, 3 à 4 semaines, moitié à la commande ; version réduite à 4 800 € HT | Inventaire plus large [DR] ; une interlocutrice pour réunir les pièces [HY] ; charge recalculée : 8,5 JP [ES], seulement sous plafond écrit (section 8) | **Prix, durée et paiement inchangés ; contenu borné, avec un écart signalé (section 8 ; D51)** |
| Report au 15 déc. 2026 et au 31 janv. 2027 (`annexes/travaux/strategie-retenue.md:697-698`) | Un patrimoine n'est pas une entité nommée | **Inchangé** |
| Plafond de 10 JP facturables par mois | En central, c'est la capacité elle-même [ES] (`interne/06-fonctionnement-a-deux.md:17`) | **Inchangé, plus contraignant** |
| Pilotage récurrent au plus tôt au mois 4 ; accélération possible, toujours sous 10 JP (`annexes/travaux/strategie-retenue.md:60`) | Une demande « tout de suite » devient plus probable [HY] | **Inchangé** |
| Refus : commission, paiement en bureaux, emploi ou capital, exploitation, robot devant le public | Rôle de bailleur plus plausible [HY] | **Inchangé** : bureaux refusés avant le bilan du mois 6 (`annexes/travaux/strategie-retenue.md:630`) |
| Modèle financier | Aucun encaissement ni contrat nouveau | **Inchangé** |

**Effet de l'administratrice sur chaque voie** [HY] :

| Voie | Effet | Pourquoi |
| --- | --- | --- |
| (a) Ventes d'œuvres (C2) | Légèrement renforcée | Elle peut coordonner l'appelant. Les préalables restent entiers (`annexes/travaux/strategie-retenue.md:311`) |
| (b) Pilotage (B0, puis B1) | Plus facile à exécuter, plus difficile à vendre | B0 exige un délégué (`annexes/travaux/strategie-retenue.md:248`) : elle peut l'être. Mais « coordonner tous les projets » recouvre le socle |
| (c) Outillage et passation (C6) | **Nettement renforcée** | Son préalable, « Décision de GianLuca de recruter ou de désigner une personne » (`annexes/travaux/strategie-retenue.md:330` ; voir aussi « désigner ou recruter une personne qui exécute », ligne 156), est peut-être rempli [DR]. C'est l'option hybride, « souvent la plus solide pour lui à long terme » [HY] (`interne/05-proposition-de-valeur.md:134`) |
| Lot unique (`interne/15-contre-analyse.md`, section 5) | Renforcée | Il peut n'acheter que des livrables (C1, C4, C7) |
| GianLuca recrute (4a, `interne/15-contre-analyse.md:303`) | **En partie réalisée** [DR] | Il aurait déjà choisi une personne pour l'exécution [DR] |
| Un associé salarié (4b, ligne 304) | Affaiblie | Le poste de coordination semble pourvu [DR] |

> **Écart avec la stratégie retenue : contenu et client du lot C6.**
> *Stratégie.* C6 « outillage et passation, avec aide au recrutement » comprend registre, tableau de bord, « 5 à 8 procédures écrites […] chacune avec sa fiche de secours manuel », comptes au nom de l'entité, « fiche de poste et grille d'entretien », deux formations et un test de restauration (`annexes/travaux/strategie-retenue.md:327`). Son client est l'entité « qui emploiera la personne, ou qui désigne un salarié existant » (ligne 325). Charge : 8 à 9 JP, dont « Morgan 3 à 4 (procédures, formation, fiche de poste) » (ligne 331) ; prix 7 500 € HT (ligne 333).
> *Cette note [PR, cette note].* Si l'administratrice est en poste et salariée de l'entité cliente : remplacer la fiche de poste et la grille d'entretien par l'inventaire de ses tâches et un entretien de prise en main d'une heure. Le reste ne change pas : les procédures écrites et les fiches de secours y sont déjà. Nom proposé : « C6 outillage et passation, prise en main par votre administratrice ». Charge [ES, cette note] : fiche de poste et grille ≈ 0,5 JP, remplacées par l'inventaire des tâches (≈ 0,25 à 0,5 JP) et l'entretien (≈ 0,25 JP), soit 8 à 9 JP à 0,25 JP près. Prix (7 500 € HT), réception et exclusions inchangés, dont « tout outil d'IA dans le recrutement ». Si le relevé tâche par tâche donne moins de 8 JP, le prix est revu selon la règle des lots (ligne 287).
> *Si elle est prestataire ou salariée d'une autre société.* C6 ne s'applique pas tel quel, puisque son client est l'entité qui emploie la personne. Revoir le client et le régime de C6 (U52) ; C6 seulement avec l'accord écrit de son employeur, et consignes passées par lui (ligne 584 ; U62).
> *Pourquoi.* Vendre une aide à un recrutement déjà fait serait facturer un travail inutile.
> *Limite.* Statut et périmètre [IN] (U52, U53). La stratégie ne chiffre pas la fiche de poste à part : les 0,5 JP sont une estimation de cette note. *Décision* : D50.

---

## 3. L'administratrice centrale

### 3.1 Partage des rôles [PR, cette note]

| Acteur | Fait | Ne fait pas |
| --- | --- | --- |
| **GianLuca** | Décide ; fait signer l'entité ; fixe les priorités en comité | Déléguer sans écrit (`interne/12-gouvernance-contrat-sortie.md:56`, G3) |
| **L'administratrice** | Exécute et coordonne au quotidien ; utilise les outils ; valide les envois dans la limite de pouvoirs écrits ; peut être déléguée et valideuse | Donner des ordres quotidiens à Morgan ou Mathys |
| **L'IA** | Prépare : tri, résumés, brouillons, recherche avec citations, rappels | Décider, signer, payer, contacter un tiers sans approbation (`interne/07-processus-ia-et-essais.md`, section 2.1) |
| **Marwin** | Prépare les décisions, outille, forme, mesure, livre des lots devisés ; garantit la réversibilité | Exécuter l'administratif (`annexes/travaux/strategie-retenue.md:650`) ; la diriger (`annexes/travaux/strategie-retenue.md:261`) |

### 3.2 Opportunités [HY]

- **Destinataire naturelle de la passation**, si elle est salariée de l'entité cliente : C6 vise l'entité « qui désigne un salarié existant » (`annexes/travaux/strategie-retenue.md:325`) ; « Marwin **ne reprend pas** l'exécution » (ligne 337) devient tenable.
- **Interlocutrice quotidienne** : elle comble le canal de travail inconnu (`interne/12-gouvernance-contrat-sortie.md`, section 10.1) et peut réunir les pièces du cadrage.
- **Valideuse possible**, si l'entité lui donne des pouvoirs écrits : la stratégie demande un « valideur nommé » de l'entité (`annexes/travaux/strategie-retenue.md:577, 629`). « Distinct d'un éventuel salarié » (ligne 629) vise un associé que GianLuca emploierait (ligne 631) [HY sur la lecture].
- **Adoption mesurable** : le critère de C6 (ligne 336) s'applique enfin à quelqu'un.

### 3.3 Risques à inscrire au registre

| N° proposé | Risque | Prob. [HY] | Parade |
| --- | --- | --- | --- |
| R53 | GianLuca juge que l'administratrice suffit ; pas de cadrage | Moyenne | Présenter le cadrage comme ce qui dit quoi outiller en premier pour elle, et à quel coût ; accepter de réduire à C6 ou à un lot (`annexes/travaux/strategie-retenue.md:695`). Le cadrage ne produit pas d'outils (ligne 227) |
| R54 | Double emploi perçu, tension avec elle | Moyenne | Rôles écrits ; l'inviter au premier entretien ; Marwin ne pilote pas ce qu'elle pilote |
| R55 | Subordination de fait par les consignes quotidiennes de l'administratrice | Faible à moyenne | *Base* : la présomption de non-salariat tombe en cas de « subordination juridique permanente » à l'égard du donneur d'ordre (C. trav. L8221-6 II) ; la société Marwin ne fait pas écran [FV] (`annexes/travaux/syn-droit.md:336` ; Légifrance, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044056617, consulté le 9 nov. 2026). Des ordres quotidiens donnés par elle au nom de l'entité seraient des ordres du donneur d'ordre : pouvoir de donner des ordres, d'en contrôler l'exécution et de sanctionner (`annexes/travaux/syn-droit.md:337`) [HY, à soumettre à l'avocat]. *Parade* : priorités du mois fixées en comité mensuel (`annexes/travaux/strategie-retenue.md:576`) et suivies en point hebdomadaire (ligne 256), sur bons de commande ; surveiller les indices de subordination (ligne 683) |
| R56 | Elle est prestataire ou salariée d'une autre société, et Marwin lui donne des consignes directes | Inconnue | Consignes via son employeur (`annexes/travaux/strategie-retenue.md:584` ; `annexes/travaux/syn-droit.md:350-362`) ; question à l'avocat en droit du travail (U62) |
| R57 | Accès à sa messagerie et aux données de plusieurs entités sans préalables ; IA grand public | Moyenne | Liste de contrôle (`interne/07-processus-ia-et-essais.md`, section 9.3) ; comptes de l'entité ; offres professionnelles |
| R58 | Dépendance à une seule personne, pour GianLuca et pour la relation | Moyenne | Procédures et fiches de secours (C6) ; deux administrateurs par compte |
| R59 | Outil perçu comme un contrôle de son travail | Moyenne | Le registre suit des décisions, jamais la performance d'une personne (`interne/12-gouvernance-contrat-sortie.md`, section 10.2) ; surveillance d'un salarié [HY, à voir avec l'avocat] |
| R60 | Le cadrage dépasse son forfait : portefeuille plus large, temps avec l'administratrice ; « 8 JP » non garantis | Moyenne | Option A : 8,5 JP [ES] seulement sous plafond écrit (section 8) ; JP réelles relevées, écart toléré ≤ 25 % (`annexes/travaux/strategie-retenue.md:171`) ; au-delà du plafond, choix de GianLuca ou proposition séparée. La marge est déjà de −9 à +13 % à 10 JP facturés [ES] (ligne 234) |

À l'inverse, une personne qui exécute **réduit** le risque de requalification lié au « s'occuper de tout » (`annexes/travaux/syn-droit.md:338-343`) [HY].

### 3.4 Ce qu'il faut apprendre d'elle, et quand

Aucun contact direct avant l'envoi du message de recadrage et l'accord de GianLuca : les questions passent d'abord par lui.

| Question | Pourquoi | Quand |
| --- | --- | --- |
| Qui est-elle, pour quelle entité, avec quel statut, depuis quand (U51, U52) ? | Rôles RGPD ; consignes | Rendez-vous, avant le 15 déc. 2026 |
| Que couvre-t-elle, avec quel temps (U53) ? | Taille du cadrage et de C6 | Rendez-vous |
| Quels pouvoirs écrits (U54) ? | Déléguée, valideuse, mandat | Avant le bon de commande |
| Quels outils et quelles IA utilise-t-elle ; qu'a-t-elle vu de Marwin (U55) ? | Préalables ; promesses déjà faites | Premier entretien du cadrage |
| Quelles tâches lui prennent le plus de temps ; que veut-elle garder ? | Mesure de départ ; adoption | Pendant le cadrage |

---

## 4. Les bâtiments (1,5 M€ déclarés)

### 4.1 Ce que le fait prouve, et ce qu'il ne prouve pas

- **Il ne prouve pas l'achat** : aucun acte connu [IN] (U57).
- **Il ne prouve pas un budget pour Marwin** : « un patrimoine déclaré n'est pas une trésorerie » (`annexes/travaux/strategie-retenue.md:566`). Un achat financé par emprunt peut même réduire la trésorerie [HY].
- **Il ne désigne pas une entité acheteuse** : le test du 15 déc. reste entier.
- **Il indique au plus** une capacité d'investir et une intention de développer des lieux [HY].
- **Entité propriétaire probablement distincte de l'exploitant** [HY], comme dans le scénario « plusieurs entités » (`interne/03-cartographie-projets.md:133`) : un bon de commande par prestation et par entité ; travaux au propriétaire, licences à l'exploitant.

### 4.2 Relier aux pièces historiques, sans conclure

| Pièce (citée par l'audit) | Ce qu'elle dit | Rapport avec le fait du 9 nov. |
| --- | --- | --- |
| `interne/offres-de-carlone-catalogue-crm.md:9`, via `annexes/travaux/ex-C9-lieux.md:22` | « Six bâtiments » déjà rachetés ; galerie en 2027 [DR] | Peut-être le même ensemble ; le montant serait la seule nouveauté [HY] |
| `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:14`, via `interne/03-cartographie-projets.md:241` | Ancien bar-restaurant-hôtel avec cour racheté pour la galerie [DR] | Compatible ; inclusion dans les 1,5 M€ [IN] |
| Même pièce, ligne 15, via `annexes/travaux/ex-C9-lieux.md:23, 130` | Il « souhaite racheter « le M » » pour un projet de cabaret [DR] : un souhait au 28 oct. | Le cabaret est désormais « à côté de la galerie » ; rien ne dit qu'il est dans le M, ni que le M est acheté [IN] |
| Dossier du 21 oct. p. 32 et `crm/PASSATION.md:41`, via `annexes/travaux/ex-C9-lieux.md:24-26` | Vieux Relais et le M « changent de main » ; « un associé rachète » | Racheteur non nommé : peut-être pas GianLuca [HY] |
| `annexes/travaux/ex-C9-lieux.md:129` | Le Vieux Relais serait peut-être la galerie [HY de l'audit] | Non confirmé |
| `interne/contexte-projet-carlone.md:24`, via `interne/03-cartographie-projets.md:51` | Rachat de « l'ancienne affaire de Medhi » [DR] | Si elle en fait partie, déclarer le lien de Morgan avec BOJ.ART devient plus urgent (`annexes/travaux/strategie-retenue.md:635`) [HY] |

Règle : ne pas additionner ces mentions. Avant l'inventaire validé, il y a « des bâtiments », pas une liste.

### 4.3 Nouveaux chantiers et offres touchées

| Chantier | Ce que l'audit sait | Offre (`interne/04-catalogue-offres.md`) |
| --- | --- | --- |
| Travaux | Autorisation de travaux d'un ERP : 4 mois ; permis de construire : 5 mois [FV] (`annexes/travaux/rj-R5-art-lieux.md:333`) | C7 (rentabilité d'un rachat ou de travaux) ; dossiers de décision du socle |
| Sécurité des ERP | Visite de réception et arrêté d'ouverture [FV] (`annexes/travaux/rj-R5-art-lieux.md:332`) ; registre de sécurité (ligne 355) ; règles sur les éléments structuraux combustibles au 1er juin 2027 [FV pour la date ; HY pour nos bâtiments] (ligne 379) | C4 (tableau des lieux et de leurs obligations) |
| Accessibilité | Non étudiée [IN] (`annexes/travaux/rj-R5-art-lieux.md:395`) | C4, avec un professionnel |
| Entretien | Vérifications par organismes agréés selon la catégorie [FV] (`annexes/travaux/rj-R5-art-lieux.md:355`) | Veille des échéances du socle (`annexes/travaux/strategie-retenue.md:263`) ; offre D plus tard |
| Énergie | Non étudiée [IN] | Aucune ; capteurs achetés par l'entité |

La gestion immobilière reste exclue pour Marwin (`annexes/travaux/strategie-retenue.md:650`).

---

## 5. Le cabaret-spectacle et les commerces

**Principe** : Marwin prépare, l'exploitant détient et signe. Ni Morgan ni Mathys ne peuvent porter les licences sans devenir exploitants [HY] (`annexes/travaux/rj-R5-art-lieux.md:467`). Aucun travail avant que le lieu et l'exploitant soient connus (ligne 469).

| Obligation | Ce que l'audit a établi | Qui la porte | Ce que Marwin prépare |
| --- | --- | --- | --- |
| Récépissé de déclaration d'entrepreneur de spectacles vivants (valant licence) | Depuis octobre 2019, la licence est remplacée par un récépissé de déclaration [FV] (F22365). Un cabaret qui programme régulièrement est exploitant de lieu, 1re catégorie ; déclaration en ligne, valable 5 ans ; formation à la sécurité des spectacles [FV] (`annexes/travaux/rj-R5-art-lieux.md:421-424`). Sans récépissé : amende administrative jusqu'à 7 500 € pour une personne morale (1 500 € pour une personne physique) ; fermeture possible jusqu'à 1 an [FV, F22365] (ligne 425). Fiche F22365 : https://entreprendre.service-public.gouv.fr/vosdroits/F22365, vérifiée le 5 avril 2024, consultée le 9 nov. 2026 | Exploitant | Calendrier, dossier, renouvellement |
| Débit de boissons, permis d'exploitation | Licence IV impossible à créer : rachat ou transfert ; licence restaurant avec repas ; permis de 20 h valable 10 ans ; déclaration en mairie 15 jours avant [FV] (`annexes/travaux/rj-R5-art-lieux.md:427-430`) ; horaires tardifs [IN] (ligne 441) | Exploitant | Comparaison des options ; dossier |
| Sécurité et accessibilité de l'ERP | Type L, 4e catégorie au-delà de 50 personnes ; type N ou P si repas ou danse [FV] (`annexes/travaux/rj-R5-art-lieux.md:417-420`) ; événement inhabituel : demande deux mois avant (ligne 334) ; accessibilité [IN] | Exploitant ; propriétaire pour les travaux | Lots C4 et C3 |
| Droits musicaux et son | Sacem : autorisation préalable (`annexes/travaux/rj-R5-art-lieux.md:345`). Spectacles : forfait si le budget des dépenses est d'au plus 5 000 € et l'entrée d'au plus 20 € ; au-delà, un taux sur la plus élevée des deux bases, recettes ou budget des dépenses. Bar ou restaurant à ambiance musicale : 1,65 % du CA HT au-delà de 153 000 €. Spré pour la musique enregistrée diffusée [FV, F3094 : https://entreprendre.service-public.gouv.fr/vosdroits/F3094, vérifiée le 12 août 2025, consultée le 9 nov. 2026]. Barème applicable au cabaret : à confirmer avec la Sacem [IN]. Sons amplifiés : 102 dB(A) et étude d'impact [FV] (ligne 434) | Exploitant | Déclarations préparées, une fois le barème confirmé |
| Artistes et techniciens | Présumés salariés (L7121-3) [FV] (`annexes/travaux/rj-R5-art-lieux.md:344, 431`). Cabaret exploitant de lieu : embauche directe, hors Guso ; un commerce qui organise des spectacles à titre accessoire passe par le Guso [FV] (C. trav. L7122-22, 2°, en vigueur depuis le 1er mai 2008 : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006904586, consulté le 9 nov. 2026 ; F22365, partie « Activité occasionnelle »). La ligne 343 de `rj-R5-art-lieux.md` ne vaut que pour les événements occasionnels. Convention collective [IN] (ligne 462) | Employeur : exploitant ou organisateur | Plannings ; contrats préparés ; aucune IA de sélection |
| Robot sur scène | Règlement machines, droit du travail, GN 6 [HY] (`annexes/travaux/rj-R5-art-lieux.md:443`) | — | Rien : exclu (`annexes/travaux/strategie-retenue.md:646`) |
| Commerces | Hygiène alimentaire, caisse, billetterie, emploi : non étudiés [IN] | Chaque exploitant | Questions aux professionnels pendant le cadrage |

L'exploitation reste **exclue** ; le cabaret revient seulement sous forme de dossiers (C3, C4, C7) et de coordination sous mandat écrit (`annexes/travaux/strategie-retenue.md:647`).

---

## 6. « Tout gérer avec l'IA aujourd'hui »

### 6.1 Réaliste, pas réaliste (novembre 2026)

| Réaliste, avec relecture humaine | Pas réaliste ou interdit |
| --- | --- |
| Rédiger, résumer, classer, traduire | Décider, signer, payer à la place d'une personne |
| Comptes rendus de réunion, avec accord des participants | Conseil juridique ou fiscal ; montants calculés par le modèle de langage au lieu d'une formule (`interne/07-processus-ia-et-essais.md:69`) |
| Recherche documentaire avec citations | Contacter un tiers ou le public sans approbation |
| Rappels d'échéances ; tableaux de bord par formule | Garantir la sécurité du public |
| Grilles de comparaison de devis ; dossiers pour les professionnels | Suivre douze domaines en parallèle à deux |

**« Veut ».** L'ambition retenue est de piloter le portefeuille par paliers payés et mesurés (`annexes/travaux/strategie-retenue.md:45`). Tout gérer avec l'IA n'est une cible à aucun horizon, puisque décider, signer et payer restent humains [PR, cette note]. **« Peut »** n'est pas démontré : les pièces montrent de la production, pas de la livraison [FV] (`interne/06-fonctionnement-a-deux.md:16`) ; pour « le travail de 100 personnes », « aucune pièce ne l'approche » (`annexes/travaux/strategie-retenue.md:163`).

### 6.2 Ce que cela implique à deux

- **Capacité** : environ 10 JP facturables par mois en central, dont ≈ 3 JP de production ; un socle, deux projets actifs, un en veille [ES] (`interne/06-fonctionnement-a-deux.md:17, 19, 21`).
- **Entretien** : la stratégie admet au plus 0,5 JP de maintenance par mois et par processus. C'est une condition d'entrée de l'offre D, pas une estimation (`annexes/travaux/strategie-retenue.md:349`). Les seules 13 aides automatiques de la présentation, à ce plafond, prendraient jusqu'à 6,5 JP par mois, soit environ deux tiers des 10 JP, avant tout travail nouveau. Les 34 autres coûtent du temps humain à chaque usage [ES].
- **Démultiplication** : « le travail de 100 personnes » suppose un facteur de 50 à 85 [ES] ; les cibles sont de 1,3 à 1,5 à 6 mois et de 1,5 à 2 à 12 mois [HY], à fixer avec GianLuca après la mesure de référence (`interne/06-fonctionnement-a-deux.md:24` ; `annexes/travaux/strategie-retenue.md:163`) : au mieux, le travail de 1,5 à 2 personnes sans outils, en central.
- **Conséquence [PR, cette note]** : la première année, deux à quatre processus outillés et mesurés (registre et comptes rendus, recherche documentaire, échéances, préparation budgétaire), en ligne avec « gains mesurés sur au moins deux processus » (`annexes/travaux/strategie-retenue.md:145`). Rien n'est automatisé au départ (`interne/07-processus-ia-et-essais.md:22`).

### 6.3 Usages à exclure ou à encadrer

| Usage | Règle | Source |
| --- | --- | --- |
| Tri, notation ou évaluation de candidats ou de salariés (artistes, personnel, administratrice) | **Exclu**, même si le haut risque est reporté au 2 déc. 2027 | `interne/07-processus-ia-et-essais.md:107, 574` |
| Décisions juridiques ou financières | Préparées par l'IA, validées par le professionnel, signées par l'entité | `annexes/travaux/strategie-retenue.md:580-581` |
| Envoi, publication, transmission à un tiers, campagne | Approbation humaine hors de portée de l'agent ; payer reste interdit | `interne/07-processus-ia-et-essais.md`, sections 2.1 et 8.1 |
| Agent qui répond au public (site, téléphone) | Règle de l'audit : toujours dire qu'il s'agit d'une IA. Obligation légale du fournisseur (art. 50, § 1), donc de Marwin si elle livre l'agent sous son nom [FV texte ; HY sur la qualification]. Avec un outil du marché, l'obligation légale pèse sur son éditeur ; pour le client, c'est une bonne pratique. Aucun agent vocal sortant | `interne/07-processus-ia-et-essais.md:573` ; `annexes/travaux/syn-droit.md:660-661` ; `annexes/travaux/strategie-retenue.md:652` |
| Contenus générés | Mention « généré par IA » ; aucune image générée présentée comme réelle | `annexes/travaux/strategie-retenue.md:798` ; `annexes/travaux/syn-droit.md:659` |
| Données personnelles (messagerie, clients, invités, salariés) | Préalables complets ; offres professionnelles ; comptes de l'entité | `interne/07-processus-ia-et-essais.md:26` |

---

## 7. La présentation du 9 novembre

### 7.1 Verdict

**L'architecture est juste ; la promesse d'échelle ne l'est pas.** Mettre l'administratrice au centre, l'IA en appui et Marwin en outilleur est cohérent avec la voie (c). Mais :
- le titre de `idee` et la formule « grande structure » (`compris:15` ; `trajectoire:24` ; notes `compris:19`, `administratrice:39`, `trajectoire:31`) reprennent la promesse « tout gérer » sous une autre forme, et font de Marwin le pilote [FV] ;
- le catalogue est intenable à deux (section 6.2) ;
- la règle « rien ne part sans relecture » est contredite par des envois « automatiques » ;
- le CRM, exposé au 4 nov. [DR] (`README.md:91`), est présenté comme un atout ;
- le cadrage décrit diffère de la proposition du 4 nov. et de celle du 9 nov. (section 8).

La présentation est signée des deux associés (`echange:20`) ; l'accord de Mathys est [IN] (U07).

**Les notes de l'orateur sont visibles par quiconque a le lien** [FV : contenu des balises `<aside>`, lu le 9 nov.]. Elles portent les promesses les plus fortes. Les relire avec le même tableau (ligne « Notes de l'orateur » de 7.3), ou les vider avant tout partage.

**Ce qui est juste** : les trois colonnes « vous décidez », « une personne contrôle tout », « les gains se mesurent » (`idee:8-17` ; le titre, ligne 4, est à corriger) ; ce qu'on ne confie pas à l'IA (`ia-aujourdhui:26-33`) ; comptes et données à son nom dès le premier jour (`logiciels:18`, première phrase ; la seconde est à corriger) ; « rien de facturé deux fois » (`methode:24-25`) ; prudence sur la robotique (`robotique:19`), conforme à `annexes/travaux/syn-droit.md:56, 75` ; licences au nom de l'exploitant (note de `cat-cabaret:18`, dont une phrase est à retirer) ; prix remis à part (`premier-pas:26`).

### 7.2 Contrôle des éléments internes [MM]

Recherche refaite le 9 nov. sur le texte et les notes des 26 diapositives de l'ordre de `PIA/deck.json:7` : aucun montant en euros ; aucun « 750 », « 15 000 », « 30 000 », « 6 500 » ou « 4 800 » ; aucune rémunération, JP ou disponibilité ; aucune mention de Medhi, BOJ.ART, STRATES, du laboratoire, de Jarvis, de la fuite ou de l'ancien prénom ; pas de 1,5 M€. **Ce contrôle ne cherche que des éléments internes : il ne juge pas les promesses, y compris celles des notes de l'orateur (7.1, 7.3).** Deux points limites : la cible « 1,5 à 2 fois » vient d'un paramètre interne [HY], à fixer avec GianLuca après la mesure de référence (`annexes/travaux/strategie-retenue.md:163`), mais elle est annoncée comme « Notre objectif » avant toute mesure (`apports:29, 33`) ; « votre outil de prospection » (`societe:10`) tranche un régime de propriété non décidé (D12). Images non vues, seulement leurs textes alternatifs [IN]. Aides : 47, dont 13 « automatiques », 24 « assistées », 10 « préparées » [MM, comptage refait le 9 nov.].

### 7.3 Corrections recommandées, par gravité

| Id | Problème | Correction proposée | Gravité |
| --- | --- | --- | --- |
| Notes de l'orateur (`<aside>` des 26 vues) | Visibles par qui a le lien ; l'ancienne version de ce tableau ne visait que le texte des diapositives. Promesses : « une seule personne peut coordonner un ensemble de lieux et de commerces avec les moyens d'une grande structure » (`administratrice:39`) ; elle « permet à deux personnes de préparer, suivre et produire beaucoup plus qu'avant » (`idee:21`) ; « L'IA peut en automatiser une grande partie » (`cat-cabaret:18`) ; « tenir tout cela à jour sans effort » (`cat-galerie:18`) ; « nous agissons comme sous-traitant, sous contrat » (`regles:17`), rôle RGPD non tranché (U46) ; « La lecture automatique de documents […] est mûre » (`avancees:15`) ; « grande structure » (`compris:19`, `trajectoire:31`) ; « cinq premières automatisations » et « domaine par domaine » (`premier-pas:28`) | Relire toutes les notes avec ce tableau, ou les vider avant tout partage. Remplacer par : « une personne peut faire davantage sur les tâches outillées et mesurées » (`administratrice:39`, `idee:21`) ; retirer la phrase de `cat-cabaret:18` ; « à tenir à jour avec moins d'effort, chaque écriture validée par une personne » (`cat-galerie:18`) ; « rôles RGPD fixés par écrit avec votre conseil avant toute donnée réelle » (`regles:17`) ; « la lecture automatique de documents progresse ; chaque résultat reste vérifié » (`avancees:15`) ; retirer « grande structure » ; aligner `premier-pas:28` sur la ligne `premier-pas` ci-dessous | Élevée |
| `idee`, `compris` | Titre « Une petite équipe, outillée par l'IA, pour piloter des projets qui en demanderaient beaucoup plus » (`idee:4`) : la promesse « tout gérer » sous une autre forme, avec Marwin comme pilote ; « Un ensemble qui demanderait une grande structure » (`compris:15`) | Titre de `idee` : « Votre administratrice, mieux outillée ; nous préparons et mesurons » ; retirer « grande structure » de `compris:15` | Élevée |
| `premier-pas` | « Les cinq premières automatisations, choisies avec votre administratrice » (ligne 12) : lu seul, le cadrage semble livrer des outils, exclus du cadrage (`annexes/travaux/strategie-retenue.md:227`) ; « domaine par domaine » (ligne 13) contre une voie à la fois (ligne 241) ; carte des rôles et délégation absentes ; « La structure qui signe et qui règle » (ligne 19) oublie le valideur (ligne 185) | Selon l'option de la section 8. **Option A (recommandée)** : « Les premières tâches à essayer, avec leur mesure de départ » ; « Le choix argumenté de la suite, avec la carte des rôles et la grille de délégation » ; « La structure qui signe, règle et valide ». **Option B** : garder les lignes 12 et 13 en ajoutant « à essayer après le cadrage, pas encore en service » ; corriger la ligne 19 ; gravité alors Moyenne | Élevée (option A) |
| `idee`, `modes` | « Rien ne part sans relecture » (`idee:13`) contre des envois classés « automatiques » | « Automatique » réservé aux tâches internes ; tout envoi « assisté » | Élevée |
| `administratrice` | « Fixe les priorités du jour » (ligne 13), à côté de « Marwin Tech, en appui » : contraire à R55 et à D49 ; « Maintient, sauvegarde, sécurise » et « Mesure et améliore chaque mois » (lignes 31-32) : un service récurrent sans prix ni limite, qui ne vient qu'au mois 4 (socle) ou au mois 7 (exploitation) (`annexes/travaux/strategie-retenue.md:43, 339`) ; « Prend en charge les gros chantiers : CRM, contenus, événements, logiciels » (ligne 33) promet production et organisation d'événements ; « Rien n'est envoyé, payé ou signé sans elle ou sans vous » (ligne 37) suppose des pouvoirs inconnus | « Organise sa journée ; les priorités confiées à Marwin se fixent en point hebdomadaire et en comité, sur bon de commande » ; « Maintenance et suivi mensuel : dans un suivi régulier commandé après l'essai » ; « Marwin réalise des travaux devisés à part » ; « Elle valide dans la limite des pouvoirs que vous lui donnez par écrit » | Élevée |
| `domaines` | Douze domaines, robotique comprise, pour deux projets actifs | « Exemples ; nous avançons sur un domaine à la fois » | Élevée |
| `trajectoire` | La réserve « ambition, pas une promesse » ne couvre que deux et cinq ans (ligne 29) : la colonne « Dans 1 an » se lit comme un engagement. Elle promet « Votre administratrice outillée sur tous les projets » et « Galerie et cabaret préparés avec nos outils » (ligne 10), contraire à la section 5 et à D52 ; à 2 ans, « ventes réguliers » (ligne 17), contraire à « aucun résultat promis » (`annexes/travaux/strategie-retenue.md:798`) ; à 5 ans, « grande structure » (ligne 24) | Réserve étendue aux trois horizons ; à 1 an : « Deux à trois processus outillés et mesurés » et « Dossiers des lieux prêts, si vous les commandez » ; retirer « ventes réguliers » et « grande structure » | Élevée |
| `etapes`, `logiciels`, `cover` | « Vous pouvez vous arrêter en gardant tout ce qui a été fait » (`etapes:35`) ; « changer de prestataire sans rien perdre » (`logiciels:18`). Or les droits ne sont cédés qu'au paiement complet et les composants génériques restent sous licence (`annexes/travaux/strategie-retenue.md:287`) ; le socle a un préavis d'un mois (ligne 274). La présentation se contredit (« Cession écrite à chaque livrable payé », `regles:13`). « Sans engagement » (`cover:7`) voisine avec « Nos engagements » (`logiciels:17`) | « Vous pouvez vous arrêter à la fin de chaque étape ; vous gardez ce qui est payé, vos comptes et vos données ; restitution sous 15 jours ouvrés » ; `logiciels:18` : « sans rien perdre de ce qui est payé » ; titre de `logiciels:17` : « Nos règles » | Élevée |
| `cat-marketing` | Site qui répond seul (ligne 10) ; campagnes « à partir du CRM déjà construit » (ligne 14) | Mention d'IA au visiteur ; « après remise en conformité du fichier » | Élevée |
| `crm` | « 500 entreprises de la Nièvre classées », « coordonnées vérifiées » (lignes 9-10) : 283 numéros sur 471 « à confirmer » [FV] (`interne/07-processus-ia-et-essais.md:20`) ; CRM exposé au 4 nov. [DR] (`README.md:91`) ; fuite dont le traitement est inconnu de l'audit [IN] (`README.md:18`) | Texte prévu : « Un CRM de 500 fiches existe ; il sera remis en conformité avant tout usage » (`annexes/travaux/strategie-retenue.md:819`) | Élevée |
| `societe` | « Votre outil de prospection » (ligne 10) ; « immatriculée avant tout engagement » (ligne 14) contre un bon de commande « en formation » (`pour-gianluca/proposition-de-cadrage.md:58`) ; « réseau de spécialistes » non documenté (ligne 21) | « Un outil de prospection existe » ; « avant toute facture et tout démarrage » ; « des spécialistes que votre société engage directement » | Élevée |
| `cover` | « Vision d'un atelier Marwin Tech » avec bras robotisé (ligne 2) : aucun atelier opérationnel documenté [FV négatif] (« aucune preuve d'atelier opérationnel », dépôt `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` p. 1-2, via `annexes/travaux/ex-C8-creations.md:72`) ; laboratoire retiré (`annexes/travaux/strategie-retenue.md:645`) | Visuel d'un lieu ; mention « générée par IA » gardée | Moyenne |
| `avancees` | Accueil téléphonique et IA locale (lignes 8, 11) : hors des onze processus ; IA locale retirée | Retirer l'IA locale ; voix limitée aux comptes rendus | Moyenne |
| `cat-admin`, `cat-galerie`, `cat-cabaret`, `cat-finance` | Automatiques à revoir : registre des décisions (`cat-admin:10`), prêts et transports (`cat-galerie:15`), réservations et caisse (`cat-cabaret:8, 12`), pièces « transmises » à l'expert-comptable (`cat-finance:10`) ; « documents conformes » (`cat-galerie:13`) ; « heures suivies » (`cat-cabaret:10`) ; exclusion des candidats seulement en note (`cat-finance:18`) | Passer en « assisté, après essai » ; « préparés pour votre validation » ; pas de suivi individuel ; exclusion écrite sur la diapositive | Moyenne |
| `cat-galerie` | « Droit de suite et contributions calculés et préparés » (ligne 14) : les montants se calculent par formule, jamais par le modèle de langage (`interne/07-processus-ia-et-essais.md:69`) | « Montants calculés par formule, puis validés » | Moyenne |
| `apports` | « Notre objectif » (ligne 29) et « Notre objectif est d'atteindre » (note, ligne 33), avant toute mesure, alors que la cible est une hypothèse « à fixer avec GianLuca après la mesure de référence » (`annexes/travaux/strategie-retenue.md:163`) et qu'aucun gain n'est mesuré (`interne/07-processus-ia-et-essais.md:20`) | « La cible sera fixée avec vous après la mesure de départ » ; garder le chiffre en interne | Moyenne |
| `regles`, `robotique` (note) | « Contrat de sous-traitance » (`regles:8`) : rôles RGPD non tranchés (U46). « Déduction réservée aux œuvres faites main » (`regles:14`) et « exécutées entièrement à la main par l'artiste » (note de `robotique:21`) : trop absolu ; l'art. 98 A de l'annexe III admet aussi la sculpture « exécutée entièrement par l'artiste », 8 fontes et 30 photographies au plus (`annexes/travaux/syn-droit.md:558`) | « Rôles fixés par écrit avec votre conseil avant toute donnée réelle » ; « Déduction sous conditions de l'art. 98 A ; à valider par l'expert-comptable » | Moyenne |
| `robotique` | Rouvre robotique et création, gelées (`annexes/travaux/strategie-retenue.md:644-646`) | Une ligne « plus tard, sous conditions » dans `etapes`, ou retrait | Moyenne |
| `methode` | « Validé par vous avant d'être facturé en entier » (ligne 17) contredit la règle de réception (`annexes/travaux/strategie-retenue.md:235, 287`) ; « par projet » (ligne 8) au lieu de « par prestation et par entité » | Reprendre la formule de la description retenue du cadrage (section 8) | Moyenne |
| `pour-dautres` | Parle de Marwin plus que de lui ; créations gelées | Retirer, ou une phrase dans `societe` | Faible |
| `echange` | Rien sur l'administratrice | Ajouter « Quel rôle et quels pouvoirs pour votre administratrice ? » | Faible |

**Ce qui manque** :
- l'information sur l'incident de données, par un écrit séparé validé par le conseil (`annexes/travaux/strategie-retenue.md:53, 809`) ;
- la comparaison de coûts, c'est-à-dire pourquoi payer Marwin en plus de l'administratrice (`annexes/travaux/strategie-retenue.md:370-378`) ;
- « un sujet, un accord » (`interne/12-gouvernance-contrat-sortie.md:62`) ;
- les exclusions : exploitation et encaissement ne figurent que dans les notes de l'orateur (`cat-cabaret:18`, `cat-galerie:18`), à remonter sur les diapositives ; l'intermédiation n'y est nulle part ;
- « Outils et abonnements payés par votre société, à son nom » (`annexes/travaux/strategie-retenue.md:188`) : les 47 aides supposent des abonnements (réservations, caisse, sites, capteurs, publicité) ;
- « Maintenance et suivi mensuel : seulement dans un suivi régulier commandé après l'essai » (lignes 43, 339) ;
- une limite de capacité lisible.

---

## 8. Le cadrage : une seule description

### 8.1 Trois descriptions pour une seule offre [FV]

| Pièce | Ce qu'elle décrit | Charge |
| --- | --- | --- |
| Stratégie et proposition du 4 nov. (`annexes/travaux/strategie-retenue.md:225-229` ; `pour-gianluca/proposition-de-cadrage.md:39-46`) | Huit livrables, dont la carte des rôles par projet (3) et la grille de délégation et le projet de mandat par entité (4) ; jusqu'à 15 pièces ; deux entretiens | 8 JP annoncés, 8,5 au détail des tâches [ES] (`interne/04-catalogue-offres.md:146-150`) |
| Présentation, `premier-pas:10-13` | Quatre résultats, dont « Les cinq premières automatisations, choisies avec votre administratrice » et « Le choix argumenté de la suite, domaine par domaine » | Non dite |
| Proposition du 9 nov. (`pour-gianluca/2026-11-09-proposition-de-cadrage.md:45-48, 67`) | Les quatre résultats de `premier-pas`, « mot pour mot » (ligne 168), bornés : « un choix et un plan d'essai, pas une mise en service » (ligne 47) ; deux séances avec l'administratrice ; carte des rôles limitée aux trois priorités ; mandat reporté (encadré n° 2, lignes 236-241) | 9 à 10,5 JP [ES], soit ≈ 620 à 720 € par JP à 6 500 € HT, sous le plancher (lignes 228-230) |

La version d'avant relecture de cette note voulait corriger `premier-pas` vers la proposition du 4 nov., et fixait « prix et 8 JP inchangés » sans calcul (ancienne D51). La proposition du 9 nov., datée du même jour, fait l'inverse et demande de réconcilier les deux textes (ligne 233). Avec deux consignes opposées, D46 ne pouvait pas être exécutée. « 8 JP inchangés » est retiré.

**Règles qui tranchent** [PR] : plancher de 750 € HT par JP estimée, « jamais remisé » ; en dessous, « on réduit le périmètre ou on refuse » (`annexes/travaux/strategie-retenue.md:119, 396`). Un cadrage à 7 500 € HT a été écarté faute de référence (ligne 130). Le cadrage ne produit ni supports, ni catalogue, ni outils (ligne 227). Écart toléré entre JP réelles et estimées : 25 % (ligne 171). À 6 500 € HT, le plancher est atteint à ≈ 8,7 JP [ES].

### 8.2 Charge par tâche [ES]

| Tâche (`annexes/travaux/strategie-retenue.md:229`) | Stratégie | Option A (recommandée) | Option B (proposition du 9 nov., lignes 218-228) |
| --- | --- | --- | --- |
| Préparation | 1 | 1 : quinze pièces analysées au plus | 1 |
| Entretien et trajet | 1,5 | 1,5 : l'administratrice est invitée au premier entretien ; pas de séance séparée | 1,75 à 2 : séance de 2 h avec elle le même jour |
| Analyse et inventaire | 2 | 2 : fiches courtes, sous le plafond écrit (8.3) | 2,5 à 3 : tout ce qui est signalé, en fiche courte |
| Carte des rôles | 1 | 0,75 : une ligne par projet de l'inventaire ; professionnels détaillés pour les trois priorités | 0,5 : trois priorités seulement |
| Priorités, mandat et comparaison | 1,5 | 1,5 : grille de délégation et projet de mandat par entité, dans le plafond, rôle de l'administratrice compris | 1 : mandat reporté ; suite limitée aux domaines des priorités |
| Tâches à essayer en premier | 0 | 0,25 : au plus trois, une par priorité, avec leur mesure de départ, dans le livrable 7 | 0,75 à 1,25 : cinq automatisations ; séance d'1 h à distance |
| Restitution | 0,5 | 0,5 | 0,5 |
| Contrôle et corrections | 1 | 1 | 1 à 1,25 |
| **Total** | **8,5** | **8,5** | **9 à 10,5** |
| Prix par JP à 6 500 € HT | ≈ 765 € | ≈ 765 € | ≈ 620 à 720 € |

Calculs [MM] : 1 + 1,5 + 2 + 0,75 + 1,5 + 0,25 + 0,5 + 1 = 8,5 ; 6 500 ÷ 8,5 ≈ 765 ; 6 500 ÷ 750 ≈ 8,67 ; 9 × 750 = 6 750 ; 10,5 × 750 = 7 875. Les JP elles-mêmes restent des estimations [ES].

### 8.3 Deux options, une recommandation

**Option A, recommandée [PR, cette note].** Garder la description de la stratégie et de la proposition du 4 nov. (huit livrables), avec trois ajouts : l'inventaire élargi, sous plafond écrit ; l'administratrice invitée au premier entretien ; « les tâches à essayer en premier, avec leur mesure de départ » (au plus trois, une par priorité ; un choix, pas une mise en service) dans le livrable 7. Pas de « cinq automatisations ». 6 500 € HT pour 8,5 JP [ES], ≈ 765 € par JP. `premier-pas` est corrigé (7.3). La proposition du 9 nov. est marquée « à reprendre » : une nouvelle version datée garde ses sections 1, 4, 5 et 7 et son tableau « qui valide quoi », et revient aux huit livrables en section 2. Les versions du 4 et du 9 nov. restent intactes.

**Plafond écrit de l'option A** [PR, cette note, chiffres à ajuster par les associés] : trois entités et douze éléments (bâtiments, lieux, commerces, projets) en fiche courte ; quinze pièces analysées. Au-delà, les éléments sont listés sans fiche, et GianLuca choisit : un élément en remplace un autre, ou il fait l'objet d'une proposition séparée, comme l'écrit déjà la proposition du 9 nov. (ligne 65). Rien n'est renvoyé d'office au lot C4, qui reste le tableau des obligations par lieu (`annexes/travaux/strategie-retenue.md:294`). Version réduite à 4 800 € HT (6 JP) inchangée (ligne 231), sans les tâches à essayer.

**Option B.** Garder la description de la proposition du 9 nov. : quatre résultats, cinq automatisations bornées, deux séances avec l'administratrice. Charge recalculée : 9 à 10,5 JP [ES]. Il faut alors soit resserrer jusqu'à 8,5 JP au plus, ce que les resserrements proposés par la proposition (8,5 à 9 JP, ligne 231) ne garantissent pas ; soit fixer un prix d'au moins 750 € par JP recalculée : 6 750 € HT à 9 JP, 7 875 € HT à 10,5 JP [ES]. Ce prix irait contre l'idée écartée d'un cadrage à 7 500 € (`annexes/travaux/strategie-retenue.md:130`) et demanderait de nouvelles versions datées de `interne/11-proposition-commerciale-revisee.md` et `interne/13-preparation-rendez-vous.md`. `premier-pas` serait seulement borné (gravité Moyenne).

**Non retenu, dans les deux options** : accepter ≈ 250 € HT sous le plancher, comme le recommande la proposition du 9 nov. (ligne 231). C'est contraire à « jamais remisé » (`annexes/travaux/strategie-retenue.md:396`).

**Pourquoi A.** Elle applique la règle « on réduit le périmètre » sans nouveau prix. Elle garde la carte des rôles par projet et la grille par entité promises le 4 nov. (`pour-gianluca/proposition-de-cadrage.md:41-42`). Elle ne laisse pas croire que le cadrage livre des outils. Elle ne transforme pas « tout gérer avec l'IA » en livrable. **Limite de A** : deux documents à reprendre (présentation, proposition) ; l'administratrice est moins associée au choix des tâches ; Morgan peut juger le message plus faible.

> **Écart avec la stratégie retenue : périmètre du cadrage (option A).**
> *Ce que dit la stratégie.* Huit livrables, dont « 3. Carte des rôles par projet » et « 4. Grille de délégation et projet de mandat par entité » (`annexes/travaux/strategie-retenue.md:225`) ; jusqu'à 15 pièces (ligne 226) ; 8 JP, 8,5 au détail des tâches (ligne 229 ; `interne/04-catalogue-offres.md:146-150`) ; 6 500 € HT (ligne 231).
> *Ce que propose cette note [PR, cette note].* Mêmes huit livrables, même prix, avec le plafond écrit de 8.3. **Livrable 3** : une ligne par projet de l'inventaire (exploitant, organisateur, vendeur, responsable du traitement, connus ou [IN]) ; les professionnels à consulter sont détaillés pour les trois priorités seulement. **Livrable 4** : grille de délégation et projet de mandat par entité, gardés dans la limite de trois entités, rôle de l'administratrice compris ; mandat de dépense à 0 € pendant le cadrage et l'essai (ligne 589). **Livrable 7** : la mesure de référence comprend au plus trois tâches à essayer en premier. Charge : 8,5 JP [ES] (8.2).
> *Pourquoi.* Portefeuille déclaré plus large [DR] ; plancher jamais remisé (ligne 396) ; pas de nouveau prix sans référence (ligne 130).
> *Limite.* JP estimées ; le plafond peut être atteint dès le premier entretien ; hors des priorités, le livrable 3 est moins détaillé. JP réelles relevées et comparées à 8,5 (écart toléré ≤ 25 %, ligne 171) ; dépassement suivi comme risque R60. Si les associés choisissent l'option B, l'écart à signaler est celui de l'encadré n° 2 de la proposition du 9 nov. (lignes 236-241), plus le prix.
> *Décision.* D51, par écrit des deux associés (`annexes/travaux/strategie-retenue.md:614`), puis D46, avant le jeu. 19 nov. 2026.

---

## 9. Effet sur les livrables (fichiers non modifiés)

| Fichier | Ce qu'il faut lire autrement | Gravité |
| --- | --- | --- |
| `README.md` | Ne référence ni cette note ni la proposition du 9 nov. ; une ligne à ajouter quand Morgan l'autorise (D55) | Moyenne |
| `interne/01-synthese-direction.md` | Verdict et chiffres inchangés. Ne renvoie pas à cette note : un associé qui lit 01 seul ignore que la présentation ne doit pas partir. Ajouter l'administratrice et les bâtiments aux points bloqués | Moyenne |
| `interne/02-etat-des-sources.md` | Inconnues U51 à U62 ; nouvelle pièce (PIA) ; toujours aucune parole directe de GianLuca | Moyenne |
| `interne/03-cartographie-projets.md` | Scénario « plusieurs entités » plus probable [HY] ; nouveaux chantiers ; « aucun lieu établi » reste vrai | Élevée |
| `interne/04-catalogue-offres.md` | C6 à adapter (D50) ; C4 et C7 plus pertinents ; cadrage à 8,5 JP sous plafond écrit (section 8) ; prix inchangés avec l'option A | Moyenne |
| `interne/05-proposition-de-valeur.md` | La comparaison avec un salarié devient réelle : l'option hybride devient le cas de base [HY] | Élevée |
| `interne/06-fonctionnement-a-deux.md` | Capacité inchangée, demande en hausse : seuils de saturation à suivre dès le cadrage | Moyenne |
| `interne/07-processus-ia-et-essais.md` | Pilote P1 mesuré sur l'administratrice ; préalables pour sa messagerie | Moyenne |
| `interne/08-feuille-de-route.md` | Dates inchangées ; jalon à ajouter : son identité et ses pouvoirs connus au rendez-vous | Faible |
| `interne/09-modele-economique-tresorerie.md` | Aucun paramètre ne change : 1,5 M€ n'est pas un encaissement | Faible |
| `interne/10-structures-et-relations.md` | Rôle de bailleur plus plausible ; subordination de fait par les consignes quotidiennes de l'administratrice (L8221-6 II ; `annexes/travaux/syn-droit.md:336-337`) à poser à l'avocat [HY] ; parade : priorités en comité et en point hebdomadaire (`annexes/travaux/strategie-retenue.md:576, 256`) | Moyenne |
| `interne/11-proposition-commerciale-revisee.md` | Objection « j'ai déjà une administratrice » ; PIA à ajouter à l'inventaire des pièces (section 6) ; prix à revoir seulement avec l'option B | Élevée |
| `interne/12-gouvernance-contrat-sortie.md` | Déléguée et valideuse probables, si pouvoirs écrits ; personne désignée de C6 identifiée, si elle est salariée de l'entité | Moyenne |
| `interne/13-preparation-rendez-vous.md` | Question 4 en partie répondue [DR] : la recentrer sur son rôle et ses pouvoirs ; ajouter bâtiments, commerces, cabaret ; « il préfère recruter » devient « il aurait recruté » [DR] | Élevée |
| `interne/14-registre-risques-inconnues-decisions.md` | Ajouter R53 à R60, U51 à U62, D45 à D55 (D53) | Moyenne |
| `interne/15-contre-analyse.md` | R1 et R10 renforcés (lignes 81, 90) ; voie 4a en partie réalisée [DR] (ligne 303) | Élevée |
| `pour-gianluca/proposition-de-cadrage.md` (4 nov.) | Section 1 dépassée ; voie (c) à écrire pour l'administratrice ; ses huit livrables servent de base à l'option A (section 8) | Élevée |
| `pour-gianluca/2026-11-09-proposition-de-cadrage.md` | Relue pour cette version. Elle décrit l'option B. Avec l'option A, elle est « à reprendre » dans une nouvelle version datée (sections 2, 3, 6 et note interne). Son encadré n° 1 recommande d'accepter ≈ 250 € HT sous le plancher : non retenu. Elle cite les lignes « 78-82 » et « 292 » de l'ancienne version de cette note | Élevée |
| `pour-gianluca/message-de-recadrage.md` | Question 3 à réécrire pour l'administratrice ; le reste tient | Moyenne |

---

## 10. Nouvelles décisions (à la suite de D44)

**Ordre et dépendances.** Ces onze décisions s'ajoutent aux onze du registre dues au plus tard le 19 nov. (D05 à D14 et D20, `interne/14-registre-risques-inconnues-decisions.md:273-288`). Elles sont classées par date limite. Tout ce qui part chez GianLuca attend **D03** (décision de notifier ou non la CNIL, due le 5 nov., état [IN]) et **D08** (information des personnes concernées et texte d'information de GianLuca, au plus tard le 19 nov.), ainsi que l'accord écrit des deux associés.

| N° | Décision [PR, cette note] | Responsable | Date limite | Attend |
| --- | --- | --- | --- | --- |
| D52 | Aucune production pour un bâtiment, un commerce ou le cabaret sans mandat ni commanditaire nommé, études et visuels compris (prolonge D05) | Les deux | Immédiate | — |
| D45 | (1) Ne pas envoyer ni montrer la présentation ; garder le lien privé ; établir qui l'a vue (U61). (2) Décider si une version corrigée et réduite sert de support au rendez-vous : notes de l'orateur relues avec le tableau 7.3 ou vidées avant tout partage | Morgan, validé par Mathys | (1) Ven. 13 nov. 2026 ; (2) pas avant D08, donc au plus tôt le jeu. 19 nov. | (2) : D03, D08 ; accord écrit des deux associés |
| D53 | Inscrire au registre R53 à R60, U51 à U62 et D45 à D55 | Morgan tient ; Mathys contrôle | Lun. 16 nov. 2026 | — |
| D55 | Autoriser l'ajout au README d'une ligne pour cette note et pour la proposition du 9 nov. | Morgan | Lun. 16 nov. 2026 | — |
| D51 | Choisir par écrit l'option du cadrage (section 8). Option A (recommandée) : 6 500 € HT ; 8,5 JP [ES] tenus seulement sous plafond écrit (trois entités, douze éléments en fiche courte, quinze pièces) ; au-delà, l'élément en remplace un autre ou fait l'objet d'une proposition séparée ; livrables 3 et 4 gardés (encadré de 8.3) ; JP réelles relevées. Option B : prix d'au moins 750 € × JP recalculées, ou périmètre resserré à 8,5 JP au plus | Morgan et Mathys, par écrit | Jeu. 19 nov. 2026 | — ; préalable de D46 |
| D46 | Une seule description du cadrage : celle de l'option choisie en D51. Avec A, une nouvelle version datée de la proposition (celle du 9 nov. marquée « à reprendre ») ; la présentation la reprend après correction. Les versions du 4 et du 9 nov. restent intactes | Morgan ; contrôle par Mathys | Jeu. 19 nov. 2026 pour le texte ; envoi avec D14 | D51 ; envoi : D03, D08 |
| D47 | Réponse écrite à « tout gérer avec l'IA » : non, ni aujourd'hui ni dans un an ; une voie, deux projets actifs, un processus en essai à la fois ; rien d'automatique vers l'extérieur ; plafond de 10 JP confirmé | Morgan et Mathys | Jeu. 19 nov. 2026, avec D13 | — |
| D50 | Adapter le contenu de C6 (encadré de la section 2) | Morgan et Mathys | Jeu. 19 nov. 2026 | U52 pour le client de C6 |
| D48 | Ajouter à l'ordre du jour les questions de la section 3.4 et sur les bâtiments ; demander à GianLuca si l'administratrice assiste au rendez-vous ; aucun contact direct avant | Morgan | Jeu. 19 nov. 2026 ; réponses au plus tard le mar. 15 déc. | Envoi : D03, D08 (avec D14) |
| D49 | Rôle de l'administratrice au contrat : déléguée ou valideuse seulement sur pouvoirs écrits ; jamais d'ordres quotidiens à Marwin (R55) ; Marwin ne la dirige pas ; si elle est prestataire, consignes via son employeur (U62) | Morgan et Mathys, avec l'avocat | Avant le premier bon de commande | U52, U54, U62 |
| D54 | Nommer l'entité et, s'il le souhaite, l'administratrice comme déléguée, avec ses pouvoirs écrits (signature, dépense, données) | GianLuca ou son entité | Mar. 15 déc. 2026, avec D24 | Demande envoyée avec D14 |

---

## Limites

- Les faits 1 à 4 sont des déclarations de Morgan [DR], qu'aucune pièce de GianLuca ou de l'administratrice ne confirme. Ce que GianLuca a vu est [IN].
- Les points [HY] sur la subordination de fait, les consignes à une prestataire, les rôles RGPD et la surveillance d'un salarié sont à soumettre à l'avocat.
- Les charges du cadrage (section 8) et de C6 sont des estimations [ES] ; le choix de l'option du cadrage n'est pas fait (D51).
- Les textes officiels cités ont été ouverts le 9 nov. 2026 ; le barème Sacem du cabaret n'est pas connu [IN].
- Aucune action n'a été faite : ni contact, ni dépense, ni modification de la présentation, des livrables ou d'un outil en service.

## Suite donnée à la relecture contradictoire

- Les 28 constats des deux relecteurs ont été vérifiés dans les sources citées : tous sont fondés et appliqués.
- Ajustements : l'option A compte 8,5 JP et non 8, car c'est le détail de la stratégie (`interne/04-catalogue-offres.md:146-150`) ; entre les deux voies proposées pour une description unique, la note recommande l'option A, la décision restant aux associés (D51) ; la base Sacem des spectacles est précisée d'après F3094 ; pour C6, le prix est gardé et les JP sont estimées, plutôt qu'une baisse de prix.

Relecture contradictoire : 28 constats reçus, 28 appliqués, 0 écartés — 9 novembre 2026
