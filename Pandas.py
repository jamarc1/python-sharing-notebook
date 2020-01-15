# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:54:23 2019

@author: JamarcH_Temp
"""
import pandas as pd
from pandas import Series, DataFrame

mjp = Series([5,4,3,2,1,])
print (mjp.values)

print (mjp.index)

jeeva = Series([5,4,3,2,1,-7,-29], index=['a','b','c','d','e','f','g'])
print (jeeva)

print (jeeva['a'])

jeeva['d'] = 9
print (jeeva)

jeeva[['a','b','c']]

print(jeeva[jeeva>0])

import numpy as np
np.mean(jeeva)

print('b' in jeeva)


player_salary = {'Jamarc': 1000000, 'Bijoy': 50000, 'Jon': 10 }
new_player = Series(player_salary)
print(new_player)


players = ['Mack','Marcel','Abdul','Sabir','Corey']
player_1 = Series(player_salary, index = players)
print(player_1)

states ={'State' :['Georgia','Alabama', 'Florida', 'South Carolina'],'Population' :[22,32,11,44],'Language' :['English','Country','Geechie','Creole']}

South = DataFrame(states)
print(South)


New_South = DataFrame(states, columns =['State', 'Language','Population', 'Per Capita Income' ], index =['a','b','c','d'])
print(New_South)
print (New_South ['State'])

New_South.Population
New_South.ix[3]
New_South

New_South['Per Capita Income']

print (New_South.columns)
print (New_South['State'])


New_South.Population
New_South['Per Capita Income'] = np.arange(4)
New_South
series = Series([44,33,22], index=['b','c','d'])
New_South['Per Capita Income'] = series
New_South


New_South['Development'] = New_South.State =='Atlanta'
New_South

del New_South['Development']
New_South


new_data = {'Jamarc': {2009: 80, 2012: 90, 2015: 100}, 'Hurd':{2010: 10, 2013: 20, 2016: 30}}
elections =DataFrame(new_data)
elections.T


DataFrame(new_data, index =[2009,2011])

ex = {'Georgia':elections['Jamarc'][:-1], 'Atlanta': elections['Hurd'][:2]}
px =DataFrame(ex)
px

from IPython.display import Image
i = Image(filename = 'Constructors.png')
print(i)
