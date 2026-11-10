// Parcourt la maquette : chaque entrée du menu ouvre un écran, qui porte la mention « Maquette — données fictives ».
// Usage : node test-maquette.js <chemin absolu de index.html>
const { chromium } = require('playwright')
;(async () => {
  const file = process.argv[2]
  const b = await chromium.launch()
  const p = await b.newPage({ viewport: { width: 1440, height: 900 } })
  const errs = []
  const reqs = []
  p.on('console', m => { if (m.type() === 'error') errs.push(m.text()) })
  p.on('pageerror', e => errs.push(String(e)))
  p.on('request', r => { if (!r.url().startsWith('file:') && !r.url().startsWith('data:')) reqs.push(r.url()) })
  await p.goto('file://' + file)
  const sel = 'nav a, nav button, .menu a, .menu button, aside a, aside button'
  const items = await p.$$(sel)
  let n = 0
  for (const it of items) {
    const label = ((await it.innerText()) || '').trim()
    if (!label) continue
    await it.click()
    await p.waitForTimeout(120)
    const vis = await p.evaluate(() => {
      const secs = [...document.querySelectorAll('main section, main .ecran, section.ecran, .ecran')].filter(s => s.offsetParent !== null && s.getBoundingClientRect().height > 100)
      const s = secs[0] || document.querySelector('main')
      if (!s) return null
      const t = s.innerText
      const h = s.querySelector('h1,h2')
      return { titre: h ? h.innerText : '', mention: /maquette — données fictives/i.test(t), mots: t.split(/\s+/).length, hotel: /hôtel/i.test(t) }
    })
    n++
    console.log(String(n).padStart(2), label.padEnd(22), JSON.stringify(vis))
  }
  const all = await p.evaluate(() => ({ liensExternes: document.querySelectorAll('a[href^="http"]').length, saisies: document.querySelectorAll('input, textarea, select').length, scriptsExternes: [...document.scripts].filter(s => s.src).length }))
  console.log('liens externes, champs de saisie, scripts externes :', JSON.stringify(all))
  console.log('erreurs console :', errs.length, errs.slice(0, 3))
  console.log('requêtes réseau :', reqs.length, reqs.slice(0, 3))
  await b.close()
})()
