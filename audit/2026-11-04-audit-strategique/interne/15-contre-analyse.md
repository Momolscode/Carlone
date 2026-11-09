# Contre-analyse et conditions de refus

Audit Marwin Tech × GianLuca Carlone · livrable 15 sur 15 · 4 novembre 2026
Statut : interne (objections, probabilités, revenus des associés, positions de repli ; ne pas transmettre à GianLuca Carlone)
Sources principales : `travaux/strategie-retenue.md` (lu en entier) ; `travaux/strat-S2-pilotage.md` ; `travaux/strat-S3-contradicteur.md` ; `travaux/juge-J1-client.md` ; `travaux/juge-J2-marwin.md` ; `travaux/syn-portefeuille.md` ; `travaux/syn-capacite-ia.md` ; `modele-financier/scenarios.md` ; `modele-financier/stress-tests.md` ; pièces d'origine du dépôt Momolscode/Carlone (commit 7b46602, inchangées depuis selon `git diff`), rouvertes en lecture seule : `interne/offre-marwin-tech-remuneration-et-collaboration.md`, `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md`, `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md`, `interne/recueil-sessions-chatgpt-2026-11-04.txt`, `interne/contexte-projet-carlone.md`, `interne/audit-marwin-tech-carlone.md`, `crm/docs/rapport/rapport-crm-hermes360.md`.
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu. Sans autre précision, une [PR] vient de la stratégie retenue ; « [PR, ce livrable] » signale une proposition ajoutée ici ; « [ES, ce livrable] » un calcul fait ici à partir de chiffres sourcés.
Échelle de probabilité [HY] : **faible** (moins d'une chance sur cinq), **moyenne** (entre une sur cinq et une sur deux), **élevée** (plus d'une sur deux). Ce sont des jugements, à remplacer par les faits observés. Échelle de gravité : **moyenne** (retard ou perte de marge), **forte** (perte du client ou d'un semestre de travail), **critique** (fin du projet ou exposition personnelle des associés).
JP : journée-personne de 7 h. Les codes d'offres (A, B0, B1, B2, C1 à C8, D, E) sont ceux de `travaux/strategie-retenue.md:194-203`, détaillés dans 04-catalogue-offres.md.

---

## En bref

1. **La stratégie retenue va dans la bonne direction.** Retirer l'abonnement de 15 000 ou 30 000 € HT par mois, traiter la fuite avant tout, vendre au forfait, refuser la commission sur les ventes et le paiement en bureaux, en emploi ou en capital : ces choix résistent à la critique (section 2.1).
2. **Sa faiblesse est ailleurs.** Elle demande beaucoup de préparation avant le premier euro (dix conditions, `travaux/strategie-retenue.md:658-669`) pour un client qui n'a encore rien dit lui-même, rien signé et rien payé [FV négatif]. Et elle repose sur la compétence la moins démontrée des associés : vendre et conclure (section 2.2).
3. **La cause d'échec la plus probable ne figure pas dans la liste de départ : rien ne se passe.** Aucune société ne commande. Viennent ensuite un besoin qui porte sur un projet et non sur un pilotage global, le revenu trop faible des associés et la dispersion de Morgan dans des travaux non payés (sections 3 et 4).
4. **Avec ses propres probabilités, la stratégie conduit à un socle récurrent dans environ 4 cas sur 10 une fois le cadrage vendu** [ES, ce livrable]. La chance de vendre le cadrage est inconnue [IN].
5. **Recommandation ferme : poursuivre, mais comme un test commercial borné, pas comme le lancement d'une entreprise.** Avant un rendez-vous tenu et une société nommée, ne traiter que la fuite, les documents et les décisions entre associés. Engager du temps commande par commande. Ne quitter aucune source de revenu avant trois échéances de socle payées à l'heure (section 6).
6. **Trois écarts avec la stratégie retenue** (section 6.2) : limiter dépenses et production avant preuve à l'obligatoire ; examiner tout de suite une éventuelle offre d'emploi, comme une alternative séparée ; après un refus du cadrage, proposer un lot unique avant de conclure.
7. **Reporter** si, au 15 décembre 2026, aucun rendez-vous n'est tenu ou aucune société n'est nommée. **Réduire** à un lot si GianLuca n'a qu'une priorité. **Refuser** s'il veut qu'on « s'occupe de tout » tout de suite, sans société ni accès, payé plus tard ou en nature (section 7).

---

## 1. Objet de ce livrable

**Ce qu'il fait.** Il cherche pourquoi le projet pourrait échouer, y compris à cause de la stratégie retenue. Pour chaque raison, il donne une probabilité, un signe avant-coureur et la preuve qui lèverait l'objection. Il compare la stratégie à quatre autres voies, puis tranche.

**Ce qu'il ne refait pas.**
- Le registre complet des risques, des inconnues et des décisions : 14-registre-risques-inconnues-decisions.md.
- Les offres, prix et critères de réception : 04-catalogue-offres.md.
- La comparaison des coûts vue par GianLuca (Marwin, salarié, prestataires) : 05-proposition-de-valeur.md, section 4.
- Les tests de trésorerie : 09-modele-economique-tresorerie.md, section 9.
- Les clauses, l'adoption et la sortie : 12-gouvernance-contrat-sortie.md.
- Les réponses à préparer pour le rendez-vous : 13-preparation-rendez-vous.md, section 8.

**Ce que l'auteur ne sait pas.** Aucune parole directe de GianLuca Carlone n'existe dans les pièces [FV négatif] (`travaux/syn-portefeuille.md:89`). Cette contre-analyse raisonne donc, comme tout l'audit, sur une demande rapportée par Morgan [DR].

---

## 2. Ce qui tient, et ce qui ne tient pas, dans la stratégie retenue

### 2.1 Ce qui résiste à la critique

| Choix de la stratégie | Pourquoi il tient | Source |
| --- | --- | --- |
| Retirer l'abonnement de 20 ou 40 JP par mois | 20 JP prennent 78 à 83 % du temps disponible des deux associés, 40 JP en demandent 140 à 145 % [ES] ; aucune demande directe du client [FV négatif] | `travaux/syn-capacite-ia.md:228-229` ; `travaux/syn-portefeuille.md:89` |
| Traiter la fuite avant toute vente | Obligation légale à délai court ; rien ne peut se construire sur des données exposées | `travaux/strategie-retenue.md:32, 53` |
| Vendre au forfait, garder 750 € comme plancher interne | Dans un modèle au temps, chaque gain d'automatisation réduit le chiffre d'affaires | `travaux/strategie-retenue.md:416` |
| Payer le temps réservé d'avance et les livrables à la livraison | Exposition limitée à ≈ 5 500 à 6 000 € HT de travail non payé [ES] | `travaux/strategie-retenue.md:447` |
| Refuser commission sur les œuvres, robot devant le public, rôle d'exploitant, recherche sans financeur | Statut d'intermédiaire, sécurité du public, licences nominatives : risques que deux associés ne peuvent pas porter | `travaux/strategie-retenue.md:703` |
| Dates butoirs du 15 décembre 2026 et du 31 janvier 2027 | Elles limitent le travail gratuit, qui dure depuis le 18 octobre | `travaux/strategie-retenue.md:697-698` ; `travaux/syn-portefeuille.md:304` |

### 2.2 Six faiblesses

**F1. Le cadrage teste d'abord le besoin de Marwin.** Ses livrables (inventaire, priorités, grille de délégation, mesure de référence, comparaison des suites) servent surtout à dimensionner l'offre de Marwin [FV, lecture du texte] (`travaux/strategie-retenue.md:225`). Pour GianLuca, la valeur reste modeste tant qu'aucun lot n'a produit de résultat chez lui (`travaux/juge-J2-marwin.md:67`). Un client qui a reçu un CRM « offert » (`interne/offre-marwin-tech-remuneration-et-collaboration.md:227`) peut trouver étrange de payer 7 800 € TTC l'inventaire de ses propres affaires [HY]. Un refus peut donc viser la forme et non le besoin. La stratégie conclut pourtant, en cas de refus, à « refuser la suite » (`travaux/strategie-retenue.md:701`). Voir l'écart n° 3.

**F2. L'espérance de gain est faible au regard de l'effort fourni avant toute preuve.**
- Avant le premier euro : 9 à 17 JP de remise en ordre (`travaux/strategie-retenue.md:213`) et jusqu'à 8 JP de démonstrateurs internes (07-processus-ia-et-essais.md, section 0), soit **12 à 25 JP non payées**, une à deux fois et demie la capacité mensuelle engagée de 10 JP [ES, ce livrable]. S'y ajoutent 5 000 à 7 000 € HT de frais de démarrage en central (`modele-financier/scenarios.md:54`) et un apport de 8 000 à 14 000 € (`travaux/strategie-retenue.md:56`).
- Le cadrage rapporte 6 500 € HT, avec une marge de −9 à +13 % si la capacité facturée reste à 10 JP [ES] (`travaux/strategie-retenue.md:234`).
- Avec les probabilités de la stratégie (pilote après le cadrage : 60 % ; socle après le pilote : 70 %, `travaux/strategie-retenue.md:502`), un socle récurrent n'arrive que dans **≈ 42 % des cas** une fois le cadrage vendu [ES, ce livrable : 0,6 × 0,7]. Le chiffre d'affaires central pondéré tombe à 38 300 € HT sur douze mois (`modele-financier/scenarios.md:45`). Si le cadrage n'a qu'une chance sur deux d'être vendu [HY], l'espérance est **d'environ 19 000 € HT** [ES, ce livrable].
- Conséquence : la préparation doit suivre la preuve, pas la précéder. Voir l'écart n° 1.

**F3. La réussite dépend de la compétence la moins démontrée.** Vendre, signer, facturer et encaisser n'a jamais été fait sous Marwin [FV négatif] (`travaux/syn-capacite-ia.md:124`). Chez OLSEN, 36 propositions et 72 brouillons d'e-mails ont été préparés, aucun n'a été envoyé ; les 503 prospects sont tous « À faire » [DR] (`travaux/note-point-4-novembre-et-activites.md:9`). L'offre pour Carlone a connu sept états en dix jours sans réaction client documentée (`travaux/syn-capacite-ia.md:782`). La contrainte se situe en aval de la production : vente, validation, décision, réception (`travaux/syn-capacite-ia.md:784`). La stratégie suppose que Morgan envoie un message, obtient un rendez-vous, fait nommer une société et encaisse un acompte. Rien de cela n'a de précédent dans les pièces [FV négatif]. Ce n'est pas une erreur de la stratégie : c'est son hypothèse principale non testée. Le premier test est simple : le message et la proposition partent-ils à la date prévue, le 27 novembre (pour-gianluca/message-de-recadrage.md, note interne) ?

**F4. Un pilotage sans pouvoir ne vaut que si GianLuca décide vite et par écrit.** Mandat de dépense à 0 € pendant le cadrage et le pilote (`travaux/strategie-retenue.md:589`), coordination sans commandement direct des salariés (`travaux/strategie-retenue.md:261`), silence qui ne vaut jamais accord (`travaux/strategie-retenue.md:603`) : ces règles protègent Marwin. Elles font aussi dépendre toute la valeur du pilotage de la vitesse de décision de GianLuca. Or son canal de travail [IN] (`travaux/juge-J1-client.md:190`) et son équipe [IN] (`travaux/syn-portefeuille.md:211-216`) sont inconnus. S'il travaille à l'oral, sans délégué, le registre ne sera pas lu et le critère d'adoption échouera [HY].

**F5. Le plafond économique est bas.** Pour un besoin stable d'environ 6 à 8 JP par mois, un coordinateur salarié coûte moins cher à GianLuca que Marwin [ES] (`travaux/strategie-retenue.md:378`). Le scénario central vend déjà 8,9 JP et 8 000 € HT par mois en régime (`modele-financier/scenarios.md:135-142`). Le succès rapproche donc Marwin du point où un client rationnel embauche (05-proposition-de-valeur.md, section 4.4). L'ambition de piloter tout le portefeuille ne tient économiquement que si une journée de Marwin vaut nettement plus qu'une journée de salarié, soit un gain mesuré d'au moins 1,5 à 2 sur les processus pilotés. C'est une cible à 12 mois [HY] (`travaux/syn-capacite-ia.md:811`), pas un acquis.

**F6. Tout ce que l'on sait du client passe par une seule personne.** Les besoins sont des propos de Morgan reformulés par un assistant IA (`travaux/syn-portefeuille.md:127-136`). La note de contexte le dit : « je n'ai fait aucune recherche sur ces personnes » (`interne/contexte-projet-carlone.md:29`). GianLuca y est appelé « plus gros client de Morgan et Mathys » (`interne/contexte-projet-carlone.md:5`), alors qu'aucune facture n'existe [FV négatif] (`travaux/strategie-retenue.md:33`). L'audit entier raisonne sur une hypothèse de demande [HY]. Il faut le savoir avant d'investir.

---

## 3. Raisons d'échec : vue d'ensemble

Les dix premières raisons viennent de la demande (`travaux/DEMANDE.md`, § 16). Les sept suivantes sont ajoutées ici. La colonne « couverture » juge la stratégie retenue.

| N° | Raison d'échec | Probabilité [HY] | Gravité | Couverture par la stratégie retenue |
| --- | --- | --- | --- | --- |
| R1 | Le pilotage global n'est pas le besoin prioritaire | Élevée | Forte | Partielle (écart n° 3) |
| R2 | GianLuca veut déléguer sans fournir moyens ni accès | Moyenne à élevée | Forte | Bonne ; une clause à ajouter |
| R3 | Les deux associés deviennent le point de blocage | Élevée s'il confie plusieurs projets ; moyenne sinon | Forte | Bonne |
| R4 | Le budget finance des outils, pas le travail | Moyenne | Moyenne | Bonne |
| R5 | La recherche absorbe la marge | Élevée | Forte | Partielle (écart n° 1) |
| R6 | Les équipes n'adoptent pas | Moyenne à élevée | Forte | Partielle |
| R7 | Les responsabilités dépassent les pouvoirs | Moyenne | Forte | Bonne |
| R8 | Dépendance excessive à une personne | Élevée (certaine au départ) | Forte | Partielle |
| R9 | Les prix ne couvrent pas la maintenance | Moyenne | Moyenne | Partielle |
| R10 | Promesse trop large pour être réceptionnée | Faible si la stratégie est appliquée ; élevée sinon | Forte | Bonne |
| R11 | Aucune société ne paie : le statu quo dure | Moyenne à élevée | Critique | Bonne |
| R12 | Les suites de la fuite de données interdisent la relation | Moyenne | Critique | Bonne |
| R13 | Le revenu est trop faible pour les associés | Élevée | Forte | Partielle (une correction de fait) |
| R14 | Le salariat devient plus attractif que Marwin | Moyenne | Forte pour Marwin | Partielle (écart n° 2) |
| R15 | Le retrait de Medhi est mal géré | Moyenne | Moyenne à forte | Bonne sur le papier, non exécutée |
| R16 | Mathys ne suit pas, ou les associés se divisent | Moyenne [IN] | Critique | Bonne |
| R17 | Le lien est requalifié en salariat déguisé | Faible à moyenne | Critique | Bonne |

**Lecture.** Les raisons les plus probables et les plus graves sont R11, R1, R13 et R5. Elles ont une cause commune : l'écart entre ce que les associés produisent et ce qu'ils vendent (`travaux/syn-capacite-ia.md:784`). C'est là que la vigilance doit porter, plus que sur le juridique, déjà bien traité.

---

## 4. Raisons d'échec : fiches

### R1. Le pilotage global n'est pas le besoin prioritaire

| Rubrique | Contenu |
| --- | --- |
| **Constat** | Les « vingt jours par mois » sont attribués à GianLuca dans une page (`sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:65`) et à Morgan dans l'autre, issue du même brief (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:7`) [FV pour les textes ; DR pour le fond]. Cette même ligne 7 indique que l'offre a remplacé une version « limitée à quatre jours mensuels », sans demande tracée. Les besoins rapportés portent sur des projets : vendre des œuvres aux entreprises de la Nièvre, une galerie, un cabaret, réunir des artistes [DR] (`sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:13-16`). Les déclencheurs visibles de l'offre sont du côté de Marwin : « faut quand même qu'il me paye ce monsieur », « une DGX Spark déjà en matériel ça serait sympa » [DR] (`interne/recueil-sessions-chatgpt-2026-11-04.txt:220`). Aucun lieu ni aucune entité à piloter n'est identifié [FV négatif] (`travaux/syn-portefeuille.md:171`) |
| **Probabilité** | Élevée [HY] |
| **Signe avant-coureur** | Au rendez-vous, il ne parle que d'un sujet ; il ne cite pas trois priorités ; il demande « combien pour le CRM » ou « pour vendre » ; il ne nomme pas de délégué |
| **Preuve qui lève l'objection** | Trois priorités signées qui touchent au moins deux projets ou lieux distincts ; un délégué nommé ; une demande écrite de suivi récurrent après le cadrage |
| **Ce que prévoit la stratégie** | Cadrage comme test ; trois voies au choix après le cadrage ; réduction à un lot si un seul projet est confié (`travaux/strategie-retenue.md:241-251, 693`) |
| **Ce qui manque** | Le cadrage est lui-même une offre de « vue d'ensemble ». Si le besoin porte sur un seul projet, c'est la mauvaise porte d'entrée (F1). Voir l'écart n° 3 |

### R2. GianLuca veut déléguer sans fournir moyens ni accès

| Rubrique | Contenu |
| --- | --- |
| **Constat** | Aucun accès fourni n'est documenté : ni comptabilité, ni contrats, ni agenda [FV négatif] (`travaux/syn-portefeuille.md:207`). La « structure qui vend les œuvres » est laissée « à compléter » dans le CRM (`travaux/syn-portefeuille.md:264`). Le seul donneur d'ordre nommé dans le CRM est Mathys [DR] (`travaux/syn-portefeuille.md:284`). Tout ce qui a été produit l'a été sans rien recevoir du client |
| **Probabilité** | Moyenne à élevée [HY] |
| **Signe avant-coureur** | Pièces du cadrage non remises 10 jours ouvrés après l'acompte ; « passez par moi » au lieu d'un délégué ; demande de travailler sur les comptes personnels de Morgan |
| **Preuve qui lève l'objection** | Accès réels remis sous 10 jours ouvrés ; comptes ouverts au nom de son entité ; délégué nommé (`travaux/strategie-retenue.md:668`) |
| **Ce que prévoit la stratégie** | Suspension si les accès manquent 10 jours ouvrés après le démarrage (`travaux/strategie-retenue.md:676`) |
| **Ce qui manque** | [PR, ce livrable] Écrire au bon de commande du cadrage que, faute de pièces sous 10 jours ouvrés, le dossier est remis sur la base des seuls entretiens, avec la liste des manques, et que le solde reste dû selon la règle de réception. Sans cette clause, un cadrage privé de pièces reste ouvert et son solde n'est jamais exigible. À traduire dans 12-gouvernance-contrat-sortie.md |

### R3. Les deux associés deviennent le point de blocage

| Rubrique | Contenu |
| --- | --- |
| **Constat** | Morgan valide tout livrable et détient la relation, les prix et les comptes (`travaux/syn-capacite-ia.md:73`). Il mène une dizaine d'autres projets (`travaux/note-point-4-novembre-et-activites.md:13-17`). La disponibilité de Mathys est inconnue [IN] (`travaux/syn-capacite-ia.md:118`). Capacité facturable : 7 à 12 JP par mois [ES] (`travaux/syn-capacite-ia.md:69`). Un projet actif coûte 3,5 à 4,5 JP par mois, d'où deux projets actifs au plus en central [ES] (`travaux/syn-capacite-ia.md:248, 253`) |
| **Probabilité** | Élevée si GianLuca confie plusieurs projets ; moyenne sinon [HY] |
| **Signe avant-coureur** | File de validation interne au-delà de 2 jours ouvrés ; une décision du client attend un document de Marwin ; un comité déplacé pour un tournage ou un autre client |
| **Preuve qui lève l'objection** | Trois mois de suite : occupation de chaque associé ≤ 85 % sur tout son temps, file de validation ≤ 2 jours ouvrés, aucun retard de plus de 5 jours ouvrés (`travaux/strategie-retenue.md:623` ; `travaux/strat-S3-contradicteur.md:539`) |
| **Ce que prévoit la stratégie** | Plafond de 10 JP facturables, limite d'encours, validation technique déléguée à Mathys, refus de tout nouveau projet au-delà de 95 % d'occupation (`travaux/strategie-retenue.md:283, 619, 623`) |
| **Ce qui manque** | Le plafond peut faire de Marwin le goulet des projets de GianLuca eux-mêmes, par exemple si la galerie accélère. [PR, ce livrable] Le dire dès la restitution du cadrage, avec la suite prévue au-delà (outillage et passation, ou recrutement) ; sinon le plafond sera vécu comme un manque de disponibilité [HY] |

### R4. Le budget finance des outils, pas le travail

| Rubrique | Contenu |
| --- | --- |
| **Constat** | Souhait d'une DGX Spark et mention de bureaux « pour du personnel » [DR] (`interne/recueil-sessions-chatgpt-2026-11-04.txt:220`). Option laboratoire de 30 000 € HT dont 13 500 € d'honoraires, le reste en achats « faits et possédés par l'entité » du client [FV pour le texte] (`interne/offre-marwin-tech-remuneration-et-collaboration.md:21`). Offre de « bureaux, une bonne rémunération », sans montant [DR] (`interne/contexte-projet-carlone.md:24`) |
| **Probabilité** | Moyenne [HY] |
| **Signe avant-coureur** | GianLuca s'intéresse au matériel, à la robotique, aux écrans plus qu'aux livrables ; il propose de « fournir l'équipement » ou les bureaux à la place des honoraires ; il demande si les achats sont déductibles |
| **Preuve qui lève l'objection** | Honoraires payés au bon de commande ; achats au nom de son entité et payés par elle, après un usage démontré |
| **Ce que prévoit la stratégie** | Laboratoire retiré ; outils au nom du client et payés par lui ; refus d'être payé en bureaux, en emploi ou en capital (`travaux/strategie-retenue.md:188-189, 645, 703`) |
| **Ce qui manque** | Rien d'essentiel. La tentation vient aussi de Marwin (la DGX Spark). Le risque est dans le discours : ne jamais présenter un achat de matériel comme une étape du projet |

### R5. La recherche absorbe la marge

| Rubrique | Contenu |
| --- | --- |
| **Constat** | Dépôt BOJART : 933 fichiers et 973 fonctions de test produits du 30 octobre au 2 novembre, sans installation sur le vrai poste [FV] (`travaux/syn-capacite-ia.md:780`). Deux artefacts « vernissage Strates » pour GianLuca datés du 4 novembre, le jour même de la décision de retrait de Medhi (`travaux/note-point-4-novembre-et-activites.md:13, 25`). Sept artefacts du film « Shelby » les 3 et 4 novembre (`travaux/note-point-4-novembre-et-activites.md:15`). La stratégie prévoit encore des démonstrateurs internes non payés avant le 2 février 2027 (`travaux/strategie-retenue.md:169`), plafonnés à 8 JP (08-feuille-de-route.md, section 3.5) |
| **Probabilité** | Élevée, par habitude [HY] ; c'était déjà l'estimation de la stratégie concurrente « pilotage » (`travaux/strat-S2-pilotage.md:579`) |
| **Signe avant-coureur** | Nouveaux documents « pour Carlone » sans bon de commande ; démonstrateurs au-delà du plafond ; relevé mensuel du temps absent ou partiel |
| **Preuve qui lève l'objection** | Deux relevés mensuels de suite, sur tout le temps de chaque associé : 0 JP de production non commandée, au plus 10 % de temps exploratoire non financé |
| **Ce que prévoit la stratégie** | STRATES, laboratoire et vernissage robotisé gelés (`travaux/strategie-retenue.md:644-646`) ; arrêt immédiat de la production non commandée (`travaux/strategie-retenue.md:716`) |
| **Ce qui manque** | Elle garde des démonstrateurs payés par Marwin avant toute vente. C'est précisément l'habitude à casser. Voir l'écart n° 1 |

### R6. Les équipes n'adoptent pas

| Rubrique | Contenu |
| --- | --- |
| **Constat** | Les seules personnes citées côté client sont GianLuca, « un associé » qui rachète deux établissements, des « responsables » et un « comptable » supposés, et les opératrices de Quali Contact [DR/HY] (`travaux/syn-portefeuille.md:211-216`). Son canal de travail est inconnu [IN] (`travaux/juge-J1-client.md:190`). On ignore même s'il a une équipe |
| **Probabilité** | Moyenne à élevée [HY] |
| **Signe avant-coureur** | Aucun délégué nommé au cadrage ; comptes rendus non commentés après deux semaines ; réponses par téléphone, hors registre |
| **Preuve qui lève l'objection** | Critères du pilote tenus quatre semaines de suite : registre consulté chaque semaine, au moins 80 % des comptes rendus commentés sous 3 jours ouvrés (`travaux/strategie-retenue.md:279`), mesurés dans le canal qu'il utilise déjà |
| **Ce que prévoit la stratégie** | Abandon du processus si les critères ne tiennent pas quatre semaines (`travaux/strategie-retenue.md:281`) ; offre d'outillage et de passation à une personne qu'il désigne (`travaux/strategie-retenue.md:321-337`) |
| **Ce qui manque** | Si GianLuca n'a pas d'équipe, « l'adoption par les équipes » n'a pas d'objet. [PR, ce livrable] Le pilote vise alors un décideur seul (une page par semaine, un appel court, une décision consignée) ou bascule vers l'outillage et passation avec un recrutement |

### R7. Les responsabilités dépassent les pouvoirs

| Rubrique | Contenu |
| --- | --- |
| **Constat** | Attente rapportée : « déléguer le quotidien » (`sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:65`), « sans avoir à en gérer chaque détail » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:13`) [DR]. Pouvoirs prévus : mandat de dépense à 0 € pendant le cadrage et le pilote, aucune exécution réglementée, coordination sans commandement direct (`travaux/strategie-retenue.md:187, 261, 589`) |
| **Probabilité** | Moyenne [HY] |
| **Signe avant-coureur** | GianLuca impute à Marwin un retard d'ouverture ou une vente manquée ; demandes de signer, payer ou appeler une administration ; consignes données en direct aux salariés d'un prestataire |
| **Preuve qui lève l'objection** | Mandat écrit par entité ; clause de limitation de responsabilité signée (`travaux/strategie-retenue.md:557`) ; RC professionnelle souscrite, incident déclaré (`travaux/strategie-retenue.md:554`) ; indicateurs « dépend de GianLuca » suivis à part et acceptés par lui (`travaux/strategie-retenue.md:159`) |
| **Ce que prévoit la stratégie** | Bonne couverture (sections 7 et 8 de la stratégie ; 12-gouvernance-contrat-sortie.md) |
| **Ce qui manque** | Le risque est surtout oral. [PR, ce livrable] Règle de langage pour les deux associés : remplacer toute promesse « on s'en occupe » par « on prépare, vous décidez, votre société signe » |

### R8. Dépendance excessive à une personne

| Rubrique | Contenu |
| --- | --- |
| **Constat** | GianLuca fait 100 % du chiffre d'affaires en central [ES] (`modele-financier/scenarios.md:44`). Il est présenté à la fois comme client, bailleur, employeur, investisseur et financeur de recherche [DR] (`travaux/syn-portefeuille.md:310-316`). La part maximale de revenus venant de lui est restée sans réponse : « 10 millions » (`interne/contexte-projet-carlone.md:129`). Côté Marwin, Morgan est le point unique de défaillance, Mathys pour le code du CRM (`travaux/syn-capacite-ia.md:73`) |
| **Probabilité** | Élevée ; certaine au démarrage |
| **Signe avant-coureur** | Aucune proposition à un autre client au mois 4 ; prospection sous 50 % du plancher deux mois de suite (`travaux/strategie-retenue.md:678`) ; accès critiques sur un seul compte personnel |
| **Preuve qui lève l'objection** | Un second client payant, ou au moins une proposition envoyée au mois 6 ; un test d'absence où l'autre associé tient seul le socle deux semaines ; un coffre d'accès partagé |
| **Ce que prévoit la stratégie** | Dépendance à 100 % assumée par écrit, variante chiffrée avec un second client (`travaux/strategie-retenue.md:116, 522`) |
| **Ce qui manque** | Le second client dépend de la même compétence non démontrée (F3). L'hypothèse réaliste est que Marwin reste le prestataire d'un seul client pendant 12 à 18 mois [HY]. Conséquence : ne réduire aucune source de revenu avant trois échéances de socle payées, ce que la stratégie dit déjà pour le second client (`travaux/strategie-retenue.md:771`) |

### R9. Les prix ne couvrent pas la maintenance

| Rubrique | Contenu |
| --- | --- |
| **Constat** | CRM « offert à ce jour » (`interne/offre-marwin-tech-remuneration-et-collaboration.md:227`) ; sa mise en conformité n'est pas facturée (`travaux/strategie-retenue.md:215`). Un outil construit dans un lot n'est maintenu contre paiement que si une exploitation le prévoit, au plus tôt au mois 7 ; les corrections sont gratuites 60 jours (`travaux/strategie-retenue.md:339, 384`). Marge du socle B1 : −8 à +29 % à 10 JP [ES] (`travaux/strategie-retenue.md:278`) |
| **Probabilité** | Moyenne [HY] |
| **Signe avant-coureur** | Demandes de « petites corrections » après 60 jours ; temps de support non imputé dans le relevé ; CRM qui reste en service sans contrat d'hébergement |
| **Preuve qui lève l'objection** | Chaque outil livré a un régime écrit : compris dans le socle, exploitation payée, ou « aucune maintenance, sauf avenant » ; support mesuré à 0,5 JP au plus par mois et par processus (`travaux/strategie-retenue.md:349`) |
| **Ce que prévoit la stratégie** | Partiellement : règle anti-double facturation et offre d'exploitation (`travaux/strategie-retenue.md:339-349, 380-391`) |
| **Ce qui manque** | [PR, ce livrable] Une ligne « maintenance après 60 jours » dans chaque bon de commande de lot. Une décision écrite, avant le rendez-vous, sur qui héberge et maintient le CRM ; à défaut, remise du CRM sans maintenance |

### R10. Promesse trop large pour être réceptionnée

| Rubrique | Contenu |
| --- | --- |
| **Constat** | En deux semaines, le périmètre est passé de huit missions de gestion au CRM, à STRATES, au vernissage et au laboratoire, sans décision tracée (`travaux/syn-portefeuille.md:170`). Le diaporama promettait encore « Six mois pour […] vendre vos œuvres avec le CRM » (`travaux/strategie-retenue.md:820`) |
| **Probabilité** | Faible si les documents sont corrigés et la règle « une commande, des critères écrits » tenue ; élevée si le discours oral reprend l'ambition [HY] |
| **Signe avant-coureur** | Un sujet nouveau accepté en réunion sans bon de commande ; un ancien document qui revient ; un livrable démarré sans critères écrits |
| **Preuve qui lève l'objection** | Toutes les commandes ont des critères écrits avant le travail ; au moins 75 à 80 % des livrables acceptés au premier passage |
| **Ce que prévoit la stratégie** | Bonne couverture : pas d'abonnement général, un bon de commande par prestation, liste des corrections du diaporama (`travaux/strategie-retenue.md:184-190, 814-828`) |
| **Ce qui manque** | Ne pas parler à GianLuca de « piloter tout le portefeuille » avant le bilan du mois 6. C'est la cible interne, pas une promesse |

### R11. Aucune société ne paie : le statu quo dure

| Rubrique | Contenu |
| --- | --- |
| **Constat** | Aucun contrat, aucune facture, aucune entité payeuse [FV négatif] (`travaux/strategie-retenue.md:33`). Aucun rendez-vous à l'agenda jusqu'au 6 novembre [DR] (`travaux/note-point-4-novembre-et-activites.md:5`). Travail gratuit depuis le 18 octobre : CRM, dossier de 34 pages, catalogue, STRATES, vernissage (`travaux/syn-portefeuille.md:304`). Un patrimoine déclaré ne prouve pas une trésorerie (`travaux/DEMANDE.md`, § 3) |
| **Probabilité** | Moyenne à élevée [HY]. Un client qui reçoit gratuitement n'a pas de raison pressante de payer |
| **Signe avant-coureur** | Pas de date de rendez-vous une semaine après l'envoi du message ; au rendez-vous, la société est « à voir » ; « commencez, on verra pour le papier » |
| **Preuve qui lève l'objection** | Société nommée (dénomination, SIREN, signataire), statut actif vérifié sur les registres publics, bon de commande signé, acompte encaissé (`travaux/strategie-retenue.md:665, 667`) |
| **Ce que prévoit la stratégie** | Report sans production au 15 décembre et au 31 janvier (`travaux/strategie-retenue.md:697-698`) |
| **Ce qui manque** | Ces dates arrêtent la production pour le client, pas la préparation interne (statuts et pacte payés, démonstrateurs). Voir l'écart n° 1 |

### R12. Les suites de la fuite de données interdisent la relation

| Rubrique | Contenu |
| --- | --- |
| **Constat** | Le dépôt FinanceScope/CRM-Carlone était public au 4 novembre à 16 h 19 [DR] (`interne/contexte-projet-carlone.md:5`). L'analyse du 2 novembre y comptait 931 numéros de téléphone, 206 adresses e-mail et 63 fichiers de profils LinkedIn (`interne/contexte-projet-carlone.md:11`). Le problème était connu au plus tard le 2 novembre [FV] (`interne/audit-marwin-tech-carlone.md:3, 15`). Le délai de 72 h pour notifier la CNIL expire le 5 novembre, à une heure inconnue [ES] (`travaux/strategie-retenue.md:32`). Le responsable du traitement n'est pas désigné [IN]. Une assurance souscrite après coup ne couvrira probablement pas l'incident [HY] (`travaux/juge-J2-marwin.md:154`) |
| **Probabilité** | Moyenne que les suites pèsent sur la relation [HY] ; gravité critique |
| **Signe avant-coureur** | Décision non documentée le 5 novembre ; dépôt encore public ou copié ; GianLuca l'apprend par un tiers ; avis du conseil qui impose d'informer les personnes, dont ses futurs prospects (`travaux/juge-J2-marwin.md:156`) |
| **Preuve qui lève l'objection** | Décision datée et motivée avec un avocat ou un DPD ; visibilité « privé » vérifiée ; avis écrit sur l'information des personnes ; GianLuca informé par écrit et d'accord pour poursuivre ; assureur informé |
| **Ce que prévoit la stratégie** | Bonne couverture : condition de validité V1, décision n° 1 (`travaux/strategie-retenue.md:53, 715`) |
| **Ce qui manque** | Si l'information des personnes est due, la voie « ventes d'œuvres » devient fragile pour longtemps : mêmes entreprises, même territoire [HY]. Seules les voies « pilotage » et « organisation interne » restent alors ouvertes au démarrage |

### R13. Le revenu est trop faible pour les associés

| Rubrique | Contenu |
| --- | --- |
| **Constat** | En central, 1 100 à 1 500 € nets par associé et par mois à partir du mois 4, avant impôt sur le revenu [ES] (`modele-financier/scenarios.md:67`) ; rien de novembre 2026 à mars 2027 (`modele-financier/scenarios.md:129-133`). Environ 130 € nets par journée consacrée à Marwin [ES] (09-modele-economique-tresorerie.md, section 7.3). L'objectif de 7 500 € nets chacun (`interne/offre-marwin-tech-remuneration-et-collaboration.md:118`) est hors d'atteinte. L'apport demandé est de 8 000 à 14 000 € (`travaux/strategie-retenue.md:56`), alors qu'une domiciliation attend 144 € depuis le 12 octobre et que des abonnements échouent depuis fin octobre [DR] (`travaux/note-point-4-novembre-et-activites.md:6, 8`) |
| **Probabilité** | Élevée ; c'est aussi l'estimation de la stratégie (`travaux/strategie-retenue.md:771`) |
| **Signe avant-coureur** | Apport non réuni au moment d'immatriculer ; un associé reprend un emploi ou relance OLSEN à plein temps ; tension sur le partage des tâches |
| **Preuve qui lève l'objection** | Décision écrite des deux sur la rémunération acceptée ; apport déposé ; plan de revenus extérieurs couvrant au moins six mois |
| **Ce que prévoit la stratégie** | Revenus extérieurs maintenus, scénario prudent assumé (`travaux/strategie-retenue.md:771`) |
| **Ce qui manque** | **Correction de fait.** La question n° 10 demande aux associés s'ils peuvent vivre « trois à quatre mois sans rémunération de Marwin » (`travaux/strategie-retenue.md:737`). Le modèle en montre **cinq** en central (novembre à mars) et **six** en prudent (novembre à avril) (`modele-financier/scenarios.md:102-108, 129-134`). C'est ce chiffre qu'il faut poser |

### R14. Le salariat devient plus attractif que Marwin

| Rubrique | Contenu |
| --- | --- |
| **Constat** | Un poste de cadre chez GianLuca rapporterait ≈ 3 400 € nets pour 6 149 € de coût employeur ; c'est un résultat de simulateur, à lire comme une estimation (`travaux/ver-R6-marche.md:25` ; `travaux/controle-modele.md:95`). GianLuca propose « une bonne rémunération » [DR] (`interne/contexte-projet-carlone.md:24`) ; la question « Veut-il salarier l'un de vous ? » reste ouverte (`interne/contexte-projet-carlone.md:109`). Morgan a écrit : « Je préfère être prestataire ou salarié » [DR] (`interne/recueil-sessions-chatgpt-2026-11-04.txt:248`). Sur douze mois, ≈ 40 000 € nets de salaire, contre ≈ 10 000 à 13 500 € nets de Marwin en central (neuf mois payés à 1 100 à 1 500 €) [ES, ce livrable]. La comparaison n'est pas tout à fait égale : le salaire suppose un plein temps, alors que Marwin, en central, n'occupe que 50 à 65 % du temps des associés (`travaux/strategie-retenue.md:495`) ; mais rien ne prouve que le temps restant soit payé ailleurs [IN] |
| **Probabilité** | Moyenne qu'il le propose [HY]. S'il le propose, l'emploi est financièrement meilleur pour l'associé concerné la première année [ES] |
| **Signe avant-coureur** | GianLuca parle de poste, d'horaires, de bureaux à Cosne-Cours-sur-Loire ; un associé hésite à déposer l'apport ; l'idée d'un associé « salarié et prestataire » revient |
| **Preuve qui lève l'objection** | Les associés écrivent pourquoi ils préfèrent l'indépendance (autres clients, actif propre, liberté) et à partir de quel revenu ils y renoncent ; ou GianLuca ne propose aucun emploi |
| **Ce que prévoit la stratégie** | Pas de discussion avant le bilan du mois 6 ; jamais un emploi combiné avec une prestation de Marwin sur les mêmes sujets (`travaux/strategie-retenue.md:631, 704, 707`) |
| **Ce qui manque** | Attendre six mois ne supprime pas le choix : cela fait attendre GianLuca, qui peut recruter quelqu'un d'autre. Voir l'écart n° 2 |

### R15. Le retrait de Medhi est mal géré

| Rubrique | Contenu |
| --- | --- |
| **Constat** | Le retrait a été demandé oralement le 4 novembre, sans formalisation avec Mathys ni avec Medhi [DR] (`travaux/note-point-4-novembre-et-activites.md:25`). Medhi était « plus que partant » [DR] (`interne/contexte-projet-carlone.md:27`). GianLuca a racheté « l'ancienne affaire de Medhi » et connaît BOJ.ART [DR] (`interne/contexte-projet-carlone.md:24`). Morgan veut ouvrir la boutique BOJ.ART avec lui (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:21`). L'offre écrite attribuait à Medhi l'atelier, le parc d'impression et Jarvis, et promettait à la galerie une exclusivité de vente et les films de fabrication [FV pour le texte] (`interne/offre-marwin-tech-remuneration-et-collaboration.md:90, 94`) |
| **Probabilité** | Moyenne [HY] |
| **Signe avant-coureur** | Pas de message écrit à Medhi au 19 novembre ; GianLuca ou Medhi évoquent STRATES ; question sur Jarvis ou sur le parc d'impression ; Morgan continue de produire pour BOJ.ART sur les jours engagés pour Marwin |
| **Preuve qui lève l'objection** | Décision écrite des deux associés ; message à Medhi envoyé et accusé ; liste de ce qui lui avait été dit ; déclaration écrite du lien de Morgan avec BOJ.ART remise à GianLuca (`travaux/strategie-retenue.md:635`) |
| **Ce que prévoit la stratégie** | Bonne couverture sur le papier : hors offre, contrat direct entre Medhi et la société de GianLuca, sans Marwin (`travaux/strategie-retenue.md:643`). Rien n'est encore exécuté [FV négatif au 4 novembre] |
| **Ce qui manque** | Si GianLuca voulait d'abord l'œuvre, le retrait lui enlève peut-être ce qui l'intéressait le plus [HY]. Ne pas le découvrir au rendez-vous : obtenir avant la réponse de Morgan sur ce que GianLuca a dit de STRATES (`travaux/strategie-retenue.md:736`) |

