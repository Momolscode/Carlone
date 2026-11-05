# Modèle économique et plan de trésorerie

Audit Marwin Tech × GianLuca Carlone · livrable 9 sur 15 · 4 novembre 2026
Statut : interne (contient rémunérations, coûts et marges ; ne pas transmettre à GianLuca Carlone)
Sources principales : `modele-financier/modele_financier.py` et ses sorties `modele-financier/scenarios.md`, `modele-financier/tresorerie-18-mois.md`, `modele-financier/tresorerie-18-mois.csv`, `modele-financier/stress-tests.md`, `modele-financier/structures.md` ; `travaux/controle-modele.md` ; `travaux/strategie-retenue.md` (sections 4.9 à 4.13, 5 et 6) ; `travaux/syn-droit.md` (section 1, SAS ou SARL) ; `travaux/rj-R1-structures.md` ; pièces d'origine du dépôt Momolscode/Carlone (commit 7b46602), rouvertes en lecture seule le 4 nov. 2026.
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu. Sans autre précision, une [PR] est une proposition de la stratégie retenue ; « [ES, ce livrable] » signale un calcul fait ici à partir des sorties du modèle.

Conventions. **JP** : journée-personne de 7 h ; deux personnes présentes une journée consomment 2 JP. **Mois 1** : premier mois facturé (janvier 2027 dans le scénario central [HY]). **HT / TTC** : TVA de 20 % ; TTC = HT × 1,2. **Trésorerie disponible** = trésorerie en banque moins la TVA collectée pas encore reversée. **Trésorerie libre** = disponible moins la réserve de 10 % et l'IS à provisionner (`modele-financier/tresorerie-18-mois.md:117`). Les codes d'offres (A cadrage, B0 socle pilote, B1 et B2 socles récurrents, C lots, D exploitation, E avenant) sont ceux de `travaux/strategie-retenue.md:194-203`, détaillés dans 04-catalogue-offres.md. Tous les montants issus du modèle sont des [ES], arrondis à la centaine d'euros (à la dizaine pour les prix par JP).

---

## En bref

1. **Le « contrat certain » vaut 0 €.** Il n'existe ni contrat, ni facture, ni entité payeuse [FV négatif] (`travaux/strategie-retenue.md:33`). Chaque euro de chiffre d'affaires de ce livrable est une hypothèse (`modele-financier/tresorerie-18-mois.md:23`).
2. **Les montants des archives ne tiennent pas.** La formule à 15 000 € HT pour 20 JP prend 78 à 83 % du temps des deux associés, celle à 30 000 € pour 40 JP 140 à 145 % [ES] (`travaux/syn-capacite-ia.md:228-229`). Les nets de 3 660 € par mois supposaient douze mois facturés, une SARL et un foyer fiscal imaginé ; le contrat proposé ne couvrait que six mois (section 2).
3. **Le taux de 750 € HT** couvre le coût complet d'une JP à pleine capacité (591 à 737 €), mais seulement le bas du coût sous le plafond de 10 JP de la première année (710 à 885 €) [ES]. Il reste un plancher interne. Le modèle réalise ≈ 870 € par JP vendue (section 3).
4. **Paiement : la nature de la prestation décide.** Temps réservé d'avance, livrables à l'acompte puis à la livraison, consommation variable en fin de mois. Le travail impayé à un instant donné reste sous ≈ 5 500 à 6 000 € HT, contre jusqu'à ≈ 18 500 € HT avec la version « fin de mois » du 29 octobre [ES, ce livrable] (section 4).
5. **Trois scénarios sur douze mois** : CA de 49 500, 89 400 et 141 100 € HT ; net par associé à partir du mois 4 de 600 à 800, 1 100 à 1 500 et 1 600 à 2 200 € par mois, avant impôt sur le revenu ; trésorerie libre au mois 12 de 7 100, 15 600 et 20 600 € (`modele-financier/scenarios.md:20-24, 41-67`). Pondéré par les probabilités de passage, le central ne vaut que 38 300 € HT, et seulement si le cadrage est vendu (section 5).
6. **La première année paie peu.** En central, Marwin verse ≈ 290 € nets par JP vendue et ≈ 130 € nets par journée réellement consacrée à Marwin [ES, ce livrable]. Un poste de cadre chez le client paierait davantage (section 7).
7. **Dix-huit mois en central** : point bas de 3 100 € en décembre 2026 (700 € ou 100 € si l'assurance est payée d'avance) ; trésorerie libre de 15 600 € au mois 12 et de 16 800 € en avril 2028. Pondérés, les encaissements tombent de 145 700 € à 54 100 € TTC (`modele-financier/tresorerie-18-mois.md:25-28, 135`) (section 8).
8. **Tests de résistance** : sans réaction, quatre situations rendent la trésorerie négative, jusqu'à 21 300 € de besoin. Avec la règle « pas de rémunération sans encaissement » et la baisse rapide des frais, il ne reste qu'un besoin de 1 700 €, dont 1 600 € de crédit de TVA remboursable (`modele-financier/stress-tests.md:340-342`). Le choc passe sur le revenu des associés : ils doivent garder d'autres revenus (section 9).
9. **Besoin de financement** : l'apport des associés seul, 10 000 € au minimum, ≈ 12 000 € si l'assurance doit être payée d'avance [ES, ce livrable]. Aucun prêt, aucun argent de GianLuca, aucune aide comptée (section 10).
10. **Deux écarts avec la stratégie retenue**, signalés en encadré : le revenu central à annoncer aux associés (≈ 1 300 € et non 1 350 à 1 550 €) et la mesure de la réserve au mois 12 (sections 5.6 et 5.7).
11. **On ne sait pas comment GianLuca paiera** : ni l'entité, ni les délais, ni la récupération de la TVA, ni le budget [IN]. Le calendrier retenu est une proposition à négocier (section 11).

---

## 1. Ce que ce livrable couvre, et ce qu'il ne refait pas

**Il couvre** : l'audit économique des montants des archives et du taux de 750 € HT ; le calendrier de paiement et sa traduction en trésorerie ; les trois scénarios chiffrés ; la différence entre chiffre d'affaires, bénéfice, trésorerie, TVA et revenu personnel ; les hypothèses des simulations de revenu ; le plan de trésorerie sur 18 mois ; les dix tests de résistance ; le besoin de financement ; les inconnues sur le paiement ; la façon de relancer le modèle.

**Il ne refait pas** : les fiches, prix, planchers et marges par offre, ni la décision sur chaque élément des archives (04-catalogue-offres.md, sections 3, 5 et 6) ; la capacité et les seuils de saturation (06-fonctionnement-a-deux.md) ; le calendrier d'action (08-feuille-de-route.md) ; le choix SAS ou SARL, le pacte et les rôles de GianLuca (10-structures-et-relations.md) ; le texte remis au client (11-proposition-commerciale-revisee.md ; pour-gianluca/proposition-de-cadrage.md) ; les clauses de paiement, de suspension et de sortie (12-gouvernance-contrat-sortie.md) ; les questions du rendez-vous (13-preparation-rendez-vous.md) ; le registre des risques (14-registre-risques-inconnues-decisions.md).

**Vérification du modèle.** Le script a été relancé le 4 nov. 2026 dans un dossier de travail séparé, avec Python 3.13.18 : « Contrôles de cohérence : tous passés », et les cinq sorties sont identiques, octet pour octet, aux fichiers déposés [MM]. Un contrôle indépendant a refait à la main le CA, l'enveloppe de rémunération, l'IS, la TVA, la trésorerie et le seuil, et corrigé six défauts sans changer un chiffre principal (`travaux/controle-modele.md:16, 20-31, 48-61`).

---

## 2. Audit des montants des archives

### 2.1 Ce que chaque montant supposait, et ce qu'il vaut une fois recalculé

La décision sur chaque élément (retiré, conservé, remplacé) est dans 04-catalogue-offres.md, section 6. Ce tableau n'en reprend que l'analyse économique.

