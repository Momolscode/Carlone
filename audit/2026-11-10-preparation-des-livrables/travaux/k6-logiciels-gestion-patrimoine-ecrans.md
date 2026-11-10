# Logiciels de gestion de patrimoine immobilier : écrans, fonctions et ergonomie de référence, pour une maquette en données fictives

Note de travail interne — sources publiques consultées le 10 novembre 2026 — ce n’est pas un avis juridique, fiscal ou d’assurance

Document interne. Ne pas transmettre à GianLuca Carlone. Sert d’abord au livrable 4 (écrans d’exemple).

## En bref

- Les quatre écrans du livrable 4 sont déjà définis dans notre annexe du 9 novembre. La maquette les illustre, sans rien ajouter.
- En 2026, les logiciels du marché ouvrent sur une liste de choses à faire, pas sur des graphiques. Les états sont écrits en mots, avec une date.
- L’intelligence artificielle annoncée en 2025 et 2026 lit, prépare et rapproche. Partout, une personne valide. Ce sont des annonces d’éditeurs, sans essai indépendant.
- Prix publics : quelques dizaines d’euros par mois en gestion locative ; non trouvés pour le patrimoine technique. Ils restent internes.
- Accessibilité : jamais la couleur seule, contraste de 4,5 pour 1, cibles de 24 pixels. Le RGAA 5 est annoncé pour décembre 2026.
- Une maquette trop finie fait croire que le logiciel existe. Donc : « Maquette — données fictives » sur chaque écran, et des images fixes.
- Trois devis se comparent sur une grille commune : périmètre, TVA, délai, validité, décennale, acompte. Depuis le 1er mars 2025, une mention sur le devis remplace l’attestation de TVA.
- Plusieurs règles lues sont écrites pour les particuliers. Leur effet pour une société reste à confirmer.

## 1. Fonctions et écrans montrés par les logiciels du marché en 2026

### 1.1 Ce que le dépôt fixe déjà (pour ne pas le refaire)

Mention ajoutée pour nos propres documents : [Document du dépôt].

- Les quatre écrans sont décrits dans `pour-carlone/logiciels-et-automatisations/2026-11-09-annexe-specification-logiciel-gestion-proprietes.md` (section 3) : fiche bâtiment (module 1), comparaison des devis (module 3, « grille commune, postes manquants et écarts signalés », niveau « Assistée »), calendrier des échéances (module 5, rappels deux mois, un mois et une semaine avant), tableau de bord (module 7, liste « à décider » avec date limite, douze indicateurs au plus par vue). La maquette suit ces listes, sans en ajouter. [Document du dépôt]
- L’outil ne dit jamais qu’un lieu est « conforme » (annexe). Toute maquette porte « Maquette — données fictives » (`audit/2026-11-09-audit-presentation-et-offre/travaux/BRIEF.md`, § 5, règle 2). [Document du dépôt]
- L’étape 2 de la proposition du 9 novembre s’appelle déjà « Maquette et essai sur données fictives » (février et mars 2027, estimation). Le livrable 4 en est un avant-goût, pas l’étape elle-même. [Document du dépôt]

### 1.2 Ce que montrent les logiciels du marché

Ce qui suit vient des pages publiques des éditeurs, non datées sauf mention. Ce sont leurs déclarations. Aucun logiciel n’a été essayé. Aucun compte n’a été créé.

- **Tableau de bord.** Il ouvre sur une liste de choses à faire, plus sur des graphiques. Amleks : « Le tableau de bord vous dit quoi faire aujourd’hui » ; puis « la liste de ce qui attend une décision » ; chaque ligne mène à son écran ; « Rien ne part sans vous. L’application prépare, vous relisez et vous validez. » (amleks.fr/fonctionnalites). Lokabail : onglet « À faire », classé par priorité (lokabail.com/pour-les-bailleurs). Wexeor et Brik Pro montrent d’abord l’argent : valeur, rentabilité, trésorerie, impayés (wexeor.com/fonctionnalites ; pro.brik.com/fonctionnalites). [Source professionnelle]
- **Fiche du bien.** Adresse, surface, diagnostics avec date de fin de validité, charges, photos, documents, historique (logiciel-gestion-immobilier.com/fonctionnalites). Carte de tous les biens (piaire.ai/fonctionnalites). [Source professionnelle]
- **Échéancier.** Vue par mois ou par an, avec rappels : loyers, révisions, fins de bail, échéances triennales, fins de crédit, diagnostics (logiciel-gestion-immobilier.com ; piaire.ai). Amleks suit les « diligences » de chaque bien « avec leur état, leur échéance et un rappel » (amleks.fr). DriveIM écrit les états en mots : « ÉCHÉANCE J−30 », « J−12 », « FAIT », « VÉRIFIÉ » (driveim.com/solutions/immobilier-tertiaire). OPTIMa alerte 30, 15 et 7 jours avant (gmao.org/secteurs/batiment). [Source professionnelle]
- **Documents.** Chaque pièce est rattachée au bien, au bail ou à la société ; recherche dans le texte, même scanné ; partage par lien, « révocable » chez Amleks (pro.brik.com ; amleks.fr). [Source professionnelle]
- **Travaux et devis.** Demande, urgence, prestataire, statut, historique par bien (pro.brik.com). DimoMaint FM : devis saisis ligne par ligne, approuvés ou refusés ; plusieurs prestataires invités ; budgets ; export vers un tableur (gmao.com/gmao-fm). [Source professionnelle]. Aucune page lue ne montre trois devis côte à côte. Cela peut nous distinguer, mais quelques pages ne prouvent rien sur le marché. [À confirmer]
- **Baux et loyers.** Bail commercial avec option pour la TVA, indexation, factures numérotées, rapprochement bancaire, relances par étapes (amleks.fr). Facture électronique annoncée pour les sociétés civiles soumises à la TVA (lokabail.com). [Source professionnelle]
- **Contacts.** Fiche par locataire et par prestataire, avec pièces administratives et alertes d’expiration (logiciel-gestion-immobilier.com ; daftar.fr/fonctionnalites). [Source professionnelle]
- **Exports.** Écritures comptables, tableur, PDF ; export complet « sans restriction ni frais » (logiciel-gestion-immobilier.com) ; registre de sécurité de l’année en PDF (daftar.fr). [Source professionnelle]
- **Contrôles obligatoires.** Daftar propose, à partir de la fiche du bâtiment, les contrôles à faire, avec base légale et périodicité ; trois états : « à programmer, programmé, réalisé » (daftar.fr). DriveIM précise : « DriveIM n’est pas un bureau de contrôle. » (driveim.com). À l’inverse, Solare IT promet de « contrôler, en quelques clics, si vous êtes conforme » (solare-it.com) : c’est la formule que notre annexe interdit. [Source professionnelle]

## 2. Nouveautés d’intelligence artificielle, 2025 et 2026

Tout ce qui suit est annoncé par les éditeurs, dans leurs communiqués ou sur leurs pages.

- **Lecture de documents.** Yardi, 29 octobre 2025 : « Smart AP » lit les factures reçues par courriel ; l’utilisateur relit et approuve. MRI Software, 3 novembre 2026 : lecture des baux « with confidence scores and an audit trail supporting human review », soit une note de confiance et une trace pour la relecture. En France : pièces « classées par l’IA à l’import » (Brik Pro) ; « L’IA lit vos contrats - durée, préavis, reconduction tacite - et vous alerte avant la date limite de dénonciation » (Daftar). [Source professionnelle]
- **Assistants et agents.** AppFolio, 16 juin 2026 : un agent comptable code les factures et signale les écarts, « with human supervision in place » ; 29 septembre 2026 : un tableau de bord construit à partir d’une demande écrite. MRI, 3 novembre 2026 : près de 250 agents, dont un agent vocal pour les appels de maintenance. Yardi, 9 septembre 2025 : assistant intégré ; 78 % de questions résolues sans passer à une personne, selon l’éditeur. En France : demandes « analysées par IA » (Muvraline, 26 juin 2026) ; ticket créé par « l’agent IA » (Brik Pro). [Source professionnelle]
- **Rapprochement.** Relevé bancaire rapproché des loyers et des factures (Amleks, Brik Pro) ; clôture mensuelle chez MRI (2 juin 2025, alors en « limited availability »). [Source professionnelle]

**Prudence.**
- Tous les chiffres viennent des éditeurs. Aucun essai indépendant n’a été trouvé. [À confirmer]
- Plusieurs fonctions sont en accès limité, « Bientôt » ou en « bêta privée » (MRI en 2025, Brik Pro).
- Les annonces américaines visent de grands gestionnaires de logements. Rien ne dit qu’elles existent en français, ni pour quelques immeubles. [À confirmer]
- Point commun de 2026 : la machine prépare, une personne valide. DriveIM : « Qualification automatique · décision humaine ». PIAIRE : « sans jamais vous dire quoi faire ». C’est notre niveau « Assistée ».

## 3. Prix publics, ordre de grandeur

Prix relevés le 9 novembre 2026 dans `interne/logiciels-et-automatisations/travaux/r1-marche-et-offre-accord.md` (section 2), d’après les pages tarifaires des éditeurs. Non relus aujourd’hui. [Source professionnelle]

- Gestion locative : de 0 à environ 70 € par mois (Rentila, Qalimo, Talok) ; au lot, de 1 € à 2,50 € HT par mois (Ublo, Locatik). Pour 10 à 20 lots : 120 à 850 € par an.
- Maintenance : de 0 à 75 dollars par utilisateur et par mois (Fiix, UpKeep) ; G’ma GMAO, 790 € HT par an jusqu’à 5 utilisateurs ; DimoMaint MX, 40 à 80 € par utilisateur, mise en place de 490 à 4 990 € HT.
- Patrimoine technique (CARL Source, Solare IT, DriveIM, Daftar) et grands éditeurs américains : aucun prix sur les pages lues. Sans doute sur devis. [À confirmer]
- Ces prix sont internes. Le brief interdit de montrer au client un autre prix que celui du cadrage, sauf décision écrite de Morgan Olsen et Mathys Couet.

## 4. Ergonomie pour une personne non technicienne, et accessibilité

**Critères reconnus.** Les dix critères de Jakob Nielsen restent la référence. Les plus utiles ici : montrer l’état du système ; parler avec les mots de l’utilisateur, pas ceux de l’équipe ; faire reconnaître plutôt que retenir ; rester sobre ; prévenir les erreurs. (« 10 Usability Heuristics for User Interface Design », Nielsen Norman Group, 24 avril 1994, revu le 30 janvier 2024) [Source professionnelle]

**Règles d’accessibilité (WCAG 2.2, recommandation du W3C du 5 octobre 2023).** [Autorité ou organisme]
- Jamais d’information par la couleur seule (critère 1.4.1, niveau A).
- Contraste du texte : 4,5 pour 1 au moins ; 3 pour 1 pour les grands textes (1.4.3, AA). Contraste des boutons, champs et pictogrammes utiles : 3 pour 1 (1.4.11, AA).
- Texte agrandi à 200 % sans perte (1.4.4, AA). Contenu lisible sur 320 pixels de large sans défilement dans les deux sens (1.4.10, AA).
- Nouveau en 2.2 : une cible cliquable mesure au moins 24 pixels sur 24, sauf exceptions (espacement suffisant, lien dans une phrase). (critère 2.5.8, AA ; page « Understanding SC 2.5.8 », W3C)

**En France : RGAA 4.1.2.** Critère 3.1 : pas d’information par la couleur seule. Critère 3.2 : contraste de 4,5 pour 1 pour un texte de moins de 24 px (ou de moins de 18,5 px en gras), 3 pour 1 au-delà. (RGAA version 4.1.2, DINUM, accessibilite.numerique.gouv.fr) [Texte officiel]

**Changement 2026.** Le RGAA 5 est annoncé pour décembre 2026, puis rendu officiel par un texte en 2027. Il reprend les WCAG 2.2 et ajoute 40 critères. Il couvre aussi les applications mobiles et les documents bureautiques. D’ici là, la version 4.1.2 reste la référence. (« Ce qui change avec le RGAA 5 », DesignGouv, 3 novembre 2026) [Autorité ou organisme]. Qui est tenu par la loi de respecter le RGAA, et depuis quand : non vérifié ici. [À confirmer]

**États et alertes (Système de design de l’État, pages non datées).** [Autorité ou organisme]
- Badge : il indique un « statut » ou un « état ». Il n’est pas cliquable. Il est placé à côté de l’élément. Libellé court. Le même badge pour la même information partout. « L’information doit être donnée par le texte du badge. L’icône est purement décorative. »
- Alerte : dire la nature du message dans le titre, car « l’icône et la couleur ne garantissent pas à elles seules la bonne compréhension ». Dire l’action attendue. Pas de terme technique. Ton courtois.

**Tableaux.**
- Première colonne : un nom lisible par un humain, pas un numéro interne. Colonnes rangées par importance. En-têtes figés. Lignes alternées pour ne pas perdre sa place. Filtre actif toujours visible. (« Data Tables: Four Major User Tasks », P. Laubheimer, Nielsen Norman Group, 3 avril 2022) [Source professionnelle]
- Unité dans le titre de la colonne. Chiffres alignés à droite. Aucune cellule vide. Sur téléphone, préférer une liste. Moins de 4 lignes ou de 3 colonnes : choisir une autre forme. (Système de design de l’État, composant Tableau) [Autorité ou organisme]

**Repères visuels.** Dans un essai, les personnes trouvent un élément environ 37 % plus vite quand le repère change à la fois de couleur et de pictogramme, par rapport au texte seul. Le pictogramme seul fait mieux que la couleur seule. (« Visual Indicators to Differentiate Items in a List », A. Harley, Nielsen Norman Group, 7 août 2016) [Source professionnelle]. Mais trop de repères créent du bruit. (« Indicators, Validations, and Notifications », K. Flaherty, Nielsen Norman Group, 17 janvier 2024) [Source professionnelle]

## 5. Présenter une maquette à un client

- Plus une maquette est soignée, plus on la croit finie. Devant une maquette brute, personne n’attend une mise en service le lendemain. Devant une maquette très finie, un dirigeant dit vite : « this looks good, let’s make it go live now ». (« UX Prototypes: Low Fidelity vs. High Fidelity », K. Pernice, Nielsen Norman Group, 18 décembre 2016) [Source professionnelle]
- Même source : une maquette très fidèle ressemble souvent à un logiciel en service. La fidélité se règle sur trois points séparés : ce qui réagit au clic, l’apparence, le contenu.
- Une maquette cliquable coûte du temps : chaque clic possible doit avoir une réponse. Des écrans fixes se préparent plus vite et se corrigent plus facilement. (même source) [Source professionnelle]
- Un éditeur légende ses captures : « Le tableau de bord, en données de démonstration ». (amleks.fr) [Source professionnelle]. Notre brief impose « Maquette — données fictives ».

## 6. Comparer trois devis de travaux côte à côte

**Ce qu’un devis contient.**
- Pour le dépannage, la réparation et l’entretien dans le bâtiment : date ; nom et adresse de l’entreprise ; nom du client ; lieu ; nature exacte des travaux ; décompte de chaque prestation et produit (désignation, prix unitaire, unité, quantité) ; frais de déplacement ; total hors taxes et toutes taxes, avec le taux de TVA ; durée de validité ; devis payant ou gratuit. (arrêté du 24 janvier 2017, article 4, Légifrance) [Texte officiel]
- Ce texte renvoie au code de la consommation, et les fiches officielles parlent du « consommateur ». S’applique-t-il quand le client est une société ? Non vérifié. [À confirmer]
- Le devis est une offre de contrat. Une fois accepté, il engage les deux parties. (fiche « Devis », DGCCRF, non datée ; Service Public, fiche F2533) [Autorité ou organisme]

**Assurance décennale.** L’attestation d’assurance est jointe aux devis et aux factures. Le professionnel y mentionne aussi son assurance, les coordonnées de l’assureur et la couverture géographique. (Service Public, fiche F2034, lue sur une copie, hors du site officiel ; Service Public Entreprendre, fiche F37370) [Autorité ou organisme]

**Acompte ou arrhes.** Avec un acompte, les deux parties sont engagées ; celle qui renonce peut devoir des dommages et intérêts. Avec des arrhes, chacun peut renoncer : le client les perd, le professionnel en rend le double. Si rien n’est écrit, la somme est présumée être des arrhes. (Service Public, fiche F31187, écrite pour les particuliers) [Autorité ou organisme]. Entre deux sociétés : non vérifié. [À confirmer]

**TVA. Changement 2025.**
- Les taux de 10 % et de 5,5 % sont réservés aux travaux dans des logements achevés depuis plus de deux ans. (« Quel taux de TVA appliquer pour les travaux réalisés dans les logements ? », impots.gouv.fr, non datée) [Autorité ou organisme]
- Ce qui compte est le local, pas le client : la règle vaut pour une personne comme pour une société, société civile comprise. (BOFiP, BOI-TVA-LIQ-30-20-90-40, version du 9 septembre 2026, doctrine de l’administration) [Texte officiel]. Pour une boutique ou une salle de spectacle, le taux normal de 20 % s’appliquerait donc : c’est notre déduction. [À confirmer]
- Depuis le 1er mars 2025, le client certifie par une mention sur le devis ou la facture que les conditions du taux réduit sont remplies. L’ancienne attestation n’est plus demandée. (même page) [Autorité ou organisme]
- L’entreprise fait apparaître séparément, sur le devis, la part à 5,5 %, à 10 % et à 20 %. (BOFiP, BOI-TVA-LIQ-30-20-90-40, version du 9 septembre 2026) [Texte officiel]

**Présentation.** Un tableau facilite la comparaison, car deux valeurs voisines se lisent sans effort de mémoire. (« Data Tables », Nielsen Norman Group, 3 avril 2022) [Source professionnelle]. DimoMaint saisit les devis ligne par ligne. (gmao.com) [Source professionnelle]

## 7. Fiche bâtiment : données et échéances dans les outils de référence

- Un arbre : site, bâtiment, étage, local, équipement. (CARL Source Facility ; DimoMaint FM) [Source professionnelle]
- Un « carnet de santé du patrimoine » : caractéristiques techniques, surfaces, documents, valeurs d’amortissement, parcelles, coordonnées GPS ; suivi de l’acquisition à la cession. (carl-software.fr, non datée) [Source professionnelle]
- Une identité réglementaire : type et catégorie d’établissement recevant du public. L’outil en tire une liste de contrôles, avec base légale et périodicité. La prochaine échéance est recalculée après chaque contrôle. (daftar.fr) [Source professionnelle]
- Les rapports des organismes de contrôle sont intégrés ; une intervention est créée pour chaque réserve à lever. (carl-software.fr) [Source professionnelle]
- Photos, historique et statut par bâtiment. (visionsoft.tech, 27 mars 2025) [Source professionnelle]
- Échéances rattachées au bien : diagnostics, assurances (sci-pilot.fr) ; révision de loyer, fin de bail, échéance triennale, fin de crédit (piaire.ai) ; date limite pour dénoncer un contrat (daftar.fr) ; contrôles, réserves, plan de travaux sur plusieurs années (solare-it.com). [Source professionnelle]
- Notre annexe (module 1) couvre déjà l’essentiel. Trois points vus ailleurs sont à rapprocher de l’annexe avant tout ajout : le niveau « équipement », les réserves à lever, la date limite de dénonciation des contrats. [À confirmer]

## 8. Tableaux de bord : erreurs fréquentes et règles simples

- Pour comparer des quantités, l’œil lit bien une longueur ou une position. Il juge mal une surface ou un angle. La couleur ne dit ni « plus » ni « moins ». (« Dashboards: Making Charts and Graphs Easier to Understand », P. Laubheimer, Nielsen Norman Group, 18 juin 2017) [Source professionnelle]
- Jusqu’à 4,5 % des personnes distinguent mal les couleurs, environ 8 % des hommes. La couleur ne fait que renforcer une information déjà donnée autrement. (même source) [Source professionnelle]
- Pratique de 2026 : une liste de choses à faire en ouverture, des états écrits en mots avec une date (voir 1.2).
- Erreurs fréquentes, déduites de ces sources : trop d’indicateurs ; la couleur seule ; un chiffre sans date ni origine ; aucune action proposée ; un graphique là où une liste suffit.
- Règles simples : la prochaine action en haut ; une date écrite à côté de chaque état ; peu de chiffres. Notre annexe dit déjà : douze indicateurs au plus par vue, et chaque chiffre mène à sa source.

## Ce que cela change pour nos livrables

**Livrable 4 (écrans d’exemple).**
- Quatre images fixes, pas de maquette cliquable. En haut de chacune : « Maquette — données fictives ». En pied, phrase possible : « Exemple d’écran. Le logiciel n’existe pas encore. Les écrans définitifs seront décidés avec vous. »
- Données inventées, et visiblement inventées : aucune adresse, entreprise ou personne réelle ; aucun prix d’achat d’immeuble.
- Tableau de bord : en haut, une rubrique « À décider », avec une date limite par ligne. Douze indicateurs au plus. Pas de graphique en secteurs.
- Échéances : l’état en toutes lettres, avec la date et la personne chargée. Exemples : « À faire avant le 15 janvier 2027 », « En retard de 12 jours », « Fait le 3 novembre 2026 ». La couleur vient en plus, jamais seule.
- Fiche bâtiment : suivre le module 1. Jamais « conforme » ; écrire « fait », « manque », « arrive le… ».
- Trois devis : un tableau, une colonne par entreprise, une ligne par poste. Lignes fixes : périmètre, postes « non chiffrés », total HT, taux de TVA, total TTC, délai, durée de validité, attestation décennale « reçue » ou « non reçue », acompte demandé. En pied : « L’outil signale les écarts. Il ne choisit pas. »
- Contraste de 4,5 pour 1, boutons de 24 pixels au moins, texte lisible agrandi à 200 %.

**Livrable 1 (offre et bon de commande).** Pour la moitié versée à la commande, écrire « acompte » ou « arrhes », jamais « versement » seul. Choix à faire valider par un avocat.

**Livrable 2 (texte de l’orateur).** Avant les écrans : « Ce sont des exemples dessinés pour vous. Rien n’est encore construit. » Objection « c’est donc prêt ? » : non ; renvoyer à l’étape « Maquette et essai sur données fictives ».

**Livrable 3 (page pour l’administratrice).** Idée à reprendre : l’outil prépare, elle relit et valide. Il l’aide ; il ne la surveille pas.

**Livrable 5 (kit de cadrage).** Questions à ajouter : qui signe les devis ; l’usage de chaque bâtiment (logement, commerce, salle de spectacle), car la TVA des travaux en dépend ; les contrôles déjà suivis ; les indicateurs voulus, douze au plus.

**Livrables 6 et 7.** À décider par Morgan Olsen et Mathys Couet : images fixes ou maquette cliquable. Préalable à tout envoi : chaque écran relu contre le brief.

**Livrable 8.** Les prix de la partie 3 restent internes. Rien dans cette note sur les logiciels d’hôtel.

**Livrable 9.** La fiche bâtiment prévoit déjà « ERP ou non ». Le type et la catégorie seraient utiles (pratique vue chez Daftar).

## Ce qu’il ne faut pas écrire ou promettre

- « Conforme », « en règle », « aux normes », sur un écran ou dans un texte.
- « Le logiciel fait déjà… ». Rien n’est construit. Pas de date de mise en service sur une maquette.
- « L’IA choisit le meilleur devis » ou « vérifie l’assurance ». Elle lit et signale ; une personne décide.
- Un gain de temps ou un taux de réussite repris d’un éditeur.
- « Accessible » ou « conforme au RGAA » : cela demande un audit. Au plus : « nous suivons les règles de contraste et de lisibilité des WCAG 2.2 ».
- Un taux de TVA pour ses bâtiments ; un avis sur un acompte ou une assurance.
- Le nom, le prix ou une critique de l’autre proposition reçue ; un prix de logiciel du marché.
- De vraies données du client dans la maquette.

## Questions à poser à un professionnel

- Avocat : la mention « Maquette — données fictives » suffit-elle à écarter tout reproche de présentation trompeuse ? Les règles lues sur le devis et les arrhes jouent-elles quand le client est une société ? Acompte ou arrhes dans notre bon de commande ?
- Expert-comptable : quel taux de TVA pour des travaux dans un immeuble qui mêle logements, boutiques et salle de spectacle ? Qui écrit la mention exigée depuis le 1er mars 2025 ?
- Assureur ou courtier : que faut-il lire sur une attestation décennale (activités, dates, lieu) ? Afficher « attestation reçue » nous engage-t-il ?
- Architecte ou maître d’œuvre : quelle grille de postes, par lot, pour comparer trois devis ?
- Spécialiste de l’accessibilité : le RGAA s’impose-t-il à un logiciel privé fait pour un seul client ? Que change le RGAA 5 ?

## Ce qui n’a pas pu être vérifié

- Aucun logiciel n’a été essayé. Fonctions et chiffres viennent des éditeurs ; beaucoup de pages ne sont pas datées.
- Prix des outils de patrimoine technique et des éditeurs américains : non trouvés.
- Un écran « trois devis côte à côte » existe-t-il sur le marché ? Non vu, non exclu.
- Règles du devis et des arrhes pour un client société : non vérifiées.
- Fiche F2034 lue sur une copie, pas sur le site officiel. Article L. 243-2 du code des assurances : non lu sur Légifrance.
- Deux pages d’impots.gouv.fr se contredisent : celle pour les particuliers décrit encore l’ancienne attestation de TVA.
- Un blog annonce le passage des règles de TVA dans un nouveau code au 1er janvier 2027 : non vérifié, adresse non conservée.
- Champ légal du RGAA : non vérifié. Conditions d’usage du Système de design de l’État : non relues. Il est fait pour les sites de l’État ; nous suivons ses règles, sans copier son apparence.
- Aucune source officielle lue sur le risque juridique d’une maquette prise pour un produit fini.
- Critères 7 à 10 de Nielsen : titres lus seulement.

## Sources (liste complète)

Toutes consultées le 10 novembre 2026. « n. d. » : page non datée.

**Textes officiels, autorités et organismes**
- « Web Content Accessibility Guidelines (WCAG) 2.2 », W3C, https://www.w3.org/TR/WCAG22/, recommandation du 5 octobre 2023, page du 12 décembre 2024.
- « What’s New in WCAG 2.2 », W3C, https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/, n. d.
- « Understanding SC 2.5.8: Target Size (Minimum) », W3C, https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html, n. d.
- « RGAA version 4.1.2 » et « Critères et tests », DINUM, https://accessibilite.numerique.gouv.fr/doc/RGAA-v4.1.2.pdf ; https://accessibilite.numerique.gouv.fr/methode/criteres-et-tests/, n. d.
- « Ce qui change avec le RGAA 5 », DesignGouv (DINUM), https://design.numerique.gouv.fr/articles/2026-11-03-rgaa5/, 3 novembre 2026.
- Composants Badge, Alerte et Tableau, Système de design de l’État, https://www.systeme-de-design.gouv.fr/version-courante/fr/composants/badge ; https://www.systeme-de-design.gouv.fr/version-courante/fr/composants/alerte ; https://www.systeme-de-design.gouv.fr/version-courante/fr/composants/tableau, n. d.
- Arrêté du 24 janvier 2017 relatif à la publicité des prix des prestations de dépannage, de réparation et d’entretien dans le secteur du bâtiment et de l’équipement de la maison, article 4, Légifrance, https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000033935526.
- « Devis », DGCCRF, https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/devis, n. d.
- « Acompte, avance, arrhes et avoir : quelles différences ? », Service Public, https://www.service-public.gouv.fr/particuliers/vosdroits/F31187, n. d.
- « Doit-on signer un devis ou un contrat avant de faire réaliser des travaux dans son logement ? », Service Public, https://www.service-public.gouv.fr/particuliers/vosdroits/F2533, n. d.
- « Devis obligatoire : activités concernées », « Documents commerciaux d’une entreprise individuelle », « Documents commerciaux d’une société », Service Public Entreprendre, https://entreprendre.service-public.gouv.fr/vosdroits/F31144 ; https://entreprendre.service-public.gouv.fr/vosdroits/F37370 ; https://entreprendre.service-public.gouv.fr/vosdroits/F37371, n. d.
- « Garantie décennale en assurance construction » (fiche F2034), lue sur une copie : sites.service-information-publique.fr/vias/guide-professionnels/F2034.html, n. d.
- « Quel taux de TVA appliquer pour les travaux réalisés dans les logements ? », impots.gouv.fr, https://www.impots.gouv.fr/professionnel/questions/quel-taux-de-tva-appliquer-pour-les-travaux-realises-dans-les-logements, n. d.
- « Plusieurs taux de TVA », impots.gouv.fr, https://www.impots.gouv.fr/particulier/plusieurs-taux-de-tva, n. d.
- BOI-TVA-LIQ-30-20-90-40, BOFiP, https://bofip.impots.gouv.fr/bofip/1742-PGP.html/identifiant%3DBOI-TVA-LIQ-30-20-90-40-20260909, version du 9 septembre 2026.
- Lus sans être repris : page Accessibilité, CNIL, https://cnil.fr/fr/accessibilite, n. d. ; « Guide des bonnes pratiques des professionnels », Anah, https://www.anah.gouv.fr/sites/default/files/2023-09/202107_RPro_Guide_des_bonnes_pratiques_VF.pdf, juillet 2021 ; un article du blog rgaa-scanner.fr, 18 juillet 2026, non officiel.

