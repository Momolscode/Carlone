# Stratégie S2 « pilotage » : un bureau de pilotage du portefeuille de GianLuca Carlone, borné, réceptionnable et rentable

Stratège « S2-pilotage » de l'audit Marwin Tech × GianLuca Carlone. Proposition rédigée le 4 novembre 2026 au soir, indépendamment des autres stratèges.

**Document interne.** Il contient des prix planchers, des coûts, des marges, des rémunérations et la stratégie des associés. Il ne doit pas être transmis tel quel à GianLuca Carlone. Peuvent servir de base à une proposition client révisée, après accord écrit de Morgan et de Mathys : les fiches d'offres de la section 4 sans les lignes « coûts » et « marge », le calendrier de paiement (section 5) et la gouvernance (section 8).

**Posture assumée.** Je construis la version la plus forte possible de l'ambition de Morgan : « GianLuca nous confie le pilotage d'un portefeuille de projets » (DEMANDE.md § 2). Je la borne pour qu'elle soit tenable à deux, je la découpe pour qu'elle soit réceptionnable, et je la chiffre pour qu'elle soit rentable. Quand l'ambition et la preuve divergent, la preuve l'emporte. L'ambition se traduit alors en conditions de montée en puissance.

---

## Méthode, sources et conventions

**Bases utilisées.**
- Les quatre synthèses : `syn-sources.md`, `syn-portefeuille.md`, `syn-capacite-ia.md` et `syn-droit.md`.
- Les inventaires `ex-C2` (offre) et le mémo `rj-R6` (marché), avec leurs contrôles.
- Les pièces d'origine rouvertes le 4 nov. 2026, en lecture seule, dans le dépôt `Momolscode/Carlone` (commit 7b46602) :
  - `interne/offre-marwin-tech-remuneration-et-collaboration.md`, lignes 13-21, 29, 56-63, 132, 148-149, 153, 193-195, 206, 211, 227, 229, 246-248 et 258 ;
  - `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md`, lignes 7, 52, 54-64, 103 et 105 ;
  - `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:65` ;
  - `sources/chatgpt-pages/2026-11-04-complement/marwin-structure-et-offres.md:26-34` ;
  - `interne/recueil-sessions-chatgpt-2026-11-04.txt:220, 248, 1469` ;
  - `interne/audit-marwin-tech-carlone.md:13, 15, 55, 62` ;
  - `interne/contexte-projet-carlone.md:95` ;
  - `pour-carlone/vernissage-strates-idees.md:110-111`.
- Les diapositives du diaporama client : `deck.json:7` et `slides/paiement.html`, `formules.html`, `proposition.html`, `garanties.html`.

Quand un contrôleur corrige un lecteur, c'est la correction qui fait foi. Elle est reprise telle que les synthèses l'ont arbitrée.

**Calculs.** Ils ont été faits en Python (`python3 -I`) avec deux scripts du bloc-notes, rejouables :
- `[dossier de travail] s2-calc/s2.py` : coût complet par journée, scénarios, seuils ;
- `[dossier de travail] s2-calc/annee1.py` : trajectoire de la première année.

Tous les montants qui en sortent sont des estimations [ES]. Ils sont exprimés hors taxes, et les nets s'entendent avant impôt sur le revenu.

**Aucune action extérieure.** Je n'ai contacté personne, rien acheté, rien publié et rien modifié en dehors de ce fichier et des deux scripts de calcul.

**Nom du client.** Le client s'appelle **GianLuca Carlone**. Les pièces qui portent l'erreur d'archives ne sont pas citées ici.

