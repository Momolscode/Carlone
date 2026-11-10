# R6 : repères de marché 2025-2026 pour fixer et défendre un prix

Chercheur : « R6-marche ». Mémo rédigé le 4 novembre 2026. Toutes les pages web ont été consultées le 4 nov. 2026. Le client s'appelle **GianLuca Carlone**.

## 0. Méthode, limites et lecture

**Codes utilisés.** [FV] fait vérifié dans une source primaire ou un fichier · [DR] déclaration rapportée · [PR] proposition · [HY] hypothèse · [ES] estimation ou calcul non validé · [MM] mesure · [IN] inconnu.

**Ce qu'il faut savoir avant de lire les chiffres.**
- Les prix de marché (TJM, centres d'appels, missions à temps partagé) ne sont publiés par **aucun organisme officiel**. Les seules références publiques sont des études de cabinets ou de plateformes (Hays, Kicklox/RH Solutions, APEC, France Transition) et des agrégateurs commerciaux. Chaque fois qu'une source est secondaire, je l'écris.
- Sources officielles réellement utilisées : URSSAF (simulateur et API publique de mon-entreprise.urssaf.fr), entreprises.gouv.fr (plan « Osez l'IA »), les-aides.fr (réseau des CCI), l'API publique Recherche d'entreprises (data.gouv.fr, DINUM, source de l'Annuaire des Entreprises), la Banque centrale européenne (taux de change), et, vus seulement dans des résultats de recherche, info.gouv.fr et economie.gouv.fr (pages refusées en lecture directe, erreur 403).
- Pages **inaccessibles** pendant la recherche : baromètre Malt (403), page TJM de Free-Work (non trouvée), page de prix ChatGPT d'OpenAI (403), pages de prix HubSpot, Ringover et Aircall (contenu non chargé ou 404), Insee « Salaires et revenus d'activité » par région et département (erreur 500), NVIDIA Marketplace (503). Les chiffres correspondants viennent donc de sources secondaires et sont marqués comme tels.
- Conversion des prix en dollars : taux de référence BCE du 4 nov. 2026, **1 € = 1,1267 USD** [FV] (https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml). Les conversions sont des [ES].
- Aucune personne ni entreprise n'a été contactée. Je n'ai rien acheté ni modifié dans le dépôt. Les seules requêtes vers des services publics sont des lectures et des calculs du simulateur URSSAF.

**Pièces du dépôt confrontées au marché.** Les chemins `slides/…` désignent le diaporama client, dans `[diaporama Offre Marwin Tech, copie du 4 nov.] slides/`, version du 4 nov. 2026.
- Taux de 750 € HT la journée-personne et formules à 15 000 € et 30 000 € HT par mois : `interne/offre-marwin-tech-remuneration-et-collaboration.md:13-18`, `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:64`, diaporama client `slides/formules.html:30`.
- Justification déjà rédigée du taux : `interne/audit-marwin-tech-carlone.md:66-87`.
- Argument « deux salariés coûteraient 1,6 à 1,9 fois leur net » : `interne/offre-marwin-tech-remuneration-et-collaboration.md:254`.
- Option laboratoire à 30 000 € HT, dont 13 500 € d'honoraires pour 18 journées : diaporama `slides/laboratoire.html`.
- DGX Spark : `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:127-131`, `interne/complement-chatgpt-2026-11-04.md:37`.
- Quali Contact et téléphonie : `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:7`, `crm/PASSATION.md:46`, `interne/audit-marwin-tech-carlone.md:101`.

---

## (a) TJM des consultants indépendants par métier

### Réponse courte
- **Chef de projet / PMO** : 550 à 760 € HT par jour en région pour un profil confirmé à senior. Moyenne nationale « gestion de projets » : 698 € (étude Kicklox 2025). [FV] dans les études citées, [ES] pour la transposition régionale.
- **Consultant en organisation / management** : médiane d'environ 600 € (fourchette 400 à 1 000 €). Sources secondaires.
- **Directeur des opérations à temps partagé (« COO fractionné »)** : aucune étude française trouvée [IN]. Repères voisins, tous secondaires : management de transition, environ 1 330 € HT par jour en moyenne (S1 2025) ; DAF à temps partagé, 800 à 1 200 € HT par jour.
- **Consultant IA / automatisation** : 650 à 1 500 € selon les sources commerciales, sans source solide. Seul repère public fiable : le Diag Data IA de Bpifrance, **10 000 € HT pour 8 jours-hommes, soit 1 250 € HT par jour d'expert** [FV] (voir (e)).
- **Développeur** : 450 à 650 € (médiane d'environ 485 €). Environ 10 % de moins en région qu'à Paris.
- **Le taux de 750 € HT de Marwin** se situe en haut de la fourchette chef de projet en région et au-dessus de la moyenne des seniors de l'étude Kicklox (643 €). Il est sous les repères « direction à temps partagé » et « expert IA », et très au-dessus de toute tâche d'exécution administrative. [ES]

### Détail

**1. Étude primaire Kicklox / RH Solutions / Didaxis 2025, la seule enquête avec méthode publiée** (663 réponses complètes de freelances tech, questionnaire diffusé du 3 juin au 15 juillet 2025) [FV] (PDF p. 5) :

| Repère | TJM moyen | Source |
|---|---|---|
| Junior (0 à 4 ans) | 268 € | PDF p. 12 (graphique) |
| Avancé (5 à 10 ans) | 462 € | PDF p. 12 |
| Senior (11 ans et plus) | 643 € | PDF p. 12 |
| Île-de-France | 613,25 € | PDF p. 13 |
| Province | 582,23 € (« écart de seulement 5 % ») | PDF p. 13 |
| Gestion de projets | 698 € | PDF p. 14 |
| IT et logiciel | 629 € | PDF p. 14 |
| Data | 533 € | PDF p. 14 |
| Évolution annuelle | 80 % des répondants : hausse inférieure à 3 % par an | PDF p. 16 |

Remarque : le « 613 € en Île-de-France » repris dans `interne/audit-marwin-tech-carlone.md:80` est en réalité la moyenne Île-de-France de cette étude, tous métiers tech confondus [FV].

**2. Hays, étude des rémunérations 2026, relayée par le Blog du Modérateur** (article du 29 janv. 2026 ; TJM à Paris, HT ; panel annoncé de plus de 2 500 professionnels). Source secondaire, étude Hays non lue directement :

| Métier | 0 à 3 ans | 3 à 5 ans | 5 à 8 ans | 8 ans et plus | Écart en région |
|---|---|---|---|---|---|
| Chef de projet | 600 € | 680 € | 730 € | 800 € | environ −5 % |
| Développeur full-stack | 450 € | 515 € | 580 € | 650 € | environ −10 % |
| Data engineer | 480 € | 590 € | 660 € | 700 € | environ −9 % |

Transposition à la Bourgogne-Franche-Comté [ES] : chef de projet de 570 à 760 € ; développeur full-stack de 405 à 585 €.

**3. Agrégateur « Baromètre TJM freelance 2026 », freelance-solution.fr** (publié et mis à jour en juin 2026). C'est la source déjà citée dans `interne/audit-marwin-tech-carlone.md:70-80`. J'ai vérifié que les chiffres repris dans le dépôt correspondent à la page [FV]. La page consolide d'autres études et contient des liens affiliés : c'est une source secondaire.

| Métier | Médiane | Fourchette | Origine déclarée |
|---|---|---|---|
| Développeur | ≈ 485 € | 350 à 650 € | RH Solutions / TJMètre 2026 |
| Chef de projet / product manager | ≈ 595 € | 450 à 800 € | TJMètre / RH Solutions 2026 |
| Consultant (stratégie, management) | ≈ 629 € | 400 à 1 000 € | RH Solutions 2026 |
| Data scientist / engineer | ≈ 620 € | 470 à 900 € | FreelanceRepublik / Jobbers |
| IA, IA générative | non chiffrée en médiane | 750 à 1 500 € (« top 5 ») | sans source précise |
| Écart en région | « 15 à 30 % » de moins à compétences égales | | RH Solutions 2026 |

Contradiction entre sources : l'étude primaire Kicklox mesure un écart province / Île-de-France d'environ 5 %, et Hays de 5 à 10 %. Les 15 à 30 % de l'agrégateur ne sont pas retrouvés dans les sources primaires lues.

**4. Grille par expérience, mondedutravail.fr** (article du 10 avril 2026, sources mêlées dont le « baromètre Malt 2025 », secondaire) : chef de projet IT confirmé de 450 à 600 €, senior de 600 à 850 € ; consultant RH / management confirmé de 450 à 650 €, senior de 650 à 900 € ; développeur web confirmé de 400 à 550 €. Médiane Malt 2025 citée : « autour de 450 € pour les profils confirmés ». **Le baromètre Malt lui-même n'a pas pu être lu (403) [IN].**

**5. Direction à temps partagé et management de transition.** Aucune étude française n'isole le « directeur des opérations à temps partagé » [IN]. Repères voisins :
- Management de transition : TJM moyen 2025 de **1 330 € HT**, attribué au « Baromètre France Transition, S1 2025 », avec 55 % des missions entre 1 000 et 1 500 € (plateya.fr, 25 oct. 2025, source secondaire, baromètre original non lu).
- Infographie LHH, qui cite le même baromètre : les fonctions « Opérations / Supply Chain » représentent **13 %** des demandes de management de transition, et le « management relais » 43 % des missions [FV] (PDF de l'infographie LHH, fichier daté du 12 juin 2026).
- Temps partagé : selon plateya.fr, le TJM est « parfois légèrement majoré (+10 à 20 %) », mais le même article évoque une décote de 5 à 10 % négociable. Les deux sens se contredisent.
- DAF à temps partagé, profil le plus proche du COO fractionné en PME : **800 à 1 200 € HT par jour** (companeo.com, vendeur du service).
- Le dépôt envisage déjà ce rôle : « Une fonction de direction des opérations pourra se négocier avec John-Lucas [sic, lire GianLuca] » (`interne/recueil-sessions-chatgpt-2026-11-04.txt:237`) [PR].

### Sources

| Source | Organisme | Statut | Date de la page | Citation courte |
|---|---|---|---|---|
| https://www.rh-solutions.com/app/uploads/2025/12/RHS-Etude-2025-les-TJM-freelances_compressed.pdf | Kicklox, RH Solutions, Didaxis (groupe privé) | Étude primaire privée | PDF créé le 14 oct. 2025 | « 663 réponses complètes ont été recueillies et analysées » (p. 5) ; « Gestion de projets (698 €) » (p. 14) |
| https://www.blogdumoderateur.com/freelance-tech-taux-journaliers-moyens-metier-2026/ | Blog du Modérateur, d'après Hays | Secondaire | 29 janv. 2026 | Chef de projet : 600 € à 800 € selon l'expérience, à Paris |
| https://www.freelance-solution.fr/barometre-tjm-freelance-2026/ | freelance-solution.fr | Secondaire, agrégateur avec liens affiliés | Juin 2026 | « L'Île-de-France reste en tête avec un TJM moyen d'environ 613 €/jour » |
| https://mondedutravail.fr/comment-fixer-tarifs-freelance/ | mondedutravail.fr | Secondaire | 10 avr. 2026 | « autour de 450 € pour les profils confirmés (baromètre Malt 2025) » |
| https://plateya.fr/blog/detail/cout-du-management-de-transition-combien-ca-coute-vraiment | plateya.fr | Secondaire, plateforme commerciale | 25 oct. 2025 | « TJM moyen en 2025 : 1 330 € HT/jour » |
| https://www.lhh.com/-/jssmedia/project/lhh/lhhfr/pdf/france,-infographie-(1).pdf | LHH, d'après France Transition | Secondaire | Fichier daté du 12 juin 2026 | « Opérations / Supply Chain (13%) » ; « Source : Baromètre France Transition, S1 2025 » |
| https://www.companeo.com/comptabilite-externalisee-expert-comptable/guide/directeur-financier-tpe-pme-temps-partage | Companeo | Secondaire, vendeur | Non affichée | 800 € à 1 200 € HT par jour (extrait de recherche) |

Aucune source officielle (administration) ne publie de TJM. **Le niveau de certitude de toute cette partie est moyen à faible.**

### Incertitudes et points à faire valider
- Le baromètre Malt et les données TJM de Free-Work n'ont pas été lus directement [IN].
- Aucune donnée TJM n'est spécifique à la Nièvre ou à la Bourgogne-Franche-Comté [IN]. La décote régionale va de 5 % (Kicklox, Hays) à 30 % (agrégateur).
- L'ancienneté réelle et les références démontrables de Morgan Olsen et de Mathys Couet ne sont pas documentées [IN]. Or c'est le premier facteur de prix : de 268 € (junior) à 643 € (senior) dans l'étude Kicklox.
- Ni COO fractionné ni PMO externalisé ne font l'objet d'une étude française [IN].
- À valider : aucun organisme officiel n'est compétent. À recouper par deux ou trois devis concurrents, par exemple d'un PMO freelance régional et d'un manager de transition.

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Le taux de 750 € HT se défend pour un rôle de chef de projet senior ou de PMO** (Hays 8 ans et plus : 800 € à Paris, environ 760 € en région [ES]). Il ne se défend que si Marwin montre l'expérience et les preuves d'un senior. Face à la moyenne des seniors Kicklox (643 €), il est 17 % plus cher [ES].
- **Ce taux est un taux d'équipe appliqué à deux personnes.** Une journée de Mathys et une journée de Morgan sont facturées pareil, quel que soit le travail. Si GianLuca compare chaque journée à un développeur (450 à 585 € en région) ou à une tâche administrative, le taux est exposé. Cela confirme `interne/audit-marwin-tech-carlone.md:69` (« mal pour l'administratif »).
- **Pour le volet « direction des opérations », le marché pratique plutôt 800 à 1 500 € par jour, mais sur 2 à 8 jours par mois**, pas 20 jours [HY]. Marwin peut s'en servir pour défendre la valeur de la coordination. Il ne peut pas s'en servir pour justifier un volume de 20 journées-personnes.
- **Pour l'IA**, le seul repère public solide est le Diag Data IA (1 250 € HT par jour d'expert habilité). Il montre que 750 € n'est pas excessif pour un travail d'expertise IA. Il rappelle aussi qu'un dispositif subventionné existe et que GianLuca peut le comparer à l'offre de Marwin (voir (e)).

---

## (b) Coût employeur d'un assistant de direction, d'un chef de projet et d'un office manager en Nièvre

### Réponse courte
- **Aucune médiane officielle par métier pour la Nièvre ou la Bourgogne-Franche-Comté n'a pu être lue** : l'Insee renvoyait une erreur 500 et France Travail ne publie pas de salaire sous forme lisible [IN].
- Meilleure source primaire : **APEC 2025, médianes des cadres dans les « autres régions »** (hors Île-de-France), fixe et variable compris [FV] :
  - assistanat de direction : 41 k€ brut par an (fourchette 30 à 53 k€) ;
  - conseil en organisation : 46 k€ (37 à 73 k€) ;
  - gestion de projets informatiques : 52 k€ (39 à 73 k€) ;
  - direction d'entreprise : 70 k€ (42 à 132 k€).
- Les postes non cadres (assistant de direction, office manager en petite structure) n'ont pas de médiane régionale publique [IN]. Plancher légal : SMIC de **1 867,02 € brut par mois depuis le 1er juin 2026** [FV].
- **Coût total employeur calculé avec l'API du simulateur URSSAF** le 4 nov. 2026 (CDI à temps plein, établissement dans la Nièvre, entreprise de 5 salariés, sans mutuelle ni frais annexes) [ES sur une source officielle] :
  - assistant de direction non cadre (2 000 à 2 600 € brut par mois) : **2 250 à 3 340 € par mois**, soit 27 à 40 k€ par an ;
  - office manager (2 300 à 2 900 € brut) : **2 810 à 3 840 € par mois**, soit 34 à 46 k€ par an ;
  - chef de projet cadre (3 833 à 4 333 € brut, médianes régionales APEC) : **5 380 à 6 150 € par mois**, soit 65 à 74 k€ par an.

### Détail

**1. Médianes APEC 2025 des cadres** (« Les rémunérations des cadres dans 111 familles de métiers », édition 2025, PDF créé le 10 déc. 2025). Rémunération annuelle brute, fixe et variable compris, en k€ : 1er décile / médiane / 9e décile [FV].

| Famille de métiers | France entière | Autres régions (hors IDF) | Entreprises de moins de 250 salariés | Source |
|---|---|---|---|---|
| Ensemble des cadres | 38 / **55** / 95 | n.d. | n.d. | PDF p. 1 |
| Assistanat de direction | 35 / **47** / 64 | 30 / **41** / 53 | 33 / **47** / 61 | PDF p. 9 |
| Conseil en organisation et stratégie | 40 / **57** / 86 | 37 / **46** / 73 | 40 / **55** / 85 | PDF p. 13 |
| Gestion de projets informatiques (dont chef de projet, PMO) | 41 / **57** / 79 | 39 / **52** / 73 | 39 / **54** / 78 | PDF p. 53 |
| Direction d'entreprise | 45 / **76** / 150 | 42 / **70** / 132 | 45 / **72** / 141 | PDF p. 42 |

Les valeurs « autres régions » et « moins de 250 salariés » sont lues sur les graphiques à barres, à partir de la couche texte du PDF.

**2. Repères nationaux privés (secondaires, non régionaux)** : assistant de direction, médiane d'environ 44 000 € brut par an (Michael Page 2026, page du cabinet relevée par recherche) ; office manager, médiane de 49 500 € brut par an (Hays 2026, relayé par le Journal du Net). Ce sont des médianes de cabinets de recrutement, tirées vers le haut par l'Île-de-France. Elles ne valent pas pour une petite structure nivernaise [HY].

**3. Paramètres sociaux 2026 constatés dans le simulateur URSSAF** [FV] :
- SMIC horaire de 12,31 €, soit 1 867,02 € par mois (valeur du simulateur, date de référence du modèle 01/07/2026). Le SMIC était de 12,02 € au 1er janvier 2026 et a été revalorisé de 2,41 % au 1er juin 2026 (info.gouv.fr, vu en résultat de recherche).
- Plafond de la sécurité sociale (PSS) 2026 : 4 005 € par mois.
- **Changement 2026** : la réduction générale dégressive unique (RGDU) remplace l'ancienne réduction générale (ex-Fillon) à partir du 1er janvier 2026. Paramètres secondaires relevés : Tmin 0,02, puissance 1,75, réduction nulle à 3 SMIC. Selon des sources professionnelles (Gazette du Palais, Tissot), le barème reste calculé sur le SMIC de 12,02 € toute l'année 2026 (« gel du barème »). Mon recalcul du coefficient sur 2 000 € brut retrouve exactement la valeur de l'URSSAF avec 12,02 € [ES]. **À confirmer sur urssaf.fr par l'expert-comptable.**

**4. Coût employeur calculé (API URSSAF, 4 nov. 2026)** [ES] : CDI à temps plein, Nièvre, effectif de 5, aucune convention collective renseignée, mutuelle, titres-restaurant et transport non renseignés.

| Profil (hypothèse de salaire) | Brut mensuel | Net avant impôt | Dont RGDU déduite | Coût employeur mensuel | Coût annuel (×12) | Coût / brut | Coût / net |
|---|---|---|---|---|---|---|---|
| Plancher légal (SMIC, non cadre) | 1 867 € | 1 456 € | n.c. | 1 988 € | 23,9 k€ | 1,06 | 1,37 |
| Assistant de direction, bas de fourchette | 2 000 € | 1 561 € | 629 € | 2 249 € | 27,0 k€ | 1,12 | 1,44 |
| Assistant de direction ou office manager | 2 300 € | 1 799 € | 499 € | 2 808 € | 33,7 k€ | 1,22 | 1,56 |
| Office manager confirmé | 2 600 € | 2 036 € | 399 € | 3 336 € | 40,0 k€ | 1,28 | 1,64 |
| Office manager senior | 2 900 € | 2 274 € | 322 € | 3 842 € | 46,1 k€ | 1,32 | 1,69 |
| Assistant de direction cadre (APEC région, 41 k€) | 3 417 € | 2 677 € | n.c. | 4 729 € | 56,7 k€ | 1,38 | 1,77 |
| Consultant en organisation cadre (APEC région, 46 k€) | 3 833 € | 3 006 € | n.c. | 5 382 € | 64,6 k€ | 1,40 | 1,79 |
| Chef de projet cadre (APEC région, 52 k€) | 4 333 € | 3 399 € | n.c. | 6 149 € | 73,8 k€ | 1,42 | 1,81 |
| Directeur, cadre dirigeant salarié (APEC région, 70 k€) | 5 833 € | 4 602 € | n.c. | 8 428 € | 101,1 k€ | 1,44 | 1,83 |

« n.c. » : non calculé. Le passage de 2 000 € à 2 300 € brut augmente le coût de 559 € par mois, parce que la RGDU diminue vite au-dessus du SMIC. C'est une propriété de la réforme de 2026 [ES].

**Coût d'une journée de travail salariée** [ES] : un chef de projet cadre régional coûte 73,8 k€ par an, à répartir sur 205 à 218 jours réellement travaillés (forfait jours, congés, formation, absences) [HY], soit **environ 340 à 360 € par jour**. Ce coût n'inclut ni poste de travail, ni logiciels, ni encadrement, ni recrutement, ni vacance de poste.

### Sources

| Source | Organisme | Statut | Date de la page | Citation courte |
|---|---|---|---|---|
| https://mon-entreprise.urssaf.fr/api/v1/evaluate (API du simulateur ; interface : https://mon-entreprise.urssaf.fr/simulateurs/salaire-brut-net) | URSSAF | **Officielle** | Modèle daté du 01/07/2026 (valeur « date » de l'API) | Réponses chiffrées : « salarié . coût total employeur » ; « SMIC . horaire » = 12,31 |
| https://corporate.apec.fr/files/live/sites/corporate/files/Nos%20etudes/PDF/Les%20remunerations%20des%20cadres%20dans%20111%20familles%20de%20metiers%202025.pdf | APEC (organisme paritaire) | Étude primaire, non administrative | Édition 2025, PDF du 10 déc. 2025 | « La rémunération médiane des cadres en poste (salaire fixe + part variable) s'établit à 55 k€ » |
| https://www.info.gouv.fr/actualite/le-smic-revalorise-le-1er-juin-2026 | Gouvernement | Officielle, vue en extrait de recherche (lecture directe refusée, 403) | Non lue | « SMIC horaire brut : 12,31 euros (contre 12,02 euros au 1er janvier 2026) » |
| https://bpifrance-creation.fr/encyclopedie/gerer-lentreprise/aides-au-recrutement/rgdu-reduction-generale-degressive-unique-ex | Bpifrance Création | Parapublique, secondaire | Non lue en détail | Intitulé : « RGDU : réduction générale dégressive unique (ex- réduction Fillon) » |
| https://www.labase-lextenso.fr/gazette-du-palais/2026-n20/revalorisation-du-smic-au-1er-juin-2026-et-gel-du-bareme-des-allegements-generaux-GPL492b6 | Gazette du Palais | Secondaire juridique | 2026, n° 20 | Titre : « revalorisation du smic au 1er juin 2026 et gel du barème des allègements généraux » |
| https://www.michaelpage.fr/recrutement/tendances-rh/salaire-moyen-d-un-assistant-de-direction | Michael Page | Secondaire, cabinet | Mai 2026 (selon l'extrait de recherche) | « environ 44 000 euros bruts par an » |

### Incertitudes et points à faire valider
- Pas de médiane régionale non cadre pour ces trois métiers [IN]. Les salaires de 2 000 à 2 900 € brut retenus pour les postes non cadres sont des **hypothèses** [HY]. Seuls le plancher (SMIC) et les médianes cadres APEC « autres régions » sont vérifiés.
- La convention collective applicable chez l'employeur (minima, prévoyance, 13e mois) n'est pas connue [IN]. La mutuelle obligatoire (part employeur au moins égale à 50 %), la prévoyance conventionnelle, les titres-restaurant, le transport et la médecine du travail ne sont pas inclus. Ils ajoutent [IN] au coût, à chiffrer par l'expert-comptable.
- Les montants APEC divisés par 12 supposent l'absence de 13e mois [HY].
- À faire valider par l'**expert-comptable ou le gestionnaire de paie** : paramètres RGDU 2026, taux AT/MP réel, versement mobilité selon la commune et l'effectif, convention collective.
- L'Insee (« Salaires et revenus d'activité en 2023 », par région et par département) est à relire quand le site répondra.

