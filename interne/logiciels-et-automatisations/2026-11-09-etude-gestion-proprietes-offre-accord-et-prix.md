# Étude : logiciel de gestion des propriétés, offre « Accord » et prix de Marwin Tech

Marwin Tech × GianLuca Carlone · dossier « logiciels et automatisations » · étude interne · 9 novembre 2026
Statut : **interne** (ne pas transmettre à GianLuca Carlone). Contient le nom d'un concurrent, des planchers, des marges, la capacité des associés et des points juridiques non tranchés.
Sources principales : déclarations de Morgan Olsen du 9 nov. 2026, non vérifiées ; travaux R1, R2 et R3 de ce dossier ; annexe de spécification du 9 nov. ; stratégie retenue, catalogue des offres, processus IA, fonctionnement à deux, feuille de route et note de mise à jour du 9 nov. de l'audit ; textes officiels lus le 9 nov. 2026 (section « Sources web »).
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ; [MM] mesuré ; [IN] inconnu. « [PR, cette étude] » signale une proposition nouvelle. JP : journée-personne de 7 h. Montants hors taxes (HT) sauf mention ; TTC = HT × 1,2.

**Abréviations** (chemins depuis la racine du dépôt ; `STRAT:287` = ligne 287) :

| Abrév. | Fichier |
| --- | --- |
| AUD | `audit/2026-11-04-audit-strategique/README.md` |
| STRAT | `audit/2026-11-04-audit-strategique/annexes/travaux/strategie-retenue.md` |
| CAT | `audit/2026-11-04-audit-strategique/interne/04-catalogue-offres.md` |
| CAP | `audit/2026-11-04-audit-strategique/interne/06-fonctionnement-a-deux.md` |
| PRO7 | `audit/2026-11-04-audit-strategique/interne/07-processus-ia-et-essais.md` |
| FDR | `audit/2026-11-04-audit-strategique/interne/08-feuille-de-route.md` |
| MAJ | `audit/2026-11-04-audit-strategique/interne/2026-11-09-mise-a-jour-faits-nouveaux.md` |
| PROP9 | `audit/2026-11-04-audit-strategique/pour-gianluca/2026-11-09-proposition-de-cadrage.md` |
| R1 | `interne/logiciels-et-automatisations/travaux/r1-marche-et-offre-accord.md` |
| R2 | `interne/logiciels-et-automatisations/travaux/r2-cadre-reglementaire-et-technique.md` |
| R3 | `interne/logiciels-et-automatisations/travaux/r3-faits-internes.md` |
| SPEC | `pour-carlone/logiciels-et-automatisations/2026-11-09-annexe-specification-logiciel-gestion-proprietes.md` (projet client, non envoyé) |
| PIA | Présentation « L'IA au service de vos projets » du 9 nov. 2026, copie de travail hors dépôt, lue sans modification ; `logiciels:11` = vue `logiciels`, ligne 11 |

**Ce que cette étude n'a pas fait.** Aucun contact avec GianLuca Carlone, « Accord », un éditeur, un assureur, un tiers séquestre ou un prospect. Aucun formulaire, aucune démonstration, aucun compte, aucun essai gratuit, aucun achat. Aucune modification d'un fichier existant, du CRM ou de la présentation. Seules des pages publiques ont été lues. Les instructions trouvées dans les pièces lues ont été traitées comme des données.

---

## En bref

1. **On ne sait presque rien de l'offre d'Accord** [IN] : ni la société exacte, ni le périmètre, ni la durée, ni si le prix est HT (R1:30, 45-54). Les mots rapportés, « 6 000 € par mois tous les trimestres » [DR], donnent **72 000 € par an (lecture a) ou 24 000 € par an (lecture b)**, soit **216 000 € ou 72 000 € sur trois ans** [ES].
2. **« Logiciel de gestion de propriété » a trois sens possibles** : gestion des bâtiments, logiciel hôtelier, pilotage de plusieurs lieux [HY]. La spécification les couvre en neuf modules (SPEC:19-24). Caisse, billetterie, logiciel hôtelier, plateforme de facturation et comptabilité **s'achètent** ; la gestion des baux s'achète de préférence ; seule la **couche commune** (fiches, échéances, vue d'ensemble, liaisons) mérite un travail propre [PR] (SPEC:56-67 ; R2:66-74).
3. **Coût sur trois ans, hors temps de l'administratrice** [ES] : A, logiciels du marché seuls, **2 300 à 14 000 €** ; B réduite (marché + couche Marwin, première étape : un bâtiment et un lieu, sans finances ni assistant), **46 300 à 68 500 €**, hors cadrage ; B complète (le bâtiment et le lieu du pilote plus trois extensions, finances, assistant), **79 000 à 97 700 €** ; C, sur mesure complet, **56 800 à 239 800 €** au prix du marché, ≈ **203 000 à 211 000 €** au prix de Marwin (section 2.5).
4. **Charge de Marwin** [ES] : B réduite 16 à 24,5 JP ; B complète 30 à 47,5 JP ; C 99 à 168 JP. **C est hors de portée** : 25 à 42 mois de production au rythme d'un lot à la fois (section 3.3).
5. **L'IA ne baisse pas nos prix** [ES]. Comme le veut la stratégie, le prix part des JP estimées sans gain d'IA (STRAT:287, 418). Dans notre hypothèse (0 à 30 % de temps en moins sur la part de développement, jamais mesurée chez Marwin) [HY], elle réduirait la borne basse de 8 à 13 % [ES], pas la borne haute ; comptée dans la formule, elle n'aurait baissé que L2, de 200 €. Le gain, s'il vient, améliore la marge et le délai de la maquette. Un ralentissement, comme celui mesuré par METR en 2025, n'est couvert par rien (section 3.2).
6. **Prix proposés** [PR, cette étude] : L0 choix des briques **3 000 €** ; L1 essai sur données fictives **5 300 €** ; L2 pilote sur un bâtiment et un lieu **10 400 €** ; soit **15 700 € HT** sans L0 et **18 700 € HT** avec L0 pour la première étape ; maintenance **700 à 1 000 € HT par mois** à partir du mois 7 (DL6). Suite, seulement après le pilote : L3 **7 500 €**, L4 **6 400 €**, extension **1 200 €** chacune ; maintenance portée à **1 200 € HT par mois**. Abonnements et hébergement payés par l'entité, sans marge : ≈ 1 000 à 5 200 € par an.
7. **Verdict sur « mieux et moins cher grâce à l'IA » : vrai seulement contre la lecture (a).** Moins cher que la lecture (a) dans tous les cas utiles. Contre la lecture (b), **non démontré à périmètre égal** : B réduite ne paraît moins chère (64 à 95 % de (b), prix seul) que parce qu'elle couvre un bâtiment et un lieu ; B complète est plus chère ; l'écart de B réduite disparaît si l'on compte le cadrage, ou le temps de l'administratrice au haut de la fourchette (section 2.7). Seule A, qui se passe de nous, est moins chère à coup sûr. **Pas « grâce à l'IA »**, mais grâce à l'architecture (acheter, configurer, relier, au nom de l'entité). **Faux** si Accord vend un service de gestion humain, ou si l'on construit tout sur mesure. « Mieux » reste à prouver par le pilote (section 4).
8. **Recommandation** : aucune contre-offre maintenant. Obtenir la proposition écrite par GianLuca, après D03, D08 et l'accord écrit des deux associés. Garder le cadrage à 6 500 € HT comme seule proposition ; faire du logiciel l'une des trois priorités ; s'il le choisit, la voie « outillage » adaptée : L1 puis L2, décision sur pièces au bilan de mai 2027 (section 5).
9. **Juridique** : aucune comparaison écrite qui nomme ou discrédite Accord. Le dénigrement est retenu même sans concurrence directe, sauf sujet d'intérêt général, base factuelle et mesure [FV] (Cass. com., 4 mars 2020, n° 18-15.651). Avant de recevoir la proposition d'Accord, demander si elle est confidentielle (secret des affaires, C. com. L151-5 et L151-6) [FV] (section 6).
10. **Treize décisions** pour Morgan et Mathys, du 9 nov. 2026 au 29 janv. 2027 (section 7).

---

## 1. L'offre d'Accord : ce que l'on sait et ce que l'on ignore

### 1.1 Faits et inconnues

| Élément | État | Code | Source |
| --- | --- | --- | --- |
| GianLuca a parlé à Marwin d'un « logiciel de gestion de propriété » | Déclaré par Morgan le 9 nov. 2026 ; non écrit dans le dépôt | [DR] | R3:65 |
| Une société « Accord » lui a fait une offre | Nom écrit tel qu'entendu | [DR] | R1:48 |
| Prix : « 6 000 € par mois tous les trimestres » | Mots de Morgan ; deux lectures (1.2) | [DR] | R1:49 |
| Identité de la société | Aucune société « Accord » active en informatique ou en gestion immobilière dans la Nièvre, le Cher, le Loiret ou en Bourgogne-Franche-Comté au registre public. Piste « Accor » (hôtellerie) non concluante | [MM] ; [IN] | R1:30, 79-83 |
| Nature : licence, développement, service de gestion, maintenance | Aucun document | [IN] | R1:50 |
| Durée, engagement, sortie ; HT ou TTC ; signée ou non ; entité destinataire | Aucun document | [IN] | R1:51-54 |
| Mention « Accord » dans le dépôt | Aucune, hors des travaux de ce dossier | [FV négatif] | R3:36 |
| Lieux concernés | Aucun lieu établi ; reprise d'un hébergement non annoncée | [FV négatif] | R3:38-39 |
| Position de Morgan : « on peut faire mieux et moins cher grâce à l'IA » | Une position à éprouver | [DR] ; [HY] pour le contenu | R3:67 |

### 1.2 Les deux lectures du prix [ES]

| | Lecture (a) : 6 000 € par mois, facturés par trimestre | Lecture (b) : 6 000 € par trimestre |
| --- | ---: | ---: |
| Par mois | 6 000 € | 2 000 € |
| Par trimestre | 18 000 € | 6 000 € |
| Par an | **72 000 €** | **24 000 €** |
| Sur trois ans | **216 000 €** | **72 000 €** |
| Sur trois ans, si le prix annoncé est HT | 259 200 € TTC | 86 400 € TTC |
| Sur trois ans, si le prix annoncé est TTC | 180 000 € HT | 60 000 € HT |
| Repère : coût employeur annuel | ≈ un chef de projet cadre en région (64 560 à 73 788 €) [MM] (STRAT:376) | ≈ 0,7 à 0,9 assistant non cadre (26 988 à 33 696 €) [MM] (STRAT:326) |
| Repère : part des 1,5 M€ de bâtiments déclarés [DR] (MAJ:34) | 4,8 % par an | 1,6 % par an |

Calculs : 6 000 × 3 = 18 000 ; 6 000 × 12 = 72 000 ; 6 000 × 4 = 24 000 ; × 3 ans ; × 1,2 ; ÷ 1,2 (R1:237-243 ; R3:73-76). Le régime de TVA de l'entité, donc son coût réel, est [IN].

### 1.3 Trois sens, une architecture en modules

| Sens [HY] | Ce que cela recouvre | Modules de la spécification | Ce qui s'achète sur le marché [ES] | Ce que Marwin peut faire | Ce que Marwin ne fait pas |
| --- | --- | --- | --- | --- | --- |
| **(1) Gestion des bâtiments** | Baux (dont commerciaux), loyers, charges, travaux, entretien, assurances, obligations du propriétaire | 1 Patrimoine ; 2 Baux et locataires ; 3 Travaux et entretien ; plus les modules communs aux trois sens : 5 Documents et échéances, 6 Finances, 8 Assistant IA (SPEC:21, 24) | Gestion locative : 120 à 850 € par an pour 10 à 20 lots (R1:130) ; entretien : 0 à 1 200 € par an (R1:160) | Choisir, configurer, relier, former, tenir les échéances (SPEC:65-67) | Gérer les biens d'autrui, encaisser, relancer en son nom : activité réglementée (loi n° 70-9) ; exclue (STRAT:650 ; R2:38) |
| **(2) Logiciel hôtelier** (« PMS »), si l'ancien bar-restaurant-hôtel reprend un hébergement | Réservations, chambres, facturation des séjours, taxe de séjour, fiches de police | 9 Hôtellerie (option) | 1 500 à 4 000 € par an pour 10 à 20 chambres (R1:143) | Aider au choix sur critères (SPEC:419-428) ; reprendre les totaux | Le construire : caisse, carte bancaire, données de voyageurs (R2:235) ; exploiter l'hôtel (STRAT:647) |
| **(3) Pilotage de plusieurs lieux** | Galerie, cabaret, commerces : fiche du lieu, autorisations, budgets, vue d'ensemble | 4 Exploitation des lieux ; 7 Tableau de bord ; plus les modules communs 5, 6 et 8 (SPEC:23-24) | Caisse : 1 200 à 6 000 € par an pour deux postes ; billetterie à la commission (R1:175, 185) ; aucun outil du marché ne réunit plusieurs sociétés et des lieux de nature différente [HY] (SPEC:67) | La couche commune : c'est là qu'un travail propre a le plus de sens (R2:73) | Caisse ou billetterie sur mesure (R2:39, 267) ; exploitation et licences (STRAT:647) |

**Architecture retenue pour l'option B** [PR, cette étude], module par module :

| Module (SPEC) | Acheter, configurer ou construire | Lot (section 3.4) | Utilisateur principal |
| --- | --- | --- | --- |
| T. Couche commune : comptes, droits, journal, sauvegardes, export | Configurer un outil existant au nom de l'entité ; scripts légers | L2 | — |
| 1. Patrimoine | Configurer (base commune) | L2 ; L5 par extension | Administratrice |
| 2. Baux et locataires | **Acheter** une gestion locative du marché, testée sur le jeu d'essai de vingt baux ; construire seulement si aucune ne passe (SPEC:65, 208) | L1 (essai) ; L2 (bâtiment pilote) ; L3 (liaison) | Administratrice, ou administrateur de biens |
| 3. Travaux et entretien | Acheter ou configurer ; registre de sécurité et échéances dans la base | L2 ; L5 | Administratrice ; responsables de lieux |
| 4. Exploitation des lieux | Configurer la fiche du lieu ; reprendre les clôtures de caisse et de billetterie | L2 (fiche) ; L3 (totaux) | Responsables de lieux |
| 5. Documents et échéances | Configurer ; rappels automatiques après essai | L2 ; résumé hebdomadaire en L4 | Administratrice |
| 6. Finances | Construire léger : formules, imports par fichier, export comptable | L3 | Administratrice ; expert-comptable |
| 7. Tableau de bord | Configurer, puis compléter | L2 (minimal) ; L4 | GianLuca ; administratrice |
| 8. Assistant IA | Configurer une offre professionnelle (option 3 de PRO7:81) | L4 | Utilisateurs autorisés |
| 9. Hôtellerie | Acheter ; reprendre les totaux | Option : 1,5 à 3 JP [ES], 2 300 € HT | Exploitant |
| Caisse, billetterie, plateforme agréée, comptabilité | Acheter (obligations : R2:33, 39) | — | Exploitants ; expert-comptable |

