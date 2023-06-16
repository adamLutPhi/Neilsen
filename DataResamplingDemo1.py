#Data Resampling
"""Head's up: It's a whole problem
where everybody has:

1. Either you have something that doesn't have any frequency
and you want to force it into something that has a frequency

( Or it just doesn't have the frequency that you want )

#match up 2 time series, more efficiently

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



# Use prevous month
# @midnight 12:45 :
# Notice: they are not timeperiods, but timepoints (in time)
# Lots of way to do the fill
# The most common is: the forward fill `ffill`
# Take the data from the previous self

# Q. Why is the forward fill is much common than a backwardfill?
# A. this case is like those cases, when timeseries is special

## Sometimes, you can interpolate data, (that makes sense!)
## With timeseries, looking into the future (not so helpful)
### There was a back-fill
### Interpolation: is another form of looking into the future (me: linear Interpolation,  is it?)
### Takeaway: you can interpolate, Unless you KNOW your data, ahead of you

# Q. what does the above code and the size, content of your data frame?

# What does the above code do to the size and content of your data frame?
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
# Q.should I just drop my data (column) is that good?
# A. No. I'm actually going to move to resampling
# It is much more flexible
"""that is one reason why I need resampling
more flexible than asfreq (the up down conversion)
"""
# Resampling
# Resample, every 2 Hours
resampled = ts.resample('2H').mean()
"""How it is deciding what number to fill in?
at 2, 2.5  (from 2 ,4)
at 4 , 4.5
Q.where does data come from?
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

# A bunch of NaNs: no method to fill in
# (anything doesn't land at 4 o'clock , just drop it )
print(irregular_ts_sorted.asfreq('D').count() )
# Most of the times: you have to resample (but not with `asfreq` )
print(irregular_ts_sorted.asfreq('D').mean() )

print(irregular_ts_sorted.asfreq('D').var() )
"""Try

1. what if you want to go to a higher frequency, but you don't want to back fill or forward fill?
why might you want to do that?

2. What is the difference between .resample() and .asfreq() ?
3. How can I forward-fill only a few days? (hint: .fillna() )
4. What are some helpful functions to use with a Resampler object ?

#Documentation tips

Logic of documentation
"the more flexible (a function ) is, the less would be documented"


aggregation operations

resampling: is aggregation (amongst many functions)
Do apply to do your own custom function

A1. we can do an Interpolation; but what if I don't want to do anything?

Q. How can I accomplish that
A. None!

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
##To fill-in Nans

print( irregular_ts.fillna(method = 'ffill',  limit=1) ) 
# I have
#Q. is timeseries still irregular?
#No, not anymore [Takeaway: by filling, timeseries is regularized ]

#-------
# Irregular Time Series

# Pentagonal Control Parameters:

#1. numPoints

numPoints1 = 10

#2. startingDate

startingDate1 = '1/1/2011'
#3. frequency

frequency1 = 'H'

#4. periods

periods1 = 72

#5. is replacable?
isreplace1 = False


#Recap

rng = pd.date_range('1/1/2011' ,  freq = 'H' , periods= 72 )

#or generalized as
rng = pd.date_range(startingDate1,  freq = frequency1, periods= periods1 )

ts = pd.Series(list(range(len(rng))), index = rng)


#Source:https://stackoverflow.com/questions/35204529/typeerror-object-of-type-int-has-no-len-error-assistance-needed
irregular_ts = ts[list(np.random.choice(a = list(range(len(ts))), size = numPoints1 , replace= isreplace1 )) ] #credits: @e.doroskevic

irregular_ts =  irregular_ts.sort_index()
print(irregular_ts)

#fillna

print( irregular_ts.resample('H').fillna( method='ffill', limit=5 ) )
#where samples gone : how to resample?

"""limit

Use limitation , sometimes, for `irregular data`: it is useful for an  timeseries
Especially if data comes in `chuncks` (me: spikes: huge ups, downs)
Maybe, have a user reports all morning (me : ~ 9 am- 10 am
(20-mins user tells medication)
Then goes silent: till Afternoon (me: ~ 3 pm  4 pm)
"""

"""# ForwardFill

I might have to forward fill 'ffill' in the morning
But, if (it's) irregular data, can bring things `forward`

But, I wouldn't bring forward my 11 am reading all the way to 4pm
here is where ffill is useful,
I could extrapolate a bit (without going crazy!):

"""


#Irregular Data - Experiment with the resampler
## Resample Hourly

resampler = irregular_ts.resample('H')
print("Mean")
print( resampler.mean())
print("Var")
print( resampler.var() ) 

# Moving window function

"""I know the whole Span,
But, tell me how are we doing, lately ?

1. Rolling window : familiar (small businesses)
 while days might go up or down,
 owner wants to know how he's doing, on weekly basis (weekly)

 (then,) the money made (profit), over last 3 days

 2. Expanding window
 Sometimes, you might get more data
 and all data (more distance, less distant in time)  are equally relevant

You're using all the data (you want)
- look how data is changing over time

For small time, rolling, expanding window the same

They match the time average:
Taking the mean:

Note:the sampling window's mean will not go down, as quickly [Why?]
"""

"""2 Hypotheses

-me: Hypothesis 1: Mean-reversion:
Because it remembers the mean ( in earlier dates)

weights them just as heavily, as the recent dates [Why?]
(For) lots of resons:

1. (You're) protected (Well-formed) in your own analysis:
From the meaningless, rapid change

Noise  i.e. in Economics : some shocks might be un-informative (for your analysis)
You can - sort of- integrate those away:

Note: "Sometimes it makes sense, sometimes it doesn't"


Q. why the `rolling window` is not as good as the actual series ?

A. (Has) got a bit of Latency (when setting last 3 days important (me:3MA) ) 
Today is the most important (me: 1MA)

# (What-if:) I am realizing I am looking at the wrong statistics
Q. How to deal with this?
A.(workarounds)
   1. re-center your data (presentation)
   2. weight (data) differently

- Hypothesis 2: Present is more important: the further away it gets, the less informative it gets
 So, the less I'll weight it )
 
Special thing about time series: data points relate to one another
 So, they are not independent ]


Hence, we can compare them , and relate them. [How?]

One way to do this is to look  at how they change
Example: we can difference a time series
"""

"""
Takeaway: Sampling Assumption  Assume I.I.D (Identically Independent Data)
 you don't start the day with assumption that:
 
 "Today's value is Independent (of yesterday's value)
 Q. What's the best predictor of tomorrow's temperature?
 A. Today's temperature , probably (is it dependent?)
 - It is dependent!
 So, we want to use the `rolling window`, to use the best information we have
 (Although it is not the best information! )

Relating immediate days to each other [How?]: differencing, shifting

In Pandas, it's a common operation, easily done:

"""

#Takeaway: Assume timeseries is `Normally Distributed`

#1. Generate (randomize  normally distributed (default assumption ) 
# ts = pd.Series(np.random.randn(20), pd.date_range('7/1/16',freq = 'D',periods=20))
# Takeaway: Range's triad:
##1. Starting date
##2. frequency: freq = 'D'
##3. periodicity: periods =20

#Now, it moved the data back, 1 period (for freq='D') that is 1 Day
#Where we start getting all those `Synergies`, work on timestamps,
#Time-related function


#change start Data and Periods

##hyperParameters Quarted

# 1. starting Date 
startingDate2 = '7/1/16'

#2. frequency 
frequency1 = 'D'

#1. numPoints

numPoints2 = 20

#2. startingDate

startingDate = '7/1/16'  # '1/1/2011'
#3. frequency

frequency1 = 'D' # 'H'

#4. periods  

periods2 = 20  #72



ts = pd.Series(np.random.randn(20), pd.date_range('7/1/16', freq='D', periods=20)) #length values =20 must match periods=20 (otherwise date_range wouldn't work)

# or generalized regular timeseries form as follows:

ts = pd.Series(np.random.randn(numPoints2), pd.date_range('7/1/16' , freq= 'D' , periods= numPoints2 )) # regular timeseries must have numPoints2 = periods2 = 20  (else it won't work ) [why] it is a Regular timeseries!

#1. Introduce a lag
ts_lagged = ts.shift()

#2. Plot
plt.plot(ts, color = 'blue' )
plt.plot(ts_lagged, color = 'red')
plt.show()

# I have  changed things in matter of hours

##Q. what If I want to shift into the 'Past' ?

##A. Negative numbers: shift(+5), shift (-5), ts.shift(-5)

# What-if:

# I want things in:
##  1. Hourly
##  2. 5H (shift= 5 move 5 hours)
### 3. change  frequency freq = 'H' , shift ts.shift(5)

#1. Generate data (from random)

#  parameters's Pentagon (to play with) :

# 1. starting_date = 7/1/16
# 2. Points generated : numPoints =  20
# 3. frequency = H
# 4. periods:  numPoints= 20
# 5. lag = 5

# hyperParameters (Quartet):

#1. numPoints
numPoints2 = 20

#2. startingDate
startingDate2 = '7/1/16'

#3.  frequency
frequency2 = 'H'

#4.  lag
lag2 = 5

# ----

#1. Generate timeseries

ts = pd.Series(np.random.randn(20), pd.date_range('7/1/16' , freq= 'H' , periods= 20 )) #length values =20 (numPoints) must match periods i.e. numPoints = 20 && periods =20 

#2. Lag
ts_lagged = ts.shift(-5)

#3. Plot
plt.plot(ts, color = 'blue' )
plt.plot(ts_lagged, color = 'red') # the lag is in red, the lag is forward in time
plt.show()

#1. Generate 
ts = pd.Series(np.random.randn(numPoints2), pd.date_range(startingDate2 , freq= frequency2 , periods= numPoints2 )) #length values =20 must match periods=20

#2. Introduce a lag
ts_lagged = ts.shift(lag2) # -5

#3. Plot
plt.plot(ts_lagged, color = 'red') 
plt.plot(ts, color = 'blue' )# the lag is in Blue, the lag is forward in time

plt.show()

#Takeaway: To shift indicies rather than data, &  use t-shift

"""I avoid tshifts
sometimes It renders data `funky`
(it had martin Luther King day, where it shouldn't)

#Generation Algorithm (triad)
1. Generate (from random distribution)  
2. lag [Auto-correlation]
3. plot


Takeaways [5+]:
1. by fill irregularized timeseries, it become `regularized`
2. Sampling Assumption  Assume I.I.D (Identically Independent Data)
3. Assumption: timeseries is `Normally Distributed` (me: vanilla timeseries) 
4. To shift indicies rather than data  , use t-shift
5. you can interpolate, Unless you KNOW your data, ahead of you
6. Extra: Documentation:  "the more flexible (a function ) is, the less would be documented"

"""



