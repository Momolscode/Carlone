# Le calcul à la demande et la combinaison locale et distante

Note de travail interne — sources publiques consultées le 10 novembre 2026 — ce n'est pas un avis juridique, fiscal ou d'investissement.

Auteur : note de recherche pour le dixième livrable (BRIEF-2, § 9.2). Elle n'est pas le livrable. Elle ne doit pas être montrée telle quelle à GianLuca Carlone. La partie « Vérification du 10 novembre 2026 », à la fin, l’emporte sur le reste de la note.

Conventions : « HT » = hors taxes. Les prix en dollars restent en dollars, sauf mention d'un taux daté. Étiquettes : [Officiel], [Prix public daté], [Mesure publiée], [Source professionnelle], [Estimation], [À confirmer]. La note k13a (prix d'achat d'une machine locale) n'existait pas dans le dépôt au moment de la rédaction : les prix de machines cités ici sont donc à recouper avec elle.

## En bref

- Louer une carte graphique en France coûte entre **0,75 € et 5,20 € HT de l'heure** selon le modèle (L4 à H200), sans engagement, chez OVHcloud, Scaleway ou Outscale. Une machine allumée tout le mois coûte entre **540 € et 2 000 € HT** environ pour une seule carte.
- Pour nos usages (lire des documents, résumer, classer, rédiger), **le paiement à l'usage d'un modèle hébergé en Europe est presque toujours le moins cher** : de 0,04 € à 7,50 € HT par million de jetons. Un million de jetons, c'est de l'ordre de plusieurs centaines de pages (estimation).
- Une machine locale ne devient moins chère que la location qu'au-delà d'un usage soutenu (plusieurs centaines d'heures par mois, voir partie 4). Elle ne devient presque jamais moins chère que le paiement à l'usage pour de petits volumes. **Son vrai avantage n'est pas le prix : c'est que les données restent sur place.**
- La combinaison raisonnable en 2026 : données sensibles traitées en local ou chez un hébergeur européen ; tâches difficiles envoyées à un modèle de pointe, avec des données réduites ou pseudonymisées. L'ANSSI et la CNIL recommandent de cartographier les données, de choisir l'hébergement selon leur sensibilité et de garder une validation humaine.
- SecNumCloud est une qualification de l'ANSSI. Elle n'est pas nécessaire pour une PME privée comme celles de GianLuca Carlone. Elle sert d'abord au secteur public et aux données très sensibles. Outscale l'affiche pour une région dédiée, plus chère d'environ 20 %.
- Un gain « × N » honnête se mesure en **traitements simultanés** : par exemple 400 requêtes par minute chez OVHcloud AI Endpoints, ou plusieurs lots en parallèle. Il ne vaut que pour des tâches répétitives, et la relecture humaine reste le goulet.

## 1. Location de cartes graphiques à l'heure en France et en Europe

### 1.1 OVHcloud (France)

- La page « Tarifs Public Cloud » affiche les instances GPU en **prix HT par heure et par mois**, sans engagement. Le centre de Gravelines (France) a le plus grand choix ; la région de Paris propose aussi des H200 (OVHcloud, « Tarifs Public Cloud », https://www.ovhcloud.com/fr/public-cloud/prices/, page sans date, consultée le 10 novembre 2026) [Prix public daté].
- Prix relevés, une carte : **L4 (24 Go) 0,75 € HT/h**, environ 540 € HT/mois ; **L40S (48 Go) 1,40 € HT/h**, 1 008 € HT/mois ; **A100 (80 Go) 2,75 € HT/h** ; **H100 (80 Go) 2,80 € HT/h**, 1 940 € HT/mois (même page) [Prix public daté].
- Prix relevés, plusieurs cartes : 2 × H100 à 5,60 € HT/h ; 4 × H100 à 11,20 € HT/h ; **8 × H200 (141 Go chacune) à 42 € HT/h**, environ 30 660 € HT/mois. Pas de H200 à l'unité sur la page lue (même page) [Prix public daté].
- Le prix mensuel est calculé sur 730 heures pour la 3e génération d'instances. Des « Savings Plans » sur 12 ou 36 mois réduisent les prix « jusqu'à 30 % » sur certaines instances (même page) [Officiel]. Leur application aux instances GPU : [À confirmer].
- Facturation à l'heure ou à la minute pour les GPU : la page affiche un prix horaire ; la règle exacte de décompte (heure entamée ou minute) n'a pas été lue [À confirmer].
- Les instances n'incluent pas d'adresse IPv4 publique par défaut ; elle est en option et son prix se voit dans l'espace client (même page) [Officiel].

### 1.2 Scaleway (France)

- La page « Tarifs Instances GPU » affiche **« Prix avant taxes »**, en euros par heure (Scaleway, « GPU Instances Tarifs », https://www.scaleway.com/fr/tarifs/gpu/, page sans date, consultée le 10 novembre 2026) [Prix public daté].
- **L4-1-24G : 0,79 € HT/h**, environ 574,87 € HT/mois ; 2 cartes 1,58 € ; 4 cartes 3,15 € ; 8 cartes 6,30 € HT/h (même page) [Prix public daté].
- Les instances L40S, H100 (PCIe et SXM) et B300-SXM (8 cartes, 288 Go chacune) figurent sur la page, mais **leur prix ne s'affichait pas** dans la zone lue (« Indisponible dans cette zone. Disponible à : PAR-2 ») (même page) [À confirmer].
- La page « Managed Inference » donne un repère indirect : un modèle servi sur une carte dédiée coûte **0,93 € HT/h sur L4, 1,72 € sur L40S, 3,40 € sur H100**, et 30,06 € HT/h sur 8 × H100 SXM (Scaleway, « Tarifs Model-as-a-service », https://www.scaleway.com/fr/tarifs/model-as-a-service/, consultée le 10 novembre 2026) [Prix public daté]. Ces prix incluent le service géré ; ils ne sont pas le prix nu de la carte.

### 1.3 3DS Outscale (France, groupe Dassault Systèmes)

- La page « Tarifs publics » est en **HT**, « sans engagement », avec **« facturation à la seconde »** (3DS Outscale, « Tarifs Publics », https://fr.outscale.com/tarifs/, consultée le 10 novembre 2026) [Prix public daté].
- Prix horaires **de la carte seule**, région Europe (eu-west-2) : L40 2,00 € ; A100 80 Go 3,60 € ; **H100 4,00 €** ; **H200 5,20 € HT/h** (même page) [Prix public daté].
- Les mêmes cartes dans la région « Cloud secteur public » (cloudgouv-eu-west-1) : L40 2,40 € ; H100 4,80 € ; H200 6,24 € HT/h, soit **20 % de plus** (même page) [Prix public daté].
- Attention : chez Outscale, le prix de la carte s'ajoute à celui de la machine virtuelle (processeurs, mémoire, stockage). Le prix total d'une machine avec carte n'est donc pas lisible directement (même page ; un comparateur tiers parle de « GPU only ») [À confirmer].
- Outscale vend aussi des **modèles Mistral sur cartes dédiées, au mois**, dans la région secteur public : Ministral 8B sur 1 L40 à 6 570 € HT/mois ; Mistral Small 3.2 sur 1 H100 à 9 800 € ; Mistral Medium 3 sur 8 H200 à 40 703 € HT/mois (même page) [Prix public daté]. Ce sont des offres pour de grandes organisations.
- Le support d'Outscale précise qu'un GPU flexible est facturé dès qu'il est réservé (« allocated »), même s'il n'est pas utilisé (3DS Outscale, « Quelle est la tarification des flexible GPU ? », https://support.outscale.com/hc/fr-fr/articles/4424942694939, article du 16 février 2022) [Officiel]. Un oubli d'extinction coûte donc de l'argent.

### 1.4 SecNumCloud : ce que c'est, qui l'a, ce que cela change pour nous

- SecNumCloud est une **qualification délivrée par l'ANSSI** à une offre précise d'un hébergeur, pas à toute l'entreprise. Le périmètre est « limité au service nommé dans la décision » (catalogue ANSSI repris par un annuaire tiers, https://nis2-pro.fr/prestataires/secnumcloud, consulté le 10 novembre 2026) [Source professionnelle].
- La page officielle de l'ANSSI liste les prestataires **en cours** de qualification. **Scaleway** y figure pour « Scaleway SecNumCloud (IaaS, PaaS) » : la qualification n'est donc pas encore obtenue (ANSSI, « Prestataires de services d'informatique en nuage — en cours de qualification », https://cyber.gouv.fr/offre-de-service/solutions-certifiees-et-qualifiees/services-de-securite-evalue/solutions-en-cours-de-qualification/prestataires-secnumcloud/, consultée le 10 novembre 2026) [Officiel].
- **OVHcloud** a trois offres qualifiées : Hosted Private Cloud (VMware), jusqu'au 29 décembre 2026 ; Bare Metal Pod, jusqu'au 24 mars 2028 ; **SNC Cloud Platform**, décision du 31 juillet 2026, jusqu'au 31 juillet 2029 (articles reprenant le catalogue ANSSI : https://ctn-solutions.com/ressources/cloud-souverain-secnumcloud-offres-kubernetes, 7 octobre 2026 ; https://keypop.io/ressources/secnumcloud, 2 novembre 2026) [Source professionnelle]. **Les instances GPU du Public Cloud lues en 1.1 ne font pas partie de ces offres** (déduction : elles ne sont pas nommées dans les décisions citées) [À confirmer].
- **Outscale** : l'offre « IaaS Cloud on Demand » est qualifiée jusqu'au **30 novembre 2026**, soit dans vingt jours. Son renouvellement n'apparaissait pas au catalogue du 16 octobre 2026 (mêmes sources) [À confirmer]. Le catalogue officiel est un PDF de l'ANSSI mis à jour le 27 octobre 2026 (https://messervices.cyber.gouv.fr/visas/catalogue-produits-services-profils-de-protection-sites-certifies-qualifies-agrees-anssi.pdf) ; nous ne l'avons pas lu en entier [À confirmer].
- Changement en 2026 : nouvelles qualifications d'OVHcloud (SNC Cloud Platform) et de NumSpot le 31 juillet 2026 ; deux échéances proches (Outscale le 30 novembre, OVHcloud VMware le 29 décembre 2026) (mêmes sources) [Source professionnelle].
- **Ce que cela signifie pour GianLuca Carlone** : SecNumCloud vise d'abord le secteur public et les données très sensibles ; il ajoute des exigences de sécurité et de protection contre les lois hors d'Europe. Ses sociétés (galerie, immobilier, commerces) n'y sont pas tenues, à notre connaissance [À confirmer auprès d'un avocat si un client public ou des données de santé entrent en jeu]. Le prix est plus élevé : + 20 % chez Outscale pour la région secteur public (voir 1.3) [Prix public daté]. Un hébergement européen, certifié ISO 27001, avec un contrat clair sur le lieu des données, suffit en général à une PME (raisonnement, pas une règle) [Estimation].

## 2. Repères hors d'Europe (pour situer les prix)

- **Lambda (États-Unis)** : prix par carte et par heure, **« plus applicable sales tax/VAT »**, donc hors taxes. Une H100 SXM seule : **4,29 $/h** ; H100 PCIe : 3,29 $/h ; B200 seule : 6,99 $/h ; A10 (24 Go) : 1,29 $/h ; en lot de 8 : H100 à 3,99 $/h par carte, B200 à 6,69 $/h (Lambda, « AI cloud pricing », https://lambda.ai/pricing, consultée le 10 novembre 2026) [Prix public daté].
- **Changement à signaler** : la page de Lambda annonce que **« de nouveaux prix prennent effet le 16 novembre 2026 »** ; les prix affichés sont donc ceux du 16 novembre, et les prix actuels ne se voient qu'en étant connecté (même page) [Officiel]. Le sens de l'évolution (hausse ou baisse) n'est pas lisible sur la page [À confirmer].
- **RunPod (États-Unis)** : page « mise à jour le 4 novembre 2026 ». Prix à l'heure par machine, facturation affichée à l'heure ou à la seconde. Exemples : **L4 0,59 $/h** ; L40S 1,09 $/h ; RTX 4090 0,89 $/h ; RTX 5090 1,19 $/h ; **H100 SXM 3,99 $/h** ; H200 5,29 $/h ; B200 7,99 $/h (RunPod, « GPU Cloud Pricing », https://www.runpod.io/pricing, 4 novembre 2026) [Prix public daté]. Le régime de taxes n'est pas écrit sur la partie lue [À confirmer]. Le niveau affiché (« Community Cloud », réseau de machines de tiers, ou « Secure Cloud », centres de données) n'est pas clair dans la lecture [À confirmer].
- **Lecture** : à carte égale, les prix français ne sont pas plus chers que les prix américains. Une H100 coûte 2,80 € HT/h chez OVHcloud, contre 3,99 à 4,29 $ chez Lambda ou RunPod. Le taux de change n'a pas été appliqué ici ; la comparaison reste un ordre de grandeur [Estimation].
- **Réserve sur les données** : envoyer des documents de GianLuca Carlone chez un hébergeur américain est un **transfert hors de l'Union européenne**. Il exige une base juridique (par exemple une adhésion de l'hébergeur au cadre de protection des données UE–États-Unis, ou des clauses contractuelles types) et une information des personnes concernées. Nous ne l'avons pas vérifié pour Lambda ni RunPod [À confirmer]. **Recommandation interne : ne pas utiliser ces hébergeurs pour ses données.** Ils restent un repère de prix.

## Vérification du 10 novembre 2026

Relecture sceptique, 10 novembre 2026 (vérification commune aux notes k13b, k13d et k13f). Pour cette note : aucune recherche par moteur ; la page « Tarifs Public Cloud » d’OVHcloud lue en entier ; la page de tarifs de Scaleway refuse les robots (erreur 403 et page de contrôle), ses prix ont donc été relus dans le catalogue public des prix de Scaleway (api.scaleway.com, « product-catalog », instances). Outscale, SecNumCloud, Lambda et RunPod n’ont pas été relus. La note s’arrête après la partie 2 : la « partie 4 » citée dans « En bref » n’existe pas ; l’essentiel est ajouté ci-dessous. Cette partie l’emporte sur le reste de la note.

**Conclusion.** Tous les prix d’OVHcloud cités sont justes et affichés hors taxes. Le prix de la carte L4 chez Scaleway (0,79 € de l’heure) est confirmé ; ceux de la L40S et de la H100, absents de la lecture d’origine, sont trouvés (environ 1,47 € et 2,87 € de l’heure). Deux précisions : OVHcloud facture la plupart de ses services à la seconde ; ses prix mensuels de cartes ne sont pas le prix horaire multiplié par 730 heures. Le « 400 requêtes par minute » de « En bref » n’a pas de source.

### Tableau des contrôles

| # | Affirmation | Verdict | Source et date |
|---|---|---|---|
| 1 | OVHcloud : prix en « HT / heure » et « HT / mois », sans engagement ; Gravelines a le plus grand choix ; Paris propose aussi des H200 | Confirmé | OVHcloud, « Tarifs Public Cloud », https://www.ovhcloud.com/fr/public-cloud/prices/, lue le 10 novembre 2026 |
| 2 | L4 (24 Go) 0,75 € HT/h, 540 € HT/mois ; L40S (48 Go) 1,40 €, 1 008 € ; A100 (80 Go) 2,75 € ; H100 (80 Go) 2,80 €, 1 940 € | Confirmé ; l’A100 affiche aussi 1 100 € HT/mois | Même page (l4-90, l40s-90, a100-180, h100-380) |
| 3 | 2 × H100 5,60 € ; 4 × H100 11,20 € ; 8 × H200 42 € HT/h, environ 30 660 € HT/mois ; pas de H200 à l’unité | Confirmé ; 4 × H100 : 7 770 € HT/mois | Même page (h100-760, h100-1520, h200-1920) |
| 4 | « Le prix mensuel est calculé sur 730 heures pour la 3e génération d’instances » | Confirmé pour les instances B3, C3 et R3 ; **ne vaut pas pour les cartes** : 540 € pour 0,75 €/h (720 h), 1 940 € pour 2,80 €/h (environ 693 h), 1 100 € pour 2,75 €/h (400 h) ; conditions du prix mensuel non lues | Même page |
| 5 | Décompte à l’heure ou à la minute : « à confirmer » | **Précisé** : « La majorité des services Public Cloud sont facturés à la seconde, avec une durée de facturation minimale d’une minute par ressource » ; le cas des cartes n’est pas détaillé | Même page |
| 6 | Pas d’adresse IPv4 publique par défaut ; option payante, prix visible dans l’espace client | Confirmé | Même page |
| 7 | Savings Plans « jusqu’à 30 % » ; application aux cartes | **Non revérifié** : la page renvoie à une page « Savings Plan » non lue | Même page |
| 8 | Scaleway : L4-1-24G 0,79 € HT/h ; 2, 4 et 8 cartes à 1,58 €, 3,15 € et 6,30 € | Confirmé : 0,0131 €, 0,0262 €, 0,0525 € et 0,105 € par minute, soit 0,79 €, 1,57 €, 3,15 € et 6,30 € de l’heure ; régions Paris 1, Paris 2 et Varsovie | Scaleway, catalogue public des prix (api.scaleway.com, product-catalog v2alpha1, instances), lu le 10 novembre 2026 |
| 9 | Scaleway : prix des L40S, H100 et B300 « non affichés » | **Complété** : L40S-1-48G 0,0245 €/min (1,47 €/h) ; H100-1-80G 0,0478 €/min (2,87 €/h) ; H100-SXM-2-80G 0,1103 €/min (6,62 €/h) ; H100-SXM-8-80G 0,4222 €/min (25,33 €/h) ; B300-SXM-8-288G 1 €/min (60 €/h) ; Paris 2 (et Varsovie pour la L40S et la H100) | Même catalogue |
| 10 | Scaleway : « Prix avant taxes » ; environ 574,87 € HT/mois pour la L4 | **Non relu** (page fermée aux robots) ; le catalogue ne dit pas si ses prix sont hors taxes | — |
| 11 | Scaleway Managed Inference : 0,93 €, 1,72 €, 3,40 € et 30,06 € HT/h | **Non relu** | — |
| 12 | OVHcloud AI Endpoints : « 400 requêtes par minute » (« En bref ») | **Sans source** dans la note ; non relu | — |
| 13 | Outscale (prix, facturation à la seconde, +20 % en région secteur public), SecNumCloud (ANSSI, échéances), Lambda, RunPod | **Non relus** : interne seulement | — |

### Corrections à appliquer

1. « En bref », « entre 0,75 € et 5,20 € HT de l’heure selon le modèle (L4 à H200) … chez OVHcloud, Scaleway ou Outscale » → « pour une carte, de 0,75 € HT de l’heure (L4, OVHcloud) à 2,80 € (H100, OVHcloud) ou environ 2,87 € (H100, Scaleway) ; les 5,20 € de la H200 chez Outscale (carte seule, machine en plus) ne sont pas revérifiés ».
2. « En bref », « Une machine allumée tout le mois coûte entre 540 € et 2 000 € HT environ » → « Les prix mensuels affichés par OVHcloud vont de 540 € (L4) à 1 940 € HT (H100) pour une carte ; leurs conditions ne sont pas lues : dans un document client, citer le prix horaire ».
3. § 1.1, « la règle exacte de décompte … [À confirmer] » → « La majorité des services Public Cloud sont facturés à la seconde, avec un minimum d’une minute par ressource (même page) ; le cas des cartes n’est pas détaillé ».
4. § 1.1 : ajouter « A100 : 1 100 € HT/mois affiché ; 4 × H100 : 7 770 € HT/mois ».
5. § 1.1, « Le prix mensuel est calculé sur 730 heures pour la 3e génération d’instances » → ajouter « (B3, C3, R3) ; pas pour les cartes, dont le prix mensuel est donné à part ».
6. § 1.2, « leur prix ne s’affichait pas » → prix du catalogue public (ligne 9 du tableau).
7. § 1.2, « 2 cartes 1,58 € » → « 1,57 € » (0,0262 € par minute).
8. « En bref », « 400 requêtes par minute chez OVHcloud AI Endpoints » → retirer, ou « à confirmer » : aucune source.
9. « En bref », « voir partie 4 » : la partie 4 n’existe pas ; voir le complément ci-dessous.

### Complément essentiel : louer ou acheter, en ordre de grandeur

[Estimation ; interne]
- Une machine de bureau de 128 Go coûterait de 5 500 à 7 500 € HT chez des revendeurs français (k13a, prix non relus). À 1,40 € de l’heure (L40S, OVHcloud), 6 000 € paient environ 4 300 heures de location : environ six mois jour et nuit, ou environ deux ans à huit heures par jour ouvré. À 2,80 € (H100), environ 2 150 heures.
- Les machines ne se valent pas : une H100 louée calcule bien plus vite qu’une DGX Spark ; une DGX Spark a plus de mémoire (128 Go) qu’une L40S (48 Go). Le calcul donne un ordre de grandeur, pas un seuil.
- À l’achat s’ajoutent l’électricité (moins de 300 € TTC par an pour une DGX Spark jour et nuit, k13a), l’installation, la sécurité et l’entretien. À la location s’ajoutent le temps de pilotage, l’envoi des données chez l’hébergeur et le risque d’oublier d’éteindre.
- Pour les volumes envisagés (quelques centaines à quelques milliers de documents par mois), le paiement à l’usage d’un modèle reste le moins cher (k13c : environ 0,02 $ à 0,04 $ par devis de trois pages), et son coût baisse vite à qualité égale (Epoch AI, 22 septembre 2026 ; k13f, vérification). La location sert aux pointes et aux essais. L’achat se justifie par la confidentialité, pas par le prix.

### Sûr à reprendre

1. « Louer une carte de calcul en France, sans engagement, coûte de 0,75 € hors taxes de l’heure (carte L4) à 2,80 € (carte H100) chez OVHcloud (page « Tarifs Public Cloud », lue le 10 novembre 2026). » — **Annexe.**
2. « Chez Scaleway, une carte L4 revient à environ 0,79 € de l’heure et une H100 à environ 2,87 €, facturées à la minute (catalogue public des prix, lu le 10 novembre 2026). » — **Annexe**, en gardant « hors taxes » d’après la page de tarifs lue par la note (« Prix avant taxes ») ; à relire sur la page avant toute remise.
3. **Interne seulement** : les prix mensuels (conditions non lues), Outscale, SecNumCloud, Lambda, RunPod, Managed Inference, AI Endpoints, le calcul « louer ou acheter ».

### Ce qui reste inconnu

- La mention « avant taxes » de la page Scaleway, non relue ce soir.
- Les conditions du prix mensuel des cartes chez OVHcloud ; l’application des Savings Plans aux cartes ; la facturation d’une instance arrêtée mais non supprimée.
- La disponibilité réelle des cartes au moment voulu ; le prix d’une adresse IPv4 publique.
- La vitesse et la qualité de chaque carte sur les documents réels de GianLuca Carlone ; les volumes réels à traiter.
- Toutes les affirmations sur Outscale, SecNumCloud, Lambda et RunPod.

