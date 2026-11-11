# Clauses d’un contrat court de prestation intellectuelle : droits sur les livrables, données personnelles, responsabilité, arrêt, facture électronique

Note de travail interne — sources publiques consultées le 10 novembre 2026 — corrigé le 11 novembre 2026 par une mention datée (audit final) — ce n’est pas un avis juridique, fiscal ou d’assurance

Document interne à Marwin Tech. Ne pas transmettre à GianLuca Carlone. Aucune clause ci-dessous n’est un texte prêt à signer : un avocat relit le bon de commande et ses conditions avant tout envoi.

Étiquettes : [Texte officiel] = loi, règlement, décision de justice lue sur un site officiel. [Autorité ou organisme] = CNIL, DGFiP, Commission européenne, service-public. [Source professionnelle] = syndicat, éditeur, fournisseur. [À confirmer] = non vérifié sur une source primaire ce jour. [Dépôt] = fait déjà établi dans une pièce du dépôt, citée par son chemin.

Pièces du dépôt relues avant d’écrire (pour ne pas refaire ce qui existe) :

- `audit/2026-11-09-audit-presentation-et-offre/travaux/BRIEF.md` (règles des documents clients) ;
- `audit/2026-11-04-audit-strategique/annexes/travaux/rj-R3-travail-contrats.md`, sections (e), (f), (i), (j) ;
- `audit/2026-11-04-audit-strategique/annexes/travaux/rj-R4-donnees-ia.md`, sections (b) et (e) ;
- `audit/2026-11-04-audit-strategique/annexes/travaux/rj-R2-fiscal.md`, section (e) ;
- `audit/2026-11-04-audit-strategique/interne/12-gouvernance-contrat-sortie.md`, sections 11 et 13 ;
- `pour-carlone/logiciels-et-automatisations/2026-11-09-logiciels-sur-mesure-methode-et-garanties.md`.

## En bref

- **Droits.** Payer ne suffit pas. Il faut une cession écrite, droit par droit, avec étendue, destination, lieu et durée. Elle vise des livrables nommés, jamais « tout ce que nous créerons ». Avant cela, chaque associé cède ses droits à la société.
- **IA.** Pas de loi spéciale. Le rapport du CSPLA du 16 juillet 2026 protège la création où l’humain garde un rôle créatif, pas la production sans apport humain. On cède « tous les droits qui existent », sans garantir qu’il y en a.
- **Données.** Par défaut, le cadrage se fait sans donnée personnelle. Dès qu’un fichier de personnes est ouvert, un écrit conforme à l’article 28 du RGPD est obligatoire, et chaque outil d’IA doit être autorisé par écrit par le client.
- **Responsabilité.** Un plafond est possible. Il tombe en cas de faute lourde, s’il vide l’obligation essentielle, ou s’il crée un déséquilibre significatif. L’article L442-1 du Code de commerce a été modifié en août 2026.
- **Arrêt.** La règle par défaut (Code civil, art. 1794) est plus dure pour le client que notre clause. L’acompte gardé s’écrit comme le prix du travail fait et du temps réservé. Le travail remis est cédé.
- **Facture.** Depuis le 1er septembre 2026, toute entreprise doit pouvoir recevoir des factures électroniques : plateforme agréée dès l’immatriculation. Émission électronique au plus tard le 1er septembre 2027 pour les petites entreprises.
- **Forme.** Un bon de commande d’une page, des conditions de deux pages, deux annexes. Chaque promesse de l’offre a sa clause, avec les mêmes mots.
- **Limite.** Rien ici n’est validé par un avocat, un expert-comptable ou un assureur. Les points marqués [À confirmer] leur sont destinés.

## 1. Cession des droits d’auteur sur les livrables

**Les faits.**

- Commander et payer ne rend pas le client titulaire des droits : il faut un écrit. « Les contrats par lesquels sont transmis des droits d’auteur doivent être constatés par écrit » (Code de la propriété intellectuelle, art. L131-2 ; `rj-R3-travail-contrats.md:393`, vérifié sur Légifrance le 4 novembre 2026). [Texte officiel] [Dépôt]
- Chaque droit cédé doit faire l’objet d’une « mention distincte », et le domaine d’exploitation doit être délimité « quant à son étendue et à sa destination, quant au lieu et quant à la durée » (CPI, art. L131-3, en vigueur depuis le 3 juillet 1992 ; `rj-R3-travail-contrats.md:394, 412`). [Texte officiel] [Dépôt]
- « La cession globale des œuvres futures est nulle » (CPI, art. L131-1). Un bon de commande ne peut donc pas céder « tout ce que nous créerons pour vous ». Il cède les livrables qu’il nomme (`rj-R3-travail-contrats.md:395`). [Texte officiel] [Dépôt]
- Pour un logiciel, les droits à nommer sont ceux de l’article L122-6 : 1° la reproduction, permanente ou provisoire, y compris le chargement, l’affichage, l’exécution, la transmission et le stockage ; 2° « la traduction, l’adaptation, l’arrangement ou toute autre modification » ; 3° « la mise sur le marché à titre onéreux ou gratuit, y compris la location » (Légifrance, art. L122-6, version en vigueur depuis le 11 mai 1994, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006278919, consulté le 10 novembre 2026). [Texte officiel]
- Un tribunal a jugé que la règle stricte de L131-3 ne s’applique pas à tous les contrats (TJ Paris, 20 avril 2023, n° 21/14626, pour un logiciel). La voie prudente reste d’écrire la cession selon L131-3 (`rj-R3-travail-contrats.md:394, 416`). [Texte officiel] [Dépôt]
- Le prix peut être forfaitaire, notamment pour un logiciel. Une cession gratuite doit être dite expressément (fiche F22667, entreprendre.service-public.gouv.fr, vérifiée le 3 mai 2024 ; `rj-R3-travail-contrats.md:399`). [Autorité ou organisme] [Dépôt]
- Marwin Tech n’a pas de salarié. La règle qui donne à l’employeur les droits sur les logiciels de ses employés (CPI, art. L113-9) ne joue donc pas pour Morgan Olsen et Mathys Couet, dirigeants non salariés (`rj-R3-travail-contrats.md:396`). [À confirmer] par l’avocat.

**Ce qu’un prestataire sans salarié doit écrire, en pratique.**

1. **Une chaîne de droits complète.** Avant de céder au client, la société doit tenir elle-même les droits : cession écrite de chaque associé à Marwin Tech (ou apport), et de tout indépendant qui aiderait. Sans cela, la société cède ce qu’elle n’a pas. [Dépôt : `rj-R3-travail-contrats.md:425`] [À confirmer] par l’avocat pour la forme (acte séparé, clause des statuts ou du pacte).
2. **Une liste des livrables cédés**, par leur nom, dans le bon de commande : dossier de cadrage, tableau d’inventaire, trames, maquettes.
3. **Les droits, un par un** : reproduire, représenter, modifier et adapter, traduire, diffuser à ses équipes, à ses sociétés et à ses conseils ; pour un logiciel, les trois droits de L122-6.
4. **Étendue et destination** : pour les besoins internes de ses sociétés et de ses projets, y compris la remise à un autre prestataire. **Lieu** : le monde entier. **Durée** : toute la durée légale des droits.
5. **Le moment** : la cession prend effet au paiement complet du prix du bon de commande. Avant ce paiement, le client a un droit d’usage interne du document remis. « Remettre n’est pas céder » (`12-gouvernance-contrat-sortie.md:26, 546`). [Dépôt]
6. **Le prix de la cession** : compris dans le forfait. Il faut l’écrire. [À confirmer] : faut-il isoler une part du prix pour la cession (question d’avocat et d’expert-comptable).

