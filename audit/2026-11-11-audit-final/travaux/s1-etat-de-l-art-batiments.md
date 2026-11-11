# État de l’art à la fin de 2026 — bâtiments, patrimoine et travaux
Document interne — ne pas transmettre à GianLuca Carlone · 11 novembre 2026

Note de chercheur pour le catalogue « State Of The Art ». Sources [B1] à [B22], en partie 7. « Lue » : page ouverte le 11 novembre 2026. « Vue » : résultat de recherche seulement. Preuve : **mesuré**, **annoncé** ou **supposé**. Les obligations et échéances sont déjà établies dans `k8-registre-des-batiments.md` et les logiciels du marché dans `k6-logiciels-gestion-patrimoine-ecrans.md` : non refaits ici.

## 1. En bref

- **Le relevé 3D est devenu accessible.** Un téléphone donne un plan à 1 à 3 cm près ; un scanner portable relève un étage en une demi-heure ; le scanner sur pied reste la seule mesure fine [B3].
- **La belle image n’est pas une mesure.** Les captures en « gaussian splatting » et les mondes générés montrent tout, sans cote fiable [B3, B5].
- **Le jumeau numérique « vivant » reste rare.** Il faut une maquette, des capteurs et quelqu’un qui lit. Notre-Dame en est la vitrine publique [B1].
- **Les gains mesurés viennent d’abord des usages.** Concours national : 11,4 % d’énergie en moins, en un an, surtout par des gestes [B7].
- **Mûr pour une petite structure en 2027 :** état zéro en 3D, carnet numérique par bâtiment, lecture des devis, baux et factures, drone sur les toits, capteurs d’eau et de climat. Une personne valide toujours.

## 2. Ce qui se fait de mieux aujourd’hui

1. **Notre-Dame de Paris (ministère de la Culture, CNRS)** — plus de 170 scientifiques en neuf groupes ; un double numérique compilé à partir de nuages de points d’avant et d’après l’incendie ; données versées sur HumaNum, accès public prévu à la fin du chantier. Mesuré : il existe ; aucun chiffre d’usage. [B1, 25 novembre 2024]
2. **Référentiel national des bâtiments (État)** — un identifiant unique et pérenne par bâtiment, l’ID-RNB. 38 bases l’intègrent ; 43 846 établissements scolaires y sont reliés. [B2, non datée] Un arrêté du 23 juin 2026 l’ajoute au registre des copropriétés. [B2, vue]
3. **Quatre façons de relever un bâtiment (Messe Frankfurt, salon des techniques du bâtiment)** — téléphone à capteur laser : ±10 à 30 mm, en minutes. Scanner portable : ±5 à 15 mm, un étage en une trentaine de minutes, 500 à 3 000 € par jour. Scanner sur pied : ±1 à 3 mm, 1 000 à 10 000 € par jour. Un bâtiment moyen pèse 50 à 200 Go de données brutes. [B3, 22 mai 2026]
4. **Le « gaussian splatting »** — « une représentation visuelle, pas une mesure » ; 1 à 3 cm seulement s’il est calé sur un scanner. [B3] Deux articles scientifiques de 2026 concluent de même : caler l’image sur un relevé laser. [B4, vue]
5. **World Labs, « Marble »** — un monde 3D tiré de quelques photos ou d’une courte vidéo d’un lieu réel ; export en splats et en maillages. Ouvert à tous. Aucune mesure de fidélité publiée. [B5, 12 novembre 2025]
6. **Matterport, racheté par CoStar** — plus de 14 millions d’espaces numérisés dans 177 pays, selon l’éditeur. Le rachat change le propriétaire de vos fichiers 3D. [B6, 28 février 2025]
7. **Cerema, concours CUBE.Écoles** — 68 écoles, 11,4 % d’économies d’énergie en moyenne en un an. Meilleure école : 31 %, par la ventilation réglée, l’extinction automatique, des ferme-portes et la formation du personnel. Un quart des écoles avaient aussi des travaux. Mesuré. [B7, 5 décembre 2025]
8. **Fédération française du bâtiment** — le drone pour inspecter et diagnostiquer les toitures : nuage de points, maquette 3D du toit, devis préparé plus vite, risque de chute évité « dans de nombreuses situations ». [B12, 30 mars 2026]
9. **Suffolk et OpenSpace (États-Unis)** — caméras sur casque ou robot pour les visites ; vues de drone superposées à la maquette pour repérer une fondation mal placée, vérifiée ensuite sur place. Aucun chiffre. [B10, 24 mars 2026]
10. **Mace et Buildots (Royaume-Uni)** — extension d’aéroport : suivi automatique des débuts et fins de tâches ; « écart de 4 200 heures de travail » repéré. Méthode non publiée, page d’éditeur. [B11, non datée]
11. **LeakBot (détecteur de fuites d’eau)** — 60 % de sinistres d’eau du réseau en moins contre un groupe témoin, après trois mois. Livre blanc co-signé par l’éditeur. [B9, 2026]
12. **Lecture des baux (MRI Software)** — lecture avec « notes de confiance » et trace pour la relecture humaine. [B19, 3 novembre 2026] Justesse annoncée par les éditeurs : 85 à 98 % ; aucun banc d’essai indépendant trouvé. [B21, vue]
13. **Échéances réglementaires (Daftar, DriveIM)** — l’outil déduit les contrôles du type et de la catégorie du lieu ; DriveIM écrit : « DriveIM n’est pas un bureau de contrôle ». [B19]
14. **Facture électronique** — toute entreprise reçoit des factures structurées depuis le 1er septembre 2026 ; les PME les émettront au 1er septembre 2027. Les factures d’artisans deviennent lisibles par une machine, ligne par ligne. Texte officiel. [B14, 27 février 2026]

## 3. Ce qui arrive en 2027, 2028, 2030

**2027**

- **Texte officiel.** Émission des factures électroniques par les PME au 1er septembre 2027 [B14]. Coefficient de l’électricité à 1,7 dans le calcul du diagnostic de performance énergétique au 1er janvier 2027 ; toitures solaires ou végétalisées à 50 % au 1er juillet 2027 pour les chantiers concernés ; année de référence OPERAT avant le 30 septembre 2027 [B18].
- **Texte officiel, lu par des sources secondaires.** Règlement européen sur la cyber-résilience : déclaration des failles exploitées depuis le 11 septembre 2026 ; application générale au 11 décembre 2027. Capteurs et automatismes vendus en Europe devront alors répondre à des exigences de sécurité [B16, vue].
- **Annoncé.** Directive européenne sur la performance énergétique des bâtiments : passeports de rénovation, certificats numériques, bases nationales. Transposition due au 29 mai 2026 ; plans nationaux définitifs au 31 décembre 2026 [B15]. L’état de la transposition française n’a pas été lu.
- **Supposé.** La capture 3D par téléphone devient le geste ordinaire de l’état des lieux et de la visite à distance.

**2028**

- **Texte officiel.** Logements classés F interdits à la location au 1er janvier 2028 ; toitures des bâtiments existants d’au moins 500 m² d’emprise au 1er janvier 2028, taux attendu par décret ; ombrières des parcs de 1 500 à 10 000 m² au 1er juillet 2028 [B18].
- **Texte officiel.** Le certificat de performance des bâtiments neufs de plus de 1 000 m² indique leur effet sur le climat, sur tout leur cycle de vie, dès janvier 2028 [B15].
- **Supposé.** Des agents rapprochent devis signés, factures structurées et réserves de chantier, et préparent le paiement pour validation. Aucune source mesurée.

**2030**

- **Texte officiel.** Automatisme de pilotage pour le chauffage ou la climatisation de plus de 70 kW, au renouvellement et au plus tard le 1er janvier 2030 ; moins 40 % d’énergie pour les sites tertiaires de 1 000 m² et plus [B18]. Bilan climat sur cycle de vie pour tous les bâtiments neufs dès janvier 2030 [B15].
- **Supposé.** Le jumeau « vivant » devient abordable : maquette 3D, capteurs et carnet de chaque pièce reliés, interrogés en langage courant. Preuve faible : le stade « capteurs reliés » est décrit [B3], pas mesuré chez un petit propriétaire.
