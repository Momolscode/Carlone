# Registre des risques, des inconnues et des décisions

Audit Marwin Tech × GianLuca Carlone · livrable 14 sur 15 · 4 novembre 2026
Statut : interne (contient des probabilités, des rémunérations visées, l'apport des associés, leurs désaccords possibles et l'analyse de l'incident de données ; ne pas transmettre à GianLuca Carlone).
Sources principales : `travaux/strategie-retenue.md` (sections 0 à 3 et 10 à 16) ; `travaux/syn-sources.md` (sections d, e et h) ; `travaux/syn-portefeuille.md` (sections 1, 2 et 4) ; `travaux/syn-capacite-ia.md` (sections 1 à 4 et 8) ; `travaux/syn-droit.md` (sections 0 et 3 à 9) ; `modele-financier/stress-tests.md` ; `modele-financier/scenarios.md` ; `modele-financier/tresorerie-18-mois.md` ; `travaux/note-point-4-novembre-et-activites.md` ; pièces d'origine rouvertes en lecture seule dans le dépôt Momolscode/Carlone (commit 7b46602) : `interne/contexte-projet-carlone.md`, `interne/audit-marwin-tech-carlone.md`, `interne/offre-marwin-tech-remuneration-et-collaboration.md`, `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md`, `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md`, `crm/PASSATION.md`, `crm/docs/rapport/rapport-crm-hermes360.md`, `crm/art_merge.py`, `README.md`, `sources/reprise-59-et-visuels-2026-11-04.md` ; copie du 4 nov. du diaporama client « Offre Marwin Tech pour Carlone » (11 vues, hors dépôt).
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu. Sans autre précision, une [PR] vient de la stratégie retenue ; « [PR, ce livrable] » signale une règle ajoutée ici.

Conventions. **JP** : journée-personne de 7 h. Montants hors taxes (HT) sauf mention. Les codes d'offres (A cadrage, B0 socle pilote, B1 et B2 socles récurrents, C1 à C8 lots, D exploitation, E avenant) sont ceux de 04-catalogue-offres.md. Les numéros d'inconnues (U01 à U45) sont ceux de 02-etat-des-sources.md, section 6 ; les ajouts de ce livrable vont de U46 à U50. Les dates des jalons suivent 08-feuille-de-route.md (scénario central : mois 1 = janvier 2027). Les chemins `slides/…` et `deck.json` renvoient à la copie du 4 nov. du diaporama client, hors dépôt. Les textes officiels ont été consultés le 4 nov. 2026 par les chercheurs juridiques de l'audit et contrôlés le même jour ; je ne les ai pas rouverts moi-même.

---

## En bref

1. **Au 4 novembre, deux décisions seulement sont prises**, toutes deux par Morgan seul : le prénom du client et le retrait de Medhi et de BOJ.ART. Le retrait a été dit à l'oral et appliqué au seul diaporama en ligne [DR/FV] (`travaux/note-point-4-novembre-et-activites.md:25-26`). Aucun accord écrit n'existe entre les associés [FV négatif] (`travaux/syn-sources.md:326`). Tout le reste est à prendre.
2. **52 risques** sont inscrits, dans huit familles. **Onze** sont jugés à la fois probables et graves [HY]. Le plus urgent est la décision sur la notification à la CNIL, attendue le jeudi 5 novembre à une heure inconnue (R01).
3. **Une vingtaine de risques ont une échéance avant le 30 novembre et ne demandent rien au client.** Les plus pressants : R01 et R02 (5 nov.) ; R25 (immédiat) ; R42 (13 nov.) ; R17, R23, R24, R48 et R50 (19 nov.) ; R10 (20 nov.) ; R29 (30 nov.).
4. **Quatorze informations sont bloquantes.** Neuf dépendent de Morgan et de Mathys, avec leurs conseils, et pas du client : elles peuvent être réunies d'ici le 30 novembre. Cinq attendent le rendez-vous avec GianLuca, à tenir avant le 15 décembre (section 3.1).
5. **44 décisions sont suivies** : 2 prises, 21 à prendre par les associés, 5 à prendre par GianLuca ou son entité, 16 différées sur une règle écrite (section 4).
6. **En trésorerie, la meilleure protection n'est pas la réserve.** C'est la règle « pas de rémunération sans encaissement », qui ramène le besoin le plus lourd de 21 300 € à 1 700 € [ES] (`modele-financier/stress-tests.md:34, 340-341`).
7. **Deux écarts avec la stratégie retenue** : la probabilité que l'apport manque est relevée (R29) ; le revenu net en régime central est pris dans le modèle financier (R21, R32).

---

## 1. Comment lire et tenir ce registre

**Ce que ce livrable ajoute.** Pour chaque risque : niveaux, signal d'alerte, parade, propriétaire et échéance. Pour chaque inconnue listée dans 02-etat-des-sources.md : comment l'obtenir et à quelle date. Pour chaque décision : son statut au 4 novembre et la preuve attendue. Il ne recopie pas les seuils de saturation (06-fonctionnement-a-deux.md), les jalons datés (08-feuille-de-route.md, section 7), les signaux de suspension (12-gouvernance-contrat-sortie.md, section 15) ni les questions du rendez-vous (13-preparation-rendez-vous.md).

**Échelles.** Ce sont des jugements de l'audit [HY], pas des mesures.

| Niveau | Probabilité (sur les 12 prochains mois) | Impact |
| --- | --- | --- |
| Faible | Peu de chances | Moins d'environ 1 000 € ou 2 JP ; aucun effet sur la relation |
| Moyen | Aussi probable qu'improbable | Un jalon retardé ; quelques milliers d'euros ; une gêne dans la relation |
| Élevé | Plus probable qu'improbable, ou déjà en cours | Sanction possible ; perte du client ; besoin de financement ; blocage entre associés |

Un risque noté « X à Y » est placé au niveau le plus haut dans la carte (section 2.1). « Inconnue » veut dire que l'audit n'a pas de base pour juger.

**Propriétaire.** La personne qui surveille le signal et déclenche la parade. Ce n'est pas forcément la cause du risque.

**Statuts des décisions.** *Prise* : décision exprimée par la personne compétente, même à l'oral (alors codée [DR]). *À prendre* : décision attendue, avec une échéance. *Différée* : la stratégie retenue propose de ne pas la prendre avant une date ou une condition ; la règle de report elle-même est à écrire (D13 et D16).

**Tenue du registre [PR, ce livrable].**
- Morgan tient le registre ; Mathys le contrôle.
- Revue de 30 minutes chaque lundi jusqu'au 15 décembre 2026, puis au comité interne mensuel. Coût ≈ 0,5 JP par mois [ES].
- Un risque se ferme sur une preuve (capture datée, signature, attestation), jamais sur une impression.
- À chaque jalon de 08-feuille-de-route.md, la probabilité est remplacée par le fait observé (`travaux/strategie-retenue.md:502`).
- Rien de ce registre n'a été exécuté : aucune action, aucun contact, aucune dépense.

---

## 2. Registre des risques

### 2.1 Carte des risques

| Probabilité \ Impact | Élevé | Moyen | Faible |
| --- | --- | --- | --- |
| **Élevée** | R01, R04*, R05*, R10*, R15, R20, R23, R24, R29, R32, R50 | R06, R19, R25, R37, R42 | — |
| **Moyenne** | R07, R08, R09, R12, R16, R17, R30, R38, R41, R44, R45, R49, R52 | R02, R03, R18, R26, R27, R28, R31, R33, R34, R35, R36, R39, R40, R46, R47 | — |
| **Faible** | R11, R14, R51 | — | — |
| **Inconnue** | R21, R48 | R13, R43 | R22 |

\* Probabilité élevée **si aucune règle n'est appliquée** (données réelles traitées, campagne lancée, CRM utilisé en l'état). La parade fait tomber ces risques au niveau faible.

### 2.2 Données

