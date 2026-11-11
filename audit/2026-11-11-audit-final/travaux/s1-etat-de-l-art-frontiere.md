# S1 — État de l’art à la frontière : où va l’IA en 2026, 2027, 2028 et 2030
Document interne — ne pas transmettre à GianLuca Carlone · 11 novembre 2026

Note de chercheur pour le catalogue « State Of The Art ». Vingt-neuf recherches et lectures le 11 novembre 2026. « Lue » : page ouverte ce jour. « Vue » : résultat de recherche seulement, à relire avant de citer. « Dépôt » : vérifié dans un travail antérieur, non relu ce jour (r3 : `audit/2026-11-09-audit-presentation-et-offre/travaux/r3-avenir-1-a-5-ans.md` ; k13a : `audit/2026-11-10-preparation-des-livrables/travaux/k13a-materiel-calcul-local.md` ; direction : `s1-etat-de-l-art-direction.md`). Niveau de preuve : **mesuré**, **annoncé** (par celui qui vend ou publie), **supposé** (notre lecture). Les sources sont numérotées [F1] à [F20] au § 7.

## 1. En bref

1. **Les agents tiennent une journée de travail, en logiciel.** METR mesure au moins seize heures d’expert réussies une fois sur deux, et dit ne plus savoir mesurer au-delà [F1, F2]. Ce n’est pas encore du travail de bureau.
2. **Image, vidéo, voix et mondes simulés se rejoignent.** Vidéo faite et retouchée par la conversation [F7] ; mondes explorables avec son et dialogues, en préversion [F8] ; voix traduite qui garde le ton, dont le français, depuis janvier 2026 [F10].
3. **Les objets suivent, inégalement.** Lunettes à écran vendues en France depuis le 13 octobre 2026 [F12] ; machine d’IA de bureau de 128 Go à environ 5 500 à 7 500 € HT (dépôt k13a) ; humanoïdes achetables, mais aucune livraison domestique vérifiée [F14].
4. **2027 à 2030 : des dates d’éditeurs, des médianes d’observateurs.** OpenAI vise un chercheur en IA automatisé en mars 2028 (dépôt r3). Des prévisionnistes indépendants placent un « programmeur automatisé » entre fin 2027 et 2030, avec une grande incertitude [F17]. Le déploiement suit les capacités avec retard [F18].
5. **Pour GianLuca Carlone :** la pointe se propose en expériences signées avec des artistes, et en outils pour son équipe. Chaque idée s’essaie sur ses lieux avant d’être promise.

## 2. Ce qui se fait de mieux aujourd’hui

Quinze réalisations. Pour chacune : qui, quoi, résultat publié, source, date.

