# Introduire des aides par l’IA auprès d’une administratrice : droit du travail, formation, bonnes pratiques

Note de travail interne — sources publiques consultées le 10 novembre 2026 — ce n’est pas un avis juridique, fiscal ou d’assurance

Document interne : ne pas transmettre à GianLuca Carlone ni à son administratrice. Tout ce qui touche au droit du travail est à faire valider par un avocat en droit social.

Étiquettes : [Texte officiel] = texte de loi ou de règlement ; [Autorité ou organisme] = CNIL, ministère, Commission européenne, ANACT, OCDE… ; [Source professionnelle] = site spécialisé, cabinet, revue ; [À confirmer] = non vérifié ce jour, ou dit de mémoire.

Point de départ : on ne sait rien de l’administratrice. Ni son nom, ni son statut (salariée ou prestataire), ni son employeur, ni sa date d’arrivée, ni ses pouvoirs (`audit/2026-11-10-preparation-des-livrables/travaux/i3-page-pour-l-administratrice.md`, § 1.6). Tout ce qui suit est donc écrit « si elle est salariée » ou « si elle est prestataire ».

## En bref

(À compléter en fin de rédaction.)

## 1. Information préalable, proportionnalité, comité social et économique, surveillance

### Les faits

- **Information préalable.** « Aucune information concernant personnellement un salarié ne peut être collectée par un dispositif qui n’a pas été porté préalablement à sa connaissance. » Version en vigueur depuis le 1er mai 2008 (Code du travail, art. L1222-4, lu sur code.travail.gouv.fr). [Texte officiel]
- **Proportionnalité.** Le Code du travail interdit les restrictions aux droits et libertés des personnes qui ne seraient pas « justifiées par la nature de la tâche à accomplir ni proportionnées au but recherché » (Code du travail, art. L1121-1, cité de mémoire, page non relue ce jour). [À confirmer]
- **Trois conditions cumulées selon la CNIL.** Un dispositif de contrôle doit être « proportionné à l’objectif poursuivi », soumis au comité social et économique « dans les entreprises privées de 50 salariés et plus », et « porté à la connaissance des personnes concernées, préalablement à sa mise en place ». L’employeur définit l’objectif et vérifie qu’« il n’existe pas de moyen moins intrusif » (CNIL, « Travail, ressources humaines : le contrôle de l’activité des personnes employées », page datée du 9 juillet 2026). [Autorité ou organisme]
- **Surveillance permanente.** « placer les membres du personnel sous surveillance permanente est en général considéré comme une atteinte excessive » (même page CNIL). [Autorité ou organisme]
- **Ce que la CNIL juge acceptable ou non.** Un enregistreur de frappe est disproportionné. Un logiciel transparent qui remonte à l’encadrant le seul nombre de dossiers traités par trimestre est jugé proportionné. La CNIL conseille de mesurer sur de longues périodes, car la productivité varie pour des raisons extérieures (même page CNIL). [Autorité ou organisme]
- **Un outil ne doit pas avoir d’objectif caché.** Exemple de la CNIL : un outil d’optimisation de tournées ne doit pas servir à contrôler la vitesse (même page CNIL). [Autorité ou organisme]
- **Sanction récente.** En décembre 2024, la CNIL a sanctionné de 40 000 € une société immobilière qui comptait des périodes d’« inactivité » et prenait des captures d’écran régulières des postes (CNIL, « Surveillance excessive des salariés : sanction de 40 000 euros à l’encontre d’une entreprise du secteur immobilier » ; résumé de recherche, page non ouverte). [Autorité ou organisme, détail à confirmer]
- **Seuils du comité social et économique.** La consultation sur les outils de contrôle vaut à partir de 50 salariés (page CNIL ci-dessus). Un comité est mis en place à partir de 11 salariés pendant douze mois consécutifs, avec des missions réduites sous 50 (Code du travail, art. L2311-2 et L2312-38, cités de mémoire). [À confirmer]

### Ce que « on mesure la tâche, jamais la personne » exige concrètement

Avec une seule utilisatrice, toute mesure d’usage est une mesure de cette personne. C’est le point le plus délicat. Le dépôt prévoit déjà deux traces qui la concernent directement : un journal « qui a demandé, qui a validé, ce qui a été fait », et une fiche de relevé avec une colonne « personne » (`pour-carlone/logiciels-et-automatisations/2026-11-09-automatisations-fiches-detaillees.md`, sections 1.3 et 1.4). Ces deux traces sont des informations qui la concernent personnellement : l’art. L1222-4 s’applique. [Analyse interne, à faire valider par un avocat]

Conséquences pratiques, déduites des sources ci-dessus [Analyse interne] :

1. **Dire avant.** Une page écrite, remise avant le premier usage, liste ce que chaque outil enregistre : journal des actions, fiche de temps, historique des conversations avec l’IA. Elle dit qui peut le lire et combien de temps on le garde.
2. **Un seul but, écrit.** Le journal sert à retrouver une erreur et à prouver qui a validé un envoi. Il ne sert jamais à juger son rythme ou sa présence. Cette règle s’écrit dans la charte (partie 6).
3. **La fiche de temps est tenue par elle.** Elle la remplit, elle la voit, elle peut la corriger. On compare la tâche avant et après, pas des journées.
4. **Résultats agrégés.** Le bilan donne des totaux par tâche et par mois : nombre de dossiers, temps moyen, erreurs trouvées. Pas de courbe jour par jour, pas d’heure de connexion.
5. **Comptes nominatifs, oui ; tableau de suivi individuel, non.** Un compte à son nom est nécessaire pour la sécurité et pour savoir qui a validé. Le tableau de bord de l’éditeur qui affiche l’activité par utilisateur n’est pas ouvert à l’employeur, ou il est désactivé si l’outil le permet. [À confirmer outil par outil]
6. **Durée courte.** La fiche de relevé est détruite ou rendue anonyme à la fin de l’essai. Durée du journal à fixer par écrit. [À confirmer avec un avocat]
7. **Rien de caché.** Pas de mesure de frappe, de capture d’écran, de temps d’inactivité, ni d’analyse du ton de ses messages.

## 2. Règlement européen sur l’IA (règlement 2024/1689)

### Les faits

- **Article 4, maîtrise de l’IA : applicable depuis le 2 février 2025** (règlement 2024/1689, art. 113 ; lu par la note `audit/2026-11-04-audit-strategique/annexes/travaux/rj-R4-donnees-ia.md`, partie d). [Texte officiel]
- **Article 4 réécrit en 2026.** Le règlement de simplification dit « Omnibus IA » (règlement 2026/1744 du 8 juillet 2026, publié le 24 juillet 2026, en vigueur le 27 juillet 2026) a changé le texte. Nouvelle rédaction : les fournisseurs et les déployeurs « prennent des mesures pour favoriser le développement de la maîtrise de l’IA par leur personnel et les autres personnes s’occupant du fonctionnement et de l’utilisation des systèmes d’IA pour leur compte […]. Cette obligation ne contraint pas […] à garantir un niveau spécifique de maîtrise de l’IA par un individu » (même note rj-R4, lignes 293 et 325). L’ancienne rédaction imposait de « garantir » un niveau suffisant. **Changement 2026.** [Texte officiel, lu par l’équipe le 4 novembre 2026]
- **Pas d’amende propre à l’article 4.** L’article 99 du règlement ne le vise pas (même note rj-R4, ligne 298). [Texte officiel, lu par l’équipe]
- **« Autres personnes » : la prestataire aussi.** L’article 4 vise le personnel et « les autres personnes » qui utilisent les systèmes pour le compte de l’entreprise. Une administratrice prestataire est donc concernée elle aussi. [Analyse interne, à confirmer]
- **Article 26, déployeurs de systèmes à haut risque.** Le déployeur utilise le système selon la notice (§ 1). Il confie le contrôle humain à des personnes qui ont « les compétences, […] la formation et l’autorité nécessaires » (§ 2). Les employeurs informent « les représentants des travailleurs et les travailleurs concernés » avant de mettre en service un tel système au travail (§ 7). Les personnes visées par une décision prise ou facilitée par un système de l’annexe III en sont informées (§ 11) (Commission européenne, Service d’assistance sur le règlement IA, page « Article 26 », texte consolidé au 27 juillet 2026). [Autorité ou organisme]
- **Annexe III, point 4 : emploi et gestion des travailleurs.** Sont à haut risque les systèmes destinés au recrutement et à la sélection (annonces ciblées, tri des candidatures, évaluation des candidats). Le sont aussi ceux qui servent à décider des conditions de travail, d’une promotion ou d’un licenciement, à répartir des tâches selon le comportement ou les traits de la personne, ou à suivre et évaluer ses performances et son comportement (règlement 2024/1689, annexe III, point 4 ; résumé de mémoire, texte exact non relu ce jour). [Texte officiel, à confirmer mot pour mot]
- **Calendrier du haut risque après le report.** Annexe III : 2 décembre 2027 au lieu du 2 août 2026. Annexe I (produits réglementés) : 2 août 2028 (Omnibus IA, art. 113, c, i ; note rj-R4, lignes 268 et 287). **Changement 2026.** [Texte officiel, lu par l’équipe]
- **Interdiction déjà en vigueur.** Depuis le 2 février 2025, l’article 5 interdit les systèmes qui déduisent les émotions d’une personne sur le lieu de travail, sauf raisons médicales ou de sécurité (règlement 2024/1689, art. 5, § 1, f ; de mémoire). [Texte officiel, à confirmer]
- **Transparence depuis le 2 août 2026.** Article 50 : une personne doit savoir qu’elle parle à une IA ; un trucage réaliste fait par IA doit être signalé (note `audit/2026-11-09-audit-presentation-et-offre/travaux/r1-nouveautes-ia-automatisation-2026.md`, fiche 8.3). Cela vise surtout les échanges avec le public, pas un brouillon relu par l’administratrice. [Texte officiel, lu par l’équipe]