### R16. Mathys ne suit pas, ou les associés se divisent

| Rubrique | Contenu |
| --- | --- |
| **Constat** | Compétences et disponibilité de Mathys inconnues [IN] (`travaux/syn-capacite-ia.md:68, 118`) ; « Temps de Mathys non fixé » (`interne/audit-marwin-tech-carlone.md:62`). Mathys est le titulaire présumé du dépôt exposé (`travaux/strategie-retenue.md:173`). La décision sur Medhi a été prise par Morgan seul (`travaux/note-point-4-novembre-et-activites.md:25`) |
| **Probabilité** | Moyenne [IN] |
| **Signe avant-coureur** | Fiche « rôles et disponibilités » non signée au 19 novembre ; désaccord sur qui répond de la fuite ; Mathys absent de la préparation du rendez-vous |
| **Preuve qui lève l'objection** | Fiche signée ; pacte signé ; Mathys qui tient seul un point client |
| **Ce que prévoit la stratégie** | Bonne couverture : conditions V2 et V3 ; rien n'est proposé au client tant que le désaccord dure (`travaux/strategie-retenue.md:54-55, 614`) |
| **Ce qui manque** | [PR, ce livrable] Régler entre associés, avant le pacte et sans chercher de coupable, qui a fait quoi sur le dépôt et qui paie le conseil sur la fuite |

