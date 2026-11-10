# Livrable 7 — Les préalables qui bloquent tout envoi — inventaire avant rédaction

Note de travail interne du 10 novembre 2026

Document interne — ne pas transmettre à GianLuca Carlone. **Ce document n’est pas un avis juridique, fiscal ou d’assurance.** Il recense ce que le dépôt contient déjà. Il ne rédige pas le livrable. Aucun fichier de données du dossier `crm/` n’a été ouvert (ni `base.tsv`, ni les lots). Aucune coordonnée de personne ou d’entreprise n’est recopiée.

Conventions. Chemins relatifs à la racine du dépôt. Abréviations : **BRIEF** = `audit/2026-11-09-audit-presentation-et-offre/travaux/BRIEF.md` ; **BRIEF-2** = `audit/2026-11-10-preparation-des-livrables/travaux/BRIEF-2.md` ; **REG** = `audit/2026-11-04-audit-strategique/interne/14-registre-risques-inconnues-decisions.md` ; **SYN-DROIT** = `audit/2026-11-04-audit-strategique/annexes/travaux/syn-droit.md` ; **R4** = `audit/2026-11-04-audit-strategique/annexes/travaux/rj-R4-donnees-ia.md` ; **vR4** = `…/ver-R4-donnees-ia.md` ; **CONTEXTE** = `interne/contexte-projet-carlone.md` ; **AUDIT-2NOV** = `interne/audit-marwin-tech-carlone.md` ; **MAJ** = `audit/2026-11-04-audit-strategique/interne/2026-11-09-mise-a-jour-faits-nouveaux.md` ; **K1A**, **K2**, **K3**, **I0**, **I6** = notes du même nom dans `audit/2026-11-10-preparation-des-livrables/travaux/` ; **a1**, **a3** = notes du même nom dans `audit/2026-11-09-audit-presentation-et-offre/travaux/` ; **03-objections** = `audit/2026-11-09-audit-presentation-et-offre/03-objections-et-conditions-d-acceptation.md` ; **13-preparation** = `audit/2026-11-04-audit-strategique/interne/13-preparation-rendez-vous.md` ; **recadrage** = `audit/2026-11-04-audit-strategique/pour-gianluca/message-de-recadrage.md` ; **CADRAGE** = `audit/2026-11-04-audit-strategique/pour-gianluca/2026-11-09-proposition-de-cadrage.md` ; **LOGICIEL** = `pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md` ; **GARANTIES** = `pour-carlone/logiciels-et-automatisations/2026-11-09-logiciels-sur-mesure-methode-et-garanties.md`. `X:12` = fichier X, ligne 12.

Statuts repris des pièces : [FV] vérifié sur une pièce ; [DR] déclaration rapportée ; [HY] hypothèse ou lecture à faire valider ; [ES] estimation ; [IN] inconnu.

## 1. Ce qui existe déjà

**Conclusion.** La matière est abondante. K3 (note de recherche du 10 novembre) couvre presque tout le volet (a). K2 et K1A couvrent le volet (b). Le registre du 4 novembre fixe déjà les décisions, les responsables et les échéances. Ce qui manque n’est pas du droit : ce sont des faits que seuls Morgan Olsen et Mathys Couet détiennent (voir parties 6 et 7). K3 n’a pas de partie « Vérification du 10 novembre 2026 » (constat à la lecture : le fichier s’arrête ligne 211). Ses points restent donc à confirmer (BRIEF-2:59).

### 1.1 Chronologie établie de l’incident du fichier de contacts

Reconstituée strictement à partir des pièces. Aucune qualification juridique ici.

| Date | Ce que disent les pièces | Qui | Statut | Source |
|---|---|---|---|---|
| 22 oct. 2026 | « Invitation GitHub au dépôt FinanceScope/CRM-Carlone » ; mise en ligne du CRM en artefact avant un rendez-vous | Non précisé | [DR] (pièce de Morgan) | CONTEXTE:43 |
| 22 au 30 oct. 2026 | Constitution du fichier, « avant tout contrat » | « Morgan et/ou Mathys » ; compte « présenté comme celui de Mathys Couet » | [HY] pour le rôle | SYN-DROIT:597 ; K3:65 (renvoi à R4:130) |
| 22 oct. 2026 | Passation : « Page CRM republiée depuis le nouveau compte (privée) » ; dépôt « FinanceScope/CRM-Carlone » | Non précisé | [FV] (texte de la pièce) | `crm/PASSATION.md:3-4` |
| 29 oct. 2026 | Rapport CRM destiné à GianLuca Carlone. Il affirme : « Personne d’autre ne lit les fiches ni le suivi » | Auteurs du CRM | [FV] (texte) | `crm/docs/rapport/rapport-crm-hermes360.md:15`, cité par R4 (partie c, « Les faits connus ») et SYN-DROIT:628 |
| 29 oct. 2026 | Version autonome sur Firebase « sous le compte des associés » | Associés | [FV] (texte) | `crm/PASSATION.md:87` |
| 30 oct. 2026 | « Dernier envoi sur le dépôt du CRM » | Non précisé | [DR] | CONTEXTE:40 et :11 |
| 2 nov. 2026 | Audit daté « Nov 2, 2026 ». Ligne « Données — Urgent — Le dépôt GitHub du CRM est public et contient des coordonnées de prospects ». Solution n° 1 : « Passer le dépôt du CRM en privé […] — Morgan — Aujourd’hui — À faire » | Morgan (porteur de l’action) | [FV] (texte daté) | AUDIT-2NOV:3, :15, :27, :93 |
| 2 nov. 2026 | « L’analyse du 2 novembre y comptait 931 numéros de téléphone, 206 adresses e-mail, 63 fichiers de profils LinkedIn et le rapport destiné à Carlone » | Non précisé | [DR] | CONTEXTE:11 |
| 2 nov. 2026 | Date de connaissance retenue : « Au plus tard le 2 nov. » | — | [FV] sur la pièce datée | SYN-DROIT:620 ; vR4:21 |
| 4 nov. 2026, matin et 16 h 19 | « je l’ai revérifié ce matin, il est toujours visible de tous » ; « Vérifié le 4 novembre via l’API GitHub : “public” » ; « revérifié le 4 novembre à 16 h 19 » | Morgan (auteur de la pièce) | [DR] | CONTEXTE:5, :9, :11 |
| 4 nov. 2026, soir | L’audit stratégique ne peut pas revérifier : accès refusé (403). « Son état ce soir est [IN] » | Chercheurs de l’audit | [FV] (refus d’accès) | R4:15 ; `audit/2026-11-04-audit-strategique/README.md:91` |
| 5 nov. 2026, heure inconnue | Fin du délai de 72 heures **si** la connaissance date du 2 novembre | Responsable du traitement, « non désigné » | [ES] | SYN-DROIT:66, :623 ; REG:70 |
| 9 nov. 2026 | « l’échéance CNIL du 5 novembre est passée : l’audit ne sait pas si la décision de notification a été prise [IN] » | — | [IN] | `audit/2026-11-04-audit-strategique/README.md:18` ; MAJ:65 |
| 10 nov. 2026 | « Ce qui a été décidé depuis est inconnu » ; état du dépôt « aujourd’hui » inconnu | — | [IN] | K3:103 ; I0:177 |

**Ce qui est vérifié.** Les textes datés du dépôt : l’alerte du 2 novembre, la phrase du rapport du 29 octobre, l’existence d’une copie privée dans `crm/`. Le contenu de la copie `crm/` a été compté par l’audit : « 800 à 940 numéros selon la méthode de comptage, 206 e-mails, 86 à 89 profils LinkedIn, 740 mentions de dirigeants (468 fiches) », des lignes mobiles, des messageries grand public, 22 fiches de type « Artiste » (SYN-DROIT:619).

**Ce qui n’est pas vérifié.** Le caractère public du dépôt (déclaration de Morgan, jamais revérifiée par l’audit : SYN-DROIT:24 ; R4:15). Le contenu exact de la version publique (on suppose qu’il égale la copie `crm/`). Qui contrôle l’organisation FinanceScope (REG:176, U08 ; REG:272, D04 « Mathys, s’il contrôle l’organisation FinanceScope [IN] »). La date et l’heure exactes où chacun a su. L’existence de copies (forks), de clones, de secrets dans l’historique. Toute visite ou copie par un tiers. Le passage en privé, sa date, son auteur. La décision sur la notification (D03) et sur l’information des personnes (D08). Ce que GianLuca Carlone a reçu du CRM (copie, rapport, accès) : U04, REG:177.

### 1.2 Volet (a) — matière réutilisable pour l’information écrite à GianLuca Carlone