### Conséquences pour Marwin Tech et GianLuca Carlone
- **15 000 € HT par mois, c'est 180 000 € par an** [PR]. Cela représente le coût employeur d'environ 2,4 chefs de projet cadres régionaux, de 5,3 assistants non cadres à 2 300 € brut, ou de 1,8 directeur salarié à la médiane régionale APEC [ES]. GianLuca peut faire ce calcul. Marwin doit donc vendre ce qu'un salarié n'apporte pas : outils et CRM déjà construits, capacité modulable, méthode, absence de recrutement et de risque social, réversibilité.
- **Une journée Marwin à 750 € vaut environ 2,1 fois le coût d'une journée de chef de projet salarié en région** (340 à 360 €) [ES]. Ce rapport est courant entre indépendant et salarié [HY], mais il doit être dit, et non découvert par le client.
- **L'argument du dépôt « 1,6 à 1,9 fois le net »** (`interne/offre-marwin-tech-remuneration-et-collaboration.md:254`) est juste pour un profil qualifié (1,64 à 1,83 selon l'URSSAF, avant mutuelle et frais). Il est faux pour un poste proche du SMIC (1,37 à 1,56), où la RGDU 2026 allège fortement le coût. Il faut **corriger cet argument** : pour les tâches administratives, un assistant local revient à 2 250 à 2 810 € par mois, et la comparaison se retourne contre Marwin [ES].
- Cela renforce la recommandation de sortir l'exécution administrative du taux de 750 € (`interne/audit-marwin-tech-carlone.md:100`) : Marwin outille et pilote, un salarié de GianLuca exécute.