| Montant des archives | Source [FV] | Ce qu'il supposait | Ce qu'il vaut, recalculé | Conclusion |
| --- | --- | --- | --- | --- |
| **15 000 € HT par mois pour 20 JP**, « environ un mi-temps » pour chacun | `interne/offre-marwin-tech-remuneration-et-collaboration.md:13-15` ; `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 3 ; `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:23, 64` | 20 JP × 750 € ; deux associés disponibles ; une demande du client | 27 à 29 JP de temps brut, soit 78 à 83 % du temps disponible des deux, dont 6 à 7 JP de production pure [ES] (`travaux/syn-capacite-ia.md:228`). 18 000 € TTC par mois, dont 3 000 € de TVA qui ne sont pas à Marwin [ES] (`travaux/rj-R2-fiscal.md:417`). Aucune parole directe du client ne le demande [FV négatif] (`travaux/syn-sources.md:38`) | Un CA de cet ordre n'existe que dans le scénario ambitieux, comme **somme** d'un socle, de lots, d'une exploitation et d'un second client, avec sous-traitance (section 5) |
| **30 000 € HT par mois pour 40 JP** | `interne/offre-marwin-tech-remuneration-et-collaboration.md:13-15` | Deux pleins temps | 49 à 51 JP de temps brut, soit 140 à 145 % du temps disponible [ES] (`travaux/syn-capacite-ia.md:229`) | Impossible à deux ; supposerait 12 à 20 JP sous-traitées ou un recrutement |
| **Six mois** : 90 000 € ou 180 000 € HT | `interne/offre-marwin-tech-remuneration-et-collaboration.md:16` | Un revenu annuel | Les nets internes sont calculés « si le même niveau dure douze mois » (`interne/offre-marwin-tech-remuneration-et-collaboration.md:105`), alors que « le contrat ne couvre que six mois » (même pièce, :121). Sur le seul contrat de 90 000 € HT, avec 25 000 € de frais : 17 100 à 19 100 € nets par personne sur l'année en SAS, ≈ 22 800 € en SARL, avant IR [ES] (`travaux/syn-droit.md:122`) | Lissé sur douze mois, ≈ 1 400 à 1 600 € nets par mois en SAS : à peine plus que le central de ce livrable (≈ 1 300 €), pour une charge de 78 à 83 % du temps pendant six mois et aucune suite garantie [ES, ce livrable] |
| **Acompte de 7 500 € HT**, déduit du premier mois | `interne/offre-marwin-tech-remuneration-et-collaboration.md:19, 193` ; `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:23, 55-56` ; diaporama client, copie du 4 nov., hors dépôt, `slides/paiement.html:9-10` | Une « trésorerie de démarrage » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:62`) | 9 000 € TTC, dont 1 500 € de TVA exigible à l'encaissement [FV pour la règle, ES pour le montant] (`travaux/rj-R2-fiscal.md:385, 416`). Il paie la moitié du premier mois : c'est un prix, pas une réserve. L'autre moitié reste due jusqu'à 7 jours après la fin du mois | Pas un coussin de trésorerie. Remplacé par l'acompte du cadrage (3 250 € HT) et celui des lots (40 %) (section 4). Un acompte n'est ni du capital ni un prêt (`interne/offre-marwin-tech-remuneration-et-collaboration.md:142`) |
| **Nets visés** : 7 500 €, 3 660 €, 2 500 € par personne et par mois ; plancher ≈ 10 300 € HT pour ≈ 14 JP ; « environ 370 € nets » par jour travaillé | `interne/offre-marwin-tech-remuneration-et-collaboration.md:107-119, 248` ; `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 18-19 | SARL à l'IS ; 180 000 € de CA et 30 000 € de frais par an ; foyer d'une part sans autre revenu ; nets **après** IR ; douze mois facturés | Le foyer est une « hypothèse pédagogique » (même PDF, p. 18) : la situation réelle est [IN] (`travaux/rj-R1-structures.md:15`). Les nets « à l'euro près » sont une précision artificielle (`travaux/syn-droit.md:136`). Le modèle de l'audit donne en central ≈ 1 300 € nets **avant** IR par associé, ≈ 290 € par JP vendue et ≈ 130 € par journée consacrée à Marwin [ES, ce livrable] (section 7) | Ne plus citer ces nets. Les remplacer par les fourchettes du modèle (`modele-financier/scenarios.md:67`) |
| **Taux de 750 € HT** par JP | Voir section 3 | — | — | Plancher interne, jamais montré (section 3) |
| **Option laboratoire** : 30 000 € HT, dont 13 500 € d'honoraires | `interne/offre-marwin-tech-remuneration-et-collaboration.md:21` ; `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` p. 8 | 18 JP × 750 € d'honoraires ; 16 500 € d'achats au nom de l'entité du client | Seuls 13 500 € auraient été du CA de Marwin ; « Les 16 500 € restants ne sont pas du chiffre d'affaires Marwin » (même PDF, p. 8) [FV]. Le poste de calcul de 10 000 € « n'est pas un besoin démontré » (p. 9). Avec la formule de base, la charge montait à 26 JP par mois (p. 8) | 0 € dans le modèle : projet non financé (section 8.3) |
| **Option création, STRATES** : ≈ 10 000 € HT pour une première phase | `interne/offre-marwin-tech-remuneration-et-collaboration.md:22, 84` | 6 JP de Marwin (4 500 € HT), plus la part de Medhi, une machine et des consommables | « Les 10 000 EUR envisagés pour le cadrage restent une enveloppe de discussion, non engagée » ; les 323 875 € HT « couvrai[en]t un programme de douze mois pour la peinture de figurines » et ne sont pas un devis (`pour-carlone/strates-proposition-artistique-v1.1.pdf` p. 4) [FV]. Le P0 du programme de figurines vaut 9 375 € HT réserve comprise (`interne/strates/archives-investisseur/budget-v1-2026-11-02.xlsx`, feuille Budget) [FV] | Retiré le 4 nov. [DR] (`travaux/note-point-4-novembre-et-activites.md:25`) ; 0 € dans le modèle |
| **Vernissage** : 4 500 à 22 500 € HT d'honoraires | `pour-carlone/vernissage-strates-idees.md:100-102, 110` | 6 à 30 JP × 750 € ; « rien à facturer en plus s'il tient dans les 20 journées » | Le format « sans supplément » faisait absorber un événement par le forfait. Lieu, date et budget [IN] (`travaux/syn-portefeuille.md:452`) | 0 € dans le modèle. Un premier événement sans robot reste possible comme lot C3 (04-catalogue-offres.md) |
| **DGX Spark** | `travaux/ver-R6-marche.md:66` | Achat de matériel pour l'IA locale | ≈ 6 170 € HT pour le 128 Go [ES] | 0 € dans le modèle ; s'il était avancé par Marwin, il coûterait 11 600 € de trésorerie avec 3 JP gratuites par mois sur deux mois (test 9, section 9) |

### 2.2 Ce que l'offre des archives aurait donné en trésorerie

| Version | Calendrier [FV] | Travail impayé au pire moment [ES, ce livrable] |
| --- | --- | --- |
| 29 oct. | Acompte de 7 500 € HT ; solde du mois 1 à sa fin ; mois 2 à 6 « règlement sous sept jours après facture de fin de mois » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:55-57`) | Jusqu'à un mois et une semaine d'honoraires, soit ≈ 18 000 à 18 500 € HT, à chaque échéance |
| 30 oct. et 2 nov. | Acompte de 7 500 € HT ; solde du mois 1 sous 7 jours ; mois 2 à 6 « d'avance, en début de mois » (`interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 3 ; `interne/offre-marwin-tech-remuneration-et-collaboration.md:19, 193-196`) | ≈ 7 500 € HT à la fin du mois 1, pendant au plus 7 jours ; ensuite 0 €, puisque le client paie d'avance |
| Stratégie retenue | Selon la nature de la prestation (section 4) | ≈ 5 500 à 6 000 € HT [ES] (`travaux/strategie-retenue.md:447`) |

**Lecture.** La version du 29 octobre faisait financer à Marwin plus d'un mois de travail, sans fonds propres connus. Les versions suivantes la corrigeaient, mais restaient attachées à une formule que les associés ne peuvent pas tenir. Le titre du diaporama, « Un calendrier simple, payé d'avance » (`slides/paiement.html:4`), couvre en réalité un premier mois soldé à terme échu (`slides/paiement.html:17-18`) [FV].

---

## 3. Le taux de 750 € HT : coût, marché, valeur

La décision (plancher interne, jamais montré, prix cible de 800 à 950 € par JP estimée, révision au mois 6) est prise par `travaux/strategie-retenue.md:393-401` et détaillée dans 04-catalogue-offres.md, section 5. Ici, on vérifie ce que le taux paie.

### 3.1 Coût complet d'une JP facturable

Méthode [ES] : (rémunération chargée des associés au prorata de leur temps pour Marwin, à 2 500 € nets par équivalent temps plein, coefficient SAS de 1,7 à 1,9 ; plus frais fixes de 1 500 à 2 500 € par mois) ÷ JP facturables ÷ 0,9 pour la réserve (`travaux/strategie-retenue.md:359` ; `travaux/calculs/arbitre-calc/verif.py` § 1).

| Situation | JP facturables par mois | Coût complet par JP [ES] | Le taux de 750 € |
| --- | --- | --- | --- |
| Prudent (Morgan 50 %, Mathys 25 %) | ≈ 7 | 744 à 962 € | Ne le couvre pas |
| Central, capacité pleine | ≈ 12 | 591 à 737 € | Le couvre |
| **Central, plafond de la première année** | **10** | **710 à 885 €** | **Couvre seulement le bas de la fourchette** |
| Haut (90 % chacun) | ≈ 20 | 508 à 614 € | Le couvre largement |

Source : `travaux/strategie-retenue.md:361-366`. Ce coût repose sur trois hypothèses fragiles : un coefficient social d'une seule source secondaire [HY] (`travaux/syn-droit.md:98`), des frais non devisés [HY], et des disponibilités que personne n'a écrites [IN] (`travaux/strategie-retenue.md:840`).

### 3.2 Repères de marché

Aucun organisme officiel ne publie de prix de conseil. Chef de projet senior en région : ≈ 570 à 760 € HT par jour [ES] ; moyenne « gestion de projets » des indépendants tech : 698 € [FV, étude privée] ; direction financière à temps partagé : 800 à 1 200 € [DR] ; management de transition : ≈ 1 330 € [DR] (`travaux/rj-R6-marche.md:29-31, 62, 80-83` ; `travaux/ver-R6-marche.md:27`). Le taux de 750 € est dans le haut de la fourchette d'un chef de projet en région et sous les repères de direction. L'origine du taux n'est documentée nulle part [HY] (`travaux/syn-portefeuille.md:633`).

### 3.3 Valeur pour GianLuca

