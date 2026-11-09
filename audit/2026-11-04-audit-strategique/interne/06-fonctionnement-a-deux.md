# Modèle de fonctionnement à deux et seuils de saturation

Audit Marwin Tech × GianLuca Carlone · livrable 6 sur 15 · 4 novembre 2026
Statut : interne (disponibilités, compétences, limites et autres activités des associés ; ne pas transmettre à GianLuca Carlone)
Sources principales : `travaux/syn-capacite-ia.md` (sections 1 à 4 et 7) ; `travaux/strategie-retenue.md` (sections 3.3, 4.5, 6 et 8) ; `travaux/ex-C4-methodes.md` ; `travaux/ex-C7-jarvis.md` ; `travaux/note-point-4-novembre-et-activites.md` ; `modele-financier/scenarios.md` ; pièces d'origine du dépôt Momolscode/Carlone (commit 7b46602), rouvertes en lecture seule le 4 nov. 2026.
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu. Sans autre précision, une [PR] est une proposition de la stratégie retenue ; « [PR, ce livrable] » signale une proposition nouvelle.

Définitions. **JP** : journée-personne de 7 h ; deux personnes présentes une journée consomment 2 JP. **Temps disponible** : jours ouvrés moins congés, maladie et formation. **Temps planifiable** : 85 % du temps disponible ; les 15 % restants absorbent aléas, urgences et imprévus. **Occupation** : tout le temps travaillé d'une personne (Marwin et autres activités) divisé par son temps disponible du mois. Les codes d'offres (A, B0, B1, B2, C1 à C8, D, E) sont ceux de `travaux/strategie-retenue.md:194-203`, détaillés dans 04-catalogue-offres.md.

---

## En bref

1. **Ce qui est démontré, c'est la production, pas la livraison.** Morgan produit vite, avec des assistants IA, des documents, des supports et du code testé en environnement d'essai [FV]. Aucune vente, aucune maintenance dans la durée, aucune coordination de prestataires n'est démontrée par une réalisation [FV négatif]. Les compétences propres de Mathys et sa disponibilité sont inconnues [IN].
2. **Capacité facturable réaliste : environ 6, 10 ou 18 JP par mois** (prudent, central, haut) [ES], si chacun garde 15 % de marge sur **tout** son temps, comme le veut la règle d'occupation de la stratégie. C'est moins que les 7, 12 et 20 JP de la synthèse capacité, repris par la stratégie retenue : voir l'encadré « Écart avec la stratégie retenue » de la section 3.3. En central, le plafond de 10 JP n'est donc pas une marge de sécurité : c'est la capacité elle-même.
3. **La capacité varie selon les mois.** Avec cinq semaines de congés prises aux mêmes dates, elle tombe à environ 6 JP en août, 9 JP en décembre et en avril, 8,5 JP en octobre [ES]. Sur l'année, on peut vendre au plus environ 9,4 JP par mois en moyenne sous le plafond de 10 [ES].
4. **Sur 10 JP facturables, la production proprement dite pèse environ 3 JP.** Le reste part en réunions, collecte, contrôle, déplacements et maintenance [ES].
5. **Les 20 JP des archives demandent environ 90 % du temps planifiable des deux associés** : c'est le scénario haut, pas « un mi-temps ». **Les 40 JP sont impossibles** à deux : il manque environ 17 JP par mois, soit une personne à plein temps [ES].
6. **À deux, en central : un socle de pilotage, deux projets actifs, un projet en veille, un seul lot en production à la fois, aucun projet exploratoire** [ES/PR].
7. **Morgan est le point de défaillance unique** (relation, prix, validation de tout livrable, comptes), et Mathys pour le code du CRM [FV/DR]. Chaque processus reçoit un suppléant nommé et un test de suppléance chaque trimestre [PR, ce livrable].
8. **Dix-sept seuils de saturation chiffrés**, chacun avec sa réponse. Ordre : reporter, réduire, renforcer, sous-traiter, recruter ; refuser ou suspendre quand un signal de la stratégie est atteint (section 8).
9. **« Le travail de 100 personnes à deux »** demanderait de multiplier par 50 à 85 chaque journée [ES]. La cible mesurable est un facteur de 1,3 à 1,5 sur les processus pilotés à 6 mois et de 1,5 à 2 à 12 mois [HY] : au mieux, le travail de 1,5 à 2 personnes sans outils en central, de 2,3 à 3 dans le scénario haut (section 9).
10. **Les rituels entre associés et le relevé du temps coûtent environ 1,5 à 2 JP par mois** à deux [ES]. Le relevé commence dès la remise en ordre de novembre 2026 et couvre aussi les autres activités, sans détail, pour mesurer l'occupation.

---

## 1. Ce que ce livrable ajoute, et ce qu'il laisse aux autres

**Il reprend** la synthèse capacité (`travaux/syn-capacite-ia.md`, sections 1 à 4 et 7) et la stratégie retenue, en revérifiant les points déterminants dans les pièces d'origine.

**Il ajoute :**
- la capacité recalculée avec la règle d'occupation de la stratégie (85 % sur tout le temps), puis mois par mois ;
- un budget de temps du socle de pilotage B1, poste par poste ;
- une carte « offre → compétences exigées → preuve disponible » ;
- un tableau des seuils de saturation qui réunit ceux de la synthèse capacité, de la stratégie et de 04-catalogue-offres.md ;
- les rituels entre associés et le format du relevé du temps.

**Il ne refait pas** : les offres, prix et marges (04-catalogue-offres.md) ; les protocoles d'essai des processus IA (07-processus-ia-et-essais.md) ; le calendrier (08-feuille-de-route.md) ; la trésorerie et les tests d'échec chiffrés (09-modele-economique-tresorerie.md) ; le pacte entre associés (10-structures-et-relations.md) ; les rôles, plafonds et règles de silence avec le client (12-gouvernance-contrat-sortie.md) ; le registre des risques (14-registre-risques-inconnues-decisions.md).

**Méthode de calcul.** Les jours ouvrés ont été recalculés le 4 nov. 2026 (lundi à vendredi, onze jours fériés de métropole). Les scripts de la synthèse capacité ont été relancés : ils donnent les mêmes résultats (253 jours ouvrés de décembre 2026 à novembre 2027 ; capacités de 7,1, 11,8, 20,0 et 28,2 JP). Les calculs nouveaux de ce livrable ont été faits en Python, sans fichier conservé. Tous leurs résultats sont des [ES] et sont arrondis au dixième.

---

## 2. Matrice des compétences

Statuts demandés (`travaux/DEMANDE.md:31-33`) : **démontrée** (une réalisation existe et a été constatée), **déclarée** (affirmée, sans réalisation constatée), **en cours d'acquisition**, **à sous-traiter**, **dépendante** d'un partenaire ou d'un équipement.

« Démontrée » veut seulement dire qu'un objet existe. Cela ne prouve ni sa qualité vue par un client, ni son usage, ni la part de travail personnelle face à l'IA : 48 des 56 commits du dépôt Momolscode/Carlone au commit 7b46602 sont signés « Claude » [FV] (relevé `git log` du 4 nov. 2026).

### 2.1 Morgan Olsen

| Compétence | Statut | Preuve ou source | Code | Portée pour l'offre |
| --- | --- | --- | --- | --- |
| Produire vite, avec des assistants IA, documents, supports et code testé en environnement d'essai | **Démontrée** (production) | Dépôt BOJART : 933 fichiers, ≈ 19 700 lignes Python, 973 fonctions de test, 7 workflows, produits du 30 oct. au 2 nov. (`travaux/ex-C7-jarvis.md:97` ; correction `travaux/ver-C7-jarvis.md:31`) | [FV] ; part personnelle [IN] | Capacité de production réelle ; aucun de ces objets n'a été réceptionné par un client |
| Discipline de preuve : séparer mesuré, simulé, déclaré, proposé ; restauration vérifiée | **Démontrée** dans un dépôt interne | `travaux/ex-C7-jarvis.md:99` ; restauration dans un dossier neuf réussie (`travaux/ex-C7-jarvis.md:47`) | [FV] / [MM] | La compétence la plus utile pour des décisions préparées et pour les essais (07-processus-ia-et-essais.md) |
| Déployer sur un vrai poste ; faire adopter un outil par un utilisateur | **Non démontrée** | Jarvis M07 « non qualifié » sur la tour (`travaux/ex-C7-jarvis.md:37`) ; densité documentaire qui risque de consommer la capacité (`travaux/ex-C7-jarvis.md:281`) | [FV] | Aucune automatisation n'est vendue comme opérationnelle avant un essai en environnement réel (`sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md:63`) |
| Supports commerciaux, diaporamas, notes | **Démontrée** (objets), avec assistant | Diaporama de 11 vues, vernissage, note de vision (`travaux/strategie-retenue.md:31`) | [FV] existence ; acceptation [IN] | Utile ; mais les versions ne sont pas tenues : la décision du 4 nov. n'a été appliquée qu'à 1 support sur au moins 5 (`travaux/syn-capacite-ia.md:699`) |
| Relation client, connaissance du terrain, diagnostic | **Déclarée** | « La complémentarité à éprouver » (`sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md:15`) | [DR] | Morgan est le seul canal vers GianLuca : aucune pièce ne rapporte une parole directe du client (`travaux/syn-sources.md:38`) |
| Méthode de conseil (cadrer, produire, piloter) | **Écrite, non éprouvée** | La méthode « reste à éprouver en mission réelle » (`sources/chatgpt-pages/2026-11-04-complement/pilotage-extraits-carlone.md:22`) | [DR] | Le cadrage et le pilote B0 servent aussi à l'éprouver |
| Vente, négociation, encaissement | **Non démontrée**, contre-indices | OLSEN : 36 propositions et 72 brouillons préparés, aucun envoyé ; 503 prospects « À faire » (`travaux/note-point-4-novembre-et-activites.md:9`) ; « Au 30 octobre, aucune prestation n'avait été facturée » (`interne/offre-marwin-tech-remuneration-et-collaboration.md:29`) | [DR] ; [FV] pour la pièce | Point le plus faible pour trouver un second client |
| Administration d'une entreprise | **Contre-indices** | Domiciliation résiliée, domaines suspendus, abonnements en échec de prélèvement (`travaux/note-point-4-novembre-et-activites.md:6-8`) | [DR] | Le poste « administration » ne doit pas être sous-estimé (section 3) |
| Vidéo avec fournisseurs IA ; drone, tournage | **Démontrée** en coupes de travail ; **déclarée** pour le drone | `travaux/syn-capacite-ia.md:95, 100` | [FV] / [DR] | Hors périmètre ; concurrence directe en temps (film « Shelby ») |
| Robotique, IA locale, CAO | **En cours d'acquisition** (simulations, profils préparés) | `travaux/syn-capacite-ia.md:101-103` | [ES] pour les simulations ; [DR] pour la CAO | Hors périmètre (`travaux/strategie-retenue.md:644-646`) |
| Structuration juridique, fiscale, sociale | **En cours** (documents de travail non validés) | `travaux/syn-capacite-ia.md:104` | [ES] | **À sous-traiter** pour toute validation |
| Impression 3D (≈ 10 machines) | **Dépendante** d'un partenaire, retirée | « J'ai également accès à un atelier d'environ dix imprimantes 3D » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:21`), probablement le parc de Medhi [HY] ; retrait du 4 nov. (`travaux/note-point-4-novembre-et-activites.md:25`) | [DR] / [HY] | À retirer de toute promesse |
| Tour RTX 4060 Ti, voix, écrans | **Dépendante** d'un équipement de propriété inconnue | « poste RTX 4060 Ti de BOJ.ART » (`travaux/ex-C7-jarvis.md:63`) | [FV] / [IN] | Un outil de pilotage ne doit pas en dépendre (`travaux/ex-C7-jarvis.md:210`) |
| Outils payants (Notion, ChatGPT Pro…) | **Dépendante** de comptes personnels | Échecs de prélèvement depuis fin octobre (`travaux/note-point-4-novembre-et-activites.md:8`) | [DR] | Risque de continuité immédiat (section 7) |

