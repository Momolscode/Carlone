export const meta = {
  name: 'carlone-scenario-final',
  description: 'Écrit le scénario de la version 12, le fait critiquer par trois lecteurs indépendants, puis le corrige',
  phases: [
    { title: 'Synthèse', detail: 'un scénario unique à partir des notes d’audit et de recherche' },
    { title: 'Critique', detail: 'GianLuca sceptique, règles et exactitude, forme' },
    { title: 'Correction', detail: 'le scénario est corrigé point par point' },
  ],
}

const ROOT = '/home/user/Carlone'
const AUD = ROOT + '/audit/2026-11-09-audit-presentation-et-offre'
const T = AUD + '/travaux'
const SCR = '/tmp/claude-0/-home-user-Carlone/5dd15790-6933-5e33-ba7c-b9089896b9b3/scratchpad'
const F04 = AUD + '/04-scenario-de-la-nouvelle-presentation.md'

const COMMUN = `À lire d'abord :
1. ${T}/BRIEF.md — contexte, décisions prises, douze règles pour tout texte montré au client, limites. Il s'applique en entier.
2. ${SCR}/gabarits/GABARITS.md — les gabarits permis, les plafonds (titre de 55 caractères au plus ; 80 mots visibles au plus, 120 pour une maquette d'écran ou un tableau ; une idée par diapositive) et les trois images disponibles.
3. Les notes d'audit ${T}/a1-point-de-vue-gianluca.md, a2-recit-et-persuasion.md, a3-exactitude-et-engagements.md, a4-offre-et-documents-clients.md, a5-forme-et-lisibilite.md (même dossier) et les notes de recherche r1-nouveautes-ia-automatisation-2026.md, r2-applications-par-metier.md, r3-avenir-1-a-5-ans.md (même dossier). Dans les notes de recherche, la partie « Vérification du 9 novembre 2026 » fait foi : seul ce qui est « sûr pour une diapositive » va dans un texte montré au client. Les vérifications s'écrivent encore pendant votre travail : si une note n'a pas encore cette partie (ou si la note r3 n'existe pas encore), relisez-la juste avant d'écrire ou de contrôler les diapositives de nouveautés et d'avenir (commande : grep -c "Vérification du 9 novembre 2026" <fichier>) ; si elle manque toujours, ne retenez que des faits datés et sourcés par une URL dans la note, écrivez-les prudemment et inscrivez en « Vigilance » : « vérification en attente ».
4. Pour les chiffres exacts : ${ROOT}/pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md et ${ROOT}/audit/2026-11-04-audit-strategique/pour-gianluca/2026-11-09-proposition-de-cadrage.md.`

const LIMITES = `Limites : vous n'écrivez ou ne modifiez que le fichier indiqué. Ni commit ni push, aucun contact, aucun achat, aucune publication. Chemins relatifs à la racine du dépôt dans le fichier. Français, style direct. Le nom du client s'écrit GianLuca Carlone.`

const FORMAT = `Format strict, un bloc par diapositive :

### <n°> · <id> · gabarit <nom> · <nouvelle | reprise v11 <id> | reprise modifiée v11 <id> | annexe-v11 <id>>
- **Section** : <nom de la partie>
- **Surtitre** : <trois mots au plus>
- **Titre** : <55 caractères au plus, espaces compris>
- **Texte visible** : <le texte exact, bloc par bloc ; pour une maquette, les lignes de l'écran ; pour un tableau, ses lignes>
- **Bandeau** : <la phrase, ou « aucun »>
- **Image** : <identifiant /_blob/… et légende obligatoire, ou « aucune »>
- **Notes de l'orateur** : <trois à six phrases, sûres pour le client>
- **Sources** : <fichier du dépôt ou URL datée pour chaque chiffre, date ou affirmation vérifiable>
- **Vigilance** : <ce qui reste à valider par Morgan et Mathys, ou « rien »>`

const ISSUES = {
  type: 'object',
  properties: {
    verdict: { type: 'string', description: 'en trois phrases : dit-il oui ? pourquoi ? qu’est-ce qui l’en empêche ?' },
    issues: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          slide: { type: 'string', description: 'id de la diapositive, ou « ensemble »' },
          severity: { type: 'string', enum: ['bloquant', 'important', 'mineur'] },
          problem: { type: 'string' },
          fix: { type: 'string', description: 'la correction précise : le texte de remplacement quand c’est un texte' },
        },
        required: ['slide', 'severity', 'problem', 'fix'],
      },
    },
    keep: { type: 'array', items: { type: 'string' }, description: 'ce qui est réussi et ne doit pas être abîmé par les corrections' },
  },
  required: ['verdict', 'issues'],
}

phase('Synthèse')
const synth = await agent(`Mission : écrire le scénario de la nouvelle présentation de Marwin Tech à GianLuca Carlone (version 12). But : qu'à la fin il ait envie de dire oui au cadrage et qu'il lui soit facile de le dire — par la clarté, la preuve et un risque réduit, jamais par l'exagération.

${COMMUN}
5. Deux séquences ont déjà été proposées par deux lecteurs indépendants. Lisez-les en entier : la note a2, section 6 (21 diapositives en cinq temps, 8 en annexe) et section 7 (les deux premières et les deux dernières minutes) ; la note a1, section « Pour la refonte : l'ordre que cette lecture suggère » (onze points), avec ses dix objections (section 3), sa demande de décision (section 6), ses cinq démonstrations (section 7) et sa liste de mots creux (section 8).
6. La note a4 : ses textes proposés pour « Notre proposition » et « Ce que nous vous proposons de décider aujourd'hui », et sa recommandation sur les prix à montrer. La note a3 : ses formulations sûres et sa liste de ce qu'il ne faut jamais dire.
7. ${T}/p0-diapositives-proposees-logiciels.md (trois diapositives déjà proposées sur le logiciel et les automatisations).
8. La présentation v11, pour reprendre ce qui est bon : ${SCR}/deck-ia/project/slides/<id>.html (ordre dans ${SCR}/deck-ia/project/deck.json).

Ce que Morgan Olsen a demandé, mot pour mot : « Audit tout, retravaille le diapo. Les dernière nouveauté automatisation que l'ont peux apporter à son affaire ce qu'ont pourra apporter à l'avenir. Fais en sorte que Carlone accepte notre offre. » Les nouveautés et l'avenir ont donc leur place dans le fil principal, montrés par ses propres cas et non en cours magistral :
- Nouveautés : une diapositive « ce qui a changé en 2026 » (trois faits pris dans les listes « sûr pour une diapositive » des notes r1 et r2, chacun traduit en une tâche de ses dossiers), et les maquettes d'écran, qui montrent ces nouveautés à l'œuvre sur ses métiers (bâtiments et propriétés, galerie, cabaret et commerces, administration).
- Avenir : une frise à un, deux et cinq ans tournée vers SES projets (pour chaque horizon : ce qui deviendrait possible, son degré de certitude, sa condition ; note r3). La robotique « plus tard, sous conditions » y tient en une ligne ; une diapositive d'annexe peut la détailler avec l'image prévue.

Méthode :
1. Comparez les deux séquences proposées sur cinq critères, de 1 à 5, avec une phrase de justification : il se reconnaît dans les trois premières diapositives ; il voit du concret avant qu'on lui explique ; l'offre et son prix sont clairs et arrivent au bon moment ; chaque objection de la note a1 trouve sa réponse à l'écran ; rien n'est exagéré ni fragile (note a3).
2. Choisissez l'ossature de la meilleure, greffez les meilleures idées de l'autre. Dites ce que vous prenez à chacune et ce que vous écartez.
3. Contenu obligatoire du fil principal : ce que nous avons compris de ses projets, « à confirmer avec vous » ; au moins deux maquettes d'écran avec « Maquette — données fictives » (lignes fictives mais plausibles, sans nom, société ni adresse réels) ; la journée de votre administratrice avant et avec l'aide (aidée, jamais remplacée ni surveillée) ; les trois niveaux d'aide et la validation humaine ; sa demande de logiciel pour ses propriétés (acheter ce qui existe, relier, construire peu ; par étapes ; tout à son nom) ; la grille neutre de questions à poser à toute offre, la nôtre comprise ; ce que nous avons déjà préparé pour lui (preuves vérifiables dans le dépôt seulement) ; qui nous sommes, sans rien cacher (deux personnes ; société en cours de création, immatriculée avant toute facture et tout démarrage ; une étape et un essai à la fois) ; le prix du cadrage en grand ; ce qu'il tient en main à la fin du cadrage ; le risque retourné (prix fixe, arrêt à chaque étape, il garde ce qui est payé, comptes et données à son nom) ; la décision demandée en une phrase, avec le calendrier par semaine ; une clôture par questions qui ne met pas le poste de son administratrice en discussion devant elle et ne suppose pas le cadrage acquis.
4. Règles de composition : fil principal de 16 à 20 diapositives, puis l'annexe (huit au plus : les diapositives v11 cat-admin, cat-batiments, cat-galerie, cat-cabaret, cat-finance, cat-marketing reprises ; dites pour chacune ce qui doit y être corrigé selon les notes a1, a2 et a3, mot pour mot ; plus, si utile, une diapositive de robotique et une diapositive des étapes du logiciel avec leurs prix si la note a4 le recommande). Une idée par diapositive. Les titres, lus à la suite, racontent l'histoire. Trois ou quatre diapositives « enonce » au plus. Pas trois diapositives de suite au même gabarit. La couverture utilise l'image /_blob/0da19f0843c584b5fda3b7136d3818a6 ; la diapositive « déjà préparé pour vous » peut utiliser /_blob/51a8be11835fa54a99fff4c0a99ac522 ; la robotique /_blob/99f8d10e60b36c00c9a38334b5a95ee4. Aucune autre image.
5. Prix : suivez la note a4. Le cadrage (6 500 € HT, forfait, trois à quatre semaines, moitié à la commande) se montre. Tout autre prix ne se reprend que mot pour mot depuis les documents clients du 9 novembre et se signale en « Vigilance ».
6. Comptez les mots visibles et les caractères du titre de chaque diapositive (avec une commande) et indiquez-les à la fin de chaque bloc : « Compte : N mots, titre N caractères ».

Écrivez un seul fichier : ${F04}. Plan :
- Titre « Scénario de la nouvelle présentation (version 12) », date (9 novembre 2026), « document interne — ne pas transmettre tel quel ».
- « Le fil en dix lignes ».
- « Pourquoi il dit oui » (six lignes : ce qu'il a vu, compris, obtenu).
- « Ce que nous avons pris à chaque séquence proposée » (tableau des notes, puis les choix).
- « Table des diapositives » (n°, id, gabarit, titre, mots).
- Les blocs, fil principal puis annexe, au format ci-dessous.
- « Points à valider par Morgan et Mathys avant de montrer la présentation » (liste numérotée : chaque prix montré, chaque engagement, chaque date).
- « Ce qui a été écarté, et pourquoi ».

${FORMAT}

Les id sont courts, en minuscules, sans accent, avec des tirets ; les diapositives d'annexe gardent leur id v11.

${LIMITES}`, {
  label: 'écriture du scénario',
  phase: 'Synthèse',
  schema: {
    type: 'object',
    properties: {
      file: { type: 'string' },
      main_count: { type: 'integer' },
      annex_count: { type: 'integer' },
      backbone: { type: 'string' },
      titles: { type: 'array', items: { type: 'string' } },
      to_validate: { type: 'array', items: { type: 'string' } },
    },
    required: ['file', 'main_count', 'titles'],
  },
})

