# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:20:11 2019

@author: JamarcH_Temp
"""

import tkinter as tk
from tkinter import filedialog

import pandas as pd

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

df.head().style.hide_index()

import pandas as ab

df=ab.DataFrame(dict(col_1 =[200,50,60,500],
                       col_2 =[1500,-4,-8,8000])
                       )

print(df)

def color_postive_red(df):
    color = 'red' if df > 100 else 'blue'
    return 'color: %s' % color
    
df.style.__format__('jamarc')


