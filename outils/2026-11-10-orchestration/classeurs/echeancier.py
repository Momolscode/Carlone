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
  ('Échéancier — cabaret, commerces et suites', Font(name='Arial', size=14, bold=True)),
  ('PROJET non envoyé — à valider par Morgan Olsen et Mathys Couet · 10 novembre 2026, corrigé le 11 novembre 2026', Font(name='Arial', size=10, bold=True, color='7E5F31')),
  ('', F),
  ('À quoi il sert : suivre, lieu par lieu, les démarches, autorisations et échéances listées dans le document « Cabaret, commerces et suites : autorisations, démarches et échéances ».', F),
  ('Ce n’est pas un avis juridique : chaque ligne est à faire valider par vos professionnels (avocat, notaire, expert-comptable, architecte, assureur) avant toute démarche.', F),
  ('Statuts : « documenté » (page officielle citée dans la dernière colonne, consultée le 10 ou le 11 novembre 2026, à revérifier à la date de la démarche) ; « à vérifier » (page officielle pas encore relue ou situation du lieu inconnue) ; « à faire valider ».', F),
  ('Responsable : un rôle (exploitant, propriétaire, architecte, administratrice…), jamais un nom ni une coordonnée.', F),
  ('La colonne « Jours restants » se calcule seule à partir de la date prévue. « Lieu 1 », « Lieu 2 » et « Lieu 3 » sont des exemples fictifs, à renommer avec vos lieux.', F)], 1):
    c = ws.cell(row=i, column=1, value=t); c.font = f; c.alignment = WR
