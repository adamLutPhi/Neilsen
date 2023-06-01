#Dealing with Time

# pandas function
"""
1. Generate sequences of fixed-frequency dates & time-spans

2. Conform or convert time series to a `particular frequency`
friends 45 mins, or you 90 mins

3. Compute `relative dates`:  based on various non-standard time increments
(e.g. 5 business days before the last day of the year )
or `roll dates:
backwaards , forwards

i.e. economics: custom business days: pandas knows it for you 
"""
# from zoneinfo import ZoneInfo
import tzdata
import pandas as pd
import numpy as np 
# Generate Series of times
period = 10
rng = pd.date_range('2016 Jul 15 10:15', periods = 10, freq='MS')
print("rng = ", rng )
# with freq= 'M' #end of month
# 'H' #Hourly
# 'D' #days
# 'B' #business (days)
# few ways to specify what happens:
#start date, numnber periods (jump this much (per jump), & do it n times 
#frequency = 'B'


#start Jul 31 WHY: I chose months (accounting: end of month )
#with freq= 'MS'

# preserves time

# start at n date :
"""july 1st to 31st"""
#Need : start end , frequency
#  OR : start, frequency, number of times

# Do whatever suits you:

#  Jul 15th to Jul 25
# dog: needs walk,every 8 hours

rng = pd.date_range(start ='2016 Jul 15 10:15', end='2016 Jul 25',freq = '8H') # no period periods = 10, freq='MS')

print(rng)
print(len(rng))

#Another way: count backwards: freq ='-8H'
## rng = pd.date_range(start ='2016 Jul 15 10:15', end='2016 Jul 25',freq = '-8H') # no period periods = 10, freq='MS')
# Note: there are ways to combine those things (read docs)

# 1. every 1H on 'B' Business day
# 2. every 3pm on '3rd' Business day (of the month )
#tz = 'Asia/HongKong'


rng = pd.date_range(start ='2016 Jul 15 10:15', end='2016 Jul 25',freq = '8H',
                    tz = 'Asia/Hong_Kong') # no period periods = 10, freq='MS')


# with normalization
rng = pd.date_range(start ='2016 Jul 15 10:15', end='2016 Jul 25' #,freq = '8H'
                    , freq = 'D'
                    #, tz = 'Asia/Hong_Kong'
                    , normalize = True) # no period periods = 10, freq='MS')
# Normalize: start and end day to mid-night (before generating the date range )
"""Use it when:
maybe you want it (to Be) the same time, even at different dates
All at the same time 
"""

print(rng)
print("type(rng[0]) = ", rng[0])
# pandas.tslib.Timestamp

#which formatting sdoe not work?

#Pandss: timeseries is very pro-North America

"""algorithm: when things are ambiguous interprets them in the american/US Style
anyone to use Euro-Dates, neet to set a flag:
first flag
"""
#Many ways to add dates

'2016 Jul 1' , '7/1/2016', '1/7/2016', 'July 1, 2016', '2016-07-01'
#Only in English, as well!

# Timestamps

##add increasing detail
pd.Timestamp('2016-07-10')

# Different times of data (we can have)

# July, 10 : timestamps on top of 64-bits, data-type
##down to nano-seconds
print( pd.Timestamp('2016-07-10 10:15:15.123456789') )  #nano-seconds
#fields for nano-seconds: finance,. in physics:
# Downside of nanoseconds: data is big, lot  of `datastorage`
#example: tey to make economic forecast, past year 400

# How much detail can you add

t = pd.Timestamp('2016-07-13 10:15:15')

# t.quarter
#3

# t.dayofweek - Monday is the fist day of the week 
#2
#quarter 

#t = pd.Timestamp('2016-07-10 8 pm')

t = pd.Timestamp('2016-07-10 8 pm')
print("t = ", t)

# Also Other handy dates:

# is_month_start
# is_month_end

# if you ever have to deal with something like: `before 1600`
# you sacrifice the deal, right?

#Q. Julian dates?
#A. unsure(calendar) : it can accomudate custom dates: holiday schedules
#I know  an easy way to add all offsets
#Golden question; what Does timestamps lack?

"""Takeaway: Time Has Ranges!
it is not usually 
sth where sth stamped it
"""
#Time Deltas
## might have time like this :
#print( pd.Timedelta('1 day lns') )
""" print(pd.Timedelta('l5 ns')* 1000  ) #  calue error could not convert string to #BUG """


