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
         
"""now, make a grid"""
zfinal = 0.0001 #m, so ~100um
tfinal = 0.0002 #s, so up to 200us
dt = tfinal/1000.00
dz = zfinal/300.00
zrange = np.arange(0,zfinal,dz)
trange = np.arange(0,tfinal,dt)
Inotrange = np.exp(np.arange(-2, 2, 0.5))
num = zeros([zrange.size])


def n(x):
        return exp(-(x-zfinal/2)**2/(5.0e-10)) #approx. atom density
        
num[:] = ([n(z) for z in zrange])
numsum = np.sum(num*dz)
num = num*6.0e12/numsum
    
od = 6.0e12*A

"define initial conditions"
Inots = np.outer(Inotrange,np.ones(trange.size))
Times = np.outer(np.ones(Inotrange.size),trange)   
I = zeros([len(Inotrange),len(zrange)+1,len(trange)])
D = zeros([len(Inotrange),len(zrange),len(trange)+1])
I[:,0,:] = Inots
Ifinal = zeros([len(Inotrange),len(trange)])
Ifinaltot = zeros([len(Inotrange),len(trange)])
rate = zeros([len(Inotrange)])

for t in range(trange.size):
  
    for z in range(zrange.size):
     
        rate = (I[:,z,t])/(1+(D[:,z,t]**2)+I[:,z,t])
        I[:,z+1,t]=I[:,z,t]-A*num[z]*rate*dz
        D[:,z,t+1]=D[:,z,t]+B*rate*dt
        
    Ifinal[:,t] = I[:,len(zrange),t]
    
Ifinaltot = np.cumsum(Ifinal*dt,axis=1)/(Times+dt)
od0 = -np.log(Ifinaltot/Inots)     
od1 = -np.log(Ifinaltot/Inots) + (Inots-Ifinaltot)
od2 = -np.log(Ifinaltot/Inots) + (Inots-Ifinaltot) - ((B*Times)**2)*(1/(Ifinaltot+1)-1/(Inots+1) + np.log((Ifinaltot+1)/(Inots+1)))/3        
        