| Pièce | Ce qu’elle dit | Réutilisable tel quel ? |
|---|---|---|
| K3:123-133 | Plan d’une « note honnête » en huit rubriques : objet et date ; faits datés ; données concernées (« catégories et ordres de grandeur. Aucun nom, aucune coordonnée ») ; « Ce que nous ne savons pas » ; ce qui a été fait ; ce qui reste à faire ; ce que cela change pour lui ; un interlocuteur et la date du prochain point | **Oui**, comme plan du projet |
| K3:177-186 | Ordre : « fiche de violation et décision motivée ; relecture par un avocat ; information écrite à GianLuca Carlone ; puis remise en conformité ». En-tête : « Projet — non envoyé — à relire par un avocat ». Quatre phrases proposées : « Le fichier de contacts ne sera pas utilisé tant qu’il n’a pas été remis en conformité. » ; « À ce jour, nous ne savons pas si des tiers ont consulté ou copié ces données. » ; « Nous vous demandons de ne pas utiliser ni transmettre les copies que vous détenez. » ; « Nous faisons relire ce point par un avocat et revenons vers vous le [date]. » « Laisser en blanc, visiblement, ce qui est inconnu » | **Oui**, phrases candidates, sous réserve de l’avocat. L’en-tête est à aligner sur BRIEF-2:68 (voir partie 3) |
| K3:115-121 | Pourquoi informer : devoir de conseil du prestataire (Cass. com., 11 juillet 2006, n° 04-17.093) ; charge de la preuve sur le professionnel (Cass. 1re civ., 2 juillet 2014) ; information « déterminante pour le consentement » (code civil, art. 1112-1, non relu sur Légifrance) ; la phrase « Personne d’autre ne lit les fiches ni le suivi » « doit être corrigée par écrit » | Oui pour la note interne et les questions à l’avocat ; **jamais** dans le texte client (pas de droit cité) |
| K3:103-110 | Six mesures à noter « avec date, heure et auteur » : rendre le dépôt privé et le vérifier « depuis un navigateur non connecté » ; relever les statistiques (fenêtre GitHub de 14 jours) ; lister les copies ; « Révoquer d’abord les clés et jetons » ; recenser les autres copies ; « Écrire la décision motivée » | Oui, comme rubrique « ce qui a été fait / reste à faire » (cases vides tant que non fait) |
| K3:58-71 | Trois lectures du rôle de responsable, « Aucune n’est tranchée » ; le fait manquant : « qui a demandé le fichier, avec quelles consignes, et ce que GianLuca Carlone a reçu » | Oui pour les questions à l’avocat. Rien dans le texte client |
| SYN-DROIT:614-636 | Tableau de la violation (faits, données, date de connaissance, qui notifie, risque, remédiation, autres copies, contradiction, réforme non en vigueur) et cinq « Décisions immédiates », dont « 4. Informer GianLuca Carlone par écrit, puisque ses prospects et son rapport sont en cause » et « 5. Ne plus présenter le CRM comme confidentiel ; ne pas le “montrer en direct” » | Oui, base de la fiche de violation interne |
| SYN-DROIT:625 ; R4 partie (c), point 4 | Évaluation du risque : « Un risque paraît difficile à exclure (hameçonnage ciblé, sollicitations, atteinte à la réputation de GianLuca) ; un risque élevé est à examiner pour les artistes et les lignes personnelles » ; « ni données sensibles au sens de l’article 9, ni données bancaires connues » | Oui pour la fiche interne et l’avocat. Pas de qualification dans le texte client |
| REG:146 (R41) | Parade : « Information écrite, dans des termes validés par le conseil, sans reconnaissance de responsabilité non pesée ; aucune donnée réelle avant les préalables » ; échéance « Au plus tard avec le message de recadrage (ven. 27 nov.) » | **Oui, règle à reprendre mot pour mot** |
| REG:276 (D08) | « Information des personnes (art. 34) ; texte d’information de GianLuca » ; « Jeu. 19 nov. 2026 au plus tard » ; preuve : « Texte validé par écrit par le conseil » | Oui (échéance et preuve) |
| `audit/2026-11-09-audit-presentation-et-offre/travaux/a1-point-de-vue-gianluca.md:128-133` | Objection 8 : réponse « Vous avez reçu à ce sujet une information écrite, séparée de cette présentation. La remise en ordre est à notre charge, et ce fichier ne vous sera jamais refacturé. » ; « Le fond de l’explication vient de ce texte, pas d’une improvisation en séance » ; « Un sujet de confiance qu’il découvre seul devient un motif de refus » | La règle « séparée de la présentation » : oui. La promesse « à notre charge » et « jamais refacturé » : **à faire valider** (voir partie 3) |
| `audit/2026-11-09-audit-presentation-et-offre/03-objections-et-conditions-d-acceptation.md:162` | « L’information écrite sur le fichier lui reste due, qu’il dise oui ou non (D08). » | **Oui, principe à reprendre** |

### 1.3 Volet (b) — matière réutilisable pour les démarches d’immatriculation et d’assurance

| Pièce | Ce qu’elle dit | Réutilisable tel quel ? |
|---|---|---|
| K2:20-46 | Étapes de création d’une SAS (fiches Service Public F35934, F32886, F36703), pièces du dossier, bénéficiaires effectifs, capital entièrement libéré, coûts officiels 2026 (33,83 € ; 19,33 € ; annonce légale 199 € hors taxes), délais (« deux semaines en moyenne » selon l’INPI ; sources professionnelles discordantes) | Oui, avec les sources et dates de K2 |
| K2:126-142 | Tableau en trois cas (favorable, courant, défavorable) **si les statuts sont signés le lundi 16 novembre 2026** ; chemin critique ; « À qui demander quoi » | **Oui, base de la liste datée** (K2:151 le dit) — mais la date du 16 novembre est une hypothèse (partie 3) |
| K2:151 | Quatre échéances à ajouter : plateforme de réception des factures dès l’immatriculation ; attestation de l’Urssaf avant la signature du client ; cotisation foncière (1447-C-SD) avant le jeudi 31 décembre 2026 si immatriculation en 2026 ; ACRE dans les 60 jours | Oui |
| K2:80-92 | Assurances : RC professionnelle non obligatoire mais demandée ; activités à nommer ; garanties à vérifier ; exclusions ; primes publiées « de 200 € à plus de 2 000 € par an » (« annonces commerciales, pas des devis ») ; cyber ; souscription possible avec le récépissé avant le Kbis ; « l’incident de données connu se déclare à l’assureur avant la souscription » | Oui, avec la mention « prix d’appel » |
| K2:156-166 ; K2:168-174 | Ce qu’il ne faut pas écrire (« Marwin Tech SAS », Siret, « Nous sommes assurés », « TVA non applicable », nom « libre ») ; questions à l’avocat, à l’expert-comptable, à l’assureur, à France Travail, à la banque | **Oui**, presque mot pour mot |
| `audit/2026-11-04-audit-strategique/interne/10-structures-et-relations.md:374-416` | Section 10 : engagements avant immatriculation (art. L210-6 ; état des actes ; Cass. com. 18 juin 2025) ; « Rien n’est encaissé avant l’immatriculation » ; vigilance du client dès 5 000 € hors taxes (ligne 408) ; « Dès la création : Compte professionnel ; RC professionnelle ; plateforme de réception des factures électroniques ; comptes techniques au nom de Marwin » (ligne 416) | Oui |
| Même fichier, ligne 430 | RC professionnelle : « Avant la première prestation » ; « plafond assuré au moins égal au plafond contractuel » ; « déclaration sincère de la fuite » | **Oui** |
| REG:283-290 | D15 forme (« SAS à l’IS, président et directeur général, capital entièrement libéré », lundi 30 novembre) ; D16 statuts et pacte (prêts au 30 nov., pacte signé avant le premier bon de commande) ; D17 apport (8 000 à 14 000 €, 30 nov.) ; D19 RC pro (« Devis la semaine du 9 nov. ; souscription avant la première prestation ») ; D22 immatriculer (« au plus tôt début décembre […] fin décembre ou début janvier en central ») | Oui, comme colonne « décision » de la liste datée |
| REG:75 (R06) ; REG:200 (U43) | « Une assurance souscrite après coup ne couvre probablement pas un incident connu » ; « aucune couverture supposée pour cet incident » ; « Deux devis, fuite déclarée » | **Oui, mot pour mot** |
| CONTEXTE:12-13 ; AUDIT-2NOV:94-96 | Liste d’origine : immatriculer avant toute facture ; RC pro ; compte pro ; outil de facturation prêt pour la facture électronique | Historique. Forme « SARL par défaut » périmée (partie 3) |

### 1.4 Volet (c) — matière réutilisable pour la liste « avant tout envoi au client »

