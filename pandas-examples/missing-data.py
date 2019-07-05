#%%
import numpy as np
import pandas as pd

#%%
d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}
df = pd.DataFrame(d)
df

#%%
# Drops any with null/nan vals
df.dropna()


#%%
# Specify Axis
df.dropna(axis=1)

#%%
# Specify Threshold
df.dropna(thresh=2)


#%%
# Fill NA Vals
df.fillna(value='LOL')


#%%
# Fill NAs with Mean of A
df['A'].fillna(value=df['A'].mean())
