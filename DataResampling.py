#Data Resampling
"""It's a whole problem
where everybody has:
either you have something that doesn't have any frequency
and you want to force it into something that has a frequency
( Or it just doesn't have the frequency that you want )

#match up 2 time series, more efficientyly

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

rng = pd.date_range('1/1/2011', periods = 72, freq = 'H')
ts = pd.Series(list(range(len(rng))), index = rng )
print(ts.head)

# I want to convert this into (a timeseries) every 45 minutes

# Hint: when I convert, I want a way to fill my new rows
# it doesn't make any sense, otherwise

converted = ts.asfreq('45Min', method = 'ffill')
print(converted.head())
# Freq: 45T, dtype: int64
"""Looking at this,
Q.what does this ffill (forward Fill) actually mean?
"""



#use prevous month
#@midnight 12:45 :
#Notice: they are not timeperiods, but timepoints (in time)
#lots of way to do the fill
#the most common is: the forward fill
#Take the data from the previous self
#Q. Why is the forward fill is much common than a backwardfill?
#this case is like those cases, when timeseries is special
##sometimes, you can interpolate data, (that makes sense!)
##with timeseries, looking into the future (not so helpful)
### there was a back-fill
### Interpolation: is another form of looking into the future (me: linear Interpolation,  is it?)
### Takeaway: you can interpolate, unless you know your data, ahead of you

#Q. what does the above code and the size, content of your data frame?

#What does the above code do to the size and content of your data frame?
"""think
original dataframe, has 72 members (72,)
more frequency -> more data)
"""
print( converted[1:10] ) # (95,)

# Tell me  your options, for filling Missing Data

## Let's check
print( ts.asfreq('45Min') )
# I'm going to get NaNs (me: alot of them)
# Anything that doesn't fall where it is used to  , it is just not a number
## if you don't want to fill, yo don't have to (pandas won't force you)

# How do I go to less frequent (rather than more frequent?)
"""maybe I have too much data, and I want less"""
converted = ts.asfreq('3H')
#useful in irregular timeseries


print(converted[1:10] ) 
print(ts[1:10]) #it is matching up!
# It seems to be matching up
#Q.should I just drop my data (column) is that good?
#A. No. I'm actually going to move to resampling
# it is much more flexible
"""that is one reason why I need resampling
more flexible than asfreq (the up down conversion)
"""
#Resampling
#Resample, every 2 Hours
resampled = ts.resample('2H').mean()
"""how it is deciding what number to fill in?
at 2, 2.5  (from 2 ,4)
at 4 , 4.5
where does data come from?
A.
2.5  from (2 ,4)
4.5 from  (4, 5)
"""

print(resampled[1:10] )
#That is it for regular timeseries data

#that is particularly useful we can use resample to event out irregular ts
irregular_ts = ts[list(np.random.choice(a = list(range(len(ts))), size = 10, replace= False)) ]

print("irregular timeseries") #it's really a mess (random indicies) 
print(irregular_ts)

#now, let us convert this `freq` to day

print(irregular_ts.asfreq('D') ) # gets me nothing! Q. What's the problem?
# ts data here are Not Consecutive [data is not ordered]
## So, you can sample, but need to reorder (data) afterwards
###Q. How to order?
###A. sort_index()

irregular_ts_sorted = irregular_ts.sort_index()
print(irregular_ts_sorted)
print(irregular_ts_sorted.asfreq('D') )#Daily frequency, now what happens?

# a bunch of NaNs: no method to fill in
# (anything doesn't land at 4 o'clock , just drop it )
print(irregular_ts_sorted.asfreq('D').count() )
#most of the times: you have to resample (but not with `asfreq` )
print(irregular_ts_sorted.asfreq('D').mean() )

print(irregular_ts_sorted.asfreq('D').var() )
"""Try

1. what if you want to go to a higher frequency, but you don't want to back fill or forward fill?
why might you want to do that?

2. What is the difference between .resample() and .asfreq() ?
3. How can I forward-fill only a few days? (hint: .fillna() )
4. What are some helpful functions to use with a Resampler object ?

logic of documentation
the more flexible (a function ) is
the less would be documented
aggregation operations
you do lot of things
resampling: is aggregation (of many functions)
do apply to do your own custom function

A1. we can do an Interpolation; but what if I don't want to do anything?

how can I accomplish that
None!

2.  asfreq(): very limied
resample(): produce an object that you can do more things of
like a resample object
Q. what do I want to do with it?
1. count it?
2. take its variance?
3. take its mean?
4. take its Quantile?

3. ffill


