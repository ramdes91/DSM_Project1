
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
df = pd.read_csv('https://raw.githubusercontent.com/jackiekazil/data-wrangling/master/data/chp3/data-text.csv')
df.head(2)


# In[2]:


df1 = pd.read_csv('https://raw.githubusercontent.com/kjam/data-wrangling-pycon/master/data/berlin_weather_oldest.csv')
df1.head(2)


# Task 1. Get the Metadata from the above files.

# In[3]:


df.info()


# In[4]:


df1.info()


# Task 2. Get the row names from the above files

# In[6]:


df.columns


# In[7]:


df1.columns


# For testing:

# In[8]:


df.head(2)


# Task 3. Change the column name from any of the above file

# In[9]:


df.rename(columns = {'Indicator':'Indicator_id'}, inplace=True)
df.head(2)


# Task 4. Change the column name from any of the above file and store the changes made permanently.

# In[10]:


df.rename(columns = {'Indicator':'Indicator_id'}, inplace=True)
df.head(2)


# For Testing:

# In[11]:


df.head(2)


# Task 5. Change the names of multiple columns.

# In[13]:


df.rename(columns = {'PUBLISH STATES':'Publication Status', 'WHO region':'WHO Region'}, inplace=True )
df.head(2)


# Task 6. Arrange values of a particular column in ascending order.

# In[15]:


df.sort_values('Year').head(5)


# Task 7. Arrange multiple column values in ascending order

# In[16]:


df.sort_values(['Indicator_id', 'Country', 'Year', 'WHO Region', 'Publication Status'], ascending=[True, True, True, True, True]).head(3)


# Test Data for Task 8

# In[17]:


df.columns


# Task 8. Make country​ as the first column of the dataframe

# In[18]:


df = df[['Country', 'Indicator_id', 'Publication Status', 'Year', 'WHO Region',
       'World Bank income group', 'Sex', 'Display Value', 'Numeric',
       'Low', 'High', 'Comments']]
df.columns


# In[19]:


df.head(2)


# Task 9. Get the column array using a variable

# In[23]:


df.values


# Task 10. Get the subset rows 11, 24, 37

# In[24]:


df.iloc[[11,24,37]]


# Task 11. Get the subset rows excluding 5, 12, 23, and 56
# 

# In[35]:


excludedRows = df.index.isin([5,12,23,34,56])
df[~excludedRows]


# Load datasets from CSV
# 

# In[37]:


users=pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/users.csv')
sessions=pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/sessions.csv')
products=pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/products.csv')
transactions=pd.read_csv('https://raw.githubusercontent.com/ben519/DataWrangling/master/Data/transactions.csv')


# In[38]:


users.head()


# In[39]:


sessions.head()


# In[40]:


products.head()


# In[41]:


transactions.head()


# Task 12: Join users to transactions, keeping all rows from transactions and only matching rows from users (left join)

# In[42]:


pd.merge
display(pd.merge(transactions,users, on="UserID", how='left'))


# Task 13: Which transactions have a UserID not in users?

# In[43]:


display(transactions[~transactions['UserID'].isin(users['UserID'])])


# Task 14. Join users to transactions, keeping only rows from transactions and users that match via UserID (inner join)

# In[46]:


display(pd.merge(transactions,users, on='UserID', how='inner'))


# Task 15. Join users to transactions, displaying all matching rows AND all non-matching rows (full outer join)

# In[47]:


display(pd.merge(transactions,users, on='UserID', how='outer'))


# Task 16. Determine which sessions occurred on the same day each user registered

# In[48]:


display(pd.merge(sessions,users, on='UserID', how='inner'))


# In[49]:


sameDayUserReg=pd.merge(sessions,users, on='UserID', how='inner')
sameDayUserReg


# In[52]:


sameDayUserReg.loc[sameDayUserReg['SessionDate'] == sameDayUserReg['Registered']]


# Task 17. Build a dataset with every possible (UserID, ProductID) pair (cross join)

# In[53]:


possibleDataSet = users.assign(value=1).merge(products.assign(value=1)).drop('value', 1)
display(possibleDataSet)


# Task 18. Determine how much quantity of each product was purchased by each user

# In[54]:


display(transactions.sort_values('Quantity'))


# Task 19. For each user, get each possible pair of pair transactions

# In[55]:


pd.merge(transactions, transactions, on='UserID')


# Task20. Join each user to his/her first occuring transaction in the transactions table

# In[56]:


data=pd.merge(users, transactions.groupby('UserID').first().reset_index(), how='left', on='UserID')
data


# Task 21. Test to see if we can drop columns

# In[58]:


columns = list(data.columns)


# In[59]:


list(data.dropna(thresh=int(data.shape[0] * .9), axis=1).columns)


# In[60]:


missingInfo = list(data.columns[data.isnull().any()])
missingInfo


# In[61]:


for col in missingInfo:
    missingNumber = data[data[col].isnull() == True].shape[0]
    print('Missing Number for Col {}: {}'.format(col, missingNumber))


# In[62]:


for col in missingInfo:
    percentMissing = data[data[col].isnull() == True].shape[0] / data.shape[0]
    print('Col Percent Missing {}: {}'.format(col, percentMissing))


# End of Project
