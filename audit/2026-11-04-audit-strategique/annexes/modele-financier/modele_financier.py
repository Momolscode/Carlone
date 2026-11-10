#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modèle financier de l'audit Marwin Tech × GianLuca Carlone (version du 4 novembre 2026).

DOCUMENT INTERNE : coûts, marges, rémunérations visées, probabilités et tests de résistance.
Rien de ce qui sort de ce script ne doit être transmis à GianLuca Carlone
(audit-work/strategie-retenue.md:787-789).

Ce que fait le script (bibliothèque standard seulement, aucune action extérieure) :
  1. il construit, mois par mois, les trois scénarios de la stratégie retenue (prudent, central,
     ambitieux) à partir des paramètres ci-dessous ;
  2. il calcule chiffre d'affaires, TVA collectée et reversée, coûts, rémunérations, IS, trésorerie,
     réserve et seuil de rentabilité ;
  3. il écrit dans son propre dossier :
       scenarios.md, tresorerie-18-mois.csv, tresorerie-18-mois.md, stress-tests.md, structures.md ;
  4. il vérifie la cohérence de ses sorties (sommes, signes, TVA) et s'arrête en cas d'écart.

Usage : python3 modele_financier.py            (écrit à côté du script)
        python3 modele_financier.py --sortie DOSSIER

Codes (audit-work/../BRIEF-AGENTS.md) : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ;
[HY] hypothèse ; [ES] estimation ou simulation ; [MM] mesure ; [IN] inconnu.

Sources : « audit-work/ » désigne le dossier de travail de l'audit du 4 nov. 2026 (hors dépôt).
Les pièces du dépôt sont citées par leur chemin dans le dépôt (commit 7b46602).
Tous les résultats du modèle sont des estimations [ES] ; ils sont arrondis à la centaine d'euros
(à la dizaine pour les prix par JP).
"""

import argparse
import copy
import csv
import math
import os
from dataclasses import dataclass, field

# =====================================================================================
# 0. ABRÉVIATIONS DE SOURCES
# =====================================================================================
STRAT = "audit-work/strategie-retenue.md"        # référence de l'audit (arbitre final, 4 nov. 2026)
DROIT = "audit-work/syn-droit.md"                # synthèse juridique (structures, TVA, IS)
R1 = "audit-work/rj-R1-structures.md"            # mémo structures (barèmes 2026)
VR1 = "audit-work/ver-R1-structures.md"          # contrôle du mémo R1
R2 = "audit-work/rj-R2-fiscal.md"                # mémo fiscal (TVA, facturation)
R6 = "audit-work/rj-R6-marche.md"                # mémo marché (coûts des outils)
VR6 = "audit-work/ver-R6-marche.md"              # contrôle du mémo R6
SYNP = "audit-work/syn-portefeuille.md"          # synthèse du portefeuille de projets
NOTE = "audit-work/note-point-4-novembre-et-activites.md"
OFF = "interne/offre-marwin-tech-remuneration-et-collaboration.md"   # offre écrite du 2 nov. (dépôt)
ACC = "sources/chatgpt-pages/2026-11-04/marwin-offre-accompagnement.md"  # version du 29 oct. (dépôt)

# =====================================================================================
# 1. CALENDRIER
# =====================================================================================
# Le modèle tourne sur 26 mois à partir de novembre 2026 (indice t = 0) pour couvrir les 12 mois de
# contrat du scénario prudent et le paiement de l'IS du premier exercice. Les sorties « 18 mois »
# couvrent novembre 2026 à avril 2028 (DEMANDE § 12 ; horizon fixé par STRAT:487).
N_SIM = 26
HORIZON_TRESO = 18
_NOMS = ["janv.", "févr.", "mars", "avr.", "mai", "juin", "juil.", "août", "sept.", "oct.", "nov.", "déc."]
MOIS = [f"{_NOMS[(10 + i) % 12]} {2026 + (10 + i) // 12}" for i in range(N_SIM)]
T_DEC_2027 = 13          # dernier mois du premier exercice [HY] : création fin 2026 ou début 2027,
                         # clôture au 31 déc. 2027 (date à arrêter avec l'expert-comptable, STRAT:552)
T_PAIEMENT_IS_EX1 = 18   # mai 2028 : solde de l'IS du premier exercice [HY] (pas d'acompte la 1re année)

# =====================================================================================
# 2. PARAMÈTRES FISCAUX ET SOCIAUX
# =====================================================================================
TVA = 0.20               # [FV] taux normal sur les prestations de Marwin ; TVA exigible à l'encaissement
                         # pour les services et les acomptes (R2:385 ; DROIT:300). Facturée dès la
                         # 1re facture, sans compter sur la franchise (STRAT:462 ; DROIT:299).
TVA_DECALAGE = 1         # [HY] régime réel normal, déclaration CA3 mensuelle : la TVA nette du mois m est
                         # reversée au mois m+1 ; un crédit est reporté. Régime à choisir avec
                         # l'expert-comptable (DROIT:299, 703-729). Variante « réel simplifié » : section
                         # TVA de tresorerie-18-mois.md.

IS_TAUX_REDUIT = 0.15    # [FV] art. 219 CGI : 15 % jusqu'à 42 500 € de bénéfice par période de 12 mois,
IS_SEUIL = 42500         #      capital entièrement libéré et détenu à 75 % au moins par des personnes
IS_TAUX_NORMAL = 0.25    #      physiques ; 25 % au-delà (DROIT:142 ; VR1:21 ; R1:94-99).
PFU = 0.314              # [FV] prélèvement forfaitaire unique sur dividendes depuis le 1er janv. 2026
                         # (12,8 % d'IR + 18,6 % de prélèvements sociaux) (DROIT:144 ; VR1:22).

# SAS : président et directeur général « assimilés salariés ».
COEF_SAS = {"bas": 1.70, "central": 1.80, "haut": 1.90}
                         # [HY] coût total pour la société = 1,7 à 1,9 fois le net ; source secondaire
                         # unique (Bpifrance), non vérifiable sur urssaf.fr (HTTP 503 le 4 nov.)
                         # (DROIT:98 ; R1:50 ; VR1:40). Central 1,8 (STRAT:478).
NET_SUR_BRUT_SAS = 0.75  # [HY] « charges ≈ 80 % du net, soit 60 % du brut » (Bpifrance, R1:50) => net ≈ 75 %
                         # du brut ; sert seulement à afficher un brut indicatif.

# SARL : deux cogérants à 50/50 => collège de gérance majoritaire => tous deux TNS [FV] (DROIT:109).
PASS = 48060             # [FV] plafond annuel de la sécurité sociale 2026 (VR1:20 ; F38152)
TNS_ABATTEMENT = 0.26    # [FV] assiette = revenu avant cotisations − 26 % (art. L136-3 III CSS) ; plancher et
                         # plafond de l'abattement ignorés [ES] (VR1:20 ; DROIT:97)
TNS_FORFAIT_DEBUT = 3591 # [FV] cotisations forfaitaires de début d'activité 2026, CFP comprise, régularisées
                         # ensuite (96 + 1 631 + 739 + 119 + 886 + 120) (VR1:20 ; DROIT:111). Montant 2027 [IN].
TNS_MINIMUM = 1255       # [ES] minimum annuel par gérant même sans rémunération (R1:47 ; non vérifiable
                         # selon VR1:39).
# Les taux TNS ci-dessous sont ceux « revenus 2025 » publiés par F38152 (vérifiée le 08/10/2026) ; les taux
# applicables aux revenus 2026-2027 sont [IN] (R1:37-44 ; VR1:20). Fonction reprise de la simulation de la
# synthèse juridique (scratchpad/syn-droit-calc/sim.py), pour rester comparable à DROIT:118-136.

# =====================================================================================
# 3. RÈGLES DE GESTION RETENUES
# =====================================================================================
RESERVE = 0.10           # [PR] 10 % du CA encaissé HT mis en réserve (STRAT:479)
MOIS_DEBUT_REMU = 4      # [PR] aucune rémunération avant le mois 4 (STRAT:511)
NET_PLAFOND_ASSOCIE = 2500   # [PR] plafond de net mensuel par associé = « plancher » de 2 500 € nets par ETP
                         # des archives (OFF:112-114 ; STRAT:359), jamais dépassé dans le modèle
OBJECTIF_RESERVE_MOIS_FRAIS = 3  # [PR] viser au mois 12 : 3 mois de frais fixes + 1 mois de rémunération
OBJECTIF_RESERVE_MOIS_REMU = 1   #      (STRAT:175, 512)
FRAIS_REDUITS_APRES_RUPTURE = 1000  # [PR] frais ramenés à ≈ 1 000 € par mois après une rupture (STRAT:529)

# Règle de calcul de la rémunération [PR du modèle, à valider par les associés] :
# une enveloppe mensuelle constante E (coût total pour la société, pour les deux associés ensemble)
# est versée à partir du mois 4. E est la plus grande enveloppe telle que, sur les mois 4 à 12, les
# encaissements HT couvrent les frais, la sous-traitance, la réserve de 10 % et l'IS de la période.
# L'excédent des mois 1 à 3 reste en trésorerie (même logique que STRAT:518, verif § 10), l'apport
# finance le démarrage. Même enveloppe E pour la SAS et la SARL (« mêmes hypothèses économiques »).

# =====================================================================================
# 4. OFFRES, PRIX ET MODALITÉS [PR] (STRAT:194-203, 438-446, 498)
# =====================================================================================
PRIX = {
    "cadrage": 6500,           # A, forfait 8 JP ; 50 % à la commande, 50 % à la réception (STRAT:197, 440)
    "cadrage_plancher": 6000,  # A au plancher (scénario prudent, STRAT:498)
    "b0": 3500,                # B0 socle pilote, mensuel d'avance, 2 mois (STRAT:198)
    "b1": 4500,                # B1 « socle + 2 projets », mensuel d'avance (STRAT:199)
    "socle_leger": 3000,       # « socle + 1 projet » du scénario prudent (STRAT:498)
    "socle_3": 5700,           # B1 + 1 projet actif (« socle + 3 »), scénario ambitieux (STRAT:498)
    "lot_pilote": 6000,        # lot du pilote (C2 ou équivalent) : 40 % commande, 60 % livraison (STRAT:201, 442)
    "lot_prudent": 4500,       # un lot par trimestre (STRAT:498)
    "lots_mois_central": 3500, # lots ≈ 3 500 € par mois en moyenne (STRAT:498)
    "lots_mois_ambitieux": 4500,
    "lots_mois_variante": 2000,  # variante centrale avec second client, à partir du mois 7 (STRAT:522)
    "exploitation": 1500,      # D, minimum mensuel d'avance, au plus tôt au mois 7 (STRAT:339-349, 494, 498)
    "second_client_amb": 2500, # second client, scénario ambitieux, à partir du mois 6 (STRAT:494, 498)
    "second_client_var": 2000, # variante centrale, à partir du mois 7 (STRAT:522)
    "avenant_jp": 900,         # E, avenant de capacité et urgences, par JP (STRAT:203, 353)
}
PRIX_PAR_JP_LOT = 800 * 1.125  # [PR] règle de devis : JP estimées × 800 € + provision de 10 à 15 % (STRAT:287)
JP = {                         # [ES] capacité consommée par prestation (STRAT:197-203, 229, 273)
    "cadrage": (6.0, 2.0),     # 8 JP : mois 1 puis mois 2
    "b0": 3.5, "b1": 5.0, "socle_leger": 3.5, "socle_3": 6.5,
    "exploitation": 1.75,      # 1 à 4 JP par mois
    "second_client_amb": 3.0, "second_client_var": 2.4,
}
SOUS_TRAITANCE = {"jp": 3.0, "prix_jp": 500, "fourchette_prix": (450, 550)}  # [HY] ambitieux (STRAT:503)

# Probabilités de passage [HY] : paramètres de jugement à remplacer par les faits (STRAT:502).
# La probabilité de vendre le cadrage lui-même est [IN] : les montants pondérés sont conditionnels.
PROBA = {
    "prudent": {"suite": 0.40, "renouvellement": 0.60},
    "central": {"pilote": 0.60, "socle": 0.70, "renouvellement": 0.80, "second_client": 0.50},
    "ambitieux": {"pilote": 0.80, "socle": 0.80, "renouvellement": 0.90, "second_client": 0.50},
}

# =====================================================================================
# 5. FRAIS DE MARWIN (HT, par mois, à partir du mois 1) [HY] (STRAT:504-508 ; R6:350-356)
# =====================================================================================
# nom : (coût direct ?, part du montant qui porte une TVA récupérable, commentaire)
FRAIS_LIGNES = {
    "Outils et IA (sièges, API, registre)": (True, 0.0,
        "pile « sobre » 150 à 260 € par mois, « confortable » 650 à 1 000 € [ES] (R6:350-356) ; éditeurs étrangers : "
        "autoliquidation de la TVA, neutre en trésorerie [HY] (R6:383)"),
    "Déplacements chez le client": (True, 0.5,
        "200 à 600 € [IN : lieu de résidence des associés] (STRAT:508) ; TVA récupérable sur la moitié [HY]"),
    "Assurances (RC pro avec volets IA, cyber, données)": (False, 0.0,
        "[IN] ; 100 à 250 € par mois en hypothèse, à remplacer par un devis (STRAT:506) ; pas de TVA"),
    "Expert-comptable et paie": (False, 1.0, "2 000 à 5 000 € HT par an (STRAT:507 ; DROIT:181)"),
    "Banque": (False, 0.0, "20 à 40 € (STRAT:508)"),
    "Conseil ponctuel (avocat, DPD)": (False, 1.0, "100 à 300 € (STRAT:508)"),
    "Divers (facturation électronique, domiciliation, téléphonie, petit matériel)": (False, 1.0,
        "[HY] ; plateforme de réception obligatoire depuis le 1er sept. 2026 [FV] (DROIT:297)"),
    "Imprévus": (False, 0.5, "[HY] marge pour les écarts des lignes précédentes"),
}
FRAIS_MONTANTS = {  # dans l'ordre de FRAIS_LIGNES ; totaux = 1 500 / 2 000 / 2 800 € (STRAT:504)
    "prudent":   [150, 300, 150, 300, 25, 150, 200, 225],
    "central":   [300, 500, 200, 350, 30, 200, 220, 200],
    "ambitieux": [500, 800, 250, 420, 40, 300, 240, 250],
}
FRAIS_FOURCHETTE = (0.80, 1.25)  # [HY] frais bas et hauts autour de la valeur centrale (cf. STRAT:359 : 1 500 à 2 500 €)

# Frais de démarrage, une fois (HT) [ES/HY] (STRAT:214, 509) : (libellé, montant, moment, part avec TVA)
# moment : "t0" = novembre 2026 (traitement de la fuite, avant l'échéance CNIL du 5 nov. au plus tard
# selon STRAT:32) ; "M1-1" = mois précédant le mois 1 ; "M1" = mois 1.
DEMARRAGE = {
    "prudent": [("Conseil sur la fuite de données (avocat ou DPD)", 1500, "t0", 1.0),
                ("Statuts et pacte (avocat)", 2500, "M1-1", 1.0),
                ("Formalités (greffe, annonce légale, bénéficiaires effectifs)", 300, "M1-1", 0.3),
                ("Mise en place (facturation électronique, coffre d'accès, matériel)", 200, "M1", 1.0)],
    "central": [("Conseil sur la fuite de données (avocat ou DPD)", 2000, "t0", 1.0),
                ("Statuts et pacte (avocat)", 3500, "M1-1", 1.0),
                ("Formalités (greffe, annonce légale, bénéficiaires effectifs)", 300, "M1-1", 0.3),
                ("Mise en place (facturation électronique, coffre d'accès, matériel)", 200, "M1", 1.0)],
    "ambitieux": [("Conseil sur la fuite de données (avocat ou DPD)", 2000, "t0", 1.0),
                  ("Statuts et pacte (avocat)", 4000, "M1-1", 1.0),
                  ("Formalités (greffe, annonce légale, bénéficiaires effectifs)", 300, "M1-1", 0.3),
                  ("Mise en place (facturation électronique, coffre d'accès, matériel)", 700, "M1", 1.0)],
}
DEMARRAGE_FOURCHETTE = {"prudent": (4000, 5000), "central": (5000, 7000), "ambitieux": (6000, 8000)}  # STRAT:509
APPORT = {"prudent": 8000, "central": 10000, "ambitieux": 13000}
                         # [HY] capital libéré et comptes courants, versés en novembre 2026 (caisse commune ;
                         # dépenses antérieures à l'immatriculation reprises par la société, DROIT:274-286)
                         # (STRAT:510 : 8 000 / 10 000 (8 000 à 14 000) / 12 000 à 14 000 €)

# =====================================================================================
# 6. SCÉNARIOS (STRAT:492-516)
# =====================================================================================
# t_m1 : indice du mois 1 (0 = novembre 2026) [HY] (STRAT:500) ; dispo et etp : disponibilités des associés [HY],
# non documentées par écrit (STRAT:495, 840) ; capacite : JP facturables par mois [ES] (STRAT:361-366, 482-483) ;
# plafond : capacité engagée au plus [PR] (STRAT:485) ; strategie : chiffres de la stratégie, cités pour
# comparaison [ES] (STRAT:511-515).
SCENARIOS = {
    "prudent": {
        "libelle": "Prudent", "t_m1": 3,   # mois 1 = février 2027 (STRAT:500)
        "dispo": "Morgan 50 %, Mathys 25 % ; Morgan garde ses autres projets",
        "etp": 0.75, "capacite": 7.0, "plafond": 7.0,
        "perimetre": "Cadrage (6 000 € HT, plancher) ; « socle + 1 projet » à 3 000 € HT par mois à partir du "
                     "mois 3 ; un lot de 4 500 € HT par trimestre. Variante basse : arrêt après le cadrage.",
        "strategie": {"ca12": 50000, "net": (650, 750), "treso": (11000, 12000)},
    },
    "central": {
        "libelle": "Central", "t_m1": 2,   # mois 1 = janvier 2027 (STRAT:500)
        "dispo": "Morgan 65 %, Mathys 50 % ; Morgan réduit fortement ses autres projets",
        "etp": 1.15, "capacite": 12.0, "plafond": 10.0,
        "perimetre": "Cadrage (6 500 € HT) ; pilote de 8 semaines (B0 à 3 500 € HT par mois et un lot de "
                     "6 000 € HT) ; à partir du mois 4, B1 à 4 500 € HT par mois et des lots pour ≈ 3 500 € HT "
                     "par mois en moyenne.",
        "strategie": {"ca12": 90000, "net": (1350, 1550), "treso": (25000, 25000)},
    },
    "ambitieux": {
        "libelle": "Ambitieux", "t_m1": 1,  # mois 1 = mi-décembre 2026 (STRAT:500)
        "dispo": "90 % chacun ; Morgan arrête l'essentiel du reste",
        "etp": 1.8, "capacite": 20.0, "plafond": 20.0,
        "perimetre": "Cadrage (6 500 € HT) ; pilote avec deux lots de 6 000 € HT ; à partir du mois 4, "
                     "« socle + 3 projets » à 5 700 € HT par mois et des lots pour ≈ 4 500 € HT par mois ; "
                     "exploitation D à 1 500 € HT par mois à partir du mois 7 ; second client à 2 500 € HT "
                     "par mois à partir du mois 6 ; sous-traitance de 3 JP par mois.",
        "strategie": {"ca12": 150000, "net": (2100, 2350), "treso": (34000, 34000)},
    },
}
ORDRE = ["prudent", "central", "ambitieux"]

# =====================================================================================
# 7. PARAMÈTRES DES TESTS DE RÉSISTANCE (STRAT:524-537) — scénario central, 18 mois
# =====================================================================================
STRESS = {
    "retards_mois": [1, 2, 3],          # [HY] 30, 60, 90 jours, durables, à partir du mois 4 (STRAT:528)
    "hausse_ia": (150, 1000),           # [HY] € par mois dès janvier 2027 (STRAT:532) ; doublements de prix annoncés
                                        # par un fournisseur au 1er déc. 2026 et au 1er janv. 2027 [FV] (VR6:33 ; R6:315-316)
    "depassement": 0.50,                # [HY] +50 % sur le lot du pilote (6 000 € HT, ≈ 6,7 JP) (STRAT:531)
    "provision_lot": (0.10, 0.15),      # [PR] provision de risque comprise dans le prix des lots (STRAT:287)
    "urgences_jp": 3.0,                 # [HY] 2 urgences de 1,5 JP dans le même mois (mois 6) (STRAT:534)
    "absence_mois": (5, 6),             # [HY] un associé absent ≈ 6 semaines (mois 5 et 6) (STRAT:533)
    "fournisseur_mois": 8,              # [HY] arrêt d'un fournisseur technique au mois 8, un mois de bascule (STRAT:535)
    "dgx_spark_ht": 6200,               # [ES] DGX Spark 128 Go ≈ 6 200 € HT (VR6:34 ; STRAT:645)
    "malus_socle": 0.05,                # [PR] malus de 5 % en avoir si deux engagements de service manqués (STRAT:279)
}

# Projets non financés (aucune recette, aucune dépense dans le modèle) [FV/DR] — pour mémoire
PROJETS_NON_FINANCES = [
    ("Option laboratoire IA et robotique", "30 000 € HT, dont 13 500 € d'honoraires Marwin et 16 500 € d'achats "
     f"au nom de l'entité du client [PR des archives] ({OFF}:21 ; {SYNP}:530)", f"Retirée ({STRAT}:411, 645)"),
    ("Option création avec Medhi (BOJ.ART), STRATES", f"≈ 10 000 € HT pour une première phase [PR des archives] ({OFF}:22)",
     f"Retirée le 4 nov. [DR] ({NOTE}:25 ; {STRAT}:31, 412) ; offre écrite non corrigée"),
    ("STRATES, Éclosion", f"aucun budget propre : les 323 875 € portent sur un ancien scénario de figurines ({SYNP}:511)",
     f"Gelés ({STRAT}:644)"),
    ("Vernissage « signature » avec bras robotisé", f"4 500 à 22 500 € HT d'honoraires selon le format [PR/ES] ({SYNP}:452)",
     f"Reporté sans date ({STRAT}:646)"),
    ("DGX Spark, IA locale", f"≈ 6 200 € HT (128 Go) [ES] ({VR6}:34)", f"Retiré ; achat par le client seulement ({STRAT}:645)"),
    ("Remise en ordre (offre 0)", f"9 à 17 JP non facturés sur les mois 0 à 2 [ES] ({STRAT}:196, 213)",
     "Interne ; ses sorties d'argent sont dans les frais de démarrage"),
]


# =====================================================================================
# 8. OUTILS DE CALCUL
# =====================================================================================
def impot_societes(benefice, mois_exercice=12):
    """IS 2026 : 15 % jusqu'à 42 500 € par période de 12 mois, 25 % au-delà [FV] (DROIT:142)."""
    if benefice <= 0:
        return 0.0
    seuil = IS_SEUIL * mois_exercice / 12.0
    return IS_TAUX_REDUIT * min(benefice, seuil) + IS_TAUX_NORMAL * max(0.0, benefice - seuil)