### Ce que doit faire un petit employeur, en pratique

1. **Article 4.** Prendre des mesures et pouvoir le montrer : une charte d’une page, une prise en main écrite, une formation courte datée, une revue chaque année (note rj-R4, ligne 337). Ce n’est pas une obligation de résultat. [Analyse interne]
2. **Article 26.** Il ne s’applique qu’aux systèmes à haut risque. Les aides prévues (tri du courrier, brouillons, résumés, rappels d’échéances) n’en sont pas, a priori. Elles le deviendraient si un outil servait à évaluer ou à répartir le travail de l’administratrice selon son comportement. [Analyse interne, à faire valider]
3. **Pourquoi « l’IA ne note jamais un candidat ni un salarié ».** Quatre raisons. (a) Ces usages sont à haut risque (annexe III, point 4) : à partir du 2 décembre 2027, ils imposent contrôle humain, information, notice, suivi. Une petite structure ne peut pas porter cette charge. (b) Le report ne rend pas ces usages anodins : le Code du travail et la CNIL s’appliquent déjà (partie 1). (c) Une notation par l’IA d’une seule personne identifiable est, de fait, une surveillance individuelle. (d) C’est la règle déjà écrite dans les documents clients (`pour-carlone/logiciels-et-automatisations/2026-11-09-automatisations-fiches-detaillees.md`, section 5). [Analyse interne]

## 3. Formation : obligation, financement, offres publiques

### Les faits

- **Obligation d’adaptation au poste.** « L’employeur assure l’adaptation des salariés à leur poste de travail. Il veille au maintien de leur capacité à occuper un emploi, au regard notamment de l’évolution des emplois, des technologies et des organisations » (Code du travail, art. L6321-1, cité de mémoire, page non relue ce jour). Une formation qui sert à tenir le poste se fait, en principe, sur le temps de travail (art. L6321-2, de mémoire). [À confirmer]
- **Convention collective possible pour une galerie.** La convention des commerces de détail non alimentaires (IDCC 1517, brochure 3251) couvre les « galeries d’art (œuvres d’art) », avec les antiquités et la brocante (Legisocial, fiche IDCC 1517 ; résultat de recherche, page non ouverte). Un avenant récent revoit la liste des codes d’activité (résultat de recherche). [Source professionnelle, à confirmer]
- **Opérateur de compétences probable : l’OPCO Commerce.** Un arrêté du 29 mars 2019 agréant l’OPCO Commerce cite l’IDCC 1517 (DREETS Bretagne, document « OPCO Commerce » ; résultat de recherche, document non ouvert). [Autorité ou organisme, à confirmer pour 2026]
- **Mais tout dépend de son employeur réel.** La convention suit l’activité principale de la société qui l’emploie, pas celle de la galerie. Si elle est salariée d’une société qui détient les bâtiments, d’un futur cabaret ou d’un hôtel, la convention et l’opérateur changent. De mémoire : spectacle vivant → AFDAS ; hôtels, cafés, restaurants → AKTO. [À confirmer]
- **Plan national « Osez l’IA ».** Présenté en juillet 2025. Objectif 2030 : 50 % des très petites entreprises et 80 % des PME et ETI utilisent l’IA. Il prévoyait une « Académie de l’IA », plateforme gratuite de formations en ligne (ministère de l’Économie, DGE, page « Le plan national Osez l’IA » ; Maddyness, 1er juillet 2025). Un bilan d’étape a eu lieu à Bercy le 3 septembre 2026 (Banque des Territoires, « Le plan Osez l’IA veut passer de la sensibilisation à l’action »). [Autorité ou organisme ; détails par résumé de recherche]
- **France Num.** La page « Exploitez l’intelligence artificielle : Osez l’IA » vise commerçants, artisans et TPE-PME, sans expertise requise. Elle annonce une formation en ligne gratuite sur les bases de l’IA et des « Cafés IA France Num » (francenum.gouv.fr ; résumé de recherche, page non ouverte). [Autorité ou organisme, à confirmer]
- **Catalogue public de solutions.** La DGE a publié un catalogue de solutions d’IA pour PME et ETI daté du 30 juillet 2026 (entreprises.gouv.fr, PDF ; non ouvert). [Autorité ou organisme, contenu à confirmer]
- **Accompagnement gratuit par le réseau ANACT-ARACT.** L’ARACT Hauts-de-France propose un accompagnement gratuit allant jusqu’à huit jours, avant déploiement, et invite à « associer vos salariés et managers à la réflexion » (résultat de recherche sur anact.fr). Offre de l’ARACT Bourgogne-Franche-Comté (région de la Nièvre) : inconnue. [Autorité ou organisme ; offre locale à confirmer]
- **Financement.** Conditions de prise en charge par l’opérateur (plafonds, organisme certifié Qualiopi exigé) : non vérifiées sur une source officielle. Un blog privé l’affirme ; ce n’est pas une preuve. [À confirmer auprès de l’opérateur, par l’employeur]

