# -*- coding: utf-8 -*-
"""
compareTickersInRange:
This program gets from the user a period of time and a list of tickers.
It prints a table with summaries of data for each ticker.
"""
import TickersProcess as tp
import pandas as pd
import urllib.request

try:
    b=input('Please enter a begin date in a yyyy-mm-dd format:')#2018-02-20 
    e=input('Please enter an end date in a yyyy-mm-dd format:')#2018-02-27
    l=input('Please enter a comma separated stock list:')#EOD/HD,XHAN/NOA3,XHAN/PRG_UADJ
    stock = l.split(",")

    for s in stock:   
        df=tp.getDataForTickerInRange(s,b,e,['Open', 'Close', 'High', 'Low', 'Volume'])
        df['Name']=s
        df['Profit']=df.Close.iloc[0]/df.Close.iloc[-1]
        p2v=tp.getP2vForTickerInRange(s,b,e)
        a=p2v[0]
        df['Peak to Valley']=a
        df['Highest Price']=df['Close'].max()
        df['Lowest Price']=df['Close'].min()
        df['Average Price']=df['Close'].sum()/df['Close'].count()
        df['Standard deviation']=df['Close'].std()
        df_compare=df[['Name','Profit','Peak to Valley','Highest Price','Lowest Price','Average Price','Standard deviation']].copy()
        compare = df_compare.iloc[0]
        print(compare.head())
except urllib.error.HTTPError:
    print('Maybe one of the stocks does not exist, please try again')
except IndexError:
    print('There is a problem with dates, please try again')