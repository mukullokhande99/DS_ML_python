# -*- coding: utf-8 -*-
"""
Created on Wed May 26 21:03:05 2021

@author: Mukul
"""

#load data
import pandas as pd
reviews=pd.read_csv("customer_reviews.csv")
reviews.iloc[0]["text"]

import nltk #pip install nltk
nltk.download("vader_lexicon")

#call sentiment intensity analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sent_analysis= SentimentIntensityAnalyzer()
sent_analysis.polarity_scores(reviews.iloc[0]["text"])
#use lambda func
reviews["polarity_Score"]=reviews["text"].apply(lambda x:sent_analysis.polarity_scores(x))
#neg: neu: pos: comp:
reviews["Comp_score"]= reviews["polarity_score"].apply(lambda x:x["compound"])
#classify feedbacks
import numpy as np
reviews["Neg_Pos"]= reviews["Comp_score"].apply(lambda x: np.where(x>0.10,"Positive","Negative"))

#extract all negative feedbacks
#make wordcloud

#recogn name entity recognition 
