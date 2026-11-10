# Si un projet d’hébergement existe : choisir un logiciel hôtelier du marché et connaître les obligations d’un petit établissement

Note de travail interne — sources publiques consultées le 10 novembre 2026 — ce n’est pas un avis juridique, fiscal ou d’assurance

Statut : interne, ne pas transmettre à GianLuca Carlone. Auteur : note de recherche pour le livrable 8. Cette note complète, sans les refaire, `audit/2026-11-09-audit-presentation-et-offre/travaux/x3-alternatives-du-marche-hebergement.md` (noté X3), `x2-logiciels-et-services-du-groupe-accor.md` (X2), `interne/logiciels-et-automatisations/travaux/r2-cadre-reglementaire-et-technique.md` (R2) et le module 9 de `pour-carlone/logiciels-et-automatisations/2026-11-09-annexe-specification-logiciel-gestion-proprietes.md` (SPEC).

Point de départ. On ne sait pas si un hébergement est prévu [À confirmer]. Seul indice : la galerie serait installée dans « un ancien bar-restaurant-hôtel avec cour » (déclaration rapportée par Morgan Olsen ; R2, ligne 57 ; `audit/2026-11-10-preparation-des-livrables/travaux/i0-faits-etablis-rapportes-inconnus.md`, ligne 76). Nombre de chambres, forme (hôtel, meublés, chambres d’hôtes) et société exploitante : inconnus.

## En bref

1. Tout ce qui suit est conditionnel. Le livrable 8 commence par une question : « Un hébergement est-il prévu ? Sous quelle forme, combien de chambres, quelle société l’exploite ? »
2. La forme choisie change presque tout : un hôtel est un établissement recevant du public avec locaux à sommeil (visites de la commission de sécurité, même petit) ; un meublé de tourisme demande une déclaration en mairie, bientôt un numéro national, et une étiquette énergétique minimale ; des chambres d’hôtes sont limitées à cinq chambres et quinze personnes.
3. Le logiciel hôtelier s’achète. Pour 5 à 40 chambres, un ensemble complet coûte de l’ordre de 1 000 à 3 600 € par an (X3). Marwin Tech aide à choisir, paramètre, relie les totaux au registre des bâtiments. Elle ne développe pas, n’exploite pas, n’encaisse pas.
4. Les critères décisifs : export complet des données, sortie sans pénalité, données dans l’Union européenne, paiement par un prestataire (aucune carte stockée), caisse certifiée si un bar ou un restaurant est encaissé, liaison avec une plateforme agréée pour la facture électronique (au plus tard le 1er septembre 2027 pour une PME), assistance en français.
5. Une enseigne ou une chaîne volontaire apporte des clients et une marque, pas du personnel. Elle se paie à la cotisation fixe (quelques milliers d’euros par an) ou au pourcentage du chiffre d’affaires.
6. Chaque obligation (taxe de séjour, fiche de police, classement, affichage des prix, fiscalité) se fait confirmer par un professionnel et par la mairie de Cosne-Cours-sur-Loire avant d’être écrite dans un document client.

## 1. Critères de choix d’un logiciel hôtelier pour 5 à 40 chambres

**À retenir : un logiciel hôtelier se choisit d’abord sur ce qu’on peut en sortir (données, contrat), ensuite sur ce qu’il relie (canaux, paiement, caisse, facture électronique), enfin sur ses fonctions.**

### 1.1 Fonctions de base attendues

- Planning des chambres, réservations, tarifs, facturation des séjours, taxe de séjour, fiches de police, paiement (SPEC, module 9, ligne 417) [Source professionnelle — document interne du 9 novembre 2026].
- Ces fonctions sont déjà présentes dans les logiciels du marché pour petits hôtels : planning, vente en ligne, lien avec les plateformes, factures (X3, section 5) [Source professionnelle].
- Rapports : nuitées, taux d’occupation, chiffre d’affaires, taxe de séjour collectée et à reverser. Ce sont les totaux que l’outil commun reprendrait (SPEC, ligne 430) [Source professionnelle].

### 1.2 Liaisons à vérifier