**Sources professionnelles : Nielsen Norman Group**
- « 10 Usability Heuristics for User Interface Design », J. Nielsen, https://www.nngroup.com/articles/ten-usability-heuristics/, 24 avril 1994, revu le 30 janvier 2024.
- « Dashboards: Making Charts and Graphs Easier to Understand », P. Laubheimer, https://www.nngroup.com/articles/dashboards-preattentive/, 18 juin 2017.
- « Data Tables: Four Major User Tasks », P. Laubheimer, https://www.nngroup.com/articles/data-tables/, 3 avril 2022.
- « Visual Indicators to Differentiate Items in a List », A. Harley, https://www.nngroup.com/articles/visual-indicators-differentiators/, 7 août 2016.
- « Indicators, Validations, and Notifications », K. Flaherty, https://www.nngroup.com/articles/indicators-validations-notifications/, 17 janvier 2024.
- « Visibility of System Status », A. Harley, https://www.nngroup.com/articles/visibility-system-status/, 3 juin 2018.
- « UX Prototypes: Low Fidelity vs. High Fidelity » et « IA-Based View of Prototype Fidelity », K. Pernice, https://www.nngroup.com/articles/ux-prototype-hi-lo-fidelity/ ; https://www.nngroup.com/articles/ia-view-prototype/, 18 décembre 2016.
- Vidéo « Presenting Low-Fidelity Prototypes to Stakeholders », https://www.nngroup.com/videos/low-fi-prototypes-stakeholders/, 11 août 2017.

**Sources professionnelles : annonces d’intelligence artificielle**
- « Yardi launches Smart AP for Breeze Premier clients », Yardi, https://www.yardi.com/news/press-releases/smart-ap-ai-invoice-automation/, 29 octobre 2025.
- « Yardi Virtuoso launches in-app assistant to deliver support and insights », Yardi, https://www.yardi.com/news/press-releases/yardi-virtuoso-launches-in-app-assistant-to-deliver-support-and-insights/, 9 septembre 2025 ; « Introducing Yardi Virtuoso », https://www.yardi.com/blog/introducing-yardi-virtuoso/, 15 septembre 2025.
- « AppFolio Unveils AI Agents… », AppFolio, https://www.appfolio.com/newsroom/appfolio-ai-agents, 11 juin 2025.
- « AppFolio Deepens Agentic AI Across Leasing, Accounting, and Resident Operations », AppFolio, https://www.appfolio.com/newsroom/appfolio-deepens-agentic-ai-across-leasing-accounting-and-resident-operations, 16 juin 2026.
- « AppFolio Introduces the New Realm-X… », AppFolio, https://www.appfolio.com/newsroom/appfolio-introduces-the-new-realm-x, 29 septembre 2026.
- « MRI Software Introduces AI Agent and Page Assistant… », MRI Software, https://www.mrisoftware.com/news/mri-software-introduces-ai-agent-and-page-assistant-to-transform-property-management-operations/, 2 juin 2025.
- « MRI Software Expands Agora AI to Simplify Leasing and Property Operations », MRI Software, https://www.mrisoftware.com/news/mri-software-expands-agora-ai-to-simplify-leasing-and-property-operations/, 3 novembre 2026.

**Sources professionnelles : pages des éditeurs (n. d. sauf mention)**
- Gestion locative et patrimoine : Amleks, https://amleks.fr/fonctionnalites/ ; Lokabail, https://lokabail.com/pour-les-bailleurs ; SCI Pilot, https://sci-pilot.fr/fonctionnalites ; https://logiciel-gestion-immobilier.com/fonctionnalites/ ; Wexeor, https://www.wexeor.com/fonctionnalites ; Brik Pro, https://pro.brik.com/fonctionnalites et https://brik.com/brik-pro ; PIAIRE, https://piaire.ai/fonctionnalites.
- Maintenance et patrimoine technique : CARL Source Facility (Berger-Levrault), https://www.carl-software.fr/secteurs-activite/facility-management-gestion-technique-du-patrimoine/carl-source-facility/fonctionnalites/ ; DimoMaint FM, https://www.gmao.com/gmao-fm/ ; DriveIM, https://driveim.com/solutions/immobilier-tertiaire/ ; Solare IT, https://www.solare-it.com/outil-gestion-immobiliere/immobilier-professionnel-tertiaire/gestion-technique/ ; OPTIMa, https://gmao.org/secteurs/batiment/ ; Daftar, https://daftar.fr/fonctionnalites/ ; Muvraline Myndea, https://muvraline.com/fr/myndea-2-2/myndea-eam-gmao/, 26 juin 2026 ; Visionsoft, https://visionsoft.tech/gestion-de-patrimoine/, 27 mars 2025.

**Documents du dépôt (lus le 10 novembre 2026)**
- `audit/2026-11-09-audit-presentation-et-offre/travaux/BRIEF.md`
- `pour-carlone/logiciels-et-automatisations/2026-11-09-annexe-specification-logiciel-gestion-proprietes.md`
- `pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md`
- `interne/logiciels-et-automatisations/travaux/r1-marche-et-offre-accord.md`
