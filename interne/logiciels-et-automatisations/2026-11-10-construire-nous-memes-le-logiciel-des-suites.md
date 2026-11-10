# Construire nous-mêmes le logiciel des neuf suites : possible, mais pas « simplement »

Document interne — ne pas transmettre à GianLuca Carlone · 10 novembre 2026 · Ce document n’est pas un avis juridique.

## En bref

1. **Techniquement, une application de réservation et de planning pour neuf suites se construit en quelques semaines.** Ce n’est pas le problème.
2. **Ce qui rend la chose « pas simple », ce sont les obligations et les connexions autour.**
   - **Connexion aux sites de réservation** : impossible en direct, car Airbnb et Booking.com réservent leur API à des éditeurs agréés. Il ne reste que la synchronisation de calendriers, avec un risque de double réservation, ou un gestionnaire de canaux payant.
   - **Encaissement** : tout logiciel qui enregistre des paiements de particuliers doit être certifié ou attesté (Code général des impôts, article 286, I, 3° bis, cité par la note k12). Les règles ont changé deux fois récemment.
   - **Paiement par carte** : il doit passer par un prestataire, sans aucune donnée de carte stockée chez nous.
   - **Fiche de police** des clients étrangers, conservée six mois (CESEDA, R814-1 à R814-3).
   - **Taxe de séjour** au tarif de la commune.
   - **Facture électronique** et ses suites.
   - **Protection des données** des clients.
   - **Assistance** le soir et le week-end, quand une réservation bloque.
3. **Coût comparé** : un logiciel du marché coûte de l’ordre de 40 à 190 € par mois pour neuf à dix chambres, soit environ 2 800 à 7 900 € sur trois ans (note `2026-11-10-choisir-un-logiciel-hotelier.md`, estimation à valider). Notre développement et sa maintenance, à deux, ne peuvent pas être moins chers. Ils créeraient en plus une dépendance de GianLuca Carlone envers nous, contraire à notre règle « tout reste à votre nom, utilisable avec qui vous voulez ».
4. **Recommandation : la voie mixte.** Le cœur réglementé, c’est-à-dire réservations, sites, encaissement, fiche de police et taxe de séjour, reste chez un logiciel du marché. **Nous construisons ce qui fait la différence** :
   - une vue d’ensemble unique pour l’administratrice (suites, galerie, cabaret, bâtiments) ;
   - les créneaux du sauna et du jacuzzi si le logiciel choisi ne les gère pas ;
   - les séjours combinés avec les vernissages et les soirées ;
   - le registre des bâtiments ;
   - le site avec réservation directe par le moteur du logiciel ;
   - les automatisations entre tous ces outils.
   C’est cela, « notre logiciel » : le logiciel de gestion de ses propriétés, dont le logiciel des suites n’est qu’une brique.

## Les trois options

| Option | Ce que c’est | Pour | Contre | Recommandation |
| --- | --- | --- | --- | --- |
| A. Tout construire | Notre propre logiciel de réservation, d’encaissement, de liaison aux sites | Sur mesure | Pas de lien direct avec Airbnb et Booking.com ; caisse à faire certifier ; maintenance et assistance permanentes à deux ; dépendance du client | Non |
| B. Logiciel du marché seul | Un logiciel hôtelier complet, paramétré | Rapide, conforme, prix connu | Pas de vue d’ensemble avec la galerie, le cabaret, les bâtiments | Possible, mais incomplet |
| C. Mixte (recommandée) | Logiciel du marché pour le cœur, notre couche autour, reliée par son API | Conforme, rapide, et sur mesure là où cela compte | Abonnement à payer au marché ; dépend de l’API du logiciel choisi | **Oui** |

## Exception possible (à ne pas proposer d’emblée)

Si GianLuca Carlone ne veut ni sites de réservation ni encaissement dans l’outil (réservations directes seulement, paiement par un prestataire externe), un petit outil de planning sur mesure devient envisageable. Les obligations restent les mêmes (fiche de police, taxe de séjour, protection des données). À n’étudier qu’après le cadrage, s’il le demande.

## Si la question tombe vendredi

« Nous pourrions écrire un logiciel de réservation, mais nous vous le déconseillons. La connexion directe à Airbnb et à Booking.com est réservée à des éditeurs agréés. L’encaissement demande un logiciel certifié. Et vous dépendriez de nous pour chaque correction. Nous prenons un logiciel du marché pour ce cœur, et nous construisons autour ce qui vous est propre : la vue d’ensemble de tous vos lieux, le bien-être, les séjours avec la galerie et le cabaret. »
