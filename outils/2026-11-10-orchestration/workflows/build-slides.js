export const meta = {
  name: 'carlone-diapositives-v12',
  description: 'Écrit les diapositives de la version 12 à partir du scénario validé ; chaque lot est rendu et mesuré',
  phases: [{ title: 'Écriture', detail: 'un agent par lot de diapositives, rendu et mesure obligatoires' }],
}

const ROOT = '/home/user/Carlone'
const AUD = ROOT + '/audit/2026-11-09-audit-presentation-et-offre'
const SCR = '/tmp/claude-0/-home-user-Carlone/5dd15790-6933-5e33-ba7c-b9089896b9b3/scratchpad'
const F04 = AUD + '/04-scenario-de-la-nouvelle-presentation.md'
const DECK = SCR + '/deck-v12/project'

const REPORT = {
  type: 'object',
  properties: {
    slides: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          natural_height: { type: 'integer' },
          margin: { type: 'integer', description: 'marge basse en px ; négatif si débordement' },
          words: { type: 'integer' },
          title_chars: { type: 'integer' },
          min_font: { type: 'number' },
          looked_at_image: { type: 'boolean' },
          changes_from_scenario: { type: 'array', items: { type: 'string' }, description: 'chaque mot coupé, déplacé dans les notes ou reformulé, et pourquoi' },
          concerns: { type: 'array', items: { type: 'string' } },
        },
        required: ['id', 'natural_height', 'margin', 'words', 'title_chars', 'min_font', 'looked_at_image'],
      },
    },
  },
  required: ['slides'],
}

const groups = (args && args.groups) || []
phase('Écriture')
const out = await parallel(groups.map(g => () => agent(`Mission : écrire ${g.slides.length} diapositives de la présentation de Marwin Tech à GianLuca Carlone (version 12), à partir d'un scénario déjà validé. Vous mettez en page ; vous n'inventez pas de contenu.

Vos diapositives (id, numéro à mettre dans le pied, gabarit) :
${g.slides.map(s => `- ${s.id} · n° ${s.n} · gabarit ${s.gabarit}`).join('\n')}

À lire d'abord, en entier :
1. ${SCR}/gabarits/GABARITS.md — le contrat de format (strict), la grille, les plafonds, les gabarits, les images permises, le contrôle obligatoire.
2. Dans ${F04}, le bloc de chacune de vos diapositives (cherchez « · <id> · »), plus « Le fil en dix lignes » en tête, pour le ton.
3. Pour chaque gabarit nommé : le fichier d'exemple dans ${SCR}/gabarits/project/slides/ (g-couverture.html, g-enonce.html, g-cartes-3.html, g-avant-apres.html, g-maquette.html, g-etapes.html, g-grand-chiffre.html, g-frise.html, g-decision.html, g-tableau.html, g-deux-colonnes.html, g-image.html, g-questions.html). Copiez la structure et les styles, remplacez le texte.
4. ${AUD}/travaux/BRIEF.md § 5 — les douze règles de tout texte montré au client.

Règles d'écriture :
- Un fichier par diapositive : ${DECK}/slides/<id>.html, qui contient exactement une balise <section id="<id>" …>. L'attribut id est l'id donné ci-dessus.
- Le texte visible, le titre, le surtitre, le bandeau, l'image avec sa légende et les notes de l'orateur sont ceux du scénario. Vous pouvez couper des mots pour tenir dans la page, ou faire passer un détail dans les notes ; vous n'ajoutez aucune affirmation, aucun chiffre, aucun prix, aucune promesse. Signalez chaque écart.
- Les notes de l'orateur vont dans <aside>, dernier enfant de la section, en texte simple.
- Pied : la ligne épinglée du gabarit, avec votre numéro : « Marwin Tech · pour GianLuca Carlone · novembre 2026 · <n°> ». (La couverture garde le pied de son gabarit.)
- Une maquette d'écran porte la mention « Maquette — données fictives », visible dans la fenêtre. Ses lignes sont celles du scénario ; les noms, montants et dates qu'elle montre sont fictifs et doivent le rester.
- Typographie française : apostrophe courbe « ’ », guillemets « », « € » après le montant, espace avant « : ; ? ! ».
- Aucune couleur, police, icône ou image hors de celles du document GABARITS.md. Pas d'emoji.

Contrôle obligatoire, à refaire jusqu'à réussite :
  cd ${SCR}/render && node render.js ../deck-v12/project out-v12-${g.key} ${g.slides.map(s => s.id).join(',')}
  cd ${SCR}/render && node lint.js ../deck-v12/project ${g.slides.map(s => s.id).join(',')}
La seconde commande relit le code et le texte (balises et propriétés permises, propriété sur la bonne balise, mots interdits, montants, guillemets) : aucune ligne ERREUR ne doit rester ; chaque ligne ALERTE est lue et corrigée, ou justifiée dans votre compte rendu. Attention aux tableaux : le style se met sur la balise table, et sur les cellules seulement width:N% (GABARITS.md § 1).
Puis regardez chaque image ${SCR}/render/out-v12-${g.key}/<id>.png avec l'outil Read. Une diapositive est terminée quand : elle ne déborde pas ; la marge basse est entre 60 et 200 px (une couverture, un énoncé ou une clôture peuvent avoir plus de marge si le texte est centré dans la page) ; les mots sont sous le plafond (80 ; 120 pour une maquette ou un tableau) ; aucune taille sous 24 px ; le titre fait 55 caractères au plus et commence à y=165 sur les diapositives de contenu ; aucune ligne « LARGEUR » ; « SECTIONS » n'apparaît pas ; et l'image regardée est lisible, équilibrée, sans texte coupé ni chevauchement. S'il reste trop de vide : grossissez le texte ou aérez, n'ajoutez pas de mots. Si cela déborde : coupez des mots, ne réduisez pas la taille sous les seuils.

Limites : vous n'écrivez que vos fichiers de diapositives (et le dossier de rendu). Vous ne touchez ni à deck.json, ni au dépôt, ni aux autres diapositives. Ni commit ni push, aucun contact, aucun achat, aucune publication. Le nom du client s'écrit GianLuca Carlone.

Renvoyez, pour chaque diapositive, les mesures du dernier rendu et la liste des écarts avec le scénario.`, { label: 'diapositives ' + g.key + ' (' + g.slides.map(s => s.id).join(', ') + ')', phase: 'Écriture', schema: REPORT }).then(r => ({ key: g.key, ...(r || {}) }))))

const done = out.filter(Boolean)
const all = done.flatMap(g => g.slides || [])
log(all.length + ' diapositives écrites ; ' + all.filter(s => s.margin < 0).length + ' en débordement déclaré')
return { groups: done, missing: groups.filter((g, i) => !out[i] || !out[i].slides).map(g => g.key) }