phase('Critique')
const CRITICS = [
  {
    key: 'gianluca',
    label: 'critique — GianLuca sceptique',
    prompt: `Vous jouez GianLuca Carlone, marchand d'art à Cosne-Cours-sur-Loire, qui a racheté plusieurs bâtiments, prépare plusieurs commerces dont un cabaret-spectacle, vient d'engager une administratrice, et a déjà reçu une autre offre de logiciel. Vous n'êtes pas technicien. Vous décidez vite quand c'est concret. Vous êtes bienveillant mais vous n'aimez pas qu'on vous fasse perdre du temps ni qu'on vous survende quelque chose. Deux jeunes associés, dont la société n'est pas encore immatriculée, vous présentent ceci.

Lisez seulement, dans l'ordre d'un spectateur : ${F04} (les titres, le texte visible, puis les notes de l'orateur). Puis lisez ${T}/a1-point-de-vue-gianluca.md pour vérifier que vos objections y trouvent réponse.

Dites, diapositive par diapositive, où vous décrochez, où vous doutez, où vous ne comprenez pas un mot, où l'on vous promet trop, où il manque une preuve, où l'on vous demande quelque chose de flou. Dites à quel moment vous seriez prêt à dire oui, et ce qui vous retient encore à la fin. Pour chaque problème, proposez la correction précise (le texte de remplacement). Ne proposez jamais d'ajouter une référence, un chiffre ou une promesse qui n'existe pas : proposez de couper, de préciser, de montrer une preuve existante ou de dire franchement une limite. Vous n'écrivez aucun fichier.`,
  },
  {
    key: 'regles',
    label: 'critique — règles et exactitude',
    prompt: `Vous êtes le relecteur de conformité. Vous cherchez à réfuter chaque affirmation du scénario ${F04}.

${COMMUN}

Pour chaque diapositive (texte visible ET notes de l'orateur), vérifiez :
1. Les douze règles du BRIEF (§ 5), une à une. En particulier : aucun nom ni prix d'un autre prestataire, aucune critique ; aucun des mots interdits (montant des bâtiments, codes d'audit, « JP », « journée-personne », « voie », « socle », plancher, marge, rémunération, taux journalier) ; « votre administratrice », aidée, jamais remplacée ni surveillée ; CRM « remis en conformité avant tout usage » ; « société en cours de création, immatriculée avant toute facture et tout démarrage » ; robotique « plus tard, sous conditions » ; avenir dit comme une ambition avec ses conditions ; maquettes marquées « Maquette — données fictives » ; images avec leur légende.
2. Chaque chiffre, date, prix et durée : ouvrez la source citée et comparez mot pour mot. Un prix autre que celui du cadrage doit être identique au document client du 9 novembre et figurer en « Vigilance ».
3. Chaque nouveauté technologique : elle doit figurer dans la liste « sûr pour une diapositive » d'une note r1, r2 ou r3. Sinon : à retirer ou à reformuler.
4. Chaque promesse implicite (gain de temps, économie, délai, résultat) : est-elle mesurée, conditionnée ou simplement affirmée ? « Mieux et moins cher » ne s'écrit que dans la formulation sûre de la note a3 ou a4.
5. Chaque fait sur GianLuca (bâtiments, commerces, cabaret, administratrice) : est-il présenté comme « ce que nous avons compris, à confirmer avec vous » ?
6. La cohérence interne : même prix, mêmes durées, mêmes mots d'une diapositive à l'autre et avec les documents clients.
Pour chaque écart : la diapositive, la gravité, le problème avec la preuve (fichier et passage), et le texte de remplacement. Vous n'écrivez aucun fichier.`,
  },
  {
    key: 'forme',
    label: 'critique — forme et récit',
    prompt: `Vous êtes un concepteur de présentations. Vous relisez le scénario ${F04} pour la forme et le récit, avant qu'il soit mis en page.

Lisez : ${SCR}/gabarits/GABARITS.md (plafonds, gabarits), ${T}/a5-forme-et-lisibilite.md et ${T}/a2-recit-et-persuasion.md, puis le scénario.

Vérifiez :
1. Les titres seuls, lus à la suite : racontent-ils l'histoire ? Chacun affirme-t-il un bénéfice ou une décision ? Comptez les caractères de chacun avec une commande (55 au plus).
2. Les mots visibles de chaque diapositive, comptés avec une commande (80 au plus ; 120 pour une maquette ou un tableau). Signalez chaque dépassement et proposez le texte coupé.
3. Une idée par diapositive : signalez celles qui en portent deux, et proposez la coupe ou le déplacement dans les notes.
4. Le gabarit choisi convient-il au contenu ? Y a-t-il trois diapositives de suite au même gabarit ? Plus de quatre « enonce » ? Les maquettes d'écran tiennent-elles en cinq lignes ?
5. Le rythme : où l'attention tombe-t-elle ? Le prix et la décision arrivent-ils au bon moment ? La fin est-elle nette ?
6. La langue : phrases courtes, mots simples, vouvoiement, pas d'anglais inutile, pas de formule creuse, pas de jargon. Signalez chaque mot qu'un marchand d'art non technicien ne comprendrait pas, avec son remplacement.
Pour chaque problème : la diapositive, la gravité, le problème, et le texte de remplacement exact. Vous n'écrivez aucun fichier.`,
  },
]
const critiques = await parallel(CRITICS.map(c => () => agent(c.prompt, { label: c.label, phase: 'Critique', schema: ISSUES }).then(r => ({ key: c.key, ...r }))))
const ok = critiques.filter(Boolean)
const all = ok.flatMap(c => (c.issues || []).map(i => ({ from: c.key, ...i })))
log(all.length + ' remarques, dont ' + all.filter(i => i.severity === 'bloquant').length + ' bloquantes')

