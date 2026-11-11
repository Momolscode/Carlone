# S1 — État de l’art à la frontière : où va l’IA en 2026, 2027, 2028 et 2030
Document interne — ne pas transmettre à GianLuca Carlone · 11 novembre 2026

Note de chercheur pour le catalogue « State Of The Art ». Vingt-neuf recherches et lectures le 11 novembre 2026. « Lue » : page ouverte ce jour. « Vue » : résultat de recherche, à relire avant de citer. « Dépôt » : vérifié dans un travail antérieur, non relu (chemins au § 7). Preuve : **mesuré**, **annoncé** (par qui vend ou publie), **supposé** (notre lecture).

## 1. En bref

1. **Les agents tiennent une journée de travail, en logiciel.** METR mesure au moins seize heures d’expert réussies une fois sur deux ; il ne sait plus mesurer au-delà [F1, F2]. Pas encore du travail de bureau.
2. **Image, vidéo, voix et mondes simulés se rejoignent.** Vidéo retouchée par la conversation [F7] ; mondes explorables avec son et dialogues, en préversion [F8] ; voix traduite qui garde le ton, français compris [F10].
3. **Les objets suivent, inégalement.** Lunettes à écran vendues en France depuis le 13 octobre 2026 [F12] ; machine d’IA de bureau de 128 Go à environ 5 500 à 7 500 € HT (dépôt k13a) ; humanoïdes achetables, mais aucune livraison domestique vérifiée [F14].
4. **2027 à 2030 : des dates d’éditeurs, des médianes d’observateurs.** OpenAI vise un chercheur en IA automatisé en mars 2028 (dépôt r3). Des prévisionnistes indépendants placent un « programmeur automatisé » entre fin 2027 et 2030, avec une grande incertitude [F17]. Le déploiement suit les capacités avec retard [F18].
5. **Pour GianLuca Carlone :** la pointe se propose en expériences signées avec des artistes, et en outils pour son équipe. Chaque idée s’essaie sur ses lieux avant d’être promise.

## 2. Ce qui se fait de mieux aujourd’hui

Douze réalisations : qui, quoi, résultat publié, source, date.

1. **METR (laboratoire indépendant) — durée des tâches menées seules.** Claude Mythos Preview réussit une fois sur deux des tâches d’au moins 16 heures d’expert (intervalle de 8,5 à 55 heures). Cinq tâches sur 228 seulement dépassent 16 heures : mesure « instable ». Cette durée dit la difficulté, pas le temps de travail sans aide ; la page n’est plus mise à jour depuis le 8 septembre 2026. À quatre réussites sur cinq : 1 h 30 en mars 2026 (dépôt r3). **Mesuré.** [F2, lue, 10 mai 2026 ; F1, lue]
2. **METR — l’IA accélère la recherche en IA.** Chez Anthropic, environ 1,97 fois, calculé par METR sur les chiffres internes (fourchette de METR : de 1,3 à 2,8) ; seuil de deux fois « plausiblement » franchi au 15 juillet 2026. Claude Opus 5.5 reste « peu susceptible » d’automatiser entièrement le travail des chercheurs. **Mesuré, très incertain.** [F5, lue, 5 novembre 2026 ; F4, lue, 22 septembre 2026]
3. **Google — Gemini Omni Flash.** Vidéo faite et retouchée par la conversation, à partir de texte, d’images, de sons ou de vidéos. Clips de 10 secondes au lancement ; filigrane invisible SynthID ; avatar enregistré avec sa propre voix. **Disponible** pour les abonnés. [F7, lue, 20 mai 2026]
4. **Google DeepMind — Genie 4.** Monde simulé interactif, avec son, musique et dialogues générés à la volée ; caméra, météo et personnages changés par la parole. Aucun chiffre publié ; testeurs choisis. **Annoncé.** [F8, lue, 27 octobre 2026]
5. **World Labs — Marble 1.1.** Monde 3D persistant, à partir d’un texte, d’une image ou d’une vidéo : de 1,20 à 2,48 $ par monde ; maillage GLB à 2,80 $. **Disponible.** [F9, lue, page non datée]
6. **Google Meet — voix traduite.** Doublage qui imite le ton et la cadence de la personne. Anglais ↔ français, espagnol, allemand, italien ou portugais ; une paire par réunion. Ouvert le 27 janvier 2026. **Disponible.** [F10, lue, 4 février 2026]
7. **Google — Gemini 3.5 Live Translate.** Plus de 70 langues, détection automatique, intonation gardée, « quelques secondes » de décalage. Préversion ; qualité affirmée par Google, sans mesure indépendante. **Annoncé.** [F11, lue, 10 juin 2026]
8. **Meta — Ray-Ban Display.** Écran couleur dans le verre, bracelet qui lit les gestes des doigts. 899 € en France depuis le 13 octobre 2026. Sous-titres en direct en anglais seulement ; 6 heures d’autonomie annoncées. **Disponible.** [F12, lue, 26 septembre 2026]
9. **Samsung et Google — lunettes Android XR.** Sans écran, traduction à l’oreille ; précommandes annoncées au 12 novembre 2026 ; ni prix ni date pour l’Europe. **Annoncé.** [F13, vues]
10. **NVIDIA — calcul sur place.** DGX Spark (128 Go) : de 5 500 à 7 500 € HT en France ; prix plus que doublé en un an. DGX Station (748 Go) : de 90 000 à 171 500 € HT chez des revendeurs européens, 1 600 W. **Disponible.** (dépôt k13a, 10 novembre 2026 ; [F16, vues])
11. **Humanoïdes — l’état réel du marché.** Unitree R1 dès 4 900 $ ; 1X NEO à 20 000 $ ou 499 $ par mois, États-Unis seulement, aucune livraison vérifiée à la mi-octobre 2026 ; « supposez qu’un humain est dans la boucle » (opérateurs à distance). En Europe, onze modèles de 9 000 à 94 600 €, pour la recherche (dépôt r3). **Mesuré (état des offres).** [F14, lue, 1er novembre 2026]
12. **Pollen Robotics (Hugging Face) — Reachy Mini.** Petit robot de bureau expressif, en logiciel ouvert ; 299 ou 449 $ (vue). Délai jusqu’à 90 jours ; envois européens en cours de transfert vers un entrepôt français. **Disponible.** [F15, lue, 29 octobre 2026]

**À retenir.** La pointe mesurée est en logiciel. Image, vidéo et voix : produits ouverts, qualités surtout déclarées. Objets : grand écart entre annonce et livraison.

## 3. Ce qui arrive en 2027, 2028, 2030

Une date d’éditeur est un objectif, pas un engagement.

**Fin 2026**
- Lunettes Android XR en vente dans quelques pays ; Europe non annoncée. **Annoncé.** [F13]
- Genie 4 pour les abonnés Ultra ; traduction en 70 langues dans Meet « plus tard cette année ». **Annoncé.** [F8, F11]

**2027**
- 20 janvier : règlement européen sur les machines applicable ; 2 décembre : règles des IA « à haut risque ». **Texte publié.** (dépôt r3)
- « IA puissante » fin 2026 ou début 2027 : prévision d’Anthropic de mars 2025, non reconfirmée dans nos lectures ; un chercheur indépendant lui donnait environ 6 % de chances. **Annoncé.** [F19, vues]
- Programmeur automatisé, médiane de novembre 2027 pour Daniel Kokotajlo (AI Futures Project). **Prévision indépendante.** [F17]
- Humanoïde Tesla livré à des clients externes « vers fin 2027 ». **Annoncé.** [F14]

**2028**
- Mars : « chercheur en IA automatisé », supervisé, objectif d’OpenAI. **Annoncé.** (dépôt r3)
- 2 août : règles européennes des produits intégrant une IA. **Texte publié.** (dépôt r3)
- Superintelligence, médiane de mars 2029 pour Daniel Kokotajlo. **Prévision indépendante, très incertaine.** [F17]