| Liaison | Pourquoi | Ce qu’il faut obtenir par écrit |
| --- | --- | --- |
| Gestionnaire de canaux | Publier les mêmes chambres sur plusieurs sites de réservation sans double vente | Liste des sites reliés ; prix selon le nombre de sites (chez Thaïs, 30 € par mois pour un site, 90 € pour cinq et plus : X3, S1) |
| Moteur de réservation | Vendre en direct sur le site de l’établissement, sans commission de plateforme | Compris ou en option ; commission éventuelle |
| Paiement | Encaisser arrhes et séjours | Prestataire de paiement nommé ; aucune donnée de carte saisie ou stockée par la société (SPEC, ligne 425 ; R2, ligne 230) |
| Serrures et clés | Arrivée autonome, si l’établissement n’a pas d’accueil permanent | Marques de serrures reliées ; coût du matériel à part [À confirmer, aucune source lue] |
| Caisse du bar et du restaurant | Encaisser les consommations sur la note du séjour | Certificat de la caisse (voir 1.3) |
| Plateforme agréée de facturation | Facture électronique et transmission des données de vente | Nom de la plateforme reliée ; format d’échange |
| Comptabilité | Transmettre les ventes à l’expert-comptable | Format d’export choisi par l’expert-comptable |
| Outil commun de Marwin Tech | Reprendre des totaux, sans donnée nominative | Export des totaux journaliers ou interface de programmation ouverte |

### 1.3 Obligations que le logiciel doit tenir

- **Caisse certifiée ou attestée : la règle a bougé deux fois.** Tout logiciel qui enregistre des paiements de particuliers doit être certifié par un organisme accrédité ou attesté par son éditeur (CGI, article 286, I, 3° bis ; R2, ligne 39) [Texte officiel, lu par R2]. La loi de finances pour 2025 avait supprimé l’attestation de l’éditeur, avec un report au 1er septembre 2026. La loi de finances pour 2026 (loi n° 2026-103 du 19 février 2026, article 125) l’a rétablie ; le BOFiP l’aurait commentée le 25 mars 2026, avec un modèle d’attestation (BOI-LETTRE-000242) (legifiscal.fr ; lemondedudroit.fr ; lhotellerie-restauration.fr, extraits du moteur de recherche) [Source professionnelle — à confirmer sur Légifrance et le BOFiP]. Conséquence : écrire « caisse certifiée, ou attestée par l’éditeur selon le modèle officiel », et demander la pièce. Amende : 7 500 € par système (R2, ligne 39) [À confirmer].
- **Facture électronique.** Une entreprise assujettie doit pouvoir recevoir des factures électroniques depuis le 1er septembre 2026. Une PME doit émettre et transmettre ses données de vente (e-reporting pour les clients particuliers) au plus tard le 1er septembre 2027 (R2, lignes 84 à 86 et 112) [Texte officiel, lu par R2]. Un logiciel hôtelier n’est pas une plateforme agréée : il doit être relié à une plateforme agréée (R2, ligne 33) [Texte officiel, lu par R2].
- **Taxe de séjour.** Au réel, elle est perçue avant le départ, sur une ligne distincte, hors base de TVA, puis reversée aux dates de la délibération (R2, ligne 226, d’après la fiche F743 de Service Public Entreprendre) [Autorité ou organisme].
- **Fiche individuelle de police.** Remplie par tout client étranger à l’arrivée ; conservée six mois ; remise à la police ou à la gendarmerie sur demande (CESEDA, R814-1 à R814-3 ; R2, ligne 227) [Texte officiel]. Destruction au bout de six mois (délibération CNIL n° 2016-176, R2, ligne 228) [À confirmer, texte repéré, non lu].
- **Paiement par carte.** La norme PCI DSS est un standard privé imposé par le contrat bancaire. Le plus simple : aucune donnée de carte chez l’exploitant, tout passe par un prestataire de paiement (R2, ligne 230) [Source professionnelle].

### 1.4 Données, sortie, contrat, assistance

