# État de l’art à la fin de 2026 — bâtiments, patrimoine et travaux
Document interne — ne pas transmettre à GianLuca Carlone · 11 novembre 2026

Note de chercheur pour le catalogue « State Of The Art ». Sources [B1] à [B23], en partie 7. « Lue » : page ouverte le 11 novembre 2026. « Vue » : résultat de recherche seulement. Preuve : **mesuré**, **annoncé** ou **supposé**. Les obligations et échéances sont déjà établies dans `k8-registre-des-batiments.md` et les logiciels du marché dans `k6-logiciels-gestion-patrimoine-ecrans.md` : non refaits ici.

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

## 4. Vingt idées pour GianLuca Carlone

Dans l’ordre : l’idée — ce qu’il verrait — ce qu’il faut — quand. Effets à mesurer.

1. **L’état zéro en 3D** — chaque bâtiment visitable depuis un lien, avec plans et surfaces — un prestataire de scan portable, l’image calée sur le relevé — 2027, avant tout chantier.
2. **Le dossier pour l’architecte des Bâtiments de France** — façades relevées, vitrines et enseignes simulées, signalées comme simulations — son architecte, l’idée 1 — avant chaque dépôt.
3. **Le survol des toitures** — une maquette 3D de chaque toit, tuiles et gouttières à reprendre, sans échelle — un télépilote en règle — chaque printemps, dès 2027.
4. **Le carnet de chaque bâtiment** — une fiche avec l’identifiant national, pièces datées, diagnostics, garanties — notre outil commun, son administratrice aidée — dès le cadrage.
5. **L’agent des échéances** — chaque lundi, les dates à venir et la pièce attendue, relance préparée — la liste de `k8` relue par un bureau de contrôle — 2027.
6. **Le lecteur de devis** — trois devis sur une même grille, postes oubliés signalés — notre montage, son maître d’œuvre qui relit — premier chantier, 2027.
7. **Le devis face à la facture** — chaque facture électronique comparée ligne à ligne au devis signé, avant paiement — la plateforme agréée de sa société — 2027.
8. **Le lecteur de baux** — congés, échéances et indexations proposés avec une note de confiance — son avocat valide — 2027.
9. **Le chantier vu chaque semaine** — photos à 360° placées sur le plan, avancement pièce par pièce — un outil du marché, l’accord des entreprises — premier chantier.
10. **La mémoire du chantier exposée** — la rénovation capturée en 3D, montrée à l’ouverture de la galerie comme une œuvre documentaire — un artiste, l’idée 9 — 2027-2028.
11. **L’eau des suites** — température de l’eau chaude relevée en continu, carnet sanitaire prérempli, alerte si l’eau refroidit — un plombier, des sondes ; les analyses restent faites — ouverture des suites.
12. **Les détecteurs de fuites d’eau** — alerte sous le jacuzzi, le sauna et les ballons, vanne coupée — un installateur, son assureur consulté — ouverture des suites.
13. **Le climat des œuvres** — température et humidité par salle, historique remis aux prêteurs et à l’assureur — un conservateur-restaurateur fixe les seuils — ouverture de la galerie.
14. **Les machines qui préviennent** — pompe du jacuzzi, ventilation du sauna, chaudière : alerte quand une courbe dérive, entretien avant la panne — capteurs du marché, un mainteneur — 2028.
15. **L’énergie par lieu** — galerie, suites, cabaret, commerces : consommation par mois, défi d’usage avec l’équipe, économies mesurées — sous-compteurs, accès aux relevés — 2027-2028.
16. **Le chauffage qui suit l’agenda** — la salle chaude à l’heure du spectacle, les suites selon les réservations — un intégrateur ; l’obligation de 2030 au-delà de 70 kW — 2028.
17. **Le cabaret en 3D** — la salle, ses jauges et ses issues pour préparer le dossier de sécurité — son bureau de contrôle, son architecte — avant le dépôt.
18. **Les commerces à distance** — chaque local vacant visitable en 3D ; états des lieux d’entrée et de sortie capturés et datés — capture par téléphone, son avocat pour l’annexe au bail — 2027.
19. **Le bouclier des objets connectés** — inventaire signé de chaque capteur, mots de passe changés, réseau à part — un spécialiste de la sécurité — dès le premier capteur.
20. **Le jumeau vivant** — chaque pièce en 3D avec sa température, sa consommation et son dernier contrôle, interrogée en langage courant — les idées 1, 4, 13 et 15 — 2028-2030.

## 5. Faits citables dans un document client

Sources lues le 11 novembre 2026.

1. Le chantier de Notre-Dame de Paris a réuni plus de 170 scientifiques ; un double numérique de la cathédrale a été bâti à partir de relevés 3D faits avant et après l’incendie. [B1, ministère de la Culture, 25 novembre 2024]
2. L’État attribue à chaque bâtiment un identifiant national unique et pérenne, l’ID-RNB ; 38 bases de données l’intègrent déjà. [B2, page consultée le 11 novembre 2026]
3. Avec un scanner portable, un étage entier se relève en une trentaine de minutes, à 5 à 15 mm près selon l’article. [B3, Messe Frankfurt, 22 mai 2026]
4. Dans un concours national, 68 écoles ont réduit leur consommation d’énergie de 11,4 % en moyenne en un an ; la meilleure de 31 %, surtout par ses usages. [B7, Cerema, 5 décembre 2025]
5. La Fédération française du bâtiment présente le drone comme un outil d’inspection et de diagnostic des toitures, qui évite le risque de chute dans de nombreuses situations. [B12, 30 mars 2026]
6. Depuis le 1er septembre 2026, toute entreprise doit pouvoir recevoir des factures électroniques ; les PME les émettront à partir du 1er septembre 2027. [B14, Service Public Entreprendre, 27 février 2026]
7. Dans les hôtels et résidences de tourisme, la température de l’eau chaude se relève au moins une fois par mois et les légionelles s’analysent au moins une fois par an ; l’application à vos neuf suites est à faire valider. [B13, arrêté du 1er février 2010, version en vigueur]
8. Selon un éditeur de sécurité, 75 % de 529 organisations étudiées avaient des automatismes de bâtiment touchés par des failles connues et exploitées. [B8, Claroty, 25 juin 2025]
9. La directive européenne révisée sur la performance énergétique des bâtiments devait être transposée au plus tard le 29 mai 2026 ; elle crée des passeports de rénovation. [B15, Commission européenne]
10. Plus de 14 millions d’espaces ont été numérisés en 3D avec les outils de Matterport, dans 177 pays, selon l’éditeur. [B6, 28 février 2025]

À ne pas citer : les 60 % de LeakBot (livre blanc co-signé par l’éditeur), les 4 200 heures de Mace (méthode inconnue), les taux de justesse de lecture des baux (éditeurs seuls).

## 6. Règles et limites

- **Mesure ou image.** Un « gaussian splatting » ne sert ni à chiffrer ni à concevoir des travaux [B3]. Pour un chantier : géomètre ou scanner sur pied.
- **Drones.** En zone peuplée, vol en catégorie « spécifique », formation agréée et autorisation préalable ; les scénarios nationaux ont pris fin le 1er janvier 2026 [B12 ; B22, vue]. Voisins filmés : données personnelles.
- **Caméras de chantier.** Pas de surveillance constante d’un ouvrier à son poste ; information, consultation des représentants du personnel, conservation d’un mois en principe [B17, page de 2018, règle toujours en vigueur]. Casques à 360° : accord écrit des entreprises.
- **Capteurs dans les suites.** Une présence ou une consommation par suite renseigne sur une personne : données personnelles, information des hôtes, rien dans l’intimité.
- **Sécurité.** Trois organisations sur quatre ont des automatismes vulnérables [B8]. Réseau séparé, inventaire, mises à jour ; règlement sur la cyber-résilience [B16, vue].
- **Pas de « conforme ».** L’outil rappelle et classe [B19]. Un registre de sécurité numérique doit rester consultable et imprimable à tout moment [B18]. Une sonde ne dispense ni des analyses ni du carnet sanitaire [B13, B20].
- **Chiffres d’éditeurs.** Lecture des baux : erreurs sur avenants, définitions et clauses conditionnelles [B21, vue]. Économies d’exploitation : elles s’effacent sans suivi dans la durée [B23, vue].
- **Échecs connus.** Le jumeau qui meurt : 50 à 200 Go par bâtiment, hébergement coûteux, personne pour le lire [B3]. Dépendance : un éditeur racheté peut changer ses conditions [B6] ; exiger l’export des fichiers dans un format ouvert.
- **Contenus simulés.** Vitrine, enseigne ou salle générée : la signaler comme simulation (règlement européen sur l’IA, article 50 ; voir `s1-etat-de-l-art-galerie.md`).

