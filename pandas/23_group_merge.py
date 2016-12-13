import numpy as np
import pandas as pd

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


print '------------------gropu by'
uefa_df = pd.read_csv('./euro_winners.csv')
print uefa_df.head()

nations_grp = uefa_df.groupby('nation')
print nations_grp.groups, len(nations_grp.groups)

nation_wins = nations_grp.size()
nation_wins.sort_values(inplace=True)

print nation_wins



print '------------------------- Pivots and reshaping data'

plant_growth_raw_df=pd.read_csv('./PlantGrowth.csv')

print plant_growth_raw_df

print plant_growth_raw_df[plant_growth_raw_df['group']=='ctrl']

print 'pivot'
print plant_growth_raw_df.pivot(index='observation', columns='group', values='weight')



print 'Stack'