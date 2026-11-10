# Contrôle indépendant de l'inventaire C2-offre (`ex-C2-offre.md`)

Contrôle fait le 4 novembre 2026. Toutes les sources citées ont été rouvertes : le dépôt `Momolscode/Carlone` (branche main, commit 7b46602, aucun fichier modifié, `git status` vide), la copie locale du diaporama client et les textes extraits des PDF, qui sont cités par la page du PDF d'origine. Le fichier du lecteur n'a pas été modifié. Aucune action extérieure n'a été faite.

**Conventions de citation**
- Les noms de fichiers du dépôt sont uniques. Leurs chemins complets :
  - `offre-marwin-tech-remuneration-et-collaboration.md` = `interne/offre-marwin-tech-remuneration-et-collaboration.md` ;
  - `marwin-offre-accompagnement.md` = `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md` ;
  - `marwin-structure-et-offres.md` = `sources/chatgpt-pages/2026-11-04-complement/marwin-structure-et-offres.md` ;
  - `travail-pour-marwin-studio.json` = `sources/chatgpt-conversations/2026-11-04/travail-pour-marwin-studio.json`.
- « PDF 30 oct. » = `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf`.
- `deck/` = `[diaporama Offre Marwin Tech, copie du 4 nov.] `.
- Les numéros « n° » et « C » renvoient aux lignes et contradictions de `ex-C2-offre.md`.

**Bilan :** 15 éléments déterminants contrôlés. **10 sont confirmés, 5 corrigés** (ce sont des nuances ou des requalifications, aucun chiffre n'est faux) et aucun n'est invérifiable. S'y ajoutent 3 corrections de codes, une réserve de forme sur le nom et 5 omissions, dont 2 importantes.

---

## 1. Éléments contrôlés

| # | Élément (n° du lecteur) | Verdict | Correction et source exacte |
| --- | --- | --- | --- |
| 1 | Formules : la base vaut 15 000 € HT par mois pour 20 journées-personnes (JP, 140 h), soit 90 000 € sur six mois ; le renforcement vaut 30 000 € pour 40 JP (280 h), soit 180 000 €. Les « vingt jours » de Morgan deviennent 20 JP cumulées (n° 2, 3, 44 ; C3). | **Confirmé** | `offre-marwin-tech-remuneration-et-collaboration.md:13-16` ; `deck/slides/formules.html:9-15, 20-26` ; `marwin-offre-accompagnement.md:7` (« vingt jours par personne constitueraient un autre volume »), `:54`, `:58`. Le PDF du 30 oct. (p. 3) précise déjà que le renforcement « suppose de confirmer leur disponibilité ». |
| 2 | Taux de 750 € : le lecteur parle d'un « calcul à rebours » (n° 6) et écrit que « 750 € résulte d'une division : 15 000 ÷ 20 » (§ 9.1). Il relève aussi que le statut du taux s'est durci (C20). | **Corrigé (nuance)** | Les citations sont exactes : `marwin-offre-accompagnement.md:64` (« Hypothèse interne : vingt journées-personnes × 750 € HT = 15 000 € HT ») ; PDF 30 oct. p. 3 (« repère de chiffrage ») ; `offre-marwin-tech-remuneration-et-collaboration.md:18` ; `deck/slides/formules.html:4`. Mais aucune pièce ne dit que le taux a été déduit du montant : la source écrit une multiplication. Le montant de 15 000 € apparaît avant le taux (`marwin-offre-accompagnement.md:7`, puis l. 58 « au même tarif journalier »), ce qui rend l'hypothèse plausible sans la prouver. Il faut recoder en [HY] (déduction du lecteur), l'origine du montant de 15 000 € restant [IN]. C20 est confirmé. |
| 3 | Paiement des mois 2 à 6. Le 29 oct., ils se règlent « sous sept jours après facture de fin de mois ». Les 30 oct. et 2 nov., ils se paient « d'avance ». Le titre « payé d'avance » est inexact pour le solde du mois 1 (n° 7, 8 ; C1). | **Confirmé** | `marwin-offre-accompagnement.md:55-57` ; PDF 30 oct. p. 3 (« 15 000 € HT d'avance, selon les modalités fixées au contrat ») ; `offre-marwin-tech-remuneration-et-collaboration.md:19, 193-196` ; `deck/slides/paiement.html:4, 10, 18, 26`. À ajouter : le PDF du 30 oct. (p. 3) annonçait aussi que « les conséquences d'une interruption seront précisées au contrat ». Ce renvoi disparaît le 2 nov., ce qui renforce le n° 39. |
| 4 | « Le travail démarre à réception » de l'acompte, et le diaporama ne parle pas de l'immatriculation (n° 9, 10 ; C2). | **Confirmé (nuance)** | `deck/slides/paiement.html:10, 32` ; `deck/slides/etapes.html:21`. Aucune des 13 diapositives ne contient « immatricul » (vérifié par recherche). Voir aussi `offre-marwin-tech-remuneration-et-collaboration.md:153, 185, 215`. Nuance : le diaporama place « Signer le contrat-cadre » avant l'acompte (`etapes.html:17`). Le client ne peut donc pas attendre un démarrage avant la signature, mais rien ne lui annonce le délai d'immatriculation. Le code [DR] pour « non immatriculée » est juste (`marwin-structure-et-offres.md:9` ; PDF 30 oct. p. 17). |
| 5 | Le CRM a été livré sans facture : 500 entreprises, 471 numéros, 60 interlocuteurs, 125 fiches. Il est « offert à ce jour » (n° 11, 12). | **Confirmé [DR]** | `offre-marwin-tech-remuneration-et-collaboration.md:29, 33, 227, 259` ; `deck/slides/livre.html:8-21, 24` (« Réalisé à ce jour sans facturation ») ; PDF 30 oct. p. 17 (« Morgan confirme le 30 octobre qu'aucune prestation n'a été facturée »). Les chiffres n'ont pas été revérifiés sur les données du CRM : le code [DR] est donc le bon. |
| 6 | Le dépôt FinanceScope/CRM-Carlone est public et contient des données de prospects, alors que le diaporama promet au client une « clause RGPD » (n° 14 ; C22). | **Confirmé [DR]** | `offre-marwin-tech-remuneration-et-collaboration.md:228` ; `deck/slides/garanties.html:26`. Dernier état documenté : « Dépôt du CRM toujours public (vérifié) » le 4 nov. (`interne/contexte-projet-carlone.md:37`). Ce point n'a pas été revérifié dans cet audit (note C) : le code [DR] est juste. |
| 7 | Le premier mois se répartit en 6, 7, 4 et 3 jours, soit 20 j et 140 h (n° 15). Le lecteur voit « trois définitions en neuf jours » et un titre « trois résultats » illustré par « quatre blocs » (C5 ; § 9.2, points 7 et 17). Il écrit aussi que « le client choisit trois priorités » (n° 19). | **Corrigé (nuance)** | Le calcul est exact (`offre-marwin-tech-remuneration-et-collaboration.md:56-61` ; `deck/slides/premier-mois.html:8-39`). Mais le PDF du 30 oct. (p. 2) contient déjà la même définition. Il annonce « Premier mois : trois résultats prioritaires » : feuille de route et tableau de bord, lot commercial avec « campagne pilote », démonstrateur. Suit une « répartition indicative » en quatre lignes, dont la quatrième est la coordination. Le quatrième bloc est donc du temps de coordination, pas un résultat de plus : l'écart tient à la présentation, pas au fond, et la définition ne bouge plus depuis le 30 oct. Par ailleurs, « trois priorités » ne figure pas à `offre-marwin-tech-remuneration-et-collaboration.md:46`, qui dit « ses priorités ». Le chiffre vient de `deck/slides/premier-mois.html:42-43`, de `deck/slides/formules.html:14` et du PDF 30 oct. p. 2 (« Jusqu'à trois priorités sont travaillées en parallèle »). |
| 8 | Option laboratoire : 30 000 € HT, dont 13 500 € d'honoraires pour 18 JP (3 + 8 + 7 jours, 126 h) et 16 500 € d'achats détaillés ; première tranche possible de 2 250 € (n° 20 ; § 3.4). | **Confirmé** | `offre-marwin-tech-remuneration-et-collaboration.md:21, 65` ; `deck/slides/laboratoire.html:9-10, 25` ; PDF 30 oct. pp. 13-14. Voir aussi `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` p. 8 : 45 000 + 13 500 = 58 500 € d'honoraires, et les 16 500 € « ne sont pas du chiffre d'affaires Marwin ». |
| 9 | L'ancre (renforcement plus laboratoire) demande 46 JP par mois, au-delà des 40 JP théoriques (C4 ; § 3.2). | **Confirmé** | `offre-marwin-tech-remuneration-et-collaboration.md:246` ; `deck/slides/laboratoire.html:25` (« 18 journées sur trois mois, en moyenne six par mois ») ; audit labo p. 8 (« Deux personnes disponibles 20 jours chacune offriraient 40 jours théoriques » ; « Leur disponibilité n'est pas établie »). Les calculs sont exacts [ES] : 210 000 € sur six mois, 40 000 € par mois sur trois mois. Ces montants sont un budget client qui inclut 16 500 € d'achats non facturés par Marwin. |
| 10 | La décision du 4 nov. n'est appliquée qu'à moitié. Le diaporama passe à 11 diapositives sans `strates` ni `strates-phases`, mais les deux fichiers restent. Le document écrit, dans une section non marquée « interne », présente toujours Medhi et BOJ.ART. Le vernissage reste signé « avec Medhi, BOJ.ART » (n° 22, 28, 29, 30, 68 ; C7). | **Confirmé** | `deck/deck.json:7`. Aucune mention de Medhi ni de BOJ dans les 11 diapositives actives (vérifié par recherche) ; ces mentions ne subsistent que dans `deck/slides/strates.html:12` et `deck/slides/strates-phases.html:10, 28`. Voir `offre-marwin-tech-remuneration-et-collaboration.md:7, 22, 67-101, 226, 236, 261` et `pour-carlone/vernissage-strates-diaporama.pdf` p. 12. Précision de code : le [FV] du n° 30 vaut pour la copie du dépôt (commit 7b46602). Pour l'artefact claude.ai lui-même, « non modifié » repose sur la note C, donc sur une [DR]. |
| 11 | Le lecteur affirme que l'atelier d'environ dix imprimantes appartient à BOJ.ART et qu'après le retrait de BOJ.ART, « cette capacité n'est plus fondée » (n° 32 ; C9). | **Corrigé** | Les lignes citées ne font pas ce lien. `marwin-offre-accompagnement.md:21` distingue BOJ.ART (« la personne avec qui je souhaite ouvrir… ») et « J'ai **également** accès à un atelier d'environ dix imprimantes 3D ». `marwin-structure-et-offres.md:100` ne nomme pas de propriétaire. `offre-marwin-tech-remuneration-et-collaboration.md:77, 138` parlent du « parc d'impression BOJ.ART » sans donner de nombre. Le PDF du 30 oct. (p. 4) juxtapose lui aussi « la collaboration envisagée avec BOJ.ART et l'accès déclaré à un atelier ». Le rapprochement est plausible : `interne/state-of-the-art-note-de-vision.md:36` attribue au parc BOJ.ART « 7–8 » puis « une dizaine » de machines (voir aussi `interne/contexte-projet-carlone.md:27`). Il reste néanmoins une [HY]. Formulation à retenir : « probablement le parc de Medhi ; à confirmer par Morgan ». |
| 12 | Simulations de revenu : 3 660, 7 500 et 2 500 € nets par associé, avec une réserve d'environ 3 900 € par mois ; 362 000 € de chiffre d'affaires pour 7 500 € nets. Plancher : 60 000 + 33 332 + 30 000 = 123 332 € par an, soit 10 278 € par mois et 13,7 JP, alors que 14 × 750 = 10 500 € (n° 50, 51 ; C19, C24). | **Confirmé** | `offre-marwin-tech-remuneration-et-collaboration.md:107-121, 157-161, 248`. PDF 30 oct. p. 18 : 43 875 € par an ; « environ 4 280 € … contre 3 660 € ». PDF 30 oct. p. 19 : 46 751 € conservés ; « environ 362 000 € de CA HT annuel » ; « Ces montants ne fixent ni vos rémunérations ni un prix à proposer à Carlone » ; « 180 000 € annuels est seulement une hypothèse commune de comparaison ». Les codes [ES] sont justes. |
| 13 | Rappels de lancement. Le lecteur code [FV] « huit rappels … tous « À préparer » au 29 oct. » (§ 3.6, n° 59), écrit que le rappel du 3 nov. est « encore « À préparer » » (§ 6, Quali Contact) et conclut que les disponibilités ont été fixées après le prix (§ 9.2, point 2). | **Corrigé (code et portée)** | La page est figée au 29 oct. à 07:11 UTC (`marwin-structure-et-offres.md:5`). Les étapes du 29 oct. et des 2, 3 et 4 nov. étaient alors à venir : dire du 3 nov. qu'il est « encore À préparer » ne prouve rien. Seules les étapes des 26 à 28 oct. sont parlantes, dont « Rôles et disponibilité » (l. 85). La page précise en outre qu'« aucun état du calendrier n'est modifié sans décision ou preuve accessible » (l. 156) : « À préparer » veut dire que rien n'est consigné dans ChatGPT, pas que rien n'a été fait. L'activation des rappels est une déclaration de ChatGPT (« Les huit rappels sont actifs », `travail-pour-marwin-studio.json:97`) : c'est une [DR], et leur état actuel est [IN]. La conclusion du lecteur reste vraie, mais elle s'appuie sur une autre source : `offre-marwin-tech-remuneration-et-collaboration.md:128` (« À décider entre vous deux avant le rendez-vous : … le temps que chacun peut réellement donner »). |
| 14 | C15 oppose deux phrases. D'un côté : « Cette offre ne prévoit ni participation au capital ni prêt ». De l'autre : « Investissement éventuel … par un pacte écrit ». Le lecteur en conclut que « le document client ouvre la porte au capital ». | **Corrigé (pas de contradiction)** | La même phrase du 29 oct. ajoute : « Si l'objectif devenait un investissement ou un prêt, un accord distinct serait nécessaire » (`marwin-offre-accompagnement.md:143`). Le diaporama dit la même chose : « Un sujet à part, après les premiers rapports mensuels » (`deck/slides/cadre.html:26`). C'est aussi le cas du PDF du 30 oct. (p. 3 : l'acompte « ne constitue ni une entrée au capital ni un prêt du client ») et de `offre-marwin-tech-remuneration-et-collaboration.md:142, 257`. Les versions concordent : l'investissement reste hors de l'offre et relève d'un accord séparé. Seul changement réel : la voie de repli interne (financer STRATES, `offre-marwin-tech-remuneration-et-collaboration.md:144`) a disparu le 4 nov. |
| 15 | Point de départ de l'offre. Le 25 oct., Morgan écrit : « faut quand même qu'il me paye ce monsieur … DGX Spark … direction des opération de cosne cours sur Loire » et « Je préfère être prestataire ou salarié » (n° 62, 63 ; C21 ; § 3.1, V1). | **Confirmé [DR]** | Les citations sont exactes (`travail-pour-marwin-studio.json:115, 140`). Le tour date du 25 oct. 2026, de 06:08 à 06:13 UTC (horodatages du fichier). La page b393673 a été créée à 06:11:41 UTC (métadonnées de `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.json`). Le « premier forfait » (feuille de route, fiche mission, cahier de passation) vient du tour de 08:41 à 09:09 UTC (`travail-pour-marwin-studio.json:72`) : l'indication « vers 09:00 UTC » est exacte. |

### Autres points contrôlés, sans écart notable
- **n° 65** : le commit b205005 compte 48 fichiers ajoutés et 1 modifié (`git show --name-status b205005`). C'est conforme à `structurer-marwin-tech.json:47`.
- **n° 69** : les « Propositions de collaboration » ne donnent aucun prix (`sources/propositions-de-collaboration.pdf` p. 1).
- **n° 68** : l'option vernissage va de 6 à 30 JP, « sans supplément s'il tient dans les 20 journées » (`pour-carlone/vernissage-strates-diaporama.pdf` pp. 10-11). À ajouter : le format le plus simple suppose déjà « Le parc de Medhi en état » (`pour-carlone/vernissage-strates-idees.md:100`).
- **n° 25 et 26** : confirmés par `deck/slides/strates-phases.html:42-43`.
- **C16** : confirmé par `deck/slides/proposition.html:3` et `marwin-offre-accompagnement.md:84`.
- **C12, C17 et C23** : « Quali », « cabaret », « astreinte », « urgence » et « abonnement » sont absents du document du 2 nov. et des 13 diapositives (vérifié par recherche).
- **C25** : confirmé par `offre-marwin-tech-remuneration-et-collaboration.md:84` et `deck/slides/strates-phases.html:11`.
- **Petites imprécisions sans effet sur les conclusions** :
  - Pièce P4 : les tours sur Éclosion vont de 02:15 à 02:34:56 UTC le 31 oct. L'heure de 02:27 n'est que le début du dernier tour.
  - § 6, ligne Jarvis : la citation « d'abord sur données fictives ou un périmètre autorisé » est attribuée à `offre-marwin-tech-remuneration-et-collaboration.md:60`, qui dit seulement « Démonstrateur Jarvis ». Le texte vient de `marwin-offre-accompagnement.md:75` (« sur des données fictives ou un périmètre autorisé ») et du PDF 30 oct. p. 2 (« d'abord sur données fictives ou autorisées »).

