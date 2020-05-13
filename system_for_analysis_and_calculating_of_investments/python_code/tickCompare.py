"""
tickCompare:
This program gets from the user a period of time, a list of tickers and the index for 
comparison.
The program will create a graph for a comparison.
"""

import pandas as pd
import matplotlib.pyplot as plt
import TickersProcess as tp
import urllib.request

try:
    b=input('Please enter a begin date in a yyyy-mm-dd format:')
    e=input('Please enter an end date in a yyyy-mm-dd format:')
    l=input('Please enter a comma separated stock list:')#EOD/HD,XHAN/NOA3,XHAN/PRG_UADJ
    g=input('Please choose the index: Price (end of the day), Profit (daily),\
            Profit(cumulative), Min price (daily), Max price (daily):')

    stock = l.split(",")

    for s in stock:
        if g=='Price (end of the day)':
            df=tp.getDataForTickerInRange(s,b,e,['Open', 'Close', 'High', 'Low', 'Volume'])
            plt.xlabel('Date')
            plt.ylabel('Price')
            df['Close'].plot()
    
        elif g=='Profit (daily)':
            df=tp.getProfitForTickerInRange(s,b,e,accumulated=False)
            plt.xlabel('Date')
            plt.ylabel('Profit (daily)')
            df['Profit'].plot()

        elif g=='Profit (cumulative)':
            df=tp.getProfitForTickerInRange(s,b,e,accumulated=True)
            plt.xlabel('Date')
            plt.ylabel('Profit (cumulative)')
            df['Profit'].plot()

        elif g=='Min price (daily)':
            df=tp.getDataForTickerInRange(s,b,e,['Open', 'Close', 'High', 'Low', 'Volume'])
            plt.xlabel('Date')
            plt.ylabel('Min price (daily)')
            df['Low'].plot()
    
        elif g=='Max price (daily)':
            df=tp.getDataForTickerInRange(s,b,e,['Open', 'Close', 'High', 'Low', 'Volume'])
            plt.xlabel('Date')
            plt.ylabel('Max price (daily)')
            df['High'].plot()
    plt.show()
except urllib.error.HTTPError:
    print('Maybe one of the stocks does not exist or there is a problem with dates, please try again')