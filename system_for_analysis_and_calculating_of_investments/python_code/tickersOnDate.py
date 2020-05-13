# -*- coding: utf-8 -*-
"""
tickersOnDate:
this program gets from the user dates of a period and list of stocks. 
Also it asks if the user wants accumulated profit or not.
It prints the profit and the close price for every stock.
"""
import TickersProcess as tp
import urllib.request

try:
    c=input('Please enter a date you want to get profit for in a yyyy-mm-dd format:')
    o=input('Please enter a date before it in a yyyy-mm-dd format:')
    l=input('Please enter a comma separated stock list:')#test:EOD/HD,XHAN/NOA3,XHAN/PRG_UADJ
    accumulated=input('Please enter True/False for accumulating:')
    stock = l.split(",")
    for s in stock:
        print(tp.getProfitForTickerInRange(s, c, o, accumulated))
except urllib.error.HTTPError:
    print('Maybe one of the stocks does not exist or there is a problem with dates, please try again')
