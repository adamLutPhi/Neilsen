# Moving window Functions
#Window functions give you moving aggregate measure of a time series

#Window functions are like aggregation functions
# you can use them in conjunction with .resample()

#@2:21:34
# Start with a  DataFrame
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
# df = pd.DataFrame(np.random.randn(600,3), index = pd.date_range('5/1/2016',periods=600), columns = ['A', 'B', 'C'])
df = pd.DataFrame(np.random.randn(600,3), index = pd.date_range('5/1/2016', freq='D' ,periods=600), columns = ['A', 'B', 'C'])

print(df.head())

#It's just a DataFrame

#There shouldn't be any trends
df.plot()


plt.show()


# let's do a rolling window

print( df.index )


# set window to 20
# this is turn-able into  a one-liner
r = df.rolling(window =20)
print(r)
# not impressive, it has got data arranged, for you (but what are you actually doing with the rolling window
#me: is there a higher ordeer Perspective in play ?  
# Note: it is not impressing, until you tell what to do with such data 


#Example: a Rolling mean

### choose Plot Criterion : draw with  color = 'gray'
print ( df['A'].plot(color = 'gray') )

### show mean values, color them in 'red' (to seperate them from gray ones 

print( r.mean()['A'].plot(color = 'red') )
plt.show()


# Try out some of these options with .rolling()
"""
r.agg , r.apply, r.max, r.median, r.name, r.quantile, r.kurt [kurtosis],
r.skew , r.sum, r.var [Variance]"""
isNumeric = True
print("Count 'all'")
print( r.count())
print("Count 'A'")
print( r['A'].count())
print( r.kurt(isNumeric)  ) 

print( r.quantile(0.5).plot())# the 50th percentile (50%)

plt.show()#necessary
"""it's cool to explore
with the smallest amount of work,
see what the

To apply more than 1 function , use r.agg()
"""
print( r.agg(['sum', 'count']).plot()) # Blue, Green , Purple visualize the systematic relationship

plt.show() #apply the last plot() command (in IDLE)



#( comment using # , to hide  )
print( r.quantile(0.5).plot() )
plt.show()

# Custom Functions

##Hint: upon calling the rolling function, use the .apply(then lambda whatever we like)
###example
"""
Lambda: recieves a numpy array, just 1 value
-Justify first value, by the 2nd value
"""

# a rolling

# divide 2nd Col 'B'/ 3rd col C
#print( df.rolling(window = 10, center = False).apply(lambda x: x[1]/x[2])[10:30].plot() )
#plt.show()

# Min - Max
#( comment by # , to hide  ) 
df.rolling(window = 10, center = False).apply(lambda x: x.max() - x.min()).plot()
plt.show()



"""That's interesting, but maybe intereset to learn about:
- the difference; between the first & last value

Where:
Index   :  Label 
  0     :  first [start ]
 -1     :  the last [end ]

"""

df.rolling(window = 10, center = False).apply(lambda x: x[0] - x[-1] ).plot()
plt.show()# show last computation

#Q. how about the Opposite?
df.rolling(window = 10, center = False).apply(lambda x: x[-1] - x[0] ).plot()
plt.show()# show last computation

df.rolling(window = 10, center = False).apply(lambda x: x[1] - x[-1] ).plot()
plt.show()

# Q. what if I want to generate :
## Rolling window function, of Monthly data (from daily data) [me: a la real-world ]
"""
What If I want to generate a rolling window function, of monthly data ?
Q. How to do that :
A. Algorithm

1. Generate random data n ( Q. is the more , merrier? )
2. Start from a generic date '7/1/16' (with periods =200) [business days , a year]

3. Use a frequency parameter freq = 'D'
4. use resampling rate ts_long.resample('M')

"""

#2 Ways to implement this ( a long time series)
#1. The first way,  use a random normal distribution with a set of n = 200 points , starting date = '7/1/16', freq = 'D'

ts_long = pd.Series(np.random.randn(200), pd.date_range('7/1/16', freq='D', periods=200 ))
#2. Or, Set the resampling to monthly 'M', taking the mean (on a monthly basis)
                    # also take a  rolling window (with 3 days)
                    # take the mean of those days
                    # In the end, plot
ts_long.resample('M').mean().rolling(window = 3).mean().plot()
#@2:32:26
"""once I'm comfortable, it would be as easy as 1,2,3"""

# in IDLE, we explicitly have to show output:
plt.show() 



df.index #has a scaling of
"""it's upo to you to ensure 
time window size make sense
"""
r = d.rolling(window = 20)
"""
it's not something , until tell it what to do
"""
# roll a mean

r = df.rolling(window = 20)
print(r)

df['A'].plot(color = 'gray')
r.mean()['A'].plot(color='red').plot()
plt.show()

# Try some of options, with rolling()

# r.agg, r. apply(), r.count, r.kurtosis , r.skew()

r['A'].count()

r.quantile[.50].plot()
#apply more 1
r.agg['sum', 'var']






# Expanding window
""" as opposed to rolling windows (the 95% of applications) whereas
the rolling window: the windows keeps getting bigger (until reaching some bound)


1. define an expanding window function
2. With min periods min_periods = 1
3. take the mean of that time series

(Assume: we start from 0)
4. finally, plot result

Mme. Nielsen" what you see is typical to every expanding window"


"""

print( df.expanding( min_periods = 1).mean().plot()) 

#in idle , show result
plt.show() #observe, it's a line #TODO, check the slope (or angle theta) 
#me: it looks like a shock (electric or not) around a mean 0,  (assumes timeseries is normal)
#Nielsen: result is not surprising, since they all are randomly sampled
#surprised, why they are converging faster  (to 0 )
#me: so , eventually they all go back to 0, the status quo, and default state




#load
ts_long  = pd.Series(np.random.rand(200), pd.date_range('7/1/16',  freq='D',
                                                        periods=200))

ts_long.resample('M').mean().rolling(window= 3).mean().plot()



#cross-ref: survival function 




"""me: the displayed figure sounds to be useful
In A,(for a timeseries A
 divided into 2 regions: above, and below (the Orange Line) 
 
"""

#Try
#EMA 
# 1. How to perform an exponentially weighted moving average
# 2. When would you use an expanding window vs. rolling window?
# 3. Write A CUSTOM function to replace .quantiles(0.5) function for
# a rolling window?  #~moving average~?
# 4. How would you compute more that 1  aggregation function on a moving window function at the same time?

ts = pd.Series(np.random.randn(1000), index = pd.date_range(start = '1/1/16'))
ts.own(span = 60, freq = 'D', min_periods = 0, adjust = True).mean().plot()
ts.rolling(window = 40).mean().plot()

# It's better not to look at things, that are not in the center of your window
# Beginning at center of window

# If adding new members, where old items are Still relevant

## recording more data

#1 I need a rolling object (for the past 20 entries) 
r = df.rolling(window = 20)
#2 sort time : get the one corresponding to the quantile
r.apply(lambda x: sorted(x)[round(len(x)*0.5)])
#note:  roll over 60 items( maybe items are minutes), calculate the mean of minutes / per hour 
ts.rolling(window = 60).mean().plot()


#3  sort time with quantile 
r = df.rolling(window = 20)
r.apply(lambda x: sorted(x)[round(len(x)*0.5)])

ts = pd.Series(np.random.randn(1000), index = pd.date_range(start = '1/1/16' , periods=200) 

#4 plug-in 
r = df.rolling(window = 20)
r.agg(['sum', 'count']).head()

#I wonder why we didn't stick with the expanding window...
               

#Last, but not least

#apply for 1 column 'A' (out of 3: A, B, C)
print( r['A'].agg(['sum', 'var']).plot()) #me: they look more tight together (they Co-relate?!)
plt.show()
