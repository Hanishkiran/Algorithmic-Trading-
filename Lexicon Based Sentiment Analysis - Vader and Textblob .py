#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Words are labelled positive or negative from negative 1 to positive 1 
# lexicon is something like a dictonary 
# Inability to process acronyms, emoticons.  Unable to account for sentiment intensity or sacarsm 

# VADER incorporated popular slangs 
# Wider spectrum from -4 to 4 
# Vader performs very well on social media 


# In[1]:


get_ipython().system('pip install vaderSentiment')


# In[2]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()


# In[3]:


analyser.polarity_scores("This is a good course")


# In[4]:


analyser.polarity_scores("The movie SUX") #Slangs


# In[5]:


analyser.polarity_scores("His antics had me ROFL")


# In[ ]:


################################Textblob Demo##################################


# In[6]:


get_ipython().system('pip install textblob')


# In[7]:


from textblob import TextBlob


# In[8]:


TextBlob("His").sentiment


# In[9]:


TextBlob("remarkable").sentiment


# In[10]:


TextBlob("impressed").sentiment


# In[11]:


TextBlob("His remarkable work ethic impressed me").sentiment

