# -*- coding: utf-8 -*-
"""
getFileForTicker:
this program gets from the user name of a ticker and a period of time.
It gets the information for the asked ticker and save it on a disk.
"""

import TickersProcess as tp
import urllib.request
import json
import re
from os import path

try:
    b=input('Please enter a begin date in a yyyy-mm-dd format:')
    e=input('Please enter an end date in a yyyy-mm-dd format:')
    s=input('Please enter a stock name:')#XHAN/PRG_UADJ
    f=input('Please enter a format csv or json:')
    p=input('Please enter a path you want to save the file to:')
    s1=re.sub('[/]', '',s)
    b1=re.sub('[-]', '',b)
    e1=re.sub('[-]', '',e)
    if f=='csv':
        if p=='data':#if the user wants to save the file to "data"
            tp.fetchTicker(s,b,e)#use the function
        else:#if the user wants to save the file using other path
            tp.fetchTicker(s,b,e)#firstly we save it to "data"
            #then we save it to the directory the user wants to
            df=tp.getDataForTickerInRange(s,b,e,['Open', 'Close', 'High', 'Low', 'Volume'])
            csv_data=df.to_csv(path.join(p,'{}_from{}_to{}.csv'.format(s1,b1,e1)), sep=',', encoding='utf-8')
    if f=='json':
        df=tp.getDataForTickerInRange(s,b,e,['Open', 'Close', 'High', 'Low', 'Volume'])
        js_data=df.to_json(orient='index')
        with open(path.join(p,'{}_from{}_to{}.json'.format(s1,b1,e1)), 'w') as jf:
            json.dump(js_data, jf)
except urllib.error.HTTPError:
    print('Maybe one of the stocks does not exist or there is a problem with dates, please try again')
