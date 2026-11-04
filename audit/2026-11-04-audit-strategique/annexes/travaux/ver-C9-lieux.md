# Vérification indépendante de `ex-C9-lieux.md` (lieux, galerie, cabaret, événements, vernissage)

Contrôle du 4 novembre 2026 pour l'audit Marwin Tech × GianLuca Carlone. Dépôt `Momolscode/Carlone` (branche main, commit 7b46602), lu sans aucune modification. Le fichier du lecteur n'a pas été modifié. Aucune action extérieure n'a été faite. Pour chaque élément, la source citée par le lecteur a été rouverte : les fichiers Markdown du dépôt, les textes extraits des deux PDF (cités ci-dessous par page du PDF d'origine), les métadonnées PDF (`pdfinfo`), l'historique git et les données du CRM (`crm/site/culture.json`).

Abréviations des chemins :
- « dossier » : `sources/dossier-partenariats-vieux-relais-et-le-m-2026-10-21.pdf` ;
- « diaporama » : `pour-carlone/vernissage-strates-diaporama.pdf` ;
- « idées » : `pour-carlone/vernissage-strates-idees.md` ;
- « page ChatGPT » : `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md` ;
- « catalogue » : `interne/offres-de-carlone-catalogue-crm.md` ;
- « offre Marwin » : `interne/offre-marwin-tech-remuneration-et-collaboration.md` ;
- « contexte » : `interne/contexte-projet-carlone.md`.

## 1. Les 15 éléments déterminants

| N° | Élément (n° du lecteur) | Verdict | Correction et source exacte |
| --- | --- | --- | --- |
| 1 | N° 1 : selon Morgan, GianLuca Carlone a racheté un « ancien bar restaurant hôtel avec cour pour en faire une galerie » [DR]. | Confirmé | Texte exact : « John-Lucas [sic, lire GianLuca] a racheté, selon Morgan, un ancien bar restaurant hôtel avec cour pour en faire une galerie » (`page ChatGPT:14`). Le code [DR] est juste, et l'indication [sic] est bien présente. |
| 2 | N° 2 : il a « déjà racheté six bâtiments » et ouvrira une galerie en 2027 [DR]. | Confirmé | `catalogue:9`. La source déclarée est « Messages de Morgan du 2 novembre 2026 » (`catalogue:140`). Le code [DR] est juste : le catalogue l'écrit comme un fait, mais il le tient de Morgan. Voir l'omission 2 pour la suite de la même ligne. |
| 3 | N° 3 : GianLuca « souhaite racheter « le M » » pour un cabaret [DR]. | Confirmé | `page ChatGPT:15`, ligne « Cabaret ». Prochaine décision indiquée sur la même ligne : « Confirmer le lieu et le stade de l'acquisition, puis établir la faisabilité de l'exploitation ». |
| 4 | N° 4 et § 1 : dans le dossier, « le bar et le restaurant qui changent de main », « Nous reprenons » ; le repreneur n'est pas nommé ; Carlone est cité 0 fois ; 34 pages, produit par Chromium le 21 oct. à 18:30 UTC. | Confirmé | Dossier, p. 32 (messages 1 à 3). Recherche dans tout le texte : 0 occurrence de « Carlone », « John », « Lucas », « galerie » ou « cabaret ». Métadonnées PDF : 34 pages, Creator « Chromium », CreationDate « Wed Oct 21 18:30:20 2026 UTC ». |
| 5 | § 4, « Nature du M » et « Nature du Vieux Relais » (n° 5 et 6) : selon le dossier, le M serait le restaurant et le Vieux Relais le bar ; selon `crm/PASSATION.md:41`, c'est l'inverse. | Corrigé (précision) | La contradiction est réelle, mais elle existe déjà **à l'intérieur** du dossier de Mathys. Le M y reçoit aussi des usages de bar : « Apéritif offert au M » (dossier, p. 2), « matchs de l'USON » retransmis au M (dossier, p. 30). Le Vieux Relais y reçoit une « salle privatisée » pour des séminaires (dossier, p. 10). La lecture « Vieux Relais = bar, M = restaurant » vient de l'ordre des mots de la p. 32. Elle est appuyée par la p. 29 (« à la carte du M et au verre au Vieux Relais ») et par la p. 6. Côté CRM, le Vieux Relais remplace « le bar » dans les textes culture (`crm/merge_culture.py:96-98`). On y parle aussi de « clientèle de l'hôtel » (`crm/site/culture.json:3020`) et de « bar-hôtel » (`crm/site/culture.json:3325`). Conclusion : le Vieux Relais est vraisemblablement un bar avec hôtel, et peut-être un restaurant (`crm/PASSATION.md:41`). Le M est restaurant ou bar selon la pièce. La portée reste « forte ». |
| 6 | N° 7 [FV] : aucun document ne dit noir sur blanc que Le Vieux Relais et le M appartiennent à GianLuca Carlone. | Confirmé (préciser le périmètre) | J'ai cherché « Vieux Relais » dans tout le dépôt (28 fichiers). Aucune phrase n'attribue la propriété de ces lieux à GianLuca. Le seul lien entre lui et le M est un souhait de rachat (`page ChatGPT:15`). Le code [FV] est acceptable s'il est formulé ainsi : « constat négatif, par recherche dans le texte du dépôt au commit 7b46602 ». La source `contexte:160` n'est qu'une synthèse. |
| 7 | N° 17 [FV] : le CRM, « pensé le 21 octobre » pour les lieux, « sert au 2 novembre » à vendre des œuvres ; le volet « lieux » serait abandonné « sans décision écrite ». | Corrigé | Le changement est documenté dès le **22 octobre**, le lendemain du dossier. Le document de reprise est « rédigé le 22/10/2026 » (`crm/PASSATION.md:37`). Il pose : « Principe du CRM […] : proposer aux entreprises d'acheter des œuvres d'art » (`crm/PASSATION.md:43`). La section « Mise à jour du 22/10/2026 » (`crm/PASSATION.md:3`) contient « Réorientation vers la vente d'œuvres d'art faite » (`crm/PASSATION.md:5`). Le 23 octobre, le zip du CRM contient les champs « art » (`contexte:42`). Une consigne écrite existe : « Ne jamais parler du Vieux Relais ni du M aux entreprises […] pour l'instant » (`crm/PASSATION.md:49`). Elle ne donne ni motif ni décideur. Le « rdv de demain » du dossier (p. 33) correspond au rendez-vous du 22 octobre (`contexte:43`), dont l'issue est inconnue (`contexte:159`). Il faut garder [FV], mais avec `crm/PASSATION.md` comme source primaire et non la synthèse `contexte:47`. |
| 8 | N° 27 et § 3 : six visuels « générés par IA le 4 novembre » [FV] ; fichiers PNG « datés du 4 nov. à 16:03 ». | Corrigé | Les six PNG existent bien [FV] (`pour-carlone/visuels/1-source.png` à `6-fossiles-de-la-loire.png`). En revanche, l'heure 16:03 (UTC) est celle de l'extraction du dépôt sur disque. Tous les fichiers de `pour-carlone/` portent 16:03:36, y compris des PDF d'autres dates. Cette heure ne date donc pas la génération des images. Les visuels ont été versés dans git par le commit fa5998a (4 nov. 2026, 16:38 +0100). Leur génération par IA et sa date sont **déclarées** par les pièces (`idées:29` ; diaporama, p. 4 à 9, « Visuel généré par IA ») : c'est du [DR], pas du [FV]. |
| 9 | N° 26 : « Onze idées, dont huit faisables », plus dix autres [HY]. | Confirmé | Premier tableau : 11 lignes (`idées:61-71`), dont 8 « Oui » (`idées:61-68`) et 3 conditionnelles (`idées:69-71`). Second tableau : 10 lignes (`idées:81-90`). Le décompte est un fait vérifié [FV]. Le mot « faisable » reste une affirmation non testée : le code [HY] du lecteur convient. |
| 10 | N° 33 et 34, et § 3 : trois formats, de 6 à 30 journées et de 4 500 à 22 500 € HT, à 750 € HT la journée ; part de la capacité mensuelle de 20 journées. | Confirmé | `idées:98-102` ; diaporama, p. 10 (« estimation à 750 € HT la journée »). Les produits sont exacts : 6 × 750 = 4 500 ; 10 × 750 = 7 500 ; 12 × 750 = 9 000 ; 18 × 750 = 13 500 ; 20 × 750 = 15 000 ; 30 × 750 = 22 500. Les parts de 20 journées sont justes : 30 à 50 %, 60 à 90 %, 100 à 150 %. Le taux de 750 € n'est justifié nulle part dans ces pièces. |
| 11 | N° 36 et § 4, « Absorption dans le forfait » : le vernissage passe « sans supplément s'il tient dans les 20 journées », alors que le premier mois est déjà réparti. | Confirmé, avec une nuance | Sources : `idées:110` ; diaporama, p. 11 ; offre Marwin:54-61 (6 + 7 + 4 + 3 = 20 jours). Nuance : les deux pièces prévoient déjà une facturation à part « si le mois est déjà plein » (`idées:111` ; diaporama, p. 11, « En option Au même taux »). Le vrai risque est donc qu'aucun critère ne définit un mois « plein ». Une option facturable, elle, existe. |
| 12 | N° 32 et § 4, « Présence de BOJ.ART » et « Prérequis du format 1 » : le diaporama cite encore BOJ.ART et cache la dépendance à Medhi. | Confirmé | Diaporama, p. 1 : « Marwin Tech et BOJ.ART, pour M. Carlone ». Diaporama, p. 12 : « avec Medhi, BOJ.ART ». Le prérequis donné au client est « un lieu et une date » (diaporama, p. 10). Le document interne exige au contraire « Le parc de Medhi en état » (`idées:100`) et l'accord de Medhi (`idées:122`). Les quatre questions de la p. 12 remplacent cet accord par « Le format retenu ». À ajouter : Medhi est encore nommé aux p. 6, 7 et 9, et la p. 1 porte la marque « State Of The Art · Proposition d'événement ». |
| 13 | N° 37 et § 4 : « La première présentation de l'œuvre, dans votre galerie » repose sur l'option création STRATES, retirée le 4 novembre. | Confirmé | Diaporama, p. 7 et p. 11. Le lien avec l'option création « en échange du financement » est écrit en `idées:112`. La phase 1 coûte environ 10 000 € HT, contre une exclusivité sur la série et les films (`contexte:79`). Le retrait de l'option est [DR] (`note-point-4-novembre-et-activites.md`, § C). |
| 14 | N° 60 : l'offre ChatGPT serait la « seule pièce » à prévoir une étude de faisabilité du cabaret. | Corrigé | `page ChatGPT:15` prévoit aussi d'« établir la faisabilité de l'exploitation » du cabaret, comme prochaine décision. `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:42` est seulement la seule pièce qui en fait un livrable (dossier, planning, prestataires, budgets). |
| 15 | N° 62 : « 97 artistes » repérés dans l'onglet Culture [DR]. | Corrigé | `crm/site/culture.json` (version du dépôt) contient 97 fiches « prospects ». Seules 38 relèvent de la famille « Artistes », dont 22 de type « Artiste ». Les autres : 30 « Associations », 17 « Lieux & institutions », 12 « Réseaux & événements ». `crm/PASSATION.md:56` parle de « 97 artistes, associations, lieux et réseaux », et `contexte:43` de « 97 prospects ». Le catalogue (l. 47 et 81) surestime donc le nombre d'artistes. La version FinanceScope du 30 octobre n'a pas été vue : le chiffre exact dans cette version reste [IN]. |

**Autres points revus sans écart** (sources rouvertes, citations exactes) : n° 8, 9, 11 à 16, 19 à 24, 30, 31, 35, 41 à 46, 48 à 50, 52 à 54, 57 à 59, 61 et 63 ; contradictions « Liste des postes hors forfait » (`idées:104` contre offre Marwin:20 ; diaporama, p. 10, sans « consommables »), « Horizon des fossiles » et « Ouverture des sources ». Trois nuances mineures :
- n° 51 : le rapport « Fusion » mentionne un « îlot sécurisé », sans autre précision (`sources/rapport-recherche-fusion-des-univers.md:52`). Il vaut mieux écrire « sécurité évoquée en un mot, non traitée » que « non traitée ».
- n° 59 : le volet Piloter comprend aussi les « séjours des invités » (offre Marwin:52). Le lecteur ne le reprend pas (voir l'omission 3).
- n° 55 : la ville n'est pas nommée à la l. 16, mais la l. 7 de la même page situe les opérations à « Cosne-Cours-sur-Loire » (`page ChatGPT:7`).

## 2. Contrôle des codes

- **Aucun fait rapporté par Morgan n'est classé [FV].** Les n° 1, 2, 3 et 55, la décision du 4 novembre (n° 32) et l'agenda (§ 3) sont bien en [DR]. C'est correct.
- **Codes à corriger :**
  - n° 17 : [FV] à conserver, mais avec `crm/PASSATION.md:5, 43, 49` comme source primaire, et non `contexte:47`. La date est aussi à corriger (élément 7 ci-dessus).
  - n° 27 et § 3 : la génération par IA et la date sont [DR]. L'heure « 16:03 » n'est pas un fait daté : elle est à retirer.
  - n° 7 : [FV] uniquement comme constat négatif de recherche, en précisant son périmètre.
  - n° 10 : plutôt [DR] que [HY]. Le dossier présuppose l'existence de « travaux du bar et du restaurant » (dossier, p. 23) : l'auditeur ne fait là aucune hypothèse.
  - n° 56 : plutôt [DR] que [PR]. C'est un constat d'organisation tiré de la page ChatGPT, d'après les informations de Morgan, et non une proposition de Marwin.
- **Codes justes à signaler :** n° 16 [FV], car la règle est écrite ; n° 22 et 23 [FV], car l'absence de prix et de vendeur est constatée dans le catalogue ; n° 33 [ES] ; n° 57 [HY], la source disant elle-même « à titre d'hypothèse » (`page ChatGPT:65`).

## 3. Contrôle du nom

- Le lecteur n'emploie jamais de variante fautive. Les mentions « John-Lucas » sont citées avec « [sic, lire GianLuca] » (ex-C9-lieux.md:21 et 201).
- Le décompte du lecteur est exact : 9 occurrences de « John-Lucas » dans la page ChatGPT, aux lignes 1, 7, 13, 14, 15, 16, 18, 32 et 65. Il n'y a aucune variante dans `idées`, le diaporama, le rapport « Fusion », le catalogue ou le dossier : 0 résultat pour john, lucas, gianluca, jean-luc et gian.
- Point de forme : le lecteur emploie souvent « Carlone » seul (par exemple ex-C9-lieux.md:22, 23, 75, 219). Ce n'est pas une erreur d'identité. Mais la consigne demande « GianLuca Carlone », « GianLuca » ou « M. Carlone » : il faut harmoniser dans la synthèse.

## Omissions

1. **L'onglet Culture du CRM contient déjà un plan d'événements et un cadre pratique pour le Vieux Relais.** Le lecteur l'aurait trouvé par `crm/PASSATION.md:50 et 56`, qu'il a lu en partie. Contenu de `crm/site/culture.json` :
   - un « playbook » (l. 2881) de 10 formats, dont « Expo tournante et vernissage avec l'artiste » (l. 2884) et « Résidence d'artiste à l'hôtel » (l. 3020) ;
   - un calendrier local de 20 dates ;
   - 23 règles pratiques : spectacles vivants sans formalité jusqu'à 6 représentations par an (l. 3202), Sacem (l. 3228), assurance « clou à clou » (l. 3272), vente au déballage (l. 3312), rémunération et conventions des artistes ;
   - 10 pistes de financement, dont le pass Culture pour un « bar-hôtel » (l. 3325) ;
   - 13 idées d'événements qui nomment le Vieux Relais (par exemple l. 1183, 1329 et 1384), ce que la règle de `crm/PASSATION.md:50` autorise auprès des artistes et des associations.

   Portée :
   - (a) C'est la réponse déjà construite au seul besoin rapporté, « réunir des artistes et peintres » (`page ChatGPT:16`). Elle est antérieure au vernissage STRATES et ne dépend ni de Medhi ni du bras. Cela nuance le point d'audit 2 du lecteur, et il faut comparer les deux approches devant GianLuca.
   - (b) Le point d'audit 8, « obligations d'exploitation absentes de toutes les pièces », n'est vrai que pour les six pièces du lecteur. Une base existe, mais elle doit être revérifiée sur les sources officielles : certaines règles s'appuient sur une consultation du 12 août 2025 (l. 3228).
   - (c) Ce plan confirme la fonction hôtelière du Vieux Relais.

   Codes : l'existence du fichier est [FV] ; son contenu est [PR] ; ses règles juridiques sont [DR], à faire valider par un professionnel.
2. **Des bureaux proposés par GianLuca, donc un rôle de bailleur.** La même ligne que les « six bâtiments » dit : « Il propose de leur fournir des bureaux, une bonne rémunération, et envisage d'investir dans leur activité » (`catalogue:9`, [DR], messages de Morgan du 2 novembre, `catalogue:140`). L'inventaire « lieux » l'ignore. Si ces bureaux se trouvent dans l'un de ses bâtiments, GianLuca serait à la fois client, bailleur et investisseur possible (`DEMANDE.md`, § 13). Questions à ajouter : quel bâtiment ? À quel titre (bail, mise à disposition gratuite, convention) ? À quel coût ? Que devient l'occupation si la collaboration prend fin ?
3. (Secondaire) **L'hébergement.** Plusieurs pièces supposent une activité hôtelière : les « séjours des invités » (offre Marwin:52), le mot « chambres » parmi les termes interdits du CRM (`crm/merge.py:152`) et la « Résidence d'artiste à l'hôtel » (`crm/site/culture.json:3020`). Les questions 8 à 11 du lecteur ne couvrent pas les obligations propres à l'hébergement. Il faut les ajouter à la liste à faire vérifier par un professionnel, sans rien affirmer sur leur contenu.

## Bilan

Sur les 15 éléments : **10 confirmés** (dont 2 avec une précision de périmètre ou une nuance), **5 corrigés**, 0 non vérifiable. Les corrections importantes :
- le CRM a changé de but dès le 22 octobre, avec une consigne écrite (`crm/PASSATION.md:5, 43, 49`) ;
- les « 97 artistes » sont en réalité 97 prospects culturels, dont 38 artistes ;
- l'horodatage des visuels n'est pas une preuve de date, et leur génération par IA est [DR] ;
- le dossier de Mathys se contredit lui-même sur la nature du M et du Vieux Relais ;
- l'étude de faisabilité du cabaret apparaît dans deux pièces, pas une.

À cela s'ajoutent cinq codes à ajuster et trois omissions, dont le plan d'événements culturels déjà présent dans le CRM.
