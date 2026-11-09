# Audit stratégique Marwin Tech × GianLuca Carlone — 4 novembre 2026

Audit Marwin Tech × GianLuca Carlone · guide du dossier (hors des 15 livrables) · 4 novembre 2026
Statut : interne (contient des prix planchers, des rémunérations visées et la stratégie des associés ; ne pas transmettre à GianLuca Carlone)
Sources principales : `travaux/DEMANDE.md` ; `travaux/BRIEF-AGENTS.md` ; `travaux/strategie-retenue.md` ; `modele-financier/scenarios.md` ; `travaux/controle-modele.md` ; les 15 livrables de `interne/`, les deux projets de `pour-gianluca/` et `annexes/correction-identite.md`.
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu. JP : journée-personne de 7 h.

---

## 1. À quoi sert ce dossier, et pour qui

Morgan Olsen a demandé, le 4 novembre 2026, un audit complet de la collaboration entre Marwin Tech (Morgan Olsen et Mathys Couet, société **non immatriculée** [DR]) et leur client GianLuca Carlone, marchand d'art (`travaux/DEMANDE.md`). La question : comment devenir l'équipe de pilotage durable de ses projets, avec l'IA et les bons partenaires, en lui apportant une valeur mesurable et en construisant une entreprise rentable et indépendante.

Le dossier sert à **décider**, pas à vendre. Il s'adresse d'abord à **Morgan et Mathys**. Seuls les deux projets du dossier `pour-gianluca/` sont écrits pour GianLuca Carlone, et ils ne partent qu'après l'accord écrit des deux associés.

Date de référence de l'audit : **4 novembre 2026**, sur le dépôt `Momolscode/Carlone`, branche `main`, commit 7b46602 [FV]. Les fichiers du dossier ont été écrits et relus à partir de cette date ; la mise en cohérence finale (section 13) a été faite le 9 novembre 2026. À cette date, l'échéance CNIL du 5 novembre est passée : l'audit ne sait pas si la décision de notification a été prise [IN].

## 2. Verdict en trois lignes

1. **Oui à une collaboration avec GianLuca Carlone, non à l'offre actuelle** de six mois à 15 000 ou 30 000 € HT par mois : personne ne l'a demandée directement, aucune entité ne paie, et la formule de base prend 78 à 83 % du temps des deux associés [ES] (`travaux/strategie-retenue.md:41`).
2. **Une seule proposition : un cadrage au forfait de 6 500 € HT** (3 à 4 semaines, moitié à la commande), précédé d'une remise en ordre non facturée (fuite de données d'abord) et suivi, s'il est payé, d'un pilote de huit semaines dans la voie choisie par GianLuca [PR] (`travaux/strategie-retenue.md:42`).
3. **Un pilotage récurrent borné (10 JP facturables par mois au plus) vient au plus tôt au quatrième mois** ; on reporte sans travail gratuit si aucune entité n'est nommée au 15 décembre 2026 ou si le cadrage n'est pas payé au 31 janvier 2027 [PR] (`travaux/strategie-retenue.md:43-44`).

## 3. Comment lire

1. **Commencer par `interne/01-synthese-direction.md`** (deux pages) : verdict, objectif à 90 jours, 6 mois et 12 mois, cinq décisions prioritaires, chiffres clés.
2. Pour **agir cette semaine** : `interne/14-registre-risques-inconnues-decisions.md` (décisions et échéances) et `interne/08-feuille-de-route.md` (calendrier daté, jalons).
3. Pour **préparer le client** : `interne/11-proposition-commerciale-revisee.md`, `interne/13-preparation-rendez-vous.md`, puis les deux projets de `pour-gianluca/`.
4. Pour **vérifier un chiffre** : `interne/09-modele-economique-tresorerie.md`, puis `annexes/modele-financier/`.
5. Pour **douter** : `interne/15-contre-analyse.md`.

En cas de désaccord entre un livrable et `travaux/strategie-retenue.md`, le livrable le dit dans un encadré « Écart avec la stratégie retenue ». Pour les chiffres financiers, les livrables retiennent le **modèle** (`modele-financier/scenarios.md`), qui ajoute l'IS, la TVA et les délais d'encaissement aux calculs simplifiés de la stratégie.

## 4. Les livrables

