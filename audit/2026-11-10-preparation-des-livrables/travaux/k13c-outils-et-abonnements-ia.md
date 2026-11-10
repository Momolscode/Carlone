# Les outils et abonnements d'IA : offres supérieures, crédits d'API, outils spécialisés, automatisation

Note de travail interne — sources publiques consultées le 10 novembre 2026 — ce n'est pas un avis juridique, fiscal ou d'investissement.

Auteur : recherche préparatoire au dixième livrable (BRIEF-2, § 9.2). Ce n'est pas le livrable. Rien n'a été acheté, souscrit ni demandé. Les prix en dollars ne sont pas convertis, sauf mention contraire (taux indiqué).

Étiquettes : [Officiel] page de l'éditeur ; [Prix public daté] prix lu sur la page de l'éditeur le 10 novembre 2026 ; [Mesure publiée] chiffre mesuré publié par un tiers ou par l'éditeur ; [Source professionnelle] article ou comparatif ; [Estimation] calcul de cette note ; [À confirmer] non vérifié.

## En bref

<!-- EN-BREF -->

## 1. Assistants d'IA : offres individuelles supérieures et offres d'équipe

### 1.1 Anthropic (Claude)

Page lue : « Pricing », claude.com/pricing, consultée le 10 novembre 2026. La page dit : « Prices shown don't include applicable tax. » Les prix sont en dollars, hors taxes. Aucun prix en euros n'est affiché dans la version lue.

