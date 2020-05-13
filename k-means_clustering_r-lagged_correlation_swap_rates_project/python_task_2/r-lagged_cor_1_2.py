#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
question 2 a, b
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#reading data
discount = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/discount.csv", skiprows=2 )
hapoalim = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/hapoalim.csv", skiprows=2 )
leumi = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/leumi.csv", skiprows=2 )
mizrahi = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/mizrahi.csv", skiprows=2 )


#sorting by date
discount['Date'] =pd.to_datetime(discount.Date)
discount.sort_values(by=['Date'], inplace=True, ascending=True)
discount = discount.set_index(['Date'])
hapoalim['Date'] =pd.to_datetime(hapoalim.Date)
hapoalim.sort_values(by=['Date'], inplace=True, ascending=True)
hapoalim = hapoalim.set_index(['Date'])
leumi['Date'] =pd.to_datetime(leumi.Date)
leumi.sort_values(by=['Date'], inplace=True, ascending=True)
leumi = leumi.set_index(['Date'])
mizrahi['Date'] =pd.to_datetime(mizrahi.Date)
mizrahi.sort_values(by=['Date'], inplace=True, ascending=True)
mizrahi = mizrahi.set_index(['Date'])


#daily returns
discount_daily_returns = discount['Adjusted Closing Price'].pct_change().abs()
hapoalim_daily_returns = hapoalim['Adjusted Closing Price'].pct_change().abs()
leumi_daily_returns = leumi['Adjusted Closing Price'].pct_change().abs()
mizrahi_daily_returns = mizrahi['Adjusted Closing Price'].pct_change().abs()


#creating a dataframe of daily returns

all_returns = pd.concat([discount_daily_returns[::],hapoalim_daily_returns[::], leumi_daily_returns[::], mizrahi_daily_returns], axis=1, keys=['discount_dr', 'hapoalim_dr', 'leumi_dr', 'mizrahi_dr'])
print(all_returns.head())
#part A
    
def crosscorr(datax, datay, lag=0, wrap=False):
    """ Lag-N cross correlation. 
    Shifted data filled with NaNs 
    
    Parameters
    ----------
    lag : int, default 0
    datax, datay : pandas.Series objects of equal length
    Returns
    ----------
    crosscorr : float
    """
    if wrap:
        shiftedy = datay.shift(lag)
        shiftedy.iloc[:lag] = datay.iloc[-lag:].values
        return datax.corr(shiftedy)
    else: 
        return datax.corr(datay.shift(lag))

d1 = all_returns['discount_dr']
d2 = all_returns['hapoalim_dr']
d3 = all_returns['leumi_dr']
d4 = all_returns['mizrahi_dr']

m_m = [crosscorr(d3,d3, lag) for lag in range(5)]
m_d = [crosscorr(d3,d1, lag) for lag in range(5)]
m_h = [crosscorr(d3,d2, lag) for lag in range(5)]
m_l = [crosscorr(d3,d4, lag) for lag in range(5)]

lst = [m_m, m_d, m_h, m_l]
discount_lagcor = pd.DataFrame(lst, index=['mizrhi/mizrahi','mizrahi/discount', 'mizrahi/hapoalim', 'mizrahi/leumi'], columns =['r=0', 'r=1', 'r=2', 'r=3', 'r=4'])
print(discount_lagcor.head())