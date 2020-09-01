import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.dates as dates

egyptData = pd.read_csv('C:/Users/adama/Desktop/egyptEconomy/data/egypt_economy_WorldBankData.csv')

egypt_interest = egyptData[['GDP_Growth_Rate']]
time = egyptData[['Year']]

x_values = time
y_values = egypt_interest

new_x = dates.datestr2num(x_values)

plt.xlabel('Date')
plt.ylabel("Annual Real Interest Rates")
plt.title("Egypt's Real Interest Rates, 1976-2019")

plt.plot_date(new_x, y_values, fmt='-', tz=None, xdate=True)

plt.legend()

plt.show()