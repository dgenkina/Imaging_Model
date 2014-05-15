# -*- coding: utf-8 -*-
"""
Created on Tue May 13 13:40:39 2014

@author: dng5
"""

from pylab import *
import numpy as np

"""first define constants"""
hbar = 1.05457173*1e-34 #m^2kg/s
c = 299792485 #m/s

"""for K atoms, on resonant light:"""
gamma = 2*pi*6035000.0 #Hz
k = 2*pi*1298518.93857 #m^-1 
omega = k*c
vrecoil = 0.01296541083 #m/s
isat = 17.5 #W/m^2
A = hbar*omega*gamma/2/isat
B = k*vrecoil
         
"""define initial atom distribution, and convert to superatoms"""
def n(x):
    return 1.1e17

zfinal = 0.0001 #m, so ~100um
dz = zfinal/100000.00
zrange = np.arange(0,zfinal,dz)

superSize = 1e10 #number of atoms per unit area in one superatom
integral = np.cumsum([n(z)*dz for z in zrange])/superSize
superAtomNumber = int(integral[zrange.size-1]) 
atomIndexes = np.arange(superAtomNumber)
positions = np.interp(atomIndexes+1,integral,zrange)




#tfinal = 0.0002 #s, so up to 200us
#dt = tfinal/1000.00
#Inotrange = np.exp(np.arange(-2, 2, 0.5))
#num = zeros([zrange.size])
#trange = np.arange(0,tfinal,dt)