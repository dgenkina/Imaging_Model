# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 09:25:35 2014

@author: dng5
"""

from pylab import *
from numpy import *

filerange = range(151,280)
filerange += range(281,343)

raw1={}
raw2={}
raw3={}
for filenum in filerange:
    filepath =  "C:/Data/2013/September/17/Flea3_17Sep2013_0"
    filepath += str(filenum)
    filepath1 = filepath + "_Raw1"
    filepath2 = filepath + "_Raw2"
    filepath3 = filepath + "_Raw3"  
    #print filepath2
    raw1[filenum] = np.genfromtxt(filepath1, unpack=True, skiprows = 1)
    raw2[filenum] = np.genfromtxt(filepath2, unpack=True, skiprows = 1)
    raw3[filenum] = np.genfromtxt(filepath3, unpack=True, skiprows = 1)