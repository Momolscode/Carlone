# Synthèse « droit » : structure, relations, propriété, art et lieux, données et IA (état au 4 novembre 2026)

Synthétiseur « droit » de l'audit Marwin Tech × GianLuca Carlone. Rédigé le 4 novembre 2026, en lecture seule. Aucun contact, aucune démarche, aucune dépense, aucune modification du dépôt `Momolscode/Carlone` (commit 7b46602), du dépôt BOJART ni des mémos. Ce document **n'est pas une consultation juridique ou fiscale** : il rassemble l'état des textes relevé par les chercheurs et leurs contrôleurs, le confronte aux pièces du dossier et prépare les questions à soumettre à l'expert-comptable et à l'avocat.

Le client s'appelle **GianLuca Carlone**. Les pièces qui portent « John-Lucas » sont citées telles quelles, suivies de [sic, lire GianLuca]. Dans les pièces, « Carlone » désigne tantôt la personne, tantôt une entité non identifiée.

## Méthode, conventions et limites

**Codes.** [FV] fait vérifié sur source primaire ou fichier ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ou lecture juridique à faire valider ; [ES] estimation ou simulation ; [MM] mesure effectivement faite ; [IN] inconnu.

**Règle de priorité.** Quand un contrôleur corrige un chercheur ou un lecteur, c'est la correction qui est retenue ici. Les points déterminants ou contestés ont été revérifiés dans les pièces d'origine (voir annexe A).

