# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:20:29 2019

@author: JamarcH_Temp
"""




import pandas as pd


df = pd.read_excel(r'C:\Users\jamarch_temp\Desktop\Projects\Logistics\Ocean KPIs.xlsx', sheet_name = 'Sheet1')
print (df)


data = pd.read_excel(r'C:\Users\jamarch_temp\Desktop\Projects\Logistics\Ocean KPIs.xlsx', sheet_name = 'Sheet1')
df = pd.DataFrame(data, columns= ['Ocean Transporation'])
print (df)