- **Pro** : 20 $ par mois en paiement mensuel ; 17 $ par mois en paiement annuel (200 $ payés d'avance). Ajoute Claude Code, la recherche approfondie, les projets, les tâches programmées, Claude dans Chrome, l'accès à Opus. Fable seulement avec des crédits d'usage (claude.com/pricing) [Prix public daté].
- **Max** : 100 $ par mois. « 5x Pro usage » toutes les cinq heures et chaque semaine. Fable jusqu'à la moitié des limites hebdomadaires. 100 $ de crédits d'API par mois. Accès prioritaire aux heures chargées (claude.com/pricing) [Prix public daté].
- **Ultra** : 200 $ par mois. Pas de limite de cinq heures pour les comptes vérifiés. « 10x Pro usage » par semaine. 200 $ de crédits d'API par mois (claude.com/pricing) [Prix public daté]. Changement 2026 : l'ancienne offre « Max 20x » à 200 $ semble remplacée par « Ultra » ; date du changement [À confirmer].
- **Offres individuelles (Free, Pro, Max, Ultra)** : pas de SSO, pas de console d'administration, pas de journal d'audit, pas de réglage de conservation (claude.com/pricing) [Officiel]. Pour ces offres, l'entraînement sur les conversations dépend d'un réglage de l'utilisateur ; la page parle de « model training opt-out by default » (claude.com/pricing) ; la règle publiée le 28 août 2025 prévoyait une conservation de cinq ans si l'utilisateur accepte l'entraînement (anthropic.com/news/updates-to-our-consumer-terms, repris de `audit/2026-11-04-audit-strategique/annexes/travaux/rj-R4-donnees-ia.md`) [Officiel]. Ces offres ne relèvent pas des « Commercial Terms » : pas d'accord de traitement des données (DPA) au sens professionnel [Officiel, même source].
- **Team** (2 à 150 places) : place Standard 20 $ (annuel) ou 25 $ (mensuel) par personne et par mois ; place Premium 100 $ (annuel) ou 125 $ (mensuel), avec « 5x the usage of standard seats ». Jusqu'à 500 $ par mois de crédits d'API mis en commun. Inclut Claude Code et Cowork, SSO, facturation centrale, « no training on content by default ». N'inclut pas : rôles, SCIM, journal d'audit, conservation sur mesure (claude.com/pricing) [Prix public daté].
- **Enterprise** : en libre-service, 20 $ par place et par mois, paiement annuel, **20 places au minimum**, plus l'usage facturé au tarif de l'API. Ajoute plafonds de dépense, rôles, SCIM, journal d'audit, conservation sur mesure, filtrage réseau. Offre accompagnée : prix sur demande (claude.com/pricing) [Prix public daté]. Pour cinq personnes, Enterprise n'est donc pas accessible en libre-service.
- **Données** : DPA d'Anthropic rattaché aux « Commercial Terms », transferts sur clauses contractuelles types ; Anthropic n'est pas inscrite au Data Privacy Framework au 4 novembre 2026 (rj-R4, sources officielles citées) [Officiel]. Hébergement : l'API propose un traitement limité aux États-Unis à 1,1 fois le prix ; aucune option « Europe » n'apparaît sur la page de prix (claude.com/pricing) [Officiel]. Traitement en Europe possible en passant par AWS ou Google Cloud selon `r1-nouveautes-ia-automatisation-2026.md` § 7.3 [À confirmer pour notre cas].

### 1.2 OpenAI (ChatGPT)

La page officielle chatgpt.com/pricing, lue le 10 novembre 2026, affiche les fonctions mais pas les montants dans la version lue (affichage dynamique). Les montants viennent de l'aide officielle et de relevés tiers datés.

- **Business, place Standard** : 20 $ par personne et par mois en paiement annuel, 25 $ en mensuel ; « at least 2 » places. Inclut ChatGPT, ChatGPT Work (l'agent) et Codex. Usage au-delà des limites : crédits d'espace de travail (help.openai.com, « ChatGPT Business overview », consultée le 10 novembre 2026) [Officiel].
- **Business, place Premium** : 100 $ (annuel) ou 125 $ (mensuel) par personne et par mois ; plus d'usage pour ChatGPT Work et Codex, « no five-hour usage limit » (même page) [Officiel]. Places Premium introduites le 24 août 2026 selon jeanhinz.io (6 juillet 2026, mis à jour le 2 novembre 2026) [Source professionnelle].
- **En euros**, relevé tiers de la page allemande le 2 novembre 2026 : Plus 23 € ; Pro 100 : 103 € ; Pro 200 : 229 € ; Pro 500 : 510 € ; Business Standard 21 € (annuel) ou 26 € (mensuel) ; Premium 105 € ou 130 €. La page ne dit pas si la TVA est comprise. Pour Plus et Pro, les mêmes montants apparaissent sur l'App Store allemand, TVA comprise : ce sont donc très probablement des prix toutes taxes comprises (jeanhinz.io/chatgpt/preise, 2 novembre 2026) [Source professionnelle]. Plus à 23 € et Pro à partir de 103 € sont aussi relevés sur chatgpt.com/fr-FR/pricing le 1er novembre 2026 (lesastucesia.com, observatoire des prix) [Source professionnelle]. Prix français hors taxes : [À confirmer].
- **Pro** : trois niveaux d'usage (chatgpt.com/pricing) [Officiel] ; 100 $, 200 $ ou 500 $ (satoriml.com, 24 septembre 2026) [Source professionnelle]. Pro 500 : « 25 fois » l'usage de Plus selon OpenAI, cité par jeanhinz.io [Source professionnelle]. Pro donne des sessions Codex et ChatGPT Work plus longues, « Dot, your always-on agent », un contexte de 400 000 unités contre 256 000 pour Plus (chatgpt.com/pricing) [Officiel]. Changement 2026 : l'offre unique à 200 $ a été découpée en trois niveaux ; nouvelles inscriptions à Pro 200 suspendues en septembre puis rouvertes avec un quota réduit (jeanhinz.io ; satoriml.com) [Source professionnelle].
- **Codex dans les offres** : fourchettes de messages par période de cinq heures, identiques pour Plus et Business Standard (par exemple 15 à 160 pour GPT-6.1 Sol, 5 à 45 pour GPT-6 Astra) ; « Weekly limits may also apply » ; Enterprise avec tarification souple : « no fixed rate limits — usage scales with credits » (chatgpt.com/codex/pricing, consultée le 10 novembre 2026) [Officiel]. Limite commune ChatGPT et Codex annoncée pour décembre 2026 selon jeanhinz.io [À confirmer].
- **Données** : Free, Plus et Pro : « we may use your content to train our models » sauf opposition ; Business, Enterprise, Edu et API : pas d'entraînement par défaut ; DPA conclu avec OpenAI Ireland Ltd. pour un client de l'EEE (rj-R4, pages officielles OpenAI) [Officiel]. Résidence des données en Europe : Enterprise et Edu, pas Business, selon jeanhinz.io et r1 § 7.3 [À confirmer]. OpenAI n'est pas inscrite au Data Privacy Framework au 4 novembre 2026 (rj-R4) [Officiel].

### 1.3 Google (Gemini, Google AI, Workspace)

- **Offres individuelles en France** (page gemini.google/fr/subscriptions, lue via moteur de recherche le 10 novembre 2026) : Google AI Plus 4,99 € par mois ; Google AI Pro 21,99 € par mois (« quatre fois » l'usage de la version gratuite, Gemini 4 Argon) ; Google AI Ultra 99,99 € par mois (« cinq fois » AI Pro) ou 219,99 € par mois (« 20 fois » AI Pro) [Prix public daté]. Ces prix grand public sont toutes taxes comprises selon nextstart.ai (31 octobre 2026) [Source professionnelle]. Changement 2026 : AI Plus passé de 7,99 € à 4,99 € en juin 2026 ; Ultra découpé en deux niveaux (nextstart.ai) [Source professionnelle]. AI Pro inclut un accès élargi à l'outil de programmation Antigravity et 10 $ de crédits Google Cloud par mois ; Ultra 5x : 40 $ ; Ultra 20x : 100 $ (nextstart.ai) [Source professionnelle].
- **Workspace** (prix hors taxes par personne et par mois) : Business Starter 6,80 € (annuel) ou 8,10 € (flexible) ; Business Standard 13,60 € ou 16,20 € ; Business Plus 21,10 € ou 25,30 €. Gemini est inclus ; dans Docs, Sheets, Meet à partir de Business Standard (nextstart.ai, 31 octobre 2026 ; epickone.fr, relevé du 4 novembre 2026 sur workspace.google.com/intl/fr/pricing ; oversales.fr, 7 septembre 2026) [Source professionnelle ; page officielle non relue ici].
- **Données** : pour Workspace, données de l'entreprise non utilisées pour entraîner les modèles ; lieu de traitement garanti seulement sur l'offre la plus haute (r1 § 7.3) [À confirmer]. Les offres Google AI grand public se prennent sur un compte personnel : à éviter pour des données de client (règle CNIL citée dans rj-R4) [Officiel].

### 1.4 Mistral (Le Chat, désormais présenté sous le nom Vibe)

- **Pro** : 14,99 $ par mois hors taxes ; 15 $ de crédits d'API par mois ; programmation « toute la journée » en ligne de commande, dans l'éditeur et en ligne ; jusqu'à cinq tâches programmées (mistral.ai/pricing, consultée le 10 novembre 2026) [Prix public daté]. En euros : 17,99 € TTC relevé le 1er novembre 2026 (lesastucesia.com) [Source professionnelle].
- **Team** : 24,99 $ par personne et par mois hors taxes ; limites plus hautes ; 30 Go par personne ; tâches programmées illimitées (mistral.ai/pricing) [Prix public daté].
- **Enterprise** : sur devis ; SSO, journal d'audit, déploiement chez le client (sur ses serveurs ou nuage privé) (mistral.ai/pricing) [Officiel].
- **Données** : la page montre une option « Opt-out » pour l'entraînement et un lien vers un accord de traitement ; elle ne dit pas quelle offre bénéficie de quoi, ni où les données sont hébergées (mistral.ai/pricing) [À confirmer]. Mistral est une société française ; l'hébergement européen par défaut est [À confirmer] sur sa page « confidentialité ».

### 1.5 Microsoft 365 Copilot

- **Copilot Business** (complément à une suite Microsoft 365) : 18,20 € HT par personne et par mois avec engagement annuel ; 21,84 € HT en paiement mensuel ; promotion à 15,60 € HT du 1er juillet au 31 décembre 2026, la première année seulement. Offres groupées : Business Standard avec Copilot 20,36 € HT ; Business Premium avec Copilot 27,73 € HT, engagement annuel (microsoft.com/fr-fr/copilot/pricing/business et microsoft.com/fr-fr/microsoft-365-copilot/pricing, relevé du 9 novembre 2026 dans r1 § 9.2 ; mêmes montants chez epickone.fr le 4 novembre 2026) [Prix public daté, relevé de la veille, non relu le 10 novembre]. Le prix groupé est inférieur à la somme des deux : conditions [À confirmer].
- **Agents** : Copilot Cowork et les agents de Copilot Studio sont facturés à part, en crédits (0,01 $ l'unité selon Microsoft, r1 § 9.4) [Officiel]. Les modèles d'Anthropic dans Copilot sont exclus de la frontière de données de l'UE et désactivés par défaut en Europe (r1 § 1.3 et § 7.3) [Officiel].
- **Particuliers** : Microsoft 365 Premium, 22 € par mois ou 219 € par an, remplace l'ancien Copilot Pro (lesastucesia.com, 1er novembre 2026) [Source professionnelle].

## 2. Agents de programmation et d'automatisation

- **Claude Code** : inclus dans Pro, Max, Ultra, Team et Enterprise ; absent de Free (claude.com/pricing) [Officiel]. Pro ajoute aussi le « hand-off » et les tâches programmées (même page) [Officiel]. Les limites de Max et Ultra (5 et 10 fois Pro) s'appliquent aussi à Claude Code, qui puise dans le même quota (claude.com/pricing) [À confirmer pour le détail]. Côté API, Anthropic propose des « Managed Agents », limités à 300 créations et 1 200 lectures par minute (platform.claude.com/docs/en/api/rate-limits) [Officiel] ; prix [À confirmer] (la page de prix lue était tronquée).
- **Codex (OpenAI)** : inclus dans toutes les offres ChatGPT ; Plus « power a few focused coding sessions each week » ; Pro « designed for longer, higher-intensity sessions each day » ; les messages locaux et les tâches dans le nuage partagent le même quota ; au-delà, des crédits (chatgpt.com/codex/pricing) [Officiel]. L'Ultrafast (réponses plus rapides) n'est ouvert qu'à Pro 500 parmi les offres Pro (jeanhinz.io, 2 novembre 2026) [Source professionnelle].
- **Autres outils reconnus** : Cursor : Plus 8 $, Premium 30 $, Super 100 $, Ultra 200 $, Teams à partir de 30 $ par personne, hors taxes ; GitHub Copilot : Pro 10 $, Pro+ 39 $, Max 100 $ (lesastucesia.com, relevé du 1er novembre 2026 sur cursor.com/pricing et github.com/features/copilot/plans) [Source professionnelle]. Mistral Pro inclut un agent de programmation (Vibe CLI, Devstral) (mistral.ai/pricing) [Officiel].
- **Ce qui change pour une équipe de deux** : un agent peut travailler en arrière-plan sur une tâche pendant que la personne fait autre chose ; plusieurs sessions peuvent tourner en même temps. Le plafond n'est plus la vitesse de frappe mais (a) le quota de l'offre, (b) le temps de relecture humaine, (c) la clarté de la demande [Estimation]. Aucune mesure publiée de gain de productivité n'a été lue pour cette note : tout gain chiffré reste une « hypothèse à évaluer » (voir § 9).
- **Limites** : quotas par période de cinq heures et par semaine (Claude, Codex) ; arrêt quand le quota est épuisé, sauf crédits payants ; une offre individuelle (Pro, Max, Ultra, ChatGPT Pro) est personnelle et ne se partage pas ; l'agent se trompe et recommence, ce qui consomme davantage (r1 § 9.4) [Officiel pour les quotas ; Estimation pour le reste].
- **Automatisation (n8n)** : Starter limité à 5 exécutions simultanées et 5 minutes par exécution ; Pro jusqu'à 50 exécutions simultanées et 40 minutes (n8n.io/pricing, consultée le 10 novembre 2026) [Officiel]. C'est une limite concrète pour des traitements longs.

## 3. Crédits d'API : prix, remises, limites de débit

Prix en dollars hors taxes par million d'unités de texte (« tokens »), entrée / sortie.

| Modèle | Entrée | Sortie | Lecture en cache | Source |
| --- | --- | --- | --- | --- |
| Claude Fable 5.2 | 8 $ | 40 $ | 0,20 $ | claude.com/pricing [Prix public daté] |
| Claude Opus 5.5 | 4 $ | 20 $ | 0,20 $ | idem |
| Claude Sonnet 5.5 | 2 $ | 10 $ | 0,10 $ | idem |
| Claude Haiku 5.5 (jusqu'à 100 000 unités) | 0,10 $ | 0,50 $ | 0,01 $ | idem |
| GPT-6 Astra | 10 $ | 50 $ | 1 $ | developers.openai.com/api/docs/pricing [Prix public daté] |
| GPT-6.1 Sol | 2 $ | 10 $ | 0,10 $ | idem |
| GPT-6 Luna | 0,10 $ | 0,50 $ | 0,01 $ | idem |
| Mistral Large | 0,5 $ | 1,5 $ | — | mistral.ai/pricing (FAQ) [Prix public daté] |

- **Remises** : traitement par lots −50 % chez Anthropic, OpenAI (« Batch » et « Flex ») et Mistral [Officiel, trois pages]. Cache : lecture à environ 5 % du prix d'entrée chez Anthropic (0,20 $ contre 4 $ pour Opus 5.5) ; « jusqu'à 90 % » de moins chez Mistral [Officiel].
- **Surcoûts** : mode rapide ×2 (Opus 5.5 et Fable 5.2 ; « up to 2.5x faster ») ; traitement limité aux États-Unis ×1,1 (claude.com/pricing) [Officiel]. OpenAI : « Fast » ×2 ; traitement régional (résidence des données) +10 % pour les modèles sortis depuis le 5 mars 2026 (developers.openai.com/api/docs/pricing) [Officiel]. Changement 2026 : « Priority processing was renamed Fast mode on July 30, 2026 » (même page) [Officiel].
- **Limites de débit Anthropic** (platform.claude.com/docs/en/api/rate-limits, consultée le 10 novembre 2026) [Officiel] :

| Niveau | Plafond de dépense mensuel | Opus 5.5 : requêtes / min | Entrée / min | Sortie / min | Lots en file |
| --- | --- | --- | --- | --- | --- |
| Start | 500 $ | 4 000 | 2 000 000 | 400 000 | 200 000 |
| Build | 1 000 $ | 10 000 | 5 000 000 | 1 000 000 | 300 000 |
| Scale | 200 000 $ | 13 000 | 10 000 000 | 2 000 000 | 500 000 |

  Une nouvelle organisation peut démarrer au niveau « Evaluation », plus bas, le temps d'établir un historique. Les unités lues en cache ne comptent pas dans la limite d'entrée. Un lot peut contenir 100 000 requêtes. Ce sont des maximums, « not guaranteed minimums » (même page) [Officiel]. Limites OpenAI par niveau : non lues [À confirmer].

- **Calcul « documents traités par heure »** [Estimation, hypothèses explicites] : un devis ou une facture de trois pages, avec ses consignes, fait environ 5 000 unités en entrée et 1 000 en sortie (hypothèse à mesurer pendant l'essai). Au niveau Start, Opus 5.5 plafonne à 2 000 000 / 5 000 = 400 documents par minute en entrée et 400 000 / 1 000 = 400 en sortie, soit environ 24 000 documents par heure au maximum théorique. Coût par document : Opus 5.5 ≈ 0,04 $ (0,02 $ par lots) ; Sonnet 5.5 ≈ 0,02 $ ; Haiku 5.5 ≈ 0,001 $. Mille documents par mois coûtent donc entre 1 $ et 40 $ selon le modèle. Le débit machine n'est jamais le goulet : la relecture humaine l'est (voir § 9).


## Compléments du 10 novembre 2026

Ajouté le 10 novembre 2026 par la relecture sceptique. La note s’arrêtait après le § 3. Le repère « En bref » était vide. Le « § 9 » cité aux lignes 62 et 93 n’existe pas. Trois questions du cahier des charges (`outils/2026-11-10-orchestration/workflows/prep-moyens.js`, entrée k13c) n’étaient pas traitées : outils spécialisés, plateformes d’automatisation, budget mensuel. Cette partie les complète, en dix lectures ou recherches au plus ; les échecs sont dits. Les prix en dollars ne sont pas convertis. La partie « Vérification du 10 novembre 2026 », plus bas, l’emporte sur toute la note.

### En bref (à lire à la place du repère vide en tête de note)

1. Une offre supérieure achète surtout du quota : plus d’usage par période de cinq heures et par semaine, des sessions d’agent plus longues, des crédits d’API. L’accès aux modèles les plus chers dépend aussi de l’offre.
2. Pour des données de client, il faut une offre d’équipe ou l’API, pas une offre individuelle. Les places d’équipe coûtent le même prix chez Anthropic et OpenAI : 20 $ (annuel) ou 25 $ (mensuel) en Standard, 100 $ ou 125 $ en Premium, hors taxes chez Anthropic.
3. L’API coûte peu par document : de 0,001 $ à 0,04 $ pour un devis de trois pages [Estimation]. Au démarrage, le premier frein est le plafond de dépense du niveau d’usage (500 $ par mois au niveau Start chez Anthropic), puis la relecture humaine.
4. Automatisation : n8n est la seule plateforme dont la page de prix dit où sont les données (Francfort) ; 20 € ou 50 € par mois en paiement annuel.
5. Budget [Estimation à valider] : deux personnes en offre d’équipe renforcée, environ 200 à 250 $ par mois, plus 50 € d’automatisation et l’API ; cinq personnes, environ 260 à 325 $ par mois, plus automatisation et API.

### C1. Outils spécialisés (question 4 du cahier des charges)

**Lecture de documents et extraction en tableaux.**

- Mistral OCR 4 : 4 $ les 1 000 pages, 2 $ en traitement par lots, indice de confiance par mot (mistral.ai/news/ocr-4, 23 juin 2026 ; confirmé par la vérification de r1 le 9 novembre 2026, liste « Confirmés tels quels », n° 19) [Prix public daté, relu la veille]. La page mistral.ai/pricing lue le 10 novembre dit seulement que l’OCR se facture « per 1,000 pages », sans montant.
- Azure AI Document Intelligence (Microsoft) : 500 pages gratuites par mois sur l’instance gratuite, sans les fonctions avancées ; prix à l’usage non affichés dans la version lue (« $- ») ; régions européennes proposées, dont France Central (azure.microsoft.com, « Document Intelligence pricing », lue le 10 novembre 2026) [Officiel ; prix À confirmer].
- Google Document AI : page de prix illisible le 10 novembre 2026 [À confirmer].
- Autre voie, chiffrée au § 3 : faire lire le document par un modèle généraliste via l’API, de 0,001 $ à 0,04 $ par devis de trois pages [Estimation].

**Transcription de réunions.**

- API OpenAI : gpt-4o-transcribe 0,006 $ la minute ; gpt-4o-mini-transcribe 0,003 $ ; gpt-transcribe 0,0045 $ (developers.openai.com/api/docs/pricing, lue le 10 novembre 2026) [Prix public daté].
- Mistral Voxtral : 0,0035 $ la minute annoncé (r1 § 3, d’après mistral.ai/news/voxtral-3, 22 octobre 2026) ; la page de prix du 10 novembre ne donne pas le montant [À confirmer].
- Google Workspace : la prise de notes en réunion fait partie de Gemini dans Meet ; absente de Business Starter, présente à partir de Business Standard (workspace.google.com/intl/fr/pricing, lue le 10 novembre 2026) [Officiel].
- Règle : informer les participants. La CNIL a annoncé des travaux sur la transcription ; aucune recommandation dédiée trouvée au 9 novembre (r1 § 8.5) [À confirmer].

**Agents vocaux en français.**

- API OpenAI, conversation vocale en temps réel : gpt-realtime-2.1, 32 $ par million d’unités audio en entrée et 64 $ en sortie ; gpt-realtime-2.1-mini, 10 $ et 20 $ (developers.openai.com/api/docs/pricing, lue le 10 novembre 2026) [Prix public daté]. Coût à la minute : non calculé, faute de savoir combien d’unités compte une minute de parole [À confirmer].
- ElevenLabs : abonnements de 6 $ (Starter) à 990 $ (Business) par mois ; « Prices exclude all taxes » ; licence commerciale à partir de Starter ; prix des agents à la minute non affiché dans la version lue ; aucune mention d’hébergement dans l’Union (elevenlabs.io/pricing, lue le 10 novembre 2026) [Prix public daté ; agents À confirmer].
- Offres d’accueil téléphonique prêtes à l’emploi : de 79 € HT à 349 € par mois selon le vendeur (r1 § 3.1, relevé du 9 novembre 2026, non relu) [Source professionnelle].
- Règle : l’appelant doit savoir qu’il parle à un système automatisé. C’est l’article 50, § 1, du règlement européen sur l’IA, applicable depuis le 2 août 2026 ; l’obligation pèse sur le fournisseur de l’outil (r1 § 8.3, confirmé le 9 novembre). Le paquet « omnibus » sur l’IA ne la décale pas, selon des sources professionnelles lues le 10 novembre 2026 (usercentrics.com ; iubenda.com) [Officiel via r1 ; Source professionnelle pour l’omnibus].

**Images et vidéos pour la communication.**

- Google, API Gemini, offre payante : Gemini 3.1 Flash Image environ 0,067 $ par image en 1K et 0,101 $ en 2K ; Gemini 3 Pro Image environ 0,134 $ ; vidéo Gemini Omni 1.2 Flash environ 0,07 $ la seconde en 720p, son compris, jusqu’à 15 secondes. Contenus de l’offre payante « not used to improve our products » (aistudio.google.com/docs/pricing, lue le 10 novembre 2026 ; page tronquée : Veo et Imagen non lus) [Prix public daté].
- OpenAI gpt-image-2 : 30 $ par million d’unités d’image produites, 8 $ en entrée image, 5 $ en entrée texte ; pas de prix par image sur la page (developers.openai.com/api/docs/pricing, 10 novembre 2026) [Prix public daté].
- Abonnements Google : AI Plus 200 crédits Flow ; AI Pro 1 000 ; Ultra 10 000 ou 25 000 (gemini.google/fr/subscriptions, 10 novembre 2026) [Officiel].
- Droits d’usage : conditions d’OpenAI pour l’Europe illisibles le 10 novembre 2026 (refus d’accès) ; ElevenLabs indique une licence commerciale à partir de Starter. Pour les autres outils [À confirmer].
- Mention obligatoire : un trucage réaliste (image, son, vidéo) est signalé par celui qui le diffuse (article 50, § 4). Le marquage lisible par machine incombe au fournisseur (article 50, § 2), avec un délai jusqu’au 2 décembre 2026 pour les systèmes déjà sur le marché avant le 2 août 2026 (r1, confirmé le 9 novembre ; mêmes dates dans les sources professionnelles lues le 10 novembre). Publication de l’omnibus au Journal officiel : non vérifiée. Une image générée n’est jamais présentée comme une photo réelle.

### C2. Plateformes d’automatisation (question 5)

| Plateforme | Offre | Prix public | Limites lues | Hébergement des données | Source (lue le 10 novembre 2026) |
| --- | --- | --- | --- | --- | --- |
| n8n en ligne | Starter | 20 € par mois, paiement annuel ; taxes non précisées | 2 500 exécutions par mois ; 5 simultanées ; 5 minutes par exécution | Union européenne, Francfort (FAQ de la page) | n8n.io/pricing |
| n8n en ligne | Pro | 50 € par mois, paiement annuel | 10 000 exécutions ; 20 à 50 simultanées ; 40 minutes | idem | idem |
| n8n auto-hébergé | Business | 667 € par mois, paiement annuel | 40 000 exécutions | là où on l’installe | idem |
| n8n auto-hébergé | Community | prix non indiqué sur la page (code publié sur GitHub ; licence à lire) | — | là où on l’installe | idem |
| Zapier | Professional | à partir de 19,99 $ par mois (annuel, 750 tâches) ou 29,99 $ (mensuel) ; taxes non indiquées | déclenchement toutes les 2 minutes ; 1 place ; dépassement facturé à la tâche (1,25 fois en annuel, 2,5 fois en mensuel), arrêt à 3 fois le forfait | non indiqué | zapier.com/pricing |
| Zapier | Team | à partir de 69 $ par mois (annuel, 2 000 tâches) ou 103,50 $ (mensuel) | 1 minute ; 25 places | non indiqué | idem |
| Make | Core, Pro, Teams | montants non affichés dans la version lue | Free : 1 000 crédits par mois ; crédits supplémentaires par blocs de 10 000 | non indiqué | make.com/en/pricing |
| Power Automate | Premium | 13,00 € HT par utilisateur et par mois, paiement annuel | — | non lu | microsoft.com/fr-fr/power-platform/products/power-automate/pricing |
| Power Automate | Process ; Hosted Process | 130,00 € HT ; 186,30 € HT par robot et par mois, paiement annuel | — | non lu | idem |

Lecture : prix de Make [À confirmer] ; hébergement de Zapier et de Make [À confirmer]. Les agents de Copilot Studio se paient en crédits ; la page française du 10 novembre 2026 n’affiche pas de montant.

### C3. Budget mensuel (question 6) [Estimation, chaque ligne sourcée]

Hypothèses : prix publics du 10 novembre 2026 ; dollars non convertis ; taxes non comprises (Anthropic, Mistral et Microsoft les excluent ; n8n et Zapier ne disent rien). Les abonnements que Marwin Tech paie aujourd’hui ne sont pas connus (U27 ; plusieurs prélèvements en échec, `audit/2026-11-04-audit-strategique/interne/02-etat-des-sources.md`, ligne 340) : la ligne (a) est une hypothèse. Le volume de 10 000 devis par mois est un exemple, pas une mesure.

| Cas | Composition | Coût mensuel | Sources |
| --- | --- | --- | --- |
| (a) Deux personnes, moyens actuels (hypothèse) | 2 places Claude Pro, paiement mensuel ; n8n Starter | 40 $ + 20 € | claude.com/pricing ; n8n.io/pricing |
| (b1) Deux personnes, offres individuelles supérieures | 2 places Claude Max (200 $ de crédits d’API inclus) ; n8n Pro ; API | 200 $ + 50 € + API au-delà des crédits (0 $ avec Sonnet 5.5, 200 $ avec Opus 5.5, pour 10 000 devis) | claude.com/pricing ; § 3 |
| (b2) Deux personnes, offre d’équipe renforcée (données de client) | Claude Team, 2 places Premium ; n8n Pro ; API | 200 $ (annuel) ou 250 $ (mensuel) + 50 € + API (crédits mis en commun « jusqu’à 500 $ », condition non lue) | claude.com/pricing ; n8n.io/pricing |
| (c) Cinq personnes en offre d’équipe | Claude Team ou ChatGPT Business : 2 places Premium et 3 Standard ; n8n Pro ; API | 260 $ (annuel) ou 325 $ (mensuel) + 50 € + API | claude.com/pricing ; aide OpenAI « ChatGPT Business overview » ; n8n.io/pricing |
| (c’) Cinq personnes, Claude Enterprise en libre-service | 20 places au minimum | 400 $ + usage au tarif de l’API | claude.com/pricing |

Calculs : (a) 2 × 20 $ = 40 $. (b1) 2 × 100 $ = 200 $ ; 10 000 × 0,02 $ = 200 $ avec Sonnet 5.5, couverts par les crédits ; 10 000 × 0,04 $ = 400 $ avec Opus 5.5, dont 200 $ au-delà des crédits. (b2) 2 × 100 $ = 200 $ ; 2 × 125 $ = 250 $. (c) 2 × 100 $ + 3 × 20 $ = 260 $ ; 2 × 125 $ + 3 × 25 $ = 325 $. (c’) 20 × 20 $ = 400 $.

Lecture : (b2) coûte à peu près comme (b1) mais donne les conditions professionnelles et le SSO ; c’est le cas cohérent pour des données de client. Pour cinq personnes, Enterprise coûte plus que Team ; il n’ajoute que le journal d’audit, la conservation sur mesure, les rôles et le SCIM.

## Vérification du 10 novembre 2026

Relecture sceptique du 10 novembre 2026. Cette partie l’emporte sur le reste de la note (BRIEF-2 § 4). Dix lectures ou recherches : claude.com/pricing ; platform.claude.com/docs/en/api/rate-limits ; developers.openai.com/api/docs/pricing ; n8n.io/pricing ; mistral.ai/pricing ; microsoft.com/fr-fr/microsoft-365-copilot/pricing ; gemini.google/fr/subscriptions ; recherche sur l’aide OpenAI « ChatGPT Business overview » ; workspace.google.com/intl/fr/pricing ; recherche sur la liste du Data Privacy Framework. En plus, sans recherche : la documentation développeur d’Anthropic fournie avec l’outil de travail (mise en cache le 3 novembre 2026), pour le mode rapide et le traitement limité aux États-Unis. Ce qui n’a pas été relu reste « non vérifié ».

**Conclusion.** Les prix d’Anthropic, de l’API d’OpenAI, de Microsoft, de Google AI, de Mistral et de n8n sont justes au 10 novembre 2026. Trois erreurs de fond : la lecture en cache ne coûte pas « environ 5 % » partout ; le calcul des documents par heure oublie le plafond de dépense mensuel ; la phrase sur l’hébergement de Workspace vise la mauvaise offre. Restent non vérifiés : les prix en euros d’OpenAI et de Workspace, Cursor et GitHub Copilot, les dates des changements d’offres, l’inscription au Data Privacy Framework.

### Tableau des contrôles (les douze affirmations qui pèsent le plus)

| n° | Affirmation de la note (ligne) | Verdict | Source et date |
| --- | --- | --- | --- |
| 1 | Claude Pro 17 $ (annuel, 200 $ d’avance) ou 20 $ ; Max 100 $, « 5x Pro usage », 100 $ de crédits d’API ; Ultra 200 $, « 10x Pro usage » par semaine, pas de limite de cinq heures, 200 $ de crédits ; prix hors taxes (l. 17-21) | confirmé ; « pour les comptes vérifiés » (Ultra) et « accès prioritaire » (Max) non vérifiés | claude.com/pricing, lue le 10 novembre 2026 |
| 2 | Team : Standard 20 $ / 25 $ ; Premium 100 $ / 125 $ (« 5x ») ; 2 à 150 places ; jusqu’à 500 $ de crédits mis en commun ; SSO ; ni journal d’audit ni conservation sur mesure ; pas d’entraînement par défaut (l. 23) | confirmé | idem |
| 3 | Enterprise en libre-service : 20 $ par place, annuel, 20 places au minimum, usage au tarif de l’API ; « pour cinq personnes, pas accessible » (l. 24) | prix confirmé ; conclusion corrigée (correction 3) | idem |
| 4 | API Anthropic : Fable 5.2 8 $ / 40 $ / 0,20 $ ; Opus 5.5 4 $ / 20 $ / 0,20 $ ; Sonnet 5.5 2 $ / 10 $ / 0,10 $ ; Haiku 5.5 0,10 $ / 0,50 $ / 0,01 $ jusqu’à 100 000 unités (l. 72-75) | confirmé ; au-delà de 100 000 unités, Haiku 5.5 passe à 0,50 $ / 2,50 $ | claude.com/pricing, 10 novembre 2026 ; documentation développeur Anthropic, 3 novembre 2026 |
| 5 | Lecture en cache « à environ 5 % du prix d’entrée chez Anthropic » (l. 81) | corrigé : de 2,5 % à 10 % selon le modèle (correction 1) | claude.com/pricing, 10 novembre 2026 |
| 6 | Limites Anthropic : Start 500 $, Build 1 000 $, Scale 200 000 $ ; Opus 5.5 : 4 000 / 2 000 000 / 400 000, puis 10 000 / 5 000 000 / 1 000 000, puis 13 000 / 10 000 000 / 2 000 000 ; lots en file 200 000 / 300 000 / 500 000 ; 100 000 requêtes par lot ; niveau « Evaluation » ; cache hors limite d’entrée (l. 85-91) | confirmé | platform.claude.com/docs/en/api/rate-limits, lue le 10 novembre 2026 |
| 7 | Environ 24 000 documents par heure au niveau Start ; « le débit machine n’est jamais le goulet » (l. 93) | arithmétique juste ; conclusion corrigée (correction 2) | idem |
| 8 | API OpenAI : GPT-6 Astra 10 $ / 50 $ / 1 $ ; GPT-6.1 Sol 2 $ / 10 $ / 0,10 $ ; GPT-6 Luna 0,10 $ / 0,50 $ / 0,01 $ ; « Fast » ×2 ; renommage le 30 juillet 2026 ; +10 % pour le traitement régional des modèles sortis depuis le 5 mars 2026 (l. 76-78, 82) | confirmé ; précision : prix du contexte court (jusqu’à 272 000 unités en entrée) ; le « −50 % » par lots se déduit des tableaux, il n’est pas écrit | developers.openai.com/api/docs/pricing, lue le 10 novembre 2026 |
| 9 | ChatGPT Business : Standard 20 $ (annuel) / 25 $ (mensuel), au moins 2 places ; Premium 100 $ / 125 $, « no five-hour usage limit » (l. 31-32) | confirmé (Premium : 5 fois l’usage Standard ; 200 places au plus) ; date d’arrivée des places Premium (24 août 2026) non vérifiée | aide OpenAI « ChatGPT Business overview », vue par moteur de recherche le 10 novembre 2026 (page non ouverte) |
| 10 | Google AI en France : Plus 4,99 € ; Pro 21,99 € (« quatre fois ») ; Ultra 99,99 € (« cinq fois ») ou 219,99 € (« 20 fois ») ; Gemini 4 Argon ; « TTC » ; crédits Google Cloud 10 $ / 40 $ / 100 $ ; « accès élargi » à Antigravity (l. 40) | prix et multiplicateurs confirmés ; TTC non vérifié (la page ne le dit pas) ; crédits Google Cloud non vérifiés (absents de la page) ; Antigravity corrigé (correction 4) | gemini.google/fr/subscriptions, lue le 10 novembre 2026 |
| 11 | Copilot Business : 18,20 € HT annuel ; 21,84 € HT mensuel ; promotion 15,60 € HT du 1er juillet au 31 décembre 2026, la première année ; Business Standard + Copilot 20,36 € HT ; Business Premium + Copilot 27,73 € HT (l. 53) | confirmé ; précision : promotion réservée aux clients Microsoft 365 Business existants ; en mensuel, 24,43 € HT et 33,28 € HT | microsoft.com/fr-fr/microsoft-365-copilot/pricing, lue le 10 novembre 2026 |
| 12 | n8n : Starter 5 exécutions simultanées, 5 minutes ; Pro jusqu’à 50, 40 minutes (l. 64) | confirmé (Pro : « 20 / 50 » dans le tableau de la page) | n8n.io/pricing, lue le 10 novembre 2026 |

Autres contrôles :

| n° | Affirmation de la note (ligne) | Verdict | Source et date |
| --- | --- | --- | --- |
| 13 | Mistral : Pro 14,99 $ HT, 15 $ de crédits ; Team 24,99 $ HT, 30 Go par personne ; Enterprise sur devis, déploiement chez le client ; Mistral Large 0,5 $ / 1,5 $ ; lots −50 % ; cache jusqu’à −90 % (l. 46-48, 79, 81) | confirmé ; version de Mistral Large non précisée ; « jusqu’à cinq tâches programmées » pour Pro non vérifié (la page ne dit pas clairement quelle offre) ; 17,99 € TTC non vérifié | mistral.ai/pricing, lue le 10 novembre 2026 |
| 14 | Anthropic : mode rapide ×2 (Opus 5.5 8 $ / 40 $ ; Fable 5.2 16 $ / 80 $), « up to 2.5x faster » ; traitement limité aux États-Unis ×1,1 ; pas d’option Europe (l. 25, 82) | confirmé par la documentation développeur ; absent de la page de prix lue | documentation développeur Anthropic, mise en cache le 3 novembre 2026 |
| 15 | Workspace : prix en euros (l. 41) ; « lieu de traitement garanti seulement sur l’offre la plus haute » (l. 42) | prix non vérifiés (page lue en dollars ; paiement annuel « économisez 16 % ») ; Gemini dans Docs et Meet dès Business Standard confirmé ; hébergement corrigé (correction 5) | workspace.google.com/intl/fr/pricing, lue le 10 novembre 2026 |
| 16 | Anthropic et OpenAI non inscrites au Data Privacy Framework au 4 novembre 2026 (l. 25, 36) | non vérifié : la recherche n’a trouvé aucune fiche, ni dans un sens ni dans l’autre | recherche du 10 novembre 2026 ; à lire sur dataprivacyframework.gov/list |
| 17 | Crédits Copilot à 0,01 $ l’unité (l. 54) | non relu le 10 novembre (la page française dit « à l’usage », sans montant) ; confirmé dans r1 le 9 novembre | microsoft.com/fr-fr, 10 novembre 2026 ; r1, vérification du 9 novembre |
| 18 | Managed Agents : 300 créations et 1 200 lectures par minute (l. 59) | confirmé | platform.claude.com/docs/en/api/rate-limits, 10 novembre 2026 |

Non relus, donc non vérifiés : Fable dans Pro et Max (l. 19-20) ; « model training opt-out by default » (l. 22) ; prix de ChatGPT en euros (l. 33) ; ChatGPT Pro en trois niveaux et ses quotas (l. 34) ; limites de Codex (l. 35, 60) ; engagements d’OpenAI et de Mistral sur les données (l. 36, 49) ; Microsoft 365 Premium (l. 55) ; Cursor et GitHub Copilot (l. 61).

### Corrections à appliquer

1. **Cache (l. 81).** Faux : « lecture à environ 5 % du prix d’entrée chez Anthropic ». Juste : « Chez Anthropic, la lecture en cache coûte de 2,5 % (Fable 5.2 : 0,20 $ pour 8 $) à 10 % (Haiku 5.5 : 0,01 $ pour 0,10 $) du prix d’entrée ; 5 % pour Opus 5.5 et Sonnet 5.5. L’écriture en cache coûte 1,25 fois le prix d’entrée (5 $ pour Opus 5.5). » Source : claude.com/pricing, 10 novembre 2026.
2. **Débit (l. 93).** Faux : « Le débit machine n’est jamais le goulet : la relecture humaine l’est. » Juste : « Au niveau Start, le plafond de dépense de 500 $ par mois arrête l’API après environ 12 500 devis lus par Opus 5.5 (0,04 $ chacun), soit une demi-heure au débit maximal ; une nouvelle organisation peut démarrer au niveau Evaluation, plus bas. Le premier frein est donc le plafond de dépense, qui se relève en changeant de niveau ; ensuite vient la relecture humaine. » Calcul : 500 / 0,04 = 12 500 ; 12 500 / 400 par minute ≈ 31 minutes. Source : platform.claude.com/docs/en/api/rate-limits, 10 novembre 2026.
3. **Enterprise (l. 24).** Faux : « Pour cinq personnes, Enterprise n’est donc pas accessible en libre-service. » Juste : « Pour cinq personnes, Enterprise en libre-service oblige à payer 20 places au minimum, soit 400 $ hors taxes par mois, plus l’usage au tarif de l’API. » Source : claude.com/pricing, 10 novembre 2026.
4. **Google AI (l. 40).** Faux : « AI Pro inclut un accès élargi à l’outil de programmation Antigravity et 10 $ de crédits Google Cloud par mois ; Ultra 5x : 40 $ ; Ultra 20x : 100 $ ». Juste : « AI Pro donne des « limites de débit de base » dans Antigravity ; Ultra 5x, des limites plus hautes ; Ultra 20x, les plus hautes. Les crédits Google Cloud ne figurent pas sur la page française du 10 novembre 2026 (non vérifié). » Source : gemini.google/fr/subscriptions.
5. **Workspace (l. 42).** Faux : « lieu de traitement garanti seulement sur l’offre la plus haute ». Juste : « Sur la page des tarifs, les « régions de données » ne figurent que dans les éditions Enterprise ; Business Starter, Standard et Plus n’en ont pas. » Source : workspace.google.com/intl/fr/pricing, 10 novembre 2026.
6. **Google AI, taxes (l. 40).** Faux : « Ces prix grand public sont toutes taxes comprises » présenté comme acquis. Juste : « La page officielle ne dit pas si la TVA est comprise ; une source tierce l’affirme (nextstart.ai, 31 octobre 2026). » Source : gemini.google/fr/subscriptions, 10 novembre 2026.
7. **Microsoft (l. 53).** Incomplet. Ajouter : « La promotion à 15,60 € HT est réservée aux clients Microsoft 365 Business existants, en abonnement annuel, la première année. » Source : microsoft.com/fr-fr/microsoft-365-copilot/pricing, 10 novembre 2026.
8. **Ultra (l. 21).** Faux par excès de précision : « Pas de limite de cinq heures pour les comptes vérifiés. » Juste : « Pas de limite de cinq heures (la condition du renvoi de bas de page n’a pas été lue). » Source : claude.com/pricing, 10 novembre 2026.
9. **Prix OpenAI (l. 76-78).** Ajouter : « prix du contexte court, jusqu’à 272 000 unités en entrée ». Source : developers.openai.com/api/docs/pricing, 10 novembre 2026.
10. **Renvois (l. 62 et 93).** Faux : « voir § 9 ». Juste : « voir la note `audit/2026-11-10-preparation-des-livrables/travaux/k13f-mesurer-les-gains-cent-fois-plus.md` » (la note k13c n’a pas de § 9).

### Sûr à reprendre

Phrases exactes, avec leur destination. Une phrase « interne seulement » ne va dans aucun document client.

**Document client (page A4 ou diapositive), source en note :**

1. « Chez Anthropic, une place d’équipe coûte 20 $ hors taxes par personne et par mois en paiement annuel, 25 $ en paiement mensuel ; une place renforcée coûte 100 $, ou 125 $ en mensuel (claude.com/pricing, tarif public relevé le 10 novembre 2026). »
2. « Dans les offres d’équipe d’Anthropic, vos contenus ne servent pas, par défaut, à entraîner les modèles (claude.com/pricing, 10 novembre 2026). »
3. « Depuis le 2 août 2026, une personne doit savoir qu’elle échange avec un système d’IA, et un trucage réaliste créé par IA doit être signalé par celui qui le diffuse (règlement européen sur l’IA, article 50) ; à faire valider par vos professionnels. » Source : r1 § 8.3, confirmé le 9 novembre 2026.

**Annexe client (comparaisons et calculs), tarifs publics avec source et date :**

4. « Prix publics de l’API d’Anthropic, par million de jetons, hors taxes : Claude Opus 5.5, 4 $ en entrée et 20 $ en sortie ; Claude Sonnet 5.5, 2 $ et 10 $ ; Claude Haiku 5.5, 0,10 $ et 0,50 $ (claude.com/pricing, 10 novembre 2026). »
5. « Le traitement par lots coûte deux fois moins cher chez Anthropic et chez Mistral (pages de tarifs, 10 novembre 2026). »
6. « Au premier niveau d’usage de l’API d’Anthropic, Claude Opus 5.5 accepte au plus 4 000 requêtes par minute, avec un plafond de dépense de 500 $ par mois ; ce sont des plafonds, pas des engagements de l’éditeur (platform.claude.com, page « Rate limits », 10 novembre 2026). »
7. « Lire un devis de trois pages coûterait environ 0,04 $ avec Claude Opus 5.5 et 0,02 $ avec Claude Sonnet 5.5 (hypothèse : 5 000 jetons lus et 1 000 produits ; estimation à valider pendant l’essai). »
8. « Microsoft 365 Copilot Business : 18,20 € hors taxes par utilisateur et par mois en engagement annuel (microsoft.com/fr-fr, 10 novembre 2026). »
9. « n8n, outil d’enchaînements automatiques : 20 € ou 50 € par mois en paiement annuel ; données hébergées à Francfort (n8n.io/pricing, 10 novembre 2026 ; taxes non précisées). »
10. « Transcription automatique : de 0,003 $ à 0,006 $ la minute chez OpenAI (tarif public, 10 novembre 2026). »

**Interne seulement :**

11. ChatGPT Business coûte comme Claude Team (20 $ / 25 $ ; 100 $ / 125 $), deux places au minimum, Premium sans limite de cinq heures (page d’aide vue par moteur de recherche, non ouverte).
12. Les offres individuelles d’Anthropic (Pro, Max, Ultra) n’ont ni SSO ni journal d’audit ; pour des données de client, préférer Team ou l’API (claude.com/pricing, 10 novembre 2026 ; conditions professionnelles : rj-R4, non revérifié).
13. Corrections 2 et 3, et les budgets de C3 (estimations).
14. Prix de Google AI en France (comptes personnels, à éviter pour des données de client).

### Ce qui reste inconnu

- Les abonnements que Marwin Tech paie aujourd’hui et leur coût (U27).
- Les prix en euros hors taxes de Claude et de ChatGPT ; aucun taux de change appliqué.
- TVA comprise ou non : Google AI, n8n, Zapier, ChatGPT Business.
- Prix de Make ; hébergement de Zapier et de Make ; prix des agents ElevenLabs à la minute ; prix d’Azure Document Intelligence et de Google Document AI ; prix de Veo.
- Droits sur les contenus générés (conditions d’OpenAI illisibles le 10 novembre).
- Inscription d’Anthropic et d’OpenAI au Data Privacy Framework.
- Conditions d’Ultra (« comptes vérifiés »), accès prioritaire de Max, condition des 500 $ de crédits de Team.
- Limites de Codex ; ChatGPT Pro ; Cursor ; GitHub Copilot ; Microsoft 365 Premium.
- Publication de l’omnibus sur l’IA au Journal officiel.
- Traitement en Europe : la documentation d’Anthropic ne propose que « global » ou « États-Unis » ; lieu par défaut chez Mistral non lu.
