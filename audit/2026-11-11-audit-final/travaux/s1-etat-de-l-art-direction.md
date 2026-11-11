# État de l’art à la fin de 2026 — direction, administratif et agents d’IA
Document interne — ne pas transmettre à GianLuca Carlone · 11 novembre 2026

Note de chercheur pour le catalogue « State Of The Art ». Vingt-huit recherches et lectures le 11 novembre 2026. « Lue » : page ouverte ce jour. « Extrait » : long passage de la page d’origine rendu par le moteur. « Vue » : résumé du moteur seulement. Preuve : **mesuré**, **annoncé**, **prévu** (analyste) ou **supposé**. Repris sans refaire : produits et connecteurs (`audit/2026-11-09-audit-presentation-et-offre/travaux/r1-nouveautes-ia-automatisation-2026.md`, « r1 », lu le 9 novembre) ; études de gains (`k13f-mesurer-les-gains-cent-fois-plus.md`) ; droit du travail (`k4-administratrice-et-outils-ia.md`).

## 1. En bref

- **Les agents tiennent des heures.** Un laboratoire indépendant mesure qu’un modèle réussit une fois sur deux des tâches de seize heures d’expert, ou plus [S1, S3]. Trois grands éditeurs vendent un assistant qui prépare un dossier entier (r1).
- **Le réel reste loin des bancs d’essai.** Sur de vraies missions payées, le meilleur agent rend un travail acceptable dans 41 % des cas [S5]. En entreprise, l’usage d’agents à grande échelle reste sous 10 % par fonction [S11].
- **Les gains mesurés se comptent en minutes.** 19 minutes par jour dans un ministère britannique, surtout pour chercher et écrire [S9]. On gagne sur des tâches, pas sur un métier entier.
- **La prise commune existe.** Le protocole MCP relie assistants et logiciels ; il a une fondation et une règle de stabilité [S12]. Il ouvre aussi des portes aux attaquants [S21 à S23].
- **Pour une administratrice seule,** le travail passe de « faire » à « faire faire et vérifier ». Sa relecture devient le goulet. D’où : procédures écrites, droits minimaux, une personne qui décide.

## 2. Ce qui se fait de mieux aujourd’hui

