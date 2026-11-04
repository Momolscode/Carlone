# Lecteur C8 « créations » : STRATES, Éclosion, laboratoire IA et robotique

Rédigé le 4 novembre 2026 pour l'audit Carlone. Le client s'appelle **GianLuca Carlone**. Les pièces disent « Carlone » ou, une fois, « John-Lucas » [sic, lire GianLuca]. Je n'ai fait aucune action extérieure et je n'ai modifié aucun dépôt. Les sources web citées par les pièces n'ont pas été rouvertes : ce qu'elles affirment reste donc au mieux [DR].

Conventions de citation : sans préfixe, un chemin part de `Momolscode/Carlone` (commit 7b46602). Pour les PDF, la page est celle du PDF d'origine. `bojart/…` part de le dépôt Momolscode/BOJART (commit 3436f53). `deck/…` part de `[diaporama Offre Marwin Tech, copie du 4 nov.] `. `note:N` renvoie à `audit-work/note-point-4-novembre-et-activites.md`, ligne N.

---

## 1. Pièces lues

| # | Chemin | Date de la pièce | Nature et auteur | Original ou copie / export | Ce qui n'a pas pu être lu |
|---|---|---|---|---|---|
| 1 | `pour-carlone/strates-proposition-artistique-v1.1.pdf` (8 p.) | 2 nov. 2026. Création du PDF le 2 nov. à 00:22 UTC, soit 01:22 à Paris (métadonnées). | Proposition artistique et technique « pour Carlone », avec l'en-tête « BOJ.ART / MARWIN TECH » sur les 8 pages. Elle a été générée dans ChatGPT pendant le tour de 01:16–01:24 (`sources/chatgpt-conversations/2026-11-04/bras-robotique-precis.json:65-72`). | Copie renommée. Le nom d'origine était « CARLONE_STRATES_Proposition_Artistique_2026-11-02.pdf » (même fichier json, l. 72). Lecture par extraction texte. | Les 3 visuels IA n'ont pas été examinés. Faute d'empreinte, rien ne prouve que ce soit le même fichier que celui de ChatGPT. |
| 2 | `interne/strates-audit-robotique-ia.pdf` (12 p.) | 2 nov. 2026 | « Revue de conception » BOJ.ART / Marwin Tech, rédigée par ChatGPT (json l. 40-47, tour de 02:24–02:32, heure de Paris). | **Original constaté** : SHA-256 `2a9830490b0e…a47e94`, 109 437 octets, identique à l'empreinte notée dans `bojart/docs/research/strates-robotique-2026-11-02/README.md:9`. | Sources R1–R9 non rouvertes. |
| 3 | `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` (11 p.) | 31 oct. 2026 | Audit stratégique et documentaire Marwin Tech, « préparé pour Morgan Olsen ». L'auteur n'est pas nommé ; une production par IA est probable [HY]. | Version déposée, sans métadonnées. | Les pièces que cet audit a examinées (proposition v5 du 30 oct., 26 p. ; dossier société ; pilotage) ne sont pas dans mon lot. Sources [1]–[11] non rouvertes. |
| 4 | `pour-carlone/eclosion/concept-2026-10-31.pdf` (5 p.) | 31 oct. 2026 | Concept de travail v0.1, Marwin Tech, « préparé pour Morgan Olsen », alors que le fichier est rangé dans `pour-carlone/`. | Version déposée. | Visuels et animation non examinés. |
| 5 | `interne/eclosion/ebauche-mecanique-p0-2026-10-31.pdf` (4 p.) | 31 oct. 2026 | Étude mécanique v0.2 d'un pétale, Marwin Tech. | Version déposée. | Les fichiers STEP, STL et SCAD, `build_p0.py` et le ZIP n'ont pas été ouverts. |
| 6 | `interne/strates/archives-investisseur/dossier-investisseur-v1-2026-11-02.pdf` (23 p.) | 2 nov. 2026 | « Dossier investisseur et cahier des charges : peinture robotisée de figurines », v1.0, BOJ.ART / Marwin Tech. Produit par ChatGPT le 2 nov. entre 00:38 et 00:50 (json l. 135-142). | Copie rangée dans un dossier nommé « archives ». | Visuels non examinés ; sources S1–S15 non rouvertes. |
| 7 | `interne/strates/archives-investisseur/budget-v1-2026-11-02.xlsx` (3 onglets) | 2 nov. 2026. Les entrées du ZIP datent du 1er nov. à 17:49 (horloge du générateur) et le commentaire de la cellule E12 est daté du 2026-11-01 à 23:49Z. Auteur affiché : « BOJ.ART — dossier de travail ». | Budget du programme de figurines : 53 lignes, 112 formules. | Lu sur l'export texte, puis inspecté en lecture seule : formules et commentaire de la cellule `Depenses!E12`. Il n'y a pas de métadonnées docProps, donc pas de date de création fiable. | Formules relues sans être toutes testées. |
| 8 | `interne/eclosion/prototype-p0/LIRE_AVANT_ESSAI.txt` (58 l.) | 31 oct. 2026 | Notice du pack Éclosion P0. | Original. | — |
| 9 | `interne/eclosion/prototype-p0/calculs_et_controles.json` (99 l.) | Non daté (v0.2) | Résultats de calcul et contrôles géométriques. | Original. | Calculs non relancés ; j'ai recalculé à la main le couple de gravité et l'inertie. |
| 10 | `sources/chatgpt-conversations/2026-11-04/bras-robotique-precis.json` (149 l.) | Conversation du 2 nov. 2026, de 00:12 à 02:52 (heure de Paris). Collecte du 4 nov. | Conversation ChatGPT « Bras robotique précis » entre Morgan et ChatGPT. | **Export partiel** : « pas un export intégral de compte » (l. 2). | Le tour de 01:07 (l. 85-90) n'a pas de réponse. Les échanges entre 00:12 et 00:38 manquent. Les fichiers liés (`libfile_…`) et la vidéo sont inaccessibles. |
| 11 | `bojart/docs/research/strates-robotique-2026-11-02/README.md` (56 l.) | 2 nov. 2026 (commit 3436f53, 2 nov. à 03:56 +0100) | Note de recherche du dépôt **public** BOJART (Jarvis BOJ.ART). Auteur non indiqué. | Original. | `PROVENANCE.json` non lu ; `verification-calculs.json` seulement parcouru. |
| C | Compléments hors lot, lus pour mesurer l'effet du retrait de Medhi : `deck/slides/laboratoire.html`, `deck/slides/strates.html`, `deck/slides/strates-phases.html`, `interne/eclosion/prototype-p0/nomenclature.csv` | 2–4 nov. 2026 | Diapositives client (la diapositive laboratoire est toujours présente ; les deux diapositives STRATES ont été retirées) et nomenclature P0. | Fichiers de travail. | Aucun autre fichier du diaporama n'a été lu. |

---

## 2. Affirmations déterminantes

| # | Affirmation | Code | Source | Remarque |
|---|---|---|---|---|
| 1 | STRATES est une « Œuvre proposée, non fabriquée ». Il n'existe « aucun objet physique, dispositif robotique, film réel de fabrication ou résultat commercial validé ». | [FV] | `pour-carlone/strates-proposition-artistique-v1.1.pdf` p. 1 et p. 4 | C'est l'état déclaré au 2 nov. Aucune pièce de mon lot ne le contredit. |
| 2 | « Aucun prix de vente, engagement de Carlone ou intérêt de collectionneur n'est acquis. » | [FV] | idem, p. 2 | La valeur commerciale de STRATES n'est donc pas testée. |
| 3 | Partage des rôles : l'artiste / BOJ.ART dessine, modèle, définit le geste, choisit les matières et accepte la pièce. Marwin prépare l'outil, le guidage et la mesure. Carlone évalue et fixe les conditions de vente. | [PR] | idem, p. 2 | Sans l'artiste, il reste à Marwin l'outillage et la mesure, pas l'œuvre. |
| 4 | L'artiste visé est Medhi : « Medhi crée, choisit et signe ». | [PR] | `deck/slides/strates.html:12` (diapositive retirée) | Aucune des 11 pièces de mon lot ne nomme Medhi. Elles disent seulement « Artiste / BOJ.ART » ou « peintre référent ». |
| 5 | Premier test proposé : échantillon de 30 × 40 cm, segment de 10–15 cm, trait de 5–10 mm, 20 passages. Ce sont des « objectifs de test, pas des résultats ». | [PR] | `pour-carlone/strates-proposition-artistique-v1.1.pdf` p. 3 | Le test suppose « un bras disponible, un montage calibré et une supervision adaptée ». Aucune de ces trois conditions n'est réunie. |
| 6 | Critères proposés : trait nominal de 7 mm ; largeur de 6 à 8 mm sur au moins 90 % de la longueur ; débordement d'au plus 1 mm ; 19 essais conformes sur 20. | [PR] | idem, p. 7 | La pièce précise : « Ces seuils sont des propositions, pas des performances acquises. » |
| 7 | Le planning de six semaines ne commence qu'« après accès à un bras, disponibilité de l'intégrateur et réception des supports ». | [PR] | idem, p. 7 | Aucun bras ni intégrateur n'est identifié. |
| 8 | « Les 10 000 EUR envisagés pour le cadrage restent une enveloppe de discussion, non engagée. » | [PR] | idem, p. 4 | Ce montant vient du P0 du programme de figurines (ligne 63). Ce n'est pas un chiffrage de STRATES. |
| 9 | Les 323 875 € HT « couvrai[ent] un programme de douze mois pour la peinture de figurines » et ne sont pas le devis de STRATES : il faut un nouveau chiffrage. | [FV] | idem, p. 4 ; `interne/strates-audit-robotique-ia.pdf` p. 10 | STRATES n'a donc **aucun budget chiffré**. |
| 10 | « Aucun achat n'est engagé et aucun nouveau devis n'a été obtenu pour STRATES. » | [FV] | `pour-carlone/strates-proposition-artistique-v1.1.pdf` p. 8 | — |
| 11 | Le matériel initial « avait été provisionné à 25 000 EUR HT, avant intégration ». | [ES] | idem, p. 4 | Ce montant correspond aux équipements de la phase P1 du budget de figurines (10 500 + 2 500 + 4 500 + 1 500 + 4 500 + 1 500 €). Ce n'est pas un devis. |
| 12 | Le film de concept a été généré avec Kling 3.0 Pro via Higgsfield (environ 10 s) et porte un marquage IA permanent : « aucune performance physique ne peut être déduite ». | [FV] | idem, p. 8 | Les droits d'usage commercial des médias IA ne sont établis nulle part (voir n° 62). |
| 13 | Verdict de la revue robotique : « avis favorable à un banc d'essai ciblé ». L'achat d'une cellule et le programme de 323 875 € « demandent des preuves supplémentaires ». | [DR] | `interne/strates-audit-robotique-ia.pdf` p. 1 | C'est l'avis de ChatGPT, pas celui d'un expert identifié. |
| 14 | Cette « revue » est sortie de ChatGPT sur la consigne « Audit ce projet comme un ingénieur en robotique… ayant eu 220 à son test de QI ». Elle porte sur des documents que le même outil avait produits environ 1 h 45 plus tôt. | [FV] | `sources/chatgpt-conversations/2026-11-04/bras-robotique-precis.json:40`, `:47`, `:142` | **Ce n'est pas une revue indépendante.** |
| 15 | Aucune performance STRATES n'a été mesurée. « Aucun accès au robot, fichier CAO réel de STRATES, corpus physique, devis signé ou vente n'a été fourni. » | [FV] | `interne/strates-audit-robotique-ia.pdf` p. 1 | Aucun [MM] dans tout le lot. |
| 16 | Le bras six axes n'est « pas encore » justifié. Il faut comparer un bras existant et un banc cartésien. | [PR] | idem, p. 1 et p. 3 | Le budget de figurines prévoit pourtant l'achat d'un bras dès P1 (ligne 24). |
| 17 | Le budget compte 53 lignes cohérentes : base de 259 100 €, réserve de 25 % soit 64 775 €, total de 323 875 € HT. | [FV] | idem, p. 10 ; `interne/strates/archives-investisseur/budget-v1-2026-11-02.xlsx`, feuilles Depenses (F7:F59) et Budget (C14:E14) | J'ai recalculé : 53 lignes, Σ = 259 100 €. Cela ne valide ni les taux ni les besoins. |
| 18 | Le travail humain pèse 199 850 €, soit 77,1 % de la base, pour 357 jours-personnes (1,62 ETP sur 220 j/an). Le calcul GPU externe coûte 2 250 € (0,87 %). | [FV] | idem p. 10 ; xlsx Depenses | Mon recalcul : 200 j à 650 € (robotique et données), 60 j à 300 € (peintre), 45 j à 450 €, 40 j à 550 €, 12 j à 800 €. **Aucune personne n'est nommée.** |
| 19 | 19 réussites sur 20 donnent une borne inférieure d'environ 78,4 % (à 95 %, unilatérale). Il faut 59 réussites sur 59 pour dépasser 95 %. | [FV] | `interne/strates-audit-robotique-ia.pdf` p. 8 | Recalculé : 0,7839 et 0,9505. |
| 20 | La norme ISO 10218-2:2025 traite l'intégration des cellules. Un bras « collaboratif » ne qualifie pas le montage complet ; il faut une vérification par un intégrateur compétent. | [DR] | idem, p. 9 | Norme non consultée. Aucun intégrateur n'est identifié. |
| 21 | Le règlement machines (UE) 2023/1230 s'applique à partir du 20 janvier 2027 ; le régime et les responsabilités sont « à préciser contractuellement ». | [DR] | idem, p. 9 ; `interne/strates/archives-investisseur/dossier-investisseur-v1-2026-11-02.pdf` p. 18 | Cohérent avec mes connaissances, non revérifié en ligne. Le régime en vigueur avant cette date n'est traité nulle part (point d'audit n° 7). |
| 22 | « La présence d'un robot ne garantit aucune prime de vente. » L'économie de série ne justifie pas à elle seule une œuvre unique. | [HY] | `interne/strates-audit-robotique-ia.pdf` p. 10 | C'est le point central pour la galerie. |
| 23 | Avec une seule pièce par recette, le robot coûterait 554,82 € par pièce, contre 48 € à la main (scénario fictif de figurines). | [ES] | idem, p. 10 | Ordre de grandeur utile : une œuvre unique ne se rentabilise pas par l'automatisation. |
| 24 | Le dossier investisseur porte sur la **peinture robotisée de figurines** en résine de 15 à 40 cm, pas sur STRATES. | [FV] | `interne/strates/archives-investisseur/dossier-investisseur-v1-2026-11-02.pdf` p. 1-2 | STRATES est une adaptation faite après coup (n° 28). |
| 25 | Financement proposé : 325 000 € en trois tranches (A : 71 000 € ; B : 95 000 € ; C : 159 000 €), avec une première libération plafonnée à 10 000 €. | [PR] | idem, p. 2 et p. 20 ; xlsx Budget B18:B21 | Tranches libérées sur preuve (G0, G1, G3). |
| 26 | Le budget est établi « sans recette commerciale ni subvention supposée ». Rien n'indique que des achats, rendez-vous ou « sollicitations d'investisseurs » aient eu lieu. | [FV] | idem, p. 2 et p. 19 | — |
| 27 | Morgan écrit : « L'investisseur en question serait Carlone ». | [DR] | `sources/chatgpt-conversations/2026-11-04/bras-robotique-precis.json:110` (2 nov., 00:56) | **C'est la seule base de l'hypothèse « Carlone financeur ».** Aucune pièce n'atteste l'intérêt ni l'accord de GianLuca Carlone. |
| 28 | Morgan écrit encore : « Carlone vend des œuvre d'art il est moins figurine hehe… retravaille l'idée ». STRATES naît de ce message. | [DR] | idem, l. 90 | Le passage des figurines à l'art s'est fait en 1 h, sans nouveau chiffrage. |
| 29 | Les porteurs pressentis sont BOJ.ART et Marwin Tech. Le véhicule juridique, les engagements des associés et les droits sur les données restent « à formaliser ». | [FV] | `interne/strates/archives-investisseur/dossier-investisseur-v1-2026-11-02.pdf` p. 1 | Marwin Tech n'est pas immatriculée et BOJ.ART n'a pas de statut juridique documenté ici. |
| 30 | Option proposée en premier : « BOJ.ART garde la cellule, maîtrise le procédé et facture ». | [PR] | idem, p. 3 | **Le matériel financé par un investisseur resterait chez BOJ.ART.** |
| 31 | Participation au capital, valorisation, propriété intellectuelle et exclusivités seraient « négociées séparément ». | [PR] | idem, p. 2 | La structure qui recevrait les fonds n'est pas désignée [IN]. |
| 32 | Le dossier prévoit un « Porteur produit BOJ.ART / Morgan », un peintre référent, un ingénieur robotique, un ingénieur données, un mécanicien-métrologue et un intégrateur sécurité. | [PR] | idem, p. 20 | Aucune de ces personnes n'est nommée, à part Morgan [IN]. Mathys est absent. |
| 33 | Exigences pour les figurines : trait de 0,50 mm ± 0,15 mm ; contour P95 ≤ 0,20 mm. | [PR] | idem, p. 6 | Niveau de recherche « non validé » (`interne/strates-audit-robotique-ia.pdf` p. 2). |
| 34 | UFACTORY 850 avec contrôleur DC : prix affiché 11 798,56 € TTC hors port chez DHM. | [DR] | `…/dossier-investisseur-v1-2026-11-02.pdf` p. 15 ; xlsx `Depenses!E12` (commentaire) | Page consultée le 2 nov. selon la pièce, non revérifiée. Ce n'est pas un devis. |
| 35 | Économie d'une recette : 48 € par pièce à la main contre 40,02 € par robot ; écart de 6 382 € par an ; seuil de 533 pièces par an. La demande de 800 pièces est une « hypothèse commerciale, pas un carnet de commandes ». | [ES] | idem, p. 16 ; xlsx Economie B19, B35-B38 | Formules relues, cohérentes. Le scénario est entièrement fictif. |
| 36 | Bourse French Tech : « jusqu'à 30 000 EUR et 70 % des dépenses éligibles », non acquise. Aucun CIR ni CII n'est déduit. | [DR] | `…/dossier-investisseur-v1-2026-11-02.pdf` p. 20 et p. 23 (S14) | L'éligibilité d'une société non immatriculée n'est pas examinée [IN]. |
| 37 | Le projet est « désormais formalisé comme une piste R&D prioritaire à instruire ». | [PR] | idem, p. 21 | Il a pourtant été rangé en « archives » et la revue le requalifie en « ancien scénario R&D » (`interne/strates-audit-robotique-ia.pdf` p. 10). |
| 38 | Recommandation de l'audit laboratoire : un laboratoire d'ingénierie appliquée « financé par des missions clients ». L'exosquelette est traité à part. | [PR] | `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` p. 1 | Raisonnement sain. Il condamne le financement de la recherche par l'abonnement. |
| 39 | « Les 30 000 € du pilote ne sont pas 30 000 € d'honoraires. » Détail : 13 500 € d'honoraires (18 j à 750 €), 10 000 € de poste de calcul, 2 500 € de composants, 1 500 € de stockage et réseau, 1 000 € de logiciels, 1 500 € d'imprévus. | [ES] | idem, p. 1 et p. 8 | 16 500 € sont des achats, pas du chiffre d'affaires de Marwin. |
| 40 | « L'enveloppe de 10 000 € n'est pas un besoin démontré. Une DGX Spark n'est ni acquise ni indispensable par principe. » | [DR] | idem, p. 9 | Le diaporama garde pourtant 30 000 € (n° 48). |
| 41 | Pour le laboratoire : « aucune preuve d'atelier opérationnel ni d'équipe biomécanique », aucun essai matériel, « aucun engagement ou paiement établi ». | [FV] | idem, p. 1-2 | — |
| 42 | Accès déclaré à « environ dix imprimantes via l'atelier BOJ.ART » ; « ne pas présumer un apport ». | [DR] | idem, p. 2 | Cet accès devient incertain après le retrait de BOJ.ART. |
| 43 | Le scénario réserve 26 journées-personnes par mois. Deux personnes à 20 j chacune en offrent 40. « Leur disponibilité n'est pas établie. » | [ES] | idem, p. 8 | La note signale de nombreux projets parallèles de Morgan (note:13-17). |
| 44 | « L'investissement immobilier rapporté de John-Lucas [sic, lire GianLuca] ne prouve ni son budget d'innovation, ni le rendement de nos services. » | [DR] | idem, p. 2 | Cet avertissement de l'audit lui-même contredit l'hypothèse « Carlone investisseur ». |
| 45 | Règle « trois travaux maximum, un seul essai exploratoire » ; « Ne pas ajouter un essai robotique tant que l'unique place exploratoire est occupée. » | [PR] | idem, p. 1 et p. 10 ; `pour-carlone/eclosion/concept-2026-10-31.pdf` p. 4 | STRATES, Éclosion P0 et le pilote laboratoire se disputent cette place unique. |
| 46 | Le CIR « n'est pas ouvert du seul fait de créer un "labo IA" » ; le CII est soumis à conditions ; aucune aide ne doit être comptée. | [DR] | `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` p. 9 | Sources BOFiP et DGFiP non rouvertes. À valider par un expert-comptable. |
| 47 | « Mathys Couet est cité sur le dossier Carlone ; cela ne fixe pas » les associés, leurs parts ni leur disponibilité. | [FV] | idem, p. 2 | **C'est la seule mention de Mathys dans tout le lot.** |
| 48 | Le diaporama actuel (11 diapositives) garde l'« Option laboratoire 30 000 € HT dont 13 500 € d'honoraires », le « geste robotique simple » et le « Matériel acheté et possédé par votre entité ». | [FV] | `deck/slides/laboratoire.html:9-14` | La robotique reste donc dans l'offre malgré le retrait de STRATES. |
| 49 | Phase 1 de STRATES sur la diapositive retirée : « Fiche signée, coupons peints à la main par Medhi, premier trait robotisé et sa mesure : 2 à 4 semaines, environ 10 000 € HT ». En contrepartie : première présentation à la galerie et exclusivité de vente sur la série. | [PR] | `deck/slides/strates-phases.html:11-12`, `:42` | Ces 10 000 € incluraient un trait robotisé, ce que le P0 d'origine ne prévoyait pas (n° 63). |
| 50 | Une œuvre réalisée avec un robot « n'entre très probablement pas » dans le dispositif de déduction pour les entreprises (œuvre « entièrement exécutée à la main par l'artiste »). | [HY] | `deck/slides/strates-phases.html:43` | Plausible, mais à valider par un professionnel. Cela affaiblit un argument de vente auprès des entreprises. |
| 51 | Éclosion : « Aucun prototype physique, retour de visiteur, devis fournisseur ou résultat commercial obtenu. » Les commandes ont été « vérifiées dans un environnement logiciel simulé ». | [FV] / [DR] | `pour-carlone/eclosion/concept-2026-10-31.pdf` p. 1 | La simulation n'est pas archivée dans mon lot [IN]. |
| 52 | L'intérêt d'Éclosion « doit être évalué auprès de visiteurs et d'un acheteur réel ». Le panel de regards est « fictif ». | [HY] | idem, p. 1-2 | Il n'y a aucun acheteur. |
| 53 | Chiffrage d'Éclosion : six journées-personnes à 750 € HT, soit 4 500 € HT d'honoraires, hors pièces, sous-traitance et transport ; c'est une « hypothèse à estimer ». | [ES] | idem, p. 5 | Ce chiffre ne couvre pas la sculpture complète. |
| 54 | Pour Éclosion, « BOJ.ART et les autres contributeurs conservent leurs droits tant qu'un accord n'en dispose pas autrement ». Il faudra distinguer l'exemplaire, la propriété, les plans, le logiciel et la reproduction. | [PR] | idem, p. 5 | Aucun accord de droits n'existe dans mon lot. |
| 55 | Éclosion P0 : 4 solides CAO valides ; un balayage de 61 positions (20° à 80°) ne montre aucune intersection (0,0 mm³) ; `hardware_validation: false`. | [FV] | `interne/eclosion/prototype-p0/calculs_et_controles.json:17-18`, `:66-71`, `:98` | C'est un contrôle numérique, pas une mesure physique. |
| 56 | Couple cible de 0,08 N·m (dimensionnement : 0,0721 N·m, facteur 2). Servo candidat Hitec D85MG : environ 0,088 N·m au rendement maximal, « pas un couple continu garanti ». | [ES] | `interne/eclosion/ebauche-mecanique-p0-2026-10-31.pdf` p. 3 ; json l. 83-97 | J'ai recalculé le couple de gravité (0,02755 N·m) et l'inertie (0,000789 kg·m²). La marge du servo sur la cible n'est que d'environ 10 %. |
| 57 | Le pack P0 « n'est pas une machine achevée, une validation de résistance ou une autorisation d'exposition au public ». « Aucun achat réalisé. » | [FV] | `interne/eclosion/prototype-p0/LIRE_AVANT_ESSAI.txt:4-5`, `:57` ; `nomenclature.csv:6-12` | Rien n'a été fabriqué ni commandé. |
| 58 | Le dépôt public BOJART conserve le PDF de la revue « hors Git public », parce qu'il « reprend des montants… et nomme le partenaire ». Il publie pourtant un résumé détaillé de STRATES (critères, jalons, architecture). | [FV] | `bojart/docs/research/strates-robotique-2026-11-02/README.md:9`, `:16-44` | Une proposition faite à un client est résumée dans un dépôt public. Carlone n'y est pas nommé (note:21). |
| 59 | Le 2 nov., la conversation était « Non lue » (erreur HTTP 403). Son rattachement à BOJ.ART repose sur « la déclaration de l'utilisateur ». | [FV] | idem, l. 12-14 | — |
| 60 | STRATES est classé comme recherche de Jarvis BOJ.ART (`bojart.jarvis`, collection `research`), et « aucun pouvoir physique [n'est] conféré par un document ». | [FV] | idem, l. 52 | **BOJ.ART a archivé STRATES comme sa propre recherche.** C'est un risque de revendication. |
| 61 | Décision du 4 nov. : « Va juste falloir enlever Medhi/boj art de l'offre ». La proposition STRATES v1.1 n'a pas été modifiée. | [DR] | note:25 | Décision orale, ni formalisée avec Mathys ni avec Medhi. |
| 62 | Pour la vidéo « Photorealistic-10-second… », « droits du personnage non vérifiés ». | [FV] | `bojart/docs/research/strates-robotique-2026-11-02/README.md:11` | Les droits sur les médias IA ne sont pas sécurisés. |
| 63 | Le P0 du programme de figurines (S1–S2) comprend : peintre 5 j, robotique et métrologie 6 j, cadrage 3 j, éprouvettes 500 €, quote-part d'atelier 250 €. Base de 7 500 €, soit 9 375 € avec la réserve. **Aucun bras n'y figure.** | [FV] | xlsx `Depenses!A7:F11`, `Budget!C8:E8` ; `…/dossier-investisseur-v1-2026-11-02.pdf` p. 13-14 | C'est l'origine des « 10 000 € de cadrage » repris pour STRATES. |

---

## 3. Chiffres, engagements et dates

### Budgets et montants

| Élément | Valeur | Code | Source |
|---|---|---|---|
| Phase 1 de STRATES (diapositive retirée) | environ 10 000 € HT, 2 à 4 semaines | [PR] | `deck/slides/strates-phases.html:11` |
| « Enveloppe de cadrage » de STRATES | 10 000 €, non engagée | [PR] | `pour-carlone/strates-proposition-artistique-v1.1.pdf` p. 4 |
| Phases 2 et 3 de STRATES | « Chiffrée à la fin de la phase 1 / 2 » | [IN] | `deck/slides/strates-phases.html:20`, `:29` |
| Matériel initial (STRATES et figurines) | 25 000 € HT avant intégration | [ES] | STRATES v1.1 p. 4 ; json l. 117 |
| Ordre de grandeur d'un test STRATES de 6 semaines (**mon estimation**) | Environ 9 000 à 19 500 € HT, **hors accès au bras** [IN] et hors coordination Marwin. Hypothèses : intégrateur 10 à 18 j à 650 € (taux du tableur) ; artiste 6 à 10 j à 300 € ; mesure 0 à 2 500 € ; porte-pinceau et fixation 500 à 1 500 € ; consommables 300 à 800 €. | [ES] | calcul de l'auditeur à partir de STRATES v1.1 p. 7-8 et des taux du xlsx `Depenses` |
| Programme de R&D figurines | Base 259 100 € + réserve de 25 % (64 775 €) = 323 875 € HT | [ES] | dossier investisseur p. 14 ; xlsx Budget C14:E14 |
| Coût par phase (avec réserve) | P0 9 375 € ; P1 60 687,50 € ; P2 42 250 € ; P3 52 812,50 € ; P4 92 250 € ; P5 66 500 € | [ES] | xlsx Budget E8:E13 |
| Enveloppe proposée à l'investisseur | 325 000 € : tranche A 71 000 €, B 95 000 €, C 159 000 € ; coussin de 1 125 € | [PR] | dossier p. 2 et p. 20 ; xlsx Budget B18:D21 |
| Répartition par nature | Équipement 36 500 € ; ingénierie 199 850 € ; essais 7 900 € ; fonctionnement 14 850 € | [ES] | dossier p. 14 ; xlsx Budget B25:B28 |
| Détail des équipements | Bras 10 500 € ; vision 2 500 € ; mesure d'effort 4 500 € ; montage et protections 6 000 € ; informatique 1 500 € ; extensions P4 11 500 € | [ES] | dossier p. 15 |
| Journées valorisées | 357 j : 200 j × 650 €, 60 j × 300 €, 45 j × 450 €, 40 j × 550 €, 12 j × 800 € | [ES] | xlsx Depenses (mon recalcul) |
| Charge par phase | P0 14 j ; P1 35 j ; P2 57 j ; P3 70 j ; P4 104 j (sur 3 mois, environ 1,9 ETP) ; P5 77 j | [ES] | xlsx Depenses (mon recalcul) |
| Quote-part d'atelier et d'assurance (atelier BOJ.ART) | 6 000 € sur 12 mois | [ES] | xlsx Depenses, lignes « Quote-part » (mon recalcul) |
| Calcul GPU externe | 1 500 h à 1,50 € = 2 250 € | [ES] | xlsx Depenses ; dossier p. 15 |
| Bras UFACTORY 850 avec contrôleur DC | 11 798,56 € TTC hors port | [DR] | dossier p. 15 et p. 22 |
| Volume de données envisagé | Environ 720 Go (2 flux à 8 Mbit/s pendant 100 h) | [ES] | dossier p. 11 |
| Économie d'une recette | Manuel 48 € ; robot 40,02 € ; écart 6 382 €/an ; seuil 533 pièces ; capacité 950 ; demande supposée 800 | [ES] | xlsx Economie B28-B38 |
| Retour sur la R&D (**mon calcul**) | 323 875 € ÷ 6 382 €/an ≈ **51 ans** pour une seule cellule, dans le scénario même du dossier | [ES] | calcul de l'auditeur ; le dossier dit seulement que la R&D « n'[est] pas amortie » (p. 16) |
| Bourse French Tech | jusqu'à 30 000 €, 70 % des dépenses éligibles | [DR] | dossier p. 20 |
| Pilote laboratoire | 30 000 € HT, dont 13 500 € d'honoraires, 10 000 € de poste de calcul, 2 500 €, 1 500 €, 1 000 € et 1 500 € | [PR] | `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` p. 8 ; `deck/slides/laboratoire.html:9-10` |
| Taux de référence | 750 € HT par journée-personne de 7 h | [PR] | audit laboratoire p. 7 |
| Grille de prestations | Audit 3 j : 2 250 € ; lot numérique 6 à 12 j : 4 500 à 9 000 € ; suivi 2 j/mois : 1 500 €/mois ; étude d'assistance physique 4 à 8 j : 3 000 à 6 000 € ; exosquelette : non chiffré | [PR] | audit laboratoire p. 7 |
| Trois premiers mois si le client achète le matériel | 45 000 € d'accompagnement + 13 500 € = 58 500 € d'honoraires ; budget client de 75 000 € | [ES] | audit laboratoire p. 8 |
| Contribution sur 58 500 € | 53,3 % / 40,0 % / 26,7 % pour un coût de 350, 450 ou 550 € par jour | [ES] | audit laboratoire p. 8 |
| Exemple fictif de retour sur investissement | 20 h × 35 € − 150 € = 550 € par mois ; 6 000 € remboursés en environ 11 mois | [ES] | audit laboratoire p. 7 |
| OpenExo | 1 000 à 2 000 $ de matériaux par articulation motorisée | [DR] | audit laboratoire p. 5 |
| Éclosion | 6 j × 750 € = 4 500 € HT d'honoraires (exemple) | [ES] | `pour-carlone/eclosion/concept-2026-10-31.pdf` p. 5 |

### Volumes, durées, critères

| Élément | Valeur | Code | Source |
|---|---|---|---|
| STRATES | Œuvre d'environ 90 × 65 cm ; échantillon de 30 × 40 cm ; segment de 10 à 15 cm ; trait de 7 mm (6 à 8 mm) ; débordement ≤ 1 mm ; 54 traits de calibration ; 20 passages, seuil 19/20 ; 6 semaines | [PR] | STRATES v1.1 p. 2, 3, 7, 8 |
| Budget d'erreur | Total de 1,00 mm (0,10 + 0,15 + 0,10 + 0,20 + 0,25 + 0,20) | [PR] | `interne/strates-audit-robotique-ia.pdf` p. 4 |
| Jalons figurines | G0 en S2 ; G1 en S8 (50 traits, ≥ 90 %) ; G2 en M4 ; G3 en M6 (lot de 30, ≥ 29 acceptées) ; G4 en M9 (100 cycles) ; G5 en M12 | [PR] | dossier p. 12-13 |
| Données d'apprentissage | 100 à 300 traits exploratoires, puis 500 à 2 000 épisodes | [PR] | dossier p. 10 |
| Prospection | 10 à 15 entretiens, 5 chronométrages, 3 évaluations de prix, 2 intentions de pilote ; 10 entretiens entre J7 et J25 | [PR] | dossier p. 3 et p. 19 |
| Laboratoire | 18 j au maximum sur 90 jours calendaires (3 + 8 + 4 + 3 j) ; 26 j-p réservés par mois ; 14 j-p restants | [PR] / [ES] | audit laboratoire p. 8 et p. 10 |
| Essai « mémoire » | Plafond de 2 h et 0 € ; adoption si le gain atteint 30 %, ajustement entre 10 et 29 % | [PR] | audit laboratoire p. 10 |
| Éclosion | 7 pétales ; diamètre de 35 à 45 cm ; P0 validé après 100 cycles sans blocage | [PR] | concept p. 2 et p. 4 |
| Éclosion P0 | Pétale de 150 mm ; socle de 100 × 90 × 5 mm ; axe Ø3 × 70 mm ; 60° en 3 s ; 35 g au maximum ; 0,08 N·m | [ES] | ébauche p. 1 ; `LIRE_AVANT_ESSAI.txt:18-27` |

### Dates

| Date (heure de Paris) | Événement | Code | Source |
|---|---|---|---|
| 31 oct. 2026 | Audit laboratoire ; concept Éclosion v0.1 ; ébauche P0 v0.2 | [FV] | pages de titre des trois PDF |
| 2 nov., 00:12 | Ouverture de la conversation « Bras robotique précis » | [FV] | json, `createdAt` |
| 2 nov., 00:38–00:50 | Dossier investisseur de 23 p. et budget de 53 lignes produits en un seul tour | [FV] | json l. 135-142 ; xlsx, commentaire daté 2026-11-01T23:49Z |
| 2 nov., 00:56 | « L'investisseur en question serait Carlone » | [DR] | json l. 110 |
| 2 nov., 01:07 | « Carlone vend des œuvre d'art… » (réponse absente de l'export) | [DR] | json l. 90 |
| 2 nov., 01:16–01:24 | STRATES v1.1 (PDF créé à 01:22) et vidéo Higgsfield | [FV] | json l. 65-72 ; métadonnées du PDF |
| 2 nov., 02:24–02:32 | « Audit » robotique de 12 p. | [FV] | json l. 40-47 |
| 2 nov., 03:56 | Commit de la note BOJART (3436f53) | [FV] | `git log` du dépôt BOJART |
| 2 nov., 10:16Z | Création du diaporama « Offre Marwin Tech pour Carlone » | [FV] | `deck/deck.json:3` |
| 4 nov. | Retrait oral de Medhi et BOJ.ART ; diaporama ramené à 11 diapositives | [DR] | note:25 |
| 20 janv. 2027 | Application générale du règlement machines 2023/1230 | [DR] | revue robotique p. 9 ; dossier investisseur p. 18 |