- **Comparaison avec un salarié** [ES] : un chef de projet cadre coûte à son employeur 5 380 à 6 149 € par mois [MM, résultat du simulateur de l'Urssaf] (`travaux/ver-R6-marche.md:25`). C'est 7,2 à 8,2 JP à 750 €, ou 6,2 à 7,1 JP au prix moyen réalisé de 870 € [ES, ce livrable]. Au-delà d'environ 6 à 8 JP stables par mois, le salarié coûte moins cher au client (`travaux/strategie-retenue.md:378`). Marwin ne peut donc pas vendre du volume ; elle vend le pilotage, la responsabilité, l'outillage et la passation.
- **Valeur du cadrage** : GianLuca évite d'engager 90 000 € HT à l'aveugle et garde l'inventaire et les priorités même s'il s'arrête (`travaux/strategie-retenue.md:232`).
- **Valeur des gains** : inconnue [IN]. Le coût actuel de ses problèmes n'est mesuré nulle part ; le cadrage doit l'estimer avec lui (`travaux/strategie-retenue.md:225`).

### 3.4 Ce que le modèle réalise

| Indicateur, mois 4 à 12 | Prudent | Central | Ambitieux | Source |
| --- | --- | --- | --- | --- |
| Prix moyen encaissé par JP vendue [ES] | 870 € | 870 € | 860 € | `modele-financier/scenarios.md:98, 125, 151` |
| Net versé aux deux associés par mois, coefficient 1,8 [ES, ce livrable] | ≈ 1 370 € | ≈ 2 610 € | ≈ 3 800 € | Enveloppe ÷ 1,8 (`modele-financier/scenarios.md:178-180`) |
| Net par JP vendue par les associés [ES, ce livrable] | ≈ 260 € | ≈ 290 € | ≈ 320 € | ÷ 5,2 ; 8,9 ; 12 JP |
| Net par journée consacrée à Marwin (temps brut de 13,1 ; 20,1 ; 31,5 JP) [ES, ce livrable] | ≈ 105 € | ≈ 130 € | ≈ 120 € | Temps brut : `travaux/syn-capacite-ia.md:183` |

**Lecture.** Le prix moyen de 870 € est dans la fourchette cible de 800 à 950 € (`travaux/strategie-retenue.md:397`). Il reste sous le haut du coût complet à 10 JP (885 €) : le repère de 2 500 € nets par ETP n'est donc pas atteint la première année. Le contrôle du modèle parle d'un « prix cible de 900 € » (`travaux/controle-modele.md:113`) ; la stratégie dit 800 à 950 €, et 900 € est le prix de l'avenant E. Les 370 € nets par jour de l'offre écrite (`interne/offre-marwin-tech-remuneration-et-collaboration.md:119`) étaient calculés après IR, en SARL, sur douze mois à 20 JP facturés : ils ne sont pas comparables.

**Sensibilité** [ES, ce livrable, calcul approché sur la règle de rémunération du modèle] : si toutes les JP du central étaient vendues à 750 € au lieu de ≈ 870 €, l'enveloppe baisserait d'environ 1 000 € par mois pour les deux, soit ≈ 270 € nets de moins par associé (≈ 1 000 € au lieu de ≈ 1 300 €). C'est pourquoi le 750 € est un plancher et non un prix.

---

## 4. Calendrier de paiement retenu

### 4.1 La contradiction

| Date | Mois 2 à 6 | Source [FV] |
| --- | --- | --- |
| 29 oct. | « 15 000 € HT par mois ; règlement sous sept jours après facture de fin de mois » | `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:57` |
| 30 oct. | « 15 000 € HT d'avance, selon les modalités fixées au contrat » | `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 3 |
| 2 nov. | « mois 2 à 6 payés d'avance, en début de mois » | `interne/offre-marwin-tech-remuneration-et-collaboration.md:19, 195` |
| Diaporama, copie du 4 nov. | « Chaque mois, payé en début de mois » | `slides/paiement.html:26` (hors dépôt) |

L'écart est d'environ 37 jours par échéance [ES] (`travaux/syn-sources.md:279`). Rien ne montre que GianLuca ait vu ou accepté l'une ou l'autre version [IN] (même ligne). La version la plus récente n'est pas une décision.

### 4.2 Règle retenue [PR] : le paiement suit la nature de la prestation

`travaux/strategie-retenue.md:431-434, 438-447` :

| Prestation | Facturation | Échéance | Démarrage | Montant TTC à l'échéance [PR] | Travail impayé au pire moment [ES] |
| --- | --- | --- | --- | --- | --- |
| A. Cadrage (6 500 € HT) | 50 % à la commande, 50 % à la réception | Acompte à réception de facture ; solde sous 8 jours, exigible au plus tard 30 jours après la remise sans réserve motivée | À l'encaissement de l'acompte | 3 900 € puis 3 900 € | ≤ 3 250 € HT |
| B0, B1, B2. Socle (3 500, 4 500, 6 900 € HT par mois) | Mensuel à échoir, facture le 25 du mois précédent | Le 1er du mois ; premier mois à la signature | À l'encaissement du premier mois | 4 200, 5 400 ou 8 280 € par mois | ≤ 15 jours de socle (≈ 2 250 € HT pour B1) |
| C. Lots | 40 % à la commande, 60 % à la livraison ; 40 / 30 / 30 au-delà de 8 JP | 8 jours | À l'encaissement de l'acompte | Ex. C2 : 2 880 € puis 4 320 € | ≤ 60 % d'un lot (≈ 3 300 à 4 500 € HT) |
| D. Exploitation | Minimum à échoir ; variable en fin de mois | Minimum le 1er ; variable sous 15 jours | — | 1 200 à 1 800 € de minimum | ≤ un mois de variable |
| E. Avenant | Fin de mois, sur bon écrit préalable | 15 jours | Après signature | 1 080 € par JP | — |
| Achats, abonnements, prestataires du client | **Jamais par Marwin** | — | — | — | 0 € |

**Exposition totale** en régime central : ≈ 5 500 à 6 000 € HT de travail non payé à un instant donné (le solde d'un lot et quinze jours de socle). Ce n'est pas une sortie d'argent tant que les associés ne se paient pas sur ce montant (`travaux/strategie-retenue.md:447`).

**Pourquoi cette règle résout la contradiction.** Le temps réservé bloque des personnes nommées : il se paie avant. Un livrable se paie quand il est remis : le client paie ce qu'il reçoit. Seule la consommation variable reste en fin de mois. La version du 29 octobre, appliquée au socle, reviendrait à un décalage durable d'environ 37 jours ; son effet est du même ordre que le test « retard de paiement de 30 jours » : jusqu'à 8 000 € de trésorerie perdue si les associés se paient comme prévu, 3 300 € si leur rémunération suit les encaissements [ES] (`modele-financier/stress-tests.md:62`).

### 4.3 Garde-fous et concessions

- **Rien n'est encaissé avant l'immatriculation**, ni sur un compte personnel, ni par l'entreprise existante de Morgan (`travaux/strategie-retenue.md:458`).
- **TVA facturée dès la première facture**, exigible à l'encaissement de chaque acompte [FV] (`travaux/rj-R2-fiscal.md:385` ; CGI art. 269, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983827, consulté le 4 nov. 2026 selon `travaux/rj-R2-fiscal.md:405`, qui note son abrogation au 1er janvier 2027 avec transfert au nouveau code des impositions sur les biens et services : la base légale sera à revérifier en janvier 2027 [IN]).
- **Retard** : relance le lendemain ; suspension des travaux non urgents 8 jours après une relance sans effet ; résiliation possible à 30 jours ; pénalités d'au moins trois fois le taux de l'intérêt légal (8,25 % au second semestre 2026) et indemnité de 40 € par facture [FV] (`travaux/strategie-retenue.md:463` ; `travaux/rj-R2-fiscal.md:378-381` ; C. com. L441-10, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038414392, et D441-5, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043197457, consultés le 4 nov. 2026 selon `travaux/rj-R2-fiscal.md:400-402`).
- **Concession possible** : socle facturé en fin de mois, payable sous 7 jours, seulement après trois échéances payées à l'heure, avec suspension automatique à J+8 (`travaux/strategie-retenue.md:464`).
- **Rétractation** [HY, à trancher par l'avocat] : si le contrat est signé hors établissement avec une entité de 5 salariés au plus, aucun paiement avant 7 jours pourrait s'imposer. Le démarrage recule alors d'une semaine (`travaux/strategie-retenue.md:466`).

Les clauses sont rédigées dans 12-gouvernance-contrat-sortie.md ; la version remise au client, sans les colonnes d'exposition, est dans pour-gianluca/proposition-de-cadrage.md.

### 4.4 Traduction dans le modèle [HY]

Solde du cadrage encaissé le mois suivant l'acompte ; socle encaissé le mois du service ; lots en tranches (40 % le mois de commande, 60 % le mois suivant) ; TVA reversée le mois suivant (régime réel normal mensuel) ; rémunérations à partir du mois 4 ; IS de l'exercice 2027 payé en mai 2028 (`modele-financier/tresorerie-18-mois.md:56-64` ; `modele-financier/scenarios.md:91`). Le modèle suppose des paiements **à l'échéance** ; les retards ne figurent que dans les tests.

---

## 5. Trois scénarios chiffrés

### 5.1 Paramètres

| Paramètre | Prudent | Central (base de pilotage) | Ambitieux |
| --- | --- | --- | --- |
| **Périmètre** [PR] | Cadrage au plancher ; « socle + 1 projet » dès le mois 3 ; un lot par trimestre. Variante basse : arrêt après le cadrage | Cadrage ; pilote de 8 semaines (B0 et un lot) ; dès le mois 4, B1 et des lots | Cadrage ; pilote avec deux lots ; dès le mois 4, « socle + 3 projets » et des lots ; exploitation D dès le mois 7 ; second client dès le mois 6 |
| **Disponibilité** [HY] | Morgan 50 %, Mathys 25 % | Morgan 65 %, Mathys 50 % | 90 % chacun |
| **Capacité facturable** [ES] | ≈ 7 JP par mois | ≈ 12 JP, plafond engagé de 10 | ≈ 20 JP |
| **JP vendues par mois, mois 4 à 12** [ES] | 5,2 | 8,9 | 15,0, dont 3,0 sous-traitées |
| **Prix** [PR] | Cadrage 6 000 € ; socle léger 3 000 € par mois ; lot de 4 500 € par trimestre | Cadrage 6 500 € ; B0 3 500 € par mois ; lot du pilote 6 000 € ; B1 4 500 € par mois ; lots ≈ 3 500 € par mois | Cadrage 6 500 € ; B0 3 500 € ; deux lots de 6 000 € ; socle + 3 à 5 700 € ; lots ≈ 4 500 € ; D 1 500 € ; second client 2 500 € par mois |
| **Modalités** [PR] | Section 4.2 | Section 4.2 | Section 4.2 ; sous-traitance à 450 à 550 € par JP |
| **Mois 1** [HY] | Février 2027 | Janvier 2027 | Décembre 2026 |
| **Probabilités de passage** [HY] | Suite après le cadrage 40 % ; renouvellement 60 % | Pilote 60 % ; socle 70 % ; renouvellement trimestriel 80 % | 80 % ; 80 % ; 90 % ; second client 50 % |
| **Frais fixes par mois** [HY] | 1 500 € | 2 000 € | 2 800 € |
| **Démarrage** [ES] | 4 000 à 5 000 € | 5 000 à 7 000 € | 6 000 à 8 000 € |
| **Apport des associés** [HY] | 8 000 € | 10 000 € | 13 000 € |
| **Dépendances** | Cadrage payé au plus tard le 31 janv. 2027 ; Morgan garde ses autres projets | Disponibilités nominatives écrites (8 à 10 JP facturables) ; pilote aux critères ; 100 % GianLuca | Engagement à 90 % inscrit au pacte ; sous-traitant identifié ; pilote réussi ; second client |

Sources : `travaux/strategie-retenue.md:494-516` ; `modele-financier/scenarios.md:32-40, 76-85`. La probabilité de vendre le cadrage lui-même est [IN]. Le détail des frais du central [HY] : outils et IA 300 €, déplacements 500 € [IN : lieu de résidence], assurance 200 € [IN : aucun devis], expert-comptable et paie 350 €, banque 30 €, conseil ponctuel 200 €, divers 220 €, imprévus 200 € ; démarrage : conseil sur la fuite 2 000 € en novembre 2026, statuts et pacte 3 500 €, formalités 300 €, mise en place 200 € (`modele-financier/modele_financier.py:158-201`).

### 5.2 Résultats sur douze mois de contrat (période préalable comprise)

Une valeur seule est la valeur centrale. Une plage va de « frais hauts et coefficient 1,9 » à « frais bas et coefficient 1,7 ».

| Rubrique [ES] | Prudent | Central | Ambitieux |
| --- | --- | --- | --- |
| **CA facturé HT, mois 1 à 12** | **49 500 €** | **89 400 €** | **141 100 €** |
| dont hors GianLuca | 0 € | 0 € | 17 500 € |
| Part de GianLuca (12 mois ; mois 12) | 100 % ; 100 % | 100 % ; 100 % | 88 % ; 82 % |
| Contrat certain | 0 € | 0 € | 0 € |
| CA pondéré par les probabilités, si le cadrage est vendu | 16 800 € | 38 300 € | 87 000 € |
| Coûts directs HT (outils et IA, déplacements) | 4 300 à 6 800 € | 7 700 à 12 000 € | 12 500 à 19 500 € |
| Sous-traitance HT | 0 € | 0 € | 13 500 € |
| **Marge après coûts directs et sous-traitance** [ES, ce livrable] | 86 à 91 % | 87 à 91 % | 77 à 82 % |
| Frais généraux HT (assurances, comptable, banque, conseil, divers) | 10 100 à 15 800 € | 11 500 à 18 000 € | 14 400 à 22 500 € |
| Frais de démarrage HT | 4 000 à 5 000 € | 5 000 à 7 000 € | 6 000 à 8 000 € |
| Rémunérations, coût total pour la société | 19 100 à 24 700 € | 38 300 à 45 600 € | 55 800 à 66 100 € |
| **Résultat avant IS** | 2 900 à 6 400 € | 14 100 à 19 600 € | 21 800 à 28 600 € |
| **Marge nette avant IS, en % du CA** [ES, ce livrable] | 6 à 13 % | 16 à 22 % | 15 à 20 % |
| IS (15 % jusqu'à 42 500 €) | 400 à 1 000 € | 2 100 à 2 900 € | 3 300 à 4 300 € |
| Résultat net | 2 400 à 5 500 € | 12 000 à 16 700 € | 18 600 à 24 300 € |
| Trésorerie en banque, fin du mois 12 | 11 200 à 14 900 € | 25 400 à 31 100 € | 37 000 à 43 900 € |
| **Trésorerie disponible** (TVA due déduite), valeur centrale | 12 800 € | 27 000 € | 38 500 € |
| dont réserve (10 % du CA encaissé) | 5 000 € | 8 900 € | 14 100 € |
| **Trésorerie libre** (après réserve et IS), valeur centrale | 7 100 € | 15 600 € | 20 600 € |
| Point bas de la trésorerie disponible | 2 900 € (janv. 2027) | 3 100 € (déc. 2026) | 5 400 € (déc. 2026) |
| **Net par associé et par mois, SAS, mois 4 à 12, avant IR** | 600 à 800 € (≈ 700 €) | 1 100 à 1 500 € (≈ 1 300 €) | 1 600 à 2 200 € (≈ 1 900 €) |
| Occupation de la capacité facturable, mois 4 à 12 | 74 % | 74 % (89 % du plafond de 10 JP) | 60 % |

Sources : `modele-financier/scenarios.md:20-24, 32-67`. Les deux lignes « marge » sont calculées ici sur ces sorties.

### 5.3 Seuil de rentabilité, en JP vendues par mois

| Scénario | Prix moyen par JP | Frais fixes | Seuil : frais et réserve, sans rémunération | Seuil : avec la rémunération du scénario | Seuil : avec 2 500 € nets par ETP engagé | JP vendues prévues | Capacité |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Prudent | 870 € | 1 500 € | 1,9 | 5,1 | 6,0 à 6,5 | 5,2 | 7 |
| Central | 870 € | 2 000 € | 2,5 | 8,5 | 8,8 à 9,5 | 8,9 | 12 (plafond 10) |
| Ambitieux | 860 € | 2 800 € | 4,2 | 14,4 | 15,6 à 16,9 | 15,0 | 20 |

Source : `modele-financier/scenarios.md:193-200` ; ETP engagés [HY] : 0,75, 1,15 et 1,8.

**Lecture.** La société survit avec très peu de JP (2,5 en central) : ses frais sont faibles. Ce qui coûte, ce sont les associés. Le repère de 2 500 € nets par ETP n'est atteint en régime que dans le central, à la limite (8,9 JP prévues pour 8,8 à 9,5 nécessaires), et jamais sur l'année, puisque rien n'est versé avant le mois 4 (`modele-financier/scenarios.md:24`).

### 5.4 Comment lire la marge

L'enveloppe de rémunération n'est pas un choix libre. Le modèle prend **la plus grande enveloppe constante** qui laisse, sur les mois 4 à 12, de quoi payer les frais, la réserve de 10 % et l'IS (`modele-financier/modele_financier.py:115-120`) [PR du modèle, à valider par les associés]. La « marge nette » est donc surtout la réserve, plus l'excédent des mois 1 à 3 (pilote payé, aucune rémunération), moins le démarrage. Ce n'est pas un profit en plus : c'est le coussin qui absorbe les chocs de la section 9. Les marges par offre sont dans 04-catalogue-offres.md.

### 5.5 Variantes et sensibilités

| Variante | Résultat [ES] | Source |
| --- | --- | --- |
| **Prudent, variante basse** (arrêt après le cadrage) | CA 6 000 € HT ; résultat −16 500 € ; trésorerie disponible −10 300 € au mois 12 si rien n'est arrêté (dont 1 800 € de crédit de TVA, non compté) ; négative dès juillet 2027 | `modele-financier/scenarios.md:205` |
| **Central avec un second client** (2 000 € HT par mois dès le mois 7) | CA 93 300 € HT ; part de GianLuca 87 % sur 12 mois, 76 % au mois 12 ; net 1 200 à 1 600 € par associé ; disponible 27 500 € au mois 12 | `modele-financier/scenarios.md:206` |
| **Central avec un pilote moins cher** : C2 seul (6 000 € HT) ou C6 seul (7 500 € HT) au lieu de B0 et un lot (13 000 € HT) | CA de 82 400 ou 83 900 € HT ; trésorerie libre au mois 12 de 9 200 ou 10 600 € au lieu de 15 600 € ; rémunération inchangée | `modele-financier/scenarios.md:232` |
| **Prime d'assurance annuelle payée d'avance** (2 400 ou 3 000 €) | Point bas de 700 € ou 100 € en décembre 2026 au lieu de 3 100 € | `modele-financier/tresorerie-18-mois.md:135` |
| **Réserve à 12 % au lieu de 10 %** | Enveloppe centrale de 4 500 € au lieu de 4 700 € (≈ 50 € nets de moins par associé) ; réserve de 10 700 € au mois 12, qui atteint seule l'objectif | [ES, ce livrable : script relancé dans un dossier de travail avec ce seul paramètre changé] |

### 5.6 Écart avec la stratégie retenue : le revenu à annoncer aux associés

> **Écart avec la stratégie retenue : revenu central et CA ambitieux.**
> La stratégie annonce ≈ 1 350 à 1 550 € nets par associé en régime central (`travaux/strategie-retenue.md:56, 511, 737`), ≈ 2 100 à 2 350 € en ambitieux et ≈ 150 000 € HT de CA ambitieux (`travaux/strategie-retenue.md:511, 513`). Le modèle donne ≈ 1 300 € (1 100 à 1 500 €), ≈ 1 900 € (1 600 à 2 200 €) et 141 100 € HT (`modele-financier/scenarios.md:217-221`).
> **Pourquoi** : la stratégie utilisait un calcul simplifié, sans IS, sans décalage de TVA ni délais d'encaissement (`travaux/strategie-retenue.md:518`). Pour l'ambitieux, elle faisait démarrer l'exploitation D au mois 4 dans son calcul, alors que sa propre règle dit « au plus tôt au mois 7 » (`travaux/strategie-retenue.md:339`) ; le modèle suit la règle écrite.
> **Ce que ce livrable retient** : les chiffres du modèle. Dans la fiche « rôles et disponibilités », la condition de validité sur le revenu (`travaux/strategie-retenue.md:56`) et la question 10 aux associés (`travaux/strategie-retenue.md:737`), écrire « ≈ 1 100 à 1 500 € nets chacun en régime central, avant impôt sur le revenu, rien avant le mois 4 ». Annoncer le haut de la fourchette ferait accepter la stratégie sur un revenu que le modèle ne confirme pas.

### 5.7 Écart avec la stratégie retenue : la réserve au mois 12

> **Écart avec la stratégie retenue : critère de réserve du mois 12.**
> La stratégie fixe une réserve de 10 % du CA (`travaux/strategie-retenue.md:479`) et un critère de réception à 12 mois : « Réserve ≥ 3 mois de frais fixes et 1 mois de rémunération » (`travaux/strategie-retenue.md:175, 512`). Le modèle montre que la réserve de 10 % ne l'atteint dans **aucun** scénario : 8 900 € pour 10 700 € visés en central ; il n'est atteint qu'avec l'apport restant et l'excédent des mois 1 à 3 (`modele-financier/scenarios.md:66`).
> **Pourquoi c'est important** : lu à la lettre, le critère serait manqué même quand tout va bien. Or l'excédent des mois 1 à 3 n'existe que si le pilote est vendu (section 5.5).
> **Ce que ce livrable propose** [PR, ce livrable] : garder la réserve de 10 % et mesurer le critère du mois 12 sur « réserve + trésorerie libre ». Si le pilote vendu est C2 ou C6 seul, ou si la trésorerie libre passe sous 5 000 € au mois 6, porter la réserve à 12 %, pour environ 50 € nets de moins par associé et par mois [ES].

---

## 6. Chiffre d'affaires, bénéfice, trésorerie, TVA, revenu personnel : cinq choses différentes

| Notion | Ce que c'est | Central, 12 mois [ES] | Ce qu'il ne faut pas confondre |
| --- | --- | --- | --- |
| **Chiffre d'affaires** | Ce que Marwin facture, hors TVA | 89 400 € HT | Ce n'est pas de l'argent reçu, ni un revenu |
| **Encaissements** | Ce qui arrive sur le compte, TVA comprise | 107 300 € TTC | 17 900 € de cette somme sont de la TVA |
| **TVA** | Impôt collecté pour l'État | Collectée 17 900 € ; déduite sur les achats 3 800 € ; reversée 12 700 € ; encore due 1 400 € fin du mois 12 | Elle n'est jamais à Marwin. Un retard du client ne la fait pas avancer : elle n'est due qu'à l'encaissement [FV] (`modele-financier/tresorerie-18-mois.md:123`) |
| **Bénéfice** | CA moins frais, démarrage et rémunérations | Avant IS : 14 100 à 19 600 € ; IS : 2 100 à 2 900 €, payé en mai 2028 ; net : 12 000 à 16 700 € | Le bénéfice se calcule **après** les salaires. Il ne se distribue qu'après l'approbation des comptes (au plus tôt au printemps 2028 [HY]) |
| **Trésorerie** | L'argent en banque | En banque 28 400 € ; disponible 27 000 € ; libre 15 600 € (après réserve de 8 900 € et IS de 2 600 €) | Elle contient l'apport de 10 000 €, qui n'est pas un bénéfice, et la TVA due |
| **Revenu personnel** | Le salaire net reçu par chaque associé | ≈ 1 300 € (1 100 à 1 500 €) par mois, à partir du mois 4 ; enveloppe de 4 700 € par mois pour les deux, cotisations comprises | Il est **avant** impôt sur le revenu, inconnu [IN]. Ce n'est pas le CA divisé par deux |

Sources : `modele-financier/scenarios.md:25, 41-64` ; `modele-financier/tresorerie-18-mois.md:26`.

**Un mois de régime, mai 2027** [ES, ce livrable, sur les paramètres du modèle] : Marwin facture 8 000 € HT et reçoit 9 600 € TTC.
- ≈ 1 400 € de TVA nette repartent à l'État (1 600 € collectés, ≈ 200 € récupérés sur les frais) ;
- ≈ 2 000 € HT paient les frais fixes ;
- ≈ 2 100 € paient les cotisations des deux associés ;
- ≈ 2 600 € arrivent sur leurs comptes personnels, soit ≈ 1 300 € chacun, avant IR ;
- il reste ≈ 1 300 € : 800 € de réserve, ≈ 200 € d'IS à provisionner, ≈ 300 € de marge.

Sur 9 600 € reçus, un peu plus d'un quart devient du revenu personnel.

**Régime de TVA** [HY, à choisir avec l'expert-comptable] : le modèle retient le réel normal mensuel. Au réel simplifié sans acompte la première année, ≈ 14 000 € de TVA nette de 2027 resteraient sur le compte jusqu'en mai 2028 ; ils gonfleraient la trésorerie apparente sans jamais être disponibles (`modele-financier/tresorerie-18-mois.md:124`). La franchise en base est sans intérêt : la TVA est facturée dès la première facture (`travaux/syn-droit.md:299`).

---

## 7. Revenu personnel : hypothèses des simulations

### 7.1 Statut, cotisations, fiscalité, frais

| Hypothèse | Valeur dans le modèle | Code | Source | À confirmer par |
| --- | --- | --- | --- | --- |
| Forme | SAS à l'IS ; président et directeur général, assimilés salariés s'ils sont rémunérés | [PR] ; [FV] pour le régime | `travaux/strategie-retenue.md:543` ; `travaux/rj-R1-structures.md:23` | Expert-comptable ; choix dans 10-structures-et-relations.md |
| Coût d'une rémunération | 1,7 à 1,9 fois le net (central 1,8) | [HY] | Une seule source secondaire (Bpifrance) ; pages urssaf.fr en erreur HTTP 503 le 4 nov. 2026 (`travaux/rj-R1-structures.md:13, 50` ; `travaux/syn-droit.md:98`) | Simulateur officiel, https://mon-entreprise.urssaf.fr/simulateurs/sasu (cité par `travaux/rj-R1-structures.md:14`) |
| Brut indicatif | Net ÷ 0,75 | [HY] | `modele-financier/scenarios.md:174` | Fiche de paie réelle |
| Protection | Pas d'assurance chômage ; indemnités journalières plafonnées à 41,95 € par jour ; **sans rémunération, aucune cotisation et aucun droit** | [FV] | `travaux/syn-droit.md:111-115` ; F38152, https://entreprendre.service-public.gouv.fr/vosdroits/F38152, consulté le 4 nov. 2026 selon `travaux/rj-R1-structures.md:69` | Assureur (prévoyance) |
| Calendrier | Rien avant le mois 4 ; enveloppe constante ensuite ; même montant pour les deux | [PR du modèle] | `modele-financier/modele_financier.py:108, 115-120` ; `modele-financier/scenarios.md:174` | Décision collective des associés |
| IS | 15 % jusqu'à 42 500 € de bénéfice, 25 % au-delà, capital entièrement libéré | [FV] | Art. 219 CGI, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868562, consulté le 4 nov. 2026 selon `travaux/rj-R1-structures.md:102` ; `travaux/syn-droit.md:142` | Expert-comptable (date de clôture, prorata d'un premier exercice long) |
| Impôt sur le revenu | **Non calculé** | [IN] | `travaux/rj-R1-structures.md:15` ; `travaux/syn-droit.md:93` | Chaque associé, avec son foyer |
| Dividendes | PFU de 31,4 % ; aucun dividende avant l'approbation des comptes ; aucun droit social | [FV] | `modele-financier/structures.md:53-60` ; `travaux/syn-droit.md:144` | Expert-comptable |
| Frais de Marwin | 1 500 / 2 000 / 2 800 € par mois ; assurance 200 € sans devis | [HY] ; [IN] pour l'assurance | `modele-financier/modele_financier.py:178-182` | Devis d'assureur, de comptable, de banque |
| Aides | Aucune : ni ACRE, ni ARE, ni ARCE, ni FRR, ni aide régionale | [PR] | `travaux/strategie-retenue.md:564` | Expert-comptable, France Travail |
| Mutuelle, prévoyance | Exclues du calcul | [HY] | `modele-financier/scenarios.md:174` | Assureur |

**Dividendes : ne pas citer « 13 700 € par associé ».** Ce chiffre comparait des ressources inégales. À ressources égales, en central, le dividende net après PFU (IR compris) vaut 11 800 €, comme le salaire net de SAS **avant** IR au coefficient 1,8 ; en ambitieux, il fait moins bien (16 400 € contre 17 100 €) [ES] (`travaux/controle-modele.md:52, 112` ; `modele-financier/structures.md:60`). Il n'existe pas de levier « dividendes » la première année.

**SAS ou SARL, même enveloppe** [ES] : en central, la SARL laisse 1 500 à 1 800 € nets par mois au lieu de 1 100 à 1 500 €, mais elle coûte des cotisations même sans rémunération (forfaits d'environ 3 600 € par gérant la première année, puis un minimum d'environ 1 255 € par an) et une régularisation de 1 900 à 3 000 € en année 2 (`modele-financier/structures.md:31-35, 43-48`). La recommandation reste la SAS (`modele-financier/structures.md:14-17`) ; le raisonnement complet est dans 10-structures-et-relations.md.

### 7.2 Hypothèses personnelles manquantes

Aucune de ces informations n'est écrite [IN]. Chacune peut changer le revenu réel ou la forme juridique.

| Inconnue | Effet | Source de la question |
| --- | --- | --- |
| Foyer fiscal de chacun (parts, conjoint, autres revenus) | Impôt sur le revenu, choix PFU ou barème | `travaux/rj-R1-structures.md:15` |
| Autres revenus pendant 18 mois : activités de Morgan (OLSEN, autres clients), emploi ou études de Mathys | Capacité à vivre sans rémunération ; occupation réelle | `travaux/strategie-retenue.md:734` ; `travaux/note-point-4-novembre-et-activites.md:9-17` |
| Droits à l'ARE ou à l'ARCE ; éligibilité à l'ACRE | Revenu de transition ; non compté | `travaux/syn-droit.md:205, 207` |
| Apport possible de chacun (8 000 à 14 000 € à deux) | Démarrage et point bas (section 10) | `travaux/strategie-retenue.md:737, 776` |
| Capacité à vivre trois à quatre mois sans rémunération de Marwin | Condition de validité sur le revenu et l'apport | `travaux/strategie-retenue.md:56, 737` |
| Besoin de mutuelle et de prévoyance | Coût en plus, non modélisé | `travaux/syn-droit.md:203` |
| Lieu de résidence | Frais de déplacement (500 € par mois en hypothèse) ; FRR | `travaux/strategie-retenue.md:508` |
| Règle de partage entre les deux associés | Le modèle partage à égalité ; la stratégie prévoit une grille liée au temps engagé | `travaux/strategie-retenue.md:550` |
| Matériel personnel utilisé | Non budgété au-delà de 200 à 700 € | `modele-financier/scenarios.md:233` |

**Partage selon le temps** [ES, ce livrable] : le modèle donne la même somme aux deux (`modele-financier/scenarios.md:174`), alors que la stratégie prévoit une rémunération « fixée par décision collective selon une grille liée au temps engagé » (`travaux/strategie-retenue.md:550`). Avec les disponibilités du central (65 % et 50 %), les ≈ 2 610 € nets mensuels se partageraient en ≈ 1 480 € pour Morgan et ≈ 1 140 € pour Mathys, au coefficient 1,8. Ce point est à trancher dans le pacte (10-structures-et-relations.md).

### 7.3 L'alternative du salariat

Un poste de cadre chez le client rapporterait ≈ 3 400 € nets pour 6 149 € de coût employeur [MM selon la source ; c'est un résultat de simulateur, plus proche d'une ES (`travaux/controle-modele.md:95`)] (`travaux/ver-R6-marche.md:25`). C'est plus que tous les scénarios de Marwin la première année (`modele-financier/scenarios.md:186` ; `travaux/strategie-retenue.md:707`). La première année de Marwin est un investissement en temps faiblement payé : ≈ 130 € nets par journée consacrée à Marwin en central [ES, ce livrable]. Les associés doivent le décider en le sachant. Le traitement de cette alternative pendant la négociation est dans 13-preparation-rendez-vous.md et 15-contre-analyse.md.

---

## 8. Plan de trésorerie sur dix-huit mois (scénario central)

### 8.1 Trois blocs distincts

| Bloc | Contenu | Encaissements sur 18 mois, TTC [ES] |
| --- | --- | --- |
| 1. Contrat certain | Aucun contrat, aucune facture, aucune entité payeuse [FV négatif] | **0 €** |
| 2. Hypothèses de vente et de renouvellement | Cadrage (probabilité [IN]) ; pilote (60 %) ; socle B1 par trimestres (70 %, puis 80 % par renouvellement) ; lots liés au socle [HY] | 145 700 €, soit 54 100 € une fois pondérés |
| 3. Projets non financés | Laboratoire, création avec Medhi et STRATES, vernissage « signature », DGX Spark | **0 €** de recette et **0 €** de dépense |

Source : `modele-financier/tresorerie-18-mois.md:33-37`.

### 8.2 Projection mensuelle

| Mois | Mois du contrat | Contrat certain | Encaissements hypothétiques TTC | dont TVA | Probabilité cumulée [HY] | Encaissements pondérés TTC [ES] | Sorties hors TVA (démarrage, frais, rémunérations) | TVA reversée | Trésorerie disponible | Trésorerie libre |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| nov. 2026 | avant | 0 € | 0 € | 0 € | 0,00 | 0 € | 2 400 € | 0 € | 7 600 € | 7 600 € |
| déc. 2026 | avant | 0 € | 0 € | 0 € | 0,00 | 0 € | 4 500 € | 0 € | 3 100 € | 3 100 € |
| janv. 2027 | 1 | 0 € | 3 900 € | 700 € | 1,00 | 3 900 € | 2 500 € | 0 € | 4 500 € | 4 200 € |
| févr. 2027 | 2 | 0 € | 11 000 € | 1 800 € | 0,60 | 8 100 € | 2 200 € | 0 € | 12 400 € | 10 800 € |
| mars 2027 | 3 | 0 € | 8 500 € | 1 400 € | 0,60 | 5 200 € | 2 300 € | 900 € | 17 500 € | 14 400 € |
| avr. 2027 | 4 | 0 € | 7 100 € | 1 200 € | 0,42 | 2 900 € | 6 900 € | 1 200 € | 16 700 € | 13 200 € |
| mai 2027 | 5 | 0 € | 9 600 € | 1 600 € | 0,42 | 4 100 € | 6 900 € | 900 € | 18 000 € | 13 500 € |
| juin 2027 | 6 | 0 € | 9 600 € | 1 600 € | 0,42 | 4 000 € | 6 900 € | 1 400 € | 19 300 € | 13 800 € |
| juil. 2027 | 7 | 0 € | 9 600 € | 1 600 € | 0,34 | 3 400 € | 7 000 € | 1 400 € | 20 600 € | 14 100 € |
| août 2027 | 8 | 0 € | 9 600 € | 1 600 € | 0,34 | 3 300 € | 6 900 € | 1 400 € | 21 900 € | 14 400 € |
| sept. 2027 | 9 | 0 € | 9 600 € | 1 600 € | 0,34 | 3 200 € | 6 900 € | 1 300 € | 23 200 € | 14 700 € |
| oct. 2027 | 10 | 0 € | 9 600 € | 1 600 € | 0,27 | 2 700 € | 6 900 € | 1 400 € | 24 500 € | 15 000 € |
| nov. 2027 | 11 | 0 € | 9 600 € | 1 600 € | 0,27 | 2 600 € | 7 000 € | 1 400 € | 25 800 € | 15 300 € |
| déc. 2027 | 12 | 0 € | 9 600 € | 1 600 € | 0,27 | 2 600 € | 7 000 € | 1 400 € | 27 000 € | 15 600 € |
| janv. 2028 | 13 | 0 € | 9 600 € | 1 600 € | 0,22 | 2 200 € | 6 900 € | 1 300 € | 28 300 € | 15 900 € |
| févr. 2028 | 14 | 0 € | 9 600 € | 1 600 € | 0,22 | 2 100 € | 6 900 € | 1 400 € | 29 600 € | 16 200 € |
| mars 2028 | 15 | 0 € | 9 600 € | 1 600 € | 0,22 | 2 000 € | 7 000 € | 1 400 € | 30 900 € | 16 500 € |
| avr. 2028 | 16 | 0 € | 9 600 € | 1 600 € | 0,17 | 1 800 € | 6 900 € | 1 400 € | 32 200 € | 16 800 € |
| **Total** | | **0 €** | **145 700 €** | **24 300 €** | | **54 100 €** | **104 000 €** | **18 200 €** | | |

Données : `modele-financier/tresorerie-18-mois.csv` (colonnes « sorties » = démarrage + frais fixes + rémunérations, additionnées ici) ; tableaux complets dans `modele-financier/tresorerie-18-mois.md:69-114`. Apport de 10 000 € versé en novembre 2026, non compté dans les encaissements.

**Comment lire la colonne « probabilité cumulée »** : 1,00 au mois 1 veut dire « si le cadrage est vendu », pas « certain » (`modele-financier/tresorerie-18-mois.md:146`). 0,60 : pilote. 0,42 : premier trimestre de socle (0,6 × 0,7). Puis × 0,8 à chaque renouvellement trimestriel : 0,34, 0,27, 0,22, 0,17. Ces probabilités sont des paramètres de jugement, à remplacer par les faits à chaque étape [HY] (`travaux/strategie-retenue.md:502`).

### 8.3 Projets non financés, pour mémoire

Laboratoire (30 000 € HT, dont 13 500 € d'honoraires), création avec Medhi et STRATES (≈ 10 000 € HT), STRATES et Éclosion (aucun budget propre), vernissage « signature » (4 500 à 22 500 € HT d'honoraires), DGX Spark (≈ 6 200 € HT) : aucun n'est inscrit au plan (`modele-financier/tresorerie-18-mois.md:42-49`). Leur retour suppose un financeur écrit, un budget plafonné et un critère d'arrêt (`travaux/strategie-retenue.md:639-654`). Marwin n'avance rien pour le client (`travaux/strategie-retenue.md:188`).

### 8.4 Ce que montre la projection

- **Le démarrage est payé avant tout encaissement** : 2 400 € TTC de conseil sur la fuite en novembre, 4 500 € de statuts et formalités en décembre. Sans apport, il manquerait 6 900 € au point bas (`modele-financier/tresorerie-18-mois.md:25`).
- **L'essentiel du coussin vient des mois 1 à 3**, où le pilote est payé sans rémunération. Un pilote non vendu le supprime (`modele-financier/tresorerie-18-mois.md:131`).
- **À partir du mois 4**, la trésorerie libre ne monte que d'environ 300 € par mois : la règle de rémunération verse presque tout le reste.
- **L'IS de 2027** (2 600 €) est dû en mai 2028, juste après l'horizon : il ne doit pas être dépensé (`modele-financier/tresorerie-18-mois.md:132`).
- **Dépendance à un seul client : 100 % pendant 18 mois**, à assumer par écrit entre les associés, ce qui n'est pas fait [IN] (`modele-financier/tresorerie-18-mois.md:133`).
- Le modèle ne calcule le plan sur 18 mois que pour le central. Le prudent et l'ambitieux sont donnés sur douze mois (section 5).

---

## 9. Tests de résistance

### 9.1 Méthode

Base : scénario central, novembre 2026 à avril 2028, apport de 10 000 €, enveloppe de 4 700 € par mois dès le mois 4. Chaque test est calculé deux fois : **A, sans réaction**, et **B, avec la règle de protection** de la stratégie. Le **besoin de financement** est l'apport supplémentaire qui garde la trésorerie disponible positive sur 18 mois (`modele-financier/stress-tests.md:20-24`). Les tests sont appliqués un par un.

### 9.2 Résultats

| Test (hypothèse) [HY] | Besoin de financement A ; B | Besoin pour garder un mois de charges A ; B | Perte maximale de trésorerie A ; B | Premier mois sous zéro (A) | Trésorerie disponible au mois 12 A ; B | Manque à la réserve cible du mois 12 A ; B |
| --- | --- | --- | --- | --- | --- | --- |
| *Base* | — | — | — | aucun | 27 000 € | 0 € |
| 1a. Retard de paiement de 30 jours, durable dès avril 2027 | 0 € ; 0 € | 0 € ; 0 € | 8 000 € ; 3 300 € | aucun | 19 000 € ; 23 800 € | 0 € ; 0 € |
| 1b. Retard de 60 jours | 0 € ; 0 € | 3 600 € ; 0 € | 16 000 € ; 6 600 € | aucun | 11 000 € ; 20 500 € | 2 200 € ; 0 € |
| 1c. Retard de 90 jours | 3 400 € ; 0 € | 10 400 € ; 0 € | 24 000 € ; 9 900 € | juin 2027 | 3 000 € ; 17 200 € | 10 200 € ; 0 € |
| 2a. Rupture brutale à la fin du pilote (fin mars 2027), dernier solde impayé | 21 300 € ; 1 700 € | 22 500 € ; 2 800 € | 53 600 € ; 33 900 € | juin 2027 | −16 900 € ; 2 800 € | 27 600 € ; 7 900 € |
| 2b. Rupture brutale après le premier trimestre de socle (fin juin 2027) | 12 600 € ; 0 € | 13 700 € ; 0 € | 44 900 € ; 25 200 € | sept. 2027 | −8 200 € ; 11 500 € | 18 900 € ; 0 € |
| 3. Pas de renouvellement après six mois de socle (fin sept. 2027) | 3 100 € ; 0 € | 4 200 € ; 0 € | 35 300 € ; 15 600 € | mars 2028 | 4 700 € ; 21 000 € | 6 000 € ; 0 € |
| 4. Dépassement de 50 % du lot du pilote | 0 € ; 0 € | 0 € ; 0 € | 3 600 € ; 3 600 € | aucun | 24 000 € ; 26 300 € | 0 € ; 0 € |
| 5. Hausse des coûts d'IA (+1 000 € par mois en A, +150 € en B) | 0 € ; 0 € | 0 € ; 0 € | 16 000 € ; 2 400 € | aucun | 15 000 € ; 25 200 € | 0 € ; 0 € |
| 6. Indisponibilité d'un associé pendant six semaines (mai et juin 2027) | 0 € ; 0 € | 0 € ; 0 € | 9 000 € ; 4 300 € | aucun | 18 000 € ; 22 800 € | 0 € ; 0 € |
| 7. Deux urgences de 1,5 JP en juin 2027 | 0 € ; 0 € | 0 € ; 0 € | 2 700 € ; 0 € | aucun | 24 300 € ; 29 700 € | 0 € ; 0 € |
| 8. Arrêt d'un fournisseur technique en août 2027 | 0 € ; 0 € | 0 € ; 0 € | 3 500 € ; 1 100 € | aucun | 23 500 € ; 26 000 € | 0 € ; 0 € |
| 9. Abandon ou retard du projet artistique (A : DGX Spark avancé et 3 JP gratuites par mois sur deux mois) | 0 € ; 0 € | 0 € ; 0 € | 11 600 € ; 0 € | aucun | 15 400 € ; 27 000 € | 0 € ; 0 € |
| 10. Croissance commerciale plus lente (cadrage payé en février, lots à 1 750 € par mois, pas de second client) | 0 € ; 0 € | 0 € ; 0 € | 21 200 € ; 7 900 € | aucun | 12 300 € ; 25 300 € | 0 € ; 0 € |

Sources : `modele-financier/stress-tests.md:29-43` et le détail de chaque test (lignes 52 à 335). Un besoin de 0 € ne veut pas dire « sans gravité » : l'apport et le coussin du pilote absorbent le choc, au prix du revenu des associés ou de la réserve.

### 9.3 Engagements devenus intenables et protections

| Test | Engagements devenus intenables | Protection [PR] |
| --- | --- | --- |
| 1. Retards | Payer les associés à date fixe ; lancer un nouveau lot ; tout nouveau frais. **À 60 jours et plus, le contrat lui-même** | Relance le lendemain ; suspension à J+8 après relance ; résiliation possible à 30 jours ; pénalités et 40 € ; socle d'avance ; rémunération seulement sur encaissements |
| 2. Rupture | Frais de 2 000 € par mois ; toute rémunération ; tout engagement de plus de trois mois ; le revenu des associés tiré de Marwin | Préavis d'un mois et mois en cours dû ; acompte et solde à la livraison ; frais ramenés à ≈ 1 000 € ; abonnements résiliables au mois ; revenus extérieurs |
| 3. Non-renouvellement | Rémunération régulière ; frais de 2 000 € ; dépendance à un seul client | Pas de tacite reconduction ; renouvellement écrit un mois avant ; prospection de 1,5 à 2,5 JP par mois dès le mois 1 |
| 4. Dépassement | 2 000 à 2 500 € de temps non payé ; un pilote livré en retard compromet la suite | Provision de 10 à 15 % ; jalon au-delà de 8 JP ; avenant signé **avant** le travail |
| 5. Coûts d'IA | À +1 000 € par mois, l'enveloppe tombe de 4 700 € à 3 800 € (≈ 300 € nets de moins par associé) | Plafond de consommation ; deux fournisseurs ; modèle moins cher par défaut ; outils du client à sa charge |
| 6. Indisponibilité | Lots promis pendant l'absence ; contrôle à quatre yeux | Binôme de secours ; passage au palier B0 sans pénalité au-delà de 10 jours ouvrés ; prévoyance |
| 7. Urgences | Plafond de 10 JP et occupation ≤ 85 % (charge portée à 11,9 JP) | Liste fermée ; arrêt sans autorisation ; tout travail en plus par avenant à 900 € HT par JP |
| 8. Fournisseur | Engagements de service du socle ; réversibilité sans exports testés | Exports mensuels testés ; mode manuel écrit ; comptes au nom du client |
| 9. Projet artistique | Toute avance de matériel ou de temps sans financeur écrit | Rien d'exploratoire sans financeur ; achats au nom du client |
| 10. Croissance lente | La rémunération centrale : l'enveloppe tombe à 3 300 € par mois, soit 900 à 1 000 € nets par associé ; la cible de dépendance | Dates butoirs du 15 déc. 2026 et du 31 janv. 2027 ; prospection ; revenus extérieurs |

Sources : `modele-financier/stress-tests.md:69-335` ; `travaux/strategie-retenue.md:463-465, 524-537`.

**Une remarque sur la prévoyance** [FV pour la règle] : en SAS, un dirigeant non rémunéré ne cotise pas et n'a aucun droit (`travaux/syn-droit.md:111`). Pendant les mois 1 à 3, une maladie d'un associé n'est donc couverte par rien qui vienne de Marwin.

### 9.4 Ce que montrent les tests

1. **Le pire cas sans réaction est la rupture à la fin du pilote** : besoin de 21 300 €, trésorerie négative dès juin 2027. Avec la règle, le besoin tombe à 1 700 €, dont 1 600 € de crédit de TVA qu'un remboursement demandé à temps couvrirait (`modele-financier/stress-tests.md:340-342`).
2. **La protection principale n'est pas la réserve.** Au mois 3, la réserve de 10 % ne vaut que 2 000 € (`modele-financier/tresorerie-18-mois.md:100`), loin des six mois de frais réduits que la stratégie lui demande de couvrir (`travaux/strategie-retenue.md:529`). Ce qui protège, c'est **« pas de rémunération sans encaissement »**, la baisse rapide des frais et le surplus du pilote (`modele-financier/stress-tests.md:341`).
3. **Ces règles reportent le choc sur le revenu des associés.** Morgan et Mathys doivent garder d'autres revenus au moins jusqu'au deuxième renouvellement du socle (`modele-financier/stress-tests.md:343` ; `travaux/strategie-retenue.md:771`).
4. **Un retard durable de 60 ou 90 jours n'est pas un cas réel sous le contrat retenu** : la suspension à J+8 et la résiliation possible à 30 jours l'arrêtent avant. Le modèle reste plus indulgent que la stratégie, puisque sa règle B ne fait que décaler la rémunération sans suspendre le travail. En pratique, ces deux tests se lisent comme une rupture.
5. **Le projet artistique est sans effet** tant qu'il reste hors du CA et qu'aucune avance n'est faite ; il redevient le premier risque si Marwin avance du matériel ou du temps (`modele-financier/stress-tests.md:344`).
6. **Les chocs ne sont pas cumulés.** Un retard pendant une absence, ou une rupture après un dépassement, aggraverait les besoins (`modele-financier/stress-tests.md:349`).

---

## 10. Besoin de financement

| Besoin | Montant [ES] | Source |
| --- | --- | --- |
| Démarrage payé avant tout encaissement (central) | 6 000 € HT, soit ≈ 7 200 € TTC | `modele-financier/tresorerie-18-mois.md:114` |
| Apport minimal pour que la trésorerie reste positive dans la base | ≈ 6 900 € | `modele-financier/tresorerie-18-mois.md:25` |
| Apport retenu (central) | 10 000 € ; point bas de 3 100 € | `modele-financier/tresorerie-18-mois.md:25` |
| Si l'assurance est payée d'avance (prime de 2 400 à 3 000 € par an) | Point bas de 700 à 100 € ; pour garder un mois de frais en caisse (≈ 2 200 €), apport d'environ 12 000 € [ES, ce livrable] | `modele-financier/tresorerie-18-mois.md:135` |
| Chocs, avec la règle de protection | 0 à 1 700 € (dont 1 600 € de crédit de TVA remboursable) | `modele-financier/stress-tests.md:342` |
| Chocs, sans réaction | Jusqu'à 21 300 € (rupture à la fin du pilote) | `modele-financier/stress-tests.md:34` |
| Arrêt après le cadrage, frais non arrêtés (prudent) | −10 300 € de trésorerie au mois 12, sur un apport de 8 000 € | `modele-financier/scenarios.md:205` |

**Recommandation** [PR, ce livrable, dans la fourchette de la stratégie de 8 000 à 14 000 € (`travaux/strategie-retenue.md:172`)] :
- financer le démarrage par l'apport seul (capital entièrement libéré et comptes courants), **déposé avant toute dépense de la phase 0** ;
- viser 10 000 € si la prime d'assurance est fractionnée au mois, ≈ 12 000 € sinon ;
- aucun prêt bancaire n'est nécessaire dans le plan ; ne pas en prendre pour payer des rémunérations ;
- aucun argent de GianLuca : un acompte n'est ni du capital ni un prêt (`interne/offre-marwin-tech-remuneration-et-collaboration.md:142`), et l'investisseur n'est pas un sujet avant 12 à 24 mois (`travaux/strategie-retenue.md:632`) ;
- aucune aide comptée (ACRE, ARE, ARCE, FRR, aide régionale) (`travaux/strategie-retenue.md:564`).

**Limite.** L'existence de l'apport est [IN] : la stratégie juge « moyenne » la probabilité qu'il n'existe pas (`travaux/strategie-retenue.md:776`), au vu d'une domiciliation résiliée faute de 144 € et d'abonnements en échec de prélèvement (`travaux/note-point-4-novembre-et-activites.md:6, 8`). Sans apport : ramener les sorties de la phase 0 au conseil sur la fuite et aux statuts, et décaler le reste après l'acompte du cadrage (`travaux/strategie-retenue.md:776`). Le conseil sur la fuite concerne un traitement antérieur à Marwin : s'il n'est pas repris par la société, il reste à la charge personnelle des associés, sans TVA récupérable (`modele-financier/tresorerie-18-mois.md:143`).

---

## 11. Ce qu'il ne faut pas prétendre savoir sur la façon dont GianLuca paiera

Aucune pièce ne rapporte une parole directe de GianLuca Carlone [FV négatif] (`travaux/syn-sources.md:38`). Ne pas écrire, ne pas supposer, ne pas modéliser comme acquis :

| Ce qu'on ignore | Code | Pourquoi c'est important | Source |
| --- | --- | --- | --- |
| Quelle entité signe, paie et valide ; une seule ou une par projet | [IN] | Sans entité, aucune facture ; chaque entité a son bon de commande | `travaux/strategie-retenue.md:33, 726` |
| Ses délais et son mode de paiement habituels | [IN] | Le calendrier retenu est une proposition à négocier, pas une hypothèse sur sa trésorerie | `travaux/strategie-retenue.md:467, 728` |
| Si son entité récupère la TVA | [IN] | Sinon, la TVA est un coût réel pour lui : le cadrage lui coûte 7 800 € TTC | `travaux/strategie-retenue.md:462` |
| Son budget pour ce type de prestation | [IN] | Les « vingt jours par mois » sont attribués tantôt au client, tantôt à Morgan | `travaux/syn-sources.md:38` |
| Sa trésorerie disponible | [IN] | Des rachats de bâtiments ou d'une galerie [DR] (`interne/contexte-projet-carlone.md:24` ; `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:14`) ne prouvent pas une trésorerie. « Un patrimoine déclaré n'est pas une trésorerie » | `travaux/strategie-retenue.md:566` ; `travaux/DEMANDE.md` § 3 |
| Son intention d'investir | [DR] | Ce n'est pas un paiement. Ne jamais échanger une baisse d'honoraires contre une promesse d'investissement | `interne/contexte-projet-carlone.md:24` ; `interne/offre-marwin-tech-remuneration-et-collaboration.md:149` |
| Les bureaux proposés | [DR] | Ce n'est pas une rémunération ; un paiement en bureaux, en emploi ou en capital est refusé | `interne/offre-marwin-tech-remuneration-et-collaboration.md:132` ; `travaux/strategie-retenue.md:703` |
| L'aide régionale au conseil (50 % jusqu'à 15 000 € sur deux ans, dépôt avant signature, échéance annoncée au 31 déc. 2026) | [DR] ; éligibilité [IN] | Jamais comptée dans le modèle ; elle peut décaler la signature | `interne/offre-marwin-tech-remuneration-et-collaboration.md:175` ; `travaux/strategie-retenue.md:239` |
| S'il a vu le taux de 750 € ou la formule à 15 000 € | [IN] | Si oui, le cadrage peut descendre à 6 000 € HT | `travaux/strategie-retenue.md:401, 736` |
| Si la règle de rétractation s'applique | [HY] | Aucun paiement avant 7 jours ; démarrage reculé | `travaux/strategie-retenue.md:466` |

**Ce qu'on fait à la place** [PR] : poser la question 3 au rendez-vous (« Quel budget, quel mode et quel délai de paiement votre entité pratique-t-elle ? Récupère-t-elle la TVA ? ») (`travaux/strategie-retenue.md:728`) ; une fois l'entité nommée, consulter sans contact les registres publics (statut actif, dirigeant habilité, comptes déposés, procédures collectives) (`travaux/strategie-retenue.md:566`) ; ne jamais démarrer avant l'acompte. La préparation de ces questions est dans 13-preparation-rendez-vous.md.

---

## 12. Recommandations : preuve, hypothèse, limite, décision

| Recommandation | Preuve | Hypothèse | Limite | Décision correspondante |
| --- | --- | --- | --- | --- |
| Écrire au pacte « pas de rémunération sans encaissement » et la baisse des frais à ≈ 1 000 € en cas de rupture | Sans la règle, besoin jusqu'à 21 300 € ; avec, 1 700 € [ES] (`modele-financier/stress-tests.md:340-342`) | Les associés appliquent la règle | Le choc passe sur leur revenu personnel | Décisions 3 et 4 de `travaux/strategie-retenue.md:717-718` (accord écrit, pacte) |
| Déposer un apport de 10 000 € avant toute dépense, ≈ 12 000 € si l'assurance est payée d'avance | Point bas de 3 100 €, puis 700 à 100 € avec la prime [ES] (`modele-financier/tresorerie-18-mois.md:25, 135`) | Démarrage de 6 000 € HT ; prime de 2 400 à 3 000 € | Apport [IN] ; prime [IN] | Décision 4 (`travaux/strategie-retenue.md:718`) |
| Faire payer selon la nature de la prestation ; démarrer à l'encaissement | Contradiction des archives [FV] (section 4.1) ; travail impayé ≤ ≈ 6 000 € HT au lieu de ≈ 18 500 € HT [ES] | Le client accepte l'avance sur le temps réservé | Pratiques de paiement [IN] ; rétractation [HY] | Décisions 2 et 5 (`travaux/strategie-retenue.md:716, 719`) |
| Garder 750 € comme plancher interne et viser 800 à 950 € ; réviser au mois 6 sur le coût mesuré | Coût complet de 710 à 885 € à 10 JP [ES] ; prix réalisé ≈ 870 € ; à 750 €, ≈ 270 € nets de moins par associé [ES] | Coefficient 1,7 à 1,9 ; frais 1 500 à 2 500 € | Aucune simulation officielle | Décision 2 ; 04-catalogue-offres.md, section 5 |
| Annoncer aux associés ≈ 1 100 à 1 500 € nets en central (≈ 1 300 €), avant IR, rien avant le mois 4 | Modèle avec IS et délais (section 5.6) | Disponibilités 65 % et 50 % | IR [IN] ; partage entre associés non tranché | Décision 3 (rémunération cible acceptée) |
| Mesurer la réserve du mois 12 sur « réserve + trésorerie libre » ; passer à 12 % si le pilote est C2 ou C6 seul | 10 % seuls : 8 900 € pour 10 700 € visés (`modele-financier/scenarios.md:66`) | Le pilote est vendu | Coussin dépendant du pilote | Décision 5 (garde-fous) |
| Prendre des frais résiliables au mois ; fractionner la prime d'assurance | Variante basse : trésorerie négative dès juillet 2027 si les frais continuent (`modele-financier/scenarios.md:205`) | Les prestataires l'acceptent | Certains assureurs exigent une prime annuelle | Décision 4 |
| Garder des revenus extérieurs jusqu'au deuxième renouvellement du socle | ≈ 130 € nets par journée consacrée à Marwin [ES] ; dépendance à 100 % | Les autres activités restent compatibles avec le plafond de 10 JP | Occupation de Morgan sur tout son temps [IN] | Décisions 3 et 5 |
| Relancer le modèle en janvier 2027 avec l'expert-comptable, puis à chaque étape vendue | Coefficient d'une source secondaire ; lois de finances 2027 à venir (`modele-financier/scenarios.md:227`) | L'expert-comptable fournit une simulation officielle | Coût de l'expert-comptable dans les frais | Décision 4 |
| Ne rien supposer du paiement de GianLuca ; poser la question 3 ; vérifier les registres sans contact | Aucune parole directe [FV négatif] (`travaux/syn-sources.md:38`) | Un rendez-vous est obtenu avant le 15 déc. 2026 | Aucun rendez-vous fixé (`travaux/note-point-4-novembre-et-activites.md:5`) | Décision 5 ; 13-preparation-rendez-vous.md |

---

## 13. Relancer le modèle

**Ce qu'il faut** : Python 3, bibliothèque standard seulement ; aucune connexion, aucune action extérieure (`modele-financier/modele_financier.py:10-17`). Testé le 4 nov. 2026 avec Python 3.13.18 [MM].

**Commande recommandée**, depuis la racine du dépôt, en écrivant d'abord dans un dossier de travail :

```
python3 -I audit/2026-11-04-audit-strategique/annexes/modele-financier/modele_financier.py --sortie /chemin/vers/un/dossier-de-travail
diff -r /chemin/vers/un/dossier-de-travail audit/2026-11-04-audit-strategique/annexes/modele-financier --exclude=modele_financier.py
```

Sans `--sortie`, le script **écrase** les cinq fichiers placés à côté de lui (`scenarios.md`, `tresorerie-18-mois.csv`, `tresorerie-18-mois.md`, `stress-tests.md`, `structures.md`). Ne le faire qu'après avoir relu les écarts, en gardant une copie datée des anciennes sorties.

**Ce qu'il affiche** : « Contrôles de cohérence : tous passés », une ligne par scénario (CA, enveloppe, net SAS, IS, trésorerie disponible et libre au mois 12, seuil) et une ligne par test de résistance.

**Où changer une hypothèse** (en tête du script ; chaque paramètre porte son code et sa source) :

| Fait nouveau | Paramètre | Ligne |
| --- | --- | --- |
| Régime de TVA choisi (1 = réel normal mensuel) | `TVA_DECALAGE` | 73 |
| Date de clôture du premier exercice | `T_DEC_2027`, `T_PAIEMENT_IS_EX1` | 63, 65 |
| Taux 2027 (IS, cotisations, PASS) ou simulation officielle | `IS_TAUX_REDUIT`, `COEF_SAS`, `PASS`, `TNS_FORFAIT_DEBUT` | 78, 85, 93, 96 |
| Règles du pacte (réserve, premier mois rémunéré) | `RESERVE`, `MOIS_DEBUT_REMU` | 107, 108 |
| Un prix change | `PRIX` | 125 |
| Probabilités remplacées par les faits | `PROBA` | 153 |
| Devis d'assurance, de comptable ; lieu de résidence connu | `FRAIS_MONTANTS` | 178 |
| Coût réel du conseil sur la fuite, des statuts | `DEMARRAGE` | 188 |
| Apport réellement déposé | `APPORT` | 203 |
| Mois réel de l'acompte du cadrage ; disponibilités écrites | `SCENARIOS` (`t_m1`, `etp`, `capacite`) | 215 |
| Paramètres des tests | `STRESS` | 249 |

**Les contrôles qui arrêtent le script** (« CONTRÔLES EN ÉCHEC ») : identités de trésorerie et de TVA ; trésorerie disponible du central jamais négative ; CA de chaque scénario à moins de 10 % de la valeur de référence de la stratégie ; JP vendues sous la capacité et sous le plafond de 10 JP en central ; arrondis ; recoupement des cotisations TNS avec `travaux/syn-droit.md` à 2 % près ; règle B jamais pire que A (`modele-financier/modele_financier.py:1800-1878`). Deux exemples :
- un apport central de 6 000 € arrête le script (« central : trésorerie disponible négative dans la base ») [MM, essai du 4 nov. 2026 dans un dossier de travail] : c'est voulu, l'apport minimal est d'environ 6 900 € ;
- si la stratégie change ses prix, le contrôle du CA peut échouer : mettre alors à jour, sciemment, la référence `SCENARIOS[...]["strategie"]` (lignes 222, 231, 241) et le noter.

**Sources dans le script** : « audit-work/ » désigne `annexes/travaux/`. Le script abrège ses sources (par exemple une abréviation pour `travaux/strategie-retenue.md`) ; la table de correspondance est aux lignes 41 à 51 du script.

**Quand relancer** : en janvier 2027 avec l'expert-comptable (lois de finances 2027, régime de TVA, date de clôture, coefficient officiel) (`modele-financier/scenarios.md:227`) ; après le devis de RC professionnelle ; après la fiche « rôles et disponibilités » ; après le rendez-vous (entité, délais de paiement) ; après la signature du cadrage (mois 1 réel, probabilités) ; au mois 6 (coût complet mesuré).

**Règle de diffusion** : toutes les sorties sont internes ; rien ne va à GianLuca Carlone (`modele-financier/modele_financier.py:6-8`).

---

## 14. Limites

- **Tout le chiffre d'affaires est une hypothèse** ; le plan n'est pas pondéré et suppose chaque étape vendue. La probabilité de vendre le cadrage est [IN] (`travaux/controle-modele.md:99`).
- **Coûts de Marwin non devisés** : assurance, déplacements, conseil, comptable [HY/IN]. Aucun coût de la fuite au-delà du conseil (sanction, réclamations, franchise) n'est chiffré [IN] (`modele-financier/scenarios.md:228, 231`).
- **Coefficient SAS** d'une source secondaire unique ; barème TNS « revenus 2025 » ; lois de 2027 à venir (`modele-financier/scenarios.md:227`).
- **Impôt sur le revenu non calculé** : tous les salaires sont avant IR.
- **Partage égal** entre associés dans le modèle, alors que la stratégie prévoit une grille liée au temps (section 7.2).
- **Pas de saisonnalité** (août, fêtes) ; les lots sont lissés (`travaux/controle-modele.md:107`).
- **Tests non cumulés** ; règle B des retards plus indulgente que le contrat retenu (section 9.4).
- **CFE non modélisée** ; montant [IN], couvert par la ligne « imprévus » (`modele-financier/tresorerie-18-mois.md:142`).
- **Calculs propres à ce livrable** (net par JP et par journée, partage selon le temps, apport de 12 000 €, sensibilité au taux de 750 €, réserve à 12 %, marges en %) : [ES], non contrôlés par un tiers.
- **Diaporama client** cité d'après sa copie du 4 nov., hors dépôt.

---

## Renvois

- Offres, prix, planchers, marges, sort des éléments des archives : 04-catalogue-offres.md.
- Capacité, occupation, seuils de saturation : 06-fonctionnement-a-deux.md.
- Calendrier d'action et budget à 90 jours : 08-feuille-de-route.md.
- SAS ou SARL, pacte, rôles de GianLuca : 10-structures-et-relations.md.
- Proposition remise au client : 11-proposition-commerciale-revisee.md ; pour-gianluca/proposition-de-cadrage.md.
- Clauses de paiement, de suspension, de sortie : 12-gouvernance-contrat-sortie.md.
- Questions sur le paiement au rendez-vous : 13-preparation-rendez-vous.md.
- Risques financiers et inconnues : 14-registre-risques-inconnues-decisions.md.
- Alternative du salariat et conditions de refus : 15-contre-analyse.md.
