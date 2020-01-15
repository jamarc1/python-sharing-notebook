# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 08:29:03 2019

@author: Jamarc.Hurd
"""

import tkinter as tk
from tkinter import filedialog
import statsmodels.api as sm

import pandas as pd
from pandas import DataFrame


root = tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    global df
    
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_excel (import_file_path)
    print(df)

browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica'
, 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()

print(df)



df.head(7)[df.columns[1:20]]


import statsmodels.api as sm

data  = {'Week':[1,2,3,4,5],'ASIN':['B000YDDF6O','B000YDDF6O','B000YDDF6O','B000YDDF6O','B000YDDF6O'],
 'Open Purchase Qty':[48642,22566,68844,62639,62748],'Avail Inventory':[3378,11847,15442,17322,5718],'Unit Ordered':[3755,5000,6702,10389,17523
] }


df = pd.DataFrame(data)

print(df)
 
x = df[['Avail Inventory','Open Purchase Qty']]

y = df['Unit Ordered']



x =sm.add_constant(x)

model = sm.OLS(y,x).fit()

predictions = model.predict(x)

print_model = model.summary()

print(print_model)