# This program is written in Python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filepath = "Analyse_Pulse_Signal/20171121_log.csv"

data = pd.read_csv(filepath, parse_dates=[0])

average = rate.mean()
length = len(data.index)

mean = pd.DataFrame(np.arange(length).reshape(length,1))
mean.columns=["Mean"]

for i in range(0, length):
	mean["Mean"][i] = average

ax = plt.subplot()
ax.plot(data.Time, data.Rate, data.Time, mean)
ax.legend(loc="best")
#ax.set_xlim([time[0]], time[length-1])
plt.savefig("graph.png")
