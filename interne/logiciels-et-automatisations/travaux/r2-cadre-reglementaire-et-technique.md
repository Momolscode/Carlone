# R2 · Cadre réglementaire et technique d'un logiciel de gestion des propriétés

Audit Marwin Tech × GianLuca Carlone · dossier « logiciels et automatisations » · travail R2 : cadre réglementaire et technique en France, novembre 2026 · 9 novembre 2026
Statut : **interne** (ne pas transmettre à GianLuca Carlone). Cite un concurrent, des règles de prix internes et le plafond de capacité de Marwin.
Sources principales : textes et pages officiels lus le 9 nov. 2026 (Légifrance, service-public, impots.gouv et BOFiP, CNIL, EUR-Lex, ecologie.gouv) ; stratégie retenue, catalogue des offres, processus IA, note de mise à jour du 9 nov. et travaux juridiques de l'audit (abréviations ci-dessous) ; travail R1 du même dossier.
Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ; [MM] mesuré ; [IN] inconnu. « [PR, R2] » signale une proposition nouvelle de ce travail. JP : journée-personne de 7 h.

**Abréviations** (chemins depuis la racine du dépôt) :

| Abrév. | Fichier |
| --- | --- |
| STRAT | `audit/2026-11-04-audit-strategique/annexes/travaux/strategie-retenue.md` |
| CAT | `audit/2026-11-04-audit-strategique/interne/04-catalogue-offres.md` |
| PRO7 | `audit/2026-11-04-audit-strategique/interne/07-processus-ia-et-essais.md` |
| MAJ | `audit/2026-11-04-audit-strategique/interne/2026-11-09-mise-a-jour-faits-nouveaux.md` |
| SYN-D | `audit/2026-11-04-audit-strategique/annexes/travaux/syn-droit.md` |
| R2F | `audit/2026-11-04-audit-strategique/annexes/travaux/rj-R2-fiscal.md` |
| R1 | `interne/logiciels-et-automatisations/travaux/r1-marche-et-offre-accord.md` |
| PIA | Présentation « L'IA au service de vos projets » du 9 nov. 2026, copie de travail hors dépôt, lue sans modification ; `logiciels:18` = vue `logiciels`, ligne 18 |

**Sources web.** Les renvois [S1] à [S42] désignent les lignes du tableau de la section 12 : adresse, organisme, date affichée par la page, nature de la lecture. Toutes ont été consultées le **9 novembre 2026**. « Lue » : page, ou passage cité, lu directement. « Repérée » : seul l'extrait d'un moteur de recherche a été lu ; le fait est alors marqué « [FV, repéré] » et doit être relu avant tout usage hors de Marwin.

**Ce que ce travail n'a pas fait.** Aucun contact avec GianLuca Carlone, « Accord », un éditeur, une plateforme agréée ou un professionnel. Aucun formulaire, aucune démonstration, aucun compte, aucun essai, aucun achat. Aucune modification de la présentation, des livrables de l'audit ou d'un outil en service. Seules des pages publiques ont été lues.

**Écart avec la stratégie retenue.** Aucun. Cette fiche applique STRAT:650 (gestion immobilière exclue pour Marwin), STRAT:189 (comptes du client à son nom), STRAT:287 (cession des développements au paiement complet) et STRAT:560 (réversibilité). Elle ne fixe aucun prix et ne tranche pas entre acheter et développer.

---

## 0. L'essentiel

1. **Un logiciel sur mesure ne peut pas être la « plateforme agréée » de facturation électronique** [FV]. Une plateforme agréée est « un opérateur de dématérialisation immatriculé par l'État », après dossier et tests [S4]. Tout autre logiciel « doit être connecté avec une plateforme agréée » [S2, Q 1.1]. Le logiciel de GianLuca peut au mieux être une « solution compatible ». Devenir plateforme agréée est hors de portée de Marwin [HY].
2. **Les loyers ne suivent pas tous la même règle** [FV]. Un bail de locaux nus **sans option** pour la TVA est exonéré : ni facture électronique, ni e-reporting [S2, Q 1.2 ; S6, § 20]. **Avec option**, choisie immeuble par immeuble [S9, § 110], le loyer facturé à une entreprise établie en France passe en facture électronique, au plus tard le 1er sept. 2027 pour une PME [S3]. Les entités, les baux et les options de GianLuca sont inconnus [IN].
3. **Toute entité assujettie de GianLuca doit déjà pouvoir recevoir des factures électroniques** depuis le 1er sept. 2026, même si elle ne fait que des locations exonérées [FV] [S2, Q 1.2]. On ignore si ses entités ont choisi une plateforme [IN]. Sanction : 500 €, puis 1 000 € par période de trois mois après mise en demeure [FV] [S1, Q 2.5].
4. **Le bail commercial a changé en mai 2026** (loi n° 2026-403 du 26 mai 2026) [FV] [S13] : dépôt de garantie plafonné à un trimestre de loyer, paiement mensuel sur demande, clause d'indexation « tunnel », restitution en trois mois. Un logiciel écrit aujourd'hui doit appliquer l'ancien ou le nouveau régime selon la date de chaque bail. **La règle bouge : la tenir à jour est un coût récurrent** [HY]. Pour un logiciel du marché, l'éditeur le porte ; pour un sur mesure, Marwin ou le client.
5. **Les honoraires du bailleur liés à la gestion des loyers ne se refacturent pas au locataire commercial** [FV] [S10]. Le coût d'un logiciel ou d'un service de gestion des loyers reste au propriétaire [HY sur l'application à l'offre d'« Accord »].
6. **Gérer les biens d'autrui est une activité réglementée** : la loi n° 70-9 vise « La gestion immobilière » exercée « d'une manière habituelle » pour autrui [FV] [S41]. Une entité qui gère ses propres bâtiments n'en relève pas [HY]. Un prestataire qui gère ou encaisse pour les entités de GianLuca doit détenir la carte professionnelle [HY, à confirmer par l'avocat]. Marwin ne gère pas et n'encaisse pas (STRAT:650 ; MAJ:173) : elle outille.
7. **La caisse ne se développe jamais sur mesure** [PR, R2]. Tout logiciel qui enregistre des paiements de particuliers, même « de gestion ou de facturation », doit être certifié ou attesté [FV] [S30, §§ 10, 40]. Pour un logiciel développé pour ses propres besoins, il faut le certificat d'un organisme accrédité [FV] [S30, § 375]. Amende : 7 500 € par système [FV, repéré] [S31]. Même logique pour le logiciel hôtelier : on l'achète.
8. **Lieux recevant du public (ERP)** : registre de sécurité, qui doit aussi porter les dates des exercices d'incendie depuis le 1er juillet 2026 [FV] [S21] ; vérifications par des organismes agréés ; visites de la commission « tous les 3 ou 5 ans » [FV] [S20] ; registre public d'accessibilité [FV] [S22]. Le logiciel peut tenir le registre sous forme dématérialisée et suivre les échéances ; l'exploitant reste responsable [FV] [S20].
9. **Données et IA** : l'entité de GianLuca est responsable du traitement ; un prestataire qui héberge ou opère est sous-traitant, avec un contrat de l'article 28 [HY sur les rôles] (PRO7:580-587). Pas d'IA pour juger la solvabilité de candidats locataires personnes physiques, ni pour trier des candidats à l'emploi : ce sont des usages à haut risque (annexe III, points 5 b et 4 a) [FV] [S38], applicables au 2 déc. 2027 [FV] [S39], exclus dès maintenant [PR] (MAJ:220). Un assistant qui répond aux locataires ou aux clients doit dire qu'il est une IA (art. 50, § 1, applicable depuis le 2 août 2026) [FV] [S38].
10. **Exigences techniques minimales** [PR, R2] : comptes et hébergement au nom de l'entité, dans l'Union européenne ; sauvegardes testées ; chiffrement ; accès par rôle et par entité ; journal inaltérable ; exports ouverts et restitution sous 15 jours ouvrés (STRAT:560) ; code cédé au paiement complet (STRAT:287). Un service hébergé, même sur mesure, doit contenir les clauses de changement de fournisseur du Data Act (art. 25) ; l'interdiction des frais de changement au 12 janv. 2027 (art. 29) ne vise pas un service conçu sur mesure (art. 31) [FV] [S40].

---

## 1. Objet, périmètre et hypothèses

### 1.1 Ce que l'on sait et ce que l'on ignore

| Point | État | Source |
| --- | --- | --- |
| GianLuca a parlé d'un « logiciel de gestion de propriété » | [DR], Morgan, 9 nov. 2026 | Déclaration non écrite dans le dépôt ; R1:46 |
| Offre d'« Accord » : « 6 000 € par mois tous les trimestres » | [DR] ; contenu, durée, HT ou TTC [IN] ; prestataire non identifié [IN] | R1:30, 47-49 |
| Lecture (a) : 6 000 € par mois, facturés par trimestre | 18 000 € par trimestre, 72 000 € par an [ES] | Calcul : 6 000 × 3 ; 6 000 × 12 |
| Lecture (b) : 6 000 € par trimestre | 24 000 € par an [ES] | Calcul : 6 000 × 4 |
| Bâtiments rachetés pour 1,5 M€ | [DR] ; aucun acte, aucune adresse, entité propriétaire [IN] (U56, U57) | MAJ:34, 48-49 |
| Ancien bar-restaurant-hôtel avec cour, pour la galerie | [DR] ; reprise d'une activité d'hébergement [IN] | MAJ:155 |
| Plusieurs commerces, dont un cabaret-spectacle à côté de la galerie | [DR] ; lieux, exploitants, jauge [IN] (U59, U60) | MAJ:35, 51-52 |
| Entité qui signe ; régime de TVA ; taille au sens de la facturation électronique | [IN] (U01) | MAJ:56 |
| Administratrice centrale | [DR] ; statut, entité, pouvoirs [IN] (U51 à U54) | MAJ:33, 43-46 |

