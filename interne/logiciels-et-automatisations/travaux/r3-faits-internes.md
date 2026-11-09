# R3 · Faits internes utiles à une offre de logiciel de gestion des propriétés

Audit Marwin Tech × GianLuca Carlone · dossier « logiciels et automatisations » · travail R3 : relevé des faits internes du dépôt · 9 novembre 2026
Statut : **interne** (ne pas transmettre à GianLuca Carlone). Contient des planchers de prix, la capacité des associés, des défauts de sécurité et le nom d'un concurrent.
Sources principales : tout le dépôt, lu en lecture seule au commit 4c7027c (9 nov. 2026) : `audit/`, `interne/`, `sources/`, `crm/`, `pour-carlone/`, `tools/` ; copie de travail de la présentation du 9 nov., hors dépôt ; déclarations de Morgan Olsen du 9 nov. 2026, non écrites dans le dépôt.
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ; [MM] mesuré ; [IN] inconnu. « [ES, calculé ici] » signale un calcul fait pour ce relevé. « [PR, R3] » signale une proposition nouvelle de ce relevé. JP : journée-personne de 7 h.

**Abréviations** (chemins depuis la racine du dépôt ; `:12` = ligne 12) :

| Abrév. | Fichier |
| --- | --- |
| AUD | `audit/2026-11-04-audit-strategique/README.md` |
| STRAT | `audit/2026-11-04-audit-strategique/annexes/travaux/strategie-retenue.md` |
| CARTO | `audit/2026-11-04-audit-strategique/interne/03-cartographie-projets.md` |
| CAT | `audit/2026-11-04-audit-strategique/interne/04-catalogue-offres.md` |
| CAP | `audit/2026-11-04-audit-strategique/interne/06-fonctionnement-a-deux.md` |
| PRO7 | `audit/2026-11-04-audit-strategique/interne/07-processus-ia-et-essais.md` |
| GOUV | `audit/2026-11-04-audit-strategique/interne/12-gouvernance-contrat-sortie.md` |
| REG | `audit/2026-11-04-audit-strategique/interne/14-registre-risques-inconnues-decisions.md` |
| MAJ | `audit/2026-11-04-audit-strategique/interne/2026-11-09-mise-a-jour-faits-nouveaux.md` |
| PROP9 | `audit/2026-11-04-audit-strategique/pour-gianluca/2026-11-09-proposition-de-cadrage.md` |
| SYND | `audit/2026-11-04-audit-strategique/annexes/travaux/syn-droit.md` |
| C5, C7J, C9 | `audit/2026-11-04-audit-strategique/annexes/travaux/ex-C5-crm.md`, `ex-C7-jarvis.md`, `ex-C9-lieux.md` |
| R3T, R5, R6 | `audit/2026-11-04-audit-strategique/annexes/travaux/rj-R3-travail-contrats.md`, `rj-R5-art-lieux.md`, `rj-R6-marche.md` |
| R1M | `interne/logiciels-et-automatisations/travaux/r1-marche-et-offre-accord.md` (travail R1 du 9 nov., même dossier) |
| PIA | Présentation « L'IA au service de vos projets » du 9 nov. 2026 : copie de travail hors dépôt, dans le dossier de travail de la session, lue sans modification. `cat-batiments:10` = vue `cat-batiments`, ligne 10 |

**Ce que ce relevé n'a pas fait.** Aucun contact (GianLuca, « Accord », éditeur, prospect). Aucun formulaire, essai, compte ou achat. Aucune modification d'un fichier existant, du CRM ou de la présentation. Aucune recherche web : tout vient du dépôt et de la copie de la présentation.

---

## 0. L'essentiel

1. **« Accord » n'apparaît nulle part dans le dépôt** [FV négatif], hors du travail R1 écrit le même jour. Les PDF ont été lus aussi : les deux occurrences du mot sont des phrases sans rapport (« accord à formaliser »). Tout ce que l'on sait de cette offre vient de Morgan [DR].
2. **Aucune pièce ne parle d'un « logiciel de gestion de propriété »** [FV négatif]. Le besoin le plus proche date du 18 oct. : trois des huit missions proposées par Marwin décrivent déjà un tel outil (suivi des établissements, gestion administrative, outils après chaque rachat) (`sources/propositions-de-collaboration.pdf` p. 1) [PR].
3. **Aucun lieu n'est établi** [FV négatif] (C9:219, repris par CARTO:276). On a des mentions qui se contredisent : un ancien bar-restaurant-hôtel avec cour pour la galerie, six bâtiments, le Vieux Relais, le M, un cabaret, des commerces, 1,5 M€ [DR]. Propriétaire et exploitant sont inconnus pour chaque lieu [IN].
4. **Aucune pièce ne dit que l'hébergement reprendra** [FV négatif]. Les obligations d'un hôtel (hors sécurité incendie) ne sont étudiées nulle part [IN].
5. **La gestion immobilière est exclue pour Marwin** (STRAT:650 ; MAJ:173 ; PROP9:141) : activité réglementée par la loi Hoguet [FV] (R3T:354). Marwin peut outiller et préparer ; elle ne gère ni baux ni loyers (SYND:418) [PR].
6. **L'audit refuse tout développement spécifique au départ** : « Aucun des onze processus ne justifie un développement spécifique » (PRO7:21) [PR]. La présentation du 9 nov. dit la même chose : outils du marché d'abord, liaisons légères ensuite, sur mesure seulement après un essai (PIA `logiciels:9-11`).
7. **La capacité est la contrainte dure** : environ 10 JP facturables par mois en central, dont 3 de production, un seul lot à la fois [ES] (CAP:17, 19, 21, 335). Les 72 000 € par an de la lecture (a) représentent 80 à 96 JP par an, soit 6,7 à 8 JP par mois [ES, calculé ici].
8. **Le CRM offre des modèles techniques, pas une base** : un fichier HTML sans bibliothèque, des scripts Python sans dépendance, un raccord Firebase [FV]. Mais il a des défauts de sécurité connus, il est hébergé chez les associés, sa propriété n'est pas réglée et ses données sont exposées (C5:53-60 ; PRO7:28 ; REG:280).
9. **Rien ne se vend avant le cadrage**, avant une entité nommée, ni avant D03 et D08 (STRAT:42, 44 ; MAJ:370). D52 interdit toute production pour un bâtiment sans mandat (MAJ:374).
10. **La présentation a changé après la note du 9 nov.** : 47 aides, mais 7 « automatiques » au lieu de 13 [MM]. L'empreinte des 26 vues ne correspond plus à celle notée dans PROP9:260 [MM].