### R17. Le lien est requalifié en salariat déguisé

| Rubrique | Contenu |
| --- | --- |
| **Constat** | Client unique, bureaux du client, prix au temps et « s'occuper de tout » sont des indices de requalification (`travaux/juge-J2-marwin.md:111` ; 10-structures-et-relations.md, section 7). Le risque monte si un associé devient salarié de GianLuca tout en facturant via Marwin (10-structures-et-relations.md, section 6) |
| **Probabilité** | Faible à moyenne (`travaux/strategie-retenue.md:777`) |
| **Signe avant-coureur** | Horaires imposés, ordres directs, place dans un organigramme, exclusivité de fait (`travaux/strategie-retenue.md:683`) |
| **Preuve qui lève l'objection** | Livrables au forfait ; méthodes et horaires choisis par Marwin ; autres clients réels |
| **Ce que prévoit la stratégie** | Bonne couverture : pas de bureaux avant le mois 6, prix au livrable (`travaux/strategie-retenue.md:777`) |
| **Ce qui manque** | Rien |

---

## 5. Comparaison avec quatre autres voies

### 5.1 Les voies comparées

| N° | Voie | Contenu |
| --- | --- | --- |
| 1 | **Stratégie retenue** | Remise en ordre ; cadrage à 6 500 € HT ; pilote de huit semaines dans une voie choisie par GianLuca ; socle borné au plus tôt au mois 4 ; plafond de 10 JP facturables ; central avec Morgan à 65 % et Mathys à 50 % (`travaux/strategie-retenue.md:41-45, 495`) |
| 2 | **Démarrage progressif à engagement minimal** | Même séquence. Mais avant un rendez-vous tenu et une société nommée, rien d'autre que l'obligatoire ; temps engagé commande par commande ; aucune source de revenu abandonnée avant trois échéances de socle payées ; porte d'entrée possible par un lot [PR, ce livrable] |
| 3 | **Collaboration plus limitée** | Un ou deux lots au forfait choisis par GianLuca (catalogue privé, pilote commercial, outillage et passation), sans socle ni ambition de pilotage ; Marwin reste un fournisseur parmi d'autres |
| 4a | **Équipe salariée : GianLuca recrute** | Il embauche un assistant ou un coordinateur ; Marwin au plus outille et forme la personne (offre C6) |
| 4b | **Équipe salariée : un associé est salarié** | Morgan ou Mathys devient salarié de GianLuca ; Marwin ne lui facture rien sur les mêmes sujets et sert d'autres clients, ou s'arrête |
| 5 | **Plusieurs prestataires spécialisés** | GianLuca contracte directement avec Quali Contact, son expert-comptable, son avocat, un organisateur d'événements, un photographe ; personne ne pilote ; Marwin au plus pour les données |

