# Fichier de contacts d’entreprises : prospection entre professionnels, rôles, incident, information du client

Note de travail interne — sources publiques consultées le 10 novembre 2026 — ce n’est pas un avis juridique, fiscal ou d’assurance

Document interne. Ne pas transmettre à GianLuca Carlone. Aucune coordonnée n’est recopiée ici. Les données du dossier `crm/` n’ont pas été ouvertes. Cette version remplace la précédente, restée inachevée.

Étiquettes : [Texte officiel] = règlement, loi, code. [Autorité ou organisme] = CNIL, CEPD (Comité européen de la protection des données), DGCCRF, service public. [Source professionnelle] = cabinet, éditeur, presse. [À confirmer] = non vérifié sur une source primaire, ou point de droit à trancher par un professionnel. [Dépôt] = fait déjà établi dans nos pièces internes (fichier et ligne).

## En bref

1. Le dépôt de code qui contenait le fichier a été public. C’est très probablement une violation de données. Elle se documente dans tous les cas (partie 5).
2. Les 72 heures ont pris fin le 5 novembre 2026, si la connaissance date du 2 novembre. Une notification tardive reste possible, avec les motifs du retard. Ce qui a été décidé depuis est inconnu.
3. Une preuve s’efface chaque jour : GitHub ne montre les clones et les visiteurs que sur 14 jours. Les relever aujourd’hui (partie 5).
4. Personne n’est désigné responsable du traitement. Tant que Marwin Tech n’est pas immatriculée, deux personnes portent le risque. Un avocat doit trancher les rôles (partie 3).
5. Entre professionnels, la prospection reste possible sans consentement préalable : objet lié à la fonction, information, opposition simple. Le consentement préalable au téléphone, en vigueur depuis le 11 août 2026, vise les consommateurs (partie 1).
6. « Remis en conformité » veut dire au moins huit choses, dont un responsable nommé, un registre, l’origine notée fiche par fiche et une liste d’opposition (partie 4).
7. L’information écrite à GianLuca Carlone donne des faits datés, l’inconnu, les mesures prises et ce qui reste à décider. Elle ne qualifie rien en droit sans relecture. Échéance interne : jeudi 19 novembre 2026 (partie 6).
8. Le risque réaliste n’est pas le plafond du règlement. C’est la confiance du client, puis une procédure simplifiée de la CNIL : 20 000 € d’amende au plus (partie 7).

## 1. Prospection entre professionnels : courriel, téléphone, courrier

**Courriel et SMS**

- Entre professionnels, pas de consentement préalable. Deux règles : informer, et permettre de s’opposer de façon simple et gratuite (CNIL, « La prospection commerciale par courrier électronique, SMS-MMS et automate d’appel », 10 juin 2026) [Autorité ou organisme].
- Condition de fond : l’intérêt légitime vaut « lorsque l’objet de la sollicitation est en rapport avec la profession de la personne démarchée » (même page) [Autorité ou organisme].
- Données « acquises auprès de tiers » : s’assurer que la personne a été informée de cet usage et peut s’y opposer. Chaque message dit qui l’envoie et comment refuser les suivants (même page) [Autorité ou organisme].
- Les adresses génériques (« info », « contact » suivis du nom de la société) ne sont pas soumises à ces règles (même page) [Autorité ou organisme].
- Texte cité par la CNIL : article L34-5 du code des postes et des communications électroniques, non lu sur Légifrance aujourd’hui (page introuvable) [À confirmer].
- Reconstituer une adresse nominative : possible seulement sous conditions (CNIL, 16 octobre 2026, `audit/2026-11-04-audit-strategique/annexes/travaux/ver-R4-donnees-ia.md:18`) [Dépôt]. Notre règle « ne jamais deviner une adresse » est plus stricte. La garder.

**Téléphone — changement de 2026**

- Depuis le 11 août 2026, on ne démarche plus un consommateur par téléphone sans son consentement préalable (code de la consommation, art. L223-1, issu de la loi du 30 juin 2025). Le consentement vaut un an au plus. Sa preuve se garde trois ans au moins (décret n° 2026-662 du 23 juillet 2026) (CNIL, « Prospection commerciale par téléphone (hors automate d’appel) », 10 juin 2026) [Autorité ou organisme].
- Vers les professionnels, la règle reste : information et opposition simple, intérêt légitime si l’objet est lié à la profession (même page) [Autorité ou organisme].
- La DGCCRF confirme que l’encadrement vise « uniquement les sollicitations des consommateurs » (foire aux questions du 17 septembre 2026, citée dans `ver-R4-donnees-ia.md:16`) [Dépôt]. Bloctel a pris fin le 11 août 2026 (même ligne, `:15`) [Dépôt].
- Démarchage illicite d’un consommateur : amende administrative jusqu’à 75 000 € (personne physique) et 375 000 € (personne morale). Écrire « par manquement », pas « par appel » (`ver-R4-donnees-ia.md:17`) [Dépôt].

**Zone grise : qui est « professionnel » ?**

- Un artiste, un entrepreneur individuel ou un dirigeant joint sur sa ligne personnelle peut relever du régime du consommateur. Notre fichier contient des lignes mobiles, des messageries grand public et 22 fiches « Artiste » (`audit/2026-11-04-audit-strategique/annexes/travaux/syn-droit.md:619`) [Dépôt] [À confirmer par l’avocat].
- Une personne physique inscrite au répertoire Sirene peut refuser la prospection (code de commerce, art. A123-96, `audit/2026-11-04-audit-strategique/annexes/travaux/rj-R4-donnees-ia.md:83`) [Dépôt]. Vérifié pour 32 fiches seulement (`syn-droit.md:609`) [Dépôt].

**Courrier postal**

- Pas de consentement préalable. Deux règles : information préalable et droit d’opposition simple et gratuit, au moment de la collecte de l’adresse. Chaque envoi dit qui l’émet et comment refuser les suivants (CNIL, « La prospection commerciale par courrier postal », 10 juin 2026) [Autorité ou organisme]. La page ne distingue pas particuliers et professionnels.

## 2. Collecte de coordonnées depuis des sources publiques

- Une donnée publique reste une donnée personnelle. Elle n’est « pas librement réutilisable » et ne peut être « réexploitée à l’insu de la personne concernée ». Manquements relevés en contrôle : source non indiquée, consentement absent quand il était exigé, opposition ignorée (CNIL, « La réutilisation des données publiquement accessibles en ligne à des fins de démarchage commercial », 30 avril 2020) [Autorité ou organisme].
- Attentes raisonnables : si la personne ne s’attend pas à être démarchée par une autre société, il faut son consentement (même page) [Autorité ou organisme]. Cette page est plus stricte que les fiches de 2026 propres aux professionnels ; les deux se lisent ensemble (`rj-R4-donnees-ia.md:74`) [Dépôt].
- Origine : l’aspiration n’est « pas autorisée » sur un site dont les conditions d’utilisation l’interdisent. Minimiser la collecte (même page) [Autorité ou organisme].
- Information des personnes quand les données ne viennent pas d’elles (RGPD, art. 14) : dans un délai raisonnable, au plus tard un mois après la collecte ; si les données servent à contacter la personne, au plus tard au premier contact ; la source des données fait partie de l’information (`rj-R4-donnees-ia.md:507`) [Dépôt, source d’origine : Texte officiel]. Le droit d’opposition est présenté à part (art. 21, § 4) (même ligne) [Dépôt].
- Notre fichier a été bâti du 22 au 30 octobre 2026 (`syn-droit.md:597`) [Dépôt]. Calcul de notre part : un mois après, cela tombe entre le 22 et le 30 novembre 2026. Savoir si le délai d’un mois joue pour un fichier jamais utilisé, ou seulement le « premier contact », est à trancher [À confirmer par l’avocat].
- Décision de référence : 240 000 € d’amende contre KASPR, le 5 décembre 2024, pour une base de contacts tirée de LinkedIn et d’annuaires. Quatre manquements : base légale (coordonnées dont les personnes avaient limité la visibilité) ; conservation de cinq ans relancée à chaque mise à jour ; information (art. 12 et 14) ; accès (sources non données). Mise en conformité exigée avant le 18 juin 2025 (CNIL, communiqué du 19 décembre 2024 ; CEPD, fiche de décision, 2025) [Autorité ou organisme].
- Suites signalées par des sites spécialisés, non vérifiées sur cnil.fr : décision SAN-2026-004 du 4 mars 2026 sans liquidation d’astreinte pour KASPR ; décisions SOLOCAL MARKETING SERVICES et CALOGA du 15 mai 2025 (consentement, conservation) [Source professionnelle] [À confirmer].
- Notre fichier : 86 à 89 profils LinkedIn, des lignes mobiles, des messageries grand public, 206 adresses électroniques (`syn-droit.md:619`) [Dépôt]. L’obtention des profils est inconnue (`rj-R4-donnees-ia.md:164`) [Dépôt]. Sans l’origine, on ne peut ni indiquer la source ni répondre à une demande d’accès : c’est un reproche fait à KASPR.

## 3. Rôles : qui est responsable du traitement ?

- Le rôle se lit dans les faits : « qui décide de quoi ? qui exécute quoi ? ». Il ne dépend pas d’un choix contractuel. En cas de doute, il faut écrire le raisonnement suivi et pouvoir le justifier (CNIL, « Responsable du traitement, sous-traitants : comment bien identifier son rôle ? », 6 juin 2025) [Autorité ou organisme]. Page nouvelle en 2025.
- Le responsable décide du « pourquoi » et des moyens essentiels : quelles données, combien de temps, pour quels destinataires. Le choix d’un logiciel est un moyen non essentiel, qui peut revenir au sous-traitant (même page) [Autorité ou organisme].
- Responsables conjoints : une décision commune, ou des décisions séparées mais complémentaires, sans lesquelles le traitement n’aurait pas lieu. Un accord écrit dit qui informe les personnes, qui répond à leurs demandes, qui gère les fuites. Chaque personne peut agir contre chacun d’eux (même page ; RGPD, art. 26, lu sur cnil.fr) [Autorité ou organisme] [Texte officiel].
- Un sous-traitant qui fixe lui-même le but et les moyens « est considéré comme un responsable du traitement » (RGPD, art. 28, § 10, `rj-R4-donnees-ia.md:129`) [Dépôt, source d’origine : Texte officiel].
- Un prestataire qui développe pour un client peut être sous-traitant ; le client est responsable s’il fixe finalité et moyens (CNIL, « Déterminer la qualification juridique des acteurs », 8 avril 2024, fiche sur l’IA) [Autorité ou organisme].
- Notre cas : fichier bâti du 22 au 30 octobre 2026, avant tout contrat, sur un compte présenté comme celui de Mathys Couet (`rj-R4-donnees-ia.md:130`) [Dépôt]. Marwin Tech, non immatriculée, ne peut ni signer un contrat de sous-traitance ni en porter les obligations (`syn-droit.md:599`) [Dépôt].
- Trois lectures possibles, aucune tranchée [À confirmer par l’avocat] :
  1. Morgan Olsen et Mathys Couet ont choisi seuls le but, les sources et les données : responsables de fait, en personne (`syn-droit.md:597`) [Dépôt].
  2. GianLuca Carlone a demandé le fichier et fixé son but : il serait responsable, eux sous-traitants. Mais aucun contrat écrit n’existe, et ce sont eux qui ont choisi données et sources.
  3. But fixé ensemble : responsabilité conjointe.
- Le fait qui manque : qui a demandé le fichier, avec quelles consignes, et ce que GianLuca Carlone a reçu. Le dépôt ne contient aucune parole directe de sa part (`audit/2026-11-10-preparation-des-livrables/travaux/i0-faits-etablis-rapportes-inconnus.md:202` et `:252`) [Dépôt].
- Pour l’avenir : l’entité de GianLuca Carlone qui prospectera serait responsable, et Marwin Tech, une fois immatriculée, son sous-traitant sous contrat écrit (`syn-droit.md:598`) [Dépôt] [À confirmer].

## 4. Remise en conformité minimale avant tout usage

« Remis en conformité » veut dire au moins ceci. Tant qu’un point manque, le fichier ne sert pas.

1. **Un responsable nommé**, par écrit. Sans lui, personne ne tient le registre, n’informe ni ne répond (partie 3).
2. **Un registre.** Obligatoire même sous 250 salariés, car la gestion de prospects n’est pas occasionnelle (RGPD, art. 30, § 5, `ver-R4-donnees-ia.md:19`) [Dépôt, source d’origine : Texte officiel].
3. **Une base légale écrite** : l’intérêt légitime, avec une courte analyse (but, nécessité, attentes des personnes) (`syn-droit.md:607`) [Dépôt].
4. **Un tri.** Garder nom, fonction, coordonnées professionnelles. Justifier ou supprimer profils LinkedIn, lignes personnelles, messageries grand public, données d’origine inconnue (`rj-R4-donnees-ia.md:162`) [Dépôt] ; minimisation (CNIL, page du 30 avril 2020) [Autorité ou organisme].
5. **L’origine notée, fiche par fiche.** Elle fait partie de l’information due ; son absence a été reprochée à KASPR (partie 2) [Autorité ou organisme].
6. **Un texte d’information** prêt pour le premier contact : qui prospecte, pourquoi, d’où viennent les données, comment s’opposer (`syn-droit.md:608`) [Dépôt].
7. **Une liste d’opposition** (« liste repoussoir »), gardée au moins trois ans, et l’opposition Sirene vérifiée pour toutes les fiches (`syn-droit.md:609`) [Dépôt]. La page CNIL sur la liste repoussoir n’a pas été rouverte [À confirmer].
8. **Une durée et une purge** : trois ans après la collecte ou le dernier contact venant du prospect. Ouvrir un courriel ne compte pas. Nos appels ne relancent pas le délai (référentiel CNIL « gestion des activités commerciales », p. 11, `ver-R4-donnees-ia.md:20`) [Dépôt, source d’origine : Autorité ou organisme].

S’y ajoutent la **sécurité** (accès nominatifs, pas de compte partagé, sauvegarde testée, aucune copie dans un dépôt de code) et le **contrat de sous-traitance** (art. 28), signable seulement après l’immatriculation (`syn-droit.md:605` et `:611`) [Dépôt]. Les comptes partagés et les mots de passe faibles figurent parmi les motifs de sanction de 2025 (partie 7).

## 5. Violation de données : règles, et cas du dépôt de code public

**Les règles**

- Deux conditions : un traitement de données personnelles, et une perte de confidentialité, d’intégrité ou de disponibilité, « de manière accidentelle ou illicite » (CNIL, « Notifier une violation de données personnelles », 24 mai 2018, lue le 10 novembre 2026) [Autorité ou organisme]. Un dépôt rendu public par erreur entre très probablement dans ce cadre, même sans preuve de téléchargement (`syn-droit.md:621`) [Dépôt] [À confirmer].
- Trois niveaux : documenter en interne dans tous les cas ; notifier la CNIL s’il y a un risque ; informer aussi les personnes si le risque est élevé. « En cas de doute, notifiez à la CNIL » (même page) [Autorité ou organisme].
- La fiche interne contient : nature de la violation ; catégories et nombre approximatif de personnes et d’enregistrements ; conséquences probables ; mesures prises ou prévues (même page) [Autorité ou organisme].
- Délai : notification initiale sous 72 heures si possible ; au-delà, expliquer les motifs du retard ; compléter ensuite (même page ; RGPD, art. 33, § 1 et 4) [Autorité ou organisme] [Texte officiel].
- Le téléservice est réservé aux responsables du traitement. La CNIL propose un document préparatoire (même page) [Autorité ou organisme]. Le sous-traitant prévient le responsable « dans les meilleurs délais » (art. 33, § 2, `rj-R4-donnees-ia.md:205`) [Dépôt].
- La CNIL peut imposer d’informer les personnes (même page) [Autorité ou organisme]. Exceptions prévues : chiffrement préalable, mesures qui écartent le risque élevé, efforts disproportionnés remplacés par une communication publique (RGPD, art. 34, § 3, non relu aujourd’hui) [Texte officiel] [À confirmer].
- Réforme : la proposition COM(2025) 837 (risque élevé seulement, 96 heures) n’est pas en vigueur (`ver-R4-donnees-ia.md:22`) [Dépôt]. Ne pas s’appuyer dessus.

