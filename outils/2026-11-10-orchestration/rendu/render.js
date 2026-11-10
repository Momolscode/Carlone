// Rendu approximatif des diapositives (Chromium) pour repérer les débordements.
// Usage : node render.js <dossier project> <dossier de sortie> [id,id,...]
const fs = require('fs')
const path = require('path')
const { chromium } = require('playwright')

const deckDir = process.argv[2]
const outDir = process.argv[3]
const only = process.argv[4] ? process.argv[4].split(',') : null
const fontDir = path.join(__dirname, 'node_modules/@fontsource')
const blobs = fs.existsSync(path.join(__dirname, 'blobs.json')) ? JSON.parse(fs.readFileSync(path.join(__dirname, 'blobs.json'), 'utf8')) : {}
const blobCache = {}
const b64 = f => fs.readFileSync(f).toString('base64')
const face = (family, pkg, slug, w) =>
  `@font-face{font-family:'${family}';font-weight:${w};font-style:normal;src:url(data:font/woff2;base64,${b64(
    path.join(fontDir, pkg, 'files', `${slug}-latin-${w}-normal.woff2`)
  )}) format('woff2')}`
const fonts = [
  ...[500, 600, 700].map(w => face('Cormorant Garamond', 'cormorant-garamond', 'cormorant-garamond', w)),
  ...[400, 500, 700].map(w => face('DM Sans', 'dm-sans', 'dm-sans', w)),
].join('\n')

const css = mode => `${fonts}
html,body{margin:0;background:#888}
*{box-sizing:border-box}
section{width:1920px;position:relative;${mode === 'fixed' ? 'height:1080px;overflow:hidden' : 'height:auto;min-height:0'}}
p,h1,h2,h3,ul,ol,hr,table{margin:0}
h1{font-size:96px}h2{font-size:64px}h3{font-size:44px}p,li,td,th{font-size:32px}
ul,ol{padding-left:1.15em}
table{border-collapse:collapse;width:100%;table-layout:fixed}
td,th{padding:0.35em 0.6em;border:1px solid #CFC8BB;text-align:left;vertical-align:top;line-height:1.4;font-size:inherit}
th{font-weight:700}
aside{display:none}
x-shape{display:block}
x-shape[kind="arrow-right"]{clip-path:polygon(0 30%,65% 30%,65% 0,100% 50%,65% 100%,65% 70%,0 70%)}
x-shape[kind="arrow-left"]{clip-path:polygon(100% 30%,35% 30%,35% 0,0 50%,35% 100%,35% 70%,100% 70%)}
x-shape[kind="arrow-down"]{clip-path:polygon(30% 0,70% 0,70% 65%,100% 65%,50% 100%,0 65%,30% 65%)}
x-shape[kind="arrow-up"]{clip-path:polygon(30% 100%,70% 100%,70% 35%,100% 35%,50% 0,0 35%,30% 35%)}
x-shape[kind="ellipse"]{border-radius:50%}
x-shape[kind="diamond"]{clip-path:polygon(50% 0,100% 50%,50% 100%,0 50%)}
x-icon{display:inline-block;width:1em;height:1em;border:2px solid;border-radius:6px;flex:none}
img{background:#3a3f48}
section>*{position:relative}
`

