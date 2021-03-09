#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd


# In[2]:


st.write('My line of code in streamlit')


# In[4]:


df = pd.read_csv("Corona_Updated.csv")


# In[8]:


df.Temprature.plot()


# In[9]:


st.line_chart(df.Temprature)


# In[ ]:




