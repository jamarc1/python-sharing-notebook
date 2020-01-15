# convert to array
return [x for x in forecast[0, :]]
# evaluate the persistence model
def make_forecasts(model, n_batch, train, test, n_lag, n_seq,n_features):
forecasts = list()
for i in range(len(test)):
X, y = test[i, :n_lag * n_features], test[i, -n_seq:]
# make forecast
forecast = forecast_lstm(model, X, n_lag)
# store the forecast
forecasts.append(forecast)
return forecasts
# invert differenced forecast
def inverse_difference(last_ob, forecast):
# invert first forecast
inverted = list()
inverted.append(forecast[0] + last_ob)
# propagate difference forecast using inverted first value
for i in range(1, len(forecast)):
inverted.append(forecast[i] + inverted[i-1])
return inverted
# inverse data transform on forecasts
def inverse_transform(series, forecasts, scaler, n_test):
inverted = list()
print ('Forecasts')
print (forecasts)
for i in range(len(forecasts)):
# create array from forecast
forecast = array(forecasts[i])
temp = forecasts
# print len(forecasts)
#   print len(forecast)
#      print 'forecast'
print (forecast)
forecast = forecast.reshape(1, len(forecast))
# invert scaling
#X : array-like, shape [n_samples, n_features]
inv_scale = scaler.inverse_transform(forecast)
inv_scale = inv_scale[0, :]
# invert differencing
index = len(series) - n_test + i - 1
last_ob = series.values[index]
inv_diff = inverse_difference(last_ob, inv_scale)
# store
inverted.append(inv_diff)
return inverted
#ValueError: operands could not be broadcast together with shapes (1,11) (2,) (1,11)
# evaluate the RMSE for each forecast time step
def evaluate_forecasts(test, forecasts, n_lag, n_seq):
for i in range(n_seq):
actual = [row[i] for row in test]
predicted = [forecast[i] for forecast in forecasts]
runfile('C:/Users/jamarch_temp/.spyder-py3/webscraper_new.py', wdir='C:/Users/jamarch_temp/.spyder-py3')
soup = BeautifulSoup(response.text, 'html.parser')
soup.findAll('a')
one_a_tag = soup.findAll(‘a’)[36]
one_a_tag = soup.findAll('a')[36]
link = one_a_tag[‘href’]
link = one_a_tag['href']
download_url = 'http://web.mta.info/developers/'+ link
urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
time.sleep(1)
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
url = 'https://www.georgiapublicnotice.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
soup.findAll('a')
one_a_tag = soup.findAll('a')[36]
link = one_a_tag['href']
runfile('C:/Users/jamarch_temp/.spyder-py3/webscraper_new.py', wdir='C:/Users/jamarch_temp/.spyder-py3')
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
#url = 'https://web.mta.info/developers/turnstile.html'
url = 'https://www.georgiapublicnotice.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
soup.findAll('a')
for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
runfile('C:/Users/jamarch_temp/.spyder-py3/webscraper_new.py', wdir='C:/Users/jamarch_temp/.spyder-py3')

## ---(Fri Sep 13 08:49:56 2019)---
runfile('C:/Users/jamarch_temp/.spyder-py3/webscraper_new.py', wdir='C:/Users/jamarch_temp/.spyder-py3')
runfile('C:/Users/jamarch_temp/.spyder-py3/multi_uni.py', wdir='C:/Users/jamarch_temp/.spyder-py3')
runfile('C:/Users/jamarch_temp/.spyder-py3/temp.py', wdir='C:/Users/jamarch_temp/.spyder-py3')
runfile('C:/Users/jamarch_temp/.spyder-py3/Multiple.py', wdir='C:/Users/jamarch_temp/.spyder-py3')
x = [0,1]
i = 0
i, x[i] = 1,2
print (x)
num1 =  1
num2 = 2
multiply = num1*num2
print('The multiple of {0} and {1}'.format(num1, num2, sum))
num1 = input('Enter First number: ')
2
num2 = input('Enter second number: ')

## ---(Tue Nov 26 08:53:22 2019)---
runfile('C:/Users/jamarch_temp/Downloads/spotipy-master (1)/spotipy-master/examples/user_playlists.py', wdir='C:/Users/jamarch_temp/Downloads/spotipy-master (1)/spotipy-master/examples')
import spotipy
sp = spotipy.Spotify()

results = sp.search(q='weezer', limit=20)
for i, t in enumerate(results['tracks']['items']):
    print ' ', i, t['name']

import spotipy
sp = spotipy.Spotify()
pip install spotipy
easy_install spotipy
pip3 install spotipy
pip freeze
runfile('C:/Users/jamarch_temp/Downloads/spotipy-master (1)/spotipy-master/examples/user_playlists.py', wdir='C:/Users/jamarch_temp/Downloads/spotipy-master (1)/spotipy-master/examples')
runfile('C:/Users/jamarch_temp/.spyder-py3/Multiple.py', wdir='C:/Users/jamarch_temp/.spyder-py3')
runfile('C:/Users/jamarch_temp/.spyder-py3/Analyze.py', wdir='C:/Users/jamarch_temp/.spyder-py3')
import tkinter as tk
from tkinter import filedialog
import statsmodels.api as sm
import pandas as pd
from pandas import DataFrame
root = tk.Tk()
canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()
runfile('C:/Users/jamarch_temp/.spyder-py3/Analyze.py', wdir='C:/Users/jamarch_temp/.spyder-py3')
import tkinter as tk
import statsmodels.api as sm
pip install spotipy
import spotipy
import spotipy.util as util
runfile('C:/Users/jamarch_temp/Downloads/spotipy-master (1)/spotipy-master/examples/user_playlists.py', wdir='C:/Users/jamarch_temp/Downloads/spotipy-master (1)/spotipy-master/examples')
runfile('C:/Users/jamarch_temp/Downloads/spotipy-master (1)/spotipy-master/examples/user_playlists_1.py', wdir='C:/Users/jamarch_temp/Downloads/spotipy-master (1)/spotipy-master/examples')
runfile('C:/Users/jamarch_temp/.spyder-py3/Analyze.py', wdir='C:/Users/jamarch_temp/.spyder-py3')