ws.column_dimensions['A'].width = 120
cols = ['N°', 'Lieu', 'Famille', 'Démarche ou échéance', 'Auprès de', 'Délai ou rythme indiqué', 'Quand', 'Responsable (rôle)', 'Pièce qui le prouve', 'Statut', 'À faire valider par', 'Date prévue', 'Jours restants', 'Fait le', 'Page officielle citée']
C, M, S = 'Cabaret (Lieu 1, exemple fictif)', 'Commerce (Lieu 2, exemple fictif)', 'Suites et espace bien-être (Lieu 3, exemple fictif)'
SP = 'Service Public Entreprendre, fiche '
DRAC = 'direction régionale des affaires culturelles (DRAC)'
rows = [
 # Cabaret, avant l’ouverture : les numéros 1 à 12 sont ceux des étapes du document.
 (C, 'Organisation', 'Fixer la société qui exploite, le lieu, le nombre de personnes accueillies, avec ou sans repas', 'vous', '—', 'avant tout', 'dirigeant', 'décision écrite', 'à faire valider', 'avocat, expert-comptable', ''),
 (C, 'Travaux', 'Plans, étude acoustique, premier échange sécurité', 'architecte, acousticien, mairie', 'inconnu', 'avant les travaux', 'exploitant', 'plans, étude', 'à faire valider', 'architecte', ''),
 (C, 'Lieu recevant du public', 'Autorisation de travaux (ou permis qui en tient lieu) ; architecte obligatoire pour le permis d’une société', 'mairie', '4 mois avec déclaration préalable, 5 avec permis', 'avant les travaux', 'exploitant', 'arrêté', 'documenté', 'architecte', SP + 'F31687, vérifiée le 20 septembre 2024'),
 (C, 'Urbanisme', 'Si site patrimonial remarquable : accord de l’architecte des Bâtiments de France', 'mairie', 'allongé (déclaration préalable : 2 mois au lieu d’1)', 'avant les travaux', 'propriétaire', 'avis', 'à vérifier', 'architecte', SP + 'F17578, vérifiée le 22 octobre 2026 (délai) ; Ministère de la Culture, base Mérimée, notice SPR2700038 (site patrimonial remarquable de Cosne-Cours-sur-Loire), mise à jour le 9 octobre 2026'),
 (C, 'Boissons', 'Licence (achat ou transfert) ; formation au permis d’exploitation', 'vendeur, préfecture, organisme de formation', 'inconnu', 'avant l’ouverture', 'exploitant', 'licence, attestation', 'à vérifier', 'avocat', ''),
 (C, 'Spectacle', 'Déclaration d’entrepreneur de spectacles', DRAC, '30 jours après dossier complet, sauf opposition du préfet', 'avant la première représentation', 'exploitant', 'récépissé', 'documenté', 'avocat', SP + 'F22365, vérifiée le 5 avril 2024'),
 (C, 'Bruit', 'Étude de l’impact des nuisances sonores', 'acousticien', 'avant le démarrage', 'avant l’ouverture', 'exploitant', 'étude', 'à vérifier', 'acousticien', ''),
 (C, 'Restauration', 'Déclaration de la cuisine ; formation à l’hygiène', 'protection des populations', 'avant l’ouverture', 'avant l’ouverture', 'exploitant', 'récépissé, attestation', 'à vérifier', 'à désigner', ''),
 (C, 'Boissons', 'Déclaration du débit de boissons', 'mairie', '15 jours avant (à vérifier)', 'avant l’ouverture', 'exploitant', 'récépissé', 'à vérifier', 'mairie', ''),
 (C, 'Horaires', 'Heures de fermeture ; dérogation éventuelle pour fermer plus tard', 'préfecture, mairie', 'à vérifier', 'avant l’ouverture', 'exploitant', 'arrêté', 'à vérifier', 'avocat', ''),
 (C, 'Caisse et billetterie', 'Caméras ; logiciel de caisse (certificat ou attestation de l’éditeur) ; déclaration de la billetterie ; droits d’auteur', 'préfecture, éditeur, administration fiscale, sociétés d’auteurs', 'avant l’ouverture', 'avant l’ouverture', 'exploitant', 'autorisation, attestation, déclaration, contrats', 'à faire valider', 'expert-comptable, avocat', ''),
 (C, 'Sécurité', 'Si le lieu dépasse les petits établissements (seuil à vérifier) : visite de la commission, puis arrêté d’ouverture', 'commission, maire', 'avant l’ouverture', 'avant l’ouverture', 'exploitant', 'procès-verbal, arrêté', 'à vérifier', 'architecte, bureau de contrôle', ''),
 # Cabaret, une fois ouvert.
 (C, 'Taxe', 'Déclaration de la taxe sur les spectacles (3,5 % de la billetterie hors TVA)', 'Centre national de la musique', 'au plus tard le dernier jour du 3e mois qui suit', 'après chaque représentation', 'exploitant', 'déclaration', 'documenté', 'expert-comptable', 'Centre national de la musique, page « Taxe », date non affichée'),
 (C, 'Sécurité', 'Vérification des installations techniques (petit lieu, 5e catégorie)', 'bureau de contrôle', 'tous les 3 ans au plus (depuis le 1er juillet 2026)', 'récurrent', 'exploitant', 'rapport', 'documenté', 'bureau de contrôle', 'Légifrance, arrêté du 25 juin 1980 (règlement de sécurité des lieux recevant du public), article PE 4, modifié par l’arrêté du 1er décembre 2025, en vigueur depuis le 1er juillet 2026'),
 (C, 'Sécurité', 'Visite périodique de la commission', 'commission de sécurité', 'tous les 3 ou 5 ans de la 1re à la 4e catégorie ; 5e : à vérifier', 'récurrent', 'exploitant', 'procès-verbal', 'documenté', 'architecte, bureau de contrôle', 'Légifrance, arrêté du 25 juin 1980 (règlement de sécurité), article GE 4, version du 1er janvier 2015'),
 (C, 'Bruit', 'Vérification des équipements de mesure du son', 'professionnel indépendant', 'tous les deux ans (à vérifier)', 'récurrent', 'exploitant', 'rapport', 'à vérifier', 'acousticien', ''),
 (C, 'Spectacle', 'Renouvellement de la déclaration d’entrepreneur de spectacles', DRAC, 'tous les 5 ans', 'récurrent', 'exploitant', 'récépissé', 'documenté', 'avocat', SP + 'F22365, vérifiée le 5 avril 2024'),
 (C, 'Boissons', 'Renouvellement du permis d’exploitation', 'organisme de formation', 'tous les 10 ans (à vérifier)', 'récurrent', 'exploitant', 'attestation', 'à vérifier', 'avocat', ''),
 (C, 'Spectacle', 'Numéro du récépissé d’entrepreneur de spectacles sur les affiches, prospectus et billets', '—', 'sur chaque affiche, prospectus et billet', 'en continu', 'exploitant', 'affiches, billets', 'documenté', 'avocat', SP + 'F22365, vérifiée le 5 avril 2024'),
 (C, 'Sécurité', 'Registre de sécurité, exercices d’incendie compris', '—', 'tenu à jour', 'en continu', 'exploitant', 'registre de sécurité', 'documenté', 'bureau de contrôle', 'Légifrance, code de la construction et de l’habitation, article R143-44, version du 1er juillet 2026'),
 (C, 'Bruit', 'Enregistrement des niveaux sonores dans les grandes salles (seuil à vérifier)', '—', 'à vérifier', 'en continu', 'exploitant', 'enregistrements', 'à vérifier', 'acousticien', ''),
 (C, 'Emploi', 'Emploi des artistes : présumés salariés ; autorisation préalable du préfet pour employer un mineur', 'préfet (mineurs)', 'avant l’engagement (à vérifier)', 'avant chaque engagement', 'exploitant', 'contrats, autorisation', 'à vérifier', 'avocat, expert-comptable', ''),
 # Commerces.
 (M, 'Urbanisme', 'Déclaration préalable ou permis si la destination ou la façade change ; dépôt en ligne pour une société', 'mairie', 'déclaration préalable : 1 mois, 2 en secteur protégé', 'avant les travaux', 'propriétaire', 'arrêté', 'à faire valider', 'architecte', SP + 'F17578, vérifiée le 22 octobre 2026'),
 (M, 'Lieu recevant du public', 'Autorisation de travaux, même intérieurs ; accessibilité', 'mairie', '4 mois avec déclaration préalable, 5 avec permis', 'avant les travaux', 'exploitant', 'arrêté', 'documenté', 'architecte', SP + 'F31687, vérifiée le 20 septembre 2024'),
 (M, 'Grandes surfaces', 'Autorisation d’exploitation commerciale pour les grands magasins (plus de 1 000 m² ; seuils à vérifier)', 'à vérifier', 'à vérifier', 'avant l’ouverture', 'exploitant', 'autorisation', 'à vérifier', 'avocat', ''),
 (M, 'Enseigne', 'Autorisation d’enseigne, terrasse, étalage', 'mairie', 'selon le cas', 'avant la pose', 'exploitant', 'autorisation', 'à vérifier', 'architecte, mairie', ''),
 (M, 'Bail', 'Bail commercial ou dérogatoire ; garanties limitées à un trimestre de loyer (local de commerce, bail conclu ou renouvelé depuis fin mai 2026)', 'notaire ou avocat', '—', 'avant l’entrée dans les lieux', 'propriétaire', 'bail signé', 'à faire valider', 'avocat, notaire', SP + 'F32304 ; loi n° 2026-403 du 26 mai 2026, article 62'),
 (M, 'Fiscalité', 'Exonération « France ruralités revitalisation » (sous conditions ; classement de la commune à vérifier)', 'administration fiscale', '—', 'à la création', 'exploitant', 'option', 'à faire valider', 'expert-comptable', SP + 'F31139, vérifiée le 21 février 2026'),
 (M, 'Emploi', 'Premier salarié : déclaration préalable à l’embauche, affichages, document unique', 'à vérifier', 'avant l’embauche', 'avant la première embauche', 'exploitant', 'déclaration, affichages, document unique', 'à faire valider', 'expert-comptable', ''),
 # Vos neuf suites et l’espace bien-être.
 (S, 'Sécurité', 'Locaux à sommeil : règles de sécurité, visites de la commission ; effet sur le classement de l’ensemble si les lieux communiquent', 'architecte, bureau de contrôle', 'inconnu', 'avant les travaux', 'exploitant', 'avis, procès-verbal', 'à faire valider', 'architecte', ''),
 (S, 'Hébergement', 'Fiche de police des clients étrangers, conservée six mois', '—', 'à chaque arrivée', 'en continu', 'exploitant', 'fiches', 'documenté', 'avocat', SP + 'F17452 (chambres d’hôtes), vérifiée le 21 mai 2026'),
 (S, 'Taxe', 'Taxe de séjour (au réel ou au forfait, selon la délibération locale)', 'mairie', 'selon la délibération', 'récurrent', 'exploitant', 'déclarations', 'à vérifier', 'expert-comptable', ''),
 (S, 'Prix', 'Affichage des prix (nuitée, prestations, en ligne)', '—', '—', 'avant l’ouverture', 'exploitant', 'affichage', 'à vérifier', 'avocat, expert-comptable', ''),
 (S, 'Classement', 'Classement en étoiles (volontaire)', 'à vérifier', 'à vérifier', 'si vous le choisissez', 'dirigeant', 'décision de classement', 'à vérifier', 'avocat, expert-comptable', ''),
 (S, 'Bien-être', 'Jacuzzi partagé par les clients : déclaration d’ouverture avec dossier justificatif (règles des piscines d’usage collectif ; un jacuzzi réservé au client d’une seule suite n’est pas concerné)', 'mairie', 'au plus tard 2 mois avant l’ouverture (code du sport, art. A322-4)', 'avant l’ouverture', 'exploitant', 'récépissé', 'documenté', 'installateur, mairie', 'Légifrance, code de la santé publique, art. L1332-1 ; code du sport, art. A322-4 ; ARS Bourgogne-Franche-Comté, page du 19 juin 2025 ; arrêtés du 26 mai 2021 et du 23 juin 2026, art. 1er'),
 (S, 'Bien-être', 'Jacuzzi : carnet sanitaire ; affichage des derniers résultats et de la durée conseillée (15 minutes au plus, déconseillé aux moins de 10 ans) ; fréquentation maximale affichée, sauf dispense des petites installations', '—', 'relevés 1 fois par jour (15 personnes ou moins) ou 2 fois par jour (16 à 150 ; 1 fois avec des régulateurs en continu)', 'en continu', 'exploitant', 'carnet sanitaire', 'documenté', 'installateur, mairie, agence régionale de santé', 'Légifrance, code de la santé publique, art. D1332-4, D1332-7 et D1332-10 ; arrêtés du 26 mai 2021 et du 23 juin 2026, annexe II'),
 (S, 'Bien-être', 'Jacuzzi : vidange complète, nettoyage et désinfection', 'personne chargée de l’entretien', 'au moins 2 fois par mois sous 10 m³ ; 2 fois par an à partir de 10 m³', 'récurrent', 'exploitant', 'carnet sanitaire', 'documenté', 'installateur', 'Légifrance, arrêté du 19 décembre 2025, art. 15'),
 (S, 'Bien-être', 'Jacuzzi : l’exploitant commande lui-même les analyses de l’eau à un laboratoire accrédité, toujours à ses frais ; résultats affichés ; incidents qui peuvent toucher la santé des baigneurs signalés à l’agence régionale de santé', 'laboratoire accrédité', '1 fois par an (15 personnes ou moins) ou par trimestre (16 à 150) ; légionelles 1 fois par an', 'dès le 1er janvier 2027 de 16 à 150 personnes ; déjà dû à 15 personnes ou moins', 'exploitant', 'rapports d’analyse', 'documenté', 'installateur, mairie', 'Légifrance, décret n° 2026-118 du 20 février 2026, art. 2 ; code de la santé publique, art. D1332-10, III ; arrêtés du 26 mai 2021 et du 23 juin 2026, annexe II'),
 (S, 'Bien-être', 'Sauna : hygiène (règlement sanitaire de la Nièvre, art. 71), sécurité de l’installation (poêle, électricité) et affichage des précautions d’usage (obligation générale de sécurité)', 'mairie, bureau de contrôle, assureur', 'à vérifier', 'avant l’ouverture', 'exploitant', 'rapport, affichage', 'à faire valider', 'mairie, bureau de contrôle, assureur', 'Préfecture de la Nièvre, règlement sanitaire départemental, art. 71 ; Légifrance, code de la consommation, art. L421-3 (version du 13 décembre 2024)'),
 (S, 'Bien-être', 'Dispositif contre la noyade (barrière, alarme, couverture ou abri) si le bassin est dehors et enterré, en tout ou en partie', 'installateur', 'à vérifier', 'avant l’ouverture', 'exploitant', 'note technique', 'à faire valider', 'installateur, architecte', 'Service Public, fiche F1722, vérifiée le 13 février 2026 ; Légifrance, code de la construction et de l’habitation, art. D134-51'),
 (S, 'Assurance', 'Déclarer l’hébergement, l’espace bien-être et les événements', 'assureur', '—', 'avant l’ouverture', 'dirigeant', 'attestation', 'à faire valider', 'assureur', ''),
]
s = wb.create_sheet('Échéancier')
for j, h in enumerate(cols, 1):
    c = s.cell(row=1, column=j, value=h); c.font = HF; c.fill = HFILL; c.alignment = Alignment(wrap_text=True, vertical='center'); c.border = B
