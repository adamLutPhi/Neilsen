# workin with time-based data
"""

READ & WORK WITH
Time-based data
different formats
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

filename='ao_monthly.txt'
#open file
with open(filename) as f:
    for X in range(5):
        print(next(f))
        #scientific representation

"""
Pandas has a read, for everything
here, Reading  a fixed-length file """

data = pd.read_fwf( filename,   header = None) #'data/ao_monthly.txt', header = None)

# Not so great [reason: no header]
print( data.head() ) 

#Let's see a dozen
print(data[1:12])


# Look at options, for read_fwf... what looks relevant?

#parameter:
##1. parse_dates
#True: parse Index

"""About reading in data

reading dates with pd.read function, have several time-related parameters, you can adjust:
parse_dates, infer_datetime_format, date_parser

Experiment with these using %timeit to see if there are performance differences

Hint: infer_datetime_format = True
no date parser provided.
What other combos, can you come up with?

"""

# import timeit
#First, let's see how to use a date_parser:

dateparse =  lambda x, y : pd.datetime.strptime('%s-%s' %(x,y), '%Y-%m')

#warning : could not infer format [elements will be parsed individually, ensuring parsing is consistent]
data = pd.read_fwf(filename, header=None, index_col = 0, parse_dates = [[0,1]], infer_datetime_format = True)
print(data)

##2. data_parser: function


#Funcion to use, for converting a sequence of string columns , to an array  of datetime instances.

print( data.head() )

"""
if we look at data analysis, we have great thing to report:
1. it has parsed the dates
2. it has paired our values

- it could becomem better

our datetime, doesn't have a frequency


"""

print( data.index )

#modify column header names
"""
Give columns , and indexes a more sensible name
"""
data.index.names = ['Month']
data.columns = ['Value']

# what is the empirical range of dates?
#Q. what is the timestamp of this dataset?
#q. what's a fast way to do this?
#A. get range(dates) How?: look at min, max (of index) 
print(min(data.index))
print(max(data.index))

# Check index type
"""What kind of index we have?
It's more of  a monthly average!
- the original dataset didn't include a date (just a month)
So, how am I supposed to get rid of that?


"""
print( type( data.index ) ) #pandas.tseries.index.DatetimeIndex


# can convert data's date by .to_period()
# in this case: pandas seem to know what we want, exactly

print( data.to_period() )

print(data)
# Now, data is in a nice monthly format

#Extra reading
"""
when reading in dates with a pd.read function, you have several time-related parameters you can adjust:
1. parse
2. dates
3. infer
4. datetime
5. format
6. date_parse

experiment with timing, to see what kind of performance differences to notice
Hint:
infer datetime.format = True
no date parser provided.

Q. What other combos can you come up with ?


"""
#vars: x,y: x: year , y: month (columns)
dateparse = lambda x, y: pd.datetime.strptime('%s-%s'%(x,y), '%Y-%m') #then convert to string format Year-month

# date_parser = dateparse: not found Reason: DEPRECIATED (throws a FutureWarning) instead, or read your data in as 'object' dtype and then call 'to_datetime' 
data = pd.read_fwf(filename, header=None, index_col=0,  infer_datetime_format = True  ) # parse_dates  = [[0,1]]) parameter removed
print(data)
# >>> [798 rows x 2 columns] year month value

# You can also extract datetimes from existing Data Frame columns

# new in pandas (0.18)
"""
DataFrame would work if data is already split into different columns, day, hour, month, year
it does the conversion for you 
"""

df = pd.DataFrame( {'year': [2015, 2016], 'month':[2,3], 'day':[4,5], 'hour':[12,13]} )
print(df)

# Truncating
"""another way to do indexing """
print("Truncating")
ts = pd.Series(range(10), index= pd.date_range('7/31/15', freq = 'M', periods = 10 ) )#, period = 12 ) ) ValueError: Length of values (10)
print(ts)

#Takeaway: truncating preserves frequency
print("Truncating preserves frequency") # for a more 'Verbal' truncating
print(ts.truncate(before = '10/31/2015', after='12/31/2015'))     
            

# You can truncate in a way that does not preserve frequency
print("Truncating without preserving the  frequency") 
print( ts[[1, 6, 7]].index) 


# But Pandas will try to preserve frequency automaticall, whenever possible
#for every month (from 0 till 10) , jump every 2 months #{Keep that frequency }
print( ts[0:10:2] ) #index) 
