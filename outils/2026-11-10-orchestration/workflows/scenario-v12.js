export const meta = {
  name: 'carlone-scenario-v12',
  description: 'Scénario de la présentation version 12 (vingt minutes) : ossature, blocs écrits par parties, assemblage, trois critiques indépendantes, correction',
  phases: [
    { title: 'Ossature', detail: 'le fil, la table des diapositives, le minutage' },
    { title: 'Blocs', detail: 'texte exact de chaque diapositive, par parties' },
    { title: 'Assemblage', detail: 'un seul fichier, comptes, points à valider' },
    { title: 'Critique', detail: 'GianLuca sceptique, règles et exactitude, forme et récit' },
    { title: 'Correction', detail: 'application des constats' },
  ],
}

const ROOT = '/home/user/Carlone'
const AUD = ROOT + '/audit/2026-11-09-audit-presentation-et-offre'
const T = AUD + '/travaux'
const P = ROOT + '/audit/2026-11-10-preparation-des-livrables/travaux'
const SCR = '/tmp/claude-0/-home-user-Carlone/5dd15790-6933-5e33-ba7c-b9089896b9b3/scratchpad'
const F04 = AUD + '/04-scenario-de-la-nouvelle-presentation.md'
const PARTS = SCR + '/scenario-v12'

const CONTEXTE = `CONTEXTE
Nous sommes le mardi 10 novembre 2026. Marwin Tech : Morgan Olsen et Mathys Couet, société en cours de création. Client : GianLuca Carlone, marchand d'art (écrivez toujours « GianLuca Carlone »). Faits rapportés par Morgan, non vérifiés auprès du client : une administratrice vient d'être engagée pour coordonner ses projets ; plusieurs bâtiments rachetés ; plusieurs commerces prévus dont un cabaret-spectacle à côté de la galerie ; une autre proposition de « gestion de propriété » reçue (jamais nommée, jamais chiffrée, jamais critiquée dans un texte client) ; il a demandé à Marwin Tech si elle pouvait lui créer un logiciel de gestion de ses propriétés.
Offre : un cadrage au forfait de 6 500 € hors taxes (7 800 € toutes taxes comprises), trois à quatre semaines, moitié à la commande, moitié à la remise du dossier ; puis un essai de huit semaines ; puis un suivi.
Demandes de Morgan : « Audit tout, retravaille le diapo. Les dernières nouveautés automatisation que l'on peut apporter à son affaire, ce qu'on pourra apporter à l'avenir. Fais en sorte que Carlone accepte notre offre. » Puis, le 10 novembre : une présentation de vingt minutes, claire, convaincante, crédible ; des écrans d'exemple en données fictives (fiche bâtiment, échéances, comparaison de trois devis) ; une page « Ce que des moyens supplémentaires nous permettraient d'accomplir », intégrée naturellement (voir le § 9.2 de ${P}/BRIEF-2.md).

RÈGLES : le § 5 de ${T}/BRIEF.md (douze règles et l'additif) et les § 5 et § 9 de ${P}/BRIEF-2.md s'appliquent à tout texte montré au client, notes de l'orateur comprises (elles sont visibles par quiconque ouvre la présentation).

LIMITES : vous n'écrivez que le ou les fichiers indiqués. Ni commit ni push, aucun contact, aucun achat, aucune publication. Français, style direct, phrases courtes.

MÉTHODE (obligatoire) : lisez par tranches de 300 lignes, cherchez d'abord avec Grep ; ne lisez jamais un fichier entier de plus de 400 lignes ; écrivez tôt, par morceaux (Write pour le début, puis cat >> "fichier" <<'EOF' … EOF, 600 mots au plus par appel).`

const SOURCES = `SOURCES À UTILISER (lisez seulement les parties indiquées)
- ${T}/a2-recit-et-persuasion.md : sections 6 et 7 (la séquence de 21 diapositives en cinq temps, les deux premières et les deux dernières minutes).
- ${T}/a1-point-de-vue-gianluca.md : « Pour la refonte : l'ordre que cette lecture suggère », sections 3, 6, 7, 8.
- ${T}/a4-offre-et-documents-clients.md : sections 7 (prix à montrer, forme exacte) et 9 (textes des diapositives « Notre proposition » et « Ce que nous vous proposons de décider aujourd'hui »).
- ${T}/a3-exactitude-et-engagements.md : formulations sûres et « ne jamais dire » (cherchez « sûr », « jamais »).
- ${AUD}/01-audit-de-la-presentation.md : conclusion et refonte recommandée (cherchez « Conclusion », « refonte », « 18 à 21 »).
- ${AUD}/03-objections-et-conditions-d-acceptation.md : conditions d'un oui, signaux d'un non, ce que nous ne promettons pas (cherchez « conditions », « signaux »).
- ${P}/k5-rendez-vous-de-decision.md : « En bref », « Ce que cela change pour nos livrables » et la partie « Vérification du 10 novembre 2026 » si elle existe.
- ${P}/i2-texte-d-orateur-et-objections.md et ${P}/i4-ecrans-d-exemple-du-logiciel.md : leur § 5 (plan proposé) et § 3 (contradictions).
- Nouveautés et avenir : ${AUD}/02-nouveautes-ia-et-automatisation-novembre-2026.md s'il existe ; sinon les parties « Vérification » (listes « sûr pour une diapositive ») de ${T}/r1-nouveautes-ia-automatisation-2026.md, ${T}/r2-applications-par-metier.md et ${T}/r3-avenir-1-a-5-ans.md. Seul ce qui est « sûr pour une diapositive » va dans un texte client.
- Moyens supplémentaires : ${P}/s-LM-moyens-supplementaires-cahier-des-charges.md s'il existe (il donne le texte exact de la diapositive) ; sinon les parties « Vérification du 10 novembre 2026 » des notes ${P}/k13a-… à k13f-… si elles existent ; sinon la diapositive est marquée « texte provisoire, à remplacer par le cahier des charges LM ».
- Gabarits et plafonds : ${SCR}/gabarits/GABARITS.md (titre de 55 caractères au plus ; 80 mots visibles au plus, 120 pour une maquette d'écran ou un tableau ; une idée par diapositive ; trois images seulement).
- Chiffres exacts : ${ROOT}/audit/2026-11-04-audit-strategique/pour-gianluca/2026-11-09-proposition-de-cadrage.md (lignes 15 à 182 seulement) et ${ROOT}/pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md.
- La version 11, pour reprendre ce qui est bon : ${SCR}/deck-ia/project/slides/<id>.html (ordre dans ${SCR}/deck-ia/project/deck.json).`

const FORMAT = `Format strict, un bloc par diapositive :

### <n°> · <id> · gabarit <nom> · <nouvelle | reprise v11 <id> | reprise modifiée v11 <id> | annexe-v11 <id>> · <minutes> min
- **Section** : <nom de la partie>
- **Surtitre** : <trois mots au plus>
- **Titre** : <55 caractères au plus, espaces compris ; le titre affirme une idée>
- **Texte visible** : <le texte exact, bloc par bloc ; pour une maquette d'écran, les lignes de l'écran, données manifestement fictives ; pour un tableau, ses lignes>
- **Bandeau** : <la phrase, ou « aucun »>
- **Image** : <identifiant /_blob/… et légende obligatoire, ou « aucune »>
- **Message essentiel** : <une phrase : ce qu'il doit retenir>
- **Notes de l'orateur** : <trois à six phrases, sûres pour le client>
- **Transition** : <la phrase qui mène à la diapositive suivante>
- **Sources** : <fichier du dépôt ou page datée pour chaque chiffre, date ou affirmation vérifiable>
- **Vigilance** : <ce qui reste à valider par Morgan et Mathys, ou « rien »>
- **Compte** : <N mots visibles, titre N caractères — comptés avec une commande>`

const COMPOSITION = `RÈGLES DE COMPOSITION
- Fil principal de 16 à 20 diapositives pour VINGT MINUTES de présentation (la somme des minutes du fil principal vaut 20), précédées d'un temps de questions et suivies de l'échange ; annexe de huit diapositives au plus, montrée seulement si on la demande.
- Une idée par diapositive ; les titres lus à la suite racontent l'histoire ; trois ou quatre diapositives « enonce » au plus ; pas trois diapositives de suite au même gabarit.
- Contenu obligatoire du fil principal : ce que nous avons compris de ses projets, « à confirmer avec vous » ; sa demande de logiciel (« Vous nous avez demandé si nous pouvions créer votre logiciel de gestion de vos propriétés. ») ; au moins deux écrans d'exemple parmi fiche bâtiment, échéances, comparaison de trois devis, chacun avec « Maquette — données fictives » (données manifestement inventées : « Bâtiment A », « Entreprise 1 » ; jamais un lieu réel ; l'écran montre l'allure et le principe, pas le modèle de données détaillé de la première étape déjà chiffrée) ; ce qui a changé en 2026, traduit en tâches de ses dossiers ; la journée de votre administratrice, aidée, jamais remplacée ni surveillée ; les trois niveaux d'aide et la validation humaine ; la grille neutre de questions à poser à toute offre, la nôtre comprise ; qui nous sommes, sans rien cacher ; le prix du cadrage en grand, sous la forme exacte de la note a4 § 7 ; ce qu'il tient en main à la fin du cadrage ; le risque retourné (prix fixe, arrêt possible, il garde ce qui est payé, comptes et données à son nom) ; la décision demandée en une phrase, avec le calendrier ; l'avenir à un, deux et cinq ans tourné vers ses projets (tendance sous conditions, jamais une promesse) ; UNE diapositive « Ce que des moyens supplémentaires nous permettraient d'accomplir », placée après la diapositive du prix et de la décision, qui ouvre une perspective sans rien conditionner ; une clôture par une question ouverte qui ne suppose pas le cadrage acquis.
- Annexe : les diapositives v11 cat-admin, cat-batiments, cat-galerie, cat-cabaret, cat-finance (dites mot pour mot ce qui doit y être corrigé selon a1, a2, a3) ; au plus deux diapositives d'annexe sur les moyens supplémentaires ; une diapositive de robotique (« plus tard, sous conditions ») si utile.
- Images : couverture /_blob/0da19f0843c584b5fda3b7136d3818a6 ; « déjà préparé pour vous » /_blob/51a8be11835fa54a99fff4c0a99ac522 ; robotique /_blob/99f8d10e60b36c00c9a38334b5a95ee4. Aucune autre. Une image générée n'est jamais présentée comme la photo d'un lieu réel.
- Prix : le cadrage se montre. Tout autre prix seulement mot pour mot depuis les documents clients du 9 novembre, signalé en « Vigilance ». Jamais le nom ni le prix de l'autre proposition.
- Les id sont courts, en minuscules, sans accent, avec des tirets ; les diapositives d'annexe reprises gardent leur id v11.`

const OUTLINE = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    fil: { type: 'string', description: 'le fil en dix lignes' },
    slides: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          n: { type: 'number' },
          id: { type: 'string' },
          gabarit: { type: 'string' },
          section: { type: 'string' },
          minutes: { type: 'number' },
          annexe: { type: 'boolean' },
          origine: { type: 'string', description: 'nouvelle, reprise v11 <id>, reprise modifiée v11 <id>, annexe-v11 <id>' },
          titre: { type: 'string' },
          intention: { type: 'string', description: 'ce que la diapositive doit faire et contenir, en deux ou trois phrases' },
          sources: { type: 'string' },
        },
        required: ['n', 'id', 'gabarit', 'section', 'titre', 'intention'],
      },
    },
  },
  required: ['file', 'slides'],
}
const ISSUES = {
  type: 'object',
  properties: {
    verdict: { type: 'string', description: 'en trois phrases : dit-il oui ? pourquoi ? qu’est-ce qui l’en empêche ?' },
    issues: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          slide: { type: 'string' },
          severity: { type: 'string', enum: ['bloquant', 'important', 'mineur'] },
          problem: { type: 'string' },
          fix: { type: 'string', description: 'la correction précise : le texte de remplacement quand c’est un texte' },
        },
        required: ['slide', 'severity', 'problem', 'fix'],
      },
    },
    keep: { type: 'array', items: { type: 'string' } },
  },
  required: ['verdict', 'issues'],
}