---

## 2. Justesse des codes

- **Faits rapportés par Morgan : aucun n'est codé [FV].** Les n° 10, 11, 12, 14, 29, 44, 49, 62 et 63 sont en [DR], ce qui est correct. Les [FV] restants (n° 28, 30, 59, 65, 66, 69 ; V6) portent sur des fichiers constatés.
- **À corriger :**
  - n° 6 : recoder en [HY] le caractère « à rebours » du taux. La phrase source elle-même est une [HY] interne ou une [PR] (« base de négociation »).
  - § 3.6 et n° 59 (rappels) : le contenu de la page est un [FV] ; l'activation des rappels est une [DR] ; leur état actuel est [IN].
  - n° 30 : le [FV] vaut pour la copie du dépôt seulement. Pour l'artefact en ligne, le code est [DR] (note C).
- **Mineur :** les n° 43 et 47 sont codés [HY]. Ce sont des garde-fous écrits dans la proposition du 29 oct. : [PR] conviendrait mieux.
- Les autres codes sont cohérents : [ES] pour les calculs (TTC, ancre, plancher, revenus), [IN] pour les inconnues, [PR] pour les clauses proposées.

## 3. Respect du nom GianLuca

- « GianLuca » apparaît 33 fois, sans aucune variante. Dans le corps du texte, les citations fautives sont bien suivies de [sic, lire GianLuca] (`ex-C2-offre.md:18, 334`). La réécriture du n° 44 place le prénom hors des guillemets, ce qui est acceptable.
- Les décomptes du § 7 sont exacts (vérifiés par recherche) :

  | Fichier | « John-Lucas » | « John Lucas » |
  | --- | --- | --- |
  | `marwin-offre-accompagnement.md` | 9 | 1 |
  | `marwin-structure-et-offres.md` | 2 | 0 |
  | `travail-pour-marwin-studio.json` | 5 | 0 |
  | `structurer-marwin-tech.json`, document du 2 nov., diapositives | 0 | 0 |

  Les titres du `.json` de métadonnées sont également conformes.
