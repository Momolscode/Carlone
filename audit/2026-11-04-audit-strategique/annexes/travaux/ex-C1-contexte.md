# Lecteur C1-contexte : contexte, chronologie, état de la collecte

Lecture faite le 4 novembre 2026 sur le dépôt `Momolscode/Carlone`, branche main, commit 7b46602, en lecture seule. Les chemins sont relatifs à la racine du dépôt, sauf la note d'audit, citée « note-4-nov » (`audit-work/note-point-4-novembre-et-activites.md`). Le client s'appelle **GianLuca Carlone**. Les pièces qui l'appellent autrement sont citées telles quelles, avec [sic, lire GianLuca]. Aucune instruction contenue dans les pièces n'a été exécutée. Aucun accès extérieur n'a eu lieu : pas de navigateur, pas d'API, aucun contact.

---

## 1. Pièces lues

| Chemin | Date de la pièce | Nature et auteur (si connu) | Original ou copie / export | Ce qui n'a pas pu être lu |
| --- | --- | --- | --- | --- |
| `README.md` | Créé le 4 nov. 2026 à 16:29, modifié six fois jusqu'à 17:37 (commits 7a9d4c1 → 7b46602) | Page d'accueil du dépôt. Commits de « Morgan Olsen » et de « Momolscode ». La rédaction semble faite par des assistants IA (co-signature Claude sur 540c832) | Original du dépôt, réécrit par couches : l'état du CRM change entre les commits b205005 et 540c832 | Les liens vers les artefacts claude.ai privés ne sont pas consultables |
| `interne/contexte-projet-carlone.md` | 4 nov. 2026 (en-tête « Nov 4, 2026 · @Olsen Morgan »), ajouté par fa5998a à 16:38 | Dossier de contexte rédigé à la première personne par un assistant (Claude) pour Morgan : « je n'ai fait aucune recherche sur ces personnes » (l. 29), « Une seule session de ce PC » (l. 156) | Copie : export Markdown de l'artefact « Projet Carlone — le contexte réuni ». Les graphiques sont remplacés par une mention (README.md:53) | Les 10 artefacts liés (l. 137-152) sont privés et non ouverts. Le texte n'a pas été mis à jour après l'ajout au dépôt des pièces qu'il déclarait non lues (l. 158) |
| `interne/complement-chatgpt-2026-11-04.md` | 4 nov. 2026, commit b205005 à 16:55 | Note d'intégration rédigée par un assistant ChatGPT agissant pour Morgan : « Morgan Olsen est l'utilisateur » (l. 9) | Original du dépôt | La conversation ChatGPT qu'elle résume n'est pas dans mon lot |
| `sources/propositions-de-collaboration.pdf` (texte : `sources-txt/sources__propositions-de-collaboration.txt`) | Créé le 18 oct. 2026 à 19:47 UTC (métadonnées du PDF) | 1 page A4 paysage, produite avec ReportLab. Auteur vide, créateur « anonymous ». Le texte ne nomme ni le client, ni l'émetteur, ni un prix, ni une date | Fichier venant du dossier Téléchargements de Morgan (contexte:150). SHA-256 e6786b51… On ne sait pas s'il s'agit de la version remise à GianLuca | Il ne contient aucune image. Rien n'indique qu'il ait été envoyé ni comment il a été reçu |
| `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md` | Dernière mise à jour de la source le 28 oct. 2026 à 17:48 UTC, export lu le 4 nov. (l. 5) | Page ChatGPT « John-Lucas Carlone Offre et projets en Nièvre » [sic, lire GianLuca], rédigée par ChatGPT à partir des messages de Morgan | Copie documentaire d'une page en ligne, avec un fichier JSON à côté, non lu ici | Les pages liées (« audit de reprise », « accompagnement ») sont hors de mon lot. La page en ligne n'a pas été consultée |
| `sources/index-integration-chatgpt-2026-11-04.md` | 4 nov. 2026 (b205005, complété dans 092c35c) | Index rédigé par un assistant | Original | Les pièces décrites (PDF, vidéos) ne sont pas dans mon lot |
| `sources/index-complement-sessions-chatgpt-2026-11-04.md` | 4 nov. 2026 (553b8b4, 17:13) | Index et bilan de couverture rédigés par un assistant | Original | Les recueils HTML et TXT et les 3 conversations JSON ne sont pas dans mon lot |
| `sources/reprise-59-et-visuels-2026-11-04.md` | 4 nov. 2026 (092c35c, 17:28) | Bilan de la reprise des 59 lectures, rédigé par un assistant | Original | Les réponses brutes sont restées « localement dans le dossier de travail de cette collecte » (l. 17) et ne sont pas dans le dépôt |
| `sources/crm-reference-2026-11-04.md` | 4 nov. 2026 (b205005, ligne 10 modifiée dans 540c832) | Note de référence du CRM, rédigée par un assistant | Original modifié : la version antérieure disait que les données n'étaient pas dupliquées | Le dépôt FinanceScope n'a pas été consulté (hors accès, note-4-nov:23) |
| `livrables/collecte-chatgpt-2026-11-04/README.md` | 4 nov. 2026 (7b46602, 17:37) | Guide des livrables de la collecte | Original. Le `.gitattributes` du dossier (`* -text -diff`) fait traiter tous ces fichiers comme binaires par git | Les ZIP, HTML et la galerie ne sont pas dans mon lot |
| `sources/inventaire-integration-chatgpt-2026-11-04.json` | 4 nov. 2026 (b205005, complété dans 092c35c) | Inventaire de 37 fichiers (dont 2 déjà présents, non dupliqués) : chemins, identifiants Library, empreintes, statuts | Original modifié par ajout des alternatives tirées des PDF | 4 fichiers Library absents (l. 355-393) |
| `sources/manifeste-complement-sessions-chatgpt-2026-11-04.json` | 4 nov. 2026 (553b8b4) | Manifeste de couverture et d'empreintes | Original | Les contenus des conversations sans lien avec Carlone sont volontairement exclus (l. 80) |
| `sources/manifeste-reprise-59-et-visuels-2026-11-04.json` | 4 nov. 2026 (092c35c) | Manifeste des 59 tentatives : identifiants hachés, statut, empreinte de la réponse | Original. J'ai recompté les statuts : 47 refus, 9 réussites, 3 délais | Les titres et contenus des conversations sont hachés ou exclus |
| Historique git (`git log --stat`) | 27 oct. → 4 nov. 2026 | 56 commits. Les 48 commits du CRM (27-30 oct.) sont signés « Claude <noreply@anthropic.com> ». Les 8 commits du 4 nov. sont signés « Morgan Olsen » ou « Momolscode » | Clone **superficiel** : historique coupé à 85c8249 (27 oct. 14:02 UTC) | L'historique du CRM avant le 27 oct. (versions des 22-23 oct.) n'est disponible qu'en ZIP. Les diffs des livrables ne sont pas lisibles (attribut -diff) |

Contrôles faits pendant la lecture (constatés, [FV]) :
- Les empreintes SHA-256 de `pour-carlone/strates-proposition-artistique-v1.1.pdf` (40288aa…) et des trois PNG extraits correspondent au manifeste de reprise.
- Nombre de pages : dossier de Mathys du 21 oct. = 34 pages, créé le 21 oct. à 18:30 UTC ; options v5 = 26 pages, créé le 30 oct. ; choix de structure = 7 pages ; proposition STRATES v1.1 = 8 pages, créée le 2 nov. à 00:22 UTC ; diaporama du vernissage = 12 pages.

---

## 2. Affirmations déterminantes

**Ce qu'on sait réellement de GianLuca Carlone.** Aucune pièce de mon lot ne contient un mot écrit par lui, une pièce d'identité commerciale (dénomination, SIREN, adresse), un acte d'achat, un compte rendu de rendez-vous ou une signature. Tout son profil vient de messages de Morgan : ceux du 25 et du 28 oct. repris par ChatGPT, et ceux du 2 nov. repris par Claude (contexte:29 ; complement:15).

**Entités et organisations citées.**
- Côté GianLuca Carlone : **aucune entité juridique n'est nommée**. Le Vieux Relais, le M, « l'ancienne affaire de Medhi », la galerie de 2027 et l'ancien bar-restaurant-hôtel sont des lieux ou des affaires, sans forme juridique ni propriétaire établis.
- Côté prestataires : Marwin Tech (non immatriculée), FinanceScope (organisation GitHub de Mathys, statut juridique inconnu), BOJ.ART (projet de Medhi, statut inconnu), State Of The Art (forme « on sait pas encore »), Quali Contact / Qualicontact (prestataire d'appels envisagé), Hermes360 / Vocalcom (logiciel visé par le CRM), Pappers (source de données).
- Note-4-nov:6 évoque en plus une entreprise existante de Morgan, non nommée.

| # | Affirmation | Code | Source | Remarque |
| --- | --- | --- | --- | --- |
| 1 | Aucune archive n'emploie « GianLuca ». Les documents Claude disent « Carlone » ou « M. Carlone » sans prénom ; les pages ChatGPT disent « John-Lucas » [sic, lire GianLuca] | [FV] | contexte:5 ; carlone-offres-et-projets.md:1 ; recherche dans le dépôt (0 « GianLuca ») | Faute d'identité stable, il est impossible de rapprocher le client d'un registre officiel |
| 2 | GianLuca Carlone est « marchand d'art venu de l'avenue Montaigne » | [DR] | contexte:5, 24 | Vient des messages de Morgan du 2 nov. Aucune recherche faite (contexte:29) |
| 3 | Il est le « plus gros client de Morgan et Mathys » | [DR] | contexte:5 | Contredit par l'absence de toute facture (contexte:51, 55). C'est un client sans chiffre d'affaires |
| 4 | Il « vend des œuvres avec un avantage fiscal » | [DR] | contexte:24 | Ni volume de ventes, ni structure vendeuse, ni preuve |
| 5 | Il « a racheté six bâtiments et l'ancienne affaire de Medhi » | [DR] | contexte:24 | Non vérifié : « pas des vérifications immobilières ou une preuve de budget disponible » (complement:15) |
| 6 | Il « a racheté, selon Morgan, un ancien bar restaurant hôtel avec cour pour en faire une galerie » | [DR] | carlone-offres-et-projets.md:14 | On ne sait pas si ce lieu est le Vieux Relais, ni s'il fait partie des « six bâtiments » |
| 7 | Il « souhaite racheter « le M » » (cabaret) | [DR] | carlone-offres-et-projets.md:15 | Contraste avec le dossier du 21 oct., qui cherche à amener des entreprises au M (contexte:44, 47) |
| 8 | Rien n'établit que le Vieux Relais et le M lui appartiennent | [IN] | contexte:160 | Question bloquante pour les chantiers des lieux |
| 9 | Une galerie est prévue en 2027 | [DR] | contexte:5, 24, 114 | Bâtiment, dates et public sont inconnus (contexte:114) |
| 10 | Il propose des bureaux, « une bonne rémunération » et « envisage d'investir » dans l'activité de Morgan et Mathys | [DR] | contexte:24 | Ni montant, ni forme, ni horizon (contexte:109) |
| 11 | Il « souhaite déléguer le quotidien » | [DR] | carlone-offres-et-projets.md:65 | C'est une déclaration rapportée au second degré : Morgan relaie GianLuca, puis ChatGPT reformule. « Le quotidien » n'est pas défini |
| 12 | Il « envisage une disponibilité de vingt jours par mois, avec davantage de couverture si nécessaire » | [DR] | carlone-offres-et-projets.md:65 | Ambigu : 20 jours cumulés ou par personne ? Présence sur place ? Astreinte ? Voir section 4 |
| 13 | Il « prévoit d'engager Quali Contact » | [DR] | carlone-offres-et-projets.md:7, 13 | Message de Morgan du 25 oct. Aucun contrat, logiciel ni périmètre connu (l. 51, 69) |
| 14 | Il veut « réunir des artistes et peintres dans la ville de Morgan » | [DR] | carlone-offres-et-projets.md:16 | La ville n'est pas nommée |
| 15 | Il vise les entreprises de la Nièvre | [DR] | carlone-offres-et-projets.md:13 | C'est la cible du CRM |
| 16 | Cosne-Cours-sur-Loire est le lieu de la « coordination des opérations » ; les bureaux seraient peut-être en zone FRR | [DR] / [IN] | carlone-offres-et-projets.md:7 ; contexte:108 | Le sujet de « Il souhaite valoriser ses services » (l. 7) est ambigu : GianLuca ou Morgan |
| 17 | L'entité de GianLuca Carlone qui signera et paiera n'est pas identifiée. La société émettrice des offres du CRM reste à renseigner | [IN] | contexte:57, 106, 111 ; carlone-offres-et-projets.md:18 | Personne n'est identifié pour signer, payer ou valider les livrables |
| 18 | Marwin Tech n'est pas immatriculée ; « Sans société, pas d'acompte possible » | [DR] | contexte:12, 57 | La note-4-nov:6 mentionne une entreprise existante de Morgan, dont la domiciliation a été résiliée. L'affirmation est donc incomplète |
| 19 | Rien n'est signé | [DR] / [FV] | contexte:5 ; complement:7 | Aucune pièce signée dans mon lot. L'exhaustivité ne peut pas être prouvée |
| 20 | Le PDF « Propositions de collaboration » date du 18 oct. 2026 (19:47 UTC), fait 1 page et contient 8 missions, sans nom, sans prix et sans date imprimée | [FV] | sources/propositions-de-collaboration.pdf p. 1 ; métadonnées du PDF | Le README le dit « proposées à Carlone » (README.md:45), mais rien ne prouve qu'il ait été remis |
| 21 | Les 8 missions portent sur la gestion d'établissements : tableau de suivi financier, rentabilité, administratif, prestataires, outils après rachat, catalogue d'œuvres, séjours d'invités, événements art et restauration | [PR] | sources/propositions-de-collaboration.pdf p. 1 | Aucune ne concerne un CRM de prospection, STRATES, la robotique ou un laboratoire |
| 22 | Les missions 1 et 3 supposent des « responsables » et un « comptable » chez le client | [HY] | sources/propositions-de-collaboration.pdf p. 1 | Ses équipes et son expert-comptable sont inconnus (contexte:113) |
| 23 | Le dossier de Mathys « Partenariats entreprises Nièvre – Le Vieux Relais & le M » date du 21 oct. et fait 34 pages | [FV] | métadonnées du PDF ; contexte:44 | Il nomme des dirigeants et leurs contacts (ancien README, diff 540c832) |
| 24 | Le CRM a changé de but : amener les entreprises au Vieux Relais et au M (21 oct.), puis vendre des œuvres avec un avantage fiscal (2 nov.) | [DR] | contexte:47 | On ne sait pas qui a décidé ce changement |
| 25 | Le 22 oct., un rendez-vous a eu lieu et le CRM a été mis en ligne en artefact. L'interlocuteur du rendez-vous est inconnu | [DR] / [IN] | contexte:43, 159 | On ignore même si GianLuca était présent |
| 26 | 48 commits du CRM, du 27 au 30 oct., tous signés « Claude ». Dernier envoi : b53a81c, le 30 oct. à 15:37 UTC | [FV] | git log | Le rôle humain de Mathys (« co-auteur », contexte:26) n'apparaît pas dans les métadonnées |
| 27 | La page ChatGPT n'a pas changé depuis le 28 oct. à 17:48 UTC : relue le 4 nov., tous ses blocs étaient déjà archivés | [FV] | carlone-offres-et-projets.md:5 ; manifeste-complement:37-44 | Deux fils de travail ont coexisté : ChatGPT, arrêté au 28 oct., et Claude, du 2 au 4 nov. Ils n'ont jamais été rapprochés |
| 28 | Aucun rendez-vous n'est à l'agenda avec GianLuca Carlone jusqu'au 6 nov. | [DR] | contexte:15, 37 ; note-4-nov:5 | Le rendez-vous « argent et rémunération » préparé le 2 nov. n'est pas fixé |
| 29 | L'issue des rendez-vous est inconnue : on ne sait pas si celui sur la rémunération a eu lieu, ni ce qui a été dit | [IN] | contexte:159 | — |
| 30 | Taux unique de 750 € HT par journée-personne, avec deux formules : 15 000 € HT pour 20 j et 30 000 € HT pour 40 j par mois, sur 6 mois | [PR] | contexte:66-72 | Le taux n'est justifié dans aucune pièce de mon lot |
| 31 | Le 28 oct., l'offre est « recalibrée à titre d'hypothèse sur vingt journées-personnes cumulées pour l'équipe ». « Vingt jours par personne n'est pas encore confirmé » | [PR] / [HY] | carlone-offres-et-projets.md:65 | Le prix de 15 000 € existait donc dès le 28 oct., avant l'offre du 2 nov. |
| 32 | Acompte de 7 500 € HT : « imputé sur le premier mois » (28 oct.), puis « à la commande », avec les mois 2 à 6 « payés d'avance » (4 nov.) | [PR] | carlone-offres-et-projets.md:65 ; contexte:75 | Les versions divergent (complement:25 ; index-complement:42) |
| 33 | Le premier mois est déjà réparti : cadrage 6 j, CRM et campagne pilote 7 j, copilote Jarvis 4 j, coordination 3 j | [PR] | contexte:76 | La campagne pilote fait double emploi avec Quali Contact. Le Jarvis relève de BOJ.ART (contexte:25, 39) |
| 34 | Plancher de négociation : environ 10 300 € HT par mois pour 14 journées | [PR] | contexte:77 | Cela fait ≈ 736 € par jour, ce qui contredit la règle « jamais le taux » (contexte:66) |
| 35 | Net estimé par personne et par mois : ≈ 3 660 € (base) et ≈ 7 500 € (renforcement) | [ES] | contexte:73, 83 | Modèle SARL à l'IS du 30 oct., non validé par un expert-comptable |
| 36 | Option laboratoire : pilote de 90 jours à 30 000 € HT, dont 13 500 € d'honoraires (18 j). Le matériel est possédé par l'entité de GianLuca Carlone | [PR] | contexte:78 | Le reste, 16 500 €, n'est pas détaillé. Qui facture le matériel ? |
| 37 | Option STRATES : phase 1 d'environ 10 000 € HT, dont 6 j Marwin (4 500 €). En échange : première présentation, exclusivité sur la série, films de fabrication | [PR] | contexte:79 | Promet des droits sur une œuvre de Medhi sans accord écrit (contexte:14). Option retirée du diaporama le 4 nov. (note-4-nov:25) |
| 38 | Programme R&D de 323 875 € HT : « ancien scénario », à ne pas présenter | [ES] | contexte:81 ; complement:23 | Les deux pièces le disent archive, pas commande |
| 39 | Décision orale du 4 nov. : « Va juste falloir enlever Medhi/boj art de l'offre » | [DR] | note-4-nov:25 | Elle ne figure ni dans le README (README.md:3, 18) ni dans le contexte (contexte:14, 20, 79) |
| 40 | Chiffres du CRM livré : 500 entreprises, 471 numéros, 60 interlocuteurs finance ou RH, 125 fiches d'appel, onglet Culture de 97 artistes et structures, version Firebase | [DR] | contexte:55 | Chiffres des documents du 2 nov., « sans nouvelle vérification » (contexte:162) |
| 41 | « Aucun prospect, rendez-vous ou taux de conversion n'est encore constaté » (au 28 oct.) | [FV] dans la page / aucun [MM] | carlone-offres-et-projets.md:57 | Aucun résultat commercial mesuré dans mon lot |
| 42 | 500 entreprises et 500 SIREN distincts à la révision 18c2080. La sélection n'est pas un classement homogène | [DR] | carlone-offres-et-projets.md:55 | Le commit 18c2080 existe bien, daté du 28 oct. à 10:15 UTC [FV] |
| 43 | Le dépôt FinanceScope/CRM-Carlone était public le 4 nov. à 16:19 ; on y avait compté 931 numéros, 206 e-mails et 63 fichiers de profils LinkedIn | [DR] | contexte:5, 11 | Non revérifié dans cet audit (note-4-nov:23). Risque RGPD en cours |
| 44 | Les comptes de Morgan n'ont qu'un accès en lecture au dépôt FinanceScope | [DR] | crm-reference:14 | C'est Mathys qui contrôle le code. La question de la propriété reste ouverte |
| 45 | Une copie du CRM (historique compris), les ZIP des 22 et 23 oct. et le dossier de Mathys sont entrés dans le dépôt privé Carlone le 4 nov. | [FV] | git 95de15f, 540c832 ; README.md:7 | Des données personnelles de dirigeants y sont donc copiées |
| 46 | La propriété du CRM déjà livré et de ses données est à trancher | [IN] | contexte:121 | Pourtant, le contexte parle de « son CRM » (contexte:5) et le README de « CRM de Carlone » (README.md:35) |
| 47 | Une intégration Hermes360 (Vocalcom) « sans serveur » a été codée le 28 oct. | [FV] | git 1d7f97d, bb9d5e2, 20a3a8e | Rien ne prouve que Quali Contact utilise Hermes360 (complement:41). C'est un développement bâti sur une hypothèse |
| 48 | Aucun test d'intégration avec Quali Contact n'a été exécuté | [DR] | carlone-offres-et-projets.md:49 ; crm-reference:12 | — |
| 49 | 219 conversations ChatGPT répertoriées : 216 actives et 3 archivées | [FV] (manifeste) | manifeste-complement:6-8 | — |
| 50 | Bilan cumulé : 169 conversations lues sur 219. Il en reste 50 sans lecture (47 refus pour limitation, 3 délais dépassés) | [FV] | manifeste-reprise:6-13 ; reprise:9-14 | J'ai recompté les statuts du manifeste : 47 / 9 / 3. Environ 23 % du corpus n'a pas été lu |
| 51 | Les lectures réussies ne rendent parfois que les derniers échanges, sans accès aux plus anciens | [DR] | reprise:19 ; index-complement:32 | « Un résultat sans mention directe ne démontre donc pas » l'absence de Carlone |
| 52 | Seules 3 conversations mentionnent directement Carlone, et chacune n'a restitué que 5 tours | [FV] | manifeste-complement:12, 53-71 | Couverture très mince, y compris sur « Bras robotique précis » |
| 53 | Les 9 nouvelles lectures ne contiennent aucune nouvelle mention de Carlone | [FV] | manifeste-reprise:15 | Même limite d'ancienneté |
| 54 | Aucun export intégral de l'historique ChatGPT n'a été obtenu | [DR] | reprise:19 ; index-complement:34 | — |
| 55 | Les 4 fichiers image originaux de la bibliothèque ChatGPT sont absents. 3 alternatives ont été extraites de PDF, sans vérification d'identité. Le 4e visuel n'a pas de correspondance certaine | [FV] | inventaire:355-393 ; manifeste-reprise:430-441 ; reprise:52-56 | J'ai vérifié les empreintes des 3 PNG |
| 56 | L'accès à la bibliothèque ChatGPT a été redirigé vers la page de connexion | [DR] | manifeste-reprise:447 ; reprise:56 | — |
| 57 | Le diaporama « Offre Marwin Tech » et les graphiques n'existent qu'en ligne | [DR] | README.md:52-55 ; index-complement:36 | Non archivés. Le nombre de diapositives diverge (section 4) |
| 58 | La section « Limites » du contexte déclare non lus des documents ajoutés ensuite au dépôt (choix de structure, options v5, dossier investisseur, budget, « Bras robotique précis ») | [FV] | contexte:158 ; git b205005, 553b8b4 | La synthèse du 4 nov. repose donc sur des résumés de seconde main |
| 59 | Avantage fiscal (art. 238 bis AB du CGI) : déduction sur 5 ans, plafond de 20 000 € ou 5 ‰ du chiffre d'affaires, pour les achats faits avant le 31 déc. 2028 | [DR] | contexte:89 | À vérifier sur source officielle (lecteur juridique). La page ChatGPT renvoie à « article 238 bis » (mécénat, l. 34) |
| 60 | Les œuvres faites à la machine (impression 3D, bras peintre) sont « très probablement exclues » de l'avantage fiscal | [HY] | contexte:90 | Rescrit non demandé |
| 61 | Interdiction de promettre un rendement, sous peine de basculer dans le régime des biens divers (AMF, contribution de 8 000 €) | [DR] | contexte:91 | À vérifier |
| 62 | Robot en galerie : intégrateur, ISO 10218-2:2025 et règlement (UE) 2023/1230 applicable au 20 janv. 2027 | [DR] | contexte:97 | À vérifier |
| 63 | Être à la fois salarié et prestataire du même client expose à une requalification | [HY] | contexte:94 ; complement:27 | Le salariat chez GianLuca reste une option ouverte (contexte:109) |
| 64 | Chercher un deuxième client d'ici le 4e mois | [PR] | contexte:95 | Morgan mène déjà de nombreux autres projets (note-4-nov:9-17). C'est un risque de capacité plus que de dépendance |
| 65 | Morgan veut faire de Marwin Tech une société de conseil et de réalisation, « sans garantie de pouvoir tout faire » | [DR] | complement:13 | — |
| 66 | Visuels et vidéos : générés par IA, ils ne démontrent aucune performance physique | [FV] (statuts) | complement:31, 35 ; inventaire:83, 139 ; reprise:60 | — |
| 67 | Le script Éclosion P0 n'a pas été exécuté. Les maillages ne certifient ni solidité ni sécurité | [DR] | complement:33 | — |
| 68 | « Une DGX Spark n'est ni une dépense approuvée ni un préalable » | [DR] | complement:37 | — |

---

## 3. Chiffres, engagements et dates

### 3.1 Montants et volumes de l'offre

| Élément | Valeur | Code | Source | Remarque |
| --- | --- | --- | --- | --- |
| Taux journalier | 750 € HT par journée-personne | [PR] | contexte:66 | Non justifié (aucun coût de revient dans mon lot) |
| Formule de base | 15 000 € HT par mois pour 20 journées (140 h), « un mi-temps chacun » | [PR] | contexte:70-71 ; carlone-offres-et-projets.md:65 | 140 h ÷ 20 = 7 h par jour |
| Renforcement | 30 000 € HT par mois pour 40 journées (280 h), « un plein temps chacun » | [PR] | contexte:70-71 | — |
| Total sur six mois | 90 000 € HT (base) ou 180 000 € HT (renforcement) | [PR] / [ES] | contexte:72 | Calcul exact |
| Acompte | 7 500 € HT | [PR] | contexte:75 ; carlone-offres-et-projets.md:65 | Imputé sur le 1er mois, ou versé à la commande (section 4) |
| Durée | 6 mois, avec reconduction comme cible | [PR] | contexte:77 | — |
| Répartition du mois 1 | 6 + 7 + 4 + 3 = 20 j | [PR] | contexte:76 | Total exact |
| Plancher | ≈ 10 300 € HT pour 14 j (≈ 736 € par jour) | [PR] | contexte:77 | 14 × 750 = 10 500 € |
| Net par personne | ≈ 3 660 € (base), ≈ 7 500 € (renforcement), 2 500 € « avec réserve » | [ES] | contexte:73, 119 | Ratio net / honoraires HT ≈ 49 % à 50 %. Simulation non validée |
| Option laboratoire | 30 000 € HT sur 90 j, dont 13 500 € pour 18 j | [PR] | contexte:78 | 16 500 € non expliqués |
| Option STRATES phase 1 | ≈ 10 000 € HT, dont 4 500 € pour 6 j | [PR] | contexte:79 | 5 500 € non expliqués. Retirée du diaporama (note-4-nov:25) |
| Option vernissage | 3 formats de 6 à 30 journées | [PR] | contexte:59, 80 | À 750 €/j, cela ferait 4 500 € à 22 500 € HT [ES, mon calcul]. Les honoraires sont « à fixer par Morgan ». Le budget hors honoraires est inconnu |
| Scénario R&D | 323 875 € HT, réserve comprise | [ES] | contexte:81 ; complement:23 | Archive, à ne pas présenter |
| Part maximale des revenus venant de GianLuca Carlone | La réponse « s'arrête sur « 10 millions » » | [IN] | contexte:129 | Réponse incohérente ou tronquée, à clarifier |

### 3.2 Volumes du CRM et de la collecte

| Élément | Valeur | Code | Source |
| --- | --- | --- | --- |
| Entreprises du CRM | 500, avec 500 SIREN distincts | [DR] | contexte:55 ; carlone-offres-et-projets.md:55 |
| Numéros, interlocuteurs, fiches d'appel, onglet Culture | 471 ; 60 ; 125 ; 97 | [DR] | contexte:55 |
| Données dans le dépôt public | 931 numéros, 206 e-mails, 63 profils LinkedIn | [DR] | contexte:11 |
| Comptes proposés pour un premier test | 20 (« choix de méthode, pas un objectif commercial ») | [PR] | carlone-offres-et-projets.md:57 |
| Conversations répertoriées / lues / non lues | 219 / 169 / 50 | [FV] | manifeste-reprise:6-14 |
| Détail des 59 relances | 9 réussies, 47 refus pour limitation, 3 délais dépassés | [FV] | manifeste-reprise:9-12 (recompté) |
| Étape précédente | 160 lues, dont 7 lors du complément | [FV] | manifeste-complement:9-11 |
| Conversations mentionnant Carlone | 3, à 5 tours restitués chacune | [FV] | manifeste-complement:12, 58-70 |
| Images Library manquantes / alternatives extraites | 4 / 3 | [FV] | manifeste-reprise:430-431 |
| Recherche dans les archives BOJART locales | 3 348 entrées, aucune correspondance | [DR] | manifeste-complement:74-76 |
| Contrôle des PDF | 11 PDF, 22 images incorporées, 3 pages rendues | [DR] | manifeste-reprise:442-446 |
| Occurrences de « John-Lucas » [sic, lire GianLuca] | ≈ 300 (note) ; 250 dans les fichiers texte du dépôt (mon comptage) | [FV] | note-4-nov:26 ; recherche dans le dépôt |

### 3.3 Échéances et durées réglementaires citées (à vérifier)

| Élément | Valeur | Code | Source |
| --- | --- | --- | --- |
| Fin du dispositif art. 238 bis AB | Achats avant le 31 déc. 2028 | [DR] | contexte:89 |
| Règlement machines (UE) 2023/1230 | Applicable au 20 janv. 2027 | [DR] | contexte:97 |
| Deuxième client | D'ici le 4e mois | [PR] | contexte:95 |
| Galerie | 2027 | [DR] | contexte:5 |
| Pilote laboratoire | 90 jours | [PR] | contexte:78 |

### 3.4 Chronologie reconstituée

| Date | Événement | Code | Source |
| --- | --- | --- | --- |
| ≈ mi-2025 | Morgan connaît Medhi « depuis un an et demi » | [DR] | contexte:27 |
| 18 oct. 2026, 19:47 UTC | PDF « Propositions de collaboration » généré (8 missions) | [FV] | Métadonnées du PDF ; contexte:45 |
| 21 oct., 18:30 UTC | Dossier de Mathys « Le Vieux Relais & le M », 34 pages : top 100 Pappers, 15 entreprises prioritaires | [FV] / [DR] | Métadonnées du PDF ; contexte:44 |
| 22 oct. | Rendez-vous (interlocuteur inconnu). CRM mis en ligne en artefact (v2, 100 entreprises). Invitation au dépôt GitHub FinanceScope | [DR] | contexte:43, 159 |
| 23 oct. | ZIP v3 du CRM : 500 entreprises, champs « art » | [DR] | contexte:42 |
| 25 oct. | Morgan annonce que GianLuca Carlone prévoit d'engager Quali Contact ; la construction de ses offres est mise de côté | [DR] | carlone-offres-et-projets.md:7 |
| 27-28 oct. | Enrichissement du CRM (numéros, décideurs, DAF), commits signés « Claude » | [FV] | git log |
| 28 oct. | Intégration Hermes360. Morgan fournit le dépôt CRM et rapporte « déléguer le quotidien » et « vingt jours par mois ». L'offre passe à 15 000 € HT. Dernière mise à jour de la page ChatGPT à 17:48 UTC | [FV] / [DR] | git 1d7f97d ; carlone-offres-et-projets.md:5, 18, 65 |
| 29 oct. | « Rapport pour M. Carlone » (PDF, Word) et étude Hermes360. CRM autonome sur Firebase. Étude « choix de structure » (7 p.) | [FV] | git 0669be1, f9aa294 ; contexte:41 |
| 30 oct. | « Options avantageuses » v5 (26 p.) : SARL à l'IS. Dernier envoi sur le CRM (b53a81c, 15:37 UTC) | [FV] | git ; métadonnées du PDF ; contexte:40 |
| 31 oct. | Éclosion (concept, P0, animation). Audit du laboratoire IA et robotique | [DR] | inventaire:5-95 (noms de fichiers datés) |
| 1er nov. | Récupération des archives BOJ.ART (3 ZIP, Jarvis M07) | [DR] | contexte:39 |
| 2 nov. | Note de vision, catalogue de 9 offres, offre Marwin Tech (document et diaporama de 13 diapositives), audit, proposition STRATES v1.1 (8 p., 00:22 UTC), dossier investisseur et budget | [DR] / [FV] (pages) | contexte:38 |
| 4 nov., matin | Point du matin : aucun rendez-vous jusqu'au 6 nov. Dépôt FinanceScope toujours public (vérifié à 16:19 selon l'en-tête) | [DR] | contexte:5, 9, 15 ; note-4-nov:5 |
| 4 nov. | Vernissage « Strates » : document d'idées, 6 visuels IA, diaporama de 12 diapositives | [DR] / [FV] (12 p.) | contexte:37 ; README.md:15 |
| 4 nov., 16:29 → 17:37 (+0100) | 8 commits : création du dépôt Carlone, dossier, intégration ChatGPT, copie du CRM (subtree), complément (160/219), reprise (169/219), livrables | [FV] | git log |
| 4 nov., après-midi | Décision orale de retirer Medhi et BOJ.ART de l'offre : le diaporama passe de 13 à 11 diapositives | [DR] | note-4-nov:25 |
| 4 nov. | Correction d'identité demandée par Morgan : GianLuca Carlone | [DR] | note-4-nov:26 |

