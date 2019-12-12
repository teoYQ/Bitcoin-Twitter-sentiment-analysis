#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


data = pd.read_csv("regression_data.csv")
data.head(10)
data["one"] = np.ones((data.shape[0],1))
print(data.shape)
print(data["one"])
#feature = pd.concat(data["sent"],data["one"],join="inner")
#print(feature)


# In[3]:


b=data["sent"].values
xbar = b.reshape(-1,1)
x_train, x_test, y_train, y_test = train_test_split(xbar, data["up"], test_size=0.25, random_state=0)


# In[4]:


print(x_train.shape)


# In[5]:


from sklearn.linear_model import LogisticRegression
logisticRegr = LogisticRegression()
logisticRegr.fit(x_train, y_train)


# In[6]:


from sklearn import metrics
predictions = logisticRegr.predict(x_test)
score = logisticRegr.score(x_test, y_test)
print(score)
cm = metrics.confusion_matrix(y_test, predictions)
print(cm)


# In[10]:


plt.scatter(b,data["up"])
plt.title("Sentiment against Price change")
plt.xlabel("Sentiment")
plt.ylabel("Price direction")
plt.savefig("data_modeling,png")


# In[21]:


#fig,ax = subplot()

fig, ax1 = plt.subplots()


x = ["Jan","Feb","March","April", "May","June","July"]
y = [11894,20232,20895,18423,33155,27122,27281]
price = [934,1074,1168,1228,1959,2709,2603]
transac = [71359,46871,86527,52062,111173,111626,121071]
color = 'tab:red'
ax1.set_xlabel('months')
ax1.set_ylabel('Highest Tweet Volume in a day', color=color)
ax1.plot(x, y, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:blue'
ax2.set_ylabel('price',color=color)  # we already handled the x-label with ax1
ax2.plot(x, price, color=color)
ax2.tick_params(axis='y',direction="in", labelcolor=color)

plt.savefig("volume.png")
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()


# In[24]:


fig2, ax11 = plt.subplots()
color = 'tab:red'
ax11.set_xlabel('months')
ax11.set_ylabel('Highest Tweet Volume in a day', color=color)
ax11.plot(x, y, color=color)
ax11.tick_params(axis='y', labelcolor=color)

ax3 = ax11.twinx()
color = 'tab:green'
ax3.set_ylabel("transactional volume",color=color)
ax3.plot(x,transac,color=color)
ax3.tick_params(axis="y",direction="out",labelcolor=color)

plt.savefig("trans.png")

