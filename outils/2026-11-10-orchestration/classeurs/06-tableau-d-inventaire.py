import os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

OUT = '/home/user/Carlone/interne/cadrage/2026-11-10-kit/06-tableau-d-inventaire.xlsx'
os.makedirs(os.path.dirname(OUT), exist_ok=True)
INK, PAPER, BRONZE, RULE = '14181F', 'F6F3EE', '7E5F31', 'D9D2C5'
F = Font(name='Arial', size=10)
HF = Font(name='Arial', size=10, bold=True, color='FFFFFF')
HFILL = PatternFill('solid', fgColor=INK)
EXFILL = PatternFill('solid', fgColor=PAPER)
thin = Side(style='thin', color=RULE)
B = Border(left=thin, right=thin, top=thin, bottom=thin)
WR = Alignment(wrap_text=True, vertical='top')

COMMON = ['Source (dit par qui, ou lu dans quelle pièce)', 'Statut', 'À compléter par']
STATUTS = '"confirmé par écrit,dit en entretien,lu dans une pièce,inconnu"'
SHEETS = [
  ('1 Sociétés', ['N°', 'Nom', 'Forme', 'SIREN', 'Rôle', 'Signataire (fonction)', 'Responsable des données', 'Professionnels (fonction seulement)'],
   {'Rôle': '"propriétaire,exploitante,holding,autre"', 'Responsable des données': '"oui,non,à confirmer"'},
   [['1', 'Entreprise 1 (exemple fictif)', 'SAS', '', 'holding', 'président', 'à confirmer', 'expert-comptable']]),
  ('2 Bâtiments et lots', ['N°', 'Bâtiment', 'Lot', 'Commune', 'Société propriétaire', 'Stade', 'Usage', 'Surface (m²)', 'Année de construction', 'Reçoit du public', 'Bail en cours', 'Chantier en cours', 'Interlocuteur (fonction)', 'Prochaine échéance', 'Pièce manquante'],
   {'Stade': '"projet,promesse,acquis"', 'Reçoit du public': '"oui,non,à vérifier"', 'Bail en cours': '"oui,non,à vérifier"', 'Chantier en cours': '"oui,non,à vérifier"'},
   [['1', 'Bâtiment A (exemple fictif)', 'Lot 1', 'Commune X', 'Entreprise 1', 'acquis', 'commerce', '120', '', 'à vérifier', 'oui', 'non', 'gestionnaire', '', 'diagnostic amiante']]),
  ('3 Lieux et projets', ['N°', 'Nom', 'Type', 'Bâtiment', 'Société qui exploite ou porte', 'Avancement', 'Ouverture visée', 'Interlocuteur (fonction)', 'Autorisations connues', 'Prochaine échéance', 'Fiche courte (douze au plus)'],
   {'Type': '"galerie,cabaret-spectacle,commerce,suites,espace bien-être,bureau,autre"', 'Avancement': '"idée,étude,travaux,ouvert"', 'Fiche courte (douze au plus)': '"oui,non"'},
   [['1', 'Lieu 1 (exemple fictif)', 'commerce', 'Bâtiment A', 'Entreprise 1', 'étude', '', '', '', '', 'oui']]),
  ('4 Contrats et baux', ['N°', 'Type', 'Société', 'Bâtiment ou lieu', 'Autre partie (nom de la société)', "Date d'effet", 'Durée', 'Échéance', 'Préavis', 'Montant, s’il est donné (€)', 'Pièce vue'],
   {'Type': '"bail commercial,bail d\'habitation,assurance,maintenance,abonnement,prestation,autre"', 'Pièce vue': '"oui,non"'},
   [['1', 'assurance', 'Entreprise 1', 'Bâtiment A', 'Entreprise 2', '', '1 an', '', '2 mois', '', 'non']]),
  ('5 Échéances', ['N°', 'Objet', 'Rattachée à', 'Date de la dernière pièce', 'Prochaine date', 'Personne chargée (fonction)', 'Rôle qui porte l’obligation', 'Pièce attendue', 'État', 'Jours restants'],
   {'Rôle qui porte l’obligation': '"propriétaire,exploitant,locataire,à vérifier"', 'État': '"à jour,à prévoir,en retard,pièce manquante,à vérifier"'},
   [['1', 'Vérification électrique (exemple fictif)', 'Bâtiment A', '', '', 'administratrice', 'exploitant', 'rapport de vérification', 'à vérifier', '']]),
  ('6 Tâches administratives', ['N°', 'Tâche', 'Déclencheur', 'Qui la fait (fonction)', 'Qui valide (fonction)', 'Fréquence', 'Volume par mois', 'Temps déclaré (min)', 'Temps relevé (min)', 'Documents en entrée', 'Résultat', 'Outil actuel', 'Données personnelles', 'Erreur fréquente', 'Réversible', 'Niveau d’aide envisagé', 'Retenue pour essai'],
   {'Fréquence': '"quotidienne,hebdomadaire,mensuelle,trimestrielle,annuelle,ponctuelle"', 'Données personnelles': '"oui,non"', 'Réversible': '"oui,non"', 'Niveau d’aide envisagé': '"automatique,assistée,préparée,aucune"', 'Retenue pour essai': '"oui,non,à discuter"'},
   [['1', 'Comparer des devis de travaux (exemple fictif)', 'réception de devis', 'administratrice', 'dirigeant', 'mensuelle', '4', '', '', 'devis PDF', 'tableau comparatif', 'tableur', 'non', '', 'oui', 'assistée', 'à discuter']]),
  ('7 Documents reçus', ['N°', 'Nom', 'Type', 'Société', 'Objet rattaché', 'Reçu le', 'Traitement', 'Données personnelles', 'Rendu ou effacé le'],
   {'Traitement': '"analysé (quinze au plus),seulement listé"', 'Données personnelles': '"oui,non"'},
   [['1', 'Devis toiture (exemple fictif)', 'devis', 'Entreprise 1', 'Bâtiment A', '', 'analysé (quinze au plus)', 'non', '']]),
  ('8 Outils et accès', ['Outil', 'Fournisseur', 'À quoi il sert', 'Compte au nom de', 'Qui y accède (fonction)', 'Accès ouvert à Marwin Tech', 'Date d’ouverture'],
   {'Accès ouvert à Marwin Tech': '"oui,non"'},
   [['Tableur (exemple fictif)', 'Entreprise 3', 'suivi des échéances', 'Entreprise 1', 'administratrice', 'non', '']]),
  # Feuille 9 : mêmes deux blocs que le tableau « Qui valide quoi » joint au bon de commande (11 novembre 2026).
  # Une ligne réduite à une seule chaîne est un titre de bloc.
  ('9 Rôles', ['Acte', 'Qui prépare', 'Notre proposition', 'Personne désignée (fonction)', 'Montant ou limite', 'En cas d’absence', 'Écrit reçu le'],
   {},
   [['Pendant le cadrage'],
    ['Signer le bon de commande', 'Marwin Tech', 'la personne habilitée de la société qui commande', '', '—', '', ''],
    ['Signer l’accord sur les données', 'Marwin Tech', 'la personne habilitée de la société responsable des données', '', '—', '', ''],
    ['Choisir les trois priorités', 'Marwin Tech', 'le dirigeant', '', '—', '', ''],
    ['Valider l’inventaire et la liste des tâches à essayer', 'Marwin Tech', 'le dirigeant, ou l’administratrice s’il l’y autorise', '', '—', '', ''],
    ['Signer la réception', 'Marwin Tech', 'le dirigeant, ou la personne qu’il désigne', '', '—', '', ''],
    ['Ouvrir des documents et des accès', '', 'l’administratrice, dans les limites fixées', '', '', '', ''],
    ['Répondre aux questions courantes', '—', 'l’administratrice', '', '—', '', ''],
    ['Engager une dépense', '—', 'personne : aucune dépense pendant le cadrage', '', '—', '—', ''],
    ['Décider d’une suite', 'Marwin Tech', 'le dirigeant', '', '—', '—', ''],
    ['Au nom de la société, aujourd’hui (aucun de ces actes n’est fait par Marwin Tech pendant le cadrage)'],
    ['Payer une facture', '', '—', '', '', '', ''],
    ['Signer un devis ou un contrat', '', '—', '', '', '', ''],
    ['Envoyer un courrier ou un message', '', '—', '', '', '', ''],
    ['Publier en ligne (site, réseaux, annonces)', '', '—', '', '', '', ''],
    ['Valider un texte ou une image à diffuser', '', '—', '', '', '', ''],
    ['Donner ou retirer un accès', '', '—', '', '', '', ''],
    ['Supprimer un document', '', '—', '', '', '', ''],
    ['Répondre à un client des suites', '', '—', '', '', '', ''],
    ['Modifier ou annuler une réservation', '', '—', '', '', '', '']]),
  ('10 Priorités et essais', ['Priorité', 'Objectif mesurable', 'Budget indicatif (€)', 'Responsable (fonction)', 'Coût actuel', 'Seuil de réussite', 'Tâche liée', 'Niveau d’aide', 'Mesure de départ', 'Condition d’essai'],
   {'Niveau d’aide': '"automatique,assistée,préparée"'},
   [['Exemple fictif : suivre les échéances des bâtiments', 'zéro échéance découverte en retard sur trois mois', '', 'administratrice', '', '', 'rappels d’échéances', 'assistée', '', 'un seul bâtiment, quatre semaines']]),
  ('11 Décisions', ['Date', 'Décision', 'Prise par (fonction)', 'Source', 'Suite', 'Échéance'], {}, []),
]

