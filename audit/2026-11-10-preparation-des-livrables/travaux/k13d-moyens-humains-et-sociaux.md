# Les moyens humains et sociaux : rémunération, recrutement, formation, conditions de travail, aides

Note de travail interne — sources publiques consultées le 10 novembre 2026 — ce n'est pas un avis juridique, fiscal ou d'investissement.

Statut : interne. Contient des coûts salariaux, des hypothèses de rémunération des associés et des tarifs d'indépendants : rien de cela ne va tel quel à GianLuca Carlone (règle 4 du § 5 de `audit/2026-11-09-audit-presentation-et-offre/travaux/BRIEF.md` : jamais « la rémunération des associés » ni « le taux journalier » dans un texte client). Les aides destinées au client sont traitées dans `k7b-aides-publiques-numerique-ia.md` ; elles ne sont pas reprises ici. La partie « Vérification du 10 novembre 2026 », à la fin, l’emporte sur le reste de la note.

Étiquettes : [Officiel] texte ou page d'une autorité ; [Prix public daté] ; [Mesure publiée] statistique ou étude publiée ; [Source professionnelle] cabinet, presse, plateforme ; [Estimation] calcul de cette note ; [À confirmer].

## En bref

1. Un salarié coûte entre 1,06 et 1,38 fois son salaire brut en 2026, selon le niveau de salaire : environ 26 900 € par an pour 2 000 € brut par mois, 43 900 € pour 2 800 €, 58 000 € pour 3 500 € [Estimation, section 1]. La réduction générale a été réformée au 1er janvier 2026 : elle s'applique jusqu'à 3 Smic, avec un plancher de 2 %.
2. Un apprenti en licence ou master coûte peu (environ 1 000 € par mois la première année pour un jeune de 21 à 25 ans), avec une aide de 2 000 € (bac + 3 à bac + 5) ou 4 500 € (bac + 2) pour une entreprise de moins de 250 salariés, si le contrat commence avant le 1er janvier 2027 [Officiel ; Estimation pour le coût].
3. Un président de SAS payé n'a pas droit au chômage. Pour lui verser 2 000 € net par mois, la société paie environ 3 500 € [Estimation]. Sans rémunération, pas de cotisations et pas de droits.
4. Les aides à l'innovation (JEI, CIR, CII, Bourse French Tech) exigent de la vraie recherche ou un vrai prototype, documentés. L'usage d'outils d'IA pour du conseil n'y suffit pas. La Bourse French Tech se demande dans l'année qui suit l'immatriculation, avant toute dépense.
5. L'article 4 du règlement européen sur l'IA impose déjà, depuis le 2 février 2025, un « niveau suffisant de maîtrise de l'IA » au personnel qui utilise ou fournit des systèmes d'IA : c'est un argument pour la formation, pas une certification obligatoire.
6. Le message pour le livrable : aujourd'hui, si l'un des deux manque, tout s'arrête. Un troisième professionnel, de la formation et une rémunération stable des associés réduisent ce risque. Aucun « × 100 » n'est possible sur l'humain : les gains humains se mesurent en continuité, en délais et en tâches menées en parallèle (au plus × 1,5 à × 2 en capacité, selon les hypothèses de la section « Gains »).

## 1. Coût employeur d'un salarié en France en 2026

**Conclusion.** Le Smic a augmenté deux fois en 2026. La réduction générale de cotisations a été refondue. Au niveau d'un développeur confirmé (2 800 à 3 500 € brut), la réduction devient faible : le coût dépasse 1,3 fois le brut.

**Smic.**
- 12,02 € brut de l'heure et 1 823,03 € brut par mois du 1er janvier au 31 mai 2026 ; 12,31 € et 1 867,02 € depuis le 1er juin 2026 (hausse automatique de 2,41 %, l'inflation ayant dépassé 2 %). Net indicatif : 1 477,93 € par mois. (Service Public, « Le Smic va augmenter le 1er juin », 18 mai 2026 ; Urssaf, « Montant du Smic » ; Insee, série du Smic, 9 septembre 2026) [Officiel]
- Changement 2026 : c'est une revalorisation en cours d'année, rare. Une nouvelle revalorisation au 1er janvier 2027 est probable, son montant est inconnu. [À confirmer en décembre 2026]

**Réduction générale (RGDU).**
- Depuis le 1er janvier 2026, la « réduction générale dégressive unique » remplace la réduction générale et les taux réduits de cotisations maladie et allocations familiales. Elle s'applique jusqu'à 3 Smic (contre 1,6 Smic avant). Coefficient maximal : 0,3981 pour moins de 50 salariés ; minimum 2 % juste sous 3 Smic ; exposant 1,75. (Urssaf, « Ce qu'il faut savoir au 1er janvier 2026 » ; Urssaf, « La réduction générale dégressive unique ») [Officiel]
- Pour 2026, le Smic retenu dans la formule reste celui du 1er janvier (21 876,40 € par an) ; seuil de sortie : 5 469,09 € brut par mois. (Décret du 12 juin 2026, résumé par Service Public Entreprendre, 18 juin 2026 ; economie.gouv.fr, fiche RGDU) [Officiel]
- La réduction ne s'applique pas à la rémunération du président de SAS. (Bpifrance Création, « Le dirigeant assimilé salarié », 31 août 2026) [Officiel]

**Taux patronaux 2026 (secteur privé, moins de 11 salariés).** Maladie 13 % ; vieillesse 8,55 % jusqu'au plafond et 2,11 % sur le tout ; allocations familiales 5,25 % ; autonomie 0,30 % ; dialogue social 0,016 % ; chômage 4,00 % ; AGS 0,25 % ; Fnal 0,10 % ; formation 0,55 % ; taxe d'apprentissage 0,59 % + 0,09 % ; accident du travail : taux notifié par la Carsat. (Urssaf, « Taux de cotisations — secteur privé », mis à jour le 1er janvier 2026) [Officiel]. S'y ajoutent la retraite complémentaire Agirc-Arrco, 6,01 % pour l'employeur sous le plafond (taux connu, non relu sur agirc-arrco.fr) [À confirmer], la part patronale de la mutuelle, et pour un cadre la prévoyance de 1,50 % [À confirmer].

**Coût total calculé** (non-cadre sauf à 3 500 €, moins de 11 salariés, accident du travail estimé à 0,75 %, mutuelle patronale estimée à 40 € par mois, sans versement mobilité) [Estimation] :

| Salaire brut mensuel | Coefficient RGDU | Coût mensuel | Coût annuel (12 mois) | Coût / brut |
|---|---|---|---|---|
| 1 867,02 € (Smic) | 0,3750 | ≈ 1 980 € | ≈ 23 800 € | 1,06 |
| 2 000 € | 0,3147 | ≈ 2 240 € | ≈ 26 900 € | 1,12 |
| 2 800 € | 0,1234 | ≈ 3 660 € | ≈ 43 900 € | 1,31 |
| 3 500 € (cadre) | 0,0611 | ≈ 4 830 € | ≈ 58 000 € | 1,38 |

Limites : pas de treizième mois, pas de convention collective appliquée (la convention Syntec impose des minima et une prévoyance à vérifier), pas de frais de poste (ordinateur, abonnements, locaux). À faire refaire par l'expert-comptable ou avec le simulateur de l'Urssaf.

**Apprenti ou alternant.**
- Aide à l'embauche d'un apprenti, entreprise de moins de 250 salariés : 5 000 € (aide unique) jusqu'au bac ; 4 500 € pour un bac + 2 ; 2 000 € pour un bac + 3 à bac + 5 ; 6 000 € pour une personne reconnue travailleur handicapé. Première année seulement. Contrats conclus depuis le 8 mars 2026 et commencés avant le 1er janvier 2027. (Décret n° 2026-168 du 6 mars 2026, Légifrance ; Service Public Entreprendre, F23556 et actualité du 10 mars 2026) [Officiel]
- Changement 2026 : l'aide pour un bac + 3 à bac + 5 est passée à 2 000 € (elle était de 5 000 € en 2025, montant de 2025 non relu ici) [À confirmer pour 2025]. Rien n'est connu pour les contrats commencés en 2027 [À confirmer].
- Salaire minimum d'un apprenti : un pourcentage du Smic selon l'âge et l'année (par exemple 53 % la première année entre 21 et 25 ans, 100 % à partir de 26 ans) : grille connue, page officielle non relue [À confirmer].
- Coût estimé pour un apprenti de 21 à 25 ans, première année : environ 990 € brut par mois ; la RGDU s'applique aussi aux apprentis (Urssaf) ; coût employeur proche de 1 000 à 1 050 € par mois, soit 12 000 à 12 600 € par an, moins l'aide de 2 000 € ou 4 500 € [Estimation]. Le vrai coût est le temps du tuteur : un apprenti doit être formé et encadré, ce qui pèse sur deux associés déjà pleins.

## 2. Rémunération des dirigeants d'une SAS

**Conclusion.** Payer les associés coûte cher, mais c'est la seule façon de leur ouvrir des droits. Le chômage reste exclu, sauf assurance privée ou vrai contrat de travail.

- Le président et les directeurs généraux d'une SAS sont « assimilés salariés » : régime général, mêmes cotisations qu'un cadre, sauf l'assurance chômage. Ils sont couverts en maladie, maternité, accident du travail, retraite de base et complémentaire, prévoyance. (Service Public Entreprendre, F36007 et F37366, pages non datées) [Officiel]
- Pas de rémunération, pas de cotisation minimale, donc pas de droits. Les dividendes ne sont pas soumis à cotisations et n'ouvrent aucune protection. (Bpifrance Création, « Le dirigeant assimilé salarié », 31 août 2026 ; F37366) [Officiel]
- Le mandataire n'a pas droit au Smic, ni aux congés payés, ni aux indemnités de rupture. La rémunération est fixée par les associés, souvent en assemblée. (Bpifrance Création, même page ; Service Public Entreprendre, F36065) [Officiel]
- Chômage : possible seulement avec un vrai contrat de travail distinct (tâches techniques, salaire, lien de subordination), pour un associé non majoritaire, à faire vérifier par France Travail. Sinon, assurance chômage privée. (Bpifrance Création, « Situation sociale et fiscale du président de SAS ») [Officiel]
- Ordre de grandeur publié : charges d'environ 63 % de la rémunération brute. (Bpifrance Création, 31 août 2026) [Officiel, arrondi]
- Calcul de cette note, avec les taux de la section 1 sans chômage ni AGS ni RGDU : pour 1 500 € net par mois, coût pour la société ≈ 2 630 € ; pour 2 000 € net, ≈ 3 510 € ; pour 3 000 € net, ≈ 5 260 €. Les cotisations représentent environ 75 % du net [Estimation]. Pour deux associés à 2 000 € net : ≈ 84 000 € par an pour la société [Estimation].
- Rappel de l'audit stratégique : le modèle financier ne compte ni ACRE, ni ARE, ni ARCE, ni mutuelle, ni prévoyance pour les associés (`audit/2026-11-04-audit-strategique/annexes/modele-financier/structures.md`, ligne 26) ; la rémunération figure parmi les accords écrits à passer entre Morgan et Mathys (`interne/01-synthese-direction.md`, ligne 36).

**Ce que change une rémunération stable.**
- Protection : indemnités journalières en cas de maladie, trimestres de retraite, prévoyance. Sans paie, un arrêt de travail d'un associé arrête aussi son revenu.
- Disponibilité : une rémunération fixe permet de réserver du temps à Marwin Tech au lieu d'autres activités. L'audit relève que les disponibilités des deux associés « ne sont documentées nulle part » (`interne/06-fonctionnement-a-deux.md`, ligne 550) et qu'un associé travaille aussi sur d'autres projets (ligne 353).
- Limite : la rémunération ne crée pas de capacité. Elle la rend fiable. C'est un argument de continuité, pas de multiplication.

## 3. Profils utiles et ordres de grandeur de salaires

**Conclusion.** Les profils les plus utiles à Marwin Tech sont, dans l'ordre : un développeur confirmé capable de maintenir ce qui est livré ; un chef de projet ou coordinateur ; plus tard un spécialiste données ou IA. En région, un ingénieur IA confirmé se paie 45 000 à 62 000 € brut par an ; un chef de projet IA 40 000 à 48 000 € [Source professionnelle]. Les écarts entre études sont grands : aucun chiffre isolé ne fait référence.

| Profil | Zone | Brut annuel fixe | Source |
|---|---|---|---|
| Ingénieur IA, junior (0 à 3 ans) | « Régions » (hors Paris et grandes villes) | 36 000 – 45 000 € | Silkhom, baromètre IA et ML 2026 (PDF, juin 2026) [Source professionnelle] |
| Ingénieur IA, confirmé (3 à 7 ans) | Régions | 45 000 – 62 000 € | idem |
| Chef de projet IA, junior | Régions | 34 000 – 40 000 € | idem |
| Chef de projet IA, confirmé | Régions | 40 000 – 48 000 € | idem |
| Chef de projet technique, junior (0 à 2 ans) | Régions | 35 000 – 42 000 € | Silkhom, « Salaires informatique 2026 », 30 juin 2026 [Source professionnelle] |
| Développeur Java ou Python (profils expérimentés) | France | ≈ 45 000 €, en léger recul | idem ; repris par myESN, 28 octobre 2026 [Source professionnelle] |
| Data scientist (profils expérimentés) | France | ≈ 56 000 € (+ 11,4 %) | idem |
| Médiane des cadres de la data | Île-de-France | 54 000 € | Étude Apec sur 111 familles de métiers, décembre 2025, citée par myESN [Source professionnelle ; étude Apec non ouverte] |
| Technicien d'intervention (installation, maintenance) | — | Inconnu | Aucune source lue [À confirmer] |

Lecture pour Marwin Tech : un poste de développeur ou de chef de projet en Nièvre à 2 800 à 3 500 € brut par mois (33 600 à 42 000 € par an) est dans le bas des fourchettes « Régions ». Il coûte 43 900 à 58 000 € par an à l'employeur (section 1) [Estimation]. Un recrutement en dessous de ces fourchettes est possible pour un junior, avec plus d'encadrement.

**Tarifs journaliers d'indépendants (usage interne seulement).**
- Malt, baromètre en continu « Grille des tarifs 2026 » (freelances expérimentés actifs les trois derniers mois) : développeur 576 € par jour (317 € de 0 à 2 ans ; 672 € au-delà de 15 ans) ; développeur Python 600 € ; data scientist 681 € (358 € de 0 à 2 ans). [Prix public daté : page consultée le 10 novembre 2026 ; hors taxes d'après Offbound, 4 novembre 2026 ; Malt ne le dit pas dans l'extrait lu : À confirmer]
- Hays 2026, cité par Offbound : chef de projet 600 à 800 € par jour ; data scientist 550 à 800 € [Source professionnelle, de seconde main].
- Usage : ces tarifs servent à comparer « embaucher » et « sous-traiter un lot ». À 576 € par jour, 20 jours de développeur indépendant coûtent ≈ 11 500 € HT, soit environ trois mois de coût employeur d'un développeur à 2 800 € brut [Estimation]. La sous-traitance d'un lot reste la première réponse prévue par l'audit avant tout recrutement (`interne/08-feuille-de-route.md`, ligne 509 : recruter « après trois mois au-delà de 85 % d'occupation », « sous-traitance d'un lot d'abord »).

## 4. Formation

**Conclusion.** Une petite société peut faire financer une partie de la formation de ses salariés par son opérateur de compétences ; un président de SAS rémunéré y a aussi accès. L'article 4 du règlement sur l'IA oblige à former à l'IA, mais sans niveau fixé ni certificat imposé.

**Financement des salariés.**
- Les entreprises de moins de 50 salariés peuvent faire prendre en charge les frais pédagogiques des formations de leur plan de développement des compétences, « selon un barème fixé par votre branche professionnelle ». (Opco Atlas, « Plan de développement des compétences », page non datée) [Officiel]
- Opco Atlas a publié de nouveaux critères le 9 janvier 2026, et ses règles de règlement ont changé le 1er octobre 2026 (paiement direct de l'organisme seulement sur demande, pour les moins de 50 salariés). (Opco Atlas, actualité du 9 janvier 2026 ; « Conditions de règlement ») [Officiel]. Les plafonds par entreprise n'ont pas été lus [À confirmer].
- Le rattachement à Opco Atlas dépend de la convention collective. Pour une société de conseil et de logiciels, la convention des bureaux d'études (Syntec) est probable, mais elle dépend du code d'activité retenu [À confirmer avec l'expert-comptable].
- Toute demande doit être déposée et acceptée avant le début de la formation (Opco Atlas, « Conditions de règlement ») [Officiel].

**Financement des dirigeants.**
- Un président de SAS rémunéré relève de l'opérateur de compétences de la société, pas d'un fonds d'assurance formation des indépendants (AGEFICE, FIF PL). (Kaelia, 23 septembre 2026 ; L'Iobette, 10 février 2026) [Source professionnelle ; à confirmer auprès d'Opco Atlas]. Sans rémunération, le financement de sa formation est incertain [À confirmer].
- Le compte personnel de formation de chaque associé reste mobilisable à titre personnel (droits acquis ailleurs) [À confirmer : page non relue].

**Certifications.** Aucune certification en IA n'est exigée par la loi. La Commission le dit : « un certificat n'est pas nécessaire » pour l'article 4 (questions-réponses citées par Proactive Academy, 9 juin 2026) [Officiel, de seconde main]. Les certifications inscrites au Répertoire spécifique de France Compétences, éligibles au CPF, n'ont pas été recherchées [À confirmer].

**Article 4 du règlement (UE) 2024/1689 (« maîtrise de l'IA »).**
- Fournisseurs et déployeurs de systèmes d'IA prennent des mesures pour que leur personnel et les personnes qui utilisent ces systèmes pour leur compte en aient la maîtrise, selon leurs connaissances, leur formation et le contexte d'usage. En application depuis le 2 février 2025. (Règlement 2024/1689, EUR-Lex ; Commission européenne, « Alphabétisation à l'IA — Questions et réponses ») [Officiel]
- **Changement de 2026** : le « paquet omnibus numérique » sur l'IA, en vigueur depuis la mi-juillet 2026, garde l'obligation mais supprime l'exigence d'un niveau « suffisant ». La surveillance par les autorités nationales s'applique depuis le 2 août 2026. (Commission européenne, même page) [Officiel]
- Concrètement, d'après la Commission : comprendre ce qu'est l'IA utilisée dans l'organisation ; savoir si l'on est fournisseur ou déployeur ; connaître les risques des systèmes utilisés ; adapter les actions aux connaissances de chacun. Lire la notice d'un outil ne suffit pas. Tenir un registre interne des formations est recommandé. Pas de certificat, pas de « délégué à l'IA » obligatoire. (Commission, questions-réponses ; Proactive Academy, 9 juin 2026) [Officiel ; Source professionnelle pour le résumé]
- Sanctions : fixées par chaque État ; proportionnées. En France, la désignation des autorités (rôle central de la CNIL) passait encore par un projet de loi fin octobre 2026. (Proactive Academy, 9 juin 2026) [Source professionnelle ; À confirmer]
- Pour Marwin Tech : elle est fournisseur ou déployeur selon les projets ; GianLuca Carlone et son administratrice seront déployeurs des outils livrés. Une formation courte et tracée, par Marwin Tech, de l'administratrice sert aussi l'obligation du client. C'est un argument de service, pas une contrainte nouvelle.

## Vérification du 10 novembre 2026

Relecture sceptique, 10 novembre 2026 (vérification commune aux notes k13b, k13d et k13f). Pour cette note : aucune recherche par moteur ; quatre fiches officielles lues : service-public.gouv.fr, Smic (F2300) ; entreprendre.service-public.gouv.fr, aide à l’embauche d’un apprenti (F23556), jeune entreprise innovante (F31188), crédit d’impôt recherche (F23533). Les pages de l’Urssaf, de Bpifrance, d’Opco Atlas, de la Commission européenne et les sources professionnelles n’ont pas été relues. La note s’arrête après la partie 4 : les parties sur les aides à l’innovation et sur les « Gains », citées dans « En bref » (points 4 et 6), n’existent pas ; l’essentiel est ajouté ci-dessous. Cette partie l’emporte sur le reste de la note.

**Conclusion.** Le Smic et l’aide à l’embauche d’un apprenti sont justes. Les conditions de la jeune entreprise innovante confirment le point 4 de « En bref » : il faut au moins 20 % de dépenses de recherche et développement dans les charges, ce que le conseil et l’usage d’outils d’IA n’atteignent pas. Le « × 1,5 à × 2 » du point 6 n’a aucun calcul dans la note. Les coûts employeur restent des estimations à faire refaire par l’expert-comptable. Rien de cette note ne va dans un document client, sauf des phrases sans chiffre.

### Tableau des contrôles

| # | Affirmation | Verdict | Source et date |
|---|---|---|---|
| 1 | Smic depuis le 1er juin 2026 : 12,31 € brut de l’heure, 1 867,02 € brut par mois, 1 477,93 € net | Confirmé ; annuel : 22 404,20 € brut | Service-public.gouv.fr, fiche F2300, vérifiée le 1er juin 2026, lue le 10 novembre 2026 |
| 2 | Smic du 1er janvier au 31 mai 2026 : 12,02 € et 1 823,03 € ; hausse de 2,41 % | **Non relu** (la fiche ne donne que le montant en vigueur) ; cohérent : 12,02 € × 1,0241 = 12,31 € | Calcul |
| 3 | Formule de la RGDU 2026 : Smic annuel de 21 876,40 € ; seuil de 5 469,09 € par mois ; coefficient 0,3981 ; plancher de 2 % ; jusqu’à 3 Smic | **Non relu** (Urssaf non ouverte) ; cohérent : 12,02 € × 1 820 h = 21 876,40 € ; 3 × 1 823,03 € = 5 469,09 € | Calcul |
| 4 | Aide à l’embauche d’un apprenti, moins de 250 salariés : 5 000 € (aide unique, jusqu’au bac) ; 4 500 € (bac + 2) ; 2 000 € (bac + 3 à bac + 5) ; 6 000 € (handicap) ; première année seulement ; contrats conclus depuis le 8 mars 2026 et commencés avant le 1er janvier 2027 ; décret n° 2026-168 du 6 mars 2026 | Confirmé ; **précisé** : la condition de date ne vaut que pour l’aide exceptionnelle (4 500 € et 2 000 €) ; le montant est proratisé selon la durée réelle du contrat | Entreprendre.service-public.gouv.fr, fiche F23556, vérifiée le 22 juillet 2026, lue le 10 novembre 2026 |
| 5 | Montant de 2025 pour bac + 3 à bac + 5 (« 5 000 € ») | **Non relu** | — |
| 6 | JEI, CIR, CII : « exigent de la vraie recherche ou un vrai prototype, documentés » | Confirmé pour la JEI : société créée depuis le 1er janvier 2023 ; PME (moins de 250 personnes, chiffre d’affaires inférieur à 50 millions d’euros ou bilan inférieur à 43 millions) ; moins de 8 ans ; dépenses de recherche et développement d’au moins 20 % des charges ; capital détenu à 50 % au moins par certaines catégories de personnes ; pas de création par reprise ou restructuration | Fiche F31188, vérifiée le 1er juin 2026, lue le 10 novembre 2026 |
| 7 | CIR (repère) | 30 % des dépenses de recherche jusqu’à 100 millions d’euros, 5 % au-delà (métropole) ; les équipements servant à concevoir des prototypes sont admis s’ils servent à des opérations de recherche. Page ancienne : taux de 2026 à faire confirmer par l’expert-comptable | Fiche F23533, vérifiée le 21 février 2025, lue le 10 novembre 2026 |
| 8 | CII ; Bourse French Tech « dans l’année qui suit l’immatriculation, avant toute dépense » | **Non relus** | — |
| 9 | Taux patronaux 2026, Agirc-Arrco, prévoyance des cadres | **Non relus** | — |
| 10 | Coûts employeur (1,06 à 1,38 fois le brut ; environ 26 900 €, 43 900 € et 58 000 € par an) ; président de SAS (environ 3 500 € pour 2 000 € net) | Estimations de la note, **non vérifiables** sans simulateur : à faire refaire par l’expert-comptable ou avec le simulateur de l’Urssaf | — |
| 11 | Président de SAS assimilé salarié, sans assurance chômage | **Non relu** ce soir (fiches F36007 et F37366 citées par la note) | — |
| 12 | Article 4 du règlement sur l’IA (2 février 2025) ; « paquet omnibus » qui supprimerait le mot « suffisant » ; surveillance depuis le 2 août 2026 | **Non relus** : ne pas reprendre le point « omnibus » sans relire la page de la Commission | — |
| 13 | « au plus × 1,5 à × 2 en capacité, selon les hypothèses de la section « Gains » » | **Sans calcul** : la section n’existe pas | — |

### Corrections à appliquer

1. § 1, apprenti : ajouter « La condition de date (contrat conclu depuis le 8 mars 2026, commencé avant le 1er janvier 2027) ne vaut que pour l’aide exceptionnelle (4 500 € et 2 000 €) ; l’aide unique de 5 000 € (jusqu’au bac) n’a pas cette échéance ; l’aide est proratisée selon la durée réelle du contrat » (F23556).
2. « En bref », point 2 : « si le contrat commence avant le 1er janvier 2027 » → « si le contrat, conclu depuis le 8 mars 2026, commence avant le 1er janvier 2027 ».
3. « En bref », point 4 : préciser « JEI : au moins 20 % de dépenses de recherche et développement dans les charges, société de moins de 8 ans (F31188) ; CIR : 30 % des dépenses de recherche (F23533, page de février 2025) ».
4. « En bref », point 6 : « au plus × 1,5 à × 2 en capacité, selon les hypothèses de la section « Gains » » → « un troisième professionnel ajoute au plus la moitié de la capacité de deux personnes, moins le temps de formation et d’encadrement (estimation, ci-dessous) ».
5. § 1, Smic : ajouter « 22 404,20 € brut par an » (F2300).
6. § 4, « le « paquet omnibus numérique » … supprime l’exigence d’un niveau « suffisant » » : marquer « non relu le 10 novembre 2026 ».

### Compléments essentiels (parties manquantes)

**Aides à l’innovation, pour Marwin Tech** [Estimation ; interne]. Le statut de jeune entreprise innovante demande que la recherche et le développement pèsent au moins 20 % des charges : une activité de conseil, de paramétrage et de formation n’y arrive pas. Le CIR ne finance que des opérations de recherche au sens fiscal. Un prototype vraiment nouveau et documenté pourrait relever du CII (non relu). À faire valider par l’expert-comptable avant de compter sur une aide ; jamais dans un document client.

**Gains humains** [Estimation ; interne]. Deux associés à plein temps font deux unités de capacité ; un troisième professionnel formé en ajoute au plus une, soit au plus × 1,5 en capacité brute, moins le temps d’encadrement la première année (un apprenti : moins encore). Le vrai gain est la continuité (une relève en cas d’absence) et le parallèle (deux chantiers au lieu d’un). Aucun multiplicateur « × 10 » ou « × 100 » ne s’applique aux personnes.

### Sûr à reprendre

1. « Aujourd’hui, nous sommes deux : une étape et un essai à la fois. » — fait de Marwin Tech. **Page « moyens ».**
2. « Un ou deux collaborateurs formés : plusieurs chantiers en parallèle, une relève en cas d’absence, des emplois, si possible dans la Nièvre. » — **Page « moyens », fiche 09.**
3. « Le plus grand changement viendrait de personnes formées et disponibles, plus que d’une machine. » — **Page « moyens ».**
4. **Interne seulement** : Smic, aide à l’apprentissage, coûts employeur, rémunération des associés, JEI, CIR, tarifs d’indépendants (règle 4 du § 5 du brief du 9 novembre).

### Ce qui reste inconnu

- Le coût employeur réel d’un poste (convention collective, paramètres de la RGDU, mutuelle, prévoyance) : à faire calculer par l’expert-comptable.
- L’aide à l’apprentissage pour les contrats commençant en 2027 ; le montant de 2025 pour bac + 3 à bac + 5.
- Les conditions actuelles de la Bourse French Tech et le taux du CII en 2026 ; l’éligibilité de Marwin Tech à une aide quelconque.
- L’opérateur de compétences de Marwin Tech (il dépend du code d’activité) et ses plafonds.
- L’état du « paquet omnibus » sur l’article 4 du règlement sur l’IA.
- Les salaires pratiqués dans la Nièvre pour les profils visés.

