import pandas as pd
import numpy as np
import math
# from sklearn.linear_model import LinearRegression


egyptData = pd.read_csv('C:/Users/adama/Desktop/egyptEconomy/data/egypt_economy_WorldBankData.csv')
turkeyData = pd.read_csv('C:/Users/adama/Desktop/egyptEconomy/data/turkey_Data.csv')

# egyptEconomy = egyptData[['RIR','GDP_Growth_Rate','Inflation']]

RIRmeanEG=egyptData['RIR'].mean()
GDPmeanEG=egyptData['GDP_Growth_Rate'].mean()
INFmeanEG=egyptData['Inflation'].mean()

RIRmeanTK=turkeyData['RIR'].mean()
GDPmeanTK=turkeyData['GDP_Growth_Rate'].mean()
INFmeanTK=turkeyData['Inflation'].mean()

RIRstdEG=egyptData['RIR'].std(ddof=1)
GDPstdEG=egyptData['GDP_Growth_Rate'].std(ddof=1)
INFstdEG=egyptData['Inflation'].std(ddof=1)

RIRstdTK=turkeyData['RIR'].std(ddof=1)
GDPstdTK=turkeyData['GDP_Growth_Rate'].std(ddof=1)
INFstdTK=turkeyData['Inflation'].std(ddof=1)


# Mean and Standard Deviation

print('//////////////////////////////////////////')
print('Egyptian National Economic Data 1976-2019')

print('\n Average Real Interest Rate for Egypt is %.4f with a standard deviation of %.11f' % (RIRmeanEG, RIRstdEG))
print(' Average Real Interest Rate for Turkey is %.4f with a standard deviation of %.11f' % (RIRmeanTK, RIRstdTK))

print('\n Average GDP Growth Rate for Egypt is %.4f with a standard deviation of %.11f' % (GDPmeanEG, GDPstdEG))
print(' Average GDP Growth Rate for Turkey is %.4f with a standard deviation of %.11f' % (GDPmeanTK, GDPstdTK))

print('\n Average Inflation Rate for Egypt is %.4f with a standard deviation of %.11f' % (INFmeanEG, INFstdEG))
print(' Average Inflation Rate for Turkey is %.4f with a standard deviation of %.11f' % (INFmeanTK, INFstdTK))


# Filter for outliers (2 standard deviations)

def outlierEG():
    RIRoutlierEG = egyptData[(egyptData['RIR']>=13.609244) | (egyptData['RIR']<=-7.796456)]
    GDPoutlierEG = egyptData[(egyptData['GDP_Growth_Rate']>=10.215923) | (egyptData['GDP_Growth_Rate']<=0.467463)]
    INFoutlierEG = egyptData[(egyptData['Inflation']>=24.08879) | (egyptData['Inflation']<=-0.296994)]
    print('\n These are the outlier years for Real Interest Rate:')
    print(RIRoutlierEG)
    print('\n These are the outlier years for GDP Growth Rate:')
    print(GDPoutlierEG)
    print('\n These are the outlier years for Inflation:')
    print(INFoutlierEG)

def outlierTK():
    RIRoutlierTK = turkeyData[(turkeyData['RIR']>=(RIRmeanTK + 2*RIRstdTK)) | (turkeyData['RIR']<=(RIRmeanTK - 2*RIRstdTK))]
    GDPoutlierTK = turkeyData[(turkeyData['GDP_Growth_Rate']>=(GDPmeanTK + 2*GDPmeanTK)) | (turkeyData['GDP_Growth_Rate']<=(GDPmeanTK - 2*GDPmeanTK))]
    INFoutlierTk = turkeyData[(turkeyData['Inflation']>=(INFmeanTK + 2*INFstdTK)) | (turkeyData['Inflation']<=-(INFmeanTK + 2*INFstdTK))]
    print('\n These are the outlier years for Real Interest Rate in Turkey:')
    print(RIRoutlierTK)
    print('\n These are the outlier years for GDP Growth Rate in Turkey:')
    print(GDPoutlierTK)
    print('\n These are the outlier years for Inflation in Turkey:')
    print(INFoutlierTk)

outlierEG()
outlierTK()