| Fichier | Contenu | Statut |
| --- | --- | --- |
| `interne/01-synthese-direction.md` | Verdict, objectif recommandé, cinq décisions prioritaires, chiffres clés, conditions de validité | Interne |
| `interne/02-etat-des-sources.md` | Accès vérifiés, inventaire des pièces, 70 contradictions, inconnues numérotées U01 à U45 | Interne |
| `interne/03-cartographie-projets.md` | Fiches des onze chantiers, acheteurs réels, classement (finance Marwin, exploratoire, hors périmètre, gelé) | Interne |
| `interne/04-catalogue-offres.md` | Offres 0, A, B0 à B2, C1 à C8, D, E : périmètre, prix, coûts, marges, réception, sortie | Interne |
| `interne/05-proposition-de-valeur.md` | Valeur pour GianLuca, comparaison avec un salarié ou d'autres prestataires | Interne ; section 10 transmissible après accord écrit des deux associés |
| `interne/06-fonctionnement-a-deux.md` | Compétences, charge mensuelle, capacité réaliste, seuils de saturation | Interne |
| `interne/07-processus-ia-et-essais.md` | Onze processus IA, protocoles d'essai, coûts complets, grille de sécurité, restitution | Interne ; sections 6, 8 et 11 réutilisables en annexe contractuelle, après retrait des éléments internes |
| `interne/08-feuille-de-route.md` | 90 jours, 6 mois, 12 mois : livrables, indicateurs, budget, jalons datés, points de non-retour | Interne |
| `interne/09-modele-economique-tresorerie.md` | Scénarios, rémunérations, trésorerie sur 18 mois, tests de résistance | Interne |
| `interne/10-structures-et-relations.md` | SAS ou SARL, pacte, rôles de GianLuca (client, bailleur, employeur, investisseur), questions aux professionnels | Interne |
| `interne/11-proposition-commerciale-revisee.md` | Passage de l'offre du 2 nov. au cadrage, échelle de repli, objections, pièces à corriger | Interne |
| `interne/12-gouvernance-contrat-sortie.md` | Délégation, plafonds, silence, urgences, principes du contrat, réversibilité | Interne ; principes des sections 2 à 9 reprenables dans un document client |
| `interne/13-preparation-rendez-vous.md` | Prérequis, ordre du jour, questions, lignes rouges, déroulé | Interne |
| `interne/14-registre-risques-inconnues-decisions.md` | Risques, inconnues, 44 décisions suivies | Interne |
| `interne/15-contre-analyse.md` | Raisons d'échec, alternatives, conditions de refus | Interne |
| `pour-gianluca/proposition-de-cadrage.md` | Proposition de cadrage : livrables, exclusions, prix HT et TTC, paiement, suites possibles | **Destiné à GianLuca Carlone** ; projet non envoyé, note interne à retirer avant envoi |
| `pour-gianluca/message-de-recadrage.md` | Message d'une page, signé des deux associés | **Destiné à GianLuca Carlone** ; projet non envoyé, note interne à retirer avant envoi |
| `annexes/correction-identite.md` | Erreur de prénom dans les archives, pièces concernées, règles de citation | Interne |

Annexes de travail : `annexes/travaux/` (abrégé `travaux/` dans les livrables) et `annexes/modele-financier/` (abrégé `modele-financier/`). Elles sont internes.

## 5. Méthode et volume