### Ce qu’on en retient

La première formation peut être courte et faite par Marwin Tech pendant la mise en service : prise en main, charte, cas d’erreur. Elle répond à l’article 4 (partie 2) et à l’article L6321-1. Elle se fait sur le temps de travail et se note (date, durée, contenu). Le financement par un opérateur reste une piste à vérifier par l’employeur ; on ne l’annonce pas. Rappel : la suite « formation » se commande à part (`audit/2026-11-09-audit-presentation-et-offre/travaux/a3-exactitude-et-engagements.md`, ligne 77). Marwin Tech n’est pas un organisme de formation certifié : à vérifier avant toute promesse de prise en charge. [Analyse interne]

## 4. Évolution du poste

### Les faits

- **Nouvelles tâches dans sa qualification = simple changement des conditions de travail.** « L’octroi de nouvelles tâches qui correspondent à la qualification du salarié constitue un simple changement des conditions de travail » ; pas d’avenant nécessaire (justice.fr, fiche « Modification du contrat de travail du salarié », reprise de service-public ; résumé de recherche). [Autorité ou organisme, à confirmer]
- **Modification du contrat = accord écrit de la salariée.** Exemples cités : fonctions sans rapport avec sa qualification, accroissement des responsabilités, toute modification de la rémunération (fiche du service du travail de Polynésie française, juin 2025 : principe général du droit du travail, à confirmer pour la métropole). [Source à confirmer]
- **Refus.** Refuser un simple changement des conditions de travail peut être fautif ; refuser une modification du contrat ne l’est pas (Weblex, « Modifier un contrat de travail : comment faire ? »). Pour un salarié protégé, même un changement des conditions demande son accord. [Source professionnelle]
- **Un nouvel outil de bureau** relève en principe du pouvoir de direction, s’il reste dans sa qualification. Aucune source lue ne traite de l’IA en particulier. [À confirmer par un avocat]
- **Charge de travail.** L’employeur doit prévenir les risques, y compris ceux liés à l’organisation du travail (Code du travail, art. L4121-1, de mémoire). [À confirmer] Le dépôt écrit déjà : « Les premières semaines, la mise en place prend souvent plus de temps qu’elle n’en fait gagner » (`pour-carlone/logiciels-et-automatisations/2026-11-09-automatisations-fiches-detaillees.md`, section 1.4).
- **Période d’essai.** Elle vient d’être engagée : elle est peut-être en période d’essai. Durées maximales de mémoire : deux mois pour les employés, trois pour les agents de maîtrise, quatre pour les cadres, renouvelable une fois si un accord de branche le prévoit (Code du travail, art. L1221-19 à L1221-21). [À confirmer]

### Ce qu’on en retient [Analyse interne, à faire valider]

1. **Deux points peuvent faire basculer vers une modification du contrat.** (a) Lui donner par écrit le pouvoir de valider des envois, des devis ou des dépenses : c’est peut-être un « accroissement des responsabilités ». (b) Lui confier le contrôle hebdomadaire des outils comme une tâche nouvelle et durable. À poser à l’avocat.
2. **Fiche de poste.** Pas trouvée comme obligation légale. Utile quand même : une fiche mise à jour, écrite avec elle, dit ce qui reste à elle et ce que l’outil prépare.
3. **Temps dédié.** Le temps de relevé, d’essai et de formation est du temps de travail. Il se prévoit dans son planning, sans rien lui retirer en douce.
4. **Période d’essai : le piège.** Pendant cette période, l’employeur évalue ses compétences. Une fiche de temps ou un journal lu à ce moment-là pourrait servir à la juger. Deux options pour la feuille de décisions : reporter le relevé de temps après la période d’essai, ou écrire noir sur blanc que ces données ne servent jamais à l’évaluer.