La stratégie retenue est déjà progressive. La voie 2 va plus loin : elle retarde tout investissement qui n'est pas exigé par la loi ou payé par le client.

### 5.2 Tableau par critère

Notes qualitatives (fort, moyen, faible) : une note chiffrée serait une précision artificielle. Montants [ES] sauf mention.

| Critère | 1. Stratégie retenue | 2. Progressif, engagement minimal | 3. Lot unique | 4a. GianLuca recrute | 4b. Un associé salarié | 5. Prestataires spécialisés |
| --- | --- | --- | --- | --- | --- | --- |
| Répond au besoin le mieux documenté [DR] (vendre des œuvres ; « ne pas gérer chaque détail ») | Moyen : passe d'abord par un inventaire | Moyen à fort : idem, ou entrée directe par un lot | Fort si sa priorité est unique ; faible pour « ne pas gérer chaque détail » | Fort pour l'exécution quotidienne ; moyen pour la coordination | Fort s'il veut une personne présente [HY] | Fort pour les ventes ; faible pour la coordination |
| Valeur vérifiable pour lui à 6 mois | Moyenne : preuve vers le mois 3 ou 4 | Moyenne, un peu plus lente | Forte : livrable réceptionné en 4 à 8 semaines | Moyenne : délai de recrutement [IN] | Moyenne : une personne, sans contrôle à quatre yeux | Moyenne : chacun livre, personne ne relie |
| Coût pour son entité | 6 500 € HT, puis ≈ 8 000 € HT par mois en régime central (`modele-financier/scenarios.md:135-142`) | Idem au départ | 3 500 à 7 500 € HT par lot (`travaux/strategie-retenue.md:291-296`) | Assistant 2 249 à 2 808 € par mois ; cadre 5 380 à 6 149 € (`travaux/ver-R6-marche.md:25`) ; + 7 500 € HT d'outillage éventuel | ≈ 6 149 € par mois pour un cadre | Prospection 3 000 à 8 000 € par mois ou 150 à 500 € par rendez-vous [DR] (05-proposition-de-valeur.md, section 4.1) |
| Revenu des associés sur 12 mois | Faible : 1 100 à 1 500 € nets chacun à partir du mois 4 (`modele-financier/scenarios.md:67`) | Faible pour Marwin, mais revenus extérieurs gardés : total plus sûr | Faible : complément ponctuel | Nul, sauf l'outillage | Fort pour le salarié (≈ 3 400 € nets) ; nul pour Marwin | Nul ou faible |
| Charge soutenable à deux | Moyenne : suppose 65 % et 50 % de disponibilité [IN] | Bonne : temps engagé commande par commande | Bonne | Sans objet | Bonne pour la personne | Bonne |
| Focalisation des associés | Bonne si Morgan réduit ses autres projets (non acquis) | Faible : autres projets gardés ; compensée par une règle de priorité écrite | Sans enjeu | Sans enjeu | Forte, au service d'un seul employeur | Sans enjeu |
| Risque juridique pour Marwin et ses associés | Faible (bien encadré) | Faible | Faible ; le pilote commercial touche aux données exposées | Faible | Élevé si combiné avec Marwin (requalification, loyauté, logiciels à l'employeur) ; faible sinon (10-structures-et-relations.md, section 6) | Faible |
| Dépendance à une seule personne | Élevée : 100 % du chiffre d'affaires (`modele-financier/scenarios.md:44`) | Élevée pour Marwin, moindre pour les associés | Faible pour les associés | Nulle pour Marwin | Très élevée : revenu, poste, peut-être bureaux et capital | Faible |
| Réversibilité | Bonne : préavis, comptes au nom du client, sortie à blanc | Bonne | Très bonne | Moyenne pour lui (contrat de travail) | Faible : logiciels créés à l'employeur (art. L113-9 CPI, cité par 10-structures-et-relations.md, section 6) | Bonne |
| Ce que Marwin construit | Moyen : références, méthode | Moyen à faible | Faible : une référence | Faible, sauf la référence « outillage et passation » | Rien | Faible |
| Travail et dépense avant le premier euro | 12 à 25 JP ; 5 000 à 7 000 € HT de démarrage | Réduits à la fuite, aux documents et aux décisions internes | Société et assurance quand même nécessaires | Faible | Nul | Faible |
| Inconnues à lever avant de commencer | Nombreuses : société, budget, Mathys, apport, fuite | Moins nombreuses | Préalables du lot | Peu pour Marwin | Intention réelle de GianLuca [DR] ; salaire [IN] | Peu |

### 5.3 Lecture

- **Aucune voie ne domine.** Les voies 1 et 2 sont les seules qui gardent à la fois une valeur pour GianLuca et un actif pour Marwin. Ce sont aussi celles qui dépendent du plus grand nombre d'inconnues.
- **La voie 2 garde l'essentiel de la voie 1 et retire les dépenses faites à l'aveugle.** Son coût : Morgan reste dispersé plus longtemps (R3, R5). D'où la règle de priorité écrite qu'elle exige (section 6.1).
- **La voie 3 est la plus sûre et la moins rémunératrice.** C'est le bon choix si GianLuca n'a qu'une priorité (R1), ou si la disponibilité écrite des associés reste sous 6 JP par mois (`travaux/strategie-retenue.md:696`).
- **La voie 4a gagne dès que le besoin est stable** au-delà de 6 à 8 JP par mois (`travaux/strategie-retenue.md:378`). Marwin doit alors la proposer elle-même, avec l'outillage et passation (`travaux/strategie-retenue.md:695`).
- **La voie 4b est le meilleur revenu pour un associé et la fin de l'indépendance de Marwin avec ce client.** C'est une décision personnelle, pas une variante de l'offre (écart n° 2).
- **La voie 5 convient si GianLuca veut garder la coordination.** Elle n'est pas concurrente : Marwin peut la préparer sous mandat, et les tiers facturent directement son entité (`travaux/strategie-retenue.md:388`).

---

## 6. Recommandation ferme

### 6.1 Énoncé [PR, ce livrable]

> **Poursuivre la collaboration avec GianLuca Carlone, mais comme un test commercial borné, pas comme le lancement d'une entreprise.**
>
> 1. **Jusqu'au rendez-vous**, ne faire que l'obligatoire : décision sur la fuite avec le conseil, documents client corrigés, décisions écrites entre associés (stratégie, Medhi, disponibilités, position sur un éventuel emploi). Aucune autre dépense, aucun démonstrateur, aucune production (écart n° 1).
> 2. **Au rendez-vous**, vendre le cadrage. S'il le refuse mais nomme une priorité concrète, proposer un lot unique avant de conclure (écart n° 3).
> 3. **Engager du temps commande par commande** (6 à 9 JP par mois pendant le cadrage et le pilote, `modele-financier/scenarios.md:130-132`). Suspendre d'abord les travaux sans revenu (créations, démonstrateurs, BOJ.ART hors contrat). **N'abandonner aucune source de revenu avant trois échéances de socle payées à l'heure.** Écrire une règle de priorité : les jours engagés pour Marwin passent avant tout autre projet.
> 4. **Examiner tout de suite une offre d'emploi**, si elle vient, comme une alternative séparée (écart n° 2).
> 5. **S'arrêter aux dates fixées**, sans les renégocier entre soi : 15 décembre 2026, 31 janvier 2027, fin du pilote, bilan du mois 6.

Cette recommandation garde le verdict, l'architecture des offres, les prix et les garde-fous de la stratégie retenue (`travaux/strategie-retenue.md:41-45`). Elle change le rythme d'engagement et trois règles.

### 6.2 Écarts avec la stratégie retenue

> **Écart avec la stratégie retenue n° 1 : avant le premier euro, ne payer et ne produire que l'obligatoire.**
>
> *Ce que dit la stratégie.* Statuts et pacte « préparés tout de suite » (`travaux/strategie-retenue.md:552`), en novembre, avec l'avocat (`travaux/strategie-retenue.md:718`), prêts à signer au 30 novembre (08-feuille-de-route.md, section 3.2). Démonstrateurs internes avant le 2 février 2027 (`travaux/strategie-retenue.md:169`), jusqu'à 8 JP (07-processus-ia-et-essais.md, section 0).
>
> *Ce que propose ce livrable.* Tant qu'aucun rendez-vous n'est tenu et qu'aucune société n'est nommée, les seules dépenses sont le conseil sur la fuite et les formalités qu'elle impose. Statuts et pacte sont rédigés à partir de modèles, sans honoraires ; l'avocat les relit dès que la société de GianLuca est nommée, sur un créneau réservé à l'avance. Les démonstrateurs se limitent au registre tenu à la main sur les réunions des associés ; aucun outil n'est développé.
>
> *Pourquoi.* L'espérance de chiffre d'affaires est faible tant que le cadrage n'est pas vendu (F2). La trésorerie personnelle est tendue (`travaux/note-point-4-novembre-et-activites.md:6, 8`). La production non commandée est l'habitude la plus coûteuse des associés (R5).
>
> *Limite.* La relecture des statuts après le rendez-vous peut retarder l'immatriculation d'une à deux semaines et rendre la date du 31 janvier plus serrée [HY]. Parade : réserver l'avocat dès novembre, sans engager d'honoraires.
>
> *Décision.* Morgan et Mathys, au 19 novembre 2026.

> **Écart avec la stratégie retenue n° 2 : une offre d'emploi s'examine tout de suite, comme une alternative, pas après six mois.**
>
> *Ce que dit la stratégie.* Le salariat « n'est pas discuté avant le bilan du mois 6 » (`travaux/strategie-retenue.md:707`) ; employeur refusé avant ce bilan (`travaux/strategie-retenue.md:631`). La réponse préparée renvoie GianLuca à « après six mois de travail ensemble » (13-preparation-rendez-vous.md, section 8.2).
>
> *Ce que propose ce livrable.* En séance, ne rien accepter et ne rien refuser : « C'est un sujet séparé ; nous vous répondrons par écrit sous trois semaines. » Dans ce délai, les associés choisissent par écrit, chiffres en main, entre trois issues : (a) décliner ; (b) un associé accepte, et Marwin ne facture plus rien à GianLuca sur les mêmes sujets ; l'autre associé poursuit Marwin avec d'autres clients ; (c) décliner et proposer l'outillage et passation pour la personne qu'il recrutera. Jamais d'emploi combiné avec une prestation de Marwin sur les mêmes sujets : cette règle de la stratégie reste entière (`travaux/strategie-retenue.md:704`). Les associés écrivent leur position de principe avant le rendez-vous.
>
> *Pourquoi.* Pour un associé, l'écart de revenu est d'environ 2 000 € nets par mois la première année (R14). Refuser sans examen peut aller contre son intérêt. Repousser à six mois ne supprime pas le choix : GianLuca peut recruter quelqu'un d'autre entre-temps [HY].
>
> *Limite.* L'option (b) met fin à l'indépendance de Marwin avec ce client et transfère à l'employeur les logiciels créés dans les fonctions salariées (10-structures-et-relations.md, section 6). Elle peut diviser les associés.
>
> *Décision.* Morgan et Mathys, avant le rendez-vous ; l'associé concerné décide pour lui-même, l'autre décide pour Marwin.

> **Écart avec la stratégie retenue n° 3 : un refus du cadrage n'est pas encore un refus de tout.**
>
> *Ce que dit la stratégie.* « Refus de payer le cadrage » : refuser la suite (`travaux/strategie-retenue.md:701`).
>
> *Ce que propose ce livrable.* Si GianLuca refuse le cadrage mais nomme une priorité concrète dont les préalables existent, proposer **un seul lot** à son prix, plancher de 750 € HT par JP estimée compris : le catalogue privé de 20 à 30 œuvres (C1) s'il fournit œuvres et photos ; l'outillage et passation (C6) s'il désigne une personne ; le pilote commercial (C2) seulement si tous ses préalables sont réunis (`travaux/strategie-retenue.md:291-296, 311`). S'il refuse tout travail payé, refuser la suite comme le prévoit la stratégie.
>
> *Pourquoi.* Le cadrage sert surtout à dimensionner l'offre de Marwin (F1). Son refus peut viser le format, pas le besoin. La stratégie admet déjà un lot sans socle quand un seul projet est confié (`travaux/strategie-retenue.md:693`). La préparation du rendez-vous l'applique déjà au refus « je veux du concret » (13-preparation-rendez-vous.md, section 8.7) : cet écart en fait une règle, pour que la phrase de la ligne 701 ne soit pas lue comme un arrêt automatique.
>
> *Limite.* Un lot sans cadrage se fait sans inventaire ni mandat : le risque de dérive du périmètre augmente (R10). Les critères de réception écrits avant le travail restent obligatoires. Un refus de payer quoi que ce soit d'avance reste un refus (même section 8.7).
>
> *Décision.* Morgan, au rendez-vous, dans les règles de 13-preparation-rendez-vous.md ; validation écrite de Mathys avant l'envoi du devis.

### 6.3 Conditions de validité

La recommandation tient si **toutes** les conditions suivantes sont réunies. Si l'une manque, la section 7 dit quoi faire.

| N° | Condition | Comment la vérifier | Au plus tard | Si elle manque |
| --- | --- | --- | --- | --- |
| CV1 | La fuite est traitée sans suite qui interdise la relation | Décision datée avec avocat ou DPD ; dépôt privé vérifié ; GianLuca informé et d'accord pour poursuivre | 5 novembre 2026 pour la décision ; avant le message pour l'information | Rien ne démarre (R12) |
| CV2 | Mathys s'engage par écrit (stratégie, Medhi, disponibilités) | Fiche « rôles et disponibilités » signée | 19 novembre 2026 | Aucune proposition au client (R16) |
| CV3 | Les associés ont des revenus extérieurs pour au moins six mois et l'argent du conseil sur la fuite et des formalités | Déclaration écrite de chacun | 19 novembre 2026 | Reporter (R13) |
| CV4 | Aucune promesse antérieure acceptée par GianLuca ne contredit ce parcours | Réponse de Morgan sur ce qu'il a vu, reçu ou accepté (`travaux/strategie-retenue.md:736`) | Avant l'envoi du message | Message de recadrage d'abord, oral puis écrit |
| CV5 | GianLuca nomme une société et paie avant le travail | Bon de commande, acompte encaissé | Société au 15 décembre 2026 ; paiement au 31 janvier 2027 | Reporter (R11) |
| CV6 | GianLuca dispose d'un canal de décision écrit ou d'un délégué | Nom du délégué ; décisions consignées pendant le cadrage | Restitution du cadrage | Pilote « décideur seul » ou outillage et passation (R6) |

**Révision vers le haut.** Si GianLuca nomme d'emblée une société, fournit les accès, paie et confie au moins deux projets réels, la voie 1 s'applique telle quelle, plafond de 10 JP compris (`travaux/strategie-retenue.md:60`).

### 6.4 Points de décision datés

| Date | Ce qui doit être vrai | Sinon |
| --- | --- | --- |
| 5 nov. 2026 | Décision sur la notification documentée ; dépôt privé vérifié | Notification en retard motivée ; rien d'autre ne démarre |
| 19 nov. 2026 | Fiche « rôles et disponibilités » signée ; décision écrite sur Medhi et message à Medhi ; position écrite sur un éventuel emploi ; écart n° 1 tranché | Pas de message à GianLuca |
| 27 nov. 2026 | Message et proposition envoyés (pour-gianluca/message-de-recadrage.md) | Signal F3 : la vente ne se fait pas ; en parler entre associés avant toute autre tâche |
| 4 déc. 2026 | Une date de rendez-vous est obtenue | Une relance, puis on attend le 15 décembre sans rien produire |
| 15 déc. 2026 | Rendez-vous tenu ; société nommée | Reporter (section 7.1) |
| 31 janv. 2027 | Cadrage ou lot payé | Reporter sans date |
| Fin du pilote (≈ fin mars 2027 en central) | Critères d'adoption tenus quatre semaines ; paiements à l'heure | Réduire aux lots, sans socle (section 7.2) |
| 4 mai 2027 (bilan du mois 6) | Bilan mesuré ; sortie à blanc réussie ; décision sur bureaux, emploi, capital, chacun séparément | Rester au lot par lot |
| Trois échéances de socle payées à l'heure (≈ juin 2027 en central, socle payé d'avance le 1er du mois) | Paiements à l'heure ; occupation de chaque associé ≤ 85 % sur tout son temps | Ne réduire aucune autre source de revenu |