| N° | Risque | Cause et source | Prob. | Impact | Signal d'alerte | Parade | Propriétaire | Échéance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R01 | La décision sur la notification à la CNIL n'est pas prise à temps, ou n'est pas documentée | Dépôt public FinanceScope/CRM-Carlone : ≈ 800 à 931 numéros et 206 e-mails [ES] (`travaux/syn-sources.md:511`) ; public le 4 nov. à 16 h 19 [DR] (`interne/contexte-projet-carlone.md:5, 11`) ; connu au plus tard le 2 nov. [FV] (`interne/audit-marwin-tech-carlone.md:3, 15`) ; responsable du traitement non désigné [IN] (`travaux/syn-droit.md:624`) | Élevée | Élevé | 5 nov. passé sans décision écrite ; dépôt encore public | Décision prise avec un avocat ou un DPD ; notification, échelonnée si le dossier est incomplet [HY], ou en retard motivée ; fiche de violation tenue dans tous les cas (`travaux/syn-droit.md:622-623`) | Mathys et Morgan | Jeu. 5 nov. 2026, heure inconnue |
| R02 | Le fichier reste exposé après le passage en privé | Dépôt public au moins depuis le dernier envoi du 30 oct. [DR] (`interne/contexte-projet-carlone.md:11`) ; GitHub ne retire pas les données des clones d'autres utilisateurs [FV] (`travaux/syn-droit.md:626`) ; autres copies : `crm/`, archives ZIP, artefacts (`travaux/syn-droit.md:627`) | Moyenne [IN : copies non vérifiées] | Moyen | Copie (fork) visible ; secret trouvé dans l'historique | Capture datée « privé » ; liste des copies ; secrets révoqués d'abord ; réécriture de l'historique seulement après coordination ; aucune copie dans un dépôt public | Mathys | Jeu. 5 nov. 2026 |
| R03 | L'information des personnes est due (art. 34) | Lignes 06 et 07, messageries grand public et fiches d'artistes dans le fichier ; risque élevé à examiner pour elles [HY] (`travaux/syn-droit.md:619, 625`) | Moyenne | Moyen | Avis du conseil qui conclut à un risque élevé | Décision écrite sur l'art. 34 ; si l'information est due, comptes du pilote commercial pris hors des fiches exposées (`travaux/strategie-retenue.md:311`) | Morgan (Mathys), avec le conseil | Jeu. 19 nov. 2026 au plus tard |
| R04 | Des données réelles sont traitées sans cadre | Aucun responsable du traitement, contrat de l'article 28 ni registre [FV] (`travaux/syn-droit.md:59`) ; Anthropic et OpenAI absents de la liste du Data Privacy Framework [MM] (`travaux/syn-droit.md:670`) ; abonnement ChatGPT Pro [DR] (`travaux/syn-droit.md:676`) | Élevée sans règle écrite | Élevé | Donnée d'un prospect ou du client collée dans un outil grand public ; essai lancé sur données réelles | Condition n° 10 de démarrage (`travaux/strategie-retenue.md:669`) ; démonstrateurs sur données fictives ; offres professionnelles avec clauses types et analyse d'impact des transferts | Mathys | Avant tout traitement réel (pas avant le pilote, 2027) |
| R05 | La prospection par le CRM n'est pas conforme | Opposition renseignée sur 33 fiches seulement [FV] (`travaux/syn-sources.md:510`) ; 24 standards en 06 ou 07 et 25 messageries grand public ; consentement préalable obligatoire vers les consommateurs depuis le 11 août 2026 [FV] (`travaux/syn-droit.md:642, 645`) ; structure vendeuse non nommée (`crm/PASSATION.md:31`) | Élevée si une campagne part en l'état | Élevé | Appel vers une ligne personnelle ; message sans le nom de la structure vendeuse ; plainte | Entreprises seulement ; tous les préalables du lot C2 (`travaux/strategie-retenue.md:311`) ; aucun appel avant | Entité vendeuse de GianLuca (responsable du traitement) ; Mathys pour l'outil | Avant le premier appel |
| R06 | L'assurance ne couvre pas l'incident déjà connu | Une assurance souscrite après coup ne couvre probablement pas un incident connu [HY] (`travaux/strategie-retenue.md:554`) | Élevée | Moyen | Questionnaire de l'assureur sur les incidents connus | Déclaration sincère de la fuite ; aucune couverture supposée pour cet incident ; conseil sur la fuite (1 000 à 3 000 € [HY]) compté dans l'apport | Morgan | Devis la semaine du 9 nov. ; souscription avant la première prestation |

La CNIL écrit : « En cas de doute, notifiez à la CNIL qui vous indiquera s'il est nécessaire d'informer les personnes » (https://cnil.fr/fr/services-en-ligne/notifier-une-violation-de-donnees-personnelles, consulté le 4 nov. 2026, cité dans `travaux/rj-R4-donnees-ia.md:243`). Pour le retrait des données d'un dépôt : https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository (consulté le 4 nov. 2026, cité dans `travaux/syn-droit.md:626`).

### 2.3 Juridique

| N° | Risque | Cause et source | Prob. | Impact | Signal d'alerte | Parade | Propriétaire | Échéance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R07 | Les associés s'engagent personnellement avant l'immatriculation | Marwin n'existe pas [DR] (`interne/offre-marwin-tech-remuneration-et-collaboration.md:153`) ; ceux qui agissent pour une société en formation en répondent solidairement et indéfiniment, sauf reprise [FV] (`travaux/syn-droit.md:276`) | Moyenne | Élevé | Demande de démarrer tout de suite ; idée de facturer par l'entreprise existante de Morgan ou d'encaisser sur un compte personnel | Rien n'est encaissé avant l'immatriculation ; au plus une signature au nom de « Marwin Tech, SAS en formation », avec un état des actes (`travaux/strategie-retenue.md:452, 458, 705`) | Morgan | Jusqu'à l'immatriculation |
| R08 | La relation est requalifiée en salariat | Indices : client unique, bureaux du client, prix au temps, « s'occuper de tout », salariat évoqué [HY] (`travaux/syn-droit.md:338-343`) ; condamnation publiable en ligne deux ans [FV] (`travaux/syn-droit.md:347`) | Faible à moyenne (`travaux/strategie-retenue.md:777`) | Élevé | Horaires imposés ; ordres directs ; place dans un organigramme ; exclusivité de fait (`travaux/strategie-retenue.md:683`) | Prix au livrable ou au périmètre ; pas de bureaux avant le bilan du mois 6 ; un rôle à la fois ; autres clients réels | Les deux, avec l'avocat en droit du travail | Comité mensuel ; bilan du 4 mai 2027 |
| R09 | Marwin exerce, par glissement, une activité réglementée | Le pilotage touche à la comptabilité, au conseil juridique, à la gestion immobilière, aux voyages, au recouvrement [HY fondé sur des textes FV] (`travaux/syn-droit.md:412-422`) ; « séjours des invités » au diaporama (`travaux/strategie-retenue.md:821`) | Moyenne | Élevé | Demande de tenir la comptabilité, rédiger un bail, réserver un séjour, relancer un débiteur | Liste d'exclusions dans chaque bon de commande ; Marwin prépare, le professionnel exécute (`travaux/strategie-retenue.md:650`) | Morgan | Dès le cadrage |
| R10 | Des arguments fiscaux faux partent vers des prospects | Simulateur du CRM à taux fixe de 25 % (`crm/art_merge.py:19, 129`) : jusqu'à 1 043 750 € affichés pour une entreprise, au plus ≈ 32 500 € par an en réalité [ES] (`travaux/syn-sources.md:512`) ; pièces faites à la machine très probablement exclues du 238 bis AB [HY] ; « mécénat » faux pour un achat d'œuvre [FV] (`travaux/syn-droit.md:568, 576`) | Élevée si le CRM sert en l'état | Élevé | Support ou e-mail qui chiffre une économie d'impôt ; mot « mécénat » | Simulateur retiré ou corrigé ; avis fiscal écrit avant le lot C2 ; chaque prospect renvoyé à son expert-comptable | Mathys (outil), Morgan (supports) | Ven. 20 nov. 2026 |
| R11 | Marwin devient intermédiaire de vente | Idée d'une rémunération sur les ventes [HY] (`travaux/syn-portefeuille.md:223`) ; obligations anti-blanchiment dès 10 000 € et droit de suite [FV] (`travaux/syn-droit.md:525-526`) | Faible si la règle est tenue | Élevé | Proposition de commission, d'encaissement, de garde ou de transport d'œuvres | Refus la première année ; dépôt-vente direct entre artistes et entité de GianLuca (`travaux/strategie-retenue.md:649`) | Morgan | Bilan annuel (4 nov. 2027) |
| R12 | Le client lit une promesse de résultat ; la responsabilité n'est pas bornée | « Six mois pour […] vendre vos œuvres avec le CRM » [FV] (`slides/proposition.html:3`) ; aucun contrat-cadre relu [FV négatif] | Moyenne | Élevé | Le client attend des ventes ou des rendez-vous ; projet de contrat sans plafond | Promesse retirée ; contrat-cadre relu : plafond lié aux honoraires, obligation de moyens, exclusion des dommages indirects (`travaux/strategie-retenue.md:557`) | Morgan, avec l'avocat | Documents au ven. 13 nov. ; contrat avant le premier bon de commande |
| R13 | La règle de rétractation s'applique au contrat de Marwin | Signature hors établissement avec une entité de 5 salariés au plus [HY] (`travaux/strategie-retenue.md:466` ; `travaux/syn-droit.md:530`) | Inconnue (effectif de l'entité [IN]) | Moyen | Entité de 5 salariés au plus ; signature prévue chez le client | Signature à distance, ou délai de 7 jours prévu au calendrier ; avis de l'avocat | Morgan | Avant le bon de commande |
| R14 | Un événement public ou une machine sont lancés sans cadre | Demande GN 6 au moins deux mois avant ; aucun événement public possible en décembre 2026 dans un lieu non autorisé [ES] ; qui assemble un bras devient fabricant [FV] (`travaux/syn-droit.md:532-533, 540`) | Faible depuis le report | Élevé | Date d'événement à moins de trois mois ; machine prévue devant le public | Format « signature » reporté sans date ; lot C3 sans robot, organisé par l'entité de GianLuca (`travaux/strategie-retenue.md:646`) | Morgan | À chaque demande d'événement |

### 2.4 Commercial

| N° | Risque | Cause et source | Prob. | Impact | Signal d'alerte | Parade | Propriétaire | Échéance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R15 | Le pilotage global n'est pas le besoin de GianLuca | Aucune parole directe du client [FV négatif] (`travaux/syn-sources.md:38`) ; « vingt jours » attribués au client (`sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:65`) puis à Morgan (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:7`) ; offre née du besoin du vendeur [DR] (`travaux/syn-portefeuille.md:156-162`) | Moyenne à élevée | Élevé | Refus de payer le cadrage ; un seul projet confié ; préférence pour embaucher ; aucun accès sous 10 jours (`travaux/syn-portefeuille.md:246-250`) | Cadrage payé, qui sert de test ; trois voies au choix ; réduire à un lot (`travaux/strategie-retenue.md:693-695`) | Morgan | Restitution du cadrage (février 2027 en central) |
| R16 | Personne ne paie | 0 contrat, 0 facture, 0 entité payeuse [FV] (`travaux/syn-sources.md:39`) ; aucun rendez-vous à l'agenda [DR] (`travaux/note-point-4-novembre-et-activites.md:5`) ; travail gratuit depuis le 18 oct. (`travaux/syn-portefeuille.md:304`) | Moyenne | Élevé | Pas de rendez-vous au 15 déc. ; pas d'acompte au 29 janv. | Dates butoirs ; report sans production (`travaux/strategie-retenue.md:697-698`) | Morgan | Mar. 15 déc. 2026 ; ven. 29 janv. 2027 |
| R17 | Des promesses déjà faites contredisent le parcours proposé | Ce que GianLuca a vu ou accepté est [IN] (`travaux/syn-sources.md:352`) ; le diaporama en ligne affiche 15 000 € et « Taux unique : 750 € HT » [FV] (`slides/formules.html:9, 30`) ; son envoi n'est pas tracé (`travaux/syn-sources.md:76`) | Faible à moyenne (`travaux/strategie-retenue.md:770`) | Moyen à élevé | Il cite 15 000 €, « vingt jours », 750 € ou une date de démarrage | Liste écrite, par Morgan, de ce qui a été remis (U04) ; message de recadrage avant tout rendez-vous ; 6 000 € HT pour le seul cadrage s'il a vu le taux (`travaux/strategie-retenue.md:231`) | Morgan | Jeu. 19 nov. 2026 |
| R18 | GianLuca voulait une équipe tout de suite et va voir ailleurs | Souhait de délégation rapporté [DR] (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:13`) | Moyenne (`travaux/strategie-retenue.md:769`) | Moyen | Réaction négative au cadrage ; demande de présence quotidienne | Montrer le pilotage comme suite ; accélérer s'il fournit entité, accès et acompte, toujours sous 10 JP (`travaux/strategie-retenue.md:60`) | Morgan | Rendez-vous |
| R19 | La voie « ventes d'œuvres » échoue | Structure vendeuse non nommée (`crm/PASSATION.md:31`) ; 283 numéros sur 471 « à confirmer » [FV] (`travaux/syn-sources.md:508`) ; aucun résultat d'appel versionné, suivi réel [IN] (`travaux/syn-sources.md:301`) ; œuvres disponibles [IN] | Élevée (`travaux/strategie-retenue.md:772`) | Moyen | Préalables du lot C2 non réunis au moment du choix | Ne pas vendre C2 sans ses préalables ; sinon voie « pilotage » ou « organisation interne » | Morgan | Choix de la voie (30 jours après la restitution) |
| R20 | Marwin dépend d'un seul client | Aucun autre client [FV négatif] ; OLSEN : 36 propositions préparées, aucune envoyée [DR] (`travaux/note-point-4-novembre-et-activites.md:9`) ; vente non démontrée (`travaux/syn-capacite-ia.md:97`) | Élevée | Élevé | Prospection sous 50 % du plancher deux mois de suite ; pas de second client au mois 9 | Plancher de prospection de 1,5 à 2,5 JP par mois ; dépendance assumée par écrit ; revenus extérieurs gardés (`travaux/strategie-retenue.md:522`) | Morgan | Mois 9 (sept. 2027 en central) ; cible ≤ 80 % au mois 18 |
| R21 | Une offre d'emploi détourne un associé de Marwin | Un poste de cadre rapporterait ≈ 3 400 € nets [MM] contre 1 100 à 1 500 € nets en central [ES] (`travaux/strategie-retenue.md:707` ; `modele-financier/scenarios.md:67`) ; intention du client non établie (`travaux/syn-sources.md:270`) | Inconnue | Élevé | Emploi proposé pendant la négociation, ou mêlé à la prestation | Pas avant le bilan du mois 6 ; décision séparée ; jamais pour les deux associés (`travaux/strategie-retenue.md:631, 707`) | Les deux | Bilan du 4 mai 2027 |
| R22 | L'aide régionale décale la signature | Dossier à déposer avant la signature ; échéance annoncée au 31 déc. 2026, « dans la limite des crédits » [DR] (`travaux/syn-droit.md:71` ; `travaux/strategie-retenue.md:239`) | Inconnue | Faible | GianLuca demande l'aide | Signature décalée, sans travailler ; cadrage jamais retardé pour une aide incertaine | Morgan | Rendez-vous ; 31 déc. 2026 |

### 2.5 Capacité

| N° | Risque | Cause et source | Prob. | Impact | Signal d'alerte | Parade | Propriétaire | Échéance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R23 | Les associés n'ont pas le temps promis | Morgan mène une dizaine d'autres projets [FV pour la liste] (`travaux/note-point-4-novembre-et-activites.md:13-17`) ; disponibilité de Mathys [IN] (`travaux/syn-capacite-ia.md:118`) ; 20 JP par mois = 78 à 83 % du temps des deux [ES] (`travaux/syn-capacite-ia.md:228`) | Élevée | Élevé | Fiche des disponibilités non signée au 19 nov. ; occupation > 85 % sur tout le temps | Plafond de 10 JP facturables par mois ; occupation mesurée sur tout le temps de chacun ; scénario prudent par défaut (`travaux/strategie-retenue.md:623, 840`) | Les deux | Jeu. 19 nov. 2026, puis chaque mois |
| R24 | Morgan devient le goulot | Relation, prix, validation de tout livrable et comptes des outils reposent sur lui (`travaux/syn-capacite-ia.md:73, 274`) | Élevée | Élevé | File de validation > 2 jours ouvrés (`travaux/syn-capacite-ia.md:295`) ; absence sans relais | Validation technique déléguée par écrit à Mathys ; coffre partagé des accès ; binôme de secours par processus | Morgan | Jeu. 19 nov. 2026 |
| R25 | Le travail gratuit continue | CRM, dossier du 21 oct., catalogue, études, STRATES et vernissage faits sans commande [FV négatif sur les factures] (`travaux/syn-portefeuille.md:304`) | Élevée | Moyen | Toute JP hors remise en ordre ; nouveau document pour le client sans bon de commande | Gel immédiat (`travaux/strategie-retenue.md:123`) ; relevé des JP de novembre | Morgan | Immédiate |
| R26 | La remise en ordre prend plus de temps que prévu | 9 à 17 JP non facturables sur les mois 0 à 2 [ES] (`travaux/syn-capacite-ia.md:220`) | Moyenne | Moyen | Jalons du 13 et du 20 nov. manqués | Rien d'autre en novembre ; ordre fixe : fuite, documents, associés, structure | Les deux | Lun. 30 nov. 2026 |
| R27 | Marwin glisse vers l'exécution | « Sans avoir à en gérer chaque détail » [DR] (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:13`) ; personne désignée côté client [IN] | Moyenne (`travaux/strategie-retenue.md:773`) | Moyen | Demandes administratives quotidiennes ; personne désignée 15 jours ouvrés après une livraison | Pas de reprise de l'exécution ; socle limité au pilotage (`travaux/strategie-retenue.md:337`) | Morgan | Dès le pilote |
| R28 | Un associé est absent plusieurs semaines | Deux personnes, sans relais ; capacité ramenée à 4 à 8 JP par mois [ES] (`travaux/syn-capacite-ia.md:865`) | Faible à moyenne | Moyen : perte de trésorerie de 9 000 € sans réaction, 4 300 € avec la règle [ES] (`modele-financier/stress-tests.md:39`) | Absence de plus de 10 jours ouvrés | Changement de palier sans pénalité ; procédures testées ; assurance homme-clé (`travaux/syn-droit.md:478`) | Les deux | Pacte (30 nov.) |

### 2.6 Trésorerie

