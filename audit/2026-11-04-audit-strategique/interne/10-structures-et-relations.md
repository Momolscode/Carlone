# Structures juridiques et relations contractuelles

Audit Marwin Tech × GianLuca Carlone · livrable 10 sur 15 · 4 novembre 2026
Statut : interne (rémunérations des associés, pacte, risques juridiques de Marwin, questions aux professionnels ; ne pas transmettre à GianLuca Carlone)
Sources principales : `travaux/syn-droit.md` (lu en entier) ; `travaux/rj-R1-structures.md`, `travaux/rj-R2-fiscal.md`, `travaux/rj-R3-travail-contrats.md`, `travaux/rj-R5-art-lieux.md` et leurs contrôles `travaux/ver-R1-structures.md`, `travaux/ver-R2-fiscal.md`, `travaux/ver-R3-travail-contrats.md`, `travaux/ver-R5-art-lieux.md` ; `travaux/ex-C3-structure.md` et `travaux/ver-C3-structure.md` ; `modele-financier/structures.md` ; `travaux/strategie-retenue.md` (sections 7, 8.6, 8.8 et 9) ; pièces d'origine du dépôt Momolscode/Carlone (commit 7b46602), rouvertes en lecture seule le 4 nov. 2026.
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu. Sans autre précision, une [PR] vient de la stratégie retenue ; « [PR, ce livrable] » signale une proposition nouvelle. JP : journée-personne de 7 h.

**Méthode.**
- **Règles de droit.** Elles ont été relevées le 4 nov. 2026 par les chercheurs juridiques de l'audit, puis contrôlées le même jour sur les sites officiels par des contrôleurs indépendants. Quand un contrôle corrige un mémo, je retiens la correction. Je n'ai pas rouvert moi-même les sites officiels : chaque URL est donnée avec la date de consultation de l'audit (4 nov. 2026) et le contrôle qui l'a vérifiée. La liste complète est en annexe.
- **Pièces du dépôt.** Je les ai rouvertes en lecture seule pour chaque point déterminant. Les PDF sont cités par page, d'après leur texte extrait.
- **Diaporama client** « Offre Marwin Tech pour Carlone » : cité d'après sa copie du 4 nov., hors dépôt (`slides/…`).
- **Aucune simulation officielle.** urssaf.fr renvoyait une erreur HTTP 503 le 4 nov. Tous les revenus sont des [ES] (`travaux/ver-R1-structures.md:8`).
- **Règles de 2027.** Les lois de finances et de financement de la sécurité sociale pour 2027 sont en discussion. Une société créée fin 2026 aura un premier exercice soumis aux règles de 2027 : tout est à revérifier en janvier 2027 (`travaux/syn-droit.md:23`).

**Ce que ce livrable ajoute** : la comparaison des formes sur les scénarios de l'audit ; la répartition des pouvoirs ; le traitement de chaque rôle proposé par GianLuca et de leur cumul ; le réexamen des recommandations des 29 et 30 octobre ; les obligations réelles pour l'art, les lieux et la robotique ; les questions précises aux professionnels.
**Il ne refait pas** : la fuite de données et le RGPD (01-synthese-direction.md, 07-processus-ia-et-essais.md) ; les clauses du contrat-cadre, du mandat, de la réception et de la sortie (12-gouvernance-contrat-sortie.md) ; la trésorerie et les tests de résistance (09-modele-economique-tresorerie.md) ; la capacité et les rituels entre associés (06-fonctionnement-a-deux.md) ; les offres et les prix (04-catalogue-offres.md) ; le registre des risques (14-registre-risques-inconnues-decisions.md).

---

## En bref

1. **Forme : une SAS à l'IS, par défaut** [PR]. Aucune rémunération n'est financée par un contrat signé [FV]. Sans rémunération, une SAS ne coûte aucune cotisation ; une SARL à deux cogérants en coûte environ 3 500 € par gérant la première année [FV/ES]. Prix de ce choix la première année : environ 3 000 à 3 500 € de net en moins par associé dans le scénario central [ES]. À confirmer par une simulation officielle de l'expert-comptable (section 2).
2. **Seule Marwin Tech, immatriculée, facture.** Rien n'est encaissé avant l'immatriculation. Ni l'entreprise existante de Morgan, ni une micro-entreprise, ni un compte personnel (section 3).
3. **Le pacte entre Morgan et Mathys est signé avant tout contrat client.** Il règle la disponibilité, les apports, la propriété du CRM et des outils, les rémunérations inégales, le blocage à 50/50, le départ et l'incapacité (section 12).
4. **Rien n'est écrit sur la propriété.** Le CRM est co-écrit, sans licence, hébergé sous les comptes des associés [FV]. La réversibilité promise au client reste inexacte tant que ces comptes ne sont pas transférés (section 13).
5. **GianLuca : un rôle à la fois.** Client seul jusqu'au bilan du mois 6. Bureaux et emploi ensuite, par accords séparés. Capital pas avant 12 à 24 mois, minoritaire. Le cumul fait tout s'arrêter ensemble et expose surtout son entité à une requalification (sections 6 et 7).
6. **Le salariat chez GianLuca est le scénario le plus risqué**, et le plus tentant : un poste de cadre rapporterait environ 3 400 € nets par mois [MM], contre 1 100 à 1 500 € en central chez Marwin la première année [ES] (section 6.1).
7. **Medhi et BOJ.ART sont hors de l'offre.** Le lien de Morgan avec BOJ.ART est déclaré par écrit au client. Marwin ne promet ni œuvres, ni films, ni exclusivité, ni code de Jarvis (section 8).
8. **Aucune aide n'est acquise** : FRR, ACRE, ARE, ARCE, aides régionales, exonération de CFE. Le plan compte zéro (section 11).
9. **Galerie, ventes, événements, lieux** : les obligations pèsent sur l'entité de GianLuca qui vend, organise ou exploite. Marwin n'y est soumise que si elle encaisse, garde des œuvres, organise ou fabrique une machine (sections 14 et 16).
10. **Arguments fiscaux** : la déduction des œuvres d'artistes vivants vaut pour les achats faits avant le 31 déc. 2028 [FV]. Les pièces faites à la machine en sont très probablement exclues [HY]. « Mécénat » est faux pour un achat d'œuvre. Aucun avantage fiscal n'est validé pour l'achat d'impression 3D, de robotique ou d'IA (section 15).
11. **Aucun robot devant le public** sans intégrateur, analyse de risques et exploitant responsable. Aucun événement public en décembre 2026 dans un lieu non autorisé [ES] (section 16).
12. **Un écart avec la stratégie** : préférer une lettre d'intention de l'entité de GianLuca et signer le bon de commande après l'immatriculation, plutôt qu'au nom de la société en formation (section 10.1).

---

## 1. Point de départ au 4 novembre 2026

| Sujet | État | Code | Source |
| --- | --- | --- | --- |
| Marwin Tech | Non immatriculée. « ni forme juridique, ni répartition du capital, ni rémunération ne sont décidées » | [DR] | `interne/offre-marwin-tech-remuneration-et-collaboration.md:153` ; `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 17 |
| Contrat, facture, entité payeuse | Aucun | [FV négatif] | `travaux/strategie-retenue.md:33` |
| Associés | Morgan Olsen et Mathys Couet sont présentés comme associés. La note du 29 oct. écrit : « L'identité du futur second associé, les parts et les fonctions restent ouvertes » | [DR] ; [FV] pour la citation | `interne/contexte-projet-carlone.md:25-26` ; `interne/archives-marwin-tech/choix-structure-2026-10-29.pdf` p. 5 |
| Un troisième nom | Une page de pilotage présente Eaglemic (Michael Bach) comme « également un associé principal de Morgan ». Son rôle dans Marwin est inconnu | [DR] / [IN] | `sources/chatgpt-pages/2026-11-04-complement/pilotage-extraits-carlone.md:9` |
| Disponibilités | Morgan mène plusieurs autres projets (OLSEN, « Shelby », Côme Millot, ventes en ligne…). Aucune donnée sur Mathys | [FV] pour la liste ; [IN] | `travaux/note-point-4-novembre-et-activites.md:9-17` |
| Entreprise existante de Morgan | « Domiciliation de l'entreprise toujours résiliée » ; entreprise non nommée | [DR] / [IN] | `travaux/note-point-4-novembre-et-activites.md:6` |
| CRM | Hébergé « sous le compte des associés » ; « Propriété : le code, les données et le suivi restent chez les associés » ; aucun fichier de licence dans `crm/` | [FV] | `crm/docs/rapport/rapport-crm-hermes360.md:12, 19` |
| Rôles prêtés à GianLuca | « propose des bureaux, une bonne rémunération et envisage d'investir » ; « a racheté six bâtiments et l'ancienne affaire de Medhi » | [DR] | `interne/contexte-projet-carlone.md:24` |
| Medhi et BOJ.ART | Retirés de l'offre le 4 nov. sur une phrase de Morgan ; ni Mathys ni Medhi n'ont été consultés par écrit | [DR] / [IN] | `travaux/note-point-4-novembre-et-activites.md:25` |
| Forme visée dans les pièces récentes | « SARL à l'IS par défaut, SAS si Carlone entre au capital » | [FV] pour la citation | `interne/contexte-projet-carlone.md:12` |

---

## 2. SAS ou SARL, sur les mêmes hypothèses

### 2.1 Hypothèses identiques

- Deux associés à 50/50, tous deux dirigeants [HY]. En SARL : deux cogérants. En SAS : un président et un directeur général (`travaux/syn-droit.md:87-89`).
- Même chiffre d'affaires, mêmes frais, même démarrage, même réserve, même impôt sur les sociétés. Seul change le partage de l'enveloppe entre cotisations et net (`modele-financier/structures.md:22-26`).
- SAS : coût total d'un dirigeant rémunéré égal à 1,7 à 1,9 fois le net [HY]. Ce coefficient vient d'une seule source secondaire (`travaux/ver-R1-structures.md:40`).
- SARL : barème de la fiche F38152 (https://entreprendre.service-public.gouv.fr/vosdroits/F38152, vérifiée le 08/10/2026, consulté le 4 nov. 2026), abattement de 26 % (art. L136-3 III CSS) [FV] (`travaux/ver-R1-structures.md:20`).
- Pas d'ACRE, pas d'ARE, pas de prévoyance. Impôt sur le revenu non calculé : la situation des foyers est [IN].

### 2.2 Comparaison juridique et sociale

| Point | SARL, deux cogérants à 50/50 | SAS, président et directeur général | Code et source |
| --- | --- | --- | --- |
| Statut social | **Travailleurs non salariés tous les deux** : le collège de gérance détient plus de la moitié des parts | Assimilés salariés **s'ils sont rémunérés** | [FV] Cass. civ. 2, 31 mai 2018, n° 17-17.518 (https://www.legifrance.gouv.fr/juri/id/JURITEXT000037042970/, consulté le 4 nov. 2026) ; F37411 et F37366 (`travaux/ver-R1-structures.md:19`) |
| Cotisations sans rémunération | Forfaits de début d'activité d'environ 3 500 à 3 600 € par gérant la première année, régularisés ensuite ; puis un minimum d'environ 1 255 € par an | **0 €**, mais aucun droit social acquis | [FV] forfaits (`travaux/ver-R1-structures.md:20`) ; [ES] minimum, non vérifiable (`travaux/ver-R1-structures.md:39`) ; `interne/archives-marwin-tech/choix-structure-2026-10-29.pdf` p. 3 |
| Charges, en part du net | ≈ 40 à 46 % | ≈ 70 à 90 % | [ES] (`travaux/syn-droit.md:112`) |
| Indemnités journalières maladie | Plafond de 65,84 € par jour, 3 jours de carence | Plafond de 41,95 € par jour ; rien sans rémunération | [FV] F38152 (`travaux/ver-R1-structures.md:42`) |
| Retraite | Régimes des indépendants | Régime général et Agirc-Arrco | [FV] régimes ; [IN] écart chiffré |
| Chômage | Aucun | Aucun | [FV] F36065 (`travaux/ver-R1-structures.md:19`) |
| Associé qui vit d'un emploi extérieur | Le gérant reste redevable du minimum | Mandat non rémunéré, sans cotisation | [FV] (`travaux/syn-droit.md:159`) |
| Règles de fonctionnement | Largement fixées par la loi | Fixées par les statuts | [FV] F36022 ; [HY] étendue de la liberté |
| Blocage à 50/50 | Les décisions ordinaires n'ont pas de majorité sans accord. Chaque cogérant engage seul la société envers les tiers | Statuts et pacte peuvent prévoir médiation, tiers expert, offre alternative | [HY] (`travaux/syn-droit.md:155`) |
| Entrée d'un investisseur | Agrément de la majorité des associés représentant la moitié des parts ; droits de 3 % après abattement | Libre par défaut, encadrée par les statuts ; droits de 0,1 % (minimum 25 €) ; actions de préférence possibles | [FV] F36015 et F36022, vérifiées le 22/07/2026 (`travaux/ver-R1-structures.md:29`) ; [DR] actions de préférence |
| Impôt sur les sociétés | 15 % jusqu'à 42 500 € de bénéfice, 25 % au-delà, si le capital est entièrement libéré | Identique | [FV] art. 219 CGI (`travaux/ver-R1-structures.md:21`) |
| Dividendes | Cotisations sociales au-delà de 10 % du capital, des primes et des comptes courants : pas un levier avec un petit capital | Prélèvement forfaitaire de 31,4 % ; aucune cotisation ; aucun droit social | [FV] art. L136-3 II 2° CSS ; F2329 (`travaux/ver-R1-structures.md:22-23`) |
| Option pour l'impôt sur le revenu | Ouverte : 5 exercices au plus, option dans les 3 premiers mois | Ouverte ; traitement social de la quote-part non vérifié | [FV] art. 239 bis AB CGI (`travaux/ver-R1-structures.md:24`) ; [IN] |
| Libération du capital | 20 % au moins à la création ; **100 % pour le taux d'IS de 15 %** | 50 % au moins ; **100 % pour le taux d'IS de 15 %** | [FV] F37411, F37366 (`travaux/ver-R1-structures.md:27`) |
| Statuts et pacte par un avocat | ≈ 1 500 à 4 000 € HT | ≈ 2 000 à 5 000 € HT | [ES] fondée sur [HY] (`travaux/syn-droit.md:180`) |
| Trésorerie sociale | Forfaits en année 1, régularisation en année 2 : à provisionner | Cotisations payées chaque mois avec le salaire | [ES] (`travaux/syn-droit.md:187-195`) |

**Piège déjà signalé dans les pièces.** 50/50 ne veut pas dire « gérance égalitaire ». Deux cogérants qui détiennent ensemble toutes les parts sont tous deux gérants majoritaires, donc TNS (`interne/archives-marwin-tech/choix-structure-2026-10-29.pdf` p. 2) [FV].

### 2.3 Les chiffres, sur les scénarios de l'audit

Nets par associé, avant impôt sur le revenu, rémunération versée des mois 4 à 12 [ES] (`modele-financier/structures.md:31-35`) :

| Scénario | Enveloppe mensuelle pour les deux | SAS : net par mois | SARL : net par mois | Écart SARL − SAS sur 9 mois (coefficient 1,8) | SARL : régularisation à provisionner en année 2 |
| --- | --- | --- | --- | --- | --- |
| Prudent | 2 100 à 2 700 € | 600 à 800 € | 800 à 1 000 € | 1 500 à 1 900 € | −800 à 0 € |
| Central | 4 300 à 5 100 € | 1 100 à 1 500 € | 1 500 à 1 800 € | 3 000 à 3 500 € | 1 900 à 3 000 € |
| Ambitieux | 6 200 à 7 300 € | 1 600 à 2 200 € | 2 200 à 2 600 € | 4 200 à 4 900 € | 4 600 à 6 200 € |

À plus haut niveau d'activité, l'écart grandit [ES] (`travaux/syn-droit.md:123-128`) :

| CA HT annuel (frais = 1/6) | SARL, tout en rémunération | SAS, tout en salaire | Écart par personne et par an |
| --- | --- | --- | --- |
| 120 000 € | ≈ 34 500 € | ≈ 26 300 à 29 400 € | ≈ 5 000 à 8 000 € |
| 180 000 € | ≈ 51 400 € | ≈ 39 500 à 44 100 € | ≈ 7 000 à 12 000 € |

**Lecture.**
- À enveloppe égale, la SARL laisse environ 15 à 30 % de net en plus. L'écart dépend surtout du coefficient SAS, non vérifié [ES].
- Les dividendes ne financent pas la vie de la première année. Ils sont versés après l'approbation des comptes, au plus tôt au printemps 2028 pour l'exercice 2027 [HY]. Ils n'ouvrent aucun droit social (`modele-financier/structures.md:60`).
- La SAS coûte zéro les mois sans rémunération. Or le scénario central ne rémunère personne avant le mois 4 (`travaux/strategie-retenue.md:511`).

> **Précision sur la stratégie retenue.** Elle chiffre le prix de la SAS à « environ 5 000 à 12 000 € de net par personne et par an de moins qu'une SARL à 120 000-180 000 € de CA » (`travaux/strategie-retenue.md:543`). C'est exact à ce niveau d'activité, que le scénario central n'atteint pas la première année. Pour la première année, l'écart pertinent est celui du modèle : 1 500 à 4 900 € par associé selon le scénario. La recommandation ne change pas.

### 2.4 Recommandation

| Élément | Contenu |
| --- | --- |
| **Recommandation** [PR] | SAS à l'IS ; un président et un directeur général, chacun avec au moins un tiers du capital ; capital modeste, **entièrement libéré** ; statuts qui organisent le blocage ; pacte signé avant le contrat client ; rémunération nulle jusqu'au premier socle récurrent (`travaux/strategie-retenue.md:543-550`) |
| **Preuve** | Aucun contrat ne finance une rémunération [FV] ; 0 € de cotisation sans rémunération en SAS [FV] ; entrée d'un investisseur et emploi extérieur évoqués [DR] (`interne/contexte-projet-carlone.md:24` ; `interne/recueil-sessions-chatgpt-2026-11-04.txt:248`) |
| **Hypothèse** | Coefficient de 1,7 à 1,9 ; les associés acceptent un revenu modeste la première année |
| **Limite** | Aucune simulation officielle ; règles de 2027 inconnues ; forfaits TNS d'une société créée fin 2026 [IN] |
| **Décision** | Décision prioritaire n° 4 (`travaux/strategie-retenue.md:718`) : statuts et pacte préparés en novembre ; immatriculation sur engagement écrit d'une entité identifiée |
| **Quand revenir à la SARL** | Seulement si les trois conditions sont réunies : aucun investisseur avant 24 mois ; un contrat signé d'au moins 120 000 € par an qui finance une rémunération régulière ; aucun associé salarié ailleurs. Il faut alors provisionner la régularisation de l'année 2 (`travaux/strategie-retenue.md:562`). Le passage ultérieur d'une forme à l'autre a un coût non chiffré [IN] |

### 2.5 Formes écartées

| Forme | Pourquoi l'écarter | Source |
| --- | --- | --- |
| Micro-entreprise | Structure individuelle pour un travail à deux (risque de société créée de fait) ; franchise de TVA perdue dès 41 250 € de CA ; frais réels non déductibles. Correction : le régime fiscal reste applicable deux ans après un dépassement, mais la franchise de TVA tombe tout de suite | [FV] (`travaux/ver-R1-structures.md:30`) ; [HY] société créée de fait |
| SARL à l'IR avec FRR | Plus avantageuse seulement si l'exonération FRR est acquise ; cotisations sur le bénéfice attribué, **même non retiré** | `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 18, 20 [FV] |
| SCOP | Étudiée le 30 oct. ; gouvernance coopérative et réserves imposées ; « elle n'est pas retenue par défaut » | `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 24 [FV] |
| Entreprise existante de Morgan | Voir section 3 | `travaux/strategie-retenue.md:564` |