---

## 1. Méthode

- **Recherche** (grep, insensible à la casse) dans tout le dépôt, PDF compris (texte extrait) : « Accord », « Accor », « logiciel de gestion », « gestion de propriété », « property management », « PMS », « gestion locative », « gestion immobilière », « hôtel », « chambres », « bâtiment », « Vieux Relais », « le M », « cabaret », « commerce », « baux », « loyer », « suivi des établissements », « après chaque rachat », « Jarvis », « Quali Contact ».
- **Lecture complète** : AUD, STRAT, CAT (sections 1 à 4), CAP (sections 1 à 6), PRO7, MAJ ; **lecture ciblée** : PROP9, GOUV, CARTO, SYND, C5, C7J, C9, R3T, R5, R6, `crm/` (README, passation, version autonome, règles, scripts), `tools/`.
- **Écarté** : `crm/ext/`, `crm/research/` et `crm/site/companies.json` contiennent des données de prospects. Les hôtels qui y figurent sont des entreprises démarchées, pas des lieux de GianLuca.
- **Présentation** : les 26 vues de l'ordre de `deck.json` ; les vues panorama, pilotage, medias et evenements, retirées, ne sont pas lues.

---

## 2. Les faits du 9 novembre et l'offre « Accord »

| N° | Fait | Code | Source |
| --- | --- | --- | --- |
| 1 | GianLuca a engagé « une administrative centrale » pour gérer ses projets | [DR] | MAJ:33 |
| 2 | Il a racheté pour 1,5 M€ de bâtiments | [DR] | MAJ:34 |
| 3 | Plusieurs commerces prévus, dont un cabaret-spectacle à côté de la galerie | [DR] | MAJ:35 |
| 4 | Il a parlé à Marwin d'un « logiciel de gestion de propriété » | [DR] | Morgan, 9 nov., non écrit dans le dépôt |
| 5 | « Accord » lui a proposé « 6 000 € par mois tous les trimestres » | [DR] | Idem |
| 6 | « On peut faire mieux et moins cher grâce à l'IA » | [DR] pour la phrase ; [HY] pour son contenu | Idem |
| 7 | « Accord » : aucune occurrence dans le dépôt hors R1M | [FV négatif] | Recherche du 9 nov. |
| 8 | Périmètre, durée, HT ou TTC, signature, entité destinataire de l'offre | [IN] | — |

**Les deux lectures du prix** [ES, calculé ici] :

| Lecture | Par mois | Par trimestre | Par an | Par an, si le prix est HT (TVA 20 %) | Par an, si le prix est TTC |
| --- | --- | --- | --- | --- | --- |
| (a) 6 000 € par mois, facturés par trimestre | 6 000 € | 18 000 € | **72 000 €** | 86 400 € TTC | 60 000 € HT |
| (b) 6 000 € par trimestre | 2 000 € | 6 000 € | **24 000 €** | 28 800 € TTC | 20 000 € HT |

**Repères internes pour lire ces montants** :

| Repère | Valeur | Code | Source | Lecture (a) | Lecture (b) |
| --- | --- | --- | --- | --- | --- |
| Chef de projet cadre salarié en région, coût employeur | 5 380 à 6 149 € par mois | [MM] | STRAT:376 | ≈ un poste de cadre à plein temps (64 560 à 73 788 € par an) [ES, calculé ici] | — |
| Assistant non cadre, coût employeur | 2 249 à 2 808 € par mois | [MM] | STRAT:326 | — | Sous le coût d'un assistant (26 988 à 33 696 € par an) [ES, calculé ici] |
| JP de Marwin entre le plancher (750 €) et l'avenant (900 €) | 750 à 900 € | [PR] | STRAT:396, 203 | 80 à 96 JP par an ; 6,7 à 8 JP par mois [ES, calculé ici] | 27 à 32 JP par an ; 2,2 à 2,7 JP par mois [ES, calculé ici] |
| Socle B1 | 4 500 € HT par mois | [PR] | STRAT:199 | B1 vaut 54 000 € par an : du pilotage, pas un logiciel | — |
| Exploitation D (minimum) | 1 000 à 1 500 € HT par mois, plus un variable | [PR] | STRAT:347 | 12 000 à 18 000 € par an, hors licences du client | Idem |

**Trois sens possibles de « logiciel de gestion de propriété »** [HY] :

| Sens | Ce que le dépôt en dit | Code | Source |
| --- | --- | --- | --- |
| (1) Gestion immobilière des bâtiments : baux, loyers, charges, travaux, entretien, assurances, obligations | Bâtiments évoqués, jamais listés. Travaux envisagés « du bar et du restaurant ». Baux, actes et licences demandés pour C4 et au cadrage | [DR] / [IN] | C9:24, 30 (dossier du 21 oct., p. 23 et 32) ; CAT:269 ; PROP9:151 |
| (2) Logiciel hôtelier (PMS) si l'hébergement reprend | Un « ancien bar restaurant hôtel avec cour » pour la galerie ; le Vieux Relais « hôtel-restaurant » selon une seule pièce. Aucune reprise d'hébergement annoncée | [DR] ; [FV négatif] pour la reprise | `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:14` ; `crm/PASSATION.md:41` |
| (3) Pilotage de l'exploitation de plusieurs lieux (galerie, cabaret, commerces) | Missions 1, 3 et 5 du 18 oct. ; volet « Piloter » de l'offre du 2 nov. ; 47 aides de la présentation | [PR] | `sources/propositions-de-collaboration.pdf` p. 1 ; `interne/offre-marwin-tech-remuneration-et-collaboration.md:52` ; PIA |

---

## 3. Bâtiments et lieux : ce que disent les pièces

Règle de l'audit : « ne pas additionner ces mentions. Avant l'inventaire validé, il y a « des bâtiments », pas une liste » (MAJ:161).

