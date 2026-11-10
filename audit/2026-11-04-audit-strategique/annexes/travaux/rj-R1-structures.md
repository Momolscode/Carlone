# R1-structures : SAS ou SARL pour Marwin Tech (droit et barèmes en vigueur au 4 novembre 2026)

Mémo du chercheur « R1-structures », rédigé le 4 novembre 2026 pour l'audit Marwin Tech × GianLuca Carlone. Toutes les pages web citées ont été consultées le **4 nov. 2026**. Aucun contact extérieur, aucune démarche, aucune modification du dépôt `Momolscode/Carlone`.

Codes utilisés : **[FV]** fait vérifié sur source primaire ; **[DR]** déclaration rapportée (pièce du dépôt ou source secondaire non recoupée) ; **[PR]** proposition ; **[HY]** hypothèse ; **[ES]** estimation ou simulation non validée ; **[MM]** mesure ; **[IN]** inconnu.

Abréviations de pièces internes : **CS p. N** = `interne/archives-marwin-tech/choix-structure-2026-10-29.pdf` p. N ; **V5 p. N** = `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. N ; **C3:ligne** = `audit-work/ex-C3-structure.md:ligne` (extraction du lecteur C3) ; **note-4-nov:ligne** = `audit-work/note-point-4-novembre-et-activites.md:ligne`.

---

## 0. Limites de ce mémo (à lire d'abord)

1. **Pages Urssaf inaccessibles.** Les pages urssaf.fr renvoyaient une erreur HTTP 503 le 4 nov. 2026 (taux et barèmes, « Choisir votre statut juridique »). Les règles Urssaf sont donc citées via entreprendre.service-public.gouv.fr (DILA), via des extraits de moteur de recherche signalés comme tels, ou via le **modèle de calcul officiel de l'Urssaf** (`modele-social` v11.1.0 publié le 16 juill. 2026, règles Publicodes de mon-entreprise.urssaf.fr, lu comme données : date de référence 01/07/2026). Le moteur de calcul lui-même n'a pas été exécuté dans cette session.
2. **Pas de simulation officielle.** Les chiffres des sections 1 et 13 sont des **[ES]** calculées par ce chercheur avec un barème simplifié (taux publiés par service-public, voir § 1). Ils donnent des ordres de grandeur, pas des montants à budgéter. **Simulateurs officiels à utiliser** : https://mon-entreprise.urssaf.fr/simulateurs/sasu (président de SAS), https://mon-entreprise.urssaf.fr/simulateurs/ind%C3%A9pendant (gérant majoritaire, URL reprise de V5 p. 22, non rouverte), https://mon-entreprise.urssaf.fr/simulateurs/dividendes (dividendes ; selon l'extrait de recherche, ce simulateur **ne couvre pas** les gérants majoritaires de SARL) et le comparateur de statuts de mon-entreprise (URL non vérifiée).
3. **Impôt sur le revenu non calculé.** Les situations fiscales personnelles de Morgan Olsen et de Mathys Couet sont **[IN]** (V5 p. 18 suppose un foyer d'une part sans autre revenu, hypothèse non confirmée).
4. **Textes en discussion.** Le PLF et le PLFSS pour 2027 ont été déposés début octobre 2026. Une synthèse secondaire du 1er oct. 2026 (legifiscal.fr, signalée comme source secondaire) n'y relève aucune mesure sur le taux réduit d'IS des PME, les dividendes, la micro-entreprise, l'ACRE ou les cotisations des indépendants. **[IN]** : état des amendements au 4 nov. 2026 non vérifié ; toute règle ci-dessous peut changer au 1er janvier 2027.

---

## 1. Statut social des dirigeants et cotisations 2026

### Réponse courte
- **SAS** : le président (et un directeur général rémunéré) est **assimilé salarié** : régime général, **sans assurance chômage**. S'il n'est pas rémunéré, il ne cotise pas et n'a pas de protection liée au mandat. **[FV]**
- **SARL avec Morgan et Mathys cogérants à 50/50** : leurs parts s'additionnent ; le « collège de gérance » détient 100 % → **tous deux travailleurs non salariés (TNS)**. Le 50/50 ne fait **pas** une gérance égalitaire. **[FV]**
- **SARL à gérance égalitaire au sens strict** : un **seul** gérant détient 50 % (l'autre associé n'est pas gérant) → le gérant est **assimilé salarié** ; l'associé non gérant n'a pas de statut social du fait de ses parts. **[FV]**
- **Ordre de grandeur des charges sociales** à coût identique : TNS ≈ **40 à 46 % du net perçu** ; assimilé salarié ≈ **70 à 85 % du net perçu**. **[ES]** À même enveloppe, le TNS laisse environ **15 à 20 % de net en plus** avant impôt sur le revenu, contre une protection sociale moindre (retraite complémentaire, indemnités journalières). **[ES]**
- **Minimum TNS** : environ **1 250 € par an** même sans rémunération **[ES]**. **Forfaits de début d'activité 2026** : environ **3 470 € par an**, avant régularisation **[FV]**. Le président de SAS non rémunéré : 0 €. **[FV]**

### Détail

**a) Qui relève de quel régime ?**
- La SARL : gérant majoritaire = TNS affilié à la sécurité sociale des indépendants ; gérant minoritaire = régime général, « assimilé à un salarié » [FV] (F37411, vérifié le 6 févr. 2026).
- Le président de SAS « ne cotise pas pour l'assurance chômage à laquelle il n'a pas droit » [FV] (F36065) ; « un dirigeant rémunéré uniquement en dividendes ne cotise pas et n'est pas protégé socialement » [FV] (F37366, vérifié le 6 févr. 2026).
- **Cogérance** : selon l'Urssaf (extrait de moteur de recherche, page non ouvrable), « le gérant majoritaire ou le collège de gérance majoritaire (détention de plus de 50 % des parts entre les gérants) sont travailleurs indépendants » et « le gérant minoritaire ou égalitaire (détention d'au plus 50 % des parts) est assimilé salarié » [DR]. La Cour de cassation l'a confirmé : les membres d'un collège de gérance majoritaire relèvent du régime des indépendants même si aucun ne détient seul plus de la moitié (Cass. civ. 2, 31 mai 2018, n° 17-17.518, publié) [FV, via Légifrance]. Les parts du conjoint, du partenaire de Pacs et des enfants mineurs sont additionnées [FV] (Bpifrance Création, ci-dessous).
- La pièce interne du 29 octobre le dit déjà dans un encadré : « 50/50 ne veut pas dire gérance égalitaire à deux » (CS p. 2) [FV] ; mais son tableau principal (« assimilé salarié si minoritaire ou égalitaire », CS p. 2) peut induire en erreur (C3:251).

**b) Taux TNS 2026 publiés par l'administration** (F38152, « Vérifié le 08 octobre 2026 ») [FV]
- Assiette : revenu professionnel **avant** cotisations, **diminué d'un abattement forfaitaire de 26 %** (réforme de l'assiette appliquée pour la première fois à la régularisation des revenus 2025 déclarés en 2026 — **changement 2025-2026** ; voir aussi la page Urssaf « Réforme de l'assiette sociale », citée via moteur de recherche [DR]).
- Maladie-maternité (revenus 2025) : 0 % sous 9 612 €, puis taux progressif jusqu'à 6,50 % à 52 866 €, 7,70 % à 96 120 €, 8,50 % à 144 180 € ; indemnités journalières 0,50 %.
- Retraite de base : 17,87 % jusqu'à 48 060 € (plafond de la sécurité sociale, PASS 2026), 0,72 % au-delà. Retraite complémentaire : 8,1 % jusqu'à 48 060 €, 9,1 % de 48 060 à 192 240 €.
- Invalidité-décès : 1,30 % jusqu'à 48 060 €. Allocations familiales (2026) : 0 % sous 52 866 €, progressif jusqu'à 3,10 % à 67 284 €.
- CSG-CRDS (2026) : 9,70 % sur les revenus professionnels. Formation professionnelle : 120 € (0,25 % du PASS).
- **Années de création** : montants forfaitaires pour un début d'activité en 2026 : maladie 96 €, retraite de base 1 631 €, retraite complémentaire 739 €, invalidité-décès 119 €, CSG-CRDS 886 € (total ≈ 3 471 €, plus la CFP), puis **régularisation** sur le revenu réel. Ce décalage crée un risque de trésorerie en année 2.
- Attention : la page présente des taux maladie et retraite « revenus 2025 » ; les taux définitifs applicables aux revenus 2026 n'y sont pas distingués → **[IN]** (probablement identiques, à confirmer sur urssaf.fr).

**c) Minimum TNS sans rémunération** [ES]
Le modèle Urssaf v11.1.0 retient des assiettes minimales : retraite de base sur 450 heures de SMIC (12,02 € au 1er janv. 2026), invalidité-décès sur 11,5 % du PASS, indemnités journalières sur 40 % du PASS, plus la CFP. Calcul de ce chercheur : 0,1787 × 450 × 12,02 + 0,013 × 5 527 + 0,005 × 19 224 + 120 ≈ **1 255 € par an et par gérant**. Pas d'assiette minimale si bénéficiaire du RSA ou de la prime d'activité (modèle Urssaf) [DR].

**d) Assimilé salarié**
Bpifrance Création (établissement public, **source secondaire signalée**) : charges ≈ « 80 % de la rémunération nette versée au dirigeant, soit 60 % de sa rémunération brute » ; pour un TNS, charges ≈ « 50 % du revenu d'activité indépendante » [DR]. Les taux détaillés 2026 du régime général pour un mandataire social n'ont pas pu être relevés sur urssaf.fr → **[IN]**. Hypothèse retenue ci-dessous : coût total = **1,70 à 1,85 fois le net** avant IR [HY]. Le mandataire n'étant pas couvert par l'assurance chômage, il ne bénéficie pas, selon la pratique, de la réduction générale des cotisations patronales — **[IN]**, à faire confirmer par l'expert-comptable.

**e) Protection sociale** (F38152) [FV]
- TNS : indemnité journalière maladie = 1/730 du revenu annuel moyen, plafond 65,84 €, carence de 3 jours ; retraite de base et complémentaire des indépendants ; invalidité-décès.
- Assimilé salarié : indemnité journalière = 50 % du salaire journalier de base, plafond 41,95 € ; retraite de base et complémentaire du régime général.
- Aucun des deux statuts n'ouvre droit à l'assurance chômage au titre du mandat (F36065 ; F37366) [FV]. La couverture des accidents du travail des TNS n'a pas été vérifiée → **[IN]**.

**f) Ordres de grandeur pour deux dirigeants à parts égales** [ES]
Hypothèses identiques pour toutes les formes [HY] : frais hors dirigeants = 1/6 du CA (20 000 / 30 000 / 60 000 €, cohérent avec les 30 000 € de V5 p. 18 à 180 000 €) ; tout le reste est affecté aux deux dirigeants ; pas d'ACRE ; pas de réserve sauf ligne A2 ; IR non déduit sauf sur les dividendes (PFU). Méthode : barème F38152 appliqué à 74 % du coût total (TNS) ; coefficient 1,70 à 1,85 (SAS).

| CA HT annuel | Disponible pour les 2 dirigeants | A. SARL cogérance 50/50 (TNS), tout en rémunération : net avant IR par personne | A2. Idem avec 10 % du CA mis en réserve (réserve après IS) | B. SAS, tout en salaire : net avant IR par personne | C. SAS, 2 000 €/mois nets chacun + dividendes après IS et PFU 31,4 % : total par personne |
|---|---|---|---|---|---|
| 120 000 € | 100 000 € | ≈ 34 000 € (charges ≈ 15 800 €, ≈ 46 % du net) | ≈ 30 300 € (réserve ≈ 10 200 €) | ≈ 27 000 à 29 400 € | ≈ 27 300 à 29 400 € |
| 180 000 € | 150 000 € | ≈ 51 400 € (charges ≈ 23 600 €) | ≈ 44 700 € (réserve ≈ 15 300 €) | ≈ 40 500 à 44 100 € | ≈ 41 200 à 43 100 € |
| 360 000 € | 300 000 € | ≈ 107 000 € (charges ≈ 43 000 €, ≈ 40 % du net) | ≈ 93 400 € (réserve ≈ 30 600 €) | ≈ 81 100 à 88 200 € | ≈ 79 800 à 81 600 € |

Lecture : la colonne C mélange un salaire **avant** IR et des dividendes **après** IR (PFU) ; elle n'est donc pas directement comparable aux colonnes A et B. Contrôle de cohérence : à 180 000 € de CA, la pièce V5 donne 43 875 € « net annuel par personne » en SARL à l'IS avec IR déduit (foyer d'une part) (V5 p. 18 ; C3:62) ; le net avant IR de ≈ 51 400 € trouvé ici est compatible avec un IR de l'ordre de 7 500 € **[ES]**.

### Sources officielles
- entreprendre.service-public.gouv.fr, DILA, « Protection sociale du dirigeant », https://entreprendre.service-public.gouv.fr/vosdroits/F38152 — « Vérifié le 08 octobre 2026 » — taux, abattement de 26 %, forfaits de début d'activité, indemnités journalières.
- entreprendre.service-public.gouv.fr, DILA, « SARL : ce qu'il faut savoir », https://entreprendre.service-public.gouv.fr/vosdroits/F37411 — « Vérifié le 06 février 2026 » — gérant minoritaire « assimilé à un salarié ».
- entreprendre.service-public.gouv.fr, DILA, « SAS : ce qu'il faut savoir », https://entreprendre.service-public.gouv.fr/vosdroits/F37366 — « Vérifié le 6 février 2026 ».
- entreprendre.service-public.gouv.fr, DILA, « Revenus du dirigeant », https://entreprendre.service-public.gouv.fr/vosdroits/F36065 — la date affichée relevée est « Vérifié le 26 avril 2024 », alors que la page cite le PFU de 31,4 % (règle de 2026) : **incohérence à revérifier** — « il ne cotise pas pour l'assurance chômage à laquelle il n'a pas droit ».
- Légifrance, Cour de cassation, 2e civ., 31 mai 2018, n° 17-17.518, https://www.legifrance.gouv.fr/juri/id/JURITEXT000037042970/ — lu via extrait de recherche (collège de gérance majoritaire → indépendants).
- Urssaf, « Choisir votre statut juridique », https://www.urssaf.fr/accueil/choisir-forme-juridique/creer-societe.html — **HTTP 503 le 4 nov. 2026**, contenu cité via extrait de moteur de recherche [DR].
- Bpifrance Création (source secondaire, établissement public), « Le statut social du dirigeant », https://bpifrance-creation.fr/encyclopedie/statut-du-dirigeant-son-conjoint/regime-social-du-dirigeant/statut-social-du-dirigeant — date non affichée — « 80 % de la rémunération nette […] soit 60 % de sa rémunération brute ».
- Urssaf / betagouv, modèle `modele-social` v11.1.0 (npm, publié le 16 juill. 2026), règles « dirigeant . régime social », « plafond sécurité sociale » (4 005 €/mois en 2026), « assiette minimale » — lu comme données.

### Incertitudes et points à faire valider
- Taux 2026 définitifs des indépendants et du régime général pour un mandataire (Urssaf, expert-comptable) **[IN]**.
- Rattachement de l'activité de Marwin (conseil, pilotage, intégration logicielle) : profession libérale non réglementée ou activité commerciale. Le régime social du gérant TNS n'en dépend plus beaucoup depuis 2019-2023, mais la catégorie fiscale et la micro-entreprise en dépendent (expert-comptable) **[IN]**.
- Validation de trimestres de retraite en SAS avec une faible rémunération : seuil non relevé **[IN]**.
- Couverture accidents du travail du TNS, prévoyance et mutuelle à souscrire (assureur, expert-comptable) **[IN]**.

### Conséquences pour Marwin Tech et GianLuca Carlone
- Si Morgan et Mathys veulent **deux cogérants à égalité**, la SARL les rend TNS : moins de charges, mais **cotisations minimales et régularisations** à provisionner même en cas de mois sans contrat. La SAS permet de ne pas se rémunérer pendant le démarrage sans cotisation (et sans protection).
- Une SARL « égalitaire » au sens strict ne donnerait le statut de gérant qu'à **un seul** des deux : asymétrie de pouvoir, et l'autre devrait être salarié avec un vrai lien de subordination (fragile pour un associé à 50 %) ou ne rien percevoir. Ce montage contredit l'idée d'un partenariat à égalité **[HY]**.
- Pour GianLuca Carlone, la forme est neutre sur le prix ; elle compte s'il veut entrer au capital (§ 9) ou si un salariat chez lui est envisagé (risque déjà signalé, C3:248).

---

## 2. Impôt sur les sociétés 2026

### Réponse courte
**25 %** de taux normal ; **15 %** jusqu'à **42 500 €** de bénéfice par période de douze mois, si le CA ≤ 10 M€ et si le capital est **entièrement libéré** et détenu de manière continue à **75 % au moins par des personnes physiques** [FV]. Seuil **inchangé** par la loi de finances pour 2026 (loi n° 2026-103 du 19 févr. 2026), même si un amendement visant 100 000 € a été voté en première lecture à l'Assemblée nationale fin 2025 [FV pour le texte en vigueur ; DR pour l'histoire de l'amendement].

### Détail
- Légifrance affiche l'article 219 du CGI « en vigueur depuis le 21 février 2026 », modifié par la loi n° 2026-103, art. 15 (V), applicable aux exercices clos à compter du 31 déc. 2025 ; le I b) maintient « 42 500 € de bénéfice imposable par période de douze mois » [FV]. La portée exacte de la modification de 2026 n'a pas été identifiée (vraisemblablement le calcul du chiffre d'affaires des groupes, voir l'actualité impots.gouv du 14 avril 2026 sur la décision du Conseil d'État du 13 mars 2025) **[IN]**.
- Le plafond s'apprécie « par période de douze mois » : pour un premier exercice plus long ou plus court (création fin 2026), il est ajusté au prorata [DR — règle BOFiP non rouverte].
- Exemples [ES] : bénéfice de 20 000 € → IS 3 000 € ; 60 000 € → 6 375 + 4 375 = 10 750 €.

### Sources officielles
- Légifrance, article 219 CGI, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868562 — version en vigueur depuis le 21 févr. 2026 — « dans la limite de 42 500 € de bénéfice imposable par période de douze mois ».
- entreprendre.service-public.gouv.fr, « Impôt sur les sociétés (IS) », https://entreprendre.service-public.gouv.fr/vosdroits/F23575 — « Vérifié le 17 février 2026 » — « un taux réduit fixé à 15 % peut s'appliquer pour la part des bénéfices allant jusqu'à 42 500 € ».
- impots.gouv.fr, actualité « Taux réduit d'IS : le critère du chiffre d'affaires revu pour les entreprises appartenant à des groupes », https://www.impots.gouv.fr/actualite/taux-reduit-dimpot-sur-les-societes-le-critere-du-chiffre-daffaires-revu-pour-les — 14 avril 2026.
- Secondaire signalé : hayot-expertise.fr (article du 17 mai 2026) : l'amendement à 100 000 € « n'a pas été retenu ».

### Incertitudes et points à faire valider
- Contenu exact de l'art. 15 de la loi n° 2026-103 (expert-comptable) **[IN]**.
- Prorata du plafond sur un premier exercice de plus de 12 mois (expert-comptable) [DR].
- Effet d'un éventuel amendement au PLF 2027 **[IN]**.

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Libérer tout le capital dès la constitution** (capital modeste) pour ne pas perdre le taux de 15 % : la libération partielle permise par le droit des sociétés (§ 7) priverait la société du taux réduit [FV + HY].
- Si GianLuca Carlone (ou une de ses sociétés) entre au capital, vérifier que la société reste détenue à **75 % au moins par des personnes physiques** (directement ou via des sociétés elles-mêmes détenues à 75 % par des personnes physiques) [FV].

---

## 3. Dividendes 2026

### Réponse courte
- **PFU : 31,4 %** = 12,8 % d'IR + **18,6 %** de prélèvements sociaux, pour les dividendes perçus depuis le **1er janvier 2026** (hausse de la CSG de 9,2 % à **10,6 %** par l'article 12 de la LFSS pour 2026, loi n° 2025-1403 du 30 déc. 2025) — **changement 2026** [FV]. Option possible pour le barème progressif (abattement de 40 %, CSG déductible de 6,8 %) [FV pour l'option ; abattement de 40 % cité par F36065].
- **SAS** et **gérant égalitaire ou minoritaire de SARL** : pas de cotisations sociales sur les dividendes [FV].
- **Gérant majoritaire de SARL (dont cogérants 50/50)** : la part des dividendes qui dépasse **10 %** du capital social, des primes d'émission et des sommes en compte courant détenus (avec conjoint, partenaire, enfants mineurs) est soumise aux **cotisations TNS** ; la part inférieure supporte les prélèvements sociaux [FV/DR].
- Aucune mesure de 2026 étendant ces cotisations aux présidents de SAS n'a été trouvée ; un amendement au PLFSS 2026 créant une contribution exceptionnelle sur les dividendes a été rejeté (scrutin n° 3446, source secondaire) [DR].

### Détail
- service-public : prélèvements sociaux 2026 sur dividendes : CSG 10,6 %, CRDS 0,5 %, prélèvement de solidarité 7,5 %, total 18,6 % ; PFU « au taux de 31,4 % (ou de 30 %) » ; certains produits (assurance vie, PEL, CEL) restent à 17,2 % [FV].
- Le modèle Urssaf v11.1.0 code la CSG non déductible au PFU à 10,6 % « si date >= 01/2026 » (9,2 % avant) [FV, données du modèle].
- Base des 10 % : la notice Urssaf des revenus 2026 inclut capital, primes d'émission et comptes courants ; F36065 ne cite que le capital social [DR, extrait de recherche]. Texte : art. L131-6 du code de la sécurité sociale [DR, non rouvert].
- Exemple [ES] : capital de 10 000 € détenu par les deux cogérants, aucun compte courant → seuil de 1 000 € de dividendes par an pour les deux ; au-delà, dividendes ≈ rémunération en coût social, après avoir déjà supporté l'IS. En SARL TNS, les dividendes ne sont donc pas un levier, sauf capital ou comptes courants importants.
- Calcul [ES] : 10 000 € de bénéfice distribué en SAS → IS 1 500 € → 8 500 € de dividende → PFU 2 669 € → **5 831 € nets** (58 % du bénéfice).

### Sources officielles
- service-public.gouv.fr, « Prélèvements sociaux (CSG, CRDS…) sur les revenus du patrimoine et de placements », https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 — « Vérifié le 30 juin 2026 » — cite la « Loi n° 2025-1403 du 30 décembre 2025 de financement de la sécurité sociale pour 2026 », « Article 12 (hausse de la CSG) ».
- entreprendre.service-public.gouv.fr, F36065 (voir § 1) — « à un taux global de 31,4 % » ; dividendes du gérant majoritaire exonérés de cotisations « dès lors qu'ils ne dépassent pas 10 % du capital social de la société ».
- Urssaf, « Déclaration de revenus 2026 des indépendants — notice explicative », https://www.urssaf.fr/files/live/sites/urssaffr/files/outils-documentation/formulaires-modeles/independant-notice-revenus-2026.pdf — lue via extrait de recherche [DR] — « 10% du montant du capital social, des primes d'émission et des sommes versées en compte courant d'associé ».
- Secondaire signalé : datan.fr, vote n° 3446 (amendement n° 173 rejeté, PLFSS 2026).

### Incertitudes et points à faire valider
- Calcul exact des 10 % (moyenne des comptes courants, date d'appréciation) et traitement social des dividendes du gérant majoritaire après la réforme de l'assiette (expert-comptable, Urssaf) [DR].
- Choix PFU ou barème selon chaque foyer (expert-comptable) **[IN]**.
- Mesures du PLFSS 2027 sur les dividendes **[IN]**.

### Conséquences pour Marwin Tech et GianLuca Carlone
- La SAS permet un mix « petit salaire + dividendes » ; en 2026 le PFU à 31,4 % (au lieu de 30 %) réduit un peu son intérêt. À 120 000 € de CA, il n'y a presque rien à distribuer après des salaires décents (§ 1, colonne C) [ES].
- Pour un investisseur (GianLuca Carlone), les dividendes de SAS ou de SARL suivent le même PFU s'il les perçoit personnellement ; via une société, le régime diffère (**[IN]**, à voir avec son conseil).

---

## 4. Option pour l'impôt sur le revenu (art. 239 bis AB CGI)

### Réponse courte
Une SAS ou une SARL **de moins de cinq ans** peut opter pour l'IR (régime des sociétés de personnes) pendant **cinq exercices** maximum, si : titres non cotés ; **≥ 50 %** du capital et des droits de vote détenus par des personnes physiques, dont **≥ 34 %** par des dirigeants ; activité professionnelle (pas de gestion de patrimoine) ; **< 50 salariés** ; CA ou total de bilan **< 10 M€** ; **accord de tous les associés** ; notification dans les **trois premiers mois** du premier exercice concerné. Une sortie anticipée interdit d'opter à nouveau [FV]. Aucun changement en 2025-2026 n'a été trouvé (version en vigueur depuis le 1er janv. 2019) [FV].

### Détail
- Effet : le bénéfice est imposé directement chez les associés, au barème. Pour un gérant majoritaire de SARL, sa quote-part supporte les cotisations TNS ; le traitement social de la quote-part d'un associé de SAS à l'IR n'a pas été vérifié **[IN]**.
- Les déficits éventuels des premières années remontent chez les associés : intérêt seulement s'ils ont d'autres revenus imposables **[HY]**.
- V5 p. 18 et p. 19 montrent que la SARL à l'IR n'est plus favorable **qu'avec** une exonération FRR (zone France Ruralités Revitalisation) non encore établie (C3:62 ; V5 p. 18) [ES/DR]. Le régime « SARL de famille » (option sans limite de durée) suppose des associés parents en ligne directe, frères et sœurs, conjoints ou partenaires de Pacs : lien entre Morgan et Mathys **[IN]**.

### Sources officielles
- Légifrance, article 239 bis AB CGI, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038586316 — version en vigueur au 04/11/2026, depuis le 1er janv. 2019 (loi n° 2019-486) — option notifiée « dans les trois premiers mois du premier exercice au titre duquel elle s'applique ».
- BOFiP, BOI-IS-CHAMP-20-20-20-20 (modalités et conséquences de l'option), https://bofip.impots.gouv.fr/bofip/4228-PGP.html/identifiant=BOI-IS-CHAMP-20-20-20-20-20140325 — commentaire de 2014, cité via extrait de recherche.

### Incertitudes et points à faire valider
- Traitement social de la quote-part de bénéfice d'un associé de SAS à l'IR (expert-comptable, Urssaf) **[IN]**.
- Articulation avec le dispositif FRR (art. 44 quindecies A) : rescrit préparé mais non envoyé (V5 p. 22 ; C3:76) [DR].

### Conséquences pour Marwin Tech et GianLuca Carlone
- Décision à prendre **avant la fin du troisième mois** du premier exercice, ce qui suppose un prévisionnel fiable dès la création [FV + HY].
- L'entrée de GianLuca Carlone au capital via une société, ou une dilution des fondateurs sous 34 %, ferait perdre l'option [FV].

---

## 5. ACRE en 2026 (réforme)

### Réponse courte
**Réforme 2026** : l'ACRE n'est plus automatique ni ouverte à tous. Depuis le **1er janvier 2026**, elle est réservée à des publics listés (demandeurs d'emploi indemnisés ; demandeurs non indemnisés inscrits plus de 6 mois sur 18 ; RSA ou ASS ; 18-25 ans ; moins de 30 ans sous conditions ; repreneurs d'entreprises en difficulté ; titulaires d'un CAPE ; création en **QPV ou en zone FRR / FRR+** ; bénéficiaires de la PreParE) et doit être **demandée à l'Urssaf dans les 60 jours** suivant le début d'activité ; l'Urssaf répond en 30 jours, son silence vaut accord [FV]. Pour un dirigeant de société (TNS ou assimilé salarié) : exonération de **25 %** des cotisations maladie-maternité, retraite de base, invalidité-décès et allocations familiales pendant **12 mois** si le revenu ≤ **36 045 €** (75 % du PASS), dégressive jusqu'à **48 060 €**, nulle au-delà [FV]. Micro-entrepreneurs : taux de 25 % pour les créations depuis le **1er juillet 2026** [FV].

### Détail
- Contrôle effectif de la société exigé pendant **au moins 2 ans** : plus de 50 % du capital (dont 35 % à titre personnel) ; **ou** être dirigeant avec au moins un tiers du capital (dont 25 % à titre personnel) si aucun autre associé ne détient plus de 50 % ; **ou** plusieurs demandeurs détenant ensemble plus de 50 %, dont un dirigeant, chacun ayant au moins le dixième de la part du principal associé [FV].
- Ne pas avoir bénéficié de l'ACRE dans les 3 années précédentes [FV].
- Textes : LFSS pour 2026, art. 23, et décret n° 2026-69 du 6 févr. 2026 (JO du 8 févr.) fixant le taux de 25 % — **références lues seulement dans des sources secondaires** (legifiscal.fr, actu-juridique.fr) [DR]. Le modèle Urssaf v11.1.0 code bien 25 % « si date de création ≥ 01/2026 » (100 % avant) [FV, données du modèle].
- Gain estimé [ES] pour un gérant TNS éligible : ≈ 1 700 € par an pour 40 000 € de coût total ; ≈ 2 000 € pour 50 000 € ; ≈ 800 € pour 60 000 € ; **0 €** au-delà d'environ 65 000 € de coût total (assiette ≥ 48 060 €). Ordre de grandeur comparable pour un président de SAS faiblement rémunéré [HY].
- La pièce V5 rapportait déjà 25 %, 36 045 €, 48 060 €, 60 jours et le contrôle de deux ans (V5 p. 24-25 ; C3:77) : conforme à la page officielle [FV].

### Sources officielles
- service-public.gouv.fr / entreprendre, « Aide à la création ou à la reprise d'une entreprise (Acre) », https://entreprendre.service-public.gouv.fr/vosdroits/F11677 — « Vérifié le 01 juillet 2026 » — « le montant de l'exonération est fixé à 25 % de ces cotisations » ; « Jusqu'au 31 décembre 2025, aucune formalité n'était à effectuer pour bénéficier de l'Acre » ; « En l'absence de réponse, l'Acre est considérée comme accordée ». Références : CSS L131-6-4, D131-6-1, D131-6-3 ; code du travail L5141-1, R5141-2.
- France Travail, « ARE, ARCE, Acre : créer son entreprise quand on est chercheur d'emploi, le guide complet 2026 », https://www.francetravail.fr/actualites/a-laffiche/2026/are-arce-acre-creer-son-entrepri.html — « Mis à jour le 4 novembre 2026 » — « Le taux de 25 % s'applique aux entreprises individuelles et aux sociétés créées depuis le 1er janvier 2026 ».

### Incertitudes et points à faire valider
- Situation de Morgan et de Mathys au regard de la liste (inscription à France Travail, indemnisation, âge, ACRE antérieure, notamment pour l'entreprise existante de Morgan, note-4-nov:6) **[IN]** (V5 p. 25-26 ; C3:59).
- **Classement FRR de l'adresse réelle** de Marwin : la pièce V5 vise la commune 58086 et annonce que « l'implantation FRR ouvre aussi une voie d'accès à l'ACRE » (V5 p. 24) [DR] ; le classement n'a pas été revérifié ici **[IN]** (Urssaf, simulateur officiel de zonage FRR).
- Formule exacte de la dégressivité entre 36 045 et 48 060 € (Urssaf) **[IN]**.

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Ne pas budgéter l'ACRE** : elle n'est pas acquise, rapporte au plus ≈ 2 000 € par personne et par an, et rien si chacun dépasse ≈ 48 000 € d'assiette [ES].
- Calendrier : **déposer la demande dans les 60 jours** suivant l'immatriculation si l'un des deux est éligible.
- Une entrée de GianLuca Carlone au capital **pendant les deux premières années** peut faire perdre le contrôle effectif exigé [FV + HY].
- Avec 50/50, chacun remplit le critère du dirigeant détenant au moins un tiers du capital **s'il est dirigeant** (président et DG en SAS, cogérants en SARL) [FV + HY].

---

## 6. ARE et ARCE

### Réponse courte
Deux options exclusives pour un créateur indemnisé par France Travail :
- **Maintien de l'ARE** en cumul avec ses revenus : l'ARE est réduite de 70 % des revenus d'activité, et le cumul est **plafonné à 60 % des droits restants** à la date de création (prolongation exceptionnelle possible sur demande à l'instance paritaire régionale, sans aucun revenu, dividendes compris) [FV].
- **ARCE** : capital égal à **60 % des droits restants**, après déduction de 3 % (retraites complémentaires), versé en **deux fois** (50 % à la création, 50 % six mois plus tard) ; **l'ACRE est obligatoire** pour l'obtenir [FV].

### Détail
- Le plafonnement du cumul à 60 % des droits restants est cité par service-public et par France Travail ; la date d'entrée en vigueur (convention d'assurance chômage 2025) n'a pas été vérifiée **[IN]**.
- Conditions supplémentaires pour le second versement de l'ARCE (activité poursuivie, pas de CDI à temps plein) pour les activités créées depuis le 1er avril 2025 [DR, extrait de recherche de la page France Travail].
- L'ARCE serait imposable et soumise à CSG-CRDS selon le guide France Travail 2026 [DR, extrait de recherche].
- Le président de SAS non rémunéré n'a pas de revenu d'activité à déclarer : ARE maintenue jusqu'au plafond **[HY]**, à confirmer par France Travail. Le gérant TNS non rémunéré doit, lui, payer les cotisations minimales (§ 1) [ES].

### Sources officielles
- entreprendre.service-public.gouv.fr, « Peut-on créer une société et continuer à percevoir l'ARE ? », https://entreprendre.service-public.gouv.fr/vosdroits/F36613 — date de vérification non relevée — cumul « limité à 60 % des droits ARE restants » ; « cumuler l'allocation d'aide au retour à l'emploi (ARE) et vos revenus professionnels ».
- France Travail, guide 2026 (voir § 5), « Mis à jour le 4 novembre 2026 » — « le cumul ARE/revenus d'entreprise est plafonné à 60 % du capital de droits restant à la date de création » ; « pour bénéficier de l'ARCE, vous devez obligatoirement obtenir l'ACRE ».
- France Travail, « Aide à la reprise et à la création d'entreprise (ARCE) », https://www.francetravail.fr/candidat/je-creereprends-une-entreprise/les-aides-financieres-creation-d/aide-a-la-reprise-et-a-la-creati.html — lue via extrait de recherche [DR].

### Incertitudes et points à faire valider
- Droits restants de chacun : « Non déterminable à ce stade » selon V5 p. 23 (C3:78) **[IN]** (France Travail).
- Effet d'une rémunération de dirigeant ou de dividendes sur l'ARE maintenue (France Travail) **[IN]**.

### Conséquences pour Marwin Tech et GianLuca Carlone
- Si l'un des associés a des droits importants, la **SAS sans rémunération initiale + ARE** peut financer le démarrage ; l'ARCE suppose l'ACRE, devenue conditionnelle [FV + HY].
- Aucun de ces revenus ne doit être présenté à GianLuca Carlone comme une garantie de capacité : ils dépendent de droits personnels non connus **[IN]**.

---

## 7. Capital, apports, apports en industrie

### Réponse courte
Pas de capital minimum (SAS : 1 € minimum). Apports en numéraire libérés à la constitution d'au moins **50 % en SAS** et **20 % en SARL**, solde sous **5 ans** [FV]. Apports en nature évalués par un **commissaire aux apports**, sauf décision unanime si **aucun apport ne dépasse 30 000 €** et si leur total **ne dépasse pas la moitié du capital** [FV]. **Apports en industrie** possibles dans les deux formes, hors capital : en SARL selon les modalités prévues par les statuts (L223-7) ; en SAS sous forme d'**actions inaliénables** (L227-1) [FV].

### Détail
- L'apport en industrie est un engagement de travail ou de savoir-faire ; il donne droit aux bénéfices et au vote selon les statuts, mais **ne transfère aucune propriété intellectuelle**. Le code, les outils, le CRM ou les méthodes déjà créés par Morgan ou Mathys restent leur propriété, sauf **apport en nature** (évalué) ou **cession / licence écrite** à la société [FV pour la définition ; HY pour l'application].
- Rappel : le taux d'IS de 15 % exige un capital **entièrement libéré** (§ 2) [FV].
- Les pièces internes recommandent déjà trois registres d'actifs (préexistants, composants Marwin, livrables clients) (CS p. 4 ; V5 p. 16 ; C3:53) [PR].

### Sources officielles
- entreprendre.service-public.gouv.fr, F37411 (SARL), « Vérifié le 06 février 2026 » — « 20 % des apports lors de la création de la société » ; apports en industrie « qui n'entrent pas dans la composition du capital social ».
- entreprendre.service-public.gouv.fr, F37366 (SAS), « Vérifié le 6 février 2026 » — moitié des apports en numéraire versée à la création, solde dans les 5 ans.
- Légifrance, article L223-7 C. com., https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006222923 — « les statuts déterminent les modalités selon lesquelles peuvent être souscrites des parts sociales en industrie » (via extrait de recherche).
- Légifrance, article L227-1 C. com., https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038799575/ — version du 1er janv. 2025 (ordonnance n° 2023-1142) — actions inaliénables résultant d'apports en industrie (via extrait de recherche).

### Incertitudes et points à faire valider
- Valorisation d'un apport en nature de logiciels ou de données ; seuils et commissaire aux apports (avocat, expert-comptable) [FV pour les seuils].
- Sort des actions ou parts en industrie en cas de départ (statuts) **[IN]** (avocat).

### Conséquences pour Marwin Tech et GianLuca Carlone
- Proposition : capital modeste, **entièrement libéré**, apporté à parts égales ; PI préexistante **licenciée** à Marwin (pas cédée par défaut) avec un registre daté [PR].
- GianLuca Carlone ne doit pas financer le capital via l'acompte : V5 p. 3 l'exclut déjà (C3:86) [PR].

---

## 8. Société en formation et reprise des actes

### Réponse courte
La société n'existe juridiquement qu'à son **immatriculation** (L210-6 C. com.). Ceux qui ont agi au nom d'une société en formation sont **tenus solidairement et indéfiniment** des actes, sauf si la société immatriculée les **reprend** ; ils sont alors réputés souscrits par elle dès l'origine (L210-6 ; art. 1843 C. civ.) [FV]. Trois voies de reprise : (1) **état des actes annexé aux statuts**, dont la signature emporte reprise à l'immatriculation (R210-5 SARL, R210-6 SAS) ; (2) **mandat** donné à un associé pour des engagements déterminés ; (3) décision des associés après l'immatriculation [FV pour (1) et (2) ; DR pour le rattachement exact de (3)].

### Détail
- **Jurisprudence assouplie** : la Cour de cassation (com., 29 nov. 2023, n° 22-12.865, publiée) ne fait plus de la mention expresse « au nom » ou « pour le compte » de la société en formation une condition absolue : le juge apprécie souverainement, au vu de l'ensemble des circonstances, si la commune intention des parties était d'agir pour la société en formation [FV]. La même chambre (18 juin 2025, n° 24-14.311, publiée) rappelle que la reprise doit en plus respecter les conditions légales [DR, extrait de recherche].
- Un acte signé « par » Morgan ou Mathys à titre personnel, sans référence à la société, reste leur engagement personnel [FV].
- Les pièces internes le disent déjà (CS p. 6 ; V5 p. 3 ; C3:49) [DR].

### Sources officielles
- Légifrance, article L210-6 C. com., https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006222358 — en vigueur depuis le 21 sept. 2000 — personnalité morale à l'immatriculation ; engagements réputés souscrits dès l'origine après reprise.
- Légifrance, article 1843 C. civ., https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006444136 — lu via extrait de recherche — solidarité si la société est commerciale.
- Légifrance, articles R210-1 à R210-8 C. com., https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000005634379/LEGISCTA000006161463/ — R210-5 : signature des statuts « emporte reprise des engagements par la société » ; mandat : « l'immatriculation de la société au registre du commerce et des sociétés emporte reprise de ces engagements ».
- Légifrance, Cass. com., 29 nov. 2023, n° 22-12.865, https://www.legifrance.gouv.fr/juri/id/JURITEXT000048581424 — « désormais au juge le pouvoir d'apprécier souverainement ».
- Légifrance, Cass. com., 18 juin 2025, n° 24-14.311, https://www.legifrance.gouv.fr/juri/id/JURITEXT000051823267 — via extrait de recherche.

### Incertitudes et points à faire valider
- Rédaction de l'état des actes et du mandat ; troisième voie de reprise et majorité requise (avocat) [DR].
- Facturation et encaissement avant l'existence d'un SIREN : impossibles au nom de Marwin **[HY]** (expert-comptable).

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Ne rien signer avec GianLuca Carlone avant l'immatriculation**, ou le signer explicitement « au nom et pour le compte de Marwin Tech, [forme] en formation », inscrit à l'état des actes annexé aux statuts [PR].
- Ne pas faire porter le contrat par l'entreprise existante de Morgan (dont la domiciliation est résiliée, note-4-nov:6) sans décision écrite des deux associés : cela brouillerait la propriété du client et des livrables [HY].
- Pour GianLuca Carlone : demander l'extrait K-bis avant de verser l'acompte protège aussi le payeur [PR].

---

## 9. Pacte d'associés : clauses utiles

### Réponse courte
Le pacte est un contrat confidentiel entre associés, qui complète les statuts ; sa modification exige l'**unanimité des signataires** (Bpifrance Création) [DR]. À 50/50, il est le principal outil pour éviter le **blocage**. Clauses utiles :

| Thème | Clause à prévoir [PR] | Point juridique |
|---|---|---|
| Égalité | Répartition du capital, rôles, temps consacré mesuré, rémunérations différentes possibles et motivées | En SAS, président + DG aux pouvoirs écrits ; en SARL, cogérants (chacun peut engager la société seul envers les tiers) |
| Blocage | Liste de décisions importantes ; médiation ; tiers expert ; puis clause de sortie forcée (« offre alternative » ou « shotgun ») | Bpifrance décrit une offre alternative : 30 jours pour acheter, sinon obligation de vendre [DR]. En SARL 50/50, les décisions ordinaires (dont nomination ou révocation d'un gérant) n'ont pas de majorité sans accord [HY, L223-29 non rouvert] |
| Départ | Préavis, transmission des dossiers, non-sollicitation des clients, non-concurrence limitée et rémunérée si nécessaire | Validité à vérifier par l'avocat |
| Incapacité ou décès | Rachat des titres, assurance homme-clé, intérim de direction | — |
| Propriété intellectuelle | Inventaire daté des actifs préexistants, licence ou cession à Marwin, titularité des développements faits pour Marwin, sort du nom « Jarvis » (C3:247) | Un apport en industrie ne transfère pas la PI (§ 7) |
| Good / bad leaver | Prix de rachat différent selon le motif de départ, formule de valorisation | Clause contractuelle de pratique ; articulation avec l'expertise de l'art. 1843-4 C. civ. à vérifier (avocat) **[IN]** |
| Cessions | Agrément, préemption, sortie conjointe, inaliénabilité (SAS : ≤ 10 ans, adoptée à l'unanimité) | F36022 [FV] |
| Investisseur | Droits d'information, absence de veto opérationnel, séparation client / associé | § 10 |

### Sources officielles
- Bpifrance Création (secondaire signalée), « Pacte d'associés : organisation et fonctionnement », https://bpifrance-creation.fr/encyclopedie/structures-juridiques/entreprendre-a-plusieurs/pacte-dassocies-organisation — « Sa modification nécessite l'accord unanime des signataires ».
- Bpifrance Création, « Pacte d'associés : attention à la rédaction des clauses », https://bpifrance-creation.fr/entrepreneur/actualites/pacte-dassocies-attention-a-redaction-clauses — clause d'offre alternative (via extrait de recherche).
- entreprendre.service-public.gouv.fr, « Cession d'actions de SAS / SASU », https://entreprendre.service-public.gouv.fr/vosdroits/F36022 — « Vérifié le 22 juillet 2026 » — inaliénabilité « ne peut pas excéder 10 ans » et « ne peut être adoptée ou modifiée qu'à l'unanimité ».

### Incertitudes et points à faire valider
- Rédaction, validité et force exécutoire des clauses (avocat) ; un pacte non respecté donne surtout lieu à des dommages-intérêts **[HY]**.
- Disponibilité réelle de chacun : non documentée (note-4-nov:17) **[IN]**.

### Conséquences pour Marwin Tech et GianLuca Carlone
- Signer le pacte **avant** le contrat client : Morgan mène plusieurs projets en parallèle (note-4-nov:12-17) et aucune donnée n'existe sur l'agenda de Mathys [FV pour le constat].
- Le pacte doit fixer qui parle à GianLuca Carlone, qui signe et qui valide une dépense pour Marwin [PR].

---

## 10. Entrée d'un investisseur client au capital (GianLuca Carlone)

### Réponse courte
La **SAS** est nettement plus adaptée : cession d'actions libre par défaut, encadrée par les statuts (agrément, préemption) ; droits d'enregistrement de **0,1 %** ; possibilité d'actions de préférence et de valeurs mobilières donnant accès au capital [FV pour 0,1 % et les clauses ; DR pour les instruments]. En **SARL**, l'entrée d'un tiers suppose l'**agrément** de la majorité des associés représentant au moins la moitié des parts ; la cession de parts coûte **3 %** après un abattement de 23 000 € × parts cédées / total des parts ; pas d'actions de préférence [FV pour l'agrément et les droits ; DR pour les instruments].

### Détail
- Exemple de l'administration [FV] : 10 parts sur 100 vendues 10 000 € → abattement 2 300 € → droits de 231 €.
- Seuils à surveiller si l'investisseur est une société : taux d'IS de 15 % (≥ 75 % de personnes physiques), option IR (≥ 50 % de personnes physiques et ≥ 34 % de dirigeants), contrôle effectif ACRE pendant 2 ans (§ 2, 4, 5) [FV].
- Conventions entre la société et un associé important : procédures de contrôle des conventions (SAS : art. L227-10 ; SARL : art. L223-19) — **non rouvertes** **[IN]**.
- Cumul de rôles : GianLuca Carlone serait à la fois client, éventuel bailleur, éventuel employeur et associé. Risque principal : qu'un désaccord commercial se transforme en blocage de la société, ou l'inverse **[HY]** (risque déjà signalé, CS p. 6 ; C3:248).

### Sources officielles
- entreprendre.service-public.gouv.fr, F36022 (voir § 9) — « le droit d'enregistrement est fixé à 0,1 %, calculé sur le prix de cession ».
- entreprendre.service-public.gouv.fr, F37411 (voir § 1) — cession de parts soumise à « l'agrément des associés ».
- impots.gouv.fr, « Je souhaite vendre des parts de ma SARL, quels seront les droits à payer ? », https://www.impots.gouv.fr/portail/particulier/questions/je-souhaite-vendre-des-parts-de-ma-sarl-quels-seront-les-droits-payer — via extrait de recherche — « 23 000 € x nombre de parts cédées / nombre total de parts de la société ».

### Incertitudes et points à faire valider
- Instruments adaptés (actions de préférence, BSA, obligations convertibles, BSPCE réservés aux sociétés par actions) : non vérifiés dans les textes (avocat) [DR].
- Entité de GianLuca Carlone qui investirait et sa composition **[IN]** (DEMANDE.md:23).

### Conséquences pour Marwin Tech et GianLuca Carlone
- Si une entrée de GianLuca Carlone au capital est sérieusement envisagée, la SAS s'impose [HY]. Proposition : **pas avant 12 à 24 mois**, minoritaire, sans droit de veto opérationnel, avec un contrat client séparé et résiliable indépendamment [PR].
- Aucune promesse d'investissement ne doit être traitée comme une trésorerie disponible (DEMANDE.md:23) [FV].

---

## 11. Micro-entreprise comme alternative de démarrage

### Réponse courte
Plafonds **2026-2028** : **83 600 €** HT de CA pour les prestations de services et activités libérales, **203 100 €** pour la vente (arrêté du 27 janv. 2026) — **changement 2026** (77 700 € et 188 700 € auparavant) [FV]. **Franchise en base de TVA** inchangée : 37 500 € pour les services (seuil majoré 41 250 €) ; les réformes prévues par les lois de finances pour 2025 et 2026 « ne sont pas entrées en vigueur » [FV]. Cotisations 2026 : **25,6 %** du CA en libéral non réglementé (BNC), **21,2 %** en prestations de services commerciales (BIC) [FV, F36232 ; des sources secondaires citent 26,1 % pour le BNC — à recontrôler]. **Limite pour deux** : la micro-entreprise est **individuelle** ; elle ne permet ni de s'associer, ni de mettre en commun le chiffre d'affaires, ni d'accueillir un investisseur.

### Détail
- Chacun facturerait séparément (deux contrats ou un contrat cadre avec deux prestataires) : risque de **société créée de fait** si l'activité est commune [HY] ; pas de déduction des frais réels (abattement fiscal de 34 % en BNC, 50 % en BIC services) [FV, impots.gouv mars 2026].
- ACRE micro : 25 % pour les créations depuis le 1er juillet 2026, jusqu'à la fin du 3e trimestre civil suivant le début d'activité, sous les mêmes conditions de public [FV, F11677].
- Versement libératoire de l'IR possible si le revenu fiscal de référence 2024 ≤ 29 315 € par part [FV, impots.gouv mars 2026].
- Simulation [ES] (BNC 25,6 %, frais réels 1/6 du CA partagés) :

| CA total (2 personnes) | CA par personne | Statut micro | Cotisations par personne | Net avant IR par personne, après frais réels |
|---|---|---|---|---|
| 120 000 € | 60 000 € | Possible (sous 83 600 €) ; **TVA due** car > 41 250 € | ≈ 15 400 € | ≈ 34 600 € (proche de la SARL TNS, § 1) |
| 180 000 € | 90 000 € | **Dépasse** 83 600 € : sortie du régime selon les règles de dépassement (non revérifiées) | ≈ 23 000 € | Non pertinent |
| 360 000 € | 180 000 € | Impossible | — | — |

### Sources officielles
- entreprendre.service-public.gouv.fr, actualité A18813, https://entreprendre.service-public.gouv.fr/actualites/A18813 — publiée le 26 févr. 2026 — seuils « pour les années 2026, 2027 et 2028 » ; arrêté du 27 janvier 2026.
- impots.gouv.fr, « Les régimes réservés aux petites entreprises » (fiche datée **mars 2026**), https://www.impots.gouv.fr/sites/default/files/media/3_Documentation/depliants/pro_fiche_regimes_reserves_aux_petites_entreprises_2026.pdf — « les modifications des règles applicables à la franchise TVA prévues dans la loi de finances pour 2025, puis dans la loi de finances pour 2026, ne sont pas entrées en vigueur ». Attention : cette fiche affiche encore les seuils micro de 77 700 / 188 700 € appréciés sur le CA 2025.
- entreprendre.service-public.gouv.fr, « Cotisations sociales d'un micro-entrepreneur », https://entreprendre.service-public.gouv.fr/vosdroits/F36232 — « Vérifié le 1er janvier 2026 » — 21,2 % (BIC services), 25,6 % (BNC non réglementé), 23,2 % (Cipav).

### Incertitudes et points à faire valider
- Taux BNC 2026 (25,6 % ou 26,1 %) : à confirmer sur autoentrepreneur.urssaf.fr **[IN]**.
- Règle de sortie après dépassement des plafonds (economie.gouv.fr inaccessible, HTTP 403) **[IN]**.
- Statut actuel de Morgan : s'il est déjà micro-entrepreneur, le CA Marwin s'ajouterait à celui de ses autres activités (OLSEN, note-4-nov:9) **[IN]**.

### Conséquences pour Marwin Tech et GianLuca Carlone
- Solution de **test court** possible jusqu'à ≈ 120 000 € de CA total (≈ 60 000 € chacun), pas une structure pour un contrat de 15 000 à 30 000 € HT par mois sur plusieurs mois : 180 000 € dépassent les plafonds dès la première année [ES].
- Pour GianLuca Carlone, deux prestataires individuels au lieu d'une société : responsabilités, propriété des livrables et continuité plus difficiles à organiser [HY].

---

## 12. Réexamen des recommandations antérieures

| Pièce interne | Affirmation | Vérification du 4 nov. 2026 |
|---|---|---|
| CS p. 1 / V5 p. 17-20 (C3:237) | SAS à l'IS « piste prioritaire » (29 oct.), puis SARL à gérance majoritaire « référence » (30 oct.) | Aucune des deux n'est validée. Le choix dépend de la question laissée ouverte en CS p. 1 (société ouverte ou rémunération à deux) **[IN]** |
| CS p. 2 (C3:42, C3:251) | 50/50 en cogérance = gérance majoritaire | **Confirmé** [FV] |
| CS p. 3 (C3:43) | IS 15 % jusqu'à 42 500 € ; capital libéré ; 75 % personnes physiques | **Confirmé** [FV] |
| CS p. 3 ; V5 p. 20 (C3:45) | Dividendes du gérant majoritaire au-delà de 10 % soumis à cotisations | **Confirmé** ; base élargie aux primes et comptes courants selon la notice Urssaf [DR] |
| V5 p. 18 (C3:69) | PFU de 31,4 % | **Confirmé** (LFSS 2026, art. 12) [FV] |
| V5 p. 24-25 (C3:77) | ACRE 25 %, 36 045 €, 48 060 €, 60 jours, contrôle 2 ans | **Confirmé** (F11677 du 1er juill. 2026) [FV] |
| V5 p. 23 (C3:78) | ARCE 60 %, retenue 3 %, deux versements, ACRE requise | **Confirmé** [FV] ; ajouter le plafonnement du cumul ARE à 60 % des droits restants |
| V5 p. 17 (C3:36) | SAS « généralement plus coûteuse » | **Exact en ordre de grandeur** : ≈ 15 à 20 % de net en moins à coût égal [ES], contre une meilleure retraite complémentaire |
| V5 p. 18 (C3:61) | Simulation sur 180 000 € de CA en 12 mois | Hypothèse non couverte par un contrat (le contrat proposé dure 6 mois) ; les règles 2026 utilisées sont les bonnes |

---

## 13. Recommandation de travail (non décisionnelle)

1. **Si l'objectif est une société ouverte** (associé futur, investisseur, dont GianLuca Carlone) **ou un démarrage sans rémunération** : **SAS à l'IS**, président + DG, capital modeste entièrement libéré, pacte signé. Coût social plus élevé à rémunération égale [PR + ES].
2. **Si l'objectif est le revenu régulier à deux, sans ouverture du capital** : **SARL à l'IS en cogérance 50/50 (TNS)** ; provisionner les régularisations de cotisations [PR + ES].
3. **Option IR et FRR** : seulement après confirmation écrite du FRR (rescrit) et avec un prévisionnel prêt avant la fin du troisième mois du premier exercice [PR].
4. **Micro-entreprise** : test court et limité, pas une base pour un contrat de 90 000 € HT sur six mois partagé à deux [ES].
5. **Questions à poser** — expert-comptable : simulation officielle des trois CA pour SAS et SARL ; taux BNC micro 2026 ; régularisations TNS ; option IR. Avocat : statuts et pacte, état des actes, PI préexistante, entrée de GianLuca Carlone. France Travail et Urssaf : droits ARE, éligibilité ACRE, zonage FRR de l'adresse réelle.

---

## 14. Tableau récapitulatif

| Règle | Valeur ou condition (4 nov. 2026) | Source | Niveau de certitude |
|---|---|---|---|
| Statut du président / DG de SAS rémunéré | Assimilé salarié, sans chômage | F37366 ; F36065 | Élevé [FV] |
| Cogérants SARL à 50/50 | Collège majoritaire → TNS | Urssaf (extrait) ; Cass. civ. 2, 31 mai 2018, 17-17.518 ; CS p. 2 | Élevé [FV/DR] |
| Gérant SARL unique à 50 % (égalitaire) | Assimilé salarié | F37411 ; Urssaf (extrait) | Élevé [FV/DR] |
| Assiette TNS | Revenu avant cotisations − 26 % (réforme appliquée aux revenus 2025) | F38152 (08/10/2026) | Élevé [FV] |
| Retraite de base TNS | 17,87 % ≤ 48 060 € ; 0,72 % au-delà | F38152 | Élevé (revenus 2025) [FV] |
| PASS 2026 | 48 060 € (4 005 €/mois) | F11677 ; modèle Urssaf | Élevé [FV] |
| Forfaits TNS création 2026 | ≈ 3 471 € + CFP 120 € | F38152 | Élevé [FV] |
| Minimum TNS sans revenu | ≈ 1 255 €/an | Calcul sur modèle Urssaf | Moyen [ES] |
| Charges assimilé salarié | ≈ 80 % du net | Bpifrance Création (secondaire) | Moyen [DR] |
| IS | 15 % ≤ 42 500 € ; 25 % au-delà ; CA ≤ 10 M€ ; capital libéré ; ≥ 75 % personnes physiques | Art. 219 CGI (vers. 21/02/2026) ; F23575 | Élevé [FV] |
| PFU 2026 | 31,4 % (12,8 % + 18,6 %) | F2329 (30/06/2026) ; LFSS 2026 art. 12 | Élevé [FV] |
| Dividendes gérant majoritaire SARL | Cotisations TNS au-delà de 10 % (capital + primes + comptes courants) | F36065 ; notice Urssaf 2026 (extrait) ; L131-6 CSS | Élevé sur le principe, moyen sur l'assiette [FV/DR] |
| Dividendes SAS | Pas de cotisations ; aucune réforme 2026 trouvée | F37366 ; F36065 | Élevé [FV] |
| Option IR | < 5 ans ; 5 exercices ; 3 mois ; unanimité ; 50 % PP dont 34 % dirigeants ; < 50 salariés ; < 10 M€ | Art. 239 bis AB CGI | Élevé [FV] |
| ACRE (non micro) | Publics ciblés ; demande sous 60 j ; 25 % ; ≤ 36 045 € puis dégressif ; nulle ≥ 48 060 € ; 12 mois ; contrôle 2 ans | F11677 (01/07/2026) ; France Travail (04/11/2026) | Élevé [FV] ; références décret/LFSS [DR] |
| ACRE micro | 25 % pour créations depuis le 1/07/2026 | F11677 ; France Travail | Élevé [FV] |
| Cumul ARE | Réduction de 70 % des revenus ; plafond 60 % des droits restants | F36613 ; France Travail | Élevé [FV] ; date d'effet [IN] |
| ARCE | 60 % des droits restants − 3 % ; 2 versements à 6 mois ; ACRE obligatoire | France Travail (04/11/2026) | Élevé [FV] |
| Libération du capital | SAS 50 % ; SARL 20 % ; solde 5 ans | F37366 ; F37411 | Élevé [FV] |
| Commissaire aux apports | Évitable à l'unanimité si chaque apport ≤ 30 000 € et total ≤ ½ capital | F37411 ; F37366 | Élevé [FV] |
| Apports en industrie | Possibles en SARL (statuts) et en SAS (actions inaliénables), hors capital | L223-7 ; L227-1 ; F37411 | Élevé [FV] |
| Société en formation | Responsabilité solidaire et indéfinie jusqu'à la reprise ; reprise par état annexé, mandat ou décision | L210-6 C. com. ; 1843 C. civ. ; R210-5/6 | Élevé [FV] |
| Mention « au nom de la société en formation » | Plus une condition absolue ; intention commune appréciée par le juge | Cass. com. 29/11/2023, 22-12.865 | Élevé [FV] |
| Cession d'actions SAS | 0,1 % (min. 25 €) ; inaliénabilité ≤ 10 ans à l'unanimité | F36022 (22/07/2026) | Élevé [FV] |
| Cession de parts SARL | 3 % après abattement 23 000 € × quote-part ; agrément | impots.gouv (extrait) ; F37411 | Élevé [FV/DR] |
| Plafonds micro 2026-2028 | 83 600 € services ; 203 100 € ventes | A18813 (26/02/2026) | Élevé [FV] |
| Franchise TVA services | 37 500 € (majoré 41 250 €) ; réformes LF 2025/2026 non entrées en vigueur | impots.gouv (mars 2026) | Élevé [FV] |
| Cotisations micro 2026 | 25,6 % BNC ; 21,2 % BIC services | F36232 (01/01/2026) | Moyen (26,1 % cité ailleurs) [FV/IN] |
| PLF / PLFSS 2027 | Aucune mesure identifiée sur ces sujets au 1er oct. 2026 | legifiscal.fr (secondaire) | Faible [IN] |
| Fourchettes nettes par personne (CA 120 k / 180 k / 360 k) | SARL TNS ≈ 34 k / 51 k / 107 k ; SAS salaire ≈ 27-29 k / 40-44 k / 81-88 k (avant IR) | Calcul de ce chercheur ; simulateur à utiliser : mon-entreprise.urssaf.fr | Faible à moyen [ES] |