---

## 3. La structure qui facture

| Option | Verdict [PR] | Pourquoi | Source |
| --- | --- | --- | --- |
| Marwin Tech SAS, immatriculée | **Oui, seule** | Elle a un SIREN, un numéro de TVA, un compte et une assurance à son nom | `travaux/strategie-retenue.md:458` |
| Marwin « en formation » | Signature possible, **aucun encaissement** | Pas de SIREN ni de compte à son nom ; les signataires répondent personnellement (section 10.1) | [FV] art. L210-6 C. com. ; [HY] encaissement (`travaux/rj-R2-fiscal.md:408-411`) |
| Entreprise existante de Morgan | **Non** | Domiciliation résiliée [DR] ; propriété des livrables brouillée ; mélange avec la prospection d'OLSEN ; Marwin pourrait paraître le prolongement d'une activité préexistante [HY] | `travaux/note-point-4-novembre-et-activites.md:6` ; `travaux/syn-droit.md:283` |
| Micro-entreprise d'un associé | **Non** | Section 2.5 | — |
| Compte personnel d'un associé | **Non** | Aucune trace propre ; aucune TVA collectée correctement | `travaux/syn-droit.md:313` |

**Côté client** [PR] :
- **Un bon de commande par prestation et par entité.** Chaque document nomme l'entité, son SIREN, le signataire habilité, le payeur, le valideur et l'effectif (`travaux/strategie-retenue.md:185, 223`). L'effectif compte pour la règle de rétractation (section 10.2).
- **Solvabilité** : consulter sans contact les registres publics une fois l'entité nommée (`travaux/strategie-retenue.md:566`). Un patrimoine déclaré n'est pas une trésorerie.
- **Achats et tiers** : commandés et payés par l'entité de GianLuca, à son nom. Quali Contact, l'expert-comptable, l'avocat, le photographe et les artistes la facturent directement (`travaux/strategie-retenue.md:387-388`).
- **Réception des factures électroniques** : l'entité de GianLuca doit pouvoir les recevoir depuis le 1er sept. 2026 [FV]. Son état est [IN] (`travaux/rj-R2-fiscal.md:322`).

