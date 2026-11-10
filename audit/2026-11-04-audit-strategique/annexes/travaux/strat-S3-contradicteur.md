# Proposition du stratège « S3-contradicteur » : une offre plus petite, payée et mesurable, au lieu du pilotage global

Rédigée le 4 novembre 2026 au soir, en lecture seule, par le stratège S3 de l'audit Marwin Tech × GianLuca Carlone. Travail indépendant des autres stratèges : leurs fichiers n'ont pas été lus.

**Document interne.** Il contient des coûts, des marges, un plancher de négociation, des cibles de revenu et la stratégie des associés. Il ne doit pas être transmis à GianLuca Carlone. Seuls l'architecture des offres (section 4, sans les colonnes « coûts » et « marge »), le calendrier de paiement (section 5) et les principes de gouvernance (section 8) peuvent servir de base à un document client, après réécriture.

**Posture demandée.** Partir de l'hypothèse que l'offre actuelle répond mal au vrai besoin, examiner les alternatives et recommander la meilleure, même si elle s'éloigne de l'ambition de Morgan.

## Méthode, sources et conventions

**Bases.** Les quatre synthèses (`syn-sources.md`, `syn-portefeuille.md`, `syn-capacite-ia.md`, `syn-droit.md`), le mémo de marché `rj-R6-marche.md` et son contrôle `ver-R6-marche.md`, les consignes (`BRIEF-AGENTS.md`, `DEMANDE.md`) et la note de l'auditeur (`note-point-4-novembre-et-activites.md`), tous dans le dossier `audit-work/`. Quand un contrôleur corrige un lecteur ou un chercheur, la correction fait foi.

**Pièces d'origine rouvertes ce soir** (dépôt `Momolscode/Carlone`, `origin/main` = 7b46602, vérifié par `git log -1`) : offre:9-25, 104-130, 186-212, 240-250 ; acc:1-30, 50-70, 88-103 ; cop:7, 13-16, 57, 65 ; R:220, 248, 1469 ; audit:50-110 ; CAT:36-60 ; texte de PROP p. 1 ; diapositives `deck/slides/paiement.html`, `formules.html`, `proposition.html`, `garanties.html`, `laboratoire.html`, et `deck/deck.json:7`.