**2030**
- Programmeur automatisé, médiane de janvier 2030 pour Eli Lifland ; mais une chance sur dix que ce soit après 2070. **Prévision indépendante.** [F17]
- Epoch AI : centres de calcul à plus de 100 milliards de dollars ; IA qui écrit seule du logiciel bien défini ; assistants de recherche dans de nombreuses sciences ; 10 à 20 % gagnés par tâche, « à terme » ; déploiement en retard. **Prévision indépendante** (septembre 2025, gardée : seule projection indépendante détaillée à 2030 trouvée). [F18]
- IA générale à cinq ou dix ans, selon le patron de Google DeepMind. **Annoncé.** (dépôt r3)

**Notre lecture (supposé, rien de mesuré).** Si la durée mesurée par METR double encore tous les quatre à sept mois : tâches de logiciel de plusieurs jours en 2027-2028. Vidéo : de clips de secondes à des scènes de minutes. Voix traduite en français dans les lunettes vers 2027. Humanoïde autonome près du public en Europe : pas avant 2030.

## 4. Vingt idées pour GianLuca Carlone

L’idée — ce qu’il verrait — ce qu’il faut — quand. Nous concevons ; artistes et spécialistes exécutent ; son équipe décide.

1. **Le vernissage sans barrière de langue** — un collectionneur italien parle, l’artiste l’entend en français, avec sa voix — casques, application de traduction vocale, essai sur cinq langues — 2027.
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
13. **La résidence « artistes et machines »** — un artiste invité crée avec un bras robotisé et un monde simulé ; on expose l’œuvre et sa fabrication — artiste, intégrateur, assurance — 2027-2028.
14. **L’humanoïde d’un soir** — loué avec son pilote pour l’ouverture du cabaret — prestataire assuré, distance avec le public — à l’ouverture.
15. **Le catalogue vivant de la galerie** — chaque œuvre vendue : dossier, double 3D, court film — inventaire, droits de reproduction — 2028.
16. **Le spectacle bilingue** — surtitres préparés, puis voix traduite en essai pour un public étranger — textes fixés, régie — 2028.
17. **Les vitrines qui changent avec les saisons** — vidéos générées à partir des produits des commerces — accord des commerçants — 2027.
18. **L’observatoire « State Of The Art »** — chaque trimestre, ce qui devient possible, essayé sur ses lieux — veille datée, rencontre publique dans la Nièvre — dès 2027.
19. **La salle d’essai** — une pièce où les visiteurs essaient lunettes, traduction et mondes 3D — matériel loué, médiateur — 2028.
20. **L’équipe d’agents de 2030** — son administratrice confie dossiers, réservations et billetterie à des agents qu’elle dirige à la voix — supposé — 2030.

## 5. Faits citables dans un document client

Sources lues le 11 novembre 2026. Ni prix, ni superlatif.

