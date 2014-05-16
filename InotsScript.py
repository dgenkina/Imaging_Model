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
I0range = np.logspace(-5,8,20)
od1All = np.empty([I0range.size,steps])
IfinalAll = np.empty([I0range.size,steps])
VinitAll = np.empty([I0range.size])

for i in range(I0range.size):
    inot = I0range[i]
    outputTuple = Image(inot,time,steps)
    od=outputTuple[0]
    od1All[i,:] = outputTuple[1]
    IfinalAll[i,:] = outputTuple[2]
    VinitAll[i] = outputTuple[3]