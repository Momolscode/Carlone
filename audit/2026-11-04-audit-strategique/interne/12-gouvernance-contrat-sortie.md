# Gouvernance, contrat et sortie

Audit Marwin Tech × GianLuca Carlone · livrable 12 sur 15 · 4 novembre 2026
Statut : interne (contient des prix internes, des planchers, des points juridiques non tranchés et la stratégie des associés ; ne pas transmettre à GianLuca Carlone). Les principes des sections 2 à 9 peuvent passer dans un document qui lui est destiné, sous la forme prévue par `travaux/strategie-retenue.md:792` et déjà reprise dans `pour-gianluca/proposition-de-cadrage.md` (section 5).
Sources principales : `travaux/strategie-retenue.md` (sections 4, 5, 7, 8, 10, 11 et 12) ; `travaux/syn-droit.md` (sections 3, 4, 5, 6 et 9) ; `travaux/rj-R3-travail-contrats.md` (sections e à j) et son contrôle `travaux/ver-R3-travail-contrats.md` ; `travaux/syn-capacite-ia.md` (sections 4, 6 et 8) ; pièces d'origine rouvertes en lecture seule dans le dépôt Momolscode/Carlone (commit 7b46602) : `interne/offre-marwin-tech-remuneration-et-collaboration.md`, `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md`, `crm/docs/rapport/rapport-crm-hermes360.md`, `interne/contexte-projet-carlone.md`, `interne/audit-marwin-tech-carlone.md` ; copie du 4 nov. du diaporama client « Offre Marwin Tech pour Carlone » (11 vues, hors dépôt).
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu. Sans autre précision, une [PR] vient de la stratégie retenue ; « [PR, ce livrable] » signale une précision ou une règle ajoutée ici.

Conventions. JP : journée-personne de 7 h. Montants hors taxes (HT) sauf mention. « Jours ouvrés » : du lundi au vendredi, hors jours fériés. Les chemins `slides/…` renvoient à la copie du 4 nov. du diaporama client, hors dépôt. Les codes d'offres (0 remise en ordre, A cadrage, B0 socle pilote, B1 et B2 socles récurrents, C1 à C8 lots, D exploitation, E avenant et urgences) sont ceux de 04-catalogue-offres.md. Les textes officiels cités ont été consultés le 4 nov. 2026 par les chercheurs juridiques de l'audit et contrôlés le même jour ; je ne les ai pas rouverts moi-même. Chaque URL est donnée avec cette date et avec le mémo qui la cite.

**Ce que ce livrable ajoute** : la colonne « qui assume » du tableau des rôles ; la traduction de « s'occuper de tout » en actes ; les plafonds par phase ; les règles de silence, d'urgence et de désaccord ; l'adoption et la définition d'une livraison réussie ; les seize principes contractuels à confier à l'avocat ; les effets d'un impayé, d'un arrêt et d'un désaccord ; la frontière entre remettre et céder ; les étapes de démarrage ; les signaux d'arrêt.
**Ce qu'il ne refait pas** : les fiches d'offres et leurs prix (04-catalogue-offres.md) ; la capacité et les seuils de saturation internes (06-fonctionnement-a-deux.md, section 8) ; la sécurité des agents, les rôles RGPD par phase, la sauvegarde et la restauration (07-processus-ia-et-essais.md, sections 8 à 11) ; le calendrier (08-feuille-de-route.md) ; la trésorerie et les tests d'échec (09-modele-economique-tresorerie.md) ; la SAS, le pacte, les rôles cumulés de GianLuca, la propriété actif par actif et les questions déjà posées aux professionnels (10-structures-et-relations.md, sections 7, 10, 12, 13 et 19) ; le texte commercial (11-proposition-commerciale-revisee.md ; pour-gianluca/proposition-de-cadrage.md).

---

## En bref

1. **Rien n'est signé, et les clauses écrites jusqu'ici se contredisent** [FV]. L'offre du 2 nov. dit qu'un livrable sans réponse est « réputé accepté » (`interne/offre-marwin-tech-remuneration-et-collaboration.md:206`). L'offre du 29 oct. dit qu'« une absence de réponse ne vaut pas approbation » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:103`). La grille de délégation détaillée du 29 oct. (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:94-101`) a été réduite à une ligne le 2 nov. (`interne/offre-marwin-tech-remuneration-et-collaboration.md:208`).
2. **GianLuca décide ; Marwin prépare, organise, coordonne et produit ses livrables ; l'entité de GianLuca signe, commande et paie** [PR] (`travaux/strategie-retenue.md:187-189`). Le tableau de la section 3 dit, pour dix-sept types d'actes, qui propose, autorise, exécute, contrôle, valide et assume.
3. **« S'occuper de tout » ne veut pas dire agir au nom du client.** Sur les quinze demandes relevées dans les archives, Marwin n'agit au nom de l'entité que dans deux cas, toujours plafonnés : des achats courants sous mandat et les urgences. Tout le reste est l'exécution de ses propres livrables, de la coordination ou de la préparation de décisions (section 4) [PR, ce livrable].
4. **Mandat de dépense à 0 € pendant le cadrage et le pilote.** Ensuite seulement, avec un socle récurrent : 500 € HT par acte et 1 500 € HT par mois et par entité, sur une liste fermée. Contrats, recrutements, emprunts, baux et travaux ne sont jamais délégués [PR] (`travaux/strategie-retenue.md:589-591`).
5. **Le silence ne vaut jamais autorisation.** Il ne déclenche qu'une chose : l'exigibilité du solde d'un livrable remis sans réserve motivée, pour la facturation seulement [PR] (`travaux/strategie-retenue.md:603-606`).
6. **Une livraison réussie, c'est trois choses** : livrée selon des critères écrits avant (ce qui déclenche le paiement), réellement utilisée, et dont le résultat est accepté par écrit. Marwin est payée à la livraison ; elle ne compte comme réussite que l'usage et l'acceptation (section 10.6) [PR] (`travaux/strategie-retenue.md:113, 287`).
7. **Seize principes contractuels sont prêts pour l'avocat** (section 11). Deux points s'écartent légèrement de la stratégie : un plancher pour le plafond de responsabilité, et une prudence sur la parade « signature à distance » contre la rétractation.
8. **Remettre n'est pas céder.** Les données, documents, exports, accès et procédures de GianLuca lui sont toujours remis, même en cas d'impayé. Les développements propres lui sont cédés au paiement complet. Les composants génériques de Marwin restent à Marwin, sous licence perpétuelle pour lui (section 13) [PR].
9. **Aujourd'hui, la promesse de réversibilité du diaporama est inexacte** : le CRM est « sous le compte des associés » [FV] (`crm/docs/rapport/rapport-crm-hermes360.md:12, 19` ; `slides/garanties.html:30`).
10. **Sept étapes, chacune avec ses conditions** : proposer, signer, démarrer, recevoir des accès, toucher des données réelles, engager une dépense, automatiser (section 14). Sans la décision sur la fuite de données, aucune ne s'ouvre.

---

## 1. Point de départ au 4 novembre 2026

| Sujet | État | Code et source |
| --- | --- | --- |
| Contrat, facture, entité payeuse | Aucun | [FV négatif] (`interne/audit-marwin-tech-carlone.md:13-14` ; `travaux/strategie-retenue.md:33`) |
| Société qui signerait | Marwin Tech non immatriculée | [DR] (`interne/offre-marwin-tech-remuneration-et-collaboration.md:153`) |
| Parole directe de GianLuca sur ce qu'il veut déléguer | Aucune ; tout vient de Morgan | [FV négatif] (`travaux/syn-sources.md:38`) |
| Besoin rapporté | « développer vos projets sans avoir à en gérer chaque détail » | [DR] (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:13`) |
| Clauses prévues le 2 nov. | Parties, objet, réception « réputé accepté », paiement et suspension, délégation en une ligne, trois registres de droits, données, durée, sortie, indépendance | [PR] (`interne/offre-marwin-tech-remuneration-et-collaboration.md:204-213`) |
| Grille de délégation du 29 oct. | Par catégorie : entité, budget, plafond par acte, plafond cumulé, personne habilitée ; contrats, recrutements, emprunts et investissements réservés au client ; questions réglementées aux professionnels | [PR] (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:94-101`) |
| Promesses du diaporama | « Un sujet, un accord » ; « Réversibilité : fichiers, configurations, documentations et accès remis » ; « Aucun travail facturé deux fois » | [FV] (`slides/cadre.html:4-5` ; `slides/garanties.html:30, 38`) |
| Hébergement du CRM | « sous le compte des associés » ; « le code, les données et le suivi restent chez les associés » | [FV] (`crm/docs/rapport/rapport-crm-hermes360.md:12, 19`) |
| Données | Dépôt public FinanceScope/CRM-Carlone avec des coordonnées de prospects ; connu au plus tard le 2 nov. | [DR] public le 4 nov. (`interne/contexte-projet-carlone.md:5`) ; [FV] date de connaissance (`interne/audit-marwin-tech-carlone.md:3, 15`) |

**Lecture.** Les bonnes idées existent déjà dans les archives, mais en ordre dispersé. Le travail consiste à les remettre dans un seul ensemble cohérent et à trancher les contradictions (`travaux/syn-sources.md:248`).

---

## 2. Principes de gouvernance

| N° | Principe [PR] | Pourquoi | Source |
| --- | --- | --- | --- |
| G1 | **GianLuca décide.** Marwin propose, prépare, organise, coordonne et produit ses propres livrables. Elle ne décide ni n'engage à sa place | La lettre du 29 oct. lui promettait déjà de conserver « la validation des décisions importantes et des engagements financiers » [PR] ; décider à sa place n'est pas plausible [HY] | `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:17` ; `travaux/syn-capacite-ia.md:793` |
| G2 | **Une entité, un signataire, un valideur, un payeur**, nommés dans chaque bon de commande | « Carlone » désigne tantôt la personne, tantôt une entité non identifiée [FV] | `travaux/syn-droit.md:5` ; `travaux/strategie-retenue.md:185` |
| G3 | **Tout pouvoir d'agir au nom du client est écrit, nominatif, plafonné et révocable.** Rien n'est délégué par défaut | Un mandat général ne couvre que les actes d'administration ; au-delà, l'acte est inopposable au client, sauf mandat apparent [FV] | `travaux/rj-R3-travail-contrats.md:306-307` |
| G4 | **Le silence ne vaut jamais autorisation** | Règle du 29 oct., à rétablir contre la clause du 2 nov. [FV] | `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:103` ; `travaux/strategie-retenue.md:604` |
| G5 | **Marwin n'avance jamais d'argent et ne manie pas les fonds du client** | Débours stricts, risques de services de paiement ou de recouvrement [FV/IN] | `travaux/strategie-retenue.md:188` ; `travaux/rj-R3-travail-contrats.md:321-322` |
| G6 | **Les comptes et outils du client sont à son nom dès le premier jour** ; Marwin y intervient comme collaborateur | C'est la condition de la réversibilité et la parade la plus simple au Data Act [PR] | `travaux/strategie-retenue.md:189` ; `travaux/syn-droit.md:512` |
| G7 | **La liste des livrables précède la liste des heures** ; aucun horaire imposé, aucune place dans un organigramme, aucun ordre direct | « S'occuper de tout » est le principal facteur de glissement vers une mise à disposition de personnes [HY] | `travaux/rj-R3-travail-contrats.md:148` ; `travaux/syn-droit.md:338-343` |
| G8 | **Quiconque constate un incident arrête**, sans autorisation préalable ; personne ne dépense pour réparer sans autorisation | Arrêter protège ; dépenser engage | `travaux/strategie-retenue.md:585, 597` |
| G9 | **Un sujet, un accord** : la prestation ne dépend d'aucun autre accord (bureaux, emploi, capital) et n'en crée aucun | Le cumul des rôles expose à la requalification, à la dépendance et au blocage croisé [HY] | `slides/cadre.html:4-5` ; `travaux/strategie-retenue.md:627-633` |
| G10 | **Chaque décision est écrite** dans un registre tenu sur un compte de l'entité, avec responsable, date et source ; une décision orale est confirmée par écrit | La décision du 4 nov. n'a été appliquée qu'à 1 support sur au moins 5 [FV] | `travaux/strategie-retenue.md:225` ; `travaux/syn-capacite-ia.md:699` |

