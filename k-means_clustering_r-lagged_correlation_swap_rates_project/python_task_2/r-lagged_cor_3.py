#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
question 2 gimmel
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#reading data
big = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/big.csv", skiprows=2 )
hapoalim = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/hapoalim.csv", skiprows=2 )
bezeq = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/bezeq.csv", skiprows=2 )
teva = pd.read_csv(r"/home/elina/Документы/sadnat mumhim/stocks/teva.csv", skiprows=2 )


#sorting by date
big['Date'] =pd.to_datetime(big.Date)
big.sort_values(by=['Date'], inplace=True, ascending=True)
big = big.set_index(['Date'])
hapoalim['Date'] =pd.to_datetime(hapoalim.Date)
hapoalim.sort_values(by=['Date'], inplace=True, ascending=True)
hapoalim = hapoalim.set_index(['Date'])
bezeq['Date'] =pd.to_datetime(bezeq.Date)
bezeq.sort_values(by=['Date'], inplace=True, ascending=True)
bezeq = bezeq.set_index(['Date'])
teva['Date'] =pd.to_datetime(teva.Date)
teva.sort_values(by=['Date'], inplace=True, ascending=True)
teva = teva.set_index(['Date'])


#daily returns
big_daily_returns = big['Adjusted Closing Price'].pct_change().abs()
hapoalim_daily_returns = hapoalim['Adjusted Closing Price'].pct_change().abs()
bezeq_daily_returns = bezeq['Adjusted Closing Price'].pct_change().abs()
teva_daily_returns = teva['Adjusted Closing Price'].pct_change().abs()

#creating a dataframe of daily returns

all_returns = pd.concat([big_daily_returns[::],hapoalim_daily_returns[::], bezeq_daily_returns[::], teva_daily_returns], axis=1, keys=['big_dr', 'hapoalim_dr', 'bezeq_dr', 'teva_dr'])
#print(all_returns.head())


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

d1 = all_returns['big_dr']
d2 = all_returns['hapoalim_dr']
d3 = all_returns['bezeq_dr']
d4 = all_returns['teva_dr']

t_t = [crosscorr(d4,d4, lag) for lag in range(5)]
t_b = [crosscorr(d4,d1, lag) for lag in range(5)]
t_h = [crosscorr(d4,d2, lag) for lag in range(5)]
t_bzq = [crosscorr(d4,d3, lag) for lag in range(5)]


lst = [t_t, t_b, t_h, t_bzq]
discount_lagcor = pd.DataFrame(lst, index=['teva/teva','teva/big', 'teva/hapoalim', 'teva/bezeq'], columns =['r=0', 'r=1', 'r=2', 'r=3', 'r=4'])
print(discount_lagcor.head())