| Lieu ou mention | Ce que dit la pièce | Code | Source | Contradiction ou inconnue |
| --- | --- | --- | --- | --- |
| Galerie | « un ancien bar restaurant hôtel avec cour pour en faire une galerie », racheté selon Morgan | [DR] | `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:14` | Adresse, acte, propriétaire [IN] (C9:21) |
| Galerie en 2027 | « a déjà racheté six bâtiments et ouvrira une galerie en 2027 » | [DR] | `interne/offres-de-carlone-catalogue-crm.md:9` | Bâtiments non listés (C9:22) |
| Six bâtiments et l'ancienne affaire de Medhi | « a racheté six bâtiments et l'ancienne affaire de Medhi » | [DR] | `interne/contexte-projet-carlone.md:24` | Lien de Morgan avec BOJ.ART à déclarer si elle en fait partie (MAJ:159) |
| Le Vieux Relais et le M | « Un associé rachète deux établissements à Cosne-Cours-sur-Loire : Le Vieux Relais (hôtel-restaurant) et le M (bar) » | [DR] | `crm/PASSATION.md:41` | Le dossier du 21 oct. inverse les fonctions (le M restaurant, le Vieux Relais bar) (C9:25-26 ; `audit/2026-11-04-audit-strategique/annexes/travaux/ex-C6-catalogue.md:149`) ; « associé » non nommé |
| Propriété du Vieux Relais et du M | « aucun document ne dit noir sur blanc qu'ils appartiennent à Carlone » | [FV] | `interne/contexte-projet-carlone.md:160` | — |
| Le M, cabaret | Il « souhaite racheter « le M » » : un souhait au 28 oct. | [DR] | `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:15` | Le cabaret du 9 nov. est « à côté de la galerie » ; rien ne dit qu'il est dans le M (MAJ:156) |
| Cabaret-spectacle et commerces | Prévus le 9 nov. | [DR] | MAJ:35 | Lieu, exploitant, jauge, licences [IN] (MAJ:51-52, U59, U60) |
| 1,5 M€ de bâtiments | Déclaré le 9 nov. | [DR] | MAJ:34 | « ne fait ni un budget pour Marwin, ni une entité qui signe » (MAJ:23) ; achat, entité et financement [IN] (MAJ:144-146, U56, U57) |
| Réouverture du bar et du restaurant | Flyers, cartes de fidélité, soirées de réouverture ; travaux électriques envisagés | [PR] / [HY] | C9:29-30 (dossier du 21 oct., p. 3, 18, 23, 29) | Aucune date, aucun budget |
| Propriétaire et exploitant | Probablement distincts | [HY] | MAJ:148 ; CARTO:133 (scénario B) | Un bon de commande par prestation et par entité (STRAT:185) |

**Hébergement et sécurité** :
- Seuil de 5e catégorie pour un hôtel (type O) : 100 personnes ; cabaret (L) : 50 ; restaurant ou bar (N) : 200 ; galerie (M ou T) : 200 [FV] (R5:325-331).
- Un ERP avec locaux d'hébergement demande une visite de réception et un arrêté d'ouverture, même en 5e catégorie [FV] (R5:332).
- Travaux d'un ERP : autorisation, 4 mois d'instruction ; permis de construire, 5 mois [FV] (R5:333 ; MAJ:167).
- Taxe de séjour, déclaration des voyageurs, classement hôtelier, données de paiement : **aucune occurrence dans le dépôt** [FV négatif] ; non étudiés [IN].
- « Séjours des invités » : vente de voyages réglementée (code du tourisme, L211-1) ; Marwin prépare, l'entité réserve et paie [FV texte ; PR rôle] (R3T:355 ; GOUV:117).

---

## 4. Ce qui a déjà été proposé ou montré sur la gestion des lieux

| Date | Pièce | Ce qu'elle propose | Code | Source |
| --- | --- | --- | --- | --- |
| 18 oct. | Huit propositions de collaboration | (1) « Suivi centralisé de vos établissements » : encaissements, dépenses, trésorerie, factures, points d'attention. (3) « Gestion administrative déléguée » : factures, contrats, assurances, abonnements, échéances, rappels automatisés. (5) « Mise en place des outils après chaque rachat » : accès, site, cartes, horaires, réservations, « suivi administratif commun » | [PR] | `sources/propositions-de-collaboration.pdf` p. 1 |
| 2 nov. | Offre de six mois (retirée) | Volet « Piloter » : suivi centralisé des établissements ; « Cadrer » : « diagnostic des outils après chaque rachat » | [PR], retiré (STRAT:407) | `interne/offre-marwin-tech-remuneration-et-collaboration.md:50, 52` |
| 4 nov. | Audit | Ces actes touchent des activités réservées ; Marwin prépare, le client ou son professionnel exécute | [PR] | GOUV:111-125 |
| 9 nov. | Présentation (PIA) | Domaine « Logiciels : outils à votre nom, reliés entre eux » (`domaines:17`). Ordre : outils du marché, liaisons légères, sur mesure après essai ; exemple : « suivi des travaux d'un lieu » (`logiciels:9-12`) | [PR] | PIA |
| 9 nov. | Présentation (PIA), aides proches de la gestion des lieux | Bâtiments : suivi de chantier, devis, carnet d'entretien (automatique), contrôles obligatoires (automatique), dossiers d'autorisation, énergie et capteurs (automatique), aides (`cat-batiments:8-14`). Finance : budgets par commerce (automatique), « Baux, assurances, abonnements et échéances suivis » (automatique) (`cat-finance:9, 11`). Administration : relances et échéances, tableau de bord par lieu (automatiques) (`cat-admin:11-12`). Cabaret et commerces : réservations, plannings, stocks, caisse (assistés) (`cat-cabaret:8, 10-12`) | [PR] | PIA |
| 9 nov. | Présentation (PIA), cibles futures de Marwin | « Hôtels, restaurants et commerces » ; « Propriétaires et gestionnaires de bâtiments » ; « Ce qui est développé pour vous vous est cédé » | [PR] | PIA `pour-dautres:12-13, 30` |
| 9 nov. | Proposition de cadrage | Exemple de tâche à essayer : « rappels automatiques avant les échéances des contrats et des assurances d'un lieu », quatre semaines sur un seul lieu | [PR] | PROP9:61 |
| 9 nov. | Proposition de cadrage | Exclusions : exécution administrative courante ; exploitation des lieux ; « Gestion immobilière : ni achat, ni location, ni gestion de biens pour vous ; nous préparons des comparaisons » | [PR] | PROP9:139-141 |

**Comptage des aides de la présentation** [MM, refait sur la copie lue le 9 nov. au soir] : 47 aides ; 7 automatiques (cat-admin 2, cat-batiments 3, cat-finance 2), 30 assistées, 10 préparées. La note du 9 nov. comptait 13, 24 et 10 (MAJ:248). Le fichier `deck.json` est identique à celui noté dans PROP9:260 ; l'empreinte des 26 vues réunies ne l'est plus (relevé : `acc15928d5cf…`, contre `d8875e29fc38…`) [MM]. La présentation a donc été corrigée après la note : les citations de lignes de MAJ section 7 peuvent ne plus correspondre.

---

## 5. Règles de l'audit qui touchent un logiciel de gestion

### 5.1 Ce que Marwin ne fait pas