phase('Correction')
const fix = await agent(`Mission : corriger le scénario ${F04} d'après trois relectures indépendantes (GianLuca sceptique, règles et exactitude, forme et récit).

${COMMUN}

Les remarques (JSON) :
${JSON.stringify(all)}

Ce qui est réussi et ne doit pas être abîmé :
${JSON.stringify(ok.flatMap(c => c.keep || []))}

Les verdicts :
${JSON.stringify(ok.map(c => ({ from: c.key, verdict: c.verdict })))}

Règles :
1. Traitez toutes les remarques « bloquant » et « important ». Traitez les « mineur » quand la correction est sûre.
2. Avant d'appliquer une correction qui touche un chiffre, un prix, une date ou une règle, vérifiez-la dans la source. Si une remarque est fausse, ne l'appliquez pas et dites pourquoi.
3. Quand deux remarques se contredisent, la règle et l'exactitude passent avant la persuasion, et la persuasion avant la forme.
4. Gardez le format strict des blocs et les plafonds (titre de 55 caractères au plus ; 80 mots visibles au plus, 120 pour une maquette ou un tableau). Recomptez avec une commande et mettez à jour la ligne « Compte ».
5. Ne rallongez pas la présentation : fil principal de 16 à 20 diapositives. Les nouveautés et l'avenir, demandés par Morgan Olsen, restent dans le fil principal.
6. Ajoutez à la fin du fichier une section « Relectures du 9 novembre 2026 » : un tableau (remarque, origine, gravité, traitée ou non, pourquoi), et « Ce qui retient encore GianLuca à la fin » avec la réponse prévue.

Vous modifiez seulement ${F04}.

${LIMITES}`, {
  label: 'correction du scénario',
  phase: 'Correction',
  schema: {
    type: 'object',
    properties: {
      file: { type: 'string' },
      applied: { type: 'integer' },
      rejected: { type: 'array', items: { type: 'string' } },
      main_count: { type: 'integer' },
      annex_count: { type: 'integer' },
      slides: { type: 'array', items: { type: 'object', properties: { n: { type: 'integer' }, id: { type: 'string' }, gabarit: { type: 'string' }, status: { type: 'string' }, title: { type: 'string' }, words: { type: 'integer' } }, required: ['id', 'gabarit', 'title'] } },
      to_validate: { type: 'array', items: { type: 'string' } },
      still_holding_back: { type: 'array', items: { type: 'string' } },
    },
    required: ['file', 'slides'],
  },
})
return { synth, critiques: ok.map(c => ({ key: c.key, verdict: c.verdict, count: (c.issues || []).length, blocking: (c.issues || []).filter(i => i.severity === 'bloquant') })), fix }
