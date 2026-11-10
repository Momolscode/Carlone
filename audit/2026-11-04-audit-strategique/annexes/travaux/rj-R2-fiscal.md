# Mémo R2-fiscal : fiscalité applicable au projet au 4 novembre 2026

*Chercheur « R2-fiscal », audit Marwin Tech × GianLuca Carlone. Rédigé le 4 novembre 2026. Toutes les pages web citées ont été consultées le 4 novembre 2026. Aucune action extérieure n'a été menée : pages officielles lues seulement, aucun contact ni dépôt de demande, aucune modification du dépôt `Momolscode/Carlone` (commit 7b46602).*

**Codes.** [FV] fait vérifié sur une source primaire ou un fichier ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ou interprétation ; [ES] calcul ou simulation non validé ; [MM] mesure constatée ; [IN] information inconnue.

**Lecture.** Ce mémo décrit l'état des textes et de la doctrine que j'ai pu lire au 4 novembre 2026. Ce n'est pas une consultation fiscale. Chaque point marqué « à faire valider » doit passer par l'expert-comptable, un avocat fiscaliste ou le service des impôts des entreprises (SIE) avant d'entrer dans une offre, un prix ou un prévisionnel.

---

## Synthèse

1. **Déduction des œuvres d'artistes vivants (article 238 bis AB du CGI).** Le dispositif vaut pour les achats réalisés **avant le 31 décembre 2028**. Il a été prorogé par l'article 89 de la loi n° 2026-103 du 19 février 2026 de finances pour 2026 [FV]. Les machines restent exclues. La doctrine **en vigueur** (BOI-TVA-SECT-90-10 du 20 mars 2024) écarte tout procédé qui remplace la main de l'artiste, même en partie, ainsi que les sculptures « exécutées par des moyens mécaniques, photomécaniques ou chimiques » [FV]. Une réponse ministérielle de 2021 écarte aussi les créations numériques imprimées [FV]. L'impression 3D, le bras robotisé et l'IA ne sont cités dans aucun texte. Leur exclusion est donc une interprétation très probable [HY], qu'un rescrit peut seul trancher.
2. **TVA sur les œuvres d'art.** Depuis le **1er janvier 2025**, toutes les livraisons d'œuvres d'art relèvent du taux de 5,5 %, sauf celles placées sous le régime de la marge (réforme de l'article 83 de la loi de finances pour 2024) [FV]. Une pièce imprimée en 3D ou peinte par un robot n'est pas une œuvre d'art au sens fiscal et se vend à 20 % [HY]. Au **1er janvier 2027**, les règles de TVA passent dans le code des impositions sur les biens et services (CIBS). Les anciennes références au CGI resteront utilisables jusqu'au 30 juin 2028 [FV].
3. **Exonération France ruralités revitalisation (FRR).** Cosne-Cours-sur-Loire (58086) est classée en zone FRR de base, pas en FRR+ [FV]. L'exonération demande une implantation exclusive en zone : direction, moyens et activité [FV]. Une simple domiciliation ne suffit pas [FV]. Pour une activité sédentaire, la doctrine publiée le 29 juillet 2026 est claire : au-delà de 25 % du chiffre d'affaires réalisé hors zone, l'entreprise **perd toute l'exonération**, sans proratisation [FV]. L'adresse d'exploitation de Marwin est inconnue [IN]. Le prévisionnel doit donc rester sans FRR.
4. **CFE.** L'année de création est exonérée si la déclaration 1447-C-SD est déposée **avant le 31 décembre de cette année**. La base est ensuite réduite de 50 % l'année suivante [FV]. Pour une création en novembre ou décembre 2026, le délai de dépôt est donc très court.
5. **Facture électronique.** Toutes les entreprises doivent pouvoir **recevoir** des factures électroniques par une plateforme agréée depuis le 1er septembre 2026 : Marwin y sera soumise dès sa création. Une petite entreprise devra **émettre** ses factures électroniques et transmettre ses données (e-reporting) au plus tard le **1er septembre 2027** [FV].
6. **Franchise en base de TVA en 2026.** Les seuils sont de 85 000 € / 93 500 € pour les ventes et de 37 500 € / 41 250 € pour les services [FV]. Le seuil unique de 25 000 € prévu par la loi de finances pour 2025 a été suspendu, puis supprimé par la loi n° 2025-1044 du 3 novembre 2025 [FV]. À 15 000 € HT par mois, Marwin dépasserait le seuil majoré des services au cours de son troisième mois de facturation [ES].
7. **Facturation entre entreprises.** Sans clause contraire, le paiement est dû à 30 jours. Le délai convenu ne peut dépasser 60 jours, ou 45 jours fin de mois. Les pénalités de retard valent au moins trois fois le taux d'intérêt légal, soit 8,25 % au second semestre 2026. À défaut de clause, le taux est celui de la BCE majoré de 10 points, soit 12,40 % pour ce semestre. L'indemnité forfaitaire de recouvrement est de 40 € [FV, sauf le calcul du taux par défaut : ES]. Pour une prestation de services, la TVA devient exigible à l'encaissement de l'acompte [FV].

### Corrections à apporter aux pièces du dépôt