| Activité | Règle | Code | Source |
| --- | --- | --- | --- |
| Gestion immobilière | Exclue ; « coordination d'un administrateur de biens ; pas de baux ni de loyers » | [PR], fondé sur un texte [FV] | STRAT:650 ; SYND:418 ; loi n° 70-9, art. 1 (R3T:354) |
| Exécution administrative, comptabilité, paie | Exclues ; l'exécution peut passer à une personne du client (C6) | [PR] | STRAT:187, 650 ; GOUV:112-113 |
| Recouvrement des impayés | Modèles de relance seulement ; l'entité signe et encaisse | [PR] | GOUV:119 ; SYND:420 |
| Maniement de fonds | « À éviter par construction » | [IN] pour le texte ; [PR] pour la règle | SYND:421 |
| Exploitation des lieux, licences, sécurité du public | Exclues ; dossiers seulement (C3, C4, C7) | [PR] | STRAT:647 ; MAJ:179, 191 |
| Contrats, baux, travaux, emprunts | Réservés à GianLuca ou au signataire ; jamais délégués | [PR] | STRAT:580, 591 ; GOUV:116 |
| Astreinte 24 h sur 24 | Exclue ; forfait séparé sur demande | [PR] | STRAT:651 |
| Agents qui agissent sans approbation | Exclus | [PR] | STRAT:652 ; GOUV:125 |
| Demande de 20 à 40 JP par mois | Refusée sous cette forme | [PR] | STRAT:702 |

### 5.2 Principes qui s'appliquent à tout outil

| Principe | Contenu | Code | Source |
| --- | --- | --- | --- |
| Comptes au nom du client | « dès le premier jour » ; Marwin y intervient comme collaborateur | [PR] | STRAT:189 ; GOUV:122 |
| Pas d'avance | Achats et abonnements commandés et payés par l'entité, sans marge | [PR] | STRAT:188, 387 |
| Engagement récurrent | Plus de 50 € par mois ou plus de 3 mois : accord écrit préalable | [PR] | STRAT:591 |
| Prix au livrable | Le temps mesure, il ne se vend pas ; aucun taux journalier montré au client | [PR] | STRAT:133, 186 |
| Droits | Développements propres cédés au paiement complet ; composants génériques de Marwin sous licence gratuite, non exclusive, perpétuelle | [PR] | STRAT:287 ; SYND:497-498 |
| Données du client | Toujours restituables ; jamais réutilisées pour la prospection de Marwin ; un kit vendu à d'autres n'utilise que des composants génériques | [PR] | STRAT:619 ; PRO7:657 |
| Hébergement par Marwin | S'il a lieu, le Data Act impose préavis de 2 mois au plus, transition de 30 jours au plus, 30 jours pour récupérer les données, « même pour un service sur mesure », et aucuns frais de changement à partir du 12 janv. 2027 | [FV] | SYND:507-510 ; CAT:378 |
| Un outil livré n'est pas refacturé | Maintenance facturée seulement dans une exploitation D ; défauts corrigés gratuitement 60 jours | [PR] | STRAT:384 |
| Gains d'automatisation | Prix fixé sur une référence mesurée avant ; gains à Marwin la première année, un tiers au client ensuite | [PR] | STRAT:418-420 |
| Rien d'exploratoire | Pas sans financeur écrit, budget plafonné et critère d'arrêt | [PR] | STRAT:190 |

### 5.3 Ce que l'audit dit du sur-mesure

- **Cinq options**, de l'actuel au développement spécifique ; l'organisation simple est un préalable aux options 3 à 5 [PR] (PRO7:79-85).
- **Option 5 (spécifique)** : 10 à 50 JP et plus ; qualité et fiabilité non démontrées ; maintenance lourde ; « risque fort » d'adoption [ES] (PRO7:320).
- **Repère** : recherche documentaire spécifique ≈ 31 à 66 k€ sur douze mois ; repère de marché 10 à 50 k€ [ES / DR] (PRO7:328).
- **Rapprochement budgétaire** : une intégration ne vaut qu'au-delà d'environ 50 pièces par mois [HY] (PRO7:347).
- **Le développement** se vend au livrable ; repère régional de 405 à 585 € par jour [ES] (STRAT:399).
- **Le coût réel est le temps humain**, pas l'abonnement : le registre des décisions coûte ≈ 4 000 à 10 500 € sur douze mois, outils compris [ES] (PRO7:23, 380).
- **Les prix des fournisseurs bougent vite** : devis d'outil daté, revu tous les trois mois ; deux fournisseurs ; plafond de consommation [PR] (PRO7:401-404).

---

## 6. Offres du catalogue concernées

**Règle de prix des lots** [PR] : JP estimées × 800 € HT + provision de 10 à 15 %, au forfait ; plancher : 750 € × borne haute des JP estimées (STRAT:287 ; CAT:67, 71). Paiement 40 / 60, ou 40 / 30 / 30 au-delà de 8 JP (CAT:193). Livraison déclenche le solde ; adoption décide de la suite (CAT:194).

