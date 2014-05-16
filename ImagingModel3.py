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
Gamma = 2*pi*6035000.0 #Hz
k = 2*pi*1298518.93857 #m^-1 
omega = k*c
vrecoil = 0.01296541083 #m/s
isat = 17.5 #W/m^2
A = hbar*omega*Gamma/2/isat
B = k*vrecoil

"""Define superatom class"""
def add(x,y): return x+y
    
class SuperAtom:
    def __init__(self,position,velocity):
        self.z = position       
        self.v = velocity
        self.zlist = [position]
        self.vlist = [velocity]
    def updateVelocity(self, Vadded):
        self.v += Vadded
        self.vlist.append(self.v)
    def updatePosition(self,time):
        self.z += self.v*time
        self.zlist.append(self.z)
        

         
"""define initial atom distribution, and convert to superatoms.
Assign initial position and velocity to each superatom"""
def n(x):
    return 1.1e17

zfinal = 0.0001 #m, so ~100um
dz = zfinal/100000.00
zrange = np.arange(0,zfinal,dz)
Inotrange = np.exp(np.arange(-5, 8, 0.5))

superSize = 5e10 #number of atoms per unit area in one superatom
integral = np.cumsum([n(z)*dz for z in zrange])/superSize
od = integral[zrange.size-1]*superSize*A
superAtomNumber = int(integral[zrange.size-1]) 
atomIndexes = np.arange(superAtomNumber)
positions = np.interp(atomIndexes+1,integral,zrange)
atoms = [[SuperAtom(zed/2,0.0) for zed in positions] for x in range(Inotrange.size)]



"define time grid and initialize intensity array"
tfinal = 0.0001 #s, so up to 200us
dt = tfinal/100.00
trange = np.arange(0,tfinal,dt)
Inots = np.outer(Inotrange,np.ones(trange.size))
Times = np.outer(np.ones(Inotrange.size),trange) 
I = np.zeros([Inotrange.size, trange.size, superAtomNumber+1])
I[:,:,0] = Inots
Delta = np.zeros([Inotrange.size])
rate = np.zeros([Inotrange.size])


for t in range(trange.size):
    sortedAtoms = []
    for i in range(Inotrange.size):
        sortedAtoms.append(sorted(atoms[i], key=lambda SuperAtom: SuperAtom.z))
        for atomIndex in atomIndexes:
            Delta[i] = 2*k*np.array(sortedAtoms[i][atomIndex].v)/Gamma
            rate[i] = (I[i,t,atomIndex])/(1+(Delta[i]**2)+I[i,t,atomIndex])
            I[i,t,atomIndex+1]=I[i,t,atomIndex]-A*superSize*rate[i]
            sortedAtoms[i][atomIndex].updateVelocity(B*rate[i]*dt*Gamma/2/k)
            sortedAtoms[i][atomIndex].updatePosition(dt)
        
Ifinaltot = np.cumsum(I[:,:,superAtomNumber]*dt,axis=1)/(Times+dt)
od0 = -np.log(Ifinaltot/Inots)     
od1 = -np.log(Ifinaltot/Inots) + (Inots-Ifinaltot)



