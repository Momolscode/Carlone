# Lecteur C4-methodes : méthodes de consulting et de pilotage, prix, OLSEN, supervision humaine, audit du 2 novembre

Extraction établie le 4 novembre 2026 pour l'audit de la collaboration Marwin Tech avec GianLuca Carlone. Lecture seule ; aucune action extérieure ; aucune modification du dépôt.

Conventions de citation : les pièces sont citées par leur nom de fichier suivi du numéro de ligne (`nom.md:12`). Les chemins complets figurent dans la section 1. Pour les deux artefacts claude.ai, les numéros de ligne renvoient au texte extrait dans `scratchpad/sources-txt/` (l'artefact d'origine n'a pas de lignes) ; l'URL de l'artefact est donnée en section 1. Pièces citées en contrôle croisé seulement : `note-point-4-novembre-et-activites.md` (note de l'auditeur, dossier `audit-work/`) et `interne/contexte-projet-carlone.md` (dépôt).

## 1. Pièces lues

| Chemin | Date de la pièce | Nature et auteur si connu | Original ou copie/export | Ce qui n'a pas pu être lu |
| --- | --- | --- | --- | --- |
| `interne/audit-marwin-tech-carlone.md` | 2 nov. 2026 (en-tête « Nov 2, 2026 · @Olsen Morgan », ligne 3) ; versé au dépôt le 4 nov. 2026 à 16 h 38 (commit fa5998a) | Audit interne « Audit Marwin Tech × Carlone : risques et solutions », rédigé pour Morgan Olsen (document produit avec un assistant ; artefact d'origine https://claude.ai/artifact/RdJ3zRdkFtxKfoFx5CeM2g selon `interne/contexte-projet-carlone.md:145`) | Export Markdown d'un document claude.ai, donc une copie | Deux contenus intégrés non exportés : « Matrice des risques · 14 risques, 4 zones » (ligne 46 ; la liste des 14 risques reste lisible, pas leur placement) et « Plan des 30 jours · 4 étapes, 3 décisions » (ligne 110, contenu entièrement absent). Les artefacts liés en ligne 118 (offre Marwin, offres CRM, note State Of The Art) n'ont pas été ouverts. |
| `sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md` | Page mise à jour le 28 oct. 2026 à 17 h 33 UTC ; collectée le 4 nov. 2026 | Page ChatGPT « Marwin Tech Méthode de consulting et audits » (espace de Morgan ; texte d'assistant, orientation attribuée à Morgan le 28 oct., ligne 9) | Copie de la page entière (42 blocs selon le .json voisin) | Les pages ChatGPT liées (premier forfait, audit du CRM, lignes 77 et 79) ne sont pas lues ici. |
| `sources/chatgpt-pages/2026-11-04-complement/audit-pilotage-extraits-carlone.md` | Page mise à jour le 25 oct. 2026 à 10 h 18 UTC ; collectée le 4 nov. 2026 | Page ChatGPT « Marwin Audit du pilotage et des outils » | Extraits seulement : 5 blocs retenus parce qu'ils citent Carlone, « John-Lucas » [sic, lire GianLuca] ou Quali Contact | Le reste de la page (blocs sans ces mots) n'est pas disponible ; les pages liées en ligne 9 ne sont pas lues. |
| `sources/chatgpt-pages/2026-11-04-complement/pilotage-extraits-carlone.md` | Page mise à jour le 31 oct. 2026 à 7 h 54 UTC ; état « rapproché le 25 octobre » (ligne 9) ; collectée le 4 nov. 2026 | Page ChatGPT « Marwin Studio Pilotage et mémoire » | Extraits seulement : 4 blocs | Le reste de la page ; la console privée citée (ligne 18) et le paquet 0.2.0 (ligne 17) n'ont pas été ouverts. |
| `[texte extrait] artifact-corpus-offres-ia-vendables-2026-08-20.txt` | 20 août 2026 (ligne 15) | Artefact claude.ai « Corpus des offres IA vendables », document interne OLSEN (entreprise individuelle de Morgan), https://claude.ai/artifact/THqmjoYaYtU1zZt8Ed7Dny | Texte extrait d'un artefact HTML, donc une copie | Les « 3 veilles sourcées · ~90 sources » (ligne 16) ne sont pas jointes : aucune statistique ni aucun prix ne peut être rattaché à sa source. La mise en page visuelle est perdue. |
| `[texte extrait] artifact-olsen-travail-qui-se-repete.txt` | 24 août 2026 | Artefact claude.ai « OLSEN — Le travail qui se répète, fait par une machine » : page commerciale de Morgan (OLSEN), https://claude.ai/artifact/3QhXaHkCdnBZDwtXKnmMsV | Texte extrait de l'aperçu (« Aperçu de la nouvelle version », ligne 6), donc une copie | Le contenu interactif « Vous faites quoi ? » (les trois questions par métier, lignes 21-31) n'est pas dans le texte. Les mentions légales sont « dans la version en ligne » (ligne 154), non disponibles. Aucune preuve de mise en ligne. |

Pièces de cadrage lues avant le travail : `BRIEF-AGENTS.md`, `DEMANDE.md` et `note-point-4-novembre-et-activites.md` (dossier `audit-work/`).

## 2. Affirmations déterminantes

| # | Affirmation | Code | Source | Remarque |
| --- | --- | --- | --- | --- |
| 1 | Verdict de l'audit du 2 nov. : « L'offre tient : un prix clair, un paiement d'avance et un outil déjà livré ». | [HY] | `audit-marwin-tech-carlone.md:7` | Appréciation. Le « paiement d'avance » n'est qu'une proposition : rien n'est signé (ligne 14). |
| 2 | Marwin Tech n'est pas immatriculée, donc aucune facture n'est possible. | [DR] | `audit-marwin-tech-carlone.md:13` | Confirmé par la note C. L'audit n'examine pas l'entreprise existante de Morgan (OLSEN, SIRET en `artifact-olsen-travail-qui-se-repete.txt:153`). |
| 3 | Rien n'est signé ; l'entité de GianLuca Carlone qui paiera n'est pas identifiée. | [DR] | `audit-marwin-tech-carlone.md:14`, `:121` | Toujours [IN] au 4 nov. dans mes pièces. |
| 4 | Le dépôt GitHub du CRM est public et contient des coordonnées de prospects ; il faut le passer en privé « aujourd'hui ». | [DR] | `audit-marwin-tech-carlone.md:15`, `:27`, `:93` | Toujours public le 4 nov. à 16 h 19 selon `interne/contexte-projet-carlone.md:5`, `:11` : l'action urgente du 2 nov. n'était pas faite deux jours plus tard. |
| 5 | Le CRM est prêt : 500 entreprises, 471 numéros, 60 interlocuteurs finance ou RH, 125 fiches d'appel, version autonome sur Firebase. | [DR] | `audit-marwin-tech-carlone.md:11`, `:35` | Non revérifié. Un autre décompte du même dépôt donne 931 numéros, 206 e-mails et 63 profils LinkedIn (`interne/contexte-projet-carlone.md:11`). |
| 6 | Le CRM a été construit sans facture. | [DR] | `audit-marwin-tech-carlone.md:31` | Travail fourni gratuitement avant tout contrat. La propriété du code et des données n'est traitée nulle part dans mes pièces. |
| 7 | Prix proposé : 750 € HT la journée-personne, deux formules, mois payés d'avance, acompte de 7 500 €. | [PR] | `audit-marwin-tech-carlone.md:12`, `:36` | L'audit le classe « Solide » alors que GianLuca Carlone ne l'a pas accepté. |
| 8 | Huit propositions sont à mener dans 20 journées par mois. | [DR] | `audit-marwin-tech-carlone.md:17`, `:60` | Les huit propositions ne sont pas énumérées dans la pièce [IN]. |
| 9 | Rémunération : environ 3 660 € nets chacun en base, soit un mi-temps ; 7 500 € nets supposent le plein temps à 30 000 € HT. | [ES] | `audit-marwin-tech-carlone.md:18`, `:84` | Hypothèses de calcul absentes (statut, cotisations, impôt, frais). Non validé par un expert-comptable (`:121`). |
| 10 | Immatriculer Marwin Tech en SARL à l'IS par défaut, en SAS si GianLuca Carlone entre au capital. | [PR] | `audit-marwin-tech-carlone.md:23`, `:94` | Aucune comparaison chiffrée dans la pièce. |
| 11 | Contrat-cadre avec acompte avant démarrage, bon de commande mensuel et réversibilité. | [PR] | `audit-marwin-tech-carlone.md:24`, `:97` | La réversibilité est citée une seule fois, sans contenu. |
| 12 | Choisir entre la base à trois priorités par mois et le renforcement pour mener les huit propositions. | [PR] | `audit-marwin-tech-carlone.md:25`, `:60` | Une « priorité » n'est bornée ni en jours ni en livrables. |
| 13 | Écrire un accord à trois avec Medhi (rôles, droits, partage des ventes, accès au parc) avant de présenter la ligne création. | [PR] | `audit-marwin-tech-carlone.md:26`, `:102` | À revoir après la décision orale du 4 nov. de retirer Medhi et BOJ.ART de l'offre (`note-point-4-novembre-et-activites.md:25`) [DR]. |
| 14 | Équipe complémentaire : « Morgan pilote, Mathys construit, Medhi crée ». | [DR] | `audit-marwin-tech-carlone.md:38` | Aucune preuve de compétence associée. Eaglemic, présenté ailleurs comme associé, est absent (`pilotage-extraits-carlone.md:9`). |
| 15 | « Carlone a racheté l'affaire de Medhi et propose bureaux et investissement. » | [DR] | `audit-marwin-tech-carlone.md:40` | Ne prouve aucune trésorerie disponible (`DEMANDE.md:23`). |
| 16 | L'audit liste 14 risques ; leur placement est « l'appréciation de cet audit, pas une mesure ». | [FV] | `audit-marwin-tech-carlone.md:46-65`, `:48` | Fait vérifié : c'est bien ce que dit le document. Le placement graphique n'est pas exporté. |
| 17 | Il existe un risque de requalification en salariat si GianLuca Carlone fixe les bureaux, les horaires et les consignes. | [HY] | `audit-marwin-tech-carlone.md:56` | La parade proposée (bons de commande, méthodes propres) n'est pas détaillée. |
| 18 | Trouver un deuxième client d'ici le mois 4 en vendant le CRM clé en main à d'autres vendeurs de la Nièvre. | [PR] | `audit-marwin-tech-carlone.md:55`, `:103` | Pose un problème de droits (CRM fait pour GianLuca Carlone) et de charge (Mathys, dont le temps n'est « pas fixé », `:62`). |
| 19 | TJM médians 2026 en France : développeur ≈ 485 €, chef de projet ≈ 595 €, data scientist ≈ 620 €, consultant ≈ 629 € ; IA générative entre 750 et 1 500 €, sans médiane. | [DR] | `audit-marwin-tech-carlone.md:71-80` | Source secondaire (freelance-solution.fr, juin 2026), consultée le 2 nov. et non revérifiée. |
| 20 | 750 € se défend pour le cadrage, le CRM et l'IA, mal pour l'administratif. | [HY] | `audit-marwin-tech-carlone.md:69`, `:82-83` | Justifié par le CRM livré, dont l'adoption n'est pas démontrée. |
| 21 | « Le volume fait le revenu » ; ne pas baisser le taux mais retirer des jours ou un volet. | [PR] | `audit-marwin-tech-carlone.md:84-85` | Règle de négociation cohérente. Le plancher n'est pas chiffré. |
| 22 | Sortir l'administratif du taux : Marwin outille et pilote, une personne de GianLuca Carlone ou un prestataire local exécute. | [PR] | `audit-marwin-tech-carlone.md:83`, `:100` | Recommandation importante pour le périmètre (séjours des invités, gestion déléguée). |
| 23 | Mettre en place une téléphonie simple reliée au CRM (Ringover ou Aircall), comme le recommandait l'étude Hermes360. | [PR] | `audit-marwin-tech-carlone.md:101` | Quali Contact n'est pas mentionné : doublon ou conflit possible avec l'outil de Quali Contact. |
| 24 | La facture électronique sera obligatoire à l'émission en septembre 2027 pour les petites entreprises. | [DR] | `audit-marwin-tech-carlone.md:95`, `:119` | À revérifier sur service-public.fr. L'obligation de réception n'est pas évoquée. |
| 25 | Souscrire une RC professionnelle, une clause de sous-traitance RGPD (article 28) et un registre des traitements avant le démarrage. | [PR] | `audit-marwin-tech-carlone.md:96`, `:98` | Ni coût ni délai indiqués. |
| 26 | Faire relire les messages de vente : ni rendement, ni rachat garanti, et économie d'impôt sous réserve de l'avis de l'expert-comptable. | [PR] | `audit-marwin-tech-carlone.md:58`, `:99` | Concerne les ventes d'œuvres de GianLuca Carlone (risque fiscal et AMF). |
| 27 | L'audit du 2 nov. n'a examiné ni contrat, ni comptabilité, ni échange avec GianLuca Carlone. | [FV] | `audit-marwin-tech-carlone.md:121` | Limite déclarée par le document lui-même. |
| 28 | L'audit du 2 nov. ne mentionne ni Quali Contact, ni Jarvis, ni le premier forfait de cadrage, ni Eaglemic, ni la TVA, ni la propriété des développements, ni la maintenance. | [FV] | Recherche dans `audit-marwin-tech-carlone.md` (4 nov.) | Ces lacunes sont importantes pour l'audit actuel. |
| 29 | Marwin Tech devient un « cabinet de conseil opérationnel et de réalisation », l'IA servant de moyen (orientation donnée par Morgan le 28 oct.). | [DR] | `marwin-methode-consulting-audits.md:9` ; `pilotage-extraits-carlone.md:22` | Attribué à Morgan. |
| 30 | Trois offres : Cadrer (diagnostic sourcé), Produire (lot défini), Piloter (temps réservé de coordination), chacune avec sa propre réception. | [PR] | `marwin-methode-consulting-audits.md:19-23` | Architecture plus prudente que le forfait mensuel unique de l'audit du 2 nov. |
| 31 | Le diagnostic est payant. La réalisation et le suivi sont chiffrés séparément. Le matériel et les bureaux ont leur propre budget. | [PR] | `marwin-methode-consulting-audits.md:25` | Contredit l'idée qu'un abonnement couvre tout. |
| 32 | Morgan garde les arbitrages commerciaux et la validation du travail livré. Les responsabilités de l'associé dépendent de ses compétences démontrées et de son temps. | [PR] | `marwin-methode-consulting-audits.md:15` | Règle de supervision humaine. Morgan est le point unique de validation. |
| 33 | L'audit approfondi suit sept étapes, et la comparaison inclut le maintien de l'existant et une amélioration simple avant toute solution d'IA. | [PR] | `marwin-methode-consulting-audits.md:29-41` | Correspond au §6 de la demande. |
| 34 | Un échange commercial initial ne constitue pas à lui seul un audit approfondi. | [PR] | `marwin-methode-consulting-audits.md:43` | Aucun audit du besoin réel de GianLuca Carlone n'est documenté dans mes pièces. |
| 35 | Une mission peut prendre quatre voies, dont « attente ou refus motivé ». S'engager suppose un résultat compris, des compétences, des accès, un budget, du temps et une réception possible. | [PR] | `marwin-methode-consulting-audits.md:61` | Fournit des conditions de refus déjà écrites. |
| 36 | Les connecteurs et systèmes autonomes doivent être éprouvés en environnement réel avant d'être vendus comme opérationnels. Les actions externes restent limitées au mandat. | [PR] | `marwin-methode-consulting-audits.md:63` | Règle à opposer à toute promesse d'automatisation faite à GianLuca Carlone. |
| 37 | Le suivi d'une mission passe par cinq états (à qualifier, cadrée, en réalisation, en réception, close). Pour clore, il faut des preuves, l'acceptation, la passation et les écarts ouverts. | [PR] | `marwin-methode-consulting-audits.md:65` | Sert de base aux preuves de réception. |
| 38 | Pour la qualité de l'IA : garder des cas normaux et des cas d'échec, mesurer le temps total corrections comprises et le coût par résultat accepté. | [PR] | `marwin-methode-consulting-audits.md:69` | S'inspire du NIST AI RMF (consulté le 28 oct.) ; « ne constitue pas une certification ». |
| 39 | Premier forfait « Cadrage et préparation du raccordement CRM » : entretien de 60 à 90 min, jusqu'à 5 pièces, 1 chantier, 1 aller-retour ; livre une feuille de route, une fiche mission et un cahier de passation ; ne s'étend pas à l'ensemble des projets. | [PR] | `marwin-methode-consulting-audits.md:77` | Point d'entrée borné, absent de l'audit du 2 nov. |
| 40 | Le prix du premier forfait n'est pas fixé : « Le prix attend les jours, tarifs et structure facturante. » | [IN] | `marwin-methode-consulting-audits.md:79` | |
| 41 | Prospection, développement du connecteur, productions marketing et lieux culturels sont des lots distincts. | [PR] | `marwin-methode-consulting-audits.md:79` | Rejoint le §4 de la demande. |
| 42 | La fiche d'entrée réutilisable est vide : tous les champs sont « à renseigner », « à convenir » ou « à calculer ». | [FV] | `marwin-methode-consulting-audits.md:85-103` | La décision attendue de GianLuca Carlone n'est formulée nulle part. |
| 43 | La revue de code couvre la console et le prototype 0.1, dont les 20 tests ont été relancés avec succès. | [DR] | `audit-pilotage-extraits-carlone.md:11` | Mesure rapportée, non relancée ici. |
| 44 | 22 dépôts et 24 périmètres sont inventoriés, mais pas tous audités (code, sécurité, résultats commerciaux). | [DR] | `audit-pilotage-extraits-carlone.md:11`, `:13` | Indique la dispersion du portefeuille de Morgan. |
| 45 | Le CRM actualisé, le logiciel de Quali Contact, les machines et les comptes de diffusion sont « hors d'accès vérifié » (25 oct.). | [DR] | `audit-pilotage-extraits-carlone.md:11` | Limite de preuve importante. |
| 46 | Ordre de travail : 1) une mission rémunérée (qui fait quoi, temps, tarifs, structure) ; 2) le raccordement à Quali Contact, testé sur une campagne fictive. | [PR] | `audit-pilotage-extraits-carlone.md:17-18` | La priorité 1 suppose un accord avec Mathys, non documenté. |
| 47 | Au 25 oct., « aucun fichier de 500 prospects vérifié n'a été produit » ; il faut définir « les 500 plus grandes entreprises de la Nièvre ». | [DR] | `audit-pilotage-extraits-carlone.md:21` | Le critère de sélection reste inconnu dans mes pièces. |
| 48 | Mathys Couet est « l'un de ses associés principaux » ; Eaglemic (Michael Bach) est aussi un associé principal de Morgan. | [DR] | `pilotage-extraits-carlone.md:9` | Contredit la présentation à deux de Marwin Tech. |
| 49 | Le CRM a été audité le 28 oct. : révision 18c2080, 500 SIREN distincts, enrichissement présent ; « suivi en service non consulté ». | [DR] | `pilotage-extraits-carlone.md:19` | Aucune preuve d'usage réel par l'équipe de GianLuca Carlone. |
| 50 | Quali Contact : « engagement prévu et logiciel à identifier ». | [DR] | `pilotage-extraits-carlone.md:24` | La nature de l'engagement est inconnue. |
| 51 | « Gain de temps à mesurer » ; cinq cas fictifs ; « ni statut, ni capital, ni rémunération, ni matériel ne sont actés » (31 oct.). | [IN] | `pilotage-extraits-carlone.md:20` | Aucun gain mesuré dans mes pièces. |
| 52 | Un atelier « Reverse API Engineer » a été ajouté au paquet 0.2.0 (106 tests, aucun site tiers capturé). | [DR] | `pilotage-extraits-carlone.md:17` | Risque juridique et contractuel s'il était utilisé sur des services tiers. |
| 53 | La console privée compte huit vues, 24 dossiers, 22 dépôts, cinq films, huit missions et 33 tests. | [DR] | `pilotage-extraits-carlone.md:18` | Mesure de l'outillage, pas d'un résultat client. |
| 54 | La méthode de consulting « reste à éprouver en mission réelle ». | [DR] | `pilotage-extraits-carlone.md:22` | Aucune mission rémunérée réalisée selon cette méthode n'est documentée. |
| 55 | Le corpus OLSEN compte 25 offres : 12 vendables tout de suite, 7 sous condition, 3 à ne pas vendre, 3 « ni offres ni impasses ». | [FV] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:46-60` | Total vérifié (12 + 7 + 3 + 3 = 25). |
| 56 | Les prix du corpus sont « des fourchettes constatées sur le marché français, pas des estimations », et non des ventes d'OLSEN. | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:865-866` | L'intitulé « prix de vente constaté » (`:69`) prête à confusion. |
| 57 | « Sur 200 déploiements IA en France », les systèmes 100 % automatiques réussissent 30 % moins bien, et 88,5 % des projets qui survivent gardent une supervision humaine. | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:115-117` | Aucune source précise : chiffre à ne pas reprendre devant GianLuca Carlone. |
| 58 | Doctrine : ne jamais vendre « ça tourne tout seul » ; vendre « ça fait le travail, vous validez en deux minutes ». | [PR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:119-121` ; `artifact-olsen-travail-qui-se-repete.txt:84-87` | Règle de supervision humaine à transposer. |
| 59 | Un forfait « tout illimité » donne une marge nulle ; « Un forfait se borne par un nombre ». | [PR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:738-739` | S'applique directement aux « huit propositions dans 20 journées ». |
| 60 | Publicité : aucune fonction ne peut activer une campagne ; le budget est borné par le code ; tout est créé « EN PAUSE » ; une vigie peut tout suspendre. | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:435-439`, `:453-459` | Exemple de garde-fou technique à reprendre pour toute dépense de GianLuca Carlone. |
| 61 | Relances d'impayés : « 20 % des dossiers doivent remonter à un humain ». | [PR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:527-528` | Taux d'escalade fixé par contrat. |
| 62 | Assistant documentaire : refuser si la documentation n'est pas fiabilisée, si les droits ne sont pas gérés, si le besoin porte sur des chiffres structurés ou si le savoir est seulement oral. Prix de marché : cadrage 3 à 12 k€, construction 10 à 50 k€, fonctionnement 1 à 3 k€ par mois. | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:559-571` | Repère direct pour Jarvis et la mémoire documentaire chez GianLuca Carlone. |
| 63 | AI Act, article 26 : si le prestataire exploite le système pour le compte du client, il peut être le « déployeur » légal ; à trancher par une clause du contrat. | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:797-802` | Non traité dans l'audit du 2 nov. Lecture juridique à faire valider. |
| 64 | « Les pipelines produisent déjà plus que ce que le carnet d'adresses absorbe » ; la première personne à recruter « appelle, elle ne code pas ». | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:710-712` | La contrainte est commerciale et relationnelle, pas productive. |
| 65 | Les pipelines OLSEN (forge, outreach à 8 agents, régie) « tournent déjà ». | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:74`, `:102`, `:196`, `:368` | Dépôt olsen-ai-intelligence non accessible (`note-point-4-novembre-et-activites.md:22`). Aucun envoi constaté (`:9`). |
| 66 | Page OLSEN : sites de démonstration « inventés », « vous voyez avant de payer », « pas d'abonnement obligatoire », « un seul interlocuteur : moi ». | [PR] | `artifact-olsen-travail-qui-se-repete.txt:59-61`, `:66-81` | Ce modèle de travail fait avant d'être payé contredit la règle « aucun travail avant contrat et acompte » (`audit-marwin-tech-carlone.md:54`). |
| 67 | OLSEN au 4 nov. : 503 prospects tous « À faire », 36 propositions de 2 200 à 4 600 € HT et 72 brouillons d'e-mails, aucun envoyé. | [DR] | `note-point-4-novembre-et-activites.md:9` | Aucune vente OLSEN n'est documentée dans mes pièces. |

## 3. Chiffres, engagements et dates

### Offre Marwin Tech et audit du 2 novembre

| Élément | Valeur | Code | Source |
| --- | --- | --- | --- |
| Taux unique | 750 € HT la journée-personne, « taux d'équipe, outils compris » | [PR] | `audit-marwin-tech-carlone.md:12`, `:78` |
| Formule de base | 20 journées-personnes par mois, soit 15 000 € HT (750 × 20, calcul cohérent) | [PR] | `audit-marwin-tech-carlone.md:17-18` ; `DEMANDE.md:55` |
| Formule renforcée | 30 000 € HT par mois, plein temps (40 journées-personnes selon `DEMANDE.md:55`) | [PR] | `audit-marwin-tech-carlone.md:18` |
| Acompte | 7 500 € (sans mention HT dans l'audit), soit 10 journées-personnes | [PR] | `audit-marwin-tech-carlone.md:12` |
| Durée | Contrat de six mois, bilan au mois 3, clause de reconduction | [PR] | `audit-marwin-tech-carlone.md:57` |
| Montant sur six mois | 90 000 € HT en base, 180 000 € HT en renforcé (mon calcul ; la TVA n'est jamais évoquée dans l'audit) | [ES] | Calcul à partir de `audit-marwin-tech-carlone.md:18`, `:57` |
| Rémunération simulée | ≈ 3 660 € nets par associé en base (mi-temps) ; 7 500 € nets à 30 000 € HT. Soit environ 49 % puis 50 % du chiffre d'affaires HT reversé en net (mon calcul) | [ES] | `audit-marwin-tech-carlone.md:18`, `:84` |
| Charge par proposition | 20 journées-personnes pour 8 propositions, soit ≈ 2,5 journées-personnes par mois et par proposition (mon calcul) | [ES] | `audit-marwin-tech-carlone.md:17` |
| Périmètre de la base | Trois priorités par mois | [PR] | `audit-marwin-tech-carlone.md:25`, `:60` |
| CRM | 500 entreprises, 471 numéros, 60 interlocuteurs finance ou RH, 125 fiches d'appel | [DR] | `audit-marwin-tech-carlone.md:11`, `:35` |
| Échéance pour le dépôt privé | « Aujourd'hui », soit le 2 nov. ; non fait au 4 nov. à 16 h 19 | [DR] | `audit-marwin-tech-carlone.md:93` ; `interne/contexte-projet-carlone.md:5` |
| Immatriculation, compte professionnel | Semaine 1 (après le rendez-vous J0) | [PR] | `audit-marwin-tech-carlone.md:94-95` |
| RC Pro, contrat-cadre, clause RGPD | Avant le démarrage | [PR] | `audit-marwin-tech-carlone.md:96-98` |
| Grille de relecture, sortie de l'administratif, téléphonie | Mois 1 | [PR] | `audit-marwin-tech-carlone.md:99-101` |
| Deuxième client | Mois 2 à 4 | [PR] | `audit-marwin-tech-carlone.md:55`, `:103` |
| Facture électronique | Émission obligatoire en septembre 2027 pour les petites entreprises | [DR] | `audit-marwin-tech-carlone.md:95` |
| Plan | 30 jours à partir du rendez-vous (J0), contenu non exporté | [IN] | `audit-marwin-tech-carlone.md:108-112` |
| Repères de TJM 2026 | Développeur ≈ 485 € (350 à 650) ; chef de projet ≈ 595 € (450 à 800) ; data scientist ≈ 620 € (470 à 900) ; consultant ≈ 629 € (400 à 1 000) ; IA 750 à 1 500 € ; moyenne IT ≈ 520 € ; Île-de-France ≈ 613 € | [DR] | `audit-marwin-tech-carlone.md:71-80` |
| Écart du taux de 750 € aux médianes | +26 % sur le chef de projet, +19 % sur le consultant, +55 % sur le développeur, +44 % sur la moyenne IT (mon calcul) | [ES] | Calcul à partir de `audit-marwin-tech-carlone.md:71-80` |

### Méthode et pilotage (pages ChatGPT)

| Élément | Valeur | Code | Source |
| --- | --- | --- | --- |
| Premier forfait de cadrage | Entretien de 60 à 90 min, jusqu'à 5 pièces, 1 chantier, 1 aller-retour ; prix non fixé | [PR] / [IN] | `marwin-methode-consulting-audits.md:77`, `:79` |
| Orientation « cabinet de conseil » | 28 oct. 2026 | [DR] | `marwin-methode-consulting-audits.md:9` |
| CRM audité | 28 oct. 2026 ; révision 18c2080 ; 500 SIREN distincts | [DR] | `pilotage-extraits-carlone.md:19` |
| Tests | 20 (prototype 0.1), 106 (paquet 0.2.0), 33 (console), dont 17 contrôles sur les missions et les prix ; 5 cas fictifs | [DR] | `audit-pilotage-extraits-carlone.md:11` ; `pilotage-extraits-carlone.md:17-18`, `:20` |
| Portefeuille de Morgan | 22 dépôts, 24 périmètres ou dossiers, 5 films, 8 missions | [DR] | `audit-pilotage-extraits-carlone.md:11`, `:13` ; `pilotage-extraits-carlone.md:18` |
| Films Marwin Studio (mission MAR-03) | Plan R02 de 10,08 s (export 10,10 s), 720 × 1280, 24 images par seconde ; devis de 70 crédits, plafond de 80 | [DR] | `pilotage-extraits-carlone.md:15` |
| Dates clés du pilotage | État rapproché le 25 oct. ; Instagram choisi le 26 oct. ; R02 terminé le 29 oct. ; atelier RAE ajouté le 30 oct. | [DR] | `pilotage-extraits-carlone.md:9`, `:14`, `:16-17` |

### Repères OLSEN (prix de marché indiqués par le corpus, pas des ventes)

| Offre | Prix | Code | Source |
| --- | --- | --- | --- |
| Site vitrine | 800 à 2 500 €, plus 15 à 30 € par mois d'hébergement ; « 5 jours annoncés, 1 après-midi réel » | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:144-147` ; `artifact-olsen-travail-qui-se-repete.txt:95` |
| Refonte et référencement local | 1 500 à 4 000 € | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:236` ; `artifact-olsen-travail-qui-se-repete.txt:101` |
| Démarchage par e-mail en marque blanche | 150 à 450 € par mois, plus 1 500 à 4 000 € de mise en place | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:190` |
| Rendez-vous facturé au résultat | 80 à 250 € par rendez-vous tenu, avec plafond écrit | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:256-259` |
| Standard téléphonique IA | 80 à 300 € par mois, plus 500 à 2 000 € de mise en place ; coût réel 3 à 5 fois le prix à la minute affiché | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:287-290` |
| Rendez-vous et rappels sans voix | 400 à 900 €, plus 40 à 90 € par mois | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:310` |
| Gestion de comptes sociaux | 600 à 1 500 € par mois ; vidéos courtes en option, 200 à 500 € par mois | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:362`, `:379` |
| Publicité | 15 à 20 % du budget média, au moins 250 € par mois | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:451` |
| Traitement des factures | 80 à 250 € par mois (TPE) ; 300 à 800 € par mois (PME), plus 2 à 5 k€ de mise en place ; rentabilisé en 2,8 à 6 mois | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:499-505` |
| Relance d'impayés | Mise en place de 2 500 à 7 500 € dans la synthèse, mais de 2 500 à 12 000 € dans le détail ; 80 à 350 € par mois | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:83` contre `:522` |
| Support client automatisé | 800 € à 12 000 € selon le palier ; API 30 à 300 € par mois ; maintenance 80 à 300 € par mois | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:538-551` |
| Assistant documentaire | Cadrage 3 à 12 k€ ; construction 10 à 50 k€ ; fonctionnement 1 à 3 k€ par mois | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:562` |
| Qualification de leads | 150 à 450 € par mois | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:588` |
| Reporting en complément | 500 à 4 000 € | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:608` |
| Conformité IA | 1 500 à 6 000 €, plus une revue annuelle de 600 à 1 500 € | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:637` |
| Micro-SaaS | ≈ 19 000 € la première année (≈ 1 600 € par mois), puis vers ≈ 670 € par mois | [ES] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:684` |
| Outillage | n8n ≈ 20 € par mois ; Make 9 à 12 $ par mois ; Zapier dès 19,99 $ ; pipelines OLSEN : API ≈ 12 $ par mois, « VPS déjà payé » | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:817-834` |
| Gains cités | Relances : 3 h 30 → 22 min par semaine ; délais de paiement −38 % (chiffre d'éditeur). Factures : 4 à 8 min → moins de 30 s ; 320 factures : 40 h → 8 h. Démarchage : remplace 15 à 25 h par semaine. 65 % du temps commercial non productif | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:81`, `:186-187`, `:496`, `:519`, `:585` |
| Échecs des agents autonomes | Navigation autonome : 34 % d'échec en moyenne, 62 % pour l'agent le plus vendu en 2025 | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:734` |
| Propositions OLSEN préparées | 36 propositions de 2 200 à 4 600 € HT, aucune envoyée | [DR] | `note-point-4-novembre-et-activites.md:9` |

### Dates réglementaires citées par le corpus (à revérifier sur les sources officielles)

| Date | Événement | Code | Source |
| --- | --- | --- | --- |
| 27 juil. 2026 | Entrée en vigueur du « Digital Omnibus » | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:760-761` |
| 2 août 2026 | AI Act, article 50 (transparence) applicable | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:333`, `:771-773` |
| 11 août 2026 | Démarchage téléphonique en consentement préalable strict (loi 2025-594, article 13), pour les particuliers seulement ; sanctions jusqu'à 75 000 € pour une personne physique et 375 000 € pour une personne morale | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:210`, `:336`, `:775-777` |
| 24 sept. 2026 | Fermeture de l'API Sora 2 | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:402`, `:779-781` |
| 2 déc. 2026 | Fin de la tolérance sur la transparence pour les systèmes déjà en place | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:634`, `:783-785` |
| 2 déc. 2027 | Systèmes à haut risque de l'annexe III (recrutement, crédit) | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:787-789` |
| 2 août 2028 | Haut risque embarqué de l'annexe I (machines) | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:791-793` |
| Sanctions AI Act | 35 M€ ou 7 % ; 15 M€ ou 3 % ; 7,5 M€ ou 1 % | [DR] | `artifact-corpus-offres-ia-vendables-2026-08-20.txt:767-769` |

## 4. Contradictions et divergences

| Sujet | Version A et source | Version B et source | Portée pour l'audit |
| --- | --- | --- | --- |
| Statut de Mathys | « l'un de ses associés principaux » (`pilotage-extraits-carlone.md:9`, état au 25 oct.) | « futur associé » ; Mathys est « identifié sur le dossier Carlone, sans que cela fixe la composition ou les parts » (`marwin-methode-consulting-audits.md:15`, 28 oct.) ; l'audit du 2 nov. le traite comme co-fondateur rémunéré à parts égales (`audit-marwin-tech-carlone.md:18`, `:94`) | Associés, parts et apports sont non décidés. Ne pas prendre la version du 2 nov. pour un accord. |
| Associés de Morgan | Eaglemic (Michael Bach) est aussi « associé principal » (`pilotage-extraits-carlone.md:9`) | Équipe : Morgan, Mathys et Medhi (`audit-marwin-tech-carlone.md:38`) ; demande centrée sur « nous deux » (`DEMANDE.md:18`) | Un troisième associé possible n'est pas traité : capital, disponibilité, conflits. |
| Place de Medhi | Accord à trois et « Medhi crée » (`audit-marwin-tech-carlone.md:26`, `:38`, `:102`) | Décision orale du 4 nov. : retirer Medhi et BOJ.ART de l'offre (`note-point-4-novembre-et-activites.md:25`) | L'audit du 2 nov. est en partie dépassé. La décision n'est ni écrite ni partagée avec Mathys ou Medhi. |
| Architecture de l'offre | Cadrer, Produire et Piloter séparés ; diagnostic payant ; lots chiffrés à part (`marwin-methode-consulting-audits.md:19-25`, `:79`) | Taux unique ; deux formules mensuelles ; huit propositions dans 20 journées (`audit-marwin-tech-carlone.md:12`, `:17`, `:78`) | Risque qu'un abonnement absorbe tous les travaux, ce que la demande veut éviter (`DEMANDE.md:28`). |
| Premier engagement | Forfait de cadrage borné qui « n'élargit pas ce forfait à l'ensemble des projets » (`marwin-methode-consulting-audits.md:77`) ; priorité à « une mission rémunérée » sur le « cadrage Carlone déjà délimité » (`audit-pilotage-extraits-carlone.md:17`) | Contrat-cadre de six mois à 15 000 ou 30 000 € HT par mois (`audit-marwin-tech-carlone.md:24`, `:57`) | Saut d'échelle sans étape de diagnostic payé. Le besoin réel de GianLuca Carlone n'est pas testé. |
| Fichier de prospects | « aucun fichier de 500 prospects vérifié n'a été produit » (`audit-pilotage-extraits-carlone.md:21`, 25 oct.) | 500 SIREN distincts (`pilotage-extraits-carlone.md:19`, 28 oct.) ; « CRM prêt » (`audit-marwin-tech-carlone.md:11`) | Évolution dans le temps, mais le critère « 500 plus grandes » n'est jamais défini dans mes pièces. |
| Volumes du CRM | 471 numéros et 60 interlocuteurs (`audit-marwin-tech-carlone.md:11`) | 931 numéros, 206 e-mails et 63 profils LinkedIn dans le dépôt (`interne/contexte-projet-carlone.md:11`) | Unités différentes (fiches ou occurrences), non expliquées. L'exposition des données personnelles est sous-estimée par le premier chiffre. |
| CRM « en service » | « Un outil qui marche », « CRM en service » (`audit-marwin-tech-carlone.md:31`, `:35`) | « suivi en service non consulté » (`pilotage-extraits-carlone.md:19`) ; CRM actualisé « hors d'accès vérifié » (`audit-pilotage-extraits-carlone.md:11`) | L'usage réel par l'équipe de GianLuca Carlone n'est pas prouvé. La « valeur déjà livrée » reste à réceptionner. |
| Téléphonie et prospection | Raccorder le CRM au logiciel de Quali Contact, à identifier (`audit-pilotage-extraits-carlone.md:18` ; `pilotage-extraits-carlone.md:19`, `:24`) | Ringover ou Aircall reliés au CRM (`audit-marwin-tech-carlone.md:101`), sans mention de Quali Contact | Risque d'outil en double ou de conflit avec le prestataire d'appels. |
| Travail avant paiement | « Vous voyez avant de payer » (`artifact-olsen-travail-qui-se-repete.txt:66-69`) ; le CRM a été « construit sans facture » (`audit-marwin-tech-carlone.md:31`) | « Aucun travail avant contrat et acompte » (`audit-marwin-tech-carlone.md:54`) | Habitude de travail gratuit à arrêter explicitement. Le statut du CRM déjà fourni est à régler (cession, licence, facture). |
| Durée d'engagement | « Pas d'abonnement obligatoire » (`artifact-olsen-travail-qui-se-repete.txt:74-75`) ; « Un contrat qui se résilie quand on veut se vend mieux » (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:748-749`) | Engagement de six mois (`audit-marwin-tech-carlone.md:57`) | Doctrine commerciale de Morgan incohérente d'une offre à l'autre. À arbitrer. |
| Forfait borné | « Un forfait se borne par un nombre » ; un forfait « tout illimité » donne une marge nulle (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:738-739`) | Huit propositions au fil de l'eau dans 20 journées (`audit-marwin-tech-carlone.md:60`) | Les leçons d'OLSEN ne sont pas appliquées à l'offre faite à GianLuca Carlone. |
| Statut de prix du corpus | « prix de vente constaté » (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:69`) | « fourchettes constatées sur le marché français » (`:865-866`) | Ce ne sont pas des ventes d'OLSEN. |
| Mise en place des relances | 2 500 à 7 500 € (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:83`) | 2 500 à 12 000 € (`:522`) ; la page commerciale n'affiche que « à partir de 80 €/mois » (`artifact-olsen-travail-qui-se-repete.txt:112`) | Incohérence interne. La page publique omet la mise en place alors qu'elle promet « pas de ligne qui apparaît à la fin ». |
| Calcul des gains sur les factures | Moins de 30 s par facture (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:496`) | 320 factures : 40 h → 8 h, soit 1,5 min par facture (même ligne) | Chiffre non expliqué ; 320 × 30 s ≈ 2,7 h. |
| Fiche Google | Comprise dans le site (`artifact-olsen-travail-qui-se-repete.txt:96`) | Option à 300 à 600 € (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:167`) | Divergence mineure de périmètre. |
| Zone commerciale d'OLSEN | Loire-Atlantique, Maine-et-Loire, Vendée (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:17`, 20 août) | Cosne-Cours-sur-Loire et « partout en France » (`artifact-olsen-travail-qui-se-repete.txt:9`, `:128-132`, 24 août) | Positionnement changeant ; les repères de prix viennent d'un autre territoire que la Nièvre. |
| Capacité déclarée et usage réel | Démarchage « tourne déjà » (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:102`) | 72 brouillons et 36 propositions, aucun envoi ; 503 prospects « À faire » (`note-point-4-novembre-et-activites.md:9`) | Pouvoir produire ne veut pas dire vendre. Constat central pour l'ambition de « faire le travail de 100 personnes ». |
| Facturation | « Aucune facture possible » (`audit-marwin-tech-carlone.md:13`) | Morgan dispose d'un SIRET (OLSEN, `artifact-olsen-travail-qui-se-repete.txt:153`), avec une domiciliation résiliée (`note-point-4-novembre-et-activites.md:6`) | Option non examinée, avec ses propres obstacles (domiciliation, TVA, domaine suspendu). |

## 5. Informations inconnues et questions

1. Quelle entité juridique de GianLuca Carlone signerait et paierait ? Qui valide les livrables ? (`audit-marwin-tech-carlone.md:14`, `:121`)
2. GianLuca Carlone a-t-il vu ou accepté une version chiffrée de l'offre (750 € HT, 15 000 € HT par mois, acompte de 7 500 €, six mois) ? Laquelle, et à quelle date ?
3. Quelles sont précisément les « huit propositions » (`audit-marwin-tech-carlone.md:17`) ? Quelle est la charge de chacune, en journées-personnes ?
4. Quel prix pour le premier forfait de cadrage (`marwin-methode-consulting-audits.md:77-79`) ? A-t-il été proposé à GianLuca Carlone ?
5. Quelle décision GianLuca Carlone doit-il pouvoir prendre à l'issue du cadrage ? La fiche d'entrée est vide (`marwin-methode-consulting-audits.md:81-103`).
6. Qui a construit le CRM (Mathys ? Morgan ? l'organisation FinanceScope ?), qui en détient le code et les données, et sous quelle licence ? Peut-on le revendre à d'autres clients (`audit-marwin-tech-carlone.md:103`) ?
7. Quel critère définit « les 500 plus grandes entreprises de la Nièvre » (`audit-pilotage-extraits-carlone.md:21`) ? D'où viennent les numéros et les profils LinkedIn ? Sur quelle base légale ?
8. L'équipe de GianLuca Carlone utilise-t-elle réellement le CRM (vue « Aujourd'hui », fiches d'appel) ? Avec quels résultats d'appels ?
9. Le dépôt FinanceScope/CRM-Carlone est-il désormais privé ? Existe-t-il des copies (forks, pages publiées) ?
10. Quel logiciel utilise Quali Contact ? Quel est son lien contractuel avec GianLuca Carlone, qui le paie, et que recouvre l'« engagement prévu » (`pilotage-extraits-carlone.md:24`) ?
11. Combien de journées par mois Morgan et Mathys peuvent-ils réellement consacrer à GianLuca Carlone, compte tenu des 22 dépôts, 24 périmètres, films Marwin Studio, projets OLSEN, Shelby et autres (`pilotage-extraits-carlone.md:18` ; `note-point-4-novembre-et-activites.md:15-17`) ?
12. Eaglemic (Michael Bach) est-il associé de Marwin Tech ? Quel est son rôle, et a-t-il des droits sur les outils (console, pipelines) ?
13. Sur quelles hypothèses reposent les « 3 660 € nets » et les « 7 500 € nets » (statut, cotisations, IS, frais, réserve) ?
14. Que contient « outils compris » dans le taux de 750 € : quels abonnements IA, à quel coût mensuel, sur quels comptes ? Plusieurs abonnements sont en échec de prélèvement (`note-point-4-novembre-et-activites.md:8`).
15. OLSEN a-t-il déjà vendu et facturé quoi que ce soit ? Avec quel régime de TVA (« confirmer TVA » reste bloquant, `note-point-4-novembre-et-activites.md:9`) ? Quels clients réels sont derrière « ceux de mes clients » (`artifact-olsen-travail-qui-se-repete.txt:59-60`) ?
16. Que contiennent le « Plan des 30 jours » et le placement des 14 risques (`audit-marwin-tech-carlone.md:46`, `:110`) ?
17. Quelle est la source de la statistique « 200 déploiements IA en France » (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:115-117`) ?
18. Les dates de l'AI Act et du « Digital Omnibus » citées par le corpus (`:760-793`) sont-elles conformes au Journal officiel de l'UE au 4 nov. 2026 ?
19. Si Marwin exploite des agents pour GianLuca Carlone, qui sera le « déployeur » au sens de l'article 26 (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:797-802`) ?
20. Le retrait de Medhi et BOJ.ART décidé le 4 nov. vaut-il aussi pour l'accord à trois, la ligne création et l'accès au parc (`audit-marwin-tech-carlone.md:102`) ?
21. Quel gain de temps a été mesuré sur un cas réel (`pilotage-extraits-carlone.md:20` : « Gain de temps à mesurer ») ?
22. Qui exécutera l'administratif sorti du taux (`audit-marwin-tech-carlone.md:100`) : un salarié de GianLuca Carlone ou un prestataire local ? Qui le paie ?

## 6. Par chantier

**1. CRM et développement commercial.**
- L'audit du 2 nov. présente un CRM prêt et autonome sur Firebase : 500 entreprises, 471 numéros, 60 interlocuteurs, 125 fiches, construit sans facture [DR] (`audit-marwin-tech-carlone.md:11`, `:31`, `:35`). Son dépôt est public et contient des données de prospects [DR] (`:15`). L'audit propose de le revendre à d'autres vendeurs de la Nièvre [PR] (`:103`) et d'y relier une téléphonie Ringover ou Aircall [PR] (`:101`).
- Les pages ChatGPT indiquent 500 SIREN au 28 oct., un suivi en service non consulté et aucun fichier vérifié au 25 oct. [DR] (`pilotage-extraits-carlone.md:19` ; `audit-pilotage-extraits-carlone.md:21`). Elles renvoient au référentiel CNIL des activités commerciales (`audit-pilotage-extraits-carlone.md:21`). La prospection est un lot distinct [PR] (`marwin-methode-consulting-audits.md:79`).
- Repères OLSEN : qualification de leads à 150-450 € par mois ; démarchage en marque blanche à 150-450 € par mois plus 1 500-4 000 € de mise en place [DR]. L'appel B2B humain reste hors du régime de consentement des particuliers. Les appels sortants par IA sont à ne pas vendre (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:181-221`, `:322-338`, `:577-596`).

**2. Quali Contact.**
- Rien dans l'audit du 2 nov. [FV].
- Les pages ChatGPT en font la priorité 2 : obtenir le nom et la version du logiciel et de l'extension, la documentation d'échange et la structure du CRM. Critère de réussite : une campagne fictive importée et exportée avec des identifiants stables, une offre versionnée, la gestion des oppositions, des doublons et des conflits, et un retour traçable [PR] (`audit-pilotage-extraits-carlone.md:18`).
- La mission MAR-07 a un « responsable opérationnel à préciser » ; Quali Contact a un « engagement prévu et logiciel à identifier » [DR] (`pilotage-extraits-carlone.md:19`, `:24`). Il faut préciser finalité et responsabilités avant toute donnée réelle [PR] (`audit-pilotage-extraits-carlone.md:21`).
- Le logiciel de Quali Contact est hors d'accès vérifié [DR] (`:11`).

**3. Organisation et pilotage.**
- Méthode complète : Cadrer, Produire, Piloter ; audit en sept étapes ; dossier remis en sept livrables ; quatre voies d'entrée ; cinq états de suivi ; fiche d'entrée vierge [PR] (`marwin-methode-consulting-audits.md:19-103`).
- L'audit du 2 nov. propose un bon de commande mensuel à trois priorités, un bilan au mois 3 et une répartition écrite des jours de Mathys [PR] (`audit-marwin-tech-carlone.md:57`, `:62`, `:97`). Le plan à 30 jours n'est pas lisible [IN].
- Page de pilotage : huit missions MAR-01 à MAR-08, console à huit vues [DR] (`pilotage-extraits-carlone.md:11-20`).
- Repères OLSEN : le devis, la promesse et le refus se délèguent mal [PR] (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:698-712`) ; un reporting se vend en complément, entre 500 et 4 000 € [DR] (`:600-613`).

**4. Jarvis, mémoire et automatisations.**
- Le mot « Jarvis » n'apparaît dans aucune de mes pièces [FV].
- Pages ChatGPT : reprise entre sessions et appareils sans doublon [PR] (`audit-pilotage-extraits-carlone.md:19`) ; console, journal, atelier « Reverse API Engineer » à réserver aux lacunes d'un connecteur officiel ; « cœur local et machines restent à raccorder » [DR] (`pilotage-extraits-carlone.md:17-18`). Règles qualité : cas d'échec, coût par résultat accepté, essais refaits à chaque changement de modèle [PR] (`marwin-methode-consulting-audits.md:69-73`).
- Corpus OLSEN :
  - assistant documentaire à 10-50 k€ de construction et 1-3 k€ par mois, avec quatre motifs de refus [DR] (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:555-573`) ;
  - le « 100 % autonome » ne tient pas [DR] (`:731-734`) ;
  - un petit modèle exécute, un gros modèle juge [PR] (`:854-859`) ;
  - déployeur au sens de l'article 26 [DR] (`:795-805`) ;
  - risque d'un coût d'inférence sous-estimé dans un abonnement à prix fixe [DR] (`:686`).

**5. Marketing et contenus.**
- Les productions marketing forment un lot distinct [PR] (`marwin-methode-consulting-audits.md:79`).
- L'audit du 2 nov. propose une grille de relecture des messages de vente [PR] (`audit-marwin-tech-carlone.md:99`).
- Le compte Instagram « Marwin Studio » sert Marwin, pas GianLuca Carlone ; aucune publication automatique [DR] (`pilotage-extraits-carlone.md:16`).
- Repères OLSEN : réseaux sociaux à 600-1 500 € par mois ; vidéo IA seulement en option, à signaler au titre de l'article 50 ; publicité à 15-20 % du budget ; site à 800-2 500 € [DR] (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:351-451`).

**6. Galerie, œuvres et artistes.**
- L'audit du 2 nov. relève le risque du discours « défiscalisation », avec ses aspects fiscal et AMF [HY] (`audit-marwin-tech-carlone.md:58`, `:99`).
- Il signale aussi que les œuvres robotisées peuvent sortir de la définition fiscale de l'œuvre d'art ; parade : vente par la galerie, rescrit si besoin [HY] / [PR] (`:61`).
- Il prévoit des démonstrations robotisées en galerie derrière une protection [PR] (`:59`).
- Rien sur la provenance, l'authenticité ou les droits des artistes.

**7. Événements et vernissage.**
- Seules mentions : les « séjours des invités » font partie de l'administratif à sortir du taux [PR] (`audit-marwin-tech-carlone.md:83`, `:100`) ; les données des invités entrent dans la clause RGPD [PR] (`:98`).
- Le vernissage « Strates » (proposé le 4 nov.) est postérieur à toutes mes pièces : rien.

**8. Cabaret et autres lieux.**
- Les « lieux culturels » restent des lots distincts [PR] (`marwin-methode-consulting-audits.md:79`) ; les « chantiers culturels [sont] conservés » [DR] (`pilotage-extraits-carlone.md:24`).
- Les bureaux proposés par GianLuca Carlone entraînent un risque de requalification [HY] (`audit-marwin-tech-carlone.md:40`, `:56`).
- Rien sur le cabaret.

**9. Medhi et BOJ.ART.**
- Selon l'audit du 2 nov., « Medhi crée » ; « Carlone a racheté l'affaire de Medhi » [DR] ; il propose un accord à trois (rôles, droits, partage des ventes, accès au parc) et relève un risque de désaccord sur STRATES [PR] (`audit-marwin-tech-carlone.md:26`, `:38`, `:40`, `:65`, `:102`).
- Le nom « BOJ.ART » n'apparaît dans aucune de mes pièces [FV].
- Décision orale de retrait du 4 nov. [DR] (`note-point-4-novembre-et-activites.md:25`).

**10. STRATES, Éclosion et créations.**
- Ligne création : « audit favorable à un banc d'essai ; rien de mesuré » [DR] (`audit-marwin-tech-carlone.md:19`). Accord à trois à signer avant l'œuvre pilote [PR] (`:65`). Source : « STRATES : verdict de l'audit (2 novembre 2026) » (`:116`), non lue ici.
- Éclosion : rien.
- Les films de Marwin Studio (R01, R02) sont des créations de Marwin, non approuvées, et sans lien établi avec GianLuca Carlone [DR] (`pilotage-extraits-carlone.md:13-16`).

**11. Laboratoire IA et robotique.**
- Robot près du public : films et démonstrations derrière une protection [PR] (`audit-marwin-tech-carlone.md:59`).
- Le matériel garde son propre budget [PR] (`marwin-methode-consulting-audits.md:25`) ; « ni matériel » n'est acté et les machines sont hors d'accès [DR] (`pilotage-extraits-carlone.md:18`, `:20` ; `audit-pilotage-extraits-carlone.md:11`).
- Le corpus OLSEN classe les machines dans l'annexe I de l'AI Act (2 août 2028), « hors périmètre OLSEN » [DR] (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:791-793`).
- Aucune mention de DGX Spark.

## 7. Erreurs d'identité

Cinq occurrences de « John-Lucas » [sic, lire GianLuca], toutes dans les pages ChatGPT :
- `sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md:81` : « la décision que John-Lucas [sic, lire GianLuca] doit pouvoir prendre » ;
- `sources/chatgpt-pages/2026-11-04-complement/audit-pilotage-extraits-carlone.md:5` : en-tête de collecte (le nom sert ici de clé de recherche) ;
- `sources/chatgpt-pages/2026-11-04-complement/pilotage-extraits-carlone.md:5` : en-tête de collecte (clé de recherche) ;
- `sources/chatgpt-pages/2026-11-04-complement/pilotage-extraits-carlone.md:9` : « le dossier John-Lucas [sic, lire GianLuca] Carlone » ;
- `sources/chatgpt-pages/2026-11-04-complement/pilotage-extraits-carlone.md:24` : titre de page « John-Lucas [sic, lire GianLuca] Carlone Offre et projets en Nièvre ».

Aucune occurrence de « John Lucas » ni d'autre variante. L'audit du 2 nov. n'emploie que « Carlone ». Les deux artefacts OLSEN ne citent pas le client. Aucune pièce n'emploie « GianLuca ». Les mêmes erreurs figurent dans les fichiers .json voisins, non comptés ici.

## 8. Instructions trouvées dans les pièces

Aucune de ces instructions n'a été exécutée. Aucune ne cherche à détourner un assistant (pas d'injection), mais plusieurs demandent des actions extérieures.

| Pièce | Texte ou demande | Destinataire apparent |
| --- | --- | --- |
| `marwin-methode-consulting-audits.md:81` | « Prochaine action : préparer la fiche d'entrée du premier audit… » | Assistant ChatGPT ou Morgan |
| `marwin-methode-consulting-audits.md:83-103` | Fiche d'entrée « à renseigner » | Morgan ou l'assistant |
| `audit-pilotage-extraits-carlone.md:17-19` | « Travail suivant » : fixer avec Mathys qui fait quoi ; obtenir le logiciel de Quali Contact ; choisir l'environnement d'exécution | Morgan ou l'assistant |
| `audit-pilotage-extraits-carlone.md:21` | « Avant les données de prospection réelles, préciser finalité… » | Morgan ou l'assistant |
| `pilotage-extraits-carlone.md:13-20` | Colonne « Prochaine action » : « Recueillir le retour… », « Réserver RAE… », « Ouvrir Offres et missions pour le premier cadrage ; exporter le suivi utile », « Obtenir le logiciel/module… », « Convenez des responsabilités… » ; interdiction : « Aucun appel supplémentaire ou publication autorisé » (`:15`), « aucune date ou publication automatique » (`:16`) | Sessions ChatGPT et Morgan |
| `audit-marwin-tech-carlone.md:21-27`, `:91-104` | Cinq décisions et douze solutions : « Passer le dépôt du CRM en privé aujourd'hui », immatriculer, signer, souscrire une RC Pro, demander un rescrit, etc. | Morgan, Mathys, expert-comptable |
| `artifact-olsen-travail-qui-se-repete.txt:119-151` | Formulaire de contact pour les visiteurs (« Dites-moi ce qui vous prend du temps ») et champ piège anti-robot « Ne rien écrire ici » (`:142`) | Visiteurs du site. Rien n'a été envoyé. |
| `artifact-corpus-offres-ia-vendables-2026-08-20.txt` | Règles internes (« Ne jamais vendre… », « réduire le volume — jamais le critique ») | Morgan, pour ses ventes. Règles de doctrine, sans action demandée. |

## 9. Points d'audit

**Ce que l'audit du 2 novembre a conclu.**
- L'offre « tient ».
- Trois risques sont à traiter avant de signer : la société, les données et le contrat.
- Le taux de 750 € se défend pour le cœur de l'offre, mais pas pour l'administratif.
- Le revenu dépend du volume, pas du taux.
- Douze solutions sont listées, dont quatre préalables à la première facture.
- Sources : `audit-marwin-tech-carlone.md:7`, `:44`, `:69`, `:84`, `:89`.

**Ce qu'il n'a pas examiné.**
- Pas de contrat, de comptabilité ni d'échange avec GianLuca Carlone : limite déclarée (`:121`).
- Pas de vérification du besoin réel de GianLuca Carlone, ni des acheteurs, signataires et payeurs.
- Pas de modèle de charge ni de disponibilité réelle des associés (seul le temps de Mathys est noté « non fixé », `:62`).
- Rien sur Quali Contact, Jarvis, le premier forfait de cadrage ou Eaglemic.
- Rien sur la TVA, la propriété du CRM et des développements, ni la maintenance.
- Pas de coût des outils IA, alors que le taux est « outils compris ».
- Pas de gains mesurés.
- Pas d'option de facturer par l'entreprise existante de Morgan.
- Rien sur le calendrier de paiement au-delà de « mois payés d'avance ».
- Rien sur la responsabilité de « déployeur » au sens de l'AI Act.

**Raisonnements faibles et affirmations à requalifier.**
1. **« Prix et paiement : Solide »** (`audit-marwin-tech-carlone.md:12`). Le prix et l'avance sont des propositions [PR] que personne n'a acceptées. Un prix non accepté ne peut pas être « solide ».
2. **« Valeur déjà livrée : Solide »** (`:11`). La livraison n'est pas réceptionnée et l'usage n'est pas constaté (`pilotage-extraits-carlone.md:19`). Le CRM a été fait gratuitement et ses données sont publiques. Sa propriété n'est pas réglée. Selon la méthode de Marwin elle-même, la clôture exige « l'acceptation du livrable [et] la passation » (`marwin-methode-consulting-audits.md:65`).
3. **Justification du taux de 750 €.** Elle repose sur une source secondaire et sur une fourchette « IA » sans médiane (`audit-marwin-tech-carlone.md:77`, `:80`). Le taux dépasse de 19 à 26 % les médianes de chef de projet et de consultant [ES]. Aucune vente antérieure de Morgan à ce niveau de prix n'est documentée : les offres OLSEN vont de quelques centaines d'euros à 12 000 € (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:76-111`), et aucune proposition OLSEN n'a été envoyée (`note-point-4-novembre-et-activites.md:9`). Un contrat de 90 000 € HT sur six mois serait la première vente du binôme à cette échelle.
4. **Huit propositions pour 20 journées.** C'est la situation que le corpus OLSEN qualifie de « marge nulle » (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:738-739`). La parade des « trois priorités par mois » ne dit pas ce que vaut une priorité en jours ou en livrables. Il faut reprendre l'architecture de la méthode : Cadrer, Produire et Piloter séparés, chacun avec sa réception (`marwin-methode-consulting-audits.md:19-25`).
5. **Saut d'échelle.** Les pages ChatGPT recommandaient d'abord un forfait de cadrage borné et payé (`marwin-methode-consulting-audits.md:77` ; `audit-pilotage-extraits-carlone.md:17`). L'audit du 2 nov. passe directement à un contrat de six mois. Le besoin de pilotage global n'a donc jamais été testé, ce qu'exige `DEMANDE.md:22`.
6. **Rémunérations simulées sans hypothèses** (`audit-marwin-tech-carlone.md:18`). Doubler le chiffre d'affaires fait passer la part reversée en net de 49 à 50 % seulement : soit le modèle n'a presque pas de coûts fixes, soit les charges croissent avec le volume. Ces hypothèses doivent être explicites. Le même montant de 7 500 € désigne à la fois l'acompte et un revenu net : source de confusion.
7. **Capacité.** Les pièces montrent 22 dépôts et 24 périmètres, des films Marwin Studio, OLSEN, Shelby et d'autres projets (`audit-pilotage-extraits-carlone.md:11`, `:13` ; `note-point-4-novembre-et-activites.md:15-17`). Morgan porte 8 des 12 solutions de l'audit (mon décompte, `audit-marwin-tech-carlone.md:93-104`) et reste le seul validateur (`marwin-methode-consulting-audits.md:15`). C'est un point de dépendance unique non traité.
8. **Deuxième client par revente du CRM** (`audit-marwin-tech-carlone.md:103`). Cela suppose que Marwin détienne les droits sur le code. Les données des prospects de GianLuca Carlone ne doivent jamais être réutilisées. La tâche revient à Mathys, dont le temps n'est pas fixé.
9. **Quali Contact absent de l'audit.** Recommander Ringover ou Aircall (`:101`) sans connaître le logiciel de Quali Contact risque de payer deux outils, ou de court-circuiter le prestataire choisi par GianLuca Carlone.
10. **Medhi.** Les décisions 4 et 10 et l'atout « équipe complémentaire » sont à réviser après le retrait oral du 4 nov. Comme cette décision n'est pas formalisée, il ne faut pas la tenir pour définitive.
11. **Facture électronique** (`audit-marwin-tech-carlone.md:95`). L'audit ne parle que de l'émission en 2027. Selon le calendrier de la réforme connu avant cet audit, la capacité de réception est exigée de toutes les entreprises depuis septembre 2026 [HY]. À vérifier sur service-public.fr. La page citée porte la mention « vérifié le 11 août 2026 », sans revérification le 2 nov.
12. **Données personnelles.** L'audit prévoit la clause de l'article 28 et le registre, mais ne traite ni la base légale de la prospection B2B (référentiel CNIL cité en `audit-pilotage-extraits-carlone.md:21`), ni l'origine des profils LinkedIn, ni la durée de conservation, ni la question de savoir qui est responsable de traitement tant que l'entité de GianLuca Carlone est inconnue.
13. **Reverse API Engineer** (`pilotage-extraits-carlone.md:17`). L'outil existe et il est testé. Pour GianLuca Carlone, il faut l'exclure de toute utilisation sur des services tiers sans autorisation écrite : conditions d'utilisation, responsabilité.
14. **Statistiques non sourcées.** Le corpus OLSEN rejette les chiffres de ROI invérifiables (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:596`, `:751-754`) mais cite lui-même « 200 déploiements », « 88,5 % », « 34 % / 62 % » sans source (`:115-117`, `:734`). Aucun de ces chiffres ne doit entrer dans un document destiné à GianLuca Carlone.
15. **Dates réglementaires du corpus.** Digital Omnibus, tolérance au 2 déc. 2026, annexe III reportée au 2 déc. 2027 (`:760-793`) : rédigées le 20 août, ce sont des déclarations [DR] à vérifier au Journal officiel de l'UE avant toute utilisation.
16. **« Outils compris »** (`audit-marwin-tech-carlone.md:78`). Le corpus cite comme première cause d'érosion d'un prix fixe le coût d'inférence sous-estimé (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:686`). Les abonnements de Morgan sont en échec de prélèvement (`note-point-4-novembre-et-activites.md:8`). Il faut chiffrer et isoler ces coûts.
17. **Option de facturation non examinée.** Morgan a un SIRET (OLSEN). Facturer par cette entreprise exige de vérifier la domiciliation (résiliée), le régime de TVA et les plafonds éventuels. C'est une piste à examiner avec l'expert-comptable, pas une recommandation.
18. **Pages ChatGPT lues en extraits.** Deux des quatre pièces du dépôt ne contiennent que les blocs citant Carlone. Des décisions ou réserves formulées ailleurs dans ces pages peuvent manquer.

**Ce que Morgan a vendu, livré ou seulement préparé (d'après mes pièces).**

| Catégorie | Éléments | Code |
| --- | --- | --- |
| Vendu ou facturé | Rien n'est documenté. « Ceux de mes clients » (`artifact-olsen-travail-qui-se-repete.txt:60`) n'est étayé par aucun nom ni aucune facture. Les sites présentés sont « inventés » (`:59`). | [IN] |
| Livré sans facture | CRM de GianLuca Carlone (`audit-marwin-tech-carlone.md:31`), réception non constatée | [DR] |
| Construit, non prouvé chez un client | Pipelines OLSEN : forge, outreach, régie (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:150`, `:196`, `:368`) ; console Marwin et paquet 0.2.0 (`pilotage-extraits-carlone.md:17-18`) ; films R01 et R02 non approuvés (`:14-15`) | [DR] |
| Seulement préparé | Corpus de 25 offres ; scripts d'appel (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:219`) ; 36 propositions et 72 brouillons non envoyés ; 503 prospects non contactés (`note-point-4-novembre-et-activites.md:9`) ; méthode de consulting et forfait de cadrage sans prix (`marwin-methode-consulting-audits.md:77-79`) ; page commerciale OLSEN en aperçu, avec un domaine suspendu depuis le 3 oct. (`artifact-olsen-travail-qui-se-repete.txt:6`, `:125` ; `note-point-4-novembre-et-activites.md:7`) | [FV] pour l'état des pièces, [DR] pour le reste |

**Leçons applicables à GianLuca Carlone, tirées de ces pièces.**
1. Commencer par un cadrage payé et borné, avec une décision à rendre possible, avant tout contrat de capacité (`marwin-methode-consulting-audits.md:25`, `:43`, `:77`).
2. Borner chaque forfait par un nombre de livrables, et pas seulement de jours. Séparer Produire, les créations et la recherche (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:738-739` ; `marwin-methode-consulting-audits.md:79`).
3. Mettre la supervision humaine dans le contrat : validation par GianLuca Carlone ou son délégué, taux d'escalade défini, aucune dépense ni publication sans accord, garde-fous techniques (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:119-121`, `:435-459`, `:527-528` ; `pilotage-extraits-carlone.md:15-16`).
4. Ne vendre comme opérationnel qu'un connecteur éprouvé en environnement réel. Mesurer le temps total corrections comprises et le coût par résultat accepté (`marwin-methode-consulting-audits.md:63`, `:69`).
5. Pour la mémoire documentaire (Jarvis), appliquer les critères de refus de l'assistant documentaire : documentation fiabilisée, droits d'accès, savoir non seulement oral. Budgéter à part, sur des repères de 10 à 50 k€ de construction (`artifact-corpus-offres-ia-vendables-2026-08-20.txt:559-571`).
6. Prévoir la clause de déployeur (AI Act, article 26) et l'étiquetage des contenus générés (article 50) pour les visuels et films faits pour GianLuca Carlone (`:333`, `:407-408`, `:797-802`).
7. Reconnaître que la contrainte de Morgan est commerciale et relationnelle, pas productive (`:710-712` ; `note-point-4-novembre-et-activites.md:9`). Démultiplier la production ne crée pas de chiffre d'affaires si personne ne relance, ne vend et ne réceptionne.
8. Arrêter le travail gratuit préalable et régler le statut du CRM déjà fourni : facture, cession ou licence (`audit-marwin-tech-carlone.md:31`, `:54`).