widths = [5, 26, 18, 44, 26, 22, 20, 18, 20, 14, 20, 13, 12, 12, 34]
for j, w in enumerate(widths, 1): s.column_dimensions[get_column_letter(j)].width = w
s.row_dimensions[1].height = 32
for r, row in enumerate(rows, 2):
    vals = [r - 1] + list(row[:10])
    for j, v in enumerate(vals, 1):
        c = s.cell(row=r, column=j, value=v); c.font = F; c.alignment = WR; c.border = B
    c = s.cell(row=r, column=15, value=row[10] or None); c.font = F; c.alignment = WR; c.border = B
for r in range(2, 301):
    s.cell(row=r, column=12).number_format = 'DD/MM/YYYY'; s.cell(row=r, column=14).number_format = 'DD/MM/YYYY'
    s.cell(row=r, column=13, value=f'=IF(L{r}="","",L{r}-TODAY())')
dv = DataValidation(type='list', formula1='"documenté,à vérifier,à faire valider"', allow_blank=True); s.add_data_validation(dv); dv.add('J2:J300')
dv2 = DataValidation(type='list', formula1='"exploitant,propriétaire,dirigeant,administratrice,architecte,expert-comptable,avocat"', allow_blank=True); s.add_data_validation(dv2); dv2.add('H2:H300')
s.freeze_panes = 'C2'; s.auto_filter.ref = 'A1:O1'
s.page_setup.orientation = 'landscape'; s.page_setup.paperSize = s.PAPERSIZE_A4
s.sheet_properties.pageSetUpPr.fitToPage = True; s.page_setup.fitToWidth = 1; s.page_setup.fitToHeight = 0; s.print_title_rows = '1:1'
wb.save(OUT); print('écrit', OUT)