---

## 3. Qui propose, autorise, exécute, contrôle, valide et assume

Le tableau reprend `travaux/strategie-retenue.md:574-585` et y ajoute la colonne « assume » et sept types d'actes [PR, ce livrable]. « Délégué » désigne la personne nommée par écrit par l'entité ; « valideur », celle qui réceptionne les livrables. Le valideur ne peut pas être un associé de Marwin salarié chez GianLuca (`travaux/strategie-retenue.md:629`).

| N° | Acte | Propose | Autorise | Exécute | Contrôle | Valide le résultat | Assume la responsabilité |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | Priorités du mois ; arbitrage entre projets | Marwin (Morgan) | GianLuca ou son délégué écrit, en comité mensuel | Marwin | Mathys (capacité, limite d'encours) | GianLuca | GianLuca pour le choix ; Marwin pour la qualité du dossier (obligation de moyens) |
| R2 | Changement de priorité entre deux comités | GianLuca, son délégué ou Marwin | Délégué, par écrit | Marwin | Mathys : la demande remplace un projet actif ou devient un lot | GianLuca, au comité suivant | GianLuca pour les reports qui en découlent |
| R3 | Commande d'une prestation de Marwin (cadrage, socle, lot, avenant) | Marwin (devis écrit) | Signataire habilité de l'entité concernée | L'associé responsable | L'autre associé (quatre yeux, au plus 2 jours ouvrés) | Valideur nommé | L'entité pour le paiement et ses dépendances ; Marwin pour l'exécution du bon |
| R4 | Livrable ou document envoyé au client | L'auteur | — | L'auteur | L'autre associé, avec le registre « décision → documents touchés » | Morgan, ou Mathys par délégation écrite | Marwin : résultat sur un livrable précis et réceptionné ; moyens pour le pilotage et les sorties d'IA |
| R5 | Réception d'un livrable | Marwin remet | — | Le valideur examine | Critères écrits avant le démarrage | Le valideur, par écrit ; réserves motivées sous 10 jours ouvrés | Le valideur pour sa décision ; le silence ne joue que sur l'exigibilité du solde |
| R6 | Dépense pour un projet, dans le mandat (socle récurrent seulement) | Marwin (devis comparés) | GianLuca, par écrit, selon les plafonds | **L'entité** paie ; Marwin peut passer la commande en son nom si l'acte est sur la liste | Marwin tient le registre des engagements | Expert-comptable de l'entité | L'entité pour la dépense ; Marwin pour le respect du mandat (fautes de gestion) |
| R7 | Engagement récurrent (abonnement, location) | Marwin | GianLuca, par écrit, toujours au-delà de 50 € par mois ou de 3 mois | L'entité | Registre des engagements | GianLuca | L'entité |
| R8 | Contrat, recrutement, emprunt, investissement, bail, travaux | Marwin prépare le dossier | **Réservé à GianLuca** ou au signataire habilité | L'entité | Ses conseils | GianLuca | GianLuca et son entité |
| R9 | Question fiscale, juridique, comptable ou d'exploitation | Marwin prépare le dossier factuel et les questions | — | Le professionnel compétent | — | Le professionnel, puis GianLuca | Le professionnel dans sa mission, puis GianLuca |
| R10 | Message à un tiers au nom du client (prospect, administration, artiste) | Marwin rédige | Délégué, message par message | L'entité, sous son nom | — | — | L'entité, expéditrice ; Marwin pour les erreurs de rédaction |
| R11 | Consigne à un prestataire du client (Quali Contact, artisans, traiteur) | Marwin prépare | Délégué | **Via l'employeur du prestataire**, jamais en direct à ses salariés | Marwin note la consigne au registre | Délégué | L'entité (son contrat) ; l'employeur du prestataire (ses salariés) |
| R12 | Ouverture d'un compte ou d'un outil | Mathys | Délégué ; GianLuca si la règle R7 s'applique | L'entité, à son nom ; Marwin invitée comme collaboratrice | Mathys (inventaire des comptes) | Délégué | L'entité, titulaire et payeuse ; Marwin pour la configuration |
| R13 | Traitement de données personnelles réelles ; automatisation | Mathys, après essai | Le responsable du traitement, par écrit, après les préalables RGPD | Mathys | Morgan et le journal | Délégué, sur critères | L'entité, responsable du traitement, pour la licéité ; Marwin, sous-traitante, pour la sécurité et le respect des instructions [HY sur les rôles] |
| R14 | Urgence de la liste fermée (section 6) | Celui qui la constate | Aucune autorisation pour **arrêter** ; mesure conservatoire au plus 300 € HT si le mandat la prévoit | Mathys (mesures techniques) | Morgan et le journal | Délégué, a posteriori, informé sous 24 h | Marwin pour la mesure prise ; l'entité pour la dépense conservatoire |
| R15 | Incident (données, envoi erroné, action non autorisée) | Quiconque le constate **arrête** | Aucune autorisation pour arrêter | Mathys | Avocat ou DPD si nécessaire | Morgan (ou Mathys en son absence [PR, ce livrable]) informe GianLuca par écrit sous 24 h | Le responsable du traitement pour les notifications ; Marwin pour l'information sans délai et les mesures techniques |
| R16 | Sous-traitance d'une partie d'un lot par Marwin | L'associé responsable | Les deux associés (unanimité) **et** l'entité, par écrit, avant | Le sous-traitant, sous l'autorité de son propre employeur | L'associé responsable | Valideur, sur le livrable de Marwin | Marwin envers le client ; le sous-traitant envers Marwin |
| R17 | Décision interne à Marwin : contrat avec GianLuca, prix, remise, engagement de plus de 1 000 € HT, recrutement, sous-traitance | L'un des associés | Les deux, à l'unanimité | — | — | — | Marwin et ses deux associés |

**Sources des lignes.** R1, R3, R4, R6, R8, R9, R10, R11, R13, R15 : `travaux/strategie-retenue.md:576-585`. R2 : `travaux/strategie-retenue.md:283, 613`. R5 : `travaux/strategie-retenue.md:235, 604, 612`. R7 : `travaux/strategie-retenue.md:591`. R12 : `travaux/strategie-retenue.md:189` [PR, ce livrable pour la répartition]. R14 : `travaux/strategie-retenue.md:597`. R16 : `travaux/strategie-retenue.md:614` et `travaux/syn-droit.md:360-362, 388` [PR, ce livrable pour l'accord de l'entité]. R17 : `travaux/strategie-retenue.md:592, 614`. Responsabilité du mandataire : il « répond […] des fautes qu'il commet dans sa gestion » (art. 1992 C. civ.) ; l'acte « accompli par un représentant sans pouvoir ou au-delà de ses pouvoirs est inopposable au représenté » (art. 1156 C. civ.) [FV] (https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070721/LEGISCTA000006118139/ et https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070721/LEGISCTA000032008382/, consultés le 4 nov. 2026 ; `travaux/rj-R3-travail-contrats.md:327, 329`).

**Deux règles qui découlent du tableau.**
- **Marwin ne se commande jamais à elle-même une prestation au nom du client.** Un avenant, un lot ou un socle de Marwin est toujours signé par le signataire de l'entité, jamais passé sous le mandat de dépense. Pour une personne physique représentée, un tel acte serait nul sauf autorisation ou ratification (art. 1161 C. civ.) [FV] (`travaux/rj-R3-travail-contrats.md:308`).
- **Seules comptent les instructions des personnes nommées au bon de commande** (signataire, valideur, délégué). Si deux d'entre elles se contredisent, le travail sur ce point s'arrête et la question part par écrit à GianLuca. La consigne la plus récente n'est pas prise pour une décision [PR, ce livrable] (même règle que `travaux/DEMANDE.md:13` pour les documents).

---

## 4. « S'occuper de tout », traduit en actes

### 4.1 D'où vient la formule

Morgan l'emploie dans sa demande (`travaux/DEMANDE.md:46`). Les archives la déclinent en trois volets, « Cadrer », « Produire », « Piloter », dont le dernier comprend le « suivi centralisé des établissements (encaissements, dépenses, trésorerie, factures) », la « gestion administrative déléguée », la « coordination des prestataires locaux », les « séjours des invités » et les « événements » [PR] (`interne/offre-marwin-tech-remuneration-et-collaboration.md:9, 52`). Plusieurs de ces actes touchent des activités réservées ; un agent d'IA qui les ferait les ferait exercer par Marwin [HY fondée sur des textes FV] (`travaux/rj-R3-travail-contrats.md:349-358, 363`).

### 4.2 Ce que Marwin fait, et ce qu'elle ne fait pas

Quatre natures d'acte : **exécution** (Marwin produit elle-même) ; **coordination** (Marwin organise le travail d'autres personnes, sans les commander) ; **préparation de décision** (Marwin instruit, GianLuca tranche) ; **pouvoir délégué** (Marwin agit au nom de l'entité, dans un mandat écrit).

| Demande des archives | Ce que fait Marwin | Nature | Ce qu'elle ne fait pas | Qui fait le reste | Source |
| --- | --- | --- | --- | --- | --- |
| Relier les sujets, organiser les priorités | Registre des décisions et des échéances ; tableau de bord ; comité mensuel ; 2 à 4 dossiers de décision par mois | Exécution (socle) et préparation | Décider | GianLuca | `travaux/strategie-retenue.md:255-264` |
| Suivi des établissements : encaissements, dépenses, trésorerie, factures | Tableau de bord de gestion à partir des données du client ; suivi budgétaire préparatoire remis à son expert-comptable ; calculs par formule, jamais par le modèle de langage | Préparation | Saisir, tenir, réviser les comptes ; faire la paie | Expert-comptable du client | `travaux/rj-R3-travail-contrats.md:351` ; `travaux/syn-capacite-ia.md:323` |
| Gestion administrative déléguée | Dossiers pour les professionnels ; procédures et outils remis à une personne du client (C6) | Préparation ; passation | Exécuter les factures, démarches et relances courantes | Personne désignée ou recrutée par GianLuca | `travaux/strategie-retenue.md:249, 650` |
| Coordination des prestataires locaux | Planning, comparatif de devis, relances préparées, comptes rendus | Coordination sous mandat | Commander les salariés d'un prestataire ; signer pour le client | L'entité signe ; consignes via l'employeur | `travaux/syn-capacite-ia.md:557, 562` ; `travaux/syn-droit.md:356-362` |
| Achats courants d'un projet | Comparer, préparer ; avec un socle et un mandat, commander au nom de l'entité dans la liste fermée | Préparation ; **pouvoir délégué plafonné** | Avancer l'argent ; payer ; acheter à son propre nom | L'entité paie | `travaux/strategie-retenue.md:188, 590` |
| Contrats, recrutements, emprunts, baux, travaux, investissements | Dossier de décision, comparaison chiffrée | Préparation | Négocier ou signer au nom du client | GianLuca ou le signataire | `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:100` |
| Séjours des invités | Liste des besoins, comparatif | Préparation | Réserver, vendre ou encaisser un séjour (code du tourisme, art. L211-1) | L'entité réserve et paie | `travaux/rj-R3-travail-contrats.md:355` |
| Événements | Faisabilité (C3), calendrier des autorisations | Préparation ; coordination | Être organisateur ou exploitant ; répondre de la sécurité du public | L'entité organisatrice | `travaux/strategie-retenue.md:293, 647` |
| Relances d'impayés des établissements | Modèles de relance | Préparation | Recouvrer ou encaisser pour le client (CPCE, art. R124-2) | L'entité signe et encaisse | `travaux/rj-R3-travail-contrats.md:356` |
| Vente d'œuvres | Préparation de 20 comptes, kit, outil de réimport (C2) | Exécution (lot) | Appeler, vendre, encaisser, garder ; toucher une commission | Appelant désigné ; entité vendeuse | `travaux/strategie-retenue.md:310, 649` |
| Questions fiscales et juridiques | Dossier factuel et questions, chaque règle avec sa source officielle datée | Préparation | Donner un conseil ou rédiger un acte pour autrui (loi n° 71-1130, art. 54) | Avocat, expert-comptable | `travaux/syn-capacite-ia.md:581-582` |
| CRM, catalogue, outils | Lots devisés, sur des comptes du client | Exécution (lots) | Héberger chez les associés | — | `travaux/strategie-retenue.md:287` |
| Messages au nom du client | Rédaction | Préparation | Envoyer sans autorisation, message par message | L'entité envoie | `travaux/strategie-retenue.md:583` |
| Urgences | Arrêter ; mesure conservatoire plafonnée si le mandat la prévoit | **Pouvoir délégué plafonné** | Astreinte 24 h sur 24 | — | `travaux/strategie-retenue.md:597, 651` |
| Automatisations | Essais, puis exploitation d'un processus prouvé (D) | Exécution | Agents qui envoient, achètent, publient ou modifient sans approbation humaine | — | `travaux/syn-capacite-ia.md:792` ; `travaux/syn-droit.md:690` |

### 4.3 Pouvoirs effectivement délégués, par phase

| Phase | Exécution | Coordination | Préparation de décisions | Pouvoir d'agir au nom de l'entité |
| --- | --- | --- | --- | --- |
| **Cadrage (A)** | Dossier du cadrage | Aucune : tout contact avec des tiers est exclu | Trois priorités, grille de délégation, projet de mandat | **Aucun** |
| **Pilote (B0, C2 ou C6)** | Socle pilote ou lot | Prestataires, sans dépense | 2 à 4 dossiers par mois | **Aucun** : mandat à 0 € ; messages au nom de l'entité autorisés un par un |
| **Lots C** | Le livrable du lot | Selon le bon de commande | Selon le lot | Aucun, sauf mention expresse au bon de commande |
| **Socle récurrent (B1, B2)** | Socle | Oui, sous mandat | Oui | Mandat écrit par entité : liste fermée, 500 € HT par acte, 1 500 € HT par mois ; mesure conservatoire de 300 € HT au plus |
| **Exploitation (D)** | Processus prouvé | — | — | Actions classées : envoyer, appeler, modifier le CRM, publier ou dépenser demandent une approbation humaine |

Sources : `travaux/strategie-retenue.md:227, 271, 589-590, 597` ; `travaux/syn-capacite-ia.md:321`.

---

## 5. Plafonds et engagements

### 5.1 Dépenses par acte et cumulées

| Situation | Par acte | Cumul | Conditions | Source |
| --- | --- | --- | --- | --- |
| Cadrage et pilote | 0 € | 0 € | Marwin prépare et compare ; l'entité commande et paie | `travaux/strategie-retenue.md:589` |
| Socle récurrent | 500 € HT | 1 500 € HT par mois **et par entité** | Liste fermée d'actes ; budget du projet déjà approuvé ; facture au nom de l'entité et payée par elle ; registre des engagements | `travaux/strategie-retenue.md:590` |
| Urgence, avec socle | 300 € HT | Compté dans les 1 500 € HT du mois [PR, ce livrable] | Prévue au mandat ; information écrite sous 24 h | `travaux/strategie-retenue.md:597` |
| Au-delà de tout plafond | — | — | Accord écrit préalable de GianLuca | `interne/offre-marwin-tech-remuneration-et-collaboration.md:208` |

**La liste fermée se fixe au cadrage**, entité par entité (livrable 4 du cadrage : « grille de délégation et projet de mandat par entité ») (`travaux/strategie-retenue.md:225`). Exemples d'actes qui pourraient y figurer [PR, ce livrable, à valider avec GianLuca] : impression de supports déjà validés ; fournitures d'un événement déjà budgété ; frais d'envoi ; achat d'un document ou d'un extrait de registre payant. N'y figurent jamais : un abonnement, une location, un acompte à un prestataire, un achat d'œuvre ou de matériel, une dépense qui crée un engagement au-delà du mois.

**Forme du mandat.** Un mandat écrit et distinct par entité, signé par son représentant légal, qui liste les actes autorisés, car un mandat général ne couvre que les actes d'administration (art. 1988 C. civ.) [FV] ; le mandataire rend compte chaque mois (art. 1993 C. civ.) par le registre des engagements rapproché du budget [PR] (`travaux/rj-R3-travail-contrats.md:306-307, 313-319`). Pas d'identifiants bancaires du client partagés ; au plus des accès nominatifs en lecture ou avec validation par le client (`travaux/rj-R3-travail-contrats.md:320`).

### 5.2 Engagements récurrents

Tout abonnement ou location de plus de 50 € par mois, ou de plus de trois mois, demande un accord écrit préalable de GianLuca, quel que soit le montant mensuel restant sous le plafond [PR] (`travaux/strategie-retenue.md:591`). Les abonnements sont ouverts au nom de l'entité et payés par elle (règle G6). L'inventaire des comptes et abonnements fait partie de la réversibilité (section 13).

### 5.3 Contrats et recrutements

**Jamais délégués** : contrats, recrutements, emprunts, investissements, baux, travaux [PR] (`travaux/strategie-retenue.md:580, 591`). Pour un recrutement chez le client (offre C6), Marwin fournit une fiche de poste et une grille d'entretien ; elle ne sélectionne pas, ne signe pas de contrat de travail et n'utilise **aucun outil d'IA dans le recrutement**, classé à haut risque par le règlement européen sur l'IA [PR] (`travaux/strategie-retenue.md:329` ; `travaux/syn-droit.md:665`).

### 5.4 Plafonds internes à Marwin

Toute dépense de plus de 300 € HT, ou tout abonnement : accord des deux associés. Plus de 1 000 € HT ou plus de trois mois : décision du pacte à l'unanimité [PR] (`travaux/strategie-retenue.md:592`). Aucune caution personnelle d'un associé pour un engagement de Marwin sans accord écrit des deux (10-structures-et-relations.md, section 10.5).

### 5.5 La capacité est aussi un plafond

Au-delà de 90 % des JP réservées avant le 20 du mois, les travaux non urgents s'arrêtent ; au-delà de 100 %, avenant écrit ou report, jamais de travail gratuit [PR] (`travaux/strategie-retenue.md:593` ; `travaux/syn-capacite-ia.md:298`). La capacité non consommée du socle se reporte d'au plus 20 %, pour du pilotage seulement ; elle ne se convertit jamais en production (`travaux/strategie-retenue.md:283`). Le plafond interne de 10 JP facturables par mois la première année ne figure pas au contrat ; le contrat montre des paliers de périmètre (`travaux/strategie-retenue.md:43, 787`).

---

## 6. Urgences

**Définition, liste fermée** [PR] (`travaux/strategie-retenue.md:597`) : (1) incident de données ou de sécurité ; (2) échéance légale à moins de 48 h. **Ne sont pas des urgences** [PR, ce livrable] : un événement à préparer, une opportunité de vente, une demande tardive, un retard du client à fournir une pièce.

| Ce que Marwin peut faire | Sans autorisation | Avec le mandat d'un socle récurrent | Jamais |
| --- | --- | --- | --- |
| Arrêter : couper un accès, suspendre un automatisme, révoquer un jeton | Oui ; ni facturé ni soumis à accord | Oui | — |
| Mesure conservatoire payante | Non | Au plus 300 € HT, payée par l'entité, information écrite sous 24 h | Au-delà de 300 € HT |
| Travail en plus | Non | Sur bon écrit du valideur **avant** le travail (avenant E) | Absorbé gratuitement |
| Présence hors heures ouvrées | Non | Seulement avec un forfait d'astreinte séparé, relais nommés | 24 h sur 24 ou 30 jours sur 30 |

**Disponibilité.** Le contrat distingue le délai d'accusé de réception, le début de traitement et la résolution (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:105`). Les valeurs sont fixées au bon de commande pour les heures ouvrées ; aucune n'est promise hors de ces heures [PR, ce livrable]. Présentation au client : « Intervention urgente de la liste fermée : par demi-journée, 450 € HT » ; le prix de 900 € HT par JP reste la base interne (04-catalogue-offres.md, section 3.6, écart).
**Urgences multiples.** Deux urgences dans le même mois : avenant ou report, aucune absorption gratuite. Plus de deux urgences hors plages dans le mois : forfait d'astreinte chiffré ou refus [PR] (`travaux/strategie-retenue.md:534` ; `travaux/syn-capacite-ia.md:300`).
**Associé indisponible.** Au-delà de 10 jours ouvrés d'absence, changement de palier sans pénalité et lots reportés ; l'autre associé tient le socle avec les procédures testées [PR] (`travaux/strategie-retenue.md:281, 533`).

---

## 7. Arbitrages entre projets et changements de priorité

1. **GianLuca arbitre**, en comité mensuel ; entre deux comités, son délégué par écrit [PR] (`travaux/strategie-retenue.md:613`).
2. **Limite d'encours** : le socle couvre un nombre nommé de projets actifs. Une demande nouvelle remplace un projet actif ou devient un lot devisé [PR] (`travaux/strategie-retenue.md:283`).
3. **Capacité répartie par entité**, pour qu'aucune entité ne consomme le temps payé par une autre (`travaux/strategie-retenue.md:268`).
4. **Trop de tâches en attente** (plus de 1,5 fois la capacité restante du mois, ou plus de 10 tâches en attente depuis plus de 10 jours ouvrés) : GianLuca choisit ce qui sort du mois ; les sorties sont consignées [PR] (`travaux/syn-capacite-ia.md:291`).
5. **Changement de priorité sur un lot en cours** : avenant, ou arrêt du lot avec paiement du travail fait (section 12.2) ; jamais absorbé [PR, ce livrable, conforme à `travaux/strategie-retenue.md:391, 465`].
6. **Indicateurs séparés** : ce que Marwin contrôle (qualité, délais) est suivi à part de ce qui dépend de GianLuca (ventes, rendez-vous, décisions prises) (`travaux/strategie-retenue.md:159`).

---

## 8. Quand GianLuca ne répond pas

**Règle** : l'engagement attend [PR] (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:103` ; `travaux/strategie-retenue.md:603`).

| Situation | Effet | Ce que le silence n'autorise jamais |
| --- | --- | --- |
| Demande de décision ou d'autorisation | Relance à 5 jours ouvrés ; à 10 jours, jalons reportés, consignés, capacité réaffectée ; à 15 jours, revue du contrat (réduction de palier) | Dépenser, engager, signer, envoyer au nom du client, étendre le périmètre |
| Livrable remis sans réserve motivée sous 10 jours ouvrés | Solde exigible au plus tard 30 jours après la remise, **pour la facturation seulement** | Valoir approbation d'une suite, d'une dépense ou d'un usage |
| Socle arrivé à échéance | Pas de tacite reconduction ; renouvellement par accord écrit | Prolonger le travail sans bon de commande |
| GianLuca injoignable | Seuls les travaux déjà autorisés continuent | Toute dépense, même sous le plafond, si l'acte n'est pas déjà autorisé |
| Délégué absent ou non nommé | Pas de pilote B0 sans délégué ; les décisions remontent à GianLuca | Transformer Marwin en délégué de fait |
| Accès non fournis 10 jours ouvrés après le démarrage | Signal de suspension (section 15) | Travailler sur des comptes personnels pour avancer |
| Personne désignée absente 15 jours ouvrés après la livraison (C2, C6) | La livraison est prononcée ; la mesure d'usage devient un lot optionnel | Que Marwin reprenne l'exécution |

Sources : `travaux/strategie-retenue.md:272, 318, 336-337, 603-606, 676` ; `travaux/syn-capacite-ia.md:293`.

La clause « réputé accepté » de l'offre du 2 nov. (`interne/offre-marwin-tech-remuneration-et-collaboration.md:206`) est **retirée** [PR] (`travaux/strategie-retenue.md:604`).

---

## 9. Désaccords

| Désaccord | Règle | Source |
| --- | --- | --- |
| **Sur un livrable** | Réserves motivées sous 10 jours ouvrés ; un cycle de correction compris ; arbitrage en comité ; puis avenant, ou arrêt du lot avec avoir. Détail en section 12.3 | `travaux/strategie-retenue.md:612` |
| **Entre deux projets du client** | GianLuca arbitre ; la limite d'encours s'applique toujours | `travaux/strategie-retenue.md:613` |
| **Entre personnes du client** (GianLuca, délégué, responsable d'un lieu) | Seules comptent les personnes nommées au bon de commande ; en cas de contradiction, arrêt sur le point et question écrite à GianLuca | [PR, ce livrable] |
| **Entre le client et ses prestataires** (Quali Contact, artisans) | Marwin n'arbitre pas : elle consigne les faits et prépare les options ; GianLuca décide ; aucun ordre direct aux salariés du prestataire | `travaux/strategie-retenue.md:584` ; `travaux/rj-R3-travail-contrats.md:147` |
| **Entre Marwin et un professionnel du client** (expert-comptable, avocat) | L'avis du professionnel prévaut dans son domaine ; Marwin signale par écrit à GianLuca un fait qui lui paraît contradictoire | [PR, ce livrable] ; `travaux/strategie-retenue.md:581` |
| **Entre associés, sur un document** (contrôle à quatre yeux) | Technique et données : Mathys, par délégation écrite de la validation technique ; relation et formulation au client : Morgan ; prix et remises : unanimité. Sans accord, le document ne part pas et le client est prévenu du délai | `travaux/strategie-retenue.md:614, 619` ; [PR, ce livrable] pour la dernière phrase |
| **Entre associés, sur une décision** | Liste des décisions prises à l'unanimité au pacte (contrat avec GianLuca, prix et remises, engagement de plus de 1 000 € HT, entrée d'un associé, recrutement, sous-traitance). Tant que le désaccord dure, **rien n'est proposé au client**. Puis médiation, tiers expert, offre alternative | `travaux/strategie-retenue.md:614` ; 10-structures-et-relations.md, section 12 |
| **Avec Medhi ou un tiers** | Aucune action au nom de Marwin sans décision écrite des deux associés | `travaux/strategie-retenue.md:615` |

Le lieu où un désaccord entre associés est écrit, et non tranché en silence, est la revue mensuelle (06-fonctionnement-a-deux.md, section 10.1).

---

## 10. Adoption par les équipes, et ce qu'est une livraison réussie

### 10.1 Personnes concernées

Aucune pièce ne nomme les collaborateurs de GianLuca ni son canal de travail [IN] (`travaux/juge-J1-client.md:190`). Le cadrage doit les établir (livrable 6 : « Canal de travail réel de GianLuca et personnes qui utiliseront les outils ») (`travaux/strategie-retenue.md:225`).

| Personne ou groupe | Ce qu'on attend d'elle | Ce qu'on sait | À fixer au cadrage |
| --- | --- | --- | --- |
| **GianLuca Carlone** | Choisir trois priorités ; décider dans les délais ; lire les comptes rendus ou les faire lire | Veut « ne pas gérer chaque détail » [DR] ; aucune parole directe [FV négatif] | Canal préféré ; délai de réponse acceptable ; ce qu'il veut voir et ce qu'il délègue |
| **Délégué et valideur** | Autoriser, réceptionner, réagir aux comptes rendus | [IN] : existence et identité | Nom, pouvoir écrit, disponibilité ; distinct d'un associé salarié chez lui |
| **Personne désignée ou recrutée** (C6) | Exécuter le quotidien avec les outils remis | [IN] : existe-t-elle ? | Décision de désigner ou de recruter ; temps disponible |
| **Appelant** (C2) : GianLuca, un assistant ou Quali Contact | Utiliser les fiches ; renvoyer les résultats d'appel | [IN] ; GianLuca « prévoit d'engager » Quali Contact [DR] ; outil de Quali Contact inconnu [IN] | Qui appelle ; contrat avec Quali Contact ; format d'échange |
| **Exploitants et responsables des lieux** | Fournir les informations des lieux (C4) | [IN] | Liste des lieux et de leurs exploitants |
| **Expert-comptable et avocat du client** | Recevoir les dossiers ; valider les mentions fiscales | [IN] | Noms et canal |
| **Prestataires** (artisans, traiteur, techniciens) | Livrer à temps, sous la coordination de Marwin | [IN] | Liste, contrats en cours |
| **Morgan et Mathys** | Utiliser eux-mêmes la recherche documentaire et le registre interne | Adoption interne mesurable (P3) | — |

Sources : `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:13` ; `travaux/syn-sources.md:38` ; `travaux/syn-capacite-ia.md:280, 738` ; `travaux/rj-R3-travail-contrats.md:55`.

### 10.2 Résistances prévisibles et réponses

Toutes ces résistances sont des hypothèses [HY] : aucune pièce ne décrit les équipes du client.

| Résistance | Signe | Réponse prévue | Source |
| --- | --- | --- | --- |
| GianLuca ne travaille pas à l'écrit | Comptes rendus non lus ; décisions données au téléphone | Mesurer l'adoption dans le canal qu'il emploie déjà ; un message court qui confirme chaque décision orale ; registre non consulté 4 semaines : abandon du processus | `travaux/juge-J1-client.md:190` ; `travaux/strategie-retenue.md:281` |
| Délégation sans délégué réel | Personne n'a le pouvoir de dire oui | Pas de pilote B0 sans délégué ; règle du silence | `travaux/strategie-retenue.md:272` |
| Outil perçu comme un contrôle des personnes | Refus de renseigner le registre | Le registre suit des décisions et des échéances, jamais la performance d'une personne ; aucun outil de notation de personnes | `travaux/strategie-retenue.md:652` |
| Refus d'enregistrer ou de prendre des notes | Participant qui refuse | Accord préalable sur la prise de notes ; notes manuelles sinon | `travaux/syn-capacite-ia.md:700, 708` |
| Le prestataire garde ses outils | Quali Contact ne veut pas changer | Format d'échange écrit et validé par lui avant tout développement | `travaux/strategie-retenue.md:295` |
| Trop de documents | Procédures non lues | 5 à 8 procédures au plus ; écrites pour des personnes, pas pour des agents | `travaux/strategie-retenue.md:327` ; `travaux/syn-capacite-ia.md:648` |
| Glissement vers l'exécution par Marwin | « Faites-le, ce sera plus vite » | Marwin ne reprend pas l'exécution ; socle limité au pilotage | `travaux/strategie-retenue.md:337` |
| Crainte de dépendre de Marwin | Hésitation à confier les outils | Comptes au nom de l'entité ; exercice de sortie à blanc au mois 6 | `travaux/strategie-retenue.md:189, 281` |

### 10.3 Formation et procédures

- **Pour l'équipe du client** (offre C6) : deux séances de formation ; 5 à 8 procédures écrites, chacune avec sa fiche de secours manuel ; 30 jours d'accompagnement compris [PR] (`travaux/strategie-retenue.md:327, 332`).
- **Une procédure est validée quand une autre personne que son auteur l'a appliquée seule** (`travaux/syn-capacite-ia.md:636`). Pour le client, cette application seule par la personne désignée est un critère d'**adoption**, pas de livraison [PR, ce livrable].
- **Pour Marwin** : charte d'usage de l'IA et une formation tracée (article 4 du règlement européen sur l'IA) (07-processus-ia-et-essais.md, section 9.3).
- **Méthodes séparées des données** : les procédures génériques de Marwin ne contiennent aucune donnée confidentielle du client (`travaux/syn-capacite-ia.md:633, 640`).

### 10.4 Transition

1. **Mesure de référence** pendant deux semaines avant tout essai (`travaux/syn-capacite-ia.md:699`).
2. **Organisation simple d'abord** (règles, modèles, rituels), puis outils existants configurés ; développement seulement si l'essai le justifie (`travaux/syn-capacite-ia.md:652-666`).
3. **Trois étapes** : démonstrateur interne, pilote client de 4 à 8 semaines, exploitation régulière ; chaque passage a sa preuve (`travaux/syn-capacite-ia.md:689-693`).
4. **Un changement à la fois** : une voie de pilote à la fois ; un processus à la fois [PR] (`travaux/strategie-retenue.md:241-251`).
5. **Le mode manuel reste disponible** : fiche de secours par processus ; retour au manuel si la relecture et les corrections dépassent 50 % du temps de référence pendant 4 semaines (`travaux/strategie-retenue.md:176`).

### 10.5 Accompagnement

Point hebdomadaire et comité mensuel du socle ; 30 jours d'accompagnement de C6 ; bilan au troisième mois ; sortie à blanc au sixième mois [PR] (`travaux/strategie-retenue.md:256-259, 281, 332`). L'accompagnement au-delà, par exemple la formation d'un nouveau prestataire du client, est chiffré en avenant [PR, ce livrable].

### 10.6 Livraison réussie

**Définition retenue.** Une livraison est réussie quand elle est **livrée** selon des critères écrits avant le démarrage, **réellement utilisée** par les personnes prévues, et que son **résultat est accepté** par écrit (`travaux/DEMANDE.md:46` ; `travaux/strat-S3-contradicteur.md:469`).
**Ce qui déclenche le paiement** : la livraison seule, que Marwin contrôle. **Ce qui décide de la suite** : l'usage et l'acceptation, qui dépendent du client [PR] (`travaux/strategie-retenue.md:113, 287`). Pour le cadrage et les lots, la livraison rend le solde exigible ; pour un socle, payé d'avance, elle correspond aux engagements de service dont dépend le malus. L'indicateur interne « résultats acceptés par JP » ne compte que les livraisons réussies (`travaux/strategie-retenue.md:163`).

| Offre | Livrée (sous le contrôle de Marwin) | Utilisée | Résultat accepté | Si l'usage ne vient pas |
| --- | --- | --- | --- | --- |
| **A cadrage** | Dossier remis et restitution tenue | Inventaire validé par écrit ; trois priorités signées | Au moins une priorité confiée avec un budget ; demande écrite d'une suite sous 30 jours | Arrêt propre ; GianLuca garde le dossier |
| **B0 socle pilote** | 100 % des décisions avec responsable, date et source ; compte rendu sous 24 h ouvrées dans ≥ 90 % des cas | ≥ 80 % des comptes rendus commentés sous 3 jours ouvrés ; registre consulté chaque semaine | Critères tenus 4 semaines ; demande écrite de poursuivre | Abandon si registre non consulté après 4 semaines |
| **C2 pilote commercial** | Fiches sourcées et datées à ≥ 90 % ; 100 % des numéros partagés signalés ; 100 % des oppositions respectées ; kit validé ; outil de réimport testé | L'appelant utilise les fiches ; ≥ 90 % des résultats d'appel réimportés | Seuils fixés avec GianLuca avant l'essai (repère : joignabilité ≥ 50 %) | Appels non commencés 15 jours ouvrés après la livraison : mesure en lot optionnel ; changer de cible ou arrêter |
| **C6 outillage et passation** | Outils en service sur les comptes du client ; procédures et fiches de secours remises ; deux formations ; restauration réussie ; exports | La personne désignée utilise le registre 4 semaines de suite et traite ≥ 80 % des comptes rendus | Chaque procédure appliquée seule une fois par cette personne [PR, ce livrable] | Personne non désignée 15 jours ouvrés après la livraison : livraison prononcée ; Marwin ne reprend pas l'exécution |
| **Autres lots C** | Critères écrits au bon de commande | Critère d'usage écrit au bon de commande [PR, ce livrable] ; exemple C4 : le tableau sert à déposer une démarche | Validation écrite du valideur | À défaut de critère d'usage écrit, seule la livraison est mesurée, et la suite n'est pas proposée |
| **D exploitation** | Niveaux de qualité écrits ; mode manuel testé | Usage régulier sur le périmètre convenu | Critères tenus ; coût par résultat accepté connu | Incident critique : arrêt du processus |

Sources : `travaux/strategie-retenue.md:235, 237, 279, 281, 318-319, 336-337, 344-349` ; `travaux/syn-capacite-ia.md:702-707`.

---

## 11. Principes contractuels à faire traduire par l'avocat

### 11.0 Architecture des documents

Retour à l'architecture « contrat-cadre et fiches de mission » du 30 oct. [PR] (`travaux/strategie-retenue.md:184`).

| Document | Signé par | Quand | Contenu |
| --- | --- | --- | --- |
| Contrat-cadre | Marwin (président) et l'entité chef de file | Avant le premier bon de commande, relu par l'avocat | Les seize principes ci-dessous |
| Bon de commande | Marwin et l'entité concernée | Une prestation, une entité | Objet, livrables, critères de réception écrits, dépendances, prix HT et TTC, échéancier, exclusions, régime des droits |
| Mandat de dépense | Représentant légal de chaque entité | Seulement avec un socle récurrent | Liste fermée d'actes, plafonds, délégué, registre |
| Accord de traitement (art. 28 RGPD) | Entité responsable du traitement et Marwin | Avant toute donnée personnelle réelle | Huit clauses a à h ; sous-traitants ultérieurs autorisés |
| Annexe des droits | Avec chaque bon de commande qui produit un livrable | À la commande | Composants génériques nommés ; développements propres ; licences tierces |
| Annexe de réversibilité | Avec le contrat-cadre ; mise à jour chaque trimestre | Dès le départ | Inventaire des comptes, données, configurations, procédures |
| Accords séparés (bureaux, emploi, capital) | — | Pas avant le bilan du mois 6 (capital : 12 à 24 mois) | Chacun avec sa durée, son prix, sa sortie ; aucun lien avec les honoraires |

Sources : `travaux/strategie-retenue.md:185, 556-560, 627-633` ; `travaux/syn-droit.md:605` ; `travaux/rj-R3-travail-contrats.md:443-449`.

Pour chacun des seize points : le **principe** [PR] ; le **pourquoi** ; ce que l'**avocat** doit trancher ou rédiger.

### 11.1 Entités et signataires

- **Principe.** Côté client : l'entité chef de file (dénomination, SIREN, signataire habilité, effectif), et pour chaque prestation l'entité qui commande, celle qui paie et la personne qui valide. Côté Marwin : Marwin Tech SAS, représentée par son président ; l'accord des deux associés précède toute signature (`travaux/strategie-retenue.md:223, 614`). Déclaration écrite du lien de Morgan avec BOJ.ART dès le premier document remis (`travaux/strategie-retenue.md:115, 635`).
- **Pourquoi.** Une relation personnelle ne fait pas un contrat avec toutes ses sociétés (`travaux/DEMANDE.md:23`). Avant l'immatriculation, les signataires sont tenus solidairement et indéfiniment des actes, sauf reprise [FV] (`travaux/syn-droit.md:274-277`). Pour un contrat d'au moins 5 000 € HT, l'entité doit obtenir de Marwin, à la signature puis tous les six mois, une attestation Urssaf de moins de six mois et un justificatif d'immatriculation (accusé de réception de l'art. R123-6 C. com. admis) ; le cadrage de 6 500 € HT est concerné [FV] (`travaux/ver-R3-travail-contrats.md:35`).
- **Solvabilité.** Une fois l'entité nommée : statut actif, dirigeant habilité, comptes déposés, absence de procédure collective, vérifiés sur les registres publics, sans contact (`travaux/strategie-retenue.md:566`).
- **Avocat.** Ordre des signatures ; lettre d'intention plutôt que bon de commande « en formation » (10-structures-et-relations.md, section 10.1, écart) ; pouvoirs du signataire de chaque entité.

### 11.2 Objet et périmètre

- **Principe.** L'objet est une liste fermée de livrables et, pour le socle, une liste fermée de services sur un nombre nommé de projets actifs. Exclusions écrites : comptabilité, paie, conseil juridique ou fiscal, gestion immobilière, vente de voyages, recouvrement, maniement de fonds, intermédiation de vente d'œuvres, organisation d'événements, exploitation de lieux, astreinte. Formule : « Marwin coordonne, le professionnel compétent exécute et signe » (`travaux/rj-R3-travail-contrats.md:384` ; `travaux/strategie-retenue.md:650`).
- **Indépendance.** Marwin organise ses méthodes, ses horaires et ses moyens (`interne/offre-marwin-tech-remuneration-et-collaboration.md:213`) ; la liste des livrables précède la liste des heures (`travaux/rj-R3-travail-contrats.md:148`).
- **Aucun résultat promis** sur les ventes, les rendez-vous ou les décisions ; ils sont suivis, pas garantis (`travaux/strategie-retenue.md:157`).
- **Pourquoi.** La présomption de non-salariat des dirigeants tombe en cas de subordination juridique permanente, même « par une personne interposée » [FV] (`travaux/ver-R3-travail-contrats.md:32`).
- **Avocat.** Rédaction des exclusions ; indices de subordination à supprimer (question déjà posée : 10-structures-et-relations.md, section 19.3).

### 11.3 Capacité réservée

- **Principe.** Le socle se vend au périmètre, pas au temps. La capacité de référence est nominative et répartie par entité ; le relevé mensuel des JP est remis comme preuve, pas comme base de prix. Report d'au plus 20 %, pour du pilotage seulement ; jamais converti en production. Deux associés en réunion ne comptent double que si le bon de commande le prévoit (`travaux/strategie-retenue.md:186, 268, 283, 389`).
- **Variations.** Changement de palier au bilan trimestriel, par accord écrit ; sans pénalité si un associé est indisponible plus de 10 jours ouvrés (`travaux/strategie-retenue.md:281`).
- **Pourquoi.** Depuis le 20 août 2026, une « réduction substantielle […] des volumes de commandes » pendant une négociation, même temporaire, peut engager la responsabilité de son auteur dans une relation établie [FV pour le texte ; HY pour l'application] (`travaux/ver-R3-travail-contrats.md:39`). Les variations doivent donc suivre un mécanisme écrit à l'avance.
- **Avocat.** Rédiger les paliers comme des périmètres ; vérifier qu'un changement de palier prévu au contrat n'est pas une rupture partielle.

### 11.4 Livrables et réception

- **Principe.** Critères de réception écrits avant le démarrage ; réception **expresse** demandée ; réserves **motivées** par écrit sous 10 jours ouvrés, rattachées aux critères ; un cycle de correction compris ; sans réserve motivée, solde exigible au plus tard 30 jours après la remise. Cette règle vaut « pour la facturation seulement » : ni approbation d'une suite, ni autorisation d'une dépense (`travaux/strategie-retenue.md:235, 604`).
- **Livraison et adoption séparées** : la livraison déclenche le solde ; l'adoption décide de la suite (section 10.6).
- **Engagements de service du socle** : rapport mensuel au 5e jour ouvré ; si deux engagements sont manqués dans le mois, avoir de 5 % sur la facture suivante (`travaux/strategie-retenue.md:279`).
- **Avocat.** Rédiger l'exigibilité sans en faire une acceptation ; articuler avec la « réception » au sens du contrat d'entreprise.

### 11.5 Dépendances au client

- **Principe.** Les obligations du client sont écrites : désigner un délégué et un valideur ; fournir pièces et accès sous 10 jours ouvrés ; répondre aux demandes de décision sous 5 jours ouvrés ; ouvrir et payer ses comptes et outils ; nommer le responsable du traitement (`travaux/strategie-retenue.md:154, 228, 272`).
- **Effets d'un manquement** : jalons reportés et consignés, sans pénalité pour Marwin ; capacité réaffectée ; au-delà, signal de suspension (section 15). Le prix d'un socle reste dû pour le mois en cours.
- **Pourquoi.** Les réceptions qui dépendent d'actes du client (recruter, appeler) avaient été mal construites dans une proposition antérieure ; la correction retenue sépare livraison et adoption [FV] (`travaux/strategie-retenue.md:113`).
- **Avocat.** Rédiger les obligations du client comme des conditions d'exécution, et non comme de simples souhaits.

### 11.6 Prix, acompte et paiement

- **Principe : le paiement suit la nature de la prestation** (`travaux/strategie-retenue.md:431-434, 440-445`).

| Prestation | Facturation | Échéance | Démarrage |
| --- | --- | --- | --- |
| Cadrage | 50 % à la commande, 50 % à la réception | Acompte à réception de facture ; solde sous 8 jours | À l'encaissement de l'acompte |
| Socle | Mensuel à échoir, facture le 25 du mois précédent | Le 1er du mois ; premier mois à la signature | À l'encaissement du premier mois |
| Lots | 40 % à la commande, 60 % à la livraison ; 40 / 30 / 30 au-delà de 8 JP | 8 jours | À l'encaissement de l'acompte |
| Exploitation | Minimum à échoir ; variable en fin de mois | Le 1er ; variable sous 15 jours | — |
| Avenants | Fin de mois | 15 jours | Après signature de l'avenant |

- **TVA** facturée dès la première facture ; devis en HT et TTC (`travaux/strategie-retenue.md:462`). Prix figés pour la période contractuelle ; partage des gains d'automatisation au renouvellement seulement (un tiers au client après la première année) (`travaux/strategie-retenue.md:418-420`).
- **Retard** : pénalités d'au moins trois fois le taux de l'intérêt légal et indemnité forfaitaire de 40 € [FV] ; effets en section 12.1 (`travaux/strategie-retenue.md:463`).
- **Concession possible** : socle facturé en fin de mois, payable sous 7 jours, après trois échéances payées à l'heure (`travaux/strategie-retenue.md:464`).
- **Rétractation des petites entreprises** [HY] : si le contrat est conclu hors établissement avec une entité de 5 salariés au plus dont l'activité principale ne couvre pas ce service, 14 jours de rétractation et aucun paiement avant 7 jours pourraient s'appliquer (art. L221-3 C. consom., https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226882, consulté le 4 nov. 2026 ; `travaux/ver-R5-art-lieux.md:39` ; `travaux/strategie-retenue.md:466`).

> **Écart avec la stratégie retenue : la parade « signature à distance ».**
> La stratégie propose deux parades à la règle de rétractation : « signature à distance, ou délai de 7 jours prévu dans le calendrier » (`travaux/strategie-retenue.md:466`). Le texte de L221-3 ne vise bien que le hors établissement ; la vente à distance entre professionnels n'est pas couverte [FV] (`travaux/rj-R5-art-lieux.md:273`). Mais l'audit n'a pas relu la définition légale du contrat « hors établissement ». Selon ma lecture, non vérifiée, elle peut englober un contrat conclu à distance juste après une sollicitation personnelle du client hors de l'établissement du professionnel, par exemple au sortir d'un rendez-vous chez lui [HY].
> *Ce que ce livrable retient.* Tant que l'avocat n'a pas tranché, et si l'entité compte 5 salariés au plus, on applique **le délai de 7 jours dans tous les cas** : aucun encaissement ni démarrage avant J+7, information sur la rétractation jointe. La signature à distance reste utile, mais ne suffit pas seule.
> *Décision* : question n° 7 de la section 17 ; Morgan et Mathys n'exigent aucun paiement avant J+7 dans ce cas.

- **Avocat.** Applicabilité de L221-3 au contrat de Marwin (déjà posée : 10-structures-et-relations.md, section 19.4, question 5) ; définition du hors établissement.

### 11.7 Frais et achats

- **Principe.** Marwin n'avance jamais d'argent pour le client. Achats, abonnements et prestataires sont commandés au nom de l'entité et payés par elle, sans marge. Les tiers (Quali Contact, expert-comptable, avocat, photographe, artistes) facturent directement l'entité (`travaux/strategie-retenue.md:188, 387-388`).
- **Débours** : seulement si les quatre conditions du BOFiP sont réunies (au nom et pour le compte du mandant, reddition de compte précise, justification, comptes de passage), avec un mandat « préalable et explicite » [FV] (BOI-TVA-BASE-10-10-30, § 200 et 220, https://bofip.impots.gouv.fr/bofip/488-PGP.html/identifiant=BOI-TVA-BASE-10-10-30-20220511, consulté le 4 nov. 2026 ; `travaux/ver-R3-travail-contrats.md:56`).
- **Déplacements** : compris dans le forfait quand le bon de commande le dit (cadrage : deux trajets) ; sinon chiffrés au devis, jamais refacturés sans accord préalable [PR, ce livrable] (`travaux/strategie-retenue.md:231`).
- **Pourquoi.** Si Marwin achète en son nom puis refacture, la somme entre dans son chiffre d'affaires et dans sa base de TVA, et Marwin porte le risque d'impayé [HY cohérente avec le BOFiP] (`travaux/rj-R3-travail-contrats.md:322`).
- **Avocat et expert-comptable.** Rédaction du mandat d'achat ; traitement TVA (question déjà posée : 10-structures-et-relations.md, section 19.1, question 11).

### 11.8 Changement de priorité

- **Principe.** Les priorités se changent en comité mensuel, ou entre deux comités par écrit du délégué. Une demande nouvelle remplace un projet actif ou devient un lot. Un lot en cours se modifie par avenant signé **avant** le travail, ou s'arrête avec paiement du travail fait (`travaux/strategie-retenue.md:283, 391, 613`).
- **Pourquoi.** Sans limite d'encours, un abonnement absorbe tout (`travaux/DEMANDE.md:28`).
- **Avocat.** Clause de modification ; calcul du travail fait en cas d'arrêt d'un lot (section 12.2).

### 11.9 Urgences et disponibilité

- **Principe.** Heures ouvrées ; plages de contact écrites ; délais distincts d'accusé de réception, de début de traitement et de résolution ; liste fermée d'urgences ; arrêt sans autorisation ; aucune astreinte par défaut ; forfait d'astreinte séparé, avec relais nommés, sur demande (section 6) (`travaux/strategie-retenue.md:353-355`).
- **Continuité** : binôme ; coffre partagé des accès ; changement de palier sans pénalité au-delà de 10 jours ouvrés d'absence d'un associé (`travaux/strategie-retenue.md:281, 619`).
- **Avocat.** Rédaction des délais comme obligations de moyens ; cas de force majeure.

### 11.10 Sous-traitance

- **Principe.** Marwin ne sous-traite qu'un lot délimité, avec l'accord écrit préalable de l'entité [PR, ce livrable] et l'accord des deux associés (`travaux/strategie-retenue.md:614`). Le sous-traitant travaille sous l'autorité de son propre employeur ou de Marwin, jamais sous celle du client ; les demandes du client passent par Morgan ou Mathys (`travaux/rj-R3-travail-contrats.md:146-147`). Marwin répond du travail de son sous-traitant envers le client.
- **Pièces** : attestation de vigilance exigée du sous-traitant dès 5 000 € HT cumulés (`travaux/syn-droit.md:388`) ; cession écrite des droits du sous-traitant à Marwin avant toute cession au client (`travaux/rj-R3-travail-contrats.md:396`) ; s'il traite des données personnelles, il devient sous-traitant ultérieur, autorisé par écrit par le responsable du traitement (07-processus-ia-et-essais.md, section 9.1).
- **Ce qui n'est pas de la sous-traitance de Marwin** : Quali Contact, les artisans, le photographe, qui contractent directement avec l'entité.
- **Pourquoi.** Le prêt de main-d'œuvre à but lucratif et à objet exclusif est interdit (art. L8241-1 C. trav.) [FV] (`travaux/ver-R3-travail-contrats.md:34`). La nouvelle vigilance du maître de l'ouvrage (art. L8222-1-1) ne vise que les sous-traitants **acceptés** au titre de la loi de 1975, au-delà d'un montant fixé par décret, avec une entrée en vigueur au plus tard fin décembre 2026 [FV] (`travaux/ver-R3-travail-contrats.md:36`).
- **Avocat.** Clause de sous-traitance ; applicabilité de la loi de 1975 à une prestation intellectuelle [IN].

### 11.11 Droits et confidentialité

- **Principe : trois régimes** (section 13) : les données et documents du client lui appartiennent ; les développements propres lui sont **cédés par livrable**, au paiement complet, par écrit, droit par droit ; les composants génériques et outils préexistants de Marwin lui sont **concédés** par une licence gratuite, non exclusive et perpétuelle pour son usage interne, qui survit au contrat (`travaux/strategie-retenue.md:287` ; `travaux/syn-droit.md:497-498`).
- **Pourquoi.** Commander et payer ne suffit pas : il faut une cession écrite (art. L131-2 CPI), chaque droit mentionné à part, domaine délimité (art. L131-3), sans cession globale des œuvres futures (art. L131-1) [FV] (https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069414/LEGISCTA000006161639/, consulté le 4 nov. 2026 ; `travaux/ver-R3-travail-contrats.md:42`).
- **CRM existant** : jamais facturé rétroactivement ; régime écrit avant tout lot qui le touche, une fois la propriété réglée entre Morgan et Mathys (`travaux/strategie-retenue.md:385`). « Copilote Jarvis » suspendu ; œuvres de Medhi hors de tout ce que Marwin peut céder (`travaux/strategie-retenue.md:643, 648`).
- **Confidentialité** : les informations du client servent à ses projets et à rien d'autre ; aucune réutilisation des données de GianLuca pour la prospection de Marwin ou d'OLSEN (`travaux/strategie-retenue.md:619` ; `pour-gianluca/proposition-de-cadrage.md:99`). Citer GianLuca comme référence auprès d'un autre client : seulement avec son accord écrit [PR, ce livrable].
- **Contenus** : contenus fiscaux validés par un professionnel avant usage ; mention « généré par IA » quand elle est due ; autorisation des artistes montrés et des personnes filmées (`travaux/syn-droit.md:499, 502`).
- **Avocat.** Annexe des droits (étendue, destination, lieu, durée) ; durée de la confidentialité après le contrat ; licence qui permet la maintenance par un tiers (section 13). Chaîne des droits du CRM : question déjà posée (10-structures-et-relations.md, section 19.4, question 1).

### 11.12 Données et sécurité

- **Principe.** Aucune donnée personnelle réelle avant : décision sur la fuite ; responsable du traitement désigné ; accord de l'article 28 (huit clauses a à h) ; registre côté responsable et côté sous-traitant ; offres d'IA professionnelles avec clauses contractuelles types et analyse d'impact des transferts pour Anthropic et OpenAI, absents de la liste du Data Privacy Framework au 4 nov. 2026 [MM] (`travaux/strategie-retenue.md:669` ; `travaux/syn-droit.md:605-606, 670-671`).
- **Sécurité** : accès nominatifs, révocables, au strict nécessaire ; secrets dans un coffre ; actions classées (autonome, approbation humaine, interdite) ; approbation hors de portée de l'agent ; journal inaltérable ; bouton d'arrêt testé chaque trimestre ; plafonds de coûts (`travaux/syn-droit.md:687-695` ; 07-processus-ia-et-essais.md, sections 8 et 10).
- **Incident** : Marwin informe l'entité sans délai, par écrit sous 24 h ; le responsable du traitement décide des notifications (`travaux/strategie-retenue.md:585` ; `travaux/syn-droit.md:624`).
- **Rôle au sens du règlement européen sur l'IA** : déployeur quand Marwin utilise des outils d'IA pour le client ; fournisseur si elle livre sous son nom un assistant [HY] (`travaux/strategie-retenue.md:559`).
- **Incident déjà survenu** : GianLuca en est informé par écrit, dans des termes validés par le conseil, sans reconnaissance de responsabilité non pesée (`travaux/strategie-retenue.md:794, 809`). Le contrat ne doit pas le passer sous silence.
- **Avocat ou DPD.** Rôles RGPD pour la période de constitution du fichier ; notification ; information des personnes ; délai contractuel d'information en cas d'incident (section 17).

### 11.13 Maintenance et garanties

- **Principe.** Les défauts de Marwin sont corrigés gratuitement pendant 60 jours après la réception. Au-delà, la maintenance n'est due que si une exploitation (offre D) la prévoit, au plus 0,5 JP par mois et par processus. Un outil construit dans un lot n'est jamais refacturé (`travaux/strategie-retenue.md:349, 384`).
- **Ce que Marwin garantit** : la conformité de chaque livrable à ses critères écrits ; sauvegardes, restauration testée, journal et réversibilité des outils du socle ; pièces de vigilance et attestation d'assurance (`travaux/strategie-retenue.md:264`).
- **Ce qu'elle ne garantit pas** : l'exactitude d'une sortie d'IA non relue ; la disponibilité ou le prix des outils tiers ouverts au nom du client ; un résultat commercial. Si un fournisseur d'IA augmente ses prix, la hausse porte sur les comptes du client ; pour les rares outils de Marwin, clause de révision (`travaux/strategie-retenue.md:532`).
- **Avocat.** Durée et étendue de la garantie de 60 jours ; articulation avec la limitation de responsabilité.

### 11.14 Responsabilités

- **Principe** (`travaux/strategie-retenue.md:557`) : plafond lié aux honoraires des douze derniers mois, aligné sur le plafond assuré ; exclusion des dommages indirects (ventes manquées, économies d'impôt espérées par des prospects, décisions d'investissement) ; obligation de moyens pour le pilotage, la préparation des décisions et les sorties d'IA ; obligation de résultat seulement pour des livrables précis réceptionnés. Marwin ne répond ni des décisions de GianLuca ni des avis de ses professionnels.
- **Limites légales** [FV] : un plafond ne joue pas en cas de faute lourde ou dolosive (art. 1231-3 C. civ., https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032010127) ; une clause qui « prive de sa substance l'obligation essentielle » est réputée non écrite (art. 1170) ; dans un contrat d'adhésion, une clause non négociable qui crée un déséquilibre significatif aussi (art. 1171, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036829836) ; consultés le 4 nov. 2026 (`travaux/rj-R3-travail-contrats.md:269, 287-290`).
- **Mandat** : la responsabilité du mandataire pour ses fautes de gestion (art. 1992) ne s'écarte pas entièrement ; le mandat étroit est la vraie protection (section 5).
- **Assurance** : RC professionnelle souscrite **avant** la première prestation, avec les volets IA, cyber et données, et la fuite déclarée sincèrement à l'assureur (`travaux/strategie-retenue.md:554`).

> **Écart avec la stratégie retenue : un plancher au plafond de responsabilité.**
> La stratégie lie le plafond « aux honoraires des douze derniers mois » (`travaux/strategie-retenue.md:557`). Au début de la relation, ce montant est très faible : au démarrage du cadrage, seul l'acompte de 3 250 € HT a été payé. Un plafond dérisoire sur la remise d'un livrable central serait fragile au regard de l'art. 1170 (`travaux/rj-R3-travail-contrats.md:278`) ; s'il tombe, la responsabilité n'est plus plafonnée du tout [HY].
> *Ce que ce livrable retient.* Plafond = le plus élevé de deux montants : les honoraires des douze derniers mois, ou le prix total du bon de commande concerné ; toujours sous le plafond assuré. Le reste du principe ne change pas.
> *Décision* : question n° 2 de la section 17 ; l'avocat fixe la formule, l'assureur confirme la couverture.

- **Avocat.** Formule du plafond ; contrat négocié ou d'adhésion (question déjà posée : 10-structures-et-relations.md, section 19.4, question 4).

### 11.15 Durée, révision et résiliation

- **Principe** (`travaux/strategie-retenue.md:274, 465`) :

| Prestation | Durée | Renouvellement | Préavis |
| --- | --- | --- | --- |
| Cadrage | 3 à 4 semaines | Une seule fois | — |
| B0 | 8 semaines | Aucune tacite reconduction | — |
| B1, B2 | 3 mois | Par accord écrit ; bilan au 3e mois | Réciproque : 1 mois la première année, 2 mois ensuite |
| D | 6 mois | Par accord écrit | À fixer au bon de commande |

- **Résiliation pour manquement** : retard de paiement de 30 jours ; manquement grave à la confidentialité ou à la sécurité ; exercice d'une activité exclue demandé avec insistance [PR, ce livrable pour le dernier cas].
- **Effets** : si Marwin interrompt de son fait, les jours non fournis sont remboursés au prorata ; sinon, le mois en cours reste dû ; travaux engagés et réversibilité dus dans tous les cas (`travaux/strategie-retenue.md:465`).
- **Révision** : prix figés pour la période ; révision au renouvellement ; partage des gains d'automatisation à partir de la deuxième année (`travaux/strategie-retenue.md:418-420`).
- **Indépendance des accords** : aucune clause qui fait tomber les honoraires si les bureaux s'arrêtent, ou l'inverse (`travaux/syn-droit.md:438`).
- **Pourquoi.** Rompre brutalement une relation commerciale établie sans préavis écrit suffisant engage son auteur ; un préavis de 18 mois met à l'abri d'une contestation sur la durée ; la règle joue dans les deux sens [FV/HY] (art. L442-1 II C. com., https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047381704, consulté le 4 nov. 2026 ; `travaux/rj-R3-travail-contrats.md:233-235` ; `travaux/ver-R3-travail-contrats.md:39`).
- **Avocat.** Préavis croissant avec l'ancienneté ; règlement amiable préalable (section 17).

### 11.16 Réversibilité et transmission

- **Principe** (`travaux/strategie-retenue.md:560` ; `travaux/rj-R3-travail-contrats.md:443-449`) : comptes au nom du client dès le premier jour ; inventaire tenu à jour (données, documents, code, configurations, automatisations, comptes, clés, sauvegardes, procédures) ; formats ouverts et documentés ; restitution complète en 15 jours ouvrés au plus ; exercice de sortie à blanc au mois 6, puis test de restitution au moins une fois par an ; données personnelles supprimées ou restituées au choix du responsable, avec attestation ; licence sur les composants génériques maintenue après la fin.
- **Transmission** : assistance au successeur du client (autre prestataire ou salarié) chiffrée en avenant au-delà de la restitution [PR, ce livrable] ; à la sortie, accès de Marwin révoqués et clés d'API renouvelées par le client [PR, ce livrable].
- **RGPD** : à la fin, le sous-traitant « supprime toutes les données à caractère personnel ou les renvoie » au choix du responsable [FV] (art. 28.3 g, https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32016R0679, consulté le 4 nov. 2026 ; `travaux/ver-R3-travail-contrats.md:43`).
- **Data Act**, si Marwin hébergeait et exploitait elle-même un service de données pour le client : clauses de changement de fournisseur (préavis de 2 mois au plus, transition de 30 jours au plus, au moins 30 jours pour récupérer les données), y compris pour un service sur mesure ; aucuns frais de changement à partir du 12 janv. 2027, règle dont les services sur mesure sont exemptés [FV] (règlement (UE) 2023/2854, art. 25, 29 et 31, https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32023R2854, consulté le 4 nov. 2026 ; `travaux/ver-R3-travail-contrats.md:43`). La parade reste la règle G6 : ne pas héberger.
- **Aujourd'hui** : la promesse du diaporama est inexacte tant que le CRM reste sous les comptes des associés ; transférer le projet Firebase et le dépôt vers des comptes de l'entité avant la signature, ou documenter le plan pour le faire (`travaux/rj-R3-travail-contrats.md:438, 463`).
- **Avocat.** Qualification de Marwin au sens du Data Act (question déjà posée : 10-structures-et-relations.md, section 19.4, question 7) ; coût de la réversibilité dans le prix.

---

## 12. Effets d'un impayé, d'un arrêt du projet, d'un désaccord sur un livrable

### 12.1 Impayé

| Moment | Ce qui se passe | Source |
| --- | --- | --- |
| Échéance | Le travail d'une prestation ne démarre qu'à l'encaissement de son acompte ou de son premier mois : l'exposition reste limitée (≈ 5 500 à 6 000 € HT au plus en régime central [ES]) | `travaux/strategie-retenue.md:440-447` |
| Lendemain de l'échéance | Relance écrite | `travaux/strategie-retenue.md:463` |
| 8 jours après une relance restée sans effet | **Suspension** des travaux non urgents, notifiée par écrit ; aucun nouveau lot ; capacité réaffectée | `travaux/strategie-retenue.md:463` ; `interne/offre-marwin-tech-remuneration-et-collaboration.md:207` |
| 30 jours de retard | Résiliation possible | `travaux/strategie-retenue.md:463` |
| À tout moment | Pénalités et indemnité de 40 € ; développements non payés non cédés | `travaux/strategie-retenue.md:463` ; `travaux/syn-capacite-ia.md:877` |

**Ce que la suspension ne suspend pas** [PR, ce livrable] : la confidentialité ; la sécurité des données que Marwin détient comme sous-traitante ; le droit d'arrêter un processus en incident ; la restitution des données et documents du client, qui ne dépend jamais du paiement (`travaux/syn-capacite-ia.md:877`).
**Aucune rétention technique** [PR, ce livrable] : Marwin ne coupe jamais un outil du client, ne change aucun mot de passe et ne retire aucun accès du client pour obtenir un paiement. Les outils sont sur ses comptes (règle G6) ; une telle mesure contredirait la promesse de réversibilité et pourrait engager Marwin [HY]. Les recours sont contractuels : pénalités, suspension, résiliation, refus de céder les droits non payés.
**En interne** : rémunération des associés arrêtée tant que l'impayé dure ; aucun travail continué « pour ne pas perdre le client » (`travaux/strategie-retenue.md:528`).

### 12.2 Arrêt du projet

| Cas | Effet | Source |
| --- | --- | --- |
| GianLuca abandonne ou reporte un projet actif du socle | Remplacé par un autre projet au comité suivant, ou palier réduit au bilan trimestriel ; le mois en cours reste dû | `travaux/strategie-retenue.md:281, 283, 465` |
| GianLuca arrête un lot en cours | Décision écrite du signataire ; Marwin remet l'état d'avancement documenté ; travail fait payé au prorata des jalons atteints, ou à défaut des JP relevées, dans la limite du prix du lot ; l'acompte reste acquis à hauteur du travail fait | [PR, ce livrable] ; `travaux/strategie-retenue.md:465` |
| GianLuca met fin à la collaboration | Préavis (1 mois la première année) ; mois en cours dû ; restitution en 15 jours ouvrés | `travaux/strategie-retenue.md:274, 465` |
| Marwin se retire de son fait | Même préavis ; jours non fournis remboursés au prorata ; restitution complète | `travaux/strategie-retenue.md:465` |
| Marwin cesse son activité | Rien n'est bloqué : comptes du client à son nom ; licence perpétuelle sur les composants génériques ; documentation sous 15 jours | `travaux/syn-capacite-ia.md:875` |
| Le projet devient impossible ou illicite (données, autorisation refusée) | Arrêt immédiat par l'une ou l'autre partie ; travail fait payé ; pas de pénalité | [PR, ce livrable] |
| Projet artistique abandonné (STRATES, laboratoire) | Sans effet : hors du contrat | `travaux/strategie-retenue.md:536` |

### 12.3 Désaccord sur un livrable

1. **Remise**, avec rappel des critères écrits avant le démarrage.
2. **Sous 10 jours ouvrés**, le valideur accepte ou formule des réserves **motivées**, rattachées aux critères. Sans réserve motivée : solde exigible au plus tard 30 jours après la remise, pour la facturation seulement.
3. **Tri des réserves** [PR, ce livrable] : une réserve qui relève des critères est un défaut, corrigé une fois sans frais ; une réserve qui ajoute une exigence est une demande nouvelle, traitée par avenant ou par un lot.
4. **Après la correction**, s'il reste un désaccord : arbitrage en comité.
5. **Issues possibles** : acceptation ; avenant ; arrêt du lot avec avoir sur la même commande, à hauteur de la part non conforme. Jamais de travail gratuit sur une autre commande.
6. **Si le désaccord persiste** : tentative écrite de règlement amiable (par exemple une médiation) avant toute action [PR, ce livrable], à faire rédiger par l'avocat.

Sources : `travaux/strategie-retenue.md:235, 390, 604, 612`.

---

## 13. Remettre n'est pas céder

**Règle** : GianLuca doit pouvoir **tout récupérer** et **tout faire reprendre** par quelqu'un d'autre. Cela ne suppose pas qu'il devienne propriétaire des composants génériques de Marwin. Le détail par situation (fin normale, cessation de Marwin, fournisseur défaillant, désaccord) est dans 07-processus-ia-et-essais.md, section 11 ; la propriété actif par actif est dans 10-structures-et-relations.md, section 13.

| Catégorie | Exemples | Régime | Quand | Conditionné au paiement ? |
| --- | --- | --- | --- | --- |
| **Données et documents du client** | Registre, comptes rendus, budgets, données du CRM qui le concernent, pièces fournies | À lui ; restitution ou suppression à son choix | À tout moment ; restitution complète en 15 jours ouvrés | **Non, jamais** |
| **Comptes et accès** | Espaces de travail, outils, abonnements | À son nom dès le premier jour ; accès de Marwin révoqués à la sortie | Immédiat | Non |
| **Exports, inventaire, journal** | Exports en formats ouverts, inventaire des outils, journal des actions | Remis | À tout moment ; à la sortie | Non |
| **Procédures, fiches de secours, configurations et prompts propres à ses processus** | Procédures C6, réglages des automatismes du client | Remis à tout moment ; **cédés** au paiement complet comme développements propres | À la remise ; cession au paiement | Usage d'une copie : non ; cession des droits : oui |
| **Développements propres** | Code et documentation faits pour lui | **Cession** par livrable, écrite, droit par droit | Au paiement complet | Oui |
| **Composants génériques et outils préexistants de Marwin intégrés à un livrable** | Modèles, scripts, méthodes, brique de mémoire si ses droits sont réglés | **Licence** gratuite, non exclusive, perpétuelle, pour son usage interne ; survit au contrat | Avec le paiement du livrable qui les intègre | Oui |
| **Outils internes de Marwin non livrés** | Bibliothèque de méthodes, outils de contrôle internes, prospection | Restent à Marwin | — | — |
| **CRM existant** | Code et fichier d'octobre | Régime écrit avant tout lot ; la part « données » relève de la première ligne | Après accord entre Morgan et Mathys | — |
| **Ce que Marwin ne détient pas** | Œuvres et fichiers de Medhi, films générés par un outil d'IA | Rien à remettre ni à céder | — | — |

Sources : `travaux/syn-capacite-ia.md:874-884` ; `travaux/syn-droit.md:494-503` ; `travaux/strategie-retenue.md:287, 385, 643`.

**Cinq règles** :
1. **Remise et cession sont deux actes distincts.** Le contrat le dit en toutes lettres (`travaux/rj-R3-travail-contrats.md:449`).
2. **La frontière entre générique et propre se fixe au bon de commande** : l'annexe des droits nomme les composants génériques utilisés [PR, ce livrable]. Sans cette liste, chaque composant devient un litige possible.
3. **La licence sur les composants génériques permet au client de faire maintenir ses outils par un tiers** de son choix, pour ses besoins internes ; elle n'autorise ni revente ni diffusion [PR, ce livrable]. Sans ce droit, la réversibilité ne serait qu'une remise de fichiers.
4. **Marwin ne garde aucune copie des données personnelles** après la mission (RGPD, art. 28.3 g) ; elle peut garder une copie de ses livrables, sans données personnelles, pour la preuve, pendant une durée fixée par l'avocat [PR, ce livrable].
5. **Ce qui ne tient pas aujourd'hui** : « le code, les données et le suivi restent chez les associés, dans leur dépôt GitHub et leur projet Firebase » [FV] (`crm/docs/rapport/rapport-crm-hermes360.md:19`). La promesse « Réversibilité : fichiers, configurations, documentations et accès remis » (`slides/garanties.html:30`) ne peut être gardée qu'avec « comptes ouverts au nom de votre entité dès le premier jour » (`travaux/strategie-retenue.md:826`).

---

## 14. Conditions minimales pour commencer

La stratégie fixe dix conditions, toutes requises, pour démarrer un travail payé (`travaux/strategie-retenue.md:660-669`). Je les répartis par étape : chaque étape suppose les précédentes [PR, ce livrable].

| Étape | Conditions supplémentaires | Preuve | Source |
| --- | --- | --- | --- |
| **1. Proposer** (message de recadrage, proposition de cadrage) | Fuite traitée : dépôt privé vérifié, fiche de violation, décision de notification documentée avec un avocat ou un DPD, décision sur l'information des personnes, GianLuca informé par écrit ; documents client cohérents ; accord écrit de Mathys ; au moins 6 JP facturables par mois engagés à deux | Décision datée ; capture de la visibilité « privé » ; fiche « rôles et disponibilités » signée | `travaux/strategie-retenue.md:54-55, 660-662` |
| **2. Signer** | Entité identifiée (dénomination, SIREN, signataire, effectif) ; solvabilité vérifiée ; contrat-cadre relu par l'avocat ; pacte signé ; dossier d'aide régionale déposé avant si l'entité la demande ; lettre d'intention ou bon de commande selon 10-structures-et-relations.md, section 10.1 | Bon de commande ou lettre d'intention ; extrait des registres | `travaux/strategie-retenue.md:453, 663, 665-666` |
| **3. Démarrer le travail** | SAS immatriculée ; compte professionnel ; RC professionnelle souscrite, fuite déclarée ; plateforme de facturation électronique ; K-bis ou accusé d'immatriculation et attestation Urssaf remis ; apport déposé ; acompte encaissé ; délai de 7 jours respecté si la règle de rétractation peut s'appliquer (section 11.6) | Relevé bancaire ; attestations | `travaux/strategie-retenue.md:455-458, 663-664, 667` |
| **4. Recevoir des accès** | Délégué nommé ; comptes et outils ouverts au nom de l'entité ; accès nominatifs | Inventaire des comptes | `travaux/strategie-retenue.md:668` |
| **5. Toucher des données personnelles réelles** | Responsable du traitement désigné ; accord de l'article 28 ; registre ; offres d'IA professionnelles, clauses contractuelles types, analyse d'impact des transferts | Accord signé ; registre | `travaux/strategie-retenue.md:669` ; 07-processus-ia-et-essais.md, section 9.3 |
| **6. Engager une dépense au nom de l'entité** | Socle récurrent signé ; mandat écrit signé par le représentant légal de l'entité ; liste fermée ; budgets approuvés ; registre des engagements ouvert | Mandat signé | `travaux/strategie-retenue.md:590` ; `travaux/rj-R3-travail-contrats.md:313-319` |
| **7. Automatiser sur données réelles** | Pilote réussi (critères tenus 4 semaines) ; grille de sécurité appliquée ; arrêt et restauration testés ; autorisation écrite du responsable du traitement | Rapport de pilote ; journal | `travaux/strategie-retenue.md:344, 582` ; `travaux/syn-capacite-ia.md:689-693` |

Rien ne s'encaisse avant l'immatriculation, ni sur un compte personnel, ni par l'entreprise existante de Morgan (`travaux/strategie-retenue.md:458`).

---

## 15. Signaux pour suspendre, réduire ou refuser

| Signal | Seuil | Réponse | Qui décide | Source |
| --- | --- | --- | --- | --- |
| Impayé | Non régularisé 8 jours après relance | **Suspendre** ; à 30 jours, résilier | Morgan, informé Mathys | `travaux/strategie-retenue.md:463, 675` |
| Accès non fournis | 10 jours ouvrés après le démarrage | **Suspendre** le lot concerné | Les deux | `travaux/strategie-retenue.md:676` |
| Décisions bloquantes | Deux en attente depuis plus de 15 jours ouvrés | **Suspendre** ; revue du contrat | Les deux, avec GianLuca | `travaux/strategie-retenue.md:677` |
| Saturation | Occupation d'un associé > 95 % deux mois, ou prospection < 50 % du plancher deux mois | **Suspendre** tout nouveau projet ; **réduire** | Les deux | `travaux/strategie-retenue.md:678` |
| Dérive du périmètre | Demandes hors périmètre > 20 % de la capacité deux mois | **Suspendre** ; en faire un lot ou un projet actif | Les deux, avec GianLuca | `travaux/strategie-retenue.md:679` |
| Incident critique | Nouvelle exposition de données, action non autorisée, envoi erroné | **Arrêter** le processus ; reprise manuelle | Quiconque le constate | `travaux/strategie-retenue.md:680` |
| Demande d'agir hors mandat | Signer, payer, engager pour le client ; travailler sans bon de commande, sur des comptes personnels ; avancer des achats | **Refuser** l'acte ; **suspendre** si la demande se répète | Les deux | `travaux/strategie-retenue.md:681` |
| Pression sur le calendrier | Travailler avant le paiement, ou avant J+7 si la rétractation peut s'appliquer | **Refuser** | Les deux | `travaux/strategie-retenue.md:682` |
| Subordination | Horaires imposés, ordres directs, place dans un organigramme, exclusivité de fait | **Suspendre** et faire corriger par écrit | Les deux, avec l'avocat | `travaux/strategie-retenue.md:683` |
| Mélange des rôles | Honoraires contre bureaux, emploi ou capital ; investissement lié à une baisse d'honoraires | **Refuser** cette partie | Les deux | `travaux/strategie-retenue.md:684, 703` |
| Activité exclue | Commission sur les ventes, encaissement pour la galerie, robot au contact du public | **Refuser** | Les deux | `travaux/strategie-retenue.md:685` |
| Besoin trop large et non cadré | 20 à 40 JP par mois sans entité, mandat ni accès | **Refuser** sous cette forme ; proposer le cadrage | Les deux | `travaux/strategie-retenue.md:702` |
| Personne côté client | Aucune personne désignée et glissement vers l'exécution | **Réduire** le socle au pilotage ; pas de reprise de l'exécution | Les deux | `travaux/strategie-retenue.md:337` |
| Absence d'engagement | Aucune entité au 15 déc. 2026 ; cadrage non payé au 31 janv. 2027 | **Reporter** sans production | Les deux | `travaux/strategie-retenue.md:697-698` |
| Désaccord entre associés | Sur une décision de la liste d'unanimité | **Rien n'est proposé** au client tant qu'il dure | Les deux | `travaux/strategie-retenue.md:614` |

La liste complète des réponses « réduire, reporter, refuser » est dans `travaux/strategie-retenue.md:691-705` ; elle n'est pas recopiée ici. Les seuils internes de saturation sont dans 06-fonctionnement-a-deux.md, section 8.

---

## 16. Recommandations : preuve, hypothèse, limite, décision

| Recommandation | Preuve | Hypothèse | Limite | Décision correspondante |
| --- | --- | --- | --- | --- |
| Le silence ne vaut jamais autorisation ; il ne rend exigible qu'un solde | Contradiction entre les offres du 29 oct. et du 2 nov. [FV] (`travaux/syn-sources.md:248`) | GianLuca accepte de décider par écrit | Canal de travail réel [IN] | Contrat-cadre (sections 8 et 11.4) |
| Mandat à 0 € jusqu'au socle récurrent ; puis liste fermée, 500 / 1 500 € HT | Règles du mandat (art. 1988, 1989, 1156 C. civ.) [FV] ; grille du 29 oct. [PR] | Le client accepte de payer lui-même toutes ses dépenses | Liste des entités et budgets [IN] | Livrable 4 du cadrage ; mandat par entité |
| Ajouter la colonne « qui assume » et les actes R2, R5, R7, R12, R14, R16, R17 | Demande de Morgan (`travaux/DEMANDE.md:46`) ; table de la stratégie sans cette colonne [FV] | Les rôles RGPD seront ceux retenus [HY] | Rôles non tranchés par un avocat | Accord écrit des associés, puis contrat-cadre |
| Séparer livraison payée et livraison réussie | Correction C7 de la stratégie [FV] (`travaux/strategie-retenue.md:113`) | L'usage se mesure dans le canal du client | Aucune équipe connue [IN] | Critères d'usage écrits à chaque bon de commande |
| Seize principes confiés à l'avocat avant le premier bon de commande | Clauses du 2 nov. incomplètes ou contradictoires [FV] (`interne/offre-marwin-tech-remuneration-et-collaboration.md:204-213`) | Coût de l'avocat dans l'apport de 8 000 à 14 000 € [ES] | Points [HY] non vérifiés dans les textes | Condition n° 7 (`travaux/strategie-retenue.md:666`) |
| Plancher au plafond de responsabilité | Art. 1170 C. civ. [FV] | Le plafond assuré le permet | Aucun devis d'assurance [IN] | Écart, section 11.14 |
| Délai de 7 jours appliqué par prudence | L221-3 C. consom. [FV] | Le contrat de Marwin peut être hors établissement [HY] | Définition non relue par l'audit | Écart, section 11.6 |
| Aucune rétention technique en cas d'impayé | Comptes au nom du client [PR] ; données toujours restituables [PR] | Les recours contractuels suffisent | Exposition ≤ 6 000 € HT environ [ES] | Contrat-cadre (section 12.1) |
| Remettre sans céder ; licence qui permet la maintenance par un tiers | Art. L131-1 à L131-3 CPI [FV] ; promesse du diaporama inexacte [FV] | Les composants génériques se distinguent au bon de commande | Propriété du CRM non réglée [IN] | Annexe des droits ; pacte avant tout lot CRM |
| Démarrage par étapes, chacune avec sa preuve | Dix conditions de la stratégie [PR] ; fuite non traitée [ES] | Un rendez-vous peut être obtenu avant le 15 déc. | Aucun rendez-vous fixé [FV] (`travaux/note-point-4-novembre-et-activites.md:5`) | Décisions n° 1 à 5 (`travaux/strategie-retenue.md:713-719`) |

---

## 17. Questions à soumettre

Les questions déjà posées dans 10-structures-et-relations.md (section 19) ne sont pas répétées. Celles-ci les complètent.

**À l'avocat en contrats**
1. Comment rédiger « solde exigible sans réserve motivée sous 10 jours ouvrés » sans que ce mécanisme vaille acceptation du livrable ni approbation d'une suite ?
2. Plafond de responsabilité : la formule « le plus élevé des honoraires des douze derniers mois et du prix du bon de commande, sous le plafond assuré » tient-elle au regard de l'art. 1170 ?
3. Mandat de dépense par entité : forme, liste des actes, plafonds ; comment le rendre visible aux fournisseurs pour éviter un mandat apparent ; responsabilité de Marwin envers les tiers.
4. Licence sur les composants génériques : rédaction qui permet la maintenance par un tiers choisi par le client, sans revente ni diffusion.
5. Arrêt d'un lot à la demande du client : calcul de ce qui reste dû (jalons ou JP relevées).
6. Impayé : usage par le client de livrables non payés, déjà installés sur ses comptes ; recours sans rétention technique.
7. Rétractation : un contrat signé à distance juste après un rendez-vous chez le client reste-t-il « hors établissement » ?
8. Clause de règlement amiable préalable ; tribunal compétent.
9. Sous-traitance de Marwin : la loi de 1975 et le nouvel art. L8222-1-1 C. trav. peuvent-ils s'appliquer à une prestation intellectuelle ?
10. Durée de la confidentialité après la fin ; citation du client comme référence.

**À l'avocat ou au DPD en données personnelles (priorité absolue, avant toute proposition)**
11. Qui est responsable du traitement pour le fichier constitué du 22 au 30 oct. et exposé dans le dépôt public ? Faut-il notifier la CNIL, à partir de quelle date de connaissance, et faut-il informer les personnes (artistes, lignes personnelles) ? (`travaux/syn-droit.md:758-764`)
12. Dans quels termes informer GianLuca par écrit, sans reconnaissance de responsabilité non pesée ?
13. Délai contractuel d'information du responsable par Marwin en cas d'incident (24 h proposé) ; liste des sous-traitants ultérieurs à faire autoriser.

**À l'assureur ou au courtier**
14. La RC professionnelle couvre-t-elle les fautes de gestion d'un mandataire de dépense, les erreurs de sorties d'IA relues et les incidents de données ? Quel traitement pour l'incident déjà connu ?

---

## 18. Limites

- **Aucune parole directe de GianLuca Carlone** n'existe dans les pièces (`travaux/syn-sources.md:38`). Ce qu'il accepte de déléguer, les décisions qu'il garde, son canal de travail et ses équipes sont [IN]. Toutes les règles de ce livrable sont des propositions à discuter avec lui.
- **Aucune entité n'est identifiée** : les rôles RGPD, la vigilance, la rétractation et la forme des mandats en dépendent [IN].
- **Les points juridiques marqués [HY]** (rôles RGPD, application de L221-3 au contrat de Marwin, définition du hors établissement, plancher du plafond de responsabilité, qualification au sens du Data Act, effets d'une rétention technique) n'ont pas été tranchés par un avocat. Les textes ont été relevés et contrôlés le 4 nov. 2026 par l'audit ; je ne les ai pas rouverts.
- **La visibilité actuelle du dépôt FinanceScope/CRM-Carlone** et la date exacte de connaissance de la fuite n'ont pas été revérifiées par l'audit (`travaux/strategie-retenue.md:836`).
- **La collecte est incomplète** : 169 conversations ChatGPT lues sur 219 ; une promesse faite au client sur la délégation, le paiement ou la réversibilité peut exister hors du corpus (`travaux/strategie-retenue.md:835`).
- **Les seuils et délais proposés** (5, 10 et 15 jours ouvrés ; 500 et 1 500 € HT ; 24 h) sont des choix de gouvernance, pas des règles légales. Ils seront à ajuster après la mesure du pilote.