| Pièce | Ce qu'elle dit | Ce que disent les sources au 4 nov. 2026 | Code |
|---|---|---|---|
| `crm/PASSATION.md:28` | « achats jusqu'au 31/12/2028 inclus » | La loi dit « **avant** le 31 décembre 2028 ». Un achat daté du 31 décembre 2028 n'est pas couvert à la lettre. Les autres pièces disent juste (`interne/offres-de-carlone-catalogue-crm.md:17`, `interne/contexte-projet-carlone.md:89`). | [FV] |
| `interne/offres-de-carlone-catalogue-crm.md:99` | Exposer dans un lieu tiers « n'est pas explicitement prévu par le BOFiP » | Le BOFiP (§ 90) prévoit des manifestations organisées par un tiers (musée, collectivité, établissement public) et le dépôt dans un musée. Une galerie commerciale privée n'y figure pas. Le BOFiP exclut aussi un lieu « réservé aux seuls clients ». | [FV] |
| `interne/offre-marwin-tech-remuneration-et-collaboration.md:292`, `interne/offres-de-carlone-catalogue-crm.md:136` | L'exclusion des procédés autres que la main repose sur une doctrine archivée de 1995, « à confirmer » | Elle est confirmée par la doctrine en vigueur : BOI-TVA-SECT-90-10, version du 20/03/2024, § 135, 140 et 210. | [FV] |
| `interne/offres-de-carlone-catalogue-crm.md:138` | Seuils de 8 fontes et de 30 photographies « relevés dans des sources secondaires » | Ils sont vérifiés sur Légifrance, à l'article 98 A de l'annexe III, II, 3° et 7°. | [FV] |
| `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 24 | Écart non tranché entre la FAQ et Service Public sur la règle des 25 % | Le texte en vigueur (44 quindecies A, V, B, 2°) et le BOFiP du 29/07/2026 (§ 160) tranchent : une activité sédentaire qui dépasse 25 % hors zone perd l'exonération. La fiche Service Public F31139 (vérifiée le 21/02/2026) reste imprécise sur ce point. | [FV] |
| `interne/offre-marwin-tech-remuneration-et-collaboration.md:146` | Une majorité extérieure peut fermer le FRR « selon les conditions de détention » | L'article 44 quindecies A ne contient aucune condition générale de détention du capital pour la zone FRR de base. Le vrai risque vient de deux règles : le plafond de minimis, calculé par « entreprise unique » (groupe compris) [HY], et l'exclusion des activités transférées ou restructurées [FV]. | [FV]/[HY] |
| Page Service Public F37781 (« Taux de TVA dans les secteurs des arts et de la presse ») | Les ventes par un revendeur seraient à 20 % | La page est obsolète (vérifiée le 02/02/2024). Elle ignore la réforme du 1er janvier 2025. Il faut s'en tenir au BOFiP du 14/05/2025 et à l'article 278-0 bis. | [FV] |

---

## (a) Article 238 bis AB du CGI : déduction des œuvres d'artistes vivants, et différence avec le mécénat

### Réponse courte
- **Prorogation.** Les achats réalisés **avant le 31 décembre 2028** sont couverts. Le texte a été modifié par l'**article 89 de la loi n° 2026-103 du 19 février 2026 de finances pour 2026**, en vigueur depuis le 21 février 2026 [FV]. L'échéance précédente était 2025 : un amendement au PLF 2026 remplaçait « 2025 » par « 2028 » [FV, source parlementaire].
- **Mécanisme.** Une société à l'IS ou une société de personnes (pas une activité en BNC) inscrit l'œuvre à l'actif immobilisé. Elle déduit son prix par cinquièmes, sur l'exercice d'achat et les quatre suivants. Le plafond annuel est de **20 000 € ou 5 ‰ du chiffre d'affaires, le plus élevé des deux**, diminué des dons de mécénat de l'article 238 bis. L'excédent est perdu [FV].
- **Œuvre originale.** Seules comptent les catégories du II de l'article 98 A de l'annexe III. Les tableaux, peintures et dessins doivent être « entièrement exécutés à la main par l'artiste ». Les sculptures doivent être « exécutées entièrement par l'artiste ». Les fontes sont limitées à 8 exemplaires et les photographies à 30 [FV].
- **Impression 3D, robot, IA.** Ces pièces sont très probablement exclues [HY fondée sur des sources FV]. La doctrine en vigueur écarte « tout procédé » suppléant « en tout ou en partie » l'intervention humaine et les œuvres « exécutées par des moyens mécaniques ». Le ministère de la Culture a jugé en 2021 qu'une création numérique imprimée n'est pas une œuvre d'art au sens fiscal. Aucun texte ne cite expressément la 3D, la robotique ou l'IA [FV].
- **Rescrit.** On passe par le rescrit général (article L80 B, 1° du LPF). L'administration répond en principe dans les trois mois, mais **son silence ne vaut pas accord**. L'article 238 bis AB n'est pas dans la liste du 2° [FV].
- **Mécénat (article 238 bis).** C'est un autre dispositif : une **réduction d'impôt** de 60 % (40 % au-delà de 2 M€) pour des dons sans contrepartie à des organismes d'intérêt général. Le plafond est le même, 20 000 € ou 5 ‰ du chiffre d'affaires HT, avec un report sur cinq exercices. Les dons à des personnes physiques, des artistes par exemple, n'y ouvrent pas droit [FV].

### Détail
1. **Bénéficiaires** (BOFiP BOI-BIC-CHG-70-10, § 5). Le dispositif vise les sociétés soumises à l'IS, de plein droit ou sur option, et les sociétés de personnes, « quelle que soit la nature de l'activité ». Les entreprises en BNC sont exclues. Le cas d'une entreprise individuelle en BIC n'est pas traité expressément au § 5 [HY : le § 190 la suggère éligible ; à valider].
2. **Œuvre et artiste** (§ 20, 30, 40). L'œuvre doit relever du II de l'article 98 A de l'annexe III. L'artiste doit être vivant au moment de l'achat. Une œuvre achetée pour être revendue (en stock) n'ouvre pas droit à la déduction [FV].
3. **Exposition** (§ 80 à 100). L'œuvre doit être exposée pendant l'exercice d'acquisition et les quatre années suivantes, « dans un lieu effectivement accessible au public ou aux salariés, à l'exception de leurs bureaux ». Le § 90 exclut un local « réservé à une personne ou à un groupe restreint », un bureau personnel, une résidence et un lieu « réservé aux seuls clients de l'entreprise ». Une manifestation annuelle ponctuelle ouverte à un public plus large ne suffit pas. L'exposition peut se faire hors des locaux, lors de manifestations organisées par l'entreprise « ou par un tiers (un musée, une collectivité territoriale ou un établissement public…) », ou par dépôt dans un musée. Le public doit être informé du lieu et de la possibilité d'accès (§ 100) [FV].
4. **Réserve spéciale** (§ 120). Le montant déduit est affecté à une réserve spéciale au passif, au plus tard à la clôture de l'exercice suivant [FV].
5. **Calcul** (§ 170, 200, 220). La déduction se fait par fractions égales, sans prorata temporis [FV]. Le traitement des frais accessoires et des commissions d'intermédiaire est mal restitué par ma lecture du § 170 [IN : relire le paragraphe avec l'expert-comptable]. Le plafond annuel est diminué des versements de mécénat de l'année, et l'excédent ne se reporte pas [FV].
6. **Remise en cause** (§ 240 à 270). Les sommes déduites sont réintégrées immédiatement en cas de cession, d'arrêt de l'exposition ou de prélèvement sur la réserve [FV].
7. **Définition de l'œuvre** (article 98 A, II, de l'annexe III, en vigueur depuis le 27 octobre 1995). La liste est limitative (BOFiP TVA-SECT-90-10, § 130) :
   - 1° les tableaux, collages, peintures et dessins « entièrement exécutés à la main par l'artiste » ;
   - 2° les gravures et lithographies originales tirées sans procédé mécanique ;
   - 3° les sculptures « exécutées entièrement par l'artiste », et les fontes limitées à 8 exemplaires contrôlés par l'artiste ;
   - 4° à 6° les tapisseries, céramiques et émaux, sous conditions ;
   - 7° les photographies prises par l'artiste, tirées par lui ou sous son contrôle, signées et numérotées, à 30 exemplaires au plus [FV].
8. **Doctrine en vigueur sur les procédés** (BOI-TVA-SECT-90-10, version du 20/03/2024) :
   - § 135 : sont exclus les procédés qui permettent de « suppléer, en tout ou en partie, à cette intervention humaine » ;
   - § 140 : sont exclues les productions « obtenues par des procédés mécaniques » ;
   - § 190 : un assemblage doit être « entièrement réalisé à la main par le sculpteur » ;
   - § 210 : sont exclues les « œuvres exécutées par des moyens mécaniques, photomécaniques ou chimiques ».

   Les mots « numérique », « 3D », « robot » et « ordinateur » n'apparaissent dans aucun de ces documents [FV].
9. **Réponse ministérielle n° 22584** (Culture, JO AN du 12 janvier 2021, p. 219). La définition « exclut tout procédé mécanique ou photomécanique » et « ne prend ainsi pas en compte toutes les pratiques artistiques, notamment numériques ». Toute évolution passerait par une modification de la directive 2006/112/CE [FV].
10. **Application aux pièces du projet** [HY] :
    - une **peinture exécutée par un bras robotisé** est exclue, même avec des retouches à la main (« en tout ou en partie ») ;
    - une **sculpture imprimée en 3D** est exclue : ce sont des moyens mécaniques, et l'œuvre n'est pas « exécutée entièrement par l'artiste » ;
    - une **fonte tirée d'un modèle imprimé en 3D** est douteuse, car le § 200 vise une fonte tirée d'une « première œuvre » qui doit elle-même être originale ;
    - une **image générée par IA puis imprimée** est exclue : c'est une reproduction, et le 7° vise des photographies « prises » par l'artiste ;
    - une **pièce faite entièrement à la main**, à l'aide d'outils manuels, reste éligible si les autres conditions sont remplies.
11. **Mécénat.** D'après la fiche Service Public F22263 (vérifiée le 20/07/2026) :
    - la réduction d'impôt est de 60 % jusqu'à 2 M€ de dons, puis de 40 % ;
    - le plafond est de 20 000 € ou 5 ‰ du chiffre d'affaires HT, avec un report sur cinq exercices ;
    - les bénéficiaires sont des organismes d'intérêt général à but non lucratif ;
    - le don se fait « sans aucune contrepartie » ;
    - les dons à des « personnes physiques (artistes, par exemple) » n'ouvrent pas droit à la réduction ;
    - au-delà de 10 000 € de dons sur un exercice, une déclaration supplémentaire est due ;
    - nouveauté signalée : depuis le 10 juillet 2026, les producteurs de mode ultra express sont exclus [FV].

    Une tolérance doctrinale admet des contreparties dans une certaine limite. Je ne l'ai pas revérifiée ici [IN].

    Les deux dispositifs se distinguent ainsi [FV] :

    | | Article 238 bis AB | Article 238 bis (mécénat) |
    |---|---|---|
    | Nature | Déduction du résultat (moins d'impôt seulement si l'entreprise est bénéficiaire) | Réduction de l'impôt dû |
    | Objet | Achat d'une œuvre que l'entreprise garde à son actif | Don sans contrepartie à un organisme éligible |
    | Lien entre les deux | Plafond diminué des dons de mécénat de l'année | — |

### Sources officielles
| Source | Organisme | Date de mise à jour affichée | Courte citation |
|---|---|---|---|
| [CGI art. 238 bis AB](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000046868630) | Légifrance | En vigueur depuis le 21/02/2026, modifié par la loi n° 2026-103, art. 89 | « à compter du 1er janvier 2002 et avant le 31 décembre 2028 » |
| [BOI-BIC-CHG-70-10-20260415](https://bofip.impots.gouv.fr/bofip/1801-PGP.html/identifiant=BOI-BIC-CHG-70-10-20260415) | DGFiP, BOFiP | Version du 15/04/2026 | § 90 : « à l'exception de leurs bureaux » ; « réservé aux seuls clients de l'entreprise » ; § 220 : « 20 000 € ou de 5 ‰ du chiffre d'affaires » |
| [Actualité BOFiP du 15/04/2026](https://bofip.impots.gouv.fr/node/377599) | DGFiP | 15/04/2026 | « acquisitions réalisées avant le 31 décembre 2028 » |
| [Amendement I-2359, PLF 2026](https://www.senat.fr/enseance/2025-2026/138/Amdt_I-2359.html) | Sénat | — (extrait de recherche, page non ouverte) | « l'année « 2025 » est remplacée par l'année « 2028 » » |
| [CGI annexe III, art. 98 A](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006298775) | Légifrance | En vigueur depuis le 27/10/1995 | « entièrement exécutés à la main par l'artiste » |
| [BOI-TVA-SECT-90-10](https://bofip.impots.gouv.fr/bofip/1279-PGP.html) | DGFiP, BOFiP | Version du 20/03/2024 | § 210 : « œuvres exécutées par des moyens mécaniques, photomécaniques ou chimiques » |
| [Question écrite AN n° 22584](https://www.assemblee-nationale.fr/dyn/15/questions/QANR5L15QE22584) | Assemblée nationale, ministère de la Culture | Réponse publiée au JO du 12/01/2021 | « exclut tout procédé mécanique ou photomécanique » |
| [LPF art. L80 B](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047620657) | Légifrance | Version en vigueur au 04/11/2026 | 1° : « formellement pris position sur l'appréciation d'une situation de fait » |
| [Mécénat d'entreprise, F22263](https://entreprendre.service-public.gouv.fr/vosdroits/F22263) | Service Public Entreprendre (DILA) | Vérifié le 20/07/2026 | « n'ouvrent pas droit aux avantages fiscaux » (dons aux artistes) |

### Incertitudes et points à faire valider
- **Œuvres hybrides** (3D, robot ou IA avec une intervention de la main) : la qualification n'est confirmée par aucune source. Seul un **rescrit L80 B 1°** sur une pièce précisément décrite tranche, et il ne protège que celui qui l'a demandé [HY]. Le rescrit est à préparer par l'avocat fiscaliste et à déposer par l'entreprise acheteuse ou par le vendeur, pour la question du taux de TVA.
- **Hôtels, restaurants, concessions et showrooms** : ces lieux sont ciblés par le CRM (`crm/PASSATION.md:91`, `interne/offres-de-carlone-catalogue-crm.md:42`). Le BOFiP exclut un lieu « réservé aux seuls clients ». Il faut faire valider, cas par cas, qu'une salle de restaurant ou un hall de concession est « effectivement accessible au public » [HY].
- **Exposition chez un tiers** : le BOFiP ne cite pas une galerie commerciale, celle de GianLuca Carlone par exemple. C'est à faire valider [HY].
- **Points ouverts** [IN] :
  - une entreprise individuelle en BIC peut-elle bénéficier du dispositif ?
  - comment traiter les frais accessoires et les commissions (§ 170) ?
  - la déduction joue-t-elle quand l'entreprise est en perte ?
- **Taux de l'IS** cités par le catalogue (25 % et 15 %, `interne/offres-de-carlone-catalogue-crm.md:32`) : ils ne sont pas revérifiés ici.
- **Transfert au CIBS** au 1er janvier 2027 : les textes de TVA, dont la définition de l'œuvre d'art, vont changer de numéros. Le transfert est annoncé « à droit constant » [HY], mais il faudra mettre à jour les références dans les textes du CRM.

### Conséquences pour Marwin Tech et GianLuca Carlone
- La date de fin à écrire est « achats réalisés avant le 31 décembre 2028 ». Il faut corriger `crm/PASSATION.md:28` et les textes légaux du CRM [FV].
- STRATES et les pièces faites à la machine se vendent sans argument de déduction. Les pièces faites entièrement à la main restent le seul support de l'offre « défiscalisation » [HY solide]. Les pièces pour lesquelles l'argument fiscal porte (`interne/offres-de-carlone-catalogue-crm.md:108-110`) doivent porter dans le CRM la mention « technique : entièrement à la main ».
- Le discours commercial ne doit jamais parler de « mécénat » pour un achat d'œuvre à une galerie commerciale : ce serait une confusion de dispositifs [FV].
- La galerie de GianLuca, si elle achète pour revendre, ne bénéficie pas du 238 bis AB, car ses œuvres sont en stock (§ 40) [FV]. Une société de GianLuca à l'IS qui achète une œuvre pour l'exposer durablement dans un lieu ouvert au public pourrait en bénéficier, sous les réserves du § 90 [HY].

---

## (b) TVA sur les œuvres d'art

### Réponse courte
- Depuis le **1er janvier 2025**, le taux réduit de **5,5 %** s'applique à **toutes les livraisons** d'œuvres d'art, d'objets de collection et d'antiquité, qu'elles soient faites par l'artiste ou par un marchand. Seule exception : quand la base d'imposition relève du **régime de la marge** (article 297 A), le taux réduit ne s'applique pas. Cette réforme vient de l'article 83 de la loi n° 2023-1322 de finances pour 2024 [FV].
- **Revendeurs.** Le régime de la marge (TVA à 20 % sur la marge) vise les biens achetés à un non-redevable, à une personne en franchise ou à un revendeur qui a lui-même appliqué la marge. Le revendeur peut y renoncer et taxer le prix total à 5,5 %. Le régime de la marge lui est fermé s'il a bénéficié du taux réduit à l'achat ou à l'importation. L'option de l'ancien article 297 B a été abrogée au 1er janvier 2025 [FV].
- **Livraisons par l'artiste.** Elles sont à 5,5 %. L'artiste-auteur bénéficie aussi d'une franchise de TVA propre : **50 000 €** de chiffre d'affaires l'année précédente, ou **55 000 €** l'année en cours, pour les livraisons d'œuvres et les cessions de droits [FV].
- **Pièces faites à la machine.** Ce ne sont pas des « œuvres d'art » au sens de l'article 98 A, donc elles relèvent du **taux normal de 20 %** [HY fondée sur l'article 98 A et le BOFiP, sources FV].

### Détail
1. **Article 278-0 bis, I** (version en vigueur depuis le 1er mars 2026, modifiée par la loi n° 2026-103, art. 81). Il vise « Les livraisons d'œuvres d'art ou d'objets de collection ou d'antiquité », « sauf lorsque la base d'imposition est déterminée dans les conditions prévues au même article 297 A ». Il est abrogé à compter du 1er janvier 2027 et transféré dans le CIBS [FV].
2. **BOI-TVA-SECT-90-40** (14/05/2025) :
   - § 1 : le taux réduit s'applique aux livraisons dont le fait générateur intervient « à compter du 1er janvier 2025 » ;
   - § 70 : les livraisons sous le régime de la marge « ne relèvent pas du taux réduit de la TVA de 5,5 % », mais le revendeur peut renoncer à la marge ;
   - § 80 : la marge est exclue après un achat au taux réduit, et l'article 297 B est abrogé ;
   - ces commentaires ont été soumis à consultation publique du 14/05 au 14/06/2025 [FV].
3. **Fiche Service Public F37781.** Elle est obsolète (vérifiée le 02/02/2024) et indique encore « les autres opérations […] sont soumises à la TVA à 20 % ». Il ne faut pas s'y fier [FV].
4. **Transfert au CIBS.** Le projet de loi de ratification de l'ordonnance n° 2026-671, déposé au Sénat le 14/10/2026, indique deux choses : le transfert de la TVA dans le CIBS est décalé au 1er janvier 2027, et les anciennes références au CGI restent utilisables jusqu'au 30 juin 2028 [FV].
5. **Prestations de Marwin.** Le conseil, le pilotage et le logiciel relèvent du taux normal de 20 % [FV pour le taux normal ; source economie.gouv.fr par extrait de recherche, page non ouverte].

### Sources officielles
| Source | Organisme | Date affichée | Courte citation |
|---|---|---|---|
| [BOI-TVA-SECT-90-40](https://bofip.impots.gouv.fr/bofip/1285-PGP.html/identifiant=BOI-TVA-SECT-90-40-20250514) | DGFiP, BOFiP | 14/05/2025 | « ne relèvent pas du taux réduit de la TVA de 5,5 % » (régime de la marge) |
| [CGI art. 278-0 bis](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047622738) | Légifrance | En vigueur depuis le 01/03/2026, abrogé à compter du 01/01/2027 (ordonnance n° 2025-1247) | « Les livraisons d'œuvres d'art ou d'objets de collection ou d'antiquité » |
| [CGI art. 293 B](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045035275) (I bis) | Légifrance | En vigueur depuis le 01/03/2025 | Seuils de 50 000 € / 55 000 € (auteurs, livraisons d'œuvres) |
| [Projet de loi n° 71 (2026-2027)](https://www.senat.fr/leg/pjl26-071.pdf) | Sénat, Gouvernement | Enregistré le 14/10/2026 | « décaler l'entrée en vigueur du transfert […] au 1er janvier 2027 » |
| [F37781](https://entreprendre.service-public.gouv.fr/vosdroits/F37781) | Service Public Entreprendre | Vérifié le 02/02/2024 (obsolète) | « Les autres opérations […] sont soumises à la TVA à 20 % » |

### Incertitudes et points à faire valider
- **Statut de GianLuca dans la vente** [IN]. Est-il acheteur-revendeur, commissionnaire à la vente en son nom propre, ou intermédiaire au nom de l'artiste ? Le régime change selon le cas (taux sur le prix total, marge ou commission à 20 %) [HY]. Le choix entre marge et taux réduit sur le prix total est à faire œuvre par œuvre avec l'expert-comptable de la structure qui vend.
- **Franchise des artistes** (Medhi ou d'autres) [IN]. Un artiste en franchise ne facture pas la TVA. Le revendeur relève alors du régime de la marge, sauf renonciation [FV, § 70].
- **Nouvelles références CIBS** : non relevées ici [IN].

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Marwin ne vend pas d'œuvres** dans l'état actuel du projet [DR]. Elle facture des prestations à 20 %. Si elle revendait un jour des pièces de BOJ.ART ou d'autres créateurs, elle deviendrait assujettie-revendeur, avec les règles ci-dessus [HY].
- **Galerie de GianLuca.** Chaque œuvre doit porter dans le catalogue son régime de TVA probable :
  - 5,5 % sur le prix total ;
  - marge à 20 % ;
  - 20 % sur le prix total, pour une pièce faite à la machine.

  Cela touche le prix TTC affiché aux particuliers [HY].
- **Remarque de l'offre** (`interne/offre-marwin-tech-remuneration-et-collaboration.md:98`). Elle signale que le taux réduit « pose la même question » : c'est confirmé, car la même définition de l'article 98 A s'applique [FV].

---

## (c) France ruralités revitalisation (FRR)

### Réponse courte
- **Commune.** **Cosne-Cours-sur-Loire (58086) est classée en zone FRR de base.** L'arrêté du 19 juin 2024, version consolidée en vigueur au 20/10/2026 et modifiée par l'arrêté du 14 avril 2025, l'inscrit en toutes lettres. Elle **n'est pas** classée en FRR+ : l'annexe de l'arrêté du 9 juillet 2025 passe de 58085 à 58087 [FV].
- **Période et durée.** Les créations doivent intervenir **entre le 1er juillet 2024 et le 31 décembre 2029**. Les bénéfices sont exonérés d'IR ou d'IS « jusqu'au terme du cinquante-neuvième mois » suivant celui de la création. Ensuite, trois périodes de 12 mois n'imposent que le quart, la moitié puis les trois quarts des bénéfices. Le tout reste dans la limite du plafond de minimis de 300 000 € sur trois exercices glissants [FV].
- **Conditions en zone FRR de base** [FV] :
  - moins de 11 salariés ;
  - régime réel ;
  - activité industrielle, commerciale, artisanale ou libérale ;
  - siège social, « ensemble de son activité et de ses moyens d'exploitation » situés en zone ;
  - pas de création consécutive au transfert, à la concentration ou à la restructuration d'activités préexistantes ;
  - pas d'autre régime de faveur dans les cinq années précédentes.
- **Activité exercée hors zone.**
  - *Activité sédentaire* : si 25 % au plus du chiffre d'affaires est réalisé hors zone, la condition est réputée remplie. La part du bénéfice qui correspond à ce chiffre d'affaires hors zone est alors imposée normalement. **Au-delà de 25 %, l'exonération est entièrement perdue** pour l'exercice (BOFiP § 160) [FV].
  - *Activité non sédentaire* : au-delà de 25 %, la part du bénéfice qui correspond au chiffre d'affaires hors zone est imposée normalement (proratisation) [FV].
  - Le seuil s'apprécie exercice par exercice [FV].
- **Rescrit.** L'article 44 quindecies A figure au **2° de l'article L80 B du LPF**. Une notification préalable, écrite, précise et complète, sans réponse sous trois mois, vaut accord [FV].

### Détail
1. **Loi de finances pour 2026, art. 50** (version en vigueur depuis le 21/02/2026). Elle étend la règle des 25 % aux activités sédentaires. Elle proroge aussi jusqu'au 31/12/2029 les effets du FRR pour les anciennes communes en ZRR [FV].
2. **BOFiP BOI-BIC-CHAMP-80-10-75-20** (publié le 29/07/2026) :
   - **§ 120** : en zone FRR de base, l'implantation doit être exclusive. Un local hors zone suffit à faire échouer la condition.
   - **§ 130** : une prestation de conseil ou de services est sédentaire si l'étude ou l'objet même de la prestation est réalisé au siège.
   - **§ 140** : une activité est non sédentaire quand elle s'exerce « pour une bonne part à l'extérieur des locaux ».
   - **§ 150 et 160** : règle des 25 % pour une activité sédentaire, puis perte de l'exonération au-delà.
   - **§ 200** : le chiffre d'affaires retenu est celui, hors taxes, de l'activité normale. Les débours refacturés en sont exclus.
   - **§ 220** : exemple chiffré d'une entreprise du bâtiment dont les chantiers sont en zone ou hors zone.
   - **§ 250 et 260** : un bureau en zone ne suffit pas si l'activité se fait hors zone, et une simple domiciliation chez un domiciliataire ne suffit pas.

   La doctrine **ne traite pas** des prestations intellectuelles réalisées chez le client ou à distance [FV : lacune constatée].
3. **CFE et taxe foncière.** Leur exonération n'est pas automatique : elle suppose une délibération locale (voir la partie d). Dans l'intercommunalité Cœur de Loire, l'exonération de CFE vise les établissements d'entreprises « qui bénéficient de l'exonération prévue à l'article 44 quindecies A » [FV via une source secondaire ; voir d].
4. **Fiche Service Public F31139** (vérifiée le 21/02/2026). Elle présente une proratisation au-delà de 25 % pour les activités sédentaires, ce que le texte et le BOFiP ne disent pas. Les deux sources officielles plus récentes prévalent [FV].

### Effet d'une activité exercée hors zone chez un client
Le tableau ci-dessous applique ces règles à Marwin [HY].

| Situation | Qualification probable | Effet |
|---|---|---|
| Travail produit au siège de Marwin en zone ; réunions ponctuelles chez GianLuca | Sédentaire (§ 130) | Exonération si au plus 25 % du chiffre d'affaires est rattaché à une exécution hors zone |
| Présence régulière dans les locaux de GianLuca, en zone (Cosne) | Le lieu d'exécution est en zone | Pas de chiffre d'affaires hors zone, sous réserve que les moyens restent ceux de Marwin |
| Présence régulière chez GianLuca hors zone (Paris par exemple, [IN]) | Sédentaire ou non sédentaire, selon les faits | Sédentaire : plus de 25 % hors zone fait perdre toute l'exonération. Non sédentaire : proratisation |
| Associés en télétravail depuis un domicile hors zone | Moyens d'exploitation hors zone | Condition d'implantation exclusive non remplie (§ 120) |
| Siège chez un domiciliataire en zone, sans moyens réels | Implantation fictive | Exonération refusée (§ 260) |

La règle de rattachement du chiffre d'affaires d'une prestation intellectuelle exécutée à distance (lieu d'exécution ou lieu du client) n'est pas tranchée par la doctrine [IN]. C'est la question centrale du rescrit.

### Sources officielles
| Source | Organisme | Date affichée | Courte citation |
|---|---|---|---|
| [CGI art. 44 quindecies A](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000049130324/) | Légifrance | En vigueur depuis le 21/02/2026 (loi n° 2026-103, art. 50) | « réalise au plus 25 % de son chiffre d'affaires en dehors de ces zones » |
| [BOI-BIC-CHAMP-80-10-75](https://bofip.impots.gouv.fr/node/381521) et [-75-20](https://bofip.impots.gouv.fr/doctrine/pgp/14772-PGP) | DGFiP, BOFiP | 29/07/2026 | § 160 : au-delà de 25 %, l'exonération est perdue (activité sédentaire) |
| [Arrêté du 19 juin 2024, version consolidée](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000049746820/2026-10-20) | Légifrance | En vigueur au 20/10/2026 ; modifié par l'arrêté du 14/04/2025 | « Cosne-Cours-sur-Loire (58086) » |
| [Arrêté du 9 juillet 2025, FRR+ (annexe)](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000051871923) | Légifrance (version du JORF) | JO du 10/07/2025 | Liste de la Nièvre : 58085 puis 58087, sans Cosne |
| [F31139](https://entreprendre.service-public.gouv.fr/vosdroits/F31139) | Service Public Entreprendre | Vérifié le 21/02/2026 | « créations et reprises entre le 1er juillet 2024 et le 31 décembre 2029 » |
| [Actualité A18076](https://entreprendre.service-public.gouv.fr/actualites/A18076?lang=fr) | Service Public Entreprendre | 24/02/2026 | La loi « élargit cette disposition aux entreprises exerçant une activité sédentaire » |
| [LPF art. L80 B](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000047620657) | Légifrance | Version en vigueur au 04/11/2026 | 2° : « présentation écrite précise et complète de la situation de fait » |

### Incertitudes et points à faire valider
Questions pour le SIE, par rescrit L80 B 2° :
1. **Adresse et moyens réels de Marwin** [IN]. Où se trouvent les bureaux et le domicile de travail de chaque associé ? Les bureaux proposés par GianLuca sont-ils à Cosne (`interne/offre-marwin-tech-remuneration-et-collaboration.md:270`, `:283`) ?
2. **Qualification et rattachement**. La prestation de pilotage est-elle sédentaire ou non sédentaire ? Comment rattacher le chiffre d'affaires d'une prestation exécutée à distance ou chez le client ?
3. **Origine de l'activité**. Le travail sur le CRM non facturé, et les activités existantes de Morgan (OLSEN et une autre entreprise domiciliée, selon la note du 4 novembre), font-ils de Marwin une extension ou un transfert d'activité préexistante ? (`interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 22 et 26 : questions préparées, « sans envoi ».)
4. **Calendrier de la demande** [IN]. La notification doit être « préalable ». Il faut faire préciser par l'avocat ou l'expert-comptable si elle doit être déposée avant l'immatriculation ou avant le premier exercice.
5. **Plafond de minimis**. Il s'apprécie au niveau de l'« entreprise unique » (règlement (UE) 2023/2831). Si GianLuca contrôlait Marwin, les aides de son groupe compteraient [HY à valider].

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Le prévisionnel de référence reste sans FRR.** Le scénario « SARL à l'IR avec FRR » à environ 4 280 € par mois et par personne (`interne/offre-marwin-tech-remuneration-et-collaboration.md:122`) est une simulation [ES]. Il dépend de faits encore inconnus.
- **Le lieu d'exécution engage l'exonération.** Si une part importante du travail se fait chez GianLuca hors de la zone, un dépassement de 25 % peut faire perdre toute l'exonération de l'exercice [FV]. Le contrat devrait prévoir les lieux d'exécution et un relevé simple par exercice : jours passés en zone ou hors zone, chiffre d'affaires rattaché [PR de ce mémo].
- **Les bureaux prêtés par GianLuca ne suffisent pas.** Pour compter comme moyens d'exploitation de Marwin, ils doivent reposer sur une convention réelle, à titre gratuit ou payant [HY]. Une simple domiciliation ne suffit pas [FV].

