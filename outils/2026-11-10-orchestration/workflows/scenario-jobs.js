export const meta = {
  name: 'carlone-scenarios-et-syntheses',
  description: 'Scénarios indépendants de la nouvelle présentation et synthèses de l’audit (lots choisis par args.jobs)',
  phases: [{ title: 'Rédaction', detail: 'un agent par lot, sans dépendance entre lots' }],
}

const ROOT = '/home/user/Carlone'
const AUD = ROOT + '/audit/2026-11-09-audit-presentation-et-offre'
const T = AUD + '/travaux'
const SCR = '/tmp/claude-0/-home-user-Carlone/5dd15790-6933-5e33-ba7c-b9089896b9b3/scratchpad'

const LIRE = `À lire d'abord, dans cet ordre :
1. ${T}/BRIEF.md — contexte, décisions déjà prises, douze règles pour tout texte montré au client, limites de ce travail. Il s'applique en entier.
2. Les notes d'audit : ${T}/a1-point-de-vue-gianluca.md, ${T}/a2-recit-et-persuasion.md, ${T}/a3-exactitude-et-engagements.md, ${T}/a4-offre-et-documents-clients.md, ${T}/a5-forme-et-lisibilite.md.
3. Les notes de recherche : ${T}/r1-nouveautes-ia-automatisation-2026.md, ${T}/r2-applications-par-metier.md, ${T}/r3-avenir-1-a-5-ans.md. Dans chacune, la partie « Vérification du 9 novembre 2026 » fait foi : une affirmation corrigée ou retirée par le vérificateur ne se reprend pas ; seule la liste « sûr pour une diapositive » peut aller dans un texte montré au client.
3 bis. ${T}/p0-diapositives-proposees-logiciels.md — trois diapositives déjà proposées sur le logiciel de gestion des propriétés et sur la mise en place des automatisations : matière à reprendre, couper ou fondre.
Si l'un de ces fichiers manque, dites-le dans votre retour et travaillez avec les autres.`

const SORTIE = `Limites : vous écrivez seulement le ou les fichiers demandés. Vous ne modifiez aucun autre fichier, vous ne faites ni commit ni push, vous ne contactez personne, vous n'achetez rien, vous ne publiez rien. Les chemins cités dans vos fichiers sont relatifs à la racine du dépôt. Français, style direct, conclusion d'abord. Le nom du client s'écrit GianLuca Carlone.`

const FORMAT = `Format de chaque diapositive (strict, une par bloc) :

### <n°> · <id> · gabarit <nom> · <nouvelle | reprise v11 <id> | reprise modifiée v11 <id>>
- **Section** : <nom de la partie>
- **Surtitre** : <trois mots au plus>
- **Titre** : <55 caractères au plus, espaces compris ; il affirme un bénéfice ou une décision>
- **Texte visible** : <le texte exact tel qu'il sera affiché, bloc par bloc ; pour une maquette, les lignes de l'écran ; pour un tableau, ses lignes>
- **Bandeau** : <la phrase du bandeau, ou « aucun »>
- **Notes de l'orateur** : <trois à six phrases, sûres pour le client>
- **Sources** : <un fichier du dépôt ou une URL datée pour chaque chiffre, date ou affirmation vérifiable>
- **Vigilance** : <ce qui reste à valider par Morgan et Mathys, ou « rien »>

L'id est court, en minuscules sans accent, avec des tirets (exemples : couverture, vos-projets, journee-avant-apres, prix-cadrage, decision). Les gabarits permis et leurs plafonds sont décrits dans ${SCR}/gabarits/GABARITS.md (§ 3, § 4 et § 6 ; les exemples sont dans ${SCR}/gabarits/project/slides/). Noms de gabarit : couverture, enonce, cartes-3, avant-apres, maquette-ecran, etapes-fleches, grand-chiffre, frise-3-horizons, decision, tableau, deux-colonnes, image, questions, ou « annexe-v11 » pour une diapositive de la version 11 reprise telle quelle en annexe.
Plafonds : titre de 55 caractères au plus ; 80 mots visibles au plus par diapositive, surtitre, titre et pied compris (120 pour une maquette d'écran ou un tableau) ; une idée par diapositive. Comptez vraiment (avec une commande si besoin).`

const CONTENU = `Ce que la présentation doit contenir (l'ordre et le dosage sont votre choix, selon votre angle) :
1. Le miroir de ses projets : ce que nous avons compris de ses lieux, de ses commerces, du cabaret-spectacle, de son administratrice — sans le montant des bâtiments, et en disant ce qui reste à confirmer avec lui.
2. Les dernières nouveautés de l'IA et de l'automatisation, montrées à travers ses propres cas, pas comme un catalogue de technologies. Seulement ce qui est « sûr pour une diapositive ».
3. Une journée de votre administratrice, avant et après (note r2).
4. Au moins deux maquettes d'écran portant « Maquette — données fictives » (par exemple : la vue d'ensemble des bâtiments et des échéances ; la file de validation de l'administratrice ; le dossier préparé pour un professionnel).
5. L'outil de gestion de ses propriétés : à lui, par étapes, et une grille neutre « les questions à poser à toute offre de logiciel » (source : pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md, section 8). Jamais le nom ni le prix d'un autre prestataire.
6. Les trois niveaux d'aide (Automatique, Assistée, Préparée), la validation humaine, et ce que l'IA ne fait pas.
7. La preuve de ce que Marwin Tech a déjà préparé pour lui, vérifiable dans le dépôt (dossiers Strates et Éclosion, laboratoire, prototype de CRM « remis en conformité avant tout usage », fiches d'automatisation, proposition de logiciel). Rien d'inventé.
8. L'avenir à un, deux et cinq ans, trié « déjà possible / probable / un pari », avec ses conditions ; la robotique « plus tard, sous conditions ».
9. La société Marwin Tech : qui, où elle en est (en cours de création, immatriculée avant toute facture et tout démarrage ; deux personnes, une étape et un essai à la fois), et ce que la relation lui apporte.
10. L'offre : le cadrage au forfait de 6 500 € HT (trois à quatre semaines, moitié à la commande), ce qu'il reçoit, et tout ce qui réduit son risque (prix fixe, arrêt possible à la fin de chaque étape, il garde ce qui est payé, comptes et données au nom de sa société).
11. La suite après le cadrage : suivez la recommandation de la note a4 sur les prix à montrer. Un prix autre que celui du cadrage ne se reprend que mot pour mot depuis les documents clients datés du 9 novembre, et se signale en « Vigilance ».
12. Une diapositive de décision : « ce que nous vous proposons de décider aujourd'hui », avec un calendrier par semaine, sans date promise que les documents ne portent pas.
13. Une clôture par trois ou quatre questions.
14. En annexe (huit diapositives au plus) : le catalogue des 47 aides, en reprenant telles quelles les diapositives v11 cat-admin, cat-batiments, cat-galerie, cat-cabaret, cat-finance, cat-marketing.
Fil principal : 14 à 20 diapositives (la note a1 plaide pour un fil court, la note a5 admet jusqu’à 22 : tranchez selon votre angle et justifiez en une ligne ; plus court vaut mieux que plus long).

Persuasion honnête seulement : la précision, la preuve montrée, le petit premier pas, la demande claire, la propriété qui lui reste, les limites dites franchement (elles donnent du crédit). Jamais d'urgence fabriquée, de référence inventée, de chiffre sans source, de promesse de résultat.`

const SC = {
  type: 'object',
  properties: {
    file: { type: 'string' },
    slide_count: { type: 'integer' },
    arc: { type: 'string', description: 'le fil du récit en cinq lignes au plus' },
    strongest_slides: { type: 'array', items: { type: 'string' } },
    risks: { type: 'array', items: { type: 'string' } },
    missing_inputs: { type: 'array', items: { type: 'string' } },
  },
  required: ['file', 'slide_count', 'arc', 'strongest_slides', 'risks'],
}
const DOC = {
  type: 'object',
  properties: {
    files: { type: 'array', items: { type: 'string' } },
    summary: { type: 'string' },
    key_points: { type: 'array', items: { type: 'string' } },
    decisions_for_partners: { type: 'array', items: { type: 'string' } },
    missing_inputs: { type: 'array', items: { type: 'string' } },
  },
  required: ['files', 'summary', 'key_points'],
}

const scenario = (n, slug, angle, consigne) => ({
  label: 'scénario ' + n + ' — ' + angle,
  schema: SC,
  prompt: `Vous êtes l'un de trois scénaristes qui travaillent chacun de leur côté, sans se lire. Mission : écrire le scénario complet d'une nouvelle présentation de Marwin Tech à GianLuca Carlone. But : qu'à la fin il ait envie de dire oui au cadrage, et qu'il lui soit facile de le dire — par la clarté, la preuve et un risque réduit, jamais par l'exagération.

${LIRE}
4. La présentation actuelle (version 11), pour savoir ce qui existe et ce qui se reprend : ${SCR}/deck-ia/project/deck.json (champ order) et ${SCR}/deck-ia/project/slides/<id>.html.
5. Pour les chiffres exacts : ${ROOT}/pour-carlone/logiciels-et-automatisations/2026-11-09-logiciel-gestion-proprietes-proposition.md, ${ROOT}/pour-carlone/logiciels-et-automatisations/2026-11-09-automatisations-fiches-detaillees.md, ${ROOT}/audit/2026-11-04-audit-strategique/pour-gianluca/2026-11-09-proposition-de-cadrage.md.

Votre angle imposé : « ${angle} ». ${consigne}

${CONTENU}

${FORMAT}

Écrivez un seul fichier : ${T}/${slug}.md. Plan du fichier : titre et date (9 novembre 2026, note de travail interne) ; « Le fil en dix lignes » ; « Pourquoi il dit oui à la fin » (cinq lignes) ; « Table des diapositives » (n°, id, gabarit, titre) ; puis un bloc par diapositive au format ci-dessus, fil principal puis annexe ; « Ce que cet angle sacrifie » (trois lignes franches).

${SORTIE}`,
})

