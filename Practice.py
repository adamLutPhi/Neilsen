import  matplotlib.pylab
import numpy as np
import pandas as pd
import datetime

import matplotlib.pyplot as plt

#import pandas.io.data as pdio #?
#import pandas.io as pdio
import pandas as pd

import yfinance as yf
def downloadTicker(tickerName,start_date,end_date):
    #initiate DataFrame 
    prices = pd.DataFrame()
    for ticker in tickers:
        prices[ticker] = yf.download(ticker,start_date,end_date)

    return pd.DataFrame(  prices) # woun't work as expected (exceed 1D Dimension 

def downloadTickerPrices(tickerName,start_date,end_date):
    #initiate DataFrame 
    open_price = pd.DataFrame();
    high_price = pd.DataFrame();
    low_price = pd.DataFrame();
    adjClose_price = pd.DataFrame();
    volume_price = pd.DataFrame();
    
    for ticker in tickers:
                
        open_price[ticker] = yf.download(ticker,start_date,end_date)['Open']
        high_price[ticker] = yf.download(ticker,start_date,end_date)['High']
        low_price[ticker] = yf.download(ticker,start_date,end_date)['Low']
        adjClose_price[ticker] = yf.download(ticker,start_date,end_date)['Adj Close']
        volume_price[ticker] = yf.download(ticker,start_date,end_date)['Volume']

    return  pd.DataFrame({'prices':[open_price, high_price, low_price,adjClose_price,
                                    volume_price ]})

def downloadTickerAdjClose(tickerName,start_date,end_date):
    #initiate DataFrame 

    adjClose_price = pd.DataFrame();
    
    for ticker in tickers:
        
        adjClose_price[ticker] = yf.download(ticker,start_date,end_date)['Adj Close']

    return  pd.DataFrame(adjClose_price)
tickers = ["AAPL"]

    
# appl  = yf.Ticker("APPL")
startingDate ='2010-1-1' #  '2019-08-01'
endingDate = '2013-1-27' # '2020-05-01'
start = pd.Timestamp(startingDate)
end = pd.Timestamp(endingDate)

aapl =  downloadTickerPrices("AAPL",startingDate, endingDate)

print(type(aapl))
# aapl = downloadTicker("AAPL", startingDate, endingDate)
print(aapl.head() )
#aapl.get_shares_full(start=start, end=end)
#aapl.history(start=start, end=end)

start_date = datetime.datetime.today() - datetime.timedelta(360)
end_date = datetime.datetime.today()
close_price = pd.DataFrame()


#f = web.DataReader('F', 'yahoo', start, end)

# Let's find some time series data

#import pandas.io.data as web

startingDate ='2010-1-1' #  '2019-08-01'
endingDate = '2013-1-27' # '2020-05-01'
start =  pd.Timestamp(startingDate)
end = pd.Timestamp(endingDate)

tickerName =  "AAPL" 

# Call function, download data , for ticker "AAPL"
data = yf.download(tickerName ,start=startingDate ,end= endingDate)

#or Intraday - source: https://github.com/rbhatia46/Fetching-Financial-Data/blob/master/yfinance.ipynb
#data = yf.download('RELIANCE.NS',period='1mo',interval='5m')
print("data.head()")
print(data.head())


#Another, simpler way of getting Ohlcv [con: unable to cherry-pick itemd from OHLCV basket]
def read_ohlcv(ticker, start_date, end_date):
    
    ohlcv_data = {}

    for ticker in tickers:
        ohlcv_data[ticker] = yf.download(ticker,start_date,end_date)


    return ohlcv_data
ohlcv_data = read_ohlcv('AAPL', startingDate, endingDate)   
print("another way: ohlcv:\n")
print(ohlcv_data )

#plot the high, low of July August 2012
##slicing?

#say, I care about Hight and Low (to compare and contrast):
res = data['2012-07': '2012-08'][['High', 'Low']].plot()
plt.show()

#Stability of variance: Is the variance of the trading volume relatively stable over time?
#apply a rolling window 

r = data.rolling(50).var()['Volume'].plot()
plt.show()

r = data.rolling(200).var()['Volume'].plot()
plt.show()

#what if I go the other way
#try: change from 2 into 3

#window small: means looking at Daily data 
r = data.rolling(3).var()['Volume'].plot()
plt.show() #wow, this looks supper jagged (me: looks more like a home-made anomaly detection) 

# Thus, my answer depends purely on how I am going to look at this

"""Takeaway: In TimeSeries,
Always think in
1. what are you doing ? 
2. Why are you doing that?
Optional [the Best]:
3. with some Domain Knowledge

"""
#cross-ref: survival function (shock)

r = data.expanding().var()['Volume'].plot()
plt.show()

# Is the expanding window variance stable, over-time ?
"""
#As a Statistician: the exapnding window function can be your friend (careful, though)
"""
# On how many days did the stock close ( higher than it opened)? 
"""
#Hint: check .tshift)_ in the pandas docs
"""

print( data.head() ) 




print( len( data[data.Close > data.Open] ) ) # 381 - is that useful (by itself?)

#We're interested in timeSeries

# Did the `up` dats become more or less frequent over time ?
# do a rolling windo (say 25) , create a new column 'DayGain' [Close - Open] to store new info in
# then , apply a custom lambda
data['DayGain'] = data.Close - data.Open # calculate the difference

#Also interested on a statistics on that difference
#note: this is an array (in np) - not a scalar value 
data.rolling( window = 25)['DayGain'].apply(lambda x: len([x_i for x_i in x if x_i > 0 ])/len(x)).plot()
"""trating an array
1. look at the length of dayGain: len(...) over the toal length
2. find days, where gain is greater than 0 (profitable, positive, ...) 
"""
plt.show()#plot last

"""looks like a year 1 finance timeseries examplw
with possible
1. mean
2. cyclical
3. seasonal
... elements

"""
##different window size  = 50 (double the size)
data.rolling( window = 25*2)['DayGain'].apply(lambda x: len([x_i for x_i in x if x_i > 0 ])/len(x)).plot()

plt.show()

# Data
# Doesn't have to be : datetime index
# It can be just a column
# then , we could run the same lambda function periodically [Event-Driven]

# looks smoother (loss of detail (and/or Noise) )

## how about an expanding window?
#Note: expanding does NOT Take a window (me: does it auto adjust? ) 
data.expanding( )['DayGain'].apply(lambda x: len([x_i for x_i in x if x_i > 0 ])/len(x)).plot()

plt.show()# itn't not bery clear if we are positive or not

#Stock-oriented

# Compute Plot mean monthly High Value (of the stock )
"""
rolling(window), expanding() , resample()
"""
#choose resample pick 'M' for monthly
print( data.resample('M').mean()['High'].plot() )
plt.show()

##what if
## discarded 'High'
#Disclaimer: not as good (as previous one)
#data.resample('M').mean().plot()
#plt.show()
"""all means are displayed
lookes non-standard
"""

# Variance of Differenced Volume
##difference
#Relation (yesterday, today) [ me: co-relation?]
"""functions
asfrequency()
resample()
window()
rolling()
expanding()
shift()
for the example:
1. shift the Volume,  first .shift()
"""

volume = data.Volume
volume_lagged  = data.Volume.shift()
diffed_volume = volume - volume_lagged

diffed_volume.rolling(window = 20 ).var().plot()
# shift is also called: last
# maybe it's called anti-last ?!
"""Sometimes, differencing helps bringing the time-series
Making it less variable, more `stationary`
Personal Opintion: Unsure that is the case, for Volume
"""
plt.show()

#Volume Difference
#1. differentiate the Volume 
volume_lagged = data.Volume.diff()
diffed_volume = volume - volume_lagged
diffed_volume.rolling(window = 20 ).var().plot()
plt.show()

#Q. Does the Lagged Time-Series Correlate with itself ?
# Yes, Auto-correlation

"""
1. get Volume, nad Volume's shift
2. make them as a DateFrame pd.DataFrame
3. Take the correlation of that DateFrame .corr()
"""

res = pd.DataFrame({'real' : data.Volume, 'lagged' : data.Volume.shift()} ).corr()
print(res) # displayed as a 2x2 Confusion matrix , of real, & lagged
# correlation of interest : corr(real, lagged) = 0.657975
"""
65.7975% similar with yesterday's data
or it's 34.2025% different from yesterday
"""

 