// ───────────── 1. Ossature ─────────────
phase('Ossature')
const outline = await agent(`${CONTEXTE}

MISSION : concevoir l'ossature de la présentation version 12 à GianLuca Carlone. But : qu'à la fin il ait envie de dire oui au cadrage et qu'il lui soit facile de le dire — par la clarté, la preuve et un risque réduit, jamais par l'exagération.

${SOURCES}

${COMPOSITION}

CE QUE VOUS ÉCRIVEZ : le début du fichier ${F04} (créez-le avec Write ; s'il existe déjà, remplacez-le) :
- Titre « Scénario de la nouvelle présentation (version 12) », puis « Document interne — ne pas transmettre tel quel — 10 novembre 2026 ».
- « Le fil en dix lignes ».
- « Pourquoi il dit oui » (six lignes : ce qu'il a vu, compris, obtenu).
- « Ce que nous avons pris aux séquences proposées » (a1, a2, 01 : ce qui est pris, ce qui est écarté, en dix lignes au plus).
- « Minutage » : avant la présentation (questions, cinq minutes environ), les vingt minutes diapositive par diapositive, puis l'échange.
- « Table des diapositives » (n°, id, gabarit, minutes, titre, intention en une phrase), fil principal puis annexe.
Ne rédigez pas les blocs détaillés : d'autres le feront à partir de votre table. Chaque intention doit être assez précise pour qu'un rédacteur écrive la diapositive sans vous (contenu, preuve, chiffre, image).
Lisez seulement ce qui est utile ; commencez à écrire après huit lectures au plus.

RÉPONSE : la sortie structurée (file, fil, slides : toutes les diapositives, fil principal puis annexe, avec n, id, gabarit, section, minutes, annexe vrai ou faux, origine, titre, intention, sources).`, { label: 'ossature', phase: 'Ossature', schema: OUTLINE })

if (!outline || !outline.slides || !outline.slides.length) {
  log('Ossature absente : arrêt')
  return { outline: null }
}
const all = outline.slides.slice().sort((a, b) => a.n - b.n)
const mainMin = all.filter(s => !s.annexe).reduce((t, s) => t + (s.minutes || 0), 0)
log(`Ossature : ${all.filter(s => !s.annexe).length} diapositives dans le fil (${mainMin} min), ${all.filter(s => s.annexe).length} en annexe`)

// ───────────── 2. Blocs, par parties ─────────────
const size = 5
const chunks = []
for (let i = 0; i < all.length; i += size) chunks.push(all.slice(i, i + size))
const table = all.map(s => `${s.n} · ${s.id} · ${s.gabarit} · ${s.annexe ? 'annexe' : (s.minutes || '?') + ' min'} · ${s.titre} — ${s.intention}`).join('\n')

const parts = await parallel(chunks.map((c, k) => () => agent(`${CONTEXTE}

MISSION : rédiger, au format strict ci-dessous, les blocs détaillés de ${c.length} diapositives de la présentation version 12 (partie ${k + 1} sur ${chunks.length}).

LA TABLE COMPLÈTE (pour la cohérence et les transitions) :
${table}

VOS DIAPOSITIVES :
${c.map(s => `- ${s.n} · ${s.id} · gabarit ${s.gabarit} · ${s.origine || 'nouvelle'} · ${s.annexe ? 'annexe' : (s.minutes || '?') + ' min'} — ${s.titre}\n  Intention : ${s.intention}\n  Sources indiquées : ${s.sources || '—'}`).join('\n')}

${SOURCES}

${COMPOSITION}

${FORMAT}

Pour une diapositive reprise de la version 11, lisez son fichier HTML et reprenez ce qui est bon, corrigé selon les notes a1, a2, a3. Pour un écran d'exemple, écrivez les lignes exactes de l'écran (cinq à huit lignes de données manifestement fictives, cohérentes entre les écrans : mêmes « Bâtiment A », « Bâtiment B », mêmes montants ronds). Comptez avec une commande les mots visibles et les caractères du titre.

FICHIER À ÉCRIRE : ${PARTS}/partie-${String(k + 1).padStart(2, '0')}.md (créez le dossier avec mkdir -p ; Write pour le premier bloc, puis cat >> pour les suivants ; seulement les blocs, sans titre de document).

RÉPONSE : le chemin du fichier et, pour chaque diapositive, une ligne « id : N mots, titre N caractères, vigilance ».`, { label: `blocs:partie-${k + 1}`, phase: 'Blocs' })))
const missingParts = parts.map((p, k) => (p ? null : k + 1)).filter(Boolean)
if (missingParts.length) log('Parties sans réponse : ' + missingParts.join(', '))