def _interp(x, x0, y0, x1, y1):
    if x <= x0:
        return y0
    if x >= x1:
        return y1
    return y0 + (y1 - y0) * (x - x0) / (x1 - x0)


def cotisations_tns(cout_total_annuel):
    """Cotisations TNS annuelles d'un gérant pour un coût total C (net + cotisations) [ES].
    Assiette = 74 % de C (abattement de 26 %) ; barème F38152 « revenus 2025 » (R1:37-43 ; VR1:20) ;
    taux maladie interpolé entre les seuils publiés ; minimum ≈ 1 255 € (R1:47)."""
    c = max(0.0, cout_total_annuel)
    a = (1 - TNS_ABATTEMENT) * c
    if a <= 9612:
        tm = 0.0
    elif a <= 52866:
        tm = _interp(a, 9612, 0.0, 52866, 0.065)
    elif a <= 96120:
        tm = _interp(a, 52866, 0.065, 96120, 0.077)
    elif a <= 144180:
        tm = _interp(a, 96120, 0.077, 144180, 0.085)
    else:
        tm = 0.085
    maladie = tm * a
    ij = 0.005 * min(a, 5 * PASS)
    retraite_base = 0.1787 * min(a, PASS) + 0.0072 * max(0.0, a - PASS)
    retraite_compl = 0.081 * min(a, PASS) + 0.091 * max(0.0, min(a, 4 * PASS) - PASS)
    invalidite = 0.013 * min(a, PASS)
    taf = 0.0 if a <= 52866 else (_interp(a, 52866, 0.0, 67284, 0.031) if a <= 67284 else 0.031)
    alloc = taf * a
    csg = 0.097 * a
    cfp = 120.0
    total = maladie + ij + retraite_base + retraite_compl + invalidite + alloc + csg + cfp
    return max(total, TNS_MINIMUM)


def r100(x):
    """Arrondi à la centaine d'euros, symétrique pour les montants négatifs."""
    s = -1 if x < 0 else 1
    return s * math.floor(abs(x) / 100.0 + 0.5) * 100


def arrondis_cumules(valeurs):
    """Arrondit une série de flux mensuels à la centaine en reportant l'arrondi d'un mois sur l'autre :
    la somme des valeurs arrondies est égale au total arrondi (les totaux de colonne restent justes)."""
    out, prec, cum = [], 0, 0.0
    for v in valeurs:
        cum += v
        rc = r100(cum)
        out.append(rc - prec)
        prec = rc
    return out


def eur(x):
    """Montant arrondi à la centaine, au format français (espaces insécables)."""
    v = int(r100(x))
    txt = f"{abs(v):,}".replace(",", " ")
    return ("−" if v < 0 else "") + txt + " €"


def eur10(x):
    """Prix unitaire (par JP) arrondi à la dizaine d'euros : l'arrondi à la centaine effaçait les écarts
    entre scénarios (871 à 874 € affichés « 900 € ») (contrôle du 4 nov. 2026)."""
    v = int(math.floor(x / 10.0 + 0.5) * 10)
    return f"{v:,}".replace(",", " ") + " €"


def texte_decalage_tva():
    return {0: "le mois même", 1: "le mois suivant"}.get(TVA_DECALAGE, f"{TVA_DECALAGE} mois plus tard")


def eur_plage(a, b):
    lo, hi = sorted((r100(a), r100(b)))
    if lo == hi:
        return "≈ " + eur(lo)
    return f"{eur(lo).replace(chr(160) + '€', '')} à {eur(hi)}"


def eur_cite(a, b=None):
    """Montant cité tel quel d'une autre pièce (aucun arrondi)."""
    f = lambda v: f"{int(v):,}".replace(",", "\u00a0")
    if b is None or a == b:
        return "≈\u00a0" + f(a) + "\u00a0€"
    return f"{f(a)} à {f(b)}\u00a0€"


def pct(x, dec=0):
    return f"{x * 100:.{dec}f}".replace(".", ",") + " %"


def num(x, dec=1):
    return f"{x:.{dec}f}".replace(".", ",")


def table(entetes, lignes):
    out = ["| " + " | ".join(entetes) + " |", "| " + " | ".join(["---"] * len(entetes)) + " |"]
    for l in lignes:
        out.append("| " + " | ".join(str(c) for c in l) + " |")
    return "\n".join(out)


# =====================================================================================
# 9. CONSTRUCTION DES PLANS MENSUELS
# =====================================================================================
@dataclass
class Ligne:
    libelle: str
    categorie: str        # cadrage, pilote, socle, lots, exploitation, autre_client, avenant, avoir
    client: str           # "GianLuca" ou "autre"
    t_facture: int
    t_encaisse: int
    ht: float
    proba: float = 1.0    # probabilité cumulée [HY], conditionnelle à la vente du cadrage


@dataclass
class Plan:
    nom: str
    t_m1: int
    lignes: list = field(default_factory=list)
    jp: list = field(default_factory=lambda: [0.0] * N_SIM)      # JP vendues réalisées par les associés
    jp_st: list = field(default_factory=lambda: [0.0] * N_SIM)   # JP sous-traitées
    frais: list = field(default_factory=lambda: [dict() for _ in range(N_SIM)])  # {ligne: HT}
    st_ht: list = field(default_factory=lambda: [0.0] * N_SIM)   # coût HT de la sous-traitance
    extra: list = field(default_factory=lambda: [[] for _ in range(N_SIM)])  # (libellé, HT, part TVA)
    demarrage: list = field(default_factory=list)                 # (t, libellé, HT, part TVA)
    apport: list = field(default_factory=lambda: [0.0] * N_SIM)
    remu_masque: list = field(default_factory=lambda: [0.0] * N_SIM)  # 1 = enveloppe versée ce mois

    def tm(self, m):
        """Indice calendaire du mois de contrat m (m = 1 pour le mois 1)."""
        return self.t_m1 + m - 1

    def ajouter(self, libelle, cat, t_fact, t_enc, ht, proba=1.0, client="GianLuca"):
        if 0 <= t_fact < N_SIM:
            self.lignes.append(Ligne(libelle, cat, client, t_fact, t_enc, ht, proba))

    def jp_ajouter(self, t, x, sous_traite=False):
        if 0 <= t < N_SIM:
            (self.jp_st if sous_traite else self.jp)[t] += x


def _frais_et_demarrage(plan, nom, frais_mult, dem_mult):
    noms = list(FRAIS_LIGNES)
    for t in range(plan.t_m1, N_SIM):
        plan.frais[t] = {n: m * frais_mult for n, m in zip(noms, FRAIS_MONTANTS[nom])}
    for lib, ht, moment, part in DEMARRAGE[nom]:
        t = {"t0": 0, "M1-1": max(0, plan.t_m1 - 1), "M1": plan.t_m1}[moment]
        plan.demarrage.append((t, lib, ht * dem_mult, part))
    plan.apport[0] = APPORT[nom]
    for t in range(plan.tm(MOIS_DEBUT_REMU), N_SIM):
        plan.remu_masque[t] = 1.0


def _cadrage(plan, prix, proba=1.0):
    t1 = plan.tm(1)
    plan.ajouter("Cadrage : acompte de 50 %", "cadrage", t1, t1, prix / 2, proba)
    plan.ajouter("Cadrage : solde de 50 % à la réception", "cadrage", t1 + 1, t1 + 1, prix / 2, proba)
    plan.jp_ajouter(t1, JP["cadrage"][0])
    plan.jp_ajouter(t1 + 1, JP["cadrage"][1])


def _mensuel(plan, libelle, cat, m_debut, m_fin, prix, jp, proba_fn, client="GianLuca"):
    for m in range(m_debut, m_fin + 1):
        t = plan.tm(m)
        plan.ajouter(libelle, cat, t, t, prix, proba_fn(m), client)   # payé d'avance, encaissé le mois même
        plan.jp_ajouter(t, jp)


def _lot(plan, libelle, m_cmd, prix, mois_solde, proba, cat="lots", mois_travail=2):
    """Lot au forfait : 40 % à la commande, 60 % à la livraison (STRAT:287, 442). Le travail s'étale sur
    `mois_travail` mois (6 à 8 semaines) ; le solde est encaissé `mois_solde` mois après la commande [HY]."""
    t = plan.tm(m_cmd)
    plan.ajouter(libelle + " : acompte de 40 %", cat, t, t, 0.4 * prix, proba)
    plan.ajouter(libelle + " : solde de 60 %", cat, t + mois_solde, t + mois_solde, 0.6 * prix, proba)
    jp_total = prix / PRIX_PAR_JP_LOT
    for k in range(mois_travail):
        plan.jp_ajouter(t + k, jp_total / mois_travail)


def _tranches_lots(plan, m_debut, m_fin, prix_mois, proba_fn):
    """Lots en régime modélisés par tranches mensuelles : chaque mois, des lots pour `prix_mois` HT sont
    commandés ; 40 % encaissés à la commande, 60 % à la livraison le mois suivant [HY] ; JP = prix / 900."""
    for m in range(m_debut, m_fin + 1):
        t = plan.tm(m)
        p = proba_fn(m)
        plan.ajouter("Lots devisés : acomptes de 40 %", "lots", t, t, 0.4 * prix_mois, p)
        plan.ajouter("Lots devisés : soldes de 60 %", "lots", t + 1, t + 1, 0.6 * prix_mois, p)
        plan.jp_ajouter(t, prix_mois / PRIX_PAR_JP_LOT)


def construire_plan(nom, frais_mult=1.0, dem_mult=1.0, variante=None, decalage_m1=0, facteur_lots=1.0):
    """Construit le plan mensuel d'un scénario. variante : None, "basse" (prudent arrêté après le cadrage)
    ou "second_client" (variante centrale de STRAT:522)."""
    sc = SCENARIOS[nom]
    plan = Plan(nom=nom, t_m1=sc["t_m1"] + decalage_m1)
    _frais_et_demarrage(plan, nom, frais_mult, dem_mult)
    fin = N_SIM  # les prestations récurrentes courent jusqu'à la fin de la simulation (renouvellements supposés)

    if nom == "prudent":
        pr = PROBA["prudent"]
        _cadrage(plan, PRIX["cadrage_plancher"])
        if variante == "basse":
            return plan
        def p_socle(m):  # trimestres du socle léger : mois 3-5, 6-8, 9-11, ...
            q = (m - 3) // 3
            return pr["suite"] * pr["renouvellement"] ** q
        _mensuel(plan, "Socle léger (socle + 1 projet)", "socle", 3, fin, PRIX["socle_leger"], JP["socle_leger"], p_socle)
        for m in range(4, fin, 3):
            _lot(plan, f"Lot trimestriel (commande au mois {m})", m, PRIX["lot_prudent"] * facteur_lots, 1, p_socle(m))
        return plan

    if nom == "central":
        pr = PROBA["central"]
        _cadrage(plan, PRIX["cadrage"])
        p_pil = pr["pilote"]
        _mensuel(plan, "Socle pilote B0", "pilote", 2, 3, PRIX["b0"], JP["b0"], lambda m: p_pil)
        _lot(plan, "Lot du pilote", 2, PRIX["lot_pilote"], 1, p_pil, cat="pilote")
        def p_socle(m):  # trimestres du socle B1 : mois 4-6, 7-9, ...
            q = (m - 4) // 3
            return p_pil * pr["socle"] * pr["renouvellement"] ** q
        _mensuel(plan, "Socle B1 (socle + 2 projets)", "socle", 4, fin, PRIX["b1"], JP["b1"], p_socle)
        if variante == "second_client":
            _tranches_lots(plan, 4, 6, PRIX["lots_mois_central"], p_socle)
            _tranches_lots(plan, 7, fin, PRIX["lots_mois_variante"], p_socle)
            _mensuel(plan, "Second client", "autre_client", 7, fin, PRIX["second_client_var"],
                     JP["second_client_var"], lambda m: pr["second_client"], client="autre")
        else:
            _tranches_lots(plan, 4, fin, PRIX["lots_mois_central"] * facteur_lots, p_socle)
        return plan

    if nom == "ambitieux":
        pr = PROBA["ambitieux"]
        _cadrage(plan, PRIX["cadrage"])
        p_pil = pr["pilote"]
        _mensuel(plan, "Socle pilote B0", "pilote", 2, 3, PRIX["b0"], JP["b0"], lambda m: p_pil)
        _lot(plan, "Premier lot du pilote", 2, PRIX["lot_pilote"], 1, p_pil, cat="pilote")
        _lot(plan, "Second lot du pilote", 2, PRIX["lot_pilote"], 1, p_pil, cat="pilote")
        def p_socle(m):
            q = (m - 4) // 3
            return p_pil * pr["socle"] * pr["renouvellement"] ** q
        _mensuel(plan, "Socle + 3 projets", "socle", 4, fin, PRIX["socle_3"], JP["socle_3"], p_socle)
        _tranches_lots(plan, 4, fin, PRIX["lots_mois_ambitieux"] * facteur_lots, p_socle)
        _mensuel(plan, "Exploitation D (minimum)", "exploitation", 7, fin, PRIX["exploitation"], JP["exploitation"], p_socle)
        _mensuel(plan, "Second client", "autre_client", 6, fin, PRIX["second_client_amb"], JP["second_client_amb"],
                 lambda m: pr["second_client"], client="autre")
        for m in range(4, fin):  # sous-traitance de 3 JP par mois sur des lots délimités
            t = plan.tm(m)
            if t < N_SIM:
                plan.st_ht[t] = SOUS_TRAITANCE["jp"] * SOUS_TRAITANCE["prix_jp"]
                plan.jp_st[t] += SOUS_TRAITANCE["jp"]
                plan.jp[t] -= SOUS_TRAITANCE["jp"]   # ces JP vendues sont réalisées par le sous-traitant
        return plan
    raise ValueError(nom)