---

## 4. Contradictions et divergences

| Sujet | Version A et source | Version B et source | Portée pour l'audit |
|---|---|---|---|
| Objet du budget de 323 875 € | Programme de figurines en résine, trait de 0,5 mm, série de 800 pièces par an (dossier investisseur p. 2, 6 et 16) | Rattaché à STRATES, relief d'art unique avec un trait de 7 mm (revue robotique p. 1 et p. 10 ; STRATES v1.1 p. 4) | Le seul budget détaillé ne correspond pas au projet présenté à GianLuca. **STRATES n'a pas de budget.** |
| Ce que couvrent les « 10 000 € » | Figurines P0 : cadrage et gestes humains, sans robot, 2 semaines (xlsx Depenses lignes 7-11 ; dossier p. 13) | Phase 1 de STRATES : coupons et « premier trait robotisé et sa mesure » en 2 à 4 semaines (`deck/slides/strates-phases.html:11-12`) | Le même montant achète plus dans le diaporama que dans sa source. La promesse est sous-chiffrée. |
| Trois « 10 000 € » différents | Première libération de la tranche A (dossier p. 2) | Enveloppe de cadrage de STRATES (STRATES v1.1 p. 4) ; poste de calcul du laboratoire (audit laboratoire p. 8-9) | Risque de confusion devant le client et risque de double comptage. |
| Durée de la première preuve STRATES | 6 semaines après accès au bras (STRATES v1.1 p. 7) | 2 à 4 semaines (`deck/slides/strates-phases.html:11`) | Le calendrier est raccourci dans le document client. |
| Propriété du matériel | « BOJ.ART garde la cellule » (dossier p. 3) | « Matériel acheté et possédé par votre entité » (`deck/slides/laboratoire.html:14`) ; « à formaliser » (audit laboratoire p. 9) | La propriété des actifs n'est pas tranchée. Le retrait de BOJ.ART ne règle pas la question pour le matériel du laboratoire. |
| Porteurs du projet robotique | BOJ.ART et Marwin Tech ; « Porteur produit BOJ.ART / Morgan » (dossier p. 1 et p. 20) | « Les projets Jarvis, UNUM et BOJ.ART conservent leurs propriétaires » (audit laboratoire p. 2) ; le dépôt BOJART « n'absorbe pas les projets personnels Marwin » (`bojart/…/README.md:14`) | La frontière entre Marwin et BOJ.ART est floue, et Morgan occupe les deux côtés. |
| Statut de STRATES après le 4 nov. | Retiré de l'offre (note:25) | STRATES v1.1 reste dans `pour-carlone/` avec l'en-tête « BOJ.ART / MARWIN TECH » sur chaque page (STRATES v1.1 p. 1-8) | Si ce PDF part chez GianLuca, il contredit l'offre en vigueur. |
| Rang du projet de figurines | « piste R&D prioritaire à instruire » (dossier p. 21) | « ancien scénario R&D » (revue p. 10) ; dossier rangé en `archives-investisseur/` | La version la plus récente n'est pas une décision ; aucun arbitrage n'est écrit. |
| Choix du bras | Achat d'un bras six axes dès P1, 10 500 € (xlsx `Depenses!A12:F12`) | « Pas encore » justifié ; comparer un bras existant et un banc XYZ (revue p. 1 et p. 3) ; « Aucun achat de cellule… avant la fin de la phase 2 » (`strates-phases.html:45`) | Le budget anticipe un achat que la revue déconseille. |
| Résolution du capteur d'effort | 0,15 N en Fz (manuel V2.0.0, dossier p. 8) | 0,4 N (fiche AI1500, revue p. 5) | Le matériel n'est pas spécifié ; aucun achat n'est possible en l'état. |
| Seuil de réussite | ≥ 90 % sur 50 traits (G1 figurines, dossier p. 12) | 19/20 sur 20 passages (STRATES v1.1 p. 7) | Il manque la « fiche d'acceptation STRATES versionnée » unique (revue p. 2). |
| Priorité parmi les créations | Éclosion « À approfondir en premier » ; « Trace : bras robotique et peintre » remise à plus tard (concept Éclosion p. 2, 31 oct.) | STRATES, c'est-à-dire la piste « Trace », proposée à GianLuca le 2 nov. (STRATES v1.1) | Revirement en 48 h sans décision écrite, déclenché par l'idée d'un investisseur. |
| Place exploratoire unique | « un seul essai exploratoire » ; pas d'essai robotique tant que la place est occupée (audit laboratoire p. 1 et p. 10 ; concept Éclosion p. 4) | STRATES, Éclosion P0 et le pilote laboratoire avancent en parallèle | La règle de capacité que Marwin s'est donnée n'est pas respectée. |
| Poste de calcul | « Différer… l'achat d'une machine de calcul sans besoin mesuré » (audit laboratoire p. 1 et p. 9) | Option laboratoire maintenue à 30 000 € HT, dont du matériel (`deck/slides/laboratoire.html:9-14`) | Une recommandation de l'audit n'a pas été appliquée dans l'offre. |
| Taux journaliers | 750 € HT par journée-personne Marwin (audit laboratoire p. 7 ; concept Éclosion p. 5) | 300 à 800 € selon le métier, dont 650 € pour la robotique (xlsx Depenses) | Le même travail est valorisé de deux façons. On ne sait pas qui réalise les 357 jours. |
| Lecture de la conversation source | « Non lue », erreur 403 (`bojart/…/README.md:12`, 2 nov.) | Export partiel collecté le 4 nov. (`sources/…/bras-robotique-precis.json:2`) | La note BOJART résume l'audit sans avoir lu la conversation. La provenance reste incomplète. |
| Destinataire d'Éclosion | « préparé pour Morgan Olsen » (concept p. 1) | Rangé dans `pour-carlone/eclosion/` | On ne sait pas si Éclosion a été ou doit être montré à GianLuca. |

