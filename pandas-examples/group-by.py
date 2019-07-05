# %%
import pandas as pd

# %%
data = {'Company': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
        'Person': ['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah'],
        'Sales': [200, 120, 340, 124, 243, 350]}

# %%
df = pd.DataFrame(data)

# %%
df

# %%
byComp = df.groupby('Company')
# %%
byComp

# %%
byComp.mean()

# %%
byComp.sum()

# %%
byComp.std()

# %%
byComp.sum().loc['FB']

# %%
df.groupby('Company').sum().loc['FB']

# %%
df.groupby('Company').count()

# %%
df.groupby('Sales').max()

# %%
df.groupby('Sales').min()

# %%
byComp.describe()
# %%
byComp.describe().transpose()
# %%
byComp.describe().transpose()['GOOG']
