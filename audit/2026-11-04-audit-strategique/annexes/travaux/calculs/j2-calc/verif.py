# Vérifications du juge J2-marwin (4 nov. 2026). Toutes les sorties sont des estimations [ES].
# Hypothèses reprises des synthèses : capacité centrale 12 JP facturables, 1,15 ETP (Morgan 65 %, Mathys 50 %),
# temps brut Marwin 20,1 JP et non facturable 8,4 JP (syn-capacite-ia.md:183-190), coefficient SAS 1,7-1,9 (syn-droit.md:98).
etp, jp = 1.15, 12
print("1. Coût complet par JP (central)")
for label, cpe in [("SAS 1,7", 2500*1.7), ("SAS 1,9", 2500*1.9), ("base S3/V5 3 889 €/ETP", 3889)]:
    for fr in (1500, 2500):
        c = (etp*cpe + fr)/jp
        print(f"  {label:24s} frais {fr}: {c:5.0f} € sans réserve ; {c/0.9:5.0f} € avec réserve 10 %")
print("2. S3 central : disponible 4 550 €/mois (année) et 5 650 (régime) contre besoin 2 500 €/ETP en SAS",
      [round(etp*2500*k) for k in (1.7, 1.9)])
print("   net par associé SAS", round(4550/1.9/2), "-", round(4550/1.7/2), "; SARL 1,43 :", round(4550/1.43/2))
print("3. Seuil de besoin (JP/mois) au-delà duquel un chef de projet cadre salarié (6 149 €/mois) coûte moins cher")
for p in (750, 800, 889, 900, 908):
    print(f"  prix {p} €/JP -> {6149/p:4.1f} JP/mois")
print("4. S2 cadrage 7 500 € / 8 JP : marge sur coût complet S2")
for c in (810, 900, 960, 1065):
    print(f"  coût {c} €/JP -> marge {100*(7500-8*c)/7500:4.0f} %")
print("5. S2 central : JP facturées (B2 9 + lots 2 500 €/920 + D1 100 fiches à 5/10/15 min)")
b = 9 + 2500/920
for m in (5, 10, 15):
    f = b + 100*m/60/7
    print(f"  D1 à {m} min/fiche -> {f:4.1f} JP ; occupation du temps Marwin {(f+8.4)/20.1*100:4.0f} %")
for f in (10.5, 12):
    print(f"  {f} JP facturées -> occupation du temps Marwin {(f+8.4)/20.1*100:4.0f} %")
print("   S2 ambitieux : B3 13 + lots 7 000/920 + D 3 000/900 + 2e client 3 000/900 =", round(13+7000/920+3000/900+3000/900, 1), "JP pour 22-24 JP de capacité")
print("6. Coût interne d'une fiche CRM qualifiée (S2 D1 vendu 12-18 €)")
for m in (5, 10, 15):
    print(f"  {m} min : {750/7*m/60:5.1f} € à 750 €/JP ; {900/7*m/60:5.1f} € à 900 €/JP")
print("7. S1 plancher cadrage 5 000 € :", 5000/8, "€/JP sur 8 JP ;", round(5000/7), "€/JP sur 7 JP")
print("8. S3 réserve de démarrage : somme des postes listés =", 2000+3000+9000, "à", 5000+5000+9000, "€ (annoncé 8 000 à 12 000)")
print("9. CA hors GianLuca nécessaire à M12 : S1 (≤ 80 %, 8 500 de GL) =", round(8500/0.8-8500), "€ ; S2 (≤ 85 %, 12 000 de GL) =", round(12000/0.85-12000), "€")