### 2.2 Mathys Couet

| Compétence | Statut | Preuve ou source | Code | Remarque |
| --- | --- | --- | --- | --- |
| Rechercher et structurer un dossier de prospection | **Démontrée** (existence) ; exécution commerciale **non démontrée** | Dossier de 34 pages signé « @Mathys », 21 oct. 2026 (`sources/dossier-partenariats-vieux-relais-et-le-m-2026-10-21.pdf` p. 1) | [FV] existence ; part personnelle [IN] | Plan jamais exécuté |
| Commander et cadrer un CRM produit par des agents | **Démontrée** comme donneur d'ordre | « Recentrage […] (23/10/2026, demande de Mathys) » (`crm/PASSATION.md:7`) ; « le dépôt de Mathys, FinanceScope/CRM-Carlone » (`README.md:35`) | [FV] pour les pièces ; rôle réel [DR] | Seul donneur d'ordre nommé dans le CRM ; son code personnel est [IN] |
| « La technique, le CRM, l'exploitation » | **Déclarée** | `interne/recueil-sessions-chatgpt-2026-11-04.txt:440` ; partage « Mathys : technique et CRM » (`interne/recueil-sessions-chatgpt-2026-11-04.txt:534`) | [DR] | Texte d'assistant écrit à partir des propos de Morgan |
| Développement, sécurité, hébergement | **Inconnue** | Défauts du CRM relevés (`travaux/syn-capacite-ia.md:116`) ; on ignore qui a décidé quoi | [IN] | Les défauts ne disent rien de ses compétences propres |
| Robotique, création, Jarvis | **Absente** des pièces | Aucune occurrence dans le dépôt BOJART (`travaux/ex-C7-jarvis.md:67`) | [FV négatif] | — |
| Disponibilité | **Inconnue** | « Temps de Mathys non fixé » (`interne/audit-marwin-tech-carlone.md:62`) ; fiche « rôles, compétences, responsabilités et temps disponible » encore à faire (`interne/recueil-sessions-chatgpt-2026-11-04.txt:1388`) | [IN] | **Principale inconnue du modèle de charge** |

Une autre inconnue touche le fonctionnement « à deux » : une page de pilotage présente Eaglemic (Michael Bach) comme « également un associé principal de Morgan » (`sources/chatgpt-pages/2026-11-04-complement/pilotage-extraits-carlone.md:9`) [DR]. Son rôle éventuel dans Marwin est [IN] ; le pacte doit le clarifier par écrit.

### 2.3 Ce que chaque offre exige, et ce qui est prouvé

| Offre | Compétences exigées | État des preuves | Ce qui manque | Parade [PR] |
| --- | --- | --- | --- | --- |
| 0 Remise en ordre | Conformité des données ; tenue des versions | **Contre-preuves** : dépôt du CRM public (`interne/contexte-projet-carlone.md:5, 11`) ; décision du 4 nov. appliquée à 1 support sur 5 | Avis d'un avocat ou d'un DPD | Avis externe ; registre « décision → documents touchés » (`travaux/strategie-retenue.md:578`) |
| A Cadrage | Entretien, analyse, synthèse sourcée, carte des rôles | Production documentaire démontrée ; entretien et méthode non éprouvés | Aucune mission de conseil payée | Un associé mène, l'autre contrôle (`travaux/strategie-retenue.md:226`) ; écart JP réelles / 8 JP estimées ≤ 25 % |
| B0, B1, B2 Socle de pilotage | Animer des réunions, tenir un registre, préparer des dossiers de décision, coordonner | Registre de tâches et d'affirmations démontré dans un dépôt interne (`travaux/ex-C7-jarvis.md:197`) ; animation et coordination non démontrées | Usage par un client non technicien | B0 de 8 semaines avec critères d'adoption et d'abandon |
| C1 Catalogue des œuvres | Structurer des fiches et des données | Démontrée (CRM, catalogues) | Photographie professionnelle | Photographe payé par l'entité cliente |
| C2 Pilote commercial | Qualifier des données ; conformité ; script | Production démontrée ; conformité contredite ; vente non démontrée | Un appelant | Appelant désigné côté client ou Quali Contact ; avis de l'avocat |
| C3, C4 Événement, lieux | Réglementation des établissements recevant du public, organisation | Aucune preuve (`travaux/syn-capacite-ia.md:126`) | Exploitant, chargé de sécurité | Dossiers seulement ; l'exploitant reste l'entité de GianLuca |
| C5 Échange avec Quali Contact | Format d'échange de fichiers | Code démontré en essai | Logiciel de Quali Contact inconnu | Rien avant le contrat et le format réel |
| C6 Outillage et passation | Configurer des outils, écrire des procédures, former | Procédures de passation écrites démontrées (`crm/PASSATION.md:37`) ; formation non démontrée | — | Deux séances ; adoption mesurée à part du paiement |
| C7 Étude de rentabilité | Modélisation financière | Documents de travail non validés ; simulateur fiscal du CRM à corriger (`travaux/strategie-retenue.md:211`) | Expert-comptable | Relecture professionnelle |
| C8 Kit de campagne | Rédaction commerciale | Démontrée (production) | Validation fiscale | Conseil du client |
| D Exploitation | Maintenir dans la durée | **Non démontrée** (`travaux/syn-capacite-ia.md:125`) | — | Au plus tôt au mois 7, maintenance plafonnée à 0,5 JP par mois et par processus (`travaux/strategie-retenue.md:349`) |
| E Urgences | Disponibilité hors plages | Non démontrée ; aucune astreinte prévue | Relais | Liste fermée ; astreinte seulement par forfait séparé |

**Lecture.** Les offres d'entrée (A, B0, C1, C6) reposent sur des compétences de production démontrées et sur des compétences de relation et de méthode seulement déclarées. C'est pourquoi chaque offre a une réception écrite et une mesure : elles servent aussi de preuve de compétence.

### 2.4 À sous-traiter, ou dépendant d'un tiers

**À sous-traiter de façon permanente** [PR] (`travaux/syn-capacite-ia.md:130`) : expertise comptable et fiscale ; conseil juridique (contrats, données personnelles, droit du travail, propriété intellectuelle) ; assurance ; intégration et sécurité robotiques ; photographie et vidéo professionnelles des œuvres ; appels sortants (payés par l'entité de GianLuca) ; sécurité des événements recevant du public. Ces tiers facturent directement l'entité de GianLuca quand ils travaillent pour elle (`travaux/strategie-retenue.md:388`).

**Retiré depuis le 4 novembre** [DR] : atelier d'impression 3D, option laboratoire, Jarvis comme produit, vernissage adossé au parc de Medhi (`travaux/syn-capacite-ia.md:134-140`).

### 2.5 Qui fait quoi, qui remplace qui

Répartition de la stratégie : Morgan porte la relation client et les prix ; Mathys la technique et les données, avec une **délégation écrite de la validation technique** (`travaux/strategie-retenue.md:619`). Le tableau ajoute un suppléant par processus [PR, ce livrable].

| Processus | Titulaire | Suppléant | Condition pour que la suppléance marche |
| --- | --- | --- | --- |
| Relation avec GianLuca, comité mensuel | Morgan | Mathys, pour la relation courante (pas les prix) | Mathys assiste à un comité sur trois (≈ 0,1 JP par mois) |
| Point hebdomadaire et comptes rendus | Morgan | Mathys | Modèles d'ordre du jour et de compte rendu ; registre partagé |
| Dossiers de décision | Morgan | Mathys | Sources rangées dans le registre, pas dans des conversations personnelles |
| Prix, devis, avenants | Morgan | Aucun : décision des deux au pacte (`travaux/strategie-retenue.md:614`) | Grille de devis écrite (04-catalogue-offres.md) |
| Outils, comptes, sauvegardes, restauration | Mathys | Morgan | Coffre partagé des accès ; restauration faite par Morgan une fois par trimestre |
| Données du CRM, réimport des résultats d'appel (C2) | Mathys | Morgan | Deux administrateurs ; procédure écrite |
| Validation technique | Mathys (délégation écrite) | Morgan | — |
| Validation des documents envoyés au client | Morgan | Mathys, par délégation écrite (`travaux/strategie-retenue.md:578`) | — |
| Contrôle à quatre yeux | L'associé qui n'est pas l'auteur, sous 2 jours ouvrés | — | Si l'autre est absent, voir section 6 |
| Prospection d'un second client | Morgan (≈ 1,75 JP par mois) | Mathys (≈ 0,75 JP) | Plancher protégé (section 8) |
| Incident | Quiconque le constate arrête ; Mathys prend les mesures techniques ; Morgan informe le client sous 24 h (`travaux/strategie-retenue.md:585`) | — | Bouton d'arrêt documenté |

---

## 3. Modèle de charge mensuel

### 3.1 Calendrier et temps disponible par personne

| Élément | Valeur | Code | Source |
| --- | --- | --- | --- |
| Jours ouvrés, décembre 2026 à novembre 2027 | 253 ; 21,1 par mois en moyenne ; de 19 (mai 2027) à 22 | [FV] (recalcul du calendrier, 4 nov. 2026) | `travaux/syn-capacite-ia.md:150` |
| Congés | 25 jours par an (30 en hypothèse haute) | [HY] | `travaux/syn-capacite-ia.md:151` |
| Maladie et indisponibilités imprévues | 8 jours par an (5 à 10) | [HY] | `travaux/syn-capacite-ia.md:152` |
| Formation, veille, outils | 10 jours par an (6 à 12) | [HY] | `travaux/syn-capacite-ia.md:153` |
| **Temps disponible** | **≈ 17,5 JP par mois** (16,8 à 18,1) | [ES] | (253 − 25 − 8 − 10) ÷ 12 |
| Marge de 15 % (seuil d'occupation de 85 %) | ≈ 2,6 JP par mois | [PR] | `travaux/strategie-retenue.md:623` |
| **Temps planifiable** | **≈ 14,9 JP par mois** | [ES] | 17,5 × 0,85 |

Une couverture sur trente jours calendaires ne vaut donc pas trente journées de production. L'archive du 29 oct. l'écrivait : « La disponibilité éventuelle pendant trente jours calendaires ne correspond ni à trente journées de production ni à une astreinte permanente » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:64`) [FV]. Un mois calendaire vaut environ 21 jours ouvrés, 17,5 JP disponibles et 14,9 JP planifiables par personne [ES].

### 3.2 Autres activités : ce qu'on sait

**Morgan mène en parallèle** [FV pour l'existence des artefacts ; DR pour l'activité] : OLSEN (plan « Vendre 10 sites », 503 prospects, 36 propositions) ; des projets personnels de vente en ligne ; le film « Shelby » (7 artefacts des 3 et 4 nov.) ; Côme Millot, maréchal-ferrant ; un kit de parrainage ; un audit de site ; BOJ.ART avec Medhi (4 artefacts des 2 au 4 nov.) (`travaux/note-point-4-novembre-et-activites.md:9-17`). Une console de pilotage suit « 24 dossiers, 22 dépôts, cinq films et huit missions » (`interne/recueil-sessions-chatgpt-2026-11-04.txt:1517`) [DR]. Son compte claude.ai porte 91 artefacts (`travaux/note-point-4-novembre-et-activites.md:16`) [FV pour le relevé].

**Mathys** : aucune information sur un emploi, des études ou d'autres projets [IN] (`travaux/strategie-retenue.md:734`, question 7).

Faute d'engagement écrit, on garde les trois scénarios de la stratégie [HY] (`travaux/strategie-retenue.md:495`) :

| Scénario | Part de Morgan pour Marwin | Part de Mathys pour Marwin | Ce que cela suppose |
| --- | --- | --- | --- |
| Prudent | 50 % | 25 % | Morgan garde OLSEN, BOJ.ART et ses projets clients ; Mathys a une autre activité principale |
| Central | 65 % | 50 % | Morgan réduit fortement ses autres projets ; Mathys à mi-temps |
| Haut | 90 % | 90 % | Les deux se consacrent presque entièrement à Marwin |

### 3.3 Charge mensuelle par poste, en régime de croisière (binôme)

Dans ce livrable, les parts ci-dessus s'appliquent au **temps planifiable** (85 %), pas au temps disponible. Les postes non facturables reprennent la synthèse capacité (`travaux/syn-capacite-ia.md:181-190`).

| Poste (JP par mois, pour deux) | Prudent | Central | Haut |
| --- | --- | --- | --- |
| Temps disponible (2 × 17,5) | 35,0 | 35,0 | 35,0 |
| Marge de 15 % : aléas, urgences, imprévus | 5,25 | 5,25 | 5,25 |
| Autres activités (OLSEN, Shelby, BOJ.ART, emploi ou études) | 18,6 (Morgan 7,4 ; Mathys 11,2) | 12,6 (Morgan 5,2 ; Mathys 7,4) | 3,0 (1,5 chacun) |
| **Temps pour Marwin** | **11,2** (7,4 + 3,7) | **17,1** (9,7 + 7,4) | **26,8** (13,4 + 13,4) |
| Administration de Marwin (comptabilité, factures, banque, assurances, registre des traitements, contrats, revues internes) | 2,0 | 2,0 | 2,5 |
| Prospection d'un second client (plancher) | 1,5 | 2,5 | 3,5 |
| Maintenance et support internes (outils, sécurité, sauvegardes, abonnements) | 1,0 | 1,5 | 2,0 |
| Capitalisation des méthodes | 0,5 | 0,75 | 1,0 |
| **Total non facturable Marwin** | **5,0** | **6,75** | **9,0** |
| **Capacité facturable réaliste** [ES] | **≈ 6** (6,2) | **≈ 10** (10,4) | **≈ 18** (17,8) |
| Pour comparaison : synthèse capacité (`travaux/syn-capacite-ia.md:190`) | ≈ 7 | ≈ 12 | ≈ 20 |

Le plafond théorique (100 % chacun pour Marwin, frais internes minimaux) donne environ 25 JP facturables, contre 28 dans la synthèse capacité [ES].

> **Écart avec la stratégie retenue : capacité de 6 / 10 / 18 JP, et non de 7 / 12 / 20.**
> *Ce que dit la stratégie.* Capacité facturable d'environ 7, 12 et 20 JP par mois (`travaux/strategie-retenue.md:361-366, 496`), plafond engagé de 10 JP la première année, et occupation mesurée par personne **sur tout son temps**, avec une alerte à 85 % (`travaux/strategie-retenue.md:485, 623`).
> *Pourquoi les deux ne tiennent pas ensemble.* Les capacités 7 / 12 / 20 viennent de la synthèse capacité. Elle répartit 100 % du temps disponible entre Marwin et les autres activités, et ne garde qu'une réserve de 8 % à l'intérieur du temps Marwin (`travaux/syn-capacite-ia.md:179`). Si les autres activités occupent vraiment 35 % du temps de Morgan et 50 % de celui de Mathys, vendre 10 JP porte l'occupation de chacun à environ 87 à 93 % [ES] : l'alerte de 85 % se déclenche tous les mois. Le jugement de l'angle Marwin notait déjà que 10 JP représentent environ 94 % du temps central consacré à Marwin (`travaux/juge-J2-marwin.md:195`).
> *Ce que ce livrable retient.* Les parts de 50/25, 65/50 et 90/90 % s'appliquent aux 85 % du temps disponible. La marge de 15 % remplace la réserve d'aléas. On obtient environ 6, 10 et 18 JP facturables [ES].
> *Conséquences.* (1) En central, le plafond de 10 JP égale la capacité : il n'y a plus de marge entre les deux, seulement celle des 15 %. (2) Les prix ne changent pas : la stratégie les calcule déjà sur le coût d'une JP à 10 JP facturés, 710 à 885 € (`travaux/strategie-retenue.md:122`). (3) Le modèle financier reste tenable : 8,9 JP vendues en moyenne en régime central, 5,2 en prudent, 12 réalisées par les associés en ambitieux (`modele-financier/scenarios.md:38-39`). Le prudent est au bord : 6 JP au mois le plus chargé pour une capacité de 6,2. En prudent, passer de 7 à 6 JP facturables relève aussi le coût complet théorique d'environ un sixième, soit ≈ 870 à 1 120 € par JP au lieu de 744 à 962 € (`travaux/strategie-retenue.md:363`) [ES] : le prix cible ne le couvre plus, ce qui reste cohérent avec un scénario sans rémunération régulière (`travaux/strategie-retenue.md:511`). (4) La fiche « rôles et disponibilités » doit fixer un **plafond des autres activités**, pas seulement une part pour Marwin : en central, environ 5 JP par mois pour Morgan (à peine plus d'un jour par semaine) et environ 7,5 JP pour Mathys.
> *Décision* : Morgan et Mathys valident cette lecture dans la fiche « rôles et disponibilités » (décision n° 3 de la stratégie, `travaux/strategie-retenue.md:717`).

**Sensibilité.** Si l'administration demande 2,5 JP au lieu de 2 (ce que suggèrent les retards administratifs constatés et le coût des rituels de la section 10), la capacité centrale tombe à environ 9,9 JP [ES]. Si Mathys ne donne que 40 % de son temps planifiable, elle tombe à environ 8,9 JP [ES].

### 3.4 Vue par personne, scénario central

| JP par mois | Morgan | Mathys |
| --- | --- | --- |
| Disponible | 17,5 | 17,5 |
| Planifiable (85 %) | 14,9 | 14,9 |
| Autres activités, au plus | 5,2 | 7,4 |
| Temps pour Marwin | 9,7 | 7,4 |
| Administration | 1,0 | 1,0 |
| Prospection | 1,75 | 0,75 |
| Maintenance interne | 0,5 | 1,0 |
| Capitalisation | 0,4 | 0,35 |
| **Facturable** [ES] | **≈ 6,0** | **≈ 4,3** |

La répartition des postes non facturables entre les deux est une hypothèse de ce livrable [HY]. Elle suit les rôles de la stratégie : prospection surtout pour Morgan, maintenance surtout pour Mathys.

### 3.5 Ce que contient la capacité facturable

L'archive du 29 oct. le disait : « Les réunions, la préparation, la coordination, les déplacements et les corrections consomment cette capacité » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:64`) [FV]. Ventilation de la synthèse capacité (`travaux/syn-capacite-ia.md:196-203`), appliquée à 10 JP [ES] :

| Poste facturable | Part [ES] | JP sur 10 | Remarque |
| --- | --- | --- | --- |
| Réunions et coordination (client, interne, prestataires) | 22 % | 2,2 | Un seul associé par réunion client, sauf décision qui demande les deux |
| Collecte et préparation des informations | 13 % | 1,3 | Plus élevée au début : accès souvent incomplets (`sources/chatgpt-pages/2026-11-04-complement/audit-pilotage-extraits-carlone.md:11`) |
| Contrôle et corrections | 15 % | 1,5 | Plus élevé tant que les sorties d'IA ne sont pas éprouvées |
| Déplacements et présence sur les lieux | 10 % | 1,0 | Lieu de résidence des associés et distance à Cosne-Cours-sur-Loire [IN] |
| Maintenance des outils du client | 8 % | 0,8 | Facturable seulement si le bon de commande la prévoit |
| **Production de livrables** | **32 %** | **3,2** | Le reste |

**Réunions.** Une réunion hebdomadaire de 2 h avec le client et une réunion interne d'une heure coûtent environ 2,5 JP par mois si un seul associé assiste à la réunion client, et 3,7 JP si les deux y vont (`travaux/syn-capacite-ia.md:205-210`) [ES, recalculé]. Avec le point de 1 h 30 du socle, c'est environ 2,2 JP avec un associé et 3,1 JP avec les deux [ES]. D'où la règle : deux associés en réunion, deux JP seulement si le bon de commande le prévoit (`travaux/strategie-retenue.md:389`).

### 3.6 Budget de temps du socle de pilotage B1

Le socle est vendu au périmètre, pas au temps (`travaux/strategie-retenue.md:186`). Son coût en temps doit pourtant tenir dans la capacité. Décompte [ES], à remplacer par le relevé du pilote B0 :

| Élément du socle (liste fermée de `travaux/strategie-retenue.md:255-264`) | Hypothèse [HY] | JP par mois |
| --- | --- | --- |
| Point hebdomadaire de 1 h 30, un associé | 4,33 semaines | 0,9 |
| Préparation du point et relances | 30 min par semaine | 0,3 |
| Comptes rendus sous 24 h ouvrées (4 à 5) | 45 min chacun, assistance IA et relecture comprises | 0,5 |
| Registre des décisions et tableau de bord | 1 h par semaine | 0,6 |
| Comité mensuel et rapport | 2 h + 3 h | 0,7 |
| Dossiers de décision | 2 dossiers × 3 h 30 | 1,0 |
| Coordination des prestataires sous mandat | 3 h | 0,4 |
| Suivi budgétaire préparatoire et veille des échéances | 3 h | 0,4 |
| Contrôle à quatre yeux par l'autre associé | 3 h | 0,4 |
| Sauvegardes, journal, restauration testée | 1 h 30 | 0,2 |
| Une visite sur place, trajet compris | Distance [IN] | 0,5 |
| **Total** | | **≈ 5,9** (≈ 5,4 sans visite ; ≈ 6,9 avec 4 dossiers) |

> **Écart avec la stratégie retenue : deux dossiers de décision par mois dans B1, pas quatre.**
> La stratégie donne 4,5 à 5,5 JP pour B1, avec « deux à quatre dossiers de décision par mois au plus » (`travaux/strategie-retenue.md:260, 273`). Le décompte ci-dessus donne environ 5,5 à 6 JP avec deux dossiers et une visite, et près de 7 JP avec quatre dossiers [ES]. 04-catalogue-offres.md relève déjà que la formule de la stratégie donne 4,5 à 6 JP ; il fixe une capacité de référence de 5,5 JP et un déclencheur à deux mois de dépassement.
> *Ce que ce livrable retient* [PR, ce livrable] : dans les fiches de mission de B0 et B1, **deux dossiers de décision par mois** ; un troisième prend la place d'un projet actif ou devient un lot ; quatre dossiers relèvent de B2. Une visite sur place par mois est comprise ; les autres passent par avenant (offre E). Prix inchangés.
> *Limite* : les durées sont des hypothèses. Le relevé du temps pendant B0 tranche.
> *Décision* : Morgan et Mathys valident avant de rédiger la fiche de mission de B0.

### 3.7 Variation selon les mois

Hypothèse de congés [HY] : les deux associés prennent leurs 25 jours aux mêmes périodes (5 jours fin décembre, 5 en avril, 10 en août, 5 fin octobre). Maladie et formation sont étalées (1,5 JP par mois). Capacité facturable du binôme en central = temps disponible du mois × 0,59 [ES] (formule de la section 3.3 rapportée au mois).

| Mois | Jours ouvrés [FV] | Congés [HY] | Disponible par personne | Planifiable par personne | Capacité facturable centrale (binôme) | Vendable sous le plafond de 10 |
| --- | --- | --- | --- | --- | --- | --- |
| Déc. 2026 | 22 | 5 | 15,5 | 13,2 | 9,2 | 9,2 |
| Janv. 2027 | 20 | 0 | 18,5 | 15,7 | 10,9 | 10 |
| Févr. 2027 | 20 | 0 | 18,5 | 15,7 | 10,9 | 10 |
| Mars 2027 | 22 | 0 | 20,5 | 17,4 | 12,1 | 10 |
| Avr. 2027 | 22 | 5 | 15,5 | 13,2 | 9,2 | 9,2 |
| Mai 2027 | 19 | 0 | 17,5 | 14,9 | 10,4 | 10 |
| Juin 2027 | 22 | 0 | 20,5 | 17,4 | 12,1 | 10 |
| Juil. 2027 | 21 | 0 | 19,5 | 16,6 | 11,5 | 10 |
| Août 2027 | 22 | 10 | 10,5 | 8,9 | 6,2 | 6,2 |
| Sept. 2027 | 22 | 0 | 20,5 | 17,4 | 12,1 | 10 |
| Oct. 2027 | 21 | 5 | 14,5 | 12,3 | 8,6 | 8,6 |
| Nov. 2027 | 20 | 0 | 18,5 | 15,7 | 10,9 | 10 |
| **Année** | **253** | **25** | **210** (17,5 par mois) | **178,5** | **≈ 124** (10,4 par mois) | **≈ 113** (9,4 par mois) |

**Conséquences** [PR, ce livrable] :
- **Congés décalés** : les deux associés ne s'absentent jamais la même semaine, pour qu'un des deux tienne toujours le socle. Le calendrier des congés de l'année est écrit dans la fiche « rôles et disponibilités ».
- **Mois réduits annoncés** : la fiche de mission du socle prévoit une capacité réduite en août et pendant la dernière semaine de décembre (socle seul, aucun lot), sans que ce soit une baisse du prix du socle, payé pour une responsabilité continue (`travaux/strategie-retenue.md:419`).
- **Pas de lot qui se termine en août ou fin décembre** : les dates de livraison évitent ces périodes.
- Les mois longs (mars, juin, septembre) ne permettent pas de vendre plus que 10 JP : le surplus va à la marge, à la prospection ou à la capitalisation.

### 3.8 Les premiers mois : une charge de démarrage non facturable

| Chantier de démarrage (mois 0 à 2) | JP [ES] | Source |
| --- | --- | --- |
| Fuite : dépôt privé, fiche de violation, décision de notification avec l'avocat, copies contrôlées ; conformité minimale | 3 à 6 | `travaux/syn-capacite-ia.md:216` |
| Immatriculation, compte professionnel, RC professionnelle, outil de facturation | 3 à 5 | `travaux/syn-capacite-ia.md:217` |
| Contrat-cadre, fiches de mission, procédure de sortie, inventaire des accès | 2 à 4 | `travaux/syn-capacite-ia.md:218` |
| Mise en cohérence après la décision du 4 nov. | 1 à 2 | `travaux/syn-capacite-ia.md:219` |
| **Total retenu par la stratégie** | **9 à 17** | `travaux/strategie-retenue.md:213` |
| Démonstrateurs internes du registre des décisions (pilote P1) et de la recherche documentaire (pilote P3), prévus à 90 jours (`travaux/strategie-retenue.md:169`) | 3 à 5 | Mise en place : 2 à 3 JP et 1 à 2 JP (`travaux/syn-capacite-ia.md:705, 737`) |
| **Total réel des mois 0 à 3** | **12 à 22** | [ES] |

> **Écart avec la stratégie retenue : charge de démarrage.** Les 9 à 17 JP de la remise en ordre (`travaux/strategie-retenue.md:213`) ne comptent pas les démonstrateurs internes que la stratégie demande à 90 jours. Avec eux, la charge non facturable des mois 0 à 3 est de 12 à 22 JP [ES]. *Ce que ce livrable retient* : les démonstrateurs sont pris sur la capitalisation et la maintenance interne des mois 1 à 3, ou reportés après la restitution du cadrage ; ils ne passent jamais avant la fuite, les documents et le cadrage. *Décision* : Morgan et Mathys choisissent entre ces deux options lors de la première revue mensuelle.

Déroulé central, pour la charge seulement (le calendrier détaillé est dans 08-feuille-de-route.md) [ES] :

| Période | Travail principal | JP facturables (binôme) | JP non facturables de démarrage |
| --- | --- | --- | --- |
| Nov. 2026 (mois 0, 20 jours ouvrés) | Fuite, documents, fiche « rôles et disponibilités », statuts et pacte, message de recadrage | 0 | 5 à 9 |
| Déc. 2026 | Rendez-vous avant le 15 déc. ; immatriculation sur engagement écrit ; contrat-cadre | 0 | 4 à 8 |
| Janv. 2027 (mois 1) | Cadrage : 8 JP (Morgan 5, Mathys 3) | 8 | 0 à 2, plus démonstrateurs |
| Févr. et mars 2027 | Pilote de 8 semaines dans la voie choisie | ≈ 3 à 7,5 par mois selon la voie (04-catalogue-offres.md, section 2.2) | Démonstrateurs éventuels |
| Avr. 2027 (mois 4) et après | Socle B1 et un lot à la fois, si GianLuca le décide par écrit | 8,5 à 10 | — |

### 3.9 Capacité facturable réaliste : ce qu'il faut retenir

| Scénario | Capacité [ES] | Ce que la stratégie engage | Condition |
| --- | --- | --- | --- |
| Prudent | ≈ 6 JP | Cadrage, puis socle léger et un lot par trimestre ; 4 à 6 JP vendues | Seul scénario défendable sans engagement écrit des disponibilités (`travaux/strategie-retenue.md:840`) |
| Central | ≈ 10 JP (≈ 9,4 en moyenne annuelle sous le plafond) | Plafond de 10 JP ; 8,5 à 10 JP vendues en régime | Autres activités plafonnées par écrit (≈ 5 JP pour Morgan, ≈ 7,5 pour Mathys) |
| Haut | ≈ 18 JP | 12 à 15 JP par les associés, 2 à 4 JP sous-traitées | Engagement à 90 % inscrit au pacte ; pas la première année pour B2 avec des lots (04-catalogue-offres.md, section 2.2) |

Condition de validité commune : au moins 6 JP facturables par mois engagées à deux (`travaux/strategie-retenue.md:55`). Sous ce seuil, on réduit au cadrage et à un lot, ou on reporte (`travaux/strategie-retenue.md:696`).

---

## 4. Comparaison avec les 20 et 40 journées des archives

| Formule des archives | Ce qu'elle demande [ES] | Verdict |
| --- | --- | --- |
| Base : 20 JP, 15 000 € HT par mois, « 10 jours, environ un mi-temps » pour chacun (`interne/offre-marwin-tech-remuneration-et-collaboration.md:13-15`) | 20 JP facturables + 6,75 JP non facturables = 26,75 JP pour Marwin, soit **90 % du temps planifiable des deux** (78 à 83 % du temps disponible selon la synthèse capacité, `travaux/syn-capacite-ia.md:228`). Par personne : ≈ 13,4 JP sur 14,9 planifiables. Production pure : ≈ 6,4 JP | **Ce n'est pas un mi-temps : c'est presque un plein temps chacun.** Tenable seulement dans le scénario haut, si les autres activités tombent à ≈ 1,5 JP par mois chacun |
| Renforcement : 40 JP, 30 000 € HT par mois, « environ un plein temps » (`interne/offre-marwin-tech-remuneration-et-collaboration.md:14-15`) | 46,75 JP pour Marwin, soit **157 % du temps planifiable des deux** (140 à 145 % du temps disponible selon `travaux/syn-capacite-ia.md:229`) | **Impossible à deux.** Il manque ≈ 17 JP par mois, soit une personne à plein temps, à recruter ou à sous-traiter, avec son encadrement |
| « Ancre » : renforcement plus pilote laboratoire (`interne/offre-marwin-tech-remuneration-et-collaboration.md:246`), ≈ 46 JP | ≈ 53 JP pour Marwin, ≈ 177 % du temps planifiable | **Impossible.** L'audit du laboratoire le notait : à 26 JP, « il resterait 14 jours pour administration, vente et autres travaux », et « leur disponibilité n'est pas établie » (`interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` p. 8) [FV] |
| « Mener les huit propositions de front demande plus de 20 journées par mois » (`interne/offre-marwin-tech-remuneration-et-collaboration.md:63`) ; les huit propositions de `sources/propositions-de-collaboration.pdf` p. 1 | 2,5 JP par proposition, dont 1 à 1,5 JP de suivi minimal | **Irréaliste** : 1 à 1,5 JP de production par proposition et par mois (`travaux/syn-capacite-ia.md:231`) |
| Premier mois de 20 JP « déjà réparti » : 6 cadrage, 7 CRM, 4 copilote, 3 coordination (`interne/offre-marwin-tech-remuneration-et-collaboration.md:54-61`) | Ignore 9 à 17 JP de démarrage non facturables et l'attente des accès | **Intenable** au premier mois ; remplacé par le seul cadrage de 8 JP |
| « Disponibilité pendant trente jours calendaires » | ≈ 21 jours ouvrés, 14,9 JP planifiables par personne | Garde-fou de l'archive du 29 oct. (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:64`), perdu dans la version du 2 nov. ; à rétablir |

**Ce que vaut la capacité centrale en chiffre d'affaires.** Au plancher interne de 750 € par JP, 10 JP représentent 7 500 € HT par mois ; la stratégie vise environ 8 000 € HT par mois en régime central, vendus au périmètre et au livrable, pas au temps (`travaux/strategie-retenue.md:499`). La moitié des 15 000 € de la formule de base, avec deux fois moins de temps.

---

## 5. Nombre de projets simultanés soutenable

Hypothèses de la synthèse capacité [ES] (`travaux/syn-capacite-ia.md:244-248`) : un socle de pilotage coûte 2 à 3 JP par mois ; chaque projet actif demande 1 à 1,5 JP de suivi ; un projet n'avance vraiment qu'avec au moins 2 à 3 JP de production par mois. Dans l'architecture retenue, le suivi est dans le socle et la production dans les lots (`travaux/strategie-retenue.md:383`).

| Scénario | Capacité | Socle | Projets actifs suivis | En veille | Lots en production en même temps | Exploratoire | Autre client |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Prudent | ≈ 6 JP | Socle léger « socle + 1 projet » (≈ 3 JP) | **1** | 1 | **Au plus 1, un trimestre sur deux environ** | 0 | 0 |
| Central | ≈ 10 JP | B1 « socle + 2 projets » (≈ 5,5 JP) | **2** | 1 | **1 à la fois** (≈ 4 JP par mois) | 0 | À partir du mois 7, ≈ 2 JP par mois, à la place d'une partie des lots (`travaux/strategie-retenue.md:522`) |
| Haut | ≈ 18 JP | « Socle + 3 projets » (≈ 6,5 à 7 JP) ; B2 (4 projets) après trois mois de B1 aux critères | **3**, puis 4 | 2 | 2 | 1 au plus, ≤ 10 % de la capacité, financé par écrit, pas avant le mois 6 (`travaux/strategie-retenue.md:644-645`) | Oui |

**Ce que cela veut dire en central.** Avec un seul lot à la fois, un seul des deux projets actifs reçoit de la production un mois donné ; l'autre avance par décisions et coordination [ES]. Deux lots de ≈ 6 000 € en parallèle (≈ 9 JP par mois) plus le socle (≈ 5,5 JP) donneraient ≈ 15 JP : impossible sous 10.

**Règles** [PR] :
1. **Limite d'encours écrite** : « un socle plus N projets actifs ». Une demande nouvelle remplace un projet actif ou devient un lot (`travaux/strategie-retenue.md:283`). Une « priorité » se compte en JP et en livrables, pas en nombre (`travaux/syn-capacite-ia.md:256`).
2. **Un seul lot en production à la fois en central**, deux au plus en haut ; le lot suivant démarre à la livraison du précédent [PR, ce livrable].
3. **Aucun projet exploratoire** sans financeur écrit, budget plafonné et critère d'arrêt (`travaux/strategie-retenue.md:190`).
4. **Un client de plus prend sa place dans les 10 JP**, il ne s'y ajoute pas.

---

## 6. Tâches incompatibles dans le temps

| Tâche A | Tâche B | Pourquoi elles s'excluent | Règle [PR] |
| --- | --- | --- | --- |
| Traitement d'un incident de données ou de sécurité (aujourd'hui : la fuite du dépôt du CRM) | Toute production | L'incident passe avant tout, avec un délai légal de 72 h | Gel des autres travaux ; client prévenu dans des termes validés par le conseil (`travaux/strategie-retenue.md:211`) |
| Remise en ordre des documents | Rendez-vous ou envoi au client | Des documents contradictoires ne doivent pas être présentés | Aucune présentation avant la liste de corrections du diaporama (`travaux/strategie-retenue.md:814-828`) |
| Événement ou visite de plusieurs jours sur place | Clôture mensuelle, rapport au 5e jour ouvré, réception de livrables | Mêmes jours, mêmes personnes | Pas d'événement dans les 3 derniers jours ouvrés du mois ni les 5 premiers |
| Campagne d'appels du pilote commercial (réimport quotidien des résultats, relances) | Journées sur le terrain, tournage, installation | Les résultats doivent être traités dans la journée | Un associé « de permanence campagne » désigné chaque semaine (`travaux/syn-capacite-ia.md:263`) |
| Validation des livrables par Morgan | Déplacements, tournages, autres projets de Morgan | File d'attente de validation | Délégation écrite de la validation technique à Mathys ; contrôle sous 2 jours ouvrés (`travaux/strategie-retenue.md:577`) |
| Contrôle à quatre yeux | Absence de l'autre associé | L'auteur ne peut pas se contrôler lui-même | Document non urgent : il attend. Document urgent : envoyé avec la mention « relu par un seul associé », contrôlé dans les 2 jours ouvrés du retour [PR, ce livrable] |
| Mise en place des outils et des accès (semaines 1 à 4) | Livrables de production promis au mois 1 | Les accès conditionnent la production | Mois 1 : cadrage et accès d'abord ; aucun lot avant les accès |
| Prospection d'un second client | Pics de charge chez GianLuca | La prospection est toujours la variable sacrifiée | Plancher protégé de 1,5 à 2,5 JP par mois (`travaux/strategie-retenue.md:719`) |
| Autres projets de Morgan (OLSEN, Shelby, BOJ.ART) | Engagements nominatifs pour GianLuca | Même personne, mêmes jours | Calendrier partagé des indisponibilités, mis à jour chaque lundi ; plafond écrit des autres activités (section 3.3) |
| Congés des deux associés | Socle récurrent | Personne pour tenir le socle | Congés jamais simultanés ; capacité réduite annoncée en août et fin décembre (section 3.7) |
| Socle (pilotage) | Lot (production) | La capacité du socle ne se convertit jamais en production (`travaux/strategie-retenue.md:283`) | Une tâche, une ligne de relevé, un bon de commande |
| Essai d'une automatisation sur données réelles | Absence des préalables (responsable du traitement, contrat de l'article 28, offres d'IA professionnelles) | Risque de nouvelle exposition | Aucune donnée réelle avant les préalables (`travaux/strategie-retenue.md:669`) |

