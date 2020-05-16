#!/usr/bin/env python
# coding: utf-8

# In[24]:


import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt


# In[25]:


#MACD is a lagging indicator 
data = yf.download('AAPL', start="2010-04-01", end="2020-05-16")
data.describe()


# In[26]:


data.tail()


# In[27]:


plt.style.use('ggplot')
#the type of plot is ggplot


# In[28]:


#to calculate expomemtial moving average 
data['12d_EMA'] = data.Close.ewm(span=12).mean()
data['26d_EMA'] = data.Close.ewm(span=26).mean()
data[['Close','12d_EMA','26d_EMA']].plot(figsize=(10,5))
plt.show()


# In[29]:


#calculating MACD 
data['MACD'] = data['26d_EMA'] - data['12d_EMA']

#calculating signal 
data['Signal'] = data.MACD.ewm(span=9).mean()

data[['MACD', 'Signal']].plot(figsize=(10,5))


# In[30]:


#creating a trading signal 
data['trading_signal'] = np.where(data['MACD'] > data['Signal'], 1, -1)
data['trading_signal'].tail(40)


# In[31]:


#backtesting
# Calculate Returns
data['returns'] = data.Close.pct_change()

# Calculate Strategy Returns
# assuming that the long or short decision will be taken the next day 
data['strategy_returns'] = data.returns * data.trading_signal.shift(1)

# Calculate Cumulative Returns
cumulative_returns = (data.strategy_returns + 1).cumprod()-1

# Plot Strategy Returns
cumulative_returns.plot(figsize=(10,5))
#data.strategy_returns.plot(figsize=(10,5))
plt.legend()
plt.show()


# In[32]:


# Total number of trading days in a year is 252
trading_days = 252

# Calculate CAGR by multiplying the average daily returns with number of trading days
annual_returns = ((1 + data.returns.mean())**(trading_days) - 1)*100

'The CAGR is %.2f%%' % annual_returns


# In[33]:


# Calculate the annualised volatility
annual_volatility = data.returns.std() * np.sqrt(trading_days) * 100
'The annualised volatility is %.2f%%' % annual_volatility


# In[34]:


#Calculatign the sharpe ratio
#Sharpe ratio = [r(x) - r(f)] / δ(x)
#annualized return of investment minus the risk free rate divided by standard deviation

