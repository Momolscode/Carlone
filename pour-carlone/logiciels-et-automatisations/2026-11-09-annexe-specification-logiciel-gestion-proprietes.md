# Annexe : spécification du logiciel de gestion de vos propriétés

Marwin Tech · pour GianLuca Carlone · 9 novembre 2026 · PROJET non envoyé, à valider par Morgan Olsen et Mathys Couet · [Mention du 11 novembre 2026 : pièce historique du 9 novembre 2026 ; elle n’est ni montrée ni remise au rendez-vous du 13 novembre 2026, sauf décision écrite de Morgan Olsen et Mathys Couet. L’hébergement n’est plus une option à confirmer : il s’agit de neuf suites et d’un espace bien-être dans l’établissement de la galerie, pour lesquels nous conseillons un logiciel du marché (pièce du 10 novembre 2026 : 2026-11-10-vos-suites-un-logiciel-du-marche-bien-choisi.md). La proposition chiffrée à laquelle cette annexe renvoie n’est pas en vigueur : seul le cadrage a un prix à ce jour. Pièces à jour : la fiche 7 du 10 novembre 2026 et les écrans d’exemple (Maquette — données fictives).]

Ce document ne remplace pas l'avis d'un avocat, d'un expert-comptable ou de tout autre professionnel.

**À quoi sert cette annexe.** Elle décrit ce que doit faire un logiciel de gestion de vos propriétés, et comment vérifier qu'il le fait. Elle s'adresse à vous et à votre administratrice. Elle ne contient ni prix ni délai de réalisation : ils figurent dans notre proposition séparée, « Votre logiciel de gestion des propriétés ». Elle peut aussi servir de base commune pour comparer plusieurs offres, quel que soit le prestataire : mêmes modules, mêmes données, mêmes critères de réception. Elle n'engage pas à construire les neuf modules : la section 1.4 dit ce qui s'achète, et chaque étape ne se réalise que sur commande séparée (section 7).

**Ce qui reste à confirmer.** Nous ne connaissons pas encore la liste de vos bâtiments, les sociétés qui les possèdent et celles qui exploitent vos lieux, vos baux en cours, ni les outils déjà utilisés par votre administratrice. Nous ignorons aussi si une activité d'hébergement reprendra. Tout ce qui suit est donc une base de travail, à ajuster avec vous (section 8).

---

## 1. Objet et principes

### 1.1 Trois sens, un seul outil

L'expression « logiciel de gestion de propriété » peut désigner trois choses. L'outil décrit ici les couvre par modules. Vous choisissez lesquels, et dans quel ordre.

| Sens | Ce que cela recouvre | Modules concernés |
| --- | --- | --- |
| 1. Gestion de vos bâtiments | Lots, baux, loyers, charges, travaux, entretien, assurances, obligations du propriétaire | 1 Patrimoine ; 2 Baux et locataires ; 3 Travaux et entretien |
| 2. Logiciel hôtelier (en anglais « PMS », *property management system*) | Réservations, chambres, facturation des séjours, si l'ancien bar-restaurant-hôtel reprend une activité d'hébergement | 9 Hôtellerie, en option, relié à un logiciel hôtelier du marché |
| 3. Pilotage de plusieurs lieux | Galerie, cabaret-spectacle, commerces : un tableau par lieu et une vue d'ensemble de vos sociétés | 4 Exploitation des lieux ; 7 Tableau de bord |
| Commun aux trois | Classement des documents, échéances, budgets, aide à la rédaction | 5 Documents et échéances ; 6 Finances ; 8 Assistant IA |

### 1.2 Principes

1. **À votre nom.** Les comptes, l'hébergement, l'espace de code et les données sont ouverts au nom de vos sociétés dès le premier jour. Marwin Tech y intervient comme collaborateur, avec des droits limités (section 2). Les droits sur le code développé pour vous sont cédés à votre société au paiement complet (section 5.8).
2. **Vos données vous appartiennent.** Vous ou votre administratrice pouvez en obtenir un export complet à tout moment, sans nous le demander (section 4.3).
3. **En modules.** Chaque module a ses critères de réception. On met en service un module à la fois. Vous pouvez vous arrêter après chacun.
4. **Acheter avant de construire.** Quand un logiciel du marché fait le travail, on l'utilise, au nom de votre société et payé par elle : comptabilité, plateforme de facturation électronique, logiciel hôtelier, caisse, billetterie, et peut-être la gestion des baux. L'outil relie ces logiciels et ajoute ce qu'aucun d'eux ne fait : la fiche de chaque bâtiment et de chaque lieu, les échéances de toutes vos sociétés en un seul endroit, la vue d'ensemble. Une partie n'est développée que si un essai montre qu'aucun logiciel du marché ne la couvre correctement.
5. **Votre administratrice, utilisatrice principale.** L'outil est conçu pour son travail quotidien. Elle saisit, classe, prépare et valide dans la limite des pouvoirs que vous lui donnez par écrit. Vous décidez et vous signez.
6. **Une personne valide.** Aucun envoi, aucun paiement, aucune signature et aucune suppression ne se fait sans la validation d'une personne habilitée.
7. **Calculs par formule.** Loyers, indexations, charges, budgets et écarts sont calculés par des formules testées. L'intelligence artificielle (IA) ne calcule jamais un montant.
8. **Mesurer avant de promettre.** Le temps gagné est mesuré pendant le pilote, par rapport à une mesure de départ prise avant. Aucun gain n'est promis avant cette mesure.

### 1.3 Vue d'ensemble

```
        Vous · votre administratrice · responsables de lieux · expert-comptable (lecture)
                                        │
        ┌─────────────────────── Votre outil, à votre nom ───────────────────────┐
        │ 1 Patrimoine   2 Baux et locataires   3 Travaux et entretien           │
        │ 4 Exploitation des lieux   5 Documents et échéances   6 Finances       │
        │ 7 Tableau de bord multi-structures   8 Assistant IA                    │
        └────────────────────────────────────────────────────────────────────────┘
              │               │               │              │              │
        Plateforme       Logiciel        Caisse(s)      Billetterie    Logiciel
        agréée de        comptable de    certifiée(s)   du marché      hôtelier
        facturation      votre expert-   ou attestée(s)                du marché
        électronique     comptable                                     (option, module 9)
        (une par société)
                    Relevés bancaires : importés par fichier, sans identifiants bancaires dans l'outil
```

### 1.4 Ce qui s'achète, ce qui se construit

| Brique | Solution prévue | Pourquoi |
| --- | --- | --- |
| Émission et réception des factures électroniques | Plateforme agréée choisie par chaque société | Seule une plateforme agréée par l'État peut transmettre les factures électroniques à vos clients et à l'administration, et les recevoir pour vous. L'outil prépare les données et s'y connecte |
| Comptabilité, fichier des écritures comptables, comptes annuels | Logiciel de votre expert-comptable | L'outil n'est pas une comptabilité. Il prépare des pièces et des exports |
| Caisse des commerces, du bar et du restaurant | Logiciel de caisse du marché, certifié ou attesté | Toute fonction qui enregistre des paiements de particuliers doit être certifiée ou attestée. L'outil n'encaisse rien |
| Billetterie du cabaret | Billetterie du marché | Un système de billetterie informatisé se déclare à l'administration fiscale à sa mise en service et à chaque modification |
| Hébergement | Logiciel hôtelier du marché (module 9) | Les logiciels hôteliers du marché gèrent en général la taxe de séjour, les fiches de police, les sites de réservation et le paiement ; chaque point est vérifié avant le choix (module 9) |
| Baux et loyers | À décider au cadrage, puis à confirmer par l'essai sur vingt baux fictifs de l'étape 2 (section 7) : logiciel de gestion locative du marché, ou module 2 de l'outil | Plusieurs logiciels du marché existent. On retient celui qui passe les critères du module 2 ; sinon, on construit |
| Travaux et entretien | À décider au cadrage : logiciel de maintenance du marché, ou module 3 de l'outil | Même règle |
| Fiche des bâtiments et des lieux, échéances communes, budgets par structure, tableau d'ensemble, liens entre les briques | Partie propre à votre organisation | C'est ce qu'aucun logiciel du marché ne réunit pour plusieurs sociétés, bâtiments et lieux de nature différente |

### 1.5 Trois niveaux d'aide

Chaque automatisation décrite à la section 3 porte l'un de ces trois niveaux. Notre document « Automatisations : fiches détaillées » et notre présentation du 9 novembre emploient les mêmes.

| Niveau | Ce que fait l'outil | Ce que fait une personne |
| --- | --- | --- |
| **Automatique après essai** | Tâches sans effet hors de vos sociétés : rappels aux utilisateurs de l'outil, contrôles de dates et de montants, calculs par formule, mise à jour des tableaux | Active la tâche seulement après un essai réussi et votre validation écrite ; contrôle les résultats chaque semaine ; peut l'arrêter à tout moment |
| **Assistée** | Prépare : brouillon de courrier, quittance, rapprochement, classement, résumé | Vérifie, puis vous ou votre administratrice validez avant tout envoi ou toute écriture définitive |
| **Préparée pour signature** | Prépare un dossier qui engage : contrat, mise en demeure, autorisation, déclaration, commande | Vous, le signataire de la société ou votre professionnel relisez et signez |

**Jamais automatique, même après essai** : un envoi à une personne extérieure à vos sociétés, une publication, une commande, un paiement, une signature, une suppression, un changement de droits d'accès.

---

## 2. Utilisateurs, rôles et droits

### 2.1 Les rôles

| Rôle | Qui | Ce qu'il fait dans l'outil |
| --- | --- | --- |
| **Direction** | Vous, et le cas échéant le dirigeant de chaque société | Voit tout ; valide les budgets, les décisions et les envois qui engagent ; signe ; décide des droits |
| **Administratrice** (utilisatrice principale) | Votre administratrice | Saisit, classe, prépare, suit les échéances ; valide les envois et les dépenses dans la limite de ses pouvoirs écrits ; exporte |
| **Responsable de lieu** | Une personne par lieu (galerie, cabaret, chaque commerce, hôtel s'il y a lieu) | Voit son lieu seulement ; signale incidents et besoins d'intervention ; dépose les documents du lieu ; propose, ne valide pas |
| **Expert-comptable** (lecture) | Votre cabinet, pour les sociétés qu'il suit | Consulte les pièces et les budgets ; télécharge les exports convenus ; ne modifie rien |
| **Maintenance** | Marwin Tech, ou un autre prestataire, si vous lui confiez la maintenance par contrat écrit | Configure, met à jour, sauvegarde, restaure ; n'accède pas aux données de gestion sans demande écrite ; ne valide, ne transmet et ne paie rien |

### 2.2 Les droits

| Action | Direction | Administratrice | Responsable de lieu | Expert-comptable | Maintenance |
| --- | --- | --- | --- | --- | --- |
| Voir les données de toutes les sociétés | Oui | Celles de son périmètre écrit | Non | Celles qu'il suit, en lecture | Non, sauf demande écrite ponctuelle, limitée dans le temps |
| Voir les données d'un lieu | Oui | Oui | Son lieu | Pièces comptables seulement | Même règle |
| Saisir et modifier | Oui | Oui | Son lieu : incidents, demandes, documents | Non | Non |
| Valider un envoi à une personne extérieure | Oui | Oui, dans ses pouvoirs écrits | Non : il propose | Non | Jamais |
| Valider un budget, un devis, une dépense | Oui | Dans ses pouvoirs écrits | Non : il propose | Non | Jamais |
| Exporter | Tout | Tout son périmètre | Son lieu | Exports comptables convenus | Sauvegardes chiffrées seulement |
| Gérer les comptes et les droits | Oui | Par délégation écrite | Non | Non | Réglages techniques, sur demande écrite |
| Lire le journal des actions | Oui | Oui | Ses propres actions | Non | Oui, pour la partie technique |
| Arrêter un automatisme en cas d'incident | Oui | Oui | Non | Non | Oui, avec information écrite sous 24 heures |

### 2.3 Règles d'accès

- Chaque personne a son propre compte. Aucun compte partagé.
- Double authentification pour tous les comptes.
- Cloisonnement par société et par lieu : une personne ne voit que ce que son rôle autorise, y compris à travers l'assistant IA (module 8).
- Deux administrateurs au moins côté vos sociétés (par exemple vous et votre administratrice), pour ne dépendre de personne.
- Revue des accès chaque trimestre. Accès retirés dès le départ d'une personne.

---

## 3. Les modules

### 3.0 Comment lire les fiches

Chaque module est décrit avec : son objectif ; ses écrans principaux ; ses données ; ses automatisations, avec leur niveau ; ses liaisons avec d'autres logiciels ; ses critères de réception.

Les critères de réception se vérifient sur un **jeu d'essai** : des cas fictifs ou rendus anonymes, préparés avant le travail, avec le résultat attendu pour chacun. Pour les montants, le résultat attendu est validé par votre expert-comptable, ou par votre avocat pour les règles du bail. Le jeu d'essai est rejoué à chaque mise à jour et à chaque changement de règle ; son résultat est archivé.

Une **erreur critique** est : un montant faux envoyé à une personne extérieure ; un document envoyé à la mauvaise personne ; un accès à des données hors de son rôle ; une perte de données ; une action faite sans la validation prévue.

### 3.1 Module 1 — Patrimoine

**Objectif.** Une fiche unique et à jour pour chaque bâtiment et chaque lot : qui le possède, ce qu'il contient, son état, ses documents, ses échéances.

**Écrans principaux.**
- Liste des bâtiments, filtrée par société propriétaire, commune ou usage.
- Fiche bâtiment : identité, adresse, références cadastrales, société propriétaire, date d'acquisition, surfaces, usages, établissement recevant du public (ERP) ou non, lots, plans, diagnostics, assurances, échéances, travaux en cours.
- Fiche lot : surface, usage (commerce, bureau, logement, lieu exploité par l'une de vos sociétés, vacant), bail en cours, état des lieux.
- Plans : consultation des plans, avec leurs versions datées.
- Tableau des diagnostics et des assurances : type, date, fin de validité, prochaine action.

**Données.** Bâtiment ; lot ; surfaces, dont la surface d'activités tertiaires par site ; plans ; diagnostics (performance énergétique, amiante, état des risques, et les autres selon le lot) ; contrats d'assurance (assureur, garanties, échéance, attestations) ; régime de TVA du bâtiment (option ou non, date) ; contacts (notaire, syndic s'il y en a un, assureur).

**Automatisations.**

| Tâche | Niveau | Garde-fou |
| --- | --- | --- |
| Rappel avant la fin de validité d'un diagnostic ou d'une assurance | Automatique après essai | Rappel aux utilisateurs de l'outil seulement ; contrôle hebdomadaire |
| Calcul de la surface tertiaire cumulée par site ; signal si le seuil de l'obligation de réduction des consommations (1 000 m²) est atteint | Automatique après essai | Formule ; surfaces saisies par une personne à partir des pièces |
| Lecture d'un diagnostic ou d'une attestation d'assurance déposé : type, dates, références proposés | Assistée | Chaque champ est confirmé par une personne |
| Déclaration de sinistre, résiliation ou renouvellement d'un contrat d'assurance | Préparée pour signature | Signée par la société assurée |

**Liaisons.** Aucune obligatoire. Import de l'existant par tableur ; documents rangés dans le module 5.

**Critères de réception.**
1. Pour le bâtiment du pilote, chaque champ obligatoire de la fiche est rempli, ou marqué « inconnu » avec une personne chargée de le compléter.
2. 100 % des documents du bâtiment du pilote sont rattachés au bon bâtiment ou au bon lot, avec leur type et leur date.
3. Sur un jeu d'essai de diagnostics et d'assurances, chaque échéance qui entre dans la période d'alerte apparaît dans la liste des échéances : aucun oubli.
4. La somme des surfaces des lots d'un bâtiment est égale à la surface du bâtiment, ou l'écart est signalé.

### 3.2 Module 2 — Baux et locataires

**Objectif.** Suivre chaque bail de la signature à la sortie : loyers, indexation, charges, dépôt de garantie, quittances, relances. Appliquer à chaque bail la règle de sa date. L'outil prépare ; les loyers sont payés sur les comptes de la société bailleresse.

**Cas où la gestion est confiée à un tiers.** Si vous confiez la gestion de certains baux à un administrateur de biens, il utilise son propre logiciel. Le module reçoit alors ses comptes rendus par import, au lieu de les produire.

**Écrans principaux.**
- Liste des baux : par bâtiment, société bailleresse, locataire, statut, prochaine échéance.
- Fiche bail : parties ; lot ; date de signature, de prise d'effet, de fin ; type (commercial, professionnel, habitation, convention d'occupation entre vos sociétés) ; loyer et périodicité (mois ou trimestre) ; indice et trimestre de référence ; clause de révision ; dépôt de garantie et autres garanties ; régime de TVA ; inventaire des charges et clés de répartition ; taxe foncière refacturée ou non ; annexes.
- Échéancier : avis d'échéance, encaissements, quittances.
- Indexation : nouveau loyer proposé, avec le détail du calcul (indices, dates, formule).
- Encaissements : rapprochement des loyers reçus avec le relevé bancaire importé.
- Relances : brouillons, par étape.
- Charges : régularisation annuelle et état récapitulatif par locataire.
- Fiche locataire : coordonnées, numéro SIREN, assujetti ou non à la TVA, lieu d'établissement.
- Sortie : état des lieux, restitution du dépôt de garantie.

**Données.** Bail ; locataire ; garant ; loyers appelés et encaissés ; indices publiés par l'Insee (indice des loyers commerciaux, indice des loyers des activités tertiaires, indice de référence des loyers pour un logement, indice du coût de la construction pour les anciennes clauses d'échelle mobile) ; charges et leurs catégories ; taxe foncière et sa clé ; dépôt de garantie ; documents du bail.

**Règles que le module applique** (à confirmer avec votre avocat et votre expert-comptable) :
- L'indice dépend de l'activité du locataire : indice des loyers commerciaux pour une activité commerciale ou artisanale, indice des loyers des activités tertiaires pour les autres activités tertiaires. L'indice du coût de la construction ne sert plus aux révisions depuis septembre 2014, mais il peut subsister dans une clause d'échelle mobile d'un bail repris avec un bâtiment.
- Révision triennale, clause d'échelle mobile, lissage d'une hausse après déplafonnement : chacune a sa règle.
- Loi n° 2026-403 du 26 mai 2026, baux commerciaux signés ou renouvelés depuis le 28 mai 2026 : dépôt de garantie limité à un trimestre de loyer, garanties de toute nature comprises ; clause pouvant encadrer la variation annuelle de l'indice, dans les mêmes proportions à la hausse et à la baisse (bornes exactes à vérifier dans le texte de loi).
- Même loi, baux commerciaux en cours compris : paiement mensuel du loyer à la demande de certains locataires (commerce, services commerciaux ou artisanaux) sans arriéré ni montant contesté ; restitution du dépôt de garantie dans les trois mois qui suivent la remise des clés, pour les clés rendues après le 26 août 2026.
- Charges : seules les catégories de l'inventaire annexé au bail sont refacturées. Les grosses réparations et les honoraires liés à la gestion des loyers restent au bailleur d'un local commercial. La taxe foncière n'est refacturée que si le bail le prévoit clairement. L'état récapitulatif annuel est adressé au plus tard le 30 septembre de l'année qui suit.
- Tous les trois ans, le bailleur d'un local commercial communique l'état des travaux prévus et réalisés.
- Logement, s'il y en a : révision par l'indice de référence des loyers, interdite pour un logement classé F ou G ; quittance gratuite sur demande ; dépôt de garantie limité à un mois de loyer hors charges pour un logement vide (règle différente pour un meublé).
- TVA : un loyer de local nu sans option pour la TVA est exonéré ; il ne donne lieu ni à facture électronique ni à transmission de données à l'administration. Avec option, choisie immeuble par immeuble, le loyer facturé à une entreprise assujettie établie en France passe par la facturation électronique ; pour un locataire qui n'est pas assujetti, les données de la location sont transmises à l'administration par la plateforme agréée. Le tout selon le calendrier de la section 5.1.

**Automatisations.**

| Tâche | Niveau | Garde-fou |
| --- | --- | --- |
| Import des indices publiés par l'Insee | Automatique après essai | Une personne confirme chaque nouvel indice avant son usage |
| Calcul du loyer indexé, du dépôt maximal, des quotes-parts de charges et de taxe foncière | Automatique après essai | Formule testée sur le jeu d'essai ; jamais calculé par l'IA |
| Application du nouveau loyer au bail | Assistée | Validation par votre administratrice |
| Avis d'échéance et quittances | Assistée | Préparés par l'outil, envoyés sous le nom de la société après validation |
| Rapprochement des loyers reçus avec le relevé bancaire | Automatique après essai pour les correspondances exactes ; assistée pour les autres | Aucune écriture définitive sans validation des cas incertains |
| Contrôle du plafond du dépôt de garantie selon la date du bail | Automatique après essai | Alerte bloquante à la saisie |
| Refus d'une catégorie de charge non refacturable | Automatique après essai | Alerte bloquante ; levée seulement par une personne, avec motif écrit au journal |
| Première relance d'un loyer impayé | Assistée | Brouillon envoyé sous le nom de la société après validation |
| Mise en demeure | Préparée pour signature | Signée par la société ; la suite judiciaire relève d'un commissaire de justice |
| Demande de révision triennale, réponse à une demande de paiement mensuel | Préparée pour signature | Relue par votre avocat si besoin |
| État récapitulatif annuel des charges | Assistée | Validé avant envoi, au plus tard le 30 septembre |
| Données des factures de loyer soumises à TVA, transmises à la plateforme agréée de la société | Assistée | Une seule source par facture ; aucune facture électronique pour un loyer exonéré |

**Liaisons.** Plateforme agréée de facturation électronique de chaque société bailleresse ; relevés bancaires par fichier ; export vers le logiciel comptable ; signature électronique du marché, si vous la retenez (section 8).

**Critères de réception.**
1. Sur un jeu d'essai d'au moins vingt baux couvrant chaque cas (les deux indices du bail commercial, indice du coût de la construction dans une ancienne clause d'échelle mobile, révision triennale, échelle mobile, lissage après déplafonnement, clause d'encadrement, bail signé avant et après le 28 mai 2026, loyer avec et sans option pour la TVA, logement s'il y en a) : 100 % des loyers indexés, dépôts maximaux et quotes-parts sont égaux au résultat attendu, au centime près.
2. Aucun loyer exonéré ne produit de facture électronique ni de transmission de données sur le jeu d'essai.
3. Chaque catégorie de charge non refacturable saisie sur le jeu d'essai est refusée ou signalée : 100 %.
4. Pendant le pilote, 100 % des avis d'échéance, quittances et relances envoyés portent au journal le nom de la personne qui les a validés.
5. Le rapprochement du mois pilote laisse zéro loyer sans statut (encaissé, partiel, impayé, en litige).

### 3.3 Module 3 — Travaux et entretien

**Objectif.** Suivre les devis, les chantiers, l'entretien et les vérifications obligatoires de chaque bâtiment et de chaque lieu. Tenir le registre de sécurité de chaque établissement recevant du public.

**Écrans principaux.**
- Demandes d'intervention : lieu, description, photo, urgence, personne chargée.
- Comparaison des devis : grille commune, postes manquants et écarts signalés.
- Chantier : planning, photos datées, comptes rendus de visite, réserves et levée des réserves, factures liées.
- Plan d'entretien par équipement : périodicité, prestataire, contrat.
- Calendrier des vérifications obligatoires : installation, organisme, date, procès-verbal, observations, suite donnée.
- Registre de sécurité par établissement, avec toutes ses rubriques : travaux d'aménagement, personnel chargé de la sécurité, consignes, contrôles et vérifications, dates des exercices d'incendie (à porter au registre depuis le 1er juillet 2026).
- Registre public d'accessibilité et sa fiche de synthèse.
- État des travaux sur trois ans, pour les baux commerciaux (avec le module 2).
- Consommations d'énergie par site, pour la déclaration annuelle sur la plateforme OPERAT si l'obligation s'applique.

**Données.** Demande ; devis ; commande ; chantier ; intervenant ; équipement ; contrat d'entretien ; vérification ; procès-verbal ; entrée du registre de sécurité ; relevé de consommation.

**Automatisations.**

| Tâche | Niveau | Garde-fou |
| --- | --- | --- |
| Rappel avant chaque vérification obligatoire et chaque entretien planifié | Automatique après essai | Rappel aux utilisateurs de l'outil seulement ; contrôle hebdomadaire |
| Grille de comparaison des devis : postes lus, écarts et oublis signalés | Assistée | Vérifiée par une personne ; le choix revient à vous ou à votre administratrice |
| Compte rendu de visite de chantier à partir de notes ou d'un enregistrement | Assistée | Enregistrement seulement avec le consentement des participants ; relu avant diffusion |
| Acceptation d'un devis, bon de commande | Préparée pour signature | Dans les budgets validés (module 6) |
| Export du registre de sécurité pour la commission de sécurité | Assistée | Relu par l'exploitant |
| Dossier d'autorisation de travaux ou de permis | Préparée pour signature | Avec votre architecte ou votre bureau de contrôle |
| Signal d'une consommation anormale | Automatique après essai | Seulement si des relevés sont importés ou si des compteurs sont achetés par votre société |
| Rappel de la déclaration annuelle des consommations avant le 30 septembre | Automatique après essai | La déclaration elle-même est préparée pour signature |

**Règle.** L'outil ne dit jamais qu'un lieu est « conforme ». Seuls la commission de sécurité, le maire et les organismes agréés le disent. L'outil dit ce qui est fait, ce qui manque et ce qui arrive.

**Liaisons.** Plateforme agréée de chaque société, pour recevoir les factures des entreprises et les rapprocher des devis et des commandes ; export d'agenda ; relevés des fournisseurs d'énergie ou compteurs, en option.

**Critères de réception.**
1. Le registre de sécurité du lieu pilote contient les cinq rubriques de l'article R143-44 du code de la construction et de l'habitation, dates des exercices d'incendie comprises ; il s'exporte en un document daté et lisible.
2. Sur un jeu d'essai de vérifications et d'entretiens, chaque échéance qui entre dans la période d'alerte déclenche un rappel : aucun oubli.
3. Pendant le pilote, chaque facture d'entreprise reçue est reliée à un devis ou à une commande, ou marquée « sans devis » avec un motif : 100 %.
4. Sur trois devis comparés pendant le pilote, chaque poste chiffré se retrouve dans la grille, contrôle fait par votre administratrice.
5. Aucun texte produit par l'outil ne qualifie un lieu de « conforme » (contrôle sur tous les modèles de documents).

### 3.4 Module 4 — Exploitation des lieux

**Objectif.** Un tableau par lieu (galerie, cabaret-spectacle, chaque commerce, hôtel s'il y a lieu) qui réunit ce qui fait vivre le lieu : exploitant, autorisations, chiffres clés, incidents, échéances. Le module ne remplace pas les logiciels d'exploitation (caisse, billetterie, réservations) : il en reprend les totaux.

**Écrans principaux.**
- Fiche lieu : société exploitante, bâtiment et lots occupés, type et catégorie d'établissement recevant du public, effectif admis, horaires, autorisations et leur échéance (déclaration d'entrepreneur de spectacles vivants, licence de débit de boissons, permis d'exploitation, autorisations des organismes de droits musicaux), assurances du lieu.
- Tableau du lieu : ventes du mois reprises des clôtures de caisse et de billetterie, fréquentation, budget et réel, échéances, incidents, travaux en cours.
- Journal du lieu : incidents, faits marquants, visites.
- Calendrier des événements : vernissages, spectacles, avec leurs démarches propres.

**Données.** Lieu ; société exploitante ; autorisation ; événement ; incident ; totaux de ventes par jour ou par mois ; fréquentation. **Aucune donnée nominative de client** n'est reprise des caisses, de la billetterie ou du logiciel hôtelier : seulement des totaux.

**Automatisations.**

| Tâche | Niveau | Garde-fou |
| --- | --- | --- |
| Reprise des totaux de caisse et de billetterie | Automatique après essai | Contrôle hebdomadaire des totaux contre les rapports des logiciels d'origine |
| Rappel avant l'échéance d'une autorisation | Automatique après essai | Rappel au responsable du lieu et à votre administratrice |
| Note mensuelle du lieu (brouillon) | Assistée | Chiffres issus des formules ; texte relu avant diffusion |
| Dossier de déclaration ou d'autorisation (spectacles, débit de boissons, événement exceptionnel) | Préparée pour signature | Signé par la société exploitante ; les autorisations restent à son nom |

**Liaisons.** Caisse du marché certifiée ou attestée (export des clôtures) ; billetterie du marché (export des ventes) ; logiciel hôtelier (module 9) ; outil de réservation ou de planning déjà retenu par l'exploitant, s'il en existe un.

**Critères de réception.**
1. Pour le lieu pilote, le total mensuel repris dans l'outil est égal au total des clôtures du logiciel de caisse, au centime près.
2. Chaque autorisation du lieu pilote a une date de fin et un responsable ; le rappel est vérifié sur un jeu d'essai.
3. Le contrôle des imports ne trouve aucune donnée nominative de client.
4. Le responsable du lieu pilote ne voit aucune donnée d'un autre lieu ni d'une autre société (test de droits).

### 3.5 Module 5 — Documents et échéances

**Objectif.** Un seul classement des documents de toutes vos sociétés et un seul calendrier d'échéances, avec une personne chargée de chaque échéance. Un registre des décisions qui garde la trace de qui a décidé quoi, quand, sur quelles pièces.

**Écrans principaux.**
- Coffre de documents : classement par société, puis par bâtiment ou lieu, puis par type ; versions ; recherche dans le texte.
- Fiche document : type, date, fin de validité, version, liens avec les bâtiments, lots, baux, lieux, contrats.
- Calendrier des échéances : vue par liste, par mois, par société, par personne chargée.
- Registre des décisions : décision, date, auteur, documents liés, suites à donner.

**Données.** Document ; échéance (contrats, assurances, abonnements, fins et révisions de baux, diagnostics, vérifications, autorisations, déclarations annuelles, dates de fin de conservation) ; décision ; personne chargée.

**Automatisations.**

| Tâche | Niveau | Garde-fou |
| --- | --- | --- |
| Classement proposé d'un document déposé : type, société, bâtiment ou lieu, dates | Assistée | Confirmé par une personne |
| Rappels avant chaque échéance (par défaut deux mois, un mois et une semaine avant, réglables) | Automatique après essai | Aux utilisateurs de l'outil seulement ; jamais à une personne extérieure |
| Résumé hebdomadaire des échéances proches et des décisions en attente | Automatique après essai | Destiné à vous et à votre administratrice |
| Archivage ou suppression à la fin de la durée de conservation | Assistée | Liste proposée, validée par une personne ; aucune suppression en masse automatique |
| Courrier de résiliation ou de renouvellement d'un contrat | Préparée pour signature | Signé par la société |

**Liaisons.** Messagerie, pour les rappels aux utilisateurs ; export d'agenda ; espace de stockage au nom de votre société ; signature électronique du marché, si vous la retenez.

**Critères de réception.**
1. Sur un jeu d'essai d'au moins trente échéances de tous types, 100 % des rappels partent à la date réglée et à la bonne personne ; aucun ne part vers l'extérieur.
2. Une échéance sans personne chargée est signalée dans le résumé hebdomadaire : 100 % sur le jeu d'essai.
3. Sur vingt recherches de test préparées avec votre administratrice, le bon document figure dans les cinq premiers résultats pour au moins dix-huit d'entre elles.
4. Aucune suppression ne se fait sans validation ; chaque suppression figure au journal.

### 3.6 Module 6 — Finances

**Objectif.** Suivre les budgets par bâtiment, par lieu et par société ; comparer le prévu, l'engagé et le réel ; préparer chaque mois les pièces pour votre expert-comptable. Ce module n'est pas une comptabilité.

**Écrans principaux.**
- Budgets : par société, bâtiment, lieu et chantier, avec leur version validée.
- Engagements : devis acceptés, commandes, contrats en cours.
- Réel : factures reçues, loyers encaissés, ventes reprises des caisses.
- Écarts : prévu, engagé, payé, par ligne.
- Trésorerie prévisionnelle par société.
- Pièces du mois : liste pour l'expert-comptable, avec un statut (reçue, rapprochée, validée, transmise).
- Opérations entre vos sociétés : loyers et frais partagés, selon les conventions validées par votre expert-comptable.

**Données.** Plan de codes par société, bâtiment et lieu, fixé avec votre expert-comptable ; budget ; engagement ; facture ; relevé bancaire importé ; totaux de ventes ; pièce justificative.

**Automatisations.**

| Tâche | Niveau | Garde-fou |
| --- | --- | --- |
| Calcul des écarts entre budget et réel | Automatique après essai | Formule ; chaque chiffre mène à ses pièces |
| Alerte de dépassement de budget | Automatique après essai | Seuils fixés par vous |
| Rapprochement d'une facture avec son devis ou sa commande | Assistée | Confirmé par une personne |
| Dossier mensuel des pièces pour l'expert-comptable | Assistée | Transmis après validation de votre administratrice |
| Prévision de trésorerie | Assistée | Hypothèses écrites et validées |
| Liste des paiements à faire | Préparée pour signature | Le paiement se fait dans votre banque, par une personne habilitée ; jamais depuis l'outil |

**Liaisons.** Logiciel comptable de votre expert-comptable, par un export au format qu'il choisit ; plateforme agréée de chaque société (factures reçues) ; relevés bancaires par fichier, sans identifiants bancaires dans l'outil ; totaux de caisse, de billetterie et du logiciel hôtelier.

**Critères de réception.**
1. Pour le mois pilote, le réel de chaque bâtiment et de chaque lieu est égal à la somme des pièces rattachées, au centime près.
2. 100 % des pièces du mois pilote ont un statut ; votre expert-comptable confirme par écrit que l'export lui convient.
3. Aucun paiement ne peut être lancé depuis l'outil (test).
4. Un responsable de lieu ne voit ni la trésorerie ni les budgets des autres lieux et sociétés (test de droits).

### 3.7 Module 7 — Tableau de bord multi-structures

**Objectif.** Une vue pour vous et une pour votre administratrice : où en est chaque société, chaque bâtiment, chaque lieu ; ce qui attend une décision.

**Écrans principaux.**
- Vue d'ensemble, par société : budget et réel, trésorerie prévue, loyers attendus et encaissés, échéances proches, décisions en attente, incidents ouverts.
- Vue par bâtiment et vue par lieu.
- Liste « à décider » : décisions et validations attendues, avec leur date limite.
- Synthèse mensuelle exportable.

**Données.** Reprises des autres modules ; pas de saisie propre, sauf des commentaires.

**Automatisations.**

| Tâche | Niveau | Garde-fou |
| --- | --- | --- |
| Mise à jour des indicateurs à partir des modules | Automatique après essai | Formules ; chaque chiffre mène à sa source |
| Alertes : budget dépassé, loyer impayé au-delà du délai que vous fixez, échéance réglementaire proche sans personne chargée | Automatique après essai | Aux utilisateurs de l'outil seulement |
| Note mensuelle de synthèse | Assistée | Texte relu ; chiffres repris des formules, jamais rédigés par l'IA |

**Liaisons.** Aucune vers l'extérieur.

**Critères de réception.**
1. Les indicateurs sont choisis et validés par écrit par vous avant d'être construits : douze au plus par vue.
2. Sur un échantillon de dix chiffres du pilote, 100 % se retrouvent à la main à partir des pièces liées.
3. Chaque rôle ne voit que son périmètre (test de droits).

### 3.8 Module 8 — Assistant IA

**Objectif.** Répondre à des questions sur vos documents, avec la source citée ; préparer des comptes rendus et des brouillons. L'assistant lit et propose. Il n'agit pas.

**Écrans principaux.**
- Question, avec le périmètre choisi (société, bâtiment, lieu) ; réponse avec les passages cités et un lien vers chaque document.
- Atelier de brouillons : courrier, relance, compte rendu, note.
- Historique des questions de chaque utilisateur, visible par lui seul.

**Règles.**
- L'assistant ne voit que ce que l'utilisateur a le droit de voir.
- Chaque réponse cite ses sources. Sans source, il répond qu'il ne sait pas.
- Les montants et les dates viennent des modules, calculés par formule ; l'assistant ne les calcule pas.
- Une instruction trouvée dans un document est traitée comme du texte : elle est signalée, jamais exécutée.
- Il ne fait aucun envoi, aucune modification, aucun paiement, aucune suppression.
- Fournisseur d'IA : offre professionnelle, données non utilisées pour l'entraînement, contrat de sous-traitance des données. Si le fournisseur traite les données hors de l'Union européenne, seules des données pseudonymisées lui sont transmises (noms, coordonnées et numéros remplacés par des codes), et le transfert est encadré par écrit avant tout usage (clauses types de la Commission européenne, analyse des transferts, avec votre conseil). Un document qui ne peut pas être traité ainsi ne passe que par un fournisseur qui traite les données dans l'Union. Un second fournisseur est configuré en secours.
- Un plafond de dépense mensuel est fixé ; alertes à 50 %, 80 % et 100 % ; arrêt automatique à 100 %.
- Comptes rendus de réunion : seulement avec le consentement des participants.
- Exclus : toute notation ou tout tri de candidats locataires, de candidats à un emploi ou de salariés ; tout suivi du travail de votre administratrice ou de vos équipes.
- Un assistant qui répondrait à des locataires, à des clients ou au public n'est pas prévu ici. S'il l'était, il devrait dire qu'il est une IA, comme l'exige le règlement européen sur l'IA depuis le 2 août 2026.

**Automatisations.**

| Tâche | Niveau | Garde-fou |
| --- | --- | --- |
| Réponse à une question sur les documents | Assistée | L'utilisateur vérifie la source citée |
| Brouillon de courrier ou de compte rendu | Assistée, ou préparée pour signature si le document engage | Relu avant tout usage |
| Résumé hebdomadaire des nouveaux documents | Automatique après essai | Destiné à votre administratrice |

**Liaisons.** Fournisseur d'IA, par une offre professionnelle ; index des documents du module 5.

**Critères de réception.**
1. Sur trente questions de test préparées avec votre administratrice, avec leur réponse attendue : au moins vingt-sept réponses justes avec la bonne source ; aucune réponse chiffrée sans source.
2. Cinq documents de test contenant des instructions cachées : 100 % signalés, aucune instruction exécutée.
3. Un utilisateur limité à un lieu ne reçoit aucune information tirée d'un autre lieu : zéro sur dix essais.
4. Le dépassement volontaire du plafond de dépense, en essai, provoque l'arrêt.
5. Cinq questions de test dont la réponse ne figure dans aucun document : l'assistant répond qu'il ne sait pas dans les cinq cas.

### 3.9 Module 9 — Hôtellerie (en option)

**Condition.** Seulement si une activité d'hébergement reprend et si une société exploitante est nommée.

**Principe.** Un logiciel hôtelier du marché, au nom de la société exploitante, gère les réservations, le planning des chambres, les tarifs, les sites de réservation, la facturation des séjours, la taxe de séjour, les fiches de police et le paiement. L'outil n'en refait aucune partie. Il reprend des totaux dans le tableau du lieu (module 4).

**Critères pour choisir le logiciel hôtelier** (à vérifier sur pièces, avant signature) :
- export complet des données, dans un format ouvert ;
- hébergement des données dans l'Union européenne, ou garanties écrites équivalentes ;
- fiche individuelle de police pour chaque client étranger, conservée six mois puis détruite ;
- taxe de séjour calculée selon la délibération de votre commune ou intercommunalité, sur une ligne distincte de la facture lorsqu'elle est perçue au réel ;
- liaison avec la plateforme agréée de la société exploitante, pour la facturation électronique et la transmission des données de vente ;
- paiement par un prestataire de paiement, sans aucune donnée de carte bancaire saisie ou stockée par la société ;
- caisse du bar et du restaurant certifiée ou attestée, si elle y est intégrée ;
- export ou liaison des totaux journaliers ;
- engagement, préavis et conditions de sortie écrits.

**Écrans dans l'outil.** Tableau de l'hôtel dans le module 4 : nuitées, taux d'occupation, chiffre d'affaires, taxe de séjour collectée et à reverser, incidents, échéances.

**Automatisations.**

| Tâche | Niveau | Garde-fou |
| --- | --- | --- |
| Reprise des totaux du logiciel hôtelier | Automatique après essai | Contrôle hebdomadaire |
| Rappel avant le reversement de la taxe de séjour | Automatique après essai | Aux utilisateurs de l'outil seulement |
| Reversement de la taxe de séjour | Préparée pour signature | Payé par la société exploitante |

**Critères de réception.**
1. Les totaux repris sont égaux aux rapports du logiciel hôtelier, au centime près, sur le mois pilote.
2. Aucune donnée nominative de voyageur, aucune fiche de police et aucune donnée de carte ne se trouve dans l'outil (contrôle des imports).
3. L'export complet du logiciel hôtelier a été testé avant la signature de son contrat.

---

## 4. Données

### 4.1 Modèle simplifié

| Objet | Ce qu'il décrit | Principaux liens |
| --- | --- | --- |
| Société | Chacune de vos structures : propriétaire, exploitante, holding | Possède des bâtiments ; exploite des lieux ; signe des baux et des contrats |
| Bâtiment | Un immeuble, à une adresse | Appartient à une société ; contient des lots ; porte des diagnostics, des assurances, des équipements |
| Lot | Une partie louable ou exploitée d'un bâtiment | Fait l'objet d'un bail ; peut être occupé par un lieu |
| Lieu | Une activité ouverte au public : galerie, cabaret, commerce, hôtel | Exploité par une société ; occupe un ou plusieurs lots ; a des autorisations |
| Personne | Locataire, garant, intervenant, assureur, professionnel, utilisateur | Liée à des baux, des contrats, des chantiers, des rôles |
| Bail | Le contrat de location d'un lot | Relie une société bailleresse, un locataire et un lot ; porte loyers, indice, charges, dépôt |
| Appel de loyer | Une échéance de loyer et de charges | Appartient à un bail ; donne une quittance ; se rapproche d'un encaissement |
| Contrat | Assurance, entretien, abonnement, prestation | Lié à une société et à un bâtiment ou un lieu ; a des échéances |
| Chantier et devis | Travaux, de la demande à la réception | Lié à un bâtiment ou un lieu, à des entreprises, à un budget |
| Équipement et vérification | Installation technique et ses contrôles | Lié à un bâtiment ou un lieu ; alimente le registre de sécurité |
| Autorisation | Déclaration, licence, permis | Liée à un lieu et à sa société exploitante |
| Document | Toute pièce déposée | Rattachée à un ou plusieurs objets ci-dessus |
| Échéance | Une date à tenir | Liée à un objet et à une personne chargée |
| Budget, engagement, pièce | Prévu, engagé, réel | Liés à une société, et à un bâtiment, un lieu ou un chantier |
| Décision | Ce qui a été décidé, par qui, quand | Liée à des documents et à des suites |
| Action | Une ligne du journal | Liée à une personne, un objet et une heure |

```
Société ──possède──> Bâtiment ──contient──> Lot <──occupe── Lieu <──exploite── Société
                         │                   │                │
                   diagnostics,           Bail ──> Appels de loyer ──> Encaissements
                   assurances,             │
                   équipements        Locataire (personne ou société)

Document et Échéance se rattachent à tout objet. Budget, engagement et pièce se rattachent à une société,
puis à un bâtiment, un lieu ou un chantier. Chaque action est inscrite au journal.
```

### 4.2 Import de l'existant

1. **Inventaire des sources** : tableurs, baux, actes, diagnostics, contrats, devis, factures, procès-verbaux, avec votre administratrice.
2. **Modèle de tableur** fourni pour chaque objet (sociétés, bâtiments, lots, baux, contrats, échéances).
3. **Import avec rapport** : chaque ligne est importée, ou refusée avec son motif. Aucun doublon.
4. **Documents** rattachés à leur objet. L'outil peut proposer les dates et références lues dans un document ; une personne confirme chaque champ (niveau assisté).
5. **Contrôle par échantillon** : votre administratrice vérifie au moins dix fiches tirées au hasard par type d'objet.
6. **Validation écrite** de l'import par vous ou par votre administratrice.

Aucune donnée réelle n'est importée avant les préalables de la section 5.2.

### 4.3 Export complet, à tout moment

- Vous ou votre administratrice lancez l'export vous-mêmes, sans nous le demander.
- Contenu : toutes les données en formats ouverts (CSV et JSON), avec la description de chaque champ ; tous les documents d'origine ; le journal des actions ; les réglages des automatisations et les modèles de documents.
- L'export est testé à chaque étape (section 7) : il est relu, puis rechargé dans un espace vide pour vérifier que rien ne manque.

---

## 5. Conformité, sécurité et réversibilité

### 5.1 Obligations prises en compte

Ce tableau résume les obligations que le logiciel doit aider à tenir. Il ne tranche aucune question juridique ou fiscale : chaque ligne est à confirmer avec votre expert-comptable, votre avocat ou le professionnel indiqué.

| Obligation | Ce que fait le logiciel | Ce qui reste à vous ou à un professionnel |
| --- | --- | --- |
| Recevoir les factures électroniques par une plateforme agréée, obligatoire pour toute société assujettie à la TVA depuis le 1er septembre 2026, même si ses loyers sont exonérés | Récupère les factures reçues ; les rapproche des devis et des commandes | Choix et contrat de la plateforme par chaque société, avec l'expert-comptable |
| Émettre des factures électroniques, et transmettre à l'administration certaines données de vente et de paiement, notamment pour les ventes à des particuliers : au plus tard le 1er septembre 2027 pour une petite ou moyenne entreprise ou une microentreprise | Prépare les données de facture et de vente ; les transmet à la plateforme ; suit leur statut | Transmission par la plateforme agréée |
| TVA des loyers : régime choisi immeuble par immeuble | Porte le régime par bâtiment et par bail ; bloque toute facture électronique d'un loyer exonéré | Choix de l'option, mention au bail : expert-comptable, avocat |
| Règles du bail commercial : indices, révision, charges, dépôt de garantie, état des travaux, annexes | Calcule par formule ; rappelle les dates ; refuse ce qui est interdit | Rédaction des baux, litiges : avocat |
| Gestion de biens pour le compte d'autrui : activité réglementée (loi n° 70-9 du 2 janvier 1970) | N'encaisse rien ; les loyers arrivent sur les comptes de la société bailleresse | Si vous confiez la gestion ou l'encaissement à un tiers, vérifier avec votre avocat qu'il détient la carte professionnelle exigée |
| Réduction des consommations des bâtiments tertiaires, à partir de 1 000 m² d'activités tertiaires sur un même site | Calcule les surfaces ; rassemble les consommations ; rappelle la déclaration du 30 septembre | Déclaration par le propriétaire et par l'occupant, chacun pour sa part ; programme d'actions : bureau d'études |
| Établissements recevant du public : registre de sécurité, vérifications, visites de la commission, registre d'accessibilité | Registre dématérialisé ; calendrier ; procès-verbaux ; exports | Vérifications : organismes agréés ; avis : commission et maire ; responsabilité : exploitant |
| Caisse : logiciel certifié ou attesté pour tout encaissement de particuliers | Aucune fonction d'encaissement ; reprend les clôtures | Choix d'une caisse certifiée ou attestée |
| Billetterie : système déclaré à l'administration fiscale | Aucune émission de billet ; reprend les ventes | Choix et déclaration de la billetterie par l'exploitant |
| Hébergement : taxe de séjour, fiches de police | Rien de nominatif ; reprend les totaux | Logiciel hôtelier du marché ; règles de la commune |
| Fichier des écritures comptables | Exports vers le logiciel comptable | Comptabilité : expert-comptable |
| Conservation : dix ans pour les livres et pièces comptables, six ans pour les documents fiscaux, cinq ans pour les contrats commerciaux, trente ans pour les actes d'acquisition d'immeubles | Archive datée, à accès restreint ; dates de fin de conservation | Durées retenues : expert-comptable et conseil en données |
| Données personnelles (règlement général sur la protection des données) | Voir 5.2 | Rôles et contrats : avocat ou délégué à la protection des données |
| Règlement européen sur l'IA | Voir le module 8 | Qualification exacte des rôles : avocat |

**Suivi des règles.** Les règles changent : la loi du 26 mai 2026 a modifié plusieurs règles du bail commercial. Pour un module construit, une personne nommée au contrat de maintenance suit les textes de ce tableau, met à jour les formules et fait rejouer le jeu d'essai avant d'appliquer une nouvelle règle. C'est un travail régulier, à prévoir dans la maintenance. Pour un logiciel du marché, l'éditeur fait cette mise à jour ; on le vérifie en rejouant le même jeu d'essai.

### 5.2 Données personnelles et IA

- Chaque société est responsable des données qu'elle traite : locataires, garants, clients, salariés, intervenants. Les rôles exacts sont fixés par écrit avec votre conseil avant toute donnée réelle.
- Tout prestataire qui héberge ou traite ces données signe un contrat de sous-traitance (article 28 du règlement général sur la protection des données). La liste de ses propres sous-traitants y figure.
- Avant toute donnée réelle : responsable désigné par écrit ; contrat de sous-traitance signé ; registre des traitements à jour ; information des personnes concernées.
- Durées de conservation paramétrées et purges proposées à la validation (module 5). Repère pour les baux : le référentiel de la CNIL sur la gestion locative des logements, à adapter avec votre conseil pour les baux commerciaux.
- En cas de violation de données : alerte, fiche d'incident, et décision de la société responsable sur la notification à la CNIL, qui doit intervenir dans les 72 heures si elle est due.
- Aucune IA pour juger la solvabilité de candidats locataires, ni pour trier des candidats à un emploi ou noter des salariés.

### 5.3 Sécurité

- Chiffrement des données pendant leur transfert et sur les serveurs.
- Mots de passe, clés et jetons d'accès dans un coffre ; jamais dans le code, un document ou le journal ; révocation testée.
- Double authentification ; droits par rôle, par société et par lieu ; lecture seule par défaut pour les comptes techniques.
- Aucune mise à jour en masse sans un échantillon validé ; modifications par lots, avec annulation possible.
- Mises à jour de sécurité suivies ; liste des composants utilisés et de leurs versions tenue à jour.
- Bouton d'arrêt de toutes les automatisations, que vous, votre administratrice ou la maintenance pouvez déclencher sans autorisation préalable ; testé chaque trimestre.
- Fiche de secours manuel pour chaque tâche outillée : comment la faire sans l'outil ; testée une fois avant la mise en service.

### 5.4 Hébergement

- Dans l'Union européenne, chez un hébergeur nommé au contrat, sur un compte au nom de votre société.
- Sous-traitants listés et connus de vous.
- Si un prestataire héberge et exploite l'outil pour vous, le contrat contient les clauses de changement de fournisseur prévues par le règlement européen sur les données (article 25).

### 5.5 Sauvegardes et reprise

| Exigence | Valeur |
| --- | --- |
| Fréquence | Export quotidien des données ; sauvegarde complète chaque semaine |
| Copies | Trois copies, sur deux supports, dont une hors de l'hébergeur principal ; copies chiffrées ; sur des espaces au nom de votre société |
| Perte maximale | 24 heures de données |
| Remise en service | Au plus tard le jour ouvré suivant l'incident |
| Test de restauration | Chaque mois pendant les trois premiers mois, puis chaque trimestre, dans un espace neuf, sans rejouer aucun envoi ; réussite : aucun écart sur le nombre d'enregistrements et sur cinq fiches tirées au hasard |

### 5.6 Journal des actions

- Chaque action est inscrite : qui, quoi, quand, sur quelle donnée ; pour une action validée : demande, validation, action, résultat.
- Le journal ne peut être modifié ni par les utilisateurs, ni par les automatisations, ni par l'assistant IA.
- Sa durée de conservation suit le registre des traitements.
- Test : une action prise au hasard se reconstitue de bout en bout à partir du seul journal.

### 5.7 Réversibilité

- Comptes et données au nom de vos sociétés dès le premier jour : vous n'avez pas besoin de nous pour partir.
- En fin de contrat, vous recevez : l'export complet (section 4.3), l'accès administrateur à tous les comptes, le code, la documentation, les réglages, les procédures et fiches de secours, et une attestation de suppression des copies chez le prestataire. Délai écrit au contrat : quinze jours ouvrés au plus après la fin du préavis.
- Une **sortie à blanc** (export complet, rechargement dans un espace vide, vérification) est faite une première fois à la fin du pilote, sur le bâtiment et le lieu du pilote (section 7), puis avant la mise en service générale, puis au moins une fois par an.

### 5.8 Propriété du code et des données

- **Vos données et vos documents** sont à vous, toujours restituables. Ils ne servent qu'à vous : aucune réutilisation pour un autre client ni pour de la prospection.
- **Le code développé pour vous** est cédé à votre société par écrit, au paiement complet, droit par droit. Il est déposé sur un espace de code au nom de votre société.
- **Les composants génériques** du prestataire (méthodes, modèles, briques réutilisables) vous sont concédés sous licence gratuite, non exclusive et perpétuelle.
- **La liste des composants tiers** et de leurs licences est remise avec chaque version.
- **Les logiciels du marché** restent la propriété de leurs éditeurs ; vos sociétés y ont un abonnement à leur nom, et vos données s'en exportent.

---

## 6. Ce que le logiciel ne fait pas

- Il ne remplace pas votre **expert-comptable** : il ne tient pas la comptabilité, ne produit ni le fichier des écritures comptables, ni les déclarations fiscales, ni les comptes annuels.
- Il ne remplace pas la **plateforme agréée** de facturation électronique : il prépare et s'y connecte.
- Il n'**encaisse** rien : ni loyer, ni vente, ni séjour. Il ne fait aucun **paiement**.
- Il ne délivre ni ne remplace les **autorisations des lieux** : déclaration d'entrepreneur de spectacles, licence de débit de boissons, autorisation d'ouverture, avis de la commission de sécurité. Il ne déclare jamais un lieu « conforme ».
- Il ne remplace pas votre **avocat**, votre **notaire**, votre **architecte** ni les **organismes de contrôle**.
- Il ne **gère pas vos biens** pour vous : votre administratrice ou vos sociétés l'utilisent ; si vous confiez la gestion à un administrateur de biens, il le fait sous sa propre responsabilité.
- Il ne **décide** pas : il prépare, rappelle, calcule et classe. Décider, signer, payer et envoyer restent humains.
- Il ne **note** ni ne trie des personnes : candidats locataires, candidats à un emploi, salariés.
- Il n'est pas une **caisse**, une **billetterie** ni un **logiciel hôtelier** : il en reprend les totaux.
- Il ne promet aucun **gain de temps** avant la mesure faite pendant le pilote.

---

## 7. Étapes

Chaque étape fait l'objet d'une commande séparée. À la fin de chaque étape, vous pouvez vous arrêter : vous gardez ce qui est payé, vos comptes et vos données. Le cadrage du logiciel s'intègre au cadrage général de vos projets, si vous faites de ce logiciel l'une de vos priorités. Notre proposition « Votre logiciel de gestion des propriétés » reprend ces quatre étapes, avec leurs dates et leurs prix.

| Étape | Ce qui se fait | Données utilisées | Pour passer à l'étape suivante (toutes les conditions) |
| --- | --- | --- | --- |
| **1. Cadrage et choix des logiciels** | Inventaire de vos sociétés, bâtiments, lots, baux, lieux, contrats et outils actuels ; tâches de votre administratrice ; choix des modules et de leur ordre ; pour chaque brique, comparaison entre logiciels du marché et construction, sur les informations publiées par les éditeurs ; questions à vos professionnels ; mesure de départ du temps passé sur les tâches visées. Si le cadrage général ne suffit pas à choisir, une comparaison détaillée par module se commande à part | Vos documents, consultés sans import | Inventaire validé par écrit ; modules et ordre choisis ; choix argumenté pour chaque brique ; critères de réception du pilote écrits ; réponses de vos professionnels aux questions qui bloquent le pilote ; mesure de départ relevée |
| **2. Maquette et essai sur données fictives** | Maquette cliquable : écrans des modules retenus, sans vrais calculs, pour vérifier l'usage avant de construire ; essais par votre administratrice. Logiciel de gestion locative du marché essayé sur le jeu d'essai d'au moins vingt baux (module 2), sur un compte d'essai ouvert par votre société | Données fictives seulement | Votre administratrice réalise sans aide au moins dix scénarios types (enregistrer un bail, voir une échéance, préparer une quittance, comparer deux devis…) ; chaque blocage relevé est corrigé, puis le scénario est refait sans aide ; vingt baux d'essai justes au centime (critère 1 du module 2), ou décision de construire le module 2 ; vous validez par écrit les écrans et les critères de réception ; export complet testé sur les données fictives ; société, bâtiment et lieu du pilote nommés ; préalables de la section 5.2 réunis |
| **3. Pilote sur un bâtiment et un lieu** | Mise en service des modules retenus sur un seul bâtiment et un seul lieu ; import de l'existant ; automatisations activées une par une, après essai et votre validation écrite | Données réelles du bâtiment et du lieu du pilote | Critères de réception de chaque module tenus quatre semaines de suite (les critères mensuels, sur un mois complet) ; aucune erreur critique ; usage réel : votre administratrice utilise l'outil chaque semaine pour les tâches visées et y traite au moins 80 % des échéances du pilote ; temps mesuré et comparé à la mesure de départ ; restauration réussie dans un espace neuf ; première sortie à blanc réussie sur le bâtiment et le lieu du pilote (export complet relu, rechargé dans un espace vide, vérifié) ; fiche de secours manuel et bouton d'arrêt testés une fois |
| **4. Mise en service progressive** | Un bâtiment, un lieu ou un module de plus à la fois, chacun avec les mêmes critères ; contrôle hebdomadaire des tâches automatiques ; bilan après chaque extension | Données réelles, extension par extension | Chaque extension tient ses critères quatre semaines de suite avant la suivante ; sortie à blanc réussie avant la mise en service générale ; tests de restauration et d'arrêt au calendrier de la section 5 |

**Ce qui arrête ou réduit le projet.**
- Si un logiciel du marché passe les critères d'un module, on le retient et on ne construit pas ce module.
- Si le pilote ne tient pas ses critères après une correction, on s'arrête ou on revient à un logiciel du marché.
- Toute erreur critique arrête l'automatisation en cause jusqu'à sa correction et un nouvel essai.

---

## 8. Questions à trancher avec vous et votre administratrice

**Sociétés et bâtiments**
1. Quelles sociétés possèdent vos bâtiments ? Lesquelles exploitent vos lieux ? Y a-t-il une holding ?
2. Quels bâtiments : adresse, usage, surfaces, état ? Lesquels reçoivent du public ?
3. Chaque société a-t-elle choisi sa plateforme de réception des factures électroniques ? (à voir avec votre expert-comptable)

**Baux**
4. Combien de baux, de quel type : commerciaux, professionnels, d'habitation, entre vos sociétés ?
5. L'option pour la TVA a-t-elle été prise, et pour quels immeubles ?
6. Qui gère les baux : vous, votre administratrice, ou un administrateur de biens ?
7. Les loyers sont-ils payés par mois ou par trimestre ? Sur quels comptes ?

**Lieux**
8. Galerie, cabaret, commerces : quelle société exploite chacun, et quand ouvre-t-il ?
9. Des logiciels de caisse, de billetterie ou de réservation sont-ils déjà choisis ?
10. Une activité d'hébergement reprendra-t-elle ? Combien de chambres ? Qui l'exploiterait ?

**Utilisateurs et rôles**
11. Quel est le périmètre de votre administratrice : quelles sociétés, quels lieux ? Quels pouvoirs écrits lui donnez-vous : valider un envoi, un devis, une dépense, gérer les droits ?
12. Quels outils utilise-t-elle aujourd'hui ? Quelles tâches lui prennent le plus de temps ? Que veut-elle garder tel quel ?
13. Qui seront les responsables de lieux ? Combien d'utilisateurs en tout ?
14. Votre expert-comptable : quel logiciel, quel format d'échange, quel calendrier mensuel ?
15. Des professionnels (avocat, notaire, architecte, bureau de contrôle) doivent-ils consulter certains dossiers ? En lecture seule, pour une durée limitée ?

**Choix techniques**
16. Validez-vous un hébergement dans l'Union européenne, sur un compte au nom de votre société ?
17. Souhaitez-vous signer à distance avec un outil de signature électronique du marché ?
18. Qui a besoin de l'outil sur téléphone : responsables de lieux, visites de chantier ?
19. Souhaitez-vous l'assistant IA ? Sur quels documents ? Avec un fournisseur qui traite les données dans l'Union européenne, ou un autre, avec des données pseudonymisées (noms et coordonnées remplacés par des codes) ?
20. Qui assure la maintenance technique, et qui est l'interlocuteur en cas d'incident ?

**Priorités**
21. Par quel bâtiment et quel lieu commencer le pilote ?
22. Quels modules en premier ? Notre suggestion : documents et échéances (5) et patrimoine (1), qui servent de base aux autres.
23. Avez-vous reçu d'autres offres pour un logiciel de ce type ? Si oui, cette annexe permet de les comparer à périmètre égal : modules couverts, données, réversibilité, propriété, critères de réception.

---

## Textes de référence

Pages officielles consultées le 9 novembre 2026. Les règles changent : chaque point est à vérifier à la date de mise en service, avec vos professionnels.

| Sujet | Source |
| --- | --- |
| Facturation électronique : calendrier, plateformes agréées | https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees ; https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees ; https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/fiche-3_tpe_a-partir-de-quand-mon-entreprise-doit-etre-prete.pdf |
| Facturation électronique : loyers exonérés, données transmises à l'administration | https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_je-decouvre-la-facturation-electronique.pdf |
| Bail commercial : indice de révision du loyer | https://entreprendre.service-public.gouv.fr/vosdroits/F20564 |
| Bail commercial : charges et dépenses | https://entreprendre.service-public.gouv.fr/vosdroits/F32336 |
| Bail commercial : loyer et révision | https://entreprendre.service-public.gouv.fr/vosdroits/F31925 |
| Bail commercial : loi du 26 mai 2026 | https://entreprendre.service-public.gouv.fr/actualites/A18929 |
| Bail commercial : contenu et annexes | https://entreprendre.service-public.gouv.fr/vosdroits/F23927 |
| Logement : révision du loyer, dépôt de garantie | https://www.service-public.gouv.fr/particuliers/vosdroits/F13723 ; https://www.service-public.gouv.fr/particuliers/vosdroits/F31269 |
| Réduction des consommations des bâtiments tertiaires | https://entreprendre.service-public.gouv.fr/vosdroits/F38065 |
| Sécurité incendie d'un établissement recevant du public | https://entreprendre.service-public.gouv.fr/vosdroits/F31684 |
| Registre de sécurité (code de la construction et de l'habitation, articles R143-34 à R143-44) | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074096/LEGISCTA000043819015/ |
| Accessibilité d'un établissement recevant du public | https://entreprendre.service-public.gouv.fr/vosdroits/F32873 |
| Taxe de séjour | https://entreprendre.service-public.gouv.fr/vosdroits/F743 |
| Fiche individuelle de police | https://www.service-public.gouv.fr/particuliers/vosdroits/F33458 |
| Durées de conservation des documents | https://entreprendre.service-public.gouv.fr/vosdroits/F10029 |
| Logiciels de caisse | https://bofip.impots.gouv.fr/bofip/10691-PGP.html/identifiant=BOI-TVA-DECLA-30-10-30-20260325 |
| Billetterie des lieux de spectacle | https://bofip.impots.gouv.fr/bofip/1054-PGP.html/identifiant%3DBOI-TVA-DECLA-20-30-20-30-20120912 |
| Gestion locative et données personnelles (CNIL) | https://www.cnil.fr/sites/default/files/atoms/files/referentiel_relatif_aux_traitements_de_donnees_personnelles_mis_en_oeuvre_dans_le_cadre_de_la_gestion_locative.pdf |
| Données personnelles (règlement général sur la protection des données) | https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32016R0679 |
| Gestion de biens pour autrui (loi n° 70-9, article 1er) | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000028806892 |
| Règlement européen sur l'IA | https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:02024R1689-20260727 |
| Règlement européen sur les données | https://eur-lex.europa.eu/legal-content/FR/TXT/HTML/?uri=CELEX:32023R2854 |

## Petit lexique

- **Plateforme agréée** : opérateur immatriculé par l'État pour émettre, recevoir et transmettre les factures électroniques.
- **Établissement recevant du public (ERP)** : lieu ouvert au public, classé par type et par catégorie, soumis à des règles de sécurité et d'accessibilité.
- **OPERAT** : plateforme publique de déclaration des consommations d'énergie des bâtiments tertiaires.
- **Jeu d'essai** : cas préparés à l'avance, avec leur résultat attendu, pour vérifier l'outil.
- **Sortie à blanc** : test de départ : on exporte tout, on recharge dans un espace vide, on vérifie que rien ne manque.
- **Journal des actions** : liste non modifiable de ce qui a été fait, par qui et quand.

Relecture contradictoire : 48 vérifications, 25 corrections ; mise en cohérence entre documents : 9 corrections — 9 novembre 2026
