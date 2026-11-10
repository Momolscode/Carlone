# Le calcul local : NVIDIA DGX Spark, DGX Station et les autres machines possibles

Note de travail interne — sources publiques consultées le 10 novembre 2026 — ce n'est pas un avis juridique, fiscal ou d'investissement.

Rédigée pour nourrir le dixième livrable (« Ce que des moyens supplémentaires nous permettraient d'accomplir », `audit/2026-11-10-preparation-des-livrables/travaux/BRIEF-2.md`, § 9.2). Ce n'est pas le livrable. Rien n'a été acheté, demandé ni commandé. Les prix « constatés » viennent de pages publiques lues le 10 novembre 2026 ; ils peuvent changer d'un jour à l'autre.

Étiquettes : [Officiel] page du fabricant ou d'une autorité ; [Prix public daté] page marchande lue à une date connue ; [Mesure publiée] essai chiffré publié et daté ; [Source professionnelle] presse ou revendeur spécialisé ; [Estimation] calcul de cette note ; [À confirmer] fait sans source vérifiée ce jour.

## En bref

(voir à la fin : « Compléments du 10 novembre 2026 », partie « En bref ». La partie « Vérification du 10 novembre 2026 », tout à la fin, l'emporte sur le reste de la note.)

## 1. NVIDIA DGX Spark

**Ce que c'est.** Un ordinateur de bureau de 15 × 15 × 5 cm, construit autour de la puce NVIDIA GB10 (processeur Arm de 20 cœurs et processeur graphique Blackwell dans le même boîtier). Il sert à faire tourner et à adapter des modèles d'IA ouverts sur place.

Caractéristiques officielles (fiche nvidia.com/fr-fr, lue le 10 novembre 2026) [Officiel] :
- Processeur : Arm 20 cœurs (10 Cortex-X925 + 10 Cortex-A725).
- Mémoire : 128 Go LPDDR5X unifiée et cohérente (partagée entre processeur et processeur graphique). Une version 64 Go existe, « disponible exclusivement auprès des partenaires OEM ».
- Bande passante mémoire : 273 Go/s. C'est elle qui limite la vitesse d'écriture des modèles (voir § 4).
- Performance annoncée : « jusqu'à 1 pétaFLOP » en précision FP4, chiffre théorique avec parcimonie (sparsity). Ce n'est pas la vitesse réelle d'un modèle de langage.
- Stockage : jusqu'à 4 To NVMe M.2, avec auto-chiffrement.
- Réseau : 1 port 10 GbE ; carte ConnectX-7 à 200 Gb/s (deux ports QSFP) ; Wi-Fi 7 ; Bluetooth 5.4.
- Alimentation : 240 W (bloc externe) ; consommation de la puce GB10 (TDP) : 140 W.
- Taille et poids : 150 × 150 × 50,5 mm ; 1,2 kg.
- Logiciel : NVIDIA DGX OS (Linux basé sur Ubuntu), avec NeMo (réglage fin), RAPIDS, NIM, PyTorch, Jupyter, et NemoClaw (pile d'agents). Accès gratuit au catalogue NGC sur inscription.
- Usages annoncés par NVIDIA : inférence de modèles « jusqu'à 200 milliards de paramètres » ; réglage fin « jusqu'à 70 milliards de paramètres ».
- Support matériel : « fourni par le fournisseur qui a vendu le système ».

**Relier plusieurs machines** [Officiel]. Jusqu'à quatre DGX Spark peuvent travailler ensemble par ConnectX-7. Deux ou trois se relient par un simple câble QSFP ; quatre demandent un commutateur réseau. Deux machines de 128 Go donnent 256 Go ; quatre donnent 512 Go, « jusqu'à 700 milliards de paramètres » selon NVIDIA. La fiche conseille un nombre de machines égal à une puissance de 2. (nvidia.com/fr-fr, FAQ.)

**Disponibilité.** Commandes ouvertes en octobre 2025 au prix de lancement de 3 999 $ (recherche interne du 4 novembre 2026, `audit/2026-11-04-audit-strategique/annexes/travaux/ver-R6-marche.md`, ligne 34) [À confirmer : annonce NVIDIA non relue ce jour]. Constructeurs partenaires cités par NVIDIA : Acer, ASUS, Dell, Gigabyte, HP, Lenovo, MSI [Officiel]. La fiche française n'affiche aucun prix ; le bouton « Acheter » renvoie vers la NVIDIA Marketplace et des revendeurs.

**Prix : ce qui a changé en 2025 et 2026.**
- Lancement en France (novembre 2025) : de 2 760 € HT (ASUS Ascent GX10, 1 To) à 3 689 € HT (Founders Edition, 4 To) ; 3 999 € HT (Acer Veriton GN100) (Le Monde Informatique, 18 novembre 2025) [Source professionnelle].
- Fin février 2026 : hausse à 4 699 $ aux États-Unis et 4 800 € sur la boutique NVIDIA européenne (forum développeurs NVIDIA, cité dans `audit/2026-11-04-audit-strategique/annexes/travaux/rj-R6-marche.md`, ligne 373) [Source professionnelle].
- Octobre 2026 : NVIDIA annonce la version 64 Go chez les partenaires « à partir de 4 999 $ » le 23 octobre ; la version 128 Go serait affichée à 6 950 $ sur la boutique NVIDIA (plusieurs sources secondaires concordantes, `ver-R6-marche.md`, ligne 34) [Source professionnelle ; prix 128 Go À confirmer sur la page NVIDIA].
- Suivi de prix d'un comparateur français pour la Founders Edition 4 To : 5 608 € le 1er septembre 2026, 6 916 € le 14 octobre, 9 960 € le 7 novembre, 7 299 € le 8 novembre 2026 (magicprices.fr) [Prix public daté ; TTC probable, à confirmer]. Les prix ont donc plus que doublé en un an et varient de plusieurs milliers d'euros d'une semaine à l'autre.

**Prix constatés en France autour du 10 novembre 2026** [Prix public daté] (détail dans le Tableau des prix) :
- NVIDIA DGX Spark Founders Edition EU, 128 Go, 4 To : 7 500 € HT / 9 000 € TTC (Senetic) ; 5 500 € HT (APY Groupe, revendeur professionnel).
- ASUS Ascent GX10, 128 Go, 1 To : 5 550,22 € HT / 6 660,26 € TTC (Senetic) ; 6 499 € (Amazon, prix du 8 novembre 2026, via 123comparer) ; 6 600 € HT (APY Groupe).
- MSI EdgeXpert MS-C931, 128 Go, 4 To : 6 602,52 € HT / 7 923,02 € TTC (Senetic) ; 8 120 € HT (APY Groupe).
- Dell Pro Max avec GB10, 128 Go, 2 To : de 7 767 € à 8 985,99 € selon le marchand (prix.net) [TTC probable, à confirmer].
- HP ZGX Nano G1n, Lenovo ThinkStation PGX, Acer Veriton GN100, Gigabyte AI TOP Atom : aucun prix français relevé ce jour [À confirmer].

Repère de calcul : pour une machine de 128 Go, il faut compter **environ 5 500 à 7 500 € HT** en novembre 2026, soit à peu près le prix du cadrage proposé à GianLuca Carlone (6 500 € HT) [Estimation].

## 2. NVIDIA DGX Station (GB300)

**Ce que c'est.** Une tour de bureau de classe « centre de données », construite autour de la puce GB300 Grace Blackwell Ultra. Elle vise les équipes de recherche et les entreprises qui entraînent ou servent de très grands modèles.

Caractéristiques officielles (fiche nvidia.com/en-us, lue le 10 novembre 2026) [Officiel] :
- Processeur graphique : 1 Blackwell Ultra, avec 252 Go de mémoire HBM3e (7,1 To/s).
- Processeur : Grace 72 cœurs (Neoverse V2), avec 496 Go LPDDR5X (396 Go/s).
- Mémoire cohérente totale : 748 Go. NVIDIA annonce des modèles « jusqu'à 1 000 milliards de paramètres ».
- Performance annoncée : 20 pétaFLOPS en FP4 (la fiche donne aussi 153, sans dire lequel est avec parcimonie) ; 10 pétaFLOPS en FP8 ; 5 pétaFLOPS en FP16/BF16.
- Réseau : ConnectX-8 jusqu'à 800 Gb/s (2 ports QSFP112), 10 GbE, port de gestion à distance (BMC). Deux stations peuvent être reliées.
- Stockage : 4 emplacements M.2 Gen 5. Une carte RTX PRO Blackwell peut être ajoutée.
- Partage : la technologie MIG découpe le processeur graphique en sept instances isolées, pour plusieurs utilisateurs.
- **Consommation : 1 600 W au total ; la fiche demande « un circuit de 20 A »** (norme américaine). En France, le raccordement (ligne dédiée, protection) est à faire valider par un électricien [À confirmer].
- Format et bruit : non indiqués sur la fiche NVIDIA [À confirmer]. Une machine de 1 600 W refroidie par ventilateurs ou liquide n'est pas silencieuse ; aucun relevé de bruit publié n'a été lu ce jour.
- Système : Ubuntu avec outils NVIDIA ; licence NVIDIA AI Enterprise en option (support éditeur).

**Constructeurs** [Officiel] : ASUS (ExpertCenter Pro ET900N G3), Dell (Pro Max avec GB300), Exxact, Gigabyte (W775-V10-L01), HP (ZGX Fury G1n), MSI (XpertStation WS300), Supermicro (Super AI Station). NVIDIA ne vend pas la DGX Station en direct : « Contact a partner to order your system ».

**Disponibilité.** Fabriquée à la commande. Délais annoncés de 3 à 5 semaines par un revendeur allemand (BuyZero, pages Dell et HP) ; livraison annoncée au 30 décembre 2026 par un revendeur britannique (Scan, ASUS) [Prix public daté]. La fiche NVIDIA propose encore de « s'inscrire pour être prévenu » [Officiel].

**Prix.** Aucun prix public NVIDIA. Prix de revendeurs lus le 10 novembre 2026 [Prix public daté] :
- Fourchette générale : « environ 90 000 à 171 500 € HT » selon le constructeur et la configuration (guide d'achat BuyZero, Allemagne, 5 novembre 2026) [Source professionnelle].
- HP ZGX Fury G1n : 133 193,28 € HT / 158 500 € TTC (BuyZero, Allemagne) ; 109 243,70 € HT cité dans le guide du 5 novembre 2026.
- Dell Pro Max avec GB300 : 171 428,57 € HT / 204 000 € TTC (BuyZero, Allemagne) ; 160 195 $ pour une configuration de 16 To sur dell.com États-Unis.
- ASUS ExpertCenter Pro ET900N G3 : 111 999,99 $ (Central Computer, États-Unis) ; 121 983,12 $ (Neutron USA, mis à jour le 8 novembre 2026) ; 119 999,99 £ (Scan, Royaume-Uni, TVA comprise probable).
- Supermicro, Gigabyte, HP, MSI : 119 600 € « VAT 0 % (export) » chacun ; ASUS 124 200 € ; Dell 172 069 € (ibfusion, prix à l'export, hors TVA).
- Aucun prix français relevé ce jour [À confirmer]. Ordre de grandeur pour la France : **environ 90 000 à 170 000 € HT** [Estimation fondée sur les revendeurs allemands et européens ci-dessus].

**Lecture honnête.** La DGX Station coûte de 13 à 30 fois une DGX Spark. Elle est faite pour entraîner des modèles et servir de nombreux utilisateurs. Pour une équipe de deux personnes qui fait des automatisations et des logiciels de gestion, aucun usage connu ne la justifie aujourd'hui [Estimation].

## 3. Les alternatives

### 3.1 Station de travail avec une carte NVIDIA RTX PRO 6000 Blackwell (96 Go)

- Carte seule : 96 Go de mémoire GDDR7 avec correction d'erreurs ; 600 W pour la version standard, 300 W pour la version Max-Q (fiche LDLC, lue le 10 novembre 2026) [Prix public daté].
- Prix de la carte seule en France, 10 novembre 2026 [Prix public daté] : 14 733,29 € HT / 17 679,95 € TTC (PNY, version OEM, LDLC.pro) ; 17 985,97 € HT / 21 583,16 € TTC (version « bulk », Senetic) ; 19 541,70 € HT / 23 450,04 € TTC (Grosbill Pro) ; Max-Q 15 500,06 € HT / 18 600,07 € TTC (Senetic).
- Il faut un ordinateur hôte (processeur, 128 Go de mémoire, alimentation d'au moins 1 000 W, boîtier ventilé). Coût non relevé ce jour : **environ 3 000 à 6 000 € HT** [Estimation]. Total d'une station complète : **environ 18 000 à 25 000 € HT** [Estimation].
- Avantages : la carte est bien plus rapide que la DGX Spark pour écrire du texte, car sa mémoire est beaucoup plus rapide (environ 1,8 To/s, chiffre NVIDIA non relu ce jour [À confirmer]). Elle sert aussi à l'image et à la vidéo. Écosystème CUDA complet. Pièces remplaçables.
- Limites : 96 Go seulement dans la carte ; prix élevé ; chaleur et bruit d'une tour de 800 à 1 000 W en charge ; montage, pilotes et mises à jour à notre charge ou à celle d'un intégrateur.

**Deux cartes grand public (par exemple deux GeForce RTX 5090 de 32 Go).** 64 Go au total, environ 575 W par carte (chiffre NVIDIA non relu ce jour) [À confirmer]. Prix français non relevé ce jour [À confirmer]. Rapides, mais 64 Go ne suffisent pas pour les grands modèles ; consommation et bruit élevés ; garantie et usage professionnel continu moins adaptés. Option de bricoleur, pas de cabinet de conseil [Estimation].

### 3.2 Apple Mac Studio (M5 Max ou M5 Ultra, 2026)

- **Nouveau en 2026** : Mac Studio M5 Max et M5 Ultra annoncés le 25 août 2026, livrés à partir du 22 septembre ; l'option 512 Go est commandable depuis le 28 octobre 2026 (Apple Newsroom France, 25 août 2026 ; World Is Small, 29 octobre 2026) [Officiel ; Source professionnelle].
- Caractéristiques [Officiel] (apple.com/fr/mac-studio/specs, lue le 10 novembre 2026) : M5 Max jusqu'à 128 Go de mémoire unifiée et 614 Go/s ; M5 Ultra 96, 256 ou 512 Go, 1,2 To/s de bande passante mémoire ; « consommation maximale en continu : 480 W » ; 19,7 × 19,7 × 9,5 cm ; 3,6 kg (M5 Ultra) ; 10 GbE ; Thunderbolt 5.
- Prix France [Prix public daté] : M5 Ultra 96 Go / 1 To à partir de 6 599 € TTC, soit 5 499 € HT (Apple Newsroom et page caractéristiques) ; M5 Ultra 256 Go : 12 429 € TTC, soit 10 357,50 € HT, délai de 13 à 15 semaines (MacGeneration, 4 novembre 2026) ; M5 Ultra 512 Go / 1 To : 25 079 € TTC, soit 20 899,17 € HT, livraisons annoncées du 1er au 8 décembre 2026 (World Is Small, 29 octobre 2026). Le passage de 256 à 512 Go coûte 12 650 € TTC (MacGeneration). Prix du M5 Max 128 Go non relevé [À confirmer].
- Avantages : grande mémoire, bande passante élevée (plus de quatre fois celle de la DGX Spark), silence relatif, faible consommation, aucune installation électrique particulière, prise en main simple, garantie Apple.
- Limites : pas de CUDA (outils MLX, llama.cpp, LM Studio à la place) ; calcul plus lent que NVIDIA pour lire de longs documents d'un coup et pour le réglage fin ; mémoire non extensible ; prix de l'option 512 Go très élevé ; délais de plusieurs semaines.

### 3.3 Mini-PC AMD Ryzen AI Max+ 395 (128 Go)

- Processeur 16 cœurs, graphique Radeon 8060S (40 unités), 128 Go LPDDR5X à 8 000 MT/s, soudés et non remplaçables (fiche GMKtec sur Amazon.fr, lue le 10 novembre 2026) [Prix public daté]. Bande passante d'environ 256 Go/s (bus de 256 bits) [Estimation ; À confirmer sur la fiche AMD]. Processeur réglé à 120 W sur le HP Z2 Mini G1a (comparateur Galaxus) [Source professionnelle].
- Prix [Prix public daté] : GMKtec EVO-X2 128 Go / 2 To : 3 799,96 € TTC (Amazon.fr, 10 novembre 2026) ; 3 499,99 € (LaBonneConfig, mis à jour le 9 novembre 2026) ; 5 559,95 € en rupture (Rue du Commerce). Revendeur européen Mirravolt, TVA comprise : GMKtec 3 381,99 € ; Minisforum MS-S1 Max 3 534,99 € ; HP Z2 Mini G1a 128 Go / 2 To 4 287,99 €. Soit **environ 2 800 à 3 600 € HT** [Estimation].
- Avantages : le moins cher des appareils à 128 Go ; Windows ou Linux ; format très compact ; consommation modeste.
- Limites : bande passante proche de la DGX Spark, donc vitesse d'écriture proche ; logiciels AMD (ROCm, Vulkan) moins mûrs que CUDA ; marques chinoises peu connues pour le service après-vente ; HP Z2 Mini plus sûr mais plus cher.

## 4. Ce que ces machines font réellement

### 4.1 Ce qui tient en mémoire

- Règle simple : taille des poids ≈ nombre de paramètres × bits par paramètre ÷ 8. Un modèle de 70 milliards de paramètres à 4 bits pèse environ 35 Go, plus le contexte (la mémoire de la conversation), les tampons et le système (Cloudzat, 1er novembre 2026) [Source professionnelle].
- Sur une machine de 128 Go (DGX Spark, mini-PC AMD, Mac Studio M5 Max) : un modèle de 120 milliards de paramètres à 4 bits (par exemple gpt-oss-120b) ou un modèle de 27 à 33 milliards en pleine précision. Exemple : Qwen3.8-27B en FP8, 30,9 Go de poids, laisse environ 93 Gio pour le contexte (GPUwerk, 7 novembre 2026) [Source professionnelle].
- Sur 512 Go (Mac Studio M5 Ultra) ou 748 Go (DGX Station) : des modèles plus grands, en précision réduite. Le meilleur modèle ouvert de novembre 2026, Kimi K3.1 Pro, demande 1,56 To pour ses poids (GPUwerk) : il ne tient sur aucune de ces machines sans forte compression [Source professionnelle ; Estimation].

### 4.2 Vitesse mesurée (jetons par seconde)

Le « jeton » vaut environ trois quarts de mot. Deux vitesses comptent : la **lecture** du texte fourni (documents, consignes) et l'**écriture** de la réponse. Une personne lit environ 5 à 10 jetons par seconde [Estimation].

Modèle gpt-oss-120b, format MXFP4, un seul utilisateur [Mesure publiée] :
- DGX Spark : écriture 55,37 jetons/s, lecture 1 725 jetons/s (NVIDIA Developer Blog, cité par SpecPicks le 8 novembre 2026) ; écriture 58,72 jetons/s, lecture 2 443,91 jetons/s (banc officiel llama.cpp, février 2026, cité par AIMultiple). Sur le système livré d'origine, un contributeur mesure 45,87 jetons/s ; le logiciel fait varier le résultat d'environ 30 % (SpecPicks).
- Mini-PC Ryzen AI Max+ 395 (GMKtec EVO-X2) : écriture 47,49 jetons/s, lecture 999,59 jetons/s, même fil de mesures llama.cpp (SpecPicks).
- Mac Studio (puce non précisée) : écriture 95 jetons/s (RigBase, via Ollama) [Mesure publiée ; méthode différente].
- RTX PRO 6000 : écriture 196,31 jetons/s (RigBase) ; 215,2 jetons/s dans le tableau LMSYS (AIMultiple).
- La vitesse baisse quand le contexte s'allonge : sur DGX Spark, de 60,57 à 40,55 jetons/s entre 0 et 32 768 jetons de contexte (SpecPicks) ; −27 % selon AIMultiple.

Modèle dense de 27 milliards (Qwen3.8 27B) : 15,2 jetons/s sur DGX Spark (Q4) contre 150 sur RTX PRO 6000 (NVFP4 avec décodage spéculatif) (RigBase) [Mesure publiée ; méthodes différentes, à ne pas comparer au chiffre près].

Lecture : la DGX Spark lit vite (calcul puissant) mais écrit lentement (mémoire à 273 Go/s). Le mini-PC AMD écrit presque aussi vite, pour environ la moitié du prix ; il lit deux fois moins vite. La RTX PRO 6000 est trois à quatre fois plus rapide, dans la limite de ses 96 Go.

### 4.3 Plusieurs traitements en même temps

- DGX Spark : 32 traitements simultanés de 4 096 jetons chacun donnent 262,20 jetons/s au total, contre 58,72 pour un seul (banc llama.cpp, février 2026, cité par AIMultiple) [Mesure publiée]. Soit environ 4,5 fois plus de texte produit par heure, mais chaque réponse est plus lente.
- DGX Station : découpage en sept instances isolées (MIG) [Officiel]. Aucune mesure de débit lue ce jour [À confirmer].

### 4.4 Autres usages

- Réglage fin : NVIDIA annonce jusqu'à 70 milliards de paramètres sur DGX Spark [Officiel]. Aucune durée mesurée lue ce jour [À confirmer].
- Transcription de réunions, lecture de documents scannés (OCR), génération d'images : ces tâches tournent sur toutes ces machines avec des modèles ouverts. Aucune mesure datée n'a été lue ce jour : vitesse et qualité sur des documents réels de GianLuca Carlone sont **inconnues** [À confirmer par essai].

### 4.5 Écart de qualité avec les modèles de pointe en ligne (novembre 2026)

- Indice Artificial Analysis v5 (publié le 27-28 octobre 2026) : en tête, Claude Opus 5.5 à 58 points ; meilleurs modèles ouverts dont les poids sont téléchargeables : DeepSeek V4.1 Flash et GLM-5.3, à 32 points, soit 26 points derrière, et sous un petit modèle fermé (Claude Haiku 5.5, 36). L'écart entre meilleur ouvert et meilleur fermé passe de 3 points (v4.3) à 12 points (v5) (artificialanalysis.ai, 27 octobre 2026) [Mesure publiée].
- Meilleurs modèles ouverts qui tiennent sur **une** DGX Spark de 128 Go à 4 bits ou plus : environ 20 points, soit 40 points sous le meilleur fermé (GPUwerk, 7 novembre 2026) [Source professionnelle].
- Classement LMArena du 6 novembre 2026 : le premier modèle ouvert est 19e ; les 18 premiers sont fermés (GPUwerk) [Source professionnelle].
- Retard médian des modèles ouverts : environ 4 mois (2 à 8 mois) selon l'indice de progrès d'Artificial Analysis (HuggingNews, 29 octobre 2026) [Source professionnelle].

Conséquence : une machine locale fait bien des tâches simples et répétitives (trier, extraire des champs, résumer, classer). Pour le raisonnement difficile, le code complexe ou la rédaction fine, les modèles en ligne restent nettement meilleurs [Estimation].

## Compléments du 10 novembre 2026

Ajout du relecteur, 10 novembre 2026. La note s’arrêtait après le § 4.5. Il manquait : le « En bref », le « Tableau des prix » annoncé au § 1, les contraintes demandées par le brief (énergie, bruit, compétences, maintenance), l’argument « les données restent chez lui » et l’adéquation à nos usages (BRIEF-2, § 9.2, point 6). Quatre recherches ont été faites pour ces compléments. Les chiffres corrigés par la vérification (partie suivante) sont déjà pris en compte ici.

### En bref

- **Une machine de 128 Go suffit pour nos usages actuels.** DGX Spark, Mac Studio M5 Max 128 Go ou mini-PC AMD : environ 2 800 à 7 500 € HT selon le modèle et le revendeur, prix relevés en novembre 2026 [Prix public daté ; Estimation].
- **La DGX Station n’est pas pour nous.** Environ 90 000 à 171 500 € HT chez un revendeur allemand en octobre 2026, 1 600 W, faite pour entraîner des modèles et servir une équipe. Aucun usage connu de Marwin Tech ne la justifie [Estimation].
- **Les prix bougent vite.** La DGX Spark Founders Edition est passée de 3 999 $ (octobre 2025) à 4 699 $ (février 2026), puis, selon la presse, à 6 950 $ (octobre 2026). Tout prix se cite avec sa date.
- **L’électricité pèse peu.** Une DGX Spark coûte moins de 250 € HT d’électricité par an, même à pleine charge jour et nuit. Une DGX Station peut dépasser 2 300 € HT par an [Estimation, § 5.1].
- **Le vrai argument est la maîtrise des données, pas le prix.** La CNIL juge « généralement plus opportun et plus sécurisé » un déploiement sur site quand on traite des données personnelles ou des documents sensibles (CNIL, 18 juillet 2024). Mais la sécurité de la machine devient alors notre affaire et la sienne (§ 6).
- **Écart de qualité.** Les meilleurs modèles ouverts téléchargeables sont à 32 points sur l’indice Artificial Analysis v5, contre 58 pour le premier modèle fermé au lancement de l’indice (27 octobre 2026). Une machine locale fait bien le tri, l’extraction et le résumé ; le raisonnement difficile reste mieux fait par les modèles en ligne [Mesure publiée ; Estimation].

### 5. Contraintes : énergie, bruit, chaleur, compétences, maintenance

#### 5.1 Énergie

Prix retenu : tarif réglementé (tarif Bleu), option Base 6 kVA, **0,2001 € TTC le kWh au 1er août 2026**, soit environ 0,167 € HT (Selectra, 17 juillet 2026, et ÉlectricitéPasCher, 1er août 2026, d’après la délibération de la CRE n° 2026-147 du 15 juillet 2026) [Source professionnelle]. Le prix réel dépend du contrat du lieu d’installation [À confirmer].

Calcul [Estimation] : « heures de bureau » = 8 h × 220 jours = 1 760 h par an ; « permanent » = 8 760 h par an. Puissance retenue = puissance mesurée en charge, donc un plafond (la machine ne travaille pas à fond tout le temps).

| Machine | Puissance en charge retenue (source) | Heures de bureau : kWh / € HT par an | Permanent : kWh / € HT par an |
|---|---|---|---|
| DGX Spark | 160 W à la prise (Tom’s Hardware, 27 janvier 2026) | 282 kWh / 47 € | 1 402 kWh / 234 € |
| Mini-PC AMD Ryzen AI Max+ 395 | 112 W en inférence (Tom’s Hardware, même essai) | 197 kWh / 33 € | 981 kWh / 164 € |
| Mac Studio M5 Max (base) | 200 W au maximum (Apple, 21 septembre 2026) | 352 kWh / 59 € | 1 752 kWh / 292 € |
| Mac Studio M5 Ultra 512 Go | 385 W au maximum (Apple, 21 septembre 2026) | 678 kWh / 113 € | 3 373 kWh / 562 € |
| Station RTX PRO 6000 | environ 900 W [Estimation : carte 600 W + hôte] | 1 584 kWh / 264 € | 7 884 kWh / 1 315 € |
| DGX Station | 1 600 W (fiche NVIDIA) | 2 816 kWh / 470 € | 14 016 kWh / 2 337 € |

Au repos : DGX Spark environ 35 W (Tom’s Hardware, 27 janvier 2026), réduits d’au plus 18 W par une mise à jour de février 2026 (Tom’s Hardware, 12 février 2026) ; Mac Studio 7 à 9 W (Apple) [Mesure publiée].

Raccordement de la DGX Station : la fiche demande « un circuit de 20 A », norme américaine en 120 V. En 230 V, 1 600 W font environ 7 A ; une ligne dédiée reste prudente. **À faire valider par un électricien** [Estimation].

#### 5.2 Bruit et chaleur

- **DGX Spark** : valeurs déclarées par NVIDIA selon la norme ECMA-109 : puissance acoustique 35 dB(A) en fonctionnement (processeur graphique à fond, 25 °C) et 19 dB(A) au repos ; pression acoustique au poste de l’opérateur 29 dB(A) et 13 dB(A) (fiche nvidia.com/fr-fr, lue le 10 novembre 2026) [Officiel]. Essai : 37,5 dB(A) au plus à 46 cm, pour un bruit de fond de 33 dB(A) ; le boîtier devient très chaud sur un coin (Tom’s Hardware, 27 janvier 2026) [Mesure publiée]. ServeTheHome n’a jamais dépassé 40 dB(A) hors essai de saturation et relève 60 à 90 W en inférence (14 octobre 2025) [Mesure publiée].
- **Mac Studio** : 1 314 BTU/h au maximum pour le M5 Ultra 512 Go, soit 385 W de chaleur (Apple, 21 septembre 2026) [Officiel]. Aucun relevé de bruit lu ce jour [À confirmer].
- **DGX Station** : aucun chiffre de bruit publié lu ce jour. Un revendeur la dit « plus fraîche et plus silencieuse » qu’un serveur et adaptée au bureau (BuyZero, fiche Dell, lue le 10 novembre 2026) [Source professionnelle ; affirmation de vendeur]. 1 600 W dégagés dans une pièce, c’est l’équivalent d’un radiateur électrique ; l’été, une climatisation peut devenir nécessaire [Estimation].
- **Station RTX PRO 6000** : chaleur et bruit d’une tour de 800 à 1 000 W [Estimation ; aucun relevé lu].

#### 5.3 Compétences et maintenance

- **Système.** DGX Spark et DGX Station tournent sous Linux (DGX OS ou Ubuntu) [Officiel]. Il faut savoir installer et mettre à jour des modèles, des pilotes et des services réseau. Mac Studio : prise en main la plus simple. Mini-PC AMD : pilotes et logiciels (ROCm, Vulkan) moins mûrs [Estimation].
- **Garantie et pannes.** Pour la DGX Spark, « la prise en charge matérielle sera fournie par le fournisseur qui a vendu le système » (fiche NVIDIA) [Officiel]. Il faut donc choisir le revendeur aussi pour son service. Les fiches DGX Station de BuyZero incluent trois ans d’intervention sur site pour HP et Dell (guide du 5 novembre 2026) [Source professionnelle].
- **Temps à prévoir.** Mises à jour de sécurité, sauvegardes, surveillance, remplacement en cas de panne : quelques heures par mois au minimum [Estimation à valider]. Chez deux personnes, ce temps est pris sur les missions.
- **Durée de vie utile.** Le matériel d’IA vieillit vite : la DGX Spark a eu deux hausses de prix et une version 64 Go en un an. Prévoir un renouvellement en trois à cinq ans [Estimation]. L’amortissement comptable et fiscal est **à faire valider par l’expert-comptable**.

### 6. « Ses données restent chez lui » : ce qui est vrai, et à quelles conditions

- **Ce qui est vrai.** La CNIL écrit : si l’on fournit au système « des données personnelles (données des clients ou des collaborateurs) ou de la documentation sensible ou stratégique », « il semble généralement plus opportun et plus sécurisé de privilégier le déploiement de solutions “sur site” (on premise) qui présentent l’avantage de limiter les risques d’extraction de données auprès d’un tiers » (CNIL, « Les questions-réponses de la CNIL sur l’utilisation d’un système d’IA générative », 18 juillet 2024) [Officiel].
- **La même page nuance.** Le coût d’un système sur site rend souvent « plus aisé » un hébergement distant, encadré par un contrat de sous-traitance ; une petite entreprise peut y recourir « dès lors que les transferts de données sont encadrés et leur sécurité assurée » (même page) [Officiel].
- **Conditions pour que l’argument reste vrai** [Estimation] :
  1. La machine est achetée et installée au nom de sa société, dans ses locaux.
  2. Les logiciels installés n’envoient pas les documents vers un service en ligne. À vérifier pour chaque outil.
  3. Quelqu’un tient la sécurité : mots de passe, mises à jour, chiffrement du disque (la DGX Spark a un stockage auto-chiffré, fiche NVIDIA), sauvegardes, accès à distance limité.
  4. Les tâches difficiles envoyées à un modèle en ligne partent avec des données réduites ou pseudonymisées (voir k13b).
- **Ce que l’argument ne dit pas.** Une machine locale ne rend pas un traitement conforme à elle seule. Le registre, l’information des personnes et les durées de conservation restent dus. **À faire valider par un avocat ou un conseil en protection des données.**

### 7. Adéquation à nos usages (deux personnes, novembre 2026)

Nos usages connus : lire et classer des documents, extraire des champs, résumer, rédiger des brouillons, relier des logiciels. Tout cela demande peu de calcul, sauf en gros volume [Estimation].

| Scénario | Matériel | Coût d’achat | Ce que cela change | Limite |
|---|---|---|---|---|
| Moyens actuels | Aucun achat ; modèles en ligne payés à l’usage (k13b) | 0 € de matériel | Rien à installer ni à entretenir | Données envoyées à un tiers : à encadrer par contrat |
| Renforcement ciblé | Une machine de 128 Go : DGX Spark, Mac Studio M5 Max 128 Go ou mini-PC AMD | Environ 2 800 à 7 500 € HT [Prix public daté ; Estimation] | Traitements de documents sensibles sur place ; essais de modèles ouverts ; plusieurs traitements en parallèle | Modèles moins bons que les modèles de pointe ; vitesse d’écriture limitée (§ 4.2) |
| Développement ambitieux | Mac Studio M5 Ultra 512 Go, ou station RTX PRO 6000, ou deux DGX Spark reliées (256 Go) | Environ 11 000 à 25 000 € HT [Estimation] | Modèles plus grands ; plus de vitesse ; plusieurs utilisateurs | Installation, chaleur et maintenance ; prix très variables |
| Exclu | DGX Station | Environ 90 000 à 171 500 € HT (BuyZero, octobre 2026) | — | Disproportionné pour deux personnes [Estimation] |

Lecture [Estimation] :
- **Pour Marwin Tech** (essais internes, sans données de clients) : le mini-PC AMD ou un Mac Studio M5 Max suffisent. La DGX Spark se justifie si nous voulons l’écosystème NVIDIA (CUDA, réglage fin).
- **Pour GianLuca Carlone** (machine chez lui, à son nom) : une DGX Spark ou un Mac Studio, installés dans ses locaux, pour traiter sur place les documents qu’il ne veut pas envoyer en ligne. C’est le seul cas où l’argument « ses données restent chez lui » joue pleinement (§ 6).
- **Gain « × N »** : sur DGX Spark, 32 traitements en parallèle produisent environ 4,5 fois plus de texte par heure qu’un seul (§ 4.3, chiffre non revérifié ce jour). Cela ne vaut que pour des tâches répétitives ; la relecture humaine reste le goulet.

### Tableau des prix (récapitulatif)

Prix relevés par la note ou par la vérification. « Vérifié » = page relue le 10 novembre 2026 par le relecteur. Taux de TVA retenu pour les conversions : 20 %.

| Machine | Configuration | Prix | HT ou TTC | Source et date | Statut |
|---|---|---|---|---|---|
| DGX Spark Founders Edition | 128 Go | 3 999 $ → 4 699 $ | Prix conseillé NVIDIA, hors taxes américaines | Forum développeurs NVIDIA, annonce du 23 février 2026 | Vérifié |
| DGX Spark Founders Edition | 128 Go | 6 950 $ | Prix conseillé | Presse, 8 octobre 2026 (titres concordants) | Page NVIDIA non lue |
| DGX Spark (partenaires) | 64 Go | à partir de 4 999 $ | Prix conseillé | Presse, 8 octobre 2026 | Page NVIDIA non lue |
| DGX Spark et dérivés, France | 128 Go | 5 500 à 7 500 € HT | HT | Senetic, APY Groupe (note, § 1) | Non revérifié |
| Mac Studio M5 Max | 36 Go, 512 Go | à partir de 2 999 € | TTC (≈ 2 499 € HT) | Apple Newsroom France, 25 août 2026 | Vérifié |
| Mac Studio M5 Ultra | 96 Go, 1 To | à partir de 6 599 € | TTC (≈ 5 499 € HT) | Apple Newsroom France, 25 août 2026 | Vérifié |
| Mac Studio M5 Ultra | 256 Go | 12 429 € | TTC | MacGeneration, 4 novembre 2026 (note) | Non revérifié |
| Mac Studio M5 Ultra | 512 Go, 1 To | 25 079 € | TTC | World Is Small, 29 octobre 2026 (note) | Non revérifié |
| Mini-PC AMD Ryzen AI Max+ 395 | 128 Go | environ 2 800 à 3 600 € HT | Estimation depuis prix TTC | Amazon.fr, LaBonneConfig, Mirravolt (note, § 3.3) | Non revérifié |
| Carte RTX PRO 6000 Blackwell | 96 Go | 14 733 à 19 542 € HT | HT | LDLC.pro, Senetic, Grosbill Pro (note, § 3.1) | Non revérifié |
| DGX Station (fourchette) | selon constructeur | environ 90 000 à 171 500 € | Net (HT) | BuyZero, guide du 5 novembre 2026, « état octobre 2026 » | Vérifié |
| HP ZGX Fury G1n | GB300 | 133 193,28 € HT / 158 500 € TTC | HT et TTC | BuyZero, fiche produit | Vérifié |
| Dell Pro Max avec GB300 | GB300, 16 To | 171 428,57 € HT / 204 000 € TTC | HT et TTC | BuyZero, fiche produit | Vérifié |
