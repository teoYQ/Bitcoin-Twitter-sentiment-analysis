#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv("6.0.csv")
df.head(10)


# In[10]:


for tweet in df.text:
    print(tweet)


# In[8]:


text = " ".join(str(tweet) for tweet in df.text)
print ("There are {} words in the combination of all review.".format(len(text)))


# In[24]:


stopwords = set(STOPWORDS)
stopwords.update(["free", "bitcoin", "index", "price", "today","btc","tiempo","es","el","en","la","precio","rbitcoin","official","RT","pago","via","comment","su","de","del","all"])

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

# Display the generated image:
# the matplotlib way:


# In[25]:


plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

plt.savefig("wordcloud.png")
plt.show()


# In[26]:


df2 = pd.read_csv("../june/tweet.csv")
text = " ".join(str(tweet) for tweet in df.text)
print ("There are {} words in the combination of all review.".format(len(text)))


# In[27]:


stopwords = set(STOPWORDS)
stopwords.update(["free", "bitcoin", "index", "price", "today","btc","tiempo","es","el","en","la","precio","rbitcoin","official","RT","pago","via","comment","su","de","del","all"])

# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)

# Display the generated image:
# the matplotlib way:


# In[28]:


plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

plt.savefig("dirty.png")
plt.show()

