#!/usr/bin/env python3
# Construit le dossier du rendez-vous à partir des sources du dépôt.
#
# Pour chaque document du manifeste (manifeste.json, à côté de ce script) : export en PDF A4 par md2pdf.js,
# puis reliure en un PDF par lot, avec une couverture, un sommaire paginé, des signets et un folio continu.
# Les documents marqués « imprimer » sont aussi copiés un par un dans le sous-dossier « a-imprimer ».
# Un fichier LISEZ-MOI.md décrit le contenu produit.
#
# Usage : python3 -I construire-le-dossier.py <racine du dépôt> <dossier « rendu » avec node_modules> [<dossier de sortie>]
#   exemple : python3 -I outils/2026-11-11-dossier/construire-le-dossier.py . outils/2026-11-10-orchestration/rendu
# Avant : « npm install » dans le dossier « rendu » (Playwright, marked, polices) ; python3 avec pypdf et reportlab.
# Le script ne modifie aucune source. Il s'arrête si une source manque.
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

if len(sys.argv) < 3:
    print(__doc__ or 'Usage : python3 -I construire-le-dossier.py <racine> <rendu> [<sortie>]')
    sys.exit(2)

ROOT = os.path.abspath(sys.argv[1])
RENDU = os.path.abspath(sys.argv[2])
HERE = os.path.dirname(os.path.abspath(__file__))
MAN = json.load(open(os.path.join(HERE, 'manifeste.json'), encoding='utf-8'))
OUT = os.path.abspath(sys.argv[3]) if len(sys.argv) > 3 else os.path.join(ROOT, MAN['sortie'])
TMP = tempfile.mkdtemp(prefix='dossier-')


def md2pdf(src, dst, pied, paysage=False, compact=True):
    cmd = ['node', os.path.join(RENDU, 'md2pdf.js'), src, dst, '--pied', pied]
    if compact:
        cmd.append('--compact')
    if paysage:
        cmd.append('--paysage')
    r = subprocess.run(cmd, capture_output=True, text=True, cwd=RENDU)
    m = re.search(r'PAGES=(\d+)', r.stdout)
    if r.returncode != 0 or not m:
        print(r.stdout, r.stderr)
        raise SystemExit('ÉCHEC md2pdf : ' + src)
    return int(m.group(1))


def slug(s):
    s = s.lower()
    for a, b in (('àâä', 'a'), ('éèêë', 'e'), ('îï', 'i'), ('ôö', 'o'), ('ùûü', 'u'), ('ç', 'c'), ('œ', 'oe')):
        for ch in a:
            s = s.replace(ch, b)
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', s)).strip('-')


def folio(page, texte):
    w = float(page.mediabox.width)
    h = float(page.mediabox.height)
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(w, h))
    c.setFont('Helvetica', 7)
    c.setFillColorRGB(0.37, 0.39, 0.42)
    c.drawRightString(w - 42, h - 22, texte)
    c.save()
    buf.seek(0)
    page.merge_page(PdfReader(buf).pages[0])


def sommaire_md(lot, lignes, total):
    out = ['# ' + lot['titre'], '', lot['mention'], '', lot['sous_titre'], '']
    if lot.get('avertissement'):
        out += ['> ' + lot['avertissement'], '']
    out += ['## Sommaire', '', '| N° | Document | Page |', '| --- | --- | --- |']
    for kind, a, b, c in lignes:
        if kind == 'partie':
            out.append('| | **%s** | |' % a)
        else:
            out.append('| %s | %s | %s |' % (a, b, c))
    out += ['', 'Pages : %s. Construit le %s à partir des sources du dépôt, par `outils/2026-11-11-dossier/construire-le-dossier.py`. En cas de doute, la source fait foi.' % (total, MAN['date'])]
    return '\n'.join(out)


os.makedirs(OUT, exist_ok=True)
IMPR = os.path.join(OUT, 'a-imprimer')
if os.path.isdir(IMPR):
    for f in os.listdir(IMPR):
        if f.endswith('.pdf'):
            os.remove(os.path.join(IMPR, f))
os.makedirs(IMPR, exist_ok=True)