1. **METR (laboratoire indépendant) — durée des tâches menées seules.** Un modèle testé en mars 2026 réussit une fois sur deux des tâches d’au moins 16 heures d’expert (intervalle de 8,5 à 55 heures). METR dit ne plus savoir mesurer au-delà ; ses tâches relèvent surtout du logiciel. En août 2025, le meilleur modèle était à 2 h 17. **Mesuré.** [S1, lue, mise à jour du 8 septembre 2026 ; S3, lue, 10 mai 2026]
2. **Anthropic — Claude Opus 5.5.** Un testeur a audité et corrigé un code de 200 000 lignes en moins de trois heures, contre plus de vingt avec le modèle précédent. Mais sur un banc de flux d’entreprise mené par Zapier, il réussit 40 % des cas (meilleur score publié : 41,4 %). **Annoncé** par l’éditeur. [S4, lue, 22 septembre 2026]
3. **Scale AI et Center for AI Safety — Remote Labor Index.** De vraies missions de travailleurs indépendants, jugées « acceptables par un client raisonnable ». Meilleur score : 2,5 % au lancement, fin 2025 ; 41,3 % affichés en novembre 2026, le suivant à 21,3 %. **Mesuré.** [S5, lue, page non datée]
4. **OpenAI — GDPval, 44 métiers.** Un modèle d’avril 2026 égale ou bat l’expert dans 84,9 % des comparaisons, selon l’éditeur. La mesure indépendante d’Artificial Analysis donne 68,3 % au meilleur modèle le 22 septembre 2026. Deux méthodes, écart non expliqué. **Annoncé.** [S6, vues]
5. **Anthropic — équipe d’agents.** Un agent chef et des sous-agents en parallèle font 90,2 % mieux qu’un agent seul sur des recherches internes. Coût : environ quinze fois le calcul d’une conversation. Gardé malgré sa date (2025) : seule mesure publique du coût de l’orchestration trouvée. **Mesuré** par l’éditeur. [S7, lue, 13 juin 2025]
6. **Anthropic et Andon Labs — Project Vend.** Un agent tient une boutique dans trois villes. Avec des outils (fichier clients, stocks, navigateur), des procédures et un agent « dirigeant », les semaines à perte disparaissent presque ; remises −80 % (extrait). L’éditeur le juge encore « vulnérable de bien des façons ». **Mesuré.** [S8, lue, 18 décembre 2025]
7. **Ministère britannique du Travail (DWP).** 3 549 agents, d’octobre 2024 à mars 2025, avec groupe de comparaison : 19 minutes gagnées par jour ; 26 pour chercher une information, 25 pour écrire des courriels. Déclaratif, sans tirage au sort. **Mesuré.** [S9, lue, 29 janvier 2026] L’essai interministériel sur 20 000 agents déclarait 26 minutes ; 17 % sans aucun gain [S10, extrait, 2 juin 2025].
8. **Stanford — AI Index 2026.** Réussite des agents sur des tâches réelles en ligne de commande : de 20 % à 77,3 % en un an. Sur un banc de bureautique, ils échouent encore une fois sur trois (extrait). Agents à grande échelle : moins de 10 % dans presque toutes les fonctions, selon l’enquête McKinsey 2025 (extrait). **Mesuré.** [S11, lue, 13 avril 2026]
9. **Fondation AAIF (Linux Foundation) — protocole MCP.** Version du 28 juillet 2026 : serveurs sans état, tâches longues reprises après une coupure, autorisations gérées par l’entreprise, douze mois de préavis avant tout retrait. Protocole confié à la fondation en décembre 2025. **Publié.** [S12, lue] Pennylane le propose en lecture seule ; Qonto prépare des virements à valider dans sa propre application (r1).
10. **Assistants qui préparent un travail entier.** Copilot Cowork (16 juin 2026), ChatGPT Work (9 juillet 2026), Claude Cowork (web et mobile le 7 juillet 2026 ; tâches programmées dans le nuage depuis le 6 octobre 2026). **Disponibles.** (r1, sources officielles lues le 9 novembre)
11. **Mémoire de l’entreprise.** Microsoft : base de connaissances d’équipe tenue par l’assistant, en préversion le 14 octobre 2026 ; réponses « jusqu’à 4 fois plus rapides » en test interne [S13, extrait]. Mémoire offerte aux agents annoncée pour décembre 2026 [S14, extrait]. Anthropic : une mémoire commune à la conversation et à Cowork, visible et modifiable ; active par défaut dans les nouvelles organisations d’équipe depuis le 31 octobre 2026 [S15, extrait]. **Annoncé.**
12. **État français — facture électronique.** Au 4 octobre 2026, 75 % des entreprises déclarant la TVA avaient choisi leur plateforme de réception ; plus de 20 millions de factures échangées. Difficultés : coût et lisibilité des offres, interopérabilité, statuts mal transmis, besoins des plus petites. Aucune sanction avant fin 2026. **Mesuré.** [S16, lue, 9 octobre 2026 ; S17, lue]
13. **Comptabilité et PME françaises.** Cas d’éditeurs et d’intégrateurs : 50 à 60 % de temps en moins sur les pièces ; de 3,1 à 0,4 minute par facture. Non audités, parfois anonymes. **Annoncé.** [S18, vues] Usage : 55 % des TPE et PME utilisaient l’IA générative fin 2025, contre 31 % fin 2024 (Bpifrance Le Lab cité par la presse) ; un baromètre de 2026 donne 26 % : définitions à vérifier [S19, vues].

