# Coût complet d'une journée-personne facturable (JP) — stratège S1, 4 nov. 2026 [ES]
# Hypothèses : dispo 17,5 JP/mois/personne (syn-capacite 2.1) ; parts Marwin et JP facturables (syn-capacite 2.2-2.3)
# Rémunération cible exprimée en net avant IR par équivalent temps plein Marwin ; coef coût/net SAS 1,70-1,90, SARL TNS 1,40-1,46 (syn-droit 1.1-1.2)
# Frais fixes Marwin 1 500 à 2 500 €/mois [HY] ; réserve 10 % du CA [PR]
scen = {
 'prudent': dict(fte=0.50+0.25, fact=7),
 'central': dict(fte=0.65+0.50, fact=12),
 'haut':    dict(fte=0.90+0.90, fact=20),
}
for target in (2500, 3660):
  print(f"\n== cible {target} € net par ETP Marwin")
  for name,s in scen.items():
    for forme,(clo,chi) in {'SAS':(1.70,1.90),'SARL':(1.40,1.46)}.items():
      lo = (s['fte']*target*clo + 1500)/s['fact']/0.9
      hi = (s['fte']*target*chi + 2500)/s['fact']/0.9
      ca_lo = (s['fte']*target*clo + 1500)/0.9
      ca_hi = (s['fte']*target*chi + 2500)/0.9
      print(f"{name:8s} {forme:4s} coût/JP fact. {lo:5.0f}-{hi:5.0f} €  | CA mensuel nécessaire {ca_lo:6.0f}-{ca_hi:6.0f} € HT")
# Seuil sans rémunération : frais seuls
print("\nSeuil sans rémunération (frais + réserve):", round(1500/0.9), '-', round(2500/0.9), '€ HT/mois')