wb = Workbook()
ws = wb.active
ws.title = 'Lisez-moi'
lines = [
  ('Tableau d’inventaire du cadrage', Font(name='Arial', size=14, bold=True, color=INK)),
  ('Document interne — ne pas transmettre à GianLuca Carlone · 10 novembre 2026, corrigé le 11 novembre 2026', Font(name='Arial', size=10, bold=True, color=BRONZE)),
  ('', F),
  ('À quoi il sert : recenser, pendant le cadrage, les sociétés, bâtiments, lieux, commerces, projets, contrats, échéances, tâches, documents et outils, à partir de ce que le client nous donne. Il nourrit le dossier remis.', F),
  ('Comment le remplir : une ligne par élément ; une feuille par objet. Chaque feuille finit par trois colonnes communes : la source (dit par qui, ou lu dans quelle pièce), le statut (liste de choix) et qui doit compléter.', F),
  ('Statuts : « confirmé par écrit », « dit en entretien », « lu dans une pièce », « inconnu ». Un inconnu reste inconnu : on ne le remplit jamais de soi-même.', F),
  ('Bornes du cadrage : douze fiches courtes au plus ; trois sociétés au plus ; une quinzaine de documents analysés au plus, les autres seulement listés.', F),
  ('Ce que le tableau ne fait pas : il ne juge rien conforme ou non conforme ; il ne contient aucune coordonnée de personne (fonction seulement) ; aucun mot de passe ; aucune donnée bancaire ou de santé.', F),
  ('Les lignes grisées sont des exemples fictifs : à supprimer avant usage.', F),
  ('Feuille « 5 Échéances » : la colonne « Jours restants » se calcule seule à partir de la prochaine date.', F),
  ('Feuille « 9 Rôles » : les deux blocs du tableau « Qui valide quoi » joint au bon de commande. « Pendant le cadrage » : nos propositions, à faire confirmer par écrit. « Au nom de la société, aujourd’hui » : comment ces actes se décident chez le client, pour préparer la grille de délégation ; ce relevé ne vaut pas délégation de pouvoirs.', F),
]
for i, (t, f) in enumerate(lines, 1):
    c = ws.cell(row=i, column=1, value=t); c.font = f; c.alignment = WR