1. « Le laboratoire indépendant METR estime qu’un modèle d’IA testé au printemps 2026 réussit, une fois sur deux, des tâches de logiciel qui prennent au moins seize heures à un expert. Il précise qu’il ne sait plus mesurer au-delà. » METR, 8 septembre 2026 ; The Decoder, 10 mai 2026 [F1, F2].
2. « Depuis janvier 2026, Google Meet traduit la parole entre l’anglais et le français, l’espagnol, l’allemand, l’italien ou le portugais, avec une voix qui imite le ton de la personne. Une paire de langues par réunion. » Google, 4 février 2026 [F10].
3. « En juin 2026, Google a ouvert en préversion une traduction de la voix dans plus de soixante-dix langues, qui garde l’intonation et suit à quelques secondes. » Annonce du 9 juin 2026, rapportée le 10 juin [F11].
4. « Depuis mai 2026, un outil de Google fait et retouche de courtes vidéos par la conversation, à partir de textes, d’images ou de sons. Chaque vidéo porte un filigrane invisible. » The Next Web, 20 mai 2026 [F7].
5. « Le 27 octobre 2026, Google DeepMind a présenté un modèle qui crée des mondes explorables, avec leurs sons et des personnages qui parlent, pilotés par la voix. Il est réservé à des testeurs. » Google, 27 octobre 2026 [F8].
6. « Des lunettes avec un petit écran dans le verre sont vendues en France depuis le 13 octobre 2026. Fin septembre, leurs sous-titres en direct ne fonctionnaient qu’en anglais. » Selectra, 26 septembre 2026 [F12].
7. « À la mi-octobre 2026, aucune livraison d’un robot humanoïde domestique à un client payant n’était vérifiée de façon indépendante. Les premiers modèles peuvent être aidés par des opérateurs à distance. » Humanoids for Home, 1er novembre 2026 [F14].
8. « Selon METR, dans un grand laboratoire, l’IA rendrait déjà les progrès de la recherche en IA environ deux fois plus rapides, avec une forte incertitude ; ses chercheurs y travaillent toujours. » METR, 5 novembre 2026 [F5].
9. « Selon Epoch AI, d’ici 2030 l’IA pourrait écrire seule du logiciel bien défini ; le gain attendu est de 10 à 20 % par tâche, et le déploiement suivra avec retard. » Epoch AI, 16 septembre 2025 [F18].
10. « En août 2026, deux prévisionnistes indépendants situaient l’arrivée d’une IA capable de programmer seule, en date médiane, entre fin 2027 et début 2030, avec une très grande incertitude. » AI Futures Project, 16 août 2026 [F17].

## 6. Règles et limites

**Droit (à faire valider par ses professionnels).**
- Contenu généré qui peut passer pour vrai : à signaler depuis le 2 août 2026 ; dire à chacun qu’il parle à une IA (règlement européen sur l’IA, art. 50 ; dépôt r3).
- Voix et visage d’un artiste ou d’un client : consentement écrit, usage et durée précisés. Une œuvre filmée, scannée en 3D ou animée relève du droit de reproduction de son auteur.
- Traduire ou transcrire une conversation, c’est traiter des données personnelles : informer, limiter, effacer.
- Lunettes à caméra : interdites dans les suites, le sauna et le jacuzzi ; affichage clair ailleurs.
- Robot près du public : règlement européen sur les machines au 20 janvier 2027, norme ISO 10218-2:2025, déclaration de conformité et marquage CE ; ne jamais modifier une machine.
- Une œuvre ne se vend jamais comme un placement ; aucun conseil fiscal.

**Sécurité.** Un agent qui lit des pages ou des courriels peut être détourné par une instruction cachée (direction, § 6). Une machine sur place garde les données chez lui, mais sa sécurité devient notre affaire et la sienne (k13a). Un humanoïde aidé à distance, c’est une personne inconnue qui voit l’intérieur des lieux.

**Échecs et limites connus.** Mesure de METR limitée au logiciel, saturée à 16 heures, plus mise à jour [F1, F2] ; bancs d’essai saturés [F5] ; classements déclarés et contradictoires [F6]. Un outil peut disparaître : l’application Sora d’OpenAI aurait fermé le 26 avril 2026 (vue, à confirmer) [F20]. Clips de 10 secondes [F7] ; aucun chiffre pour Genie 4 [F8] ; sous-titres des lunettes en anglais seulement [F12]. Humanoïdes : aucune livraison domestique vérifiée [F14]. Prix du calcul instables (k13a). Selon Eli Lifland, une chance sur dix que le programmeur automatisé arrive après 2070 [F17].

## 7. Sources

Toutes consultées le 11 novembre 2026.