| Offre | Résultat | JP [ES] | Prix HT [PR] | Plancher | Lien avec un logiciel de gestion | Source |
| --- | --- | --- | --- | --- | --- | --- |
| A, cadrage | Inventaire des entités, lieux, projets, accès ; trois priorités ; carte des rôles ; grille de délégation ; registre ; au plus trois tâches à essayer | 8,5 | 6 500 € | 6 000 € | Seul point d'entrée. Il **ne produit pas d'outils** (STRAT:227) | STRAT:225-231 ; MAJ:323-325 |
| C1 | Catalogue privé des œuvres | 4 à 7 | 3 500 à 6 400 € | 3 000 à 5 250 € | Module « œuvres » d'un outil multi-lieux | STRAT:291 ; CAT:212 |
| C3 | Faisabilité d'un événement sans robot | 4 à 6 | 3 500 à 5 500 € | 3 000 à 4 500 € | Indirect | STRAT:293 |
| **C4** | **Par lieu : propriétaire, exploitant, licences, classement ERP, calendrier des démarches**, à valider par les professionnels | 3 à 5 | 2 700 à 4 600 € | 2 250 à 3 750 € | **Fondation des données** d'un outil de gestion : la fiche de chaque lieu et ses échéances | STRAT:294 ; CAT:260-277 |
| C5 | Échange de fichiers avec Quali Contact | 3 à 4 | 2 700 à 3 700 € | 2 250 à 3 000 € | Modèle pour tout connecteur : rien avant le format réel | STRAT:295 ; CAT:279-296 |
| **C6** | **Outillage et passation** : registre, tableau de bord, 5 à 8 procédures avec fiche de secours, comptes au nom de l'entité, deux formations, restauration testée | 8 à 9 | 7 500 € | 6 750 € | **Passation des outils à l'administratrice** ; contenu à adapter (D50). Exclut « tout développement spécifique » et le nom « Jarvis » | STRAT:321-337 ; CAT:298-316 ; MAJ:84-89 |
| **C7** | **Rentabilité d'un rachat ou de travaux** : budget, seuil, trois scénarios, calculs par formule | 3 à 5 | 2 700 à 4 600 € | 2 250 à 3 750 € | Module « travaux et investissements » ; une opération par lot ; jamais dans le socle | STRAT:297 ; CAT:320-337 |
| C8 | Kit de campagne | 3 à 5 | 2 700 à 4 600 € | 2 250 à 3 750 € | Aucun | STRAT:298 |
| B0, B1, B2 | Socle de pilotage | 3 à 9 par mois | 3 500 ; 4 500 ; 6 900 € par mois | 3 000 ; 4 125 ; 6 750 € | Suivi budgétaire préparatoire et veille des échéances compris ; B1 au plus tôt au mois 4 | STRAT:198-200, 262-263 ; CAT:64-66 |
| D | Exploitation d'un processus prouvé | 1 à 4 par mois | 1 000 à 1 500 € par mois + variable | Jamais sous le coût manuel mesuré | Seule forme d'un **service logiciel récurrent** ; au plus tôt au mois 7 ; maintenance ≤ 0,5 JP par mois et par processus | STRAT:339-349 ; CAT:358-380 |
| E | Avenant, urgences | Résiduelle | 900 € par JP ; 450 € la demi-journée | — | Un livrable de plus de 2 JP se devise en lot | CAT:390-403 |

**Exemples de prix d'un module devisé en lot** [ES, calculé ici, règle de STRAT:287] :

| JP estimées | Formule (× 800 €, + 10 à 15 %) | Plancher (750 € × borne haute) |
| --- | --- | --- |
| 3 à 5 | 2 640 à 4 600 € HT | 3 750 € HT |
| 5 à 8 | 4 400 à 7 360 € HT | 6 000 € HT |
| 10 à 20 (spécifique, bas de fourchette) | 8 800 à 18 400 € HT | 15 000 € HT |
| 50 (spécifique, haut de fourchette) | 44 000 à 46 000 € HT | 37 500 € HT |

Le plancher porte sur la borne haute de l'estimation retenue pour le lot. Une estimation de 3 à 4 JP donne donc 3 000 € ; c'est pourquoi CAT donne pour C4 un plancher de 2 250 à 3 750 € (CAT:272).

---

## 7. Capacité réelle des deux associés

| Fait | Valeur | Code | Source |
| --- | --- | --- | --- |
| Capacité facturable réaliste (prudent, central, haut) | ≈ 6, 10, 18 JP par mois | [ES] | CAP:17, 174 |
| Plafond engagé la première année | 10 JP facturables par mois, « quelle que soit la demande » | [PR] | STRAT:43, 485 |
| En central, plafond et capacité se confondent | « le plafond de 10 JP n'est donc pas une marge de sécurité : c'est la capacité elle-même » | [ES] | CAP:17 ; MAJ:68 |
| Production pure sur 10 JP | ≈ 3,2 JP | [ES] | CAP:19, 215 |
| Par personne, central | Morgan ≈ 6,0 JP ; Mathys ≈ 4,3 JP | [ES] | CAP:200 |
| Moyenne annuelle vendable | ≈ 9,4 JP par mois ; ≈ 6,2 JP en août | [ES] | CAP:258, 262 |
| Projets simultanés, central | Un socle, deux projets actifs, un en veille, **un seul lot à la fois** (≈ 4 JP par mois), aucun exploratoire | [ES/PR] | CAP:21, 328, 335 |
| Deux lots en parallèle | ≈ 15 JP avec le socle : « impossible sous 10 » | [ES] | CAP:331 |
| Occupation | Alerte à 85 % sur **tout** le temps de chacun ; refus de tout projet au-delà de 95 % deux mois | [PR] | STRAT:623 |
| Autres activités à plafonner | ≈ 5 JP par mois pour Morgan ; ≈ 7,5 pour Mathys | [PR] | CAP:183 |
| Ce qui est démontré | La production, pas la livraison ; « déployer sur un vrai poste ; faire adopter un outil » : non démontré | [FV] | CAP:16, 58 |
| Compétences de Mathys en développement, sécurité, hébergement ; sa disponibilité | Inconnues | [IN] | CAP:78, 80 |
| Maintenance dans la durée (offre D) | Non démontrée | [FV négatif] | CAP:98 |
| Points de défaillance unique | Morgan (relation, prix, validation) ; Mathys (code du CRM) | [FV/DR] | CAP:22 |

**Traductions** [ES, calculé ici] :
- Un développement spécifique de 10 à 50 JP occupe la place du lot unique pendant 2,5 à 12,5 mois, à ≈ 4 JP de lot par mois (CAP:328 ; PRO7:320).
- Un logiciel découpé en 5 processus outillés, à 0,5 JP de maintenance chacun, prend 2,5 JP par mois, soit un quart du plafond, avant tout travail nouveau (STRAT:349). La note du 9 nov. faisait ce calcul pour les 13 aides automatiques d'alors : 6,5 JP (MAJ:212). Avec les 7 aides automatiques de la copie actuelle : 3,5 JP.
- Remplacer la lecture (a) d'« Accord » par du temps de Marwin prendrait 6,7 à 8 JP par mois sur ≈ 10 (section 2).

---

## 8. Conditions de la stratégie retenue

