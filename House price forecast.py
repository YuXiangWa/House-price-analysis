# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:59:16 2020

@author: user
"""


import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('House.csv')
X = data
Y = data['Final Price']

x_train, x_test, y_train, y_test = train_test_split(X, Y,
                                                   test_size=0.3,
                                                   random_state=87)
regr = LinearRegression()
regr.fit(x_train, y_train)
y_predict = regr.predict(x_test)
plt.scatter(y_test, y_predict)
plt.plot([0,17500],[0,17500],'r')
plt.xlabel('True Price')
plt.ylabel('Predicted Price')

plt.figure(figsize=(12,7))
plt.subplot(2,2,1)
plt.scatter(data['Type'],data['Final Price'])
plt.xlabel('Type')
plt.ylabel('Price')
plt.subplot(2,2,2)
plt.scatter(data['Unit Price'],data['Final Price'])
plt.xlabel('Unit Price')
plt.ylabel('Price')
plt.subplot(2,2,3)
plt.scatter(data['Flooring'],data['Final Price'])
plt.xlabel('Flooring')
plt.ylabel('Price')
plt.subplot(2,2,4)
plt.scatter(data['Parking Space'],data['Final Price'])
plt.xlabel('Parking Space')
plt.ylabel('Price')