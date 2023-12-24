#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install cartopy


# In[6]:


import matplotlib


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


# In[4]:


#plot setup
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (14, 10)


# In[22]:


# reading a csv file
data = pd.read_csv('1.0_week.csv')
data


# In[6]:


# converting time coulumn to the standard form
data['time'] = pd.to_datetime(data['time'])
data.head()


# In[27]:


# getting a data from a csv file for processing
mask = ((data['time'] >= '2023-11-01') & (data['time'] < '2023-11-05'))
df = data.loc[mask]


# In[28]:


# show data 
# print(df)


# In[29]:


#minimum mg earht
print(df[df.mag == df.mag.min()])


# In[30]:


# max mag earth qua
print(df[df.mag == df.mag.max()])


# In[31]:


#getting latitude,longitude and magnitude
lats = list(df['latitude'])
lons = list(df['longitude'])
mag = list(df['mag'])


# In[ ]:





# In[32]:


#plotting data 
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines(resolution='50m')  # Corrected 'resolution' typo
ax.stock_img()
for i in range(len(mag)):
    plt.scatter(lons[i],lats[i])
# Show the plot
plt.show()


# In[ ]:




