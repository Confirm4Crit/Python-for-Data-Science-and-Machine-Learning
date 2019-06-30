import os
try:
    os.chdir(os.path.join(os.getcwd(), 'pandas-examples'))
    print(os.getcwd())
except:
    pass
#%%
import numpy as np
import pandas as pd

#%% [markdown]
# ### Creating a Series
#
# You can convert a list,numpy array, or dictionary to a Series:

#%%
labels = ['a', 'b', 'c']
my_list = [10, 20, 30]
arr = np.array([10, 20, 30])
myDict = {'a': 10, 'b': 20, 'c': 30}

#%% [markdown]
# ** Using Lists**

#%%
pd.Series(data=my_list)


#%%
pd.Series(data=my_list, index=labels)


#%%
pd.Series(my_list, labels)

#%% [markdown]
# ** NumPy Arrays **

#%%
pd.Series(arr)


#%%
pd.Series(arr, labels)

#%% [markdown]
# ** Dictionary**

#%%
pd.Series(myDict)

#%% [markdown]
# ### Data in a Series
#
# A pandas Series can hold a variety of object types:

#%%
pd.Series(data=labels)


#%%
# Even functions (although unlikely that you will use this)
pd.Series([sum, print, len])

#%% [markdown]
# ## Using an Index
#
# The key to using a Series is understanding its index. Pandas makes use of
# these index names or numbers by allowing for fast look ups of information
# (works like a hash table or dictionary).
#
# Let's see some examples of how to grab information from a Series.
# Let us create two sereis, ser1 and ser2:

#%%
ser1 = pd.Series([1, 2, 3, 4], index=['USA', 'Germany', 'USSR', 'Japan'])


#%%
ser1


#%%
ser2 = pd.Series([1, 2, 5, 4], index=['USA', 'Germany', 'Italy', 'Japan'])


#%%
ser2


#%%
ser1['USA']

#%% [markdown]
# Operations are then also done based off of index:

#%%
ser1 + ser2

#%% [markdown]
# Let's stop here for now and move on to DataFrames, which will expand on the
# concept of Series!
# # Great Job!