- **RGPD.** L’éditeur traite des données de voyageurs pour le compte de l’exploitant : il faut un contrat de sous-traitance écrit (RGPD, article 28) [Texte officiel, connu, non relu ce jour]. Demander le lieu d’hébergement des données (Union européenne ou garanties écrites) et la liste des sous-traitants (SPEC, ligne 421) [Source professionnelle].
- **Réversibilité.** Export complet dans un format ouvert, testé avant signature (SPEC, lignes 420 et 443) [Source professionnelle]. Demander : quelles données (réservations, clients, factures, historique), quel format, quel délai, quel coût, combien de temps après la résiliation.
- **Durée d’engagement.** Thaïs affiche un abonnement « mensuel et sans engagement de durée » ; Sirvoy offre un mois en paiement annuel (X3, vérification, points 1 et 2) [Source professionnelle, pages d’éditeurs lues le 9 novembre 2026]. Les autres éditeurs : non vérifié [À confirmer].
- **Assistance en français.** Thaïs est un éditeur français (X3, section 1) [Source professionnelle]. Pour les autres : langue, horaires, canal (téléphone, messagerie), délai de réponse et coût de la mise en place sont à demander par écrit [À confirmer].
- **Prix.** Pour 10 chambres : 79 € par mois chez Sirvoy Pro (taxes non précisées) ; 130 à 190 € HT chez Thaïs avec moteur et canaux. Pour 25 chambres : 149 € et 235 à 295 € HT (X3, section 1 et vérification) [Source professionnelle]. Pour 5 ou 40 chambres : non vérifié [À confirmer].

## 2. Compléments à X3 : offres, prix publics 2026, intelligence artificielle

**À retenir : peu de prix nouveaux. Amenitiz ne publie toujours aucun prix. L’IA des logiciels hôteliers sert surtout à répondre aux messages des clients et à proposer des prix. Elle ne remplace ni l’accueil ni les obligations.**

- **Amenitiz (page relue ce jour).** Aucun montant affiché : « Votre tarif dépend de vos chambres. » Deux formules, Core et Advanced, prix mensuels sur devis. Logiciel, moteur de réservation et gestionnaire de canaux compris ; paiement intégré à « 1,5 % + 0,25 € » ; « Migration de données offerte » ; « Opérationnel en 30 jours ou le premier mois est offert ». Modules payants : site, serrures connectées, conseil de prix. Leur caisse n’est proposée qu’en Espagne et au Portugal. Assistance « dans votre langue maternelle », dont le français, par téléphone, messagerie et courriel ; horaires non indiqués. Export et lieu d’hébergement des données : non mentionnés (amenitiz.com/fr/nos-tarifs, non datée, lue le 10 novembre 2026) [Source professionnelle — page de l’éditeur]. Cela corrige X3 : le code [FV] de la ligne Amenitiz devient vérifié pour le paiement (1,5 % + 0,25 €), et le reste est précisé.
- **IA chez Amenitiz.** « Ami » propose des réponses rédigées par IA aux messages des clients, dans leur langue, avec « trois modes au choix : manuel, brouillon automatique ou réponse automatique ». Un module de gestion des prix (« Amenitiz RMS ») est annoncé « à partir du T4 2026 » (même page) [Source professionnelle]. Pour nos livrables : seul le mode « brouillon » correspond au niveau « Assistée » (une personne valide).
- **Ordre de grandeur publié par d’autres éditeurs.** Pour 20 chambres, 100 à 300 dollars par mois ; un abonnement affiché à 100 dollars peut atteindre 300 dollars avec le gestionnaire de canaux, le moteur, les utilisateurs et la mise en place (smartorder.ai, 2026, éditeur concurrent, extrait du moteur) [À confirmer — source intéressée]. Utile seulement comme mise en garde : toujours demander le coût total, modules compris.
- **IA et prix dynamiques.** Les mentions d’IA trouvées portent surtout sur des outils de prix (par exemple PriceLabs) et sur les avis clients, pas sur le logiciel hôtelier lui-même (résultats de recherche du 10 novembre 2026) [À confirmer].
- **Mews, Thaïs, eviivo, Little Hotelier, RoomRaccoon** : offres et IA 2026 non relues ce jour [À confirmer]. Les prix Thaïs et Sirvoy de X3 restent les seuls vérifiés.