### 1.2 Trois sens, six modules

Cette fiche reprend les six modules de R1 (R1:107-114) et ajoute une couche commune. Pour chaque module, elle dit quel cadre s'applique et quel signal il donne. Le choix entre acheter, configurer et développer reste à faire avec R1 (prix) et avec le cadrage (STRAT:42).

| Module | Sens couvert | Cadre principal (sections) | Signal du cadre [PR, R2] |
| --- | --- | --- | --- |
| 1. Gestion immobilière | (1) bâtiments | TVA et facture électronique (2) ; baux, charges, dépôt, diagnostics, tertiaire (3) ; RGPD (7) | Marché ou sur mesure possibles ; les calculs réglementés demandent une veille suivie |
| 2. Hébergement | (2) logiciel hôtelier | Taxe de séjour, fiches de police, classement, carte bancaire (5) ; e-reporting (2) ; caisse (6) | **Acheter** un logiciel hôtelier du marché |
| 3. Travaux et entretien | (1) et (3) | ERP (4) ; DPE et tertiaire (3) | Configurer ou développer : peu de contraintes propres au logiciel |
| 4. Caisse et commerces | (3) exploitation | Caisse certifiée ou attestée (6) ; e-reporting (2) ; carte bancaire (5) | **Acheter** ; jamais sur mesure |
| 5. Billetterie | (3) cabaret | Caisse si elle encaisse des particuliers [HY] (6) ; jauge de l'ERP (4) ; carte bancaire (5) | **Acheter** |
| 6. Pilotage multi-lieux | (3) exploitation | RGPD, journal, accès (7, 8) ; échéances réglementaires des autres modules | Configurer ou développer : c'est là qu'un sur mesure a le plus de sens [HY] |
| T. Couche commune | Tous | Plateforme agréée (2) ; FEC et expert-comptable (6) ; RGPD et IA (7) ; sécurité (8) | **Se connecter** à des services agréés ; ne pas les reproduire |

---

## 2. Facturation électronique

### 2.1 Calendrier, taille et sanctions

| Obligation | Grandes entreprises et ETI | PME et microentreprises | Source |
| --- | --- | --- | --- |
| Recevoir les factures électroniques par une plateforme agréée | Depuis le 1er sept. 2026 | **Depuis le 1er sept. 2026** | [FV] [S3, p. 1] ; [S2, Q 1.2] |
| Émettre des factures électroniques | Depuis le 1er sept. 2026 | **Au plus tard le 1er sept. 2027** ; entrée anticipée possible | [FV] [S3, p. 2] ; [S2, Q 1.3] |
| Transmettre les données de transaction et de paiement (e-reporting) | Même calendrier que l'émission | Au plus tard le 1er sept. 2027 | [FV] [S2, Q 1.3] |

- **Taille.** Elle suit les critères de la loi de modernisation de l'économie : microentreprise, moins de 10 personnes et au plus 2 M€ de chiffre d'affaires ou de bilan ; PME, moins de 250 personnes [FV] [S1, Q 1.1]. Les entités de GianLuca sont probablement des PME ou des microentreprises [HY] ; leur taille réelle est [IN].
- **Sanctions.** 50 € par facture non émise sous forme électronique, plafonnés à 15 000 € par année civile, la première infraction n'étant pas sanctionnée [FV] [S1, Q 2.4]. Sans plateforme de réception : 500 € trois mois après une mise en demeure, puis 1 000 € par nouvelle période de trois mois [FV] [S1, Q 2.5].
- **Holding.** Une holding passive, non assujettie, est hors du champ ; une holding animatrice qui facture ses filiales y entre [FV] [S1, Q 1.8]. La structure de détention de GianLuca est [IN].
- **Quatre mentions nouvelles** : SIREN du client, nature des opérations (biens, services ou les deux), option pour la TVA d'après les débits, adresse de livraison si elle diffère [FV] [S8]. La DGFiP les dit obligatoires dès le 1er sept. 2026 ; la fiche F31808 les rattache au déploiement progressif : les deux sources officielles divergent [FV] (R2F:296-302). Lecture prudente : les porter dès maintenant [PR] (R2F:298-305 ; SYN-D:297).

### 2.2 Les plateformes agréées, et pourquoi le logiciel ne peut pas en être une

- **Définition.** « Une plateforme agréée est un opérateur de dématérialisation immatriculé par l'État. » [FV] [S4]. Le candidat dépose un dossier qui montre sa conformité fiscale, la sécurité de ses infrastructures et de ses données, et son interopérabilité avec le portail public et les autres plateformes. « L'immatriculation définitive n'est accordée qu'après réussite des tests d'interopérabilité en conditions réelles. » [FV] [S4]. L'immatriculation vaut trois ans, renouvelables [FV] [S5].
- **Monopole des fonctions.** « Seule une plateforme agréée est habilitée à assurer toutes les fonctionnalités prévues par la réforme » : émettre, transmettre et recevoir les factures, transmettre les données à l'administration [FV] [S5]. Un prestataire qui n'est pas plateforme agréée ne peut ni transmettre les factures aux plateformes des clients, ni recevoir pour l'entreprise, ni transmettre les données à l'administration [FV] [S5].
- **Solution compatible.** « Si vous passez par une solution compatible (logiciel de facturation, par exemple), celle-ci doit être connectée avec une plateforme agréée. » [FV] [S2, Q 1.1]. Un logiciel existant peut continuer à servir, « charge à lui de se connecter à une plateforme agréée » [FV] [S3, p. 2]. La DGFiP distingue deux logos, « plateforme agréée » et « solution compatible » [FV] [S4].
- **Conclusion.** Le logiciel sur mesure de GianLuca ne peut pas être sa plateforme agréée [FV]. Il prépare les factures et les données, puis les fait passer par la plateforme que l'entité a choisie [FV]. Faire immatriculer Marwin comme plateforme agréée demanderait un dossier de sécurité et des tests d'interopérabilité hors de proportion avec deux associés et un client [HY].
- **Choix et format.** L'entité choisit sa plateforme de réception ; un fournisseur ne peut pas lui imposer un format [FV] [S1, Q 2.3]. Si un tiers facture au nom de l'entité (mandat de facturation), la facture passe en principe par la plateforme de l'émetteur, c'est-à-dire de l'entité [FV] [S1, Q 2.2].

### 2.3 Conséquences pour les loyers, cas par cas

**Règle générale** [FV] : seules les opérations dans le champ de la TVA « et qui ne sont pas exonérées en application des articles 261 à 261 E du CGI » relèvent de la facture électronique ou de l'e-reporting [S2, Q 1.2]. Les opérations exonérées par ces articles sont exclues de la transmission des données et « ne donnent, par ailleurs, pas lieu à facturation » [S6, § 20, remarque 2]. Le taux zéro, lui, n'est pas exclu [S7].

| Situation | TVA | Facture électronique | E-reporting | Document remis au locataire | Source |
| --- | --- | --- | --- | --- | --- |
| Local commercial ou professionnel **nu, sans option** | Exonéré (CGI, art. 261 D) | Non : pas de facture obligatoire | Non | Avis d'échéance et quittance, par usage [HY] | [FV] [S2, Q 1.2] ; [S6, § 20] |
| Local nu **avec option** (CGI, art. 260, 2°) | Taxable | Oui, si le locataire est un assujetti établi en France ; PME : au plus tard le 1er sept. 2027 | Données de paiement : statut « encaissée » quand la TVA est exigible à l'encaissement, sauf option pour les débits (R2F:295) | Facture | [FV] [S9, §§ 10, 110] ; [S2, Q 1.1] |
| Locataire non assujetti, local nu avec option | Taxable si le bail « fasse mention expresse de l'option » | Non (client non assujetti) | Oui, données de transaction | Facture | [FV] [S9, §§ 10, 50] ; [S2, Q 1.1] |
| Locaux nus destinés à l'habitation | Option impossible | Non | Non | Quittance gratuite sur demande, avec le détail loyer et charges ; dématérialisée avec l'accord exprès du locataire (loi n° 89-462, art. 21) | [FV] [S9, § 10] ; [FV, repéré] [S17] |
| Locaux équipés pour l'activité (« aménagés ») | Taxable de plein droit [HY, non relu ce jour] | Comme avec option | Comme avec option | Facture | — |
| Hébergement hôtelier, client particulier | Taxable | Non | Oui, données de transaction ; PME au plus tard le 1er sept. 2027 | Note ou facture ; taxe de séjour « au réel » sur une ligne distincte | [FV] [S2, Q 1.1, 1.3] ; [S23] |
| Hébergement, client entreprise établie en France | Taxable | Oui | Données de paiement si TVA à l'encaissement | Facture | [FV] [S2, Q 1.1] |
| Charges et taxe foncière refacturées | Suivent le régime du loyer [HY, à valider par l'expert-comptable] | Idem | Idem | Avec l'appel de loyer | — |

**Trois conséquences** :

1. **Un même propriétaire peut avoir les deux régimes** : l'option se prend immeuble par immeuble [FV] [S9, § 110]. Le logiciel doit donc porter le régime au niveau de l'immeuble et du bail [PR, R2].
2. **Même sans aucune facture à émettre, l'entité doit recevoir.** Un assujetti qui ne réalise que des opérations hors du dispositif « doit être en capacité de recevoir les factures électroniques » de ses fournisseurs, depuis le 1er sept. 2026 [FV] [S2, Q 1.2]. Les factures de travaux, d'énergie et d'entretien des bâtiments arrivent donc par une plateforme [HY sur la situation des entités].
3. **Si les bâtiments sont loués aux sociétés d'exploitation de GianLuca** (galerie, cabaret, commerces), avec option, les loyers entre ses propres sociétés deviennent des factures électroniques [HY : schéma « propriétaire distinct de l'exploitant », MAJ:148].

