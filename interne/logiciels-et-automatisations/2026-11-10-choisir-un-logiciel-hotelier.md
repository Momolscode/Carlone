# Choisir un logiciel hôtelier du marché pour les neuf suites et l’espace bien-être

Document interne — ne pas transmettre à GianLuca Carlone · 10 novembre 2026 · Ce document n’est pas un avis juridique.

Statut : note ferme du livrable 8. La note conditionnelle prévue (`interne/logiciels-et-automatisations/2026-11-10-choisir-un-logiciel-hotelier-note-conditionnelle.md`, jamais écrite) devient cette note ferme (BRIEF-2, § 10.1). Elle suit les additifs du 10 novembre au soir et dans la nuit (`audit/2026-11-10-preparation-des-livrables/travaux/BRIEF-2.md`, § 10 à 12) : ce n’est pas un hôtel séparé, mais **neuf suites « privilège », un sauna et un jacuzzi dans l’établissement de la galerie** (rapporté par Morgan Olsen, 10 novembre 2026 ; non vérifié ; adresse, ouverture, capacité, restauration et société exploitante inconnues ; BRIEF-2, § 11.1). Prix publics relus sur les pages des éditeurs le 10 novembre 2026 (douze lectures, aucune inscription, aucun devis). Page client associée : `pour-carlone/logiciels-et-automatisations/2026-11-10-votre-hotel-un-logiciel-du-marche-bien-choisi.md`.

## En bref

1. **Pour les neuf suites, il faut un logiciel hôtelier du marché, pas un logiciel construit par nous.** Fiche de police, taxe de séjour, caisse certifiée, sites de réservation, paiement et facture électronique sont déjà faits, et tenus à jour, par des éditeurs (BRIEF-2, § 10.3 et § 11.3).
2. **Notre rôle** : cahier des besoins, comparaison écrite, paramétrage, liaison avec le registre des bâtiments et la comptabilité, formation de l’administratrice. Nous construisons seulement ce qui manque (par exemple les créneaux du sauna et du jacuzzi si le logiciel ne les gère pas). Nous ne gérons pas les suites pour le compte de GianLuca Carlone.
3. **Prix publics relus le 10 novembre 2026, pour 9 à 10 chambres** : Sirvoy Pro 79 € par mois (taxes non précisées) ; Thaïs 130 à 190 € HT par mois avec moteur et canaux (exemple d’un hôtel 2 étoiles) ; eviivo à partir de 40 € HT par mois ; RoomRaccoon Entry 130 à 164 € par mois selon la facturation (taxes non précisées, page incohérente). Amenitiz, Mews et Misterbooking ne publient pas de prix d’abonnement.
4. **Sur trois ans, un ensemble complet (logiciel, moteur, canaux) coûte de l’ordre de 2 800 à 7 900 €** (estimation à valider ; hors caisse, frais de paiement, commissions des sites et facture électronique). L’autre proposition : 24 000 € par an, soit 72 000 € sur trois ans (groupe Accor, d’après Morgan Olsen, 9 novembre 2026 ; non vérifié auprès de GianLuca Carlone ; contenu inconnu). **Ces chiffres ne se comparent pas tant que le contenu de l’autre offre est inconnu.** Interne seulement.
5. **Ce qui départage les logiciels n’est pas le prix** : export des données, engagement, agréments Airbnb, Booking.com et Expedia, interface de programmation ouverte, créneaux pour le sauna et le jacuzzi, fiche de police et taxe de séjour. Aucune page de prix lue ne répond à tout : questions écrites, envoyées par l’exploitant.
6. **Vendredi 13 novembre** : cinq questions (§ 5) et une phrase (§ 6). Quatre décisions des associés avant jeudi soir (§ 7).

## 1. Ce que doit faire le logiciel de neuf suites

**À retenir : quatorze besoins, dont neuf éliminatoires (deux sous condition). Un logiciel qui ne sort pas les données, ne tient pas la fiche de police ou ne se relie à rien est écarté, quel que soit son prix.**

| Besoin | Ce que le logiciel doit faire | Pourquoi (source) | Éliminatoire |
| --- | --- | --- | --- |
| Réservations et planning | Planning des neuf suites, tarifs, réservations directes et venues des sites, annulations | Fonctions de base (annexe de spécification du 9 novembre, module 9 ; k12, § 1.1) | Oui |
| Arrivées et départs | Liste du jour, état des suites, note du séjour ; arrivée autonome si pas d’accueil permanent | k12, § 1.2 (serrures reliées : à confirmer) | Non |
| Fiche de police | Remplie à l’arrivée par tout client de nationalité étrangère, y compris de l’Union européenne ; conservée six mois, puis effacée | Service Public Entreprendre, F17452, lue le 10 novembre 2026 (k12, vérification n° 8) ; CESEDA, R814-1 à R814-3 (R2, ligne 227, non relu) | Oui |
| Taxe de séjour | Calcul au réel ou au forfait selon la délibération de la commune ; ligne distincte, hors base de TVA ; état à reverser | R2, ligne 226 (fiche F743) ; tarifs de la commune : inconnus | Oui |
| Caisse | Si petit-déjeuner, bar ou restaurant encaissé : caisse certifiée, ou attestée par l’éditeur | CGI, art. 286, I, 3° bis ; loi n° 2026-103, art. 125 ; BOFiP, ACTU-2026-00073, 25 mars 2026 (k12, vérification n° 1) | Oui, s’il y a une caisse |
| Facture électronique | Liaison avec une plateforme agréée : réception depuis le 1er septembre 2026 ; émission et données de vente au plus tard le 1er septembre 2027 pour une PME | DGFiP, FAQ du 1er septembre 2026 (R2, lignes 84 et 112) | Non, mais obligatoire en 2027 |
| Gestionnaire de canaux | Un seul calendrier pour Airbnb, Booking.com, Expedia, par un accès agréé par ces sites ; pas de simples liens de calendrier (iCal) | `interne/logiciels-et-automatisations/2026-11-10-connexion-airbnb-booking-et-autres-sites.md`, § 1 à 3 | Oui, si ces sites sont voulus |
| Moteur de réservation | Vente directe sur le site de l’établissement, sans commission de plateforme | k12, § 1.2 | Non |
| Paiement | Arrhes et séjours par un prestataire de paiement ; aucune carte saisie ni stockée par l’exploitant | R2, ligne 230 (norme PCI DSS) | Oui |
| RGPD | Contrat de sous-traitance (article 28) ; données dans l’Union européenne ou garanties écrites ; liste des sous-traitants | k12, § 1.4 | Oui |
| Export des données | Export complet (réservations, clients, factures, historique), format ouvert, délai et coût écrits, testé avant signature | k12, § 1.4 et § 5 | Oui |
| Créneaux du sauna et du jacuzzi | Réserver des créneaux, les rattacher à un séjour ; si possible, offres combinées avec les événements de la galerie | BRIEF-2, § 11.3 | Non (sinon outil de créneaux relié) |
| Interface de programmation | Ouverte au client, documentée, coût connu : c’est par elle que nous relions le reste | BRIEF-2, § 12 | Oui |
| Assistance | En français ; horaires, canaux et délai écrits | k12, § 1.4 | Non |

La catégorie juridique de l’hébergement (hôtel, avec ou sans classement, ou autre) change une partie de ces obligations. Elle est à faire valider par les professionnels de GianLuca Carlone (BRIEF-2, § 11.2). Les obligations de sécurité et d’hygiène des suites, du sauna et du jacuzzi sont traitées dans le livrable 9, pas ici.

## 2. Les logiciels du marché : tableau comparatif

**À retenir : huit logiciels regardés, quatre affichent un prix d’abonnement. Aucune page de prix ne parle de la fiche de police, de la taxe de séjour, de la caisse certifiée, de la facture électronique ni de l’export des données : ces points se demandent par écrit.**

Toutes les pages ont été lues le 10 novembre 2026. Aucune ne porte de date de mise à jour visible, sauf mention contraire. Les prix sont des prix affichés, pas des devis.

