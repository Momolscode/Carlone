# R4-donnees-ia : prospection, RGPD, fuite GitHub, AI Act, transferts et sécurité des agents IA (droit applicable au 4 novembre 2026)

Mémo du chercheur « R4-donnees-ia », rédigé le 4 novembre 2026 pour l'audit Marwin Tech × GianLuca Carlone. Toutes les pages web citées ont été consultées le **4 nov. 2026**. Aucun contact extérieur, aucune démarche, aucune modification du dépôt `Momolscode/Carlone`. Ce mémo n'est pas une consultation juridique : il prépare les questions à soumettre à un avocat (données personnelles et numérique) ou à un délégué à la protection des données.

Codes : **[FV]** fait vérifié sur source primaire ; **[DR]** déclaration rapportée (pièce du dépôt ou source secondaire non recoupée) ; **[PR]** proposition ; **[HY]** hypothèse ; **[ES]** estimation ; **[MM]** mesure faite par ce chercheur ; **[IN]** inconnu. Le repère **[Changement 2025]** ou **[Changement 2026]** signale une règle modifiée en 2025 ou en 2026.

Abréviations : **RGPD** = règlement (UE) 2016/679 ; **RIA** = règlement (UE) 2024/1689 sur l'intelligence artificielle (« AI Act ») ; **Omnibus IA** = règlement (UE) 2026/1744 ; **C5:ligne** = `audit-work/ex-C5-crm.md` (extraction du lecteur C5, CRM) ; **C7:ligne** = `audit-work/ex-C7-jarvis.md` ; **note-4-nov:ligne** = `audit-work/note-point-4-novembre-et-activites.md`. Les autres chemins sont relatifs au dépôt `Momolscode/Carlone`.

---

## 0. Limites de ce mémo (à lire d'abord)

1. **Légifrance inaccessible.** Les pages Légifrance renvoyaient une erreur 403 ou un contenu tronqué. Le texte exact de l'article L223-1 du code de la consommation (version du 11 août 2026) et celui de l'article L34-5 du code des postes et des communications électroniques **n'ont pas été lus à la source** [IN]. Leur contenu est établi par les fiches officielles de la DGCCRF et de la CNIL, qui les citent.
2. **EUR-Lex bloqué en lecture directe.** Les textes européens (RIA, Omnibus IA, RGPD, décisions 2021/914, 2021/915 et 2023/1795) ont été lus dans leur version publiée au Journal officiel, téléchargée depuis l'Office des publications de l'Union (`publications.europa.eu`, même document que sur EUR-Lex). Les citations sont donc de première main [FV].
3. **economie.gouv.fr bloqué en lecture directe.** Les fiches DGCCRF ont été lues par un service de lecture tiers (Exa). Leur contenu concorde avec les extraits du moteur de recherche [FV, avec cette réserve].
4. **Dépôt FinanceScope/CRM-Carlone non revérifié.** L'API GitHub a refusé l'accès depuis cette session (accès non activé). Son caractère public au 4 nov. à 16 h 19 reste une déclaration de Morgan Olsen (`interne/contexte-projet-carlone.md:11`) [DR]. Son état ce soir est [IN].
5. **Liste officielle du Data Privacy Framework.** Elle a été interrogée le 4 nov. 2026 vers 18 h 35 UTC par l'interface publique qu'utilise le site officiel `dataprivacyframework.gov` (Département du Commerce des États-Unis) [MM].
6. **Pas de dates de mise à jour inventées.** Quand une page n'affiche pas de date, c'est indiqué.

---

## Synthèse

