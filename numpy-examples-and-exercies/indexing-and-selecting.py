# Indexing and Selecting
#%%
import numpy as np
#%%
arr = np.arange(0, 11)
#%%
arr[8]
#%%
arr[1:5]
#%%
arr[0:]
#%%
arr[0:5] = 100
arr
#%%
sliceOfArr = arr[0:6]
#%%
sliceOfArr[:] = 99
sliceOfArr
#%%
# It's not a copy
arr
#%%
arrCopy = arr.copy()
#%%
arr
#%%
arrCopy
#%%
arrCopy[:] = 3
#%%
arr
#%%
arrCopy
#%%
arr2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
arr2d
#%%
arr2d[0][0]
#%%
arr2d[0, 0]
#%%
arr2d[:2]
#%%
arr2d[:2, 1:]

#%%
arr = np.arange(1, 11)
boolArr = arr > 5
arr[boolArr]

#%%
arr[arr > 5]
