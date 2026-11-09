# Préparation du rendez-vous avec GianLuca Carlone

Audit Marwin Tech × GianLuca Carlone · livrable 13 sur 15 · 4 novembre 2026
Statut : interne (tactique du rendez-vous, échelle de prix, lignes rouges ; ne pas transmettre à GianLuca Carlone)
Sources principales : `travaux/strategie-retenue.md` (sections 1, 4.3, 4.4, 5.3, 5.4, 8.8, 9 à 14, 17) ; `travaux/syn-portefeuille.md` (sections 1.6, 2.3 et 5) ; `travaux/ex-C2-offre.md` (sections 3.1, 5 et 7) ; pièces d'origine du dépôt Momolscode/Carlone rouvertes en lecture seule (base de l'audit : commit 7b46602 ; ces fichiers n'ont pas changé depuis, vérifié par `git diff`) : `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md`, `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md`, `interne/contexte-projet-carlone.md`, `interne/offre-marwin-tech-remuneration-et-collaboration.md`, `interne/offres-de-carlone-catalogue-crm.md`, `interne/recueil-sessions-chatgpt-2026-11-04.txt`, `crm/PASSATION.md`, `crm/docs/rapport/rapport-crm-hermes360.md` ; pour-gianluca/message-de-recadrage.md ; pour-gianluca/proposition-de-cadrage.md ; 11-proposition-commerciale-revisee.md ; 12-gouvernance-contrat-sortie.md.
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu. Sauf mention, [PR] désigne une proposition de la stratégie retenue ; « [PR, ce livrable] » signale une précision ajoutée ici.

Conventions. JP : journée-personne de 7 h. Prix hors taxes (HT), avec le TTC entre parenthèses (TVA à 20 %). « Les dix questions bloquantes » sont celles de `travaux/strategie-retenue.md:723-737`. Les phrases entre guillemets dans les sections 6 et 8 sont des formulations proposées, à dire avec ses propres mots.

**Ce que ce livrable ajoute** : l'objectif et le résultat minimal du rendez-vous ; les prérequis avant d'en fixer la date ; l'ordre du jour minuté ; le partage des rôles ; les questions formulées pour être dites ; les pièces à apporter ou à laisser ; huit scénarios de réponses ; les lignes rouges propres à la séance ; la fiche à remplir avant de partir ; les suites à 48 heures. **Ce qu'il ne refait pas** : les prix, l'échelle de repli et les dix-neuf objections courantes (11-proposition-commerciale-revisee.md, sections 3 et 4.2) ; la liste complète des pièces à corriger (même livrable, section 6) ; le texte remis au client (pour-gianluca/proposition-de-cadrage.md et pour-gianluca/message-de-recadrage.md) ; les clauses (12-gouvernance-contrat-sortie.md) ; le calendrier d'ensemble (08-feuille-de-route.md) ; l'erreur de prénom (annexes/correction-identite.md).

---

## En bref

