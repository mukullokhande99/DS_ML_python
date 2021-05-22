# -*- coding: utf-8 -*-
"""
Created on Thu May 20 21:19:44 2021

@author: Mukul
"""

import os
os.chdir("C:/Users/Mukul/Documents")
import pandas as pd
import numpy as np
tel_data=pd.read_csv("Telecom_Data.csv")

#set depe indep var
tel_data.columns
x=tel_data.drop(["phone number","churn"],axis=1)
y= tel_data[["churn"]]
x=pd.get_dummies(x)

#divide train test
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest= train_test_split(x,y,test_size=0.2)

#random forest model
from sklearn.ensemble import RandomForestClassifier as rf
model=rf()
model.fit(xtrain,ytrain)
#apply to testset
pred_churn= model.predict(xtest)

from sklearn.metrics import classification_report as cr
cr(ytest,pred_churn)

#validation 