### 2.4 Ce que le logiciel doit faire [PR, R2]

- Porter, par immeuble et par bail, le régime de TVA, la date de l'option et sa mention au bail.
- Porter, par locataire, son SIREN, sa qualité d'assujetti et son lieu d'établissement : ce sont eux qui décident du canal (facture électronique, e-reporting ou rien) [FV] [S2, Q 1.1].
- Produire les données de facture avec les quatre mentions, les transmettre à la plateforme de l'entité et récupérer les statuts (déposée, rejetée, encaissée).
- Avoir **une seule source** pour chaque facture : soit le logiciel, soit la plateforme, jamais les deux.
- Récupérer les factures fournisseurs reçues par la plateforme et les rapprocher des devis, bons de commande et budgets.
- Archiver factures et pièces pendant la durée légale (section 6.2).
- **Ne jamais** émettre une facture électronique pour un loyer exonéré.

---

## 3. Gestion locative et baux commerciaux

### 3.1 Indices et révision du loyer

| Règle | Contenu | Source |
| --- | --- | --- |
| Indice d'un bail commercial | ILC pour une activité commerciale ou artisanale ; ILAT pour les activités tertiaires autres (bureaux, professions libérales, entrepôts logistiques). L'ICC ne sert plus aux révisions et renouvellements depuis septembre 2014, mais reste possible dans une clause d'échelle mobile | [FV] [S12] |
| Publication | Indices trimestriels de l'Insee, avec deux trimestres de décalage ; séries 001532540 (ILC) et 001617112 (ILAT) | [FV] [S12] |
| Révision triennale (C. com., L145-38) | Demande possible trois ans après l'entrée, le renouvellement ou la précédente révision ; plafond : variation de l'ILC ou de l'ILAT ; formule : loyer × (dernier indice publié ÷ indice de référence) | [FV] [S11] |
| Clause d'échelle mobile (L145-39) | Révision automatique à la périodicité choisie ; si le loyer varie de « plus d'¼ » par rapport au prix précédemment fixé, chaque partie peut demander une révision à la valeur locative | [FV] [S11] |
| Lissage | Après un déplafonnement, la hausse ne peut dépasser, pour une année, « 10 % du loyer acquitté au cours de l'année précédente » | [FV] [S11] |
| Clause « tunnel » | Pour les baux conclus ou renouvelés à compter du 28 mai 2026, la clause peut encadrer la variation annuelle de l'indice, « dans les mêmes proportions, à la hausse et à la baisse » | [FV] [S13] ; F31925 cite des bornes de ± 3 % ou ± 5 % [S11] : texte de loi non relu [IN] |
| Logement (IRL) | Révision une fois par an si le bail le prévoit ; formule par l'IRL du même trimestre ; non rétroactive ; perdue au-delà d'un an ; **interdite** pour un logement classé F ou G depuis le 24 août 2022 en métropole | [FV] [S15] |

### 3.2 Ce que la loi du 26 mai 2026 change

| Changement | Baux concernés | Source |
| --- | --- | --- |
| Paiement **mensuel** du loyer à la demande du locataire (commerce de détail ou de gros, services commerciaux ou artisanaux), s'il n'a ni arriéré ni montant contesté | Baux en cours au 26 mai 2026, nouveaux et renouvelés | [FV] [S13] ; [S11] (L145-32-1) |
| Dépôt de garantie plafonné à **un trimestre** de loyer, autres garanties comprises | Baux signés ou renouvelés à compter du 28 mai 2026 | [FV] [S13] ; [S14] |
| Restitution du dépôt sous **3 mois** après la remise des clés ; mainlevée des autres garanties sous 6 mois | Baux en cours au 26 mai 2026, clés rendues après le 26 août 2026 | [FV] [S13] |
| En cas de vente, de donation ou de succession, le **nouveau bailleur** restitue le dépôt ; les autres garanties tombent | Transferts à compter du 26 août 2026 | [FV] [S13] |
| Clause d'indexation « tunnel » | Baux conclus ou renouvelés à compter du 28 mai 2026 | [FV] [S13] |

**Conséquence** [HY] : un logiciel doit dater chaque bail et appliquer la règle de sa date. En six mois, quatre règles de calcul ont changé. Pour un logiciel du marché, l'éditeur fait cette mise à jour ; pour un sur mesure, il faut une veille et une maintenance payées (section 9).

### 3.3 Charges, taxe foncière et travaux

| Règle | Contenu | Source |
| --- | --- | --- |
| Inventaire des charges (C. com., L145-40-2) | Le bail, ou une annexe, contient un inventaire précis et limitatif des catégories de charges, impôts et taxes, et leur répartition. Sans inventaire, « le bailleur ne peut pas facturer de charges au locataire » | [FV] [S10] |
| État récapitulatif annuel (R145-35 à R145-37) | Adressé au locataire « au plus tard le 30 septembre de l'année qui suit celle où il est établi » ; en copropriété, dans les 3 mois après la reddition des comptes | [FV] [S10] |
| Charges qui restent au bailleur | Grosses réparations de l'article 606 du code civil ; travaux de vétusté ou de mise en conformité qui en relèvent (accessibilité, sécurité incendie, électricité, travaux ordonnés par l'administration) ; « Les honoraires du bailleur liés à la gestion des loyers du local » ; charges des locaux vacants ou imputables à d'autres locataires | [FV] [S10] |
| Taxe foncière | Payée par le bailleur ; refacturable seulement si elle est « clairement identifiée » dans le bail. CFE et CVAE restent au locataire | [FV] [S10] |
| État des travaux tous les 3 ans | Dans les 2 mois de chaque échéance triennale : travaux prévus sur 3 ans avec budget, bilan des travaux des 3 années passées avec leur coût ; justificatifs sur demande | [FV] [S10] |

### 3.4 Dépôt de garantie

- **Bail commercial** : plafonné à un trimestre pour un bail signé ou renouvelé à compter du 28 mai 2026 [FV] [S14] ; restitution et transfert : tableau 3.2.
- **Logement vide** : au plus un mois de loyer hors charges, non révisable en cours de bail [FV] [S16].

### 3.5 Annexes et diagnostics d'un bail commercial

Le bailleur annexe [FV] [S14] : l'état des lieux ; l'inventaire des charges ; la liste des travaux des 3 dernières années et des 3 suivantes ; le **DPE** ; l'état des risques, de moins de 6 mois, si le local est dans une zone concernée ; la dernière attestation annuelle **OPERAT** pour un bâtiment tertiaire de plus de 1 000 m², pour information ; l'**annexe environnementale** pour des locaux de bureaux ou de commerces d'au moins 2 000 m². Le diagnostic amiante est tenu à jour et mis à disposition du locataire, sans être annexé [FV] [S14].

**DPE affiché dans un ERP** : obligatoire notamment pour un bâtiment de plus de 500 m² qui abrite un ERP de catégorie 1 à 4 et fait l'objet d'un DPE lors d'une construction, d'une vente ou d'une location ; affiché près de l'entrée ; mise en demeure, puis amende jusqu'à 1 500 € [FV] [S19].

### 3.6 Éco énergie tertiaire (« décret tertiaire »)

- **Champ** : bâtiments, parties ou ensembles de bâtiments sur une même unité foncière ou un même site, qui hébergent des activités tertiaires sur une surface de plancher cumulée d'au moins 1 000 m² [FV] [S18 ; S42].
- **Objectifs** : − 40 % en 2030, − 50 % en 2040, − 60 % en 2050 [FV] [S42].
- **Déclaration** : consommations de l'année précédente sur OPERAT, « au plus tard le 30 septembre » de chaque année, par le propriétaire et, s'il y en a, le preneur, chacun pour sa part ; année de référence à choisir avant le 30 sept. 2027 [FV] [S18].
- **Sanctions** : mise en demeure à 3 mois, publication des mises en demeure restées sans effet, puis amende administrative [FV] [S18].
- **Pour GianLuca** : galerie, cabaret, commerces et hôtel sont des activités tertiaires [HY]. Si les bâtiments d'un même site dépassent 1 000 m² cumulés, l'obligation s'applique. Surfaces [IN] (U56).

