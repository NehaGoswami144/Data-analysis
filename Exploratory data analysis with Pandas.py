#!/usr/bin/env python
# coding: utf-8

# In[93]:


import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[94]:


f=pd.read_csv("adult.data.csv")


# In[95]:


f.info()


# In[96]:


f.head()


# 1. How many men and women (sex feature) are represented in this dataset?
# 

# In[97]:


f["sex"].value_counts()


# 2. What is the average age (age feature) of women?
# 

# In[98]:


f[f["sex"]=="Female"]["age"].mean()


# 3. What is the percentage of German citizens (native-country feature)?
# 

# In[99]:


f["native-country"].value_counts(normalize=True)


# 4. Find the maximum age of men of Amer-Indian-Eskimo race

# In[100]:


f[(f["sex"]=="Male")& (f["race"]=="Amer-Indian-Eskimo")]["age"].max()


# 5. What are the mean and standard deviation of age for those who earn more than 50K per year (salary feature)?

# In[101]:


f[f["salary"]==">50K"]["age"].std()
f[f["salary"]==">50K"]["age"].mean()


# 6. What are the mean and standard deviation of age for those who earn less than 50K per year?

# In[102]:


f[f["salary"]=="<=50K"]["age"].std()
f[f["salary"]=="<=50K"]["age"].mean()


# 7. Is it true that people who earn more than 50K have at least high school education? (education – Bachelors, Prof-school, Assoc-acdm, Assoc-voc, Masters or Doctorate feature)

# In[120]:


len(f[(f["salary"]==">50K") &(f["education-num"]>13)])/len(f[f["salary"]==">50K"])


# 8. Count the average time of work (hours-per-week) for those who earn a little and a lot (salary) for each country (native-country). What will these be for Japan?

# In[104]:


f[(f["salary"]==">50K") & (f["native-country"]=="Japan")]["hours-per-week"].mean()
f[(f["salary"]=="<=50K") & (f["native-country"]=="Japan")]["hours-per-week"].mean()


# 9. What is the maximum number of hours a person works per week (hours-per-week feature)? How many people work such a number of hours, and what is the percentage of those who earn a lot (>50K) among them

# In[105]:


max(f["hours-per-week"])


# In[106]:


len(f[f["hours-per-week"]==99])


# In[107]:


a=f[(f["hours-per-week"]==max(f["hours-per-week"])) & (f["salary"]==">50K")]["hours-per-week"].count()
a


# In[108]:


a/len(f[f["hours-per-week"]==99])


# 10. Among whom is the proportion of those who earn a lot (>50K) greater: married or single men (marital-status feature)? Consider as married those who have a marital-status starting with Married (Married-civ-spouse, Married-spouse-absent or Married-AF-spouse), the rest are considered bachelors

# In[109]:



len(f[(f["marital-status"].str.contains("Married"))& (f["salary"]==">50K")])/len(f[f["salary"]==">50K"])


# In[110]:


len(f[f["marital-status"].str.contains("Married")])


# In[111]:


len(f[f["salary"]==">50K"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




