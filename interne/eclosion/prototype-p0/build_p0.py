"""Eclosion P0 v0.2 - geometrie d'etude, unites mm, aucun materiel commande."""
from pathlib import Path
import json, math, csv
import numpy as np
from scipy.interpolate import PchipInterpolator
import cadquery as cq

HERE=Path(__file__).resolve().parent
L=150.0
interp=PchipInterpolator([0,12,35,60,90,120,142,150],[7,13,23,27,25,18,8,0])
x=np.linspace(0,L,91); w=interp(x)
outline=[(float(a),float(b)) for a,b in zip(x,w)]+[(float(a),-float(b)) for a,b in zip(x[-2::-1],w[-2::-1])]

plate=cq.Workplane('XY').polyline(outline).close().extrude(1.6)
root=cq.Workplane('XY').box(20,18,12,centered=(False,True,False)).translate((-8,0,0))
rib=cq.Workplane('XY').polyline([(10,-1.2),(138,-1.2),(146,0),(138,1.2),(10,1.2)]).close().extrude(3).translate((0,0,1.6))
petal=plate.union(root).union(rib)
# Axe horizontal suivant Y. Passage nominal, finition et jeu a valider.
bore=cq.Solid.makeCylinder(1.6,30,cq.Vector(0,-15,6),cq.Vector(0,1,0))
petal=petal.cut(bore)
# Reservation d'une vis de pression M3 : avant-trou a tarauder, non valide en fatigue.
radial=cq.Solid.makeCylinder(1.3,8,cq.Vector(0,0,6),cq.Vector(0,0,1))
petal=petal.cut(radial)

base=cq.Workplane('XY').box(100,90,5,centered=(True,True,False))
for px in (-42,42):
 for py in (-35,35):
  base=base.cut(cq.Solid.makeCylinder(2.25,8,cq.Vector(px,py,-1)))
for py in (-17,17):
 post=cq.Workplane('XY').box(16,6,36,centered=(True,True,False)).translate((0,py,5))
 base=base.union(post)
shaft_void=cq.Solid.makeCylinder(1.6,50,cq.Vector(0,-25,35),cq.Vector(0,1,0))
base=base.cut(shaft_void)

gauge=cq.Workplane('XY').box(70,20,4,centered=(False,False,False))
for xx,d in zip([10,26,42,58],[3.0,3.2,3.4,3.6]):
 gauge=gauge.cut(cq.Solid.makeCylinder(d/2,6,cq.Vector(xx,10,-1)))

def pose(theta):
 return petal.translate((0,0,-6)).rotate((0,0,0),(0,1,0),theta-90).translate((0,0,35))

spacer=cq.Workplane('XY').circle(4).circle(1.65).extrude(4.5)
parts={'petale_p0':petal,'socle_p0':base,'coupon_alesages':gauge,'entretoise_p0':spacer}
meta={}
for name,obj in parts.items():
 s=obj.val();assert s.isValid() and len(obj.solids().vals())==1,(name,'geometrie invalide')
 cq.exporters.export(obj,str(HERE/(name+'.step')))
 cq.exporters.export(obj,str(HERE/(name+'.stl')),tolerance=.035,angularTolerance=.12)
 b=s.BoundingBox();c=s.Center()
 meta[name]={'volume_mm3':s.Volume(),'center_mm':[c.x,c.y,c.z],
 'bbox_mm':[b.xlen,b.ylen,b.zlen],'solid_valid':True,'solid_count':1}

positions=[]
for theta in np.linspace(20,80,61):
 solid=pose(float(theta)).val()
 vol=solid.intersect(base.val()).Volume()
 positions.append({'angle_deg':float(theta),'intersection_mm3':vol})
(HERE/'collision_diagnostic.json').write_text(json.dumps(positions,indent=2))
assert max(p['intersection_mm3'] for p in positions)<1e-5,'Collision geometrique nominale'

shaft=cq.Workplane('XY').newObject([cq.Solid.makeCylinder(1.5,70,cq.Vector(0,-35,35),cq.Vector(0,1,0))])
asm=cq.Assembly(name='Eclosion_P0_ouverte')
asm.add(base,name='socle',color=cq.Color(.16,.21,.22))
asm.add(pose(80),name='petale_80deg',color=cq.Color(.75,.60,.32))
asm.add(shaft,name='axe_3mm_70mm',color=cq.Color(.65,.67,.69))
for label,yy in [('gauche',-13.5),('droite',9)]:
 asm.add(spacer.rotate((0,0,0),(1,0,0),-90).translate((0,yy,35)),name='entretoise_'+label,color=cq.Color(.55,.56,.57))
asm.save(str(HERE/'assemblage_p0.step'))

density=1.24 # g/cm3, hypothese PLA de la source indiquee dans le PDF.
mass=meta['petale_p0']['volume_mm3']/1000*density
cm=meta['petale_p0']['center_mm']
radial_mm=math.hypot(cm[0],cm[2]-6)
g=9.80665
mmax=.035;rmax=.080;ez=.006
sweep=math.radians(60);duration=3
# Quintique s(u)=10u^3-15u^4+6u^5 : max |s''|=10sqrt(3)/3.
amax=(10*math.sqrt(3)/3)*sweep/duration**2
Imax=mmax*(.150**2+ez**2)
Tgravity=mmax*g*math.hypot(rmax,ez)
Tinertia=Imax*amax
Tfriction=.008 # hypothese a mesurer au banc
factor=2
Ttarget=factor*(Tgravity+Tinertia+Tfriction)
checks={'version':'0.2','units':'mm, kg, N.m, s',
 'geometry':meta,'nominal_sweep':{'min_deg':20,'max_deg':80,'samples':61,
 'max_intersection_mm3':max(x['intersection_mm3'] for x in positions),
 'scope':'petale/socle nominaux seulement ; sans moteur, couplage, cables ni deformation'},
 'mass_model':{'density_g_cm3':density,'solid_petal_mass_g':mass,'center_from_pivot_mm':[cm[0],cm[1],cm[2]-6],'radial_distance_mm':radial_mm},
 'sizing':{'max_moving_mass_kg':mmax,'max_com_radius_m':rmax,'com_offset_m':ez,'sweep_deg':60,'move_time_s':duration,
 'max_acceleration_rad_s2':amax,'max_inertia_kg_m2':Imax,'gravity_torque_Nm':Tgravity,'inertia_torque_Nm':Tinertia,
 'friction_assumption_Nm':Tfriction,'design_factor':factor,'target_torque_Nm':Ttarget,'target_kgfcm':Ttarget/.0980665,
 'suggested_target_Nm':.08,'hardware_validation':False}}
(HERE/'calculs_et_controles.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
with (HERE/'effort_par_angle.csv').open('w',newline='') as f:
 writer=csv.writer(f);writer.writerow(['angle_from_vertical_deg','gravity_torque_Nm','design_torque_Nm'])
 for theta in range(20,81,5):
  a=math.radians(theta);t=mmax*g*(rmax*math.sin(a)+ez*math.cos(a))
  writer.writerow([theta,round(t,6),round(factor*(t+Tinertia+Tfriction),6)])
(HERE/'outline.json').write_text(json.dumps(outline))
print(json.dumps({'geometry':meta,'estimated_mass_g':mass,'sizing':checks['sizing'],'sweep_max_intersection_mm3':checks['nominal_sweep']['max_intersection_mm3']},indent=2))