### 3.7 Obligations du bailleur, quittances, relances et gestion pour autrui

- **Contrats, bail, travaux** : décisions réservées à GianLuca ou au signataire habilité ; Marwin prépare le dossier (STRAT:580) ; les questions juridiques et fiscales vont au professionnel (STRAT:581).
- **Relances** : préparées, signées par l'entité, encaissées sur ses comptes ; le recouvrement amiable pour autrui est réglementé (CPCE, R124-2) [FV] (SYN-D:420). Marwin n'envoie aucune relance en son nom [PR] (STRAT:650).
- **Gestion pour autrui** : la loi n° 70-9 s'applique aux personnes qui, « d'une manière habituelle, se livrent ou prêtent leur concours, même à titre accessoire », aux opérations sur les biens d'autrui relatives notamment à « La gestion immobilière » [FV] [S41]. Un éditeur qui fournit seulement un logiciel n'en relève pas [HY]. Un prestataire qui encaisse les loyers ou gère les baux pour l'entité propriétaire en relève [HY, à confirmer par l'avocat].

### 3.8 Ce que le logiciel doit faire [PR, R2]

- Dater chaque bail et lui associer son régime : indice, période de référence, clause (triennale, échelle mobile, tunnel), plafond du dépôt, périodicité de paiement.
- Importer les indices de l'Insee et calculer par **formule testée**, jamais par un modèle de langage (PRO7:69). Garder un jeu d'essai de cas connus, rejoué à chaque changement de règle.
- Tenir l'inventaire des charges par bail ; refuser les catégories non refacturables (606, honoraires de gestion des loyers) ; produire l'état récapitulatif avant le 30 septembre.
- Rappeler les échéances : révision triennale, état triennal des travaux, fin de bail, restitution du dépôt, validité des diagnostics, déclaration OPERAT.
- Produire quittances et avis d'échéance ; préparer les relances, qui partent sous le nom de l'entité après validation humaine (PRO7:22).
- Ne jamais encaisser sur un compte autre que celui de l'entité.

---

## 4. Établissements recevant du public (ERP)

| Obligation | Contenu | Qui la porte | Source |
| --- | --- | --- | --- |
| Classement | Type et catégorie selon l'activité et l'effectif : galerie en M ou T, 5e catégorie jusqu'à 200 personnes ; cabaret en L, 4e catégorie au-delà de 50 personnes ; N ou P si repas ou danse | Exploitant | [FV] (SYN-D:532 ; MAJ:185) |
| Registre de sécurité (CCH, R143-44) | Travaux d'aménagement (dates, nature, intervenants) ; personnel du service de sécurité ; consignes d'incendie et d'évacuation adaptées aux handicaps ; dates des contrôles et vérifications et leurs observations ; **dates des exercices de sécurité incendie** (version en vigueur depuis le 1er juillet 2026, décret n° 2025-1100) | Exploitant | [FV] [S21] |
| Forme du registre | « Le registre peut se présenter sous forme papier ou dématérialisée. Il est mis à jour dès que des informations changent. » Il est présenté à la commission | Exploitant | [FV] [S20] |
| Vérifications techniques (R143-34) | Électricité, éclairage, alarme, désenfumage, ascenseurs, extincteurs… vérifiés pendant la construction et périodiquement en exploitation par des personnes ou organismes agréés ; procès-verbaux tenus à disposition de la commission | Constructeur, installateur, exploitant | [FV] [S20 ; S21] |
| Visites de la commission (R143-41) | « tous les 3 ou 5 ans » selon le type et la catégorie ; pas de visite périodique pour un ERP de 5e catégorie **sans** locaux d'hébergement ; fermeture possible par le maire en cas de danger | Exploitant présent ou représenté | [FV] [S20 ; S21] |
| Registre public d'accessibilité | Prestations ; pièces administratives (attestations, dérogations, calendrier d'agenda programmé) ; pièces techniques (maintenance des ascenseurs, élévateurs, rampes) ; pour les catégories 1 à 4, attestation annuelle de formation du personnel d'accueil ; consultable à l'accueil, éventuellement dématérialisé, ou sur le site internet | Exploitant | [FV] [S22] (décret n° 2017-431 ; arrêté du 19 avril 2017) |
| Travaux dans un ERP | Autorisation de travaux : 4 mois ; permis de construire : 5 mois | Propriétaire, exploitant | [FV] (MAJ:167) |

**Ce que le logiciel doit faire** [PR, R2] : un registre de sécurité dématérialisé par établissement, avec toutes les rubriques de R143-44 ; un échéancier par installation et par organisme ; les procès-verbaux attachés ; un export lisible pour la commission ; le registre d'accessibilité et sa fiche de synthèse, publiables sur le site. **Il ne dit jamais qu'un lieu est « conforme »** : seuls la commission, le maire et les organismes agréés le disent [PR] (MAJ:267, « documents conformes » à corriger).

---

## 5. Hébergement touristique, si l'hôtel reprend [IN]

| Obligation | Contenu | Source |
| --- | --- | --- |
| Taxe de séjour | Instituée « au réel » ou « au forfait » par la commune ou l'intercommunalité. Au réel : perçue par le logeur « avant le départ des personnes hébergées », sur une ligne distincte de la facture, hors base de TVA, reversée aux dates fixées par la délibération. Au forfait : déclaration en mairie au plus tard un mois avant la période, montant inclus dans la base de TVA. Taxation d'office possible après mise en demeure | [FV] [S23] ; existence et tarifs à Cosne-Cours-sur-Loire [IN] |
| Fiche individuelle de police (CESEDA, R814-1 à R814-3) | Tout client de nationalité étrangère la remplit et la signe à l'arrivée : nom, date et lieu de naissance, nationalité, dates d'arrivée et de départ prévue, entre autres ; conservée **6 mois** ; remise à la police ou à la gendarmerie seulement sur demande, éventuellement par voie électronique | [FV] [S24] |
| Destruction des fiches | Au terme des 6 mois, destruction définitive et sécurisée | [FV, repéré] [S24] (délibération CNIL n° 2016-176) |
| Classement en étoiles | Volontaire ; visite par un organisme accrédité ; prononcé par Atout France ; valable 5 ans | [FV, repéré] [S25] ; référentiel en vigueur en 2027 [IN] |
| Paiement par carte | La norme PCI DSS n'est pas une loi : c'est un standard privé imposé par le contrat avec la banque. Pour rester dans le questionnaire le plus léger (SAQ A, vente à distance), aucune donnée de carte n'est stockée, traitée ou transmise par les systèmes du commerçant ; tout passe par un prestataire de paiement conforme | [FV, repéré, standard privé] [S26] |
| Caisse du bar et du restaurant | Caisse certifiée ou attestée (section 6.3) | [FV] [S30] |
| ERP avec locaux à sommeil | Soumis aux visites périodiques de la commission, même en 5e catégorie | [FV, a contrario] [S20] ; fréquence exacte [IN] |
| Facture électronique | Clients particuliers : e-reporting ; clients entreprises : facture électronique (tableau 2.3) | [FV] [S2, Q 1.1] |

**Signal** [PR, R2] : un logiciel hôtelier du marché fait déjà la taxe de séjour, les fiches de police, la facturation, la liaison avec les sites de réservation et souvent la caisse (R1:132-148). Le refaire sur mesure ferait porter à Marwin la caisse, la carte bancaire et les données de voyageurs. Le sur mesure se limite à relier ce logiciel au pilotage (module 6).

---

## 6. Comptabilité, conservation et caisse

### 6.1 Fichier des écritures comptables (FEC)

- L'entreprise qui tient une comptabilité informatisée remet en cas de vérification une copie de ses écritures au format de l'article A. 47 A-1 du LPF, dès la première intervention sur place [FV, repéré] [S28].
- Amende pour défaut ou non-conformité : 5 000 €, ou 10 % des droits rappelés si ce montant est plus élevé, par exercice (CGI, art. 1729 D) [FV, repéré] [S28].
- **Pour le logiciel** [PR, R2] : le FEC est produit par le **logiciel comptable** de l'entité ou de son expert-comptable. Le logiciel de gestion n'est pas une comptabilité : il exporte des pièces et des écritures préparatoires dans un format convenu avec l'expert-comptable. Marwin ne tient pas la comptabilité (STRAT:650).

### 6.2 Conservation des pièces

| Document | Durée | Source |
| --- | --- | --- |
| Livres et registres comptables | 10 ans à partir de la clôture de l'exercice | [FV] [S27] |
| Pièces justificatives (bons de commande, factures clients et fournisseurs) | 10 ans à partir de la clôture de l'exercice | [FV] [S27] |
| Documents sur lesquels s'exerce le contrôle fiscal | 6 ans | [FV] [S27] |
| Contrats et correspondance commerciale | 5 ans | [FV] [S27] |
| Contrats d'acquisition ou de cession d'immeubles | 30 ans | [FV] [S27] |
| Documents bancaires | 5 ans | [FV] [S27] |

**Tension avec le RGPD** [HY] : ces durées obligent à garder des données personnelles (locataires, clients) en archive intermédiaire, à accès restreint, puis à les purger (section 7.3).