;(async () => {
  const deck = JSON.parse(fs.readFileSync(path.join(deckDir, 'deck.json'), 'utf8'))
  const ids = (only || deck.order)
  fs.mkdirSync(outDir, { recursive: true })
  const browser = await chromium.launch()
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 0.5 })
  const report = []
  for (const id of ids) {
    const file = path.join(deckDir, 'slides', id + '.html')
    if (!fs.existsSync(file)) { report.push({ id, error: 'fichier absent' }); continue }
    const html = fs.readFileSync(file, 'utf8').replace(/\/_blob\/([0-9a-f]{32})/g, (m, id) => {
      const local = path.join(__dirname, 'blobs', id + '.jpg')
      if (!fs.existsSync(local)) return m
      if (!blobCache[id]) blobCache[id] = 'data:image/jpeg;base64,' + fs.readFileSync(local).toString('base64')
      return blobCache[id]
    })
    // passe 1 : hauteur naturelle
    await page.setContent(`<html><head><style>${css('natural')}</style></head><body>${html}</body></html>`)
    await page.evaluate(() => document.fonts.ready)
    const m = await page.evaluate(() => {
      const s = document.querySelector('section')
      const sections = document.querySelectorAll('section').length
      const natural = s.offsetHeight
      const cs = getComputedStyle(s)
      const padB = parseFloat(cs.paddingBottom), padT = parseFloat(cs.paddingTop)
      const padL = parseFloat(cs.paddingLeft), padR = parseFloat(cs.paddingRight)
      let minFont = 999, small = []
      const wide = []
      const all = [...s.querySelectorAll('*')].filter(e => !e.closest('aside'))
      for (const e of all) {
        const hasText = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())
        if (hasText) {
          const fs_ = parseFloat(getComputedStyle(e).fontSize)
          if (fs_ < minFont) minFont = fs_
          if (fs_ < 24) small.push(fs_ + 'px: ' + e.textContent.trim().slice(0, 40))
        }
        const r = e.getBoundingClientRect()
        if (r.right > 1920 - padR + 1 && getComputedStyle(e).position !== 'absolute' && !e.closest('[style*="position:absolute"]'))
          wide.push(e.tagName + ' droite=' + Math.round(r.right) + ' : ' + e.textContent.trim().slice(0, 40))
        if (e.scrollWidth > e.clientWidth + 2 && e.clientWidth > 0)
          wide.push(e.tagName + ' contenu plus large que la boîte (' + e.scrollWidth + '>' + e.clientWidth + ') : ' + e.textContent.trim().slice(0, 40))
      }
      const clone = s.cloneNode(true)
      clone.querySelectorAll('aside').forEach(a => a.remove())
      const text = clone.textContent.replace(/\s+/g, ' ').trim()
      const words = text ? text.split(' ').length : 0
      const title = (s.querySelector('h1,h2') || {}).textContent || ''
      const aside = s.querySelector('aside')
      const pinned = [...s.children].filter(e => getComputedStyle(e).position === 'absolute')
      const pinnedOut = pinned.filter(e => { const r = e.getBoundingClientRect(); return r.right > 1793 || r.left < 127 }).length
      return { sections, natural, padT, padB, padL, minFont, small, wide: wide.slice(0, 6), words, elements: all.length,
        title: title.trim(), titleChars: title.trim().length, notesChars: aside ? aside.textContent.length : 0, pinned: pinned.length, pinnedOut }
    })
    // passe 2 : image à hauteur fixe
    await page.setContent(`<html><head><style>${css('fixed')}</style></head><body>${html}</body></html>`)
    await page.evaluate(() => document.fonts.ready)
    const y = await page.evaluate(() => {
      const s = document.querySelector('section')
      const t = s.querySelector('h1,h2')
      return t ? Math.round(t.getBoundingClientRect().top) : null
    })
    await page.screenshot({ path: path.join(outDir, id + '.png'), clip: { x: 0, y: 0, width: 1920, height: 1080 } })
    report.push({ id, ...m, titleTop: y, overflow: m.natural - 1080 })
  }
  await browser.close()
  fs.writeFileSync(path.join(outDir, 'report.json'), JSON.stringify(report, null, 1))
  for (const r of report) {
    if (r.error) { console.log(r.id.padEnd(16), r.error); continue }
    console.log(
      r.id.padEnd(16),
      ('haut. ' + r.natural).padEnd(11),
      (r.overflow > 0 ? 'DÉBORDE +' + r.overflow : 'marge ' + (-r.overflow)).padEnd(14),
      ('mots ' + r.words).padEnd(9),
      ('min ' + r.minFont + 'px').padEnd(10),
      ('titre ' + r.titleChars + 'c y=' + r.titleTop).padEnd(18),
      'élts ' + r.elements,
      r.wide.length ? ' | LARGEUR: ' + r.wide[0] : '',
      r.sections !== 1 ? ' | SECTIONS=' + r.sections : ''
    )
  }
})()
