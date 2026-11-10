# Relier les neuf suites à Airbnb, Booking.com et aux autres sites : est-ce faisable ?

Document interne — ne pas transmettre à GianLuca Carlone · 10 novembre 2026 · Ce document n’est pas un avis juridique.

## En bref

1. **Oui, c’est faisable, mais pas en branchant notre propre logiciel directement sur Airbnb ou Booking.com.** Ces sites ne donnent leurs interfaces de programmation (API) qu’à des éditeurs agréés.
   - **Airbnb n’accepte plus de nouvelles demandes d’accès à son API.** Selon des pages tierces, sa page partenaires indique en octobre 2026 : « At this time, we are not accepting new access requests for our API. » Seuls des éditeurs déjà intégrés (programme « Preferred Software Partner ») y ont accès. À vérifier sur la page officielle d’Airbnb.
   - **Booking.com réserve son interface à des « Connectivity Partners »**, qui doivent remplir des conditions d’entrée et suivre toutes les évolutions de l’API (Booking.com, documentation développeurs). Une source tierce indique qu’en juillet 2026 l’entrée de nouveaux partenaires était suspendue ; non confirmé par Booking.com.
2. **La voie normale, et la seule réaliste pour nous** : choisir pour les suites un **logiciel de gestion hôtelière du marché avec gestionnaire de canaux intégré**, déjà agréé par Airbnb, Booking.com, Expedia et d’autres. Il synchronise en temps réel les disponibilités, les prix et les réservations sur tous les sites et évite les doubles réservations.
3. **Notre valeur ajoutée** : relier ce logiciel au reste de l’établissement par **son** API, s’il en publie une (critère de choix obligatoire). On relie ainsi le registre des bâtiments, la comptabilité, l’administratrice, les créneaux du sauna et du jacuzzi et les événements de la galerie. On construit seulement ce qui manque autour.
4. **À éviter** : la synchronisation par simples calendriers (liens « iCal »). Elle ne transmet que les dates bloquées, avec du retard, d’où un risque de double réservation. Les éditeurs eux-mêmes la déconseillent. Elle ne sert que de solution de secours.
5. Pour un établissement de neuf suites, cette architecture est courante et ne demande aucun développement lourd. Le coût principal est l’abonnement au logiciel du marché et le temps de paramétrage.

## 1. Pourquoi ne pas brancher notre logiciel directement

| Site | Accès à l’API | Ce que cela implique |
| --- | --- | --- |
| Airbnb | Réservé aux éditeurs agréés ; nouvelles demandes non acceptées (octobre 2026, page partenaires citée par des tiers) | Impossible pour Marwin Tech aujourd’hui ; passer par un éditeur agréé |
| Booking.com | Réservé aux « Connectivity Partners », conditions d’entrée, obligation de suivre toutes les évolutions de l’API ; entrée possiblement suspendue (source tierce, juillet 2026) | Devenir partenaire est un métier d’éditeur, hors de notre portée et sans intérêt pour neuf suites |
| Expedia, Google, autres | Même logique de partenaires agréés (à vérifier site par site) | Idem |

Même si l’accès était ouvert, il faudrait maintenir chaque connexion à chaque évolution des sites, avec un risque de réservations perdues. C’est exactement ce que vendent les éditeurs agréés.

## 2. L’architecture recommandée

1. **Logiciel de gestion hôtelière avec gestionnaire de canaux**, agréé par les principaux sites : disponibilités, prix, réservations, arrivées, fiche de police, taxe de séjour, facturation.
2. **Moteur de réservation directe** sur le site de l’établissement : sans commission de plateforme.
3. **Créneaux du sauna et du jacuzzi** : dans le même logiciel s’il le permet (module de services ou d’activités), sinon un outil de réservation de créneaux relié.
4. **Notre couche de liaison**, par l’API du logiciel choisi : registre des bâtiments et échéances, tableau de suivi pour l’administratrice, comptabilité, offres combinées avec les événements de la galerie. Rien n’est envoyé, payé ni annulé sans la validation d’une personne.

## 3. Critères de choix à ajouter à la comparaison

- Agréments en cours chez Airbnb, Booking.com et Expedia (vérifier sur les pages de partenaires des sites, pas seulement chez l’éditeur).
- API documentée et ouverte aux intégrations du client, avec ses conditions et son coût.
- Gestion de services ou de créneaux (sauna, jacuzzi) et d’offres combinées.
- Export complet des données ; durée d’engagement ; assistance en français ; caisse certifiée et facture électronique.

## 4. Points à vérifier avant d’en parler au client

- **Catégorie de l’hébergement** (hôtel, ou autre) : elle détermine les obligations affichées sur les sites, par exemple un numéro d’enregistrement pour un meublé de tourisme (loi du 19 novembre 2024 et règlement européen 2024/1028). À faire valider par ses professionnels.
- La taxe de séjour collectée par certains sites, les commissions des plateformes et la parité tarifaire : à lire dans les contrats des sites.
- L’état exact de l’accès aux API d’Airbnb et de Booking.com, sur leurs pages officielles.

## 5. La phrase à dire si GianLuca Carlone le demande

« Oui, vos suites pourront apparaître sur Airbnb, Booking.com et les autres sites, avec un seul calendrier à jour. Nous ne réinventons pas cette connexion : nous choisissons avec vous un logiciel du marché déjà agréé par ces sites, et nous le relions au reste de votre établissement. »

## Sources (consultées le 10 novembre 2026)

- Booking.com, documentation des partenaires de connectivité : https://developers.booking.com/connectivity/docs (« To become Booking.com Connectivity Partners, companies must meet specific onboarding requirements »).
- Airbnb, conditions de l’API : https://www.airbnb.com/terms/api ; statut de l’accès cité par BNBCalc, « Does Airbnb have an API? » : https://www.bnbcalc.com/help/articles/does-airbnb-have-an-api (source tierce).
- Supergood, « API Report Card — Booking.com » (juillet 2026, source tierce) : https://supergood.ai/api-report-card/booking-com
- Smoobu, « What is the Airbnb API? » : https://www.smoobu.com/en/blog/airbnb-api/ (éditeur, source intéressée).
- Comparatifs de gestionnaires de canaux (éditeurs, sources intéressées) : https://www.guesty.com/blog/best-channel-managers ; https://hoteltechreport.com/vacation-rental-software/vr-channel-manager
