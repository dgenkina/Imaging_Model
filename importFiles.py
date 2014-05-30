# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 09:25:35 2014

@author: dng5
"""

from pylab import *
import numpy as np

filerange = range(1,10)
#filerange += range(281,343)

raw1={}
raw2={}
raw3={}
for filenum in filerange:
    filepath =  "C:/Data/2013/September/06/Flea3_06Sep2013_000"
    filepath += str(filenum)
    filepath1 = filepath + "_Raw1"
    filepath2 = filepath + "_Raw2"
    filepath3 = filepath + "_Raw3"  
    savedfilepath = "RawData/Sept06_"+str(filenum)
    Raw1=np.genfromtxt(filepath1, unpack=True, skiprows = 1)
    Raw2=np.genfromtxt(filepath2, unpack=True, skiprows = 1)
    Raw3=np.genfromtxt(filepath3, unpack=True, skiprows = 1)
    np.savez(savedfilepath, Raw1=Raw1, Raw2=Raw2, Raw3=Raw3)    
    #print filepath2
    #raw1[filenum] = np.genfromtxt(filepath1, unpack=True, skiprows = 1)
    #raw2[filenum] = np.genfromtxt(filepath2, unpack=True, skiprows = 1)
    #raw3[filenum] = np.genfromtxt(filepath3, unpack=True, skiprows = 1)