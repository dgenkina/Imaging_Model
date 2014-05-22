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
sdtdevTot={}
Isatcounts = np.arange(1,80,0.5)

ODrange = np.linspace(1.55,1.7,40)
IsatMin = np.empty([ODrange.size])
SdtdevT = np.empty([ODrange.size])

for i in range(ODrange.size):
    ODinit = ODrange[i]
    #Simulate(ODinit,i)
    simul = np.load("SimulatedOD"+str(int(ODinit*1000))+".npz")
    for isat in Isatcounts:
        error100[isat] = np.interp(probeCl[times[2]]/times[2]/isat,simul['I0range'], simul['od0All'][:,500]) - Rod0Clean[times[2]]
        sdtdev100[isat] = dot(error100[isat],error100[isat])
        error75[isat] = np.interp(probeCl[times[1]]/times[1]/isat,simul['I0range'], simul['od0All'][:,375]) - Rod0Clean[times[1]]
        sdtdev75[isat] = dot(error75[isat],error75[isat])
        error40[isat] = np.interp(probeCl[times[0]]/times[0]/isat,simul['I0range'], simul['od0All'][:,200]) - Rod0Clean[times[0]] 
        sdtdev40[isat] = dot(error40[isat],error40[isat])
        sdtdevTot[isat]=sdtdev40[isat]+sdtdev75[isat]+sdtdev100[isat]        
        
    IsatMin[i] = min(sdtdevTot, key=sdtdevTot.get)
    SdtdevT[i] = np.interp(IsatMin[i],Isatcounts,[sdtdevTot[isat] for isat in Isatcounts])
    
SdtdevMin = np.amin(SdtdevT)
ODindex = int(np.where(SdtdevT==SdtdevMin)[0])
IsatCounts = IsatMin[ODindex]
ODbest = ODrange[ODindex]

simul = np.load("SimulatedOD"+str(int(ODbest*1000))+".npz")
for isat in Isatcounts:
    error100[isat] = np.interp(probeCl[times[2]]/times[2]/isat,simul['I0range'], simul['od0All'][:,500]) - Rod0Cl[times[2]]
    sdtdev100[isat] = dot(error100[isat],error100[isat])
    error75[isat] = np.interp(probeCl[times[1]]/times[1]/isat,simul['I0range'], simul['od0All'][:,375]) - Rod0Cl[times[1]]
    sdtdev75[isat] = dot(error75[isat],error75[isat])
    error40[isat] = np.interp(probeCl[times[0]]/times[0]/isat,simul['I0range'], simul['od0All'][:,200]) - Rod0Cl[times[0]]
    sdtdev40[isat] = dot(error40[isat],error40[isat])
    sdtdevTot[isat]=sdtdev40[isat]+sdtdev75[isat]+sdtdev100[isat]    

graph = plt.figure()
fits = graph.add_subplot(1,1,1)
fits.plot(Isatcounts,[sdtdev100[isat]for isat in Isatcounts], 'r-', linewidth = 2)
fits.plot(Isatcounts,[sdtdev75[isat]for isat in Isatcounts], 'g-',linewidth = 2)
fits.plot(Isatcounts,[sdtdev40[isat]for isat in Isatcounts], 'b-',linewidth = 2)
fits.plot(Isatcounts,[sdtdevTot[isat]for isat in Isatcounts], 'd-',linewidth = 2)
fits.set_xlabel('Isat [counts/us]', size=15)
fits.set_ylabel('Variance of OD' , size=15)
fits.legend([fits.lines[i] for i in range(4)],['t = 100us','t = 75us', 't=40us', 'total'])
fits.set_title('OD='+str(ODbest))
show()


timeIndexes = (200, 375, 500)
odfigure = plt.figure()
odpanel = odfigure.add_subplot(1,1,1)
color={}
color[0]='b'
color[1]='g'
color[2]='r'
for t in range(len(timeIndexes)):
    index = timeIndexes[t]
    odpanel.plot(probeCl[times[t]]/times[t]/IsatCounts,  Rod0Cl[times[t]] , color[t]+'o')
    odpanel.plot(simul['I0range'], simul['od0All'][:,index], color[t]+'-',linewidth=2)
    odpanel.set_xlabel("I/Isat", size=15)
    odpanel.set_ylabel("OD", size=15)
odpanel.legend((odpanel.lines[0],odpanel.lines[2],odpanel.lines[4]),('t=40us','t=75us','t=100us'))
odpanel.set_xlim(0,3)
odpanel.set_title('Isat = '+str(IsatCounts)+' counts/us')
odfigure.show()

