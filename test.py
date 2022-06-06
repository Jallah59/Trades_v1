import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.signal import argrelextrema

# Generate a noisy AR(1) sample

np.random.seed(0)
rs = np.random.randn(200)
xs = [0]
for r in rs:
    xs.append(xs[-1] * 0.9 + r)
xs = pd.read_excel('NQ.xlsx')
xy = xs.to_numpy()
df = pd.DataFrame(xs, columns=['data'])
print(xy)
print(argrelextrema(xy, np.greater, order=5))

#df = pd.read_excel('NQ.xlsx')
#df = pd.DataFrame(dd['Date'], dd['Closing'])
n = 5  # number of points to be checked before and after

# Find local peaks

df['min'] = df.iloc[argrelextrema(df.data.values, np.less_equal,
                    order=n)[0]][0]
df['max'] = df.iloc[argrelextrema(df.data.values, np.greater_equal,
                    order=n)[0]][0]

print(df['min'])

# Plot results

plt.scatter(df.index, df['min'], c='r')
plt.scatter(df.index, df['max'], c='g')
plt.plot(df.index, df['data'])
plt.show()