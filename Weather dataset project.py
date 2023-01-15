#!/usr/bin/env python
# coding: utf-8

# # Working on real Projects on Python
# 
# (A Part of big data analysis)
# 

# The Weather Datase
# 
# Here , the weather dataset is a time series dataset with per hour information about weather condition at particular location it records , Dew points Temperature , relative humidity , wind speed visibility and conditions

# In[42]:


import pandas as pd


# In[43]:


data = pd.read_csv(r'C:\Users\lenovo\Downloads\1. Weather Data.csv')


# In[44]:


data


# # ANALYSING DATA FRAMES
# For first n rows (where n = 5)

# In[45]:


data.head()

 1.For total number of Rows and columns of the dataframe

# In[46]:


data.shape


# 2.For indexs 

# In[48]:


data.index


# 3.For the name of each column

# In[50]:


data.columns


# In[ ]:


4.For the data types of each column


# In[51]:


data.dtypes


# 5.For showing the unique value in a single particular column

# In[53]:


data['Weather'].unique()


# 6.For showing unique value in each column as well as on whole data fram

# In[54]:


data.nunique()


# 7.For showing not null value in each column 
# 

# In[55]:


data.count()


# 8 .For showing unique value with their count

# In[59]:


data['Weather'].value_counts()


# In[60]:


data.info()


# Ques 1 - Find all the unique "wind speed" value in the data 

# In[61]:


data.head(2)


# In[62]:


data.nunique()


# In[75]:


data['Wind Speed_km/h'].nunique()


# In[76]:


data['Wind Speed_km/h'].unique()


# Ques 2 - Find the number of times when "the weather is exactly clear"

# In[78]:


data.head(2)


# In[81]:


data.Weather.value_counts()


# In[87]:


data.head(2)


# In[97]:


data.groupby('Weather').get_group('Clear')


# In[ ]:


ques 3 - find out all the null value in the data


# In[124]:


data.isnull().sum()


# Ques 4 - Rename the column form 'weather' of the dataframe to 'weather conditios'

# In[126]:


data.rename(columns = {'Weather': 'Weather conditions'})


# Ques 6- what is the mean visibility
# 

# In[128]:


data.Visibility_km.mean()


# Ques 8 - what is the standared daviation 'Pressure' on data

# In[130]:


data.Press_kPa.std()


# Ques 9 - what is the varieance of 'Relative humidity' in this data

# In[131]:


data['Rel Hum_%'].var()


# Ques  10 - What is the minimum and maximum value for each column against each 'weather conditions'

# In[188]:


data.groupby('Weather').min()


# In[189]:


data.groupby('Weather').max()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




