#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 14:16:22 2020

@author: elina

"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#reading data
df = pd.read_csv('/home/elina/Документы/udemy analysis/udemy_courses.csv')
#print(df.head(10))
#print(df.columns)
#(['course_id', 'course_title', 'url', 'is_paid', 'price',
#       'num_subscribers', 'num_reviews', 'num_lectures', 'level',
#       'content_duration', 'published_timestamp', 'subject'],
#      dtype='object')

#serching for NaN and null
#print(df.isna().sum())
#print(df.isnull().sum())

#cheaking for duplicates
#duplicated_rows = df[df.duplicated()]
#print(duplicated_rows)

#deleating duplicates
df = df.drop_duplicates().reset_index(drop = True)
#print(df.info())

'''
How many of the courses are paid/free?
'''
paid = (df['is_paid'] == True).sum() 
free = (df['is_paid'] == False).sum() 
print('There are {} paid courses and {} free courses.'.format(paid, free))

#df.groupby(['is_paid']).sum().plot(kind='bar')
#df.groupby(['price'])['content_duration'].sum()[:10].plot(kind="bar")
print('_____________________')
'''
Number of the courses by subject
'''
print('Number of the courses by subject:')
print(df.subject.value_counts())
print('_____________________')

#df.subject.value_counts().plot(kind = 'bar')
'''
What are the most popular courses by subject?
'''
print('Number of subscribers by subject:')
print(df.groupby(['subject']).num_subscribers.sum())
print('_____________________')

#df.groupby(['subject']).num_subscribers.sum().plot(kind = 'barh')
'''
Which course is the most popular?
'''
print('The most popular course is:')
print(df.loc[df.num_subscribers == df.num_subscribers.max()]['course_title'])
print('_____________________')

'''
Levels
'''
#plt.figure(figsize=(10,6))
#sorted_levels = df['level'].value_counts()
#plt.pie(sorted_levels, labels = sorted_levels.index, startangle = 90,
#        counterclock = False,autopct='%1.0f%%', pctdistance=1.1, labeldistance=1.2);
#plt.axis('square')
'''
Let's look how different points (colmns) of the data are correlated.
'''
sns.heatmap(df.corr(), annot = True, fmt = '.2f', cmap = 'vlag_r', center = 0)

'''
Let's look how number of subscribers has changed year by year.
'''
#df['year'] = pd.DatetimeIndex(df['published_timestamp']).year
#sns.lineplot(data = df, x = 'year', y = 'num_subscribers')