| N° | Risque | Cause et source | Prob. | Impact | Signal d'alerte | Parade | Propriétaire | Échéance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R29 | L'apport n'est pas réuni, ou il est trop juste | Apport visé 8 000 à 14 000 € [ES] (`travaux/strategie-retenue.md:56`) ; avec 10 000 €, point bas de 3 100 € en déc. 2026, et 700 € ou 100 € si la RC est payée d'avance [ES] (`modele-financier/tresorerie-18-mois.md:25, 135`) ; domiciliation impayée (144 €) et abonnements en échec [DR] (`travaux/note-point-4-novembre-et-activites.md:6, 8`) | Moyenne à élevée (écart ci-dessous) | Élevé | Fonds non déposés au 30 nov. | Sorties de novembre limitées au conseil sur la fuite et aux statuts ; prime d'assurance fractionnée ; haut de la fourchette d'apport (`travaux/strategie-retenue.md:776`) | Les deux | Lun. 30 nov. 2026 |
| R30 | Le client arrête brutalement | Client unique ; probabilités de passage [HY] (`travaux/strategie-retenue.md:502`) | Moyenne | Élevé sans règle : besoin de 21 300 € (fin du pilote) ou 12 600 € (après un trimestre de socle) ; 1 700 € et 0 € avec la règle [ES] (`modele-financier/stress-tests.md:34-35`) | Critères d'adoption non tenus 4 semaines ; décisions en attente > 10 jours ouvrés | « Pas de rémunération sans encaissement » ; frais ramenés à ≈ 1 000 € ; préavis d'un mois ; remboursement de TVA demandé à temps (`modele-financier/stress-tests.md:341-342`) | Les deux | Mars 2027 (fin du pilote) ; juin 2027 (fin du premier trimestre de socle), en central |
| R31 | L'entité paie en retard | Pratiques de paiement [IN] (`travaux/strategie-retenue.md:467`) | Moyenne | Moyen : à 90 jours, besoin de 3 400 € sans réaction, 0 € avec suspension [ES] (`modele-financier/stress-tests.md:33`) | Échéance dépassée d'un jour | Relance le lendemain ; suspension 8 jours après la relance ; rémunération arrêtée ; aucun nouveau lot (`travaux/strategie-retenue.md:463, 528`) | Morgan | Dès la première facture |
| R32 | Le revenu des associés reste trop faible | Rien avant le mois 4, puis 1 100 à 1 500 € nets par associé en central [ES] (`modele-financier/scenarios.md:67`) | Élevée (`travaux/strategie-retenue.md:771`) | Élevé | Disponibilité réduite ; autres missions reprises sans déclaration | Revenus extérieurs gardés jusqu'au deuxième renouvellement du socle (`modele-financier/stress-tests.md:343`) | Les deux | Jeu. 19 nov. 2026 (rémunération acceptée par écrit) |
| R33 | Les coûts d'IA augmentent | Doublements de prix annoncés au 1er déc. 2026 et au 1er janv. 2027 chez un fournisseur (`travaux/strategie-retenue.md:532`) | Moyenne | Moyen avec la règle : perte de 16 000 € sur 18 mois sans réaction, 2 400 € avec [ES] (`modele-financier/stress-tests.md:38`) | Dépense mensuelle d'IA > 150 % du budget [PR, ce livrable] | Plafonds par tâche et coupure à 100 % ; deux fournisseurs ; clause de révision (`travaux/syn-capacite-ia.md:841`) | Mathys | Mar. 1er déc. 2026 |
| R34 | La TVA ou la facturation électronique sont mal tenues | TVA exigible à l'encaissement des acomptes ; franchise vite perdue ; réception des factures électroniques obligatoire depuis le 1er sept. 2026 [FV] (`travaux/syn-droit.md:297, 299-300`) | Moyenne | Moyen | Facture sans TVA ou sans les nouvelles mentions ; aucune plateforme choisie | TVA dès la première facture ; plateforme choisie à la création (`travaux/strategie-retenue.md:462`) | Morgan, avec l'expert-comptable | Immatriculation |
| R35 | Un lot dépasse son estimation | JP estimées [ES] ; données absentes ou contradictoires | Moyenne | Moyen : ≈ 2 000 à 2 750 € de temps non payé pour un lot de 6 000 € dépassé de 50 % [ES] (`travaux/strategie-retenue.md:531`) | 75 % des JP consommées au jalon intermédiaire [PR, ce livrable] | Provision de 10 à 15 % ; avenant signé avant le travail (`travaux/strategie-retenue.md:287`) | Associé responsable du lot | Chaque lot |

> **Écart avec la stratégie retenue (R29).** La stratégie note « L'apport n'existe pas » avec une probabilité moyenne [HY] (`travaux/strategie-retenue.md:776`). Ce registre la relève à « moyenne à élevée ». Deux raisons. D'abord, avec 10 000 € d'apport, le modèle laisse un point bas de 3 100 € en décembre 2026, puis 700 € ou 100 € seulement si la RC professionnelle est payée en une fois [ES] (`modele-financier/tresorerie-18-mois.md:25, 135`) : la marge est presque nulle. Ensuite, de petites sommes restent impayées depuis plusieurs semaines (144 € de domiciliation attendus depuis le 12 octobre, abonnements en échec depuis fin octobre) [DR] (`travaux/note-point-4-novembre-et-activites.md:6, 8`). Ces signaux concernent Morgan et ses autres activités. Ils ne disent rien de l'épargne de chacun ni de la situation de Mathys [IN]. La parade ne change pas. Ce qui change : le constat de l'apport passe avant toute dépense de statuts, et le 30 novembre devient un point d'arrêt (D17).

> **Écart avec la stratégie retenue (R21, R32).** La stratégie annonce 1 350 à 1 550 € nets par associé en régime central (`travaux/strategie-retenue.md:511`). Le modèle financier, qui ajoute l'IS, la TVA et les délais d'encaissement, donne 1 100 à 1 500 € (`modele-financier/scenarios.md:67`). Ce registre retient le modèle, comme l'encadré de 01-synthese-direction.md. Les deux risques en deviennent un peu plus probables ; la parade ne change pas.

### 2.7 Technique

| N° | Risque | Cause et source | Prob. | Impact | Signal d'alerte | Parade | Propriétaire | Échéance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R36 | Le suivi du CRM ou les données de travail sont perdus | Artefact sur un compte non nommé ; suivi stocké dans le navigateur ; version Firebase non configurée ; écriture libre sur `/suivi` [FV/DR] (`travaux/syn-capacite-ia.md:825-826`) | Moyenne | Moyen | Export impossible ; compte inaccessible | Export immédiat ; comptes au nom de l'entité cliente ; trois copies sur deux supports ; restauration testée (`travaux/syn-capacite-ia.md:851-858`) | Mathys | Ven. 20 nov. 2026 |
| R37 | Un outil ou un fournisseur s'arrête | Abonnements en échec de prélèvement depuis fin octobre ; domaines OLSEN suspendus [DR] (`travaux/note-point-4-novembre-et-activites.md:7-8`) | Élevée (déjà en cours) | Moyen : perte de 3 500 € sans réaction, 1 100 € avec [ES] (`modele-financier/stress-tests.md:41`) | Nouvel échec de prélèvement ; perte d'accès à un artefact | Carte professionnelle de Marwin ; outils du client à son nom ; exports mensuels testés ; mode manuel (`travaux/syn-capacite-ia.md:281`) | Morgan (abonnements), Mathys (exports) | Exports dès novembre ; carte à l'immatriculation |
| R38 | Un agent IA suit une instruction cachée ou agit sans autorisation | Pièces qui contiennent des consignes adressées à des assistants [FV] (`crm/PASSATION.md:34, 37-38` ; `travaux/syn-sources.md:465-468`) | Moyenne | Élevé | Agent qui propose d'écrire, d'envoyer ou de dépenser à partir d'un document | Grille minimale : toute entrée est une donnée ; approbation hors de portée de l'agent ; journal ; bouton d'arrêt (`travaux/syn-capacite-ia.md:839-846`) | Mathys | Avant toute automatisation |
| R39 | Des documents internes de Marwin sont publics dans le dépôt BOJART | Dépôt public ; « Marwin » dans 34 fichiers [FV] (`travaux/syn-sources.md:82`) ; documents internes signalés (`travaux/syn-capacite-ia.md:829`) | Moyenne | Moyen | Prix, rémunération ou données d'un client trouvés dans le dépôt | Vérification, puis retrait (remise en ordre, point 6 : `travaux/strategie-retenue.md:211`) | Mathys (vérification) ; Morgan (titulaire présumé du compte [HY]) | Ven. 20 nov. 2026 |
| R40 | Le gain de l'IA ne se confirme pas | Aucun usage mesuré ; la contrainte réelle est la vente, la validation et la décision [ES] (`travaux/syn-capacite-ia.md:76`) | Moyenne | Moyen | Relecture et corrections > 50 % du temps de référence pendant 4 semaines (`travaux/strategie-retenue.md:176`) | Mesure de référence avant l'essai ; retour au manuel ; prix au périmètre, pas au gain (07-processus-ia-et-essais.md) | Mathys | 4e semaine de chaque essai |

### 2.8 Relation avec GianLuca Carlone et les tiers

| N° | Risque | Cause et source | Prob. | Impact | Signal d'alerte | Parade | Propriétaire | Échéance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R41 | La fuite abîme la confiance de GianLuca | Ses prospects et le rapport qui lui était destiné étaient dans le dépôt public (`interne/contexte-projet-carlone.md:11`) | Moyenne (`travaux/strategie-retenue.md:774`) | Élevé | Il l'apprend par un tiers ; question sur la sécurité | Information écrite, dans des termes validés par le conseil, sans reconnaissance de responsabilité non pesée ; aucune donnée réelle avant les préalables | Morgan | Au plus tard avec le message de recadrage (ven. 27 nov.) |
| R42 | GianLuca détient des pièces contradictoires | Trois versions de l'offre ; retrait de Medhi appliqué au seul diaporama ; PDF de 13 pages sur la PR n° 1 [FV] (`travaux/syn-sources.md:40, 63-69`) | Élevée | Moyen | Il cite STRATES, le laboratoire ou l'option création | Une seule version ; pièces marquées « historique, retiré le [date] » ; PR n° 1 fermée ou PDF marqué ; diaporama corrigé (`travaux/strategie-retenue.md:802, 814-828`) | Morgan | Ven. 13 nov. 2026 |
| R43 | Une pièce remise porte l'ancien prénom | 433 occurrences dans les archives ; deux documents rédigés pour le client la portent : `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 1 et 5, et `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:9-11` [FV] (`travaux/syn-sources.md:43, 446`) | Inconnue (remise [IN]) | Faible à moyen | Pièce historique renvoyée ; nouveau texte tiré des archives | Aucune pièce historique renvoyée ; contrôle « 0 occurrence » avant chaque envoi ; correction sobre si une pièce erronée a été reçue (annexes/correction-identite.md) | Morgan | Avant chaque envoi |
| R44 | Les rôles de GianLuca se cumulent | Client, bailleur, employeur, investisseur, financeur de la recherche [DR] (`travaux/syn-portefeuille.md:308-318`) | Moyenne | Élevé | Bureaux, emploi ou capital proposés en même temps que les honoraires | Un rôle à la fois ; un accord par sujet (`travaux/strategie-retenue.md:627-632`) | Les deux | Bilan du 4 mai 2027 ; capital pas avant 12 à 24 mois |
| R45 | Le lien de Morgan avec BOJ.ART n'est pas déclaré | Morgan co-porte BOJ.ART et a rédigé le catalogue de vente de GianLuca [DR] (`travaux/syn-sources.md:325`) | Moyenne | Moyen à élevé | Recommandation qui touche Medhi ; GianLuca découvre le lien seul | Déclaration écrite dès le premier document remis ; abstention sur tout ce qui concerne Medhi (`travaux/strategie-retenue.md:635`) | Morgan | Message de recadrage (ven. 27 nov.) |
| R46 | Medhi n'est pas informé et revendique | Retrait dit à l'oral, non formalisé avec Medhi [DR] (`travaux/note-point-4-novembre-et-activites.md:25`) ; Medhi informé ou non [IN] ; exclusivité de vente et usage des films promis à la galerie (`interne/offre-marwin-tech-remuneration-et-collaboration.md:94`) | Moyenne | Moyen | Medhi évoque STRATES, le vernissage ou Jarvis comme acquis | Décision écrite des deux ; message écrit à Medhi ; dépôt-vente direct si la galerie veut ses pièces (`travaux/strategie-retenue.md:643`) | Morgan | Jeu. 19 nov. 2026 |
| R47 | GianLuca ne répond pas ; les décisions bloquent | Toutes les décisions passent par lui ; aucun délégué connu (`travaux/syn-capacite-ia.md:276`) | Moyenne | Moyen | Décision en attente > 5 jours ouvrés ; deux décisions bloquantes > 15 jours ouvrés | L'engagement attend ; jalons reportés ; revue du contrat (`travaux/strategie-retenue.md:603`) | Morgan | Dès le cadrage |