const JOBS = {
  s1: scenario(1, 's1-son-projet-d-abord', 'son projet d’abord', 'Ouvrez sur ses lieux et ses projets. Il doit se reconnaître dans les trois premières diapositives. Chaque nouveauté est attachée à l’un de ses projets. L’offre arrive comme la suite naturelle de ce qu’il veut faire.'),
  s2: scenario(2, 's2-la-demonstration-d-abord', 'la démonstration d’abord', 'Montrez avant d’expliquer. Dès le début : une journée de son administratrice avant et après, puis des maquettes d’écran. Les explications (niveaux, règles, société) viennent après, courtes. L’offre découle de ce qu’il vient de voir.'),
  s3: scenario(3, 's3-la-decision-d-abord', 'la décision d’abord', 'Dites dès la deuxième ou la troisième diapositive ce que nous lui proposons de décider et ce que cela coûte. Le reste de la présentation répond une à une aux questions qu’il se pose (qu’est-ce que j’y gagne, qu’est-ce que je risque, pourquoi vous, pourquoi maintenant, et après ?). Finissez sur la même décision, devenue évidente.'),
  d1: {
    label: 'synthèse de l’audit et objections',
    schema: DOC,
    prompt: `Mission : écrire deux documents internes de synthèse pour Morgan Olsen et Mathys Couet, à partir des notes d'audit déjà écrites.

${LIRE}
4. Au besoin, la présentation v11 : ${SCR}/deck-ia/project/deck.json et ${SCR}/deck-ia/project/slides/<id>.html ; et les documents clients cités par les notes.

Fichier 1 : ${AUD}/01-audit-de-la-presentation.md — « Audit de la présentation v11 et de l'offre ». Plan : Conclusion en cinq lignes ; Les dix constats qui comptent, du plus grave au moins grave (chacun : le constat, la preuve avec la diapositive ou le fichier, la conséquence pour la décision de GianLuca, la correction) ; Diapositive par diapositive (tableau des 26 : garder, fusionner, réécrire, passer en annexe ou retirer, et pourquoi en une ligne) ; Ce qui est exact, ce qui est fragile, ce qui est à retirer (d'après a3) ; L'offre et les documents clients (d'après a4 : ce qui est prêt, ce qui ne l'est pas, les incohérences entre documents) ; Ce qui manque pour qu'il dise oui ; Décisions à prendre par Morgan et Mathys avant tout envoi (liste numérotée, chacune avec l'option recommandée). Les codes de l'audit du 4 novembre peuvent y figurer : c'est un document interne.

Fichier 2 : ${AUD}/03-objections-et-conditions-d-acceptation.md — « Ce que GianLuca peut objecter, et à quelles conditions il accepte ». Plan : Conclusion en cinq lignes ; Tableau des objections (au moins douze : l'objection dans ses mots, ce qu'elle cache, la réponse honnête en deux phrases, la preuve à montrer, la diapositive qui y répond, ce qu'il ne faut pas répondre) — dont : « vous n'êtes pas encore une société », « vous n'êtes que deux », « j'ai déjà une autre offre », « mon administratrice va le faire », « l'IA se trompe », « pourquoi payer un cadrage », « combien cela coûtera-t-il au total », « et si vous arrêtez », « qui est propriétaire », « mes données » ; Les conditions d'un oui (ce qu'il doit avoir vu, compris et obtenu) ; Les signaux d'un non et quoi faire ; Ce que nous ne promettons pas ; Les questions à lui poser pendant le rendez-vous ; Ce qui doit être réglé avant d'envoyer quoi que ce soit (immatriculation, assurance, décisions en attente, accord écrit des deux associés).

En tête de chaque fichier : la date (9 novembre 2026) et « document interne — ne pas transmettre à GianLuca Carlone ». Chaque affirmation renvoie à sa source (note de travail, diapositive v11, fichier du dépôt).

${SORTIE}`,
  },
  d2: {
    label: 'synthèse des nouveautés',
    schema: DOC,
    prompt: `Mission : écrire un document interne de référence sur les nouveautés de l'IA et de l'automatisation utiles aux affaires de GianLuca Carlone, à partir des trois notes de recherche déjà écrites et vérifiées.

${LIRE}
(Les notes r1, r2 et r3 sont votre matière. Les notes a1 à a5 ne servent qu'au contexte.)

Fichier : ${AUD}/02-nouveautes-ia-et-automatisation-novembre-2026.md — « Nouveautés de l'IA et de l'automatisation à novembre 2026 : ce que nous pouvons lui apporter, aujourd'hui et demain ». Plan :
1. Conclusion en six lignes : ce qui a vraiment changé en un an, ce que cela permet chez lui dès maintenant, ce qui reste un pari.
2. Les nouveautés qui comptent (tableau : la nouveauté en mots simples ; depuis quand ; source avec URL et date ; ce que cela change pour lui, sur un de ses cas ; niveau d'aide — Automatique, Assistée ou Préparée ; sûr pour une diapositive, oui ou non).
3. Par domaine (administration et son administratrice ; bâtiments et propriétés ; galerie et vente d'art ; cabaret-spectacle et événements ; finances et obligations ; communication) : trois à cinq usages chacun, avec la condition et la limite.
4. Une journée de son administratrice, avant et après (reprise de r2, vérifiée).
5. Ce qui arrive : dans un an, dans deux ans, dans cinq ans — trié « déjà possible / probable / un pari », avec la condition de chacun et la source.
6. La robotique : où l'on en est vraiment, ce qui serait possible chez lui plus tard, à quelles conditions.
7. Les règles qui encadrent (règlement européen sur l'IA, données personnelles, facturation électronique…) : seulement ce que les notes établissent, avec les dates.
8. Ce que nous n'affirmons pas, et pourquoi (les affirmations retirées ou corrigées par les vérificateurs).
9. Sources (liste complète, URL et date de consultation).

Règles : aucune affirmation qui ne soit dans les notes ; ce que le vérificateur a corrigé se reprend corrigé ; ce qu'il a retiré va seulement en section 8 ; pas de nouvelle recherche sur le web sauf pour rouvrir une URL déjà citée et en confirmer un point. En tête : la date (9 novembre 2026) et « document interne — ne pas transmettre tel quel ».

${SORTIE}`,
  },
}

const jobs = (args && args.jobs) || Object.keys(JOBS)
phase('Rédaction')
const out = await parallel(jobs.map(k => () => agent(JOBS[k].prompt, { label: JOBS[k].label, phase: 'Rédaction', schema: JOBS[k].schema }).then(r => ({ key: k, result: r }))))
return { done: out.filter(Boolean), missing: jobs.filter((k, i) => !out[i] || !out[i].result) }
