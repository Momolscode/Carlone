# Lecteur C6-catalogue : catalogue des offres de GianLuca Carlone et dossier « Partenariats Vieux Relais & le M »

Lecture faite le 4 novembre 2026, en lecture seule, sur le dépôt `Momolscode/Carlone` (branche main, commit 7b46602). Aucun site extérieur n'a été consulté : les pages officielles citées par les pièces (BOFiP, AMF, Légifrance) n'ont **pas** été rouvertes. Quand j'ajoute une remarque fiscale ou juridique tirée de mes propres connaissances, je la marque « à revérifier ».

Abréviations utilisées dans les citations :
- **CAT** = `interne/offres-de-carlone-catalogue-crm.md` (citée par ligne, ex. CAT:9) ;
- **DPV** = `sources/dossier-partenariats-vieux-relais-et-le-m-2026-10-21.pdf` (cité par page, ex. DPV p. 32) ;
- pièces hors lot, consultées seulement sur des lignes précises pour situer : `crm/PASSATION.md` (PASS), `interne/contexte-projet-carlone.md` (CTX), `sources/crm-reference-2026-11-04.md` (CRMREF), et la note de l'auditeur `note-point-4-novembre-et-activites.md` (NOTE).

---

## 1. Pièces lues

| Chemin | Date de la pièce | Nature et auteur | Original ou copie/export | Ce qui n'a pas pu être lu |
| --- | --- | --- | --- | --- |
| `interne/offres-de-carlone-catalogue-crm.md` (140 lignes, lu en entier) | 2 nov. 2026 (CAT:3). Versée au dépôt le 4 nov. 2026 à 16:38 (commit fa5998a) | Document interne « Offres de Carlone — catalogue pour le CRM », signé « @Olsen Morgan » (CAT:3). Il tire ses informations sur le client des « Messages de Morgan du 2 novembre 2026 » (CAT:140) et du dépôt FinanceScope/CRM-Carlone au commit b53a81c (CAT:139). Mise en forme typique des documents claude.ai : rédaction probablement assistée par IA [HY] | Export Markdown d'un artefact claude.ai privé « Offres de Carlone — catalogue CRM (2 nov.) » (NOTE:13). C'est donc une copie, pas l'original | Le schéma intégré « Parcours d'une vente · 7 étapes, 1 alerte » n'a pas été exporté (CAT:73) : les sept étapes et l'alerte sont inconnues. Les pages BOFiP et AMF citées (CAT:134-137) n'ont pas été rouvertes. Le dépôt FinanceScope (CAT:81, 139) est hors de mon accès (NOTE:23) |
| `sources/dossier-partenariats-vieux-relais-et-le-m-2026-10-21.pdf` (34 p. A4, lu en entier via le texte extrait `sources-txt/sources__dossier-partenariats-vieux-relais-et-le-m-2026-10-21.txt` ; contrôle visuel des p. 22, 26 et 33) | 21 oct. 2026 (DPV p. 1). Métadonnées : créé le 21 oct. 2026 à 18:30:20 UTC par Chromium (Skia/PDF m153), jamais modifié. Versé au dépôt le 4 nov. 2026 (commit fa5998a) | Dossier « Partenariats entreprises Nièvre – Le Vieux Relais & le M », signé « @Mathys » (DPV p. 1). Impression d'une page web au même format que le catalogue : production probablement assistée par IA [HY]. Le dossier ne nomme jamais GianLuca Carlone, Morgan ni Marwin Tech | Fichier PDF original tel que versé (aucune image ; 47 liens hypertextes) | Rien d'illisible. Les 47 liens (23 sites d'entreprises, Pappers, annuaire-entreprises.data.gouv.fr) n'ont pas été suivis. L'extraction texte place les titres de section en haut de page (p. 22, 25, 26, 28, 31) alors que le PDF les met en bas de page : l'ordre des tableaux est correct dans le PDF. La page web d'origine n'est pas archivée |

**Pièces hors lot consultées ponctuellement (lignes précises, pour situer seulement)** : PASS:3-7, 35, 41, 45, 49-51, 56 ; CTX:5, 24, 43-47, 149, 160 ; CRMREF:3-12 ; NOTE:13, 23, 25-26. Elles ne sont pas analysées en entier.

---

## 2. Affirmations déterminantes

**Ce que mes pièces disent des activités de GianLuca Carlone et des entités.** Tout ce qui le concerne dans le catalogue repose sur des messages de Morgan (CAT:140) : marchand d'art venu de l'avenue Montaigne, six bâtiments rachetés, galerie en 2027, ventes d'œuvres « avec un avantage fiscal ». Le dossier de Mathys parle d'un bar (le Vieux Relais) et d'un restaurant (le M) à Cosne-Cours-sur-Loire qui « changent de main », sans dire qui les reprend. **Aucune entité juridique n'est nommée dans les deux pièces** : ni la structure qui détient les lieux, ni celle qui vendra les œuvres (CAT:90, 119), ni Marwin Tech.

| N° | Affirmation | Code | Source | Remarque |
| --- | --- | --- | --- | --- |
| 1 | GianLuca Carlone est un « marchand d'art venu de l'avenue Montaigne à Paris » | [DR] | CAT:9 ; source déclarée CAT:140 | Aucune pièce primaire (extrait Kbis, site, facture) dans mon lot |
| 2 | « Carlone vend des œuvres d'art avec un avantage fiscal » | [DR] | CAT:7 | Le même document demande : « Vend-il déjà à Paris avec cet argument ? » (CAT:124). Le fait n'est donc pas établi |
| 3 | Il « a déjà racheté six bâtiments » | [DR] | CAT:9 | Quels bâtiments, où, par quelle entité, financés comment : [IN] |
| 4 | Il « ouvrira une galerie en 2027 » | [DR] | CAT:9 | Bâtiments, dates et public restent des questions ouvertes (CAT:127) |
| 5 | Il propose des bureaux et « une bonne rémunération », et « envisage d'investir » dans l'activité de Morgan et Mathys | [DR] | CAT:9 | Aucun montant, aucune forme, aucun écrit |
| 6 | « Morgan et Mathys lui ont construit un CRM » | [DR] | CAT:9 | Le code existe (copie dans `crm/`, CRMREF:10), mais ni sa réception par GianLuca Carlone ni son usage réel ne sont prouvés |
| 7 | Le Vieux Relais et le M sont « le bar et le restaurant qui changent de main à Cosne-Cours-sur-Loire » ; message type : « Nous reprenons le Vieux Relais et le M » | [DR] | DPV p. 32 | Le repreneur n'est pas nommé. Les deux pièces ne disent pas que les lieux appartiennent à GianLuca Carlone (voir aussi CTX:160) |
| 8 | Le M est le restaurant, le Vieux Relais le bar (« le midi au M, afterwork au Vieux Relais » ; vins « à la carte du M et au verre au Vieux Relais ») | [DR] | DPV p. 2, 6, 29 | Contredit par PASS:41 (voir section 4) |
| 9 | Les deux établissements vont rouvrir après travaux (« flyers de réouverture », « pack d'annonces pour la réouverture », « déco rénovée du Vieux Relais », « travaux du bar et du restaurant ») | [DR] | DPV p. 3, 5, 23, 29 | Date de reprise et de réouverture : [IN] |
| 10 | Le nom de la structure qui vend les œuvres n'est pas décidé : le CRM le laisse « à compléter » dans chaque mail | [FV] | CAT:90, 119 | Aucun contrat de vente ni de démarchage ne peut être signé tant que ce point reste ouvert |
| 11 | Aucune des deux pièces ne mentionne Marwin Tech, une rémunération de Morgan ou de Mathys, ni la personne qui paie ces travaux | [FV] | CAT entier ; DPV p. 1-34 | Le catalogue et le dossier sont des livrables sans commande ni prix connus |
| 12 | Article 238 bis AB du CGI : une entreprise qui achète une œuvre originale d'artiste vivant et l'expose au public déduit son prix sur cinq ans ; le dispositif vaut pour les achats faits avant le 31 déc. 2028, prolongation due à l'article 89 de la loi de finances pour 2026 | [DR] | CAT:17, 135 | Non rouvert. D'après mes connaissances antérieures, le dispositif courait jusqu'au 31 déc. 2025 : la prolongation est à revérifier sur Légifrance |
| 13 | Le dispositif vise les sociétés à l'IS (de plein droit ou sur option) et les sociétés de personnes ; les professions en BNC sont exclues | [DR] | CAT:21 (BOFiP § 5) | À revérifier ; détermine quelles entreprises du CRM peuvent être ciblées |
| 14 | L'œuvre doit être originale au sens de l'article 98 A, II de l'annexe III du CGI, d'un artiste vivant au jour de l'achat, et inscrite à l'actif immobilisé, jamais en stock | [DR] | CAT:22-23 | Conditions reprises du BOFiP selon l'auteur |
| 15 | Déduction d'un cinquième du prix par an, sur l'exercice d'achat et les quatre suivants, sans prorata ; frais accessoires exclus | [DR] | CAT:24 | Si le « suivi sur cinq ans » est inclus dans le prix de l'œuvre (CAT:45), il gonfle la base déductible : risque de remise en cause |
| 16 | Plafond annuel : 20 000 €, ou 5 ‰ du CA HT si c'est plus, moins les dons de mécénat de l'année ; l'excédent est perdu | [DR] | CAT:25 | Le plafond est commun à toutes les œuvres en cours de déduction. Le tableau CAT:58-63 suppose une seule œuvre et aucun autre achat sur cinq ans |
| 17 | Le montant déduit doit être placé dans une réserve spéciale au passif ; vente, arrêt d'exposition ou prélèvement sur la réserve entraînent une réintégration immédiate | [DR] | CAT:26, 28 | Obligation comptable chez l'acheteur, hors du contrôle du vendeur |
| 18 | Exposition gratuite dans un lieu accessible au public ou aux salariés, jamais un bureau, pendant cinq exercices, avec information du public | [DR] | CAT:27 | Base de l'offre 4 (suivi) |
| 19 | Une peinture doit être « exécutée entièrement à la main » ; la doctrine exclut « tout procédé [...] permettant de suppléer, en tout ou en partie, à cette intervention humaine » | [DR] | CAT:30 ; source CAT:136 | La source est une fiche archivée de 1995, « à confirmer sur le texte en vigueur » (CAT:136) |
| 20 | Fonte limitée à 8 exemplaires, photographie à 30 exemplaires signés et numérotés | [DR] | CAT:30, 138 | « Relevés dans des sources secondaires, à vérifier sur Légifrance » (CAT:138). Les autres catégories de l'article 98 A (gravures, tapisseries, céramiques, etc.) ne sont pas traitées (à revérifier) |
| 21 | Le titre de section annonce « Le cadre fiscal vérifié » | [FV] | CAT:15 | Surévaluation : deux éléments clés sont déclarés non vérifiés (CAT:136, 138) |
| 22 | Au taux normal de l'IS de 25 %, 20 000 € déduits économisent 5 000 € ; au taux réduit de 15 %, 3 000 € | [ES] | CAT:32 | Calcul juste, mais le taux de 15 % ne s'applique qu'à la première tranche de bénéfice d'une PME éligible (plafond de 42 500 € selon mes connaissances, à revérifier). L'économie réelle dépend du bénéfice de chaque client |
| 23 | Les particuliers ne sont pas concernés : on leur vend une œuvre sans argument de défiscalisation | [PR] | CAT:34 | Règle saine, reprise dans l'offre 9 |
| 24 | Le document « n'est pas un conseil fiscal » ; chaque offre doit être validée par l'expert-comptable ou l'avocat fiscaliste de GianLuca Carlone avant d'être vendue | [PR] | CAT:13 | Aucune validation n'est documentée [IN] ; le conseil n'est pas identifié (CAT:123) |
| 25 | Neuf offres en quatre familles ; une seule (l'œuvre exposée) est déjà dans le CRM, avec simulation et mémo d'appel | [PR] / [DR] | CAT:38 | Six offres sont « à construire » et deux « pour 2027 » (CAT:42-50) |
| 26 | Offre 1 « Œuvre exposée » : prix de l'œuvre « au plus cinq fois le plafond annuel du client » | [PR] | CAT:42 | Prix calé sur la capacité fiscale de l'acheteur, pas sur la valeur de l'œuvre (voir section 9) |
| 27 | Offre 2 « Collection d'entreprise » : grands comptes dont le plafond dépasse 20 000 €, « soit plus de 4 M€ de CA », trois à cinq œuvres | [PR] | CAT:43 | Seuil juste (20 000 € / 0,005 = 4 M€) |
| 28 | Offre 3 « Commande sur mesure » : devis de l'artiste, acompte, solde à la livraison ; déduction « si l'œuvre est originale au sens fiscal » | [PR] | CAT:44 | Dépend de l'artiste et de la technique |
| 29 | Offre 4 « Suivi sur cinq ans » : information du public, photo datée, attestation pour l'expert-comptable, rappel de la réserve, alerte en cas de déménagement ; forfait annuel ou inclus dans le prix | [PR] | CAT:45 | Qui signe l'attestation et en répond en cas de contrôle : [IN] |
| 30 | Offre 5 « Vernissage en entreprise » : soirée avec l'artiste chez le client, invitations envoyées depuis le CRM, forfait par événement | [PR] | CAT:46 | Une soirée ne prouve pas cinq ans d'exposition ; envoi d'invitations à des prospects depuis le CRM soumis aux règles de prospection |
| 31 | Offre 6 « Programme artistes » : 97 artistes « déjà repérés dans l'onglet Culture » ; convention de dépôt, assurance, commission sur vente, « jamais de loyer facturé à l'artiste » | [PR] / [DR] | CAT:47 | Taux de commission non fixé. Le chiffre 97 désigne ailleurs des « prospects » (CTX:43) ou « artistes, associations, lieux et réseaux » (PASS:56) |
| 32 | Offre 7 « Cercle des collectionneurs fondateurs » (adhésion ou gratuit, à décider) et offre 8 « Privatisation et événements » dans la galerie et les bâtiments, toutes deux « pour 2027 » | [PR] | CAT:48-49 | Dépendent de lieux non désignés et d'un calendrier inconnu |
| 33 | Offre 9 « Collectionneur particulier » : conseil, sélection, livraison, certificat d'authenticité | [PR] | CAT:50 | Qui délivre le certificat, sur quelle provenance : [IN] |
| 34 | « Les prix ne sont pas fixés ici : ils dépendent des œuvres et des artistes que Carlone réunira » | [IN] | CAT:52 | Aucun stock d'œuvres ni aucun artiste engagé n'est documenté |
| 35 | Règle déjà inscrite dans le CRM : les textes destinés aux entreprises ne citent ni le Vieux Relais ni le M | [DR] | CAT:52 ; PASS:49 | Inverse exact du dossier du 21 oct., entièrement rédigé au nom de ces lieux (DPV p. 32-33) |
| 36 | Exemple : une PME de 2 M€ de CA déduit jusqu'à 20 000 €/an ; une œuvre de 30 000 € coûte net 22 500 € à 25 % (économie de 7 500 €), ou économise 4 500 € à 15 % | [ES] | CAT:56, 65 | J'ai refait les calculs : ils sont justes. Ils supposent une entreprise bénéficiaire, sans don ni autre œuvre (CAT:67) |
| 37 | « Déjà en place » : 500 entreprises de la Nièvre classées en vagues, calculs de plafond, simulation à trois prix, mémo d'appel, note pour l'expert-comptable, refus de prospection, onglet Culture, « liaison avec Hermes360 », version autonome sur Firebase | [DR] | CAT:81 | Non vérifié dans mon lot. « Liaison avec Hermes360 » est contredite par CRMREF:10-12 (présence en branche ≠ raccordement) |
| 38 | À ajouter au CRM : fiches Offre, Œuvre et Vente, tâches annuelles automatiques, alertes de réintégration et de fin de période | [PR] | CAT:85-89 | Développement non chiffré : qui le paie, qui le maintient pendant cinq ans : [IN] |
| 39 | « La vente n'est que la quatrième étape sur sept : la valeur du CRM est dans les cinq années de suivi » | [HY] | CAT:71 | Thèse commerciale non testée ; elle suppose des ventes qui n'existent pas encore |
| 40 | « À la fin des cinq ans, le client a déjà l'habitude d'acheter : c'est le moment de proposer une nouvelle œuvre » | [HY] | CAT:75 | Aucune donnée de réachat |
| 41 | Le dépôt FinanceScope/CRM-Carlone est public ; sa branche de travail contient 931 numéros de téléphone, 206 adresses e-mail, 63 fichiers de profils LinkedIn de décideurs, la stratégie commerciale et le rapport destiné à GianLuca Carlone | [DR] | CAT:96 | Constat du 2 nov., non revérifié ici. Toujours public le 4 nov. à 16 h 19 selon CTX:5. Copie complète aussi dans `crm/` du dépôt Carlone (CRMREF:10) |
| 42 | Mettre en avant un rendement, proposer une reprise avec revalorisation ou gérer les œuvres pour le client fait entrer l'offre dans le régime des intermédiaires en biens divers : dossier préalable à l'AMF et contribution de 8 000 € | [DR] | CAT:97, 137 | Montant et critères à revérifier sur le site de l'AMF |
| 43 | En cas de doute (impression 3D, peinture au robot, procédé numérique), ne pas promettre la déduction et demander d'abord un rescrit | [PR] | CAT:98 | Garde-fou essentiel pour STRATES et l'atelier |
| 44 | Exposer dans un lieu tiers (« la galerie ou un établissement de Carlone ») une œuvre achetée par une entreprise « n'est pas explicitement prévu par le BOFiP : à faire valider » | [DR] | CAT:99 ; PASS:35 (« piste du Vieux Relais ») | Point juridique majeur, voir section 9 |
| 45 | Vente hors établissement à une entreprise de 5 salariés au plus : délai de rétractation et aucun paiement avant 7 jours ; « le CRM l'affiche déjà » | [DR] | CAT:101 | Règle à revérifier (Code de la consommation) ; affichage dans le CRM non vérifié |
| 46 | Prospection : respect des oppositions, « STOP », coordonnées professionnelles publiées uniquement, « règles déjà en place dans le CRM » | [DR] | CAT:102 | Le dossier du 21 oct. ne mentionne aucune de ces règles (DPV p. 32-34) |
| 47 | Pièces de BOJ.ART faites entièrement à la main par Medhi : utilisables pour les offres 1 à 3 ; pièces imprimées en 3D ou peintes par le bras robotisé, dont STRATES : « très probablement » exclues de l'avantage fiscal | [HY] | CAT:106-109 | Raisonnement prudent, fondé sur la doctrine archivée de 1995 (CAT:136) |
| 48 | « Conséquence pour STRATES : sa valeur est artistique et d'image, pas fiscale » ; l'échantillon peint à la main par Medhi peut être proposé aux entreprises | [PR] | CAT:110 | Le catalogue n'a pas été mis à jour après le retrait de Medhi/BOJ.ART de l'offre Marwin le 4 nov. (NOTE:25) |
| 49 | Une commande sur mesure signée dans le CRM peut ouvrir un dossier dans le Jarvis de l'atelier ; les deux outils échangent la commande, « pas leurs données clients » | [PR] | CAT:111 | Aucune interface ni règle d'accès décrite |
| 50 | « Dix réponses suffisent pour transformer ce catalogue en offres vendables » | [HY] | CAT:117-128 | Il manque au moins la TVA applicable, l'assurance, le stock d'œuvres et la validation fiscale écrite |
| 51 | Objectif du dossier du 21 oct. : faire des plus grosses entreprises de la Nièvre des « clients réguliers du Vieux Relais et du M » en testant 5 types de partenariats et en gardant ceux qui accrochent | [PR] | DPV p. 1 | Démarche de test, pas d'offre figée : bonne posture |
| 52 | Base : classement Pappers des 100 premières entreprises de la Nièvre par chiffre d'affaires, « édité le 02/09/2026 » ; chaque entreprise a été recherchée (commune, activité, distance de Cosne, interlocuteur, idée sur mesure) | [DR] | DPV p. 1, 34 | Méthode déclarée. Aucun chiffre d'affaires ni résultat n'est reproduit dans le dossier |
| 53 | 15 entreprises en priorité A, dont 12 à Cosne même ou avec un site à Cosne | [FV] | DPV p. 2-3 | Recompté : 15 lignes, 12 à Cosne, plus Pouilly, Donzy et Varennes-Vauzelles |
| 54 | 7 secteurs : industrie 27 (3 A), automobile 13 (3 A), commerce 28 (3 A), bois-BTP 16 (1 A), transport 7 (1 A), santé 4 (2 A), vins-sport-médias 5 (2 A) | [FV] | DPV p. 4, 11, 18, 22, 25, 26, 28 | Total recompté : 100 entreprises et 15 A, cohérents avec la synthèse |
| 55 | Les groupes sont approchés en une seule fois (Vincent n° 3, 16, 29, 37 ; SUMA n° 19, 43, 69 ; Rousseau n° 9, 14, 82) ; les holdings passent par leur filiale | [FV] | DPV p. 11, 25, 31 | Évite les doublons de démarchage |
| 56 | Entreprises en procédure collective signalées et écartées des comptes et du crédit : Premester (liquidation, 19/07/2024), Pobi Structures (sauvegarde, 01/08/2024), CFP (redressement, 02/02/2026) | [DR] | DPV p. 8, 23, 31 | Dates issues de Pappers, non revérifiées. Prudence financière utile |
| 57 | Les distances sont des « estimations routières » ; les éléments « non confirmé » ou « à vérifier » n'ont pas pu être recoupés | [FV] | DPV p. 2, 34 | Limites déclarées honnêtement |
| 58 | Des dirigeants sont nommés (DG de Command-SMFI, DG de Soyez Frères) | [DR] | DPV p. 4, 5 | Données personnelles issues de registres publics : à traiter selon le RGPD |
| 59 | Liens vers 23 sites d'entreprises (sur 100), plus Pappers et l'annuaire des entreprises de l'État | [FV] | DPV, annotations du PDF (mon décompte) | Environ trois quarts des fiches n'ont pas de lien de vérification |
| 60 | Trois messages types et un script d'appel au standard ; capacité, remise et dates restent entre crochets, « chiffres à fixer ensemble au rdv » | [PR] | DPV p. 32-33 | L'offre de base n'existait pas le 21 oct. |
| 61 | Le message à la direction affirme « Il reste des dates en décembre » et propose des groupes « jusqu'à [X] personnes, avec privatisation » | [PR] | DPV p. 32 | Engagement de disponibilité sans lieu rouvert ni capacité connue |
| 62 | « La fenêtre la plus rentable se trouve maintenant : les repas de fin d'année se réservent entre fin octobre et mi-novembre » | [HY] | DPV p. 33 | Aucune source. Au 4 nov., cette fenêtre se referme |
| 63 | Plan : au « rdv de demain » (22 oct.), fixer l'offre, répartir les secteurs entre deux « associés », valider 15 à 20 cibles ; semaines 1 à 4 ; relance à J+5 puis J+12 ; bilan des réponses, rendez-vous et réservations | [PR] | DPV p. 33-34 | Toutes les cases sont vides. Aucun envoi ni résultat documenté [IN]. Les « associés » ne sont pas nommés |
| 64 | Angle CSE réservé aux « entreprises de 50 salariés et plus (elles ont un CSE) » | [DR] | DPV p. 1 | Imprécis : selon mes connaissances, le CSE existe dès 11 salariés et le budget des activités sociales et culturelles dès 50 (à revérifier) |
| 65 | Idées d'approvisionnement local et d'aménagement des lieux : contrat boissons « négocié à la reprise » avec matériel, imprimeurs pour menus et cartes, chaises, parquet, pergola | [PR] | DPV p. 3, 5, 7, 18, 23, 24, 25 | Révèle un chantier de rénovation et d'achats sans budget connu |
| 66 | Contacter le Journal du Centre pour un « article sur la reprise du Vieux Relais et du M » | [PR] | DPV p. 3, 29 | Stratégie de visibilité publique, opposée au silence imposé ensuite dans le CRM (CAT:52) |
| 67 | Le CRM, conçu pour amener les entreprises au Vieux Relais et au M, a été réorienté vers la vente d'œuvres d'art au plus tôt le 22 oct., donc dès le lendemain du dossier | [DR] | PASS:3-5 ; CTX:47 (hors lot) | Le dossier de Mathys a perdu son objet en quelques jours ; sa base de 100 fiches a été réutilisée (PASS:7, recentrage du 23/10 « demande de Mathys ») |
| 68 | Aucune vente d'œuvre, aucun rendez-vous et aucune réservation ne sont constatés dans mes deux pièces | [IN] (pas de [MM]) | CAT entier ; DPV entier | Il n'existe aucun résultat mesuré pour la valeur commerciale du catalogue ou du dossier |

---

## 3. Chiffres, engagements et dates

| Élément | Valeur | Code | Source |
| --- | --- | --- | --- |
| Date du dossier de Mathys | 21 oct. 2026 (PDF créé à 18:30 UTC) | [FV] | DPV p. 1 ; métadonnées |
| Date du catalogue | 2 nov. 2026 | [FV] | CAT:3 |
| Versement des deux pièces au dépôt | 4 nov. 2026, 16:38 (commit fa5998a) | [FV] | `git log` |
| Classement Pappers utilisé | 100 premières entreprises de la Nièvre par CA, édité le 02/09/2026 | [DR] | DPV p. 1, 34 |
| Types de partenariats testés | 5 (CSE, compte entreprise, événements, fournisseur, visibilité) | [PR] | DPV p. 1 |
| Seuils de cible | CSE : 50 salariés et plus ; événements : 20 salariés et plus | [PR] | DPV p. 1 |
| Priorités | 15 A (12 à Cosne), 8 B « proches de Cosne » | [FV] | DPV p. 2-3 |
| Écartées | 14 entreprises ; « une vingtaine » d'autres en C pour la seule distance (> 70 km) | [DR] | DPV p. 31 |
| Cibles à valider au rendez-vous | 15 à 20 entreprises | [PR] | DPV p. 33 |
| Rendez-vous | « demain », soit le 22 oct. 2026 | [DR] | DPV p. 33 ; CTX:43 |
| Fenêtre de réservation des repas de fin d'année | fin octobre à mi-novembre | [HY] | DPV p. 33 |
| Calendrier d'action | semaine 1, semaine 2, semaines 3 et 4 | [PR] | DPV p. 33 |
| Relances | J+5, puis J+12 | [PR] | DPV p. 34 |
| Appel proposé | 10 minutes | [PR] | DPV p. 32 |
| Remise, capacité, dates, prix | non fixés (« [X %] », « [X] personnes ») | [IN] | DPV p. 32 |
| Distances clés | Pouilly 15 km ; Donzy 18-20 km ; Ciez 20-25 km ; La Charité 30 km ; Nevers 55 km ; Decize 90 km | [ES] | DPV p. 3, 18, 22, 29 |
| Procédures collectives | Premester 19/07/2024 ; Pobi 01/08/2024 ; CFP 02/02/2026 | [DR] | DPV p. 8, 23, 31 |
| Dispositif 238 bis AB | achats avant le 31/12/2028 ; art. 89 de la loi de finances pour 2026 ; BOFiP du 15 avril 2026 | [DR] | CAT:17, 134-135 |
| Durée de déduction et d'exposition | 5 exercices (achat + 4), 1/5 par an | [DR] | CAT:24, 27 |
| Plafond annuel | 20 000 € ou 5 ‰ du CA HT si plus élevé, moins le mécénat | [DR] | CAT:25 |
| Seuil « grands comptes » | plus de 4 M€ de CA | [ES] | CAT:43 |
| Taux d'IS utilisés | 25 % (normal), 15 % (réduit PME) | [DR] | CAT:32 |
| Exemplaires originaux | fontes ≤ 8 ; photographies ≤ 30, signées et numérotées | [DR] | CAT:30, 138 |
| Tableau d'exemples | CA 1 M€ et 2 M€ → plafond 20 000 €, prix max 100 000 €, économie max 25 000 € ; 10 M€ → 50 000 €, 250 000 €, 62 500 € ; 40 M€ → 200 000 €, 1 000 000 €, 250 000 € | [ES] | CAT:58-63 (calculs revérifiés : justes) |
| Exemple d'une œuvre de 30 000 € | 6 000 €/an déduits ; 1 500 €/an d'impôt en moins à 25 % ; 7 500 € au total ; coût net 22 500 € ; 4 500 € à 15 % | [ES] | CAT:65 |
| Offres | 9 offres, 4 familles, 1 dans le CRM, 6 « à construire », 2 « pour 2027 » | [PR] | CAT:38-50 |
| Offre 2 | 3 à 5 œuvres | [PR] | CAT:43 |
| Artistes repérés | 97 (onglet Culture) | [DR] | CAT:47, 81 |
| CRM | 500 entreprises ; branche du 30 oct. ; commit b53a81c | [DR] | CAT:81, 139 |
| Données personnelles exposées | 931 téléphones, 206 e-mails, 63 fichiers de profils LinkedIn | [DR] | CAT:96 |
| Contribution AMF (biens divers) | 8 000 € | [DR] | CAT:97, 137 |
| Petites entreprises | 5 salariés au plus ; aucun paiement avant 7 jours | [DR] | CAT:101 |
| Parcours d'une vente | 7 étapes, la vente à la 4e, 1 alerte | [PR] | CAT:71, 73 |
| Questions à poser | 10 | [PR] | CAT:117-128 |
| Galerie | ouverture en 2027 | [DR] | CAT:9 |
| Bâtiments rachetés | 6 | [DR] | CAT:9 |
| Prix des œuvres, commission des artistes, forfait de suivi, forfait vernissage, adhésion au cercle, tarif de privatisation | non fixés | [IN] | CAT:42-52 |
| Engagements signés | aucun dans mes deux pièces | [IN] | CAT ; DPV |

---

## 4. Contradictions et divergences

| Sujet | Version A + source | Version B + source | Portée pour l'audit |
| --- | --- | --- | --- |
| Nature des deux lieux | Le M est le restaurant, le Vieux Relais le bar (DPV p. 2, 6, 29, 32) | « Le Vieux Relais (hôtel-restaurant) et le M (bar) » (PASS:41, hors lot) | Même les fonctions des lieux ne sont pas stables. Toute fiche « cabaret et autres lieux » doit repartir d'une description confirmée par GianLuca Carlone |
| Qui reprend les lieux | Repreneur non nommé, « Nous reprenons » (DPV p. 32) ; « Un associé rachète deux établissements » (PASS:41) | « Carlone a déjà racheté six bâtiments » (CAT:9) ; « aucun document ne dit [...] qu'ils appartiennent à Carlone » (CTX:160) | L'acheteur, le signataire et le payeur des prestations liées aux lieux sont inconnus |
| Faut-il nommer les lieux ? | Toute l'approche est faite au nom du Vieux Relais et du M, y compris un article de presse sur la reprise (DPV p. 29, 32-33) | « Ne citer ni Le Vieux Relais ni le M » dans les textes aux entreprises (CAT:52 ; PASS:49) | Deux discours opposés auprès des mêmes 100 entreprises. Risque de confusion, voire de défiance, si les deux campagnes se croisent |
| But de la prospection | Remplir un bar et un restaurant (DPV p. 1) | Vendre des œuvres d'art avec un avantage fiscal (CAT:7) ; réorientation au plus tôt le 22 oct. (PASS:3-5) | Changement d'objectif en un jour, sans bilan de la première approche. Le besoin prioritaire de GianLuca Carlone n'est pas stabilisé |
| Périmètre de la cible | 100 entreprises (DPV p. 1) | 500 entreprises (CAT:81) | Évolution normale, mais le dossier de Mathys ne couvre que le top 100 |
| Pratique actuelle de GianLuca Carlone | « Carlone vend des œuvres d'art avec un avantage fiscal » (CAT:7) | « Vend-il déjà à Paris avec cet argument ? » (CAT:124) | Une hypothèse est présentée comme un fait dès la première phrase |
| Niveau de vérification fiscale | « Le cadre fiscal vérifié » ; règles « relues sur les textes officiels » (CAT:13, 15) | Doctrine archivée « à confirmer » ; seuils tirés de « sources secondaires, à vérifier » (CAT:136, 138) ; accès direct à bofip et legifrance bloqué dans la session du CRM (PASS:34) ; plafond de 20 000 € « confirmé » (PASS:5) puis « à vérifier » (PASS:45) | Le niveau de preuve réel est inférieur à ce qu'annonce le titre. À faire valider avant toute vente |
| Liaison avec Hermes360 (Quali Contact) | « Déjà en place : [...] liaison avec Hermes360 » (CAT:81) | « Leur présence dans une branche ne prouve pas un raccordement opérationnel » ; logiciel de Quali Contact « à confirmer » (CRMREF:10-12) | Surévaluation de l'état d'avancement d'un chantier |
| Le chiffre 97 | « 97 artistes » (CAT:47, 81) | « 97 prospects » (CTX:43) ; « 97 artistes, associations, lieux et réseaux » (PASS:56) | Le vivier d'artistes du programme 6 est peut-être surestimé |
| Lieu d'exposition des œuvres vendues | Possible dans « la galerie ou un établissement de Carlone », à valider (CAT:99) ; « piste du Vieux Relais » (PASS:35) | « Ne jamais parler [...] du lieu d'exposition des œuvres » aux entreprises, « pour l'instant » (PASS:49) ; gérer les œuvres pour le client relève des biens divers (CAT:97) | Montage sensible : il est caché aux prospects et non validé juridiquement (voir section 9) |
| Place de BOJ.ART | Les œuvres de BOJ.ART peuvent entrer au catalogue de Carlone ; échantillon peint à la main par Medhi proposé aux entreprises (CAT:106-110) | Le 4 nov., Morgan demande de retirer Medhi/BOJ.ART de l'offre Marwin (NOTE:25) | Le catalogue n'a pas été mis à jour. Il faut dire si le retrait vaut aussi pour le catalogue de GianLuca Carlone |
| Données personnelles exposées | 931 téléphones, 206 e-mails (CAT:96) | 388 entreprises sur 500 ont un numéro ; 38 e-mails génériques (PASS:6, 16) | Unités différentes (occurrences brutes ou entreprises). L'ampleur réelle de l'exposition reste à mesurer |
| Délai de mise en privé | « Passer le dépôt en privé sans attendre » (CAT:96, 2 nov.) | Toujours public le 4 nov. à 16 h 19 (CTX:5) | Une recommandation urgente reste non appliquée après deux jours |

---

## 5. Informations inconnues et questions

**Lieux et entités**
1. Quelle entité juridique détient ou exploite le Vieux Relais et le M ? GianLuca Carlone en est-il associé, dirigeant ou simple investisseur ?
2. La reprise est-elle signée ? À quelle date les lieux rouvrent-ils, avec quelle capacité de salle et quelles licences ?
3. Lequel des deux lieux est le bar, lequel le restaurant (DPV p. 29 contre PASS:41) ? L'un d'eux est-il un hôtel ?
4. Les deux lieux font-ils partie des « six bâtiments » rachetés ? Quels sont les quatre autres, et lequel accueillera la galerie de 2027 ?
5. Quelle structure vendra les œuvres, et sous quel statut de marchand (TVA, registre des objets mobiliers) ?

**Ventes d'œuvres et fiscalité**
6. GianLuca Carlone a-t-il déjà vendu une œuvre à une entreprise avec l'argument du 238 bis AB ? À quel prix, avec quels contrats ?
7. Quels artistes vivants et quelles œuvres sont disponibles, avec leur technique, leur nombre d'exemplaires et leur prix ?
8. Quelle TVA s'applique aux ventes prévues (vente par l'artiste, par un marchand, régime de la marge) et le prix est-il exprimé HT ou TTC ? Le catalogue n'en parle pas.
9. La prolongation du 238 bis AB jusqu'au 31 déc. 2028 (art. 89 de la loi de finances pour 2026) est-elle confirmée sur Légifrance ?
10. Une œuvre achetée par une entreprise peut-elle être exposée dans un lieu appartenant au vendeur (galerie, Vieux Relais) sans perdre la déduction ni tomber dans le régime des biens divers ? Un rescrit a-t-il été demandé ?
11. Qui signe l'« attestation pour l'expert-comptable » de l'offre 4, et qui en répond si la déduction est refusée ?
12. Le forfait de suivi sera-t-il facturé à part, pour ne pas gonfler la base déductible ?
13. Qui délivre les certificats d'authenticité (offre 9), et comment la provenance est-elle établie ?
14. Les assurances sont-elles prévues (œuvres en dépôt, transport, exposition chez le client, événements) ?

**CRM, données et rémunération**
15. Le dépôt FinanceScope/CRM-Carlone est-il désormais privé ? Une copie publique a-t-elle été faite (forks, archives) ?
16. Qui commande et paie les développements « à ajouter » (fiches Offre, Œuvre, Vente, tâches annuelles, alertes), et qui les maintient pendant cinq ans ?
17. Le catalogue et le dossier du 21 oct. ont-ils été facturés, ou font-ils partie du travail « offert » ?
18. Combien d'artistes, et non de prospects culturels, compte réellement l'onglet Culture ?

**Dossier du 21 octobre**
19. Le rendez-vous du 22 oct. a-t-il eu lieu, avec qui, et l'offre de base (remise CSE, formules, capacité, prix) a-t-elle été fixée ?
20. Un seul message ou appel de ce plan a-t-il été envoyé ou passé ? Avec quels résultats ?
21. Qui sont les deux « associés » chargés des secteurs (DPV p. 33) : Morgan et Mathys, ou des associés de GianLuca Carlone ?
22. Quelle part du dossier Mathys a-t-il rédigée lui-même, et en combien de temps ? Cela compte pour évaluer sa capacité réelle de production.
23. La campagne « bar et restaurant » est-elle abandonnée, suspendue ou à reprendre après la réouverture ?

---

## 6. Par chantier

| Chantier | Ce que mes pièces disent |
| --- | --- |
| **CRM et développement commercial** | C'est le cœur des deux pièces. Le dossier du 21 oct. est une base de 100 fiches de prospection avec priorités, angles, messages et plan sur quatre semaines (DPV p. 1-34) [PR]. Le catalogue définit neuf offres de vente d'œuvres et les fiches à ajouter au CRM (CAT:38-50, 85-90) [PR]. Le CRM « déjà en place » reste déclaratif (CAT:81) [DR]. Aucune vente, aucun rendez-vous et aucun taux de réponse ne sont mesurés [IN]. Point bloquant : la structure qui vend n'est pas choisie (CAT:90) |
| **Quali Contact** | Une seule mention indirecte : « liaison avec Hermes360 » donnée comme déjà en place (CAT:81) [DR], contredite par CRMREF:10-12. Rien d'autre |
| **Organisation et pilotage** | Le plan d'action du dossier (répartition entre deux « associés », semaines 1 à 4, relances à J+5 et J+12, bilan par angle) est un petit modèle de pilotage commercial (DPV p. 33-34) [PR], sans responsable nommé ni suivi. Le catalogue liste dix questions à poser au client (CAT:117-128) : c'est une préparation de décision |
| **Jarvis, mémoire et automatisations** | Tâches annuelles automatiques (photo datée, attestation, rappel de la réserve) et alertes de réintégration ou de fin de période proposées dans le CRM (CAT:88-89) [PR]. Relais CRM → Jarvis de l'atelier pour les commandes sur mesure (CAT:111) [PR]. Version autonome sur Firebase citée (CAT:81) [DR]. Le dossier du 21 oct. : rien |
| **Marketing et contenus** | Trois messages types et un script d'appel au nom des lieux (DPV p. 32-33) ; idées d'imprimeurs pour la nouvelle identité imprimée (menus, cartes, flyers de réouverture) (DPV p. 5, 7, 11) ; article et pack d'annonces dans le Journal du Centre (DPV p. 29). Catalogue : cartel, information du public, « textes de vente validés » à produire (CAT:42, 85) ; consigne de ne jamais promettre de rendement (CAT:97) |
| **Galerie, œuvres et artistes** | Galerie annoncée pour 2027 (CAT:9) [DR] ; offres 7 et 8 conditionnées à son ouverture (CAT:48-49). Programme artistes : dépôt, assurance, commission, pas de loyer (CAT:47) [PR]. Règles fiscales sur l'œuvre originale (CAT:22, 30) [DR]. Aucun artiste engagé, aucune œuvre en stock, aucun prix [IN] |
| **Événements et vernissage** | Offre 5 « Vernissage en entreprise » (CAT:46) et offre 8 « Privatisation et événements » (CAT:49) [PR]. Le dossier du 21 oct. propose de nombreux événements dans les lieux : repas de fin d'année, séminaires, soirées automobiles, motos, rugby, dégustations, lancements de modèles (DPV p. 1-30) [PR]. Le vernissage « Strates » n'est pas mentionné |
| **Cabaret et autres lieux** | Le Vieux Relais et le M à Cosne-Cours-sur-Loire : bar et restaurant en cours de reprise, à rénover et rouvrir (DPV p. 3, 23, 32) [DR]. Fonctions des lieux contradictoires (section 4). Les bâtiments servent à l'offre 8 (CAT:49). Cabaret : rien |
| **Medhi et BOJ.ART** | Les pièces entièrement faites à la main par Medhi peuvent servir les offres 1 à 3 ; les pièces imprimées en 3D ou peintes au robot sont « très probablement » exclues de l'avantage fiscal (CAT:106-109) [HY]. Le catalogue n'a pas été mis à jour après la décision du 4 nov. (NOTE:25). Le dossier du 21 oct. : rien |
| **STRATES, Éclosion et créations** | STRATES : « sa valeur est artistique et d'image, pas fiscale » ; seul l'échantillon peint à la main par Medhi peut être proposé aux entreprises (CAT:110) [PR]. Éclosion : rien |
| **Laboratoire IA et robotique** | Indirectement : les œuvres produites par impression 3D, bras robotisé ou procédé numérique ne doivent pas être vendues avec la promesse d'une déduction sans rescrit favorable (CAT:98, 109). Cela affaiblit tout argument fiscal adossé au laboratoire (DEMANDE.md:64). Rien d'autre |

---

## 7. Erreurs d'identité

- **Aucune occurrence** de « John-Lucas », « John Lucas », « Jean-Luc » ou d'une autre variante dans mes deux pièces (recherche insensible à la casse sur `john`, `lucas`, `jean-luc`, `gian` : 0 dans CAT, 0 dans le texte extrait de DPV).
- Le catalogue désigne le client uniquement par son nom, « Carlone » (14 occurrences, dont le titre CAT:1), sans prénom. Ce n'est pas une erreur, mais aucune de mes pièces n'écrit « GianLuca ».
- Le dossier du 21 oct. ne nomme pas du tout le client (aucune occurrence de « Carlone ») : le lien entre ce dossier et GianLuca Carlone n'est établi que par d'autres pièces (CTX:44, 47 ; PASS:1-3).

---

## 8. Instructions trouvées dans les pièces

Aucune instruction n'est adressée explicitement à un assistant IA dans mes deux pièces. Les demandes d'action suivantes visent des personnes. **Aucune n'a été exécutée.**

| Source | Texte ou demande | Destinataire apparent |
| --- | --- | --- |
| CAT:96 | « passer le dépôt en privé sans attendre (Settings, Danger Zone, Change visibility), puis vérifier qu'aucune copie publique n'existe » | Propriétaire du dépôt FinanceScope/CRM-Carlone |
| CAT:128 | « Le dépôt du CRM peut-il passer en privé aujourd'hui ? » | GianLuca Carlone |
| CAT:13 | Faire valider chaque offre par l'expert-comptable ou l'avocat fiscaliste avant de la vendre | Morgan, Mathys et GianLuca Carlone |
| CAT:98 | Demander un rescrit avant de promettre la déduction pour une œuvre au procédé douteux | Vendeur |
| CAT:85-90 | Ajouter au CRM les fiches Offre, Œuvre et Vente, les tâches automatiques et les alertes ; décider du nom de la structure qui vend | Équipe CRM et associés |
| DPV p. 32 | « Remplacez les crochets avant envoi : capacité des salles, remise proposée, dates » ; trois messages prêts à envoyer | Personne chargée du démarchage |
| DPV p. 33 | Script d'appel au standard pour obtenir le nom et l'adresse e-mail du CSE ou de l'assistante de direction | Idem |
| DPV p. 33-34 | Plan : appeler les standards des priorités A, envoyer les messages 1, 2 et 3, relancer à J+5 et J+12, commencer les priorités B, « refaire une vague » | Les deux « associés » |
| DPV p. 31 | « Vérifier d'abord que le casino est toujours ouvert » ; vérifier l'enseigne du magasin de Decize | Idem |

---

## 9. Points d'audit

### A. Le catalogue d'offres (2 novembre)

1. **Une hypothèse présentée comme un fait dès la première ligne.** « Carlone vend des œuvres d'art avec un avantage fiscal » (CAT:7) est démenti par la question CAT:124. Toute la construction (neuf offres, suivi sur cinq ans, CRM) repose sur une activité dont aucune vente n'est prouvée. Avant de développer quoi que ce soit, il faut la preuve d'au moins une vente ou d'une demande d'entreprise [IN].
2. **Une demande solvable non démontrée.** Pour une PME de la Nièvre de 1 à 4 M€ de CA, l'économie d'impôt maximale est de 5 000 € par an (CAT:32, 60-61), et seulement si elle est bénéficiaire. L'entreprise paie toujours au moins 75 % du prix. Rien ne montre que des dirigeants nivernais veulent acheter des œuvres de 30 000 à 100 000 € [IN]. Le catalogue ne donne aucune estimation du nombre d'acheteurs possibles.
3. **Un prix calé sur la capacité fiscale de l'acheteur.** « Prix de l'œuvre, au plus cinq fois le plafond annuel du client » (CAT:42) suggère d'ajuster le prix à la déduction possible plutôt qu'à la valeur de l'œuvre. En cas de contrôle, un prix sans référence de marché expose l'acheteur et le vendeur. Il faut une cote ou des ventes comparables par artiste.
4. **Un plafond présenté comme individuel alors qu'il est partagé.** Le tableau CAT:58-63 suppose une seule œuvre. Or le plafond annuel est commun au mécénat (CAT:25) et à toutes les œuvres en cours de déduction. L'offre 2 et la relance « nouvelle œuvre » à la fin des cinq ans (CAT:75) n'en tiennent pas compte.
5. **Un taux réduit simplifié.** L'économie « à 15 % » (CAT:32, 65) ne vaut que pour la tranche de bénéfice imposée à ce taux. Selon mes connaissances, au-delà de 42 500 € de bénéfice, la déduction économise 25 % (à revérifier). Le CRM devrait calculer l'économie à partir du bénéfice réel.
6. **Un titre « vérifié » excessif.** Deux piliers (l'exclusion des procédés non manuels et les seuils d'exemplaires) reposent sur une doctrine archivée de 1995 et des sources secondaires (CAT:136, 138). La prolongation jusqu'en 2028 n'a pas été rouverte dans cet audit. Il faut écrire « à valider » et obtenir un avis écrit d'un professionnel.
7. **La TVA est absente.** Le catalogue ne dit rien de la TVA sur les ventes d'œuvres (taux, régime de la marge, prix HT ou TTC pour une entreprise). C'est une question directe pour l'expert-comptable (à revérifier).
8. **Le montage le plus risqué n'est pas traité : l'exposition chez le vendeur.** CAT:99 et PASS:35 envisagent d'exposer les œuvres achetées par les entreprises dans la galerie ou au Vieux Relais. En même temps, le CRM interdit de parler du lieu d'exposition aux prospects « pour l'instant » (PASS:49). Si l'œuvre reste chez le vendeur, trois risques se cumulent : (a) un lieu non prévu par le BOFiP (CAT:99) ; (b) une « gestion des œuvres pour le client » qui peut faire basculer l'offre dans le régime des biens divers (CAT:97) ; (c) le reproche d'avoir caché un élément déterminant à l'acheteur. Il faut un avis juridique et fiscal écrit avant toute prospection sur ce schéma, et la transparence envers les acheteurs.
9. **Une responsabilité non attribuée dans l'offre 4.** Produire une « attestation pour l'expert-comptable » chaque année (CAT:45) engage celui qui la signe. Si la déduction est refusée, l'acheteur se retournera contre lui. Il faut préciser qui signe, avec quelle assurance, et facturer ce suivi séparément pour ne pas gonfler la base déductible (CAT:24, 45).
10. **Des développements sans financeur.** Les fiches et automatisations « à ajouter » (CAT:85-89) supposent cinq ans de maintenance. Ni le prix, ni le payeur, ni la propriété ne sont dits. C'est exactement le risque, signalé par la demande, d'un abonnement qui absorbe des développements (DEMANDE.md:28).
11. **Un conflit d'intérêts à déclarer.** Morgan orchestre BOJ.ART (CTX:25) et rédige le catalogue de vente de GianLuca Carlone, qui propose de vendre des pièces de Medhi aux entreprises (CAT:108, 110). Même après le retrait de BOJ.ART de l'offre Marwin (NOTE:25), ce double rôle doit être déclaré par écrit au client.
12. **Une urgence sur les données non réglée.** Le dépôt public contenant des centaines de coordonnées personnelles était signalé comme urgent le 2 nov. (CAT:96). Il était toujours public le 4 nov. (CTX:5), et une copie existe maintenant dans le dépôt Carlone (CRMREF:10). C'est un risque RGPD immédiat, sans responsable de traitement désigné [IN].
13. **Un état d'avancement surévalué.** « Liaison avec Hermes360 » (CAT:81) et « 97 artistes » (CAT:47) donnent une image plus avancée que les autres pièces (CRMREF:10-12 ; PASS:56). Dans une proposition commerciale, seuls des éléments recettés doivent être présentés comme « en place ».
14. **Un point fort à conserver.** Le catalogue écarte clairement les promesses de rendement (CAT:97), distingue particuliers et entreprises (CAT:34), prévoit le rescrit pour les procédés non manuels (CAT:98) et formule dix questions utiles (CAT:117-128). C'est un bon exemple de « préparation de décision » que Marwin peut facturer, à condition de le présenter comme un travail à valider et non comme une offre prête à vendre.

### B. Le dossier de Mathys (21 octobre) : méthode, sources, limites

**Méthode (points forts).** La base est explicite et datée : le classement Pappers du 02/09/2026 (DPV p. 1). Le dossier présente une grille de cinq angles avec un intérêt pour chaque lieu, des priorités A, B et C fondées sur un critère clair (la proximité de Cosne et la taille), des comptes cohérents que j'ai recomptés (100 entreprises, 15 en A), un regroupement des groupes et des holdings pour éviter les doublons (DPV p. 11, 25, 31), et une mise à l'écart prudente des entreprises en procédure collective (DPV p. 31). Le plan d'action est mesurable : relances datées et bilan « par angle » (DPV p. 33-34). Les limites sont déclarées : distances estimées, mentions « non confirmé » (DPV p. 34). La posture est celle d'un test (« garder ceux qui accrochent », DPV p. 1), ce qui est sain.

**Sources (points moyens).** Le dossier s'appuie sur trois familles de sources (Pappers, l'annuaire de l'État, les sites et la presse, DPV p. 34), mais seulement 23 fiches sur 100 renvoient au site de l'entreprise. Aucun chiffre d'affaires, résultat ou effectif précis n'est reproduit alors que le classement en dépend. Plusieurs faits précis ne sont pas sourcés : chômage partiel chez Aperam (DPV p. 7), anniversaire de Look (DPV p. 6), situation déficitaire d'Aizen (DPV p. 9). La documentation est probablement produite avec un assistant IA [HY]. La part de travail propre à Mathys et le temps passé sont inconnus [IN].

**Limites (points faibles).**
15. **Un objectif non validé et vite abandonné.** Le dossier a été écrit pour un bar et un restaurant dont ni le propriétaire ni la date de réouverture ne sont établis. Le CRM a été réorienté vers l'art au plus tôt le lendemain (PASS:3-5). Aucun bilan de l'approche « bar et restaurant » n'existe. C'est le symptôme d'un besoin client qui change plus vite que les livrables.
16. **Des engagements implicites dans les messages.** « Nous reprenons le Vieux Relais et le M » et « Il reste des dates en décembre » (DPV p. 32) engagent les lieux sur une capacité et un calendrier inconnus. De plus, l'expéditeur se présente comme repreneur alors que son identité et son mandat ne sont pas définis. Si Marwin démarchait ainsi, il agirait au nom d'un tiers sans mandat écrit.
17. **Aucune règle de prospection.** Le dossier ne parle ni d'opposition à la prospection, ni de lien de désinscription, ni d'origine des coordonnées. Pourtant, 13 entreprises s'étaient opposées à la prospection sur Pappers (PASS:51), et le dossier nomme des dirigeants (DPV p. 4, 5). Le CRM a corrigé ce point ensuite (CAT:102).
18. **Une hypothèse de calendrier non sourcée.** La « fenêtre » de fin octobre à mi-novembre (DPV p. 33) n'est appuyée sur rien. Au 4 nov., elle est presque close et aucun envoi n'est prouvé.
19. **Une offre de base absente.** La remise, les formules, la capacité et les prix devaient être fixés « au rdv de demain » (DPV p. 33). Sans eux, le dossier n'est pas exécutable : il prépare une décision, il ne la remplace pas.
20. **Une imprécision réglementaire mineure.** Le dossier réserve l'angle CSE aux entreprises de 50 salariés et plus, au motif qu'« elles ont un CSE » (DPV p. 1). Selon mes connaissances, le CSE existe dès 11 salariés et le seuil de 50 concerne le budget social et culturel (à revérifier).

**Verdict sur la qualité du travail de Mathys.** C'est un bon travail de recherche et de structuration commerciale : clair, prudent sur les entreprises fragiles, avec un plan mesurable. On peut le réutiliser comme modèle de « cadrage de prospection », et sa base a effectivement nourri le CRM (PASS:7). Il ne prouve en revanche ni une capacité de vente (aucun résultat mesuré), ni une compréhension validée du besoin du client (objectif abandonné en un jour), ni une maîtrise des règles de prospection et de mandat. Pour l'audit de capacité, ce dossier compte comme une compétence **démontrée en recherche et en rédaction assistée**, et **non démontrée en exécution commerciale**.

### C. Points transversaux

21. **Les entités ne sont pas cartographiées.** Mes deux pièces ne permettent d'identifier ni l'acheteur, ni le signataire, ni le payeur, ni le bénéficiaire d'aucune prestation. Le lieu (Vieux Relais, le M), la vente d'œuvres et la future galerie peuvent relever de trois structures différentes. Une proposition commerciale unique adressée à « Carlone » serait juridiquement fragile.
22. **Deux récits commerciaux incompatibles visent les mêmes entreprises.** Le restaurant qui recrute des CSE se présente à visage découvert (DPV p. 32). Le vendeur d'œuvres doit, lui, taire ces lieux (CAT:52). Sans arbitrage écrit de GianLuca Carlone sur l'ordre et l'identité des campagnes, le risque est de brouiller la relation avec les 12 cibles prioritaires situées à Cosne.
23. **Aucune preuve mesurée [MM] dans les deux pièces.** Tout ce qui est chiffré relève de la simulation [ES] ou de la déclaration [DR]. Le premier jalon utile n'est pas un nouvel outil. C'est un résultat observable : une offre validée par un fiscaliste, une structure vendeuse désignée, et une première série d'appels avec ses taux de réponse et de rendez-vous.
