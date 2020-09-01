import pandas as pd
import numpy as np
import math
# from sklearn.linear_model import LinearRegression


egyptData = pd.read_csv('C:/Users/adama/Desktop/egyptEconomy/data/egypt_economy_WorldBankData.csv')

# egyptEconomy = egyptData[['RIR','GDP_Growth_Rate','Inflation']]

RIRmean=egyptData['RIR'].mean()
GDPmean=egyptData['GDP_Growth_Rate'].mean()
INFmean=egyptData['Inflation'].mean()

RIRstd=egyptData['RIR'].std(ddof=1)
GDPstd=egyptData['GDP_Growth_Rate'].std(ddof=1)
INFstd=egyptData['Inflation'].std(ddof=1)

# Mean and Standard Deviation

print('Egyptian National Economic Data 1976-2019')

print('\n The average Annual Real Interest Rate is %.4f' % RIRmean)
print('...with a standard deviation of %.11f' % RIRstd)

print('\n The average Annual GDP Growth Rate is %.4f' % GDPmean)
print('...with a standard deviation of %.11f' % GDPstd)

print('\n The average Annual Inflation Rate is %.4f' % INFmean)
print('...with a standard deviation of %.11f' % INFstd)

# Filter for outliers (2 standard deviations)

def outlier():
    RIRoutlier = egyptData[(egyptData['RIR']>=13.609244) | (egyptData['RIR']<=-7.796456)]
    GDPoutlier = egyptData[(egyptData['GDP_Growth_Rate']>=10.215923) | (egyptData['GDP_Growth_Rate']<=0.467463)]
    INFoutlier = egyptData[(egyptData['Inflation']>=24.08879) | (egyptData['Inflation']<=-0.296994)]
    print('\n These are the outlier years for Real Interest Rate:')
    print(RIRoutlier)
    print('\n These are the outlier years for GDP Growth Rate:')
    print(GDPoutlier)
    print('\n These are the outlier years for Inflation:')
    print(INFoutlier)

outlier()

