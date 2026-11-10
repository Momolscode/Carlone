// Génère les gabarits de la v12 (exemples testés). Usage : node gen.js
const fs = require('fs'), path = require('path')
const SERIF = "font-family:'Cormorant Garamond', Georgia, serif"
const SANS = "font-family:'DM Sans', Arial, sans-serif"
const light = (id, extra = '') => `<section id="${id}" data-transition="fade" style="background:#F6F3EE;color:#14181F;${SANS};padding:120px 128px 160px;display:flex;flex-direction:column;gap:40px${extra}">`
const dark = (id, extra = '') => `<section id="${id}" data-transition="fade" style="background:#14181F;color:#F3EFE8;${SANS};padding:120px 128px 160px;display:flex;flex-direction:column;gap:40px${extra}">`
const head = (eyebrow, title) => `<div style="display:flex;flex-direction:column;gap:14px">
<p style="font-size:24px;font-weight:500;letter-spacing:4px;text-transform:uppercase;color:#7E5F31">${eyebrow}</p>
<h2 style="${SERIF};font-size:64px;font-weight:600;line-height:1.08;color:#14181F">${title}</h2>
</div>`
const foot = (n, darkBg) => `<p style="position:absolute;left:128px;bottom:64px;width:1664px;font-size:24px;color:${darkBg ? '#9A9286' : '#5F636C'}">Marwin Tech · pour GianLuca Carlone · novembre 2026 · ${n}</p>`
const G = {}

G['g-enonce'] = `${dark('g-enonce', ';justify-content:center')}
<p style="font-size:24px;font-weight:500;letter-spacing:4px;text-transform:uppercase;color:#B08D57">Surtitre court</p>
<h2 style="${SERIF};font-size:92px;font-weight:600;line-height:1.06;color:#F3EFE8">Une seule phrase forte, sur deux lignes au plus, qui dit l’idée.</h2>
<p style="font-size:34px;line-height:1.4;color:#E7E1D6">Une phrase d’appui, courte, qui précise la condition ou la preuve.</p>
${foot(3, true)}
<aside>Notes de l’orateur, sûres pour le client.</aside>
</section>`

const card3 = (n, h, t, hi) => `<div style="flex:1;display:flex;flex-direction:column;gap:16px;background:#FFFDF9;border:${hi ? '2px solid #B08D57' : '1px solid #D9D2C5'};border-radius:16px;padding:36px">
<p style="${SERIF};font-size:64px;font-weight:600;line-height:1.0;color:#7E5F31">${n}</p>
<h3 style="font-size:36px;font-weight:700;line-height:1.2;color:#14181F">${h}</h3>
<p style="font-size:28px;line-height:1.4;color:#3D4450">${t}</p>
</div>`
G['g-cartes-3'] = `${light('g-cartes-3')}
${head('Surtitre', 'Un titre qui affirme, cinquante-cinq caractères au plus')}
<div style="display:flex;gap:32px;align-items:stretch">
${card3('1', 'Titre de carte', 'Vingt mots au plus par carte. Une phrase sur ce que cela change pour lui, une autre sur la condition.', true)}
${card3('2', 'Titre de carte', 'Vingt mots au plus par carte. Une phrase sur ce que cela change pour lui, une autre sur la condition.')}
${card3('3', 'Titre de carte', 'Vingt mots au plus par carte. Une phrase sur ce que cela change pour lui, une autre sur la condition.')}
</div>
<p style="${SERIF};font-size:40px;font-weight:600;line-height:1.2;color:#F3EFE8;background:#14181F;border-radius:16px;padding:28px 40px">Bandeau facultatif : la phrase à retenir, quinze mots au plus.</p>
${foot(4)}
<aside>Notes de l’orateur.</aside>
</section>`

