# Vérifications du juge J1-client (4 nov. 2026). Tous résultats [ES].
def r(x): return round(x)
print("== 1. Coût complet JP (formule S1 : (ETP*net*coef + frais)/JP/0,9)")
sc = {"prudent":(0.75,7),"central":(1.15,12),"haut":(1.8,20)}
for k,(etp,jp) in sc.items():
    for net in (2500,3660):
        lo=(etp*net*1.7+1500)/jp/0.9; hi=(etp*net*1.9+2500)/jp/0.9
        print(k,net,r(lo),r(hi))
print("== 2. S3 : coefficient implicite OFF:114 (SARL, net après IR)")
etp_cost=(60000+33332)/24; print("coût ETP 2500 nets", r(etp_cost), "coef", round(etp_cost/2500,3))
for k,(etp,jp) in sc.items():
    print("S3",k, r((etp*etp_cost+1500)/jp), r((etp*etp_cost+2500)/jp))
lo=(1.15*2500*1.7+1500)/12/0.9; hi=(1.15*2500*1.9+2500)/12/0.9
print("marge sur 750 au coût SAS+réserve central:", round((750-hi)/750*100,1), "à", round((750-lo)/750*100,1), "%")
print("== 3. S2 coût JP central (2 associés, 12 JP, frais 2500, coef 1,8)")
for net in (2000,2500):
    c=(2*net*1.8+2500)/12; print(net, r(c), r(c/0.9))
print("S2 diag 4 : net/associé à 12 JP x 750, frais 2500, réserve 10% :", r((9000*0.9-2500)/1.9/2), r((9000*0.9-2500)/1.7/2))
print("S2 cadrage 7500 / 8 JP : marge sur coût complet")
for c in (810,900,960,1065):
    print(c, round((7500-8*c)/7500*100,1),"%")
print("S2 seuils:", r((2*2000*1.8+2500)/0.9), r((2*2500*1.8+2500)/0.9))
print("S2 central capacité: B2 9 JP + lots 2500/925 =", round(9+2500/925,1), "+ D1 (1 à 1,5 JP) -> ", round(9+2500/925+1,1), "à", round(9+2500/925+1.5,1), "JP pour 12 disponibles")
print("S2 part GianLuca <=85% avec CA 12000 tout Carlone -> autre CA requis:", r(12000/0.85-12000))
print("S2 seuil recrutement: salarié cadre 5380-6150 €/mois ; équivalent JP Marwin à 900 €:", round(5380/900,1), round(6150/900,1), "; à 750 €:", round(5380/750,1), round(6150/750,1))
# S2 année 1 : mois 1 = déc.
ca=[3750,3750,5400,5400]+[8000]*8
lots=[0,0,0]+[2500]*9
d1=[0]*7+[1500]*5
print("S2 année 1 (B2 dès avril):", sum(ca)+sum(lots)+sum(d1))
ca2=[3750,3750,5400,5400,5400]+[8000]*7
print("S2 année 1 (B2 après 3 mois de B1, dès mai):", sum(ca2)+sum(lots)+sum(d1))
print("== 4. S1 scénarios 12 mois")
print("central:", 6000+3500*2+5000+8500*9, " prudent:", 6000+3000*10+4500*3, " ambitieux≈", 7500+5500*2+2*5000+14500*9)
print("S1 cadrage 8 JP coût central", r(8*590), r(8*740), "marge", round((6000-8*740)/6000*100,1), round((6000-8*590)/6000*100,1))
print("== 5. S3 scénarios")
print("central", 7200*6+8500*6, "prudent", 3600*6+3000*6, "ambitieux", 11000*6+16000*6)
disp=4550
print("S3 net 2 associés : coef 1,42..1,9 ->", r(disp/1.9), r(disp/1.42), "; plancher 2500/ETP x1,15 =", 2875)
print("S3 15000/2808 =", round(15000/2808,2), "; 15000/6149 =", round(15000/6149,2))
print("== 6. Grille neutre : net/associé (SAS, coef 1,7-1,9, réserve 10 %, frais 1500-2500) à 12 JP facturés")
for p in (750,800,900):
    ca=12*p
    lo=(ca*0.9-2500)/1.9/2; hi=(ca*0.9-1500)/1.7/2
    print(p, ca, r(lo), r(hi))
print("== 7. Coût annuel pour GianLuca (HT / TTC si TVA non récupérable)")
for n,v in (("S1 central",94500),("S2 central",112000),("S3 central Marwin seul",80000),("S3 + assistant bas",80000+27000),("S3 + assistant haut",80000+40000),("Offre archives base 6 mois",90000)):
    print(n, v, r(v*1.2))
print("== 8. TVA : cadrage TTC", 6000*1.2, 6500*1.2, 7500*1.2)
