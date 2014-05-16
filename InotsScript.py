# -*- coding: utf-8 -*-
"""
Created on Thu May 15 16:23:12 2014

@author: dng5
"""

import numpy as np
import ImagingModel3 

"""This is a script to run the imaging model for a range of probe intensities"""

time = 0.0002 #s, so up to 200us
steps = 100
Inotrange = np.exp(np.arange(-5,5,0.5))
od = []
od1All = []
IfinalAll = []
VinitAll = []

for i in range(Inotrange.size):
    inot = Inotrange[i]
    outputTuple = Image(inot,time,steps)
    od.append(outputTuple[0])
    od1All.append(outputTuple[1])
    IfinalAll.append(outputTuple[2])
    VinitAll.append(outputTuple[3])