| Condition | Contenu | Code | Source |
| --- | --- | --- | --- |
| Cadrage d'abord | Une seule proposition : le cadrage à 6 500 € HT, moitié à la commande ; un pilote de huit semaines ensuite, dans une seule voie | [PR] | STRAT:42, 243-251 |
| Entité nommée | Dénomination, SIREN, signataire, effectif ; solvabilité vérifiée ; bon de commande | [PR] | STRAT:665 ; REG:297 (D24, 15 déc.) |
| Dates de report | Pas d'entité au 15 déc. 2026 : report sans production ; cadrage non payé au 31 janv. 2027 : report sans date | [PR] | STRAT:44, 697-698 |
| Dix conditions avant tout travail payé | Fuite traitée, documents cohérents, accord de Mathys, SAS immatriculée, apport, entité, contrat relu, acompte, accès, aucune donnée réelle avant les préalables | [PR] | STRAT:658-669 |
| Rien ne part au client | Avant D03 (CNIL), D08 (information des personnes) et l'accord écrit des deux associés | [PR] | MAJ:20, 370 |
| D52 | « Aucune production pour un bâtiment, un commerce ou le cabaret sans mandat ni commanditaire nommé, études et visuels compris » ; immédiate | [PR] | MAJ:374 |
| D45 | Ne pas envoyer ni montrer la présentation | [PR] | MAJ:375 |
| D47 | Réponse écrite à « tout gérer avec l'IA » : non ; une voie, deux projets actifs, un processus en essai à la fois ; rien d'automatique vers l'extérieur | [PR] | MAJ:380 |
| Mandat de dépense | 0 € pendant le cadrage et le pilote | [PR] | STRAT:589 |
| Calendrier des offres | Lots après le cadrage ; socle au plus tôt au mois 4 ; exploitation D au plus tôt au mois 7 (juillet 2027 en central) | [PR] | CAT:62-68 ; PRO7:708 |
| Démonstrateurs internes | Registre (P1) et recherche documentaire (P3), plafonnés à 8 JP avant le 2 févr. 2027, sur données fictives ou corpus filtré | [PR] | PRO7:689 |

---

## 9. Le CRM déjà construit : quelles briques réutiliser

### 9.1 Ce qui existe

| Brique | Constat | Code | Source |
| --- | --- | --- | --- |
| Interface | Un seul fichier `crm/site/index.html` de 3 032 lignes (≈ 272 Ko), une seule balise `<script>`, sans bibliothèque JavaScript externe ; seules les polices Google sont chargées | [FV] | `crm/site/index.html:3-5, 1016` |
| Données | Fichiers JSON chargés à l'ouverture (`companies.json` ≈ 2,7 Mo, `culture.json`) | [FV] | `crm/site/index.html:2989` ; `crm/README.md:8` |
| Persistance sur claude.ai | `window.claude.use("db")`, `("user")`, `("downloads")` | [FV] | `crm/site/index.html:2524, 3013` |
| Version autonome | Firebase : connexion Google seule, Firestore, hébergement ; SDK 10.14.1 copié ; région conseillée europe-west9 (Paris) | [FV] | `crm/autonome/LISEZMOI.md:3-12, 31, 77` |
| Raccord | `crm-firebase.js` (248 lignes) donne au CRM la même interface que claude.ai ; écritures par transaction, fusion des champs | [FV] | `crm/autonome/source/crm-firebase.js:1-6, 56-63` |
| Droits | Règles Firestore : associés listés lisent ; seul le propriétaire charge le code et les données ; suivi partagé | [FV] | `crm/autonome/firestore.rules:10-41` |
| Scripts de données | Python 3, bibliothèque standard seulement, lancés avec `python3 -I` ; chaîne `merge.py` → `ext_merge.py` (861 lignes) → `art_merge.py` | [FV] | `crm/README.md:9-21` ; `crm/merge.py:1` ; `crm/ext_merge.py:4` ; `crm/art_merge.py:11` |
| Garde-fous de contenu | Expression « INTERDIT » qui bloque certaines mentions dans les textes | [FV] | `crm/PASSATION.md:49` |
| Fonctions réutilisables | Export CSV ; export d'agenda `.ics` ; import du rapport d'appels sans doublon, avec conflits signalés | [FV] | `crm/site/index.html:1555, 2550` ; `crm/PASSATION.md:83` |
| Autres modèles du dépôt | Modèle financier de l'audit : Python standard, vérifie sommes, signes et TVA, reproductible octet pour octet [MM] ; `tools/restaurer-archives.py` : restitution avec contrôle d'empreinte | [FV] | AUD:120-129 ; `tools/restaurer-archives.py:6-27` |

### 9.2 Ce qui empêche une réutilisation telle quelle