---

## 7. Réduire, reporter ou refuser : les scénarios précis

### 7.1 Reporter : le scénario le plus probable aujourd'hui [HY]

**Situation.** Le message part le 27 novembre. Au 15 décembre 2026, GianLuca n'a pas fixé de date ; ou il a reçu Morgan mais renvoie la question de la société « à plus tard » ; ou il dit « commencez le catalogue, on verra pour le papier ». Variante : la décision sur la fuite n'est pas documentée, ou Mathys n'a pas signé sa fiche au 19 novembre.

**Réponse.**
- Report sans date. Aucune production, aucune immatriculation, aucune dépense hors fuite.
- Remettre à GianLuca ce qui lui revient (documents, données qui le concernent), après avis sur les rôles au regard des données personnelles (`travaux/strategie-retenue.md:701`).
- Rester joignable. Une seule relance écrite en mars 2027.
- Réaffecter le temps à des clients qui paient.

**Pourquoi reporter et non refuser.** Rien ne prouve que le besoin est absent ; seulement qu'il n'est pas solvable aujourd'hui.

### 7.2 Réduire

**Situation A.** Au rendez-vous, GianLuca nomme sa société de marchand d'art. Sa priorité est de vendre des œuvres aux entreprises, ou d'avoir un catalogue. Il ne veut ni inventaire ni suivi.
**Réponse.** Un lot unique (écart n° 3) : catalogue privé (C1) s'il fournit œuvres et photos ; pilote commercial (C2) seulement avec tous ses préalables, dont des comptes hors des fiches exposées si l'information des personnes est due (`travaux/strategie-retenue.md:311`). Pas de socle, pas de « pilotage ». Les associés n'engagent que les jours du lot.

**Situation B.** Il préfère embaucher quelqu'un.
**Réponse.** Outillage et passation (C6) pour cette personne, puis, au plus, un socle léger de pilotage (`travaux/strategie-retenue.md:695`). Marwin ne reprend jamais l'exécution (`travaux/strategie-retenue.md:337`).

**Situation C.** La disponibilité écrite des deux associés reste sous 6 JP facturables par mois.
**Réponse.** Cadrage et un lot au plus (`travaux/strategie-retenue.md:696`).

**Situation D.** À la fin du pilote, il paie à l'heure, mais le registre n'est pas lu et les critères d'adoption échouent.
**Réponse.** Pas de socle récurrent. Des lots devisés seulement, sur demande écrite.

### 7.3 Refuser

**Situation.** GianLuca répond en substance : « Je ne veux pas d'étude. Occupez-vous de tout dès maintenant : la galerie, les lieux, les artistes. Venez travailler dans mes bureaux. Je vous paierai bien quand les choses tourneront, ou je vous fais entrer au capital. » Aucune société n'est nommée. Aucun accès n'est donné.

Mêmes réponses dans ces cas :
- il exige d'appeler tout de suite les 500 fiches du CRM malgré l'incident ;
- il demande une commission sur les ventes d'œuvres, l'encaissement pour la galerie, un rôle d'exploitant ou un robot devant le public ;
- il veut qu'un associé soit salarié **et** que Marwin facture sur les mêmes sujets.

