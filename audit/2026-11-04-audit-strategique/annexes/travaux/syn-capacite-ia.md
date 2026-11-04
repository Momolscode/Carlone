# Synthèse « capacité-ia » : ce que Morgan et Mathys peuvent tenir à deux, et ce que l'IA y change

Synthétiseur « capacité-ia » de l'audit Marwin Tech × GianLuca Carlone, rédigé le 4 novembre 2026 au soir.

**Document interne.** Il contient des éléments sur la disponibilité, les compétences et les limites des associés. Il ne doit pas être transmis tel quel à GianLuca Carlone. Les seuils, protocoles d'essai et règles de sécurité (sections 4, 6 et 8) peuvent en revanche servir de base à une annexe contractuelle.

---

## Méthode, sources et conventions

**Bases utilisées.**
- Inventaires des lecteurs : ex-C2 (offre), ex-C3 (section 3, chiffres), ex-C4 (méthodes), ex-C5 (CRM), ex-C7 (Jarvis), avec leurs contrôles ver-C2, ver-C3, ver-C4, ver-C5 et ver-C7.
- Mémos rj-R4 (données, IA, sécurité des agents) et rj-R6 (marché), avec leurs contrôles ver-R4 et ver-R6.
- Note de l'auditeur du 4 novembre (`audit-work/note-point-4-novembre-et-activites.md`, ci-après NOTE).
- Pour cohérence seulement : `audit-work/syn-portefeuille.md` (classement des chantiers).

Quand un contrôleur corrige un lecteur, c'est sa correction qui est retenue. Elle est signalée par « corr. ver-… ».

