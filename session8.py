# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 21:02:45 2021

@author: Mukul
"""


#pip install tensorflow
#pip install pytorch
import tensorflow as tf
#pip install keras
import keras
#pip install tensorflow-gpu
import pandas as pd
import numpy as np
import os
os.chdir("C:/Users/Mukul/Documents")
df=pd.read_csv('bank-full.csv',sep=';')
df['y']=np.where(df.y=="no",0,1)
df=pd.get_dummies(df)
#get all indep var as array
x= df.drop(['y'],axis=1).values
#get dep var as array
y=df['y'].values

#divide data in trainset and testset
from sklearn.model_selection import train_test_split
xtrain,xtest, ytrain, ytest=train_test_split(x,y,test_size=0.2)
#scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
xtrain=sc.fit_transform(xtrain)
xtest=sc.fit_transform(xtest)

from keras.models import Sequential
from keras.layers import Dense

classifier= Sequential()
classifier.add(Dense(9,kernel_initializer='uniform',activation='relu', input_dim=51))
#Dense param- layers, weights, act fun, input columns
classifier.add(Dense(1,kernel_initializer='uniform',activation='sigmoid'))
#op layer-sigmoid act
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#error minimize compile model
#compile para
classifier.fit(xtrain,ytrain,batch_size=10,epochs=50)
#fiting model

#apply DL into testset
ypred=classifier.predict(xtest)
ypred_bin= np.where(ypred>0.51,1,0)

#validation
from sklearn.metrics import classification_report
validation= classification_report(ytest, ypred_bin)