**Notre cas au 10 novembre 2026**

- Connaissance au plus tard le 2 novembre ; délai de 72 heures échu le 5 novembre (`syn-droit.md:620` et `:623`) [Dépôt]. Dépôt encore public le 4 novembre, selon Morgan (`syn-droit.md:618`) [Dépôt]. État actuel du dépôt et décisions D03 et D04 : inconnus (`i0-faits-etablis-rapportes-inconnus.md:177`) [Dépôt].
- Mesures à prendre et à noter, avec date, heure et auteur :
  1. Rendre le dépôt privé ; vérifier depuis un navigateur non connecté.
  2. Relever **aujourd’hui** les statistiques de fréquentation. GitHub montre les clones complets et les visiteurs des 14 derniers jours seulement, aux personnes qui ont le droit d’écrire dans le dépôt (GitHub Docs, « Viewing traffic to a repository ») [Source professionnelle]. Calcul de notre part : au 10 novembre, rien d’antérieur au 27 octobre n’est plus visible. Chaque jour efface un jour de preuve.
  3. Lister les copies (« forks ») et les autres copies (dossier `crm/`, archives) (`syn-droit.md:626-627`) [Dépôt].
  4. Révoquer d’abord tout secret présent dans le code. GitHub prévient qu’on ne retire pas les données des clones d’autres utilisateurs (`syn-droit.md:626`) [Dépôt].
  5. Écrire la décision motivée : notifier ou non, informer les personnes ou non, pourquoi, et qui décide.

## 6. Informer le client par écrit : devoir de conseil et note honnête

**Pourquoi écrire**

- Le prestataire informatique doit renseigner et conseiller un client « dépourvu de toute compétence en la matière » (Cass. com., 11 juillet 2006, n° 04-17.093, LibreJustice) [Source professionnelle]. Il doit aussi le mettre en garde (Com., 7 septembre 2010, n° 08-17.890 ; Com., 10 janvier 2018, n° 16-23.790, cités par Open Lefebvre Dalloz, 21 septembre 2020) [Source professionnelle].
- C’est au professionnel de prouver qu’il a informé (Cass. 1re civ., 2 juillet 2014, n° 13-10.076, résumé par Le Monde du Droit, 6 janvier 2015) [Source professionnelle]. D’où un écrit daté.
- Avant un contrat, une information « déterminante pour le consentement de l’autre » doit être donnée (code civil, art. 1112-1, cité par Open Lefebvre Dalloz) [Source professionnelle].
- Lecture de notre part [À confirmer] : ces arrêts visent la fourniture informatique ; les appliquer à un incident de données, et voir dans l’état du fichier une information déterminante avant le cadrage, reste à valider.
- Une phrase d’un rapport déjà rédigé pour le client est fausse tant que le dépôt est public : « Personne d’autre ne lit les fiches ni le suivi » (`syn-droit.md:628`) [Dépôt]. Elle doit être corrigée par écrit.

**Contenu d’une note honnête** (proposition de notre part, à faire relire)

1. Objet et date. 2. Faits datés : ce qui était accessible, depuis quand, jusqu’à quand, comment nous l’avons vu. 3. Données concernées : catégories et ordres de grandeur, aucun nom. 4. Ce que nous ne savons pas (consultations ou copies par des tiers). 5. Mesures prises, datées. 6. Ce qui reste à décider, par qui, pour quand. 7. Ce que cela change pour lui : fichier non utilisé ; s’il en détient une copie, ne pas l’utiliser ni la transmettre (on ignore ce qu’il a reçu, `i0-faits-etablis-rapportes-inconnus.md:252`) [Dépôt]. 8. Un interlocuteur et la date du prochain point.

Échéance interne : texte validé par écrit par un conseil le jeudi 19 novembre 2026 au plus tard (`audit/2026-11-04-audit-strategique/interne/14-registre-risques-inconnues-decisions.md:276`) [Dépôt].

## 7. Risques réalistes pour une très petite structure

- Procédure simplifiée : affaire sans difficulté particulière, procédure écrite, un mois pour répondre, conseil possible, décision d’un seul membre. Sous 50 millions d’euros de chiffre d’affaires : rappel à l’ordre, amende de 20 000 € au plus, astreinte de 100 € par jour au plus (CNIL, « La procédure de sanction simplifiée », 5 décembre 2022) [Autorité ou organisme]. Procédure ordinaire : jusqu’à 20 millions d’euros ou 4 % du chiffre d’affaires (CNIL, rapport annuel 2025) [Autorité ou organisme].
- Bilan 2025 : 83 sanctions (87 en 2024), dont 67 en procédure simplifiée. Motifs principaux en procédure simplifiée : sécurité insuffisante (14, dont mots de passe faibles et comptes partagés), absence de réponse à la CNIL (14), demandes d’opposition, d’accès ou d’effacement ignorées (14). Prospection : 10 sanctions (CNIL, « bilan 2025 », 9 février 2026 ; rapport annuel 2025) [Autorité ou organisme].
- Montants : 16 sanctions simplifiées de mai à octobre 2025, pour 108 000 € en tout ; 14 sur 16 sont nées d’une plainte ; 10 visent un défaut de coopération (avocats, médecins, sociétés) (CNIL, communiqué du 13 octobre 2025) [Autorité ou organisme]. Calcul de notre part : environ 6 750 € par sanction en moyenne.
- Lecture de notre part [À confirmer] : le scénario probable part d’une plainte d’un prospect. Ce qui aggrave : ne pas répondre à la CNIL, ignorer une opposition, n’avoir aucune fiche de violation. Le premier risque reste la confiance de GianLuca Carlone. Aucune sanction visant un dépôt de code public dans une très petite structure n’a été trouvée.

