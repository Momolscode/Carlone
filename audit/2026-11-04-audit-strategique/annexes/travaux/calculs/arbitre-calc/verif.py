# Verifications de l'arbitre final (4 nov. 2026). Tous les resultats sont des [ES].
import itertools

print("== 1. Cout complet d'une JP facturable (SAS, reserve 10 %) ==")
# (part ETP x net cible x coef + frais fixes) / JP facturables / 0.9
cas = {"prudent": (0.75, 7), "central": (1.15, 12), "central_10JP": (1.15, 10), "haut": (1.8, 20)}
for nom, (etp, jp) in cas.items():
    for net in (2500,):
        lo = (etp*net*1.7 + 1500)/jp/0.9
        hi = (etp*net*1.9 + 2500)/jp/0.9
        print(f"{nom:13s} net {net}/ETP : {lo:6.0f} a {hi:6.0f} EUR/JP")

print("\n== 2. Seuil ou un coordinateur salarie devient moins cher ==")
for cout_emp in (5380, 6149):
    for prix in (750, 800, 900):
        print(f"cout employeur {cout_emp} / prix {prix} -> {cout_emp/prix:4.1f} JP/mois")

print("\n== 3. Cadrage 8 JP : marge sur cout complet central (591-737) ==")
for prix in (6000, 6500, 7000, 7500):
    for c in (591, 737):
        print(f"prix {prix} cout/JP {c}: marge {(prix-8*c)/prix*100:5.1f} %  ({prix/8:.0f} EUR/JP)")

print("\n== 4. Prix des projets supplementaires du socle (1 a 1,5 JP de suivi) ==")
for p in (1000, 1200):
    print(f"+{p} EUR/projet : {p/1.5:.0f} a {p/1.0:.0f} EUR/JP")
print("Socle + 2 projets 4500 EUR pour 4,5 a 5,5 JP :", round(4500/5.5), "a", round(4500/4.5), "EUR/JP")
print("Socle + 4 projets 6900 EUR pour 6,5 a 9 JP  :", round(6900/9), "a", round(6900/6.5), "EUR/JP")

print("\n== 5. Offres forfaitaires : EUR par JP estimee ==")
offres = {"cadrage 6500/8": 6500/8, "socle pilote 3500/3,5": 3500/3.5, "pilote commercial 5500/6-7": (5500/7, 5500/6),
          "outillage 7000/9": 7000/9, "plancher cadrage 6000/8": 6000/8}
for k, v in offres.items(): print(k, v)

print("\n== 6. Scenarios a 12 mois ==")
def scenario(nom, mois, frais_fixes, demarrage, apport, coef, debut_remu, net_cible, soustrait=None, autre_client=None):
    # mois : liste de CA HT factures par mois (encaissement suppose le mois meme, sauf decalage teste)
    ca = sum(mois)
    ca_autre = sum(autre_client) if autre_client else 0
    st = sum(soustrait) if soustrait else 0
    tres = apport - demarrage
    bas = tres
    remu_tot = 0
    for i, m in enumerate(mois, start=1):
        a = autre_client[i-1] if autre_client else 0
        s = soustrait[i-1] if soustrait else 0
        recette = m + a
        reserve = 0.10*recette
        dispo = recette - reserve - frais_fixes - s
        remu = 0
        if i >= debut_remu and dispo > 0:
            remu = min(dispo, 2*net_cible*coef)
        tres += recette - frais_fixes - s - remu
        remu_tot += remu
        bas = min(bas, tres)
    nets = remu_tot/coef/2
    mois_remu = max(1, len(mois)-debut_remu+1)
    return dict(nom=nom, ca_carlone=ca, ca_autre=ca_autre, part=ca/(ca+ca_autre) if ca+ca_autre else 0,
                net_moyen_associe_mois_remunere=nets/mois_remu, tres_fin=tres, point_bas=bas, soustrait=st)

# Prudent : cadrage en fevrier 2027 (M1), socle leger 3000 des M3, un lot 4500 par trimestre
prud = [3250, 3250, 3000, 3000, 3000+4500, 3000, 3000, 3000+4500, 3000, 3000, 3000+4500, 3000]
# Central : cadrage 6500 (50/50) M1-M2 ; pilote socle 3500 x2 (M2-M3) + lot 5500 (40/60 : M2, M3) ; M4-M12 socle 4500 + lots ~3500/mois en moyenne
cent = [3250, 3250+3500+2200, 3500+3300] + [4500+3500]*9
# Variante centrale avec second client 2000 EUR/mois des M7
autre = [0]*6 + [2000]*6
# Ambitieux : cadrage 7000 en dec. 2026 ; pilote avec deux lots ; M4-M12 socle+3 projets 5700 + lots 6000 + exploitation 1500 ; sous-traitance 2 a 4 JP a 500
amb = [3500, 3500+3500+4400, 3500+6600+2200] + [5700+6000+1500]*9
st_amb = [0, 0, 0] + [1500]*9
for coef in (1.7, 1.9):
    for nom, m, ff, dem, app, debut, net, st, ac in [
        ("prudent", prud, 1500, 5000, 8000, 4, 2500, None, None),
        ("central", cent, 2000, 6000, 10000, 4, 2500, None, None),
        ("central+2e client", cent, 2000, 6000, 10000, 4, 2500, None, autre),
        ("ambitieux", amb, 2800, 7000, 12000, 4, 2500, st_amb, None)]:
        r = scenario(nom, m, ff, dem, app, coef, debut, net, st, ac)
        print(f"coef {coef} {r['nom']:18s} CA Carlone {r['ca_carlone']:7.0f} autre {r['ca_autre']:6.0f} part {r['part']*100:4.0f} % "
              f"net/associe/mois remunere {r['net_moyen_associe_mois_remunere']:6.0f} tres fin {r['tres_fin']:7.0f} point bas {r['point_bas']:7.0f}")
print("CA regime central (M4-M12):", 4500+3500, " ; prudent:", 3000+1500, " ; ambitieux:", 5700+6000+1500)
print("JP vendus central regime ~ socle 4,5-5 + lots 3500/850 =", 4.5+3500/850, "a", 5+3500/800)
print("JP vendus ambitieux regime ~ socle 6-7 + lots 6000/900 + expl 1-2 =", 6+6000/900+1, "a", 7+6000/850+2)

print("\n== 7. Exposition maximale (central) ==")
print("60 % d'un lot de 5500 :", 0.6*5500, "; 15 jours de socle 4500 :", 4500/2, "; total", 0.6*5500+4500/2)

print("\n== 8. Marge par offre sur cout complet (12 JP : 591-737 ; 10 JP : 710-885) ==")
offres = [("A cadrage", 6500, 8, 8), ("A reduit", 4800, 6, 6), ("B0 socle pilote/mois", 3500, 3, 4), ("B1 socle+2/mois", 4500, 4.5, 5.5),
          ("B2 socle+4/mois", 6900, 6.5, 9), ("C2 pilote commercial", 5500, 6, 7), ("C6 outillage", 7000, 8, 9),
          ("C lot type 6 JP", 6*800*1.125, 6, 6), ("E avenant 1 JP", 900, 1, 1)]
for nom, prix, jlo, jhi in offres:
    res = []
    for (clo, chi) in ((591, 737), (710, 885)):
        mmin = (prix - jhi*chi)/prix*100
        mmax = (prix - jlo*clo)/prix*100
        res.append(f"{mmin:5.0f} a {mmax:4.0f} %")
    print(f"{nom:22s} {prix:7.0f} EUR ; {prix/jhi:5.0f}-{prix/jlo:5.0f} EUR/JP ; marge 12 JP : {res[0]} ; 10 JP : {res[1]}")

