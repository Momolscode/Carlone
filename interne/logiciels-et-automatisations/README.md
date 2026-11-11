# Logiciels et automatisations : guide du dossier interne

Marwin Tech × GianLuca Carlone · dossier « logiciels et automatisations » · guide · 9 novembre 2026
Statut : **interne** (ne pas transmettre à GianLuca Carlone). Le dossier contient le nom d'un concurrent, des planchers, des marges et la capacité des associés.
Sources : les fichiers listés ci-dessous ; `audit/2026-11-04-audit-strategique/annexes/travaux/strategie-retenue.md` (STRAT) ; `audit/2026-11-04-audit-strategique/interne/2026-11-09-mise-a-jour-faits-nouveaux.md` (MAJ).
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ; [MM] mesuré ; [IN] inconnu. JP : journée-personne de 7 h. Chemins depuis la racine du dépôt.

---

## À quoi sert ce dossier

Le 9 nov. 2026, Morgan a rapporté que GianLuca parle d'un « logiciel de gestion de propriété » et qu'une société « Accord » lui propose « 6 000 € par mois tous les trimestres » [DR]. Morgan estime qu'on peut « faire mieux et moins cher grâce à l'IA » [DR]. Ce dossier éprouve cette position, chiffre trois façons de faire et prépare les documents client correspondants, sans contact ni envoi.

## Les fichiers

| Fichier | Contenu | Statut | Date |
| --- | --- | --- | --- |
| `interne/logiciels-et-automatisations/2026-11-09-etude-gestion-proprietes-offre-accord-et-prix.md` | **L'étude de référence** : ce que l'on sait de l'offre « Accord » et ses deux lectures du prix ; trois sens et neuf modules ; options A, B et C chiffrées sur trois ans ; lots L0 à L5 et maintenance ; capacité sous 10 JP ; verdict ; recommandation ; risques juridiques de la comparaison ; décisions DL1 à DL13 ; mise en cohérence du dossier (section 8) | Interne | 9 nov. |
| `interne/logiciels-et-automatisations/travaux/r1-marche-et-offre-accord.md` | Travail R1 : identité d'« Accord » (non trouvée) ; prix publics des logiciels du marché ; ce que 24 000 ou 72 000 € par an achètent ; effet mesuré de l'IA sur le développement | Interne ; travail préparatoire | 9 nov. |
| `interne/logiciels-et-automatisations/travaux/r2-cadre-reglementaire-et-technique.md` | Travail R2 : facturation électronique, baux commerciaux, ERP, hébergement touristique, caisse, RGPD, règlement sur l'IA ; exigences techniques minimales | Interne ; travail préparatoire | 9 nov. |
| `interne/logiciels-et-automatisations/travaux/r3-faits-internes.md` | Travail R3 : faits du dépôt utiles à l'offre (lieux, offres du catalogue, capacité, CRM, règles de l'audit) | Interne ; travail préparatoire | 9 nov. |

R1 à R3 gardent leur propre découpe en modules ; une note ajoutée à la fin de chacun donne la correspondance avec les neuf modules de la spécification. **En cas de différence, l'étude fait foi** [PR].

**Projets client liés** (dans `pour-carlone/logiciels-et-automatisations/`, voir son README) : la proposition « Votre logiciel de gestion des propriétés », l'annexe de spécification, « Logiciels sur mesure : notre méthode et vos garanties » et « Automatisations : fiches détaillées ». Tous sont des **projets non envoyés**, à valider par écrit par Morgan et Mathys.

## Ordre de lecture

1. **Étude, « En bref »** (dix points), puis **section 8** (ce qui a été mis en cohérence le 9 nov. au soir).
2. **Étude, section 7** : les treize décisions DL1 à DL13, avec leurs dates (du 9 nov. 2026 au 29 janv. 2027).
3. **Étude, sections 4 et 5** : verdict sur « mieux et moins cher grâce à l'IA », recommandation, comment en parler sans dénigrer.
4. **Les quatre projets client**, dans l'ordre de leur README : proposition, annexe de spécification, méthode et garanties, fiches d'automatisation.
5. **Étude, sections 2, 3 et 6, et annexe A** pour vérifier un chiffre ou un point juridique ; **R1 à R3** pour remonter à la source.

## Chiffres retenus après la mise en cohérence [PR, étude, sections 3.5, 3.6 et 5.1]

| Élément | Prix HT | Condition |
| --- | ---: | --- |
| Cadrage général | 6 500 € | Inchangé ; seule proposition commerciale (STRAT:42) |
| L0 Choix des briques (facultatif) | 3 000 € | Seulement ce que le cadrage ne fait pas |
| L1 Essai sur données fictives | 5 300 € | Logiciel choisi comme priorité |
| L2 Pilote sur un bâtiment et un lieu | 10 400 € | Règle de la stratégie, sans gain d'IA (DL5) |
| Première étape | 15 700 € ; 18 700 € avec L0 | — |
| L3 Raccordements et finances ; L4 Tableau de bord et assistant ; L5 extension | 7 500 € ; 6 400 € ; 1 200 € | Après le bilan du pilote |
| Option hôtellerie | 2 300 € | Si un hébergement reprend |
| Maintenance après le pilote ; après L4 | 700 à 1 000 € par mois (DL6) ; 1 200 € par mois | Au plus tôt en juillet 2027 |
| Coût sur trois ans pour GianLuca, hors cadrage et temps de l'administratrice [ES] | 46 300 à 68 500 € (B réduite) ; 79 000 à 97 700 € (B complète) | À comparer à 72 000 € (lecture b) ou 216 000 € (lecture a) |

**Verdict** [ES, étude, section 4] : « moins cher » est vrai contre la lecture (a), **non démontré à périmètre égal** contre la lecture (b) ; « mieux » n'est pas démontré ; « grâce à l'IA » est faux tel quel : l'économie vient de l'architecture (acheter, configurer, relier), pas de l'IA.

## Règles du dossier

- **Rien ne part** avant D03 et D08 et l'accord écrit des deux associés (MAJ:370) [PR] ; aucune contre-offre ni aucun chiffre donné avant la proposition écrite de l'autre prestataire (DL1).
- **Jamais le nom « Accord »** ni une critique d'une autre offre dans un document client ; toute comparaison écrite relue par l'avocat (DL9) [PR].
- **Ni contact, ni compte, ni essai, ni achat** : ce dossier n'a contacté personne ; hors des deux dossiers `logiciels-et-automatisations/` (interne et client), il n'a modifié qu'un fichier existant, `README.md` à la racine, d'une ligne par dossier [MM]. La présentation du 9 nov. n'est pas modifiée.
- Le client s'appelle **GianLuca Carlone**.

Relu et contrôlé : 9 novembre 2026 — chemins relatifs à la racine du dépôt ; prénom du client vérifié ; chiffres repris de l'étude après mise en cohérence.

[Mention du 11 novembre 2026 : quatre notes du 10 novembre complètent ce dossier : choisir un logiciel hôtelier (`interne/logiciels-et-automatisations/2026-11-10-choisir-un-logiciel-hotelier.md`) ; connexion aux sites de réservation (`…/2026-11-10-connexion-airbnb-booking-et-autres-sites.md`) ; construire nous-mêmes (`…/2026-11-10-construire-nous-memes-le-logiciel-des-suites.md`) ; questions sur l’autre proposition (`…/2026-11-10-questions-a-poser-et-comparaison-a-refaire.md`). Pour les neuf suites, elles l’emportent sur l’étude.]