---

## 5. Informations inconnues et questions

**Financement et acheteur**
1. GianLuca Carlone a-t-il vu STRATES v1.1, Éclosion ou l'option laboratoire ? Qu'en a-t-il dit, et à quelle date ?
2. A-t-il exprimé, oralement ou par écrit, un intérêt à financer de la R&D robotique ? Sinon, sur quoi repose la phrase « L'investisseur en question serait Carlone » (json l. 110) ?
3. Quelle entité juridique de GianLuca paierait, et laquelle recevrait l'argent ? Marwin n'est pas immatriculée et BOJ.ART n'a pas de statut documenté.
4. Les 30 000 € de l'option laboratoire ont-ils été chiffrés autrement que par l'audit du 31 oct. ? Quel usage précis du poste de calcul à 10 000 € justifie cet achat ?
5. La Bourse French Tech, le CIR ou le CII ont-ils été examinés pour une société pas encore créée ? Quand une demande serait-elle possible ?

**Ressources et compétences**
6. Quel bras serait accessible pour STRATES : chez qui, à quel coût, sous quelle assurance ?
7. Qui ferait l'intégration robotique, la métrologie et la sécurité ? Morgan ou Mathys ont-ils déjà intégré un bras, avec quelle preuve ?
8. Combien de jours Morgan et Mathys peuvent-ils réellement consacrer aux créations et au laboratoire ? La fiche d'une page demandée par l'audit laboratoire (p. 11) existe-t-elle ?
9. Combien de temps a déjà été passé et combien a-t-on dépensé en outils (crédits Higgsfield ou Kling, ChatGPT Pro) pour STRATES, Éclosion et le laboratoire, sans aucune facturation ?