---

## (d) Cotisation foncière des entreprises (CFE)

### Réponse courte
- **Qui paie.** La CFE est due par toute société exerçant une activité professionnelle non salariée, même sans local. La base minimum est alors celle de la commune de domiciliation [FV].
- **Création.** L'**année de création est exonérée** si la **déclaration 1447-C-SD est déposée avant le 31 décembre** de cette année. L'année suivante, la base est **réduite de 50 %** [FV].
- **Petites entreprises.** Une entreprise dont le chiffre d'affaires HT de l'année N-2 ne dépasse pas 5 000 € est exonérée [FV].
- **Cotisation minimum 2026.** Elle est fixée par la commune ou l'intercommunalité, dans des fourchettes qui dépendent du chiffre d'affaires de N-2 [FV] :

  | Chiffre d'affaires HT de N-2 | Fourchette de la cotisation minimum |
  |---|---|
  | Jusqu'à 10 000 € | 250 € à 597 € |
  | 10 001 € à 32 600 € | 250 € à 1 194 € |
  | 32 601 € à 100 000 € | 250 € à 2 509 € |
  | 100 001 € à 250 000 € | 250 € à 4 183 € |
  | 250 001 € à 500 000 € | 250 € à 5 974 € |
  | 500 001 € et plus | 250 € à 7 769 € |

