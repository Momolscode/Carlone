# Cabaret, commerces et suites : sources et limites du document client

Document interne — ne pas transmettre à GianLuca Carlone · 10 novembre 2026, relu et corrigé le même jour après les vérifications · Ce document n’est pas un avis juridique.

## En bref

1. Le document client (`pour-carlone/cabaret-et-commerces/2026-11-10-autorisations-et-echeances.md`, titre devenu « Cabaret, commerces et suites ») et son échéancier (`pour-carlone/cabaret-et-commerces/2026-11-10-echeancier.xlsx`, fabriqué par `outils/2026-11-10-orchestration/classeurs/echeancier.py`) reprennent les notes `audit/2026-11-10-preparation-des-livrables/travaux/k10-cabaret-spectacle.md`, `k11-commerces-urbanisme-baux.md` et, pour les suites, `k12-hebergement-logiciel-hotelier.md`.
2. Les trois notes ont maintenant leur partie « Vérification du 10 novembre 2026 » (k10, lignes 266 à 338 ; k11, lignes 229 à 304 ; k12, lignes 155 à 233). Le document client y est aligné : « documenté » seulement quand la vérification confirme une page officielle, citée par un numéro [1] à [10] en fin de document ; ce que la vérification n’a pas relu est passé « à vérifier » ou retiré.
3. Ajout demandé par BRIEF-2, § 11.4 : partie 5 « Vos neuf suites et l’espace bien-être » (sept lignes, une seule « documenté ») et sept lignes « Lieu 3 » dans l’échéancier. Aucune page officielle n’a été lue sur le sauna et le jacuzzi : « à vérifier ».
4. Aucun montant en euros dans le document client ni dans l’échéancier. Seul taux : la taxe sur les spectacles, 3,5 % de la billetterie hors taxe sur la valeur ajoutée (Centre national de la musique, page « Taxe », consultée le 10 novembre 2026 ; k10, lignes 287 et 312).
5. Contrôle mécanique : document client, 0 erreur, 1 alerte (« dépôt de garantie », terme juridique). Échéancier contrôlé sur le texte de ses cellules : 0 erreur, même alerte. La description complète du classeur (`xlsx-dump.py`) signale des « codes de l’audit » : ce sont les références de cellules (D10 à D30) ; faux positif.

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
| Sauna et jacuzzi | à vérifier | aucune page lue ; à chercher sur les pages officielles (règles des piscines et bains collectifs : déclaration, contrôle sanitaire, qualité de l’eau, registre ; BRIEF-2, § 11.4) |
| Assurance | à faire valider | BRIEF-2, § 11.4 |

Phrase d’ouverture : « D’après nos échanges, vous prévoyez neuf suites, un sauna et un jacuzzi dans l’établissement de la galerie (à confirmer avec vous). » Fait rapporté par Morgan Olsen le 10 novembre 2026, non vérifié auprès de GianLuca Carlone (BRIEF-2, § 11.1). Vocabulaire du § 11.2 : jamais « votre hôtel ».

## Pages officielles citées dans le document client

Toutes consultées le 10 novembre 2026 par les vérifications.

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

## Limites

- Les bâtiments, leurs usages, leurs surfaces et les sociétés exploitantes sont inconnus : le document est générique.
- Suites : adresse, capacité, ouverture, société exploitante et catégorie juridique inconnues (BRIEF-2, § 11.1 et 11.2).
- Le périmètre du site patrimonial remarquable de la commune n’a pas été vu.
- La durée totale jusqu’à l’ouverture du cabaret est inconnue : elle dépend des travaux.
- Rien n’a été demandé à une administration ; aucun professionnel n’a été consulté.

## À décider par Morgan Olsen et Mathys Couet avant vendredi 13 novembre

1. **Forme vendredi** : document montré à l’écran seulement, ou laissé à GianLuca Carlone. Sans les préalables, rien n’est laissé (BRIEF-2, § 10.4).
2. **Phrase d’ouverture de la partie 5** (ci-dessus) : la garder, ou la remplacer par une question posée en rendez-vous.
3. **Délai de quatre mois** : accepter la lecture de k11 (F31687), ou repasser la ligne en « à vérifier » comme le voulait k10.
4. **Lectures restantes** pour passer des lignes de « à vérifier » à « documenté » : licence IV et permis d’exploitation ; déclaration en mairie ; cuisine et hygiène ; maintien de l’arrêté de la Nièvre de 2003 ; article R. 1336-1 et arrêté du 17 avril 2023 (bruit) ; seuil de 50 personnes (article PE 2) ; article L752-1 ; classement de Cosne-Cours-sur-Loire en France ruralités revitalisation ; sauna et jacuzzi ; taxe de séjour de la commune ; affichage des prix ; classement en étoiles (k10, lignes 319 à 328 ; k11, lignes 283 à 289 ; k12, lignes 223 à 233).
