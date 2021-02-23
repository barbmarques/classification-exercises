#!/usr/bin/env python
# coding: utf-8

# **1. Make a function named ```get_titanic_data``` that returns the titanic data from the codeup data science database as a pandas data frame. Obtain your data from the *Codeup Data Science Database*.**

# In[6]:


import pandas as pd

from env import host, password, user 

def get_connection(db, user=user, host=host, password=password):
    '''
    This function uses my info from my env file to
    create a connection url to access the Codeup db.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_titanic_data():
    '''
    This function reads in the titanic data from the Codeup db
    and returns a pandas DataFrame with all columns.
    '''
    sql_query = 'SELECT * FROM passengers'
    return pd.read_sql(sql_query, get_connection('titanic_db'))
    
get_titanic_data()


# **2. Make a function named ```get_iris_data``` that returns the data from the ```iris_db``` on the codeup data science database as a pandas data frame. The returned data frame should include the actual name of the species in addition to the ```species_ids```. Obtain your data from the *Codeup Data Science Database*.**

# In[15]:


def get_iris_data():
    '''
    This function reads in the iris data from the Codeup db
    and returns a pandas DataFrame with all columns.
    '''
    sql_query = 'SELECT * FROM species JOIN measurements ON species.species_id = measurements.species_id;'
    return pd.read_sql(sql_query, get_connection('iris_db'))

get_iris_data()
    


# **3. Once you've got your ```get_titanic_data``` and ```get_iris_data``` functions written, now it's time to add caching to them. To do this, edit the beginning of the function to check for a local filename like ```titanic.csv``` or ```iris.csv```. If they exist, use the .csv file. If the file doesn't exist, then produce the SQL and pandas necessary to create a dataframe, then write the dataframe to a .csv file with the appropriate name.**
# 
# **Be sure to add ```titanic.csv``` and ```iris.csv``` to your .gitignore file.**

# In[ ]:





# In[ ]:




