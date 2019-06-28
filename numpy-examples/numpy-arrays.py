#%%
import numpy as np

myList = [1, 2, 3]
#%%
arr = np.array(myList)
#%%
print(arr)
myMat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
np.array(myMat)
np.arange(0, 10)
#%%
np.arange(0, 11, 2)
#%%
np.zeros((5, 5))
np.zeros((2, 3))
#%%
np.ones((3, 4))
#%%
np.linspace(0, 5, 10)
#%%
np.eye(4)
#%%
np.random.rand(5)

#%%
np.random.randn(2)
np.random.randn(4, 4)

#%%
np.random.randint(0, 10, 5)

#%%
arr = np.arange(25)
ranarr = np.random.randint(0, 50, 10)
ranarr

#%%
arr.reshape(5, 5)

#%%
ranarr
#%%
ranarr.max()
#%%
ranarr.min()

#%%
ranarr.argmax()
#%%
ranarr.argmin()

#%%
arr.shape

#%%
arr.dtype
