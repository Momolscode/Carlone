# Lecture C7 « jarvis » — Jarvis, dépôt BOJART et note de vision State Of The Art

Lecteur C7-jarvis, 4 novembre 2026. Dépôt public BOJART lu au commit 3436f53 (2 nov. 2026, 03:56 +0100), en clone superficiel : une seule révision visible, branche `main` seulement. Dépôt Carlone lu au commit 7b46602. Abréviations : **V** = `interne/state-of-the-art-note-de-vision.md` ; **B/** = `BOJART:`. Je n'ai rejoué aucun test, consulté aucun résultat GitHub Actions, contacté personne ni modifié aucun fichier en dehors de ce document.

## 1. Pièces lues

| Chemin | Date de la pièce | Nature et auteur | Original ou copie | Ce qui n'a pas pu être lu |
|---|---|---|---|---|
| V (`interne/state-of-the-art-note-de-vision.md`) | 2 nov. 2026 (V:3). Versée au dépôt le 4 nov. (commit fa5998a) | Note de vision signée « @Olsen Morgan ». Rédaction très probablement assistée par IA [HY]. Les lignes 130 à 134 portent des annotations manuelles (fautes de frappe, « tout comme moi ») [HY] | Export Markdown de l'artefact claude.ai « State Of The Art — note de vision », mis à jour le 2 nov. selon la note du 4 nov., partie B : **copie** | Deux contenus intégrés illisibles (V:54 « 3 pôles, 4 activités » ; V:96 « Feuille de route · 5 étapes, 4 décisions »). Sources citées inaccessibles ici : PDF STRATES privé, branches non fusionnées, conversation ChatGPT |
| B/README.md | Non daté (état du 1–2 nov.) | Point d'entrée du dépôt ; rédigé par des sessions d'assistant pour le compte Momolscode [HY, voir l. 36 du tableau 2] | Original | Liens hors périmètre non suivis |
| B/PRODUCTION.md | 1 nov. 2026 (l. 5) | Plan de reprise de la production vidéo | Original | — |
| B/SECURITY.md | Non daté | Politique de confidentialité du dépôt public | Original | — |
| B/AGENTS.md | Non daté | Consignes adressées aux assistants | Original | — |
| B/context/CURRENT.md | 2 nov. 2026 (l. 1) | État courant consolidé | Original | — |
| B/context/SESSION_HANDOFF.md | 1–2 nov. 2026 | Journal de passation entre sessions (244 lignes) | Original | — |
| B/creative/CURRENT.md | Non daté (≈ 1 nov.) | Direction créative « Le dernier geste » | Original | REVUE_R03.json non lu |
| B/jarvis/README.md | M07 (1 nov.) + sections du 31 oct. | Présentation de Jarvis M07 | Original | — |
| B/jarvis/context/START_HERE.md | Actualisé le 2 nov. (l. 3) ; corps des 30–31 oct. | Reprise en cinq minutes | Original (contenu en partie historique) | — |
| B/jarvis/context/PERIMETRE_ET_FEUILLE_DE_ROUTE.md | Non daté | Périmètre et priorités | Original | — |
| B/jarvis/context/CONTRADICTIONS_RESOLUES.md | Non daté | Tableau des contradictions | Original | — |
| B/jarvis/context/HANDOFF_CLAUDE.md | Non daté | Mission adressée à un assistant | Original | — |
| B/jarvis/docs/m07/RELEASE_M07.md | 1 nov. 2026 | Note de version M07 | Original | `docs/evidence/m07-2026-11-01/TESTS_SUMMARY.json` non lu |
| B/jarvis/docs/m07/RECHERCHE_2026-11-01.md | 1 nov. 2026 (l. 3) | Recherche rédigée par un assistant (« mon modèle », l. 64) | Original | Sources web citées non rouvertes |
| B/docs/audits/jarvis-installation-2026-11-01/RAPPORT.md | 1 nov. 2026 (l. 2) | Évaluation datée de l'installation | Original | PREUVES.json, SOURCES.json et DELTA_A_REEXAMINER.json non lus |
| B/docs/AUDIT_CONTINU_2026-11-01.md | 1 nov. 2026 | Audit de continuité (création et CI) | Original | — |
| B/docs/evidence/ : README de handoff-v5-2026-11-02, simulations-2026-11-02 et workflows-2026-11-02, plus les lignes de bilan des 10 journaux `.log` | 1–2 nov. 2026 | Preuves de tests et de mesures | Originaux | Les JSON bruts (run-*.json, reception.json, manifestes) n'ont pas été lus en entier |
| B/tests/, tests_agent/, tests_ops/, tests_workflows/, jarvis/tests/, jarvis/apps/jarvis/tests(_m03)/, jarvis/knowledge/metier/tests/ | — | Structure seulement : liste des fichiers et comptage des fonctions de test | Originaux | Contenu non lu, tests non rejoués |
| B/.github/workflows/ (7 fichiers) | — | Déclencheurs et commandes seulement | Originaux | Résultats des exécutions non consultés (aucune requête extérieure) |
| Compléments consultés pour vérification | 1–2 nov. 2026 | B/docs/memory/POSTE_RTX4060TI.md ; B/docs/preinstallation/DECISIONS_UTILISATEUR.txt ; B/docs/research/strates-robotique-2026-11-02/README.md et verification-calculs.json ; B/archive/2026-11-01/README.md ; B/INSTALLER_DEMAIN.md (l. 1–15) ; B/jarvis/LICENSE_SCOPE.md ; B/jarvis/apps/jarvis/AGENTS.md (l. 1–12) ; B/ops/orchestration.json (tâche strates-g0) ; B/data/catalog/recovery-2026-11-01/sources.json (structure) ; B/sites/atelier/dist/assets/*.json (recherche ciblée) ; quatre PDF (recherche de noms seulement : deux sous `docs/historical/`, deux reconstitués en mémoire depuis `archive/2026-11-01/chunks/`, sans écriture sur disque) | Originaux | — |
| Dépôt Carlone, lignes contenant « Jarvis » | 2–4 nov. 2026 | interne/offre-marwin-tech-remuneration-et-collaboration.md ; sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md ; sources/chatgpt-pages/2026-11-04-complement/marwin-structure-et-offres.md ; interne/complement-chatgpt-2026-11-04.md ; interne/offres-de-carlone-catalogue-crm.md ; pour-carlone/vernissage-strates-idees.md | Copies ou exports | Lecture limitée aux lignes citées |
| Non lus | — | Branches M08, « bras peintre » et « Veille » (non fusionnées) ; trois branches d'archive (3 340 contenus) ; historique Git du dépôt BOJART ; PDF « STRATES : verdict de l'audit » ; proposition STRATES v1.1 ; dossier investisseur ; budget ; conversation « Bras robotique précis » | — | Inaccessibles d'ici ou hors clone |

## 2. Affirmations déterminantes

| N° | Affirmation | Code | Source | Remarque |
|---|---|---|---|---|
| 1 | Jarvis M07 n'est ni installé ni qualifié sur la tour : « Lancement physique non qualifié ». | [FV] | B/jarvis/README.md:14 ; B/context/CURRENT.md:84 ; B/jarvis/docs/m07/RELEASE_M07.md:23 | État au 2 nov. Aucune pièce postérieure ne signale d'installation. |
| 2 | Le socle permet une « installation de validation ». Le Jarvis complet (voix continue, création, imprimantes, publication autonome) n'est pas démontré. | [FV] | B/docs/audits/jarvis-installation-2026-11-01/RAPPORT.md:5 | Le rapport refuse de calculer un pourcentage de préparation (l. 7). |
| 3 | Le lancement évalué le 1 nov. a utilisé le repli local, pas LangGraph : `langgraph=missing_dependency`, `production_ready=false`, `physical_commands=false`. | [MM] | RAPPORT.md:14 | Résultat transcrit ; journaux bruts non joints (l. 29). |
| 4 | Base M07 : 578 tests Python et 7 tests de signal réussis. | [MM] | B/context/CURRENT.md:26 ; B/docs/evidence/m07-baseline-tests.log:8, 292, 299, 342, 369 | Total cohérent avec le journal (274 + 242 + 40 + 22 = 578, plus 7). Exécution dans l'environnement de l'assistant, pas sur la tour. Non rejoué. |
| 5 | Dans un conteneur propre (arbre V5), `jarvis/tests` (280 tests) donne 1 échec et 2 erreurs, et `jarvis/apps/jarvis/tests` (49 tests) 1 échec et 10 erreurs, faute de médias privés, de cadquery, de playwright et de pytest. Les autres suites passent. | [MM] | B/docs/evidence/handoff-v5-2026-11-02/README.md:19-21 | Le cœur M06/M07 ne passe pas intégralement sans les dépendances et les médias privés. |
| 6 | La CI exécute `tests/`, `tests_agent/`, `tests_ops/`, `tests_workflows/`, trois tests Node de `jarvis/tests` et des simulations. Elle n'exécute pas les suites Python `jarvis/tests` (dont `test_jarvis_m07.py`) ni `jarvis/apps/jarvis/tests`. | [FV] | B/.github/workflows/continuity.yml:19-27 ; agent-memory.yml:10-21 ; audit.yml:23 ; workflow-simulations.yml:33-41 | Trois workflows tournent aussi sous Windows. |
| 7 | La note de vision qualifie Jarvis M07 de « Tests et CI verts ». | [DR] | V:38 | Formule trop large au vu des lignes 5 et 6. Je n'ai pas vérifié le statut des exécutions CI. |
| 8 | Voix : capture et arrêt sur pause testés avec un signal synthétique et des doubles ASR et Jev. Aucun test sur micro physique ; les poids de faster-whisper ne sont pas configurés. | [FV] | B/jarvis/docs/m07/RECHERCHE_2026-11-01.md:52-58 ; RELEASE_M07.md:15-17 | — |
| 9 | Les « trois vues » sont des onglets de navigateur, pas trois moniteurs appairés. | [FV] | B/jarvis/README.md:57 ; B/jarvis/context/CONTRADICTIONS_RESOLUES.md:7 | La note de vision (V:38) parle de « trois vues » sans cette réserve. |
| 10 | Les connecteurs d'imprimantes, la découpe, la publication et les statistiques restent à raccorder. | [FV] | B/context/CURRENT.md:28 ; RECHERCHE:61 | Aucune impression pilotée par Jarvis. |
| 11 | Mémoire documentaire : installation minimale, six routes HTTP 200, restauration dans un dossier neuf réussie (`ok=true`). | [MM] | RAPPORT.md:10-12 | Environnement Linux de l'assistant. |
| 12 | Banc mémoire : 1 260 recherches (14 questions répétées 90 fois), référence dans les cinq premiers résultats à chaque fois, médiane 0,706 ms. | [MM] | B/docs/evidence/simulations-2026-11-02/README.md:11, 18 | Quatorze questions seulement, hôte Linux sans GPU, aucun LLM. |
| 13 | La référence attendue reste dans le contexte transmis au modèle dans 71,4 % des cas à 8 000 octets et 92,9 % à 13 000 octets. | [MM] | simulations-2026-11-02/README.md:19, 28 | C'est le point faible d'un copilote documentaire : trouver une source ne suffit pas si elle n'est pas transmise. |
| 14 | Simulation de commandes : 810 essais, p95 de 32,06 ms jusqu'au reçu, avec des reçus injectés par le script et sans navigateur. | [MM] | B/docs/evidence/workflows-2026-11-02/README.md:18-23 | Ce n'est « pas un taux de compréhension vocale » (l. 23). |
| 15 | Sous Windows avec LangGraph : p95 de 740,9 ms et maximum de 17 964,7 ms, sept essais au-dessus d'une seconde. Cause non isolée. | [MM] | workflows-2026-11-02/README.md:37-40 | La tour cible tourne sous Windows. |
| 16 | Planification fictive du parc : gain de 15,25 % (231 min) sur 8 machines et 24 boîtes fictives ; « non généralisable ». | [ES] | workflows-2026-11-02/README.md:56-60 | Durées supposées. |
| 17 | Aucun modèle réel n'a été essayé sur le poste ; le profil « speed » est seulement préparé. | [FV] | B/context/CURRENT.md:84 ; V:39 | — |
| 18 | Le dépôt écrit lui-même qu'une réussite technique ne vaut ni validation artistique ni mesure d'audience, et qu'aucune performance commerciale n'est établie. | [FV] | B/README.md:38 ; B/PRODUCTION.md:39-40 ; B/creative/CURRENT.md:14 | Aucune vente, aucun chiffre d'audience, aucun usage quotidien mesuré. |
| 19 | La tour fonctionne sous Windows 11 Pro Insider Preview 25H2, avec un Ryzen 5 5600G, 16 Go de RAM (passage à 32 Go décidé, non constaté), une RTX 4060 Ti 8 Go et 932 Go affichés. | [DR] | B/context/CURRENT.md:62 ; B/docs/preinstallation/DECISIONS_UTILISATEUR.txt:6-8 | Lu sur une photo, ce n'est pas un diagnostic (B/docs/memory/POSTE_RTX4060TI.md:3). |
| 20 | Profil de modèle retenu : Qwen3.5 4B Q4_K_M (≈ 3,3 Go) et Qwen3 Embedding 0.6B via Ollama, avec un contexte de 16 384 tokens et 512 tokens de réponse. | [PR] | POSTE_RTX4060TI.md:18-20 | « pas une qualification de performance ». |
| 21 | Les 8 Go de mémoire graphique ne permettent pas de présumer que l'image, la vidéo, la voix et le LLM fonctionneront ensemble. | [HY] | POSTE_RTX4060TI.md:45 | Réserve formulée par le document lui-même. |
| 22 | Jev est un service hébergé par TypeSafe, appelé par API et facultatif. Son meilleur terrain est l'anglais. | [FV] | RECHERCHE:28-30 ; B/README.md:36 | Dépendance distante, avec une clé et un coût, contraire au « local d'abord ». |
| 23 | Les vidéos passent par un fournisseur payant (Higgsfield, Seedance 2.5). Des refus « ip_detected » et « nsfw » ont été enregistrés. | [FV] | B/docs/AUDIT_CONTINU_2026-11-01.md:25-31 ; B/creative/CURRENT.md:9 | Coût total des crédits inconnu [IN]. |
| 24 | Le parc compte « 7–8 », puis « une dizaine » de machines FDM et résine, sans inventaire ni modèles connus. | [DR] | V:36 ; B/context/CURRENT.md:62 ; B/jarvis/context/PERIMETRE_ET_FEUILLE_DE_ROUTE.md:7 | — |
| 25 | Le site public de l'atelier contient des mots-clés de machines (#elegoosaturn, #elegoomars, #ender5pro, #ender5plus) et de lieu (#montmorency). | [FV] | B/sites/atelier/dist/assets/archive-index.json:170 | C'est un indice partiel d'inventaire. Les documents disent pourtant « modèles inconnus ». |
| 26 | Le budget de la tour est de 3 000 à 5 000 € dans les documents historiques ; un PDF de plan annonce un « PC dédié » à 8 000 €. | [DR] | B/jarvis/context/START_HERE.md:10 ; B/docs/historical/BOJ_ART_Atelier_3D_Plan_de_mise_en_oeuvre.pdf p. 2 et p. 7 | Coût réel de la tour et payeur inconnus [IN]. |
| 27 | Le poste est appelé « poste RTX 4060 Ti de BOJ.ART ». | [FV] | POSTE_RTX4060TI.md:1 | Propriétaire du matériel non établi [IN]. |
| 28 | Le dépôt BOJART est public, sous le compte Momolscode. Son seul commit visible est attribué à Momolscode (adresse Gmail de Morgan Olsen). | [FV] | B/SECURITY.md:3 ; métadonnées du commit 3436f53 | — |
| 29 | Le dépôt n'a pas de fichier de licence à la racine, et `jarvis/LICENSE_SCOPE.md` n'impose « aucune licence globale ». | [FV] | B/jarvis/LICENSE_SCOPE.md:2 | Les droits de réutilisation dépendent donc d'un accord écrit, inexistant à ce jour [IN]. |
| 30 | Jarvis BOJ.ART doit rester distinct d'UNUM, de M-Tek et des « projets personnels Marwin ». | [FV] | B/AGENTS.md:6 ; B/jarvis/README.md:45 | Le dépôt sépare lui-même Jarvis de Marwin. |
| 31 | Medhi et Mathys ne sont nommés nulle part dans le dépôt BOJART. L'utilisateur y est « l'artiste et son associé » ou « le propriétaire ». | [FV] | Recherche du 4 nov. (0 occurrence) ; PERIMETRE:4 ; B/jarvis/apps/jarvis/AGENTS.md:5 | Aucune trace d'une contribution de Mathys. |
| 32 | « Le code de Jarvis et du CRM : Morgan et Mathys, dans une structure à préciser. » | [PR] | V:84 | Contredit par les lignes 33 et 34. |
| 33 | Medhi « lui fait confiance pour son Jarvis ». | [DR] | V:23 | « Son Jarvis » désigne celui de Medhi. |
| 34 | Dans l'offre écrite, Medhi (BOJ.ART) apporte « atelier, parc d'impression et Jarvis ». | [PR] | interne/offre-marwin-tech-remuneration-et-collaboration.md:90 | L'offre attribue donc Jarvis au pôle de Medhi. |
| 35 | « BOJ.ART, Jarvis et UNUM conservent leurs propriétaires […] leur présence dans le contexte ne constitue pas un apport automatique à Marwin Tech. » | [PR] | sources/chatgpt-pages/2026-11-04-complement/marwin-structure-et-offres.md:22 | — |
| 36 | Les textes du dépôt sont écrits par des sessions d'assistant IA à la demande de l'utilisateur (« Demande : … », « mon modèle », « Le destinataire demandé est Claude Opus 5.5 »). | [FV] | B/context/SESSION_HANDOFF.md:5, 188 ; RECHERCHE:64 ; DECISIONS_UTILISATEUR.txt:2 | La part du code écrite par Morgan lui-même est inconnue [IN]. |
| 37 | Le PDF d'audit STRATES porte l'en-tête « BOJ.ART / MARWIN TECH ». Le dépôt public n'en garde que la référence et l'empreinte. | [FV] | B/docs/research/strates-robotique-2026-11-02/README.md:9 | Marwin Tech est donc associé publiquement à BOJ.ART. |
| 38 | State Of The Art réunit l'art (Medhi), la tech (Morgan et Mathys) et les lieux (Carlone). Première étape : STRATES Phase 1. | [PR] | V:7, 17 | Vision antérieure au retrait du 4 nov. |
| 39 | GianLuca Carlone serait un marchand d'art venu de l'avenue Montaigne et le plus gros client de Morgan et Mathys. Il aurait racheté six bâtiments, dont une future galerie (2027), et proposerait des bureaux, une rémunération, peut-être un investissement. Il aurait envisagé un cabaret et racheté l'ancienne affaire de Medhi. | [DR] | V:9, 24 ; source : « messages de Morgan du 2 novembre » (V:28) | Rien n'est vérifié. Un patrimoine ne prouve pas une trésorerie disponible. |
| 40 | « Le logiciel est solide en démonstration et en simulation, mais rien n'est encore qualifié sur le vrai matériel. » | [DR] | V:32 | La seconde moitié est confirmée par le dépôt. « Solide » est nuancé par les lignes 5, 13 et 15. |
| 41 | Le programme R&D de 323 875 € HT est « chiffré dans le budget BOJART » ; l'audit ne le soutient pas encore. | [DR] | V:61 ; montant absent du dépôt public (verification-calculs.json, « amounts withheld ») | Budget non lu ici. |
| 42 | Bras recommandé : UFACTORY xArm 6 (≈ 9 500 USD hors outillage). Option économique : AgileX PiPER (≈ 2 400 €). Prix « indicatifs ». | [PR] / [ES] | V:66 | Hors capteur, sécurité et intégration ; aucun devis. |
| 43 | La simulation produit un rendu en 13 236 touches ; la durée de bras estimée est de 6 à 9 h. | [ES] / [HY] | V:68 | « une hypothèse et non une mesure ». |
| 44 | Les pièces faites à la machine ne sont « très probablement pas des œuvres originales au sens fiscal ». | [HY] | V:118 | À faire valider par un professionnel avant tout argument commercial. |
| 45 | « Jarvis bloque déjà les personnages protégés (cas Végéta). » | [DR] | V:109 | Le dépôt montre autre chose : la demande Végéta reste « CLARIFY » ou non raccordée (SESSION_HANDOFF:203 ; workflows README:25), et le refus « ip_detected » vient du fournisseur (AUDIT_CONTINU:27). Aucun filtre de droits n'est démontré. |
| 46 | Le site public de l'atelier présente des pièces représentant des personnages protégés (Vegeta, Baki, Sukuna). | [FV] | B/sites/atelier/dist/assets/atelier-motion-sources.json:32, 69, 99 | Risque de droits pour toute vente ou exposition en galerie. |
| 47 | « Les informations de Carlone restent privées et hors du dépôt public BOJART. » | [PR] | V:90, 114 | Vérifié au 4 nov. (ligne 57). |
| 48 | Le dépôt du CRM de Carlone est public et expose des données personnelles de prospects : « le passer en privé sans attendre ». | [DR] | V:120 (2 nov.) | Dernier état documenté : public le 4 nov. à 16 h 19 (note du 4 nov., partie C). |
| 49 | La case « Structure qui porte l'activité : Marwin Tech, OLSEN ou une autre » est cochée, sans réponse écrite. | [FV] | V:130 | Marwin Tech n'est pas immatriculée (BRIEF-AGENTS.md:3). |
| 50 | Annotation : « Part maximale des revenus qui peut venir de Carlone ( 10 millions ». | [FV] | V:134 | Sens inconnu [IN] : plafond, espoir de chiffre d'affaires ou investissement ? |
| 51 | Fiche G0 (motif, format) et enveloppe de la Phase 1 non tranchées ; la tâche `strates-g0` est « blocked ». | [FV] | V:126-128 ; B/ops/orchestration.json:443 | — |
| 52 | Le 4 nov., Morgan a écrit « Va juste falloir enlever Medhi/boj art de l'offre ». Le diaporama est passé de 13 à 11 diapositives ; l'offre écrite, STRATES v1.1 et le diaporama du vernissage n'ont pas été modifiés. | [DR] | note-point-4-novembre-et-activites.md:25 | Décision orale, non formalisée avec Mathys ni avec Medhi. |
| 53 | L'offre écrite garde la ligne « Créer des œuvres avec la robotique et l'IA », la Phase 1 STRATES (≈ 10 000 € HT, dont 6 journées Marwin à 4 500 € HT) et la ligne « Medhi (BOJ.ART) … Jarvis ». | [FV] | interne/offre-marwin-tech-remuneration-et-collaboration.md:67-90 | Ce document est incohérent avec la décision du 4 nov. |
| 54 | Le « copilote Jarvis » destiné à GianLuca est un démonstrateur à construire : 4 jours (28 h) au premier mois, « sur des données fictives ou un périmètre autorisé ». | [PR] | offre :60 ; sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:75 | Ce n'est pas le Jarvis de l'atelier. |
| 55 | « L'atelier Jarvis, UNUM et les recherches artistiques ne sont pas automatiquement inclus dans un abonnement commercial Carlone. » | [PR] | interne/complement-chatgpt-2026-11-04.md:17 | — |
| 56 | Le vernissage « Strates » s'appuie sur le parc de Medhi, Jarvis, le CRM, les films et le bras peintre. | [PR] | pour-carlone/vernissage-strates-idees.md:13 | Devenu fragile depuis le 4 nov. |
| 57 | Aucune occurrence de Carlone, GianLuca, John-Lucas, Montaigne, Quali Contact, FinanceScope, CRM-Carlone, Nièvre, Mathys, Couet, Medhi, cabaret, vernissage ou Éclosion dans les 933 fichiers texte suivis, ni dans les quatre PDF. | [FV] | Recherche du 4 nov. sur B/ (git grep, puis extraction du texte des PDF) | Limites : historique Git, autres branches et vidéos non examinés. |
| 58 | Le dépôt public contient, en fragments binaires, le PDF « MARWIN_Audit_Global_2026-10-25 » (9 pages), un audit des films personnels de Morgan (« MORGAN / MARWIN STUDIO »). | [FV] | B/archive/2026-11-01/README.md:11 ; texte p. 1 du PDF reconstitué | Pas de donnée Carlone, mais des documents internes de Marwin sont publics. |
| 59 | SECURITY.md recommande un stockage privé, ou le passage du dépôt en privé, avant d'importer les archives. | [PR] | B/SECURITY.md:11 | Une sélection d'archives est déjà publiée (B/archive/2026-11-01/). |
| 60 | Les « 219 sources » de la récupération BOJART sont des fichiers : 168 de bibliothèque, 32 médias de fournisseur, 14 preuves, 4 exports de sites, 1 export GitHub. | [FV] | B/data/catalog/recovery-2026-11-01/sources.json | Simple coïncidence avec les « 169 conversations sur 219 » de l'inventaire Carlone (DEMANDE.md:11). |
| 61 | Volume du dépôt : 933 fichiers suivis, ≈ 19 700 lignes Python, 932 fonctions de test Python, 7 workflows CI. | [FV] | Comptage du 4 nov. sur B/ | Le front-end des sites compte ≈ 104 000 lignes JS/TS, probablement en partie générées [HY]. |
| 62 | Rythme : M04 le 31 oct., M07 le 1 nov., publication V5 et session robotique le 2 nov. | [FV] | START_HERE.md:46 ; RELEASE_M07.md:3 ; SESSION_HANDOFF.md:222 | Effort intense sur BOJ.ART juste avant la préparation de l'offre à GianLuca. |
| 63 | Le dépôt applique une discipline de preuve : empreintes SHA-256, restaurations vérifiées, séparation entre mesuré, simulé, déclaré et proposé. | [FV] | B/context/CURRENT.md:70 ; RAPPORT.md:27 ; B/data/knowledge/claims.jsonl (champ `status`) | C'est la compétence la plus directement transférable à GianLuca. |

## 3. Chiffres, engagements et dates

| Élément | Valeur | Code | Source |
|---|---|---|---|
| Date de la note de vision | 2 nov. 2026 ; versée au dépôt le 4 nov. | [FV] | V:3 ; commit fa5998a |
| Dernier commit BOJART | 3436f53, 2 nov. 2026 à 03:56 +0100 | [FV] | Métadonnées git |
| Chronologie de Jarvis | Recherche du 30 oct. ; M04 et SEO le 31 oct. ; M07 et audit d'installation le 1 nov. ; V5, profil 4060 Ti et STRATES le 2 nov. | [FV] | START_HERE.md:39, 43, 46 ; RELEASE_M07.md ; SESSION_HANDOFF.md:168, 222 |
| Installation sur la tour | « prévue le 2 novembre » ; non constatée | [DR] / [IN] | SESSION_HANDOFF.md:38 ; CURRENT.md:84 |
| Tests M07 | 578 Python + 7 de signal | [MM] | CURRENT.md:26 ; m07-baseline-tests.log |
| Tests de l'arbre V5 | 102 / 234 / 98 / 20 / Node 41 / métier 41 réussis ; `jarvis/tests` : 1 échec et 2 erreurs sur 280 ; `apps/jarvis/tests` : 1 échec et 10 erreurs sur 49 | [MM] | handoff-v5 README:19-21 |
| Tests sélectionnés au 1 nov. | 172 tests Python et 10 cas documentaires | [MM] | RAPPORT.md:19-27 |
| Intentions du routeur | 10 | [FV] | RAPPORT.md:35 |
| Fiches métier | 54 | [DR] | jarvis/README.md:26 |
| Mémoire : recherche | 1 260 essais ; médiane 0,706 ms ; p95 1,053 ms | [MM] | simulations README:11 |
| Mémoire : contexte | 71,4 % (8 000 octets) ; 92,9 % (13 000 octets) | [MM] | simulations README:19 |
| Charge mixte | 960 opérations, 0 erreur ; p95 attente comprise 331,955 ms | [MM] | simulations README:15-16, 20 |
| Commandes | 810 essais ; p95 19,95 ms (persistance) et 32,06 ms (reçu) | [MM] | workflows README:20-21 |
| Windows et LangGraph | p95 740,895 ms ; maximum 17 964,718 ms | [MM] | workflows README:38 |
| Latences M06 historiques | 66–98 ms au calme ; 115–997 ms sous calcul CAO ; pic de 1,4 s ; hors STT et Jev | [MM] | RECHERCHE:46 |
| Arrêt sur pause | Pause ≈ 1,1 s ; plafond de 15 s | [FV] | RECHERCHE:42 |
| Planification fictive | 25 h 15 contre 21 h 24 ; gain de 231 min (15,25 %) | [ES] | workflows README:56-60 |
| Matériel | Ryzen 5 5600G ; 16 Go (32 Go prévus) ; RTX 4060 Ti 8 Go ; 932 Go affichés ; Windows 11 Insider 25H2 | [DR] | CURRENT.md:62 |
| Modèle local | Qwen3.5 4B Q4_K_M (≈ 3,3 Go) ; Embedding 0.6B ; contexte 16 384 ; sortie 512 ; maintien en mémoire 300 s | [PR] | POSTE_RTX4060TI.md:18-20 |
| Budget de la tour | 3 000–5 000 € (historique) ; 8 000 € (PDF) | [DR] | START_HERE.md:10 ; PDF de plan p. 2 |
| Parc | 7–8, puis « une dizaine » de machines | [DR] | V:36 |
| Récupération | 3 340 contenus, 6 445 emplacements, 219 sources (fichiers) ; 3 402 originaux après complément | [FV] (déclaré vérifié) | CURRENT.md:70 ; README.md:52 |
| Catalogue | 1 060 emplacements, 1 016 contenus | [FV] | README.md:16 |
| Film R03 | 9,25 s, 222 images, 720 × 1280, 24 i/s ; −15,18 LUFS | [MM] (historique) | creative/CURRENT.md:12-13 |
| Visuels classés | 96 images, 77 vidéos, 126 visuels Jarvis | [DR] | V:48 |
| Archive TikTok | 31 publications, 29 vidéos ; « 14 017 abonnés » contesté | [DR] | V:44 ; CONTRADICTIONS:9 |
| Figurines M08 | 200 mm ; 2 min 12 s ; impression estimée à 12 h 16 + 8 h 10 | [ES] | V:40 |
| Critères STRATES | Trait de 7 mm ; 6–8 mm sur 90 % ; débordement ≤ 1 mm, incertitude comprise | [PR] | V:62 |
| Format STRATES | 90 × 65 cm ou 90 × 56 cm | [PR] | V:78 |
| Statistiques d'essai | 19/20 → ≈ 78,4 % ; 59/59 → > 95 % | [FV] (recalcul) | strates README:38 ; verification-calculs.json |
| Simulation des bras | 52–58 réussites sur 59 (± 0,1 mm) ; Lite 6 : 26 | [ES] | V:64 |
| Prix des bras | xArm 6 ≈ 9 500 USD ; PiPER ≈ 2 400 € | [ES] | V:66 |
| Programme R&D | 323 875 € HT | [DR] | V:61 |
| Phase 1 STRATES (offre) | ≈ 10 000 € HT, dont 6 journées Marwin = 4 500 € HT (soit 750 €/journée) | [PR] | offre :69, 84 |
| Copilote, premier mois | 4 jours, 28 h | [PR] | offre :60 |
| Option laboratoire | 90 jours, 18 journées de R&D | [PR] | offre :65 |
| Durée du bras | 6–9 h | [HY] | V:68 |
| Galerie | Ouverture en 2027, date non fixée | [DR] | V:9, 98 |
| Règlement machines (UE) 2023/1230 | Applicable au 20 janv. 2027 (selon l'audit STRATES) | [DR] | V:110 ; strates README:40 |
| Ancienneté de la relation Morgan–Medhi | 1 an et demi | [DR] | V:23 |
| Décisions attendues | 13, dont 4 qui conditionnent la présentation | [FV] | V:124 |
| Réception HTTP | Corps borné à 16 Kio et à 12 lecteurs | [FV] | SESSION_HANDOFF.md:212 |

## 4. Contradictions et divergences

| Sujet | Version A + source | Version B + source | Portée pour l'audit |
|---|---|---|---|
| Propriétaire de Jarvis | Code de Jarvis à « Morgan et Mathys » (V:84) ; Morgan « construit Jarvis » (V:21) | « son Jarvis », celui de Medhi (V:23) ; Medhi apporte « Jarvis » (offre :90) ; Jarvis « conserve ses propriétaires » (marwin-structure-et-offres.md:22) ; dépôt sous le compte de Morgan, sans licence (B/jarvis/LICENSE_SCOPE.md:2) | **Majeure.** Sans accord écrit, Marwin ne peut ni vendre ni réutiliser librement Jarvis chez GianLuca, surtout après le retrait de Medhi. |
| Rôle de Mathys dans Jarvis | Co-titulaire du code (V:84) | Aucune mention dans le dépôt (0 occurrence) ; « Rôle de Mathys dans BOJ.ART […] tout comme moi » encore ouvert (V:132) | La capacité technique à deux sur Jarvis n'est pas démontrée. |
| État des tests | « Tests et CI verts » (V:38) | La CI n'exécute pas les suites Python M06/M07 (continuity.yml:19-27) ; des échecs apparaissent en conteneur propre (handoff-v5 README:20-21) | Niveau de preuve surévalué dans la note destinée à présenter le projet. |
| Suites jarvis après V5 | « Après ajout des deux documents indexés, ces suites repassent » (SESSION_HANDOFF.md:238) | 1 échec et 2 erreurs, puis 1 échec et 10 erreurs, « identiques sur main » (handoff-v5 README:20-21) | Rédaction ambiguë ; à clarifier avant d'invoquer ces tests. |
| LangGraph | « intégré » depuis M06/M07 (CONTRADICTIONS:8 ; PERIMETRE:35) | Le lancement évalué a utilisé le repli local (RAPPORT:14) ; les campagnes locales aussi (workflows README:10) | Le moteur décrit n'est pas celui qui a tourné lors de l'évaluation. |
| Filtre de droits | « Jarvis bloque déjà les personnages protégés (cas Végéta) » (V:109) | Demande « CLARIFY » ou non raccordée (SESSION_HANDOFF:203) ; refus venant du fournisseur (AUDIT_CONTINU:27) ; le site public présente Vegeta, Baki et Sukuna (atelier-motion-sources.json:32, 69, 99) | Argument de conformité non démontré ; risque de droits sur les pièces existantes de BOJ.ART. |
| Modèles d'imprimantes | « modèles inconnus » (V:36 ; POSTE_RTX4060TI.md:47) | Mots-clés Elegoo Saturn et Mars, Ender 5 Pro et Plus sur le site (archive-index.json:170) | Un inventaire partiel est possible à partir de sources existantes. |
| Taille du parc | « 7–8 » (PERIMETRE:7) | « une dizaine » (V:36 ; CURRENT.md:62) | Aucun inventaire. |
| Budget de la tour | 3 000–5 000 € (START_HERE.md:10) | 8 000 € (PDF de plan p. 2, p. 7) ; configuration réelle plus modeste (CURRENT.md:62) | Payeur et coût réel inconnus. |
| Visibilité du dépôt | Dépôt « en privé » `bojart-jarvis` ; publication en Release dans un dépôt PRIVÉ (START_HERE.md:37 ; jarvis/README.md:43) | Dépôt public `Momolscode/BOJART` (AGENTS.md:5 ; SECURITY.md:3) avec des archives binaires publiées (archive/2026-11-01/README.md:9-12) | Pratique incompatible avec des données de GianLuca : dépôt privé indispensable. |
| Fonctionnement local | « Priorité au fonctionnement local » (START_HERE.md:10) | Jev hébergé (RECHERCHE:28), fournisseur vidéo payant (AUDIT_CONTINU:25-31), GitHub Actions | Coûts récurrents et dépendances externes non chiffrés. |
| Les trois vues | « trois vues (atelier, Jarvis, création) » (V:38) | Onglets, pas de moniteurs appairés (jarvis/README.md:57) | Formulation optimiste. |
| Format STRATES | 90 × 65 cm (audit ; offre :80) | 90 × 56 cm (simulation, V:78) | Non tranché (fiche G0). |
| Place de Medhi | Pôle « art » de State Of The Art, « plus que partant » (V:7, 23) | Retiré de l'offre le 4 nov. (note du 4 nov.:25), alors que l'offre écrite le garde (offre :67-90) | Documents de l'offre incohérents entre eux ; la vision est devenue caduque sans être révisée. |
| Sens de « Jarvis » | Jarvis = outil de l'atelier BOJ.ART (V:11, 85) | Jarvis = « votre » copilote de pilotage pour GianLuca (marwin-offre-accompagnement.md:17, 109) | Un même nom pour deux produits : risque de confusion sur ce qui est vendu et sur qui le possède. |
| Structure de l'activité | Case cochée (V:130) | Aucune structure nommée ; Marwin Tech non immatriculée ; le dépôt parle aussi de « Marwin Studio » (archive/2026-11-01/README.md:3) et d'« OLSEN » | Le porteur juridique de Jarvis et du copilote reste inconnu. |
| Part de revenus venant de GianLuca | « Fixer une part maximale de revenus venant de Carlone » (V:88) | « ( 10 millions » (V:134) | Annotation contradictoire avec le principe affiché ; sens à clarifier. |

## 5. Informations inconnues et questions

1. Qui détient aujourd'hui les droits sur le code de Jarvis : Morgan à titre personnel, son entreprise existante (OLSEN ?), une future Marwin Tech ou Medhi/BOJ.ART ? Existe-t-il un écrit ?
2. Medhi a-t-il payé, ou doit-il payer, le développement de Jarvis ? La « facture Jarvis pour l'atelier » (V:85) a-t-elle été émise ou chiffrée ?
3. Quelle part du code a été écrite par Morgan, par Mathys ou par des assistants IA ? Mathys a-t-il contribué au dépôt BOJART ?
4. À qui appartient la tour (RTX 4060 Ti), où se trouve-t-elle, et qui l'a payée ?
5. Jarvis a-t-il été installé et utilisé sur la tour entre le 2 et le 4 novembre ? Medhi l'utilise-t-il ? Quelles tâches réelles a-t-il accomplies ?
6. Quel est le coût cumulé des services payants utilisés pour BOJ.ART (crédits de génération vidéo, Jev, abonnements) et qui l'a payé ?
7. Sous quelle licence, et avec quel accord, des composants de BOJART (mémoire documentaire, registre d'affirmations, orchestration) peuvent-ils être réutilisés pour GianLuca ?
8. Le « copilote Jarvis » de GianLuca serait-il hébergé sur un poste local (lequel ?), sur un serveur ou dans un service cloud ? Avec quel modèle, et avec quelles garanties de confidentialité ?
9. Pourquoi Medhi et BOJ.ART ont-ils été retirés de l'offre le 4 novembre ? Est-ce un retrait définitif, un report ou une séparation des contrats ? Medhi et Mathys en sont-ils informés ?
10. State Of The Art est-il abandonné, reporté ou maintenu hors de l'offre à GianLuca ? Qui doit réviser la note de vision ?
11. Que deviennent STRATES Phase 1 (≈ 10 000 € HT), le vernissage « Strates » et l'option laboratoire, qui s'appuient sur l'atelier de Medhi ?
12. Que signifie « ( 10 millions » (V:134) ? Quelle structure a été cochée (V:130) ?
13. Qui est l'« investisseur » du « dossier investisseur v1.0 » cité par l'audit STRATES (strates README:18) ? Est-ce GianLuca ?
14. Les branches M08, « bras peintre » et « Veille » seront-elles fusionnées, et ont-elles encore une utilité sans Medhi ?
15. Que sont UNUM et M-Tek, à qui appartiennent-ils, et quel lien ont-ils avec Marwin Tech ?
16. Qui contrôle l'organisation GitHub FinanceScope qui héberge `CRM-Carlone` ? Le dépôt est-il désormais privé ?
17. Les pièces de BOJ.ART représentant des personnages protégés (Vegeta, Baki, Sukuna) ont-elles été vendues ? Une présentation dans la galerie de GianLuca est-elle envisagée ?
18. Le système Windows 11 Insider Preview est-il volontaire sur un poste destiné à la production ?
19. Quelle qualité de réponse en français obtient le modèle 4B sur de vraies questions de pilotage ? Aucune mesure n'existe.
20. Combien de journées Morgan a-t-il consacrées à Jarvis BOJ.ART entre le 30 octobre et le 2 novembre ? Ce temps a-t-il été facturé ?

## 6. Par chantier

1. **CRM et développement commercial.** Le dépôt BOJART ne contient aucun CRM. La publication et le CRM sont classés en priorité P2, « autorisés » (PERIMETRE:31). Growth ne produit que des brouillons, sans connexion sociale (jarvis/README.md:49). La note de vision rapporte un CRM de GianLuca « construit par Morgan et Mathys », « non examiné » (V:46), et un dépôt public qui expose des prospects (V:120) [DR]. Le catalogue des offres envisage qu'une commande signée dans le CRM ouvre un dossier dans Jarvis (interne/offres-de-carlone-catalogue-crm.md:111) [PR].
2. **Quali Contact.** Rien.
3. **Organisation et pilotage.** Plusieurs éléments sont transposables en méthode : le registre `ops/orchestration.json` (tâches, dépendances, blocages, critère d'acceptation : B/ops/orchestration.json:443), le registre d'affirmations à statuts (`observed`, `user_decision`, `source_reported`, `proposal` : B/data/knowledge/claims.jsonl), et le protocole de passation (objectif, sources datées, décisions, tests réellement exécutés, limites, prochaine preuve : SESSION_HANDOFF.md:18). Ces outils servent aux agents ; aucune interface n'existe pour un client non technicien. La note de vision pose des principes de pilotage : étapes courtes, décision fondée sur une preuve, temps humain et temps machine comptés à part (V:89, 94).
4. **Jarvis, mémoire et automatisations.** C'est le cœur du dépôt. Ce qui est démontré relève du logiciel en environnement d'essai (tableau 2, l. 1 à 18). Rien n'est démontré sur le vrai poste. Bilan de réutilisation :

   | Composant | Démontré | Réutilisable pour un copilote chez GianLuca ? | Conditions |
   |---|---|---|---|
   | Mémoire documentaire (`bojart_memory` : SQLite FTS5, citations avec lignes, versions, sauvegarde et restauration, serveur MCP) | Tests CI Linux et Windows ; banc de 1 260 recherches (14 questions) | Oui en principe : brique générique | Accord sur les droits ; dépôt et hébergement privés ; essai sur de vraies questions françaises ; meilleure sélection du contexte (71,4 % à 8 000 octets) |
   | Registre d'affirmations à statuts et provenance | Fichiers et validateur présents | Oui : c'est la méthode de « décisions préparées » | Interface lisible pour GianLuca à créer |
   | Registre des tâches et dépendances (`ops/orchestration.json`) | Planificateur en lecture seule, tests | Partiellement : modèle de suivi de portefeuille | Il manque l'agenda, la messagerie, la comptabilité et le CRM |
   | Garde des actions (route → garde → distribution → reçu ; confirmation explicite ; une source est une donnée, pas une instruction) | 16 scénarios de garde, 48/48 (workflows README:46) | Oui, comme principe de gouvernance des automatisations | Pour d'autres actions (courriels, CRM, dépenses), il faut de nouveaux tests |
   | Bancs de mesure et simulations | Rapports versionnés | Oui, comme méthode de preuve | — |
   | CAO CadQuery, tour à trois vues, voix et Jev, planificateur du parc, Studio et Growth (TikTok), productions vidéo, sites Atelier et Studio, STRATES | Démonstrations, sans qualification matérielle | Non : propre à l'atelier BOJ.ART | — |
   | Manques pour un copilote | — | Connecteurs messagerie, agenda, CRM et comptabilité ; multi-utilisateur ; accès nominatifs ; journal d'audit destiné au client ; hébergement maîtrisé ; chiffrement ; procédure de sortie | À construire et à chiffrer |

   Dépendances matérielles : tour Windows Insider avec une 4060 Ti 8 Go, Ollama, Python 3.12, Jev distant, poids ASR, trois écrans, micro, imprimantes (tableau 2, l. 19 à 27). Un copilote de pilotage n'a besoin ni de la tour ni du GPU [HY] ; il ne devrait pas dépendre d'un poste appartenant au pôle de Medhi.
5. **Marketing et contenus.** Pour BOJ.ART seulement : deux comptes TikTok, audiences inconnues (START_HERE.md:29) ; 31 publications archivées (V:44) ; film R03 en coupe de travail, sans master approuvé ni mesure d'audience (creative/CURRENT.md:9-16) ; six skills SEO et une route `/growth` sans publication (jarvis/README.md:49). La méthode est transposable : registre des expérimentations avec prix, statut et décision (PRODUCTION.md:37), et séparation entre « fichier généré » et « validé » (PRODUCTION.md:40).
6. **Galerie, œuvres et artistes.** La galerie de GianLuca est annoncée pour 2027, avec STRATES comme pièce phare (V:9, 52) [DR]/[PR]. Risque fiscal sur les pièces faites à la machine (V:118) [HY]. Le motif doit être une création originale ou une œuvre du domaine public (V:78). Le site BOJ.ART présente des personnages protégés (atelier-motion-sources.json:32, 69, 99) [FV]. SECURITY.md rappelle que « visible sur un réseau social » ne veut pas dire « libre de droits » (SECURITY.md:14).
7. **Événements et vernissage.** La note de vision évoque des événements préparés par GianLuca (V:9, 24) [DR]. Le dépôt BOJART n'en parle pas. Le vernissage « Strates » repose sur l'atelier de Medhi (pour-carlone/vernissage-strates-idees.md:13) [PR].
8. **Cabaret et autres lieux.** « Piste tant que Carlone ne l'a pas confirmé » (V:56), à placer « plus tard » (V:113) ; question ouverte (V:133). Six bâtiments rachetés (V:9) [DR]. Rien dans BOJART.
9. **Medhi et BOJ.ART.** Medhi crée et fabrique ; il possède la marque et les œuvres (V:84) [PR]. La relation avec Morgan date d'un an et demi (V:23) [DR]. GianLuca a racheté l'ancienne affaire de Medhi (V:9) [DR]. Le dépôt ne nomme jamais Medhi (« l'artiste », « le propriétaire »). Retrait de l'offre le 4 nov. (note du 4 nov.:25) [DR], non répercuté dans l'offre écrite (offre :67-90) [FV].
10. **STRATES, Éclosion et créations.** STRATES : audit documentaire de 12 pages, avis favorable à un banc d'essai ciblé, pas à l'achat d'une cellule (strates README:3, 20) [PR]. Critères à 7 mm (V:62). Fiche G0 non signée (ops/orchestration.json:443). Programme R&D à 323 875 € HT jugé surdimensionné (V:61, 112) [DR]. Films « Le dernier geste » R03 et « Veille » V1 : coupes de travail (V:43). Éclosion : rien.
11. **Laboratoire IA et robotique.** Bras comparés en simulation seulement (V:41, 64) [ES]. xArm 6 recommandé ; PiPER pour un banc de coupons (V:66) [PR]. Sécurité : ISO 10218-2:2025 et règlement (UE) 2023/1230 au 20 janv. 2027 ; « aucune conformité n'est attestée » (strates README:40). Architecture proposée avec chaîne de sécurité indépendante (strates README:34) [PR]. L'offre prévoit une option de 18 journées de R&D (offre :65) [PR]. Le laboratoire devait s'appuyer sur le parc de Medhi (V:66 ; strates README:28) : son retrait laisse le banc sans atelier identifié [HY].

## 7. Erreurs d'identité

- **V** (note de vision) : 0 occurrence de « John-Lucas », « John Lucas » ou d'une autre variante. Le client y est toujours appelé « Carlone », jamais par son prénom.
- **Dépôt BOJART** : 0 occurrence dans les 933 fichiers texte suivis et les quatre PDF. Les seules correspondances de « john » se trouvent dans des octets compressés des fragments PDF, sans rapport avec le nom.
- Relevé hors périmètre, en citant les lignes « Jarvis » du dépôt Carlone : sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:109, « le copilote à construire progressivement pour les activités de John-Lucas » [sic, lire GianLuca].

## 8. Instructions trouvées dans les pièces

Aucune de ces instructions n'a été exécutée.

| Source | Contenu |
|---|---|
| B/AGENTS.md:3-18 | Règles pour les assistants : lire CURRENT et SESSION_HANDOFF, ne pas fusionner les branches d'archive, « aucun force-push », commandes de test, outils MCP. |
| B/jarvis/context/HANDOFF_CLAUDE.md:1-14 | « Mission de reprise sur le PC autorisé » : vérifier la connexion GitHub, auditer la tour en lecture seule, lancer les contrôles et le serveur, établir la recette des écrans et de la voix. |
| B/jarvis/apps/jarvis/AGENTS.md:5-12 | Règles de reprise de la Mission 03 pour un assistant. |
| B/docs/preinstallation/DECISIONS_UTILISATEUR.txt:2 | « Le destinataire demandé est Claude Opus 5.5 » : mission d'audit et de préparation. |
| B/docs/audits/jarvis-installation-2026-11-01/RAPPORT.md:56-59 | « Priorités pour l'auditeur » : rejouer l'installation, installer les moteurs réels, qualifier une FDM et une résine. |
| B/README.md:3, 23-30 ; B/INSTALLER_DEMAIN.md:5-15 ; POSTE_RTX4060TI.md:26-35 | Instructions d'installation et de lancement, y compris le téléchargement de modèles. |
| B/jarvis/README.md:16-20 | « Commencer sans perdre le fil » : commandes de vérification. |
| B/SECURITY.md:3-14 | Interdits du dépôt public et recommandation de le passer en privé. |
| B/docs/research/strates-robotique-2026-11-02/README.md:56 | « Si l'utilisateur l'autorise, verser le PDF, les deux vidéos et le texte de la conversation dans un stockage privé ». |
| V:120 | Demande d'action : passer le dépôt du CRM de GianLuca en privé « sans attendre ». |
| V:124-138 | Liste de 13 décisions et informations attendues. |
| Répertoires `skills/`, `jarvis/.claude/skills/`, `jarvis/.agents/skills/` | Fichiers SKILL.md destinés à des agents IA (présence constatée, non lus). |

## 9. Points d'audit

**Maturité réelle.**
- Ce qui est démontré : un logiciel testé dans des conteneurs Linux et sur les machines Windows de la CI, sur des données synthétiques ou fictives. La mémoire documentaire, la restauration, les gardes et la distribution des commandes ont été mesurées (tableau 2, l. 4, 11 à 15).
- Ce qui n'est que déclaré : la voix, les trois écrans, les imprimantes, le modèle local, le filtre de droits (l. 45) et la fluidité.
- Après quatre jours d'efforts intenses (30 oct.–2 nov.), aucune heure d'usage réel sur le poste n'est documentée.
- La note de vision présente ce niveau comme « Tests et CI verts » (V:38) ; c'est inexact pour le cœur M06/M07 (l. 5 et 6).

**Copilote chez GianLuca.**
- Le copilote vendu à GianLuca (4 jours au premier mois) est un autre produit que le Jarvis de l'atelier. Seuls la mémoire documentaire, le registre d'affirmations, le principe de garde et la méthode de preuve sont transposables (section 6, chantier 4).
- La valeur d'un copilote dépend de la qualité des réponses sur ses données. Or la seule mesure disponible porte sur 14 questions et montre des sources perdues dans 28,6 % des cas à 8 000 octets (l. 13).
- Un démonstrateur en 28 heures est plausible pour une recherche documentaire sur des données fictives [HY]. Il ne l'est pas pour des automatisations reliées aux outils de GianLuca : messagerie, agenda, CRM, comptabilité.

**Propriété de Jarvis.**
- Quatre versions incompatibles coexistent (section 4) et aucune licence n'existe.
- Avant de proposer à GianLuca un produit appelé « Jarvis », il faut un écrit séparant trois choses : les composants génériques (à Morgan ou à Marwin Tech), les développements propres à BOJ.ART et les développements propres à GianLuca.
- Le nom « Jarvis » désigne déjà deux produits. Il évoque aussi un personnage d'une franchise commerciale et un projet de Microsoft (RECHERCHE:20) : vérifier la marque avant tout usage commercial [HY].

**Dépendances matérielles.**
- La tour reste mal connue : configuration rapportée sur photo, RAM inférieure au besoin annoncé, système Insider Preview, latences Windows jusqu'à 18 s en CI.
- Le copilote de pilotage ne doit dépendre ni de cette tour ni d'un GPU appartenant au pôle de Medhi.
- Le discours « local d'abord » masque des services payants (Jev, génération vidéo) dont le coût n'est chiffré nulle part.

**Compétences démontrées de Morgan.**
- Démontré par ce dépôt :
  - piloter des sessions d'assistants IA de manière soutenue ;
  - exiger des preuves datées et versionnées (empreintes, restaurations, séparation mesuré / simulé / déclaré) ;
  - mettre en place une CI multi-plateforme ;
  - documenter ses limites honnêtement ;
  - assembler un pipeline de production vidéo avec fournisseurs IA.
- Non démontré :
  - le déploiement sur un vrai poste ;
  - l'adoption par un utilisateur (Medhi) ;
  - la maintenance dans la durée ;
  - un revenu tiré de Jarvis ;
  - la part du code écrite personnellement (l. 36).
- Mathys n'apparaît pas dans ce dépôt.
- Point de vigilance : la densité documentaire est très forte (journal de 244 lignes en trois jours, dizaines de rapports). Elle risque de consommer la capacité plutôt que de produire des livrables reçus par un client.

**State Of The Art depuis le 4 novembre.**
- La vision reposait sur trois pôles. Le retrait de Medhi et de BOJ.ART supprime le pôle art, la première étape (STRATES Phase 1), le banc robotique adossé au parc de Medhi et le fondement du vernissage « Strates ».
- Pourtant, la note de vision, l'offre écrite (:67-90), le vernissage et STRATES v1.1 restent en l'état. Ces documents contradictoires ne doivent pas être présentés à GianLuca ; il faut les dater comme versions antérieures.
- Les principes de la vision restent valables et deviennent plus urgents : propriété écrite, une facture par activité, part maximale de revenus venant d'un seul client, trois validations indépendantes (V:82-90).
- L'annotation « ( 10 millions » (V:134) contredit le principe de dépendance limitée et doit être clarifiée.

**Données de GianLuca.**
- Aucune donnée de GianLuca n'est présente dans la révision publique examinée (l. 57).
- Cette vérification ne couvre pas l'historique Git (clone d'un seul commit), les branches d'archive (3 340 contenus), les branches non fusionnées ni les vidéos.
- Le dépôt publie déjà des documents internes de Marwin (l. 58) et le lien BOJ.ART / Marwin Tech (l. 37). Toute réutilisation pour GianLuca doit partir d'un dépôt privé distinct.
- Le risque le plus concret reste le dépôt CRM public signalé le 2 nov. (V:120). Son état actuel n'est pas vérifié ici.

**Chiffres non justifiés ou hypothèses présentées comme des faits.**
- Le programme R&D de 323 875 € HT, les prix des bras « relus » sans devis, la durée de 6–9 h et le gain de 15,25 % sur une fixture fictive sont des estimations.
- Les attributs prêtés à GianLuca (avenue Montaigne, six bâtiments, investissement) sont des déclarations rapportées par Morgan (V:28), non vérifiées.
- Le taux implicite de 750 € HT par journée (offre :84) n'est pas justifié dans mes pièces.

**Risques non traités.**
- Point de défaillance unique : Morgan et les sessions IA, sans relecteur humain indépendant.
- Système Windows Insider sur un poste de production.
- Droits sur les pièces existantes de BOJ.ART.
- Dépendance à des fournisseurs payants.
- Absence d'accord avec Medhi sur Jarvis et la tour.
- Temps passé sur BOJ.ART alors que l'agenda montre de nombreux projets parallèles (note du 4 nov., partie B).
