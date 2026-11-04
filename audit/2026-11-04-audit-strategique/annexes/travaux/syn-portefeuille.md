# Synthèse « portefeuille » : besoin réel, acheteurs et chantiers de GianLuca Carlone

Synthétiseur « portefeuille » de l'audit Marwin Tech × GianLuca Carlone, rédigé le 4 novembre 2026 au soir.

**Document interne.** Il contient des éléments de négociation, de capacité et de stratégie propres aux associés. Il ne doit pas être transmis tel quel à GianLuca Carlone.

## Méthode, sources et conventions

**Bases utilisées :**
- les inventaires ex-C1, ex-C2, ex-C5, ex-C6, ex-C8, ex-C9 et ex-C10 (sections 2, 5, 6 et 9) et leurs contrôles ver-C1 à ver-C10 ;
- le mémo rj-R5 et son contrôle ver-R5 pour les obligations liées aux lieux, aux œuvres et à la robotique ;
- rj-R4 et ver-R4 pour la violation de données ;
- ver-C7, en appui, pour Jarvis.

Quand un contrôleur corrige un lecteur, c'est sa correction qui est retenue. Elle est signalée par « corr. ver-… ».

**Pièces d'origine rouvertes pour les points déterminants ou contestés.** Le dépôt `Momolscode/Carlone` est sur la branche main, au commit 7b46602 du 4 nov. 2026 à 17:37 (vérifié par `git log -1`, arbre propre), et a été lu sans modification. Pièces rouvertes :
- `sources/propositions-de-collaboration.pdf` p. 1 ;
- `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:7, 13-18, 65` ;
- `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:7-25, 94-105` ;
- `interne/contexte-projet-carlone.md:5-60, 100-130` ;
- `interne/offre-marwin-tech-remuneration-et-collaboration.md:9-23, 44-66, 84, 262-275` ;
- `interne/recueil-sessions-chatgpt-2026-11-04.txt:220, 248, 755, 809, 1469` ;
- `interne/audit-marwin-tech-carlone.md:1-16, 66-90` ;
- le texte extrait de `pour-carlone/vernissage-strates-diaporama.pdf` ;
- `deck/deck.json` ;
- l'arbre de la branche distante de la PR n° 1.

Les calculs ont été refaits en Python.

**Aucune action extérieure** n'a eu lieu : aucun contact, aucune consultation en ligne, aucune modification hors de ce fichier.

**Nom du client.** Le client s'appelle **GianLuca Carlone**. Les pièces qui portent l'erreur d'archives sont citées telles quelles, suivies de [sic, lire GianLuca].

**Codes.**

| Code | Sens |
| --- | --- |
| [FV] | Fait vérifié |
| [DR] | Déclaration rapportée, presque toujours « selon Morgan » |
| [PR] | Proposition de Marwin |
| [HY] | Hypothèse |
| [ES] | Estimation |
| [MM] | Résultat mesuré |
| [IN] | Inconnu |

**Abréviations des pièces citées.** Sauf mention contraire, les chemins partent de la racine du dépôt.

| Abréviation | Pièce |
| --- | --- |
| PROP | `sources/propositions-de-collaboration.pdf` (18 oct.) |
| COP | `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md` (page ChatGPT, 28 oct.) |
| ACC | `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md` (page ChatGPT, 29 oct.) |
| STR | `sources/chatgpt-pages/2026-11-04-complement/marwin-structure-et-offres.md` (29 oct.) |
| TMS | `sources/chatgpt-conversations/2026-11-04/travail-pour-marwin-studio.json` |
| BRAS | `sources/chatgpt-conversations/2026-11-04/bras-robotique-precis.json` |
| R | `interne/recueil-sessions-chatgpt-2026-11-04.txt` |
| CTX | `interne/contexte-projet-carlone.md` (4 nov.) |
| OFF | `interne/offre-marwin-tech-remuneration-et-collaboration.md` (2 nov.) |
| AUD | `interne/audit-marwin-tech-carlone.md` (2 nov.) |
| CAT | `interne/offres-de-carlone-catalogue-crm.md` (2 nov.) |
| DPV | `sources/dossier-partenariats-vieux-relais-et-le-m-2026-10-21.pdf` (dossier de Mathys) |
| PASS | `crm/PASSATION.md` |
| RAP | `crm/docs/rapport/rapport-crm-hermes360.md` |
| V5 | `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` |
| LABO | `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` |
| STRv11 | `pour-carlone/strates-proposition-artistique-v1.1.pdf` |
| IDEES | `pour-carlone/vernissage-strates-idees.md` |
| VERN | `pour-carlone/vernissage-strates-diaporama.pdf` |
| deck/ | `…/scratchpad/artifact-files/04f14ef8-a5fd-429b-9b3e-6d69b1d2ce5f/project/` (diaporama client en ligne) |
| NOTE | `audit-work/note-point-4-novembre-et-activites.md` |

**Faits nouveaux intégrés à cette synthèse**

1. **Retrait de Medhi et de BOJ.ART.** Le 4 nov. 2026, Morgan a demandé de retirer Medhi et BOJ.ART de l'offre : « Va juste falloir enlever Medhi/boj art de l'offre » [DR] (NOTE:25).
   - Corrigé : le diaporama client, qui compte désormais 11 diapositives sans `strates` ni `strates-phases` [FV] (`deck/deck.json:7`).
   - Non corrigés : l'offre écrite (OFF:22, 67-101), STRATES v1.1, le vernissage (diaporama et idées) et le PDF de 13 diapositives de la PR n° 1. Ce PDF est vérifié par `git ls-tree` sur la branche `origin/claude/dossier-carlone-2026-11-04` : il contient `pour-carlone/offre-marwin-tech-pour-carlone.pdf` et les diapositives `08-strates.jpg` et `09-strates-phases.jpg` [FV].
   - La décision est orale. Elle n'a été formalisée ni avec Mathys ni avec Medhi [DR].
2. **Violation de données probable.** Le dépôt public FinanceScope/CRM-Carlone constitue très probablement une violation de données personnelles [HY fort] (rj-R4 (c)).
   - Si la connaissance date du 2 nov. (AUD:3, 15 : « Urgent », « Le dépôt GitHub du CRM est public »), le délai de 72 heures pour notifier la CNIL expire le **5 nov.**, à une heure inconnue [ES]. Au soir du 4 nov., il n'est donc pas encore dépassé, sauf si la connaissance est antérieure [IN] (corr. ver-R4 n° 7).
   - Le responsable de traitement n'est pas désigné [IN].
3. **Aucune base contractuelle.** Il n'existe aucun contrat, aucune facture et aucune entité payeuse identifiée. C'est un constat d'absence dans tout le dépôt [FV négatif] (CTX:5, 51 ; OFF:269 ; R:609).

---

## 0. Ce qu'il faut retenir

1. **Le « pilotage global » n'est ni démontré ni réfuté.**
   - Aucune pièce ne contient une parole directe de GianLuca Carlone : la recherche de « selon Carlone », « Carlone dit » ou « Carlone veut » ne donne rien (ver-C10 § 2) [FV négatif].
   - Le même brief du 28 oct. attribue les « vingt jours par mois » tantôt à GianLuca (COP:65), tantôt à Morgan (ACC:7) [DR contradictoire] (corr. ver-C1 n° 4).
   - L'offre est passée d'une version « limitée à quatre jours mensuels » à 20 journées-personnes sans demande du client documentée (ACC:7) [DR].
2. **Le besoin le mieux documenté est un besoin par projet.** Il reste rapporté [DR] :
   - vendre des œuvres aux entreprises de la Nièvre ;
   - ouvrir une galerie en 2027 ;
   - peut-être racheter le M pour un cabaret ;
   - réunir des artistes ;
   - engager Quali Contact pour les appels (COP:7, 13-16 ; CAT:9) ;
   - et, en plus, un souhait de « ne pas gérer chaque détail » (ACC:13).

   Cela rend plausible un besoin de **coordination**. Cela ne prouve pas un besoin d'abonnement de 20 à 40 journées-personnes par mois.
3. **L'acheteur est introuvable.**
   - Aucune entité juridique de GianLuca Carlone n'est nommée dans le dépôt [FV négatif].
   - Le Vieux Relais, le M, la galerie et les « six bâtiments » n'ont ni propriétaire ni exploitant établis (ver-C9 n° 6) [FV négatif].
   - Un patrimoine déclaré n'est pas une trésorerie disponible (`interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` p. 2) [DR].
4. **Un seul actif a été produit : le CRM.**
   - Il compte 500 fiches. Il a été livré sans facture et sans usage mesuré [FV/DR].
   - Il fait l'objet d'une violation de données probable, avec une décision de notification à prendre avant le 5 nov.
5. **Classement des onze chantiers** (section 4) :
   - **cinq peuvent financer Marwin**, sous conditions : cadrage et pilotage, CRM, Quali Contact, productions par lot (supports, catalogue privé des œuvres, dossiers d'événements et de lieux), et Jarvis réduit à un outil documentaire mesuré ;
   - **trois sont exploratoires** et consomment des ressources sans financeur : STRATES et Éclosion, le laboratoire, et le vernissage dans son format « signature » ;
   - **le reste est hors périmètre ou retiré** : Medhi et BOJ.ART, l'exploitation du cabaret, et les obligations d'exploitant, de conseil fiscal et d'intermédiaire de vente.
6. **La décision du 4 nov. n'est appliquée qu'à moitié.** Au moins sept documents ou fichiers la contredisent encore (section 3.9). L'option laboratoire, toujours dans le diaporama, avait pour « geste robotique » le premier trait de STRATES (OFF:84). Elle n'a donc plus d'objet.
7. **Recommandation de portefeuille [PR].**
   - Vendre d'abord un **forfait de cadrage court et payé**, qui sert aussi de test du besoin : entités, lieux, trois priorités, accès, interlocuteurs, budget.
   - Ensuite, un **lot CRM** : conformité d'abord, non facturée puisque l'exposition est de notre fait, puis un pilote de 20 comptes mesuré.
   - Geler STRATES, Éclosion et le laboratoire.
   - Ne proposer un pilotage récurrent qu'une fois le cadrage accepté et payé.

---

## 1. Test de l'hypothèse « GianLuca veut un pilotage global »

### 1.1 D'où vient l'hypothèse : la chaîne de transmission

| Date | Énoncé | Qui parle | Code | Source |
| --- | --- | --- | --- | --- |
| 18 oct. | Huit missions « pour accompagner vos activités et simplifier leur suivi » : suivi des établissements, rentabilité, administration, prestataires, outils après rachat, catalogue privé des œuvres, séjours des invités, événements. Aucun nom, aucun prix, aucun émetteur | Émetteur anonyme (Marwin, très probablement) | [PR] | PROP p. 1. Remise au client : [IN] (ex-C1 n° 20) |
| 25 oct. | « faut quand même qu'il me paye ce monsieur moi je peux lui faire une offre d accompagnement » ; « une DGX Spark déjà en matériel ça serait sympa » ; « il a investis dans des bureaux pour du personnel ont en ferait partie » | Morgan | [DR] | R:220 ; TMS:140 |
| 25 oct. | « Je préfère être prestataire ou salarié » | Morgan | [DR] | R:248 |
| 25 oct. | « le client prévoit d'engager Quali Contact ; le message précédent proposant de construire ses offres reste mis de côté » | Morgan, reformulé par ChatGPT | [DR] | COP:7 |
| Entre le 25 et le 28 oct. | Une version de l'offre « limitée à quatre jours mensuels » | — | [IN] (contenu non archivé) | ACC:7 |
| 28 oct. | Version A : « John-Lucas [sic, lire GianLuca] souhaite déléguer le quotidien et envisage une disponibilité de vingt jours par mois, avec davantage de couverture si nécessaire » | Morgan, reformulé par ChatGPT | [DR] | COP:65 |
| 28 oct. | Version B, même brief : « John-Lucas [sic, lire GianLuca] souhaite déléguer le suivi quotidien de ses projets, et **Morgan envisage une implication de vingt jours par mois** » | Morgan, reformulé par ChatGPT | [DR] | ACC:7 |
| 29 oct. | Brouillon de lettre : « Vous m'avez expliqué vouloir développer vos projets sans avoir à en gérer chaque détail » | Morgan, rédigé par ChatGPT | [DR] ; envoi [IN] | ACC:13 (= R:967) |
| 2 nov. | Il « propose des bureaux, une bonne rémunération et envisage d'investir dans l'activité de Morgan et Mathys » | Morgan (messages du 2 nov.) | [DR] | CTX:24 ; CAT:9, 140 ; OFF:132 |
| 4 nov. | Aucun rendez-vous à l'agenda jusqu'au 6 nov. | Agenda de Morgan | [DR] | NOTE:5 ; CTX:15 |

### 1.2 Éléments en faveur de l'hypothèse

1. **Plusieurs projets déclarés.** On parle de CRM et de vente d'œuvres, de galerie, de cabaret, d'événement artistique, d'établissements rachetés et de Quali Contact. S'ils sont réels, cela fait un portefeuille à coordonner [DR] (COP:13-16 ; CTX:24 ; CAT:9).
2. **Trois formulations concordantes d'un souhait de délégation :**
   - « déléguer le quotidien » (COP:65) ;
   - « déléguer le suivi quotidien de ses projets » (ACC:7) ;
   - « sans avoir à en gérer chaque détail » (ACC:13).

   Toutes passent par Morgan [DR].
3. **Des moyens proposés pour du personnel :** des « bureaux pour du personnel » (R:220) et « une bonne rémunération » (CTX:24) [DR]. Cela indique une volonté d'avoir des gens près de lui pour faire avancer ses affaires.
4. **Une cohérence d'ensemble :** les huit missions du 18 oct. correspondent au profil d'un détenteur de plusieurs établissements (PROP p. 1) [PR], ce qui concorde avec les rachats déclarés [DR].

### 1.3 Éléments contre l'hypothèse, ou qui l'affaiblissent

1. **Aucune trace directe du client.** On ne trouve aucun écrit, aucune réponse aux propositions et aucun compte rendu de rendez-vous [FV négatif] (ex-C1 § 9.1 ; ver-C10 § 2). L'issue du rendez-vous du 22 oct. est inconnue [IN] (CTX:43, 159 ; corr. ver-C1 n° 17).
2. **Les « vingt jours » ont une attribution contradictoire** (versions A et B ci-dessus).
   - Ce volume a pu être proposé par Morgan [DR] et non demandé par le client.
   - On ignore si GianLuca entend 20 jours pour l'équipe ou par personne. Dans le second cas, il attendrait le « renforcement » à 30 000 € HT au prix de la formule de base (ex-C1 § 4) [HY].
3. **L'offre est née du côté de l'offre, pas de la demande.** Ses déclencheurs visibles sont :
   - le besoin de Morgan d'être payé (R:220) ;
   - son souhait d'une DGX Spark (R:220) ;
   - son souhait d'une « direction des opérations » à Cosne (R:221 ; TMS:140) ;
   - le laboratoire « en parallèle » (R:1330) [DR].

   Le prix de 15 000 € apparaît avant le taux, et son origine est [IN] (corr. ver-C2 n° 2).
4. **Les besoins rapportés sont ciblés et en partie confiés à d'autres.** Les appels iraient à Quali Contact (COP:7) [DR]. Le message de ChatGPT qui proposait de construire ses offres est « mis de côté » (COP:7) [DR].
5. **Aucun paiement ni usage.**
   - Le CRM est « offert à ce jour » (OFF:227) [DR] et rien n'est facturé (V5 p. 17) [DR].
   - Aucun appel, aucun rendez-vous et aucune vente ne sont constatés (COP:57) [DR].
   - Aucun suivi n'est versionné (ver-C5 n° 7) [FV].
6. **Il n'y a pas d'urgence visible côté client.** Aucun rendez-vous n'est fixé (NOTE:5). Le rendez-vous « argent et rémunération » préparé le 2 nov. n'a pas de date (CTX:15) [DR].
7. **Il propose peut-être de salarier plutôt que de confier un mandat.** Les bureaux pour du personnel, la rémunération et l'emploi évoqué (CTX:109 ; OFF:274) peuvent traduire une préférence pour intégrer des personnes plutôt que confier un pilotage à une société extérieure [HY].
8. **Le périmètre a dérivé sans décision tracée.** On est passé des huit missions de gestion d'établissements (18 oct.) au CRM, à STRATES, au vernissage et au laboratoire (2-4 nov.) (ex-C1 § 4, ligne « Ce qui a été proposé ») [FV].
9. **Les objets à piloter ne sont pas établis.** Aucun établissement n'est identifié (ex-C9 § 9.1) [FV négatif]. Le volet « Piloter » (OFF:52) porte donc sur des lieux inconnus.

### 1.4 Ce qui n'est que rapporté par Morgan

Tout ce qui suit est [DR]. Aucune de ces affirmations n'a fait l'objet d'une vérification, de registre, de cadastre ou de document du client (CTX:29 : « je n'ai fait aucune recherche sur ces personnes » ; `interne/complement-chatgpt-2026-11-04.md:15`).

| Affirmation | Source |
| --- | --- |
| Marchand d'art « venu de l'avenue Montaigne » | CTX:5, 24 ; CAT:9 |
| « Plus gros client de Morgan et Mathys », alors qu'aucune facture n'existe | CTX:5 ; R:419, 609 |
| « Vend des œuvres avec un avantage fiscal », alors que le même document demande « Vend-il déjà à Paris avec cet argument ? » | CAT:7, 124 |
| A racheté « six bâtiments » et « l'ancienne affaire de Medhi » | CTX:24 |
| A racheté « un ancien bar restaurant hôtel avec cour pour en faire une galerie » | COP:14 |
| Ouvrira une galerie en 2027 | CAT:9 |
| « Souhaite racheter le M » (cabaret) | COP:15 |
| Veut « réunir des artistes et peintres dans la ville de Morgan » | COP:16 |
| Vise les entreprises de la Nièvre | COP:13 |
| Prévoit d'engager Quali Contact | COP:7 |
| Veut déléguer le quotidien, « vingt jours par mois » (attribution contradictoire) | COP:65 ; ACC:7 |
| Propose des bureaux, une bonne rémunération, peut-être un investissement | CTX:24 ; OFF:132 |
| « L'investisseur en question serait Carlone » (programme robotique). C'est une seule phrase de Morgan, le 2 nov. à 00:56 | BRAS:110 |
| Connaît BOJ.ART ; lien avec Medhi par le rachat de son affaire | CTX:24, 29 |

### 1.5 Ce qu'on sait du besoin : état par rubrique

| Rubrique (DEMANDE § 3) | Ce qu'on sait | Code | Source |
| --- | --- | --- | --- |
| **Problèmes prioritaires** | Vendre des œuvres aux entreprises de la Nièvre ; galerie 2027 ; peut-être cabaret ; réunir des artistes ; campagnes d'appels via Quali Contact ; ne pas gérer chaque détail | [DR] | COP:7, 13-16 ; CAT:9 ; ACC:13 |
| | Leur **ordre de priorité** n'est donné nulle part ; le choix « parmi les huit missions » est une question ouverte | [IN] | CTX:107 ; OFF:273 |
| **Coûts actuels** (temps, argent, opportunités perdues) | Aucune donnée : ni temps passé, ni personnel, ni coût de gestion des lieux, ni coût de Quali Contact | [IN] | — |
| | Une « fenêtre » de réservations de fin d'année (fin octobre à mi-novembre) pour les lieux | [HY] (non sourcée) | DPV p. 33 |
| **Ce qu'il délègue** | « Le quotidien », « le suivi quotidien de ses projets », les appels à Quali Contact | [DR] | COP:7, 65 ; ACC:7 |
| | Le contenu exact du « quotidien » | [IN] | ex-C1 Q7 |
| **Ce qu'il garde** | Inconnu | [IN] | — |
| | Proposé le 29 oct. : contrats, recrutements, emprunts, investissements et changements stratégiques réservés au client, et « une absence de réponse ne vaut pas approbation » | [PR] | ACC:100-103 |
| | Réduit le 2 nov. à une ligne de plafonds, avec en plus une réception tacite « réputé accepté » | [PR] | OFF:206, 208 ; ex-C2 C14 |
| **Accès et informations qu'il fournirait** | Aucun accès fourni n'est documenté : ni comptabilité, ni contrats, ni agenda | [FV négatif] | Dépôt entier |
| | Inventaire des accès entre J1 et J10 | [PR] | ACC:25 |
| | Autoriser « l'adresse de M. Carlone » dans le CRM | [PR] | RAP:140 |
| **Fonctionnement qu'il accepterait** | Point régulier, revues à 30 et 90 jours, tableau de bord : proposés, sans réponse connue | [PR] / [IN] | ACC:25 ; OFF:23 |
| **Personnes impliquées** | GianLuca Carlone | [DR] | — |
| | « Un associé » qui « rachète deux établissements » | [DR] | PASS:41 |
| | Le « nous » repreneur du Vieux Relais et du M | [DR] | DPV p. 32 |
| | « Responsables » d'établissement et « comptable » | [HY] | PROP p. 1 |
| | Expert-comptable ou avocat fiscaliste | [IN] | CTX:113 |
| | Opératrices de Quali Contact | [DR] | COP:7 |
| | Medhi | [DR] | CTX:24 |
| | Artistes : aucun engagé | [IN] | CAT:52 |
| | Côté Marwin : Morgan (programme, prix) et Mathys (technique, CRM) ; disponibilité de Mathys | [DR] ; [IN] pour la disponibilité | CTX:25-26, 120 |
| **Résultats qu'il paierait** | Aucun budget, aucun montant, aucun mode de paiement exprimé | [IN] | ex-C1 Q15 ; ex-C2 Q25 |
| | « Une bonne rémunération », sans montant | [DR] | CTX:24 |
| | Résultats possibles : ventes d'œuvres, ouverture de la galerie, réouverture des lieux, temps libéré | [HY] | — |
| | Une rémunération liée aux ventes exposerait Marwin au statut d'intermédiaire (LCB-FT, droit de suite) | [HY] | rj-R5 (a) |