| Phase | Ce qui a été fait | Où le trouver |
| --- | --- | --- |
| 1. Lecture des sources | Dix lectures thématiques des pièces du dépôt (contexte, offre, structure, méthodes, CRM, catalogue, Jarvis, créations, lieux, recueils ChatGPT), chacune contre-vérifiée par un contrôleur | `travaux/ex-C1-contexte.md` à `travaux/ex-C10-recueils.md` ; `travaux/ver-C1-contexte.md` à `travaux/ver-C10-recueils.md` |
| 2. Recherche officielle | Six mémos : structures, fiscalité, travail et contrats, données et IA, art et lieux, repères de marché ; environ 260 liens distincts, surtout Légifrance, service-public, BOFiP, EUR-Lex, CNIL, Urssaf, consultés le 4 nov. 2026 ; chacun contre-vérifié | `travaux/rj-R1-structures.md` à `travaux/rj-R6-marche.md` ; `travaux/ver-R1-structures.md` à `travaux/ver-R6-marche.md` |
| 3. Synthèses | Sources, portefeuille, capacité et IA, droit | `travaux/syn-sources.md`, `travaux/syn-portefeuille.md`, `travaux/syn-capacite-ia.md`, `travaux/syn-droit.md` |
| 4. Panel de stratégies | Trois stratégies concurrentes (progressive, pilotage, contradicteur), jugées par deux juges (angle client, angle Marwin), puis arbitrées | `travaux/strat-S1-progressif.md`, `travaux/strat-S2-pilotage.md`, `travaux/strat-S3-contradicteur.md` ; `travaux/juge-J1-client.md`, `travaux/juge-J2-marwin.md` ; `travaux/strategie-retenue.md` |
| 5. Calculs et modèle financier | Calculs refaits en Python ; modèle mensuel de trois scénarios, contrôlé ligne à ligne : cœur juste, six défauts corrigés, aucun chiffre principal changé | `travaux/calculs/` ; `modele-financier/modele_financier.py` ; `travaux/controle-modele.md` |
| 6. Rédaction et relecture | 15 livrables, 2 projets client, 1 annexe ; chaque fichier relu (ligne finale « Relu et contrôlé ») | `interne/`, `pour-gianluca/`, `annexes/correction-identite.md` |
| 7. Mise en cohérence finale | Comparaison des 18 fichiers entre eux et avec la stratégie et le modèle ; recherches automatiques de contrôle | Section 13 de ce fichier |

**Volume** [MM, comptage du 9 nov. 2026] : 46 fichiers de travail (≈ 343 000 mots) et 5 scripts de calcul ; un modèle de 1 984 lignes et 5 sorties ; 18 fichiers de livrables (≈ 176 000 mots). Les lignes « Relu et contrôlé » des 18 fichiers totalisent 538 vérifications et 168 corrections.

## 6. Conventions

- **Codes** sur chaque affirmation déterminante : [FV], [DR], [PR], [HY], [ES], [MM], [IN] (définis en tête de ce fichier). Sans autre précision, une [PR] est une proposition de `travaux/strategie-retenue.md`.
- **Chemins depuis la racine du dépôt** pour les pièces d'origine : `interne/contexte-projet-carlone.md:5`, `sources/propositions-de-collaboration.pdf p. 1`. Les PDF sont cités par page, jamais par leur texte extrait.
- **Travaux de l'audit** : `travaux/…` désigne `annexes/travaux/` ; `modele-financier/…` désigne `annexes/modele-financier/`. Les livrables se citent entre eux par leur nom de fichier (`08-feuille-de-route.md`).
- **Dans le modèle financier et dans certains fichiers de travail**, « audit-work/ » désigne le même dossier que `travaux/` (nom du dossier de travail au moment du calcul). `travaux/strategie-retenue.md` utilise en outre des abréviations qu'il définit lui-même (ligne 25).
- **Sources officielles** : URL et date de consultation (4 nov. 2026).
- **Chiffres** : fourchettes et arrondis ; aucun résultat du modèle n'est une prévision.

## 7. Accès vérifiés et limites

| Point | État | Effet sur l'audit |
| --- | --- | --- |
| Dépôt `Momolscode/Carlone` | Lu en entier, en lecture seule, commit 7b46602 [FV] | Base de l'audit ; rien n'y a été modifié hors du dossier `audit/` |
| Conversations ChatGPT | **169 lues sur 219** ; 50 non lues, certaines lues seulement sur les derniers échanges [FV] (`sources/reprise-59-et-visuels-2026-11-04.md:13-14`) | Des promesses faites au client peuvent exister hors du corpus [IN] |
| Dépôt `Momolscode/olsen-ai-intelligence` | **Non lu** : accès refusé (403) [FV] (`travaux/note-point-4-novembre-et-activites.md:22`) | Activité OLSEN connue seulement par déclaration |
| Dépôt `FinanceScope/CRM-Carlone` | **Visibilité non revérifiée** : accès refusé (403) ; dernier état documenté « public » le 4 nov. à 16 h 19 [DR] (`interne/contexte-projet-carlone.md:5`) | L'alerte sur la fuite repose sur ce dernier état |
| Gmail, Google Drive, Notion, Google Agenda | **Non interrogés** ; seule la page « Point du 4 novembre » est utilisée [DR] (`travaux/note-point-4-novembre-et-activites.md:3-10, 24`) | Rendez-vous, échanges récents et documents hors dépôt [IN] |
| Bibliothèque ChatGPT (visuels originaux) | Inaccessible [DR] | Certains visuels connus seulement par description |
| Parole de GianLuca Carlone | **Aucune pièce ne la contient** [FV négatif] (`travaux/syn-sources.md:38`) | Son besoin, ses priorités et sa solvabilité restent des hypothèses |
| Avis professionnels | **Aucun** : ni avocat, ni DPD, ni expert-comptable, ni assureur | Les points juridiques marqués [HY] et toutes les simulations sociales et fiscales sont à refaire par eux |
| Disponibilités des associés | Non documentées [IN] | Sans engagement écrit, seul le scénario prudent est défendable |

