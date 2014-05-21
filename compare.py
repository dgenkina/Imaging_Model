# -*- coding: utf-8 -*-
"""
Created on Wed May 07 17:02:21 2014

@author: dng5
"""

from pylab import *
import numpy as np

error100 = {}
sdtdev100 = {}
error75 = {}
sdtdev75 = {}
error40 = {}
sdtdev40 = {}
Isatcounts = np.arange(1,80,0.5)

ODrange = np.linspace(1.4,1.5,1)
IsatAvg = np.empty([ODrange.size])
SdtdevAvg = np.empty([ODrange.size])

for i in range(ODrange.size):
    ODinit = ODrange[i]
    #Simulate(ODinit,i)
    simul = np.load("SimulatedOD"+str(i)+".npz")
    for isat in Isatcounts:
        error100[isat] = np.interp(probeCl[times[2]]/times[2]/isat,simul['I0range'], simul['od0All'][:,500]) - Rod0Clean[times[2]]
        sdtdev100[isat] = dot(error100[isat],error100[isat])
        error75[isat] = np.interp(probeCl[times[1]]/times[1]/isat,simul['I0range'], simul['od0All'][:,375]) - Rod0Clean[times[1]]
        sdtdev75[isat] = dot(error75[isat],error75[isat])
        error40[isat] = np.interp(probeCl[times[0]]/times[0]/isat,simul['I0range'], simul['od0All'][:,200]) - Rod0Clean[times[0]] 
        sdtdev40[isat] = dot(error40[isat],error40[isat])
        
    IsatAvg[i] = ( min(sdtdev100, key=sdtdev100.get)+min(sdtdev75, key=sdtdev75.get)+min(sdtdev40, key=sdtdev40.get))/3.0
    SdtdevAvg[i] = (np.interp(IsatAvg[i],Isatcounts,[sdtdev100[isat] for isat in Isatcounts])+np.interp(IsatAvg[i],Isatcounts,[sdtdev75[isat] for isat in Isatcounts])+np.interp(IsatAvg[i],Isatcounts,[sdtdev40[isat] for isat in Isatcounts]))/3.0 
    
SdtdevMin = np.amin(SdtdevAvg)
ODindex = int(np.where(SdtdevAvg==SdtdevMin)[0])
IsatCounts = IsatAvg[ODindex]
ODbest = ODrange[ODindex]

simul = np.load("SimulatedOD"+str(ODindex)+".npz")
for isat in Isatcounts:
    error100[isat] = np.interp(probe[times[2]]/times[2]/isat,simul['I0range'], simul['od0All'][:,500]) - Rod0Av[times[2]][0,:] 
    sdtdev100[isat] = dot(error100[isat],error100[isat])
    error75[isat] = np.interp(probe[times[1]]/times[1]/isat,simul['I0range'], simul['od0All'][:,375]) - Rod0Av[times[1]][0,:] 
    sdtdev75[isat] = dot(error75[isat],error75[isat])
    error40[isat] = np.interp(probe[times[0]]/times[0]/isat,simul['I0range'], simul['od0All'][:,200]) - Rod0Av[times[0]][0,:] 
    sdtdev40[isat] = dot(error40[isat],error40[isat])

graph = plt.figure()
fits = graph.add_subplot(1,1,1)
fits.plot(Isatcounts,[sdtdev100[isat]for isat in Isatcounts], 'r-', linewidth = 2)
fits.plot(Isatcounts,[sdtdev75[isat]for isat in Isatcounts], 'g-',linewidth = 2)
fits.plot(Isatcounts,[sdtdev40[isat]for isat in Isatcounts], 'b-',linewidth = 2)
fits.set_xlabel('Isat [counts/us]', size=15)
fits.set_ylabel('Standard deviation of OD' , size=15)
fits.legend([fits.lines[i] for i in range(3)],['t = 100us','t = 75us', 't=40us'])
fits.set_title('OD='+str(ODbest))
show()

