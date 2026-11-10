# Cabaret, commerces et suites : sources et limites du document client

Document interne — ne pas transmettre à GianLuca Carlone · 10 novembre 2026, relu et corrigé le même jour après les vérifications, mis à jour le 11 novembre 2026 (audit final : partie 5, jacuzzi et sauna) · Ce document n’est pas un avis juridique.

## En bref

1. Le document client (`pour-carlone/cabaret-et-commerces/2026-11-10-autorisations-et-echeances.md`, titre devenu « Cabaret, commerces et suites ») et son échéancier (`pour-carlone/cabaret-et-commerces/2026-11-10-echeancier.xlsx`, fabriqué par `outils/2026-11-10-orchestration/classeurs/echeancier.py`) reprennent les notes `audit/2026-11-10-preparation-des-livrables/travaux/k10-cabaret-spectacle.md`, `k11-commerces-urbanisme-baux.md` et, pour les suites, `k12-hebergement-logiciel-hotelier.md` ; pour le jacuzzi et le sauna, `k14-sauna-jacuzzi-espace-bien-etre.md`.
2. Les trois premières notes ont leur partie « Vérification du 10 novembre 2026 » (k10, lignes 266 à 338 ; k11, lignes 229 à 304 ; k12, lignes 155 à 233). Le document client y est aligné : « documenté » seulement quand une page officielle est citée, par un numéro [1] à [18] en fin de document ; ce que la vérification n’a pas relu est passé « à vérifier » ou retiré. La note k14 n’a pas de partie « Vérification » : ses lignes marquées « sûr » sont des pages officielles lues le 10 novembre 2026 avec un outil qui résume (k14, ligne 7) ; toute citation exacte est à relire avant un usage juridique.
3. Ajout demandé par BRIEF-2, § 11.4 : partie 5 « Vos neuf suites et l’espace bien-être », portée le 10 novembre au soir à douze lignes, dont cinq « documenté » (fiche de police ; jacuzzi : déclaration, eau et affichage, entretien, règles du 1er janvier 2027), et douze lignes « Lieu 3 » dans l’échéancier (n° 23 à 34). Sauna : aucune règle sanitaire propre trouvée, « à faire valider ».
4. Aucun montant en euros dans le document client ni dans l’échéancier. Seul taux : la taxe sur les spectacles, 3,5 % de la billetterie hors taxe sur la valeur ajoutée (Centre national de la musique, page « Taxe », consultée le 10 novembre 2026 ; k10, lignes 287 et 312).
5. Contrôle mécanique, relancé le 11 novembre 2026 : document client, 0 erreur, 2 alertes lues (« dépôt de garantie », terme juridique ; « surveillance des eaux de piscine », titre de l’arrêté du 23 juin 2026, source [14]) ; cinq pages en rendu compact. Échéancier contrôlé sur le texte de ses cellules : 0 erreur, une alerte (« garanties », même terme juridique). La description complète du classeur (`xlsx-dump.py`) signale des « codes de l’audit » : ce sont les références de cellules (D10 à D35) ; faux positif.

## Ce que la relecture a changé, et pourquoi

| Point du document client | Avant | Après | Raison (source) |
| --- | --- | --- | --- |
| Délai de l’autorisation de travaux | « quatre mois, cinq avec permis » | « quatre mois avec une déclaration préalable, cinq avec un permis » [3] ; architecte obligatoire pour le permis d’une société | k11, lignes 243, 272 et 274 (F31687 lue). k10, ligne 285, n’avait pas trouvé « quatre mois » ; k11 a lu la fiche officielle : elle l’emporte |
| Licence de boissons, permis d’exploitation, cuisine, hygiène, débit de boissons | « Documenté » ; « vingt heures », « quatorze heures », « accord du préfet » | « À vérifier » ; durées et accord du préfet retirés | k10, ligne 328 : non revérifiés |
| Étude d’impact sonore ; contrôle du son tous les deux ans ; enregistrements gardés six mois | « Documenté » | « À vérifier » ; « six mois » retiré | k10, lignes 291, 317 et 325 |
| Fermeture tardive (4 heures, une nuit par semaine, un an au plus) | détails de l’arrêté de 2003 | « heures de fermeture et dérogation éventuelle », à vérifier | k10, ligne 315 : interne seulement tant que le maintien en vigueur n’est pas confirmé |
| Commission de sécurité avant l’ouverture ; visites tous les trois ou cinq ans | « Documenté » | « À vérifier », selon la catégorie | k10, lignes 284 et 322 (seuil de 50 personnes non vérifié) ; k12, ligne 176 |
| Vérifications techniques « chaque année » | annuelles | tous les trois ans au plus pour la 5e catégorie, depuis le 1er juillet 2026 [6] | k11, lignes 244, 260 et 276 |
| Taxe sur les spectacles | « avant la fin du troisième mois » | « hors taxe sur la valeur ajoutée », « au plus tard le dernier jour du troisième mois qui suit la représentation » [2] | k10, lignes 287 et 312 |
| Déclaration de spectacles | — | « sauf opposition du préfet » ; numéro du récépissé sur affiches et billets [1] | k10, lignes 280 et 309 |
| Taux de TVA du billet | absent | taux normal en principe, exceptions possibles [5] | k10, ligne 314 |
| Autorisation des caméras « tous les cinq ans » | « Documenté » | retirée du tableau des rythmes | k10, ligne 328 (vidéoprotection non revérifiée) |
| Autorisation d’exploitation commerciale | « ne vise que … plus de 1 000 m² », « Documenté » | « s’ajoute pour les grands magasins », seuils à vérifier | k11, ligne 287 (article L752-1 non relu) |
| Enseignes au sol, 2 novembre 2027 | citée | retirée | k11, lignes 245 et 261 : ne pas la citer tant que la population de l’agglomération n’est pas vérifiée |
| Déclaration préalable | « délai allongé » | un mois, deux en secteur protégé ; dépôt en ligne pour une société dans une commune de plus de 3 500 habitants [4] | k11, lignes 239, 242, 271 et 273 |
| Dépôt de garantie | « plafonné … depuis le 28 mai 2026 » | local de commerce, depuis fin mai 2026, un trimestre de loyer, garanties comprises ; date exacte à préciser par l’avocat [8] | k11, lignes 247, 262 et 278 |
| Bail dérogatoire | « trois ans au plus » | et règle du mois après le terme [7] | k11, lignes 246 et 275 |
| France ruralités revitalisation | « La commune est classée » | « si le classement se confirme » ; cinq ans, puis trois ans en partie [9] | k11, lignes 249 et 280 (classement de Cosne non relu) |
| « Changement d’usage » | — | « changement de destination », terme de k11 | k11, ligne 27 |
| Échéances « dans votre logiciel de gestion des propriétés » | — | « dans le registre de vos bâtiments, relié à vos logiciels » | BRIEF-2, § 10.1 et 10.3 : « gestion de propriété » désigne le logiciel hôtelier ; les échéances vont dans le registre |

## Partie 5 du document client : les suites et l’espace bien-être

| Ligne | Statut | Source |
| --- | --- | --- |
| Sécurité incendie : locaux à sommeil, visites de la commission, effet sur l’ensemble si les lieux communiquent | à faire valider | BRIEF-2, § 11.4 ; k12, ligne 176 (l’article GE 4 soumet aux visites la 5e catégorie avec locaux à sommeil ; périodicité non trouvée) |
| Fiche de police : clients étrangers, Union européenne comprise, conservée six mois | documenté [10] | k12, lignes 172 et 214 (F17452, fiche des chambres d’hôtes). Articles R814-1 à R814-3 du code de l’entrée et du séjour des étrangers non relus : application aux suites à faire valider |
| Taxe de séjour, au réel ou au forfait | à vérifier | k12, ligne 105 ; tarifs de la commune non trouvés (k12, ligne 230 ; k11, ligne 286) |
| Affichage des prix | à vérifier | k12, ligne 106 ; arrêté du 18 décembre 2015 non relu (k12, ligne 231) |
| Classement en étoiles, volontaire | à vérifier | k12, ligne 101 ; textes non relus (k12, ligne 229) |
| Jacuzzi partagé : déclaration à la mairie avant l’ouverture, au plus tard deux mois avant selon l’ARS ; un jacuzzi réservé au client d’une seule suite n’est pas d’usage collectif | documenté [11] [12] [14] | k14, lignes 22, 29 et 30 (code de la santé publique, art. L1332-1 ; ARS Bourgogne-Franche-Comté, page du 19 juin 2025 ; arrêté du 23 juin 2026, art. 1er) ; installation réelle à faire valider |
| Jacuzzi : eau et affichage (carnet sanitaire, derniers résultats, fréquentation maximale, quinze minutes, enfants de moins de dix ans) | documenté [13] | k14, lignes 38 et 51 (art. D1332-10 et D1332-7) |
| Jacuzzi : entretien (150 litres par baigneur ; vidanges) | documenté [15] | k14, lignes 53 et 54 (arrêté du 19 décembre 2025, art. 4 et 15) |
| Jacuzzi : à partir du 1er janvier 2027 (analyses par un laboratoire accrédité, aux frais de l’exploitant ; rythme selon la capacité d’accueil) | documenté [14] [16] | k14, lignes 24, 44 et 45 (décret n° 2026-118 du 20 février 2026, art. 2 ; arrêté du 23 juin 2026, annexes I et II) ; capacité des suites inconnue |
| Sauna | à faire valider | k14, lignes 60 et 67 à 70 : aucune règle sanitaire propre trouvée ; obligation générale de sécurité des services [17] ; règlement sanitaire de la Nièvre non lu |
| Sécurité des bassins (dispositif contre la noyade) | à faire valider | k14, ligne 61 (fiche F1722 [18]) : application à un jacuzzi intérieur non tranchée |
| Assurance | à faire valider | BRIEF-2, § 11.4 |