const row = (h, a, b) => `<p style="font-size:28px;font-weight:700;line-height:1.35;color:#7E5F31;padding:20px 0px 20px 0px;border-top:1px solid #D9D2C5">${h}</p>
<p style="font-size:28px;line-height:1.35;color:#5F636C;padding:20px 0px 20px 0px;border-top:1px solid #D9D2C5">${a}</p>
<p style="font-size:28px;line-height:1.35;color:#14181F;padding:20px 0px 20px 0px;border-top:1px solid #D9D2C5">${b}</p>`
G['g-avant-apres'] = `${light('g-avant-apres', '')}
${head('Surtitre', 'Avant et après : un titre de cinquante-cinq caractères')}
<div style="display:grid;grid-template-columns:220px 1fr 1fr;gap:0px 40px">
<p style="font-size:24px;font-weight:500;letter-spacing:3px;text-transform:uppercase;color:#5F636C;padding:0px 0px 12px 0px">Moment</p>
<p style="font-size:24px;font-weight:500;letter-spacing:3px;text-transform:uppercase;color:#5F636C;padding:0px 0px 12px 0px">Aujourd’hui</p>
<p style="font-size:24px;font-weight:500;letter-spacing:3px;text-transform:uppercase;color:#7E5F31;padding:0px 0px 12px 0px">Avec l’aide préparée</p>
${row('Le matin', 'Une ligne courte, douze mots au plus, qui décrit la tâche.', 'Une ligne courte, douze mots au plus : ce qui est prêt, ce qu’elle valide.')}
${row('À midi', 'Une ligne courte, douze mots au plus, qui décrit la tâche.', 'Une ligne courte, douze mots au plus : ce qui est prêt, ce qu’elle valide.')}
${row('L’après-midi', 'Une ligne courte, douze mots au plus, qui décrit la tâche.', 'Une ligne courte, douze mots au plus : ce qui est prêt, ce qu’elle valide.')}
${row('Le soir', 'Une ligne courte, douze mots au plus, qui décrit la tâche.', 'Une ligne courte, douze mots au plus : ce qui est prêt, ce qu’elle valide.')}
</div>
${foot(5)}
<aside>Notes de l’orateur.</aside>
</section>`

const mrow = (a, b, chip, col) => `<div style="display:flex;gap:24px;align-items:center;padding:18px 28px;border-top:1px solid #E7E1D6">
<p style="flex:1;font-size:26px;font-weight:700;line-height:1.3;color:#14181F">${a}</p>
<p style="flex:1;font-size:24px;line-height:1.3;color:#5F636C">${b}</p>
<p style="font-size:24px;font-weight:700;line-height:1.2;color:${col};background:#F3EFE8;border-radius:24px;padding:8px 20px">${chip}</p>
</div>`
G['g-maquette'] = `${light('g-maquette')}
${head('Surtitre', 'Ce que vous verriez : un titre court et concret')}
<div style="display:flex;gap:48px;align-items:start">
<div style="width:540px;display:flex;flex-direction:column;gap:20px">
<p style="font-size:30px;line-height:1.4;color:#14181F"><b>Une phrase qui dit ce que l’écran montre.</b></p>
<ul style="font-size:28px;line-height:1.45;color:#3D4450">
<li>Un bénéfice concret</li>
<li>Qui valide quoi</li>
<li>Ce qui reste à lui</li>
</ul>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;flex-direction:column;background:#FFFDF9;border:1px solid #D9D2C5;border-radius:16px;overflow:hidden;box-shadow:0px 12px 32px #14181F1F">
<div style="display:flex;gap:12px;align-items:center;background:#14181F;padding:18px 28px">
<x-shape kind="ellipse" style="width:14px;height:14px;background:#B08D57"></x-shape>
<p style="font-size:24px;font-weight:500;line-height:1.2;color:#F3EFE8">Titre de l’écran · exemple</p>
</div>
${mrow('Ligne un', 'Détail court', 'Dans 12 jours', '#7E5F31')}
${mrow('Ligne deux', 'Détail court', 'À valider', '#8A3B2E')}
${mrow('Ligne trois', 'Détail court', 'À jour', '#3F6B4F')}
${mrow('Ligne quatre', 'Détail court', 'Dans 45 jours', '#7E5F31')}
${mrow('Ligne cinq', 'Détail court', 'À jour', '#3F6B4F')}
</div>
<p style="font-size:24px;line-height:1.3;color:#5F636C">Maquette — données fictives</p>
</div>
</div>
${foot(6)}
<aside>Notes de l’orateur.</aside>
</section>`