"""
Takeaway:
Unless you do thing too destructive, panda's going to presve that thing to you
you add a day to all of them

# month start and it updates for you
end of time delta

don't wanna my timestamp, & hop-scotching that into the next big thing 
"""
#Time Spans 
p = pd.Period('7/2016') # 1.mark a period, at any time (we want) i.e. july 2016
t = pd.Timestamp('7/21/2016') #.TimeStamp('7/21/2016')

p.start_time < t and p.end_time > t

# pd.period 
# generate a range of periods
# that would makes sense, in the `same way`

#May be all day, in monday , everymonth
## all day, business day
#Lot of work to me,

#Takeaway: hour weakness (detected)

rng = pd.period_range('2016-01-01 12:15', freq = 'H', periods =10 )
print("rng = ",rng)

#to get around the hour Weakness
rng = pd.period_range('2016-01-01 12:15', freq = '60T', periods =10 ) #<--- #TODO:UncommentME

print("rng = ",rng)
from pandas.core.dtypes.dtypes import PeriodDtype
"""desc

# period

    _typ = "periodindex"

    _data: PeriodArray
    freq: BaseOffset
    dtype: PeriodDtype

PeriodDtype(freq)
    
>>> idx = pd.PeriodIndex(year=[2000, 2002], quarter=[1, 3])


pandas has this policy of round sensible numbers:

# how can you determine whether
timestamp falls within a given period ?

# load snippetw/ startend.py
#50:13

rng

"""
"""
- the frequency is different

statsmodels.tsa.statespace.mlemodel

frequency: month
(takes you till end of the month
"""


print(rng + pd.Timedelta('1day')) #freq = MS #month Start #ok


#pandas trying to preserve thst, for you

"""take dates
add a date
figures it is still a month `start` & `end couple (tuple)

- mark a period , at any granulary want
july 2016 
"""

#Time Span

p = pd.Period('7/2016')

t = pd.Timestamp('7/21/2016') 

#check if timestamp fall in the `range`:

condition = p.start_time < t and p.end_time > t #True

#Solution: wait for the  them , till they finish


#(besides a range of dates, 
## Generate a range of periods

rng = pd.period_range('2016-01-01 12:15', freq = 'H', periods = 10)


rng = pd.period_range('2016-01-01 12:15', freq = '60T', periods = 10)      


"""that  males sense of the default behavior, if wannt to go (around that)
-> go to the next level of granularity"""


rng = pd.period_range('2016-01-01 12:15', freq = '1H', periods = 10)   #also okay '1h'

print("rng = ", rng)
"""takeaway:
a period gives a `periodIndex` rather than a datetime index ''


# Anchored Offsets

W-SUN  weekly frequency (sundays) same as W
W-MON
W-TUE
W-WED
W-THU
W-SAT

quarterly, ens in : 
(B) (Q(*S) - JAN
(B)Q(S)-FEB
(B)q(S)-MAR
"""
#How can you make a pandas Time Series with these aliasses
num_periods = 40
_pd = pd.Series( range(num_periods), pd.period_range('2016-07-01 11:15', freq='60T', periods = num_periods )) # 53:44
print("pd",_pd)
# Try out some other functionality with different offset

#----
# How can you determine ewhether a time stam falls within a given period?
#load snippets/ startend.py

##timestamp
###period
#if we do this period

"""it will default to a monthly period """

p = pd.Period('2016-07') #UPDATE: 58:12 "If I go back to monthly (from daily), it should be fixed  "
print("p ", p) # M - gonna have to specify that (month)

#if i go ahead, give it a day (it'll give me a `daily` period)
p = pd.Period('2016-07-21')
p = pd.Period('2016-07-21 10') #if i give it an `hour`, gives me an hourly period
""" very intuitive, the best way to learn is to ask what if """

print("p ", p) # D 
print("start t = ", p.start_time )
print("End t = ", p.end_time ) 

# DO a time falls betwee 2 periods?

"""if I want to figure that out,
todo that: pick a time, not in that period
"""
t = pd.Timestamp('July 5, 1812') #earth quake # [that's how we've won the war]
print("p",p.start_time)
""" if times goes uo (always
if i want to fall between that
do i want a falue > or < stat_time
later time
- not guaranteed, but at least, after the period have started
"""
print(" p.start_time < t",  p.start_time < t ) #False # not within
#----
#Try again
t = pd.Timestamp('July 5, 2016') # Another earth quake
print(" p.start_time < t",  p.start_time < t )#False

# """reason: period starts at the 21st (July)"""
t = pd.Timestamp('July 22, 2016')
print(" p.start_time < t",  p.start_time < t ) #True #now i make it in

#REDO Exercise