## 8. Qui peut relire, à quel coût, ressources gratuites

- **Avocat en données personnelles** : le bon relecteur pour les rôles, la notification et la note au client. Ordres de grandeur commerciaux, non officiels : environ 200 € de l’heure (cyber-diagnostic.fr, 2 juillet 2026) ; 800 à 1 500 € par jour en cabinet (dpo-partage.fr, 16 février 2026) [Source professionnelle]. Demander un devis au forfait.
- **Délégué à la protection des données externe** : 189 à 350 € HT par mois pour une TPE (cyber-diagnostic.fr) ; 390 € HT par mois, abonnement de 12 mois, page mise à jour le 6 octobre 2026 (aocsi.fr) [Source professionnelle]. Ce dernier précise que « la rédaction juridique reste à votre avocat ». Utile pour le registre, le tri, la fiche de violation ; pas pour trancher la responsabilité.
- **Gratuit** : fiches CNIL citées ici ; document préparatoire à la notification ; cybermalveillance.gouv.fr pour l’aide en cas d’incident (CNIL, page « Notifier une violation ») [Autorité ou organisme]. Permanences de la CNIL, France Num et consultations gratuites des barreaux : non vérifiées aujourd’hui [À confirmer].

## Ce que cela change pour nos livrables

**Livrable 7 (préalables qui bloquent tout envoi)**

- Ordre : relevé des statistiques GitHub ; fiche de violation et décision motivée (D03) ; relecture par un avocat ; information écrite à GianLuca Carlone (D08) ; puis les huit points de la partie 4.
- En-tête : « Projet — non envoyé — à relire par un avocat ». Rubriques : les huit points de la partie 6. Laisser en blanc, visiblement, l’inconnu : date du passage en privé, décision de notification, copies.
- Phrases possibles : « Le fichier de contacts ne sera pas utilisé tant qu’il n’a pas été remis en conformité. » « À ce jour, nous ne savons pas si des tiers ont consulté ou copié ces données. » « Si vous détenez une copie de ce fichier, nous vous demandons de ne pas l’utiliser ni la transmettre. » « Nous faisons relire ce point par un avocat et revenons vers vous le [date]. »
- Échéances : aujourd’hui pour les statistiques GitHub ; jeudi 19 novembre 2026 pour le texte validé ; 22 au 30 novembre 2026 pour la question de l’information des personnes (à confirmer).

**Livrable 6 (décisions)** : qui consulte quel avocat, avec quel budget ; notifier ou non, avec motifs du retard ; qui signe la note au client ; qui relève les statistiques aujourd’hui. Rappeler le risque porté en personne.

**Livrable 1 (offre et bon de commande)** : « Le fichier de contacts n’est pas compris dans cette commande. Il sera remis en conformité avant tout usage. » Prévoir un contrat de sous-traitance des données, signé après l’immatriculation. Pas de signature avant que le client ait reçu la note.

**Livrable 2 (orateur)** : objection « Et le fichier de contacts ? » : faits, mesures, règle « pas d’usage avant remise en conformité ». Ne pas montrer l’outil (`syn-droit.md:636`) [Dépôt].

**Livrable 3 (administratrice)** : aucune donnée du fichier. Une demande « ne plus me contacter » est notée et transmise le jour même.

**Livrable 4 (écrans)** : données fictives seulement, aucune capture de l’outil actuel.

**Livrable 5 (kit du cadrage)** : quelle entité prospectera ? qui détient des copies ? quels canaux ? qui répond aux oppositions ? des artistes ou des entrepreneurs individuels seront-ils appelés ?

**Livrables 8 et 9** : pas d’effet repéré.

## Ce qu’il ne faut pas écrire ou promettre

- Ni « violation », ni « nous sommes responsables », ni « vous êtes responsable du traitement », ni « aucune obligation de notifier » avant l’avis écrit de l’avocat. Écrire « incident » et décrire les faits.
- Ni « aucune donnée n’a été consultée » ou « aucun risque » : on ne le sait pas.
- Ni « conforme au RGPD », ni « fichier prêt », ni « coordonnées vérifiées ».
- Aucun nom, aucune coordonnée, aucun extrait du fichier dans la note ou la présentation.
- Aucune promesse d’indemnisation, aucune date de remise en conformité sans responsable nommé.
- Aucun code d’audit (D03, D08…) dans un texte client (`audit/2026-11-09-audit-presentation-et-offre/travaux/BRIEF.md:60`) [Dépôt].

## Questions à poser à un professionnel

**À l’avocat en données personnelles**

1. Qui était responsable du traitement du 22 octobre à ce jour : les deux associés, GianLuca Carlone, ou les deux ensemble ?
2. Faut-il notifier la CNIL maintenant, avec quels motifs de retard ? Faut-il informer les personnes, surtout les artistes et les lignes personnelles ?
3. Le délai d’un mois de l’article 14 court-il pour un fichier jamais utilisé ?
4. Que peut dire notre note sans valoir reconnaissance de responsabilité ?
5. Que faire d’éventuelles copies détenues par le client ?

**À l’assureur** : un incident connu avant la souscription est-il couvert ? (à poser lors des démarches d’assurance du livrable 7) [À confirmer].

## Ce qui n’a pas pu être vérifié

- Texte de l’article L34-5 sur Légifrance (page introuvable).
- Article 34, § 3, et lignes directrices 9/2022 du CEPD (moment de la « prise de connaissance »), non relus aujourd’hui.
- Page CNIL sur la liste repoussoir ; décisions SOLOCAL, CALOGA et SAN-2026-004 sur cnil.fr.
- Permanences gratuites (CNIL, barreaux, France Num).
- État du dépôt, décisions D03, D04 et D08, et ce que GianLuca Carlone a reçu.
- Aucun bilan des sanctions 2026 trouvé.

## Sources (consultées le 10 novembre 2026)

1. CNIL, « La prospection commerciale par courrier électronique, SMS-MMS et automate d’appel », 10 juin 2026 — https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique-sms-mms-et-automate-dappel
2. CNIL, « Prospection commerciale par téléphone (hors automate d’appel) : quelles sont les règles ? », 10 juin 2026 — https://www.cnil.fr/fr/prospection-commerciale-par-telephone-hors-automate-dappel-quelles-sont-les-regles
3. CNIL, « La prospection commerciale par courrier postal », 10 juin 2026 — https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-postal
4. CNIL, « La réutilisation des données publiquement accessibles en ligne à des fins de démarchage commercial », 30 avril 2020 — https://www.cnil.fr/fr/la-reutilisation-des-donnees-publiquement-accessibles-en-ligne-des-fins-de-demarchage-commercial
5. CNIL, « Aspiration de données : sanction de 240 000 euros à l’encontre de la société KASPR », 19 décembre 2024 — https://www.cnil.fr/fr/aspiration-de-donnees-sanction-de-240-000-euros-lencontre-de-la-societe-kaspr
6. CEPD, fiche « Data scraping: French Supervisory Authority fined KASPR », 2025 — https://www.edpb.europa.eu/news/news/2025/data-scraping-french-supervisory-authority-fined-kaspr-eu240-000_fr
7. CNIL, « Responsable du traitement, sous-traitants : comment bien identifier son rôle ? », 6 juin 2025 — https://www.cnil.fr/fr/rgpd-comment-bien-identifier-son-role
8. CNIL, RGPD, chapitre IV (art. 26) — https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4 (date non affichée)
9. CNIL, « Déterminer la qualification juridique des acteurs », 8 avril 2024 — https://www.cnil.fr/fr/determiner-la-qualification-juridique-des-fournisseurs-de-systemes-dia
10. CNIL, « Notifier une violation de données personnelles », 24 mai 2018 — https://www.cnil.fr/fr/notifier-une-violation-de-donnees-personnelles
11. CNIL, « La procédure de sanction simplifiée », 5 décembre 2022 — https://www.cnil.fr/fr/la-procedure-de-sanction-simplifiee
12. CNIL, « Sanctions et mesures correctrices : la CNIL présente le bilan 2025 », 9 février 2026 — https://www.cnil.fr/fr/bilan-sanctions-2025
13. CNIL, rapport annuel 2025, mai 2026 — https://cnil.fr/sites/default/files/2026-05/rapport_annuel_2025.pdf
14. CNIL, « La CNIL prononce 16 nouvelles sanctions dans le cadre de la procédure simplifiée », 13 octobre 2025 — https://www.cnil.fr/fr/la-cnil-prononce-16-nouvelles-sanctions-dans-le-cadre-de-la-procedure-simplifiee
15. GitHub Docs, « Viewing traffic to a repository », non datée — https://docs.github.com/en/repositories/viewing-activity-and-data-for-your-repository/viewing-traffic-to-a-repository
16. LibreJustice, Cass. com., 11 juillet 2006, n° 04-17.093 — https://librejustice.fr/decision/fr/_ycPmdrkXQNG
17. Le Monde du Droit, « Contrats informatiques : panorama de jurisprudence 2014 », 6 janvier 2015 — https://www.lemondedudroit.fr/decryptages/10634-contrats-informatiques-panorama-de-jurisprudence-2014.html?start=6
18. Open Lefebvre Dalloz, « Contrat informatique (Obligation de renseignement) », 21 septembre 2020 — https://open.lefebvre-dalloz.fr/droit-affaires/contrats-commerciaux/contrat-informatique_dz-oasis-001802
19. Sources commerciales sur les prix : cyber-diagnostic.fr/consultant-rgpd (2 juillet 2026) ; dpo-partage.fr/dpo-externalise-prix-comparatif (16 février 2026) ; aocsi.fr/dpo-externalise (mise à jour 6 octobre 2026).
20. Sources secondaires non confirmées : prospection-externalisee.fr/sanctions-cnil-prospection/2024-kaspr (non datée) ; fytt.me/san-2024-020-manquements-cnil (non datée).
21. Pièces internes : `audit/2026-11-04-audit-strategique/annexes/travaux/syn-droit.md`, `rj-R4-donnees-ia.md`, `ver-R4-donnees-ia.md` (vérifications du 4 novembre 2026 : loi n° 2025-594, décret n° 2026-662, FAQ DGCCRF, référentiel CNIL, fiche CNIL du 16 octobre 2026) ; `audit/2026-11-04-audit-strategique/interne/14-registre-risques-inconnues-decisions.md` ; `audit/2026-11-10-preparation-des-livrables/travaux/i0-faits-etablis-rapportes-inconnus.md`.

## Vérification du 10 novembre 2026

Relecture sceptique. Document interne — ne pas transmettre à GianLuca Carlone. Ce n’est pas un avis juridique. Cette partie l’emporte sur le reste de la note (`audit/2026-11-10-preparation-des-livrables/travaux/BRIEF-2.md`, § 4). Aucune donnée du dossier `crm/` n’a été ouverte.

**Conclusion.** Les règles de fond sont confirmées : prospection entre professionnels fondée sur l’intérêt légitime, avec information et opposition simple ; information des personnes dans un mois au plus, ou au premier contact ; procédure simplifiée de la CNIL plafonnée à 20 000 €. Quatre points sont à préciser :

1. La CNIL ne dit pas « pas de consentement préalable » en ces mots. Elle dit que la prospection vers des professionnels « peut être fondée sur l’intérêt légitime » de l’organisme.
2. Article 14 : l’information dit aussi si les données viennent ou non de sources accessibles au public. Une exception existe (art. 14, § 5, b : information impossible ou « efforts disproportionnés »), avec des mesures de protection, dont la publication de l’information. Lecture littérale du § 3 : le délai d’un mois du point a) est un plafond ; le point b) (premier contact) ne le prolonge pas. Pour un fichier bâti du 22 au 30 octobre 2026, l’échéance tomberait donc entre le 22 et le 30 novembre 2026, fichier utilisé ou non. Lecture à confirmer par l’avocat.
3. Plusieurs documents internes parlent de « l’incident du 4 novembre ». La connaissance date au plus tard du 2 novembre ; le 4 novembre, le dépôt était encore public (`audit/2026-11-04-audit-strategique/annexes/travaux/syn-droit.md`, lignes 617 et 619). Corrigé dans `interne/prealables/`.
4. Le projet d’information au client affirme « Aucune donnée bancaire ni de santé » sans source. Mis entre crochets, à vérifier avant d’écrire.

**Méthode.** Quatre appels pour cette note le 10 novembre 2026, dont un échec (Légifrance, article L34-5 : identifiant introuvable, erreur 404). Quinze appels au total pour k1b, k2 et k3. Les autres points viennent des vérifications du 4 novembre (`audit/2026-11-04-audit-strategique/annexes/travaux/ver-R4-donnees-ia.md`). **L’outil de lecture résume les pages et ne rend que de courts extraits** : toute citation doit être relue sur la page avant un usage juridique.

### Tableau des contrôles

| # | Affirmation de la note | Verdict | Source et date |
|---|---|---|---|
| 1 | Courriel vers des professionnels : pas de consentement préalable ; information ; opposition simple ; objet en rapport avec la profession ; adresses génériques hors de ces règles ; article L34-5 cité (partie 1) | confirmé ; formulation précisée | CNIL, « La prospection commerciale par courrier électronique, SMS-MMS et automate d’appel », lue le 10 nov. 2026 (date de mise à jour non relevée par l’outil ; la note indique le 10 juin 2026) : « peut être fondée sur l’intérêt légitime » ; « lorsque l’objet de la sollicitation est en rapport avec la profession de la personne démarchée » ; personne informée et « en mesure de s’y opposer » ; adresses « info » et « contact » « pas soumises » ; renvoi à L34-5. Aucune durée de conservation sur cette page |
| 2 | Art. 14 : délai raisonnable, un mois au plus ; au plus tard au premier contact ; source des données (partie 2) | confirmé ; complété | RGPD, chapitre III, sur cnil.fr (page datée du 23 mai 2016) : § 2, f (source, et « mention indiquant qu’elles sont issues ou non de sources accessibles au public ») ; § 3, a (« ne dépassant pas un mois ») et b (« au plus tard au moment de la première communication ») ; § 5, b (« impossible ou exigerait des efforts disproportionnés ») |
| 3 | Opposition simple à la prospection (art. 21) | confirmé | même page : art. 21, § 2 (« à tout moment ») et § 3 (les données « ne sont plus traitées à ces fins ») |
| 4 | Procédure simplifiée : un seul membre décide ; un mois pour répondre ; sous 50 millions d’euros de chiffre d’affaires, rappel à l’ordre, amende de 20 000 € au plus, astreinte de 100 € par jour au plus (partie 7) | confirmé | CNIL, « La procédure de sanction simplifiée », lue le 10 nov. 2026 (date non relevée par l’outil ; la note indique le 5 décembre 2022). Le résumé ajoute des plafonds plus hauts au-delà de 50 millions d’euros : sans effet ici, à relire avant toute citation |
| 5 | Article L34-5 du code des postes et des communications électroniques | non relu | Légifrance : identifiant essayé introuvable (erreur 404) |
| 6 | Conservation : trois ans après la collecte ou le dernier contact venant du prospect ; ouvrir un courriel ne compte pas (partie 4) | confirmé (dépôt) | Référentiel CNIL « gestion des activités commerciales », p. 11 (`ver-R4-donnees-ia.md`, ligne 20) ; non relu ce jour |
| 7 | Violation : documentation dans tous les cas ; 72 heures ; information des personnes si risque élevé (partie 5) | confirmé (dépôt) | RGPD, art. 33 et 34, sur cnil.fr (`ver-R4-donnees-ia.md`, ligne 21) |
| 8 | Téléphone : consentement préalable du consommateur depuis le 11 août 2026 ; appels vers des professionnels hors de cette règle (partie 1) | confirmé (dépôt) | DGCCRF, fiche du 27/07/2026 et foire aux questions du 17/09/2026 ; loi n° 2025-594, art. 13 (`ver-R4-donnees-ia.md`, lignes 15 et 16) |
| 9 | Liste d’opposition gardée au moins trois ans (partie 4) | non vérifié | page de la CNIL non rouverte |

### Corrections à appliquer

1. **Base légale (En bref, point 5 ; partie 1, première puce).** Phrase à préciser : « Entre professionnels, pas de consentement préalable. » Phrase juste : « Entre professionnels, la prospection par courriel peut être fondée sur l’intérêt légitime, si son objet est en rapport avec la profession de la personne ; celle-ci est informée et peut s’opposer simplement et gratuitement. » Source : CNIL, page de la ligne 1.
2. **Information des personnes (partie 2, quatrième puce).** Ajouter : « L’information indique aussi si les données viennent ou non de sources accessibles au public (art. 14, § 2, f). Exception : information impossible ou exigeant des efforts disproportionnés (art. 14, § 5, b) ; le responsable prend alors des mesures de protection, dont la publication de l’information. » Source : RGPD sur cnil.fr.
3. **Délai d’un mois (partie 2, cinquième puce).** Ajouter, avant « à trancher » : « Lecture littérale : le point a) du § 3 fixe un plafond d’un mois après l’obtention des données ; le point b) ne le prolonge pas. L’échéance tomberait donc entre le 22 et le 30 novembre 2026, fichier utilisé ou non, sauf exception ou suppression du fichier. » Lignes directrices du CEPD sur la transparence : non relues.
4. **Date de l’incident (documents de `interne/prealables/`).** « L’incident du 4 novembre » devient « l’incident du dépôt public (connu au plus tard le 2 novembre, encore public le 4 novembre) ». Source : `syn-droit.md`, lignes 617 et 619. Fait dans les trois fichiers concernés.
5. **Projet d’information au client.** « Aucune donnée bancaire ni de santé. » n’a pas de source dans la note ni dans `syn-droit.md` (ligne 618, liste des données exposées). Mis entre crochets, à vérifier. Fait dans `interne/prealables/2026-11-10-projet-d-information-sur-le-fichier-de-contacts.md`.

### Sûr à reprendre

**Projet d’information au client** (après validation écrite d’un conseil) : les phrases factuelles déjà proposées (« Nous ne savons pas si des tiers ont consulté ou copié le fichier pendant cette période » ; « Le fichier n’a pas été utilisé et ne le sera pas tant qu’il n’est pas remis en conformité » ; « Si vous en détenez une copie, merci de ne pas l’utiliser ni la transmettre »). Elles ne qualifient rien en droit.

**Interne seulement** :

- « Entre professionnels, la prospection par courriel peut reposer sur l’intérêt légitime si son objet est en rapport avec la profession de la personne ; elle est informée et peut s’opposer simplement et gratuitement. » Source : CNIL.
- « Quand les données ne viennent pas de la personne, elle est informée dans un délai raisonnable, d’un mois au plus, et au plus tard au premier contact ; l’information donne la source des données. » Source : RGPD, art. 14, § 2, f, et § 3.
- « Une personne peut s’opposer à tout moment à la prospection ; ses données ne servent alors plus à cette fin. » Source : RGPD, art. 21, § 2 et 3.
- « En procédure simplifiée, la CNIL peut prononcer un rappel à l’ordre, une amende de 20 000 € au plus et une astreinte de 100 € par jour au plus (entreprise de moins de 50 millions d’euros de chiffre d’affaires). » Source : CNIL, « La procédure de sanction simplifiée ».

### Ce qui reste inconnu

- Qui est responsable du traitement ; qui a demandé le fichier et avec quelles consignes ; ce que GianLuca Carlone a reçu.
- La décision sur la notification (D03), l’état du dépôt (D04), l’information du client (D08).
- Le point de départ du délai d’un mois pour un fichier jamais utilisé et l’usage de l’exception de l’art. 14, § 5, b : lecture littérale ci-dessus, à confirmer.
- Le texte de l’article L34-5 sur Légifrance ; la durée de la liste d’opposition.
- Les dates exactes des pages de la CNIL sur la prospection par courriel et la procédure simplifiée (non relevées par l’outil).
- L’article 34, § 3, et les lignes directrices 9/2022 du CEPD ; les décisions SOLOCAL, CALOGA et SAN-2026-004.

### Pages relues le 10 novembre 2026

- CNIL, « La prospection commerciale par courrier électronique, SMS-MMS et automate d’appel » : https://www.cnil.fr/fr/la-prospection-commerciale-par-courrier-electronique-sms-mms-et-automate-dappel
- CNIL, RGPD, chapitre III (art. 12 à 23), page datée du 23 mai 2016 : https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre3
- CNIL, « La procédure de sanction simplifiée » : https://www.cnil.fr/fr/la-procedure-de-sanction-simplifiee
- Non lue : Légifrance, article L34-5 (identifiant LEGIARTI000032228578 introuvable, erreur 404).
- Toutes ces lectures passent par un outil qui résume la page.
