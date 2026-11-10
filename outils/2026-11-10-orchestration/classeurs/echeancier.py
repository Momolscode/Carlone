import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter
OUT = '/home/user/Carlone/pour-carlone/cabaret-et-commerces/2026-11-10-echeancier.xlsx'
os.makedirs(os.path.dirname(OUT), exist_ok=True)
F = Font(name='Arial', size=10); HF = Font(name='Arial', size=10, bold=True, color='FFFFFF')
HFILL = PatternFill('solid', fgColor='14181F'); thin = Side(style='thin', color='D9D2C5'); B = Border(left=thin, right=thin, top=thin, bottom=thin)
WR = Alignment(wrap_text=True, vertical='top')
wb = Workbook(); ws = wb.active; ws.title = 'Lisez-moi'
for i, (t, f) in enumerate([
  ('Échéancier — cabaret et commerces', Font(name='Arial', size=14, bold=True)),
  ('PROJET non envoyé — à valider par Morgan Olsen et Mathys Couet · 10 novembre 2026', Font(name='Arial', size=10, bold=True, color='7E5F31')),
  ('', F),
  ('À quoi il sert : suivre, lieu par lieu, les démarches, autorisations et échéances listées dans le document « Cabaret et commerces : autorisations, démarches et échéances ».', F),
  ('Ce n’est pas un avis juridique : chaque ligne est à faire valider par vos professionnels (avocat, notaire, expert-comptable, architecte, assureur) avant toute démarche.', F),
  ('Statuts : « documenté » (texte ou page officielle cités, à revérifier à la date de la démarche) ; « à vérifier » ; « à faire valider ».', F),
  ('Responsable : un rôle (exploitant, propriétaire, architecte, administratrice…), jamais un nom ni une coordonnée.', F),
  ('La colonne « Jours restants » se calcule seule à partir de la date prévue. Les lieux « Lieu 1 » sont des exemples fictifs à remplacer.', F)], 1):
    c = ws.cell(row=i, column=1, value=t); c.font = f; c.alignment = WR
