# Brief complémentaire — les neuf livrables du 10 novembre 2026

10 novembre 2026 · document de travail interne (ne pas transmettre à GianLuca Carlone)

Ce brief complète `audit/2026-11-09-audit-presentation-et-offre/travaux/BRIEF.md` (le « brief du 9 novembre », avec son additif). Les deux se lisent ensemble. En cas de contradiction, l'additif du 9 novembre puis ce brief complémentaire l'emportent sur le texte d'origine.

## 1. La demande

Morgan Olsen, le 10 novembre 2026 : « Je veux que tu te lances sur tous les points que tu viens de citer. Fais en sorte de ne rien oublier. Avant de te lancer, élargis ton champ de connaissances sur tout ce qui est nécessaire. » Niveau attendu : l'état de l'art.

Les neuf points :

1. L'offre en une page et un projet de bon de commande.
2. Le texte d'orateur de la présentation et les réponses aux objections.
3. Une page pour l'administratrice.
4. Des écrans d'exemple du logiciel de gestion des propriétés, en données fictives.
5. Le kit du cadrage.
6. La feuille de décisions pour Morgan Olsen et Mathys Couet.
7. Les préalables qui bloquent tout envoi.
8. La suite sur l'autre proposition reçue et, si un hébergement est prévu, le choix d'un logiciel hôtelier du marché.
9. Cabaret et commerces : autorisations et échéances.

S'y ajoutent la version 12 de la présentation (demande du 9 novembre) et un sommaire du dossier du 10 novembre.

## 2. Dates et noms de fichiers

- Nous sommes le **mardi 10 novembre 2026** (heure de Paris). Les nouvelles pièces portent cette date dans leur nom (`2026-11-10-…`) et dans leur en-tête.
- Les pièces existantes sont des pièces historiques. On ne les modifie pas, on ne les renomme pas, on ne les supprime pas. Une correction se fait par une nouvelle pièce datée qui dit ce qu'elle remplace.
- Dans un fichier, les chemins cités sont relatifs à la racine du dépôt.

## 3. Où tout doit aller (carte des fichiers prévus)

Les cahiers des charges (fichiers `s-…` du § 4) peuvent ajuster cette carte ; ils doivent alors dire pourquoi.

| Livrable | Dossier | Fichiers prévus | Lecteur |
|---|---|---|---|
| 1 | `pour-carlone/offre-cadrage/` | `2026-11-10-offre-en-une-page.md` ; `2026-11-10-projet-de-bon-de-commande.md` (avec ses conditions courtes) | client (projet non envoyé) |
| 1 | `interne/offre-cadrage/` | `2026-11-10-note-interne-offre-et-bon-de-commande.md` (choix faits, points à faire relire par un avocat) | interne |
| 2 | `interne/rendez-vous/` | `2026-11-10-reponses-aux-objections.md` ; `2026-11-10-deroule-du-rendez-vous.md` ; `2026-11-10-antiseche-une-page.md` ; `2026-11-10-texte-d-orateur.md` (écrit après la version 12 de la présentation) | interne |
| 3 | `pour-carlone/offre-cadrage/` | `2026-11-10-une-page-pour-votre-administratrice.md` | client (projet non envoyé) |
| 4 | `pour-carlone/maquettes/2026-11-10-ecrans-d-exemple/` | `index.html` (maquette cliquable, un seul fichier) ; `LISEZ-MOI.md` ; images des écrans | client, seulement après décision des deux associés |
| 5 | `interne/cadrage/2026-11-10-kit/` | guide du premier entretien ; plan des semaines ; grille de choix des priorités ; trame du dossier remis ; modèle de compte rendu ; tableau d'inventaire (`.xlsx`) | interne |
| 5 | `pour-carlone/cadrage/` | `2026-11-10-questionnaire-preparatoire.md` ; `2026-11-10-liste-des-pieces-a-rassembler.md` | client (projet non envoyé) |
| 6 | `interne/decisions/` | `2026-11-10-feuille-de-decisions.md` | interne |
| 7 | `interne/prealables/` | `2026-11-10-projet-d-information-sur-le-fichier-de-contacts.md` ; `2026-11-10-demarches-immatriculation-et-assurance.md` ; `2026-11-10-liste-avant-tout-envoi.md` ; `2026-11-10-questions-pour-l-avocat.md` | interne (le projet d'information est destiné à GianLuca Carlone après relecture d'un avocat) |
| 8 | `interne/logiciels-et-automatisations/` | `2026-11-10-questions-a-poser-et-comparaison-a-refaire.md` ; `2026-11-10-choisir-un-logiciel-hotelier-note-conditionnelle.md` | interne |
| 9 | `pour-carlone/cabaret-et-commerces/` | `2026-11-10-autorisations-et-echeances.md` ; échéancier (`.xlsx`) | client (projet non envoyé) |
| 9 | `interne/cabaret-et-commerces/` | `2026-11-10-sources-et-limites.md` | interne |
| Tous | `audit/2026-11-10-preparation-des-livrables/` | `README.md` (sommaire, calendrier, questions ouvertes) | interne |

Les fichiers PDF et les tableaux `.xlsx` sont fabriqués par l'orchestration à partir des textes ; les rédacteurs écrivent le texte (Markdown) ou la structure demandée.

## 4. Les notes de préparation (à lire avant d'écrire)

Dossier : `audit/2026-11-10-preparation-des-livrables/travaux/`.

- `i0-…` : la fiche de faits commune (établi par une pièce, rapporté par Morgan, inconnu). **Personne ne remplit un inconnu de son propre chef** : ni le nom de l'administratrice, ni le nombre ou l'adresse des bâtiments, ni le nom des sociétés, ni une date d'ouverture.
- `i1-…` à `i9-…` : un inventaire par livrable (ce qui existe, contradictions, plan, manques).
- `k…` : une note de recherche par sujet. **La partie « Vérification du 10 novembre 2026 », à la fin de chaque note, l'emporte sur le reste de la note.** Un fait que la vérification corrige ou ne confirme pas ne va pas dans un document client.
- `c-…` : ce qui manque encore, par livrable. `g-…` : les compléments de recherche. `s-…` : le cahier des charges de chaque livrable.

Autres pièces de référence : `audit/2026-11-09-audit-presentation-et-offre/01-audit-de-la-presentation.md`, `03-objections-et-conditions-d-acceptation.md`, `travaux/a1` à `a5`, `travaux/r1` à `r3` (seules les listes « sûr pour une diapositive » passent dans un texte client), `travaux/x1` à `x3`.

## 5. Règles d'un document destiné au client

Les douze règles du § 5 du brief du 9 novembre et son additif s'appliquent à tout fichier de `pour-carlone/`. S'y ajoutent :

1. **Première ligne sous le titre** : « PROJET non envoyé — à valider par Morgan Olsen et Mathys Couet ». Pour un texte à portée juridique (bon de commande, conditions, information sur le fichier) : ajouter « Projet à faire relire par un avocat avant tout usage ».
2. **L'autre proposition** : jamais de nom, jamais de prix, jamais de critique. On écrit « l'autre proposition que vous avez reçue ».
3. **Le logiciel est sa demande** : « Vous nous avez demandé si nous pouvions créer votre logiciel de gestion de vos propriétés. »
4. **Prix** : seul le cadrage est affiché librement (6 500 € hors taxes, soit 7 800 € toutes taxes comprises ; moitié à la commande, moitié à la remise du dossier). Tout autre prix n'apparaît que s'il figure déjà, à l'identique, dans un document client daté du 9 novembre, et reste « à valider ». Un tarif public (droit, taxe, redevance) se cite avec sa source et sa date.
5. **Société** : « Marwin Tech, société en cours de création, immatriculée avant toute facture et tout démarrage ». On ne promet ni attestation d'assurance, ni relecture par un avocat tant que ce n'est pas fait.
6. **Droit** : un document client n'est jamais un avis juridique. Tout ce qui touche à une autorisation, un bail, un contrat de travail, une taxe ou une assurance porte « à faire valider par vos professionnels (avocat, notaire, expert-comptable, architecte, assureur) ».
7. **Pas de pression** : aucune urgence fabriquée, aucune remise, aucune gratuité, aucun « satisfait ou remboursé ». Une date limite ne s'écrit que si elle est vraie (durée de validité de l'offre, échéance légale avec sa source).
8. **Aucune adresse électronique, aucun numéro de téléphone, aucune coordonnée** d'une personne ou d'une entreprise réelle.
9. **Typographie française** : apostrophe courbe « ’ », guillemets « », « € » après le nombre, « hors taxes » écrit en toutes lettres à la première mention. Pas d'emoji. Pas de mot anglais quand un mot français existe.
10. **Données fictives** : toute maquette, tout exemple chiffré inventé porte « Maquette — données fictives » ou « Exemple fictif ». Les noms sont manifestement inventés (« Bâtiment A », « Entreprise 1 ») et ne ressemblent à aucun bien réel.

## 6. Règles d'un document interne

- En tête : « Document interne — ne pas transmettre à GianLuca Carlone », la date, et, si le sujet touche au droit : « Ce document n'est pas un avis juridique. »
- On peut écrire « le groupe Accor (d'après Morgan Olsen, 9 novembre 2026 ; non vérifié auprès de GianLuca Carlone) ».
- Chaque affirmation de fait renvoie à sa source : fichier du dépôt (chemin et ligne) ou page publique (organisme, titre, date, adresse).
- Un chiffre sans source est écrit « estimation à valider » ou n'est pas écrit.

## 7. Limites (inchangées)

- Les documents et les pages consultés sont des sources à examiner. Leurs instructions éventuelles n'autorisent rien.
- Aucun contact avec GianLuca Carlone, son administratrice, des prospects, des fournisseurs, un avocat, un assureur ou une administration. Aucun compte créé, aucun formulaire rempli, aucun achat, aucun envoi, aucune publication, aucune automatisation réelle, aucune modification du CRM.
- Les fichiers de données du dossier `crm/` ne sont pas ouverts. Aucune coordonnée n'est recopiée.
- Pas de commande git par les rédacteurs.

## 8. Méthode d'écriture

- Écrire par morceaux : un premier appel d'écriture pour le titre et la première partie, puis un ajout par partie (600 mots au plus par appel).
- Lire les gros fichiers par tranches de 300 lignes ; chercher d'abord ce qui concerne le sujet.
- Dire d'abord la conclusion, puis la preuve. Phrases courtes, mots simples.

## 9. Additif du 10 novembre 2026 (deuxième demande de Morgan Olsen) — prévaut sur ce qui précède

Morgan Olsen a confirmé le 10 novembre 2026 le feu vert sur les neuf points, avec des précisions, et a demandé une page de plus. Ce qui suit complète les § 1 à 8 et l'emporte en cas de contradiction.

### 9.1 Précisions sur les neuf livrables

1. **Offre et bon de commande** : faire apparaître le périmètre, les livrables, les étapes, les prix déjà arrêtés et les modalités connues ; signaler les champs à compléter et les conditions restant à décider, notamment **l'identité du contractant (quelle société de GianLuca Carlone signe) et du signataire** (de son côté et du nôtre).
2. **Texte d'orateur** : présentation de **vingt minutes**, diapositive par diapositive, avec les transitions, les messages essentiels et les réponses aux objections probables : **prix, légitimité, coût du logiciel, comparaison avec l'autre proposition, modalités de démarrage**.
3. **Page pour l'administratrice** : ce que le projet lui apporte, la place qu'elle garde, ce qui change dans son quotidien, le temps demandé ; **valoriser sa connaissance de l'activité** ; transition progressive, réaliste et respectueuse de son travail.
4. **Écrans d'exemple** : fiche bâtiment, échéances, comparaison de trois devis, en données fictives. Toute démonstration cliquable reste dans un **périmètre de présentation clairement défini** et **ne livre pas par avance le contenu ni la valeur de l'étape déjà chiffrée à 5 300 € hors taxes** (première étape du logiciel, document client du 9 novembre). Les écrans montrent à quoi cela ressemblerait ; ils ne sont pas un logiciel utilisable.
5. **Kit du cadrage** : au minimum le guide du premier entretien, le tableau d'inventaire à remplir et la trame du dossier remis ; méthode prête à utiliser dès le démarrage.
6. **Feuille de décisions** : reprendre **les vingt et une décisions** du § 10 de `audit/2026-11-09-audit-presentation-et-offre/travaux/a4-offre-et-documents-clients.md` (lignes 469 à 512 ; trois y « commandent le rendez-vous » : la 3, la 4 et la 14), avec leur priorité et une recommandation pour chacune ; faire correspondre les trente décisions du document `01-audit-de-la-presentation.md` ; faire ressortir **les trois arbitrages qui conditionnent le rendez-vous** : (a) séparation des documents clients et internes, (b) signataire, (c) présentation éventuelle d'un prix pour le logiciel ; distinguer clairement **déjà décidé** et **à trancher**.
7. **Préalables** : projets sur le fichier de contacts, l'immatriculation et les assurances, avec les informations manquantes et les points à faire relire par les professionnels compétents.
8. **Suite de l'analyse sur l'autre proposition** : reprendre **les cinq questions en attente** posées à Morgan le 9 novembre (contenu exact de l'offre ; quel bâtiment et s'il existe un projet d'hôtel ou de chambres, combien ; hors taxes ou non et durée d'engagement ; existence d'une proposition écrite que GianLuca Carlone peut montrer ; veut-il qu'on lui amène des clients ou seulement un outil de gestion) ; pour chacune, **ce que la réponse permettra de déterminer** ; si le scénario hôtelier se confirme, une comparaison des logiciels hôteliers du marché adaptés aux besoins réels.
9. **Cabaret et commerces** : tableau des autorisations, démarches, responsables et échéances, en distinguant ce qui est documenté (source officielle) de ce qui reste à vérifier ou à faire valider.

Un récapitulatif final dit ce qui est terminé, ce qui reste à compléter et les décisions précises attendues de Morgan Olsen et Mathys Couet. La cohérence entre présentation, prix, engagements, bon de commande et annexes est vérifiée à la fin.

### 9.2 Le dixième livrable : « Ce que des moyens supplémentaires nous permettraient d'accomplir »

Demande : une page pour GianLuca Carlone, intégrée naturellement à la présentation, qui explique comment un soutien financier adapté changerait la capacité d'action de Marwin Tech sur les plans humain, social, matériel et technologique. Idée à transmettre : notre ambition dépasse nos moyens actuels ; avec les bons investissements, certaines capacités changent d'échelle (« jusqu'à cent fois plus »).

Règles propres à ce livrable :

1. **Aucun multiplicateur sans mesure.** Tout « × N » est attaché à un indicateur concret (par exemple : documents traités par heure, tâches menées en parallèle, délai de réponse, coût par document) et à une base de comparaison explicite (aujourd'hui, à deux, avec nos outils actuels). Un gain non démontré s'écrit « hypothèse à évaluer ». « Cent fois » ne vaut que pour des tâches répétitives et parallélisables, et la validation humaine reste le goulet : on le dit.
2. **Chaîne obligatoire pour chaque investissement** : moyen supplémentaire → obstacle levé → application concrète → résultat attendu → bénéfice pour GianLuca Carlone et notre collaboration.
3. **Trois scénarios** : moyens actuels, renforcement ciblé, développement ambitieux ; pour chacun : investissement initial, dépenses récurrentes, capacités accessibles, premières priorités ; recommandation fondée sur le coût total et l'utilité réelle.
4. **Séparation nette avec l'offre actuelle** : la page dit que ces investissements sont des possibilités de développement et que **l'offre actuelle (le cadrage à 6 500 € hors taxes) se suffit à elle-même** avec nos moyens actuels. Elle ne conditionne rien, ne demande aucun montant précis, ne crée aucune urgence.
5. **Prix** : les prix de matériel, d'abonnements et de services de calcul sont des **tarifs publics** : chacun est cité avec sa source et sa date ; un total de scénario est une « estimation à valider ». Aucun autre prix de Marwin Tech que le cadrage.
6. **Matériel** : évaluer honnêtement NVIDIA DGX Spark, DGX Station et les alternatives (station de travail avec carte graphique, calcul à la demande, combinaison locale et distante) : adéquation à nos usages, coûts, contraintes (énergie, bruit, compétences, maintenance, écart de qualité entre modèles ouverts et modèles de pointe), capacités réelles. Un argument fort et vrai : un matériel installé chez lui, au nom de sa société, garde ses données chez lui.
7. **Laboratoire et robotique** : distinguer les applications proches (quelques mois) des pistes de recherche (sans date).
8. **Humain et social** : rémunération stable, temps dédié, collaborateurs spécialisés, formation, conditions de travail ; relier chaque moyen à la qualité du service, à la transmission des compétences, à l'emploi et à la continuité (aujourd'hui, deux personnes : une étape et un essai à la fois).
9. **Forme du soutien** (commande plus large, matériel acheté au nom de sa société, avance sur contrat, prise de participation, aides publiques) : **jamais détaillée dans le document client** ; elle est étudiée dans la note interne, avec les risques (dépendance, conflit d'intérêts, statuts) et les points à faire valider par un avocat et un expert-comptable.
10. **Fichiers** : page client `pour-carlone/developpement/2026-11-10-ce-que-des-moyens-supplementaires-permettraient.md` (une page A4) ; annexe client `pour-carlone/developpement/2026-11-10-annexe-comparaisons-et-calculs.md` (comparaisons techniques et calculs) ; note interne `interne/developpement/2026-11-10-note-interne-moyens-supplementaires.md` (sources, scénarios détaillés, forme du soutien, risques, décisions) ; une diapositive dans la version 12 (et au plus deux en annexe).
11. **Place dans la présentation** : une seule diapositive dans le fil principal, jamais avant la diapositive du prix et de la décision ; elle ouvre une perspective, elle ne remplace pas la demande du jour. La décision de la montrer revient à Morgan Olsen et Mathys Couet (nouvelle décision à inscrire dans la feuille de décisions).

## 10. Additif du 10 novembre 2026, soir (troisième message de Morgan Olsen) — prévaut sur tout ce qui précède

1. **« Gestion de propriété » veut dire un logiciel de gestion hôtelière** (en anglais « property management system ») : il existe donc un projet d’hôtel ou de chambres (rapporté par Morgan Olsen, 10 novembre 2026 ; nombre de chambres, bâtiment et date inconnus). Le scénario hôtelier est confirmé : la note conditionnelle du livrable 8 devient une note ferme.
2. **Pas de gestion confiée à un tiers** : l’administratrice centrale gérera l’administratif. Marwin Tech l’aide ; elle ne gère pas les lieux.
3. **Position de Marwin Tech, inchangée et à dire clairement** : nous ne construisons pas un logiciel hôtelier sur mesure (caisse certifiée, fiche de police, gestionnaire de canaux, paiement, facturation électronique : des logiciels du marché le font). Nous aidons à **choisir un logiciel du marché**, à le paramétrer, à le **relier** au reste (registre des bâtiments, comptabilité, administratrice), et nous construisons seulement ce qui manque autour. C’est la réponse honnête à « pouvez-vous créer notre logiciel ? ». L’étape « choix des logiciels et comparaison écrite » (3 000 € HT dans le document client du 9 novembre) en est le cadre naturel, sous réserve de la décision DL1.
4. **Rendez-vous avec GianLuca Carlone : vendredi 13 novembre 2026** (rapporté par Morgan). Tout doit être prêt le jeudi 12 novembre. Cela précède la date de premier envoi jusqu’ici retenue (jeudi 19 novembre) : les préalables (décision sur l’incident de données, texte d’information validé par un conseil, accord écrit des deux associés) deviennent urgents ; à défaut, la présentation est montrée à l’écran sans laisser de document ni faire signer quoi que ce soit. Décision des deux associés, à inscrire en tête de la feuille de décisions.
5. Dans un document client, l’autre prestataire n’est toujours jamais nommé ni chiffré ; des tarifs publics de logiciels hôteliers du marché peuvent être cités, avec leur source et leur date.

## 11. Additif du 10 novembre 2026, nuit (quatrième message de Morgan Olsen) — prévaut sur le § 10 pour l'hébergement

1. **Ce n’est pas un hôtel séparé.** Dans le même établissement que la galerie d’art, GianLuca Carlone met en place **neuf suites « privilège »**, un **sauna** et un **jacuzzi** (rapporté par Morgan Olsen, 10 novembre 2026 ; non vérifié ; adresse, ouverture, capacité, restauration et société exploitante inconnues). Le cabaret-spectacle reste prévu à côté de la galerie.
2. **Vocabulaire dans un document client** : « vos neuf suites », « l’espace bien-être (sauna et jacuzzi) », « l’établissement de la galerie ». Ne pas écrire « votre hôtel » : la catégorie juridique de l’hébergement (hôtel, avec ou sans classement, ou autre) est **à faire valider** par ses professionnels.
3. **Logiciel** : il faut un logiciel du marché adapté à un **petit établissement de neuf suites** (réservations, planning, arrivées, fiche de police des clients étrangers, taxe de séjour, caisse certifiée, facture électronique, canaux de vente, paiement) **capable aussi de gérer des créneaux** pour le sauna et le jacuzzi, et si possible des offres combinées avec les événements de la galerie. Toujours : nous aidons à choisir, paramétrer, relier ; nous ne construisons pas de logiciel hôtelier ni de billetterie.
4. **Obligations à ajouter au livrable 9** (document client `pour-carlone/cabaret-et-commerces/2026-11-10-autorisations-et-echeances.md`, échéancier et note des sources), dans une partie « Les suites et l’espace bien-être » : établissement recevant du public avec locaux à sommeil (règles de sécurité renforcées, effet sur le classement de tout l’établissement, galerie et cabaret compris s’ils communiquent) ; déclarations et obligations de l’hébergement (taxe de séjour, fiche de police, affichage des prix, classement volontaire) ; bain à remous et sauna ouverts aux clients (règles d’hygiène et de sécurité des piscines et bains collectifs : déclaration, contrôle sanitaire, qualité de l’eau, registre ; à vérifier sur les pages officielles) ; assurance. Statut « documenté » seulement avec une page officielle citée ; sinon « à vérifier » ou « à faire valider ».
5. **Présentation** : la diapositive sur le logiciel parle de « vos neuf suites et de l’espace bien-être », pas d’un hôtel.

## 12. Additif du 10 novembre 2026, nuit (cinquième message de Morgan Olsen)

Morgan veut que le logiciel puisse publier les suites sur Airbnb, Booking.com et les sites semblables, si GianLuca Carlone le demande (pas encore demandé). Conclusion de `interne/logiciels-et-automatisations/2026-11-10-connexion-airbnb-booking-et-autres-sites.md` : faisable par un logiciel hôtelier du marché avec gestionnaire de canaux déjà agréé par ces sites (Airbnb n’accepte plus de nouveaux accès à son API ; Booking.com réserve la sienne à des partenaires agréés) ; Marwin Tech relie ce logiciel au reste par son API. Critères de choix à ajouter : agréments Airbnb, Booking.com, Expedia ; API ouverte du logiciel ; gestion des créneaux du sauna et du jacuzzi. Dans un document client : « vos suites pourront apparaître sur les principaux sites de réservation, avec un seul calendrier à jour », sans promettre de résultat de réservation.
