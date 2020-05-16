#!/usr/bin/env python
# coding: utf-8

# In[4]:


import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as pdr 


# In[5]:


ohlc = yf.download('AAPL', start="2010-04-01", end="2020-05-16")


# In[6]:


def BollBand(DF,n):
    df = DF.copy()
    df["MA"] = df["Adj Close"].rolling(n).mean()
    df["BB_up"] = df["MA"] + 2*df["MA"].rolling(n).std()
    df["BB_dn"] = df["MA"] - 2*df["MA"].rolling(n).std()
    df["BB_width"] = df["BB_up"] - df["BB_dn"]
    df.dropna(inplace=True)
    return df
BollBand(ohlc, 20).iloc[-100: ,[-4,-3,-2]].plot()

