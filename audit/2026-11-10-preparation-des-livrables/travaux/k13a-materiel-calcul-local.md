# Le calcul local : NVIDIA DGX Spark, DGX Station et les autres machines possibles

Note de travail interne — sources publiques consultées le 10 novembre 2026 — ce n'est pas un avis juridique, fiscal ou d'investissement.

Rédigée pour nourrir le dixième livrable (« Ce que des moyens supplémentaires nous permettraient d'accomplir », `audit/2026-11-10-preparation-des-livrables/travaux/BRIEF-2.md`, § 9.2). Ce n'est pas le livrable. Rien n'a été acheté, demandé ni commandé. Les prix « constatés » viennent de pages publiques lues le 10 novembre 2026 ; ils peuvent changer d'un jour à l'autre.

Étiquettes : [Officiel] page du fabricant ou d'une autorité ; [Prix public daté] page marchande lue à une date connue ; [Mesure publiée] essai chiffré publié et daté ; [Source professionnelle] presse ou revendeur spécialisé ; [Estimation] calcul de cette note ; [À confirmer] fait sans source vérifiée ce jour.

## En bref

(complété en fin de rédaction, voir plus bas)

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