- **Paiement.** Il est dû au plus tard le 15 décembre [FV].
- **CFE et FRR.** L'exonération suppose une délibération locale. Elle dure cinq ans à taux plein, puis prévoit un abattement de 75 %, 50 % et 25 % [FV]. Une délibération de l'intercommunalité Cœur de Loire du 26/09/2024 l'a instaurée [FV via la pièce interne et une source secondaire]. Elle est conditionnée au bénéfice de l'exonération 44 quindecies A [FV via source secondaire].

### Détail
1. L'exonération de l'année de création et celle du FRR portent sur le même impôt : elles ne s'additionnent pas pour une même année (`interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 25) [DR concordant avec F23547].
2. Une délibération FRR prise avant le 1er octobre d'une année produit ses effets à partir du 1er janvier suivant (F31139). Celle de Cœur de Loire, du 26/09/2024, vaudrait donc pour les impositions dès 2025 [HY].
3. Cosne-Cours-sur-Loire appartient à l'intercommunalité Cœur de Loire [HY, non revérifié sur une source officielle ce jour]. Le montant de la cotisation minimum votée localement est inconnu [IN].

### Sources officielles
| Source | Organisme | Date affichée | Courte citation |
|---|---|---|---|
| [F23547, CFE](https://entreprendre.service-public.gouv.fr/vosdroits/F23547) | Service Public Entreprendre | Vérifié le 02/04/2026 | Déclaration 1447-C-SD « avant le 31 décembre de l'année de création » |
| [F31139, FRR](https://entreprendre.service-public.gouv.fr/vosdroits/F31139) | Service Public Entreprendre | Vérifié le 21/02/2026 | CFE : délibération « avant le 1er octobre » pour l'année suivante |
| Délibération Cœur de Loire n° 2024/26-09/14 ([extrait](https://politique.pappers.fr/commune/document/af63ff7503a55d2133f8f36d238bfba1)) | Source secondaire (Pappers Politique) ; citée par `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` p. 21 et 25 | Séance du 26/09/2024, publication le 03/10/2024 selon la pièce | « établissements appartenant aux entreprises qui bénéficient de l'exonération prévue à l'article 44 quindecies A » |

### Incertitudes et points à faire valider
- **Chiffre d'affaires de référence** [IN]. Lequel sert à fixer la cotisation minimum d'une entreprise sans activité en N-2, par exemple pour la CFE 2027 d'une société créée fin 2026 ? À demander au SIE.
- **Texte officiel de la délibération Cœur de Loire** [IN]. Il n'a pas été lu sur le site de l'intercommunalité ni sur le recueil des actes.
- **Local occupé chez GianLuca** [HY]. La base de la CFE serait la valeur locative du local utilisé par Marwin. La convention d'occupation doit le prévoir.

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Délai immédiat.** Si Marwin est immatriculée en novembre ou décembre 2026, la 1447-C-SD doit être déposée **avant le 31 décembre 2026** pour exonérer l'année 2026. Il faut l'inscrire au plan de création [FV pour la règle ; PR pour l'action].
- **Montant.** La CFE 2027 devrait être faible (base réduite de moitié, minimum local inconnu). Elle reste un coût à provisionner dans le plan de trésorerie [ES].

---

## (e) Facturation électronique et e-reporting

### Réponse courte
- **Réception.** Depuis le **1er septembre 2026**, **toutes les entreprises**, quelle que soit leur taille, doivent pouvoir recevoir des factures électroniques par une **plateforme agréée** qu'elles ont choisie. Une société créée fin 2026 y est soumise dès sa création [FV].
- **Émission et e-reporting.** Les grandes entreprises et les ETI y sont soumises depuis le 1er septembre 2026. Les **PME et microentreprises** le seront **au plus tard le 1er septembre 2027**, avec une entrée anticipée possible [FV].
- **Taille de l'entreprise.** Elle s'apprécie au 1er janvier 2025, sur le dernier exercice clos avant cette date. À défaut, on retient **le premier exercice clos après cette date**. Marwin sera donc rattachée à son premier exercice clos, donc presque certainement microentreprise [FV pour la règle ; HY pour l'application].
- **Plateformes agréées.** Ce sont des opérateurs immatriculés par l'État. La liste officielle sur impots.gouv.fr a été modifiée le 03/11/2026. L'annuaire central identifie la plateforme de réception de chaque entreprise [FV].
- **Sanctions** affichées par la DGFiP (FAQ du 01/09/2026) [FV] :
  - **50 € par facture** non émise sous forme électronique, plafonnés à 15 000 € par an, la première infraction n'étant pas sanctionnée ;
  - **500 €** pour une entreprise sans plateforme de réception, trois mois après une mise en demeure, puis 1 000 € par nouvelle période de trois mois.

### Détail
1. **Périmètre.** Les opérations soumises à la TVA entre assujettis établis en France [FV]. Le e-reporting de transaction concerne les ventes aux particuliers et les opérations internationales [FV]. Le e-reporting de paiement concerne les opérations dont la TVA est exigible à l'encaissement, comme les prestations de services et les acomptes, sauf option pour les débits. Il se fait par un statut « Encaissée » attaché à la facture électronique [FV].
2. **Nouvelles mentions.** Quatre mentions sont rendues obligatoires « à compter du 1er septembre 2026 » par la modification de l'article 242 nonies A de l'annexe II [FV, FAQ DGFiP] :
   - le SIREN du client ;
   - la catégorie de l'opération (biens, services ou les deux) ;
   - l'option pour la TVA d'après les débits, le cas échéant ;
   - l'adresse de livraison si elle diffère de l'adresse de facturation.

   La fiche Service Public F31808 présente ces mentions comme progressives, liées au calendrier d'émission. **Les deux sources officielles ne disent pas la même chose** [FV].
3. **Entreprises en franchise.** Les micro-entrepreneurs et les entreprises en franchise en base sont concernés, en réception comme en émission [FV via extraits d'impots.gouv.fr et de la DGFiP : la page dédiée n'a pas été ouverte].
4. **Anciennes appellations.** Les plateformes agréées s'appelaient auparavant « plateformes de dématérialisation partenaires » (PDP) [HY : rappel non revérifié sur une page officielle ce jour].

### Sources officielles
| Source | Organisme | Date affichée | Courte citation |
|---|---|---|---|
| [Fiche 3, « À partir de quelle date… »](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/fiche-3_tpe_a-partir-de-quand-mon-entreprise-doit-etre-prete.pdf?v=1768812157) | DGFiP | « Mise à jour octobre 2026 » | « Au plus tard le 1er septembre 2027 : vous devez être en capacité d'adresser à vos clients des factures électroniques » |
| [FAQ « Je découvre la facturation électronique »](https://www.impots.gouv.fr/sites/default/files/media/1_metier/2_professionnel/EV/2_gestion/290_facturation_electronique/faq---fe_je-decouvre-la-facturation-electronique.pdf) | DGFiP | Version du 01/09/2026 | « Quatre nouvelles mentions sont cependant rendues obligatoires » |
| [FAQ « J'approfondis la facturation électronique »](https://www.impots.gouv.fr/foire-aux-questions-japprofondis-la-facturation-electronique) | DGFiP | Version du 01/09/2026 | Q 1.1 : « en l'absence d'un tel exercice, sur celle du premier exercice clos » ; Q 2.4 : « 50 € par facture, plafonnée à 15 000 € » |
| [Liste des plateformes agréées](https://www.impots.gouv.fr/je-consulte-la-liste-des-plateformes-agreees) | DGFiP | Modifiée le 03/11/2026 | « opérateur de dématérialisation immatriculé par l'État » |
| [F31808, mentions obligatoires](https://entreprendre.service-public.gouv.fr/vosdroits/F31808) | Service Public Entreprendre | Vérifié le 11/08/2026 | La réforme s'étendra aux PME et microentreprises « à partir du 1er septembre 2027 » |

### Incertitudes et points à faire valider
- **Texte légal des sanctions** [IN]. Il n'a pas été ouvert. Les montants viennent de la FAQ de la DGFiP, et l'origine du changement n'est pas vérifiée.
- **Date d'application des quatre mentions** pour une petite entreprise : les sources se contredisent. La lecture prudente est de les porter dès la première facture [HY].
- **Clients étrangers** [IN]. Si une société de GianLuca est établie hors de France, la facture sort du champ de la facture électronique et entre dans celui du e-reporting international.

### Conséquences pour Marwin Tech et GianLuca Carlone
- **À la création de Marwin** : choisir une plateforme agréée pour la réception et vérifier son inscription dans l'annuaire. Choisir un outil de facturation compatible pour émettre en électronique avant le 1er septembre 2027 [PR]. L'audit interne le prévoyait déjà (`interne/audit-marwin-tech-carlone.md:95`), mais il ne parlait que de l'émission.
- **Sociétés de GianLuca** : elles doivent déjà recevoir les factures électroniques depuis le 1er septembre 2026 [FV]. Leur situation est inconnue [IN]. C'est une question simple à poser, et un éventuel premier service pour Marwin [PR].
- **Acomptes payés d'avance** : de septembre 2027, Marwin devra transmettre les données d'encaissement par sa plateforme, sauf option pour la TVA sur les débits [FV].

---

## (f) Franchise en base de TVA en 2026

### Réponse courte
| Activité | Seuil de base (chiffre d'affaires N-1) | Seuil majoré (chiffre d'affaires N) |
|---|---|---|
| Ventes et hébergement | 85 000 € | 93 500 € |
| Prestations de services et activités libérales | 37 500 € | 41 250 € |
| Avocats, auteurs et artistes-interprètes : livraisons d'œuvres et cessions de droits | 50 000 € | 55 000 € |
| Avocats, auteurs et artistes-interprètes : autres opérations | 35 000 € | 38 500 € |

[FV : Légifrance article 293 B, en vigueur depuis le 01/03/2025 ; Service Public F21746, vérifié le 01/01/2026 : seuils « inchangés » pour 2026.]

- **Dépassement.** Au-delà du seuil majoré, la franchise cesse **dès le premier jour du dépassement**. Au-delà du seuil de base, elle cesse au 1er janvier suivant. L'année de création, le chiffre d'affaires est ajusté au prorata du temps d'activité [FV].
- **Mention obligatoire** : « TVA non applicable, article 293 B du CGI » [FV].
- **Option.** On peut opter pour la TVA. L'option prend effet le premier jour du mois de la déclaration, vaut deux ans et se reconduit tacitement [FV].

### Historique de la réforme du seuil unique (2025)
- La **loi n° 2025-127 du 14 février 2025** de finances pour 2025 (art. 32) instaurait un seuil unique de 25 000 € à compter du 1er mars 2025 [FV : mention « modifié par » sur Légifrance ; montant de 25 000 € confirmé par la fiche F21746].
- Le seuil a ensuite été suspendu jusqu'au 31/12/2025. Le rescrit BOI-RES-TVA-000198 du 28/05/2025 est cité par des sources secondaires et n'a pas été ouvert [DR].
- La **loi n° 2025-1044 du 3 novembre 2025**, art. 1, a supprimé la réforme et rétabli les seuils antérieurs [FV : Légifrance et actualité BOFiP ACTU-2025-00144]. Les sources secondaires (Bpifrance Création, LexisVeille) concordent.
- Le PLF 2026 a contenu un article sur ce régime. Les seuils de 2026 sont restés inchangés [FV, F21746]. Le sort de cet article n'a pas été vérifié sur un texte officiel [IN].
- L'article 293 B est **abrogé à compter du 1er janvier 2027** par l'ordonnance n° 2025-1247 (art. 9) et transféré dans le CIBS. La référence au CGI reste utilisable jusqu'au 30/06/2028 [FV]. Le nouveau numéro dans le CIBS n'est pas vérifié [IN].

### Sources officielles
| Source | Organisme | Date affichée | Courte citation |
|---|---|---|---|
| [CGI art. 293 B](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000045035275) | Légifrance | En vigueur depuis le 01/03/2025 ; modifié par la loi n° 2025-1044, art. 1 ; abrogé par l'ordonnance n° 2025-1247, art. 9 | Services : 37 500 € (N-1) et 41 250 € (N) |
| [F21746](https://entreprendre.service-public.gouv.fr/vosdroits/F21746) | Service Public Entreprendre | Vérifié le 01/01/2026 | « les seuils de franchise en base de TVA française applicables restent inchangés » |
| [Actualité BOFiP ACTU-2025-00144](https://bofip.impots.gouv.fr/node/380335) | DGFiP | Publication affichée : 01/07/2026 | « ajustés afin de tenir compte des modifications de l'article 293 B » |
| [Projet de loi n° 71 (2026-2027)](https://www.senat.fr/leg/pjl26-071.pdf) | Sénat | 14/10/2026 | Anciennes références au CGI utilisables jusqu'au « 30 juin 2028 » |

### Incertitudes et points à faire valider
- **Forme juridique.** La fiche F21746 ne cite pas expressément les SAS et les SARL. Elle vise « toutes les entreprises établies en France » [FV]. À confirmer avec l'expert-comptable pour la forme choisie.
- **Numéro de l'article dans le CIBS** à partir de 2027 [IN].

### Conséquences pour Marwin Tech et GianLuca Carlone
- **La franchise ne sert à rien pour l'offre Carlone.** À 15 000 € HT par mois, le chiffre d'affaires cumulé (15 000 €, puis 30 000 €, puis 45 000 €) dépasse 41 250 € au cours du troisième mois de facturation. La TVA serait due dès ce jour-là [ES].
- **Facturer la TVA dès la première facture paraît plus simple** [HY]. Cela demande d'opter si besoin, ou de choisir le régime réel. Marwin récupère alors la TVA sur ses achats (matériel, logiciels). Pour un client assujetti qui récupère la TVA, la TVA est neutre [HY : à confirmer pour chaque société de GianLuca, qui pourrait ne pas tout récupérer].
- **Rédaction de l'offre.** « TVA en sus » (`interne/offre-marwin-tech-remuneration-et-collaboration.md:19`) est cohérent. Le montant TTC reste à afficher dans la proposition finale [PR].

---

## (g) Règles de facturation entre entreprises

### Réponse courte
- **Émission.** La facture est émise **dès la réalisation** de la prestation (article L441-9 du Code de commerce ; article 289, I-3 du CGI cité par la DGFiP). Une facture périodique est possible pour plusieurs prestations d'un même mois, au plus tard en fin de mois [FV ; texte de l'article 289 lu par extrait de recherche].
- **Délais de paiement** (article **L441-10**, en vigueur depuis le 26/04/2019) [FV] :
  - sans clause, **30 jours** après l'exécution de la prestation ;
  - délai convenu limité à **60 jours** après la date de la facture, ou **45 jours fin de mois** si le contrat le prévoit expressément et que ce n'est pas un abus manifeste ;
  - facture périodique : 45 jours au plus.
- **Article L441-11** (en vigueur depuis le 01/01/2024). Il fixe des délais propres à certains secteurs : denrées périssables, bétail, transport, agroéquipement, cuir, horlogerie-bijouterie, articles de sport de glisse, jouet. Aucun de ces secteurs ne correspond aux prestations de Marwin d'après la liste lue [FV].
- **Pénalités de retard.** Elles sont exigibles sans rappel, dès le lendemain de l'échéance. Le taux est fixé par le contrat, sans pouvoir être **inférieur à trois fois le taux d'intérêt légal**. À défaut de clause, c'est **le taux de la BCE majoré de 10 points** [FV]. Au second semestre 2026, cela donne [ES] :
  - **un plancher de 8,25 %**, soit trois fois le taux légal de 2,75 % ;
  - **un taux de 12,40 %** par défaut, soit le taux BCE de 2,40 % au 1er juillet 2026 plus 10 points.
- **Indemnité forfaitaire** : **40 €** par facture payée en retard, due de plein droit, avec un complément possible sur justificatifs (articles L441-10, II, et D441-5) [FV].
- **Sanctions administratives** [FV] :
  - délais (L441-16) : jusqu'à **75 000 €** pour une personne physique et **2 M€** pour une personne morale, le double en cas de réitération ;
  - mentions de facture (L441-9) : jusqu'à 75 000 € et 375 000 €.
- **TVA sur les acomptes.** Pour une prestation de services, la TVA est **exigible à l'encaissement des acomptes**, du prix ou de la rémunération, sauf option pour les débits (article 269, 2, c). Il faut émettre une **facture d'acompte**. Une facture d'acompte ne rend pas la TVA exigible avant l'encaissement [FV].

### Détail : mentions obligatoires (Service Public F31808, vérifié le 11/08/2026) [FV]
- **Numérotation et dates** : numéro unique et chronologique, date d'émission, date de la prestation ou du versement de l'acompte.
- **Vendeur** : dénomination, forme juridique, capital, adresse du siège, SIREN, adresse de facturation si elle diffère.
- **Client** : dénomination ; numéro de bon de commande s'il existe.
- **TVA** : numéros de TVA intracommunautaire, sauf pour une facture de 150 € HT ou moins ; taux de TVA ou mention d'exonération, par exemple « TVA non applicable, article 293 B du CGI ».
- **Détail et montants** : quantité, prix unitaire HT, totaux HT et TTC, réductions.
- **Paiement** : date de règlement, conditions d'escompte (« Escompte pour paiement anticipé : néant »), taux des pénalités, indemnité forfaitaire de 40 €.
- **Société en cours d'immatriculation** : la page indique la mention « Siret en cours d'attribution » et une facture au nom de la société.
- **Quatre nouvelles mentions** : voir la partie (e).

### Sources officielles
| Source | Organisme | Date affichée | Courte citation |
|---|---|---|---|
| [C. com. L441-10](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038414392) | Légifrance | En vigueur depuis le 26/04/2019 | « ne peut dépasser soixante jours après la date d'émission de la facture » (extrait de recherche) |
| [C. com. L441-9 à L441-16](https://www.legifrance.gouv.fr/codes/id/LEGISCTA000038411051) | Légifrance | L441-11 en vigueur depuis le 01/01/2024 ; L441-16 depuis le 01/11/2021 | L441-9 : « Tout achat de produits ou toute prestation de service pour une activité professionnelle fait l'objet d'une facturation » |
| [C. com. D441-5](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000043197457) | Légifrance | En vigueur depuis le 27/02/2021 | « est fixé à 40 euros » |
| [Taux d'intérêt légal, F783](https://www.service-public.gouv.fr/particuliers/vosdroits/F783) | Service Public | Vérifié le 01/07/2026 | 2e semestre 2026 : 2,75 % (autres cas) |
| [Taux directeurs de la BCE](https://www.ecb.europa.eu/stats/policy_and_exchange_rates/key_ecb_interest_rates/html/index.en.html) | Banque centrale européenne | Page officielle consultée le 04/11/2026 | Taux de refinancement : 2,40 % au 17/06/2026, puis 2,65 % au 16/09/2026 |
| [CGI art. 269](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000044983827) | Légifrance | En vigueur depuis le 01/01/2023 ; abrogé à compter du 01/01/2027 (transfert au CIBS) | « lors de l'encaissement des acomptes, du prix » |
| [F31808](https://entreprendre.service-public.gouv.fr/vosdroits/F31808) | Service Public Entreprendre | Vérifié le 11/08/2026 | Mentions obligatoires sur une facture |

### Incertitudes et points à faire valider
- **Taux BCE à retenir au 1er janvier 2027** pour les factures du premier semestre 2027 [IN]. Le taux est de 2,65 % depuis le 16/09/2026. Une clause contractuelle fixe vaut mieux qu'un taux de référence mouvant [PR].
- **Facturation avant l'immatriculation** [HY]. Il est risqué d'encaisser un acompte au nom d'une société pas encore immatriculée : elle n'a pas encore de SIREN ni de numéro de TVA. Il faut faire valider le mécanisme de reprise des actes (article L210-6 du Code de commerce, non relu ici) par l'avocat, ou signer et facturer après l'immatriculation.
- **Qualification « acompte » ou « arrhes »** entre professionnels : à fixer clairement dans le contrat [HY, non vérifié ici].

### Conséquences pour Marwin Tech et GianLuca Carlone
- **Calendrier de paiement de l'offre** (`interne/offre-marwin-tech-remuneration-et-collaboration.md:19`) : acompte à la commande, solde du premier mois sous 7 jours, mois 2 à 6 payés d'avance. Il reste dans les limites légales [FV par comparaison avec L441-10].
- **Effet sur la trésorerie** de chaque encaissement d'avance : facture d'acompte et TVA exigible au moment de l'encaissement [FV]. Exemple [ES] :
  - acompte de 7 500 € HT : 1 500 € de TVA, 9 000 € TTC ;
  - mois à 15 000 € HT : 3 000 € de TVA, 18 000 € TTC.
- **Conditions générales et factures** : elles doivent porter le taux des pénalités (au moins 8,25 % au second semestre 2026), l'indemnité de 40 € et la mention d'escompte [FV].
- **Retard de paiement de GianLuca** : les pénalités et l'indemnité sont dues de plein droit [FV]. Leur réclamation effective relève d'une décision commerciale [HY].

---

## Tableau récapitulatif

| Règle | Valeur ou condition | Source | Certitude |
|---|---|---|---|
| Fin du 238 bis AB | Achats **avant** le 31/12/2028 (loi n° 2026-103, art. 89) | Légifrance art. 238 bis AB ; BOFiP 15/04/2026 | Élevée [FV] |
| Plafond 238 bis AB | 20 000 € ou 5 ‰ du chiffre d'affaires (le plus élevé), moins le mécénat ; excédent perdu | BOI-BIC-CHG-70-10 § 220 | Élevée [FV] |
| Lieu d'exposition | Accessible au public ou aux salariés ; pas un bureau, pas un lieu réservé aux seuls clients ; cinq exercices | BOI-BIC-CHG-70-10 § 80 à 100 | Élevée [FV] ; application aux hôtels et restaurants : moyenne [HY] |
| Œuvre originale | Peinture « entièrement exécutée à la main » ; sculpture « exécutée entièrement par l'artiste » ; 8 fontes ; 30 photographies | CGI annexe III art. 98 A | Élevée [FV] |
| 3D, robot, IA | Exclus selon toute vraisemblance (procédés suppléant la main, moyens mécaniques) | BOI-TVA-SECT-90-10 § 135, 140, 210 ; question écrite 22584 | Moyenne à élevée [HY] ; rescrit nécessaire |
| Rescrit 238 bis AB | L80 B 1° : réponse en trois mois, silence sans valeur d'accord | LPF L80 B | Élevée [FV] |
| Mécénat | Réduction de 60 % (40 % au-delà de 2 M€) ; plafond de 20 000 € ou 5 ‰ ; dons aux artistes exclus | F22263 | Élevée [FV] |
| TVA des œuvres d'art | 5,5 % sur toutes les livraisons depuis le 01/01/2025, sauf régime de la marge | BOI-TVA-SECT-90-40 ; CGI 278-0 bis | Élevée [FV] |
| Pièces faites à la machine | 20 % (pas des œuvres d'art au sens fiscal) | Article 98 A et BOFiP | Moyenne à élevée [HY] |
| TVA dans le CIBS | Transfert au 01/01/2027 ; références au CGI tolérées jusqu'au 30/06/2028 | Projet de loi Sénat n° 71 (ordonnance n° 2026-671) | Élevée [FV] |
| Zone de Cosne-Cours-sur-Loire | Zone FRR de base : oui ; FRR+ : non | Arrêtés du 19/06/2024 (consolidé) et du 09/07/2025 | Élevée [FV] |
| Fenêtre et durée FRR | Créations du 01/07/2024 au 31/12/2029 ; exonération totale 59 mois, puis 75 %, 50 %, 25 % ; de minimis 300 000 € | CGI 44 quindecies A ; F31139 | Élevée [FV] |
| Travail hors zone (sédentaire) | Au plus 25 % : exonération avec imposition au prorata du hors-zone ; au-delà : perte totale | CGI 44 quindecies A, V, B, 2° ; BOFiP § 150 et 160 | Élevée [FV] ; qualification de Marwin : [IN] |
| Implantation FRR | Siège, direction et moyens en zone ; domiciliation seule insuffisante | BOFiP § 120 et 260 | Élevée [FV] |
| Rescrit FRR | L80 B 2° : notification préalable ; silence de trois mois vaut accord | LPF L80 B | Élevée [FV] ; moment du dépôt : [IN] |
| CFE l'année de création | Exonérée si la 1447-C-SD est déposée avant le 31/12 ; base réduite de 50 % en N+1 | F23547 | Élevée [FV] |
| CFE et FRR | Sur délibération (Cœur de Loire, 26/09/2024) ; liée au bénéfice de l'exonération 44 quindecies A | Pièce interne, p. 21 et 25 ; Pappers (source secondaire) | Moyenne [FV via source secondaire] |
| Cotisation minimum de CFE 2026 | De 250 € à 597 € jusqu'à 7 769 €, selon le chiffre d'affaires de N-2 ; montant local inconnu | F23547 | Élevée pour le barème [FV] ; local : [IN] |
| Réception des factures électroniques | Obligatoire pour toutes les entreprises depuis le 01/09/2026 | DGFiP, fiche 3 et FAQ | Élevée [FV] |
| Émission et e-reporting (PME et micro) | Au plus tard le 01/09/2027 | DGFiP, fiche 3 et FAQ | Élevée [FV] |
| Taille pour le calendrier | Exercice clos avant le 01/01/2025, à défaut premier exercice clos | FAQ « J'approfondis », Q 1.1 | Élevée [FV] |
| Sanctions de la facture électronique | 50 € par facture (plafond de 15 000 € par an) ; 500 € puis 1 000 € sans plateforme de réception | FAQ DGFiP Q 2.4 et 2.5 | Moyenne [FV sur la FAQ, texte légal non lu] |
| Quatre nouvelles mentions | Obligatoires depuis le 01/09/2026 (DGFiP) ou progressives (Service Public) | FAQ DGFiP ; F31808 | Faible (sources contradictoires) |
| Franchise de TVA 2026 | Services : 37 500 € / 41 250 € ; ventes : 85 000 € / 93 500 € ; artistes : 50 000 € / 55 000 € | CGI 293 B ; F21746 | Élevée [FV] |
| Seuil unique de 25 000 € | Prévu par la loi de finances pour 2025, suspendu, supprimé par la loi n° 2025-1044 du 03/11/2025 | Légifrance 293 B ; BOFiP ACTU-2025-00144 | Élevée [FV] |
| Délai de paiement entre entreprises | 30 jours sans clause ; au plus 60 jours ou 45 jours fin de mois | C. com. L441-10 | Élevée [FV] |
| Pénalités de retard | Au moins trois fois le taux légal (8,25 % au second semestre 2026) ; par défaut BCE + 10 points (12,40 %) | L441-10 ; F783 ; BCE | Élevée pour la règle [FV] ; calcul [ES] |
| Indemnité de recouvrement | 40 € | C. com. D441-5 | Élevée [FV] |
| TVA sur les acomptes de services | Exigible à l'encaissement ; facture d'acompte obligatoire | CGI 269, 2, c ; F31808 | Élevée [FV] |

---

## Limites de ce mémo
- **Lecture des pages.** Les pages ont été lues par un outil de récupération qui restitue des citations courtes. Plusieurs paragraphes sont donc résumés plutôt que recopiés. Les textes marqués « extrait de recherche » n'ont pas été ouverts : amendement I-2359, article L441-10 pour la citation exacte, article 289 du CGI, question impots.gouv.fr sur la franchise.
- **Documents PDF.** Trois PDF officiels ont été téléchargés pour lecture seule, dans le dossier de travail (sous-dossier `r2dl`) ou dans le cache de l'outil : FAQ et fiche 3 de la DGFiP, projet de loi n° 71 du Sénat, question écrite AN n° 22584.
- **Sources secondaires**, signalées à chaque usage : Pappers Politique (délibération Cœur de Loire) ; Legifiscal (ordonnance n° 2026-671, confirmée ensuite par le Sénat) ; Bpifrance Création et LexisVeille (loi n° 2025-1044, confirmée par Légifrance) ; Banque des Territoires (nombre de communes FRR+ dans la Nièvre, non repris).
- **Non examinés** : CVAE, taxe foncière, IS (taux et conditions du taux réduit), régime social des dirigeants, ACRE. Ils relèvent d'autres volets de l'audit.
