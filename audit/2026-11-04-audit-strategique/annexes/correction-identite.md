# Correction d'identité : le client s'appelle GianLuca Carlone

Audit Marwin Tech × GianLuca Carlone · Annexe · 4 novembre 2026

Statut : interne. Ne pas transmettre à GianLuca Carlone : cette annexe liste des pièces internes et des erreurs de Marwin. Le client ne reçoit, au besoin, qu'une phrase de correction sobre (section 4.3).

Sources principales : `travaux/DEMANDE.md:8` ; `travaux/syn-sources.md:396-450` (section f) ; `travaux/strategie-retenue.md:21, 798-812` ; recomptage refait pour cette annexe sur le dépôt `Momolscode/Carlone` (`grep`, `pdftotext`, lecture des ZIP), contrôles faits dans la nuit du 4 au 5 nov. 2026 ; pièces d'origine rouvertes : `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md`, `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf`, `interne/archives-marwin-tech/choix-structure-2026-10-29.pdf`, `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` ; diaporama interne « Projet Carlone — tout le contexte » (page claude.ai privée de Morgan).

Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

---

## L'essentiel

- Le client s'appelle **GianLuca Carlone**. Morgan Olsen a demandé cette correction le 4 nov. 2026 [DR] (`travaux/DEMANDE.md:8` ; `travaux/note-point-4-novembre-et-activites.md:26`).
- Les archives du dépôt portent **433 fois** un ancien prénom erroné, dans **28 fichiers** [FV] (recomptage de cette annexe, section 2 ; même total que `travaux/syn-sources.md:437`). Aucune archive n'emploie « GianLuca » [FV].
- Ces 28 pièces restent **intactes**. Personne ne les réécrit (section 3).
- **Deux documents rédigés pour le client** portent l'erreur : le PDF des options du 30 oct. (p. 1 à 16) et la lettre de la page ChatGPT du 29 oct. On ne les corrige pas et on ne les renvoie pas : leur contenu est retiré. Ils sont remplacés par les deux projets du dossier `pour-gianluca/` [PR] (`travaux/strategie-retenue.md:211, 798` ; section 4).
- Dans les nouveaux livrables de l'audit, l'ancien prénom n'apparaît que dans **5 citations exactes**, toutes suivies de [sic, lire GianLuca]. Les deux documents destinés à GianLuca : **0 occurrence** [FV] (section 6).
- Le diaporama interne « Projet Carlone — tout le contexte » a été corrigé le 4 nov. [DR]. Sa version en ligne écrit bien « GianLuca Carlone » [FV] (section 7).

**Écart avec la stratégie retenue : aucun.** Cette annexe applique `travaux/strategie-retenue.md:21, 798, 802, 812`.

---

## 1. La règle

### 1.1 Le nom et les formes erronées

| Point | Règle | Source |
| --- | --- | --- |
| Nom du client | **GianLuca Carlone** ; à défaut « GianLuca » ou « M. Carlone » | `travaux/DEMANDE.md:8` ; `travaux/BRIEF-AGENTS.md:14` |
| Qui a tranché, et quand | Morgan Olsen, le 4 nov. 2026 [DR] | `travaux/note-point-4-novembre-et-activites.md:26` ; `14-registre-risques-inconnues-decisions.md:251` (décision D01) |
| Formes erronées trouvées | **Variante A** : « John-Lucas » [sic, lire GianLuca], avec trait d'union. **Variante B** : « John Lucas » [sic, lire GianLuca], sans trait d'union. Aucune autre graphie du prénom dans les archives [FV] (section 2) | Recomptage, section 2 |
| Usage permis des formes erronées | Alias de recherche pour retrouver les sources ; citation exacte d'une pièce, suivie de [sic, lire GianLuca] | `travaux/DEMANDE.md:8` ; `travaux/BRIEF-AGENTS.md:14` |
| Usage interdit | Désigner le client dans une nouvelle rédaction ; corriger une pièce historique sans le dire | `travaux/DEMANDE.md:8` ; `travaux/strategie-retenue.md:802` |
| À ne pas confondre | Les **134 « Jean-Luc »** de `crm/` sont des dirigeants d'entreprises prospectées. Ces fiches ne se corrigent pas [FV] (recompté : 134) | `travaux/syn-sources.md:402` |
| Encore inconnu | Nom complet et état civil, nécessaires au bon de commande et au contrat [IN] | `14-registre-risques-inconnues-decisions.md:220` (inconnue U26) |

