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

for odind in range(ODrange.size): 
    odinit = ODrange[odind]
    tempfile = np.load("Data/SimulatedOD"+str(int(odinit*1000))+".npz") 
    allODs40us[odind,:]=tempfile['od0All'][:,200]
    
np.savez("Data/Simul40us", od = allODs40us)

def simulODfunction(odInitial, Inot):
    return interpolate.RectBivariateSpline(ODrange,tempfile['I0range'],allODs40us).ev(odInitial, Inot)


