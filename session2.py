# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 22:01:47 2021

@author: Mukul
"""

import os
os.getcwd()

#to change working dir
os.chdir("C:/Users/Mukul/Documents")

#read csv file
import pandas as pd
com_data=pd.read_csv("Computer_Data.csv")

#loc and iloc- extract row and column
##extract column by position-iloc
#extracting first 2 rows
com_data.iloc[:2]
#extracting first 2 columns
com_data.iloc[:,:2]
#extract column by column name-loc
data1=com_data.loc[:,["price","speed"]]
#to get column names
com_data.columns
#filter data with given condition
#get rows where price>4500
#filter subset functions in R
#query in python
data2=com_data.query("price>4500")
#get rows where price>4500 and cd=no
data3=com_data.query("price>4500 & cd=='no'")

#check missing values
com_data.isnull().any()
#get count
com_data.isnull().sum()
#remove column price and hd
data4= com_data.drop(["price","hd"],axis=1)

#to create dummy var
dummy_data= pd.get_dummies(com_data)

#add new column
com_data["newcol"]=com_data.price/com_data.speed
#add new column at 3rd position
com_data.insert(3,"newcol2",com_data.price/com_data.speed)

#to get datatypes
com_data.dtypes
com_data.price.dtype
#visualization/lambda function
#seaborn,matplot