# =====================================================================================
# 10. SIMULATION MENSUELLE
# =====================================================================================
def simuler(plan, enveloppe):
    """Simule mois par mois. `enveloppe` = coût total mensuel des rémunérations (deux associés).
    Renvoie un dictionnaire de séries (non arrondies)."""
    n = N_SIM
    S = {k: [0.0] * n for k in (
        "fact_ht", "enc_ht", "enc_ht_gl", "enc_ht_autre", "enc_ttc", "tva_coll", "enc_pond_ttc",
        "frais_ht", "frais_direct_ht", "frais_ttc", "dem_ht", "dem_ttc", "st_ht", "st_ttc",
        "extra_ht", "extra_ttc", "tva_ded", "remu", "tva_versee", "is_paye", "apport",
        "flux", "cash", "tva_due", "credit_tva", "disponible", "reserve", "is_prov", "libre",
        "resultat", "jp", "jp_st")}
    for c in ("cadrage", "pilote", "socle", "lots", "exploitation", "autre_client", "avenant", "avoir"):
        S["enc_ttc_" + c] = [0.0] * n
    cash = credit = reserve = 0.0
    # TVA nette calculée au mois t, reversée au mois t + TVA_DECALAGE (contrôle du 4 nov. : le paramètre
    # TVA_DECALAGE n'était pas utilisé, le décalage d'un mois était écrit en dur)
    nette_due = [0.0] * n
    res_ex = {1: 0.0, 2: 0.0}
    is_ex1_paye = False
    for t in range(n):
        lf = [l for l in plan.lignes if l.t_facture == t]
        le = [l for l in plan.lignes if l.t_encaisse == t]
        S["fact_ht"][t] = sum(l.ht for l in lf)
        S["enc_ht"][t] = sum(l.ht for l in le)
        S["enc_ht_gl"][t] = sum(l.ht for l in le if l.client == "GianLuca")
        S["enc_ht_autre"][t] = sum(l.ht for l in le if l.client != "GianLuca")
        S["enc_ttc"][t] = S["enc_ht"][t] * (1 + TVA)
        S["tva_coll"][t] = S["enc_ht"][t] * TVA
        S["enc_pond_ttc"][t] = sum(l.ht * l.proba for l in le) * (1 + TVA)
        for l in le:
            S["enc_ttc_" + l.categorie][t] += l.ht * (1 + TVA)
        # Frais fixes
        fh = sum(plan.frais[t].values())
        fd = sum(v for k, v in plan.frais[t].items() if FRAIS_LIGNES[k][0])
        ftva = sum(v * FRAIS_LIGNES[k][1] * TVA for k, v in plan.frais[t].items())
        S["frais_ht"][t], S["frais_direct_ht"][t], S["frais_ttc"][t] = fh, fd, fh + ftva
        # Démarrage
        dh = sum(x[2] for x in plan.demarrage if x[0] == t)
        dtva = sum(x[2] * x[3] * TVA for x in plan.demarrage if x[0] == t)
        S["dem_ht"][t], S["dem_ttc"][t] = dh, dh + dtva
        # Sous-traitance (facturée avec TVA récupérable [HY])
        S["st_ht"][t] = plan.st_ht[t]
        S["st_ttc"][t] = plan.st_ht[t] * (1 + TVA)
        # Charges exceptionnelles des tests
        eh = sum(x[1] for x in plan.extra[t])
        etva = sum(x[1] * x[2] * TVA for x in plan.extra[t])
        S["extra_ht"][t], S["extra_ttc"][t] = eh, eh + etva
        S["tva_ded"][t] = ftva + dtva + plan.st_ht[t] * TVA + etva
        # Rémunérations (coût total pour la société ; cotisations versées le mois même, hypothèse prudente)
        S["remu"][t] = enveloppe * plan.remu_masque[t]
        # TVA : la TVA nette du mois (après imputation du crédit) est reversée TVA_DECALAGE mois plus tard
        nette = S["tva_coll"][t] - S["tva_ded"][t] - credit
        if nette >= 0:
            nette_due[t], credit = nette, 0.0
        else:
            nette_due[t], credit = 0.0, -nette
        S["tva_versee"][t] = nette_due[t - TVA_DECALAGE] if t >= TVA_DECALAGE else 0.0
        a_payer = sum(nette_due[max(0, t - TVA_DECALAGE + 1): t + 1])   # TVA calculée, pas encore reversée
        # IS du premier exercice payé en mai 2028
        ex = 1 if t <= T_DEC_2027 else 2
        res_ex[ex] += (S["fact_ht"][t] - fh - dh - plan.st_ht[t] - eh - S["remu"][t])
        S["resultat"][t] = res_ex[ex]
        if t == T_PAIEMENT_IS_EX1:
            S["is_paye"][t] = impot_societes(res_ex[1])
            is_ex1_paye = True
        S["apport"][t] = plan.apport[t]
        flux = (plan.apport[t] + S["enc_ttc"][t] - S["frais_ttc"][t] - S["dem_ttc"][t] - S["st_ttc"][t]
                - S["extra_ttc"][t] - S["remu"][t] - S["tva_versee"][t] - S["is_paye"][t])
        cash += flux
        reserve += RESERVE * S["enc_ht"][t]
        S["flux"][t], S["cash"][t] = flux, cash
        S["tva_due"][t], S["credit_tva"][t] = a_payer, credit
        S["disponible"][t] = cash - a_payer
        S["reserve"][t] = reserve
        S["is_prov"][t] = (0.0 if is_ex1_paye else impot_societes(res_ex[1])) + (impot_societes(res_ex[2]) if ex == 2 else 0.0)
        S["libre"][t] = S["disponible"][t] - reserve - S["is_prov"][t]
        S["jp"][t], S["jp_st"][t] = plan.jp[t], plan.jp_st[t]
    return S


def fenetre(plan, debut_m=1, fin_m=12):
    return range(plan.tm(debut_m), plan.tm(fin_m) + 1)


def resoudre_enveloppe(plan, plafond=None):
    """Enveloppe mensuelle E (coût total, deux associés) versée à partir du mois 4 : la plus grande telle que
    les encaissements HT des mois 4 à 12 couvrent frais, sous-traitance, réserve, IS de la période et E."""
    s0 = simuler(plan, 0.0)
    f4 = fenetre(plan, MOIS_DEBUT_REMU, 12)
    disponible = sum(s0["enc_ht"][t] * (1 - RESERVE) - s0["frais_ht"][t] - s0["st_ht"][t] - s0["extra_ht"][t] for t in f4)
    nb = sum(plan.remu_masque[t] for t in f4)
    t12 = plan.tm(12)
    base_res = sum(s0["fact_ht"][t] - s0["frais_ht"][t] - s0["dem_ht"][t] - s0["st_ht"][t] - s0["extra_ht"][t]
                   for t in range(0, t12 + 1))
    if nb == 0 or disponible <= impot_societes(base_res):
        return 0.0
    lo, hi = 0.0, disponible / nb
    for _ in range(80):
        mid = (lo + hi) / 2
        if nb * mid + impot_societes(base_res - nb * mid) <= disponible:
            lo = mid
        else:
            hi = mid
    if plafond is None:
        plafond = 2 * NET_PLAFOND_ASSOCIE * COEF_SAS["central"]
    return min(lo, plafond)


# =====================================================================================
# 11. INDICATEURS SUR 12 MOIS
# =====================================================================================
def indicateurs_12_mois(plan, E, s=None):
    s = s or simuler(plan, E)
    t12 = plan.tm(12)
    f = fenetre(plan)
    av = range(0, t12 + 1)                      # novembre 2026 -> fin du mois 12 (période préalable comprise)
    fr = fenetre(plan, MOIS_DEBUT_REMU, 12)
    I = {}
    I["fact_ht"] = sum(s["fact_ht"][t] for t in f)
    I["enc_ht"] = sum(s["enc_ht"][t] for t in f)
    I["enc_ht_autre"] = sum(s["enc_ht_autre"][t] for t in f)
    I["part_gl"] = 1 - I["enc_ht_autre"] / I["enc_ht"] if I["enc_ht"] else 1.0
    t_last = plan.tm(12)
    I["part_gl_m12"] = s["enc_ht_gl"][t_last] / s["enc_ht"][t_last] if s["enc_ht"][t_last] else 1.0
    I["enc_pond_ht"] = sum(s["enc_pond_ttc"][t] for t in f) / (1 + TVA)
    I["tva_coll"] = sum(s["tva_coll"][t] for t in av)
    I["tva_ded"] = sum(s["tva_ded"][t] for t in av)
    I["tva_versee"] = sum(s["tva_versee"][t] for t in av)
    I["tva_due"] = s["tva_due"][t12]
    I["credit_tva"] = s["credit_tva"][t12]
    I["frais_direct"] = sum(s["frais_direct_ht"][t] for t in av)
    I["frais_generaux"] = sum(s["frais_ht"][t] - s["frais_direct_ht"][t] for t in av)
    I["st"] = sum(s["st_ht"][t] for t in av)
    I["demarrage"] = sum(s["dem_ht"][t] for t in av)
    I["extra"] = sum(s["extra_ht"][t] for t in av)
    I["remu"] = sum(s["remu"][t] for t in av)
    I["resultat"] = I["fact_ht"] - I["frais_direct"] - I["frais_generaux"] - I["st"] - I["demarrage"] - I["extra"] - I["remu"]
    I["is"] = impot_societes(I["resultat"])
    I["resultat_net"] = I["resultat"] - I["is"]
    I["cash"] = s["cash"][t12]
    I["disponible"] = s["disponible"][t12]
    I["reserve"] = s["reserve"][t12]
    I["libre"] = I["disponible"] - I["reserve"] - I["is"]
    I["point_bas"] = min(s["disponible"][t] for t in av)
    I["t_point_bas"] = min(av, key=lambda t: s["disponible"][t])
    I["jp_regime"] = sum(s["jp"][t] + s["jp_st"][t] for t in fr) / len(fr)
    I["jp_assoc_regime"] = sum(s["jp"][t] for t in fr) / len(fr)
    I["jp_max"] = max(s["jp"][t] for t in f)
    I["valeur_regime"] = sum(s["fact_ht"][t] for t in fr)
    I["jp_regime_total"] = sum(s["jp"][t] + s["jp_st"][t] for t in fr)
    I["prix_jp"] = I["valeur_regime"] / I["jp_regime_total"] if I["jp_regime_total"] else 0.0
    I["frais_mensuels"] = sum(s["frais_ht"][t] for t in fr) / len(fr)
    I["st_mensuel"] = sum(s["st_ht"][t] for t in fr) / len(fr)
    I["nb_mois_remu"] = sum(plan.remu_masque[t] for t in fr)
    I["objectif_reserve"] = OBJECTIF_RESERVE_MOIS_FRAIS * I["frais_mensuels"] + OBJECTIF_RESERVE_MOIS_REMU * E
    I["E"] = E
    return I, s


def seuils_jp(I, E, etp):
    """Seuil de rentabilité en JP vendues par mois (associés et sous-traitance), IS négligé
    (il ne porterait que sur la réserve). Prix moyen et coûts du régime (mois 4 à 12)."""
    p = I["prix_jp"]
    v = (I["st_mensuel"] / I["jp_regime"]) if I["jp_regime"] else 0.0   # coût variable de sous-traitance par JP vendue
    marge_jp = p * (1 - RESERVE) - v
    F = I["frais_mensuels"]
    res = {"frais": F / marge_jp, "remu": (F + E) / marge_jp}
    # plancher : 2 500 € nets par ETP engagé (etp ETP au total), au coefficient bas et haut
    res["plancher"] = tuple((F + NET_PLAFOND_ASSOCIE * etp * k) / marge_jp for k in (COEF_SAS["bas"], COEF_SAS["haut"]))
    return res


def nets_par_associe(E, nb_mois):
    """Nets par associé sur la période (avant IR), SAS et SARL, pour une même enveloppe E."""
    C = E / 2 * nb_mois                                 # coût total annuel par associé
    out = {"C": C}
    out["sas"] = {k: C / v for k, v in COEF_SAS.items()}
    out["sas_brut"] = {k: C / v / NET_SUR_BRUT_SAS for k, v in COEF_SAS.items()}
    cot = cotisations_tns(C)
    out["sarl_cotis"] = cot
    out["sarl_net"] = C - cot
    out["sarl_regul"] = cot - TNS_FORFAIT_DEBUT        # > 0 : à payer en année 2 ; < 0 : remboursement [ES]
    return out


# =====================================================================================
# 12. ÉCRITURE : scenarios.md
# =====================================================================================
ENTETE_COMMUN = (
    "**Document interne.** Il contient des coûts, des marges, des rémunérations visées et des probabilités : "
    f"il ne doit pas être transmis à GianLuca Carlone ({STRAT}:787-789).\n\n"
    "Produit le 4 novembre 2026 par `modele_financier.py` (même dossier), qui contient tous les paramètres, leur "
    "code et leur source. Pour changer une hypothèse, modifier le paramètre en tête du script et le relancer. "
    "« audit-work/ » désigne le dossier de travail de l'audit (hors dépôt) ; les autres chemins renvoient au dépôt "
    "(commit 7b46602).\n\n"
    "Codes : [FV] fait vérifié ; [DR] déclaration rapportée ; [PR] proposition ; [HY] hypothèse ; [ES] estimation ou "
    "simulation ; [MM] mesure ; [IN] inconnu. **Tous les résultats chiffrés sont des [ES]**, arrondis à la centaine "
    "d'euros (à la dizaine pour les prix par JP) : un total peut différer de 100 à 200 € de la somme de ses lignes arrondies. Les fourchettes combinent "
    "frais bas et coefficient social bas, puis frais hauts et coefficient haut.\n\n"
    "**Impôt sur le revenu non calculé** : les situations fiscales des foyers de Morgan Olsen et de Mathys Couet sont "
    f"[IN] ({R1}:15 ; {DROIT}:93). Tous les nets sont « avant impôt sur le revenu ».\n"
)

FAITS_NOUVEAUX = (
    "**Trois faits pris comme base** ({s}:29-33) :\n"
    "1. **Aucun contrat, aucune facture, aucune entité payeuse identifiée** [FV négatif]. Le « contrat certain » vaut "
    "donc **0 €** dans tous les scénarios : chaque euro de chiffre d'affaires ci-dessous est une hypothèse.\n"
    "2. **Medhi et BOJ.ART retirés de l'offre** le 4 nov. 2026 à la demande de Morgan [DR] ({n}:25). Seul le diaporama "
    "client a été corrigé (11 diapositives) ; l'offre écrite, STRATES v1.1, le vernissage et le PDF de 13 diapositives "
    "de la PR n° 1 ne l'ont pas été [FV] ({s}:31). Le modèle ne compte **aucune recette ni dépense** pour STRATES, la "
    "création, le laboratoire ou le vernissage « signature ».\n"
    "3. **Fuite de données très probable** (dépôt public FinanceScope/CRM-Carlone) ; délai CNIL de 72 h possiblement "
    "échu le 5 nov. si la connaissance date du 2 nov. [ES] ({s}:32). Le modèle compte le conseil (avocat ou DPD) "
    "dans les frais de démarrage de novembre 2026 [HY] ; une sanction, une action des personnes ou un refus "
    "d'assurance ne sont **pas chiffrés** [IN]. Rien ne démarre tant que la fuite n'est pas traitée ({s}:53, 660).\n"
).format(s=STRAT, n=NOTE)


