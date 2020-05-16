#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 4 most useful Python Libraries 
# NLTK 
# Vader 
# Scikit Learn 
# TextBlob 


# In[ ]:


# Tokenisation 
# Lemmatization - removing the inflectional forms of the words  
# Stemming - Keeping the root wood and rejecting other forms 
# Stop words - Remove connector words 
# Normallization - Cleaning data such as removing punctuation 


# In[1]:


get_ipython().system('pip install nltk')


# In[ ]:


# Tokenization


# In[5]:


text = "I am not a sentimental person but I believe in the utility of sentiment analysis"


# In[6]:


import nltk
nltk.download('punkt')


# In[7]:


# Tokenization
from nltk.tokenize import word_tokenize
tokens = word_tokenize(text)
print(tokens)


# In[13]:


nltk.download('wordnet')


# In[14]:


# Lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
tokens=[lemmatizer.lemmatize(word) for word in tokens]


# In[16]:


# Stemming
from nltk.stem import PorterStemmer
tokens=word_tokenize(text.lower())
ps = PorterStemmer()
tokens=[ps.stem(word) for word in tokens]
print(tokens)


# In[18]:


nltk.download('stopwords')


# In[20]:


# Stop words
import nltk
stopwords = nltk.corpus.stopwords.words('english')


tokens_new = [j for j in tokens if j not in stopwords]


# In[21]:


tokens_new

