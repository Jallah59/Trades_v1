import pandas as pd
from scipy.signal import argrelextrema
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


# import data

def get_data(file): 
    return pd.read_excel(file)

#Takes data from Datatable and covert to 2D with time and closing values
def create_line_closing_2D(data):
    out = (data[0], data[2])
    return out

def plot_line_stop(y_value):
    plt.axhline(y = y_value, color = 'r', linestyle = '-')




df = get_data('NQ.xlsx')
#np_close = df['Close']

#Find extremals on given timeframe
df['min'] = df.iloc[argrelextrema(df.Close.values, np.less_equal, order=1)[0]]['Close']
df['max'] = df.iloc[argrelextrema(df.Close.values, np.greater_equal, order=1)[0]]['Close']

print(df['min'])
#Set graph settings
#plt.ion()
plt.ylabel('Price')
plt.title('NQ price 2017-2022')
plt.scatter(df.index, df['min'], c='r')
plt.scatter(df.index, df['max'], c='g')
plt.plot(df.index, df['Close'])

plt.show()