1. **Le rendez-vous sert à deux choses** : savoir quelle société de GianLuca achète, et obtenir une réponse claire sur un seul achat, le cadrage à 6 500 € HT (7 800 € TTC). Un « non » net est un résultat. Sortir sans savoir qui achète est un échec (section 1).
2. **On ne fixe la date qu'après huit prérequis** : fuite traitée, GianLuca informé de l'incident par écrit, documents corrigés, accord écrit de Mathys, message à Medhi, réponse de Morgan sur ce que GianLuca a vu, message de recadrage envoyé, statuts et contrat-cadre en préparation. Au 4 novembre, aucun n'est établi (section 2).
3. **90 minutes, les questions d'abord.** La proposition arrive vers la 60e minute. Les 30 dernières minutes sont réservées à l'entité, au cadrage et au récapitulatif (section 4).
4. **Morgan mène, Mathys est présent** (sur place ou à distance), note mot à mot et répond sur les données et les outils. Aucun prix ni aucune concession hors de ce qui a été convenu la veille à deux (section 5).
5. **Rien n'est signé pendant le rendez-vous.** Le document d'engagement part par écrit sous 48 heures, pour une signature à distance. Si la société compte 5 salariés au plus, aucun encaissement avant 7 jours [HY, à trancher par l'avocat] (sections 9 et 11).
6. **Huit scénarios sont préparés** (section 8). Règle commune : une phrase claire, la règle, puis retour à l'ordre du jour. Bureaux, emploi, capital et commission ne se négocient jamais en séance.
7. **Ce sera la première parole directe de GianLuca dans le dossier** : aucune pièce n'en contient [FV négatif] (`travaux/syn-portefeuille.md:88-90`). On la note mot à mot et on la lui fait confirmer par écrit sous 24 heures (sections 10 et 11).

---

## 1. Objectif du rendez-vous et résultat minimal

### 1.1 Ce qui change par rapport à la préparation du 4 novembre

| | Préparation des archives | Préparation retenue [PR] |
| --- | --- | --- |
| Objectif écrit | « Le rendez-vous doit rapporter quatre réponses : la formule, l'entité qui signe et paie, la date de démarrage et celle de l'acompte » [FV] (`interne/contexte-projet-carlone.md:102`) | Comprendre le besoin de la bouche de GianLuca ; savoir qui achète ; lui proposer un seul achat, le cadrage |
| Ce qu'on vend | La formule de six mois, à 15 000 ou 30 000 € HT par mois [FV] (`interne/offre-marwin-tech-remuneration-et-collaboration.md:13-16`) | Le cadrage de 3 à 4 semaines (`travaux/strategie-retenue.md:42, 197`) |
| Conclusion visée | « Conclure sur la décision attendue aujourd'hui : la formule, l'entité qui signe et la date de démarrage » (note de l'orateur du diaporama, `slides/etapes.html:29`, citée en entier dans 02-etat-des-sources.md et en extrait dans `travaux/ex-C2-offre.md:296`) | Une réponse sur le cadrage et une date pour l'engagement écrit, sans signature en séance |
| Ordre | Présenter l'offre, puis montrer le CRM en direct (`travaux/ex-C2-offre.md:296`) | Questions d'abord, proposition ensuite ; aucune démonstration du CRM |

Pourquoi ce changement : l'offre est née du côté de Marwin, pas d'une demande du client (`travaux/syn-portefeuille.md:156-162`) ; aucune société payeuse n'est nommée [FV négatif] (`travaux/syn-portefeuille.md:101-102`) ; les « vingt jours par mois » sont attribués tantôt à GianLuca (`sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:65`), tantôt à Morgan (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:7`) [DR contradictoire].

### 1.2 Trois niveaux de résultat [PR, ce livrable]

| Niveau | Ce qu'on rapporte | Ce que cela déclenche |
| --- | --- | --- |
| **Minimal** (le rendez-vous a servi) | 1. La société qui signerait, au moins son nom, ou une date ferme pour la nommer, au plus tard le vendredi 11 décembre 2026. 2. Sa réponse au cadrage : oui, version réduite, un seul sujet, ou non. 3. Un interlocuteur et un canal d'échange | Récapitulatif écrit sous 24 h ; si « oui », document d'engagement sous 48 h (section 11) |
| **Attendu** | En plus : SIREN, signataire habilité, effectif, payeur et valideur ; ses trois priorités dans ses mots ; ses habitudes de paiement et la récupération de la TVA ; son intérêt pour l'aide régionale ; une date pour l'entretien de cadrage en janvier | Consultation des registres publics ; immatriculation dès l'engagement écrit (`travaux/strategie-retenue.md:552`) |
| **Hors objectif** (ne pas le chercher) | Une signature, un acompte, le détail des lieux, des budgets ou des accès ; toute discussion sur les bureaux, l'emploi ou le capital | Ce détail est le travail payé du cadrage (`travaux/strategie-retenue.md:225`) ; le reste attend le bilan du mois 6 (`travaux/strategie-retenue.md:629-632`) |

**Un « non » est un résultat.** « Un refus de payer un cadrage est déjà une réponse » (`travaux/strategie-retenue.md:694`). Il confirme ou infirme l'hypothèse d'un besoin de pilotage (`travaux/syn-portefeuille.md:240-250`).

**Le rendez-vous est un échec** si l'on repart sans savoir qui achète ni ce qu'il pense du cadrage, ou après avoir promis quelque chose de la section 9.

### 1.3 Dates qui encadrent le rendez-vous

| Date | Ce qui doit être vrai | Source |
| --- | --- | --- |
| Jeu. 19 nov. 2026 | Message de recadrage et proposition signés par les deux associés | `travaux/strategie-retenue.md:716` ; pour-gianluca/message-de-recadrage.md, note interne |
| Ven. 27 nov. 2026 | Message envoyé au plus tard | 08-feuille-de-route.md, section 6.1, semaine 4 |
| Lun. 30 nov. au mar. 15 déc. 2026 | Fenêtre du rendez-vous dans le scénario central (semaines 5 à 7, bornées par le jalon du 15 déc.) ; engagement écrit visé le ven. 11 déc. | 08-feuille-de-route.md, section 6.1, semaines 5 à 7 |
| Mar. 15 déc. 2026 | Sans société nommée ni rendez-vous tenu : report à janvier, sans production | `travaux/strategie-retenue.md:697` |
| 31 janv. 2027 (un dimanche : en pratique ven. 29 janv.) | Cadrage non commandé et payé : report sans date | `travaux/strategie-retenue.md:698` |

---

## 2. Prérequis avant de fixer le rendez-vous

### 2.1 Les huit prérequis

| N° | Prérequis | Preuve qu'il est rempli | État au 4 nov. 2026 | Échéance | Responsable | Base |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **Fuite traitée** | Dépôt privé vérifié ; copies contrôlées ; fiche de violation ; décision de notification documentée avec un avocat ou un DPD ; décision sur l'information des personnes ; aucune donnée réelle utilisée | Dépôt public au dernier état documenté, le 4 nov. à 16 h 19 [DR] (`travaux/note-point-4-novembre-et-activites.md:23` ; `interne/contexte-projet-carlone.md:5, 11`). Décision [IN] | Décision avant l'échéance du 5 nov. | Mathys et Morgan | `travaux/strategie-retenue.md:660, 715` |
| 2 | **GianLuca informé de l'incident par écrit**, dans des termes validés par le conseil | Message envoyé, texte validé daté | Aucun texte connu de l'audit [IN]. Choix d'un message séparé du recadrage (pour-gianluca/message-de-recadrage.md, encadré) | Avant le message de recadrage, ou avec lui | Morgan ; validation par l'avocat ou le DPD | `travaux/strategie-retenue.md:660, 794, 809` |
| 3 | **Documents corrigés** | Une seule version de l'offre ; anciennes pièces marquées « historique » ; aucune mention de formule, de taux, de Medhi, de STRATES ou du laboratoire dans ce qui sera remis, sauf la déclaration du lien de Morgan avec BOJ.ART (11-proposition-commerciale-revisee.md, section 5.2, encadré n° 2) | Les 11 vues du diaporama sont à corriger [FV] (11-proposition-commerciale-revisee.md, section 6.3) ; le PDF de 13 vues reste sur la branche de la PR n° 1 [FV] (`travaux/syn-portefeuille.md:77`) | Ven. 13 nov. | Morgan ; contrôle Mathys | `travaux/strategie-retenue.md:661, 716` |
| 4 | **Accord écrit de Mathys** : stratégie, retrait de Medhi, SAS, régime du CRM ; disponibilités nominatives d'au moins 6 JP facturables par mois à deux ; échelle de prix validée | Fiche « rôles et disponibilités » signée | La décision du 4 nov. est orale, non formalisée avec Mathys [DR] (`travaux/note-point-4-novembre-et-activites.md:25`) ; disponibilités [IN] | Jeu. 19 nov. | Les deux | `travaux/strategie-retenue.md:662, 717` |
| 5 | **Message écrit à Medhi** sur la portée du retrait | Message envoyé | [IN] | Jeu. 19 nov. | Morgan | `travaux/strategie-retenue.md:211` (point 4) ; 08-feuille-de-route.md, semaine 3 |
| 6 | **Réponse de Morgan à la question n° 9** : ce que GianLuca a vu, reçu ou accepté | Liste écrite, datée | [IN] (`travaux/ex-C2-offre.md:221, 278`) | Avant l'envoi du message | Morgan | `travaux/strategie-retenue.md:736` |
| 7 | **Message de recadrage et proposition de cadrage envoyés**, avec la déclaration du lien de Morgan avec BOJ.ART | Envoi daté, signé des deux | Projets non envoyés [FV] (pour-gianluca/message-de-recadrage.md) | Signés le 19 nov., envoyés au plus tard le 27 nov. | Morgan, validé par Mathys | `travaux/strategie-retenue.md:58, 804-812` |
| 8 | **Statuts et pacte prêts, non signés ; contrat-cadre en relecture chez l'avocat** ; question de la rétractation posée | Projets datés ; demande à l'avocat envoyée | [IN] | Lun. 30 nov. | Les deux, avec l'avocat | `travaux/strategie-retenue.md:451, 552` ; 12-gouvernance-contrat-sortie.md, section 11.6 |

### 2.2 Règle de décision [PR, ce livrable]

- **Prérequis 1 à 7 manquants** : on ne propose aucune date. La raison tient en une ligne : on ne présente pas une offre qui contredit nos propres documents, ni une offre que l'un des associés n'a pas approuvée (`travaux/strategie-retenue.md:614`).
- **Seul le prérequis 8 manque** : le rendez-vous peut avoir lieu, mais l'engagement écrit attendra la relecture du contrat-cadre. Cela peut décaler le démarrage de quelques jours [HY].
- **Les prérequis 5 et 6 conditionnent le message** (prérequis 7). GianLuca « connaît BOJ.ART » et aurait racheté « l'ancienne affaire de Medhi » [DR] (`interne/contexte-projet-carlone.md:24`) : il ne doit pas apprendre le retrait par la conversation.

### 2.3 Si GianLuca appelle avant que tout soit prêt

C'est possible : il traite avec Morgan en direct [DR], et aucun rendez-vous n'est fixé (`travaux/note-point-4-novembre-et-activites.md:5`). Réponse préparée [PR, ce livrable] :

> « Merci de votre appel. Nous avons revu notre proposition pour partir de vos priorités. Vous la recevrez par écrit d'ici [date au plus tard le 27 novembre]. Pouvons-nous fixer un rendez-vous juste après, pour en parler sur pièces ? »

Pendant cet appel : aucun prix, aucune formule, aucun commentaire sur l'incident hors du texte validé, aucune promesse de travail. S'il demande un service urgent, on note la demande et on répond par écrit, à deux.

---

## 3. Format, lieu et préparation

| Point | Recommandation [PR, ce livrable] | Pourquoi | Limite |
| --- | --- | --- | --- |
| Durée | 90 minutes ; variante de 60 minutes (section 4.3) | Le message de recadrage propose « une heure à une heure et demie » (pour-gianluca/message-de-recadrage.md) | S'il dispose de moins de 45 minutes, on ne présente pas le cadrage : on fixe un second rendez-vous |
| Lieu | À sa préférence : chez lui ou à distance | Sur place, la relation y gagne [HY]. À distance, pas de trajet, et la question du contrat « hors établissement » se pose moins [HY] (12-gouvernance-contrat-sortie.md, section 11.6, encadré) | Lieu de résidence des associés inconnu, donc coût des trajets inconnu [IN] (`travaux/strategie-retenue.md:233`) |
| Participants côté client | GianLuca ; et, pour les 30 dernières minutes, la personne qui travaillerait avec nous au quotidien, s'il en a une | Le message lui demande déjà de penser à cette personne (pour-gianluca/message-de-recadrage.md, point 3) | Elle peut ne pas exister encore [IN] |
| Participants côté Marwin | Morgan et Mathys | Section 5 | Mathys indisponible : section 5.3 |
| Enregistrement | Aucun. Aucun outil d'IA de transcription sur ses propos | Données personnelles ; transferts hors Union vers des fournisseurs non inscrits au Data Privacy Framework [FV selon l'audit, liste non revérifiée ici] (`travaux/syn-droit.md:60` ; `travaux/strategie-retenue.md:559, 669`) | Les notes à la main sont moins complètes : d'où le rôle de Mathys |
| Coût pour Marwin | ≈ 2 à 3,5 JP non facturables pour les deux : préparation, rendez-vous, trajets, compte rendu [ES] ; déplacements [IN] | Temps de prospection, non facturé (`travaux/strategie-retenue.md:483`) | Estimation sans relevé |

### 3.1 Préparation à deux, la veille (1 heure)

| Sujet | Ce qu'on fixe | Base |
| --- | --- | --- |
| Échelle de prix | Ce que chacun peut dire en séance : 6 500 € HT ; 6 000 € HT seulement si GianLuca a vu le taux de 750 € ; version réduite à 4 800 € HT ; rien en dessous. Ces montants ne se négocient pas en séance | 11-proposition-commerciale-revisee.md, section 3.2 ; `travaux/strategie-retenue.md:231, 401` |
| Réponse à la question n° 9 | Ses effets : prix d'ouverture ; phrase sur le prénom ; manière de poser la question des « vingt jours » (section 6.1, encadré) | `travaux/strategie-retenue.md:736` |
| Incident | Ce qu'on peut dire : le texte validé, rien d'autre | `travaux/strategie-retenue.md:794` |
| Scénarios | Les huit réponses de la section 8, dites à voix haute, une fois chacune | 11-proposition-commerciale-revisee.md, sections 4.2 et 7 |
| Signal entre associés | Une phrase convenue pour reporter un point : « Nous vous répondons par écrit d'ici deux jours. » | Prix et remises à l'unanimité (`travaux/strategie-retenue.md:614`) |
| Dates | Deux ou trois créneaux pour l'entretien de cadrage en janvier, et la semaine de restitution | Fiche des disponibilités (prérequis 4) |
| Pièces | Vérification de la liste de la section 7 | — |

---

## 4. Ordre du jour minuté

### 4.1 Déroulé de 90 minutes [PR, ce livrable]

| Minutes | Sujet | Mène | Ce qu'on cherche | À éviter |
| --- | --- | --- | --- | --- |
| 0 à 5 | Accueil ; objet et durée ; « nous voulons d'abord vous écouter » ; « rien à signer aujourd'hui » | Morgan | Un cadre clair et détendu | Présenter Marwin longuement |
| 5 à 12 | L'incident de données : rappel du message écrit, mesures prises, ses questions | Morgan pour l'information ; Mathys pour les mesures techniques | Traiter le sujet tôt, pour qu'il ne pèse pas sur la fin | Sortir du texte validé ; reconnaître une responsabilité non pesée (`travaux/strategie-retenue.md:809`) |
| 12 à 37 | Ses projets et ses priorités : questions bloquantes 2 et 4 ; autres questions du bloc A (section 6.2) | Morgan pose ; Mathys note mot à mot | Ses trois priorités, dans ses mots, et ce qu'elles lui coûtent | Corriger ou conseiller ; produire une analyse en séance |
| 37 à 49 | Qui porte ses projets, qui paie : questions bloquantes 1 et 3 ; aide régionale | Morgan | La société, le signataire, l'effectif, les habitudes de paiement | Demander l'état de sa fortune ou de sa trésorerie |
| 49 à 59 | Ventes d'œuvres et fichier de prospection : question bloquante 5 ; bloc C. **Seulement si c'est une de ses priorités** ; sinon, ces dix minutes passent au cadrage | Mathys | Les préalables d'un éventuel pilote commercial (`travaux/strategie-retenue.md:311`) | Montrer le CRM ; citer une économie d'impôt |
| 59 à 77 | Notre proposition : le cadrage (livrables, déroulé, prix HT et TTC, paiement, démarrage, réception) ; les trois suites possibles, sans leur prix ; notre façon de travailler | Morgan pour le cadrage et le prix ; Mathys pour le registre, les comptes à son nom et la réversibilité | Une seule chose à juger | Les prix des suites, sauf s'il les demande (11-proposition-commerciale-revisee.md, section 2.3) |
| 77 à 85 | Ses réactions, ses questions, ses objections | Morgan | Sa réponse : oui, version réduite, un seul sujet, non, ou « je réfléchis » | Concéder un prix ou un délai en séance |
| 85 à 90 | Récapitulatif oral ; prochaines étapes ; date de l'engagement écrit et du prochain contact | Morgan ; Mathys relit la fiche (section 10) | Le résultat minimal (section 1.2) | Partir sans avoir relu le nom et le SIREN de la société |

### 4.2 Règles de conduite

- **Les 30 dernières minutes sont protégées.** Si, à la 50e minute, la conversation porte encore sur ses projets, on renvoie les ventes d'œuvres au cadrage et on passe à la société et à la proposition [PR, ce livrable].
- **S'il demande le prix dès le début**, on le donne tout de suite et simplement : « 6 500 € hors taxes, 7 800 € TTC, pour trois à quatre semaines », puis on revient aux questions. Cacher le prix abîme la confiance [HY].
- **Le rendez-vous n'est pas le cadrage.** On recueille ce qui sert à décider et à dimensionner ; le reste se fait dans le travail payé. Le gel de la production gratuite est immédiat (`travaux/strategie-retenue.md:123, 716`).
- **Écouter plus que parler** dans les 50 premières minutes [HY : c'est la seule façon d'obtenir une parole directe, qui manque au dossier].
- **À distance**, seul le PDF de la proposition est partagé à l'écran ; tout le reste est fermé (section 7.2).

### 4.3 Variante de 60 minutes

| Minutes | Sujet |
| --- | --- |
| 0 à 3 | Accueil |
| 3 à 8 | Incident |
| 8 à 25 | Priorités (questions 2 et 4) |
| 25 à 35 | Société et paiement (questions 1 et 3) |
| 35 à 50 | Le cadrage ; la question 5 est renvoyée au cadrage |
| 50 à 55 | Ses réactions |
| 55 à 60 | Récapitulatif et prochaines étapes |

### 4.4 Ordre du jour à joindre à l'invitation [PR, ce livrable]

Texte court, conforme à `travaux/strategie-retenue.md:796` (« Les questions 1 à 5 […] sous forme d'ordre du jour ») :

> 1. Vos priorités pour les trois prochains mois.
> 2. Les sociétés qui portent vos projets, et la personne qui travaillerait avec nous.
> 3. Notre proposition de cadrage : contenu, durée, prix, paiement.
> 4. Les prochaines étapes.

---

## 5. Partage des rôles entre Morgan et Mathys

### 5.1 Qui fait quoi

| Rôle | Morgan | Mathys |
| --- | --- | --- |
| Conduite | Mène le rendez-vous, tient le temps | Signale l'heure aux minutes 50 et 80 |
| Relation | Accueil, écoute, relances | Intervient sur ses sujets ; confirme que les décisions sont prises à deux |
| Incident | Rappelle le message écrit | Explique les mesures techniques prises, dans le texte validé (`travaux/strategie-retenue.md:173, 585`) |
| Questions | Blocs « priorités », « société », « paiement » | Bloc « ventes d'œuvres et fichier » ; questions sur les accès et les outils |
| Proposition | Cadrage, prix, paiement, suites possibles | Registre au nom de sa société, comptes à son nom, sauvegarde, réversibilité (`travaux/strategie-retenue.md:189`) |
| Sujets sensibles | Bureaux, emploi, capital : une phrase, puis retour à l'ordre du jour (section 8.3) ; déclaration de son lien avec BOJ.ART si le sujet vient | Confirme que le retrait de Medhi est une décision des deux associés |
| Notes | — | Fiche de la section 10, paroles de GianLuca entre guillemets |
| Récapitulatif | Le dit à voix haute | Relit la fiche, vérifie le nom, le SIREN, les dates |
| Après | Envoie le récapitulatif | Le relit avant envoi (contrôle à quatre yeux, `travaux/strategie-retenue.md:578`) |

Cette répartition suit celle de la stratégie : Morgan porte la relation et les prix, Mathys la technique et les données (`travaux/strategie-retenue.md:619` ; 06-fonctionnement-a-deux.md, section 2.5). 08-feuille-de-route.md (semaine 5) ne nomme que Morgan pour le rendez-vous ; ce livrable recommande la présence des deux pour les raisons suivantes.

### 5.2 Pourquoi les deux

- **Preuve** : les prix et les remises se décident à l'unanimité (`travaux/strategie-retenue.md:614`) ; Mathys est le titulaire présumé du dépôt du CRM (`travaux/strategie-retenue.md:173`) et c'est lui qui a demandé le recentrage du fichier sur 100 entreprises (`crm/PASSATION.md:7`) [FV].
- **Hypothèse** : GianLuca n'a traité qu'avec Morgan [DR] ; voir le binôme rend crédible le contrôle à quatre yeux promis [HY].
- **Limite** : une JP de plus, non facturable [ES], et un trajet si le rendez-vous a lieu sur place [IN].
- **Décision** : à inscrire dans la fiche des disponibilités du 19 nov. (prérequis 4).

### 5.3 Si Mathys ne peut pas venir

- Il se joint à distance pour les minutes 5 à 12 (incident) et 49 à 77 (fichier, proposition), si possible.
- Sinon, Morgan prend les notes lui-même et ne concède rien : toute demande nouvelle reçoit la phrase convenue (« Nous vous répondons par écrit d'ici deux jours »).
- Mathys relit le récapitulatif avant l'envoi.

---

## 6. Questions à poser

### 6.1 Les dix questions bloquantes

La stratégie en compte dix : cinq pour GianLuca, cinq pour les associés (`travaux/strategie-retenue.md:723-737`). **Les cinq questions internes se règlent avant de fixer la date** ; elles sont des prérequis (section 2).

**Questions 1 à 5, à poser à GianLuca**

| N° | Formulation proposée | Ce qu'on doit obtenir | Relance si la réponse est vague | Ce que la réponse décide |
| --- | --- | --- | --- | --- |
| 1 | « Pour vos projets, quelle société signerait avec nous, paierait et validerait notre travail ? Pouvez-vous nous donner son nom exact, son numéro SIREN et la personne qui peut signer ? Combien de salariés compte-t-elle ? Est-ce la même société pour tous vos projets ? » | Dénomination, SIREN, signataire habilité, effectif ; payeur et valideur | « Laquelle porte le sujet le plus important pour vous ? » | Bon de commande, facture, TVA, responsabilité des données ; avec 5 salariés au plus, règle de rétractation possible [HY] (`travaux/strategie-retenue.md:466`) |
| 2 | « Si vous deviez choisir trois sujets à faire avancer d'ici trois mois, lesquels ? Pour chacun, qu'est-ce que cela vous coûte aujourd'hui : du temps, de l'argent, des occasions manquées ? » Puis la question sur le volume (encadré ci-dessous) | Trois priorités, dans ses mots ; un ordre ; un coût actuel, même approximatif | « Si un seul de ces sujets avançait, lequel changerait le plus votre année ? » | Le contenu du cadrage ; la voie probable ensuite (`travaux/strategie-retenue.md:241-251`) |
| 3 | « Comment votre société règle-t-elle habituellement ses prestataires : à la commande, à réception, à trente jours ? Récupère-t-elle la TVA ? Avez-vous une enveloppe en tête pour ce premier travail ? Pensez-vous demander l'aide de la Région au conseil ? Si oui, le dossier doit être déposé avant toute signature. » | Mode et délai de paiement ; TVA ; ordre de grandeur ; aide oui ou non | « Pour un travail de cet ordre, comment procédez-vous d'habitude ? » | Le calendrier de signature ; si la TVA n'est pas récupérée, le TTC est son vrai coût [HY] (`travaux/strategie-retenue.md:462`) ; dépôt de l'aide avant signature [DR] (`travaux/strategie-retenue.md:239`) |
| 4 | « Qui, chez vous, travaillerait avec nous au quotidien ? Quelqu'un est-il déjà en place, ou faudrait-il recruter ? Quels documents et quels accès pourriez-vous nous ouvrir pendant le cadrage ? Comment préférez-vous échanger : téléphone, messagerie, e-mail, rendez-vous ? Et quelle présence attendez-vous de nous ? » | Un interlocuteur ; une réponse sur le recrutement ; le canal réel ; ses attentes de présence | « Quand vous déléguez aujourd'hui, à qui, et comment ? » | Les conditions de démarrage (accès sous 10 jours ouvrés) ; la voie « organisation interne » s'il veut recruter ; 06-fonctionnement-a-deux.md, section 12 |
| 5 | « La vente d'œuvres aux entreprises fait-elle partie de vos priorités ? Si oui : au nom de quelle société vendez-vous ? Quelles œuvres sont disponibles aujourd'hui, de quels artistes, à quels prix ? Qui vous conseille sur la fiscalité ? Qui appellera les entreprises : vous, un assistant, Quali Contact ? Avez-vous signé avec eux ? » | Structure vendeuse ; 5 à 10 œuvres réellement disponibles ; conseil fiscal ; appelant ; état du contrat avec Quali Contact | « Avez-vous déjà vendu à des entreprises, par exemple à Paris ? Avec quel argument ? » (question restée ouverte, `interne/offres-de-carlone-catalogue-crm.md:124`) | Faisabilité du pilote commercial (`travaux/strategie-retenue.md:311`) ; la structure vendeuse reste un point « À décider par les associés » dans la passation du CRM [FV] (`crm/PASSATION.md:31`) |

> **Écart avec la stratégie retenue : la question des « vingt jours ».**
> *Ce que dit la stratégie.* La question 2 demande : « Les « vingt jours par mois » viennent-ils de vous ? » (`travaux/strategie-retenue.md:727`).
> *Pourquoi l'adapter.* Si GianLuca n'a jamais vu l'offre de 20 journées, la question réintroduit à l'oral un volume que la stratégie retire de tout document (`travaux/strategie-retenue.md:661`) et qui peut devenir une attente [HY]. Ce qu'il a vu est inconnu [IN] (`travaux/ex-C2-offre.md:221`).
> *Ce que ce livrable retient [PR, ce livrable].* La forme dépend de la réponse de Morgan à la question n° 9.
> - S'il a vu une offre chiffrée en jours : « Dans notre ancienne proposition, nous étions partis sur un volume de jours par mois. Était-ce votre attente, ou notre lecture de vos besoins ? »
> - S'il ne l'a pas vue : « Combien de temps imaginiez-vous que nous y consacrions, et sous quelle forme : présence, réunions, réponses dans la journée ? »
> *Limite.* Dans le second cas, on n'apprend pas d'où venait le chiffre ; seul Morgan peut le dire. *Décision.* Morgan et Mathys choisissent la forme la veille (section 3.1).

**Questions 6 à 10, à régler entre associés avant de fixer la date**

| N° | Question (`travaux/strategie-retenue.md:733-737`) | Effet sur le rendez-vous |
| --- | --- | --- |
| 6 | Depuis quand savez-vous que le dépôt du CRM est public ? Qui contrôle l'organisation qui l'héberge ? Est-il encore public ? Des copies existent-elles ? Qui décide de la notification ? | Prérequis 1 et 2 ; ce qu'on peut dire de l'incident |
| 7 | Combien de JP par mois chacun engage-t-il par écrit de décembre 2026 à juin 2027, et quels projets Morgan suspend-il ? Quelle est la situation de Mathys ? | Les dates qu'on peut proposer pour janvier ; la présence de Mathys |
| 8 | Mathys approuve-t-il la stratégie, le retrait de Medhi, la SAS et le régime du CRM ? | Prérequis 4 : sans accord, pas de rendez-vous (`travaux/strategie-retenue.md:614`) |
| 9 | Qu'a vu, reçu ou accepté GianLuca : version à quatre jours, lettre du 29 oct. au prénom erroné, options du 30 oct., diaporama de 13 ou de 11 vues, taux de 750 €, rapport CRM, vernissage ? Qu'a-t-on promis à Medhi ? | Prix d'ouverture (6 000 € HT s'il a vu le taux) ; phrase sur le prénom ; forme de la question des « vingt jours » ; risque qu'il ait accepté l'offre de six mois à l'oral (`travaux/strategie-retenue.md:770`) |
| 10 | Quel apport pouvez-vous déposer (8 000 à 14 000 €), quelle rémunération acceptez-vous (≈ 1 350 à 1 550 € nets chacun en régime central selon la stratégie ; ≈ 1 100 à 1 500 € selon le modèle financier [ES], `modele-financier/scenarios.md` ; écart signalé dans 01-synthese-direction.md), et pouvez-vous vivre trois à quatre mois sans rémunération de Marwin ? | Peut-on dire « oui » à un démarrage en janvier ? Résister à une offre d'emploi (section 8.2) |

### 6.2 Les autres questions, si le temps le permet

Elles viennent de `travaux/syn-portefeuille.md:606-619`, de `travaux/ex-C2-offre.md:219-243` et de 06-fonctionnement-a-deux.md. Chacune doit servir à décider ou à dimensionner ; sinon, elle attend le cadrage.

**Bloc A. Besoin et fonctionnement** (minutes 12 à 37)
- « Qu'est-ce qui vous prend le plus de temps aujourd'hui, concrètement ? »
- « Qu'est-ce que vous voulez absolument garder en main ? » (décisions qu'il garde, `travaux/syn-portefeuille.md:613`)
- « Dans trois mois, qu'est-ce qui vous ferait dire que cela valait la peine, ou qu'il faut arrêter ? » (`travaux/syn-portefeuille.md:618`)
- « Comment voyez-vous la suite au-delà de quelques mois ? » (`travaux/ex-C2-offre.md:239`)

**Bloc B. Lieux et projets** (en quelques mots seulement ; le détail est au cadrage)
- « Quels lieux avez-vous aujourd'hui, lesquels sont en cours de rachat, et qui les exploite ? » Les pièces disent tantôt qu'il « souhaite racheter » le M (`sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:15`), tantôt qu'« un associé rachète deux établissements » (`crm/PASSATION.md:41`) [DR].
- « Le projet de cabaret est-il toujours d'actualité ? » (`travaux/ex-C2-offre.md:236`)
- « Pour la galerie de 2027, où en êtes-vous : lieu, calendrier ? »

**Bloc C. Ventes d'œuvres et fichier** (minutes 49 à 59, si c'est une priorité)
- « Le fichier de 500 entreprises préparé pour vous : souhaitez-vous l'utiliser ? Quelle société en serait responsable ? » (`travaux/syn-portefeuille.md:617`)
- « Aux entreprises, préférez-vous parler seulement des œuvres, ou aussi des lieux où elles seraient exposées ? » Le CRM interdit pour l'instant de citer les lieux (`crm/PASSATION.md:49`) [FV].
- « Quel outil utilise Quali Contact, et avez-vous un modèle de fichier ? » (`travaux/syn-portefeuille.md:615`)

**Bloc D. Personnes et documents**
- « Qui sont votre expert-comptable et votre avocat ? Pourrons-nous préparer des dossiers pour eux, avec votre accord ? »
- « Quels documents pourriez-vous nous confier pour le cadrage, une quinzaine au plus ? » (`travaux/strategie-retenue.md:226`)

### 6.3 Ce qu'on garde pour le cadrage

Ne pas demander en détail, parce que c'est le travail payé (`travaux/strategie-retenue.md:225`) : la fiche de chaque lieu (propriétaire, exploitant, licences, classement), les budgets par projet, l'organigramme et les associés de chaque société, la liste complète des accès, les plafonds de délégation, les contrats des prestataires, l'inventaire et la provenance des œuvres.

### 6.4 Ce qu'on ne demande pas

| Question écartée | Pourquoi | Base |
| --- | --- | --- |
| « Pour les bureaux, l'emploi et l'investissement évoqués : sous quelle forme ? » (`travaux/syn-portefeuille.md:619`) | Ces sujets ne se discutent pas avant le bilan du mois 6. Les ouvrir nous-mêmes crée une attente. S'il en parle, section 8.3 | `travaux/strategie-retenue.md:629-632, 707` |
| Tout ce qui touche à sa fortune ou à sa trésorerie personnelle | Indiscret ; et un patrimoine déclaré n'est pas une trésorerie. On consulte les registres publics sans contact | `travaux/strategie-retenue.md:566` |
| L'avis de Medhi, ou ce que GianLuca sait de la décision | Le retrait relève des associés ; on ne parle pas pour Medhi | `travaux/strategie-retenue.md:615, 793` |

---

## 7. Ce qu'il faut apporter, et ce qu'il ne faut pas montrer

### 7.1 À apporter

| Pièce | Forme | Qui | Condition |
| --- | --- | --- | --- |
| Proposition de cadrage, version finale (pour-gianluca/proposition-de-cadrage.md, sans les lignes « Audit », « Statut », « Sources » ni la note interne) | Deux exemplaires papier ; PDF daté | Morgan | Validée par les deux ; prix ajusté selon la question n° 9 |
| Copie du message de recadrage et du message sur l'incident, tels qu'envoyés | Papier | Morgan | Pour citer les mots exacts |
| Comparaison de **ses** coûts : Marwin, un assistant salarié, un coordinateur salarié, des prestataires ; aucune ligne des archives | Une page | Morgan | À sortir seulement s'il parle d'embaucher ou demande une comparaison (11-proposition-commerciale-revisee.md, section 5.2, encadré n° 1 ; 05-proposition-de-valeur.md, section 4.1) |
| Ordre du jour (section 4.4) | Papier | Morgan | — |
| Fiche de notes (section 10) | Papier | Mathys | — |
| Deux ou trois dates pour l'entretien de cadrage en janvier, et la semaine de restitution | Agenda | Les deux | Fiche des disponibilités signée |
| Coordonnées professionnelles qui fonctionnent | Carte ou e-mail | Morgan | Les domaines olsen-web.fr et olsen-contact.fr sont suspendus depuis le 3 oct. [DR] (`travaux/note-point-4-novembre-et-activites.md:7`) : ne pas donner d'adresse qui en dépend |
| Échelle de prix convenue la veille | Dans la tête ; jamais sur la table ni à l'écran | Les deux | 11-proposition-commerciale-revisee.md, section 3.2 |

### 7.2 À ne pas montrer

| Pièce | Pourquoi | Où elle se trouve |
| --- | --- | --- |
| Diaporama « Offre Marwin Tech pour Carlone » (11 vues) et PDF de 13 vues | Formules à 15 000 et 30 000 € HT, taux de 750 €, laboratoire, « CRM prêt à servir » ; 11 vues sur 11 à corriger [FV] | 11-proposition-commerciale-revisee.md, sections 6.2 et 6.3. Exception : une nouvelle version datée, construite à partir de la proposition de cadrage |
| Offre écrite du 2 nov. | Formules, positions de négociation, option création avec Medhi | `interne/offre-marwin-tech-remuneration-et-collaboration.md:13-22, 244-248` |
| Page du 29 oct. avec la lettre au client | Ancien prénom dans la formule d'appel ; 15 000 € ; BOJ.ART | `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:9-13` |
| Options du 30 oct. | Ancien prénom en page 1 ; annexe interne sur le revenu des fondateurs | `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` |
| STRATES v1.1, vernissage, Éclosion, visuels générés par IA | Sujets retirés ou gelés (`travaux/strategie-retenue.md:644-646`) | `pour-carlone/` |
| Le CRM en direct, ses fiches, le rapport du 29 oct., le simulateur d'économie d'impôt | Violation de données très probable (`travaux/strategie-retenue.md:32`) ; le rapport affirme « Personne d'autre ne lit les fiches ni le suivi » (`crm/docs/rapport/rapport-crm-hermes360.md:15`) ; simulateur retiré (`travaux/strategie-retenue.md:653`) | `crm/` |
| Catalogue de neuf offres de vente d'œuvres | Arguments fiscaux non validés ; place de BOJ.ART (`interne/offres-de-carlone-catalogue-crm.md:106-110`) | `interne/offres-de-carlone-catalogue-crm.md` |
| Les documents de l'audit, ce fichier, les pages internes de Morgan (« Projet Carlone — le contexte réuni ») | Coûts, marges, planchers, rémunérations, stratégie (`travaux/strategie-retenue.md:787-791`) | `audit/` ; pages privées (`travaux/note-point-4-novembre-et-activites.md:13`) |
| Tout ce qui touche aux autres activités de Morgan, à ses autres entreprises et à ses abonnements | Interne ; sans intérêt pour le client | `travaux/note-point-4-novembre-et-activites.md:6-17` |

---

## 8. Scénarios de réponses et réponses préparées

Toutes les réactions ci-dessous sont des hypothèses [HY] : aucune pièce ne rapporte une parole directe de GianLuca (`travaux/syn-portefeuille.md:88-90`). Les réponses appliquent la stratégie. Les autres objections (prix, taux de 750 €, paiement à trente jours, CRM, astreinte, « votre société n'existe pas ») sont traitées dans 11-proposition-commerciale-revisee.md, section 4.2.

### 8.1 Il veut tout, tout de suite

**Ce qu'il peut dire** : « Je n'ai pas besoin d'un diagnostic, prenez tout en main dès maintenant. » « Je veux une équipe sur place. » Ce souhait est cohérent avec les besoins rapportés : « déléguer le quotidien » (`sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md:65`), « sans avoir à en gérer chaque détail » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:13`) [DR].

**Réponse préparée** (Morgan) :
> « C'est bien là que nous voulons aller. Pour tout prendre en main sans rien laisser tomber, il nous faut d'abord la liste de vos sociétés, de vos lieux et de vos priorités : c'est le cadrage, trois à quatre semaines. Si votre société, l'acompte et les accès sont prêts, le suivi régulier peut commencer juste après la restitution, sur un nombre de projets fixé. »

**S'il insiste pour démarrer tout de suite** :
> « Notre société est en cours d'immatriculation : nous ne pouvons ni facturer ni commencer avant. Si votre société s'engage d'ici la mi-décembre, nous démarrons début janvier. »

**S'il demande une présence quotidienne ou un volume de jours** :
> « Nous ne vendons pas des journées de présence, mais des résultats : un point par semaine, un compte rendu sous 24 heures ouvrées, des décisions préparées. Une présence tous les jours, ce serait un poste chez vous ; nous pouvons vous aider à le définir. »

**À ne pas dire** : « vingt jours », un taux journalier, « on peut commencer lundi », « on s'occupe de tout ».

**Décision interne** : la stratégie prévoit d'accélérer s'il fournit société, accès et acompte (`travaux/strategie-retenue.md:60`) : le cadrage reste la première commande, puis le socle récurrent peut suivre la restitution sans pilote intermédiaire (11-proposition-commerciale-revisee.md, section 2.4). Le plafond de 10 JP facturables par mois tient (`travaux/strategie-retenue.md:43`). On refuse 20 à 40 JP par mois sans société, mandat ni accès (`travaux/strategie-retenue.md:702`), et tout démarrage avant l'immatriculation (`travaux/strategie-retenue.md:705`). Les prix du suivi régulier ne se donnent que s'il les demande (11-proposition-commerciale-revisee.md, section 2.3).

### 8.2 Il veut embaucher plutôt que payer un prestataire

**Cas a. Il préfère recruter quelqu'un** : « Un salarié me coûterait moins cher. »

> « C'est possible, et nous vous le montrerons chiffres à l'appui. Pour un besoin stable de plus de six à huit jours par mois, un coordinateur salarié vous coûte moins cher que nous. Nous pouvons alors outiller cette personne : registre, procédures, comptes à votre nom, fiche de poste, formation. Le cadrage vous dira laquelle des deux solutions vous convient. »

Base : seuil de 6 à 8 JP par mois de besoin stable [ES] (`travaux/strategie-retenue.md:108, 378`) ; coût employeur d'un assistant non cadre, 2 249 à 2 808 € par mois, et d'un chef de projet cadre, 5 380 à 6 149 € [ES : résultats du simulateur de l'Urssaf, codés [MM] par la stratégie] (`travaux/strategie-retenue.md:326, 376` ; `travaux/controle-modele.md:95`) ; réponse « réduire » vers l'offre d'outillage et de passation à 7 500 € HT (9 000 € TTC) (`travaux/strategie-retenue.md:333, 695`). Montrer la page de comparaison (section 7.1). Aucun outil d'IA dans le recrutement (`travaux/strategie-retenue.md:329`).

**Cas b. Il veut embaucher Morgan ou Mathys à la place de Marwin** : « Pourquoi ne viendriez-vous pas travailler pour moi ? »

> « Merci, c'est une marque de confiance. Pour l'instant, nous voulons vous montrer ce que Marwin vous apporte. Un emploi serait un sujet séparé, que nous pourrons regarder après six mois de travail ensemble, et pas pour nous deux. »

Base : employeur refusé avant le bilan du mois 6, jamais des deux associés (`travaux/strategie-retenue.md:631, 704`).

**Décision interne** : la tentation est réelle. Un poste de cadre chez lui, ≈ 3 400 € nets, rapporterait plus que Marwin en régime central la première année [ES] (`travaux/strategie-retenue.md:707` ; 09-modele-economique-tresorerie.md, section 7.3). Morgan a déjà écrit « Je préfère être prestataire ou salarié » [DR] (`interne/recueil-sessions-chatgpt-2026-11-04.txt:248`). Règle : personne ne dit oui en séance, même par politesse. Si l'un des associés veut étudier l'offre, c'est une décision séparée entre associés, revenu contre indépendance (`travaux/strategie-retenue.md:707`), et les règles de 10-structures-et-relations.md, section 6.1, s'appliquent.

**À noter mot à mot** : le poste, les fonctions, le lieu, le montant évoqué.

**À ne pas dire** : nos besoins de revenu ; « ce serait plus rentable pour nous » ; un montant de salaire attendu.

### 8.3 Il propose des bureaux, une rémunération ou une entrée au capital

**Ce que disent les pièces** : il « propose des bureaux, une bonne rémunération et envisage d'investir dans l'activité de Morgan et Mathys » [DR] (`interne/contexte-projet-carlone.md:24` ; `interne/offres-de-carlone-catalogue-crm.md:9`) ; « il a investis dans des bureaux pour du personnel ont en ferait partie » (Morgan, vers le 25 oct.) [DR] (`interne/recueil-sessions-chatgpt-2026-11-04.txt:220`).

**Réponse préparée** (Morgan) :
> « Merci. Nous préférons traiter chaque sujet par un accord séparé, pour que chacun puisse vivre ou s'arrêter seul. Pendant le cadrage et le premier essai, nous travaillons avec nos propres moyens. Nous pourrons parler de bureaux après le bilan des six mois. Une participation au capital, nous l'accueillerions plus tard, une fois la collaboration prouvée, et jamais en échange d'une baisse de prix. »

| Sujet | Règle (`travaux/strategie-retenue.md:629-632`) | Ce qu'on note |
| --- | --- | --- |
| Bureaux | Refusés pendant le cadrage et le pilote ; ensuite, convention séparée, sans horaires imposés ni lien avec les honoraires | Lieu, conditions, date |
| Rémunération | Voir section 8.2, cas b | Forme, montant, fonctions |
| Capital | Pas avant 12 à 24 mois et deux renouvellements ; minoritaire, sans veto ; contrat client résiliable à part ; « L'acompte n'est ni du capital ni un prêt » [FV] (`interne/offre-marwin-tech-remuneration-et-collaboration.md:142`) | Forme, montant, horizon |
| Financer STRATES à la place du capital | Piste interne du 2 nov. (`interne/offre-marwin-tech-remuneration-et-collaboration.md:144`), caduque depuis le gel de STRATES (10-structures-et-relations.md, section 6.4) | — |

**Signal de suspension** : s'il lie ces sujets aux honoraires (« je vous loge, vous baissez le prix »), on refuse cette partie et on le dit (`travaux/strategie-retenue.md:684, 703`).

**À ne pas dire** : nos besoins de financement, l'apport des associés, les enjeux d'aides publiques ; « oui pour les bureaux dès janvier ».

### 8.4 Il ne veut payer qu'au résultat

**Ce qu'il peut dire** : « Payez-vous sur les ventes. » « Je paie si cela marche. » « Prenez un pourcentage. »

**Réponse préparée** (Morgan) :
> « Nous ne pouvons pas être payés sur vos ventes d'œuvres : cela ferait de nous un intermédiaire de vente, avec des obligations que nous ne portons pas. Et les ventes dépendent aussi de vos œuvres et de vos appels. Ce que nous proposons protège votre argent autrement : un prix fixe pour un résultat écrit à l'avance ; la moitié à la commande, le solde à la remise ; dix jours ouvrés pour formuler des réserves, que nous corrigeons. »

**S'il insiste** :
> « Plus tard, une part liée à une économie réelle, mesurée et validée par vous, peut se discuter, au bout d'un an. Pas sur les ventes. »

Base : aucune variable sur les ventes d'œuvres (statut d'intermédiaire, lutte contre le blanchiment, droit de suite [HY]) ; prime sur économie réelle mesurée possible à 12 mois (`travaux/strategie-retenue.md:421-422, 649`) ; réception et paiement du cadrage (`travaux/strategie-retenue.md:235-236`). Les ventes sont suivies, jamais promises (`travaux/strategie-retenue.md:157`).

**S'il refuse tout paiement non lié au résultat** : c'est un refus de payer le cadrage (section 8.7). Toute demande de rémunération sur les ventes est un signal de suspension (`travaux/strategie-retenue.md:685`).

**À ne pas dire** : un nombre de ventes ou de rendez-vous espéré ; « on peut mixer fixe et commission ».

### 8.5 Il parle de STRATES ou de Medhi

**Ce qu'il peut dire** : « Et le tableau peint par le robot ? » « Medhi m'a parlé de votre projet. » « Je veux financer STRATES. » « Où en est le vernissage ? »

**Contexte** : décision orale du 4 nov. de retirer Medhi et BOJ.ART de l'offre [DR] (`travaux/note-point-4-novembre-et-activites.md:25`) ; GianLuca aurait racheté « l'ancienne affaire de Medhi » [DR] (`interne/contexte-projet-carlone.md:24`) ; STRATES est gelé, le vernissage « signature » reporté (`travaux/strategie-retenue.md:644, 646`).

**Réponse préparée** (Morgan ; Mathys confirme que c'est une décision des deux) :
> « Ces projets ne font plus partie de l'offre de Marwin. Cela ne dit rien du travail de Medhi. Si ses œuvres vous intéressent pour la galerie, la relation se fait directement entre lui et votre société, sans nous. Comme nous vous l'avons écrit, Morgan a un lien avec BOJ.ART : c'est pourquoi nous ne vous ferons aucune recommandation sur ses œuvres. »

**Sur le vernissage** :
> « Un premier événement, sans robot, pourra être étudié plus tard, avec votre société comme organisatrice. »

**S'il veut financer STRATES** : « C'est un projet de Medhi : voyez-le directement avec lui. »

Base : relation directe par dépôt-vente, sans Marwin ni commission (`travaux/strategie-retenue.md:643`) ; déclaration proactive du lien de Morgan (`travaux/strategie-retenue.md:635`) ; premier événement sans robot par un lot séparé (`travaux/strategie-retenue.md:646`).

**À ne pas dire** : le détail de la décision ; ce qui avait été dit ou promis à Medhi (`travaux/strategie-retenue.md:793`) ; un avis sur Medhi ; une date ou un prix de STRATES ; le programme de 323 875 € (`interne/offre-marwin-tech-remuneration-et-collaboration.md:145`) ; un robot devant le public.

**Prérequis** : le message à Medhi est parti (prérequis 5). Sinon, le rendez-vous n'a pas lieu.

### 8.6 Il ne nomme pas de société

**Ce qu'il peut dire** : « Facturez-moi, on verra. » « Mon comptable s'en occupera. » « La société de la galerie n'existe pas encore. » « C'est mon associé qui exploite les lieux. »

**Contexte** : aucune société de GianLuca n'est nommée dans le dépôt [FV négatif] (`travaux/syn-portefeuille.md:101-102`). Quatre cas sont possibles : une société pour tout, plusieurs sociétés, une signature personnelle, ou un tiers qui exploite les lieux (`travaux/syn-portefeuille.md:300-303`).

**Réponse préparée** (Morgan) :
> « Nous en avons besoin pour une raison simple : la facture, la TVA, la signature et la responsabilité des données dépendent de la société. Si vous en avez plusieurs, une seule peut commander le cadrage pour l'ensemble ; les suites seront facturées à la société concernée. Laquelle porte le sujet le plus important pour vous ? »

**S'il ne sait pas** :
> « Pouvez-vous nous l'indiquer, avec son numéro SIREN et la personne qui signe, d'ici le [date, au plus tard le vendredi 11 décembre] ? Votre expert-comptable peut aussi nous l'envoyer. »

**S'il veut signer à titre personnel** :
> « C'est possible pour certains projets, mais les règles changent : nous devons d'abord les vérifier avec notre avocat. » [HY] (`travaux/syn-portefeuille.md:302`)

**Si un associé ou un tiers exploite les lieux** : sa société commande le cadrage ; pour ces lieux, un accord séparé viendra plus tard avec l'exploitant (`travaux/syn-portefeuille.md:303`).

**Décision interne** : aucun travail, aucun document produit, aucune immatriculation sans engagement écrit d'une société identifiée (`travaux/strategie-retenue.md:552, 665`). Sans société au 15 décembre : report à janvier, sans production (`travaux/strategie-retenue.md:697`). On ne le présente pas comme un ultimatum.

**À ne pas dire** : « on peut facturer par l'entreprise de Morgan » (`travaux/strategie-retenue.md:564`) ; « on commence et on régularisera ».

### 8.7 Il refuse de payer le cadrage

Trois refus différents, trois réponses :

| Ce qu'il dit | Réponse | Base |
| --- | --- | --- |
| « C'est trop cher. » | Détailler ce qu'il garde, même s'il s'arrête là. Proposer la version réduite : 4 800 € HT (5 760 € TTC), inventaire et trois priorités. S'il a vu le taux de 750 €, le cadrage complet à 6 000 € HT. Rien en dessous, et rien d'autre en séance | 11-proposition-commerciale-revisee.md, section 3.2 ; `travaux/strategie-retenue.md:231, 694` |
| « Je ne paie pas un diagnostic, je veux du concret. » | Un seul sujet, en lot direct, sur devis écrit après le rendez-vous, avec ses préalables écrits (par exemple le catalogue privé de ses œuvres) | `travaux/strategie-retenue.md:693` ; 11-proposition-commerciale-revisee.md, section 3.2, rang 4 |
| « Je ne paie rien d'avance », ou « vous avez déjà fait le CRM gratuitement, continuez » | Pas de suite. Le CRM ne lui sera jamais refacturé et la remise en ordre est à notre charge, mais tout nouveau travail est payé | `travaux/strategie-retenue.md:385-386, 701` |

**Réponse au refus total** (Morgan) :
> « Nous comprenons. Sans ce premier travail, nous ne pouvons pas vous proposer de suite sérieuse, et nous préférons nous arrêter là plutôt que de promettre ce que nous ne pourrions pas tenir. Les documents qui vous concernent vous restent acquis : nous vous dirons par écrit ce que nous pouvons vous remettre. Notre porte reste ouverte. »

**Décision interne** : l'hypothèse d'un besoin de pilotage est infirmée (`travaux/syn-portefeuille.md:246-250`). Report sans date, temps réorienté vers d'autres clients (`travaux/strategie-retenue.md:698`). La remise des données du CRM attend l'avis sur les rôles RGPD : rien n'est remis sur place (`travaux/strategie-retenue.md:701`).

**À ne pas dire** : nos coûts, nos marges ; « nous perdons de l'argent » ; un geste hors de l'échelle convenue.

### 8.8 Il demande la réduction d'impôt sur des œuvres faites à la machine

**Ce qu'il peut dire** : « Mes clients pourront déduire les pièces imprimées en 3D ? » « Mettez l'avantage fiscal dans vos e-mails. » « STRATES y ouvre droit ? »

**Contexte** : les pièces de Marwin disent qu'il « vend des œuvres d'art avec un avantage fiscal » [DR] (`interne/offres-de-carlone-catalogue-crm.md:7`), sans savoir s'il vend déjà ainsi (`interne/offres-de-carlone-catalogue-crm.md:124`). Le catalogue de Marwin écrivait déjà : « ce qui est fait à la machine en est très probablement exclu » (`interne/offres-de-carlone-catalogue-crm.md:106` ; voir aussi :98 et :109).

**Ce que disent les textes** :
- Le dispositif des entreprises qui achètent des œuvres d'artistes vivants (article 238 bis AB du CGI) est une **déduction** du résultat, par cinquièmes sur cinq exercices, plafonnée ; il couvre les achats faits avant le 31 décembre 2028 [FV] (BOI-BIC-CHG-70-10-20260415, https://bofip.impots.gouv.fr/bofip/1801-PGP.html/identifiant=BOI-BIC-CHG-70-10-20260415, consulté le 4 nov. 2026 selon `travaux/rj-R2-fiscal.md:95-96` ; `travaux/syn-droit.md:553-556`).
- L'œuvre doit être originale : par exemple, peintures « entièrement exécutés à la main par l'artiste » [FV] (CGI, annexe III, art. 98 A, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006298775, consulté le 4 nov. 2026 selon `travaux/rj-R2-fiscal.md:98`).
- La doctrine exclut les procédés qui suppléent la main « en tout ou en partie » et les œuvres « exécutées par des moyens mécaniques » [FV] (BOI-TVA-SECT-90-10, https://bofip.impots.gouv.fr/bofip/1279-PGP.html, consulté le 4 nov. 2026 selon `travaux/rj-R2-fiscal.md:99`).
- Application aux pièces imprimées en 3D, peintes par un robot ou produites avec l'IA : **très probablement exclues** [HY fondée sur ces textes], sauf position écrite de l'administration (rescrit), dont le silence ne vaut pas accord [FV] (`travaux/syn-droit.md:56, 559-560, 568`).
- Le mécénat (article 238 bis) est un autre dispositif : une **réduction** d'impôt pour un don sans contrepartie à un organisme d'intérêt général ; les dons aux artistes n'y ouvrent pas droit [FV] (`travaux/syn-droit.md:561`).

**Réponse préparée** (Morgan) :
> « Ce n'est pas à nous de le trancher : c'est une question pour votre conseil fiscal, et nous ne mettrons aucun argument fiscal dans un message sans son avis écrit. Ce que disent les textes publics : le dispositif pour les entreprises qui achètent des œuvres d'artistes vivants est une déduction étalée sur cinq ans, pas une réduction d'impôt. Il vise des œuvres originales, par exemple des peintures entièrement faites à la main par l'artiste. L'administration écarte les procédés qui remplacent la main, même en partie. Une pièce imprimée en 3D, peinte par un robot ou produite avec l'IA en est donc très probablement exclue. Votre conseil peut demander une position écrite de l'administration sur une pièce précise. »

**S'il parle de mécénat** :
> « Le mécénat est un autre dispositif : un don sans contrepartie à un organisme d'intérêt général. Il ne sert pas à vendre une œuvre. »

**Décision interne** : le simulateur d'économie d'impôt du CRM est retiré (`travaux/strategie-retenue.md:653`) ; un kit commercial ne part qu'avec des mentions validées par son conseil, sans le mot « mécénat » (`travaux/strategie-retenue.md:298`) ; l'exposition chez le vendeur n'est pas prévue par la doctrine et reste à valider (`crm/PASSATION.md:35`) [HY].

**À ne pas dire** : un montant d'économie ; « c'est déductible » ; « mécénat » ; un avis sur un schéma précis.

---

## 9. Lignes rouges pendant le rendez-vous

La liste complète de ce qu'on ne concède jamais dans un contrat est dans 11-proposition-commerciale-revisee.md, section 3.4. Celle-ci ne garde que ce qui peut se jouer en séance.

| N° | Ligne rouge | Phrase de sortie | Si la demande insiste | Base |
| --- | --- | --- | --- | --- |
| 1 | Rien n'est signé pendant le rendez-vous : ni bon de commande, ni lettre d'intention | « Nous vous envoyons le document d'ici deux jours, à signer à distance. » | On s'en tient là | Encadré ci-dessous |
| 2 | Aucun prix, aucune remise hors de l'échelle convenue la veille | « Nous vous répondons par écrit d'ici deux jours. » | Décision à deux sous 48 h | `travaux/strategie-retenue.md:614` |
| 3 | Aucune date de démarrage avant l'immatriculation, la signature et l'encaissement, et avant 7 jours si sa société compte 5 salariés au plus | « Nous démarrons à l'encaissement de l'acompte, après l'immatriculation. » | Report du travail (`travaux/strategie-retenue.md:705`) | `travaux/strategie-retenue.md:458, 466` ; 12-gouvernance-contrat-sortie.md, section 11.6, encadré |
| 4 | Aucune démonstration du CRM ; aucune donnée réelle à l'écran | « Il sera remis en conformité avant tout usage. » | — | `travaux/strategie-retenue.md:669, 819` |
| 5 | Rien sur l'incident hors du texte validé ; aucune reconnaissance de responsabilité | « Nous vous avons écrit ce que nous savons et ce que nous avons fait. Pour le reste, nous vous répondrons par écrit, après avis de notre conseil. » | Question transmise au conseil le jour même | `travaux/strategie-retenue.md:794, 809` |
| 6 | Aucun avis fiscal ou juridique ; aucune promesse de déduction | Section 8.8 | — | `travaux/strategie-retenue.md:187, 650` |
| 7 | Aucune promesse de ventes, de rendez-vous ou d'ouverture d'un lieu | « Nous les suivons ; nous ne pouvons pas les promettre. » | — | `travaux/strategie-retenue.md:157, 798` |
| 8 | Ni commission, ni encaissement, ni garde d'œuvres ; ni bureaux, ni emploi, ni capital en paiement | Sections 8.3 et 8.4 | Refus de cette partie, expliqué | `travaux/strategie-retenue.md:44, 703` |
| 9 | Aucun volume de journées, aucun taux journalier, aucune présence quotidienne, aucune astreinte | Section 8.1 | — | `travaux/strategie-retenue.md:395, 651` |
| 10 | On ne parle pas pour Medhi ; aucune recommandation sur ses œuvres | Section 8.5 | — | `travaux/strategie-retenue.md:635` |
| 11 | Le rendez-vous ne devient pas un cadrage gratuit : pas d'analyse ni de conseil sur ses projets, pas de document promis en plus du récapitulatif et de la proposition | « C'est exactement ce que le cadrage vous apportera. » | — | `travaux/strategie-retenue.md:123` |
| 12 | Aucune information sur les autres activités de Morgan, ses autres entreprises, nos revenus, notre apport | « Nous réservons pour vous une capacité écrite, et nous la mesurons chaque mois. » | — | `travaux/strategie-retenue.md:788` ; 11-proposition-commerciale-revisee.md, section 4.2, objection 18 |
| 13 | Aucun enregistrement, aucune transcription par un outil d'IA | — | — | Section 3 |
| 14 | Toujours « GianLuca » ; si une pièce au prénom erroné ressort, une correction sobre | « Une de nos lettres comportait une erreur sur votre prénom ; nous vous prions de nous en excuser. » | — | `travaux/strategie-retenue.md:812` ; annexes/correction-identite.md |

> **Écart avec la stratégie retenue : pas de signature en séance.**
> *Ce que dit la stratégie.* L'étape du rendez-vous prévoit « entité, signataire, valideur ; lettre d'intention ou bon de commande du cadrage, signé au nom de « Marwin Tech, SAS en formation » » (`travaux/strategie-retenue.md:452`). Elle ne dit pas si la signature a lieu pendant le rendez-vous.
> *Ce que ce livrable retient [PR, ce livrable].* Rien n'est signé pendant la séance. Le document part sous 48 heures, pour une signature à distance.
> *Pourquoi.* 1) Un contrat conclu hors de l'établissement de Marwin avec une société de 5 salariés au plus, dont l'activité principale ne couvre pas ce service, pourrait ouvrir 14 jours de rétractation et interdire tout paiement avant 7 jours [HY] (art. L221-3 du Code de la consommation, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226882, consulté le 4 nov. 2026 selon 12-gouvernance-contrat-sortie.md, section 11.6) ; on ignore encore si la signature à distance juste après une visite suffit à l'écarter (même livrable, section 17, question 7). 2) L'aide régionale exige le dépôt du dossier avant la signature [DR] (`travaux/strategie-retenue.md:239, 453`). 3) Le bon de commande suppose un contrat-cadre relu par l'avocat (`travaux/strategie-retenue.md:666` ; 08-feuille-de-route.md, section 7.2).
> *Limite.* Quelques jours de délai, et un risque que son élan retombe [HY]. Si la société compte 5 salariés au plus, le délai de 7 jours s'applique de toute façon avant l'encaissement (12-gouvernance-contrat-sortie.md, section 11.6, encadré).
> *Décision.* Morgan et Mathys valident cette règle la veille ; l'avocat tranche la question de la rétractation avant le premier encaissement.

---

## 10. Ce qu'il faut noter avant de partir

### 10.1 Fiche à remplir (Mathys)

Règle de notes : les paroles de GianLuca entre guillemets, telles qu'il les dit. Tout est [DR] jusqu'à sa confirmation écrite. Sa confirmation prouve sa position, pas les faits qu'il affirme (patrimoine, rachats, trésorerie).

| N° | Rubrique | Ce qu'on note | Ce que cela déclenche |
| --- | --- | --- | --- |
| 1 | Participants, date, lieu, mode (chez lui ou à distance) | Noms et rôles | Le lieu compte pour la question « hors établissement » [HY] |
| 2 | Société qui signe | Dénomination, forme, SIREN (relu chiffre par chiffre), signataire habilité, effectif | Registres publics ; règle des 7 jours si 5 salariés au plus |
| 3 | Payeur et valideur | Société, personne | Bon de commande ; réception |
| 4 | Autres sociétés citées | Nom et projet porté | Fiches de mission ultérieures |
| 5 | Interlocuteur quotidien et canal | Nom, rôle, moyen d'échange préféré ; présence attendue | Conditions de démarrage |
| 6 | Trois priorités | Dans ses mots, dans son ordre, avec ce qu'elles lui coûtent | Contenu du cadrage |
| 7 | Paiement | Habitudes, délai, TVA récupérée ou non, enveloppe évoquée | Calendrier ; prix TTC à mettre en avant |
| 8 | Aide régionale | Oui, non, ne sait pas | Ordre dépôt, signature, acompte |
| 9 | Ventes d'œuvres (si priorité) | Structure vendeuse, œuvres et artistes disponibles, prix, conseil fiscal, appelant, contrat et outil de Quali Contact | Préalables du pilote commercial |
| 10 | Fichier de prospection | Veut-il l'exploiter ? Quelle société en serait responsable ? | Rôles RGPD ; à transmettre au conseil |
| 11 | Lieux | Noms et statut (acquis, en cours, souhaité), exploitant si connu | Inventaire du cadrage |
| 12 | Réaction au cadrage | Oui, version réduite, un seul sujet, non, « je réfléchis » ; objections mot à mot | Suites (section 11.2) |
| 13 | Ce qu'il a vu ou compris de nos anciens documents ; promesses qu'il croit avoir reçues | Mot à mot | Correction écrite si besoin |
| 14 | Sujets hors périmètre qu'il a soulevés | Bureaux, emploi, capital, STRATES, Medhi, fiscalité : mot à mot, avec notre réponse | Décisions entre associés, jamais en séance |
| 15 | Ses conseils | Expert-comptable, avocat : noms | Dossiers à préparer pour eux |
| 16 | Nos engagements pris en séance | Quoi, pour quand | Récapitulatif |
| 17 | Prochaine étape | Date de l'engagement écrit ; date du prochain contact ; dates de janvier | Jalons du 15 déc. et du 31 janv. |

### 10.2 Avant de se lever

1. Morgan récapitule à voix haute trois à cinq points : société, réponse au cadrage, interlocuteur, prochaines dates.
2. Mathys relit le nom exact et le SIREN de la société.
3. On demande son accord pour lui envoyer un récapitulatif écrit, et l'adresse à utiliser.
4. On confirme ce que nous lui enverrons, et quand.
5. On vérifie que rien n'a été signé ni promis hors de la section 9.

---

## 11. Suites dans les 48 heures

Si le rendez-vous a lieu un jeudi ou un vendredi, compter deux jours ouvrés.

### 11.1 Pour tous les cas

| Délai | Action | Qui | Preuve |
| --- | --- | --- | --- |
| Dans l'heure | Bilan à deux, 20 à 30 minutes : fiche complète ; écarts avec ce qui était prévu ; points à trancher | Les deux | Fiche datée |
| Le jour même | Registre interne des décisions mis à jour. Toute question sur l'incident ou sur les données est transmise au conseil. S'il apparaît que sa société est responsable du traitement des données du fichier, elle doit être informée sans délai [HY] (`travaux/syn-portefeuille.md:354`) | Mathys | Message au conseil |
| Sous 24 h | E-mail récapitulatif à GianLuca : ce que nous avons compris (cinq points au plus), ce qui est convenu, ce que nous attendons de lui, les prochaines étapes, une demande de confirmation par retour. Aucun contenu interne ; aucun prix autre que ceux de la proposition | Morgan rédige ; Mathys relit | E-mail envoyé |
| Sous 48 h | Société nommée : consultation des registres publics, sans contact (statut actif, dirigeant habilité, comptes déposés, procédures collectives) | Morgan | Note interne datée (`travaux/strategie-retenue.md:566`) |
| Sous 48 h | Toute demande hors de l'échelle ou des règles : décision à deux, réponse écrite | Les deux | Réponse envoyée |
| Sous 48 h | Mise à jour de 14-registre-risques-inconnues-decisions.md : les hypothèses qu'il a confirmées ou infirmées remplacent les paramètres de jugement (`travaux/strategie-retenue.md:502`) | Mathys | Registre daté |

### 11.2 Selon sa réponse

| Cas | Suites dans les 48 heures | Ensuite |
| --- | --- | --- |
| **A. Oui au cadrage, société nommée** | Document d'engagement envoyé pour signature à distance : bon de commande au nom de « Marwin Tech, SAS en formation » si le contrat-cadre est relu, sinon lettre d'intention. S'il veut l'aide régionale, on attend le dépôt de son dossier avant toute signature | Immatriculation dès l'engagement écrit ; RC professionnelle avant la première prestation ; K-bis et attestation de vigilance avant la facture d'acompte ; démarrage à l'encaissement, et pas avant J+7 si sa société compte 5 salariés au plus (`travaux/strategie-retenue.md:451-458, 552-554` ; 08-feuille-de-route.md, jalon 5) |
| **B. Oui de principe, société non nommée** | Récapitulatif avec la demande : nom, SIREN, signataire, à une date convenue (au plus tard le 11 déc.) | Aucun travail. Sans réponse au 15 déc. : report à janvier, sans production (`travaux/strategie-retenue.md:697`) |
| **C. Version réduite ou un seul sujet** | Proposition écrite après décision à deux : version réduite (11-proposition-commerciale-revisee.md, section 3.2) ou lot direct avec ses préalables écrits | Mêmes règles d'engagement que le cas A |
| **D. « Je réfléchis » ou « je vois avec mon expert-comptable »** | Récapitulatif et proposition renvoyée ; une relance unique au bout de 5 jours ouvrés | Jalon du 15 déc. ; silence ne vaut pas accord (`travaux/strategie-retenue.md:603`) |
| **E. Non** | E-mail courtois de remerciement ; liste de ce qui lui revient, envoyée après l'avis sur les rôles RGPD | Report sans date ; temps réorienté (`travaux/strategie-retenue.md:698, 701`) |
| **F. Rendez-vous difficile** (incident, colère, demande hors des lignes rouges) | Bilan le jour même ; réponse écrite après avis du conseil si l'incident est en cause | Revoir les conditions de validité de la stratégie (`travaux/strategie-retenue.md:51-58`) |

---

## 12. Recommandations : preuve, hypothèse, limite, décision

| Recommandation | Preuve | Hypothèse | Limite | Décision correspondante |
| --- | --- | --- | --- | --- |
| Ne fixer la date qu'après les prérequis 1 à 7 | Conditions de démarrage (`travaux/strategie-retenue.md:660-662`) ; message de recadrage avant tout rendez-vous (`travaux/strategie-retenue.md:58`) | GianLuca accepte d'attendre jusqu'à fin novembre [HY] | Il peut appeler avant ; la relation peut se refroidir | Jalon 3 de 08-feuille-de-route.md (19 au 27 nov.) ; réponse de la section 2.3 |
| Viser la société et une réponse au cadrage, pas une signature | Aucune société payeuse [FV négatif] (`travaux/syn-portefeuille.md:101-102`) ; ancien objectif centré sur la formule [FV] (`interne/contexte-projet-carlone.md:102`) | Une réponse claire est possible en une séance [HY] | Il peut devoir consulter son expert-comptable | Jalon du 15 déc. (`travaux/strategie-retenue.md:697`) |
| Rien signé en séance ; engagement à distance sous 48 h | Règle de L221-3 limitée au hors établissement [FV] (12-gouvernance-contrat-sortie.md, section 11.6) ; aide régionale à déposer avant signature [DR] | La signature à distance suffit à écarter la règle [HY] | L'avocat n'a pas tranché ; quelques jours de délai | Question 7 à l'avocat (12-gouvernance-contrat-sortie.md, section 17) ; délai de 7 jours si 5 salariés au plus |
| Morgan mène, Mathys présent ; aucune concession en séance | Prix et remises à l'unanimité (`travaux/strategie-retenue.md:614`) ; Mathys titulaire présumé du dépôt (`travaux/strategie-retenue.md:173`) | Mathys est disponible [IN] | Une JP de plus non facturable [ES] ; trajet [IN] | Fiche des disponibilités du 19 nov. (`travaux/strategie-retenue.md:717`) |
| Questions d'abord, proposition vers la 60e minute, 30 minutes finales protégées | Aucune parole directe [FV négatif] (`travaux/syn-portefeuille.md:88-90`) ; offre née du côté de Marwin, pas d'une demande du client (`travaux/syn-portefeuille.md:156-162`) | Il parle librement de ses priorités [HY] | Il peut exiger le prix d'emblée : on le donne aussitôt | Répétition la veille (section 3.1) |
| Récapitulatif écrit sous 24 h, à faire confirmer | Première parole directe du dossier ; les dix questions bloquantes (`travaux/strategie-retenue.md:723-737`) | Il répond par écrit [HY] | Sa confirmation ne prouve ni sa solvabilité ni ses biens | Morgan envoie, Mathys relit ; registres publics sous 48 h (`travaux/strategie-retenue.md:566`) |

---

## 13. Limites

- **Aucune parole directe de GianLuca** n'existe dans les pièces (`travaux/syn-portefeuille.md:88-90`). Ses réactions, ses objections et ses priorités sont des hypothèses. Ce livrable prépare des réponses ; il ne prédit pas la conversation.
- **Ce qu'il a vu ou reçu est inconnu** (`travaux/ex-C2-offre.md:221`). La réponse de Morgan à la question n° 9 peut changer le prix d'ouverture, la phrase sur le prénom et la question des « vingt jours ».
- **L'état de la fuite n'a pas été revérifié** par cet audit (`travaux/note-point-4-novembre-et-activites.md:23`). Tout le calendrier suppose une décision prise avant l'échéance du 5 nov., ou un retard motivé.
- **Les points juridiques marqués [HY]** (rétractation, signature personnelle, rôles RGPD) restent à trancher par l'avocat ou le DPD (`travaux/strategie-retenue.md:839`).
- **Les références fiscales** de la section 8.8 ont été relevées par l'audit le 4 nov. 2026 (`travaux/rj-R2-fiscal.md:95-102`) ; elles n'ont pas été rouvertes en ligne pour ce livrable. Elles informent ; elles ne remplacent pas l'avis du conseil fiscal de GianLuca.
- **La collecte est incomplète** : 169 conversations ChatGPT lues sur 219. Des promesses faites au client peuvent exister hors du corpus (`travaux/strategie-retenue.md:835`).
- **Les dates** supposent le scénario central de 08-feuille-de-route.md ; dans le scénario prudent, le rendez-vous glisse en janvier 2027.
- Ce livrable n'a contacté personne et n'a modifié aucune autre pièce.

Relu et contrôlé le 4 novembre 2026 : 90 vérifications, 16 corrections.