| Pièce | Ce qu’elle dit | Réutilisable tel quel ? |
|---|---|---|
| `audit/2026-11-09-audit-presentation-et-offre/03-objections-et-conditions-d-acceptation.md:218-262` | « Rien ne part aujourd’hui : ni présentation, ni proposition, ni message. » Treize préalables en trois blocs (« trois verrous », la société, les documents), avec état au 9 novembre, preuve attendue, échéance, source ; puis les décisions en attente | **Oui, c’est la meilleure base** : mettre à jour l’état au 10 novembre |
| `audit/2026-11-04-audit-strategique/interne/13-preparation-rendez-vous.md:67-84` | Huit prérequis avec « Preuve qu’il est rempli » ; règle : « Prérequis 1 à 7 manquants : on ne propose aucune date » | Oui (colonne « preuve ») |
| `audit/2026-11-04-audit-strategique/annexes/travaux/strategie-retenue.md:658-669` | « Conditions minimales pour démarrer un travail payé (toutes requises) » : dix conditions, dont « 10. Aucune donnée personnelle réelle avant la désignation du responsable du traitement, le contrat de l’article 28, le registre… » | Oui, comme seconde liste (« avant tout démarrage ») |
| `audit/2026-11-09-audit-presentation-et-offre/travaux/a3-exactitude-et-engagements.md:418-466` | « Rien ne part avant » (7.1), décisions (7.2), vérifications ouvertes (7.3), calendrier (7.5) : « Aucune version de la présentation ne se montre avant cette date » (19 novembre) | Oui |
| Même fichier, lignes 396-409 | Mots interdits, dont « 11. “immatriculée”, “assurée”, “relu par notre avocat”, avant que ce soit vrai et prouvé par une pièce » et « 12. “conforme” […] “vos données sont en sécurité chez nous” » | **Oui, contrôle de relecture** |
| `audit/2026-11-10-preparation-des-livrables/travaux/k1b-clauses-contrat-court.md:198` | À ajouter au livrable 7 : « cession écrite des droits de chaque associé à la société ; attestation d’assurance ; plateforme agréée ; accords de traitement des données avec les fournisseurs d’IA ; attestations de vigilance ; relecture du bon de commande par l’avocat » | Oui |
| BRIEF:55-68 ; BRIEF:94-98 ; BRIEF-2:64-77 | Les douze règles et l’additif ; les dix règles complémentaires d’un document client (première ligne « PROJET non envoyé — à valider par Morgan Olsen et Mathys Couet », mention avocat, aucune coordonnée, typographie) | Oui, comme dernière section de la liste (« contrôle du texte ») |
| `audit/2026-11-04-audit-strategique/interne/01-synthese-direction.md:68` ; MAJ:20 | « Rien ne part au client avant la décision 1 et l’accord écrit des associés » ; « Rien ne part au client, présentation comprise, avant D03, D08 et l’accord écrit des deux associés » | **Oui, phrase d’ouverture de la liste** |

## 2. Décisions prises et décisions ouvertes qui conditionnent ce livrable

**Déjà décidé (ne pas rouvrir).**

- « Rien ne part au client, présentation comprise, avant D03, D08 et l’accord écrit des deux associés » (MAJ:20 ; `audit/2026-11-04-audit-strategique/interne/01-synthese-direction.md:68`).
- Formules imposées : le fichier est « remis en conformité avant tout usage » (BRIEF:63) ; Marwin Tech est une « société en cours de création, immatriculée avant toute facture et tout démarrage » (BRIEF:64).
- L’information sur le fichier est un écrit **séparé** de la présentation et de la proposition (a1:130 ; `audit/2026-11-04-audit-strategique/interne/13-preparation-rendez-vous.md:72`). Elle est due « qu’il dise oui ou non » (03-objections:162).
- Gel de toute production non commandée (REG:273, D05). Aucune donnée réelle avant les préalables (REG:146).

**À trancher, par ordre d’urgence** (état au 10 novembre : inconnu pour toutes, I0:177).

| Décision | Objet | Échéance écrite | Effet sur le livrable 7 |
|---|---|---|---|
| D04 (REG:272) | Dépôt privé, copies, secrets | 5 nov., dépassée | Rubrique « ce qui a été fait » du projet (a) |
| D03 (REG:271) | Notifier ou non la CNIL, et comment | 5 nov., dépassée | Le projet (a) ne peut pas dire « nous avons informé l’autorité » sans elle |
| D08 (REG:276) | Information des personnes (art. 34) ; texte pour GianLuca Carlone | Jeudi 19 nov. | C’est le projet (a) lui-même |
| D45 (MAJ:375) | Qui a le lien de la présentation | Vendredi 13 nov. | Ligne de la liste (c) |
| D06, D07 (REG:274-275) | Une seule offre ; pièces marquées « historique » | Vendredi 13 nov. | Ligne de la liste (c) |
| D09 à D11 (REG:277-279) | Rôles, retrait de Medhi, accord de Mathys | Jeudi 19 nov. | Ligne de la liste (c) |
| Recadrage:69 | Écrit séparé envoyé le même jour que le message de recadrage, ou phrases dans le message | Avant le 19 nov. | Date d’envoi du projet (a) |
| D12 (REG:280 ; 03-objections:257) | À qui est le fichier | « Avant toute mention du fichier » | Le projet (a) ne dit pas à qui il appartient |
| D18 (REG:286) | CRM : hébergement privé, oppositions appliquées | Vendredi 20 nov. | Rubrique « reste à faire » du projet (a) |
| D14 (REG:282) | Envoi du recadrage et de la proposition | Signés le 19 nov., envoyés au plus tard le 27 nov. | Borne finale de la liste (c) |
| D15, D16, D17 (REG:283-285) | Forme, statuts et pacte, apport | Lundi 30 nov. | Point de départ de la liste datée (b) |
| D19 (REG:287) ; DL10 | RC professionnelle, fuite déclarée | Devis « semaine du 9 nov. » | Volet assurance de (b) |
| D21, D22 (REG:289-290) | Contrat relu ; date d’immatriculation | Avant le bon de commande ; « sous condition » | Volet (b) et liste (c) |
| Sans code (K3:190) | Qui consulte quel avocat, avec quel budget ; qui signe l’information ; qui relève aujourd’hui les statistiques du dépôt | Aucune | À inscrire dans la feuille de décisions (livrable 6) |
| Sans code (`10-structures-et-relations.md:35` ; K1A:15) | Signer le bon de commande « en formation » ou après l’immatriculation (lettre d’intention avant) | Aucune | Volet (b) et liste (c) |

## 3. Contradictions et écarts entre les pièces — version à retenir

1. **Volume des données.** « 931 numéros […] 206 adresses e-mail, 63 fichiers de profils LinkedIn » (CONTEXTE:11, analyse du 2 novembre, [DR]) ; « 800 à 940 numéros selon la méthode de comptage, 206 e-mails, 86 à 89 profils » (SYN-DROIT:619, compté sur la copie `crm/`, [FV]) ; « ≈ 800 à 931 » (REG:70). **À retenir** : SYN-DROIT:619, seul compte vérifié, en ordres de grandeur, avec la réserve « contenu de la version publique supposé identique, à confirmer ». « Fichiers » et « profils » ne mesurent pas la même chose.
2. **Début de la constitution du fichier.** « 22-30 oct. » (SYN-DROIT:597) ; mais une page CRM existait sur un « ancien compte », en « version 9 », avant le 22 octobre (`crm/PASSATION.md:3`, `:55`), et le dossier de Mathys du 21 octobre partait déjà du classement (CONTEXTE:44). **À retenir** : « constitué en octobre 2026 » ; date de début inconnue. Conséquence : la limite d’un mois de l’article 14 (K3:51, « entre le 22 et le 30 novembre ») pourrait tomber plus tôt.
3. **Échéance de l’information.** « Jeu. 19 nov. 2026 au plus tard » (D08, REG:276) ; « Au plus tard avec le message de recadrage (ven. 27 nov.) » (R41, REG:146) ; « Avant le message de recadrage, ou avec lui » (13-preparation:72). **À retenir** : texte validé par le conseil au 19 novembre ; envoi au plus tard avec le message de recadrage. Les deux dates se complètent.
4. **Où raconter l’incident.** Dans le message de recadrage (`strategie-retenue.md:809`) ou dans un écrit séparé (recadrage:59-69 ; 13-preparation:72). **À retenir** : écrit séparé, plus récent et motivé (« ne doit pas être mêlé à une proposition commerciale », recadrage:65).
5. **En-tête du projet.** « Projet — non envoyé — à relire par un avocat » (K3:178). **À retenir** : BRIEF-2:68, qui prévaut : « PROJET non envoyé — à valider par Morgan Olsen et Mathys Couet » puis « Projet à faire relire par un avocat avant tout usage ».
6. **Promesse de prise en charge.** « La remise en ordre est à notre charge, et ce fichier ne vous sera jamais refacturé » (a1:130 ; 03-objections:75) contre « sans reconnaissance de responsabilité non pesée » (REG:146 ; `strategie-retenue.md:809`). **À retenir** : aucune phrase sur la charge ou la responsabilité avant l’avis de l’avocat. Formule plus neutre déjà proposée : « Le fichier de contacts n’est pas compris dans cette commande. Il sera remis en conformité avant tout usage. » (K3:195).
7. **Forme de la société.** « SARL à l’IS par défaut » (CONTEXTE:12 ; AUDIT-2NOV:23, :94) contre « SAS à l’IS » à décider (REG:283). **À retenir** : « société en cours de création » ; SAS envisagée, à confirmer (I0:185).
8. **« En cours de constitution »** (CADRAGE:98 ; recadrage:49 ; GARANTIES:135) contre « en cours de création » (BRIEF:64). **À retenir** : BRIEF.
9. **Signer avant l’immatriculation.** Bon de commande « au nom et pour le compte de Marwin Tech, SAS en formation » (CADRAGE:98 ; `strategie-retenue.md:452`) contre « préférer la lettre d’intention […] et signer le bon de commande après l’immatriculation » (`10-structures-et-relations.md:35`) et « Le plus simple : signer après l’immatriculation » (K1A:15). **À retenir** : les deux voies, sans les fondre (I0:190) ; choix des associés après l’avocat. CADRAGE:173 est en outre ambigu (« par votre société, au nom de Marwin Tech »).
10. **Moment de l’assurance.** « Avant la première commande » (LOGICIEL:99) ; « Avant tout démarrage » (GARANTIES:110) ; « Avant l’immatriculation » (03-objections:236 ; DL10) ; « souscription avant la première prestation » (D19, REG:287). **À retenir** : devis tout de suite ; souscription avant la signature du bon de commande si les documents clients gardent leur promesse, sinon retirer la promesse partout (03-objections:236).
11. **Attestation de vigilance.** Promise (CADRAGE:174 ; GARANTIES:110) ; incertaine pour une société sans personnel (K2:140 ; a3:444) ; « Ne pas citer l’attestation de vigilance » (03-objections:88). **À retenir** : ne pas la promettre ; question à l’expert-comptable.
12. **Calendrier d’immatriculation.** Statuts « signés le lundi 16 novembre 2026 » (K2:126, hypothèse) ; statuts « prêts au 30 nov. » (D16) ; immatriculation déclenchée par un engagement écrit du client, « au plus tôt début décembre », « fin décembre ou début janvier en central » (D22, REG:290). **À retenir** : la liste (b) prend la date de signature des statuts comme variable. Les associés tranchent : signer tôt (K2) ou attendre l’engagement du client (D22).
13. **Oppositions.** « 13 entreprises » (`crm/PASSATION.md:51`) ; « 14 oppositions notées » (a3:123) ; vérification sur 32 fiches seulement (`crm/PASSATION.md:26`). **À retenir** : « vérification incomplète », sans nombre dans un texte client.
14. **Phrase du rapport du 29 octobre.** « Personne d’autre ne lit les fiches ni le suivi » (`crm/docs/rapport/rapport-crm-hermes360.md:15`) : fausse tant que le dépôt était public (SYN-DROIT:628). **À retenir** : la corriger par écrit dans le projet (a), si GianLuca Carlone a reçu ce rapport (inconnu, U04).

## 4. Règles et lignes rouges propres à ce livrable

1. **Rien n’est envoyé.** Le projet (a) reste un projet. Aucun contact avec GianLuca Carlone, un avocat, un assureur, la CNIL, l’Urssaf ou le greffe (BRIEF-2:89).
2. **Deux en-têtes.** Projet (a) : « PROJET non envoyé — à valider par Morgan Olsen et Mathys Couet » et « Projet à faire relire par un avocat avant tout usage » (BRIEF-2:68). Fichiers (b), (c) et questions : « Document interne — ne pas transmettre à GianLuca Carlone », la date, « Ce document n’est pas un avis juridique » (BRIEF-2:81).
3. **Projet (a) = texte client.** Vouvoiement, phrases courtes, aucun code ([FV], D03, U08…), aucun article de loi, aucun nom d’autre prestataire, aucune coordonnée, aucun nom de personne du fichier (BRIEF:57-60 ; BRIEF-2:75).
4. **Ne rien qualifier en droit** avant l’avocat : ni « violation », ni « fuite », ni « responsable du traitement » (K3:17). Les faits, datés ; l’inconnu, écrit comme inconnu ; les cases non faites, laissées vides et visibles (K3:185).
5. **Aucune reconnaissance de responsabilité non pesée** (REG:146 ; `strategie-retenue.md:809`). Aucune promesse de prise en charge ou de gratuité avant l’avocat (partie 3, n° 6). BRIEF-2:74 interdit aussi toute « gratuité » affichée.
6. **Ne jamais écrire avant la pièce** : « immatriculée », « assurée », « relu par notre avocat », « conforme », « vos données sont en sécurité chez nous » (a3:408-409) ; « Marwin Tech SAS », Siret, numéro de TVA, « Nous sommes assurés », « TVA non applicable », « le nom est libre » (K2:158-162).
7. **Pas d’urgence fabriquée** (BRIEF-2:74). Une échéance légale ne s’écrit qu’avec sa source ; les échéances internes (19 et 27 novembre) ne vont pas dans le texte client.
8. **Données.** Le fichier ne sert pas, n’est pas montré, n’est pas cité comme une référence (BRIEF:63 ; SYN-DROIT:636). La fiche de violation et l’évaluation de l’exposition des associés restent internes (`strategie-retenue.md:794`).
9. **Dates.** Montants et délais publics avec leur source et leur date (K2). Tarifs d’avocat, d’assurance ou de délégué à la protection des données : « annonces commerciales, pas des devis » (K2:86 ; K3:157).

## 5. Plan détaillé proposé

Quatre fichiers, comme prévu par BRIEF-2:45, dans `interne/prealables/`. Markdown. Aucun n’est envoyé.

**(a) `2026-11-10-projet-d-information-sur-le-fichier-de-contacts.md`** — projet destiné à GianLuca Carlone après relecture d’un avocat. Une page, 350 à 500 mots.

1. Les deux lignes d’en-tête (partie 4, n° 2).
2. Objet et date (« [date d’envoi] »).
3. Ce qui s’est passé, daté : constitution du fichier en octobre 2026 ; un dépôt de code qui le contenait était accessible au public ; dernier ajout le 30 octobre ; constaté au plus tard le 2 novembre ; encore accessible le 4 novembre ; rendu privé le « [date, heure — à remplir] ».
4. Les données concernées : catégories (entreprises, noms et fonctions de dirigeants, numéros, adresses électroniques, liens vers des profils en ligne, quelques fiches d’artistes) et ordres de grandeur. Aucun nom.
5. Ce que nous ne savons pas : visites, copies par des tiers, date de début exacte.
6. Ce qui a été fait (cases datées, vides si non faites).
7. Ce qui reste à faire, par qui, pour quand.
8. Ce que cela change pour vous : le fichier n’est pas utilisé ; demande de ne pas utiliser ni transmettre les copies détenues ; correction de la phrase du rapport du 29 octobre (si reçu).
9. Un interlocuteur, la date du prochain point. Signature des deux associés.
10. Hors texte, à détacher : tableau des sources de chaque phrase et liste des blancs.

**(b) `2026-11-10-demarches-immatriculation-et-assurance.md`** — interne. Deux à trois pages.

1. En bref : chemin critique ; trois cas de calendrier (K2:130-135), avec la date de signature des statuts en variable.
2. Décisions à prendre d’abord (D15 à D17, D22 ; liste K2:150).
3. Tableau daté : étape ; qui ; pièce ; coût officiel (source, date) ; cas favorable, courant, défavorable ; dépend de.
4. Actes avant l’immatriculation : état des actes, mandat (K2:48-56 ; `10-structures-et-relations.md:374-391`).
5. Après le Kbis : compte, TVA, plateforme de réception des factures, Urssaf, cotisation foncière avant le 31 décembre 2026, ACRE dans les 60 jours (K2:151).
6. Assurances : RC professionnelle, cyber ; garanties et exclusions à vérifier ; incident déclaré ; « aucune couverture supposée pour cet incident » (REG:75).
7. Ce qu’on ne peut pas écrire tant que ce n’est pas fait (K2:156-166).

**(c) `2026-11-10-liste-avant-tout-envoi.md`** — interne. Une à deux pages. Une ligne par contrôle : case ; preuve attendue ; qui ; échéance ; état au 10 novembre.

1. Phrase d’ouverture : MAJ:20.
2. Verrous : D04, D03, D08 et projet (a), accord écrit des deux associés.
3. Société : signataire, immatriculation, assurance, avocat, bon de commande et conditions, attestations (sans les promettre).
4. Documents : une seule version de l’offre ; pièces historiques marquées ; texte client séparé de toute note interne ; lien de la présentation (D45) ; déclaration du lien de Morgan avec BOJ.ART ; message à Medhi ; ce que GianLuca Carlone a vu (U04).
5. Données : aucune donnée réelle ; fichier hors du périmètre ; accord sur les données après l’immatriculation ; fournisseurs d’IA (k1b:198).
6. Contrôle du texte : règles de BRIEF:55-68, de l’additif et de BRIEF-2:64-77, mots interdits (a3:396-409).
7. Ordre d’envoi : projet (a) validé, puis message de recadrage et proposition, au plus tard le 27 novembre.

**(d) `2026-11-10-questions-pour-l-avocat.md`** — interne. Questions numérotées, regroupées : incident (rôles, notification tardive, article 34, article 14 pour un fichier non utilisé, formulation sans reconnaissance, copies chez le client) ; contrats (société en formation, rétractation, accord sur les données avant l’immatriculation, K1A et K5:152-155) ; assurance d’un incident connu ; questions reçues des autres livrables (i3:144 ; k7, partie « Questions à poser à un professionnel »).