print("\n== 9. Cout annuel pour GianLuca (central) et comparaison ==")
print("Marwin central 12 mois ~ 91 000 HT ; TTC si TVA non recuperable :", 91000*1.2)
print("Offre d'archives 6 mois : 90 000 HT ; TTC", 90000*1.2)
print("Assistant non cadre : 2249-2808 /mois -> an", 2249*12, 2808*12)
print("Socle B1 4500 + assistant 2249-2808 =", 4500+2249, "a", 4500+2808, "EUR/mois")

print("\n== 10. Scenarios retenus (parametres finaux de l'arbitre) ==")
# Prudent : M1 = fevrier 2027 ; cadrage 6000 (50/50) ; socle leger 3000 des M3 ; un lot 4500 par trimestre (40/60)
prud = [3000, 3000, 3000, 3000+1800, 3000+2700, 3000, 3000+1800, 3000+2700, 3000, 3000+1800, 3000+2700, 3000]
# Central : M1 = janvier 2027 ; cadrage 6500 ; pilote : socle 3500 x 2 + lot 6000 (40/60) ; M4-M12 : B1 4500 + lots 3500 en moyenne
cent = [3250, 3250+3500+2400, 3500+3600] + [4500+3500]*9
# Variante centrale : second client 2000 des M7, lots GianLuca ramenes a 2000 pour rester sous 10 JP
cent_v = [3250, 3250+3500+2400, 3500+3600] + [8000]*3 + [4500+2000]*6
autre_v = [0]*6 + [2000]*6
# Ambitieux : M1 = mi-dec. 2026 ; cadrage 6500 ; pilote socle 3500 x2 + deux lots ; M4-M12 : socle+3 5700 + lots 4500 + exploitation 1500 ; 2e client 2500 des M6 ; sous-traitance 1500/mois des M4
amb = [3250, 3250+3500+2400+2400, 3500+3600+3600] + [5700+4500+1500]*9
autre_a = [0]*5 + [2500]*7
st_a = [0, 0, 0] + [1500]*9
for coef in (1.7, 1.9):
    for nom, m, ff, dem, app, st, ac in [
        ("prudent", prud, 1500, 5000, 8000, None, None),
        ("central", cent, 2000, 6000, 10000, None, None),
        ("central variante", cent_v, 2000, 6000, 10000, None, autre_v),
        ("ambitieux", amb, 2800, 7000, 12000, st_a, autre_a)]:
        r = scenario(nom, m, ff, dem, app, coef, 4, 2500, st, ac)
        part12 = m[-1]/(m[-1]+(ac[-1] if ac else 0))
        print(f"coef {coef} {nom:17s} CA Carlone {r['ca_carlone']:7.0f} autre {r['ca_autre']:6.0f} part 12 mois {r['part']*100:4.0f} % part M12 {part12*100:4.0f} % "
              f"net/associe/mois (M4-M12) {r['net_moyen_associe_mois_remunere']:6.0f} tres fin M12 {r['tres_fin']:7.0f}")
print("JP regime : prudent", 3.25+ (4500/800)/3, "; central", 4.5+3500/875, "a", 5.5+3500/800, "; variante", 4.5+2000/875+2000/850, "a", 5.5+2000/800+2000/800,
      "; ambitieux (associes)", 6+4500/900-3+1.5+2500/850, "a", 7+4500/850-2+2+2500/800, "+ 2 a 4 sous-traites")

print("\n== 11. Marges des prix definitifs C2 et C6 ==")
for nom, prix, jlo, jhi in [("C2 pilote commercial", 6000, 6, 7), ("C6 outillage", 7500, 8, 9)]:
    out = []
    for (clo, chi) in ((591, 737), (710, 885)):
        out.append(f"{(prix-jhi*chi)/prix*100:5.1f} a {(prix-jlo*clo)/prix*100:5.1f} %")
    print(nom, prix, f"{prix/jhi:.0f}-{prix/jlo:.0f} EUR/JP", "12 JP:", out[0], "; 10 JP:", out[1], "; plancher 750 x JP max =", 750*jhi)
