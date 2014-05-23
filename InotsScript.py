# -*- coding: utf-8 -*-
"""
Created on Thu May 15 16:23:12 2014

@author: dng5
"""
import matplotlib.pyplot as plt
import numpy as np
import ImagingModel3 

"""This is a script to run the imaging model for a range of probe intensities"""

time = 0.0002 #s, so up to 200us
steps = 1000
I0range = np.linspace(0.1,5,40)
od0All = np.empty([I0range.size,steps])
od1All = np.empty([I0range.size,steps])
IfinalAll = np.empty([I0range.size,steps])
VatomAll = np.empty([I0range.size,steps+1])

def Simulate(ODinit,index):
    for i in range(I0range.size):
        inot = I0range[i]
        outputTuple = Image(inot,time,steps,ODinit)
        od=outputTuple[0]
        od0All[i,:] = outputTuple[1]
        od1All[i,:] = outputTuple[2]
        IfinalAll[i,:] = outputTuple[3]
        VatomAll[i,:] = outputTuple[4]
    
    #outfile = open("InotsScriptOutputs",'r+')
    np.savez("Data/SimulatedOD"+str(int(ODinit*1000)), od=od, od0All=od0All, od1All=od1All, IfinalAll=IfinalAll, VatomAll=VatomAll, I0range = I0range)
    #outfile.close()