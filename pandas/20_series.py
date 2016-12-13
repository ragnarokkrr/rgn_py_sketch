import pandas as pd
import numpy as np
import calendar as cal

pd.set_option('display.height', 1000)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


#  Series is really a 1D NumPy array under the hood. It consists of a NumPy array coupled with an array of labels


np.random.seed(100)

ser = pd.Series(np.random.rand(7))
print ser

month_names = [ cal.month_name[i] for i in np.arange(1,6)]
print 'month_names', month_names

months =  pd.Series(np.arange(1,6), index=month_names)
print 'months', months


# dict

curr_dict = {'US': 'dollar',
             'UK': 'pound',
             'Germany': 'euro',
             'Mexico': 'peso',
             'Nigeria': 'naira',
             'China': 'yuan',
             'Japan': 'yen'}


curr_series = pd.Series(curr_dict)
print curr_series


stock_prices = {'GOOG': 1180.97,
                'TWTR': 64.5,
                'AMZN': 358.69,
                'AAPL': 500.6
                }

stock_prices_series = pd.Series(stock_prices, index=['GOOG', 'FB', 'YAHOO', 'TWTR', 'AMZN', 'AAPL'],
                                name='stock_prices')

print stock_prices_series


#scalar


dog_series = pd.Series('chiuahuah', index=['breed', 'countryOfOrigin', 'name', 'gender'] )
print dog_series



###### OPERATIONS

print 'assign', curr_dict['China']

stock_prices_series['GOOG'] = 1200.
print stock_prices_series


try:
    stock_prices_series['MSFT']
except KeyError as ke:
    print 'KeyError', ke.message

print 'MSFT does not exist: ', stock_prices_series.get('MSFT', np.NaN)



# slicing

print 'stock sliced\n', stock_prices_series[:4]

print 'stock sliced by value\n', stock_prices_series[stock_prices_series > 100]

# mean, std, ser*ser, sqrt


##### NES