### 2.9 Associés

| N° | Risque | Cause et source | Prob. | Impact | Signal d'alerte | Parade | Propriétaire | Échéance |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R48 | Mathys n'approuve pas | Décisions du 4 nov. non partagées avec lui ; aucun accord écrit (`travaux/syn-sources.md:326`) | Inconnue | Élevé | Fiche non signée au 19 nov. | Rien n'est proposé au client tant que le désaccord dure ; médiation (`travaux/strategie-retenue.md:614`) | Les deux | Jeu. 19 nov. 2026 |
| R49 | Les associés se bloquent à 50/50, ou leurs temps divergent | Parts et dirigeants non arrêtés (`travaux/syn-droit.md:454`) ; Morgan porte seul 6 des 12 solutions de l'audit du 2 nov. (`travaux/syn-sources.md:327`) | Moyenne | Élevé | Décision d'unanimité sans accord après deux semaines [PR, ce livrable] ; écart de temps non compensé | Statuts et pacte avant le contrat client : liste d'unanimité, médiation, tiers expert, offre alternative ; rémunération liée au temps (`travaux/strategie-retenue.md:548, 550, 619`) | Les deux, avec l'avocat | Prêts au 30 nov. ; signés avant le premier bon de commande |
| R50 | La propriété du CRM et de Jarvis reste floue | « Le code, les données et le suivi restent chez les associés » (`crm/docs/rapport/rapport-crm-hermes360.md:19`) ; dépôt « de Mathys » (`README.md:35`) ; aucune licence sur Jarvis (`travaux/syn-sources.md:290`) ; réversibilité promise inexacte (`travaux/syn-droit.md:505`) | Élevée | Élevé | Lot CRM demandé avant l'inventaire ; nom « Jarvis » dans un document client | Inventaire daté au pacte ; licence à Marwin par défaut ; régime écrit du CRM « offert » avant tout lot CRM (`travaux/strategie-retenue.md:385, 619`) | Les deux | Principe au 19 nov. ; inventaire au pacte |
| R51 | Un associé part ou devient indisponible durablement ; les accès restent personnels | Artefacts et pages sur les comptes de Morgan ; CRM sur le compte « de Mathys » (`travaux/syn-capacite-ia.md:274-275`) | Faible | Élevé | Un seul administrateur pour un outil | Coffre partagé ; deux administrateurs ; clauses de départ et d'incapacité ; assurance homme-clé (`travaux/syn-droit.md:477-478`) | Les deux | Pacte |
| R52 | Les données de GianLuca servent à la prospection propre | Revente d'un CRM « clé en main » envisagée (`travaux/syn-sources.md:294`) ; activité OLSEN de Morgan (`travaux/note-point-4-novembre-et-activites.md:9`) | Faible à moyenne | Élevé | Fichier ou script du CRM réutilisé ailleurs | Clause de non-réutilisation au pacte ; kit vendu à d'autres sur des composants génériques seulement (`travaux/strategie-retenue.md:619`) | Les deux | Pacte |

---

## 3. Registre des informations inconnues

La liste et la classification viennent de 02-etat-des-sources.md, section 6, sur la base de `travaux/syn-sources.md:343-392`. Ce registre ajoute la manière d'obtenir chaque réponse, la date visée et ce qu'elle bloque. Aucune réponse ne doit être devinée : tant qu'une inconnue bloquante reste ouverte, la décision liée attend.

### 3.1 Bloquantes (14)

**Ce que Morgan et Mathys peuvent obtenir sans le client, avec leurs conseils (9).**

| N° | Information inconnue | Qui peut répondre | Comment l'obtenir | Date visée | Ce qu'elle bloque |
| --- | --- | --- | --- | --- | --- |
| U08 | Dépôt FinanceScope/CRM-Carlone : encore public ? qui contrôle l'organisation ? date exacte de connaissance ? copies ? responsable du traitement ? | Mathys et Morgan ; avocat ou DPD | Mathys ouvre les réglages et la liste des copies ; capture datée ; les deux écrivent la date à laquelle ils ont su ; consultation écrite du conseil | Jeu. 5 nov. 2026 | D03, D04 ; tout usage de données |
| U04 | Ce que GianLuca a vu, reçu ou accepté : version à quatre jours, lettre du 29 oct., PDF des options du 30 oct., diaporama de 13 ou de 11 vues, taux de 750 €, rapport CRM, vernissage | Morgan | Liste écrite pièce par pièce, tirée de la messagerie, des messageries instantanées et des rendez-vous ; recherche dans l'export ChatGPT (U25) | Jeu. 19 nov. 2026 | D14 |
| U06 | Disponibilité nominative (JP par mois, de décembre 2026 à juin 2027) ; situation de Mathys ; projets que Morgan suspend | Morgan ; Mathys | Fiche « rôles et disponibilités », agendas en regard | Jeu. 19 nov. 2026 | D09 ; dimensionnement de toute offre |
| U07 | Accord de Mathys sur la stratégie, le retrait de Medhi, la SAS et le régime du CRM | Mathys | Lecture de 01-synthese-direction.md et de ce registre ; signature | Jeu. 19 nov. 2026 | D11 ; tout envoi au client |
| U10 | Portée du retrait de Medhi ; ce qui lui a été promis ; Medhi et Mathys informés ? | Morgan | Décision écrite des deux ; liste, par Morgan, de ce qui a été dit à Medhi | Jeu. 19 nov. 2026 | D10 |
| U19 | Rémunération cible acceptée par chacun (avant ou après impôt) | Morgan ; Mathys | Discussion chiffrée avec 09-modele-economique-tresorerie.md | Jeu. 19 nov. 2026 | D09 |
| U09 | Propriété du CRM (code, fiches, suivi) et régime vis-à-vis du client | Morgan et Mathys, puis GianLuca | Inventaire daté des actifs au pacte ; régime proposé au client pendant le cadrage | 19 nov. (principe) ; cadrage | D12 ; tout lot CRM |
| U42 | Apport que chacun peut déposer ; capacité à vivre 3 à 4 mois sans rémunération de Marwin | Morgan ; Mathys | Relevé des fonds de chacun ; dépôt sur un compte de la société en formation | Lun. 30 nov. 2026 | D17 ; D22 |
| U05 | Structure qui facture : forme, date d'immatriculation, régime de TVA | Morgan et Mathys, avec l'expert-comptable | Rendez-vous avec l'expert-comptable ; simulation officielle (U47) | Lun. 30 nov. 2026 | D15, D22 |

**Ce qui attend GianLuca (5).** Les questions sont rédigées dans 13-preparation-rendez-vous.md.

| N° | Information inconnue | Qui peut répondre | Comment l'obtenir | Date visée | Ce qu'elle bloque |
| --- | --- | --- | --- | --- | --- |
| U01 | Entité : dénomination, SIREN, signataire habilité, valideur, effectif | GianLuca ou son expert-comptable | Question au rendez-vous ; puis registres publics, sans contact (U45) | Mar. 15 déc. 2026 | D24, D26 ; bon de commande |
| U02 | Besoin réel ; décisions qu'il garde ; origine et unité des « vingt jours » | GianLuca ; Morgan pour ce qu'il a entendu | Question au rendez-vous ; entretiens du cadrage | Rendez-vous ; restitution du cadrage | D28 |
| U03 | Budget, mode et délai de paiement ; TVA récupérée ou non ; intérêt pour l'aide régionale | GianLuca, avec son expert-comptable | Question au rendez-vous | Avant le 15 déc. | D25, D26 ; R31 |
| U41 | Personne qui exécutera au quotidien ; accès ; canal de travail | GianLuca | Question au rendez-vous | Rendez-vous ; accès sous 10 jours ouvrés après l'acompte | Démarrage du cadrage |
| U11 | Structure qui vend les œuvres | GianLuca | Question au rendez-vous | Avant le choix de la voie « ventes d'œuvres » | D27 ; lot C2 |

### 3.2 Importantes

| N° | Information inconnue | Qui peut répondre | Comment l'obtenir | Date visée | Lien |
| --- | --- | --- | --- | --- | --- |
| U43 | RC professionnelle : couverture IA, cyber et données ; traitement d'un incident connu ; prime | Assureur ou courtier | Deux devis, fuite déclarée | Devis semaine du 9 nov. ; souscription avant la première prestation | D19 ; R06, R29 |
| U46 *(ajout)* | Points juridiques [HY] non tranchés : rôles RGPD, notification échelonnée, art. 34, rétractation appliquée au contrat de Marwin, rôle de déployeur ou de fournisseur au sens du règlement sur l'IA | Avocat ou DPD ; avocat en contrats | Consultation écrite sur les questions de `travaux/syn-droit.md:747-764` | 5 nov. (notification) ; 19 nov. (rôles, art. 34) ; avant le bon de commande (contrat) | D03, D08, D21 |
| U47 *(ajout)* | Simulations officielles SAS et SARL ; coût réel d'un dirigeant rémunéré ; dates de création et de clôture ; CFE | Expert-comptable | Simulateur officiel de l'Urssaf, avec les questions de `travaux/syn-droit.md:705-729` | Lun. 30 nov. 2026 | D15 |
| U44 | Lieu de résidence des associés (déplacements) | Morgan ; Mathys | Fiche « rôles et disponibilités » | 19 nov. | Prix du cadrage, trajets compris |
| U27 | Coût complet d'une JP ; frais réels ; abonnements d'IA | Morgan ; Mathys ; expert-comptable | Relevés bancaires ; devis ; budget de 09-modele-economique-tresorerie.md | 30 nov. ; révision au mois 6 | D40 ; R33 |
| U22 | OLSEN et entreprise à domiciliation résiliée : forme, SIRET, TVA | Morgan | Avis de situation au répertoire SIRENE ; extrait K-bis | 30 nov. | D15 (risque d'« extension » d'une activité existante, `travaux/syn-droit.md:283`) |
| U20 | Situations personnelles : ACRE, ARE, ARCE, foyers fiscaux | Morgan ; Mathys ; expert-comptable ; France Travail | Rendez-vous individuels | 30 nov. | D15 ; R32 |
| U21 | Associés et capital : Eaglemic, parts, apports ; « Matisse » désigne-t-il Mathys ? | Morgan ; Mathys | Déclaration écrite avant les statuts | 30 nov. | D16 |
| U14 | Usage réel du CRM : suivi, appels passés, version utilisée | Morgan ; Mathys | Export de la collection « suivi » ; comptage des appels | 20 nov. | D18, D27 |
| U30 | Qui maintient le CRM depuis le 30 oct., avec quel budget | Morgan ; Mathys ; GianLuca | Constat interne ; décision sur le CRM au cadrage | Cadrage | D27 |
| U24 | Conformité de la prospection : oppositions, lignes mobiles, information des personnes | Avocat ou DPD | Vérification des oppositions sur toutes les fiches ; consultation | Avant tout appel | R05 ; lot C2 |
| U15 | Titulaire et licence du code de Jarvis ; disponibilité du nom | Morgan ; Medhi ; Mathys | Inventaire des composants et des licences ; recherche d'antériorité du nom | Pacte (30 nov.) | D12, D36 |
| U16 | Propriétaire du parc d'impression et de la tour de calcul | Morgan ; Medhi | Liste écrite | Avant toute promesse de matériel | D33, D34 |
| U17 | Rendez-vous du 22 oct. et rendez-vous « argent et rémunération » : tenus ? contenu ? | Morgan | Messagerie ; agenda | 19 nov. | U04 ; D14 |
| U25 | Contenu des 50 conversations ChatGPT non lues (`sources/reprise-59-et-visuels-2026-11-04.md:13-14`) | Morgan | Export intégral du compte ; recherche par mots (Carlone, prix, jours, engagement) | Ven. 27 nov. 2026 | U04 ; R17 |
| U28 | Console « marwin-control-room » : accès et données exposées | Morgan | Ouverture par Morgan ; liste des accès | Ven. 13 nov. 2026 | R02, R39 |
| U12 | Lieux : propriétaire, exploitant, stade d'acquisition, usage | GianLuca | Inventaire du cadrage ; actes et extraits fournis par lui | Restitution du cadrage | Lots C3, C4, C7 |
| U13 | Quali Contact : contrat, payeur, logiciel, format ; qui appelle | GianLuca | Question au rendez-vous ; copie du devis et modèle de fichier | Choix de la voie | Lots C2, C5 |
| U18 | Bureaux, salariat, investissement : réalité et termes | GianLuca | Écouter s'il en parle, sans ouvrir la négociation (`travaux/strategie-retenue.md:707`) | Bilan du 4 mai 2027 | D30 à D32 |
| U23 | Validation fiscale : œuvres exposées chez le vendeur, pièces faites à la machine, TVA des ventes | Avocat fiscaliste ou expert-comptable de GianLuca | Avis écrit ; rescrit sur une pièce précise | Avant le lot C2 | R10 ; lots C2, C8 |
| U26 | Nom complet et état civil du client | GianLuca | Au bon de commande | Bon de commande | D01 ; contrat |
| U45 | Solvabilité de l'entité | Marwin, une fois U01 connue | Registres publics, sans contact | Avant le bon de commande | D26 |
| U48 *(ajout)* | Éligibilité à l'aide régionale (entité cliente ; prestataire nouveau) ; crédits restants | GianLuca et son expert-comptable ; Région | Démarche de l'entité auprès de la Région | Avant toute signature ; 31 déc. 2026 | D25 ; R22 |

### 3.3 Secondaires

| N° | Information inconnue | Qui | Comment | Date visée |
| --- | --- | --- | --- | --- |
| U29 | Rappels et veille ChatGPT encore actifs | Morgan | Liste des tâches planifiées du compte | 13 nov. |
| U31 | Visuels originaux ; le quatrième a-t-il été montré au client ? | Morgan | Bibliothèque ChatGPT | Avant le rendez-vous |
| U32 | Sens de « ( 10 millions » (`interne/contexte-projet-carlone.md:129`) | Morgan | Question directe | 19 nov. |
| U33 | Versions 1 à 4 du PDF du 30 oct. ; version à quatre jours (importante si le client les a vues) | Morgan | Export ChatGPT (U25) | 27 nov. |
| U34 | Format de STRATES | Morgan ; Medhi | — | Sans objet tant que le projet est gelé |
| U35 | Orthographe de Medhi | Medhi | Message du 19 nov. | 19 nov. |
| U36 | Historique du CRM avant le 27 oct. ; envois après le commit b53a81c | Mathys | Journal du dépôt d'origine | 20 nov. |
| U37 | Éclosion est-il destiné au client ? | Morgan | Question directe | Sans objet tant que le projet est gelé |
| U38 | Origine de l'erreur sur le prénom | Morgan | Mémoire de l'assistant ChatGPT | Pas de date |
| U39 | Auteur et date du rapport « Fusion des univers » | Morgan | — | Pas de date |
| U49 *(ajout)* | État de la PR n° 1 : ouverte, fusionnée ou fermée ? | Morgan | Page de la PR sur GitHub | 13 nov. |
| U50 *(ajout)* | Délai d'obtention d'une attestation de vigilance pour une société nouvelle | Urssaf | Espace en ligne, après l'immatriculation | Immatriculation |

---

## 4. Registre des décisions

Aucune décision de la stratégie retenue n'est prise : elle le dit elle-même (`travaux/strategie-retenue.md:19`). Les jalons datés, avec leurs pièces et leurs suites « si oui, si non », sont dans 08-feuille-de-route.md, section 7.1. Ce registre donne le statut de chaque décision au 4 novembre et la preuve qui permettra de la déclarer prise.

### 4.1 Décisions prises

| N° | Décision | Qui | Date | Statut au 4 nov. | Ce qui reste ouvert | Preuve attendue |
| --- | --- | --- | --- | --- | --- | --- |
| D01 | Le client s'appelle **GianLuca Carlone**. Les anciennes graphies restent intactes dans les pièces historiques et servent d'alias de recherche | Morgan | 4 nov. 2026 | **Prise** [DR] (`travaux/DEMANDE.md:8` ; `travaux/note-point-4-novembre-et-activites.md:26`) | Nom complet et état civil pour le contrat (U26) ; correction tracée (annexes/correction-identite.md) | 0 occurrence de l'ancien prénom dans tout document remis ; pièces historiques non réécrites |
| D02 | Retirer Medhi et BOJ.ART de l'offre | Morgan seul, à l'oral | 4 nov. 2026 | **Prise oralement** [DR] (`travaux/note-point-4-novembre-et-activites.md:25`) ; appliquée au seul diaporama en ligne, passé à 11 vues [FV] (`deck.json:7`) | Portée [IN] ; accord de Mathys [IN] ; Medhi non informé [IN] ; offre écrite, STRATES v1.1, vernissage et PDF de 13 pages non corrigés [FV] (`travaux/strategie-retenue.md:31`) | Décision écrite des deux (D10) ; message à Medhi ; pièces marquées « historique » (D07) |

### 4.2 Présentées comme décidées, mais qui ne le sont pas

Une version récente n'est pas une décision approuvée (`travaux/DEMANDE.md`, section 1).

| Ce que disent les pièces | Source | Pourquoi ce n'est pas une décision | Où la décision est suivie |
| --- | --- | --- | --- |
| « SARL à l'IS par défaut, SAS si Carlone entre au capital » | `interne/contexte-projet-carlone.md:12` | Référence « provisoire » du 30 oct., sans validation professionnelle (`travaux/syn-droit.md:44`) | D15 |
| GianLuca « envisage une disponibilité de vingt jours par mois » | `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:65` | Le même brief l'attribue à Morgan (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:7`) | U02 |
| Offre de six mois à 15 000 ou 30 000 € HT ; « Taux unique : 750 € HT » | `interne/offre-marwin-tech-remuneration-et-collaboration.md:13-19` ; `slides/formules.html:30` | « En vigueur » en ligne, jamais validée ni signée (`travaux/syn-sources.md:40, 76`) | D06 |
| « Sans réponse dans ce délai, le livrable est réputé accepté » | `interne/offre-marwin-tech-remuneration-et-collaboration.md:206` | Contredit par « une absence de réponse ne vaut pas approbation » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:103`) | D21 |
| Mois 2 à 6 « payés d'avance, en début de mois » | `interne/offre-marwin-tech-remuneration-et-collaboration.md:19` | Contredit par « règlement sous sept jours après facture de fin de mois » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:57`) | D21 (paiement selon la nature de la prestation) |
| CRM « offert à ce jour » | `interne/offre-marwin-tech-remuneration-et-collaboration.md:227` | Conseil donné à Morgan ; régime jamais écrit (`travaux/syn-sources.md:267`) | D12 |