## 7. Sources

Consultées le 11 novembre 2026 ; lues, sauf mention « vue ».

- [B1] Ministère de la Culture, 25 novembre 2024 — https://www.culture.gouv.fr/actualites/special-notre-dame-de-paris-5-6-la-science-a-l-aeuvre
- [B2] Référentiel national des bâtiments, non datée — https://rnb.beta.gouv.fr/ ; arrêté du 23 juin 2026 : vu (lexisveille.fr).
- [B3] Messe Frankfurt, « BIM in Building Operations », 22 mai 2026 — https://building-technologies.messefrankfurt.com/frankfurt/en/media-library/specialized-articles/bim-in-building-operations.html
- [B4] ISPRS Annals XI-M-1-2026 et ISPRS Archives XLVIII-2-W12-2026 : vus.
- [B5] World Labs, 12 novembre 2025 — https://www.worldlabs.ai/blog/marble-world-model
- [B6] Matterport, 28 février 2025 — https://matterport.com/news/costar-group-completes-acquisition-of-matterport-ushering-in-a-new-era-of-3d
- [B7] Cerema, 5 décembre 2025 — https://www.cerema.fr/fr/actualites/114-economies-energie-moyenne-resultats-remise-prix-saison
- [B8] Claroty, 25 juin 2025 — https://claroty.com/blog/claroty-team82-state-of-cps-security-2025-report-building-management-system-exposures
- [B9] LeakBot, livre blanc 2026, non daté — https://leakbot.io/resources/whitepaper/
- [B10] Suffolk, 24 mars 2026 — https://suffolk.com/news/openspace-air-how-drone-based-reality-capture-is-changing-construction-progress-tracking
- [B11] Casestudies.com, Mace et Buildots, non datée — https://www.casestudies.com/company/buildots/case-study/automated-progress-tracking-saves-mace-4200-work-hours
- [B12] Fédération française du bâtiment, 30 mars 2026 — https://www.ffbatiment.fr/techniques-batiment/enveloppe-du-batiment/couverture/dossier/utilisation-drone-couverture
- [B13] Légifrance, arrêté du 1er février 2010, modifié le 30 décembre 2022 — https://www.legifrance.gouv.fr/loda/id/JORFTEXT000021795143
- [B14] Service Public Entreprendre, A17450, mise à jour du 27 février 2026 — https://entreprendre.service-public.gouv.fr/actualites/A17450
- [B15] Commission européenne, page de la directive, non datée — https://energy.ec.europa.eu/topics/energy-efficiency/energy-performance-buildings/energy-performance-buildings-directive_en
- [B16] Commission européenne, « CRA reporting », et cabinets d’avocats : vus — https://digital-strategy.ec.europa.eu/en/policies/cra-reporting
- [B17] CNIL, 23 juillet 2018 — https://www.cnil.fr/fr/la-videosurveillance-videoprotection-au-travail
- [B18] Dépôt : `k8-registre-des-batiments.md`, 10 novembre 2026.
- [B19] Dépôt : `k6-logiciels-gestion-patrimoine-ecrans.md`, 10 novembre 2026.
- [B20] Dépôt : `k14-sauna-jacuzzi-espace-bien-etre.md`, 10 novembre 2026.
- [B21] Basking.io et RETS, blogs d’éditeurs sur la lecture des baux : vus.
- [B22] Question écrite au Sénat du 7 août 2025 ; supports de formation aux scénarios européens : vus.
- [B23] ACEEE, actes de 2024, persistance des économies : vu.