1. **Téléphone vers des entreprises.** Le consentement préalable, obligatoire depuis le 11 août 2026, ne protège que les **consommateurs** (loi n° 2025-594, décret n° 2026-662, fin de Bloctel) [FV] [Changement 2026]. Les appels B2B restent possibles sur la base de l'intérêt légitime **si l'objet de l'appel a un rapport avec la profession** de la personne. Il faut aussi l'informer et lui permettre de s'opposer simplement [FV]. Le risque se concentre sur les lignes personnelles, les entrepreneurs individuels et les artistes que contient le fichier [HY].
2. **E-mail vers des entreprises.** Il reste possible sans consentement aux mêmes conditions de lien avec la profession, avec l'identité de l'expéditeur et un moyen simple de se désinscrire [FV]. Depuis le 16 octobre 2026, la CNIL encadre la « reconstitution » d'adresses (prenom.nom@…) : elle est possible sous conditions, et non interdite par principe [FV] [Changement 2026].
3. **Fichier de 500 entreprises.** L'intérêt légitime est une base défendable pour une prospection B2B [FV, considérant 47 du RGPD et CNIL]. La légalité dépend toutefois des preuves : analyse documentée, minimisation, information au plus tard au premier contact avec la source des données, droit d'opposition, liste repoussoir, durée de conservation, registre des traitements [FV]. **Aucune de ces pièces n'existe aujourd'hui** (C5:65, C5:181) [FV].
4. **Article 28.** Tout sous-traitant (Marwin pour le compte de l'entité de GianLuca Carlone, Quali Contact, hébergeurs, fournisseurs de LLM) doit être lié par un **contrat écrit** qui comporte les huit clauses obligatoires de l'article 28, § 3 [FV]. Aucun contrat n'existe et Marwin Tech n'est pas immatriculée [FV]. Le fichier a été constitué avant tout contrat (C5:88) : Morgan et Mathys pourraient donc être regardés comme **responsables du traitement de fait** [HY].
5. **Dépôt GitHub public.** L'exposition publique de numéros, d'e-mails et de profils LinkedIn de prospects correspond très probablement à une **violation de données personnelles** au sens de l'article 4, point 12, du RGPD (divulgation non autorisée accidentelle) [HY fort]. Elle doit **toujours** être documentée. Elle doit être **notifiée à la CNIL dans les 72 heures** suivant sa connaissance, sauf si elle n'est « pas susceptible d'engendrer un risque » [FV]. Une pièce datée du 2 novembre la signale déjà comme « Urgent » (`interne/audit-marwin-tech-carlone.md:3,15`) [FV]. Le délai est donc vraisemblablement atteint ou dépassé [ES], ce qui impose une **décision immédiate avec un avocat**. La réforme « omnibus numérique » du RGPD (96 heures, seuil du risque élevé) **n'est pas en vigueur** [FV].
6. **AI Act : calendrier réel.** L'application générale a commencé le **2 août 2026**, avec l'article 50 sur la transparence [FV]. Le règlement (UE) 2026/1744 (« Omnibus IA », en vigueur le 27 juillet 2026) a **reporté le haut risque** au 2 décembre 2027 pour l'annexe III et au 2 août 2028 pour l'annexe I. Il a aussi **assoupli l'article 4** sur la maîtrise de l'IA, devenu une obligation de moyens, et donné jusqu'au 2 décembre 2026 aux systèmes déjà sur le marché pour le marquage de l'article 50, § 2 [FV] [Changement 2026].
7. **Marwin et l'AI Act.** Quand Marwin utilise ChatGPT ou Claude pour GianLuca Carlone, elle est **déployeur**. Elle doit alors favoriser la maîtrise de l'IA de ses intervenants (article 4) et signaler les hypertrucages ainsi que certains textes d'intérêt public (article 50, § 4) [FV]. Si elle livre sous son nom un assistant conversationnel, un agent vocal ou le « copilote Jarvis », elle devient **fournisseur**. Elle doit alors informer les personnes qu'elles parlent à une IA (article 50, § 1) et, selon le cas, marquer les contenus générés (article 50, § 2) [FV texte] [HY qualification].
8. **Transferts vers les États-Unis.** Le Data Privacy Framework est valide [FV] et un pourvoi est pendant devant la Cour de justice (C-703/25 P) [FV]. **Anthropic et OpenAI ne figurent pas sur la liste officielle** au 4 novembre 2026 [MM]. Les transferts vers ces deux fournisseurs reposent donc sur les clauses contractuelles types, qui exigent une analyse d'impact des transferts (AITD) [FV]. Les offres grand public (ChatGPT Plus ou Pro, Claude Free, Pro ou Max) ne conviennent pas aux données personnelles du client [FV, politiques des éditeurs et CNIL].
9. **Sécurité des agents IA.** L'ANSSI a publié le 30 octobre 2026 « Sécuriser un système IA agentique » (sept principes) [FV] [Changement 2026]. L'OWASP a publié son Top 10 LLM 2026 le 3 août 2026 et son Top 10 des applications agentiques en décembre 2025 [FV]. Ils convergent : entrées non fiables, droits minimaux, approbation humaine des actions critiques, contrôles déterministes hors du modèle, secrets hors du contexte, journaux inaltérables, arrêt d'urgence [FV].
10. **Priorités [PR].** (1) Traiter la fuite GitHub aujourd'hui, avec l'avocat. (2) Désigner le responsable du traitement et signer les contrats de l'article 28. (3) Rédiger le registre, l'analyse d'intérêt légitime et la mention d'information. (4) Segmenter le fichier entre contacts B2B et contacts proches du B2C. (5) Passer les usages IA sur données client en offres professionnelles (API, Team ou Enterprise) avec AITD. (6) Appliquer la grille ANSSI avant toute automatisation agentique.

---

## (a) Prospection commerciale B2B par téléphone et par e-mail

### Réponse courte
- **Téléphone vers un consommateur** : interdit sans **consentement préalable** depuis le **11 août 2026**, sauf contrat en cours (si l'appel a un rapport avec ce contrat) et vente de journaux. Le consentement vaut un an au plus, sa preuve se conserve au moins trois ans, et Bloctel a disparu [FV] [Changement 2026, loi n° 2025-594 du 30 juin 2025 et décret n° 2026-662 du 23 juillet 2026].
- **Téléphone vers un professionnel** : **non visé** par cet opt-in. La DGCCRF répond « Non » à la question des appels « à destination des professionnels » [FV]. La CNIL admet l'**intérêt légitime** « lorsque l'objet de la sollicitation est en rapport avec la profession de la personne démarchée », avec **information** et **opposition simple et gratuite** [FV].
- **E-mail vers un professionnel** : même régime (intérêt légitime, lien avec la profession, identité de l'expéditeur, désinscription simple) [FV]. Les adresses génériques (contact@…) ne sont pas soumises à ces règles [FV]. La reconstitution d'adresses nominatives est encadrée depuis le 16 octobre 2026 [FV] [Changement 2026].
- **Zone grise** : un entrepreneur individuel, un artiste ou un dirigeant joint sur sa ligne personnelle pour un achat **personnel** relève du régime du consommateur [HY fondé sur la définition légale du consommateur].

### Détail

**1. Le nouveau régime du démarchage des consommateurs [FV] [Changement 2026].**
- Fiche DGCCRF du 27 juillet 2026 : « Il est interdit de démarcher par téléphone un consommateur sans avoir au préalable recueilli son consentement. » Le consentement doit être « libre, spécifique, clair, univoque et révocable » et « n'est valable qu'un an au maximum ». La preuve se conserve « durant une période minimale de 3 ans ».
- Seules deux exceptions subsistent : le contrat en cours, si la sollicitation a un rapport avec son objet, et la fourniture de journaux, périodiques ou magazines.
- Les appels autorisés sont limités au lundi-vendredi, de 10 h à 13 h et de 14 h à 20 h, et à quatre par période de trente jours. Le démarchage téléphonique est totalement interdit en rénovation énergétique, en adaptation du logement et pour le CPF.
- Sanctions : jusqu'à 75 000 € par appel pour une personne physique et 375 000 € pour une personne morale, avec publication systématique des amendes [FV, fiche DGCCRF].
- Bloctel : « Le service Bloctel a pris fin avec l'entrée en vigueur au 11 août 2026 » [FV, pro.bloctel.gouv.fr].
- Le numéro de la loi (n° 2025-594) et celui du décret (n° 2026-662) figurent dans la FAQ DGCCRF du 17 septembre 2026 [FV]. Selon une source secondaire, c'est l'article 13 de la loi qui réécrit l'article L223-1 [DR].

**2. Le périmètre B2C ou B2B.**
- La fiche DGCCRF définit le démarchage comme « la situation dans laquelle un professionnel contacte un consommateur » [FV].
- La FAQ DGCCRF du 17 septembre 2026 répond : « L'encadrement s'applique-t-il à des appels à destination des professionnels ? Non, ce sont uniquement les sollicitations des consommateurs par des professionnels […] qui sont encadrées par le décret » [FV]. La phrase suivante de la FAQ est mal rédigée (« les appels téléphoniques des consommateurs à destination des professionnels »). Elle ne change pas le sens, mais elle porte sur le décret « jours et horaires » et non sur l'article L223-1 lui-même [FV texte] [IN portée exacte].
- Le code de la consommation définit le consommateur comme « toute personne physique qui agit à des fins qui n'entrent pas dans le cadre de son activité commerciale, industrielle, artisanale, libérale ou agricole » (article liminaire, extrait lu sur une page Légifrance tronquée) [FV].
- **Conséquence** : le critère est la **finalité de l'appel**, pas le type de ligne. Un dirigeant appelé au sujet d'un achat d'œuvre pour sa société agit à titre professionnel [HY]. Le même dirigeant appelé pour une œuvre destinée à son domicile serait un consommateur [HY].

**3. Ce qu'exige la CNIL en B2B (téléphone, hors automate d'appel) [FV].**
- La base légale est l'intérêt légitime « lorsque l'objet de la sollicitation est en rapport avec la profession de la personne démarchée (par exemple, un appel présentant les mérites d'un logiciel au directeur informatique d'une entreprise) ».
- Deux règles sont à respecter : l'« information (par exemple, lors de la collecte de leur numéro de téléphone) » et l'« opposition simple et gratuite ».
- Pour des données achetées ou obtenues auprès de tiers, la CNIL précise qu'« il faut s'assurer que la personne concernée a été informée » et qu'elle « est en mesure de s'opposer ».
- La CNIL recommande une case décochée par défaut pour l'opposition en B2B.

**4. E-mail B2B [FV] [Changement 2026 pour la reconstitution].**
- Même base (intérêt légitime et lien avec la profession). Chaque message doit permettre « de prendre connaissance de l'identité de l'organisation » et d'exprimer « par un moyen simple, son refus » (page CNIL du 10 juin 2026).
- « Les adresses génériques de type info@nomsociete.fr, contact@nomsociete.fr […] ne sont pas soumises aux principes rappelés ci-dessus. »
- **Reconstitution d'adresses** (fiche CNIL du 16 octobre 2026) : elle est possible sur l'intérêt légitime « si certaines conditions sont remplies ».
  - La CNIL examine la finalité, la visibilité en ligne de la personne et les mesures qu'elle a prises pour protéger ses coordonnées. Une personne « ne disposant d'aucune présence identifiable en ligne » ne peut pas, a priori, s'attendre à la reconstitution de son adresse.
  - Garanties citées : ne conserver l'adresse qu'en cas de « premier contact effectif » dans un délai raisonnable, et exclure immédiatement toute personne qui s'y oppose.
  - **Ceci tranche le point laissé « non confirmé » dans `crm/docs/hermes-vocalcom.md:322` et confirme la source secondaire qui y est citée.**
- La page CNIL de 2020 sur la réutilisation des données publiques reste plus stricte. Elle écarte la collecte lorsque les conditions générales du site « interdisent l'aspiration » et exige le consentement pour la prospection électronique fondée sur des données moissonnées, sans distinguer B2B et B2C [FV, page du 30 avril 2020]. Elle doit être lue avec les pages de 2026, plus récentes et propres au B2B [HY].

**5. Automates d'appel et agents vocaux IA.**
- La page CNIL sur les automates d'appel n'énonce pas de règle propre au B2B : le principe affiché reste le consentement [FV]. L'application de l'exception B2B aux automates est donc [IN].
- Un agent vocal IA qui compose et parle seul pourrait être qualifié d'« automate d'appel » [HY]. Il relève en outre de l'article 50, § 1, du RIA (information sur l'interaction avec une IA ; voir (d)).
- **Numéros affichés** : la fiche DGCCRF interdit seulement aux « plateformes utilisant des systèmes automatisés d'appel » d'appeler les « particuliers » depuis des 06 ou 07 (décision ARCEP n° 2022-1583) [FV, formulation de la fiche]. La décision ARCEP elle-même n'a pas été lue [IN] ; son application à des appels B2B manuels reste à vérifier.

**6. Sous-traitance des appels.** La FAQ DGCCRF précise que recourir à un sous-traitant, même à l'étranger, « ne change en aucun cas » les obligations du professionnel, qui doit s'assurer que le sous-traitant s'y conforme [FV, pour les appels vers des consommateurs]. Le RGPD produit le même effet en B2B (article 28, voir (b)).

**7. Opposition au répertoire Sirene.** L'article A123-96 du code de commerce permet à une **personne physique** immatriculée de demander que ses informations du répertoire « ne puissent être utilisées par des tiers […] à des fins de prospection, notamment commerciale ». L'Insee ajoute que ces informations « ne peuvent alors être rediffusées, ni utilisées à des fins de prospection » [FV, insee.fr].
- Le CRM prévoit pour 13 entreprises « opposées à la prospection sur Pappers » : « pas de mailing, contact direct uniquement » (`crm/PASSATION.md:51`) [FV].
- Si ce drapeau traduit une opposition Sirene (entreprise individuelle) ou une opposition au titre du RGPD, **aucun canal de prospection** ne devrait être utilisé, téléphone compris [HY]. La signification exacte du drapeau Pappers est [IN].

### Sources officielles
| Source | Organisme | Date affichée | Citation courte |
|---|---|---|---|
| https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/demarchage-telephonique-professionnels-mettez-vous-en-conformite-avec-la-reglementation (titre « Les règles du démarchage téléphonique s'imposant aux entreprises ») | DGCCRF | « Écrit le 27/07/2026 » | « un consommateur ne peut être démarché que s'il y a consenti préalablement » |
| https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/encadrement-des-jours-horaires-et-frequence-du-demarchage-telephonique-la-faq-pour-les-professionnels | DGCCRF | « Écrit le 17/09/2026 » | « Non, ce sont uniquement les sollicitations des consommateurs par des professionnels […] qui sont encadrées » |
| https://pro.bloctel.gouv.fr/faq | Bloctel (service public) | non affichée | « Le service Bloctel a pris fin […] au 11 août 2026 » |
| https://www.cnil.fr/fr/prospection-commerciale-par-telephone-hors-automate-dappel-quelles-sont-les-regles | CNIL | 10 juin 2026 (le contenu décrit le régime du 11 août 2026) | « La prospection à l'égard de professionnels peut être fondée sur l'intérêt légitime » |
| https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique-sms-mms-et-automate-dappel | CNIL | 10 juin 2026 | « Les adresses génériques […] ne sont pas soumises aux principes rappelés ci-dessus » |
| https://www.cnil.fr/fr/reconstitution-adresses-professionnelles-quel-cadre | CNIL | 16 octobre 2026 | « ne peut reposer sur l'intérêt légitime que si certaines conditions sont remplies » |
| https://www.cnil.fr/fr/la-reutilisation-des-donnees-publiquement-accessibles-en-ligne-des-fins-de-demarchage-commercial | CNIL | 30 avril 2020 | « dont les conditions générales d'utilisation (CGU) interdisent l'aspiration » |
| https://www.cnil.fr/fr/comment-utiliser-une-liste-repoussoir-pour-respecter-lopposition-la-prospection | CNIL | non relevée (lue par extrait de recherche) | informations d'opposition « conservées au minimum 3 ans » |
| https://www.insee.fr/fr/information/4127417 | Insee | non affichée | « ne peuvent alors être rediffusées, ni utilisées à des fins de prospection » |

### Incertitudes et points à faire valider
- Texte exact de l'article L223-1 en vigueur et date de version (Légifrance non lu) [IN] → **avocat**.
- Traitement d'un **entrepreneur individuel** ou d'un **artiste-auteur** joint pour un sujet lié à son activité : un artiste contacté pour vendre ou exposer ses œuvres agit-il en professionnel ? [HY : oui le plus souvent] → **avocat**.
- Régime des **automates d'appel et agents vocaux IA** en B2B [IN] → avocat ou CNIL.
- Application de la décision ARCEP n° 2022-1583 à Quali Contact et à un numéroteur prédictif [IN] → **Quali Contact** et avocat.
- Signification du drapeau d'opposition Pappers (Sirene, RGPD ou option propre à Pappers) [IN].
- Enregistrement des appels : la règle CNIL (information orale, droit de s'opposer) est citée dans `crm/docs/hermes-vocalcom.md` (partie 6.1, lignes 279-306). La page n'a pas été rouverte [DR].

### Conséquences pour Marwin Tech et GianLuca Carlone
- Les règles du CRM (`crm/docs/rapport/rapport-crm-hermes360.md:85-90`) vont dans le bon sens : coordonnées professionnelles, pas d'adresse devinée, quatre appels en 30 jours, pas d'enregistrement [FV]. Elles ne suffisent pas, pour quatre raisons :
  1. **Segmenter le fichier** [PR] : sociétés et fonctions de direction (B2B) d'un côté ; lignes 06/07, messageries grand public, entrepreneurs individuels et artistes de l'autre. C5:63-64 compte 24 standards en 06/07, 25 e-mails grand public dans `companies.json`, ainsi que 21 mobiles, 26 e-mails grand public et 38 fiches d'artistes dans `culture.json` [FV via C5]. Le second groupe est à traiter avec la prudence du régime du consommateur, ou à écarter sans consentement [PR].
  2. **Script d'information au premier appel** [PR] : qui appelle, pour quelle entité vendeuse, d'où viennent les coordonnées, droit de s'opposer sur-le-champ. L'appel est suivi d'un e-mail de mention d'information avec lien de désinscription.
  3. **Désigner l'entité qui démarche** : la structure qui vend les œuvres est encore « à compléter » (`crm/PASSATION.md:27`) [FV]. C'est elle, et non Marwin, qui sera le « professionnel » et en principe le responsable du traitement [HY].
  4. **Quali Contact** : contrat de sous-traitance, validation des scripts, liste d'exclusion transmise avant chaque campagne, retour des oppositions. Ces éléments sont aujourd'hui [IN] (C5:81, C5:184).
- **Ne déployer aucun agent vocal IA sortant** (piste suggérée par l'abonnement ElevenLabs de Morgan, note-4-nov:8 [DR]) sans validation juridique préalable [PR].

---

## (b) RGPD : article 28, registre, sécurité, base légale d'un fichier de 500 entreprises et de leurs dirigeants

### Réponse courte
- **Article 28 (sous-traitant)** : un contrat **écrit** (le format électronique est admis) doit définir l'objet, la durée, la nature, la finalité, les types de données, les catégories de personnes et les droits du responsable. Il doit comporter **huit clauses** : instructions documentées (y compris pour les transferts), confidentialité, sécurité (article 32), conditions de recours à un sous-traitant ultérieur, aide aux droits des personnes, aide aux articles 32 à 36, suppression ou restitution en fin de prestation, audits [FV]. La Commission propose des clauses types (décision d'exécution (UE) 2021/915) [FV].
- **Registre** : obligatoire pour la gestion des prospects, même dans une entreprise de moins de 250 salariés, car le traitement n'est pas occasionnel [FV, CNIL]. Un sous-traitant tient en outre un registre de ses activités pour le compte de ses clients [FV].
- **Sécurité** : mesures « adaptées au risque » (article 32) : chiffrement ou pseudonymisation, confidentialité, intégrité, disponibilité, restauration, tests réguliers [FV].
- **Base légale du fichier de 500 entreprises** : l'**intérêt légitime** (article 6, § 1, f, et considérant 47) est la base attendue d'une prospection B2B [FV]. Il faut le **démontrer et le documenter** : intérêt réel, nécessité et minimisation, mise en balance avec les attentes raisonnables des dirigeants. Il faut aussi informer les personnes (article 14), respecter leur droit d'opposition discrétionnaire (article 21, § 2 et 3) et limiter la conservation (trois ans selon la CNIL) [FV].

### Détail

**1. Qui est responsable du traitement, qui est sous-traitant ?**
- Article 28, § 10 : « si, en violation du présent règlement, un sous-traitant détermine les finalités et les moyens du traitement, il est considéré comme un responsable du traitement pour ce qui concerne ce traitement » [FV].
- État des faits [FV via C5] : le CRM a été produit du 22 au 30 octobre par des agents IA. Les 48 commits visibles sont signés « Claude » (C5:34). Il a été produit **avant tout contrat** (C5:88). Le dépôt d'origine est au compte FinanceScope, présenté comme celui de Mathys (C5:60). Aucun responsable du traitement n'est désigné (C5:65, C5:181).
- Lecture [HY] :
  - pour la **constitution** du fichier, Morgan et/ou Mathys (à titre personnel ou par une structure existante) sont responsables du traitement de fait ;
  - pour **l'exploitation commerciale** (vendre des œuvres de GianLuca Carlone), le responsable sera l'entité vendeuse de M. Carlone ; Marwin, une fois immatriculée, sera son sous-traitant ; Quali Contact sera sous-traitant de M. Carlone, ou sous-traitant ultérieur de Marwin ;
  - Anthropic ou OpenAI (selon l'offre), GitHub, Google (Firebase) et Notion sont des sous-traitants ultérieurs à déclarer.
- Marwin Tech n'étant pas immatriculée, elle ne peut aujourd'hui ni signer un contrat de sous-traitance ni en assumer les obligations [FV, note-4-nov:6 et `interne/audit-marwin-tech-carlone.md:13`].

**2. Contenu obligatoire du contrat (article 28, § 3) [FV].** Le contrat « définit l'objet et la durée du traitement, la nature et la finalité du traitement, le type de données à caractère personnel et les catégories de personnes concernées, et les obligations et les droits du responsable du traitement ». Il prévoit que le sous-traitant :
- a) ne traite que « sur instruction documentée du responsable du traitement, y compris en ce qui concerne les transferts » ;
- b) garantit la confidentialité des personnes autorisées ;
- c) prend les mesures de l'article 32 ;
- d) respecte les conditions de recrutement d'un autre sous-traitant, avec autorisation écrite préalable, spécifique ou générale, et droit d'objection (§ 2) ;
- e) aide à répondre aux demandes d'exercice des droits ;
- f) aide pour les articles 32 à 36 (sécurité, violations, analyse d'impact) ;
- g) supprime ou renvoie les données en fin de prestation, au choix du responsable ;
- h) fournit les informations nécessaires et permet les audits.