**Prudence.** Une réponse automatique envoyée à un client engage l’exploitant (prix, conditions d’annulation, accès). Un prix proposé par une machine reste une décision de l’exploitant. Les données des voyageurs passent chez l’éditeur et parfois chez un fournisseur d’IA : à couvrir par le contrat de sous-traitance [À confirmer par un juriste].

## 3. Obligations d’un petit hôtel, de meublés de tourisme ou de chambres d’hôtes

**À retenir : trois formes, trois régimes. L’hôtel relève de la sécurité incendie des établissements recevant du public. Le meublé relève de la déclaration nationale (depuis le 20 mai 2026) et d’une étiquette énergétique minimale. La chambre d’hôtes reste chez l’habitant, limitée en taille.**

### 3.1 Hôtel : établissement recevant du public avec locaux à sommeil

- Les hôtels sont des établissements de type O. En 5e catégorie, l’effectif total est limité à 100 personnes ; hébergement en sous-sol interdit (GHR, « Sécurité incendie dans les HCR », 8 janvier 2026) [Source professionnelle].
- Petit hôtel de 5e catégorie : détection automatique d’incendie, alarme audible dans les chambres, déclencheurs manuels, extincteurs à chaque niveau, éclairage de sécurité, consignes affichées dans les chambres, registre de sécurité à jour (même source) [Source professionnelle].
- Vérifications techniques : article PO 1 de l’arrêté du 22 juin 1990 ; tous les deux ans pour les hôtels de 5e catégorie selon le tableau de la page ; installations électriques chaque année (même source) [Source professionnelle — à confirmer sur le texte].
- Personnel : deux séances d’instruction par an sur l’incendie et l’évacuation (même source) [Source professionnelle].
- Commission de sécurité : visite de réception avant ouverture, et avant réouverture après plus de dix mois de fermeture (même source) [Source professionnelle]. Visites périodiques : 5 ans pour un établissement de 5e catégorie avec locaux à sommeil (`audit/2026-11-10-preparation-des-livrables/travaux/k8-registre-des-batiments.md`, ligne 51) [À confirmer] ; une réponse ministérielle ancienne parle d’une visite « au moins une fois tous les cinq ans » conseillée par une circulaire de 1990 (assemblee-nationale.fr, extrait du moteur) [À confirmer].
- Registre de sécurité : il doit porter les dates des exercices d’incendie depuis le 1er juillet 2026 (R2, ligne 40) [Texte officiel, lu par R2]. Changement 2026.
- Les petits hôtels ont eu des règles renforcées par un arrêté publié le 4 août 2006, puis par l’arrêté du 26 octobre 2011 (échéancier de travaux) (extraits du moteur) [À confirmer].
- Un ancien hôtel fermé depuis longtemps doit être traité comme une ouverture : visite de réception, mise aux normes, accessibilité [À confirmer par la mairie et un bureau de contrôle].

### 3.2 Meublés de tourisme

- **Déclaration nationale depuis le 20 mai 2026.** L’article L324-1-1 du code du tourisme, dans sa version en vigueur depuis le 20 mai 2026 (loi n° 2024-1039 du 19 novembre 2024), impose une déclaration préalable « en personne » auprès d’un téléservice national ; celui-ci délivre « sans délai » un numéro de déclaration, transmis à la commune (Légifrance, article L324-1-1, lu le 10 novembre 2026) [Texte officiel]. Changement 2026.
- **Le téléservice national n’est peut-être pas encore ouvert.** Des sites professionnels disent que la déclaration passe encore par la mairie (Cerfa 14004) et que la mise en service est annoncée pour le quatrième trimestre 2026 (cpim.fr, socic.fr, extraits du moteur) [À confirmer auprès de la mairie]. La page de la Direction générale des entreprises lue ce jour date du 10 février 2025 et décrit l’ancien régime (entreprises.gouv.fr) [Autorité ou organisme, page ancienne].
- **Sanctions** : jusqu’à 10 000 € pour défaut de déclaration, 20 000 € pour fausse déclaration (article L324-1-1, V) [Texte officiel].
- **Données des plateformes** : le décret n° 2026-196 du 19 mars 2026 organise la transmission des données des plateformes vers la Direction générale des entreprises, puis vers les communes (Légifrance) [Texte officiel]. Changement 2026.
- **Performance énergétique** : entre le 21 novembre 2024 et le 31 décembre 2033, logement classé A à E ; à partir du 1er janvier 2034, A à D ; le maire peut suspendre le numéro en cas de logement insalubre (economie.gouv.fr, extrait du moteur) [Autorité ou organisme — à relire]. Le calendrier « F en 2025, E en 2028 » concerne les résidences principales louées, pas les meublés de tourisme (décret n° 2015-587, annexe, extrait) [Texte officiel — à relire].
- **Classement volontaire** : une à cinq étoiles, valable cinq ans, visite par un organisme accrédité, 133 critères (entreprises.gouv.fr, 10 février 2025) [Autorité ou organisme].

