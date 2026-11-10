# Décrit un classeur .xlsx en texte : feuilles, dimensions, en-têtes, listes de choix, volets figés, mise en page,
# formules, puis tout le texte des cellules. Sert au contrôle (relecture, lint-doc.js sur le texte produit).
# Usage : python3 -I xlsx-dump.py <classeur.xlsx> [<sortie.txt>]
import sys
from openpyxl import load_workbook

if len(sys.argv) < 2:
    print('Usage : python3 -I xlsx-dump.py <classeur.xlsx> [<sortie.txt>]')
    sys.exit(2)

path = sys.argv[1]
out = open(sys.argv[2], 'w', encoding='utf-8') if len(sys.argv) > 2 else sys.stdout


def say(s=''):
    out.write(s + '\n')


wb = load_workbook(path)  # formules conservées telles qu'écrites
problems = []
say('# ' + path.split('/')[-1])
say('Feuilles : ' + ' | '.join(wb.sheetnames))
if wb.vba_archive is not None:
    problems.append('le classeur contient des macros')
try:
    links = getattr(wb, '_external_links', [])
    if links:
        problems.append('le classeur contient %d lien(s) externe(s)' % len(links))
except Exception:
    pass

for ws in wb.worksheets:
    say()
    say('## Feuille « %s »' % ws.title)
    say('Dimensions : %s ; %d ligne(s) × %d colonne(s)' % (ws.dimensions, ws.max_row, ws.max_column))
    say('Volets figés : %s' % (ws.freeze_panes or 'aucun'))
    say('Filtre automatique : %s' % (ws.auto_filter.ref or 'aucun'))
    ps = ws.page_setup
    say('Impression : orientation %s ; papier %s ; ajuster à %s page(s) de large ; zone %s ; lignes répétées %s' % (
        ps.orientation or 'par défaut', ps.paperSize or 'par défaut',
        ps.fitToWidth if ws.sheet_properties.pageSetUpPr and ws.sheet_properties.pageSetUpPr.fitToPage else 'non réglé',
        ws.print_area or 'non définie', ws.print_title_rows or 'aucune'))
    widths = {k: round(v.width, 1) for k, v in ws.column_dimensions.items() if v.width}
    say('Largeurs de colonnes : ' + (', '.join('%s=%s' % kv for kv in sorted(widths.items())) or 'par défaut'))
    dvs = ws.data_validations.dataValidation if ws.data_validations else []
    for dv in dvs:
        say('Liste de choix : %s → %s (%s)' % (dv.sqref, dv.formula1, dv.type))
    if ws.conditional_formatting:
        for rng in ws.conditional_formatting:
            say('Mise en forme conditionnelle : %s (%d règle(s))' % (rng.sqref, len(rng.rules)))
    if ws.protection and ws.protection.sheet:
        say('Feuille protégée : oui')
    merged = [str(m) for m in ws.merged_cells.ranges]
    if merged:
        say('Cellules fusionnées : ' + ', '.join(merged[:20]) + (' …' if len(merged) > 20 else ''))
    formulas = 0
    no_wrap_long = 0
    say()
    for row in ws.iter_rows():
        cells = []
        for c in row:
            v = c.value
            if v is None:
                continue
            s = str(v)
            if isinstance(v, str) and v.startswith('='):
                formulas += 1
                if '[' in v and ']' in v and '!' in v:
                    problems.append('%s!%s : formule vers un autre classeur' % (ws.title, c.coordinate))
            if isinstance(v, str) and len(v) > 60 and not (c.alignment and c.alignment.wrap_text):
                no_wrap_long += 1
            cells.append('%s: %s' % (c.coordinate, s.replace('\n', ' ⏎ ')))
        if cells:
            say(' | '.join(cells))
    say()
    say('Formules : %d ; textes longs sans retour à la ligne automatique : %d' % (formulas, no_wrap_long))
    if ws.max_row > 1 and not ws.freeze_panes and ws.title.lower() not in ('lisez-moi', 'lisez moi'):
        problems.append('feuille « %s » : pas de volets figés' % ws.title)
    if no_wrap_long:
        problems.append('feuille « %s » : %d texte(s) long(s) sans retour à la ligne automatique' % (ws.title, no_wrap_long))
    if len(ws.title) > 31:
        problems.append('feuille « %s » : nom de plus de 31 caractères' % ws.title)

if wb.sheetnames and wb.sheetnames[0].lower().replace(' ', '-') != 'lisez-moi':
    problems.append('la première feuille ne s’appelle pas « Lisez-moi »')
say()
say('## Contrôle')
for p in problems:
    say('ALERTE ' + p)
say('FEUILLES=%d ALERTES=%d' % (len(wb.sheetnames), len(problems)))
if out is not sys.stdout:
    out.close()
    print('FEUILLES=%d ALERTES=%d ; texte écrit dans %s' % (len(wb.sheetnames), len(problems), sys.argv[2]))