Le sous-traitant doit aussi alerter si une instruction lui paraît illicite. Les mêmes obligations s'imposent aux sous-traitants ultérieurs (§ 4), et le contrat est écrit, éventuellement électronique (§ 9). Les clauses types de la décision 2021/915 peuvent servir de base (§ 6 et 7) [FV].

**3. Registre (article 30) [FV].** L'exemption des structures de moins de 250 personnes ne joue pas si le traitement « n'est pas occasionnel » (article 30, § 5). La CNIL cite expressément « la gestion des clients/prospects » parmi les traitements non occasionnels à inscrire. Elle recommande deux registres à un prestataire qui est à la fois responsable et sous-traitant, et propose un modèle simplifié (ODS).

**4. Sécurité (article 32) [FV].** Le texte vise « la pseudonymisation et le chiffrement », la « confidentialité, l'intégrité, la disponibilité et la résilience constantes des systèmes », le rétablissement de l'accès « dans des délais appropriés » et « une procédure visant à tester, à analyser et à évaluer régulièrement l'efficacité des mesures ». État du CRM selon C5 :
- règles Firestore correctes en lecture (C5:54) ;
- mais tout associé peut effacer tout le suivi, sans historique (C5:55) ;
- code exécuté par `document.write` depuis un seul compte (C5:56) ;
- sauvegarde par export CSV manuel, sans restauration testée (C5:57) [FV via C5].

**5. Base légale du fichier.**
- Article 6, § 1, f : le traitement « nécessaire aux fins des intérêts légitimes poursuivis par le responsable du traitement ou par un tiers, à moins que ne prévalent les intérêts ou les libertés et droits fondamentaux de la personne concernée » [FV]. Considérant 47 : le traitement « à des fins de prospection peut être considéré comme étant réalisé pour répondre à un intérêt légitime » [FV].
- Conditions pratiques [HY, déduites du texte et des pages CNIL citées en (a)] :
  - **Intérêt réel** : vendre des œuvres à des entreprises.
  - **Lien avec la fonction** : la décision d'achat et sa fiscalité concernent bien le dirigeant ou le responsable financier, comme l'argumente déjà `crm/docs/hermes-vocalcom.md:308-318` [DR].
  - **Minimisation** : nom, fonction et coordonnées professionnelles. Les liens LinkedIn (87 profils, C5:62), les « actualités datées » et les lignes personnelles doivent être justifiés ou supprimés [PR].
  - **Attentes raisonnables** : réduites pour les personnes sans présence professionnelle en ligne (CNIL, 16 octobre 2026).
- **Moissonnage** : la CNIL écarte la collecte sur des sites dont les conditions d'utilisation interdisent l'aspiration (page de 2020) [FV]. Le mode d'obtention des profils LinkedIn par les agents est [IN].
- **Information (article 14)** [FV] : pour des données non collectées auprès de la personne, l'information comprend « la source d'où proviennent les données » et indique si elles sont issues de sources publiques. Elle est donnée « dans un délai raisonnable […] ne dépassant pas un mois » et, si les données servent à communiquer avec la personne, « au plus tard au moment de la première communication ». Le droit d'opposition doit être « explicitement porté à l'attention de la personne » au premier contact, « clairement et séparément de toute autre information » (article 21, § 4).
- **Opposition** : en prospection, la personne peut s'opposer « à tout moment », sans motif, et ses données « ne sont plus traitées à ces fins » (article 21, § 2 et 3) [FV]. La liste repoussoir se conserve au moins trois ans (CNIL) [FV].
- **Conservation** : selon le référentiel CNIL « gestion des activités commerciales », les données d'un prospect non client se conservent « trois ans à compter de leur collecte par le responsable de traitement ou du dernier contact émanant du prospect ». Ouvrir un e-mail ne compte pas comme un contact [FV]. Le CRM affiche « supprimé 3 ans après le dernier contact » (`crm/docs/rapport/rapport-crm-hermes360.md:90`). Or c'est le contact **émanant du prospect** qui compte, pas nos appels, et aucune purge n'est outillée (C5:172) [FV].
- **Analyse d'impact (AIPD)** : son caractère obligatoire n'a pas été établi pour ce fichier [IN]. Une analyse courte est conseillée en raison de l'enrichissement par agents IA et du croisement de sources [PR].

**6. Sanctions encourues (rappel, sans préjuger d'un cas) [FV].** L'article 83, § 4, prévoit jusqu'à 10 000 000 € ou 2 % du chiffre d'affaires mondial pour les obligations des articles 25 à 39 (dont 28, 30, 32 et 33). L'article 83, § 5, prévoit jusqu'à 20 000 000 € ou 4 % pour les principes, la base légale, les droits des personnes et les transferts.

**7. Réforme en discussion : « omnibus numérique » du RGPD [FV] [non en vigueur].** Le Conseil de l'UE a adopté sa position le 21 octobre 2026, et le Parlement européen n'a pas encore voté la sienne. Rien ne change donc au 4 novembre 2026. Selon des sources secondaires, le Parlement ne se prononcerait pas avant le début de 2027 [DR].

### Sources officielles
| Source | Organisme | Date affichée | Citation courte |
|---|---|---|---|
| RGPD, http://data.europa.eu/eli/reg/2016/679/oj (JO L 119 du 4.5.2016, lu via publications.europa.eu) | UE | 27 avril 2016 (version d'origine, non modifiée sur ces articles) | art. 28, § 3, a : « sur instruction documentée du responsable du traitement » ; considérant 47 |
| Décision d'exécution (UE) 2021/915, http://data.europa.eu/eli/dec_impl/2021/915/oj | Commission européenne | 4 juin 2021 | « clauses contractuelles types entre les responsables du traitement et les sous-traitants au titre de l'article 28, paragraphe 7 » |
| https://www.cnil.fr/fr/RGPD-le-registre-des-activites-de-traitement | CNIL | non affichée | « les traitements non occasionnels (exemple : […] gestion des clients/prospects […]) » |
| https://www.cnil.fr/sites/default/files/atoms/files/referentiel_traitements-donnees-caractere-personnel_gestion-activites-commerciales.pdf | CNIL | non affichée sur l'extrait | « trois ans à compter de leur collecte […] ou du dernier contact émanant du prospect » |
| https://www.consilium.europa.eu/en/press/press-releases/2026/10/21/digital-rulebook-council-agrees-position-to-simplify-data-protection-privacy-and-cyber-reporting-rules/ | Conseil de l'UE | 21 octobre 2026, mis à jour le 22 octobre 2026 | « the Council presidency will start negotiations with the European Parliament once the latter adopts its own negotiating position » |

### Incertitudes et points à faire valider
- **Qualification des rôles** (responsable, coresponsables, sous-traitant) pour la phase passée (constitution du fichier sans contrat) et pour la phase à venir → **avocat**. La réponse détermine qui notifie la fuite (voir (c)).
- Analyse d'intérêt légitime : validation de l'argument du « lien avec la fonction » pour une offre d'achat d'œuvre adossée à l'article 238 bis AB du CGI [HY] → avocat.
- Mode d'obtention des profils LinkedIn et respect des conditions d'utilisation des sites sources [IN].
- AIPD obligatoire ou non [IN] → DPD ou avocat.
- Contrat de Quali Contact (existence, payeur, clauses de l'article 28) [IN] (C5:81, C5:184).

### Conséquences pour Marwin Tech et GianLuca Carlone
- Le **contrat Marwin–entité de GianLuca Carlone** doit comporter une annexe « sous-traitance de données » reprenant l'article 28, § 3, a à h [PR]. Elle doit aussi fixer la liste des sous-traitants ultérieurs (fournisseur LLM, GitHub, Google, Notion, Quali Contact si Marwin le pilote), les mesures de sécurité, la notification des violations « dans les meilleurs délais » (article 33, § 2), la restitution et la suppression en fin de mission, et un droit d'audit raisonnable [PR]. Le dossier `interne/contexte-projet-carlone.md:96` mentionne déjà une « clause de sous-traitance RGPD (article 28) dans le contrat » [PR].
- **Livrables de conformité à facturer ou à inclure** [PR] : registre (côté client et côté Marwin), analyse d'intérêt légitime, mention d'information, procédure d'opposition, purge à trois ans, procédure de violation. Le travail est modeste, mais c'est une condition pour exploiter le CRM.
- **Propriété et réversibilité** : le fichier appartient fonctionnellement au responsable du traitement. GianLuca Carlone doit pouvoir le récupérer et le faire purger [PR]. La phrase « le code, les données et le suivi restent chez les associés » (`crm/docs/rapport/rapport-crm-hermes360.md:19`) est incompatible avec un rôle de sous-traitant [HY].

---

## (c) Exposition publique d'un tel fichier sur GitHub : violation de données ? notification ?

### Réponse courte
- **Qualification** : la mise en ligne publique, par erreur, d'un fichier de prospects nominatif est une « divulgation non autorisée » ou un « accès non autorisé » « de manière accidentelle » au sens de l'article 4, point 12, du RGPD. Il s'agit donc très probablement d'une **violation de données personnelles**, même sans preuve que quelqu'un a téléchargé le fichier [HY fort, fondé sur la définition et la doctrine de la CNIL : « perte […] de confidentialité »].
- **Obligations** :
  1. **Documenter** toujours la violation (article 33, § 5) [FV].
  2. **Notifier la CNIL** « dans les meilleurs délais et, si possible, 72 heures au plus tard après en avoir pris connaissance », sauf si la violation n'est « pas susceptible d'engendrer un risque ». Au-delà de 72 heures, il faut motiver le retard (article 33, § 1) [FV].
  3. **Informer les personnes** si le risque est **élevé** (article 34) [FV].
  4. Le sous-traitant prévient le responsable du traitement « dans les meilleurs délais » (article 33, § 2) [FV].
- **En cas de doute, la CNIL demande de notifier** [FV].
- **Délai** : une pièce datée du 2 novembre 2026 signale déjà le dépôt public comme « Urgent » (`interne/audit-marwin-tech-carlone.md:3,15`) [FV]. Si la connaissance date du 2 novembre, le délai de 72 heures s'achève vers le 5 novembre [ES]. Notifier en retard en expliquant pourquoi vaut mieux que ne pas notifier [HY].

### Détail

**1. Les faits connus.**
- Le dépôt FinanceScope/CRM-Carlone était public le 4 novembre à 16 h 19 (dernier envoi le 30 octobre), et une analyse du 2 novembre y comptait « 931 numéros de téléphone, 206 adresses e-mail, 63 fichiers de profils LinkedIn et le rapport destiné à Carlone » (`interne/contexte-projet-carlone.md:11`) [DR].
- La copie versée dans `crm/` contient environ 940 numéros, 206 e-mails et 87 profils LinkedIn distincts (C5:62), ainsi que des mentions de 468 dirigeants (C5:63) [FV via C5].
- Le rapport destiné à GianLuca Carlone affirme pourtant que « Personne d'autre ne lit les fiches ni le suivi » (`crm/docs/rapport/rapport-crm-hermes360.md:15`), affirmation contredite par ce dépôt public (C5:153) [FV].
- État du dépôt ce soir, existence de duplications (forks) et journal d'accès : [IN].

**2. Qualification [FV pour les textes, HY pour l'application].**
- Article 4, point 12 : « une violation de la sécurité entraînant, de manière accidentelle ou illicite, la destruction, la perte, l'altération, la divulgation non autorisée de données à caractère personnel […] ou l'accès non autorisé à de telles données ».
- CNIL : deux conditions suffisent, un traitement de données personnelles et une « perte de disponibilité, d'intégrité ou de confidentialité […] de manière accidentelle ou illicite ».

**3. Qui doit agir ?** Le **responsable du traitement** notifie. Il n'est pas désigné (voir (b), point 1).
- Si Morgan et Mathys sont responsables de fait, ils notifient eux-mêmes [HY].
- S'ils sont sous-traitants de l'entité de GianLuca Carlone, ils doivent la prévenir sans délai. Le délai de 72 heures du responsable court alors à partir du moment où celui-ci est informé [HY].
- Dans les deux cas, attendre n'arrange rien [HY].

**4. Évaluer le risque [HY, à valider].**
- Données en cause : noms et fonctions de dirigeants, numéros (dont des mobiles), e-mails (dont des messageries personnelles), profils LinkedIn, informations d'entreprise, stratégie commerciale. Il n'y a ni données sensibles au sens de l'article 9, ni données bancaires connues.
- Conséquences plausibles : sollicitations non désirées, hameçonnage ciblé, usurpation d'une démarche « au nom de Carlone », atteinte à la réputation de GianLuca Carlone.
- Lecture : un **risque** paraît difficile à exclure, d'où une notification à la CNIL probable. Un **risque élevé** est moins évident, mais il doit être examiné pour les artistes et les lignes personnelles [HY].

**5. Remédiation technique [FV pour la documentation GitHub, PR pour la suite].**
- Rendre le dépôt privé, ou le supprimer après sauvegarde, puis contrôler les forks. La documentation GitHub prévient que des données retirées peuvent rester accessibles « In any clones or forks of your repository », « Directly via their SHA-1 hashes in cached views on GitHub » et que « You cannot remove sensitive data from other users' clones » [FV, documentation de l'éditeur].
- Révoquer ou renouveler d'abord tout secret (clé d'API, jeton, configuration) éventuellement présent [FV, même documentation] [IN : présence de secrets dans la branche publique].
- Réécrire l'historique (git-filter-repo) seulement après coordination [FV].
- Contrôler les autres copies : le dépôt privé `Momolscode/Carlone` (dossier `crm/`), les artefacts claude.ai et les archives zip (C5:25, C5:49). Ces copies ne sont pas des violations si elles restent privées, mais elles multiplient les surfaces [HY].

**6. Ce qui ne change pas encore [FV].** Le Conseil propose de ne notifier que les violations à **risque élevé**, sous 96 heures, mais le texte n'est **pas adopté**. La règle des 72 heures pour toute violation « susceptible d'engendrer un risque » reste en vigueur.

### Sources officielles
| Source | Organisme | Date affichée | Citation courte |
|---|---|---|---|
| RGPD, art. 4, point 12 ; art. 33 ; art. 34 (http://data.europa.eu/eli/reg/2016/679/oj) | UE | 27 avril 2016 | « 72 heures au plus tard après en avoir pris connaissance » |
| https://cnil.fr/fr/services-en-ligne/notifier-une-violation-de-donnees-personnelles | CNIL | non affichée | « En cas de doute, notifiez à la CNIL qui vous indiquera s'il est nécessaire d'informer les personnes. » |
| https://www.cnil.fr/fr/definition/violation-de-donnees | CNIL | non affichée | « tout incident de sécurité […] ayant comme conséquence de compromettre […] la confidentialité » |
| https://cnil-d10.cnil.fr/fr/securite-gerer-les-incidents-et-les-violations (fiche « Sécurité : gérer les incidents et les violations ») | CNIL | 14 mars 2024 | « Tenir un registre interne de toutes les violations de données personnelles. » |
| https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository | GitHub (éditeur, source non officielle au sens administratif) | non affichée | « You cannot remove sensitive data from other users' clones of your repository » |
| Communiqué du Conseil du 21 octobre 2026 (URL en (b)) | Conseil de l'UE | 21 et 22 octobre 2026 | « backs the Commission proposal to extend the deadline for the notification of personal data breaches » (proposition non adoptée) |

### Incertitudes et points à faire valider
- **Qui est le responsable du traitement** et donc qui notifie → **avocat, aujourd'hui**.
- Date de « prise de connaissance » : 2 novembre ou plus tôt [IN].
- Durée d'exposition, accès réels, forks, indexation par des moteurs de recherche [IN].
- Niveau de risque (simple ou élevé) et opportunité d'informer les personnes → avocat ou DPD, avec le téléservice de la CNIL.
- Présence de secrets techniques dans la branche publique [IN].

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Avant toute présentation commerciale** [PR] : (1) rendre le dépôt privé et le vérifier ; (2) ouvrir la fiche de violation (faits, données, nombre de personnes, mesures) ; (3) décider de la notification avec l'avocat ; (4) informer GianLuca Carlone par écrit, puisque ses prospects et son rapport sont en cause.
- **Ne pas présenter le CRM comme confidentiel** tant que ce point n'est pas réglé (contradiction C5:153) [PR].
- **Leçon de gouvernance** [PR] : aucune donnée personnelle de client dans un dépôt de code. Le code et les données doivent être séparés, avec des dépôts privés par défaut, une analyse automatique des secrets et des données, et une personne nommée responsable des accès.

---

## (d) AI Act (règlement (UE) 2024/1689) : calendrier réellement applicable en 2026 et obligations d'une petite société qui utilise des LLM pour un client

### Réponse courte
- **Le RIA s'applique depuis le 2 août 2026** pour l'essentiel, dont **l'article 50 (transparence)** [FV]. Les interdictions et l'article 4 s'appliquent depuis le 2 février 2025, et les modèles d'IA à usage général depuis le 2 août 2025 [FV].
- L'**Omnibus IA** (règlement (UE) 2026/1744 du 8 juillet 2026, JO du 24 juillet 2026, en vigueur le 27 juillet 2026) a apporté ces changements [FV] [Changement 2026] :
  - **haut risque reporté** au **2 décembre 2027** pour l'annexe III et au **2 août 2028** pour l'annexe I ;
  - **article 4 réécrit** : obligation de prendre des mesures pour **favoriser** la maîtrise de l'IA, sans garantir un niveau individuel ;
  - délai jusqu'au **2 décembre 2026** pour le marquage de l'article 50, § 2, des systèmes génératifs mis sur le marché avant le 2 août 2026 ;
  - **nouvelles interdictions** applicables au 2 décembre 2026.
- **Pour Marwin** : en tant que **déployeur** de ChatGPT ou de Claude, elle doit appliquer l'article 4 et l'article 50, § 4 (hypertrucages ; textes publiés pour informer le public sur des questions d'intérêt public, sauf contrôle éditorial humain) [FV]. En tant que **fournisseur** d'un assistant conversationnel, d'un agent vocal ou d'un copilote mis en service sous son nom, elle doit aussi appliquer l'article 50, § 1 (dire qu'il s'agit d'une IA) et l'article 50, § 2 (marquage lisible par machine des contenus de synthèse), sauf exceptions [FV texte] [HY qualification].
- **Sanctions** : jusqu'à 15 M€ ou 3 % du chiffre d'affaires pour l'article 50, le montant **le plus faible** étant retenu pour une PME [FV]. L'article 99 ne prévoit pas d'amende propre à l'article 4 [FV].

### Détail

**1. Calendrier consolidé au 4 novembre 2026 [FV : article 113 du RIA et articles 39-40 de l'Omnibus IA].**

| Date | Ce qui s'applique |
|---|---|
| 1er août 2024 | Entrée en vigueur du RIA (« vingtième jour suivant » la publication au JO du 12 juillet 2024) |
| 2 février 2025 | Chapitres I et II : définitions, **article 4** (maîtrise de l'IA), **article 5** (pratiques interdites) |
| 2 août 2025 | Modèles d'IA à usage général (chapitre V), gouvernance, sanctions (chapitre XII) |
| 27 juillet 2026 | Entrée en vigueur de l'Omnibus IA (« troisième jour suivant » sa publication du 24 juillet 2026) ; **nouvel article 4** ; articles 102 à 110 applicables |
| **2 août 2026** | **Application générale**, dont **l'article 50** (aucun report de l'article 50 dans l'Omnibus, seul son § 7 est réécrit) |
| 2 décembre 2026 | Article 50, § 2, pour les systèmes génératifs mis sur le marché avant le 2 août 2026 (nouvel article 111, § 4) ; nouvelles interdictions de l'article 5, § 1, points b bis et b ter, et § 1 bis et 1 ter |
| **2 décembre 2027** | Chapitre III, sections 1 à 3 : **haut risque de l'annexe III** |
| 2 août 2028 | Haut risque de l'annexe I (produits réglementés) |
| 2 août 2030 | Systèmes à haut risque des autorités publiques |

**2. Les textes utiles à Marwin [FV].**
- **Définitions** : le « fournisseur » est la personne « qui développe ou fait développer un système d'IA […] et le met sur le marché ou met le système d'IA en service sous son propre nom ou sa propre marque, à titre onéreux ou gratuit ». Le « déployeur » est la personne « utilisant sous sa propre autorité un système d'IA sauf lorsque ce système est utilisé dans le cadre d'une activité personnelle à caractère non professionnel » (article 3, points 3 et 4).
- **Article 4 réécrit** : « Les fournisseurs et les déployeurs de systèmes d'IA prennent des mesures pour favoriser le développement de la maîtrise de l'IA par leur personnel et les autres personnes s'occupant du fonctionnement et de l'utilisation des systèmes d'IA pour leur compte […]. Cette obligation ne contraint pas les fournisseurs ou les déployeurs à garantir un niveau spécifique de maîtrise de l'IA par un individu. » [Changement 2026, l'ancienne rédaction imposait de « garantir » la maîtrise de l'IA (considérant 36 de l'Omnibus)].
- **Article 50, § 1** : les fournisseurs veillent à ce que les personnes « soient informées qu'elles interagissent avec un système d'IA », sauf évidence pour une personne raisonnablement attentive.
- **Article 50, § 2** : les fournisseurs de systèmes générant des contenus de synthèse veillent à ce que les sorties soient « marquées dans un format lisible par machine ». Ce n'est pas exigé pour une simple « fonction d'assistance pour la mise en forme standard » ou si le système ne modifie pas substantiellement les données d'entrée.
- **Article 50, § 4** : le déployeur d'un système qui produit un **hypertrucage** indique que le contenu a été généré ou manipulé. Pour une œuvre « manifestement artistique, créative, satirique, fictive », il suffit de signaler l'existence de ces contenus « d'une manière appropriée qui n'entrave pas l'affichage ou la jouissance de l'œuvre ». Pour des **textes publiés pour informer le public sur des questions d'intérêt public**, la mention est due, sauf « processus d'examen humain ou de contrôle éditorial » avec responsabilité éditoriale.
- **Article 50, § 5** : l'information est donnée « au plus tard au moment de la première interaction ou de la première exposition ».
- **Sanctions** (article 99) : § 4, g, « jusqu'à 15 000 000 EUR ou […] 3 % » pour l'article 50 ; § 6, pour les PME le montant « le plus faible » ; nouvel article 99, § 6 bis, même règle pour les petites entreprises à moyenne capitalisation. L'article 4 ne figure pas dans les § 3 à 5 [FV].
- **Lignes directrices et code** : la Commission a publié des lignes directrices sur l'article 50 et facilite un code de bonnes pratiques sur le marquage et l'étiquetage. Une icône européenne est prévue [FV, pages de la Commission ; date de publication des lignes directrices non affichée].

**3. Autorités françaises.** Le schéma publié le 9 septembre 2025 par la DGE et la DGCCRF confie aux autorités suivantes le contrôle de l'article 50 :
- DGCCRF et Arcom : interaction avec une IA, contenus de synthèse, hypertrucages ;
- CNIL : reconnaissance des émotions ;
- Arcom : textes d'intérêt public ;
- DGCCRF : point de contact unique.

Ce schéma est mis en œuvre « sous réserve qu'il soit accepté par le Parlement » [FV, page DGE]. Au début de novembre 2026, aucune loi de désignation n'était définitivement adoptée selon deux sources secondaires (aiactinsight.eu au 3 novembre 2026, proofcan.com) [DR]. Le règlement reste directement applicable [FV].

**4. Situations concrètes pour Marwin [HY sauf mention].**

| Usage | Rôle | Obligations RIA |
|---|---|---|
| Rédiger des comptes rendus, des notes ou des offres avec ChatGPT ou Claude, relus par Morgan ou Mathys | Déployeur | Article 4 ; pas d'étiquetage obligatoire si le texte ne vise pas à informer le public sur une question d'intérêt public, ou s'il est relu sous responsabilité éditoriale |
| Images ou vidéos réalistes de lieux ou de personnes existants (visuels de vernissage, simulations de galerie) | Déployeur | Article 50, § 4 : mention « généré par IA » ; mention allégée pour une œuvre manifestement artistique |
| Assistant conversationnel, « copilote Jarvis » ou agent vocal livré à GianLuca Carlone sous le nom de Marwin (`interne/offre-marwin-tech-remuneration-et-collaboration.md:51,60`) [PR] | Fournisseur (si mis en service sous son nom) | Article 50, § 1 ; article 50, § 2 si le système génère des contenus de synthèse [IN pour un simple habillage d'une API] |
| Outil de tri des candidats, d'évaluation du personnel ou de notation de crédit | Fournisseur ou déployeur | **Haut risque (annexe III)** à partir du **2 décembre 2027** : à ne pas lancer sans étude préalable |
| Priorisation des 500 prospects B2B | Déployeur | Ne figure pas, a priori, à l'annexe III [HY] ; le RGPD s'applique pleinement |

Les obligations propres aux modèles d'IA à usage général pèsent sur OpenAI et Anthropic, sauf si Marwin modifie substantiellement un modèle [HY].

### Sources officielles
| Source | Organisme | Date affichée | Citation courte |
|---|---|---|---|
| RIA, http://data.europa.eu/eli/reg/2024/1689/oj (JO L du 12.7.2024, lu via publications.europa.eu) | UE | 13 juin 2024 | art. 113 : « Il est applicable à partir du 2 août 2026. » |
| Omnibus IA, http://data.europa.eu/eli/reg/2026/1744/oj (JO L du 24.7.2026, lu via publications.europa.eu) | UE | 8 juillet 2026 | art. 113, c, i : « du 2 décembre 2027 en ce qui concerne les systèmes d'IA classés comme étant à haut risque en vertu de l'article 6, paragraphe 2, et de l'annexe III » |
| https://digital-strategy.ec.europa.eu/fr/policies/guidelines-ai-transparency-obligations | Commission européenne | non affichée | « L'article 50 de la législation sur l'IA s'applique à partir du 2 août 2026. » |
| https://commission.europa.eu/news-and-media/news/safer-and-more-transparent-ai-2026-08-02_fr | Commission européenne | 2 août 2026 | « Le 2 août 2026, de nouvelles règles sur la transparence des systèmes d'IA sont entrées en vigueur. » |
| https://www.entreprises.gouv.fr/priorites-et-actions/transition-numerique/soutenir-le-developpement-de-lia-au-service-de-0 | DGE (ministère de l'Économie) | 9 septembre 2025 (date indexée) | « La DGCCRF et l'Arcom seront quant à elles chargées du contrôle des systèmes d'IA destinés à interagir directement avec des personnes » |

### Incertitudes et points à faire valider
- **Qualification de fournisseur** pour un assistant bâti sur une API d'OpenAI ou d'Anthropic, et application de l'article 50, § 2, à un tel assistant [IN] → lignes directrices de la Commission, puis avocat.
- Loi française de désignation des autorités et régime des sanctions nationales [IN].
- Version finale du code de bonnes pratiques sur le marquage (finalisation annoncée pour juin 2026) : date et contenu non vérifiés [IN].
- Un agent vocal sortant cumulerait l'article 50, § 1, le RGPD et les règles sur les automates d'appel [HY] → avocat.

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Article 4** [PR] : une courte politique d'usage de l'IA (outils autorisés, données interdites dans les prompts, relecture obligatoire, traçabilité), une formation tracée de Morgan, de Mathys et des équipes de GianLuca Carlone qui utiliseront les outils, puis une revue annuelle. Ce n'est pas une obligation de résultat, mais c'est la preuve attendue.
- **Contrat** [PR] : une clause « usage de l'IA » qui précise les outils, les offres (professionnelles), les données transmises, l'absence d'entraînement, la relecture humaine et le rôle (déployeur ou fournisseur) pour chaque livrable.
- **Supports et contenus** [PR] : mention « image générée par IA » pour tout visuel réaliste de lieu ou de personne ; pour les œuvres, mention discrète conforme à l'exception artistique.
- **Exclure du périmètre initial** [PR] : tout outil RH ou de notation de personnes. Le report du haut risque à 2027 ne rend pas ces outils anodins.

---

## (e) Transferts de données hors UE avec des fournisseurs de LLM américains

### Réponse courte
- **Data Privacy Framework (DPF)** : la décision d'adéquation (UE) 2023/1795 du 10 juillet 2023 est **en vigueur** [FV]. Le Tribunal de l'UE a rejeté le recours en annulation le 3 septembre 2025 (T-553/23), et un **pourvoi est pendant** devant la Cour de justice (C-703/25 P, introduit le 31 octobre 2025) [FV]. Aucune décision n'est connue au 4 novembre 2026 [DR].
- **Le DPF ne couvre que les organisations inscrites sur la liste officielle.** Au 4 novembre 2026, **Anthropic et OpenAI n'y figurent sous aucun statut**. Google LLC, GitHub et Microsoft y sont actifs [MM].
- **Conséquence** : pour Anthropic et OpenAI, les transferts reposent sur les **clauses contractuelles types** (décision 2021/914) de leurs contrats de traitement. Il faut alors une **analyse d'impact des transferts (AITD)**, à réaliser par l'exportateur avec l'aide de l'importateur [FV].
- **Offres grand public** (Claude Free, Pro ou Max, Claude Code sur ces comptes ; ChatGPT Free, Plus ou Pro) : les conversations **peuvent servir à l'entraînement** si l'utilisateur ne s'y oppose pas. Elles sont conservées **cinq ans** chez Anthropic si l'option est activée. Les offres professionnelles (API, Team, Enterprise, Business) n'entraînent pas les modèles par défaut [FV, pages des éditeurs] [Changement 2025 chez Anthropic]. La CNIL réserve les services grand public aux usages **non confidentiels** [FV].

### Détail

**1. DPF : état du droit [FV].**
- Titre de la décision : décision d'exécution (UE) 2023/1795 « constatant […] le niveau de protection adéquat des données à caractère personnel assuré par le cadre de protection des données UE - États-Unis ».
- L'avis de pourvoi publié au JOUE (affaire C-703/25 P, M. Latombe) demande l'annulation de l'arrêt du Tribunal du 3 septembre 2025 et de la décision. Il soulève quatre moyens : indépendance de la Data Protection Review Court, absence d'autorisation préalable pour la collecte en masse, et autres.
- Selon des sources secondaires : Microsoft a été admis à intervenir le 4 juin 2026, aucune date d'audience ni de conclusions n'était annoncée à la fin d'octobre 2026, et le prochain réexamen périodique de la Commission est attendu trois ans après celui d'octobre 2024 [DR].
- Si le DPF tombait, aucune période de transition n'est garantie [HY, position rapportée de l'autorité norvégienne]. Des clauses contractuelles types de secours restent utiles même pour Google ou GitHub [PR].

**2. Vérification de la liste officielle [MM, 4 novembre 2026].**

| Organisation recherchée | Résultat sur la liste DPF |
|---|---|
| Anthropic, Anthropic PBC | **Aucune inscription** (tous statuts) |
| OpenAI, OpenAI OpCo, Open AI | **Aucune inscription** (tous statuts) |
| Google LLC (dont Firebase et Google Workspace) | Active : UE–États-Unis, données RH et non RH ; Suisse et Royaume-Uni |
| GitHub | Active : UE–États-Unis, données non RH |
| Microsoft Corporation | Active |
| ElevenLabs | Active |
| Notion Labs, Inc. ; Constant Contact Inc ; Wix.com Inc. | « Active - Re-certification under Review » |
| Base44 ; Mistral | Aucune inscription |

**Contradiction relevée** : une source secondaire allemande (skill-sprinters.de, 30 mai 2026) affirme qu'OpenAI et Anthropic sont « zertifiziert ». La liste officielle le dément au 4 novembre 2026 [MM]. Il ne faut pas citer le DPF pour ces deux fournisseurs dans un registre.

**3. Contrats des éditeurs [FV, documents des éditeurs, à relire avant signature].**
- **OpenAI**, Data Processing Addendum (mis à jour le 1er décembre 2025, en vigueur au 1er janvier 2026) : il complète l'« OpenAI Services Agreement », donc les offres professionnelles. Il est conclu avec « OpenAI Ireland Ltd. » si le client est établi dans l'EEE. OpenAI y « acts as a Data Processor », notifie les violations « without undue delay » et autorise des sous-traitants ultérieurs avec 30 jours pour objecter.
- **Anthropic**, Data Processing Addendum (en vigueur le 24 février 2025) : il est rattaché aux « Commercial Terms ». Anthropic y est sous-traitant (« Customer is the controller and Anthropic is Customer's processor ») et les transferts reposent sur les « Standard Contractual Clauses » de la décision 2021/914 (modules 2 et 3). L'entité contractante pour un client européen n'a pas été vérifiée [IN].
- **Offres grand public** :
  - Anthropic, 28 août 2025 : le choix de l'entraînement concerne « Claude Free, Pro, and Max plans, including when they use Claude Code », avec une conservation de cinq ans si l'option est activée et de 30 jours sinon ; ces règles « do not apply to services under our Commercial Terms » [FV].
  - OpenAI : pour Free, Plus et Pro, « we may use your content to train our models » sauf opposition ; « By default, we don't use inputs or outputs from ChatGPT Business, ChatGPT Enterprise, ChatGPT Edu, or our API » [FV].

**4. AITD [FV].** Selon la CNIL, l'AITD doit être faite « avant de transférer les données vers un pays hors de l'EEE lorsque ce transfert s'appuie sur un outil de l'article 46 », sauf décision d'adéquation ou dérogation de l'article 49. Quand un sous-traitant européen transfère hors UE, c'est lui qui réalise l'AITD et le responsable du traitement la vérifie [DR, source secondaire résumant le guide]. Le guide propose un modèle ODS.

**5. Ce que dit la CNIL de l'usage d'IA générative en entreprise [FV, questions-réponses du 18 juillet 2024].** « Pour des usages non confidentiels, l'utilisation d'un service grand public […] pourra être envisagée avec des garanties appropriées (à condition d'éviter la création de compte avec des adresses électroniques personnelles et […] en désactivant la possibilité pour le fournisseur du système de réutiliser les données d'usage). » Pour des données personnelles de clients ou une documentation sensible, la CNIL juge « plus opportun et plus sécurisé » un déploiement maîtrisé.

### Sources officielles
| Source | Organisme | Date affichée | Citation courte |
|---|---|---|---|
| Décision (UE) 2023/1795, http://data.europa.eu/eli/dec_impl/2023/1795/oj | Commission européenne | 10 juillet 2023 | « niveau de protection adéquat […] cadre de protection des données UE - États-Unis » |
| https://eur-lex.europa.eu/eli/C/2025/6610/oj/eng (avis de l'affaire C-703/25 P) | Cour de justice de l'UE, JOUE | pourvoi du 31 octobre 2025 | « set aside the judgment of the General Court […] of 3 September 2025 » |
| https://www.dataprivacyframework.gov/list/ (et son interface publique) | Département du Commerce des États-Unis | interrogée le 4 novembre 2026 | Anthropic : 0 ; OpenAI : 0 ; Google LLC : « Active » |
| Décision (UE) 2021/914, http://data.europa.eu/eli/dec_impl/2021/914/oj | Commission européenne | 4 juin 2021 | « clauses contractuelles types pour le transfert de données à caractère personnel vers des pays tiers » |
| https://cnil.fr/fr/analyse-dimpact-des-transferts-des-donnees-la-cnil-publie-la-version-finale-de-son-guide-aitd | CNIL | 9 juillet 2025 (version finale annoncée le 31 janvier 2025 selon des sources secondaires) | « Une AITD doit être réalisée par l'exportateur soumis au RGPD » |
| https://cnil.fr/fr/les-questions-reponses-de-la-cnil-sur-lutilisation-dun-systeme-dia-generative | CNIL | 18 juillet 2024 | « Pour des usages non confidentiels, l'utilisation d'un service grand public […] pourra être envisagée » |
| https://openai.com/policies/data-processing-addendum/ ; https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance | OpenAI (éditeur) | DPA « Updated: December 1, 2025 » ; page d'aide non datée | « OpenAI Ireland Ltd. » ; « we may use your content to train our models » |
| https://www.anthropic.com/legal/data-processing-addendum ; https://www.anthropic.com/news/updates-to-our-consumer-terms | Anthropic (éditeur) | DPA « Effective February 24, 2025 » ; annonce du 28 août 2025 | « Standard Contractual Clauses » ; « do not apply to services under our Commercial Terms » |

### Incertitudes et points à faire valider
- Offres réellement utilisées pour produire le CRM et les documents (Claude grand public ou professionnel, ChatGPT Pro, réglage d'entraînement activé ou non) [IN]. L'abonnement ChatGPT Pro de Morgan est mentionné dans note-4-nov:8 [DR].
- Entité contractante d'Anthropic pour l'Europe et éventuelle option de stockage dans l'UE [IN].
- Issue du pourvoi C-703/25 P [IN].
- Contenu de l'AITD pour Anthropic et OpenAI → DPD ou avocat.

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Règle de base** [PR] : aucune donnée personnelle de prospects, de salariés ou de clients de GianLuca Carlone dans une offre grand public. Il faut utiliser l'API, Team ou Enterprise avec un contrat de traitement accepté, l'entraînement désactivé et une AITD.
- **Registre** [PR] : indiquer pour chaque outil l'entité, le pays, la base de transfert (DPF pour Google et GitHub ; clauses types pour Anthropic et OpenAI) et la date de vérification de la liste DPF, à refaire chaque trimestre.
- **Minimisation** [PR] : pseudonymiser avant envoi au LLM (identifiant de fiche plutôt que nom et téléphone) quand la tâche le permet.
- **Plan de repli** [PR] : prévoir un fournisseur européen ou un modèle local pour les traitements les plus sensibles si le DPF ou les clauses types devenaient inutilisables. Le « local d'abord » de Jarvis est surtout déclaratif à ce jour (C7:162) [FV via C7].

---

## (f) Bonnes pratiques de sécurité pour des agents IA (ANSSI, CNIL, OWASP)

### Réponse courte
Les sources de référence convergent [FV] :
- traiter **toute entrée comme non fiable** (documents, e-mails, pages web, mémoires), car l'injection d'instructions ne peut pas être éliminée ;
- **limiter l'autonomie et les droits** au strict besoin ;
- **classer les actions** (autonome, approbation humaine, interdite) ;
- placer un **contrôle d'autorisation déterministe hors du modèle** ;
- garder les **secrets hors du contexte** et utiliser des jetons courts ;
- **cloisonner** les environnements et les mémoires ;
- **limiter les boucles et les coûts** ;
- **journaliser** de façon inaltérable la chaîne « demande → autorisation → action → résultat » ;
- prévoir un **arrêt d'urgence** et une **restauration testée**.

Publications récentes : ANSSI, « Sécuriser un système IA agentique », 30 octobre 2026 ; CERT-FR, 13 avril 2026 ; CNIL et CIANum, 20 juillet 2026 ; OWASP, Top 10 LLM 2026 du 3 août 2026 [Changement 2026].

### Détail

**1. ANSSI.**
- « Recommandations de sécurité pour un système d'IA générative » (29 avril 2024) [FV] : « Il est fortement recommandé de limiter voire de proscrire les actions automatiques sur le SI déclenchées depuis un système d'IA et à partir d'entrées non-maîtrisées (ex. : données issues d'Internet ou de mails, etc.) ». Le guide recommande des filtres sur les requêtes et sur les réponses (informations sensibles, coordonnées personnelles), une limite de taille des réponses et une maîtrise des greffons (« plugins »).
- « Sécuriser un système IA agentique » (collection Les Essentiels, v1.0, publié le 30 octobre 2026) [FV] [Changement 2026], en sept principes :
  1. **Analyser et traiter les risques** de bout en bout. Nommer un responsable humain par mesure et « bloquer la mise en service tant qu'un risque reste inacceptable ».
  2. **Limiter l'autonomie** : mission documentée et revue au moins chaque année, inventaire des accès justifié « au regard du strict besoin métier », élargissement progressif.
  3. **Classer les actions** en « exécution autonome, approbation humaine obligatoire et action interdite ». Garder le mécanisme d'approbation « hors de portée du système agentique » et montrer à l'approbateur « l'action exacte ».
  4. **Cloisonner** : identités, secrets et connecteurs distincts pour le développement, l'évaluation et la production ; mémoires séparées par client. « Considérer que toute donnée transmise à un modèle hébergé peut être accessible à son fournisseur. »
  5. **Autorisation déterministe** hors de l'agent, refus par défaut, contrôle des enchaînements d'actions, « aucune confiance ni aucun privilège implicites ».
  6. **Limiter l'impact** : entrées et sorties non fiables, limite des appels successifs entre agents. « Maintenir les secrets hors du contexte du modèle, des mémoires et des journaux. » Jetons courts, arrêt d'urgence, restauration testée, pas de double exécution après restauration.
  7. **Démontrer la maîtrise** : inventaire des composants et des prompts système, tests réguliers, supervision. Les journaux doivent rester « hors de portée des modifications de l'agent » et permettre de reconstituer « demande → autorisation → action → résultat ».
- CERT-FR (CERTFR-2026-ACT-016, 13 avril 2026) [FV] : les assistants autonomes de poste de travail « ne doivent pas être déployés » tant qu'ils ne sont pas stabilisés. Le CERT-FR exige des actions limitées « au strict nécessaire », une « validation humaine […] obligatoire dès qu'une commande système ou une action à effet de bord est envisagée » et une exécution en bac à sable. La formulation défensive des prompts « peut être contournée via des attaques par injection ».
- ANSSI et BSI, assistants de programmation (4 octobre 2024) : recommandations pour un usage sûr des outils de génération de code [FV, page de l'ANSSI].

**2. CNIL.**
- Note conjointe avec le CIANum « IA agentique et données personnelles » (20 juillet 2026) [FV] : filtrage des requêtes, surveillance en temps réel des actions des agents, tests de robustesse, **mémoires cloisonnées** et limitées dans le temps, bac à sable.
- Recommandations sur le développement des systèmes d'IA (page du 22 juillet 2025) [FV] : analyse de risque, AIPD conseillée, contrôle des accès, chiffrement, possibilité de stopper le système, filtres sur les sorties.
- Fiche France Num et CNIL pour les TPE et PME (mars 2025) [FV] : « N'introduisez pas de données confidentielles, personnelles ou stratégiques » dans les outils grand public, et une charte d'usage est recommandée.

**3. OWASP (fondation OWASP, projet GenAI Security).**
- **Top 10 for LLM Applications 2026** (publié le 3 août 2026) [FV, page OWASP] [Changement 2026] : LLM01 injection d'instructions, toujours première ; LLM02 divulgation d'informations sensibles ; **LLM03 pouvoir d'agir excessif** (« Excessive Agency », sixième en 2025) ; LLM06 consommation non bornée, qui progresse de quatre rangs. Le document constate que modèles et données partagent le même canal, sans équivalent des requêtes paramétrées : la défense est « architectural rather than interceptive ».
- **Top 10 for Agentic Applications 2026** (décembre 2025) [FV] : ASI01 détournement d'objectif (injection indirecte par documents, e-mails, agendas), ASI02 mauvais usage d'outils, ASI03 abus d'identité et de privilèges, ASI04 chaîne d'approvisionnement (serveurs MCP), ASI05 exécution de code inattendue, ASI06 empoisonnement de mémoire, ASI08 défaillances en cascade, ASI10 agents incontrôlés. Mesures citées : « least privilege for agent tools », « human approval for high-impact or goal-changing actions », « comprehensive logging and continuous monitoring ».

**4. Lien avec le projet [FV via C5 et C7].**
- Plusieurs pièces contiennent des **instructions adressées à des assistants IA** : `crm/PASSATION.md:32-38` (« à joindre dans la nouvelle conversation », « Élargir l'accès réseau ») et les fichiers AGENTS et HANDOFF de BOJART (C7:228-234). C'est précisément le vecteur d'injection indirecte décrit par l'ANSSI (principe 6) et par l'OWASP (ASI01).
- Le CRM a été construit par des lots d'agents (48 commits « Claude », C5:34) et les relectures humaines ne sont pas tracées (C5:34).
- Jarvis revendique un fonctionnement « local d'abord » mais dépend de services distants payants (C7:162, C7:265).

### Sources officielles
| Source | Organisme | Date affichée | Citation courte |
|---|---|---|---|
| https://messervices.cyber.gouv.fr/guides/essentiels-ia-agentique (PDF : https://messervices.cyber.gouv.fr/documents-guides/anssi_essentiels_ia_agentique_1.0.pdf) | ANSSI | « Publié le 30 octobre 2026 », v1.0 (10/26) | « Garder le mécanisme d'approbation hors de portée du système agentique. » |
| https://messervices.cyber.gouv.fr/guides/recommandations-de-securite-pour-un-systeme-dia-generative | ANSSI | 29 avril 2024 | « limiter voire […] proscrire les actions automatiques […] à partir d'entrées non-maîtrisées » |
| https://cert.cyber.gouv.fr/actualite/CERTFR-2026-ACT-016/ | CERT-FR (ANSSI) | 13 avril 2026 | « une validation humaine doit être obligatoire dès qu'une commande système ou une action à effet de bord est envisagée » |
| https://www.cnil.fr/fr/ia-agentique-cnil-cianum-note | CNIL et CIANum | 20 juillet 2026 | « la mémoire des systèmes devrait être cloisonnée » (PDF de la note) |
| https://www.cnil.fr/fr/developpement-des-systemes-dia-les-recommandations-de-la-cnil-pour-respecter-le-rgpd | CNIL | 22 juillet 2025 | « Prévoir la possibilité de stopper le système » |
| https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/ | OWASP GenAI Security Project | 3 août 2026 | LLM01 « Prompt Injection », LLM03 « Excessive Agency » |
| https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ | OWASP GenAI Security Project | décembre 2025 | « Treat all natural-language inputs […] as untrusted » |

### Incertitudes et points à faire valider
- Aucune de ces recommandations n'est en soi une obligation légale. Elles servent de référence pour apprécier les « mesures appropriées » de l'article 32 du RGPD [HY].
- Les sources OWASP sont des référentiels communautaires, pas des textes administratifs.
- Le coût de mise en œuvre pour une équipe de deux personnes n'est pas chiffré [IN] → à intégrer au modèle de charge (autres chercheurs de l'audit).

### Conséquences pour Marwin Tech et GianLuca Carlone
**Grille minimale avant toute automatisation chez GianLuca Carlone** [PR, dérivée des sources ci-dessus] :

| Contrôle | Règle pratique | Source |
|---|---|---|
| Entrées non fiables | Les documents, e-mails, pages web et pièces du dépôt sont des données, jamais des ordres ; signaler toute instruction adressée à un assistant | ANSSI, principe 6 ; OWASP ASI01 |
| Classement des actions | Autonome : lire, résumer, proposer. Approbation humaine : envoyer un e-mail, appeler, modifier le CRM, engager une dépense, publier. Interdite : paiement, suppression de masse, changement de droits | ANSSI, principe 3 ; CERT-FR |
| Droits minimaux | Un compte et un jeton par agent et par client, en lecture seule par défaut, à durée courte | ANSSI, principes 4 et 6 ; OWASP ASI03 |
| Secrets | Coffre-fort ou proxy ; jamais dans les prompts, les journaux ou un dépôt | ANSSI, principe 6 ; documentation GitHub |
| Données | Offres professionnelles uniquement ; pseudonymisation ; aucune donnée client dans un dépôt de code | CNIL (2024, 2025) |
| Boucles et coûts | Plafond d'appels, de jetons et de dépenses par tâche et par jour ; alerte en cas de dépassement | ANSSI, principe 6 ; OWASP LLM06 (2026) |
| Journalisation | Journal hors de portée de l'agent : demande, autorisation, action, résultat, auteur humain | ANSSI, principe 7 ; OWASP ASI01 |
| Arrêt et reprise | Bouton d'arrêt avec révocation des accès ; procédure manuelle de secours ; restauration testée | ANSSI, principe 6 ; CNIL (2025) |
| Inventaire | Liste des agents, prompts système, connecteurs et serveurs MCP, versions ; revue annuelle | ANSSI, principe 7 ; OWASP ASI04 |

---

## Tableau récapitulatif

Niveaux de certitude : **élevé** = texte officiel lu ; **moyen** = page officielle lue par un intermédiaire, ou interprétation directe d'un texte ; **faible** = source secondaire ou hypothèse ; **[IN]** = non établi.

| Règle | Valeur ou condition | Source | Certitude |
|---|---|---|---|
| Démarchage téléphonique d'un consommateur | Consentement préalable depuis le 11/08/2026 ; un an de validité ; preuve conservée 3 ans ; fin de Bloctel [Changement 2026] | Fiche DGCCRF du 27/07/2026 ; Bloctel | moyen (lue par intermédiaire) |
| Exceptions au consentement (consommateur) | Contrat en cours si l'appel a un rapport avec son objet ; journaux et magazines | Fiche DGCCRF ; CNIL | moyen |
| Horaires et fréquence (consommateur) | Lundi-vendredi, 10 h-13 h et 14 h-20 h ; 4 appels ou tentatives par 30 jours glissants | FAQ DGCCRF du 17/09/2026 | moyen |
| Sanctions du démarchage illicite (consommateur) | Jusqu'à 75 000 € (personne physique) et 375 000 € (personne morale) | Fiche DGCCRF | moyen |
| Appels vers des professionnels | Hors du décret « jours et horaires » ; consentement non requis | FAQ DGCCRF ; CNIL | moyen |
| Prospection B2B (téléphone et e-mail) | Intérêt légitime si l'objet a un rapport avec la profession ; information ; opposition simple et gratuite | CNIL, pages du 10/06/2026 | élevé |
| Adresses génériques (contact@…) | Hors des règles de prospection des personnes | CNIL | élevé |
| Reconstitution d'adresses e-mail | Possible sur l'intérêt légitime sous conditions (visibilité, garanties) [Changement 2026] | CNIL, 16/10/2026 | élevé |
| Liste repoussoir | Au moins 3 ans ; empreintes hachées conseillées | CNIL | moyen (extrait) |
| Opposition Sirene (A123-96) | Données d'une personne physique non utilisables par des tiers pour la prospection | Insee | élevé |
| Base légale du fichier B2B | Intérêt légitime (art. 6, § 1, f ; considérant 47), à documenter | RGPD | élevé (texte) ; application [HY] |
| Information des personnes (données indirectes) | Au plus tard au premier contact, et au plus un mois ; source des données ; opposition présentée séparément | RGPD, art. 14, § 3, et art. 21, § 4 | élevé |
| Conservation des données de prospects | 3 ans après la collecte ou le dernier contact **émanant du prospect** | Référentiel CNIL | élevé |
| Contrat de sous-traitance | Écrit ; objet, durée, nature, finalité, données, personnes ; huit clauses a à h | RGPD, art. 28, § 3 et 9 | élevé |
| Clauses types de l'article 28 | Décision (UE) 2021/915 | JOUE | élevé |
| Registre des traitements | Obligatoire pour la gestion des prospects, même sous 250 salariés | RGPD, art. 30, § 5 ; CNIL | élevé |
| Amendes RGPD | Art. 83, § 4 : 10 M€ ou 2 % ; art. 83, § 5 : 20 M€ ou 4 % | RGPD | élevé |
| Violation de données | Définition : divulgation ou accès non autorisé, accidentel ou illicite | RGPD, art. 4, point 12 | élevé |
| Notification à la CNIL | Dans les meilleurs délais, si possible sous 72 h après connaissance, sauf absence de risque ; documentation toujours | RGPD, art. 33 ; CNIL | élevé |
| Information des personnes après violation | Si risque élevé, sauf exceptions de l'art. 34, § 3 | RGPD, art. 34 | élevé |
| Fuite GitHub du CRM | Violation probable ; délai de 72 h vraisemblablement atteint (connaissance au plus tard le 2/11) | `interne/audit-marwin-tech-carlone.md:3,15` ; analyse | faible à moyen [HY]/[ES] |
| Omnibus numérique du RGPD | Position du Conseil du 21/10/2026 (96 h, risque élevé) ; **non en vigueur** | Conseil de l'UE | élevé |
| Application générale du RIA | 2 août 2026 | RIA, art. 113 | élevé |
| Article 4 du RIA | Depuis le 02/02/2025 ; réécrit au 27/07/2026 : « prennent des mesures pour favoriser », sans niveau garanti [Changement 2026] | Omnibus IA, art. 1er, point 5 | élevé |
| Article 50 du RIA | Applicable au 02/08/2026 ; marquage de l'art. 50, § 2, au 02/12/2026 pour les systèmes déjà sur le marché [Changement 2026] | RIA ; Omnibus IA, art. 111, § 4 | élevé |
| Haut risque (annexe III / annexe I) | 2 décembre 2027 / 2 août 2028 [Changement 2026] | Omnibus IA, art. 113, c | élevé |
| Nouvelles interdictions de l'art. 5 | 2 décembre 2026 | Omnibus IA, art. 113, a | élevé |
| Amende pour l'article 50 | Jusqu'à 15 M€ ou 3 % ; pour une PME, le montant le plus faible | RIA, art. 99, § 4, g, et § 6 | élevé |
| Amende propre à l'article 4 | Aucune dans l'art. 99 | RIA, art. 99 | élevé |
| Autorités françaises (art. 50) | DGCCRF et Arcom (CNIL pour les émotions) ; loi de désignation non adoptée | DGE (09/2025) ; sources secondaires (11/2026) | moyen / [IN] |
| DPF UE–États-Unis | En vigueur ; pourvoi C-703/25 P pendant | Décision 2023/1795 ; JOUE | élevé |
| Anthropic et OpenAI sur la liste DPF | Non inscrits au 04/11/2026 | Liste officielle (interrogation) | élevé [MM] |
| Google LLC et GitHub sur la liste DPF | Actifs (GitHub : données non RH) | Liste officielle (interrogation) | élevé [MM] |
| AITD | Obligatoire avec les clauses types (art. 46) ; dispense si adéquation ou art. 49 | CNIL | élevé |
| Offres grand public des LLM | Entraînement possible sauf opposition ; Anthropic : 5 ans si l'option est activée [Changement 2025] | Pages Anthropic (28/08/2025) et OpenAI | moyen (éditeurs) |
| Agents IA : actions critiques | Approbation humaine obligatoire ; mécanisme hors de portée de l'agent | ANSSI, 30/10/2026 ; CERT-FR, 13/04/2026 | élevé (recommandation) |
| Agents IA : journaux | Inaltérables par l'agent ; chaîne demande → autorisation → action → résultat | ANSSI, 30/10/2026 | élevé (recommandation) |
| Top 10 OWASP LLM | Édition 2026 du 03/08/2026 ; « Excessive Agency » au 3e rang | OWASP | moyen (référentiel communautaire) |
| Texte exact de l'art. L223-1 (version 2026) | Non lu | Légifrance inaccessible | [IN] |

---

## Questions bloquantes à poser (avocat données personnelles, DPD)

1. **Aujourd'hui** : qui est responsable du traitement du fichier exposé sur GitHub ? Faut-il notifier la CNIL et à partir de quelle date de connaissance ? Faut-il informer les personnes (artistes, lignes personnelles) ?
2. Quelle entité de GianLuca Carlone démarche, signe le contrat de sous-traitance et figure dans les mentions d'information ?
3. L'argument « achat d'œuvre adossé à l'article 238 bis AB, donc lié à la fonction du dirigeant » suffit-il pour l'intérêt légitime ? Quel traitement réserver aux entrepreneurs individuels, aux artistes et aux lignes personnelles ?
4. Un assistant ou un agent vocal bâti sur l'API d'un LLM rend-il Marwin « fournisseur » au sens de l'article 50, § 1 et § 2, du RIA ? Un agent vocal sortant est-il un « automate d'appel » ?
5. Quelles offres d'IA (et quelles entités contractantes) Marwin peut-elle utiliser pour des données personnelles du client, et qui rédige l'AITD ?
