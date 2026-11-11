# État de l’art à la fin de 2026 — direction, administratif et agents d’IA
Document interne — ne pas transmettre à GianLuca Carlone · 11 novembre 2026

Note de chercheur pour le catalogue « State Of The Art ». Vingt-huit recherches et lectures, le 11 novembre 2026. « Lue » : page ouverte ce jour ; « extrait » : long passage de la page d’origine rendu par le moteur ; « vue » : résumé du moteur. Repris sans refaire : r1 (`audit/2026-11-09-audit-presentation-et-offre/travaux/r1-nouveautes-ia-automatisation-2026.md`, produits et connecteurs), k13f (gains mesurés), k4 (droit du travail).

## 1. En bref

- **Les agents tiennent des heures.** Un modèle réussit une fois sur deux des tâches de seize heures d’expert, ou plus [S1, S3]. Trois grands éditeurs vendent un assistant qui prépare un dossier entier (r1).
- **Le réel reste en retrait.** Sur de vraies missions payées, le meilleur agent rend un travail acceptable dans 41 % des cas [S5]. En entreprise, l’usage d’agents à grande échelle reste sous 10 % dans presque toutes les fonctions [S11].
- **Les gains mesurés se comptent en minutes** : 19 par jour dans un ministère britannique, surtout pour chercher et écrire [S9].
- **La prise commune existe.** Le protocole MCP relie assistants et logiciels, sous une fondation [S12]. Il ouvre aussi des portes aux attaquants [S21 à S23].
- **Pour une administratrice seule,** le travail passe de « faire » à « faire faire et vérifier ». Sa relecture devient le goulet.

## 2. Ce qui se fait de mieux aujourd’hui

1. **METR, laboratoire indépendant.** Un modèle testé en mars 2026 réussit une fois sur deux des tâches d’au moins 16 heures d’expert (intervalle : 8,5 à 55 heures), surtout en logiciel. Au-delà, METR ne sait plus mesurer. Août 2025 : 2 h 17. **Mesuré.** [S1, lue, 8 septembre 2026 ; S3, lue, 10 mai 2026]
2. **Anthropic, Claude Opus 5.5.** Un code de 200 000 lignes audité et corrigé en moins de trois heures, contre plus de vingt avec le modèle précédent. Mais 40 % de réussite sur un banc de flux d’entreprise mené par Zapier (meilleur publié : 41,4 %). **Annoncé.** [S4, lue, 22 septembre 2026]
3. **Scale AI, Remote Labor Index.** Vraies missions de travailleurs indépendants, jugées « acceptables par un client raisonnable » : 2,5 % au meilleur au lancement, fin 2025 ; 41,3 % en novembre 2026, 21,3 % au suivant. **Mesuré.** [S5, lue, non datée]
4. **OpenAI, GDPval (44 métiers).** 84,9 % de comparaisons gagnées ou égales face à l’expert, selon l’éditeur (avril 2026) ; 68,3 % au meilleur selon la mesure indépendante d’Artificial Analysis (septembre 2026). **Annoncé.** [S6, vues]
5. **Anthropic, équipe d’agents.** Un agent chef et des sous-agents parallèles font 90,2 % mieux qu’un agent seul, pour environ quinze fois le calcul d’une conversation. Gardé malgré sa date (2025) : seule mesure publique du coût de l’orchestration trouvée. **Mesuré** par l’éditeur. [S7, lue, 13 juin 2025]
6. **Anthropic et Andon Labs, Project Vend.** Une boutique tenue par un agent, dans trois villes. Avec des outils, des procédures et un agent « dirigeant », les semaines à perte disparaissent presque. L’éditeur le juge encore « vulnérable de bien des façons ». **Mesuré.** [S8, lue, 18 décembre 2025]
7. **Ministère britannique du Travail (DWP).** 3 549 agents, d’octobre 2024 à mars 2025, avec groupe de comparaison : 19 minutes gagnées par jour ; 26 pour chercher une information, 25 pour écrire des courriels. Déclaratif. **Mesuré.** [S9, lue, 29 janvier 2026] Essai sur 20 000 agents : 26 minutes déclarées, 17 % sans aucun gain [S10, extrait, 2 juin 2025].
8. **Stanford, AI Index 2026.** Agents sur des tâches réelles en ligne de commande : de 20 % à 77,3 % de réussite en un an. Sur un banc de bureautique, un échec sur trois ; usage à grande échelle sous 10 % dans presque toutes les fonctions (extraits). **Mesuré.** [S11, lue, 13 avril 2026]
9. **Fondation AAIF, protocole MCP.** Version du 28 juillet 2026 : tâches longues reprises après une coupure, autorisations gérées par l’entreprise, douze mois de préavis avant tout retrait. **Publié.** [S12, lue] Pennylane l’offre en lecture seule ; Qonto prépare des virements validés dans sa propre application (r1).
10. **Assistants qui préparent un travail entier.** Copilot Cowork (16 juin 2026), ChatGPT Work (9 juillet 2026), Claude Cowork, avec tâches programmées dans le nuage depuis le 6 octobre 2026. **Disponibles.** (r1)
11. **Mémoire de l’entreprise.** Microsoft : base de connaissances d’équipe tenue par l’assistant, préversion du 14 octobre 2026 [S13] ; mémoire ouverte aux agents en décembre [S14]. Anthropic : mémoire visible et modifiable, active par défaut dans les nouvelles organisations d’équipe depuis le 31 octobre 2026 [S15]. **Annoncé** (extraits).
12. **État français, facture électronique.** Au 4 octobre 2026, 75 % des entreprises déclarant la TVA ont choisi leur plateforme ; plus de 20 millions de factures échangées. Difficultés : coût des offres, interopérabilité, statuts mal transmis. Aucune sanction avant fin 2026. **Mesuré.** [S16, lue, 9 octobre 2026 ; S17]
13. **Comptabilité et PME françaises.** Cas d’éditeurs : 50 à 60 % de temps en moins sur les pièces ; de 3,1 à 0,4 minute par facture. Non audités. **Annoncé.** [S18, vues] 55 % des TPE et PME utilisaient l’IA générative fin 2025, selon Bpifrance Le Lab cité par la presse ; un baromètre de 2026 dit 26 % [S19, vues].

**Tenable par une administratrice seule :** assistant de bureau, connecteurs en lecture seule, tâches programmées, mémoire de documents. Pas sans intégrateur : des agents qui écrivent en banque ou en comptabilité.

## 3. Ce qui arrive en 2027, 2028, 2030

- **Décembre 2026** — mémoire partagée avec les agents chez Microsoft [S14] ; second comité de la facture électronique [S16]. **Annoncé.**
- **1er septembre 2027** — les PME et micro-entreprises émettent leurs factures électroniques [S16]. **Texte publié.**
- **2 décembre 2027 et 2 août 2028** — règles européennes des IA « à haut risque », dont l’emploi (k4, r1). **Texte publié.**
- **Fin 2027** — plus de 40 % des projets d’agents abandonnés ; environ 130 vrais éditeurs d’agents parmi des milliers [S20]. **Prévu** (Gartner).
- **2028** — 15 % des décisions courantes de travail prises par des agents ; un tiers des logiciels d’entreprise en contiennent [S20]. **Prévu.**
- **2027-2028** — des tâches de plusieurs jours, si la durée mesurée double encore tous les quatre à sept mois (vue [S2]). Mesuré en logiciel ; **supposé** pour l’administratif.
- **2030** — **supposé** : une administratrice qui dirige ses agents à la voix ; une mémoire qui répond avec ses pièces ; une comptabilité où l’agent écrit après validation (Pennylane l’annonce, sans date, r1).

## 4. Vingt idées pour GianLuca Carlone

Partout : outil du marché, lecture seule par défaut, son administratrice valide, prix écrit avant toute commande. Chaque ligne : l’idée ; ce qu’il verrait ; ce qu’il faut ; quand.

1. **La page du lundi** : trésorerie, suites, cabaret, galerie, échéances. Verrait : chaque chiffre avec sa pièce. Faut : logiciels reliés. 2027.
2. **L’équipe d’agents de l’administratrice** : un agent par lieu, un coordinateur. Verrait : une seule file « à valider ». Faut : droits minimaux, journal. 2027.
3. **La mémoire de la maison** : « que dit le bail de la boutique sur les travaux ? » Verrait : la réponse et sa page. Faut : archives classées. 2027.
4. **Le dossier vivant de chaque œuvre** : provenance, factures, assurance, prêts, expositions. Verrait : un dossier prêt pour l’acheteur. Faut : inventaire, règles du négoce validées. 2027.
5. **Factures sans saisie** : reçues, rangées, rapprochées des devis et paiements. Verrait : les écarts avant paiement. Faut : une plateforme par société. Dès maintenant ; émission en septembre 2027.
6. **La clôture du mois prête** : pièces rapprochées, questions pour l’expert-comptable. Verrait : un dossier mensuel complet. Faut : comptabilité reliée. 2027.
7. **Le courrier du matin** : courriels, lettres, messages d’artistes classés, brouillons prêts. Verrait : rien ne part sans elle. Faut : accord sur les données. 2027, en dernier.