**Réponse.**
- Refuser cette forme, par écrit, en expliquant pourquoi (`travaux/strategie-retenue.md:702-704`).
- Proposer une fois le cadrage, ou un lot unique.
- S'il refuse tout travail payé : arrêter, remettre ce qui lui revient et le dire simplement.

**Pourquoi.** Cette forme cumule les risques les plus graves : travail non payé (R11), responsabilités sans pouvoirs (R7), requalification (R17), dépendance totale (R8).

### 7.4 Arrêter en cours de route

Les signaux de suspension et les règles de sortie sont dans `travaux/strategie-retenue.md:673-685` et dans 12-gouvernance-contrat-sortie.md, sections 12 et 15. Deux chiffres pour s'en souvenir. Une rupture brutale à la fin du pilote coûterait 21 300 € d'apport supplémentaire si l'on continuait à travailler et à se payer, contre 1 700 € en appliquant la règle d'arrêt [ES] (`modele-financier/stress-tests.md:34`). La règle n'est utile que si elle est appliquée le jour même.

---

## 8. Recommandations : preuve, hypothèse, limite, décision

| Recommandation | Preuve | Hypothèse | Limite | Décision |
| --- | --- | --- | --- | --- |
| Traiter le projet comme un test commercial borné | 0 contrat, 0 facture, 0 entité [FV négatif] (`travaux/strategie-retenue.md:33`) ; socle dans ≈ 42 % des cas une fois le cadrage vendu [ES, ce livrable] | Les probabilités de la stratégie sont plausibles [HY] | Aucune parole directe du client ; tout peut aller plus vite qu'estimé | Morgan et Mathys, au 19 nov. 2026 |
| Écart n° 1 : ne payer et ne produire que l'obligatoire avant le rendez-vous | 12 à 25 JP non payées prévues [ES, ce livrable] ; trésorerie personnelle tendue [DR] (`travaux/note-point-4-novembre-et-activites.md:6, 8`) | Un avocat peut relire les statuts en une à deux semaines [HY] | Date du 31 janvier plus serrée | Morgan et Mathys, au 19 nov. 2026 |
| Écart n° 2 : examiner tout de suite une offre d'emploi, comme alternative séparée | Cadre ≈ 3 400 € nets contre 1 100 à 1 500 € de Marwin [ES] (`travaux/ver-R6-marche.md:25` ; `modele-financier/scenarios.md:67`) | GianLuca peut recruter ailleurs s'il attend [HY] | Fin de l'indépendance avec ce client si un associé accepte | Chaque associé pour lui-même ; les deux pour Marwin ; position écrite avant le rendez-vous |
| Écart n° 3 : un lot unique avant de conclure après un refus du cadrage | Le cadrage sert surtout Marwin (`travaux/juge-J2-marwin.md:67`) ; un lot seul est déjà admis (`travaux/strategie-retenue.md:693`) | Le refus vise le format, pas le besoin [HY] | Pas d'inventaire ni de mandat : risque de dérive | Morgan au rendez-vous ; Mathys valide le devis |
| N'abandonner aucune source de revenu avant trois échéances de socle payées | Revenu central de 1 100 à 1 500 € nets, rien pendant cinq mois (`modele-financier/scenarios.md:67, 129-133`) | Les autres revenus existent [IN] | Morgan reste dispersé (R3, R5) | Règle de priorité écrite au pacte |
| Clause « cadrage remis sur entretiens » si les pièces manquent | Aucun accès fourni à ce jour [FV négatif] (`travaux/syn-portefeuille.md:207`) | L'avocat la juge valable [HY] | Dossier plus pauvre | À traduire dans 12-gouvernance-contrat-sortie.md |
| Régime de maintenance écrit dans chaque lot ; décision sur le CRM avant le rendez-vous | Maintenance payée seulement par l'exploitation, au plus tôt au mois 7 (`travaux/strategie-retenue.md:339, 384`) | Le client accepte un régime « sans maintenance » [HY] | Pression relationnelle pour des corrections gratuites | Mathys, avant le premier devis de lot |
| Corriger la question n° 10 : cinq mois sans rémunération en central, six en prudent | `modele-financier/scenarios.md:102-108, 129-134` | — | Dates de démarrage elles-mêmes hypothétiques | Morgan et Mathys, en remplissant la fiche du 19 nov. |