const step = (n, h, d, c, hi, dash) => `<div style="flex:1;display:flex;flex-direction:column;gap:12px;background:#FFFDF9;border:${hi ? '2px solid #B08D57' : dash ? '1px dashed #B5AC9C' : '1px solid #D9D2C5'};border-radius:16px;padding:32px">
<p style="${SERIF};font-size:64px;font-weight:600;line-height:1.0;color:#7E5F31">${n}</p>
<h3 style="font-size:36px;font-weight:700;line-height:1.2;color:#14181F">${h}</h3>
<p style="font-size:26px;line-height:1.4;color:#5F636C">${d}</p>
<p style="font-size:26px;line-height:1.4;color:#3D4450">${c}</p>
</div>`
const arrow = `<div style="display:flex;align-items:center"><x-shape kind="arrow-right" style="width:48px;height:24px;background:#B08D57"></x-shape></div>`
G['g-etapes'] = `${light('g-etapes')}
${head('Surtitre', 'Trois étapes, et vous décidez à chacune')}
<div style="display:flex;gap:16px;align-items:stretch">
${step('1', 'Cadrer', 'Trois à quatre semaines', 'Ce que vous recevez, en dix mots.', true)}
${arrow}
${step('2', 'Essayer', 'Huit semaines', 'Ce que vous recevez, en dix mots.')}
${arrow}
${step('3', 'Installer', 'Suivi revu chaque trimestre', 'Ce que vous recevez, en dix mots.')}
</div>
<p style="${SERIF};font-size:40px;font-weight:600;line-height:1.2;color:#F3EFE8;background:#14181F;border-radius:16px;padding:28px 40px">Bandeau : la phrase à retenir, quinze mots au plus.</p>
${foot(7)}
<aside>Notes de l’orateur.</aside>
</section>`

G['g-grand-chiffre'] = `${light('g-grand-chiffre')}
${head('Surtitre', 'Un prix fixe, connu avant de commencer')}
<div style="display:flex;gap:64px;align-items:stretch">
<div style="width:680px;display:flex;flex-direction:column;gap:16px;justify-content:center">
<p style="${SERIF};font-size:168px;font-weight:600;line-height:1.0;color:#14181F">6 500 €</p>
<p style="font-size:32px;line-height:1.35;color:#3D4450"><b>hors taxes, au forfait.</b> Une ligne de précision, quinze mots au plus.</p>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px;background:#FFFDF9;border:2px solid #B08D57;border-radius:16px;padding:40px">
<h3 style="font-size:34px;font-weight:700;line-height:1.2;color:#14181F">Ce que vous recevez</h3>
<ul style="font-size:28px;line-height:1.5;color:#3D4450">
<li>Premier élément, dix mots au plus</li>
<li>Deuxième élément, dix mots au plus</li>
<li>Troisième élément, dix mots au plus</li>
<li>Quatrième élément, dix mots au plus</li>
</ul>
</div>
</div>
<p style="font-size:28px;line-height:1.4;color:#3D4450">Une ligne sous le bloc : la condition ou la garantie, vingt mots au plus.</p>
${foot(8)}
<aside>Notes de l’orateur.</aside>
</section>`

const hor = (chip, h, items, cond, hi) => `<div style="flex:1;display:flex;flex-direction:column;gap:16px;border-top:4px solid ${hi ? '#B08D57' : '#B5AC9C'};padding:28px 0px 0px 0px">
<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#7E5F31">${chip}</p>
<h3 style="${SERIF};font-size:52px;font-weight:600;line-height:1.1;color:#14181F">${h}</h3>
<ul style="font-size:28px;line-height:1.45;color:#3D4450">
${items.map(i => `<li>${i}</li>`).join('\n')}
</ul>
<p style="font-size:24px;line-height:1.4;color:#5F636C">${cond}</p>
</div>`
G['g-frise'] = `${light('g-frise')}
${head('Surtitre', 'Dans un an, deux ans, cinq ans')}
<div style="display:flex;gap:48px;align-items:stretch">
${hor('Déjà possible', 'Dans un an', ['Un point, huit mots au plus', 'Un point, huit mots au plus', 'Un point, huit mots au plus'], 'Condition : une ligne courte.', true)}
${hor('Probable', 'Dans deux ans', ['Un point, huit mots au plus', 'Un point, huit mots au plus', 'Un point, huit mots au plus'], 'Condition : une ligne courte.')}
${hor('Un pari', 'Dans cinq ans', ['Un point, huit mots au plus', 'Un point, huit mots au plus', 'Un point, huit mots au plus'], 'Condition : une ligne courte.')}
</div>
${foot(9)}
<aside>Notes de l’orateur.</aside>
</section>`