**Ce qu’une administratrice seule peut tenir.** Les mesures sérieuses viennent de grandes organisations ou de bancs d’essai. Tenable : un assistant de bureau, des connecteurs en lecture seule, des tâches programmées, une mémoire de documents. Hors de portée sans intégrateur : des agents qui écrivent dans la banque ou la comptabilité. Nous concevons et relions ; un intégrateur sécurise ; elle valide.

## 3. Ce qui arrive en 2027, 2028, 2030

- **Décembre 2026** — mémoire partagée avec les agents chez Microsoft [S14] ; second comité de suivi de la facture électronique [S16]. **Annoncé.**
- **1er septembre 2027** — les PME et micro-entreprises émettent leurs factures électroniques ; la transmission des données de vente monte en charge [S16]. **Texte publié.**
- **2 décembre 2027 et 2 août 2028** — règles européennes des IA « à haut risque », dont celles qui touchent l’emploi (k4, r1). **Texte publié.**
- **Fin 2027** — plus de 40 % des projets d’agents abandonnés ; environ 130 vrais éditeurs d’agents parmi des milliers [S20]. **Prévu** (Gartner, juin 2025).
- **2028** — 15 % des décisions courantes de travail prises par des agents ; un tiers des logiciels d’entreprise en contiennent [S20]. **Prévu.**
- **2027-2028** — des tâches de plusieurs jours menées seules, si la durée mesurée continue de doubler tous les quatre à sept mois (vue [S2]). Mesuré pour le logiciel ; **supposé** pour l’administratif.
- **2030** — **supposé** : une administratrice qui dirige une équipe d’agents à la voix ; une mémoire de la maison qui répond avec ses pièces ; des connecteurs comptables qui écrivent après validation (Pennylane l’annonce, sans date, r1). Aucune preuve.

## 4. Vingt idées pour GianLuca Carlone

Partout : un outil du marché quand il existe, lecture seule par défaut, son administratrice valide, un prix écrit avant toute commande.

1. **La page du lundi** — trésorerie, suites réservées, places du cabaret, ventes de la galerie, échéances. Verrait : chaque chiffre avec sa pièce. Faut : logiciels reliés. 2027.
2. **L’équipe d’agents de l’administratrice** — un agent par lieu, un coordinateur. Verrait : une seule file « à valider ». Faut : droits minimaux, journal. 2027, après essai.
3. **La mémoire de la maison** — « que dit le bail de la boutique sur les travaux ? » Verrait : la réponse et sa page. Faut : archives classées. 2027.
4. **Le dossier vivant de chaque œuvre** — provenance, factures, assurance, prêts, expositions. Verrait : un dossier prêt pour l’acheteur. Faut : inventaire, règles du négoce validées. 2027.
5. **Factures électroniques sans saisie** — réception, rangement, rapprochement avec devis et paiements. Verrait : les écarts avant paiement. Faut : une plateforme par société. Dès maintenant ; émission en septembre 2027.
6. **La clôture du mois prête** — pièces rapprochées, anomalies et questions pour l’expert-comptable. Verrait : un dossier mensuel complet. Faut : comptabilité reliée. 2027.
7. **Le courrier du matin** — courriels, lettres scannées, messages d’artistes classés par lieu et urgence, avec brouillons. Verrait : rien ne part sans elle. Faut : accord sur les données. 2027, en dernier.
8. **Des réunions aux décisions** — compte rendu, puis registre daté : qui, quoi, quand. Verrait : les retards en tête de la page du lundi. Faut : prévenir les participants. 2027.
9. **Le chantier sous les yeux** — par bâtiment : devis comparés, avancement, réserves, factures face aux devis. Verrait : chaque dépassement avant de payer. Faut : pièces numérisées. 2027.
10. **Les contrats d’artistes préparés** — modèles validés par son avocat, remplis et vérifiés. Verrait : un contrat prêt à relire. Faut : les modèles. 2027.
11. **Les coulisses du cabaret** — plannings, fiches techniques, obligations du spectacle, billetterie. Verrait : la semaine préparée le lundi. Faut : billetterie reliée. 2028.
12. **Les baux des commerces tenus** — échéances, révisions, quittances, relances ; calculs par formule. Verrait : aucune échéance oubliée. Faut : baux lus par un professionnel. 2027.
13. **Le calendrier des contrôles** — sécurité du public, électricité, eau du jacuzzi, assurance des œuvres. Verrait : la pièce attendue jointe au rappel. Faut : liste établie avec ses professionnels. Janvier 2027.
14. **Le mémo mensuel de direction** — par activité, trois décisions, deux options, sources citées. Verrait : deux pages par mois. Faut : la page du lundi. 2027.
15. **Le simulateur de saison** — prix des suites, jauge du cabaret, expositions ; calculs par formule. Verrait : trois scénarios comparés. Faut : une saison d’historique. 2028.
16. **Le veilleur d’aides publiques** — aides de la Région, de l’État, de Bpifrance ; dossiers préparés, une personne dépose. Verrait : une liste par trimestre. 2027.
17. **Le travail de nuit** — tâches longues lancées le soir : archives d’un bâtiment racheté, une année de relevés. Verrait : le résultat au matin, un échantillon contrôlé. 2027.
18. **Les agents tenus en laisse** — charte, comptes nominatifs, essai d’attaque chaque trimestre. Verrait : une page de règles, un rapport. Faut : un intégrateur. Dès le cadrage.
19. **Des procédures que tous suivent** — chaque tâche décrite une fois ; agents et personne qui la relaie l’appliquent pareil. Verrait : une absence ne bloque rien. 2027.
20. **L’administratrice, cheffe d’orchestre** — prise en main sur son temps de travail, attestation datée. Verrait : elle choisit ce que font les agents. Faut : son accord. 2027.