resume = []
impr_n = 0
for li, lot in enumerate(MAN['lots'], 1):
    docs = []
    n = 0
    for partie in lot['parties']:
        for d in partie['documents']:
            src = os.path.join(ROOT, d['source'])
            if not os.path.isfile(src):
                raise SystemExit('SOURCE ABSENTE : ' + d['source'])
            n += 1
            pdf = os.path.join(TMP, 'l%d-%03d.pdf' % (li, n))
            pages = md2pdf(src, pdf, lot['pied'] + ' · ' + d['titre'], paysage=d.get('paysage', False))
            docs.append(dict(d, n=n, pdf=pdf, pages=pages, partie=partie['titre']))
            if d.get('max_pages') and pages > d['max_pages']:
                print('ALERTE %s : %d pages (limite %d)' % (d['source'], pages, d['max_pages']))
    # Sommaire : deux passes, la première pour connaître son nombre de pages.
    som_pages = 1
    for _ in range(2):
        lignes = []
        cur = som_pages + 1
        last = None
        for d in docs:
            if d['partie'] != last:
                lignes.append(('partie', d['partie'], '', ''))
                last = d['partie']
            lignes.append(('doc', str(d['n']), d['titre'], str(cur)))
            d['debut'] = cur
            cur += d['pages']
        total = cur - 1
        som_src = os.path.join(TMP, 'sommaire-%d.md' % li)
        open(som_src, 'w', encoding='utf-8').write(sommaire_md(lot, lignes, total))
        som_pdf = os.path.join(TMP, 'sommaire-%d.pdf' % li)
        som_pages = md2pdf(som_src, som_pdf, lot['pied'] + ' · sommaire', compact=False)
    # Reliure, signets, folio.
    w = PdfWriter()
    for p in PdfReader(som_pdf).pages:
        w.add_page(p)
    w.add_outline_item('Sommaire', 0)
    parents = {}
    for d in docs:
        start = len(w.pages)
        for p in PdfReader(d['pdf']).pages:
            w.add_page(p)
        if d['partie'] not in parents:
            parents[d['partie']] = w.add_outline_item(d['partie'], start)
        w.add_outline_item('%d. %s' % (d['n'], d['titre']), start, parent=parents[d['partie']])
    total = len(w.pages)
    for i, p in enumerate(w.pages, 1):
        folio(p, '%s · page %d / %d' % (lot['folio'], i, total))
        p.compress_content_streams()  # sans cela, la fusion du folio laisse chaque page non compressée
    try:
        w.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    except Exception:
        pass  # versions de pypdf sans cette fonction : le fichier est seulement un peu plus lourd
    w.add_metadata({'/Title': lot['titre'], '/Author': 'Marwin Tech (projet)', '/Subject': lot['mention']})
    dest = os.path.join(OUT, lot['fichier'])
    with open(dest, 'wb') as f:
        w.write(f)
    # Documents à imprimer, un par un.
    for d in docs:
        if d.get('imprimer'):
            impr_n += 1
            shutil.copyfile(d['pdf'], os.path.join(IMPR, '%02d-%s.pdf' % (impr_n, slug(d['titre'])[:70])))
            d['imprime_sous'] = '%02d-%s.pdf' % (impr_n, slug(d['titre'])[:70])
    resume.append((lot, docs, total, os.path.getsize(dest)))
    print('LOT %d : %s ; %d documents ; %d pages ; %.1f Mo' % (li, lot['fichier'], len(docs), total, os.path.getsize(dest) / 1e6))

# LISEZ-MOI.md du dossier produit.
L = ['# ' + MAN['titre'], '', MAN['mention'], '']
L += MAN['introduction'] + ['']
for lot, docs, total, size in resume:
    L += ['## `%s` — %s' % (lot['fichier'], lot['titre']), '', '%s %d pages.' % (lot['sous_titre'], total), '']
    if lot.get('avertissement'):
        L += [lot['avertissement'], '']
    L += ['| N° | Document | Page | Pages | Source | À imprimer |', '| --- | --- | --- | --- | --- | --- |']
    last = None
    for d in docs:
        if d['partie'] != last:
            L.append('| | **%s** | | | | |' % d['partie'])
            last = d['partie']
        L.append('| %d | %s | %d | %d | `%s` | %s |' % (d['n'], d['titre'], d['debut'], d['pages'], d['source'], ('`a-imprimer/%s`' % d['imprime_sous']) if d.get('imprime_sous') else ''))
    L.append('')
L += MAN['fin']
open(os.path.join(OUT, 'LISEZ-MOI.md'), 'w', encoding='utf-8').write('\n'.join(L) + '\n')
shutil.rmtree(TMP, ignore_errors=True)
print('ÉCRIT : ' + OUT)
