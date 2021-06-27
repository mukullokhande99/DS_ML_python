# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 21:37:35 2021

@author: Mukul
"""

#pip install tensorflow==2.2
import pandas as pd
import numpy as np
import os
os.chdir("C:/Users/Mukul/Documents")
df=pd.read_csv("bank-full.csv",sep=';')
df['y']=np.where(df.y=='no',0,1)
df=pd.get_dummies(df)
#get all independent variables as array
x=df.drop(['y'],axis=1).values
#get dependent variable as array
y=df['y'].values
#divide the data into training and testset
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.20)
#Scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
xtrain=sc.fit_transform(xtrain)
xtest=sc.fit_transform(xtest)

import keras
from keras.models import Sequential
from keras.layers import Dense

classifier=Sequential()
classifier.add(Dense(9,kernel_initializer='uniform',activation='relu',input_dim=51))
classifier.add(Dense(1,kernel_initializer='uniform',activation='sigmoid'))
classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
classifier.fit(xtrain,ytrain,batch_size=10,epochs=50)

#apply deep learning model into testset
ypred=classifier.predict(xtest)
ypred_binary=np.where(ypred>0.50,1,0)
from sklearn.metrics import classification_report
validation=classification_report(ytest,ypred_binary)