## 8. Correction d'identité

Le client s'appelle **GianLuca Carlone**. Les archives portent 433 fois un ancien prénom erroné, dans 28 fichiers [FV]. Ces pièces restent intactes. Dans les livrables, l'ancien prénom n'apparaît que dans 6 citations exactes, toutes suivies de [sic, lire GianLuca] ; les deux projets de `pour-gianluca/` n'en contiennent aucune. Les deux pièces client fautives (PDF des options du 30 oct., lettre du 29 oct.) ne sont jamais renvoyées. Détail et règles : `annexes/correction-identite.md`.

## 9. Ce que l'audit n'a pas fait

- **Aucun contact** avec GianLuca Carlone, Medhi, Quali Contact, un prospect ou un professionnel.
- **Aucun achat**, aucune dépense, aucun engagement.
- **Aucune modification du CRM** en service ni de ses données ; aucune modification du dépôt FinanceScope/CRM-Carlone (hors accès).
- **Aucune publication** et aucun envoi : les deux documents client sont des projets.
- **Aucune automatisation** activée ; les processus IA restent des protocoles d'essai.
- **Aucune décision** : tout ce qui est marqué [PR] attend l'accord écrit de Morgan et de Mathys.
- Les instructions trouvées dans les pièces lues ont été traitées comme des données, pas comme des ordres.

## 10. Pièces historiques et nouvelles versions

- **Pièces d'origine préservées** : rien n'a été réécrit dans le dépôt en dehors de `audit/`. L'offre écrite du 2 nov., STRATES v1.1, le diaporama du vernissage, le PDF de 13 diapositives de la PR n° 1 et le PDF des options du 30 oct. restent tels quels. La stratégie recommande de les marquer « historique, retiré le [date] » : c'est une action de Morgan, **pas encore faite** par l'audit (`travaux/strategie-retenue.md:802` ; 08-feuille-de-route.md, section 3.2, livrable 4).
- **Nouvelles versions datées** : `pour-gianluca/proposition-de-cadrage.md` et `pour-gianluca/message-de-recadrage.md` portent « Projet du 4 novembre 2026 — non envoyé ». Ils remplacent toutes les propositions antérieures.
- **Diaporama client de 11 vues** : non modifié par l'audit ; la liste des corrections est dans `travaux/strategie-retenue.md:814-828` et dans 11-proposition-commerciale-revisee.md, section 6.3.

## 11. Relancer le modèle financier

```
cd audit/2026-11-04-audit-strategique/annexes/modele-financier
python3 -I modele_financier.py                  # réécrit les 5 sorties à côté du script
python3 -I modele_financier.py --sortie DOSSIER # écrit ailleurs, pour comparer
```

- Python 3, bibliothèque standard seulement ; aucune action extérieure. Le script vérifie ses sommes, ses signes et l'identité de TVA, et s'arrête en cas d'écart.
- **Reproductibilité vérifiée** le 9 nov. 2026 (Python 3.13) : une exécution dans un dossier séparé redonne les 5 sorties identiques, octet pour octet [MM].
- Pour changer une hypothèse (prix, dates, disponibilités, frais, probabilités), modifier le paramètre en tête du script, relancer, puis reporter les chiffres dans les livrables qui les citent : 01, 08, 09, 14 et 15 surtout (`modele-financier/scenarios.md:20-23, 41, 45, 67`).
- Calculs de l'arbitre : `python3 -I annexes/travaux/calculs/arbitre-calc/verif.py` (affiche les résultats, n'écrit rien).
- À refaire avec l'expert-comptable en janvier 2027 : coefficient social, barèmes 2027, IS, TVA, date de clôture (`modele-financier/scenarios.md:227`).

## 12. Chiffres de référence du modèle (central) [ES]

| Indicateur | Valeur | Source |
| --- | --- | --- |
| CA facturé, mois 1 à 12 (prudent ; central ; ambitieux) | 49 500 ; 89 400 ; 141 100 € HT | `modele-financier/scenarios.md:41` |
| Net par associé et par mois, SAS, avant IR, à partir du mois 4 | ≈ 700 ; ≈ 1 300 (1 100 à 1 500) ; ≈ 1 900 € | `modele-financier/scenarios.md:21, 67` |
| Trésorerie disponible au mois 12 | 12 800 ; 27 000 ; 38 500 € | `modele-financier/scenarios.md:23` |
| Point bas (central) | 3 100 € en déc. 2026 ; 700 ou 100 € si la RC est payée d'avance | `modele-financier/tresorerie-18-mois.md:25, 135` |
| Contrat certain | 0 € dans tous les scénarios [FV négatif] | `modele-financier/scenarios.md:46` |

La stratégie annonçait 1 350 à 1 550 € nets en central et ≈ 150 000 € de CA en ambitieux ; les livrables retiennent le modèle (encadré de 01-synthese-direction.md).

## 13. Mise en cohérence finale (9 nov. 2026)

Les 18 fichiers ont été comparés entre eux, avec `travaux/strategie-retenue.md` et avec le modèle. Corrections faites :

| Incohérence | Correction | Fichiers |
| --- | --- | --- |
| Sortie à blanc datée tantôt au 4 mai 2027, tantôt en septembre 2027, tantôt « au mois 6 » | Une première sortie à blanc sur les outils du pilote avant le bilan du 4 mai 2027 (`travaux/strategie-retenue.md:169`) ; la sortie complète au 6e mois du socle, septembre 2027 en central (`travaux/strategie-retenue.md:281`) | 04, 05, 07, 08, 11, 12, 15 |
| Prix de la voie « pilotage » : « 3 500 à 6 500 € » pour le lot, ou 10 500 à 13 500 € au total, dans trois livrables, contre 2 700 à 6 400 € (9 700 à 13 400 €) dans deux autres | Fourchette corrigée partout (lot C1 ou C4) ; renvoi à l'encadré de 03-cartographie-projets.md, section 5.2 | 04, 05, 08 |
| Revenu central des associés donné à 1 350 à 1 550 € sans le chiffre du modèle | ≈ 1 300 € (1 100 à 1 500 €), chiffre du modèle, avec l'ancien chiffre signalé comme écart | 02, 13 |
| Travail non payé avant le premier euro : 12 à 22 JP ou 12 à 25 JP | 12 à 22 JP, 25 au plus si le plafond de démonstrateurs est atteint | 15 |
| Date butoir du 31 janv. lue « cadrage ou lot payé » | Cadrage commandé et acompte encaissé ; lot unique seulement dans le cas de l'écart n° 3 de 15 | 15 |
| Point bas de trésorerie sans sa sensibilité à l'assurance | Ajout du point bas de 700 ou 100 € | 08 |
| Abréviation « V5 » non définie | Définie, ou remplacée par le nom du fichier | 08, 11 |
| Marqueur [sic, lire GianLuca] placé dans les guillemets | Replacé après le guillemet fermant | 03 ; annexe mise à jour |
| Projets client numérotés « livrable 11 » et « livrable 13 » comme les livrables internes | Présentés comme projets rattachés aux livrables 11 et 13 | `pour-gianluca/` |

**Contrôles automatiques faits après correction** [MM] : aucune occurrence de l'ancien prénom hors citation suivie de [sic, lire GianLuca] ; aucun chemin local de machine ; aucune abréviation interne non définie ; dans `pour-gianluca/`, aucun montant interne et aucune occurrence de « 750 », « 15 000 », « 30 000 », « Medhi », « BOJ », « STRATES », « laboratoire » ou « fuite ».

**Principaux écarts maintenus**, signalés en encadré dans les livrables : capacité réaliste de 6, 10 ou 18 JP (06) ; capacité du cadrage et de B1 (04) ; réception du cadrage tolérée jusqu'au 31 mars 2027 (08) ; envoi du message de recadrage au plus tard le 27 nov. 2026 au lieu du 19 nov. (08) ; revenus et réserve du mois 12 (09) ; message de recadrage limité à quatre des sept points (`pour-gianluca/message-de-recadrage.md`) ; trois écarts de 15-contre-analyse.md. D'autres encadrés, plus limités, figurent dans 02, 03, 05, 06, 07, 10, 11, 12, 13 et 14. Chacun attend une décision de Morgan et de Mathys.
