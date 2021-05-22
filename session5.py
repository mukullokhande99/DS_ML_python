# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:03:55 2021

@author: Mukul
"""

from sklearn.model_selection import train_test_split
import os
os.chdir("C:/Users/Mukul/Documents")
import pandas as pd
import numpy as np
com_data=pd.read_csv("Computer_Data.csv")

#to divide data into training and testset
x=com_data.drop("price",axis=1) #independent var
#com_data.columns
#x= cp,_data[['A','B']]


y=com_data[["price"]] #dependent var
#get dummy var against independent var
x=pd.get_dummies(x)
#divide data
xtrain, xtest, ytrain, ytest= train_test_split(x,y,test_size=0.30)

#session 6
#linear reg
from sklearn.linear_model import LinearRegression
model= LinearRegression()
model.fit(xtrain, ytrain)

#apply model to testset
predicted_price= model.predict(xtest)

#validation
from sklearn.metrics import mean_absolute_error
mean_absolute_error(ytest, predicted_price)

#dump model to file
import pickle
filename= "price_prediction_model.sav"
pickle.dump(model,open(filename,'wb'))

#load model and provide input

#logistic reg