Phrase d’ouverture : « D’après nos échanges, vous prévoyez neuf suites, un sauna et un jacuzzi dans l’établissement de la galerie (à confirmer avec vous). » Fait rapporté par Morgan Olsen le 10 novembre 2026, non vérifié auprès de GianLuca Carlone (BRIEF-2, § 11.1). Vocabulaire du § 11.2 : jamais « votre hôtel ». La suite du paragraphe nomme les inconnues relevées par k14 (ligne 5) : emplacement du jacuzzi, partagé ou propre à une suite ; accès vendu ou non à des personnes extérieures.

Les mêmes règles sont reprises dans la fiche 02 (`pour-carlone/fiches/2026-11-10-fiche-02-vos-neuf-suites-et-l-espace-bien-etre.md`, « À faire valider par vos professionnels ») : mêmes textes, mêmes dates.

## Pages officielles citées dans le document client

Les pages 1 à 10 ont été consultées le 10 novembre 2026 par les vérifications ; les pages 11 à 18, le même jour, par la note k14 (sans partie « Vérification » ; lecture par un outil qui résume).

1. Service Public Entreprendre, F22365, vérifiée le 5 avril 2024 — https://entreprendre.service-public.gouv.fr/vosdroits/F22365 (k10, ligne 332)
2. Centre national de la musique, « Taxe », date non affichée — https://cnm.fr/taxe/ (k10, ligne 333)
3. Service Public Entreprendre, F31687, vérifiée le 20 septembre 2024, plus ancienne que les autres fiches — https://entreprendre.service-public.gouv.fr/vosdroits/F31687 (k11, ligne 296)
4. Service Public Entreprendre, F17578, vérifiée le 22 octobre 2026 — https://entreprendre.service-public.gouv.fr/vosdroits/F17578 (k11, ligne 295)
5. BOFiP, BOI-TVA-LIQ-30-20-40, 7 février 2024 — https://bofip.impots.gouv.fr/bofip/167-PGP.html/identifiant=BOI-TVA-LIQ-30-20-40-20240207 (k10, ligne 334)
6. Légifrance, arrêté du 1er décembre 2025, lu par extraits — https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053020948 (k11, ligne 303)
7. Service Public Entreprendre, F32304, vérifiée le 9 juin 2026 — https://entreprendre.service-public.gouv.fr/vosdroits/F32304 (k11, ligne 298)
8. Légifrance, loi n° 2026-403 du 26 mai 2026, article 62, lu par extraits — https://www.legifrance.gouv.fr/loda/id/JORFTEXT000054131304 ; F36538 (k11, ligne 301)
9. Service Public Entreprendre, F31139, vérifiée le 21 février 2026, lue en partie — https://entreprendre.service-public.gouv.fr/vosdroits/F31139 (k11, ligne 299)
10. Service Public Entreprendre, F17452, vérifiée le 21 mai 2026, lue le 10 novembre 2026 (k12, lignes 170 et 172)
11. Légifrance, code de la santé publique, art. L1332-1 à L1332-9 (piscines et baignades), versions en vigueur le 10 novembre 2026 — https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072665/LEGISCTA000006171063/ (k14, ligne 102)
12. Agence régionale de santé de Bourgogne-Franche-Comté, « Piscine : réglementation en vigueur », 19 juin 2025 — https://www.bourgogne-franche-comte.ars.sante.fr/piscine-reglementation-en-vigueur (k14, ligne 109)
13. Légifrance, code de la santé publique, art. D1332-7, version du 1er janvier 2022 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000019506574 ; art. D1332-10, dans la section des art. D1332-1 à D1332-11-1 — https://www.legifrance.gouv.fr/codes/id/LEGISCTA000019506535 (k14, lignes 103 et 104)
14. Légifrance, arrêté du 23 juin 2026 relatif à la surveillance des eaux de piscine, en vigueur le 1er janvier 2027 — https://www.legifrance.gouv.fr/jorf/id/JORFSCTA000054321874 (k14, ligne 106)
15. Légifrance, arrêté du 19 décembre 2025 relatif aux dispositions techniques applicables aux piscines — https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053158834 (k14, ligne 107)
16. Légifrance, décret n° 2026-118 du 20 février 2026, art. 2, en vigueur le 1er janvier 2027 — https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000053524186 (k14, ligne 105)
17. Légifrance, code de la consommation, art. L421-3, version du 13 décembre 2024 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032225448 (k14, ligne 110)
18. Service Public, « Dispositif de sécurité des piscines privées familiales et collectives », F1722, vérifiée le 13 février 2026 — https://www.service-public.gouv.fr/particuliers/vosdroits/F1722 (k14, ligne 112)

## Limites

- Les bâtiments, leurs usages, leurs surfaces et les sociétés exploitantes sont inconnus : le document est générique.
- Suites : adresse, capacité, ouverture, société exploitante et catégorie juridique inconnues (BRIEF-2, § 11.1 et 11.2).
- Espace bien-être : jacuzzi partagé ou propre à une suite, volume du bassin, capacité d’accueil en personnes, accès vendu ou non à des personnes extérieures : inconnus (k14, lignes 5 et 95). Les règles du jacuzzi et leur rythme en dépendent.
- Le périmètre du site patrimonial remarquable de la commune n’a pas été vu.
- La durée totale jusqu’à l’ouverture du cabaret est inconnue : elle dépend des travaux.
- Rien n’a été demandé à une administration ; aucun professionnel n’a été consulté.

## À décider par Morgan Olsen et Mathys Couet avant vendredi 13 novembre

1. **Forme vendredi** : document montré à l’écran seulement, ou laissé à GianLuca Carlone. Sans les préalables, rien n’est laissé (BRIEF-2, § 10.4).
2. **Phrase d’ouverture de la partie 5** (ci-dessus) : la garder, ou la remplacer par une question posée en rendez-vous.
3. **Délai de quatre mois** : accepter la lecture de k11 (F31687), ou repasser la ligne en « à vérifier » comme le voulait k10.
4. **Lectures restantes** pour passer des lignes de « à vérifier » à « documenté » : licence IV et permis d’exploitation ; déclaration en mairie ; cuisine et hygiène ; maintien de l’arrêté de la Nièvre de 2003 ; article R. 1336-1 et arrêté du 17 avril 2023 (bruit) ; seuil de 50 personnes (article PE 2) ; article L752-1 ; classement de Cosne-Cours-sur-Loire en France ruralités revitalisation ; taxe de séjour de la commune ; affichage des prix ; classement en étoiles (k10, lignes 319 à 328 ; k11, lignes 283 à 289 ; k12, lignes 223 à 233). Pour l’espace bien-être, depuis la note k14 : règlement sanitaire de la Nièvre (sauna) ; régime des petits bassins avant le 1er janvier 2027 ; dispositif contre la noyade et arrêté du 14 septembre 2004 ; règles du code du sport si l’accès est vendu à des personnes extérieures (k14, lignes 93 à 98).
5. **Note k14** : la faire relire par une seconde lecture (partie « Vérification »), comme les autres notes, avant de laisser le document ou la fiche 02, ou accepter ses lectures telles quelles. Quatre des cinq lignes « documenté » de la partie 5 s’appuient sur elle seule.
