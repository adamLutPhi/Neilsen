#3 Timezone Handling Demo
"""
Handling Timezones
"""
import pandas as pd

#Pandas Time Zone Information

default_date= '3/6/2016 00:00'
rng = pd.date_range( default_date , periods = 15 , freq = 'd')

print(rng)
#print( rng.timetz)

print("timezone for Naive time: ", rng.tz)

#>>> None #I'm not seeing anything (it's a naive date) [no timeone object for naive instance of time]

#Note:  in pandas, there is no Default UTC Time Zone

#The only way to add a time zone, is to do it explicitly

#creeate range

rng = pd.date_range( default_date , periods = 15 , freq = 'd', tz = 'Europe/London')

print(rng)
print("timezone for explicitly set time: ", rng.tz)


# Get Lists of timezones

from pytz import common_timezones, all_timezones # depreciated, unfortunately


print( len(common_timezones)) #433 common timezones


print(len(all_timezones) ) # 596 total timezones

# What are differences between 2 collections


# What timezones that are not Common  ?

##me: apply set theory (and venn diagram visualization ) 
## 1. make a set (out of all time-zones)

#Give me set of all items, that are not common
#target =  all - common

#Do it, regardless the (In)efficiencies

target = set(all_timezones) - set(common_timezones)


#Localizing a timestamp
#( to `localize` a timestamp` (via a timezone, externally) 
t_naive = pd.Timestamp('2016-05-05 08:15')
print(t_naive) # a naive time: just an idea of a time


#However, using tz_localize(timezone)
## Using tz_localize

#Sets the timezone into Central time, USA

t = t_naive.tz_localize(tz = 'US/Central')
print(t)

# If you want to localize
# You have to reassign

# Say my boss is in Tokyo, then I have to convert my (current) time into her timezone, first
## Using `tz_convert`
print("localized timestamp (Tokyo): \n")

#Convert: the current timezone on hand, into a Tokyo timezone

print( t.tz_convert('Asia/Tokyo') ) 

## Q. what is the difference between tz_convevrt, tz_localize ?

#Hint : try run tz_convert on a naive timestamp

#tz_convert: converts timezone
#tz_localize: sets the timestamp
"""
Q. so, if a timestamp is naive, i.e. doesn't have a
it doesn't have a timestamp (model) with it
Q2. so, how can I conver it?
try localize somwthing that has a time

but how about we try localizing a timestamp?
"""

#could not execute this line ( to convert the timezone of a naive timestamp (as naive timestamps doesn't

# have any timezones (but we could either localize and set it Automatically ) 

""" Uncomment: Try me
print( t_naive.tz_convert('Asia/Tokyo') ) # this would error out: REASON: Cannot convert timestamp to the given localized REASON: timestamp is just NAIVE
"""

#try to localize a timestamp

"""Uncomment this block
t.tz_localize(tz = 'Asia/Tokyo'); # we cannot do that , on a naive timezone [as it is timezone un-aware]

# Meanwhile, we can only convert non-naive timezones [or tz-aware Timestamps ]

"""


## Ambigous times
# Hint: use pandas: pd.Series, pd.DatetimeIndex()

"""
Leap Year,
Day Light Saving (DST)
...
"""

#You will get  with timezones, backed on daylight savings

rng = pd.date_range('2016-03-10', periods = 10, tz = 'US/Eastern')
ts = pd.Series(range(10), index =rng)
# What should we notice?

print(ts)
"""Notice:
time here is taken care of
(so you don't have to worry (about conversion , or not 
1:37:10

"""

# Now, you'll get (some) Weirdness, with timezones & DST [Day Light Savings]
"""Uncomment me:
rng = pd.date_range('2016-03-10', periods = 10, ts = 'US/Eastern')

"""
ts = pd.Series(range(10), index = rng)

# What do you notice ?
print(ts)

# For the same reason:
## You can run int (what we call) an ambigous state:

rng_hourly = pd.DatetimeIndex( ['11/06/2011 00:00', '11/06/2011 1:00','11/06/2011 2:00','11/06/2011 3:00'] )

print(rng_hourly)

# What happens if we localize?
"""
rng_hourly.tz_localize('US/central') # Erroneous input : AmbiguousTimeError

Description:
Say you've got time:

2:00 am
3:00 am
hour never existed.. cosmetically!
now: python: you have got AmbiguousTimeError , so you'd better make up some decision
(As, I don't want to make these decisions for you )

- In particular:
If we have a 'raw' timestamp, and we want to also add a timezone 'US/Central'

A. add parameter ambiguous = 'infer'
"""

# How do we deal with ambiguous time error?
"""
rng_hourly2 = rng_hourly.tz_lcoalize('US/central', ambiguous = 'infer' #2022 BUG
#BUG Name: tz_localize(ambiguous="infer") breaks on DST with missing data near DST

#issues:45905 |  Label(s):[Docs] [enhancement] [timezones]   https://github.com/pandas-dev/pandas/issues/45905

#issue: 47398 | Label(s):[enhancement] [timezones] | Status: Open :  https://github.com/pandas-dev/pandas/issues/47398

"""

#latest hack:
#note: rng_hourly == S.dt                     

"""Missing data around a DST change can break `infer` in this case return `NaT`."""  
# ---> this Except name AmbiguousTimeError outputs:  error is undefined 



def tz_localize_with_missing(S, nonexistent='shift_forward'):

    try:
        return (
            #S.dt.
            S.tz_localize(
                "Europe/London",
                ambiguous='infer',
                nonexistent=nonexistent,
            )
         
        )
    except AmbiguousTimeError: 
        return (
            S.
            dt.tz_localize(
                "Europe/London",
               # ambiguous='NaT', #<---- take this one [Reason: Does not exist, anymore]
              nonexistent=nonexistent,
            )
            .dt.tz_convert("UTC")
        )
ambiguous parameter is removed
#DEMO:
rng_hourly2 = pd.DatetimeIndex( ['11/06/2022 00:00', '11/06/2022 1:00'] )
print( tz_localize_with_missing(rng_hourly2) )

# now, pass-in our time with DST `rng_hourly`, as a parameter:
print("Output: tz_localize_with_missing(rng_hourly)")
print( tz_localize_with_missing(rng_hourly) )

##rng_hourly
print( tz_localize_with_missing(rng_hourly) )
 
print("Output: rng_hourly")
print(rng_hourly)

#Q. how to check whether this has achieved what I want?
#Look at UTC, all timezones should behave
#Convert

###rng_hourly.tz_ #uncomment

#once again
""" Do not Umcomment 
rng_hourly = rng_hourly.tz_localize('US/Central', ambigouous='infer') # Bug #reason `ambigouous` @unknown
#reason: must be: someone have deleted parameter `ambigouous`

"""





