// Contrôle mécanique d'un document destiné au client (Markdown ou HTML) : lignes rouges, prix, typographie.
// Usage : node lint-doc.js [--tarifs-publics] [--interne] <fichier> [<fichier> …]
//   --tarifs-publics : un montant inconnu devient une ALERTE (document qui cite des tarifs officiels avec leur source).
//   --interne        : document interne ; seules les règles valables partout sont appliquées (nom du client, emoji, adresse électronique).
// Sortie : une ligne par constat « fichier:ligne NIVEAU message », puis un total. Code de sortie 1 s'il reste une ERREUR.
const fs = require('fs')
const path = require('path')

const args = process.argv.slice(2)
const publicFees = args.includes('--tarifs-publics')
const internal = args.includes('--interne')
const files = args.filter(a => !a.startsWith('--'))
if (!files.length) { console.error('Usage : node lint-doc.js [--tarifs-publics] [--interne] <fichier> …'); process.exit(2) }

const RED_ALL = [
  [/John[- ]?Lucas(?!\s*»?\s*\[sic)/i, 'ERREUR', 'nom du client mal écrit (hors citation suivie de [sic, lire GianLuca])'],
  [/Gian[- ]luca|Gianluca|GianLucca|Carlonne/, 'ERREUR', 'nom du client : écrire « GianLuca Carlone »'],
  [/[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[a-z]{2,}/, 'ERREUR', 'adresse électronique écrite dans le document'],
]
const RED_CLIENT = [
  [/1[,.]5\s*M\b|1[,.]5\s*million|\bmillions?\b/i, 'ERREUR', 'montant des bâtiments ou « million »'],
  [/\bJP\b|journées?[- ]personnes?/i, 'ERREUR', '« JP » ou « journée-personne »'],
  [/\bsocle\b/i, 'ERREUR', '« socle »'],
  [/\bvoies?\b(?!\s+(publique|publiques|de recours|ferrée|d’accès|d'accès))/i, 'ERREUR', '« voie » (mot interne)'],
  [/(?<!surface de |surfaces de )plancher/i, 'ERREUR', '« plancher » (prix plancher interne)'],
  [/(?<!TVA sur la |régime de la |taxation sur la |taxe sur la |imposition sur la )\bmarges?\b(?! bénéficiaire du régime)/i, 'ERREUR', '« marge » (hors « TVA sur la marge », régime fiscal des œuvres)'],
  [/taux journalier|tarif journalier|prix (par|à la) jour/i, 'ERREUR', 'taux journalier'],
  [/\bD\d{2}\b|\bDL\d+\b|\bU\d{2}\b|\[(FV|DR|PR|HY|ES|MM|IN)\]/, 'ERREUR', 'code de l’audit'],
  [/BOJ|Medhi|Mehdi/i, 'ERREUR', 'partenaire retiré de l’offre'],
  [/Quali ?Contact/i, 'ERREUR', 'tiers nommé'],
  [/mieux et moins cher/i, 'ERREUR', '« mieux et moins cher »'],
  [/6[\s  ]?000[\s  ]?(€|euros)|\b15[\s  ]?000\b|\b30[\s  ]?000\b|\b72[\s  ]?000\b|\b24[\s  ]?000\b/, 'ERREUR', 'prix de l’autre proposition ou ancienne offre mensuelle'],
  [/\bAccor(hotels|invest)?\b/i, 'ERREUR', 'nom de l’autre prestataire : ne jamais le nommer dans un texte client'],
  [/(^|[^a-zà-ÿ’'])Accord(?![a-zà-ÿ])/, 'ALERTE', '« Accord » avec majuscule : vérifier que ce n’est pas le nom de l’autre prestataire'],
  [/garanti(?!e de parfait achèvement|e décennale|e légale)/i, 'ALERTE', '« garanti… » : aucune garantie de résultat ne doit être donnée'],
  [/remplac/i, 'ALERTE', '« remplac… » : l’administratrice n’est jamais remplacée'],
  [/surveill|contrôl(e|er) (son|le) travail/i, 'ALERTE', '« surveill… » : l’administratrice n’est jamais surveillée'],
  [/(^|[\s(«])(tu|ton|ta|tes|toi)(?=[\s,.;:!?»)])/i, 'ALERTE', 'tutoiement possible'],
  [/not(e|er|ation) (les|des) (candidats|salariés)|classe(r)? les candidats/i, 'ALERTE', 'notation de candidats ou de salariés'],
  [/\b(workflow|dashboard|pipeline|onboarding|reporting|business|feedback|deadline|roadmap|process|backlog|kick-?off|quick win|use case|scal(e|able)|insight|back-?office|front-?office|no-?code|low-?code|prompt|chatbot|data|cloud|booster|disrupt)\b/i, 'ALERTE', 'anglais ou jargon'],
  [/révolution|incontournable|100\s?%|zéro (erreur|risque)|sans (aucun )?risque|toujours à jour|en temps réel|clé en main|leader|n°\s?1\b|meilleur/i, 'ALERTE', 'formule creuse ou promesse absolue'],
  [/\bimmédiatement\b|dès demain|en quelques (clics|minutes|secondes)/i, 'ALERTE', 'promesse de délai'],
  [/dernière chance|offre limitée|avant qu’il ne soit trop tard|ne ratez pas|\burgent/i, 'ERREUR', 'pression commerciale'],
  [/nos clients|d’autres clients|références clients|témoignage/i, 'ALERTE', 'référence client : aucune ne doit être inventée'],
  [/démonstration gratuite|satisfait ou remboursé|\bremise\s+de\s+\d|\boffert(e|s)?\b|\bgratuit(e|s|ement)?\b/i, 'ALERTE', 'gratuité, remise ou remboursement : rien de tel n’est prévu'],
  [/Marwin Tech (est|a été) (créée|immatriculée)|notre société existe/i, 'ERREUR', 'la société est présentée comme déjà immatriculée'],
  [/photo(graphie)? (du|de la|des|de votre|de vos) /i, 'ALERTE', '« photo de… » : une image générée n’est jamais présentée comme une photo réelle'],
]
const EMOJI = /[\u{1F000}-\u{1FAFF}\u{2600}-\u{27BF}\u{2B00}-\u{2BFF}\u{FE0F}]/u
const PRICE_OK = new Set(['6500', '7800', '3250', '3900', '1300'])
const PRICE_DOC = new Set(['3000', '5300', '10400', '15700', '18700', '7500', '6400', '1200', '2300', '700', '1000', '1400', '1500', '22200', '25200', '80', '430', '70', '275', '40', '85', '100', '46300', '68500', '79000', '97700', '57000', '240000', '14000', '10300', '37000'])

let errors = 0, alerts = 0
for (const file of files) {
  const name = path.basename(file)
  if (!fs.existsSync(file)) { errors++; console.log(`${name} ERREUR fichier absent`); continue }
  let raw = fs.readFileSync(file, 'utf8')
  const isHtml = /\.html?$/i.test(file)
  if (isHtml) raw = raw.replace(/<style[\s\S]*?<\/style>/gi, m => m.replace(/[^\n]/g, '')).replace(/<script[\s\S]*?<\/script>/gi, m => m.replace(/[^\n]/g, ''))
  const lines = raw.split('\n')
  const say = (n, level, msg) => { level === 'ERREUR' ? errors++ : alerts++; console.log(`${name}:${n} ${level}  ${msg}`) }
  let straight = 0, inCode = false
  lines.forEach((line0, i) => {
    const n = i + 1
    if (/^```/.test(line0)) { inCode = !inCode; return }
    let line = isHtml ? line0.replace(/<[^>]*>/g, ' ').replace(/&nbsp;/g, ' ').replace(/&amp;/g, '&') : line0.replace(/\]\([^)]*\)/g, ']').replace(/<[^>]*>/g, ' ')
    if (!line.trim()) return
    for (const [rx, level, msg] of RED_ALL) { const h = line.match(rx); if (h) say(n, level, `${msg} : « …${line.slice(Math.max(0, h.index - 30), h.index + h[0].length + 30).trim()}… »`) }
    if (EMOJI.test(line.replace(/[☐☑☒✓✔]/g, ''))) say(n, 'ERREUR', 'emoji ou pictogramme')
    if (internal) return
    for (const [rx, level0, msg] of RED_CLIENT) {
      const h = line.match(rx)
      if (!h) continue
      // Document qui cite des tarifs et des seuils officiels : un montant rond n'est pas forcément le prix de l'autre proposition.
      const level = (publicFees && /prix de l’autre proposition/.test(msg)) ? 'ALERTE' : level0
      say(n, level, `${msg} : « …${line.slice(Math.max(0, h.index - 30), h.index + h[0].length + 30).trim()}… »`)
    }
    for (const p of line.matchAll(/(\d{1,3}(?:[\s  ]\d{3})+|\d+)(?:,\d+)?[\s  ]?(?:€|euros?\b)/g)) {
      const v = p[1].replace(/[\s  ]/g, '')
      if (PRICE_OK.has(v)) continue
      if (PRICE_DOC.has(v)) say(n, 'ALERTE', `prix ${p[0]} : figure dans un document client du 9 novembre, à valider par Morgan et Mathys`)
      else say(n, publicFees ? 'ALERTE' : 'ERREUR', `prix ${p[0]} : absent des documents clients${publicFees ? ' (tarif public : la source est-elle citée sur la ligne ?)' : ''}`)
    }
    if (!isHtml && /[A-Za-zÀ-ÿ]'[A-Za-zÀ-ÿ]/.test(line.replace(/`[^`]*`/g, ''))) straight++
  })
  if (!internal && straight) say(0, 'ALERTE', `${straight} ligne(s) avec une apostrophe droite (typographie française : ’)`)
  const all = lines.join('\n')
  if (!internal && /maquette/i.test(all) && !/Maquette — données fictives/.test(all)) say(0, 'ERREUR', 'maquette sans la mention exacte « Maquette — données fictives »')
  if (!internal && /6[\s  ]500/.test(all) && !/HT|hors taxes/.test(all)) say(0, 'ALERTE', '6 500 € sans « HT »')
  if (!internal && !/PROJET|Projet non envoyé/i.test(all)) say(0, 'ALERTE', 'mention « PROJET non envoyé, à valider par Morgan Olsen et Mathys Couet » absente')
  const words = all.replace(/[#*_>|`-]/g, ' ').split(/\s+/).filter(Boolean).length
  console.log(`${name} : ${words} mots`)
}
console.log(`\nTotal : ${errors} erreur(s), ${alerts} alerte(s) sur ${files.length} fichier(s).`)
process.exit(errors ? 1 : 0)