### 1.6 Verdict et test proposé

**Verdict [HY].** Un besoin de coordination est plausible. Un pilotage global n'est pas démontré, et la solvabilité est inconnue. La seule base est une parole rapportée au second degré : Morgan, puis un assistant IA.

Une capacité technique déjà démontrée ne prouve pas l'existence d'une demande solvable. C'est le cas du CRM [FV pour le code], qui n'a aucun usage mesuré.

**Test proposé [PR].** Le test est un **forfait de cadrage court et payé**. Son prix est à établir : 6 journées-personnes à 750 € feraient 4 500 € HT [ES], mais le taux n'est pas justifié (ex-C2 § 9.1). Son contenu :
- inventaire signé des entités, des lieux et des projets ;
- trois priorités sur 90 jours choisies par GianLuca ;
- accès et interlocuteurs désignés ;
- budget par projet ;
- mandat écrit.

C'est la reprise du « premier forfait » borné du 25 oct. (R:1469 ; TMS:72).

**Signaux qui confirmeraient l'hypothèse [PR]** :
- un bon de commande signé par une entité identifiée, et un premier paiement reçu ;
- des accès réels fournis (comptabilité, contrats, agendas) ;
- des responsables désignés ;
- la demande d'un suivi récurrent après le cadrage.

**Signaux qui l'infirmeraient** :
- un refus de payer le cadrage ;
- le besoin réduit à un seul projet, par exemple les ventes d'œuvres ;
- une préférence pour l'embauche salariée ;
- aucun accès fourni dans les 10 jours.

