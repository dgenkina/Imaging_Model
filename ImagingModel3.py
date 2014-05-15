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
        
class ReturnValues:
    def __init__(y0,y1,y2,y3):
        self.od = y0
        self.od1 = y1
        self.Ifinal=y2
        self.AtomVelocity=y3
        

def Image(Inot, tfinal,steps):         
    """define initial atom distribution, and convert to superatoms.
    Assign initial position and velocity to each superatom"""
    def n(x):
        return 1.1e17
    
    zfinal = 0.0001 #m, so ~100um
    dz = zfinal/100000.00
    zrange = np.arange(0,zfinal,dz)
    
    superSize = 1e10 #number of atoms per unit area in one superatom
    integral = np.cumsum([n(z)*dz for z in zrange])/superSize
    od = integral[zrange.size-1]*superSize*A
    superAtomNumber = int(integral[zrange.size-1]) 
    atomIndexes = np.arange(superAtomNumber)
    positions = np.interp(atomIndexes+1,integral,zrange)
    atoms = [SuperAtom(zed/2,0.0) for zed in positions]
    
    "define time grid and initialize intensity array"
    dt = tfinal/float(steps)
    trange = np.arange(0,tfinal,dt)
 #   Inot = 1.3
    I = np.zeros([trange.size, superAtomNumber+1])
    I[:,0] = Inot
    
    for t in range(trange.size):
        sortedAtoms = sorted(atoms, key=lambda SuperAtom: SuperAtom.z)
        for atomIndex in atomIndexes:
            Delta = 2*k*sortedAtoms[atomIndex].v/Gamma
            rate = (I[t,atomIndex])/(1+(Delta**2)+I[t,atomIndex])
            I[t,atomIndex+1]=I[t,atomIndex]-A*superSize*rate
            sortedAtoms[atomIndex].updateVelocity(B*rate*dt*Gamma/2/k)
            sortedAtoms[atomIndex].updatePosition(dt)
        
    Ifinaltot = np.cumsum(I[:,superAtomNumber]*dt)/(trange+dt)
    #od0 = -np.log(Ifinaltot/Inot)     
    od1 = -np.log(Ifinaltot/Inot) + (Inot-Ifinaltot)
    
    return ReturnValues(od, od1, Ifinaltot, atoms[0].vlist[1])