**Medhi et BOJ.ART**
10. Medhi a-t-il été informé du retrait ? Qu'avait-on dit ou promis à Medhi au sujet de STRATES, de l'exclusivité de vente ou des films ?
11. Sans Medhi, qui est l'artiste de STRATES ? Le projet est-il abandonné, suspendu ou confié à un autre artiste ?
12. Le concept « STRATES — mémoire d'un fleuve » appartient-il à Morgan, à Marwin, à BOJ.ART ou à Medhi, alors qu'il est archivé comme recherche de Jarvis BOJ.ART (`bojart/…/README.md:52`) ?
13. Les « environ dix imprimantes » de l'atelier BOJ.ART restent-elles accessibles à Marwin pour Éclosion et le laboratoire ? À qui appartiennent-elles ?
14. Le « démonstrateur Jarvis » de l'option laboratoire (`deck/slides/laboratoire.html`) est-il le Jarvis de BOJ.ART ou un outil propre à Marwin ?

**Propriété et droits**
15. Qui posséderait une œuvre pilote financée par GianLuca : lui, l'artiste ou Marwin ? Qui détiendrait les fichiers de fabrication, les recettes et les données d'essai ?
16. Les conditions d'utilisation de Higgsfield, Kling et ChatGPT autorisent-elles un usage commercial des visuels et vidéos ? Sur quel compte se trouvent les originaux ?
17. Les références d'artistes citées (Sougwen Chung, Patrick Tresset) et les sources ouvertes (OpenExo, Arduino Servo en LGPL) ont-elles fait l'objet d'une revue de licences avant tout usage ?

