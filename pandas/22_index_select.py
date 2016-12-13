import numpy as np
import pandas as pd
import scipy.constants as phys
import math





#### Basic Indexing

spot_crude_prices_2013_data={
    'U.K. Brent':
        {'2013-Q1':112.9, '2013-Q2':103.0, '2013-Q3':110.1, '2013-Q4':109.4},
    'Dubai':
        {'2013-Q1':108.1, '2013-Q2':100.8,'2013-Q3':106.1,'2013-Q4':106.7},
    'West Texas Intermediate':
        {'2013-Q1':94.4, '2013-Q2':94.2, '2013-Q3':105.8,'2013-Q4':97.4}}


print spot_crude_prices_2013_data


spot_crude_prices_2013_df = pd.DataFrame.from_dict(spot_crude_prices_2013_data)

print spot_crude_prices_2013_df

print '-----dubai prices'

dubai_prices = spot_crude_prices_2013_df['Dubai']
print dubai_prices

print '--- column select'

print spot_crude_prices_2013_df[['West Texas Intermediate', 'U.K. Brent']]

try:
    spot_crude_prices_2013_df['Brent Blend']
except KeyError as e:
    print  "'{}' column does not exist".format(e.message)


print 'Brent Blend again:', spot_crude_prices_2013_df.get('Brent Blend', 'N/A')

print '------ dot operator '

print spot_crude_prices_2013_df.Dubai # <=== VALID PYTHON IDENTIFIER


print 'renaming columns '
spot_crude_prices_2013_df.columns=['Dubai', 'UK_Brent', 'West_Texas_Intermediate']
print spot_crude_prices_2013_df
print spot_crude_prices_2013_df.West_Texas_Intermediate

print 'column index'
print spot_crude_prices_2013_df[[1,2]]


print '-------- Range Slicing'

print spot_crude_prices_2013_df[:2] # first 2 rows
print spot_crude_prices_2013_df[2:] # from row 2
print spot_crude_prices_2013_df[::2] # intervals of 2 from 0
print spot_crude_prices_2013_df[::-1] # reverse rows


dubai_prices = spot_crude_prices_2013_df['Dubai']
print dubai_prices[1:] # last 3 rows
print dubai_prices[:-1] # all rows but the last
print dubai_prices[::-1] # reverse rows



print "======= Label, integer and mixed indexing"

print '------ Label indexing'


nyc_snow_avgs_data={'Months' : ['January','February','March', 'April', 'November', 'December'],
                    'Avg SnowDays' : [4.0,2.7,1.7,0.2,0.2,2.3],
                    'Avg Precip. (cm)' : [17.8,22.4,9.1,1.5,0.8,12.2],
                    'Avg Low Temp. (F)' : [27,29,35,45,42,32] }

nyc_snow_avgs_data_df = pd.DataFrame(nyc_snow_avgs_data,
                                        index=nyc_snow_avgs_data['Months'],
                                        columns=['Avg SnowDays', 'Avg Precip. (cm)','Avg Low Temp. (F)'])


print nyc_snow_avgs_data_df


print nyc_snow_avgs_data_df.loc['January']
print nyc_snow_avgs_data_df.loc['January']['Avg SnowDays']
print nyc_snow_avgs_data_df.loc['January':'March']
print nyc_snow_avgs_data_df.loc['January':'March']['Avg SnowDays']



#Note that while using the .loc , .iloc , and .ix operators on a DataFrame, the row
#index must always be specified first. This is the opposite of the [] operator, where
#only columns can be selected directly. Hence, we get an error if we do the following
print nyc_snow_avgs_data_df.loc[:,'Avg SnowDays']


# that the [] operator cannot be used to select rows directly. The columns
# must be selected first to obtain a Series




print '------ Selection using a boolean array'

print nyc_snow_avgs_data_df.loc[nyc_snow_avgs_data_df['Avg SnowDays']<1,:]

print '------'
print nyc_snow_avgs_data_df.loc['January']>20
print nyc_snow_avgs_data_df.loc[:, nyc_snow_avgs_data_df.loc['January']>20]


print '------ Integer-oriented indexing'

sci_values=pd.DataFrame([[math.pi, math.sin(math.pi), math.cos(math.pi)],
                    [math.e, math.log(math.e), phys.golden],
                    [phys.c, phys.g, phys.e],
                    [phys.m_e, phys.m_p, phys.m_n]],
                    index=list(range(0,20,5)))
print sci_values

print '# first two rows'
print sci_values.iloc[:2]

print '#  column two and ????'
print sci_values.iloc[2, 0:2] #a


print 'mixed indexing'

stock_index_data_df = pd.read_csv('./stock_index_prices.csv')
print stock_index_data_df


print '----- Multiindexing'


shares_index_data_df=pd.read_csv('./stock_index_prices.csv')
print shares_index_data_df


shares_index_df = shares_index_data_df.set_index(['TradingDate', 'PriceType'])

shares_index = shares_index_df.index


print shares_index
print shares_index_df

print shares_index.get_level_values(0)

print shares_index.get_level_values(1)

print shares_index_df.ix['2014/02/21':'2014/02/24']

# print shares_index_df.ix[('2014/02/21','open'):('2014/02/24','open')] # error@!

print shares_index_df.sortlevel(0).ix[('2014/02/21','open'):('2014/02/24','open')]

print shares_index_df.ix[('2014/02/21','close'),('2014/02/24','open')]


print '-------- Swapping and reordering levels'


reordered_df =  shares_index_df[:7].reorder_levels(['PriceType', 'TradingDate'], axis=0)

print reordered_df



print '----- Cross Sections '

cross_sections = shares_index_df.xs('open', level='PriceType')

print cross_sections


swapped_cross= shares_index_df.swaplevel(0, 1, axis=0).ix['open']

print swapped_cross

print '----- Boolean indexing'

bool_idx = shares_index_data_df.ix[shares_index_data_df['PriceType']=='close']

print bool_idx


high_selection = shares_index_data_df['PriceType'] == 'high'
nasdaq_high = shares_index_data_df['Nasdaq']<4300

print shares_index_data_df.ix[high_selection & nasdaq_high]



print '----- The is in and all methods'

stock_series = pd.Series(['NFLX','AMZN','GOOG','FB','TWTR'])

print stock_series.isin(['AMZN', 'FB'])


print stock_series[stock_series.isin(['AMZN', 'FB'])]

print '------ The where() method'

np.random.seed(100)
normvals = pd.Series([np.random.normal() for i in np.arange(10)])

print normvals

print normvals[normvals>0]

print normvals.where(normvals>0)

norm_df = pd.DataFrame([[round(np.random.normal(), 3) for i in np.arange(5)] for j in range(3)],
                       columns=['0', '30', '60', '90', '120'])

print norm_df

print norm_df[norm_df>0]

print norm_df.where(norm_df > 0)

print norm_df.mask(norm_df>0)


print ' ----- operations in indexes'