### 1.4 Ce que 72 000 € ou 24 000 € par an achètent d'habitude

- **Pas seulement un abonnement.** Un assemblage d'outils du marché pour le cas type coûte ≈ 3 460 à 13 010 € par an, briques communes comprises [ES] (R1:217-227). À 24 000 ou 72 000 € par an, on achète en général **du travail humain** : un service de gestion délégué, une équipe de développement, une astreinte, un salarié (R1:32, 264-271).
- **Si c'est un service de gestion** (encaissement, relances, comptes des propriétés) : il faut le comparer à un administrateur de biens titulaire de la carte, à 5 à 8 % HT des sommes encaissées [FV, barèmes 2025 et 2026] (R1:256), pas à un logiciel. Exemple de cohérence [HY] : des loyers de 75 000 à 150 000 € par an donneraient 3 750 à 12 000 € d'honoraires (R1:260). Marwin ne peut pas offrir ce service (STRAT:650).
- **Signaux d'alerte à vérifier** : prix sans périmètre écrit ; paiement d'avance par trimestre ; location financière ; données ou code non restitués ; encaissement sans carte professionnelle ; caisse sans certificat (R1:273-288).

### 1.5 Questions à poser à GianLuca

**Règles** [PR] : aucune question avant D03 (notification CNIL), D08 (information des personnes) et l'accord écrit des deux associés (MAJ:370) ; elles passent par GianLuca ou son administratrice, jamais par un contact avec Accord ; la première question porte sur la confidentialité (section 6.6). Le plus simple est qu'il transmette la proposition écrite, ou qu'il en résume lui-même le contenu.

| N° | Question (formulation proposée, en vouvoiement) | Ce qu'elle tranche |
| --- | --- | --- |
| Q1 | « La proposition que vous avez reçue porte-t-elle une mention de confidentialité ? Si oui, nous ne la lirons pas ; vous pourrez nous dire vous-même ce qu'elle couvre. » | Réception de la pièce (section 6) |
| Q2 | « Pouvez-vous nous transmettre la proposition écrite, ou nous dire, ligne par ligne, ce qu'elle couvre ? » | Toute la comparaison |
| Q3 | « Le prix est-il de 6 000 € par mois ou par trimestre ? HT ou TTC ? Payé d'avance ? » | Lecture (a) ou (b) ; facteur 3 |
| Q4 | « S'agit-il d'un logiciel existant sous licence, d'un développement pour vous, d'un service de gestion (encaissements, relances, comptes), de maintenance, ou d'un mélange ? » | Nature : logiciel ou travail humain |
| Q5 | « Pour quels bâtiments, lots, baux et lieux ? Combien d'utilisateurs ? Y a-t-il un hôtel, une caisse, une billetterie ? » | Périmètre ; sens (1), (2) ou (3) |
| Q6 | « Quelle durée d'engagement, quel préavis, quels frais de sortie ? Le contrat passe-t-il par une société de location financière ? » | Engagement (R1:279) |
| Q7 | « À qui appartiennent les données ? Où sont-elles hébergées ? Pouvez-vous en obtenir un export complet vous-même, sous quel format, en combien de jours ? » | Propriété des données ; réversibilité |
| Q8 | « S'il y a un développement, à qui appartient le code ? Recevez-vous les sources ? » | Propriété du code (R2:338) |
| Q9 | « Quel niveau de service est écrit : heures couvertes, délai de prise en charge, délai de rétablissement, pénalités, astreinte ? » | Niveau de service |
| Q10 | « Le prestataire encaisse-t-il des loyers ou gère-t-il des baux pour vous ? Avec quelle carte professionnelle ? » | Loi n° 70-9 (R2:193) |
| Q11 | « Le logiciel est-il relié à une plateforme agréée de facturation électronique ? Applique-t-il les règles du bail commercial de mai 2026 ? » | Conformité (R2:33-36) |
| Q12 | « Utilise-t-il de l'IA ? Laquelle, où, avec quelles données ? » | Données ; règlement sur l'IA (R2:309-319) |
| Q13 | « L'offre est-elle signée ? Avant quelle date devez-vous répondre ? » | Urgence ; risque de rupture d'un contrat signé (section 6.5) |
| Q14 | « Quel problème voulez-vous régler d'abord : vos bâtiments et vos baux, un hôtel, ou le suivi de vos lieux ? Qu'est-ce qui vous a plu dans cette offre ? » | Sens prioritaire ; critères de GianLuca |
| Q15 | « Qui utilisera l'outil chaque jour ? Votre administratrice ? Quels outils utilise-t-elle déjà ? Combien de baux, de lots, de lieux, de sociétés ? » | Volumes ; utilisatrice (SPEC:618-646) |

---

## 2. Trois options pour GianLuca, chiffrées sur trois ans

### 2.1 Hypothèses communes [HY]

- **Horizon** : 36 mois à partir du début des travaux (central : janvier 2027 à décembre 2029). Montants HT ; arrondis à l'euro dans les calculs, à la centaine dans le texte.
- **Périmètre comparé : le « cœur »** (modules 1 à 8 de la spécification). Les **briques communes** à toutes les options (caisse, billetterie, logiciel hôtelier, plateforme agréée, comptabilité) sont comptées à part : ≈ 10 300 à 37 000 € sur trois ans [ES] (R1, modules 2, 4, 5 : 2 700 à 10 000 € par an × 3, plus 2 200 à 7 000 € de mise en place et de matériel ; plateforme agréée [IN]). Si l'offre d'Accord les comprend, il faut les ajouter à A, B et C avant de comparer.
- **Les options ne couvrent pas le même périmètre** [FV, d'après 3.4] : B réduite ne couvre ni les finances (module 6, lot L3) ni l'assistant (module 8, lot L4), et un seul bâtiment et un seul lieu ; B complète couvre le cœur pour cinq bâtiments ou lieux (le bâtiment et le lieu du pilote, plus trois extensions). Une offre qui couvrirait tout le parc [HY] se compare à B complète, plus les extensions manquantes (2.7).
- **Le cadrage général** (6 500 € HT, STRAT:197) n'est pas compté : il sert à tous les projets.
- **Temps de l'administratrice** : seulement le temps dû à l'outil (mise en place, formation, essais, saisie en double, consolidation entre outils, contrôles hebdomadaires), pas son travail de gestion. Coût d'un jour : **125 à 342 €** [ES], du coût employeur d'un assistant non cadre (2 249 € par mois ÷ 18 jours) à celui d'un cadre (6 149 € ÷ 18) [MM] (STRAT:326, 376). Son statut et son coût réels sont [IN] (MAJ:44).

| Option | Mise en place (jours) | Récurrent (jours par mois) | Total sur 36 mois (jours) | Coût [ES] |
| --- | --- | --- | --- | --- |
| A | 5 à 10 | 1 à 3 : consolidation entre trois à cinq outils, double saisie | 41 à 118 | 5 125 à 40 356 € |
| B réduite | 6 à 10 | 0,75 à 1,5 : consolidation des finances encore manuelle | 33 à 64 | 4 125 à 21 888 € |
| B complète | 6 à 10 | 0,5 à 1 : contrôle hebdomadaire des automatismes | 24 à 46 | 3 000 à 15 732 € |
| C | 10 à 18 : recette de neuf modules | 0,5 à 1 | 28 à 54 | 3 500 à 18 468 € |
| Accord, si c'est un logiciel intégré | 6 à 10 (même hypothèse que B complète) | 0,5 à 1 | 24 à 46 | 3 000 à 15 732 € |
| Accord, si c'est un service de gestion | [IN] | [IN] | [IN] | [IN] |

Calcul : jours = mise en place + 36 × récurrent ; coût = jours bas × 125 € à jours hauts × 342 €. **C'est le poste le plus incertain de l'étude** : il n'est mesuré nulle part [IN]. Les totaux sont donc donnés avec et sans lui.

### 2.2 Option A : logiciels du marché seuls

L'entité de GianLuca souscrit et configure elle-même, avec l'aide des éditeurs.

| Poste | Trois ans [ES] | Base |
| --- | ---: | --- |
| Mise en place externe | 0 à 5 000 € | Outils en libre-service, jusqu'à une mise en service payante d'un outil d'entretien (490 à 4 990 € [DR], R1:157) |
| Abonnements du cœur | 2 280 à 9 030 € | 760 à 3 010 € par an : gestion locative 120 à 850, entretien 0 à 1 200, pilotage (sièges et espace de registre) 640 à 960 (R1:219-224) |
| Hébergement | 0 € | Compris dans les abonnements |
| Maintenance | 0 € | Assurée par les éditeurs, mises à jour réglementaires comprises (R2:36, 158) |
| Évolutions | 0 € | Feuille de route des éditeurs ; aucune adaptation possible |
| **Sous-total** | **2 280 à 14 030 €** | |
| Temps de l'administratrice | 5 125 à 40 356 € | 2.1 |
| **Total** | **7 405 à 54 386 €** | |

**Forces** : coût direct très bas, mise en route immédiate, règles tenues par les éditeurs. **Faiblesses** : aucune vue d'ensemble de plusieurs sociétés et lieux ; double saisie ; échéances dispersées ; qualité de configuration inégale [HY].

### 2.3 Option B : logiciels du marché et couche Marwin

Deux variantes : **B réduite** = première étape seule (lots L0, L1, L2 : choix, essai, pilote) ; **B complète** = toutes les étapes (L0 à L4 et trois extensions L5). Prix des lots : section 3.5.

| Poste | B réduite [ES] | B complète [ES] | Base |
| --- | ---: | ---: | --- |
| Mise en place par Marwin | 18 700 € | 36 200 € | L0 + L1 + L2 = 3 000 + 5 300 + 10 400 ; + L3 7 500 + L4 6 400 + 3 × L5 1 200 (3.5) |
| Abonnements et hébergement, payés par l'entité sans marge | 3 000 à 12 630 € | 3 360 à 15 510 € | Réduite : 1 000 à 4 210 € par an (gestion locative 120 à 850 ; entretien 0 à 1 200 ; base commune et sièges 640 à 960 ; automate et petit serveur dans l'Union 240 à 1 200). Complète : + IA par API 120 à 960 € par an (PRO7:371) |
| Maintenance par Marwin | 21 000 à 30 000 € | 34 000 à 35 200 € | Réduite : 700 à 1 000 € par mois (DL6) des mois 7 à 36 (30 mois). Complète : 700 à 1 000 € des mois 7 à 10, puis 1 200 € des mois 11 à 36 (4 × 700 ou 4 × 1 000, + 26 × 1 200) (3.6) |
| Évolutions | 3 600 à 7 200 € | 5 400 à 10 800 € | Années 2 et 3 : 2 à 4 JP par an (réduite), 3 à 6 JP par an (complète), à 900 € par JP (STRAT:203) |
| **Sous-total** | **46 300 à 68 530 €** | **78 960 à 97 710 €** | |
| Temps de l'administratrice | 4 125 à 21 888 € | 3 000 à 15 732 € | 2.1 |
| **Total** | **50 425 à 90 418 €** | **81 960 à 113 442 €** | |

**Ce que B apporte de plus que A** [HY] : une fiche unique par bâtiment et par lieu, les échéances de toutes les sociétés en un seul endroit, une vue d'ensemble, des liaisons qui évitent la double saisie, une restauration et une sortie testées, une passation à l'administratrice. **Ce que cela coûte de plus que A** : ≈ 44 000 à 54 500 € sur trois ans pour B réduite, hors temps de l'administratrice [ES]. Ce surcoût n'est justifié que si le pilote mesure un gain réel (temps, échéances manquées évitées) : c'est la règle de la spécification, « Mesurer avant de promettre » (SPEC:35).

### 2.4 Option C : développement sur mesure complet

| Poste | C au prix du marché [ES] | C au prix de Marwin [ES] | Base |
| --- | ---: | ---: | --- |
| Construction | 40 054 à 151 110 € | 126 000 € | 98,9 à 167,9 JP (3.3) × 405 € (indépendant en région, STRAT:399) à × 900 € (agence, R1:202) ; Marwin : règle des lots (3.5) |
| Outils du cœur pendant la construction (12 mois) et IA par API | 1 120 à 5 890 € | 1 120 à 5 890 € | 760 à 3 010 € pour un an d'outils du marché ; API 120 à 960 € par an × 3 |
| Hébergement | 3 600 à 7 200 € | 3 600 à 7 200 € | 1 200 à 2 400 € par an (R1:208, 211) ; R1:208 cite aussi 200 à 2 000 € par mois selon les sources : la borne haute retenue est basse |
| Maintenance (24 mois, si livraison au mois 12) | 12 016 à 75 555 € | 72 000 € | Marché : 15 à 25 % du coût initial par an [DR] (R1:206). Marwin : 3 000 € par mois (3.6) |
| Évolutions | Non comptées : la maintenance du marché couvre corrections, sécurité et compatibilité (R1:345), pas les évolutions | Non comptées : la maintenance de Marwin les exclut, elles sont sur devis (3.6) | C est donc sous-estimée dans les deux colonnes [HY] |
| **Sous-total** | **56 790 à 239 755 €** | **202 720 à 211 090 €** | |
| Temps de l'administratrice | 3 500 à 18 468 € | 3 500 à 18 468 € | 2.1 |
| **Total** | **60 290 à 258 223 €** | **206 220 à 229 558 €** | |

**Le chiffre « Marwin » est théorique** : une livraison au mois 12 demanderait 8 à 14 JP de production par mois, alors que Marwin en a ≈ 4 pour un lot (CAP:328-331) (section 3.3). Pendant une construction plus longue, l'administratrice travaille comme en A : son temps est sous-estimé ici [HY]. Le sur mesure porte aussi la veille réglementaire du bail (quatre règles changées en six mois, R2:36, 158), la facturation électronique par une plateforme agréée (R2:98) et la responsabilité des calculs.

### 2.5 Synthèse et comparaison avec les deux lectures de l'offre d'Accord

**Prix seul**, hors temps de l'administratrice, contre le prix annoncé d'Accord pris HT :

| Option | Trois ans [ES] | Part de la lecture (a), 216 000 € | Écart avec (a) | Part de la lecture (b), 72 000 € | Écart avec (b) |
| --- | ---: | ---: | ---: | ---: | ---: |
| A, marché seul | 2 280 à 14 030 € | 1 à 6 % | 202 000 à 213 700 € de moins | 3 à 19 % | 58 000 à 69 700 € de moins |
| B réduite | 46 300 à 68 530 € | 21 à 32 % | 147 500 à 169 700 € de moins | 64 à 95 % | 3 500 à 25 700 € de moins |
| B complète | 78 960 à 97 710 € | 37 à 45 % | 118 300 à 137 000 € de moins | 110 à 136 % | **7 000 à 25 700 € de plus** |
| C, marché | 56 790 à 239 755 € | 26 à 111 % | de 23 800 € de plus à 159 200 € de moins | 79 à 333 % | de 167 800 € de plus à 15 200 € de moins |
| C, Marwin (théorique) | 202 720 à 211 090 € | 94 à 98 % | 4 900 à 13 300 € de moins | 282 à 293 % | ≈ 130 700 à 139 100 € de plus |

**Avec le temps de l'administratrice des deux côtés** (pour Accord, l'hypothèse d'un logiciel intégré : 3 000 à 15 732 €, soit 219 000 à 231 732 € en lecture a et 75 000 à 87 732 € en lecture b) :

| Option | Trois ans [ES] | Part de (a) | Part de (b) | Si le prix d'Accord est TTC (b = 60 000 € HT, soit 63 000 à 75 732 €) |
| --- | ---: | ---: | ---: | --- |
| A | 7 405 à 54 386 € | 3 à 23 % | 10 à 62 % | 12 à 72 % : toujours moins cher |
| B réduite | 50 425 à 90 418 € | 23 à 39 % | 67 à 103 % | 80 à 119 % : **de 12 600 € de moins à 14 700 € de plus** |
| B complète | 81 960 à 113 442 € | 37 à 49 % | 109 à 129 % | 130 à 150 % : plus cher |
| C, marché | 60 290 à 258 223 € | 28 à 111 % | 80 à 294 % | Plus cher, sauf la borne basse |
| C, Marwin | 206 220 à 229 558 € | 94 à 99 % | 262 à 275 % | Plus cher |

Méthode : part = coût de l'option ÷ coût d'Accord, borne basse sur borne basse et borne haute sur borne haute ; les calculs sont refaits en annexe A.

**Lecture** [ES] :
1. **Contre la lecture (a)**, toutes les options utiles sont nettement moins chères : B réduite coûte d'un cinquième à un tiers, B complète moins de la moitié.
2. **Contre la lecture (b)**, seule l'option A l'est à coup sûr. B réduite coûte 64 à 95 % de (b) sur le prix seul, 67 à 103 % temps de l'administratrice compris, si le prix d'Accord est HT ; donc **à périmètre réduit** (un bâtiment et un lieu, sans finances ni assistant), et pas à coup sûr : au même coût par jour de l'administratrice (342 €), avec des jours aux bornes opposées, B réduite coûte 90 418 € contre 80 208 € pour (b). Elle peut aussi ne plus l'être si le prix d'Accord est TTC. **B complète, la plus proche d'une offre qui couvrirait tout le parc, est plus chère que la lecture (b).** C l'est presque toujours. Sensibilités : 2.7.
3. **Si Accord vend un service de gestion humain**, ces comparaisons ne valent pas : il faut comparer avec un administrateur de biens (1.4).
4. **Si l'offre d'Accord comprend les briques communes**, ajouter 10 300 à 37 000 € à A, B et C (2.1) : la conclusion contre (a) ne change pas ; contre (b), B réduite passe à 56 600 à 105 530 € sur le prix seul, soit 79 à 147 % de (b) : moins chère seulement dans le bas de la fourchette [ES].
5. **Si l'entité ne récupère pas la TVA** (locations nues sans option, R2:34), elle paie nos prix TTC : B réduite coûte alors 55 600 à 82 200 € TTC sur le prix seul, contre 72 000 € pour (b) si ce prix est TTC, et 86 400 € s'il est HT [ES]. Le régime de TVA de chaque entité est [IN].

### 2.6 Ce que le coût ne dit pas

| Critère | A | B réduite | B complète | C |
| --- | --- | --- | --- | --- |
| Délai avant un premier usage | Immédiat | Pilote vers mi-mai 2027 en central (3.9) | Mise en service générale vers février 2028 au plus tôt : trois extensions tenues quatre semaines chacune (SPEC:607) | 2029 au plus tôt avec Marwin ; 9 à 18 mois avec une agence [HY] |
| Vue d'ensemble multi-sociétés | Non | Oui, pour le bâtiment et le lieu du pilote, puis par extension | Oui | Oui |
| Qui porte les règles du bail | Éditeur | Éditeur (gestion locative achetée) | Éditeur | Le prestataire, avec une veille payée (R2:158) |
| Propriété et sortie | Exports des éditeurs | Comptes et code au nom de l'entité ; sortie testée (SPEC:567-579) | Idem | Idem si le contrat le prévoit |
| Dépendance à une personne | Faible | Moyenne (Marwin, deux associés) | Plus forte | Forte |
| Risque principal | Dispersion, oublis | Adoption ; capacité de Marwin | Coût ; capacité | Coût, délai, responsabilité |

### 2.7 Sensibilités défavorables (relecture contradictoire du 9 nov. 2026)

Les tableaux de 2.5 retiennent pour B réduite des hypothèses qui lui sont favorables. Chaque ligne ci-dessous change une hypothèse ; les deux lignes « ensemble » en combinent plusieurs. Toutes sont des [ES] ; les hypothèses changées sont des [HY].

| Hypothèse changée | Pourquoi | Coût sur trois ans [ES] (B réduite, sauf dernière ligne) | Comparaison avec la lecture (b), prix d'Accord HT |
| --- | --- | ---: | --- |
| Aucune (2.5) | — | 46 300 à 68 530 € (prix seul) | 64 à 95 % de 72 000 € |
| Cadrage compté (6 500 €) | Aucun pilote sans cadrage payé et réceptionné (STRAT:42) ; s'il n'est commandé que pour le logiciel, il entre dans son coût | 52 800 à 75 030 € (prix seul) | 73 à 104 % |
| Support réaliste : maintenance à 1 000 € par mois aux deux bornes | Support de 0,25 à 0,5 JP par mois au lieu de 0,02 à 0,04 (3.6) ; borne basse + 30 mois × 300 € ; la borne haute de 2.3 compte déjà 1 000 € | 55 300 à 68 530 € (prix seul) | 77 à 95 % |
| Ensemble : cadrage et support réaliste | Les deux lignes précédentes | 61 800 à 75 030 € (prix seul) | **86 à 104 %** |
| Temps de l'administratrice comme en A hors du pilote | B réduite ne relie qu'un bâtiment et un lieu ; ailleurs, 1 à 3 jours par mois comme en A : 42 à 118 jours, 5 250 à 40 356 € | 51 550 à 108 886 € (temps compris) | (b) temps compris : 75 000 à 87 732 € ; 69 à 124 % |
| Bornes croisées, même coût par jour (342 €) | B réduite au haut (64 jours), Accord au bas (24 jours) | 90 418 € (temps compris) | 80 208 € : **B réduite plus chère d'environ 10 200 €** |
| Ensemble : cadrage, support réaliste, temps comme en A | — | 67 050 à 115 386 € (temps compris) | 89 à 132 % de (b) temps compris |
| Périmètre égal : B complète et trois extensions de plus | Six bâtiments, un cabaret et des commerces évoqués [DR] (R3:38) ; hypothèse de huit bâtiments ou lieux [HY] ; B complète en couvre cinq (le bâtiment et le lieu du pilote, plus trois extensions) ; + 3 × 1 200 € ; Accord supposé (logiciel intégré) couvrir tout le parc [HY] | 82 560 à 101 310 € (prix seul) | **115 à 141 %** |

**Non comptés, dans aucune option** [IN] : honoraires de l'expert-comptable et de l'avocat du client qui valident le jeu d'essai (SPEC:125) ; préalables sur les données des locataires (contrat de l'article 28, registre, PRO7:605-616) ; sortie à blanc avant la mise en service générale puis chaque année (SPEC:571) ; revue de sécurité par un tiers, prudente après la fuite ; astreinte, exclue (STRAT:355) et à chiffrer à part si un lieu en a besoin ; extensions au-delà du parc supposé. Ces postes alourdissent B et C plus que A ; certains concernent aussi l'offre d'Accord [IN].

**Conclusion de la relecture** [ES] : contre la lecture (a), l'avantage tient dans toutes les lignes. Contre la lecture (b), il ne tient qu'à périmètre réduit et dans le bas des fourchettes ; à périmètre égal, Marwin est plus chère. La mise en cohérence du 9 nov. (L2 à 10 400 € et maintenance de 700 à 1 000 €, section 3.5 et 3.6) renforce cette conclusion : la borne haute de B réduite passe de 82 à 95 % de (b), prix seul.

---

## 3. Charge, prix, marge et capacité de Marwin Tech

### 3.1 Méthode [PR, cette étude]

- **JP sans IA** : estimation par tâche, comme le ferait un prestataire qui n'utilise pas d'assistant de code [ES]. Chaque tâche a une **part de développement** `s` (écrans, code, tests, scripts), la seule que l'IA accélère.
- **JP avec IA** : borne basse = Σ JP basses × (1 − 0,30 × s) ; **borne haute inchangée** (aucun gain garanti, 3.2). Elles servent à la marge du meilleur cas, pas au prix.
- **Prix par la règle des lots** (STRAT:287 ; CAT:71) : formule = JP centrales **sans IA** × 800 € × 1,15 (provision de risque haute, logiciel) ; **plancher = 750 € × borne haute** ; **prix proposé = la plus grande des deux valeurs, arrondie à la centaine supérieure**. C2 suit cette formule (6,5 JP centrales × 920 € ≈ 6 000 €, STRAT:314) ; C6 suit une provision de 10 % (8,5 × 880 € ≈ 7 500 €, STRAT:333).
- **Marge** = (prix − JP × coût complet) ÷ prix, au coût de la première année, 710 à 885 € par JP à 10 JP facturées (CAT:48). Pire cas : borne haute au coût haut ; meilleur cas : borne basse avec IA au coût bas.
- **Contrôle** : prix ÷ JP centrales sans IA, à comparer au prix cible de 800 à 950 € par JP estimée (STRAT:397).

> **Mise en cohérence du 9 nov. : retour à la règle de la stratégie pour la formule de prix** (ancien écart, levé).
> *Ce que dit la stratégie.* « Prix = JP estimées × 800 € HT + provision de risque de 10 à 15 % » (STRAT:287) ; le prix est fixé « à partir d'une référence mesurée **avant** l'automatisation » et « le gain obtenu pendant la période revient à Marwin » (STRAT:418).
> *Ce que faisait la version précédente.* La formule partait des JP centrales **avec IA** : L2 tombait de 10 400 € à 10 200 €, une petite remise d'IA consentie d'avance, contraire à la règle de 3.2 (« l'IA n'est jamais présentée comme une remise »). La relecture contradictoire recommandait de revenir à la stratégie.
> *Ce que fait désormais l'étude* [PR]. Formule sur les JP centrales sans IA, comme la stratégie et comme la proposition client du 9 nov. : L2 à **10 400 €**, B réduite à **18 700 €**, B complète à **36 200 €**. Les autres prix ne changent pas (plancher ou arrondi).
> *Décision.* DL5 : confirmer par écrit (section 7).

### 3.2 Gain attendu de l'IA, et ses limites

| Point | Ce que l'on sait | Code | Source |
| --- | --- | --- | --- |
| Effet mesuré sur le développement | De 19 % de temps en plus (METR 2025, développeurs expérimentés sur leurs projets) à 26 % de tâches en plus (trois essais en entreprise) ; METR juge ses mesures de début 2026 peu fiables | [FV] | R1:323-325 |
| Hypothèse retenue | 0 à 30 % de temps en moins sur la part `s` ; aucun gain sur l'analyse des règles, la validation par l'expert-comptable et l'avocat, la recette, la formation, la coordination | [HY] | R1:338 |
| Effet sur nos estimations | Borne basse réduite de 7,8 % (B réduite : 16 → 14,75 JP), 9,5 % (B complète : 30 → 27,16), 12,8 % (C : 98,9 → 86,24) | [ES] | Annexe A |
| Effet sur nos prix | **Aucun** : le prix part des JP sans IA (3.1). Comptée dans la formule, l'IA n'aurait baissé que L2, de 200 € (10 400 € à 10 200 €) ; ailleurs, le plancher, fixé sur la borne haute, ou l'arrondi donnent le même prix (3.5) | [ES] | Annexe A |
| Ce que l'IA ne réduit pas | Maintenance (15 à 25 % par an), sécurité (44 à 45 % des tâches de code produisent une faille connue), support, responsabilité, conformité, réversibilité | [FV/DR] | R1:327, 343-352 |
| Nos propres gains | Jamais mesurés : Marwin produit vite, mais n'a encore livré ni maintenu aucun outil chez un client | [FV négatif] | CAP:16 ; PRO7:20 |
| Où l'IA aide vraiment | Maquette (L1) plus rapide ; tests, scripts d'import, documentation en brouillon ; dans le produit, classement des documents, recherche avec citations, brouillons (gain de temps de l'administratrice, à mesurer avant toute promesse) | [HY] | SPEC:35, 148, 300 |

**Règle** [PR] (R1:356-359) : l'IA n'est jamais présentée comme une remise. Le gain, s'il vient, reste à Marwin pendant la période ; au renouvellement de la maintenance, un tiers du gain mesuré revient au client (STRAT:418-420). Un ralentissement, possible, **n'est pas couvert par la provision** : quand le plancher fixe le prix, celui-ci ne dépasse 750 € × borne haute que de l'arrondi. Si le ralentissement de METR 2025 (+19 %) touchait la part `s`, la borne haute de B réduite passerait de 24,5 à ≈ 25,7 JP, et la marge du pire cas de −16 % à −22 % [ES]. Seule parade : mesurer, et abandonner l'IA sur les tâches où elle ralentit.

### 3.3 Option C : charge par module

| Module ou étape (SPEC) | JP sans IA [ES] | Part `s` | JP avec IA [ES] | Ce qui pèse |
| --- | --- | --- | --- | --- |
| T. Socle technique commun | 10 à 16 | 0,6 | 8,2 à 16 | Double authentification, droits par société et par lieu, journal inaltérable, sauvegardes en trois copies, restauration, export complet, import avec rapport, bouton d'arrêt (SPEC:109-115, 534-571) |
| 1. Patrimoine | 4 à 7 | 0,65 | 3,22 à 7 | Fiches, diagnostics, assurances, surface tertiaire (SPEC:129-157) |
| 2. Baux et locataires | 14 à 24 | 0,5 | 11,9 à 24 | Indices, révision, échelle mobile, lissage, clause d'encadrement, loi de mai 2026, charges, dépôt, quittances, relances, rapprochement, données de facture ; jeu d'essai de vingt baux validé au centime (SPEC:159-212) |
| 3. Travaux et entretien | 8 à 13 | 0,6 | 6,56 à 13 | Devis, chantiers, vérifications, registre de sécurité, accessibilité, OPERAT (SPEC:214-253) |
| 4. Exploitation des lieux | 5 à 9 | 0,5 | 4,25 à 9 | Formats de caisse et de billetterie inconnus (R3:322) |
| 5. Documents et échéances | 7 à 11 | 0,6 | 5,74 à 11 | Coffre, classement assisté, rappels, résumé, registre des décisions, recherche (SPEC:284-312) |
| 6. Finances | 9 à 15 | 0,55 | 7,51 à 15 | Budgets, engagé, réel, trésorerie, pièces du mois, export comptable, opérations entre sociétés (SPEC:314-346) |
| 7. Tableau de bord | 3 à 5 | 0,65 | 2,42 à 5 | Douze indicateurs au plus par vue (SPEC:371) |
| 8. Assistant IA | 6 à 10 | 0,5 | 5,1 à 10 | Citations, droits, documents piégés, plafond de dépense, trente questions (SPEC:375-411) ; repère 4 à 8 JP de conception (PRO7:370) |
| 9. Hôtellerie (choix et reprise des totaux) | 2 à 4 | 0,3 | 1,82 à 4 | SPEC:413-443 |
| Étape 1 : cadrage du logiciel | 3 à 5 | 0 | 3 à 5 | SPEC:604 |
| Étape 2 : maquette cliquable | 4 à 7 | 0,6 | 3,28 à 7 | SPEC:605 |
| Étape 3 : pilote | 5 à 8 | 0,2 | 4,7 à 8 | SPEC:606 |
| Étape 4 : mise en service, quatre extensions | 6 à 12 | 0,2 | 5,64 à 12 | SPEC:607 |
| Sous-total | 86 à 146 | — | 73,34 à 146 | — |
| Coordination, contrôle à quatre yeux, documentation, formation (15 % du sous-total sans IA) | 12,9 à 21,9 | 0 | 12,9 à 21,9 | [HY] |
| **Total C** | **98,9 à 167,9** | — | **86,24 à 167,9** | Repère : 10 à 50 JP et plus **par processus** en développement spécifique (PRO7:320) |

**Prix de C par la règle** : formule sans IA 133,4 × 920 = 122 728 € ; avec IA 127,07 × 920 = 116 904 € ; plancher 750 × 167,9 = 125 925 € ; **prix 126 000 € HT** (151 200 € TTC), ≈ 945 € par JP centrale. Marge : −17,9 % à +51,4 %.
**Délai** [ES] : à ≈ 4 JP par mois pour le lot en cours, un lot à la fois (CAP:328), **25 à 42 mois** (21,6 au mieux avec IA) ; même à 10 JP par mois, sans rien d'autre pour GianLuca, 10 à 17 mois. **C n'est pas faisable par Marwin la première année** sous le plafond de 10 JP (STRAT:485).

### 3.4 Option B : charge par lot

| Lot | Tâche | JP sans IA [ES] | `s` |
| --- | --- | --- | --- |
| **L0 Choix des briques** | Lecture de la proposition écrite, si elle est reçue dans les règles de 6.6 | 0,5 | 0 |
| | Grille par module et coût sur trois ans selon les deux lectures | 1 à 1,5 | 0 |
| | Deux ou trois solutions du marché par module, sur pages publiques | 0,5 à 1 | 0 |
| | Questions aux professionnels, critères de réception écrits | 0,5 à 1 | 0 |
| | **Total L0** | **2,5 à 4** | — |
| **L1 Essai sur données fictives** | Maquette cliquable de la couche commune (fiches, échéances, registre, tableau) | 2 à 3 | 0,6 |
| | Jeu d'essai de vingt baux ; essai de la gestion locative retenue sur un compte d'essai ouvert au nom de l'entité, par elle | 1,5 à 2,5 | 0,2 |
| | Dix scénarios avec l'administratrice, corrections (SPEC:605) | 0,5 à 1 | 0,3 |
| | Contrôle à quatre yeux | 0,5 | 0 |
| | **Total L1** | **4,5 à 7** | — |
| **L2 Pilote : base commune et échéances, un bâtiment et un lieu** | Base commune configurée : sociétés, bâtiments, lots, lieux, documents, registre des décisions | 2,5 à 3,5 | 0,4 |
| | Échéances et rappels automatiques après essai | 1 à 1,5 | 0,6 |
| | Logiciels du marché retenus configurés pour le bâtiment pilote ; import des baux | 1 à 1,5 | 0,1 |
| | Tableau du lieu et vue d'ensemble minimale | 0,5 à 1 | 0,5 |
| | Droits, journal, sauvegardes, restauration testée, export complet, bouton d'arrêt | 1 à 1,5 | 0,4 |
| | Import avec rapport, suivi du pilote sur quatre semaines, mesure du temps | 1,5 à 2 | 0,1 |
| | Procédures, fiches de secours, deux formations | 1 à 1,5 | 0 |
| | Contrôle à quatre yeux | 0,5 à 1 | 0 |
| | **Total L2** | **9 à 13,5** | — |
| **L3 Raccordements et finances** | Loyers appelés et encaissés, importés de la gestion locative | 1 à 2 | 0,6 |
| | Clôtures de caisse et de billetterie (format réel exigé avant tout travail, R3:322) | 1 à 2 | 0,6 |
| | Relevés bancaires par fichier, rapprochement assisté | 1 à 1,5 | 0,6 |
| | Budgets, engagé, réel, écarts par formule ; pièces du mois ; export comptable | 2 à 3 | 0,5 |
| | Essais, journal, fiches de secours, contrôle | 1 à 1,5 | 0,1 |
| | **Total L3** | **6 à 10** | — |
| **L4 Tableau de bord et assistant** | Tableau multi-sociétés, alertes, synthèse mensuelle | 1,5 à 2,5 | 0,6 |
| | Résumé hebdomadaire automatique (repère : 2 à 4 JP sans base existante, PRO7:370) | 1 à 2 | 0,6 |
| | Assistant documentaire : offre professionnelle configurée, citations, droits par périmètre, trente questions, cinq documents piégés, plafond (repère 2 à 3,5 JP, PRO7:370) | 2 à 3,5 | 0,3 |
| | Contrôle | 0,5 | 0 |
| | **Total L4** | **5 à 8,5** | — |
| **L5 Extension** | Un bâtiment ou un lieu de plus : import, contrôles, quatre semaines de critères (SPEC:607) | 1 à 1,5 | 0,1 |

### 3.5 Prix des lots

| Lot | JP sans IA | JP avec IA | Formule sans IA | Formule avec IA | Plancher (750 × borne haute) | **Prix proposé HT** | TTC | € par JP centrale | Marge [ES] (pire ; meilleur) |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| L0 Choix des briques | 2,5 à 4 | 2,5 à 4 | 2 990 € | 2 990 € | 3 000 € | **3 000 €** | 3 600 € | 923 € | −18,0 % ; +40,8 % |
| L1 Essai sur données fictives | 4,5 à 7 | 4,0 à 7 | 5 290 € | 5 062 € | 5 250 € | **5 300 €** | 6 360 € | 922 € | −16,9 % ; +46,3 % |
| L2 Pilote | 9 à 13,5 | 8,25 à 13,5 | 10 350 € | 10 005 € | 10 125 € | **10 400 €** | 12 480 € | 924 € | −14,9 % ; +43,7 % |
| L3 Raccordements et finances | 6 à 10 | 5,13 à 10 | 7 360 € | 6 960 € | 7 500 € | **7 500 €** | 9 000 € | 938 € | −18,0 % ; +51,4 % |
| L4 Tableau de bord et assistant | 5 à 8,5 | 4,37 à 8,5 | 6 210 € | 5 920 € | 6 375 € | **6 400 €** | 7 680 € | 948 € | −17,5 % ; +51,5 % |
| L5 Extension (une) | 1 à 1,5 | 0,97 à 1,5 | 1 150 € | 1 136 € | 1 125 € | **1 200 €** | 1 440 € | 960 € | −10,6 % ; +42,6 % |
| Option hôtellerie | 1,5 à 3 | 1,37 à 3 | 2 070 € | 2 008 € | 2 250 € | **2 300 €** | 2 760 € | 1 022 € | — |
| **B réduite (L0 à L2)** | **16 à 24,5** | **14,75 à 24,5** | — | — | — | **18 700 €** (15 700 € sans L0) | 22 440 € | — | — |
| **B complète (L0 à L4 + 3 × L5)** | **30 à 47,5** | **27,16 à 47,5** | — | — | — | **36 200 €** | 43 440 € | — | — |

Exemple refaisable (L2) : centrale sans IA = (9 + 13,5) ÷ 2 = 11,25 ; formule = 11,25 × 920 = 10 350 € ; plancher = 750 × 13,5 = 10 125 € ; prix = 10 400 €. € par JP centrale = 10 400 ÷ 11,25 = 924 €. Pour information, borne basse avec IA = 2,5 × 0,88 + 1 × 0,82 + 1 × 0,97 + 0,5 × 0,85 + 1 × 0,88 + 1,5 × 0,97 + 1 + 0,5 = 8,25 ; formule avec IA = (8,25 + 13,5) ÷ 2 × 920 = 10 005 € : elle aurait donné 10 200 € (encadré de 3.1). **Paiement** (STRAT:287) : 40 / 60 jusqu'à 8 JP (L0, L1, L5, option hôtellerie) ; 40 / 30 / 30 avec un jalon écrit au-delà (L2, L3, L4). Le client ne voit que des forfaits, aucun taux journalier (STRAT:133, 798).

> **Écart avec la stratégie retenue : six lots hors catalogue et un développement léger.**
> *Ce que dit la stratégie.* Huit lots, C1 à C8, au prix de la règle des lots (STRAT:287-298) ; « Aucun des onze processus ne justifie un développement spécifique » (PRO7:21) ; le développement se vend au livrable (STRAT:399) ; la gestion immobilière est exclue (STRAT:650).
> *Ce que propose cette étude [PR, cette étude].* Six lots nouveaux, L0 à L5, prix fixés par la même règle. Ils n'utilisent que des outils existants configurés (option 3) et une intégration légère après essai (option 4) (PRO7:79-85). Le développement spécifique complet (option C) est écarté. Marwin outille ; elle ne gère ni baux ni loyers.
> *Pourquoi.* Un besoin nouveau est rapporté [DR] ; la décision de GianLuca peut engager 24 000 à 72 000 € par an.
> *Limite.* JP non mesurées ; prix non validés par les associés ; un seul lot à la fois (CAP:21). R1 proposait un lot de comparaison de 2,5 à 3 JP à environ 2 700 € (R1:308-312) ; L0 y ajoute les critères de réception et les questions aux professionnels. **Risque de double facturation** (relecture) : si le logiciel est l'une des trois priorités du cadrage, celui-ci livre déjà, pour lui, « le coût actuel estimé avec lui et le seuil au-delà duquel un lot se rentabilise » (STRAT:225), et l'étape « cadrage » de la spécification compare déjà marché et construction (SPEC:604). L0 ne peut porter que sur ce que le cadrage ne fait pas (grille détaillée par module, critères de réception) ; sinon, il sort de B réduite (« Une tâche, une ligne », STRAT:382).
> *Décision.* DL5 (section 7).

### 3.6 Maintenance et hébergement

**Charge de maintenance** (corrective, sauvegardes, restauration testée chaque trimestre, mises à jour de sécurité, suivi des changements des éditeurs, support aux heures ouvrées ; hors évolutions) [ES, d'après PRO7:373-379] :

| Composant | B réduite (JP par mois) | B complète (JP par mois) | C (JP par mois) |
| --- | --- | --- | --- |
| Base commune et échéances (maintenance 0,1 à 0,25 ; restauration ≈ 0,05 à 0,125 ; support ≈ 0,02 à 0,04) | 0,17 à 0,42 | 0,17 à 0,42 | — |
| Automatismes (rappels, résumé) | 0,12 à 0,29 | 0,12 à 0,29 | — |
| Tableau de bord | 0,05 à 0,1 | 0,05 à 0,1 | — |
| Assistant (option 3 : ≈ 0,25 JP par mois, PRO7:375) | — | 0,25 | — |
| Raccordements (repère : 0,25 à 0,5 JP par mois, PRO7:375) | — | 0,25 à 0,5 | — |
| Modules construits : T 0,3 à 0,5 ; 1 : 0,1 à 0,2 ; 2 : 0,4 à 0,8 (veille réglementaire) ; 3 : 0,2 à 0,3 ; 4 : 0,15 à 0,3 ; 5 : 0,2 à 0,3 ; 6 : 0,2 à 0,4 ; 7 : 0,05 à 0,1 ; 8 : 0,5 à 1 (option 4, PRO7:375) ; 9 : 0,05 à 0,1 | — | — | 2,15 à 4 |
| **Total** | **0,34 à 0,81** | **0,84 à 1,56** | **2,15 à 4** |

**Prix mensuel par la règle** (centrale × 920 ; plancher 750 × borne haute) :

| Contrat | Formule | Plancher | **Prix proposé HT par mois** | TTC | Par an | Marge [ES] (pire ; meilleur) |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| Maintenance B réduite (plafond 0,81 JP par mois) | 529 € | 608 € | **700 €** | 840 € | 8 400 € | −2,4 % ; +65,5 % |
| Maintenance B réduite, support réaliste (plafond 1,27 JP par mois, voir ci-dessous) | 844 € | 949 € | **1 000 €** | 1 200 € | 12 000 € | −12,0 % ; +59,5 % |
| Maintenance B complète (plafond 1,56 JP par mois) | 1 104 € | 1 170 € | **1 200 €** | 1 440 € | 14 400 € | −15,1 % ; +50,3 % |

**Prix présenté au client** [PR] : **700 à 1 000 € HT par mois** après le pilote, selon le volume de support fixé au contrat, tant que DL6 n'est pas prise ; 1 200 € HT après L4. C'est ce qu'affiche la proposition client du 9 nov. (section 7).
| Maintenance C (plafond 4 JP par mois) | 2 829 € | 3 000 € | **3 000 €** | 3 600 € | 36 000 € | — |

La maintenance de C ainsi calculée vaut ≈ 29 % du prix de construction par an, au-dessus du repère du marché (15 à 25 %, R1:206), surtout à cause de la veille réglementaire et de l'assistant construit.

**Ce que cette charge oublie** (relecture contradictoire) [ES/HY] : le support y vaut 0,02 à 0,04 JP par mois, soit 8 à 17 minutes ; ce chiffre vient du poste « support et sortie » d'un simple registre sur douze mois (PRO7:379), pas d'un outil utilisé chaque jour par l'administratrice. Les « corrections et évolutions » que PRO7:376 compte à part (1 à 2,5 JP par an pour la base et le résumé) n'y sont pas, ni la sortie à blanc annuelle (SPEC:571), ni le changement de fournisseur (PRO7:378), ni le partenaire de secours payé par Marwin (4.5). Avec un support de 0,25 à 0,5 JP par mois [HY], la charge de B réduite passe à 0,57 à 1,27 JP, et la règle donne elle-même **1 000 € HT par mois** (formule 844 €, plancher 949 €). Avec le partenaire de secours au plafond (1 170 € par an), la marge du pire cas tombe à ≈ −16 % pour B réduite à 700 € et à ≈ −23 % pour B complète à 1 200 €.

**Hébergement** : Marwin **ne le vend pas**. Abonnements et hébergement sont souscrits au nom de l'entité et payés par elle, sans marge (STRAT:188-189 ; R2:342). Estimation [ES] : B réduite ≈ 83 à 351 € par mois (1 000 à 4 210 € par an) ; B complète ≈ 93 à 431 € par mois (1 120 à 5 170 € par an) ; C : 100 à 200 € par mois d'hébergement (R1:208), plus les outils. La proposition client arrondit à « environ 80 à 430 € par mois ». Ces montants comprennent les outils communs des automatisations (assistant, espace partagé, automate, consommation d'IA ; 70 à 275 € par mois, fiches détaillées, section 1.5) : le document client précise qu'ils ne s'ajoutent pas [PR].

**Contenu du contrat de maintenance borné** [PR, cette étude] : périmètre ci-dessus ; plafond de JP par mois, non reportable ; heures ouvrées, prise en compte le jour ouvré suivant ; **aucune astreinte** (STRAT:355) ; arrêt d'un automatisme possible à tout moment par l'administratrice, sans nous (SPEC:541) ; évolutions sur devis ; durée de six mois renouvelable par écrit, préavis d'un mois ; prix révisé au renouvellement sur les JP mesurées, un tiers du gain au client après un an (STRAT:420) ; contrôle trimestriel : prix ÷ JP consommées ≥ 750 € (CAT:372) ; réversibilité en 15 jours ouvrés (STRAT:560) ; limitation de responsabilité alignée sur le plafond assuré (STRAT:557). Au plus tôt au mois 7, après un pilote tenu (STRAT:339-349) ; avant, les défauts de Marwin sont corrigés gratuitement pendant 60 jours après chaque réception (STRAT:384).

> **Écart avec la stratégie retenue : maintenance sous le minimum de l'offre D.**
> *Ce que dit la stratégie.* L'exploitation D a un minimum de 1 000 à 1 500 € HT par mois, plus un prix par résultat accepté (STRAT:347) ; maintenance ≤ 0,5 JP par mois et par processus (STRAT:349).
> *Ce que propose cette étude [PR, cette étude].* Pour B réduite, 700 € HT par mois pour au plus 0,81 JP, ou 1 000 € HT pour au plus 1,27 JP avec un support réaliste, sans part variable : une maintenance de logiciel n'a pas de « résultat accepté » à compter. Le client voit la fourchette de 700 à 1 000 €. B complète (1 200 €) reste dans la fourchette de D, sans part variable non plus.
> *Pourquoi.* La règle des lots donne 608 € de plancher ; 1 000 € ferait payer 1 235 € par JP au plafond.
> *Limite.* À 700 €, la marge tombe à −2 % si 0,81 JP sont consommées au coût haut, à ≈ −16 % avec le partenaire de secours. Aligner sur 1 000 € coûterait 9 000 € de plus à GianLuca sur trois ans (30 × 300 €). Avec un support réaliste, la règle des lots donne elle-même 1 000 € (voir ci-dessus) : l'écart avec l'offre D disparaît alors.
> *Décision.* DL6 : 700 € (règle) ou 1 000 € (minimum D).

### 3.7 Marge

- **Lots** : de −15 à −18 % si la borne haute se réalise au coût haut, à +41 à +52 % si le gain de l'IA se confirme au coût bas [ES]. Au plancher, le catalogue annonçait −18 à +5 % (CAT:196) : le prix proposé ne fait guère mieux dans le pire cas ; **seul un gain réel de productivité améliore la marge**.
- **Maintenance** : −2 à +66 % (réduite à 700 €) ; −12 à +60 % (réduite à 1 000 €, support réaliste) ; −15 à +50 % (complète).
- **Dépassement** : un lot dépassé de 50 % coûte 2 000 à 2 750 € de temps non payé pour un lot de 6 000 € (STRAT:531) ; la provision de 15 % en couvre une partie.
- **Chiffre d'affaires de la première année** [ES] : B réduite 18 700 + 6 × (700 à 1 000) = **22 900 à 24 700 € HT** ; B complète 36 200 + 4 × (700 à 1 000) + 2 × 1 200 = **41 400 à 42 600 € HT**. À comparer aux ≈ 89 400 € du scénario central du modèle (AUD:138) : le logiciel en serait le quart ou la moitié, pas un revenu de plus.

### 3.8 Plafond de 10 JP facturables et autres engagements

Capacité réaliste en central : ≈ 10 JP facturables par mois, dont ≈ 3 JP de production ; un socle, deux projets actifs, **un seul lot à la fois** (CAP:17, 19, 21) ; 6,2 JP en août (FDR:445).

| Mois (central) | Travail pour GianLuca | JP par mois [ES] | Sous 10 JP ? |
| --- | --- | --- | --- |
| Nov. et déc. 2026 | Remise en ordre ; aucune production pour un bâtiment ou un lieu (D52, MAJ:374) | 0 facturable | — |
| Janv. 2027 (1) | Cadrage A (FDR:438) | 8,5 | Oui ; rien d'autre |
| Févr. 2027 (2) | L0, puis première moitié de L1 | 4,75 à 7,5 | Oui |
| Mars 2027 (3) | Fin de L1, début de L2 | 4,5 à 6,9 | Oui |
| Avr. 2027 (4) | L2 | 4,5 à 6,75 | Oui **sans socle**. Avec le socle B1 (4,5 à 6 JP) : 9 à 12,75, **non** |
| Mai 2027 (5) | Fin de L2 ; bilan ; décision | 2,25 à 3,4 | Oui |
| Juin et juil. 2027 (6-7) | L3 ; maintenance dès juillet | 3 à 5,8 | Oui ; avec B1 : 7,5 à 11,8, à la limite |
| Août 2027 (8) | Maintenance seule ; aucune livraison | 0,34 à 0,81 | Oui |
| Sept. et oct. 2027 (9-10) | L4 et maintenance | 2,8 à 5,1 | Oui ; avec B1 : 7,3 à 11,1, à la limite |
| Nov. 2027 à janv. 2028 (11-13) | Trois extensions, chacune tenue quatre semaines avant la suivante (SPEC:607) ; maintenance complète ; sortie à blanc en février 2028 | ≈ 1,8 à 3,1, plus la sortie à blanc, non chiffrée | Oui |

Calculs : L1 et L2 répartis par demi-mois (L2 sur huit semaines : 9 à 13,5 ÷ 2) ; L3 sur deux mois ; L4 sur deux mois ; trois extensions sur trois mois (3 à 4,5 ÷ 3) ; maintenance 0,34 à 0,81 puis 0,84 à 1,56 JP par mois. Correction de la relecture : la version précédente plaçait les trois extensions en deux mois, ce que la règle de quatre semaines par extension (SPEC:607) interdit.

**Conséquences** [PR, cette étude] :
1. **Le logiciel occupe la place du lot unique pendant environ douze mois** (février 2027 à janvier 2028 pour B complète). Aucun autre lot (catalogue C1, tableau des lieux C4, étude C7) ne passe en parallèle, sauf en remplaçant un lot L.
2. **Pas de socle B1 pendant le pilote L2.** Ensuite, socle et un lot L tiennent tout juste sous 10 JP.
3. **Le logiciel est la voie choisie** : les voies « ventes d'œuvres » et « pilotage » ne démarrent pas en même temps (STRAT:243, 251).
4. **La maintenance mord sur la capacité** : 0,34 à 1,56 JP par mois, chaque mois, sans fin prévue ; 3 % à 16 % du plafond.
5. **C est incompatible** avec le plafond et avec tout autre engagement (3.3).

### 3.9 Calendrier réaliste

| Date | Étape | Condition |
| --- | --- | --- |
| Dès maintenant | Aucune production, aucun chiffre donné (DL1) | D52 (MAJ:374) |
| Jeu. 19 nov. 2026 | Questions de 1.5 ajoutées au message et à l'ordre du jour | D48 ; envoi après D03, D08 et l'accord écrit (MAJ:370, 382) |
| Avant le mar. 15 déc. 2026 | Rendez-vous ; entité nommée ; proposition d'Accord transmise (ou son résumé) | Sinon report sans production (STRAT:697) |
| Janv. 2027 | Cadrage, avec le logiciel parmi les trois priorités | Acompte au plus tard le ven. 29 janv. (FDR:19) |
| Févr. et mars 2027 | L0 (si GianLuca veut la comparaison écrite), puis L1 | Bon de commande et acompte par lot |
| Mi-mars à mi-mai 2027 | L2, pilote de huit semaines sur un bâtiment et un lieu | Préalables de données réunis (SPEC:605 ; PRO7:605-616) |
| Mi-mai 2027 | Bilan du pilote, environ deux semaines après le bilan des six mois du 4 mai (FDR:442), avec une première sortie à blanc sur le bâtiment et le lieu du pilote ; décision écrite de GianLuca | Critères de la spécification tenus quatre semaines (SPEC:606) |
| Juil. 2027 (mois 7) | Maintenance, au plus tôt | Pilote tenu ; deux à trois mois de critères (STRAT:344) |
| Juin 2027 à janv. 2028 | L3, L4, puis trois extensions, un lot à la fois ; chaque extension tenue quatre semaines avant la suivante (SPEC:607) | Décision écrite à chaque lot |
| Vers févr. 2028 au plus tôt | Sortie à blanc (SPEC:571), puis mise en service générale de B complète | Extensions tenues ; sortie à blanc réussie |

**Scénario prudent** : tout glisse d'un mois (mois 1 en février 2027, FDR:55). **Ambitieux** : d'un demi-mois à un mois plus tôt. **Si GianLuca est pressé** : l'option A peut démarrer tout de suite, par son entité, et B se construit ensuite sur les mêmes outils du marché. C'est une décision « sans regret » à lui suggérer [HY].

---

## 4. Verdict sur « faire mieux et moins cher grâce à l'IA »

### 4.1 Verdict : vrai seulement contre la lecture (a)

| Partie de la phrase | Verdict | Pourquoi |
| --- | --- | --- |
| « **Moins cher** » que la lecture (a) | **Vrai**, nettement | B réduite d'un cinquième à un tiers, B complète moins de la moitié du coût sur trois ans [ES] (2.5) |
| « **Moins cher** » que la lecture (b) | **Non démontré à périmètre égal** ; vrai pour A, qui se passe de nous | B réduite : 64 à 95 % de (b) sur le prix seul, 67 à 103 % temps de l'administratrice compris, si le prix d'Accord est HT, mais pour un bâtiment et un lieu, sans finances ni assistant ; de 12 600 € de moins à 14 700 € de plus s'il est TTC ; 86 à 104 % de (b) avec le cadrage et un support réaliste. B complète : 110 à 136 % ; 115 à 141 % pour le parc supposé. C : plus cher [ES] (2.5, 2.7) |
| « **Mieux** » | **Non démontré** | Aucune réalisation livrée, adoptée et maintenue chez un client [FV négatif] (CAP:16). Seul le pilote L2, sur ses critères écrits, peut le montrer |
| « **Grâce à l'IA** » | **Faux tel quel** | Le prix est fixé par le plancher, pas par l'IA (3.5). L'économie vient de l'architecture : acheter ce qui existe, configurer au nom de l'entité, ne relier que le nécessaire. Les outils à quelques euros par mois intègrent déjà de l'IA (R1:297) |
| Si Accord vend un **service de gestion humain** | **Faux** | Marwin ne gère pas les biens d'autrui et n'assure pas d'astreinte (STRAT:650-651) ; la comparaison se fait avec un administrateur de biens (1.4) |
| Si Marwin **construit tout sur mesure** | **Faux** | C coûte autant que la lecture (a) au prix de Marwin, et ne se livre pas avant 2029 (2.4, 3.3) |

### 4.2 Conditions pour que la phrase devienne vraie

1. **L'offre d'Accord est un logiciel** (licence, plateforme, développement), pas un service de gestion humain : à établir par la proposition écrite (Q2 à Q4).
2. **Comparaison à périmètre égal**, sur la grille de la spécification (mêmes modules, mêmes données, mêmes critères de réception) (SPEC:7, 651).
3. **Marwin propose une démarche par étapes** (A avec passation, puis B réduite), pas un sur mesure complet, et ne présente jamais B réduite comme l'équivalent d'une offre qui couvrirait tout le parc (2.7).
4. **« Moins cher » ne s'écrit que chiffré, sourcé et vérifiable**, jamais en nommant Accord (section 6).
5. **« Mieux » se prouve** par le pilote L2 : critères tenus quatre semaines, aucune erreur critique, usage réel par l'administratrice, temps mesuré contre la mesure de départ, restauration et export testés (SPEC:606).
6. **Les préalables de la stratégie** sont remplis : fuite traitée, SAS immatriculée, RC professionnelle, contrat relu, entité nommée, acompte (STRAT:658-669).
7. **La capacité est réservée** : le logiciel devient la voie de l'année ; un lot à la fois ; pas de socle pendant le pilote (3.8).
8. **L'IA n'est pas vendue comme une remise** ; ses gains sont mesurés avant d'être annoncés (3.2).

### 4.3 Ce qui pourrait rendre l'offre de Marwin meilleure

Ce sont des engagements à tenir, pas des preuves [PR] : tout prestataire peut écrire les mêmes clauses. Ils ne deviennent un avantage que comparés, sur pièce, à l'autre offre (grille de 5.3).

| Atout | En pratique | Source |
| --- | --- | --- |
| **Propriété** | Comptes, données, hébergement et espace de code au nom de l'entité dès le premier jour ; code cédé au paiement complet ; composants génériques sous licence perpétuelle | STRAT:189, 287 ; SPEC:28, 573-579 |
| **Réversibilité** | Export complet lancé par l'administratrice sans nous ; restitution en 15 jours ouvrés ; sortie à blanc avant la mise en service générale | SPEC:492-496, 567-571 ; STRAT:560 |
| **Intégration** | Une seule vue pour plusieurs sociétés, bâtiments et lieux ; les logiciels du marché sont reliés, pas remplacés | SPEC:31, 67 |
| **Engagement court** | Un bon de commande par étape ; arrêt possible après chaque lot ; pas de reconduction tacite | SPEC:600 ; STRAT:184-186 |
| **Conformité intégrée** | Aucune caisse ni encaissement sur mesure ; plateforme agréée pour les factures ; calculs par formule ; règles du bail testées sur un jeu d'essai | R2:33-42 ; SPEC:56-67, 208 |
| **Proximité** | Connaissance des projets de GianLuca (pièces d'octobre 2026 [FV], connues surtout par Morgan [DR]) ; conception autour de son administratrice. Proximité géographique : lieu de résidence des associés [IN] (STRAT:233) | STRAT:25 ; SPEC:32 |
| **Mesure** | Aucun gain promis avant la mesure de départ | SPEC:35 |

### 4.4 Ce qui la rend fragile

| Fragilité | Pourquoi | Code | Source |
| --- | --- | --- | --- |
| Deux personnes | Morgan est le point de défaillance unique ; compétences de Mathys en développement, sécurité et hébergement inconnues ; sa disponibilité aussi | [FV/IN] | CAP:22, 78, 80 |
| Aucune référence | Production démontrée, livraison et maintenance non | [FV négatif] | CAP:16 |
| Maintenance dans la durée | 0,34 à 1,56 JP par mois, chaque mois, sur une capacité de 10 | [ES] | 3.6 |
| Pas d'astreinte | Heures ouvrées seulement ; acceptable parce que l'outil n'encaisse rien et que caisse, billetterie et hôtel restent chez des éditeurs | [PR] | STRAT:355 ; SPEC:62-64 |
| Responsabilité | Un calcul faux (indexation, charges) peut coûter au client ; obligation de moyens pour le pilotage, de résultat seulement pour des livrables précis | [HY] | STRAT:557 |
| Assurance | RC professionnelle non souscrite ; elle doit couvrir la conception et la maintenance de logiciels, le cyber, la perte de données, et la fuite doit être déclarée ; prix [IN] (hypothèse de modèle : 100 à 250 € par mois) | [IN] | STRAT:506, 554 |
| Société non immatriculée | Ni encaissement ni facture avant l'immatriculation ; au plus une signature « en formation » | [DR] | STRAT:33, 458, 705 |
| Historique de la fuite | Le seul outil livré, le CRM, a été exposé ; la confiance peut en souffrir | [DR] | AUD:93 ; MAJ:65 |
| Délai | Rien en service avant mi-mai 2027 ; Accord peut être plus rapide [IN] | [ES] | 3.9 |
| Dépendance à un client | 100 % du chiffre d'affaires chez GianLuca en central | [ES] | STRAT:514 |
| Fournisseurs d'IA | Hausses de prix ; Anthropic et OpenAI absents du Data Privacy Framework au 4 nov. 2026 | [MM] | PRO7:20-26 ; STRAT:532 |

### 4.5 Mesures pour couvrir ces fragilités

| Fragilité | Mesure [PR, cette étude] | Coût [ES] | Qui | Quand |
| --- | --- | --- | --- | --- |
| Deux personnes, point de défaillance unique | Suppléant nommé par brique ; test de suppléance chaque trimestre (CAP:22) ; contrôle à quatre yeux compté dans chaque lot | Compris dans les JP des lots | Mathys | Avant L1 |
| Pas de relève technique | **Partenaire de secours** : un développeur indépendant ou une petite agence de la région, choisi sur pages publiques, avec un contrat de sous-traitance prêt et l'attestation de vigilance dès 5 000 € HT cumulés (STRAT:503) ; une revue de reprise d'un à deux jours par an | 405 à 1 170 € par an (1 à 2 jours × 405 à 585 €, STRAT:399), payés par Marwin sur la maintenance ; non comptés dans les marges du tableau de 3.6 (effet : 3.6) | Mathys | Choix au 29 janv. 2027 ; revue après L2 |
| Code et savoir-faire | **Documentation** : guide d'exploitation, procédures, fiches de secours, liste des composants et de leurs licences, remis à chaque version (SPEC:542, 578) | Compris dans les lots | Mathys | Chaque lot |
| Risque de perdre les sources | **Code sur un espace au nom de l'entité** : il remplace l'entiercement pour le code propre. Pour nos composants génériques : sources déposées dans le même espace sous licence (SPEC:576-577). Entiercement chez un tiers séquestre (l'Agence pour la protection des programmes en est un [DR]) seulement si Marwin refuse ce dépôt ; prix [IN] | 0 € ; entiercement [IN] | Les deux | Avant L2 |
| Maintenance qui déborde | **Contrat de maintenance borné** (3.6) : plafond de JP, heures ouvrées, pas d'astreinte, évolutions sur devis, préavis d'un mois, révision au renouvellement | — | Morgan | Avant le mois 7 |
| Responsabilité | Limitation au plafond des honoraires des douze derniers mois, aligné sur l'assurance ; obligation de moyens ; réception sur jeu d'essai validé par l'expert-comptable et l'avocat du client (SPEC:125) | Avocat [IN] | Les deux | Avant le premier bon de commande |
| Assurance | Devis de RC professionnelle couvrant conception, configuration et maintenance de logiciels, cyber, données et IA ; fuite déclarée | [IN] ; hypothèse 1 200 à 3 000 € par an | Morgan | Avant l'immatriculation, au plus tard avant L1 |
| Société non immatriculée | Aucun lot avant l'immatriculation, le compte et l'acompte (STRAT:451-458) | — | Les deux | — |
| Délai | Proposer à GianLuca de démarrer l'option A tout de suite s'il en a besoin ; B se construit ensuite dessus | 0 € pour Marwin | Morgan | Au rendez-vous |
| Confiance après la fuite | Aucune donnée réelle avant la liste de contrôle de PRO7:605-616 ; hébergement dans l'Union ; journal ; information écrite validée par le conseil | — | Mathys | Avant L2 |

---

## 5. Recommandation

### 5.1 Option et prix

**Option recommandée : B réduite, par étapes, avec arrêt possible après chaque lot** [PR, cette étude]. L'option C est écartée. L'option A est présentée honnêtement comme la moins chère, et comme un départ possible tout de suite.

| Élément | Prix HT | TTC | Quand | Condition |
| --- | ---: | ---: | --- | --- |
| Cadrage général (inchangé) | 6 500 € | 7 800 € | Janv. 2027 | Seule proposition commerciale (STRAT:42) |
| L0 Choix des briques et comparaison écrite (facultatif) | 3 000 € | 3 600 € | Févr. 2027 | Si GianLuca veut une comparaison détaillée |
| L1 Essai sur données fictives | 5 300 € | 6 360 € | Févr.-mars 2027 | Logiciel choisi comme priorité |
| L2 Pilote sur un bâtiment et un lieu | 10 400 € | 12 480 € | Mi-mars à mi-mai 2027 | Critères de L1 tenus ; préalables de données |
| **Première étape (L1 et L2 ; avec L0)** | **15 700 € ; 18 700 €** | **18 840 € ; 22 440 €** | | |
| Maintenance après la première étape | 700 à 1 000 € par mois | 840 à 1 200 € | Dès le mois 7 | Pilote tenu ; prix fixé par DL6 |
| L3 Raccordements et finances | 7 500 € | 9 000 € | Juin-juil. 2027 | Décision écrite après le pilote |
| L4 Tableau de bord et assistant | 6 400 € | 7 680 € | Sept.-oct. 2027 | Idem |
| L5 Extension, par bâtiment ou lieu | 1 200 € | 1 440 € | Nov. 2027 à janv. 2028, une à la fois | Idem ; extension précédente tenue quatre semaines (SPEC:607) |
| Maintenance après L4 | 1 200 € par mois | 1 440 € | Dès la réception de L4 | — |
| Abonnements et hébergement | ≈ 1 000 à 5 200 € par an | — | — | Au nom de l'entité, payés par elle, sans marge |

**Coût pour GianLuca sur trois ans** : 46 300 à 68 500 € (B réduite : un bâtiment et un lieu) ; 79 000 à 97 700 € (B complète : le bâtiment et le lieu du pilote, plus trois extensions), hors cadrage et hors temps de l'administratrice [ES]. Ce sont les fourchettes de la proposition client du 9 nov. Sensibilités défavorables : 2.7. **Première année** : 22 900 à 24 700 € HT (B réduite) ; 41 400 à 42 600 € HT (B complète), hors abonnements.

### 5.2 Ordre par rapport au cadrage

1. **Maintenant et jusqu'au 19 nov. 2026** : aucune contre-offre, aucun chiffre, aucune production (DL1, D52). Décisions de la section 7.
2. **Après D03, D08 et l'accord écrit des associés** : les questions de 1.5 partent avec le message de recadrage et l'ordre du jour (D48, D14). La première porte sur la confidentialité.
3. **Au rendez-vous, avant le 15 déc. 2026** : le cadrage reste la seule proposition. Le logiciel peut être **l'une des trois priorités**. Le cadrage compare déjà les suites, y compris « un autre prestataire » (PROP9:41, 49) : c'est le bon cadre, sans nommer personne. Si GianLuca est pressé, lui dire que l'option A peut démarrer tout de suite.
4. **Le logiciel peut-il être le pilote choisi ?** Oui, dans la **voie (c) « organisation interne »**, adaptée : sa personne désignée existe peut-être déjà, l'administratrice (MAJ:79). **Lot du catalogue le plus proche : C6 « outillage et passation »** (STRAT:321-337), dont D50 adapte déjà le contenu (MAJ:84-89). Le pilote logiciel est L1 puis L2 ; C4 (tableau des lieux et de leurs obligations) reste un lot séparé, utile avant les extensions (R3:193).
5. **Au bilan, vers mi-mai 2027** : trois issues écrites. Arrêt (GianLuca garde ses comptes et ses données). B réduite seule, avec maintenance. Suite vers B complète, un lot à la fois.

> **Écart avec la stratégie retenue : le pilote logiciel coûte plus que la voie (c).**
> *Ce que dit la stratégie.* Après le cadrage, une voie à la fois, un pilote de huit semaines au plus (STRAT:243) ; voie (c) : C6 à 7 500 € HT pour 8 à 9 JP (STRAT:249, 333) ; les trois voies coûtent 6 000 à 13 400 € HT (CAT:79-81).
> *Ce que propose cette étude [PR, cette étude].* Un pilote logiciel en deux lots, L1 (essai sur données fictives) puis L2 (huit semaines sur un bâtiment et un lieu), 15 700 € HT pour 13,5 à 20,5 JP ; 18 700 € avec L0. Variante plus courte : C6 tel quel, à 7 500 €, sans fiches de patrimoine ni configuration des logiciels du marché ; le logiciel commencerait alors après.
> *Pourquoi.* Choisir la gestion locative du marché demande l'essai sur vingt baux (SPEC:208) ; le pilote doit tester le vrai besoin (fiche du bâtiment, échéances, baux) ; la décision en jeu vaut 24 000 à 72 000 € par an.
> *Limite.* Exposition avant décision deux fois plus forte que la voie (c) ; L1 et L2 ne tiennent pas dans les huit semaines ensemble ; aucune autre voie en parallèle.
> *Décision.* DL7.

### 5.3 Comment en parler à GianLuca sans dénigrer Accord

**Principes** [PR] :
- Ne jamais prononcer ni écrire le nom d'Accord ; ne jamais commenter son offre, ni à l'oral ni à l'écrit (section 6).
- Parler de « toute offre », « un autre prestataire », « chaque façon de faire ».
- Présenter **trois façons de faire** (marché seul, marché relié, sur mesure) avec leurs coûts sourcés, dont la moins chère, qui ne passe pas par nous.
- Remettre **la même grille** pour toutes les offres, nous compris. GianLuca ou son administratrice remplit la colonne de l'autre offre à partir de sa proposition écrite ; nous remplissons la nôtre, avec nos preuves.
- Rappeler que la spécification sert justement à comparer « quel que soit le prestataire » (SPEC:7, 651).

**Grille de comparaison neutre** (à remplir seulement à partir de pièces écrites) :

| Critère | Question posée à chaque offre | Preuve attendue | Offre 1 | Offre 2 | Marwin Tech |
| --- | --- | --- | --- | --- | --- |
| Périmètre | Quels modules de la spécification, pour quels bâtiments, lieux et utilisateurs ? | Liste écrite, module par module | | | |
| Nature | Licence, développement, service de gestion, maintenance ? | Lignes du devis | | | |
| Coût sur trois ans | Mise en place, abonnements, hébergement, maintenance, évolutions ; HT et TTC | Devis daté | | | |
| Temps de votre administratrice | Combien de jours pour démarrer, puis par mois ? | Estimation écrite, puis mesure au pilote | | | |
| Engagement | Durée, préavis, reconduction, frais de sortie, location financière ? | Conditions générales | | | |
| Propriété des données | À qui ? Export complet par vous, sans demande ? Format, délai ? | Clause et essai d'export | | | |
| Propriété du code | Cession ? Sources remises ? | Clause | | | |
| Hébergement | Où ? Quels sous-traitants ? Contrat de sous-traitance des données ? | Liste et contrat | | | |
| Niveau de service | Heures, délais de prise en charge et de rétablissement, pénalités | Clause | | | |
| Conformité | Plateforme agréée ; règles du bail de mai 2026 ; caisse certifiée ; carte professionnelle s'il encaisse | Attestations | | | |
| IA | Laquelle, où, quelles données, quelle mention ? | Description écrite | | | |
| Réception | Critères écrits avant le travail ; jeu d'essai | Liste des critères | | | |
| Continuité | Que se passe-t-il si le prestataire disparaît ? | Plan écrit, documentation | | | |
| Références et assurance | Clients comparables ; attestation d'assurance | Pièces | | | |

**À dire** : « Voici ce que coûte, sur trois ans, chaque façon de faire, à périmètre égal. » ; « Voici les questions à poser à tout prestataire, nous compris. » ; « Vous pouvez commencer tout de suite avec des logiciels du marché ; nous pouvons les relier ensuite. » ; « Nous ne promettons aucun gain avant de l'avoir mesuré avec votre administratrice. »
**À ne pas dire** : un jugement sur une autre offre (« trop cher », « inutile », « dépassé ») ; « nous faisons mieux » ; « l'IA divise les coûts » ; un pourcentage d'économie qui ne sort pas d'un calcul remis par écrit ; tout conseil de rompre un contrat déjà signé.

---

## 6. Risques juridiques de la comparaison et confidentialité

### 6.1 Publicité comparative

- **Règle** [FV] (C. conso., L122-1, L122-2, L122-5, en vigueur au 9 nov. 2026) : une publicité qui compare des biens ou services en identifiant, même implicitement, un concurrent n'est licite que si elle n'est pas trompeuse, porte sur des biens ou services qui répondent aux mêmes besoins, et compare objectivement des caractéristiques essentielles, pertinentes, vérifiables et représentatives, dont le prix. Elle ne doit ni dénigrer, ni créer de confusion, ni tirer indûment profit de la notoriété d'un nom. L'annonceur doit pouvoir prouver rapidement l'exactitude de ce qu'il affirme.
- **Pour nous** [HY, à trancher par l'avocat] : un document remis à un seul client peut être qualifié de publicité. Prudence : le traiter comme tel. Une comparaison « implicite » suffit : « une offre à 6 000 € par mois » désigne Accord pour GianLuca.

### 6.2 Dénigrement

- **Règle** [FV, texte de l'arrêt lu] : « même en l'absence d'une situation de concurrence directe et effective », la divulgation d'une information de nature à jeter le discrédit sur un produit d'autrui est un dénigrement, sauf si elle « se rapporte à un sujet d'intérêt général et repose sur une base factuelle suffisante », exprimée « avec une certaine mesure » (Cass. com., 4 mars 2020, n° 18-15.651, au visa des articles 1240 du code civil et 873 du code de procédure civile ; principe déjà posé par Cass. com., 9 janv. 2019, n° 17-18.350 [DR]).
- **Pour nous** [HY] : une comparaison remise à un client n'est pas un sujet d'intérêt général. Une critique exacte peut donc être fautive. L'arrêt de 2019 portait justement sur une information adressée aux clients d'une entreprise (une action en contrefaçon encore pendante) [DR, sources secondaires] : un public restreint ne protège pas. Un arrêt de 2026 exigerait une condition de publicité [DR, source secondaire non lue, à ne pas utiliser sans l'avocat].

### 6.3 Pratique commerciale trompeuse

- **Règle** [FV, repéré] : les pratiques trompeuses (C. conso., L121-2 à L121-4) visent aussi les pratiques dirigées vers des professionnels (L121-5 ; version en vigueur à relire).
- **Pour nous** : « moins cher grâce à l'IA » ou « mieux » sans preuve serait trompeur. Seuls des chiffres calculés, datés et sourcés peuvent être écrits ; chaque fourchette garde ses hypothèses (2.5).

### 6.4 Secret des affaires et confidentialité de la proposition d'Accord

- **Règle** [FV, textes lus, en vigueur au 9 nov. 2026] : une information est protégée si elle n'est pas aisément accessible, a une valeur commerciale du fait de son secret et fait l'objet de mesures raisonnables de protection (C. com., L151-1). Son utilisation ou sa divulgation est illicite si elle se fait sans le consentement de son détenteur par une personne qui viole une obligation de ne pas la divulguer ou d'en limiter l'usage (L151-5). **Celui qui la reçoit est aussi en faute s'il savait, ou aurait dû savoir au regard des circonstances, qu'elle venait d'une personne qui la divulguait illicitement** (L151-6).
- **Pour nous** [HY] : une proposition commerciale avec ses prix, son périmètre et sa méthode peut être un secret des affaires, surtout si elle porte une mention de confidentialité. Si GianLuca nous la montre en violant une clause, nous pourrions être en faute en l'utilisant, par exemple pour caler nos prix ou reprendre sa structure.

### 6.5 Autres risques

- **Contrat déjà signé** [HY] : inciter GianLuca à rompre un contrat signé avec Accord pourrait engager notre responsabilité. Si Q13 répond « signé », seule une sortie prévue au contrat, vue avec son avocat, est envisageable.
- **Droit d'auteur** [HY] : le texte et la mise en forme de la proposition peuvent être protégés ; ne rien recopier.
- **Données personnelles** : la proposition peut nommer des personnes de chez Accord ; ne pas la conserver au-delà du besoin.
- **Usage de l'IA** : ne pas soumettre la proposition à un assistant d'IA, sauf offre professionnelle sans entraînement et accord exprès de GianLuca (PRO7:26).

### 6.6 Règles pratiques [PR, cette étude]

1. **Fixer nos prix avant de lire quoi que ce soit** (DL5, 26 nov. 2026) : personne ne pourra dire que nous les avons calés sur un secret.
2. **Demander d'abord si la proposition est confidentielle** (Q1). Si oui : ne pas la recevoir ; GianLuca nous dit lui-même ce qu'il veut (périmètre, prix, durée), ou la fait relire par son avocat.
3. **Si elle ne l'est pas** : la recevoir par écrit, de lui ; la ranger dans un dossier lisible par les deux associés seulement ; noter au registre la date de réception.
4. **N'en tirer que les faits utiles à sa décision** (colonnes de la grille 5.3) ; ne reprendre ni sa structure, ni ses textes, ni ses prix dans nos documents, ni pour d'autres clients.
5. **Ne jamais la transmettre** à un tiers ni à une IA grand public ; ne jamais la citer dans un document.
6. **La supprimer** après la décision de GianLuca, ou à sa demande ; noter la date au registre.
7. **Aucun document qui nomme ou compare Accord** ; tout document comparatif est relu par l'avocat avant envoi (DL9).

---

## 7. Décisions à prendre par Morgan et Mathys

Numérotées DL1 à DL13 pour éviter tout conflit avec le registre de l'audit (D45 à D55, MAJ:374-384) ; à y inscrire avec DL12.

| N° | Décision [PR, cette étude] | Responsable | Date limite | Attend |
| --- | --- | --- | --- | --- |
| DL1 | Aucune contre-offre, aucun chiffre donné à GianLuca sur ce logiciel, aucune production, avant sa proposition écrite (ou son résumé) et avant D03 et D08 (prolonge D52) | Les deux | Immédiate (lun. 9 nov. 2026) | — |
| DL2 | Adopter les règles de réception de la proposition d'Accord (6.6) | Les deux ; avocat si clause de confidentialité | Jeu. 19 nov. 2026 | — |
| DL3 | Ajouter les questions Q1 à Q15 au message et à l'ordre du jour, Q1 en premier | Morgan ; contrôle par Mathys | Jeu. 19 nov. 2026 (texte) ; envoi avec D14 | D03, D08, accord écrit (MAJ:370) |
| DL4 | Retenir la position : option B réduite par étapes ; C écartée ; A présentée comme la moins chère ; pas de « moins cher grâce à l'IA » dans un écrit | Les deux, par écrit | Jeu. 19 nov. 2026 | — |
| DL5 | Valider les lots L0 à L5 hors catalogue, leurs prix et la règle « plus grande valeur entre JP centrales sans IA × 920 € et 750 € × borne haute » ; confirmer le retour à la règle de la stratégie fait à la mise en cohérence (encadré de 3.1 : L2 à 10 400 €, et non 10 200 €) ; fixer la frontière entre L0 et le cadrage (3.5) | Les deux, par écrit | Jeu. 26 nov. 2026 | DL4 |
| DL6 | Prix de la maintenance après la première étape : 700 € (règle, support de 8 à 17 minutes par mois) ou 1 000 € (minimum de D, et prix de la règle avec un support réaliste) ; d'ici là, la proposition client affiche 700 à 1 000 € ; contenu du contrat borné (3.6) | Les deux | Jeu. 26 nov. 2026 | DL5 |
| DL7 | Le logiciel comme priorité possible du cadrage et comme pilote dans la voie (c) adaptée (L1 puis L2), ou C6 tel quel à 7 500 € ; pas de socle pendant L2 (5.2) | Les deux | Jeu. 19 nov. 2026, avec D51 | — |
| DL8 | Mathys écrit ses compétences (développement, sécurité, hébergement) et sa disponibilité pour L1 à L4 et la maintenance ; suppléant nommé par brique | Mathys | Jeu. 19 nov. 2026, avec D11 | — |
| DL9 | Interdire toute comparaison écrite qui nomme ou vise un concurrent ; tout document comparatif relu par l'avocat | Les deux | Jeu. 19 nov. 2026 | — |
| DL10 | Demander des devis de RC professionnelle couvrant conception, configuration et maintenance de logiciels, cyber, données et IA, fuite déclarée | Morgan | Avant l'immatriculation ; au plus tard avant L1 | D03 |
| DL11 | Choisir un partenaire de secours sur pages publiques et préparer le contrat de sous-traitance (4.5) | Mathys | Ven. 29 janv. 2027 | DL8 |
| DL12 | Inscrire au registre les décisions DL1 à DL13 et les risques de 4.4 (délai face à un concurrent plus rapide ; maintenance qui déborde ; confidentialité ; responsabilité des calculs) | Morgan tient ; Mathys contrôle | Jeu. 26 nov. 2026 | D53 |
| DL13 | Refaire les chiffres des sections 1.2 et 2.5 dès réception de la proposition (ou de son résumé) ; fixer avec GianLuca les critères d'arrêt du pilote | Les deux | À réception ; au plus tard au rendez-vous (mar. 15 déc. 2026) | DL2, DL3 |

---

## 8. Mise en cohérence du 9 novembre (soir)

Les cinq livrables du dossier (cette étude, la proposition, l'annexe de spécification, les fiches d'automatisation, la méthode et les garanties) et les trois travaux R1 à R3 ont été comparés entre eux, avec la stratégie retenue et avec la présentation du 9 nov. (PIA, lue sans modification). Corrections faites [MM] :

| Incohérence | Correction | Fichiers |
| --- | --- | --- |
| L2 à 10 200 € ici (formule avec IA), à 10 400 € dans la proposition client | Règle de la stratégie (JP sans IA) : L2 10 400 € ; première étape 15 700 € sans L0, 18 700 € avec ; B complète 36 200 € ; tableaux 2.3, 2.5, 2.7, 3.5, 3.7, 4.1, 5.1 et annexe A refaits par script | Cette étude |
| Maintenance après le pilote : 700 € ici, 700 à 1 000 € dans la proposition | Fourchette de 700 à 1 000 € jusqu'à DL6 ; trois ans : 46 300 à 68 500 € (B réduite) et 79 000 à 97 700 € (B complète), comme la proposition | Cette étude |
| B complète « quatre bâtiments ou lieux » ici, « pilote plus trois bâtiments ou lieux » dans la proposition | Cinq : le bâtiment et le lieu du pilote, plus trois extensions ; ligne « périmètre égal » de 2.7 refaite avec trois extensions de plus | Cette étude ; proposition (« trois extensions ») |
| Étapes numérotées 0 à 4 (proposition), 1 à 4 (spécification), 1 à 6 (méthode) | Numérotation de la spécification partout : 1. cadrage et choix des logiciels (1a et 1b dans la proposition) ; 2. maquette et essai sur données fictives (vingt baux) ; 3. pilote sur un bâtiment et un lieu ; 4. mise en service progressive. La méthode dit comment ses six temps s'y répartissent | Proposition, section 5 ; spécification, sections 1.4 et 7 ; méthode, sections 2 et 8 |
| Abonnements et hébergement « 85 à 435 € par mois » (proposition) contre 83 à 431 € ici ; outils communs des fiches (70 à 275 €) comptables deux fois | « Environ 80 à 430 € », outils communs des automatisations compris et non additionnés | Proposition, section 7 ; fiches, section 1.6 ; cette étude, 3.6 |
| Liste « jamais automatique » plus courte dans la spécification que dans les fiches | Ajout de « une publication, une commande » ; renvoi aux mêmes trois niveaux dans les fiches et la présentation | Spécification, section 1.5 |
| Gestion locative « à décider au cadrage » (spécification, méthode), mais essayée sur vingt baux à l'étape 2 (proposition) | « Décidée au cadrage, confirmée par l'essai sur vingt baux fictifs de l'étape 2 » | Spécification, 1.4 ; méthode, section 8 |
| Paiement des automatisations : 40 / 60 seulement | 40 / 60 sous huit jours ; 40 / 30 / 30 au-delà de huit jours de travail estimés (STRAT:287) | Fiches, section 1.5 |
| Sens (1) et (3) rattachés aux modules 5, 6 et 8 autrement que dans la spécification | Rattachement de SPEC:21-24 : 5, 6 et 8 communs aux trois sens | Cette étude, 1.3 |
| Spécification : prix « dans une proposition séparée, si vous en demandez une » | Renvoi nommé à la proposition du 9 nov. | Spécification, ligne 7 |
| Travaux R1 à R3 : six modules (R1, R2) ou M0 à M6 (R3) au lieu des neuf modules de la spécification ; lot de comparaison à ≈ 2 700 € (R1) | Note de correspondance ajoutée à la fin de chaque travail, sans changer ses numéros de ligne ; L0 à 3 000 € fait foi | R1, R2, R3 |
| Sortie à blanc placée seulement « avant la mise en service générale » (vers février 2028), alors que la stratégie la veut parmi les livrables des six mois (STRAT:169) et que R2 la plaçait avant le bilan de mai 2027 | Première sortie à blanc à la fin du pilote, sur son bâtiment et son lieu ; puis avant la mise en service générale ; puis chaque année | Spécification, 5.7 et 7 ; proposition, sections 5 et 6 ; méthode, section 7 ; cette étude, 3.9 |

**Contrôles automatiques faits après correction** [MM] : aucune occurrence de l'ancien prénom erroné dans le dossier ; aucun chemin local de machine ; dans les quatre documents de `pour-carlone/logiciels-et-automatisations/` (spécification comprise) et leur README, aucune occurrence du nom du concurrent, d'un code [FV] à [IN], de « JP », « voie », « socle », plancher, marge, rémunération ou « 1,5 M ». La spécification garde ses 693 lignes : les renvois SPEC:… de cette étude restent justes. Le script de l'annexe A redonne L0 à L5.

**Cohérence avec la présentation** [FV, PIA lue le 9 nov.] : douze domaines (`domaines`) ; trois niveaux « automatique, assistée, préparée » (`modes`), repris sous les noms « automatique après essai, assistée, préparée pour signature » ; 47 aides sur six pages (`cat-admin` 8, `cat-batiments` 7, `cat-galerie` 8, `cat-cabaret` 8, `cat-finance` 8, `cat-marketing` 8), dont 7 automatiques, 30 assistées et 10 préparées : le tableau de la section 3 des fiches les reprend une à une avec le même niveau. « Trois tâches à essayer au plus » (`premier-pas`) = fiches, section 4. « Pilote de huit semaines » (`etapes`) = proposition, étape 3. Rien dans le dossier ne contredit `logiciels` (marché, liaisons légères, sur mesure après essai).

> **Écart avec la stratégie retenue : prix indicatifs des automatisations.**
> *Ce que dit la stratégie.* Lots C de 3 à 9 JP, prix = JP × 800 € + 10 à 15 %, plancher de 750 € × borne haute (STRAT:201, 287 ; CAT:71).
> *Ce que montrent les fiches* [FV, fiches détaillées, section 2.0]. Quinze mises en place de 1 400 à 6 500 € HT, soit ≈ 1,5 à 7 JP au prix cible de 920 € [ES, déduit ici] ; six fiches (3, 4, 7, 9, 10, 15) ont une borne basse sous 2 250 € (3 × 750), donc des lots plus petits que le catalogue ; extension à ≈ 1 200 € par bâtiment, comme L5.
> *Pourquoi c'est acceptable* [PR, cette étude]. Ce sont des fourchettes « indicatives, données avant le cadrage » ; le prix ferme de chaque bon de commande suit la règle de 3.1 (la plus grande valeur entre JP centrales sans IA × 920 € et 750 € × borne haute).
> *Limite.* Les JP par fiche ne sont écrites nulle part en interne ; une fiche commandée seule à moins de 3 JP reste sous le format des lots C.
> *Décision.* À joindre à DL5 : JP par fiche écrites et contrôlées avant tout envoi des fiches.

> **Écart avec la stratégie retenue : bilan du pilote logiciel après le jalon des six mois.**
> *Ce que dit la stratégie.* Au 4 mai 2027 : « Pilote de 8 semaines terminé dans la voie choisie ; bilan mesuré remis à GianLuca ; exercice de sortie à blanc » (STRAT:169).
> *Ce que prévoit le dossier* [PR, cette étude]. Si le logiciel est la voie choisie, L1 puis L2 mènent le bilan du pilote vers la mi-mai 2027 (3.9), environ deux semaines après le 4 mai, sortie à blanc du pilote comprise.
> *Pourquoi.* L1 (essai sur vingt baux) précède le pilote de huit semaines ; les deux ne tiennent pas avant le 4 mai si le cadrage est payé en janvier.
> *Limite.* Le bilan des six mois se fait le 4 mai sur un pilote non terminé ; dans le scénario prudent, tout glisse d'un mois.
> *Décision.* Avec DL7 : accepter ce décalage, ou réduire L1 pour finir L2 avant le 4 mai.

---

## Limites

- **L'offre d'Accord n'est connue que par quelques mots rapportés** [DR] ; son identité, sa nature et son prix réel sont [IN]. Toutes les comparaisons de la section 2 sont à refaire sur pièce (DL13).
- **Les comparaisons de 2.5 opposent des périmètres différents** : B réduite couvre un bâtiment et un lieu ; l'étendue de l'offre d'Accord est [IN]. Les sensibilités de 2.7 montrent que l'avantage contre la lecture (b) ne résiste pas à des hypothèses moins favorables.
- **Les JP sont des estimations** [ES], jamais mesurées chez Marwin pour un logiciel livré ; les parts `s` et le gain de 0 à 30 % sont des hypothèses [HY].
- **Le temps de l'administratrice** repose sur des hypothèses de jours et sur un coût par jour tiré de repères généraux ; son statut est [IN].
- **Les prix du marché** viennent de pages d'éditeurs et de comparatifs lus le 9 nov. 2026 (R1) ; aucun n'est confirmé par un devis. La plateforme agréée et l'assurance sont [IN].
- **Les points juridiques marqués [HY]** (qualification de publicité, dénigrement par une communication privée, secret des affaires d'une proposition, incitation à rompre) sont à soumettre à l'avocat. Les textes ont été lus sur Légifrance ; la jurisprudence n'a pas été recherchée au-delà de deux arrêts.
- **La présentation du 9 nov.** a été modifiée après la note de mise à jour (R3:45) ; cette étude ne s'appuie sur elle que pour la vue `logiciels`, lue le 9 nov.
- **Aucune action** : ni contact, ni compte, ni dépense, ni modification d'un fichier existant.

---

## Sources web consultées

Toutes lues le **9 novembre 2026**.

| Source | Adresse | Lecture |
| --- | --- | --- |
| Code de la consommation, L122-1 à L122-7 (publicité comparative), version en vigueur au 9 nov. 2026 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221021/ | Lue (L122-1, L122-2, L122-5) |
| Code de commerce, L151-1 à L151-9 (secret des affaires), version en vigueur au 9 nov. 2026 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000005634379/LEGISCTA000037266549/ | Lue (L151-1, L151-5, L151-6) |
| Code de la consommation, L121-5 (pratiques trompeuses visant des professionnels) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032227291 | Repérée (extrait de recherche) ; version en vigueur à relire |
| Cass. com., 4 mars 2020, n° 18-15.651 (dénigrement) | https://www.dalloz-actualite.fr/document/com-4-mars-2020-fs-pb-n-18-15651 | Lue (texte de l'arrêt, attendu de principe) ; relue à la relecture contradictoire : arrêt n° 225, visa des articles 1240 du code civil et 873 du code de procédure civile |
| Cass. com., 9 janv. 2019, n° 17-18.350 (dénigrement) | https://www.dalloz-actualite.fr/document/com-9-janv-2019-fs-pb-n-17-18350 | Repérée [DR] ; objet confirmé à la relecture par des commentaires (https://cms.law/fr/FRA/Publication/Denigrement-fautif) [DR] |
| Agence pour la protection des programmes (tiers séquestre) | https://www.app.asso.fr/ | Repérée [DR] ; aucun tarif lu |
| Code de commerce, L151-1, L151-5, L151-6 (relecture) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000005634379/LEGISCTA000037266549/ | Relus : en vigueur depuis le 1er août 2018 (loi n° 2018-670) ; contenu conforme à 6.4 |
| METR, mise à jour du 24 févr. 2026 (relecture) | https://metr.org/blog/2026-02-24-uplift-update/ | Lue : −18 % (−38 à +9 %) pour les anciens participants, −4 % (−15 à +9 %) pour les nouveaux ; « unreliable signal » ; biais probable vers un gain sous-estimé. Conforme à R1:325 |
| Loi n° 2026-403 du 26 mai 2026, baux commerciaux (relecture) | https://www.notaires.fr/fr/actualites/baux-commerciaux-les-nouveautes-de-la-loi-ndeg-2026-403-du-26-mai-2026-de-simplification-de-la-vie-economique-sve | Repérée (résultats de recherche) : existence et objet conformes à R2:36 ; date d'effet du 26 ou du 28 mai selon les sources [DR] |

Les autres sources (prix des éditeurs, barèmes, études sur l'IA, textes sur la facturation électronique, le bail commercial, la caisse et la billetterie) sont celles de R1 et R2, lues le 9 nov. 2026, citées par leur ligne.

---

## Annexe A : calculs refaisables

Formules (section 3.1, après la mise en cohérence du 9 nov.) : `bas_IA = Σ bas × (1 − 0,30 × s)` ; `centrale = (bas + haut) ÷ 2` (sans IA) ; `formule = centrale × 800 × 1,15` ; `plancher = 750 × haut` ; `prix = arrondi à la centaine supérieure de max(formule, plancher)` ; `marge pire = (prix − haut × 885) ÷ prix` ; `marge meilleure = (prix − bas_IA × 710) ÷ prix`.

```python
import math
def lot(taches):                      # taches : liste de (bas, haut, s)
    bas = sum(b for b, h, s in taches); haut = sum(h for b, h, s in taches)
    bas_ia = sum(b * (1 - 0.30 * s) for b, h, s in taches)
    centrale = (bas + haut) / 2          # JP sans IA (STRAT:287, 418)
    prix = math.ceil(max(centrale * 920, 750 * haut) / 100) * 100
    return bas, haut, round(bas_ia, 2), prix, round((prix - haut * 885) / prix, 3), round((prix - bas_ia * 710) / prix, 3)
L0 = [(0.5, 0.5, 0), (1, 1.5, 0), (0.5, 1, 0), (0.5, 1, 0)]
L1 = [(2, 3, .6), (1.5, 2.5, .2), (.5, 1, .3), (.5, .5, 0)]
L2 = [(2.5, 3.5, .4), (1, 1.5, .6), (1, 1.5, .1), (.5, 1, .5), (1, 1.5, .4), (1.5, 2, .1), (1, 1.5, 0), (.5, 1, 0)]
L3 = [(1, 2, .6), (1, 2, .6), (1, 1.5, .6), (2, 3, .5), (1, 1.5, .1)]
L4 = [(1.5, 2.5, .6), (1, 2, .6), (2, 3.5, .3), (.5, .5, 0)]
L5 = [(1, 1.5, .1)]
for nom, t in [("L0", L0), ("L1", L1), ("L2", L2), ("L3", L3), ("L4", L4), ("L5", L5)]:
    print(nom, lot(t))
```

Résultat attendu : L0 3 000 € ; L1 5 300 € ; L2 10 400 € ; L3 7 500 € ; L4 6 400 € ; L5 1 200 € (vérifié par exécution le 9 nov. 2026 [MM]).

Autres calculs :
- **C** : sous-total sans IA 86 à 146 JP ; coordination 15 % = 12,9 à 21,9 ; total 98,9 à 167,9 ; avec IA, borne basse 73,34 + 12,9 = 86,24 ; centrale 127,07 ; formule 116 904 € ; plancher 125 925 € ; prix 126 000 €. Délai : 98,9 ÷ 4 = 24,7 mois ; 167,9 ÷ 4 = 42 mois.
- **Maintenance** : B réduite 0,17 + 0,12 + 0,05 = 0,34 à 0,42 + 0,29 + 0,10 = 0,81 ; centrale 0,575 × 920 = 529 € ; plancher 750 × 0,81 = 607,5 € ; prix 700 €. B complète : 0,84 à 1,56 ; 1,2 × 920 = 1 104 € ; plancher 1 170 € ; prix 1 200 €. C : 2,15 à 4 ; 3,075 × 920 = 2 829 € ; plancher 3 000 €.
- **Coût sur trois ans** : A = (0 à 5 000) + 3 × (760 à 3 010) ; B réduite = 18 700 + 3 × (1 000 à 4 210) + 30 × (700 à 1 000) + (4 à 8) × 900 = 46 300 à 68 530 ; B complète = 36 200 + 3 × (1 120 à 5 170) + (4 × (700 à 1 000) + 26 × 1 200) + (6 à 12) × 900 = 78 960 à 97 710 ; C marché = (98,9 × 405 à 167,9 × 900) + (760 + 3 × 120 à 3 010 + 3 × 960) + 3 × (1 200 à 2 400) + 2 × (15 % × 40 054 à 25 % × 151 110) ; C Marwin = 126 000 + (1 120 à 5 890) + (3 600 à 7 200) + 24 × 3 000.
- **Temps de l'administratrice** : (mise en place + 36 × récurrent) jours × 125 € (borne basse) à × 342 € (borne haute) ; 2 249 ÷ 18 ≈ 125 ; 6 149 ÷ 18 ≈ 342.
- **Parts** (2.5) : coût de l'option ÷ coût d'Accord, borne basse sur borne basse, borne haute sur borne haute ; Accord avec temps de l'administratrice = prix + 3 000 à 15 732 €.
- **Sensibilités** (2.7, refaites à la mise en cohérence) : cadrage 46 300 + 6 500 = 52 800 à 68 530 + 6 500 = 75 030 ; support réaliste : charge 0,1 + 0,05 + 0,25 + 0,12 + 0,05 = 0,57 à 0,25 + 0,125 + 0,5 + 0,29 + 0,1 = 1,265 JP, formule 0,9175 × 920 = 844 €, plancher 750 × 1,265 = 949 €, prix 1 000 €, borne basse + 30 × 300 = 9 000 €, soit 55 300 à 68 530 € ; ensemble 61 800 à 75 030 € ; temps comme en A : (6 + 36 × 1) = 42 à (10 + 36 × 3) = 118 jours, 42 × 125 = 5 250 à 118 × 342 = 40 356 €, soit 51 550 à 108 886 € ; bornes croisées : 68 530 + 64 × 342 = 90 418 contre 72 000 + 24 × 342 = 80 208 ; ensemble avec temps : 61 800 + 5 250 = 67 050 à 75 030 + 40 356 = 115 386 ; périmètre égal : 78 960 + 3 600 = 82 560 à 97 710 + 3 600 = 101 310 ; briques communes : 46 300 + 10 300 = 56 600 à 68 530 + 37 000 = 105 530 ; TVA non récupérée : 46 300 × 1,2 = 55 560 à 68 530 × 1,2 = 82 236.
- **IA et prix de L2** : formule sans IA = 11,25 × 920 = 10 350 € → 10 400 € (prix retenu) ; avec IA 10 005 € et plancher 10 125 € → 10 200 € (ancienne version). **Ralentissement** : Σ (haut × s) = 2,6 (L1) + 3,75 (L2) ; × 0,19 = 1,21 JP ; 24,5 + 1,21 = 25,7 JP ; marge pire (18 700 − 25,7 × 885) ÷ 18 700 = −22 % (−16 % sans ralentissement).
- **Maintenance avec partenaire de secours** : (8 400 − 0,81 × 885 × 12 − 1 170) ÷ 8 400 = −16 % ; (14 400 − 1,56 × 885 × 12 − 1 170) ÷ 14 400 = −23 %.

Contrôles faits le 9 nov. 2026 [MM] : calculs des sections 2 et 3 refaits par script, résultats reportés ci-dessus, puis refaits à la mise en cohérence (section 8) ; textes de L122-1, L122-2, L122-5, L151-1, L151-5, L151-6 et de l'arrêt du 4 mars 2020 lus ; aucune occurrence de l'ancien prénom erroné du client ; aucun chemin local de machine ; aucun contact, aucun compte, aucune dépense.

Relecture contradictoire : 231 vérifications, 35 corrections — 9 novembre 2026
Mise en cohérence du dossier : 12 incohérences corrigées (section 8) — 9 novembre 2026