---

## 7. Dépendances à une seule personne et parades

| Point unique | Ce qui en dépend | Preuve | Parade [PR] | Test [PR, ce livrable] |
| --- | --- | --- | --- | --- |
| **Morgan** | Relation client, prix, arbitrages commerciaux, validation de tout livrable (« Morgan garde les arbitrages commerciaux et la validation du travail livré », `sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md:15`) ; seul responsable de 6 des 12 solutions de l'audit du 2 nov., et de 2 en partage (`travaux/ver-C4-methodes.md:28`) ; artefacts et pages ChatGPT sur ses comptes personnels (`travaux/note-point-4-novembre-et-activites.md:16`) | [FV] / [DR] | Suppléant nommé par processus (section 2.5) ; validation technique déléguée par écrit ; Mathys à un comité sur trois ; procédures et modèles écrits ; documents du client sur les comptes de son entité | Une semaine par trimestre (pendant les congés de Morgan), Mathys tient seul le socle : comptes rendus sous 24 h, registre à jour, aucune décision perdue |
| **Mathys** | Code et dépôt du CRM (`README.md:35`) ; mesures techniques en cas d'incident ; comptes techniques à venir | [DR] | Dépôt transféré à un compte de Marwin ou de l'entité cliente ; deux administrateurs ; procédure de restauration écrite | Une fois par trimestre, Morgan restaure le registre et le CRM dans un espace neuf |
| **GianLuca Carlone** | Toutes les décisions, les accès, la validation ; aucun délégué connu | `travaux/syn-capacite-ia.md:276` | Délégué nommé ; réponse sous 5 jours ouvrés ; « une absence de réponse ne vaut pas approbation » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:103`) | Seuil des décisions bloquantes (section 8, n° 6) |
| **Un seul client** | 100 % du chiffre d'affaires en central | `travaux/strategie-retenue.md:514` | Plancher de prospection ; variante avec un second client au mois 7 ; dépendance assumée par écrit sinon | Part de GianLuca ≤ 80 % au mois 12, ou décision écrite de l'assumer |
| **Compte qui héberge le CRM en service** | Suivi des appels ; propriétaire non nommé | `travaux/syn-capacite-ia.md:278` | Export immédiat ; hébergement sur un compte de l'entité cliente ; sauvegarde quotidienne | Restauration testée |
| **Fournisseurs d'IA** | Toute la production assistée (48 commits sur 56 signés « Claude ») | [FV] (`git log`, 4 nov. 2026) | Deux fournisseurs configurés ; consignes portables ; fiche de secours manuel par processus | Une journée « mode dégradé » par trimestre, sans le fournisseur principal |
| **Moyens de paiement des abonnements** | Outils de travail | Échecs de prélèvement depuis fin octobre (`travaux/note-point-4-novembre-et-activites.md:8`) | Carte professionnelle de Marwin ; alerte sur échec ; abonnements du client à son nom | Revue mensuelle des abonnements |
| **Quali Contact** (voie commerciale seulement) | Tous les appels si l'externalisation se confirme ; outil inconnu | `travaux/syn-capacite-ia.md:280` | Format d'échange écrit avant tout développement ; appelant de secours désigné | — |

**Indisponibilité d'un associé plusieurs semaines.** L'autre fait tourner seul le socle. La capacité tombe à environ 4 à 6 JP par mois en central [ES], dans la fourchette de 4 à 8 JP de la stratégie (`travaux/strategie-retenue.md:533`). Le socle passe au palier B0 sans pénalité au-delà de 10 jours ouvrés d'absence, et les lots sont reportés (`travaux/strategie-retenue.md:281`). L'effet sur la trésorerie est chiffré dans `modele-financier/stress-tests.md` (section « Indisponibilité d'un associé pendant six semaines »).

---

## 8. Seuils de saturation et réponses

### 8.1 Tableau des seuils

Les seuils sont mesurés chaque semaine dans le registre et le relevé du temps, et revus à la revue mensuelle (section 10). « Vigilance » déclenche une information ; « action » déclenche la réponse prévue, décidée par écrit. Les seuils qui touchent GianLuca sont repris dans le contrat (12-gouvernance-contrat-sortie.md).

| N° | Indicateur | Mesure | Vigilance | Action | Réponse | Qui décide | Source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Occupation par personne, sur tout son temps** | (Marwin + autres activités) ÷ temps disponible du mois | > 85 % | > 95 % deux mois de suite, ou > 100 % plus de deux semaines | **Refuser** tout nouveau projet ; puis **sous-traiter** un lot ; au 3e mois au-delà de 85 %, **recruter** seulement si un contrat renouvelé le finance, sinon **réduire** | Morgan et Mathys | `travaux/strategie-retenue.md:623, 678` |
| 2 | Consommation de la capacité réservée | JP consommées ÷ JP réservées, par bon de commande | > 90 % avant le 20 du mois | > 100 % | Dès 90 % avant le 20 : arrêt des travaux non urgents ; au-delà de 100 % : **avenant** écrit (offre E) ou **report** ; jamais de travail gratuit | GianLuca, par écrit | `travaux/strategie-retenue.md:593` |
| 3 | Socle B1 au-delà de sa référence | JP du socle dans le mois | > 5,5 JP un mois | > 5,5 JP deux mois de suite | Bilan trimestriel : **réduire** (un dossier ou un projet en veille de moins) ou relever le prix au renouvellement | Morgan et Mathys, puis comité | 04-catalogue-offres.md, encadré sur B1 |
| 4 | Tâches en attente | JP des tâches acceptées non commencées ÷ capacité restante du mois | > 1,0 | > 1,5, ou plus de 10 tâches en attente depuis plus de 10 jours ouvrés | **Reporter** : GianLuca choisit ce qui sort du mois ; les sorties sont consignées | GianLuca, sur proposition de Morgan | `travaux/syn-capacite-ia.md:291` |
| 5 | Retards | Livrables en retard de plus de 5 jours ouvrés | 1 | 2 dans le mois, ou un jalon critique en retard de plus de 10 jours ouvrés | **Réduire** le périmètre du mois suivant ; cause écrite (accès, décision attendue, capacité) | Comité mensuel | `travaux/syn-capacite-ia.md:292` |
| 6 | Décisions bloquantes attendues du client | Jours ouvrés depuis la demande | > 5 (relance) | > 10 : report des jalons ; > 15 : revue du contrat ; deux décisions à plus de 15 jours : signal de suspension | **Reporter**, puis **réduire** de palier ; jamais d'autorisation tacite | Morgan informe ; GianLuca décide | `travaux/strategie-retenue.md:603, 677` |
| 7 | File de validation interne | Jours ouvrés d'attente avant contrôle | > 2 | > 4 | **Renforcer** : délégation écrite de la validation technique à Mathys ; réaffectation du contrôle | Morgan et Mathys | `travaux/syn-capacite-ia.md:295` |
| 8 | Charge de contrôle d'un processus assisté par IA | (Contrôle + corrections) ÷ production, sur 2 semaines | > 30 % | > 50 % ; pour un pilote, relecture et corrections > 50 % du temps de référence pendant 4 semaines | Retour au **mode manuel** ou à une assistance plus légère ; abandon si aucune baisse en 4 semaines | Responsable du processus | `travaux/syn-capacite-ia.md:294` ; `travaux/strategie-retenue.md:176` |
| 9 | Corrections | Livrables refusés au premier passage ÷ livrables présentés | > 20 % | > 35 %, ou plus de 2 cycles sur un même livrable | Re-cadrer le livrable (critères écrits) ; pas de nouveau lot du même type avant correction | Comité mensuel | `travaux/syn-capacite-ia.md:297` |
| 10 | Incidents | Par processus et par mois | 1 incident mineur | 1 incident critique (exposition de données, action non autorisée, envoi erroné, perte de données), ou 2 mineurs sur le même processus | **Arrêt** immédiat ; reprise manuelle ; fiche d'incident ; information écrite du client sous 24 h ; notification légale si nécessaire | Quiconque constate arrête ; Morgan informe | `travaux/syn-capacite-ia.md:296` ; `travaux/strategie-retenue.md:585` |
| 11 | Urgences hors plages | Nombre par mois | 1 | 2 dans le mois ; plus de 2 : astreinte ou refus | À 2 : **avenant** à 900 € HT par JP ou **report**, jamais d'absorption gratuite ; au-delà : astreinte seulement par forfait séparé, sinon **refus** | GianLuca et Marwin | `travaux/strategie-retenue.md:203, 354-355, 534` |
| 12 | Demandes hors périmètre | JP demandées hors bon de commande ÷ capacité du mois | > 10 % [PR, ce livrable] | > 20 % deux mois de suite (signal de suspension) | **Réduire** : lot séparé, avenant ou refus | Morgan, validé par Mathys | `travaux/strategie-retenue.md:679` |
| 13 | Prospection sacrifiée | JP réalisées ÷ plancher prévu | < 75 % | < 50 % deux mois de suite (signal de suspension) | **Réduire** le périmètre client pour libérer le plancher | Morgan et Mathys | `travaux/syn-capacite-ia.md:301` ; `travaux/strategie-retenue.md:678` |
| 14 | Écart d'estimation | JP réelles ÷ JP estimées (cadrage, lots) | > 110 % | > 125 % | Provision de risque, puis **avenant** signé avant le travail ; estimations suivantes corrigées | Morgan | `travaux/strategie-retenue.md:171, 287` |
| 15 | Maintenance d'un processus en exploitation (offre D) | JP par mois et par processus | > 0,5 | > 0,5 deux mois de suite (recherche documentaire : > 1 JP) | Revoir le prix au renouvellement ou **arrêter** le processus | Mathys propose ; comité | `travaux/strategie-retenue.md:349` ; `travaux/syn-capacite-ia.md:739` |
| 16 | Absence imprévue d'un associé | Jours ouvrés d'indisponibilité | > 5 | > 10 | **Réduire** : palier B0 sans pénalité ; lots **reportés** ; validations déléguées | Morgan et Mathys ; client informé | `travaux/strategie-retenue.md:281, 533` |
| 17 | Impayés | Jours après l'échéance | > 0 : relance le lendemain | Relance restée sans effet 8 jours | **Suspension** des travaux non urgents ; résiliation possible à 30 jours de retard | Morgan | `travaux/strategie-retenue.md:463` |

### 8.2 Choisir la réponse

Ordre recommandé (`travaux/syn-capacite-ia.md:304-309`) :

| Réponse | Quand | Comment | Limite |
| --- | --- | --- | --- |
| **1. Reporter** | La cause est une décision du client ou un pic ponctuel | GianLuca choisit ce qui sort du mois ; jalons décalés et consignés | Ne règle rien si la cause est un engagement trop large |
| **2. Réduire le périmètre** | L'engagement est trop large pour la capacité | Un projet passe en veille ; un dossier de décision de moins ; palier inférieur (B2 → B1 → B0) ; lot découpé | Le prix suit le palier ; aucun travail gratuit pour « tenir » le périmètre |
| **3. Renforcer en interne** | La cause est interne et passagère (validation, absence) | Délégation de validation ; réaffectation entre associés ; part pour Marwin relevée **seulement si l'occupation reste ≤ 85 %** | Ne touche jamais au plancher de prospection ni à la marge de 15 % plus d'un mois |
| **4. Sous-traiter un lot délimité** | La surcharge dure plus d'un mois sur un travail sous-traitable (contenus, développement, photographie) | 450 à 550 € HT par JP [HY] ; contrat écrit, confidentialité, contrat de l'article 28 si des données personnelles circulent ; attestation de vigilance dès 5 000 € HT cumulés (`travaux/strategie-retenue.md:503`) ; décision des deux associés à l'unanimité (`travaux/strategie-retenue.md:614`) | Le contrôle du sous-traitant consomme du temps d'associé, environ 15 à 25 % du temps sous-traité [HY] ; jamais la relation client ni la validation |
| **5. Recruter** | Après trois mois au-delà de 85 % d'occupation **et** un contrat renouvelé qui finance le poste | Par décision unanime, après bilan avec l'expert-comptable | Si le besoin stable de GianLuca dépasse 6 à 8 JP par mois, un coordinateur salarié **chez lui** coûte moins cher que Marwin (`travaux/strategie-retenue.md:108, 378`) : proposer d'abord l'offre C6 (outillage et passation) plutôt qu'un recrutement chez Marwin |
| **Refuser ou suspendre** | Un signal de la stratégie est atteint (`travaux/strategie-retenue.md:673-685`) | Écrit motivé ; travaux non urgents arrêtés | Les données et documents du client lui restent toujours restituables |

---

## 9. « Le travail de 100 personnes à deux », traduit en mesures

Morgan demande de traduire cette ambition « en processus, volumes, délais, niveaux de qualité et responsabilités mesurables » (`travaux/DEMANDE.md:18`).

### 9.1 L'ordre de grandeur

- Cent personnes représentent environ 1 750 JP disponibles par mois [ES] (`travaux/strategie-retenue.md:163`).
- Il faudrait que chaque journée de Morgan ou de Mathys produise 50 à 85 fois une journée ordinaire, contrôle compris [ES] (même source). Rapporté au temps réellement consacré à Marwin (17 JP en central, 27 en haut), le facteur serait de 65 à 100 [ES].
- Aucune pièce n'approche ce facteur. Les pièces montrent plutôt que **produire n'est pas livrer** : CRM de 500 fiches sans appel ni vente, dépôt BOJART de 933 fichiers sans installation réelle, 36 propositions OLSEN non envoyées, sept états de l'offre sans réaction client documentée (`travaux/syn-capacite-ia.md:777-782`). Le corpus d'offres de Morgan le dit lui-même : « les pipelines produisent déjà plus que ce que le carnet d'adresses absorbe », et la personne à recruter « appelle, elle ne code pas » [DR] (`travaux/ex-C4-methodes.md:87`).

**La contrainte est en aval de la production** : vente, validation, décision du client, réception, adoption.

### 9.2 Traduction par processus

Volumes du socle B1 et des pilotes de la stratégie. Les protocoles complets sont dans 07-processus-ia-et-essais.md ; seuls les engagements mesurables sont repris ici.

| Processus | Volume mensuel | Délai | Qualité | Exécute / contrôle | Référence à mesurer | Cible [HY] |
| --- | --- | --- | --- | --- | --- | --- |
| Comptes rendus et registre des décisions (pilote P1) | 4 à 5 réunions ; ≥ 20 décisions ou actions | Compte rendu sous 24 h ouvrées dans ≥ 90 % des cas | 100 % des décisions avec responsable, date et source ; au plus 1 correction de fond par compte rendu | Morgan / Mathys | Temps par réunion relevé pendant le cadrage (`travaux/strategie-retenue.md:170`) | Temps humain ≤ 70 % de la référence à 6 mois (`travaux/syn-capacite-ia.md:704`) |
| Dossiers de décision | 2 par mois dans B1 | Remis au moins 2 jours ouvrés avant la réunion [PR, ce livrable] | Décisions préparées à temps ≥ 85 % à 6 mois, ≥ 90 % à 12 mois | Morgan / Mathys | Délai de décision mesuré au premier trimestre | Délai de décision −25 % à 6 mois, −40 % à 12 mois (`travaux/syn-capacite-ia.md:806`) |
| Recherche documentaire avec citations (pilote P3) | Jeu de 60 questions, puis usage ≥ 3 fois par semaine | Réponse vérifiée | ≥ 90 % de réponses justes avec citation exacte ; 0 citation inventée | Mathys / Morgan | 30 questions traitées à la main | ≤ 50 % du temps de référence (`travaux/syn-capacite-ia.md:736`) |
| Qualification CRM (pilote P2, voie commerciale) | 20 comptes | 2 semaines de préparation | ≥ 90 % des champs sourcés et datés ; 100 % des oppositions respectées | Mathys / Morgan | 5 fiches qualifiées à la main, chronométrées | Temps par fiche acceptée connu ; prix jamais sous le coût manuel (`travaux/strategie-retenue.md:126`) |
| Détection des incohérences (pilote P4, facultatif) | Avant chaque envoi au client | — | Rappel ≥ 70 %, et 100 % sur prix, paiement et propriété | Mathys / Morgan | Jeu des contradictions connues de l'audit | Tri ≤ 5 min par alerte |
| Couverture du portefeuille | Projets actifs suivis par le socle | — | Registre à jour pour 100 % des projets actifs | Morgan | B1 : 2 projets pour ≈ 5,5 JP | 3 projets pour ≈ 5,5 JP à 12 mois, soit +50 % de projets par JP de socle ; le projet en plus est proposé par Marwin, au prix du socle (`travaux/strategie-retenue.md:419`) |

### 9.3 Indicateurs de démultiplication

| Indicateur | Définition | Départ | 6 mois [HY] | 12 mois [HY] | Qui le mesure |
| --- | --- | --- | --- | --- | --- |
| Résultats acceptés par JP | Livrables acceptés au 1er ou au 2e passage ÷ JP consommées, par type | [IN] : à mesurer au mois 1 | +20 % sur les processus pilotés | +30 à +50 % | Mathys, à partir du relevé |
| Temps humain par résultat accepté | Préparation, exécution, contrôle, corrections et reprises | Référence mesurée avant l'essai | −30 % sur P1 et P3 | −30 à −50 % sur 4 processus | Mathys |
| Équivalent temps humain évité | Heures de la méthode de référence ÷ heures réellement passées | 1,0 | **1,3 à 1,5** | **1,5 à 2** | Mathys ; publié au client (`travaux/strategie-retenue.md:423`) |
| Coût complet par résultat accepté | Temps × coût interne + outils + maintenance | [IN] | Stable ou en baisse | En baisse | Morgan, avec l'expert-comptable |
| Taux de corrections | Refus au premier passage | [IN] | < 20 % | < 15 % | Comité mensuel |
| Incidents critiques | Par mois | Une violation de données probable | 0 | 0 | Mathys |
| Occupation des associés | Section 8, n° 1 | [IN] | ≤ 85 % | ≤ 85 % | Revue mensuelle |
| Résultats qui dépendent de GianLuca | Décisions prises, rendez-vous, ventes | 0 constaté | Suivis à part | Suivis à part | Comité ; jamais promis |

Sources : `travaux/syn-capacite-ia.md:800-812` ; `travaux/strategie-retenue.md:163, 171`.

### 9.4 Ce qu'on peut dire honnêtement

- **Calcul** [ES] : en central, le temps pour Marwin vaut environ une personne à plein temps (17,1 JP pour 17,5). Avec un facteur de 1,5 à 2 sur les processus pilotés, cela fait au mieux le travail de 1,5 à 2 personnes sans outils. En haut (26,8 JP), au mieux 2,3 à 3 personnes. Ce sont des bornes hautes : le facteur ne s'applique qu'aux processus pilotés, pas aux réunions, aux déplacements ni à la vente.
- **Formulation proposée** [PR, ce livrable] : « À deux, avec l'IA, piloter un portefeuille borné de deux à trois projets actifs avec la régularité d'une équipe de deux personnes (trois au plus dans le scénario haut), mesurée chaque mois par les résultats acceptés, les délais tenus et le temps humain par résultat accepté. »
- **Ce qui est plausible** [HY] (`travaux/syn-capacite-ia.md:788-794`) : débit multiplié par 2 à 10 sur des tâches étroites et vérifiables ; plus de projets suivis à effort égal ; dossiers de décision plus complets ; 10 à 30 % de capacité libérée la première année sur les processus pilotés.
- **Ce qui ne l'est pas** : remplacer la relation, la présence sur les lieux et la négociation ; couvrir 24 h sur 24 et 30 jours sur 30 (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:105`) ; des agents qui envoient, achètent ou publient sans approbation ; supprimer le contrôle humain, qui pèse 15 % de la capacité facturable.
- **Usage** : « 100 personnes » peut rester une image interne. Un document destiné à GianLuca ne promet aucun facteur ni aucun résultat (`travaux/strategie-retenue.md:798`) ; il montre des résultats mesurés. Les cibles de 1,3 à 2 se fixent avec lui après la mesure de référence, et l'« équivalent temps humain évité » lui est publié une fois mesuré (`travaux/strategie-retenue.md:163, 423`).

---

## 10. Rituels entre associés et relevé du temps

### 10.1 Rituels

| Rituel | Rythme | Durée | Qui | Contenu | Ce qui en sort | Coût pour deux [ES] |
| --- | --- | --- | --- | --- | --- | --- |
| **Point de planification** | Chaque lundi | 30 min | Les deux | Calendrier partagé des indisponibilités ; tâches de la semaine par bon de commande ; file de validation ; permanence campagne ; alertes de la semaine | Registre mis à jour ; responsable et suppléant de chaque tâche | ≈ 0,6 JP par mois |
| **Contrôle à quatre yeux** | Au fil de l'eau | Sous 2 jours ouvrés | L'associé qui n'est pas l'auteur | Relecture de tout document envoyé au client ; vérification dans le registre « décision → documents touchés » | Visa daté dans le registre | Compté dans le contrôle (15 % de la capacité facturable) |
| **Relevé du temps** | Chaque jour ; clôture le vendredi | ≈ 3 min par jour, 10 min le vendredi | Chacun | Section 10.2 | Relevé de la semaine | ≈ 0,5 JP par mois |
| **Revue mensuelle de capacité** | Avant le 5e jour ouvré, avant le rapport au client | 1 h 30 | Les deux | Occupation de chacun sur tout son temps ; les dix-sept seuils ; réponses à décider ; prospection ; impayés ; capacité du mois suivant (congés compris) | Décisions écrites ; données du rapport mensuel au client | ≈ 0,4 JP par mois |
| **Revue trimestrielle du pacte** | Chaque trimestre | 2 h | Les deux | Disponibilités et autres activités ; rémunération ; tests de suppléance, de restauration et de mode dégradé ; risques ; prix (révision prévue au mois 6) | Fiche « rôles et disponibilités » mise à jour et signée | ≈ 0,2 JP par mois |
| **Bilan du mois 6** | Une fois | Une demi-journée | Les deux, avec l'expert-comptable | Coût complet mesuré par JP ; taux de référence révisé ; écarts d'estimation ; décision sur le socle récurrent | Décisions écrites (`travaux/strategie-retenue.md:169`) | — |

