# -*- coding: utf-8 -*-
"""
TickersProcess module:
operations of download, saving (on a disk)
and analysis of historical stock quotes.

"""

import pandas as pd
from os import path
from os import mkdir
import re
import urllib.request
import pathlib
"""
fetchTicker function: 
the function brings data for a stock using a stock's name and dates of tne begining
and the end of a period we are inerested in. Then the function saves it on a disk.
"""
def fetchTicker(ticker_name, from_date, to_date):
    try:
        if (path.exists('data') == False):
            mkdir('data')
        with open('api_key.txt', 'r') as my_key:
            api = my_key.read()
        url_template = "https://www.quandl.com/api/v3/datasets/{}/data.csv?start_date={}&end_date={}&api_key={}"
        url = url_template.format(ticker_name, from_date, to_date, api)
        TICKER_NAME=re.sub('[/]', '',ticker_name)
        from_DATE=re.sub('[-]', '',from_date)
        to_DATE=re.sub('[-]', '',to_date)
        tickers = pd.read_csv(url, index_col='Date', parse_dates=True)
        output_file = path.join('data','{}_from{}_to{}.csv'.format(TICKER_NAME,from_DATE,to_DATE))
        paths = pathlib.Path(output_file)
        if paths.is_file():
            print('This file already exist.')
        else:
            return(tickers.to_csv(output_file, sep=',', encoding='utf-8'))
    except urllib.error.HTTPError:
        print('Maybe one of the stocks does not exist or there is a problem with dates, please try again')
#fetchTicker('EOD/HD','2018-02-04','2018-02-09')    

"""
getDataForTickerInRange:
the function gets name of a stock, period of time and a list of information.
It returns Pandas.DataFrame object that makes a table with information we asked for.
"""
def getDataForTickerInRange(ticker_name,from_date,to_date, inf):
    try:
        with open('api_key.txt', 'r') as my_key:
            api = my_key.read()
        url_template = "https://www.quandl.com/api/v3/datasets/{}/data.csv?start_date={}&end_date={}&api_key={}"
        url = url_template.format(ticker_name, from_date, to_date, api)
        df_tickers = pd.read_csv(url, index_col='Date', parse_dates=True)
        df_tickers = df_tickers[inf].copy()
        return(df_tickers.head())
    except KeyError:
        print('Some kind of data in the inf list does not exist.')
    except urllib.error.HTTPError:
        print('Maybe one of the stocks does not exist or there is a problem with dates, please try again')
    
#print(getDataForTickerInRange('EOD/HD','2018-02-01','2018-02-06',['Open', 'Close', 'High', 'Low', 'Volume']))

"""
getProfitForTickerInRange:
the function gets name of a stock, period of time and true or false for accumulation
(depends on type of profit we want to get).
It returns profit of a stock.
"""
def getProfitForTickerInRange(ticker_name,from_date,to_date, accumulated):
    try:
        with open('api_key.txt', 'r') as my_key:
            api = my_key.read()
        url_template = "https://www.quandl.com/api/v3/datasets/{}/data.csv?start_date={}&end_date={}&api_key={}"
        url = url_template.format(ticker_name, from_date, to_date, api)
        df_tickers = pd.read_csv(url, index_col='Date', parse_dates=True)
        df_tickers['Name']=ticker_name
        if accumulated == False:
            df_tickers['Profit'] = df_tickers.Close/df_tickers.Close.shift(-1)
        else:
            df_tickers['Percents'] = ((df_tickers.Close/df_tickers.Close.shift(-1))/100+1)
            df_tickers['Profit'] = df_tickers.Percents*df_tickers.Percents.shift(-1)
        df_profit=df_tickers[['Name','Profit','Close']].copy() 
        return(df_profit.head())
    except urllib.error.HTTPError:
        print('Maybe one of the stocks does not exist or there is a problem with dates, please try again')

#print(getProfitForTickerInRange('EOD/HD','2018-02-01','2018-02-06', accumulated = False))
"""
getP2vForTickerInRange:
the function gets name of a stock and a period of time we are interested in.
It returns peak to valley value, values of a peak and of a valley 
and number of days between them.
"""
def getP2vForTickerInRange(ticker_name,from_date,to_date):
    try:
        with open('api_key.txt', 'r') as my_key:
            api = my_key.read()
        url_template = "https://www.quandl.com/api/v3/datasets/{}/data.csv?start_date={}&end_date={}&api_key={}"
        url = url_template.format(ticker_name, from_date, to_date, api)
        df_tickers = pd.read_csv(url, index_col='Date', parse_dates=True)
        #finding a peak value
        df_tickers['Peak'] = df_tickers.Close[(df_tickers.Close.shift(1) < df_tickers.Close) & (df_tickers.Close.shift(-1) < df_tickers.Close)]
        #finding a valley value
        df_tickers['Valley'] = df_tickers.Close[(df_tickers.Close.shift(1) > df_tickers.Close) & (df_tickers.Close.shift(-1) > df_tickers.Close)]
        df_tickers['Days']=df_tickers.index.date
        df_tickers['Peak'].fillna(0, inplace=True)    
        df_tickers['Valley'].fillna(0, inplace=True)
        Peak_Valley = df_tickers[['Valley', 'Peak', 'Days']].copy()
        Peak_Valley = Peak_Valley[(Peak_Valley.Valley != 0) | (Peak_Valley.Peak !=0)]
        valley = Peak_Valley[Peak_Valley.Valley != 0].iloc[0]
        peak=Peak_Valley[Peak_Valley.Peak != 0].iloc[-1]
        m_valley=valley['Valley']#getting the value
        m_peak=peak['Peak']#getting the value
        p2v=m_peak-m_valley#getting the result of peak to valley
        day_v=valley['Days']#getting a day of a valley
        day_p=peak['Days']#getting a day of a peak
        day_p2v=day_v-day_p#getting the number of days between
        return([p2v,m_valley,m_peak,day_p2v])
    except urllib.error.HTTPError:
        print('Maybe one of the stocks does not exist or there is a problem with dates, please try again')

#print(getP2vForTickerInRange('EOD/HD','2018-02-04','2018-02-20')) 

if __name__ == "__main__":
    print(getDataForTickerInRange('EOD/HD','2018-02-01','2018-02-06',['Open', 'Close', 'High', 'Low', 'Volume']))
    print(getProfitForTickerInRange('EOD/HD','2018-02-01','2018-02-06', accumulated = False))
    print(getP2vForTickerInRange('EOD/HD','2018-02-04','2018-02-20')) 