| Logiciel | Fonctions publiées | Liaisons publiées | Prix public (source) | Engagement | Réversibilité | Assistance en français |
| --- | --- | --- | --- | --- | --- | --- |
| Thaïs (éditeur français, X3, § 1) | Logiciel hôtelier ; modules restaurant (45 à 65 € par mois, selon le nombre de caisses) et point de vente (30 à 50 €) | Moteur 35 € par mois ; gestionnaire de canaux 30 à 90 € par mois « selon le nombre d’OTA » ; « API ouverte » dans l’offre de base ; paiement en ligne « inclus dans l’abonnement de base » | « 65 € HT par mois pour un hôtel de 10 chambres 2 étoiles », hors modules ; avec moteur et canaux, 130 à 190 € par mois ; mise en place 200 à 1 000 € une fois ; taxes des modules non précisées (https://thais-pms.com/tarifs) | « mensuel et sans engagement de durée » | Export : non mentionné | Non précisée ; centre d’aide et téléphone |
| Sirvoy | Logiciel, moteur « 100 % sans commission » ; formule Starter sans gestionnaire de canaux | Gestionnaire de canaux (Booking.com, Airbnb) en Pro ; « URL de rappel » pour envoyer les réservations à un autre système ; calendriers iCal ; aucune interface de programmation nommée | Pro : 79 € par mois jusqu’à 10 chambres (calculateur de la page : 44, 59, 79, 109, 149 € pour 2, 5, 10, 20, 50 chambres) ; Starter : 22 € ; hors taxes ou non : non précisé ; facturation annuelle « Économisez 8 % » (https://sirvoy.com/fr/prix, « © 2026 ») | « pas de contrats, pas de frais d’installation et pas de commissions » | Export : non mentionné | Assistance « 24 h/24 et 7 j/7 » ; langue non précisée |
| eviivo | Logiciel, moteur et gestionnaire de canaux dans l’abonnement de base | Options par chambre et par mois : paiement + 1 € ; messages clients, promotions, performance, propriétaires + 2 € chacune | « à partir de € 40 » par mois, « Prix affichés Hors-Taxes » ; remise au-delà de 10 chambres ; frais de traitement de 0,50 par réservation confirmée (devise incohérente sur la page) (https://eviivo.com/fr/tarifs/) | Non indiquée | Non mentionnée | Page en français ; ni horaires ni canaux |
| RoomRaccoon | Formule Entry : logiciel, gestionnaire de canaux (trois sites), moteur, paiements intégrés ; terminal de paiement vendu à part | Une option ou une intégration à partir de la formule Essential | Entry : 156 € par mois affiché, 130 € en facturation annuelle ; le calculateur de la même page donne 164 € par mois de 1 à 18 chambres ; hors taxes ou non : non précisé ; page modifiée le 30 septembre 2026 selon ses métadonnées (https://roomraccoon.fr/tarifs/) | Non indiquée | Non mentionnée | Téléphone en formules Premium et Pro seulement, du lundi au vendredi de 9 h à 17 h |
| Amenitiz | Logiciel, moteur et gestionnaire de canaux dans chaque formule ; caisse proposée seulement en Espagne et au Portugal ; réponses aux messages rédigées par IA (trois modes, dont brouillon) | Paiement intégré « 1,5 % + 0,25 € » | Sur devis : « Votre tarif dépend de vos chambres » (amenitiz.com/fr/nos-tarifs, lue le 10 novembre 2026 par k12, vérification n° 11) | Non publiée | Non mentionnée | « dans votre langue maternelle », dont le français ; horaires non indiqués |
| Mews | Formules Core, Pro, Enterprise ; caisse et « services réservables » en compléments | Frais de paiement facturés à part | Aucun prix affiché ; « facturé par chambre » (https://www.mews.com/fr/pricing) | Non indiquée | Non mentionnée | Non indiquée |
| Misterbooking | Logiciel hôtelier, éditeur présent en France | Non lu | Aucun tarif public trouvé ; « sur demande » selon des comparateurs (recherche du 10 novembre 2026 : appvizer.fr, hellopro.fr ; pas de page de l’éditeur lue) | Non lu | Non lu | Non lu |
| Little Hotelier | Non lu | Non lu | Non vérifié : page des tarifs refusée le 10 novembre 2026 ; les prix de X3 (129 € et 219 €) viennent d’un éditeur concurrent, à ne pas reprendre (X3, « À ne pas reprendre », point 9) | Non lu | Non lu | Non lu |

**Lecture.**

- **Prix les plus bas affichés pour un ensemble complet** : Sirvoy (79 € par mois) et eviivo (à partir de 40 € HT, options en plus). **Seul éditeur français avec prix public, interface ouverte et modules de restauration** : Thaïs. **Tout compris dans une formule** : RoomRaccoon et Amenitiz.
- **Liste courte proposée pour la comparaison écrite** (proposition de travail, à confirmer après vendredi) : Thaïs ; un logiciel tout compris (RoomRaccoon ou Amenitiz) ; Sirvoy ou eviivo pour le prix. Trois au plus (k12, § 5).
- **Les agréments Airbnb, Booking.com et Expedia** se vérifient sur les pages partenaires de ces sites, pas chez l’éditeur (note de connexion, § 3).
- **La gestion des créneaux du sauna et du jacuzzi** n’apparaît clairement que chez Mews (« services réservables », en complément). Pour les autres : à demander.

## 3. Coût sur trois ans d’un logiciel du marché (interne seulement)

**À retenir : de l’ordre de 2 800 à 7 900 € sur trois ans pour un ensemble complet (logiciel, moteur, canaux), estimation à valider. Avec notre étape de choix, environ 5 800 à 10 800 €. Rien de cette partie ne va dans un document client.**

Calculs sur les prix du § 2, pour 9 à 10 chambres, 36 mois, sans hausse de prix.

| Hypothèse | Par mois | Sur trois ans | Taxes |
| --- | ---: | ---: | --- |
| Sirvoy Pro, jusqu’à 10 chambres | 79 € | 2 844 € (environ 2 616 € en facturation annuelle, 8 % de moins) | Non précisées |
| eviivo, prix minimum | à partir de 40 €, plus options par chambre et 0,50 par réservation | 1 440 € au moins ; total pour neuf suites non calculable | HT |
| RoomRaccoon Entry | 130 à 164 € | 4 680 à 5 904 € | Non précisées |
| Thaïs, 10 chambres 2 étoiles, moteur et canaux | 130 à 190 € | 4 680 à 6 840 €, plus 200 à 1 000 € de mise en place : 4 880 à 7 840 € | HT pour la base ; modules non précisés |

Calculs : 79 × 36 = 2 844 ; 79 × 0,92 × 36 = 2 616 ; 40 × 36 = 1 440 ; 130 × 36 = 4 680 ; 164 × 36 = 5 904 ; 190 × 36 = 6 840 ; 6 840 + 1 000 = 7 840.

**Non compris** (à ajouter selon les réponses de vendredi) : caisse ou module restaurant (chez Thaïs, 45 à 65 € par mois, point de vente 30 à 50 €) ; frais de paiement (chez Amenitiz, 1,5 % + 0,25 € par opération ; ailleurs, à demander) ; commissions des sites (Airbnb : 15,5 % pour la plupart des hôtes, X3, vérification n° 12) ; plateforme agréée de facture électronique (non chiffrée) ; outil de créneaux si le logiciel ne le fait pas (non chiffré) ; serrures ; temps de l’administratrice.

**Notre aide**, d’après le document client du 9 novembre (`pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md`, lignes 109 et 116 ; prix à valider, sous réserve de DL1) :

- étape « Choix des logiciels et comparaison écrite (facultatif) » : 3 000 € HT, cadre naturel de ce travail (BRIEF-2, § 10.3) ;
- « Option hôtellerie (choix du logiciel, reprise des totaux) » : 2 300 € HT.

Les deux lignes se recouvrent en partie (le choix du logiciel hôtelier). À trancher avant tout chiffre montré (§ 7). Logiciel et étape de choix ensemble : 2 844 + 3 000 = 5 844 € à 7 840 + 3 000 = 10 840 € sur trois ans [estimation à valider ; taxes mêlées].

**Mise en regard.** L’autre proposition : 6 000 € tous les trois mois, soit 24 000 € par an et 72 000 € sur trois ans (groupe Accor, d’après Morgan Olsen, 9 novembre 2026 ; non vérifié auprès de GianLuca Carlone ; hors taxes ou non : inconnu ; contenu inconnu ; `audit/2026-11-09-audit-presentation-et-offre/travaux/BRIEF.md`, additif).

- Sur trois ans, l’ensemble logiciel du § 3 en représente environ un neuvième à un vingt-cinquième (72 000 ÷ 7 840 = 9,2 ; 72 000 ÷ 2 844 = 25,3).
- Lecture : à ce prix, l’autre offre n’est très probablement pas un logiciel seul (X3, conclusion 1, hypothèse). Elle peut comprendre une marque, des réservations apportées ou des personnes sur place, qu’un logiciel ne fournit pas (X3, conclusion 4).
- Les enseignes du groupe lues demandent en général cinquante chambres et plus ; le plus petit exemple en compte 31 (x1, conclusion 2 et vérification n° 4). Neuf suites sont loin de ce seuil. Hypothèse : une franchise est peu probable ; seule la pièce écrite le dira.
- Conséquence : on ne dit jamais « moins cher » ni « mieux ». On donne la grille de questions, valable pour tout prestataire, nous compris (`interne/logiciels-et-automatisations/2026-11-10-questions-a-poser-et-comparaison-a-refaire.md`, § 2 et § 3, cas A).