**Coût total** : environ 1,5 à 2 JP par mois pour deux [ES]. Le point du lundi relève de la coordination des projets (réunions, 22 % de la capacité facturable). La revue mensuelle, la revue trimestrielle et le relevé relèvent de l'administration de Marwin : sur les 2 JP prévus, il en reste environ 1 pour la comptabilité, les factures, la banque, les assurances et le registre des traitements. C'est serré ; d'où la sensibilité de la section 3.3.

**Désaccord entre associés.** Les règles de la stratégie s'appliquent : décisions à l'unanimité listées au pacte, rien n'est proposé au client tant que le désaccord dure, puis médiation (`travaux/strategie-retenue.md:614`). La revue mensuelle est le lieu où un désaccord est écrit, pas tranché en silence.

### 10.2 Relevé du temps

**But.** Mesurer ce que le binôme consomme vraiment, par bon de commande et par poste, pour : tenir les seuils de la section 8 ; vérifier les estimations (cadrage : écart ≤ 25 % sur 8 JP, `travaux/strategie-retenue.md:171`) ; calculer le coût complet par JP au mois 6 ; mesurer les gains des processus assistés. Le temps sert à mesurer, pas à vendre (`travaux/strategie-retenue.md:186`).

**Format** [PR, ce livrable] :