**Point d'attention.** L'aide régionale au conseil stratégique (50 % jusqu'à 15 000 € sur deux ans) impose de **déposer le dossier avant la signature** du devis [DR] (R:755, 809 ; ver-C10, omission 2). Si GianLuca y est éligible, la séquence est la suivante : dépôt du dossier, puis signature, puis acompte. Elle doit être réconciliée avec la règle « le travail démarre à réception de l'acompte » (OFF:193) et avec l'absence d'immatriculation de Marwin (OFF:153).

---

## 2. Cartographie des acheteurs

### 2.1 Entités juridiques connues ou supposées

| Entité | Ce qu'on sait | Code | Source | Rôle possible |
| --- | --- | --- | --- | --- |
| **GianLuca Carlone**, personne physique | Nom fixé par Morgan le 4 nov. ; état civil et fonctions officielles non vérifiés | [DR] | NOTE:26 ; ver-C1 « Nom du client » | Commanditaire déclaré de tout |
| Société de marchand d'art (Paris) | Aucune dénomination ni SIREN | [IN] | CTX:24, 106 | Signataire ou payeur possible |
| « Structure qui vend les œuvres » | Laissée « à compléter » dans chaque mail du CRM. On ignore si elle existe déjà | [FV] pour le champ vide ; [IN] pour l'existence | `crm/site/index.html:2040, 2135` ; PASS:31 (corr. ver-C5 n° 14 ; ver-C6 n° 3) | Bénéficiaire du CRM et responsable de traitement possible |
| Propriétaire des « six bâtiments » | SCI, société ou personne physique : inconnu | [DR] / [IN] | CAT:9 | Bailleur des bureaux ; maître d'ouvrage des travaux |
| Exploitant(s) du Vieux Relais et du M | « Nous reprenons » ; « Un associé rachète deux établissements » ; le CRM parle de « nos établissements » | [DR] ; repreneur [IN] | DPV p. 32 ; PASS:41, 27 ; `crm/site/index.html:2040` (corr. ver-C6 n° 10) | Commanditaire du volet « Piloter » et des événements |
| Exploitant du futur cabaret (le M ?) | « Souhaite racheter » | [DR] | COP:15 | Titulaire des licences |
| Future galerie (2027) | Bâtiment, entité et dates inconnus | [DR] / [IN] | CAT:9 ; COP:14 | Organisateur des événements ; vendeur |
| « L'ancienne affaire de Medhi » | Nature et forme inconnues | [DR] | CTX:24 | — |
| Conseil (expert-comptable, avocat) | Non identifié | [IN] | CTX:113 | Validation fiscale et juridique |
| Quali Contact / Qualicontact | Prestataire d'appels « prévu » ; contrat, outil et payeur inconnus | [DR] ; [IN] | COP:7, 13, 51 | Sous-traitant probable de l'entité vendeuse |
| **Marwin Tech** | Non immatriculée ; forme non décidée | [DR] | OFF:153, 215 ; CTX:12 | Prestataire, sans pouvoir facturer aujourd'hui |
| Entreprise existante de Morgan (non nommée) | Domiciliation résiliée ; 144 € et RIB attendus depuis le 12 oct. | [DR] | NOTE:6 | Structure de facturation de repli éventuelle, à examiner |
| FinanceScope | Organisation GitHub « de Mathys » ; titulaire et statut juridique inconnus | [DR] / [IN] | `README.md:35` (ex-C5 n° 2) | Détenteur du code du CRM |
| BOJ.ART | Projet de Medhi ; statut juridique inconnu. Morgan s'y dit co-porteur (« la personne avec qui je souhaite ouvrir la boutique ») | [DR] | ACC:21 ; OFF:90 (ex-C2 C8) | Retiré de l'offre le 4 nov. |
| State Of The Art | Forme : « on sait pas encore » | [DR] | CTX:129 | Marque d'ensemble, sans existence juridique |

### 2.2 Projet par projet : qui commande, profite, signe, paie et valide

« Inconnu » vaut [IN] partout. Les colonnes « Signataire », « Payeur » et « Valideur » sont **inconnues pour tous les projets** : aucune pièce ne les nomme [FV négatif] (OFF:269, 272 ; CTX:106).

| Projet | Entité porteuse probable | Commanditaire | Bénéficiaires | Remarque déterminante |
| --- | --- | --- | --- | --- |
| CRM et vente d'œuvres aux entreprises | « Structure qui vend les œuvres » [IN] | GianLuca [DR] ; seul donneur d'ordre nommé dans le CRM : Mathys (PASS:7) [DR] | Entité vendeuse ; acheteurs entreprises | Responsable de traitement **non désigné** [IN] : c'est lui qui notifie la violation (rj-R4 (c) 3). Travail passé non facturé [DR] |
| Coordination Quali Contact | Entité vendeuse [HY] | GianLuca [DR] | Entité vendeuse | Contrat entre GianLuca et Quali Contact : [IN] |
| Organisation et pilotage | Entités des établissements [IN] | GianLuca [DR] | GianLuca et ses établissements (non identifiés) | Valideur demandé en OFF:272. Un accord personnel ne lie pas les sociétés |
| Jarvis et automatisations | — | Proposé par Marwin [PR] | GianLuca [PR] | Propriété du nom et du code [IN] : « Medhi apporte… Jarvis » (OFF:90) |
| Marketing et contenus | Entité vendeuse, galerie, lieux [IN] | Aucune demande exprimée [IN] | Mêmes entités | « Studio marketing » est un positionnement de Marwin (corr. ver-C1 n° 16) [PR] |
| Galerie, œuvres, artistes | Galerie, entité vendeuse [IN] | GianLuca [DR] | Galerie ; artistes (dépôt-vente) | Les contrats avec les artistes relèvent de l'entité de GianLuca, pas de Marwin (rj-R5 (b)) [PR] |
| Événements et vernissage | Organisateur légal : entité de GianLuca ou exploitant du lieu (rj-R5 (d)) [PR] | Vernissage : proposé par Marwin [PR]. « Réunir des artistes » : GianLuca [DR] | Galerie, lieux | Les autorisations (GN 6, boissons, Sacem, spectacles) sont au nom de l'organisateur |
| Cabaret et autres lieux | Exploitant [IN] ; propriétaire [IN] | GianLuca ou « un associé » [DR] | Exploitant | Le signataire doit être l'exploitant, titulaire des autorisations (rj-R5 (e)) |
| Medhi et BOJ.ART | BOJ.ART (statut [IN]) | Proposé par Morgan [PR] | Medhi ; galerie | Retiré le 4 nov. [DR] |
| STRATES et Éclosion | Porteurs pressentis BOJ.ART et Marwin ; véhicule « à formaliser » (`…/dossier-investisseur-v1-2026-11-02.pdf` p. 1) [PR] | Proposé par Morgan [PR] | Galerie (exclusivité) [PR] | Payeur : « serait Carlone » (BRAS:110) [DR, une phrase]. Aucun accord écrit avec Medhi [IN] |
| Laboratoire IA et robotique | Marwin (projet propre) ; matériel « possédé par votre entité » (`deck/slides/laboratoire.html:14`) [PR] | Proposé par Marwin [PR] | Marwin ; GianLuca (cas d'usage non défini) | « Aucun […] financement du laboratoire par le client n'est acté » (STR:102) |

### 2.3 Scénarios explicites, faute de connaître les entités

| Scénario | Description | Conséquences pour le contrat | Ce qu'il faut demander |
| --- | --- | --- | --- |
| **S1. Une société unique de GianLuca commande tout** | Par exemple sa société de marchand d'art, qui commande et paie pour tous les projets | Un contrat-cadre et des fiches de mission par projet (architecture du 30 oct., V5 p. 2, perdue le 2 nov. : corr. ver-C2, omission 4). Risque : une société paie pour des projets qui profitent à d'autres entités, sous réserve de refacturation interne [HY, à faire valider par l'expert-comptable] | Dénomination, SIREN, signataire habilité, objet social, rattachement des projets |
| **S2. Plusieurs entités** | Une SCI propriétaire des murs, une ou plusieurs sociétés d'exploitation (Vieux Relais, le M, peut-être avec un associé), une structure de vente d'œuvres, une galerie | Un contrat-cadre signé par une entité « chef de file », avec des fiches de mission **par entité** et une facturation à chacune. Ou bien des contrats séparés. La capacité réservée doit être répartie par entité, pour éviter qu'une entité consomme le temps payé par une autre | Organigramme, associés de chaque entité, qui peut engager quoi |
| **S3. GianLuca signe à titre personnel** | Il signe pour ses projets patrimoniaux (catalogue privé de ses œuvres, séjours de ses invités) | Les règles applicables à un client non professionnel peuvent changer le contrat [HY, à faire valider par un avocat]. Solvabilité non démontrée. Les sociétés ne sont pas liées | Pour quels projets il agit en personne, pour lesquels via une société |
| **S4. Un tiers exploite les lieux** | Un associé ou une société dans laquelle GianLuca est investisseur exploite le Vieux Relais et le M | Le commanditaire du volet « Piloter » et des événements est ce tiers. L'accord de GianLuca ne l'engage pas. Il faut un mandat ou un contrat séparé | Identité de « l'associé » (PASS:41) et du « nous » (DPV p. 32) |
| **S5. Statu quo : personne ne paie** | Situation de fait depuis le 18 oct. : CRM, dossier du 21 oct., catalogue, études, STRATES, vernissage, tous produits sans commande [FV négatif sur les factures] | Le travail gratuit s'accumule. Propriété et responsabilité non couvertes. Risques ACRE et FRR sur la date de début d'activité (corr. ver-C2, omission 3) [HY] | Arrêter toute production nouvelle non commandée [PR] |

**Règle de prudence [PR].** Tant que les scénarios S1 à S4 ne sont pas tranchés par écrit, aucune proposition ne doit être adressée « à Carlone » en général. Elle doit nommer l'entité, le projet, le signataire et le valideur. La relation personnelle avec GianLuca ne vaut pas contrat avec ses sociétés.

### 2.4 Les rôles cumulés de GianLuca

Selon les pièces, GianLuca serait à la fois :
- **client** [DR] ;
- **bailleur** des bureaux [DR] (CTX:108 ; R:220) ;
- **employeur** possible [DR] (CTX:109 ; R:248) ;
- **investisseur** possible [DR] (CTX:24 ; OFF:132) ;
- **financeur de la R&D** [DR] (BRAS:110) ;
- et peut-être **associé de Marwin**, via la SAS « si Carlone entre au capital » [PR] (CTX:12).

Ce cumul rend Marwin entièrement dépendante d'une seule personne, avant même toute signature. La part de revenus maximale venant de lui est restée sans réponse (« 10 millions », CTX:129) [DR].

La règle « un sujet, un accord » (OFF:132) est la bonne [PR]. Elle n'est appliquée nulle part par écrit.

---

## 3. Fiches des onze chantiers

Les priorités sont notées de P0 (immédiat, avant tout rendez-vous) à P4 (gelé). Le taux de 750 € HT n'est utilisé que comme repère de calcul [ES]. Il n'est justifié ni par les coûts ni par la valeur (ex-C2 § 9.1 ; AUD:69-84 pour un repère de marché tiré d'une source secondaire).

### 3.1 CRM et développement commercial

| Rubrique | Contenu |
| --- | --- |
| **Bénéficiaire et responsable** | Bénéficiaire : la structure qui vend les œuvres [IN]. Côté Marwin : Mathys, co-auteur et seul donneur d'ordre nommé (PASS:7 ; CTX:26) [DR]. Côté client : inconnu [IN]. **Responsable de traitement non désigné** [IN] (rj-R4 (c) 3). |
| **Besoin et résultat recherché** | Vendre des œuvres aux entreprises de la Nièvre grâce à l'article 238 bis AB [DR] (COP:13 ; CAT:7). Que GianLuca vende déjà ainsi n'est pas établi (CAT:124) [IN]. Résultat attendu : des ventes. Ce n'est pas en soi un service payé à Marwin (ex-C5 § 9.14). |
| **État réel et preuves** | *Le fichier* [FV] (recomptages de ver-C5 n° 1-6 et ver-C6 n° 6) : 500 fiches et 500 SIREN, dont 485 en campagne ; 471 numéros, dont 283 « à confirmer » et une seule date de vérification ; 125 fiches d'appel ; un onglet culture de 97 prospects, dont 38 de la famille « Artistes » et 22 de type « Artiste ». |
| | *L'usage* : aucun champ de suivi n'est versionné ; le suivi vit dans un artefact ou dans le navigateur [FV] / [IN] (ver-C5 n° 7). Aucun appel, rendez-vous ni vente [DR] (COP:57), donc aucun [MM]. Livré sans facture [DR] (OFF:227 ; V5 p. 17). Objet changé le 22 oct. : des lieux vers les œuvres [FV] (PASS:5, 43, 49 ; corr. ver-C9 n° 7). |
| | *La technique* : version Firebase non configurée dans le dépôt [FV] (`crm/autonome/public/config.js:6-9`) ; déploiement [IN]. Export et import Hermes360 codés [FV], raccordement réel [IN] (corr. ver-C6 n° 7). |
| | *Le calcul fiscal* : l'« économie max » ignore le bénéfice et le taux réduit des PME (`crm/art_merge.py:19, 129`). 58 des 485 fiches en campagne ont un plafond supérieur à leur bénéfice [FV] (corr. ver-C5 n° 9). |
| | *Les oppositions* : les entreprises opposées sur Pappers restent appelables, par choix délibéré (PASS:22) [FV] (ver-C5, omission 1). |
| | *Les données exposées* : dépôt FinanceScope public au 4 nov. à 16:19 [DR] (CTX:5, 11). Copie dans `crm/` (commit 95de15f) [FV]. Entre 800 et 940 numéros selon la méthode de comptage, 206 e-mails, environ 86 à 89 profils LinkedIn [ES] (corr. ver-C5 n° 15). |
| **Livrables** | Existants : le CRM (site, version Firebase, exports), le rapport du 29 oct. (RAP), le catalogue de neuf offres (CAT:38-50) [PR]. |
| | Proposés : « premier lot commercial exploitable », 7 journées-personnes au mois 1 (OFF:59) [PR] ; lot de consolidation : dictionnaire de données, registre d'enrichissement, spécification d'échange, recette sur 10 fiches fictives, prix non fixé (`sources/chatgpt-pages/2026-11-04-complement/audit-crm-carlone.md:58-64`) [PR] ; démarrage sur 20 comptes (COP:57) [PR] ; fiches Offre, Œuvre et Vente avec alertes sur cinq ans (CAT:85-89) [PR]. |
| **Données, accès, compétences** | *Données à obtenir* : nom de la structure vendeuse ; œuvres, artistes et prix (CAT:52) [IN] ; avis fiscal écrit (CAT:13 ; exposition en lieu tiers « non explicitement prévue » par le BOFiP, CAT:99 et PASS:35) [DR] ; responsable de traitement, registre et analyse de l'intérêt légitime (rj-R4). |
| | *Compétences* : production de données et de code démontrée, mais par des agents IA. Les 48 commits sont signés « Claude » et la relecture humaine n'est pas tracée [FV]. Exécution commerciale non démontrée (ex-C6 § 9-B, verdict). |
| **Budget** | Aucun budget identifié [IN]. Proposé : 7 journées-personnes × 750 € = 5 250 € HT au mois 1, à l'intérieur du forfait [ES]. Développements « à ajouter » sans financeur [IN]. |
| **Coûts et dépendances** | Maintenance non chiffrée : 645 fichiers, chaîne de scripts au README incomplet, données qui vieillissent, quotas d'agents IA (ex-C5 § 9.9) [ES qualitative]. Offre gratuite de Firebase pour 2 à 4 associés [ES] (RAP:18). |
| | Dépendances : structure vendeuse ; validation fiscale ; décision sur Quali Contact ; traitement de la violation de données. |
| **Risques** | RGPD : violation probable, mobiles et messageries personnelles d'artistes, oppositions ignorées. |
| | Argument fiscal surévalué : responsabilité envers les acheteurs ; risque de basculer dans le régime des biens divers (CAT:97). |
| | Loyauté commerciale : le lieu d'exposition est tu aux prospects (PASS:49). |
| | Propriété floue : code chez Mathys, copie chez Morgan, « votre CRM » dit au client (`deck/slides/livre.html:4` ; OFF:37, 281). |
| | Si Marwin est rémunérée sur les ventes, elle peut devenir intermédiaire au sens de la LCB-FT et redevable du droit de suite (rj-R5 (a)) [HY]. |
| **Critères de réception [PR]** | 1. Dépôt rendu privé, violation documentée, décision de notification tracée. 2. Responsable de traitement désigné par écrit ; registre ouvert. 3. Simulateur corrigé (bénéfice réel, taux PME). 4. Structure vendeuse saisie ; textes validés par le conseil de GianLuca. 5. Pilote de 20 comptes : taux de joignabilité, de rendez-vous et de refus **mesurés** [MM]. 6. Export restituable et restauration testée. |
| **Priorité et prochaine décision** | **P0 pour la conformité**. Cette remise en ordre est de notre fait et ne doit **pas** être facturée [PR]. **P1 pour le pilote commercial.** |
| | Décision immédiate (Mathys et Morgan, avec un avocat) : qualifier la violation, la documenter et décider de la notification à la CNIL avant le 5 nov. si la connaissance date du 2 nov. (rj-R4 (c) ; ver-R4 n° 7). Si l'entité de GianLuca est responsable de traitement, elle doit être informée sans délai [HY]. |
| | Décision suivante (GianLuca) : veut-il exploiter ce CRM, au nom de quelle structure, et qui appelle ? |

### 3.2 Coordination avec Quali Contact

| Rubrique | Contenu |
| --- | --- |
| **Bénéficiaire et responsable** | Entité vendeuse [HY] ; commanditaire supposé de Quali Contact : GianLuca [DR]. Marwin coordonnerait [PR]. Interlocuteur chez Quali Contact : [IN]. |
| **Besoin et résultat recherché** | « Le client prévoit d'engager Quali Contact » (COP:7, message de Morgan du 25 oct.) [DR]. Résultat visé : des campagnes d'appels avec des offres validées, et le retour des résultats d'appel, des rendez-vous et des oppositions dans le CRM (COP:20-49) [PR]. |
| **État réel et preuves** | Aucun contrat vu. Logiciel, module et formats inconnus [IN] (COP:51, 69 ; `sources/crm-reference-2026-11-04.md:12`). Les pages publiques de Qualicontact décrivent des campagnes et de la « relation donateurs » [DR] (COP:51). |
| | Cahier de raccordement proposé, aucun test exécuté [PR] (COP:38-49). Module Hermes360 développé sur une hypothèse non vérifiée (commits 1d7f97d, bb9d5e2, 20a3a8e) [FV]. |
| | **Quali Contact a disparu** de l'offre du 2 nov. et du contexte du 4 nov. : aucune occurrence de « Quali » dans OFF ni dans CTX [FV] (ver-C10, omission 1). |
| **Livrables** | Spécification d'échange dans les deux sens ; fiches d'offre versionnées pour les opératrices ; essai sur données fictives (COP:20-30 ; `sources/crm-reference-2026-11-04.md:12`) [PR]. |
| **Données, accès, compétences** | Modèle de fichier d'import et de retour ; contrat de sous-traitance RGPD entre l'entité vendeuse et Quali Contact ; scripts validés par le conseil ; accès de test. Compétence d'intégration de fichiers démontrée [FV : code d'export et d'import]. |
| **Budget** | Inconnu des deux côtés [IN]. Rien n'est prévu dans l'offre du 2 nov. |
| **Coûts et dépendances** | Contrat entre GianLuca et Quali Contact ; conformité du CRM ; structure vendeuse ; arbitrage avec la « campagne pilote » de 7 journées-personnes (OFF:59). |
| **Risques** | Double emploi avec la campagne pilote de Marwin [HY] (corr. ver-C1 n° 22). Développer un connecteur avant de connaître le format, comme avec Hermes360. Être responsable de fait d'un prestataire qu'on ne contracte pas. Appeler des entreprises opposées à la prospection (PASS:22). |
| **Critères de réception [PR]** | Fichier d'essai importé chez Quali Contact, puis résultats réimportés sans perte sur 10 fiches fictives. Correspondance des champs validée par écrit par Quali Contact. Liste d'opposition appliquée. |
| **Priorité et prochaine décision** | **P1, conditionnelle.** Décision de GianLuca : Quali Contact est-il engagé (contrat, outil, périmètre, payeur) ? Faute de réponse, le chantier reste en attente et rien n'est développé. |

### 3.3 Organisation et pilotage des projets

| Rubrique | Contenu |
| --- | --- |
| **Bénéficiaire et responsable** | GianLuca et ses « établissements », non identifiés [IN]. Côté Marwin : Morgan (programme, prix, coordination) [DR] (CTX:25). Valideur côté client : inconnu [IN] (OFF:272). |
| **Besoin et résultat recherché** | « Déléguer le quotidien », « ne pas gérer chaque détail » [DR] (COP:65 ; ACC:7, 11). Résultat visé : une vision claire, des décisions préparées, des résultats vérifiables (DEMANDE § 2 ; OFF:23) [PR]. |
| **État réel et preuves** | Huit missions proposées le 18 oct. (PROP p. 1) [PR], sans réponse connue [IN]. Offre de six mois à 15 000 ou 30 000 € HT par mois (OFF:13-16) [PR]. Rien n'est signé [FV négatif]. |
| | Les disponibilités ne sont pas tranchées : « le temps que chacun peut réellement donner » reste ouvert (CTX:120 ; OFF:128) [DR]. |
| | Aucun établissement identifié, donc « Piloter » n'a pas d'objet vérifiable (ex-C9 § 9.1) [FV négatif]. Aucun [MM]. |
| **Livrables** | Proposés : inventaire des projets et des accès de J1 à J10 ; feuille de route à 90 jours avec budgets ; tableau de bord ; revues à 30 et 90 jours (ACC:25 ; R:1026-1032) [PR]. Premier mois : 6 journées-personnes de cadrage et 3 de coordination (OFF:58, 61) [PR]. Mandat écrit avec plafonds (ACC:94-103) [PR]. Forfait de cadrage borné du 25 oct. (R:1469) [PR]. |
| **Données, accès, compétences** | Liste des entités et des lieux ; encaissements, trésorerie et factures des établissements (la mission 1 suppose des « responsables » et un « comptable » : PROP p. 1 [HY]) ; contrats ; agendas ; interlocuteurs. |
| | Compétences : préparation documentaire démontrée [FV], sous forme de dossiers et d'études produits avec des assistants IA. Pilotage opérationnel chez un client : non démontré [IN]. La frontière avec l'expertise comptable (mission 1) et la réglementation des séjours (mission 7) est à vérifier [IN] (ex-C2 Q19). |
| **Budget** | Côté client : inconnu [IN]. Proposé : 9 journées-personnes au mois 1, soit 6 750 € HT [ES], dans un forfait de 15 000 € HT [PR]. L'aide régionale au conseil est à examiner, avec un dépôt avant signature [DR] (R:755, 809). |
| **Coûts et dépendances** | Déplacements et présence à Cosne-Cours-sur-Loire non chiffrés. Disponibilité réelle de Morgan : 91 artefacts et plusieurs clients en parallèle (NOTE:9-17) [FV pour la dispersion]. Disponibilité de Mathys inconnue [IN]. Société non immatriculée [DR] (OFF:153). |
| **Risques** | Un abonnement qui absorbe développements, événements et urgences (DEMANDE § 4). L'astreinte « chiffrée à part » a disparu le 2 nov. (ex-C2 C23). Des responsabilités plus larges que les pouvoirs, sans mandat. |
| | La réception tacite « réputé accepté » (OFF:206) contredit « une absence de réponse ne vaut pas approbation » (ACC:103). |
| | Les tâches administratives peuvent être comparées au coût d'un assistant (AUD:83) [DR]. À 15 000 € par mois pour environ un équivalent temps plein, l'offre équivaut au coût d'un salarié payé environ 7 900 à 9 400 € nets par mois (ex-C2 § 9.1) [ES]. Forte dépendance à Morgan. |
| **Critères de réception [PR]** | Inventaire des entités, lieux, projets, interlocuteurs et accès, **validé par écrit par GianLuca**. Feuille de route à 90 jours : trois priorités choisies par lui, budget par projet. Registre des décisions daté. Tableau de bord mis à jour à date fixe. Mandat écrit avec plafonds unitaires et cumulés. |
| **Priorité et prochaine décision** | **P0 sous forme de cadrage court et payé.** Un pilotage récurrent ne vient qu'après, si le cadrage confirme le besoin. Décision de GianLuca : cadrage seul, cadrage plus suivi borné, ou lots ponctuels ; et quelle entité signe. |

### 3.4 Jarvis, mémoire documentaire et automatisations

| Rubrique | Contenu |
| --- | --- |
| **Bénéficiaire et responsable** | GianLuca (« votre Jarvis », ACC:17) [PR]. Responsable : Morgan, qui « construit Jarvis » (CTX:25) [DR]. **Propriétaire du nom et du code inconnu** [IN] : « Medhi apporte… Jarvis » (OFF:90) ; « Jarvis conserve son propriétaire » (STR:22) (ex-C2 C10). |
| **Besoin et résultat recherché** | Retrouver les informations, suivre les actions et les échéances, préparer des synthèses, automatiser après vérification (ACC:17) [PR]. Mission 3 : « automatiser les rappels et le classement » (PROP p. 1) [PR]. Aucun besoin exprimé par le client [IN]. |
| **État réel et preuves** | Jarvis M07 appartient au dépôt public BOJART. Il n'est ni installé ni qualifié sur la tour (`BOJART:jarvis/README.md:14`) [FV] (ver-C7 n° 1). Aucune licence n'est concédée sur son code (corr. ver-C7 n° 10). |
| | La console « Offres et missions » passe 33 tests sur données fictives, sans modèle d'IA [DR] (STR:120-122 ; corr. ver-C10 : [DR] et non [MM]). Le gain de productivité n'est pas mesuré ; −30 % n'est qu'une cible [HY]. |
| | Une « tour de contrôle » est hébergée sur chatgpt.site ; son contenu et son niveau d'accès sont inconnus [IN] (ver-C1, omission 3). |
| | Au mois 1, un démonstrateur de 4 journées-personnes, **inclus dans le forfait** et non dans l'option laboratoire (OFF:60, 65 ; corr. ver-C8 n° 9) [PR]. |
| **Livrables** | Démonstrateur sur un périmètre autorisé : recherche documentaire, suivi des actions, journal, arrêt, retour au fonctionnement manuel (ACC:109-113) [PR]. |
| **Données, accès, compétences** | Corpus de documents de GianLuca, avec autorisation et règles d'accès. Compétence logicielle démontrée dans un autre contexte : 578 tests M07 réussis dans le dépôt BOJART [MM côté BOJART] (ver-C7 n° 3). Une licence commerciale n8n serait nécessaire si le client configure lui-même les automatisations (R:1384) [DR]. |
| **Budget** | 4 journées-personnes, soit 3 000 € HT [ES], dans le forfait. Coûts récurrents d'IA et d'hébergement non inclus (ex-C2 C12) [IN]. DGX Spark : besoin « pas établi » (ACC:131 ; LABO p. 9) [DR]. |
| **Coûts et dépendances** | Abonnements d'IA : ceux de Morgan sont en échec de prélèvement (NOTE:8) [DR]. Maintenance. Le code dépend de BOJ.ART, retiré de l'offre le 4 nov. |
| **Risques** | Propriété du code. Instructions malveillantes cachées dans les documents. Données du client versées dans un dépôt public. Vendre un « multiplicateur » de productivité non mesuré, alors que l'audit du laboratoire recommande de « chronométrer nos propres tâches, corrections comprises, au lieu de vendre un multiplicateur général de productivité » (LABO p. 6) [DR] (ver-C8, omission 1). |
| **Critères de réception [PR]** | Sur un jeu de questions réelles tiré des documents de GianLuca, taux de réponses sourcées et correctes au moins égal à un seuil fixé **avant** l'essai. Temps de préparation d'une réunion mesuré avant et après, corrections comprises [MM]. Export et restauration testés. |
| **Priorité et prochaine décision** | **P2.** D'abord un essai mesuré en interne sur un processus de Marwin. Décision des associés : qui possède « Jarvis » (Marwin ou BOJ.ART) ? Faut-il renommer l'outil avant de le promettre au client ? |

### 3.5 Marketing, communication, contenus et supports commerciaux

| Rubrique | Contenu |
| --- | --- |
| **Bénéficiaire et responsable** | Structure vendeuse, galerie, lieux [IN]. Responsable : inconnu [IN] ; Morgan se dit « studio marketing » (R:220) [DR]. |
| **Besoin et résultat recherché** | Aucune demande précise du client [IN]. « Studio marketing » est le positionnement proposé pour Marwin (R:237) [PR] (corr. ver-C1 n° 16). Mission 5 : site, cartes, horaires, réservations (PROP p. 1) [PR]. Fiches d'offre pour les opératrices (COP:20-30) [PR]. Textes de vente validés (CAT:85) [PR]. |
| **État réel et preuves** | Diaporamas : offre en 11 diapositives et vernissage en 12 pages [FV]. Visuels générés par IA, « non contractuels » (`deck/slides/cover.html:5`) [FV]. Le dossier de Mathys prévoit messages, script, identité imprimée et presse (DPV p. 3, 5, 29, 32-33) [PR]. Rien n'a été vendu ni publié (R:1513-1515) [DR]. |
| **Livrables** | Fiches d'offre ; cartels et information du public, qu'exige l'exposition prévue par l'article 238 bis AB (CAT:27) ; modèles de mails conformes ; supports de réouverture des lieux ; contenus de la galerie [PR]. |
| **Données, accès, compétences** | Charte graphique. Autorisations écrites des artistes pour toute reproduction de leurs œuvres (CPI L131-3, rj-R5 (b)). Identité de l'émetteur. Production démontrée [FV], mais les droits commerciaux des médias générés par IA ne sont pas vérifiés (`bojart/docs/research/strates-robotique-2026-11-02/README.md:11`) [FV]. |
| **Budget** | Inconnu [IN]. Pas de lot distinct. Publicité hors forfait (OFF:20). |
| **Coûts et dépendances** | Crédits des outils de génération [IN]. Structure vendeuse. Arbitrage entre trois discours incompatibles : lieux nommés aux entreprises (DPV p. 32), lieux tus aux entreprises (CAT:52), lieux nommés aux artistes (CRM, onglet culture) (ver-C6, omission 1). |
| **Risques** | Promesse implicite : « vendre vos œuvres avec le CRM » (`deck/slides/proposition.html:3`) (ex-C2 C16). Visuels IA pris pour la réalité. Erreur d'identité dans un document destiné au client : « Proposition d'accompagnement pour John-Lucas Carlone » [sic, lire GianLuca] (V5 p. 1) (ver-C2, omission 5). |
| **Critères de réception [PR]** | Chaque support validé par GianLuca, et par son conseil pour la fiscalité. Mentions obligatoires présentes. Droits documentés. |
| **Priorité et prochaine décision** | **P2, par lots devisés.** Décision de GianLuca : quel discours tenir aux entreprises (les lieux ou les œuvres), et quelle entité émet les messages ? |

### 3.6 Galerie, vente d'œuvres et relations avec les artistes

| Rubrique | Contenu |
| --- | --- |
| **Bénéficiaire et responsable** | Galerie ou structure vendeuse [IN]. Responsable : GianLuca, comme marchand [DR]. |
| **Besoin et résultat recherché** | Galerie en 2027 (CAT:9) dans un ancien bar-restaurant-hôtel avec cour (COP:14) [DR]. Ventes aux entreprises [DR]. Mission 6 : catalogue privé des œuvres (PROP p. 1) [PR]. |
| **État réel et preuves** | Aucun artiste engagé, aucune œuvre en stock, aucun prix [IN] (CAT:52). Catalogue de neuf offres à l'état de brouillon, dont une seule intégrée au CRM (CAT:38-50) [PR]. |
| | Article 238 bis AB jusqu'au 31 déc. 2028 : [DR], à valider (CAT:17). Œuvres faites à la machine « très probablement » exclues [HY] (CAT:98, 106-110). |
| | Vivier : 22 artistes individuels, et non « 97 artistes » (corr. ver-C6 n° 6). |
| **Livrables** | Catalogue privé : fiches, photos, emplacements, mouvements [PR]. Conventions de dépôt-vente, rédigées par l'avocat de l'entité (rj-R5 (b)) [PR]. Champs du registre, alerte LCB-FT et calcul du droit de suite dans le CRM (rj-R5 (a)) [PR]. |
| **Données, accès, compétences** | Inventaire des œuvres avec leur provenance ; contrats d'artistes ; conseil fiscal. |
| | Obligations de l'exploitant [FV] (rj-R5 (a) ; ver-R5 n° 1-6) : registre des objets mobiliers, qui incombe aux dirigeants si le vendeur est une société (C. pén. art. 321-7) ; LCB-FT dès 10 000 € (CMF L561-2, 10°) ; droit de suite (CPI L122-8) ; facture conforme au décret n° 81-255 ; contribution des diffuseurs de 1 % + 0,1 %, avec déclaration avant le 1er mai, même à néant. |
| **Budget** | Inconnu [IN] : acquisitions, aménagement de la galerie, assurances. |
| **Coûts et dépendances** | Lieu ; entité vendeuse ; conseil fiscal ; assurance « clou à clou », pratique de marché non obligatoire [HY]. |
| **Risques** | Marwin intermédiaire, avec les obligations LCB-FT et la charge du droit de suite (R122-9), si elle touche une commission ou encaisse (rj-R5 (a)) [HY]. Marwin dépositaire si elle garde ou transporte des œuvres [HY]. |
| | Prix calé sur le plafond fiscal du client (CAT:42). Exposition chez le vendeur (CAT:99). Attestation fiscale de l'offre 4 : qui la signe en répond (CAT:45). Conflit d'intérêts de Morgan avec BOJ.ART (ex-C6 § 9-A.11). |
| **Critères de réception [PR]** | Catalogue privé de N œuvres **réelles**, aux fiches complètes et exportables. Offres validées par écrit par le conseil fiscal. |
| **Priorité et prochaine décision** | **P1 pour le catalogue privé**, livrable concret et peu risqué, s'il existe des œuvres. **P3 pour la galerie 2027.** Décision de GianLuca : quelles œuvres, quels artistes, quelle entité vend, quel conseil. |

### 3.7 Événements et vernissage

| Rubrique | Contenu |
| --- | --- |
| **Bénéficiaire et responsable** | GianLuca et la galerie. **Organisateur légal : l'entité de GianLuca ou l'exploitant du lieu** (rj-R5 (d)) [PR]. Côté Marwin : Morgan [DR]. |
| **Besoin et résultat recherché** | « Réunir des artistes et peintres dans la ville de Morgan » (COP:16) [DR]. Mission 8 : événements associant art et restauration (PROP p. 1) [PR]. Le vernissage « Strates » est une proposition de Marwin, **pas un besoin exprimé** (ex-C9 § 9.2). |
| **État réel et preuves** | Vernissage : cinq temps, 21 idées, trois formats de 6 à 30 journées-personnes, soit 4 500 à 22 500 € HT d'honoraires [PR] / [ES] (IDEES:98-102 ; VERN p. 10). Lieu, date, jauge et budget inconnus [IN] (IDEES:123-125). |
| | Il dépend du parc et de l'accord de Medhi (IDEES:100, 122), et cet accord n'est pas obtenu [IN]. Le diaporama cite encore BOJ.ART et Medhi (VERN p. 1, 6, 7, 9 et 12) [FV, texte relu]. |
| | Les formats sont « sans supplément s'ils tiennent dans les 20 journées » (IDEES:110 ; VERN p. 11), mais une option facturable existe et aucun critère ne définit un mois « plein » (corr. ver-C9 n° 11). |
| | **Une alternative existe déjà** : le plan culture du CRM (10 formats, 20 dates, 23 règles pratiques, 13 idées nommant le Vieux Relais) (`crm/site/culture.json:2881-3325`) [FV pour l'existence ; PR pour le contenu ; DR pour les règles] (ver-C9, omission 1). |
| **Livrables** | Étude de faisabilité et budget d'un premier événement **sans robot** ; liste des démarches par lieu, avec calendrier ; dossiers à signer par l'organisateur [PR]. |
| **Données, accès, compétences** | Lieu, jauge, classement ERP. Obligations de l'organisateur [FV] (rj-R5 (d) ; ver-R5 n° 8-10) : demande GN 6 **deux mois avant** une manifestation inhabituelle ou une démonstration ; boissons (débit temporaire ou licence) ; Sacem et Spré ; spectacles (jusqu'à 6 représentations par an sans déclaration) ; artistes présumés salariés (Guso). L'appellation « enchères » est réservée aux opérateurs habilités (rj-R5 § 0.3) [FV partiel]. |
| **Budget** | Honoraires estimés [ES]. Tout le reste (hors honoraires) est inconnu [IN]. |
| **Coûts et dépendances** | Présence sur place : deux personnes un soir valent deux journées-personnes. Déplacements. Dossiers. Délai d'au moins deux mois : pas d'événement public en décembre 2026 dans un lieu non autorisé [ES] (ver-R5 n° 9). |
| **Risques** | Absorption par le forfait. Données des invités envoyées via un CRM exposé. Robot au contact du public : la norme ISO 10218-2:2025 ne couvre pas le public (ver-R5). Enchères. Dépendance à Medhi. Promesse d'une « première présentation » de STRATES (VERN p. 7) sans financement. |
| **Critères de réception [PR]** | Dossier de faisabilité validé par GianLuca : lieu, date, jauge, budget, organisateur désigné, autorisations listées avec leurs dates de dépôt, devis. |
| **Priorité et prochaine décision** | **P2, en lot séparé.** Format « signature » avec bras robotisé : **reporté**. Décision de GianLuca : quel événement, pour quel objectif mesurable (ventes, adhésions), dans quel lieu ? |

### 3.8 Cabaret et autres lieux (Vieux Relais, le M, « six bâtiments »)

| Rubrique | Contenu |
| --- | --- |
| **Bénéficiaire et responsable** | Propriétaire et exploitant inconnus [IN]. Le responsable doit être l'exploitant légal [HY]. |
| **Besoin et résultat recherché** | Racheter le M pour un cabaret (COP:15) [DR]. Rouvrir le Vieux Relais et le M après travaux (DPV p. 3, 5, 23, 29) [DR]. Missions 1 et 5 : suivi des établissements, outils après chaque rachat (PROP p. 1) [PR]. |
| **État réel et preuves** | Aucun lieu n'est établi [FV négatif]. Le Vieux Relais est vraisemblablement un bar avec hôtel ; le M est restaurant ou bar selon la pièce (corr. ver-C9 n° 5). Repreneur non nommé (DPV p. 32 ; PASS:41). |
| | Cabaret : « peut-être », « plus tard » (CTX:24, 60). Dossier de Mathys de 34 pages, dont le plan d'action n'a pas été exécuté (cases vides, DPV p. 33) [FV]. Le cabaret disparaît de l'offre du 2 nov. (ex-C2 C17) [FV]. |
| **Livrables** | Dossier de faisabilité opérationnelle, payé à part (ACC:42 ; rj-R5 (e)) [PR]. Inventaire des lieux, dans le cadrage [PR]. Calendrier des démarches [PR]. |
| **Données, accès, compétences** | Actes, baux, licences, classement ERP, jauges. Obligations **nominatives** de l'exploitant [FV] (rj-R5 (e) ; ver-R5 n° 8, 10) : on ne peut plus créer de licence IV ; permis d'exploitation (20 heures de formation) ; récépissé d'entrepreneur de spectacles ; cabaret de type L, en 5e catégorie jusqu'à 50 personnes ; formation à la sécurité ; limites des sons amplifiés. Marwin ne peut pas porter ces autorisations [HY]. |
| **Budget** | Acquisitions, travaux et fonctionnement inconnus [IN]. |
| **Coûts et dépendances** | Tout dépend de la propriété et de l'exploitant. Présence locale requise. |
| **Risques** | Parler au nom d'un repreneur non désigné, sans mandat (« Nous reprenons », DPV p. 32). S'engager sur des dates (« Il reste des dates en décembre », DPV p. 32). Absorber le cabaret dans un « Piloter » sans objet. Porter des responsabilités d'exploitant. |
| **Critères de réception [PR]** | Inventaire des lieux validé par écrit. Tableau des obligations par lieu, validé par des professionnels (mairie, commission de sécurité, avocat). |
| **Priorité et prochaine décision** | **P1 pour l'inventaire des lieux**, dans le cadrage. **P3 pour le cabaret.** Décision de GianLuca : liste des lieux, propriétaire, exploitant, calendrier ; le cabaret est-il toujours d'actualité ? |

### 3.9 Collaboration avec Medhi et BOJ.ART

| Rubrique | Contenu |
| --- | --- |
| **Bénéficiaire et responsable** | Medhi et BOJ.ART ; la galerie de GianLuca [PR]. Responsable : Morgan, qui « orchestre BOJ.ART » (CTX:25) [DR]. |
| **Besoin et résultat recherché** | Aucun besoin de GianLuca exprimé pour cette collaboration [IN]. Lien préexistant : GianLuca aurait racheté « l'ancienne affaire de Medhi » [DR] (CTX:24). |
| **État réel et preuves** | **Retrait oral du 4 nov.** [DR] (NOTE:25). Diaporama client corrigé [FV] (`deck/deck.json:7`). Aucun accord écrit avec Medhi, à aucune date [IN] (OFF:226). On ignore si Mathys et Medhi sont informés [IN]. Le rôle de Morgan dans BOJ.ART est ambigu (ACC:21 contre OFF:90) [DR]. |
| | **Pièces non mises en cohérence** [FV] : |
| | 1. OFF:22 et 67-101 : section « Créer des œuvres… », qui n'est pas marquée « interne ». |
| | 2. STRv11, signé « BOJ.ART / Marwin Tech ». |
| | 3. VERN p. 1 (« Marwin Tech et BOJ.ART »), p. 6, 7 et 9 (Medhi), p. 12 (« avec Medhi, BOJ.ART »). |
| | 4. IDEES:20-22, 57, 100 et 122. |
| | 5. `pour-carlone/strates/bras-robotique-concept-ia-10s.mp4` et `relief-mineral-bleu-galerie.png`. |
| | 6. Branche de la PR n° 1 : le PDF de l'offre en **13 diapositives** et les JPG `08-strates` et `09-strates-phases`. |
| | 7. `README.md:3, 18` et CAT:104-113. |
| | 8. Côté BOJ.ART : tâche `strates-g0`, ouverte, en priorité 1 (`bojart/ops/orchestration.json:443-456`). |
| | 9. L'option laboratoire, maintenue, dont le geste robotique était le premier trait de STRATES (OFF:84) (ver-C2, omission 2). |
| **Livrables** | Pour GianLuca : aucun après le 4 nov. En interne [PR] : inventaire des documents à retirer, suspendre ou réécrire ; décision écrite et partagée avec Mathys ; échange écrit avec Medhi sur ce qui lui a été dit ou promis (exclusivité, films). |
| **Données, accès, compétences** | Sans objet. |
| **Budget** | Aucun. La phase 1 de STRATES (environ 10 000 € HT) est retirée [PR, retirée]. |
| **Coûts et dépendances** | Perte de l'accès présumé à environ dix imprimantes 3D, probablement le parc de Medhi [HY] (corr. ver-C2 n° 11). Effets sur le format 1 du vernissage, sur Éclosion et sur le laboratoire. Le code de Jarvis reste dans le dépôt BOJART. |
| **Risques** | Documents destinés au client contradictoires entre eux : jusqu'à trois versions de l'offre. Promesses faites à Medhi non tenues. STRATES classé comme recherche de BOJ.ART : c'est le rattachement fait par l'utilisateur du dépôt, et un risque de revendication [HY] (corr. ver-C8 n° 12). Conflit d'intérêts non déclaré au client. Relation préexistante entre GianLuca et Medhi, donc sujet sensible. |
| **Critères de réception [PR]** | Tous les documents destinés au client concordent avec la décision. La décision est écrite et validée par Mathys. La PR n° 1 est fermée, mise à jour, ou son PDF est marqué « historique ». |
| **Priorité et prochaine décision** | **P0 : mise en cohérence avant tout rendez-vous.** Décision de Morgan et Mathys : retrait définitif ou suspension ? Qui informe Medhi, et sous quelle forme ? |

### 3.10 STRATES, Éclosion et autres créations

| Rubrique | Contenu |
| --- | --- |
| **Bénéficiaire et responsable** | La galerie de GianLuca, à qui seraient promises la première présentation et une exclusivité [PR]. Financeur supposé : « serait Carlone » (BRAS:110) [DR, une seule phrase]. Responsable : Morgan (jalon G0 « Morgan + artiste ») [PR]. |
| **Besoin et résultat recherché** | Aucun besoin exprimé par GianLuca [IN]. STRATES apparaît après le message « Carlone vend des œuvre d'art il est moins figurine » (BRAS:90) [DR] (corr. ver-C8 n° 3). |
| **État réel et preuves** | Rien n'est fabriqué ni mesuré (STRv11 p. 1 et 4), selon une auto-déclaration [DR]. Pas de budget propre : les 323 875 € sont un « ancien scénario » de peinture de figurines (STRv11 p. 4). |
| | Les « 10 000 € » de la phase 1 reprennent le P0 du programme de figurines, sans bras (`interne/strates/archives-investisseur/budget-v1-2026-11-02.xlsx`, feuille Depenses, A7:F11) [FV] (ver-C8 n° 5). |
| | La revue robotique n'est pas indépendante : elle sort du même outil, environ 1 h 35 après les documents qu'elle juge (corr. ver-C8 n° 1). Depuis le 4 nov., plus d'artiste. |
| | Éclosion : CAO de prototype P0, aucune pièce, aucun achat, `hardware_validation: false` (`interne/eclosion/prototype-p0/calculs_et_controles.json:98`) [FV]. Le concept ne nomme jamais GianLuca (corr. ver-C8 n° 15). |
| | Retour sur investissement du programme de figurines : environ 35 à 44 ans [ES] (corr. ver-C8 n° 11). |
| **Livrables** | STRATES v1.1 (8 p.), concept Éclosion (5 p.), pack CAO P0, vidéos générées par IA. Rien n'est facturé. |
| **Données, accès, compétences** | Bras, intégrateur, métrologie, artiste : aucun identifié. « Compétences démontrées, pas présumées » (LABO p. 5) [DR]. Aucune compétence d'intégration robotique démontrée. |
| **Budget** | STRATES : inconnu [IN]. Éclosion P0 : 6 journées-personnes, soit 4 500 € HT hors pièces [ES] (`pour-carlone/eclosion/concept-2026-10-31.pdf` p. 5). Un test STRATES de six semaines coûterait environ 9 000 à 19 500 € HT, hors bras [ES] (ex-C8 § 9.4). |
| **Coûts et dépendances** | Temps passé et crédits d'IA non comptés [IN]. Régime du fabricant : règlement (UE) 2023/1230 au 20 janv. 2027 ; directive (UE) 2024/2853 pour les produits mis sur le marché après le 8 déc. 2026 [FV] (corr. ver-R5 n° 11-12). |
| **Risques** | Aucune valeur fiscale pour les entreprises [HY]. Droits de l'artiste et des médias générés par IA. Confidentialité : résumé de STRATES publié dans le dépôt public BOJART. Occupation de l'unique place exploratoire (LABO p. 1, 10). |
| **Critères de réception [PR]** | Aucun pour le client aujourd'hui. Conditions de toute reprise : financeur écrit, budget plafonné, artiste sous contrat, banc fermé sans public. |
| **Priorité et prochaine décision** | **P4, gelé.** Décision de GianLuca : a-t-il un intérêt écrit ? Sinon, archiver. |

### 3.11 Laboratoire IA et robotique

| Rubrique | Contenu |
| --- | --- |
| **Bénéficiaire et responsable** | Projet propre de Marwin (ACC:121-123 ; STR:98-102), devenu une option payée par le client (OFF:21, 65) [PR]. Responsable : inconnu [IN]. |
| **Besoin et résultat recherché** | Souhaits de Morgan : DGX Spark (R:220), laboratoire « en parallèle » (R:1330) [DR]. Cas d'usage pour GianLuca non défini : « un cas d'IA lié à vos projets » [IN]. |
| **État réel et preuves** | Option à 30 000 € HT : 13 500 € d'honoraires (18 journées-personnes) et 16 500 € d'achats possédés par l'entité de GianLuca (OFF:21 ; LABO p. 8) [PR]. |
| | Toujours présente dans le diaporama en vigueur (`deck/slides/laboratoire.html:9-14`) [FV]. Envoi au client : [IN] (corr. ver-C8 n° 8). |
| | Son « geste robotique simple » était le premier trait de STRATES (OFF:84) : **il n'a plus d'objet** depuis le 4 nov. |
| | Selon l'audit du 31 oct. : ni atelier, ni équipe, ni paiement ; poste de calcul à 10 000 € « pas un besoin démontré » (LABO p. 1-2, 9) [DR]. |
| | L'ancre de négociation demande 46 journées-personnes par mois, pour 40 théoriques (OFF:246) [ES]. |
| **Livrables** | Un cas d'IA, puis un geste robotique sur un banc d'essai (OFF:65) [PR]. |
| **Données, accès, compétences** | Station de calcul, intégrateur, assurance. Aucune compétence robotique démontrée [IN]. |
| **Budget** | 30 000 € HT proposés. Financement non validé [DR]. CIR et CII non acquis (LABO p. 9) [DR]. |
| **Coûts et dépendances** | Matériel, maintenance, sauvegarde [IN]. Capacité déjà dépassée. |
| **Risques** | La R&D financée par le client absorbe la marge. Marwin pourrait devenir fabricant. Promesse sans objet depuis le retrait de STRATES. |
| **Critères de réception [PR]** | Aucun tant qu'aucun usage n'est démontré. |
| **Priorité et prochaine décision** | **P4, gelé.** Décision de Morgan et Mathys avant tout rendez-vous : **retirer la diapositive**, ou la remplacer par un essai d'IA documentaire sans robot, rattaché au chantier 3.4. |

---

## 4. Classement : ce qui finance, ce qui consomme, ce qui sort du périmètre

### 4.1 Activités qui peuvent financer Marwin, sous conditions

| Activité | Chantiers | Conditions préalables | Repère de volume [ES] |
| --- | --- | --- | --- |
| **A. Cadrage initial au forfait.** C'est aussi le test du besoin | 3.3 et 3.8 (inventaire des lieux) ; entités (§ 2) | Entité signataire identifiée ; Marwin immatriculée, ou structure de facturation tranchée ; séquence de l'aide régionale vérifiée | 6 à 10 journées-personnes, prix à justifier par les coûts |
| **B. CRM : pilote commercial et consolidation**, après une mise en conformité non facturée | 3.1 | Structure vendeuse ; avis fiscal écrit ; responsable de traitement ; dépôt privé ; décision sur Quali Contact | Environ 7 journées-personnes pour le pilote de 20 comptes ; maintenance à chiffrer à part |
| **C. Coordination de Quali Contact** (spécification et essai) | 3.2 | Contrat entre GianLuca et Quali Contact ; outil et format connus | À chiffrer après réception du modèle de fichier |
| **D. Pilotage récurrent borné** (tableau de bord, registre des décisions, coordination des prestataires) | 3.3 | Cadrage accepté et payé ; mandat écrit ; accès fournis ; capacité réelle des associés établie | Volume à dimensionner sur l'inventaire. Les 20 journées-personnes actuelles ne reposent sur aucun dimensionnement (ex-C2 § 9.1) |
| **E. Productions par lot devisé** : catalogue privé des œuvres, supports commerciaux, dossiers de faisabilité d'un événement ou d'un lieu | 3.5, 3.6, 3.7, 3.8 | Lot, prix, réception et acompte propres, **hors abonnement** | Par devis |
| (Accessoire) **Jarvis réduit à un outil documentaire** | 3.4 | Gain mesuré en interne ; propriété du code tranchée | Inclus dans D, ou lot séparé |

**Règles transversales [PR].**
- Pas d'abonnement qui absorbe implicitement les développements, les événements, les urgences et la recherche. On revient à l'architecture « contrat-cadre plus fiches de mission » du 30 oct. (V5 p. 2).
- Les gains d'automatisation sont traités explicitement dans le prix. La règle du 29 oct. a disparu le 2 nov. (corr. ver-C2, omission 1).
- Aucune rémunération sur les ventes d'œuvres sans avis d'avocat (rj-R5 (a)).

### 4.2 Projets exploratoires qui consomment des ressources

| Projet | Ce qu'il a déjà consommé | Financeur | Règle proposée [PR] |
| --- | --- | --- | --- |
| STRATES et programme de figurines | STRATES v1.1, revue de 12 p., dossier investisseur de 23 p., budget de 53 lignes, vidéos IA (31 oct. – 2 nov.) ; temps et crédits [IN] (ex-C8 § 9.10) | « Serait Carlone » [DR], sans écrit | Gel. Reprise seulement avec un financeur écrit, un budget plafonné, un artiste sous contrat et la place exploratoire libre |
| Éclosion | Concept de 5 p., pack CAO P0, animation | Aucun | Rester au stade du dessin, sans achat |
| Laboratoire IA et robotique, DGX Spark | Audit de 11 p., option à 30 000 € HT | Aucun acté (STR:102) | Retirer l'option de l'offre ; aucun achat |
| Jarvis M07 et « tour de contrôle » comme produits | Dépôt BOJART, console de 33 tests | Aucun | Outil interne seulement, jusqu'à un gain mesuré |
| Vernissage « signature » avec bras, week-end « Métamorphose », pistes « Fusion des univers » (capteurs biométriques) | Document d'idées, diaporama de 12 p., 6 visuels IA | Aucun | Report ; écarter explicitement les pistes biométriques (ex-C9 § 9.10) |
| Module Hermes360 | 3 commits du 28 oct. | Aucun | Ne plus développer avant de connaître l'outil de Quali Contact |
| Travail gratuit pour les lieux (dossier de Mathys du 21 oct.) | 34 p., plan non exécuté | Aucun, et aucun mandat | Aucune production pour un lieu sans mandat ni commanditaire identifié |

### 4.3 Activités hors du périmètre de Marwin

- **Obligations d'exploitant** : licences, permis d'exploitation, ERP, GN 6, récépissé de spectacles, emploi d'artistes, Sacem. Elles relèvent de l'entité de GianLuca ou de l'exploitant (rj-R5 (d) et (e)). Marwin prépare les dossiers et coordonne, sous mandat écrit [PR].
- **Conseil fiscal ou juridique** et signature d'attestations : validation de l'article 238 bis AB, attestation annuelle de l'offre 4 (CAT:45).
- **Intermédiaire de vente** avec commission ou encaissement (LCB-FT, droit de suite), **garde ou transport d'œuvres**, et **enchères publiques** (rj-R5 (a), (b), § 0.3).
- **Fabricant ou intégrateur** d'une machine destinée au public (rj-R5 (f)).
- **Engagements au nom du client** sans mandat : contrats, recrutements, travaux, investissements (ACC:100).
- **Exploitation du cabaret** et des lieux.
- **Collaboration avec Medhi et BOJ.ART** dans l'offre, depuis le 4 nov. [DR], sous réserve d'une formalisation.
- À vérifier avant de les accepter : la gestion de la trésorerie et des factures (mission 1, frontière avec l'expertise comptable) et l'organisation des séjours (mission 7, réglementation éventuelle) [IN] (ex-C2 Q19). Une **coordination simple**, sans achat de prestations pour le compte du client, reste possible [HY].

### 4.4 Tableau récapitulatif

| N° | Chantier | Classement | Priorité |
| --- | --- | --- | --- |
| 1 | CRM et développement commercial | Peut financer (B), après une conformité non facturée | P0 conformité ; P1 pilote |
| 2 | Coordination de Quali Contact | Peut financer (C), si le contrat est confirmé | P1 conditionnelle |
| 3 | Organisation et pilotage | Peut financer (A puis D) | P0 cadrage ; récurrent ensuite |
| 4 | Jarvis et automatisations | Accessoire ; exploratoire tant que rien n'est mesuré | P2 |
| 5 | Marketing et contenus | Peut financer (E) | P2 |
| 6 | Galerie, œuvres, artistes | Peut financer (E, catalogue privé) ; vente et intermédiation hors périmètre | P1 catalogue ; P3 galerie |
| 7 | Événements et vernissage | Peut financer (E, faisabilité) ; format « signature » exploratoire | P2 ; signature reportée |
| 8 | Cabaret et autres lieux | Inventaire dans A ; exploitation hors périmètre | P1 inventaire ; P3 cabaret |
| 9 | Medhi et BOJ.ART | Retiré de l'offre ; mise en cohérence interne | P0 cohérence |
| 10 | STRATES, Éclosion, créations | Exploratoire | P4 gelé |
| 11 | Laboratoire IA et robotique | Exploratoire | P4 gelé ; retirer la diapositive |

---

## 5. Questions bloquantes à poser à GianLuca Carlone

Douze questions au plus, courtes, à poser lors du rendez-vous. Aucun rendez-vous n'est fixé à ce jour (NOTE:5).

1. Quelle entité signe, paie et valide nos travaux : dénomination, SIREN, personne habilitée ? Une seule entité, ou une par projet ?
2. Quels lieux détenez-vous ou exploitez-vous (Vieux Relais, le M, galerie, autres bâtiments) ? Pour chacun : propriétaire, exploitant, date.
3. Quelles sont vos trois priorités pour les 90 prochains jours, et que vous coûte chacune aujourd'hui ?
4. Que voulez-vous nous confier : un cadrage, un suivi régulier ou des lots ponctuels ? Les « vingt jours par mois », est-ce votre demande ?
5. Quel budget mensuel, sur quelle durée et selon quel calendrier de paiement pouvez-vous engager ?
6. Quelles décisions gardez-vous, et quels plafonds de dépense acceptez-vous de déléguer ?
7. Quels documents et accès nous donnerez-vous, et qui sont vos interlocuteurs (responsables, comptable, avocat) ?
8. Avez-vous engagé Quali Contact (contrat, outil, périmètre) ? Qui appellera les entreprises ?
9. Au nom de quelle structure vendez-vous les œuvres ? Avec quels artistes et quelles œuvres disponibles ?
10. Voulez-vous utiliser le CRM livré ? Quelle entité sera responsable des données ?
11. Quel résultat, mesuré à trois mois, vous ferait continuer ou arrêter ?
12. Pour les bureaux, l'emploi et l'investissement évoqués : sous quelle forme et à quelles conditions ?

---

## Annexe : corrections des contrôleurs reprises et limites

**Corrections retenues** (le lecteur est corrigé par son contrôleur) :

| Sujet | Correction retenue | Source |
| --- | --- | --- |
| Vingt jours par mois | Attribution contradictoire, et non souhait établi du client | ver-C1 n° 4 |
| Acompte | Les versions concordent ; seule diverge la règle de paiement des mois 2 à 6 | ver-C1 n° 7 |
| Plancher de prix | Seuil de coûts, et non remise sur le taux | ver-C1 n° 8 |
| PDF de 13 diapositives | Présent sur la branche de la PR n° 1 | ver-C1, omission 1 |
| Origine du taux de 750 € | [HY], et non « calcul à rebours » prouvé | ver-C2 n° 2 |
| Atelier de dix imprimantes | Rattachement à BOJ.ART : [HY] | ver-C2 n° 11 |
| Capital | Pas de contradiction sur le principe de l'investissement | ver-C2 n° 14 ; ver-C10 n° 12 |
| Structure vendeuse | Son existence est [IN] ; seul son nom est « à compléter » | ver-C5 n° 14 |
| Numéros exposés | 800 à 940 selon la méthode de comptage | ver-C5 n° 15 |
| Bénéficiaires dont le plafond dépasse le bénéfice | 58 sur 485 en campagne | ver-C5 n° 9 |
| Onglet culture | 22 artistes individuels, et non 97 | ver-C6 n° 6 ; ver-C9 n° 15 |
| Hermes360 | Fonction codée, raccordement inconnu | ver-C6 n° 7 |
| Vieux Relais | Axe culture toujours actif dans le CRM | ver-C6 n° 13 ; ver-C9, omission 1 |
| Réorientation du CRM | Datée du 22 oct. | ver-C9 n° 7 |
| Revue robotique | Écart d'environ 1 h 35 avec les documents jugés | ver-C8 n° 1 |
| Retour sur investissement (figurines) | 35 à 44 ans, et non 51 | ver-C8 n° 11 |
| Option laboratoire | « En vigueur », et non « envoyée » | ver-C8 n° 8 |
| Démonstrateur Jarvis | Dans le forfait, pas dans l'option laboratoire | ver-C8 n° 9 |
| Tests de la console | [DR], et non [MM] | ver-C10 § 2 |
| Eaglemic | Associé de Morgan en général, non de Marwin | ver-C10 n° 14 |
| Directive (UE) 2024/2853 | Produits mis sur le marché « après le 8 décembre 2026 » | ver-R5 n° 12 |
| Délai CNIL | Expire le 5 nov., sans être encore dépassé au 4 nov. au soir | ver-R4 n° 7 |

**Limites :**
- Cette synthèse ne couvre ni la capacité détaillée, ni le prix, ni la structure : ces sujets relèvent d'autres synthétiseurs.
- La collecte des conversations ChatGPT reste incomplète : 169 conversations lues sur 219 (`livrables/collecte-chatgpt-2026-11-04/README.md:7`). Des engagements pris envers GianLuca peuvent exister hors du corpus lu [IN].
- La visibilité du dépôt FinanceScope n'a pas été revérifiée dans cet audit (NOTE:23).
- Aucune information n'existe sur l'agenda de Mathys (NOTE:17).
