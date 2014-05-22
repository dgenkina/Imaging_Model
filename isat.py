# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\dng5\.spyder2\.temp.py
"""
from pylab import *
import numpy as np
times = (40.00, 75.00, 100.00)
filerange = {}
filerange[times[0]] = range(281,343)
filerange[times[1]] = range(151,219)
filerange[times[2]] = range(220,280)


ymask = range(226,260)
xmask = range(308,335)
yprobe = range(287,316)
xprobe = range(300,330)
ybgnd = range(204,223)
xbgnd = range(187,193)
isatRange = range(100,200,100)

Rod0stdev = {}
Rod1stdev = {}
isatus = {}
Rod0Av = {}
Rod1Av={}
probe={}
Rod0Clean={}
probeClean={}
probeCl={}
Rod0Cl={}
probeAv={}
probeVar={}

delta = 16913.0

for time in times: 
    Rod0Av[time] = zeros((len(isatRange),len(filerange[time])))
    Rod1Av[time] = zeros((len(isatRange),len(filerange[time])))
    probe[time] = zeros(len(filerange[time]))
    probeVar[time] = zeros(len(filerange[time]))
    probeAv[time] = zeros(len(filerange[time]))
    Rod0Clean[time]=[]
    probeClean[time]=[]
    a = (delta*time*10e-7)**2/3
    t = times.index(time)
    for isat in isatRange:
        i= isatRange.index(isat)
        for filenum in filerange[time]:
            f = filerange[time].index(filenum)
            #print filepath2
            Raw1=raw1[filenum]
            Raw2=raw2[filenum]
            Raw3=raw3[filenum]
            ifin = Raw1-Raw3
            inot = Raw2-Raw3 
            Rod0 = -np.log((ifin)/(inot)) #+ (inot-ifin)/isat
            Rod1 = -np.log((ifin)/(inot)) + (inot-ifin)/isat# - a*(isat/(ifin+isat)-isat/(inot+isat) + np.log((ifin+isat)/(inot+isat)))        
            bgndod = 0.0            
            for x in xbgnd:
                for y in ybgnd:
                    bgndod += Rod0[x,y]/len(ybgnd)/len(xbgnd)
                    
            for x in xmask:
                for y in ymask:
                    probe[time][f] += inot[x,y]/len(xmask)/len(ymask)
                    if Rod0[x,y] != Rod0[x,y]:
                        #print "nan in file" + str(filenum) + "!!!"
                        Rod0[x,y] = 0
                        Rod1[x,y] = 0
                    elif Rod0[x,y]==inf:
                        Rod0[x,y] = 0
                        Rod1[x,y] = 0
                    else:
                        Rod0Av[time][i,f] += Rod0[x,y]/len(ymask)/len(xmask)
                        Rod1Av[time][i,f] += Rod1[x,y]/len(ymask)/len(xmask) 
            Rod0Av[time][i,f] -= bgndod
            Rod1Av[time][i,f] -= bgndod
            
            """Get variance of probe counts to caibrate photoelectons/photon"""
            for x in xprobe:
                for y in yprobe:
                    probeAv[time][f] += inot[x,y]/len(xprobe)/len(yprobe)
        
            for x in xprobe:
                for y in yprobe:
                    probeVar[time][f] += ((probeAv[time][f]-inot[x,y])**2)/len(xprobe)/len(yprobe)

            if probe[time][f]>300.0:
                Rod0Clean[time].append(Rod0Av[time][0,f])
                probeClean[time].append(probe[time][f])
            
        Rod0stdev[time] = np.std(Rod0Av[time], axis=1)
        Rod1stdev[time] = np.std(Rod1Av[time], axis=1)
        probeCl[time] = np.array(probeClean[time])
        Rod0Cl[time] = np.array(Rod0Clean[time])
    isatus[time] = [float(x)/time for x in isatRange]
#plot (isat, odstdev), show()
    #print odavg

#imshow(od), show(), plt.colorbar()
