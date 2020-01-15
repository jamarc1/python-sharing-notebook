# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:46:12 2019

@author: Jamarc.Hurd
"""

import tkinter as tk
from tkinter import filedialog
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams

rcParams['figure.figsize'] = 15, 6

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


df.head(7)[df.columns[0:6]]



from statsmodels.tsa.stattools import acf, pacf, adfuller

lag_acf = acf(df, nlags=20)
lag_pacf = pacf(df, nlags=20, method='ols')

#Plot ACF: 
plt.subplot(121) conda l
plt.plot(lag_acf)
plt.axhline(y=0,linestyle='--',color='gray')
plt.axhline(y=-1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
plt.axhline(y=1.96/np.sqrt(len(ts_log_diff)),linestyle='--',color='gray')
plt.title('Autocorrelation Function')


df.plot.line(x = 'Week', 
             y = 'Avail Inventory')
plt.show()



from statsmodels.tsa.api import ExponentialSmoothing, SimpleExpSmoothing, Holt
import pandas as pd
import numpy as np
# Simple Exponential Smoothing
fit1 = SimpleExpSmoothing(df).fit(smoothing_level=0.2,optimized=False)
fcast1 = fit1.forecast(12).rename(r'$\alpha=0.2$')
# plot
fcast1.plot(marker='o', color='blue', legend=True)
fit1.fittedvalues.plot(marker='o',  color='blue')