---

## (c) Centres d'appels externalisés pour la prospection B2B, et ce qu'on sait publiquement de Quali Contact

### Réponse courte
- **Tarifs** : aucune statistique publique française [IN]. Sources commerciales (secondaires) :
  - rendez-vous B2B qualifié livré : **150 à 500 € HT par rendez-vous tenu** (200 à 400 € selon un autre prestataire) ;
  - SDR (téléprospecteur) externalisé : **3 000 à 8 000 € par mois**, avec un engagement d'au moins 6 mois ;
  - tarif horaire en Belgique : 35 à 45 € par heure (pas un repère français).
- **Quali Contact** [FV] (registre public) : SAS **QUALI CONTACT, SIREN 394 573 497**, active, créée le 1er avril 1994. Siège à Clichy (92). Un **établissement actif à Cosne-Cours-sur-Loire** (ZA du Parc, 30-32 rue Eugène Perreau, 58200), ouvert le 15 août 2000. Code d'activité NAF 73.20Z (« Études de marché et sondages »). Effectif de 50 à 99 salariés (tranche 2024), catégorie PME. Président : CALOGERO SAS. Convention collective IDCC 2098.
- **Activité affichée sur son site** [FV] : « Agence multimedia spécialisée en Fundraising ». Campagnes d'appels sortants et entrants « pour le secteur caritatif ». Le site ne mentionne **ni prospection B2B ni tarifs**.

### Détail

**1. Prix de la prospection téléphonique externalisée** (toutes les sources sont secondaires) :

| Modèle de facturation | Fourchette | Source | Remarque |
|---|---|---|---|
| Au rendez-vous tenu | 150 à 500 € HT | derrick-app.com, comparatif 2026 | Comparer au coût par rendez-vous **tenu**, définition du rendez-vous à écrire |
| Rendez-vous B2B qualifié « tout compris » | 200 à 400 € | cocowork.fr, blog de prestataire | Selon la difficulté de la cible |
| Coût par lead qualifié | 34 à 48 € en externe, 65 à 80 € en interne | cocowork.fr | Unité différente du rendez-vous |
| SDR externalisé (forfait) | 3 000 à 8 000 € par mois, 6 mois minimum | derrick-app.com | |
| Journée d'appels | environ 300 à 455 $ par jour pour 100 à 120 appels | comeup.com (offre de vendeur) | Devise mélangée, offre isolée |
| À l'heure (Belgique) | 35 à 45 € par heure | bobex.be | Hors France |

Marché : le marché français des centres de contacts externalisés représentait 3,56 Md€ en 2023 selon SP2C et EY, d'après Xerfi (secondaire). Selon une page de JobPhoning, ces prix « ne font l'objet d'aucune statistique publique en France » [DR].

**2. Quali Contact : données publiques** (API Recherche d'entreprises, consultée le 4 nov. 2026) [FV] :

| Champ | Valeur |
|---|---|
| Dénomination, SIREN | QUALI CONTACT, 394 573 497 |
| Forme | SAS (code 5710) |
| Création, état | 1er avril 1994, active |
| Activité principale | 73.20Z, études de marché et sondages (pas 82.20Z « centres d'appels ») |
| Effectif | Tranche 21 : 50 à 99 salariés (année 2024), PME |
| Siège | Espace Clichy, 38 rue Mozart, 92110 Clichy (tranche 20 à 49 salariés) |
| Établissement nivernais | ZA du Parc, 30-32 rue Eugène Perreau, 58200 Cosne-Cours-sur-Loire, actif depuis le 15 août 2000 (tranche 10 à 19 salariés) |
| Dirigeants publiés | CALOGERO SAS (présidente) ; Comptabilité Audit Conseil (commissaire aux comptes titulaire) |
| Convention collective | IDCC 2098 |
| Autre | Déclarée organisme de formation |
| Finances 2025 (jeu de données) | Chiffre d'affaires affiché à 0 et résultat net de 228 255 €. Un chiffre d'affaires nul signale probablement une donnée non publiée : **à ne pas interpréter** [IN] |

- Homonyme à ne pas confondre : QUALICONTACT, SIREN 511 316 903 (Aubervilliers, 2009), **cessée** [FV].
- Site qualicontact.com [FV] : « Agence multimedia spécialisée en Fundraising ». Il « réalise tous types de campagnes en émission et en réception d'appels pour le secteur caritatif ». Logos de clients associatifs (Restos du Cœur, Handicap International, Fondation de France, Institut Pasteur…). Pied de page « © 2018 » : la date de mise à jour du site est incertaine.
- ZoomInfo [DR] : créée en 1994, deux bureaux (Clichy et Cosne-Cours-sur-Loire). Une base commerciale avance environ 500 salariés, ce qui **contredit** la tranche officielle de 50 à 99. La donnée du registre prévaut.
- Lien avec le dossier : le dépôt indique que GianLuca « prévoit d'engager Quali Contact » (`sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:7`, [DR] selon Morgan, 25 oct. 2026). Le logiciel utilisé n'est « pas formellement identifié (peut-être Vocalcom Hermes360) » (`crm/PASSATION.md:46`) [IN]. Les bureaux proposés à Marwin seraient à Cosne-Cours-sur-Loire (`interne/contexte-projet-carlone.md:108`), la même commune que l'établissement de Quali Contact [FV]. Aucun lien capitalistique ou personnel entre GianLuca et Quali Contact n'est établi par les sources lues [IN] ; je n'en suppose aucun.

**3. Cadre du démarchage téléphonique (point juridique signalé, non traité à fond)** : depuis le **11 août 2026**, un **consommateur** ne peut être démarché par téléphone qu'avec son consentement préalable. C'est la fin de Bloctel, en application de la loi du 30 juin 2025 et d'un décret n° 2026-662 du 23 juillet 2026, selon les fiches de la DGCCRF sur economie.gouv.fr (extraits de recherche, page refusée en lecture, 403). **Pour les appels entre professionnels (B2B), je n'ai trouvé aucune source officielle confirmant l'absence de consentement préalable** [IN]. Une source secondaire (donneespersonnelles.fr) l'affirme. Les entrepreneurs individuels prospectés restent un cas à trancher.

### Sources

| Source | Organisme | Statut | Date | Citation courte |
|---|---|---|---|---|
| https://recherche-entreprises.api.gouv.fr/search?q=quali%20contact (fiche lisible : https://annuaire-entreprises.data.gouv.fr/entreprise/394573497) | DINUM / data.gouv.fr (Annuaire des Entreprises, données Sirene et RNE) | **Officielle** | Données lues le 4 nov. 2026 | « QUALI CONTACT … ZA DU PARC N° 30-32 RUE EUGENE PERREAU 58200 COSNE-COURS-SUR-LOIRE » |
| https://www.qualicontact.com/ | Quali Contact | Primaire (site de l'entreprise) | Non affichée (© 2018) | « Agence multimedia spécialisée en Fundraising » |
| https://www.zoominfo.com/c/qualicontact/161644917 | ZoomInfo | Secondaire commerciale | Non affichée | « two offices in France - one in Clichy and another in Cosne-Cours-Sur Loire » |
| https://derrick-app.com/fr/meilleures-agences/agence-de-prospection-b2b.md | Derrick (éditeur) | Secondaire, intéressé | 2026 | « 150 à 500 EUR par rendez-vous » |
| https://cocowork.fr/blog/externaliser-prospection-telephonique-b2b-seuils-chiffres-kpi/ | Cocowork (prestataire) | Secondaire, intéressé | Non affichée | « entre 200 et 400 euros selon la difficulté de la cible » |
| https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques/les-regles-du-demarchage-telephonique-simposant-aux-entreprises | DGCCRF | **Officielle**, vue en extrait de recherche (403) | « Écrit le 27/07/2026 » | Consentement préalable du consommateur à compter du 11 août 2026 |

### Incertitudes et points à faire valider
- Tarifs réels de Quali Contact, ses unités de facturation (heure, appel, rendez-vous), son expérience en prospection B2B hors du secteur caritatif, son logiciel et ses formats d'import et d'export : [IN]. **Ne pas le contacter dans le cadre de l'audit.** Ces questions sont à poser par GianLuca ou avec son accord.
- Qui contracte et qui paie Quali Contact : GianLuca directement, ou une de ses entités [IN]. Le statut de Marwin doit aussi être fixé : coordinateur, sans revente ni sous-traitance implicite.
- Régime juridique de la prospection B2B après le 11 août 2026, et traitement des données du CRM (base légale, information des personnes, opposition, conservation) : à faire valider par un **avocat** et à confronter aux pages de la **CNIL**. La CNIL annonce un webinaire « Nouveau régime de la prospection téléphonique », daté du 19 oct. 2026.
- Données financières de Quali Contact : à lire dans les comptes déposés au greffe, s'ils sont publiés [IN].

### Conséquences pour Marwin Tech et GianLuca Carlone
- Quali Contact est un acteur **local**, établi à Cosne depuis 2000, mais **spécialisé dans la collecte de dons**. Sa capacité, ses scripts et ses prix pour une prospection B2B auprès des entreprises de la Nièvre restent à démontrer [HY]. Pour GianLuca, le bon test est un **lot pilote payé au rendez-vous tenu** : quelques centaines de fiches du CRM, une définition écrite du rendez-vous qualifié, et un retour des résultats importé dans le CRM.
- Pour Marwin, la coordination de Quali Contact **ne doit pas être comptée comme production d'appels**. Le travail de Marwin se limite à préparer les listes, scripts et supports, contrôler la qualité, réimporter les résultats et produire les indicateurs. À environ 150 à 500 € le rendez-vous, un rendez-vous coûte l'équivalent de 0,2 à 0,7 journée Marwin [ES]. Cela aide à expliquer à GianLuca ce qu'il paie à qui.
- L'établissement de Quali Contact se trouve dans la commune des bureaux proposés. Marwin doit garder son indépendance d'organisation et ne pas devenir l'encadrant de fait des équipes de Quali Contact, pour éviter un mélange des responsabilités [HY, à valider par l'avocat].

---

## (d) Coût des outils

### Réponse courte
- **Assistants IA en équipe**, par siège et par mois, HT, tarifs publics en USD :
  - Claude Team : 20 $ (annuel) ou 25 $ (mensuel) pour un siège standard, 100 ou 125 $ pour un siège premium [FV] ;
  - ChatGPT Business : 20 $ (annuel) ou 25 $ (mensuel), d'après des sources secondaires, la page d'OpenAI n'ayant pas pu être lue ;
  - Mistral Le Chat Team : 24,99 $ [FV].
- **API LLM**, par million de jetons (entrée / sortie), tarifs standard ; le traitement par lots coûte 50 % de moins chez Anthropic, OpenAI et Google [FV] :
  - modèles intermédiaires : environ 2 $ / 10 $ (Claude Sonnet 5.5, GPT-6.1 Sol, Gemini 4 Argon) ;
  - modèles haut de gamme : 4 $ / 20 $ (Claude Opus 5.5), 10 $ / 50 $ (Claude Fable 5.1, GPT-6 Astra) ;
  - petits modèles : 0,10 $ / 0,50 $ (Claude Haiku 5.5, GPT-6 Luna) ;
  - Mistral Large : 0,5 $ / 1,5 $.
- **CRM et gestion de projet**, par siège et par mois :
  - Pipedrive : 14 à 79 $ (annuel) [FV] ;
  - HubSpot Sales Hub : Starter 20 €, Professional 90 à 100 € plus 1 470 € de mise en service (secondaire) ;
  - Notion : Plus 10 $, Business 20 $ [FV] ;
  - monday : 9 à 19 $ (annuel, 3 sièges minimum) [FV] ;
  - Airtable : Team 20 $, Business 45 $ (annuel) [FV].
- **Téléphonie**, HT, par utilisateur et par mois (sources secondaires) :
  - Ringover : 21 € (Smart), 44 € (Business), 54 € (Advanced), en annuel ;
  - Aircall : 30 € (Essentials) ou 50 € (Professional) en annuel, 40 ou 70 € en mensuel, 3 licences minimum.
- **NVIDIA DGX Spark (128 Go)** : pas de prix officiel lisible ce jour [IN].
  - Repères : 3 999 $ au lancement ; 4 699 $ et **4 800 € sur la boutique NVIDIA UE après la hausse de fin février 2026** (forum NVIDIA, secondaire) ;
  - prix observés en Europe en octobre 2026 : **environ 5 040 à plus de 8 100 € HT** selon le fabricant et le stockage (secondaire).

### Détail

**1. Abonnements d'assistants IA** (USD hors taxes sauf mention ; conversion au taux BCE [ES]) :

| Offre | Prix par siège et par mois | En € [ES] | Conditions | Source et statut |
|---|---|---|---|---|
| Claude Team, siège standard | 20 $ en annuel ; 25 $ en mensuel | 17,75 € ; 22,19 € | Équipes de 2 à 150 | claude.com/pricing [FV] |
| Claude Team, siège premium | 100 $ en annuel ; 125 $ en mensuel | 88,75 € ; 110,94 € | « 5x more usage than standard seats » | claude.com/pricing [FV] |
| ChatGPT Business | 20 $ en annuel ; 25 $ en mensuel | 17,75 € ; 22,19 € | 2 utilisateurs minimum ; baisse de prix du 2 avril 2026 | Secondaire (eesel.ai, elephas.app) ; page OpenAI non lue (403) [IN] |
| Mistral Le Chat Team | 24,99 $ | 22,18 € | | mistral.ai/pricing [FV] |

**2. API, prix par million de jetons (USD)** :

| Fournisseur et modèle | Entrée | Sortie | Remarques | Source |
|---|---|---|---|---|
| Anthropic Claude Fable 5.1 | 10 $ | 50 $ | Cache en lecture 0,25 $ | claude.com/pricing [FV] |
| Anthropic Claude Opus 5.5 | 4 $ | 20 $ | Cache en lecture 0,20 $ ; « Save 50% with batch processing » | claude.com/pricing [FV] |
| Anthropic Claude Sonnet 5.5 | 2 $ | 10 $ | Cache en lecture 0,10 $ | claude.com/pricing [FV] |
| Anthropic Claude Haiku 5.5 | 0,10 $ | 0,50 $ | Requêtes de 100 000 jetons ou moins ; 0,50 $ / 2,50 $ au-delà | claude.com/pricing [FV] |
| OpenAI GPT-6 Astra | 10 $ | 50 $ | Lot : 5 $ / 25 $ | developers.openai.com [FV, lu par outil automatique ; recoupé par la presse] |
| OpenAI GPT-6.1 Sol | 2 $ | 10 $ | Entrée en cache 0,10 $ | Idem, recoupé par plusieurs sites |
| OpenAI GPT-6.1 Terra | 1 $ | 5 $ | | developers.openai.com [FV, lecture automatique] |
| OpenAI GPT-6 Luna | 0,10 $ | 0,50 $ | | Idem |
| Google Gemini 4 Argon | 2 $ | 10 $ | **La page annonce un doublement des prix standard au 1er décembre 2026** | aistudio.google.com/docs/pricing [FV, lecture automatique] |
| Google Gemini 3.8 Flash | 0,75 $ | 3,75 $ | Doublement annoncé au 1er janvier 2027 | Idem |
| Google Gemini 3.1 Flash-Lite | 0,25 $ | 1,50 $ | | Idem |
| Mistral Large | 0,5 $ | 1,5 $ | Fournisseur européen | mistral.ai/pricing [FV] |

Ordre de grandeur mensuel [ES] :
- usage documentaire modéré (30 millions de jetons en entrée et 3 millions en sortie par mois) : environ 90 $ avec Sonnet 5.5 ou GPT-6.1 Sol (≈ 80 €), 180 $ avec Opus 5.5 (≈ 160 €), moins de 5 $ avec Haiku 5.5 ou GPT-6 Luna ;
- usage d'agents intensif (300 millions en entrée, 20 millions en sortie) : environ 1 600 $ avec Opus 5.5 (≈ 1 420 €) avant cache et traitement par lots.

L'écart va de 1 à 300 selon le modèle et le volume : le coût de l'IA dépend surtout des choix d'architecture.

**3. CRM, gestion de projet, téléphonie** :

| Outil | Prix par siège et par mois | Conditions | Source et statut |
|---|---|---|---|
| Pipedrive | Lite 14 $, Growth 39 $, Premium 59 $, Ultimate 79 $ | Facturation annuelle, hors TVA ; « Économisez jusqu'à 42% » par rapport au mensuel | pipedrive.com/fr/pricing [FV] |
| HubSpot Sales Hub | Starter 20 € (promotion dès 7 €) ; Professional 100 € en mensuel, 90 € en annuel ; Enterprise 150 à 175 € | Mise en service obligatoire : 1 470 € (Professional), 3 420 € (Enterprise). Nouveau modèle « sièges et crédits » pour les nouveaux clients EMEA (oct. 2026) | Secondaire (hublead.io, relevé du 22 oct. 2026) ; page HubSpot non chargée [IN] |
| Notion | Plus 10 $, Business 20 $ (agent IA inclus) | « Économisez jusqu'à 20 % avec la facturation annuelle » ; agents personnalisés facturés à part : 10 $ pour 1 000 crédits | notion.com/fr/pricing [FV] |
| monday work management | Basic 9 $, Standard 12 $, Pro 19 $ | Annuel ; 3 utilisateurs minimum ; hors taxes | monday.com/pricing [FV] |
| Airtable | Team 20 $, Business 45 $ | Annuel ; seuls les éditeurs sont facturés | airtable.com/pricing [FV] |
| Ringover | Smart 21 €, Business 44 €, Advanced 54 € HT | Annuel ; Business et Advanced : 3 licences et 12 mois minimum. La page officielle affiche « jusqu'à -30% » en annuel et « 100+ intégrations CRM » | Secondaire (skipcall.io, relevé de sept. 2026) ; grille officielle non chargée |
| Aircall | Essentials 30 €, Professional 50 € (annuel) ; 40 € et 70 € (mensuel) | 3 licences minimum ; module IA en option | Secondaire (cloudtalk.io, juillet 2026, **concurrent d'Aircall**) |

**4. DGX Spark** :

| Repère | Prix | Date | Source et statut |
|---|---|---|---|
| Fiche NVIDIA France | Aucun prix affiché ; 64 Go ou 128 Go ; jusqu'à 4 To ; « La configuration avec 64 Go de mémoire est disponible exclusivement auprès des partenaires OEM » | Page de 2026, article du 2 oct. 2026 | nvidia.com/fr-fr [FV] |
| Boutique NVIDIA UE | 4 800 € | Hausse signalée le 24 févr. 2026 | Forum développeurs NVIDIA, message d'utilisateur (secondaire) |
| Boutique NVIDIA US | 4 699 $ (contre 4 000 $ auparavant) | 24 févr. 2026 | Idem |
| Variante OEM de 1 To (Asus) | 3 300 € en Allemagne | 9 mars 2026 | Idem |
| Prix observés en Europe | environ 5 038 € à plus de 8 096 € HT | Octobre 2026 | tech-insider.org (secondaire) |

Amortissement [ES] : sur 36 mois, entre 135 et 225 € par mois, hors électricité, maintenance, sauvegarde et temps d'administration.

**5. Pile d'outils pour Marwin à deux** [ES, hypothèses de choix] :

| Scénario | Composition | Coût mensuel HT [ES] |
|---|---|---|
| Sobre | 2 sièges Claude Team standard (mensuel, 44 €) + Notion Plus (18 €) + CRM existant (0 € de licence, hébergement [IN]) + Ringover Smart ×2 (42 €) + API 50 à 150 € | **≈ 150 à 260 €** |
| Confortable | 2 sièges Claude premium (222 €) + 2 ChatGPT Business (44 €) + Notion Business (36 €) + Pipedrive Growth ×2 (69 €) + Ringover Business ×3 minimum (132 €) + API 150 à 500 € | **≈ 650 à 1 000 €** |
| Avec HubSpot Professional | Remplace Pipedrive par HubSpot Professional ×2 (180 €), plus 1 470 € de mise en service une seule fois | +110 € par mois, +1 470 € au départ |

Rapporté aux 15 000 € HT mensuels, les outils représentent **1 à 7 %** du chiffre d'affaires [ES]. Les outils ne sont donc pas ce qui fait le prix. Leur coût est faible, mais il faut les payer de façon fiable : la note du 4 novembre signale des **abonnements de Morgan en échec de prélèvement** (Notion, ChatGPT Pro…) depuis un changement de carte [FV] (`note-point-4-novembre-et-activites.md:8`).

### Sources

| Source | Organisme | Statut | Date de la page | Citation courte |
|---|---|---|---|---|
| https://claude.com/pricing | Anthropic | Primaire (éditeur) | Non affichée | « Per seat / month if billed annually » ; « Save 50% with batch processing. » |
| https://developers.openai.com/api/docs/pricing | OpenAI | Primaire, lue par outil automatique | Non affichée | « Prices per 1M tokens » |
| https://aistudio.google.com/docs/pricing (redirection de ai.google.dev) | Google | Primaire, lue par outil automatique | Non affichée | « Batch API (50% cost reduction) » |
| https://mistral.ai/pricing | Mistral AI | Primaire | Non affichée | « Mistral Large costs $0.5 /M tokens in and $1.5 /M tokens out » |
| https://www.pipedrive.com/fr/pricing | Pipedrive | Primaire | Non affichée | « Par poste et par mois, facturation annuelle » |
| https://www.notion.com/fr/pricing | Notion | Primaire | Non affichée | « Prix en USD » |
| https://monday.com/pricing | monday.com | Primaire | Non affichée | « The monthly plan is not discounted » |
| https://airtable.com/pricing | Airtable | Primaire | Non affichée | « Enterprise Scale plan pricing is custom » |
| https://www.nvidia.com/fr-fr/products/workstations/dgx-spark/ | NVIDIA | Primaire | 2026 | « Trouvez votre meilleure option d'achat sur NVIDIA Marketplace » |
| https://forums.developer.nvidia.com/t/dgx-spark-price-increase/361640 | Forum NVIDIA | Secondaire (utilisateurs) | Messages des 24 févr. au 9 mars 2026 | « the EU price of the DGX Spark on the NVIDIA marketplace increased to 4800 € » |
| https://www.hublead.io/fr/blog/hubspot-new-pricing | hublead.io | Secondaire | Oct. 2026 | Professional 90 € et Enterprise 175 € par siège en annuel |
| https://skipcall.io/avis/ringover | skipcall.io | Secondaire | Sept. 2026 | « Smart à 21 € … Business à 44 € et Advanced à 54 € » |
| https://www.cloudtalk.io/fr/blog/tarification-aircall/ | CloudTalk (concurrent) | Secondaire, intéressé | 7 juil. 2026 | « Essentials €30, Professional €50 » |
| https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml | BCE | **Officielle** | 4 nov. 2026 | 1 EUR = 1,1267 USD |

### Incertitudes et points à faire valider
- Les prix des éditeurs changent souvent : hausse du DGX Spark en février 2026, baisse de ChatGPT Business en avril 2026, nouveau modèle HubSpot en EMEA en octobre 2026, doublements de prix Gemini annoncés pour le 1er décembre 2026 et le 1er janvier 2027. **Chaque devis doit être daté et revu tous les trois mois** [HY].
- Les noms et prix des modèles OpenAI et Google proviennent d'une lecture automatique des pages officielles. Ils sont recoupés pour GPT-6.1 Sol et GPT-6 Astra, mais pas pour tous [IN partiel].
- Prix officiels non lus : ChatGPT Business, HubSpot, Ringover, Aircall, boutique NVIDIA [IN].
- À faire valider par l'**expert-comptable** : le traitement de la TVA sur les abonnements achetés à des éditeurs étrangers (autoliquidation pour un assujetti français [HY]), l'amortissement d'un DGX Spark, et la refacturation éventuelle des outils au client.
- Localisation et réutilisation des données (RGPD, transferts hors UE) selon l'offre retenue (Team ou Enterprise, API, fournisseur européen) : à vérifier avec le **DPO ou l'avocat** et la documentation de chaque éditeur.

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Contradiction à lever dans le dépôt** : l'audit interne présente le taux comme « taux d'équipe, outils compris » (`interne/audit-marwin-tech-carlone.md:78`). Le diaporama client écrit « bureaux, matériel, publicité, fabrication et sous-traitants sur devis séparés » (`slides/formules.html:30`), sans rien dire des logiciels. Il faut écrire noir sur blanc ce qui est inclus : les outils de Marwin (≈ 150 à 1 000 € par mois [ES]) peuvent être compris ; les licences utilisées par les équipes de GianLuca et les consommations d'API au-delà d'un plafond doivent être facturées à part ou payées directement par lui.
- **Les licences au nom de GianLuca ou de son entité** facilitent la réversibilité (`DEMANDE.md:49`) : il garde ses comptes et ses données si la collaboration s'arrête.
- **DGX Spark** : à 4 800 à 8 100 € HT, l'appareil absorberait **29 à 49 %** des 16 500 € non consacrés aux honoraires dans l'option laboratoire à 30 000 € HT (`slides/laboratoire.html`) [ES]. Avec les tarifs API ci-dessus, 4 800 € représentent par exemple environ 3 ans d'usage documentaire modéré sur un modèle intermédiaire (environ 80 € par mois [ES]). L'achat ne se justifie donc que par une contrainte démontrée de confidentialité ou de volume, comme le dit déjà `interne/complement-chatgpt-2026-11-04.md:37`.
- **Risque de hausse des coûts d'IA** (test d'échec de `DEMANDE.md:58`) : les doublements de prix annoncés par Google montrent que ce risque est réel. Il faut prévoir dans le contrat un plafond de consommation, un modèle de repli moins cher et une clause de révision.

---

## (e) Prix observés de missions de « pilotage externalisé » ou d'assistance à maîtrise d'ouvrage pour des PME

### Réponse courte
- **Repère public le plus solide** [FV, officiel] : le **Diag Data IA** (plan « Osez l'IA », France 2030, opéré par Bpifrance) coûte **10 000 € HT pour 8 jours-hommes**, soit **1 250 € HT par jour d'expert habilité**. Il est pris en charge à **40 %**, ce qui laisse **6 000 € HT** à l'entreprise. Il est réservé aux PME et ETI de 10 à 2 000 salariés, avec au moins 1 M€ de chiffre d'affaires et plus d'un an d'existence.
- Les « Accélérateurs IA » durent 18 mois, commencent par un diagnostic de 12 jours et sont pris en charge à 46 %. Leur prix total n'est pas publié sur la page lue [IN].
- **PMO externalisé et AMOA pour PME** : aucune grille publique fiable [IN]. Repères voisins, secondaires :
  - DAF à temps partagé : 800 à 1 200 € HT par jour, soit environ 4 000 à 8 000 € par mois pour quelques jours par semaine ;
  - DPO externalisé : 400 à 2 500 € HT par mois au forfait ;
  - management de transition : environ 1 330 € HT par jour ;
  - SDR externalisé : 3 000 à 8 000 € par mois.
- **Le format courant du « temps partagé » est de 2 à 8 jours par mois** [HY, d'après ces sources]. La formule de base de Marwin (20 journées-personnes, 15 000 € HT par mois) se rapproche plutôt d'**un équivalent temps plein externalisé**.

### Détail

| Prestation comparable | Prix observé | Unité | Source et statut |
|---|---|---|---|
| Diag Data IA (expert data et IA habilité Bpifrance) | 10 000 € HT, 8 jours-hommes, 40 % pris en charge, reste 6 000 € HT | Forfait de 3 mois maximum | entreprises.gouv.fr (mis à jour le 28 sept. 2026) et les-aides.fr (CCI, mis à jour le 12 août 2026) [FV, officiel] |
| Accélérateur IA | 18 mois, diagnostic de 12 jours, 46 % pris en charge | Prix [IN] | entreprises.gouv.fr [FV] |
| DAF à temps partagé | 800 à 1 200 € HT par jour | Jour | companeo.com (vendeur) |
| DAF à temps partagé | 4 000 à 8 000 € par mois pour « quelques jours par semaine » (le même article donne aussi 8 000 à 12 000 € pour 2 jours par semaine : contradiction interne) | Mois | plateya.fr (secondaire) |
| Management de transition | 1 330 € HT par jour en moyenne, 55 % des missions entre 1 000 et 1 500 € | Jour | plateya.fr, citant France Transition S1 2025 |
| DPO externalisé | 400 à 2 500 € HT par mois (forfait) ou 600 à 1 200 € HT par jour (régie) | Mois ou jour | legiscope.com (vendeur) |
| SDR (prospection) externalisé | 3 000 à 8 000 € par mois, 6 mois minimum | Mois | derrick-app.com (secondaire) |
| AMOA, consultant salarié (pour comparaison) | Médiane d'environ 4 459 € brut par mois au national | Salaire, pas TJM | Michael Page 2026, relayé par le Journal du Net (secondaire) |
| Marchés publics d'AMO | Montants non exploités | | Données DECP sur data.gouv.fr non analysées [IN] |

Évolution du dispositif public : en 2023, l'appel à candidatures du Diag Data IA annonçait 3 900 à 13 000 € HT pour 3 à 10 jours, pris en charge à 80 % (secondaire). En 2026, la prise en charge est de **40 %** [FV]. **La règle a donc changé** : le reste à charge a fortement augmenté.

Équivalences pour 15 000 € HT par mois [ES] :
- 12 jours d'un expert IA au prix du Diag Data IA (1 250 €) ;
- 11 jours de manager de transition (1 330 €) ;
- 12 à 19 jours de DAF à temps partagé (800 à 1 200 €) ;
- 20 jours de Marwin (750 €).

### Sources

| Source | Organisme | Statut | Date | Citation courte |
|---|---|---|---|---|
| https://www.entreprises.gouv.fr/priorites-et-actions/transition-numerique/accompagner-les-entreprises-dans-leur-transition/le-plan | Ministère de l'Économie, DGE | **Officielle** | Publiée le 1er juil. 2026, mise à jour le 28 sept. 2026 | « prestation de 8 jours-hommes » ; « coût de 10 000 euros HT, avec une prise en charge de 40 % par France 2030 » |
| https://les-aides.fr/aide/aVkf3w/bpifrance/diagnostic-data-intelligence-artificielle.html | CCI France (les-aides.fr) | Parapublique | « Mise à jour le 12 août 2026 » | « un reste à charge pour l'entreprise qui s'élève à 6 000 € HT » |
| https://www.companeo.com/comptabilite-externalisee-expert-comptable/guide/directeur-financier-tpe-pme-temps-partage | Companeo | Secondaire, vendeur | Non affichée | 800 à 1 200 € HT par jour |
| https://www.plateya.fr/blog/detail/quel-est-le-cout-dun-daf-a-temps-partage | plateya.fr | Secondaire | Non affichée | 4 000 à 8 000 € par mois |
| https://www.legiscope.com/blog/dpo-externalise-cout.html | Legiscope | Secondaire, vendeur | Non affichée | 400 à 2 500 € HT par mois |

### Incertitudes et points à faire valider
- Aucune grille publique pour le PMO externalisé ni pour l'AMOA de PME [IN]. Il faut deux ou trois devis comparables, sans contacter de prestataire au nom de GianLuca sans son accord.
- **Éligibilité des entités de GianLuca au Diag Data IA ou à un Accélérateur IA** : effectif, chiffre d'affaires, ancienneté [IN]. À vérifier avec Bpifrance (chargé d'affaires régional) et l'expert-comptable de GianLuca. **Aucune aide n'est acquise.**
- Un expert Marwin peut-il être habilité par Bpifrance ? [IN]. Ne pas le présenter comme possible sans vérification.
- Les données DECP (marchés publics) pourraient fournir des prix d'AMO réellement attribués : analyse non faite [IN].

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Le taux de 750 € est inférieur aux repères de direction à temps partagé et d'expertise IA.** Marwin peut défendre la valeur d'une journée de pilotage. Ce qui est atypique, c'est **le volume** : 20 journées-personnes par mois pendant 6 mois, soit 90 000 € HT (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:54`) [PR], contre 2 à 8 jours par mois pour un temps partagé classique [HY]. Le marché soutient davantage un cadrage court payé au forfait, puis un pilotage récurrent de quelques jours par mois, avec des lots complémentaires.
- **Le Diag Data IA est une alternative concrète pour GianLuca** (6 000 € HT à sa charge, s'il est éligible). Il peut aussi servir à Marwin : un cadrage IA facturé au même ordre de grandeur (≈ 8 jours, 6 000 à 10 000 € HT) est lisible et comparable [PR à étudier]. Il ne faut pas laisser croire que l'offre Marwin est subventionnée.
- Pour les fonctions récurrentes (prospection, protection des données, finance), le marché vend des **forfaits mensuels bornés** (400 à 8 000 € par mois). Cela justifie de découper l'offre Marwin en forfaits par résultat plutôt qu'en un abonnement général (`DEMANDE.md:28`).

---

## Contradictions et constats sur les pièces du dépôt

| Pièce | Ce qu'elle dit | Ce que montre le marché | Code |
|---|---|---|---|
| `interne/audit-marwin-tech-carlone.md:70-80` | Tableau TJM 2026 (développeur 485 €, chef de projet 595 €, consultant 629 €, IA 750 à 1 500 €), source freelance-solution.fr | Chiffres fidèles à la page (juin 2026), mais source secondaire. Le chiffre IA n'est pas sourcé sur la page. L'étude primaire Kicklox 2025 donne la gestion de projets à 698 € et les seniors à 643 € | [FV] |
| `interne/audit-marwin-tech-carlone.md:80` | « environ 613 € en Île-de-France » | C'est la moyenne Île-de-France de l'étude Kicklox, tous métiers tech. La province y est à 582 € (−5 %), pas 15 à 30 % en dessous | [FV] |
| `interne/offre-marwin-tech-remuneration-et-collaboration.md:254` | Deux salariés coûteraient « 1,6 à 1,9 fois leur net » | URSSAF : 1,37 à 1,56 près du SMIC, 1,64 à 1,83 pour des profils qualifiés, avant mutuelle et frais | [ES] |
| `interne/audit-marwin-tech-carlone.md:78` et `slides/formules.html:30` | « outils compris » contre « matériel … sur devis séparés » | Le contenu du prix est à préciser : outils de Marwin, licences du client, consommations d'API | [FV] contradiction |
| `slides/laboratoire.html` | 30 000 € HT, dont 13 500 € d'honoraires pour 18 journées | Un DGX Spark (4 800 à 8 100 € HT) prendrait 29 à 49 % du reste | [ES] |
| `crm/PASSATION.md:46` | Logiciel de Quali Contact « pas formellement identifié » | Le site public de Quali Contact ne nomme aucun logiciel | [IN] |

---

## Tableau récapitulatif

| Règle ou repère | Valeur ou condition | Source | Niveau de certitude |
|---|---|---|---|
| TJM moyen des freelances tech seniors (11 ans et plus) | 643 € | Kicklox / RH Solutions 2025, PDF p. 12 | Moyen (étude privée, 663 réponses) |
| TJM moyen des freelances tech juniors (0 à 4 ans) | 268 € | Idem, PDF p. 12 | Moyen |
| TJM moyen « gestion de projets » | 698 € | Idem, PDF p. 14 | Moyen |
| Écart province / Île-de-France | −5 % (Kicklox) ; −5 % pour les chefs de projet et −10 % pour les développeurs (Hays) ; « 15 à 30 % » (agrégateur) | Kicklox p. 13 ; Blog du Modérateur (Hays) ; freelance-solution.fr | Faible à moyen (sources divergentes) |
| TJM chef de projet par expérience, Paris | 600 → 800 € | Hays 2026, via Blog du Modérateur | Moyen (secondaire) |
| Médiane consultant stratégie et management | ≈ 629 € (400 à 1 000 €) | freelance-solution.fr, juin 2026 | Faible (agrégateur) |
| TJM développeur | ≈ 485 € (350 à 650 €) | freelance-solution.fr ; Hays 450 → 650 € à Paris | Moyen |
| TJM consultant IA | 750 à 1 500 € | freelance-solution.fr, non sourcé | Faible |
| Prix public d'un jour d'expert IA (dispositif d'État) | 1 250 € HT (10 000 € pour 8 jours-hommes) | entreprises.gouv.fr, mise à jour du 28 sept. 2026 | **Élevé (officiel)** |
| Prise en charge du Diag Data IA | 40 % (France 2030), reste 6 000 € HT ; 80 % en 2023 | entreprises.gouv.fr ; les-aides.fr | Élevé pour 2026 ; la règle a changé |
| Management de transition, TJM moyen | ≈ 1 330 € HT (S1 2025) | plateya.fr, citant France Transition | Faible (source primaire non lue) |
| COO ou directeur des opérations à temps partagé | Aucune donnée française | — | [IN] |
| DAF à temps partagé | 800 à 1 200 € HT par jour | companeo.com | Faible (vendeur) |
| SMIC au 1er juin 2026 | 12,31 € par heure ; 1 867,02 € par mois | API URSSAF ; info.gouv.fr (extrait) | **Élevé (officiel)** |
| SMIC au 1er janvier 2026 | 12,02 € par heure (base de la RGDU toute l'année 2026, « gel ») | info.gouv.fr (extrait) ; Gazette du Palais | Élevé pour le montant ; moyen pour le gel (à confirmer sur urssaf.fr) |
| Plafond de la sécurité sociale 2026 | 4 005 € par mois | API URSSAF | Élevé |
| RGDU (nouvelle en 2026) | Remplace la réduction générale ; nulle à 3 SMIC ; Tmin 0,02 ; puissance 1,75 | API URSSAF (calcul) ; Bpifrance Création ; sources professionnelles | Moyen (paramètres non lus sur urssaf.fr) |
| Coût employeur d'un assistant ou office manager non cadre, 2 000 à 2 900 € brut, Nièvre | 2 249 à 3 842 € par mois (27 à 46 k€ par an), hors mutuelle et frais | Calcul API URSSAF, 4 nov. 2026 | Élevé pour le calcul ; **hypothèse de salaire** [HY] |
| Coût employeur d'un chef de projet cadre à 52 k€ (médiane régionale APEC) | 6 149 € par mois (73,8 k€ par an) | API URSSAF + APEC 2025 p. 53 | Moyen |
| Médianes des cadres « autres régions » | Assistanat 41 k€ ; organisation 46 k€ ; projets IT 52 k€ ; direction 70 k€ | APEC 2025, PDF p. 9, 13, 53, 42 | Moyen à élevé (étude paritaire, lecture des graphiques) |
| Médiane non cadre Nièvre pour ces métiers | Non trouvée | Insee inaccessible (erreur 500) | [IN] |
| Prospection B2B externalisée | 150 à 500 € HT par rendez-vous tenu ; SDR 3 000 à 8 000 € par mois | Derrick, Cocowork | Faible (vendeurs) |
| Quali Contact : identité | SAS, SIREN 394 573 497, créée en 1994, active, 50 à 99 salariés (2024), NAF 73.20Z | API Recherche d'entreprises (data.gouv.fr) | **Élevé (officiel)** |
| Quali Contact : présence locale | Établissement actif à Cosne-Cours-sur-Loire depuis le 15 août 2000 (10 à 19 salariés) | Idem | Élevé |
| Quali Contact : activité affichée | Collecte de dons pour le secteur caritatif, appels sortants et entrants ; B2B non mentionné | qualicontact.com | Moyen (site possiblement ancien) |
| Démarchage téléphonique des consommateurs | Consentement préalable obligatoire depuis le 11 août 2026 (fin de Bloctel) | DGCCRF, economie.gouv.fr (extrait) | Élevé pour les consommateurs ; **[IN] pour le B2B** |
| Claude Team | 20 $ (annuel) ou 25 $ (mensuel) par siège standard ; 100 ou 125 $ premium | claude.com/pricing | Élevé (éditeur) |
| ChatGPT Business | 20 $ (annuel) ou 25 $ (mensuel) par siège, depuis le 2 avril 2026 | Secondaire | Moyen |
| API, modèles intermédiaires | ≈ 2 $ / 10 $ par million de jetons (Sonnet 5.5, GPT-6.1 Sol, Gemini 4 Argon) | Pages des éditeurs | Élevé (Anthropic) ; moyen (OpenAI, Google : lecture automatique) |
| API, réduction pour traitement par lots | −50 % (Anthropic, OpenAI, Google) | Pages des éditeurs | Élevé |
| Hausse annoncée des prix Gemini | Doublement au 1er déc. 2026 (Argon) et au 1er janv. 2027 (Flash) | aistudio.google.com | Moyen (lecture automatique) |
| Pipedrive | 14 à 79 $ par siège et par mois (annuel, HT) | pipedrive.com | Élevé |
| HubSpot Sales Hub Professional | 90 à 100 € par siège et par mois + 1 470 € de mise en service | hublead.io | Moyen (secondaire) |
| Notion, monday, Airtable | Notion 10 ou 20 $ ; monday 9 à 19 $ (3 sièges minimum) ; Airtable 20 ou 45 $ | Pages des éditeurs | Élevé |
| Ringover | 21, 44 ou 54 € HT par utilisateur et par mois (annuel) | skipcall.io | Moyen (secondaire) |
| Aircall | 30 ou 50 € par licence et par mois (annuel), 3 licences minimum | cloudtalk.io (concurrent) | Faible à moyen |
| DGX Spark 128 Go | 4 800 € (boutique UE, février 2026) ; 5 040 à plus de 8 100 € HT observés en octobre 2026 | Forum NVIDIA ; tech-insider.org | Faible (pas de prix officiel lisible) |
| Pile d'outils Marwin à deux | ≈ 150 à 1 000 € HT par mois (1 à 7 % des 15 000 €) | Calcul à partir des prix ci-dessus | [ES] |
| Équivalent salarial de 15 000 € HT par mois | ≈ 2,4 chefs de projet cadres régionaux, ou 5,3 assistants à 2 300 € brut | Calcul URSSAF + APEC | [ES] |

## Questions bloquantes à faire trancher
1. **Expérience démontrable** de Morgan et de Mathys (années, références) : c'est elle qui situe le taux entre la moyenne « avancé » (462 €) et « senior » (643 €). Sans réponse, 750 € reste difficile à défendre [IN].
2. **Contenu exact du prix** : outils compris ou non, licences du client, plafond d'API. Il faut une seule version, cohérente entre le document interne et le diaporama.
3. **Expert-comptable** : paramètres RGDU 2026, convention collective et coût complet (mutuelle, prévoyance, frais) d'un poste d'assistant ou d'office manager chez GianLuca, pour une comparaison loyale.
4. **Avocat ou CNIL** : régime de la prospection téléphonique B2B après le 11 août 2026 et cadre du traitement des données du CRM confié à Quali Contact.
5. **GianLuca, avec son accord** : contrat, prix et logiciel de Quali Contact, et entité qui paie ; éligibilité de ses entités au Diag Data IA.
