# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 13:23:12 2019

@author: Jamarc.Hurd
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

df = pd.read_csv("C:\\Users\\jamarch_temp\\OneDrive - Kids II\\Desktop\\Supply Orders\\Amazon\\Master Amazon DataSet.xlsx")
