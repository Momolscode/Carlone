#!/usr/bin/env python3
# Extrait le texte de la présentation (ce qui est à l'écran et les notes d'orateur), diapositive par diapositive,
# dans l'ordre de deck.json, et l'écrit dans un document interne en Markdown.
# À relancer après toute correction d'une diapositive, avant de reconstruire le dossier.
#
# Usage : python3 -I extraire-le-texte-de-la-presentation.py <dossier project> <sortie.md> "<date en toutes lettres>"
#   exemple : python3 -I outils/2026-11-11-dossier/extraire-le-texte-de-la-presentation.py \
#             pour-carlone/presentation-ia/2026-11-10-version-12-projet/project \
#             interne/rendez-vous/2026-11-11-presentation-texte-des-36-diapositives.md "11 novembre 2026"
import html
import json
import os
import re
import sys

if len(sys.argv) < 4:
    print('Usage : python3 -I extraire-le-texte-de-la-presentation.py <dossier project> <sortie.md> "<date>"')
    sys.exit(2)

P, OUT, DATE = sys.argv[1], sys.argv[2], sys.argv[3]
deck = json.load(open(os.path.join(P, 'deck.json'), encoding='utf-8'))
order = deck['order']
debut = {v['start']: v['description'] for v in deck.get('sections', {}).values()}


def texte(s):
    s = re.sub(r'<x-icon[^>]*></x-icon>', '', s)
    s = re.sub(r'<(br|/p|/h[1-6]|/li|/tr|/div)[^>]*>', '\n', s)
    s = re.sub(r'</t[dh]>', ' · ', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = html.unescape(s)
    lignes = [re.sub(r'[ \t]+', ' ', x).strip(' ·') for x in s.split('\n')]
    return [x for x in lignes if x]


annexe_des = None
for i, sid in enumerate(order, 1):
    if debut.get(sid, '').lower().startswith('annexe'):
        annexe_des = i
fil = (annexe_des - 1) if annexe_des else len(order)

out = [
    '# Présentation : texte des %d diapositives et notes d’orateur' % len(order),
    '',
    'Document interne — ne pas transmettre à GianLuca Carlone · %s' % DATE,
    '',
    'Copie de travail, pour relire et répéter sans connexion : ce qui est à l’écran, puis ce que dit l’orateur, dans l’ordre publié. '
    'Fil principal : diapositives 1 à %d. Annexe, seulement si on la demande : %d à %d. '
    'La source fait foi : `%s` ; après toute correction d’une diapositive, relancer `outils/2026-11-11-dossier/extraire-le-texte-de-la-presentation.py`.'
    % (fil, fil + 1, len(order), P.rstrip('/') + '/'),
    '',
]
for i, sid in enumerate(order, 1):
    if sid in debut:
        out += ['## ' + debut[sid], '']
    h = open(os.path.join(P, 'slides', sid + '.html'), encoding='utf-8').read()
    m = re.search(r'<aside>(.*?)</aside>', h, re.S)
    notes = ' '.join(texte(m.group(1))) if m else ''
    corps = texte(re.sub(r'<aside>.*?</aside>', '', h, flags=re.S))
    corps = [x for x in corps if not re.match(r'^Marwin Tech · pour GianLuca Carlone · novembre 2026( · \d+)?$', x)]
    out += ['### %d. `%s`' % (i, sid), '', '**À l’écran** : ' + ' / '.join(corps), '']
    out += ['**L’orateur dit** : ' + (notes or '(aucune note)'), '']
open(OUT, 'w', encoding='utf-8').write('\n'.join(out).rstrip() + '\n')
print('%d diapositives (%d dans le fil) ; écrit %s' % (len(order), fil, OUT))