| Champ | Contenu |
| --- | --- |
| Date, personne | — |
| Code | Bon de commande (cadrage, socle, lot, exploitation, avenant) ; ou code interne : remise en ordre, administration, prospection, maintenance interne, capitalisation ; ou **AUTRE** (activités hors Marwin, en bloc, sans détail) |
| Poste | Production ; collecte ; contrôle et corrections ; réunion ; déplacement ; maintenance ; administration ; prospection |
| Processus | Pilote P1, P2, P3, P4, ou aucun |
| Assistance IA | Oui ou non |
| Reprise | Oui si le temps corrige un livrable refusé |
| Livrable | Référence dans le registre |

**Règles** :
- unité d'un quart d'heure ; une JP vaut 7 h ;
- **tout** le temps travaillé est relevé, y compris les autres activités en bloc : sans cela, l'occupation sur tout le temps ne se mesure pas (`travaux/strategie-retenue.md:619`, déclaration écrite des autres activités au pacte) ;
- deux associés en réunion : deux lignes ;
- seul le temps humain compte, pas l'attente d'un traitement par un outil ;
- aucune ligne sans code : l'indicateur « 0 JP hors bon de commande » se lit directement (`travaux/strategie-retenue.md:171`) ;
- relevé commencé **dès la remise en ordre de novembre 2026**, pour remplacer l'estimation de 9 à 17 JP par une mesure ;
- outil : un tableur partagé ou une base Notion ou Airtable dans l'espace de Marwin, sans développement ; export mensuel conservé avec les sauvegardes.