| Défaut | Code | Source |
| --- | --- | --- |
| Code du CRM chargé depuis la base puis exécuté par `document.write` ; aucun en-tête de sécurité du contenu | [FV] | C5:56 ; `crm/autonome/source/crm-firebase.js:142` ; `crm/autonome/firebase.json:5-7` |
| Tout associé peut modifier et supprimer tout le suivi, sans historique côté serveur | [FV] | C5:55 ; `crm/autonome/firestore.rules:32-37` |
| Sauvegarde par export CSV manuel ; aucune restauration testée | [DR] | C5:57 ; PRO7:634 |
| Tests annoncés (30 parcours, émulateurs) mais aucun fichier de test dans `crm/` | [FV négatif] | C5:58 |
| Purge des prospects à 3 ans affichée, jamais programmée | [HY] | C5:67 |
| Version autonome non configurée (« A_REMPLACER », adresses d'exemple) | [FV] | C5:53 |
| Hébergé « chez les associés, dans leur dépôt GitHub et leur projet Firebase » : contraire aux comptes au nom du client | [DR] ; [FV] pour l'écart | `crm/docs/rapport/rapport-crm-hermes360.md:19` ; PRO7:663 |
| Dépôt source public au 4 nov., avec ≈ 931 numéros et 206 e-mails | [DR] | `interne/contexte-projet-carlone.md:11` ; AUD:93 |
| Propriété du code non réglée entre associés (D12) ; CRM jamais facturé, ni rétroactivement ni dans un lot | [IN] ; [PR] | REG:280 ; SYND:494 ; STRAT:385 |
| Simulateur fiscal faux (taux d'IS fixe de 25 %) | [FV] | `crm/art_merge.py:19, 129` ; PRO7:69 |
| Code produit en grande partie par des agents : 48 commits sur 56 signés « Claude » | [FV] | CAP:50 |

**Lecture** [HY] : on peut reprendre des **modèles** (fichier unique sans dépendance, scripts Python standard, raccord qui rend le même code portable entre deux hébergements, exports ouverts, import sans doublon). On ne reprend ni les données, ni l'hébergement, ni le code sans corriger les défauts ci-dessus et régler D12.

---

## 10. Jarvis (copilote)

| Fait | Code | Source |
| --- | --- | --- |
| Jarvis M07 n'est ni installé ni qualifié sur la tour | [FV] | C7J:37 |
| Dépôt BOJART public, sans licence ; droits réservés par défaut | [FV] ; [HY] | C7J:64-65 ; SYND:496 |
| L'offre écrite attribue Jarvis au pôle de Medhi | [PR] | C7J:70 |
| « Copilote Jarvis » suspendu comme produit et comme nom | [PR] | STRAT:648 ; PRO7:677 |
| C6 exclut le nom « Jarvis » | [PR] | STRAT:329 |
| Mémoire documentaire : la bonne source n'atteint le modèle que dans 71,4 % des cas à 8 000 octets | [MM] | PRO7:40 |
| Brique de mémoire réutilisable seulement après règlement écrit des droits | [PR] | PRO7:391 |

---

## 11. Quali Contact

| Fait | Code | Source |
| --- | --- | --- |
| GianLuca « prévoit d'engager » Quali Contact | [DR] | `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:7, 13` |
| SAS, SIREN 394 573 497, 50 à 99 salariés, siège à Clichy, établissement à Cosne-Cours-sur-Loire (10 à 19 salariés) | [FV] | R6:220-234 |
| Activité affichée : collecte de dons pour le secteur caritatif | [FV] pour l'affichage | R6:237 ; STRAT:118 |
| Logiciel utilisé « pas formellement identifié (peut-être Vocalcom Hermes360) » | [IN] | `crm/PASSATION.md:46` |
| Un module Hermes360 a été construit sur cette hypothèse non vérifiée | [FV] | CAT:284 ; `crm/PASSATION.md:83` |
| Consignes aux opératrices via leur employeur ; C5 seulement si Quali Contact est engagé | [PR] | STRAT:584, 300 |
| Lien avec la gestion des lieux | Aucun [FV négatif] | — |

**Leçon pour un logiciel de gestion** [PR] : ne construire aucun connecteur (comptabilité, caisse, logiciel hôtelier, banque) avant d'avoir le logiciel, la version et un modèle de fichier réel (C5 : CAT:287).

---

## 12. Exigences de sécurité de PRO7 qui s'appliquent

| Exigence | Règle | Source |
| --- | --- | --- |
| Classes d'actions | Autonome : lire, chercher, résumer, proposer. Approbation humaine : envoyer, appeler, modifier, publier, engager une dépense. Interdit : payer, supprimer en masse, changer des droits | PRO7:67 |
| Approbation | Hors de portée de l'agent, qui montre l'action exacte ; un compte et un jeton par agent et par client, lecture seule par défaut, durée courte | PRO7:557 |
| Documents = données | Toute instruction trouvée dans un document est signalée, jamais exécutée | PRO7:68, 556 |
| Calculs | Montants, sommes et dates par formule, jamais par le modèle de langage | PRO7:69 |
| Banque | « jamais d'identifiants bancaires confiés à un agent » | PRO7:169 |
| Coûts | Plafonds par tâche, jour et mois ; alertes à 50, 80, 100 % ; coupure à 100 % | PRO7:558, 564-568 |
| Erreurs en masse | Aucune mise à jour en masse sans échantillon validé ; modifications par lots, avec annulation | PRO7:559 |
| Secrets | Coffre ; jamais dans un prompt, un journal ou un dépôt ; révocation testée | PRO7:560 |
| Journal | Inaltérable par l'agent : demande, autorisation, action, résultat, auteur humain | PRO7:561 |
| Composants | Inventaire des agents, connecteurs, serveurs MCP et versions | PRO7:562 |
| Données réelles | Seulement après les dix points de la liste de contrôle (responsable du traitement, contrat de l'article 28, registre, offres professionnelles, analyse des transferts, pseudonymisation…) | PRO7:605-616 |
| Fournisseurs | Anthropic et OpenAI absents du Data Privacy Framework au 4 nov. 2026 [MM] ; offres grand public exclues | PRO7:595-603 |
| Sauvegardes | Export quotidien ; trois copies, deux supports, une hors du fournisseur ; perte maximale 24 h ; reprise en un jour ouvré ; restauration testée chaque mois puis chaque trimestre | PRO7:625-628, 636 |
| Arrêt et secours | Bouton d'arrêt testé chaque trimestre ; fiche de secours manuel par processus | PRO7:630-631, 638 |
| Passages d'étape | Démonstrateur → pilote → exploitation, avec preuves écrites ; un test sur données fictives ou une démonstration ne prouvent rien | PRO7:539-544 |
| Rôle au sens de l'AI Act | Fournisseur si Marwin livre un assistant à son nom : informer l'utilisateur, marquer les contenus | PRO7:572-573 |

---

## 13. Ce qui reste incertain

| Inconnue | Qui peut répondre | Référence |
| --- | --- | --- |
| Identité d'« Accord », contenu de l'offre, durée, HT ou TTC, signée ou non | GianLuca, par un devis écrit | Nouvelle ; R1M:30-33 |
| Sens de « gestion de propriété » : immobilier, hôtellerie, exploitation | GianLuca | Nouvelle |
| Bâtiments : lesquels, adresses, usages ; entité propriétaire | GianLuca ; son notaire | U56, U57 (MAJ:48-49) |
| Lien entre six bâtiments, bar-restaurant-hôtel, le M, le Vieux Relais | GianLuca | U58 (MAJ:50) |
| Commerces et cabaret : lieux, exploitants, calendrier | GianLuca | U59, U60 (MAJ:51-52) |
| Outils déjà utilisés par l'administratrice ; ses pouvoirs | Elle ; GianLuca | U54, U55 (MAJ:46-47) |
| Reprise d'une activité d'hébergement ; nombre de chambres | GianLuca | Nouvelle |
| Volumes : baux, locataires, lieux, pièces par mois, prestataires | GianLuca ; administratrice | PRO7:717 |
| Compétences et disponibilité de Mathys | Mathys | CAP:78, 80 |
| Propriété du code du CRM | Morgan et Mathys | D12 (REG:280) |
| Sort de la fuite (décision CNIL) | Morgan et Mathys | D03 (MAJ:12 ; AUD:18) |

---

## 14. Ce que cela implique pour une offre de logiciel de gestion des propriétés

1. **Obtenir l'offre écrite avant de comparer** [PR, R3]. Le sujet entre dans le cadrage comme une des trois priorités possibles : inventaire des lieux, outils déjà en place, devis d'« Accord » fourni par GianLuca. Aucune réponse chiffrée avant cela, et rien avant D03, D08 et l'accord des deux associés (MAJ:370). Aucun prototype pour un bâtiment avant un mandat (D52, MAJ:374).

2. **Comparer à périmètre égal, sans promettre « moins cher » en bloc** [HY]. Si l'offre couvre un service humain (gestion locative, encaissement, astreinte), Marwin ne peut pas le remplacer : gestion immobilière et astreinte sont exclues (STRAT:650-651), et la lecture (a) prendrait 6,7 à 8 JP par mois sur ≈ 10 (section 7). Si elle couvre un logiciel, des outils du marché sur les comptes de l'entité coûtent sans doute beaucoup moins [ES] (R1M:31). « Mieux » n'est pas démontré : Marwin n'a encore fait adopter aucun outil (CAP:16, 58).

3. **Architecture en modules, chacun vendu comme un lot borné, un à la fois** [PR, R3], selon la règle des lots (STRAT:287) :

   | Module | Sens | Offre qui le porte | Qui exécute au quotidien |
   | --- | --- | --- | --- |
   | M0. Fiche de chaque lieu : propriétaire, exploitant, licences, ERP, échéances | (1), (2), (3) | Cadrage, puis C4 | Administratrice |
   | M1. Échéances : contrôles, assurances, contrats, baux ; rappels | (1), (3) | Essai de rappels (PROP9:61), puis C6 | Administratrice |
   | M2. Travaux et entretien : devis comparés, suivi de chantier, carnet d'entretien | (1) | C7 pour une opération ; lot devisé pour l'outil | Administratrice ; maître d'œuvre |
   | M3. Gestion locative : baux, loyers, charges, quittances | (1) | Outil du marché au nom de l'entité, configuré dans un lot ; jamais exploité par Marwin | Administratrice ou administrateur de biens [HY, loi Hoguet à faire valider par l'avocat] |
   | M4. Logiciel hôtelier | (2) | Seulement si l'hébergement est décidé et l'exploitant nommé ; outil du marché | Exploitant |
   | M5. Exploitation des commerces et du cabaret : réservations, caisse, stocks, plannings | (3) | Outils du marché par exploitant ; lot de mise en place | Chaque exploitant |
   | M6. Tableau consolidé : budget, engagé, payé par lieu, par formule | (1), (3) | Socle (suivi préparatoire), puis D au plus tôt au mois 7 | Administratrice ; expert-comptable |

4. **Le sur-mesure vient en dernier** [PR]. L'audit ne voit aucun processus qui le justifie aujourd'hui (PRO7:21). Un développement de 10 à 50 JP bloque le lot unique 2,5 à 12,5 mois [ES, calculé ici]. Il ne se lance qu'après un essai où les outils du marché et une liaison légère échouent, avec cession au client au paiement et composants génériques séparés **avant** d'écrire le code (STRAT:287, 619 ; PIA `pour-dautres:30`).

5. **Pas d'abonnement logiciel de Marwin avant le mois 7** [PR]. Le seul service récurrent prévu est l'exploitation D : 1 000 à 1 500 € HT par mois plus un variable, après un pilote tenu, maintenance ≤ 0,5 JP par mois et par processus (STRAT:339-349). Les licences restent au nom et à la charge de l'entité (STRAT:188-189). Si Marwin hébergeait elle-même, le Data Act interdirait les frais de changement dès le 12 janv. 2027 (SYND:507-510).

6. **L'administratrice exécute, Marwin outille et passe la main** [PR]. C6 adapté (D50 ; MAJ:84-89) est la voie naturelle : registre, tableau de bord, procédures, comptes au nom de l'entité, formation, restauration testée. Marwin ne reprend pas l'exécution (STRAT:337) et ne reçoit pas d'ordres quotidiens d'elle (MAJ:117, D49).

7. **Une entité, un responsable du traitement et un bon de commande par module** [PR]. Propriétaire et exploitant sont sans doute distincts (MAJ:148). Locataires, clients d'hôtel et salariés sont des personnes : aucune donnée réelle avant la liste de contrôle (PRO7:605-616) ; jamais d'identifiants bancaires confiés à un agent (PRO7:169) ; relances de loyers signées et encaissées par l'entité (GOUV:119).

8. **Sécurité intégrée dès le devis** [PR]. Chaque module reprend la grille de PRO7 section 8 : approbation hors de portée de l'agent, journal inaltérable, calculs par formule, sauvegardes à trois copies, restauration et arrêt testés. Les 7 aides « automatiques » de la présentation (carnet d'entretien, contrôles, capteurs, baux, budgets) restent des rappels internes, pas des actions vers l'extérieur (D47, MAJ:380).

9. **Reprendre du CRM la méthode, pas l'objet** [HY]. Fichier unique sans dépendance, scripts Python standard, raccord portable, exports ouverts, import sans doublon : oui, comme modèles. Données de prospects, hébergement chez les associés, `document.write`, droits d'écriture trop larges et absence de tests : non (section 9.2). Rien ne se réutilise avant D12 (REG:280).

10. **Texte client sobre** [PR]. Ne jamais nommer « Accord » ni le critiquer. La proposition du 9 nov. promet déjà une comparaison « avec un autre prestataire » (PROP9:41) : c'est le bon cadre. Les deux associés valident par écrit avant tout envoi (STRAT:578 ; MAJ:370).

---

## Limites

- Les faits sur « Accord » et sur le « logiciel de gestion de propriété » sont des déclarations de Morgan [DR], absentes du dépôt.
- La présentation a été modifiée après la note du 9 nov. ; ce relevé cite la copie lue le 9 nov. au soir, dont l'empreinte diffère de celle de PROP9:260.
- Les points juridiques (loi Hoguet appliquée à un outil, rôles RGPD par module, obligations d'un hôtel) sont des hypothèses à soumettre à l'avocat.
- Les JP sont des estimations ; les prix sont ceux de la stratégie, non validés par les associés.
- Aucune recherche web n'a été faite pour ce relevé ; les prix du marché sont dans R1M.

---

## Note de mise en cohérence (9 nov. 2026, soir)

Ajoutée à la fin pour ne pas déplacer les numéros de ligne cités ailleurs (`R3:…`). Le corps de ce relevé n'est pas modifié.

- **Modules.** Les modules M0 à M6 de la section 14 sont une première découpe. Les livrables suivent les **neuf modules** de la spécification (`pour-carlone/logiciels-et-automatisations/2026-11-09-annexe-specification-logiciel-gestion-proprietes.md`, section 3) : M0 → modules 1 et 4 ; M1 → module 5 ; M2 → module 3 ; M3 → module 2 ; M4 → module 9 ; M5 → module 4 (totaux des outils du marché) ; M6 → modules 6 et 7.
- **Offres.** Le dossier ajoute les lots L0 à L5, hors catalogue, au prix de la règle des lots, et une maintenance de 700 à 1 000 € HT par mois après le pilote, sous le minimum de l'offre D (point 5 de la section 14) : écarts signalés en encadré dans l'étude (`interne/logiciels-et-automatisations/2026-11-09-etude-gestion-proprietes-offre-accord-et-prix.md`, sections 3.5, 3.6 et 8 ; décisions DL5 et DL6).
