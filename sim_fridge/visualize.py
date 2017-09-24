"""
Visualize number of customers vs. energy cost
2016 Gregor Ulm
"""

import pandas as pd
import numpy  as np

from sklearn import preprocessing
from matplotlib import pyplot as plt

df_1 = pd.io.parsers.read_csv("output/correlate_raw.csv",
        header=None,
        usecols=[0]
        )


df_2 = pd.io.parsers.read_csv("output/correlate_raw.csv",
        header=None,
        usecols=[1]
        )

df_1.columns=['Customers']
df_2.columns=['Energy']


def plot():
  plt.figure(figsize=(8,6))

  plt.scatter(df_1['Customers'], df_2['Energy'],
      color='green', label='input scale', alpha=0.5)

  plt.title("Customers vs Energy Consumption (both)  -- business hours")
  plt.xlabel('Customers')
  plt.ylabel('Energy')
  #plt.legend(loc='upper left')
  plt.grid()

  plt.tight_layout()

print "###"
print df_2.corrwith(df_1.Customers)
plot()
plt.show()