**Ce qui va au client, ce qui reste interne.**

| Remis à GianLuca chaque mois | Reste interne |
| --- | --- |
| JP consommées par bon de commande de son entité, livrables, décisions attendues (`travaux/strategie-retenue.md:382`) | Lignes AUTRE ; occupation ; prospection ; administration ; coût complet ; écarts d'estimation ; marges |

---

## 11. Recommandations : preuve, hypothèse, limite, décision

| Recommandation | Preuve | Hypothèse | Limite | Décision correspondante |
| --- | --- | --- | --- | --- |
| Engager une capacité nominative de 10 JP facturables au plus en central (6 en prudent), et la lire comme la capacité elle-même, pas comme une marge | Calcul de la section 3.3 [ES] ; capacité de 7 / 12 / 20 sans marge sur tout le temps (`travaux/syn-capacite-ia.md:190`) ; 10 JP ≈ 94 % du temps central (`travaux/juge-J2-marwin.md:195`) | Parts de 65 et 50 % ; postes non facturables de la synthèse capacité | Disponibilités réelles [IN], surtout celles de Mathys | Décision n° 3 de la stratégie : fiche « rôles et disponibilités » |
| Plafonner par écrit les autres activités (≈ 5 JP pour Morgan, ≈ 7,5 pour Mathys en central) | Liste des projets parallèles de Morgan [FV pour la liste] (`travaux/note-point-4-novembre-et-activites.md:9-17`) | Les autres activités continuent | Le temps réel passé sur OLSEN, Shelby et BOJ.ART est [IN] | Pacte : déclaration des autres activités et règle de priorité (`travaux/strategie-retenue.md:619`) |
| Un seul associé par réunion client ; deux JP seulement si le bon de commande le prévoit | 2,5 contre 3,7 JP par mois de réunions récurrentes [ES] (`travaux/syn-capacite-ia.md:205-210`) | Le client accepte un interlocuteur à la fois | Certaines décisions demandent les deux | Fiche de mission du socle |
| Déléguer par écrit la validation technique à Mathys ; contrôle à quatre yeux sous 2 jours ouvrés ; un suppléant par processus | Morgan seul validateur (`sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md:15`) ; 6 solutions de l'audit du 2 nov. portées seul (`travaux/ver-C4-methodes.md:28`) | Mathys a les compétences pour valider | Compétences propres de Mathys [IN] | Décision n° 3 de la stratégie |
| Un lot à la fois en central ; limite d'encours « socle + 2 projets » ; aucun exploratoire | Section 5 [ES] | Lot moyen ≈ 4 JP par mois | Durée réelle des lots non mesurée | Fiches de mission ; 04-catalogue-offres.md |
| B0 et B1 : deux dossiers de décision par mois et une visite comprise | Décompte de la section 3.6 [ES] | Durées unitaires de la section 3.6 | Non mesuré avant B0 | Fiche de mission de B0 |
| Congés jamais simultanés ; capacité réduite annoncée en août et fin décembre | Section 3.7 : 6,2 JP en août si congés simultanés [ES] | Répartition des congés | Congés réels [IN] | Fiche « rôles et disponibilités » ; contrat (12-gouvernance-contrat-sortie.md) |
| Appliquer les dix-sept seuils avec leur réponse écrite | Seuils de `travaux/syn-capacite-ia.md:289-302` et `travaux/strategie-retenue.md:593, 623, 673-685` | Mesure hebdomadaire possible avec un relevé simple | Seuils non éprouvés ; à ajuster après trois mois | Décision n° 5 de la stratégie (garde-fous) |
| Relever tout le temps dès novembre 2026, y compris les autres activités en bloc | Aucune mesure de temps n'existe [FV négatif] ; gain de temps « à mesurer » (`sources/chatgpt-pages/2026-11-04-complement/pilotage-extraits-carlone.md:20`) | Discipline tenue ≈ 3 min par jour | Coût ≈ 0,5 JP par mois | Revue mensuelle |
| Traduire « 100 personnes » en indicateurs de résultats acceptés ; cible 1,3 à 1,5 à 6 mois, 1,5 à 2 à 12 mois | Section 9 ; aucune pièce n'approche ×50 [FV négatif] | Les pilotes P1 et P3 réussissent | Aucun gain mesuré à ce jour [IN] | Objectif à 6 et 12 mois (`travaux/strategie-retenue.md:143-145`) |
| Recruter seulement après trois mois au-delà de 85 % et un contrat renouvelé ; proposer d'abord C6 au client | Seuil de 6 à 8 JP stables (`travaux/strategie-retenue.md:108`) | Le besoin du client est stable | Coûts cachés d'un recrutement non chiffrés [IN] | Pacte (unanimité) |

---

## 12. Questions bloquantes et limites

**Questions à Morgan et Mathys** (reprennent et précisent les questions 7 et 8 de `travaux/strategie-retenue.md:734-735`) :
1. Combien de JP par mois chacun engage-t-il par écrit de décembre 2026 à juin 2027, et quel plafond fixe-t-il à ses autres activités ?
2. Quelle est la situation de Mathys (emploi, études, autres projets) ? Quelles réalisations personnelles peut-il montrer (code, projets) ?
3. Quels projets Morgan suspend-il (OLSEN, Shelby, BOJ.ART, ventes en ligne), et à partir de quand ?
4. Où habitent-ils, et combien de temps faut-il pour aller à Cosne-Cours-sur-Loire ?
5. Quelles périodes de congés prévoient-ils en 2027, et peuvent-ils les décaler l'un par rapport à l'autre ?
6. Eaglemic (Michael Bach) a-t-il un rôle dans Marwin ?
7. Acceptent-ils le relevé de tout leur temps, y compris les autres activités en bloc ?

**Question à GianLuca Carlone** (ordre du jour du rendez-vous, 13-preparation-rendez-vous.md) : quelle présence attend-il (visites, réunions, délais de réponse), et qui sera son délégué ?

**Limites.**
- Les disponibilités de Morgan et de Mathys ne sont documentées nulle part [IN] (`travaux/strategie-retenue.md:840`) : tous les chiffres de capacité sont des scénarios.
- Les ratios de ventilation, les durées du socle et les postes non facturables sont des estimations, à remplacer par le relevé dès le premier mois.
- Aucune pièce ne rapporte une parole directe de GianLuca Carlone : ses attentes de présence et de délai sont [IN] (`travaux/syn-sources.md:38`).
- Les durées de déplacement sont inconnues ; le poste « déplacements » (10 %) peut être sous-estimé.
- Les seuils n'ont jamais été appliqués ; leurs valeurs seront revues après trois mois de mesure.
- Les compétences sont jugées sur des objets produits avec des assistants IA ; la part de travail personnelle de chaque associé reste [IN].

---

Relu et contrôlé le 4 novembre 2026 : 30 vérifications, 9 corrections.