p = pd.Period('2016-07')
print("p ", p) # M
print("start t = ", p.start_time )
print("End t = ", p.end_time ) 

# DO a time falls betwee 2 periods?



#----
#Try again
t = pd.Timestamp('July 22, 2016') #another earth quake
print(" p.start_time < t",  p.start_time < t )#False

"""reason: period starts at the 21st (July)"""
t = pd.Timestamp('July 22, 2016')
print(" p.start_time < t",  p.start_time < t ) #True #now i make it in

print(" p.end_time ", p.end_time ) # 57:32 
print(" p.end_time > t",  p.end_time > t ) ## end_time should be greater than t
""" now, I am at the super set
- it's mostly how the properties are
-- how (2) things relate to each other
--- the main thing: time goes Up! the forward march of time, it gets bigger and bigger
---- think about linux time stamps

it's 9:06 , I think we deserve a break (let's call it a ... 5 , 10 minute break
- after break
2 announce ments
it tales longer
-From berkley to Austin (TX) than from Boston to Austin (TX) ;)
in a 12K 200 journey, 200 is epsilon, in many fields ~!
i.e. i work in diabetes management
(that's scary if you're diabetic
`Blood glucose` monitors only have to be accurate to +/- 20 % -> which is must be the best we can do
, hence 200 miles is certainly an epsilon
-----

2. there is much more beautiple and expressive Way to check the range
"""
print("More Beautiful , expressive way to check time:  p.start_time < t < p.end_time = ", p.start_time < t < p.end_time  )

"""footnote: it's shorter and it shows what we want to do. this is yet another reason why python is beautiful, simple """
""" so, we still  in "how we address a `Timeseries` in a `daterange` ..
- I only care about them: if I can fit them in a useful way """

# How can we index a time series with  a `date_range` ?

num_periods = 40
#count up: `daterange` with num_periods = 40, freq = 60 Minures, starting at July 1st
ts_dt = pd.Series( range(num_periods), pd.date_range('2016-07-01 11:15', freq = '60T', periods = num_periods)) 

#ts_dt.head look at the beginning
print("ts_dt.head() =", ts_dt.head()  )

#look at end: .tail
print("ts_dt.tail() = ",ts_dt.tail() )

print( "type( ts_dt.index) = " , type( ts_dt.index))
      
"""but what does `datetime` index     `ts_dt.index` contain?
takeaway: datetime indexes: hold `timestamps
"""

num_periods = 40
ts_dt = pd.Series( range(num_periods), pd.date_range('2016-07-01 11:15', freq = '60T', periods = num_periods))
ts_dt.head()
print( "type(ts_dt)", type(ts_dt.index) )
print( "type(ts_dt.index)[0]", type(ts_dt.index) ) #TypeError: type 'DatetimeIndex' is not subscriptable
"""Recap:
1. Timestamp
2. DateTimeIndex 
3. period
4. perod index

Q. why does it matter?
A. there is some really cool string indexing (still haven't mentioned, yet )

Makes it easy access ranges, dates  (or a particular )

- I want to think of these `ts_dt('2016-7-11') ` as periods 
Takeaway; It's not line
"""
# What are the use cases for a series with a DateTimeIndex 
print("ts_dt['2016-7-11'] =", ts_dt['2016-7-1 11'] )

"""Takeaway:
It's not I have a point in time every hour, it's I have an hour, every hour ( & they stack UP)
- If I want a period (and not a  `timestamp` ) (then)
Q. How would I modify this code? 

1. The value of series won't going to change
2. number of periods num_periods` won't change
3. Now, Instead of daterange `pd.date_range` I want a period range `pd.period_range`

`ts_dt.head()`

# Check what the index is

Takeaway:
Differentiate

1. point in time
2. period in time

Each (object) has its data `type`
And the kind of index

40 million rows: (no memory o(for that))
- how about
40 thousand rows


"""

num_periods = 40
ts_dt = pd.Series( range(num_periods), pd.date_range('2016-07-01 11:15', freq = '60T', periods = num_periods))
ts_dt.head()

# How can we convert between a `DateTimeIndex` and a `PeriodIndex` ?
"""Q. should we go back & re-declare the whole thing?
A. Instead
We're going to use these 2 handy functions

ts_dt.to_period()
ts_pd.to_timeStamp()
experiment with that , pass them back and forth

1.convert to a period


"""

print("type(ts_dt.index[0]) = ", type(ts_dt.index[0]) )

# print("ts_pd.to_timestamp() =", ts_dt.to_timestamp() ) # 


