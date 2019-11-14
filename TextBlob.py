#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd
from textblob import TextBlob
data = pd.read_csv("sent.csv")


# In[10]:


data.head(10)
data = data.drop(["date","username","retweets","favorites"],axis=1)
#data = data.drop([0],axis=1)

#data = data.drop(["text"],axis=1)
data = data.drop(["Unnamed: 0","Unnamed: 0.1"],axis=1)
data = data.drop(["month"],axis=1)


# In[11]:


import numpy as np
data["subjectivity"] = np.zeros((data.shape[0],1))
data.head(10)


# In[ ]:




sentiment = []
polarity = []
for i in range(data.shape[0]):
  # print(data['cleantext'][i])
    analysis = TextBlob(str(data['text'][i]))
    #print(analysis.sentiment)
    #temp = {'polarity':analysis.sentiment[0], 'subjectivty':analysis.sentiment[1]}
    #sentiment.append(temp)
    data["sentiment"][i] = analysis.sentiment[0]
    
    data["subjectivity"][i] = analysis.sentiment[0]
    #polarity.append(analysis.sentiment[0])
    if (i%1000==0):
        print(i)

#data['polarityTextBlob'] = pd.Series(polarity).values

#sentimenttb = data[['text', 'polarity', 'polarityTextBlob']]
data.head(20)
#print(sentiment)


# In[ ]:


import matplotlib.pyplot as plt


# In[8]:



#data = data.drop(["Unnamed: 0","Unnamed: 0.1","date","username","retweets","favorites","text","month"],axis=1)
data.head(10)
#data = pd.to_numeric(data["sentiment"],errors="coerce")
print(sentiment)


# In[ ]:


#data_group = data["sentiment"].groupby(data['date2'])
#data_group = data.groupby(data['date2']).sum()
#data_group = data.groupby(data['date2']).transform('sum')


# In[ ]:


print(data_group.shape)#grp_sent.columns = ['date','score']


# In[ ]:




