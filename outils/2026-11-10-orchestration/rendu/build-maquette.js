// Assemble la maquette cliquable (un seul fichier HTML, sans dépendance externe), puis la contrôle et la photographie.
// Usage : node build-maquette.js <dossier source> <sortie.html> [<dossier des captures>]
//
// Dossier source attendu :
//   socle/base.html     page complète. Doit contenir, chacun une seule fois, les repères :
//                         /*__POLICES__*/   dans une balise <style>      (remplacé par les polices embarquées)
//                         <!--__ECRANS__--> dans le <body>               (remplacé par les écrans, dans l'ordre des noms de fichiers)
//                         /*__DONNEES__*/   dans une balise <script>     (remplacé par socle/donnees.js)
//                         /*__SCRIPTS__*/   dans une balise <script>     (remplacé par les ecrans/*.js, dans l'ordre)
//   socle/donnees.js    les données fictives communes à tous les écrans (une constante DONNEES).
//   ecrans/NN-<id>.html un écran : <section class="ecran" id="ecran-<id>" data-titre="…"> … </section>
//   ecrans/NN-<id>.js   (facultatif) le script de cet écran.
// Navigation attendue : adresse « #/<id> » ; l'écran affiché est le seul visible.
//
// Contrôles : aucune requête externe, aucune erreur de script, mention exacte « Maquette — données fictives » visible
// sur chaque écran, pas de défilement horizontal, taille de texte minimale, aucun texte interdit.
// Captures : <captures>/revue/<id>.png (1440 × 900) et <captures>/diapo/<id>.png (1280 × 720, densité 2).
const fs = require('fs')
const path = require('path')
const { chromium } = require('playwright')

const [src, out, shots] = process.argv.slice(2)
if (!src || !out) { console.error('Usage : node build-maquette.js <dossier source> <sortie.html> [<dossier des captures>]'); process.exit(2) }

const read = f => fs.readFileSync(f, 'utf8')
const fontDir = path.join(__dirname, 'node_modules/@fontsource')
const face = (family, pkg, w, style) => {
  const f = path.join(fontDir, pkg, 'files', `${pkg}-latin-${w}-${style}.woff2`)
  return `@font-face{font-family:'${family}';font-weight:${w};font-style:${style};font-display:block;src:url(data:font/woff2;base64,${fs.readFileSync(f).toString('base64')}) format('woff2')}`
}
const fonts = [
  face('Cormorant Garamond', 'cormorant-garamond', 600, 'normal'),
  face('Cormorant Garamond', 'cormorant-garamond', 700, 'normal'),
  face('DM Sans', 'dm-sans', 400, 'normal'),
  face('DM Sans', 'dm-sans', 500, 'normal'),
  face('DM Sans', 'dm-sans', 700, 'normal'),
  face('DM Sans', 'dm-sans', 400, 'italic'),
].join('\n')

let problems = 0
const bad = m => { problems++; console.log('ERREUR  ' + m) }
const warn = m => console.log('ALERTE  ' + m)

const basePath = path.join(src, 'socle/base.html')
if (!fs.existsSync(basePath)) { bad('socle/base.html absent'); process.exit(1) }
let html = read(basePath)
const ecransDir = path.join(src, 'ecrans')
const names = fs.existsSync(ecransDir) ? fs.readdirSync(ecransDir).sort() : []
const ecransHtml = names.filter(n => n.endsWith('.html')).map(n => `<!-- ${n} -->\n` + read(path.join(ecransDir, n))).join('\n\n')
const ecransJs = names.filter(n => n.endsWith('.js')).map(n => `// ${n}\n` + read(path.join(ecransDir, n))).join('\n\n')
const donnees = fs.existsSync(path.join(src, 'socle/donnees.js')) ? read(path.join(src, 'socle/donnees.js')) : ''

const put = (mark, value) => {
  const n = html.split(mark).length - 1
  if (n !== 1) { bad(`repère ${mark} présent ${n} fois dans socle/base.html (attendu : 1)`); return }
  html = html.replace(mark, () => value)
}
put('/*__POLICES__*/', fonts)
put('<!--__ECRANS__-->', ecransHtml)
put('/*__DONNEES__*/', donnees)
put('/*__SCRIPTS__*/', ecransJs)

// Aucune dépendance externe.
const ext = html.replace(/url\(data:[^)]*\)/g, '').match(/(?:src|href)\s*=\s*["'](?:https?:)?\/\/[^"']+|@import|url\(\s*["']?https?:/gi)
if (ext) bad('dépendance externe : ' + [...new Set(ext)].slice(0, 5).join(' ; '))

fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true })
fs.writeFileSync(out, html)
console.log(`ÉCRIT   ${out} (${Math.round(html.length / 1024)} Ko ; ${names.filter(n => n.endsWith('.html')).length} écran(s))`)

const FORBIDDEN = [
  [/Accor/i, 'nom de l’autre prestataire'],
  [/Cosne|Nièvre|Carlone|GianLuca/i, 'lieu ou personne réels dans une maquette en données fictives'],
  [/BOJ|Medhi|Mehdi/i, 'partenaire retiré'],
  [/@[a-z0-9-]+\.[a-z]{2,}/i, 'adresse électronique'],
  [/\b0[1-9](?:[ .]?\d{2}){4}\b/, 'numéro de téléphone'],
  [/lorem ipsum/i, 'texte de remplissage'],
  [/[\u{1F000}-\u{1FAFF}\u{2600}-\u{26FF}\u{FE0F}]/u, 'emoji'],
  [/\b(dashboard|workflow|reporting|deadline|upload|download|settings|login|logout)\b/i, 'mot anglais visible'],
  [/caisse|billetterie|comptabilité|paiement en ligne|réservation de chambre/i, 'fonction exclue de la proposition (caisse, billetterie, comptabilité, paiement, hôtellerie) — à vérifier'],
]

;(async () => {
  const browser = await chromium.launch()
  const run = async (viewport, scale, dir, check) => {
    const ctx = await browser.newContext({ viewport, deviceScaleFactor: scale })
    const page = await ctx.newPage()
    const errs = []
    page.on('pageerror', e => errs.push('script : ' + e.message))
    page.on('console', m => { if (m.type() === 'error') errs.push('console : ' + m.text()) })
    page.on('request', r => { const u = r.url(); if (!u.startsWith('file:') && !u.startsWith('data:') && !u.startsWith('about:')) errs.push('requête externe : ' + u.slice(0, 80)) })
    await page.goto('file://' + path.resolve(out))
    await page.evaluate(() => document.fonts.ready)
    const ids = await page.evaluate(() => [...document.querySelectorAll('section.ecran')].map(s => ({ id: s.id.replace(/^ecran-/, ''), titre: s.dataset.titre || '' })))
    if (!ids.length) { bad('aucun écran trouvé (section.ecran)'); await ctx.close(); return }
    if (dir) fs.mkdirSync(dir, { recursive: true })
    for (const e of ids) {
      await page.evaluate(id => { location.hash = '#/' + id }, e.id)
      await page.waitForTimeout(250)
      if (check) {
        const info = await page.evaluate(id => {
          const vis = el => { const r = el.getBoundingClientRect(); const s = getComputedStyle(el); return r.width > 0 && r.height > 0 && s.visibility !== 'hidden' && s.display !== 'none' }
          const shown = [...document.querySelectorAll('section.ecran')].filter(vis).map(s => s.id)
          const text = document.body.innerText
          let small = 0, smallSample = ''
          const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT)
          while (w.nextNode()) {
            const n = w.currentNode
            if (!n.nodeValue.trim() || !n.parentElement || !vis(n.parentElement)) continue
            const fs = parseFloat(getComputedStyle(n.parentElement).fontSize)
            if (fs < 13) { small++; if (!smallSample) smallSample = n.nodeValue.trim().slice(0, 40) + ' (' + fs + 'px)' }
          }
          return {
            shown, text,
            mention: (text.match(/Maquette — données fictives/g) || []).length,
            overflowX: document.documentElement.scrollWidth - window.innerWidth,
            height: document.documentElement.scrollHeight,
            small, smallSample,
            focusables: document.querySelectorAll('a[href],button,input,select,textarea,[tabindex]').length,
            noName: [...document.querySelectorAll('button,a[href]')].filter(b => vis(b) && !(b.innerText || '').trim() && !b.getAttribute('aria-label') && !b.title).length,
          }
        }, e.id)
        const line = `ÉCRAN   ${e.id.padEnd(22)} hauteur ${String(info.height).padStart(5)} px ; mention ${info.mention} ; texte < 13 px : ${info.small}${info.small ? ' — ex. « ' + info.smallSample + ' »' : ''}`
        console.log(line)
        if (info.shown.length !== 1 || info.shown[0] !== 'ecran-' + e.id) bad(`${e.id} : écrans visibles = [${info.shown.join(', ')}] (attendu : un seul, celui demandé)`)
        if (!info.mention) bad(`${e.id} : mention exacte « Maquette — données fictives » absente de l'écran`)
        if (info.overflowX > 1) bad(`${e.id} : défilement horizontal de ${info.overflowX} px à ${viewport.width} px de large`)
        if (info.small > 6) warn(`${e.id} : ${info.small} textes sous 13 px`)
        if (info.noName) warn(`${e.id} : ${info.noName} bouton(s) ou lien(s) sans nom lisible`)
        if (info.height > viewport.height * 2.6) warn(`${e.id} : écran très long (${info.height} px) — la capture pour diapositive ne montrera que le haut`)
        for (const [rx, msg] of FORBIDDEN) { const h = info.text.match(rx); if (h) (/à vérifier/.test(msg) ? warn : bad)(`${e.id} : ${msg} — « ${info.text.slice(Math.max(0, h.index - 25), h.index + h[0].length + 25).replace(/\s+/g, ' ')} »`) }
      }
      if (dir) await page.screenshot({ path: path.join(dir, e.id + '.png'), fullPage: false })
    }
    for (const m of [...new Set(errs)]) bad(m)
    await ctx.close()
    return ids
  }
  const ids = await run({ width: 1440, height: 900 }, 1, shots ? path.join(shots, 'revue') : null, true)
  if (shots) await run({ width: 1280, height: 720 }, 2, path.join(shots, 'diapo'), false)
  // Petit écran de portable : seulement le défilement horizontal.
  {
    const ctx = await browser.newContext({ viewport: { width: 1180, height: 700 } })
    const page = await ctx.newPage()
    await page.goto('file://' + path.resolve(out))
    for (const e of ids || []) {
      await page.evaluate(id => { location.hash = '#/' + id }, e.id)
      await page.waitForTimeout(120)
      const o = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth)
      if (o > 1) warn(`${e.id} : défilement horizontal de ${o} px à 1180 px de large`)
    }
    await ctx.close()
  }
  await browser.close()
  console.log(`\nÉCRANS=${(ids || []).length} ERREURS=${problems}${shots ? ' ; captures dans ' + shots : ''}`)
  process.exit(problems ? 1 : 0)
})()