print("ts_dt = ", ts_dt )
print("ts_dt['2016-7-1 11'] = ", ts_dt['2016-7-1 11'])

print("pi = ts_dt.to_period() = ", ts_dt.to_period() )

#print("ts_dt.to_period() = ", ts_dt.to_timestamp() )

pi =  ts_dt.to_period()

result = pi.to_timestamp()
#pi[::2] #unsude about the size 
print("pi.to_timestamp() = ", pi.to_timestamp() )
"""pandas/tests/frame/methods/test_to_timestamp.py
source: https://github.com/pandas-dev/pandas/blob/fe85cbfb20f3f360ebba62905b93a6f98bf655c1/pandas/tests/frame/methods/test_to_timestamp.py

"""
from datetime import timedelta
from pandas import date_range
import numpy as np
exp_index = date_range("1/1/2001", end="12/31/2009", freq="A-DEC")
print( "date_range(\"1/1/2001\", end=\"12/31/2009\", freq=\"A-DEC\" ",exp_index )
exp_index = exp_index + timedelta(days=1)  #timedelta(1, "D") #- timedelta(1, "ns")
ts_pd = exp_index + timedelta(days=1) # point-data [time-serie]
exp_index = exp_index -  np.timedelta64(1, "ns")
exp_index.freq = 'A-DEC'
print("  exp_index -  np.timedelta64(1, \"ns\") ", exp_index)

#---

"""Check the docs:
scipy 2014

converting between Representations

Instead of ts_dt.to_period(freq = "D")
ts_dt.freq = 'D'

1:06:19

This function takes every hourly time on july 1st convert to date july first

What if we do hourly H ?

freq = '60T' minutely (60 minutes) 1:06:55
"""
# ts_dt.to_period(freq = 'D') old

# ts_dt = ts_dt +  timedelta(days=1)

# TypeError: Concatenation operation is not implemented for NumPy arrays, use np.concatenate() instead.
## print("ts_dt +  timedelta(days=1)", ts_dt.to_period() +  timedelta(days=1)) 



"""can just specify the `frfequency`

freq is the key word 

"""
#comparison
## got a period indexed timeseries ts
# period-indexed time series
print("period-indexed  = ", ts_pd) #.head())

#time-indexed time-series
print("time-indexed  = ", 
ts_dt.head())
# 1:07:45

""" someone
freq strings are `hard` to track down
agreed, but pretty consistent
always freq is keyword

Notice:

on period ts:  no seconds
why:
because it's a period stamp
every second is part of that period

Can have nano-second (as small as datatype allows
----
Let's think about this string indexing : 

ts_pd.to_timestamp()

Takeaway: complement of 2 periods
is (2) timestamp
- 2 period , 2 timestamp

datetime, datetime index (to `timestamp`)
period , periodIndex ( to `timestamp`)

These things keep piling up
but have (mostly) the same vocab !

"""
from pandas import DatetimeIndex
#conversion (timeseries to timestamp)

ts_pd = DatetimeIndex.to_period( ts_pd,freq = '60T' ) # <--- 


# Indexing

##timeseries (timestamp)

print( ts_dt['2016-7-1 11'] )



# you do the same thing: even anti social people have to take a stance

#print( ts_pd['2016-7-1']) #<---- DNE
#11'] )
# print( ts_pd.head() )


#print("type(ts_dt.index[0]) = ", type(ts_dt.index)) # [0]) )

# 1. change the day

#print( ts_pd['2016-7-1'])

"""how do I find a range?

"""

print( ts_dt['2016-7-1 11'] )

#print ( ts_pd[ pd.period_range(start = 'July 2 2016', end = 'July 3 2016')] )  #, freq = '60T')]

#print( ts_pd.loc['2016-7-1' : '2016-7-2' ] )  # ('2016-7-1' : '2016-7-2']))
##print(type( ts_pd['2016-7-1' : '2016-7-2' ] ))  # ('2016-7-1' : '2016-7-2']))



print( ts_dt['2016-7-3']) #11'])

print(ts_dt[ : '2016-7-2' ])

print( ts_dt['2016-7-1' : '2016-7-2' ] )

# july 2nd or later

print( ts_dt['Jul 2 2016': ])  # '2016-7-1' : '2016-7-2' ] )

# print( ts_dt['Jul 2 ': ])  # So not Work #haven't specified year


""" how to time sgam eu sty
print( ts_dt['Jul 2 2016': ]._day)  # '2016-7-1' : '2016-7-2' ] )
"""
print('20/12/2016')

# Try march 4th 2016




# print( ts_dt['Jul 2 2016'] ) #Unxomment me