### 3.3 Chambres d’hôtes

- Chez l’habitant ; cinq chambres et quinze personnes au plus ; au moins trois services sur quatre (accueil, petit-déjeuner, linge, ménage) ; déclaration en mairie avant la première location (Cerfa 13566), sinon 450 € d’amende ; activité commerciale à immatriculer ; prix affichés ; fiche de police pour les clients étrangers, conservée six mois (Service Public Entreprendre, F17452, vérifiée le 21 mai 2026) [Autorité ou organisme].
- Surfaces minimales : 7 m² pour une personne, 9 m² pour deux ; une salle d’eau et un WC pour cinq personnes ; table d’hôtes : menu unique, table commune ; alcool : formation, permis d’exploitation et licence (même source) [Autorité ou organisme].
- Limite pour GianLuca Carlone : il faut que l’exploitant habite sur place. Une société propriétaire de bâtiments ne remplit pas cette condition [À confirmer par un juriste].

### 3.4 Classement des hôtels

- Volontaire ; référentiel de l’arrêté du 29 décembre 2021, appliqué depuis le 1er avril 2022 ; renouvellement tous les cinq ans ; inspection par un organisme accrédité par le COFRAC, puis inscription par Atout France (Légifrance ; atout-france.fr, extraits du moteur) [Texte officiel — à relire]. Changements récents : nouveaux panonceaux (arrêté du 13 février 2025) ; décret n° 2026-14 du 14 janvier 2026 sur le renouvellement du classement, dont certaines dispositions s’appliquent depuis le 1er septembre 2026 (Légifrance, extrait du moteur) [À confirmer].

### 3.5 Taxe de séjour, affichage des prix, fiscalité

- **Taxe de séjour** : au réel ou au forfait, selon la délibération de la commune ou de l’intercommunalité (R2, ligne 226) [Autorité ou organisme]. Tarifs de Cosne-Cours-sur-Loire ou de Cœur de Loire : non trouvés [À confirmer]. Les tarifs déclarés par les collectivités sont publiés par l’État et consultables par commune (collectivites-locales.gouv.fr, extrait) [Autorité ou organisme].
- **Affichage des prix d’un hôtel** (arrêté du 18 décembre 2015) : prix de la nuitée toutes taxes comprises ; à l’extérieur, le prix de la prochaine nuitée en chambre double, le petit-déjeuner et l’accès à internet ; à la réception, en plus, les heures d’arrivée et de départ ; dans la chambre, le prix des prestations annexes ; en ligne, le prix définitif à tout moment de la réservation. Taxe de séjour au réel : montant indiqué près du prix (Légifrance ; GHR ; DGCCRF, extraits) [Texte officiel — à relire]. Les meublés relèvent d’un autre texte [À confirmer].
- **Impôt sur le revenu, location en nom propre** (revenus 2025) : meublé non classé, seuil 15 000 €, abattement 30 % ; meublé classé et chambres d’hôtes, seuil 77 700 €, abattement 50 % (impots.gouv.fr, modifiée le 6 juillet 2026) [Autorité ou organisme]. Changement 2025. Seuil 2026 pour les chambres d’hôtes : 83 600 € (F17452) [Autorité ou organisme]. Pour une société soumise à l’impôt sur les sociétés, ces règles ne s’appliquent pas telles quelles [À confirmer par l’expert-comptable].
- **TVA** : 10 % sur l’hébergement et la table d’hôtes, 20 % sur l’alcool, sauf franchise (F17452) [Autorité ou organisme].
