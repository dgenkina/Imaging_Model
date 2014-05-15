# -*- coding: utf-8 -*-
"""
Created on Thu May 15 16:23:12 2014

@author: dng5
"""
from pylab import *
import numpy as np
import ImagingModel3 

"""This is a script to run the imaging model for a range of probe intensities"""

time = 0.0002 #s, so up to 200us
steps = 100
Inotrange = exp(np.arange(-5,5,0.5))

for i in range(Inotrange.size):
    inot = Inotrange[i]
    outputObject[i] = Image(inot,time,steps)
od[:] = outputObject[:].od
od1All[:] = outputObject[:].od1[steps]
IfinalAll[:] = outputObject[:].Ifinal[steps]
VinitAll[:] = outputObject[:].AtomVelocity