---

## 9. Limites

- **Aucune parole directe de GianLuca Carlone** (`travaux/syn-portefeuille.md:89`). Les probabilités de ce livrable sont des jugements sur une demande rapportée [HY].
- **La collecte est incomplète** : 169 conversations ChatGPT lues sur 219 ; des promesses au client peuvent exister hors du corpus (`travaux/strategie-retenue.md:835`).
- **L'audit ne sait pas si la décision sur la fuite a été prise** ni si le dépôt est toujours public [IN] (`travaux/strategie-retenue.md:836`).
- **Les chiffres viennent du modèle financier** (`modele-financier/scenarios.md`) : coefficient social d'une source secondaire, frais supposés, impôt sur le revenu non calculé. L'expert-comptable doit les refaire.
- **Le coût d'un salarié** est un résultat de simulateur, à lire comme une estimation (`travaux/controle-modele.md:95`). Les coûts cachés d'un recrutement ne sont pas chiffrés [IN].
- **Les écarts n° 1 à 3** n'ont été soumis ni aux juges ni à l'arbitre de l'audit. Ils sont proposés à Morgan et Mathys, qui décident.
- **Points juridiques** (rôles au regard des données personnelles, information des personnes, requalification, propriété des logiciels d'un salarié) : à faire confirmer par l'avocat ou le DPD.
