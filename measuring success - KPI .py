#!/usr/bin/env python
# coding: utf-8

# In[17]:


#CAGR


# In[18]:


import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as pdr 


# In[19]:


Stock = yf.download('SPY', start="2017-01-01", end="2020-04-21")


# In[20]:


def CAGR(DF):
    df = DF.copy()
    df['daily_return'] = DF['Adj Close'].pct_change()
    df['cum_return'] = (1 + df['daily_return']).cumprod()
    n = len(df)/252
    CAGR = ((df['cum_return'][-1])**(1/n) -1)
    return CAGR 


# In[21]:


CAGR(Stock)


# In[22]:


#Annualized volatility - daily(252), weekly(52), monthly(12)


# In[23]:


def volatility(DF):
    df = DF.copy()
    df['daily_return'] = DF['Adj Close'].pct_change()
    vol = (df['daily_return'].std() * np.sqrt(252)) 
    return vol 


# In[24]:


volatility(Stock)


# In[25]:


#Sharpe ratio 


# In[26]:


rf = 0.0065
def sharpe(DF, rf):
    df = DF.copy()
    sr = (CAGR(df) -rf)/ volatility(df)
    return sr


# In[27]:


sharpe(Stock, rf)


# In[28]:


#maximum drawdown 
#Calmar ratio is the ratio of CAGR and Max drawdown and it is a measure of risk adjusted return
#Calmar ratio = CAGR / Max drawdown 


# In[29]:


def max_dd(DF):
    df = DF.copy()
    df['daily_return'] = DF['Adj Close'].pct_change()
    df['cum_return'] = (1 + df['daily_return']).cumprod()
    df['cum_roll_max'] = df['cum_return'].cummax()
    df['drawdown'] = df['cum_roll_max'] - df['cum_return']
    df['drawdown_pct'] = df['drawdown']/df['cum_roll_max']
    max_dd = df['drawdown_pct'].max()
    return max_dd


# In[30]:


max_dd(Stock)


# In[31]:


def calmar(DF):
    df = DF.copy()
    clmr = CAGR(df)/max_dd(df)
    return clmr 


# In[32]:


calmar(Stock)