**Abréviations de citation.**
- Mémos et contrôles (dossier `audit-work/`) : **R1** = `rj-R1-structures.md`, **vR1** = `ver-R1-structures.md` ; de même R2/vR2 (fiscal), R3/vR3 (travail et contrats), R4/vR4 (données et IA), R5/vR5 (art et lieux) ; **C3**/**vC3** = `ex-C3-structure.md`/`ver-C3-structure.md` ; **C5**/**vC5** = `ex-C5-crm.md`/`ver-C5-crm.md` ; **C6**/**vC6** = `ex-C6-catalogue.md`/`ver-C6-catalogue.md`. Forme : `R1:279` = ligne 279.
- Pièces du dépôt : **CS p. N** = `interne/archives-marwin-tech/choix-structure-2026-10-29.pdf` p. N ; **V5 p. N** = `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. N ; **offre-md** = `interne/offre-marwin-tech-remuneration-et-collaboration.md` ; **contexte** = `interne/contexte-projet-carlone.md` ; **audit-md** = `interne/audit-marwin-tech-carlone.md` ; **accomp** = `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md` ; **recueil** = `interne/recueil-sessions-chatgpt-2026-11-04.txt` ; **PASS** = `crm/PASSATION.md` ; **rapport-crm** = `crm/docs/rapport/rapport-crm-hermes360.md` ; **vernissage** = `pour-carlone/vernissage-strates-idees.md`.
- **Diaporama** = diaporama client « Offre Marwin Tech pour Carlone », version du 4 nov. (`scratchpad/artifact-files/04f14ef8-…/project/deck.json:7` : 11 vues).
- **Note 4 nov.** = `audit-work/note-point-4-novembre-et-activites.md`.

**Sources officielles.** Elles ont été consultées le 4 nov. 2026 par les chercheurs et revérifiées par leurs contrôleurs (Légifrance, BOFiP, entreprendre.service-public.gouv.fr, EUR-Lex, CNIL, DGCCRF, ANSSI, etc.). Les URL et dates de mise à jour figurent dans les mémos cités.

**Limites.**
1. **urssaf.fr** renvoyait une erreur HTTP 503 le 4 nov. : les cotisations du régime général d'un mandataire social n'ont pas pu être relevées. Aucun simulateur officiel n'a été exécuté (R1:13-14 ; vR1:8, 40). Toutes les fourchettes de revenu ci-dessous sont des [ES].
2. Les **lois de finances et de financement de la sécurité sociale pour 2027** sont en discussion. Une société créée fin 2026 aura un premier exercice soumis aux règles de 2027 : il faut **tout revérifier en janvier 2027** (vR1:43).
3. Le dépôt **FinanceScope/CRM-Carlone** n'a pas été revérifié dans l'audit (accès refusé) : son caractère public est une déclaration de Morgan (contexte:5, :11) [DR] (R4:16).

### Trois faits nouveaux intégrés

1. **Retrait de Medhi et de BOJ.ART de l'offre (4 nov.)** [DR]. Morgan a écrit : « Va juste falloir enlever Medhi/boj art de l'offre » (Note 4 nov., § C). Le diaporama client a été corrigé : 11 vues, sans `strates` ni `strates-phases` (deck.json:7) [FV]. En revanche, quatre documents n'ont pas été corrigés [FV] :
   - l'offre écrite garde l'« Option création » (offre-md:22) et le tableau « Qui apporte quoi » avec Medhi (offre-md:88-94) ;
   - la proposition STRATES v1.1 porte toujours l'en-tête « BOJ.ART / MARWIN TECH » (`pour-carlone/strates-proposition-artistique-v1.1.pdf` p. 1) ;
   - le document du vernissage repose sur le parc et la main de Medhi (vernissage:5, 20-22, 57, 122) ;
   - le PDF de 13 pages de la PR n° 1 contient les vues STRATES (`syn-sources.md:61-70`).

   La décision n'est formalisée ni avec Mathys ni avec Medhi.
2. **Fuite probable de données personnelles.** Le dépôt public FinanceScope/CRM-Carlone est très probablement une violation de données personnelles. Le délai de 72 heures pour notifier la CNIL **expirerait le 5 nov.**, à une heure inconnue, si la connaissance date du 2 nov. (R4:207 ; vR4:21) [ES].
3. **Aucun contrat, aucune facture, aucune entité payeuse identifiée** [FV] (audit-md:13-14 ; offre-md:16 ; contexte:106).

   Toutes les obligations qui dépendent du cocontractant restent donc conditionnelles : vigilance, rôles RGPD, LCB-FT, organisateur d'événement.

---

## 0. L'essentiel

1. **SARL ou SAS : aucune des deux n'est décidée** [FV] (V5 p. 17 ; offre-md:153). La version du 30 octobre (SARL à l'IS) était une référence « provisoire » (V5 p. 20 ; vC3:21). Les documents en aval la traitent pourtant comme une décision (offre-md:155 ; contexte:12 ; audit-md:23).
   - À rémunération régulière égale, la SARL en cogérance 50/50 laisse **environ 15 à 30 % de net en plus avant IR** [ES].
   - La SAS est préférable si l'un de ces trois cas se présente : **entrée d'un investisseur**, démarrage **sans rémunération régulière**, ou associé qui vit d'un **emploi extérieur**.
   - Au 4 novembre, les trois signaux existent [DR/IN]. **Recommandation conditionnelle : SAS par défaut, à confirmer par une simulation officielle** (§ 1.10).
2. **Ne rien encaisser avant l'immatriculation.** Si un acte doit être signé avant, il l'est au nom de la société en formation, avec un état des actes annexé aux statuts. Il ne faut pas faire porter le contrat par l'entreprise existante de Morgan (R1:279-281 ; vR1:28).
3. **Quatre relations à séparer : client, bailleur, employeur, investisseur.** GianLuca Carlone est présenté dans ces quatre rôles [DR]. Leur cumul expose à plusieurs risques : requalification en contrat de travail (le risque pèse surtout sur son entité), dépendance totale de Marwin et blocage croisé. Règle : un accord par sujet, chacun avec sa propre sortie ; salariat différé ; capital minoritaire, au plus tôt 12 à 24 mois après le début (§ 4).
4. **Pacte entre Morgan et Mathys avant le contrat client.** Il doit traiter : le temps réel de chacun, les autres activités de Morgan, la propriété du CRM et de Jarvis, les rémunérations inégales, le blocage à 50/50, le départ et l'incapacité (§ 5).
5. **La propriété des actifs n'est écrite nulle part.**
   - Le CRM est co-écrit, sans licence, et hébergé sous les comptes des associés [FV/DR].
   - La garantie de réversibilité affichée dans le diaporama n'est donc **pas encore exacte** (R3:438).
   - Le retrait de Medhi fait sortir ses œuvres, ses motifs et les films STRATES de tout ce que Marwin peut promettre (§ 6).
6. **Galerie, ventes et événements.** Les obligations (registre, LCB-FT, droit de suite, contribution diffuseur, rétractation, ERP, licences) pèsent sur **l'entité de GianLuca qui vend, organise ou exploite**, pas sur Marwin. Marwin les supporterait seulement si elle devenait intermédiaire de vente, dépositaire, organisateur ou fabricant. Un événement public dans un lieu non autorisé est **impossible en décembre 2026** (R5:353) [ES] (§ 7).
7. **Arguments fiscaux.** La déduction des œuvres d'artistes vivants (238 bis AB) est **validée jusqu'aux achats faits avant le 31 déc. 2028** [FV]. Elle est **très probablement fermée** aux pièces faites à la machine (3D, robot, IA) [HY], sauf rescrit. Le mot « mécénat » ne doit jamais servir à vendre une œuvre (§ 8).
8. **Données.**
   - La fuite GitHub doit être traitée **avant le 5 nov.**, avec un avocat ou un DPD [ES].
   - Aucun responsable du traitement, aucun contrat de l'article 28 et aucun registre n'existent [FV].
   - Les prestataires d'IA **Anthropic et OpenAI ne sont pas inscrits au Data Privacy Framework** : il faut des clauses contractuelles types et une analyse d'impact des transferts [MM] (§ 9).

### Échéancier juridique (dates fermes ou probables)

| Date | Échéance | Qui | Code et source |
|---|---|---|---|
| **5 nov. 2026** (heure inconnue) | Fin du délai de 72 h de notification à la CNIL, si la violation est connue depuis le 2 nov. | Responsable du traitement, non désigné | [ES] R4:207 ; vR4:21 |
| 2 déc. 2026 | AI Act : marquage (art. 50, § 2) pour les systèmes génératifs déjà sur le marché ; nouvelles interdictions de l'art. 5 | Fournisseurs | [FV] R4:286 ; vR4:24 |
| 9 déc. 2026 (produits mis sur le marché **après le 8 déc.**) | Nouvelle responsabilité du fait des produits, logiciels et IA compris | Fabricants, intégrateurs | [FV] vR5:44 |
| Fin déc. 2026, au plus tard | Entrée en vigueur de L8222-1-1 (vigilance du maître d'ouvrage sur les sous-traitants acceptés) | Entité de GianLuca, si maître d'ouvrage | [FV] vR3:36 |
| **31 déc. 2026** | Déclaration 1447-C-SD de CFE, si la société est créée en 2026 | Marwin | [FV] R2:278 ; vR2:44 |
| 31 déc. 2026 | Échéance annoncée des aides régionales, « dans la limite des crédits » | Marwin, client éligible | [DR] V5 p. 23 |
| Janvier 2027 | Revérifier IS, PFU, cotisations, ACRE et seuils (LF et LFSS 2027) | Expert-comptable | [IN] vR1:43 |
| 60 jours après le début d'activité | Demande d'ACRE, si l'un des deux est éligible | Chaque associé | [FV] R1:177 |
| 3 mois après l'ouverture du premier exercice | Option pour l'IR (art. 239 bis AB) | Tous les associés | [FV] R1:153 |
| 20 janv. 2027 | Règlement machines (UE) 2023/1230 applicable | Fabricant, intégrateur | [FV] R5:477 |
| 10 juill. 2027 | Règlement européen anti-blanchiment (AMLR) : marchands d'art dès 10 000 € ; espèces plafonnées à 10 000 € dans l'UE | Entité qui vend | [FV] vR5:35 |
| **1er sept. 2027** | Émission des factures électroniques et e-reporting pour les PME | Marwin | [FV] R2:17 |
| 2 déc. 2027 | AI Act : systèmes à haut risque de l'annexe III | Fournisseurs et déployeurs | [FV] R4:287 |
| Achats faits **avant** le 31 déc. 2028 | Fin du 238 bis AB | Entreprises acheteuses | [FV] R2:13 ; vR2:26 |

---

## 1. SAS ou SARL à deux associés, sur des hypothèses identiques

### 1.1 Hypothèses communes [HY]

- **Deux associés à parts égales (50/50)**, tous deux dirigeants :
  - en SARL : cogérants ;
  - en SAS : président et directeur général.
- **Frais hors dirigeants : 1/6 du chiffre d'affaires**, soit 20 000, 30 000 et 60 000 € (même convention que R1:58, cohérente avec les 30 000 € de V5 p. 18).
- Tout le reste revient aux deux dirigeants, sauf dans les scénarios « avec réserve ».
- Pas d'ACRE, pas de FRR, pas de prévoyance ni de mutuelle.
- Impôt sur le revenu (IR) non déduit : la situation fiscale des foyers est [IN] (R1:15).
- Capital entièrement libéré, donc taux réduit d'IS de 15 % jusqu'à 42 500 € (R1:94, 113).

**Barèmes utilisés.**
- **TNS** : barème de la fiche F38152 (vérifiée le 08/10/2026), appliqué à 74 % du coût total (abattement de 26 %, art. L136-3 III CSS). Le plancher et le plafond de l'abattement sont ignorés (vR1:20). Les taux « revenus 2025 » servent pour 2026 [IN] (R1:44).
- **Assimilé salarié** : coût total égal à **1,70 à 1,90 fois le net**. Ce coefficient vient d'une seule source secondaire (Bpifrance) et de l'ordre de grandeur de 1,6 à 1,9 retenu par offre-md:126 [HY] (vR1:40).
- **Dividendes** : PFU de 31,4 %, soit 12,8 % d'IR et 18,6 % de prélèvements sociaux (vR1:22).

**Calcul.** Il a été refait par ce synthétiseur avec un script Python (`scratchpad/syn-droit-calc/sim.py`), le 4 nov. 2026 [ES].

**Ligne de contrôle.** Le seul contrat proposé vaut **90 000 € HT sur 6 mois** [PR], non signé (offre-md:16). Il est ajouté avec 25 000 € de frais [HY], parce que les frais fixes (assurance, comptable, logiciels) ne baissent pas au prorata.

### 1.2 Statut social et protection

| Point | SARL, deux cogérants à 50/50 | SAS, président et directeur général | Code et source |
|---|---|---|---|
| Régime | **Travailleurs non salariés (TNS) tous les deux** : le collège de gérance détient plus de la moitié des parts | **Assimilés salariés** s'ils sont rémunérés | [FV] Cass. civ. 2, 31 mai 2018, n° 17-17.518 ; F37411, F37366 (vR1:19) |
| Piège | « 50/50 » ne signifie pas « gérance égalitaire » : le tableau de CS p. 2 induit en erreur | — | [FV] C3:251 ; vR1:19 |
| Sans rémunération | Minimum d'environ **1 255 € par an et par gérant** ; forfaits de début d'activité d'environ **3 591 € par an**, CFP comprise, régularisés ensuite | **0 €**, mais aucun droit social créé par le mandat | [ES] minimum (vR1:39) ; [FV] forfaits (F38152, vR1:20) ; [FV] R1:33 |
| Charges, en part du net | ≈ 40 à 46 % | ≈ 70 à 90 % | [ES] calcul § 1.3 ; vR1:40 |
| Indemnités journalières maladie | Plafond de 65,84 € par jour, 3 jours de carence | Plafond de 41,95 € par jour | [FV] F38152 (vR1:42) |
| Retraite | Base et complémentaire des indépendants | Base et Agirc-Arrco : en général plus de droits à coût égal | [FV] régimes ; [IN] écart chiffré (R1:386) |
| Chômage | Aucun | Aucun | [FV] F36065 (vR1:19) |
| Accidents du travail | Couverture à vérifier | Cotisation AT/MP (taux non vérifié) | [IN] R1:55 ; [HY] V5 p. 18 |

### 1.3 Fourchettes de revenu net par personne et par an, avant impôt sur le revenu [ES]

| CA HT annuel (frais) | A. SARL TNS, tout en rémunération | A2. SARL TNS, réserve de 10 % du CA après IS | B. SAS, tout en salaire | B2. SAS, salaire et même réserve | C. SAS, 2 000 €/mois nets chacun + dividendes (net de prélèvements sociaux, avant IR) | C0. SAS sans salaire, tout en dividendes |
|---|---|---|---|---|---|---|
| **90 000 € (25 000 €)**, contrat seul | ≈ 22 800 | ≈ 19 200 | 17 100 à 19 100 | 14 300 à 16 000 | **Infaisable** : les deux salaires coûtent plus que le disponible | ≈ 21 600 (≈ 18 200 après PFU), **sans protection** |
| **120 000 € (20 000 €)** | ≈ 34 500 (charges ≈ 15 500) | ≈ 29 900 (réserve 12 000) | 26 300 à 29 400 | 22 600 à 25 300 | 27 000 à 30 400 (26 600 à 29 400 après PFU) | ≈ 32 300 (≈ 27 200 après PFU), sans protection |
| **180 000 € (30 000 €)** | ≈ 51 400 (charges ≈ 23 600) | ≈ 43 700 (réserve 18 000) | 39 500 à 44 100 | 33 900 à 37 900 | 43 700 à 46 600 (40 600 à 43 100 après PFU) | ≈ 47 500 (≈ 40 000 après PFU), sans protection |
| **360 000 € (60 000 €)** | ≈ 107 000 (charges ≈ 43 000) | ≈ 91 000 (réserve 36 000) | 78 900 à 88 200 | 67 800 à 75 800 | 89 500 à 92 400 (79 200 à 81 600 après PFU) | ≈ 93 300 (≈ 78 600 après PFU), sans protection |

**Lecture.**
- **Écart SARL / SAS en rémunération pure** (A contre B) : environ **+5 000 à +8 000 €** par personne à 120 k€, **+7 000 à +12 000 €** à 180 k€ et **+19 000 à +28 000 €** à 360 k€, soit **+15 à +30 %** [ES]. R1 trouvait +15 à +20 % avec un coefficient plus bas (R1:26) : l'écart dépend surtout du coefficient SAS non vérifié.
- **Le mélange « salaire et dividendes » en SAS** (C) réduit l'écart à environ 4 000 à 8 000 € à 120-180 k€. Mais les dividendes :
  - ne sont ni mensuels ni garantis (V5 p. 20) ;
  - ne créent aucun droit à la retraite ;
  - supportent l'IS, puis le PFU.

  L'écart de 2 795 € de V5 p. 18 compare deux stratégies différentes (rémunération pure contre salaire et dividendes). Il ne mesure pas le surcoût d'une rémunération régulière en SAS (vC3:22).
- **Sur le seul contrat de 6 mois**, chacun toucherait environ **19 000 à 23 000 € avant IR sur l'année** en SARL, soit environ 1 600 à 1 900 € par mois. Le lecteur C3 trouvait 1 400 à 1 750 € (C3:228). Les nets de 3 660 € par mois affichés en aval supposent 12 mois facturés (V5 p. 18-19 ; offre-md:109-112) [ES].
- **Les nets « à l'euro près »** de V5 p. 18 (43 875 €, 51 408 €, 41 080 €…) sont une précision artificielle : il faut parler en fourchettes (C3:345 ; vC3:23).

### 1.4 IS, dividendes et option pour l'IR

| Règle | Contenu au 4 nov. 2026 | Effet sur le choix | Code et source |
|---|---|---|---|
| **Impôt sur les sociétés (IS)** | 15 % jusqu'à 42 500 € de bénéfice par période de 12 mois, puis 25 %. Conditions : CA ≤ 10 M€, capital **entièrement libéré**, détenu à 75 % au moins par des personnes physiques **ou par des sociétés qui remplissent ce critère**. Inchangé par la LF 2026 : son art. 15 ne touche que les titres de participation | Identique pour SAS et SARL. **Libérer tout le capital dès la constitution**. Une entrée de GianLuca par une société ne fait pas forcément perdre le taux réduit | [FV] vR1:21 ; vC3:26 |
| Premier exercice de plus ou de moins de 12 mois | Plafond de 42 500 € ajusté au prorata | Choisir la date de clôture avec l'expert-comptable | [DR] R1:98 |
| **Dividendes en SAS** | PFU de 31,4 % (CSG à 10,6 % depuis le 1er janv. 2026), ou barème avec abattement de 40 % ; aucune cotisation sociale | Levier possible à partir d'un bénéfice suffisant ; nul à 90 k€ | [FV] vR1:22 |
| **Dividendes du gérant majoritaire de SARL** | Cotisations TNS sur la part qui dépasse **10 % du capital, des primes d'émission et des comptes courants**. Base légale : art. L136-3 II 2° CSS (et non L131-6). La fiche F36065 est en retard sur ce point | Avec un capital modeste, ce **n'est pas un levier** : seuil de 200 € par an pour 2 000 € de capital | [FV] vR1:23 ; [ES] exemple |
| **Option pour l'IR** (art. 239 bis AB) | Société de moins de 5 ans, pour 5 exercices au plus. Conditions : ≥ 50 % des droits de vote à des personnes physiques, dont ≥ 34 % aux dirigeants ; accord de tous ; option dans les **3 premiers mois** | Ouverte aux deux formes. Une majorité extérieure ne la fait perdre que si une **société** dépasse 50 % ou si les dirigeants passent sous 34 % | [FV] vR1:24 ; vC3:41 |
| Cotisations en SARL à l'IR | Elles portent sur le bénéfice attribué, **même non retiré** | Risque de trésorerie personnelle. Ne pas retenir ce scénario sans rescrit FRR | [FV] V5 p. 20 ; vC3:69 |
| Option IR en SAS | Traitement social de la quote-part non vérifié ; scénario non simulé | À faire simuler | [IN] R1:156 ; C3:355 |

### 1.5 Souplesse, gouvernance et blocage

| Point | SARL | SAS | Code |
|---|---|---|---|
| Règles de fonctionnement | Largement fixées par la loi : gérance, majorités, agrément | Fixées librement par les statuts : organes, majorités, agrément, inaliénabilité (10 ans au plus, à l'unanimité), exclusion | [FV] F36022 (R1:298 ; vR1:29) ; [HY] étendue de la liberté |
| Blocage à 50/50 | Les décisions ordinaires, dont la nomination ou la révocation d'un gérant, n'ont pas de majorité sans accord. Chaque cogérant engage seul la société envers les tiers | Les statuts et le pacte peuvent prévoir médiation, tiers expert, voix prépondérante, offre alternative | [HY] R1:293 (art. L223-29 non rouvert) ; [PR] |
| Fixation des rémunérations | Décision collective : à 50/50, un désaccord bloque | Selon les statuts : organe désigné, plafond fixé dans le pacte | [HY] |
| Responsabilité | Limitée aux apports, sauf cautions personnelles et fautes de gestion | Idem | [FV] CS p. 2 (vC3:72) |
| Apports en industrie | Possibles selon les statuts (L223-7), hors capital | Possibles sous forme d'actions inaliénables (L227-1), hors capital. **Aucun des deux ne transfère de propriété intellectuelle** | [FV] R1:234-237 ; vR1:27 |
| Associé salarié ailleurs | Un gérant TNS reste redevable du minimum de cotisations | Mandat non rémunéré possible sans cotisation | [FV] V5 p. 20 ; offre-md:166 |

### 1.6 Entrée d'un investisseur, dont GianLuca Carlone

| Point | SARL | SAS | Code et source |
|---|---|---|---|
| Entrée d'un tiers | Agrément de la majorité des associés représentant au moins la moitié des parts | Libre par défaut, encadrée par les statuts (agrément, préemption) | [FV] F36015, F36022 (vR1:29) |
| Droits de cession | **3 %** après un abattement de 23 000 € × parts cédées / total des parts | **0,1 %** (minimum 25 €) | [FV] vR1:29 |
| Instruments | Pas d'actions de préférence | Actions de préférence, BSA ; BSPCE réservés aux sociétés par actions | [DR] R1:319, 333 (non vérifiés dans les textes) |
| Seuils à surveiller | IS à 15 % (75 % de personnes physiques ou de sociétés qui remplissent ce critère) ; option IR (50 % et 34 %) ; ACRE (contrôle effectif pendant **2 ans**) ; plafond de minimis du FRR apprécié par « entreprise unique » si GianLuca contrôlait Marwin | Idem | [FV] R1:323 ; vC3:26, 41 ; [HY] R2:231 |
| Conventions avec un associé important | Contrôle des conventions (L223-19) | Contrôle des conventions (L227-10) | [IN] non rouvert (R1:324) |

**Conclusion** [HY] : si une entrée de GianLuca Carlone au capital est sérieusement envisagée, la SAS s'impose (R1:337). La pièce de V5 qui fait de la SARL la « référence » le reconnaît : la SAS reste prioritaire « si l'entrée d'investisseurs et la souplesse des statuts deviennent prioritaires » (V5 p. 17 ; vC3:21).

### 1.7 Coûts de création et de fonctionnement

**Aucun montant ci-dessous n'a été vérifié** : ce sont des ordres de grandeur de marché [HY], à remplacer par des devis.

| Poste | SARL | SAS | Code |
|---|---|---|---|
| Formalités : greffe, bénéficiaires effectifs, annonce légale | Quelques centaines d'euros | Idem | [HY] |
| Statuts et pacte rédigés par un avocat | ≈ 1 500 à 4 000 € HT | ≈ 2 000 à 5 000 € HT (statuts plus libres, donc plus à écrire) | [ES] fondée sur [HY] |
| Expert-comptable, par an | ≈ 2 000 à 5 000 € HT | Idem, plus la paie du ou des dirigeants rémunérés (≈ quelques centaines d'euros par an) | [ES] fondée sur [HY] |
| Cotisations même sans revenu | ≈ 1 255 € par gérant et par an, et forfaits de la première année | 0 € | [ES] / [FV] § 1.2 |
| Entrée ultérieure d'un associé | 3 % (après abattement) et agrément | 0,1 % | [FV] |
| Passage ultérieur de la SARL à la SAS | Transformation (avocat, formalités) : coût et délai non relevés | — | [IN] |
| Commissaire aux comptes | Non requis sous les seuils légaux (seuils non revérifiés) | Idem | [HY] |

### 1.8 Trésorerie sociale (point omis par les pièces)

- **En SARL TNS** [ES], la première année se paie sur des forfaits (≈ 3 591 € par gérant), puis une **régularisation** suit sur le revenu réel (R1:43 ; C3:357). Sans ajustement des acomptes, l'écart à provisionner l'année suivante serait d'environ :
  - **12 000 €** par gérant à 120 k€ de CA ;
  - **20 000 €** à 180 k€ ;
  - **39 000 €** à 360 k€.

  Une estimation anticipée du revenu permettrait de réduire cet écart [HY], à valider avec l'expert-comptable.
- **En SAS**, les cotisations sont payées chaque mois avec le salaire. Il n'y a pas de régularisation, mais la charge est immédiate.
- **Ordre des sorties d'argent** proposé par V5 p. 20, à conserver [PR] : frais, puis rémunération avec provisions (cotisations, TVA, impôts), puis fonds de roulement, puis distribution (vC3:75).

### 1.9 Ce qui reste à simuler (par l'expert-comptable, sur mon-entreprise.urssaf.fr)

1. Les deux formes, aux trois niveaux de CA **et sur le seul contrat de 90 000 € HT**, avec les taux 2026 définitifs, puis **ceux de 2027**.
2. Le coût réel d'un président ou d'un directeur général de SAS rémunéré : taux, réduction dégressive unique de 2026 applicable ou non à un mandataire [IN] (vR1:41), taux AT/MP.
3. L'IR de chaque foyer (parts, autres revenus), et le choix entre PFU et barème [IN].
4. La protection sociale : retraite (points, trimestres validés avec une faible rémunération), indemnités journalières, prévoyance et mutuelle à souscrire [IN] (R1:79-82).
5. L'échéancier des cotisations TNS et le montant de la régularisation de l'année 2.
6. L'ACRE, si l'un des deux est éligible : environ 2 000 € par personne et par an au plus, nulle au-delà d'environ 65 000 € de coût total [ES] (R1:183, 196).
7. Le scénario de SAS à l'IR, jamais simulé (C3:355).
8. L'effet d'un associé salarié ailleurs ou chez le client sur l'ARE, l'ARCE et l'ACRE (vC3:70).

### 1.10 Recommandation conditionnelle [PR]

**Quatre questions décident de la forme :**

| Question | Si oui | Si non | Réponse au 4 nov. |
|---|---|---|---|
| Q1. Un investisseur (GianLuca ou un autre) entrera-t-il au capital dans les 24 mois, ou voulez-vous pouvoir associer un tiers ? | SAS | Neutre | **Évoqué** : GianLuca « envisage d'investir » [DR] (contexte:24) |
| Q2. Marwin paiera-t-elle aux deux une rémunération régulière dès les premiers mois, grâce à un contrat signé ? | SARL TNS (≈ 15 à 30 % de net en plus) | SAS (0 cotisation sans rémunération) | **Non** : aucun contrat, aucun payeur [FV] |
| Q3. L'un de vous vivra-t-il d'un emploi extérieur, y compris chez GianLuca ? | SAS, mandat non rémunéré | Neutre | **Évoqué**, comme souhait de Morgan et non du client [DR] (recueil:243, 248 ; vC3:34) |
| Q4. Le FRR sera-t-il confirmé par rescrit, avec l'essentiel des bénéfices retirés ? | Option IR à envisager (SARL ou SAS), 5 exercices | Option IR à écarter | **Inconnu** : adresse, moyens et origine de l'activité non établis [IN] (R2:227-231) |

**Recommandation.**
1. **Par défaut, sur les faits du 4 novembre : une SAS à l'IS**, avec :
   - un président et un directeur général, tous deux dirigeants avec au moins un tiers du capital (condition de l'ACRE) ;
   - un capital modeste, **entièrement libéré** ;
   - des statuts qui organisent le blocage, et un pacte signé avant le contrat client ;
   - une rémunération faible ou nulle tant qu'aucun contrat n'est signé, puis fixée par décision collective.
2. **Coût de ce choix** : environ 5 000 à 12 000 € de net par personne et par an à 120-180 k€ de CA, par rapport à une SARL TNS [ES]. C'est le prix de la souplesse, à confirmer par une simulation officielle.
3. **SARL en cogérance 50/50 à l'IS**, seulement si les réponses changent : pas d'investisseur avant 24 mois, rémunération régulière financée par un contrat signé d'au moins 120 k€ par an, aucun associé salarié ailleurs. Il faut alors provisionner la régularisation (§ 1.8).
4. **Micro-entreprise** : à écarter pour l'offre Carlone.
   - Elle est individuelle : risque de société créée de fait.
   - La TVA est due dès 41 250 € de CA.
   - Les frais réels ne sont pas déductibles.
   - Correction de vR1:30 : un dépassement des plafonds ne fait pas sortir du régime micro dès la première année, mais **la franchise de TVA est perdue dès le dépassement**.
5. **Ne pas immatriculer pour le seul dossier Carlone tant que l'entité payeuse n'est pas identifiée.** Il faut préparer les statuts et le pacte, puis immatriculer quand l'entité de GianLuca a confirmé par écrit (bon de commande ou lettre d'intention) [PR].

---

## 2. Réexamen des recommandations des 29 et 30 octobre

| # | Affirmation des pièces | Source | Verdict au 4 nov. 2026 | Ce qu'il faut écrire |
|---|---|---|---|---|
| 1 | SAS à l'IS « piste prioritaire » si l'entreprise doit être évolutive | CS p. 1, p. 7 | **Tient**, comme recommandation conditionnelle [PR] | La question posée (société ouverte ou revenu à deux) n'a jamais reçu de réponse [IN] (C3:34) |
| 2 | La SARL à gérance majoritaire à l'IS devient la « référence » | V5 p. 17, p. 20 | **Tient seulement comme référence provisoire** (« tant que le FRR et les situations personnelles ne sont pas établis ») | Faux de la traiter comme une décision (offre-md:155 ; contexte:12 ; audit-md:23) (vC3:21) |
| 3 | La SAS est « généralement plus coûteuse » | V5 p. 17 | **Exact en ordre de grandeur** pour une rémunération régulière (+15 à +30 % de net en SARL) [ES] | L'écart de 2 795 € de V5 p. 18 ne le mesure pas (vC3:22) |
| 4 | Nets annuels : 43 875 €, 51 408 €, 41 080 €… | V5 p. 18 | **Calculs cohérents, précision artificielle** ; base de 12 mois alors que le contrat dure 6 mois | Donner des fourchettes ; sur le seul contrat : ≈ 1 400 à 1 900 € par mois et par personne [ES] (C3:228 ; § 1.3) |
| 5 | Deux cogérants à 50/50 relèvent de la gérance majoritaire (TNS) | CS p. 2 (encadré) ; V5 p. 20 | **Confirmé** (Cass. 2018) [FV] | Le tableau de CS p. 2 (« assimilé salarié si […] égalitaire ») est à corriger |
| 6 | IS à 15 % jusqu'à 42 500 € | CS p. 3 | **Confirmé** [FV] | Ajouter : capital entièrement libéré ; 75 % de personnes physiques « ou sociétés répondant au critère » |
| 7 | PFU de 31,4 % | V5 p. 18 | **Confirmé** (LFSS 2026, art. 12) [FV] | — |
| 8 | Cotisations sur les dividendes de SARL au-delà de 10 % | CS p. 3 ; V5 p. 20 | **Confirmé** [FV] | Base légale : L136-3 II 2° CSS ; l'assiette comprend les primes et les comptes courants |
| 9 | Conditions de l'option pour l'IR | V5 p. 21 | **Confirmé** [FV] | « Une majorité extérieure ferait perdre l'option IR » (offre-md:146) est trop large (vC3:41) |
| 10 | ACRE à 25 %, plafonds de 36 045 € et 48 060 €, demande sous 60 jours, contrôle pendant 2 ans | V5 p. 24-26 | **Confirmé** (F11677 ; décret n° 2026-69) [FV] | ACRE réservée à des publics listés, dont une création en zone FRR. Le silence vaut accord pour les micro-entrepreneurs ; pour les dirigeants de société, c'est [IN] (vR1:25) |
| 11 | ARCE : 60 % des droits, 3 % de retenue, deux versements | V5 p. 23 | **Confirmé** [FV] | Ajouter : cumul de l'ARE plafonné à 60 % des droits restants depuis le 1er avril 2025 ; second versement incompatible avec un CDI à temps plein (vR1:26 ; vC3:70) |
| 12 | Cosne-Cours-sur-Loire classée FRR | V5 p. 21 | **Confirmé : FRR de base, pas FRR+** [FV] | Le classement de la commune ne vaut pas exonération pour Marwin (R2:171) |
| 13 | La règle des 25 % hors zone est présentée différemment par la FAQ et par Service Public | V5 p. 24 | **Tranché** par le BOFiP du 29/07/2026 : pour une activité sédentaire, au-delà de 25 %, **perte totale** de l'exonération [FV] | La fiche F31139 est imprécise (R2:29, 199) |
| 14 | « Une majorité extérieure peut fermer […] le FRR selon les conditions de détention » | offre-md:146 ; C3:352 | **Faux en l'état** : l'art. 44 quindecies A n'a pas de condition générale de détention en zone FRR de base [FV] | Vrais risques : plafond de minimis par « entreprise unique » [HY] ; activité transférée ou préexistante [FV] (R2:30) |
| 15 | Exonération de CFE votée par Cœur de Loire | V5 p. 21, 25 | **Source secondaire** (Pappers) [DR] | Le barème « cotisation minimum » de 250 € à 7 769 € est une **base** minimum, à multiplier par le taux local (vR2:14) |
| 16 | Aides régionales : avance remboursable à la création ; aide à l'investissement « de 20 % » | V5 p. 23 | **[DR] non revérifié** ; l'aide à l'investissement est **aussi** une avance remboursable (vC3:31) | Ne rien budgéter (bonne pratique de V5, C3:376) |
| 17 | « Carlone veut vous salarier et acheter des prestations » | V5 p. 20 | **Non sourcé du côté du client** : c'est le souhait de Morgan, « Je préfère être prestataire ou salarié […] être payé en plus par des missions de prestation » (recueil:248) [DR] | L'intention de GianLuca est [IN] (vC3:34) |
| 18 | Les gains d'automatisation servent « à réaliser davantage dans la capacité réservée ou **à ajuster le forfait** » | V5 p. 4 | **Engagement contraire à la demande** (rémunérer la valeur quand l'automatisation réduit le temps, DEMANDE.md § 11) | À retirer avant tout envoi (vC3:67) |
| 19 | Un même PDF réunit les pages pour le client et l'annexe interne sur les rémunérations | V5 p. 1, p. 17 | **Toujours vrai** [FV] | Ne jamais transmettre ce fichier tel quel (C3:344) |
| 20 | « Si le contrat doit être signé avant l'immatriculation, il l'est au nom de la société en formation » | offre-md:185 ; CS p. 6 | **Confirmé** (L210-6 ; Cass. com. 2023 et 2025) [FV] | Ajouter : **pas d'encaissement** avant l'immatriculation, et reprise formelle (vR1:28) |
| 21 | « Sans société, pas d'acompte possible » | contexte:12 | **Juste en pratique** [HY] : pas de SIREN, de numéro de TVA ni de compte ouvert à son nom. Service Public prévoit seulement une mention « Siret en cours d'attribution » (R2:394) | Signer « en formation » si nécessaire, encaisser après l'immatriculation |
| 22 | Norme ISO 10218-2:2025 comme référence pour un bras « près du public » | offre-md:100 ; contexte:97 | **Faux** : la norme exclut les dangers « when the public or non-working adults have access » [FV] | Analyse de risques propre au lieu, intégrateur, demande GN 6 (R5:41 ; vR5) |
| 23 | 238 bis AB : « achats jusqu'au 31/12/2028 inclus » | PASS:28 | **Faux à la lettre** : « avant le 31 décembre 2028 » [FV] | Corriger le CRM (vR2:26) |
| 24 | Exposer dans un lieu tiers « n'est pas explicitement prévu par le BOFiP » | `interne/offres-de-carlone-catalogue-crm.md:99` ; PASS:35 | **À préciser** : le BOFiP (§ 90) prévoit les manifestations d'un musée, d'une collectivité ou d'un établissement public, et le dépôt dans un musée ; il **ne cite pas une galerie commerciale** et exclut un lieu « réservé aux seuls clients » [FV] | Avis écrit avant toute prospection (R2:26) |
| 25 | L'exclusion des procédés autres que la main repose sur une doctrine archivée de 1995 | offre-md:292 | **Confirmé** par la doctrine en vigueur (BOI-TVA-SECT-90-10 du 20/03/2024, § 135, 140, 210) [FV] | (R2:27) |
| 26 | Marwin « gardez la majorité à vous deux » ; « un sujet, un accord » ; « n'échangez jamais une baisse d'honoraires contre une promesse d'investissement » | offre-md:132, 146, 149 ; contexte:93 | **Tient** [PR] | À inscrire dans le pacte et dans la stratégie de négociation (§ 4) |

---

## 3. Avant l'immatriculation

### 3.1 Société en formation et reprise des actes

- **Règles** [FV] (R1:260-264 ; vR1:28) :
  - la société n'existe qu'à son immatriculation (L210-6 C. com.) ;
  - ceux qui agissent en son nom avant sont **tenus solidairement et indéfiniment** des actes, sauf reprise ;
  - la reprise se fait par **état des actes annexé aux statuts** (R210-5 pour la SARL, R210-6 pour la SAS), par **mandat** donné pour des engagements déterminés, ou par décision des associés après l'immatriculation [DR pour ce troisième mode].
- **Jurisprudence** [FV] :
  - la mention « au nom de la société en formation » n'est plus une condition absolue : le juge apprécie l'intention commune (Cass. com., 29 nov. 2023, n° 22-12.865) ;
  - mais une reprise ne peut résulter « du seul accord » : les conditions légales s'imposent (Cass. com., 18 juin 2025, n° 24-14.311).
- **Ce qu'il faut faire** [PR] :
  1. Ne rien signer avec GianLuca Carlone avant l'immatriculation. À défaut, signer explicitement « au nom et pour le compte de Marwin Tech, [forme] en formation » et inscrire l'acte à l'état annexé (R1:279).
  2. **Ne pas faire porter le contrat par l'entreprise existante de Morgan**, dont la domiciliation est résiliée (Note 4 nov., § A) (R1:280). Cela brouillerait la propriété du client et des livrables, et pourrait faire de Marwin l'extension d'une activité préexistante (risque pour le FRR, R2:229 ; C3:348).
  3. Aucune exécution risquée avant la reprise : achats, données personnelles, accès aux systèmes du client (R3:280).
  4. Proposer à GianLuca de demander l'extrait K-bis avant de verser l'acompte : cela protège aussi le payeur (R1:281).
  5. Décrire fidèlement le travail déjà fait (CRM, catalogue, études), même non facturé. L'absence de facture ne prouve pas que l'activité n'a pas commencé (V5 p. 17 ; C3:56) [PR].

### 3.2 Liste de contrôle avant le premier euro facturé

| Sujet | Règle ou point | Échéance | Code et source |
|---|---|---|---|
| **Statuts et pacte** | Signés avant le contrat client ; pacte modifiable à l'unanimité | Avant la signature | [PR] R1:311 |
| **Capital et compte** | Dépôt des fonds sur un compte au nom de la société en formation ; libération minimale de 50 % (SAS) ou 20 % (SARL), mais **100 % pour l'IS à 15 %** ; fonds disponibles après l'immatriculation | À la constitution | [FV] R1:234, 113 ; [HY] modalités bancaires |
| Apports en nature (CRM, outils) | Commissaire aux apports évitable à l'unanimité si chaque apport ≤ 30 000 € et leur total ≤ la moitié du capital. **Par défaut, préférer une licence** à Marwin plutôt qu'un apport (§ 5 et § 6) | À la constitution | [FV] vR1:27 ; [PR] R1:252 |
| **RC professionnelle** | Non obligatoire en général, mais à souscrire **avant la première prestation**. Demander les exclusions IA, cyber et données, et faire correspondre le plafond contractuel au plafond assuré. Assurance du local **si Marwin est locataire** ; une convention de bureaux n'est pas forcément un bail | Avant la première prestation | [FV] F37365 ; [HY] vR3:40 ; [IN] exclusions (R3:281) |
| Prévoyance et homme-clé | Protection des dirigeants et rachat des parts en cas de décès ou d'incapacité | Avec le pacte | [PR] R1:295 |
| **Facture électronique** | **Réception** obligatoire pour toutes les entreprises depuis le 1er sept. 2026 : choisir une plateforme agréée et vérifier l'inscription à l'annuaire dès la création. **Émission** et e-reporting au plus tard le 1er sept. 2027. Porter dès la première facture les **4 nouvelles mentions** (SIREN du client, catégorie de l'opération, option pour les débits, adresse de livraison) : les sources se contredisent sur leur date | Dès la création | [FV] R2:286-302 ; vR2:35 ; [PR] R2:317 |
| Sanctions | 50 € par facture non électronique (plafond de 15 000 € par an) une fois l'obligation d'émettre en vigueur ; 500 € puis 1 000 € sans plateforme de réception | — | [FV] FAQ DGFiP (R2:290-292) |
| **TVA** | Franchise pour les services : 37 500 € (N-1), seuil majoré 41 250 € (N). À 15 000 € HT par mois, elle cesse **au 3e mois** de facturation. Le CA de l'année de création serait annualisé : la franchise pourrait tomber dès le 1er janv. 2027 [HY]. **Facturer la TVA dès la première facture** (option ou régime réel) | Dès la création | [FV] R2:330-341 ; [HY] vR2:36 ; [PR] R2:364 |
| TVA sur les acomptes | Exigible **à l'encaissement**, avec une facture d'acompte. Acompte de 7 500 € HT = 9 000 € TTC ; mois à 15 000 € HT = 18 000 € TTC | À chaque encaissement | [FV] R2:385 ; [ES] R2:416-417 |
| Conditions de paiement | Paiement d'avance et solde du mois 1 sous 7 jours : conformes à L441-10 [FV]. Pénalités ≥ 3 fois le taux légal (8,25 % au 2e semestre 2026) ; à défaut de clause, taux BCE + 10 points (12,40 %, puis ≈ 12,65 % au 1er semestre 2027 si la BCE ne bouge pas) ; indemnité de 40 € | Au contrat et sur les factures | [FV] R2:378-381, 414 ; [ES] vR2:37 |
| **CFE** | Pas due l'année de la création. Déclaration 1447-C-SD **avant le 31 décembre** de l'année de création pour obtenir la base réduite de 50 % l'année suivante. Montant : base minimum × taux local [IN] | 31 déc. de l'année de création | [FV] vR2:44 |
| **ACRE** | Publics listés, dont une création en zone FRR ; demande sous 60 jours ; contrôle effectif de la société pendant 2 ans | 60 jours | [FV] R1:177-180 |
| Option IR | Dans les 3 premiers mois de l'exercice | 3 mois | [FV] R1:153 |
| **Rescrit FRR** | Notification préalable (L80 B 2°) ; adresse et moyens réels en zone (une domiciliation chez un domiciliataire ne suffit pas, le domicile du dirigeant **en zone** est admis) ; part du travail hors zone ; origine de l'activité | Avant de compter l'exonération | [FV] R2:184 ; vR2:47-48 ; [IN] moment du dépôt (R2:230) |
| Bénéficiaires effectifs | Déclaration au Guichet unique | À l'immatriculation | [DR] CS p. 6 (C3:50) |
| Attestation de vigilance | Pièce que l'entité de GianLuca exigera à la signature puis tous les 6 mois. Délai d'obtention pour une société nouvelle : [IN]. L'accusé de réception R123-6 C. com. peut servir de justificatif d'immatriculation | Dès la signature | [FV] vR3:35 ; [IN] R3:179 |
| Dépôts et comptes techniques | Comptes GitHub, Firebase, IA et Notion **au nom de la société** (ou du client), plus au nom des associés | Avant la première prestation | [PR] R3:445 ; R4:259 |
| Mention « John-Lucas » [sic, lire GianLuca] | Corriger les pièces destinées au client (V5 p. 1, 5, 12) avant tout envoi | Avant tout envoi | [FV] C3:310-315 |

### 3.3 À ne pas faire

- Encaisser un acompte sur un compte personnel, ou au nom d'une société non immatriculée [HY] (R2:410).
- Présenter l'ACRE, l'ARE, l'ARCE, le FRR ou une aide régionale comme acquis (R1:196, 227 ; R2:234).
- Envoyer V5 au client : il mélange l'interne et le client, contient « John-Lucas » [sic, lire GianLuca], des images de façades parisiennes et de bras industriels qui ne correspondent pas au projet (vC3:35), et la clause sur les gains d'automatisation.

---

## 4. Relations à séparer : client, bailleur, employeur, investisseur

### 4.1 Faits

| Rôle prêté à GianLuca Carlone | État | Code et source |
|---|---|---|
| **Client** (CRM, accompagnement) | Aucune entité, aucun signataire, aucun payeur identifié ; aucun contrat ; CRM livré sans facture | [FV] audit-md:13-14 ; offre-md:16, 29 |
| **Bailleur** de bureaux | « Propose des bureaux » ; lieu inconnu, en zone FRR ou non | [DR] contexte:24, 108 |
| **Employeur** | Scénario présent dans V5 p. 20 ; intention du client non sourcée ; souhait de Morgan de cumuler (recueil:248) | [DR] / [IN] vC3:34 |
| **Investisseur** | « Envisage d'investir » ; aucune forme, aucun montant | [DR] contexte:24 ; C6:33 |
| Financeur de la R&D, de STRATES et du laboratoire | Options proposées ; STRATES retirée du diaporama le 4 nov. | [PR] offre-md:21-22 ; [DR] Note 4 nov. |
| Acquéreur de l'ancienne affaire de Medhi | « A racheté […] l'ancienne affaire de Medhi » | [DR] contexte:24 |

### 4.2 Risque de requalification en contrat de travail

- **Règle** [FV] (R3:64-67 ; vR3:32) :
  - les dirigeants d'une société immatriculée sont **présumés** non salariés (L8221-6 I) ;
  - la présomption tombe en cas de **subordination juridique permanente**, « directement ou par une personne interposée » (L8221-6 II) : la société Marwin ne fait donc pas écran ;
  - la subordination, c'est le pouvoir de donner des ordres, d'en contrôler l'exécution et de sanctionner (Cass. soc., 13 nov. 1996) ; travailler dans un « service organisé » n'en est qu'un indice.
- **Indices présents** [HY] (R3:74-79) :
  - un client unique ;
  - les bureaux du client ;
  - un prix au temps (« 20 journées-personnes », offre-md:13-16) ;
  - un périmètre « s'occuper de tout » (offre-md:52) ;
  - un salariat parallèle envisagé.
- **Conséquences** :
  - pour le donneur d'ordre (l'entité de GianLuca), si l'intention est établie : travail dissimulé, jusqu'à 3 ans et 45 000 € pour une personne physique, 225 000 € pour une société [FV] (vR3:33) ;
  - les cotisations patronales sur les sommes versées ne sont dues **qu'après condamnation pénale** [FV] (vR3:32) ;
  - **nouveau en 2026** : la condamnation pourra être **publiée en ligne pendant deux ans** par le ministère, une fois le décret pris [FV] (loi n° 2026-534 ; vR3:33) ;
  - pour Morgan et Mathys : la relation passe sous le droit du travail, et les factures et simulations perdent leur objet [HY] (R3:83).

### 4.3 Prêt de main-d'œuvre illicite et marchandage

- **Règle** [FV] (R3:113-115 ; vR3:34) :
  - le prêt de main-d'œuvre à but lucratif et à objet exclusif est interdit (L8241-1) ;
  - le marchandage est puni (L8231-1) ;
  - peines : 2 ans et 30 000 € ; 150 000 € pour une société. Les peines principales sont **inchangées** en 2026 : seule la peine complémentaire d'affichage a été modifiée.
- **Situations à risque** [HY] (R3:123-126) :
  - des tiers (freelances, futurs salariés) placés par Marwin chez le client et dirigés par lui ;
  - les **opératrices de Quali Contact** qui recevraient leurs consignes directement de Marwin ou de GianLuca ;
  - la « coordination des prestataires locaux » si elle devient un commandement direct.
- **Règle de conduite** [PR] (R3:146-148) :
  - tout intervenant travaille sous l'autorité de son propre employeur, sur un lot défini, avec un prix au livrable ou à une capacité engagée sur des livrables ;
  - la liste des livrables du mois précède la liste des heures.

### 4.4 Dépendance économique et rupture brutale

- **Règle** [FV] (R3:233-235 ; vR3:39) :
  - rompre brutalement, même partiellement, une relation commerciale établie sans préavis écrit suffisant engage la responsabilité de son auteur (L442-1 II) ;
  - un préavis de 18 mois met à l'abri de toute contestation sur la durée ;
  - **nouveau depuis le 20 août 2026** : une **réduction substantielle des volumes commandés pendant une négociation**, même temporaire, peut aussi engager la responsabilité de son auteur. Par exemple, passer de 40 à 20 journées.
- **Portée** [HY] :
  - la règle joue dans les deux sens ;
  - un contrat de 6 mois à peine commencé est rarement une relation « établie » ;
  - l'abus de dépendance économique (L420-2) suppose un effet sur la concurrence : il est peu utile ici.
- **La vraie protection est contractuelle et commerciale** :
  - un préavis gradué et réciproque ;
  - une réduction de périmètre plutôt qu'un arrêt ;
  - le paiement des travaux engagés et de la réversibilité ;
  - un **deuxième client avant le 4e mois** (contexte:95) et un plafond de dépendance suivi chaque mois [PR] (R3:258-260).

  La question « part maximale des revenus venant de Carlone » est restée sans réponse (« 10 millions », contexte:129) [FV].

### 4.5 Vigilance Urssaf

- **Obligation de l'entité de GianLuca envers Marwin** [FV] (R3:155-158 ; vR3:35) :
  - elle s'applique à tout contrat **d'au moins 5 000 € HT** (R8222-1), et l'offre de base vaut 90 000 € HT ;
  - elle doit obtenir, **à la signature puis tous les 6 mois**, une attestation Urssaf de moins de 6 mois dont elle vérifie l'authenticité, et un justificatif d'immatriculation (D8222-5) ;
  - sanctions : solidarité financière, et annulation de ses propres réductions de cotisations (plafonnée à 15 000 € ou 75 000 € sans antécédent).
- **Obligation de Marwin** envers Medhi, des freelances et tout sous-traitant, dès 5 000 € HT cumulés [PR] (R3:185).
- **Nouveau L8222-1-1** [FV] (vR3:36) :
  - en vigueur par décret, au plus tard fin décembre 2026 ;
  - il vise seulement les sous-traitants **acceptés** par un maître d'ouvrage au titre de la loi de 1975, au-delà d'un montant fixé par décret ;
  - la loi ne parle pas de vigilance « en cascade ».
- **Argument commercial** : proposer un dossier de conformité (attestation, K-bis) à la signature, puis aux mois 6 et 12 [PR].

### 4.6 Salariat chez le client et prestation de Marwin

**Possible en droit, mais c'est le scénario le plus risqué** [HY] (R3:193-197 ; vR3:38).

**Règles** :
- loyauté du salarié : une activité **concurrente** constitue une faute grave, même sans clause de non-concurrence (Cass. soc., 14 janv. 2026, arrêt **inédit**) ;
- conflit d'intérêts : un salarié du client ne doit ni commander, ni valider, ni payer les prestations de Marwin ;
- les logiciels créés par un salarié dans ses fonctions appartiennent à **l'employeur** (L113-9 CPI) [FV] ;
- le second versement de l'ARCE peut être incompatible avec un CDI à temps plein (vC3:70) [FV].

**Recommandation** [PR] (R3:224) :
- différer tout salariat au-delà du bilan des mois 3 à 6 ;
- s'il le faut : une seule personne, des fonctions non couvertes par le contrat Marwin, des temps séparés, et une validation des livrables Marwin par une autre personne côté client ;
- ne pas s'en servir comme argument de négociation des honoraires.

### 4.7 « S'occuper de tout » : activités réservées à ne pas exercer

Le volet « Piloter » (offre-md:52) touche des activités réglementées. Marwin peut **préparer, organiser et coordonner**. Elle ne doit pas les **exercer** [HY fondé sur des textes FV] (R3:349-358 ; vR3:41).

| Activité | Texte | Ce que Marwin peut faire [PR] |
|---|---|---|
| Expertise comptable (tenue, révision des comptes) | Ord. n° 45-2138, art. 2 et 20 ; peines de 433-17 C. pén. ; la personne morale est aussi responsable (433-25) | Tableau de bord à partir des données du client ; préparation des pièces pour son expert-comptable |
| Consultation juridique et rédaction d'actes pour autrui | Loi n° 71-1130, art. 54 | Dossier factuel et questions pour l'avocat. **Les calculs d'« économie d'impôt » envoyés aux prospects sont à faire valider** (R3:362) |
| Gestion immobilière (loi Hoguet) | Loi n° 70-9, art. 1 | Coordination d'un administrateur de biens ; pas de baux ni de loyers. GianLuca « a racheté six bâtiments » [DR] |
| Vente de voyages et séjours | C. tourisme L211-1 | Le client réserve et paie lui-même les « séjours des invités » |
| Recouvrement amiable | CPCE R124-2 | Relances signées par le client ; encaissement sur ses comptes |
| Maniement de fonds | [IN] (services de paiement) | À éviter par construction : Marwin ne détient pas les fonds du client |
| Intermédiaire en biens divers | AMF [DR] (montant de 8 000 € non revérifié) | Ne jamais promettre rendement, plus-value ou rachat (contexte:91) |

**Mandat de dépense.** Il faut rétablir la grille détaillée du 29 octobre (accomp:92-103) plutôt que la ligne du 2 novembre (offre-md:208) [PR] (R3:312, 338) :
- un mandat écrit par entité ;
- une liste fermée d'actes, avec un plafond par acte et un plafond cumulé ;
- des factures au nom du client et payées par lui ;
- un registre des engagements ;
- « une absence de réponse ne vaut pas approbation ».

Pour la TVA, les **débours** supposent quatre conditions cumulatives (BOFiP BOI-TVA-BASE-10-10-30, § 200) [FV].

### 4.8 Préserver la décision et la sortie [PR]

| Moyen | Contenu | Source |
|---|---|---|
| **Un accord par sujet** | Contrat de prestation, convention de bureaux, achats directs du client, pacte d'investissement : chacun avec sa durée, son prix et sa sortie | offre-md:132 ; diaporama `cadre.html` [PR] |
| Pas de lien entre les accords | Aucune clause qui fait tomber les honoraires si les bureaux s'arrêtent, ou l'inverse. Seule exception : un délai de restitution des locaux aligné sur le préavis | R3:259 |
| Convention de bureaux | Accès sans horaires imposés ; usage partagé ; assurance ; restitution ; gratuit ou avec loyer ; base de la CFE ; preuve des moyens en zone pour le FRR | offre-md:136 ; R2:236 ; R2:275 |
| Investissement | Pas avant 12 à 24 mois ; minoritaire ; sans veto opérationnel ; droit d'information ; contrat client résiliable indépendamment ; **jamais en échange d'une baisse d'honoraires** ; l'acompte n'est ni du capital ni un prêt | R1:337 ; offre-md:142, 149 |
| Majorité aux fondateurs | Garder au moins la majorité, et ≥ 34 % aux dirigeants si l'option IR est retenue | offre-md:146 ; vC3:41 |
| Gouvernance côté client | Une personne qui valide les livrables, distincte d'un éventuel fondateur salarié | R3:224 |
| Sortie | Préavis gradué et réciproque ; réversibilité chiffrée ; licences sur les composants génériques qui survivent à la fin du contrat | R3:258 ; R3:447 |
| Signaux d'alerte à suivre | Horaires imposés, place dans un organigramme, compte rendu à un cadre comme un salarié, exclusivité de fait, baisse brutale des volumes | R3:106 ; vR3:39 |

---

## 5. Entre Morgan et Mathys : faits et clauses de pacte

### 5.1 Faits connus

| Sujet | État | Code et source |
|---|---|---|
| Associés, parts, mandats | Rien n'est décidé ; une variante « Matisse » a circulé pour le second associé | [FV] V5 p. 17 ; CS p. 5 (C3:52) |
| Disponibilité de Morgan | Plusieurs projets menés en parallèle (OLSEN, « Shelby », Côme Millot, vente en ligne personnelle, vente en ligne, etc.) ; disponibilité pour Carlone non documentée | [FV] Note 4 nov., § A et B |
| Disponibilité de Mathys | Aucune donnée | [IN] Note 4 nov., § B |
| Rôles | Morgan : programme et prix ; Mathys : technique et CRM ; « tout comme moi » pour le rôle de Mathys | [PR] offre-md:224 ; [DR] contexte:129 |
| Point de dépendance unique | Morgan pilote et valide seul les notes ; le rôle de Mathys reste « à préciser » | [DR] V5 p. 6, 12 (C3:363) |
| CRM | Co-écrit par Mathys ; 48 commits signés « Claude » du 27 au 30 oct. ; dépôt d'origine au compte FinanceScope, présenté comme celui de Mathys ; aucun fichier de licence dans `crm/` | [DR] contexte:26 ; [FV] vC5:21 ; [DR] C5:60 ; [FV] R3:402 |
| Jarvis et BOJART | Dépôt public sans licence globale (« Aucune licence globale nouvelle n'est imposée ») ; commits du compte « Momolscode » ; Jarvis est aussi le nom d'un livrable client | [FV] `BOJART:jarvis/LICENSE_SCOPE.md:2` ; `git log` ; [HY] Momolscode = Morgan ; C3:247 |
| Conflit d'intérêts | Morgan orchestre BOJ.ART et rédige le catalogue de vente de GianLuca, qui proposait des pièces de Medhi | [DR] contexte:25 ; C6:258 |
| Cibles de revenu | 2 500 €, 3 660 € ou 7 500 € nets par mois : l'objectif de 7 500 € est attribué aux fondateurs, sans savoir s'il s'entend avant ou après IR | [DR] / [IN] vC3:25 ; contexte:119 |

### 5.2 Clauses de pacte (et de statuts)

Toutes sont des propositions [PR], à rédiger et à faire valider par l'avocat.

| Thème | Clause proposée | Point juridique | Source |
|---|---|---|---|
| **Disponibilité** | Temps minimal engagé par mois, en journées ; relevé mensuel ; déclaration écrite des autres activités ; règle de priorité pour les clients de Marwin ; non-concurrence pendant le mandat, limitée aux clients et à l'objet de Marwin | Une clause de non-concurrence d'associé doit être proportionnée [HY] | R1:292, 294 ; Note 4 nov. |
| **Apports** | Numéraire à parts égales, **entièrement libéré**. Apport en industrie possible pour compenser un temps inégal (actions inaliénables en SAS), **sans effet sur la propriété intellectuelle** | Commissaire aux apports pour un apport en nature, sauf exception | R1:234-237 ; vR1:27 |
| **Travail existant** (CRM, Jarvis, catalogue, études, code) | **Inventaire daté des actifs préexistants** de chacun. Pour chacun : licence à Marwin (par défaut : non exclusive, durée du pacte, usage pour les clients de Marwin) ou cession écrite. Distinguer les co-auteurs (CRM) ; régler le cas de Jarvis (périmètre BOJ.ART et Medhi d'un côté, Morgan de l'autre) ; vérifier la disponibilité du nom « Jarvis » [IN] | Cession écrite, « mention distincte » et domaine délimité (L131-2, L131-3) ; une cession gratuite doit être expresse ; la protection du code généré par IA est [IN] | R3:393-407 ; vR3:42 ; CS p. 4 |
| **Travail futur pour Marwin** | Chaque associé cède ou concède à Marwin ses créations faites pour elle, livrable par livrable. **Pas de cession globale des œuvres futures**. Le régime des logiciels de salariés (L113-9) ne joue pas pour un dirigeant non salarié | L131-1 : cession globale nulle ; [HY] sur L113-9 | R3:395-396 |
| **Rémunérations différentes** | Rémunération liée au temps engagé et à la fonction ; grille écrite ; dividendes au prorata du capital, sauf actions de préférence en SAS ; décision par l'organe fixé dans les statuts, avec un plafond inscrit au pacte | En SARL, la décision collective peut bloquer à 50/50 [HY] | R1:292 |
| **Désaccord et blocage** | Liste des décisions importantes, prises à l'unanimité : contrat avec GianLuca, engagement de plus de X €, entrée d'un associé, recrutement. Puis médiation, tiers expert, et en dernier recours une **offre alternative** (« shotgun ») ou un rachat à dire d'expert | Validité et exécution forcée à vérifier : un pacte non respecté donne surtout lieu à des dommages-intérêts [HY] | R1:293, 307 |
| **Relation avec le client** | Qui parle à GianLuca, qui signe, qui engage une dépense, qui valide une remise | — | R1:312 |
| **Départ** | Préavis ; transmission des dossiers et des accès ; non-sollicitation des clients ; non-concurrence limitée et rémunérée si nécessaire ; prix de rachat différent selon le motif du départ (« good / bad leaver ») | Articulation avec l'expertise de l'art. 1843-4 C. civ. [IN] | R1:294, 297 |
| **Incapacité ou décès** | Rachat des titres ; assurance homme-clé ; intérim de direction ; **coffre partagé des accès et secrets** ; délégation de signature croisée | Les indemnités journalières TNS sont plafonnées à 65,84 € après 3 jours | R1:295 ; § 1.2 |
| **Cessions** | Agrément, préemption, sortie conjointe ; inaliénabilité de 10 ans au plus en SAS | F36022 | R1:298 |
| **Investisseur** | Droit d'information ; pas de veto opérationnel ; séparation entre client et associé | — | R1:299 |
| **Conflits d'intérêts** | Déclaration écrite des liens avec BOJ.ART, Medhi, OLSEN et toute entité de GianLuca ; abstention lors des décisions concernées ; information du client | — | C6:258 |
| **Comptes et données** | Comptes techniques au nom de Marwin ; aucun compte personnel pour les données d'un client | RGPD, art. 28 et 32 | R4:259 |

---

## 6. Propriété et droits d'utilisation

**Principe** [FV] : commander et payer ne suffit pas à rendre le client propriétaire. La conclusion d'un contrat d'ouvrage « n'emporte pas dérogation » aux droits de l'auteur (L111-1). Il faut une **cession écrite**, chaque droit mentionné distinctement (L131-2, L131-3), et aucune cession globale des œuvres futures (L131-1) (R3:393-396 ; vR3:42).

**Architecture prévue** : trois registres (outils préexistants, composants réutilisables de Marwin, développements propres au client), cédés ou concédés au paiement complet (offre-md:209 ; CS p. 4) [PR]. Elle est saine, mais il manque la liste des droits, la durée, le territoire, l'exclusivité et les licences tierces (R3:407).

| Actif | État et titulaire probable | Risque | Régime recommandé [PR] | Code et source |
|---|---|---|---|---|
| **Code du CRM** | Co-écrit par Morgan et Mathys, en grande partie produit par des agents IA ; aucune licence ; dépôt public au compte FinanceScope ; version Firebase « sous le compte des associés » ; « offert à ce jour » | Titulaire réel [IN] ; part protégeable du code généré [IN] ; le client paie la suite sans droit sur la base | Cession des associés à Marwin, ou licence. Puis, avec GianLuca : licence d'usage perpétuelle et non exclusive, ou cession des développements propres au client au paiement. **Écrire le régime du CRM « offert »**, même gratuit | [FV] R3:402 ; offre-md:37, 227 ; [DR] rapport-crm:19 |
| **Données du CRM** (500 entreprises, dirigeants, coordonnées) | « Le code, les données et le suivi restent chez les associés » (rapport-crm:19). Fonctionnellement, les données appartiennent au **responsable du traitement**, qui serait l'entité vendeuse de GianLuca [HY] | Phrase incompatible avec un rôle de sous-traitant ; droit du producteur de base de données (L341-1) non examiné [HY] | Données au client, en restitution ou suppression à son choix (RGPD 28.3 g) ; Marwin n'en garde aucune copie après la mission | R4:193 ; R3:406 |
| **Outils préexistants** (Jarvis, scripts, méthodes, modèles de documents) | Propriété de leurs auteurs. Jarvis : périmètre BOJ.ART et Medhi d'une part, Morgan d'autre part, non tranché ; dépôt BOJART public **sans licence** : les droits sont réservés par défaut [HY] | Vendre « Jarvis » sans inventaire de ses composants et de leurs licences ; confusion entre le nom d'un actif tiers et celui d'un livrable | Inventaire des composants et des licences ; licence de l'auteur à Marwin ; pour le client, licence d'usage non exclusive. Clarifier le nom | [FV] LICENSE_SCOPE.md:2 ; C3:247, 361 |
| **Composants réutilisables de Marwin** | À créer après l'immatriculation | Revendication du client, ou de son employeur si un fondateur est salarié (L113-9) | Marwin reste propriétaire ; licence non exclusive, perpétuelle et gratuite pour l'usage interne du client, maintenue après la fin du contrat | R3:407 ; R3:205 |
| **Développements propres au client** | À créer | Le client paie mais dépend de Marwin | **Cession par livrable**, à la réception et au paiement complet ; annexe des droits (étendue, destination, lieu, durée) ; code source, documentation et comptes remis | R3:426 |
| **Contenus** (catalogue d'offres, textes, supports, études) | Produits pour GianLuca sans commande ni prix connus | Mélange avec les pièces internes (V5) ; mentions fiscales non validées | Cession des contenus livrés au paiement ; contenus fiscaux validés par un professionnel avant usage | C6:39 ; R3:362 |
| **Œuvres de Medhi** (sculptures, motifs, STRATES) | À Medhi : « ses œuvres, ses droits d'auteur, ses machines » (offre-md:90). **Depuis le 4 nov., hors de l'offre Marwin** [DR] | L'offre écrite et STRATES v1.1 promettent encore à la galerie une « exclusivité de vente » et « l'usage des films de fabrication » (offre-md:94) : **Marwin ne peut pas céder ce qu'elle ne détient pas** | Retirer ces promesses des documents de Marwin. Toute vente de ses pièces par la galerie : contrat de dépôt-vente direct entre Medhi et l'entité de GianLuca | R3:405 ; R5:249 |
| **Fichiers de fabrication** (STL, parcours de bras, réglages, fiches matière) | Mêlent le motif de l'artiste (ses droits) et la technique (Marwin ou l'atelier) | Reproduction d'une œuvre sans autorisation de l'auteur | Contrat à trois, ou aucune utilisation par Marwin, maintenant que Medhi est retiré ; licence limitée à la fabrication autorisée | [HY] |
| **Films et images** | Films de concept générés avec un outil d'IA (Kling via Higgsfield, STRATES v1.1 p. 8) ; visuels du vernissage ; images V5 p. 5, 9 et 15 | Droits des artistes montrés (L131-3) ; **droit à l'image des invités** (le film de la soirée envoyé par le CRM, vernissage:25) ; conditions d'utilisation de l'outil d'IA [IN] ; mention « généré par IA » (AI Act, art. 50, § 4) | Autorisation écrite de chaque artiste ; consentement des personnes filmées ; étiquetage IA ; conditions d'utilisation des outils vérifiées | R5:248 ; R4:314 ; vC3:35 |
| **Matériel** (station, bras, banc) | « Acheté et possédé par votre entité » (diaporama `garanties.html`, `cadre.html`, `laboratoire.html`) | Si Marwin achète puis refacture, le matériel entre dans son CA et elle porte le risque ; si Marwin assemble une machine, elle peut devenir **fabricant** | Achats directs par l'entité cliente ; machines de BOJ.ART à leurs propriétaires ; un intégrateur tiers porte la conformité | offre-md:138 ; R5:496-499, 543 |

**Réversibilité.** Le diaporama promet : « Réversibilité : fichiers, configurations, documentations et accès remis » (`garanties.html`) [PR]. C'est inexact tant que le CRM reste hébergé sous le compte des associés (R3:438).

**Data Act** [FV] (R3:437 ; vR3:43). Si Marwin héberge et exploite un service de traitement de données pour le client :
- l'art. 25 impose des clauses de changement de fournisseur : préavis de 2 mois au plus, transition de 30 jours au plus, au moins 30 jours pour récupérer les données ;
- cette obligation vaut **même pour un service sur mesure** ;
- à partir du 12 janv. 2027, aucuns frais de changement ne sont permis.

Solution la plus simple [PR] : comptes au nom de l'entité cliente dès le départ, Marwin y intervenant comme collaborateur (R3:442, 463).

---

## 7. Galerie, œuvres et événements : obligations réellement applicables

**Principe** [PR] (R5:402, 467) : ce sont des obligations d'**exploitant, de vendeur ou d'organisateur**. Elles incombent à l'entité de GianLuca qui vend, organise ou exploite le lieu. Cette entité n'est pas identifiée [IN] (C6:38 ; vC5:24).

Marwin coordonne sous mandat écrit, sans être titulaire des autorisations, sans encaisser, sans garder d'œuvres et sans fabriquer de machine. Sinon, elle porte elle-même ces obligations.

| Obligation | Contenu au 4 nov. 2026 | À qui elle incombe | Quand Marwin y serait soumise | Code et source |
|---|---|---|---|---|
| **Registre des objets mobiliers** (« livre de police ») | Pour toute vente d'objets acquis auprès d'autres personnes que leurs fabricants ; tenue jour par jour ; déclaration préalable en préfecture ; registre informatisé conservé 10 ans ; 6 mois et 30 000 €, 150 000 € pour une personne morale (via 131-38) | Entité qui vend ; **personnellement ses dirigeants** si c'est une société (art. 321-7, al. 3) | Si elle achetait pour revendre | [FV] R5:52 ; vR5:33 ; [HY] galerie qui ne vend qu'en premier marché |
| **LCB-FT** | Marchands et intermédiaires d'œuvres, galeries comprises, dès **10 000 €** : identification du client et du bénéficiaire effectif, personnes politiquement exposées, cartographie des risques, déclarant Tracfin, déclaration de soupçon, conservation 5 ans. Espèces limitées à 1 000 € pour un client domicilié en France. Contrôle par la douane (DGDDI). AMLR le 10 juill. 2027 | Entité qui vend | **Si elle trouve des acheteurs contre commission ou encaisse pour la galerie** | [FV] R5:55-65 ; vR5:34-35 ; [HY] R5:193 |
| **Droit de suite** | Seulement pour les **reventes** avec un professionnel : dès 750 €, 4 % jusqu'à 50 000 €, puis taux dégressifs, plafond de 12 500 € ; à la charge du vendeur. Paiement par le vendeur professionnel, à défaut l'intermédiaire qui encaisse, à défaut l'acheteur professionnel ; aux enchères, l'opérateur. Pas dû sur une première vente en dépôt pour l'artiste | Entité qui vend | Si elle est l'intermédiaire qui reçoit le paiement (R122-9) | [FV] R5:66-71 ; vR5:36 |
| **Contribution des diffuseurs** | 1 % + 0,1 % de 30 % du prix TTC, ou de la commission TTC en dépôt-vente ; **déclaration annuelle avant le 1er mai, même à néant** ; reproductions purement mécaniques exclues | Galerie | — | [FV] vR5:38 ; [HY] pièces imprimées en 3D |
| **Certificat d'authenticité** | **Aucune obligation légale** de certificat séparé. Décret Marcus : facture détaillée si l'acheteur la demande ; une signature engage la garantie d'auteur ; mention « Reproduction » obligatoire | Vendeur | — | [FV] vR5:37 ; [HY] R5:72 |
| Description du procédé | Une pièce faite à la machine doit être décrite comme telle (impression, bras). « Peint par l'artiste » engagerait la garantie et la qualification fiscale | Vendeur | — | [HY] R5:137 |
| **Rétractation des petites entreprises** | Vente **hors établissement** à une entreprise de **5 salariés au plus**, dont l'objet sort de son activité principale : information précontractuelle, contrat et formulaire ; **14 jours** de rétractation ; **aucun paiement avant 7 jours** ; délai prolongé de 12 mois si l'information manque. Exceptions : œuvre sur mesure, enchère publique [HY]. Vente à distance non visée | Entité qui vend | — | [FV] R5:257-273 ; vR5:39 |
| Vernissage en entreprise (offre 5 du catalogue) | Chaque vente conclue pendant la soirée est hors établissement : elle n'est pas définitive avant 14 jours | Entité qui vend | — | [FV] R5:309 |
| **Établissement recevant du public (ERP)** | Classement par type et catégorie (galerie M ou T : 5e catégorie jusqu'à 200 personnes ; cabaret L : 50). Visite de réception et arrêté du maire. Autorisation de travaux (4 mois). **Demande GN 6 au moins deux mois avant** une manifestation inhabituelle ou une démonstration à risque, présentée conjointement par l'exploitant et l'**utilisateur occasionnel** | Exploitant du lieu, et organisateur pour GN 6 | Si elle était organisatrice ou utilisatrice des locaux | [FV] R5:318-334 ; vR5:40-41 |
| Calendrier | **Pas d'événement public en décembre 2026 dans un lieu non autorisé** : 2 à 3 mois dans un ERP ouvert, 4 à 6 mois ou plus dans un bâtiment à aménager. Contredit les « dates en décembre » (dossier du 21 oct. p. 32) | — | — | [ES] R5:353, 361-367 |
| **Boissons** | Débit temporaire : autorisation du maire, 18° au plus. Licence IV : création interdite, rachat ou transfert. Permis d'exploitation de 20 h. Déclaration 15 jours avant. Ratio d'un débit pour 450 habitants (3e et 4e catégories ensemble) | Exploitant ou organisateur | — | [FV] R5:335-339, 426-430 ; vR5:52 |
| **Spectacles** | Jusqu'à 6 représentations par an sans déclaration, récépissé dès la 7e (un mois d'opposition) ; artistes présumés salariés (Guso) ; formation à la sécurité pour l'exploitant d'un lieu | Organisateur, exploitant | — | [FV] R5:340-344 ; vR5:42 |
| **Musique** | Autorisation Sacem et rémunération Spré, y compris pour une musique d'ambiance | Organisateur | — | [FV] R5:345-348 |
| **« Enchères » en fin de soirée** | L'appellation « ventes aux enchères publiques » est réservée aux opérateurs habilités (L321-2 C. com.). Idées « mise aux enchères » et « enchère du premier trait » (vernissage:81, 89) | — | — | [FV partiel] R5:44, 360 → avocat |
| **Assurances** | RC de l'organisateur : pas d'obligation générale trouvée, indispensable en pratique. Assurance « clou à clou » : pratique de marché, valeur agréée par œuvre. **Un dépositaire rémunéré répond « avec plus de rigueur »** (C. civ. 1928) | Organisateur ; galerie dépositaire | Si elle transportait ou gardait des œuvres | [HY] R5:210, 349 ; vR5:61-62 |
| **Contrat de dépôt-vente avec les artistes** | Aucun contrat type légal ; inventaire, prix plancher, commission, garde, assurance, droits de reproduction écrits, restitution | Entité de GianLuca et chaque artiste | Si elle signait à leur place | [HY] R5:204-226 ; [PR] R5:246 |
| **Robot devant le public** | Règlement machines au 20 janv. 2027 ; celui qui assemble un bras avec un outil et une commande **fabrique une machine** (marquage CE, documentation) ; ISO 10218-2 ne couvre pas le public ; nouvelle responsabilité du fait des produits pour les produits mis sur le marché après le 8 déc. 2026, logiciel compris | Fabricant, intégrateur, exploitant | **Si Marwin assemble et remet le bras** : elle devient fabricante | [FV] R5:477-492 ; vR5:44 ; [HY] R5:496 |
| Biens culturels importés | Licence ou déclaration de l'importateur depuis le 28 juin 2025 (surtout pour les biens anciens) | Importateur | — | [FV partiel] R5:74 |

**Effet du retrait de Medhi.** Le programme STRATES, le « geste » du bras, les fragments imprimés par son parc et la vente de ses pièces sont sortis de l'offre de Marwin (Note 4 nov., § C) [DR]. Les obligations ci-dessus s'appliquent donc à la galerie et à Medhi, plus à Marwin. Mais tant que le document du vernissage et STRATES v1.1 circulent sous le nom de Marwin, celle-ci paraît organisatrice ou co-productrice. Il faut les **marquer comme historiques ou les retirer** [PR].

---

## 8. Arguments fiscaux pour les entreprises : ce qui est validé, ce qui ne l'est pas

### 8.1 Validé [FV] (R2:13, 38-43 ; vR2:26-30)

| Point | Contenu |
|---|---|
| **238 bis AB prorogé** | Achats faits **avant le 31 déc. 2028** (LF 2026, art. 89) |
| Bénéficiaires | Sociétés à l'IS et sociétés de personnes ; activités en BNC exclues |
| Mécanisme | Œuvre originale d'un artiste vivant, inscrite à l'**actif immobilisé** (jamais en stock) ; déduction par cinquièmes sur 5 exercices ; réserve spéciale ; réintégration en cas de cession ou d'arrêt de l'exposition |
| Plafond | 20 000 € ou 5 ‰ du CA, le plus élevé des deux, **diminué des dons de mécénat** ; l'excédent est perdu ; le plafond est **commun à toutes les œuvres** en cours de déduction |
| Exposition | 5 ans, dans un lieu accessible au public ou aux salariés, **hors bureaux** ; pas dans un lieu « réservé aux seuls clients » ; manifestations organisées par l'entreprise ou par un tiers (musée, collectivité, établissement public) ; dépôt dans un musée |
| Œuvre originale (art. 98 A, annexe III) | Peinture « entièrement exécutée à la main par l'artiste » ; sculpture « exécutée entièrement par l'artiste » ; 8 fontes au plus ; 30 photographies au plus |
| Doctrine en vigueur (20/03/2024) | Exclut tout procédé qui supplée la main « en tout ou en partie » et les œuvres « exécutées par des moyens mécaniques » ; une réponse ministérielle de 2021 exclut les créations numériques imprimées |
| Rescrit | Rescrit général (L80 B 1°) : réponse en 3 mois en principe, **le silence ne vaut pas accord** |
| **Mécénat** (238 bis) | Autre dispositif : **réduction** d'impôt de 60 % (40 % au-delà de 2 M€) pour un **don sans contrepartie à un organisme d'intérêt général** ; les dons aux artistes, personnes physiques, sont exclus |
| **TVA des œuvres** | 5,5 % sur toutes les livraisons depuis le 1er janv. 2025, sauf sous le régime de la marge. Franchise propre aux artistes-auteurs : 50 000 € / 55 000 €. Transfert dans le CIBS au 1er janv. 2027, références au CGI utilisables jusqu'au 30 juin 2028. Les prestations de Marwin sont à 20 % |

### 8.2 Non validé, ou à faire trancher

| Argument | Statut | Ce qu'il faut faire | Code et source |
|---|---|---|---|
| Pièces imprimées en 3D, peintes par robot ou générées par IA, dont STRATES | **Très probablement exclues** de la déduction et du taux de 5,5 % (taux de 20 % probable) | Vendre par la galerie sans argument fiscal, ou rescrit sur une pièce précise | [HY] R2:66-71, 129 |
| Fonte tirée d'un modèle imprimé en 3D | Douteuse | Rescrit | [HY] R2:69 |
| Exposition chez le vendeur (galerie de GianLuca, Vieux Relais) | Non prévue par le BOFiP pour une galerie commerciale. Risque de qualification « biens divers » si la galerie gère les œuvres pour l'acheteur, et risque de cacher un élément déterminant à l'acheteur | **Avis écrit d'un avocat fiscaliste avant toute prospection** sur ce schéma | [HY] R2:107 ; C6:255 |
| Hôtels, restaurants, halls de concession comme lieux « accessibles au public » | Incertain : le BOFiP exclut un lieu réservé aux clients | Validation au cas par cas | [HY] R2:106 |
| Économie d'impôt de 25 % ou de 15 % (CRM, catalogue) | Dépend du bénéfice réel de l'acheteur, et de l'existence d'un bénéfice | Calculer sur le bénéfice réel et faire valider par l'expert-comptable de l'acheteur | [ES] C6:252 ; [IN] R2:111 |
| Prix de l'œuvre « au plus cinq fois le plafond annuel du client » | Prix calé sur la capacité fiscale de l'acheteur, pas sur la valeur de l'œuvre | Cote ou ventes comparables par artiste | [PR] à revoir (C6:54, 250) |
| « Suivi sur cinq ans » inclus dans le prix ; attestation annuelle pour l'expert-comptable | Gonfle la base déductible ; engage celui qui signe l'attestation | Facturer à part ; désigner le signataire et son assurance | C6:43, 256 |
| Entreprise individuelle au BIC ; déduction en cas de perte ; frais accessoires et commissions | [IN] | Expert-comptable | R2:108-111 |
| « Mécénat » pour l'achat d'une œuvre en galerie | **Faux** : c'est une confusion de dispositifs | Ne jamais employer le mot | [FV] R2:118 |
| Rendement, plus-value, rachat garanti | Fait basculer l'offre dans le régime des intermédiaires en biens divers (AMF) | Ne jamais le promettre (règle déjà posée) | [DR] contexte:91 ; C6:70 |
| Pièces « entièrement à la main par Medhi » pour les offres 1 à 3 | Éligibles si les autres conditions sont remplies, mais **sorties de l'offre Marwin le 4 nov.** ; le catalogue n'est pas mis à jour | Mettre le catalogue à jour, ou le marquer historique | [HY] C6:75-76 ; [DR] Note 4 nov. |
| Avantages fiscaux pour des entreprises qui achèteraient de l'impression 3D, de la robotique ou de l'IA (DEMANDE.md § 14) | **Aucun dispositif validé dans l'audit.** CIR, CII ou JEI seulement pour des travaux éligibles et documentés ; « la simple utilisation d'IA ne suffit pas ». Aides régionales : avances remboursables [DR] | Ne présenter aucun argument fiscal sur ces technologies sans avis écrit | [PR] V5 p. 22 (C3:81) ; vC3:31 |
| Calculs fiscaux envoyés par le CRM à chaque prospect | Peuvent relever de la consultation juridique (loi de 1971, art. 54) | Validation par un professionnel ; renvoi de chaque prospect à son expert-comptable | [HY] R3:362 |

**Corrections à reporter dans les pièces** [FV] (R2:25-31) :
- PASS:28 : remplacer « inclus » par « avant le 31 décembre 2028 » ;
- `interne/offres-de-carlone-catalogue-crm.md:99` : préciser ce que prévoit le BOFiP (§ 90) ;
- catalogue et offre-md:292 : la doctrine de 1995 est confirmée par celle de 2024 ;
- catalogue:138 : seuils vérifiés sur Légifrance ;
- fiche F37781 (TVA à 20 % pour un revendeur) : obsolète.

---

## 9. Données et IA

### 9.1 Rôles RGPD

| Phase | Responsable du traitement | Sous-traitants | Code et source |
|---|---|---|---|
| Constitution du fichier (22-30 oct.), avant tout contrat | **Morgan et/ou Mathys, responsables de fait**, à titre personnel ou par une structure existante | Anthropic ou OpenAI selon l'offre utilisée, GitHub, Google (Firebase) | [HY] R4:129-134 |
| Exploitation commerciale (vente d'œuvres) | **Entité vendeuse de GianLuca**, encore à nommer (PASS:31) | Marwin une fois immatriculée ; Quali Contact (sous-traitant de GianLuca, ou sous-traitant ultérieur de Marwin) ; fournisseurs d'IA, GitHub, Google, Notion | [HY] R4:133 ; [FV] vC5:24 |
| Aujourd'hui | Marwin n'existe pas : elle ne peut ni signer un contrat de sous-traitance ni en assumer les obligations | — | [FV] R4:135 |

### 9.2 Obligations à mettre en place [FV pour les règles, PR pour les mesures]

| Obligation | Contenu | Source |
|---|---|---|
| **Contrat de l'article 28** | Contrat écrit (électronique admis) : objet, durée, nature, finalité, données, personnes concernées. **Huit clauses a à h** : instructions documentées (y compris pour les transferts), confidentialité, sécurité, sous-traitants ultérieurs, aide pour les droits des personnes, aide pour les art. 32 à 36, suppression ou restitution, audits. Clauses types : décision (UE) 2021/915 | R4:121, 137-147 ; vR4:19 |
| **Registre** | Obligatoire pour la gestion des prospects, même sous 250 salariés (traitement non occasionnel). Un registre côté responsable, un registre côté sous-traitant | R4:122, 149 |
| Base légale | Intérêt légitime (art. 6, § 1, f ; considérant 47), **à documenter** : analyse d'intérêt légitime, minimisation (pourquoi garder 87 profils LinkedIn et des lignes personnelles ?) | R4:158-163 |
| Information (art. 14) | Au plus tard au premier contact, avec la source des données ; droit d'opposition présenté séparément (art. 21, § 4). Le mail d'approche prévoit déjà une information partielle (vC5:35) | R4:165 |
| Opposition | À tout moment, sans motif ; liste repoussoir conservée au moins 3 ans ; opposition Sirene (A123-96) : le drapeau Pappers vérifié pour 32 fiches seulement | R4:83-85, 166 ; PASS:26 |
| Conservation | **3 ans** à compter de la collecte ou du dernier contact **émanant du prospect**, et non de nos appels ; aucune purge outillée | vR4:20 ; R4:167 |
| Sécurité (art. 32) | Firebase non configuré ; écriture libre de tout associé ; code exécuté par `document.write` ; sauvegarde CSV manuelle, sans restauration testée | vC5:22 ; R4:151-155 |
| Analyse d'impact (AIPD) | Caractère obligatoire non établi ; analyse courte conseillée (enrichissement par agents, croisement de sources) | [IN] R4:168 |

### 9.3 Violation de données : dépôt GitHub public

| Élément | État | Code et source |
|---|---|---|
| Faits | Dépôt FinanceScope/CRM-Carlone public ; dernier envoi le 30 oct. ; toujours public le 4 nov. (vérifié par Morgan via l'API) | [DR] contexte:5, :11 |
| Données exposées | Dans la copie `crm/` : **800 à 940 numéros** selon la méthode de comptage, **206 e-mails**, 86 à 89 profils LinkedIn, 740 mentions de dirigeants (468 fiches), des lignes 06/07 et des messageries grand public, des fiches d'artistes (22 de type « Artiste ») | [FV] vC5:16, 25, 33-34 ; [ES] sur les numéros |
| Date de connaissance | **Au plus tard le 2 nov.** (audit-md:3, « Nov 2, 2026 » ; audit-md:15, « Urgent ») | [FV] vR4:21 |
| Qualification | « Divulgation non autorisée » ou « accès non autorisé », accidentels (art. 4, point 12) : **violation très probable**, même sans preuve de téléchargement | [HY fort] R4:200 |
| Obligations | **Documenter dans tous les cas** (art. 33, § 5) ; notifier la CNIL « dans les meilleurs délais et si possible 72 heures au plus tard », sauf absence de risque, et motiver un retard ; informer les personnes si le risque est élevé (art. 34) ; **en cas de doute, la CNIL demande de notifier** | [FV] R4:202-206 |
| Délai | **Le 5 nov.**, à l'heure correspondante, qui est inconnue, si la connaissance date du 2 nov. Le 4 nov. au soir, le délai n'est **pas encore dépassé**, sauf connaissance antérieure [IN]. Notifier en retard en expliquant pourquoi vaut mieux que ne pas notifier | [ES] vR4:21 ; [HY] R4:207 |
| Qui notifie | Le responsable du traitement, **non désigné** : si Morgan et Mathys sont responsables de fait, ce sont eux ; s'ils sont sous-traitants, ils préviennent sans délai l'entité de GianLuca, dont le délai court à partir de cette information | [HY] R4:221-224 |
| Évaluation du risque | Un risque paraît difficile à exclure (hameçonnage ciblé, sollicitations, atteinte à la réputation de GianLuca) ; un risque **élevé** est à examiner pour les artistes et les lignes personnelles | [HY] R4:226-229 |
| Remédiation (décision de Morgan et de Mathys) | Rendre le dépôt privé et le vérifier ; contrôler les copies (forks) ; révoquer d'abord tout secret ; réécrire l'historique seulement après coordination. GitHub prévient qu'on ne peut pas retirer les données des clones d'autres utilisateurs | [FV] doc. GitHub (R4:232-234) |
| Autres copies | Copie dans `crm/` du dépôt **privé** Carlone, artefacts, archives zip : pas une violation si elles restent privées, mais autant de surfaces en plus | [HY] R4:235 ; vC6:24 |
| Contradiction | « Personne d'autre ne lit les fiches ni le suivi » (rapport-crm:15) : faux tant que le dépôt est public | [FV] R4:214 |
| Réforme | Seuil du risque élevé et délai de 96 h : proposition de la Commission COM(2025) 837, soutenue par le Conseil le 21 oct. 2026. **Pas en vigueur** | [FV] vR4:22 |

**Décisions immédiates** [PR] (R4:257) :
1. Rendre le dépôt privé.
2. Ouvrir la fiche de violation : faits, données, nombre de personnes, mesures prises.
3. Décider de la notification **avec un avocat ou un DPD, avant le 5 nov.**
4. Informer GianLuca Carlone **par écrit**, puisque ses prospects et son rapport sont en cause.
5. Ne plus présenter le CRM comme confidentiel ; ne pas le « montrer en direct » au client (diaporama `livre.html`) avant ces étapes.

### 9.4 Prospection B2B

| Règle | Contenu | Code et source |
|---|---|---|
| Téléphone vers un **consommateur** | **Consentement préalable obligatoire depuis le 11 août 2026** (loi n° 2025-594, art. 13 ; décret n° 2026-662) ; fin de Bloctel ; plages horaires et quatre appels par 30 jours ; sanctions jusqu'à 75 000 € (personne physique) et 375 000 € (personne morale), **par manquement** : la mention « par appel » vient seulement de la fiche DGCCRF | [FV] vR4:15-17 |
| Téléphone vers un **professionnel** | Hors de l'obligation de consentement. Intérêt légitime **si l'objet est en rapport avec la profession** ; information et opposition simple et gratuite | [FV] vR4:16, 18 |
| E-mail vers un professionnel | Même régime, avec l'identité de l'expéditeur et un moyen simple de se désinscrire. Adresses génériques hors champ. Reconstitution d'adresses possible sous conditions (CNIL, 16 oct. 2026) ; la règle du CRM « ne jamais deviner une adresse » est plus stricte : la garder | [FV] vR4:18 ; PASS:52 |
| Zone grise | Entrepreneurs individuels, artistes, dirigeants joints sur une ligne personnelle pour un achat personnel : régime du consommateur [HY]. Dans le fichier : 24 standards en 06/07 et 25 messageries grand public dans `companies.json` ; 21 mobiles et 24 adresses grand public dans `culture.json` | [FV] vC5:33-34 ; [HY] R4:43 |
| Agents vocaux et automates d'appel | Règle propre au B2B non établie ; à cumuler avec l'art. 50, § 1, de l'AI Act. **Aucun agent vocal sortant sans validation** | [IN] R4:77-78 ; [PR] R4:114 |
| Entité qui démarche | C'est elle, pas Marwin, le « professionnel » et le responsable du traitement ; à nommer dans chaque message (PASS:31) | [HY] R4:112 |

### 9.5 AI Act (règlement (UE) 2024/1689) et Omnibus IA (règlement (UE) 2026/1744)

- **Calendrier** [FV] (R4:266-273 ; vR4:23-24) :
  - application générale **depuis le 2 août 2026**, y compris l'art. 50 (transparence) ;
  - art. 4 (maîtrise de l'IA) réécrit au 27 juill. 2026 : il faut « prendre des mesures pour favoriser » cette maîtrise, sans garantir de niveau, et **aucune amende** n'y est attachée ;
  - marquage de l'art. 50, § 2, au 2 déc. 2026 pour les systèmes déjà sur le marché ;
  - haut risque reporté au **2 déc. 2027** (annexe III) et au **2 août 2028** (annexe I) ;
  - référence exacte : « article 1er, points 39 et 40 » du règlement 2026/1744.
- **Marwin comme déployeur** (ChatGPT ou Claude utilisés pour le client), à condition d'avoir une politique d'usage et une formation tracée :
  - art. 4 ;
  - art. 50, § 4 : mention « généré par IA » pour un hypertrucage, par exemple un visuel réaliste d'un lieu ou d'une personne existants. Pour une œuvre manifestement artistique, une mention discrète suffit.
- **Marwin comme fournisseur**, si elle livre sous son nom un assistant, le copilote Jarvis ou un agent vocal [HY sur la qualification] :
  - art. 50, § 1 : dire à l'utilisateur qu'il parle à une IA ;
  - art. 50, § 2 : marquer les contenus de synthèse.
- **Sanctions** : jusqu'à 15 M€ ou 3 % du CA pour l'art. 50, le montant le plus faible pour une PME.
- **Autorités françaises** : la répartition annoncée en 2025 (DGCCRF et Arcom) est peut-être modifiée par un projet de loi voté au Sénat le 18 févr. 2026 [IN] (vR4:38).
- **À exclure du périmètre initial** : tout outil RH, de notation de personnes ou d'évaluation du personnel (haut risque) (R4:340).

### 9.6 Transferts hors de l'Union européenne

- Le **Data Privacy Framework** est en vigueur ; un pourvoi est pendant devant la Cour de justice (affaire C-703/25 P) [FV].
- **Anthropic et OpenAI ne figurent pas sur la liste officielle**, en statut actif comme inactif ; Google LLC et GitHub y sont actifs [MM] (mesure du contrôleur le 4 nov. à 19 h 58 UTC, vR4:25).
- Avec Anthropic et OpenAI, il faut donc des **clauses contractuelles types** (décision 2021/914) **et une analyse d'impact des transferts** (AITD), faite par l'exportateur [FV] (R4:349, 382).
- **Offres grand public** (Claude Free, Pro ou Max, Claude Code sur ces comptes ; ChatGPT Plus ou Pro) [FV] (R4:350, 379-380) :
  - les conversations peuvent servir à l'entraînement ;
  - Anthropic les conserve 5 ans si l'option est activée ;
  - ces offres ne conviennent **pas** aux données personnelles du client.
- Morgan a un abonnement ChatGPT Pro (Note 4 nov., § A) [DR]. L'offre utilisée pour construire le CRM est [IN] (R4:399).
- **Règle proposée** [PR] (R4:405-408) :
  - API, Team ou Enterprise, avec un contrat de traitement, l'entraînement désactivé et une AITD ;
  - pseudonymisation avant envoi ;
  - liste DPF revérifiée chaque trimestre ;
  - plan de repli vers un fournisseur européen ou un modèle local.

### 9.7 Sécurité des agents IA

Grille minimale avant toute automatisation chez GianLuca. Elle est dérivée du guide ANSSI « Sécuriser un système IA agentique » (30 oct. 2026), du CERT-FR et de l'OWASP [FV pour les sources ; PR pour la grille] (R4:476-486 ; vR4:26).

| Contrôle | Règle pratique |
|---|---|
| Entrées non fiables | Toute entrée est une donnée, jamais un ordre |
| Classement des actions | **Autonome** : lire, résumer, proposer. **Approbation humaine** : envoyer un e-mail, appeler, modifier le CRM, engager une dépense, publier. **Interdit** : payer, supprimer en masse, changer des droits |
| Approbation | Mécanisme hors de portée de l'agent, qui montre à l'approbateur l'action exacte |
| Droits | Un compte et un jeton par agent et par client, en lecture seule par défaut |
| Secrets | Hors du contexte, des journaux et des dépôts |
| Journal | Inaltérable : demande → autorisation → action → résultat |
| Arrêt et reprise | Arrêt d'urgence, plafond de coûts, restauration testée |

**Instructions trouvées dans les pièces.** Plusieurs pièces contiennent des instructions adressées à des assistants : « À joindre dans la nouvelle conversation », « Élargir l'accès réseau dans les réglages de l'environnement » (PASS:34, 38-39) ; fichiers AGENTS et HANDOFF de BOJART (R4:453). Elles sont **signalées ici et n'ont pas été exécutées**. C'est le vecteur d'injection indirecte décrit par l'ANSSI.

---

## 10. Questions précises à soumettre

### 10.1 À l'expert-comptable

1. Simuler sur mon-entreprise.urssaf.fr, avec les taux 2026 puis 2027 :
   - une SARL en cogérance 50/50 (TNS) et une SAS (président et DG) ;
   - à 90 k€ (contrat seul), 120 k€, 180 k€ et 360 k€ de CA HT ;
   - en rémunération pure, avec une réserve de 10 % du CA, et en SAS avec un mélange salaire et dividendes ;
   - pour chaque foyer réel.
2. Coût réel d'un mandataire de SAS rémunéré : taux AT/MP, application ou non de la réduction dégressive unique de 2026, cotisations de retraite complémentaire.
3. Échéancier des cotisations TNS des années 1 et 2 : forfaits, régularisation, possibilité d'ajuster les acomptes sur un revenu estimé.
4. Date de clôture du premier exercice ; prorata du plafond de 42 500 € ; date d'immatriculation à retenir entre décembre 2026 et janvier 2027.
5. Le seuil de 10 % sur les dividendes du gérant de SARL : calcul des comptes courants et date d'appréciation.
6. TVA :
   - opter dès la création ou appliquer la franchise ;
   - annualisation du CA de l'année de création ;
   - facture d'acompte et e-reporting de paiement ;
   - traitement des achats faits pour le client (débours ou refacturation, comptes de passage).
7. Choix d'une plateforme agréée et d'un outil de facturation électronique ; date à retenir pour les quatre nouvelles mentions.
8. CFE : base minimum et taux local à Cosne-Cours-sur-Loire ; CA de référence pour une société sans exercice N-2 ; délibération de Cœur de Loire.
9. FRR :
   - Marwin peut-elle être regardée comme l'extension d'une activité préexistante de Morgan (OLSEN, entreprise domiciliée chez LegalPlace) ou du travail fait sur le CRM ?
   - comment rattacher le CA d'un pilotage fait à distance ou chez le client ?
   - quand déposer le rescrit L80 B 2° ?
10. ACRE pour un dirigeant de société : formule de dégressivité ; le silence vaut-il accord ; effet d'une entrée au capital dans les deux ans.
11. Effets d'une éventuelle requalification sur la TVA facturée, les cotisations déjà payées et les aides obtenues.
12. Frontière entre le « suivi de trésorerie des établissements » (offre-md:52) et la tenue de comptabilité ; statut de la paie au regard du monopole.
13. Contenu des 30 000 à 36 000 € de frais annuels : RC pro, comptable, banque, logiciels, CFE, déplacements (C3:279).
14. **Pour l'entité de GianLuca**, avec son propre expert-comptable : récupère-t-elle la TVA ? Peut-elle recevoir des factures électroniques ? Est-elle éligible à l'aide régionale au conseil, à déposer **avant** la signature du devis ?

### 10.2 À l'avocat en droit des sociétés

1. SAS ou SARL au regard des réponses aux questions Q1 à Q4 (§ 1.10) ; statuts adaptés au 50/50 (mécanismes contre le blocage, clause d'exclusion, inaliénabilité).
2. Rédaction du pacte (§ 5.2) : validité et exécution de l'offre alternative, des clauses de départ (« good / bad leaver ») et de non-concurrence ; articulation avec l'art. 1843-4 C. civ.
3. Apport en industrie ou rémunération différenciée pour compenser un temps inégal.
4. État des actes de la société en formation, mandat de reprise, et rédaction d'un contrat signé avant l'immatriculation.
5. Entrée de GianLuca Carlone au capital : instruments (actions de préférence, BSA), conventions réglementées (L227-10 ou L223-19), effet sur les seuils de l'IS, de l'option IR, de l'ACRE et du plafond de minimis.
6. Instruction écrite sur le retrait de Medhi et de BOJ.ART : faut-il formaliser la décision avec Mathys et Medhi, et retirer ou marquer les documents restés en circulation ?

### 10.3 À l'avocat en droit du travail

1. Le contrat-cadre, la convention de bureaux et le mode de commande écartent-ils assez la subordination (L8221-6 II) ? Quels indices supprimer ?
2. Un salariat d'un fondateur chez une entité de GianLuca est-il compatible avec la prestation de Marwin ? À quelles conditions (fonctions, PI, conflit d'intérêts, ARCE) ?
3. Critères du prêt de main-d'œuvre appliqués à une prestation intellectuelle, et au pilotage de Quali Contact.
4. La convention de bureaux est-elle un bail ? Quelles obligations d'assurance en découlent ?

### 10.4 À l'avocat en contrats, propriété intellectuelle et numérique

1. Chaîne des droits sur le CRM (Morgan, Mathys, agents IA) puis vers Marwin et vers le client ; portée de L131-3 pour un contrat de développement ; protection du code généré par IA ; conditions d'utilisation des outils d'IA sur la propriété des sorties.
2. Régime de Jarvis : composants, licences tierces, nom.
3. Cession par livrable et licence sur les composants génériques ; régime écrit du CRM « offert ».
4. Plafond de responsabilité, exclusions, obligation de moyens ou de résultat ; contrat négocié ou d'adhésion.
5. Préavis de L442-1 II dans les deux sens, y compris le nouvel alinéa sur la réduction des volumes.
6. Mandats de dépense par entité ; responsabilité de Marwin envers les tiers.
7. Marwin est-elle un « fournisseur de services de traitement de données » (Data Act, art. 25) ?
8. Droits sur les films et images : artistes montrés, invités filmés, contenus générés par IA.

### 10.5 À l'avocat ou au DPD en données personnelles (en priorité le 4 ou le 5 novembre)

1. Qui est responsable du traitement du fichier exposé ? Faut-il notifier la CNIL, et à partir de quelle date de connaissance ? Faut-il informer les personnes (artistes, lignes personnelles) ?
2. Quelle entité de GianLuca démarche, signe le contrat de l'article 28 et figure dans les mentions d'information ?
3. L'argument « achat d'œuvre lié à la fonction du dirigeant » suffit-il pour l'intérêt légitime ? Quel traitement pour les entrepreneurs individuels, les artistes et les lignes personnelles ?
4. Un agent vocal sortant est-il un automate d'appel ? Un assistant bâti sur une API rend-il Marwin fournisseur (art. 50) ?
5. Quelles offres d'IA, avec quelles entités contractantes, pour des données du client ? Qui rédige l'AITD ?

### 10.6 À l'avocat fiscaliste et à l'avocat du marché de l'art (côté GianLuca)

1. Rescrit L80 B 1° sur une pièce précise faite à la machine (3D, bras robotisé) : déduction et taux de TVA.
2. Exposition d'une œuvre achetée par une entreprise dans la galerie du vendeur ou au Vieux Relais ; risque « biens divers ».
3. Statut de GianLuca dans chaque vente (acheteur-revendeur, commissionnaire, mandataire) et régime de TVA œuvre par œuvre.
4. Registre des objets mobiliers pour une galerie qui ne vend qu'en premier marché ; dispositif LCB-FT existant pour l'activité parisienne.
5. Rémunération de Marwin sur les ventes : comment éviter qu'elle devienne « intermédiaire » au sens de L561-2, 10°, et de R122-9 ?
6. « Enchères » pendant une soirée : opérateur habilité obligatoire ?
7. Contrat de dépôt-vente type avec les artistes ; exceptions à la rétractation (sur mesure) pour les professionnels.

### 10.7 À d'autres interlocuteurs

| Interlocuteur | Question |
|---|---|
| Urssaf | Délai d'obtention d'une attestation de vigilance pour une société nouvelle ; ACRE d'un dirigeant (silence vaut accord ?) |
| France Travail | Droits ARE de chacun ; maintien de l'ARE pour un président de SAS non rémunéré ; ARCE en cas de salariat |
| Assureur ou courtier | RC pro couvrant le pilotage, le développement, l'IA et les données (exclusions cyber et IA) ; assurance des locaux ; garanties pour les événements |
| Banque | Dépôt du capital et délai de déblocage ; compte professionnel |
| Mairie, SDIS, préfecture (avec l'entité de GianLuca) | Classement ERP des bâtiments ; demande GN 6 ; débit temporaire ; licence IV disponible |
| Intégrateur robotique (si un projet de bras revient) | Statut du bras (machine ou quasi-machine), analyse de risques avec du public, date de mise en service |

### 10.8 Questions à GianLuca Carlone qui conditionnent toutes les réponses juridiques

1. Quelle entité signe et paie (dénomination, SIREN), qui la représente, et qui valide les livrables ?
2. Quelle entité vend les œuvres, organise les événements, exploite chaque lieu ? Quel est son expert-comptable ou son avocat ?
3. Où sont les bureaux proposés ? À quel titre seraient-ils occupés ?
4. Envisage-t-il réellement de salarier l'un des fondateurs, et pour quelles fonctions ? D'investir, sous quelle forme et à quel horizon ?
5. Une activité parisienne existe-t-elle déjà, avec registre, dispositif LCB-FT et déclaration de diffuseur ?

---

## Annexe A. Vérifications faites par ce synthétiseur dans les pièces d'origine (4 nov. 2026)

| Point | Constat | Source |
|---|---|---|
| Diaporama client | 11 vues ; `strates` et `strates-phases` hors de l'ordre ; Medhi et BOJ.ART ne figurent que dans ces deux fichiers retirés | `deck.json:7` ; recherche dans `slides/*.html` [FV] |
| Offre écrite non corrigée | « Option création : des œuvres de Medhi (BOJ.ART)… » ; tableau « Qui apporte quoi » ; exclusivité de vente et films promis à la galerie | offre-md:22, 88-94 [FV] |
| Promesses du diaporama | « Convention de bureaux », « Investissement éventuel […] par un pacte écrit », « Réversibilité : fichiers, configurations, documentations et accès remis », matériel « acheté et possédé par votre entité » | `slides/cadre.html`, `garanties.html`, `laboratoire.html` [FV] |
| Date de connaissance de la fuite | « Nov 2, 2026 » ; « Données : Urgent — Le dépôt GitHub du CRM est public » | audit-md:3, :15 [FV] |
| Hébergement et propriété du CRM | « hébergé sur Firebase […] sous le compte des associés » ; « Propriété : le code, les données et le suivi restent chez les associés » ; « Personne d'autre ne lit les fiches » | rapport-crm:12, :15, :19 [FV] |
| Date du 238 bis AB dans le CRM | « achats jusqu'au 31/12/2028 inclus » | PASS:28 [FV] |
| Salariat | « Carlone veut vous salarier et acheter des prestations » (V5 p. 20) ; Morgan : « Je préfère être prestataire ou salarié. Oui, mes pouvoirs fait en sorte d'être payé en plus par des missions de prestation » (transcription telle quelle) | V5 p. 20 ; recueil:248 [FV] |
| Clause sur les gains d'automatisation | « Les gains d'automatisation servent à réaliser davantage dans la capacité réservée ou à ajuster le forfait » | V5 p. 4 [FV] |
| Cotisations en SARL à l'IR | « Les cotisations portent sur le bénéfice professionnel attribué, même non retiré » | V5 p. 20 [FV] |
| Responsabilité limitée | « La responsabilité limitée connaît des exceptions, notamment les cautions personnelles et les fautes de gestion » | CS p. 2 [FV] |
| Licence de Jarvis | « Aucune licence globale nouvelle n'est imposée à l'œuvre, aux médias ou aux données historiques par cette consolidation » ; aucun fichier LICENSE à la racine ; commits du compte « Momolscode » | `BOJART:jarvis/LICENSE_SCOPE.md:2` ; `git log` (commit 3436f53) [FV] |
| Lien entre GianLuca et Medhi | « a racheté six bâtiments et l'ancienne affaire de Medhi » | contexte:24 [DR] |
| Grille de mandat du 29 oct. | « une absence de réponse ne vaut pas approbation » | accomp:92-103 [FV] |
| Vernissage | Fragments imprimés par le parc de Medhi ; film de la soirée envoyé par le CRM aux invités ; « mise aux enchères » | vernissage:20-25, 81, 89 [FV] |

## Annexe B. Corrections des contrôleurs retenues ici (au lieu du texte d'origine)

- **vR1** : règle des 10 % sur les dividendes à l'art. L136-3 CSS ; l'art. 15 de la LF 2026 ne touche pas le taux réduit d'IS ; dépassement des plafonds de la micro-entreprise ; ARE plafonnée depuis le 1er avril 2025 ; coefficient SAS sans source officielle.
- **vR2** : barème de CFE = base minimum ; CFE non due l'année de la création ; annualisation pour la franchise de TVA ; plafond de minimis sur trois ans ; garantie du rescrit FRR ; domiciliation au domicile du dirigeant en zone admise.
- **vR3** : cotisations du donneur d'ordre seulement après condamnation pénale ; publication en ligne des condamnations ; peines du prêt de main-d'œuvre inchangées ; date et champ de L8222-1-1 ; arrêt du 14 janv. 2026 inédit ; nouvel alinéa de L442-1 sur la baisse des volumes ; TJ Paris 2023 d'autorité faible ; Data Act, art. 25, sans exemption pour le sur-mesure.
- **vR4** : délai de 72 h au 5 nov. et non « dépassé » ; plafonds DGCCRF par manquement ; référence de l'Omnibus IA ; origine des « 96 h » ; art. 13 de la loi n° 2025-594 vérifié ; autorités françaises de l'art. 50 [IN].
- **vR5** : directive 2024/2853 applicable après le **8** déc. 2026 ; registre à la charge des dirigeants ; déclaration de diffuseur avant le 1er mai ; « un mois » d'opposition pour les spectacles ; modification de L561-2 par la loi sur le sport ; ratio des débits de boissons.
- **vC3** : référence SARL provisoire ; écart de 2 795 € non probant ; objectif de 7 500 € [DR] ; condition des 75 % ; achat de la station non décidé avant l'étude ; aide à l'investissement remboursable ; salariat = souhait de Morgan ; omissions (gains d'automatisation, cotisations sur bénéfice non retiré, ARCE et CDI).
- **vC5 et vC6** : 800 à 940 numéros ; 22 artistes au sens strict ; copie `crm/` dans un dépôt privé ; information partielle déjà prévue dans le mail d'approche.

## Annexe C. Limites propres à cette synthèse

- Simulations de revenu refaites sur un barème simplifié (`scratchpad/syn-droit-calc/sim.py`) : aucune ne remplace le simulateur officiel ou l'expert-comptable [ES].
- Les coûts de création et de conseil (§ 1.7) sont des ordres de grandeur non vérifiés [HY].
- Les règles du code de commerce (L223-29, L227-10, L223-19), du droit des marques (« Jarvis ») et des conditions d'utilisation des outils d'IA n'ont été rouvertes ni par les chercheurs ni par ce synthétiseur [IN].
- L'état réel du dépôt FinanceScope ce soir, l'existence de copies (forks) et l'indexation par des moteurs de recherche restent [IN].
