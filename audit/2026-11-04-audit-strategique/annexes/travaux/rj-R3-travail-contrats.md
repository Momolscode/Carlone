# R3-travail-contrats : risques de droit du travail et de droit des contrats d'une prestation longue pour un client unique

Mémo du chercheur « R3-travail-contrats », rédigé le 4 novembre 2026 pour l'audit Marwin Tech × GianLuca Carlone. Toutes les pages web citées ont été consultées le **4 nov. 2026**. Aucun contact extérieur, aucune démarche, aucune modification du dépôt `Momolscode/Carlone`.

Le client s'appelle **GianLuca Carlone**. Les pièces qui l'appellent autrement sont citées telles quelles, suivies de [sic, lire GianLuca].

**Codes** : **[FV]** fait vérifié sur source primaire (texte de loi ou pièce du dépôt) ; **[DR]** déclaration rapportée (pièce non vérifiée, propos de Morgan, source secondaire) ; **[PR]** proposition ; **[HY]** hypothèse ou lecture juridique du chercheur, à faire valider ; **[ES]** estimation ; **[MM]** mesure ; **[IN]** inconnu.

**Abréviations des pièces internes**
- **offre-md:N** = `interne/offre-marwin-tech-remuneration-et-collaboration.md:N` (document de travail du 2 nov., sections internes).
- **contexte:N** = `interne/contexte-projet-carlone.md:N`.
- **accomp:N** = `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:N` (offre du 29 oct., export ChatGPT).
- **audit-md:N** = `interne/audit-marwin-tech-carlone.md:N`.
- **DECK/x.html:N** = diaporama client du 4 nov., `scratchpad/artifact-files/04f14ef8-a5fd-429b-9b3e-6d69b1d2ce5f/project/slides/x.html:N` (11 diapositives, `deck.json:7`).
- **CS p. N** et **V5 p. N** = `interne/archives-marwin-tech/choix-structure-2026-10-29.pdf` et `…/options-structure-remuneration-v5-2026-10-30.pdf`, cités **via** l'extraction du lecteur C3 (`audit-work/ex-C3-structure.md:ligne`) ; ce chercheur n'a pas relu ces PDF.
- **C1:N, C2:N, C3:N, C5:N** = extractions des lecteurs dans `audit-work/ex-C*.md`.

---

## 0. Limites de ce mémo et changements 2025-2026 (à lire d'abord)

### 0.1 Limites
1. **Pages Urssaf inaccessibles** : urssaf.fr renvoyait une erreur HTTP 503 le 4 nov. 2026 (comme pour le chercheur R1). L'obligation de vigilance est donc établie par les **textes** (Légifrance) et par la fiche **F31490** d'entreprendre.service-public.gouv.fr, pas par la page Urssaf.
2. **Page du ministère du Travail sur le prêt illicite de main-d'œuvre** (travail-emploi.gouv.fr) : bloquée par un CAPTCHA. Les critères de distinction viennent donc de la jurisprudence publiée sur Légifrance ; une partie (arrêts « inédits », moyens de pourvoi) n'a été vue qu'à travers des extraits de moteur de recherche, signalés **[DR]**.
3. **Mode de lecture** : les pages Légifrance et service-public ont été lues par un outil d'extraction qui limite les citations à de courts segments. Les citations ci-dessous sont exactes mais partielles ; il faut relire l'article complet avant de rédiger un contrat.
4. **EUR-Lex** : lu par un lecteur de pages (Exa) qui a restitué le texte intégral du règlement (UE) 2023/2854 et du RGPD ; citations vérifiées par recherche dans ce texte.
5. **Ce mémo n'est pas un avis juridique.** Il identifie les règles, leur état au 4 nov. 2026 et les points à faire trancher par un **avocat** (droit du travail, droit des contrats, propriété intellectuelle) et par un **expert-comptable** (TVA, débours, activités réservées).

### 0.2 Règles modifiées en 2025 ou 2026 (repérées dans ce mémo)
| Règle | Changement | Date d'effet | Source |
| --- | --- | --- | --- |
| Peines du prêt illicite de main-d'œuvre (L8243-1) et du marchandage (L8234-1) | Articles modifiés par la **loi n° 2026-534 du 25 juin 2026** (lutte contre les fraudes sociales et fiscales), art. 98 ; peine de base inchangée dans la version lue (2 ans, 30 000 €) | 27 juin 2026 | Légifrance (pages des articles) [FV] ; intitulé de la loi via senat.fr (liste des lois promulguées) [DR] |
| Vigilance du maître d'ouvrage sur les sous-traitants (nouvel article L8222-1-1) | Créé par la loi n° 2026-534, art. 95 ; **pas encore en vigueur** | « À venir », version datée du **26 déc. 2026** sur Légifrance ; « au plus tard le **27 décembre 2026** » selon F31490 (écart d'un jour à signaler) | Légifrance ; F31490 [FV] |
| Rupture brutale (L442-1 C. com.) | Article modifié par la **loi n° 2026-796 du 18 août 2026**, art. 54 ; le texte du II cité ci-dessous est celui en vigueur | 20 août 2026 | Légifrance [FV] ; intitulé « d'urgence pour la protection et la souveraineté agricoles » vu seulement dans un sommaire du JO repris par un site d'avocats [DR] |
| Loyauté du salarié qui crée une activité concurrente | Cass. soc., 14 janv. 2026, n° 24-20.799 : faute grave même sans clause de non-concurrence | Jurisprudence | entreprendre.service-public.gouv.fr, actualité A18850 du 20 mars 2026 [FV] |
| Réversibilité des services de données (Data Act) | Règlement (UE) 2023/2854 applicable depuis le **12 sept. 2025** ; plus aucuns frais de changement de fournisseur à compter du **12 janv. 2027** | 12/09/2025 et 12/01/2027 | EUR-Lex [FV] |
| Présomption de non-salariat (L8221-6) | **Aucun changement** : version en vigueur depuis le 1er janv. 2023, aucune version future affichée. Un amendement au projet de loi « fraudes » (Sénat, COM-34) proposait de la remplacer pour certains travailleurs ; il n'apparaît pas dans le texte en vigueur | — | Légifrance [FV] ; senat.fr (amendement, extrait de recherche) [DR] |

**[IN]** Les projets de loi de finances et de financement de la sécurité sociale pour 2027 sont en discussion à la date de l'audit ; ce chercheur n'a pas vérifié s'ils touchent les règles ci-dessous. Aucune loi relative aux activités réglementées citées en section (h) n'a été repérée pour 2025-2026, mais l'historique complet (« Chronolégi ») n'a pas été ouvert pour chaque article.

---

## 0.3 Faits du dossier qui commandent l'analyse

| Fait | Code | Source |
| --- | --- | --- |
| GianLuca Carlone « propose des bureaux, une bonne rémunération et envisage d'investir dans l'activité de Morgan et Mathys » | [DR] (propos rapportés par Morgan, rien d'écrit du client) | contexte:24 ; offre-md:132 ; C2:82 |
| Le salariat d'un fondateur chez GianLuca Carlone est traité comme un risque le 29 oct. (CS p. 6) puis comme un scénario de structure le 30 oct. (« Carlone veut vous salarier », V5 p. 20) ; l'intention du client n'est pas sourcée | [DR] / [IN] | C3:48 ; C3:248 ; C3:362 |
| Offre de base : 15 000 € HT par mois pour **20 journées-personnes (140 h)** ; renforcement 30 000 € HT pour 40 journées-personnes (280 h) ; six mois ; paiement d'avance | [PR] | offre-md:13-14 ; offre-md:195 |
| Volet « Piloter » : suivi des encaissements, dépenses, trésorerie et factures des établissements ; « gestion administrative déléguée » ; coordination des prestataires locaux ; **séjours des invités** ; événements | [PR] | offre-md:52 ; DECK/volets.html:29-37 |
| Principes contractuels prévus : plafonds de dépense, achats au nom de l'entité de GianLuca Carlone ; trois registres de droits ; clause RGPD art. 28 ; sortie avec remise des fichiers et accès ; clause d'indépendance | [PR] | offre-md:206-213 |
| Le mandat détaillé du 29 oct. (catégories d'actes, plafonds par acte et cumulés, « une absence de réponse ne vaut pas approbation ») est réduit le 2 nov. à une ligne de tableau | [FV] (comparaison des pièces) | accomp:92-103 ; offre-md:208 ; C2:253 |
| Le CRM a été fait sans facture ; Mathys en est co-auteur ; la version autonome est hébergée « sur Firebase sous le compte des associés » ; le dépôt FinanceScope/CRM-Carlone était public et contient des données de prospects | [DR] | offre-md:29 ; offre-md:37 ; contexte:26 ; offre-md:228 |
| GianLuca Carlone « a racheté six bâtiments » | [DR] | contexte:24 |
| Quali Contact : centre d'appels que le client « prévoit d'engager » ; ses opératrices utiliseraient les offres préparées par Marwin | [DR] | `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:7,13,20-22` ; C5:80 |
| Le diaporama montré au client promet une « Convention de bureaux », un « Investissement éventuel […] par un pacte écrit » et la « Réversibilité : fichiers, configurations, documentations et accès remis » | [PR] | DECK/cadre.html:16, :26 ; DECK/garanties.html:30 |
| Marwin Tech n'est pas immatriculée ; aucune embauche n'est décidée | [FV] (la pièce le dit) / [DR] | note-point-4-novembre-et-activites.md:6 ; C3:60 |

---

## (a) Présomption de non-salariat et requalification en contrat de travail

### Réponse courte
- Les dirigeants d'une société immatriculée sont **présumés** ne pas être liés à leur donneur d'ordre par un contrat de travail (L8221-6 I). Cette présomption est **simple** : elle tombe si la prestation est fournie « dans des conditions qui les placent dans un lien de subordination juridique permanente » à l'égard du donneur d'ordre, **directement ou par personne interposée** (L8221-6 II). La société Marwin ne fait donc pas écran par elle-même. **[FV]**
- Le lien de subordination est le pouvoir de **donner des ordres et des directives, d'en contrôler l'exécution et de sanctionner les manquements** (Cass. soc., 13 nov. 1996). Le travail au sein d'un **service organisé** n'en est qu'un **indice**, et seulement si le donneur d'ordre fixe **unilatéralement** les conditions d'exécution. **[FV]**
- Le schéma envisagé cumule plusieurs indices : client unique, bureaux du client, temps facturé en journées, disponibilité « vingt jours par mois, avec davantage de couverture si nécessaire » (C1:191), mission de « s'occuper de tout », éventuel salariat parallèle. Le risque de requalification est **réel** si la prestation s'exécute comme une intégration dans les équipes de GianLuca Carlone. **[HY]**
- Conséquence principale en cas de requalification avec intention : **travail dissimulé** pour le donneur d'ordre, jusqu'à **3 ans et 45 000 €** (personne physique), **225 000 €** pour une société, plus les cotisations patronales sur les sommes versées. **[FV]**

### Détail
1. **Le texte.** L8221-6 (version en vigueur depuis le 1er janv. 2023) présume non salariés, pour l'activité qui donne lieu à immatriculation, les personnes physiques immatriculées et « les dirigeants des personnes morales immatriculées » et leurs salariés. Le II permet d'établir un contrat de travail en cas de subordination juridique permanente ; la dissimulation d'emploi est alors retenue si le donneur d'ordre s'est soustrait **intentionnellement** aux obligations de l'employeur, et le donneur d'ordre condamné paie les cotisations patronales sur les sommes versées. **[FV]**
2. **Une seconde présomption** (L8221-6-1, en vigueur depuis le 6 août 2008) : « Est présumé travailleur indépendant celui dont les conditions de travail sont définies exclusivement par lui-même ou par le contrat les définissant avec son donneur d'ordre. » **[FV]** Elle invite à écrire les conditions d'exécution **dans le contrat** et à les respecter en pratique.
3. **Le juge regarde les conditions réelles, pas l'étiquette.** La fiche F1691 : la présomption peut être levée si « les conditions réelles d'exécution du travail révèlent l'existence d'un lien de subordination » ; le recours à de « faux » indépendants peut constituer du travail dissimulé ; un contrôle Urssaf ou de l'inspection du travail, ou une action du travailleur, peuvent déclencher la requalification. **[FV]** La pièce du 29 oct. le disait déjà : « Le statut ne se déduit pas du titre affiché ni de la présence dans les bureaux » (accomp:90). **[FV]**
4. **Faisceau d'indices utilisé par la Cour de cassation** (Cass. soc., 4 mars 2020, n° 19-13.316, chauffeur Uber, publié) : intégration à un service conçu et géré par le donneur d'ordre, absence de « clientèle propre », tarifs fixés par le donneur d'ordre, directives et contrôle de l'activité, pouvoir de sanction (désactivation). **[FV]** Ce n'est pas un cas de prestation intellectuelle, mais les mêmes indices sont transposables. **[HY]**
5. **Indices présents dans le projet Carlone** **[HY]** :
   - **Client unique** et dépendance économique (contexte:95 : « chercher un deuxième client d'ici le quatrième mois ») ;
   - **bureaux** fournis par le client, à Cosne-Cours-sur-Loire (contexte:108) ; les pièces internes reconnaissent que « des horaires imposés et une place dans ses équipes sont des indices de salariat » (offre-md:136 ; contexte:94 ; audit-md:56) ;
   - **prix au temps** : 20 journées-personnes, 140 h, et « davantage de couverture si nécessaire » (offre-md:14 ; C1:191) ;
   - **périmètre « tout »** : pilotage, administration, prestataires, séjours, événements (offre-md:52) ;
   - **salariat parallèle** possible d'un fondateur (offre-md:124-126 ; V5 p. 20 via C3:48).
6. **Indices contraires à construire** **[PR]** (ils ne valent que s'ils sont réels) : livrables et lots définis avec critères de réception ; méthodes, horaires, outils et lieu d'exécution choisis par Marwin (offre-md:213) ; aucune autorité hiérarchique ni pouvoir disciplinaire de GianLuca Carlone ou de ses cadres sur Morgan et Mathys ; adresses électroniques, matériel et comptes Marwin (pas d'adresse ni de badge « salarié » chez le client) ; liberté d'avoir d'autres clients et preuve qu'ils existent ; prix par lot ou par capacité réservée **avec engagement de livrables**, pas un taux horaire de présence ; convention de bureaux séparée qui donne un **accès** sans imposer d'horaires (DECK/cadre.html:16 ; offre-md:136).
7. **Ce que la requalification coûterait** :
   - au donneur d'ordre (l'entité de GianLuca Carlone) : cotisations patronales sur les sommes versées (L8221-6 II), et, si l'intention est établie, les peines du travail dissimulé (L8224-1 : « emprisonnement de trois ans et […] amende de 45 000 euros », version en vigueur ; 225 000 € pour une personne morale selon F31490) **[FV]** ;
   - à Morgan et Mathys : la relation passe sous le droit du travail (durée du travail, rupture, prud'hommes). Le chiffre d'affaires de Marwin et les simulations de structure (R1) deviennent sans objet pour cette activité **[HY]** ;
   - à Marwin : effets fiscaux et sociaux sur les factures déjà émises **[IN]** (à faire chiffrer par l'expert-comptable).

### Sources officielles
| Source | Organisme | Mise à jour affichée | Consultation | Citation courte |
| --- | --- | --- | --- | --- |
| Code du travail, art. L8221-6 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044056617 | Légifrance (DILA) | En vigueur depuis le 01/01/2023 (ord. n° 2021-1189, art. 35) ; aucune version future affichée | 4 nov. 2026 | II : prestations dans un « lien de subordination juridique permanente » |
| Code du travail, art. L8221-6-1 — https://www.legifrance.gouv.fr/affichCodeArticle.do?idArticle=LEGIARTI000019285915&cidTexte=LEGITEXT000006072050 | Légifrance | En vigueur depuis le 06/08/2008 (loi n° 2008-776) | 4 nov. 2026 | « Est présumé travailleur indépendant celui dont les conditions de travail sont définies exclusivement par lui-même » |
| Code du travail, art. L8224-1 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006904833 | Légifrance | En vigueur depuis le 01/05/2008, aucun texte modificatif postérieur affiché | 4 nov. 2026 | « emprisonnement de trois ans et d'une amende de 45 000 euros » |
| Cass. soc., 13 nov. 1996, n° 94-13.187, publié — https://www.legifrance.gouv.fr/juri/id/JURITEXT000007035180/ | Légifrance | — | 4 nov. 2026 | « qui a le pouvoir de donner des ordres et des directives, d'en contrôler l'exécution » « et de sanctionner les manquements » |
| Cass. soc., 4 mars 2020, n° 19-13.316, publié — https://www.legifrance.gouv.fr/juri/id/JURITEXT000042025162 | Légifrance | — | 4 nov. 2026 | « ne constitue aucune clientèle propre » ; statut d'indépendant « fictif » |
| Fiche F1691 « Comment différencier le travailleur indépendant du salarié ? » — https://entreprendre.service-public.gouv.fr/vosdroits/F1691 | DILA (Entreprendre Service Public) | Vérifié le 21/11/2025 | 4 nov. 2026 | « les conditions réelles d'exécution du travail révèlent l'existence d'un lien de subordination » |
| Fiche F31490 « Sanctions de l'employeur en cas de travail illégal » — https://entreprendre.service-public.gouv.fr/vosdroits/F31490 | DILA | Vérifié le 03/07/2026 | 4 nov. 2026 | Travail dissimulé : 3 ans et 45 000 €, « portés à 225 000 € » pour une société (reformulation de la fiche) |

### Incertitudes et points à faire valider
- **[IN]** Le niveau de risque réel dépend de l'exécution (présence, horaires, consignes), qui n'existe pas encore. **Avocat en droit du travail** : relire le contrat-cadre, la convention de bureaux et la façon dont les demandes de GianLuca Carlone seront formulées (commande de livrable ou ordre de travail).
- **[HY]** Le fait que Morgan et Mathys soient **dirigeants** de Marwin (et non salariés de Marwin) ne change pas l'analyse : le II de L8221-6 vise aussi la subordination « par personne interposée ». À confirmer par l'avocat.
- **[IN]** Effets d'une requalification sur la TVA facturée, les cotisations déjà payées par les dirigeants et les aides éventuelles (ACRE, FRR, voir R1) : **expert-comptable**.
- **[DR]** Un amendement sénatorial (COM-34, projet de loi « fraudes ») proposait de supprimer la présomption de non-salariat pour certains travailleurs ; il n'apparaît pas dans le texte en vigueur au 4 nov. 2026 (Légifrance). Les débats parlementaires futurs n'ont pas été suivis.

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Pour GianLuca Carlone (ou son entité)** : c'est lui qui porte le risque pénal et le rappel de cotisations. Il a donc intérêt, autant que Marwin, à un contrat de livrables et à une séparation nette des rôles. **[HY]**
- **Pour Marwin** : la clause « Indépendance » (offre-md:213) est nécessaire mais **insuffisante** ; il faut des preuves d'autonomie tenues dans le temps (comptes rendus de livrables, journal des demandes, autres clients). Le prix « 20 journées-personnes, davantage si nécessaire » est l'élément le plus exposé : présenter la capacité comme une **réserve de production pour des lots définis**, pas comme une présence. **[PR]**
- **Signal d'alerte** à inscrire au registre des risques : demande d'horaires fixes, d'intégration à un organigramme, de rendre compte à un cadre du client comme un salarié, ou de travailler exclusivement pour lui. **[PR]**

---

## (b) Prêt de main-d'œuvre illicite (L8241-1) et marchandage (L8231-1)

### Réponse courte
- « Toute opération à but lucratif ayant pour objet exclusif le prêt de main-d'oeuvre est interdite » (L8241-1), hors travail temporaire et quelques exceptions. Le **marchandage** est une « opération à but lucratif de fourniture de main-d'oeuvre » qui cause un préjudice au salarié ou élude la loi ou une convention (L8231-1). **[FV]**
- Ces deux délits supposent la mise à disposition de **salariés**. Aujourd'hui, Marwin n'existe pas et n'a pas de salarié : le risque **direct** est faible. Il apparaît dès que Marwin fait travailler des **salariés ou des sous-traitants sous les ordres du client**, ou dès que des prestataires (Quali Contact, prestataires locaux) reçoivent leurs consignes directement de Marwin ou de GianLuca Carlone au lieu de leur propre encadrement. **[HY]**
- Peines (versions en vigueur depuis le **27 juin 2026**, loi n° 2026-534) : **2 ans et 30 000 €** ; 5 ans et 75 000 € si plusieurs personnes ou personne vulnérable ; 10 ans et 100 000 € en bande organisée ; interdiction de sous-traiter de la main-d'œuvre de 2 à 10 ans. **150 000 €** pour une société selon F31490. **[FV]**

### Détail
1. **Ce qui distingue une vraie prestation d'un prêt de personnel** (jurisprudence, appréciée au cas par cas) :
   - **objet** : une tâche définie qui mobilise un savoir-faire propre au prestataire, distinct de celui des salariés du client (Cass. soc., 9 juin 1993, n° 91-40.222, publié, vu en extrait [DR] ; Cass. soc., 17 févr. 2016, n° 15-12.262, inédit, vu en extrait [DR]) ;
   - **encadrement** : le prestataire garde l'autorité sur son personnel et contrôle l'exécution (Cass. crim., 19 mars 2013, n° 11-86.552, publié, vu en extrait [DR]) ;
   - **prix** : un forfait lié au résultat plutôt qu'une facturation au temps ou selon le nombre et la qualification des personnes (Cass. crim., 28 janv. 1997, n° 96-80.727 : argument tiré des moyens, vu en extrait [DR]) ;
   - **but lucratif** : il peut s'agir d'« un bénéfice, un profit ou un gain pécuniaire » ; l'infraction a été retenue alors même que les salariés restaient sous l'autorité de la société prêteuse, parce qu'ils effectuaient « exclusivement les tâches habituellement dévolues » aux salariés de l'utilisatrice (Cass. crim., 9 sept. 2020, n° 18-82.746, publié) **[FV]**.
2. **Trois situations du projet à surveiller** **[HY]** :
   - **Marwin renforcée par des tiers** (freelances, Medhi/BOJ.ART, futurs salariés) placés dans les bureaux du client et dirigés par lui : c'est le cas typique. Le prix par « journée-personne » (offre-md:14) est un indice défavorable s'il n'est pas adossé à des livrables.
   - **Quali Contact** : si Marwin ou GianLuca Carlone donnent leurs consignes quotidiennes directement aux opératrices (scripts, volumes, horaires), c'est l'entité qui commande et Quali Contact qui sont exposées. Les consignes doivent passer par l'encadrement de Quali Contact, dans un contrat qui définit les campagnes et les résultats (`carlone-offres-et-projets.md:20-22` ; C5:184).
   - **« Coordination des prestataires locaux »** (offre-md:52) : Marwin peut coordonner des **contrats** (planning, réception, relances), pas commander directement le personnel d'un autre prestataire.
3. **Le prêt à but non lucratif** (refacturation limitée aux salaires, charges et frais) est autorisé sous conditions (L8241-1 dernier alinéa ; L8241-2) **[FV]** ; il ne correspond pas au modèle de Marwin, qui doit dégager une marge.
4. **Conséquence civile** : un prêt illicite peut créer une situation de **coemploi** entre prestataire et utilisateur (Cass. soc., 5 avr. 2018, n° 16-14.695, inédit, vu en extrait) **[DR]**.

### Sources officielles
| Source | Organisme | Mise à jour affichée | Consultation | Citation courte |
| --- | --- | --- | --- | --- |
| C. trav., art. L8241-1 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030442435 | Légifrance | En vigueur depuis le 04/04/2015 (ord. n° 2015-380) | 4 nov. 2026 | « Toute opération à but lucratif ayant pour objet exclusif le prêt de main-d'oeuvre est interdite. » |
| C. trav., art. L8231-1 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006904839 | Légifrance | En vigueur depuis le 01/05/2008 | 4 nov. 2026 | « Le marchandage, défini comme toute opération à but lucratif de fourniture de main-d'oeuvre » |
| C. trav., art. L8243-1 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031013807 | Légifrance | **En vigueur depuis le 27/06/2026** (loi n° 2026-534, art. 98) | 4 nov. 2026 | « d'un emprisonnement de deux ans et d'une amende de 30 000 euros » |
| C. trav., art. L8234-1 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000031013816 | Légifrance | **En vigueur depuis le 27/06/2026** (loi n° 2026-534, art. 98) | 4 nov. 2026 | Base : 2 ans et 30 000 € ; aggravé : 5 ans et 75 000 € ; bande organisée : 10 ans et 100 000 € |
| Cass. crim., 9 sept. 2020, n° 18-82.746, publié — https://www.legifrance.gouv.fr/juri/id/JURITEXT000042348631 | Légifrance | — | 4 nov. 2026 | « pour effectuer exclusivement les tâches habituellement dévolues aux salariés de cette dernière » |
| Fiche F31490 — https://entreprendre.service-public.gouv.fr/vosdroits/F31490 | DILA | Vérifié le 03/07/2026 | 4 nov. 2026 | Prêt illicite et marchandage : 2 ans et 30 000 €, 150 000 € pour une société (reformulation) |

### Incertitudes et points à faire valider
- **[DR]** Plusieurs arrêts de la section 1 ont été lus en extraits de recherche ; l'**avocat** doit confirmer les critères applicables à une prestation intellectuelle (conseil, pilotage, développement).
- **[IN]** Organisation réelle de Quali Contact (contrat, encadrement, payeur) : inconnue (C5:81, C5:184).
- **[IN]** Marwin aura-t-elle des salariés ou des sous-traitants réguliers ? Aucune décision (C3:60).

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Règle de conduite [PR]** : tout intervenant que Marwin fait venir travaille **sous l'autorité de Marwin**, sur un lot défini, avec un prix au livrable ou à la capacité engagée sur des livrables. Les demandes du client passent par Morgan ou Mathys, pas directement au sous-traitant.
- **Pour GianLuca Carlone** : ses équipes ne doivent pas diriger le personnel de Marwin ni celui de Quali Contact ; elles valident des livrables. **[PR]**
- Le volet « s'occuper de tout » est le principal facteur de glissement vers une simple mise à disposition de personnes : chaque mois, la liste des livrables doit précéder la liste des heures. **[PR]**

---

## (c) Obligation de vigilance du donneur d'ordre (L8222-1)

### Réponse courte
- Tout contrat d'un montant **au moins égal à 5 000 € HT** (R8222-1) oblige le donneur d'ordre à vérifier que son cocontractant est immatriculé et à jour de ses déclarations sociales, **à la conclusion puis tous les six mois** jusqu'à la fin de l'exécution (D8222-5). **[FV]**
- Il doit obtenir : (1) l'**attestation Urssaf** de fourniture des déclarations et de paiement des cotisations (art. L243-15 CSS), de **moins de six mois**, dont il **vérifie l'authenticité** auprès de l'organisme ; (2) un justificatif d'immatriculation (extrait K ou K bis, extrait RNE, ou document portant le numéro d'immatriculation). **[FV]**
- Sanctions du donneur d'ordre défaillant si son cocontractant pratique le travail dissimulé : **solidarité financière** (impôts, cotisations, pénalités, aides publiques, salaires) (L8222-2) et **annulation de ses propres réductions de cotisations**, plafonnée à **15 000 €** (personne physique) ou **75 000 €** (personne morale) en l'absence d'annulation dans les cinq ans (L133-4-5 CSS). **[FV]**
- L'offre de base représente **90 000 € HT** sur six mois (15 000 € × 6) **[ES]** : l'entité de GianLuca Carlone sera tenue à cette vigilance envers Marwin ; Marwin le sera envers ses propres sous-traitants dès 5 000 € HT. **[HY]**

### Détail
1. **Seuil global** : R8222-1 vise « toute opération d'un montant au moins égal à 5 000 euros hors taxes » ; un contrat payé en mensualités est apprécié globalement (Urssaf, extrait de recherche, page inaccessible) **[DR]**. Prudence : retenir le montant total du contrat-cadre et de chaque bon de commande. **[HY]**
2. **Périodicité** : D8222-5 (version en vigueur depuis le 1er janv. 2023) : documents à obtenir « lors de la conclusion et tous les six mois jusqu'à la fin de son exécution ». **[FV]** F31490 indique « supérieur à 5 000 € HT » alors que R8222-1 dit « au moins égal » : le décret fait foi. **[FV]**
3. **Particuliers** : un particulier qui contracte pour son usage personnel n'est tenu qu'à une partie des vérifications (L8222-1) **[FV]**. Ce n'est pas le cas ici si le contrat est signé par une société de GianLuca Carlone, ce qui est la recommandation (contexte:106). **[HY]**
4. **Changement 2026** : le nouvel article L8222-1-1 (loi n° 2026-534, art. 95) impose au **maître de l'ouvrage** de vérifier périodiquement les sous-traitants qu'il accepte ; il est « à venir » (version datée du 26 déc. 2026 sur Légifrance ; « au plus tard le 27 décembre 2026 » selon F31490, qui parle de vigilance étendue « à l'ensemble des sous-traitants en cascade »). **[FV]** Effet probable : si Marwin sous-traite une partie d'un lot (Medhi, freelance), l'entité de GianLuca Carlone pourra devoir vérifier aussi ces sous-traitants. **[HY]**

### Sources officielles
| Source | Organisme | Mise à jour affichée | Consultation | Citation courte |
| --- | --- | --- | --- | --- |
| C. trav., art. L8222-1 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000024197683 | Légifrance | En vigueur depuis le 18/06/2011 (loi n° 2011-672) ; aucune version future affichée | 4 nov. 2026 | Vérification « lors de la conclusion » puis périodique, modalités par décret (reformulation) |
| C. trav., art. R8222-1 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030422273 | Légifrance | En vigueur depuis le 01/05/2015 (décret n° 2015-364) | 4 nov. 2026 | « pour toute opération d'un montant au moins égal à 5 000 euros hors taxes » |
| C. trav., art. D8222-5 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046078939 | Légifrance | En vigueur depuis le 01/01/2023 (décret n° 2022-1015) | 4 nov. 2026 | « lors de la conclusion et tous les six mois jusqu'à la fin de son exécution » |
| C. trav., art. L8222-1-1 (nouveau) — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054335512 | Légifrance | **À venir** (version datée du 26/12/2026 ; loi n° 2026-534, art. 95) | 4 nov. 2026 | Vérification des sous-traitants acceptés par le maître de l'ouvrage (reformulation) |
| C. trav., art. L8222-2 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006904824 | Légifrance | En vigueur depuis le 01/05/2008 | 4 nov. 2026 | Solidarité au paiement des impôts, cotisations, pénalités, aides et salaires (reformulation) |
| CSS, art. L133-4-5 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046804928 | Légifrance | En vigueur depuis le 01/01/2023 (LFSS 2023, art. 6) | 4 nov. 2026 | Plafond réduit à 15 000 € (personne physique) et 75 000 € (personne morale) (reformulation) |
| Fiche F31490 — https://entreprendre.service-public.gouv.fr/vosdroits/F31490 | DILA | Vérifié le 03/07/2026 | 4 nov. 2026 | Attestation à demander à la conclusion puis tous les 6 mois « jusqu'à la fin du contrat » |
| Page Urssaf « Obtenir et vérifier une attestation de vigilance » — https://www.urssaf.fr/accueil/attestation-vigilance.html | Urssaf | **Non lue (HTTP 503)** | 4 nov. 2026 | — |

### Incertitudes et points à faire valider
- **[IN]** À partir de quand une société nouvellement immatriculée peut-elle obtenir une attestation de vigilance (avant ses premières déclarations) ? Page Urssaf inaccessible : **à demander à l'Urssaf ou à l'expert-comptable** avant la signature.
- **[IN]** Date exacte d'entrée en vigueur de L8222-1-1 et contenu du décret d'application (liste des documents).
- **[HY]** Si GianLuca Carlone signe à titre personnel pour un usage professionnel, le régime simplifié des particuliers ne s'applique pas ; à confirmer.

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Marwin** : aucune signature ni facture avant l'immatriculation (offre-md:215) ; préparer un dossier de conformité remis à la signature puis tous les six mois (attestation Urssaf, extrait K bis ou RNE). Calendrier : à la signature, mois 6, mois 12. **[PR]**
- **Marwin donneur d'ordre** : exiger les mêmes pièces de Medhi/BOJ.ART, des freelances et de tout sous-traitant dès 5 000 € HT cumulés. **[PR]**
- **GianLuca Carlone** : la vigilance protège son entité ; la proposer comme garantie dans l'offre est un argument de sérieux. **[PR]**

---

## (d) Cumul : salariat chez le client et prestation par sa propre société

### Réponse courte
- **Juridiquement possible**, mais c'est le scénario le plus risqué du dossier. Il exige deux contrats distincts, des fonctions distinctes et une frontière tenue dans les faits ; sinon, le salariat « contamine » la prestation et favorise la requalification de toutes les factures. **[HY]**
- Pendant le contrat de travail, le salarié doit une **obligation de loyauté** : pas d'activité concurrente, même accessoire et même sans clause de non-concurrence (Cass. soc., 14 janv. 2026, n° 24-20.799 : faute grave). **[FV]**
- Une **clause d'exclusivité** peut interdire le cumul ; elle ne peut pas être imposée à un temps partiel sauf justification ; elle peut être levée **1 an** (jusqu'à 2 ans) pour créer ou reprendre une entreprise. Les durées maximales (10 h par jour, 48 h par semaine) ne s'appliquent qu'aux activités **salariées**. **[FV]**
- Un salarié de l'entité de GianLuca Carlone ne doit ni **commander**, ni **valider**, ni **payer** les prestations de Marwin : conflit d'intérêts. En représentation d'une personne physique, l'acte conclu par un représentant pour son propre compte avec le représenté est **nul** sauf autorisation ou ratification (C. civ., art. 1161). **[FV]**
- Les logiciels créés par un salarié **dans ses fonctions** appartiennent à l'employeur (CPI, L113-9) : si un fondateur développe pendant son temps salarié, le code revient à l'entité de GianLuca Carlone, pas à Marwin. **[FV]**

### Détail
1. **Contradiction des pièces** : CS p. 6 présente le salariat comme un risque à faire examiner (« Si John-Lucas [sic, lire GianLuca] devient à la fois employeur et client ») ; V5 p. 20 en fait un scénario de structure (« Carlone veut vous salarier ») sans source (C3:248 ; C3:273). L'offre interne prévoit : « Le salariat ne vaut que pour des fonctions réellement salariées, avec un contrat distinct ; un CDD exige un motif légal temporaire. Les lots autonomes restent facturés par Marwin » (offre-md:126) **[PR]**. La question « Veut-il salarier l'un de vous, et pour quelles fonctions ? » reste ouverte (contexte:109) **[IN]**.
2. **Règles du cumul** (F1945, vérifiée le 21 juin 2023, page ancienne mais textes stables à la connaissance du chercheur) **[FV]** : 10 h par jour, 48 h par semaine ou 44 h en moyenne sur 12 semaines, tous employeurs confondus ; amende jusqu'à 1 500 € (3 000 € en récidive) en cas de dépassement ; loyauté ; clause d'exclusivité ; levée temporaire pour création d'entreprise.
3. **Risques propres au cumul chez le même client** **[HY]** :
   - **frontière floue** : mêmes lieux, mêmes interlocuteurs, mêmes sujets → un contrôleur peut considérer que les factures de Marwin rémunèrent en réalité du travail subordonné (L8221-6 II), et les réintégrer dans l'assiette des cotisations ;
   - **conflit d'intérêts** : le salarié qui prépare le budget ou valide les livrables de sa propre société. L'art. 1161 ne vise, depuis 2018, que la représentation des **personnes physiques** ; pour une société de GianLuca Carlone, le risque relève de la loyauté du salarié et des règles de la société concernée (**avocat**) ;
   - **propriété intellectuelle** : L113-9 attribue à l'employeur les logiciels créés par l'employé « dans l'exercice de [ses] fonctions ou d'après les instructions » de l'employeur (reformulation) ; sans séparation stricte, les composants que Marwin voudrait réutiliser chez d'autres clients pourraient appartenir au client ;
   - **dépendance totale** : emploi, honoraires, bureaux et peut-être capital chez la même personne ; tout s'arrête ensemble (offre-md:148).
4. **Statut social** : un fondateur salarié chez le client et dirigeant de Marwin cumule deux régimes (voir R1, `rj-R1-structures.md`) ; l'offre interne envisage une SAS avec mandat non rémunéré dans ce cas (offre-md:166) **[PR]**.

### Sources officielles
| Source | Organisme | Mise à jour affichée | Consultation | Citation courte |
| --- | --- | --- | --- | --- |
| Fiche F1945 « À quelles conditions un salarié peut-il cumuler plusieurs emplois ? » — https://www.service-public.gouv.fr/particuliers/vosdroits/F1945 | DILA | Vérifié le 21/06/2023 | 4 nov. 2026 | « plus de 10 heures par jour et 48 heures par semaine » |
| Actualité A18850 (loyauté, micro-entreprise concurrente) — https://entreprendre.service-public.gouv.fr/actualites/A18850 | DILA | 20/03/2026 | 4 nov. 2026 | « le simple fait de créer et d'exercer en tant que micro-entrepreneur une activité directement concurrente » |
| C. civ., art. 1161 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036829830 | Légifrance | En vigueur depuis le 01/10/2018 (loi n° 2018-287) | 4 nov. 2026 | « un représentant ne peut agir pour le compte de plusieurs parties au contrat en opposition d'intérêts » |
| CPI, art. L113-9 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039279818 | Légifrance | En vigueur depuis le 01/01/2020 (ord. n° 2019-964) | 4 nov. 2026 | « Sauf dispositions statutaires ou stipulations contraires, les droits patrimoniaux sur les logiciels et leur documentation » |

### Incertitudes et points à faire valider
- **[IN]** Réalité et contenu de l'offre d'emploi (entité employeuse, fonctions, temps de travail, durée, rémunération).
- **Avocat en droit du travail** : rédaction du contrat de travail (fonctions, clause d'exclusivité levée ou absente, clause de propriété intellectuelle limitée aux fonctions salariées, déclaration de conflit d'intérêts) et articulation avec le contrat Marwin.
- **Expert-comptable / Urssaf** : traitement social et fiscal du cumul ; effet sur ACRE, FRR et option IR (R1).
- **[HY]** Un CDD exige un motif légal (offre-md:126) ; motifs non examinés ici.

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Recommandation du chercheur [PR]** : **différer** tout salariat chez GianLuca Carlone au-delà du premier bilan (mois 3 à 6). S'il devient nécessaire : une seule personne, fonctions clairement non couvertes par le contrat Marwin, temps séparés, et validation des livrables Marwin par une autre personne du côté client.
- **Pour GianLuca Carlone** : salarier un fondateur et payer Marwin pour des tâches voisines crée pour lui un double risque (requalification des factures, contentieux de propriété du code). **[HY]**
- Tant que la question n'est pas tranchée, ne pas l'utiliser comme argument de négociation des honoraires (contexte:93 ; offre-md:149). **[PR]**

---

## (e) Dépendance économique et rupture brutale de relations commerciales établies (L442-1 II C. com.)

### Réponse courte
- Engage sa responsabilité celui qui rompt **brutalement, même partiellement**, une relation commerciale **établie**, sans **préavis écrit** tenant compte notamment de la durée de la relation (L442-1 II). Un préavis de **dix-huit mois** met l'auteur de la rupture à l'abri d'une contestation sur la durée. La rupture sans préavis reste possible en cas d'inexécution grave ou de force majeure. **[FV]**
- La règle joue **dans les deux sens** : elle protège Marwin si l'entité de GianLuca Carlone arrête brutalement une relation devenue établie, mais elle oblige aussi Marwin à un préavis si elle se retire. **[HY]**
- La relation peut être « établie » malgré des contrats successifs à durée déterminée, si la victime pouvait raisonnablement anticiper sa poursuite (Cass. com., 19 mars 2025, n° 23-22.182, publié). Un contrat de six mois à peine commencé l'est probablement moins **[HY]**.
- L'abus de **dépendance économique** (L420-2 al. 2) suppose un effet sur la concurrence : peu utile pour une petite prestation **[HY]**. La vraie protection de Marwin est **contractuelle** (préavis gradué, sortie organisée) et **commerciale** (deuxième client).

### Détail
1. **Texte en vigueur** (version depuis le 20 août 2026, loi n° 2026-796, art. 54) : « Engage la responsabilité de son auteur et l'oblige à réparer le préjudice causé le fait, » « par toute personne exerçant des activités de production, de distribution ou de services » « de rompre brutalement, même partiellement, une relation commerciale établie, » « en l'absence d'un préavis écrit qui tienne compte notamment de la durée de la relation commerciale ». Et : la responsabilité « ne peut être engagée du chef d'une durée insuffisante dès lors qu'il a respecté un préavis de dix-huit mois ». **[FV]**
2. **Préavis raisonnable** : le temps nécessaire à la victime « pour réorienter son activité » (formule de la cour d'appel reprise dans Cass. com., 19 mars 2025) ; une période qui ne permet pas de se réorganiser ne vaut pas préavis effectif. **[FV]** Autres critères (ancienneté, volume d'affaires, dépendance, investissements) : Cass. com., 14 oct. 2020, n° 18-22.119, vu en extrait **[DR]**. La dépendance économique n'a pas à être prouvée pour établir la brutalité : Cass. com., 24 juin 2020, n° 18-10.896, vu en extrait **[DR]**.
3. **Champ** : L442-1 vise une personne exerçant une activité de production, de distribution ou de services. Il faut donc savoir **quelle entité** signe pour GianLuca Carlone (contexte:106) **[IN]**. Si la relation était requalifiée en contrat de travail, c'est le droit du travail, et non L442-1, qui s'appliquerait **[HY]**.
4. **Dépendance de Marwin** : 100 % du chiffre d'affaires prévu viendrait d'un seul client, qui fournirait aussi les bureaux, peut-être un salaire et un investissement (C1:343 ; offre-md:148). La réparation de L442-1 couvre en principe la perte liée à l'**insuffisance du préavis**, pas la perte de la relation elle-même **[HY, à confirmer par l'avocat]**. La réponse interne « 10 millions » à la question de la part maximale des revenus venant de Carlone (contexte:129) montre que ce risque n'est pas traité **[FV]**.
5. **L420-2 al. 2** (version issue de l'ordonnance du 3 juillet 2019) interdit l'exploitation abusive de l'état de dépendance économique d'une entreprise cliente ou fournisseur « dès lors qu'elle est susceptible d'affecter le fonctionnement ou la structure de la concurrence » (reformulation d'un extrait de recherche) **[DR]**.

### Sources officielles
| Source | Organisme | Mise à jour affichée | Consultation | Citation courte |
| --- | --- | --- | --- | --- |
| C. com., art. L442-1 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047381704 | Légifrance | **En vigueur depuis le 20/08/2026** (loi n° 2026-796, art. 54) | 4 nov. 2026 | « de rompre brutalement, même partiellement, une relation commerciale établie » ; « un préavis de dix-huit mois » |
| Cass. com., 19 mars 2025, n° 23-22.182, publié — https://www.legifrance.gouv.fr/juri/id/JURITEXT000051367827 | Légifrance | — | 4 nov. 2026 | « raisonnablement anticiper la poursuite » ; préavis « pour réorienter son activité » |
| C. com., art. L420-2 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038725501 | Légifrance | Version issue de l'ord. du 03/07/2019 (vue en extrait) | 4 nov. 2026 | — (page non ouverte en entier) |

### Incertitudes et points à faire valider
- **[DR]** Objet exact de la modification de L442-1 par la loi n° 2026-796 (loi agricole selon un sommaire du JO repris par un tiers) : le II cité est bien celui en vigueur, mais le contenu modifié n'a pas été identifié.
- **[HY]** À partir de quelle durée la relation Marwin–Carlone serait « établie » : à apprécier par l'**avocat** au regard de la durée prévue (6 mois, reconduction) et de la régularité.
- **[IN]** Entité contractante et nature de son activité.

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Clause de préavis graduée [PR]** (durées à valider par l'avocat) : par exemple 1 mois pendant les six premiers mois, puis un préavis croissant avec l'ancienneté ; préavis réciproque ; possibilité de réduire le périmètre plutôt que d'arrêter ; paiement des travaux engagés et de la réversibilité pendant le préavis.
- **Clause de sortie des bureaux** liée au préavis : la convention de bureaux doit prévoir un délai de restitution, sinon l'arrêt des honoraires et la perte des locaux sont simultanés. **[PR]**
- **Objectif commercial** : un deuxième client avant le quatrième mois (contexte:95) et un plafond de dépendance suivi chaque mois (part du chiffre d'affaires venant des entités de GianLuca Carlone). **[PR]**

---

## (f) Responsabilité civile professionnelle et limitation de responsabilité

### Réponse courte
- L'assurance **RC professionnelle n'est pas obligatoire** pour toutes les sociétés ; elle l'est pour certaines activités réglementées (F37365, vérifiée le 7 juillet 2026). Pour Marwin, elle est **fortement recommandée** et deviendrait **obligatoire** si Marwin exerçait certaines activités réglementées (recouvrement de créances, vente de voyages, immobilier : voir (h)). **[FV]**
- Si Marwin occupe les bureaux du client **comme locataire**, elle doit assurer le local (F37365). La convention de bureaux doit le préciser (DECK/cadre.html:16 ; offre-md:136). **[FV]** / **[PR]**
- Une **clause limitative de responsabilité** est en principe admise entre professionnels, mais elle ne joue pas en cas de **faute lourde ou dolosive** (C. civ., 1231-3), elle est réputée non écrite si elle **prive de sa substance l'obligation essentielle** (1170), ou si elle crée un **déséquilibre significatif** dans un contrat d'adhésion (1171). Les dommages réparables se limitent au **prévisible** (1231-3) et au **direct** (1231-4). **[FV]**

### Détail
1. **Textes** : art. 1231-3 (en vigueur depuis le 1er oct. 2016) : le débiteur n'est tenu que des dommages prévus ou prévisibles lors de la conclusion, « sauf lorsque l'inexécution est due à une faute lourde ou dolosive » **[FV, via extraits Légifrance]** ; art. 1170 : « Toute clause qui prive de sa substance l'obligation essentielle du débiteur est réputée non écrite » **[FV]** ; art. 1171 (version du 1er oct. 2018) : dans un contrat d'adhésion, la clause non négociable qui crée un déséquilibre significatif est réputée non écrite, sans contrôle du prix ni de l'objet principal **[FV]**. Entre partenaires commerciaux, L442-1 I sanctionne aussi le déséquilibre significatif **[HY : texte du I non relu dans cette session]**.
2. **Application à Marwin** **[PR]** :
   - plafond global lié aux honoraires (par exemple les honoraires des douze derniers mois), à négocier et à aligner sur le plafond de l'assurance ;
   - exclusion des dommages indirects (ventes d'œuvres manquées, économie d'impôt espérée par les prospects, décisions d'investissement) ;
   - obligation **de moyens** pour le pilotage, la préparation de décisions et les sorties d'IA ; obligation de résultat seulement pour des livrables précis réceptionnés ;
   - obligations du client écrites (données, accès, validations, délais de réponse) ; « une absence de réponse ne vaut pas approbation » pour les dépenses (accomp:103) ;
   - le plafond ne doit pas vider l'obligation essentielle (Chronopost, Cass. com., 22 oct. 1996, n° 93-18.632, vu en extrait **[DR]**) : un plafond dérisoire sur la remise d'un livrable central serait fragile.
3. **Dommages corporels** et événements avec public : la validité d'une limitation pour dommages corporels est douteuse **[HY]** ; ces activités (vernissage, robotique en galerie) demandent une assurance spécifique et un exploitant responsable (contexte:97) ; elles sont hors de ce mémo.
4. **Avant immatriculation** : un acte signé pour la société en formation engage ses signataires jusqu'à la reprise (accomp:145 ; offre-md:215) **[DR]** ; ne rien exécuter de risqué avant la reprise.
5. **IA et données** : erreurs d'un agent (courriel à un prospect, chiffre fiscal faux, suppression de données), incident de sécurité. Les contrats d'assurance peuvent exclure ou plafonner les risques « cyber » ou liés à l'IA **[IN]** : à demander à l'assureur.

### Sources officielles
| Source | Organisme | Mise à jour affichée | Consultation | Citation courte |
| --- | --- | --- | --- | --- |
| Fiche F37365 « Assurances de la société » — https://entreprendre.service-public.gouv.fr/vosdroits/F37365 | DILA | Vérifié le 07/07/2026 | 4 nov. 2026 | « cette obligation peut notamment porter sur une assurance de responsabilité civile professionnelle (RCP) » ; « Si la société est locataire d'un local, elle doit souscrire une assurance. » |
| C. civ., art. 1231-3 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032010127 | Légifrance | En vigueur depuis le 01/10/2016 | 4 nov. 2026 | « sauf lorsque l'inexécution est due à une faute lourde ou dolosive » |
| C. civ., art. 1231-4 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032010129 | Légifrance | En vigueur depuis le 01/10/2016 | 4 nov. 2026 | Suite immédiate et directe de l'inexécution (reformulation) |
| C. civ., art. 1170 — https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070721/LEGISCTA000032008690/ | Légifrance | En vigueur depuis le 01/10/2016 | 4 nov. 2026 | « Toute clause qui prive de sa substance l'obligation essentielle du débiteur est réputée non écrite. » |
| C. civ., art. 1171 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036829836 | Légifrance | En vigueur depuis le 01/10/2018 | 4 nov. 2026 | Clause créant un déséquilibre significatif « réputée non écrite » |

### Incertitudes et points à faire valider
- **Assureur ou courtier** : RC professionnelle (montant, franchises, exclusions IA, cyber, données) ; assurance des locaux mis à disposition ; garanties pour les événements si Marwin coordonne.
- **Avocat** : rédaction du plafond et des exclusions ; qualification du contrat (négocié ou d'adhésion) ; texte de L442-1 I.
- **[IN]** Les « 30 000 € de frais annuels » des simulations ne détaillent pas la RC pro (C3:279).

### Conséquences pour Marwin Tech et GianLuca Carlone
- Souscrire la RC pro **avant** la première prestation (contexte:13 le prévoit) **[PR]** ; plafond contractuel ≤ plafond assuré.
- Pour GianLuca Carlone : un plafond lisible et une assurance identifiée sont des garanties ; un prestataire sans assurance qui pilote ses achats et ses données est un risque pour lui. **[HY]**

---

## (g) Mandat et pouvoirs délégués pour engager des dépenses au nom du client

### Réponse courte
- Agir au nom du client suppose un **mandat** (C. civ., 1984), qui peut être donné par écrit, « même par lettre » (1985). Un mandat **général** ne couvre que les **actes d'administration** ; pour aliéner ou tout autre acte de propriété, il faut un mandat **exprès** (1988). **[FV]**
- Le mandataire « ne peut rien faire au-delà de ce qui est porté dans son mandat » (1989) ; l'acte accompli **sans pouvoir ou au-delà** est inopposable au client, sauf **mandat apparent** (1156). Le mandataire répond de ses fautes (1992) et doit **rendre compte** (1993). **[FV]**
- Marwin ne doit jamais se commander à elle-même une prestation au nom du client ; pour une personne physique représentée, l'acte serait nul sauf autorisation ou ratification (1161). **[FV]**
- **TVA** : les achats refacturés ne sortent de la base taxable de Marwin (régime des **débours**) que si quatre conditions cumulatives sont réunies : dépenses engagées **au nom et pour le compte** du mandant, **reddition de compte précise**, **justification** auprès de l'administration, **comptes de passage** (BOFiP BOI-TVA-BASE-10-10-30, § 200). **[FV]**

### Détail
1. **Ce que les pièces prévoient** : le 29 oct., une délégation par catégories, avec pour chacune « l'entité concernée, le budget disponible, le plafond par acte, le plafond cumulé et la personne habilitée » ; nouveaux contrats, recrutements, emprunts et investissements réservés au client ; fiscalité, droit, travaux et exploitation réglementée confiés à un professionnel compétent (accomp:94-101) ; « une absence de réponse ne vaut pas approbation » (accomp:103) **[PR]**. Le 2 nov., il ne reste qu'une ligne : « Plafonds de dépense ; achats au nom de l'entité de Carlone ; aucune dépense hors plafond sans accord écrit » (offre-md:208) **[PR]**. Le diaporama ne montre que « Achats directs : Le matériel est acheté et possédé par votre entité » (DECK/cadre.html:21) **[PR]**. La version détaillée du 29 oct. est la plus protectrice ; elle doit revenir dans le contrat. **[HY]**
2. **Architecture recommandée [PR]** :
   - un mandat **écrit et distinct** par entité de GianLuca Carlone, signé par son représentant légal ;
   - une liste fermée d'actes autorisés, avec plafond par acte, plafond mensuel cumulé et budget par projet ; tout engagement récurrent (abonnement, contrat) au-delà d'une durée fixée exige un accord écrit ;
   - les factures fournisseurs sont **émises au nom de l'entité cliente** et **payées par elle** ; Marwin prépare, le client valide et paie ; Marwin ne détient pas les fonds du client ;
   - un registre des engagements, rapproché chaque mois du budget (reddition de compte, 1993) ;
   - urgences : un plafond d'urgence faible, documenté après coup ;
   - silence du client : l'engagement attend (accomp:103).
3. **Accès bancaires** : pas d'identifiants personnels du client partagés ; accès délégués et nominatifs, en lecture ou avec validation par le client (offre-md:210 pour les accès nominatifs) **[PR]**.
4. **Maniement de fonds de tiers** : encaisser ou payer pour le compte du client peut relever de réglementations financières (services de paiement, recouvrement, voir (h)) **[IN, non vérifié dans cette session]** ; à éviter par construction.
5. **Débours** : si Marwin achète **en son nom** puis refacture, la somme entre dans son chiffre d'affaires et dans sa base de TVA, et Marwin porte le risque d'impayé **[HY, cohérent avec BOFiP § 200 et § 220]**. Le BOFiP exige un « mandat préalable et explicite » et que l'intermédiaire agisse au nom du mandant (§ 220) **[FV]**.

### Sources officielles
| Source | Organisme | Mise à jour affichée | Consultation | Citation courte |
| --- | --- | --- | --- | --- |
| C. civ., art. 1984 à 2010 (mandat) — https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070721/LEGISCTA000006118139/ | Légifrance | Version en vigueur au 04/11/2026 | 4 nov. 2026 | 1989 : « Le mandataire ne peut rien faire au-delà de ce qui est porté dans son mandat » ; 1992 : « Le mandataire répond non seulement du dol, mais encore des fautes qu'il commet dans sa gestion. » ; 1993 : « Tout mandataire est tenu de rendre compte de sa gestion » |
| C. civ., art. 1988 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006445241/1804-03-20 | Légifrance | Texte d'origine (1804), toujours en vigueur selon la section | 4 nov. 2026 | « Le mandat conçu en termes généraux n'embrasse que les actes d'administration. » (extrait de recherche) |
| C. civ., art. 1153 à 1161 (représentation) — https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070721/LEGISCTA000032008382/ | Légifrance | 1153 et 1156 : 01/10/2016 ; 1161 : 01/10/2018 | 4 nov. 2026 | 1156 : « L'acte accompli par un représentant sans pouvoir ou au-delà de ses pouvoirs est inopposable au représenté » |
| BOFiP, BOI-TVA-BASE-10-10-30-20220511 (débours) — https://bofip.impots.gouv.fr/bofip/488-PGP.html/identifiant=BOI-TVA-BASE-10-10-30-20220511 | DGFiP | Publié le 11/05/2022 | 4 nov. 2026 | « engagées au nom et pour le compte de leurs mandants » ; « portées dans des comptes de passage » |

### Incertitudes et points à faire valider
- **Expert-comptable** : traitement TVA des achats (débours ou refacturation), comptes de passage, facturation électronique.
- **Avocat** : rédaction des mandats par entité ; responsabilité de Marwin envers les tiers en cas de dépassement ; articulation avec les pouvoirs des dirigeants des sociétés de GianLuca Carlone.
- **[IN]** Liste des entités, de leurs représentants et de leurs budgets (C2:227).

### Conséquences pour Marwin Tech et GianLuca Carlone
- Rétablir dans le contrat la grille du 29 oct. (accomp:94-101) plutôt que la ligne du 2 nov. **[PR]**
- Pour GianLuca Carlone : un mandat précis le protège d'engagements non voulus ; un mandat flou l'expose au mandat apparent (1156). **[HY]**
- Pour Marwin : sans mandat écrit, chaque achat fait « pour rendre service » engage sa responsabilité (1992) et peut lui rester à charge. **[HY]**

---

## (h) Gestion administrative déléguée : activités réglementées à ne pas exercer

### Réponse courte
Le volet « Piloter » (offre-md:52) touche plusieurs activités **réservées** ou **encadrées**. Marwin peut **préparer, organiser, suivre et coordonner** ; elle ne doit pas **exercer** ces activités elle-même sans remplir leurs conditions. **[HY]** fondée sur les textes **[FV]** ci-dessous.

| Activité | Ce qui est réservé ou encadré | Texte | Risque dans le projet | Ce que Marwin peut faire **[PR]** |
| --- | --- | --- | --- | --- |
| **Expertise comptable** | Exécuter **habituellement** les travaux de l'art. 2 (al. 1 : réviser et apprécier les comptabilités ; al. 2 : **tenir**, centraliser, ouvrir, arrêter, surveiller, redresser et consolider les comptabilités) sans être inscrit à l'Ordre | Ord. n° 45-2138, art. 2 et art. 20 (délit, peines de l'art. 433-17 C. pén. : 1 an et 15 000 €) **[FV]** | « Suivi centralisé des établissements (encaissements, dépenses, trésorerie, factures) » (offre-md:52) | Tableau de bord de gestion et de trésorerie à partir des données du client ; préparation et classement des pièces pour l'expert-comptable ; **pas** de saisie, tenue, révision ni établissement des comptes |
| **Paie et déclarations sociales** | **[IN]** : statut de la paie au regard du monopole non vérifié | — | « gestion administrative déléguée » | Coordination avec le cabinet ou le prestataire de paie du client |
| **Consultation juridique et rédaction d'actes** | Donner des consultations juridiques ou rédiger des actes sous seing privé **pour autrui, à titre habituel et rémunéré** est réservé aux personnes qualifiées (art. 54) ; l'exception de l'art. 60 suppose une **qualification reconnue** liée à l'activité principale | Loi n° 71-1130, art. 54 (en vigueur depuis le 01/01/2020) et art. 60 **[FV]** ; Conseil d'État, 4 avr. 2018, n° 415946 (extrait) **[DR]** | Contrats d'artistes, conditions de vente, baux, statuts ; calcul du « plafond de déduction » et de l'« économie d'impôt » par entreprise prospecte (offre-md:34) | Préparer un dossier factuel et une liste de questions pour l'avocat ; information fiscale **générale** validée par un professionnel, avec renvoi de chaque prospect à son expert-comptable **[HY : la frontière entre information générale et consultation personnalisée est à faire trancher]** |
| **Immobilier (loi Hoguet)** | Personnes qui, « d'une manière habituelle », « se livrent ou prêtent leur concours, même à titre accessoire » aux opérations sur les biens d'autrui, dont la **gestion immobilière** (6°), la location, la vente | Loi n° 70-9, art. 1 (en vigueur depuis le 27/03/2014) **[FV]** ; carte professionnelle, garantie et RC pro (fiche F32994, non ouverte) **[DR]** | GianLuca Carlone « a racheté six bâtiments » (contexte:24) ; suivi des établissements | Pas de recherche de locataires, de gestion des baux ni d'encaissement des loyers pour son compte ; coordination d'un administrateur de biens ou de l'équipe du client |
| **Vente de voyages et séjours** | Ceux qui « élaborent et vendent ou offrent à la vente » des forfaits ou services de voyage : immatriculation, garantie financière, RC pro ; exclusion seulement pour une offre occasionnelle, **sans but lucratif**, pour un groupe limité | C. tourisme, art. L211-1 (en vigueur depuis le 01/07/2018) **[FV]** | « Séjours des invités » (offre-md:52 ; DECK/volets.html:31) | Organiser pour le compte du client, qui réserve et paie directement hôtels et transports ; Marwin ne vend pas de séjour |
| **Recouvrement amiable de créances** | Assurance RC pro, **compte exclusivement affecté** aux fonds encaissés, **déclaration écrite au procureur** avant toute activité | CPCE, art. R124-2 (en vigueur depuis le 01/01/2020) **[FV]** | « encaissements » et relances d'impayés des établissements | Relances signées par le client, encaissements sur ses comptes ; pas de recouvrement rémunéré pour son compte |
| **Intermédiaire en biens divers** | Proposer un rendement ou un rachat garanti sur des œuvres | Non vérifié dans cette session ; signalé par contexte:91 **[DR]** | Vente d'œuvres aux entreprises | Ne jamais promettre rendement, plus-value ou rachat (contexte:91) |
| **Données personnelles** | Sous-traitant au sens du RGPD (art. 28) : contrat écrit, instructions documentées, fin de prestation | RGPD art. 28 **[FV]** (voir (j)) | CRM, Jarvis, Quali Contact | Clause art. 28 déjà prévue (offre-md:210) |

### Détail
1. **Expertise comptable** : art. 20 : « Exerce illégalement la profession d'expert-comptable celui qui, sans être inscrit au tableau de l'ordre en son propre nom » « exécute habituellement des travaux prévus par les deux premiers alinéas de l'article 2 », en intervenant directement dans la tenue, la vérification, l'appréciation ou le redressement des comptes (version en vigueur depuis le 16 févr. 2022) ; l'art. 2 al. 1 (en vigueur depuis le 8 mai 2017) vise celui qui « fait profession habituelle de réviser et d'apprécier les comptabilités des entreprises ». **[FV]** La Cour de cassation (crim., 22 févr. 2022, n° 21-85.594, extrait) rappelle que ces missions sont réservées **[DR]**.
2. **Consultation juridique** : le diaporama et l'offre le prévoient déjà en partie : « Questions fiscales, juridiques, travaux et exploitation réglementée : professionnel compétent et responsable désignés ; Marwin coordonne le dossier dans son mandat » (accomp:101) **[PR]**, et « Les contenus fiscaux et commerciaux sont fournis ou validés par les responsables compétents » (`carlone-offres-et-projets.md:22`) **[PR]**. Le CRM calcule pourtant, par entreprise, un « plafond de déduction » et une « économie d'impôt », avec un mail d'approche (offre-md:34) **[DR]** : à faire valider par l'expert-comptable de GianLuca Carlone avant tout envoi.
3. **Agents d'IA** : un agent qui rédige un contrat, calcule un impôt ou saisit une écriture pour le client fait **exercer par Marwin** l'activité concernée ; la limite vaut aussi pour les automatisations **[HY]**.

### Sources officielles
| Source | Organisme | Mise à jour affichée | Consultation | Citation courte |
| --- | --- | --- | --- | --- |
| Ord. n° 45-2138, art. 20 — https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000045178543 | Légifrance | En vigueur depuis le 16/02/2022 (loi n° 2022-172) | 4 nov. 2026 | « exécute habituellement des travaux prévus par les deux premiers alinéas de l'article 2 » |
| Ord. n° 45-2138 (texte consolidé, art. 2) — https://legifrance.gouv.fr/loda/id/JORFTEXT000000698851/2026-08-23 | Légifrance | Art. 2 en vigueur depuis le 08/05/2017 ; aucune modification 2025-2026 de l'art. 2 affichée | 4 nov. 2026 | « fait profession habituelle de réviser et d'apprécier les comptabilités des entreprises » |
| C. pén., art. 433-17 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000021342951 | Légifrance | (vu en extrait de recherche) | 4 nov. 2026 | 1 an d'emprisonnement et 15 000 € d'amende (reformulation) |
| Loi n° 71-1130, art. 54 — https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000039280601 | Légifrance | En vigueur depuis le 01/01/2020 (ord. n° 2019-964) — extrait de recherche | 4 nov. 2026 | Consultations juridiques et actes sous seing privé pour autrui, à titre habituel et rémunéré (reformulation) |
| Loi n° 71-1130, art. 60 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006903404 | Légifrance | Rédaction issue de la loi n° 90-1259 — extrait de recherche | 4 nov. 2026 | Qualification reconnue, consultation relevant directement de l'activité principale (reformulation) |
| Loi n° 70-9, art. 1 — https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000028806892 | Légifrance | En vigueur depuis le 27/03/2014 | 4 nov. 2026 | « d'une manière habituelle, » « se livrent ou prêtent leur concours, même à titre accessoire, » ; 6° « La gestion immobilière ; » |
| C. tourisme, art. L211-1 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000036242695 | Légifrance | En vigueur depuis le 01/07/2018 | 4 nov. 2026 | « élaborent et vendent ou offrent à la vente » ; exclusion « qu'à titre occasionnel, dans un but non lucratif et pour un groupe limité de voyageurs uniquement » |
| CPCE, art. R124-2 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000025938364 | Légifrance | En vigueur depuis le 01/01/2020 (décret n° 2019-966) | 4 nov. 2026 | « Ce compte doit être exclusivement affecté à la réception des fonds encaissés pour le compte des créanciers. » |

### Incertitudes et points à faire valider
- **Expert-comptable** : frontière exacte entre « suivi de trésorerie » et tenue de comptabilité ; statut de la paie **[IN]**.
- **Avocat** : statut des calculs fiscaux du CRM envoyés à des tiers ; rédaction de documents juridiques par des outils d'IA pour le client.
- **[IN]** Réglementation des services de paiement si Marwin manie des fonds ; régime de l'intermédiation en biens divers et des ventes d'œuvres (autre chercheur).
- **[IN]** Historique complet (Chronolégi) non ouvert pour l'art. 54 et l'art. 60 de la loi de 1971.

### Conséquences pour Marwin Tech et GianLuca Carlone
- Inscrire au contrat une **liste d'exclusions** (comptabilité, paie, conseil juridique et fiscal, gestion immobilière, vente de voyages, recouvrement, manipulation de fonds) et la règle « Marwin coordonne, le professionnel compétent exécute et signe » (accomp:101). **[PR]**
- Budget : ces professionnels sont **à la charge du client** et hors forfait ; leur coordination est dans le forfait. **[PR]**
- Pour GianLuca Carlone : un prestataire qui « s'occupe de tout » sans ces limites l'exposerait à la complicité d'exercice illégal et à des actes contestables. **[HY]**

---

## (i) Propriété intellectuelle des développements logiciels et des contenus

### Réponse courte
- **Commander et payer ne suffit pas** à rendre le client propriétaire : la conclusion d'un contrat de louage d'ouvrage ou de service « n'emporte pas dérogation » aux droits de l'auteur (CPI, L111-1). Il faut une **cession écrite** (L131-2 : « Les contrats par lesquels sont transmis des droits d'auteur doivent être constatés par écrit »). **[FV]**
- L131-3 exige que chaque droit cédé fasse l'objet d'une « mention distincte » et que le domaine d'exploitation soit délimité « quant à son étendue et à sa destination, quant au lieu et quant à la durée ». Une partie de la jurisprudence limite cette exigence stricte aux contrats de représentation, d'édition et de production audiovisuelle (Cass. civ. 1re, 21 nov. 2006, n° 05-19.294, cité par TJ Paris, 20 avr. 2023, pour un logiciel) ; **la rédiger quand même selon L131-3 est la voie prudente**. **[FV]** / **[HY]**
- « La cession globale des oeuvres futures est nulle » (L131-1) : un contrat-cadre ne peut pas céder d'avance « tout ce qui sera créé » ; il faut une cession **par livrable**, à la réception ou au paiement. **[FV]**
- L113-9 (logiciels des **employés**) ne joue **pas** entre un client et son prestataire, et ne joue pas non plus, en principe, entre Marwin et ses **dirigeants non salariés** : Marwin doit obtenir par écrit les droits de Morgan, de Mathys et de tout freelance avant de pouvoir les céder ou les concéder au client. **[HY, à valider par l'avocat]**

### Détail
1. **Rémunération** : en principe proportionnelle ; **forfaitaire possible**, notamment pour un logiciel ; une cession gratuite doit être expressément consentie (F22667, vérifiée le 3 mai 2024, page ancienne) **[FV]**. Le CRM « offert à ce jour » (offre-md:227 ; offre-md:259) devra faire l'objet d'une cession ou licence écrite, même gratuite. **[PR]**
2. **Droit moral** : perpétuel, inaliénable (F22667) **[FV]** ; il est restreint pour les logiciels (art. L121-7, non relu dans cette session) **[HY]**.
3. **État des actifs du dossier** :
   - **CRM** : construit sans facture, avant toute société (offre-md:29) ; Mathys co-auteur (contexte:26) ; 48 commits signés « Claude » (C1:265) ; dépôt FinanceScope (titulaire et visibilité à confirmer, note-point-4-novembre-et-activites.md:23) ; **aucune licence** dans `crm/` (vérifié : pas de fichier LICENSE ni de mention de droits dans `crm/README.md` et `crm/PASSATION.md`) **[FV]** ; propriétaire **[IN]** (contexte:121).
   - **Code produit avec une IA** : la protection par le droit d'auteur suppose une création originale humaine ; la part protégeable du code généré et la titularité correspondante sont **[IN]** (aucune source officielle consultée).
   - **Jarvis** : le dépôt BOJART indique : « Aucune licence globale nouvelle n'est imposée à l'œuvre, aux médias ou aux données historiques par cette consolidation. Les mentions originales des composants sont conservées » (`BOJART:jarvis/LICENSE_SCOPE.md:2`) **[FV]**. Le nom désigne aussi un livrable client (C3:247). Avant de vendre « Jarvis », inventaire des composants et de leurs licences. **[PR]**
   - **Œuvres et créations de Medhi** : elles restent à Medhi (« Ses œuvres, ses droits d'auteur, ses machines », offre-md:90) **[PR]** ; Marwin ne peut pas céder ce qu'elle ne détient pas.
   - **Bases de données** : le CRM peut aussi relever du droit du producteur de bases de données (CPI, L341-1, non relu dans cette session) **[HY]**.
4. **Architecture prévue** : « Trois registres : outils préexistants, composants réutilisables de Marwin, développements propres à Carlone, cédés ou concédés au paiement complet » (offre-md:209) **[PR]**. Elle est saine ; il manque la liste des droits cédés, la durée, le territoire, l'exclusivité, le sort des composants génériques (licence non exclusive, perpétuelle, gratuite pour l'usage interne du client) et les licences tierces (open source, IA).

### Sources officielles
| Source | Organisme | Mise à jour affichée | Consultation | Citation courte |
| --- | --- | --- | --- | --- |
| CPI, art. L131-3 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006278958 | Légifrance | En vigueur depuis le 03/07/1992 | 4 nov. 2026 | « fasse l'objet d'une mention distincte dans l'acte de cession » |
| CPI, art. L131-1 et L131-2 — https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069414/LEGISCTA000006161639/ | Légifrance | L131-2 en vigueur depuis le 01/10/2016 | 4 nov. 2026 | « La cession globale des oeuvres futures est nulle. » ; « Les contrats par lesquels sont transmis des droits d'auteur doivent être constatés par écrit. » |
| CPI, art. L113-9 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039279818 | Légifrance | En vigueur depuis le 01/01/2020 | 4 nov. 2026 | « Sauf dispositions statutaires ou stipulations contraires, les droits patrimoniaux sur les logiciels et leur documentation » |
| CPI, art. L111-1 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000042814694 | Légifrance | (vu en extrait de recherche) | 4 nov. 2026 | « n'emporte pas dérogation à la jouissance du droit reconnu par le premier alinéa » |
| TJ Paris, 20 avr. 2023, n° 21/14626 — https://www.legifrance.gouv.fr/juri/id/JURITEXT000047636347 | Légifrance | — | 4 nov. 2026 | L131-3 « ne s'applique pas aux autres contrats » (suite logicielle) |
| Fiche F22667 « Contrat de cession de droits d'auteur » — https://entreprendre.service-public.gouv.fr/vosdroits/F22667 | DILA | Vérifié le 03/05/2024 | 4 nov. 2026 | « la cession globale des œuvres futures est interdite » |

### Incertitudes et points à faire valider
- **Avocat en propriété intellectuelle** : chaîne des droits (Morgan, Mathys, freelances → Marwin → client) ; portée de L131-3 pour un contrat de développement ; droits sur le code généré par IA ; licences open source et conditions des fournisseurs d'IA.
- **[IN]** Propriétaire du CRM existant et du dépôt FinanceScope ; date et cadre du travail initial (C3:268).
- **[DR]** La fiche F22667 date de mai 2024 ; aucune réforme du droit d'auteur en 2025-2026 n'a été repérée, mais la recherche n'a pas été exhaustive.

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Avant la signature [PR]** : acte de cession de Morgan et Mathys à Marwin (ou apport) pour le CRM et les outils préexistants ; inventaire des composants et licences ; décision écrite sur le CRM « offert » (cession ou licence, avec ou sans exclusivité).
- **Au contrat [PR]** : cession par livrable à la réception et au paiement complet ; licence sur les composants génériques ; aucune cession globale des créations futures ; annexe listant les droits, la durée, le territoire et la destination.
- **Pour GianLuca Carlone** : sans écrit, il paie mais ne détient pas les droits ; il dépend de Marwin pour modifier ou faire reprendre ses outils. C'est aussi l'enjeu de la réversibilité (j). **[HY]**

---

## (j) Clause de réversibilité

### Réponse courte
- Aucun texte français général n'impose une clause de réversibilité dans un contrat de prestation : elle est **contractuelle**. **[HY]**
- Deux textes l'encadrent toutefois :
  - **RGPD, art. 28.3 g)** : à la fin de la prestation, le sous-traitant, « selon le choix du responsable du traitement, supprime toutes les données à caractère personnel ou les renvoie », et détruit les copies existantes, sauf obligation de conservation. **[FV]**
  - **Data Act (règlement (UE) 2023/2854)**, applicable depuis le **12 sept. 2025** : si Marwin fournit un **service de traitement de données** (outil hébergé exploité pour le client), le contrat doit prévoir le changement de fournisseur : préavis maximal de **deux mois**, période transitoire maximale de **trente jours**, au moins **trente jours** pour récupérer les données, effacement final ; **aucuns frais de changement à compter du 12 janvier 2027**. Les services dont la majorité des caractéristiques principales sont **conçues sur mesure** pour un client et non proposés à grande échelle sont exemptés de **certaines** de ces obligations (art. 31.1). **[FV]**
- Le diaporama promet déjà : « Réversibilité : fichiers, configurations, documentations et accès remis » (DECK/garanties.html:30) **[PR]** ; or la version autonome du CRM est hébergée « sous le compte des associés » (offre-md:37) **[DR]** : la promesse n'est pas encore tenue.

### Détail
1. **Data Act, art. 25.2** (extraits) : clauses permettant au client de passer à un autre fournisseur ou à une infrastructure sur site « sans retard injustifié et, en tout état de cause, pas après la période transitoire maximale obligatoire de trente jours calendaires » (point a) ; obligation de « concourir à la stratégie de sortie du client » (point b) ; « un délai de préavis maximal pour le lancement du processus de changement de fournisseur, qui ne dépasse pas deux mois » (point d) ; spécification exhaustive des données exportables (point e) ; « une période minimale d'au moins trente jours calendaires pour la récupération des données » (point g) ; effacement intégral (point h). Art. 29.1 : « À compter du 12 janvier 2027, les fournisseurs de services de traitement de données ne peuvent imposer aucun frais de changement de fournisseur ». Art. 31.1 : exemption partielle (art. 23 d), 29 et 30.1 et 30.3) pour les services conçus sur mesure. Art. 50 : applicable « à partir du 12 septembre 2025 ». **[FV]**
2. **Application à Marwin** **[HY]** : un CRM ou un copilote « Jarvis » hébergé et exploité par Marwin pour le client pourrait être un service de traitement de données ; s'il est développé sur mesure pour GianLuca Carlone, l'exemption de l'art. 31.1 jouerait pour une partie des obligations seulement. La qualification est à faire valider. Le plus simple est d'**éviter d'être fournisseur d'hébergement** : comptes et projets cloud au nom de l'entité cliente dès le départ, Marwin y intervenant comme collaborateur.
3. **Contenu recommandé de la clause [PR]** :
   - inventaire tenu à jour : données, documents, code, configurations, automatisations, comptes, clés d'API, sauvegardes, procédures ;
   - comptes (Firebase/Google, GitHub, fournisseurs d'IA, CRM, Notion) **au nom du client**, accès nominatifs de Marwin révocables ;
   - formats d'export ouverts et documentés ; test de restitution au moins une fois par an ;
   - assistance à la sortie chiffrée (journées), durée, interlocuteurs ; suite des licences sur les composants génériques de Marwin après la fin ;
   - suppression ou restitution des données personnelles au choix du client, avec attestation (RGPD 28.3 g) ;
   - distinguer la remise des **livrables et données** du client et la **propriété des composants génériques** de Marwin (offre-md:209).

### Sources officielles
| Source | Organisme | Mise à jour affichée | Consultation | Citation courte |
| --- | --- | --- | --- | --- |
| Règlement (UE) 2023/2854 (Data Act) — https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32023R2854 | Office des publications de l'UE (EUR-Lex) | JO UE ; texte lu le 4 nov. 2026 | 4 nov. 2026 | « qui ne dépasse pas deux mois » ; « À compter du 12 janvier 2027 » ; « Il est applicable à partir du 12 septembre 2025. » |
| Règlement (UE) 2016/679 (RGPD), art. 28.3 g) — https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32016R0679 | EUR-Lex | — | 4 nov. 2026 | « supprime toutes les données à caractère personnel ou les renvoie au responsable du traitement au terme de la prestation » |

### Incertitudes et points à faire valider
- **[HY]** Qualification de Marwin comme « fournisseur de services de traitement de données » au sens du Data Act ; portée de l'exemption sur mesure : **avocat (droit du numérique)**.
- **[IN]** Une loi française de 2024 sur le numérique (loi « SREN ») a anticipé ces règles pour l'informatique en nuage ; non vérifiée dans cette session.
- **[IN]** Qui est responsable de traitement pour le CRM (quelle entité de GianLuca Carlone) (C5:181).

### Conséquences pour Marwin Tech et GianLuca Carlone
- Transférer, **avant la signature**, le projet Firebase et le dépôt du CRM vers des comptes au nom de l'entité cliente (ou documenter le plan pour le faire), sinon la garantie montrée au client est inexacte. **[PR]**
- La réversibilité a un coût de maintenance (documentation, exports, tests) : à inclure dans le prix de l'exploitation, pas à offrir implicitement. **[PR]**
- Pour GianLuca Carlone : c'est la garantie qui rend acceptable la dépendance à un petit prestataire. **[HY]**

---

## Questions courtes à poser aux professionnels

**Avocat (travail, contrats, PI, numérique)**
1. Le contrat-cadre, la convention de bureaux et le mode de commande écartent-ils suffisamment le lien de subordination (L8221-6 II) ? Quels indices supprimer ?
2. Un salariat d'un fondateur chez une entité de GianLuca Carlone est-il compatible avec la prestation de Marwin, et à quelles conditions (fonctions, PI, conflit d'intérêts) ?
3. Quelle durée de préavis prévoir pour respecter L442-1 II dans les deux sens ?
4. Plafond de responsabilité et exclusions acceptables ; contrat négocié ou d'adhésion ?
5. Rédaction des mandats par entité ; responsabilité de Marwin envers les tiers.
6. Chaîne des droits sur le CRM, Jarvis et le code produit avec IA ; portée de L131-3 pour un contrat de développement.
7. Marwin est-elle un fournisseur de services de traitement de données (Data Act) ?
8. Les calculs fiscaux du CRM envoyés aux prospects relèvent-ils de la consultation (loi 1971, art. 54) ?

**Expert-comptable**
9. Traitement TVA des achats pour le client (débours ou refacturation) ; comptes de passage.
10. Frontière entre suivi de trésorerie et tenue de comptabilité ; statut de la paie.
11. Effets fiscaux et sociaux d'une éventuelle requalification.

**Urssaf**
12. À partir de quand une société nouvellement créée obtient-elle une attestation de vigilance ?

**Assureur ou courtier**
13. RC professionnelle couvrant le pilotage, le développement, l'IA et les données ; assurance des locaux mis à disposition.

---

## Tableau récapitulatif

Niveau de certitude : **élevé** = texte en vigueur vérifié sur Légifrance, EUR-Lex ou service-public le 4 nov. 2026 ; **moyen** = texte vérifié mais application au cas Marwin = interprétation, ou source partiellement lue ; **faible** = source secondaire, extrait de recherche ou non vérifié.

| Règle | Valeur ou condition | Source | Certitude |
| --- | --- | --- | --- |
| Présomption de non-salariat | Dirigeants de sociétés immatriculées présumés non salariés ; renversée par une subordination juridique permanente, même par personne interposée | C. trav. L8221-6 (en vigueur depuis le 01/01/2023) | Élevé |
| Présomption d'indépendance | Conditions de travail définies par le travailleur ou par le contrat avec le donneur d'ordre | C. trav. L8221-6-1 | Élevé |
| Lien de subordination | Pouvoir de donner des ordres et directives, contrôler, sanctionner ; service organisé = indice si conditions fixées unilatéralement | Cass. soc. 13/11/1996 n° 94-13.187 ; 04/03/2020 n° 19-13.316 | Élevé (règle) / moyen (application au cas) |
| Travail dissimulé | 3 ans et 45 000 € ; 225 000 € pour une société | C. trav. L8224-1 ; F31490 (03/07/2026) | Élevé |
| Prêt illicite de main-d'œuvre | Interdit si but lucratif et objet exclusif ; 2 ans et 30 000 € (version du 27/06/2026) ; 150 000 € pour une société | C. trav. L8241-1, L8243-1 ; F31490 | Élevé |
| Marchandage | Fourniture lucrative de main-d'œuvre causant préjudice ou éludant la loi ; 2 ans et 30 000 € (version du 27/06/2026) | C. trav. L8231-1, L8234-1 | Élevé |
| Critères prestation réelle / prêt | Tâche définie et savoir-faire propre, encadrement par le prestataire, prix lié au résultat | Jurisprudence (Cass. crim. 2020 publié ; autres arrêts vus en extraits) | Moyen |
| Vigilance : seuil | Contrat ≥ 5 000 € HT | C. trav. R8222-1 | Élevé |
| Vigilance : périodicité et pièces | À la conclusion puis tous les 6 mois ; attestation Urssaf < 6 mois vérifiée + justificatif d'immatriculation | C. trav. D8222-5 (01/01/2023) | Élevé |
| Vigilance : sanctions | Solidarité financière ; annulation des réductions du donneur d'ordre, plafond 15 000 € / 75 000 € sans antécédent sur 5 ans | C. trav. L8222-2 ; CSS L133-4-5 | Élevé |
| Vigilance sur les sous-traitants (nouveau) | Maître d'ouvrage vérifie les sous-traitants acceptés ; entrée en vigueur prévue 26-27 déc. 2026 | C. trav. L8222-1-1 (loi 2026-534) ; F31490 | Moyen (date exacte) |
| Offre Marwin soumise à vigilance | 15 000 € × 6 = 90 000 € HT | offre-md:13 ; offre-md:195 | [ES] élevé |
| Cumul d'emplois | 10 h/jour, 48 h/semaine (activités salariées seulement) ; amende 1 500 € (3 000 € récidive) | F1945 (21/06/2023) | Moyen (page ancienne) |
| Loyauté du salarié | Activité concurrente = faute grave, même sans clause de non-concurrence | Cass. soc. 14/01/2026 n° 24-20.799 (A18850) | Élevé |
| Clause d'exclusivité et création d'entreprise | Levée 1 an (jusqu'à 2 ans) à compter de l'immatriculation | F1945 | Moyen |
| Représentant contractant avec lui-même | Acte nul sauf autorisation ou ratification (représentation de personnes physiques) | C. civ. 1161 (01/10/2018) | Élevé |
| Logiciels des salariés | Droits patrimoniaux à l'employeur, sauf stipulation contraire | CPI L113-9 (01/01/2020) | Élevé |
| Rupture brutale | Préavis écrit tenant compte de la durée ; 18 mois = protection contre la contestation de durée ; exceptions inexécution et force majeure | C. com. L442-1 II (version du 20/08/2026) | Élevé |
| Relation établie | Possible malgré des CDD successifs si poursuite raisonnablement anticipée | Cass. com. 19/03/2025 n° 23-22.182 | Élevé (règle) / faible (pour une relation de 6 mois) |
| Abus de dépendance économique | Suppose un effet sur la concurrence | C. com. L420-2 al. 2 (extrait) | Faible |
| RC professionnelle | Non obligatoire en général ; obligatoire pour certaines activités réglementées ; assurance obligatoire du local si locataire | F37365 (07/07/2026) | Élevé |
| Limitation de responsabilité | Inopposable en cas de faute lourde ou dolosive ; non écrite si elle vide l'obligation essentielle ; déséquilibre significatif (contrat d'adhésion) | C. civ. 1231-3, 1170, 1171 | Élevé |
| Mandat | Écrit possible même par lettre ; mandat général = actes d'administration ; rien au-delà du mandat ; responsabilité pour faute ; reddition de compte | C. civ. 1984-1993, 1988 | Élevé |
| Acte hors pouvoir | Inopposable au représenté, sauf mandat apparent | C. civ. 1156 | Élevé |
| Débours (TVA) | Au nom et pour le compte du mandant ; reddition de compte ; justification ; comptes de passage ; mandat préalable explicite | BOFiP BOI-TVA-BASE-10-10-30 (11/05/2022) § 200, 220 | Élevé (règle) / moyen (application) |
| Expertise comptable | Tenue et révision habituelles des comptabilités réservées ; délit (peines de 433-17 : 1 an, 15 000 €) | Ord. 45-2138 art. 2 et 20 ; C. pén. 433-17 | Élevé (texte) / moyen (frontière avec le suivi de trésorerie) |
| Consultation juridique | Habituelle et rémunérée pour autrui : réservée ; exception art. 60 si qualification reconnue | Loi 71-1130 art. 54 et 60 (extraits) | Moyen |
| Gestion immobilière (Hoguet) | Concours habituel, même accessoire, aux opérations sur les biens d'autrui | Loi 70-9 art. 1 (27/03/2014) | Élevé |
| Vente de voyages et séjours | Élaborer et vendre des forfaits : régime du Code du tourisme ; exclusion occasionnelle non lucrative pour un groupe limité | C. tourisme L211-1 (01/07/2018) | Élevé |
| Recouvrement amiable | Assurance RC pro, compte affecté, déclaration au procureur | CPCE R124-2 (01/01/2020) | Élevé |
| Cession de droits d'auteur | Écrit ; mention distincte et domaine délimité (étendue, destination, lieu, durée) ; portée stricte discutée hors L131-2 al. 1 | CPI L131-2, L131-3 ; TJ Paris 20/04/2023 | Élevé (texte) / moyen (portée) |
| Œuvres futures | Cession globale nulle | CPI L131-1 | Élevé |
| Commande ≠ cession | Le contrat de service n'emporte pas dérogation aux droits de l'auteur | CPI L111-1 (extrait) | Moyen |
| Fin de sous-traitance RGPD | Suppression ou restitution au choix du responsable ; destruction des copies | RGPD art. 28.3 g) | Élevé |
| Data Act : changement de fournisseur | Préavis ≤ 2 mois ; transition ≤ 30 jours ; récupération ≥ 30 jours ; applicable depuis le 12/09/2025 | Règl. (UE) 2023/2854 art. 25, 50 | Élevé (texte) / moyen (applicabilité à Marwin) |
| Data Act : frais de changement | Interdits à compter du 12/01/2027 ; exemption partielle pour services sur mesure | Règl. (UE) 2023/2854 art. 29, 31 | Élevé |
| Attestation de vigilance d'une société nouvelle | Délai de délivrance | — | [IN] |
| Statut de la paie au regard du monopole comptable | — | — | [IN] |
| Protection du code généré par IA | — | — | [IN] |
