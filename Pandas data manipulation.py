#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning

# In[1]:


import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv("C:/Users/HP/Downloads/Admission_Prediction.csv")


# In[3]:


df


# In[4]:


df.isna().sum()


# In[5]:


df.info()


# In[6]:


df.describe().T


# In[7]:



for i in df.columns :
    if df[i].isna().sum()>0:
        df[i].fillna(df[i].median(),inplace=True)


# In[8]:


df.info()


# In[9]:


df.groupby(["Chance of Admit"]>=0.95)["CGPA"]>0.95


# In[ ]:


df.set_index(["Chance of Admit"],inplace=True)


# In[ ]:


df


# In[10]:


(df["Chance of Admit"]>=0.95).sum()  


# In[11]:


#as it is named
df.iloc[1:20]


# In[12]:


df.iloc[12:14,1:3]


# In[13]:


df.isna().sum()


# # Data Analysis

# In[14]:


df.columns


# In[15]:


df["University Rating"].value_counts()


# In[16]:


df.Research.unique()


# In[17]:


df["Research"].value_counts()


# In[18]:


#this is giving indexes where Research is equal to 1

np.where(df["Research"]==1)


# In[19]:


df.info()


# In[20]:


df.describe().T


# In[21]:


df.set_index(["Serial No."],inplace=True)


# In[22]:


df


# In[23]:


df.groupby("Research")["CGPA"].value_counts()


# In[24]:


df.groupby(["Research","Chance of Admit"])["CGPA"].value_counts()


# insights:
# 
#  . students having CGPA>9.87 haves the greater chance of admition 
#  
#  . studnets having CGPA>9.87 had the most REsearch

# In[25]:


df.loc[df["Chance of Admit"]>=0.98]


# In[26]:


df["GRE Score"].mode()


# In[27]:


df["TOEFL Score"].max()


# In[28]:


df.groupby(["Chance of Admit","Research"])["GRE Score","TOEFL Score"].value_counts()


# In[29]:


df.loc[df["Research"]==1]


# In[37]:


df.iloc[np.where(df["Chance of Admit"]==max(df["Chance of Admit"]))]


# In[52]:


df.iloc[np.where(df["CGPA"]==max(df["CGPA"])) and  np.where(df["Chance of Admit"]<max(df["Chance of Admit"]))]


# In[11]:


df["CGPA"].max()


# In[12]:


c=df["CGPA"]=df['CGPA'].replace(9.92,"max")


# In[29]:


df["CGPA"]


# In[3]:


df[142:144]


# In[10]:





# In[ ]:




