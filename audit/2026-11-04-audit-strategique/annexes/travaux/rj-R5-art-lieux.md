# R5-art-lieux : vente d'œuvres, événements, lieux et robotique — obligations en vigueur au 4 novembre 2026

Mémo du chercheur « R5-art-lieux » pour l'audit Marwin Tech × GianLuca Carlone. Rédigé le 4 novembre 2026. Toutes les pages web citées ont été consultées le **4 nov. 2026**. Le dépôt `Momolscode/Carlone` (branche main, commit 7b46602) a été lu sans être modifié. Les chemins du dépôt sont relatifs à sa racine. Aucune action extérieure n'a été faite : aucun contact, aucune démarche, aucune dépense.

Codes : [FV] fait vérifié dans une source primaire ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ou interprétation ; [ES] estimation ; [MM] mesure ; [IN] inconnu.

Ce mémo **n'est pas un avis juridique**. Il prépare les questions à poser à un avocat, à l'expert-comptable, à la mairie, à la commission de sécurité, à la préfecture, à la DRAC, à l'assureur et à un intégrateur robotique.

---

## 0. À lire d'abord

### 0.1 Limites de la recherche

1. **EUR-Lex n'a pas pu être ouvert directement** (pages vides ou refus derrière un filtre anti-robot). Les textes européens (règlements 2023/1230 et 2026/1744, directive 2024/2853, règlement 2024/1624) ont été lus par les extraits que renvoie un moteur de recherche (Exa) **sur le domaine eur-lex.europa.eu**. Ils sont classés [FV], avec cette réserve. Les pages LawPlayer, Certifico et cabinets d'avocats ne servent que de recoupement. Elles sont signalées comme **sources secondaires**.
2. **Pages non ouvertes** : la page Urssaf sur la contribution des diffuseurs (erreur 503), la fiche DGCCRF « Petits professionnels » sur economie.gouv.fr (erreur 403) et sacem.fr (domaine refusé à l'outil). Elles ont été remplacées par le site de la Sécurité sociale des artistes-auteurs, Légifrance et Service Public.
3. **Extraits de recherche** : quelques textes (articles L131-3 du CPI, L7121-3 du Code du travail, R1336-1 du CSP, L321-2 du Code de commerce, L421-3 du Code de la consommation, articles 1927-1928 du Code civil) n'ont été vus que dans les **extraits de résultats Légifrance**. Ils sont marqués « extrait Légifrance, page non ouverte ».
4. **Faits du dossier** : aucun lieu de GianLuca Carlone n'est établi. On ne connaît ni l'adresse, ni le propriétaire, ni l'exploitant, ni la jauge, ni le stade d'acquisition (`ex-C9-lieux.md:219`). L'entité qui vendra les œuvres n'est pas décidée (`interne/offres-de-carlone-catalogue-crm.md:90`). Les règles ci-dessous sont donc présentées **par hypothèse d'usage**. Elles ne valent pas validation d'un lieu.
5. **Fiscalité de l'art** (TVA à 5,5 %, régime de la marge, article 238 bis AB, facture électronique) : elle est traitée dans `rj-R2-fiscal.md`, auquel ce mémo renvoie sans refaire l'analyse.

### 0.2 Règles modifiées en 2025 ou 2026, ou qui changent bientôt

| Règle | Changement | Effet au 4 nov. 2026 | Source |
|---|---|---|---|
| LCB-FT, art. L561-2 CMF | Version modifiée par la **loi n° 2026-725 du 3 août 2026** (art. 26), en vigueur depuis le **5 août 2026**. La page cite aussi la loi n° 2026-534 du 25 juin 2026. | Le 10° (marchands d'art, seuil de 10 000 €) est en vigueur dans les termes cités au § (a). **Ce que ces lois ont changé dans l'article n'a pas été analysé** [IN]. | Légifrance, L561-2 [FV] |
| LCB-FT, règlement (UE) 2024/1624 (AMLR) | Applicable le **10 juillet 2027** : plafond européen de 10 000 € pour les paiements en espèces, et marchands d'art assujettis à partir de 10 000 €. | Pas encore applicable. Prévoir l'adaptation pour 2027. | EUR-Lex, synthèse [FV] |
| Import de biens culturels, règlement (UE) 2019/880 | Pleinement applicable depuis le **28 juin 2025** : licence ou déclaration de l'importateur selon les catégories. | En vigueur. | Douane, extrait de recherche [FV partiel] |
| Sécurité incendie des ERP, art. GN 6 | Délai de demande porté de 15 jours à **deux mois** avant une manifestation inhabituelle (arrêté du 30 oct. 2023, en vigueur le 4 nov. 2023). | En vigueur. | Légifrance [FV] |
| ERP de 5e catégorie, art. PE 2 et suivants | Modifiés par l'**arrêté du 1er décembre 2025** (PE 2, PE 7, PE 9 et PE 21 au 1er janvier 2026 ; PE 4 et PE 10 au 1er juillet 2026) et par l'arrêté du 4 février 2026 (PE 27, au 1er mai 2026). | Seuils de la 5e catégorie inchangés pour les types utiles ici. **Le contenu des autres modifications n'a pas été analysé** [IN]. | Légifrance [FV] |
| Règlement de sécurité ERP, arrêté du 19 février 2026 | Structures combustibles, réaction au feu, dossier de sécurité. | S'appliquera aux autorisations de travaux déposées **à partir du 1er juin 2027**. | Légifrance [FV] |
| Règlement machines (UE) 2023/1230 | Modifié par le **règlement (UE) 2026/1744 du 8 juillet 2026** (« Digital Omnibus on AI »), en vigueur le 27 juillet 2026. Il ajoute des exigences sur l'IA, par actes délégués, qui « shall apply by 2 August 2028 ». | **La date d'application du 20 janvier 2027 est inchangée.** | EUR-Lex [FV, via extraits] |
| AI Act, systèmes à haut risque de l'annexe I | Report au **2 août 2028** (règlement 2026/1744, considérant 40). Les machines passent de la section A à la section B de l'annexe I. | Sans effet immédiat pour un bras peintre dont l'IA n'est pas un composant de sécurité [HY]. | EUR-Lex [FV, via extraits] |
| Responsabilité du fait des produits, directive (UE) 2024/2853 | S'applique aux produits mis sur le marché ou en service après le **9 décembre 2026** ; elle couvre les logiciels et l'IA. | Transposition française **non adoptée selon les dernières sources trouvées** (réponse ministérielle du 12 mai 2026 ; cabinets, sept. 2026). État au 4 nov. : [IN]. | EUR-Lex [FV] ; AN [FV] ; secondaires [DR] |
| Obligation générale de sécurité, art. L421-3 C. conso | Depuis le **13 décembre 2024** (loi n° 2024-364), l'article ne vise plus que les **services**. Les produits relèvent du règlement (UE) 2023/988. | En vigueur. | Extrait Légifrance [FV partiel] |
| TVA à 5,5 % sur les œuvres, transfert au CIBS, facture électronique | Voir `rj-R2-fiscal.md:14-17`. | — | R2 |

### 0.3 Corrections à apporter aux pièces du dépôt

| Pièce | Ce qu'elle dit | Correction | Code |
|---|---|---|---|
| `interne/offre-marwin-tech-remuneration-et-collaboration.md:100` ; `interne/contexte-projet-carlone.md:97` ; `interne/state-of-the-art-note-de-vision.md:110` | La norme **ISO 10218-2:2025** est citée comme référence pour un bras robotisé « près du public » ou « en galerie ». | Selon la fiche ISO, cette norme ne couvre **pas** les dangers « when the public or non-working adults have access ». Elle sert à concevoir la cellule, mais elle **ne suffit pas** pour une démonstration devant des visiteurs. Il faut une analyse de risques propre au lieu et au public, confiée à un intégrateur, plus les règles ERP (GN 6). | [FV] iso.org |
| Mêmes pièces | Règlement machines « applicable au 20 janvier 2027 ». | Exact [FV]. Il faut ajouter que le règlement a été modifié en juillet 2026 (règlement 2026/1744) sans changement de cette date. | [FV] |
| `crm/docs/hermes-vocalcom.md:324-333` ; `interne/offres-de-carlone-catalogue-crm.md:101` | Règle de rétractation de 14 jours et absence de paiement avant 7 jours pour les ventes hors établissement à une entreprise de 5 salariés au plus. Pièce appuyée sur des sources secondaires (Actu-Juridique, Le Monde du droit). | **Confirmée sur Légifrance** : L221-3, qui étend les sections 2, 3 et 6, dont L221-10. Il faut ajouter deux exceptions : la **commande sur mesure** (L221-28, 3°) et l'**enchère publique** (L221-28, 11°). Il faut aussi préciser que **la vente à distance entre professionnels n'est pas visée** par L221-3. | [FV] |
| `pour-carlone/vernissage-strates-idees.md:81, 89` | Œuvres « mises aux enchères » en fin de soirée. | L'appellation « ventes aux enchères publiques » est réservée aux opérateurs habilités (art. L321-2 du Code de commerce, extrait Légifrance). À faire valider par un avocat avant toute annonce. | [FV partiel] |

---

## (a) Marchand d'art : registre, LCB-FT, droit de suite, authenticité, factures, provenance

### Réponse courte

- **Registre des objets mobiliers (« livre de police »).** Il est obligatoire pour toute personne dont l'activité « comporte la vente d'objets mobiliers usagés ou acquis à des personnes autres que celles qui les fabriquent ou en font le commerce » (art. 321-7 du Code pénal). Il faut le tenir **jour par jour** et déclarer l'activité au préalable à la préfecture (R321-1). Le registre mentionne aussi les objets **déposés en vue de la vente** (R321-3). Sanction : **6 mois et 30 000 €** pour une personne physique, 150 000 € pour une personne morale [FV].
  - Une galerie qui revend des œuvres achetées à des collectionneurs y est soumise.
  - Une galerie qui ne vend que des œuvres reçues directement des artistes (qui « fabriquent » les œuvres) en est **probablement** exclue [HY fondée sur le texte FV]. Par prudence, il faut tenir le registre dès la première œuvre du second marché.
- **LCB-FT.** Les marchands et intermédiaires d'œuvres d'art, galeries comprises, sont assujettis « lorsque la valeur de la transaction ou d'une série de transactions liées est d'un montant égal ou supérieur à 10 000 euros » (L561-2, 10° du CMF, version du 5 août 2026) [FV]. Leurs obligations :
  - identifier le client et le bénéficiaire effectif ;
  - connaître l'objet de la relation ;
  - repérer les personnes politiquement exposées ;
  - exercer une vigilance renforcée si le risque est élevé ;
  - établir une cartographie des risques et des procédures ;
  - désigner un déclarant et un correspondant Tracfin ;
  - faire une déclaration de soupçon si nécessaire ;
  - conserver les documents **5 ans** [FV].

  Le contrôle revient à la **DGDDI** (douane), avec une sanction jusqu'à **5 000 000 €** [FV]. Les espèces sont limitées à **1 000 €** pour un client domicilié en France [FV].
- **Droit de suite** (art. L122-8 du CPI) [FV] :
  - Il s'applique aux **reventes** après la première cession par l'auteur, lorsqu'un professionnel du marché de l'art intervient.
  - Seuil : **750 €**. Taux dégressifs : **4 %** jusqu'à 50 000 €, 3 %, 1 %, 0,5 %, puis 0,25 % au-delà de 500 000 €. Plafond : **12 500 €** par vente.
  - Il est « à la charge du vendeur ». Le paiement incombe au **professionnel** qui intervient : le vendeur professionnel, à défaut l'intermédiaire qui reçoit le paiement, à défaut l'acheteur professionnel.
  - Il ne joue pas si le vendeur a acheté l'œuvre directement à l'auteur moins de 3 ans avant et revend à 10 000 € au plus.
  - Une vente en dépôt-vente pour le compte de l'artiste est une première cession : pas de droit de suite [HY fondée sur L122-8].
- **Authenticité (décret n° 81-255, dit « Marcus »).** Il n'existe **pas d'obligation légale de remettre un « certificat d'authenticité »** séparé [HY : aucun texte trouvé qui l'impose]. Le décret oblige le vendeur professionnel à délivrer, **si l'acheteur le demande**, une facture ou un bordereau qui précise la nature, la composition, l'origine et l'ancienneté de l'objet. Les formules employées engagent le vendeur : signature de l'artiste, « attribué à », « atelier de », etc. Une reproduction doit porter la mention « Reproduction ». Sanction : contravention de 5e classe [FV].
- **Factures.** Il faut les mentions générales, celles du décret Marcus et le régime de TVA de chaque œuvre (voir R2).
- **Provenance et circulation.** Le registre et la LCB-FT imposent de documenter l'origine. À l'importation hors UE, la licence ou la déclaration de l'importateur est en vigueur depuis le **28 juin 2025** (règlement 2019/880), surtout pour des biens anciens. Elle concerne peu l'art contemporain d'artistes vivants [FV partiel / HY].
- **Contribution « diffuseur ».** Une galerie qui vend des œuvres originales doit à la Sécurité sociale des artistes-auteurs **1 % + 0,1 %** de **30 % du prix de vente TTC**, ou de la **commission TTC** en dépôt-vente, y compris pour des artistes décédés (R382-17 CSS ; secu-artistes-auteurs.fr) [FV]. Ce point est ajouté car il manquait dans le dossier.

### Détail

**a.1 Registre et déclaration préalable.**
- Champ d'application (art. 321-7, en vigueur depuis le 16 mars 2011). Le registre indique « la nature, les caractéristiques, la provenance, le mode de règlement de l'objet ». Il permet d'identifier les objets et les personnes qui les ont vendus ou apportés [FV].
- Contenu (R321-3, version du 29 janvier 2012) [FV] :
  - l'identité de chaque personne qui a vendu, échangé ou **déposé en vue de la vente**, avec les références de sa pièce d'identité ;
  - la nature, la provenance et la description des objets.
- Autres articles :
  - R321-4 : un numéro d'ordre par objet ;
  - R321-5 : prix d'achat et estimation ;
  - R321-6 : registre papier coté et paraphé, inscriptions à l'encre indélébile, conservation 5 ans ;
  - R321-6-1 : registre informatisé, données conservées **10 ans**.
- Déclaration préalable en préfecture (R321-1, version du 1er novembre 2021). Le formulaire est la « Demande d'inscription sur le registre des revendeurs d'objets mobiliers ». Il faut garder le récépissé (F39552, vérifiée le 24 avril 2026) [FV].
- Nuance : la fiche F39552 indique que les œuvres d'art « ne sont pas considérés comme des biens d'occasion » au sens de la définition du bien d'occasion. **Cela n'écarte pas l'article 321-7**, dont le critère est différent : un objet « acquis à des personnes autres que celles qui les fabriquent » [HY fondée sur les deux textes FV]. À faire confirmer par la préfecture ou un avocat.
- Selon l'archive, GianLuca Carlone est un « marchand d'art venu de l'avenue Montaigne » (`interne/offres-de-carlone-catalogue-crm.md:9`) [DR]. Il tient peut-être déjà un registre pour une structure parisienne [IN]. La galerie de 2027, si c'est une nouvelle entité ou un nouvel établissement, doit faire sa propre déclaration ou une déclaration de changement, et ouvrir **un registre par établissement** (F39552) [FV].

**a.2 Lutte contre le blanchiment (LCB-FT).**
- Texte (L561-2, 10°, version en vigueur depuis le 5 août 2026) : « Les personnes qui négocient des œuvres d'art et des antiquités ou agissent en qualité d'intermédiaires […] y compris lorsque celui-ci est réalisé par des galeries d'art, lorsque la valeur de la transaction ou d'une série de transactions liées est d'un montant égal ou supérieur à 10 000 euros » [FV].
- Obligations rappelées par la fiche DGDDI du 26 juillet 2024 [FV] :
  - identification et vérification du client et du bénéficiaire effectif (L561-5) ;
  - connaissance de l'objet de la relation (L561-5-1) ;
  - vigilance constante (L561-6) ;
  - mesures complémentaires pour les personnes politiquement exposées et les pays à risque (L561-10) ;
  - vigilance renforcée (L561-10-1) ;
  - examen renforcé des opérations inhabituelles (L561-10-2) ;
  - interdiction d'exécuter l'opération si l'identification est impossible (L561-8).
- Lignes directrices DGDDI-Tracfin pour les marchands d'art (novembre 2020) [FV] :
  - une cartographie des risques et des procédures écrites (L561-32) ;
  - un déclarant et un correspondant Tracfin, qui peuvent être « une seule et même personne en cas d'effectif inférieur à cinq personnes » ;
  - une conservation de **5 ans** ;
  - des obligations de **gel des avoirs**.

  Ces lignes directrices datent de 2020. Elles n'intègrent pas les lois de 2026 [IN sur les écarts].
- Espèces (F10999, vérifiée le 26 juin 2026) [FV] :
  - « limité à 1 000 € » pour un particulier domicilié en France ;
  - pour un client domicilié à l'étranger qui règle une dépense personnelle : jusqu'à **15 000 €** auprès d'un professionnel soumis à la LCB-FT, sinon 10 000 € ;
  - amende jusqu'à 5 % des sommes, partagée entre les deux parties.
- 2027 : l'AMLR (règlement 2024/1624) s'appliquera le **10 juillet 2027**. Il fixe un plafond européen de 10 000 € pour les espèces et maintient l'assujettissement des marchands de biens culturels à partir de 10 000 € (synthèse EUR-Lex) [FV]. La définition exacte des « biens culturels » visés reste à vérifier : un commentaire secondaire renvoie à l'annexe I du règlement 116/2009, ce qui pourrait restreindre le champ [HY, source secondaire].

**a.3 Droit de suite** [FV, sauf mention contraire].
- Article L122-8, version en vigueur depuis le 24 décembre 2016 (ordonnance 2016-1823) :
  - champ : « toute vente d'une oeuvre après la première cession opérée par l'auteur », dès qu'intervient « un professionnel du marché de l'art » ;
  - exception : achat direct à l'auteur depuis moins de trois ans et prix de vente d'au plus 10 000 € ;
  - principe : « Le droit de suite est à la charge du vendeur. »
- Partie réglementaire :
  - R122-5 : non exigible sous **750 €** ; prix hors taxes (prix de cession perçu par le vendeur ou prix d'adjudication) ;
  - R122-6 (version du 25 juin 2022) : 4 % jusqu'à 50 000 € ; 3 % de 50 000,01 à 200 000 € ; 1 % de 200 000,01 à 350 000 € ; 0,5 % de 350 000,01 à 500 000 € ; 0,25 % au-delà ; total « ne peut excéder 12 500 euros » ;
  - R122-9 : responsable du paiement = vendeur professionnel, à défaut l'intermédiaire qui reçoit le paiement, à défaut l'acheteur professionnel ;
  - R122-10 : paiement dans les 4 mois de la demande ; à défaut de demande, information d'un organisme de gestion collective (par exemple l'ADAGP, [HY sur le nom]) au plus tard 3 mois après la fin du trimestre ;
  - R122-12 : contravention de 3e classe.
- Un extrait d'arrêt de la Cour de cassation (assemblée plénière) indique qu'une clause peut faire supporter **la charge économique** du droit de suite à l'acheteur, sans changer le redevable légal [FV partiel, extrait Légifrance non ouvert].

**a.4 Authenticité : décret n° 81-255 du 3 mars 1981** (en vigueur au 4 nov. 2026) [FV].
- Art. 1 (version du 1er octobre 2001) : sur demande de l'acheteur, remise d'une « facture, quittance, bordereau de vente ou extrait du procès-verbal de la vente publique » qui contient les spécifications de l'œuvre.
- Art. 3 : « l'indication qu'une oeuvre ou un objet porte la signature ou l'estampille d'un artiste entraîne la garantie » que l'artiste en est l'auteur.
- Art. 4 à 7 (extraits de recherche) : « attribué à », « atelier de », « école de » donnent des garanties décroissantes ; « dans le goût de », « style » ou « d'après » n'en donnent aucune.
- Art. 9 : une reproduction doit porter « de manière visible et indélébile la mention "Reproduction" ».
- Art. 10 : contravention de 5e classe.
- **Application au projet** [HY] :
  - Pour des **artistes vivants**, la meilleure preuve reste un certificat signé par l'artiste, joint à une facture conforme au décret, avec la technique et le nombre d'exemplaires.
  - Pour les pièces de STRATES ou les fragments imprimés en 3D, la facture doit décrire honnêtement le procédé (impression, bras robotisé). Une formule ambiguë du type « peint par l'artiste » engagerait la garantie du décret et, en fiscalité, la définition de l'œuvre originale (voir R2, article 98 A).

**a.5 Factures et mentions.**
- Mentions générales et facture électronique : voir R2, section (e). La **réception** électronique est obligatoire depuis le 1er septembre 2026 ; l'**émission** le sera au plus tard le 1er septembre 2027 pour les PME (`rj-R2-fiscal.md:17`) [FV selon R2].
- Mentions propres à l'art, à ajouter [HY, construit sur les textes FV ci-dessus] :
  - artiste, titre, date, technique, dimensions ;
  - numéro d'exemplaire pour un tirage ou une fonte ;
  - formule d'attribution conforme au décret Marcus ;
  - provenance connue ;
  - régime de TVA (5,5 % sur le prix total, ou marge ; voir R2) ;
  - mention du droit de suite si c'est une revente ;
  - pour une vente hors établissement à une petite entreprise : information sur la rétractation (voir (c)).

**a.6 Provenance.**
- Registre (a.1) et LCB-FT (a.2) obligent à tracer l'origine et le vendeur. Pour l'art contemporain acheté directement aux artistes, la provenance se résume au contrat avec l'artiste et à son certificat [HY].
- Importation hors UE (DGDDI, démarche « Importer des biens culturels », extrait de recherche) : « depuis le 28 juin 2025, une licence d'importation ou une déclaration de l'importateur sont requises ». Selon la synthèse EUR-Lex, la déclaration vise les biens de plus de 200 ans d'une valeur supérieure à 18 000 € [FV partiel].
- Exportation hors UE : certificat pour certains biens anciens au-delà de seuils, relevés en 2021, par exemple 300 000 € pour un tableau de plus de 50 ans (décret n° 2020-1718, extrait Légifrance) [FV partiel, page non ouverte]. Cela ne concerne normalement pas les œuvres d'artistes vivants [HY].

**a.7 Contribution des diffuseurs (régime social des artistes-auteurs).**
- R382-17 CSS (version du 1er janvier 2019) : « il est tenu compte de 30 % du prix de vente des oeuvres et, en cas de vente à la commission, du montant de la commission ». La règle vaut pour les œuvres « des artistes, vivants ou morts », même tombées dans le domaine public [FV].
- Taux fixés par arrêté (R382-18) : 1 % pour la Sécurité sociale et 0,1 % pour la formation professionnelle, soit 1,1 %. Source : secu-artistes-auteurs.fr, page mise à jour le 13 janvier 2025 [FV]. **Taux 2026 non revérifié sur urssaf.fr** (page en erreur 503) [IN partiel].
- Exemple [ES] : une œuvre vendue 10 000 € TTC par une galerie qui l'a achetée donne une assiette de 3 000 € et une contribution de 33 €. En dépôt-vente avec une commission de 4 000 € TTC, l'assiette est de 4 000 € et la contribution de 44 €.

### Sources officielles

| Source (URL exacte) | Organisme | Mise à jour affichée | Courte citation |
|---|---|---|---|
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000023717783 | Légifrance (DILA), Code pénal art. 321-7 | En vigueur depuis le 16/03/2011 (loi 2011-267) | « un registre indiquant la nature, les caractéristiques, la provenance, le mode de règlement de l'objet » |
| https://www.legifrance.gouv.fr/codes/id/LEGIARTI000043531943/2021-11-01 | Légifrance, Code pénal R321-1 à R321-8 | R321-1 en vigueur depuis le 01/11/2021 | « Toute personne soumise à l'obligation de tenir le registre d'objets mobiliers » |
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000025213232 | Légifrance, Code pénal R321-3 | En vigueur depuis le 29/01/2012 | « Le registre d'objets mobiliers prévu au premier alinéa de l'article 321-7 comporte : » |
| https://entreprendre.service-public.gouv.fr/vosdroits/F39552 | Service Public Entreprendre (DILA) | Vérifié le 24/04/2026 | « Vous devez conserver le récépissé que la préfecture vous remet. » |
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033582023 | Légifrance, CMF L561-2 | En vigueur depuis le 05/08/2026 (loi 2026-725, art. 26) | « y compris lorsque celui-ci est réalisé par des galeries d'art » ; « égal ou supérieur à 10 000 euros » |
| https://www.douane.gouv.fr/sites/default/files/2024-07/26/fiche-d-information-lcb-ft-fr.pdf | DGDDI | PDF du 26/07/2024 | « sanction pécuniaire d'un montant maximum de 5 000 000 € » |
| https://www.douane.gouv.fr/sites/default/files/uploads/files/TRACFIN/lignes-directrices-tracfin-dgddi-marchands-d-art-novembre-2020.pdf | DGDDI et Tracfin | Novembre 2020 | « une seule et même personne en cas d'effectif inférieur à cinq personnes » |
| https://www.service-public.gouv.fr/particuliers/vosdroits/F10999 | Service Public (DILA) | Vérifié le 26/06/2026 | « Le paiement en espèces d'un particulier à un professionnel ou entre professionnels est limité à 1 000 €. » |
| https://eur-lex.europa.eu/EN/legal-content/summary/preventing-abuse-of-the-financial-system-for-money-laundering-and-terrorism-purposes-from-2027.html | EUR-Lex, synthèse de l'AMLR 2024/1624 | Non affichée | « The regulation will apply from 10 July 2027 » |
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000033688066 | Légifrance, CPI L122-8 | En vigueur depuis le 24/12/2016 | « Le droit de suite est à la charge du vendeur. » |
| https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069414/LEGISCTA000019989747/ | Légifrance, CPI R122-2 à R122-12 | R122-6 en vigueur depuis le 25/06/2022 | Montant total « ne peut excéder 12 500 euros » |
| https://www.legifrance.gouv.fr/loda/id/JORFTEXT000000684875 | Légifrance, décret n° 81-255 | En vigueur ; art. 1 depuis le 01/10/2001 | « facture, quittance, bordereau de vente ou extrait du procès-verbal de la vente publique » |
| https://www.douane.gouv.fr/demarche/importer-des-biens-culturels | DGDDI | Non lue directement (extrait de recherche) | « depuis le 28 juin 2025, une licence d'importation ou une déclaration de l'importateur sont requises » |
| https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006173688/ | Légifrance, CSS R382-17 et R382-18 | R382-17 en vigueur depuis le 01/01/2019 | « il est tenu compte de 30 % du prix de vente des oeuvres » |
| https://www.secu-artistes-auteurs.fr/commerce-dart/taux-de-contribution-des-commerces-dart | Sécurité sociale des artistes-auteurs | Mise à jour le 13/01/2025 | Sécurité sociale 1 % ; formation 0,1 % ; « Y compris les ventes à l'exportation » |

### Incertitudes et points à faire valider

1. **Qui vend** : GianLuca Carlone en personne, une société parisienne existante ou une nouvelle société de galerie ? [IN] (`interne/offres-de-carlone-catalogue-crm.md:90`). Toutes les obligations ci-dessus pèsent sur cette entité. Interlocuteurs : **avocat** et **expert-comptable** de GianLuca.
2. **Registre pour une galerie qui ne vend que des œuvres d'artistes vivants en dépôt** : le champ de l'article 321-7 est-il applicable ? À faire trancher par la **préfecture de la Nièvre** ou un avocat [HY].
3. **LCB-FT** : contenu exact des modifications de L561-2 par les lois 2026-534 et 2026-725 [IN]. Existence chez GianLuca d'une cartographie des risques et d'un déclarant Tracfin [IN]. Interlocuteurs : **avocat**, DGDDI.
4. **Droit de suite** : quel organisme de gestion collective informer ? (arrêté prévu par R122-7, non relu) [IN].
5. **Contribution des diffuseurs** : taux 2026 à confirmer sur urssaf.fr, ainsi que l'immatriculation de la galerie comme diffuseur [IN partiel]. Interlocuteur : **Urssaf artistes-auteurs**.
6. **Certificat d'authenticité** : aucun texte n'impose de certificat séparé ; c'est une pratique de marché [HY]. Pour les pièces faites à la machine, faire valider par un avocat la rédaction du procédé sur facture et certificat.

### Conséquences pour Marwin Tech et GianLuca Carlone

- **Pour GianLuca Carlone** : ce sont des obligations d'exploitant, pas des options [FV]. Avant toute vente de la galerie ou par le CRM, il faut : un registre (au moins pour le second marché), un dispositif LCB-FT écrit au-delà de 10 000 €, une procédure de droit de suite pour les reventes, des factures conformes au décret Marcus, et la déclaration de diffuseur auprès des artistes-auteurs.
- **Pour Marwin, un risque de requalification** [HY à faire valider par un avocat] :
  - Si Marwin « agit en qualité d'intermédiaire dans le commerce des œuvres d'art » (trouver des acheteurs contre commission, encaisser pour le compte de la galerie), elle peut devenir **elle-même assujettie** à la LCB-FT (L561-2, 10°).
  - Elle peut aussi devenir responsable du paiement du droit de suite (R122-9 : « à défaut l'intermédiaire qui reçoit le paiement »).
  - Une **rémunération variable sur les ventes**, évoquée dans `DEMANDE.md` § 11, doit être rédigée pour ne pas faire de Marwin un intermédiaire de vente. Il faut un contrat de prestation sur le CRM et l'outillage, sans mandat de vente ni encaissement.
- **Ce que Marwin peut apporter** [PR] : dans le CRM, les champs du registre (vendeur ou déposant, pièce d'identité, provenance, mode de règlement, numéro d'ordre), une alerte à 10 000 €, un calcul du droit de suite selon le barème R122-6 et des modèles de facture conformes au décret Marcus. Ces données (pièces d'identité) sont **sensibles** : elles ne doivent pas aller dans le dépôt CRM signalé public (`interne/offres-de-carlone-catalogue-crm.md:96`) [DR]. La conformité RGPD est à traiter par ailleurs.

---

## (b) Contrat de dépôt-vente avec des artistes et assurance « clou à clou »

### Réponse courte

- **Aucun contrat type légal** n'existe pour le dépôt-vente entre une galerie et un artiste [HY : aucun texte spécifique trouvé ; le ministère de la Culture publie un contrat type de **production** d'œuvre, pas de dépôt-vente]. Le contrat se construit à partir de règles connues :
  - le **dépôt** (Code civil, art. 1927-1928) : un dépositaire rémunéré répond « avec plus de rigueur » de la garde de l'œuvre [FV partiel] ;
  - le **mandat** ou la **commission** pour la vente ;
  - le **droit d'auteur** : vendre l'objet ne transfère pas les droits de reproduction. Toute cession (catalogue, site, films) doit mentionner chaque droit cédé et délimiter son étendue, sa destination, le lieu et la durée (L131-3 du CPI) [FV partiel].
- La **TVA** du dépôt-vente (commission ou achat-revente) relève de R2 [renvoi].
- La **contribution diffuseur** se calcule sur la commission (voir (a)) [FV].
- L'**assurance « clou à clou »** (du décrochage chez le prêteur au raccrochage) est une **pratique d'assurance**, pas une obligation légale [HY ; aucune source officielle trouvée]. Elle est vivement recommandée dès qu'une œuvre est transportée, prêtée ou exposée hors de l'atelier. Le contrat doit fixer une **valeur agréée** par œuvre et désigner l'assuré et le payeur.

### Détail

Clauses minimales recommandées [PR, construites sur les textes cités ; à faire relire par un avocat] :

1. **Parties et qualité** : quelle entité de GianLuca est dépositaire ; l'artiste est-il assujetti à la TVA ou en franchise (voir R2).
2. **Inventaire signé** : titre, technique, dimensions, état constaté avec photos datées, certificat de l'artiste, **valeur agréée** pour l'assurance et **prix de vente public minimal**.
3. **Mandat de vente** : prix plancher, remises autorisées, exclusivité éventuelle (territoire, durée), commission en % (à négocier [IN]), délai de reversement à l'artiste après encaissement, droit de regard sur l'acheteur.
4. **Garde et risques** : obligation renforcée du dépositaire rémunéré (art. 1928, extrait Légifrance) ; conditions d'exposition, de stockage et de transport ; interdiction de restaurer sans accord.
5. **Assurance** : « clou à clou » ou « tous risques expositions », pour le transport, l'accrochage, l'exposition, le stockage et le retour. Préciser l'assuré, le bénéficiaire, la franchise et les exclusions (bris, usure, vol sans effraction) [HY, pratique de marché].
6. **Droits d'auteur** : autorisation écrite et délimitée de reproduire les œuvres pour le catalogue, le site, les réseaux, les films de fabrication et le CRM (L131-3). Mention du nom de l'artiste. Respect du droit moral [FV partiel].
7. **Durée, restitution et fin du contrat** : préavis, frais de retour, reprise des invendus, sort des œuvres en cas de cessation ou de redressement de la galerie.
8. **Obligations sociales et fiscales** : contribution diffuseur sur la commission (R382-17) ; factures ou notes conformes.
9. **Droit de suite** : sans objet pour la première vente par la galerie au nom de l'artiste [HY]. Il est dû lors des reventes futures.
10. **Pièces faites à la machine** (impression 3D, bras robotisé) : décrire le procédé ; ne pas les présenter comme des œuvres originales au sens fiscal sans rescrit (voir R2).

Le ministère de la Culture recommande, pour les institutions publiques, un « droit de présentation » versé aux artistes exposés. Son application à une galerie commerciale n'a pas été vérifiée [IN].

### Sources officielles

| Source (URL exacte) | Organisme | Mise à jour affichée | Courte citation |
|---|---|---|---|
| https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006070721/LEGISCTA000006150317/ | Légifrance, Code civil art. 1927 à 1946 | Version de 1804, non modifiée (extrait de recherche) | Art. 1928 : obligation appliquée « avec plus de rigueur » si un salaire est stipulé pour la garde |
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006278958 | Légifrance, CPI L131-3 | Extrait de recherche, page non ouverte | Chaque droit cédé doit faire l'objet d'une « mention distincte dans l'acte de cession » |
| https://www.culture.gouv.fr/content/download/160793/file/Contrat%20type%20de%20production%20d'oeuvre.pdf | Ministère de la Culture | Non datée (non ouverte) | Contrat type de **production** d'œuvre ; pas un dépôt-vente |
| https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006173688/ | Légifrance, CSS R382-17 | En vigueur depuis le 01/01/2019 | « en cas de vente à la commission, du montant de la commission » |

### Incertitudes et points à faire valider

- **Commission usuelle, durée, exclusivité** : aucun chiffre officiel. Les usages du marché varient [IN] ; ne pas inventer de taux. Interlocuteur : **avocat** de GianLuca.
- **Qualification fiscale** (commissionnaire ou mandataire transparent) : voir R2 ; à valider par l'**expert-comptable**.
- **Assurance** : demander à un **assureur spécialisé en objets d'art** une offre « clou à clou » ou « expositions », avec valeur agréée. Vérifier si l'assurance multirisque existante de GianLuca couvre déjà les œuvres confiées [IN].

### Conséquences pour Marwin Tech et GianLuca Carlone

- L'offre 6 « Programme artistes » prévoit une « convention de dépôt, assurance, partage du prix convenu » (`interne/offres-de-carlone-catalogue-crm.md:47`) [PR]. Ce mémo en donne le squelette. **Le contrat doit être signé par l'entité de GianLuca et les artistes**, pas par Marwin [PR].
- Marwin peut préparer l'inventaire, les fiches d'œuvre, les échéanciers de reversement et les alertes de fin de dépôt dans le CRM [PR]. Elle ne doit **pas détenir les œuvres** (garde, transport) sans assurance et sans contrat, car elle deviendrait dépositaire [HY].
- Les **films et visuels** de Marwin qui montrent des œuvres d'artistes exigent une autorisation écrite et délimitée de chaque artiste (L131-3). Cela touche les « films de fabrication » et les visuels (`pour-carlone/vernissage-strates-idees.md:67`, cité par `ex-C9-lieux.md:48`) [HY].
- Medhi a été retiré de l'offre le 4 nov. [DR] (note § C). Si ses pièces sont vendues par la galerie, il lui faut **son propre contrat de dépôt-vente** avec l'entité de GianLuca [PR].

---

## (c) Vente hors établissement à une petite entreprise (5 salariés au plus)

### Réponse courte

- **Confirmé sur Légifrance** [FV] : l'article L221-3 du Code de la consommation (en vigueur depuis le 1er juillet 2016) étend les sections 2, 3 et 6 du chapitre aux « contrats conclus hors établissement entre deux professionnels ». Trois conditions :
  - le contrat est conclu **hors établissement** ;
  - son objet « n'entre pas dans le champ de l'activité principale du professionnel sollicité » ;
  - celui-ci emploie **5 salariés au plus**.
- Effets [FV] :
  - **information précontractuelle** sur papier ou support durable (L221-5, L221-8) ;
  - **exemplaire daté et signé du contrat avec formulaire de rétractation** (L221-9) ;
  - **14 jours** de rétractation (L221-18), qui courent à partir de la réception du bien pour une vente de biens, l'acheteur pouvant se rétracter dès la signature ;
  - si l'information manque, délai **prolongé de 12 mois** (L221-20) ;
  - remboursement sous 14 jours (L221-24) ;
  - **aucun paiement ni aucune contrepartie avant 7 jours** à compter de la conclusion (L221-10, section 3, donc étendu).
- Deux **exceptions** utiles (L221-28, en vigueur depuis le 28 mai 2022) [FV] :
  - 3° biens « confectionnés selon les spécifications du consommateur ou nettement personnalisés », soit la commande sur mesure ;
  - 11° contrats « conclus lors d'une enchère publique ».

  Leur application aux professionnels par le renvoi de L221-3 est logique, car la section 6 est étendue en bloc. Elle reste à confirmer par un avocat [HY].
- **Hors champ** [FV par le texte] : la vente **à distance** (e-mail, téléphone, site) à une petite entreprise. L221-3 ne vise que le hors établissement.

### Détail

- **Ce qui compte comme « hors établissement »** dans le projet [HY, à valider] :
  - rendez-vous chez le client (offre 1) ;
  - vernissage dans les locaux de l'entreprise (offre 5, `interne/offres-de-carlone-catalogue-crm.md:46`) ;
  - vente conclue lors d'une soirée dans un lieu qui n'est pas celui où la galerie exerce en permanence (un autre bâtiment de GianLuca, le Vieux Relais).
  - Une vente signée **à la galerie**, sans sollicitation préalable hors de ses murs, n'est pas visée [HY].
- **« Activité principale »** : l'achat d'une œuvre sort normalement de l'activité principale d'une PME non spécialisée [HY]. Une jurisprudence citée par le dépôt (Cass. 1re civ., 31 août 2022, n° 21-11.455, `crm/docs/hermes-vocalcom.md:331`) apprécie ce critère selon le métier réellement exercé. **Non relue ici** [DR].
- **Calendrier de paiement** [FV] : pas d'acompte avant J+7. Il faut prévoir le formulaire de rétractation. Par prudence, livrer ou encaisser le solde après la fin du délai de 14 jours (recommandation déjà notée dans `crm/docs/hermes-vocalcom.md:333`) [DR, cohérent avec FV].
- **Commande sur mesure (offre 3, `interne/offres-de-carlone-catalogue-crm.md:44`)** : l'exception L221-28, 3° peut écarter la rétractation. Il faut **informer** l'acheteur de l'absence de droit de rétractation (L221-5). L'interdiction de paiement avant 7 jours (L221-10) reste applicable, car elle relève de la section 3 [HY fondée sur FV]. L'acompte prévu « devis de l'artiste, acompte » doit donc attendre J+7.
- **Particuliers (offre 9)** : le régime « consommateur » s'applique pleinement (14 jours à distance ou hors établissement). Il n'y a pas de rétractation légale pour un achat en galerie [FV pour le texte ; F39552 le rappelle pour les biens d'occasion].

### Sources officielles

| Source (URL exacte) | Organisme | Mise à jour affichée | Courte citation |
|---|---|---|---|
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226882 | Légifrance, C. conso L221-3 | En vigueur depuis le 01/07/2016 | « Les dispositions des sections 2, 3, 6 du présent chapitre » ; « inférieur ou égal à cinq » |
| https://www.legifrance.gouv.fr/codes/id/LEGISCTA000032226870 | Légifrance, C. conso L221-8 à L221-10-1 | L221-10 depuis le 01/07/2016 ; L221-9 depuis le 28/05/2022 | « avant l'expiration d'un délai de sept jours » |
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032226842 | Légifrance, C. conso L221-18 | Depuis le 01/07/2016 | « délai de quatorze jours pour exercer son droit de rétractation » |
| https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221365/ | Légifrance, C. conso L221-18 à L221-28 | L221-20 depuis le 28/05/2022 | « le délai de rétractation est prolongé de douze mois » |
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044563170 | Légifrance, C. conso L221-28 | Depuis le 28/05/2022 | « De fourniture de biens confectionnés selon les spécifications du consommateur ou nettement personnalisés ; » |

### Incertitudes et points à faire valider

- La fiche DGCCRF « Petits professionnels : vous avez 14 jours… » (economie.gouv.fr) n'a pas pu être ouverte (erreur 403) [IN]. Elle n'est pas indispensable : le texte de loi a été lu.
- Application des exceptions L221-28 aux professionnels via L221-3 : interprétation à confirmer par un **avocat** [HY].
- Sanctions administratives en cas de manquement : non recherchées ici [IN].

### Conséquences pour Marwin Tech et GianLuca Carlone

- La règle affichée par le CRM est **confirmée** (`crm/docs/rapport/rapport-crm-hermes360.md:88`) [FV]. Il faut la compléter par trois points [PR] :
  - un **modèle de contrat** avec information précontractuelle et formulaire ;
  - un **blocage de l'encaissement avant J+7** dans le suivi des ventes ;
  - la distinction **sur mesure / catalogue** et **hors établissement / à distance**.
- Pour l'offre 5, chaque vente conclue pendant une soirée en entreprise est **hors établissement**. Elle n'est **pas définitive avant 14 jours** pour une entreprise de 5 salariés au plus [FV]. Le prévisionnel de ventes de GianLuca doit en tenir compte.
- La rédaction des documents de vente relève de l'**avocat** de l'entité qui vend. Marwin peut les intégrer techniquement [PR].

---

## (d) Organisation d'événements : ERP, boissons, spectacles, musique, assurance

### Réponse courte

- **Lieu recevant du public (ERP)** [FV] :
  - Tout lieu où le public est admis est un ERP, classé par **type** et par **catégorie** :
    - 1re catégorie : plus de 1 500 personnes ;
    - 2e : de 701 à 1 500 ;
    - 3e : de 301 à 700 ;
    - 4e : jusqu'à 300 ;
    - 5e : sous les seuils fixés par type.
  - Seuils de la 5e catégorie (article PE 2, version du 1er janvier 2026), en effectif total :
    - galerie en magasin (M) ou salle d'exposition (T) : **200** ;
    - salle de réunion (L) : 200 ;
    - salle de spectacles ou **cabaret** (L) : **50** ;
    - restaurant ou bar (N) : 200 ;
    - salle de danse (P) : 120 ;
    - hôtel (O) : 100.
  - Avant toute ouverture, il faut une **visite de réception** par la commission de sécurité et un **arrêté d'ouverture du maire** (R143-38, R143-39). Seule exception : la 5e catégorie sans locaux d'hébergement (renvoi à R143-14).
  - Créer ou modifier un ERP exige une **autorisation de travaux** : 4 mois d'instruction (le silence vaut accord), 5 mois pour un permis de construire.
- **Événement inhabituel dans un ERP**, ou démonstration à risque : il faut une **demande d'autorisation au moins deux mois avant** (art. GN 6, depuis le 4 novembre 2023). Elle est présentée **conjointement** par l'exploitant et l'organisateur si ce sont deux personnes différentes [FV].
- **Boissons** [FV] :
  - Un **débit temporaire** à l'occasion d'une foire, d'une vente ou d'une fête publique ne demande pas de licence, mais l'**autorisation du maire** (L3334-2).
  - Seules les boissons de 18° au plus y sont autorisées, hors Antilles et Guyane.
  - Une association est limitée à 5 autorisations par an.
  - Offrir gratuitement des boissons lors d'un vernissage privé n'est **probablement pas** un « débit » [HY, à confirmer en mairie].
- **Spectacles** [FV] :
  - Une entité dont ce n'est pas l'activité principale peut organiser **jusqu'à 6 représentations par an** sans déclaration (L7122-19, R7122-13).
  - Au-delà, il faut un **récépissé d'entrepreneur de spectacles** : déclaration en ligne, 30 jours d'opposition du préfet, validité 5 ans.
  - Les artistes et techniciens occasionnels sont employés via le **Guso**.
  - Un artiste rémunéré est **présumé salarié** (L7121-3).
- **Musique** [FV] : il faut l'autorisation de la **Sacem** et la rémunération de la **Spré**, même à entrée gratuite :
  - pour une musique de fond lors d'un cocktail ou d'une exposition : forfait par jour ou par semaine ;
  - la Spré vaut 65 % du tarif Sacem, avec un minimum de 102,27 € HT ;
  - réduction de 20 % si la déclaration est faite avant l'installation du matériel.
- **Assurance RC de l'organisateur** : **aucune obligation générale** trouvée pour un événement d'entreprise non sportif [HY ; seules les manifestations sportives et motorisées sont visées par des textes, art. L331-9 du Code du sport]. Elle reste **indispensable en pratique** et souvent exigée par le lieu ou la mairie.

### Détail

1. **Bâtiment non encore ouvert au public.** Le vernissage est envisagé dans « un de ses bâtiments avant l'ouverture de la galerie » (`pour-carlone/vernissage-strates-idees.md:123`) [PR]. Un bâtiment qui reçoit du public devient un ERP [FV, F32351]. S'il n'a ni classement ni autorisation d'ouverture, il faut l'accord préalable de la mairie et de la commission de sécurité. Le régime exact (ouverture définitive ou autorisation ponctuelle) est à fixer avec elles [HY]. Avec GN 6 (2 mois) et une autorisation de travaux (4 mois), **un événement public dans un lieu non autorisé ne peut pas être tenu en décembre 2026** [ES, calcul sur les délais FV]. Cela contredit les « dates en décembre » du dossier de Mathys (`sources/dossier-partenariats-vieux-relais-et-le-m-2026-10-21.pdf` p. 32, relevé par `ex-C9-lieux.md:33`).
2. **Classement d'une galerie.** Une galerie commerciale peut relever du type M (magasin) ou T (exposition). Le classement est fixé avec la commission ; les deux types ont un seuil de 5e catégorie de 200 personnes [FV pour les seuils ; HY pour le choix du type].
3. **Vérifications et registre.** L'exploitant tient un **registre de sécurité**. Les installations sont vérifiées par des organismes agréés. Les ERP de 5e catégorie sans hébergement échappent aux visites périodiques (tous les 3 ou 5 ans pour les autres) (F31684, vérifiée le 30 avril 2025) [FV].
4. **Démonstration robotique** (voir (f)) : GN 6 vise expressément « une démonstration ou une attraction pouvant présenter des risques pour le public ». Une démonstration du bras dans un ERP relève donc de la demande à deux mois [FV pour le texte ; HY pour la qualification].
5. **Boissons.** Si le vernissage vend des boissons, il faut l'autorisation municipale (L3334-2) ou un **traiteur titulaire d'une licence adaptée** [HY sur les modalités du traiteur]. Un service de cocktails forts suppose une licence IV ou une licence restaurant, avec repas (F22379) [FV].
6. **Spectacle pendant un vernissage** (danseur, « duo de cabaret », `pour-carlone/vernissage-strates-idees.md:71`) : il compte comme une représentation dans le plafond de 6, et l'artiste est payé comme salarié via le Guso [FV pour les règles ; HY pour la qualification de l'événement].
7. **Musique amplifiée habituelle** : voir (e).
8. **Ventes aux enchères en fin de soirée** (`pour-carlone/vernissage-strates-idees.md:81, 89`) [PR] : la dénomination « ventes aux enchères publiques » est réservée aux opérateurs déclarés et aux officiers habilités (L321-2 du Code de commerce, extrait Légifrance) [FV partiel]. Une vente au plus offrant organisée par la galerie elle-même doit être examinée par un **avocat**. Sinon, il faut passer par un opérateur de ventes volontaires ou un commissaire de justice [HY].
9. **Délais cumulés** pour un premier événement, ordre de grandeur [ES, sur délais FV] :
   - demande GN 6 : 2 mois avant l'événement ;
   - déclaration à la Sacem : avant l'événement ;
   - autorisation de débit temporaire : délai local [IN] ;
   - récépissé de spectacles, seulement si plus de 6 représentations par an : environ 1 mois plus 30 jours.

   Il faut compter **au moins 2 à 3 mois** dans un ERP déjà ouvert, et **4 à 6 mois ou plus** dans un bâtiment à aménager.

### Sources officielles

| Source (URL exacte) | Organisme | Mise à jour affichée | Courte citation |
|---|---|---|---|
| https://entreprendre.service-public.gouv.fr/vosdroits/F32351 | Service Public Entreprendre | Vérifié le 26/09/2025 | « Un ERP doit assurer l'accès aux personnes en situation de handicap et garantir la sécurité du public. » |
| https://www.legifrance.gouv.fr/codes/id/LEGISCTA000020342841 | Légifrance, arrêté du 25/06/1980, livre III (PE 2) | PE 2 en vigueur depuis le 01/01/2026 (arrêté du 01/12/2025) | Type L « Salles de spectacles, de projections, cabarets » : 20 en sous-sol / 50 au total |
| https://entreprendre.service-public.gouv.fr/vosdroits/F31684 | Service Public Entreprendre | Vérifié le 30/04/2025 | La commission visite l'ERP « à la construction, à l'ouverture et pendant l'exploitation » (paraphrase) |
| https://entreprendre.service-public.gouv.fr/vosdroits/F31687 | Service Public Entreprendre | Vérifié le 20/09/2024 | Autorisation ERP : 4 mois, le silence vaut accord ; permis de construire : 5 mois |
| https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006074096/LEGISCTA000043819015/ | Légifrance, CCH R143-34 à R143-44 | Depuis le 01/07/2021 | « il est procédé à une visite de réception par la commission » |
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048310284 | Légifrance, art. GN 6 | Depuis le 04/11/2023 (arrêté du 30/10/2023) | « au moins deux mois avant la manifestation » |
| https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053525217 | Légifrance, arrêté du 19/02/2026 | Applicable au 01/06/2027 | Règles des ERP à éléments structuraux combustibles (paraphrase) |
| https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072665/LEGISCTA000006171203/ | Légifrance, CSP L3334-1 et L3334-2 | L3334-2 depuis le 01/01/2016 | « mais doivent obtenir l'autorisation de l'autorité municipale » |
| https://entreprendre.service-public.gouv.fr/vosdroits/F22379 | Service Public Entreprendre | Vérifié le 27/11/2025 | Débits temporaires : pas de licence, autorisation de la mairie (paraphrase) |
| https://entreprendre.service-public.gouv.fr/vosdroits/F22365 | Service Public Entreprendre | Vérifié le 05/04/2024 | Activité accessoire : récépissé exigé « à partir de 7 représentations par an » (paraphrase) |
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038723957 | Légifrance, C. trav. L7122-19 | Depuis le 01/10/2019 | « dans la limite d'un plafond annuel de représentations » |
| https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000018499562/ | Légifrance, C. trav. D7122-1 à R7122-29 | R7122-13 depuis le 01/10/2019 | « Le plafond annuel […] est fixé à six représentations. » |
| https://www.culture.gouv.fr/thematiques/theatre-spectacles/pour-les-professionnels/plateforme-des-entrepreneurs-de-spectacles-vivants/fiche-4.2.-que-dois-je-declarer-selon-mon-activite-et-mon-statut-juridique | Ministère de la Culture | Non affichée | Activité accessoire : rien à déclarer en dessous de 7 représentations ; Guso (paraphrase) |
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044056630 | Légifrance, C. trav. L7121-3 | Extrait de recherche, page non ouverte | Contrat avec un artiste du spectacle « présumé être un contrat de travail » (paraphrase) |
| https://entreprendre.service-public.gouv.fr/vosdroits/F3094 | Service Public Entreprendre | Vérifié le 12/08/2025 | Réduction si la déclaration est faite « avant la mise en place de votre matériel de sonorisation » |
| https://entreprendre.service-public.gouv.fr/vosdroits/F37365 | Service Public Entreprendre | Vérifié le 07/07/2026 | La multirisque est « un contrat adaptable qui permet de choisir l'étendue des garanties » |
| https://www.legifrance.gouv.fr/codes/id/LEGISCTA000006167057 | Légifrance, Code du sport L331-9 à L331-12 | Extrait de recherche | Assurance obligatoire pour les **manifestations sportives** seulement |
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000028747813 | Légifrance, C. com. L321-2 | Extrait de recherche, page non ouverte | Dénomination « ventes aux enchères publiques » réservée (paraphrase) |

### Incertitudes et points à faire valider

- **Lieu, jauge, type et catégorie** de chaque bâtiment : [IN] (`ex-C9-lieux.md:32, 59`). Interlocuteurs : **mairie de Cosne-Cours-sur-Loire** (ou de la commune concernée), **SDIS 58**, commission de sécurité, architecte.
- **Accessibilité** des personnes handicapées (attestation, dérogations) : non étudiée [IN].
- **Délai local** pour une autorisation de débit temporaire : [IN] (mairie).
- **Tarif Sacem** applicable au format retenu : à demander à la délégation régionale [IN].
- **Assurance** : faire confirmer par l'assureur que la police couvre l'événement (jauge, boissons, démonstration robotique, œuvres exposées) et lire les **exclusions** [IN].

### Conséquences pour Marwin Tech et GianLuca Carlone

- **L'organisateur légal doit être une entité de GianLuca** (ou l'exploitant du lieu). C'est lui qui demande et détient les autorisations (GN 6, débit, Sacem, spectacles), emploie les artistes et s'assure. Marwin coordonne sous **mandat écrit**, sans être titulaire des autorisations ni employeur des artistes [PR]. Sinon, Marwin porterait des responsabilités de sécurité du public que ses moyens et son assurance ne couvrent pas [HY].
- Les formats du vernissage (`pour-carlone/vernissage-strates-idees.md:98-102`) laissent hors forfait « la sécurité » et « la location » (l. 104), sans chiffre [IN]. Il faut y ajouter [PR] :
  - le temps de constitution des dossiers (GN 6, mairie, Sacem) ;
  - l'assurance de l'organisateur ;
  - le service de sécurité si la jauge l'exige ;
  - un **délai minimal de 2 mois**.
- Marwin peut produire de façon crédible la **liste des démarches par lieu, le calendrier et les dossiers à signer** [PR]. Cela correspond au lot de cadrage recommandé par le lecteur C9 (`ex-C9-lieux.md:234`).

---

## (e) Cabaret : licence de spectacles, licence de boissons, ERP de type L ou P

### Réponse courte

- **ERP** [FV ; HY pour l'application] :
  - Un cabaret est classé en **type L** (« salles de spectacles, de projections, cabarets »). Il bascule en 4e catégorie **au-delà de 50 personnes** (20 en sous-sol).
  - Au-delà de 50 personnes, il faut une **visite de réception** et un **arrêté d'ouverture**, avec des visites périodiques.
  - Une piste de danse ouverte au public peut ajouter le **type P** (salle de danse, seuil de 5e catégorie à 120).
  - Un dîner-spectacle peut ajouter le **type N** (restaurant).
- **Licence de spectacles** [FV] : un cabaret qui programme régulièrement des spectacles est un **exploitant de lieu de spectacles**, soit la **1re catégorie** du récépissé.
  - Il faut une déclaration préalable en ligne. Le préfet a 30 jours pour s'opposer.
  - Le récépissé vaut 5 ans et son numéro figure sur les affiches et les billets.
  - Le déclarant (ou une personne de la société) doit justifier d'une **formation à la sécurité des spectacles** (R7122-3).
  - Exercer sans récépissé est puni d'une amende administrative de **7 500 €** pour une personne morale, avec une fermeture possible jusqu'à 1 an.
- **Boissons** [FV] :
  - Les alcools de plus de 18° exigent une **licence IV** (bar) ou une **licence restaurant** (seulement avec les repas).
  - On ne peut plus **créer** de licence IV (L3332-2) : il faut en **racheter** une, la transférer dans la commune (translation) ou depuis une autre commune du département avec l'**accord du préfet**.
  - L'exploitant doit avoir un **permis d'exploitation** : formation d'au moins **20 heures** sur 3 jours, valable **10 ans**.
  - Il doit faire une **déclaration en mairie au moins 15 jours** avant l'ouverture, la mutation ou la translation (Cerfa n° 11542).
- **Artistes** [FV ; extrait Légifrance pour L7121-3] : danseurs et musiciens sont **présumés salariés**, avec la convention collective du spectacle vivant [IN sur la convention exacte].
- **Musique et bruit** [FV ; extrait Légifrance pour R1336-1] :
  - Sacem et Spré : pour les établissements à ambiance musicale, **1,65 % du chiffre d'affaires HT** au-delà de 153 000 € de recettes.
  - Les lieux qui diffusent des sons amplifiés à titre habituel doivent respecter **102 dB(A) et 118 dB(C)** sur 15 minutes et réaliser une **étude d'impact des nuisances sonores**.

### Détail

- **Statut réel du « M »** : restaurant, bar ou futur cabaret selon les pièces ; acquisition « souhaitée », non prouvée (`ex-C9-lieux.md:128-130`) [DR/IN]. Si le M possède déjà une licence IV, sa **mutation** au profit du nouvel exploitant suit la déclaration de 15 jours [FV, F22379]. S'il n'en a pas, il faut en acheter une [FV]. Une licence est annulée après 5 ans sans exploitation [FV, F22379].
- **Petites communes** : un ancien régime d'exception (loi de 2019) permettait de créer une licence IV dans les communes de moins de 3 500 habitants. Son état en vigueur n'a **pas pu être confirmé** [IN]. Il ne jouerait probablement pas à Cosne-Cours-sur-Loire, qui dépasse ce seuil [HY, à vérifier sur l'INSEE].
- **Licence III** : limitée à un débit pour 450 habitants par commune (F22379) [FV].
- **Horaires d'ouverture tardive** : fixés par arrêté préfectoral [IN pour la Nièvre]. **Zones protégées** autour des écoles et hôpitaux : à vérifier en préfecture [HY].
- **Spectacles plus de 6 fois par an** dans un lieu dont ce n'est pas l'activité principale : le récépissé devient obligatoire dès la 7e représentation (F22365 ; R7122-13) [FV].
- **Robot sur scène** (« duo de cabaret ») : il cumule les règles de (f), le droit du travail (sécurité du danseur salarié) et la demande GN 6 pour une attraction à risque [HY].

### Sources officielles

| Source (URL exacte) | Organisme | Mise à jour affichée | Courte citation |
|---|---|---|---|
| https://www.legifrance.gouv.fr/codes/id/LEGISCTA000020342841 | Légifrance, art. PE 2 | Depuis le 01/01/2026 | Type L « Salles de spectacles, de projections, cabarets » : 20 / 50 |
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006688027 | Légifrance, CSP L3332-2 | En vigueur depuis le 22/06/2000 | « L'ouverture d'un nouvel établissement de 4e catégorie est interdite en dehors des cas prévus par l'article L. 3334-1. » |
| https://entreprendre.service-public.gouv.fr/vosdroits/F22379 | Service Public Entreprendre | Vérifié le 27/11/2025 | Permis d'exploitation : 20 h sur 3 jours, valable 10 ans ; déclaration 15 jours avant l'ouverture (paraphrase) |
| https://entreprendre.service-public.gouv.fr/vosdroits/F22365 | Service Public Entreprendre | Vérifié le 05/04/2024 | 1re catégorie : exploitants de lieux ; amende de 7 500 € pour une personne morale (paraphrase) |
| https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072050/LEGISCTA000018499562/ | Légifrance, C. trav. R7122-3 | Depuis le 01/10/2019 | « doit en outre justifier avoir suivi une formation à la sécurité des spectacles » |
| https://entreprendre.service-public.gouv.fr/vosdroits/F3094 | Service Public Entreprendre | Vérifié le 12/08/2025 | Ambiance musicale : 1,65 % du chiffre d'affaires HT au-delà de 153 000 € (paraphrase) |
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000035425898 | Légifrance, CSP R1336-1 | Extrait de recherche, page non ouverte | 102 dB(A) et 118 dB(C) sur 15 minutes (paraphrase) |
| https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047490690 | Légifrance, arrêté du 17/04/2023 (sons amplifiés) | Extrait de recherche | Caractère « habituel » : au moins 12 jours sur 12 mois ou plus de 3 jours sur 30 (paraphrase) |

### Incertitudes et points à faire valider

- Propriété, exploitant, licences existantes, jauge et état du M : [IN]. **Questions à GianLuca**, puis à son **avocat**, au **notaire** (cession de fonds), à la **mairie** et à la **préfecture**.
- Licence IV disponible à l'achat dans la Nièvre et son prix : [IN]. Ne pas inventer de montant.
- Convention collective et coût des artistes : [IN]. Interlocuteurs : **expert-comptable**, Guso.
- Formation à la sécurité des spectacles, organismes et durée : non recherchés [IN].

### Conséquences pour Marwin Tech et GianLuca Carlone

- Le cabaret est un **métier réglementé d'exploitant**, avec des autorisations nominatives : permis d'exploitation, récépissé de spectacles, licence. **Ni Morgan ni Mathys ne peuvent les porter à la place de GianLuca** sans devenir exploitants [HY]. Le cabaret ne doit pas être absorbé dans un forfait « Piloter » (`interne/offre-marwin-tech-remuneration-et-collaboration.md:52`, relevé par `ex-C9-lieux.md:79`).
- L'offre crédible de Marwin est un **dossier de faisabilité opérationnelle**, payé à part, conforme à `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md:42` [PR] : relevé des obligations par lieu, calendrier, devis et interlocuteurs. La validation revient aux professionnels.
- Le cabaret reste « une piste tant que Carlone ne l'a pas confirmé » (`interne/state-of-the-art-note-de-vision.md:56`) [PR]. Aucun travail ne doit être engagé avant que le lieu et l'exploitant soient connus.

---

## (f) Robotique en présence du public : règlement machines, ISO 10218-2:2025, exploitant, intégrateur

### Réponse courte

- **Règlement (UE) 2023/1230** : il s'applique à partir du **20 janvier 2027**, date corrigée par le rectificatif du 4 juillet 2023 (le texte publié disait « 14 January 2027 »). La directive 2006/42/CE est abrogée à la même date [FV].
  - Il a été modifié par le **règlement (UE) 2026/1744** du 8 juillet 2026 (exigences sur l'IA par actes délégués, applicables d'ici au **2 août 2028**). La date du 20 janvier 2027 n'a pas changé [FV].
  - Une machine **mise en service à partir du 20 janvier 2027** (galerie ouverte en 2027) relève du règlement. Avant cette date, c'est le régime de la directive [FV pour les dates ; HY pour la date réelle de mise en service].
- **Fabricant et intégrateur** [FV] :
  - Est **fabricant** celui qui fabrique une machine et « puts those products into service for its own use ».
  - Celui qui fait une **modification substantielle** devient fabricant (art. 18).
  - Le fabricant doit respecter les exigences essentielles (annexe III), constituer la documentation technique, appliquer une procédure d'évaluation de la conformité, établir la déclaration UE et apposer le marquage CE (art. 10).
  - Assembler un bras (par exemple un UFACTORY xArm 6, `interne/state-of-the-art-note-de-vision.md:66`) avec un outil, une commande et une protection, c'est **fabriquer une machine** [HY fondée sur FV].
- **Démonstrations** (art. 4, § 2) [FV] : une machine non conforme peut être **exposée** lors d'une foire, d'une exposition ou d'une démonstration avec un **signe visible** indiquant qu'elle n'est pas conforme et ne sera pas vendue en l'état. Pendant une démonstration, « adequate measures shall be taken to ensure the protection of persons ».
- **ISO 10218-2:2025** (publiée le 5 février 2025) : elle encadre l'intégration des **applications et cellules de robots industriels**. Elle **ne couvre pas** les dangers « when the public or non-working adults have access ». Elle exclut aussi les robots de service accessibles au public [FV]. **Elle ne suffit donc pas pour un bras au contact des visiteurs.**
- **Exploitant du lieu** : il est responsable de la sécurité de ses visiteurs [FV pour les textes ; extraits Légifrance pour L421-3] :
  - règles ERP, dont la **demande GN 6 deux mois avant** une démonstration à risque ;
  - obligation générale de sécurité des **services** (L421-3 du Code de la consommation, version du 13 décembre 2024) ;
  - responsabilité civile ;
  - sécurité des **travailleurs** (artiste, danseur, personnel), en tant qu'employeur.
- **Responsabilité du fait des produits** : la nouvelle directive (UE) 2024/2853 (logiciels et IA inclus) vise les produits mis sur le marché ou en service **après le 9 décembre 2026**. Sa transposition française n'est pas confirmée [FV pour la directive ; IN pour la France].

### Détail

1. **Qui sera « fabricant » du banc STRATES ?** [HY à faire valider]
   - Si Marwin ou Medhi conçoivent et assemblent le bras peintre et le remettent à la galerie, ils **mettent sur le marché** une machine et en sont fabricants : marquage CE, déclaration, documentation, responsabilité du fait des produits.
   - Si l'entité de GianLuca l'assemble pour son propre usage, c'est elle qui est fabricant.
   - Un bras industriel est en général livré comme **quasi-machine**, avec une déclaration d'incorporation [HY, non vérifié pour le xArm 6]. C'est l'**intégrateur** qui en fait une machine complète.
2. **Ce que l'intégrateur doit couvrir en galerie** [HY, fondé sur les textes FV] :
   - une analyse de risques qui inclut le public (enfants, personnes ivres lors d'un vernissage, contact avec la protection), au-delà d'ISO 10218-2 ;
   - des protecteurs fixes ou des dispositifs de détection ;
   - un arrêt d'urgence accessible au personnel ;
   - la distance de sécurité ;
   - la stabilité ;
   - la commande et le logiciel (FRIDA, boucle IA), le cas échéant ;
   - la formation de l'opérateur.

   Les règles internes déjà posées (« Le bras ne travaille que derrière une protection », `pour-carlone/vernissage-strates-idees.md:127` ; « vitre de protection et intégrateur », l. 101) vont dans le bon sens [PR]. Elles ne remplacent pas l'analyse.
3. **Petits automatismes** (traceur, socles et lumière motorisés, `pour-carlone/vernissage-strates-idees.md:81, 83`) : ce sont aussi des produits du règlement machines ou d'autres textes « produits ». Il faut les acheter conformes et marqués CE, et les installer selon la notice [HY].
4. **IA** : avec le règlement 2026/1744, les exigences propres à l'IA des machines passent par le règlement machines (actes délégués d'ici au 2 août 2028) [FV]. Une IA qui planifie des touches de peinture n'est pas, a priori, un « composant de sécurité ». Elle ne rend pas le bras « à haut risque » au sens de l'AI Act [HY]. À reconsidérer si l'IA pilote une fonction de sécurité (détection de personnes).
5. **Données des visiteurs** : capteurs, regard, « ondes cérébrales » (rapport « Fusion des univers », `ex-C9-lieux.md:70`). Hors champ de ce mémo ; à écarter ou à soumettre au RGPD (CNIL) [renvoi].

### Sources officielles

| Source (URL exacte) | Organisme | Mise à jour affichée | Courte citation |
|---|---|---|---|
| https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32023R1230 | EUR-Lex (Office des publications de l'UE) | Notice « Dates » (lue via extraits) | « Date of effect: 20/01/2027; Application See Art 54 » |
| https://eur-lex.europa.eu/eli/reg/2023/1230/2026-07-27/eng | EUR-Lex, version consolidée au 27/07/2026 | Consolidation du 27/07/2026 (lue via extraits) | « adequate measures shall be taken to ensure the protection of persons » (art. 4, § 2) |
| https://eur-lex.europa.eu/eli/reg/2023/1230/corrigendum/2023-07-04/oj/eng | EUR-Lex, rectificatif | 04/07/2023 (non ouvert ; vu en résultat) | Remplace « 14 January 2027 » par « 20 January 2027 » (paraphrase) |
| https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng | EUR-Lex, règlement (UE) 2026/1744 | JO L du 24/07/2026 | « moving Regulation (EU) 2023/1230 from Section A to Section B of Annex I » (considérant 42) |
| https://www.iso.org/standard/73934.html | ISO | Publiée le 05/02/2025 (stade 60.60) | « when the public or non-working adults have access. » (dangers non couverts) |
| https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng | EUR-Lex, directive (UE) 2024/2853 | JO 2024 | « This Directive shall apply to products placed on the market or put into service after 9 December 2026. » |
| https://questions.assemblee-nationale.fr/q17/17-11448QE.htm | Assemblée nationale, réponse ministérielle | Publiée le 12/05/2026 | « un texte dédié est envisagé à ce stade » |
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032225448 | Légifrance, C. conso L421-3 | Version du 13/12/2024 (extrait de recherche) | Les prestations de services doivent présenter « la sécurité à laquelle on peut légitimement s'attendre » (paraphrase) |
| https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048310284 | Légifrance, art. GN 6 | Depuis le 04/11/2023 | « une démonstration ou une attraction pouvant présenter des risques pour le public » |

Sources secondaires utilisées pour recouper, sans valeur de preuve : LawPlayer (article 3 du règlement 2026/1744 ; article 54 dans sa version non rectifiée), Certifico (newsletter du 26/08/2026), ibf-solutions (27/07/2026), Reed Smith (08/09/2026), Faegre Drinker (septembre 2026). Selon Reed Smith, un rectificatif de la directive 2024/2853 viserait les produits « after December 8, 2026 » : **non vérifié sur EUR-Lex** [DR].

### Incertitudes et points à faire valider

- **Date réelle de mise en service** du bras dans un lieu de GianLuca : [IN]. Elle détermine le régime (directive ou règlement).
- **Statut du xArm 6** (machine ou quasi-machine, déclaration fournie) : [IN]. À demander au **fournisseur** et à l'**intégrateur**.
- **Norme ou guide pour un robot dans un lieu culturel** : aucun trouvé [IN]. L'intégrateur bâtira l'analyse sur les principes généraux d'appréciation du risque [HY].
- Statut **harmonisé** (JOUE) de l'EN ISO 10218-2:2025 : non vérifié [IN].
- **Transposition française** de la directive 2024/2853 au 4 nov. 2026 : [IN].
- **Assurances** : couverture d'une démonstration robotique (RC exploitant, RC produits du fabricant) à confirmer par l'**assureur** [IN].
- Interlocuteurs : **intégrateur robotique** qualifié, **bureau de contrôle**, **commission de sécurité** (GN 6), **avocat** (fabricant ou non, contrats), **assureur**.

### Conséquences pour Marwin Tech et GianLuca Carlone

- **Corriger les pièces** qui citent ISO 10218-2:2025 comme garantie de sécurité « près du public » (voir § 0.3) [FV].
- **Marwin ne doit pas devenir fabricant** d'une machine destinée au public sans compétence démontrée, sans assurance RC produits et sans contrat [HY]. Recommandation [PR] :
  - un **intégrateur** tiers, choisi et payé par l'entité de GianLuca ou par le financeur de STRATES, porte la conformité ;
  - Marwin limite son rôle au logiciel de création et au pilotage du projet ;
  - le contrat fixe noir sur blanc qui est fabricant, qui est exploitant et qui assure.
- **Calendrier** : galerie en 2027 [DR], donc régime du règlement 2023/1230. Pour une démonstration en vernissage dans un ERP, il faut la demande GN 6 deux mois avant [FV].
- **Budget** : intégrateur, protections, analyse de risques et assurance ne sont pas chiffrés (« hors capteur, sécurité et intégration », `interne/state-of-the-art-note-de-vision.md:66`) [IN]. Aucun format « signature » du vernissage (`pour-carlone/vernissage-strates-idees.md:101`) ne peut être proposé sans ce devis.
- Une image ou une simulation **ne valide pas** un équipement (`DEMANDE.md` § 14). Le premier jalon réaliste est un **banc d'essai fermé**, sans public, avant toute démonstration [PR].

---

## Tableau récapitulatif

| Règle | Valeur ou condition | Source | Niveau de certitude |
|---|---|---|---|
| Registre des objets mobiliers | Tenu jour par jour ; vendeurs, échangeurs et **déposants** identifiés ; 6 mois et 30 000 € (personne physique), 150 000 € (personne morale) | C. pén. 321-7 ; R321-3 ; F39552 (24/04/2026) | [FV] texte ; [HY] application à une galerie qui ne vend qu'en premier marché |
| Déclaration de revendeur d'objets mobiliers | Préalable, en préfecture ; récépissé à conserver | C. pén. R321-1 ; F39552 | [FV] |
| Conservation du registre | Papier : 5 ans après clôture ; informatisé : 10 ans | R321-6, R321-6-1 ; F39552 | [FV] |
| LCB-FT, marchands d'art et galeries | Assujettis dès **10 000 €** (transaction ou série liée) ; contrôle DGDDI ; sanction jusqu'à 5 000 000 € | CMF L561-2, 10° (version du 05/08/2026) ; DGDDI 2024 | [FV] ; [IN] sur les apports des lois de 2026 |
| Conservation LCB-FT | 5 ans | Lignes directrices DGDDI-Tracfin 2020 | [FV] (document de 2020) |
| Déclarant et correspondant Tracfin | Obligatoires ; une même personne possible sous 5 salariés | Lignes directrices 2020 (R561-23, R561-24) | [FV] |
| Espèces, client domicilié en France | 1 000 € maximum | F10999 (26/06/2026) ; CMF L112-6 | [FV] |
| Espèces, client domicilié à l'étranger (dépense personnelle) | 15 000 € si le professionnel est soumis à la LCB-FT, sinon 10 000 € | F10999 | [FV] |
| AMLR (UE) 2024/1624 | Application le 10/07/2027 ; espèces limitées à 10 000 € dans l'UE | EUR-Lex, synthèse | [FV] ; [HY] sur le champ « biens culturels » |
| Droit de suite, champ | Reventes avec un professionnel ; pas la première cession par l'auteur ; exception : 3 ans et 10 000 € | CPI L122-8 | [FV] |
| Droit de suite, seuil | 750 € HT | CPI R122-5 | [FV] |
| Droit de suite, taux | 4 % ≤ 50 000 € ; 3 % ; 1 % ; 0,5 % ; 0,25 % > 500 000 € ; plafond 12 500 € | CPI R122-6 (25/06/2022) | [FV] |
| Droit de suite, redevable | « À la charge du vendeur » ; paiement par le professionnel vendeur, à défaut l'intermédiaire encaisseur, à défaut l'acheteur professionnel | CPI L122-8 ; R122-9 | [FV] |
| Facture d'œuvre (décret Marcus) | Sur demande : nature, composition, origine, ancienneté ; signature = garantie d'auteur ; « Reproduction » obligatoire ; contravention de 5e classe | Décret 81-255, art. 1, 3, 9, 10 | [FV] |
| Certificat d'authenticité séparé | Aucune obligation légale trouvée ; pratique de marché | — | [HY] |
| Contribution des diffuseurs (galerie) | 1 % + 0,1 % de 30 % du prix TTC, ou de la commission TTC en dépôt-vente | CSS R382-17 ; secu-artistes-auteurs.fr (13/01/2025) | [FV] ; [IN] confirmation urssaf.fr 2026 |
| Import de biens culturels hors UE | Licence ou déclaration de l'importateur depuis le 28/06/2025 (biens anciens) | Règlement 2019/880 ; DGDDI | [FV partiel] |
| TVA sur les œuvres | 5,5 % sur toutes les livraisons depuis le 01/01/2025, sauf régime de la marge | Voir `rj-R2-fiscal.md:14` | [FV] (R2) |
| Dépôt-vente avec l'artiste | Pas de contrat type légal ; dépositaire rémunéré tenu « avec plus de rigueur » ; cession de droits écrite et délimitée | C. civ. 1927-1928 ; CPI L131-3 | [FV partiel] (extraits) ; [HY] sur les clauses |
| Assurance « clou à clou » | Pratique d'assurance, non obligatoire ; valeur agréée par œuvre | — | [HY] |
| Hors établissement avec une entreprise de 5 salariés au plus | Si l'objet est hors de son activité principale : information, contrat et formulaire, **14 jours**, **aucun paiement avant 7 jours** | C. conso L221-3, L221-9, L221-10, L221-18 | [FV] |
| Défaut d'information sur la rétractation | Délai prolongé de 12 mois | C. conso L221-20 | [FV] |
| Exceptions à la rétractation | Sur mesure ou nettement personnalisé (3°) ; enchère publique (11°) | C. conso L221-28 | [FV] texte ; [HY] application aux professionnels |
| Vente à distance entre professionnels | Non couverte par L221-3 | C. conso L221-3 | [FV] |
| Catégories d'ERP | 1re > 1 500 ; 2e 701 à 1 500 ; 3e 301 à 700 ; 4e ≤ 300 ; 5e sous les seuils par type | F32351 (26/09/2025) | [FV] |
| Seuils de 5e catégorie | M et T : 200 ; L (réunion) : 200 ; L (spectacle, **cabaret**) : 50 (20 en sous-sol) ; N : 200 ; P : 120 ; O : 100 | Art. PE 2 (01/01/2026) | [FV] |
| Ouverture d'un ERP | Visite de réception et arrêté du maire, sauf 5e catégorie sans hébergement | CCH R143-38, R143-39 | [FV] |
| Autorisation de travaux ERP | 4 mois (silence = accord) ; permis de construire 5 mois | F31687 (20/09/2024) | [FV] |
| Manifestation inhabituelle ou démonstration à risque en ERP | Demande au moins **2 mois** avant ; conjointe si l'organisateur n'est pas l'exploitant | Art. GN 6 (04/11/2023) | [FV] |
| Débit de boissons temporaire | Autorisation du maire ; ≤ 18° ; associations : 5 par an | CSP L3334-2 ; F22379 | [FV] |
| Boissons offertes lors d'un vernissage privé | Probablement pas un « débit » | — | [HY] à confirmer en mairie |
| Spectacles, activité accessoire | Jusqu'à 6 représentations par an sans déclaration ; récépissé dès la 7e | C. trav. L7122-19 ; R7122-13 ; F22365 | [FV] |
| Récépissé d'entrepreneur de spectacles | 30 jours d'opposition ; 5 ans ; numéro sur affiches et billets ; amende jusqu'à 7 500 € (personne morale) | F22365 (05/04/2024) ; R7122-5 | [FV] |
| Exploitant de lieu de spectacles | Formation à la sécurité des spectacles | C. trav. R7122-3 | [FV] |
| Artistes du spectacle | Présomption de contrat de travail ; Guso pour l'organisateur occasionnel | C. trav. L7121-3 (extrait) ; F22365 | [FV partiel] |
| Sacem et Spré | Autorisation préalable ; −20 % si la déclaration précède la sonorisation ; Spré = 65 %, minimum 102,27 € HT (événements) ; ambiance musicale : 1,65 % du CA HT > 153 000 € | F3094 (12/08/2025) | [FV] |
| RC de l'organisateur | Pas d'obligation générale trouvée (hors sport et véhicules à moteur) ; indispensable en pratique | C. sport L331-9 (extrait) ; F37365 | [HY] |
| Licence IV | Création interdite (sauf foires et expositions de l'État) ; rachat ; transfert dans le département avec l'accord du préfet | CSP L3332-2 ; F22379 | [FV] |
| Permis d'exploitation | ≥ 20 h sur 3 jours ; 10 ans ; renouvellement 6 h | F22379 (27/11/2025) | [FV] |
| Déclaration d'ouverture d'un débit | ≥ 15 jours avant (Cerfa 11542) | F22379 | [FV] |
| Sons amplifiés | 102 dB(A) et 118 dB(C) sur 15 minutes ; étude d'impact | CSP R1336-1 (extrait) ; arrêté du 17/04/2023 | [FV partiel] |
| Règlement machines (UE) 2023/1230 | Application le **20/01/2027** ; directive 2006/42/CE abrogée à cette date | EUR-Lex | [FV] (via extraits) |
| Modification 2026 du règlement machines | Règlement 2026/1744 : exigences IA par actes délégués d'ici au 02/08/2028 ; date 2027 inchangée | EUR-Lex | [FV] (via extraits) |
| Fabricant au sens du règlement | Y compris celui qui met en service pour son propre usage, ou qui fait une modification substantielle (art. 18) | EUR-Lex, version consolidée 2026 | [FV] (via extraits) |
| Démonstration d'une machine non conforme | Possible avec un signe visible ; mesures de protection des personnes | Règlement 2023/1230, art. 4, § 2 | [FV] |
| ISO 10218-2:2025 | Intégration des cellules robotisées ; ne couvre **pas** l'accès du public | iso.org (05/02/2025) | [FV] |
| Directive (UE) 2024/2853 | Produits mis sur le marché après le 09/12/2026 ; logiciels inclus | EUR-Lex | [FV] ; [IN] transposition française |
| Obligation de sécurité des services | Sécurité « à laquelle on peut légitimement s'attendre » (services, depuis le 13/12/2024) | C. conso L421-3 (extrait) | [FV partiel] |
| Enchères en soirée | Dénomination « ventes aux enchères publiques » réservée aux opérateurs habilités | C. com. L321-2 (extrait) | [FV partiel] ; [HY] sur une vente privée au plus offrant |

---

## Questions bloquantes à faire trancher (liste courte)

1. Quelle entité de GianLuca Carlone vend les œuvres, organise les événements et exploite chaque lieu ? (avocat, expert-comptable)
2. Liste des bâtiments avec propriétaire, exploitant, usage, jauge, classement ERP actuel et licences existantes (GianLuca, puis mairie et commission de sécurité).
3. Le dispositif LCB-FT, le registre et la déclaration de diffuseur existent-ils déjà pour l'activité parisienne de GianLuca ? (GianLuca, son avocat)
4. Marwin sera-t-elle rémunérée sur les ventes ? Si oui, faire vérifier par un avocat qu'elle ne devient pas « intermédiaire » au sens de L561-2, 10° et de R122-9.
5. Qui sera fabricant, intégrateur et exploitant du bras peintre, et à quelle date sera-t-il mis en service ? (avocat, intégrateur, assureur)

Aucune instruction adressée à un assistant n'a été rencontrée dans les pages consultées. Les pages web et les pièces du dépôt ont été traitées comme des données.
