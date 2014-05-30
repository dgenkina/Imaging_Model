# -*- coding: utf-8 -*-
"""
Created on Thu May 29 10:42:56 2014

@author: dng5
"""

""" Create a table of simulated values of OD for an imaging time of 40 us
and make a function that interpolates the table to get a value of simulated
OD for any input initial od and probe intensity"""
import numpy as np
from scipy import interpolate

tempfile = np.load("Data/SimulatedOD10.npz")
ODrange = np.linspace(0.01,2.5,500)
allODs40us = np.zeros([ODrange.size,tempfile['I0range'].size])

for odind in range(ODrange.size): 
    odinit = ODrange[odind]
    tempfile = np.load("Data/SimulatedOD"+str(int(odinit*1000))+".npz") 
    allODs40us[odind,:]=tempfile['od0All'][:,200]
    
np.savez("Data/Simul40us", od = allODs40us)

def simulODfunction(odInitial, Inot):
    return interpolate.RectBivariateSpline(ODrange,tempfile['I0range'],allODs40us).ev(odInitial, Inot)[0]

def whatsMyTrueODfunction(Rod, Inot):
    ODarray = np.empty_like(Rod)
    Rod=np.array(Rod)
    Inot=np.array(Inot)    
    for x in range(Rod.shape[0]):
        for y in range(Rod.shape[1]):
            ODarray[x,y]=np.interp(Rod[x,y],[simulODfunction(OD, Inot[x,y]) for OD in ODrange], ODrange)
    return ODarray
#whatsMyTrueODvectFunc = np.vectorize(whatsMyTrueODfunction, otypes=[np.float])
    
def whatsMyTrueODfunc(Rod, Inot):
    tempfile = np.load("Data/SimulatedOD10.npz")
    SimulFile = np.load("Data/Simul40us.npz")
    allODs40us = SimulFile['od']
    I0range = tempfile['I0range']
    ODarray = np.empty_like(Rod)
    Rod=np.array(Rod)
    Inot=np.array(Inot)    
    for x in range(Rod.shape[0]):
        for y in range(Rod.shape[1]):
            Iindex = np.searchsorted(I0range,Inot[x,y])
            #print Iindex
            ODindex = np.searchsorted(allODs40us[:,Iindex-1], Rod[x,y])
            #print ODindex
            ODarray[x,y] = ODrange[ODindex-1]
    return ODarray