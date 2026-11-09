# Processus IA prioritaires et protocoles d'essai

Audit Marwin Tech × GianLuca Carlone · livrable 7 sur 15 · 4 novembre 2026
Statut : interne (ne pas transmettre à GianLuca Carlone). Les protocoles d'essai (section 6), la grille de sécurité (section 8) et la liste de restitution (section 11) peuvent servir de base à une annexe contractuelle, après accord écrit des deux associés et après retrait des coûts, des JP, des seuils de rentabilité, des marges, des démonstrateurs internes et de toute mention de Medhi, BOJ.ART, STRATES, du laboratoire ou de l'incident de données hors des termes validés par le conseil (`travaux/strategie-retenue.md:783-797`).
Sources principales : `travaux/syn-capacite-ia.md` (sections 5, 6 et 8) ; `travaux/rj-R4-donnees-ia.md` et `travaux/ver-R4-donnees-ia.md` ; `travaux/rj-R6-marche.md` (partie d) et `travaux/ver-R6-marche.md` ; `travaux/strategie-retenue.md` (sections 4.7, 4.13 et 9) ; `modele-financier/stress-tests.md` ; pièces d'origine du dépôt Momolscode/Carlone (commit 7b46602), rouvertes en lecture seule.
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu. JP : journée-personne de 7 h ; deux personnes présentes une journée consomment 2 JP. **Coût interne d'une JP : 700 à 900 € [ES]**, arrondi du coût complet calculé pour 10 JP facturées par mois (710 à 885 €, `travaux/strategie-retenue.md:365`). Dollars convertis au taux BCE du 4 nov. 2026 (1 € = 1,1267 $, `travaux/rj-R6-marche.md:377`).

**Ce que ce livrable ajoute** : une fiche complète pour chacun des onze processus de la demande ; une comparaison chiffrée des cinq options ; le coût complet sur douze mois des automatisations retenues, avec le temps qu'il faudrait gagner pour les rembourser ; les protocoles des quatre essais, rattachés aux offres qui les financent ; les règles de sécurité, de données, de continuité et de restitution propres à l'IA ; une position argumentée sur la DGX Spark, le laboratoire et les architectures multi-agents.

**Ce qu'il ne refait pas** : la capacité des associés et les seuils de saturation (06-fonctionnement-a-deux.md) ; les prix, marges et règles de facturation des offres (04-catalogue-offres.md) ; le calendrier (08-feuille-de-route.md) ; la trésorerie et les tests de résistance (09-modele-economique-tresorerie.md) ; les clauses du contrat, la délégation et la sortie (12-gouvernance-contrat-sortie.md) ; le registre des risques (14-registre-risques-inconnues-decisions.md).

**Méthode.** J'ai relu les sections demandées des travaux de l'audit et rouvert, pour chaque point déterminant, la pièce d'origine du dépôt (lignes citées). Les pages officielles (ANSSI, CNIL, CERT-FR, OWASP, liste du Data Privacy Framework, pages de prix des éditeurs) ont été consultées le 4 nov. 2026 par les chercheurs de l'audit et contrôlées par un second lecteur ; je ne les ai pas rouvertes moi-même et je les cite avec leur URL et le fichier de travail qui les rapporte. Les coûts ont été recalculés ici ; ce sont tous des estimations [ES] à remplacer par des mesures dès le premier mois.

---

## 0. L'essentiel

1. **Aucun gain de l'IA n'est mesuré aujourd'hui** [IN]. Les pièces montrent du volume produit, pas des résultats acceptés : un CRM de 500 fiches dont 283 numéros sur 471 restent « à confirmer », une seule date de vérification et aucun appel [FV] (`travaux/ex-C5-crm.md:39-40, 49`) ; une cible de −30 % de temps jamais mesurée (`sources/chatgpt-pages/2026-11-04-complement/marwin-structure-et-offres.md:122`).
2. **Aucun des onze processus ne justifie un développement spécifique.** Tous partent d'une organisation simple et d'outils existants bien configurés, avec l'IA en assistance contrôlée. Une intégration légère n'est envisagée qu'après essai, sur une partie étroite : surtout la recherche documentaire et la détection des incohérences (essais P3 et P4), puis le résumé hebdomadaire du registre et l'échange de fichiers du CRM si Quali Contact est engagé (tableau 3.0) [PR] (`travaux/syn-capacite-ia.md:654-666`).
3. **Rien n'est automatisé au départ.** Seuls les rappels internes, le résumé hebdomadaire et les contrôles déterministes (dates, montants, doublons) peuvent l'être après essais. Toute action vers l'extérieur (envoi, appel, modification du CRM, dépense) reste soumise à une approbation humaine [PR].
4. **Le coût réel est le temps humain, pas l'abonnement.** Les outils coûtent 150 à 400 € par mois à Marwin dans le scénario central (`travaux/strategie-retenue.md:505`). Le registre des décisions, par exemple, coûte environ 4 000 à 10 500 € sur douze mois en conception, maintenance, restauration, formation et sortie [ES] : il faudrait gagner 0,5 à 0,9 JP par mois pour le rembourser en temps. **La première année, il se justifie par la qualité et la traçabilité, pas par une économie de temps** (section 5).
5. **Quatre essais, financés différemment** [PR] : démonstrateurs internes (registre, recherche documentaire, en option contrôle des incohérences) payés par Marwin, plafonnés à 8 JP avant le 2 février 2027 ; un seul pilote client, dans la voie choisie par GianLuca après le cadrage : registre et comptes rendus dans le socle pilote (voie b) ou l'outillage (voie c), qualification du CRM dans le pilote commercial (voie a) (section 6.0).
6. **Temps économisé, capacité libérée et économie réelle sont trois choses différentes.** Au premier trimestre, la capacité libérée est négative. Pour GianLuca, il n'y a d'économie réelle que si une dépense qu'il paie disparaît (section 6.7).
7. **Aucune donnée personnelle réelle avant les préalables** : fuite traitée, responsable du traitement désigné, contrat de l'article 28, offres professionnelles avec clauses types et analyse d'impact des transferts. Anthropic et OpenAI ne figurent pas sur la liste du Data Privacy Framework au 4 nov. 2026 [MM] (`travaux/ver-R4-donnees-ia.md:25`).
8. **La grille de sécurité de l'ANSSI (30 oct. 2026) s'applique avant toute automatisation** : entrées traitées comme des données, trois classes d'actions, approbation hors de portée de l'agent, plafonds de coût, journal inaltérable, arrêt testé (section 8).
9. **La réversibilité promise n'est pas tenable aujourd'hui** : le CRM est sur les comptes des associés (`crm/docs/rapport/rapport-crm-hermes360.md:19`). Il faut ouvrir les comptes au nom du client dès le premier jour et tester une sortie à blanc au mois 6 (section 11).
10. **Non à la DGX Spark, au laboratoire et aux architectures multi-agents pour GianLuca la première année.** Aucun usage démontré, aucun financeur, et nos propres archives ne les ont jamais validés (section 12).

---

## 1. Point de départ

### 1.1 Ce que montrent les pièces : produire n'est pas livrer

| Réalisation | Volume produit | Résultat constaté | Source |
| --- | --- | --- | --- |
| CRM Nièvre, produit par des agents IA du 22 au 30 oct. 2026 | 500 fiches ; 645 fichiers | 283 numéros sur 471 « à confirmer » ; date de vérification renseignée pour 1 fiche sur 500 ; aucun champ de suivi ; aucun appel ni vente ; dépôt public [FV] | `travaux/ex-C5-crm.md:39-40, 49` ; `travaux/ver-C5-crm.md:25` ; `interne/audit-marwin-tech-carlone.md:15` |
| Mémoire documentaire du dépôt BOJART | 1 260 recherches sur 14 questions de test | Restauration réussie dans un dossier neuf [MM] ; la bonne source n'est transmise au modèle que dans 71,4 % des cas à 8 000 octets [MM] ; régressions quand on ajoute des documents [FV] | `travaux/ex-C7-jarvis.md:47-49` ; `travaux/ver-C7-jarvis.md:63` |
| Prospection OLSEN de Morgan | 36 propositions, 72 brouillons d'e-mails, 503 prospects | Aucun envoi [DR] | `travaux/note-point-4-novembre-et-activites.md:9` |
| Console « Offres et missions » | Module contrôlé sur données fictives | « La comparaison de productivité reste à réaliser » ; la cible de −30 % « reste un objectif » [FV] | `sources/chatgpt-pages/2026-11-04-complement/marwin-structure-et-offres.md:120-122` |
| Offre Carlone | Sept états du 25 oct. au 4 nov. | 24 contradictions confirmées ; décision du 4 nov. appliquée à 1 support sur au moins 5 [FV] | `travaux/syn-capacite-ia.md:617, 782` |

**Conclusion** [HY] : la contrainte n'est pas la production. Elle est en aval : vérification, décision du client, réception, adoption. Un essai qui ne mesure que la vitesse de production ne prouve rien.

### 1.2 Nos propres règles existent déjà

Les archives de Marwin contiennent déjà la bonne méthode [FV, textes de propositions non appliquées] :
- « Pour chaque automatisation, décrire le déclencheur, les données autorisées, le résultat attendu et les erreurs possibles. […] Prévoir journal, prévention des doublons, contrôle humain adapté, arrêt et retour au fonctionnement manuel. » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:111`)
- « Mesurer le temps total, les corrections, les erreurs résiduelles et le coût par résultat accepté. » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:113`)
- « Les connecteurs et systèmes autonomes doivent être éprouvés dans leur environnement réel avant d'être vendus comme opérationnels. » (`sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md:63`)
- « Pour le premier cas documentaire, viser 30 % de réduction du temps total sans erreur critique […] abandonner en cas de confusion de données ou de coût injustifié. » (`interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf p. 11`)

Le CRM a pourtant été construit avant tout contrat et sans ces règles. Ce livrable transforme ces principes en protocoles chiffrés.

---

## 2. Règles communes à tous les processus

### 2.1 Préalables [PR]

| Règle | Contenu | Source |
| --- | --- | --- |
| Données autorisées | Aucune donnée personnelle réelle avant : décision sur la fuite, responsable du traitement désigné, contrat de l'article 28, registre, information des personnes, offre d'IA professionnelle avec clauses types et analyse d'impact des transferts. Avant : données fictives, ou corpus filtré (encadré de la section 6.0) | `travaux/strategie-retenue.md:669` ; `travaux/syn-capacite-ia.md:319` |
| Offres d'IA | Professionnelles seulement (API, Team, Business, Enterprise), entraînement désactivé, comptes au nom de Marwin ou de l'entité cliente, jamais sur un compte personnel | `travaux/rj-R4-donnees-ia.md:350, 405` |
| Classement des actions | **Autonome** : lire, chercher, résumer, proposer. **Approbation humaine** : envoyer, appeler, modifier le CRM, publier, engager une dépense. **Interdit** : payer, supprimer en masse, changer des droits | `travaux/rj-R4-donnees-ia.md:479` (ANSSI, principe 3) |
| Documents = données | Toute instruction trouvée dans un document est signalée, jamais exécutée | `travaux/rj-R4-donnees-ia.md:478` ; exemples réels : `crm/PASSATION.md:32, 34, 38` |
| Calculs | Montants, sommes et dates calculés par formule, jamais par le modèle de langage. Toute formule fiscale est validée par un professionnel : le simulateur du CRM applique un taux d'IS fixe de 25 % sans limite par le bénéfice (`crm/art_merge.py:19, 129`) [FV] ; pour une entreprise qui fait 130 000 € de bénéfice, il affiche 1 043 750 € d'« économie max » sur cinq ans, alors que l'impôt en moins ne peut guère dépasser 32 500 € par an pour elle [ES] | `travaux/ver-C5-crm.md:19` |
| Mesure | Temps humain total (préparation, exécution, contrôle, corrections, reprises) ; erreurs restantes ; coût par résultat accepté ; cas d'échec conservés ; essais refaits à chaque changement d'outil, de modèle ou de source | `sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md:69` |
| Comptes et coûts | Outils du client ouverts à son nom et payés par lui ; Marwin n'avance aucun achat ni abonnement | `travaux/strategie-retenue.md:188-189` |
| Responsable | Chaque processus a un responsable, un suppléant et une fiche de secours manuel testée | `travaux/syn-capacite-ia.md:862` |

### 2.2 Les cinq modes et les cinq options

**Modes de prise en charge** (`travaux/DEMANDE.md`, § 6) : (a) automatisation envisageable après essais ; (b) travail assisté par IA avec contrôle humain ; (c) intervention humaine spécialisée ; (d) coordination d'un prestataire ; (e) activité exclue de notre périmètre.

**Options comparées** (`travaux/syn-capacite-ia.md:327-332`) :
1. **Actuel** : ce qui existe aujourd'hui.
2. **Organisation simple** : règles, modèles, rituels, sans outil nouveau.
3. **Outils existants configurés** : assistant professionnel, tableur, Notion ou Airtable, CRM existant hébergé correctement.
4. **Intégration légère** : scripts ou automatismes simples (export, import, n8n), avec journal et arrêt.
5. **Développement spécifique** : outil construit pour GianLuca.

L'option 2 est un **préalable** aux options 3 à 5 : un outil ne corrige pas un registre qui n'est pas tenu.

---

## 3. Les onze processus

### 3.0 Vue d'ensemble [PR]

| N° | Processus | Mode | Option retenue | Offre qui le porte | Responsable | Priorité |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Recherche dans les documents | (b) | 2, puis 3 ; 4 sous conditions | Interne ; exploitation (offre D) au plus tôt au mois 7 | Mathys (outil) | Démonstrateur |
| 2 | Réunions et comptes rendus | (b) | 2 + 3 ; 4 au mois 6 au plus tôt | Socle de pilotage (B0, B1) ; outillage (C6) | L'associé qui anime | Pilote |
| 3 | Tâches, échéances, décisions | (a) pour les rappels internes et le résumé ; (b) pour le reste | 2 + 3 ; 4 pour le seul résumé | Socle ; C6 | Morgan (contenu), Mathys (outil) | Pilote |
| 4 | Budget et rapprochements | (b) + calcul déterministe + (c) expert-comptable | 2 + 3 | Socle (suivi budgétaire préparatoire) ; étude C7 | Mathys ; l'expert-comptable du client valide | Après le cadrage |
| 5 | Mise à jour et qualification du CRM | (b) ; (a) pour les contrôles de format et de doublons ; contact sortant humain | Mise en conformité, puis 2, puis 3 ; 4 si Quali Contact est engagé | Pilote commercial (C2) ; échange de fichiers (C5) ; exploitation (D) | Mathys ; responsable du traitement [IN] | Pilote, après conformité |
| 6 | Campagnes et supports commerciaux | (b) ; envoi approuvé | 2 + 3 ; 4 après le pilote commercial | C2 (script) ; kit C8 | Morgan | Après C2 |
| 7 | Rédaction et production de contenus | (b) ; (c) photographe | 2 + 3 | Lots devisés | Morgan | Par lot |
| 8 | Coordination des prestataires | (d), préparée avec l'IA | 2 + 3 | Socle, sous mandat écrit | Morgan (relation), Mathys (registre) | Selon les projets |
| 9 | Préparation administrative pour les professionnels | (b), puis (c) | 2 + 3 | Socle ; dossiers C3, C4, C7 | Morgan | Selon les besoins |
| 10 | Détection des incohérences et retards | (a) pour le déterministe ; (b) pour le sémantique | 2 + 3 ; 4 en essai facultatif | Interne, jamais facturé | Mathys (outil), Morgan (tri) | Démonstrateur facultatif |
| 11 | Capitalisation des méthodes | (b) | 2 + 3 | Interne, non facturé | Chacun ; Mathys tient la bibliothèque | Continu |

**Activités exclues (mode e)** [PR] (`travaux/strategie-retenue.md:650-653` ; `travaux/syn-capacite-ia.md:668`) : exécution administrative courante ; tenue de la comptabilité ; conseil juridique ou fiscal ; appels sortants par agent vocal ; tout outil d'IA de recrutement, de notation ou d'évaluation des personnes ; toute action financière par un agent ; démarchage multi-agents de type OLSEN ; simulateur d'« économie d'impôt » tant qu'il n'est pas corrigé et validé par un professionnel.

### 3.1 Recherche dans les documents

| Canevas | Contenu |
| --- | --- |
| Besoin | Retrouver vite une information sourcée (décision, montant, version, engagement) dans un corpus dispersé : dépôt, artefacts, pages ChatGPT, messagerie. L'inventaire n'a lu que 169 conversations sur 219 (`travaux/DEMANDE.md`, § 1) |
| Entrée | Question en langage courant ; corpus autorisé, daté, avec le statut de chaque pièce (proposition, décision, archive) |
| Données autorisées | Documents internes et documents du client couverts par le mandat. **Exclus** : `crm/`, `sources/archives-crm/` et toute pièce avec des coordonnées de prospects, tant que les préalables ne sont pas réunis (encadré de la section 6.0) |
| Traitement | Recherche plein texte et assistant professionnel ; réponse avec citation chemin:ligne ou page ; liste des versions concurrentes ; refus explicite si aucune source |
| Intervention humaine | Relecture de toute réponse qui sert à une décision, un prix, un engagement ou un document remis au client |
| Contrôle | Ouverture de la citation ; vérification de la date et du statut de la pièce ; jeu de 60 questions rejoué après chaque ajout d'au moins 10 documents ou changement de modèle |
| Sortie | Réponse courte, citations, avertissement sur les versions |
| Résultat à mesurer | Part de réponses justes et correctement citées ; part de refus corrects ; temps entre la question et la réponse vérifiée ; citations inventées (cible : 0) |
| Mode | (b) travail assisté par IA avec contrôle humain |
| Erreurs possibles | Citation inventée ; version récente prise pour une décision approuvée ; bonne source trouvée mais non transmise au modèle (28,6 % des cas à 8 000 octets sur le banc BOJART [MM], `travaux/ex-C7-jarvis.md:49`) ; régression quand le corpus grossit (`travaux/ver-C7-jarvis.md:63`) ; instruction cachée dans un document exécutée ; ancienne orthographe erronée du prénom du client, présente dans environ 300 passages des archives, non reconnue (`travaux/note-point-4-novembre-et-activites.md:26`) |
| Cas exceptionnels | PDF scanné ou image ; visuel non archivé ; question qui demande un jugement ; décision orale jamais écrite |
| Secours manuel | Registre des sources et recherche plein texte (grep) ; question posée à la personne qui détient l'information |
| Responsable | Mathys pour l'outil ; l'auteur de la réponse pour sa vérification ; Morgan pour tout usage client |

### 3.2 Préparation des réunions et comptes rendus

| Canevas | Contenu |
| --- | --- |
| Besoin | Arriver en réunion avec les décisions attendues préparées ; en sortir avec un compte rendu exact, des décisions datées et des actions attribuées |
| Entrée | Registre des décisions et des tâches (processus 3) ; notes ; transcription seulement avec l'accord de tous les participants |
| Données autorisées | Participants informés ; aucun enregistrement sans accord ; données personnelles limitées aux participants et aux sujets traités |
| Traitement | Ordre du jour tiré des décisions ouvertes et des échéances proches ; brouillon de compte rendu ; extraction « décision, responsable, échéance, source » |
| Intervention humaine | L'animateur relit et corrige ; GianLuca ou son délégué confirme les décisions. Le silence ne vaut pas approbation (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:103`) |
| Contrôle | Chaque décision a un responsable, une date et une source ; comparaison entre le compte rendu et le registre ; aucune décision ajoutée qui n'ait été prise |
| Sortie | Compte rendu d'une page ; registre mis à jour |
| Résultat à mesurer | Délai d'envoi (cible : moins de 24 h ouvrées) ; part des décisions complètes (cible : 100 %) ; corrections demandées ; temps humain par réunion |
| Mode | (b) |
| Erreurs possibles | Décision inventée ou mal attribuée ; nuance perdue (« à étudier » devenu « décidé ») ; information confidentielle envoyée à la mauvaise liste ou collée dans un outil grand public |
| Cas exceptionnels | Réunion informelle ou téléphonique sans notes ; participant qui refuse l'enregistrement ; décision contredite la semaine suivante |
| Secours manuel | Modèle de compte rendu rempli à la main |
| Responsable | L'associé qui anime la réunion ; l'autre associé contrôle (quatre yeux) |

### 3.3 Suivi des tâches, échéances et décisions

| Canevas | Contenu |
| --- | --- |
| Besoin | Une seule vue fiable de ce qui est décidé, en cours, bloqué ou en retard, par projet |
| Entrée | Comptes rendus ; demandes du client ; échéances contractuelles et réglementaires |
| Données autorisées | Données de pilotage ; données personnelles réduites au nom des responsables |
| Traitement | Registre à cinq états (à qualifier, cadrée, en réalisation, en réception, close : `sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md:65`) ; détection des échéances proches ou dépassées par règles de dates ; résumé hebdomadaire |
| Intervention humaine | Chaque responsable met à jour ses tâches ; GianLuca arbitre les priorités ; toute relance externe est approuvée |
| Contrôle | Revue hebdomadaire ; chaque tâche a un responsable, une échéance et un critère de réception |
| Sortie | Tableau de bord ; liste des décisions attendues ; relances préparées |
| Résultat à mesurer | Retards détectés avant l'échéance ; délai moyen des décisions ; part des tâches avec critère de réception ; échéances manquées |
| Mode | (a) pour les rappels internes et le résumé (actions de la classe « autonome ») ; (b) avec approbation pour toute relance externe |
| Erreurs possibles | Registre non tenu (cause principale d'échec) ; doublons ; relance envoyée à tort ; mauvaise date ou mauvais fuseau |
| Cas exceptionnels | Changement de priorité en cours de mois ; tâche sans responsable ; tiers qui ne répond pas |
| Secours manuel | Tableau imprimable et revue orale hebdomadaire |
| Responsable | Morgan pour le registre client ; Mathys pour l'outil |

### 3.4 Préparation budgétaire et rapprochement des informations

| Canevas | Contenu |
| --- | --- |
| Besoin | Savoir, par projet, ce qui est budgété, engagé, facturé et payé, et repérer les écarts avant qu'ils coûtent |
| Entrée | Devis, bons de commande, factures, budgets ; exports comptables en lecture seule |
| Données autorisées | Sous mandat écrit ; lecture seule ; **jamais d'identifiants bancaires confiés à un agent** |
| Traitement | Extraction des montants des PDF vers un tableur (IA, avec contrôle) ; rapprochements et sommes par formules ; liste des écarts |
| Intervention humaine | Vérification de chaque ligne au-delà d'un seuil ; validation par l'expert-comptable de tout ce qui touche à la comptabilité ou à la fiscalité |
| Contrôle | Totaux recalculés ; contrôle croisé HT, TVA et TTC ; unicité des factures ; tolérance zéro sur les montants |
| Sortie | Tableau budget, engagé et payé par projet ; liste des écarts et des décisions à prendre |
| Résultat à mesurer | Erreurs de montant découvertes après coup (cible : 0) ; délai de production ; écarts signalés avant dépassement |
| Mode | (b) pour l'extraction, calcul déterministe, puis (c) expert-comptable |
| Erreurs possibles | Confusion HT et TTC ; honoraires et achats mélangés (les 30 000 € de l'option laboratoire mêlaient 13 500 € d'honoraires et 16 500 € d'achats, `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf p. 8`) ; facture en double ; mauvaise entité |
| Cas exceptionnels | Entité payeuse inconnue [IN] ; devis non signé ; devise étrangère ; avoir |
| Secours manuel | Saisie manuelle dans le tableur |
| Responsable | Mathys pour la préparation ; l'expert-comptable du client pour la validation |
| Frontière | Marwin prépare et rapproche ; elle ne tient ni la comptabilité ni la trésorerie (`travaux/strategie-retenue.md:187`) |

### 3.5 Mise à jour et qualification du CRM

| Canevas | Contenu |
| --- | --- |
| Besoin | Des fiches d'entreprises exactes, datées et appelables pour vendre des œuvres aux entreprises |
| Entrée | 500 fiches (485 en campagne) ; sources publiques ; retours d'appels |
| Données autorisées | **Après la mise en conformité seulement.** Données professionnelles liées à la fonction ; liste d'opposition ; opposition Sirene. Entrepreneurs individuels, artistes et lignes personnelles exclus jusqu'à l'avis de l'avocat (`travaux/syn-droit.md:645`) |
| Traitement | Recherche assistée ; dédoublonnage ; datation de chaque champ ; export au format de l'appelant ; réimport des résultats d'appel |
| Intervention humaine | Validation d'un échantillon ; traitement des oppositions ; décision humaine sur tout nouveau contact nominatif ; tout appel ou e-mail est passé par une personne |
| Contrôle | Échantillon appelé ; numéros partagés signalés (34 numéros pour 73 fiches [FV], `travaux/ex-C5-crm.md:41`) ; date de vérification renseignée |
| Sortie | Fiches qualifiées avec source et date ; fichier d'appel au format de l'appelant |
| Résultat à mesurer | Joignabilité au premier appel ; part des fiches datées ; doublons ; oppositions respectées (cible : 100 %) ; temps humain par fiche acceptée |
| Mode | (b) ; (a) pour les contrôles de format et de doublons après essais ; tout contact sortant est humain |
| Erreurs possibles | Numéro faux (283 sur 471 « à confirmer ») ; résultat rattaché à la mauvaise entreprise ; argument fiscal surévalué (section 2.1) ; entreprise opposée contactée (« les entreprises opposées à la prospection sur Pappers restent appelables », `crm/PASSATION.md:22`) ; nouvelle exposition du fichier |
| Cas exceptionnels | Standard de groupe ; holding sans numéro ; procédure collective ; changement de dirigeant |
| Secours manuel | Tableur maître et journal d'appels tenu à la main |
| Responsable | Mathys pour l'outil et les données ; le responsable du traitement est l'entité vendeuse de GianLuca, encore à nommer [IN] |

### 3.6 Préparation des campagnes et supports commerciaux

| Canevas | Contenu |
| --- | --- |
| Besoin | Scripts, e-mails, fiches d'offre et supports conformes et cohérents pour la vente d'œuvres |
| Entrée | Offres validées par GianLuca ; cibles ; arguments fiscaux **validés par écrit** par un professionnel |
| Données autorisées | Segments et caractéristiques d'entreprises ; aucune donnée personnelle nécessaire pour concevoir les supports |
| Traitement | Brouillons et variantes ; contrôle d'une grille de conformité (identité de l'expéditeur, opposition, aucune promesse de rendement, économie d'impôt « sous réserve ») |
| Intervention humaine | Morgan valide le message ; le conseil de GianLuca valide toute affirmation fiscale ; GianLuca valide l'offre et la structure vendeuse |
| Contrôle | Grille de relecture ; essai sur 20 comptes avant tout élargissement |
| Sortie | Kit de campagne versionné |
| Résultat à mesurer | Validation au premier passage ; résultats du pilote commercial (joignabilité, rendez-vous, ventes) [MM à produire] |
| Mode | (b) ; envoi soumis à approbation humaine |
| Erreurs possibles | Promesse fiscale fausse ; mot « mécénat » pour vendre une œuvre (`travaux/strategie-retenue.md:298`) ; structure vendeuse absente du message ; mention des établissements que la passation interdit de citer (`crm/PASSATION.md:31`) ; envoi à une entreprise opposée |
| Cas exceptionnels | GianLuca refuse un argument ; changement d'offre ; artiste qui refuse une mention |
| Secours manuel | Modèles écrits à la main |
| Responsable | Morgan |

### 3.7 Rédaction et production de contenus

| Canevas | Contenu |
| --- | --- |
| Besoin | Textes, visuels, vidéos courtes et dossiers pour la galerie, les événements et les réseaux |
| Entrée | Brief validé ; charte ; droits sur les œuvres et les images |
| Données autorisées | Œuvres et images dont les droits sont acquis ; aucune image de personne sans accord |
| Traitement | Brouillons de textes ; visuels d'intention générés ; montage |
| Intervention humaine | Relecture ; vérification des droits ; artiste consulté pour ses œuvres ; photographe professionnel pour les reproductions d'œuvres, payé par le client |
| Contrôle | Mention « image générée par IA » pour tout visuel réaliste (AI Act, art. 50, § 4, applicable depuis le 2 août 2026, `travaux/syn-droit.md:652, 659`) ; aucun personnage protégé |
| Sortie | Contenus validés et datés |
| Résultat à mesurer | Validation au premier passage ; délai ; incidents de droits (cible : 0) |
| Mode | (b) ; (c) pour la photographie d'œuvres |
| Erreurs possibles | Visuel d'intention pris pour une réalisation ; atteinte aux droits d'un artiste ; refus du fournisseur pour contenu protégé |
| Cas exceptionnels | Œuvre sans accord de l'artiste ; outil de génération arrêté par son éditeur |
| Secours manuel | Production classique ; photographe |
| Responsable | Morgan |

### 3.8 Coordination des prestataires

| Canevas | Contenu |
| --- | --- |
| Besoin | Que les prestataires de GianLuca (Quali Contact, artisans, traiteur, techniciens) livrent à temps, au prix convenu et selon les règles |
| Entrée | Liste des prestataires, devis, contrats, planning |
| Données autorisées | Coordonnées professionnelles ; contrats transmis sous mandat |
| Traitement | Registre des prestataires ; comparatif de devis (extraction par IA, puis contrôle) ; planning ; relances préparées |
| Intervention humaine | Marwin coordonne ; **GianLuca ou son signataire engage** ; aucune commande sans accord écrit ; consignes passées **par l'employeur du prestataire**, jamais en direct à ses salariés (`travaux/strategie-retenue.md:584`) |
| Contrôle | Plafonds par dépense et cumulés ; double validation au-delà d'un seuil |
| Sortie | Planning, comparatifs, comptes rendus de chantier |
| Résultat à mesurer | Livraisons à l'heure ; écarts de prix ; litiges |
| Mode | (d) coordination d'un prestataire, préparée avec l'IA |
| Erreurs possibles | Engagement pris sans autorisation ; Marwin devient l'encadrant de fait des équipes d'un prestataire ; devis mal comparés |
| Cas exceptionnels | Prestataire défaillant ; urgence un soir d'événement ; GianLuca injoignable (l'engagement attend) |
| Secours manuel | Téléphone et tableur |
| Responsable | Morgan (relation) ; Mathys (registre) |

### 3.9 Préparation administrative pour les professionnels compétents

| Canevas | Contenu |
| --- | --- |
| Besoin | Remettre à l'expert-comptable, à l'avocat, à l'assureur ou à la mairie des dossiers complets, pour qu'ils décident vite |
| Entrée | Pièces du client ; liste des exigences publiée par l'administration |
| Données autorisées | Sous mandat ; données minimales |
| Traitement | Listes de pièces ; synthèse ; questions précises ; chaque règle citée avec sa source officielle et sa date |
| Intervention humaine | Le professionnel décide et signe. Marwin ne donne ni conseil juridique ni conseil fiscal (`sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md:61`) |
| Contrôle | Chaque règle vérifiée sur une source officielle datée ; aucune règle tirée de la seule mémoire d'un modèle |
| Sortie | Dossier prêt à transmettre ; liste de questions |
| Résultat à mesurer | Dossiers renvoyés pour pièce manquante ; délai de traitement par le professionnel |
| Mode | (b), puis (c) |
| Erreurs possibles | Règle périmée : plusieurs règles ont changé en 2026 (démarchage téléphonique des consommateurs le 11 août, Omnibus IA le 27 juillet, `travaux/ver-R4-donnees-ia.md:15, 24`) ; règle inventée ; mauvaise entité |
| Cas exceptionnels | Règle en cours de réforme (omnibus du RGPD non adopté) ; administration injoignable |
| Secours manuel | Liste de pièces fournie par le professionnel lui-même |
| Responsable | Morgan ; le professionnel pour la décision |

### 3.10 Détection des incohérences et retards

| Canevas | Contenu |
| --- | --- |
| Besoin | Repérer avant le client les contradictions entre versions (prix, périmètre, calendrier, propriété) et les retards |
| Entrée | Registre ; documents versionnés ; budgets ; CRM |
| Données autorisées | Documents internes et documents du client sous mandat |
| Traitement | Contrôles **déterministes** (échéances dépassées, montants différents pour une même rubrique, statut des versions) ; comparaison **sémantique** assistée, avec citations ; registre « décision → documents touchés » |
| Intervention humaine | Tri de chaque alerte : vraie, fausse, déjà connue |
| Contrôle | Jeu d'essai de contradictions connues |
| Sortie | Liste d'alertes datées, avec citations et proposition de correction |
| Résultat à mesurer | Part des contradictions connues retrouvées ; part d'alertes utiles ; temps de tri |
| Mode | (a) pour le déterministe après essais ; (b) pour le sémantique |
| Erreurs possibles | Fausse assurance (contradiction de prix non vue) ; avalanche d'alertes inutiles ; citation inventée |
| Cas exceptionnels | Pièce non versionnée ; décision orale non écrite (la décision du 4 nov. en est un exemple, `travaux/note-point-4-novembre-et-activites.md:25`) |
| Secours manuel | Revue humaine mensuelle des documents de référence |
| Responsable | Mathys (outil) ; Morgan (tri des alertes qui concernent le client) |

### 3.11 Capitalisation des méthodes

| Canevas | Contenu |
| --- | --- |
| Besoin | Que chaque mission rende la suivante plus rapide, et qu'un associé puisse reprendre le travail de l'autre |
| Entrée | Comptes rendus de mission, erreurs, modèles de livrables, cas de test |
| Données autorisées | Méthodes et modèles **séparés des données confidentielles du client** (`sources/chatgpt-pages/2026-11-04-complement/marwin-methode-consulting-audits.md:73`) ; aucune donnée de GianLuca réutilisée pour la prospection de Marwin (`travaux/strategie-retenue.md:619`) |
| Traitement | Brouillon de procédure ou de modèle rédigé par l'IA à partir des notes ; relecture ; versionnement |
| Intervention humaine | Rédaction finale ; test de la procédure par l'autre associé |
| Contrôle | Une procédure n'est validée que si quelqu'un d'autre que son auteur l'a appliquée seul |
| Sortie | Bibliothèque de procédures, modèles et cas de test |
| Résultat à mesurer | Part des processus pilotés qui ont une procédure testée ; temps de reprise par l'autre associé |
| Mode | (b) |
| Erreurs possibles | Données du client mélangées aux méthodes génériques ; procédure obsolète ; documentation écrite pour des agents plutôt que pour des personnes (passation du CRM « à joindre dans la nouvelle conversation », `crm/PASSATION.md:38`) |
| Cas exceptionnels | Méthode propre à un seul client ; outil remplacé |
| Secours manuel | Passation orale mise par écrit |
| Responsable | Chacun pour ses processus ; Mathys tient la bibliothèque |

---

## 4. Comparaison des cinq options

### 4.1 Ce que chaque option apporte, en général [ES]

| Option | Coût complet | Qualité | Fiabilité | Maintenance | Adoption |
| --- | --- | --- | --- | --- | --- |
| 1. Actuel | 0 € d'outil ; temps non mesuré [IN] ; coût caché des erreurs (fuite, contradictions non vues) | Irrégulière | Dépend de la mémoire de Morgan | Aucune, mais dettes accumulées | Sans objet |
| 2. Organisation simple | 0,5 à 2 JP par processus, puis quelques heures par mois | Bonne si la règle est tenue | Dépend de la discipline | Très faible | Bonne si le rituel est court |
| 3. Outils existants configurés | 1 à 3 JP, plus 10 à 45 $ par siège et par mois (`travaux/rj-R6-marche.md:296-336`) | Bonne ; citations parfois imprécises | Éditeurs stables, prix changeants | Faible ; essais à refaire à chaque changement de modèle | Bonne si l'interface est connue et les comptes au nom du client |
| 4. Intégration légère | 2 à 8 JP, plus 0,1 à 1 JP par mois | Meilleure sur des tâches étroites | Dépend du journal, des tests et d'une seule personne (Mathys) | Moyenne à forte | Invisible pour le client si elle marche ; risque de dépendance |
| 5. Développement spécifique | 10 à 50 JP et plus | Non démontrée | Non éprouvée | Lourde | Risque fort : une console technique n'est pas lisible par un non-technicien (`travaux/syn-capacite-ia.md:424`) |

### 4.2 Coût complet sur douze mois, par processus et par option [ES]

Calcul : (mise en place + 12 × maintenance mensuelle) × 700 à 900 € + 12 × abonnement propre au processus. Les sièges d'assistant de Marwin (≈ 35 à 45 € par mois pour deux sièges standard) servent à tous les processus : ils sont comptés une seule fois dans ses frais fixes. Les options 3 à 5 s'ajoutent à l'option 2. Le temps d'exploitation (contrôle compris) n'est pas inclus : il se mesure dans les essais. Mises en place tirées de `travaux/syn-capacite-ia.md:362-646` ; maintenances [HY].

| Processus | 1. Actuel | 2. Organisation simple | 3. Outils existants | 4. Intégration légère | 5. Spécifique |
| --- | --- | --- | --- | --- | --- |
| 1. Recherche | Temps [IN] | ≈ 3 à 7 k€ | ≈ 3 à 4,5 k€ | ≈ 11,5 à 19 k€, plus les droits sur la brique [IN] | ≈ 31 à 66 k€ ; repère de marché 10 à 50 k€ [DR] |
| 2. Réunions | Aucun compte rendu de rendez-vous avec GianLuca dans le dépôt [FV négatif] | ≈ 0,5 à 1 k€ | ≈ 1 à 2 k€ | ≈ 2 à 5,5 k€ | Non chiffré : aucun besoin |
| 3. Tâches | Rappels épars, état [IN] | ≈ 1,5 à 2 k€ | ≈ 2 à 6 k€ | ≈ 2 à 6,5 k€ | ≈ 11 à 38 k€ |
| 4. Budget | Budgets épars | ≈ 1,5 à 3 k€ | ≈ 1,5 à 3 k€ | ≈ 4,5 à 7,5 k€ | Doublon avec la comptabilité |
| 5. CRM | Non conforme ; mise en conformité de 3 à 6 JP dans tous les cas (≈ 2 à 5,5 k€) | ≈ 1,5 à 4,5 k€ | ≈ 3 à 9 k€ | ≈ 3,5 à 6,5 k€ (lot C5) | ≈ 11 à 29 k€ ; module temps réel à arrêter |
| 6. Campagnes | 72 brouillons OLSEN, aucun envoi | ≈ 0,5 à 1,5 k€ | ≈ 0,5 à 1 k€ | ≈ 2 à 5,5 k€ | Exclu |
| 7. Contenus | Visuels « non contractuels » | ≈ 0,5 à 1,5 k€ | Compris dans les sièges | Aucune intégration utile | Exclu |
| 8. Prestataires | Rien de documenté | ≈ 1 à 2 k€ | ≈ 0 en plus | Non justifié | Non justifié |
| 9. Dossiers | Documents non validés | ≈ 1 à 2 k€ | ≈ 0 en plus | Non justifié | Non justifié |
| 10. Incohérences | Contradictions trouvées par l'audit seulement | ≈ 1,5 à 2 k€ | ≈ 1 à 1,5 k€ | ≈ 4,5 à 8,5 k€ | Non justifié |
| 11. Capitalisation | Passations écrites pour des agents | ≈ 1 à 3 k€ | ≈ 0 en plus | Revient au processus 1 | Non justifié |

### 4.3 Pourquoi l'option retenue l'emporte [PR]

| Processus (option retenue) | Coût complet | Qualité | Fiabilité | Maintenance | Adoption |
| --- | --- | --- | --- | --- | --- |
| 1. Recherche (2 + 3 ; 4 sous conditions) | 2 + 3 ≈ 6 à 11,5 k€, contre 11,5 à 19 k€ de plus pour l'option 4 | Citations moins précises en option 3 : on le mesure sur le même jeu de questions avant de payer l'option 4 | Option 4 non éprouvée sur des questions réelles en français | Option 3 : ≈ 0,25 JP par mois ; option 4 : ≈ 1 JP, au-dessus du seuil d'exploitation de 0,5 JP | Interface déjà connue |
| 2. Réunions (2 + 3) | ≈ 1,5 à 3 k€ | Dépend de la relecture, pas de l'outil | Modèle manuel toujours disponible | Quasi nulle | Le client lit un compte rendu d'une page, pas un outil |
| 3. Tâches (2 + 3 ; 4 pour le résumé) | ≈ 3,5 à 8 k€ | Un registre tenu vaut mieux qu'un outil riche | Rappels natifs de l'éditeur | Faible | Comptes au nom du client ; pas de console à apprendre |
| 4. Budget (2 + 3) | ≈ 3 à 6 k€ | Tolérance zéro par formule et validation de l'expert-comptable | Calcul déterministe | Faible | Tableur connu de l'expert-comptable. L'option 4 ne vaut qu'au-delà d'environ 50 pièces par mois [HY] |
| 5. CRM (conformité, 2, puis 3) | Conformité inévitable ; option 2 suffisante pour 20 à 100 comptes | Champs sourcés et datés | Hébergement au nom du client, sauvegarde quotidienne | ≤ 0,5 JP par mois pour entrer en exploitation | L'outil se choisit **après** avoir su qui appelle (associés, assistant ou Quali Contact) |
| 6. Campagnes (2 + 3) | ≈ 1 à 2,5 k€ | Grille de conformité | Approbation humaine de chaque envoi | Faible | Kit court, validé par le conseil du client |
| 7. Contenus (2 + 3, par lot) | ≤ 1,5 k€ hors lots | Droits vérifiés, mention IA | Photographe en secours | Faible | Selon les lots commandés |
| 8. Prestataires (2 + 3) | ≈ 1 à 2 k€ | Le mandat écrit compte plus que l'outil | Plafonds et double validation | Faible | Les prestataires gardent leurs outils |
| 9. Dossiers (2 + 3) | ≈ 1 à 2 k€ | Sources officielles datées | Le professionnel décide | Faible | Le professionnel reçoit un dossier complet |
| 10. Incohérences (2 + 3 ; 4 en essai) | ≈ 2,5 à 3,5 k€ ; option 4 seulement si l'essai montre un vrai gain | Un jeu d'essai réel existe déjà (contradictions relevées par l'audit) | Le déterministe ne se trompe pas de date ; le sémantique doit être trié | Faible à moyenne | Utilisé avant chaque envoi au client |
| 11. Capitalisation (2 + 3) | ≈ 1 à 3 k€ | Procédure validée par un autre que son auteur | Versionnement | Faible | Le risque est d'écrire trop, pour des agents plutôt que pour des personnes |

---

## 5. Coût complet des automatisations retenues

### 5.1 Hypothèses [HY]

- Six automatisations sont retenues pour essai : le **registre et les comptes rendus** (processus 2 et 3), le **résumé hebdomadaire automatique** (processus 3, option 4), la **recherche documentaire** en option 3 et, en secours, en option 4 (processus 1), la **qualification du CRM** (processus 5) et le **contrôle des incohérences** (processus 10, option 4).
- Le **contrôle humain** est compté à part : il remplace une partie du travail manuel et se mesure dans les essais. Le **changement de fournisseur** est une provision, à payer seulement s'il survient.
- Horizon : douze mois, sauf le résumé (mois 7 à 12) et le CRM (pilote de deux mois puis six mois d'exploitation au mieux). Le modèle financier ne compte une exploitation qu'au mois 7 et dans le seul scénario ambitieux (`modele-financier/scenarios.md:82`).

### 5.2 Coût par composant [ES]

| Composant | Registre et comptes rendus | Résumé hebdomadaire automatique | Recherche, option 3 | Recherche, option 4 | Qualification du CRM | Contrôle des incohérences |
| --- | --- | --- | --- | --- | --- | --- |
| Conception et intégration | 2 à 3 JP | 2 à 4 JP | 2 à 3,5 JP, dont le jeu de 60 questions | 4 à 8 JP, après règlement écrit des droits sur la brique BOJART [IN] | 2 à 3 JP (réimport, contrôles de format et de doublons), sans la mise en conformité de 3 à 6 JP de l'offre 0 | 3 à 6 JP |
| Abonnements et consommations | Espace registre 20 à 40 $ par mois, au nom du client | Automate hébergé ≈ 20 € par mois [DR] (`travaux/syn-capacite-ia.md:427`) | 0 en plus (sièges partagés) ; deux sièges au nom du client en exploitation | API 10 à 80 € par mois ; hébergement [IN] | API de recherche 10 à 50 € par lot de 20 ; CRM 0 à 70 € par mois ; téléphonie à la charge du client | API ≤ 50 € pour l'essai, puis ≈ 10 à 30 € par mois |
| Stockage et sauvegarde | Export hebdomadaire, copie chiffrée hors du fournisseur : 0 à 10 € par mois | Export de la configuration | Corpus déjà sauvegardé | Index et base à sauvegarder | Export quotidien, copie chiffrée : 0 à 10 € par mois | Négligeable |
| Restauration testée | 0,6 à 1,5 JP par an | 0,25 à 0,5 JP | ≤ 0,25 JP | 0,5 à 1 JP | 0,6 à 1,5 JP par an | ≤ 0,25 JP |
| Contrôle humain | Relecture des comptes rendus ≈ 0,2 à 0,4 JP par mois [HY], dans le temps du socle | 0,05 à 0,1 JP par mois | Ouverture des citations, mesurée par question | Idem | Vérification par fiche [IN], mesurée dans l'essai | Tri : ≤ 5 minutes par alerte |
| Maintenance | 0,1 à 0,25 JP par mois | 0,1 à 0,25 JP par mois | ≈ 0,25 JP par mois (jeu rejoué) | ≈ 1 JP par mois (`travaux/syn-capacite-ia.md:367`) | 0,25 à 0,5 JP par mois en exploitation | ≈ 0,25 JP par mois |
| Corrections et évolutions | 1 à 2 JP par an | 0,25 à 0,5 JP | 0,5 à 1 JP | 1 à 2 JP | 1 à 2 JP (l'échange avec Quali Contact est un lot à part) | 0,5 à 1 JP |
| Formation | 0,5 à 1 JP (délégué, personne désignée) | 0,25 JP | 0,25 à 0,5 JP | 0,5 JP | 0,5 JP (appelant) | — |
| Changement de fournisseur, s'il survient | 1 à 2 JP | 1 à 2 JP | 0,5 à 1 JP | 0,5 à 1 JP | 0,5 à 1 JP | 0,5 JP |
| Support et sortie | 0,25 à 0,5 JP | 0,25 JP | 0,25 JP | 0,5 à 1 JP | 0,5 JP (export, purge attestée) | — (outil de Marwin) |
| **Total, hors contrôle et hors changement de fournisseur** (euros : JP × 700 à 900 €, outils compris, arrondi) | **≈ 5,5 à 11 JP**, soit ≈ 4 000 à 10 500 €, dont 200 à 600 € d'outils | **≈ 3,5 à 7 JP**, soit ≈ 2 500 à 6 500 €, dont ≈ 150 € d'outils | **≈ 6 à 8,5 JP**, soit ≈ 4 000 à 8 000 €, dont 0 à 550 € d'outils | **≈ 18,5 à 24,5 JP**, soit ≈ 13 000 à 23 000 €, dont 100 à 1 200 € d'outils | **≈ 6 à 10,5 JP**, soit ≈ 4 500 à 10 000 €, dont 0 à 600 € d'outils | **≈ 6,5 à 10,5 JP**, soit ≈ 4 500 à 10 000 €, dont 150 à 400 € d'outils |
| **Temps à gagner par mois pour couvrir ces coûts** | ≈ 0,5 à 0,9 JP | ≈ 0,6 à 1,2 JP | ≈ 0,5 à 0,7 JP | ≈ 1,5 à 2 JP | ≈ 0,5 à 0,9 JP | ≈ 0,5 à 0,9 JP |
| **Lecture** | Ne se rembourse probablement pas en temps la première année ; se justifie par la qualité (décisions complètes, traçabilité) et par le socle qu'il rend possible | Seulement si le résumé manuel mesuré dépasse ≈ 1 JP par mois ; sinon, résumé assisté (option 3) | Raisonnable si l'outil sert plusieurs fois par jour | Peu probable à notre échelle ; ne passe pas le seuil de maintenance d'une exploitation | Conception payée par le pilote commercial ; l'exploitation reste à prouver | Sert d'abord à éviter une erreur de prix ou de paiement, pas à gagner du temps |

### 5.3 Qui paie, qui maintient, quand revoir ou arrêter [PR]

| Automatisation | Qui paie la conception | Qui paie le fonctionnement | Qui maintient | Revoir | Arrêter |
| --- | --- | --- | --- | --- | --- |
| Registre et comptes rendus | Démonstrateur : Marwin. Chez le client : compris dans le socle pilote (3 500 € HT par mois) ou dans l'outillage (7 500 € HT) (`travaux/strategie-retenue.md:275, 333`) | Espace registre : l'entité, à son nom ; temps : le socle | Mathys (outil), Morgan (contenu) ; dans la voie (c), la personne désignée par GianLuca | Au bilan du pilote ; au renouvellement trimestriel ; à chaque changement de modèle | Critères d'abandon du pilote P1 (section 6.1) ; erreur critique |
| Résumé hebdomadaire | Marwin : le prix du socle ne baisse pas quand le temps baisse, le gain lui revient la première année (`travaux/strategie-retenue.md:418-419`) | Abonnement au nom du client, avec son accord écrit préalable, car il dure plus de trois mois (`travaux/strategie-retenue.md:591`) | Mathys | Au mois 6 au plus tôt, après deux mois d'usage stable du registre | Résumé faux deux fois dans le mois ; maintenance au-delà de 0,25 JP par mois ; une relance externe partie sans approbation |
| Recherche, option 3 | Démonstrateur : Marwin. Exploitation : offre D, minimum de 1 000 à 1 500 € HT par mois (`travaux/strategie-retenue.md:347`) | Sièges au nom du client en exploitation | Mathys | À chaque ajout de 10 documents ou changement de modèle | Moins de 80 % de réponses justes ; une citation inventée non détectée ; maintenance au-delà de 1 JP par mois en essai ou de 0,5 JP en exploitation |
| Recherche, option 4 | Marwin, comme composant générique concédé sous licence, seulement après règlement écrit des droits | API au nom du client en exploitation | Mathys, avec un second administrateur | Seulement si l'option 3 échoue au jeu d'essai | Droits non réglés : pas de démarrage ; maintenance au-delà de 0,5 JP par mois : pas d'exploitation |
| Qualification du CRM | Pilote commercial (6 000 € HT) ; mise en conformité préalable à la charge de Marwin, non facturée (`travaux/strategie-retenue.md:215`) | API, hébergement et téléphonie : l'entité ; Quali Contact facture directement l'entité ; exploitation : offre D | Mathys | Après la vague de 20 comptes ; avant chaque extension | Joignabilité sous 50 % ; conformité non tenue ; appelant qui n'utilise pas les fiches ; incident de données |
| Contrôle des incohérences | Marwin (outil interne, jamais facturé, `travaux/strategie-retenue.md:386`) | Marwin | Mathys | Après l'essai P4 | Rappel sous 50 % ; tri plus long qu'une relecture complète |

Règles communes : les défauts de Marwin sont corrigés gratuitement pendant 60 jours après la réception ; un outil construit dans un lot n'est jamais refacturé ; sa maintenance n'est facturée que dans une exploitation (`travaux/strategie-retenue.md:384`).

> **Précision : deux seuils de maintenance différents, à garder tous les deux.** Le protocole de recherche documentaire tolère jusqu'à 1 JP de maintenance par mois pendant l'essai (`travaux/syn-capacite-ia.md:739`) ; l'entrée en exploitation exige au plus 0,5 JP par mois et par processus (`travaux/strategie-retenue.md:349`). Le premier est un seuil d'abandon de l'essai, le second un seuil d'entrée en service. L'option 4 de la recherche (≈ 1 JP par mois) ne peut donc pas entrer en exploitation telle quelle.

### 5.4 Prix des fournisseurs et arrêt d'un outil

- **Les prix bougent vite** [FV] : doublement des prix standard annoncé par Google au 1er déc. 2026 et au 1er janv. 2027 ; hausse de la DGX Spark ; grille Ringover probablement périmée (Talk 19 à 29 €, Business 49 à 69 €, Unified 69 à 89 € HT par utilisateur et par mois, à relire avant tout devis) (`travaux/rj-R6-marche.md:315-316, 380` ; `travaux/ver-R6-marche.md:45`). Chaque devis d'outil est daté et revu tous les trois mois [PR].
- **Hausse des coûts d'IA** : +1 000 € par mois sans garde-fou coûteraient environ 16 000 € de trésorerie sur 18 mois ; avec plafond de consommation et modèle de repli (+150 € par mois), environ 2 400 € [ES] (`modele-financier/stress-tests.md:206-225`).
- **Arrêt d'un outil central** : environ 3 500 € de perte sans export testé, 1 100 € avec exports mensuels testés et mode manuel écrit [ES] (`modele-financier/stress-tests.md:272-290`).
- **Parades** [PR] : plafond de consommation mensuel ; deux fournisseurs configurés ; modèle le moins cher par défaut ; clause de révision au contrat ; outils et licences du client à son nom et à sa charge (`travaux/strategie-retenue.md:532, 535`).

---

## 6. Pilote : protocoles d'essai

### 6.0 Quatre essais, trois étapes, un financement clair [PR]

| Essai | Processus | Démonstrateur interne | Pilote client | Exploitation possible |
| --- | --- | --- | --- | --- |
| **P1** Registre des décisions et des échéances, avec comptes rendus | 2 et 3 | Nov. 2026 à janv. 2027 ; réunions internes de Morgan et Mathys et préparation du cadrage ; 2 à 3 JP payées par Marwin | Voie (b) : critères de réception du socle pilote, 2 mois. Voie (c) : critère d'adoption de l'outillage. Référence mesurée pendant le cadrage (livrable 7 du cadrage, `travaux/strategie-retenue.md:225`) | Pas d'offre D : devient le socle récurrent, au plus tôt au mois 4 |
| **P2** Qualification CRM et lot de 20 comptes | 5, et 6 pour le script | Format d'échange testé sur 10 entreprises fictives ; 0,5 à 1 JP payées par Marwin | Voie (a) : pilote commercial C2, 6 à 7 JP comprises dans les 6 000 € HT | Offre D « tenue et qualification du CRM », au plus tôt au mois 7 |
| **P3** Recherche documentaire avec citations | 1 | Corpus filtré (encadré ci-dessous) ; 60 questions ; 2 à 3,5 JP payées par Marwin | Seulement dans la voie (b), sur les documents du client, après le socle pilote | Offre D, au plus tôt au mois 7 |
| **P4** (facultatif) Détection des incohérences | 10 | Contradictions connues de l'offre ; 3 à 6 JP payées par Marwin, seulement après la remise en ordre | Aucun : usage interne avant chaque envoi au client | Outil générique de Marwin, jamais facturé |

**Plafond des démonstrateurs** [PR] : au plus **8 JP non facturées avant le 2 février 2027** pour P1, P2 (format) et P3, prises sur le budget non facturable de maintenance interne et de capitalisation (1,5 à 3 JP par mois, `travaux/strategie-retenue.md:483`). P4 ne démarre que si la remise en ordre est terminée et que ce plafond n'est pas atteint. Les démonstrateurs ne sont jamais facturés au client (04-catalogue-offres.md, section 4).

**Trois étapes, chacune avec sa preuve** : démonstrateur (données fictives ou filtrées), pilote client (4 à 8 semaines, données réelles sur un périmètre restreint, après les préalables), exploitation régulière. Les preuves exigées sont à la section 7.

> **Écart avec la stratégie retenue : « données internes » ne veut pas dire « sans données personnelles ».**
> La stratégie prévoit des démonstrateurs P1 et P3 « sur données fictives ou internes » (`travaux/strategie-retenue.md:169`). Le protocole d'origine de P3 exclut seulement le dossier `crm/` (`travaux/syn-capacite-ia.md:732`). Or le dépôt contient aussi `sources/archives-crm/` : trois archives qui renferment `companies.json` (et `culture.json` pour deux d'entre elles), c'est-à-dire les fiches de prospects [FV, vérifié le 4 nov. 2026]. Les autres pièces nomment des personnes réelles (GianLuca Carlone, Medhi, des artistes, des interlocuteurs) : ce sont des données personnelles. Les envoyer à Anthropic ou à OpenAI est un transfert hors de l'Union, qui demande une offre professionnelle, des clauses types et une analyse d'impact des transferts (`travaux/syn-droit.md:671`).
> **Position de ce livrable** [PR] : (1) exclure du corpus `crm/`, `sources/archives-crm/` et toute pièce qui contient des coordonnées de personnes ; (2) n'utiliser qu'une offre professionnelle, entraînement désactivé ; (3) remplacer les noms de tiers par des codes quand la question ne les exige pas ; (4) tant que l'offre professionnelle n'est pas souscrite au nom de Marwin, limiter le démonstrateur aux pièces sans nom de tiers (offres, méthodes, études), ou attendre. La condition n° 10 de la stratégie (`travaux/strategie-retenue.md:669`) doit valoir aussi pour nos propres traitements internes. La qualification exacte de ces traitements est à confirmer avec l'avocat ou le DPD [HY].

> **Précision sur l'objectif à 12 mois.** La stratégie vise des gains mesurés sur au moins deux processus, dont P1 et P3 (`travaux/strategie-retenue.md:145, 171`). Si GianLuca choisit la voie (a), P1 n'est jamais essayé chez lui : les deux processus mesurés seront P2 et un processus interne (P3 ou P4). Un gain interne prouve notre capacité ; il ne prouve pas une valeur pour GianLuca. Le bilan du mois 12 doit le dire.

### 6.1 Pilote P1 : registre des décisions et des échéances, avec comptes rendus

| Élément | Protocole |
| --- | --- |
| Lien avec l'offre | Démonstrateur interne ; puis critères de réception du socle pilote (`travaux/strategie-retenue.md:279`) ou critère d'adoption de l'outillage (`travaux/strategie-retenue.md:336`) |
| Préalables | Entité identifiée ; délégué nommé ; accord des participants sur la prise de notes ; registre ouvert sur un compte de l'entité ; offre d'IA professionnelle si des noms de tiers sont traités |
| Fonctionnement de référence | **Mesuré pendant deux semaines avant l'essai**, avec la fiche de relevé de la section 6.6 : temps par réunion (préparation, compte rendu, relances) ; part des décisions avec responsable, date et source ; délai d'envoi du compte rendu ; échéances manquées. Déjà constaté : décision du 4 nov. appliquée à 1 support sur au moins 5 [FV] ; aucun compte rendu de rendez-vous avec GianLuca dans le dépôt [FV négatif] (`travaux/syn-capacite-ia.md:699`) |
| Données et cas | Démonstrateur : réunions internes et préparation du cadrage. Pilote : réunions avec GianLuca ou son délégué |
| Volumes | 8 semaines ; au moins 8 réunions ; au moins 40 décisions ou actions |
| Qualité acceptable | 100 % des décisions avec responsable, date et source ; compte rendu envoyé en moins de 24 h ouvrées dans au moins 90 % des cas ; au plus une correction de fond par compte rendu |
| Erreurs critiques | Décision inventée ou attribuée à tort ; engagement traité comme approuvé faute de réponse ; information confidentielle envoyée hors de la liste prévue ou dans un outil grand public |
| Temps humain total | Préparation, rédaction, relecture, corrections, relances et reprises, chronométrées ; la durée de la réunion elle-même est notée à part. Cible : au plus 70 % du temps de référence [HY], dans la ligne du −30 % des archives |
| Coût | Deux sièges professionnels et un espace de registre : ≈ 60 à 90 $ par mois [ES] (`travaux/strategie-retenue.md:277`) ; mise en place 2 à 3 JP ; coût complet en section 5.2 |
| Critères d'adoption | GianLuca ou son délégué réagit à au moins 80 % des comptes rendus sous 3 jours ouvrés et consulte le registre au moins une fois par semaine |
| Critères d'abandon | Relecture et corrections au-delà de 50 % du temps de référence pendant 4 semaines ; une erreur critique non détectée ; registre non consulté par le client après 4 semaines (`travaux/strategie-retenue.md:281`) |
| Décision en fin d'essai | Socle récurrent ; retour au modèle manuel ; ou arrêt |

### 6.2 Pilote P2 : qualification du CRM et lot de 20 comptes

| Élément | Protocole |
| --- | --- |
| Lien avec l'offre | Pilote commercial C2, 6 000 € HT (`travaux/strategie-retenue.md:302-319`) |
| Préalables, tous requis | Remise en ordre terminée ; responsable du traitement désigné et contrat de l'article 28 signé ; décision sur l'information des personnes et comptes choisis hors des fiches exposées si cette information est due ; entreprises seulement ; structure vendeuse nommée ; 5 à 10 œuvres réellement disponibles ; avis fiscal écrit ; appelant désigné ; seuils de poursuite fixés **avec** GianLuca avant l'essai (`travaux/strategie-retenue.md:311`) |
| Fonctionnement de référence | État constaté [FV] : 471 numéros dont 283 « à confirmer » ; 1 date de vérification sur 500 ; 34 numéros pour 73 fiches ; 14 entreprises opposées, opposition vérifiée pour 33 fiches ; aucun champ de suivi ; aucun appel (`travaux/ex-C5-crm.md:39-41, 49, 66`). Temps de référence : qualification manuelle de 5 fiches, chronométrée |
| Données et cas | Démonstrateur : 10 entreprises fictives pour le format d'échange. Pilote : 20 comptes tirés des 37 cibles et des 57 fiches de priorité haute |
| Volumes | 20 comptes ; au plus 4 tentatives par compte sur 30 jours [DR, règle du CRM] ; 2 semaines de préparation, 4 semaines d'appels |
| Qualité acceptable | Au moins 90 % des champs de contact avec source et date ; 100 % des numéros partagés signalés ; 100 % des oppositions respectées ; aucun argument fiscal non validé |
| Erreurs critiques | E-mail à une entreprise opposée ; donnée personnelle sans base légale ; promesse fiscale erronée ; mention des établissements interdite par la passation ; nouvelle exposition du fichier |
| Temps humain total | Par fiche acceptée : recherche, vérification, préparation, réimport, corrections. Le temps de l'appelant est mesuré à part : il est payé par le client |
| Coût | API de recherche 10 à 50 € ; téléphonie à la charge du client ; Quali Contact facturé directement à l'entité ; 6 à 7 JP de Marwin comprises dans le prix |
| Critères d'adoption | L'appelant utilise les fiches et renvoie au moins 90 % des résultats d'appel au format convenu |
| Critères d'abandon | Joignabilité sous 50 % après les premières tentatives (changer de source avant d'élargir) ; conformité non tenue ; appelant qui n'utilise pas les fiches |
| Ce qui se mesure vraiment | Marwin contrôle la qualité des fiches et les délais. Joignabilité, rendez-vous et ventes dépendent aussi de l'appelant, de GianLuca et des œuvres : ils sont suivis à part. Si les appels n'ont pas commencé 15 jours ouvrés après la livraison, la mesure devient un lot optionnel (`travaux/strategie-retenue.md:318`) |

### 6.3 Pilote P3 : recherche documentaire avec citations

| Élément | Protocole |
| --- | --- |
| Lien avec l'offre | Démonstrateur interne ; pilote client seulement dans la voie (b) ; exploitation possible au mois 7 au plus tôt |
| Fonctionnement de référence | 30 questions types posées à la main sur le corpus filtré : temps jusqu'à la réponse vérifiée, justesse, sources |
| Données et cas | Démonstrateur : corpus filtré (encadré de la section 6.0). Pilote : documents du client sous mandat |
| Volumes | **60 questions** : 35 ordinaires ; 15 pièges (versions contradictoires, montants HT et TTC, ancienne orthographe du prénom du client, décision orale, **5 pièces contenant des instructions adressées à un assistant**) ; 10 sans réponse dans le corpus. Jeu rejoué après chaque ajout d'au moins 10 documents ou changement de modèle |
| Qualité acceptable | Au moins 90 % de réponses justes avec citation exacte ; au moins 95 % des questions sans réponse correctement refusées ; 0 citation inventée ; aucune version récente présentée comme une décision approuvée ; 100 % des instructions piégées signalées, 0 exécutée |
| Erreurs critiques | Citation inventée ; données confidentielles envoyées dans un outil grand public ; exécution d'une instruction trouvée dans un document |
| Temps humain total | De la question à la réponse vérifiée, relecture comprise. Cible : au plus 50 % du temps de référence [HY] |
| Coût | Option 3 : sièges partagés (≈ 40 à 50 $ par mois), 2 à 3,5 JP. Option 4, seulement si les droits sont réglés : 4 à 8 JP, API ≤ 80 € par mois. Les deux options sont comparées **sur le même jeu de questions** |
| Critères d'adoption | Utilisé au moins trois fois par semaine par les deux associés pendant 4 semaines |
| Critères d'abandon | Moins de 80 % de réponses justes après réglage ; maintenance au-delà de 1 JP par mois ; une citation inventée non détectée |

### 6.4 Pilote P4 (facultatif) : détection des incohérences et retards

| Élément | Protocole |
| --- | --- |
| Fonctionnement de référence | Les 24 contradictions confirmées dans l'offre écrite (`travaux/syn-capacite-ia.md:746`). C'est un jeu d'essai rare : on connaît la bonne réponse |
| Données et cas | 24 contradictions et 10 paires de passages concordants (pour mesurer les fausses alertes) ; registre fictif avec des échéances dépassées |
| Volumes | Environ 35 cas sémantiques ; 50 tâches datées |
| Qualité acceptable | Au moins 70 % des contradictions retrouvées, et 100 % de celles qui touchent le prix, le paiement ou la propriété ; au moins 60 % d'alertes utiles ; 100 % des alertes de dates exactes |
| Erreurs critiques | Contradiction de prix ou de paiement non vue ; alerte appuyée sur une citation inventée |
| Temps humain total | Tri : au plus 5 minutes par alerte en moyenne |
| Coût | 3 à 6 JP ; API ≤ 50 € pour l'essai [ES] |
| Critères d'adoption | Utilisé avant chaque envoi de document au client |
| Critères d'abandon | Moins de 50 % des contradictions retrouvées, ou tri plus long qu'une relecture humaine complète |

### 6.5 Cas difficiles : réponse prévue avant l'essai [PR]

| Cas | P1 Registre | P2 CRM | P3 Recherche | P4 Incohérences | Règle commune |
| --- | --- | --- | --- | --- | --- |
| Données absentes | Réunion sans notes : compte rendu marqué « reconstitué », validé par un participant | Fiche sans numéro ou holding : « à trouver », jamais de numéro deviné | Refus explicite (10 questions du jeu) | Pièce non versionnée : alerte « statut inconnu » | Ne jamais combler un manque par le modèle ; marquer [IN] |
| Document contradictoire | Décision changée la semaine suivante : nouvelle version, l'ancienne est gardée | Deux sources pour un numéro : les deux, avec source et date | Versions listées ; la plus récente n'est pas une décision | Cas nominal de l'essai | Le statut (proposition, décision, archive) prime sur la date |
| Doublon | Même action deux fois : fusion à la main | 34 numéros pour 73 fiches : un seul appel par numéro | Copie et original : citer l'original | Alertes en double : regroupées | Pas de fusion automatique sans échantillon validé |
| Opposition commerciale | GianLuca conteste une décision consignée : compte rendu corrigé, version initiale gardée | Entreprise opposée : aucun e-mail ; le choix « appel direct maintenu » est tranché par l'avocat avant l'essai (`crm/PASSATION.md:22`) ; argument refusé par GianLuca : retiré du kit | — | — | L'objection est consignée avec sa date et son auteur |
| Changement de priorité | Consigné ; un projet sort si un autre entre (limite d'encours) | Vente reportée : essai suspendu, mesure reportée | Nouvelles questions ajoutées au jeu | — | Le changement est écrit ; jamais absorbé en silence |
| Outil indisponible | Modèle manuel | Tableur maître et journal à la main | Registre des sources et grep | Relecture humaine | Fiche de secours manuel ; second fournisseur configuré |
| Erreur qui demande une intervention humaine | Arrêt du processus, fiche d'incident, reprise manuelle ; information écrite de GianLuca sous 24 h si l'incident est critique (`travaux/strategie-retenue.md:585`) | Idem ; si une donnée personnelle est en cause, le responsable du traitement décide des notifications | Idem | Idem | Quiconque constate l'incident arrête, sans autorisation préalable |
| GianLuca ne répond pas | L'engagement attend : relance à 5 jours ouvrés, jalons reportés à 10 jours (`travaux/strategie-retenue.md:603`) | Pas d'appel tant que les seuils ne sont pas fixés avec lui | — | — | Le silence ne vaut jamais accord |

### 6.6 Comment mesurer le temps humain total [PR]

Une fiche de relevé par tâche, la même pour la référence et pour l'essai :
- date, processus, personne, version de l'outil et du modèle ;
- temps par étape : préparation, exécution, **contrôle**, **corrections**, **reprises**, relances ;
- résultat : accepté au premier passage, au second, ou refusé ;
- erreurs trouvées après coup, avec leur gravité ;
- si deux associés travaillent ensemble, deux lignes (2 JP pour une journée à deux).

Les fiches sont conservées avec le jeu d'essai. Sans référence mesurée **avant** l'essai, aucun gain n'est annoncé.

### 6.7 Temps économisé, capacité libérée, économie réelle

| Notion | Définition | État aujourd'hui |
| --- | --- | --- |
| **Temps économisé** | Temps de référence moins temps humain total avec l'outil, contrôle, corrections et reprises compris | [IN] : aucun gain mesuré |
| **Capacité libérée** | Temps économisé moins les coûts propres de l'outil (mise en place amortie, maintenance, restauration, formation), **et réellement réaffecté** à un travail utile | Négative au premier trimestre : la mise en place dépasse les gains [ES] (`travaux/syn-capacite-ia.md:762`) |
| **Économie réelle** | Dépense effectivement évitée : sous-traitance non commandée, heure non payée, embauche différée | Pour GianLuca, seulement si une tâche qu'il paie disparaît. Pour Marwin, seulement si le temps libéré est vendu ou sert à la prospection |

**Illustration sur P1, un mois** [ES, chiffres fictifs pour montrer le mécanisme] :
- Référence : 4 réunions × (1 h 30 de préparation + 1 h 30 de compte rendu + 1 h de relances) = 16 h, soit ≈ 2,3 JP.
- Avec l'outil : 4 × (1 h de préparation + 30 min de rédaction + 30 min de relecture et corrections + 30 min de relances) = 10 h, soit ≈ 1,4 JP.
- **Temps économisé** : ≈ 0,9 JP par mois.
- **Capacité libérée** la première année : 0,9 JP moins les coûts propres de l'outil (≈ 0,5 à 0,9 JP par mois, section 5.2), soit **0 à 0,4 JP par mois**. La deuxième année, une fois la mise en place payée, environ 0,6 à 0,8 JP.
- **Économie réelle** : pour GianLuca, 0 € pendant le contrat, car le prix du socle ne baisse pas quand le temps baisse (`travaux/strategie-retenue.md:419`). Pour Marwin, 0 à 350 € par mois environ, et seulement si ce temps est vendu à un autre travail ou sert la prospection.

**Partage** [PR] (`travaux/strategie-retenue.md:418-423`) : la première année, le gain reste à Marwin ; au renouvellement, un tiers du gain mesuré revient au client ; une prime sur économie réelle n'est possible qu'à 12 mois, sur une dépense que GianLuca payait vraiment, mesurée et validée par écrit. Au client, on publie l'indicateur « équivalent temps humain évité », jamais des heures fictives (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:66` ; `travaux/syn-capacite-ia.md:811`). Le mécanisme de prix est détaillé dans 04-catalogue-offres.md (section 7).

---

## 7. Preuves pour passer d'une étape à l'autre [PR]

| Passage | Preuves exigées, toutes | Qui constate | Qui décide |
| --- | --- | --- | --- |
| **Idée → démonstrateur** | Processus de la liste ; option 2 en place ; données fictives ou corpus filtré ; jeu d'essai, critères de qualité et d'abandon écrits **avant** ; budget en JP plafonné | Mathys | Morgan et Mathys |
| **Démonstrateur → pilote client** | Critères de qualité atteints sur le jeu d'essai ; temps humain total mesuré (référence et outil) ; fiche de secours écrite et testée une fois ; grille de sécurité appliquée (section 8) ; restauration réussie dans un espace neuf ; préalables RGPD réunis si des données réelles sont traitées ; bon de commande signé (socle pilote, pilote commercial ou outillage) avec critères écrits | Mathys (validation technique), l'autre associé (quatre yeux) | Le signataire de l'entité, sur proposition de Marwin |
| **Pilote client → exploitation** | Critères tenus 4 semaines de suite ; aucune erreur critique ; usage réel par le client (critères d'adoption) ; coût par résultat accepté connu ; puis 2 à 3 mois de critères tenus ; reprise manuelle et restauration testées ; maintenance ≤ 0,5 JP par mois ; responsable et maintenance chiffrés au contrat ; prix unitaire jamais sous le coût manuel mesuré (`travaux/strategie-retenue.md:344-349`) | Mathys et le délégué du client | Le responsable du traitement ou le signataire, par écrit |
| **Exploitation → révision ou arrêt** | Incident critique ; critères non tenus deux mois ; maintenance au-delà du seuil ; hausse de prix ou changement des conditions d'un fournisseur ; fin du DPF ou des clauses types pour un fournisseur | Quiconque le constate | Arrêt immédiat sans autorisation ; révision au comité mensuel |

**Ce qui ne compte pas comme preuve** : un test sur données fictives seul ; un nombre de fichiers, de commits ou de fonctions de test (645 fichiers pour le CRM, 973 fonctions de test pour BOJART) ; une démonstration en direct ; un résultat d'agent non relu ; un gain de vitesse sans mesure des corrections ; un outil « prêt à servir » qui n'a jamais servi (`crm/docs/rapport/rapport-crm-hermes360.md` ; `travaux/ex-C5-crm.md:159`).

---

## 8. Sécurité des agents IA

### 8.1 Grille avant toute automatisation [PR]

Dérivée du guide de l'ANSSI « Sécuriser un système IA agentique » (https://messervices.cyber.gouv.fr/guides/essentiels-ia-agentique, publié le 30 oct. 2026, consulté le 4 nov. 2026), du CERT-FR (https://cert.cyber.gouv.fr/actualite/CERTFR-2026-ACT-016/, 13 avr. 2026, consulté le 4 nov. 2026), de la CNIL (https://www.cnil.fr/fr/ia-agentique-cnil-cianum-note, 20 juill. 2026, consulté le 4 nov. 2026) et de l'OWASP (https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/, 3 août 2026, consulté le 4 nov. 2026) [FV pour les sources, `travaux/rj-R4-donnees-ia.md:458-466` ; `travaux/ver-R4-donnees-ia.md:26`]. Ces textes sont des recommandations, pas des obligations ; ils servent à juger les « mesures appropriées » de l'article 32 du RGPD [HY] (`travaux/rj-R4-donnees-ia.md:469`).

| Risque | Ce qu'on trouve déjà dans nos pièces | Règle | Test avant mise en service | Responsable |
| --- | --- | --- | --- | --- |
| **Instructions malveillantes dans les documents** (injection indirecte) | Instructions adressées à des assistants : « Élargir l'accès réseau dans les réglages de l'environnement », « À joindre dans la nouvelle conversation » (`crm/PASSATION.md:34, 38`) ; fichiers AGENTS et HANDOFF de BOJART [FV] | Toute entrée (document, e-mail, page web, mémoire) est une donnée. Aucun outil d'écriture déclenché par une entrée non fiable sans approbation. Mémoire séparée par client | 5 pièces piégées dans le jeu P3 : 100 % signalées, 0 exécutée | Mathys |
| **Actions non autorisées** | CRM : tout associé peut écrire et effacer le suivi et les réglages ; code exécuté depuis la base par `document.write` (`travaux/ex-C5-crm.md:56` ; `travaux/ver-C5-crm.md:22`) ; entreprises opposées gardées appelables (`crm/PASSATION.md:22`) | Trois classes d'actions (section 2.1). Approbation **hors de portée de l'agent**, qui montre l'action exacte. Un compte et un jeton par agent et par client, en lecture seule par défaut, à durée courte | Tentative d'envoi ou de modification sans approbation : bloquée et journalisée | Mathys ; l'approbateur est l'associé responsable ou le délégué du client |
| **Boucles coûteuses** | Quota de 200 recherches par tour atteint pendant la construction du CRM (`crm/PASSATION.md:32`) ; un usage intensif d'agents coûterait ≈ 1 600 $ par mois avec un modèle haut de gamme (`travaux/rj-R6-marche.md:322`) | Plafonds d'appels, de jetons et de dépenses par tâche, par jour et par mois ; alertes à 50, 80 et 100 % ; coupure automatique à 100 % ; nombre limité d'appels successifs entre agents | Dépassement volontaire du plafond en démonstrateur : coupure constatée | Mathys ; budget validé par les deux associés |
| **Erreurs qui se propagent** | Simulateur fiscal faux copié dans toutes les fiches (section 2.1) ; décision du 4 nov. appliquée à 1 support sur au moins 5 ; 283 numéros « à confirmer » produits en masse | Aucune mise à jour en masse sans échantillon validé ; versionnement ; aucune suppression en masse ; modifications du CRM par lots, avec annulation ; registre « décision → documents touchés » | Lot de 10 fiches avec une erreur injectée : détectée à l'échantillon | L'auteur, puis l'autre associé (quatre yeux) |
| **Secrets** | Dépôt public avec des données de prospects | Coffre-fort ; jamais de secret dans un prompt, un journal ou un dépôt ; révocation testée | Révocation d'un jeton, puis vérification qu'il ne marche plus | Mathys |
| **Journal** | Relectures humaines du CRM non tracées (`travaux/rj-R4-donnees-ia.md:454`) | Journal hors de portée de l'agent : demande → autorisation → action → résultat → auteur humain ; conservation alignée sur le registre RGPD | Reconstitution d'une action de bout en bout à partir du seul journal | Mathys ; contrôle par Morgan |
| **Composants tiers** | Serveur MCP de la mémoire documentaire de BOJART (`travaux/ex-C7-jarvis.md:202`) | Inventaire des agents, prompts système, connecteurs, serveurs MCP et versions ; revue annuelle | Inventaire à jour avant le pilote | Mathys |

### 8.2 Plafonds de coût proposés [PR]

- **Marwin, usage interne** : API ≤ 100 € par mois, dans l'enveloppe d'outils et d'IA de 150 à 400 € du scénario central (`travaux/strategie-retenue.md:505`) ; plafond journalier égal au dixième du plafond mensuel ; toute dépense de plus de 300 € HT et tout abonnement, quel que soit son montant, demandent l'accord des deux associés ; au-delà de 1 000 € HT ou de 3 mois, décision à l'unanimité prévue par le pacte (`travaux/strategie-retenue.md:592`).
- **Client, en exploitation** : plafond mensuel écrit dans la fiche de l'offre D, sur les comptes de l'entité, payé par elle ; modèle le moins cher par défaut ; revue sous 30 jours si un fournisseur augmente ses prix ou change ses conditions (entraînement, lieu de stockage).
- **Par tâche** : plafond fixé dans la fiche du processus avant l'essai, mesuré pendant le démonstrateur.

### 8.3 Rôle de Marwin au sens de l'AI Act

- **Déployeur** quand elle utilise un assistant pour GianLuca : elle doit prendre des mesures pour favoriser la maîtrise de l'IA de ses intervenants (article 4, réécrit au 27 juill. 2026, sans amende propre) et signaler les hypertrucages (article 50, § 4) [FV] (`travaux/syn-droit.md:651-659`).
- **Fournisseur** si elle livre sous son nom un assistant, un copilote ou un agent vocal : informer l'utilisateur qu'il parle à une IA et marquer les contenus de synthèse (article 50, § 1 et 2) [FV texte ; HY qualification]. Le contrat doit préciser le rôle (`travaux/strategie-retenue.md:559`).
- **Haut risque reporté** au 2 déc. 2027 pour l'annexe III (Omnibus IA, règlement (UE) 2026/1744, http://data.europa.eu/eli/reg/2026/1744/oj, consulté le 4 nov. 2026, `travaux/ver-R4-donnees-ia.md:24`). Les outils RH, de recrutement ou de notation restent exclus.

---

## 9. Données

### 9.1 Rôles RGPD par phase [HY, à confirmer par l'avocat ou le DPD]

| Phase | Responsable du traitement | Sous-traitants | À signer avant |
| --- | --- | --- | --- |
| Constitution du fichier (22-30 oct. 2026), avant tout contrat | Morgan et/ou Mathys, responsables de fait | Fournisseur d'IA utilisé, GitHub, Google (Firebase) | Fiche de violation et décision de notification (`travaux/syn-droit.md:597, 620-623`) |
| Démonstrateurs internes | Marwin une fois immatriculée, ou les associés, pour leurs propres documents | Fournisseur d'IA (contrat de traitement, clauses types) | Offre professionnelle ; analyse d'impact des transferts si des données personnelles partent hors de l'Union |
| Pilote et exploitation chez GianLuca | L'entité de GianLuca (vendeuse pour le CRM, chef de file pour le pilotage), à nommer [IN] | Marwin ; puis, comme sous-traitants ultérieurs autorisés par écrit : fournisseur d'IA, hébergeur du registre, outil de CRM, téléphonie ; Quali Contact, sous-traitant de l'entité | Contrat de l'article 28 (huit clauses a à h), liste des sous-traitants ultérieurs, registre côté responsable et côté sous-traitant (`travaux/rj-R4-donnees-ia.md:190-193`) |
| Aujourd'hui | Marwin n'existe pas : elle ne peut ni signer un contrat de sous-traitance ni en assumer les obligations [FV] (`travaux/syn-droit.md:599`) | — | — |

### 9.2 Fournisseurs et transferts

État de la liste officielle du Data Privacy Framework interrogée le 4 nov. 2026 (https://www.dataprivacyframework.gov/list, consulté le 4 nov. 2026) [MM] (`travaux/rj-R4-donnees-ia.md:362-371` ; `travaux/ver-R4-donnees-ia.md:25`).

| Fournisseur | Usage prévu | Liste DPF au 4 nov. 2026 | Base de transfert | Offre à utiliser | Point ouvert |
| --- | --- | --- | --- | --- | --- |
| Anthropic | Assistant, API | **Absent** | Clauses types (contrat de traitement du 24 févr. 2025) et analyse d'impact des transferts | Team ou API, conditions commerciales | Entité contractante pour l'Europe [IN] ; date du contrat non revérifiée par le contrôle (`travaux/ver-R4-donnees-ia.md:66`) |
| OpenAI | Assistant, API | **Absent** | Clauses types (contrat de traitement conclu avec OpenAI Ireland) et analyse d'impact | Business ou API | Date du contrat non revérifiée par le contrôle [IN] (`travaux/ver-R4-donnees-ia.md:66`) |
| Google (Firebase, Workspace) | Hébergement éventuel du CRM | Actif | DPF ; clauses types de secours conseillées | Compte au nom de l'entité | Hausse des prix des modèles Gemini annoncée |
| GitHub | Code des développements | Actif (données non RH) | DPF | Dépôts privés seulement ; aucune donnée de prospect dans un dépôt | — |
| Notion | Registre possible | « Active - Re-certification under Review » | DPF à surveiller ; clauses types de secours | Compte au nom de l'entité | Statut à revérifier chaque trimestre |
| Fournisseur européen (par exemple Mistral) | Repli pour les données sensibles | Sans objet si le traitement reste dans l'Union | — | Offre professionnelle | Lieu d'hébergement et sous-traitants [IN] |
| Quali Contact | Appels, si l'entité le choisit | Sans objet (société française, `travaux/rj-R6-marche.md:202`) | — | Contrat entre l'entité et Quali Contact | Existence et contenu du contrat [IN] |

Les offres grand public (Claude Free, Pro ou Max ; ChatGPT Plus ou Pro) ne conviennent pas aux données du client : les conversations peuvent servir à l'entraînement et sont conservées cinq ans chez Anthropic si l'option est activée [FV] (`travaux/rj-R4-donnees-ia.md:350`). Un abonnement ChatGPT Pro figure parmi les abonnements en échec de prélèvement relevés dans les outils de Morgan [DR] (`travaux/note-point-4-novembre-et-activites.md:8`).

### 9.3 Liste de contrôle avant toute donnée réelle [PR]

1. Fuite traitée : dépôt privé vérifié, fiche de violation, décision de notification documentée avec l'avocat ou le DPD (`travaux/strategie-retenue.md:660`).
2. Responsable du traitement désigné par écrit.
3. Contrat de l'article 28 signé, avec la liste des sous-traitants ultérieurs.
4. Registre des traitements, côté responsable et côté sous-traitant.
5. Analyse d'intérêt légitime, mention d'information (au plus tard au premier contact, avec la source des données), procédure d'opposition, liste repoussoir conservée au moins trois ans (`travaux/syn-droit.md:607-609`).
6. Conservation : trois ans à compter de la collecte ou du dernier contact **venant du prospect**, avec une purge outillée (`travaux/ver-R4-donnees-ia.md:20`).
7. Offres d'IA professionnelles, entraînement désactivé ; analyse d'impact des transferts pour Anthropic et OpenAI ; liste DPF revérifiée chaque trimestre.
8. Pseudonymisation avant envoi au modèle quand la tâche le permet (identifiant de fiche plutôt que nom et téléphone).
9. Analyse d'impact (AIPD) courte, conseillée pour l'enrichissement par agents ; son caractère obligatoire est [IN] (`travaux/syn-droit.md:612`).
10. Charte d'usage de l'IA et une séance de formation tracée (article 4 de l'AI Act).

---

## 10. Sauvegarde, restauration, journal, arrêt, reprise manuelle [PR]

| Élément | Règle | Source |
| --- | --- | --- |
| Périmètre | Registre des décisions, CRM (fiches et suivi), budgets, documents de référence, configurations des automatismes, prompts, procédures | `travaux/syn-capacite-ia.md:853` |
| Fréquence | Export quotidien du CRM et du registre (CSV et JSON, avec la description des champs) ; sauvegarde complète hebdomadaire | `travaux/syn-capacite-ia.md:854` |
| Copies | Trois copies, sur deux supports, dont une hors du fournisseur principal ; copies chiffrées ; **jamais dans un dépôt de code public** ; sauvegardes du client sur un espace à son nom | `travaux/syn-capacite-ia.md:855, 858` |
| Objectifs | Perte de données maximale de 24 h ; reprise du registre et du CRM en un jour ouvré | `travaux/syn-capacite-ia.md:856` |
| Restauration testée | Une fois par mois les trois premiers mois, puis chaque trimestre, dans un espace neuf, sans rejouer les actions déjà faites. Une restauration dans un dossier neuf a déjà réussi sur la mémoire documentaire de BOJART, dans l'environnement d'un assistant [MM] ; la capacité des associés à la refaire seuls sur les outils du client n'est pas démontrée [IN] | `travaux/syn-capacite-ia.md:857` ; `travaux/ex-C7-jarvis.md:47` |
| Journal | Inaltérable par l'agent ; chaîne demande → autorisation → action → résultat → auteur humain | Section 8.1 |
| Arrêt | Bouton d'arrêt documenté (désactivation des automatismes, révocation des jetons), que peuvent déclencher Morgan, Mathys ou le délégué de GianLuca ; testé chaque trimestre ; aucun accord préalable n'est nécessaire pour arrêter | `travaux/syn-capacite-ia.md:845` ; `travaux/strategie-retenue.md:597` |
| Reprise manuelle | Chaque processus a sa fiche de secours (section 3) ; « mode dégradé » testé une fois par trimestre | `travaux/syn-capacite-ia.md:862` |
| Continuité des personnes | Si un associé est absent plusieurs semaines, l'autre fait tourner le socle grâce aux procédures testées ; capacité ramenée à 4 à 8 JP par mois ; changement de palier sans pénalité au-delà de 10 jours ouvrés ; coffre partagé des accès | `travaux/syn-capacite-ia.md:863-866` |
| Fournisseur | Second fournisseur configuré ; prompts portables ; exports mensuels testés | `travaux/syn-capacite-ia.md:867` |
| État actuel | CRM en service sur un artefact d'un compte non nommé, suivi dans le navigateur ; sauvegarde par export CSV manuel, sans restauration testée [FV/DR] | `travaux/ex-C5-crm.md:49, 57` |

**Test de restauration, en six étapes** : (1) créer un espace neuf, vide ; (2) y restaurer la dernière sauvegarde ; (3) comparer le nombre d'enregistrements et cinq fiches tirées au hasard avec la source ; (4) vérifier qu'aucune action (envoi, relance) ne se rejoue ; (5) noter la durée et les écarts ; (6) détruire l'espace de test. Réussite : 0 écart, durée sous un jour ouvré.

**Test d'arrêt, en quatre étapes** : (1) déclencher l'arrêt ; (2) vérifier que les automatismes ne tournent plus et que les jetons sont refusés ; (3) faire tourner le processus en mode manuel une journée ; (4) relancer et vérifier le journal.

**Responsabilité** : Mathys pour les mesures techniques ; Morgan pour l'information du client ; le responsable du traitement pour les notifications (`travaux/strategie-retenue.md:585`).

---

## 11. Ce que GianLuca récupère

### 11.1 Par situation [PR]

| Situation | Ce qu'il récupère | Délai | Condition |
| --- | --- | --- | --- |
| **Fin normale de la collaboration** | Exports complets en formats ouverts (CRM, registre, budgets, documents) ; accès administrateur à tous les comptes à son nom ; configurations des automatismes ; prompts système ; procédures et fiches de secours ; journal ; inventaire des outils et abonnements ; code des développements propres à Carlone ; attestation de suppression des copies chez Marwin | 15 jours ouvrés après le préavis | Sommes dues payées ; développements propres cédés au paiement complet (`interne/offre-marwin-tech-remuneration-et-collaboration.md:209`) |
| **Marwin cesse son activité** | Idem. Les outils propres au client sont sur ses comptes dès le premier jour : rien n'est bloqué. Licence perpétuelle et non exclusive sur les composants génériques de Marwin utilisés dans ses livrables | Comptes : immédiat ; documentation : 15 jours | Clause de réversibilité ; **sortie à blanc au mois 6** (`travaux/strategie-retenue.md:85, 281`) |
| **Un fournisseur disparaît ou change ses prix** | Données et configurations exportées ; procédure de bascule ; mode manuel | Selon la fiche de secours | Exports mensuels testés |
| **Désaccord ou impayé** | Ses données et ses documents, toujours ; les développements non payés restent à Marwin jusqu'au paiement | Données : immédiat ; code : au paiement | Distinguer ses données (toujours restituables) et nos composants |

### 11.2 Trois régimes à ne pas confondre [PR]

- **Les données et documents de GianLuca** lui appartiennent et sont toujours restituables ; Marwin n'en garde aucune copie après la mission (article 28, § 3, g, du RGPD) (`travaux/syn-droit.md:495`).
- **Les développements propres à Carlone** lui sont cédés au paiement complet, par écrit, droit par droit (`travaux/syn-droit.md:498`).
- **Les outils préexistants et composants génériques de Marwin** (méthodes, modèles, outil de contrôle des incohérences, brique de mémoire si ses droits sont réglés) lui sont concédés sous licence, pas cédés. Le régime du CRM déjà construit est écrit avant tout lot qui le touche (`travaux/strategie-retenue.md:385`).

### 11.3 Ce qui ne tient pas aujourd'hui

- Le diaporama promet « Réversibilité : fichiers, configurations, documentations et accès remis » (diaporama client, copie du 4 nov., `slides/garanties.html:30`) [FV]. Or le rapport du CRM écrit : « le code, les données et le suivi restent chez les associés, dans leur dépôt GitHub et leur projet Firebase » (`crm/docs/rapport/rapport-crm-hermes360.md:19`) [FV]. Cette phrase est incompatible avec un rôle de sous-traitant (`travaux/rj-R4-donnees-ia.md:193`). La promesse ne se garde qu'avec « comptes ouverts au nom de votre entité dès le premier jour » (`travaux/strategie-retenue.md:826`).
- Si Marwin hébergeait elle-même un service de traitement de données pour le client, le Data Act lui imposerait des clauses de changement de fournisseur : préavis de deux mois au plus, transition de 30 jours au plus, au moins 30 jours pour récupérer les données, et aucuns frais de changement à partir du 12 janv. 2027 [FV] (`travaux/syn-droit.md:507-510`). La solution la plus simple reste les comptes au nom du client.

Les clauses correspondantes sont rédigées dans 12-gouvernance-contrat-sortie.md.

---

## 12. DGX Spark, laboratoire et architectures multi-agents

| Sujet | Position [PR] | Preuves | Conditions d'un retour | Qui financerait |
| --- | --- | --- | --- | --- |
| **DGX Spark** (calcul local) | **Non** | Aucun des onze processus ne demande de calcul local (section 3). Prix [ES] : 128 Go affiché à environ 6 950 $ (≈ 6 170 € HT) par NVIDIA depuis le 2 oct. 2026 [DR concordante], offres européennes de 6 200 à 8 100 € HT ; 64 Go à partir de 4 999 $ (≈ 4 440 € HT) (`travaux/ver-R6-marche.md:34`). Un usage documentaire modéré par API coûte ≈ 80 à 160 € par mois selon le modèle (`travaux/rj-R6-marche.md:321`) : l'appareil vaut 3 à 8 ans de cet usage, avant électricité, sauvegarde, maintenance et temps d'administration. Nos archives ne l'ont jamais validée : « Une DGX Spark n'est ni une dépense approuvée ni un préalable » (`interne/complement-chatgpt-2026-11-04.md:37`) ; « Le besoin de DGX Spark n'est pas établi pour le seul raccordement CRM […] Aucun achat […] n'est validé » (`sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:131`) ; poste de calcul de 10 000 € : « Enveloppe, choix et devis non validés » (`interne/laboratoire/audit-ia-robotique-2026-10-31.pdf p. 8`) | Une contrainte **mesurée** : donnée que le contrat interdit d'envoyer à un fournisseur hébergé, sans fournisseur européen acceptable ; ou coût d'API mesuré supérieur, pendant trois mois, à l'amortissement et à l'exploitation de l'appareil. Essai comparatif sur le jeu P3 (qualité locale contre API). Pas avant le mois 6 à 12 ; au plus 10 % de la capacité (`travaux/strategie-retenue.md:645`) | L'entité cliente achète et possède l'appareil ; jamais Marwin. Si Marwin l'avançait avec du temps sur un projet abandonné, la trésorerie à 18 mois baisserait d'environ 11 600 € [ES] (`modele-financier/stress-tests.md:294-308`) |
| **Laboratoire IA et robotique** | **Retiré** | Option de 30 000 € HT dont 13 500 € d'honoraires (`interne/offre-marwin-tech-remuneration-et-collaboration.md:21`) ; son geste robotique dépendait de la phase 1 de STRATES avec Medhi (`interne/offre-marwin-tech-remuneration-et-collaboration.md:65, 84`), retirée le 4 nov. [DR] | Un usage démontré, un financeur écrit, un achat par l'entité cliente, un intégrateur tiers pour toute machine, au plus 10 % de la capacité, pas avant le mois 6 à 12 (`travaux/strategie-retenue.md:645`) | Un financeur écrit, hors du chiffre d'affaires de Marwin |
| **Architecture multi-agents** | **Non pour GianLuca la première année** | Le CRM a été produit par des lots d'agents (48 commits signés « Claude », `travaux/rj-R4-donnees-ia.md:130`) : volume élevé, qualité non vérifiée, entreprises opposées gardées appelables, données exposées. L'ANSSI demande de limiter les appels successifs entre agents ; l'OWASP classe les défaillances en cascade parmi les dix risques des applications agentiques ; le CERT-FR demande de ne pas déployer d'assistants autonomes de poste tant qu'ils ne sont pas stabilisés (`travaux/rj-R4-donnees-ia.md:438-450`) | Un processus déjà prouvé en mode assisté simple (critères d'exploitation tenus trois mois) ; un goulet mesuré sur des sous-tâches indépendantes ; un coût par résultat accepté inférieur à la version simple, sur le même jeu d'essai ; grille de la section 8 appliquée à chaque agent | Marwin pour ses essais internes ; le client seulement dans un lot devisé, après preuve |
| **« Copilote Jarvis »** comme produit | **Suspendu** | Propriété du code et du nom non réglée ; dépôt BOJART sans licence (`travaux/strategie-retenue.md:648`) | Droits réglés par écrit ; gain mesuré sur P3 | — |
| **Agent vocal sortant** | **Exclu** | AI Act, art. 50 ; risques d'automate d'appel (`travaux/strategie-retenue.md:652`) | Avis de l'avocat ou du DPD ; grille de sécurité | — |

Les associés peuvent utiliser des agents pour leur propre travail sur des données publiques (veille, recherche), avec les plafonds et le journal de la section 8, sans action d'écriture vers l'extérieur et sans données de GianLuca.

---

## 13. Recommandations : preuve, hypothèse, limite, décision

| Recommandation | Preuve | Hypothèse | Limite | Décision correspondante |
| --- | --- | --- | --- | --- |
| Organisation simple et outils existants pour les onze processus ; aucun développement spécifique | Aucun gain mesuré [IN] ; production sans résultat accepté (section 1.1) [FV] ; options 4 et 5 de 2 à 10 fois plus chères (section 4.2) [ES] | Les outils du marché suffisent aux volumes de GianLuca | Volumes réels [IN] ; aucune parole directe du client | Décision n° 2 de 01-synthese-direction.md (arrêt de toute production non commandée) |
| Démonstrateurs P1 et P3 internes, plafonnés à 8 JP avant le 2 févr. 2027, sur corpus filtré | Archives de prospects dans `sources/archives-crm/` [FV] ; budget non facturable de 1,5 à 3 JP par mois [ES] | Une offre professionnelle est souscrite au nom de Marwin | Disponibilités des associés [IN] | Décision des deux associés, à inscrire au registre interne |
| Un seul pilote client, dans la voie choisie après le cadrage | Stratégie : une voie à la fois (`travaux/strategie-retenue.md:243-251`) | GianLuca choisit sur pièces | Aucune entité nommée à ce jour [FV négatif] | Choix de GianLuca à la restitution du cadrage |
| Mesurer le temps humain total, contrôle compris, avant et pendant chaque essai | Cible de −30 % jamais mesurée [FV] | Les associés tiennent la fiche de relevé | Discipline de mesure non démontrée | Fiche de relevé (section 6.6) adoptée avant le premier démonstrateur |
| Justifier le registre par la qualité, pas par le temps, la première année | Coût propre ≈ 0,5 à 0,9 JP par mois pour un gain illustratif d'environ 0,9 JP [ES] | Référence de l'ordre de 2 JP par mois | Référence réelle [IN] | Aucun gain de temps promis au client avant la mesure |
| Option 4 de la recherche et résumé automatique seulement sur mesure | Maintenance ≈ 1 JP par mois au-delà du seuil d'exploitation de 0,5 JP [ES] | L'option 3 tient les critères | Jeu d'essai encore à écrire | Comparaison des options sur le même jeu (P3) |
| Grille de sécurité avant toute automatisation ; aucune action externe sans approbation | Instructions adressées à des assistants dans nos pièces [FV] ; guide ANSSI du 30 oct. 2026 [FV] | La grille est tenable à deux | Coût de mise en œuvre non mesuré [IN] | Condition d'entrée en pilote (section 7) |
| Aucune donnée réelle avant les préalables ; offres professionnelles, clauses types, analyse d'impact des transferts | Anthropic et OpenAI absents du DPF [MM] ; fuite probable [HY fort] | Le responsable du traitement est l'entité de GianLuca | Rôles RGPD à confirmer par l'avocat [HY] | Décision n° 1 de 01-synthese-direction.md (fuite) ; condition n° 10 de la stratégie |
| Comptes au nom du client dès le premier jour ; sortie à blanc au mois 6 | Promesse de réversibilité contredite par le rapport du CRM [FV] ; Data Act [FV] | GianLuca accepte d'ouvrir et de payer ses comptes | Outils déjà utilisés par lui [IN] | Clause de réversibilité (12-gouvernance-contrat-sortie.md) |
| Non à la DGX Spark, au laboratoire et au multi-agents la première année | Aucun usage démontré ; archives qui ne les valident pas [FV] ; prix de 6 200 à 8 100 € HT [ES] | Aucune contrainte de confidentialité forte n'apparaît | Besoins futurs du client [IN] | Retrait déjà acté par la stratégie (section 9) |

---

## 14. Décisions à prendre et renvois

**Décisions des associés** [PR] :
1. **Avant tout démonstrateur** : souscrire une offre d'IA professionnelle au nom de Marwin (après l'immatriculation) ou, d'ici là, limiter les démonstrateurs aux pièces sans nom de tiers. Responsable : Mathys.
2. **Au 19 nov. 2026** : adopter la fiche de relevé du temps (section 6.6) et le plafond de 8 JP pour les démonstrateurs. Responsables : les deux.
3. **Avant le pilote commercial** : faire trancher par l'avocat le sort des entreprises opposées « appelables » (`crm/PASSATION.md:22`). Responsable : Morgan.
4. **Avant le cadrage** : décider qui, de Mathys ou d'un second administrateur, détient les accès techniques, pour ne pas faire de Mathys un point unique (`travaux/syn-capacite-ia.md:275`).
5. **Au mois 6** : sortie à blanc et décision sur l'exploitation éventuelle d'un processus.

**Renvois** : capacité et seuils de saturation, 06-fonctionnement-a-deux.md ; offres, prix et partage des gains, 04-catalogue-offres.md ; calendrier des démonstrateurs et du pilote, 08-feuille-de-route.md ; coût des outils dans la trésorerie et tests de résistance, 09-modele-economique-tresorerie.md ; clauses de données, de sécurité et de réversibilité, 12-gouvernance-contrat-sortie.md ; risques liés à l'IA et aux données, 14-registre-risques-inconnues-decisions.md ; objections sur la capacité réelle de l'IA, 15-contre-analyse.md.

---

## Limites

- **Aucune mesure de temps n'existe** : toutes les références, cibles et coûts de ce document sont des estimations [ES] ou des hypothèses [HY] à remplacer dès le premier mois.
- **Les volumes de GianLuca sont inconnus** [IN] : nombre de réunions, de pièces comptables, de documents, de prestataires. Les choix d'options peuvent changer avec eux.
- **Les pages officielles n'ont pas été rouvertes par l'auteur de ce livrable** : elles ont été consultées le 4 nov. 2026 par les chercheurs de l'audit et contrôlées (`travaux/ver-R4-donnees-ia.md` ; `travaux/ver-R6-marche.md`). Les prix des éditeurs changent souvent.
- **Les rôles RGPD, la qualification de Marwin au sens de l'AI Act et le traitement des entreprises opposées** sont des hypothèses à soumettre à l'avocat ou au DPD.
- **La visibilité actuelle du dépôt FinanceScope/CRM-Carlone n'a pas été revérifiée** ; le dernier état documenté est « public » le 4 nov. (`interne/contexte-projet-carlone.md:11`).
- **Les compétences et la disponibilité de Mathys**, qui porte l'essentiel des responsabilités techniques de ce livrable, ne sont documentées nulle part [IN] (`travaux/syn-capacite-ia.md:68`).

Relu et contrôlé le 4 novembre 2026 : 32 vérifications, 10 corrections.