### 6.3 Logiciels de caisse

- **Obligation** (CGI, art. 286, I, 3° bis) : les assujettis qui encaissent des particuliers utilisent un logiciel ou système de caisse qui respecte des conditions « d'inaltérabilité, de sécurisation, de conservation et d'archivage » [FV] [S29 ; S30]. Ceux qui ne travaillent qu'avec des professionnels sont exclus [FV] [S30, § 10].
- **Preuve** : certificat d'un organisme accrédité, ou attestation individuelle de l'éditeur, de nouveau admise depuis le 21 février 2026 (loi n° 2026-103 du 19 février 2026, art. 125) [FV] [S29].
- **Champ large** : tout logiciel « dispose d'une fonctionnalité de caisse » s'il enregistre un paiement sans passer en même temps une écriture comptable, « quelle que soit sa qualification (de caisse, comptable, de gestion ou de facturation) » ; seule la fonction de caisse doit être sécurisée [FV] [S30, §§ 30, 40, 70].
- **Sur mesure** : les logiciels « développés en interne », y compris par un intégrateur extérieur, sont concernés [FV] [S30, § 45]. L'éditeur est « la personne qui détient le code source » [FV] [S30, § 300]. Un assujetti qui développe pour ses propres besoins doit obtenir un **certificat** d'organisme accrédité [FV] [S30, § 375]. Une modification des fonctions de sécurité invalide le certificat ou l'attestation, et l'intégrateur qui la fait devient éditeur [FV] [S30, § 315].
- **Amende** : 7 500 € par logiciel ou système non justifié [FV, repéré] [S31].
- **Conséquence** [PR, R2] : aucune fonction d'encaissement de particuliers dans un logiciel sur mesure (loyers d'habitation compris, si un module encaissait). Caisses, billetterie et logiciel hôtelier sont achetés ; le sur mesure importe seulement leurs clôtures.

### 6.4 Lien avec l'expert-comptable [PR, R2]

À fixer avec lui, avant tout développement : plan de comptes et codes analytiques par entité et par lieu ; format des exports (écritures, pièces, journaux de caisse) ; qui saisit quoi ; calendrier mensuel ; qui valide. Les pièces partent vers lui « après validation » (PIA, `cat-finance:10`), jamais automatiquement (MAJ:267).

---

## 7. Données personnelles et IA

### 7.1 Rôles et contrats

| Personnes concernées | Responsable du traitement [HY] | Sous-traitants possibles | Source |
| --- | --- | --- | --- |
| Locataires, cautions, candidats | L'entité propriétaire | Éditeur ou hébergeur du logiciel ; Marwin si elle héberge ou opère ; administrateur de biens éventuel | PRO7:580-587 |
| Clients de l'hôtel, du cabaret, des commerces | L'entité exploitante | Logiciel hôtelier, caisse, billetterie, prestataire de paiement | Idem |
| Salariés, artistes, administratrice | L'entité employeuse | Paie, planning, logiciel de gestion | Idem |

- **Contrat de l'article 28** avec chaque sous-traitant : objet, durée, nature et finalité, types de données, catégories de personnes, obligations ; instructions documentées, y compris pour les transferts ; sous-traitants ultérieurs autorisés par écrit [FV] [S34 ; S35]. Aucune donnée réelle avant ce contrat (STRAT:669).
- **Registre des traitements** (art. 30), **sécurité** (art. 32), **notification d'une violation à la CNIL sous 72 heures** (art. 33) [FV] [S34]. L'incident de données de novembre 2026 [DR] montre que ce n'est pas théorique (MAJ:65).

### 7.2 Hébergement et transferts

- Le RGPD n'impose pas d'héberger dans l'Union, mais tout transfert hors de l'Espace économique européen demande une base (décision d'adéquation, clauses types) et, avec les clauses types, une analyse d'impact des transferts [FV] [S34, art. 44 à 49 ; S36].
- Anthropic et OpenAI n'étaient pas inscrits au Data Privacy Framework le 4 nov. 2026 [MM] (PRO7:595-596) ; non revérifié ce jour [IN].
- **Règle** [PR, R2] : hébergement dans l'Union européenne, sous-traitants listés ; appels à une IA hors de l'Union seulement sur données pseudonymisées, avec offre professionnelle et entraînement désactivé (PRO7:605-616).

### 7.3 Durées de conservation

| Données | Durée indicative | Source |
| --- | --- | --- |
| Prospects d'une location | 3 ans après le dernier contact | [FV] [S32, § 53] |
| Solvabilité des candidats | 3 mois en base active | [FV] [S32, § 53] |
| Locataire retenu | Durée du bail jusqu'à la clôture des comptes, puis archive intermédiaire : 3 ans en gestion directe, 5 ans en gestion déléguée | [FV] [S32, § 53] |
| Archive plus longue | Seulement pour une obligation légale (comptable, fiscale) ou une preuve, dans la limite de la prescription | [FV] [S32, § 54] |
| Fiches de police | 6 mois | [FV] [S24] |
| Salariés | Référentiel de la CNIL adopté le 29 janv. 2026, publié au JO le 2 avril 2026 ; durées non lues [IN] | [FV] [S33] |

**Limite** : le référentiel de 2021 vise les locaux d'**habitation** [FV] [S32, § 1]. Pour les baux commerciaux, il guide les durées des personnes physiques en cause (gérants, cautions, interlocuteurs) [HY]. Un nouveau référentiel « gestion locative » était en projet fin 2025 pour le logement social [FV, repéré] ; son sort est [IN].

### 7.4 Règlement européen sur l'IA

| Point | Règle | Source |
| --- | --- | --- |
| Assistant qui parle aux locataires, aux clients ou au public | Les personnes doivent être informées qu'elles interagissent avec une IA (art. 50, § 1) ; règlement applicable depuis le 2 août 2026 (art. 113) | [FV] [S38] |
| Contenus générés | Marquage lisible par machine (art. 50, § 2) ; délai jusqu'au 2 déc. 2026 pour les systèmes mis sur le marché avant le 2 août 2026 ; hypertrucages signalés (art. 50, § 4) | [FV] [S38] |
| Solvabilité de personnes physiques | Haut risque (annexe III, point 5 b), sauf détection de fraude | [FV] [S38] |
| Recrutement, évaluation de salariés | Haut risque (annexe III, point 4 a et b) | [FV] [S38] |
| Date du haut risque (annexe III) | 2 déc. 2027 | [FV] [S39 ; S38, art. 113] |
| Maîtrise de l'IA (art. 4) | Réécrit : fournisseurs et déployeurs « prennent des mesures pour favoriser » la maîtrise de l'IA de leur personnel | [FV] [S39] |
| Rôle de Marwin | Déployeur quand elle utilise un assistant ; fournisseur si elle livre un assistant sous son nom | [FV texte ; HY qualification] (PRO7:570-574) |

**Règles pour le logiciel** [PR] : aucune notation de candidats locataires ni de salariés, même avant le 2 déc. 2027 (MAJ:220) ; mention « vous échangez avec une IA » pour tout agent qui répond à l'extérieur (MAJ:223) ; aucune décision ni aucun envoi automatique vers l'extérieur (PRO7:22) ; montants par formule, jamais par le modèle (PRO7:69).

---

## 8. Exigences techniques minimales [PR, R2]

| Domaine | Exigence minimale | Source ou repère |
| --- | --- | --- |
| Comptes | Tous les comptes (hébergement, base, dépôt de code, plateforme, IA) au nom de l'entité dès le premier jour ; Marwin y est collaboratrice | STRAT:189, 560 |
| Hébergement | Dans l'Union européenne ; fournisseur et sous-traitants listés au contrat de l'article 28 ; aucune donnée dans un dépôt de code | [S34 ; S36] ; PRO7:626 |
| Sauvegardes | Export quotidien ; complète chaque semaine ; trois copies, deux supports, une hors du fournisseur principal ; copies chiffrées ; perte maximale 24 h ; reprise en un jour ouvré | PRO7:620-627 |
| Restauration | Testée chaque mois les trois premiers mois, puis chaque trimestre, dans un espace neuf, sans rejouer les envois | PRO7:628 |
| Chiffrement | En transit et au repos ; clés et secrets dans un coffre, jamais dans le code ni dans un journal | PRO7:550-568 ; [S37] |
| Accès par rôle | Rôles au moins : direction (GianLuca), administratrice, gestionnaire de lieu, expert-comptable en lecture, Marwin en maintenance ; **cloisonnement par entité** ; double authentification ; lecture seule par défaut ; revue des accès chaque trimestre | [S34, art. 32] ; PRO7:557 |
| Journal | Inaltérable, hors de portée des automatismes ; qui, quoi, quand, sur quelle donnée ; demande → autorisation → action → résultat ; durée alignée sur le registre RGPD | PRO7:629 |
| Calculs réglementés | Indexation, charges, dépôt, taxe de séjour : formules testées sur un jeu de cas, rejoué à chaque changement de règle | PRO7:69 |
| Facturation | Connexion à la plateforme agréée de l'entité ; une seule source par facture | Section 2 |
| Réversibilité | Exports complets en formats ouverts (CSV et JSON avec description des champs, documents d'origine) ; restitution sous 15 jours ouvrés ; sortie à blanc avant le bilan de mai 2027 | STRAT:560 ; PRO7:650-651 |
| Data Act | Si un prestataire héberge et exploite le service : clauses de changement de fournisseur (préavis de 2 mois au plus, transition de 30 jours au plus) ; plus aucuns frais de changement à partir du 12 janv. 2027 pour un service commercial standard ; un service conçu sur mesure est dispensé de l'article 29, pas de l'article 25 | [FV] [S40, art. 25, 29, 31] ; SYN-D:507-510 |
| Propriété du code | Cession écrite des développements propres au paiement complet, chaque droit mentionné ; licence perpétuelle et non exclusive sur les composants génériques ; code sur un dépôt au nom de l'entité ; liste des dépendances et de leurs licences | STRAT:287 ; SYN-D:488, 497 |
| Exploitation | Bouton d'arrêt ; mode manuel écrit et testé ; second fournisseur d'IA configuré | PRO7:630-633 |
| Veille réglementaire | Une personne nommée suit les textes des sections 2 à 7 et déclenche les mises à jour ; jeu d'essai rejoué | Section 3.2 |

**Si Marwin hébergeait le logiciel sur ses propres comptes**, elle porterait d'un coup quatre régimes : sous-traitant RGPD, fournisseur de service de traitement de données au sens du Data Act, éventuel éditeur d'une fonction de caisse, fournisseur d'IA si l'assistant est à son nom [HY]. D'où la règle des comptes au nom de l'entité (STRAT:189) et une RC professionnelle qui couvre le cyber et les données (STRAT:554).

---

## 9. Ce que ce cadre change pour l'offre d'« Accord » et pour Marwin

### 9.1 Questions de conformité à poser sur l'offre, par l'intermédiaire de GianLuca

Aucun contact direct ; le devis écrit est demandé par GianLuca, après D03 et D08 (R1:37 ; MAJ:367).

| Question | Pourquoi | Section |
| --- | --- | --- |
| Que couvrent les 6 000 € : licence, développement, service de gestion, maintenance ? Par mois ou par trimestre ? HT ? Durée ? | Lecture (a), 72 000 € par an, ou lecture (b), 24 000 € par an [ES] | 1.1 |
| Si c'est un service de gestion : numéro de carte « gestion immobilière » et garantie financière ? | Loi n° 70-9 [FV] [S41] ; garantie [HY, non relue] | 3.7 |
| Ses honoraires seront-ils refacturés aux locataires commerciaux ? | Interdit pour la gestion des loyers [FV] [S10] | 3.3 |
| Le logiciel est-il « solution compatible » ? Relié à quelle plateforme agréée ? | Facturation électronique [FV] [S2 ; S4] | 2 |
| Gère-t-il les règles de mai 2026 (dépôt, paiement mensuel, tunnel) et le régime de TVA par immeuble ? | [FV] [S13 ; S9] | 2.3, 3.2 |
| Où sont hébergées les données ? Quels sous-traitants ? Contrat de l'article 28 ? | RGPD [FV] [S34] | 7 |
| Export complet, délai, format ; frais de sortie après le 12 janv. 2027 ? | Data Act [FV] [S40] | 8 |
| S'il y a développement : à qui appartient le code ? | Propriété (SYN-D:488) | 8 |
| Contient-il une caisse ou un module hôtelier ? Certificat ou attestation ? | [FV] [S30] | 5, 6.3 |
| Utilise-t-il de l'IA ? Laquelle, où, avec quelle mention ? | [FV] [S38] | 7.4 |

### 9.2 Conséquences pour la position « mieux et moins cher grâce à l'IA » [DR]

- **L'IA réduit le coût d'écriture du code ; elle ne réduit ni la responsabilité réglementaire, ni la veille, ni les briques à acheter** [HY]. Plateforme agréée, caisse, logiciel hôtelier, prestataire de paiement et logiciel comptable restent payants, avec ou sans sur mesure [HY]. R1 arrive à la même conclusion par les prix (R1:35).
- **La maintenance réglementaire pèse sur la capacité de Marwin** : au plus 10 JP facturables par mois la première année (STRAT:485) ; au plus 0,5 JP de maintenance par mois et par processus en exploitation (STRAT:349) ; exploitation au plus tôt au 7e mois (STRAT:339). Un logiciel de gestion des baux qui suit les textes de 2026 et 2027 ne tient dans ces limites que si son périmètre est étroit [HY].
- **Tout devis de Marwin** suit la règle des lots : plancher de 750 € HT × la borne haute des JP estimées, jamais remisé (CAT:71 ; STRAT:396). Rien ne se développe avant le cadrage payé (STRAT:42) et une entité nommée avant le 15 déc. 2026 (STRAT:44).
- **Marwin ne remplace pas un administrateur de biens** : si l'offre d'« Accord » est un service de gestion, la seule alternative de Marwin est un outil utilisé par l'administratrice de GianLuca ou par l'entité elle-même (MAJ:79 ; STRAT:650) [HY].

---

## 10. Questions ouvertes et professionnels à consulter

| N° | Question | Qui répond | Ce qu'elle bloque |
| --- | --- | --- | --- |
| Q1 | Entités : propriétaire, exploitants, holding ; SIREN ; taille | GianLuca ; son expert-comptable | Calendrier de facturation électronique ; rôles RGPD |
| Q2 | Chaque entité a-t-elle choisi une plateforme de réception ? | Expert-comptable | Risque de sanction (2.1) |
| Q3 | Baux existants : dates, locataires, régime de TVA (option, immeuble), indice, clause | GianLuca ; notaire ; avocat | Règles applicables (3.1, 3.2) |
| Q4 | Surfaces tertiaires par site | GianLuca ; géomètre ou diagnostiqueur | Éco énergie tertiaire (3.6) |
| Q5 | Classement ERP de chaque bâtiment, procès-verbaux, registres existants | Exploitant ; mairie ; SDIS ; bureau de contrôle | Module 3 (4) |
| Q6 | L'hôtel reprend-il ? Combien de chambres ? Taxe de séjour à Cosne ou dans l'intercommunalité ? | GianLuca ; mairie | Module 2 (5) |
| Q7 | Contenu écrit de l'offre d'« Accord » | GianLuca | Comparaison (9) |
| Q8 | Garantie financière exigée d'un administrateur de biens ; portée exacte de la loi n° 70-9 pour un service mixte logiciel et gestion | Avocat | 3.7, 9.1 |
| Q9 | Régime de TVA des charges et de la taxe foncière refacturées ; locaux « aménagés » | Expert-comptable | 2.3 |
| Q10 | Rôles RGPD de l'administratrice et de Marwin ; durée d'archive des données locatives commerciales | Avocat ou DPD | 7 |
| Q11 | Bornes de la clause tunnel dans le texte de loi | Avocat (texte à relire sur Légifrance) | 3.1 |

---

## 11. Tableau de synthèse

« Exigence » : la règle et sa source. « Le logiciel doit » : ce qu'un logiciel, acheté ou sur mesure, doit faire [PR, R2]. « Reste à » : ce qui ne peut pas être confié au logiciel ni à Marwin.

| N° | Exigence | Le logiciel doit | Reste à un professionnel ou à un tiers | Module |
| --- | --- | --- | --- | --- |
| 1 | Recevoir les factures électroniques depuis le 1er sept. 2026 [FV] [S2, Q 1.2 ; S3] | Récupérer les factures reçues par la plateforme ; les rapprocher des devis et bons de commande | Choix et contrat de la plateforme : l'entité, avec l'expert-comptable ; annuaire : la plateforme | T |
| 2 | Émettre en électronique, PME au plus tard le 1er sept. 2027 ; quatre mentions [FV] [S3 ; S8] | Produire les données de facture complètes ; les transmettre à la plateforme ; suivre les statuts | Transmission aux clients et à l'administration : la plateforme agréée | T, 1 |
| 3 | E-reporting de transaction (particuliers) et de paiement [FV] [S2, Q 1.1, 1.3 ; R2F:295] | Préparer les données ; marquer les encaissements | Transmission : la plateforme ; option pour les débits : expert-comptable | T, 2 |
| 4 | Loyers exonérés hors champ ; option immeuble par immeuble [FV] [S2, Q 1.2 ; S6 ; S9] | Régime de TVA par immeuble et par bail ; bloquer toute facture électronique d'un loyer exonéré | Option et mention au bail : expert-comptable, avocat | 1 |
| 5 | Indexation ILC, ILAT, IRL ; révision triennale ; échelle mobile ; lissage ; tunnel [FV] [S11 ; S12 ; S13 ; S15] | Importer les indices Insee ; calculer par formule testée ; alerter aux dates ; bloquer l'IRL d'un logement F ou G | Clauses du bail, déplafonnement, contentieux : avocat | 1 |
| 6 | Paiement mensuel sur demande (loi n° 2026-403) [FV] [S13] | Échéancier mensuel ou trimestriel par bail ; contrôle des arriérés | Réponse à la demande : l'entité bailleresse | 1 |
| 7 | Inventaire limitatif des charges ; état récapitulatif au 30 sept. ; charges interdites [FV] [S10] | Ventiler selon l'inventaire ; produire l'état annuel ; refuser les catégories non refacturables | Rédaction de l'inventaire et litiges : avocat | 1 |
| 8 | Taxe foncière refacturée si identifiée au bail [FV] [S10] | Quote-part par lot selon la clé du bail ; avis joint | Clause : avocat ; montant : avis d'imposition | 1 |
| 9 | État triennal des travaux [FV] [S10] | Rappel ; modèle de l'état prévisionnel et du bilan | Contenu technique : maître d'œuvre ; envoi : l'entité | 1, 3 |
| 10 | Dépôt de garantie plafonné, restitution en 3 mois, transfert [FV] [S13 ; S14 ; S16] | Contrôler le plafond selon la date du bail ; échéance de restitution ; suivi des garanties | Mainlevées : banque, notaire ; litiges : avocat | 1 |
| 11 | Annexes et diagnostics du bail ; DPE affiché dans un ERP [FV] [S14 ; S19] | Coffre de documents par lot, avec dates de validité et alertes | Diagnostics : diagnostiqueur certifié ; annexes : notaire, avocat | 1, 3 |
| 12 | Éco énergie tertiaire au-delà de 1 000 m² ; OPERAT au 30 sept. [FV] [S18 ; S42] | Surfaces tertiaires par site ; collecte des consommations ; rappel | Déclaration : propriétaire et preneur ; programme d'actions : bureau d'études | 3 |
| 13 | Quittance d'habitation gratuite et détaillée [FV, repéré] [S17] ; relances [FV] (SYN-D:420) | Quittances et avis d'échéance ; relances préparées, envoyées au nom de l'entité après validation | Recouvrement forcé : commissaire de justice ; jamais Marwin | 1 |
| 14 | Gestion pour autrui réglementée [FV] [S41] | Aucun encaissement hors des comptes de l'entité | Gestion déléguée : administrateur de biens titulaire de la carte | 1 |
| 15 | Registre de sécurité (R143-44) [FV] [S20 ; S21] | Registre dématérialisé complet, dates des exercices comprises ; export pour la commission | Visite : commission ; responsabilité : exploitant | 3 |
| 16 | Vérifications périodiques ; visites de la commission [FV] [S20 ; S21] | Échéancier par installation ; procès-verbaux attachés ; alertes | Vérifications : organismes agréés ; avis : commission, maire | 3 |
| 17 | Registre public d'accessibilité [FV] [S22] | Générer le registre et la fiche ; publier ; rappel de l'attestation annuelle (cat. 1 à 4) | Attestations d'accessibilité : contrôleur technique ou architecte ; formation : employeur | 3 |
| 18 | Taxe de séjour [FV] [S23] | Calcul par nuitée selon la délibération ; ligne distincte ; état de reversement | Tarifs : commune ou intercommunalité ; logiciel hôtelier du marché | 2 |
| 19 | Fiche de police, 6 mois [FV] [S24] | Saisie à l'arrivée ; purge automatique à 6 mois ; transmission sur demande | Logiciel hôtelier du marché ; demande : police ou gendarmerie | 2 |
| 20 | Carte bancaire (PCI DSS, contrat bancaire) [FV, repéré] [S26] | Ne stocker ni saisir aucune donnée de carte ; lien ou terminal du prestataire | Prestataire de paiement ; banque | 2, 4, 5 |
| 21 | Caisse certifiée ou attestée ; sur mesure = certificat [FV] [S29 ; S30] | Aucune fonction d'encaissement de particuliers ; import des clôtures des caisses | Éditeur de caisse ; organisme accrédité | 4, 5 |
| 22 | FEC [FV, repéré] [S28] | Exports structurés vers le logiciel comptable | Comptabilité, FEC, liasse : expert-comptable | T |
| 23 | Conservation 10 ans, 6 ans, 5 ans [FV] [S27] | Archive horodatée à accès restreint ; purge des données personnelles au terme | Durées retenues : expert-comptable et DPD | T |
| 24 | RGPD : rôles, article 28, registre [FV] [S34 ; S35] | Registre préparé ; droits des personnes outillés ; minimisation | Rôles et contrats : avocat ou DPD ; décisions : responsable du traitement | T |
| 25 | Transferts hors de l'Union [FV] [S34 ; S36] | Hébergement dans l'Union ; pseudonymisation avant tout appel à une IA hors Union | Analyse d'impact des transferts : DPD ou avocat | T |
| 26 | Durées CNIL de la gestion locative [FV] [S32] | Purges paramétrées : candidats 3 mois ; locataires fin de bail plus 3 ou 5 ans | Validation : DPD | 1 |
| 27 | Violation de données : 72 h [FV] [S34] | Journal ; alerte ; fiche de violation | Décision et notification : responsable du traitement, avec le DPD ou l'avocat | T |
| 28 | IA : article 50 ; annexe III [FV] [S38 ; S39] | Mention « IA » ; aucune notation de personnes ; aucun envoi automatique vers l'extérieur | Qualification fournisseur ou déployeur : avocat | T |
| 29 | Sécurité (art. 32) [FV] [S34 ; S37] | Chiffrement, double authentification, rôles par entité, journal, sauvegardes testées | Audit de sécurité indépendant [PR] ; assureur cyber | T |
| 30 | Réversibilité et Data Act [FV] [S40] | Exports ouverts ; documentation ; restitution sous 15 jours ouvrés | Clauses du contrat : avocat | T |
| 31 | Propriété du code | Code sur un dépôt au nom de l'entité ; inventaire des composants et licences | Cession écrite et licences : avocat en propriété intellectuelle | T |

---

## 12. Sources

Toutes consultées le **9 novembre 2026**.

| N° | Source et adresse | Organisme | Date affichée | Lecture |
| --- | --- | --- | --- | --- |
| S1 | FAQ « J'approfondis la facturation électronique » — https://www.impots.gouv.fr/foire-aux-questions-japprofondis-la-facturation-electronique | DGFiP | Version du 01/09/2026 | Lue (Q 1.1, 1.3, 1.5, 1.8, 2.2 à 2.5) |
| S2 | FAQ « Je découvre la facturation électronique » — https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_je-decouvre-la-facturation-electronique.pdf | DGFiP | Version du 01/09/2026 | Lue (Q 1.1 à 1.3) |
| S3 | Fiche 3, « À partir de quelle date mon entreprise doit-elle être prête… » — https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/fiche-3_tpe_a-partir-de-quand-mon-entreprise-doit-etre-prete.pdf | DGFiP | Mise à jour octobre 2026 | Lue |
| S4 | Liste des plateformes agréées — https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees | DGFiP | Modifiée le 09/11/2026 | Lue |
| S5 | « Facturation électronique et plateformes agréées » — https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees | DGFiP | Non datée | Lue |
| S6 | BOI-TVA-DECLA-20-30-50-10 — https://bofip.impots.gouv.fr/doctrine/BOI-TVA-DECLA-20-30-50-10 | DGFiP, BOFiP | Publication du 30/09/2026 | Lue (§ 20) |
| S7 | BOI-RES-TVA-000275 — https://bofip.impots.gouv.fr/bofip/15143-PGP.html/identifiant=BOI-RES-TVA-000275-20260923 | DGFiP, BOFiP | 23/09/2026 | Lue |
| S8 | F31808, mentions obligatoires sur une facture — https://entreprendre.service-public.gouv.fr/vosdroits/F31808 | Service Public Entreprendre | Vérifié le 11 août 2026 | Lue |
| S9 | BOI-TVA-CHAMP-50-10, personnes effectuant des locations immobilières — https://bofip.impots.gouv.fr/bofip/730-PGP.html/identifiant=BOI-TVA-CHAMP-50-10-20140404 | DGFiP, BOFiP | En vigueur depuis le 04/04/2014 | Lue (§§ 10, 50, 70, 110) |
| S10 | F32336, bail commercial : charges et dépenses — https://entreprendre.service-public.gouv.fr/vosdroits/F32336 | Service Public Entreprendre | Vérifié le 29 mai 2026 | Lue |
| S11 | F31925, bail commercial : fixer et réviser le loyer — https://entreprendre.service-public.gouv.fr/vosdroits/F31925 | Service Public Entreprendre | Vérifié le 28 mai 2026 | Lue |
| S12 | F20564, quel indice de référence utiliser — https://entreprendre.service-public.gouv.fr/vosdroits/F20564 | Service Public Entreprendre | Vérifié le 30 janvier 2025 | Lue |
| S13 | Actualité A18929, loi de simplification de la vie économique : bail commercial — https://entreprendre.service-public.gouv.fr/actualites/A18929 | Service Public Entreprendre | Publiée le 29 mai 2026 | Lue |
| S14 | F23927, contrat de bail commercial — https://entreprendre.service-public.gouv.fr/vosdroits/F23927 | Service Public Entreprendre | Vérifié le 28 mai 2025 selon la page, qui cite pourtant la règle du 28 mai 2026 | Lue |
| S15 | F13723, révision du loyer d'un logement — https://www.service-public.gouv.fr/particuliers/vosdroits/F13723 | Service Public | Vérifié le 15 octobre 2026 | Lue |
| S16 | F31269, dépôt de garantie d'un bail d'habitation — https://www.service-public.gouv.fr/particuliers/vosdroits/F31269 | Service Public | Vérifié le 9 juin 2026 | Lue |
| S17 | Loi n° 89-462, art. 21 — https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000028806698/ | Légifrance | En vigueur depuis le 27 mars 2014 | Repérée |
| S18 | F38065, réduction de la consommation d'énergie des bâtiments tertiaires — https://entreprendre.service-public.gouv.fr/vosdroits/F38065 | Service Public Entreprendre | Vérifié le 9 septembre 2025 | Lue |
| S19 | F31689, DPE dans un ERP — https://entreprendre.service-public.gouv.fr/vosdroits/F31689 | Service Public Entreprendre | Vérifié le 29 janvier 2025 | Lue |
| S20 | F31684, règles de sécurité incendie d'un ERP — https://entreprendre.service-public.gouv.fr/vosdroits/F31684 | Service Public Entreprendre | Vérifié le 30 avril 2025 | Lue |
| S21 | CCH, art. R143-34 à R143-44 — https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074096/LEGISCTA000043819015/ | Légifrance | R143-44 en vigueur depuis le 1er juillet 2026 ; R143-34 depuis le 21 novembre 2025 | Lue |
| S22 | F32873, accessibilité d'un ERP — https://entreprendre.service-public.gouv.fr/vosdroits/F32873 | Service Public Entreprendre | Vérifié le 28 novembre 2025 | Lue |
| S23 | F743, taxe de séjour — https://entreprendre.service-public.gouv.fr/vosdroits/F743 | Service Public Entreprendre | Vérifié le 1er janvier 2026 | Lue |
| S24 | F33458, fiche individuelle de police — https://www.service-public.gouv.fr/particuliers/vosdroits/F33458 ; CESEDA, R814-1 à R814-3 — https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070158/LEGISCTA000042803266/ ; délibération CNIL n° 2016-176 — https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000032788981 | Service Public ; Légifrance | Vérifié le 22 janvier 2025 (F33458) | F33458 lue ; Légifrance repérée |
| S25 | Atout France, « Hôtel de tourisme » — https://www.atout-france.fr/fr/classement/hotel-de-tourisme | Atout France | Non relevée | Ouverte (titre) ; contenu repéré |
| S26 | PCI SSC, SAQ A v4.0 — https://listings.pcisecuritystandards.org/documents/PCI-DSS-v4-0-SAQ-A.pdf ; FAQ 1588 — https://www.pcisecuritystandards.org/faqs/1588/ | PCI Security Standards Council (organisme privé) | Non relevée | Repérée |
| S27 | F10029, délais de conservation des documents — https://entreprendre.service-public.gouv.fr/vosdroits/F10029 | Service Public Entreprendre | Vérifié le 1er juillet 2024 | Lue |
| S28 | BOI-CF-IOR-60-40-10 — https://bofip.impots.gouv.fr/bofip/9026-PGP.html/identifiant=BOI-CF-IOR-60-40-10-20211215 | DGFiP, BOFiP | 15/12/2021 | Repérée |
| S29 | ACTU-2026-00073, attestation de l'éditeur rétablie — https://bofip.impots.gouv.fr/bofip/15035-PGP.html/ACTU-2026-00073 | DGFiP, BOFiP | 25/03/2026 | Lue |
| S30 | BOI-TVA-DECLA-30-10-30 — https://bofip.impots.gouv.fr/bofip/10691-PGP.html/identifiant=BOI-TVA-DECLA-30-10-30-20260325 | DGFiP, BOFiP | 25/03/2026 | Lue (§§ 10, 30, 40, 45, 70, 300, 310, 315, 375) |
| S31 | CGI, art. 1770 duodecies — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000051203251 | Légifrance | Non relevée | Repérée |
| S32 | Référentiel CNIL « gestion locative » — https://www.cnil.fr/sites/default/files/atoms/files/referentiel_relatif_aux_traitements_de_donnees_personnelles_mis_en_oeuvre_dans_le_cadre_de_la_gestion_locative.pdf | CNIL | Adopté le 6 mai 2021 | Lue (§§ 1 à 4, 53 à 55) |
| S33 | Délibération CNIL n° 2026-031 du 29 janvier 2026, durées de conservation en ressources humaines — https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053749693 | Légifrance | JORF du 2 avril 2026 | Lue (titre et date) ; annexe non lue |
| S34 | RGPD, règlement (UE) 2016/679 — https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32016R0679 | EUR-Lex | — | Ouverte ; articles 28, 30, 32, 33 et 44 à 49 cités sans relecture intégrale |
| S35 | CNIL, « Sécurité : gérer la sous-traitance » — https://www.cnil.fr/fr/securite-gerer-la-sous-traitance ; guide du sous-traitant (2017) — https://www.cnil.fr/sites/cnil/files/atoms/files/rgpd-guide_sous-traitant-cnil.pdf | CNIL | Guide : septembre 2017 | Page ouverte ; guide repéré |
| S36 | CNIL, guide de l'analyse d'impact des transferts — https://www.cnil.fr/sites/cnil/files/2025-02/guide_aitd_pdf.pdf | CNIL | Février 2025 | Ouverte ; non relue en entier |
| S37 | CNIL, guide de la sécurité des données personnelles, édition 2024 — https://www.cnil.fr/sites/cnil/files/2024-03/cnil_guide_securite_personnelle_2024.pdf | CNIL | Mars 2024 | Ouverte ; non relue en entier |
| S38 | Règlement (UE) 2024/1689 sur l'IA, texte consolidé — https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:02024R1689-20260727 | EUR-Lex | Consolidé au 27.07.2026 | Lue (art. 50, 113 ; annexe III, points 4 et 5) |
| S39 | Règlement (UE) 2026/1744 du 8 juillet 2026 (omnibus numérique sur l'IA) — https://eur-lex.europa.eu/legal-content/FR/TXT/PDF/?uri=OJ%3AL_202601744 | EUR-Lex | JO L du 24.7.2026 | Lue (considérant sur les dates ; nouvel art. 4) |
| S40 | Règlement (UE) 2023/2854 sur les données (Data Act) — https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32023R2854 | EUR-Lex | — | Lue (art. 25, 29, 31) |
| S41 | Loi n° 70-9 du 2 janvier 1970, art. 1er — https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000028806892 | Légifrance | Version en vigueur au 9 nov. 2026 ; article en vigueur depuis le 27 mars 2014 | Lue |
| S42 | « Éco Énergie Tertiaire (EET) » — https://www.ecologie.gouv.fr/politiques-publiques/eco-energie-tertiaire-eet | Ministère de la Transition écologique | Mise à jour le 9 septembre 2025 | Lue |

---

## Limites

- **Avis professionnels** : aucun. Les points marqués [HY] (rôles RGPD, portée de la loi n° 70-9, régime de TVA des charges, locaux « aménagés », garantie financière d'un administrateur de biens) sont à soumettre à l'avocat, à l'expert-comptable ou au DPD.
- **Pages non lues ou mal datées** : la page d'economie.gouv.fr sur la facturation électronique a refusé l'accès (403) ; la fiche F23927 affiche une vérification de 2025 et une règle de 2026 ; les sources « repérées » (S17, S24 pour Légifrance, S25, S26, S28, S31) sont à relire avant tout usage hors de Marwin.
- **Texte de la loi n° 2026-403** : non relu sur Légifrance ; les bornes de la clause tunnel (± 3 % ou ± 5 %) viennent de la seule fiche F31925 [IN].
- **Faits sur GianLuca** : tous [DR] ou [IN] ; aucune entité, aucun bail, aucune surface, aucune activité d'hébergement n'est établie (section 1.1).
- **Fréquences des visites ERP** : le tableau de l'article GE 4 de l'arrêté du 25 juin 1980 n'a pas été relu ; la fréquence propre à chaque bâtiment est [IN].
- **Aucune action** : ni contact, ni dépense, ni modification d'un fichier existant, ni publication.

Relu et contrôlé : 9 novembre 2026 — chemins relatifs à la racine du dépôt ; prénom du client vérifié ; aucun engagement pris.

---

## Note de mise en cohérence (9 nov. 2026, soir)

Ajoutée à la fin pour ne pas déplacer les numéros de ligne cités ailleurs (`R2:…`). Le corps de ce travail n'est pas modifié.

- **Modules.** Les « six modules » et la « couche commune » de la section 1.2 reprennent R1. Les livrables du dossier suivent les **neuf modules** de la spécification (`pour-carlone/logiciels-et-automatisations/2026-11-09-annexe-specification-logiciel-gestion-proprietes.md`, section 3) : 1 Gestion immobilière → modules 1 et 2 ; 2 Hébergement → module 9 ; 3 Travaux et entretien → module 3 ; 4 Caisse et 5 Billetterie → module 4, par reprise des totaux ; 6 Pilotage multi-lieux → modules 5, 6 et 7 ; T Couche commune → droits, journal, sauvegardes et export de la spécification (sections 2 et 5), plus l'assistant (module 8).
- **Exigences techniques** (section 8) : reprises sans écart dans la spécification (section 5), la proposition (section 6) et la méthode (sections 4 à 7). Précision sur la sortie à blanc : une première a lieu à la fin du pilote, sur son bâtiment et son lieu, vers la mi-mai 2027 et non avant le 4 mai ; une autre avant la mise en service générale ; puis chaque année (étude, sections 3.9 et 8, avec l'encadré d'écart correspondant).
