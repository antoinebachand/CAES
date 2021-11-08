# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:35:53 2020

@author: antoi
"""
#============================================================
# Configuration d'air comprimé
#============================================================


import matplotlib.pyplot as plt

from caes.core_graphique import CAES

from params import config

test = CAES(config)
test.start_workflow()
config_CAES= test.ml


"""
0;0.18673515
7199;0.18673515
7200;0.141535
17999;0.141535
18000;0

"""
#============================================================
# Calcul des fuites de l'hydrogène 
#============================================================

from caes.core_graphique import CAES
from params import H_1
from params import H_2
from params import H_3
from params import H_4
from params import H_5
from params import H_6
from params import H_7
from params import H_8
from params import H_9
from params import H_10
from params import H_11
from params import H_12
from params import H_13
from params import H_14
from params import H_15
from params import H_16
from params import H_17
from params import H_18
from params import H_19


test = CAES(H_1)
test.start_workflow()
ml_H_1 = test.ml
 
test = CAES(H_2)
test.start_workflow()
ml_H_2 = test.ml
 
test = CAES(H_3)
test.start_workflow()
ml_H_3 = test.ml

test = CAES(H_4)
test.start_workflow()
ml_H_4 = test.ml
 
test = CAES(H_5)
test.start_workflow()
ml_H_5 = test.ml

test = CAES(H_6)
test.start_workflow()
ml_H_6 = test.ml

test = CAES(H_7)
test.start_workflow()
ml_H_7 = test.ml

test = CAES(H_8)
test.start_workflow()
ml_H_8 = test.ml

test = CAES(H_9)
test.start_workflow()
ml_H_9 = test.ml

test = CAES(H_10)
test.start_workflow()
ml_H_10 = test.ml

test = CAES(H_11)
test.start_workflow()
ml_H_11 = test.ml

test = CAES(H_12)
test.start_workflow()
ml_H_12 = test.ml

test = CAES(H_13)
test.start_workflow()
ml_H_13 = test.ml

test = CAES(H_14)
test.start_workflow()
ml_H_14 = test.ml

test = CAES(H_15)
test.start_workflow()
ml_H_15 = test.ml

test = CAES(H_16)
test.start_workflow()
ml_H_16 = test.ml

test = CAES(H_17)
test.start_workflow()
ml_H_17 = test.ml

test = CAES(H_18)
test.start_workflow()
ml_H_18 = test.ml

test = CAES(H_19)
test.start_workflow()
ml_H_19 = test.ml

#============================================================
# Calcul des fuites de l'hydrogène à 36 Mpa
#============================================================
from caes.core_graphique import CAES
from params import H_1_50MPa
from params import H_2_50MPa
from params import H_3_50MPa
from params import H_4_50MPa
from params import H_5_50MPa
from params import H_6_50MPa
from params import H_7_50MPa
from params import H_8_50MPa
from params import H_9_50MPa
from params import H_10_50MPa
from params import H_11_50MPa
from params import H_12_50MPa
from params import H_13_50MPa
from params import H_14_50MPa
from params import H_15_50MPa
from params import H_16_50MPa
from params import H_17_50MPa
from params import H_18_50MPa
from params import H_19_50MPa


test = CAES(H_1_50MPa)
test.start_workflow()
ml_H_1_50MPa = test.ml
 
test = CAES(H_2_50MPa)
test.start_workflow()
ml_H_2_50MPa = test.ml
 
test = CAES(H_3_50MPa)
test.start_workflow()
ml_H_3_50MPa = test.ml

test = CAES(H_4_50MPa)
test.start_workflow()
ml_H_4_50MPa = test.ml
 
test = CAES(H_5_50MPa)
test.start_workflow()
ml_H_5_50MPa = test.ml

test = CAES(H_6_50MPa)
test.start_workflow()
ml_H_6_50MPa = test.ml

test = CAES(H_7_50MPa)
test.start_workflow()
ml_H_7_50MPa = test.ml

test = CAES(H_8_50MPa)
test.start_workflow()
ml_H_8_50MPa = test.ml

test = CAES(H_9_50MPa)
test.start_workflow()
ml_H_9_50Mpa = test.ml

test = CAES(H_10_50MPa)
test.start_workflow()
ml_H_10_50MPa = test.ml

test = CAES(H_11_50MPa)
test.start_workflow()
ml_H_11_50MPa = test.ml

test = CAES(H_12_50MPa)
test.start_workflow()
ml_H_12_50MPa = test.ml

test = CAES(H_13_50MPa)
test.start_workflow()
ml_H_13_50MPa = test.ml

test = CAES(H_14_50MPa)
test.start_workflow()
ml_H_14_50MPa = test.ml

test = CAES(H_15_50MPa)
test.start_workflow()
ml_H_15_50MPa = test.ml

test = CAES(H_16_50MPa)
test.start_workflow()
ml_H_16_50MPa = test.ml

test = CAES(H_17_50MPa)
test.start_workflow()
ml_H_17_50MPa = test.ml

test = CAES(H_18_50MPa)
test.start_workflow()
ml_H_18_50MPa = test.ml

test = CAES(H_19_50MPa)
test.start_workflow()
ml_H_19_50MPa = test.ml


#============================================================
# Représentation graphique 
#============================================================

fig,ax = plt.subplots(dpi=200)
ax.plot( ml_H_1, 'r')
ax.plot(ml_H_2,'b')
ax.plot(ml_H_3,'g')
ax.plot(ml_H_4,'m')
ax.plot(ml_H_5,'c')
ax.plot(ml_H_6,'k')
ax.plot(ml_H_7,'y')
ax.set_xlabel('time (s)')
ax.set_ylabel('Leakage rate (kg/s)')
ax.set_title('Hydrogen leakage rate (k = 10-21 m2 ) ')
plt.legend(['r= 0.5m: leakage of 11.59 %','r= 0.4m: leakage of 14.8 %', 'r= 0.3m: leakage of 20.1 %', 'r=0.3m (73%)', 'r=0.2m (85%)', 'r=0.15m (90%)', 'r=0.1m (95%)'], loc='best')
# Exportation à forte résolution 
#plt.savefig("Leakage.jpg ", dpi=150)    


#============================================================
# Calcule du pourcentage de fuite 
#============================================================
 
# 18 MPa

Total_mas_of_injection = 2873
Leak_Mass = [sum(ml_H_1), sum(ml_H_2), sum(ml_H_3), sum(ml_H_4), sum(ml_H_5), sum(ml_H_6), sum(ml_H_7), sum(ml_H_8),
             sum(ml_H_9), sum(ml_H_10), sum(ml_H_11), sum(ml_H_12), sum(ml_H_13), sum(ml_H_14), sum(ml_H_15), sum(ml_H_16), sum(ml_H_17), sum(ml_H_18), sum(ml_H_19)  ] 

Leakage_rate = [ (i / Total_mas_of_injection)*100 for i in Leak_Mass]
print("Les fuites sont de: ")
print(Leakage_rate)
Radius = [0.25, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2]

# 36 MPa

Total_mas_of_injection_36MPa = 5746
Leak_Mass_36MPa = [sum(ml_H_1_50MPa), sum(ml_H_2_50MPa), sum(ml_H_3_50MPa), sum(ml_H_4_50MPa), sum(ml_H_5_50MPa), sum(ml_H_6_50MPa), sum(ml_H_7_50MPa), sum(ml_H_8_50MPa),
             sum(ml_H_9_50Mpa), sum(ml_H_10_50MPa), sum(ml_H_11_50MPa), sum(ml_H_12_50MPa), sum(ml_H_13_50MPa), sum(ml_H_14_50MPa), sum(ml_H_15_50MPa), sum(ml_H_16_50MPa), sum(ml_H_17_50MPa), sum(ml_H_18_50MPa), sum(ml_H_19_50MPa)  ] 


Leakage_rate_36MPa = [ (i / Total_mas_of_injection_36MPa)*100 for i in Leak_Mass_36MPa]
print("Les fuites sont de: ")
print(Leakage_rate_36MPa)

#============================================================
# Représentation graphique du pourcentage de fuite 
#============================================================

fig,ax = plt.subplots(dpi=200)
ax.plot(Radius, Leakage_rate, 'crimson')
ax.plot(Radius, Leakage_rate_36MPa, 'b')
ax.set_xlabel('Radius (m)')
ax.set_ylabel('Leakage percentage for 1 day of storage (%)')
ax.set_title('Leakage VS Radius')
plt.legend(['18 MPa or 180 bar','36 MPa or 360 bar'], loc='best')
plt.show() 



