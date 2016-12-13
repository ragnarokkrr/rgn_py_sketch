import numpy as np
import pandas as pd


#### #DataFrame creation###



stock_summaries = {
    'AMZN': pd.Series([346.15, 0.59, 459.0, 0.52, 589.8, 158.88],
            index =['Closing Price', 'EPS', 'Shares Outstanding(M)', 'Beta', 'P/E', 'Market Cap(B)']),
    'GOOG': pd.Series([1133.43,36.05,335.83,0.87,31.44,380.64],
                      index=['Closing Price', 'EPS', 'Shares Outstanding(M)', 'Beta', 'P/E', 'Market Cap(B)']),
    'FB': pd.Series([61.48,0.59,2450,104.93,150.92],
                    index=['Closing Price', 'EPS', 'Shares Outstanding(M)', 'Beta', 'Market Cap(B)']),
    'YHOO': pd.Series([34.90,1.27,1010,27.48,0.66,35.36],
                    index=['Closing price','EPS','Shares Outstanding(M)', 'P/E','Beta', 'Market Cap(B)']),
    'TWTR':pd.Series([65.25,-0.3,555.2,36.23],
                    index=['Closing price','EPS','Shares Outstanding(M)','Market Cap(B)']),
    'AAPL':pd.Series([501.53,40.32,892.45,12.44,447.59,0.84],
                    index=['Closing price','EPS','Shares Outstanding(M)','P/E','Market Cap(B)','Beta'])
}


stock_df = pd.DataFrame(stock_summaries)

print stock_df
print 'stock_df.index', stock_df.index
print 'stock_df.columns', stock_df.columns


stock_df2 = pd.DataFrame(stock_summaries,
                         index=['Closing Price', 'EPS', 'Shares Outstanding(M)', 'P/E', 'Market Cap(B)', 'Beta'])

print stock_df2


stock_df3 = pd.DataFrame(stock_summaries,
                         index=['Closing Price', 'EPS', 'Shares Outstanding(M)', 'P/E', 'Market Cap(B)', 'Beta'],
                         columns= ['FB', 'TWTR', 'SCNW'])

print stock_df3


############ Using a dictionary of ndarrays/lists

############ Using a structured array


############ Using a structured array
member_data = np.zeros((4,), dtype = [('Name', 'a15'),
                              ('Age', 'i4'),
                              ('Weight', 'f4')])

member_data[:] = [('Sanjeev', 37, 162.24),
                  ('Yingluck', 45, 137.8),
                  ('Emeka', 28, 153.2),
                  ('Amy', 67, 101.3)]


print member_data


member_data_df = pd.DataFrame(member_data, index=['a', 'b', 'c', 'd'])
print member_data_df



########### Using a Series structure


curr_dict = {'US': 'dollar',
             'UK': 'pound',
             'Germany': 'euro',
             'Mexico': 'peso',
             'Nigeria': 'naira',
             'China': 'yuan',
             'Japan': 'yen'}


curr_series = pd.Series(curr_dict)

print curr_series

####### operations
print '=============== operations'

print member_data_df['Name']
print '---------'

member_data_df['Height']=60 # new column
print member_data_df
print '---------'

del member_data_df['Height']
print member_data_df


print ' pop '

member_data_df['BloodType']= 'O'
blood_type = member_data_df.pop('BloodType')
print 'blood_type', blood_type

print 'insert'

member_data_df.insert(2, 'isSenior', member_data_df['Age']>60)
print member_data_df


######## Alignement
print 'Alignement'
ore1_df = pd.DataFrame(np.array([[20, 35, 25, 20],
                                 [11, 28, 32, 29]]),
                        columns= ['iron', 'magnesium', 'copper', 'silver'])



ore2_df = pd.DataFrame(np.array([[14,34,26,26],
                                 [33,19,25,23]]),
                       columns=['iron', 'magnesium', 'gold', 'silver'])





print ore1_df
print ore2_df

print ore1_df + ore2_df


print ore1_df + pd.Series([25,25,25,25],
                          index=['iron', 'magnesium', 'copper', 'silver'])


##### Panel

#### 3D Numpy
print '-----3D Numpy'
stock_data= np.array([[[63.03,61.48,75],
                        [62.05,62.75,46],
                        [62.74,62.19,53]],
                        [[411.90, 404.38, 2.9],
                        [405.45, 405.91, 2.6],
                        [403.15, 404.42, 2.4]]])


print stock_data

stock_historical_prices = pd.Panel(stock_data,
                                   items=['FB', 'NFLX'],
                                   major_axis=pd.date_range('10/3/2014', periods=3),
                                    minor_axis = ['open price', 'closing price', 'volume'])

print stock_historical_prices


###### Using a Python dictionary of DataFrame objects
print '-------- dictionary '

us_data=pd.DataFrame(np.array([[249.62, 8900],
                                [282.16, 12680],
                                [309.35, 14940]]),
                                columns=['Population(M)', 'GDP($B)'],
                                index=[1990, 2000, 2010])
print us_data



china_data=pd.DataFrame(np.array([[1133.68, 390.28],
                                [ 1266.83,1198.48],
                                [1339.72, 6988.47]]),
                                columns=['Population(M)','GDP($B)'],
                                index=[1990,2000,2010])
print china_data


us_china_data = {'US': us_data,
                 'China': china_data}

us_china_pn = pd.Panel(us_china_data)
print us_china_pn