1. **METR (laboratoire indépendant) — durée des tâches menées seules.** Claude Mythos Preview réussit une fois sur deux des tâches d’au moins 16 heures d’expert (intervalle de 8,5 à 55 heures). Cinq tâches seulement sur 228 dépassent 16 heures : la mesure devient « instable ». **Mesuré.** [F2, lue, 10 mai 2026] La page de METR ajoute : au-dessus de 16 heures, mesure non fiable ; la durée mesure la difficulté, pas le temps qu’une IA travaille ; elle « ne veut pas dire » qu’une IA automatise une journée de travail. Page « plus mise à jour activement » depuis le 8 septembre 2026. [F1, lue]
2. **METR — à 80 % de réussite.** Sur la période du 16 février au 16 mars 2026 : 12 heures réussies une fois sur deux, 1 h 30 quatre fois sur cinq. **Mesuré.** (dépôt r3, rapport METR du 19 mai 2026)
3. **METR et Anthropic — l’IA accélère la recherche en IA.** Les chiffres internes d’Anthropic impliquent une accélération d’environ 1,97 fois ; METR l’encadre entre 1,3 et 2,8. METR juge « plausible » que le seuil de deux fois ait été franchi au 15 juillet 2026. Anthropic emploie toujours ses chercheurs. **Mesuré, avec une forte incertitude.** [F5, lue, 5 novembre 2026]
4. **METR — Claude Opus 5.5.** Évaluation de dix jours ouvrés : le modèle accélère les chercheurs mais est « peu susceptible » d’automatiser entièrement leur travail ; pas de gain net de « jugement ». **Mesuré.** [F4, lue, 22 septembre 2026]
5. **Classements des modèles, novembre 2026.** Des tableaux composites placent en tête Claude Fable 5.2, Gemini 4 Carbon, Claude Opus 5.5 et GPT-6 Astra. Scores déclarés par les éditeurs, contradictoires d’une page à l’autre ; aucune page d’éditeur lue pour Fable 5.2. **Annoncé.** [F6, vues] Ne rien citer au client.
6. **Google — Gemini Omni Flash.** Fait et retouche une vidéo à partir de texte, d’images, de sons ou de vidéos, par conversation. Clips de 10 secondes au lancement. Filigrane invisible SynthID sur chaque vidéo. Avatar enregistré avec sa propre voix. Ouvert aux abonnés le 20 mai 2026. **Disponible.** [F7, lue, 20 mai 2026]
7. **Google DeepMind — Genie 4.** Monde simulé interactif : son ambiant, musique et dialogues générés à la volée ; on change la caméra, la météo ou les personnages par la parole. Ni résolution ni durée publiées. Testeurs choisis ; abonnés Ultra « bientôt ». **Annoncé.** [F8, lue, 27 octobre 2026]
8. **World Labs — Marble 1.1.** Un monde 3D persistant, à partir d’un texte, d’une image ou d’une vidéo. Par l’interface de programmation : environ 1,20 à 2,48 $ par monde ; export en nuage de points sans frais ; maillage texturé (GLB) à 2,80 $. Création à partir de ses propres prises de vue ouverte en bêta le 30 octobre 2026 (vue). **Disponible.** [F9, lue, page non datée, coûts observés jusqu’au 25 juin 2026]
9. **Google — traduction de la parole dans Meet.** Une voix traduite, doublée sur l’originale, qui imite le ton et la cadence de la personne. Anglais ↔ espagnol, français, allemand, portugais ou italien ; une seule paire par réunion. Ouvert à tous les clients éligibles le 27 janvier 2026 ; sur téléphone depuis avril (vue). **Disponible.** [F10, lue, 4 février 2026]
10. **Google — Gemini 3.5 Live Translate.** Plus de 70 langues, détection automatique, voix qui garde intonation et rythme, « quelques secondes » de décalage. Interface de programmation en préversion publique ; Meet en préversion privée ; application Traduction avec n’importe quel casque. Qualité affirmée par Google, sans mesure indépendante. **Annoncé.** [F11, lue, 10 juin 2026, source secondaire de l’annonce du 9 juin]
11. **Meta — Ray-Ban Display en France.** Lunettes avec un petit écran couleur dans le verre et un bracelet qui lit les gestes des doigts. 899 € en France, vente le 13 octobre 2026, boutique à Paris. Limites : sous-titres en direct en anglais seulement au 24 septembre ; 6 heures d’autonomie annoncées ; navigation à pied non annoncée en France. **Disponible.** [F12, lue, 26 septembre 2026]
12. **Samsung et Google — lunettes Android XR.** Faites avec Gentle Monster et Warby Parker ; traduction dite à l’oreille, sans écran. Précommandes le 12 novembre 2026 selon Warby Parker ; aucun prix ; Europe non annoncée. **Annoncé.** [F13, vues]
13. **NVIDIA — calcul sur place.** DGX Spark (128 Go) : environ 5 500 à 7 500 € HT en France autour du 10 novembre 2026 ; prix plus que doublé en un an. DGX Station (GB300, 748 Go) : environ 90 000 à 171 500 € HT chez des revendeurs européens, 1 600 W. **Disponible.** (dépôt k13a, lu le 10 novembre 2026) Disponibilité générale chez Supermicro annoncée au Computex 2026 [F16, vue].
14. **Humanoïdes — l’état réel du marché.** Unitree R1 commandable dès 4 900 $ ; 1X NEO à 20 000 $ ou 499 $ par mois, États-Unis seulement, aucune livraison vérifiée hors du programme de l’éditeur à la mi-octobre 2026. Les premiers robots peuvent être aidés par des opérateurs à distance : « supposez qu’un humain est dans la boucle ». Tesla : clients externes « vers fin 2027 », selon son patron. **Mesuré (état des offres).** [F14, lue, 1er novembre 2026] En Europe, onze modèles de 9 000 à 94 600 €, pour la recherche et l’enseignement (dépôt r3, heise, 3 novembre 2026).
15. **Pollen Robotics (Hugging Face) — Reachy Mini.** Petit robot de bureau expressif, à programmer, en logiciel ouvert ; 299 $ ou 449 $ (vue, 2025). Délai jusqu’à 90 jours ; expédié de Shenzhen ; envois européens en cours de transfert vers un entrepôt français. **Disponible.** [F15, lue, 29 octobre 2026]