**Siège de Marwin** [IN]. Le lieu de résidence des associés est inconnu. Trois options : domicile d'un dirigeant, domiciliataire, bureaux d'un tiers. Les bureaux de GianLuca sont exclus avant le bilan du mois 6 (section 6.2). Le choix fixe la commune de la CFE. Il garde ou ferme la voie du FRR : une domiciliation chez un domiciliataire ne suffit pas, le domicile du dirigeant **situé en zone** est admis [FV] (BOI-BIC-CHAMP-80-10-75-20, § 260, https://bofip.impots.gouv.fr/doctrine/pgp/14772-PGP, publié le 29/07/2026, consulté le 4 nov. 2026 ; `travaux/ver-R2-fiscal.md:33, 48`). Question à l'expert-comptable (section 19.1).

---

## 4. Associés et pouvoirs

| Sujet | Règle proposée | Code | Source |
| --- | --- | --- | --- |
| Qui est associé | Morgan et Mathys, 50/50, par écrit. Le pacte dit si Eaglemic (Michael Bach) ou un autre tiers a un rôle, et lequel. Sans écrit, personne d'autre n'a de droit sur Marwin | [PR, ce livrable] | `sources/chatgpt-pages/2026-11-04-complement/pilotage-extraits-carlone.md:9` [DR] |
| Mandats | Un président et un directeur général. Peu importe qui préside si le DG reçoit les mêmes pouvoirs de représentation ; ce qui compte, c'est la délégation croisée de signature et le double accord interne | [PR] ; [HY] sur la mécanique des pouvoirs | `travaux/strategie-retenue.md:546` |
| Pouvoirs envers les tiers | En SAS, le président représente la société ; les statuts peuvent donner les mêmes pouvoirs au DG. Les limites internes ne sont en principe **pas opposables aux tiers** : une seule signature engage Marwin envers GianLuca | [HY] art. L227-6 C. com., non rouvert dans l'audit | À confirmer par l'avocat (section 19.2) |
| Décisions à l'unanimité | Contrat avec GianLuca ; prix et remises ; engagement de plus de 1 000 € HT ; entrée d'un associé ; recrutement ; sous-traitance. Toute dépense de plus de 300 € HT ou tout abonnement : accord des deux | [PR] | `travaux/strategie-retenue.md:592, 614` |
| Rendre la règle visible | Faire signer chaque bon de commande et chaque avenant par les deux dirigeants. Le client sait ainsi qu'un engagement suppose l'accord des deux | [PR, ce livrable] | Conséquence de la ligne « Pouvoirs envers les tiers » |
| Répartition des rôles | Morgan : relation client et prix. Mathys : technique et données, avec **délégation écrite de la validation technique** | [PR] | `travaux/strategie-retenue.md:619` ; `interne/offre-marwin-tech-remuneration-et-collaboration.md:223` [FV] |
| Conventions avec un associé | Licence du CRM d'un associé à Marwin, compte courant, bail : à traiter comme conventions entre la société et un dirigeant ou un associé | [HY] art. L227-10 C. com., non rouvert | `travaux/syn-droit.md:169` |
| Cessions | Agrément, préemption, inaliénabilité (10 ans au plus, adoptée à l'unanimité) | [FV] F36022 | `travaux/ver-R1-structures.md:29` |
| Quand rien n'est proposé au client | Tant qu'un désaccord entre associés dure | [PR] | `travaux/strategie-retenue.md:614` |

---

## 5. Rémunérations

| Règle [PR] | Contenu | Source |
| --- | --- | --- |
| Aucune rémunération avant le premier socle récurrent | En central, rien avant le mois 4 ; puis ≈ 1 100 à 1 500 € nets par associé et par mois en SAS [ES] | `travaux/strategie-retenue.md:550` ; `modele-financier/structures.md:34` |
| Plancher non atteint | Le plancher de 2 500 € nets par équivalent temps plein n'est pas atteint la première année [ES] | `travaux/strategie-retenue.md:112, 511` |
| Grille liée au temps | Rémunération fixée par l'organe désigné aux statuts, selon une grille écrite au pacte : temps engagé et fonction ; plafond inscrit au pacte | `travaux/syn-droit.md:474` |
| Rémunérations différentes | Un temps inégal se compense par le salaire du mandat, pas par les dividendes, qui suivent le capital sauf actions de préférence [HY]. Un apport en industrie est possible (actions inaliénables) mais ne transfère aucune propriété intellectuelle [FV] | `travaux/ver-R1-structures.md:27` |
| Ordre des sorties d'argent | Frais justifiés ; rémunération avec provisions (cotisations, TVA, impôts) ; fonds de roulement ; distribution éventuelle après clôture | `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 20 [FV] |
| Protection | Un dirigeant de SAS non rémunéré n'acquiert aucun droit social : prévoyance et mutuelle à étudier avant la première prestation | `interne/archives-marwin-tech/choix-structure-2026-10-29.pdf` p. 3 [FV] |
| Allocation chômage | Le maintien de l'ARE pour un président de SAS non rémunéré est une hypothèse ; le cumul est plafonné à 60 % des droits restants depuis le 1er avril 2025 | [HY] ; [FV] F36613, vérifiée le 29/09/2026 (`travaux/ver-R1-structures.md:26`) |
| Cibles personnelles | Les pièces citent 2 500 €, 3 660 € et 7 500 € nets par mois. Le 7 500 € suppose environ 30 000 € HT par mois pendant douze mois. Aucune de ces cibles n'est tenable la première année [ES] | `interne/contexte-projet-carlone.md:119` ; `interne/offre-marwin-tech-remuneration-et-collaboration.md:118` [DR] |

Le détail des scénarios et de la trésorerie est dans 09-modele-economique-tresorerie.md.

---

## 6. Ce que GianLuca propose : emploi, bureaux, matériel, financement, capital

### 6.0 Ce que disent les pièces

| Rôle prêté à GianLuca | État | Code | Source |
| --- | --- | --- | --- |
| Client | Aucune entité, aucun signataire, aucun payeur identifié | [FV négatif] | `travaux/strategie-retenue.md:33` |
| Bailleur | « propose des bureaux » ; lieu inconnu, en zone FRR ou non | [DR] / [IN] | `interne/contexte-projet-carlone.md:24, 108` |
| Employeur | « Carlone veut vous salarier et acheter des prestations » (30 oct.). Rien ne vient du client : c'est Morgan qui répond « Je préfère être prestataire ou salarié » | [DR] ; intention du client [IN] | `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 20 ; `interne/recueil-sessions-chatgpt-2026-11-04.txt:248` |
| Investisseur | « envisage d'investir » ; aucune forme, aucun montant | [DR] / [IN] | `interne/contexte-projet-carlone.md:24` |
| Financeur de création et de R&D | Options laboratoire (30 000 € HT) et création (≈ 10 000 € HT) proposées le 2 nov., retirées depuis | [PR] retirée | `interne/offre-marwin-tech-remuneration-et-collaboration.md:21-22` ; `travaux/strategie-retenue.md:411-412` |
| Acquéreur de l'ancienne affaire de Medhi | Lien direct entre GianLuca et Medhi, hors de Marwin | [DR] | `interne/contexte-projet-carlone.md:24` |

### 6.1 Salariat éventuel chez GianLuca

**Règles** [FV] :
- Un salarié doit la loyauté à son employeur. Créer une activité **concurrente**, même sans clause de non-concurrence, peut être une faute grave (Cass. soc., 14 janv. 2026, n° 24-20.799, arrêt inédit ; actualité A18850, https://entreprendre.service-public.gouv.fr/actualites/A18850, consulté le 4 nov. 2026) (`travaux/ver-R3-travail-contrats.md:38`). L'appliquer à un associé de Marwin salarié chez le client reste [HY].
- Les logiciels créés par un salarié dans ses fonctions appartiennent à l'employeur (art. L113-9 CPI, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039279818, consulté le 4 nov. 2026).
- Le second versement de l'ARCE peut être incompatible avec un CDI à temps plein (`travaux/ver-R1-structures.md:26`).
- Les durées maximales (10 h par jour, 48 h par semaine) ne comptent que les activités salariées (F1945).

**Risques** [HY] : mêmes lieux, mêmes interlocuteurs, mêmes sujets. Un contrôleur peut juger que les factures de Marwin paient du travail subordonné. Le salarié peut se retrouver à préparer ou valider les livrables de sa propre société. Le code écrit pendant le temps salarié peut appartenir au client. Tout s'arrête ensemble (`travaux/rj-R3-travail-contrats.md:199-207`).

**La tentation est réelle.** Un poste de cadre chez GianLuca (≈ 3 400 € nets pour 6 149 € de coût employeur [MM]) rapporterait plus que Marwin en central la première année [ES] (`travaux/strategie-retenue.md:707`).

**Règle** [PR] (`travaux/strategie-retenue.md:631`) : refusé avant le bilan du mois 6 ; jamais les deux associés ; ensuite, une seule personne, des fonctions non couvertes par Marwin, des temps séparés, une validation des livrables de Marwin par une autre personne du client ; jamais un argument de prix.

**À ajouter si le cas se présente** [PR, ce livrable] :
- l'associé salarié déclare le conflit par écrit à l'autre associé et s'abstient dans les décisions de Marwin qui concernent GianLuca ;
- le contrat de travail limite la clause de propriété intellectuelle aux fonctions salariées et liste les composants de Marwin qui restent à Marwin ;
- son mandat dans Marwin devient non rémunéré si nécessaire (`interne/offre-marwin-tech-remuneration-et-collaboration.md:166`) ;
- France Travail et l'expert-comptable sont consultés avant la signature (ARE, ARCE, ACRE).

### 6.2 Bureaux

- **Refusés pendant le cadrage et le pilote** [PR]. Des bureaux fournis « dès le départ par convention » sont un indice de requalification (`travaux/strategie-retenue.md:132, 630`).
- **Après le bilan du mois 6, par convention séparée** [PR] : accès sans horaires imposés ; usage partagé ; assurance ; entretien ; restitution ; gratuit ou avec loyer. Aucun lien avec les honoraires, sauf un délai de restitution aligné sur le préavis (`travaux/syn-droit.md:438-439`).
- **Assurance** : si Marwin est locataire, elle doit assurer le local [FV] (F37365, https://entreprendre.service-public.gouv.fr/vosdroits/F37365, vérifiée le 07/07/2026, consulté le 4 nov. 2026 ; `travaux/ver-R3-travail-contrats.md:40`). Une convention de mise à disposition n'est pas forcément un bail [IN] : question à l'avocat.
- **CFE** : la base serait la valeur locative du local utilisé [HY] (`travaux/rj-R2-fiscal.md:275`).
- **Signaux d'alerte** : horaires fixés par le client, badge ou adresse e-mail du client, place dans un organigramme, compte rendu à un cadre comme un salarié (`travaux/syn-droit.md:444`).

### 6.3 Matériel

- **L'entité de GianLuca achète et possède le matériel destiné à ses projets** ; Marwin facture seulement les travaux convenus [PR] (`interne/offre-marwin-tech-remuneration-et-collaboration.md:138` ; `travaux/strategie-retenue.md:188`).
- Si Marwin achetait pour refacturer, l'achat entrerait dans son chiffre d'affaires et elle en porterait le risque. Les débours ne se refacturent hors TVA qu'aux quatre conditions du BOFiP [FV] (BOI-TVA-BASE-10-10-30, § 200 ; `travaux/ver-R3-travail-contrats.md:56`).
- Si Marwin assemblait une machine (bras, outil, commande), elle en deviendrait **fabricant** (section 16).
- Les imprimantes et machines de BOJ.ART restent à leurs propriétaires. « L'accès annoncé à environ dix imprimantes n'est pas un transfert de propriété » (`interne/archives-marwin-tech/choix-structure-2026-10-29.pdf` p. 4) [FV].
- Le poste de travail, les logiciels et les comptes de Marwin sont à Marwin et payés par elle.
- La station DGX Spark et l'IA locale sont retirées (`travaux/strategie-retenue.md:645`).

### 6.4 Financement des projets

- **Marwin n'avance jamais d'argent pour le client** [PR] (`travaux/strategie-retenue.md:188`).
- **L'acompte n'est ni du capital ni un prêt** [FV pour la règle des pièces] (`interne/offre-marwin-tech-remuneration-et-collaboration.md:142` ; `interne/archives-marwin-tech/choix-structure-2026-10-29.pdf` p. 3).
- **La « ligne création » comme forme d'investissement est caduque.** Le 2 nov., l'offre proposait à GianLuca de financer STRATES « phase par phase » plutôt que d'entrer au capital (`interne/offre-marwin-tech-remuneration-et-collaboration.md:144`). STRATES est gelé et Medhi retiré (`travaux/strategie-retenue.md:644`).
- **Projets du client** : financés par son entité, avec un financeur écrit, un budget plafonné et un critère d'arrêt (section 17).
- **Financement de Marwin** : apport des associés de 8 000 à 14 000 € (capital libéré et comptes courants) [PR] (`travaux/strategie-retenue.md:510`). Aucun prêt bancaire ni aide n'est supposé. Les aides régionales à la création sont des avances remboursables (section 11).

### 6.5 Entrée de GianLuca au capital

**Règle** [PR] (`travaux/strategie-retenue.md:632`) : pas de discussion avant 12 à 24 mois ; après au moins deux renouvellements du socle ; minoritaire ; sans veto opérationnel ; contrat client résiliable indépendamment ; jamais contre une baisse d'honoraires.

| Effet d'une entrée au capital | Règle | Code et source |
| --- | --- | --- |
| Forme | La SAS est plus adaptée : cession libre selon les statuts, droits de 0,1 % | [FV] F36022 (`travaux/ver-R1-structures.md:29`) |
| Taux d'IS de 15 % | Capital détenu à 75 % au moins par des personnes physiques **ou par des sociétés qui remplissent ce critère**. Une entrée par une société de GianLuca ne fait pas forcément perdre le taux réduit | [FV] (`travaux/syn-droit.md:142` ; `travaux/ver-C3-structure.md:26`) |
| Option pour l'IR | Perdue si une société dépasse 50 % des droits de vote ou si les dirigeants passent sous 34 % | [FV] (`travaux/syn-droit.md:146`) |
| ACRE | Contrôle effectif de la société par les bénéficiaires pendant 2 ans | [FV] F11677 (`travaux/ver-R1-structures.md:25`) |
| Plafond de minimis (FRR) | Apprécié par « entreprise unique » si GianLuca contrôlait Marwin | [HY] (`travaux/syn-droit.md:168`) |
| Conventions entre Marwin et un associé important | Le contrat client lui-même pourrait devenir une convention à soumettre aux associés | [HY] art. L227-10 C. com., non rouvert (`travaux/syn-droit.md:169`) |
| Majorité | Les fondateurs gardent la majorité, et au moins 34 % chacun si l'option IR est retenue | [PR] (`interne/offre-marwin-tech-remuneration-et-collaboration.md:146` ; `travaux/syn-droit.md:441`) |
| Prix d'entrée | Aucune base de valorisation tant que Marwin n'a pas d'historique | [IN] |

---

## 7. Risque cumulé : GianLuca client, bailleur, employeur et investisseur

### 7.1 Ce que chaque rôle fait courir

| Rôle | Ce que Marwin risque | Qui porte le risque juridique principal | Effet sur la décision | Effet sur la sortie |
| --- | --- | --- | --- | --- |
| Client | Dépendance à 100 % du chiffre d'affaires la première année [ES] | Marwin | Le client peut peser sur le prix et le périmètre | Préavis ; rupture brutale (art. L442-1 II C. com.) dans les deux sens |
| Bailleur | Indice de subordination ; locaux perdus avec le contrat | L'entité de GianLuca en cas de requalification | Présence quotidienne, ordres directs | Restitution des locaux en même temps que la fin du contrat |
| Employeur | Requalification des factures ; conflit d'intérêts ; code qui revient au client | L'entité de GianLuca (travail dissimulé) ; l'associé salarié (loyauté) | L'associé salarié décide pour Marwin et obéit au client | Démission ou licenciement liés à la fin du contrat |
| Investisseur | Blocage croisé : un désaccord commercial devient un conflit d'associés | Marwin et ses fondateurs | Pression sur les honoraires ; conventions à faire approuver | Le client ne peut plus partir sans toucher au capital, et l'inverse |
| **Les quatre ensemble** | « si la relation s'arrête, honoraires, bureaux et capital s'arrêtent ensemble » | Les deux côtés | Plus aucune décision n'est prise sur pièces | Aucune sortie propre |

Sources : `interne/offre-marwin-tech-remuneration-et-collaboration.md:148` [FV pour la citation] ; `travaux/syn-droit.md:332-348, 364-380` ; `travaux/rj-R1-structures.md:325`.

**Requalification : ce qu'il en coûterait** [FV] (`travaux/syn-droit.md:332-348` ; `travaux/ver-R3-travail-contrats.md:32-33`) :
- les dirigeants d'une société immatriculée sont présumés non salariés, sauf subordination juridique permanente, « directement ou par une personne interposée » (art. L8221-6 C. trav., https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044056617, consulté le 4 nov. 2026). Marwin ne fait donc pas écran ;
- pour l'entité de GianLuca, si l'intention est établie : travail dissimulé, jusqu'à 3 ans et 45 000 €, 225 000 € pour une société (art. L8224-1 ; F31490) ;
- **nouveau en 2026** : la condamnation pourra être publiée en ligne par le ministère pendant deux ans, une fois le décret pris (loi n° 2026-534, art. 98) ;
- pour Morgan et Mathys : la relation passe sous le droit du travail et les factures perdent leur objet [HY].

**Rupture brutale** [FV] : depuis le 20 août 2026, une réduction substantielle des volumes commandés pendant une négociation, même temporaire, peut aussi engager la responsabilité de son auteur (art. L442-1 II C. com., modifié par la loi n° 2026-796, art. 54 ; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047381704, consulté le 4 nov. 2026 ; `travaux/ver-R3-travail-contrats.md:39, 74`). Un contrat de quelques mois est rarement une relation « établie » [HY]. La vraie protection reste contractuelle.

### 7.2 Quatre situations concrètes

| Situation | Sans précaution | Avec les règles ci-dessous |
| --- | --- | --- |
| Désaccord sur un livrable alors que GianLuca est associé | Il bloque une décision de Marwin pour obtenir gain de cause sur le livrable | Pas de capital avant 12-24 mois ; associé minoritaire sans veto ; réserves traitées au contrat (12-gouvernance-contrat-sortie.md) |
| GianLuca propose d'investir contre une baisse d'honoraires | Marwin perd sa marge et sa liberté | Refus : « N'échangez jamais une baisse d'honoraires contre une promesse d'investissement » (`interne/offre-marwin-tech-remuneration-et-collaboration.md:149`) [PR] |
| L'associé salarié chez GianLuca valide les livrables de Marwin | Conflit d'intérêts ; preuve de subordination | Valideur distinct nommé au bon de commande (`travaux/strategie-retenue.md:629`) |
| Contrôle de l'Urssaf ou de l'inspection du travail | Bureaux, présence quotidienne, prix au temps, client unique : faisceau d'indices | Prix au livrable ; liste des livrables avant la liste des heures ; pas de bureaux avant le mois 6 ; autres clients réels (`travaux/strategie-retenue.md:777`) |

### 7.3 Moyens de préserver la décision et la sortie

| Moyen | Contenu [PR] | Source |
| --- | --- | --- |
| Un rôle à la fois | Client seul jusqu'au bilan du mois 6 ; chaque autre rôle ensuite, par accord séparé | `travaux/strategie-retenue.md:625-633` |
| Un accord par sujet | Contrat de prestation, convention de bureaux, contrat de travail, pacte d'investissement : chacun avec sa durée, son prix et sa sortie | `interne/offre-marwin-tech-remuneration-et-collaboration.md:132` ; diaporama client, `slides/cadre.html:4` [FV] |
| Aucun lien entre les accords | Aucune clause qui fait tomber les honoraires si les bureaux s'arrêtent, ni l'inverse | `travaux/syn-droit.md:438` |
| Décisions de Marwin gardées par Marwin | Contrat avec GianLuca, prix, remises : unanimité des deux associés ; aucun droit de veto donné au client | `travaux/strategie-retenue.md:614` |
| Valideur distinct | Une personne du client valide les livrables, distincte d'un éventuel associé salarié | `travaux/syn-droit.md:442` |
| Investisseur encadré | Minoritaire ; droit d'information ; pas de veto opérationnel ; contrat client résiliable indépendamment | `travaux/strategie-retenue.md:632` |
| Sortie préparée | Préavis gradué et réciproque ; réversibilité chiffrée ; comptes au nom du client dès le premier jour ; licences sur les composants génériques qui survivent au contrat | `travaux/syn-droit.md:443` ; 12-gouvernance-contrat-sortie.md |
| Dépendance suivie | Part de GianLuca dans le chiffre d'affaires mesurée chaque mois ; second client recherché ; dépendance à 100 % assumée par écrit à défaut | `travaux/strategie-retenue.md:116, 522` |
| Signaux d'alerte | Horaires imposés ; organigramme ; exclusivité de fait ; baisse brutale des volumes ; proposition d'échanger honoraires contre bureaux, emploi ou capital | `travaux/strategie-retenue.md:683-684` |

---

## 8. Relations avec Medhi et BOJ.ART

**Faits.**

| Fait | Code | Source |
| --- | --- | --- |
| Décision orale du 4 nov. : « Va juste falloir enlever Medhi/boj art de l'offre » | [DR] | `travaux/note-point-4-novembre-et-activites.md:25` |
| Seul le diaporama client a été corrigé (11 vues) | [FV] | diaporama client, `deck.json:7` |
| L'offre écrite garde l'« Option création » et le tableau « Qui apporte quoi » ; elle promet à la galerie « une exclusivité de vente sur la série » et « l'usage des films de fabrication » | [FV] | `interne/offre-marwin-tech-remuneration-et-collaboration.md:22, 88-94` |
| STRATES v1.1 porte l'en-tête « BOJ.ART / MARWIN TECH » | [FV] | `pour-carlone/strates-proposition-artistique-v1.1.pdf` p. 1 |
| Le vernissage repose sur le parc et la main de Medhi | [FV] | `pour-carlone/vernissage-strates-idees.md:20-22` |
| Morgan « orchestre BOJ.ART » et a construit Jarvis ; le catalogue de vente qu'il a rédigé pour GianLuca proposait des pièces de Medhi | [DR] | `interne/contexte-projet-carlone.md:25` ; `travaux/syn-droit.md:461` |
| Le dépôt public BOJART ne contient aucune mention de « Carlone » | [FV] | `travaux/note-point-4-novembre-et-activites.md:21` |
| Ce qui a été promis à Medhi | [IN] | `travaux/strategie-retenue.md:754` |
| La tâche « Écrire l'accord à trois avec Medhi » figure encore dans le contexte du 4 nov. | [FV] | `interne/contexte-projet-carlone.md:14` |

**Règles** [PR] (`travaux/strategie-retenue.md:615, 635, 643`) :
1. Medhi et BOJ.ART sont hors de l'offre de Marwin. La tâche « accord à trois » est caduque.
2. Décision écrite des deux associés sur la portée du retrait, puis message écrit à Medhi (calendrier : 08-feuille-de-route.md).
3. **Déclaration écrite et proactive** du lien de Morgan avec BOJ.ART dans le premier document remis à GianLuca. Morgan s'abstient de toute recommandation d'achat ou de vente qui concerne Medhi.
4. Si la galerie veut vendre ses pièces : **contrat de dépôt-vente direct** entre Medhi et l'entité de GianLuca, sans Marwin ni commission.
5. Marwin ne promet jamais ce qu'elle ne détient pas : œuvres, motifs, films, exclusivité, parc d'impression, code de Jarvis (`travaux/syn-droit.md:500`).
6. Un retour de Medhi suppose une décision écrite des deux associés, un contrat séparé (prix, propriété intellectuelle, attestation de vigilance dès 5 000 € HT cumulés) et un conflit déclaré au client.
7. Les documents encore en circulation sous le nom de Marwin sont marqués « historique, retiré le [date] ». Sinon, Marwin paraît organisatrice ou coproductrice (`travaux/syn-droit.md:543`).

---

## 9. Réexamen des recommandations des 29 et 30 octobre

Pièces : note « Quelle structure pour Marwin Tech ? » du 29 oct. (`interne/archives-marwin-tech/choix-structure-2026-10-29.pdf`) et dossier du 30 oct. avec annexe interne (`interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf`). Verdicts tirés des contrôles (`travaux/syn-droit.md:237-266` ; `travaux/ver-C3-structure.md:21-35`), citations revérifiées dans les PDF.

| N° | Ce que disait la pièce | Source | Verdict au 4 nov. 2026 | Ce qu'il faut retenir |
| --- | --- | --- | --- | --- |
| 1 | SAS à l'IS « piste prioritaire », « si vous confirmez une association à deux et la volonté de développer une entreprise évolutive » | 29 oct., p. 1 et 7 | **Tient**, comme recommandation conditionnelle [PR] | La question posée n'a jamais reçu de réponse [IN] |
| 2 | SARL à gérance majoritaire à l'IS : « C'est la référence tant que le FRR et les situations personnelles ne sont pas établis » | 30 oct., p. 17, 20 | **Provisoire**, et dépassée par les faits : aucune rémunération n'est financée | Les pièces suivantes l'ont traitée à tort comme une décision (`interne/offre-marwin-tech-remuneration-et-collaboration.md:155` ; `interne/contexte-projet-carlone.md:12`) |
| 3 | Le régime social de la SAS est « généralement plus coûteux pour une rémunération régulière » | 30 oct., p. 17 | **Exact** en ordre de grandeur (+15 à +30 % de net en SARL) [ES] | Sans objet tant qu'il n'y a pas de rémunération régulière |
| 4 | Nets annuels de 43 875 €, 42 272 €, 51 408 €, 41 080 € | 30 oct., p. 18 | **Calculs cohérents, précision artificielle** ; base de 12 mois pour un contrat de 6 | Raisonner en fourchettes (section 2.3) |
| 5 | Écart SAS / SARL de 2 795 € par an | 30 oct., p. 18 | **Non probant** : il compare deux stratégies (rémunération pure contre salaire et dividendes) | Ne pas s'en servir |
| 6 | Deux cogérants à 50/50 relèvent de la gérance majoritaire | 29 oct., p. 2 ; 30 oct., p. 20 | **Confirmé** [FV] (Cass. civ. 2, 31 mai 2018) | Les deux sont TNS |
| 7 | IS à 15 % jusqu'à 42 500 € ; capital entièrement libéré, 75 % de personnes physiques « ou sociétés répondant au critère » | 29 oct., p. 3 | **Confirmé** [FV] ; inchangé par la loi de finances pour 2026 | Libérer tout le capital à la constitution |
| 8 | Cotisations sur les dividendes du gérant de SARL au-delà de 10 % | 29 oct., p. 3 ; 30 oct., p. 20 | **Confirmé** [FV] ; base légale : art. L136-3 II 2° CSS | Pas un levier avec un petit capital |
| 9 | Conditions de l'option pour l'IR | 30 oct., p. 21 | **Confirmé** [FV] | « Une majorité extérieure ferait perdre l'option IR » (`interne/offre-marwin-tech-remuneration-et-collaboration.md:146`) est trop large |
| 10 | Une majorité extérieure peut fermer le FRR « selon les conditions de détention » | `interne/offre-marwin-tech-remuneration-et-collaboration.md:146` | **Faux en l'état** : pas de condition générale de détention en FRR de base [FV] | Vrais risques : plafond de minimis par entreprise unique [HY] ; activité transférée ou préexistante [FV] |
| 11 | Cosne-Cours-sur-Loire (58086) classée en FRR | 30 oct., p. 21 | **Confirmé** : FRR de base, pas FRR+ [FV] | Le classement de la commune ne vaut pas exonération pour Marwin |
| 12 | Effet du seuil de 25 % hors zone présenté différemment selon les sources | 30 oct., p. 24 | **Tranché** : pour une activité sédentaire, au-delà de 25 %, **perte totale** [FV] (BOFiP du 29/07/2026, § 160) | Un pilotage exécuté hors zone peut tout faire perdre |
| 13 | Exonération de CFE votée par Cœur de Loire | 30 oct., p. 21, 25 | **Source secondaire** [DR] ; liée au bénéfice du FRR | Barème de 250 € à 7 769 € = **base** minimum, à multiplier par le taux local [FV] |
| 14 | Aides régionales : avance remboursable à la création ; investissement matériel ; conseil stratégique | 30 oct., p. 23 | **[DR] non revérifié** ; création **et** investissement sont des avances remboursables ; seul le conseil est une subvention, pour un client éligible | Ne rien budgéter |
| 15 | ACRE à 25 %, plafonds de 36 045 € et 48 060 €, demande sous 60 jours, contrôle pendant 2 ans | 30 oct., p. 25 | **Confirmé** [FV] (F11677 ; décret n° 2026-69) | Réservée à des publics listés ; le silence vaut accord pour une société : [IN] |
| 16 | ARCE : 60 % des droits restants, retenue de 3 %, deux versements | 30 oct., p. 23 | **Confirmé** [FV] | Cumul ARE plafonné à 60 % des droits restants depuis le 1er avril 2025 ; second versement incompatible avec un CDI à temps plein |
| 17 | « Carlone veut vous salarier et acheter des prestations » | 30 oct., p. 20 | **Non sourcé du côté du client** : c'est le souhait de Morgan [DR] | Intention de GianLuca : [IN] |
| 18 | Les gains d'automatisation servent « à ajuster le forfait » | 30 oct., p. 4 | **Contraire à la demande** (rémunérer la valeur quand le temps baisse) | Retiré ; règle de partage des gains en 04-catalogue-offres.md |
| 19 | Un même PDF réunit les pages client et l'annexe interne « à partir de la page 17 » ; il porte l'ancien prénom erroné | 30 oct., p. 1, 5, 12, 17 | **Toujours vrai** [FV] | Ne jamais transmettre ce fichier |
| 20 | Signer au nom de la société en formation, puis faire reprendre l'acte | 29 oct., p. 6 ; `interne/offre-marwin-tech-remuneration-et-collaboration.md:185` | **Confirmé** [FV] (art. L210-6 C. com. ; Cass. com. 2023 et 2025) | Ajouter : aucun encaissement avant l'immatriculation (section 10.1) |
| 21 | « Sans société, pas d'acompte possible » | `interne/contexte-projet-carlone.md:12` | **Juste en pratique** [HY] | Signer en formation si nécessaire, encaisser après |
| 22 | Norme ISO 10218-2:2025 comme référence pour un bras « près du public » | `interne/offre-marwin-tech-remuneration-et-collaboration.md:100` ; `interne/contexte-projet-carlone.md:97` | **Faux** : la norme exclut les dangers « when the public or non-working adults have access » [FV] | Analyse de risques propre au lieu et au public, par un intégrateur (section 16) |
| 23 | 238 bis AB : « achats jusqu'au 31/12/2028 inclus » | `crm/PASSATION.md:28` | **Faux à la lettre** : « avant le 31 décembre 2028 » [FV] | Corriger |
| 24 | Trois registres d'actifs ; « BOJ.ART, l'atelier Jarvis et UNUM conservent leurs propriétaires » | 29 oct., p. 4 | **Tient** [PR] | Il manque la liste des droits, la durée, le territoire, l'exclusivité et les licences tierces (section 13) |
| 25 | « Un sujet, un accord » ; garder la majorité ; jamais une baisse d'honoraires contre un investissement | `interne/offre-marwin-tech-remuneration-et-collaboration.md:132, 146, 149` ; `interne/contexte-projet-carlone.md:93` | **Tient** [PR] | Inscrit au pacte (section 12) |
| 26 | Un associé qui vit d'un emploi extérieur : SAS à l'IS avec mandat non rémunéré | 30 oct., p. 17, 20 | **Tient** [FV pour la règle sociale] | Argument de plus pour la SAS |
| 27 | « Ne pas dépendre d'un seul client » : un deuxième client d'ici le quatrième mois | `interne/contexte-projet-carlone.md:95` | **Tient comme principe**, irréaliste comme date | La stratégie vise un second client vers le mois 7, sinon une dépendance assumée par écrit (`travaux/strategie-retenue.md:522`) |
| 28 | CIR, CII ou JEI « seulement sur des travaux effectivement éligibles et documentés ; la simple utilisation d'IA ne suffit pas » | 30 oct., p. 22 | **Tient** [PR] | Aucun crédit d'impôt compté (section 11) |

---

## 10. Avant l'immatriculation et au démarrage

### 10.1 Engagements antérieurs à l'immatriculation

**Règles** [FV] (`travaux/ver-R1-structures.md:28`) :
- La société n'a la personnalité morale qu'à son immatriculation (art. L210-6 C. com., https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006222358, consulté le 4 nov. 2026).
- Ceux qui agissent avant en son nom sont **tenus solidairement et indéfiniment** des actes, sauf reprise.
- La reprise passe par un état des actes présenté aux associés avant la signature des statuts et annexé à ceux-ci, ou par un mandat donné pour des engagements déterminés, ou par une décision des associés après l'immatriculation [FV pour les deux premiers modes ; DR pour le troisième] (`travaux/rj-R1-structures.md:259-265`).
- La mention « au nom de la société en formation » n'est plus une condition absolue (Cass. com., 29 nov. 2023, n° 22-12.865). Mais la reprise « ne peut résulter du seul accord » : les conditions légales s'imposent (Cass. com., 18 juin 2025, n° 24-14.311, https://www.legifrance.gouv.fr/juri/id/JURITEXT000051823267, consulté le 4 nov. 2026).

**Ce qu'il faut faire** [PR] :
1. Statuts et pacte préparés en novembre ; immatriculation déclenchée par un engagement écrit d'une entité identifiée de GianLuca (`travaux/strategie-retenue.md:552`).
2. Rien n'est encaissé avant l'immatriculation, ni sur un compte personnel, ni par l'entreprise existante de Morgan (`travaux/strategie-retenue.md:458`).
3. Aucune exécution risquée avant la reprise : achats, données personnelles, accès aux systèmes du client (`travaux/syn-droit.md:284`).
4. Décrire fidèlement le travail déjà fait (CRM, catalogue, études), même non facturé : « l'absence de facture […] ne prouve pas, à elle seule, que l'activité n'a pas déjà débuté » (`interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 17) [FV].
5. Proposer à l'entité de GianLuca de demander le K-bis avant de verser l'acompte : cela protège aussi le payeur.

> **Écart avec la stratégie retenue.** La stratégie admet que l'engagement qui déclenche l'immatriculation soit « une lettre d'intention ou un bon de commande « en formation » » (`travaux/strategie-retenue.md:452, 552`). Je recommande de **préférer la lettre d'intention**, signée par la seule entité de GianLuca, et de signer le bon de commande **après** l'immatriculation. Raisons : (1) un acte signé « en formation » engage Morgan et Mathys personnellement, solidairement et indéfiniment, tant que la reprise n'est pas faite [FV] ; (2) la reprise doit être organisée à l'avance : si les statuts sont signés avant le bon de commande, l'état annexé ne peut plus le contenir et il faut un mandat préalable ou une décision après l'immatriculation [FV/DR] ; un oubli laisse l'engagement aux deux associés ; (3) la RC professionnelle de Marwin n'existe pas encore ; (4) le gain est faible : l'immatriculation prend 1 à 3 semaines [HY] (`travaux/strategie-retenue.md:486`), et le travail ne démarre de toute façon qu'à l'encaissement de l'acompte, après l'immatriculation (`travaux/strategie-retenue.md:456-458`). Si l'entité de GianLuca exige un bon de commande signé avant, on le signe « en formation », comme le prévoit la stratégie, avec l'avocat qui organise l'état des actes ou le mandat. Le reste de la stratégie ne change pas.

### 10.2 Facturation

| Sujet | Règle au 4 nov. 2026 | Ce que fait Marwin [PR] | Code et source |
| --- | --- | --- | --- |
| **TVA : franchise** | Services : 37 500 € (année précédente), seuil majoré 41 250 € (année en cours). Au-delà du seuil majoré, la franchise cesse dès le jour du dépassement. Le CA de l'année de création serait annualisé pour juger l'année suivante [HY] | **Facturer la TVA dès la première facture** (option ou régime réel). Dans le scénario central (≈ 90 000 € HT sur 12 mois), le seuil majoré serait franchi au cours de la première année [ES] | [FV] art. 293 B CGI, F21746 (`travaux/ver-R2-fiscal.md:36`) ; `travaux/strategie-retenue.md:462` |
| TVA sur les acomptes | Pour une prestation de services, exigible **à l'encaissement**, avec une facture d'acompte | Exemple : acompte du cadrage de 3 250 € HT = 650 € de TVA, 3 900 € TTC [ES] | [FV] art. 269 CGI (`travaux/ver-R2-fiscal.md:37`) |
| Ce que coûte la TVA au client | Neutre si son entité la récupère ; un coût réel sinon | Devis en HT **et** TTC ; question posée à GianLuca | [HY] (`travaux/strategie-retenue.md:462`) |
| **Facture électronique : réception** | Obligatoire pour toutes les entreprises depuis le 1er sept. 2026 | Choisir une plateforme agréée et vérifier l'inscription à l'annuaire **dès la création** | [FV] FAQ DGFiP du 01/09/2026 (`travaux/ver-R2-fiscal.md:35`) |
| **Facture électronique : émission et e-reporting** | PME et microentreprises : **au plus tard le 1er sept. 2027** | Outil de facturation compatible dès le départ | [FV] fiche 3 DGFiP, « mise à jour octobre 2026 » (`travaux/ver-R2-fiscal.md:35`) |
| Quatre nouvelles mentions | SIREN du client ; catégorie de l'opération ; option pour les débits ; adresse de livraison si différente. Les sources officielles se contredisent sur leur date | Les porter **dès la première facture** | [FV] FAQ DGFiP ; contradiction avec F31808 (`travaux/rj-R2-fiscal.md:296-302`) |
| Sanctions | 50 € par facture non électronique, plafonnés à 15 000 € par an, une fois l'émission obligatoire ; 500 € puis 1 000 € sans plateforme de réception, après mise en demeure | — | [FV] FAQ DGFiP, texte légal non lu (`travaux/ver-R2-fiscal.md:35`) |
| Mentions obligatoires | Numéro, dates, identité et SIREN, forme et capital, TVA, détail, conditions de paiement, pénalités, indemnité de 40 €, escompte | Modèle de facture validé par l'expert-comptable | [FV] F31808 (`travaux/rj-R2-fiscal.md:387-395`) |
| Délais de paiement | 30 jours sans clause ; au plus 60 jours, ou 45 jours fin de mois | Calendrier de la stratégie : acompte, solde à 8 jours, socle d'avance | [FV] art. L441-10 C. com. ; `travaux/strategie-retenue.md:436-447` |
| Pénalités de retard | Au moins 3 fois le taux légal (8,25 % au second semestre 2026) ; à défaut, taux BCE + 10 points (12,40 %, puis ≈ 12,65 % au premier semestre 2027 si la BCE ne bouge pas) ; indemnité de 40 € | Taux fixe écrit au contrat | [FV] ; [ES] pour 2027 (`travaux/ver-R2-fiscal.md:37`) |
| Rétractation des petites entreprises | Contrat **hors établissement** avec une entreprise de **5 salariés au plus**, hors de son activité principale : 14 jours de rétractation, aucun paiement avant 7 jours | Connaître l'effectif de l'entité ; signer à distance ou prévoir les 7 jours ; l'avocat tranche si la règle vise le contrat de Marwin [HY] | [FV] art. L221-3 C. consom. (`travaux/ver-R5-art-lieux.md:39`) ; `travaux/strategie-retenue.md:466` |
| Vigilance du client envers Marwin | Contrat d'au moins 5 000 € HT : attestation Urssaf de moins de 6 mois et justificatif d'immatriculation, à la signature puis tous les 6 mois. Le cadrage de 6 500 € HT est concerné | K-bis ou accusé de réception de l'immatriculation, et attestation, remis à la signature. **Délai d'obtention de l'attestation pour une société nouvelle : [IN]** | [FV] art. R8222-1 et D8222-5 C. trav. (`travaux/ver-R3-travail-contrats.md:35`) |
| Vigilance de Marwin envers ses sous-traitants | Mêmes pièces dès 5 000 € HT cumulés | Pour tout freelance ou partenaire | [PR] (`travaux/syn-droit.md:388`) |

### 10.3 Calendrier de création

| Échéance | Quoi | Qui | Code et source |
| --- | --- | --- | --- |
| À la constitution | Capital déposé et **entièrement libéré** ; statuts ; pacte signé ; bénéficiaires effectifs déclarés | Les associés | [FV] ; [DR] bénéficiaires effectifs (`travaux/syn-droit.md:293, 306`) |
| Dès la création | Compte professionnel ; RC professionnelle ; plateforme de réception des factures électroniques ; comptes techniques au nom de Marwin | Marwin | `travaux/strategie-retenue.md:554` |
| **Avant le 31 déc. de l'année de création** | Déclaration 1447-C-SD de CFE. La CFE n'est pas due l'année de création ; la déclaration sert à obtenir une base réduite de 50 % l'année suivante. Montant = base minimum × taux local [IN] | Marwin | [FV] F23547 (`travaux/ver-R2-fiscal.md:34`) |
| 60 jours après le début d'activité | Demande d'ACRE, si l'un des deux est éligible | Chaque associé | [FV] F11677 |
| 3 premiers mois du premier exercice | Option pour l'IR, si elle était retenue (non recommandée) | Tous les associés | [FV] art. 239 bis AB |
| Janvier 2027 | Revérifier IS, cotisations, ACRE, seuils (lois pour 2027) | Expert-comptable | [IN] (`travaux/syn-droit.md:72`) |
| Avant le 1er mai de chaque année | Pour la galerie seulement : déclaration de diffuseur, même à néant | Entité de GianLuca | [FV] (`travaux/ver-R5-art-lieux.md:38`) |
| 1er sept. 2027 | Émission des factures électroniques et e-reporting | Marwin | [FV] |

La date de création et la date de clôture du premier exercice se choisissent avec l'expert-comptable. Une création en décembre 2026 impose la déclaration de CFE dans le mois et un premier exercice soumis aux règles de 2027 [HY].

### 10.4 Assurances

| Assurance | Obligatoire ? | Qui la prend | Quand | Points à demander | Code et source |
| --- | --- | --- | --- | --- | --- |
| RC professionnelle de Marwin | Non en général ; obligatoire pour certaines activités réglementées que Marwin n'exerce pas | Marwin | **Avant la première prestation** | Activités couvertes (pilotage, développement, IA) ; exclusions IA, cyber et données ; plafond assuré au moins égal au plafond contractuel ; **déclaration sincère de la fuite** : une assurance prise après coup ne couvre probablement pas un incident déjà connu | [FV] F37365 (`travaux/ver-R3-travail-contrats.md:40`) ; [HY] (`travaux/strategie-retenue.md:554`) |
| Assurance du local | Oui si Marwin est locataire | Marwin | Si une convention de bureaux est signée (pas avant le mois 6) | La convention est-elle un bail ? [IN] | [FV] F37365 |
| Cyber | Non | Marwin | À étudier avec la RC | Données du client, incidents d'agents IA | [HY] |
| Prévoyance, mutuelle, homme-clé | Non | Les dirigeants ; Marwin pour l'homme-clé | Avec le pacte | Un dirigeant de SAS non rémunéré n'a aucun droit social ; rachat des parts en cas de décès ou d'incapacité | [PR] (`travaux/syn-droit.md:296`) |
| RC de l'organisateur d'un événement | Pas d'obligation générale trouvée ; indispensable en pratique | L'entité de GianLuca qui organise | Avant tout événement | — | [HY] (`travaux/ver-R5-art-lieux.md:61`) |
| « Clou à clou » pour les œuvres | Pratique de marché | La galerie ; un dépositaire rémunéré répond « avec plus de rigueur » (art. 1928 C. civ.) | Avant tout transport ou dépôt | Valeur agréée par œuvre | [HY] (`travaux/syn-droit.md:538`) |
| RC produits d'une machine | — | Le fabricant ou l'intégrateur | Avant toute mise en service | Couverture d'une démonstration avec public | [IN] (`travaux/rj-R5-art-lieux.md:537`) |

### 10.5 Responsabilités

| Qui | Pour quoi | Règle | Parade [PR] |
| --- | --- | --- | --- |
| Morgan et Mathys, à titre personnel | Actes signés avant l'immatriculation | Solidaire et indéfinie jusqu'à la reprise [FV] | Section 10.1 |
| Morgan et Mathys, à titre personnel | Fichier de prospects constitué et exposé avant toute société | Responsables de fait du traitement [HY] | Traité dans 01-synthese-direction.md et 12-gouvernance-contrat-sortie.md |
| Dirigeants de Marwin | Fautes de gestion ; cautions personnelles | « La responsabilité limitée connaît des exceptions, notamment les cautions personnelles et les fautes de gestion » [FV] | Aucune caution personnelle pour un engagement de Marwin sans accord écrit des deux |
| Marwin | Inexécution du contrat | Clause limitative admise entre professionnels, sauf faute lourde ou dolosive (art. 1231-3 C. civ.), ni si elle vide l'obligation essentielle (art. 1170), ni en cas de déséquilibre significatif dans un contrat d'adhésion (art. 1171) [FV] | Plafond lié aux honoraires et aligné sur l'assurance ; obligation de moyens pour le pilotage et les sorties d'IA (rédaction : 12-gouvernance-contrat-sortie.md) |
| Marwin | Activités réservées exercées pour le client | Exercice illégal de l'expertise comptable : 1 an et 15 000 € (art. 433-17 C. pén.) ; consultation juridique réservée (loi n° 71-1130, art. 54) ; gestion immobilière, vente de voyages, recouvrement : professions réglementées [FV] | Marwin prépare et coordonne ; elle n'exerce pas (`travaux/syn-droit.md:410-431` ; `travaux/strategie-retenue.md:650`) |
| Marwin | Calculs d'« économie d'impôt » envoyés aux prospects | Peuvent relever de la consultation juridique [HY] | Simulateur retiré ou validé par un professionnel (section 15) |
| Marwin | Machine assemblée et remise | Fabricant au sens du règlement machines [HY fondée sur FV] | Intégrateur tiers (section 16) |
| Entité de GianLuca | Requalification ; défaut de vigilance | Travail dissimulé ; solidarité financière [FV] | Section 7 ; pièces de vigilance remises par Marwin |

### 10.6 Validations professionnelles

| Sujet | Professionnel | Avant quoi | Payé par |
| --- | --- | --- | --- |
| Choix SAS ou SARL, simulations officielles, date de création | Expert-comptable de Marwin | Signature des statuts | Marwin |
| Statuts, pacte, état des actes, mandat de reprise | Avocat en droit des sociétés | Tout contrat client | Marwin |
| Contrat-cadre, limitation de responsabilité, rétractation, cession des droits | Avocat en contrats et propriété intellectuelle | Le premier bon de commande | Marwin |
| Subordination, convention de bureaux, salariat d'un associé | Avocat en droit du travail | Bureaux ou emploi (pas avant le mois 6) | Marwin |
| Notification de la fuite, rôles RGPD | Avocat ou DPD | Immédiatement | Marwin |
| Arguments fiscaux de vente des œuvres, schéma d'exposition | Avocat fiscaliste et expert-comptable **de GianLuca** et de chaque acheteur | Toute prospection | Entité de GianLuca |
| Registre, LCB-FT, droit de suite, dépôt-vente, « enchères » | Avocat du marché de l'art **de GianLuca** | Toute vente par la galerie | Entité de GianLuca |
| Classement ERP, autorisation de travaux, GN 6 | Mairie, commission de sécurité, bureau de contrôle | Tout événement public | Entité exploitante |
| Bras robotisé | Intégrateur, bureau de contrôle, assureur | Toute démonstration | Financeur du projet |
| Couvertures d'assurance | Assureur ou courtier | La première prestation | Marwin |

Les dossiers de questions sont à la section 19.

---

## 11. Aides et exonérations : rien n'est acquis

Le plan de trésorerie compte **zéro** pour chacune (`travaux/strategie-retenue.md:488, 564`).

| Dispositif | Ce qu'il apporterait | Conditions qui le rendent incertain | Statut | Code et source |
| --- | --- | --- | --- | --- |
| **FRR** (art. 44 quindecies A CGI) | Exonération d'IS ou d'IR pendant 59 mois, puis imposition au quart, à la moitié et aux trois quarts | Commune de Cosne classée en FRR de base [FV], mais adresse et moyens de Marwin inconnus ; implantation exclusive en zone ; domiciliataire insuffisant ; activité sédentaire hors zone au-delà de 25 % = perte totale ; pas d'extension d'une activité préexistante (CRM, entreprise de Morgan) ; plafond de minimis de 300 000 € par entreprise unique ; rescrit préalable conseillé | [IN] | [FV] art. 44 quindecies A (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049130324/, consulté le 4 nov. 2026) ; BOFiP du 29/07/2026, § 120, 130, 160, 260 (`travaux/ver-R2-fiscal.md:31-33`) |
| Exonération de CFE liée au FRR | CFE exonérée sur délibération locale | Délibération de Cœur de Loire du 26/09/2024 connue par une source secondaire ; liée au bénéfice du FRR | [DR] / [IN] | `travaux/ver-R2-fiscal.md:54` |
| **ACRE** | Exonération de 25 % des cotisations pendant 12 mois si le revenu est au plus de 36 045 €, dégressive jusqu'à 48 060 € ; au plus ≈ 2 000 € par personne et par an [ES] | Publics listés depuis le 1er janv. 2026 (dont création en zone FRR) ; demande sous 60 jours ; contrôle effectif 2 ans ; éligibilité de chacun [IN] ; règle du silence pour une société [IN]. Sans rémunération en SAS, elle ne sert à rien | [IN] | [FV] F11677, vérifiée le 01/07/2026 ; décret n° 2026-69 (`travaux/ver-R1-structures.md:25`) ; [ES] (`travaux/syn-droit.md:205`) |
| **ARE** (maintien) | Revenu de transition | Droits ouverts de chacun [IN] ; ARE réduite de 70 % des revenus ; cumul plafonné à 60 % des droits restants depuis le 1er avril 2025 ; cas du président de SAS non rémunéré non traité par la fiche officielle [HY] | [IN] | [FV] F36613 ; France Travail (`travaux/ver-R1-structures.md:26`) |
| **ARCE** | 60 % des droits restants, moins 3 %, en deux versements | Alternative au maintien de l'ARE ; ACRE obligatoire ; second versement incompatible avec un CDI à temps plein ; imposable | [IN] | [FV] (`travaux/ver-R1-structures.md:26`) |
| Aide régionale à la création | Avance remboursable de 20 000 à 200 000 € | « Ce n'est pas une subvention » ; apports et prêt bancaire exigés ; échéance annoncée au 31 déc. 2026 | [DR] | `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 23 |
| Aide régionale à l'investissement matériel | Avance remboursable, 20 % de l'assiette | Projet productif ; dépôt avant engagement ; « Ne pas acheter du matériel uniquement pour obtenir une aide » | [DR] | idem, p. 23 |
| Aide régionale au conseil stratégique | Subvention de 50 % jusqu'à 15 000 € sur deux ans, **pour le client** | Entreprise cliente de moins de 50 personnes, secteur admis, marchés hors région ; mission de 5 jours au moins ; 1 000 € HT par jour au plus ; **dépôt avant la signature du devis** ; exclut l'installation de logiciels ; éligibilité d'un prestataire nouveau [IN] | [DR] | idem, p. 23 ; `travaux/strategie-retenue.md:239` |
| CIR, CII, JEI | Crédits d'impôt ou exonérations | Travaux éligibles et documentés seulement ; « la simple utilisation d'IA ne suffit pas » | Non étudié, non compté | idem, p. 22 |
| Exonération patronale FRR à l'embauche | Allègement sur un recrutement | Aucun recrutement prévu la première année | Sans objet | idem, p. 21 |

---

## 12. Entre Morgan et Mathys : ce que le pacte règle avant le contrat client

Toutes ces clauses sont des propositions [PR] à faire rédiger et valider par l'avocat (`travaux/strategie-retenue.md:617-619` ; `travaux/syn-droit.md:464-482`). Les rituels de suivi (revue trimestrielle, relevé du temps) sont dans 06-fonctionnement-a-deux.md.

| Thème | Fait connu | Risque | Clause proposée | Point juridique |
| --- | --- | --- | --- | --- |
| **Disponibilité** | Morgan : plusieurs autres projets [FV] ; Mathys : [IN] (`travaux/note-point-4-novembre-et-activites.md:12-17`) | Aucun engagement tenable ; le plus disponible porte tout | JP minimales par mois et par associé, de décembre 2026 à juin 2027 ; relevé mensuel ; **déclaration écrite des autres activités** (OLSEN, « Shelby », BOJ.ART, ventes en ligne…) et règle de priorité ; non-concurrence limitée aux clients et à l'objet de Marwin, pendant le mandat | Non-concurrence d'associé à proportionner [HY] |
| **Apports** | Apport visé de 8 000 à 14 000 € ; capacité de chacun [IN] | Apport inégal ; capital non libéré | Numéraire à parts égales, **entièrement libéré** ; complément en compte courant, remboursable selon une règle écrite ; apport en industrie possible pour un temps inégal, sans effet sur la propriété intellectuelle | Commissaire aux apports pour un apport en nature, sauf exception [FV] |
| **Propriété du travail existant** | CRM co-écrit, sans licence, dépôt au compte FinanceScope (présenté comme celui de Mathys) [DR] ; Jarvis dans un dépôt public sans licence globale [FV] | Personne ne peut céder au client ; un associé qui part garde l'outil | **Inventaire daté** des actifs de chacun. Par défaut, licence non exclusive à Marwin pour la durée du pacte, pour les clients de Marwin ; ou cession écrite. Distinguer les co-auteurs du CRM. Régler Jarvis (part BOJ.ART et Medhi, part Morgan) et le nom | Cession écrite, mention distincte de chaque droit, domaine délimité (art. L131-2, L131-3 CPI) ; cession gratuite expresse ; protection du code généré par IA [IN] |
| **Travail futur** | — | Revendication d'un associé sur un livrable | Chaque associé cède ou concède à Marwin ses créations faites pour elle, **livrable par livrable** ; pas de cession globale des œuvres futures | Cession globale des œuvres futures nulle (art. L131-1 CPI) [FV] ; le régime des logiciels de salariés ne joue pas pour un dirigeant non salarié [HY] |
| **Rémunérations différentes** | Temps probablement inégal [HY] | Ressentiment, blocage de la décision collective | Grille écrite : rémunération liée au temps engagé et à la fonction ; plafond au pacte ; dividendes au prorata du capital | En SAS, organe désigné par les statuts [HY] |
| **Désaccord** | — | Rien ne se décide ; le client attend | Liste des décisions à l'unanimité (section 4) ; tant que le désaccord dure, rien n'est proposé au client ; puis médiation, puis tiers expert | Pacte non respecté : surtout des dommages-intérêts [HY] |
| **Blocage durable** | 50/50 | Société paralysée | En dernier recours, **offre alternative** (l'un propose un prix, l'autre achète ou vend à ce prix) ou rachat à dire d'expert ; clause d'exclusion dans les statuts de la SAS | Validité, exécution forcée, articulation avec l'art. 1843-4 C. civ. [IN] ; clause d'exclusion (art. L227-16 C. com., non rouvert) [HY] |
| **Départ** | — | Clients, accès et code partent avec l'associé | Préavis ; transmission des dossiers et des accès ; non-sollicitation des clients ; non-concurrence limitée et rémunérée si nécessaire ; prix de rachat selon le motif du départ (« good / bad leaver ») | À valider par l'avocat [IN] |
| **Incapacité ou décès** | Morgan est le point de défaillance unique (06-fonctionnement-a-deux.md, section 7) | Plus personne ne peut signer ni accéder aux comptes | **Coffre partagé des accès et des secrets** ; délégation de signature croisée ; intérim de direction ; rachat des titres ; assurance homme-clé | Un dirigeant de SAS non rémunéré n'a pas d'indemnités journalières [FV] |
| **Conflits d'intérêts** | Lien de Morgan avec BOJ.ART [DR] | Recommandation biaisée au client | Déclaration écrite des liens (BOJ.ART, Medhi, OLSEN, toute entité de GianLuca) ; abstention sur les décisions concernées ; information du client | — |
| **Données des clients** | CRM sous les comptes des associés [FV] | Réutilisation des données de GianLuca | **Aucune réutilisation** des données de GianLuca pour la prospection de Marwin ou d'OLSEN ; un kit CRM vendu à d'autres ne contient que des composants génériques ; comptes techniques au nom de Marwin ou du client | RGPD, art. 28 et 32 |
| **Associés et tiers** | Eaglemic présenté comme associé de Morgan [DR] | Un tiers revendique un rôle | Liste fermée des associés ; toute entrée à l'unanimité | — |

---

## 13. Droits et propriété

**Principe** [FV] : commander et payer ne rend pas le client propriétaire. Le contrat d'ouvrage « n'emporte pas dérogation » aux droits de l'auteur (art. L111-1 CPI). Il faut une cession écrite, chaque droit mentionné à part, sans cession globale des œuvres futures (art. L131-1 à L131-3 CPI, https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069414/LEGISCTA000006161639/, consulté le 4 nov. 2026 ; `travaux/ver-R3-travail-contrats.md:42`).

| Actif | État aujourd'hui | Titulaire probable | Risque | Régime recommandé [PR] | Décision et échéance |
| --- | --- | --- | --- | --- | --- |
| **Code du CRM** | Co-écrit par Morgan et Mathys, en grande partie par des agents IA ; aucune licence ; dépôt public au compte FinanceScope ; version Firebase « sous le compte des associés » ; « offert à ce jour » [FV] (`crm/docs/rapport/rapport-crm-hermes360.md:12` ; `interne/offre-marwin-tech-remuneration-et-collaboration.md:227`) | Les associés [HY] ; part protégeable du code généré [IN] | Le client paie la suite sans droit sur la base ; promesse de réversibilité inexacte | Cession ou licence des associés à Marwin ; puis, avec GianLuca, licence d'usage perpétuelle non exclusive, ou cession des développements propres au client à leur paiement. **Écrire le régime du CRM « offert »**, même gratuit. Jamais refacturé (`travaux/strategie-retenue.md:385`) | Pacte, avant tout lot CRM |
| **Données du CRM** (≈ 500 entreprises, dirigeants, coordonnées) | « le code, les données et le suivi restent chez les associés » [FV] (`crm/docs/rapport/rapport-crm-hermes360.md:19`) | Fonctionnellement : le responsable du traitement, qui serait l'entité vendeuse de GianLuca [HY] | Phrase incompatible avec un rôle de sous-traitant ; droit du producteur de bases de données non examiné | Données à l'entité de GianLuca, restituées ou supprimées à son choix (RGPD, art. 28.3 g) ; Marwin n'en garde aucune copie après la mission | Après avis sur les rôles RGPD (12-gouvernance-contrat-sortie.md) |
| **Outils préexistants** (Jarvis, scripts, méthodes, modèles) | Jarvis : dépôt public BOJART sans licence globale ; « Aucune licence globale nouvelle n'est imposée » [FV] (dépôt Momolscode/BOJART, `jarvis/LICENSE_SCOPE.md:2`, commit 3436f53) | Leurs auteurs ; partage BOJ.ART / Morgan non tranché | Vendre « Jarvis » sans inventaire ; confusion entre un actif tiers et un livrable | Inventaire des composants et licences ; licence de l'auteur à Marwin ; licence d'usage non exclusive au client ; « Copilote Jarvis » suspendu (`travaux/strategie-retenue.md:648`) | Pacte |
| **Composants réutilisables de Marwin** | À créer après l'immatriculation | Marwin | Revendication du client, ou de l'employeur si un associé est salarié chez lui (art. L113-9 CPI) | Marwin reste propriétaire ; licence gratuite, non exclusive et perpétuelle pour l'usage interne du client, maintenue après le contrat | Contrat-cadre |
| **Développements propres au client** | À créer | Marwin jusqu'à cession | Le client paie mais dépend de Marwin | **Cession par livrable**, à la réception et au paiement complet ; annexe des droits (étendue, destination, lieu, durée) ; code, documentation et comptes remis | Chaque bon de commande |
| **Créations et contenus** (catalogue d'offres, textes, supports, études) | Produits pour GianLuca sans commande ni prix [FV] | Les associés | Mélange avec les pièces internes ; mentions fiscales non validées | Cession des contenus livrés au paiement ; contenus fiscaux validés par un professionnel avant usage | Au cadrage |
| **Œuvres de Medhi** (sculptures, motifs, STRATES) | « Ses œuvres, ses droits d'auteur, ses machines » (`interne/offre-marwin-tech-remuneration-et-collaboration.md:90`) ; hors de l'offre depuis le 4 nov. [DR] | Medhi | L'offre écrite promet encore exclusivité et films : Marwin ne peut pas céder ce qu'elle ne détient pas | Retirer ces promesses ; dépôt-vente direct entre Medhi et l'entité de GianLuca | Documents marqués « historique » |
| **Fichiers de fabrication** (STL, parcours du bras, réglages) | Mêlent le motif de l'artiste et la technique | Medhi pour le motif ; l'auteur technique pour le reste [HY] | Reproduction d'une œuvre sans autorisation | **Aucune utilisation par Marwin** depuis le retrait de Medhi ; sinon contrat à trois, licence limitée à la fabrication autorisée | — |
| **Films et images** | Film de concept généré « avec Kling 3.0 Pro via Higgsfield » (`pour-carlone/strates-proposition-artistique-v1.1.pdf` p. 8) ; film de la soirée envoyé aux invités par le CRM (`pour-carlone/vernissage-strates-idees.md:25`) | Selon les conditions de l'outil d'IA [IN] ; artistes montrés ; personnes filmées | Droits des artistes ; **droit à l'image des invités** ; mention « généré par IA » (AI Act, art. 50, § 4) | Autorisation écrite de chaque artiste ; consentement des personnes filmées ; étiquetage IA ; conditions des outils vérifiées | Avant toute diffusion |
| **Matériel** (station, bras, banc) | « Matériel acheté et possédé par votre entité » (diaporama client, `slides/laboratoire.html:14`) [FV] | L'entité de GianLuca | Si Marwin achète puis refacture, elle porte le risque ; si elle assemble, elle devient fabricant | Achats directs par l'entité cliente ; machines de BOJ.ART à leurs propriétaires ; intégrateur tiers pour la conformité | Section 6.3 |

**Réversibilité.** Le diaporama promet « Réversibilité : fichiers, configurations, documentations et accès remis » (diaporama client, `slides/garanties.html:30`) [FV]. C'est inexact tant que le CRM reste sous les comptes des associés. Si Marwin hébergeait et exploitait un service de données pour le client, le Data Act imposerait des clauses de changement de fournisseur : préavis de 2 mois au plus, transition de 30 jours au plus, au moins 30 jours pour récupérer les données ; aucuns frais de changement à compter du 12 janv. 2027. L'exemption « sur mesure » ne couvre pas ces clauses [FV] (règlement (UE) 2023/2854, art. 25 et 29, https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32023R2854, consulté le 4 nov. 2026 ; `travaux/ver-R3-travail-contrats.md:43, 80`). Solution la plus simple : comptes au nom de l'entité cliente dès le premier jour, Marwin intervenant comme collaborateur (`travaux/strategie-retenue.md:189`).

---

## 14. Galerie, œuvres et événements : obligations réelles et à qui elles incombent

**Principe** [PR] : ce sont des obligations de vendeur, d'organisateur ou d'exploitant. Elles incombent à l'entité de GianLuca qui vend, organise ou exploite, encore non identifiée [IN]. Marwin coordonne sous mandat écrit, sans être titulaire des autorisations, sans encaisser, sans garder d'œuvres et sans fabriquer de machine (`travaux/syn-droit.md:516-520`).

| Obligation | Contenu au 4 nov. 2026 | Incombe à | Marwin y serait soumise si… | Code et source |
| --- | --- | --- | --- | --- |
| Registre des objets mobiliers | Toute vente d'objets acquis auprès d'autres que leurs fabricants ; tenue jour par jour ; déclaration préalable en préfecture ; 6 mois et 30 000 € ; si le vendeur est une société, l'obligation pèse sur **ses dirigeants** | Entité qui vend et ses dirigeants ; probablement pas pour le premier marché seul [HY] | elle achetait pour revendre | [FV] art. 321-7 C. pén. (`travaux/ver-R5-art-lieux.md:33`) |
| Lutte contre le blanchiment | Marchands et intermédiaires d'œuvres, galeries comprises, dès **10 000 €** : identification, bénéficiaire effectif, personnes politiquement exposées, cartographie, déclarant Tracfin, conservation 5 ans ; espèces limitées à 1 000 € pour un client domicilié en France ; règlement européen applicable le 10 juill. 2027 | Entité qui vend | elle trouvait des acheteurs contre commission ou encaissait pour la galerie | [FV] art. L561-2, 10° CMF (`travaux/ver-R5-art-lieux.md:34-35`) |
| Droit de suite | Reventes avec un professionnel ; dès 750 € ; 4 % jusqu'à 50 000 €, puis dégressif ; plafond 12 500 € ; à la charge du vendeur | Entité qui vend | elle était l'intermédiaire qui reçoit le paiement | [FV] art. L122-8 CPI (`travaux/ver-R5-art-lieux.md:36`) |
| Contribution des diffuseurs | 1 % + 0,1 % de 30 % du prix TTC, ou de la commission TTC en dépôt-vente ; déclaration annuelle avant le 1er mai, même à néant | Galerie | — | [FV] urssaf.fr, vérifiée le 26/01/2026 (`travaux/ver-R5-art-lieux.md:38`) |
| Facture et authenticité | Pas de certificat obligatoire ; facture détaillée si l'acheteur la demande ; mention « Reproduction » ; une pièce faite à la machine est décrite comme telle | Vendeur | — | [FV] décret n° 81-255 (`travaux/ver-R5-art-lieux.md:37`) ; [HY] description |
| Rétractation | Vente hors établissement à une entreprise de 5 salariés au plus, hors de son activité principale : 14 jours, aucun paiement avant 7 jours ; un vernissage en entreprise est hors établissement | Entité qui vend | — | [FV] art. L221-3 C. consom. (`travaux/ver-R5-art-lieux.md:39`) |
| TVA des œuvres | 5,5 % sur toutes les livraisons depuis le 1er janv. 2025, sauf régime de la marge ; pièces faites à la machine à 20 % [HY] | Entité qui vend | elle revendait des pièces | [FV] (`travaux/ver-R2-fiscal.md:30`) |
| Dépôt-vente avec les artistes | Aucun contrat type légal ; inventaire, prix plancher, commission, garde, assurance, droits de reproduction, restitution | Entité de GianLuca et chaque artiste | elle signait à leur place | [HY] (`travaux/syn-droit.md:539`) |
| « Enchères » en fin de soirée | Appellation réservée aux opérateurs habilités | Opérateur habilité | — | [FV partiel] art. L321-2 C. com. (`travaux/syn-droit.md:537`) ; idées « mise aux enchères » (`pour-carlone/vernissage-strates-idees.md:81, 89`) |
| Assurances | Voir section 10.4 | Organisateur ; galerie | elle transportait ou gardait des œuvres | [HY] |
| Lieux, boissons, spectacles, musique | Voir section 16 | Exploitant ; organisateur | elle était organisatrice ou utilisatrice des locaux | [FV] |

**Conséquence pour l'offre** [PR] : aucune commission, aucun encaissement, aucune garde ni aucun transport d'œuvres par Marwin la première année (`travaux/strategie-retenue.md:422, 649`).

---

## 15. Arguments fiscaux pour les entreprises : ce qui tient, ce qui ne tient pas

| Argument | Statut | Ce qu'on peut écrire | Code et source |
| --- | --- | --- | --- |
| Déduction des œuvres d'artistes vivants (238 bis AB) | **Validée** pour les achats faits **avant le 31 déc. 2028** (loi n° 2026-103, art. 89) | Sociétés à l'IS et sociétés de personnes (pas les BNC) ; œuvre originale inscrite à l'actif immobilisé ; déduction par cinquièmes ; plafond de 20 000 € ou 5 ‰ du CA, le plus élevé, **diminué des dons de mécénat**, commun à toutes les œuvres ; excédent perdu ; réserve spéciale ; réintégration en cas de cession | [FV] https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868630, consulté le 4 nov. 2026 ; BOI-BIC-CHG-70-10 du 15/04/2026 (`travaux/ver-R2-fiscal.md:26-27`) |
| Lieu d'exposition | **Validé avec limites** | 5 ans, lieu accessible au public ou aux salariés ; **jamais les bureaux** ; pas un lieu « réservé aux seuls clients » ; manifestations d'un musée, d'une collectivité ou d'un établissement public | [FV] BOFiP § 90 |
| Exposition chez le vendeur (galerie de GianLuca, Vieux Relais) | **Non validé** : une galerie commerciale n'est pas citée ; risque de régime « biens divers » | Rien avant un avis écrit d'un avocat fiscaliste | [HY] (`travaux/syn-droit.md:570`) |
| Hôtels, restaurants, halls comme lieux « accessibles au public » | **Incertain** | Au cas par cas | [HY] |
| Pièces imprimées en 3D, peintes par un robot ou générées par IA (dont STRATES) | **Très probablement exclues** de la déduction et du taux de 5,5 % | Vendre par la galerie, sans argument fiscal ; ou rescrit sur une pièce précise | [HY] fondée sur l'art. 98 A, annexe III CGI (« entièrement exécutés à la main ») et la doctrine du 20/03/2024 (§ 135, 140, 210) ; question écrite AN n° 22584 (`travaux/ver-R2-fiscal.md:28-29`) |
| Rescrit sur une pièce | Possible (art. L80 B, 1° LPF) ; **le silence ne vaut pas accord** | Décision du vendeur, à ses frais | [FV] |
| « Mécénat » pour l'achat d'une œuvre | **Faux** : autre dispositif (réduction de 60 % pour un don sans contrepartie à un organisme d'intérêt général ; dons aux artistes exclus) | Ne jamais employer le mot | [FV] F22263 (`travaux/ver-R2-fiscal.md:27`) |
| Économie d'impôt de 25 % affichée par le CRM | **Surestimée** : taux fixe de 25 % sans le taux PME ni le bénéfice réel (`crm/art_merge.py:19, 129`) [FV] ; jusqu'à 1 043 750 € affichés pour une entreprise | Retirer ou corriger le simulateur ; renvoyer chaque prospect à son expert-comptable | `travaux/strategie-retenue.md:211, 653` |
| Prix de l'œuvre calé sur « cinq fois le plafond » du client | Prix fondé sur la capacité fiscale, pas sur la valeur | Cote ou ventes comparables par artiste | [PR] (`travaux/syn-droit.md:573`) |
| « Suivi sur cinq ans » inclus dans le prix ; attestation annuelle | Gonfle la base déductible ; engage celui qui signe | Facturer à part ; désigner le signataire et son assurance | `travaux/syn-droit.md:574` |
| Rendement, plus-value, rachat garanti | Fait basculer dans le régime des intermédiaires en biens divers | Ne jamais le promettre | [DR] (`interne/contexte-projet-carlone.md:91`) |
| Avantage fiscal pour une entreprise qui achète de l'impression 3D, de la robotique ou de l'IA | **Aucun dispositif validé** dans l'audit ; CIR, CII ou JEI seulement pour des travaux éligibles et documentés | Aucun argument fiscal sur ces technologies sans avis écrit | [PR] (`travaux/syn-droit.md:579`) |
| TVA des prestations de Marwin | 20 % | — | [FV, risque d'erreur faible] (`travaux/ver-R2-fiscal.md:57`) |

**Corrections à reporter dans les pièces** [FV] : `crm/PASSATION.md:28` (« avant », pas « inclus ») ; `interne/offres-de-carlone-catalogue-crm.md:99` (le BOFiP prévoit des lieux tiers publics, pas une galerie commerciale) (`travaux/syn-droit.md:582-587`). Le lot C8 (kit de campagne) n'est vendu qu'avec des mentions fiscales validées par le conseil du client (`travaux/strategie-retenue.md:298`).

---

## 16. Lieux et robotique

### 16.1 Lieux : qui exploite, qui répond du public

- **Aucun lieu n'est établi** : galerie, Vieux Relais, le M, cabaret et « six bâtiments » reposent sur des déclarations rapportées, contradictoires (`travaux/ex-C9-lieux.md:219`) [DR/IN].
- **L'exploitant est l'entité de GianLuca.** Elle demande et détient les autorisations, emploie les artistes, s'assure. Marwin prépare les dossiers (lots C3, C4, C7) et coordonne sous mandat écrit, sans devenir exploitant ni organisateur (`travaux/strategie-retenue.md:647` ; `travaux/rj-R5-art-lieux.md:402`).

| Règle | Contenu | Code et source |
| --- | --- | --- |
| Établissement recevant du public | Classement par type et catégorie (galerie M ou T : 5e catégorie jusqu'à 200 personnes ; cabaret L : 50) ; autorisation de travaux (4 mois) ; visite et arrêté d'ouverture | [FV] art. PE 2, version du 01/01/2026 (`travaux/ver-R5-art-lieux.md:40`) |
| Manifestation inhabituelle ou démonstration à risque | Demande **au moins deux mois avant**, présentée conjointement par l'exploitant et l'utilisateur occasionnel des locaux | [FV] art. GN 6 (https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048310284, consulté le 4 nov. 2026 ; `travaux/ver-R5-art-lieux.md:41`) |
| Calendrier | **Aucun événement public en décembre 2026 dans un lieu non autorisé** : 2 à 3 mois dans un établissement déjà ouvert, 4 à 6 mois ou plus dans un bâtiment à aménager. Cela contredit les « dates en décembre » du dossier du 21 oct. | [ES] (`travaux/rj-R5-art-lieux.md:353, 367`) ; `sources/dossier-partenariats-vieux-relais-et-le-m-2026-10-21.pdf` p. 32 |
| Boissons | Débit temporaire sur autorisation du maire (18° au plus) ; licence IV : création interdite, rachat ou transfert ; permis d'exploitation | [FV] F22379 (`travaux/ver-R5-art-lieux.md:52`) |
| Spectacles | Jusqu'à 6 représentations par an sans déclaration ; récépissé dès la 7e, un mois d'opposition ; artistes présumés salariés | [FV] (`travaux/ver-R5-art-lieux.md:42`) |
| Musique | Autorisation Sacem et rémunération Spré | [FV] F3094 |
| Cabaret | Métier réglementé d'exploitant, autorisations nominatives : ni Morgan ni Mathys ne les portent | [HY] (`travaux/rj-R5-art-lieux.md:467`) |

### 16.2 Robotique en présence du public

| Règle | Contenu | Code et source |
| --- | --- | --- |
| Règlement machines (UE) 2023/1230 | Applicable le **20 janv. 2027** ; modifié par le règlement (UE) 2026/1744 sans changement de cette date | [FV] (`travaux/ver-R5-art-lieux.md:43`) |
| Qui est fabricant | Celui qui fabrique une machine, y compris pour son propre usage, et celui qui fait une modification substantielle. Assembler un bras, un outil, une commande et une protection, c'est fabriquer une machine : marquage CE, documentation, déclaration | [FV] art. 10 et 18 ; [HY] application (`travaux/rj-R5-art-lieux.md:480-484`) |
| Norme ISO 10218-2:2025 | Ne couvre **pas** les dangers « when the public or non-working adults have access » | [FV] https://www.iso.org/standard/73934.html, consulté le 4 nov. 2026 (`travaux/ver-R5-art-lieux.md:50`) |
| Démonstration d'une machine non conforme | Possible avec un signe visible et des mesures de protection des personnes | [DR] confirmé par une source secondaire seulement (`travaux/ver-R5-art-lieux.md:54`) |
| Responsabilité du fait des produits | Nouvelle directive (UE) 2024/2853, logiciels et IA compris, pour les produits mis sur le marché ou en service **après le 8 déc. 2026** (rectificatif du 7 mai 2026) ; transposition française [IN] | [FV] (`travaux/ver-R5-art-lieux.md:44`) |
| Exploitant du lieu | Sécurité des visiteurs ; demande GN 6 ; obligation générale de sécurité des services ; sécurité de ses salariés | [FV partiel] (`travaux/rj-R5-art-lieux.md:487-491`) |

**Règles** [PR] (`travaux/strategie-retenue.md:646` ; `travaux/rj-R5-art-lieux.md:541-550`) :
- Jamais de robot devant le public sans intégrateur tiers, analyse de risques propre au lieu et au public, exploitant responsable et assurance identifiée.
- Marwin ne devient pas fabricant. Un intégrateur, choisi et payé par l'entité de GianLuca ou par le financeur, porte la conformité. Le contrat dit noir sur blanc qui est fabricant, qui est exploitant et qui assure.
- Premier jalon réaliste : un **banc d'essai fermé, sans public**.
- **Une image ou une simulation ne valide pas un équipement** (DEMANDE § 14). Les visuels générés par IA du vernissage et de STRATES restent des illustrations (`pour-carlone/strates-proposition-artistique-v1.1.pdf` p. 1 : « Visualisation générée par IA. Œuvre proposée, non fabriquée ») [FV].
- Un **premier événement sans robot** reste possible par le lot C3, l'organisateur légal étant l'entité de GianLuca.

---

## 17. Conditions pour tout projet exploratoire

**Règle générale** [PR] : rien d'exploratoire sans financeur écrit, budget plafonné et critère d'arrêt (`travaux/strategie-retenue.md:190`). Les conditions ci-dessous sont **toutes** requises.

| Condition | Contenu | Pourquoi |
| --- | --- | --- |
| Financeur écrit | Une entité identifiée signe un bon de commande pour la phase | Sans payeur, la recherche absorbe la marge |
| Budget plafonné | Honoraires de Marwin et achats séparés ; achats faits et payés par l'entité cliente | Section 6.3 |
| Responsable | Un nom côté client, un nom côté Marwin | Décisions et réception |
| Jalons | Phases courtes ; décision écrite « autoriser, adapter ou arrêter » avant chaque achat | Repris de `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 13 (`travaux/ver-C3-structure.md:29`) |
| Critère de poursuite et d'arrêt | Fixé avant l'essai, mesurable | Une démonstration ne prouve pas une valeur |
| Limite de dépense | Plafond par phase, jamais dépassé sans avenant signé avant | Section 4.10 de la stratégie |
| Capacité | Au plus 10 % de la capacité de Marwin, hors socle | `travaux/strategie-retenue.md:644-645` |
| Calendrier | Pas avant le mois 6 (laboratoire : mois 6 à 12) | Le cadrage et le pilote passent d'abord |
| Droits | Propriété des résultats, des fichiers et des films réglée par écrit avant le début | Section 13 |
| Sécurité | Intégrateur tiers pour toute machine ; banc fermé sans public | Section 16 |
| Données | Aucune donnée personnelle réelle sans les préalables RGPD | 12-gouvernance-contrat-sortie.md |

**Application** :

| Projet | Statut au 4 nov. 2026 | Ce qui manque pour qu'il revienne |
| --- | --- | --- |
| STRATES, Éclosion et autres créations | **Gelés** ; aucun budget propre (les 323 875 € du dossier investisseur portent sur les figurines) ; plus d'artiste | Financeur écrit ; artiste sous contrat ; banc fermé ; intégrateur ; droits réglés (`travaux/strategie-retenue.md:644`) |
| Laboratoire IA et robotique, DGX Spark, IA locale | **Retirés** ; aucun des processus étudiés ne demande de calcul local | Usage démontré (contrainte mesurée de confidentialité ou de volume) ; financeur ; achat par l'entité cliente (`travaux/strategie-retenue.md:645`) |
| Vernissage « signature » avec bras | **Reporté sans date** | Section 16 (`travaux/strategie-retenue.md:646`) |
| « Copilote Jarvis » comme produit | **Suspendu** | Propriété et licences réglées ; gain mesuré (`travaux/strategie-retenue.md:648`) |
| Agents vocaux sortants, outils RH | **Exclus** | Avis de l'avocat ou du DPD ; grille de sécurité (`travaux/strategie-retenue.md:652`) |

---

## 18. Recommandations : preuve, hypothèse, limite, décision

| Recommandation | Preuve | Hypothèse | Limite | Décision |
| --- | --- | --- | --- | --- |
| SAS à l'IS, capital entièrement libéré | Aucune rémunération financée [FV] ; 0 € de cotisation sans rémunération [FV] ; écart de 3 000 à 3 500 € par associé en central [ES] | Coefficient de 1,7 à 1,9 | Aucune simulation officielle ; règles de 2027 | Décision n° 4 (`travaux/strategie-retenue.md:718`) |
| Seule Marwin immatriculée facture ; rien encaissé avant | L210-6 C. com. [FV] ; domiciliation de l'autre entreprise résiliée [DR] | — | Délai d'immatriculation [HY] | Décision n° 4 |
| Lettre d'intention plutôt que bon de commande « en formation » | Responsabilité solidaire et indéfinie des signataires [FV] ; Cass. com., 18 juin 2025 [FV] | Le client accepte d'attendre 1 à 3 semaines | Le client peut exiger une signature | Écart, section 10.1 |
| Pacte signé avant le contrat client | Disponibilités non documentées [FV/IN] ; CRM sans licence [FV] | Les deux associés veulent continuer ensemble | Validité de certaines clauses [IN] | Décision n° 3 (`travaux/strategie-retenue.md:717`) |
| Un rôle à la fois pour GianLuca | Rôles cumulés [DR] ; requalification et travail dissimulé [FV] ; rupture brutale [FV] | GianLuca accepte des accords séparés | Ses intentions [IN] | `travaux/strategie-retenue.md:625-633` |
| Salariat refusé avant le bilan du mois 6 | L113-9 CPI ; loyauté [FV] ; poste à ≈ 3 400 € nets [MM] | — | L'offre d'emploi n'est pas sourcée [IN] | `travaux/strategie-retenue.md:707` |
| Medhi et BOJ.ART hors offre ; lien déclaré | Décision du 4 nov. [DR] ; documents non corrigés [FV] | Mathys est d'accord | Ce qui a été promis à Medhi [IN] | Décision n° 3 |
| Aucune aide comptée | Conditions FRR, ACRE, aides régionales [FV/DR] | — | Éligibilités [IN] | Plan de trésorerie (09-modele-economique-tresorerie.md) |
| Régime écrit de chaque actif | Aucun écrit sur la propriété [FV] ; L131-1 à L131-3 CPI [FV] | — | Protection du code généré par IA [IN] | Pacte puis contrat-cadre |
| Aucune commission, aucun encaissement, aucune garde d'œuvres | LCB-FT, droit de suite, registre [FV] | — | — | `travaux/strategie-retenue.md:422, 649` |
| Aucun argument fiscal sur les pièces faites à la machine | Art. 98 A ; doctrine de 2024 [FV] | Exclusion très probable [HY] | Un rescrit pourrait trancher autrement | Lot C8 conditionné |
| Aucun robot devant le public | ISO 10218-2 exclut le public [FV] ; règlement machines [FV] | — | Statut du bras [IN] | `travaux/strategie-retenue.md:646` |

---

## 19. Questions précises aux professionnels

### 19.1 À l'expert-comptable de Marwin (avant la signature des statuts)

1. Simuler sur mon-entreprise.urssaf.fr, avec les taux de 2026 puis de 2027, une SAS (président et DG) et une SARL (deux cogérants), sur les trois scénarios de `modele-financier/scenarios.md` : rémunération pure, avec réserve de 10 %, et en SAS un mélange petit salaire et dividendes. Pour chaque foyer réel.
2. Coût réel d'un président et d'un DG de SAS rémunérés : taux, accidents du travail, retraite complémentaire ; la réduction dégressive unique de 2026 s'applique-t-elle à un mandataire ?
3. Forfaits TNS de première année si la société est créée en décembre 2026 ou en janvier 2027, et montant de la régularisation de l'année 2.
4. Date de création et date de clôture du premier exercice ; plafond de 42 500 € au prorata ; avantage ou inconvénient d'une création en 2026.
5. TVA : opter dès la création ou appliquer la franchise ? Comment s'annualise le CA de l'année de création ? Régime réel normal ou simplifié ?
6. Facture électronique : quelle plateforme agréée et quel outil ? Porter les quatre nouvelles mentions dès la première facture ?
7. CFE : base minimum et taux local de la commune du siège ; quel CA de référence pour une société sans exercice N-2 ?
8. Siège : domicile d'un dirigeant, domiciliataire ou autre ? Effet sur la CFE et sur une demande future de FRR.
9. Frais engagés avant l'immatriculation (statuts, conseil sur la fuite) : sont-ils déductibles dans la société ? Comment les reprendre ?
10. Apport : quelle part en capital, quelle part en compte courant ? Règles de remboursement du compte courant.
11. Traitement des achats faits pour le client : débours, refacturation ou achat direct par le client (BOI-TVA-BASE-10-10-30, § 200).
12. Frontière entre le suivi budgétaire préparé par Marwin et la tenue de comptabilité réservée.
13. Effets d'une éventuelle requalification sur la TVA facturée et les cotisations déjà payées.
14. FRR, si un jour envisagé : Marwin serait-elle l'extension d'une activité préexistante de Morgan ou du travail sur le CRM ? Comment rattacher le CA d'un pilotage fait à distance ou chez le client ?
15. ACRE de chaque associé : éligibilité, dégressivité, effet d'une entrée au capital dans les deux ans.

### 19.2 À l'avocat en droit des sociétés (avant la signature des statuts)

1. Statuts d'une SAS à 50/50 : mécanismes contre le blocage, clause d'exclusion, inaliénabilité, agrément, préemption.
2. Pouvoirs du président et du DG envers les tiers ; inopposabilité des limites internes (art. L227-6 C. com.) ; comment rendre visible au client la règle de double accord ?
3. Pacte : validité et exécution de l'offre alternative, des clauses de départ et de non-concurrence d'associé ; articulation avec l'art. 1843-4 C. civ.
4. Rémunération différenciée selon le temps : organe compétent, plafond au pacte ; apport en industrie utile ou non ?
5. Reprise des actes : ordre des signatures (bon de commande, statuts, dépôt du capital) ; rédaction de l'état des actes ou d'un mandat pour un acte précis.
6. Licence ou cession du CRM et des outils des associés à Marwin : convention avec un dirigeant (art. L227-10 C. com.) ?
7. Entrée future de GianLuca : instruments, conventions réglementées, effets sur l'IS à 15 %, l'option IR, l'ACRE et le plafond de minimis.
8. Retrait de Medhi et de BOJ.ART : faut-il formaliser la décision avec Mathys et Medhi ? Comment marquer les documents déjà diffusés ?

### 19.3 À l'avocat en droit du travail (avant tout bureau ou emploi)

1. Le contrat-cadre et le mode de commande écartent-ils assez la subordination (art. L8221-6 II C. trav.) ? Quels indices supprimer ?
2. Une convention de bureaux est-elle un bail ? Quelles obligations d'assurance ?
3. Un associé salarié chez une entité de GianLuca : à quelles conditions (fonctions, propriété intellectuelle, loyauté, conflit d'intérêts, ARCE) ?
4. Critères du prêt de main-d'œuvre appliqués à une prestation intellectuelle et à la coordination de Quali Contact.

### 19.4 À l'avocat en contrats, propriété intellectuelle et numérique (avant le premier bon de commande)

1. Chaîne des droits sur le CRM (Morgan, Mathys, agents IA) puis vers Marwin et le client ; protection du code généré par IA ; conditions des outils d'IA sur la propriété des sorties.
2. Régime de Jarvis : composants, licences tierces, nom.
3. Cession par livrable et licence sur les composants génériques : rédaction conforme à l'art. L131-3 CPI.
4. Plafond de responsabilité, exclusions, obligation de moyens ou de résultat ; contrat négocié ou d'adhésion.
5. La règle de rétractation des petites entreprises (art. L221-3 C. consom.) vise-t-elle le contrat de Marwin ?
6. Préavis et rupture brutale dans les deux sens, y compris la nouvelle règle sur la baisse des volumes.
7. Marwin est-elle un « fournisseur de services de traitement de données » au sens du Data Act ?
8. Droits sur les films et images : artistes montrés, invités filmés, contenus générés par IA.

### 19.5 Questions que GianLuca pose à ses propres conseils (à lui transmettre comme ordre du jour, sans les traiter)

1. Quelle entité vend les œuvres, organise les événements, exploite chaque lieu ?
2. Statut de son entité dans chaque vente (acheteur-revendeur, commissionnaire, mandataire) et régime de TVA œuvre par œuvre.
3. Registre, dispositif de lutte contre le blanchiment, déclaration de diffuseur : existent-ils pour l'activité parisienne ?
4. Exposition d'une œuvre achetée par une entreprise dans sa galerie : rescrit ou avis avant toute prospection.
5. Pièces faites à la machine : rescrit sur une pièce précise.
6. « Enchères » pendant une soirée : opérateur habilité obligatoire ?
7. Son entité récupère-t-elle la TVA ? Peut-elle recevoir des factures électroniques ? Veut-elle déposer une demande d'aide au conseil **avant** de signer ?

### 19.6 À d'autres interlocuteurs

| Interlocuteur | Question |
| --- | --- |
| Assureur ou courtier | RC professionnelle couvrant pilotage, développement, IA et données ; exclusions cyber et IA ; traitement de l'incident connu ; prévoyance et homme-clé |
| Urssaf | Délai d'obtention d'une attestation de vigilance pour une société nouvelle ; ACRE d'un dirigeant de société |
| France Travail | Droits de chacun ; maintien de l'ARE pour un président de SAS non rémunéré ; ARCE en cas de salariat |
| Banque | Dépôt du capital, délai de déblocage, compte professionnel |
| Mairie et commission de sécurité (par l'entité de GianLuca) | Classement des bâtiments ; demande GN 6 ; débit temporaire |
| Intégrateur robotique (si un projet revient) | Statut du bras (machine ou quasi-machine) ; analyse de risques avec public ; date de mise en service |

Les questions sur la fuite de données (rôles, notification, information des personnes) sont dans 01-synthese-direction.md et 12-gouvernance-contrat-sortie.md.

---

## 20. Limites

- **Aucune simulation officielle** : urssaf.fr inaccessible le 4 nov. ; le coefficient SAS vient d'une seule source secondaire ; le minimum TNS sans rémunération n'a pas pu être vérifié (`travaux/ver-R1-structures.md:39-40`).
- **Règles de 2027 inconnues** : lois de finances et de sécurité sociale en discussion [IN].
- **Articles non rouverts dans l'audit** : L227-6, L227-10 et L227-16 du Code de commerce (pouvoirs, conventions, exclusion en SAS), L223-29 (majorités en SARL), droit des marques pour « Jarvis ». Ce que j'en dis est [HY].
- **Sources officielles** : consultées le 4 nov. 2026 par les chercheurs et contrôleurs de l'audit, pas rouvertes par moi. Certaines n'ont été lues que par extraits ; les contrôles le signalent.
- **Faits du client** : aucune parole directe de GianLuca ; entités, lieux, effectifs, intentions sur l'emploi et le capital : [IN].
- **Faits des associés** : disponibilités, droits France Travail, situation fiscale, lieu de résidence, existence juridique d'OLSEN : [IN].
- **Corpus incomplet** : 169 conversations ChatGPT lues sur 219 ; des promesses peuvent exister hors des pièces.

---

## Annexe : sources officielles citées

Toutes ont été consultées le 4 nov. 2026 par l'audit. La colonne « Contrôle » renvoie au fichier qui les a vérifiées.

| Texte ou fiche | URL | Version ou date affichée | Contrôle |
| --- | --- | --- | --- |
| Protection sociale du dirigeant, F38152 | https://entreprendre.service-public.gouv.fr/vosdroits/F38152 | Vérifiée le 08/10/2026 | `travaux/ver-R1-structures.md:20` |
| SARL, F37411 | https://entreprendre.service-public.gouv.fr/vosdroits/F37411 | Vérifiée le 06/02/2026 | `travaux/ver-R1-structures.md:19, 27` |
| SAS, F37366 | https://entreprendre.service-public.gouv.fr/vosdroits/F37366 | Vérifiée le 06/02/2026 | `travaux/ver-R1-structures.md:19, 27` |
| Revenus du dirigeant, F36065 | https://entreprendre.service-public.gouv.fr/vosdroits/F36065 | Vérifiée le 26/04/2024 (en retard sur la règle des 10 %) | `travaux/ver-R1-structures.md:23` |
| Cass. civ. 2, 31 mai 2018, n° 17-17.518 | https://www.legifrance.gouv.fr/juri/id/JURITEXT000037042970/ | Publiée au Bulletin | `travaux/ver-R1-structures.md:19` |
| CGI, art. 219 (IS) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868562 | En vigueur depuis le 21/02/2026 | `travaux/ver-R1-structures.md:21` |
| CGI, art. 239 bis AB (option IR) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038586316 | En vigueur depuis le 01/01/2019 | `travaux/ver-R1-structures.md:24` |
| Prélèvements sociaux, F2329 | https://www.service-public.gouv.fr/particuliers/vosdroits/F2329 | Vérifiée le 30/06/2026 | `travaux/ver-R1-structures.md:22` |
| ACRE, F11677 | https://entreprendre.service-public.gouv.fr/vosdroits/F11677 | Vérifiée le 01/07/2026 | `travaux/ver-R1-structures.md:25` |
| ARE et création, F36613 | https://entreprendre.service-public.gouv.fr/vosdroits/F36613 | Vérifiée le 29/09/2026 | `travaux/ver-R1-structures.md:26` |
| Cession d'actions de SAS, F36022 | https://entreprendre.service-public.gouv.fr/vosdroits/F36022 | Vérifiée le 22/07/2026 | `travaux/ver-R1-structures.md:29` |
| Micro-entreprise, actualité A18813 | https://entreprendre.service-public.gouv.fr/actualites/A18813 | 26/02/2026 | `travaux/ver-R1-structures.md:30` |
| C. com., art. L210-6 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006222358 | En vigueur au 04/11/2026 | `travaux/ver-R1-structures.md:28` |
| Cass. com., 29 nov. 2023, n° 22-12.865 | https://www.legifrance.gouv.fr/juri/id/JURITEXT000048581424 | FS-B+R | `travaux/ver-R1-structures.md:28` |
| Cass. com., 18 juin 2025, n° 24-14.311 | https://www.legifrance.gouv.fr/juri/id/JURITEXT000051823267 | Publiée | `travaux/ver-R1-structures.md:28` |
| CGI, art. 238 bis AB | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868630 | En vigueur depuis le 21/02/2026 | `travaux/ver-R2-fiscal.md:26` |
| BOI-BIC-CHG-70-10 | https://bofip.impots.gouv.fr/bofip/1801-PGP.html/identifiant=BOI-BIC-CHG-70-10-20260415 | 15/04/2026 | `travaux/ver-R2-fiscal.md:27` |
| CGI, annexe III, art. 98 A | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006298775 | En vigueur depuis le 27/10/1995 | `travaux/ver-R2-fiscal.md:28` |
| BOI-TVA-SECT-90-10 | https://bofip.impots.gouv.fr/bofip/1279-PGP.html | 20/03/2024 | `travaux/ver-R2-fiscal.md:29` |
| Question écrite AN n° 22584 | https://www.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE22584 | JO du 12/01/2021 | `travaux/ver-R2-fiscal.md:29` |
| BOI-TVA-SECT-90-40 | https://bofip.impots.gouv.fr/bofip/1285-PGP.html/identifiant=BOI-TVA-SECT-90-40-20250514 | 14/05/2025 | `travaux/ver-R2-fiscal.md:30` |
| Mécénat d'entreprise, F22263 | https://entreprendre.service-public.gouv.fr/vosdroits/F22263 | Vérifiée le 20/07/2026 | `travaux/ver-R2-fiscal.md:27` |
| CGI, art. 44 quindecies A (FRR) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049130324/ | En vigueur depuis le 21/02/2026 | `travaux/ver-R2-fiscal.md:32` |
| BOI-BIC-CHAMP-80-10-75-20 (FRR) | https://bofip.impots.gouv.fr/doctrine/pgp/14772-PGP | 29/07/2026 | `travaux/ver-R2-fiscal.md:33` |
| Arrêté du 19 juin 2024 (zones FRR) | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000049746820/2026-10-20 | Version consolidée au 20/10/2026 | `travaux/ver-R2-fiscal.md:31` |
| LPF, art. L80 B (rescrit) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047620657 | En vigueur depuis le 29/07/2026 | `travaux/ver-R2-fiscal.md:29, 32` |
| CFE, F23547 | https://entreprendre.service-public.gouv.fr/vosdroits/F23547 | Vérifiée le 02/04/2026 | `travaux/ver-R2-fiscal.md:34` |
| CGI, art. 293 B (franchise) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045035275 | En vigueur depuis le 01/03/2025 | `travaux/ver-R2-fiscal.md:36` |
| Facture électronique, FAQ DGFiP | https://www.impots.gouv.fr/foire-aux-questions-japprofondis-la-facturation-electronique | 01/09/2026 | `travaux/ver-R2-fiscal.md:35` |
| C. com., art. L441-10 (délais) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038414392 | En vigueur depuis le 26/04/2019 | `travaux/ver-R2-fiscal.md:37` |
| C. trav., art. L8221-6 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044056617 | En vigueur depuis le 01/01/2023 | `travaux/ver-R3-travail-contrats.md:32` |
| Travail illégal, F31490 | https://entreprendre.service-public.gouv.fr/vosdroits/F31490 | Vérifiée le 03/07/2026 | `travaux/ver-R3-travail-contrats.md:33, 35` |
| C. trav., art. R8222-1 et D8222-5 (vigilance) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030422273 ; https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046078939 | En vigueur depuis le 01/05/2015 et le 01/01/2023 | `travaux/ver-R3-travail-contrats.md:35` |
| C. com., art. L442-1 (rupture brutale) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047381704 | En vigueur depuis le 20/08/2026 | `travaux/ver-R3-travail-contrats.md:39` |
| Actualité A18850 (loyauté du salarié) | https://entreprendre.service-public.gouv.fr/actualites/A18850 | 20/03/2026 | `travaux/ver-R3-travail-contrats.md:38` |
| Assurances de la société, F37365 | https://entreprendre.service-public.gouv.fr/vosdroits/F37365 | Vérifiée le 07/07/2026 | `travaux/ver-R3-travail-contrats.md:40` |
| C. civ., art. 1231-3 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032010127 | En vigueur depuis le 01/10/2016 | `travaux/ver-R3-travail-contrats.md:40` |
| CPI, art. L131-1 à L131-3 | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069414/LEGISCTA000006161639/ | L131-2 en vigueur depuis le 01/10/2016 | `travaux/ver-R3-travail-contrats.md:42` |
| CPI, art. L113-9 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000039279818 | En vigueur depuis le 01/01/2020 | `travaux/ver-R3-travail-contrats.md:42` |
| Règlement (UE) 2023/2854 (Data Act) | https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32023R2854 | Applicable depuis le 12/09/2025 | `travaux/ver-R3-travail-contrats.md:43` |
| C. pén., art. 321-7 (registre) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000023717783 | En vigueur depuis le 16/03/2011 | `travaux/ver-R5-art-lieux.md:33` |
| CMF, art. L561-2 (lutte contre le blanchiment) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033582023 | En vigueur depuis le 05/08/2026 | `travaux/ver-R5-art-lieux.md:34` |
| CPI, art. L122-8 (droit de suite) | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033688066 | En vigueur depuis le 24/12/2016 | `travaux/ver-R5-art-lieux.md:36` |
| Contribution des diffuseurs (urssaf.fr) | https://www.urssaf.fr/accueil/artiste-auteur-diffuseur/diffuseur-commercant-art/cotisation-contribution-sociale.html | Vérifiée le 26/01/2026 | `travaux/ver-R5-art-lieux.md:38` |
| Décret n° 81-255 (« Marcus ») | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000684875 | En vigueur au 04/11/2026 | `travaux/ver-R5-art-lieux.md:37` |
| C. consom., art. L221-3 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226882 | En vigueur depuis le 01/07/2016 | `travaux/ver-R5-art-lieux.md:39` |
| ERP, art. PE 2 | https://www.legifrance.gouv.fr/codes/id/LEGISCTA000020342841 | En vigueur depuis le 01/01/2026 | `travaux/ver-R5-art-lieux.md:40` |
| ERP, art. GN 6 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048310284 | En vigueur depuis le 04/11/2023 | `travaux/ver-R5-art-lieux.md:41` |
| Débits de boissons, F22379 | https://entreprendre.service-public.gouv.fr/vosdroits/F22379 | Vérifiée le 27/11/2025 | `travaux/ver-R5-art-lieux.md:52` |
| Règlement (UE) 2026/1744 (modifiant le règlement machines) | https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng | JO L du 24/07/2026 | `travaux/ver-R5-art-lieux.md:43` |
| Rectificatif de la directive (UE) 2024/2853 | https://eur-lex.europa.eu/eli/dir/2024/2853/corrigendum/2026-05-07/oj/eng | JO L du 07/05/2026 | `travaux/ver-R5-art-lieux.md:44` |
| ISO 10218-2:2025 | https://www.iso.org/standard/73934.html | Édition 2, 2025-02 | `travaux/ver-R5-art-lieux.md:50` |