---

## 4. Contradictions et divergences

| Sujet | Version A + source | Version B + source | Portée pour l'audit |
| --- | --- | --- | --- |
| Disponibilité de 20 jours | « disponibilité de vingt jours par mois, avec davantage de couverture si nécessaire » (souhait rapporté), recalibrée en 20 journées-personnes cumulées ; « vingt jours par personne n'est pas encore confirmé » (carlone-offres-et-projets.md:65) | 20 journées = « un mi-temps chacun » ; 40 journées = « un plein temps chacun » (contexte:71) | Si GianLuca entend 20 j par personne, il attend le renforcement (30 000 €) au prix de la base (15 000 €). « Davantage de couverture » n'a ni prix ni plafond |
| Calendrier de paiement | Acompte de 7 500 € « imputé sur le premier mois » (carlone-offres-et-projets.md:65) ; « facturation en fin de mois » dans certaines copies (complement:25) | Acompte « à la commande », travail démarrant à sa réception, mois 2 à 6 « payés d'avance » (contexte:75) | Contradiction non tranchée (index-complement:42), avec un effet direct sur la trésorerie |
| Règle du taux | « on ajuste le périmètre, jamais le taux » (contexte:66) | Plancher de 10 300 € pour 14 j, soit ≈ 736 € par jour (contexte:77) | Le plancher revient à une remise implicite de 1,9 % sur le taux |
| Place de Quali Contact | Prestataire d'appels prévu par le client, avec une passerelle CRM à construire (carlone-offres-et-projets.md:7, 13, 36-49) | Absent de tout le contexte du 4 nov. ; le mois 1 prévoit une « campagne pilote » de 7 j par Marwin (contexte:76) | Risque de double emploi, ou de périmètre mal défini : qui appelle, qui paie Quali Contact ? |
| Offres de GianLuca Carlone | « le message précédent proposant de construire ses offres reste mis de côté » ; la création d'une offre complète « n'est pas relancée » (carlone-offres-et-projets.md:7, 32) | Catalogue de 9 offres rédigé le 2 nov. (contexte:56) | Le périmètre a été rouvert sans décision tracée |
| Statut du M | « souhaite racheter « le M » » (carlone-offres-et-projets.md:15) | Destination des entreprises dès le 21 oct. (contexte:44, 47) ; propriété non établie (contexte:160) | Situation foncière inconnue. On ne peut pas fonder un chantier « lieux » là-dessus |
| Cabaret | « souhaite racheter » (carlone-offres-et-projets.md:15) | « peut-être un cabaret » (contexte:24) ; « le cabaret plus tard » (contexte:60) ; « Le cabaret tient-il toujours ? » (contexte:114) | Projet incertain, à classer comme exploratoire |
| Biens possédés | « six bâtiments et l'ancienne affaire de Medhi » (contexte:24) | « un ancien bar restaurant hôtel avec cour » (carlone-offres-et-projets.md:14) | Les deux sont des déclarations rapportées et aucune n'est vérifiée. Elles ne prouvent pas une trésorerie disponible |
| Medhi et BOJ.ART | Partie prenante : README.md:3 (« avec Medhi (BOJ.ART) »), README.md:18 (proposition STRATES « BOJ.ART et Marwin Tech » dans `pour-carlone/`), contexte:14, 20, 79 | « Va juste falloir enlever Medhi/boj art de l'offre » (note-4-nov:25) | Décision orale, non formalisée. Les documents destinés au client n'ont pas été mis à jour. Le vernissage « Strates » montre une œuvre de BOJ.ART (contexte:5, 59) |
| Diaporama de l'offre | 13 diapositives (README.md:52 ; contexte:38, 144) | 11 diapositives après le retrait du 4 nov. (note-4-nov:25) | Versions multiples, aucune n'est validée |
| Emplacement du CRM | « Le CRM reste dans son dépôt canonique » (crm-reference:3) ; « Le code et les données restent dans FinanceScope » (complement:41) | Copie complète dans `crm/`, « chacun peut désormais y travailler » (README.md:35 ; crm-reference:10) | Deux copies vivantes, synchronisées à la main (subtree pull), avec un risque de divergence |
| Données personnelles dans le dépôt | « Les nouvelles pièces n'incluent ni export des 500 entreprises ni identifiants » (complement:43) | `crm/` et `sources/` « contiennent les coordonnées des entreprises prospectées » (README.md:7). Le dossier de Mathys, qui nomme des dirigeants, a été ajouté (540c832) | Données copiées dans un 3e emplacement |
| Propriété du CRM | « son CRM » (contexte:5) ; « le CRM de Carlone » (README.md:35) | « la propriété du CRM déjà livré et de ses données » est à trancher (contexte:121) ; le code est dans le dépôt de Mathys (README.md:35), où Morgan n'a pas de droit d'écriture (crm-reference:14) | Le travail a été livré gratuitement avant toute immatriculation. Les droits sont à clarifier avant toute remise |
| Couverture de la collecte | 160 lues sur 219 (README.md:64 ; index-complement:30) | 169 lues sur 219 (README.md:68 ; reprise:13) | Étapes successives. Seul le dernier bilan (169) vaut |
| Limites du contexte | « Non lus, faute d'accès » : structure, options, dossier investisseur… (contexte:158) | Pièces ajoutées au dépôt 17 à 35 minutes plus tard (b205005, 553b8b4) | La synthèse est antérieure aux pièces. Ses chiffres de structure sont de seconde main |
| Format de STRATES | 90 × 65 cm (contexte:58, audit) | 90 × 56 cm (contexte:126, simulation) | Non tranché avec Medhi |
| Vérification du dépôt public | « revérifié ce matin » (contexte:9) | « revérifié le 4 novembre à 16 h 19 » (contexte:5) | Incohérence mineure d'horodatage |
| Revenus et durée | Objectif de 7 500 € nets chacun (contexte:119) | Suppose 12 mois à plein temps, alors que le contrat n'en couvre que 6 (contexte:83) | L'objectif personnel n'est pas finançable par le contrat proposé |
| Facturation | « Sans société, pas d'acompte possible » (contexte:12) | Morgan a une entreprise existante, mais sa domiciliation est résiliée (note-4-nov:6) | La structure qui facture n'est pas arrêtée |
| Gouvernance du capital | « Garder la majorité à Morgan et Mathys » (contexte:93) | « SAS si Carlone entre au capital » (contexte:12) | Ce n'est pas une contradiction, mais une tension non arbitrée |
| Ce qui a été proposé | 8 missions de gestion d'établissements (pdf p. 1) | Un seul chantier livré, le CRM, et cinq propositions tech et art (contexte:51-60) | Le besoin initial, plus proche du pilotage, a dérivé vers des projets techniques et artistiques |
| Hiérarchie des sources | « Ses priorités récentes priment sur les idées plus anciennes » (complement:7) | La demande d'audit interdit de prendre la version la plus récente pour une décision approuvée | Cette règle de hiérarchie a été posée par un assistant, pas par une décision |
| Référence fiscale | « article 238 bis du CGI » (mécénat), avec un lien Légifrance (carlone-offres-et-projets.md:34) | « article 238 bis AB du CGI » (œuvres d'artistes vivants) (contexte:89) | La page distingue bien les deux dispositifs mais ne cite que le premier. Les références sont à vérifier |

---

## 5. Informations inconnues et questions

**Sur GianLuca Carlone et ses entités**
1. Quelle est l'orthographe exacte de son nom (« GianLuca ») et quelles sont ses fonctions officielles dans ses sociétés ?
2. Quelles entités juridiques détient-il ou dirige-t-il (dénomination, SIREN, siège) ? Laquelle commande, laquelle signe, laquelle paie, et qui valide les livrables (contexte:106) ?
3. Quels biens possède-t-il réellement : les « six bâtiments », lesquels et à quel titre ; l'« ancien bar restaurant hôtel avec cour » ; le Vieux Relais ? Le M est-il acquis, en cours d'achat ou seulement souhaité ?
4. Qu'est-ce que « l'ancienne affaire de Medhi » qu'il aurait rachetée, à quelles conditions, et quels liens en résultent avec Medhi ?
5. Quelle structure vend les œuvres, et quel nom le CRM doit-il porter dans chaque message (contexte:111) ?
6. Qui sont ses responsables d'établissement, son comptable et son expert-comptable ou avocat fiscaliste (pdf p. 1 ; contexte:113) ?

**Sur le besoin et la délégation**
7. Que recouvre « déléguer le quotidien » : lesquelles des 8 missions du 18 oct., dans quel ordre ?
8. Le PDF du 18 oct. a-t-il été remis à GianLuca Carlone ? Quand, par qui, et qu'en a-t-il dit ?
9. « Vingt jours par mois » : est-ce son expression ou celle de Morgan ? S'agit-il de jours cumulés ou par personne ? De présence sur place ? Que signifie « davantage de couverture » (astreinte, soirées, week-ends) ?
10. Quelles décisions veut-il garder, et quels plafonds de dépense accepterait-il de déléguer ?
11. Quels accès et données est-il prêt à fournir : comptabilité, contrats, agenda, outils ?

**Sur les rendez-vous et la relation**
12. Avec qui a eu lieu le rendez-vous du 22 oct., et qu'a-t-on montré ou promis ?
13. Le rendez-vous « argent et rémunération » a-t-il eu lieu ? Sinon, à quelle date ?
14. GianLuca Carlone a-t-il vu ou utilisé le CRM ? Le « Rapport pour M. Carlone » du 29 oct. lui a-t-il été remis ?
15. A-t-il exprimé un budget, un mode de paiement ou une préférence entre paiement d'avance et fin de mois ?

**Sur Quali Contact**
16. Quali Contact est-il engagé (contrat, entité signataire, date) ? Quel logiciel et quel module utilise-t-il (Hermes360 / Vocalcom ou autre) ? Qui pilote ses campagnes ?
17. La « campagne pilote » du mois 1 (7 j) fait-elle double emploi avec Quali Contact ?

**Sur Marwin Tech, Morgan et Mathys**
18. Quelle structure facturerait aujourd'hui : l'entreprise existante de Morgan (non nommée), une nouvelle société, ou autre ?
19. Combien de jours par mois chacun peut-il réellement consacrer à GianLuca Carlone, compte tenu de ses autres projets (note-4-nov:9-17) ?
20. Qui possède le CRM, ses données et les développements Hermes360 et Firebase ? Mathys a-t-il donné son accord à la copie dans le dépôt Carlone ?
21. Le dépôt FinanceScope/CRM-Carlone est-il désormais privé ?
22. Que signifie la réponse « 10 millions » à la question de la part maximale des revenus venant de GianLuca Carlone (contexte:129) ?

**Sur Medhi, STRATES et le vernissage**
23. Le retrait de Medhi et BOJ.ART vaut-il aussi pour la proposition STRATES v1.1 et pour le vernissage « Strates », qui reste centré sur une œuvre de BOJ.ART ?
24. Mathys et Medhi ont-ils été informés de ce retrait ?

**Sur la collecte**
25. Les 50 conversations non lues et les parties anciennes des 169 lues contiennent-elles des engagements, des prix ou des promesses faits à GianLuca Carlone ?
26. Où sont les 4 images originales de la bibliothèque, et le 4e visuel (« Atelier MARWIN TECH, art et robotique ») a-t-il été montré au client ?

---

## 6. Par chantier

| Chantier | Ce que disent mes pièces |
| --- | --- |
| **CRM et développement commercial** | Seul chantier livré, sans facture : 500 entreprises, 471 numéros, 60 interlocuteurs, 125 fiches, plafond fiscal calculé, version Firebase (contexte:55) [DR]. Changement de but entre le 21 oct. et le 2 nov. (contexte:47). 48 commits signés « Claude » du 27 au 30 oct. [FV]. Aucun prospect, rendez-vous ni taux de conversion constaté (carlone-offres-et-projets.md:57). Proposition de démarrer avec 20 comptes (l. 57) [PR]. Dépôt FinanceScope public au 4 nov. (contexte:11) [DR]. Copie dans le dépôt Carlone [FV]. Propriété non tranchée (contexte:121). L'entité émettrice des offres est inconnue (carlone-offres-et-projets.md:18) |
| **Quali Contact** | Le client « prévoit d'engager Quali Contact » (carlone-offres-et-projets.md:7) [DR]. Cahier de raccordement proposé, « pas une compatibilité attestée » (l. 38-49) [PR]. Critères de réception définis mais aucun test exécuté (l. 49). Le logiciel et le format d'échange sont inconnus (l. 51, 69 ; crm-reference:12) [IN]. Une étude et une intégration Hermes360 / Vocalcom existent dans le CRM, sans preuve d'usage par Quali Contact (complement:41) [HY]. **Absent du contexte du 4 nov.** |
| **Organisation et pilotage** | Missions 1 à 5 du PDF du 18 oct. : suivi des établissements, rentabilité, administratif, prestataires, outils après rachat (pdf p. 1) [PR]. Souhait de « déléguer le quotidien » et « vingt jours par mois » (carlone-offres-et-projets.md:65) [DR]. Offre de 15 000 ou 30 000 € HT par mois (contexte:70) [PR]. Coordination de 3 j au mois 1 (contexte:76). Modèle « Cadrer / Produire / Piloter » (complement:17) [PR]. La continuité passe par « des plages, des relais et une éventuelle astreinte distincte ; aucun engagement permanent » (carlone-offres-et-projets.md:65) |
| **Jarvis, mémoire et automatisations** | Morgan « construit Jarvis » (contexte:25) ; archives BOJ.ART « Jarvis M07 » (contexte:39) ; « copilote Jarvis » de 4 j au mois 1 (contexte:76) [PR]. « L'atelier Jarvis, UNUM et les recherches artistiques ne sont pas automatiquement inclus dans un abonnement commercial Carlone » (complement:17). L'IA doit « documenter et orchestrer », « sans garantie de pouvoir tout faire » (complement:13). La mission 3 prévoit d'« automatiser les rappels et le classement » (pdf p. 1). Aucune mesure de résultat |
| **Marketing et contenus** | « studio marketing » (carlone-offres-et-projets.md:7) [DR]. La mission 5 prévoit d'actualiser « le site, les cartes, les horaires et les réservations » (pdf p. 1) [PR]. Visuels et vidéos IA du vernissage, de STRATES et d'Éclosion : intentions uniquement (complement:31 ; reprise:60). Rien d'autre |
| **Galerie, œuvres et artistes** | Galerie en 2027 (contexte:5, 24) [DR]. Ancien bar-restaurant-hôtel avec cour racheté pour une galerie (carlone-offres-et-projets.md:14) [DR]. Mission 6, catalogue privé des œuvres (pdf p. 1) [PR]. Catalogue de 9 offres de vente aux entreprises, brouillon à faire valider par l'expert-comptable (contexte:56) [PR]. Règles fiscales (contexte:89-91) [DR]. Les artistes, les œuvres et les prix sont inconnus (contexte:112) [IN]. Mise en garde mécénat / déduction (carlone-offres-et-projets.md:34) |
| **Événements et vernissage** | Mission 7, séjours des invités, et mission 8, événements art et restauration (pdf p. 1) [PR]. Souhait de « réunir des artistes et peintres dans la ville de Morgan » (carlone-offres-et-projets.md:16) [DR]. Vernissage « Strates » : 5 temps, 21 idées, 3 formats de 6 à 30 j, 6 visuels IA, diaporama de 12 diapositives (contexte:59, 80 ; README.md:15-17) [PR]. Lieu, date, nombre d'invités et budget inconnus (contexte:115) [IN] |
| **Cabaret et autres lieux** | « souhaite racheter « le M » » (carlone-offres-et-projets.md:15) ; « peut-être un cabaret » (contexte:24) ; « plus tard » (contexte:60) [DR]. Le Vieux Relais et le M sont des cibles du dossier du 21 oct., mais leur propriété n'est pas établie (contexte:44, 160) [IN]. Les missions 1 et 5 parlent d'« établissements » et de « rachat » (pdf p. 1) |
| **Medhi et BOJ.ART** | Medhi : sculptures, figurines, parc d'impression 3D, « plus que partant » (contexte:27) [DR]. Accord à trois à écrire avant de présenter STRATES (contexte:14) [PR]. Ses trois documents ne mentionnent pas Carlone (contexte:62). Ses droits ne sont pas transférés par leur ajout au dépôt (complement:9). Retrait de l'offre le 4 nov., décision orale (note-4-nov:25) [DR], pas reporté dans README.md:3, 18 |
| **STRATES, Éclosion et créations** | STRATES : relief d'environ 90 × 65 cm peint par un bras robotisé ; rien n'est fabriqué ni mesuré (contexte:58) [DR]. Phase 1 à environ 10 000 € HT (contexte:79) [PR], retirée du diaporama. Vidéo IA de 10 s (complement:35 ; inventaire:79-86). Éclosion : concept, CAO P0, script non exécuté, aucun essai (complement:33 ; index-integration:17-18). Visuels extraits de PDF sans identité vérifiée (reprise:23-50) |
| **Laboratoire IA et robotique** | Pilote de 90 j à 30 000 € HT, matériel possédé par l'entité de GianLuca Carlone (contexte:78) [PR]. Audit du 31 oct., « financement non validé » (index-integration:20). Proposition d'évolution, illustrations générées (complement:31). DGX Spark non approuvée (complement:37). Normes à respecter avant tout robot en galerie (contexte:97) [DR] |

---

## 7. Erreurs d'identité

**Dans les pièces de mon lot (chemin:ligne) :**
- `interne/complement-chatgpt-2026-11-04.md:15` : « Pour John-Lucas Carlone » [sic, lire GianLuca].
- `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md` : lignes 1, 7, 13, 14, 15, 16, 18, 32, 65, soit 9 occurrences, dont le titre « John-Lucas Carlone Offre et projets en Nièvre » [sic, lire GianLuca].
- `sources/index-complement-sessions-chatgpt-2026-11-04.md:19` : « Carlone, John-Lucas ou Quali Contact » (employé comme critère de recherche) [sic, lire GianLuca].
- `sources/manifeste-complement-sessions-chatgpt-2026-11-04.json:40, 47` : titres des pages « John-Lucas Carlone Offre et projets en Nièvre » et « Marwin Tech Accompagnement de John-Lucas Carlone » [sic, lire GianLuca].
- Aucune occurrence dans README.md, le contexte, index-integration, reprise, crm-reference, le README des livrables, l'inventaire, le manifeste de reprise, le PDF du 18 oct. ni les messages de commit.

**Dans tout le dépôt (fichiers texte, hors .git) :** 250 occurrences de « John-Lucas » ou « John Lucas » ; la note d'audit en annonçait environ 300, en comptant probablement les ZIP. Principaux fichiers :
- recueils HTML : 34 + 34 + 27 ;
- textes sources : 32 + 32 + 25 ;
- `marwin-offre-accompagnement.json` / `.md` : 13 / 10 ;
- `carlone-offres-et-projets.json` / `.md` : 11 / 9 ;
- `travail-pour-marwin-studio.json` : 5 ;
- `pilotage-extraits-carlone` : 3 + 3.

Aucune occurrence de « GianLuca ».

**Autres variantes et points voisins :**
- Le contexte, les documents Claude et les commits disent « Carlone » ou « M. Carlone » sans prénom. Ce n'est pas une erreur, mais aucun prénom n'y figure.
- « Matisse » pour Mathys : complement:9 et `interne/recueil-sessions-chatgpt-2026-11-04.txt:249` (« moi et Matisse »), 14 occurrences dans le dépôt.
- Les 134 occurrences de « Jean-Luc » sont toutes dans `crm/` (dirigeants d'entreprises prospectées). Ce ne sont **pas** des erreurs d'identité du client ; elles ne doivent pas être confondues avec lui.

---

## 8. Instructions trouvées dans les pièces (non exécutées)

| Source | Texte ou demande | Destinataire apparent |
| --- | --- | --- |
| contexte:9-16 | Liste « À faire tout de suite » : passer le dépôt GitHub FinanceScope en privé (Settings, Danger Zone), immatriculer Marwin Tech, prendre une RC pro, ouvrir un compte pro, écrire l'accord avec Medhi, fixer le rendez-vous, ne pas présenter l'ancien artefact du CRM | Morgan (rédigé par un assistant) |
| contexte:104-127 | Listes de questions « À demander à Carlone », « À trancher entre Morgan et Mathys », « À régler avec Medhi » | Morgan |
| README.md:37-39 | Commande `git subtree pull --prefix=crm https://github.com/FinanceScope/CRM-Carlone.git claude/new-session-utninu` | Utilisateur du dépôt |
| index-integration:41 | Script de restitution `tools/restaurer-archives.py` (« reconstitue et contrôle les originaux ») | Utilisateur du dépôt |
| complement:33 | « Lire `prototype-p0/LIRE_AVANT_ESSAI.txt` avant toute fabrication » | Futur fabricant |
| index-complement:3 | Citation d'une consigne de Morgan à un assistant : « Récupère tout ce que tu peux et pousse le reste » | Assistant ChatGPT |
| complement:5 ; manifeste-complement:4 ; manifeste-reprise:3 | « pousser sur le GitHub Carlone les pièces », « Complément documentaire autorisé par Morgan », « explicitement demandées par Morgan » | Assistants de collecte |
| note-4-nov:25 | « Va juste falloir enlever Medhi/boj art de l'offre » (déjà appliqué au diaporama selon la note) | Assistant Claude |
| carlone-offres-et-projets.md:13-16, 67-69 | « Prochaine décision » et « Prochaine étape technique » : obtenir le logiciel de Quali Contact, tester une campagne fictive, etc. | Morgan et l'équipe |
| crm-reference:12 | « Premier essai à prévoir sur données fictives, sans toucher à la production » | Équipe |
| index-integration:11 | « ne pas remettre ce dossier au client » | Équipe |
| index-complement:7 ; livrables/collecte-chatgpt-2026-11-04/README.md:9 | « télécharger le fichier HTML puis l'ouvrir dans un navigateur », « ouvrir index.html » | Lecteur |

Aucune de ces instructions n'a été exécutée dans le cadre de cette lecture.

---

## 9. Points d'audit

1. **Profil client invérifié et payeur inconnu.** Tout ce qu'on sait de GianLuca Carlone (origine, acquisitions, galerie, investissement, rémunération proposée) vient de Morgan, par l'intermédiaire de deux assistants IA (contexte:29 ; complement:15). Aucune entité juridique n'est nommée (contexte:57, 106). Il est impossible de contracter, de facturer ou d'apprécier la solvabilité en l'état. « Plus gros client » (contexte:5) est une projection, puisqu'aucune facture n'a été émise.
2. **Besoin réel non établi.** La seule pièce de besoin est une proposition de Marwin (PDF du 18 oct., anonyme, sans réponse connue), plus deux phrases rapportées : « déléguer le quotidien » et « vingt jours par mois ». La répartition du mois 1 (CRM 7 j, Jarvis 4 j) ne correspond à aucune des 8 missions, sauf la coordination. L'hypothèse d'un « pilotage global » reste à tester.
3. **Ambiguïté sur les 20 jours.** Cette ambiguïté détermine le prix (15 000 ou 30 000 €) et la charge. La « couverture si nécessaire » n'a ni prix ni plafond.
4. **Quali Contact effacé du contexte de référence.** Le document de référence du 4 nov. ignore un prestataire que le client prévoit d'engager. Un développement Hermes360 a été fait sans savoir quel logiciel Quali Contact utilise : c'est un travail bâti sur une hypothèse, non facturé.
5. **Deux fils IA parallèles non rapprochés.** ChatGPT (arrêté au 28 oct. : Quali Contact, pas d'offres à construire) et Claude (2-4 nov. : catalogue, STRATES, vernissage, laboratoire) divergent sur le périmètre. La règle « les priorités récentes priment » (complement:7) a été posée par un assistant, pas par une décision.
6. **Taux de 750 € HT non justifié** dans mon lot : ni coût de revient, ni comparaison, ni charge réelle. Le plancher à environ 736 € par jour contredit la règle du taux unique. Les nets (3 660 et 7 500 €) sont des simulations non validées. L'objectif de 7 500 € n'est pas finançable sur 6 mois (contexte:83).
7. **Calendrier de paiement contradictoire** : imputation sur le mois 1 et fin de mois, ou paiement à la commande et d'avance. Il faut une seule version écrite avant toute proposition.
8. **Structure qui facture non résolue.** L'affirmation « Sans société, pas d'acompte » ignore l'entreprise existante de Morgan, dont la domiciliation est résiliée et les abonnements en échec (note-4-nov:6-8). Du travail a déjà été livré avant toute structure et tout contrat : le CRM, le rapport du 29 oct., les études. Propriété et responsabilité ne sont pas couvertes.
9. **Données personnelles exposées et dupliquées.** Le dépôt FinanceScope était public au dernier contrôle rapporté (931 numéros, 206 e-mails, 63 profils LinkedIn). Une copie complète et le dossier nommant des dirigeants sont désormais dans un 3e emplacement. Aucune base légale ni durée de conservation n'est documentée dans mon lot.
10. **Propriété du CRM floue.** Il est dit « son CRM » et « CRM de Carlone », mais il se trouve dans le dépôt de Mathys, où Morgan n'a qu'un accès en lecture, et sa propriété est « à trancher ». Les commits sont signés par un assistant IA, et l'historique antérieur au 27 oct. n'est pas visible dans le clone superficiel.
11. **Retrait de Medhi et BOJ.ART incomplet.** Le README, `pour-carlone/strates-proposition-artistique-v1.1.pdf` et le contexte présentent toujours BOJ.ART. Le vernissage « Strates » reste construit sur une œuvre de BOJ.ART. L'option STRATES promettait déjà une exclusivité sur la série de Medhi sans accord écrit (contexte:79 contre l. 14). Il y a un risque de présenter au client un document qui contredit la décision.
12. **Collecte incomplète.** 50 conversations sur 219 n'ont pas été lues (environ 23 %). Les lectures sont partielles, avec seulement les derniers échanges. Les 3 conversations qui citent Carlone n'ont restitué que 5 tours chacune. L'absence de mention ne prouve pas l'absence d'engagement : des promesses de prix ou de délai faites à GianLuca Carlone peuvent exister hors du corpus lu.
13. **Contexte de référence en partie périmé.** Ses « Limites » listent comme non lues des pièces ajoutées ensuite. Ses chiffres (CRM, structure) sont de seconde main, « sans nouvelle vérification » (contexte:162). Il ne doit pas être traité comme la vérité de référence.
14. **Visuels.** Ce sont des intentions générées par IA. Les 4 originaux sont absents et les 3 extractions n'ont pas d'identité vérifiée. L'image « bras éducatif » provient d'un document interne de rémunération (options v5, p. 9) mais a été rangée dans `pour-carlone/`. Ce classement « n'atteste pas leur validation » (index-integration:11).
15. **Lieux.** Le M est-il « à racheter » ou déjà une destination ? Le Vieux Relais lui appartient-il ? La galerie est-elle « l'ancien bar-restaurant-hôtel » ? Rien n'est établi. Les missions et chantiers liés aux lieux (cabaret, événements, outils après rachat) reposent sur des acquisitions non vérifiées.
16. **Dépendance cumulée.** GianLuca Carlone serait à la fois payeur, bailleur des bureaux, investisseur et peut-être employeur (contexte:24, 94-95, 109). La réponse « 10 millions » (contexte:129) montre que la question de la dépendance n'est pas traitée sérieusement.
17. **Capacité de Morgan non documentée.** Morgan mène de nombreux projets parallèles : 91 artefacts, plan « Vendre 10 sites », plusieurs clients (note-4-nov:9-17). La disponibilité de Mathys n'est documentée nulle part (contexte:120). La formule de 20 à 40 journées-personnes par mois n'a pas de base de capacité démontrée.
18. **Affirmations réglementaires à vérifier** sur source officielle datée : art. 238 bis AB (plafond, date limite), régime des biens divers et contribution AMF, ISO 10218-2:2025, règlement (UE) 2023/1230. Ce sont des [DR] reprises d'une session à l'autre sans citation datée dans le contexte.
19. **Aucun rendez-vous prévu** jusqu'au 6 nov. et dix questions bloquantes sans réponse (contexte:106-115). La préparation documentaire (offre, diaporamas, vernissage) a pris de l'avance sur la validation du besoin et de l'acheteur.
20. **Aucun résultat mesuré [MM] dans mon lot** : pas de vente d'œuvre, pas d'appel, pas de rendez-vous obtenu, pas de test d'intégration, pas d'essai physique. Toute valeur affichée pour GianLuca Carlone reste à démontrer.