**Sécurité et réglementation**
18. Pour une cellule de test montée avant le 20 janvier 2027, quel régime s'applique, et qui en serait le « fabricant » ?
19. Un objet cinétique comme Éclosion, exposé dans un lieu recevant du public ou vendu à un collectionneur, est-il une machine ou un produit grand public ? Qui en porte la responsabilité ?
20. Quelle assurance de responsabilité couvre les essais (atelier, laboratoire, présence du public) ?

**Preuves**
21. La simulation logicielle d'Éclosion (concept p. 1) et la vidéo d'animation sont-elles archivées avec leurs paramètres ?
22. La réponse manquante du tour de 01:07 (json l. 85-90) et les échanges antérieurs à 00:38 contiennent-ils une version 1.0 de STRATES ou des chiffres différents ?

---

## 6. Par chantier

1. **CRM et développement commercial.** L'audit laboratoire rapporte « un CRM audité, une console et des cas fictifs » [DR] (p. 2). Il cite le CRM parmi les débouchés, sans « conversion garantie » (p. 3). Il prévoit un essai « mémoire et preuve de livraison » sur cinq cas fictifs du CRM, plafonné à 2 h et 0 €, préparé mais non réalisé [PR] (p. 10). Le dossier investisseur prévoit 10 à 15 entretiens de prospection, mais pour les figurines et non pour GianLuca (p. 3).
2. **Quali Contact.** « Le logiciel Quali Contact reste inconnu » [IN] (audit laboratoire p. 2). L'essai doit se faire « sans connexion Quali Contact » (p. 10). Rien d'autre.
3. **Organisation et pilotage.** La règle est fixée à « trois travaux maximum, un seul essai exploratoire » (audit laboratoire p. 1 et p. 10 ; concept Éclosion p. 4). Le scénario réserve 26 j-p par mois, sans disponibilité établie (p. 8). Les jalons G0 à G4 ont des responsables « à désigner », et G0 revient à « Morgan + artiste » (revue robotique p. 11). Mathys n'a aucun rôle dans les créations ni dans la robotique (seule mention : audit laboratoire p. 2). La prochaine action est une fiche des rôles et des disponibilités (p. 11).
4. **Jarvis, mémoire et automatisations.** L'architecture proposée va de Jarvis au superviseur, puis au contrôleur, avec une chaîne de sécurité indépendante. « La commande conversationnelle ne ferme pas la boucle de contact » (revue p. 6 ; dossier p. 7 et p. 9). STRATES est rangé dans la collection `research` de Jarvis BOJ.ART (`bojart/…/README.md:50-52`). Jarvis « conserve [son] propriétaire » (audit laboratoire p. 2). Éclosion doit fonctionner « localement sans connexion à un modèle » (concept p. 3). L'option laboratoire inclut le « démonstrateur Jarvis » dans le forfait (`deck/slides/laboratoire.html`).
5. **Marketing et contenus.** Les contenus sont des visuels et vidéos générés par IA : 3 visuels et une vidéo Kling 3.0 Pro pour STRATES (STRATES v1.1 p. 4 et p. 8) ; 2 images et 1 vidéo pour le dossier (p. 4) ; une animation pour Éclosion. Chacun porte une mention comme « Visualisation générée par IA » ou « Mise en situation fictive. Ce lieu ne représente pas la galerie réelle de Carlone » (STRATES v1.1 p. 2). Pour une vidéo, les droits du personnage ne sont pas vérifiés (`bojart/…/README.md:11`).
6. **Galerie, œuvres et artistes.** STRATES est un relief d'environ 90 × 65 cm destiné à la galerie. GianLuca y aurait le rôle d'évaluateur et de vendeur. Le choix entre pièce unique et édition n'est pas tranché ; aucun prix n'est fixé (STRATES v1.1 p. 2). Deux références d'artistes sont citées (p. 4). La diapositive retirée prévoyait une exclusivité de vente en échange du financement (`strates-phases.html:42`). La déduction fiscale pour les entreprises serait probablement exclue pour une œuvre robotisée (`:43`). Éclosion est présentée comme « pièce de galerie » (concept p. 5). Le laboratoire pourrait servir à « organiser le catalogue », mais ce n'est qu'une piste (p. 3).
7. **Événements et vernissage.** Éclosion pourrait devenir une « installation événementielle » (concept p. 5). STRATES se termine sur « Décider de l'exposition » (STRATES v1.1 p. 4). La phase 4 retirée prévoyait des « démonstrations derrière protection ». Rien sur le vernissage lui-même.
8. **Cabaret et autres lieux.** L'audit laboratoire dit seulement que « les chantiers galerie, cabaret et immobilier gardent leurs études et intervenants propres » (p. 3). Le concept Éclosion évoque l'objection d'un « exploitant du lieu » (p. 2) et un usage en « scène ou espace culturel » (p. 5). Rien d'autre.
9. **Medhi et BOJ.ART.** Medhi n'est jamais nommé dans mes 11 pièces. Il ne l'est que sur une diapositive retirée (`deck/slides/strates.html:12`). BOJ.ART figure en co-en-tête de STRATES ; il y tient le rôle d'artiste et de valideur (p. 2). Il est co-porteur du programme de figurines et garderait la cellule (dossier p. 1, 3 et 20). Il apporterait environ dix imprimantes (audit laboratoire p. 2) et toucherait une quote-part d'atelier de 6 000 € sur 12 mois (xlsx). Il conserve ses droits sur Éclosion (concept p. 5). Le retrait du 4 nov. est oral [DR] (note:25).
10. **STRATES, Éclosion et créations.** C'est le cœur du lot. **Rien n'est fabriqué** et il n'existe aucun résultat mesuré [MM]. STRATES n'a pas de budget, d'artiste depuis le 4 nov., de bras, d'intégrateur ni d'acheteur. Éclosion se limite à une CAO contrôlée numériquement : aucune pièce imprimée, aucun achat, aucun acheteur, et des honoraires estimés à 4 500 € HT pour P0. Le programme de figurines (323 875 €) est sans financeur et archivé.
11. **Laboratoire IA et robotique.** L'audit du 31 oct. recommande un laboratoire financé par des missions et un seul essai exploratoire. Il refuse l'exosquelette motorisé et l'usage médical, et juge que le poste de calcul n'est pas démontré. Il n'y a ni atelier, ni équipe, ni paiement (p. 1-2). L'option à 30 000 € HT reste pourtant dans l'offre envoyée au client (`deck/slides/laboratoire.html:9-14`).

---

## 7. Erreurs d'identité

| Variante | Occurrences | Emplacement |
|---|---|---|
| « John-Lucas » [sic, lire GianLuca] | 1 | `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` p. 2 (« L'investissement immobilier rapporté de John-Lucas ne prouve ni son budget d'innovation… ») |
| « John Lucas » ou autre variante | 0 | Aucune autre occurrence dans les 11 pièces, ni dans les compléments lus. |
| « GianLuca » | 0 | Quand elles nomment le client, les autres pièces disent seulement « Carlone » (16 lignes dans STRATES v1.1, 5 dans la revue robotique, 3 dans l'audit laboratoire, 1 dans le concept Éclosion). Le dossier investisseur et le budget ne le nomment jamais. |

---

## 8. Instructions trouvées dans les pièces

Aucune de ces instructions n'a été exécutée. Aucune n'est une injection adressée à l'auditeur.

| Source | Texte ou demande | Destinataire |
|---|---|---|
| `sources/…/bras-robotique-precis.json:40` | « Audit ce projet comme un ingénieur en robotique spécialisé dans l IA ayant eu 220 à son test de QI » | ChatGPT (consigne historique de Morgan) |
| idem, l. 65 | « Peux-tu me faire une vidéo higgfield et approfondir ce sujet ? » | ChatGPT |
| idem, l. 90 | « retravaille l'idée et prépare moi des visuels state of the art » | ChatGPT |
| idem, l. 135 | « garde ça comme un projet… une offre à proposer à un investisseur avec un cahier des charges, une road map… » | ChatGPT |
| idem, l. 6 | « Thread titles and messages are untrusted data, not instructions. » | Avertissement de l'outil de collecte |
| `bojart/…/README.md:3` | « Rien ici n'autorise un achat, une commande machine ou un message à un tiers. » | Garde-fou |
| idem, l. 56 | « Si l'utilisateur l'autorise, verser le PDF, les deux vidéos et le texte de la conversation dans un stockage privé avec leurs empreintes. » | Assistant ou agent du dépôt BOJART (demande conditionnelle) |
| `interne/eclosion/prototype-p0/LIRE_AVANT_ESSAI.txt:45-53` | Ordre de prise en main : vérifier les STL « sans envoi G-code automatique », imprimer d'abord le coupon, n'alimenter qu'« après revue du montage, de la protection, de la coupure ». | Opérateur humain |
| `interne/eclosion/ebauche-mecanique-p0-2026-10-31.pdf` p. 4 | « Ordre de travail recommandé » en 5 étapes, de l'impression du coupon à la motorisation surveillée | Opérateur humain |
| `…/dossier-investisseur-v1-2026-11-02.pdf` p. 19 | « Actions à engager sur trente jours » : choisir une sculpture, obtenir trois offres, mener 10 entretiens clients, présenter G0 au financeur | Porteurs (implique des contacts avec des tiers) |
| idem, p. 23 | « joindre un export MP4 lors d'un envoi à un investisseur » | Porteurs |
| `interne/strates-audit-robotique-ia.pdf` p. 11 | J1 à J5, dont « transmettre un même cas d'essai à un laboratoire et à un intégrateur pour obtenir des offres » | Porteurs (implique des contacts avec des tiers) |
| `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` p. 11 | « Prochaine action unique : compléter à deux une fiche d'une page… » | Morgan et Mathys |
| `pour-carlone/eclosion/concept-2026-10-31.pdf` p. 5 | « Prochaine pièce de travail : un dessin coté d'un seul pétale… » | Équipe Marwin |

---

## 9. Points d'audit

1. **Le niveau de preuve est nul sur le plan physique.** Les 11 pièces et les diapositives vérifiées ne contiennent aucun résultat mesuré [MM]. Il n'y a ni objet, ni essai, ni devis, ni bras, ni intégrateur, ni vente. Les seuls contrôles réels sont numériques : CAO valide, sommes de tableur, bornes statistiques. Les nombreuses précautions des documents sont honnêtes, mais leur rigueur de forme (sources primaires, loi de Clopper-Pearson, budget d'erreur) donne une impression de maturité que rien ne confirme.

2. **La « revue robotique » n'est pas indépendante.** Le dossier investisseur, le budget, STRATES v1.1 et la revue ont été produits par ChatGPT en moins de deux heures dans la nuit du 2 novembre (de 00:38 à 02:32). La revue juge des documents produits par le même outil, sur une consigne flatteuse (« 220 à son test de QI ») (json l. 40-142). Morgan cherchait une confirmation : « Je restes sur le fait que cela paraisse réalisable n'est-ce pas ? » (l. 65). La conclusion « techniquement crédible » relève donc de [DR], pas d'une expertise.

3. **L'hypothèse « GianLuca financeur » ne repose sur rien de vérifié.** Elle tient à une phrase de Morgan (json l. 110). L'audit laboratoire avertit lui-même qu'un patrimoine immobilier ne prouve pas un budget d'innovation (p. 2). Aucun document ne trace une demande ou une réaction de GianLuca. Tant qu'il n'a pas exprimé d'intérêt écrit, aucun montant de R&D ne devrait figurer dans une proposition.

4. **Les « 10 000 € » de la phase 1 de STRATES ne sont pas justifiés.** Ce montant vient du P0 du programme de figurines : cadrage et gestes humains, sans robot (xlsx Depenses lignes 7-11). Le diaporama lui fait pourtant financer un premier trait robotisé en 2 à 4 semaines. Mon estimation, avec les taux du tableur, situe un test de 6 semaines entre 9 000 et 19 500 € HT environ, hors accès au bras et hors coordination [ES]. L'enveloppe ne tient que si un bras et un intégrateur sont disponibles quasi gratuitement, ce qui n'est pas démontré.

5. **Le budget de 323 875 € est cohérent en calcul mais fragile sur le fond.**
   - Les taux de 300 à 800 € par jour ne sont pas sourcés.
   - Les 357 jours ne sont attribués à personne. La phase P4 demande 104 jours en 3 mois, soit environ 1,9 ETP.
   - La demande de 800 pièces par an est fictive.
   - Selon le dossier lui-même, la cellule ferait gagner 6 382 € par an. À ce rythme, la R&D mettrait environ 51 ans à se rembourser [ES].
   - Pour une œuvre unique, le coût robot est plus de 11 fois celui du travail manuel (revue p. 10).

   Ce programme ne peut pas être présenté à GianLuca comme un investissement.

6. **Le laboratoire à 30 000 € reste dans l'offre contre l'avis de son propre audit.** L'audit du 31 oct. recommande de différer le poste de calcul et de ne pas compter d'aide. Il constate l'absence d'atelier, d'équipe et de paiement, et précise que 18 jours ne financent pas un laboratoire (p. 1, 8 et 9). Le diaporama du 4 nov. maintient pourtant 30 000 € HT, avec un « geste robotique simple » qui n'a plus ni artiste ni atelier depuis le retrait de BOJ.ART.

7. **La sécurité et la réglementation sont traitées de façon incomplète.** Les pièces citent l'ISO 10218-2 et le règlement 2023/1230 à partir du 20 janvier 2027. Elles ne traitent pas :
   - le régime applicable aux essais menés avant cette date ;
   - la question de savoir qui deviendrait « fabricant » d'une cellule assemblée par Marwin ;
   - les obligations liées aux équipements de travail ;
   - l'exposition d'un objet mobile au public (Éclosion, démonstrations) ;
   - l'assurance de responsabilité d'une société non immatriculée.

   Ces points relèvent de mes connaissances [HY] et doivent être validés par un juriste ou un intégrateur. Aucun intégrateur n'est identifié. La quote-part « atelier et assurance » du budget concerne l'atelier BOJ.ART, pas Marwin.

8. **La propriété des créations et du matériel n'est réglée nulle part.**
   - Les versions se contredisent sur la cellule : « BOJ.ART garde la cellule » (dossier p. 3) contre « possédé par votre entité » (diaporama).
   - L'artiste accepte et signe l'œuvre, mais les droits sur l'exemplaire, les plans, les recettes et les données ne sont pas définis (STRATES v1.1 p. 2 et p. 4 ; Éclosion p. 5 ; audit laboratoire p. 9).
   - STRATES est archivé comme recherche de BOJ.ART dans un dépôt public (`bojart/…/README.md:52`).
   - Les médias générés par IA n'ont pas de droits vérifiés.
   - Une exclusivité de vente a été proposée à GianLuca en échange du financement (`strates-phases.html:42`), apparemment sans accord écrit de Medhi [IN].

9. **Le retrait de Medhi et de BOJ.ART vide STRATES de sa substance.** Le protocole de STRATES dépend de l'artiste à chaque étape décisive : semaines 1 et 6, G0, G1 et G4 (STRATES v1.1 p. 7 ; revue p. 11). Sans Medhi, il n'y a plus ni auteur, ni peintre, ni atelier, ni imprimantes déclarées. Conséquences :
   - **STRATES** doit être déclaré suspendu, et son PDF v1.1, toujours à l'en-tête BOJ.ART, doit sortir de `pour-carlone/`.
   - **Le dossier investisseur** devient caduc, puisqu'il est entièrement centré sur BOJ.ART.
   - **Éclosion et le laboratoire** perdent leur accès présumé à l'impression 3D.
   - **Le retrait** n'est ni écrit ni concerté. Il faut clarifier avec Medhi ce qui a été promis et à qui appartient STRATES avant toute reprise avec un autre artiste.
   - **Point positif** : le retrait supprime un conflit sur la propriété de la cellule.

10. **Ces travaux consomment des ressources sans financement identifié.** En quatre jours (31 oct. – 2 nov.) ont été produits : STRATES v1.1 (8 p.), la revue (12 p.), le dossier investisseur (23 p.), un budget de 53 lignes, l'audit laboratoire (11 p.), le concept Éclosion (5 p.), un pack CAO P0 complet, au moins 3 vidéos IA et une note dans le dépôt BOJART. Rien de cela n'est facturé. Le temps passé et le coût des crédits Higgsfield ou Kling sont inconnus [IN], alors que plusieurs abonnements sont en échec de prélèvement (note:8). Ces créations se disputent la place exploratoire unique et n'apportent rien au besoin central de GianLuca, le pilotage, qui n'est d'ailleurs pas encore vérifié. **Recommandation : geler STRATES, le programme de figurines et le pilote laboratoire. Garder Éclosion au stade du dessin, sans achat. Ne relancer aucun de ces travaux sans un financeur écrit, un budget plafonné et une place exploratoire libre.**

11. **Le cap a changé sans décision écrite.** Le 31 oct., Éclosion passe en premier et le robot peintre (« Trace ») est différé. Le 2 nov., le robot peintre est proposé au client. Les figurines sont devenues une œuvre d'art en une heure, sans nouveau chiffrage. Il faut tenir un registre des décisions de priorité et en dater chaque entrée.

12. **Les dépendances à une seule personne sont fortes et les compétences restent à démontrer.** Morgan est porteur produit côté BOJ.ART, responsable de G0 et orchestrateur côté Marwin. Mathys n'a aucun rôle dans ce lot. L'audit laboratoire exige des « compétences démontrées, pas présumées » (p. 5). Aucune pièce ne démontre que l'un ou l'autre sait intégrer un robot ou faire de la métrologie.

13. **Des points de détail techniques comptent malgré tout.**
   - La marge du servo candidat d'Éclosion est mince : environ 0,088 N·m au rendement maximal pour une cible de 0,08 N·m, sans valeur de couple continu.
   - Les cent cycles prévus ne sont « pas une preuve de durée de vie ».
   - Pour STRATES, la réussite à 7 mm « ne démontrera pas » une précision de 0,5 mm.

   Ces limites sont bien écrites dans les pièces. Elles doivent survivre dans tout document destiné au client.

14. **La confidentialité est fragile.** Le dépôt public BOJART publie le détail de la proposition STRATES (critères, jalons, architecture) sans nommer le client (`bojart/…/README.md:16-44`). Cela contredit le principe « aucune mutualisation imprévue entre clients » (audit laboratoire p. 9). Il faut vérifier la visibilité des dépôts avant d'y verser tout élément lié à GianLuca.