def ecrire_scenarios(dossier, R):
    L = []
    L.append("# Modèle financier : trois scénarios sur douze mois\n")
    L.append(ENTETE_COMMUN)
    L.append("\n" + FAITS_NOUVEAUX)

    P, C, A = (R[n]["I"] for n in ORDRE)
    nC = R["central"]["nets"]
    L.append("\n## 0. L'essentiel\n")
    L.append(
        f"- **Chiffre d'affaires facturé sur les mois 1 à 12** [ES] : {eur(P['fact_ht'])} HT (prudent), "
        f"{eur(C['fact_ht'])} HT (central), {eur(A['fact_ht'])} HT (ambitieux, dont {eur(A['enc_ht_autre'])} "
        "encaissés d'un second client). Pondéré par les probabilités de passage, et à condition que le cadrage soit "
        f"vendu, le central ne vaut plus que {eur(C['enc_pond_ht'])} HT encaissés.\n"
        f"- **Rémunération soutenable à partir du mois 4**, en SAS, avant IR : ≈ {eur(R['prudent']['net_central'])} "
        f"({eur_plage(*R['prudent']['net_plage'])}) nets par associé et par mois en prudent, "
        f"≈ {eur(R['central']['net_central'])} ({eur_plage(*R['central']['net_plage'])}) en central, "
        f"≈ {eur(R['ambitieux']['net_central'])} ({eur_plage(*R['ambitieux']['net_plage'])}) en ambitieux. Le central "
        f"est inférieur d'environ {eur(sum(SCENARIOS['central']['strategie']['net']) / 2 - R['central']['net_central'])} "
        f"au milieu de la fourchette de la stratégie (1 350 à 1 550 €, {STRAT}:511), qui ne comptait ni l'IS ni les "
        f"délais d'encaissement ({STRAT}:518).\n"
        f"- **Même enveloppe en SARL** (deux cogérants TNS) : {eur(R['central']['nets']['sarl_net'] / R['central']['I']['nb_mois_remu'])} "
        f"nets par associé et par mois en central, soit {eur(nC['sarl_net'] - nC['sas']['central'])} de plus sur les neuf "
        "mois rémunérés qu'en SAS (coefficient central), contre une protection sociale moindre et des cotisations dues même sans "
        "rémunération (voir `structures.md`).\n"
        f"- **Trésorerie disponible à la fin du mois 12** (apport compris, TVA due déduite) : {eur(P['disponible'])} "
        f"(prudent), {eur(C['disponible'])} (central), {eur(A['disponible'])} (ambitieux). Une fois la réserve et l'IS "
        f"mis de côté, il reste {eur(P['libre'])}, {eur(C['libre'])} et {eur(A['libre'])}.\n"
        f"- **Seuil de rentabilité** (frais couverts, réserve comprise, sans rémunération) : "
        f"{num(R['prudent']['seuils']['frais'])} JP vendues par mois (prudent), {num(R['central']['seuils']['frais'])} "
        f"(central), {num(R['ambitieux']['seuils']['frais'])} (ambitieux). Pour payer **2 500 € nets par ETP engagé** "
        f"(soit {eur(NET_PLAFOND_ASSOCIE * SCENARIOS['central']['etp'])} nets à deux en central), il faudrait "
        f"{num(R['central']['seuils']['plancher'][0])} à {num(R['central']['seuils']['plancher'][1])} JP vendues par mois "
        f"en régime, pour {num(C['jp_regime'])} prévues et un plafond de 10 : "
        + ("hors d'atteinte" if R['central']['seuils']['plancher'][0] > SCENARIOS['central']['plafond']
           else "à la limite en régime" if R['central']['seuils']['plancher'][1] > C['jp_regime'] else "atteignable en régime")
        + f". Sur l'année, il n'est pas atteint, puisque rien n'est versé avant le mois 4 ({STRAT}:511).\n"
        "- **La TVA n'est jamais du chiffre d'affaires** : elle est collectée à l'encaissement et reversée "
        f"{texte_decalage_tva()} ; de novembre 2026 au mois 12, le central collecte {eur(C['tva_coll'])} de TVA, en déduit "
        f"{eur(C['tva_ded'])} sur ses achats, en reverse {eur(C['tva_versee'])} et en doit encore {eur(C['tva_due'])}.\n"
    )

    # ---- Synthèse
    L.append("\n## 1. Tableau de synthèse (douze mois de contrat, période préalable comprise)\n")
    L.append("Lecture : une valeur seule est la valeur centrale ; une plage est la fourchette « frais hauts et "
             "coefficient 1,9 » à « frais bas et coefficient 1,7 ». Les coûts et la trésorerie couvrent la période "
             "de novembre 2026 à la fin du mois 12 ; le chiffre d'affaires couvre les mois 1 à 12.\n")
    rows = []
    def ligne(lib, f, plage=None):
        rows.append([lib] + [f(n) for n in ORDRE])
    sc = SCENARIOS
    ligne("Mois 1 [HY]", lambda n: MOIS[sc[n]["t_m1"]])
    ligne("Mois 12", lambda n: MOIS[sc[n]["t_m1"] + 11])
    ligne("Disponibilité des associés [HY]", lambda n: sc[n]["dispo"])
    ligne("Capacité facturable (JP par mois) [ES]", lambda n: num(sc[n]["capacite"], 0) + (" (plafond engagé 10)" if n == "central" else ""))
    ligne("JP vendues par mois, mois 4 à 12 (moyenne) [ES]", lambda n: num(R[n]["I"]["jp_regime"]) +
          (f" dont {num(R[n]['I']['jp_regime'] - R[n]['I']['jp_assoc_regime'])} sous-traitées" if R[n]["I"]["jp_regime"] != R[n]["I"]["jp_assoc_regime"] else ""))
    ligne("JP réalisées par les associés, mois le plus chargé", lambda n: num(R[n]["I"]["jp_max"]))
    ligne("Occupation de la capacité facturable (mois 4 à 12)", lambda n: pct(R[n]["I"]["jp_assoc_regime"] / sc[n]["capacite"]))
    ligne("**CA facturé HT, mois 1 à 12**", lambda n: "**" + eur(R[n]["I"]["fact_ht"]) + "**")
    ligne("CA encaissé HT, mois 1 à 12", lambda n: eur(R[n]["I"]["enc_ht"]))
    ligne("dont hors GianLuca Carlone", lambda n: eur(R[n]["I"]["enc_ht_autre"]))
    ligne("Part de GianLuca Carlone (12 mois ; mois 12)", lambda n: f"{pct(R[n]['I']['part_gl'])} ; {pct(R[n]['I']['part_gl_m12'])}")
    ligne("CA encaissé pondéré par les probabilités [ES], si le cadrage est vendu", lambda n: eur(R[n]["I"]["enc_pond_ht"]))
    ligne("Contrat certain", lambda n: "0 €")
    ligne("TVA collectée (à l'encaissement)", lambda n: eur(R[n]["I"]["tva_coll"]))
    ligne("TVA déductible (frais, démarrage, sous-traitance)", lambda n: eur(R[n]["I"]["tva_ded"]))
    ligne("TVA reversée au Trésor", lambda n: eur(R[n]["I"]["tva_versee"]))
    ligne(f"TVA restant due fin du mois 12 (reversée {texte_decalage_tva()})", lambda n: eur(R[n]["I"]["tva_due"]))
    ligne("Coûts directs HT (outils et IA, déplacements)", lambda n: eur_plage(R[n]["Ih"]["frais_direct"], R[n]["Ib"]["frais_direct"]))
    ligne("Sous-traitance HT", lambda n: eur(R[n]["I"]["st"]))
    ligne("Frais généraux HT (assurances, comptable, banque, conseil, divers)", lambda n: eur_plage(R[n]["Ih"]["frais_generaux"], R[n]["Ib"]["frais_generaux"]))
    ligne("Frais de démarrage HT (une fois)", lambda n: eur_plage(R[n]["Ih"]["demarrage"], R[n]["Ib"]["demarrage"]))
    ligne("Rémunérations, coût total pour la société", lambda n: eur_plage(R[n]["Ih"]["remu"], R[n]["Ib"]["remu"]))
    ligne("Résultat avant IS", lambda n: eur_plage(R[n]["Ih"]["resultat"], R[n]["Ib"]["resultat"]))
    ligne("IS (15 % jusqu'à 42 500 €) [FV pour le taux]", lambda n: eur_plage(R[n]["Ih"]["is"], R[n]["Ib"]["is"]))
    ligne("Résultat net", lambda n: eur_plage(R[n]["Ih"]["resultat_net"], R[n]["Ib"]["resultat_net"]))
    ligne("Apport des associés [HY]", lambda n: eur(APPORT[n]))
    ligne("Trésorerie en banque fin du mois 12", lambda n: eur_plage(R[n]["Ih"]["cash"], R[n]["Ib"]["cash"]))
    ligne("Trésorerie disponible (TVA due déduite)", lambda n: eur_plage(R[n]["Ih"]["disponible"], R[n]["Ib"]["disponible"]))
    ligne("dont réserve (10 % du CA encaissé)", lambda n: eur(R[n]["I"]["reserve"]))
    ligne("dont IS à payer après la clôture", lambda n: eur_plage(R[n]["Ih"]["is"], R[n]["Ib"]["is"]))
    ligne("Trésorerie libre (après réserve et IS)", lambda n: eur_plage(R[n]["Ih"]["libre"], R[n]["Ib"]["libre"]))
    ligne("Point bas de la trésorerie disponible (mois)", lambda n: f"{eur(R[n]['I']['point_bas'])} ({MOIS[R[n]['I']['t_point_bas']]})")
    def _objectif(n):
        I = R[n]["I"]
        o = I["objectif_reserve"]
        a = "atteint" if I["reserve"] >= o else "**non atteint**"
        b = "atteint" if I["disponible"] - I["is"] >= o else "**non atteint**"
        return (f"{eur(o)} : {a} par la seule réserve de 10 % ({eur(I['reserve'])}) ; {b} avec l'apport restant et "
                f"l'excédent des mois 1 à 3 ({eur(I['disponible'] - I['is'])} hors TVA et IS)")
    ligne(f"Objectif de réserve au mois 12 : 3 mois de frais + 1 mois de rémunération [PR] ({STRAT}:512)", _objectif)
    ligne("Net mensuel par associé, SAS, mois 4 à 12 (avant IR)", lambda n: eur_plage(*R[n]["net_plage"]))
    ligne("Net mensuel par associé, SARL, même enveloppe (avant IR)", lambda n: eur_plage(*R[n]["net_sarl_plage"]))
    ligne(f"Pour comparaison, stratégie retenue ({STRAT}:511-515) : CA sur 12 mois ; net par associé ; trésorerie M12", lambda n:
          f"{eur_cite(sc[n]['strategie']['ca12'])} ; {eur_cite(*sc[n]['strategie']['net'])} ; {eur_cite(*sc[n]['strategie']['treso'])}")
    L.append(table(["Rubrique", "Prudent", "Central", "Ambitieux"], rows))

    # ---- Détail par scénario
    L.append("\n\n## 2. Périmètre, capacité, prix et modalités\n")
    L.append("Prix proposés [PR] et calendrier de paiement retenu ({s}:194-203, 427-446). Le paiement suit la nature "
             "de la prestation : capacité réservée payée d'avance ; livrables payés par acompte puis solde à la "
             "livraison ; consommation variable payée en fin de mois. Rien n'est encaissé avant l'immatriculation "
             "({s}:458).\n".format(s=STRAT))
    rows = [
        ["A. Cadrage (8 JP, 3 à 4 semaines)", "6 000 € HT (plancher)", "6 500 € HT", "6 500 € HT",
         "50 % à la commande, 50 % à la réception sous 8 jours ; travail démarré à l'encaissement"],
        ["B0. Socle pilote (3 à 4 JP par mois, 2 mois)", "—", "3 500 € HT par mois", "3 500 € HT par mois",
         "D'avance : facture le 25, échéance le 1er ; 1er mois à la signature"],
        ["Socle récurrent (périodes de 3 mois)", "Socle + 1 projet : 3 000 € HT par mois dès le mois 3",
         "B1 : 4 500 € HT par mois dès le mois 4", "Socle + 3 : 5 700 € HT par mois dès le mois 4", "D'avance, le 1er du mois"],
        ["C. Lots devisés (JP × 800 € + 10 à 15 %)", "4 500 € HT par trimestre", "Lot du pilote 6 000 € HT ; puis ≈ 3 500 € HT par mois",
         "Deux lots du pilote à 6 000 € HT ; puis ≈ 4 500 € HT par mois", "40 % à la commande, 60 % à la livraison sous 8 jours"],
        ["D. Exploitation d'un processus prouvé", "—", "—", "1 500 € HT par mois dès le mois 7",
         "Minimum d'avance ; variable en fin de mois sous 15 jours (non modélisé)"],
        ["Second client", "—", "— (variante : 2 000 € HT par mois dès le mois 7)", "2 500 € HT par mois dès le mois 6 (probabilité 50 %)", "[HY] mensuel d'avance"],
        ["Sous-traitance", "0", "0 (tiers facturés au client)", "3 JP par mois à 450 à 550 € HT", "Attestation de vigilance dès 5 000 € HT cumulés"],
        ["E. Avenant, urgences", "900 € HT par JP", "900 € HT par JP", "900 € HT par JP", "Fin de mois, sous 15 jours ; seulement sur bon écrit préalable"],
    ]
    L.append(table(["Offre", "Prudent", "Central", "Ambitieux", "Modalités"], rows))
    L.append("\n\nTous les prix sont HT ; TTC = HT × 1,2. Si l'entité de GianLuca ne récupère pas la TVA, la TVA est "
             f"un coût réel pour elle [HY] ({STRAT}:462). Achats, abonnements et prestataires du client ne passent "
             f"jamais par Marwin et ne sont pas dans le CA ({STRAT}:188, 445, 488).\n")
    L.append("\n**Hypothèses de modélisation propres au script** [HY] : le solde du cadrage est encaissé le mois "
             "suivant l'acompte ; le socle est encaissé le mois du service ; les lots en régime sont représentés par "
             "des tranches mensuelles (40 % encaissés le mois de commande, 60 % le mois suivant) ; les lots du pilote "
             "et du prudent ont leur solde le mois suivant la commande ; JP d'un lot = prix ÷ 900 €.\n")

    for n in ORDRE:
        r = R[n]
        s, plan, I = r["s"], r["plan"], r["I"]
        L.append(f"\n### {SCENARIOS[n]['libelle']}\n")
        L.append(f"**Périmètre** [PR] : {SCENARIOS[n]['perimetre']}\n\n"
                 f"**Capacité** [ES] : {SCENARIOS[n]['dispo']} ; capacité facturable ≈ {num(SCENARIOS[n]['capacite'], 0)} JP "
                 f"par mois ({STRAT}:361-366, 495-496). JP vendues en moyenne sur les mois 4 à 12 : {num(I['jp_regime'])} ; "
                 f"prix moyen encaissé par JP vendue : {eur10(I['prix_jp'])}.\n")
        rows = []
        nmois = plan.tm(12) + 1
        a = series_affichees(s, nmois)
        sorties = arrondis_cumules([s["frais_ttc"][t] + s["dem_ttc"][t] + s["st_ttc"][t] for t in range(nmois)])
        for t in range(nmois):
            m = t - plan.t_m1 + 1
            rows.append([MOIS[t], f"M{m}" if m >= 1 else "avant", eur(a["fact_ht"][t]), eur(a["enc_ttc"][t]),
                         eur(a["tva_coll"][t]), eur(a["tva_versee"][t]), eur(sorties[t]), eur(a["remu"][t]),
                         eur(a["cash"][t]), eur(a["disponible"][t]), num(s["jp"][t] + s["jp_st"][t])])
        rows.append(["**Total**", "", eur(sum(a["fact_ht"])), eur(sum(a["enc_ttc"])), eur(sum(a["tva_coll"])),
                     eur(sum(a["tva_versee"])), eur(sum(sorties)), eur(sum(a["remu"])), "", "", ""])
        L.append(table(["Mois", "M", "Facturé HT", "Encaissé TTC", "TVA collectée", "TVA reversée",
                        "Frais, démarrage, sous-traitance TTC", "Rémunérations (coût)", "Trésorerie en banque",
                        "Trésorerie disponible", "JP vendues"], rows))
        L.append("\n")

    # ---- Rémunérations
    L.append("\n## 3. Rémunérations : brut, cotisations et net par associé (SAS et SARL)\n")
    L.append(
        "**Hypothèses explicites.** Deux associés à parts égales, tous deux dirigeants ; même enveloppe pour les deux ; "
        f"rien avant le mois 4 ({STRAT}:511) ; enveloppe constante ensuite, calculée par le script (règle en tête du "
        f"script). SAS : coût total = 1,7 à 1,9 fois le net [HY] ({DROIT}:98) ; brut indicatif = net ÷ 0,75 [HY] "
        f"({R1}:50). SARL : deux cogérants à 50/50, donc TNS [FV] ({DROIT}:109) ; barème F38152 « revenus 2025 » "
        f"appliqué à 74 % du coût total [ES] ({DROIT}:97) ; forfaits de première année ≈ 3 591 € puis régularisation "
        f"[FV/ES] ({DROIT}:111, 189-195). Pas d'ACRE, d'ARE, de mutuelle ni de prévoyance ; **pas d'impôt sur le "
        "revenu** [IN].\n")
    rows = []
    for n in ORDRE:
        r = R[n]
        nb = r["I"]["nb_mois_remu"]
        nt = r["nets"]
        rows.append([SCENARIOS[n]["libelle"], eur(r["I"]["E"]), eur(nt["C"]),
                     eur_plage(nt["sas_brut"]["haut"], nt["sas_brut"]["bas"]),
                     eur_plage(nt["C"] - nt["sas"]["haut"], nt["C"] - nt["sas"]["bas"]),
                     eur_plage(nt["sas"]["haut"], nt["sas"]["bas"]),
                     eur_plage(nt["sas"]["haut"] / nb, nt["sas"]["bas"] / nb),
                     eur(nt["sarl_cotis"]), eur(nt["sarl_net"]), eur(nt["sarl_net"] / nb),
                     eur(nt["sarl_regul"])])
    L.append(table(["Scénario", "Enveloppe mensuelle (deux associés, coût total)", "Coût total par associé sur 9 mois",
                    "SAS : brut indicatif", "SAS : cotisations (salariales et patronales)", "SAS : net sur 9 mois",
                    "SAS : net par mois", "SARL : cotisations TNS définitives", "SARL : net sur 9 mois",
                    "SARL : net par mois", "SARL : régularisation en année 2 (+ à payer, − rendu)"], rows))
    L.append(
        "\n\nLecture : frais et démarrage à leur valeur centrale ; les plages SAS ne reflètent que le coefficient "
        "1,7 à 1,9 (la synthèse de la section 1 y ajoute les frais bas et hauts). En SARL, la première "
        "année se paie sur les forfaits (≈ 3 600 € par gérant), même pendant les mois sans rémunération ; l'écart est "
        f"régularisé l'année suivante ({DROIT}:189-192). Les dividendes ne sont pas un levier la première année : "
        "aucun bénéfice n'est distribuable avant la clôture et l'approbation des comptes (voir `structures.md`).\n")
    L.append(
        "\n**Comparaison avec un emploi salarié chez le client** (pour mémoire) : un poste de cadre ≈ 3 400 € nets pour "
        f"6 149 € de coût employeur [MM] ({VR6}:25) rapporterait plus que tous les scénarios centraux de Marwin la "
        f"première année ({STRAT}:707). C'est le principal risque pour l'indépendance de Marwin pendant la négociation.\n")

    # ---- Seuils
    L.append("\n## 4. Seuil de rentabilité en journées vendues\n")
    L.append("Méthode [ES] : JP vendues par mois nécessaires pour couvrir, au prix moyen par JP du régime (mois 4 à 12), "
             "les frais fixes, la réserve de 10 % et, selon la ligne, une rémunération. La sous-traitance est comptée "
             "comme coût variable par JP. L'IS est négligé (il ne porte que sur la réserve).\n")
    rows = []
    for n in ORDRE:
        r = R[n]
        sj = r["seuils"]
        rows.append([SCENARIOS[n]["libelle"], eur10(r["I"]["prix_jp"]), eur(r["I"]["frais_mensuels"]),
                     num(sj["frais"]), num(sj["remu"]),
                     f"{num(sj['plancher'][0])} à {num(sj['plancher'][1])}",
                     num(r["I"]["jp_regime"]),
                     num(SCENARIOS[n]["capacite"], 0) + (" (plafond 10)" if n == "central" else "")])
    L.append(table(["Scénario", "Prix moyen par JP vendue", "Frais fixes par mois", "Seuil : frais et réserve",
                    "Seuil : + rémunération du scénario", "Seuil : + 2 500 € nets par ETP engagé",
                    "JP vendues prévues (mois 4 à 12)", "Capacité facturable"], rows))
    L.append(f"\n\nETP engagés [HY] : 0,75 (prudent), 1,15 (central), 1,8 (ambitieux) ({STRAT}:363-366).\n")

    # ---- Variantes
    L.append("\n## 5. Variantes\n")
    vb, vs = R["variante_basse"], R["variante_second"]
    L.append(
        f"- **Prudent, variante basse** (GianLuca s'arrête au cadrage, probabilité {pct(1 - PROBA['prudent']['suite'])} "
        f"selon {STRAT}:502) : CA {eur(vb['I']['fact_ht'])} HT ; résultat avant IS {eur(vb['I']['resultat'])} ; "
        f"trésorerie disponible à la fin du mois 12 {eur(vb['I']['disponible'])} (dont {eur(vb['I']['credit_tva'])} de crédit "
        f"de TVA remboursable, non compté) sur un apport de {eur(APPORT['prudent'])}, "
        "si rien n'est arrêté. Aucune rémunération. Sans arrêt des frais fixes de 1 500 € par mois, la trésorerie devient "
        f"négative en {MOIS[vb['premier_negatif']] if vb['premier_negatif'] is not None else '(jamais)'} : les "
        "abonnements et l'assurance doivent être résiliables au mois et arrêtés dès l'échec constaté.\n"
        f"- **Central avec un second client** ({STRAT}:522) : CA {eur(vs['I']['fact_ht'])} HT ; part de GianLuca "
        f"{pct(vs['I']['part_gl'])} sur douze mois et {pct(vs['I']['part_gl_m12'])} au mois 12 ; net par associé "
        f"{eur_plage(*vs['net_plage'])} par mois en SAS ; trésorerie disponible fin du mois 12 {eur(vs['I']['disponible'])}. "
        "Si le second client n'est pas signé au mois 9, la cible de dépendance « 80 % au plus » passe au mois 18.\n")

    # ---- Écarts
    L.append("\n## 6. Écarts avec la stratégie retenue et leurs causes\n")
    L.append(
        f"La stratégie ({STRAT}:492-518) utilisait un modèle simplifié qui encaisse les factures le mois même et ne "
        "modélise ni l'IS ni la TVA. Ce modèle les ajoute, ce qui explique les écarts :\n"
        "- **IS** : il réduit la rémunération soutenable d'environ 1/9 de l'IS annuel par mois ;\n"
        "- **TVA** : neutre sur l'année, elle gonfle la trésorerie en banque d'un mois de TVA nette (à ne jamais "
        "dépenser) et coûte un peu de trésorerie au démarrage (TVA payée sur les frais avant d'en collecter) ;\n"
        "- **délais d'encaissement** : les soldes de lots arrivent le mois suivant ; le dernier solde des mois 1 à 12 "
        "tombe au mois 13 ;\n"
        "- **exploitation D (ambitieux)** : la stratégie la fait commencer au mois 7 dans son texte ({s}:494) mais au "
        "mois 4 dans son calcul (verif § 10 : 1 500 € par mois sur les mois 4 à 12). Le modèle suit la règle écrite "
        "(« au plus tôt au mois 7 », {s}:339), d'où un CA ambitieux inférieur d'environ 4 500 €.\n".format(s=STRAT))
    rows = []
    for n in ORDRE:
        st = SCENARIOS[n]["strategie"]
        I = R[n]["I"]
        rows.append([SCENARIOS[n]["libelle"], eur_cite(st["ca12"]), eur(I["fact_ht"]),
                     eur_cite(*st["net"]), f"≈ {eur(R[n]['net_central'])} ({eur_plage(*R[n]['net_plage'])})",
                     eur_cite(*st["treso"]), eur(I["disponible"])])
    L.append(table(["Scénario", "CA 12 mois (stratégie)", "CA 12 mois (modèle)", "Net par associé (stratégie)",
                    "Net par associé (modèle, SAS)", "Trésorerie M12 (stratégie, avant IS et TVA)",
                    "Trésorerie disponible M12 (modèle)"], rows))

    # ---- Limites
    L.append("\n\n## 7. Limites\n")
    L.append(
        f"- Les probabilités de passage sont des paramètres de jugement [HY] ({STRAT}:502) ; celle de vendre le cadrage "
        "est inconnue [IN].\n"
        f"- Le coefficient SAS vient d'une source secondaire unique ; le barème TNS est celui des revenus 2025 ; les "
        f"lois de finances et de financement de la sécurité sociale pour 2027 sont en discussion : **tout refaire en "
        f"janvier 2027** avec l'expert-comptable et le simulateur officiel ({DROIT}:22-23, 198-207).\n"
        f"- Les frais (assurance, déplacements, conseil) sont des hypothèses [HY/IN] à remplacer par des devis ({STRAT}:837).\n"
        f"- L'IS est calculé comme si les douze mois formaient un exercice, avec le seuil de 42 500 € non proratisé ; "
        "un premier exercice de 13 ou 14 mois relèverait ce seuil au prorata (sans effet ici : aucun bénéfice n'atteint "
        "42 500 €) ; en prudent, le mois 12 (janv. 2028) appartient déjà au deuxième exercice. La date de clôture réelle "
        f"est à arrêter avec l'expert-comptable ({DROIT}:143).\n"
        f"- Les comportements de paiement de l'entité de GianLuca sont inconnus [IN] ({STRAT}:467) : voir `stress-tests.md`.\n"
        "- Aucun coût lié à la fuite au-delà du conseil (sanction, réclamations, franchise d'assurance) n'est chiffré [IN].\n"
        "- Le central retient la voie de pilote la plus chère (B0 et un lot, 13 000 € HT ; voies du pilote : "
        f"{STRAT}:247-249). Avec un pilote " + " ; avec un pilote ".join(
            f"{lib} ({eur(prix)} HT), le CA sur 12 mois tombe à {eur(ca)} HT et la trésorerie libre du mois 12 à {eur(lib_)}"
            for lib, prix, ca, lib_, _e in R["central"]["voies_pilote"])
        + f" (contre {eur(C['libre'])}). La règle de rémunération, qui ne regarde que les mois 4 à 12, ne baisse pas : "
        "c'est le coussin qui absorbe l'écart.\n"
        "- Matériel informatique non budgété au-delà de la mise en place (200 à 700 €) : les associés utilisent leur "
        "propre matériel [HY].\n")
    _ecrire(dossier, "scenarios.md", "\n".join(L))


# =====================================================================================
# 13. ÉCRITURE : tresorerie-18-mois.csv et .md (scénario central)
# =====================================================================================
COLONNES_CSV = [
    ("mois", None), ("mois_contrat", None),
    ("contrat_certain_ttc", None), ("cadrage_ttc", "enc_ttc_cadrage"), ("pilote_ttc", "enc_ttc_pilote"),
    ("socle_ttc", "enc_ttc_socle"), ("lots_ttc", "enc_ttc_lots"), ("total_encaissements_ttc", "enc_ttc"),
    ("dont_tva_collectee", "tva_coll"), ("encaissements_ht", "enc_ht"), ("probabilite_cumulee", None),
    ("encaissements_ponderes_ttc", "enc_pond_ttc"), ("projets_non_finances", None),
    ("apport_associes", "apport"), ("demarrage_ttc", "dem_ttc"), ("frais_fixes_ttc", "frais_ttc"),
    ("tva_deductible", "tva_ded"), ("remunerations_cout_total", "remu"), ("tva_reversee", "tva_versee"),
    ("is_paye", "is_paye"), ("flux_net", "flux"), ("tresorerie_fin_de_mois", "cash"),
    ("tva_due_fin_de_mois", "tva_due"), ("tresorerie_disponible", "disponible"), ("reserve_cumulee", "reserve"),
    ("is_a_provisionner", "is_prov"), ("tresorerie_libre", "libre"), ("jp_vendues", "jp"),
]


def _proba_mois(plan, t):
    ps = [l.proba for l in plan.lignes if l.t_encaisse == t and l.categorie != "cadrage"]
    if any(l.t_encaisse == t and l.categorie == "cadrage" for l in plan.lignes) and not ps:
        return 1.0
    return min(ps) if ps else 0.0


FLUX = ("enc_ttc_cadrage", "enc_ttc_pilote", "enc_ttc_socle", "enc_ttc_lots", "enc_ttc", "tva_coll", "enc_ht",
        "enc_pond_ttc", "apport", "dem_ttc", "frais_ttc", "tva_ded", "remu", "tva_versee", "is_paye", "flux",
        "fact_ht", "st_ttc")


def series_affichees(s, n):
    """Flux : arrondis cumulés (totaux justes) ; soldes (trésorerie, réserve, TVA due…) : arrondi direct."""
    a = {}
    for k, v in s.items():
        a[k] = arrondis_cumules(v[:n]) if k in FLUX else [r100(x) for x in v[:n]]
    return a