const chk = t => `<div style="display:flex;gap:20px;align-items:start">
<x-icon name="CheckCircle" style="color:#7E5F31;width:48px;height:48px"></x-icon>
<p style="flex:1;font-size:30px;line-height:1.4;color:#14181F">${t}</p>
</div>`
const wk = (w, t) => `<div style="display:flex;gap:24px;align-items:baseline;padding:16px 0px 16px 0px;border-top:1px solid #D9D2C5">
<p style="width:200px;font-size:26px;font-weight:700;line-height:1.3;color:#7E5F31">${w}</p>
<p style="flex:1;font-size:26px;line-height:1.35;color:#3D4450">${t}</p>
</div>`
G['g-decision'] = `${light('g-decision')}
${head('Surtitre', 'Ce que nous vous proposons de décider')}
<div style="display:flex;gap:56px;align-items:stretch">
<div style="flex:1;display:flex;flex-direction:column;gap:24px;background:#FFFDF9;border:2px solid #B08D57;border-radius:16px;padding:40px">
<h3 style="font-size:34px;font-weight:700;line-height:1.2;color:#14181F">Aujourd’hui, une seule décision</h3>
${chk('Première ligne, quinze mots au plus.')}
${chk('Deuxième ligne, quinze mots au plus.')}
${chk('Troisième ligne, quinze mots au plus.')}
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:0px">
<h3 style="font-size:34px;font-weight:700;line-height:1.2;color:#14181F;padding:0px 0px 20px 0px">Ensuite</h3>
${wk('Semaine 1', 'Une ligne, douze mots au plus.')}
${wk('Semaine 2', 'Une ligne, douze mots au plus.')}
${wk('Semaine 3', 'Une ligne, douze mots au plus.')}
${wk('Semaine 4', 'Une ligne, douze mots au plus.')}
</div>
</div>
${foot(10)}
<aside>Notes de l’orateur.</aside>
</section>`

const th = (t, w) => `<th style="width:${w}%;font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;text-align:left;color:#7E5F31;padding:14px 20px;border-bottom:2px solid #B08D57">${t}</th>`
const td = (t, b) => `<td style="font-size:26px;line-height:1.35;color:${b ? '#14181F' : '#3D4450'};${b ? 'font-weight:700;' : ''}padding:18px 20px;border-bottom:1px solid #D9D2C5">${t}</td>`
G['g-tableau'] = `${light('g-tableau')}
${head('Surtitre', 'Un tableau court : cinq lignes au plus')}
<table style="width:100%">
<tr>${th('Question', 34)}${th('Pourquoi la poser', 33)}${th('Notre réponse', 33)}</tr>
<tr>${td('Première question, dix mots au plus ?', true)}${td('Une ligne courte, douze mots au plus.')}${td('Une ligne courte, douze mots au plus.')}</tr>
<tr>${td('Deuxième question, dix mots au plus ?', true)}${td('Une ligne courte, douze mots au plus.')}${td('Une ligne courte, douze mots au plus.')}</tr>
<tr>${td('Troisième question, dix mots au plus ?', true)}${td('Une ligne courte, douze mots au plus.')}${td('Une ligne courte, douze mots au plus.')}</tr>
<tr>${td('Quatrième question, dix mots au plus ?', true)}${td('Une ligne courte, douze mots au plus.')}${td('Une ligne courte, douze mots au plus.')}</tr>
<tr>${td('Cinquième question, dix mots au plus ?', true)}${td('Une ligne courte, douze mots au plus.')}${td('Une ligne courte, douze mots au plus.')}</tr>
</table>
${foot(11)}
<aside>Notes de l’orateur.</aside>
</section>`

G['g-deux-colonnes'] = `${light('g-deux-colonnes')}
${head('Surtitre', 'Deux colonnes : un propos, une preuve')}
<div style="display:flex;gap:56px;align-items:stretch">
<div style="flex:1;display:flex;flex-direction:column;gap:20px">
<p style="font-size:32px;line-height:1.4;color:#14181F"><b>Une phrase d’accroche, quinze mots au plus.</b></p>
<ul style="font-size:28px;line-height:1.5;color:#3D4450">
<li>Un point, douze mots au plus</li>
<li>Un point, douze mots au plus</li>
<li>Un point, douze mots au plus</li>
</ul>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px;background:#14181F;border-radius:16px;padding:40px">
<h3 style="${SERIF};font-size:44px;font-weight:600;line-height:1.15;color:#B08D57">Titre de l’encadré</h3>
<p style="font-size:28px;line-height:1.45;color:#E7E1D6">Trente mots au plus : la preuve, l’exemple ou la règle qui rend le propos crédible. Pas de chiffre sans source.</p>
</div>
</div>
${foot(12)}
<aside>Notes de l’orateur.</aside>
</section>`

G['g-image'] = `${light('g-image')}
${head('Surtitre', 'Une image et un propos court')}
<div style="display:flex;gap:56px;align-items:start">
<div style="flex:1;display:flex;flex-direction:column;gap:20px">
<p style="font-size:32px;line-height:1.4;color:#14181F"><b>Une phrase d’accroche, quinze mots au plus.</b></p>
<ul style="font-size:28px;line-height:1.5;color:#3D4450">
<li>Un point, douze mots au plus</li>
<li>Un point, douze mots au plus</li>
<li>Un point, douze mots au plus</li>
</ul>
</div>
<div style="display:flex;flex-direction:column;gap:12px">
<img src="/_blob/51a8be11835fa54a99fff4c0a99ac522" alt="Description exacte de l’image" style="width:800px;height:448px;object-fit:cover;border-radius:16px">
<p style="font-size:24px;line-height:1.3;color:#5F636C">Vision générée par IA — dossier Strates, déjà remis</p>
</div>
</div>
${foot(13)}
<aside>Notes de l’orateur.</aside>
</section>`

const q = (n, t) => `<div style="flex:1;display:flex;flex-direction:column;gap:16px;border-top:2px solid #B08D57;padding:24px 0px 0px 0px">
<p style="${SERIF};font-size:56px;font-weight:600;line-height:1.0;color:#B08D57">${n}</p>
<p style="font-size:32px;line-height:1.35;color:#F3EFE8">${t}</p>
</div>`
G['g-questions'] = `${dark('g-questions', ';justify-content:space-between')}
<div style="display:flex;flex-direction:column;gap:20px">
<p style="font-size:24px;font-weight:500;letter-spacing:4px;text-transform:uppercase;color:#B08D57">À vous</p>
<h2 style="${SERIF};font-size:88px;font-weight:600;line-height:1.05;color:#F3EFE8">Titre de clôture</h2>
</div>
<div style="display:flex;gap:48px">
${q('1', 'Une question, quinze mots au plus ?')}
${q('2', 'Une question, quinze mots au plus ?')}
${q('3', 'Une question, quinze mots au plus ?')}
</div>
<p style="position:absolute;left:128px;bottom:64px;width:1664px;font-size:24px;color:#9A9286">Morgan Olsen · Mathys Couet — Marwin Tech</p>
<aside>Notes de l’orateur.</aside>
</section>`

G['g-couverture'] = `<section id="g-couverture" data-transition="fade" style="background:#14181F;color:#F3EFE8;${SANS};padding:128px;display:flex;flex-direction:column;justify-content:end;gap:28px">
<img src="/_blob/0da19f0843c584b5fda3b7136d3818a6" alt="Vision générée par IA : une grande salle de pierre, un mur peint aux couleurs du fleuve, des invités" style="position:absolute;left:0px;top:0px;width:1920px;height:1080px;object-fit:cover">
<div style="position:absolute;left:0px;top:0px;width:1920px;height:1080px;background:linear-gradient(90deg, #14181FF7 0%, #14181FE6 45%, #14181F40 100%)"></div>
<p style="font-size:24px;font-weight:500;letter-spacing:4px;text-transform:uppercase;color:#B08D57">Marwin Tech · pour GianLuca Carlone</p>
<h1 style="${SERIF};font-size:112px;font-weight:600;line-height:1.02;color:#F3EFE8;width:1100px">Titre de couverture, huit mots au plus</h1>
<p style="font-size:34px;line-height:1.4;color:#E7E1D6;width:980px">Une phrase qui dit ce qu’il va voir et ce qu’il pourra décider.</p>
<p style="font-size:24px;color:#B5AC9C">Novembre 2026 · document de présentation</p>
<p style="position:absolute;right:128px;bottom:64px;width:620px;font-size:24px;text-align:right;color:#E7E1D6">Visuel : vision générée par IA — dossier Strates</p>
<aside>Notes de l’orateur.</aside>
</section>`

const ids = Object.keys(G)
for (const id of ids) fs.writeFileSync(path.join(__dirname, 'project/slides', id + '.html'), G[id] + '\n')
fs.writeFileSync(path.join(__dirname, 'project/deck.json'), JSON.stringify({ v: 4, title: 'Gabarits v12', order: ids }, null, 1))
console.log(ids.join(','))
