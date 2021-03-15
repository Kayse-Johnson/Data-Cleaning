#%%
import pandas as pd
df = pd.read_csv("flights.txt",delimiter='|')
#%%

df['CANCELLED'].replace(
    to_replace=['0','False','F','T','True','1'],
    value=[False, False, False, True, True, True],
    inplace=True
)
#%%
#print(df['CANCELLED'])


print(set(df['CANCELLED']))
# %%