## 5. Faits citables dans un document client

Sources lues le 11 novembre 2026. Ne jamais citer un chiffre seulement « vu ». Le contrôle des documents clients refuse le mot « million ».

1. « Dans un ministère britannique, 3 549 agents ont essayé un assistant d’IA de bureautique d’octobre 2024 à mars 2025 : environ 19 minutes gagnées par jour, surtout pour chercher une information et écrire des courriels. Gains déclarés, sans tirage au sort. » GOV.UK, 29 janvier 2026 [S9].
2. « Au 4 octobre 2026, trois entreprises sur quatre déclarant la TVA avaient choisi leur plateforme de réception des factures électroniques. Les PME et micro-entreprises émettront les leurs à partir du 1er septembre 2027. » Communiqué ministériel, 9 octobre 2026 [S16].
3. « Selon l’AI Index de Stanford, la réussite des agents d’IA sur un banc d’essai de tâches réelles est passée de 20 % à 77,3 % en un an. » 13 avril 2026 [S11].
4. « Le laboratoire indépendant METR estime qu’un modèle testé en mars 2026 réussit une fois sur deux des tâches d’au moins seize heures d’expert, surtout en logiciel ; il ne sait plus mesurer au-delà. » Page METR du 8 septembre 2026 ; presse spécialisée, 10 mai 2026 [S1, S3].
5. « Sur de vraies missions de travailleurs indépendants, le meilleur agent d’IA rendait un travail acceptable par un client dans 2,5 % des cas fin 2025 ; en novembre 2026, le meilleur score affiché est de 41,3 %. » Classement Scale AI, consulté le 11 novembre 2026 [S5].
6. « Une boutique tenue par un agent d’IA est passée des pertes à des semaines presque toutes bénéficiaires, une fois dotée d’outils et de procédures ; l’éditeur la juge encore vulnérable. » Anthropic, 18 décembre 2025 [S8].
7. « Une équipe d’agents coordonnés a fait 90 % mieux qu’un agent seul sur des recherches, pour environ quinze fois plus de calcul qu’une conversation, selon son éditeur. » Anthropic, 13 juin 2025 [S7].
8. « Le cabinet Gartner prévoit l’abandon de plus de 40 % des projets d’agents d’IA d’ici fin 2027 : coûts, valeur peu claire ou risques mal maîtrisés. » Prévision du 25 juin 2025 [S20].
9. « Le protocole ouvert qui relie les assistants d’IA aux logiciels d’entreprise relève depuis décembre 2025 d’une fondation de la Linux Foundation ; sa version du 28 juillet 2026 prévoit douze mois de préavis avant le retrait d’une fonction. » [S12]
10. « Le 9 novembre 2026, un hébergeur allemand a révélé une intrusion passée par le connecteur qui reliait les assistants d’IA de ses clients à sa plateforme : 56 projets touchés, huit jours sans détection. » [S23]

