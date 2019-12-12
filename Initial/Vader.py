#!/usr/bin/env python
# coding: utf-8

# In[11]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import numpy as np


# In[12]:


df = pd.read_csv("8.0.csv")
df["sentiment"] = np.zeros(df["text"].shape[0])
df.head(10)
print(df.shape)
df.dropna(inplace = True)
print(df.shape)
df.reset_index(drop=True,inplace=True)


# In[ ]:


sid = SentimentIntensityAnalyzer()
for i in range(df.shape[0]):
    text = df["text"][i]
    print(i)
    print(text)
    score = sid.polarity_scores(text)
    print(score["compound"])
    df["sentiment"][i] = score["compound"]
    
    


# In[ ]:



month = df["month"][2]
print(month)
df.to_csv("sentiment/{}sent.csv".format(month))


# In[ ]:


print(df.head(100))
june_grp = df.groupby("date2").sum()
print(june_grp)

