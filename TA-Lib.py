#!/usr/bin/env python
# coding: utf-8

# In[12]:


import talib
import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt


# In[13]:


data = yf.download('DIS', start="2017-04-01", end="2020-05-16")


# In[14]:


data.tail(5)


# In[15]:


close = data['Close'].values
close


# In[16]:


from talib import RSI, BBANDS


# In[17]:


rsi = RSI(close, timeperiod=14)


# In[18]:


print("RSI (first 10 elements)\n", rsi[14:24])

