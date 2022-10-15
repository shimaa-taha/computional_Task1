#!/usr/bin/env python
# coding: utf-8

# In[4]:





# In[57]:


import pyopenms
from pyopenms import *
AvogadroNumber=pyopenms.Constants.AVOGADRO
print("number of avogadro is ",AvogadroNumber)
print(" ")

#################################################################################################################
#common elements in pyopenms Oxygen and Sulfur as well as information on their average and monoisotopic weight.
#first Oxygen
EDB=ElementDB()
EDB.hasElement("O")#if has print true else print false
ox=EDB.getElement("O")
print("Name of element is : ",ox.getName())
print("the MonoWeight of it is : ",ox.getMonoWeight())
print("the avarage weight is : ",ox.getAverageWeight())
print("IsotopeDistribution",ox.getIsotopeDistribution())
x=ox.getIsotopeDistribution()
oxygen_isoDist = {"mass ": [], " abundance ": [] }
for iso in x.getContainer():
    print ("Oxygen isotope", iso.getMZ(), "has abundance", iso.getIntensity() * 100, " % ")
    oxygen_isoDist["mass "].append(iso.getMZ())
    oxygen_isoDist[" abundance "].append((iso.getIntensity() * 100))
print(" ")

#################################################################################################################
#second Sulfur
EDB.hasElement("S")#if has print true else print false
S=EDB.getElement("S")
print("Name of element is : ",S.getName())
print("the MonoWeight of it is : ",S.getMonoWeight())
print("the avarage weight is : ",S.getAverageWeight())
print("IsotopeDistribution",S.getIsotopeDistribution())
S=S.getIsotopeDistribution()
Sulfer_isoDist = {"mass ": [], " abundance ": [] }
for iso in S.getContainer():
    print ("Sulfer isotope", iso.getMZ(), "has abundance", iso.getIntensity() * 100, " % ")
    Sulfer_isoDist["mass "].append(iso.getMZ())
    Sulfer_isoDist[" abundance "].append((iso.getIntensity() * 100))
    
print(" ")

#################################################################################################################
#third Hydrogen
EDB.hasElement("H")#if has print true else print false
H=EDB.getElement("H")
print("Name of element is : ",H.getName())
print("the MonoWeight of it is : ",H.getMonoWeight())
print("the avarage weight is : ",H.getAverageWeight())
print("IsotopeDistribution",H.getIsotopeDistribution())
H=H.getIsotopeDistribution()
Hydrogen_isoDist = {"mass ": [], " abundance ": [] }
for iso in H.getContainer():
    print ("Hydrogen isotope", iso.getMZ(), "has abundance", iso.getIntensity() * 100, " % ")
    Hydrogen_isoDist["mass "].append(iso.getMZ())
    Hydrogen_isoDist[" abundance "].append((iso.getIntensity() * 100))
    
print(" ")

#################################################################################################################
######  The isotope distribution of oxygen and sulfur can be displayed with the following extra code:

import math
from matplotlib import pyplot as plt

def adjustText(x1, y1, x2, y2):
    if y1 > y2:
        plt.annotate('%0.3f' % (y2), xy=(x2, y2), xytext=(x2+0.5,y2+9), textcoords=' data ',
                     arrowprops=dict(arrowstyle="->", color='r', lw=0.5),horizontalalignment='Right', verticalalignment='Top')
    else:
        plt.annotate('%0.3f' % (y1), xy=(x1, y1), xytext=(x1+0.5,y1+9),textcoords=' data ',
                     arrowprops=dict(arrowstyle="->", color='r', lw=0.5), horizontalalignment='Right', verticalalignment='Top')

def plotDistribution(distribution):
    n = len(distribution["mass "])
    for i in range(0, n):
        plt.vlines(x=distribution["mass "][i], ymin=0, ymax=distribution[" abundance "][i])
        if int(distribution["mass "][i - 1]) == int(distribution["mass "][i]) and i != 0:
            adjustText(distribution["mass "][i - 1],distribution[" abundance "][i - 1], 
                       distribution["mass "][i],distribution[" abundance "][i])
        else:
            plt.text(x=distribution["mass "][i], y=(distribution[" abundance "][i] + 2),
                     s='%0.3f' % (distribution[" abundance "][i]), va='center', ha='center')
    plt.ylim([0, 110])
    plt.xticks(range(math.ceil(distribution["mass "][0]) - 2,
                     math.ceil(distribution["mass "][-1]) + 2))


plt.figure(figsize=(14,7))

plt.subplot(1,2,1)
plt.title("Isotopic distribution of oxygen")
plotDistribution(oxygen_isoDist)
plt.xlabel("Atomic mass (u)")
plt.ylabel("Relative abundance (%)")

#plt.subplot(1,2,2)
#plt.title("Isotopic distribution of sulfur")
#plotDistribution(Sulfer_isoDist)
#plt.xlabel("Atomic mass (u)")
#plt.ylabel("Relative abundance (%)")

plt.subplot(1,2,2)
plt.title("Isotopic distribution of Hydrogen")
plotDistribution(Hydrogen_isoDist)
plt.xlabel("Atomic mass (u)")
plt.ylabel("Relative abundance (%)")
plt.show()

#################################################################################################################
#Mass Defect for carbon and nitrogen
#first carbon
isotopes = EDB.getElement("C").getIsotopeDistribution().getContainer()
carbon_isotope_difference = isotopes[1].getMZ() - isotopes[0].getMZ()
print("Mass difference between 12C and 13C :",carbon_isotope_difference)

#second nitrogen
isotopes = EDB.getElement("N").getIsotopeDistribution().getContainer()
nitrogen_isotope_difference = isotopes[1].getMZ() - isotopes[0].getMZ()
print("Mass difference between 12C and 13C :",nitrogen_isotope_difference )

#################################################################################################################
#Molecular Formulae
#Elements can be combined to molecular formulas (EmpiricalFormula)
Methanol = EmpiricalFormula("CH3OH")
Water = EmpiricalFormula("H2O")
Ethanol = EmpiricalFormula("CH2") + Methanol
print("Ethanol chemical formula is :", Ethanol.toString())
print("Ethanol Composition is : ",Ethanol.getElementalComposition())

#################################################################################################################
#ResidueDB
L = ResidueDB().getResidue("Lysine")
print(L.getName())

print(L.getThreeLetterCode())

print(L.getOneLetterCode())#the most usable

print(L.getAverageWeight())

print(L.getMonoWeight())

print(L.getFormula().toString())

#################################################################################################################


# In[ ]:




