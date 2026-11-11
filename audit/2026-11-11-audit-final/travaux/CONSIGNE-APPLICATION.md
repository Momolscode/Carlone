# Consigne d’application des constats de l’audit final

Document interne — ne pas transmettre à GianLuca Carlone · 11 novembre 2026

Neuf relectures ont rendu leurs constats dans `audit/2026-11-11-audit-final/travaux/a1-…md` à `a9-…md` (et `a10-…md` s’il existe : vérification des notes k7 et k14). Chaque constat donne un fichier, une ligne, le texte actuel et le texte proposé. Cette consigne dit quoi en faire.

## 1. La règle qui commande tout

Morgan Olsen a tranché le 11 novembre 2026 : « Non, on peut proposer bien d’autres choses, soyons créatifs et ambitieux. State of the art. » (`BRIEF-STATE-OF-THE-ART.md`). Donc :

- **On applique** tout constat d’exactitude, de droit, de cohérence ou de clarté : un chiffre, une date, un nom, un renvoi, une clause, une contradiction entre deux documents, une promesse de résultat absolu (« aucune échéance oubliée »), une règle de droit oubliée, une phrase obscure.
- **On n’applique pas** un constat qui réduit l’ambition ou retire une offre : présenter les programmes comme de simples « pistes » ; dire qu’« aujourd’hui seul le cadrage est proposé » ; retirer « cent fois plus vite » (il reste, avec sa tâche, son point de comparaison et « hypothèse à mesurer ») ; remplacer les enjeux par « rien ne presse » ; raccourcir la présentation ou renvoyer l’ambition en annexe ; « prendre en charge » → « préparer avec vous ». Constats visés : a1 n° 4, 10, 11, 12, 16, 17, 29 et 35 ; dans a4, le fil court (§ 9) et tout ce qui retire une offre ou une ambition. Ces sujets seront repris à part, avec le programme « State Of The Art ».
- **On ne tranche pas** ce qui revient aux deux associés (colonne « à décider par les associés ») : on laisse le texte tel quel, et l’on rend la liste de ces points dans sa réponse. Exception : quand la proposition ne fait que mettre entre crochets une promesse que l’audit du 9 novembre interdisait (attestation de vigilance, attestation d’assurance), on l’applique.

## 2. Formules arrêtées pendant l’audit (à employer partout)

- Mesure de METR : « Sur des tâches de logiciel, la durée des tâches que les meilleurs agents d’IA réussissent une fois sur deux double environ tous les sept mois depuis 2019 (METR, janvier 2026) : une mesure du passé, pas une prévision. » Une seule date de source : janvier 2026.
- Sept jours : « aucun paiement n’est demandé ni reçu pendant les sept jours qui suivent la signature ».
- Cession : « une fois le prix dû payé (le solde ; en cas d’arrêt, l’acompte) ».
- Essai : « un essai de huit semaines au plus, sur une seule tâche, mesurée avant et après, commandé à part, avec son prix ».
- Séjours qui réunissent une nuit, un spectacle et un soin : ajouter là où l’idée est décrite « Vendre ensemble une nuit, un spectacle et un soin peut relever des règles de la vente de séjours : à faire valider par vos professionnels. »
- Machine d’IA sur place : « … garderait vos archives chez vous, si ses logiciels n’envoient rien en ligne et si la sécurité de la machine est tenue ».
- Les trois pièces jointes du bon de commande se nomment : le tableau « Qui valide quoi » ; la page « Votre droit de rétractation : information et formulaire » ; l’accord sur les données.
- « Réactifs » remplace « Rapides et disponibles » ; « Un interlocuteur nommé » remplace « Un seul interlocuteur » ; aucune comparaison avec d’autres prestataires.

## 3. Méthode

1. Cherchez avec Grep, dans tous les rapports `a*.md`, chaque ligne qui cite un fichier de votre lot (par son nom court). Lisez la ligne entière.
2. Pour chaque constat : appliquez-le (outil Edit, au plus près du texte ; cherchez par le texte, les numéros de ligne ont pu bouger), écartez-le selon le § 1, ou classez-le « à décider ». Deux rapports proposent parfois deux textes pour la même phrase : gardez celui qui respecte le § 2 et l’offre en une page.
3. Dans chaque fichier modifié, ajoutez à la ligne de date de l’en-tête « corrigé le 11 novembre 2026 » (une seule fois ; ne changez pas le nom du fichier).
4. Contrôles : `cd /tmp/claude-0/-home-user-Carlone/5dd15790-6933-5e33-ba7c-b9089896b9b3/scratchpad/render && node lint-doc.js --tarifs-publics <fichier client>` ou `--interne <fichier interne>` → 0 erreur, chaque alerte lue ; `node md2pdf.js <fichier.md> /tmp/claude-0/-home-user-Carlone/5dd15790-6933-5e33-ba7c-b9089896b9b3/scratchpad/pdf-controle/<nom>.pdf --compact` → une page unique reste sur 1 page, une fiche sur 2 pages au plus, le bon de commande sur 3, la proposition sur 6.
5. Cadre : aucun contact, aucun envoi, aucun achat, aucune publication ; pas de commande git ; ne jamais ouvrir `crm/` ; n’écrire que les fichiers de votre lot ; une pièce datée d’avant le 10 novembre ne se réécrit pas (mention datée seulement). Typographie française ; vouvoiement ; « vos neuf suites », « votre administratrice ».
