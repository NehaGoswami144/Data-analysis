#!/usr/bin/env python
# coding: utf-8

# ### Missing Values and Deleting Data points
# 
# 
# 
# ### Step 1. Import the necessary libraries numpy, pandas etc

# In[34]:


import pandas as pd
import numpy as np


# ### Step 2. Import the dataset *wine.txt* from this [address](https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data) or from the folder

# In[18]:


wine = pd.read_table("https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data",sep=",",header=None)


# ### Step 3. Assign it to a variable called wine
# 
# Please note that the original data text file doesn't contain any header. Please ensure that when you import the data, you should use a suitable argument so as to avoid data getting imported as header.

# In[19]:


wine.head()


# ### Step 4. Delete the first, fourth, seventh, nineth, eleventh, thirteenth and fourteenth columns

# In[20]:


wine.drop([1,4,9,7,11,13],inplace=True,axis=1)


# In[21]:


wine


# ### Step 5. Assign the columns as below:
# 
# The attributes are (dontated by Riccardo Leardi, riclea '@' anchem.unige.it):  
# 1) alcohol  
# 2) malic_acid  
# 3) alcalinity_of_ash  
# 4) magnesium  
# 5) flavanoids  
# 6) proanthocyanins  
# 7) hue 

# In[27]:


wine.rename({2:"Alcohol",3:"malic_acid",5:"alcalinity_of_ash",6:"magnesium",8:"flavanoids",10:"proanthocyanins",12:"hue"},axis=1,inplace=True)


# ### Step 6. Set the values of the first 3 values from alcohol column as NaN

# In[68]:


wine.iloc(["Alcohol"][:3])=np.nan


# ### Step 7. Now set the value of the rows 3 and 4 of magnesium as NaN

# In[65]:


wine["magnesium"][3:5]=np.nan


# ### Step 8. Fill the value of NaN with the number 10 in alcohol and 100 in magnesium

# In[84]:


#wine["Alcohol"].fillna(value=wine["Alcohol"][10],inplace=True)
wine.fillna({"Alcohol":wine["Alcohol"][10],"magnesium":wine["magnesium"][100]},inplace=True)


# ### Step 9. Count the number of missing values in all columns.

# In[85]:


wine.isna().sum()


# ### Step 10.  Create an array of 10 random numbers up until 10 and save it.

# In[91]:


np.random.randint(1,10,10)


# ### Step 11.  Set the rows corresponding to the random numbers to NaN in the column *alcohol*

# In[ ]:





# ### Step 12.  How many missing values do we have now?

# In[ ]:


wine.isna().sum()


# ### Step 14. Print only the non-null values in alcohol

# In[ ]:


np.where(wine.isna()==False)


# ### Step 13. Delete the rows that contain missing values

# In[ ]:


wine.dropna(axis=0,inplace=True)


# ### Step 15.  Reset the index, so it starts with 0 again

# In[ ]:


wine.reset_index()

