# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 18:25:32 2014

@author: dng5
"""
import matplotlib.pyplot as plt
times = (50, 200, 500)
fig = plt.figure()
panel = {}
line1 = {}
line2 = {}
line3 = {}

for time in times:
    t = times.index(time)+1
    panel[time] = fig.add_subplot(1,len(times),t)
    line1[time],=panel[time].plot(Inotrange, od0[:,time], 'bo')
    line2[time],=panel[time].plot(Inotrange, od0[:,time]-od1[:,time] + od, 'g-',linewidth=2)
   # line3[time],=panel[time].plot(Inotrange, od0[:,time]-od2[:,time] + od, 'r-',linewidth=2)
    panel[time].set_xlabel("I/Isat", size=15)
    panel[time].set_ylabel("OD", size=15)
    panel[time].set_title("time =  "+str(int(trange[time]*1000000)) + " us", size=15)
    panel[time].set_xscale('log')
    panel[time].set_yscale('log')
fig.show()
