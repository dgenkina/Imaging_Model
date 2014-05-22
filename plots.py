# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 18:25:32 2014

@author: dng5
"""
import matplotlib.pyplot as plt



"""initialVelocities = plt.figure()
velocities = initialVelocities.add_subplot(1,1,1)
velOfProbe = velocities.plot(I0range,VinitAll, 'bo')
highIlim = velocities.plot(I0range,[Gamma*vrecoil*time/steps/2 for x in I0range] ,'g-')
lowIlim = velocities.plot(I0range,Gamma*vrecoil*time*I0range/steps/2 ,'r-')
velocities.set_xlabel("I/Isat", size=15)     
velocities.set_ylabel("Initial velocity of 1st atom [m/s]", size=15)
velocities.set_yscale('log')
velocities.set_xscale('log')
velocities.legend((velocities.lines[0],velocities.lines[1],velocities.lines[2]),("simulation","high intensity limit", "low intensity limit"), loc ="upper left")
initialVelocities.show()"""


"""odpanel = {}
line1 = {}
line2 = {}
line3 = {}

for t in range(len(timeIndexes)):
    index = timeIndexes[t]
    odpanel[t] = odfigure.add_subplot(1,len(timeIndexes),t+1)
    line1[t],=odpanel[t].plot(I0range, od0All[:,index], 'bo')
    line2[t],=odpanel[t].plot(I0range, od0All[:,index]-od1All[:,index] + od, 'g-',linewidth=2)
   # line3[time],=panel[time].plot(Inotrange, od0[:,time]-od2[:,time] + od, 'r-',linewidth=2)
    odpanel[t].set_xlabel("I/Isat", size=15)
    odpanel[t].set_ylabel("OD", size=15)
    odpanel[t].set_title("time =  "+str(index/5) + " us", size=15)
    odpanel[t].set_xscale('log')
    odpanel[t].set_yscale('log')
odfigure.show()"""