- [F1] METR, « Time Horizons », mise à jour du 8 septembre 2026, lue — https://metr.org/time-horizons/
- [F2] The Decoder, 10 mai 2026, lue — https://the-decoder.com/metr-says-it-can-barely-measure-claude-mythos-palo-alto-networks-warns-of-autonomous-ai-attackers/
- [F4] METR, évaluation de Claude Opus 5.5, 22 septembre 2026, lue — https://metr.org/blog/2026-09-22-claude-opus-5-5/
- [F5] METR, revue du rapport de risques d’Anthropic, 5 novembre 2026, lue — https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review/
- [F6] Classements, vues — https://benchlm.ai/frontier-ai-models ; https://officechai.com/ai/fable-5-2-benchmarks/
- [F7] The Next Web, 20 mai 2026, lue — https://thenextweb.com/news/google-gemini-omni-flash-video-model-io-2026
- [F8] Google, « Introducing Genie 4 », 27 octobre 2026, lue — https://blog.google/innovation-and-ai/models-and-research/google-deepmind/introducing-genie-4/
- [F9] World Labs, tarifs, non datée, lue — https://docs.worldlabs.ai/api/pricing.md
- [F10] Google Workspace Updates, 4 février 2026, lue — https://workspaceupdates.googleblog.com/2026/02/speech-translation-meet-ga.html ; téléphone, 8 avril 2026, vue — https://workspaceupdates.googleblog.com/2026/04/speech-translation-in-google-meet-is-now-rolling-out-to-mobile-devices.html
- [F11] PPC Land, 10 juin 2026, lue — https://ppc.land/googles-gemini-3-5-live-translate-lands-with-70-language-real-time-speech/
- [F12] Selectra, 26 septembre 2026, lue — https://selectra.info/telecom/actualites/marche/lunettes-meta-ray-ban-display-arrivent-en-france
- [F13] Lunettes Android XR, vues — https://www.thurrott.com/hardware/339507/samsung-details-upcoming-smart-glasses-developed-with-gentle-monster-and-warby-parker ; https://www.droid-life.com/2026/05/19/android-xr-launch-fall-2026/
- [F14] Humanoids for Home, 1er novembre 2026, lue — https://humanoidsforhome.com/guides/can-you-buy-a-humanoid-robot-today/
- [F15] Pollen Robotics, expédition, 29 octobre 2026, lue — https://store.pollen-robotics.com/policies/shipping-policy ; prix, vue — https://techcrunch.com/2025/07/09/hugging-face-opens-up-orders-for-its-reachy-mini-desktop-robots
- [F16] DGX Station, vues — https://www.servethehome.com/nvidia-dgx-station-systems-available-at-last-gb300-gb200-workstations-for-your-desktop ; https://learn-more.supermicro.com/data-center-stories/supermicro-super-ai-station-nvidia-gb300
- [F17] AI Futures Project, 16 août 2026, lue — https://blog.aifutures.org/p/q25-2026-timelines-update-uplift
- [F18] Epoch AI, 16 septembre 2025, lue — https://epoch.ai/blog/what-will-ai-look-like-in-2030
- [F19] Anthropic, mars 2025, vue — https://anthropic.com/news/anthropic-s-recommendations-ostp-u-s-ai-action-plan ; critique, vue — https://www.lesswrong.com/posts/gabPgK9e83QrmcvbK/what-s-up-with-anthropic-predicting-agi-by-early-2027-1
- [F20] Arrêt de Sora, vue (source secondaire) — https://www.vo3ai.com/blog/google-deepmind-teases-veo-4-days-after-openai-kills-sora-the-ai-video-power-vac-2026-03-30
- Dépôt, non relu : r3 = `audit/2026-11-09-audit-presentation-et-offre/travaux/r3-avenir-1-a-5-ans.md` (METR du 19 mai 2026, OpenAI, Google DeepMind, heise, règles européennes) ; k13a = `audit/2026-11-10-preparation-des-livrables/travaux/k13a-materiel-calcul-local.md` (prix NVIDIA) ; direction = `s1-etat-de-l-art-direction.md`.