def ecrire_tresorerie(dossier, R):
    plan, s, E = R["central"]["plan"], R["central"]["s"], R["central"]["I"]["E"]
    a = series_affichees(s, HORIZON_TRESO)
    chemin = os.path.join(dossier, "tresorerie-18-mois.csv")
    with open(chemin, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow([c for c, _ in COLONNES_CSV])
        for t in range(HORIZON_TRESO):
            m = t - plan.t_m1 + 1
            row = []
            for c, k in COLONNES_CSV:
                if c == "mois":
                    row.append(MOIS[t])
                elif c == "mois_contrat":
                    row.append(f"M{m}" if m >= 1 else "avant")
                elif c in ("contrat_certain_ttc", "projets_non_finances"):
                    row.append(0)
                elif c == "probabilite_cumulee":
                    row.append(f"{_proba_mois(plan, t):.2f}".replace(".", ","))
                elif c == "jp_vendues":
                    row.append(num(s["jp"][t]))
                else:
                    row.append(int(a[k][t]))
            w.writerow(row)

    L = []
    L.append("# Plan de trésorerie sur dix-huit mois : scénario central\n")
    L.append(ENTETE_COMMUN)
    L.append("\nDonnées mensuelles : `tresorerie-18-mois.csv` (séparateur « ; », même contenu que les tableaux "
             "ci-dessous). Les flux mensuels sont arrondis à la centaine en reportant l'arrondi d'un mois sur l'autre : "
             "les totaux de colonne sont justes, mais une même dépense de 2 224 € peut apparaître pour 2 200 € un mois "
             "et 2 300 € le suivant. Les soldes (trésorerie, réserve, TVA due) sont arrondis directement.\n")
    L.append("\n" + FAITS_NOUVEAUX)
    t12 = plan.tm(12)
    t_fin = HORIZON_TRESO - 1
    pb = min(range(HORIZON_TRESO), key=lambda t: s["disponible"][t])
    L.append("\n## 0. Lecture rapide\n")
    L.append(
        f"- **Contrat certain : aucun.** Les encaissements « certains » valent 0 € chaque mois [FV négatif] ({STRAT}:33). "
        "Tout le reste est une hypothèse commerciale, à commencer par la vente du cadrage.\n"
        f"- Mois 1 = {MOIS[plan.t_m1]} [HY] : il suppose un rendez-vous avant le 15 décembre 2026, une entité payeuse "
        f"nommée, une immatriculation fin décembre ou début janvier et l'acompte du cadrage encaissé en janvier "
        f"({STRAT}:44, 500).\n"
        f"- **Point bas de la trésorerie disponible** : {eur(s['disponible'][pb])} en {MOIS[pb]}. L'apport de "
        f"{eur(APPORT['central'])} couvre le démarrage ({eur(sum(x[2] for x in plan.demarrage))} HT) ; sans apport, "
        f"il manquerait {eur(max(0, APPORT['central'] - s['disponible'][pb]))} à ce moment.\n"
        f"- **Fin du mois 12 ({MOIS[t12]})** : trésorerie en banque {eur(s['cash'][t12])}, dont TVA due "
        f"{eur(s['tva_due'][t12])}, réserve {eur(s['reserve'][t12])} et IS de l'exercice 2027 à payer en mai 2028 "
        f"{eur(s['is_prov'][t12])} ; trésorerie libre {eur(s['libre'][t12])}.\n"
        f"- **Fin des 18 mois ({MOIS[t_fin]})** : trésorerie en banque {eur(s['cash'][t_fin])} ; trésorerie libre "
        f"{eur(s['libre'][t_fin])}. Rémunération versée à partir du mois 4 : enveloppe de {eur(E)} par mois pour les "
        f"deux associés, soit ≈ {eur(R['central']['net_central'])} ({eur_plage(*R['central']['net_plage'])}) nets par "
        "associé et par mois en SAS, avant IR.\n"
        f"- **Pondéré par les probabilités de passage** (pilote 60 %, socle 70 %, renouvellement trimestriel 80 %, "
        f"{STRAT}:502), les encaissements des 18 mois tombent de {eur(sum(s['enc_ttc'][:HORIZON_TRESO]))} à "
        f"{eur(sum(s['enc_pond_ttc'][:HORIZON_TRESO]))} TTC, **à condition que le cadrage soit vendu** "
        "(probabilité [IN]). Le plan ci-dessous est donc un plan de pilotage, pas une prévision.\n")

    L.append("\n## 1. Trois blocs distincts\n")
    L.append(table(["Bloc", "Contenu", "Encaissements sur 18 mois (TTC)"], [
        ["1. Contrat certain", "Aucun contrat, aucune facture, aucune entité payeuse [FV négatif]", "0 €"],
        ["2. Hypothèses de vente et de renouvellement",
         "Cadrage (première vente, probabilité [IN]) ; pilote (60 %) ; socle B1 par trimestres renouvelés "
         "(70 %, puis 80 % par trimestre) ; lots liés au socle [HY] (" + STRAT + ":502)",
         eur(sum(s["enc_ttc"][:HORIZON_TRESO]))],
        ["3. Projets non financés", "Laboratoire, création avec Medhi et STRATES, vernissage « signature », DGX Spark : "
         "aucune recette et aucune dépense ; Marwin n'avance rien pour le client (" + STRAT + ":188, 639-654)", "0 €"],
    ]))
    L.append("\n\n**Projets non financés, pour mémoire** (montants des archives, jamais inscrits au plan) :\n")
    L.append(table(["Projet", "Montant évoqué", "Statut"], [list(x) for x in PROJETS_NON_FINANCES]))

    L.append("\n\n## 2. Calendrier de paiement retenu et traduction dans le modèle\n")
    L.append(
        f"La contradiction des archives (« règlement sous sept jours après facture de fin de mois », {ACC}:57, contre "
        f"« mois 2 à 6 payés d'avance, en début de mois », {OFF}:19) est tranchée par la stratégie : **le paiement suit "
        f"la nature de la prestation** [PR] ({STRAT}:429-434).\n")
    L.append(table(["Prestation", "Règle retenue [PR]", "Dans le modèle [HY]"], [
        ["A. Cadrage", "50 % à la commande ; 50 % à la réception, sous 8 jours", "Acompte au mois 1 ; solde au mois 2"],
        ["B0, B1. Socle", "D'avance : facture le 25 du mois précédent, échéance le 1er", "Encaissé le mois du service"],
        ["C. Lots", "40 % à la commande ; 60 % à la livraison, sous 8 jours", "Tranches mensuelles : 40 % le mois de commande, 60 % le mois suivant"],
        ["Achats et prestataires du client", "Jamais par Marwin", "0 €"],
        ["TVA", "Exigible à l'encaissement [FV] (" + R2 + ":385)", "Collectée à l'encaissement ; reversée " + texte_decalage_tva() + " (réel normal mensuel [HY])"],
        ["Rémunérations", "Rien avant le mois 4 [PR]", "Enveloppe constante dès le mois 4, cotisations comprises le mois même"],
        ["IS", "15 % puis 25 % [FV]", "Exercice 2027 clos le 31 déc. [HY] ; solde payé en mai 2028, hors horizon : provisionné"],
    ]))

    L.append("\n\n## 3. Encaissements par bloc (TTC)\n")
    rows = []
    for t in range(HORIZON_TRESO):
        m = t - plan.t_m1 + 1
        rows.append([MOIS[t], f"M{m}" if m >= 1 else "avant", "0 €", eur(a["enc_ttc_cadrage"][t]), eur(a["enc_ttc_pilote"][t]),
                     eur(a["enc_ttc_socle"][t]), eur(a["enc_ttc_lots"][t]), eur(a["enc_ttc"][t]), eur(a["tva_coll"][t]),
                     num(_proba_mois(plan, t), 2), eur(a["enc_pond_ttc"][t]), "0 €"])
    rows.append(["**Total**", "", "0 €", eur(sum(a["enc_ttc_cadrage"])), eur(sum(a["enc_ttc_pilote"])),
                 eur(sum(a["enc_ttc_socle"])), eur(sum(a["enc_ttc_lots"])),
                 eur(sum(a["enc_ttc"])), eur(sum(a["tva_coll"])), "",
                 eur(sum(a["enc_pond_ttc"])), "0 €"])
    L.append(table(["Mois", "M", "Contrat certain", "Cadrage", "Pilote", "Socle B1", "Lots", "Total TTC", "dont TVA",
                    "Probabilité cumulée la plus faible du mois [HY]", "Pondéré TTC [ES]", "Projets non financés"], rows))

    L.append("\n\n## 4. Décaissements et trésorerie\n")
    rows = []
    for t in range(HORIZON_TRESO):
        m = t - plan.t_m1 + 1
        rows.append([MOIS[t], f"M{m}" if m >= 1 else "avant", eur(a["apport"][t]), eur(a["dem_ttc"][t]), eur(a["frais_ttc"][t]),
                     eur(a["remu"][t]), eur(a["tva_versee"][t]), eur(a["flux"][t]), eur(a["cash"][t]), eur(a["tva_due"][t]),
                     eur(a["disponible"][t]), eur(a["reserve"][t]), eur(a["is_prov"][t]), eur(a["libre"][t]), num(s["jp"][t])])
    H = HORIZON_TRESO
    rows.append(["**Total**", "", eur(sum(a["apport"])), eur(sum(a["dem_ttc"])), eur(sum(a["frais_ttc"])), eur(sum(a["remu"])),
                 eur(sum(a["tva_versee"])), eur(sum(a["flux"])), eur(a["cash"][H - 1]), "", "", "", "", "", ""])
    L.append(table(["Mois", "M", "Apport", "Démarrage TTC", "Frais fixes TTC", "Rémunérations (coût total)",
                    "TVA reversée", "Flux net", "Trésorerie en banque", "TVA due", "Trésorerie disponible",
                    "Réserve cumulée", "IS à provisionner", "Trésorerie libre", "JP vendues"], rows))
    L.append("\n\nDéfinitions : trésorerie disponible = trésorerie en banque − TVA collectée non encore reversée ; "
             "trésorerie libre = disponible − réserve (10 % du CA encaissé) − IS à provisionner. JP vendues : plafond "
             f"engagé de 10 JP par mois la première année ({STRAT}:485).\n")

    # TVA : variante réel simplifié
    tva_2027 = sum(s["tva_coll"][t] - s["tva_ded"][t] for t in range(0, T_DEC_2027 + 1))
    L.append("\n## 5. TVA : ce qui entre n'est pas à Marwin\n")
    L.append(
        f"- Sur les 18 mois, Marwin collecte {eur(sum(s['tva_coll'][:HORIZON_TRESO]))} de TVA, en déduit "
        f"{eur(sum(s['tva_ded'][:HORIZON_TRESO]))} et en reverse {eur(sum(s['tva_versee'][:HORIZON_TRESO]))} ; "
        f"{eur(s['tva_due'][t_fin])} restent dus fin {MOIS[t_fin]}.\n"
        "- Un retard de paiement du client ne fait pas avancer la TVA : elle n'est exigible qu'à l'encaissement [FV] "
        f"({R2}:19, 385).\n"
        f"- **Variante « réel simplifié »** [HY, à confirmer par l'expert-comptable] : sans acompte la première année, "
        f"la TVA nette de 2027 (≈ {eur(tva_2027)}) resterait sur le compte jusqu'à la déclaration annuelle de mai 2028. "
        "Elle gonflerait la trésorerie apparente sans jamais être disponible. Le modèle retient la déclaration "
        "mensuelle, plus lisible pour deux associés qui découvrent la gestion.\n"
        f"- Franchise en base : sans intérêt ici ; facturer la TVA dès la première facture ({DROIT}:299).\n")

    L.append("\n## 6. Points d'attention\n")
    L.append(
        f"- **Démarrage financé par l'apport.** Le conseil sur la fuite (novembre 2026) et les statuts et le pacte "
        f"(décembre 2026) sont payés avant tout encaissement. Si l'apport n'existe pas, la stratégie prévoit de réduire "
        f"les sorties de la phase 0 au conseil sur la fuite et aux statuts ({STRAT}:776).\n"
        "- **Le surplus des mois 1 à 3** (pilote payé, aucune rémunération) constitue l'essentiel du coussin : un pilote "
        "non vendu le supprime (voir `stress-tests.md`).\n"
        f"- **L'IS de l'exercice 2027** ({eur(s['is_prov'][T_DEC_2027])}) est dû en mai 2028, juste après l'horizon : "
        "il ne doit pas être dépensé.\n"
        f"- **Dépendance à un seul client : 100 %** pendant 18 mois, **à assumer par écrit** entre les associés [PR], ce qui n'est pas fait [IN] ({STRAT}:514) ; la variante avec "
        "un second client est dans `scenarios.md`.\n"
        f"- **Cotisations des dirigeants** : en SAS, aucune sans rémunération ; versées avec chaque paie ensuite "
        f"({DROIT}:195).\n"
        + "- **Prime d'assurance payée d'avance** [ES] : si la RC professionnelle est payée en une fois avant la "
        "première prestation, le point bas de la trésorerie disponible tombe à "
        + " ; ".join(f"{eur(v_)} en {MOIS[t_]} pour une prime de {eur(p_)} par an" for p_, v_, t_ in R["central"]["sensib_rc"])
        + f" (montant de la prime [IN], hypothèse de 200 à 250 € par mois, {STRAT}:506). L'apport de "
        f"{eur(APPORT['central'])} ne laisse alors presque aucune marge : obtenir un paiement fractionné de la prime, ou "
        f"viser le haut de la fourchette d'apport (8 000 à 14 000 €, {STRAT}:172).\n")
    L.append("\n## 7. Limites\n")
    L.append(
        f"- Pratiques de paiement de l'entité de GianLuca inconnues [IN] ({STRAT}:467) ; le plan suppose des paiements à "
        "l'échéance.\n"
        "- Les renouvellements trimestriels du socle et le rythme des lots sont des hypothèses ; ils sont présentés "
        "en clair, avec leur probabilité cumulée, pour ne jamais être lus comme acquis.\n"
        "- Date de création, date de clôture et régime de TVA à arrêter avec l'expert-comptable ; CFE non due l'année "
        f"de création, puis base réduite si la déclaration 1447-C-SD est déposée à temps ({DROIT}:302) : non modélisée ; "
        "son montant est [IN] (quelques centaines d'euros par an au plus [HY]) et la ligne « imprévus » le couvre. Si la "
        "société est créée en décembre 2026, une première CFE réduite peut tomber en décembre 2027, dans l'horizon.\n"
        "- **Frais engagés avant l'immatriculation** (conseil sur la fuite, statuts) : supposés repris par la société, TVA "
        "récupérée et charges déductibles [HY]. La fuite concerne un traitement antérieur à Marwin : si le conseil n'est "
        "pas un acte de la société en formation, il reste à la charge des associés, sans TVA récupérable ni déduction "
        "(question 5 de `structures.md`).\n"
        "- **Crédit de TVA** : il n'est pas compté dans la trésorerie disponible (prudence) ; il se récupère par imputation "
        "ou sur demande de remboursement.\n"
        "- **Déplacements** : TVA récupérée sur la moitié [HY] ; elle ne l'est pas sur les billets de transport de "
        "personnes ni sur des indemnités kilométriques. La TVA déductible affichée est donc un peu surévaluée ; l'effet "
        "sur la trésorerie est négligeable.\n"
        "- **Colonne « probabilité cumulée »** : la valeur 1,00 des mois du cadrage est **conditionnelle à la vente du "
        "cadrage**, dont la probabilité est [IN] ; ce n'est pas une certitude.\n")
    _ecrire(dossier, "tresorerie-18-mois.md", "\n".join(L))


# =====================================================================================
# 14. TESTS DE RÉSISTANCE (scénario central, 18 mois)
# =====================================================================================
def _mesures(s_base, s, plan, E):
    """Mesures d'un test sur 18 mois. Besoin de financement = apport supplémentaire pour que la trésorerie
    disponible ne soit jamais négative ; besoin « un mois de charges » = pour garder chaque mois en caisse les
    frais et rémunérations du mois. Mois critique = premier mois sous zéro, à défaut mois de l'écart maximal
    avec la base."""
    h = range(HORIZON_TRESO)
    tmin = min(h, key=lambda t: s["disponible"][t])
    besoin = max(0.0, -s["disponible"][tmin])
    besoin_charges = max(0.0, max(s["frais_ttc"][t] + s["remu"][t] - s["disponible"][t] for t in h))
    ecarts = [s_base["disponible"][t] - s["disponible"][t] for t in h]
    t_ecart = next(t for t in h if ecarts[t] >= max(ecarts) - 50)   # premier mois où la perte atteint son maximum
    premier_negatif = next((t for t in h if s["disponible"][t] < 0), None)
    t12 = plan.tm(12)
    objectif = OBJECTIF_RESERVE_MOIS_FRAIS * sum(FRAIS_MONTANTS["central"]) + E
    return {
        "point_bas": s["disponible"][tmin], "t_bas": tmin, "besoin": besoin, "besoin_charges": besoin_charges,
        "ecart_max": s_base["disponible"][t_ecart] - s["disponible"][t_ecart], "t_ecart": t_ecart,
        "t_critique": premier_negatif if premier_negatif is not None else t_ecart,
        "ecart_fin": s["disponible"][HORIZON_TRESO - 1] - s_base["disponible"][HORIZON_TRESO - 1],
        "dispo_m12": s["disponible"][t12], "objectif": objectif,
        "manque_objectif": max(0.0, objectif - (s["disponible"][t12] - s["is_prov"][t12])),
        "premier_negatif": premier_negatif,
        # crédit de TVA au point bas : créance sur le Trésor, remboursable sur demande, NON comptée dans la
        # trésorerie disponible (contrôle du 4 nov. 2026 : il explique l'essentiel de certains besoins)
        "credit_bas": s["credit_tva"][tmin],
    }


def _reduire_frais(plan, t_debut, montant):
    for t in range(t_debut, N_SIM):
        tot = sum(plan.frais[t].values())
        if tot > 0:
            plan.frais[t] = {k: v * montant / tot for k, v in plan.frais[t].items()}


def _supprimer(plan, cond):
    plan.lignes = [l for l in plan.lignes if not cond(l)]


def tests_de_resistance(base_plan, E):
    s_base = simuler(base_plan, E)
    tm = base_plan.tm
    out = []

    def run(plan, env=E):
        s = simuler(plan, env)
        return s, _mesures(s_base, s, plan, env)

    # 1. Retards de paiement
    for d in STRESS["retards_mois"]:
        pa = copy.deepcopy(base_plan)
        for l in pa.lignes:
            if l.client == "GianLuca" and l.t_encaisse >= tm(4):
                l.t_encaisse += d
        sa, ma = run(pa)
        pb = copy.deepcopy(pa)
        pb.remu_masque = [0.0] * N_SIM
        for t in range(tm(4) + d, N_SIM):   # rémunération versée seulement sur encaissements reçus
            pb.remu_masque[t] = 1.0
        sb, mb = run(pb)
        out.append({"id": f"1-{d}", "titre": f"Retard de paiement de {30 * d} jours", "A": ma, "B": mb,
                    "hyp": f"À partir du mois 4 ({MOIS[tm(4)]}), chaque paiement de l'entité de GianLuca arrive {30 * d} jours "
                           "après l'échéance, durablement. A : Marwin continue de travailler et de payer les associés. "
                           "B : la rémunération n'est versée que sur les encaissements reçus (décalée du même retard).",
                    "intenable": "Payer les associés à l'échéance prévue ; lancer un nouveau lot ; tout engagement de "
                                 "frais nouveau. " + ("À 60 jours et plus, le contrat lui-même devient intenable."
                                                      if d >= 2 else ""),
                    "mesure": f"Relance le lendemain de l'échéance ; suspension des travaux non urgents 8 jours après une "
                              f"relance sans effet ; résiliation possible à 30 jours ; pénalités ≥ 3 fois le taux légal et "
                              f"40 € par facture [FV] ({STRAT}:463) ; socle payé d'avance ; aucune rémunération sans "
                              f"encaissement. La TVA, exigible à l'encaissement, n'est pas avancée [FV]."})

    # 2. Rupture après trois mois (fin du pilote) et après le premier trimestre de socle
    for m_fin, lib in ((3, "à la fin du pilote (mois 3)"), (6, "après le premier trimestre de socle (mois 6)")):
        pa = copy.deepcopy(base_plan)
        t_stop = tm(m_fin)
        # rupture brutale : plus rien n'est facturé après la rupture, et le dernier solde de lot (travail fait
        # avant la rupture) n'est pas payé
        dernier = max(l.t_facture for l in pa.lignes
                      if l.client == "GianLuca" and "solde" in l.libelle and l.t_facture <= t_stop + 1)
        _supprimer(pa, lambda l: l.client == "GianLuca" and (l.t_facture > t_stop or
                                                            ("solde" in l.libelle and l.t_facture == dernier)))
        # B : règle (rémunération arrêtée, frais ramenés à 1 000 € après un mois)
        pb = copy.deepcopy(pa)
        pb.remu_masque = [1.0 if tm(4) <= t <= t_stop else 0.0 for t in range(N_SIM)]
        _reduire_frais(pb, t_stop + 2, FRAIS_REDUITS_APRES_RUPTURE)
        sb, mb = run(pb)
        # A : réaction tardive (rémunération maintenue 3 mois, frais de 2 000 € maintenus 6 mois, puis 1 000 €)
        pa.remu_masque = [1.0 if tm(4) <= t <= max(t_stop, tm(3)) + 3 else 0.0 for t in range(N_SIM)]
        _reduire_frais(pa, t_stop + 7, FRAIS_REDUITS_APRES_RUPTURE)
        sa, ma = run(pa)
        out.append({"id": f"2-{m_fin}", "titre": f"Rupture brutale {lib}", "A": ma, "B": mb,
                    "hyp": f"L'entité de GianLuca arrête tout fin {MOIS[t_stop]} sans préavis et ne paie pas le dernier "
                           "solde de lot ; aucun autre client avant avril 2028. A : réaction tardive, rémunération "
                           "versée trois mois de plus, frais de 2 000 € maintenus six mois puis ramenés à 1 000 €. "
                           "B : règle appliquée, rémunération arrêtée, frais ramenés à 1 000 € par mois après un mois.",
                    "intenable": "Les frais fixes de 2 000 € par mois et toute rémunération ; un abonnement ou un "
                                 "engagement de plus de trois mois ; le revenu des associés tiré de Marwin.",
                    "mesure": f"Préavis d'un mois et mois en cours dû ({STRAT}:465) ; acompte et solde à la livraison ; "
                              f"réserve visant six mois de frais réduits ({STRAT}:529) ; revenus extérieurs maintenus ; "
                              "abonnements résiliables au mois."})

    # 3. Non-renouvellement après six mois de socle (fin du mois 9), préavis respecté
    pa = copy.deepcopy(base_plan)
    t9 = tm(9)
    _supprimer(pa, lambda l: l.client == "GianLuca" and l.categorie in ("socle",) and l.t_facture > t9)
    _supprimer(pa, lambda l: l.client == "GianLuca" and l.categorie == "lots" and
               ((l.t_facture > t9 and "acompte" in l.libelle) or (l.t_facture > t9 + 1)))
    pb = copy.deepcopy(pa)
    pb.remu_masque = [1.0 if tm(4) <= t <= t9 else 0.0 for t in range(N_SIM)]
    _reduire_frais(pb, t9 + 2, FRAIS_REDUITS_APRES_RUPTURE)
    sb, mb = run(pb)
    pa.remu_masque = [1.0 if tm(4) <= t <= t9 + 3 else 0.0 for t in range(N_SIM)]
    _reduire_frais(pa, t9 + 7, FRAIS_REDUITS_APRES_RUPTURE)
    sa, ma = run(pa)
    out.append({"id": "3", "titre": "Pas de renouvellement après six mois de socle", "A": ma, "B": mb,
                "hyp": f"Le socle n'est pas renouvelé après {MOIS[t9]} (fin du deuxième trimestre) ; le dernier lot est "
                       "livré et payé ; aucun autre client avant avril 2028. A : rémunération versée trois mois de plus, "
                       "frais de 2 000 € maintenus six mois puis ramenés à 1 000 €. B : rémunération arrêtée à la fin "
                       "du socle, frais ramenés à 1 000 € après un mois.",
                "intenable": "Une rémunération régulière tirée de Marwin ; les frais de 2 000 € ; la dépendance à un seul "
                             "client.",
                "mesure": "Pas de tacite reconduction, renouvellement écrit un mois avant ; prospection de 1,5 à 2,5 JP "
                          f"par mois dès le mois 1 ({STRAT}:719) ; bascule vers d'autres clients ; réserve."})

    # 4. Dépassement d'un développement de 50 % (lot du pilote)
    pa = copy.deepcopy(base_plan)
    jp_lot = PRIX["lot_pilote"] / PRIX_PAR_JP_LOT
    jp_sup = jp_lot * STRESS["depassement"]
    for l in pa.lignes:
        if l.libelle.startswith("Lot du pilote : solde"):
            l.t_facture += 1
            l.t_encaisse += 1
    perte = jp_sup * PRIX_PAR_JP_LOT

    def _reduire_lots_m4(plan_):
        # le travail en plus se fait au mois 4 et prend la place d'autant de lots (plafond de 10 JP)
        for l in plan_.lignes:
            if l.categorie == "lots" and ((l.t_facture == tm(4) and "acompte" in l.libelle) or
                                          (l.t_facture == tm(5) and "solde" in l.libelle)):
                l.ht = max(0.0, l.ht * (1 - perte / PRIX["lots_mois_central"]))
    _reduire_lots_m4(pa)
    sa, ma = run(pa)
    pb = copy.deepcopy(base_plan)   # B : provision comprise, reste facturé par avenant si la cause est chez le client
    _reduire_lots_m4(pb)
    provision = sum(STRESS["provision_lot"]) / 2
    jp_avenant = max(0.0, jp_sup - jp_lot * provision)
    pb.ajouter("Avenant de dépassement", "avenant", tm(4), tm(5), jp_avenant * PRIX["avenant_jp"])
    for l in pb.lignes:
        if l.libelle.startswith("Lot du pilote : solde"):
            l.t_facture += 1
            l.t_encaisse += 1
    sb, mb = run(pb)
    cout_temps = (jp_sup * 591, jp_sup * 737)
    out.append({"id": "4", "titre": "Dépassement d'un développement de 50 %", "A": ma, "B": mb,
                "hyp": f"Le lot du pilote (6 000 € HT, ≈ {num(jp_lot)} JP) demande {num(jp_sup)} JP de plus et est livré un "
                       "mois plus tard ; le travail en plus prend, au mois 4, la place de lots pour "
                       f"≈ {eur(perte)} HT (plafond de 10 JP). A : dépassement de notre fait, entièrement absorbé. "
                       f"B : la provision de risque ({num(jp_lot * provision)} JP) est absorbée, le reste "
                       f"({num(jp_avenant)} JP) est facturé par avenant signé avant le travail (cause chez le client).",
                "intenable": f"Temps non payé valant {eur_plage(*cout_temps)} au coût complet central ({STRAT}:364) ; un "
                             "pilote livré en retard compromet la décision de poursuivre.",
                "mesure": f"Provision de risque de 10 à 15 % dans chaque devis ; jalon écrit au-delà de 8 JP ; avenant "
                          f"signé **avant** tout travail supplémentaire ({STRAT}:287) ; plafond de 10 JP."})

    # 5. Hausse des coûts d'IA
    res5 = []
    for h in STRESS["hausse_ia"]:
        pa = copy.deepcopy(base_plan)
        for t in range(tm(1), N_SIM):
            pa.extra[t].append(("Hausse des coûts d'IA", h, 0.0))
        sa, ma = run(pa)
        E2 = resoudre_enveloppe(pa)
        res5.append((h, ma, E2))
    out.append({"id": "5", "titre": "Hausse des coûts d'IA", "A": res5[1][1], "B": res5[0][1],
                "hyp": f"Les outils et API coûtent {eur_cite(STRESS['hausse_ia'][0])[2:]} (B, plafond de consommation et "
                       f"modèle de repli) ou {eur_cite(STRESS['hausse_ia'][1])[2:]} (A, sans garde-fou) de plus par mois dès janvier 2027 "
                       f"(doublements annoncés chez un fournisseur au 1er déc. 2026 et au 1er janv. 2027 [FV], {VR6}:33). "
                       "Rémunération inchangée.",
                "intenable": f"À +1 000 € par mois, l'enveloppe soutenable tombe de {eur(E)} à {eur(res5[1][2])} par mois : "
                             f"le net par associé baisse d'environ {eur((E - res5[1][2]) / 2 / COEF_SAS['central'])} par mois.",
                "mesure": f"Plafond de consommation mensuel ; deux fournisseurs configurés ; modèle moins cher par défaut ; "
                          f"clause de révision ; outils et licences du client à son nom et à sa charge ({R6}:387-390)."})

    # 6. Indisponibilité d'un associé plusieurs semaines
    m1, m2 = STRESS["absence_mois"]
    pa = copy.deepcopy(base_plan)
    for l in pa.lignes:
        if l.categorie == "socle" and tm(m1) <= l.t_facture <= tm(m2):
            l.ht = PRIX["b0"]                     # changement de palier sans pénalité (au-delà de 10 jours ouvrés)
    _supprimer(pa, lambda l: l.categorie == "lots" and tm(m1) <= l.t_facture <= tm(m2) and "acompte" in l.libelle)
    _supprimer(pa, lambda l: l.categorie == "lots" and tm(m1) + 1 <= l.t_facture <= tm(m2) + 1 and "solde" in l.libelle)
    for t in (tm(m1), tm(m2)):
        pa.jp[t] = JP["b0"]
    sa, ma = run(pa)
    pb = copy.deepcopy(pa)                    # B : rémunération de l'associé absent suspendue (indemnités journalières)
    for t in (tm(m1), tm(m2)):
        pb.remu_masque[t] = 0.5
    sb, mb = run(pb)
    out.append({"id": "6", "titre": "Indisponibilité d'un associé pendant six semaines", "A": ma, "B": mb,
                "hyp": f"Un associé est absent en {MOIS[tm(m1)]} et {MOIS[tm(m2)]} ; capacité ramenée à 4 à 8 JP. Le socle "
                       "passe au palier B0 (3 500 € HT) sans pénalité ; les lots de ces deux mois ne sont pas commandés. "
                       "A : rémunérations maintenues. B : la rémunération de l'associé absent est suspendue.",
                "intenable": "Les lots promis pendant l'absence ; les délais de réception ; le contrôle à quatre yeux, "
                             "qui suppose deux personnes.",
                "mesure": f"Binôme de secours et procédures écrites ; changement de palier sans pénalité au-delà de 10 jours "
                          f"ouvrés ({STRAT}:84, 533) ; prévoyance à souscrire (indemnités journalières plafonnées à 41,95 € "
                          f"en SAS [FV], {DROIT}:113) ; coffre partagé des accès."})

    # 7. Plusieurs urgences simultanées
    tu = tm(6)
    pa = copy.deepcopy(base_plan)
    perte = STRESS["urgences_jp"] * PRIX_PAR_JP_LOT
    for l in pa.lignes:
        if l.categorie == "lots" and ((l.t_facture == tu and "acompte" in l.libelle) or (l.t_facture == tu + 1 and "solde" in l.libelle)):
            l.ht = max(0.0, l.ht * (1 - perte / PRIX["lots_mois_central"]))
    sa, ma = run(pa)
    pb = copy.deepcopy(base_plan)
    pb.ajouter("Avenant urgences", "avenant", tu, tu + 1, STRESS["urgences_jp"] * PRIX["avenant_jp"])
    pb.jp[tu] += STRESS["urgences_jp"]
    sb, mb = run(pb)
    out.append({"id": "7", "titre": "Plusieurs urgences simultanées", "A": ma, "B": mb,
                "hyp": f"Deux urgences de 1,5 JP chacune en {MOIS[tu]}. A : absorbées gratuitement, elles prennent la "
                       f"place des lots du mois (≈ {eur(perte)} HT perdus). B : facturées par avenant à 900 € HT par JP, "
                       f"en fin de mois, sous 15 jours ; charge du mois portée à {num(pb.jp[tu])} JP pour un plafond de 10.",
                "intenable": "Le plafond de 10 JP et l'occupation à 85 % au plus ; les délais des lots en cours.",
                "mesure": f"Liste fermée des urgences ; arrêt sans autorisation, tout travail en plus par avenant "
                          f"({STRAT}:354, 597) ; au-delà de 90 % des JP réservées avant le 20 du mois, arrêt des travaux non "
                          f"urgents ({STRAT}:593)."})

    # 8. Arrêt d'un fournisseur technique
    tf = tm(STRESS["fournisseur_mois"])
    pa = copy.deepcopy(base_plan)
    perte = 3 * PRIX_PAR_JP_LOT
    for l in pa.lignes:
        if l.categorie == "lots" and ((l.t_facture == tf and "acompte" in l.libelle) or (l.t_facture == tf + 1 and "solde" in l.libelle)):
            l.ht = max(0.0, l.ht * (1 - perte / PRIX["lots_mois_central"]))
    for t in (tf, tf + 1):
        pa.extra[t].append(("Double abonnement pendant la bascule", 300, 0.0))
    pa.ajouter("Malus de 5 % (avoir)", "avoir", tf + 1, tf + 1, -STRESS["malus_socle"] * PRIX["b1"])
    sa, ma = run(pa)
    pb = copy.deepcopy(base_plan)
    perte_b = 1 * PRIX_PAR_JP_LOT
    for l in pb.lignes:
        if l.categorie == "lots" and ((l.t_facture == tf and "acompte" in l.libelle) or (l.t_facture == tf + 1 and "solde" in l.libelle)):
            l.ht = max(0.0, l.ht * (1 - perte_b / PRIX["lots_mois_central"]))
    pb.extra[tf].append(("Outil de remplacement", 150, 0.0))
    sb, mb = run(pb)
    out.append({"id": "8", "titre": "Arrêt d'un fournisseur technique", "A": ma, "B": mb,
                "hyp": f"Un outil central (registre, IA, hébergement) s'arrête en {MOIS[tf]}. A : sans export testé, 3 JP "
                       "de reprise non facturables, deux mois de double abonnement (300 € par mois), deux engagements "
                       "de service manqués (malus de 5 % du socle en avoir). B : exports mensuels testés et mode "
                       "manuel écrit, 1 JP de bascule, un mois d'outil de remplacement.",
                "intenable": "Les engagements de service du socle (comptes rendus, registre) pendant la bascule ; la "
                             "réversibilité promise si les exports ne sont pas testés.",
                "mesure": f"Exports mensuels testés, restauration dans un espace neuf, mode manuel écrit ; comptes ouverts "
                          f"au nom du client ({STRAT}:189, 535)."})

    # 9. Abandon ou retard du projet artistique
    pa = copy.deepcopy(base_plan)
    pa.extra[tm(2)].append(("Achat d'un DGX Spark avancé par Marwin", STRESS["dgx_spark_ht"], 1.0))
    perte = 3 * PRIX_PAR_JP_LOT
    for m in (4, 5):   # 3 JP par mois consacrés à STRATES, non facturés, à la place des lots
        for l in pa.lignes:
            if l.categorie == "lots" and ((l.t_facture == tm(m) and "acompte" in l.libelle) or (l.t_facture == tm(m) + 1 and "solde" in l.libelle)):
                l.ht = max(0.0, l.ht * (1 - perte / PRIX["lots_mois_central"]))
    sa, ma = run(pa)
    sb, mb = run(copy.deepcopy(base_plan))
    out.append({"id": "9", "titre": "Abandon ou retard du projet artistique", "A": ma, "B": mb,
                "hyp": "B (règle retenue) : STRATES, la création avec Medhi et le laboratoire sont hors du CA ; leur "
                       "abandon ou leur retard ne change rien au plan. A (contre-épreuve, si Marwin avait gardé les "
                       f"options des archives) : Marwin avance un DGX Spark (≈ {eur(STRESS['dgx_spark_ht'])} HT) au mois 2 "
                       "et consacre 3 JP par mois aux mois 4 et 5 à STRATES, non facturés, à la place de lots ; le projet "
                       "est ensuite abandonné.",
                "intenable": "Toute avance de matériel, de fabrication ou de temps pour un projet sans financeur écrit ; "
                             f"les documents non corrigés (offre écrite, STRATES v1.1, vernissage, PDF de 13 diapositives) "
                             f"qui laissent croire à un engagement ({STRAT}:31).",
                "mesure": f"Rien d'exploratoire sans financeur écrit, budget plafonné et critère d'arrêt ({STRAT}:190, 644-645) ; "
                          "achats au nom du client ; décision écrite sur Medhi ; documents marqués « retirés »."})

    # 10. Croissance commerciale plus lente
    pa = construire_plan("central", decalage_m1=1, facteur_lots=0.5)
    pa_s = simuler(pa, E)
    ma = _mesures(s_base, pa_s, pa, E)
    E10 = resoudre_enveloppe(pa)
    sb, mb = run(pa, E10)
    out.append({"id": "10", "titre": "Croissance commerciale plus lente", "A": ma, "B": mb,
                "hyp": f"Le cadrage n'est payé qu'à la date butoir (mois 1 = {MOIS[pa.t_m1]}) ; les lots ne représentent que "
                       "1 750 € HT par mois ; aucun second client. A : rémunération du scénario central maintenue. B : "
                       "rémunération recalculée sur le chiffre d'affaires réel.",
                "intenable": f"La rémunération centrale : l'enveloppe soutenable tombe à {eur(E10)} par mois, soit "
                             f"{eur_plage(E10 / 2 / COEF_SAS['haut'], E10 / 2 / COEF_SAS['bas'])} nets par associé ; la cible "
                             "de dépendance (80 % au plus) ; la sortie des autres revenus des associés.",
                "mesure": f"Plancher de prospection de 1,5 à 2,5 JP par mois ; dates butoirs du 15 déc. 2026 et du 31 janv. "
                          f"2027 ({STRAT}:44, 719) ; revenus extérieurs maintenus ; dépendance à assumer par écrit [PR]."})
    return out, s_base


def ecrire_stress(dossier, R, tests, s_base):
    plan, E = R["central"]["plan"], R["central"]["I"]["E"]
    L = ["# Tests de résistance : scénario central, dix-huit mois\n", ENTETE_COMMUN, "\n" + FAITS_NOUVEAUX]
    L.append("\n## Méthode\n")
    hb = range(HORIZON_TRESO)
    tb = min(hb, key=lambda t: s_base["disponible"][t])
    L.append(
        f"- Base : scénario central (`tresorerie-18-mois.md`), novembre 2026 à avril 2028, apport de "
        f"{eur(APPORT['central'])}, enveloppe de rémunération de {eur(E)} par mois dès le mois 4. Point bas de la "
        f"trésorerie disponible de la base : {eur(s_base['disponible'][tb])} en {MOIS[tb]}.\n"
        "- **Besoin de financement maximal** = montant qu'il faudrait apporter en plus pour que la trésorerie disponible "
        "(banque − TVA due) ne devienne jamais négative sur les 18 mois. **Mois critique** = premier mois où la "
        "trésorerie disponible devient négative ; à défaut, mois où la perte par rapport à la base est maximale.\n"
        "- Chaque test est calculé deux fois : **A, sans réaction** (on continue comme prévu) et **B, avec la règle de "
        f"protection** prévue par la stratégie ({STRAT}:524-537). La différence entre A et B mesure ce que la règle "
        "protège.\n"
        f"- Objectif de réserve au mois 12 [PR] : 3 mois de frais fixes et 1 mois de rémunération, soit "
        f"{eur(OBJECTIF_RESERVE_MOIS_FRAIS * sum(FRAIS_MONTANTS['central']) + E)} ({STRAT}:175).\n"
        "- L'IS n'est pas payé dans l'horizon (exercice 2027 soldé en mai 2028) ; il baisse quand le résultat baisse.\n")

    L.append("\n## 1. Synthèse\n")
    rows = []
    for x in tests:
        A, B = x["A"], x["B"]
        rows.append([x["titre"], eur(A["besoin"]), eur(B["besoin"]),
                     f"{eur(A['besoin_charges'])} ; {eur(B['besoin_charges'])}",
                     MOIS[A["t_critique"]] + (" (sous zéro)" if A["premier_negatif"] is not None else ""),
                     f"{eur(A['ecart_max'])} ; {eur(B['ecart_max'])}",
                     f"{eur(A['ecart_fin'])} ; {eur(B['ecart_fin'])}",
                     "oui" if A["manque_objectif"] > 0 else "non"])
    L.append(table(["Test", "Besoin de financement maximal, A (sans réaction)", "Besoin maximal, B (avec la règle)",
                    "Besoin pour garder un mois de charges en caisse, A ; B", "Mois critique (A)",
                    "Perte maximale de trésorerie par rapport à la base, A ; B", "Écart à 18 mois, A ; B",
                    "Réserve cible du mois 12 manquée (A)"], rows))
    L.append("\n\nLecture : le **besoin de financement** est l'apport supplémentaire qui empêche la trésorerie disponible "
             "de devenir négative ; le **besoin pour garder un mois de charges** est plus prudent (frais et rémunérations "
             "du mois toujours couverts). Un besoin de 0 € signifie que l'apport et le coussin du pilote suffisent : cela "
             "ne veut pas dire que le test est sans gravité. La **perte maximale** mesure la trésorerie perdue, au pire "
             "moment, par rapport à la base ; le **mois critique** est le premier mois sous zéro, ou à défaut le mois de "
             "cette perte maximale.\n")

    L.append("\n## 2. Détail des dix tests\n")
    for i, x in enumerate(tests):
        A, B = x["A"], x["B"]
        L.append(f"\n### {x['titre']}\n")
        L.append(f"**Hypothèse** [HY] : {x['hyp']}\n")
        L.append(table(["Mesure [ES]", "A, sans réaction", "B, avec la règle"], [
            ["Besoin de financement maximal (trésorerie jamais négative)", eur(A["besoin"]), eur(B["besoin"])],
            ["Besoin pour garder un mois de charges en caisse", eur(A["besoin_charges"]), eur(B["besoin_charges"])],
            ["Point bas de la trésorerie disponible (mois)", f"{eur(A['point_bas'])} ({MOIS[A['t_bas']]})",
             f"{eur(B['point_bas'])} ({MOIS[B['t_bas']]})"],
            ["Premier mois sous zéro", MOIS[A["premier_negatif"]] if A["premier_negatif"] is not None else "aucun",
             MOIS[B["premier_negatif"]] if B["premier_negatif"] is not None else "aucun"],
            ["Perte maximale par rapport à la base (mois)", f"{eur(A['ecart_max'])} ({MOIS[A['t_ecart']]})",
             f"{eur(B['ecart_max'])} ({MOIS[B['t_ecart']]})"],
            ["dont crédit de TVA au point bas (remboursable sur demande, non compté)", eur(A["credit_bas"]), eur(B["credit_bas"])],
            ["Trésorerie disponible au mois 12", eur(A["dispo_m12"]), eur(B["dispo_m12"])],
            ["Manque par rapport à la réserve cible du mois 12", eur(A["manque_objectif"]), eur(B["manque_objectif"])],
            ["Écart de trésorerie à 18 mois avec la base", eur(A["ecart_fin"]), eur(B["ecart_fin"])],
        ]))
        L.append(f"\n\n**Engagements devenus intenables** : {x['intenable']}\n\n**Mesure de protection** [PR] : {x['mesure']}\n")

    L.append("\n## 3. Ce que montrent ces tests\n")
    pire = max(tests, key=lambda x: x["A"]["besoin"])
    L.append(
        f"- Le test le plus coûteux sans réaction est « {pire['titre']} » : besoin de {eur(pire['A']['besoin'])}, "
        f"trésorerie sous zéro à partir de {MOIS[pire['A']['t_critique']]}. Avec la règle, le besoin tombe à "
        f"{eur(pire['B']['besoin'])}.\n"
        "- La protection principale n'est pas la réserve, mais **la règle « pas de rémunération sans encaissement »** "
        "et l'arrêt rapide des frais : elles transforment un besoin de financement en baisse de revenu des associés.\n"
        f"- Sans réaction, {len([x for x in tests if x['A']['besoin'] > 0])} situations rendent la trésorerie négative : "
        + " ; ".join(f"{x['titre'].lower()}, {eur(x['A']['besoin'])}" for x in tests if x["A"]["besoin"] > 0)
        + ". Avec la règle, " + ("un besoin ne subsiste que pour : " + " ; ".join(
            f"{x['titre'].lower()}, {eur(x['B']['besoin'])}, dont {eur(min(x['B']['besoin'], x['B']['credit_bas']))} "
            "de crédit de TVA qu'un remboursement demandé à temps couvrirait" for x in tests if x["B"]["besoin"] > 0)
            if any(x["B"]["besoin"] > 0 for x in tests) else "aucune ne laisse de besoin")
        + ".\n"
        "- Dans tous ces cas, la règle protège la société en reportant le choc sur le revenu des associés : "
        "**Morgan et Mathys doivent garder d'autres revenus** jusqu'au deuxième renouvellement du socle "
        f"({STRAT}:771).\n"
        "- Le projet artistique est sans effet tant qu'il reste hors du chiffre d'affaires et qu'aucune avance n'est "
        "faite ; il redevient le premier risque si Marwin avance du matériel ou du temps.\n")
    L.append("\n## 4. Limites\n")
    L.append(
        "- Les tests sont appliqués un par un ; leur cumul (par exemple un retard et une absence) aggraverait les besoins.\n"
        "- Les retards sont supposés durables à partir du mois 4 ; un retard ponctuel coûte moins.\n"
        f"- Les comportements de paiement de l'entité de GianLuca sont [IN] ({STRAT}:467).\n"
        "- Les règles B sont des propositions [PR] ; elles ne protègent que si elles sont écrites au contrat et au "
        "pacte, et appliquées.\n"
        "- Le crédit de TVA (TVA payée sur les frais quand plus rien n'est encaissé) n'est pas compté dans la trésorerie "
        "disponible : les besoins sont donc légèrement surestimés quand l'activité s'arrête ; la ligne « dont crédit de "
        "TVA » de chaque test le chiffre. Un remboursement se demande auprès du service des impôts des entreprises.\n"
        "- L'IS n'est jamais payé dans l'horizon (mai 2028) : une rupture n'en économise que la provision.\n")
    _ecrire(dossier, "stress-tests.md", "\n".join(L))


# =====================================================================================
# 15. ÉCRITURE : structures.md
# =====================================================================================
def comparer_reference(ca, frais):
    """Contrôle : reproduit la ligne A et B de DROIT:118-125 (tout le disponible en rémunération)."""
    C = (ca - frais) / 2
    return C - cotisations_tns(C), (C / COEF_SAS["haut"], C / COEF_SAS["bas"])


def ecrire_structures(dossier, R):
    L = ["# SAS ou SARL : comparaison sur les mêmes hypothèses économiques\n", ENTETE_COMMUN]
    L.append("\n## 0. Conclusion\n")
    c = R["central"]
    L.append(
        f"- **Recommandation inchangée : SAS à l'IS** [PR] ({STRAT}:543 ; {DROIT}:209-235), à confirmer par une "
        "simulation officielle de l'expert-comptable.\n"
        f"- À enveloppe égale, la SARL (deux cogérants TNS) laisse plus de net : en central, "
        f"{eur(c['nets']['sarl_net'])} contre {eur_plage(c['nets']['sas']['haut'], c['nets']['sas']['bas'])} par associé sur "
        f"les neuf mois rémunérés, soit {eur_plage(c['nets']['sarl_net'] - c['nets']['sas']['bas'], c['nets']['sarl_net'] - c['nets']['sas']['haut'])} "
        "de plus [ES].\n"
        "- Mais la SARL coûte des cotisations même sans rémunération (forfaits de première année, minimum ensuite), "
        "protège moins (indemnités, retraite complémentaire), gêne l'entrée d'un investisseur et bloque plus vite à "
        "50/50. Or, au 4 novembre, **aucune rémunération n'est financée par un contrat signé** [FV] : c'est le cas où la "
        f"SAS est la plus sûre ({DROIT}:216).\n"
        f"- La SARL ne redevient préférable que si les trois conditions de {STRAT}:562 sont réunies : aucun investisseur "
        "avant 24 mois, un contrat signé d'au moins 120 000 € par an, aucun associé salarié ailleurs.\n")

    L.append("\n## 1. Hypothèses identiques pour les deux formes\n")
    L.append(
        "- Même chiffre d'affaires, mêmes frais, même démarrage, même réserve, même IS : l'**enveloppe de rémunération** "
        "(coût total pour la société) est celle que calcule le modèle pour chaque scénario (`scenarios.md`, section 3). "
        "Seul change le partage de cette enveloppe entre cotisations et net.\n"
        f"- Deux associés à 50/50, tous deux dirigeants. SARL : cogérants, donc TNS [FV] ({DROIT}:109) ; SAS : président "
        f"et directeur général assimilés salariés [FV] ({R1}:23).\n"
        f"- SAS : coût = 1,7 à 1,9 fois le net [HY] ({DROIT}:98). SARL : barème F38152 « revenus 2025 », assiette à 74 % "
        f"du coût, plancher et plafond de l'abattement ignorés [ES] ({DROIT}:97 ; {VR1}:20).\n"
        f"- IS identique (rémunérations et cotisations déductibles dans les deux cas) : 15 % jusqu'à 42 500 € [FV] ({DROIT}:142).\n"
        "- Pas d'ACRE, d'ARE, d'ARCE, de prévoyance ni de mutuelle ; **impôt sur le revenu non calculé** [IN].\n")

    L.append("\n## 2. Résultats par scénario (neuf mois rémunérés, mois 4 à 12)\n")
    rows = []
    for n in ORDRE:
        r = R[n]
        nb = r["I"]["nb_mois_remu"]
        lo, hi = r["nets_lo"], r["nets_hi"]   # frais hauts / frais bas
        rows.append([
            SCENARIOS[n]["libelle"],
            eur_plage(r["E_lo"], r["E_hi"]),
            eur_plage(lo["sas"]["haut"], hi["sas"]["bas"]),
            eur_plage(lo["sas"]["haut"] / nb, hi["sas"]["bas"] / nb),
            eur_plage(lo["sarl_net"], hi["sarl_net"]),
            eur_plage(lo["sarl_net"] / nb, hi["sarl_net"] / nb),
            eur_plage(lo["sarl_net"] - lo["sas"]["central"], hi["sarl_net"] - hi["sas"]["central"]),
            eur_plage(lo["sarl_regul"], hi["sarl_regul"]),
        ])
    L.append(table(["Scénario", "Enveloppe mensuelle (deux associés)", "SAS : net par associé sur 9 mois",
                    "SAS : net par mois", "SARL : net par associé sur 9 mois", "SARL : net par mois",
                    "Écart SARL − SAS (coefficient 1,8)", "SARL : régularisation en année 2"], rows))
    L.append("\n\nFourchettes : frais hauts (× 1,25) et démarrage haut, puis frais bas (× 0,8) et démarrage bas ; pour "
             "la SAS, en plus, coefficient 1,9 puis 1,7. Une régularisation négative est un remboursement des forfaits "
             "trop payés [ES].\n")

    L.append("\n## 3. Sans rémunération : ce que coûte chaque forme\n")
    L.append(table(["Situation", "SARL (deux cogérants TNS)", "SAS (président et directeur général)", "Source"], [
        ["Mois 1 à 3 (aucune rémunération)", "Forfaits de début d'activité ≈ 3 600 € par gérant et par an, régularisés "
         "ensuite ; minimum ≈ 1 300 € par an et par gérant", "0 €, sans droit social", f"[FV/ES] {DROIT}:111"],
        ["Variante basse du prudent (arrêt après le cadrage)", "Forfaits ≈ 7 200 € avancés pour les deux la première "
         "année, ramenés ensuite au minimum (≈ 2 500 € par an pour les deux), sans aucun revenu",
         "0 €", f"[ES] {DROIT}:182"],
        ["Associé salarié ailleurs", "Le gérant reste redevable du minimum", "Mandat non rémunéré possible sans cotisation",
         f"[FV] {DROIT}:159"],
        ["Trésorerie sociale", "Forfaits l'année 1, régularisation l'année 2 : à provisionner", "Cotisations payées chaque mois "
         "avec le salaire, pas de régularisation", f"[ES] {DROIT}:187-195"],
    ]))

    L.append("\n\n## 4. Dividendes\n")
    # Contrôle du 4 nov. 2026 : la version précédente distribuait tout le bénéfice de l'année (réserve conservée),
    # y compris l'excédent des mois 1 à 3 que le scénario « salaire » laisse dans la société ; elle comparait donc
    # des ressources inégales (+1 900 € par associé en central). Ligne principale : à ressources égales.
    rows = []
    for n in ORDRE:
        r = R[n]
        I = r["I"]
        nb = I["nb_mois_remu"]
        pool = nb * I["E"]                                   # enveloppe de 9 mois remplacée par des dividendes
        d_is = impot_societes(I["resultat"] + pool) - impot_societes(I["resultat"])
        net_eq = (pool - d_is) / 2 * (1 - PFU)
        sas = r["nets"]["sas"]
        benef = I["resultat"] + I["remu"]                    # variante : tout le bénéfice distribué
        dispo = max(0.0, benef - impot_societes(benef) - I["reserve"])
        r["div_egal"], r["div_tout"] = net_eq, dispo / 2 * (1 - PFU)
        rows.append([SCENARIOS[n]["libelle"], eur(pool), eur(d_is), eur(net_eq),
                     eur_plage(sas["haut"], sas["bas"]), eur(dispo / 2 * (1 - PFU))])
    L.append(table(["Scénario (SAS)", "Enveloppe des mois 4 à 12 versée en dividendes au lieu de salaires (deux associés)",
                    "IS supplémentaire", "Dividende net par associé après PFU de 31,4 % (donc après IR)",
                    "Pour comparaison : salaire net SAS par associé, avant IR (coefficient 1,9 à 1,7)",
                    "Variante non comparable : tout le bénéfice distribué, réserve conservée, net après PFU"], rows))
    c_ = R["central"]
    L.append(
        "\n\nLecture [ES] : **à ressources égales**, le dividende net après PFU (qui comprend 12,8 % d'IR) est à peu "
        f"près égal au salaire net de SAS **avant** IR au coefficient central de 1,8 (central : {eur(c_['div_egal'])} "
        f"contre {eur(c_['nets']['sas']['central'])}) ; il ne gagne que l'IR que supporterait le salaire. En ambitieux, "
        f"où une partie du bénéfice passe à 25 % d'IS, il fait moins bien ({eur(R['ambitieux']['div_egal'])} contre "
        f"{eur(R['ambitieux']['nets']['sas']['central'])}). La dernière colonne distribue en plus l'excédent "
        "des mois 1 à 3 que les scénarios « salaire » laissent dans la société : elle ne compare pas des ressources "
        "égales et ne doit pas servir d'argument. Le dividende n'est versé "
        "qu'**après la clôture et l'approbation "
        "des comptes** (au plus tôt au printemps 2028 pour l'exercice 2027 [HY]), il n'ouvre **aucun droit social** "
        f"(ni retraite, ni indemnités) et il dépend du bénéfice ({DROIT}:129-132, 144). Il ne finance donc pas la vie "
        "des associés pendant la première année ; un mélange « petit salaire et dividendes » est à faire simuler par "
        "l'expert-comptable. IS calculé avec le seuil de 42 500 € sur douze mois : un premier exercice de 13 ou 14 mois "
        "relèverait ce seuil au prorata et réduirait l'IS de ce tableau de 350 à 700 € [ES]. "
        "En SARL, les dividendes des cogérants au-delà de 10 % du capital, "
        f"des primes et des comptes courants supportent les cotisations TNS : pas de levier avec un petit capital [FV] "
        f"({DROIT}:145).\n")

    L.append("\n## 5. Contrôle : reproduction de la synthèse juridique\n")
    rows = []
    for ca, fr, ref_a, ref_b in ((120000, 20000, "≈ 34 500", "26 300 à 29 400"), (180000, 30000, "≈ 51 400", "39 500 à 44 100")):
        a, b = comparer_reference(ca, fr)
        rows.append([eur(ca), eur(a), ref_a + " €", eur_plage(*b), ref_b + " €"])
    L.append(table(["CA HT annuel (frais = 1/6)", "SARL, tout en rémunération (modèle)", f"SARL ({DROIT}:123-124)",
                    "SAS, tout en salaire (modèle)", f"SAS ({DROIT}:123-124)"], rows))
    L.append("\n\nLe modèle reproduit les fourchettes de la synthèse juridique : les deux calculs reposent sur les mêmes "
             "barèmes et la même méthode.\n")

    L.append("\n## 6. Ce que les chiffres ne disent pas\n")
    L.append(table(["Critère", "SARL", "SAS", "Source"], [
        ["Indemnités journalières maladie", "Plafond 65,84 € par jour, 3 jours de carence", "Plafond 41,95 € par jour", f"[FV] {DROIT}:113"],
        ["Retraite", "Régimes des indépendants", "Régime général et Agirc-Arrco : en général plus de droits à coût égal", f"[FV/IN] {DROIT}:114"],
        ["Chômage", "Aucun", "Aucun", f"[FV] {DROIT}:115"],
        ["Blocage à 50/50", "Décisions ordinaires bloquées sans accord", "Médiation, tiers expert, offre alternative prévues aux statuts", f"[HY] {DROIT}:155"],
        ["Entrée d'un investisseur (dont GianLuca)", "Agrément ; droits de cession de 3 % après abattement", "Libre selon les statuts ; 0,1 %", f"[FV] {DROIT}:165-166"],
        ["Coût de création (statuts, pacte)", "≈ 1 500 à 4 000 € HT", "≈ 2 000 à 5 000 € HT", f"[ES] {DROIT}:180"],
    ]))
    L.append("\n\n## 7. Questions à l'expert-comptable (avant toute décision)\n")
    L.append(
        "1. Simulations officielles SAS et SARL sur les trois scénarios de `scenarios.md`, avec les taux 2026 définitifs, "
        f"puis ceux de 2027 ({DROIT}:200).\n"
        f"2. Coût réel d'un président et d'un directeur général rémunérés : taux, réduction dégressive unique, AT/MP ({DROIT}:201).\n"
        "3. Forfaits TNS de première année si la société est créée fin 2026 ou début 2027, et montant de la régularisation.\n"
        "4. Régime de TVA (réel normal mensuel ou réel simplifié), date de création et date de clôture.\n"
        "5. Déductibilité, dans la société, des frais engagés avant l'immatriculation (dont le conseil sur la fuite).\n"
        f"6. ACRE, si l'un des deux associés est éligible ({DROIT}:205).\n")
    _ecrire(dossier, "structures.md", "\n".join(L))


# =====================================================================================
# 16. CONTRÔLES DE COHÉRENCE
# =====================================================================================
def controles(R, tests, s_base):
    erreurs = []
    def verifier(cond, msg):
        if not cond:
            erreurs.append(msg)
    for n, r in list(R.items()):
        s, plan = r["s"], r["plan"]
        cash = 0.0
        for t in range(N_SIM):
            # identité de trésorerie
            cash += (s["apport"][t] + s["enc_ttc"][t] - s["frais_ttc"][t] - s["dem_ttc"][t] - s["st_ttc"][t]
                     - s["extra_ttc"][t] - s["remu"][t] - s["tva_versee"][t] - s["is_paye"][t])
            verifier(abs(cash - s["cash"][t]) < 1e-6, f"{n} : identité de trésorerie fausse en {MOIS[t]}")
            verifier(abs(s["enc_ttc"][t] - 1.2 * s["enc_ht"][t]) < 1e-6, f"{n} : TTC ≠ 1,2 × HT en {MOIS[t]}")
            cats = sum(s["enc_ttc_" + c][t] for c in ("cadrage", "pilote", "socle", "lots", "exploitation",
                                                      "autre_client", "avenant", "avoir"))
            verifier(abs(cats - s["enc_ttc"][t]) < 1e-6, f"{n} : somme des catégories ≠ total en {MOIS[t]}")
            verifier(abs(s["enc_ht_gl"][t] + s["enc_ht_autre"][t] - s["enc_ht"][t]) < 1e-6, f"{n} : clients ≠ total")
            for k in ("frais_ttc", "dem_ttc", "st_ttc", "remu", "tva_versee", "tva_due", "credit_tva", "is_paye", "jp"):
                verifier(s[k][t] >= -1e-9, f"{n} : {k} négatif en {MOIS[t]}")
            verifier(s["enc_pond_ttc"][t] <= s["enc_ttc"][t] + 1e-6, f"{n} : pondéré > total en {MOIS[t]}")
        # identité de TVA : collectée − déductible = reversée + due − crédit
        coll, ded, vers = sum(s["tva_coll"]), sum(s["tva_ded"]), sum(s["tva_versee"])
        verifier(abs((coll - ded) - (vers + s["tva_due"][-1] - s["credit_tva"][-1])) < 1e-6, f"{n} : identité de TVA fausse")
        # rémunération : jamais de net au-delà du plafond, jamais négative
        verifier(0 <= r["I"]["E"] <= 2 * NET_PLAFOND_ASSOCIE * COEF_SAS["central"] + 1e-6, f"{n} : enveloppe hors bornes")
        # la règle de rémunération laisse au moins la réserve et l'IS en trésorerie sur les mois 4 à 12
        f4 = fenetre(plan, MOIS_DEBUT_REMU, 12)
        surplus = sum(s["enc_ht"][t] - s["frais_ht"][t] - s["st_ht"][t] - s["extra_ht"][t] - s["remu"][t] for t in f4)
        verifier(surplus + 1 >= sum(RESERVE * s["enc_ht"][t] for t in f4) + r["I"]["is"] - 1e-6 or r["I"]["E"] == 0,
                 f"{n} : la rémunération entame la réserve ou l'IS")
        # fourchettes ordonnées
        if "Ib" in r:
            verifier(r["Ih"]["remu"] <= r["I"]["remu"] + 1e-6 <= r["Ib"]["remu"] + 2e-6, f"{n} : fourchette de rémunération")
            verifier(r["net_plage"][0] <= r["net_plage"][1], f"{n} : plage de net inversée")
    # le décalage de TVA est un vrai paramètre (contrôle du 4 nov. 2026) : à 0, 1 ou 2 mois, l'identité de TVA
    # tient et la trésorerie disponible (banque − TVA due) ne change pas ; seule la trésorerie en banque bouge
    global TVA_DECALAGE
    ref_lag, dispo_lag = TVA_DECALAGE, {}
    try:
        for lag in (0, 1, 2):
            TVA_DECALAGE = lag
            s_ = simuler(R["central"]["plan"], R["central"]["I"]["E"])
            ecart = (sum(s_["tva_coll"]) - sum(s_["tva_ded"])) - (sum(s_["tva_versee"]) + s_["tva_due"][-1] - s_["credit_tva"][-1])
            verifier(abs(ecart) < 1e-6, f"identité de TVA fausse avec un décalage de {lag} mois")
            dispo_lag[lag] = s_["disponible"]
    finally:
        TVA_DECALAGE = ref_lag
    verifier(all(abs(dispo_lag[0][t] - dispo_lag[2][t]) < 1e-6 for t in range(N_SIM)),
             "la trésorerie disponible dépend du décalage de TVA")
    # trésorerie de base du central jamais négative
    verifier(min(R["central"]["s"]["disponible"][:HORIZON_TRESO]) >= 0, "central : trésorerie disponible négative dans la base")
    # cohérence des CA avec la stratégie (écart toléré : 10 %)
    for n in ORDRE:
        ca, ref = R[n]["I"]["fact_ht"], SCENARIOS[n]["strategie"]["ca12"]
        verifier(abs(ca - ref) / ref <= 0.10, f"{n} : CA sur 12 mois ({ca:.0f}) à plus de 10 % de la stratégie ({ref})")
    # capacité : central sous le plafond de 10 JP, chaque scénario sous sa capacité
    for n in ORDRE:
        I = R[n]["I"]
        verifier(I["jp_max"] <= SCENARIOS[n]["capacite"] + 1e-6, f"{n} : JP vendues au-delà de la capacité ({I['jp_max']:.1f})")
    verifier(R["central"]["I"]["jp_max"] <= SCENARIOS["central"]["plafond"] + 1e-6, "central : plafond de 10 JP dépassé")
    # arrondis : les totaux des colonnes arrondies sont égaux aux totaux arrondis
    a = series_affichees(R["central"]["s"], HORIZON_TRESO)
    for k in FLUX:
        verifier(sum(a[k]) == r100(sum(R["central"]["s"][k][:HORIZON_TRESO])), f"arrondis cumulés faux pour {k}")
    verifier(a["cash"][-1] == sum(a["flux"]), "trésorerie arrondie ≠ somme des flux arrondis")
    # contrôle croisé avec la synthèse juridique (± 2 %)
    a, b = comparer_reference(120000, 20000)
    verifier(abs(a - 34493) / 34493 < 0.02, "TNS : écart avec la synthèse juridique à 120 k€")
    a, b = comparer_reference(180000, 30000)
    verifier(abs(a - 51420) / 51420 < 0.02, "TNS : écart avec la synthèse juridique à 180 k€")
    # tests : la règle B ne doit jamais coûter plus que A pour les tests où elle réduit les sorties
    for x in tests:
        if x["id"].startswith(("1-", "2-", "3", "6")):
            verifier(x["B"]["besoin"] <= x["A"]["besoin"] + 1e-6, f"test {x['id']} : la règle aggrave le besoin")
    return erreurs


# =====================================================================================
# 17. PROGRAMME PRINCIPAL
# =====================================================================================
def _ecrire(dossier, nom, texte):
    with open(os.path.join(dossier, nom), "w", encoding="utf-8") as f:
        f.write(texte.rstrip() + "\n")


def calculer():
    R = {}
    for n in ORDRE:
        plan = construire_plan(n)
        E = resoudre_enveloppe(plan)
        I, s = indicateurs_12_mois(plan, E)
        dlo, dhi = DEMARRAGE_FOURCHETTE[n]
        dem_c = sum(x[1] for x in DEMARRAGE[n])
        plan_h = construire_plan(n, frais_mult=FRAIS_FOURCHETTE[1], dem_mult=dhi / dem_c)   # frais hauts
        plan_b = construire_plan(n, frais_mult=FRAIS_FOURCHETTE[0], dem_mult=dlo / dem_c)   # frais bas
        E_h, E_b = resoudre_enveloppe(plan_h), resoudre_enveloppe(plan_b)
        Ih, _ = indicateurs_12_mois(plan_h, E_h)
        Ib, _ = indicateurs_12_mois(plan_b, E_b)
        nb = I["nb_mois_remu"]
        nets = nets_par_associe(E, nb)
        nets_lo, nets_hi = nets_par_associe(E_h, nb), nets_par_associe(E_b, nb)
        R[n] = {"plan": plan, "s": s, "I": I, "Ih": Ih, "Ib": Ib, "E_lo": E_h, "E_hi": E_b,
                "nets": nets, "nets_lo": nets_lo, "nets_hi": nets_hi,
                "net_plage": (nets_lo["sas"]["haut"] / nb, nets_hi["sas"]["bas"] / nb),
                "net_central": nets["sas"]["central"] / nb,
                "net_sarl_plage": (nets_lo["sarl_net"] / nb, nets_hi["sarl_net"] / nb),
                "seuils": seuils_jp(I, E, SCENARIOS[n]["etp"])}
    # variantes
    pv = construire_plan("prudent", variante="basse")
    Iv, sv = indicateurs_12_mois(pv, 0.0)
    R["variante_basse"] = {"plan": pv, "s": sv, "I": Iv,
                           "premier_negatif": next((t for t in range(N_SIM) if sv["disponible"][t] < 0), None)}
    ps = construire_plan("central", variante="second_client")
    Es = resoudre_enveloppe(ps)
    Is, ss = indicateurs_12_mois(ps, Es)
    nb = Is["nb_mois_remu"]
    ps_h = construire_plan("central", variante="second_client", frais_mult=FRAIS_FOURCHETTE[1], dem_mult=7000 / 6000)
    ps_b = construire_plan("central", variante="second_client", frais_mult=FRAIS_FOURCHETTE[0], dem_mult=5000 / 6000)
    R["variante_second"] = {"plan": ps, "s": ss, "I": Is, "net_central": nets_par_associe(Es, nb)["sas"]["central"] / nb,
                            "net_plage": (resoudre_enveloppe(ps_h) / 2 / COEF_SAS["haut"], resoudre_enveloppe(ps_b) / 2 / COEF_SAS["bas"])}
    # Sensibilité (contrôle du 4 nov. 2026) : prime de RC professionnelle payée en une fois avant la 1re prestation
    base, E_c = R["central"]["plan"], R["central"]["I"]["E"]
    cle = "Assurances (RC pro avec volets IA, cyber, données)"
    sens = []
    for mensuel in (FRAIS_MONTANTS["central"][list(FRAIS_LIGNES).index(cle)], 250):
        pc = copy.deepcopy(base)
        for t in range(N_SIM):
            if cle in pc.frais[t]:
                pc.frais[t][cle] = 0.0
        for t in (pc.t_m1 - 1, pc.t_m1 + 11):
            if 0 <= t < N_SIM:
                pc.extra[t].append(("Prime annuelle de RC professionnelle payée d'avance", 12 * mensuel, 0.0))
        s2 = simuler(pc, E_c)
        tb = min(range(HORIZON_TRESO), key=lambda t: s2["disponible"][t])
        sens.append((12 * mensuel, s2["disponible"][tb], tb))
    R["central"]["sensib_rc"] = sens
    # Voies de pilote moins chères (contrôle du 4 nov. 2026) : le central retient B0 + un lot (13 000 € HT) ;
    # STRAT:247-249 offre aussi C2 seul (6 000 € HT) ou C6 seul (7 500 € HT)
    voies = []
    for lib, prix in (("C2 seul", PRIX["lot_pilote"]), ("C6 seul", 7500)):
        pv_ = copy.deepcopy(base)
        pv_.lignes = [l for l in pv_.lignes if l.categorie != "pilote"]
        for t in (pv_.tm(2), pv_.tm(3)):
            pv_.jp[t] -= JP["b0"] + PRIX["lot_pilote"] / PRIX_PAR_JP_LOT / 2
        _lot(pv_, "Pilote " + lib, 2, prix, 1, PROBA["central"]["pilote"], cat="pilote")
        Ev = resoudre_enveloppe(pv_)
        Iv_, _ = indicateurs_12_mois(pv_, Ev)
        voies.append((lib, prix, Iv_["fact_ht"], Iv_["libre"], Ev))
    R["central"]["voies_pilote"] = voies
    tests, s_base = tests_de_resistance(R["central"]["plan"], R["central"]["I"]["E"])
    return R, tests, s_base


def main():
    ap = argparse.ArgumentParser(description="Modèle financier Marwin Tech × GianLuca Carlone (audit du 4 nov. 2026)")
    ap.add_argument("--sortie", default=os.path.dirname(os.path.abspath(__file__)))
    args = ap.parse_args()
    os.makedirs(args.sortie, exist_ok=True)
    R, tests, s_base = calculer()
    erreurs = controles(R, tests, s_base)
    if erreurs:
        print("CONTRÔLES EN ÉCHEC :")
        for e in erreurs:
            print(" -", e)
        raise SystemExit(1)
    ecrire_scenarios(args.sortie, R)
    ecrire_tresorerie(args.sortie, R)
    ecrire_stress(args.sortie, R, tests, s_base)
    ecrire_structures(args.sortie, R)
    print("Contrôles de cohérence : tous passés.")
    for n in ORDRE:
        I = R[n]["I"]
        print(f"{n:10s} CA facturé M1-M12 {eur(I['fact_ht'])} HT ; enveloppe {eur(I['E'])}/mois ; "
              f"net SAS {eur_plage(*R[n]['net_plage'])} ; IS {eur(I['is'])} ; dispo M12 {eur(I['disponible'])} ; "
              f"libre {eur(I['libre'])} ; seuil {num(R[n]['seuils']['frais'])} JP")
    for x in tests:
        print(f"test {x['id']:5s} besoin A {eur(x['A']['besoin'])} / charges {eur(x['A']['besoin_charges'])} "
              f"(critique {MOIS[x['A']['t_critique']]}, perte max {eur(x['A']['ecart_max'])}) ; "
              f"B {eur(x['B']['besoin'])} / charges {eur(x['B']['besoin_charges'])} ; écart 18 m A {eur(x['A']['ecart_fin'])} B {eur(x['B']['ecart_fin'])}")
    print("Fichiers écrits dans", args.sortie)


if __name__ == "__main__":
    main()
