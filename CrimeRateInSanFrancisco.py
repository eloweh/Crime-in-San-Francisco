#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import folium


# In[27]:


sfpd = pd.read_csv('https://cocl.us/sanfran_crime_dataset', index_col=0)


# In[28]:


# group by neighborhood
sfpd = sfpd.groupby('PdDistrict').count()
sfpd = pd.DataFrame(sfpd,columns=['Category'])  # remove unneeded columns
sfpd.reset_index(inplace=True)   # default index, otherwise groupby column becomes index
sfpd.rename(columns={'PdDistrict':'Neighborhood','Category':'Count'}, inplace=True)
sfpd.sort_values(by='Neighborhood', inplace=True)
#print(sf)


# In[29]:


sfpd.head(10)


# In[30]:


# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42
sf_neighborhood_geo = 'https://cocl.us/sanfran_geojson'


# In[31]:


# Create map
sf_map = folium.Map(
       location=[latitude,longitude],
       zoom_start=12)

sf_map


# In[32]:


# Use json file  TEST based on class
sf_map.choropleth(
       geo_data=sf_neighborhood_geo,
       data=sf,
       columns=['Neighborhood','Count'],
       key_on='feature.properties.DISTRICT',
       fill_color='YlOrRd',
       fill_opacity='0.7',
       line_opacity='0.2',
       legend_name='Crime Rate in San Francisco, by Neighborhood')

# display the map
sf_map


# In[ ]:




