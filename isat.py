# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\dng5\.spyder2\.temp.py
"""
from pylab import *
import numpy as np
import scipy
import scipy.ndimage, scipy.optimize, scipy.special, scipy.stats

"""This takes three raw images, selects a small square at the center which 
should have roughly the same probe intensity and atom number accross it, and
finds the average OD and probe intensity in that region for a myriad of files"""

"""Define the files to read in"""
times = (40.00, 75.00, 100.00)
filerange = {}
filerange[times[0]] = range(281,343)
filerange[times[1]] = range(151,219)
filerange[times[2]] = range(220,280)

"""Set up the range of teh small square in the middle, as well as a small 
square away from the atoms where the background OD will be measured"""
ymask = range(226,260)
xmask = range(308,335)
ROImask = np.ones_like(raw1[151])
ROImask[308:335,226:260]=0
yprobe = range(287,316)
xprobe = range(300,330)
ybgnd = range(204,223)
xbgnd = range(187,193)
BgndMask = np.ones_like(raw1[151])
BgndMask[100:490,65:390]=0
BgndMask[140:460,100:370]=1

"""Define all the dictionaries - the keys of these dictionaries are the three
imaging times, 40.00, 75.00, and 100.00 and they point to arrays of values 
for each file at that imaging time"""
Rod0stdev = {}
isatus = {}
Rod0Av = {}
probe={}
Rod0Clean={}
probeClean={}
probeCl={}
Rod0Cl={}
probeAv={}
probeVar={}


delta = 16913.0

def zeroNansInfs(x):
    if x!=x:
        return 0
    elif np.isinf(x):
        return 0
    else:
        return x
zeroNansInfsVector = np.vectorize(zeroNansInfs, otypes=[np.float])

"""Loop over the three different imaging times"""
for time in times: 
    Rod0Av[time] = zeros(len(filerange[time]))
    probe[time] = zeros(len(filerange[time]))
    probeVar[time] = zeros(len(filerange[time]))
    probeAv[time] = zeros(len(filerange[time]))
    Rod0Clean[time]=[]
    probeClean[time]=[]
    a = (delta*time*10e-7)**2/3
    t = times.index(time)

    """loop over all the files taken at that imaging time"""
    for filenum in filerange[time]:
        f = filerange[time].index(filenum)
        Raw1=raw1[filenum]
        Raw2=raw2[filenum]
        Raw3=raw3[filenum]
        ifin = Raw1-Raw3
        inot = Raw2-Raw3 
        
        """Calculate the OD and high intensity corrected OD"""
        Rod0Raw = -np.log((ifin)/(inot)) #+ (inot-ifin)/isat
        Rod0 = zeroNansInfsVector(Rod0Raw)
         
        """Check the OD in the square of interest for Nans and infinitys,
        then average the OD over the square""" 
        Rod0masked = np.ma.masked_array(Rod0,ROImask)
        probeMasked = np.ma.masked_array(inot,ROImask)
        Rod0Av[time][f]=np.ma.average(Rod0masked)
        probe[time][f]=np.ma.average(probeMasked)
                    
        bgndMasked = np.ma.masked_array(Rod0,BgndMask)
        bgndod2 = np.ma.average(bgndMasked)
        bgndod = 0
        """Use the defined background square to find the average background OD"""
        for x in xbgnd:
            for y in ybgnd:
                bgndod += Rod0[x,y]/len(ybgnd)/len(xbgnd)
                    
        """Subtract the average background from the average OD"""            
        Rod0Av[time][f] -= bgndod2

        """Get variance of probe counts to caibrate photoelectons/photon"""
        probeSmooth=scipy.ndimage.gaussian_filter(inot, sigma=4);
        probeNoise=probeSmooth-inot
        num = 0            
        for x in xprobe:
            for y in yprobe:
                if inot[x,y]<4095: #throw out points where the camera saturates
                    num+=1
                    probeAv[time][f] += inot[x,y]
        probeAv[time][f] = probeAv[time][f]/num
    
        for x in xprobe:
            for y in yprobe:
                if inot[x,y]<4095:
                    probeVar[time][f] += ((probeNoise[x,y])**2)/num

        """Take out low probe intensity points because they are confusing"""
        if probe[time][f]>300.0:
            Rod0Clean[time].append(Rod0Av[time][f])
            probeClean[time].append(probe[time][f])
        
    Rod0stdev[time] = np.std(Rod0Av[time])
    
    """Convert the average probe and OD to numpy arrays for future convenience"""
    probeCl[time] = np.array(probeClean[time])
    Rod0Cl[time] = np.array(Rod0Clean[time])
   # isatus[time] = [float(x)/time for x in isatRange]
#plot (isat, odstdev), show()
    #print odavg

#imshow(od), show(), plt.colorbar()