ws.column_dimensions['A'].width = 120
ws.page_setup.orientation = 'portrait'

for title, cols, lists, examples in SHEETS:
    s = wb.create_sheet(title)
    allc = cols + COMMON
    for j, h in enumerate(allc, 1):
        c = s.cell(row=1, column=j, value=h); c.font = HF; c.fill = HFILL; c.alignment = Alignment(wrap_text=True, vertical='center'); c.border = B
        s.column_dimensions[get_column_letter(j)].width = max(12, min(34, len(h) + 4))
    s.row_dimensions[1].height = 42
    if title == '9 Rôles': s.column_dimensions['A'].width = 34
    bloc = 0
    for r, ex in enumerate(examples, 2):
        if len(ex) == 1:  # titre de bloc (feuille 9)
            bloc += 1
            c = s.cell(row=r, column=1, value=ex[0]); c.font = Font(name='Arial', size=10, bold=True, color=BRONZE); c.alignment = WR; c.border = B
            s.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(allc))
            continue
        if title != '9 Rôles':
            row = ex + ['Exemple fictif', 'inconnu', '']
        elif bloc == 1:
            row = ex + ['proposition de cadrage, version client (10 novembre), et tableau « Qui valide quoi » (11 novembre)', 'inconnu', 'dirigeant']
        else:
            row = ex + ['tableau « Qui valide quoi » (11 novembre)', 'inconnu', 'dirigeant']
        for j, v in enumerate(row, 1):
            c = s.cell(row=r, column=j, value=v); c.font = F; c.alignment = WR; c.border = B
            if title != '9 Rôles': c.fill = EXFILL
    last = 300
    for name, formula in lists.items():
        j = allc.index(name) + 1
        dv = DataValidation(type='list', formula1=formula, allow_blank=True); s.add_data_validation(dv)
        dv.add(f'{get_column_letter(j)}2:{get_column_letter(j)}{last}')
    js = allc.index('Statut') + 1
    dv = DataValidation(type='list', formula1=STATUTS, allow_blank=True); s.add_data_validation(dv)
    dv.add(f'{get_column_letter(js)}2:{get_column_letter(js)}{last}')
    for name in allc:
        if any(k in name for k in ('Date', 'date', 'Échéance', 'Reçu le', 'effacé le', 'Ouverture visée', 'Écrit reçu')):
            j = allc.index(name) + 1
            for r in range(2, last + 1): s.cell(row=r, column=j).number_format = 'DD/MM/YYYY'
        if '(€)' in name:
            j = allc.index(name) + 1
            for r in range(2, last + 1): s.cell(row=r, column=j).number_format = '#,##0 €'
    if title == '5 Échéances':
        jd = allc.index('Prochaine date') + 1; jr = allc.index('Jours restants') + 1
        for r in range(2, last + 1):
            s.cell(row=r, column=jr, value=f'=IF({get_column_letter(jd)}{r}="","",{get_column_letter(jd)}{r}-TODAY())')
    s.freeze_panes = 'B2'
    s.auto_filter.ref = f'A1:{get_column_letter(len(allc))}1'
    s.page_setup.orientation = 'landscape'; s.page_setup.paperSize = s.PAPERSIZE_A4
    s.sheet_properties.pageSetUpPr.fitToPage = True; s.page_setup.fitToWidth = 1; s.page_setup.fitToHeight = 0
    s.print_title_rows = '1:1'
wb.save(OUT)
print('écrit', OUT)