ws.column_dimensions['A'].width = 120
cols = ['N°', 'Lieu', 'Famille', 'Démarche ou échéance', 'Auprès de', 'Délai ou rythme indiqué', 'Quand', 'Responsable (rôle)', 'Pièce qui le prouve', 'Statut', 'À faire valider par', 'Date prévue', 'Jours restants', 'Fait le']
rows = [
 ('Cabaret (Lieu 1, exemple fictif)', 'Organisation', 'Fixer la société qui exploite, le lieu, la jauge, repas ou non', 'vous', '—', 'avant tout', 'dirigeant', 'décision écrite', 'à faire valider', 'avocat, expert-comptable'),
 ('Cabaret (Lieu 1, exemple fictif)', 'Travaux', 'Plans, étude acoustique, premier échange sécurité', 'architecte, acousticien, mairie', 'inconnu', 'avant les travaux', 'exploitant', 'plans, étude', 'à faire valider', 'architecte'),
 ('Cabaret (Lieu 1, exemple fictif)', 'Lieu recevant du public', 'Autorisation de travaux (ou permis qui en tient lieu)', 'mairie', '4 mois, 5 avec permis', 'avant les travaux', 'exploitant', 'arrêté', 'documenté', 'architecte'),
 ('Cabaret (Lieu 1, exemple fictif)', 'Urbanisme', 'Accord de l’architecte des Bâtiments de France si site patrimonial remarquable', 'mairie', 'délai allongé', 'avant les travaux', 'propriétaire', 'avis', 'à vérifier', 'architecte'),
 ('Cabaret (Lieu 1, exemple fictif)', 'Boissons', 'Licence (achat ou transfert, accord du préfet) ; permis d’exploitation 20 h', 'vendeur, préfecture, organisme de formation', 'inconnu', 'avant l’ouverture', 'exploitant', 'licence, attestation', 'documenté', 'avocat'),
 ('Cabaret (Lieu 1, exemple fictif)', 'Spectacle', 'Déclaration d’entrepreneur de spectacles (en ligne)', 'DRAC', '30 jours après dossier complet ; 5 ans', 'avant la première représentation', 'exploitant', 'récépissé', 'documenté', ''),
 ('Cabaret (Lieu 1, exemple fictif)', 'Bruit', 'Étude de l’impact des nuisances sonores', 'acousticien', 'avant le démarrage', 'avant l’ouverture', 'exploitant', 'étude', 'documenté', ''),
 ('Cabaret (Lieu 1, exemple fictif)', 'Restauration', 'Déclaration de la cuisine ; formation hygiène 14 h', 'protection des populations', 'avant l’ouverture', 'avant l’ouverture', 'exploitant', 'récépissé, attestation', 'documenté', ''),
 ('Cabaret (Lieu 1, exemple fictif)', 'Boissons', 'Déclaration du débit de boissons', 'mairie', '15 jours avant', 'avant l’ouverture', 'exploitant', 'récépissé', 'documenté', ''),
 ('Cabaret (Lieu 1, exemple fictif)', 'Horaires', 'Dérogation de fermeture tardive', 'préfet ou sous-préfet', 'un mois avant ; un an au plus', 'chaque année', 'exploitant', 'arrêté', 'à vérifier', 'avocat'),
 ('Cabaret (Lieu 1, exemple fictif)', 'Sécurité', 'Visite de la commission, puis arrêté d’ouverture', 'commission, maire', 'avant toute ouverture', 'avant l’ouverture', 'exploitant', 'procès-verbal, arrêté', 'documenté', ''),
 ('Cabaret (Lieu 1, exemple fictif)', 'Taxe', 'Déclaration de la taxe sur les spectacles (3,5 %)', 'Centre national de la musique', 'avant la fin du 3e mois', 'après chaque représentation', 'exploitant', 'déclaration', 'documenté', 'expert-comptable'),
 ('Cabaret (Lieu 1, exemple fictif)', 'Bruit', 'Vérification des équipements de mesure du son', 'professionnel indépendant', 'tous les deux ans', 'récurrent', 'exploitant', 'rapport', 'documenté', ''),
 ('Cabaret (Lieu 1, exemple fictif)', 'Sécurité', 'Visite périodique de la commission', 'commission de sécurité', 'tous les 3 ou 5 ans', 'récurrent', 'exploitant', 'procès-verbal', 'documenté', ''),
 ('Commerce (Lieu 2, exemple fictif)', 'Urbanisme', 'Déclaration préalable ou permis si usage ou façade change', 'mairie', 'selon le cas', 'avant les travaux', 'propriétaire', 'arrêté', 'à faire valider', 'architecte'),
 ('Commerce (Lieu 2, exemple fictif)', 'Lieu recevant du public', 'Autorisation de travaux, même intérieurs ; accessibilité', 'mairie', 'selon le cas', 'avant les travaux', 'exploitant', 'arrêté', 'documenté', 'architecte'),
 ('Commerce (Lieu 2, exemple fictif)', 'Enseigne', 'Autorisation d’enseigne, terrasse, étalage', 'mairie', 'selon le cas', 'avant la pose', 'exploitant', 'autorisation', 'à vérifier', ''),
 ('Commerce (Lieu 2, exemple fictif)', 'Bail', 'Bail commercial ou dérogatoire ; dépôt de garantie plafonné (baux depuis le 28 mai 2026)', 'notaire ou avocat', '—', 'avant l’entrée dans les lieux', 'propriétaire', 'bail signé', 'à faire valider', 'avocat, notaire'),
 ('Commerce (Lieu 2, exemple fictif)', 'Fiscalité', 'Exonération « France ruralités revitalisation » (sous conditions)', 'administration fiscale', '—', 'à la création', 'exploitant', 'option', 'à faire valider', 'expert-comptable'),
]
s = wb.create_sheet('Échéancier')
for j, h in enumerate(cols, 1):
    c = s.cell(row=1, column=j, value=h); c.font = HF; c.fill = HFILL; c.alignment = Alignment(wrap_text=True, vertical='center'); c.border = B
widths = [5, 26, 18, 44, 26, 22, 20, 18, 20, 14, 20, 13, 12, 12]
for j, w in enumerate(widths, 1): s.column_dimensions[get_column_letter(j)].width = w
s.row_dimensions[1].height = 32
for r, row in enumerate(rows, 2):
    vals = [r - 1] + list(row)
    for j, v in enumerate(vals, 1):
        c = s.cell(row=r, column=j, value=v); c.font = F; c.alignment = WR; c.border = B
for r in range(2, 301):
    s.cell(row=r, column=12).number_format = 'DD/MM/YYYY'; s.cell(row=r, column=14).number_format = 'DD/MM/YYYY'
    s.cell(row=r, column=13, value=f'=IF(L{r}="","",L{r}-TODAY())')
dv = DataValidation(type='list', formula1='"documenté,à vérifier,à faire valider"', allow_blank=True); s.add_data_validation(dv); dv.add('J2:J300')
dv2 = DataValidation(type='list', formula1='"exploitant,propriétaire,dirigeant,administratrice,architecte,expert-comptable,avocat"', allow_blank=True); s.add_data_validation(dv2); dv2.add('H2:H300')
s.freeze_panes = 'C2'; s.auto_filter.ref = 'A1:N1'
s.page_setup.orientation = 'landscape'; s.page_setup.paperSize = s.PAPERSIZE_A4
s.sheet_properties.pageSetUpPr.fitToPage = True; s.page_setup.fitToWidth = 1; s.page_setup.fitToHeight = 0; s.print_title_rows = '1:1'
wb.save(OUT); print('écrit', OUT)
