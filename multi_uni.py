# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 14:56:23 2019

@author: Jamarc.Hurd
"""

from pandas import DataFrame
from pandas import Series
from pandas import concat
from pandas import read_csv
from pandas import datetime
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from math import sqrt
from matplotlib import pyplot
from numpy import array
import numpy as np
import pandas as pd

# date-time parsing function for loading the dataset
def parser(x):
   return datetime.strptime(x, '%m/%d/%y')

# convert time series into supervised learning problem
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
   """
    Frame a time series as a supervised learning dataset.
    Arguments:
        data: Sequence of observations as a list or NumPy array.
        n_in: Number of lag observations as input (X).
        n_out: Number of observations as output (y).
        dropnan: Boolean whether or not to drop rows with NaN values.
    Returns:
        Pandas DataFrame of series framed for supervised learning.
    """
   n_vars = 1 if type(data) is list else data.shape[1]
   df = DataFrame(data)
   cols, names = list(), list()
   # input sequence (t-n, ... t-1)
   for i in range(n_in, 0, -1):
      cols.append(df.shift(i))
      names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
   # forecast sequence (t, t+1, ... t+n)
   for i in range(0, n_out):
      cols.append(df.shift(-i))
      if i == 0:
         names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
      else:
         names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
   # put it all together
   agg = concat(cols, axis=1)
   agg.columns = names
   # drop rows with NaN values
   if dropnan:
      agg.dropna(inplace=True)
   #agg = agg.
   #agg.drop(columns=['var2(t)','var2(t+1)','var2(t+2)','var2(t+3)','var2(t+4)'], inplace = True)
   print (agg)
   return (agg)

# transform series into train and test sets for supervised learning
def prepare_data(raw_data, n_test, n_lag, n_seq):
   """
   :param raw_data: pandas DF containing input data
   :param n_test: number of test data point to forecast for
   :param n_lag: how many steps back to include
   :param n_seq: how many steps forward to forecast
   :return: 2D array [samples, features]
   """
   diff_raw_data = raw_data.diff(axis=0)
   diff_values = diff_raw_data.values

   # rescale values to -1, 1
   scaler = MinMaxScaler(feature_range=(-1, 1))
   scaled_values = scaler.fit_transform(diff_values)
   # transform into supervised learning problem X, y
   supervised = series_to_supervised(scaled_values, n_lag, n_seq)
   supervised_values = supervised.values
   # split into train and test sets
   train, test = supervised_values[0:-n_test], supervised_values[-n_test:]
   return scaler, train, test

# fit an LSTM network to training data
def fit_lstm(train, n_lag, n_seq, n_batch, nb_epoch, n_neurons,n_features):
   """
   :param train: 2D array [samples, features]
   :param n_lag: time steps back to include
   :param n_seq: number of time steps forward to forecast for
   :param n_batch: We require predictions to be made at each time step of the test dataset. batch = 1
   :param nb_epoch:
   :param n_neurons:
   :return:
   """
   # reshape training into [samples, timesteps, features]
   # split into input and outputs
   X, y = train[:, :n_lag * n_features], train[:, -n_seq:]
   X = X.reshape((X.shape[0], n_lag, n_features))
   """
   This first requires that the training dataset be transformed from a 2D array [samples, features] 
   to a 3D array [samples, timesteps, features]. We will fix time steps at 1, so this change is straightforward.
   """
   # design network
   model = Sequential()
   model.add(LSTM(n_neurons, batch_input_shape=(n_batch, X.shape[1], X.shape[2]), stateful=True))
   model.add(Dense(y.shape[1]))  #TODO what is up with this magic number copied unistep
   model.compile(loss='mean_squared_error', optimizer='adam')
   # fit network
   for i in range(nb_epoch):
      model.fit(X, y, epochs=1, batch_size=n_batch, verbose=0, shuffle=False)
      model.reset_states()
   return model

# make one forecast with an LSTM,
def forecast_lstm(model, X, n_lag):
   """
   :param model: use the fit LSTM network to make forecasts
   :param X: 2D array [samples, features]
   :param n_batch: We require predictions to be made at each time step of the test dataset. batch_size = 1
   :return:
   """
   # reshape input pattern to [samples, timesteps, features]
   X = X.reshape(1, n_lag, len(X))
   # make forecast
   forecast = model.predict(X,batch_size=1)
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
      rmse = sqrt(mean_squared_error(actual, predicted))
      #print predicted
      print('t+%d RMSE: %f' % ((i+1), rmse))

# plot the forecasts in the context of the original dataset
def plot_forecasts(series, forecasts, n_test):
   # plot the entire dataset in blue
   pyplot.plot(series.values)
   # plot the forecasts in red
   for i in range(len(forecasts)):
      off_s = len(series) - n_test + i - 1
      off_e = off_s + len(forecasts[i]) + 1
      xaxis = [x for x in range(off_s, off_e)]
      yaxis = [series.values[off_s]] + forecasts[i]
      pyplot.plot(xaxis, yaxis, color='red')
   # show the plot
   pyplot.show()

# load dataset
raw_data = read_csv('/Users/randino/desktop/kids2_weekly.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
raw_data = raw_data[['order_qty']]
# configure
n_lag = 1
n_seq = 12           # Number of time steps to take
n_test = 10          # A total of 10 n_seq(5) forecasts are required
n_epochs = 1500
n_batch = 1
n_neurons = 1
n_features = len(raw_data.columns)
# prepare data
scaler, train, test = prepare_data(raw_data, n_test, n_lag, n_seq)
# fit model
#print ('train')
#print train.shape
#print train

model = fit_lstm(train, n_lag, n_seq, n_batch, n_epochs, n_neurons,n_features)
# make forecasts
forecasts = make_forecasts(model, n_batch, train, test, n_lag, n_seq,n_features)
# inverse transform forecasts and test
forecasts = inverse_transform(raw_data, forecasts, scaler, n_test+2)
actual = [row[n_lag:] for row in test]
actual = inverse_transform(raw_data, actual, scaler, n_test+2)
# evaluate forecasts
evaluate_forecasts(actual, forecasts, n_lag, n_seq)
# plot forecasts
plot_forecasts(raw_data, forecasts, n_test+2)
print ("forecasts")
print (forecasts)
