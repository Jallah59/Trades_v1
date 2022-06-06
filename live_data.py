from ast import Or
from cgitb import text
from operator import truediv
from unicodedata import numeric
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.signal import argrelextrema
import numpy as np
from matplotlib import style
import pandas as pd
import time

#Style and create plot
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


def calculate_extremal(dt):
    return dt.iloc[argrelextrema(dt.Close.values, np.less_equal, order=3)[0]]['Close'], dt.iloc[argrelextrema(dt.Close.values, np.greater_equal, order=3)[0]]['Close']  


#Function for animating, iterates i times
def animate(i):
    #There is no stop function and stop order will move weird at times. This can easily be fixex by adding a function that only updates when you get a higher low, will do this later.
    order = False
    #Clear plot
    ax1.clear()
    df = pd.read_csv("live_data.csv", sep=";")

    #enter position at index 713 just for simplicity, greater than is just used to remove an error will fix this later
    if len(df['Close']) >= 713:
        order = True

    
    #Find extremals on given timeframe
    df['min'] = df.iloc[argrelextrema(df.Close.values, np.less_equal, order=3)[0]]['Close']
    df['max'] = df.iloc[argrelextrema(df.Close.values, np.greater_equal, order=3)[0]]['Close']  
    df_calc_high = df['max']
    df_calc_high.dropna(inplace=True)
    df_calc_keys = df_calc_high.keys()

    prev_high = df_calc_high[df_calc_keys[len(df_calc_keys)-1]]

    df_calc_low = df['min']
    df_calc_low.dropna(inplace=True)
    df_calc_keys = df_calc_low.keys()

    prev_low = df_calc_low[df_calc_keys[len(df_calc_keys)-1]]


    #if in a position
    if order == True:
        #Entry marked in blue, stop in red
        ax1.axhline(df['Close'][712], linewidth = 0.3, c='b')
        ax1.axhline(prev_low-50, linewidth = 0.5, c='r') 


    ax1.scatter(df.index, df['min'], c='r')
    ax1.scatter(df.index, df['max'], c='g')
    ax1.plot(df.index, df['Close'], linewidth = 0.5)
    

#Run animation to figure = fig with function animate
ani = animation.FuncAnimation(fig, animate, interval=1)

plt.show()