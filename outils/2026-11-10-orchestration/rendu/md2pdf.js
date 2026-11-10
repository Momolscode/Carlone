// Markdown -> PDF A4 mis en page (charte Marwin Tech : Cormorant Garamond + DM Sans, encre et bronze).
// Usage : node md2pdf.js <entrée.md> <sortie.pdf> [--bandeau "texte"] [--pied "texte"] [--compact] [--paysage]
// Affiche : PAGES=<n> et le chemin écrit. Ne modifie jamais le fichier d'entrée.
const fs = require('fs')
const path = require('path')
const { chromium } = require('playwright')
const { marked } = require('marked')

const argv = process.argv.slice(2)
const input = argv[0], output = argv[1]
if (!input || !output) { console.error('Usage : node md2pdf.js <entrée.md> <sortie.pdf> [--bandeau "texte"] [--pied "texte"] [--compact] [--paysage]'); process.exit(2) }
const opt = name => { const i = argv.indexOf('--' + name); return i >= 0 ? argv[i + 1] : null }
const flag = name => argv.includes('--' + name)
const bandeau = opt('bandeau')
const pied = opt('pied') || 'Marwin Tech'
const compact = flag('compact')
const paysage = flag('paysage')

const fontDir = path.join(__dirname, 'node_modules/@fontsource')
const b64 = f => fs.readFileSync(f).toString('base64')
const face = (family, pkg, w, style) =>
  `@font-face{font-family:'${family}';font-weight:${w};font-style:${style};src:url(data:font/woff2;base64,${b64(
    path.join(fontDir, pkg, 'files', `${pkg}-latin-${w}-${style}.woff2`)
  )}) format('woff2')}`
const fonts = [
  ...[500, 600, 700].flatMap(w => ['normal', 'italic'].map(s => face('Cormorant Garamond', 'cormorant-garamond', w, s))),
  ...[400, 500, 700].flatMap(w => ['normal', 'italic'].map(s => face('DM Sans', 'dm-sans', w, s))),
].join('\n')

const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
let md = fs.readFileSync(input, 'utf8')
// Cases à cocher : « - [ ] » et « ☐ » deviennent de vraies cases dessinées.
md = md.replace(/^(\s*[-*] )\[ \] /gm, '$1<span class="case"></span> ').replace(/^(\s*[-*] )\[x\] /gim, '$1<span class="case coche"></span> ')
md = md.replace(/☐/g, '<span class="case"></span>').replace(/☑|☒/g, '<span class="case coche"></span>')
// Typographie française : espace insécable avant ; : ? ! » € % et après «, hors des passages de code (les sources ne sont pas modifiées).
const insecables = t => t.replace(/ ([;:?!»€%])/g, '\u00A0$1').replace(/« /g, '«\u00A0')
const typo = h => h.split(/(<code[\s\S]*?<\/code>|<pre[\s\S]*?<\/pre>)/).map((seg, i) => (i % 2 ? seg : seg.replace(/>([^<]+)</g, (m, t) => '>' + insecables(t) + '<'))).join('')
const body = typo(marked.parse(md, { gfm: true, breaks: false }))

const base = compact ? 9.4 : 10.4
const css = `${fonts}
@page{size:A4 ${paysage ? 'landscape' : 'portrait'};margin:${compact ? '14mm 15mm 16mm' : '18mm 18mm 20mm'}}
*{box-sizing:border-box}
html{font-size:${base}pt}
body{margin:0;font-family:'DM Sans',Arial,sans-serif;color:#14181F;line-height:1.5;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.bandeau{border:1px solid #B08D57;color:#7E5F31;background:#FFFDF9;font-size:0.82rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;padding:5pt 9pt;margin:0 0 12pt;border-radius:2pt}
h1{font-family:'Cormorant Garamond',Georgia,serif;font-weight:600;font-size:2.5rem;line-height:1.1;margin:0 0 10pt;color:#14181F}
h2{font-family:'Cormorant Garamond',Georgia,serif;font-weight:600;font-size:1.7rem;line-height:1.15;margin:${compact ? '12pt' : '18pt'} 0 6pt;padding-bottom:3pt;border-bottom:1px solid #D9D2C5;color:#14181F;break-after:avoid}
h3{font-family:'DM Sans',Arial,sans-serif;font-weight:700;font-size:1.08rem;margin:${compact ? '9pt' : '13pt'} 0 4pt;color:#7E5F31;break-after:avoid}
h4{font-weight:700;font-size:1rem;margin:9pt 0 3pt;break-after:avoid}
p{margin:0 0 ${compact ? '5pt' : '7pt'}}
ul,ol{margin:0 0 ${compact ? '5pt' : '7pt'};padding-left:1.25em}
li{margin:0 0 2.5pt}
li>p{margin:0 0 2.5pt}
li:has(>.case){list-style:none;margin-left:-1.25em;padding-left:0}
.case{display:inline-block;width:0.95em;height:0.95em;border:1.2px solid #14181F;border-radius:1.5pt;vertical-align:-0.12em;margin-right:0.35em;background:#fff}
.case.coche{background:#7E5F31;border-color:#7E5F31}
strong{font-weight:700}
a{color:#7E5F31;text-decoration:none}
hr{border:0;border-top:1px solid #D9D2C5;margin:12pt 0}
blockquote{margin:0 0 8pt;padding:7pt 10pt;background:#FFFDF9;border:1px solid #D9D2C5;border-left:3pt solid #B08D57;border-radius:2pt;break-inside:avoid}
blockquote p:last-child{margin-bottom:0}
table{border-collapse:collapse;width:100%;margin:0 0 9pt;font-size:0.93rem}
thead{display:table-header-group}
tr{break-inside:avoid}
th{background:#F6F3EE;font-weight:700;text-align:left;border:1px solid #D9D2C5;padding:4pt 6pt;vertical-align:bottom}
td{border:1px solid #D9D2C5;padding:4pt 6pt;vertical-align:top}
code{font-family:'DM Sans',Arial,sans-serif;background:#F6F3EE;padding:0 2pt;border-radius:2pt;font-size:0.95em}
pre{background:#F6F3EE;border:1px solid #D9D2C5;padding:7pt 9pt;border-radius:2pt;white-space:pre-wrap;font-size:0.92rem;break-inside:avoid}
pre code{background:none;padding:0}
.signature td{height:60pt}
`
const html = `<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>${css}</style></head><body>${bandeau ? `<div class="bandeau">${esc(bandeau)}</div>` : ''}${body}</body></html>`

;(async () => {
  const browser = await chromium.launch()
  const page = await browser.newPage()
  await page.setContent(html, { waitUntil: 'load' })
  await page.evaluate(() => document.fonts.ready)
  fs.mkdirSync(path.dirname(path.resolve(output)), { recursive: true })
  const footer = `<div style="width:100%;font-family:Arial,sans-serif;font-size:7.5pt;color:#5F636C;padding:0 18mm;display:flex;justify-content:space-between"><span>${esc(pied)}</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>`
  const buf = await page.pdf({ path: output, format: 'A4', landscape: paysage, printBackground: true, displayHeaderFooter: true, headerTemplate: '<span></span>', footerTemplate: footer, preferCSSPageSize: true })
  await browser.close()
  const pages = (buf.toString('latin1').match(/\/Type\s*\/Page[^s]/g) || []).length
  console.log('PAGES=' + pages, output)
})()