Dans la suite, « variante A » et « variante B » désignent ces deux formes, pour ne pas les répéter.

Un point voisin n'est pas une erreur de prénom : dans les anciennes pièces, « Carlone » désigne tantôt la personne, tantôt une entité. L'entité qui signe et paie reste à identifier [IN] (`travaux/syn-sources.md:336` ; 02-etat-des-sources.md).

### 1.2 Trois principes

1. **Les pièces historiques restent intactes.** Archives, pages ChatGPT, recueils, PDF et ZIP ne sont pas réécrits (`travaux/DEMANDE.md:8` ; `travaux/strategie-retenue.md:802`).
2. **Toute nouvelle version est corrigée et datée.** Tout document produit à partir du 4 nov. 2026 écrit « GianLuca Carlone ».
3. **Aucune pièce historique fautive n'est renvoyée au client** (`travaux/strategie-retenue.md:798`). Si une telle pièce lui a déjà été remise, une correction sobre suffit (`travaux/strategie-retenue.md:812` ; section 4.3).

---

## 2. Recomptage

### 2.1 Méthode

- **État du dépôt.** Hors du dossier `audit/`, la branche de l'audit est identique au commit `7b46602` de `main` (4 nov. 2026, 17 h 37) : `git diff 7b46602 HEAD` ne montre aucun changement hors `audit/` [FV].
- **Commandes lancées à la racine du dépôt** :

```
grep -rci --exclude-dir=.git "john-lucas" .   # variante A, alias de recherche [sic, lire GianLuca]
grep -rci --exclude-dir=.git "john lucas" .   # variante B, alias de recherche [sic, lire GianLuca]
grep -rci --exclude-dir=.git "john-luca" .    # forme tronquée, alias de recherche [sic, lire GianLuca]
grep -rIoi --exclude-dir=.git -E "john[- ]lucas?" .   # occurrences, et non lignes
```

- `grep -c` compte des **lignes**, pas des occurrences. Les occurrences ont été comptées à part (`grep -o`).
- `grep` ne lit pas le texte des PDF ni des ZIP, qui sont compressés. Le texte des PDF a été extrait avec `pdftotext` (le `.pdf.gz` décompressé d'abord). Les membres des ZIP ont été lus en mémoire, sans extraction sur le disque. Le `.docx` et le `.xlsx` du dépôt ont aussi été lus : 0 occurrence.
- Le dossier `audit/` est compté à part (section 6).

### 2.2 Résultats (hors dossier `audit/`)

| Mesure | Variante A | Variante B | Total |
| --- | ---: | ---: | ---: |
| `grep -rci` : lignes dans les fichiers texte | 238 lignes, 22 fichiers | 8 lignes, 8 fichiers | 246 lignes |
| Occurrences dans les fichiers texte | 242 | 8 | **250** |
| Occurrences dans les PDF (4 fichiers, dont l'original compressé) | 8 | 0 | **8** |
| Occurrences dans les ZIP (2 archives, 16 membres) | 169 | 6 | **175** |
| **Total** | **419** | **14** | **433** |

Lecture [FV] :

- **433 occurrences physiques** dans 28 fichiers ; **430** sans l'original compressé du PDF des options, qui double son texte. C'est le même total que `travaux/syn-sources.md:437`.
- `grep -rci` donne 246 lignes pour 250 occurrences : deux fichiers JSON portent plusieurs occurrences sur une même ligne (`sources/chatgpt-conversations/2026-11-04/travail-pour-marwin-studio.json:147` ; `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.json:59`).
- La forme tronquée trouve exactement les 238 lignes de la variante A : il n'existe pas de forme tronquée sans « s ».
- « GianLuca », « Gianluca », « Gian Luca » : 0 occurrence dans les archives.
- Branche de la PR n° 1 (`origin/claude/dossier-carlone-2026-11-04`) : mêmes 246 lignes dans les mêmes 22 fichiers texte (`git grep`).
- Le chiffre « environ 300 » de la note du 4 nov. (`travaux/note-point-4-novembre-et-activites.md:26`) ne correspond à aucun périmètre reproductible (`travaux/syn-sources.md:441`). **433 est le chiffre de référence.**

**Origine probable de l'erreur.** Elle apparaît dans les réponses des assistants ChatGPT et dans les pages ChatGPT du 25 au 31 oct. Dans ses messages visibles, Morgan écrit « Carlone » ou « ce monsieur » [FV] (`interne/recueil-sessions-chatgpt-2026-11-04.txt:104, 139, 220`). L'erreur vient sans doute de la mémoire de l'assistant [HY] ; l'origine exacte est inconnue [IN] (`travaux/syn-sources.md:447` ; `14-registre-risques-inconnues-decisions.md:236`, inconnue U38).

---

## 3. Pièces historiques qui portent l'erreur, laissées intactes

Toutes restent telles quelles [PR] (`travaux/strategie-retenue.md:802`). Comptes vérifiés pour cette annexe [FV].

### 3.1 Fichiers texte (22)

| Chemin | Type | Var. A | Var. B | Total | Où |
| --- | --- | ---: | ---: | ---: | --- |
| `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md` | Page ChatGPT exportée (mise à jour le 29 oct.) | 9 | 1 | 10 | l. 1, 7, 9 (var. B), 11, 34, 45, 88, 109, 117, 143. **Contient la lettre au client** (section 4) |
| `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.json` | Métadonnées et blocs de la même page | 12 | 1 | 13 | — |
| `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md` | Page ChatGPT exportée (mise à jour le 28 oct.) | 9 | 0 | 9 | l. 1 (titre), 7, 13, 14, 15, 16, 18, 32, 65 |
| `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.json` | Métadonnées et blocs | 11 | 0 | 11 | 8 lignes |
| `sources/chatgpt-pages/2026-11-04-complement/marwin-structure-et-offres.md` | Page ChatGPT exportée | 2 | 0 | 2 | l. 71, 124 |
| `sources/chatgpt-pages/2026-11-04-complement/marwin-structure-et-offres.json` | Métadonnées | 2 | 0 | 2 | — |
| `sources/chatgpt-pages/2026-11-04-complement/pilotage-extraits-carlone.md` | Extraits de page ChatGPT | 3 | 0 | 3 | l. 5, 9, 24 |
| `sources/chatgpt-pages/2026-11-04-complement/pilotage-extraits-carlone.json` | Métadonnées | 3 | 0 | 3 | — |
| `sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md` | Page ChatGPT exportée | 1 | 0 | 1 | l. 81 |
| `sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.json` | Métadonnées | 1 | 0 | 1 | — |
| `sources/chatgpt-pages/2026-11-04-complement/audit-pilotage-extraits-carlone.md` | Extraits de page ChatGPT | 1 | 0 | 1 | l. 5 (critère de recherche) |
| `sources/chatgpt-pages/2026-11-04-complement/audit-pilotage-extraits-carlone.json` | Métadonnées | 1 | 0 | 1 | — |
| `sources/chatgpt-conversations/2026-11-04/travail-pour-marwin-studio.json` | Conversation ChatGPT | 5 | 0 | 5 | l. 72, 97, 122, 147 (deux fois), dans les réponses de l'assistant |
| `sources/manifeste-complement-sessions-chatgpt-2026-11-04.json` | Manifeste de collecte | 2 | 0 | 2 | l. 40, 47 (titres de pages) |
| `sources/index-complement-sessions-chatgpt-2026-11-04.md` | Index de collecte (4 nov.) | 1 | 0 | 1 | l. 19 (critère de recherche) |
| `interne/complement-chatgpt-2026-11-04.md` | Note de collecte (4 nov.) | 1 | 0 | 1 | l. 15 |
| `interne/recueil-sessions-chatgpt-2026-11-04.txt` | Recueil des sessions ChatGPT, v2 | 31 | 1 | 32 | Identique octet pour octet à `livrables/collecte-chatgpt-2026-11-04/CARLONE_Sources_retrouvees_v2.txt` |
| `interne/recueil-sessions-chatgpt-2026-11-04.html` | Recueil v2 (HTML) | 33 | 1 | 34 | Identique à `livrables/collecte-chatgpt-2026-11-04/CARLONE_Recueil_et_sources_v2.html` |
| `livrables/collecte-chatgpt-2026-11-04/CARLONE_Sources_retrouvees.txt` | Recueil v1 | 24 | 1 | 25 | — |
| `livrables/collecte-chatgpt-2026-11-04/CARLONE_Sources_retrouvees_v2.txt` | Recueil v2 | 31 | 1 | 32 | — |
| `livrables/collecte-chatgpt-2026-11-04/CARLONE_Recueil_et_sources.html` | Synthèse v1 (HTML) | 26 | 1 | 27 | — |
| `livrables/collecte-chatgpt-2026-11-04/CARLONE_Recueil_et_sources_v2.html` | Synthèse v2 (HTML) | 33 | 1 | 34 | — |
| **Sous-total texte** | | **242** | **8** | **250** | |

L'index et la note de collecte du 4 nov. ont été écrits par des assistants le jour même. Ils font partie du dépôt au commit `7b46602` : ils sont traités comme des pièces historiques. S'ils sont un jour repris, la nouvelle version sera corrigée et datée [PR].

### 3.2 PDF (4)

| Chemin | Type | Var. A | Var. B | Où |
| --- | --- | ---: | ---: | --- |
| `interne/archives-marwin-tech/choix-structure-2026-10-29.pdf` | Étude interne de structure (29 oct.) | 1 | 0 | p. 6 : « Si John-Lucas devient à la fois employeur et client » [sic, lire GianLuca] |
| `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` | PDF de 26 p. : p. 1 à 16 adressées au client, p. 17 à 26 « annexe interne aux fondateurs » | 3 | 0 | p. 1, 5, 12 (section 4) |
| `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.original.pdf.gz` | Original compressé du même PDF | 3 | 0 | Même texte (doublon) |
| `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` | Audit interne du laboratoire (31 oct.) | 1 | 0 | p. 2 : « L’investissement immobilier rapporté de John-Lucas ne prouve ni son budget d’innovation… » [sic, lire GianLuca] |
| **Sous-total PDF** | | **8** | **0** | 8 occurrences, 5 sans le doublon |

### 3.3 Archives ZIP (2)

| Chemin | Type | Var. A | Var. B | Total |
| --- | --- | ---: | ---: | ---: |
| `livrables/collecte-chatgpt-2026-11-04/CARLONE_Recueil_complement_v2.zip` | Archive de collecte (10 membres concernés) | 95 | 3 | 98 |
| `livrables/collecte-chatgpt-2026-11-04/CARLONE_Recueil_complet.zip` | Archive de collecte (6 membres concernés) | 74 | 3 | 77 |
| **Sous-total ZIP** | | **169** | **6** | **175** |

**Total des trois tableaux : 28 fichiers, 419 + 14 = 433 occurrences** [FV].

### 3.4 Pièces sans erreur

0 occurrence [FV] dans : `crm/` (645 fichiers) ; `pour-carlone/` (textes et PDF) ; `sources/propositions-de-collaboration.pdf` (18 oct.) ; `crm/docs/rapport/Rapport CRM Nièvre et Hermes360.pdf` et sa version `.docx` ; l'offre écrite du 2 nov. (`interne/offre-marwin-tech-remuneration-et-collaboration.md`) ; le contexte (`interne/contexte-projet-carlone.md`) ; les cinq autres ZIP ; le tableur du dossier investisseur. Ces pièces disent « Carlone » ou « M. Carlone », sans prénom.

---

## 4. Documents rédigés pour le client qui portent l'erreur

### 4.1 Les deux documents

| Document | Où est l'erreur [FV] | Remis au client ? | Sort retenu | Nouvelle version |
| --- | --- | --- | --- | --- |
| **PDF des options du 30 oct.**, p. 1 à 16 (`interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf`). En-tête « PROPOSITION CARLONE \| À FINALISER », « Version de travail du 30 octobre 2026 » (p. 1) | p. 1 : « Proposition d’accompagnement pour John-Lucas Carlone » [sic, lire GianLuca] ; p. 5 : « John-Lucas, nous vous proposons… » [sic, lire GianLuca] ; p. 12 : « John-Lucas / entité cliente » [sic, lire GianLuca] | Inconnu [IN] (`travaux/syn-sources.md:352` ; `travaux/ver-C2-offre.md:114`) | **Jamais transmis**, même corrigé : la formule de six mois et l'option laboratoire sont retirées [PR] (`travaux/strategie-retenue.md:211, 661`) | Pas de version corrigée de ce PDF. Il est remplacé par `pour-gianluca/proposition-de-cadrage.md` et `pour-gianluca/message-de-recadrage.md` (projets non envoyés) |
| **Lettre de la page ChatGPT du 29 oct.** (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:9-30`), signée « Morgan Olsen / Marwin Tech » (l. 29-30) | l. 9, titre : « Proposition à adresser à John Lucas » [sic, lire GianLuca] ; l. 11 : « Bonjour John-Lucas, » [sic, lire GianLuca] | Inconnu [IN] (`travaux/strategie-retenue.md:736`, question 9) | **Pas renvoyée** : son offre (six mois à 15 000 € HT par mois, l. 23) est retirée [PR] (`travaux/strategie-retenue.md:41, 798`) | Même remplacement |

Les deux projets de remplacement écrivent « GianLuca » et ne contiennent **aucune** occurrence de l'ancien prénom [FV] (section 6).

### 4.2 Pourquoi pas de version corrigée

La synthèse des sources proposait d'en faire des versions corrigées et datées (`travaux/syn-sources.md:401`). La stratégie retenue tranche autrement : aucune pièce historique fautive n'est renvoyée, et le PDF des options n'est jamais transmis (`travaux/strategie-retenue.md:211, 798`). Leur contenu n'est plus proposé ; une version corrigée remettrait en circulation une offre retirée. Cette annexe suit la stratégie.

### 4.3 Si l'un des deux a déjà été remis

Le message de recadrage prévoit une phrase facultative : « Une de nos lettres comportait une erreur sur votre prénom ; nous vous prions de nous en excuser. » (`pour-gianluca/message-de-recadrage.md:46` ; 13-preparation-rendez-vous.md, ligne 480). On la garde seulement si Morgan confirme qu'une pièce au prénom erroné a été remise ; sinon on la supprime [PR] (`travaux/strategie-retenue.md:812`). La phrase ne répète pas le prénom erroné.

### 4.4 Autres documents pour le client : pas d'erreur de prénom

- **Diaporama client « Offre Marwin Tech pour Carlone »** : 0 occurrence dans la version à 11 vues et dans l'ancienne à 13 vues [FV] (`travaux/syn-sources.md:442`, revérifié sur la copie du 4 nov. ; les 11 vues en ligne ont les mêmes tailles de fichiers que cette copie). Il dit « M. Carlone ». Il reste à corriger sur d'autres points avant toute remise (`travaux/strategie-retenue.md:814-828`).
- `pour-carlone/`, `sources/propositions-de-collaboration.pdf`, le rapport CRM du 29 oct. : 0 occurrence [FV].
- Quand une nouvelle version de ces documents emploie un prénom, elle écrit « GianLuca » [PR].

---

## 5. Règle de citation [sic, lire GianLuca]

**Forme** : « citation exacte » [sic, lire GianLuca] (`chemin:ligne` ou `chemin.pdf p. N`).

**Exemple** : « Bonjour John-Lucas, » [sic, lire GianLuca] (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:11`).

1. On cite **exactement** : mêmes mots, même ponctuation. On ne corrige pas l'erreur entre les guillemets.
2. Le marqueur suit **immédiatement** le guillemet fermant, avant la source.
3. Pour une page ChatGPT dont le titre porte l'erreur, on préfère le chemin du fichier. Si on cite le titre, on ajoute le marqueur.
4. Une forme erronée peut servir d'**alias de recherche** (commande, critère, tableau de décompte) dans un document interne. Elle ne sert jamais à désigner le client.
5. **Jamais dans un document destiné à GianLuca** : ni la forme erronée, ni une citation qui la contient (`travaux/strategie-retenue.md:798`). Seule exception : la phrase de correction de la section 4.3, qui ne répète pas le prénom.
6. On ne touche pas aux « Jean-Luc » de `crm/`.
7. **Contrôle avant envoi** [PR] : `grep -ciE "john[- ]?luca" <fichier>` doit renvoyer 0 pour tout document destiné à GianLuca. Pour un document interne, chaque ligne trouvée doit porter le marqueur. Responsable : Morgan, avant chaque envoi (`14-registre-risques-inconnues-decisions.md:148`, risque R43).

---

## 6. État dans les nouveaux documents de l'audit

Contrôle fait dans la nuit du 4 au 5 nov. 2026 sur le dossier `audit/2026-11-04-audit-strategique/` [FV].

| Ensemble | Occurrences de l'ancien prénom | Statut |
| --- | ---: | --- |
| Livrables internes 01-synthese-direction.md à 14-registre-risques-inconnues-decisions.md (14 fichiers) | 5 | Toutes sont des citations exactes suivies de [sic, lire GianLuca] : 4 dans 02-etat-des-sources.md (lignes 311 et 490), 1 dans 03-cartographie-projets.md (ligne 57). **0 hors citation** |
| `pour-gianluca/proposition-de-cadrage.md` et `pour-gianluca/message-de-recadrage.md` | **0** | Conforme à `travaux/strategie-retenue.md:798` |
| `modele-financier/` (6 fichiers) | 0 | — |
| 15-contre-analyse.md | — | Pas encore écrit au moment du contrôle : à contrôler avant diffusion [IN] |
| Cette annexe | — | Les formes erronées n'y figurent que dans des citations exactes ou comme alias de recherche, chaque fois suivies du marqueur |
| Travaux préparatoires (`travaux/`, 32 fichiers concernés) | 148 | 85 suivies du marqueur. Les 63 autres sont des alias de recherche, des tableaux de décompte ou l'énoncé de la règle (`travaux/DEMANDE.md:8` ; `travaux/BRIEF-AGENTS.md:14`), et quelques citations sans marqueur déjà signalées (`travaux/ver-C2-offre.md:76`, à propos de `travaux/ex-C2-offre.md:269-270`). Aucune ne désigne le client dans la rédaction propre d'un agent |

Autres constats [FV] :

- L'orthographe « GianLuca » est employée partout. Aucune graphie concurrente (« Gianluca », « Gian Luca ») dans les livrables ni dans les projets pour le client.
- Les travaux préparatoires ne sont pas destinés à être diffusés. Un passage repris d'un fichier de `travaux/` dans un livrable doit recevoir le marqueur s'il ne l'a pas.

**Conclusion : zéro occurrence de l'ancien prénom hors citations dans les nouveaux documents de l'audit, et zéro dans les documents destinés à GianLuca** [FV].

---

## 7. Diaporama interne « Projet Carlone — tout le contexte »

- **Nature** : page claude.ai privée de Morgan, diaporama de 22 vues, interne. Sa couverture porte « À ne pas montrer à Carlone » [FV] (`travaux/note-point-4-novembre-et-activites.md:13`).
- **Correction** : le prénom a été corrigé le 4 nov. 2026 [DR].
- **Version vérifiée** [FV] : https://claude.ai/artifact/BKT5BhNLbHuuiY6srrcFoq, version mise à jour le 4 nov. 2026, lue le 5 nov. 2026.
  - Vue `personnes` : « GianLuca Carlone, marchand d’art venu de l’avenue Montaigne. »
  - Notes de la même vue : « Le client s’appelle GianLuca Carlone (correction de Morgan du 4 novembre) ». La suite de la note mentionne l'erreur des archives ChatGPT entre guillemets, avec les mots « par erreur ».
  - Les 21 autres vues disent « Carlone » ou « M. Carlone ». Aucune ne désigne le client par l'ancien prénom.
- **Ce qu'on ne sait pas** : le texte d'avant la correction [IN]. La seule copie antérieure disponible est un index de 23 vues, sans le texte des vues.
- **Limite** : la correction porte sur le prénom. Le reste de ce diaporama date d'avant la stratégie retenue : il présente par exemple « 750 € HT la journée » comme « Solide » (vue `audit`), ce que la stratégie abandonne (`travaux/strategie-retenue.md:41`). Il reste interne et ne va jamais au client (11-proposition-commerciale-revisee.md, ligne 267 ; 13-preparation-rendez-vous.md, ligne 298).

---

## 8. Recommandations et décisions

| Recommandation [PR] | Preuve | Hypothèse | Limite | Décision correspondante |
| --- | --- | --- | --- | --- |
| 1. Ne renvoyer ni le PDF des options ni la lettre du 29 oct., même corrigés ; les remplacer par la proposition de cadrage et le message de recadrage | Erreur aux p. 1, 5 et 12 du PDF et aux l. 9 et 11 de la lettre [FV] ; contenu retiré (`travaux/strategie-retenue.md:211, 798`) | GianLuca a pu recevoir l'un des deux [HY] | Une copie déjà remise échappe à tout contrôle | Morgan dit ce que GianLuca a vu ou reçu (`travaux/strategie-retenue.md:736`, question 9) ; on garde ou on supprime la phrase de `pour-gianluca/message-de-recadrage.md:46` |
| 2. Contrôle « 0 occurrence » avant tout envoi au client (section 5, règle 7) | 433 occurrences dans les archives, surtout dans les pages ChatGPT dont les nouveaux textes s'inspirent [FV] | Des passages seront encore repris des archives [HY] | Le contrôle ne lit ni les images ni le texte inclus dans une image | Morgan, avant chaque envoi (`14-registre-risques-inconnues-decisions.md:148`) |
| 3. Laisser les 28 pièces intactes ; cette annexe sert de registre de l'erreur | Règle de `travaux/DEMANDE.md:8` ; `travaux/strategie-retenue.md:802` | — | Qui ouvre une pièce sans lire cette annexe ne voit pas l'erreur signalée | Aucune décision nouvelle : application de la décision D01 (`14-registre-risques-inconnues-decisions.md:251`) |
| 4. Obtenir le nom complet et l'état civil avant le bon de commande | Aucune pièce ne les donne [FV] | — | Sans eux, ni bon de commande ni contrat fiable | GianLuca, au bon de commande (`14-registre-risques-inconnues-decisions.md:220`) |
| 5. Vérifier la mémoire et les instructions personnalisées du compte ChatGPT de Morgan, et y corriger le prénom s'il y figure | L'erreur n'apparaît que dans les réponses des assistants, jamais dans les messages de Morgan [FV] (`interne/recueil-sessions-chatgpt-2026-11-04.txt:104, 139, 220`) | Elle vient de la mémoire de l'assistant [HY] | Origine exacte inconnue [IN] ; 50 conversations sur 219 non lues | Morgan, sans date imposée (`14-registre-risques-inconnues-decisions.md:236`) |

---

## 9. Limites du recomptage

- Il couvre le dépôt `Momolscode/Carlone` : fichiers texte, PDF, ZIP, `.docx` et `.xlsx`. Il ne lit pas le texte inclus dans les images ni dans les vidéos [IN].
- Il ne couvre pas les e-mails, messages ou documents envoyés à GianLuca hors du dépôt : Gmail et Drive n'ont pas été consultés [IN] (`travaux/note-point-4-novembre-et-activites.md`, § C).
- La collecte ChatGPT est incomplète : 169 conversations lues sur 219 (`travaux/DEMANDE.md`, § 1). D'autres occurrences peuvent exister hors du dépôt [IN].
- Le dépôt public BOJART n'a pas été relu pour cette annexe. Le dernier état documenté donne 0 occurrence (`travaux/syn-sources.md:442`).