## 6. Règles et limites

- **Droit.** Facture électronique : réception obligatoire depuis le 1er septembre 2026 ; activités exonérées à trancher par l’expert-comptable (r1). Règlement européen sur l’IA : favoriser la maîtrise de l’IA (art. 4, réécrit en juillet 2026) ; dire qu’on parle à une IA (art. 50) ; jamais d’IA qui note une personne (k4). Code du travail, art. L1222-4 : dire avant ce que l’outil enregistre, mémoire de l’assistant comprise [S15] (k4). Relier sa banque à un assistant lève le secret bancaire sur ce point (r1). Lieu de traitement écrit au contrat. Aucun conseil fiscal. À faire valider par ses professionnels.
- **Sécurité.** Un agent lit des contenus non fiables (courriels, formulaires, pages) ; une instruction cachée peut le détourner. Démontré : les données d’un fichier clients envoyées à un attaquant par un simple formulaire [S21] ; 85 % de réussite d’une attaque contre trois agents de programmation [S22]. Référence : les dix risques de l’OWASP (objectif détourné, outils et droits abusés, mémoire empoisonnée) [S24]. Note CIANum-CNIL de juillet 2026 : validation humaine, journal, mémoire cloisonnée, bouton d’arrêt (r1).
- **Échecs connus.** Base de production et sauvegardes effacées en neuf secondes par un agent muni d’un accès trop large ; trente heures d’arrêt (vue [S25], 25 avril 2026). Hébergeur attaqué par son connecteur [S23]. Outils juridiques dits « sans hallucination » : 17 à 33 % de réponses fausses [S26 ; étude de 2024 révisée en 2026, gardée comme seule mesure préenregistrée d’outils documentaires du commerce]. Développeurs 19 % plus lents avec l’IA en 2025, en se croyant plus rapides (k13f).
- **Pour l’administratrice.** Son temps passe de la saisie à la relecture : le gain dépend de la vitesse de vérification. Les débutants gagnent le plus (+34 %, k13f). Règles : lecture seule par défaut ; aucun paiement, envoi ou signature sans elle ; un échantillon contrôlé chaque semaine ; on mesure la tâche, jamais la personne.

## 7. Sources

Toutes consultées le 11 novembre 2026.