// ───────────── 3. Assemblage ─────────────
phase('Assemblage')
const asm = await agent(`${CONTEXTE}

MISSION : assembler le scénario. Le début du fichier ${F04} existe (titre, fil, minutage, table). Les blocs détaillés sont dans ${PARTS}/partie-01.md à partie-${String(chunks.length).padStart(2, '0')}.md.

1. Vérifiez que chaque partie existe. S'il manque une partie (${missingParts.length ? 'parties signalées absentes : ' + missingParts.join(', ') : 'aucune signalée'}), rédigez vous-même les blocs manquants au format ci-dessous, d'après la table du fichier.
2. Ajoutez au fichier ${F04}, dans l'ordre, une ligne « ## Les diapositives — fil principal », les blocs du fil principal, puis « ## Annexe », les blocs d'annexe (commande : cat partie-…md >> fichier, en respectant l'ordre des numéros ; déplacez les blocs si l'ordre n'est pas bon).
3. Contrôlez : chaque id de la table a un bloc et un seul ; la somme des minutes du fil principal vaut 20 (corrigez la table et les blocs sinon) ; aucun titre ne dépasse 55 caractères ; aucun bloc ne dépasse 80 mots visibles (120 pour un écran d'exemple ou un tableau) ; les transitions s'enchaînent ; les montants et les dates sont identiques partout.
4. Ajoutez à la fin : « ## Points à valider par Morgan et Mathys avant de montrer la présentation » (liste numérotée : chaque prix montré, chaque engagement, chaque date, la diapositive des moyens supplémentaires, les écrans d'exemple) et « ## Ce qui a été écarté, et pourquoi ».
5. Lancez le contrôle mécanique sur le fichier : cd ${SCR}/render && node lint-doc.js --interne "${F04}" ; puis, pour vérifier les textes destinés au client, extrayez les lignes « Titre », « Texte visible », « Bandeau », « Message essentiel », « Notes de l'orateur » et « Transition » dans ${PARTS}/texte-client.md (avec grep), ajoutez en tête la ligne « PROJET non envoyé — à valider par Morgan Olsen et Mathys Couet », et lancez : node lint-doc.js --tarifs-publics "${PARTS}/texte-client.md". Corrigez dans ${F04} chaque erreur fondée.

${FORMAT}

RÉPONSE : le nombre de diapositives (fil, annexe), la somme des minutes, les corrections faites, la dernière ligne de chaque contrôle mécanique.`, { label: 'assemblage', phase: 'Assemblage' })

// ───────────── 4. Critique ─────────────
const CRITICS = [
  {
    key: 'gianluca', label: 'critique — GianLuca sceptique',
    prompt: `Vous êtes GianLuca Carlone : marchand d'art, chef d'entreprise, plusieurs projets en même temps, pas informaticien, peu de temps, méfiant envers les promesses ; vous avez reçu une autre proposition ; vous avez demandé à ces deux jeunes gens s'ils pouvaient vous créer un logiciel de gestion de vos propriétés. Lisez le scénario ${F04} en entier, par tranches, comme si vous assistiez aux vingt minutes. Diapositive par diapositive : est-ce que je comprends ? est-ce que cela me concerne ? est-ce que j'y crois ? qu'est-ce qui me fait douter ? À la fin : est-ce que je dis oui au cadrage ? Qu'est-ce qui m'en empêche ? La diapositive des moyens supplémentaires me donne-t-elle confiance (ambition) ou méfiance (on me demande de l'argent) ? Donnez des corrections précises, avec le texte de remplacement.`,
  },
  {
    key: 'regles', label: 'critique — règles et exactitude',
    prompt: `Vous êtes le gardien des règles et de l'exactitude. Lisez le scénario ${F04} en entier, par tranches. Vérifiez chaque bloc contre : le § 5 de ${T}/BRIEF.md (douze règles et additif), les § 5 et § 9 de ${P}/BRIEF-2.md, la note ${T}/a3-exactitude-et-engagements.md (formulations sûres, « ne jamais dire »), la note ${T}/a4-offre-et-documents-clients.md § 7 (forme exacte du prix). Pour chaque chiffre, date, nouveauté ou affirmation : est-il sourcé, « sûr pour une diapositive », identique aux documents clients du 9 novembre ? Les écrans d'exemple portent-ils « Maquette — données fictives » et des données manifestement inventées ? Livrent-ils par avance le contenu de la première étape chiffrée ? La diapositive des moyens supplémentaires respecte-t-elle les onze règles du § 9.2 (multiplicateur avec indicateur et base, séparation avec l'offre, aucun montant demandé, prix publics sourcés) ? Relancez : cd ${SCR}/render && node lint-doc.js --tarifs-publics "${PARTS}/texte-client.md" (s'il existe). Donnez des corrections précises.`,
  },
  {
    key: 'forme', label: 'critique — forme et récit',
    prompt: `Vous êtes un concepteur de présentations exigeant. Lisez le scénario ${F04} en entier, par tranches, et ${SCR}/gabarits/GABARITS.md. Vérifiez : les titres lus à la suite racontent-ils l'histoire ? une idée par diapositive ? le rythme (pas trois gabarits identiques de suite, trois ou quatre « enonce » au plus) ? les plafonds (titre de 55 caractères, 80 mots visibles, 120 pour un écran ou un tableau) ? le minutage (vingt minutes au total, temps réaliste par diapositive) ? les transitions ? l'ouverture (il se reconnaît dans les trois premières diapositives) et la clôture (une décision claire, puis une question ouverte) ? la place de la diapositive des moyens supplémentaires (après le prix et la décision, sans diluer la demande) ? Donnez des corrections précises.`,
  },
]
phase('Critique')
const critiques = (await parallel(CRITICS.map(c => () => agent(`${CONTEXTE}\n\n${c.prompt}\n\nVous ne modifiez aucun fichier.`, { label: c.label, phase: 'Critique', schema: ISSUES }).then(r => r && ({ key: c.key, ...r }))))).filter(Boolean)
const issues = critiques.flatMap(c => (c.issues || []).map(i => ({ from: c.key, ...i })))
log(`Critiques : ${critiques.length}/3 ; constats : ${issues.length} (bloquants : ${issues.filter(i => i.severity === 'bloquant').length})`)

// ───────────── 5. Correction ─────────────
phase('Correction')
const fix = await agent(`${CONTEXTE}

MISSION : corriger le scénario ${F04} d'après trois relectures indépendantes.

VERDICTS :
${critiques.map(c => `- ${c.key} : ${c.verdict}`).join('\n')}

CONSTATS :
${JSON.stringify(issues, null, 1)}

À PRÉSERVER :
${critiques.flatMap(c => c.keep || []).map(k => '- ' + k).join('\n')}

Appliquez tous les constats bloquants et importants, et les mineurs utiles. Quand deux constats se contredisent : les briefs l'emportent, puis l'intérêt de GianLuca Carlone, puis la forme. Modifiez par petites retouches (outil Edit). Mettez à jour la table, le minutage et les comptes si un bloc change. Relancez le contrôle mécanique (cd ${SCR}/render && node lint-doc.js --interne "${F04}") et, après avoir régénéré ${PARTS}/texte-client.md comme à l'assemblage, node lint-doc.js --tarifs-publics "${PARTS}/texte-client.md". Ajoutez à la fin du fichier « ## Corrections du 10 novembre 2026 » : la liste des constats appliqués et de ceux écartés, avec la raison.

RÉPONSE : constats appliqués, constats écartés et pourquoi, la dernière ligne de chaque contrôle, le nombre de diapositives (fil, annexe) et la somme des minutes.`, { label: 'correction du scénario', phase: 'Correction' })

return {
  fil: outline.fil,
  slides: all.map(s => ({ n: s.n, id: s.id, gabarit: s.gabarit, annexe: !!s.annexe, minutes: s.minutes || null, titre: s.titre })),
  minutes: mainMin,
  asm,
  critiques: critiques.map(c => ({ key: c.key, verdict: c.verdict, n: (c.issues || []).length, bloquants: (c.issues || []).filter(i => i.severity === 'bloquant').map(i => `${i.slide}: ${i.problem}`) })),
  fix,
}