**Ce qu’il faut retenir.** La pointe mesurée est en logiciel. Pour l’image, la vidéo et la voix, on a des produits ouverts au public, mais leurs qualités sont surtout déclarées par les éditeurs. Pour les objets, l’écart est grand entre l’annonce et la livraison.

## 3. Ce qui arrive en 2027, 2028, 2030

Chaque ligne porte son niveau de preuve. Une date d’éditeur est un objectif, pas un engagement.

**Fin 2026**
- Lunettes Android XR en vente dans quelques pays ; Europe non annoncée. **Annoncé.** [F13]
- Genie 4 pour les abonnés Ultra ; traduction en 70 langues dans Meet « plus tard cette année ». **Annoncé.** [F8, F11]

**2027**
- 20 janvier : règlement européen sur les machines applicable ; 2 décembre : règles des IA « à haut risque ». **Texte publié.** (dépôt r3)
- « IA puissante » à la fin de 2026 ou au début de 2027 : prévision d’Anthropic, écrite en mars 2025, non reconfirmée depuis dans ce que nous avons lu. Un chercheur indépendant lui donnait environ 6 % de chances. **Annoncé.** [F19, vues]
- Programmeur automatisé, médiane de novembre 2027 pour Daniel Kokotajlo (AI Futures Project). **Prévision indépendante.** [F17]
- Humanoïde Tesla livré à des clients externes « vers fin 2027 ». **Annoncé.** [F14]

**2028**
- Mars : « chercheur en IA automatisé », supervisé, objectif d’OpenAI. **Annoncé.** (dépôt r3)
- 2 août : règles européennes des produits intégrant une IA. **Texte publié.** (dépôt r3)
- Superintelligence, médiane de mars 2029 pour Daniel Kokotajlo. **Prévision indépendante, très incertaine.** [F17]

**2030**
- Programmeur automatisé, médiane de janvier 2030 pour Eli Lifland ; mais une chance sur dix que ce soit après 2070. **Prévision indépendante.** [F17]
- Epoch AI : centres de calcul à plus de 100 milliards de dollars ; IA qui corrige et écrit seule du logiciel bien défini ; assistants de recherche dans de nombreuses sciences ; 10 à 20 % de productivité gagnée par tâche, « à terme » ; déploiement en retard sur les capacités. **Prévision indépendante** (septembre 2025, gardée : seule projection indépendante détaillée à 2030 trouvée). [F18]
- IA générale à cinq ou dix ans, selon le patron de Google DeepMind. **Annoncé.** (dépôt r3)

