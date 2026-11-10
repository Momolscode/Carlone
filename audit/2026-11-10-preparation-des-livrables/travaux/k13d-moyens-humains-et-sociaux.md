# Les moyens humains et sociaux : rémunération, recrutement, formation, conditions de travail, aides

Note de travail interne — sources publiques consultées le 10 novembre 2026 — ce n'est pas un avis juridique, fiscal ou d'investissement.

Statut : interne. Contient des coûts salariaux, des hypothèses de rémunération des associés et des tarifs d'indépendants : rien de cela ne va tel quel à GianLuca Carlone (règle 4 du § 5 de `audit/2026-11-09-audit-presentation-et-offre/travaux/BRIEF.md` : jamais « la rémunération des associés » ni « le taux journalier » dans un texte client). Les aides destinées au client sont traitées dans `k7b-aides-publiques-numerique-ia.md` ; elles ne sont pas reprises ici.

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

