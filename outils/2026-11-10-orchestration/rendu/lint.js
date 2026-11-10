// Contrôle mécanique des diapositives : contrat de format et lignes rouges des textes montrés au client.
// Usage : node lint.js <dossier project> [id,id,...]   (sans liste : l'ordre de deck.json)
// Sortie : une ligne par constat, « ERREUR » (à corriger) ou « ALERTE » (à regarder), puis un total.
const fs = require('fs')
const path = require('path')

const deckDir = process.argv[2]
const only = process.argv[3] ? process.argv[3].split(',') : null
const deck = JSON.parse(fs.readFileSync(path.join(deckDir, 'deck.json'), 'utf8'))
const ids = only || deck.order

const TAGS = new Set(['section', 'h1', 'h2', 'h3', 'p', 'ul', 'ol', 'li', 'br', 'div', 'table', 'tr', 'th', 'td', 'img', 'hr', 'aside', 'b', 'i', 'u', 'a', 'span', 'x-shape', 'x-connector', 'x-icon'])
const VOID = new Set(['br', 'img', 'hr'])
const ICONS = new Set('Activity Book Chart Chat Check CheckCircle Clock Cloud Code Database Globe GraduationCap Home Key Lightbulb Lightning Link Lock PaperPlane Play Search Settings Star ThumbsUp Tool Trust Users Verified Warning Wrench'.split(' '))
const BLOBS = {
  '978b33fb6a67a61eb7cddd412da92807': 'Maquette — données fictives',
  'ca5c05894b7cb83f246620fbfe87cf73': 'Maquette — données fictives',
  '350cfbd80fbdc22430717071f3ee3b3b': 'Maquette — données fictives',
  '1b2ea244605412dde80b8ce6c60c6a25': 'Maquette — données fictives',
  '0ff853b8e971486dbf4d7bc5cdd570ba': 'Maquette — données fictives',
  '1bf0b8bb98320f23191cb005752f68a7': 'Maquette — données fictives',
  '93ccdd00d255c1a63124e7cb89171197': 'Maquette — données fictives',
  'e4bee9f3265a00353b2f5d0b11907895': 'Maquette — données fictives',
  'e8c2d6f07d1eade1eab238e9fe94544a': 'Maquette — données fictives',
  '0323693fb134fb5fa9dabd5434dbda5d': 'Maquette — données fictives',
  'e6a52fd272f874369fa34a9a961fe98d': 'Maquette — données fictives',
  'ad0412a37b6980cb8a80eb94c5f3363b': 'vision générée par IA',
  '6fab0132c846ec1c3083832f2c086864': 'générée par IA',
  '0da19f0843c584b5fda3b7136d3818a6': 'vision générée par IA',
  '51a8be11835fa54a99fff4c0a99ac522': 'générée par IA',
  '99f8d10e60b36c00c9a38334b5a95ee4': 'générée par IA',
}
const PROPS = new Set(['display', 'flex-direction', 'gap', 'row-gap', 'column-gap', 'align-items', 'justify-content', 'flex', 'align-self', 'flex-wrap', 'grid-template-columns', 'grid-template-rows',
  'position', 'left', 'top', 'right', 'bottom', 'width', 'height', 'padding', 'padding-top', 'padding-right', 'padding-bottom', 'padding-left', 'overflow',
  'font-family', 'font-size', 'font-weight', 'font-style', 'line-height', 'letter-spacing', 'text-align', 'text-transform', 'white-space', 'color',
  'background', 'background-color', 'border', 'border-top', 'border-right', 'border-bottom', 'border-left', 'border-radius', 'box-shadow', 'opacity', 'object-fit', 'text-decoration', 'transform', 'min-width', 'min-height', 'max-width', 'max-height', 'aspect-ratio', 'text-shadow', 'flex-grow', 'flex-shrink', 'flex-basis', 'justify-items', 'justify-self', 'grid-column', 'grid-row'])
const POS = ['position', 'left', 'top', 'right', 'bottom', 'width', 'height', 'opacity', 'transform']
const ELEMENT_PROPS = {
  td: new Set(['width', 'text-align', 'color', 'padding']),
  th: new Set(['width', 'text-align', 'color', 'padding', 'font-weight']),
  tr: new Set(['background']),
  table: new Set([...POS, 'font-family', 'font-size', 'color', 'background', 'border', 'border-top', 'border-right', 'border-bottom', 'border-left', 'border-radius', 'box-shadow', 'padding', 'align-self', 'flex']),
  span: new Set(['color', 'font-weight', 'font-style', 'text-decoration']),
  'x-shape': new Set([...POS, 'background', 'border', 'box-shadow', 'flex', 'align-self']),
  'x-icon': new Set([...POS, 'color', 'background', 'border', 'border-radius', 'box-shadow', 'flex', 'align-self']),
  img: new Set([...POS, 'object-fit', 'background', 'border', 'border-top', 'border-right', 'border-bottom', 'border-left', 'border-radius', 'box-shadow', 'flex', 'align-self', 'aspect-ratio']),
  hr: new Set([...POS, 'color', 'background', 'border', 'flex', 'align-self']),
}
const PALETTE = new Set(['#14181f', '#f6f3ee', '#fffdf9', '#d9d2c5', '#7e5f31', '#b08d57', '#3d4450', '#5f636c', '#f3efe8', '#e7e1d6', '#3f6b4f', '#8a3b2e', '#9a9286', '#ffffff', '#000000'])

// Lignes rouges : [expression, niveau, message]
const RED = [
  [/1[,.]5\s*M\b|1[,.]5\s*million|million/i, 'ERREUR', 'montant des bâtiments ou « million »'],
  [/\bJP\b|journées?[- ]personnes?/i, 'ERREUR', '« JP » ou « journée-personne »'],
  [/\bsocle\b/i, 'ERREUR', '« socle »'],
  [/\bvoies?\b/i, 'ERREUR', '« voie »'],
  [/plancher/i, 'ERREUR', '« plancher »'],
  [/\bmarges?\b/i, 'ERREUR', '« marge »'],
  [/taux journalier|tarif journalier|prix (par|à la) jour/i, 'ERREUR', 'taux journalier'],
  [/\bD\d{2}\b|\bDL\d+\b|\bU\d{2}\b|\[(FV|DR|PR|HY|ES|MM|IN)\]/, 'ERREUR', 'code de l’audit'],
  [/John[- ]?Lucas/i, 'ERREUR', 'nom du client mal écrit'],
  [/Gian[- ]luca|Gianluca|GianLucca|Carlonne/, 'ERREUR', 'nom du client : écrire « GianLuca Carlone »'],
  [/BOJ|Medhi|Mehdi/i, 'ERREUR', 'partenaire retiré de l’offre'],
  [/Quali ?Contact/i, 'ERREUR', 'tiers nommé'],
  [/mieux et moins cher/i, 'ERREUR', '« mieux et moins cher »'],
  [/6[\s  ]?000[\s  ]?€|15[\s  ]?000|30[\s  ]?000|72[\s  ]?000|24[\s  ]?000/, 'ERREUR', 'prix de l’autre offre ou ancienne offre mensuelle'],
  [/\bAccor(hotels|invest)?\b/i, 'ERREUR', 'nom de l’autre prestataire (groupe hôtelier) : ne jamais le nommer dans un texte client'],
  [/(^|[^a-zà-ÿ’'])Accord(?![a-zà-ÿ])/, 'ALERTE', '« Accord » avec majuscule : vérifier que ce n’est pas le nom de l’autre prestataire'],
  [/garanti/i, 'ALERTE', '« garanti… » : aucune garantie de résultat ne doit être donnée'],
  [/remplac/i, 'ALERTE', '« remplac… » : l’administratrice n’est jamais remplacée'],
  [/surveill|contrôl(e|er) (son|le) travail/i, 'ALERTE', '« surveill… » : l’administratrice n’est jamais surveillée'],
  [/\b(tu|ton|ta|tes|toi)\b/i, 'ALERTE', 'tutoiement possible'],
  [/not(e|er|ation) (les|des) (candidats|salariés)|classe(r)? les candidats/i, 'ALERTE', 'notation de candidats ou de salariés'],
  [/\b(workflow|dashboard|pipeline|onboarding|reporting|business|feedback|deadline|roadmap|process|backlog|kick-?off|quick win|use case|scal(e|able)|insight|back-?office|front-?office|no-?code|low-?code|prompt|chatbot|data|cloud|booster|disrupt)\b/i, 'ALERTE', 'anglais ou jargon'],
  [/révolution|incontournable|sur[- ]mesure à 100|100\s?%|zéro (erreur|risque)|sans (aucun )?risque|toujours à jour|en temps réel|clé en main|leader|n°\s?1|meilleur/i, 'ALERTE', 'formule creuse ou promesse absolue'],
  [/\bimmédiatement\b|dès demain|en quelques (clics|minutes|secondes)/i, 'ALERTE', 'promesse de délai'],
  [/dernière chance|offre limitée|avant qu’il ne soit trop tard|ne ratez pas|urgent/i, 'ERREUR', 'pression commerciale'],
  [/nos clients|d’autres clients|références clients|témoignage/i, 'ALERTE', 'référence client : aucune ne doit être inventée'],
]
const EMOJI = /[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}\u{FE0F}]/u
const PRICE_OK = new Set(['6500', '7800'])
const PRICE_DOC = new Set(['3000', '5300', '10400', '15700', '18700', '7500', '6400', '1200', '2300', '700', '1000', '1400', '1500', '22200', '25200', '80', '430', '70', '275', '40', '85', '100'])

let errors = 0, alerts = 0
const say = (id, level, msg) => { level === 'ERREUR' ? errors++ : alerts++; console.log(`${id.padEnd(18)} ${level}  ${msg}`) }
const txt = s => s.replace(/<[^>]*>/g, ' ').replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/\s+/g, ' ').trim()

ids.forEach((id, idx) => {
  const file = path.join(deckDir, 'slides', id + '.html')
  if (!fs.existsSync(file)) return say(id, 'ERREUR', 'fichier absent')
  const html = fs.readFileSync(file, 'utf8')
  const E = m => say(id, 'ERREUR', m), A = m => say(id, 'ALERTE', m)

  // 1. Structure
  const nSec = (html.match(/<section\b/g) || []).length
  if (nSec !== 1) E(`${nSec} balises <section> (une seule attendue)`)
  if (!/^\s*<section\b/.test(html) || !/<\/section>\s*$/.test(html)) E('du contenu hors de la balise <section>')
  const sid = (html.match(/<section\b[^>]*\bid="([^"]*)"/) || [])[1]
  if (sid !== id) E(`id de la section « ${sid} » différent du nom du fichier`)
  if (/<style|<script|<link|<html|<body|<head|\bclass=|\bonclick=|<svg|<iframe|<video/i.test(html)) E('balise ou attribut interdit (style, script, class, svg…)')
  if (/colspan|rowspan/i.test(html)) E('colspan ou rowspan')
  if (/<!--/.test(html)) A('commentaire HTML dans le fichier')

  // 2. Balises, profondeur, styles
  const re = /<(\/?)([a-zA-Z][\w-]*)((?:"[^"]*"|'[^']*'|[^>"'])*)>/g
  let m, count = 0, divDepth = 0, maxDiv = 0, listDepth = 0, inAside = false
  const cellPaddings = new Set()
  const stack = []
  while ((m = re.exec(html))) {
    const closing = m[1] === '/', tag = m[2].toLowerCase(), attrs = m[3]
    if (!TAGS.has(tag)) { E(`balise non permise <${tag}>`); continue }
    if (closing) {
      if (tag === 'div') divDepth--
      if (tag === 'ul' || tag === 'ol') listDepth--
      if (tag === 'aside') inAside = false
      const top = stack.pop()
      if (top !== tag) E(`balises mal fermées : </${tag}> ferme <${top}>`)
      continue
    }
    if (inAside) E(`balise <${tag}> dans les notes de l’orateur (texte simple attendu)`)
    count++
    if (!VOID.has(tag)) stack.push(tag)
    if (tag === 'div') { divDepth++; maxDiv = Math.max(maxDiv, divDepth) }
    if (tag === 'ul' || tag === 'ol') { listDepth++; if (listDepth > 1) E('liste imbriquée') }
    if (tag === 'aside') inAside = true
    if (tag === 'x-icon') { const n = (attrs.match(/\bname="([^"]*)"/) || [])[1]; if (!ICONS.has(n)) E(`icône inconnue « ${n} »`) }
    if (tag === 'x-shape') { const k = (attrs.match(/\bkind="([^"]*)"/) || [])[1]; if (!/^(ellipse|diamond|arrow-right|arrow-left|arrow-up|arrow-down|line)$/.test(k || '')) E(`forme inconnue « ${k} »`) }
    if (tag === 'img') {
      const src = (attrs.match(/\bsrc="([^"]*)"/) || [])[1] || ''
      const b = (src.match(/^\/_blob\/([0-9a-f]{32})$/) || [])[1]
      if (!b || !BLOBS[b]) E(`image non autorisée : ${src}`)
      else if (!txt(html).includes(BLOBS[b])) E(`image ${b.slice(0, 8)}… sans sa légende « ${BLOBS[b]} »`)
      if (!/\balt="[^"]+"/.test(attrs)) E('image sans texte de remplacement (alt)')
    }
    const style = (attrs.match(/\bstyle="([^"]*)"/) || [])[1]
    if (style == null) continue
    for (const decl of style.split(';')) {
      const i = decl.indexOf(':'); if (i < 0) continue
      const p = decl.slice(0, i).trim().toLowerCase(), v = decl.slice(i + 1).trim()
      if (!p) continue
      const only_ = ELEMENT_PROPS[tag]
      if (only_ && !only_.has(p)) E(`propriété « ${p} » non permise sur <${tag}>`)
      if ((tag === 'td' || tag === 'th') && p === 'padding') cellPaddings.add(v)
      if (p === 'overflow' && tag !== 'div') E(`overflow sur <${tag}> (div seulement)`)
      if (/^(display|gap|align-items|justify-content|flex-direction|grid-template-columns|grid-template-rows)$/.test(p) && tag !== 'div' && tag !== 'section') E(`${p} sur <${tag}> (section ou div seulement)`)
      if (/^margin|^z-index$|^float$|^box-sizing$|^animation|^transition/.test(p)) E(`propriété interdite ou sans effet : ${p}`)
      else if (!PROPS.has(p)) A(`propriété hors du sous-ensemble connu : ${p}:${v}`)
      if (/calc\(|var\(|currentcolor/i.test(v)) E(`valeur interdite : ${p}:${v}`)
      const isCellWidth = p === 'width' && (tag === 'th' || tag === 'td')
      const pctOk = isCellWidth || p === 'border-radius' || p === 'line-height' || (p === 'background' && /gradient/.test(v)) || (p === 'flex' && /\b0%/.test(v))
      if (/\d(em|rem|vw|vh|pt|ch|ex)\b/.test(v)) E(`unité interdite : ${p}:${v}`)
      else if (/%/.test(v) && !pctOk) E(`pourcentage hors des cas permis : ${p}:${v} sur <${tag}>`)
      if (p === 'position' && v !== 'absolute' && v !== 'relative') E(`position:${v}`)
      if (p === 'font-size') { const n = parseFloat(v); if (n < 24) E(`taille de texte ${v} (24px au moins)`) }
      if (p.startsWith('padding')) for (const n of v.split(/\s+/).map(parseFloat)) if (n < 0 || n > 256) E(`padding hors bornes : ${v}`)
      if (/^border(-top|-right|-bottom|-left)?$/.test(p) && v !== 'none' && v !== '0') {
        if (!/\b(solid|dashed|dotted)\b/.test(v)) E(`bordure sans style : ${p}:${v}`)
        const w = parseFloat(v); if (w > 16) E(`bordure trop épaisse : ${v}`)
      }
      if (p === 'background' && /gradient/.test(v) && (v.match(/gradient/g) || []).length > 1) E('plusieurs dégradés dans un fond')
      if (p === 'background' && /url\(/.test(v)) E('image de fond par URL')
      if (/^(color|background|background-color)$/.test(p)) for (const c of v.match(/#[0-9a-fA-F]{6}\b/g) || []) if (!PALETTE.has(c.toLowerCase())) A(`couleur hors palette : ${c}`)
    }
  }
  if (stack.length) E(`balises non fermées : ${stack.join(', ')}`)
  if (cellPaddings.size > 1) E('plusieurs valeurs de padding dans les cellules d’un tableau (une seule permise)')
  if (count > 200) E(`${count} éléments (200 au plus)`)
  if (maxDiv > 15) E(`${maxDiv} <div> imbriqués (15 au plus)`)

  // 3. Notes de l'orateur et pied
  const aside = (html.match(/<aside>([\s\S]*?)<\/aside>/) || [])[1]
  if (aside == null) E('notes de l’orateur absentes (<aside>)')
  else {
    if (!/<\/aside>\s*<\/section>\s*$/.test(html)) E('les notes de l’orateur ne sont pas le dernier élément')
    if (aside.length > 4000) E(`notes de l’orateur trop longues (${aside.length} caractères)`)
    if (txt(aside).length < 80) A('notes de l’orateur très courtes')
  }
  const visibleHtml = html.replace(/<aside>[\s\S]*?<\/aside>/, '')
  const visible = txt(visibleHtml), notes = txt(aside || ''), all = visible + ' ¶ ' + notes
  const foot = visible.match(/Marwin Tech · pour GianLuca Carlone · novembre 2026 · (\d+)/)
  const isCover = id === deck.cover, isLast = idx === ids.length - 1
  if (!only && !isCover) {
    if (!foot) A('pied de page type absent')
    else if (Number(foot[1]) !== idx + 1) E(`numéro du pied (${foot[1]}) différent du rang (${idx + 1})`)
  }
  const pinned = (visibleHtml.match(/position:absolute[^"]*bottom:64px/g) || []).length
  if (pinned > 1) E(`${pinned} lignes épinglées en pied`)

  // 4. Lignes rouges (texte visible et notes)
  for (const [rx, level, msg] of RED) {
    for (const [where, s] of [['écran', visible], ['notes', notes]]) {
      const hit = s.match(rx)
      if (hit) say(id, level, `${msg} — ${where} : « …${s.slice(Math.max(0, hit.index - 30), hit.index + hit[0].length + 30)}… »`)
    }
  }
  if (EMOJI.test(all)) E('emoji ou pictogramme Unicode')
  if (/['"]/.test(visible.replace(/\d"/g, ''))) A('apostrophe ou guillemet droit à l’écran (typographie française : ’ et « »)')
  // Prix
  for (const [where, s] of [['écran', visible], ['notes', notes]]) {
    for (const p of s.matchAll(/(\d{1,3}(?:[\s  ]\d{3})*|\d+)(?:,\d+)?[\s  ]?(?:€|euros?)/g)) {
      const n = p[1].replace(/[\s  ]/g, '')
      if (PRICE_OK.has(n)) continue
      if (PRICE_DOC.has(n)) say(id, 'ALERTE', `prix ${p[0]} (${where}) : figure dans un document client du 9 novembre, à valider par Morgan et Mathys`)
      else say(id, 'ERREUR', `prix ${p[0]} (${where}) : absent des documents clients`)
    }
    for (const p of s.matchAll(/\d+(?:[,.]\d+)?[\s  ]?%/g)) say(id, 'ALERTE', `pourcentage ${p[0]} (${where}) : une source datée est-elle citée ?`)
  }
  if (/6[\s  ]500/.test(all) && !/HT|hors taxes/.test(all)) A('6 500 € sans « HT »')
  // Maquettes
  if (/maquette/i.test(visible) && !/Maquette — données fictives/.test(visible)) E('maquette sans la mention exacte « Maquette — données fictives »')
  // Société
  if (/Marwin Tech (est|a été) (créée|immatriculée)|notre société existe/i.test(all)) E('la société est présentée comme déjà immatriculée')
  // Titre
  const title = txt((visibleHtml.match(/<h[12]\b[^>]*>([\s\S]*?)<\/h[12]>/) || [])[1] || '')
  if (!title) A('pas de titre h1 ou h2')
  else if (title.length > 55 && !isCover) A(`titre de ${title.length} caractères (55 au plus) : « ${title} »`)
  const words = visible ? visible.split(' ').length : 0
  if (words > 120) E(`${words} mots visibles`)
  else if (words > 80) A(`${words} mots visibles (80 au plus, 120 pour une maquette ou un tableau)`)
  void isLast
})
console.log(`\nTotal : ${errors} erreur(s), ${alerts} alerte(s) sur ${ids.length} diapositive(s).`)