"""
print(ts.head())
print(type(ts))

#ts.resample(rule = 'ffill') #maybe we'll use the DataFrame...
#ts = pd.DateFrame({'values' : ts.values}, index = ts.index ) #Potential Bug

print(ts.resample('D'))

print(irregular_ts)


#fillna: non values using specific method
##To fill in Nans

print( irregular_ts.fillna(method = 'ffill',  limit=1) ) 
# I have resampled.Q. is timeseries still irregular?
#No, not anymore

#Recaop

rng = pd.date_range('1/1/2011', periods= 72, freq = 'H' )
ts = pd.Series(list(range(len(rng))), index = rng)

#Source:https://stackoverflow.com/questions/35204529/typeerror-object-of-type-int-has-no-len-error-assistance-needed
irregular_ts = ts[list(np.random.choice(a = list(range(len(ts))), size = 10, replace= False)) ] #credits: @e.doroskevic

irregular_ts =  irregular_ts.sort_index()
print(irregular_ts)

#fillna

print( irregular_ts.resample('H').fillna( method='ffill', limit=5 ) )
#where samples gone : how to resample?
"""limit
Use limitation , sometimes, which is useful for an irregular timeseries
Especially if data comes in chuncks
Maybe, have a user reports all morning
(20 mins user tells medication)
Then goes silent, till afternoon
That is good: I might have to forward fill 'ffill' in the morning
So, if irregular data, I can sort of bring things forward

But, I wouldn't bring forward my 11 am reading all the way to 4pm
here is where ffill is usefull,
I could extrapolate a bit (without going crazy)


"""


#experiment with the resampler
## resample Hourly 
resampler = irregular_ts.resample('H')
print("Mean")
print( resampler.mean())
print("Var")
print( resampler.var() ) 

# Moving window function
"""I know the whole Span!
but, tell me how are we doing, lately ?

1. Rolling window : familiar (small businesses
 while days might go up or down,
 owner wants to know how he's doing on weekly basis

 money made, over last 3 days

 2. Expanding window
 sometimes, you might get more data
 and all data (more distance, less distant in time)  are equally relevant

You're using all the data that you have
looking how that is changing over time

for small time , rolloing , expanding window the same

they match the time average
taking mean
the exampning window's mean will not go down, as quickly ,
because it remembers the mean , in earlier dates
weights them just as heavily, as the recent dates
lots of resons
1. protected in your own analysis:
from the meaningless, rapid change

i.e. Economics: some shocks might be uninformative (for your analysis)
you can sort of integrate those away
Sometimes it makes sense, somnetimes it doesn't

Q. why the rolling window is not as good as the actual series ?

A. got a bit of Latency (when setting last  3 days important (me:3MA) ) 
Today is the most important (me: 1MA)

# I am realizing I am looking at the wrong statistics
Q. how to deal with this?
A. 1. recenter your data (presentation)
    2. weight, differently

Hypothesis: the further away it gets, the less informative it gets
 the less I'm gonna weight it

special thing about time series: data points relate to one another
they are not independent

so we can compare them , and relate them .
One way to do this is to look  at how they change
example: we can difference a time series


 Takeaway: assume IID (Identically Independent
 you don't start the day with assumtion that:
 "today's value is Independent (of yesterday's value)
 Q. what's the best predictor of tomorrow's temperature?
 A. today's temperature , probably (is it dependent?)
 - it is dependent
 So, we want to use the rolling window, to use the best information we have
 (Although it is not the best information )

Relating immediate days to each other: differencing, shifting

in pandas, it's such a common operation, it is easily done.

"""

# ts = pd.Series(np.random.randn(20), pd.date_range('7/1/16',freq = 'D',periods=20))




ts = pd.Series(np.random.randn(20), pd.date_range('7/1/16', freq='D', periods=20)) #length values =20 must match periods=20
#Introduce a log
ts_lagged = ts.shift()

#

plt.plot(ts, color = 'blue' )
plt.plot(ts_lagged, color = 'red')
plt.show()
#it moved the data back , 1 period (for freq='D') that is 1 Day
#Where we start getting all those Synergies, work on timestamps,
#time related function


#what-if:
## I want things Hourly
## I want to move 5 hours
###I want to change my frequency freq = 'H' , shift ts.shift(5)
ts = pd.Series(np.random.randn(20), pd.date_range('7/1/16', freq='H', periods=20)) #length values =20 must match periods=20
#Introduce a log
ts_lagged = ts.shift(5)
plt.plot(ts, color = 'blue' )
plt.plot(ts_lagged, color = 'red')
plt.show()








