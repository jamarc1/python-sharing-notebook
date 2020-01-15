# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 08:57:47 2019

@author: JamarcH_Temp
"""


import numpy as np

list = [1,2,3,4,]
arr = np.array(list)
print(arr)

print (np.arange(7))

import SciPy 
from Sci.cluster.vq import kmeans, vq, whiten

from numpy import vstack, array
from numpy.random import rand

data = vstack((rand(100,3) + array([.5,.5,.5]),rand(100,3)))