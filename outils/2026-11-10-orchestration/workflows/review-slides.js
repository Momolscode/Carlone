export const meta = {
  name: 'carlone-relecture-v12',
  description: 'Trois relectures indépendantes des diapositives de la version 12, corrections, puis contrôle final',
  phases: [
    { title: 'Relecture', detail: 'règles et exactitude, GianLuca sceptique, forme et rendu' },
    { title: 'Correction', detail: 'les remarques sont appliquées par lot' },
    { title: 'Contrôle final', detail: 'rendu complet, cohérence d’ensemble' },
  ],
}

const ROOT = '/home/user/Carlone'
const AUD = ROOT + '/audit/2026-11-09-audit-presentation-et-offre'
const T = AUD + '/travaux'
const SCR = '/tmp/claude-0/-home-user-Carlone/5dd15790-6933-5e33-ba7c-b9089896b9b3/scratchpad'
const F04 = AUD + '/04-scenario-de-la-nouvelle-presentation.md'
const DECK = SCR + '/deck-v12/project'
const order = (args && args.order) || []
const lots = (args && args.lots) || []

const ISSUES = {
  type: 'object',
  properties: {
    verdict: { type: 'string' },
    issues: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          slide: { type: 'string', description: 'id exact de la diapositive' },
          severity: { type: 'string', enum: ['bloquant', 'important', 'mineur'] },
          where: { type: 'string', description: 'texte visible, notes de l’orateur, mise en page' },
          problem: { type: 'string' },
          fix: { type: 'string', description: 'la correction précise : le texte de remplacement ou le changement de style' },
        },
        required: ['slide', 'severity', 'problem', 'fix'],
      },
    },
    keep: { type: 'array', items: { type: 'string' } },
  },
  required: ['verdict', 'issues'],
}

const LISTE = `Ordre des diapositives (fil principal puis annexe) : ${order.join(', ')}. Fichiers : ${DECK}/slides/<id>.html (le texte de <aside> = notes de l'orateur, lisibles par le client).`
const RENDU = `Contrôle automatique du code et du texte (à lancer d'abord) : cd ${SCR}/render && node lint.js ../deck-v12/project. Pour voir les diapositives : cd ${SCR}/render && node render.js ../deck-v12/project <dossier de sortie à vous> — sans liste d'id, tout le jeu est rendu dans l'ordre de deck.json — puis regardez les images <id>.png avec l'outil Read (toutes).`

phase('Relecture')
const REVIEWERS = [
  {
    key: 'regles',
    label: 'relecture — règles et exactitude',
    prompt: `Vous êtes le relecteur de conformité de la présentation de Marwin Tech à GianLuca Carlone (version 12). Vous cherchez à réfuter chaque affirmation. ${LISTE}

Lisez d'abord : ${T}/BRIEF.md (§ 4, 5 et 6), ${T}/a3-exactitude-et-engagements.md, ${T}/a4-offre-et-documents-clients.md, le scénario ${F04} (les lignes « Sources » et « Vigilance »), et pour les chiffres : ${ROOT}/pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md et ${ROOT}/audit/2026-11-04-audit-strategique/pour-gianluca/2026-11-09-proposition-de-cadrage.md. Pour les nouveautés technologiques : les parties « Vérification du 9 novembre 2026 » de ${T}/r1-nouveautes-ia-automatisation-2026.md, r2-applications-par-metier.md, r3-avenir-1-a-5-ans.md.

Extrayez le texte de chaque fichier (texte visible ET notes), puis vérifiez :
1. Les douze règles du BRIEF § 5, une à une, sur chaque diapositive. Cherchez par commande (grep, sans tenir compte de la casse) : le nom de l'autre prestataire, « 1,5 », « JP », « journée-personne », « voie », « socle », « plancher », « marge », « taux journalier », « rémunération », les codes d'audit (FV, DR, PR, HY, ES, MM, IN entre crochets ; D0x, DLx, Uxx), « John », « garanti », « sans risque », « moins cher », « révolution », un tutoiement, un emoji.
2. Chaque chiffre, prix, durée et date : identique à la source, mot pour mot. Les mêmes d'une diapositive à l'autre.
3. Chaque nouveauté technologique : dans une liste « sûr pour une diapositive ».
4. Chaque promesse : mesurée, conditionnée ou retirée. L'avenir dit comme une ambition avec ses conditions. Robotique : « plus tard, sous conditions ».
5. Chaque maquette porte « Maquette — données fictives » et ne montre aucune personne, société ou adresse réelle. Chaque image porte sa légende ; aucune image générée par IA n'est présentée comme une photo.
6. Marwin Tech : « société en cours de création, immatriculée avant toute facture et tout démarrage ». « Votre administratrice » : aidée, jamais remplacée ni surveillée. CRM : « remis en conformité avant tout usage ».
7. Tout écart entre une diapositive et son bloc du scénario qui change le sens.
Pour chaque écart : l'id, la gravité, l'endroit, le problème avec sa preuve, et le texte de remplacement. Vous n'écrivez et ne modifiez aucun fichier de la présentation ni du dépôt.`,
  },
  {
    key: 'gianluca',
    label: 'relecture — GianLuca sceptique',
    prompt: `Vous jouez GianLuca Carlone, marchand d'art à Cosne-Cours-sur-Loire : vous avez racheté plusieurs bâtiments, vous préparez plusieurs commerces dont un cabaret-spectacle, vous venez d'engager une administratrice, vous avez déjà reçu une autre offre de logiciel. Vous n'êtes pas technicien. Vous décidez vite quand c'est concret ; vous n'aimez ni perdre votre temps ni qu'on vous survende quelque chose. Deux jeunes associés, dont la société n'est pas encore immatriculée, vous projettent cette présentation. ${LISTE}

${RENDU}

Regardez les images dans l'ordre, comme un spectateur : cinq secondes par diapositive d'abord (qu'avez-vous compris ? qu'avez-vous envie de demander ?), puis lisez le texte et les notes. Lisez ensuite ${T}/a1-point-de-vue-gianluca.md pour vérifier que les objections qui y sont listées trouvent une réponse à l'écran.

Dites où vous décrochez, où vous doutez, où un mot vous échappe, où l'on vous promet trop, où il manque une preuve, où la demande est floue, où le prix arrive trop tôt ou trop tard. Dites à quelle diapositive vous seriez prêt à dire oui, et ce qui vous retient encore à la fin. Pour chaque problème : l'id, la gravité, le problème, et la correction précise (texte de remplacement). Ne proposez jamais d'ajouter une référence, un chiffre ou une promesse qui n'existe pas dans le scénario ${F04} : proposez de couper, de préciser, de montrer une preuve existante ou de dire franchement une limite. Vous n'écrivez et ne modifiez aucun fichier de la présentation ni du dépôt.`,
  },
  {
    key: 'forme',
    label: 'relecture — forme et rendu',
    prompt: `Vous êtes le relecteur de mise en page de la présentation de Marwin Tech à GianLuca Carlone (version 12). ${LISTE}

Lisez d'abord ${SCR}/gabarits/GABARITS.md en entier (contrat de format, grille, plafonds, contrôle).

${RENDU} Relevez aussi les lignes imprimées par la commande.

Vérifiez sur chaque diapositive :
1. Mesures : pas de « DÉBORDE » ; marge basse entre 60 et 200 px (plus admis pour une couverture, un énoncé ou une clôture au texte centré) ; mots sous le plafond (80 ; 120 pour une maquette ou un tableau) ; aucune taille sous 24 px ; titre de 55 caractères au plus ; titre à y=165 sur les diapositives de contenu ; pas de « LARGEUR » ni de « SECTIONS ».
2. Contrat de format, par commande sur les fichiers : une seule <section> dont l'id est le nom du fichier ; aucun <style>, <script>, class= ; aucune unité em, rem, vw, vh, % (hors width:N% des cellules de première ligne d'un tableau) ; aucun calc( ni var( ; aucun margin, z-index, float ; chaque border a son mot de style ; <aside> dernier enfant ; icônes parmi la liste permise ; images seulement /_blob/ parmi les trois identifiants permis, avec leur légende ; pas plus de 200 éléments ; couleurs et polices de la grille seulement.
3. À l'œil, sur chaque image : texte coupé, chevauchement, bloc collé au bord, colonnes déséquilibrées, grand vide, ligne veuve, taille de texte incohérente entre blocs de même rang, contraste insuffisant, légende manquante.
4. D'ensemble : le pied (texte et numéros dans l'ordre, sans trou ni doublon), la constance des surtitres, pas trois diapositives de suite au même gabarit, pas plus de quatre énoncés sur fond sombre, la typographie française (apostrophe courbe, guillemets « », espace avant « : ; ? ! », « € » après le montant).
Pour chaque problème : l'id, la gravité, l'endroit, le problème, et la correction précise (changement de style ou texte coupé). Vous n'écrivez et ne modifiez aucun fichier de la présentation ni du dépôt (votre dossier de rendu excepté).`,
  },
]
const reviews = (await parallel(REVIEWERS.map(r => () => agent(r.prompt, { label: r.label, phase: 'Relecture', schema: ISSUES }).then(x => ({ key: r.key, ...(x || {}) }))))).filter(Boolean)
const issues = reviews.flatMap(r => (r.issues || []).map(i => ({ from: r.key, ...i })))
log(issues.length + ' remarques, dont ' + issues.filter(i => i.severity === 'bloquant').length + ' bloquantes')

phase('Correction')
const known = new Set(lots.flat())
const fixes = (await parallel(lots.map((ids, k) => () => {
  const mine = issues.filter(i => ids.includes(i.slide) || (k === 0 && !known.has(i.slide)))
  if (!mine.length) return Promise.resolve({ lot: k + 1, applied: 0, rejected: [], slides: [] })
  return agent(`Mission : corriger des diapositives de la présentation de Marwin Tech à GianLuca Carlone (version 12) d'après trois relectures indépendantes (règles et exactitude ; GianLuca sceptique ; forme et rendu).

Vos diapositives : ${ids.join(', ')}. Fichiers : ${DECK}/slides/<id>.html. ${k === 0 ? 'Les remarques marquées « ensemble » ou portant sur un id inconnu vous reviennent aussi : appliquez-les à vos diapositives et signalez dans votre réponse ce qui concerne les autres.' : ''}

Lisez d'abord : ${SCR}/gabarits/GABARITS.md (contrat de format, strict), ${T}/BRIEF.md § 5, et dans ${F04} les blocs de vos diapositives.

Les remarques (JSON) :
${JSON.stringify(mine)}

Ce qui est réussi et ne doit pas être abîmé :
${JSON.stringify(reviews.flatMap(r => r.keep || []))}

Règles :
1. Traitez toutes les remarques « bloquant » et « important » ; les « mineur » quand la correction est sûre.
2. Avant d'appliquer une correction qui touche un chiffre, un prix, une date ou une règle, vérifiez-la dans la source citée par le scénario. Si une remarque est fausse, ne l'appliquez pas et dites pourquoi.
3. Quand deux remarques se contredisent : la règle et l'exactitude passent avant la persuasion, la persuasion avant la forme.
4. N'ajoutez aucune affirmation, aucun chiffre, aucun prix, aucune promesse qui n'est pas dans le scénario.
5. Après chaque modification : cd ${SCR}/render && node render.js ../deck-v12/project out-v12-fix${k + 1} ${ids.join(',')} puis regardez les images. Puis : node lint.js ../deck-v12/project ${ids.join(',')} — aucune ligne ERREUR ne doit rester. Les seuils de GABARITS.md § 5 s'appliquent.
Limites : vous ne modifiez que vos fichiers de diapositives. Ni deck.json, ni dépôt, ni commit, ni push, ni contact, ni achat, ni publication.`, { label: 'corrections lot ' + (k + 1), phase: 'Correction', schema: {
    type: 'object',
    properties: {
      applied: { type: 'integer' },
      rejected: { type: 'array', items: { type: 'string' } },
      for_others: { type: 'array', items: { type: 'string' } },
      slides: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, margin: { type: 'integer' }, words: { type: 'integer' }, changed: { type: 'boolean' } }, required: ['id'] } },
    },
    required: ['applied', 'slides'],
  } }).then(x => ({ lot: k + 1, ...(x || {}) }))
}))).filter(Boolean)

phase('Contrôle final')
const final = await agent(`Mission : contrôle final de la présentation de Marwin Tech à GianLuca Carlone (version 12), après corrections. ${LISTE}

Lisez ${SCR}/gabarits/GABARITS.md et ${T}/BRIEF.md § 5.

1. Rendez tout le jeu : cd ${SCR}/render && node render.js ../deck-v12/project out-v12-final — relevez chaque ligne, regardez chaque image. Puis : node lint.js ../deck-v12/project — aucune ligne ERREUR ne doit rester ; lisez chaque ALERTE.
2. Vérifiez diapositive par diapositive les seuils du § 5 de GABARITS.md et le contrat de format du § 1 (par commande : une seule <section> par fichier, id = nom du fichier, pas de class=, <style>, margin, z-index, unités interdites, var(, calc( ; images /_blob/ permises seulement).
3. Vérifiez l'ensemble : numéros du pied dans l'ordre de la liste, sans trou ni doublon ; mêmes prix, durées et mots partout ; lus à la suite, les titres racontent l'histoire ; la demande de décision est claire ; chaque maquette porte « Maquette — données fictives » ; chaque image a sa légende.
4. Recherchez une dernière fois, par commande, dans le texte visible et les notes : le nom de l'autre prestataire, « 1,5 », « JP », « journée-personne », « socle », « plancher », « marge », « taux journalier », « John », « garanti », « moins cher ».
5. Remarques transmises par les correcteurs pour d'autres lots : ${JSON.stringify(fixes.flatMap(f => f.for_others || []))}
Corrigez vous-même ce qui est simple et sûr (un pied, un numéro, une taille, un mot coupé, une apostrophe), en rendant de nouveau la diapositive. Signalez ce qui demande une décision. Vous ne modifiez que des fichiers ${DECK}/slides/<id>.html. Ni deck.json, ni dépôt, ni commit, ni push, ni contact, ni achat, ni publication.`, { label: 'contrôle final', phase: 'Contrôle final', schema: {
  type: 'object',
  properties: {
    ready: { type: 'boolean' },
    fixed: { type: 'array', items: { type: 'string' } },
    remaining: { type: 'array', items: { type: 'object', properties: { slide: { type: 'string' }, problem: { type: 'string' }, decision_needed: { type: 'string' } }, required: ['slide', 'problem'] } },
    measures: { type: 'array', items: { type: 'object', properties: { id: { type: 'string' }, margin: { type: 'integer' }, words: { type: 'integer' }, title_chars: { type: 'integer' } }, required: ['id'] } },
    titles_in_order: { type: 'array', items: { type: 'string' } },
  },
  required: ['ready', 'remaining'],
} })
return { reviews: reviews.map(r => ({ key: r.key, verdict: r.verdict, count: (r.issues || []).length })), blocking: issues.filter(i => i.severity === 'bloquant'), fixes, final }
