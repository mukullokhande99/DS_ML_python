# -*- coding: utf-8 -*-
"""
Created on Tue May  4 22:02:25 2021

@author: Mukul
"""
import os
os.chdir("C:/Users/Mukul/Documents")
import pandas as pd
import numpy as np
com_data=pd.read_csv("Computer_Data.csv")
data1=com_data[["price","speed","hd"]].apply(lambda x:x/5)

#lambda function
#get %s of missing values in each column
percent_miss = com_data.isnull().sum() * 100 / len(com_data)
missing_value_df = pd.DataFrame({'column_name': com_data.columns,
                                 'percent_miss': percent_miss})
#method2
data2 = com_data.apply(lambda x: (x.isnull().sum() * 100 / len(x)))

#all values between 0-1
#the contribution of the value in column shouldn't change
data3=com_data["price"]/com_data['price'].sum()
#data3=com_data.price/com_data.price.sum()
data4 = com_data[["price","speed","hd"]].apply(lambda x: x / x.sum() )

#comparing value >th and convert in 1/0
data5=com_data[["price","speed","hd"]].apply(lambda x:np.where(x>200,1,0))