- **Réserve de forme :** au § 7 (`ex-C2-offre.md:269-270`), trois fragments sont cités sans [sic, lire GianLuca] : « Proposition à adresser à John Lucas », « Bonjour John-Lucas » et « John-Lucas Carlone Offre et projets en Nièvre ». C'est tolérable dans un relevé d'erreurs, mais contraire à la lettre de la règle 1. Il faut ajouter la mention.

---

## 4. Omissions

### Omissions importantes

1. **La règle sur les gains d'automatisation a disparu, alors qu'elle touche directement au prix.**
   - Le 29 oct. : « Les économies issues de l'automatisation permettent de réaffecter la capacité ou de revoir le forfait ; elles ne sont pas présentées comme des heures manuelles fictivement réalisées » (`marwin-offre-accompagnement.md:66`).
   - Le 30 oct., même règle : les gains « servent à réaliser davantage dans la capacité réservée ou à ajuster le forfait » (PDF 30 oct. p. 4).
   - Le document du 2 nov. et le diaporama ne disent plus rien, alors que la facturation reste au temps : « Les livrables, avec les journées consommées » (`deck/slides/garanties.html:15`).

   **Pourquoi c'est important :** les versions antérieures acceptaient de reverser les gains au client, jusqu'à une baisse du forfait. Dans un modèle au temps, chaque gain d'automatisation réduit ce que Marwin peut facturer. C'est le cœur de DEMANDE § 11 (« rémunérer organisation, responsabilité et valeur quand l'automatisation réduit le temps »). Il faut trancher explicitement [PR] et ne pas laisser la question disparaître en silence.

2. **L'option laboratoire, maintenue dans le diaporama à 11 diapositives, dépend encore de BOJ.ART et de STRATES.**
   - PDF 30 oct. p. 13 : « La disponibilité réelle de BOJ.ART et des intervenants est vérifiée avant de fixer les lots ».
   - `offre-marwin-tech-remuneration-et-collaboration.md:84` : « Si le pilote laboratoire est retenu, son geste robotique devient ce premier trait » de STRATES.
   - L'image de la diapositive montre une imprimante 3D en arrière-plan (`deck/slides/laboratoire.html:21`).

   **Pourquoi c'est important :** retirer Medhi et BOJ.ART le 4 nov. prive aussi l'option laboratoire de son geste robotique cible et de l'accès aux imprimantes, sans que la diapositive change. Le lecteur signale le retrait incomplet pour le document écrit et le vernissage (C7 ; § 9.2, points 9 et 10), mais pas pour cette option encore présentée au client.

### Autres omissions

3. **Société en formation, responsabilité personnelle et date de début d'activité.**
   - `offre-marwin-tech-remuneration-et-collaboration.md:185` : « D'ici là, les signataires en répondent personnellement » ; voir aussi `marwin-offre-accompagnement.md:145`.
   - PDF 30 oct. p. 17 : l'absence de facture « ne prouve pas, à elle seule, que l'activité n'a pas déjà débuté : les travaux réalisés sur le CRM … doivent être décrits fidèlement ».
   - `offre-marwin-tech-remuneration-et-collaboration.md:169` : le FRR exige de prouver « l'origine de l'activité (dont le CRM non facturé) ».

   Le CRM « offert » peut donc peser sur l'ACRE (demande dans les 60 jours du début d'activité, l. 173), sur le FRR et sur sa propriété. Le lecteur cite ces aides en [DR] sans faire le lien. C'est une question pour l'expert-comptable.

4. **L'architecture contractuelle « contrat-cadre et fiches de mission » a été perdue.**
   - PDF 30 oct. p. 2 : « Un contrat-cadre organise la collaboration ; des fiches de mission précisent les projets réellement engagés ».
   - PDF 30 oct. p. 4 : « critères de réception, changements de périmètre, reports de capacité, interruption de mission … fixés avant le démarrage ».
   - Le diaporama parle toujours de « Signer le contrat-cadre » (`deck/slides/etapes.html:17`), mais le document du 2 nov. ne définit plus de fiches de mission.

   C'était précisément le garde-fou contre l'absorption par l'abonnement (DEMANDE § 4). Il manque à la liste des pertes du lecteur (§ 9.2, point 16).

5. **Une erreur d'identité figure dans un document destiné au client, hors du lot du lecteur.** Le PDF du 30 oct. (pages 1 à 4, « PROPOSITION CARLONE ») s'intitule « Proposition d'accompagnement pour John-Lucas Carlone » [sic, lire GianLuca] (p. 1). Le lecteur a consulté cette page, mais son § 7 ne relève que la lettre de la page ChatGPT. Si ce PDF a été montré au client, il portait l'erreur [IN].