- [S1] METR, « Time Horizons », mise à jour du 8 septembre 2026, lue — https://metr.org/time-horizons/
- [S2] Rythme de doublement, résumés, vues — https://www.lesswrong.com/posts/EYb2K9acKfyG2bome/metr-time-horizons-now-10x-year ; https://ai2027-tracker.com/predictions/metr-doubling/
- [S3] The Decoder, 10 mai 2026, lue — https://the-decoder.com/metr-says-it-can-barely-measure-claude-mythos-palo-alto-networks-warns-of-autonomous-ai-attackers/
- [S4] Anthropic, Claude Opus 5.5, 22 septembre 2026, lue — https://www.anthropic.com/news/claude-opus-5-5
- [S5] Scale AI, Remote Labor Index, non datée, lue — https://labs.scale.com/leaderboard/rli
- [S6] GDPval, vues — https://benchmarkregistry.org/benchmarks/gdpval/gdpval (24 septembre 2026) ; https://www.benchleader.com/benchmarks/aa_gdpval (10 novembre 2026) ; page d’OpenAI refusée à l’ouverture.
- [S7] Anthropic, système multi-agents, 13 juin 2025, lue — https://www.anthropic.com/engineering/multi-agent-research-system
- [S8] Anthropic, Project Vend phase 2, 18 décembre 2025, lue — https://www.anthropic.com/research/project-vend-2
- [S9] GOV.UK, évaluation DWP, 29 janvier 2026, lue — https://www.gov.uk/government/publications/an-evaluation-of-dwps-microsoft-copilot-365-trial/an-evaluation-of-dwps-microsoft-365-copilot-trial
- [S10] GOV.UK, essai interministériel, 2 juin 2025, extrait — https://www.gov.uk/government/publications/microsoft-365-copilot-experiment-cross-government-findings-report/microsoft-365-copilot-experiment-cross-government-findings-report-html
- [S11] Stanford HAI, 13 avril 2026, lue — https://hai.stanford.edu/news/inside-the-ai-index-12-takeaways-from-the-2026-report ; rapport, extrait — https://hai.stanford.edu/assets/files/ai_index_report_2026.pdf
- [S12] AAIF, 28 juillet 2026, lue — https://aaif.io/blog/mcp-graduates-to-enterprise-infrastructure-stateless-architecture-formal-governance-and-security
- [S13] Microsoft, 14 octobre 2026, extrait — https://techcommunity.microsoft.com/blog/spblog/introducing-a-team-knowledge-base-curated-by-copilot-and-agents/4564203
- [S14] Microsoft 365, message RM578869, 5 novembre 2026, extrait (archive tierce) — https://mc.merill.net/message/RM578869
- [S15] Anthropic, mémoire, 25 août 2026, extrait — https://claude.com/resources/articles/claudes-memory-works-everywhere-and-you-decide-whats-in-it
- [S16] Communiqué ministériel n° 1103, 9 octobre 2026, texte intégral lu dans sa reproduction — https://www.publicnow.com/view/A82FED1C05965CC8C76DAE06CF0F15ED82BA1E3B
- [S17] TPE Actu, 10 octobre 2026, lue — https://tpeactu.fr/2026/10/10/facturation-electronique-premier-bilan-octobre-2026/
- [S18] Cas comptables, vues — https://www.lagencesauvage.com/blog/ia-cabinet-comptable-donnees-2025-reussir-2026/ (29 décembre 2025) ; https://vantacrew.ai/fr/cas-client/cabinet-comptable-pre-saisie-factures-ocr-ia (22 avril 2026)
- [S19] Bpifrance Le Lab cité par la presse, vues — https://itsocial.fr/contenus/actualites/intelligence-artificielle-actualites-contenus/bpifrance-constate-un-basculement-des-usages-avec-55-des-tpe-pme-utilisatrices-dia-generative-fin-2025/ (10 février 2026) ; https://www.lenouveleconomiste.fr/ia-entreprise-maitrise-pme-134741/ (5 juin 2026)
- [S20] Gartner, 25 juin 2025, texte du communiqué lu dans l’extrait — https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027
- [S21] PromptArmor, 6 février 2026, extrait — https://www.promptarmor.com/resources/data-exfiltration-in-openai-agent-builder-via-mcp
- [S22] Cloud Security Alliance, juin 2026, extrait — https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/06/CSA%5Fresearch%5Fnote%5Fagentjacking%5Fsentry%5Fmcp%5F20260614-csa-styled-2.pdf
- [S23] The Record, 9 novembre 2026, lue — https://therecord.media/cyberattack-germany-ai-mittwald
- [S24] OWASP, 10 décembre 2025, extrait — https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- [S25] AppSentinels (blog d’éditeur), 13 juillet 2026, vue — https://appsentinels.ai/blog/two-months-after-pocketos-what-a-9-second-database-deletion-taught-us-about-agentic-ai-security/
- [S26] Magesh et al., mai 2024, version du 24 août 2026, extrait — https://arxiv.org/abs/2405.20362
- Travaux du dépôt, non revérifiés : r1 (9 novembre 2026) ; k13f et k4 (10 novembre 2026).
