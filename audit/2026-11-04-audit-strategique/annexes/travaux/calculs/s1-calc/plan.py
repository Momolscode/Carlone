# Plans à 12 mois (mois 1 = mois de signature du cadrage), montants HT, encaissements [ES]
import itertools
def plan(name, ca_by_month, pay_net_each, pay_from, frais=2000, setup=4500, capital=3000, coef=1.8, delay=0):
    # delay = retard de paiement uniforme en mois appliqué aux encaissements à partir du mois 4
    enc = [0.0]*15
    for m,v in enumerate(ca_by_month, start=1):
        d = delay if m>=4 else 0
        if m+d < 15: enc[m+d] += v
    cash = capital - setup
    low = cash; rows=[]
    for m in range(1,13):
        pay = 2*pay_net_each*coef if m>=pay_from else 0
        cash += enc[m] - frais - pay
        low = min(low,cash)
        rows.append((m, ca_by_month[m-1], enc[m], pay, round(cash)))
    return sum(ca_by_month), low, rows
P = [3000,3000] + [4500]*10            # cadrage 6 000 puis socle léger 3 000 + lots ~1 500/mois
C = [3000,3000+3500+2200,3500+3300] + [8500]*9   # cadrage, pilote 2 mois (socle 3 500 + lot 5 500), puis socle 4 500 + lots ~4 000
A = [3750,3750+4000+4400,4000+6600] + [14500]*9  # cadrage 7 500, pilote (socle 4 000 + 2 lots 11 000), puis 14 500
for name,ca,pay,frm in [('prudent',P,0,99),('prudent-pay500',P,500,4),('central',C,1200,4),('central-1500',C,1500,4),('ambitieux',A,2500,4)]:
    tot,low,rows = plan(name,ca,pay,frm)
    print(f"\n{name}: CA 12 mois {tot:,.0f} € HT ; point bas trésorerie {low:,.0f} € ; fin M12 {rows[-1][4]:,} €")
for name,ca,pay,frm in [('central',C,1200,4),('ambitieux',A,2500,4)]:
    for d in (1,2,3):
        tot,low,rows = plan(name,ca,pay,frm,delay=d)
        print(f"{name} retard {d*30} j dès M4 : point bas {low:,.0f} € ; fin M12 {rows[-1][4]:,} €")
# rupture après M4 (aucun encaissement après M4) central
C_r = C[:4] + [0]*8
tot,low,rows = plan('central-rupture',C_r,1200,4)
print("\ncentral rupture après M4 (paie suspendue au M6):")
# paie arrêtée M6
def plan2(ca,stop):
    cash = 3000-4500; out=[]
    for m in range(1,13):
        pay = 2*1200*1.8 if 4<=m<stop else 0
        cash += ca[m-1]-2000-pay; out.append(round(cash))
    return out
print(plan2(C_r,6))
print("central pay 1200 rows:", plan('c',C,1200,4)[2])
# Capacité facturable implicite (JP) au taux de référence 750-850
for name,v in [('prudent',4500),('central',8500),('ambitieux',14500)]:
    print(name, 'JP implicites', round(v/850,1),'-',round(v/750,1))
