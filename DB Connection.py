# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:56:06 2019

@author: JamarcH_Temp
"""

import  pyodbc

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ksql028;'
                      'Database=Operations;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('Select * from [dbo].[PO_Attainment] where week_date =22 and year_date=2019')

for row in cursor:
    print(row)