**Pièces d'origine rouvertes (4 nov. 2026, lecture seule).** Dépôt `Momolscode/Carlone`, branche main, commit 7b46602 (vérifié par `git log -1`) :
- `interne/offre-marwin-tech-remuneration-et-collaboration.md:15, 46, 56-63, 128, 207` ;
- `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:7, 59, 64, 66, 103, 105, 109-113` ;
- `sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md:15, 61, 63, 65, 69, 73` ;
- `interne/recueil-sessions-chatgpt-2026-11-04.txt:249, 434, 440, 485, 534, 543, 804, 861, 1388, 1407, 1517` ;
- `interne/audit-marwin-tech-carlone.md:36-40, 54-64, 93-104` ;
- `interne/contexte-projet-carlone.md:11` ;
- `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` p. 8 et `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 11 (via le texte extrait) ;
- branche distante de la PR n° 1, `origin/claude/dossier-carlone-2026-11-04` (commit 797e81e) : liste des fichiers et `pdfinfo` de `pour-carlone/offre-marwin-tech-pour-carlone.pdf`.

**Calculs.** Les jours ouvrés et le modèle de charge ont été calculés en Python (`python3 -I`). Les scripts sont dans le bloc-notes : `[dossier de travail] charge.py` et `[dossier de travail] charge2.py`.

**Aucune action extérieure** : aucun contact, aucune consultation en ligne, aucune automatisation activée, aucune modification du dépôt. Seul ce fichier a été écrit.

**Nom du client.** Le client s'appelle **GianLuca Carlone**. Les pièces qui portent l'erreur d'archives sont citées telles quelles, suivies de [sic, lire GianLuca].

**Abréviations de sources.**

| Abréviation | Pièce |
| --- | --- |
| OFF | `interne/offre-marwin-tech-remuneration-et-collaboration.md` (2 nov.) |
| ACC | `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md` (29 oct.) |
| STR | `sources/chatgpt-pages/2026-11-04-complement/marwin-structure-et-offres.md` |
| METH | `sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md` |
| APIL / PIL | `sources/chatgpt-pages/2026-11-04-complement/audit-pilotage-extraits-carlone.md` / `pilotage-extraits-carlone.md` |
| AUDIT | `interne/audit-marwin-tech-carlone.md` (2 nov.) |
| R | `interne/recueil-sessions-chatgpt-2026-11-04.txt` |
| V5 | `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` |
| LAB | `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` |
| V | `interne/state-of-the-art-note-de-vision.md` |
| CTX | `interne/contexte-projet-carlone.md` |
| B/ | dépôt public BOJART, `BOJART:` (commit 3436f53) |
| CORPUS | artefact « Corpus des offres IA vendables » (OLSEN, 20 août 2026), texte extrait dans `scratchpad/sources-txt/` |
| deck/ | diaporama client, `scratchpad/artifact-files/04f14ef8-a5fd-429b-9b3e-6d69b1d2ce5f/project/` |
| NOTE | `audit-work/note-point-4-novembre-et-activites.md` |
| JP | journée-personne de 7 h (définition de l'offre : 20 JP = 140 h, OFF:13-16) |

**Codes.** [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu.

**Trois faits nouveaux intégrés.**
1. **Décision du 4 novembre** : Morgan a demandé de retirer Medhi et BOJ.ART de l'offre [DR] (NOTE:25). Le diaporama client est passé à 11 diapositives (`deck/deck.json:7`) [FV]. En revanche, l'offre écrite (OFF:22, 67-101), STRATES v1.1 et le diaporama du vernissage (signé « avec Medhi, BOJ.ART », `pour-carlone/vernissage-strates-diaporama.pdf` p. 12) n'ont pas été modifiés [FV pour les copies du dépôt]. **Vérifié ce soir** : sur la branche de la PR n° 1 (commit 797e81e), `pour-carlone/offre-marwin-tech-pour-carlone.pdf` compte **13 pages**, créé le 4 nov. à 15:37 UTC, et le dossier de diapositives contient encore `08-strates.jpg` et `09-strates-phases.jpg` [FV]. Le fait rapporté passe donc de [DR] à [FV].
2. **Dépôt public FinanceScope/CRM-Carlone** : très probablement une violation de données personnelles (rj-R4 (c)) [HY fort]. Si la connaissance date du 2 novembre (AUDIT:3, 15), le délai de 72 heures pour notifier la CNIL **expire le 5 novembre** à une heure inconnue (corr. ver-R4 n° 7) [ES]. La visibilité du dépôt n'a pas été revérifiée par cet audit [DR] (CTX:11 ; NOTE:23).
3. **Aucun contrat, aucune facture, aucune entité payeuse identifiée** [FV négatif] (OFF:29 ; V5 p. 17 ; AUDIT:14, 121). Toute « capacité facturable » de ce document est donc théorique : le chiffre d'affaires constaté de Marwin est nul.

---

## 0. Ce qu'il faut retenir

1. **Aucune compétence de vente, de maintenance dans la durée ni de coordination de prestataires n'est démontrée par une réalisation.** Ce qui est démontré : produire vite, avec des assistants IA, des documents, des supports, un CRM et du code testé en environnement d'essai. Le CRM (500 fiches) et le dépôt BOJART (933 fichiers, 973 fonctions de test) en sont les preuves [FV]. Aucun n'a de réception client, d'usage mesuré ou de revenu [FV négatif].
2. **Mathys est presque invisible dans les pièces.** On sait qu'il a commandé le CRM (crm/PASSATION.md:7), qu'il contrôle probablement son dépôt (README.md:35) [DR] et qu'il a signé un dossier de prospection de 34 pages [FV]. Ses compétences propres et sa disponibilité sont [IN].
3. **La capacité facturable réaliste est de 7 à 12 JP par mois, et 20 JP au mieux** [ES]. Calcul : 21 jours ouvrés par mois en moyenne (253 de décembre 2026 à novembre 2027), environ 17,5 JP disponibles par personne après congés, maladie et formation, puis déduction des autres projets de Morgan, de la disponibilité inconnue de Mathys et du temps non facturable (administration, prospection, maintenance interne, aléas).
4. **La formule de base (20 JP) n'est pas « un mi-temps chacun »** (OFF:15). Elle demande environ **80 % du temps disponible de chacun des deux** [ES]. **La formule renforcée (40 JP) est impossible** : elle demanderait 140 à 145 % du temps disponible des deux [ES]. L'« ancre » (40 + 6 JP du laboratoire) l'est encore plus.
5. **Sur 20 JP facturées, la production proprement dite ne pèse qu'environ 6 à 7 JP.** Le reste part en réunions, collecte, contrôle, déplacements et maintenance [ES]. L'archive du 29 oct. le disait déjà (ACC:64) ; la version du 2 nov. l'a perdu.
6. **Le portefeuille soutenable est d'un socle de pilotage plus deux projets actifs** (scénario central), et **aucun projet exploratoire** tant qu'il n'est pas financé [ES/PR]. Mener les huit propositions de front dans 20 JP laisse 1 à 1,5 JP de production par proposition : c'est irréaliste.
7. **Morgan est le point de défaillance unique** : relation client, prix, validation de tout livrable (METH:15), comptes des outils et des artefacts, abonnements en échec de prélèvement (NOTE:8). Mathys l'est pour le code du CRM.
8. **Sur les onze processus étudiés, aucun ne justifie un développement spécifique au départ.** Neuf relèvent d'une organisation plus simple et d'outils existants bien configurés, avec l'IA en assistance contrôlée. Deux admettent une intégration légère après essais : la recherche documentaire et la détection des incohérences.
9. **Pilote proposé** : registre des décisions et comptes rendus, qualification CRM sur 20 comptes, recherche documentaire avec citations et, en option, détection des incohérences. Chaque essai a une référence mesurée avant de commencer, des critères d'adoption et d'abandon chiffrés, et des cas difficiles. Coût humain total : **environ 12 à 20 JP sur huit semaines** [ES], à financer.
10. **« Le travail de 100 personnes à deux » demanderait un multiplicateur de 50 à 85 par journée-personne** [ES]. Aucune pièce ne l'approche. Ce qui est plausible : ×2 à ×10 sur des tâches étroites et vérifiables, et **10 à 30 % de capacité libérée la première année** sur les processus pilotés [HY]. La contrainte réelle est la vente, la validation et la décision, pas la production.
11. **Rien ne doit toucher des données réelles avant le traitement de la fuite.** Il faut décider de la notification à la CNIL, désigner le responsable de traitement, signer les contrats de l'article 28, utiliser des offres professionnelles d'IA avec analyse d'impact des transferts (Anthropic et OpenAI ne sont pas sur la liste du DPF au 4 nov., [MM] rj-R4 et ver-R4), journaliser, et prévoir l'arrêt et la reprise manuelle (section 8).

---

## 1. Matrice des compétences de Morgan et de Mathys

Statuts : **démontrée** (une réalisation existe et a été constatée) ; **déclarée** (affirmée, sans réalisation constatée) ; **en cours d'acquisition** (essais, simulations, documents de travail) ; **à sous-traiter** (métier réglementé ou spécialité hors de portée) ; **dépendante** (repose sur un partenaire ou un équipement qui n'appartient pas aux associés).

Précision importante : « démontrée » veut dire qu'un objet existe. Cela ne prouve ni sa qualité vue par un client, ni son usage, ni la part de travail personnelle face à l'IA. Presque toutes les productions ont été écrites par des sessions d'assistants (48 commits « Claude » sur le CRM, ex-C5 aff. 4 ; textes de BOJART, ex-C7 l. 36) [FV].

### 1.1 Morgan Olsen

| Compétence | Statut | Preuve ou source | Code | Ce que cela vaut pour GianLuca |
| --- | --- | --- | --- | --- |
| Piloter des sessions d'assistants IA et produire vite une documentation et du code abondants | **Démontrée** (production) | Dépôt BOJART : 933 fichiers suivis, ≈ 19 700 lignes Python, 973 fonctions de test, 7 workflows CI, produits du 30 oct. au 2 nov. (ex-C7 l. 61-62, corr. ver-C7 n° 16) | [FV] ; part écrite personnellement [IN] | Capacité de production réelle. La densité documentaire risque toutefois de consommer la capacité plutôt que de produire des livrables réceptionnés (ex-C7 § 9). |
| Discipline de preuve : séparer mesuré, simulé, déclaré et proposé ; empreintes, restaurations vérifiées | **Démontrée** dans un dépôt | B/context/CURRENT.md:70 ; B/data/knowledge/claims.jsonl (ex-C7 l. 63) | [FV] | La compétence la plus directement utile à des « décisions préparées ». |
| Intégration continue multi-plateforme, bancs de mesure | **Démontrée**, avec réserves | 7 workflows ; mesures de mémoire documentaire (1 260 recherches) et de commandes (810 essais) [MM] ; mais la CI n'exécute pas les suites Jarvis M07 (ver-C7 n° 5) | [FV] / [MM] | Méthode transférable aux essais du pilote (section 6). |
| Supports commerciaux et diaporamas | **Démontrée** (objets existants), avec assistant | `deck/` (11 diapositives actives), vernissage (12 p.), note de vision V | [FV] existence ; acceptation client [IN] | Utile. Mais les versions divergent (13 contre 11 diapositives, offre écrite non corrigée) : la gestion des versions n'est pas maîtrisée. |
| Production vidéo avec fournisseurs IA | **Démontrée** en coupes de travail | Film R03 de 9,25 s ; refus « ip_detected » et « nsfw » enregistrés ; aucun master approuvé (B/creative/CURRENT.md:9-16 ; ex-C7 l. 23) | [FV] / [MM] historique | Secondaire pour le pilotage. Risque de droits et d'étiquetage (AI Act, art. 50). |
| Relation client, connaissance du terrain, diagnostic technique, créativité | **Déclarée** | METH:15 et R:1407 (« complémentarité à éprouver ») | [DR] | À éprouver. Le besoin de GianLuca n'est connu qu'à travers Morgan (syn-portefeuille § 1). |
| Vente et encaissement | **Non démontrée**, avec des contre-indices | OLSEN : 36 propositions de 2 200 à 4 600 € HT et 72 brouillons préparés, **aucun envoyé** ; 503 prospects tous « À faire » (NOTE:9). Aucune facture Marwin (OFF:29 ; V5 p. 17) | [DR] | Point le plus faible pour une activité qui doit trouver un second client (AUDIT:55, 103). |
| Direction des opérations | **Déclarée** (souhait) | « Aux direction des opération de cosne cours sur Loire » (`sources/chatgpt-conversations/2026-11-04/travail-pour-marwin-studio.json:140`) | [DR] | Aucune expérience documentée de gestion d'établissement. |
| Sites web, pipelines d'agents OLSEN (forge, démarchage à 8 agents, régie) | **Déclarée** | CORPUS:74, 102, 144-147, 196, 368 ; dépôt `olsen-ai-intelligence` inaccessible (NOTE:22) ; aucune vente (corr. ver-C4 n° 11) | [DR] | Ne pas présenter comme référence client. |
| Drone, tournage, storyboard (« Shelby ») | **Déclarée** (titres d'artefacts) | NOTE:15 | [DR] | Activité concurrente en temps (section 2.2). |
| Robotique (bras, banc d'essai) | **En cours d'acquisition** : simulations seulement | V:64-68 ; LAB exige des « compétences démontrées, pas présumées » (ex-C8:323) | [ES] | À sous-traiter à un intégrateur pour tout usage réel (sécurité machines). |
| IA locale (Ollama, modèle 4B, « local d'abord ») | **En cours** : profil préparé, aucun essai sur le poste | ex-C7 l. 17 et 20 ; le « local d'abord » dépend en fait de services payants (ex-C7 l. 162) | [FV] | Pas de base pour vendre un copilote local. |
| CAO et mécanique (Éclosion) | **En cours** : ébauche annoncée par ChatGPT | ex-C2 n° 64 | [DR] | Hors périmètre de GianLuca. |
| Structuration juridique, fiscale, sociale | **En cours** (documents de travail) ; **à sous-traiter** pour toute validation | V5 ; `choix-structure-2026-10-29.pdf` ; « non validé » (OFF:296) | [ES] | Expert-comptable et avocat obligatoires. |
| Impression 3D (≈ 10 machines) | **Dépendante d'un partenaire**, retiré le 4 nov. | « J'ai également accès à un atelier d'environ dix imprimantes 3D » (ACC:21) ; « probablement le parc de Medhi » (corr. ver-C2 n° 11) [HY] ; retrait (NOTE:25) | [DR] / [HY] | **Capacité à retirer de toute promesse**, y compris de la couverture du diaporama (cover.html, imprimante 3D en image). |
| Tour RTX 4060 Ti, voix, écrans | **Dépendante** d'un équipement de propriété inconnue | « poste RTX 4060 Ti de BOJ.ART » (B/docs/memory/POSTE_RTX4060TI.md:1) ; installation non qualifiée (B/jarvis/README.md:14) | [FV] / [IN] propriété | Un copilote de pilotage ne doit pas en dépendre (ex-C7 § 9). |
| Outils payants (Notion, ChatGPT Pro, ElevenLabs, Base44…) | **Dépendante** de comptes personnels | Échecs de prélèvement depuis fin octobre (NOTE:8) | [DR] | Risque de continuité immédiat (section 8). |

### 1.2 Mathys Couet

| Compétence | Statut | Preuve ou source | Code | Remarque |
| --- | --- | --- | --- | --- |
| Recherche et structuration d'un dossier de prospection | **Démontrée** en recherche et rédaction assistée ; **non démontrée** en exécution commerciale | `sources/dossier-partenariats-vieux-relais-et-le-m-2026-10-21.pdf`, 34 p., signé « @Mathys » (p. 1) ; verdict de ex-C6:277 | [FV] existence ; part personnelle [IN] | Plan mesurable, jamais exécuté, produit sans mandat (ex-C9 § 9.11). |
| Commande et cadrage d'un CRM produit par des agents | **Démontrée** comme donneur d'ordre | Recentrage demandé le 23/10 (`crm/PASSATION.md:7`) ; « le dépôt de Mathys » (`README.md:35`) | [DR] ; commits tous signés « Claude » [FV] | Seul donneur d'ordre nommé dans le CRM. Son code personnel : [IN]. |
| « La technique, le CRM, l'exploitation » | **Déclarée** | R:440 ; partage de la parole « Mathys : technique et CRM » (R:534, R:804) | [DR] | Texte rédigé par un assistant à partir des propos de Morgan. |
| Développement logiciel, sécurité, hébergement | **Inconnue** | Version Firebase non configurée (`crm/autonome/public/config.js:6-9`) ; écriture libre sur `/suivi` (ex-C5 aff. 25) | [FV] / [IN] | Les défauts du CRM ne disent rien de ses compétences : on ignore qui a décidé quoi. |
| Robotique, création, Jarvis | **Absente** des pièces | Aucune occurrence dans BOJART (ex-C7 l. 31) ; aucun rôle dans les créations (ex-C8:230) | [FV négatif] | La co-titularité du code Jarvis (V:84) n'a aucun appui. |
| Disponibilité | **Inconnue** | « Temps de Mathys non fixé » (AUDIT:62) ; jalon « rôles et disponibilité » ouvert depuis le 26 oct. (R:1388 ; STR:85) | [IN] | C'est la principale inconnue du modèle de charge. |

### 1.3 Le binôme : compétences manquantes ou à confier

| Domaine | État | Source | Traitement proposé [PR] |
| --- | --- | --- | --- |
| Vendre, signer, facturer, encaisser | Jamais fait sous Marwin (0 contrat, 0 facture) | OFF:29 ; AUDIT:13-14 | Premier objectif : un cadrage court payé (syn-portefeuille § 0.7). |
| Maintenir un outil dans la durée | Non démontré (CRM, Jarvis) | ex-C5 § 9.9 ; ex-C7 § 9 | Chiffrer la maintenance à part ; responsable nommé. |
| Coordonner des prestataires, mener un événement, gérer l'administratif d'établissements | Aucune preuve | ex-C2 § 6 (« Aucune preuve de capacité démontrée sur ce volet ») | Coordination seulement, sous mandat ; exécution par l'équipe de GianLuca ou un prestataire local (AUDIT:100). |
| Conformité des données | Contre-preuve : dépôt public | rj-R4 (c) | Avocat ou DPO externalisé (400 à 2 500 € HT par mois, rj-R6 (e), source secondaire [DR]). |
| Méthode de conseil | « reste à éprouver en mission réelle » | PIL:22 | Le pilote (section 6) sert aussi à l'éprouver. |

**À sous-traiter de façon permanente** [PR] : expertise comptable et fiscale (dont l'article 238 bis AB et l'argument de déduction du CRM), conseil juridique (contrats, RGPD, droit du travail, propriété intellectuelle), assurance, intégration et sécurité robotiques, photographie et vidéo professionnelles des œuvres si la qualité l'exige, appels sortants (Quali Contact, payé par GianLuca), sécurité des événements recevant du public (exploitant ou chargé de sécurité).

### 1.4 Effet de la décision du 4 novembre sur la capacité

| Capacité ou promesse | Avant le 4 nov. | Après le 4 nov. | Source |
| --- | --- | --- | --- |
| Accès à un atelier d'impression 3D | Présenté comme un atout (ACC:21, 119) | Indisponible, sauf accord séparé [HY] | NOTE:25 ; corr. ver-C2 n° 11 |
| Option laboratoire (diapositive toujours active) | Geste robotique cible : premier trait de STRATES (OFF:84) ; disponibilité de BOJ.ART à vérifier (V5 p. 13) | Sans objet ni atelier identifié | corr. ver-C2, omission 2 ; ex-C7 § 6.11 |
| Jarvis livrable à GianLuca | « Copilote Jarvis » de 4 JP au mois 1 (OFF:60) ; Jarvis attribué à Medhi (OFF:90) | Propriété du code [IN] ; nom à éviter tant qu'elle n'est pas réglée | ex-C7 § 4 ; corr. ver-C7 n° 10 |
| Vernissage « Strates » | Repose sur « le parc de Medhi en état » (`pour-carlone/vernissage-strates-idees.md:100`) | Format le plus simple lui-même fragilisé | ver-C2 § 1 |
| Charge de mise en cohérence | — | Au moins quatre supports à dater ou corriger : offre écrite, STRATES v1.1, vernissage, PDF de 13 pages de la PR n° 1 | [FV] ce soir |

---

## 2. Modèle de charge mensuel pour deux personnes

### 2.1 Calendrier et disponibilité individuelle

| Élément | Valeur | Code | Source |
| --- | --- | --- | --- |
| Jours ouvrés, décembre 2026 à novembre 2027 (lundi-vendredi hors fériés) | 253 au total ; 21,1 par mois en moyenne ; de 19 (mai 2027) à 22 | [FV] calcul | `charge.py` |
| Congés | 25 jours par an (5 semaines) ; 30 jours en hypothèse haute | [HY] | Hypothèse : un indépendant ne s'impose pas de congés, mais ne pas en prendre n'est pas soutenable |
| Maladie et indisponibilités | 5 à 10 jours par an | [HY] | Ordre de grandeur, à ajuster |
| Formation, veille, outils | 6 à 12 jours par an | [HY] | Nécessaire avec des outils d'IA qui changent tous les trimestres (rj-R6 (d) : doublements de prix Gemini au 1er déc. 2026 et au 1er janv. 2027) |
| **Disponibilité par personne** | **≈ 17,5 JP par mois** (16,8 à 18,1 selon les hypothèses) | [ES] | (253 − 25 − 8 − 10) ÷ 12 |

Une couverture sur trente jours calendaires ne vaut donc pas trente journées de production. L'archive du 29 oct. l'écrivait : « La disponibilité éventuelle pendant trente jours calendaires ne correspond ni à trente journées de production ni à une astreinte permanente » (ACC:64). Ce garde-fou a disparu de la version du 2 nov. (ex-C2 n° 43).

### 2.2 Part du temps consacrée à Marwin : les autres projets de Morgan, l'inconnue Mathys

**Morgan mène en parallèle**, d'après les pièces [FV pour l'existence des artefacts, DR pour l'activité] :
- OLSEN : plan « Vendre 10 sites », 503 prospects, 36 propositions (NOTE:9) ;
- projets personnels de vente en ligne (NOTE:10) ;
- film « Shelby » (7 artefacts des 3 et 4 nov.), Côme Millot, maréchal-ferrant (3 artefacts), kit parrainage, audit enveloppebulle.com (NOTE:15) ;
- BOJ.ART avec Medhi (4 artefacts des 2 au 4 nov., NOTE:14 ; dépôt BOJART très actif du 30 oct. au 2 nov.) ;
- une console qui suit « 24 dossiers, 22 dépôts, cinq films et huit missions » (R:1517 ; APIL:11, 13) ;
- des difficultés administratives : domiciliation résiliée, domaines suspendus, abonnements en échec (NOTE:6-8).

Sa disponibilité réelle pour Carlone n'est documentée nulle part (NOTE:17) [IN]. Celle de Mathys non plus (AUDIT:62) [IN]. D'où trois scénarios, plus un plafond théorique [HY] :

| Scénario | Part de Morgan pour Marwin | Part de Mathys pour Marwin | Ce que cela suppose |
| --- | --- | --- | --- |
| Prudent | 50 % | 25 % | Morgan garde OLSEN, BOJ.ART et ses projets clients ; Mathys a un autre emploi ou d'autres études |
| Central | 65 % | 50 % | Morgan réduit fortement ses autres projets ; Mathys à mi-temps |
| Haut | 90 % | 90 % | Les deux se consacrent presque entièrement à Marwin ; Morgan arrête l'essentiel du reste |
| Plafond théorique | 100 % | 100 % | Aucun autre projet, frais internes minimaux : sert seulement de borne |

### 2.3 Charge mensuelle par poste, en journées-personnes (régime de croisière)

Calculs [ES] faits avec `charge2.py`. Les postes non facturables sont ceux que l'abonnement ne paie pas directement. La « réserve d'aléas » couvre les incidents internes, les urgences non facturées et les reprises (8 % du temps brut ; 5 % pour le plafond).

| Poste (JP par mois) | Prudent | Central | Haut | Plafond |
| --- | --- | --- | --- | --- |
| Temps brut pour Marwin : Morgan + Mathys | 8,8 + 4,4 = **13,1** | 11,4 + 8,8 = **20,1** | 15,8 + 15,8 = **31,5** | 17,5 + 17,5 = **35,0** |
| Administration de Marwin (comptabilité, factures, banque, assurances, registre RGPD, contrats) | 2,0 | 2,0 | 2,5 | 2,0 |
| Prospection d'un second client (recommandée d'ici le mois 4, AUDIT:55, 103) | 1,5 | 2,5 | 3,5 | 1,5 |
| Maintenance et support internes non facturés (outils de Marwin, sécurité, sauvegardes, abonnements) | 1,0 | 1,5 | 2,0 | 1,0 |
| Capitalisation des méthodes non facturée | 0,5 | 0,75 | 1,0 | 0,5 |
| Réserve d'aléas | 1,1 | 1,6 | 2,5 | 1,8 |
| **Total non facturable** | **6,0** | **8,4** | **11,5** | **6,8** |
| **Capacité facturable réaliste** | **≈ 7** | **≈ 12** | **≈ 20** | **≈ 28** |

### 2.4 Ce que contient une journée facturée

L'archive du 29 oct. le disait : « Les réunions, la préparation, la coordination, les déplacements et les corrections consomment cette capacité » (ACC:64) [PR]. Ventilation proposée pour une mission de pilotage [ES] :

| Poste facturable | Part | Prudent | Central | Haut | Hypothèse |
| --- | --- | --- | --- | --- | --- |
| Réunions et coordination (client, interne, prestataires) | 22 % | 1,6 | 2,6 | 4,4 | Voir le calcul des réunions ci-dessous |
| Collecte et préparation des informations | 13 % | 0,9 | 1,5 | 2,6 | Accès souvent incomplets au début (APIL:11 : CRM, logiciel de Quali Contact et machines « hors d'accès vérifié ») |
| Contrôle et corrections | 15 % | 1,1 | 1,8 | 3,0 | Plus élevé tant que les sorties d'IA ne sont pas éprouvées : 283 des 471 numéros du CRM restent « à confirmer » (ex-C5 aff. 9) |
| Déplacements et présence sur les lieux | 10 % | 0,7 | 1,2 | 2,0 | Lieu de résidence des associés [IN] ; bureaux proposés à Cosne-Cours-sur-Loire [DR] |
| Maintenance et support des outils du client (CRM, automatisations) | 8 % | 0,6 | 0,9 | 1,6 | Facturable seulement si le contrat le prévoit |
| **Production de livrables** | **32 %** | **2,3** | **3,8** | **6,4** | Le reste |

**Calcul des réunions récurrentes** [ES] : une réunion hebdomadaire de 2 h avec GianLuca et une réunion interne d'1 h coûtent :
- 2,5 JP par mois si un seul associé assiste à la réunion client ;
- 3,7 JP par mois si les deux y assistent ;
- plus environ 1 JP de coordination des prestataires.

Deux personnes présentes une journée consomment deux journées-personnes. **Règle proposée [PR] : un seul associé par réunion client, sauf décision qui demande les deux.**

### 2.5 Les premiers mois : une charge de démarrage non facturable

| Chantier de démarrage | JP [ES] | Facturable ? | Source |
| --- | --- | --- | --- |
| Traitement de la fuite (dépôt privé, fiche de violation, décision de notification avec l'avocat, contrôle des copies) et mise en conformité minimale (responsable de traitement, registre, analyse d'intérêt légitime, contrat de l'article 28) | 3 à 6 | **Non** : l'exposition est de notre fait | rj-R4 (b) et (c) ; syn-portefeuille § 0.7 |
| Immatriculation, compte professionnel, RC professionnelle, outil de facturation | 3 à 5 | Non | AUDIT:94-96 |
| Contrat-cadre, fiches de mission, procédure de sortie, inventaire des accès et des outils | 2 à 4 | Non (ou inclus dans le cadrage) | V5 p. 2 et 4 ; ver-C2, omission 4 |
| Mise en cohérence après la décision du 4 nov. (offre écrite, STRATES v1.1, vernissage, PDF de 13 p., note de vision, diapositive laboratoire) | 1 à 2 | Non | Fait nouveau n° 1 |
| **Total sur les mois 0 à 2** | **9 à 17** | — | — |

Au premier trimestre, la capacité facturable baisse donc d'environ 3 à 6 JP par mois par rapport au régime de croisière [ES].

### 2.6 Comparaison avec les 20 et 40 journées des archives

| Formule des archives | Ce qu'elle demande | Verdict [ES] |
| --- | --- | --- |
| Base : 20 JP, 15 000 € HT par mois, « environ un mi-temps pour chacun » (OFF:13-15) | 27 à 29 JP de temps brut, soit **78 à 83 % du temps disponible des deux associés**. Partagé à égalité : 14,5 JP sur 17,5 chacun | **Tenable seulement dans le scénario haut**, c'est-à-dire si Morgan arrête l'essentiel de ses autres projets et si Mathys est disponible à 90 %. Ce n'est **pas** un mi-temps. Production pure : environ 6 à 7 JP. |
| Renforcement : 40 JP, 30 000 € HT par mois, « environ un plein temps » (OFF:15) | 49 à 51 JP de temps brut, soit **140 à 145 % du temps disponible des deux** | **Impossible** à deux, même sans aucun autre projet ni prospection. Supposerait un recrutement ou une sous-traitance d'environ 12 à 20 JP par mois, avec leur marge et leur encadrement. |
| Ancre : renforcement plus laboratoire, 46 JP (OFF:246 ; ex-C2 C4) | Au-delà même du plafond théorique de 35 JP bruts | **Impossible.** LAB p. 8 le notait : à 26 JP, « il resterait 14 jours pour administration, vente et autres travaux » sur 40 théoriques, et « leur disponibilité n'est pas établie » [FV]. |
| « Mener les huit propositions de front demande plus de 20 journées » (OFF:63) | 2,5 JP par proposition, dont 1 à 1,5 JP de suivi minimal | **Irréaliste** : 1 à 1,5 JP de production par proposition et par mois [ES]. |

**Lecture pour le prix et le contrat.**
- Dans le scénario central, environ 12 JP facturables correspondent, au taux de 750 €, à environ 9 000 € HT par mois [ES]. Ce chiffre ne dit rien de la valeur pour le client ; il borne seulement ce que le binôme peut tenir.
- Le marché du « temps partagé » vend plutôt 2 à 8 jours par mois (rj-R6 (e)) [HY]. Le volume de 20 JP est atypique, et il n'est pas tenable sans changer l'organisation des associés.
- Le contrat doit fixer une capacité **engagée nominativement** (qui, combien de jours) une fois la fiche « rôles et disponibilités » faite (R:1388) [PR].

---

## 3. Projets simultanés, incompatibilités et dépendances

### 3.1 Nombre de projets simultanés soutenable

Hypothèses [ES] :
- un socle de pilotage (registre des décisions, tableau de bord, réunion hebdomadaire, compte rendu) coûte 2 à 3 JP par mois ;
- chaque projet actif demande un suivi minimal de 1 à 1,5 JP par mois (réunions, relances, contexte à reprendre) ;
- un projet n'avance réellement qu'avec au moins 2 à 3 JP de production par mois ;
- un projet actif coûte donc environ 3,5 à 4,5 JP par mois.

| Scénario | Capacité facturable | Socle de pilotage | Projets actifs soutenables | Projets en veille | Projet exploratoire |
| --- | --- | --- | --- | --- | --- |
| Prudent | ≈ 7 JP | 2 JP | **1** | 1 (suivi léger) | 0 |
| Central | ≈ 12 JP | 2,5 JP | **2** | 1 à 2 | 0 |
| Haut | ≈ 20 JP | 3 JP | **3 à 4** | 2 | 1 au plus, plafonné à 10 % de la capacité et financé |

**Règle proposée [PR].** Limite d'encours écrite au contrat : « un socle plus N projets actifs », N étant fixé par la capacité nominative engagée. Toute demande nouvelle remplace un projet actif ou passe en lot séparé. La règle « trois priorités par mois » (AUDIT:60 ; deck/slides/premier-mois.html:42) va dans ce sens, mais une priorité n'est bornée ni en jours ni en livrables (ex-C4 n° 12). La règle doit compter en JP et en livrables, pas en « priorités ». Le laboratoire proposait déjà « trois travaux maximum, un seul essai exploratoire » (ex-C8:230).

### 3.2 Tâches incompatibles dans le temps

| Tâche A | Tâche B | Pourquoi elles s'excluent | Règle proposée [PR] |
| --- | --- | --- | --- |
| Événement ou vernissage (présence sur place, souvent des deux associés, sur plusieurs jours) | Clôture mensuelle, rapport, réception de livrables | Même fin de mois, mêmes personnes | Pas d'événement dans les 3 derniers jours ouvrés du mois ; rapport décalé et prévenu |
| Campagne d'appels pilote (relances à J+1 et J+3, import quotidien des résultats ; règles CRM, `rapport-crm-hermes360.md:40, 43` [DR]) | Journées sur le terrain, tournage, installation | Le retour des résultats doit être traité dans la journée | Un associé « de permanence campagne » désigné par semaine |
| Traitement d'un incident de données ou de sécurité | Toute production | L'incident passe avant tout, avec des délais légaux (72 h) | Gel des autres travaux ; client prévenu |
| Validation des livrables par Morgan (seul validateur, METH:15) | Déplacements, tournages et autres projets de Morgan | File d'attente de validation | Délégation écrite de la validation technique à Mathys ; délai maximal de 2 jours ouvrés |
| Mise en place des outils et des accès (semaines 1 à 4) | Livrables de production promis au mois 1 | Les accès conditionnent la production (APIL:11) | Mois 1 : cadrage et accès d'abord ; pas de promesse de lot commercial avant d'avoir les accès |
| Prospection d'un second client | Pics de charge chez GianLuca | La prospection est toujours la variable sacrifiée | Plancher de prospection protégé : 1,5 à 2,5 JP par mois |
| Projets personnels de Morgan (OLSEN, Shelby, BOJ.ART) | Engagements nominatifs pour GianLuca | Mêmes jours, même personne | Calendrier partagé des indisponibilités, tenu à jour chaque semaine |

### 3.3 Dépendances à une seule personne ou à un seul fournisseur

| Point unique | Ce qui en dépend | Preuve | Réponse [PR] |
| --- | --- | --- | --- |
| **Morgan** | Relation client, prix, arbitrages commerciaux, validation de tout livrable (METH:15) ; 6 des 12 solutions de l'audit seul et 2 en partage (corr. ver-C4 n° 10) ; artefacts claude.ai et pages ChatGPT sur ses comptes (NOTE:12-16) | [FV] / [DR] | Binôme de secours nommé par processus ; procédures écrites ; coffre-fort partagé avec accès d'urgence ; outils du client sur des comptes du client |
| **Mathys** | Code et dépôt du CRM (« le dépôt de Mathys », README.md:35 ; les comptes consultés n'ont qu'un accès en lecture, corr. ver-C5 n° 11) | [DR] | Transfert du dépôt vers un compte de Marwin ou de l'entité de GianLuca ; deux administrateurs |
| **GianLuca Carlone** | Toutes les décisions, les accès, la validation ; aucun délégué connu | syn-portefeuille § 2.4 | Délégué nommé ; délai de réponse écrit ; « une absence de réponse ne vaut pas approbation » (ACC:103) |
| **Un seul client** | 100 % du chiffre d'affaires, avec en plus des bureaux et un investissement éventuels | AUDIT:55 ; OFF:148 | Plancher de prospection ; part maximale de revenus par client (V:88) |
| **Compte claude.ai hébergeant le CRM en service** | Suivi des appels (collection « suivi ») ; propriétaire non nommé | ex-C5 aff. 22 (corr. ver-C5 § 2) | Export immédiat ; hébergement sur un compte de l'entité cliente ; sauvegarde quotidienne |
| **Fournisseurs d'IA** (Anthropic, OpenAI) | Toute la production assistée | rj-R4 (e) | Deux fournisseurs configurés ; repli européen (Mistral) ou modèle local documenté |
| **Quali Contact** | Tous les appels si l'externalisation est confirmée ; outil inconnu | ex-C5 aff. 50-51 ; rj-R6 (c) : activité affichée de collecte de dons [FV] | Pilote au rendez-vous tenu ; format d'échange écrit avant tout développement |
| **Moyens de paiement des abonnements** | Notion, ChatGPT Pro, etc. en échec depuis fin octobre | NOTE:8 | Carte professionnelle de Marwin ; alerte sur échec ; abonnements du client à son nom |

---

## 4. Seuils de saturation et réponses prévues

Les seuils sont des propositions à fixer avec GianLuca [PR]. Ils sont mesurés chaque semaine dans le registre (processus 3) et revus au comité mensuel. « Vigilance » déclenche une information ; « action » déclenche la réponse prévue, décidée par écrit.

| Indicateur | Mesure | Vigilance | Action | Réponse prévue | Qui décide |
| --- | --- | --- | --- | --- | --- |
| **Tâches en attente** | JP des tâches acceptées non commencées ÷ capacité facturable restante du mois | > 1,0 | > 1,5, ou plus de 10 tâches en attente depuis plus de 10 jours ouvrés | **Report** : GianLuca choisit ce qui sort du mois ; les sorties sont consignées | GianLuca, sur proposition de Morgan |
| **Retards** | Livrables en retard de plus de 5 jours ouvrés sur l'échéance convenue | 1 | 2 dans le mois, ou un jalon critique en retard de plus de 10 jours ouvrés | **Réduction du périmètre** du mois suivant ; cause écrite (accès, décision attendue, capacité) | Comité mensuel |
| **Décisions bloquantes en attente du client** | Jours ouvrés depuis la demande de décision | > 5 | > 10 | **Report** automatique des jalons concernés, sans autorisation tacite (ACC:103) ; au-delà de 15 jours, revue du contrat | Morgan informe ; GianLuca décide |
| **Charge de contrôle** | (Temps de contrôle + corrections) ÷ temps de production, par processus assisté par IA, sur 2 semaines | > 30 % | > 50 % | Retour du processus au **mode manuel** ou assisté plus léger ; nouvel essai ; abandon si aucune baisse en 4 semaines | Responsable du processus |
| **File de validation** | Livrables en attente de validation interne | > 2 jours ouvrés | > 4 jours ouvrés | **Renforcement interne** : délégation de la validation technique à Mathys sur un périmètre écrit | Morgan et Mathys |
| **Incidents** | Incidents par processus et par mois | 1 incident mineur | 1 incident critique (fuite, action non autorisée, envoi erroné, perte de données) ou 2 incidents mineurs sur le même processus | **Arrêt** immédiat du processus ; reprise manuelle ; fiche d'incident ; information du client ; notification légale si nécessaire | Quiconque constate l'incident arrête ; Morgan informe le client |
| **Corrections** | Livrables refusés au premier passage ÷ livrables présentés | > 20 % | > 35 %, ou plus de 2 cycles de correction sur le même livrable | **Re-cadrage** du livrable (critères de réception écrits) ; pas de nouveau lot du même type avant correction | Comité mensuel |
| **Dépassement de la capacité réservée** | JP consommées ÷ JP réservées | > 90 % avant le 20 du mois | > 100 % | **Arrêt** des travaux non urgents ; avenant écrit ou report au mois suivant ; pas de travail gratuit | GianLuca, par écrit |
| **Taux d'occupation total des associés** | (Temps facturé + non facturé) ÷ temps disponible, sur le mois | > 85 % | > 95 % pendant 2 mois, ou plus de 2 semaines au-delà de 100 % | **Refus** de tout nouveau projet ; **sous-traitance** d'un lot de production ; au 3e mois, **recrutement** ou réduction du contrat | Morgan et Mathys |
| **Urgences hors plages convenues** | Nombre par mois | 1 | > 2 | Astreinte chiffrée à part (ACC:59, 105) ou **refus** | GianLuca et Marwin |
| **Prospection sacrifiée** | JP de prospection réalisés ÷ plancher prévu | < 75 % | < 50 % pendant 2 mois | **Réduction du périmètre** client pour libérer le plancher | Morgan et Mathys |
| **Impayés** | Jours de retard sur une échéance | > 0 (relance) | Relance restée sans effet | **Suspension** des travaux (OFF:207) | Morgan |

**Choisir la réponse.** La demande liste cinq réponses. Ordre recommandé [PR] :
1. **Report** : la cause est une décision du client ou un pic ponctuel.
2. **Réduction du périmètre** : la cause est un engagement trop large.
3. **Renforcement** : la cause est interne et passagère, par exemple une validation ou une absence.
4. **Sous-traitance** d'un lot délimité : la surcharge dure plus d'un mois sur un type de travail sous-traitable (production de contenus, développement, appels).
5. **Recrutement** : seulement après trois mois au-delà de 85 % d'occupation **et** un contrat renouvelé qui le finance.

---

## 5. L'apport de l'IA processus par processus

### 5.0 Préalables communs à tous les processus

| Règle | Contenu | Source |
| --- | --- | --- |
| **Données autorisées** | Aucune donnée personnelle réelle avant : décision sur la fuite ; responsable de traitement désigné ; contrat de l'article 28 ; registre ; information des personnes. Avant cela, seulement des données fictives ou des documents sans données personnelles | rj-R4 (b), (c) [FV] |
| **Outils d'IA** | Offres professionnelles uniquement (API, Team, Business, Enterprise), entraînement désactivé. Anthropic et OpenAI hors de la liste DPF au 4 nov. 2026 [MM], d'où des clauses contractuelles types et une analyse d'impact des transferts (AITD). Pseudonymisation quand c'est possible | rj-R4 (e) ; ver-R4 n° 11 |
| **Classement des actions** | Autonome : lire, chercher, résumer, proposer. Approbation humaine : envoyer, appeler, modifier le CRM, publier, engager une dépense. Interdite : payer, supprimer en masse, changer des droits | rj-R4 (f) (ANSSI, 30 oct. 2026, principe 3) |
| **Documents = données** | Toute instruction trouvée dans un document est signalée, jamais exécutée (exemples : `crm/PASSATION.md:32-38` ; B/AGENTS.md) | rj-R4 (f) ; ANSSI principe 6 ; OWASP ASI01 |
| **Calculs** | Les montants, sommes et dates sont calculés par formule (tableur, script), jamais par le modèle de langage | [PR] ; erreur constatée : l'« économie max » de `crm/art_merge.py:129` ignore le bénéfice (ex-C5 aff. 42) |
| **Mesure** | Temps total corrections comprises, erreurs restantes, coût par résultat accepté, cas d'échec conservés, essais refaits à chaque changement d'outil ou de modèle | METH:69 [PR] ; V5 p. 11 |
| **Ne rien vendre comme opérationnel** | « Les connecteurs et systèmes autonomes doivent être éprouvés dans leur environnement réel avant d'être vendus comme opérationnels » | METH:63 [PR] |

**Les cinq options comparées pour chaque processus.**
1. **Actuel** : ce qui existe aujourd'hui.
2. **Organisation simple** : règles, modèles, rituels, sans outil nouveau.
3. **Outils existants configurés** : assistants professionnels, tableur, Notion ou Airtable, CRM existant correctement hébergé.
4. **Intégration légère** : scripts ou automatismes simples (n8n, Make, export et import), avec journal et arrêt.
5. **Développement spécifique** : outil construit pour GianLuca.

Coûts en [ES], d'après rj-R6 (d) :
- assistants en équipe : 20 à 25 $ par siège et par mois ;
- Notion : 10 à 20 $ ; Airtable : 20 à 45 $ ; Pipedrive : 14 à 79 $ ;
- API : environ 80 € par mois pour un usage documentaire modéré sur un modèle intermédiaire ;
- pile d'outils complète : 150 à 260 € par mois en version sobre, 650 à 1 000 € en version confortable.

Le temps humain est compté en JP au coût interne. Le marché de l'assistant documentaire, d'après le corpus OLSEN [DR], est de 3 à 12 k€ de cadrage, 10 à 50 k€ de construction et 1 à 3 k€ par mois de fonctionnement (CORPUS:562).

---

### 5.1 Recherche dans les documents

| Canevas | Contenu |
| --- | --- |
| Besoin | Retrouver vite une information sourcée (décision, montant, version, engagement) dans un corpus dispersé : dépôt Git, artefacts claude.ai, pages ChatGPT, messagerie, Drive, Notion. L'inventaire a lu 169 conversations sur 219 (DEMANDE § 1) |
| Entrée | Question en langage courant ; corpus autorisé et daté |
| Données autorisées | Documents internes et documents du client couverts par le mandat ; **exclure** les fichiers de prospects (`crm/site/*.json`) et les données personnelles tant que les préalables ne sont pas réunis |
| Traitement | Recherche plein texte et sémantique ; réponse rédigée **avec citation chemin:ligne ou page** ; liste des versions concurrentes ; refus explicite si aucune source |
| Intervention humaine | Relecture de toute réponse utilisée pour une décision, un prix ou un engagement |
| Contrôle | Ouverture de la citation ; vérification de la date et du statut de la pièce (proposition ou décision) ; jeu de questions de test rejoué à chaque ajout important de documents |
| Sortie | Réponse courte, citations, avertissement sur les versions |
| Résultat à mesurer | Taux de réponses justes et correctement citées ; taux de refus corrects ; temps question → réponse vérifiée ; citations inventées (cible 0) |
| Mode | **Assisté par IA avec contrôle humain** |
| Erreurs possibles | Citation inventée. Version récente prise pour une décision approuvée (règle 5 de l'audit). Référence trouvée mais perdue dans le contexte transmis au modèle : 28,6 % des cas à 8 000 octets sur le banc BOJART [MM] (ex-C7 l. 13). Régression quand le corpus grossit (corr. ver-C7, omission 3). Instruction cachée dans un document exécutée. Alias de nom (« John-Lucas » [sic, lire GianLuca]) non reconnu |
| Cas exceptionnels | PDF scanné ou image ; visuels non archivés ; question qui demande un jugement ; documents contradictoires |
| Secours manuel | Registre des sources (organisation simple) et recherche plein texte (grep) ; question posée à la personne qui détient l'information |
| Responsable | Mathys pour l'outil ; l'auteur de la réponse pour sa vérification ; Morgan pour un usage client |

| Option | Contenu et coût complet [ES] | Qualité, fiabilité, maintenance, adoption |
| --- | --- | --- |
| 1. Actuel | Recherche manuelle dans des sources dispersées ; temps non mesuré [IN] | Contradictions non vues : la décision du 4 nov. n'a été propagée qu'au diaporama [FV] |
| 2. Organisation simple | Arborescence unique, règle de nommage et de datation, registre des sources avec statut (proposition, décision, archive) : 1 à 2 JP, puis 0,5 JP par mois | Fiable et peu coûteux ; dépend de la discipline. **Préalable aux options 3 et 4** |
| 3. Outils existants | Projets Claude Team ou ChatGPT Business avec fichiers : 1 à 2 JP, 40 à 50 $ par mois pour deux sièges | Rapide à adopter. Citations moins précises ; limite de taille ; données confiées au fournisseur sous contrat professionnel |
| 4. Intégration légère | Reprise de la brique de mémoire documentaire de BOJART (SQLite FTS5, citations avec lignes, sauvegarde testée) avec une API professionnelle : 4 à 8 JP, environ 1 JP par mois, API 10 à 80 € par mois | Meilleures citations. **Conditions** : droits sur le code réglés (ex-C7 § 4, propriété de Jarvis en litige), dépôt privé, essai sur des questions réelles en français |
| 5. Développement spécifique | « Copilote Jarvis » complet relié à la messagerie, à l'agenda, au CRM et à la comptabilité, éventuellement local sur DGX Spark (≈ 6 200 à 8 100 € HT pour 128 Go, corr. ver-R6 n° 12) : 20 à 50 JP et plus | Non justifié : aucun usage démontré, maintenance lourde. Repère de marché : 10 à 50 k€ [DR] |

**Verdict [PR]** : option 2 puis 3 ; option 4 seulement si l'essai 3 (section 6.3) montre que l'option 3 ne tient pas les critères **et** que les droits sur le code sont réglés.

---

### 5.2 Préparation des réunions et comptes rendus

| Canevas | Contenu |
| --- | --- |
| Besoin | Arriver en réunion avec les décisions attendues préparées ; sortir avec un compte rendu exact, des décisions datées et des actions attribuées |
| Entrée | Registre des décisions et des tâches (processus 3) ; notes ; transcription seulement avec l'accord de tous les participants |
| Données autorisées | Participants informés ; aucun enregistrement sans accord ; données personnelles limitées aux participants et aux sujets |
| Traitement | Ordre du jour généré à partir des décisions ouvertes et des échéances proches ; brouillon de compte rendu ; extraction « décision, responsable, échéance, source » |
| Intervention humaine | L'animateur relit et corrige ; GianLuca ou son délégué confirme les décisions. Le silence ne vaut pas approbation d'un engagement (ACC:103) |
| Contrôle | Chaque décision a un responsable, une date et une source ; comparaison entre le compte rendu et le registre ; aucune décision ajoutée qui n'ait été prise |
| Sortie | Compte rendu d'une page ; mise à jour du registre |
| Résultat à mesurer | Délai d'envoi (cible : moins de 24 h ouvrées) ; part des décisions complètes (cible : 100 %) ; corrections demandées ; temps humain par réunion |
| Mode | **Assisté par IA avec contrôle humain** |
| Erreurs possibles | Décision inventée ou mal attribuée ; nuance perdue (« à étudier » devenu « décidé ») ; information confidentielle envoyée à la mauvaise liste |
| Cas exceptionnels | Réunion informelle ou téléphonique sans notes ; participant qui refuse l'enregistrement ; décision contredite plus tard |
| Secours manuel | Modèle de compte rendu à remplir à la main |
| Responsable | L'associé qui anime la réunion |

| Option | Contenu et coût [ES] | Appréciation |
| --- | --- | --- |
| 1. Actuel | Rappels ChatGPT (8 rappels, état [IN], corr. ver-C2 n° 13) ; la préparation de comptes rendus n'est qu'un « usage à éprouver » (ACC:129) | Aucun compte rendu de rendez-vous avec GianLuca dans le dépôt (recherche « compte rendu » du 4 nov.) [FV négatif] ; aucune parole directe de lui (syn-portefeuille § 0.1) |
| 2. Organisation simple | Modèle d'ordre du jour et de compte rendu, rituel hebdomadaire : 0,5 JP | Indispensable |
| 3. Outils existants | Assistant professionnel pour rédiger ; transcription intégrée à l'outil de visioconférence, si l'on y consent : 0,5 à 1 JP, compris dans les sièges | Bon rapport coût-gain |
| 4. Intégration légère | Envoi automatique des actions extraites vers le registre : 2 à 3 JP | Utile après 2 mois d'usage stable, avec validation avant écriture |
| 5. Spécifique | — | Non justifié |

**Verdict [PR]** : options 2 et 3 ; option 4 éventuelle au 6e mois.

---

### 5.3 Suivi des tâches, échéances et décisions

| Canevas | Contenu |
| --- | --- |
| Besoin | Une seule vue fiable de ce qui est décidé, en cours, bloqué ou en retard, par projet |
| Entrée | Comptes rendus ; demandes du client ; échéances contractuelles et réglementaires |
| Données autorisées | Données de pilotage ; données personnelles réduites au nom des responsables |
| Traitement | Registre structuré (cinq états : à qualifier, cadrée, en réalisation, en réception, close, METH:65) ; résumé hebdomadaire généré ; détection des échéances proches ou dépassées par règles de dates |
| Intervention humaine | Mise à jour par le responsable de chaque tâche ; arbitrage par GianLuca des priorités |
| Contrôle | Revue hebdomadaire ; chaque tâche a un responsable, une échéance et un critère de réception |
| Sortie | Tableau de bord ; liste des décisions attendues ; relances préparées |
| Résultat à mesurer | Retards détectés avant l'échéance ; délai moyen des décisions ; part des tâches avec critère de réception ; échéances manquées |
| Mode | **Automatisation envisageable après essais** pour les rappels internes et le résumé ; **approbation humaine** pour toute relance externe |
| Erreurs possibles | Registre non tenu (cause principale d'échec) ; doublons ; relance envoyée à tort ; mauvais fuseau ou mauvaise date |
| Cas exceptionnels | Changement de priorité en cours de mois ; tâche sans responsable ; dépendance à un tiers silencieux |
| Secours manuel | Tableau imprimable et revue orale hebdomadaire |
| Responsable | Morgan pour le registre client ; Mathys pour l'outil |

| Option | Contenu et coût [ES] | Appréciation |
| --- | --- | --- |
| 1. Actuel | Rappels ChatGPT ; console « Offres et missions » sur données fictives, 33 tests, sans modèle d'IA [DR] (STR:120-122) ; `B/ops/orchestration.json` conçu pour des agents | Pas d'interface lisible par un client non technicien (ex-C7 § 6.3) |
| 2. Organisation simple | Un tableau partagé et un rituel hebdomadaire : 1 JP | Suffisant au démarrage |
| 3. Outils existants | Notion, Airtable ou monday, avec rappels natifs : 1 à 2 JP, 10 à 45 $ par siège et par mois | Bon choix si les comptes sont **au nom de l'entité de GianLuca** (réversibilité) |
| 4. Intégration légère | Résumé hebdomadaire automatique (n8n, environ 20 € par mois [DR], CORPUS:817) : 2 à 4 JP | Après essais |
| 5. Spécifique | Console Marwin adaptée : 10 à 30 JP | Risque d'adoption et de dépendance ; non justifié |

**Verdict [PR]** : options 2 et 3 ; option 4 pour le seul résumé hebdomadaire.

---

### 5.4 Préparation budgétaire et rapprochement des informations

| Canevas | Contenu |
| --- | --- |
| Besoin | Savoir, par projet, ce qui est budgété, engagé, facturé et payé, et repérer les écarts avant qu'ils coûtent |
| Entrée | Devis, bons de commande, factures, budgets ; exports comptables en lecture seule |
| Données autorisées | Sous mandat écrit ; accès en lecture seule ; **jamais d'identifiants bancaires confiés à un agent** |
| Traitement | Extraction des montants des PDF vers un tableur (IA, avec contrôle) ; rapprochements et sommes par formules ; liste des écarts |
| Intervention humaine | Vérification de chaque ligne au-delà d'un seuil ; **validation par l'expert-comptable** de tout ce qui touche à la comptabilité ou à la fiscalité |
| Contrôle | Totaux recalculés ; contrôle croisé HT, TVA et TTC ; contrôle d'unicité des factures ; tolérance zéro sur les montants |
| Sortie | Tableau budget, engagé et payé par projet ; liste des écarts et des décisions à prendre |
| Résultat à mesurer | Erreurs de montant détectées après coup (cible 0) ; délai de production du tableau ; écarts signalés avant dépassement |
| Mode | **Assisté par IA** (extraction) + calcul déterministe + **intervention humaine spécialisée** (expert-comptable) |
| Erreurs possibles | Confusion HT et TTC (l'acompte est écrit « 7 500 € » sans HT dans AUDIT:12, ver-C4 n° 3) ; honoraires et achats mélangés (les 30 000 € du laboratoire mêlent 13 500 € d'honoraires et 16 500 € d'achats, LAB p. 8) ; facture en double ; mauvaise entité |
| Cas exceptionnels | Entité payeuse inconnue [IN] ; devis non signé ; devise étrangère ; avoir |
| Secours manuel | Saisie manuelle dans le tableur |
| Responsable | Mathys pour la préparation ; l'expert-comptable de GianLuca pour la validation |
| **Frontière** | Marwin prépare et rapproche ; elle ne tient pas la comptabilité et ne gère pas la trésorerie. Le « suivi centralisé des encaissements, de la trésorerie et des factures » est à vérifier au regard de l'expertise comptable (ex-C2 Q19) [IN] |

| Option | Contenu et coût [ES] | Appréciation |
| --- | --- | --- |
| 1. Actuel | Budgets épars (PDF, tableur de 53 lignes pour STRATES) | Pas de vue consolidée |
| 2. Organisation simple | Modèle de budget par projet et registre des engagements : 1 à 2 JP | Indispensable |
| 3. Outils existants | Tableur partagé et export du logiciel comptable du client (logiciel [IN]) : 1 à 2 JP | Suffisant tant que le volume reste sous environ 50 pièces par mois [HY] |
| 4. Intégration légère | Extraction automatique des PDF vers le tableur, avec file de validation : 3 à 5 JP | Seulement si le volume le justifie |
| 5. Spécifique | — | Non justifié ; doublon avec les outils comptables |

**Verdict [PR]** : options 2 et 3.

---

### 5.5 Mise à jour et qualification du CRM

| Canevas | Contenu |
| --- | --- |
| Besoin | Disposer de fiches d'entreprises exactes, datées et appelables pour la vente d'œuvres aux entreprises |
| Entrée | 500 fiches (485 en campagne) ; sources publiques ; retours d'appels |
| Données autorisées | **Après mise en conformité seulement.** Données professionnelles en rapport avec la fonction ; liste d'opposition ; opposition Sirene. Entrepreneurs individuels, artistes et lignes personnelles (24 standards en 06/07, 25 e-mails grand public, ex-C5 aff. 33) **exclus** jusqu'à l'avis de l'avocat (rj-R4 (a)) |
| Traitement | Recherche par agents (comme du 22 au 30 oct.) ; dédoublonnage ; datation de chaque champ ; préparation des exports pour l'appelant |
| Intervention humaine | Validation d'un échantillon ; traitement des oppositions ; décision sur tout nouveau contact nominatif |
| Contrôle | Échantillon appelé ; numéros partagés (34 numéros sur 73 fiches, ex-C5 aff. 11) ; date de vérification renseignée (aujourd'hui 1 fiche sur 500, ex-C5 aff. 10) |
| Sortie | Fiches qualifiées avec source et date ; fichier d'appel au format de l'appelant |
| Résultat à mesurer | Taux de numéros joignables au premier appel ; part des fiches datées ; doublons ; oppositions respectées (cible 100 %) ; temps humain par fiche acceptée |
| Mode | **Assisté par IA avec contrôle** ; automatisation des contrôles de format et de doublons après essais ; **tout contact sortant = humain** |
| Erreurs possibles | Numéro faux (283 sur 471 « à confirmer ») ; suivi rattaché à la mauvaise entreprise (indexation par rang, ex-C5 aff. 56) ; argument fiscal surévalué (Textilot : 1 043 750 € affichés pour au plus environ 32 500 € d'impôt en moins par an, corr. ver-C5 n° 9) ; appel d'une entreprise opposée (choix délibéré de les garder appelables, `crm/PASSATION.md:22`, ver-C5 omission 1) ; nouvelle exposition des données |
| Cas exceptionnels | Standard de groupe ; holding sans numéro ; procédure collective ; changement de dirigeant |
| Secours manuel | Tableur maître et journal d'appels papier ou tableur |
| Responsable | Mathys (outil et données) ; responsable de traitement à désigner (entité de GianLuca [IN]) |

| Option | Contenu et coût [ES] | Appréciation |
| --- | --- | --- |
| 1. Actuel | Artefact claude.ai privé, suivi dans le navigateur ; version Firebase non configurée ; dépôt public | **Non conforme** ; à corriger avant toute autre option (3 à 6 JP non facturables) |
| 2. Organisation simple | Tableur maître, statut d'appel, journal, règles d'opposition : 1 à 2 JP | Robuste pour 20 à 100 comptes |
| 3. Outils existants | CRM existant hébergé en privé sur un compte de l'entité cliente, avec sauvegarde (1 à 3 JP) ; ou Pipedrive à 14 à 39 $ par siège | À choisir selon qui appelle (associés ou Quali Contact) |
| 4. Intégration légère | Échange de fichiers avec l'outil de Quali Contact une fois son format connu : 2 à 4 JP | **Pas avant** d'avoir un modèle de fichier réel (ex-C5 § 9.11) |
| 5. Spécifique | Module Hermes360, temps réel par webhooks | **Arrêter** : développé avant de connaître l'outil et contre la recommandation de sa propre étude (ex-C5 § 4, ligne « Hermes360 ») |

**Verdict [PR]** : conformité d'abord, puis option 2 pour le pilote de 20 comptes, puis option 3 ; option 4 si Quali Contact est confirmé.

---

### 5.6 Préparation des campagnes et supports commerciaux

| Canevas | Contenu |
| --- | --- |
| Besoin | Scripts, e-mails, fiches d'offre et supports conformes et cohérents pour la vente d'œuvres |
| Entrée | Offres validées par GianLuca (catalogue de 9 offres encore au stade de brouillon, ex-C2 § 6) ; cibles ; arguments fiscaux **validés par écrit** par l'expert-comptable |
| Données autorisées | Segments et caractéristiques d'entreprises ; aucune donnée personnelle nécessaire pour concevoir les supports |
| Traitement | Brouillons et variantes ; contrôle automatique d'une grille de conformité (identité de l'expéditeur, opposition, pas de rendement ni de rachat garanti, économie d'impôt « sous réserve ») |
| Intervention humaine | Morgan valide le message ; l'expert-comptable valide toute affirmation fiscale ; GianLuca valide l'offre et l'entité vendeuse |
| Contrôle | Grille de relecture (AUDIT:99) ; essai sur 20 comptes avant élargissement |
| Sortie | Kit de campagne versionné |
| Résultat à mesurer | Validation au premier passage ; résultats du pilote (joignabilité, rendez-vous, ventes) [MM] à venir |
| Mode | **Assisté par IA avec contrôle** ; **envoi soumis à approbation** humaine |
| Erreurs possibles | Promesse fiscale fausse ; mention interdite des lieux (filtre « INTERDIT », ver-C5 § 2) ; entité vendeuse absente des messages ; envoi à des opposés |
| Cas exceptionnels | Opposition commerciale de GianLuca à un argument ; changement d'offre ; artiste qui refuse une mention |
| Secours manuel | Modèles écrits à la main |
| Responsable | Morgan |

| Option | Contenu et coût [ES] | Appréciation |
| --- | --- | --- |
| 1. Actuel | Mail d'approche et discours dans `crm/PASSATION.md:27` ; chez OLSEN, 72 brouillons jamais envoyés (NOTE:9) | Production abondante, aucune diffusion |
| 2. Organisation simple | Modèles et grille de conformité : 1 JP | Indispensable |
| 3. Outils existants | Assistant professionnel et outils bureautiques ou graphiques sous licence professionnelle | Suffisant |
| 4. Intégration légère | Publipostage depuis le CRM, avec étape d'approbation, depuis une messagerie au nom de l'entité vendeuse : 2 à 3 JP | Après le pilote |
| 5. Spécifique | Démarchage multi-agents de type OLSEN | **Exclu** pour GianLuca : risques de réputation et de conformité |

**Verdict [PR]** : options 2 et 3 ; option 4 après le pilote.

---

### 5.7 Rédaction et production de contenus

| Canevas | Contenu |
| --- | --- |
| Besoin | Textes, visuels, vidéos courtes et dossiers pour la galerie, les événements et les réseaux |
| Entrée | Brief validé ; charte ; droits sur les œuvres et les images |
| Données autorisées | Œuvres et images dont les droits sont acquis ; aucune image de personne sans accord |
| Traitement | Brouillons de textes ; visuels d'intention générés ; montage |
| Intervention humaine | Relecture ; vérification des droits ; artiste consulté pour ses œuvres ; photographe professionnel pour les reproductions d'œuvres si la qualité l'exige |
| Contrôle | Mention « image générée par IA » pour tout visuel réaliste (AI Act, art. 50, applicable depuis le 2 août 2026, rj-R4 (d)) ; aucun personnage protégé (le site BOJ.ART présente Vegeta, Baki et Sukuna, ex-C7 l. 46) |
| Sortie | Contenus validés et datés |
| Résultat à mesurer | Validation au premier passage ; délai ; incidents de droits (cible 0) |
| Mode | **Assisté par IA avec contrôle** ; **humain spécialisé** pour la photographie d'œuvres |
| Erreurs possibles | Visuel pris pour une réalisation (« image générée par IA : une intention, aucune pièce encore réalisée », OFF:80) ; atteinte aux droits ; refus du fournisseur (« ip_detected ») |
| Cas exceptionnels | Œuvre sans accord de l'artiste ; fournisseur indisponible ou arrêté (API Sora 2 fermée le 24 sept. 2026, CORPUS:779-781 [DR]) |
| Secours manuel | Production classique ; photographe |
| Responsable | Morgan |

Options [ES] : 1. Actuel : visuels IA « non contractuels » et vidéos de travail. 2. Charte et brief : 1 JP. 3. Assistant et outils graphiques sous licence professionnelle : déjà dans la pile. 4. Aucune intégration utile. 5. Pipeline vidéo BOJART : **exclu**, propre à l'atelier (ex-C7 § 6.4).

**Verdict [PR]** : options 2 et 3, en **lots devisés** hors abonnement (syn-portefeuille § 4.1 E).

---

### 5.8 Coordination des prestataires

| Canevas | Contenu |
| --- | --- |
| Besoin | Que les prestataires de GianLuca (Quali Contact, artisans, traiteur, locations, techniciens) livrent à temps, au prix convenu et selon les règles |
| Entrée | Liste des prestataires, devis, contrats, planning |
| Données autorisées | Coordonnées professionnelles ; contrats sous mandat |
| Traitement | Registre des prestataires ; comparatif de devis (extraction par IA et contrôle) ; planning ; relances préparées |
| Intervention humaine | Morgan ou Mathys coordonnent ; **GianLuca signe et engage** dans les limites du mandat ; aucune commande sans accord écrit |
| Contrôle | Plafonds par dépense et cumulés ; double validation au-delà d'un seuil |
| Sortie | Planning, comparatifs, comptes rendus de chantier |
| Résultat à mesurer | Livraisons à l'heure ; écarts de prix ; litiges |
| Mode | **Coordination d'un prestataire**, préparée avec l'IA |
| Erreurs possibles | Engagement pris sans autorisation ; Marwin devient l'encadrant de fait des équipes de Quali Contact (risque juridique, rj-R6 (c) [HY]) ; devis mal comparés |
| Cas exceptionnels | Prestataire défaillant ; urgence un soir d'événement ; GianLuca injoignable |
| Secours manuel | Téléphone et tableur |
| Responsable | Morgan (relation) ; Mathys (registre) |

Options [ES] : 1. Actuel : rien de documenté. 2. Registre, modèle de demande de devis et règles de mandat : 1 JP. 3. Tableur et agenda partagés. 4 et 5. Non justifiés.

**Verdict [PR]** : options 2 et 3 ; **le mandat écrit compte plus que l'outil**.

---

### 5.9 Préparation administrative pour les professionnels compétents

| Canevas | Contenu |
| --- | --- |
| Besoin | Remettre à l'expert-comptable, à l'avocat, à l'assureur, à la mairie (ERP), à la Sacem ou au Guso des dossiers complets, pour qu'ils décident vite |
| Entrée | Pièces du client ; liste des exigences publiée par l'administration |
| Données autorisées | Sous mandat ; données minimales |
| Traitement | Listes de pièces ; synthèse ; questions précises ; chaque règle citée avec sa source officielle et sa date |
| Intervention humaine | **Le professionnel décide et signe.** Marwin ne donne ni conseil juridique ni conseil fiscal (METH:61 ; choix-structure p. 4, ver-C3 omission 3) |
| Contrôle | Chaque règle vérifiée sur une source officielle datée ; aucune règle tirée de la seule mémoire d'un modèle |
| Sortie | Dossier prêt à transmettre ; liste de questions |
| Résultat à mesurer | Dossiers renvoyés pour pièce manquante ; délai de traitement par le professionnel |
| Mode | **Assisté par IA**, puis **intervention humaine spécialisée** |
| Erreurs possibles | Règle périmée : les règles changent vite en 2026 (opt-in téléphonique du 11 août, Omnibus IA du 27 juillet, RGDU par décret du 12 juin ; rj-R4, ver-R6) ; règle inventée ; mauvaise entité |
| Cas exceptionnels | Règle en cours de réforme (omnibus RGPD non adopté) ; administration injoignable |
| Secours manuel | Liste de pièces fournie par le professionnel lui-même |
| Responsable | Morgan ; le professionnel pour la décision |

Options [ES] : 1. Actuel : documents de travail non validés (V5 ; « non validé », OFF:296). 2. Listes de pièces par démarche : 1 JP. 3. Assistant professionnel et dossier partagé. 4 et 5. Non justifiés.

**Verdict [PR]** : options 2 et 3.

---

### 5.10 Détection des incohérences et retards

| Canevas | Contenu |
| --- | --- |
| Besoin | Repérer avant le client les contradictions entre versions (prix, périmètre, calendrier, propriété) et les retards |
| Entrée | Registre ; documents versionnés ; budgets ; CRM |
| Données autorisées | Documents internes et documents du client sous mandat |
| Traitement | Contrôles **déterministes** (échéances dépassées, montants différents pour une même rubrique, nombre de diapositives, statut des versions) ; comparaison **sémantique** assistée par IA, avec citations, entre documents qui traitent du même sujet ; règle « décision → documents touchés » |
| Intervention humaine | Tri de chaque alerte : vraie, fausse, déjà connue |
| Contrôle | Jeu d'essai de contradictions connues |
| Sortie | Liste d'alertes datées, avec citations et proposition de correction |
| Résultat à mesurer | Rappel sur les contradictions connues ; précision des alertes ; temps de tri |
| Mode | **Automatisation envisageable après essais** pour les contrôles déterministes ; **assisté par IA avec contrôle** pour le sémantique |
| Erreurs possibles | Fausse assurance (contradiction de prix non vue) ; avalanche d'alertes inutiles ; citation inventée |
| Cas exceptionnels | Pièce non versionnée ; décision orale non écrite (la décision du 4 nov. est un exemple) |
| Secours manuel | Revue humaine mensuelle des documents de référence |
| Responsable | Mathys (outil) ; Morgan (tri des alertes client) |

| Option | Contenu et coût [ES] | Appréciation |
| --- | --- | --- |
| 1. Actuel | Contradictions découvertes par audit : 25 dans la seule offre (ex-C2 C1 à C25) ; décision du 4 nov. propagée à 1 support sur au moins 5 | Coûteux et tardif |
| 2. Organisation simple | Registre des documents de référence, avec la liste des documents à mettre à jour après chaque décision : 1 JP | Aurait évité la demi-application du 4 nov. |
| 3. Outils existants | Règles de dates et de montants dans le tableur | Simple |
| 4. Intégration légère | Script de comparaison de versions et passage d'un modèle avec citations : 3 à 6 JP | **Bon candidat** : un jeu d'essai réel existe déjà (cet audit) |
| 5. Spécifique | — | Non justifié |

**Verdict [PR]** : options 2 et 3 tout de suite ; option 4 en pilote facultatif (section 6.4).

---

### 5.11 Capitalisation des méthodes

| Canevas | Contenu |
| --- | --- |
| Besoin | Que chaque mission rende la suivante plus rapide, et qu'un associé puisse reprendre le travail de l'autre |
| Entrée | Comptes rendus de mission, erreurs, modèles de livrables, cas de test |
| Données autorisées | Méthodes et modèles **séparés des données confidentielles du client** (METH:73) |
| Traitement | Brouillon de procédure ou de modèle rédigé par l'IA à partir des notes ; relecture ; versionnement |
| Intervention humaine | Rédaction finale ; test de la procédure par l'autre associé |
| Contrôle | Une procédure n'est validée que si quelqu'un d'autre que son auteur l'a appliquée seul |
| Sortie | Bibliothèque de procédures, modèles et cas de test |
| Résultat à mesurer | Part des processus pilotés qui ont une procédure testée ; temps de reprise par l'autre associé |
| Mode | **Assisté par IA avec contrôle** |
| Erreurs possibles | Données du client mélangées aux méthodes génériques (risque de droits et de confidentialité) ; procédure obsolète |
| Cas exceptionnels | Méthode propre à un seul client ; outil remplacé |
| Secours manuel | Passation orale enregistrée par écrit |
| Responsable | Chacun pour ses processus ; Mathys tient la bibliothèque |
| **Droits** | Composants et méthodes génériques à Marwin, concédés au client ; développements propres au client, cédés au paiement (OFF:209 ; rj-R3) |

Options [ES] : 1. Actuel : passations très détaillées mais destinées à des agents (`crm/PASSATION.md` ; B/context/SESSION_HANDOFF.md, 244 lignes en trois jours). 2. Modèles et fiches de procédure : 1 à 2 JP. 3. Notion ou Drive. 4. Recherche documentaire (processus 5.1). 5. Non justifié.

**Verdict [PR]** : options 2 et 3. Le risque n'est pas de manquer de documentation, mais d'en produire trop, pour des agents plutôt que pour des personnes.

---

### 5.12 Tableau de synthèse des onze processus

| N° | Processus | Mode | Option retenue | Mise en place [ES] | Coût d'outils mensuel [ES] | Priorité |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Recherche dans les documents | Assisté IA + contrôle | 2 + 3 ; 4 sous conditions | 2 à 4 JP (4 à 8 JP si option 4) | 40 à 130 € | Pilote |
| 2 | Réunions et comptes rendus | Assisté IA + contrôle | 2 + 3 | 1 à 1,5 JP | Compris dans les sièges | Pilote (avec 3) |
| 3 | Tâches, échéances, décisions | Rappels internes automatisables après essais ; relances externes approuvées | 2 + 3 (+ 4 pour le résumé) | 2 à 3 JP | 10 à 45 $ par siège | Pilote |
| 4 | Budget et rapprochements | Assisté IA + calcul déterministe + expert-comptable | 2 + 3 | 2 à 4 JP | ≈ 0 | Après le cadrage |
| 5 | CRM | Assisté IA + contrôle ; contact sortant humain | Conformité, puis 2, puis 3 (+ 4 si Quali Contact) | 3 à 6 JP de conformité + 1 à 3 JP | 0 à 40 $ par siège | Pilote, après conformité |
| 6 | Campagnes et supports | Assisté IA + contrôle ; envoi approuvé | 2 + 3 | 1 JP | Compris | Après le pilote CRM |
| 7 | Contenus | Assisté IA + contrôle ; photographe | 2 + 3, en lots devisés | 1 JP | Selon les outils graphiques | Par lot |
| 8 | Prestataires | Coordination humaine préparée par IA | 2 + 3 | 1 JP | ≈ 0 | Selon les projets |
| 9 | Dossiers pour professionnels | Assisté IA + professionnel | 2 + 3 | 1 JP | ≈ 0 | Selon les besoins |
| 10 | Incohérences et retards | Déterministe automatisable ; sémantique assisté | 2 + 3 ; 4 en pilote | 1 JP (3 à 6 JP si option 4) | API ≤ 50 € | Pilote facultatif |
| 11 | Capitalisation | Assisté IA + contrôle | 2 + 3 | 1 à 2 JP | ≈ 0 | Continu |

**Exclusions de périmètre** [PR] : exécution administrative courante (AUDIT:100) ; tenue de la comptabilité ; conseil fiscal ou juridique ; appels sortants par agent vocal (« à ne pas vendre », CORPUS:322-338 [DR]) ; tout outil RH ou de notation de personnes (rj-R4 (d)) ; toute action financière par un agent.

**Ce que cela dit de la DGX Spark, du laboratoire et des architectures multi-agents.** Aucun des onze processus ne demande de calcul local, de GPU ou d'orchestration multi-agents pour démarrer. À environ 6 200 à 8 100 € HT, une DGX Spark de 128 Go représente plusieurs années d'usage documentaire par API (environ 80 € par mois) [ES] (corr. ver-R6 n° 12). Elle ne se justifie que par une contrainte démontrée de confidentialité ou de volume (`interne/complement-chatgpt-2026-11-04.md:37`), ce qui n'est pas le cas.

---

## 6. Pilote : quatre processus et leurs protocoles d'essai

### 6.0 Conditions et étapes

**Avant tout essai sur des données réelles** [PR] :
- fuite traitée et décision de notification prise avec l'avocat ;
- responsable de traitement désigné ;
- contrat de l'article 28 ;
- offres d'IA professionnelles, avec AITD ;
- entité cliente identifiée ;
- mandat écrit ;
- financement du pilote décidé. Le pilote coûte environ 12 à 20 JP sur huit semaines [ES], soit un mois à un mois et demi de la capacité facturable du scénario central : il doit être payé dans le cadrage, ou assumé comme un investissement plafonné.

**Trois étapes, chacune avec sa preuve** [PR] :

| Étape | Données | Preuve exigée pour passer à la suivante |
| --- | --- | --- |
| **Démonstrateur** (interne) | Fictives, ou documents internes sans données personnelles | Critères de qualité atteints sur le jeu d'essai ; temps humain total mesuré ; procédure de secours écrite |
| **Pilote client** (4 à 8 semaines) | Réelles, sur un périmètre restreint, après les préalables | Critères atteints sur 4 semaines consécutives ; aucune erreur critique ; utilisation réelle par le client ; coût par résultat accepté connu |
| **Exploitation régulière** | Périmètre convenu | 2 à 3 mois de critères tenus ; reprise manuelle testée ; sauvegarde et restauration testées ; responsable et maintenance chiffrés au contrat |

### 6.1 Pilote P1 : registre des décisions et des échéances, avec comptes rendus (processus 2 et 3)

| Élément | Protocole |
| --- | --- |
| Fonctionnement de référence | **Mesuré pendant 2 semaines avant l'essai** : temps passé par réunion (préparation, compte rendu, relances) ; part des décisions avec responsable et date ; échéances manquées. **Référence déjà constatée** : la décision du 4 nov. n'a été appliquée qu'à 1 support sur au moins 5 [FV] ; aucun compte rendu de rendez-vous avec GianLuca n'existe dans le dépôt (recherche du 4 nov.) [FV négatif] |
| Données et cas | Démonstrateur : réunions internes Morgan et Mathys, et projet de cadrage Carlone. Pilote : réunions avec GianLuca ou son délégué, avec accord sur la prise de notes |
| Volumes | 8 semaines ; au moins 8 réunions ; au moins 40 décisions ou actions |
| Qualité acceptable | 100 % des décisions avec responsable, date et source ; compte rendu envoyé en moins de 24 h ouvrées dans au moins 90 % des cas ; au plus 1 correction de fond par compte rendu |
| Erreurs critiques | Décision inventée ou attribuée à tort ; engagement traité comme approuvé faute de réponse ; information confidentielle envoyée hors de la liste prévue ou dans un outil grand public |
| Temps humain total | Préparation + relecture + corrections + reprises, chronométrés. Cible : au plus 70 % du temps de référence [HY], dans la ligne de l'objectif de −30 % des archives (V5 p. 11) |
| Coût des outils | Deux sièges professionnels (≈ 40 à 50 $ par mois) et un espace Notion ou Airtable (≈ 20 à 40 $ par mois) [ES] ; mise en place de 2 à 3 JP |
| Adoption | GianLuca ou son délégué réagit à au moins 80 % des comptes rendus dans les 3 jours ouvrés et consulte le registre au moins une fois par semaine |
| Abandon | Relecture et corrections dépassent 50 % du temps de référence pendant 4 semaines ; une erreur critique non détectée ; registre non consulté par le client après 4 semaines |
| Cas difficiles | Réunion sans notes ; propos contradictoires ; décision changée la semaine suivante (versionner, ne pas écraser) ; priorité modifiée en cours de mois ; outil indisponible (modèle manuel) ; participant qui refuse l'enregistrement ; GianLuca qui ne répond pas (report, pas d'autorisation tacite) |

### 6.2 Pilote P2 : qualification CRM et lot de 20 comptes (processus 5, et 6 pour le script)

| Élément | Protocole |
| --- | --- |
| Conditions | Conformité terminée ; structure vendeuse choisie ; argument fiscal validé par écrit ; décision sur qui appelle (associés ou Quali Contact) |
| Fonctionnement de référence | État constaté [FV] (ex-C5, corr. ver-C5) : 471 numéros dont 283 « à confirmer » ; 1 date de vérification sur 500 ; 34 numéros partagés par 73 fiches ; 14 oppositions, vérifiées pour 33 fiches ; aucun champ de suivi ; aucun appel, rendez-vous ni vente constaté. Référence de temps : qualification manuelle de 5 fiches, chronométrée |
| Données et cas | Démonstrateur : 10 entreprises fictives pour le format d'échange (`audit-crm-carlone.md:58-64`). Pilote : 20 comptes de priorité haute parmi les 37 cibles, entreprises seulement, sans entrepreneurs individuels ni lignes personnelles avant l'avis de l'avocat |
| Volumes | 20 comptes ; au plus 4 tentatives par compte sur 30 jours (règle du CRM [DR]) ; 2 semaines de préparation et 4 semaines d'appels |
| Qualité acceptable | Au moins 90 % des champs de contact avec source et date ; 100 % des numéros partagés signalés ; 100 % des oppositions respectées ; aucun argument fiscal non validé |
| Erreurs critiques | Contact d'une entreprise opposée par e-mail ; donnée personnelle sans base légale ; promesse fiscale erronée ; mention interdite ; nouvelle exposition du fichier |
| Temps humain total | Par fiche acceptée : recherche, vérification, préparation, réimport des résultats et corrections |
| Coût des outils | API de recherche : 10 à 50 € pour le lot [ES] ; téléphonie : grille Ringover à relire (19 à 69 € par utilisateur, corr. ver-R6), ou coût de Quali Contact payé par GianLuca (150 à 500 € HT par rendez-vous tenu sur le marché, rj-R6 (c), source secondaire [DR]) ; environ 5 à 7 JP de Marwin |
| Adoption | L'appelant utilise les fiches et renvoie au moins 90 % des résultats d'appel au format convenu |
| Abandon | Joignabilité inférieure à 50 % après les premières tentatives (changer de source avant d'élargir) ; conformité non tenue ; appelant qui n'utilise pas les fiches |
| Cas difficiles | Standard de groupe partagé ; holding sans numéro ; société en procédure ; opposition notée mais « appel direct » maintenu (à trancher par l'avocat) ; vente reportée par GianLuca ; outil de Quali Contact inconnu ; doublon entre deux fiches |
| Ce qui se mesure vraiment | Joignabilité, rendez-vous et ventes [MM] : **résultats qui dépendent aussi de GianLuca et de l'appelant**, à séparer de ce que Marwin contrôle (qualité des fiches, délais) |

### 6.3 Pilote P3 : recherche documentaire avec citations (processus 1)

| Élément | Protocole |
| --- | --- |
| Fonctionnement de référence | 30 questions types posées à la main sur le corpus Carlone. Mesure du temps jusqu'à la réponse vérifiée, de la justesse et des sources |
| Données et cas | Démonstrateur : dépôt Carlone privé **sans** le dossier `crm/` ni aucune donnée de prospects. Pilote : documents du client sous mandat |
| Volumes | **60 questions réelles** (au lieu des 14 du banc BOJART) : 35 ordinaires ; 15 pièges (versions contradictoires, montants HT et TTC, alias de nom, décision orale) ; 10 sans réponse dans le corpus. Jeu rejoué à chaque ajout d'au moins 10 documents (corr. ver-C7, omission 3) |
| Qualité acceptable | Au moins 90 % de réponses justes avec citation exacte ; au moins 95 % des questions sans réponse correctement refusées ; 0 citation inventée ; aucune version récente présentée comme une décision approuvée |
| Erreurs critiques | Citation inventée ; données confidentielles envoyées dans un outil grand public ; exécution d'une instruction trouvée dans un document |
| Temps humain total | Question → réponse vérifiée, relecture comprise. Cible : au plus 50 % du temps de référence [HY] |
| Coût des outils | Variante A (option 3) : projets Claude Team ou ChatGPT Business, ≈ 40 à 50 $ par mois, 1 à 2 JP. Variante B (option 4), seulement si les droits sont réglés : brique de mémoire de BOJART, 4 à 8 JP, API ≤ 80 € par mois. **Comparer A et B sur le même jeu de questions** |
| Adoption | Utilisé au moins trois fois par semaine par les deux associés pendant 4 semaines |
| Abandon | Moins de 80 % de réponses justes après réglage ; maintenance supérieure à 1 JP par mois ; une citation inventée non détectée |
| Cas difficiles | Versions contradictoires (la plus récente n'est pas forcément approuvée) ; PDF scanné ; visuels non archivés ; « John-Lucas » [sic, lire GianLuca] utilisé comme clé de recherche ; question qui demande un jugement ; outil indisponible (registre des sources et recherche plein texte) |

### 6.4 Pilote P4 (facultatif) : détection des incohérences et retards (processus 10)

| Élément | Protocole |
| --- | --- |
| Fonctionnement de référence | Contradictions déjà relevées par cet audit : C1 à C25 de ex-C2, avec les corrections des contrôleurs (ver-C2 n° 14 : C15 n'est pas une contradiction). C'est un jeu d'essai rare : on connaît la bonne réponse |
| Données et cas | 24 contradictions confirmées et 10 paires de passages concordants (pour mesurer les fausses alertes) ; registre fictif avec échéances dépassées |
| Volumes | Environ 35 cas sémantiques ; 50 tâches datées |
| Qualité acceptable | Rappel d'au moins 70 % sur les contradictions connues, et de 100 % sur celles qui touchent le prix, le paiement ou la propriété ; précision d'au moins 60 % ; 100 % des alertes de dates exactes |
| Erreurs critiques | Contradiction de prix ou de paiement non détectée ; alerte appuyée sur une citation inventée |
| Temps humain total | Tri : au plus 5 minutes par alerte en moyenne |
| Coût des outils | 3 à 6 JP ; API ≤ 50 € pour l'essai [ES] |
| Adoption | Utilisé avant chaque envoi de document au client |
| Abandon | Rappel inférieur à 50 %, ou tri plus long qu'une relecture humaine complète |
| Cas difficiles | Décision orale non écrite ; deux documents à des dates différentes, tous deux « en vigueur » ; même montant avec deux sens (180 000 € : renforcement sur 6 mois et base sur 12 mois, ex-C2 C24) |

### 6.5 Temps économisé, capacité libérée, économies réalisables

| Notion | Définition | Ce qu'on peut en dire aujourd'hui |
| --- | --- | --- |
| **Temps économisé** | Temps de référence moins temps humain total avec l'outil, contrôle, corrections et reprises compris | [IN] : aucun gain mesuré (« Gain de temps à mesurer », PIL:20 ; cible de −30 % non mesurée, STR:120-122) |
| **Capacité libérée** | Temps économisé réellement réaffecté à un autre travail utile, une fois déduits la mise en place, la maintenance et l'apprentissage | Négative au premier trimestre : la mise en place (environ 12 à 20 JP) dépasse les gains [ES] |
| **Économie réalisable** | Coût réellement évité : une sous-traitance non commandée, une heure supplémentaire non payée, une embauche différée | Pour GianLuca, seulement si une tâche aujourd'hui payée disparaît. Pour Marwin, rien dans un modèle au temps : un gain réduit les jours facturables. D'où la question du prix (ver-C2, omission 1 : la règle des gains d'automatisation a disparu le 2 nov.) |

---

## 7. « Le travail de 100 personnes à deux » : ce qui est plausible et ce qui ne l'est pas

### 7.1 L'ordre de grandeur

- 100 personnes représentent environ 1 750 JP disponibles par mois (17,5 × 100) [ES].
- Deux associés à plein temps représentent au plus 35 JP bruts et environ 28 JP facturables (section 2.3) [ES].
- Faire « le travail de 100 personnes » demanderait donc que chaque journée de Morgan ou de Mathys produise **50 à 85 fois** ce que produit une journée ordinaire, **contrôle compris** [ES].

### 7.2 Ce que montrent les pièces : produire n'est pas livrer

| Réalisation | Volume produit | Résultat constaté | Source |
| --- | --- | --- | --- |
| CRM Nièvre (agents IA, 22-30 oct.) | 500 fiches, 125 fiches d'appel, 645 fichiers | 283 numéros sur 471 à confirmer ; 1 date de vérification ; aucun appel ni vente ; données exposées | ex-C5 [FV] |
| Dépôt BOJART (30 oct. - 2 nov.) | 933 fichiers, 973 fonctions de test | Rien d'installé ni de qualifié sur le vrai poste ; aucun usage par l'artiste documenté | ex-C7 [FV] |
| OLSEN | 36 propositions, 72 brouillons d'e-mails, 503 prospects | Aucun envoi, aucune vente | NOTE:9 [DR] |
| Offre Carlone | Sept états successifs du 25 oct. au 4 nov. (V1 à V6, ex-C2 § 3.1) | Aucune réaction client documentée ; 25 contradictions relevées, dont 24 confirmées (ver-C2 n° 14) | ex-C2 § 3.1, § 4 [FV] |

Le corpus OLSEN de Morgan le dit lui-même : « les pipelines produisent déjà plus que ce que le carnet d'adresses absorbe », et la première personne à recruter « appelle, elle ne code pas » (CORPUS:710-712) [DR]. **La contrainte est en aval de la production** : vente, validation, décision du client, réception, adoption.

### 7.3 Plausible et non plausible

| Plausible, à démontrer par essai [HY] | Non plausible [HY], et pourquoi |
| --- | --- |
| Débit multiplié par 2 à 10 sur des tâches étroites, bien définies et vérifiables : recherche de sources, extraction, premiers jets, mise en forme, dédoublonnage, contrôles de cohérence | Remplacer la relation avec GianLuca, ses équipes et ses prestataires, la présence sur les lieux, la négociation |
| Suivre davantage de projets avec le même effort de pilotage, grâce au registre, aux résumés et aux alertes | Mener 8 propositions de front à deux (section 2.6), ou couvrir 24 h sur 24 et 30 jours sur 30 (ACC:105) |
| 10 à 30 % de capacité libérée la première année sur les processus pilotés, soit environ 1 à 4 JP par mois dans le scénario central | Des agents autonomes qui envoient, achètent, publient ou modifient sans approbation : contraire aux recommandations de l'ANSSI et du CERT-FR (rj-R4 (f)) |
| Préparer des dossiers de décision plus complets et mieux sourcés | Décider à la place de GianLuca, ou assumer une responsabilité d'exploitant, de comptable ou d'avocat |
| Une qualité plus régulière grâce aux contrôles déterministes | Supprimer le contrôle humain : sa charge fait partie du coût (15 % de la capacité facturable, section 2.4) |

### 7.4 Traduction mesurable : indicateurs à suivre

L'ambition se traduit en **résultats acceptés par journée-personne**, **portefeuille couvert** et **qualité**, pas en nombre d'agents ou de documents. Les cibles sont des hypothèses à fixer avec GianLuca après la mesure de référence [HY].

| Indicateur | Définition | Point de départ | Cible à 90 j | À 6 mois | À 12 mois |
| --- | --- | --- | --- | --- | --- |
| Résultats acceptés par JP | Livrables acceptés au premier ou au second passage ÷ JP consommées, par type de livrable | À mesurer au mois 1 [IN] | Mesure stable | +20 % sur les processus pilotés | +30 à +50 % |
| Temps humain total par résultat accepté | Préparation, exécution, contrôle, corrections et reprises | Mesure de référence (section 6) | −20 % sur P1 | −30 % sur P1 et P3 | −30 à −50 % sur 4 processus |
| Coût complet par résultat accepté | Temps × coût interne + outils + API + maintenance | [IN] | Calculé | Stable ou en baisse | En baisse |
| Taux de corrections | Livrables refusés au premier passage | [IN] | < 25 % | < 20 % | < 15 % |
| Délai de décision | De la demande de décision à la décision consignée | [IN] | Mesuré | −25 % | −40 % |
| Décisions préparées à temps | Part des décisions présentées avec un dossier complet avant la réunion | [IN] | ≥ 70 % | ≥ 85 % | ≥ 90 % |
| Couverture du portefeuille | Projets avec registre à jour ÷ projets confiés | 0 | 100 % des projets actifs | Idem | Idem, avec plus de projets suivis à charge égale |
| Incidents | Critiques et mineurs par mois | Une violation de données probable (rj-R4) | 0 critique | 0 critique | 0 critique |
| Occupation des associés | (Facturé + non facturé) ÷ disponible | [IN] | ≤ 85 % | ≤ 85 % | ≤ 85 % |
| Équivalent temps humain évité | Heures qu'aurait demandées la méthode de référence ÷ heures réellement passées, par processus | 1,0 | Mesuré sur P1 | 1,3 à 1,5 sur les processus pilotés | 1,5 à 2 [HY] |
| Résultats qui dépendent de GianLuca | Rendez-vous, ventes, décisions prises | 0 constaté | Suivis à part | Suivis à part | Suivis à part |

Ce tableau dit honnêtement l'ambition : sur douze mois, un facteur de **1,5 à 2** sur les processus pilotés est un objectif exigeant [HY]. Un facteur de 50 n'est appuyé par aucune pièce. Le dernier indicateur sépare ce que Marwin contrôle (qualité, délais) de ce qui dépend de GianLuca et des autres (ventes, décisions), comme le demande la section 10 de la demande.

---

## 8. Sécurité des agents IA et continuité

### 8.1 Constats sur l'existant

| Constat | Risque | Source |
| --- | --- | --- |
| Dépôt public contenant des données de prospects | Violation de données ; délai de 72 h | rj-R4 (c) ; ver-R4 n° 7 [HY fort / ES] |
| CRM en service : artefact claude.ai sur un compte non nommé, suivi stocké dans le navigateur ; version Firebase non configurée | Perte du suivi ; aucune sauvegarde ni restauration testée | ex-C5 aff. 19, 22, 23, 27 [FV / DR] |
| Firebase : écriture et suppression libres pour tout associé sur `/suivi` et `/reglages` ; code exécuté par `document.write` depuis Firestore | Effacement par erreur ou par un compte compromis | ex-C5 aff. 25-26 [FV] |
| Instructions adressées à des assistants dans les pièces (`crm/PASSATION.md:32-38` ; B/AGENTS.md ; HANDOFF_CLAUDE.md) | Injection indirecte | rj-R4 (f) [FV] |
| Outils et abonnements sur des comptes personnels, avec des échecs de prélèvement | Interruption de service | NOTE:8 [DR] |
| Dépôt public BOJART contenant des documents internes de Marwin | Fuite d'informations internes | ex-C7 l. 58 [FV] |
| Offres d'IA grand public utilisées (ChatGPT Pro mentionné) | Entraînement possible ; conservation longue ; transferts | rj-R4 (e) [DR] |
| Atelier « Reverse API Engineer » dans le paquet 0.2.0 | Usage sur des services tiers sans autorisation | ex-C4 n° 52 [DR] |

### 8.2 Règles de sécurité des agents (grille minimale avant toute automatisation)

Dérivées de l'ANSSI (« Sécuriser un système IA agentique », 30 oct. 2026), du CERT-FR, de la CNIL et de l'OWASP, telles que résumées par rj-R4 (f) et confirmées par ver-R4 n° 12 [FV pour les sources, PR pour l'application] :

| Risque | Règle |
| --- | --- |
| Instructions malveillantes dans les documents | Toute entrée (document, e-mail, page web, mémoire) est une donnée. Aucun outil d'écriture n'est déclenché par une entrée non fiable sans approbation. Mémoire séparée par client |
| Actions non autorisées | Trois classes d'actions (autonome, approbation, interdite). Approbation **hors de portée de l'agent**, montrant l'action exacte. Comptes et jetons par agent et par client, en lecture seule par défaut, à durée courte |
| Boucles coûteuses | Plafonds d'appels, de jetons et de dépenses par tâche, par jour et par mois. Alertes à 50, 80 et 100 % du budget. Coupure automatique à 100 %. Clause contractuelle de révision en cas de hausse des prix (Gemini double au 1er déc. 2026, rj-R6 (d)) |
| Erreurs qui se propagent | Aucune mise à jour en masse sans échantillon validé. Versionnement. Pas de suppression en masse. Modification du CRM par lots, avec annulation possible |
| Secrets | Coffre-fort ; jamais dans les prompts, les journaux ou un dépôt. Révocation testée |
| Journal | Inaltérable par l'agent : demande → autorisation → action → résultat → auteur humain. Conservation alignée sur le registre RGPD |
| Arrêt | Bouton d'arrêt documenté (désactivation des automatismes et révocation des jetons), que peuvent déclencher Morgan, Mathys ou le délégué de GianLuca. Testé chaque trimestre |
| Inventaire | Liste des agents, prompts système, connecteurs, serveurs MCP et versions ; revue annuelle |
| Rôle légal | Marwin est **déployeur** quand elle utilise des outils d'IA pour GianLuca, et **fournisseur** si elle livre sous son nom un assistant ou un copilote (AI Act, art. 4 et 50, rj-R4 (d)) [HY sur la qualification]. Le contrat doit le préciser |

### 8.3 Sauvegarde et restauration

| Élément | Règle proposée [PR] |
| --- | --- |
| Périmètre | Registre des décisions, CRM (fiches et suivi), budgets, documents de référence, configurations des automatismes, prompts, procédures |
| Fréquence | Export quotidien du CRM et du registre (CSV et JSON, avec la description des champs) ; sauvegarde complète hebdomadaire |
| Règle 3-2-1 | Trois copies, sur deux supports, dont une hors du fournisseur principal ; copies chiffrées ; **jamais dans un dépôt de code public** |
| Objectifs | Perte de données maximale de 24 h ; reprise du registre et du CRM en un jour ouvré [PR] |
| Restauration testée | Une fois par mois les trois premiers mois, puis chaque trimestre, dans un espace neuf, sans double exécution des actions après restauration (ANSSI, principe 6). Le dépôt BOJART montre que Morgan sait le faire (restauration `ok=true`, ex-C7 l. 11 [MM]) |
| Propriété | Sauvegardes du client stockées sur un espace **au nom de son entité** |

### 8.4 Reprise manuelle et continuité des personnes

- **Chaque processus automatisé ou assisté a une fiche de secours manuel** (section 5, ligne « Secours manuel »), testée au moins une fois par trimestre en « mode dégradé » [PR].
- **Indisponibilité d'un associé pendant plusieurs semaines** (test d'échec de la demande, § 12) :
  - l'autre associé doit pouvoir faire tourner seul le socle (registre, comptes rendus, CRM) grâce aux procédures testées (processus 11) ;
  - la capacité facturable tombe alors à environ 4 à 8 JP par mois [ES], et la clause de continuité prévoit un report du périmètre, sans pénalité, au-delà de 10 jours ouvrés d'absence [PR] ;
  - les validations de Morgan sont déléguées par écrit à Mathys sur un périmètre défini.
- **Indisponibilité d'un fournisseur d'IA** : second fournisseur configuré, prompts portables, données exportables ; pour les données les plus sensibles, repli européen ou local documenté (rj-R4 (e)).
- **GianLuca injoignable** : les engagements attendent ; seuls les travaux déjà autorisés continuent ; aucune dépense n'est faite (ACC:103).

### 8.5 Ce que GianLuca récupère

| Situation | Ce qu'il récupère | Délai proposé [PR] | Condition |
| --- | --- | --- | --- |
| **Fin normale de la collaboration** | Exports complets dans des formats ouverts (CRM, registre, budgets, documents) ; accès administrateur à tous les comptes à son nom ; configurations des automatismes ; prompts système ; procédures et fiches de secours ; journal ; inventaire des outils et abonnements ; code des développements propres à Carlone | 15 jours ouvrés après le préavis | Paiement des sommes dues ; développements propres **cédés** au paiement complet (OFF:209) |
| **Marwin cesse son activité** | Idem. Comme les outils et dépôts propres au client sont **sur ses comptes dès le premier jour**, rien n'est bloqué. Licence perpétuelle et non exclusive sur les composants génériques de Marwin utilisés dans ses livrables | Immédiat pour les comptes ; 15 jours pour la documentation | Clause de réversibilité ; **exercice de sortie à blanc au 6e mois** |
| **Un fournisseur disparaît ou change ses prix** | Données et configurations exportées ; procédure de bascule vers un autre outil ; mode manuel | Selon la fiche de secours | Exports mensuels testés |
| **Désaccord ou impayé** | Ses données et ses documents, toujours ; les développements non payés restent à Marwin jusqu'au paiement | Données : immédiat ; code : au paiement | Distinguer **ses données** (toujours restituables, RGPD) et **nos composants** |

**À distinguer** [PR] :
- les **données et documents de GianLuca**, qui lui appartiennent et sont toujours restituables ;
- les **développements propres à Carlone**, cédés au paiement ;
- les **outils préexistants et composants génériques** de Marwin (méthodes, modèles, briques comme la mémoire documentaire si les droits sont réglés), concédés sous licence et non cédés.

La propriété de Jarvis et du CRM doit être réglée **avant** de facturer (ex-C2 C10, C11 ; ex-C7 § 4 ; rj-R3).

---

## 9. Questions bloquantes et décisions pour les associés

1. **Avant le 5 novembre** : qui est responsable de traitement du fichier exposé, et faut-il notifier la CNIL ? (rj-R4 Q1). Aucun processus du pilote ne démarre sur données réelles avant cette décision.
2. **Disponibilités nominatives** : combien de jours par mois Morgan et Mathys donnent-ils réellement, et quels projets Morgan arrête-t-il (OLSEN, Shelby, BOJ.ART, autres) ? Sans réponse écrite, seule la formule « scénario prudent » (≈ 7 JP facturables) est défendable.
3. **Compétences de Mathys** : quelles réalisations personnelles (code, projets, expérience) peut-il montrer ? Le taux de 750 € et le partage « Mathys : technique et CRM » en dépendent (rj-R6, question 1).
4. **Validation** : Morgan accepte-t-il de déléguer par écrit la validation technique à Mathys ?
5. **Formule** : retirer le renforcement à 40 JP et l'ancre à 46 JP de toute présentation (impossibles à tenir) ; reformuler la base (« environ quatre cinquièmes du temps de chacun », pas « un mi-temps »).
6. **Pilote** : qui le finance (cadrage payé ou investissement plafonné à environ 12 à 20 JP) ?
7. **Comptes** : les outils du client seront-ils ouverts au nom de son entité dès le premier jour ?
8. **Propriété** : cession ou licence du CRM ; sort du code Jarvis ; transfert du dépôt FinanceScope.
9. **Gains d'automatisation** : comment les traiter dans le prix, puisque la règle du 29 oct. a disparu (ver-C2, omission 1) ?
10. **Mise en cohérence après le 4 novembre** : qui corrige l'offre écrite, STRATES v1.1, le vernissage et le PDF de 13 pages de la PR n° 1, et Medhi et Mathys ont-ils été informés ?

---

## Annexe : corrections des contrôleurs reprises, et limites

**Corrections retenues.**
- ver-C2 n° 2 : l'origine « à rebours » du taux de 750 € est une [HY] ; la provenance des 15 000 € reste [IN].
- ver-C2 n° 11 : l'atelier de dix imprimantes n'est que « probablement le parc de Medhi » [HY].
- ver-C2 n° 13 : les rappels ChatGPT relèvent de [DR] ; leur état actuel est [IN].
- ver-C2, omissions 1 et 2 : règle des gains d'automatisation disparue ; option laboratoire dépendante de BOJ.ART.
- ver-C3 n° 9 : l'achat de la station de calcul dépend d'une étude préalable ; il n'est pas décidé d'avance.
- ver-C4 n° 6 : les huit propositions sont identifiées dans `sources/propositions-de-collaboration.pdf` p. 1, dont trois administratives.
- ver-C4 n° 10 : Morgan porte seul 6 solutions de l'audit du 2 nov. et en partage 2.
- ver-C4 n° 12 : le lien d'Eaglemic avec Marwin est [IN].
- ver-C5 n° 9 : économie fiscale annuelle d'au plus environ 32 500 € pour Textilot.
- ver-C5 n° 11 : titulaire des comptes GitHub non précisé.
- ver-C5 n° 15 : 800 à 940 numéros selon la méthode de comptage.
- ver-C5, omission 1 : entreprises opposées gardées appelables.
- ver-C7 n° 5 : la CI n'exécute pas les suites Python de Jarvis.
- ver-C7 n° 10 : aucune licence n'est concédée sur le code de Jarvis.
- ver-C7 n° 16 : 973 fonctions de test.
- ver-C7, omission 3 : fragilité de la recherche documentaire quand le corpus grossit.
- ver-R4 n° 7 : le délai de 72 h expire le 5 nov. si la connaissance date du 2 nov.
- ver-R6 n° 6 : 1 250 € par jour est un plafond de devis divisé par 8, pas un prix de marché.
- ver-R6 n° 12 : DGX Spark de 128 Go à environ 6 200 à 8 100 € HT.
- ver-R6 : grille Ringover à relire.

**Limites.**
- Aucune donnée sur l'agenda de Mathys, son lieu de résidence, ses autres activités ou ses compétences personnelles.
- Les durées de déplacement sont inconnues.
- Les ratios de ventilation (section 2.4), les temps de mise en place (section 5) et les cibles (sections 6 et 7) sont des estimations à remplacer par des mesures dès le premier mois.
- Les pièces lues ne contiennent aucune parole directe de GianLuca Carlone : ses attentes en matière de présence, de délai de réponse et de couverture sont [IN].
- Les pages ChatGPT ne sont souvent lues qu'en extraits.
- La visibilité du dépôt FinanceScope n'a pas été revérifiée par cet audit.