## 5. Bonnes pratiques d’accompagnement

### Les faits

- **Associer les personnes dès le début.** Le réseau ANACT-ARACT insiste sur un dialogue « social, professionnel et technique » dès l’introduction d’une technologie, et organise des échanges sur les métiers touchés par l’IA (ARACT Normandie, « Transitions et travail #1 : l’IA au cœur des transformations », Caen). Une synthèse indexée par l’ANACT recommande de « concevoir et mettre en œuvre des expérimentations organisationnelles » (portail de veille ANACT, notice « Le développement du dialogue social technologique en France »). [Autorité ou organisme ; résumés de recherche, pages non ouvertes]
- **Peu de salariés se sentent accompagnés.** Selon une enquête Malakoff Humanis et BCG citée par le portail de veille de l’ANACT, 20 % des salariés se disent assez accompagnés sur l’IA, contre 56 % des managers (date de l’enquête inconnue). [Source professionnelle, à confirmer]
- **LaborIA.** Laboratoire du ministère du Travail et d’Inria, créé en novembre 2021 pour cinq ans. Son rapport « LaborIA Explorer » (13 mars 2023) a interrogé 250 décideurs d’entreprises de plus de 50 salariés. Constats : les craintes baissent une fois l’outil en place ; ceux qui n’ont pas essayé craignent surtout une perte de lien entre collègues ; il recommande un compromis trouvé par le dialogue interne (travail-emploi.gouv.fr, « enquête LaborIA », PDF ; Centre Inffo). **Limites** : questionnaire passé avant l’arrivée massive de l’IA générative ; décideurs seulement ; grandes structures. [Autorité ou organisme]
- **Expérimentation de l’État, 2026.** L’évaluation de l’« Assistant IA » des agents publics (DITP, juin 2026, avec un consortium qui comprend LaborIA-Inria) indique que 60,5 % des testeurs pensent avoir progressé pendant l’évaluation (modernisation.gouv.fr ; chiffre lu dans un résumé de recherche, PDF refusé à l’ouverture). [Autorité ou organisme, à confirmer]
- **OCDE, études expérimentales.** Dans un essai auprès de 444 professionnels, l’accès à ChatGPT a réduit le temps des tâches d’écriture d’environ 40 % et amélioré la qualité d’environ 18 %. Les gains sont plus forts pour les moins expérimentés. Les effets d’ensemble, dans la durée, restent incertains ; une étude note une baisse de la réflexion autonome chez les utilisateurs ; les effets varient selon les personnes (OCDE, billet « Unlocking productivity with generative AI: Evidence from experimental studies », juillet 2025 ; rapport « The effects of generative AI on productivity, innovation and entrepreneurship », juin 2025). [Autorité ou organisme ; résumé de recherche]
- **OCDE, petites entreprises.** Un rapport de novembre 2025 indique que l’IA générative aide à réduire la charge de travail du personnel des PME (OCDE, « Generative AI and the SME Workforce: New Survey Evidence »). [Autorité ou organisme ; résumé de recherche, chiffres non lus]
- **Limites communes de ces études.** Tâches courtes et isolées, souvent en laboratoire, souvent déclaratives. Aucune ne porte sur une administratrice seule dans une petite structure française. Elles ne permettent pas d’annoncer un gain à GianLuca Carlone. [Analyse interne]

### Pratiques à retenir [Analyse interne, fondée sur les sources ci-dessus et sur les fiches du dépôt]

1. **Elle choisit avec nous.** Les tâches à outiller se listent avec elle (étape « Repérer » des fiches). On lui demande aussi ce qu’elle veut garder tel quel.
2. **Une tâche à la fois, sur un petit périmètre.** C’est déjà la méthode du dépôt (une société, un lieu ou un bâtiment).
3. **Du temps prévu, pas pris sur ses soirées.** Formation, relevé et essai sont sur le temps de travail.
4. **Un droit d’arrêt.** « Toute personne qui constate le problème, sans autorisation préalable » peut arrêter une aide (fiches, étape 8). On lui dit, par écrit.
5. **Une voie de retour.** À créer : un carnet partagé « ce qui ne marche pas », lu à chaque point, avec une réponse sous un délai fixé. Les demandes de changement passent par GianLuca Carlone.
6. **Un bilan qu’elle relit avant son employeur.** Le bilan de l’essai parle de la tâche. Elle peut le corriger avant sa remise.

## 6. Charte d’usage de l’IA dans une petite structure

### Les faits

- **France Num et CNIL, fiche pour les TPE et PME (mars 2025)** : « N’introduisez pas de données confidentielles, personnelles ou stratégiques » dans les outils grand public ; une charte d’usage est recommandée (note `audit/2026-11-04-audit-strategique/annexes/travaux/rj-R4-donnees-ia.md`, ligne 446). [Autorité ou organisme, lu par l’équipe]
- **Violation de données.** Une fuite de données personnelles se notifie à la CNIL dans les 72 heures (RGPD, art. 33 ; même note, ligne 242). [Texte officiel, lu par l’équipe]
- **Force de la charte.** Au-delà de 50 salariés, le règlement intérieur est obligatoire ; une charte qui prévoit des sanctions y est souvent rattachée. Sous ce seuil, son statut (note de service, annexe au contrat) est à faire préciser (Code du travail, art. L1311-2, de mémoire). [À confirmer]

### Contenu type, une page [Analyse interne]

1. **But** : l’IA prépare, une personne décide.
2. **Outils permis** : ceux de la liste, sur les comptes de la société, en offre professionnelle, sans entraînement sur nos données. Pas de compte personnel, pas d’outil gratuit grand public, pas d’extension de navigateur non validée.
3. **Données interdites** : mots de passe, coordonnées bancaires, pièces d’identité, santé, salaires, données d’un salarié ou d’un locataire hors besoin, informations sur des acheteurs ou des œuvres non publiques, sauf outil validé pour cela.
4. **Vérification humaine** : tout texte est relu ; tout montant vient d’une formule testée ; toute source est ouverte avant d’être citée.
5. **Quatre verbes interdits à l’outil** : envoyer, payer, signer, supprimer, sans validation d’une personne habilitée.
6. **Contenus pour le public** : dire qu’on parle à une IA ; signaler une image réaliste générée.
7. **Ce que les outils enregistrent**, qui le lit, combien de temps ; ce que ces traces ne servent jamais à faire (partie 1).
8. **Incident** : à qui le dire, tout de suite ; pas de reproche pour un signalement fait de bonne foi.
9. **Droit d’arrêt et voie de retour** (partie 5).
10. **Formation et revue** : une prise en main datée ; une relecture chaque année.

## 7. Si elle est prestataire indépendante

### Les faits

- **Présomption d’indépendance.** « Est présumé travailleur indépendant celui dont les conditions de travail sont définies exclusivement par lui-même ou par le contrat les définissant avec son donneur d’ordre » (Code du travail, art. L8221-6-1, en vigueur depuis le 6 août 2008 ; lu par la note `audit/2026-11-04-audit-strategique/annexes/travaux/rj-R3-travail-contrats.md`, lignes 71 et 90). [Texte officiel, lu par l’équipe]
- **Requalification.** Le statut d’indépendant tombe si « les conditions réelles d’exécution du travail révèlent l’existence d’un lien de subordination » (service-public, fiche F1691, vérifiée le 21 novembre 2025 ; même note, ligne 94). Exemple de statut jugé « fictif » : Cass. soc., 4 mars 2020, n° 19-13.316 (même note, ligne 93). [Autorité ou organisme ; jurisprudence lue par l’équipe]
- **Consignes.** Si elle dépend d’une autre société, ses consignes passent par son employeur ou par son contrat, pas par Marwin Tech (`audit/2026-11-09-audit-presentation-et-offre/travaux/a3-exactitude-et-engagements.md`, ligne 432). Faire travailler une personne sous les ordres d’un tiers expose au prêt de main-d’œuvre illicite (note rj-R3, lignes 114 à 128). [Analyse de l’équipe, à valider]

### Ce qui change [Analyse interne, à faire valider]

| Sujet | Si elle est salariée | Si elle est prestataire |
|---|---|---|
| Information sur ce que l’outil enregistre | Code du travail, art. L1222-4, et RGPD | RGPD seulement (information de la personne, de mémoire art. 13). Le devoir d’informer reste |
| Comité social et économique | Selon l’effectif de son employeur | Sans objet chez GianLuca Carlone |
| Formation | Due par l’employeur (art. L6321-1) | À sa charge ; son propre fonds de formation (lequel : à confirmer). L’article 4 du règlement IA vise quand même « les autres personnes » qui utilisent les outils pour l’entreprise |
| Charte | Note interne, ou annexe au règlement intérieur | Clause ou annexe de son contrat de prestation |
| Fiche de temps | Mesure de la tâche, tenue par elle | Attention : imposer un relevé de temps, des horaires, des outils et un contrôle hebdomadaire sont des indices de subordination. À écrire dans son contrat comme livrable, ou à éviter |
| Comptes et outils | Fournis par l’employeur | Accès donnés par la société cliente, dans les limites de son contrat |
| Qui lui parle | Son employeur | Son donneur d’ordre, par son contrat ; jamais Marwin Tech en direct |

Conséquence pour la page du livrable 3 : on écrit une version qui tient dans les deux cas. Aucun mot ne suppose son statut (« votre contrat », « votre employeur » sont à éviter).

## 8. Ton et formulations

### Ce que disent les sources

- Les craintes portent sur la perte de lien et baissent après la mise en place (LaborIA Explorer, 2023). [Autorité ou organisme]
- Une large part des salariés ne se sent pas accompagnée (enquête citée par l’ANACT, à confirmer). [Source professionnelle]
- Le réseau ANACT recommande de discuter du travail réel, de faire des essais et d’associer les personnes (partie 5). [Autorité ou organisme]
- Aucune source publique trouvée sur les mots exacts à employer. Le tableau ci-dessous est une proposition de l’équipe, fondée sur les audits du dépôt (`audit/2026-11-09-audit-presentation-et-offre/travaux/a1-point-de-vue-gianluca.md`, lignes 198 à 220 ; `audit/2026-11-10-preparation-des-livrables/travaux/i3-page-pour-l-administratrice.md`, § 1.4 et § 3). [Analyse interne]

### Ce qui rassure, ce qui inquiète

Rassure : savoir d’avance ce qui change et quand ; pouvoir dire non à une aide ; garder la main sur la décision ; un temps prévu ; savoir ce qui est enregistré ; garder ses compétences ; un interlocuteur nommé.

Inquiète : les mots « productivité », « optimiser », « gain de temps » sans chiffre ; tout ce qui ressemble à un compteur ; un outil qui « fait à sa place » ; un étranger qui parle d’elle à son employeur ; l’impression qu’on a déjà décidé pour elle.

| À préférer | À éviter |
|---|---|
| « L’outil prépare un brouillon. Vous le corrigez et vous décidez. » | « L’IA s’occupe de vos courriers. » |
| « On mesure la tâche, jamais la personne. » | « On mesure votre productivité. » |
| « Vous choisissez avec nous les tâches à essayer. » | « Nous allons automatiser votre poste. » |
| « Au début, cela vous prendra du temps. Nous vous dirons combien avant de commencer. » | « Cela ne vous prendra rien. » |
| « Vous pouvez arrêter une aide qui ne marche pas, sans demander. » | « Il faudra vous adapter. » |
| « Voici ce que l’outil enregistre, et qui peut le lire. » | « Aucune donnée n’est enregistrée. » |
| « Si cela ne sert pas, on arrête. » | « Vous gagnerez des heures chaque semaine. » |
| « Vous gardez les comptes et les outils, même si nous partons. » | « Notre solution. » |

## Ce que cela change pour nos livrables

**Livrable 3 — page pour l’administratrice (principal).**
- Ajouter un bloc « Ce que les outils enregistrent » : le journal (qui a demandé, qui a validé, ce qui a été fait), la fiche de temps qu’elle tient, l’historique des échanges avec l’IA. Pour chacun : à quoi il sert, qui le lit, combien de temps on le garde (« durée fixée avec vous avant le début »). C’est l’information préalable de l’art. L1222-4.
- Phrase possible : « Ces traces servent à retrouver une erreur et à savoir qui a validé. Elles ne servent jamais à juger votre travail. »
- Phrase possible : « Les bilans donnent des totaux par tâche et par mois. Pas de suivi jour par jour, pas d’heure de connexion. »
- Bloc « Votre temps » : rappeler que formation, relevé et essai se font sur le temps de travail. Ne pas reprendre le chiffre du logiciel (6 à 10 jours) pour le cadrage.
- Bloc « Si quelque chose ne marche pas » : droit d’arrêt sans autorisation ; carnet « ce qui ne marche pas » ; réponse sous un délai à fixer.
- Ne jamais écrire « votre contrat » ou « votre employeur » : la page doit tenir si elle est prestataire.
- Mention de pied : « Ces règles seront confirmées par GianLuca Carlone et ses professionnels avant tout démarrage. »

**Livrable 1 — offre et bon de commande.** Ajouter trois lignes : aucune notation ni surveillance de personnes ; une charte d’usage remise à la mise en service ; l’information des personnes concernées faite par leur employeur avant le premier usage, avec un modèle fourni par Marwin Tech.

**Livrable 2 — texte d’orateur.** Objection probable : « Vous allez surveiller mon administratrice ? » Réponse : « Non. On mesure la tâche, jamais la personne. Elle tient elle-même la fiche, et elle sait d’avance ce que l’outil garde. » Autre objection : « Il faudra la former ? » Réponse : « Une prise en main courte, sur son temps de travail, au moment de la mise en service. Une formation plus longue se commande à part. »

**Livrable 4 — écrans d’exemple.** Pas d’écran « activité par utilisateur », pas de classement, pas de compteur de temps par personne. Le journal affiche un rôle (« validé par : administration ») ou un nom fictif, avec la mention « Maquette — données fictives ». Le bilan de l’essai montre des totaux par tâche.

**Livrable 5 — kit du cadrage.** Guide du premier entretien, questions à poser à GianLuca Carlone (pas à elle en direct) : son statut ; la société qui l’emploie ; sa date d’arrivée ; période d’essai en cours ; l’effectif de chaque société ; la convention collective et l’opérateur de compétences ; les outils d’IA déjà utilisés, y compris sur des comptes personnels. Tableau d’inventaire : rubrique « effectif, instances, convention ». Trame du dossier : une section « information des personnes, charte, formation ».

**Livrable 6 — feuille de décisions.** Décider : (a) relevé de temps reporté après la période d’essai, ou engagement écrit de ne jamais s’en servir pour l’évaluer ; (b) durée de conservation du journal et de la fiche ; (c) qui rédige l’information préalable (son employeur, sur modèle de Marwin Tech) ; (d) si Marwin Tech rédige la charte ; (e) qui reçoit ses retours, sous quel délai.

**Livrable 7 — préalables.** Marwin Tech applique elle-même l’article 4 : sa propre charte et une formation notée de Morgan Olsen et Mathys Couet avant tout démarrage. Ajouter aux questions pour l’avocat celles de la section « Questions à poser à un professionnel ».

**Livrable 8 — logiciel hôtelier.** Les logiciels hôteliers du marché tiennent souvent un journal par utilisateur et des tableaux d’activité du personnel (à confirmer par éditeur). Mêmes règles : information préalable, pas d’usage pour noter le personnel ; vérifier ce qu’on peut désactiver.

**Livrable 9 — cabaret et commerces.** Chaque embauche future relève des mêmes règles. Suivre l’effectif de chaque société : un comité social et économique dès 11 salariés, des consultations sur les outils de contrôle dès 50. Le haut risque (annexe III) s’appliquera le 2 décembre 2027 à tout outil de tri de candidats : à exclure pour les recrutements du cabaret.

**Échéances utiles.** Article 4 : déjà applicable. Article 50 : depuis le 2 août 2026. Annexe III, haut risque : 2 décembre 2027. Charte : relecture chaque année.

## Ce qu’il ne faut pas écrire ou promettre

1. « Conforme au règlement européen sur l’IA », « conforme au RGPD », « validé par la CNIL ».
2. « Aucune donnée n’est enregistrée » ou « tout est anonyme » : avec une seule utilisatrice, rien n’est anonyme.
3. « Votre administratrice gagnera X heures » : aucun chiffre avant la mesure.
4. « Formation prise en charge par l’OPCO » ou « gratuite » : non vérifié.
5. « Productivité », « performance », « suivi de son activité ».
6. « L’IA remplace », « fait à sa place », « automatise son poste ».
7. Tout ce qui suppose son statut, son nom, ses pouvoirs ou sa période d’essai.
8. « Pas besoin de l’informer, ce n’est pas de la surveillance. »
9. Une phrase qui lui donne une consigne, ou qui nous fait la diriger.
10. Une durée de formation précise (« une heure suffit »).

## Questions à poser à un professionnel

**Avocat en droit social.**
1. Le journal des actions et la fiche de temps, tenus pour une seule personne, sont-ils un « dispositif » au sens de l’art. L1222-4 ? Quelle information écrite suffit ?
2. Lui donner par écrit un pouvoir de valider des envois ou des dépenses est-il une modification de son contrat ?
3. Peut-on mesurer une tâche pendant sa période d’essai sans risque ?
4. Quelle forme donner à la charte sous 50 salariés pour qu’elle s’applique ?
5. Si elle est prestataire : comment écrire l’usage des outils et le relevé de temps sans créer de lien de subordination ?
6. Durée de conservation conseillée pour le journal et la fiche ?

**Expert-comptable ou gestionnaire de paie de GianLuca Carlone.**
7. Quelle convention collective et quel opérateur de compétences pour chaque société ? Quel effectif ?
8. Quelles formations à l’IA peuvent être financées, et à quelles conditions ?

**Délégué à la protection des données, si l’une des sociétés en a un.**
9. Faut-il une analyse d’impact pour le journal des actions ?