### 4.3 À prendre par Morgan et Mathys

| N° | Décision | Qui décide (avec l'avis de) | Échéance | Statut au 4 nov. | Preuve attendue | Liens |
| --- | --- | --- | --- | --- | --- | --- |
| D03 | Notifier ou non la CNIL, et comment (échelonnée, ou en retard motivée) | Le responsable du traitement [IN] ; en pratique Mathys et Morgan s'ils sont responsables de fait [HY] (`travaux/syn-droit.md:597`), avec l'avocat ou le DPD | Jeu. 5 nov. 2026, heure inconnue | À prendre | Décision datée et motivée ; fiche de violation ; accusé de la CNIL si notification | R01 ; U08, U46 |
| D04 | Rendre le dépôt privé ; contrôler les copies ; révoquer les secrets | Mathys, s'il contrôle l'organisation FinanceScope [IN] | Jeu. 5 nov. 2026 | À prendre | Capture datée « privé » ; liste des copies ; journal des révocations | R01, R02 |
| D05 | Arrêter toute production non commandée | Les deux | Immédiate | À prendre | 0 JP hors remise en ordre au relevé de novembre | R25 |
| D06 | Remplacer l'offre de six mois par le seul cadrage ; retirer formules, taux affiché, « ancre », laboratoire, option création | Morgan, validé par Mathys | Ven. 13 nov. 2026 | À prendre | Une seule version de l'offre ; 0 mention interdite (`travaux/strategie-retenue.md:661`) | R12, R17, R42 |
| D07 | Sort des pièces en circulation : PR n° 1 fermée ou PDF marqué « historique » ; offre écrite, STRATES v1.1 et vernissage marqués « retiré le [date] » ; diaporama corrigé | Morgan | Ven. 13 nov. 2026 | À prendre | Liste datée des pièces marquées ; corrections de `travaux/strategie-retenue.md:814-828` faites | R42 ; U49 |
| D08 | Information des personnes (art. 34) ; texte d'information de GianLuca | Le responsable du traitement, avec le conseil | Jeu. 19 nov. 2026 au plus tard | À prendre | Texte validé par écrit par le conseil | R03, R41 |
| D09 | Fiche « rôles et disponibilités » : JP par mois et par associé (au moins 6 facturables à deux), projets que Morgan suspend, délégation de la validation technique à Mathys, rémunération cible | Les deux | Jeu. 19 nov. 2026 | À prendre | Fiche signée | R23, R24, R32 ; U06, U19, U44 |
| D10 | Portée du retrait de Medhi ; message écrit à Medhi | Les deux ; envoi par Morgan | Jeu. 19 nov. 2026 | À prendre (formalise D02) | Décision signée ; message envoyé | R46 ; U10 |
| D11 | Accord de Mathys sur la stratégie retenue | Mathys | Jeu. 19 nov. 2026 | À prendre | Signature | R48 ; U07 |
| D12 | Principe du régime du CRM et de Jarvis entre associés (licence à Marwin par défaut) | Les deux | 19 nov. (principe) ; inventaire au pacte | À prendre | Inventaire daté des actifs | R50 ; U09, U15 |
| D13 | Garde-fous : 15 déc. et 31 janv. ; plafond de 10 JP facturables par mois ; occupation ≤ 85 % sur tout le temps ; plancher de prospection ; refus listés (`travaux/strategie-retenue.md:703`) | Les deux | Jeu. 19 nov. 2026 | À prendre | Règles inscrites dans ce registre, puis au pacte | R16, R20, R23 |
| D14 | Envoyer le message de recadrage et la proposition de cadrage (pour-gianluca/message-de-recadrage.md ; pour-gianluca/proposition-de-cadrage.md) ; demander le rendez-vous | Morgan, validé par Mathys | Signés le 19 nov. ; envoyés au plus tard le ven. 27 nov. | À prendre ; conditionnée à D03, D06, D07, D09 à D11 | Message signé des deux et envoyé ; lien de Morgan avec BOJ.ART déclaré | R17, R41, R45 ; U04 |
| D15 | Forme : SAS à l'IS, président et directeur général, capital entièrement libéré | Les deux, avec l'expert-comptable | Lun. 30 nov. 2026 | À prendre | Simulation officielle ; projet de statuts | U05, U20, U22, U47 |
| D16 | Statuts et pacte prêts ; pacte signé avant tout contrat client | Les deux, avec l'avocat | Prêts au 30 nov. ; pacte signé avant le premier bon de commande | À prendre | Projets ; puis pacte signé | R49, R51, R52 ; U21 |
| D17 | Apport réuni (8 000 à 14 000 €) | Les deux | Lun. 30 nov. 2026 | À prendre | Fonds disponibles | R29 ; U42 |
| D18 | CRM : hébergement privé, oppositions appliquées, simulateur fiscal retiré ou corrigé ; dépôt BOJART vérifié | Mathys | Ven. 20 nov. 2026 | À prendre | Constat daté des quatre points | R10, R36, R39 ; U14 |
| D19 | RC professionnelle avec volets IA, cyber et données, fuite déclarée | Morgan | Devis la semaine du 9 nov. ; souscription avant la première prestation | À prendre | Attestation d'assurance | R06 ; U43 |
| D20 | Garder des revenus extérieurs et écrire « pas de rémunération sans encaissement » | Chaque associé ; les deux pour la règle | Jeu. 19 nov. (engagement) ; pacte | À prendre | Règle au pacte ; déclaration des autres activités | R30, R32 |
| D21 | Contrat-cadre relu : plafond de responsabilité, livraison et adoption séparées, mandat de dépense, rétractation, silence, paiement selon la nature | Les deux, avec l'avocat | Avant le premier bon de commande | À prendre | Version relue par l'avocat | R12, R13 ; U46 |
| D22 | Immatriculer | Les deux | À l'engagement écrit d'une entité identifiée : au plus tôt début décembre (scénario ambitieux) ; fin décembre ou début janvier en central [HY] (`travaux/strategie-retenue.md:500` ; `modele-financier/tresorerie-18-mois.md:24`) | À prendre, sous condition | K-bis ou accusé de réception ; compte professionnel ; plateforme de factures | R07, R34 ; U05, U42 |
| D23 | Constater les dates butoirs : entité et rendez-vous au 15 déc. ; cadrage commandé et payé au 31 janv. 2027, un dimanche, donc en pratique le ven. 29 janv. (`travaux/strategie-retenue.md:697-698`) | Les deux | Mar. 15 déc. 2026 ; ven. 29 janv. 2027 | À prendre à la date | Constat écrit ; report sans production si non | R16 |

### 4.4 À prendre par GianLuca Carlone ou son entité

| N° | Décision | Qui décide | Échéance | Statut au 4 nov. | Preuve attendue | Liens |
| --- | --- | --- | --- | --- | --- | --- |
| D24 | Désigner l'entité qui signe, paie et valide ; le signataire ; le valideur ; le délégué | GianLuca | Mar. 15 déc. 2026 | À prendre (aucun rendez-vous fixé) | Fiche de l'entité : dénomination, SIREN, effectif | U01, U41 |
| D25 | Demander ou non l'aide régionale au conseil (dépôt avant la signature) | GianLuca, avec son expert-comptable | Avant la signature ; échéance annoncée au 31 déc. 2026 | À prendre | Dossier déposé, ou renoncement écrit | R22 ; U48 |
| D26 | Commander et payer le cadrage | L'entité de GianLuca | Commande vers le 11 déc. pour tenir le 2 févr. ; acompte au plus tard le 29 janv. | À prendre | Bon de commande ; acompte encaissé | R16 ; U03, U45 |
| D27 | Exploiter ou non le CRM ; au nom de quelle structure ; qui appelle | GianLuca | Pendant le cadrage | À prendre | Décision écrite (livrable 5 du cadrage, `travaux/strategie-retenue.md:225`) | R05, R19 ; U11, U30 |
| D28 | Choisir la suite : ventes d'œuvres, pilotage ou organisation interne | GianLuca | 30 jours après la restitution | À prendre après le cadrage | Demande écrite d'une suite, ou arrêt propre | R15, R27 ; U02 |

### 4.5 Différées

Chaque report ci-dessous est une proposition [PR] ; il ne protège que s'il est écrit (D13, D16).

| N° | Décision | Qui décidera | Pas avant | Condition pour la rouvrir | Preuve attendue | Source |
| --- | --- | --- | --- | --- | --- | --- |
| D29 | Socle récurrent B1 | GianLuca, sur pièces | Fin du pilote (décision avant le 25 mars 2027 en central) | Critères du pilote tenus | Contrat signé | `travaux/strategie-retenue.md:43` |
| D30 | Bureaux chez GianLuca | Les deux, puis accord séparé | Bilan du 4 mai 2027 | Convention séparée, sans lien avec les honoraires | Convention signée | `travaux/strategie-retenue.md:630` |
| D31 | Salariat d'un associé chez GianLuca | L'associé concerné et les deux | Bilan du 4 mai 2027 ; jamais pour les deux | Fonctions non couvertes par Marwin ; valideur distinct | Décision écrite séparée | `travaux/strategie-retenue.md:631, 707` |
| D32 | Entrée de GianLuca au capital | Les deux | 12 à 24 mois, après deux renouvellements du socle | Minoritaire, sans veto opérationnel, jamais contre une baisse d'honoraires | Pacte d'investissement séparé | `travaux/strategie-retenue.md:632` |
| D33 | STRATES, Éclosion et autres créations | Les deux | Mois 6 | Financeur écrit, budget plafonné, artiste sous contrat, intégrateur tiers | Contrat de financement | `travaux/strategie-retenue.md:644` |
| D34 | Laboratoire IA et robotique, DGX Spark, IA locale | Les deux ; achat par l'entité cliente | Mois 6 à 12 | Usage démontré ; financeur écrit | Bon de commande de l'entité | `travaux/strategie-retenue.md:645` |
| D35 | Vernissage « signature » avec bras robotisé | GianLuca (organisateur) ; Marwin pour sa part | Sans date | Intégrateur, analyse de risques, exploitant responsable ; un premier événement sans robot reste possible (lot C3) | Autorisations au nom de l'organisateur | `travaux/strategie-retenue.md:646` |
| D36 | « Copilote Jarvis » comme produit et comme nom | Les deux | Propriété réglée | Licences écrites ; gain mesuré sur l'essai de recherche documentaire | Inventaire des licences ; mesure | `travaux/strategie-retenue.md:648` |
| D37 | Exploitation d'un processus prouvé (offre D) | GianLuca, sur proposition de Marwin | Mois 7 | Pilote réussi, puis 2 à 3 mois de critères tenus | Contrat d'exploitation | `travaux/strategie-retenue.md:344` |
| D38 | Passage au socle B2 ; palier B3 | GianLuca, sur proposition de Marwin | B2 après trois mois de B1 ; B3 pas la première année | Gains mesurés ; occupation < 85 % trois mois | Avenant | `travaux/strategie-retenue.md:272, 281` |
| D39 | Recrutement ou sous-traitance durable | Les deux | Trois mois au-delà de 85 % d'occupation | Contrat renouvelé qui le finance | Contrat de travail ou de sous-traitance | `travaux/strategie-retenue.md:623` |
| D40 | Révision du taux de référence interne | Les deux, avec l'expert-comptable | Mois 6 | Coût complet mesuré | Nouveau barème interne | `travaux/strategie-retenue.md:400` |
| D41 | Partage des gains d'automatisation ; prime sur économie réelle | Les deux, puis GianLuca | Après la première année ; prime en option à 12 mois | Gain mesuré et validé par écrit | Calcul remis avec le rapport | `travaux/strategie-retenue.md:420-421` |
| D42 | SARL plutôt que SAS | Les deux, avec l'expert-comptable | Si toutes les conditions sont réunies | Aucun investisseur avant 24 mois ; contrat d'au moins 120 000 € par an ; aucun associé salarié ailleurs | Simulation officielle | `travaux/strategie-retenue.md:562` |
| D43 | Commission sur les ventes, encaissement, intermédiation | Les deux | Pas la première année | Avis écrit d'un avocat | Avis écrit | `travaux/strategie-retenue.md:649` |
| D44 | Cible de dépendance ≤ 80 % | Les deux | Mois 18 si aucun second client au mois 9 | Second client signé | Contrat d'un autre client | `travaux/strategie-retenue.md:522` |

---

## 5. Recommandations : preuve, hypothèse, limite, décision

| Recommandation | Preuve | Hypothèse | Limite | Décision correspondante |
| --- | --- | --- | --- | --- |
| Traiter les risques « données » avant tout acte commercial | Dépôt public le 4 nov. [DR] (`interne/contexte-projet-carlone.md:5`) ; connu au plus tard le 2 nov. [FV] (`interne/audit-marwin-tech-carlone.md:15`) ; aucun responsable du traitement, contrat ni registre [FV] (`travaux/syn-droit.md:59`) | Violation au sens du RGPD [HY fort] ; associés responsables de fait [HY] (`travaux/syn-droit.md:597`) | Visibilité non revérifiée par l'audit ; date exacte de connaissance [IN] | D03, D04, D08 |
| Ne rien envoyer à GianLuca avant D06, D07 et D09 à D11 | Trois versions de l'offre ; retrait appliqué au seul diaporama [FV] (`travaux/syn-sources.md:40`) ; accord de Mathys [IN] | Un message cohérent sert mieux la relation qu'un contact rapide | GianLuca a peut-être déjà tout vu (U04) | D14 |
| Tenir ce registre chaque semaine jusqu'au 15 déc., Morgan tenant, Mathys contrôlant [PR, ce livrable] | Aucun accord écrit entre associés [FV négatif] ; décision du 4 nov. non partagée (`travaux/note-point-4-novembre-et-activites.md:25`) | 30 minutes par semaine suffisent | Coût ≈ 0,5 JP par mois [ES] ; efficacité non mesurée | D09, D13 |
| Remplacer chaque probabilité par le fait observé à chaque jalon | Les probabilités de passage sont des jugements (`travaux/strategie-retenue.md:502`) | Les jalons de 08-feuille-de-route.md sont tenus | Marwin n'a aucun historique | D23 et jalons de 08-feuille-de-route.md |
| Écrire « pas de rémunération sans encaissement » et garder des revenus extérieurs | Rupture au mois 3 : besoin de 21 300 € sans la règle, 1 700 € avec [ES] (`modele-financier/stress-tests.md:34`) | Chacun peut vivre 3 à 4 mois sans Marwin (U42) | Chocs testés un par un (`modele-financier/stress-tests.md:349`) ; impôt sur le revenu non calculé | D16, D20 |
| Réunir l'apport dans le haut de la fourchette et fractionner la prime d'assurance | Point bas de 3 100 €, puis 700 € ou 100 € si la prime est payée d'avance [ES] (`modele-financier/tresorerie-18-mois.md:25, 135`) | Prime de 2 400 à 3 000 € par an [HY] | Prime réelle [IN] (U43) | D17, D19 |
| Écrire la propriété du CRM et de Jarvis avant tout lot CRM et tout usage du nom « Jarvis » | Aucune licence [FV] (`travaux/syn-droit.md:494, 496`) ; « restent chez les associés » (`crm/docs/rapport/rapport-crm-hermes360.md:19`) | Les associés s'accordent sur une licence à Marwin | Protection du code produit par IA [IN] | D12, D16 |
| Formaliser le retrait de Medhi et le lui dire par écrit | Décision orale [DR] ; pièces non corrigées [FV] (`travaux/strategie-retenue.md:31`) | Mathys partage la décision | Ce qui a été promis à Medhi [IN] | D10 |
| Obtenir de Morgan, avant le message, la liste écrite de ce que GianLuca a vu | 50 conversations non lues [FV] (`sources/reprise-59-et-visuels-2026-11-04.md:13-14`) ; envoi du diaporama non tracé (`travaux/syn-sources.md:76`) | Morgan retrouve l'essentiel dans ses messageries | Échanges oraux non tracés | D14 (via U04) |
| Traiter une offre d'emploi comme une décision séparée, pas avant le bilan du mois 6 | ≈ 3 400 € nets contre 1 100 à 1 500 € [MM/ES] (`travaux/strategie-retenue.md:707` ; `modele-financier/scenarios.md:67`) | GianLuca pourrait la faire [DR] | Son intention [IN] | D31 |
| Garder l'exécution hors de Marwin | Activités réglementées [FV] (`travaux/syn-droit.md:412-422`) ; un assistant salarié coûte 2 249 à 2 808 € par mois à l'employeur [MM] (`travaux/strategie-retenue.md:326`) | GianLuca peut désigner ou recruter une personne | Aucune personne connue côté client [IN] | D21, D28 |

---

## 6. Limites

- **Aucune parole directe de GianLuca Carlone** n'existe dans les pièces (`travaux/syn-sources.md:38`). Les risques commerciaux et de relation reposent sur des déclarations rapportées par Morgan.
- **Les probabilités et les impacts sont des jugements** [HY]. Ils ne viennent d'aucune mesure ni d'aucun historique de Marwin.
- **La visibilité actuelle du dépôt FinanceScope/CRM-Carlone n'a pas été revérifiée** par l'audit, qui n'y a pas accès (`travaux/note-point-4-novembre-et-activites.md:23`). La date exacte de connaissance de la fuite est [IN] ; si elle est antérieure au 2 novembre, le délai de la CNIL est déjà dépassé.
- **La collecte est incomplète** : 169 conversations ChatGPT lues sur 219 (`sources/reprise-59-et-visuels-2026-11-04.md:13-14`). Des promesses peuvent exister hors du corpus.
- **Les montants de trésorerie sont des simulations** du modèle financier [ES], chocs pris un par un, sans impôt sur le revenu. Aucune simulation officielle n'a été faite.
- **Les points juridiques marqués [HY]** (rétractation appliquée au contrat de Marwin, notification échelonnée, rôles RGPD, assurance d'un incident connu) restent à trancher par l'avocat ou le DPD (U46).
- **Les disponibilités de Morgan et de Mathys ne sont écrites nulle part.** Sans la fiche du 19 novembre, seul le scénario prudent est défendable (`travaux/strategie-retenue.md:840`).
- **Ce registre décrit l'état au 4 novembre 2026.** Il vieillit vite : il n'a de valeur que s'il est tenu.

Relu et contrôlé le 4 novembre 2026 : 20 vérifications, 11 corrections.