**Notre lecture (supposé).** Si la durée mesurée par METR continue de doubler tous les quatre à sept mois, des tâches de logiciel de plusieurs jours seront menées seules en 2027-2028. La vidéo passera de clips de secondes à des scènes de minutes. La traduction de la voix arrivera dans les lunettes, en français, vers 2027. Un humanoïde qui travaille seul près du public en Europe : pas avant 2030. Aucune de ces dates n’est mesurée.

## 4. Vingt idées pour GianLuca Carlone

Format : l’idée — ce qu’il verrait — ce qu’il faut — quand. Partout : artistes et spécialistes exécutent, nous concevons et orchestrons, son équipe décide.

1. **Le vernissage sans barrière de langue** — un collectionneur italien parle, l’artiste l’entend en français, avec sa voix — casques, traduction de Meet, essai sur cinq langues — 2027.
2. **La visite à distance traduite** — un acheteur allemand visite la galerie en visioconférence, chacun dans sa langue — compte d’entreprise, accord des participants — 2027.
3. **Le double 3D de chaque exposition** — une salle explorable en ligne pour les collectionneurs absents — prises de vue, accord des artistes — 2027.
4. **L’accrochage essayé avant** — déplacer les œuvres dans le double 3D de la galerie avant de toucher un clou — vidéo de la salle, régisseur — 2027.
5. **Le décor vivant du cabaret** — un monde simulé, piloté à la voix, en fond de scène — artiste vidéo, régisseur, essai sur un numéro — 2028.
6. **Le court film de chaque œuvre** — une vidéo tirée des photos de l’œuvre, signalée comme générée — accord de l’artiste, mention obligatoire — 2027.
7. **La voix de l’artiste dans vingt langues** — son commentaire, dans sa voix, pour chaque visiteur — consentement écrit, outil de traduction vocale — 2028.
8. **Le cartel qui parle** — sous-titres et traduction près de l’œuvre, sur téléphone puis lunettes — textes préparés ; lunettes quand le français arrive — 2028.
9. **L’agent de nuit du marchand** — le matin, le dossier de provenance d’un lot et les ventes comparables — sources désignées, une personne valide — 2027.
10. **La machine de la maison** — une station d’IA de bureau pour les archives confidentielles de la galerie — sécurité tenue, décision après le cadrage — 2027.
11. **Le concierge de vos neuf suites, en plusieurs langues** — un assistant vocal qui dit qu’il est une IA et passe la main — logiciel du marché, règles écrites — 2027.
12. **Le petit robot hôte** — un robot de bureau expressif présente une œuvre au vernissage, une personne à côté — 90 jours de délai, programme écrit — 2027.
13. **La résidence « artistes et machines »** — un artiste invité crée avec un bras robotisé, la vidéo générée et un monde simulé ; on expose l’œuvre et sa fabrication — artiste, intégrateur, assurance — 2027-2028.
14. **L’humanoïde d’un soir** — loué avec son pilote pour l’ouverture du cabaret — prestataire assuré, distance avec le public — à l’ouverture.
15. **Le catalogue vivant de la galerie** — chaque œuvre vendue : dossier, double 3D, court film — inventaire, droits de reproduction — 2028.
16. **Le spectacle bilingue** — surtitres préparés, puis voix traduite en essai pour un public étranger — textes fixés, régie — 2028.
17. **Les vitrines qui changent avec les saisons** — vidéos générées à partir des produits des commerces — accord des commerçants — 2027.
18. **L’observatoire « State Of The Art »** — chaque trimestre, ce qui devient possible, essayé sur ses lieux — veille datée, une rencontre publique dans la Nièvre — dès 2027.
19. **La salle d’essai** — une pièce où les visiteurs essaient lunettes, traduction et mondes 3D — matériel loué, médiateur — 2028.
20. **L’équipe d’agents de 2030** — son administratrice confie dossiers, réservations et billetterie à des agents qu’elle dirige à la voix — supposé — 2030.