**Outils, méthodes et composants préexistants de Marwin Tech.** Ils ne sont pas cédés. Ils sont concédés : licence non exclusive, gratuite, pour le monde entier, pour la durée des droits, pour les besoins des sociétés du client, avec le droit de les faire maintenir par un tiers ; elle survit à la fin du contrat (`12-gouvernance-contrat-sortie.md:420` ; document client du 9 novembre, section 5). Le savoir-faire et les méthodes ne sont pas des œuvres : on écrit seulement que Marwin Tech reste libre de les réutiliser, sans les informations du client. [Dépôt] [À confirmer]

**Composants tiers ou libres.** Marwin Tech ne peut pas céder ce qui appartient à un tiers. Le contrat renvoie à une liste : nom, version, licence. Chaque composant reste sous sa propre licence. Piège : une licence libre « à réciprocité » peut imposer des obligations si le logiciel est redistribué. [À confirmer] par l’avocat, composant par composant. Pour le cadrage (documents et tableaux), ce point est presque vide ; il compte pour le logiciel, plus tard.

## 2. Contenus produits avec l’aide d’une IA

- Il n’existe pas de texte spécial. Le rapport du Conseil supérieur de la propriété littéraire et artistique (CSPLA), publié le 16 juillet 2026, juge que le droit d’auteur actuel suffit. Il distingue la « création hybride », où l’humain garde un rôle créatif et qui peut être protégée si elle est originale, et la « production synthétique, générée sans intervention humaine significative », qui reste hors du droit d’auteur (ministère de la Culture, page du 16 juillet 2026, lien en fin de note). [Autorité ou organisme] **Nouveau en 2026.** C’est un rapport, pas une loi.
- L’originalité peut se loger à trois moments : avant (conception, paramétrage), pendant (direction de l’outil, essais successifs), après (sélection, retouche, intégration). La vraie difficulté est la preuve de l’apport humain (même page). [Autorité ou organisme]
- Un cabinet d’avocats cite deux décisions récentes (Cour de justice de l’Union européenne, Mio/Konektra, 4 décembre 2025 ; Evema c/ Someva, 9 avril 2026). Nous ne les avons pas lues. [Source professionnelle] [À confirmer]
- Côté fournisseur, les conditions commerciales d’Anthropic (en vigueur depuis le 17 juin 2025, articles B et D.3) disent que le client garde ses droits sur ce qu’il envoie et possède les résultats ; qu’Anthropic lui cède ses propres droits sur ces résultats « (if any) », c’est-à-dire « s’il y en a » ; qu’Anthropic ne peut pas entraîner ses modèles sur ces contenus ; et que le client doit vérifier les résultats avant de s’en servir (https://www.anthropic.com/legal/commercial-terms). [Source professionnelle]
- OpenAI suivrait la même logique, et ses conditions ajouteraient que le code généré peut relever de licences de tiers. Nous ne l’avons lu que sur des sites secondaires. [À confirmer]

**Ce que cela veut dire.** Le fournisseur ne réclame rien. Mais il ne garantit pas qu’un droit d’auteur existe, ni que le résultat est unique ou libre de droits de tiers.

**Prudence dans la clause de cession.**

1. Dire que des outils d’IA aident, sous relecture et correction humaines.
2. Céder « tous les droits qui existent » sur le livrable. Ne pas garantir que chaque élément est protégé par le droit d’auteur.
3. Garantir seulement ce que l’on maîtrise : la société tient les droits de ses auteurs ; elle n’a pas copié sciemment un tiers ; si un tiers réclame, elle corrige ou remplace. La garantie de son propre fait ne s’écarte pas. [À confirmer]
4. Garder la trace des choix humains (consignes, versions, corrections) : c’est la preuve de l’originalité.

## 3. Données personnelles pendant un cadrage

**Les faits.**

- Le sous-traitant est celui « qui traite des données pour le compte d’un autre organisme (le responsable de traitement), dans le cadre d’un service ou d’une prestation » (CNIL, « Travailler avec un sous-traitant », https://www.cnil.fr/fr/sous-traitant, date non affichée). [Autorité ou organisme]
- « Un contrat écrit, ou un autre acte juridique, est obligatoire. » Et : « Le contrat ne doit pas se contenter de reproduire le RGPD. Il doit expliquer concrètement comment les obligations seront mises en œuvre et notamment le niveau de sécurité requis » (CNIL, « Responsable du traitement, sous-traitants : comment bien identifier son rôle ? », 6 juin 2025). [Autorité ou organisme]
- Contenu minimal (RGPD, art. 28 §3) : objet, durée, nature et finalité du traitement, type de données, catégories de personnes. Puis huit engagements : agir sur instruction écrite ; confidentialité des personnes ; sécurité ; règles pour les sous-traitants ultérieurs ; aide pour les droits des personnes ; aide en cas de violation ; suppression ou restitution en fin de mission ; preuves et audits (texte sur https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4 ; `rj-R4-donnees-ia.md`, section (b)). [Texte officiel] [Dépôt]
- L’écrit peut être électronique (art. 28 §9). Le sous-traitant qui fixe lui-même les buts et les moyens devient responsable (art. 28 §10). [Texte officiel]
- Deux modèles publics existent : l’exemple de clauses de la CNIL (« Ces clauses ne constituent pas, à elles seules, un contrat de sous-traitance ») et les clauses types de la Commission, décision (UE) 2021/915 du 4 juin 2021. Elles ne sont pas obligatoires si le contrat contient tous les éléments de l’article 28 (CNIL, 30 juin 2021, https://cnil.fr/fr/clauses-contractuelles-types-entre-responsable-de-traitement-et-sous-traitant). [Autorité ou organisme]
- Réutiliser une même base pour plusieurs clients est un signe fort que l’on devient responsable d’un traitement à soi (CNIL, 8 avril 2024). [Autorité ou organisme]

**Quand Marwin Tech est-elle sous-traitante pendant le cadrage ?** Lecture de travail. [À confirmer] par l’avocat.

- **Non**, tant qu’elle n’ouvre aucun fichier de personnes : entretiens, plans, liste des bâtiments, procédures, modèles de tableaux vides.
- **Oui**, dès qu’elle consulte, copie, trie ou analyse pour le client un fichier de personnes : fichier de contacts, locataires, salariés, artistes. Lire à l’écran compte déjà.
- Dans tous les cas, elle est responsable de ses propres données : coordonnées de ses interlocuteurs, factures.

**Règle simple pour le bon de commande.** Par défaut, le cadrage se fait sans donnée personnelle : structure des fichiers, noms de colonnes, exemples fictifs. Si un accès réel devient utile, une annexe « données » est signée avant. Elle dit : quel fichier, pour quoi faire, combien de temps ; accès en lecture seule dans les outils du client ; aucune copie sur nos postes ; engagement de confidentialité de chaque intervenant ; alerte écrite en cas d’incident ; restitution ou suppression à la remise du dossier, confirmée par écrit. Le document client du 9 novembre promet déjà « aucune donnée réelle avant que les rôles soient fixés par écrit » et une alerte sous 24 heures : le bon de commande doit dire la même chose. [Dépôt]

## 4. Outils d’IA appliqués aux documents du client

- Si un outil d’IA reçoit des données personnelles du client, son fournisseur devient un sous-traitant ultérieur. Il faut l’autorisation écrite préalable du client, et un contrat qui reprend les mêmes obligations (RGPD, art. 28 §2 et §4). [Texte officiel]
- La CNIL demande à l’organisme qui utilise une IA générative de « s’interroger sur son rôle et celui du fournisseur », « le cas échéant en passant un contrat de sous-traitance », de « s’opposer à la réutilisation des données d’usage par le fournisseur du système, voire à l’enregistrement de l’historique », et d’écrire une charte des usages autorisés et interdits (CNIL, questions-réponses du 18 juillet 2024). [Autorité ou organisme]
- Les offres grand public peuvent réutiliser les échanges pour entraîner les modèles. Les offres professionnelles (accès par interface de programmation, offres entreprise) ne le font pas par défaut. Anthropic et OpenAI publient chacun un accord de traitement des données (24 février 2025 ; 1er décembre 2025) (`rj-R4-donnees-ia.md`, section (e)). [Source professionnelle] [Dépôt]
- Lieu des données : au 4 novembre 2026, Anthropic et OpenAI ne figuraient pas sur la liste du cadre de transfert Union européenne – États-Unis. Un envoi de données personnelles vers eux repose donc sur les clauses types de la décision (UE) 2021/914 et sur une analyse d’impact du transfert (`rj-R4-donnees-ia.md`, section (e) ; guide de la CNIL). [Dépôt] [À confirmer] à la date de signature.
- **Recommandations de la CNIL, 2025.** 19 juin 2025 : recommandations sur l’intérêt légitime pour développer une IA. 22 juillet 2025 : recommandations finales ; le sous-traitant doit avoir un contrat, suivre strictement les instructions, ne rien faire d’autre des données, les sécuriser, alerter (https://www.cnil.fr/fr/developpement-des-systemes-dia-les-recommandations-de-la-cnil-pour-respecter-le-rgpd). [Autorité ou organisme]
- **2026.** Aucune page de la CNIL sur l’IA datée de 2026 n’est ressortie de notre recherche. Le projet européen de simplification (« omnibus numérique ») n’était pas adopté au 4 novembre 2026 (`rj-R4-donnees-ia.md`). [À confirmer]

**Ce que le contrat doit dire.** Une liste nominative des outils et hébergeurs, en annexe. Pas d’ajout sans accord écrit préalable. Offres professionnelles seulement. Aucune réutilisation pour entraîner un modèle. Aucun document du client dans un compte personnel ou une offre grand public. Données personnelles hors Union européenne : seulement rendues non nominatives, ou pas du tout. La même règle vaut pour les documents confidentiels sans donnée personnelle (prix d’achat, baux, plans d’affaires) : c’est alors la clause de confidentialité qui joue (partie 5).

## 5. Confidentialité et secret des affaires

- Le secret des affaires protège une information qui remplit trois critères : elle n’est pas « généralement connue ou aisément accessible » dans le secteur ; elle « revêt une valeur commerciale, effective ou potentielle, du fait de son caractère secret » ; elle fait l’objet « de mesures de protection raisonnables, compte tenu des circonstances, pour en conserver le caractère secret » (Code de commerce, art. L151-1, en vigueur depuis le 1er août 2018, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037266553). [Texte officiel]
- Conséquence pratique : une clause de confidentialité signée est une de ces « mesures de protection ». Elle aide le client à garder la protection de la loi pour ses prix d’achat, ses baux, ses projets. [À confirmer]
- Clause habituelle : tout ce que le client remet ou montre est confidentiel, marqué ou non ; usage limité à la mission ; accès limité aux personnes qui en ont besoin ; exceptions classiques (information déjà publique sans faute, reçue d’un tiers libre de la donner, trouvée seul, exigée par la loi ou un juge) ; restitution ou destruction à la fin. On retrouve cette structure dans les conditions commerciales d’Anthropic, article E (version du 17 juin 2025). [Source professionnelle]
- Durée : la loi n’en fixe pas. L’usage de trois à cinq ans après la fin de la mission n’a pas été vérifié sur une source ce jour. [À confirmer] Proposition à faire valider : cinq ans après la fin ; sans limite pour ce qui reste un secret des affaires ; les données personnelles suivent le RGPD, pas cette durée.
- La clause est réciproque : elle protège aussi les méthodes et les prix de Marwin Tech.

## 6. Responsabilité

- **Obligation de moyens.** Marwin Tech promet du soin et une méthode, pas un résultat économique. Piège : un forfait avec un livrable nommé et une date ressemble, pour la remise elle-même, à un résultat. Il faut écrire les deux : « nous remettons le dossier » (ferme) et « nous ne garantissons pas les gains » (moyens). [À confirmer]
- **Plafond.** Il est possible entre professionnels, avec quatre limites. Il tombe en cas de « faute lourde ou dolosive » (Code civil, art. 1231-3). Il est réputé non écrit s’il « prive de sa substance l’obligation essentielle » (art. 1170). Dans un contrat d’adhésion, une clause non négociable qui crée un déséquilibre significatif est réputée non écrite (art. 1171) (`rj-R3-travail-contrats.md`, section (f)). [Texte officiel] [Dépôt]
- Quatrième limite : engage sa responsabilité celui qui soumet l’autre partie « à des obligations créant un déséquilibre significatif dans les droits et obligations des parties » (Code de commerce, art. L442-1, I, 2°, version en vigueur depuis le 20 août 2026, modifiée par la loi n° 2026-796 du 18 août 2026, art. 54, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054716237). [Texte officiel] **Texte modifié en 2026** : nous n’avons pas comparé le I avec la version d’avant. [À confirmer]
- Formule déjà retenue : plafond égal au plus élevé entre douze mois d’honoraires et le prix du bon de commande, toujours sous le plafond assuré ; pas de plafond pour la faute lourde ou intentionnelle (`12-gouvernance-contrat-sortie.md`, 11.14). Pour un cadrage à 6 500 € HT, un plafond égal au prix est bas : l’avocat dit s’il tient. [Dépôt] [À confirmer]
- « Dommages indirects » : l’expression seule est floue. Il faut donner des exemples (perte de chiffre d’affaires, perte de chance). [À confirmer]
- **Assurance.** L’assurance de responsabilité civile professionnelle n’est pas obligatoire en général (fiche F37365, vérifiée le 7 juillet 2026, `rj-R3-travail-contrats.md`). Notre document client promet une attestation avant tout démarrage. La mention au contrat (assureur, numéro de police, zone couverte) ne s’écrit qu’une fois la police souscrite. Les assureurs peuvent exclure les risques liés au numérique ou à l’IA : à lire avant de signer. [Dépôt] [À confirmer]

## 7. Clause d’arrêt, force majeure, litiges

- **Règle par défaut.** « Le maître peut résilier, par sa seule volonté, le marché à forfait, quoique l’ouvrage soit déjà commencé, en dédommageant l’entrepreneur de toutes ses dépenses, de tous ses travaux, et de tout ce qu’il aurait pu gagner dans cette entreprise » (Code civil, art. 1794, en vigueur depuis le 21 mars 1804, https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006443583). [Texte officiel]
- Sans clause, le client qui arrête un forfait doit donc aussi le gain manqué. Notre clause est plus douce pour lui : il ne laisse que l’acompte. Que l’on puisse écarter l’article 1794 par contrat, et qu’il vaille pour une prestation intellectuelle, n’a pas été vérifié ce jour. [À confirmer]
- **Pénalité ou prix de sortie ?** Pour une pénalité, « le juge peut, même d’office, modérer ou augmenter la pénalité ainsi convenue si elle est manifestement excessive ou dérisoire » (Code civil, art. 1231-5, en vigueur depuis le 1er octobre 2016). [Texte officiel] Un extrait de jurisprudence lu sur un site privé dit qu’une somme convenue pour pouvoir sortir du contrat est un « dédit », que le juge ne modère pas. [À confirmer]
- **Force majeure.** C’est « un événement échappant au contrôle du débiteur, qui ne pouvait être raisonnablement prévu lors de la conclusion du contrat et dont les effets ne peuvent être évités par des mesures appropriées ». Empêchement temporaire : l’exécution est suspendue. Empêchement définitif : le contrat est résolu de plein droit (Code civil, art. 1218, en vigueur depuis le 1er octobre 2016). [Texte officiel]
- **Médiation.** Le Médiateur des entreprises propose un service « gratuit, rapide – moins de trois mois – et confidentiel », pour « tout différend lié à l’exécution d’un contrat de droit privé ». Un médiateur rappelle sous sept jours (economie.gouv.fr, date non affichée ; fiche F38216 de service-public). [Autorité ou organisme]

**Rédaction prudente de « l’acompte reste acquis, le solde n’est pas dû, et vous recevez le travail fait ».**

1. Présenter l’acompte gardé comme le prix du travail déjà fait et du temps réservé. Pas comme une sanction.
2. Écrire que le prix dû est alors ramené à l’acompte, et que le travail remis est cédé dans les mêmes conditions. Sinon la clause contredit « cession au paiement complet ».
3. Fixer la forme (un écrit daté) et le délai de remise du travail fait (dix jours ouvrés, à valider).
4. Dire ce qui se passe si c’est Marwin Tech qui arrête : rendre la part d’acompte non couverte par un travail remis. Décision à prendre.
5. Force majeure : renvoyer à l’article 1218 ; après trente jours de blocage, chacun peut arrêter.
6. Droit français. Médiateur des entreprises avant tout procès. Une clause qui choisit un tribunal ne vaut qu’entre commerçants et si elle est très apparente (Code de procédure civile, art. 48, non relu) ; l’entité qui signera pour GianLuca Carlone n’est pas connue. [À confirmer]

**Deux pièges.** Un arrêt au deuxième jour laisse la moitié du prix pour peu de travail : risque d’« avantage […] manifestement disproportionné » (Code de commerce, art. L442-1, I, 1°). [À confirmer] Et la clause n’efface pas un éventuel droit de rétractation de quatorze jours, si la commande est signée hors de nos locaux par une entité de cinq salariés au plus dont ce n’est pas l’activité principale : règle interne, aucun encaissement ni démarrage avant sept jours (`12-gouvernance-contrat-sortie.md`, 11.6). [Dépôt] [À confirmer]


## 8. Facture électronique

- **En vigueur depuis 2026.** « Depuis le 1er septembre 2026, les grandes entreprises et les entreprises de taille intermédiaire doivent émettre leurs factures via une plateforme agréée, et toutes les entreprises doivent être en capacité de recevoir des factures électroniques » (impots.gouv.fr, actualité du 28 septembre 2026, https://www.impots.gouv.fr/actualite/facturation-electronique). [Autorité ou organisme]
- Les petites et moyennes entreprises et les microentreprises émettent sous cette forme au plus tard le 1er septembre 2027 (fiche F23208, entreprendre.service-public.gouv.fr, date non affichée). La taille d’une société créée fin 2026 se lit sur son premier exercice clos (`rj-R2-fiscal.md`, section (e)). [Autorité ou organisme] [Dépôt] [À confirmer] par l’expert-comptable.
- Une plateforme agréée est immatriculée par l’administration pour trois ans renouvelables. Une simple « solution compatible » ne transmet pas elle-même (impots.gouv.fr, « Facturation électronique et plateformes agréées », date non affichée). Une page d’economie.gouv.fr parle encore de « PDP » et de Chorus Pro : vocabulaire ancien, à ne pas reprendre. [Autorité ou organisme]
- **Quatre mentions nouvelles** : numéro SIREN du client ; catégorie de l’opération (biens, services ou les deux) ; option pour la TVA d’après les débits, si elle est prise ; adresse de livraison si elle diffère (impots.gouv.fr, « J’approfondis mes connaissances sur la réforme », date non affichée). La fiche F23208 les date du 1er septembre 2027 pour les petites entreprises ; une réponse de la DGFiP relevée dans le dépôt dit autre chose. Prudence : les mettre dès la première facture. [À confirmer]
- **Mentions classiques** (F23208) : date, numéro unique, date de la prestation, identité complète des deux parties, numéro du bon de commande s’il existe, numéro de TVA, désignation, total hors taxe et toutes taxes, date de règlement, escompte, taux des pénalités de retard, indemnité forfaitaire de 40 €. [Autorité ou organisme]
- Sanctions relevées dans le dépôt : 50 € par facture non émise sous forme électronique, plafonnés à 15 000 € par an ; 500 € puis 1 000 € par trimestre sans plateforme de réception, après mise en demeure (`rj-R2-fiscal.md`, section (e)). [Dépôt]

**Ce que cela impose.** À Marwin Tech : choisir une plateforme agréée dès l’immatriculation, car l’obligation de recevoir joue dès le premier jour. Au client : son entité doit déjà en avoir une ; le bon de commande lui demande dénomination, SIREN, adresse de facturation et numéro de TVA. Point d’expert-comptable : « 7 800 € TTC » suppose une TVA à 20 % ; une société en franchise en base ne facture pas de TVA. La facture d’acompte et la date d’exigibilité de la TVA (encaissement ou débits) se règlent avec lui. Aucune facture avant l’immatriculation (`BRIEF.md`). [Dépôt]

## 9. Indépendance et référence

- Une société immatriculée est présumée non salariée de son client. La présomption tombe s’il existe un lien de subordination juridique permanente (Code du travail, art. L8221-6, inchangé ; `rj-R3-travail-contrats.md`). [Dépôt]
- **Clause utile.** Marwin Tech organise seule son travail, ses horaires et ses outils. Elle peut avoir d’autres clients. Aucune exclusivité, dans aucun sens. Un interlocuteur unique côté client. L’administratrice valide les livrables ; elle ne donne pas d’ordres sur les horaires ni sur les méthodes.
- **Dépendance économique.** La clause ne l’efface pas : un seul client reste un risque d’affaires. L’abus de dépendance (Code de commerce, art. L420-2) suppose un effet sur la concurrence (`rj-R3-travail-contrats.md`, section (i)). [Dépôt]
- **Rupture brutale.** Rompre une relation commerciale établie demande « un préavis écrit qui tienne compte notamment de la durée de la relation commerciale ». **Nouveau en 2026** : le texte vise aussi « une réduction substantielle […] des volumes de commandes » (Code de commerce, art. L442-1, II, version du 20 août 2026). Un premier cadrage n’est sans doute pas encore une relation établie. [Texte officiel] [À confirmer]
- **Vigilance.** Le client doit se faire remettre des attestations (immatriculation, Urssaf) au-dessus d’un seuil non revérifié ce jour. Un nouvel article L8222-1-1 entre en vigueur fin décembre 2026 (loi n° 2026-534 du 25 juin 2026 ; `rj-R3-travail-contrats.md`). Le contrat prévoit donc la remise des attestations au démarrage. [Dépôt] [À confirmer]
- **Référence.** Accord écrit préalable, usage par usage, révocable. Par défaut, aucun nom cité. Les conditions d’Anthropic font l’inverse (citation permise sauf refus, article G) : c’est le modèle à ne pas suivre ici. [Source professionnelle]

## 10. Modèles publics et contrat d’une page

- **Numeum** publie une « contrathèque ». Son modèle de contrat de développement de logiciel spécifique limite la responsabilité aux « dommages directs et prévisibles », laisse les parties définir les dommages indirects et le plafond, et écarte le plafond « en cas de décès ou dommage corporel, ni en cas de dol ou faute lourde ». Il fait dire aux parties que le prix reflète ce partage du risque (lien en fin de note, date non affichée). [Source professionnelle]
- **CINOV, Bpifrance Création** : aucun modèle de contrat n’est ressorti de nos recherches ce jour. **Service-public** : des fiches (facture F23208, médiation F38216), pas de modèle de contrat trouvé.
- Deux listes d’éditeurs privés (rappli.fr, 2 août 2026 ; cidesp.com, 28 juillet 2026) donnent les mêmes rubriques, douze à quatorze : parties, objet et livrables, périmètre, calendrier, coopération du client, prix, facturation et retard, validation, changements, propriété intellectuelle, confidentialité, données personnelles, responsabilité et assurance, durée, arrêt et litiges. [Source professionnelle]

**Pour un contrat lisible par un non-juriste** (proposition de travail, sans source) :

1. Un bon de commande d’une page : qui, quoi, quand, combien, et les cinq promesses. Des conditions de deux pages au plus. Deux annexes : « données » et « outils ».
2. Une idée par phrase. Les mêmes mots que l’offre : si l’offre dit « le dossier est à vous », la clause s’appelle « Ce qui est à vous ».
3. Chaque promesse de l’offre a sa clause. Aucune clause ne dit moins que l’offre.
4. Un ordre de priorité : le bon de commande, puis les conditions, puis les annexes.
5. Aucun renvoi à un texte non joint.
6. Le signataire, sa qualité et son entité sont écrits en toutes lettres.

## Ce que cela change pour nos livrables

**Livrable 1 (offre d’une page et bon de commande).**

- Douze rubriques : Qui · Quoi · Quand · Prix et paiement · Ce qui est à vous · Vos données · Confidentialité · Notre responsabilité · Arrêter · Indépendance et référence · En cas de désaccord · Annexes.
- Champs à remplir pour le client : dénomination, forme, SIREN, adresse de facturation, numéro de TVA, nom et qualité du signataire. Les mêmes pour Marwin Tech, donc après l’immatriculation.
- Phrases possibles, à faire relire par l’avocat :
  - « Au paiement complet du prix, nous vous cédons les droits sur le dossier de cadrage et ses annexes : le reproduire, le modifier, le traduire, le diffuser à vos équipes, à vos sociétés et à vos conseils, le remettre à un autre prestataire. Pour le monde entier et pour toute la durée des droits. Le prix de cette cession est compris dans le forfait. »
  - « Nos méthodes et nos modèles généraux restent à nous. Vous recevez le droit de les utiliser et de les faire modifier, pour vos besoins, sans limite de durée. »
  - « Une partie du travail est faite avec l’aide d’outils d’IA, puis relue et corrigée par nous. Nous vous cédons tous les droits qui existent sur le résultat. »
  - « Le cadrage se fait sans donnée personnelle. Si l’accès à un fichier de personnes devient utile, nous signons d’abord une annexe “données”. »
  - « Vous pouvez arrêter à tout moment, par écrit. L’acompte nous reste acquis, en contrepartie du travail déjà fait et du temps réservé. Le solde n’est pas dû. Nous vous remettons le travail fait sous dix jours ouvrés ; il vous est cédé dans les mêmes conditions. »
  - « Nous ne citons pas votre nom sans votre accord écrit. »
- Délais : immatriculation avant toute facture et tout démarrage ; une signature avant l’immatriculation engage les associés en personne (`rj-R3-travail-contrats.md`) ; plateforme agréée dès l’immatriculation ; ni encaissement ni démarrage avant sept jours si la rétractation peut jouer ; 1er septembre 2027 pour l’émission électronique.

**Livrable 2 (texte de l’orateur, objections).** Trois réponses courtes. « À qui appartient le dossier ? » À vous, une fois le prix payé ; c’est écrit droit par droit. « Et si j’arrête ? » Vous gardez le travail fait, nous gardons l’acompte, le solde n’est pas dû. « Où vont mes documents ? » Ils restent dans vos outils ; la liste des nôtres est jointe au bon de commande. Mots à éviter : « garanti », « conforme », « sans frais », « jamais ».

**Livrable 3 (page pour l’administratrice).** Elle valide les livrables, tient la liste des accès et l’annexe « données », reçoit les alertes d’incident. Ne pas écrire qu’elle « dirige » ou « encadre » l’équipe de Marwin Tech.

**Livrable 4 (écrans d’exemple).** Mention « données fictives » sur chaque écran. Aucun nom réel. Les écrans ne sont cédés que si le bon de commande les nomme.

**Livrable 5 (kit de cadrage).** Quatre trames : annexe « données » ; liste des outils (nom, fournisseur, pays, type d’offre) ; journal des choix humains quand une IA aide ; engagement de confidentialité par intervenant.

**Livrable 6 (fiche de décision).** Neuf décisions : montant du plafond ; durée de la confidentialité ; sort de l’acompte si Marwin Tech arrête ; tribunal ; médiateur ; liste des outils d’IA ; règle de référence ; part du prix pour la cession ; régime de TVA.

**Livrable 7 (préalables à tout envoi).** Ajouter : cession écrite des droits de chaque associé à la société ; attestation d’assurance ; plateforme agréée ; accords de traitement des données avec les fournisseurs d’IA ; attestations de vigilance ; relecture du bon de commande par l’avocat.

**Livrable 8 (autre proposition, logiciel hôtelier).** Poser à tout fournisseur les mêmes questions : à qui sont les données, comment les exporter, combien coûte la sortie, qui sont les sous-traitants, où sont les serveurs. Le règlement européen sur les données interdit les frais de changement de fournisseur à partir du 12 janvier 2027 (`rj-R3-travail-contrats.md`, section (j)). [Dépôt]

**Livrable 9 (autorisations et délais).** Le dossier de cadrage liste les autorisations à titre d’information. Il n’est pas une consultation juridique : l’écrire. La règle qui réserve cette consultation à certaines professions (loi du 31 décembre 1971) n’a pas été relue. [À confirmer]

## Ce qu’il ne faut pas écrire ou promettre

- « Tout ce que nous créerons vous appartient » : cession globale d’œuvres futures, nulle.
- « Le dossier est à vous dès la remise », si la cession prend effet au paiement.
- Un droit d’auteur garanti sur ce qu’une IA a aidé à produire.
- « Vos données ne quittent jamais l’Europe », sans vérification outil par outil.
- « Conforme au RGPD », « certifié », « assuré », avant d’avoir les pièces.
- « Aucune responsabilité » : un plafond, jamais une exclusion totale.
- Un résultat garanti ou un gain chiffré.
- Une confidentialité « sans limite » sans les exceptions de la loi.
- Le nom ou le prix de l’autre prestataire dans un document client (`BRIEF.md`).
- « Résiliable sans frais », alors que l’acompte reste acquis.
- Une exclusivité, dans un sens ou dans l’autre.
- Une facture, un encaissement ou un démarrage avant l’immatriculation.

## Questions à poser à un professionnel

**Avocat.**

1. La cession écrite selon L131-3 est-elle complète ? Quelle forme pour la cession des associés à la société ?
2. Peut-on écarter l’article 1794 du Code civil ? L’acompte gardé est-il un dédit ou une pénalité ?
3. Quel plafond tient pour un cadrage à 6 500 € HT ? Qu’a changé la loi du 18 août 2026 à l’article L442-1, I ?
4. Le droit de rétractation peut-il jouer, selon l’entité qui signe et le lieu de signature ?
5. Quel tribunal écrire, selon que l’entité du client est commerçante ou non ?
6. Quelle garantie donner sur des contenus aidés par une IA ?
7. Quelle durée de confidentialité ? L’annexe « données » suffit-elle au regard de l’article 28 du RGPD ?

**Expert-comptable.** Régime de TVA et prix « 7 800 € TTC » ; facture d’acompte ; date d’effet des quatre mentions ; catégorie de taille d’une société créée fin 2026 ; choix de la plateforme agréée ; faut-il isoler le prix de la cession.

**Assureur.** La police couvre-t-elle le conseil, le logiciel, l’usage d’IA et les données ? Quel plafond, quelle date d’effet, quelles exclusions ? Que mettre sur l’attestation ?

**Architecte.** Non concerné par cette note.

## Ce qui n’a pas pu être vérifié

- La page d’impots.gouv.fr sur la facturation électronique entre entreprises (accès refusé, erreur 403). Les faits viennent d’autres pages du même site.
- Les modèles de CINOV et de Bpifrance Création : non trouvés.
- Les conditions d’OpenAI : lues sur des sites secondaires seulement.
- Le rapport complet du CSPLA et les deux décisions de 2025 et 2026 : non lus. Seule la page du ministère l’a été.
- Le caractère impératif ou non de l’article 1794, et son application à une prestation intellectuelle. La référence de la décision sur le « dédit ».
- Ce que la loi du 18 août 2026 a changé au I de l’article L442-1.
- L’usage sur la durée de confidentialité.
- Non relus ce jour : Code de procédure civile, art. 48 ; Code de commerce, art. L441-10 (pénalités de retard) ; loi du 31 décembre 1971 ; seuil de l’obligation de vigilance ; Code de la consommation, art. L221-3.
- Aucune page de la CNIL sur l’IA datée de 2026 n’a été trouvée.
- Un site d’avocat dit que certains modèles récents d’Anthropic imposent trente jours de conservation : non vérifié.
- L’entité qui signera pour GianLuca Carlone, sa forme et son effectif : inconnus.

## Sources (liste complète)

Toutes les pages ci-dessous ont été consultées le 10 novembre 2026. Quatorze recherches ou lectures au total.

**Textes officiels (Légifrance, sauf mention).**

- Code de la propriété intellectuelle, art. L122-6 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006278919 — en vigueur depuis le 11 mai 1994.
- Code de commerce, art. L442-1 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000054716237 — en vigueur depuis le 20 août 2026 (loi n° 2026-796 du 18 août 2026, art. 54).
- Code de commerce, art. L151-1 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000037266553 — en vigueur depuis le 1er août 2018.
- Code civil, art. 1794 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000006443583 — en vigueur depuis le 21 mars 1804.
- Code civil, art. 1218 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032041431 — en vigueur depuis le 1er octobre 2016.
- Code civil, art. 1231-5 — https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000032010131 — en vigueur depuis le 1er octobre 2016.
- RGPD, chapitre IV (art. 28), texte reproduit par la CNIL — https://www.cnil.fr/fr/reglement-europeen-protection-donnees/chapitre4 — règlement du 27 avril 2016.

**Autorités et organismes publics.**

- CNIL, « Travailler avec un sous-traitant » — https://www.cnil.fr/fr/sous-traitant — date non affichée.
- CNIL, « Sous-traitance : exemple de clauses » — https://www.cnil.fr/fr/sous-traitance-exemple-de-clauses — date non affichée.
- CNIL, « Clauses contractuelles types entre responsable de traitement et sous-traitant » — https://cnil.fr/fr/clauses-contractuelles-types-entre-responsable-de-traitement-et-sous-traitant — 30 juin 2021.
- CNIL, « Responsable du traitement, sous-traitants : comment bien identifier son rôle ? » — https://www.cnil.fr/fr/rgpd-comment-bien-identifier-son-role — 6 juin 2025.
- CNIL, recommandations sur le développement des systèmes d’IA — https://www.cnil.fr/fr/developpement-des-systemes-dia-les-recommandations-de-la-cnil-pour-respecter-le-rgpd — 22 juillet 2025.
- CNIL, « Les fiches pratiques IA » — https://www.cnil.fr/fr/les-fiches-pratiques-ia — date non notée.
- CNIL, qualification juridique des fournisseurs de systèmes d’IA — https://www.cnil.fr/fr/determiner-la-qualification-juridique-des-fournisseurs-de-systemes-dia — 8 avril 2024.
- CNIL, questions-réponses sur l’IA générative — https://cnil.fr/fr/les-questions-reponses-de-la-cnil-sur-lutilisation-dun-systeme-dia-generative — 18 juillet 2024.
- CNIL, recommandations sur l’intérêt légitime — https://cnil.fr/fr/recommandations-developpement-ia-interet-legitime — 19 juin 2025.
- DGFiP, actualité « Facturation électronique » — https://www.impots.gouv.fr/actualite/facturation-electronique — 28 septembre 2026.
- DGFiP, « J’approfondis mes connaissances sur la réforme » — https://www.impots.gouv.fr/japprofondis-mes-connaissances-sur-la-reforme — date non affichée.
- DGFiP, « Facturation électronique et plateformes agréées » — https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees — date non affichée.
- DGFiP, page non lue (erreur 403) — https://www.impots.gouv.fr/facturation-electronique-entre-entreprises-et-transmission-de-donnees-de-facturation.
- Service-public, fiche F23208 « Tout savoir sur la facturation » — https://entreprendre.service-public.gouv.fr/vosdroits/F23208 — date non affichée.
- Service-public, fiche F38216 (médiation) — https://entreprendre.service-public.gouv.fr/vosdroits/F38216 — date non notée.
- Ministère de l’Économie, fiche sur la facturation électronique entre entreprises — https://www.economie.gouv.fr/cedef/fiches-pratiques/la-facturation-electronique-entre-entreprises — date non notée, vocabulaire ancien.
- Ministère de l’Économie, « Relations difficiles avec un fournisseur ou un client, faites appel à la Médiation des entreprises » — https://www.economie.gouv.fr/entreprises/trouver-des-aides-et-des-financements/trouver-des-solutions-pour-son-entreprise-en-difficulte/relations-difficiles-avec-un-fournisseur-ou — date non affichée.
- Ministère de la Culture, CSPLA, « Publication du rapport de mission sur le statut des productions de l’intelligence artificielle » — https://www.culture.gouv.fr/nous-connaitre/organisation-du-ministere/conseil-superieur-de-la-propriete-litteraire-et-artistique-cspla/travaux-et-publications-du-cspla/missions-du-cspla/publication-du-rapport-de-mission-sur-le-statut-des-productions-de-l-intelligence-artificielle — 16 juillet 2026.

**Sources professionnelles.**

- Anthropic, « Commercial Terms of Service » — https://www.anthropic.com/legal/commercial-terms — en vigueur depuis le 17 juin 2025.
- Numeum, contrathèque, « Contrat de développement de logiciel spécifique » — https://quali-contratheque.numeum.fr/Contract/Download?contractId=3a3cbd95-0233-42cd-8ee1-0acccd8626cb&type=pdf — date non affichée.
- Cabinet DDG, observations sur le rapport du CSPLA — https://www.ddg.fr/actualite/observations-sur-le-rapport-du-cspla-sur-la-protection-des-creations-generees-par-lia — 17 août 2026.
- rappli.fr, liste de clauses d’un contrat de prestation — https://www.rappli.fr/blog/contrat-prestation-service-clauses-checklist.html — 2 août 2026. cidesp.com, 28 juillet 2026 (adresse exacte non notée).
- Pappers Justice, extraits sous l’article 1794 — https://justice.pappers.fr/loi/LEGITEXT000006070721/article/LEGIARTI000006443583 — date non affichée.
- Sites secondaires sur les conditions d’OpenAI : convika.com (23 octobre 2026), theinnovationattorney.com (27 juillet 2026), njbusiness-attorney.com (11 juin 2026). Adresses exactes non notées.

**Textes cités d’après le dépôt, non rouverts ce jour.** CPI, art. L131-1, L131-2, L131-3, L113-9 ; TJ Paris, 20 avril 2023 ; fiches F22667 et F37365 ; Code civil, art. 1231-3, 1170, 1171 ; Code du travail, art. L8221-6 ; Code de commerce, art. L420-2 ; Code de la consommation, art. L221-3 ; décisions (UE) 2021/915 et 2021/914. Voir les pièces listées en tête de note.

## Vérification du 10 novembre 2026

Relecture sceptique. Document interne — ne pas transmettre à GianLuca Carlone. Ce n’est pas un avis juridique, fiscal ou d’assurance. Cette partie l’emporte sur le reste de la note (`audit/2026-11-10-preparation-des-livrables/travaux/BRIEF-2.md`, § 4).

**Conclusion.** La note est juste sur l’essentiel. Pénalités de retard, indemnité de 40 €, obligation de recevoir des factures électroniques, Médiateur des entreprises et assurance non obligatoire : confirmés sur des pages officielles. Six points sont à corriger avant tout usage :

1. L’article L441-10 du Code de commerce est désormais lu : l’indemnité de 40 € est due par « tout professionnel » en retard ; la fiche F23211 la limite aux actes de commerce (k1a, ligne 302). La divergence va à l’avocat.
2. Médiateur des entreprises : une médiation dure « de quelques heures à 2 ou 3 mois maximum » ; il intervient dans des relations d’affaires régulières, en général pour des litiges de plus de 1 500 €. « Contrat de droit privé » n’a pas été relu.
3. Rétractation : le critère légal est le contrat « hors établissement », pas « hors de nos locaux ».
4. L’article L221-10 interdit de recevoir un paiement avant sept jours ; il n’interdit pas de démarrer. Le démarrage avant le quinzième jour suit l’article L221-25. [Mention du 11 novembre 2026 : voir la mention datée sous la correction 4.]
5. Le projet de bon de commande cède les droits sans les nommer un par un, sans lieu ni durée. La note (partie 1) demande l’inverse (CPI, art. L131-3).
6. Le projet de bon de commande écrit « aucun paiement n’est demandé » ; l’article L221-10 vise aussi le paiement reçu.

**Méthode.** Cinq appels pour cette note le 10 novembre 2026, dont deux partagés avec k2 (fiche F37365, facture électronique) et un échec (economie.gouv.fr, erreur 403). Quinze appels au total pour k1b, k2 et k3. Les autres points sont contrôlés dans le dépôt (k1a, partie « Vérification » ; `rj-R3-travail-contrats.md`). **L’outil de lecture résume les pages et ne rend que de courts extraits** : toute citation ci-dessous doit être relue sur la page avant un usage juridique.

### Tableau des contrôles

| # | Affirmation de la note | Verdict | Source et date |
|---|---|---|---|
| 1 | Pénalités au taux de la BCE majoré de 10 points ; indemnité forfaitaire de 40 € (partie 8) ; L441-10 « non relu » | confirmé ; une divergence | Légifrance, Code de commerce, art. L441-10, « En vigueur au 10/11/2026 », version du 26 avril 2019 (ord. n° 2019-359) : trente jours par défaut ; au plus soixante jours après la facture ou quarante-cinq jours fin de mois ; taux de la BCE majoré de 10 points, pas moins de trois fois le taux de l’intérêt légal ; pénalités « exigibles sans qu’un rappel soit nécessaire » ; indemnité due par « Tout professionnel en situation de retard de paiement », montant fixé par décret (D441-5 non relu). F23211 : « que sur des actes de commerce » (k1a, ligne 302) |
| 2 | « toutes les entreprises doivent être en capacité de recevoir des factures électroniques » depuis le 1er septembre 2026 (partie 8) | confirmé | impots.gouv.fr, actualité « Facturation électronique », 28/09/2026, lue le 10 nov. 2026. La page ne date pas l’émission des PME ; F31808, vérifiée le 11 août 2026 : 1er septembre 2027 (k1a, ligne 306) |
| 3 | Médiateur : « gratuit, rapide – moins de trois mois – et confidentiel » ; « tout différend lié à l’exécution d’un contrat de droit privé » ; rappel sous sept jours (partie 7) | confirmé en partie ; corrigé | F38216, « Prévenir et résoudre les litiges commerciaux grâce au Médiateur des entreprises », « Vérifié le 27 novembre 2024 » : « gratuit, rapide et confidentiel » ; « de quelques heures à 2 ou 3 mois maximum » ; médiateur « dans les 7 jours » ; relations d’affaires régulières ; litiges en général de plus de 1 500 €. Page economie.gouv.fr : erreur 403 |
| 4 | Responsabilité civile professionnelle non obligatoire en général (partie 6) | confirmé | F37365, version anglaise vue en résultat de recherche le 10 nov. 2026 : « not always mandatory », obligatoire pour certaines activités réglementées. Date « Vérifié le 07/07/2026 » relevée le 4 novembre (`rj-R3-travail-contrats.md`, ligne 286) |
| 5 | Rétractation si la commande est signée « hors de nos locaux » par une entité de cinq salariés au plus ; « ni encaissement ni démarrage avant sept jours » (partie 7 ; livrable 1) | corrigé | Code de la consommation, art. L221-3, Légifrance, en vigueur depuis le 1er juillet 2016, lu le 10 nov. 2026 (k1a, ligne 295) ; L221-10, L221-18 et L221-25 lus sur Légifrance le 9 nov. 2026 (k1a, ligne 312) : contrat « hors établissement » ; aucun paiement reçu avant sept jours ; démarrage anticipé sur demande « sur papier ou sur support durable » |
| 6 | Cession écrite, droit par droit, étendue, destination, lieu, durée ; cession globale des œuvres futures nulle (partie 1) | confirmé (dépôt) | CPI, art. L131-1 à L131-3, vérifiés le 4 nov. 2026 (`rj-R3-travail-contrats.md`, lignes 393 à 395) ; non relus ce jour |
| 7 | Code civil, art. 1794, 1231-5 et 1218 (partie 7) | non relu ce jour | lus sur Légifrance par la note ; le caractère supplétif de 1794 reste inconnu |
| 8 | L442-1 modifié par la loi n° 2026-796 du 18 août 2026 | non vérifié | page non relue (limite de recherches) |

### Corrections à appliquer

1. **Indemnité de 40 € (partie 8 ; « Ce qui n’a pas pu être vérifié »).** Retirer « Code de commerce, art. L441-10 (pénalités de retard) » des textes non relus. Ajouter : « L441-10, II (version du 26 avril 2019, lue le 10 novembre 2026) : l’indemnité forfaitaire est due par « tout professionnel en situation de retard de paiement » ; la fiche F23211 la limite aux actes de commerce. Pour une société civile, l’avocat tranche. »
2. **Médiation (partie 7).** Phrase trop large : « gratuit, rapide – moins de trois mois – et confidentiel », pour « tout différend lié à l’exécution d’un contrat de droit privé ». Phrase juste : « Le Médiateur des entreprises est gratuit, rapide et confidentiel. Une médiation dure de quelques heures à deux ou trois mois au plus ; un médiateur rappelle sous sept jours. Il intervient dans des relations d’affaires régulières, en général pour des litiges de plus de 1 500 €. » Source : F38216, vérifiée le 27 novembre 2024. Un premier cadrage n’est peut-être pas une relation régulière : la clause dit « chacun peut saisir », jamais « nous saisirons ».
3. **Rétractation (partie 7, « Deux pièges »).** Remplacer « si la commande est signée hors de nos locaux » par « si la commande est conclue hors établissement, par exemple chez le client ». Source : L221-3 ; `interne/offre-cadrage/2026-11-10-note-interne-offre-et-bon-de-commande.md`, ligne 20.
4. **Délais (« Ce que cela change », livrable 1).** Phrase fausse : « ni encaissement ni démarrage avant sept jours si la rétractation peut jouer ». Phrase juste : « aucun paiement demandé ni reçu avant sept jours (L221-10) ; aucun démarrage avant le quinzième jour sans demande du client sur papier ou sur support durable (L221-25) ».
   [Mention du 11 novembre 2026 : la fiche F23224 de Service Public Entreprendre (vérifiée le 11 août 2026) indique qu’aucune prestation ne peut être effectuée pendant les sept jours ; point à trancher par l’avocat ; d’ici là, aucun démarrage avant le huitième jour. Source : `audit/2026-11-11-audit-final/travaux/a8-pieces-jointes-du-bon-de-commande.md`, constat 24.]
5. **Cession (projet de bon de commande, condition 6).** La note est juste ; le bon ne l’applique pas : « lui sont cédés […] ; elle les utilise avec qui elle veut » ne nomme ni les droits, ni le lieu, ni la durée. Correction transmise à l’agent qui relit les documents client, sur le modèle de la première phrase proposée pour le livrable 1. Source : CPI, art. L131-3.
6. **Sept jours (projet de bon de commande, partie 5).** « Aucun paiement n’est demandé pendant les sept jours » devient « Aucun paiement n’est demandé ni reçu pendant les sept jours ». Source : L221-10 (« ne peut recevoir aucun paiement ») ; L242-7 punit le fait d’« exiger ou obtenir » (k1a, ligne 296).

### Sûr à reprendre

**Document client** (bon de commande, avec « Projet à faire relire par un avocat avant tout usage ») :

- « Factures payables sous huit jours. En cas de retard : pénalités au taux de refinancement de la Banque centrale européenne majoré de dix points, et indemnité forfaitaire de 40 € pour frais de recouvrement. » Source : Code de commerce, art. L441-10, II, Légifrance, lu le 10 novembre 2026.
- « Aucun paiement n’est demandé ni reçu pendant les sept jours qui suivent la signature. » Source : Code de la consommation, art. L221-10.
- « En cas de désaccord, chacun peut d’abord saisir le Médiateur des entreprises, service gratuit et confidentiel. » Source : F38216, vérifiée le 27 novembre 2024. Facultatif ; le tribunal reste à l’avocat.

**Interne seulement** :

- « Depuis le 1er septembre 2026, toutes les entreprises doivent pouvoir recevoir des factures électroniques ; les grandes entreprises et les ETI les émettent par une plateforme agréée. » Source : impots.gouv.fr, 28 septembre 2026.
- « Les pénalités de retard sont exigibles sans rappel ; leur taux ne peut être inférieur à trois fois le taux de l’intérêt légal. » Source : L441-10, II.
- « L’assurance de responsabilité civile professionnelle n’est pas obligatoire pour toute société ; elle l’est pour certaines activités réglementées. » Source : F37365.

### Ce qui reste inconnu

- L’entité qui signera pour GianLuca Carlone (forme, effectif, activité principale) : donc la rétractation et l’indemnité de 40 €.
- L’indemnité de 40 € face à une société civile (« tout professionnel » ou « actes de commerce ») ; l’article D441-5, non relu.
- Le caractère supplétif de l’article 1794 du Code civil ; dédit ou pénalité pour l’acompte gardé ; acompte ou arrhes entre professionnels.
- Ce que la loi du 18 août 2026 a changé au I de l’article L442-1.
- La page du Médiateur des entreprises sur economie.gouv.fr (erreur 403) ; le champ exact de son intervention pour un premier contrat.
- Les sanctions de la facture électronique (50 €, 15 000 €, 500 €, 1 000 €) : reprises du dépôt, non relues.
- L’usage sur la durée de confidentialité.

### Pages relues le 10 novembre 2026

- Légifrance, Code de commerce, art. L441-10, « En vigueur au 10/11/2026 » : https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000038414392
- impots.gouv.fr, « Facturation électronique », 28 septembre 2026 : https://www.impots.gouv.fr/actualite/facturation-electronique
- Service Public Entreprendre, F38216, vérifiée le 27 novembre 2024 : https://entreprendre.service-public.gouv.fr/vosdroits/F38216
- Service Public Entreprendre, F37365, version anglaise vue en résultat de recherche, date non affichée dans le résultat : https://entreprendre.service-public.gouv.fr/vosdroits/F37365
- Non lue : economie.gouv.fr, page du Médiateur des entreprises (erreur 403).
- Toutes ces lectures passent par un outil qui résume la page.
