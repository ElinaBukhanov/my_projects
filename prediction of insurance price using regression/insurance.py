#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exploratory Data Analysis and Visualisations
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('/home/elina/Загрузки/insurance.csv')
print(df.head())

print(df.describe())

print(df.isnull().sum())#checkin for NaN

#Charges distribution
sns.set(style='darkgrid')
sns.set_palette('pastel')
f, ax = plt.subplots(1,1, figsize=(12, 8))
ax = sns.distplot(df['charges'], kde = True, color = 'm')
plt.title('Distribution of the Charges')

print('Skew coefficient:',df['charges'].skew())

#Charges distribution normalized
f, ax = plt.subplots(1, 1, figsize=(12, 8))
ax = sns.distplot(np.log(df['charges']), kde = True, color = 'g' )

print('Skew coefficient:',np.log(df['charges']).skew())

#Charges by region
charges = df['charges'].groupby(df.region).sum().sort_values(ascending = True)
f, ax = plt.subplots(1, 1, figsize=(8, 6))
ax = sns.barplot(charges.head(), charges.head().index)

#Charges by region (male/female)
f, ax = plt.subplots(1, 1, figsize=(12, 8))
ax = sns.barplot(x='region', y='charges', hue='sex', data=df, capsize=.2)

#Charges by smoker/non-smoker
f, ax = plt.subplots(1,1, figsize=(12,8))
ax = sns.barplot(x = 'region', y = 'charges', hue='smoker', data=df, capsize=.2, palette ='Paired')

#Charges by number of children
f, ax = plt.subplots(1, 1, figsize=(12, 8))
ax = sns.barplot(x='region', y='charges', hue='children', data=df, palette='Set1')

#Charges by age, BMI, children number, based on smoker/non-smoker
ax = sns.lmplot(x = 'age', y = 'charges', data=df, hue='smoker', markers=["o", "x"], palette='rocket')
ax = sns.lmplot(x = 'bmi', y = 'charges', data=df, hue='smoker', markers=["o", "x"], palette='mako')
ax = sns.lmplot(x = 'children', y = 'charges', data=df, hue='smoker', markers=["o", "x"],  palette='viridis')

#Converting objects  into categorical
df[['sex', 'smoker', 'region']] = df[['sex', 'smoker', 'region']].astype('category')
print(df.dtypes)

#Converting category into numerical using LabelEncoder
label = LabelEncoder()
label.fit(df.sex.drop_duplicates())
df.sex = label.transform(df.sex)
label.fit(df.smoker.drop_duplicates())
df.smoker = label.transform(df.smoker)
label.fit(df.region.drop_duplicates())
df.region = label.transform(df.region)
print(df.dtypes)

#Building a heatmap to understand correlations
f, ax = plt.subplots(1, 1, figsize=(10, 10))
ax = sns.heatmap(df.corr(), annot=True, cmap='Blues')



"""
Linear regression
"""

from sklearn.model_selection import train_test_split as holdout
from sklearn.linear_model import LinearRegression
from sklearn import metrics
x = df.drop(['charges'], axis = 1)
y = df['charges']
x_train, x_test, y_train, y_test = holdout(x, y, test_size=0.2, random_state=0)
Lin_reg = LinearRegression()
Lin_reg.fit(x_train, y_train)
print(Lin_reg.intercept_)
print(Lin_reg.coef_)
print(Lin_reg.score(x_test, y_test))


"""
Polynomial Regression
"""

from sklearn.preprocessing import PolynomialFeatures
x = df.drop(['charges', 'sex', 'region'], axis = 1)
y = df.charges
pol = PolynomialFeatures (degree = 2)
x_pol = pol.fit_transform(x)
x_train, x_test, y_train, y_test = holdout(x_pol, y, test_size=0.2, random_state=0)
Pol_reg = LinearRegression()
Pol_reg.fit(x_train, y_train)
y_train_pred = Pol_reg.predict(x_train)
y_test_pred = Pol_reg.predict(x_test)
print(Pol_reg.intercept_)
print(Pol_reg.coef_)
print(Pol_reg.score(x_test, y_test))

#Evaluating the performance of the algorithm
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_test_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_test_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_test_pred)))


#Predicting the charges
y_test_pred = Pol_reg.predict(x_test)
#Comparing the actual output values with the predicted values
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_test_pred})
print(df)