**Calculs** refaits en Python (`python3 -I`), scripts dans `[dossier de travail] s3-calc/` : `cout_jp.py` (coût complet d'une journée), `scenarios.py` (trois scénarios sur 12 mois), `marges.py` (marge par offre), `tresorerie.py` (encaissements et exposition).

**Aucune action extérieure** : aucun contact, aucune consultation en ligne, aucune modification hors de ce fichier.

**Codes.** [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou simulation ; [MM] résultat mesuré ; [IN] inconnu. Une [PR] sans autre précision est une proposition de ce document.

**Unité.** JP = journée-personne de 7 h ; deux personnes présentes une journée consomment deux JP (acc:53).

**Abréviations** (chemins relatifs au dépôt, sauf mention) :

| Abréviation | Pièce |
| --- | --- |
| offre | `interne/offre-marwin-tech-remuneration-et-collaboration.md` (2 nov.) |
| acc | `sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md` (29 oct.) |
| cop | `sources/chatgpt-pages/2026-11-04/carlone-offres-et-projets.md` (28 oct.) |
| ctx | `interne/contexte-projet-carlone.md` (4 nov.) |
| audit | `interne/audit-marwin-tech-carlone.md` (2 nov.) |
| CAT | `interne/offres-de-carlone-catalogue-crm.md` (2 nov.) |
| R | `interne/recueil-sessions-chatgpt-2026-11-04.txt` |
| PROP | `sources/propositions-de-collaboration.pdf` (18 oct.) |
| V5 | `interne/archives-marwin-tech/options-structure-remuneration-v5-2026-10-30.pdf` |
| LABO | `interne/laboratoire/audit-ia-robotique-2026-10-31.pdf` |
| PASS | `crm/PASSATION.md` |
| deck/ | copie du diaporama client, `[diaporama Offre Marwin Tech, copie du 4 nov.] ` |
| PR1 | branche `origin/claude/dossier-carlone-2026-11-04` (PR n° 1) |
| CORPUS | texte extrait de l'artefact OLSEN « Corpus des offres IA vendables » (20 août 2026), `scratchpad/sources-txt/artifact-corpus-offres-ia-vendables-2026-08-20.txt` |
| note | `audit-work/note-point-4-novembre-et-activites.md` |
| SS, SP, SC, SD | `audit-work/syn-sources.md`, `syn-portefeuille.md`, `syn-capacite-ia.md`, `syn-droit.md` |
| R6, vR6, R4, vR4, R5 | mémos et contrôles `audit-work/rj-R6-marche.md`, `ver-R6-marche.md`, `rj-R4-donnees-ia.md`, `ver-R4-donnees-ia.md`, `rj-R5-art-lieux.md` |

**Trois faits nouveaux intégrés.**
1. **Retrait de Medhi et de BOJ.ART** demandé par Morgan le 4 nov. (« Va juste falloir enlever Medhi/boj art de l'offre », note:25) [DR]. Seul le diaporama client a été corrigé : 11 vues (`deck/deck.json:7`) [FV]. Restent incohérents l'offre écrite (offre:22), STRATES v1.1, le vernissage (signé « avec Medhi, BOJ.ART », `pour-carlone/vernissage-strates-diaporama.pdf` p. 12) et le PDF de 13 diapositives de PR1 [FV] (SS a.2).
2. **Dépôt public FinanceScope/CRM-Carlone** : violation très probable de données personnelles [HY fort] (R4 (c)). Si la connaissance date du 2 nov. (audit:3, 15), le délai de 72 h pour notifier la CNIL expire le **5 nov.** à une heure inconnue [ES] (vR4 n° 7).
3. **Aucun contrat, aucune facture, aucune entité payeuse identifiée** [FV, constat négatif sur le dépôt] (SS § 0.2 ; offre:16).

---

## 1. Verdict en trois phrases

1. L'offre actuelle (20 ou 40 JP par mois à 15 000 ou 30 000 € HT pendant six mois, avec une option laboratoire à 30 000 € HT) vend un pilotage global qu'aucune parole de GianLuca Carlone ne demande, qu'aucune entité identifiée ne s'est engagée à payer et que Morgan et Mathys ne peuvent pas tenir : 20 JP prennent environ 80 % de leur temps disponible, 40 JP sont impossibles [DR, FV négatif, ES] (cop:65 contre acc:7 ; SC § 2.6).
2. Je recommande de ne pas présenter cette offre au prochain rendez-vous. Il faut vendre à la place un **cadrage court payé** (environ 6 500 € HT), puis deux lots qui produisent un résultat vérifiable chez lui : un **pilote de développement commercial** sur le CRM remis en conformité, et l'**outillage d'un suivi** repris par une personne qu'il désigne ou recrute. Un **socle d'exploitation** de 3 500 à 4 500 € HT par mois les prolonge ensuite. Le chiffre d'affaires réaliste est de 6 000 à 9 000 € HT par mois : moins que l'ambition, mais finançable, mesurable et réversible [PR, ES].
3. Si aucune entité n'a signé et payé ce cadrage six semaines après le rendez-vous, et au plus tard le 31 janvier 2027, il faut reporter, arrêter toute production gratuite et chercher d'autres clients. STRATES, le laboratoire, le vernissage robotisé et l'exploitation des lieux sont refusés en l'état [PR].

---

## 2. Diagnostic (dix points)

| N° | Constat | Code | Source |
| --- | --- | --- | --- |
| D1 | **Le besoin d'un pilotage global n'est pas démontré.** Aucune pièce ne rapporte une parole directe de GianLuca. Les « vingt jours par mois » sont attribués à GianLuca dans une page (cop:65) et à Morgan dans l'autre (acc:7), à partir du même brief du 28 oct. En une semaine, l'offre est passée d'une version « limitée à quatre jours mensuels » à 20, puis 40 JP, sans aucune demande tracée du client (acc:7 ; offre:13-16). | [DR] contradictoire ; [FV négatif] | SS § 0.1, DIS-1, PER-1 ; SP § 1.1 |
| D2 | **L'offre est née du besoin du vendeur.** Ses déclencheurs visibles sont tous côté Marwin : « faut quand même qu'il me paye ce monsieur », « une DGX Spark déjà en matériel ça serait sympa » (R:220), « Je préfère être prestataire ou salarié » (R:248). Les besoins rapportés du client portent sur des projets précis : vendre des œuvres aux entreprises de la Nièvre, ouvrir une galerie, peut-être un cabaret, réunir des artistes, faire appeler par Quali Contact (cop:7, 13-16). | [DR] | R:220, 248 ; cop:7, 13-16 |
| D3 | **L'acheteur est introuvable.** On ne connaît ni l'entité, ni le signataire, ni le payeur, ni le valideur, pour aucun projet. Les lieux (Vieux Relais, le M, « six bâtiments ») n'ont ni propriétaire ni exploitant établis. Un patrimoine déclaré ne prouve pas une trésorerie disponible. | [FV négatif] ; [DR] | SP § 2.1-2.2 ; SS U01-U03, U12 |
| D4 | **La capacité réelle est de 7 à 12 JP facturables par mois, 20 au mieux.** Les 20 JP de la formule de base demandent 78 à 83 % du temps disponible des deux associés : ce n'est pas « un mi-temps chacun » (offre:15). Les 40 JP demandent 140 à 145 % de ce temps. Morgan mène au moins une dizaine d'autres projets (OLSEN, Shelby, vente en ligne personnelle, Côme Millot…). On ignore la disponibilité de Mathys. | [ES] ; [FV] pour la liste des projets ; [IN] | SC § 0.3-0.4, § 2.6 ; note:9-17 |
| D5 | **Produire n'est pas livrer ni vendre.** Le CRM compte 500 fiches, mais 283 numéros sur 471 restent « à confirmer » et une seule fiche porte une date de vérification. Aucun appel, aucun rendez-vous et aucune vente ne sont constatés (cop:57). Côté OLSEN, 36 propositions et 72 brouillons ont été préparés, aucun n'a été envoyé (note:9). La vente, la maintenance dans la durée et la coordination de prestataires ne sont démontrées par aucune réalisation. | [FV] CRM ; [DR] OLSEN | SS h.1 ; SC § 0.1, § 1.3, § 7.2 |
| D6 | **Le taux tient, le volume et l'objet non.** 750 € HT par JP correspondent à peu près au coût complet d'une JP facturable (section 4.3) et à un PMO senior en région (550 à 760 €, R6 (a)). Mais 15 000 € HT par mois équivalent au coût employeur de 5,3 assistants ou de 2,4 chefs de projet cadres régionaux (R6 (b)). Le marché du temps partagé vend 2 à 8 jours par mois, pas 20 (R6 (e)). Enfin, la règle sur les gains d'automatisation a disparu le 2 nov. : dans une facturation au temps, chaque gain réduit le chiffre d'affaires (acc:66 contre `deck/slides/formules.html:30`). | [ES] ; [HY] marché ; [FV] disparition de la règle | R6 (a), (b), (e) ; vR6 n° 3 ; SS REM-1, REM-4 |
| D7 | **L'exploratoire a envahi l'offre, et la décision du 4 nov. n'est appliquée qu'au diaporama.** L'option laboratoire à 30 000 € HT reste dans le diaporama (`deck/slides/laboratoire.html:9`). Son « geste robotique » devait être le premier trait de STRATES (offre:84) : il n'a plus d'objet. STRATES n'a pas de budget propre. Le vernissage dépend du parc de Medhi. Au moins quatre supports contredisent encore la décision. | [FV] ; [DR] pour la décision | SS PER-2, PER-5, AVA-5 ; SP § 3.9-3.11 |
| D8 | **Le risque juridique est immédiat.** Il y a une violation de données probable, avec une échéance CNIL le 5 nov. si la connaissance date du 2 nov. GianLuca est présenté à la fois comme client, bailleur, employeur et investisseur. Les indices de requalification sont nombreux : client unique, bureaux du client, prix au temps, « s'occuper de tout ». Marwin n'est pas immatriculée : aucun encaissement n'est possible. | [ES] ; [DR] ; [HY] requalification ; [FV] règles | vR4 n° 7 ; SD § 0, § 3.1, § 4.2 |
| D9 | **Le calendrier de paiement se contredit.** Pour les mois 2 à 6, une version prévoit une facture de fin de mois payée sous 7 jours (acc:57), l'autre un paiement d'avance (offre:19 ; `deck/slides/paiement.html:26`). L'écart est d'environ 37 jours par échéance. Le titre « payé d'avance » est inexact pour le mois 1 (`paiement.html:4` contre `:18`). Le démarrage « à réception de l'acompte » (`paiement.html:10`) est impossible avant l'immatriculation. | [FV] ; [ES] écart | SS PAY-2 à PAY-4 |
| D10 | **La dépendance est totale, dans les deux sens.** Le chiffre d'affaires viendrait à 100 % d'une seule personne, qui fournirait aussi les bureaux et peut-être le capital. Morgan est le point de défaillance unique : il valide tout et détient les comptes. Mathys l'est pour le code du CRM. Les outils sont sur des comptes personnels, et plusieurs prélèvements échouent depuis fin octobre (note:8). La part maximale de revenus venant de GianLuca est restée sans réponse (« ( 10 millions », ctx:129). | [FV] / [DR] | SC § 3.3 ; SD § 4.4 ; audit:55 |

**Conséquence.** Le problème n'est pas d'abord le prix. L'offre répond à une question que le client n'a pas posée (« qui pilote tout ? »), avec une capacité que les associés n'ont pas, auprès d'un acheteur qui n'est pas identifié. La seule base concrète est un besoin commercial (vendre des œuvres) et un besoin de suivi (« ne pas gérer chaque détail », acc:13), tous deux rapportés par Morgan [DR].

---

## 3. Objectifs possibles et objectif principal recommandé

### 3.1 Six objectifs comparés

Notes qualitatives (fort, moyen, faible) : une note chiffrée serait une précision artificielle. Les montants sont des [ES] tirés des sections 4 et 6.

| Objectif | Valeur pour GianLuca | Chiffre d'affaires pour Marwin | Tenable à deux ? | Preuve disponible aujourd'hui | Principal risque | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| **O1. Devenir l'équipe de pilotage globale** (ambition de Morgan, DEMANDE § 2) | Forte si le portefeuille existe ; aujourd'hui, aucun objet vérifiable (aucun lieu ni entité identifiés) | 15 000 à 30 000 € HT par mois sur le papier | Non : 20 JP ≈ 80 % du temps, 40 JP impossibles | Aucune | Promesse trop large pour être réceptionnée ; requalification ; abonnement qui absorbe tout | **Différé.** À réexaminer au 6e mois, sur preuves |
| **O2. Développement commercial outillé** : le CRM et la prospection produisent des rendez-vous, puis des ventes, pour GianLuca | Forte et mesurable : c'est le seul chantier qui peut créer du chiffre d'affaires chez lui | 8 000 € HT pour le pilote, puis 4 000 à 6 000 € HT par vague de prospection | Oui (10 JP sur 6 à 8 semaines) | Fichier existant (500 fiches) [FV] ; aucun résultat d'appel [FV négatif] | Prérequis côté client : structure vendeuse, œuvres disponibles, avis fiscal, appelant désigné. Pas de commission pour Marwin (R5 (a)) | **Retenu**, après la mise en conformité |
| **O3. Outilleur pendant que GianLuca recrute un assistant** : Marwin installe le registre, les procédures et les outils sur ses comptes, puis forme la personne qui exécute | Forte : il garde l'organisation et paie l'exécution au prix d'un assistant (2 250 à 3 340 € par mois, R6 (b)) au lieu de 750 € par JP | 7 000 € HT pour l'outillage, puis un socle de 3 500 à 4 500 € HT par mois | Oui | Méthode de preuve et de restauration démontrée dans BOJART [FV/MM] (SC § 1.1) | GianLuca ne recrute pas ; Marwin glisse alors vers l'exécution administrative | **Retenu** |
| **O4. Mission limitée** : cadrage payé, puis décision | Moyenne : un dossier de décision, et non un résultat | Environ 6 500 € HT, une seule fois | Oui (8 JP) | Forfait borné déjà conçu le 25 oct. (R:1469) [PR] | Marwin reste un fournisseur d'études | **Retenu comme première étape** |
| **O5. Plusieurs prestataires** : GianLuca contracte directement avec Quali Contact (appels), son expert-comptable, son avocat et un organisateur local ; Marwin n'est que l'un d'eux | Forte : spécialistes payés à leur prix, moins de dépendance | Plus faible, mais plus sûr | Oui | Quali Contact existe et est établi à Cosne [FV] (vR6 n° 8) ; il est spécialisé dans la collecte de dons [FV] | Coordination diffuse ; personne pour relier les sujets | **Retenu comme principe d'organisation** : Marwin coordonne la documentation, il ne commande pas les autres |
| **O6. Report ou refus** | Nulle à court terme | Nul | — | — | Perte de la relation ; travail gratuit déjà fourni non valorisé | **Scénario de repli** si les conditions de la section 10 ne sont pas réunies |
| *(O7. Indépendance de Marwin : un « kit » CRM et suivi vendu à d'autres entreprises de la Nièvre)* | — | 2 000 à 4 000 € HT par mois et par client, dès le 5e ou 6e mois | Oui, si le kit est réutilisable | Recommandé par l'audit du 2 nov. (audit:103, solution 11 ; deuxième client « d'ici le mois 4 », audit:55) [PR] | Dispersion de Morgan, déjà sur dix projets | **Retenu comme objectif secondaire** |

**Comparaison des coûts mensuels pour GianLuca** [ES] :

| Formule | Coût mensuel |
| --- | --- |
| Offre actuelle, base | 15 000 € HT, soit 18 000 € TTC (offre:13) |
| Offre actuelle, renforcement | 30 000 € HT |
| Organisation recommandée | Socle Marwin (≈ 4 000 € HT) + assistant salarié (2 250 à 3 340 € de coût employeur, R6 (b), vR6 n° 3) + appels payés au rendez-vous (150 à 500 € HT par rendez-vous tenu, R6 (c), source secondaire [DR]), soit environ 7 000 à 9 000 € par mois, plus des lots ponctuels |

GianLuca peut faire ce calcul lui-même (R6 (b)). Il vaut mieux le lui présenter que le lui laisser découvrir.

### 3.2 Objectif principal recommandé [PR]

> **Dans les 90 jours qui suivent la signature, livrer à une entité identifiée de GianLuca Carlone une organisation commerciale et de suivi qui fonctionne chez lui sans Marwin au quotidien.** Elle comprend :
> - un CRM conforme, hébergé à son nom ;
> - un pilote de prospection mesuré sur 20 à 40 comptes ;
> - un registre des décisions et des procédures repris par la personne qu'il désigne ou recrute.
>
> **Ce travail doit être facturé à un prix qui couvre le coût complet de Marwin, et au plus 80 % du chiffre d'affaires de Marwin doit venir de GianLuca au 12e mois.**

Cet objectif s'éloigne de l'ambition « nous pilotons tout » : Marwin devient l'**outilleur et le pilote léger** de l'organisation de GianLuca, et non son exécutant. Il garde pourtant la porte ouverte à O1. Si, au 6e mois, le registre montre un portefeuille réel, plusieurs entités, une charge mesurée de plus de 12 JP par mois et des paiements à l'heure, une formule récurrente plus large pourra être proposée sur preuves.

### 3.3 Ce que Marwin contrôle, ce qui dépend de GianLuca

| Sous le contrôle de Marwin | Dépend de GianLuca Carlone (ou de tiers) |
| --- | --- |
| Traiter la fuite de données et décider de la notification, avec un avocat ou un DPD (si Morgan et Mathys sont responsables de fait, SD § 9.1) | Désigner l'entité qui signe, paie, valide et devient responsable du traitement |
| Mettre en cohérence tous les documents après le 4 nov. ; fermer PR1 ou en marquer le PDF comme historique | Accepter un cadrage payé au lieu d'un abonnement |
| Disponibilités nominatives, pacte, immatriculation, RC professionnelle, compte bancaire, facturation électronique | Fournir les accès et les interlocuteurs sous 10 jours ouvrés |
| Qualité des fiches CRM, délais, taux de corrections, restaurations testées, absence d'incident | Nommer la structure vendeuse ; fournir des œuvres disponibles avec leurs prix ; obtenir l'avis fiscal écrit de son conseil |
| Kit de campagne conforme ; mesure honnête du pilote | Désigner qui appelle (lui, un assistant ou Quali Contact) ; payer Quali Contact |
| Fiche de poste, procédures, formation | Recruter ou désigner un assistant |
| Prospection d'un second client | Rendez-vous tenus, ventes, décisions prises à temps : **résultats qu'on suit, mais qu'on ne promet pas** |
| Refuser ce qui sort du périmètre | Faire une offre de bureaux, d'emploi ou d'investissement : chacune dans un accord séparé |

---

## 4. Architecture des offres

### 4.1 Vue d'ensemble

Le schéma suit le principe « contrat-cadre et fiches de mission » du 30 oct. (V5 p. 2, 4), abandonné le 2 nov. (SS PER-6). Chaque offre a son prix, sa réception et sa condition de poursuite. **Aucune ne contient implicitement les autres** (DEMANDE § 4).

| Code | Offre | Nature du prix | Capacité | Durée | Prix proposé [PR] |
| --- | --- | --- | --- | --- | --- |
| 0 | Remise en ordre (fuite, conformité, cohérence des documents) | **Non facturée** : l'exposition est de notre fait | 4 à 8 JP | Novembre 2026 | 0 € |
| A | Cadrage et décision | Forfait | 8 JP | 3 à 4 semaines | 6 500 € HT (fourchette de négociation : 6 000 à 7 500 €) |
| B | Pilote de développement commercial (CRM) | Forfait | 10 JP | 6 à 8 semaines | 8 000 € HT |
| C | Outillage du suivi et passation à la personne désignée | Forfait | 9 JP | 4 à 6 semaines, puis 30 jours d'accompagnement | 7 000 € HT |
| D | Socle d'exploitation | Abonnement borné, par processus exploité | 4 à 5 JP par mois (référence) | 3 mois minimum, puis au mois | 4 000 € HT par mois (3 000 € en version légère) |
| E | Lots devisés | Forfait par lot | 4 à 10 JP par lot | Selon le lot | 4 000 à 8 000 € HT par lot |
| F | Régie et urgences | Au temps, sur bon écrit | Résiduelle | — | 750 € HT par JP ; demi-journée minimale |

### 4.2 Fiches des offres

#### Offre 0 : remise en ordre (non facturée)

| Rubrique | Contenu |
| --- | --- |
| Client | Aucun : obligation de Marwin et de ses associés |
| Problème | Données de prospects exposées dans un dépôt public [HY fort] ; documents destinés au client contradictoires avec la décision du 4 nov. [FV] ; CRM présenté comme « livré » alors qu'il n'est ni conforme ni réellement utilisé (SS AVA-1) |
| Résultat | Fiche de violation tenue ; décision de notification prise et tracée avec un avocat ou un DPD ; dépôt privé, copies vérifiées. Un seul jeu de documents à jour, les autres marqués « historique ». CRM hébergé en privé, oppositions appliquées, simulateur fiscal corrigé (prise en compte du bénéfice et du taux PME : `crm/art_merge.py:19, 129`, SP § 3.1) |
| Périmètre | Ce qui précède, et l'information écrite de GianLuca sur l'incident (SD § 9.3) |
| Exclusions | Toute nouvelle production pour le client |
| Dépendances | Avocat ou DPD (honoraires [IN]) ; Mathys, titulaire présumé du dépôt [DR] |
| Capacité | 3 à 6 JP pour la fuite et la conformité ; 1 à 2 JP pour la cohérence (SC § 2.5) [ES] |
| Coût | ≈ 2 000 à 6 500 € de temps au coût complet, plus les honoraires du conseil [ES] |
| Réception | Critères 1 à 3 de SP § 3.1 (dépôt privé, violation documentée, responsable désigné) |
| Poursuite | Condition préalable à toute offre qui touche des données réelles |

#### Offre A : cadrage et décision

| Rubrique | Contenu |
| --- | --- |
| Client | L'entité de GianLuca qui signe le bon de commande (dénomination, SIREN, signataire habilité). À défaut d'entité, pas de commande (SP § 2.3, règle de prudence) |
| Problème | Personne ne sait aujourd'hui quelles entités, quels lieux et quels projets existent, ni ce que GianLuca veut déléguer, garder et payer (D1, D3) |
| Résultat | 1. Inventaire signé des entités, lieux, projets, interlocuteurs et accès. 2. Trois priorités à 90 jours, choisies par lui, chacune avec son budget. 3. Carte des intervenants : qui fait quoi parmi Marwin, l'assistant, Quali Contact, l'expert-comptable et l'avocat. 4. Décision écrite sur le CRM : exploiter ou non, au nom de quelle structure, qui appelle. 5. Grille de délégation : décisions gardées, plafonds, valideur. 6. Recommandation chiffrée des lots suivants |
| Périmètre | Deux entretiens d'environ 2 h (le premier avec les deux associés, le second avec un seul) ; analyse de 15 pièces au plus ; un atelier de restitution ; un rapport d'environ 10 pages et ses annexes |
| Exclusions | Toute production (supports, CRM, automatisations) ; tout contact avec un tiers en son nom ; tout conseil fiscal ou juridique ; toute étude de lieu sur place au-delà d'une visite |
| Dépendances | Marwin immatriculée ; entité cliente identifiée ; pièces fournies sous 10 jours ouvrés. Si GianLuca est éligible à l'aide régionale au conseil, le dossier doit être déposé **avant** la signature [DR] (R:755, 809) : cette séquence décale le démarrage |
| Capacité | 8 JP : 5 pour Morgan (entretiens, priorités, grille de délégation), 3 pour Mathys (inventaire des accès, décision sur le CRM) |
| Durée | 3 à 4 semaines calendaires |
| Prix et justification | **6 500 € HT** (≈ 810 € par JP). *Coût complet* : 500 à 810 € par JP dans le scénario central (section 4.3). *Marché* : un cadrage court au forfait est le format que soutient le marché (R6 (e)). Le Diag Data IA est plafonné à 10 000 € HT pour 8 jours et laisse 6 000 € à la charge d'une PME éligible (vR6 n° 6 : c'est un plafond de devis, pas un prix constaté). Un PMO senior en région coûte 550 à 760 € par jour (R6 (a)). *Valeur* : le cadrage évite d'engager 90 000 € HT sur un périmètre non dimensionné |
| Coûts directs | Déplacements : 100 à 300 € [ES], selon les lieux, qui sont [IN] |
| Marge | Après rémunération cible des associés : environ 0 à 35 % selon la cible (2 500 ou 3 660 € nets par ETP) [ES] (`marges.py`) |
| Réception | Inventaire et priorités **signés** par GianLuca ou son valideur. Sans réponse, la réception n'est prononcée **que pour le paiement**, 10 jours ouvrés après une relance écrite. Aucune décision du rapport ne vaut accord tacite (section 8) |
| Conditions de poursuite | Au moins un lot (B ou C) commandé ; accès fournis ; valideur nommé. Sinon, la relation s'arrête au cadrage, sans travail gratuit en attendant |

#### Offre B : pilote de développement commercial sur le CRM

| Rubrique | Contenu |
| --- | --- |
| Client | La structure qui vend les œuvres (U11), nommée dans chaque message (PASS:31) |
| Problème | GianLuca veut vendre des œuvres aux entreprises de la Nièvre [DR] (cop:13). Le fichier existe, mais il n'est ni fiable (283 numéros sur 471 à confirmer), ni conforme, ni utilisé. On ignore si la cible achète |
| Résultat | Entre 20 et 40 comptes qualifiés (source et date pour chaque champ) ; un kit de campagne validé par son conseil (script, e-mail, fiche d'offre « œuvre exposée », CAT:42) ; les résultats d'appel réimportés ; un rapport mesuré (joignabilité, rendez-vous, refus, oppositions, temps humain par fiche) [MM à produire] ; une recommandation d'extension ou d'arrêt |
| Périmètre | Préparation (2 semaines) ; appui pendant 4 semaines d'appels (réimport hebdomadaire, ajustement du script) ; bilan. Les comptes sont tirés des 37 cibles et des 57 fiches de priorité haute, entreprises seulement, sans entrepreneurs individuels ni lignes personnelles avant l'avis de l'avocat (SC § 6.2) |
| Exclusions | Les appels et les rendez-vous eux-mêmes ; la vente ; toute commission ; tout encaissement ; le conseil fiscal ; le connecteur Hermes360 ou Quali Contact tant qu'aucun modèle de fichier réel n'existe (SC § 5.5, « arrêter ») ; tout agent vocal sortant |
| Dépendances | Offre 0 terminée ; responsable du traitement désigné et contrat de l'article 28 signé ; avis fiscal écrit (238 bis AB valable pour les achats faits avant le 31 déc. 2028 [FV], vR2 n° 1 ; exposition en galerie commerciale non couverte par le BOFiP, SD § 2 n° 24) ; au moins 5 à 10 œuvres réellement disponibles, avec prix et artiste vivant [IN] ; appelant désigné : GianLuca, l'assistant ou Quali Contact, qui facture directement GianLuca |
| Capacité | 10 JP : 6 pour Mathys (données, outil, réimport), 4 pour Morgan (kit, bilan) |
| Durée | 6 à 8 semaines |
| Prix et justification | **8 000 € HT** (≈ 800 € par JP). *Coût* : section 4.3. *Marché* : un téléprospecteur externalisé coûte 3 000 à 8 000 € par mois, avec un engagement de 6 mois au moins (R6 (c), source secondaire [DR]) ; ici, Marwin ne fournit pas les appels. *Valeur* : une seule vente d'œuvre à une entreprise peut dépasser ce montant. Le plafond de déduction est de 20 000 € par an ou 5 ‰ du CA, et le prix déductible va jusqu'à 100 000 € sur cinq ans (CAT:56-60) [HY sur la conversion] |
| Coûts directs | API de recherche : 10 à 50 € ; téléphonie, si l'appelant en a besoin, à la charge du client (SC § 6.2) |
| Marge | Environ 0 à 35 % [ES] |
| Réception | Au moins 90 % des champs de contact sourcés et datés ; 100 % des oppositions respectées ; aucun argument fiscal non validé ; résultats d'au moins 90 % des appels réimportés (SC § 6.2) |
| Conditions de poursuite | Seuils fixés **avant** l'essai, avec GianLuca. Repère proposé [HY] : joignabilité d'au moins 50 % et au moins quelques rendez-vous tenus sur la vague. Si les seuils sont atteints : extension par vagues (offre E). Sinon : changer de source ou de cible, ou arrêter. Les ventes sont suivies à part : elles dépendent de lui et des œuvres |

#### Offre C : outillage du suivi et passation à la personne désignée

| Rubrique | Contenu |
| --- | --- |
| Client | L'entité de GianLuca qui emploiera l'assistant, ou qui désigne un salarié existant |
| Problème | « Ne pas gérer chaque détail » (acc:13) [DR], sans payer de l'exécution administrative à 750 € par JP. L'audit du 2 nov. le disait déjà : « Marwin outille et pilote, une personne recrutée par Carlone ou un prestataire local exécute » (audit:83, 100) [PR] |
| Résultat | Un registre des décisions et des échéances ; un tableau de bord ; des modèles d'ordre du jour et de compte rendu ; 5 à 8 procédures écrites pour les tâches récurrentes repérées au cadrage, chacune avec sa fiche de secours manuel ; tous les comptes ouverts **au nom de l'entité cliente** ; une fiche de poste et une grille d'entretien pour l'assistant ; deux séances de formation ; un premier test de restauration |
| Périmètre | Processus 2, 3 et 11 de SC § 5 (réunions, échéances, capitalisation), avec les options « organisation simple » et « outils existants configurés » seulement (SC § 5.12) |
| Exclusions | Le recrutement lui-même (sélection, contrat de travail, paie) ; l'exécution des tâches ; la tenue de la comptabilité ; tout développement spécifique ; l'usage du nom « Jarvis » (propriété non réglée, SS PRO-2) |
| Dépendances | Décision de GianLuca de recruter ou de désigner une personne ; accès ; offres d'IA professionnelles avec analyse d'impact des transferts si des données personnelles sont traitées (SD § 9.6) |
| Capacité | 9 JP : 5 pour Mathys (outils, comptes, restauration), 4 pour Morgan (procédures, formation) |
| Durée | 4 à 6 semaines, puis 30 jours d'accompagnement, compris |
| Prix et justification | **7 000 € HT** (≈ 780 € par JP). *Valeur* : GianLuca paie ensuite l'exécution au coût d'un assistant (27 à 40 k€ par an, R6 (b)) et non 180 000 € par an. *Coût* : section 4.3 |
| Coûts directs | Outils au nom du client, payés par lui : environ 40 à 130 € par mois (SC § 5.12) |
| Marge | Environ 0 à 35 % [ES] |
| Réception | La personne désignée utilise le registre pendant 4 semaines consécutives ; elle traite au moins 80 % des comptes rendus ; une restauration est réussie ; les exports sont remis |
| Conditions de poursuite | Si personne n'est désigné à la fin du lot, Marwin **ne reprend pas** l'exécution au taux de 750 € : le socle (offre D) reste limité au pilotage |

#### Offre D : socle d'exploitation

| Rubrique | Contenu |
| --- | --- |
| Client | L'entité signataire du contrat-cadre |
| Problème | Garder dans la durée un suivi fiable, des outils maintenus et des décisions préparées, sans abonnement fourre-tout |
| Résultat (liste fermée) | Exploitation et maintenance des outils livrés (registre, CRM hébergé chez le client) ; sauvegardes, avec une restauration testée chaque mois au premier trimestre, puis chaque trimestre ; un comité mensuel avec un associé et deux points courts ; un tableau de bord mensuel ; la détection des incohérences et des retards ; l'appui à l'assistant (environ 2 h par semaine) ; deux dossiers de décision par mois au plus (étude de rentabilité simple, comparaison de devis) |
| Exclusions | Tout ce qui n'est pas dans la liste : production de contenus, campagnes, événements, développements, urgences hors plages. Ces travaux passent en lot (E) ou en régie (F) |
| Dépendances | Offre C livrée, ou outils équivalents ; valideur nommé |
| Capacité | 4 à 5 JP de référence par mois. C'est une **capacité de référence**, pas un compteur facturé : le prix ne baisse pas si l'automatisation réduit le temps (section 4.6) |
| Durée | 3 mois minimum, puis reconduction mensuelle, préavis d'un mois des deux côtés. C'est la doctrine de Morgan lui-même : « Un contrat qui se résilie quand on veut se vend mieux et se renouvelle plus longtemps » (CORPUS:749) [DR] |
| Prix et justification | **4 000 € HT par mois** (≈ 800 € par JP de référence) ; version légère à 3 000 € HT pour 3 à 4 JP. *Marché* : forfaits mensuels bornés de 400 à 8 000 € pour les fonctions récurrentes (DPO externalisé, DAF à temps partagé, R6 (e), sources secondaires). *Responsabilité* : Marwin porte la maintenance, les sauvegardes et la réversibilité, quel que soit le temps passé |
| Coûts directs | ≈ 100 € par mois (part des outils propres à Marwin) [ES] |
| Marge | Environ 0 à 35 % [ES] |
| Réception | Rapport mensuel remis le 5 ouvré ; indicateurs de SC § 4 (attente, retards, corrections, incidents) |
| Conditions de poursuite | Paiements à l'heure ; décisions du client sous 10 jours ouvrés en moyenne ; aucun incident critique ; occupation des associés d'au plus 85 % |

#### Offre E : lots devisés (exemples)

| Lot | Condition préalable | Capacité | Prix indicatif [PR] |
| --- | --- | --- | --- |
| Extension commerciale, par vague de 50 à 100 comptes | Pilote B concluant | 5 à 7 JP | 4 000 à 6 000 € HT par vague |
| Catalogue privé des œuvres (PROP p. 1, mission 6) | Œuvres réelles, photos et provenance fournies | 6 à 10 JP | 5 000 à 8 000 € HT |
| Dossier de faisabilité d'un premier événement **sans robot**, l'organisateur légal étant l'entité de GianLuca | Lieu, date et jauge connus ; au moins deux mois avant l'événement pour les démarches (R5 (d)) | 5 à 8 JP | 4 000 à 6 500 € HT |
| Inventaire des lieux et tableau des obligations par lieu | Propriétaire et exploitant identifiés | 4 à 6 JP | 3 500 à 5 000 € HT |
| Étude de rentabilité d'un rachat ou de travaux (PROP p. 1, mission 2) | Données du vendeur ou des devis | 3 à 5 JP | 2 500 à 4 000 € HT |

Pour chaque lot : un bon de commande, des critères de réception écrits **avant** le démarrage, et un calendrier de paiement de type « lot » (section 5).

#### Offre F : régie et urgences

- **750 € HT par JP**, sur bon de commande écrit avant le travail, avec une demi-journée minimale [PR].
- **Pas d'astreinte 24 h sur 24.** Une astreinte hors des plages convenues n'est proposée que sur demande, avec un forfait chiffré à part (acc:59, 105) [PR].
- Une intervention urgente hors plages est majorée de 50 % [PR, à discuter].

#### Hors catalogue, refusé en l'état [PR]

- **Le pilotage global à 20 ou 40 JP par mois**, et l'« ancre » de 46 JP (offre:246).
- **STRATES, Éclosion, l'option laboratoire et la DGX Spark.** Aucun financeur écrit, aucun objet depuis le 4 nov., aucune compétence robotique démontrée (SP § 3.10-3.11 ; LABO p. 9).
- **Le vernissage « signature » avec un bras robotisé**, qui expose une machine au public (SD § 2 n° 22).
- **L'exploitation des lieux et du cabaret.** Les licences et autorisations sont nominatives, au nom de l'exploitant (R5 (e)).
- **L'intermédiation dans la vente d'œuvres, toute commission sur les ventes et tout encaissement pour le compte du client** (LCB-FT, droit de suite : R5 (a)).
- **La tenue de comptabilité, le conseil fiscal ou juridique, la gestion immobilière, la vente de séjours** (SD § 4.7).
- **Toute collaboration avec Medhi ou BOJ.ART dans l'offre.**

### 4.3 Coût complet d'une journée et ce que devient le taux de 750 € HT

**Calcul** [ES] (`cout_jp.py`). Le coût complet d'une JP facturable comprend la rémunération chargée des associés au prorata de leur temps pour Marwin, plus les frais fixes de 1 500 à 2 500 € par mois [HY]. On le divise par la capacité facturable de SC § 2.3.

| Scénario de disponibilité | JP facturables par mois | Cible de 2 500 € nets par ETP (plancher, offre:112-114) | Cible de 3 660 € nets par ETP (base, offre:110) |
| --- | --- | --- | --- |
| Prudent (Morgan 50 %, Mathys 25 %) | ≈ 7 | 630 à 775 € par JP | 885 à 1 030 € par JP |
| Central (65 % et 50 %) | ≈ 12 | 500 à 580 € par JP | 725 à 810 € par JP |
| Haut (90 % et 90 %) | ≈ 20 | 425 à 475 € par JP | 640 à 690 € par JP |

Hypothèses du calcul : un ETP coûte environ 3 890 € par mois pour 2 500 € nets (60 000 € nets + 33 332 € de cotisations et d'IR pour deux, offre:114), et environ 6 250 € pour 3 660 € nets (offre:110, 114 : 180 000 € moins 30 000 € de frais, partagés entre deux). Ces bases viennent du modèle SARL de V5 et restent à faire valider par un expert-comptable.

**Lecture.**
- **750 € HT par JP n'est ni trop cher ni suffisant.**
  - Dans le scénario central, ce taux couvre le coût complet avec une marge de 23 à 34 % si la cible est de 2 500 € nets par ETP. Il arrive tout juste à l'équilibre (−8 % à +3 %) pour 3 660 € nets.
  - Il ne finance **jamais** l'objectif de 7 500 € nets chacun (offre:118).
  - Le plancher de 10 278 € par mois (offre:112-114 ; SS h.1) demande 13,7 JP facturés à 750 € : c'est plus que la capacité centrale.
- **Côté marché**, ce taux se situe en haut de la fourchette des PMO en région (550 à 760 €) et sous les repères de direction à temps partagé (800 à 1 500 €) (R6 (a)). Il est **indéfendable pour de l'exécution administrative** (R6 (b)).

**Ce que devient le taux [PR].**
1. **Il cesse d'être le prix affiché.** On retire « Un seul taux » (`deck/slides/formules.html:4`) et « On ajuste le périmètre […] pas le taux » (offre:18). Le client voit des **forfaits par résultat** et un socle par processus.
2. Il devient le **taux de référence interne** pour chiffrer les forfaits : JP estimées × 750 à 850 €, plus une provision de risque de 10 à 15 % sur les lots dont le périmètre est incertain.
3. Il reste le **taux de régie**, réservé aux travaux de coordination, d'analyse ou d'outillage. Aucune tâche d'exécution n'est vendue par Marwin, à aucun taux.
4. Il sera revu à la hausse seulement sur preuve : références client réceptionnées, gains mesurés. La règle de l'audit (« ne pas baisser le taux », audit:85) reste valable, mais elle s'applique désormais aux forfaits.

### 4.4 Règle anti-double facturation [PR]

1. **Une tâche n'a qu'une ligne.** Chaque tâche figure dans une seule ligne du contrat : socle, lot ou régie. Le rapport mensuel liste chaque tâche avec sa ligne.
2. **Le socle est une liste fermée.** Tout ce qui n'y figure pas exige un bon de commande écrit **avant** de commencer.
3. **Pas de transfert entre lignes.** Le temps passé sur un lot ne s'impute jamais sur le socle, et inversement.
4. **On ne facture pas deux fois une automatisation.** La construction se paie dans un lot, une fois. L'exploitation se paie dans le socle. La correction des défauts de Marwin est gratuite pendant 60 jours après la réception.
5. **Non facturable, toujours** : la remise en ordre (offre 0), les corrections de nos erreurs, nos outils internes, notre administration, notre prospection, la mise en cohérence après le 4 nov., et le CRM « offert », que l'on ne refacture jamais rétroactivement (offre:227).
6. **Outils** : les abonnements au nom du client sont payés par lui. Les outils de Marwin sont dans ses frais. Aucune refacturation avec marge sans accord écrit.
7. **Tiers** : Quali Contact, l'expert-comptable, l'avocat et les artistes facturent directement l'entité de GianLuca. Marwin ne refacture ni ne revend leurs prestations.
8. **Deux associés en réunion** : on compte deux JP seulement si le bon de commande prévoit la présence des deux. Sinon, une seule (SC § 2.4).

### 4.5 Exemple : ce que coûte l'organisation recommandée pour GianLuca la première année [ES]

Scénario central de la section 6 :
- Marwin : environ 94 000 € HT sur 12 mois, dont environ 80 000 € venant de lui une fois retiré le second client (≈ 14 000 €).
- Un assistant : 27 000 à 40 000 €.
- Les appels : à la carte.

L'offre actuelle demandait 90 000 € HT pour **six** mois, sans assistant ni appels (offre:16).

### 4.6 Rémunérer la responsabilité et la valeur quand l'automatisation réduit le temps [PR]

| Mécanisme | Règle | Pourquoi |
| --- | --- | --- |
| **Forfait par livrable** (A, B, C, E) | Prix fixe, indépendant du temps réellement passé. Marwin garde le gain de productivité et porte le risque de dépassement | C'est la seule façon de ne pas être pénalisé par ses propres gains (SC § 6.5) |
| **Socle = exploitation de processus** (D) | Prix par processus exploité, avec un niveau de service. Il ne baisse pas pendant le contrat si le temps baisse. Le temps libéré sert à absorber un processus de plus, à capacité égale, sur proposition de Marwin | Retire la clause « ajuster le forfait » de V5 p. 4, contraire à DEMANDE § 11 (SD § 2 n° 18) |
| **Responsabilité** | Une part du socle (environ un quart [HY]) rémunère la maintenance, les sauvegardes, les restaurations, la réversibilité et l'astreinte des plages convenues | Ces obligations existent même un mois calme |
| **Économies réalisables** | Si une automatisation fait disparaître un coût que GianLuca payait vraiment (sous-traitance arrêtée, heures supplémentaires évitées), une prime égale à 20 à 30 % de l'économie **mesurée**, versée pendant 12 mois et plafonnée [PR] | Distingue le temps économisé de l'économie réelle (SC § 6.5) |
| **Variable** | Au plus 10 à 15 % du socle, lié à des indicateurs que Marwin contrôle : délais, taux de corrections, absence d'incident. **Jamais** un pourcentage sur les ventes d'œuvres. Une prime par rendez-vous tenu n'est envisageable qu'après l'avis de l'avocat (R5 (a) ; SD § 10.6 n° 5) | Évite le statut d'intermédiaire, la LCB-FT et le droit de suite |
| **Renouvellement** | À la reconduction, les gains mesurés sont présentés au client. Il choisit entre un processus de plus et une baisse négociée. Aucune baisse automatique | La valeur est partagée de façon visible, sans fausses heures (acc:66) |

---

## 5. Calendrier de paiement (la contradiction entre avance et fin de mois est tranchée)

**Décision proposée [PR] : les travaux récurrents se paient d'avance, et les lots ont leur propre échéancier.** On abandonne l'acompte de 7 500 € HT de l'offre de 90 000 € et la version « fin de mois sous 7 jours » (acc:57).

| Offre | Échéancier | Délai |
| --- | --- | --- |
| A Cadrage | 50 % à la commande, 50 % à la remise du rapport | Sous 8 jours |
| B, C, E (lots) | 40 % à la commande, 60 % à la réception. Au-delà de 6 000 € HT : 40 %, puis 30 % à un jalon intermédiaire écrit, puis 30 % à la réception | Sous 10 jours |
| D Socle | **Terme à échoir** : facture émise le 25 du mois précédent, payable le 1er. Le premier mois se paie à la signature | Le 1er du mois |
| F Régie | Terme échu, en fin de mois | Sous 15 jours |

**Règles communes.**
- **Rien n'est encaissé avant l'immatriculation.** Si un acte doit être signé avant, il l'est « au nom de la société en formation » et repris (SD § 3.1).
- TVA facturée dès la première facture (SD § 3.2). Exemples : socle de 4 000 € HT = 4 800 € TTC ; cadrage de 6 500 € HT = 7 800 € TTC.
- Retard de paiement : relance le lendemain de l'échéance. **Suspension des travaux** si la relance reste sans effet après 8 jours (offre:207). Pénalités d'au moins 3 fois le taux légal et indemnité de 40 € (SD § 3.2).
- La réception tacite ne vaut **que pour le paiement** d'un livrable, 10 jours ouvrés après une relance écrite. Elle ne vaut jamais pour une décision, une dépense ou un engagement (section 8).
- Sortie : un mois de socle payé d'avance reste dû pendant le préavis. Si Marwin résilie sans faute du client, elle rembourse au prorata.

**Justification.**
- Marwin n'a ni trésorerie, ni historique de paiement avec ce client, ni payeur identifié. GianLuca dispose, selon Morgan, de moyens importants [DR]. L'asymétrie de risque justifie l'avance sur le récurrent.
- Avec l'offre d'origine en version « fin de mois sous 7 jours », Marwin aurait avancé environ 18 500 € HT de travail par échéance [ES].
- Avec le calendrier proposé, l'exposition maximale du scénario central est d'environ **9 000 € HT** : à la fin du 3e mois, quand deux lots s'achèvent avant leur réception. Elle reste ensuite à 5 000 € HT au plus [ES] (`tresorerie.py`).

**Concession possible.** Si GianLuca refuse l'avance sur le socle, on peut passer à une facturation de fin de mois payable sous 7 jours, mais seulement :
- après trois échéances payées à l'heure ;
- et avec une suspension automatique à J+8.

**Réserve de démarrage** à apporter par les associés (capital entièrement libéré et comptes courants) : environ **8 000 à 12 000 €** [ES]. Elle couvre :
- les frais de création (statuts et pacte : 2 000 à 5 000 € HT, SD § 1.7 [HY]) ;
- deux mois de frais fixes ;
- l'exposition maximale sur les lots.

**Tests de défaillance (scénario central)** [ES] :

| Test | Effet | Parade |
| --- | --- | --- |
| Retard de 30 jours | Suspension à J+8 ; perte d'environ 1 mois de socle | Réserve de démarrage |
| Retard de 60 ou 90 jours | Travail arrêté depuis J+8 ; créance d'environ 4 000 à 9 000 € HT | Pénalités ; injonction de payer [HY] ; aucun nouveau lot |
| Rupture après trois mois | Perte de 70 à 90 % du CA | Préavis d'un mois ; second client visé dès le 5e ou 6e mois |
| Associé indisponible plusieurs semaines | Capacité facturable de 4 à 8 JP | Clause de report sans pénalité au-delà de 10 jours ouvrés (SC § 8.4) |

---

## 6. Trois scénarios : prudent, central, ambitieux

Mois 1 = mois de signature du cadrage, au plus tôt mi-décembre 2026, plus probablement janvier 2027. Calculs [ES] (`scenarios.py`). Les frais fixes sont de 1 500 à 2 500 € par mois, plus 5 000 à 6 000 € de démarrage le mois 1 [HY]. La réserve prélevée est de 10 % du CA. Le « disponible » est ce qui reste pour les rémunérations chargées.

| | **Prudent** | **Central (recommandé)** | **Ambitieux** |
| --- | --- | --- | --- |
| Périmètre | Cadrage, puis socle léger. Pas de pilote CRM : la structure vendeuse, les œuvres ou l'avis fiscal manquent | Cadrage ; pilote B ; outillage C ; socle D ; un lot tous les deux mois ; un second client à partir du mois 6 | Le central, plus l'exploitation commerciale par vagues après un pilote réussi, un socle plus large (deux entités), des lots, et un second client dès le mois 5 |
| Capacité facturable utilisée | 4 à 8 JP par mois (capacité ≈ 7) | 8 à 10,5 JP (capacité ≈ 12) | 15 à 19 JP (capacité ≈ 20 : **à la limite**) |
| Disponibilité supposée | Morgan 50 %, Mathys 25 % | Morgan 65 %, Mathys 50 % | Les deux à 90 % : Morgan arrête l'essentiel de ses autres projets |
| Prix | 6 500 € une fois, puis 3 000 € HT par mois | Section 4.1 | Section 4.1 ; vagues de 5 500 € HT par mois en moyenne |
| **CA mensuel HT** | ≈ 3 600 € en moyenne de M1 à M6, puis 3 000 € | ≈ 7 200 € de M1 à M6, puis **≈ 8 500 €** | ≈ 11 000 € de M1 à M6, puis ≈ 16 000 € |
| CA sur 12 mois | ≈ 40 000 € | ≈ 94 000 € | ≈ 162 000 € |
| Part venant de GianLuca à M12 | 100 % | ≈ 75 % | ≈ 78 % |
| Disponible moyen pour les rémunérations chargées | ≈ 1 000 € par mois | ≈ 4 550 € par mois | ≈ 9 150 € par mois |
| Équivalent net pour **les deux associés** ensemble, avant IR | ≈ 550 à 730 € par mois | ≈ 2 400 à 3 200 € par mois | ≈ 4 800 à 6 400 € par mois |
| Hypothèses clés | GianLuca paie le cadrage mais délègue peu ; Marwin reste une activité d'appoint | Entité identifiée ; pilote financé ; assistant recruté ; second client signé vers le mois 6 | Pilote concluant ; deux entités clientes ; second client actif ; associés quasi à plein temps |
| Seuil de rentabilité | Frais couverts dès 2 000 à 3 000 € de CA par mois ; aucune rémunération significative | Le plancher de 2 500 € nets par ETP au prorata du temps est atteint ; 3 660 € ne l'est pas | Proche de l'ancienne formule de base, mais atteinte lot par lot, sur preuves |
| Ce qu'il faut accepter | Garder les autres revenus ; ne quitter aucun emploi | Revenu modeste la première année ; Morgan réduit ses autres projets | Saturation : sous-traiter un lot ou recruter si l'occupation dépasse 85 % pendant 3 mois (SC § 4) |

**Lecture.**
- Aucun scénario honnête ne paie 7 500 € nets chacun la première année.
- Le scénario central paie environ 1 200 à 1 600 € nets par associé pour un temps partiel (65 % et 50 %).
- Le scénario ambitieux retrouve l'ordre de grandeur de l'offre d'origine, mais il suppose précisément ce que les pièces ne montrent pas : un portefeuille réel, un payeur identifié, et deux associés libres.

Pour comparer, sur le seul contrat de 90 000 € HT, une SARL aurait laissé environ 19 000 à 23 000 € nets par associé sur l'année (SD § 1.3) [ES].

---

## 7. Structure et relations

### 7.1 Structure recommandée [PR, à faire valider]

- **Forme : SAS à l'IS**, avec un président et un directeur général qui détiennent chacun au moins un tiers du capital, un capital modeste **entièrement libéré** (pour le taux réduit de 15 %), et une rémunération nulle ou faible tant qu'aucun contrat n'est signé (SD § 1.10).
- **Raisons propres à cette stratégie :**
  - les premiers mois ne paient pas de rémunération régulière (section 6) : une SAS ne coûte alors aucune cotisation, alors qu'un gérant de SARL TNS doit environ 1 255 € par an au minimum, plus les forfaits de début d'activité (SD § 1.2) ;
  - Morgan garde d'autres activités, et Mathys peut-être un emploi ;
  - GianLuca envisagerait d'investir [DR].
- **Conditions pour basculer en SARL en cogérance 50/50** (≈ 15 à 30 % de net en plus à rémunération égale, SD § 1.3) : un contrat signé d'au moins 120 000 € HT par an qui finance une rémunération régulière, aucun investisseur dans les 24 mois, et aucun associé salarié ailleurs.
- **Séquence :**
  1. Préparer les statuts et le pacte.
  2. Immatriculer **seulement après une lettre d'intention ou un bon de commande** d'une entité identifiée de GianLuca (SD § 1.10 n° 5).
  3. Signer ensuite, puis encaisser.
  
  L'entreprise existante de Morgan, dont la domiciliation est résiliée, **ne facture pas** à la place de Marwin (SD § 3.1).
- **Pacte signé avant le contrat client** (SD § 5.2). Il couvre :
  - le temps engagé par chacun, en JP par mois ;
  - la déclaration écrite des autres activités de Morgan (OLSEN, Shelby, BOJ.ART…) et une règle de priorité ;
  - l'inventaire daté des actifs préexistants (CRM, Jarvis) et leur licence à Marwin ;
  - des rémunérations liées au temps ;
  - les mécanismes de blocage, de départ et d'incapacité ;
  - un coffre partagé des accès.

### 7.2 Principes de la relation avec GianLuca Carlone [PR]

| Rôle | Principe |
| --- | --- |
| **Client** | Seul rôle accepté pendant les 6 premiers mois. Un contrat-cadre et des fiches de mission **par entité** (SP § 2.3, S2). Un valideur nommé, distinct de toute personne liée à Marwin |
| **Bailleur** | Pas de bureaux pendant les 3 premiers mois. Ils ajoutent un indice de subordination (SD § 4.2) et ne sont pas nécessaires à ce périmètre. Ensuite, seulement une convention séparée : usage partagé, aucun horaire imposé, assurance, restitution alignée sur le préavis, sans lien avec les honoraires (SD § 4.8) |
| **Employeur** | Aucun salariat avant le bilan du 6e mois ; jamais des deux associés. Le cas échéant : des fonctions non couvertes par le contrat Marwin, et une validation des livrables de Marwin par une autre personne. Ne jamais en faire un argument de négociation des honoraires (SD § 4.6) |
| **Investisseur** | Rien avant 12 à 24 mois. Participation minoritaire, sans veto opérationnel. Contrat client résiliable indépendamment. **Jamais en échange d'une baisse d'honoraires**, d'un report de paiement ou de bureaux (offre:149 ; SD § 4.8) |
| **Dépendance** | Part de GianLuca dans le CA de Marwin : au plus 90 % au 6e mois et 80 % au 12e mois. Mesurée chaque mois. Au-delà de ces seuils, aucun nouveau lot pour lui tant que la prospection n'a pas repris |

### 7.3 Principes de la relation avec Medhi [PR]

1. **Écrire la décision du 4 nov.**, la faire valider par Mathys et l'annoncer à Medhi par écrit. Le message doit dire ce qui ne sera pas proposé et ce qui avait pu lui être dit : exclusivité, films, parc (SP § 3.9).
2. **Retirer ou marquer « historique »** l'offre écrite (offre:22, 88-94), STRATES v1.1, le vernissage, les médias de `pour-carlone/strates/` et le PDF de PR1.
3. **Ne rien promettre sur les œuvres de Medhi.** Marwin ne peut céder ni l'exclusivité ni les films (SD § 6). Si GianLuca veut vendre ses pièces, cela passe par un contrat direct entre Medhi et l'entité de GianLuca.
4. **Conflit d'intérêts.** Morgan déclare par écrit à GianLuca son lien avec BOJ.ART (« la personne avec qui je souhaite ouvrir la boutique », acc:21). Il s'abstient de tout conseil sur l'achat d'œuvres de BOJ.ART.
5. **Ni le nom ni le code de Jarvis** dans les livrables tant que leur propriété n'est pas réglée (SS PRO-2). Aucune capacité d'impression 3D promise (SC § 1.4).

---

## 8. Gouvernance minimale

| Acte | Propose | Autorise | Exécute | Contrôle | Valide le résultat |
| --- | --- | --- | --- | --- | --- |
| Priorités du mois, ouverture d'un lot | Morgan | GianLuca ou son valideur, **par écrit** (bon de commande) | — | Mathys (capacité disponible) | GianLuca |
| Production d'un livrable Marwin | L'associé responsable du lot | Contrat ou lot signé | L'associé responsable | **L'autre associé** (relecture à quatre yeux, au plus 2 jours ouvrés) | Le valideur du client |
| Données, CRM, outils | Mathys | Le responsable du traitement (entité de GianLuca) | Mathys | Morgan ; journal | Le responsable du traitement |
| Dépense pour le compte du client | Marwin prépare | L'entité cliente, par écrit, au-delà de tout plafond | L'entité cliente paie elle-même | Registre des engagements | L'entité cliente |
| Questions fiscales, juridiques, comptables, d'exploitation | Marwin prépare le dossier | — | Le professionnel compétent | — | Le professionnel, puis GianLuca |
| Contrat avec GianLuca, avenant, remise, engagement interne de plus de 1 000 € HT | L'un des associés | **Les deux associés**, par écrit | — | — | — |

**Plafonds [PR].**
- **Par défaut, Marwin n'engage aucune dépense au nom du client.**
- Si un mandat est indispensable : un mandat écrit **par entité**, avec une liste fermée d'actes, au plus 500 € HT par acte et 2 000 € HT cumulés par mois, aucun engagement récurrent, aucun contrat ni recrutement, des factures au nom du client et un registre des engagements (acc:94-103 ; SD § 4.7).
- Interne à Marwin : tout engagement de plus de 1 000 € HT, ou de plus de 3 mois, demande l'accord des deux associés.

**Le silence ne vaut pas accord [PR]** (acc:103).

| Délai sans réponse | Effet |
| --- | --- |
| 5 jours ouvrés | Relance écrite |
| 10 jours ouvrés | Le jalon concerné est reporté, consigné, et la capacité est réaffectée |
| 15 jours ouvrés | Revue du contrat au comité mensuel |

Seuls les travaux déjà autorisés continuent. L'absence de réponse ne vaut jamais autorisation de dépenser, d'engager ou d'étendre le périmètre.

La clause « réputé accepté » (offre:206) est **limitée au paiement** d'un livrable (section 5).

**Urgences et arbitrages.**
- Une urgence est traitée en régie, sur bon de commande écrit. Un courriel suffit, mais il doit venir du valideur.
- Un arbitrage entre deux projets revient au client.
- Un désaccord entre les associés suit le pacte : liste des décisions à l'unanimité, puis médiation (SD § 5.2).

**Adoption.** Une livraison est réussie quand elle est **utilisée** : registre consulté chaque semaine, comptes rendus traités, fiches CRM réellement appelées (SC § 6.1-6.2). Ce n'est pas le cas quand elle est seulement remise.

---

## 9. Feuille de route (datée à partir du 4 novembre 2026)

| Horizon | Livrables | Indicateurs (cible) | Responsable | Arrêt ou révision si… |
| --- | --- | --- | --- | --- |
| **Semaine 1 (4-11 nov.)** | Décision sur la notification à la CNIL **avant l'échéance du 5 nov.**, avec un avocat ou un DPD ; dépôt privé vérifié ; fiche de violation. Décision du 4 nov. écrite et validée par Mathys. **Gel de toute production gratuite** à partir du 15 nov., sauf la remise en ordre. Disponibilités nominatives écrites | Fiche de violation ouverte ; décision datée ; 0 nouveau document « pour Carlone » hors de la remise en ordre | Mathys (dépôt), Morgan (documents) | — |
| **90 jours (≈ début févr. 2027)** | Pacte et statuts signés ; SAS immatriculée **après** la lettre d'intention ; RC professionnelle et compte ouvert ; plateforme de facturation électronique choisie. Rendez-vous avec GianLuca : proposition de cadrage et dix questions (section 13). **Cadrage A signé et payé**, puis livré. Offre 0 terminée. Bon de commande de B et/ou C | Entité cliente identifiée (oui ou non) ; cadrage payé dans les délais ; inventaire signé ; accès fournis sous 10 jours ouvrés ; heures non facturées hors remise en ordre = 0 | Morgan (client), Mathys (conformité) | Pas d'entité ni de paiement au 31 janv. 2027 : **report** (section 10) |
| **6 mois (≈ début mai 2027)** | Pilote B mesuré (joignabilité, rendez-vous, refus) ; outillage C réceptionné ; assistant en poste et formé ; socle D en route depuis 1 à 3 mois ; **sortie à blanc** (exports et restauration dans un espace neuf) ; un second client signé ou une proposition envoyée | Paiements à l'heure (100 %) ; corrections au premier passage < 25 % ; occupation des associés ≤ 85 % ; part de GianLuca ≤ 90 % ; 0 incident critique ; registre consulté chaque semaine par le client | Morgan (comité), Mathys (outils) | Pilote sous les seuils fixés d'avance : arrêt de la prospection ou changement de cible. Assistant non recruté : socle limité au pilotage |
| **12 mois (≈ début nov. 2027)** | Bilan avec GianLuca : reconduction, élargissement ou fin propre avec réversibilité. Décisions sur les bureaux, l'emploi et l'investissement, chacune dans un accord séparé. Deux ou trois clients. Facturation électronique en émission (obligatoire au 1er sept. 2027, SD échéancier) | Part de GianLuca ≤ 80 % ; temps humain par résultat accepté −20 à −30 % sur les processus pilotés (SC § 7.4) ; gains mesurés documentés ; marge après rémunération cible ≥ 0 sur 12 mois | Les deux associés | Occupation > 95 % pendant 2 mois : sous-traiter ou réduire. Impayé récurrent : sortie |

---

## 10. Conditions pour commencer, signaux de suspension, scénarios de réduction, de report ou de refus

**Conditions minimales pour commencer (toutes requises) [PR] :**
1. Fuite de données traitée : décision de notification prise, dépôt privé, copies vérifiées, GianLuca informé par écrit.
2. Documents destinés au client mis en cohérence avec le retrait de Medhi ; PR1 fermée ou son PDF marqué « historique ».
3. Disponibilités nominatives écrites, d'au moins 8 JP par mois à eux deux ; accord écrit de Mathys sur la stratégie.
4. Pacte et statuts signés ; Marwin immatriculée ; RC professionnelle ; compte professionnel.
5. Entité cliente identifiée (dénomination, SIREN, signataire, valideur), par une lettre d'intention puis un bon de commande.
6. 50 % du cadrage encaissés **avant** le premier jour de travail.
7. Comptes et outils du client ouverts **à son nom** dès le premier jour.

**Signaux de suspension :**
- échéance impayée après une relance de 8 jours ;
- décision bloquante en attente depuis plus de 15 jours ouvrés ;
- demandes hors périmètre de plus de 20 % de la capacité pendant deux mois ;
- indices de subordination : horaires imposés, consignes directes, place dans un organigramme (SD § 4.8) ;
- nouvel incident de données ;
- demande d'engager une dépense sans mandat ;
- pression pour travailler avant le paiement ;
- proposition d'échanger des honoraires contre des bureaux, un emploi ou du capital.

**Réduire** au seul cadrage, ou à un seul lot, si GianLuca ne veut confier qu'un projet (par exemple, la vente d'œuvres), ou si la disponibilité réelle est celle du scénario prudent.

**Reporter**, c'est-à-dire tout geler, prospecter ailleurs et rester joignable, si l'une de ces conditions est remplie :
- aucune entité identifiée ou aucun cadrage payé six semaines après le rendez-vous, et au plus tard le 31 janvier 2027 ;
- fuite non traitée ;
- moins de 8 JP par mois disponibles à eux deux ;
- désaccord entre associés sur la stratégie.

**Refuser** dans l'un de ces cas :
- GianLuca exige un pilotage global de 20 à 40 JP sans entité, sans mandat ni accès ;
- il veut payer en bureaux, en emploi ou en capital plutôt qu'en honoraires ;
- il demande que Marwin encaisse des fonds, touche une commission sur les ventes ou porte des autorisations d'exploitant ;
- il demande un robot au contact du public ;
- il conditionne la mission au salariat simultané des associés.

---

## 11. Cinq décisions prioritaires (pour Morgan et Mathys)

1. **Avant le 5 novembre** : désigner qui répond de la fuite, rendre le dépôt privé, décider de la notification à la CNIL avec un avocat ou un DPD, et informer GianLuca par écrit (vR4 n° 7 ; SD § 9.3).
2. **Retirer l'offre de 20 et 40 JP, l'ancre de 46 JP et l'option laboratoire** de toute présentation. Les remplacer par la proposition « cadrage payé, puis lots, puis socle » (section 4). Mettre en cohérence tous les documents après le 4 nov. et **geler toute production gratuite** à partir du 15 nov.
3. **Fixer par écrit les disponibilités et le rôle de Marwin** : outilleur et pilote léger, pas exécutant administratif. Cela suppose de dire quels projets Morgan réduit, combien de JP Mathys engage, et qui valide.
4. **Choisir la structure et la séquence** : SAS par défaut, pacte d'abord, immatriculation après une lettre d'intention de l'entité de GianLuca, aucun encaissement avant.
5. **Adopter le calendrier de paiement** (socle d'avance, lots par acompte et réception, suspension à J+8) et la règle anti-double facturation, et fixer le seuil de report au 31 janvier 2027.

---

## 12. Principaux risques et preuve qui lèverait chaque objection

| Risque ou objection | Probabilité [HY] | Preuve qui lèverait l'objection |
| --- | --- | --- |
| Le pilotage global n'est pas le besoin prioritaire de GianLuca (D1) | Élevée | Une demande écrite de sa main : inventaire signé, priorités, bon de commande pour un suivi récurrent après le cadrage |
| GianLuca veut déléguer sans fournir les moyens ni les accès | Moyenne | Accès fournis sous 10 jours ouvrés ; valideur nommé ; interlocuteurs désignés |
| L'acheteur n'est pas solvable ou n'existe pas comme entité | Moyenne | SIREN de l'entité, bon de commande signé, premier paiement reçu |
| Les deux associés deviennent le goulot d'étranglement | Élevée | Trois mois avec une occupation ≤ 85 %, une file de validation ≤ 2 jours et aucun retard de plus de 5 jours (SC § 4) |
| Le budget finance des outils, pas le travail | Moyenne | Factures de lots réceptionnés ; outils payés par le client à son nom |
| La recherche absorbe la marge | Faible si la stratégie est suivie | Zéro JP sur STRATES et le laboratoire dans le relevé mensuel |
| Les équipes n'adoptent pas les outils | Moyenne | Registre consulté chaque semaine ; comptes rendus traités à 80 % ; fiches réellement appelées |
| Les responsabilités dépassent les pouvoirs | Moyenne | Mandat écrit par entité ; registre des engagements ; aucune dépense faite par Marwin |
| Dépendance excessive à une personne (GianLuca, Morgan) | Élevée | Second client signé ; part de GianLuca ≤ 80 % ; binôme de secours nommé pour chaque processus ; coffre d'accès partagé |
| Les prix ne couvrent pas la maintenance | Moyenne | Socle par processus ; maintenance chiffrée ; restauration testée et facturée dans le socle |
| La promesse est trop large pour être réceptionnée | Élevée avec l'offre actuelle, faible avec celle-ci | Critères de réception écrits avant chaque lot ; taux de réception au premier passage |
| **Risques de la présente stratégie** | | |
| GianLuca voulait « une équipe » et va voir ailleurs | Moyenne | Proposer explicitement l'option d'élargir au 6e mois, sur preuves ; mesurer sa réaction au cadrage |
| Le pilote commercial échoue faute d'œuvres ou de structure vendeuse | Élevée | Liste d'œuvres disponibles et nom de la structure vendeuse **avant** de vendre le lot B |
| Aucun assistant n'est recruté, et Marwin glisse vers l'exécution | Moyenne | Décision de recrutement inscrite au cadrage ; règle de l'offre C, ligne « Conditions de poursuite » |
| Le revenu est trop faible pour les associés la première année | Élevée | Revenus extérieurs maintenus, scénario prudent assumé ; second client avant de quitter toute autre source de revenu |
| La requalification du lien malgré tout | Faible à moyenne | Pas de bureaux pendant 3 mois ; prix au livrable ; liste des livrables du mois avant les heures (SD § 4.3) ; revue par un avocat en droit du travail |
| Une seconde exposition de données | Faible si l'offre 0 est faite | Comptes au nom du client ; offres d'IA professionnelles ; journal ; zéro incident critique |

---

## 13. Questions bloquantes (dix au plus)

**À GianLuca Carlone :**
1. Quelle entité signe, paie et valide (dénomination, SIREN, personne habilitée) ? Une seule, ou une par projet ?
2. Que voulez-vous obtenir en priorité dans les 90 jours ? Les « vingt jours par mois » viennent-ils de vous, et pour l'équipe ou par personne ?
3. Au nom de quelle structure vendez-vous les œuvres, avec quelles œuvres disponibles et quel conseil fiscal ? Qui appellera les entreprises : vous, un assistant ou Quali Contact (contrat, outil, payeur) ?
4. Êtes-vous prêt à recruter ou à désigner une personne pour exécuter le suivi au quotidien ?
5. Quel budget, et quel mode de paiement (d'avance ou à terme échu) pouvez-vous engager pour un cadrage, puis pour un suivi mensuel ?

**À Morgan et Mathys :**

6. Qui est responsable de la fuite, depuis quand la connaissez-vous (2 nov. ou plus tôt), et la décision de notification est-elle prise ?
7. Combien de JP par mois chacun engage-t-il par écrit, et quels projets Morgan réduit-il (OLSEN, Shelby, BOJ.ART, autres) ?
8. Mathys est-il d'accord avec la décision du 4 nov., avec cette stratégie et avec le partage des rôles ? Medhi est-il informé ?
9. Quelles versions de l'offre GianLuca a-t-il reçues ou vues (quatre jours par mois, lettre du 29 oct., V5, 13 ou 11 diapositives, rapport CRM, vernissage) ?
10. Qui détient le code et les données du CRM (organisation FinanceScope) et sous quel régime : cession, licence ou « offert » écrit ?

---

*Fichiers de calcul (hors dépôt) : `[dossier de travail] s3-calc/cout_jp.py`, `scenarios.py`, `marges.py`, `tresorerie.py`. Tous les montants qu'ils produisent sont des [ES], fondés sur des hypothèses de frais [HY] et sur des bases de rémunération à faire valider par un expert-comptable.*
