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
Isatcounts = range(1,80,2)
for isat in Isatcounts:
    error100[isat] = np.interp(probe[times[2]]/times[2]/isat,Inotrange, od0[:,500]) - Rod0Av[times[2]][0,:] 
    sdtdev100[isat] = dot(error100[isat],error100[isat])
    error75[isat] = np.interp(probe[times[1]]/times[1]/isat,Inotrange, od0[:,375]) - Rod0Av[times[1]][0,:] 
    sdtdev75[isat] = dot(error75[isat],error75[isat])
    error40[isat] = np.interp(probe[times[0]]/times[0]/isat,Inotrange, od0[:,200]) - Rod0Av[times[0]][0,:] 
    sdtdev40[isat] = dot(error40[isat],error40[isat])

graph = plt.figure()
fits = graph.add_subplot(1,1,1)
fits.plot(Isatcounts,[sdtdev100[isat]for isat in Isatcounts], 'r-', linewidth = 2)
fits.plot(Isatcounts,[sdtdev75[isat]for isat in Isatcounts], 'g-',linewidth = 2)
fits.plot(Isatcounts,[sdtdev40[isat]for isat in Isatcounts], 'b-',linewidth = 2)
fits.set_xlabel('Isat [counts/us]', size=15)
fits.set_ylabel('Standard deviation of OD' , size=15)
fits.legend([fits.lines[i] for i in range(3)],['t = 100us','t = 75us', 't=40us'])
show()