**Codes.** [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu.

**Abréviations.** Les chemins sans préfixe partent de `Momolscode/Carlone`. Les fichiers `syn-*`, `ex-*`, `rj-*` et `ver-*` sont dans `audit-work/`.

| Abréviation | Pièce |
| --- | --- |
| OFF | `interne/offre-marwin-tech-remuneration-et-collaboration.md` (2 nov.) |
| ACC | `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md` (29 oct.) |
| COP | `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md` (28 oct.) |
| STR | `sources/chatgpt-pages/2026-11-04-complement/marwin-structure-et-offres.md` (29 oct.) |
| R | `interne/recueil-sessions-chatgpt-2026-11-04.txt` |
| AUD | `interne/audit-marwin-tech-carlone.md` (2 nov.) |
| CTX | `interne/contexte-projet-carlone.md` (4 nov.) |
| IDEES | `pour-carlone/vernissage-strates-idees.md` |
| V5 | `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` |
| DECK | `[diaporama Offre Marwin Tech, copie du 4 nov.] ` (diaporama client, 11 vues) |
| NOTE | `audit-work/note-point-4-novembre-et-activites.md` |
| JP | Journée-personne de 7 h ; deux personnes un jour = 2 JP |

**Trois faits nouveaux intégrés.**
1. **Retrait de Medhi et de BOJ.ART.** Le 4 nov., Morgan a demandé de retirer Medhi et BOJ.ART de l'offre [DR] (NOTE:25).
   - Le diaporama client est passé à 11 vues [FV] (DECK `deck.json:7`).
   - L'offre écrite (OFF:22, 67-101), STRATES v1.1, le vernissage et le PDF de 13 diapositives de la PR n° 1 ne sont pas corrigés [FV] (`syn-sources.md`, PER-2).
   - La décision n'est pas formalisée avec Mathys ni avec Medhi [DR].
2. **Violation de données probable.** Le dépôt public FinanceScope/CRM-Carlone est très probablement une violation de données personnelles [HY fort]. Si la connaissance date du 2 nov. (AUD:15), le délai de 72 h pour notifier la CNIL expire le **5 nov.** [ES] (`syn-droit.md` § 9.3 ; corr. ver-R4 n° 7).
3. **Aucune base contractuelle.** Il n'existe aucun contrat, aucune facture et aucune entité payeuse identifiée [FV négatif] (OFF:29 ; CTX:106).

---

## 1. Verdict

1. L'ambition de Morgan est atteignable sous une seule forme : un **bureau de pilotage du portefeuille**, vendu en offres séparées. Il se compose :
   - d'un cadrage payé, qui sert aussi de test du besoin ;
   - d'un pilotage mensuel avec capacité réservée nominative et limite du nombre de projets suivis ;
   - de lots de production devisés ;
   - plus tard, de l'exploitation de processus outillés, payée au résultat.

   Ce n'est pas l'abonnement « tout compris » de 20 à 40 JP à 750 € HT : celui-ci dépasse la capacité réelle du binôme et ne couvre pas le coût complet au volume tenable.
2. **Rien ne peut être signé ni facturé aujourd'hui.** Il manque une entité payeuse, la société Marwin et une parole directe de GianLuca. La violation de données est à traiter avant le 5 novembre, et la décision du 4 novembre n'est appliquée qu'à un seul support. Les trente premiers jours servent donc à lever ces blocages et à vendre un seul produit, le cadrage.
3. **Cible centrale à douze mois.** Elle tient en cinq éléments :
   - environ 12 000 € HT par mois facturés à des entités identifiées, payés d'avance pour le temps réservé et à la réception pour les livrables ;
   - quatre projets actifs suivis, avec un registre des décisions à jour ;
   - un ou deux processus outillés en exploitation, avec un gain mesuré ;
   - une part de GianLuca ramenée sous 85 % du chiffre d'affaires ;
   - et l'engagement de réduire, reporter ou refuser si le cadrage n'est pas commandé et payé avant fin janvier 2027.

---

## 2. Diagnostic en dix points

| N° | Constat | Code | Source | Conséquence pour S2 |
| --- | --- | --- | --- | --- |
| 1 | **Le besoin d'un pilotage global n'est pas démontré.** Aucune pièce ne rapporte une parole directe de GianLuca. Les « vingt jours par mois » sont attribués tantôt à lui (COP:65), tantôt à Morgan (ACC:7). | [DR] contradictoire ; [FV négatif] | COP:65 ; ACC:7 ; `syn-portefeuille.md` § 1.3 | Le premier produit vendu doit **tester** le besoin : un cadrage payé. |
| 2 | **L'acheteur est introuvable** : aucune entité nommée, aucun signataire, aucun payeur, aucun valideur. Le CRM a été livré sans facture. | [FV négatif] | OFF:29 ; CTX:106 ; `syn-sources.md` U01 | Un contrat par entité, avec signataire et valideur nommés. Aucune offre adressée « à Carlone » en général. |
| 3 | **L'offre est surdimensionnée.** La base de 20 JP demande 78 à 83 % du temps disponible des deux associés. Le renforcement de 40 JP en demande 140 à 145 %. L'ancre de 46 JP dépasse même le plafond théorique de 35 JP bruts. La capacité facturable réaliste est d'environ 7, 12 ou 20 JP selon le scénario. | [ES] | OFF:13-16, 246 ; `syn-capacite-ia.md` § 2.3 et 2.6 | Des paliers bornés, et une capacité réservée nominative. |
| 4 | **Le taux de 750 € HT n'est pas justifié, et il est trop bas au volume tenable.** Il est passé d'« hypothèse interne » (ACC:64) à « pas le taux » (OFF:18) sans justification nouvelle. À 12 JP facturables, il laisse environ 1 470 à 1 650 € nets par associé en SAS, réserve de 10 % comprise. | [FV] pour le durcissement ; [ES] pour le calcul | ACC:64 ; OFF:18 ; `ex-C2-offre.md` § 9.1 ; `s2.py` | Prix au périmètre ; 750 € devient un **plancher interne** (§ 4.7). |
| 5 | **L'abonnement absorbe tout.** Le premier mois est déjà réparti en 6 + 7 + 4 + 3 = 20 JP (OFF:56-61). Les huit propositions « demandent plus de 20 journées » (OFF:63). L'événement entre « sans supplément s'il tient dans les 20 journées » (IDEES:110). | [FV] | OFF:56-63 ; IDEES:110-111 | Séparer pilotage, production, exploitation et recherche ; règle anti-double facturation (§ 4.6). |
| 6 | **Le calendrier de paiement est contradictoire, et le démarrage impossible en l'état.** Le 29 oct., les mois 2 à 6 se paient « sous sept jours après facture de fin de mois » (ACC:57). Le 2 nov., ils se paient « d'avance, en début de mois » (OFF:19, 195). La diapositive titre « payé d'avance » (DECK `slides/paiement.html:4`), mais le solde du mois 1 est à terme échu (OFF:19). « Le travail démarre à réception » de l'acompte (`paiement.html:10`), alors que « Marwin Tech n'existe pas encore » (OFF:153). | [FV] | ACC:57 ; OFF:19, 153, 195 ; DECK `paiement.html:4, 10` | Tranché en section 5. |
| 7 | **La violation de données est probable.** Le dépôt public contient environ 800 à 931 numéros et 206 e-mails selon le comptage. Ni responsable de traitement, ni registre, ni contrat de l'article 28 n'existent. | [HY fort] ; [ES] pour les volumes ; [FV] pour l'absence de documents | AUD:15 ; `syn-droit.md` § 9.3 | Condition préalable à tout le reste. Remise en conformité **non facturée**. |
| 8 | **La décision du 4 nov. n'est appliquée qu'à un support.** La section « Option création » de l'offre écrite (OFF:22), STRATES v1.1, le vernissage (« avec Medhi, BOJ.ART », p. 12) et le PDF de 13 p. de la PR n° 1 restent en l'état. L'option laboratoire a perdu son objet robotique (OFF:84). | [FV] ; décision [DR] | DECK `deck.json:7` ; `syn-sources.md` PER-2 | Mise en cohérence avant tout rendez-vous ; règle « décision → documents touchés » (§ 8). |
| 9 | **La capacité démontrée se limite à produire vite avec l'IA.** La vente, la maintenance dans la durée et la coordination de prestataires ne sont démontrées par aucune réalisation. Chez OLSEN, 36 propositions et 72 brouillons ont été préparés, et aucun n'a été envoyé. Aucun gain d'IA n'a été mesuré. | [FV] ; [DR] pour OLSEN ; [IN] pour les gains | NOTE:9 ; `syn-capacite-ia.md` § 0.1 et 7.2 | Ne fixer aucun prix sur un « multiplicateur ». Mesurer d'abord (pilotes), capter la valeur ensuite (offre D). |
| 10 | **Concentration et points uniques de défaillance.** GianLuca serait à la fois client, bailleur, employeur et investisseur. Morgan mène une dizaine d'autres projets. La disponibilité de Mathys n'est pas fixée. La part maximale des revenus venant de Carlone est restée sans réponse (« 10 millions »). | [DR] ; [FV] pour la liste des projets ; [IN] pour Mathys | OFF:132, 148 ; NOTE:12-17 ; AUD:62 ; CTX:129 | Accords séparés, pacte d'associés, capacité nominative, second client, plafond de dépendance. |

---

## 3. Objectifs possibles et objectif principal recommandé

### 3.1 Cinq objectifs comparés

| Objectif | Contenu | Revenu possible [ES] | Risques principaux | Verdict S2 |
| --- | --- | --- | --- | --- |
| **O1. Cadrage seul** | Une mission ponctuelle de 6 à 10 JP : inventaire, priorités, feuille de route | 6 000 à 9 000 € HT, une fois | Pas de récurrence. Marwin reste un fournisseur d'études | **Repli** si le besoin récurrent n'est pas confirmé |
| **O2. Bureau de pilotage du portefeuille** | Cadrage, puis pilotage à capacité réservée, lots devisés et exploitation de processus | 5 400 à 22 000 € HT par mois selon le scénario (section 6) | Dépendance au client ; saturation ; adoption | **Objectif principal recommandé** |
| **O3. Verticale « vente d'œuvres »** | CRM, coordination de Quali Contact, supports, catalogue privé | 2 000 à 6 000 € HT par mois | Résultats (ventes) dépendant de GianLuca et de l'appelant ; argument fiscal non validé ; statut d'intermédiaire si la rémunération est liée aux ventes | **Repli** si GianLuca ne veut confier que ce projet |
| **O4. Intégration salariée chez GianLuca** | Morgan et/ou Mathys salariés, Marwin réduite à des lots | Salaire [IN] | Requalification ; perte d'indépendance ; propriété des logiciels créés à l'employeur (L113-9 CPI) ; c'est un souhait de Morgan [DR] (R:248), pas une demande établie du client | **Différé**, au plus tôt au bilan du 6e mois (§ 7) |
| **O5. Laboratoire et créations financés par GianLuca** | STRATES, Éclosion, IA locale, robotique | 0 tant qu'il n'y a pas de financeur écrit | Aucun financement acté ; aucune compétence robotique démontrée ; Medhi retiré | **Refusé** dans l'offre ; gelé (§ 4.5) |

### 3.2 Objectif principal (O2), formulé pour être mesurable

**Dans douze mois (au 4 nov. 2027), Marwin Tech est le bureau de pilotage contractuel du portefeuille que GianLuca Carlone lui a confié.**
- Chaque projet actif confié a une fiche, un budget, un responsable et un registre des décisions à jour.
- Les décisions sont préparées par écrit avant les réunions et tracées après.
- Un à trois processus outillés sont en exploitation, avec un gain mesuré par rapport à une référence.
- Marwin facture des entités identifiées, qui paient à l'échéance.
- Marwin finance ses deux associés sans travail gratuit.
- Marwin ne dépend plus de GianLuca pour la totalité de son chiffre d'affaires.

**Ce que devient « le travail de 100 personnes ».** C'est une ambition de **couverture**, mesurée en projets suivis par journée de pilotage et en résultats acceptés par JP, pas en nombre d'agents. Les cibles sont des hypothèses [HY], à fixer après la mesure de référence du cadrage :
- au départ, environ 1,25 à 1,5 JP de suivi par projet actif (`syn-capacite-ia.md` § 3.1) ;
- vers 1,0 JP à 6 mois et 0,8 JP à 12 mois, si les pilotes P1 et P3 tiennent leurs critères.

À capacité égale (13 JP de pilotage), le bureau suivrait alors 8 projets au lieu de 6. Un facteur de 1,5 à 2 sur les processus pilotés est exigeant ; un facteur de 50 n'est appuyé par aucune pièce (`syn-capacite-ia.md` § 7).

### 3.3 Ce qui est sous le contrôle de Marwin et ce qui dépend de GianLuca

| Sous le contrôle de Marwin | Dépend de GianLuca (ou de tiers) |
| --- | --- |
| Traiter la violation de données et mettre les documents en cohérence | Désigner l'entité ou les entités qui signent, paient et valident |
| Immatriculer la société, signer le pacte, souscrire la RC professionnelle, ouvrir les comptes à son nom | Commander et payer le cadrage, puis le pilotage |
| Fixer et tenir une capacité nominative ; respecter la limite d'encours | Fournir les accès, les documents et les interlocuteurs dans les délais |
| Qualité, délais et critères de réception des livrables | Décider dans les délais convenus ; arbitrer les priorités |
| Comptes rendus sous 24 h, registre à jour, rapport mensuel | Adoption par ses équipes et prestataires (Quali Contact, comptable, responsables de lieux) |
| Mesure des gains de l'IA, sécurité, sauvegardes, réversibilité | Ventes d'œuvres, ouverture de la galerie, réouverture des lieux, cabaret |
| Prospection d'un second client ; maîtrise des coûts | Bureaux, emploi, investissement éventuels |
| Refuser ce qui sort du mandat ou de la capacité | Validation par ses conseils (expert-comptable, avocat) des sujets fiscaux et juridiques |

---

## 4. Architecture des offres

**Principe [PR].** On vend un **périmètre** et des **niveaux de service**. On réserve une **capacité nominative**, qui sert de plancher de disponibilité et non de compteur. On réceptionne des **livrables**. Cela reprend l'architecture « trois offres simples » du 29 oct. (STR:26-34) et le « contrat-cadre et fiches de mission » du 30 oct. (V5 p. 2), perdus le 2 nov. (corr. ver-C2, omission 4). J'y ajoute une offre d'exploitation payée au résultat.

**Repère interne commun [ES].** Dans le scénario central (12 JP facturables, 2 500 € de frais par mois, SAS avec un coût total de 1,8 fois le net), le coût complet d'une JP facturable est :
- d'environ **810 €** hors réserve, et 900 € avec une réserve de 10 %, pour 2 000 € nets par associé ;
- d'environ **960 €** hors réserve, et 1 065 € avec la réserve, pour 2 500 € nets.

En SARL, avec des cotisations TNS de 40 à 46 % du net, ces coûts baissent d'environ 15 % (`s2.py`). Toutes les offres ci-dessous visent **880 à 950 € HT par JP estimée**.

### 4.0 Chantier P0, interne et non facturé : la remise en ordre

| Rubrique | Contenu |
| --- | --- |
| Objet | Traiter la violation de données : dépôt privé, fiche de violation, décision de notification avec un avocat ou un délégué à la protection des données, information écrite de GianLuca. Marquer « historiques » l'offre écrite, STRATES v1.1, le vernissage et le PDF de 13 p. Préparer statuts, pacte, contrat-cadre et modèles de bon de commande. |
| Capacité | 9 à 17 JP sur les mois 0 à 2 [ES] (`syn-capacite-ia.md` § 2.5) |
| Coût | Avocat ou DPD pour la violation : 1 000 à 3 000 € [HY]. Statuts et pacte : 2 000 à 5 000 € HT [ES] (`syn-droit.md` § 1.7) |
| Facturation | **Aucune.** L'exposition des données est de notre fait (`syn-portefeuille.md` § 3.1). |

### 4.1 Offre A : cadrage du portefeuille (forfait)

| Rubrique | Contenu |
| --- | --- |
| **Client** | L'entité de GianLuca désignée comme chef de file : dénomination, SIREN, signataire habilité. S'il y a plusieurs entités, une seule commande le cadrage pour toutes [PR]. |
| **Problème** | GianLuca a plusieurs projets déclarés : vente d'œuvres aux entreprises, galerie en 2027, lieux rachetés, cabaret éventuel, réunion d'artistes, Quali Contact [DR] (COP:7, 13-16). Ni leurs priorités, ni leurs porteurs juridiques, ni leurs budgets ne sont établis [IN]. |
| **Résultat** | GianLuca sait ce qu'il pilote, qui porte quoi et ce qu'il veut faire dans les 90 jours. Il peut décider en connaissance de cause s'il confie un pilotage récurrent, et dans quel palier. |
| **Périmètre (livrables)** | 1. Carte des entités et des lieux : propriétaire, exploitant, signataire et valideur par projet, **validée par écrit**. 2. Fiche de chacun des projets déclarés : bénéficiaire, état, preuves, budget connu, prochaine décision. 3. **Trois priorités à 90 jours** choisies par GianLuca, chacune avec un budget et un critère de réussite. 4. Projet de mandat par entité, avec plafonds (§ 8). 5. Registre des décisions et tableau de bord v0, ouverts **sur un compte au nom de l'entité**. 6. Mesure de référence pour les pilotes P1 (comptes rendus et registre) et P3 (recherche documentaire), avec leurs protocoles (`syn-capacite-ia.md` § 6.1 et 6.3). 7. Proposition de palier de pilotage (offre B) et liste chiffrée des lots (offre C). |
| **Exclusions** | Toute production : CRM, supports, catalogue, dossiers de lieux. Le conseil fiscal ou juridique. Toute démarche au nom du client. Toute donnée personnelle de prospects. |
| **Dépendances** | Deux entretiens avec GianLuca (60 à 90 min chacun) ; accès aux documents dans les 10 jours ouvrés ; interlocuteurs nommés (comptable, avocat, responsables de lieux) ; société Marwin immatriculée. |
| **Capacité** | **8 JP** : Morgan 5 (entretiens, priorités, mandat), Mathys 3 (registre, tableau de bord, mesures de référence) [PR]. Si les deux associés assistent à une réunion, elle compte double. |
| **Durée** | 4 à 5 semaines à compter de l'acompte encaissé. Les congés de fin d'année ne comptent pas. |
| **Prix proposé** | **7 500 € HT** (9 000 € TTC), soit environ 940 € par JP [PR]. **Repli** à 6 000 € HT (8 × 750 €) seulement si GianLuca a déjà vu le taux de 750 € (question U04). **Plancher** : 6 000 € HT. |
| **Justification du prix** | *Coût complet* : 8 JP × 810 à 1 065 € = 6 500 à 8 500 € [ES]. *Marché* : le Diag Data IA de Bpifrance, seul prix public solide, vaut 10 000 € HT pour 8 jours d'expert, soit 1 250 € par jour [FV officiel] (`rj-R6-marche.md` (e)) ; Marwin n'est pas habilitée à ce dispositif [IN], et il ne faut pas laisser croire que l'offre est subventionnée. *Valeur* : décider avant d'engager un pilotage récurrent de 65 000 à 140 000 € par an [ES], ou décider de ne pas l'engager. |
| **Coûts directs** | Déplacements : 2 à 3 journées sur place, coût [IN] (lieu de résidence des associés inconnu). Outils : moins de 100 €. |
| **Marge** | Contribution d'environ 6 900 à 7 300 € [ES]. Marge sur coût complet de 0 à 15 % selon la rémunération visée. Le cadrage n'est pas fait pour enrichir Marwin : il sert à tester le besoin et à amorcer la relation. |
| **Réception** | Critères écrits : livrables 1, 3 et 4 signés par GianLuca ou son délégué ; livrables 2, 5, 6 et 7 remis. Réserves motivées par écrit sous 10 jours ouvrés, avec un cycle de correction compris. La réception est **expresse** (§ 5 : le paiement du solde a sa propre règle). |
| **Conditions de poursuite** | Si GianLuca commande B ou au moins un lot C dans les 30 jours après la réception, on poursuit. Sinon, la relation se clôt proprement : remise des livrables, comptes au nom du client. Marwin ne produit rien d'autre sans commande. |

**Aide régionale.** Une aide au conseil stratégique (50 % jusqu'à 15 000 € sur deux ans) existerait, à condition de **déposer le dossier avant de signer le devis** [DR] (OFF:229 ; R:755, 809). Si l'entité de GianLuca y est éligible [IN], l'ordre est le suivant : dépôt du dossier, puis signature, puis acompte. Rien n'est budgété sur cette aide.

### 4.2 Offre B : pilotage du portefeuille (abonnement à capacité réservée et limite d'encours)

**Ce que contient le socle** (identique dans tous les paliers) [PR] :
- une réunion hebdomadaire de 1 h 30 à 2 h, avec **un seul associé** sauf décision qui demande les deux ;
- un compte rendu envoyé sous 24 h ouvrées ;
- un registre des décisions et des échéances, et un tableau de bord mis à jour chaque semaine ;
- un comité mensuel avec les deux associés et un rapport : capacité consommée, livrables, décisions attendues, risques, indicateurs ;
- des dossiers de décision préparés avant chaque comité ;
- la coordination, sous mandat, des prestataires et des professionnels de GianLuca : comptable, avocat, Quali Contact, artisans ;
- un suivi budgétaire préparatoire par projet (budget, engagé, payé), remis à l'expert-comptable ;
- une veille des échéances réglementaires listées dans le cadrage.

Charge estimée du socle : environ 3,5 JP par mois. Il faut y ajouter environ 1,25 JP par projet actif suivi et 0,25 JP par projet en veille [ES] (`syn-capacite-ia.md` § 2.4 et 3.1).

| Palier | Projets actifs suivis | Projets en veille | Capacité réservée nominative | Prix HT par mois | Équivalent par JP | Condition d'accès |
| --- | --- | --- | --- | --- | --- | --- |
| **B1 « Socle »** | 2 | 1 | 6 JP (Morgan 4, Mathys 2) | **5 400 €** (6 480 € TTC) | 900 € | Cadrage reçu ; mandat signé ; accès fournis |
| **B2 « Portefeuille »** | 4 | 2 | 9 JP (Morgan 5, Mathys 4) | **8 000 €** (9 600 € TTC) | ≈ 890 € | Trois mois de B1 aux critères tenus, **ou** disponibilité nominative écrite du scénario central |
| **B3 « Portefeuille étendu »** | 6 (8 si les gains P1 et P3 sont mesurés) | 3 | 13 JP (Morgan 7, Mathys 6) | **11 800 €** (14 160 € TTC) | ≈ 910 € | Engagement écrit de chaque associé à au moins 80 % de son temps ; sous-traitant identifié pour les lots ; pas avant le mois 5 |

| Rubrique | Contenu |
| --- | --- |
| **Client** | L'entité chef de file, avec une fiche de mission **par entité** si les projets relèvent de plusieurs entités. La capacité est répartie entre entités, pour qu'aucune ne consomme le temps payé par une autre (`syn-portefeuille.md` § 2.3, S2). |
| **Problème** | GianLuca veut « ne pas gérer chaque détail » [DR] (ACC:13), mais les décisions, les échéances et les prestataires de plusieurs projets doivent avancer en même temps. |
| **Résultat** | Une vision à jour du portefeuille, des décisions préparées et tracées, des prestataires coordonnés et des retards détectés avant l'échéance. |
| **Périmètre** | Le socle ci-dessus, appliqué aux projets actifs nommés dans la fiche de mission. **Limite d'encours** : un projet de plus en remplace un, ou fait changer de palier par avenant. |
| **Exclusions** | Production de livrables (offre C). Exploitation d'un processus (offre D). Exécution administrative courante : comptabilité, paie, recouvrement, réservations de séjours, gestion locative (`syn-droit.md` § 4.7). Conseil fiscal ou juridique. Présence lors d'événements. Urgences hors plages (option séparée). Recherche et développement. |
| **Dépendances** | Mandat écrit par entité ; validateur nommé ; délai de réponse aux décisions de 5 jours ouvrés au plus ; outils ouverts au nom de l'entité ; comptes rendus validés. |
| **Capacité** | Selon le palier. Elle est **nominative** et rapportée chaque mois. Une capacité non consommée peut être reportée au mois suivant, dans la limite de 20 %, **pour du pilotage seulement**. Elle n'est jamais convertie en production. |
| **Durée** | **Trois mois fermes**, puis reconduction mensuelle. Préavis réciproque d'un mois pendant les douze premiers mois, de deux mois ensuite (`syn-droit.md` § 4.4). Changement de palier avec un mois de préavis, et sans pénalité si un associé est indisponible plus de 10 jours ouvrés. |
| **Justification du prix** | *Coût complet* : environ 900 € par JP, ce qui finance environ 2 000 € nets par associé et 10 % de réserve à 12 JP facturables [ES]. *Marché* : le temps partagé se vend en général 2 à 8 jours par mois, à 800 à 1 200 € HT par jour (DAF à temps partagé), soit 4 000 à 8 000 € par mois. Le management de transition est à environ 1 330 € par jour [DR, sources secondaires] (`rj-R6-marche.md` (a) et (e)). *Valeur* [HY] : pas de recrutement ni de risque social, deux profils, des outils et une méthode déjà en place, un palier modulable et la réversibilité. |
| **Comparaison honnête** | Un chef de projet cadre salarié en région coûte 5 380 à 6 150 € par mois à temps plein (`rj-R6-marche.md` (b), calcul Urssaf). **Si le besoin stable dépasse 15 JP par mois pendant plus de 12 mois, un recrutement est moins cher pour GianLuca.** S2 l'assume : le lot C7 l'aide à recruter un coordinateur local. Marwin pilote et outille ; le salarié exécute. |
| **Coûts directs** | Outils de Marwin : 150 à 300 € par mois. Les outils du client sont payés par lui. API plafonnée à 50 à 80 € par mois. Déplacements : [IN]. |
| **Marge** | Sur coûts directs : plus de 90 %. Sur coût complet : environ 10 %, pour 2 000 € nets par associé ; proche de zéro, voire négative, pour 2 500 € [ES]. **La marge réelle viendra des gains de productivité gardés par Marwin dans le forfait** (§ 4.8), pas d'un taux plus élevé. |
| **Réception mensuelle** | Rapport mensuel remis au 5e jour ouvré. Engagements de service : comptes rendus sous 24 h ouvrées dans au moins 90 % des cas ; 100 % des décisions avec responsable, date et source ; tableau de bord mis à jour chaque semaine. **Malus** de 5 % sur la facture suivante si deux engagements sont manqués dans le mois. Aucun bonus lié aux ventes. |
| **Conditions de poursuite** | Bilan au 3e mois : passage de B1 à B2, maintien, ou réduction. Bilan au 6e mois, avec un **exercice de sortie à blanc** : restitution complète testée (`syn-capacite-ia.md` § 8.5). |

### 4.3 Offre C : lots de production devisés

**Règle de prix [PR].** JP estimées × 900 à 950 €, plus 10 à 15 % d'aléas, **jamais moins de 750 € par JP**. Chaque lot a son bon de commande, ses critères de réception et sa cession de droits au paiement complet.

**Règle de capacité.** Les lots s'exécutent dans la capacité facturable restante, soit environ 2 à 3 JP par mois dans le scénario central. Au-delà, on reporte ou on sous-traite un lot délimité.

| Lot | Capacité [ES] | Prix [PR] | Conditions préalables | Réception |
| --- | --- | --- | --- | --- |
| **C1. Pilote commercial CRM, 20 comptes** | 6 à 7 JP (2 semaines de préparation, 4 semaines d'appels) | 6 000 € HT | Conformité faite et non facturée ; structure vendeuse nommée ; argument fiscal validé par écrit par le conseil de GianLuca ; décision sur qui appelle | Protocole P2 (`syn-capacite-ia.md` § 6.2) : au moins 90 % des champs de contact sourcés et datés ; 100 % des oppositions respectées ; joignabilité, rendez-vous et refus **mesurés** [MM] |
| **C2. Catalogue privé des œuvres** | 4 à 8 JP selon le nombre d'œuvres réelles | 3 500 à 7 500 € HT ; photographe hors lot | Inventaire des œuvres, provenance, autorisations de reproduction | Fiches complètes et exportables ; aucune œuvre sans autorisation |
| **C3. Dossier de faisabilité d'un lieu ou d'un événement**, sans robot et sans exploitation | 4 à 6 JP | 4 000 à 5 500 € HT | Lieu, propriétaire et exploitant identifiés | Lieu, date, jauge, budget, organisateur désigné, autorisations avec leurs dates de dépôt (GN 6 deux mois avant), devis (`syn-portefeuille.md` § 3.7) |
| **C4. Kit de campagne et supports commerciaux** | 3 à 5 JP | 3 000 à 4 500 € HT | Offres validées par GianLuca ; mentions fiscales validées par son conseil | Grille de conformité respectée ; validation au premier ou au second passage |
| **C5. Spécification et essai d'échange avec Quali Contact** | 2 à 4 JP | 2 000 à 3 500 € HT | Contrat entre GianLuca et Quali Contact ; modèle de fichier réel | 10 fiches fictives importées puis réimportées sans perte ; correspondance des champs validée par écrit |
| **C6. Outils d'un établissement après rachat** | Sur inventaire | Sur devis | Établissement, exploitant et accès identifiés | Outils en service **au nom de l'exploitant**, documentés, restaurables |
| **C7. Aide au recrutement d'un coordinateur local chez GianLuca** | 3 à 5 JP | 3 000 à 4 500 € HT | Décision de GianLuca de recruter | Fiche de poste, procédures écrites, transfert des outils ; le recrutement lui-même reste au client |

**Coûts directs** : photographe, déplacements et outils de mise en page, refacturés seulement s'ils sont payés par Marwin et prévus au devis ; de préférence achetés directement par le client. **Marge visée** : 10 à 20 % sur coût complet, grâce aux aléas inclus [ES].

### 4.4 Offre D : exploitation d'un processus outillé, payée au résultat

**Condition d'entrée [PR].** Un pilote réussi (critères tenus 4 semaines), puis 2 à 3 mois de critères tenus en régime, une reprise manuelle testée et une restauration testée (`syn-capacite-ia.md` § 6.0). Le prix porte sur un **volume et un niveau de service**, pas sur des heures.

| Processus | Contenu | Prix [ES / PR] | Hypothèse de coût |
| --- | --- | --- | --- |
| **D1. Exploitation du CRM** | Qualification continue, imports et exports des résultats d'appel, liste d'opposition, sauvegarde quotidienne, export mensuel | 1 200 à 1 800 € HT par mois jusqu'à 100 fiches qualifiées et une campagne ; au-delà, 12 à 18 € HT par fiche **acceptée** | Qualification manuelle estimée à 10 à 15 min par fiche (≈ 18 à 27 € de coût interne) [HY], ramenée à environ 5 min avec assistance si le pilote le confirme |
| **D2. Assistant documentaire du portefeuille** | Recherche avec citations dans les documents autorisés, jeu de test rejoué, maintenance | 600 à 900 € HT par mois | Maintenance de 0,3 à 0,5 JP par mois ; API plafonnée ; outil au nom du client |
| **D3. Rapprochement budgétaire mensuel** | Budget, engagé et payé par projet ; liste des écarts ; dossier pour l'expert-comptable | 800 à 1 200 € HT par mois jusqu'à 50 pièces | Calculs par formule, jamais par le modèle de langage ; validation par l'expert-comptable du client |

**Clause de prix [PR].**
- Le prix est fixe pendant 12 mois.
- Il est revu chaque année sur le volume.
- La première année, **les gains de productivité restent à Marwin**.
- À partir de la deuxième année, le prix unitaire baisse d'un tiers du gain mesuré [MM], partagé et documenté.

**Marge visée** : 35 à 50 % une fois les gains établis [HY]. Avant cela, environ 10 %.

### 4.5 Hors catalogue, gelé ou refusé

| Sujet | Règle S2 |
| --- | --- |
| Astreinte et urgences hors plages | Aucune par défaut. Si GianLuca la demande : option séparée, chiffrée à part (ACC:59, 105), jamais absorbée par B. |
| Exécution d'événements (présence, logistique) | Contrat séparé. L'organisateur légal est l'entité de GianLuca ou l'exploitant du lieu (`syn-droit.md` § 7). Marwin coordonne au titre de C3 ou de son mandat. |
| STRATES, Éclosion, laboratoire, DGX Spark | **Gelés.** Retirer la diapositive laboratoire (DECK `slides/laboratoire.html`). Reprise seulement avec un financeur écrit, un budget plafonné, une compétence démontrée ou sous-traitée, et pas avant le mois 6. Plafond de 10 % de la capacité, hors B. |
| Intermédiation de vente d'œuvres, commission, encaissement, garde ou transport d'œuvres, « enchères » | **Refusés.** Ils exposeraient Marwin à la LCB-FT et au droit de suite (`syn-droit.md` § 7), et le terme « enchères » est réservé aux opérateurs habilités (L321-2 C. com.). |
| Collaboration avec Medhi et BOJ.ART | **Hors offre** depuis le 4 nov. [DR] (§ 7.3). |
| Obligations d'exploitant (licences, ERP, spectacles) | Hors périmètre : Marwin prépare les dossiers, l'exploitant signe (`syn-portefeuille.md` § 4.3). |

### 4.6 Règle anti-double facturation

1. **Un livrable, une commande.** Chaque livrable et chaque JP sont rattachés à un seul bon de commande, dans un registre des commandes partagé avec le client.
2. **Le pilotage ne produit pas, la production ne pilote pas.** B ne contient aucun livrable de production. Un lot C ne contient que ses propres réunions de cadrage et de réception. Le suivi de l'avancement d'un lot passe par B, sans rien ajouter au devis du lot.
3. **La capacité de B ne se convertit pas en production.** Le report est limité à 20 %, pour du pilotage seulement (§ 4.2).
4. **Aucun travail déjà fait n'est refacturé.**
   - Le CRM livré est réglé par une licence ou une cession écrite, même gratuite (`syn-droit.md` § 6). Il n'entre dans aucun prix.
   - La mise en conformité du CRM n'est jamais facturée.
   - Les démonstrateurs internes et la mesure de référence du cadrage restent des investissements de Marwin.
5. **Outils et achats.** Les comptes et licences du client sont ouverts et payés par son entité, sans marge de Marwin. Les outils internes de Marwin sont dans ses frais généraux, jamais refacturés. Les débours ne sont refacturés que s'ils remplissent les quatre conditions du BOFiP (BOI-TVA-BASE-10-10-30, § 200) (`syn-droit.md` § 4.7).
6. **Déplacements.** Ils sont compris dans un rayon à fixer au contrat. Au-delà, ils sont facturés aux frais réels, sur justificatifs, après accord préalable.
7. **Relevé mensuel.** Par commande : JP consommées par personne, livrables remis, livrables reçus. GianLuca peut le contrôler.
8. **Malus et avoirs.** Un malus ou un livrable refusé donne lieu à un avoir sur la même commande, jamais à du travail gratuit sur une autre.

### 4.7 Ce que devient le taux de 750 € HT

| Avant (2 nov.) | Après (S2) [PR] |
| --- | --- |
| « Un seul taux » affiché au client (DECK `slides/formules.html:4`) ; « on ajuste le périmètre […] pas le taux » (OFF:18) | **Plus de taux unique affiché.** Le client achète des forfaits par périmètre (A, B, C) et des volumes (D). |
| Base de calcul de tous les prix | **Plancher interne** : aucun forfait ne descend sous 750 € par JP estimée, aléas compris. En dessous, on réduit le périmètre ou on refuse. |
| — | **Prix cible interne** : 880 à 950 € par JP estimée. Il se justifie par le coût complet à capacité réaliste (≈ 810 à 1 065 € par JP) et par le marché du temps partagé (800 à 1 200 €). Il reste sous le prix public d'un jour d'expert IA (1 250 €). |
| — | **Taux d'avenant** pour une capacité supplémentaire ponctuelle demandée par écrit : **900 € HT par JP**, en heures ouvrées. |
| Le taux s'applique au même prix à Morgan et à Mathys (`rj-R6-marche.md` (a)) | Le forfait évite de comparer chaque journée à un développeur (450 à 585 € en région) ou à un assistant. Sans preuve d'expérience senior, un taux de 900 € affiché resterait difficile à défendre ; un forfait au périmètre l'est moins. |

Si GianLuca a déjà vu « 750 € la journée-personne » [IN] (U04), on l'applique au seul cadrage (6 000 € HT) et on explique le passage au forfait pour la suite.

### 4.8 Rémunérer la responsabilité et la valeur quand l'automatisation réduit le temps

Dans un modèle au temps, chaque gain réduit le chiffre d'affaires (REM-4, `syn-sources.md`). La règle des 29 et 30 oct., qui voulait « ajuster le forfait » aux gains (V5 p. 4), est **à retirer** (`syn-droit.md` § 2, n° 18). Six mécanismes la remplacent [PR] :

1. **Pilotage au périmètre.** Le prix de B dépend du nombre de projets suivis et des niveaux de service, pas des heures. Le temps gagné reste à Marwin dans le forfait. Le client gagne en couverture : 8 projets au lieu de 6 en B3 si les gains sont mesurés.
2. **Exploitation au volume** (offre D). Prix par fiche acceptée, par rapport ou par lot de pièces, fixé sous le coût manuel du client. Le gain va à Marwin la première année, puis il est partagé (un tiers au client à partir de la deuxième année).
3. **Mise en place rémunérée.** Chaque outil passé en exploitation a un lot C de mise en place, qui paie la conception une fois.
4. **Prime de responsabilité dans le socle.** Registre, mandat, conformité et coordination des professionnels portent une responsabilité réelle. Elle est payée dans le socle de B, même quand la production diminue.
5. **Bonus et malus sur ce que Marwin contrôle** (délais, comptes rendus, registre), jamais sur les ventes d'œuvres. Une rémunération liée aux ventes exposerait Marwin au statut d'intermédiaire (LCB-FT, droit de suite) sans avis d'avocat (`syn-portefeuille.md` § 1.5).
6. **Prime de gain, en option à 12 mois.** Si une automatisation supprime une dépense que GianLuca payait réellement (sous-traitance, heures facturées), Marwin perçoit 20 à 30 % de l'économie de la première année [HY]. Elle doit être mesurée [MM] et validée par écrit. On ne la propose pas avant d'avoir une référence.

---

## 5. Calendrier de paiement (la contradiction est tranchée)

**Règle S2 [PR] : le temps réservé se paie d'avance, les livrables se paient à la réception, et rien ne commence sans acompte encaissé par une société immatriculée.**

| Offre | Échéance | Quand | Justification |
| --- | --- | --- | --- |
| A. Cadrage | 50 % à la commande, 50 % à la réception | Acompte encaissé **avant** le démarrage. Solde exigible à la réception **ou**, au plus tard, 30 jours après la remise si aucune réserve motivée n'a été formulée | L'acompte couvre le coût engagé. Le solde ne dépend pas du silence du client, mais le silence ne vaut pas réception : la cession des droits n'a lieu qu'à la réception expresse et au paiement complet. |
| B. Pilotage | Mensualité d'avance | Facture le 1er jour ouvré du mois, payable sous 10 jours. Le premier mois est payable à la signature. | Une capacité réservée est du temps bloqué. Avant toute facture payée, le client n'expose qu'un mois. |
| C. Lots | 50 % à la commande, 50 % à la réception (même règle que A). Au-delà de 10 000 € HT : 40 / 30 / 30 avec un jalon intermédiaire | — | Marwin ne préfinance jamais plus de la moitié d'un lot. |
| D. Exploitation | Mensualité d'avance ; volume excédentaire facturé à terme échu le mois suivant | Comme B | Comme B |
| Achats et prestataires du client | Payés directement par son entité | — | Marwin ne détient pas les fonds du client (`syn-droit.md` § 4.7). |
| Retard | Pénalités au moins égales à 3 fois le taux légal, indemnité de 40 € ; **suspension** des travaux 8 jours après une relance restée sans effet ; résiliation pour faute à 30 jours de retard | — | Conforme à L441-10 [FV] (`syn-droit.md` § 3.2) |

**Comment la contradiction se résout.**
- La version du 29 oct. (« sous sept jours après facture de fin de mois », ACC:57) faisait travailler Marwin environ 37 jours avant d'être payée, à chaque échéance [ES].
- La version du 2 nov. (« d'avance, en début de mois », OFF:19, 195) demandait à un client qui n'a rien payé de préfinancer six mois à 15 000 €, sans règle de sortie (`syn-sources.md` PAY-5).
- S2 garde l'avance **pour le seul temps réservé**, sur un engagement de trois mois puis mensuel. Elle paie les livrables à la réception, et prévoit un **remboursement au prorata** des jours non fournis si Marwin interrompt la mission de son fait.
- Le titre « payé d'avance » de la diapositive (`paiement.html:4`) devient : « Le temps réservé est payé d'avance, les livrables à la réception ».

**TVA.** Elle est facturée à 20 % dès la première facture, sans compter sur la franchise : à ces montants, elle tomberait dans l'année (`syn-droit.md` § 3.2). La TVA d'un acompte est exigible à l'encaissement.

**Ordre des opérations [PR].**
1. Violation de données traitée (4-5 nov.).
2. Documents mis en cohérence, pacte et statuts prêts (avant le rendez-vous).
3. Rendez-vous avec GianLuca : entité, signataire, priorités ; lettre d'intention ou bon de commande du cadrage, signé au nom de la société en formation, avec un état des actes annexé aux statuts.
4. Dépôt du dossier d'aide régionale, si l'entité y est éligible.
5. Immatriculation, compte bancaire, RC professionnelle.
6. Facture d'acompte ; démarrage du cadrage à l'encaissement.

Rien n'est encaissé sur un compte personnel ni par l'entreprise existante de Morgan (`syn-droit.md` § 3.1 et 3.3).

**Tests d'échec sur la trésorerie** (scénario central) [ES] :
- **Retard de 30 jours sur B2.** La suspension intervient vers le 18e jour. Il manque environ 8 000 € HT pendant un mois. Cela se couvre si la réserve atteint au moins deux mois de frais fixes, soit environ 5 000 €.
- **Retard de 60 jours.** Résiliation pour faute. Environ 16 000 € HT (19 200 € TTC) sont décalés ou perdus. Les rémunérations de la SAS sont suspendues : c'est l'avantage de la SAS, sans cotisation minimale quand il n'y a pas de rémunération (`syn-droit.md` § 1.2).
- **Retard de 90 jours.** Recouvrement judiciaire. Le travail est arrêté depuis le 18e jour, donc la perte est plafonnée à environ un mois et demi de B.
- **Rupture après trois mois.** Les trois mois fermes ont été payés d'avance : aucune perte sur B. Les lots en cours ont été payés à 50 %.

---

## 6. Trois scénarios

Hypothèses communes [HY] :
- SAS ; coût total d'une rémunération égal à 1,7 à 1,9 fois le net ; réserve de 10 % du chiffre d'affaires, avant impôt sur les sociétés ;
- capacité facturable tirée de `syn-capacite-ia.md` § 2.3 ;
- nets avant impôt sur le revenu ;
- premier encaissement en décembre 2026.

| | **Prudent** | **Central** (recommandé) | **Ambitieux** |
| --- | --- | --- | --- |
| **Disponibilité des associés** | Morgan 50 %, Mathys 25 % ; Morgan garde OLSEN et ses autres projets | Morgan 65 %, Mathys 50 % ; Morgan réduit fortement ses autres projets | Les deux à 90 % ; Morgan arrête l'essentiel du reste ; sous-traitant encadré |
| **Capacité facturable** | ≈ 7 JP par mois | ≈ 12 JP par mois | ≈ 18 à 20 JP + 4 JP sous-traités |
| **Périmètre en régime (mois 6 à 12)** | A, puis B1 (2 projets actifs), 1 petit lot par trimestre | A, puis B1 et B2 à partir du mois 5, 1 lot par mois en moyenne, D1 à partir du mois 8 | A, puis B2 et B3 à partir du mois 7, 1 à 2 lots par mois, D1 et D2, un second client |
| **Prix** | B1 5 400 € ; lots ≈ 1 000 € par mois en moyenne | B2 8 000 € ; lots ≈ 2 500 € ; D1 ≈ 1 500 € | B3 11 800 € ; lots ≈ 7 000 € ; D ≈ 3 000 € ; second client ≈ 3 000 € |
| **CA mensuel en régime** | **≈ 6 400 €** | **≈ 12 000 €** | **≈ 22 000 à 25 000 €**, dont ≈ 3 000 € hors Carlone |
| **CA de la première année** (déc. 2026 à nov. 2027) | ≈ 64 000 € | ≈ 112 000 € | ≈ 200 000 € |
| **Frais fixes mensuels** | ≈ 1 800 € | ≈ 2 500 € | ≈ 3 500 € + sous-traitance ≈ 2 000 € (4 JP à environ 500 €) |
| **Net par associé en régime** | ≈ 1 050 à 1 150 € | ≈ 2 200 à 2 450 € | ≈ 3 700 à 4 150 € (hors second client) |
| **Net moyen sur la première année** | ≈ 750 € | ≈ 1 500 € (≈ 1 900 € en SARL TNS) | ≈ 2 900 € |
| **Réserve en régime** | ≈ 640 € par mois | ≈ 1 200 € par mois | ≈ 2 200 € par mois |
| **Part de GianLuca dans le CA au mois 12** | ≈ 100 % de Marwin, mais Marwin n'est qu'une activité parmi d'autres pour Morgan | Objectif ≤ 85 % | ≈ 88 % (objectif ≤ 80 % à 18 mois) |
| **Point bas de trésorerie, avant rémunération** | ≈ −2 000 € (décembre) | ≈ −3 750 € (décembre) | ≈ −4 750 € (décembre) |
| **Seuil de rentabilité** | ≈ 2 000 € de CA par mois pour couvrir les frais ; ≈ 10 000 € pour 2 000 € nets chacun | ≈ 2 800 € pour les frais ; ≈ 10 800 € pour 2 000 € nets ; ≈ 12 800 € pour 2 500 € nets | ≈ 3 900 € pour les frais ; ≈ 13 900 € pour 2 500 € nets chacun |
| **Hypothèses clés** | GianLuca ne confie qu'un ou deux projets ; Marwin reste un complément de revenu | Cadrage payé en décembre et janvier ; B commandé en février ; un lot CRM au printemps ; pilotes mesurés | Gains de 1,5 fois mesurés sur P1 et P3 ; sous-traitant fiable ; prospection réussie ; aucune indisponibilité longue |
| **Condition d'entrée** | Cadrage reçu | Disponibilités nominatives écrites ; B1 aux critères pendant trois mois | Engagement à 90 % signé dans le pacte ; B2 aux critères ; second client signé |

Calculs : `s2.py` et `annee1.py` [ES].

**Lecture.**
- **Le scénario central fait vivre deux personnes modestement**, autour de 2 000 à 2 500 € nets chacun en régime et environ 1 500 € en moyenne la première année. Il est loin de l'objectif de 7 500 € nets attribué aux fondateurs [DR] (OFF:118 ; `syn-sources.md` REM-3). Cet objectif supposait 40 JP facturés pendant douze mois, ce qui est impossible à deux (`syn-capacite-ia.md` § 2.6).
- **Ce qui change l'équation**, c'est le volume rendu possible par des gains mesurés, l'exploitation au volume (D), la sous-traitance encadrée et un second client. Ce n'est pas le taux affiché.
- **Besoin de financement initial** : environ 8 000 à 14 000 € [ES]. Il comprend la création (3 000 à 6 000 €), le conseil sur la violation (1 000 à 3 000 €) et deux mois de frais sans recette. Il est à couvrir par le capital libéré et des apports en comptes courants des associés [IN : leurs moyens], **jamais par GianLuca**. L'acompte n'est ni du capital ni un prêt (OFF:149).

---

## 7. Structure recommandée et relations

### 7.1 Forme juridique

**Recommandation : une SAS à l'IS** [PR], conformément à la recommandation conditionnelle de `syn-droit.md` § 1.10. Trois raisons :
- aucune rémunération régulière n'est financée par un contrat signé [FV] ;
- une entrée de GianLuca au capital est évoquée [DR] ;
- un associé pourrait garder un emploi extérieur [DR].

S2 ajoute une raison : la **souplesse de rémunération**. On peut suspendre les salaires lors d'un impayé, sans cotisation minimale.

**Conditions [PR].**
- Un président et un directeur général, chacun avec au moins un tiers du capital (condition de l'ACRE, si l'un des deux y est éligible).
- Un capital modeste, entièrement libéré, pour bénéficier du taux réduit d'IS de 15 %.
- Statuts organisant le blocage ; pacte signé **avant** le contrat client.
- Pas de rémunération avant le premier encaissement, puis une rémunération fixée par décision collective.
- Immatriculation déclenchée par l'engagement écrit de l'entité de GianLuca (lettre d'intention ou bon de commande signé « en formation »), pas avant (`syn-droit.md` § 1.10, point 5).

**Coût de ce choix.** Environ 5 000 à 12 000 € de net par personne et par an de moins qu'une SARL TNS, à 120 000-180 000 € de CA [ES]. À confirmer par une simulation officielle de l'expert-comptable.

**SARL en cogérance 50/50, seulement si toutes ces conditions sont réunies** :
- pas d'investisseur avant 24 mois ;
- un contrat d'au moins 120 000 € par an signé ;
- aucun associé salarié ailleurs.

Il faut alors provisionner la régularisation TNS de la deuxième année.

**Ne pas facturer par l'entreprise existante de Morgan** : sa domiciliation est résiliée (NOTE:6), et cela brouillerait la propriété du client et le FRR (`syn-droit.md` § 3.1).

### 7.2 Relations avec GianLuca : quatre rôles, quatre accords

| Rôle | Principe S2 [PR] | Ce qu'il faut éviter |
| --- | --- | --- |
| **Client** | Contrat-cadre et fiches de mission **par entité** ; validateur nommé, distinct de tout fondateur salarié ; mandat écrit par entité. | Un accord personnel censé engager toutes ses sociétés. |
| **Bailleur** | Convention de bureaux séparée : accès sans horaires imposés, usage partagé, assurance, restitution alignée sur le préavis du contrat, gratuité ou loyer écrits. Aucun lien entre bureaux et honoraires (OFF:132). | Horaires imposés, badge de salarié, place dans un organigramme : ce sont des indices de subordination (`syn-droit.md` § 4.2). |
| **Employeur** | **Différé** au-delà du bilan du 6e mois. S'il est retenu : une seule personne, des fonctions disjointes du contrat Marwin, des temps séparés, et une autre personne qui valide les livrables Marwin (`syn-droit.md` § 4.6). Jamais utilisé comme argument de prix. | Être salarié et prestataire du même client sur les mêmes sujets. |
| **Investisseur** | Pas avant 12 à 24 mois. Minoritaire, sans veto opérationnel, avec un droit d'information. Contrat client résiliable indépendamment. **Jamais en échange d'une baisse d'honoraires** (OFF:149). Les fondateurs gardent la majorité. | Accepter un financement de la R&D en guise de chiffre d'affaires. |

**Plafond de dépendance [PR].** La part de GianLuca dans le CA est suivie chaque mois. Cible : au plus 85 % au mois 12 et 70 % au mois 18 dans le scénario central. Le temps de prospection d'un second client est protégé : 1,5 à 2,5 JP par mois (`syn-capacite-ia.md` § 2.3 ; AUD:55 ; CTX:95).

### 7.3 Relations avec Medhi

1. **Formaliser le retrait par écrit** entre Morgan et Mathys : portée exacte (offre, STRATES, vernissage, catalogue, laboratoire, PR n° 1), et retrait définitif ou suspension [PR].
2. **Informer Medhi par écrit** de ce qui lui a été présenté ou promis : exclusivité, films, ligne création. Personne n'agit au nom de Marwin envers lui sans cet écrit.
3. **Déclarer à GianLuca le lien de Morgan avec BOJ.ART** (co-porteur selon ACC:21, organisateur selon CTX:25). S'abstenir de préparer une décision d'achat qui concerne les pièces de Medhi (`syn-sources.md` ASS-4).
4. **Ne rien promettre de ce que Marwin ne détient pas** : œuvres, motifs, films, accès au parc d'impression, code de Jarvis (`syn-droit.md` § 6). Le nom « Jarvis » n'est pas utilisé tant que la propriété du code n'est pas réglée.
5. **Toute relation future** passe par un contrat séparé : prix, propriété intellectuelle, attestation de vigilance au-delà de 5 000 € HT. Si la galerie vend ses pièces, c'est un dépôt-vente direct entre Medhi et l'entité de GianLuca, sans commission pour Marwin.

---

## 8. Gouvernance minimale

### 8.1 Qui fait quoi

| Acte | Propose | Autorise | Exécute | Contrôle | Valide le résultat |
| --- | --- | --- | --- | --- | --- |
| Priorités du mois et changement de projet actif | Marwin (Morgan) | GianLuca, ou son délégué écrit, en comité mensuel | Marwin | Mathys (cohérence capacité et encours) | GianLuca |
| Livrable Marwin (lot, rapport) | Marwin | Bon de commande signé par l'entité | L'associé responsable | **L'autre associé** (règle des quatre yeux) | Le validateur nommé de l'entité |
| Document envoyé au client | L'auteur | — | L'auteur | L'autre associé, avec le registre « décision → documents touchés » | Morgan, ou Mathys par délégation écrite |
| Dépense au nom de l'entité | Marwin | GianLuca selon les plafonds ci-dessous | L'entité paie | Marwin tient le registre des engagements | Expert-comptable de l'entité |
| Contrat, recrutement, travaux, bail, emprunt, investissement | Marwin peut préparer le dossier | **Toujours GianLuca**, ou le signataire de l'entité | L'entité | Ses conseils | GianLuca |
| Automatisation sur données réelles | Mathys | GianLuca (périmètre et données), après les préalables RGPD | Mathys | Morgan (critères du pilote) | GianLuca (adoption) |
| Incident (données, envoi erroné, action non autorisée) | Quiconque le constate **arrête** le processus | — | Mathys (mesures techniques) | Avocat ou DPD si nécessaire | Morgan informe GianLuca par écrit sous 24 h |

### 8.2 Plafonds et règles [PR, montants à valider avec GianLuca]

- **Dépense unitaire sous mandat** : au plus 500 € HT, pour des catégories listées au mandat. La facture est au nom de l'entité et payée par elle.
- **Cumul mensuel** : au plus 1 500 € HT par entité.
- **Engagement récurrent** (abonnement, location) de plus de 50 € par mois ou de plus de 3 mois : accord écrit préalable.
- **Urgence** (sécurité, perte de données, échéance légale à moins de 48 h) : mesure conservatoire d'au plus 300 € HT, information écrite sous 24 h, puis régularisation.
- **Le silence ne vaut pas accord** (ACC:103). Une décision bloquante sans réponse donne lieu à :
  - une relance au bout de 5 jours ouvrés ;
  - un report automatique des jalons concernés et une escalade au bout de 10 jours ;
  - une revue du contrat (réduction de palier) au bout de 15 jours.

  La règle « réputé accepté » (OFF:206) est retirée. Seule l'exigibilité du solde a une échéance (§ 5).
- **Désaccord sur un livrable** : réserves motivées sous 10 jours ouvrés ; un cycle de correction compris ; puis arbitrage en comité ; puis avenant ou arrêt du lot.
- **Arbitrage entre projets** : en comité mensuel. Entre deux comités, par écrit du délégué. La limite d'encours s'applique toujours.
- **Prestataires** : Marwin coordonne mais ne donne pas d'ordres aux salariés d'un prestataire, par exemple aux opératrices de Quali Contact. Les consignes passent par leur employeur (`syn-droit.md` § 4.3).
- **Entre associés (pacte)** :
  - unanimité pour le contrat avec GianLuca, le prix, tout engagement de plus de 2 000 € et toute entrée au capital ;
  - en cas de blocage : médiation, puis tiers expert, puis offre alternative ;
  - déclaration écrite des autres activités et de la disponibilité mensuelle ;
  - délégation écrite de la validation technique à Mathys, avec un délai de validation de 2 jours ouvrés au plus (`syn-capacite-ia.md` § 4).

### 8.3 Adoption

Une livraison n'est réussie que si elle est **utilisée**. Indicateurs du pilote P1 :
- GianLuca ou son délégué réagit à au moins 80 % des comptes rendus sous 3 jours ouvrés ;
- le registre est consulté au moins une fois par semaine.

En dessous de ces seuils pendant 4 semaines, on revient au mode manuel et on refait le cadrage du processus (`syn-capacite-ia.md` § 6.1).

---

## 9. Feuille de route

### 9.1 Les 90 premiers jours (4 nov. 2026 → début février 2027)

| Période | Livrables | Indicateurs | Responsable | Condition de passage |
| --- | --- | --- | --- | --- |
| **4-5 nov.** | Dépôt rendu privé et vérifié ; fiche de violation ; décision de notification tracée, avec un avocat ou un DPD ; information écrite de GianLuca | Décision prise avant l'échéance du 5 nov., ou retard motivé | Mathys (dépôt) ; Morgan et Mathys (décision) | **Aucun** usage de données réelles avant cette étape |
| **Semaines 1-3** | Documents historiques marqués (offre écrite, STRATES v1.1, vernissage, PDF de 13 p., diapositive laboratoire) ; décision écrite sur Medhi ; fiche « rôles et disponibilités » ; projet de pacte et de statuts ; proposition client **réduite au cadrage A** | Tous les documents client cohérents avec la décision du 4 nov. ; disponibilités nominatives écrites | Morgan (documents, Medhi) ; les deux (pacte) | Accord écrit de Mathys sur S2 |
| **Rendez-vous** (date [IN]) | Entité, signataire, valideur ; trois intentions de priorités ; lettre d'intention ou bon de commande du cadrage | Entité identifiée par sa dénomination et son SIREN | Morgan | Sans entité identifiée, rien ne démarre |
| **Semaines 3-6** | Immatriculation ; compte bancaire ; RC professionnelle ; plateforme de réception des factures électroniques ; comptes techniques au nom de Marwin ; facture d'acompte | Acompte de 3 750 € HT encaissé | Morgan (formalités) ; Mathys (comptes techniques) | Encaissement avant tout démarrage |
| **Semaines 6-11** (congés exclus) | Cadrage A : les 7 livrables ; mesure de référence de P1 et P3 ; démonstrateur interne de P3 sans données de prospects | Réception du cadrage ; trois priorités signées ; accès fournis sous 10 jours ouvrés | Morgan (priorités, mandat) ; Mathys (registre, mesures) | Réception expresse et solde payé |
| **Jour 90** | Proposition B (palier) et lots chiffrés ; commande de B1 ou B2 signée ; premier mois payé | CA encaissé ≈ 7 500 € ; 0 incident critique ; occupation ≤ 85 % | Les deux | Sinon : bascule vers O1 ou O3 (§ 10) |

**Budget des 90 jours** [ES] : 8 000 à 14 000 € de dépenses, contre environ 7 500 € de recettes, d'où le besoin de financement initial (§ 6).

### 9.2 À six mois (début mai 2027)

| Livrables | Indicateurs | Seuils de révision |
| --- | --- | --- |
| B en régime depuis 3 mois, avec bilan du 3e mois (B1 → B2 ou maintien) | Comptes rendus sous 24 h dans au moins 90 % des cas ; 100 % des décisions complètes ; rapport mensuel au 5e jour ouvré | Deux engagements manqués deux mois de suite : réduction du palier |
| P1 (registre et comptes rendus) passé en exploitation interne ; P3 (recherche documentaire) mesuré | Temps humain par réunion ≤ 70 % de la référence ; recherche documentaire ≥ 90 % de réponses justes et citées, 0 citation inventée | Contrôle et corrections > 50 % du temps de référence pendant 4 semaines : abandon du processus |
| Au moins un lot reçu (C1, C2 ou C3) | Livrables acceptés au premier passage ≥ 75 % | Refus > 35 % : nouveau cadrage des critères |
| Prospection : au moins 3 propositions envoyées hors Carlone, et 1 signée | Temps de prospection ≥ 75 % du plancher | < 50 % pendant 2 mois : réduction du périmètre client |
| Pacte signé ; attestation Urssaf et K-bis remis au client au mois 6 | Taux d'occupation ≤ 85 % | > 95 % pendant 2 mois : refus de nouveau projet, puis sous-traitance |

### 9.3 À douze mois (début novembre 2027)

| Livrables | Indicateurs | Décisions attendues |
| --- | --- | --- |
| B2 (central) ou B3 (ambitieux) ; 4 à 6 projets actifs suivis | Projets suivis par JP de pilotage : de 1,25-1,5 à 1,0-0,8 [HY] ; décisions préparées à temps ≥ 90 % | Palier de l'année 2 ; prix revus sur le périmètre |
| D1, et éventuellement D2, en exploitation, avec un coût par résultat accepté connu | Temps humain par résultat accepté réduit de 30 à 50 % sur les processus pilotés [HY] ; restauration testée chaque trimestre | Partage des gains de l'année 2 (§ 4.4) |
| Exercice de sortie à blanc réussi (fait au 6e mois de B) | Restitution complète en 15 jours ouvrés au plus | — |
| CA mensuel ≈ 12 000 € (central) ; part de GianLuca ≤ 85 % | Retard de paiement moyen ≤ 10 jours ; réserve ≥ 2 mois de frais fixes | Faut-il recruter ou sous-traiter durablement ? (oui seulement après 3 mois au-delà de 85 % d'occupation, avec un contrat qui le finance) |
| Émission des factures électroniques conforme au 1er sept. 2027 | 100 % des factures conformes | Bureaux, emploi, investissement : chacun traité par un accord séparé |

---

## 10. Commencer, suspendre, réduire, reporter ou refuser

### 10.1 Conditions minimales pour commencer (toutes requises)

1. Violation traitée : dépôt privé, fiche de violation, décision de notification, information écrite de GianLuca.
2. Documents destinés au client cohérents avec la décision du 4 nov., les anciennes versions marquées « historiques » et datées.
3. Accord écrit entre Morgan et Mathys sur S2 : disponibilités nominatives, rôles, rémunération visée, retrait de Medhi.
4. Entité de GianLuca identifiée : dénomination, SIREN, signataire, validateur.
5. SAS immatriculée ; compte bancaire, RC professionnelle et comptes techniques à son nom ; pacte signé.
6. Bon de commande du cadrage signé et acompte encaissé.
7. Aucune donnée personnelle réelle traitée avant le responsable de traitement, le contrat de l'article 28 et le registre.

### 10.2 Signaux de suspension

- Retard de paiement de plus de 8 jours après une relance.
- Accès non fournis 10 jours ouvrés après le démarrage.
- Deux décisions bloquantes en attente depuis plus de 15 jours ouvrés.
- Taux d'occupation des associés au-delà de 95 % pendant deux mois.
- Un incident critique (données, envoi erroné, action non autorisée).
- Une demande d'agir hors mandat : signer, payer ou engager pour le client.
- Des indices de subordination : horaires imposés, ordres directs, place dans un organigramme.
- Un investissement proposé en échange d'une baisse d'honoraires.
- Une demande de rémunération sur les ventes d'œuvres, ou d'encaissement pour la galerie.

### 10.3 Réduire, reporter, refuser

| Situation | Réponse S2 |
| --- | --- |
| GianLuca ne veut confier qu'un projet, par exemple la vente d'œuvres | **Réduire** : lots C1, C4 et C5, éventuellement B1 limité à ce projet (objectif O3) |
| Cadrage reçu, mais pas de demande de suivi récurrent | **Réduire** : objectif O1 ; clôture propre ; relance à 3 mois |
| Entité non identifiée, violation non réglée, disponibilités non écrites ou Mathys en désaccord à la mi-décembre | **Reporter** à janvier 2027 ; aucune production nouvelle en attendant |
| Cadrage non commandé et payé avant fin janvier 2027 | **Reporter sans date** et réorienter le temps vers d'autres clients |
| « Commencez, on verra le paiement » ; demande de 40 JP ; mélange de salariat et de prestation sur les mêmes sujets ; rôle d'exploitant, d'intermédiaire de vente ou d'organisateur légal ; R&D sans financeur écrit | **Refuser** cette partie, en expliquant pourquoi, et proposer le cadrage |
| Indisponibilité d'un associé pendant plus de 10 jours ouvrés | Réduction du palier par avenant, sans pénalité, et report des lots |

---

## 11. Cinq décisions prioritaires

1. **Violation de données, à décider avant l'échéance du 5 nov.** (Morgan et Mathys, avec un avocat ou un DPD) : rendre le dépôt privé, ouvrir la fiche de violation, décider de la notification et la tracer, informer GianLuca par écrit. Aucune donnée réelle ne sera utilisée avant.
2. **Retirer l'offre du 2 nov.**
   - Retirer le 15 000 / 30 000 € avec 750 € comme « taux unique », l'ancre de 46 JP, l'option laboratoire et tous les supports qui citent Medhi, STRATES ou BOJ.ART.
   - Marquer comme historiques l'offre écrite, STRATES v1.1, le vernissage et le PDF de 13 p. de la PR n° 1.
   - Adopter l'architecture A / B / C / D et la règle anti-double facturation.
3. **Engagement nominatif et pacte.**
   - Fixer par écrit combien de JP par mois Morgan et Mathys donnent à Marwin, et quels projets Morgan arrête (OLSEN, Shelby, BOJ.ART…).
   - Déléguer la validation technique à Mathys.
   - Signer le pacte avant le contrat client.
   - Sans cela, seul le scénario prudent est défendable.
4. **Créer une SAS déclenchée par un engagement écrit de l'entité de GianLuca.** Ne rien encaisser avant ; ne pas facturer par l'entreprise existante de Morgan.
5. **Ne vendre qu'une chose au prochain rendez-vous : le cadrage A** (7 500 € HT, 50 / 50). Repartir avec l'entité, le signataire, le validateur, les trois priorités et la date de l'acompte. Le pilotage récurrent n'est proposé qu'à la réception du cadrage.

---

## 12. Principaux risques et preuve qui lèverait chaque objection

| Risque ou objection | Probabilité / gravité [HY] | Preuve qui lèverait l'objection | Parade en attendant |
| --- | --- | --- | --- |
| Le pilotage global n'est pas le besoin prioritaire de GianLuca | Élevée / élevée | Cadrage commandé et payé ; trois priorités signées ; demande écrite de suivi récurrent après le cadrage | Vendre le cadrage seul ; replis O1 et O3 |
| Aucune entité solvable ne paie | Moyenne / critique | Bon de commande signé par une entité identifiée ; acompte encaissé ; paiements à l'heure pendant 3 mois | Paiement d'avance du temps réservé ; 50 % à la commande |
| Il délègue sans fournir moyens ni accès | Moyenne / élevée | Accès fournis sous 10 jours ouvrés ; délégué et validateur nommés ; inventaire validé | Report automatique des jalons ; suspension (§ 10.2) |
| Les deux associés deviennent le goulet d'étranglement | Élevée / élevée | Occupation ≤ 85 % pendant 3 mois ; file de validation ≤ 2 jours ouvrés ; limite d'encours respectée | Paliers, sous-traitance d'un lot, refus d'un nouveau projet |
| Le budget finance des outils, pas le travail | Moyenne / moyenne | Outils sur les comptes du client et payés par lui ; Marwin ne facture que du travail ; frais d'outils ≤ 3 % du CA | Règle anti-double facturation, point 5 |
| La recherche absorbe la marge | Élevée (par habitude) / élevée | Temps exploratoire ≤ 10 % de la capacité, hors B, et financé par écrit ; aucun achat de matériel | Gel de STRATES, d'Éclosion et du laboratoire |
| Les équipes n'adoptent pas les outils | Moyenne / élevée | Comptes rendus lus et validés dans au moins 80 % des cas sous 3 jours ; registre consulté chaque semaine | Mode manuel ; nouveau cadrage du processus ; lot C7 (coordinateur local) |
| Les responsabilités dépassent les pouvoirs | Moyenne / élevée | Mandat signé par entité, avec plafonds ; RC professionnelle couvrant l'IA et les données, au même plafond que le contrat | Refus d'agir hors mandat |
| Dépendance à une seule personne (Morgan, GianLuca) | Élevée / élevée | Procédures testées par l'autre associé ; un second client au moins à 15 % du CA au mois 12 | Plancher de prospection ; coffre partagé des accès |
| Les prix ne couvrent pas la maintenance | Moyenne / moyenne | Coût par résultat accepté mesuré ; maintenance de D ≤ 0,5 JP par mois et par processus ; marge de D ≥ 35 % après la 1re année | Prix au volume ; clause de révision annuelle |
| Promesse trop large pour être réceptionnée | Élevée aujourd'hui / élevée | Chaque offre a ses critères ; au moins 75 % des livrables acceptés au premier passage | Retirer « vendre vos œuvres avec le CRM » (DECK `proposition.html:3`) |
| Requalification en salariat ou prêt de main-d'œuvre | Faible à moyenne / critique | Lots et livrables définis ; méthodes, outils et horaires choisis par Marwin ; autres clients réels | Convention de bureaux séparée ; salariat différé |
| Nouvelle exposition de données, ou injection dans un agent | Moyenne / critique | 0 incident critique ; journal ; arrêt testé chaque trimestre ; restauration testée | Classes d'actions ; approbation humaine pour tout envoi (`syn-capacite-ia.md` § 8.2) |
| Hausse des coûts d'IA ou arrêt d'un fournisseur | Moyenne / faible | Second fournisseur configuré ; API plafonnée ; données exportables | Coûts d'IA du client à son nom ; clause de révision |
| L'objectif de revenu des associés n'est pas atteint | Élevée / moyenne | Mois 6 : CA ≥ 10 800 € par mois (central) | Garder d'autres revenus pendant l'année 1 ; SAS sans cotisation minimale |

---

## 13. Questions bloquantes (dix au plus)

1. **Morgan et Mathys, avant le 5 nov.** Depuis quand connaissez-vous le caractère public du dépôt FinanceScope/CRM-Carlone ? Est-il toujours public ? Qui contrôle l'organisation FinanceScope ? Qui est responsable du traitement ?
2. **Morgan et Mathys.** Combien de JP par mois chacun peut-il engager nominativement de décembre 2026 à juin 2027, et quels projets Morgan arrête-t-il ?
3. **Mathys.** Approuves-tu l'architecture S2, la décision du 4 nov. sur Medhi et la délégation de la validation technique ?
4. **Morgan.** Quelles versions GianLuca a-t-il vues ou reçues (13 ou 11 diapositives, V5, lettre du 29 oct., rapport CRM, vernissage), et a-t-il vu le taux de 750 € ?
5. **GianLuca Carlone.** Quelle entité signe, paie et valide, pour chaque projet ? Dénomination, SIREN, personne habilitée.
6. **GianLuca Carlone.** Quelles sont vos trois priorités pour les 90 prochains jours, et que voulez-vous déléguer ? Les « vingt jours par mois » sont-ils votre demande ?
7. **GianLuca Carlone.** Quel budget mensuel pouvez-vous engager, et acceptez-vous de payer d'avance le temps réservé et à la réception les livrables ?
8. **GianLuca Carlone.** Quels accès et quels interlocuteurs (comptable, avocat, responsables de lieux) nous donnerez-vous, et qui sera votre délégué ?
9. **GianLuca Carlone.** Avez-vous engagé Quali Contact ? Qui appellera les entreprises, et au nom de quelle structure vendez-vous les œuvres ?
10. **GianLuca Carlone.** Pour les bureaux, l'emploi et l'investissement évoqués : sous quelle forme et à quelle échéance ?

---

*Limites.*
- Tous les prix sont des propositions [PR] fondées sur des estimations [ES]. Aucune n'a été confrontée à GianLuca Carlone ni validée par un expert-comptable.
- Les coefficients de coût d'une rémunération en SAS (1,7 à 1,9) sont une hypothèse de source secondaire (`syn-droit.md` § 1.1). Le site urssaf.fr était indisponible le 4 nov.
- Le lieu de résidence des associés, les durées de déplacement, la disponibilité et les compétences de Mathys, et le contenu des 50 conversations ChatGPT non lues restent [IN].
- La visibilité actuelle du dépôt FinanceScope n'a pas été revérifiée par cet audit.
