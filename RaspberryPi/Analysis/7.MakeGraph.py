# This program is written in Python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

logfile = "Analyse_Pulse_Signal/20171121_log.csv"

data = pd.read_csv(logfile, parse_dates=[0])

time = data.Time
rate = data.Rate

print(time)

average = rate.mean()

length = len(data.index)

mean = pd.DataFrame(np.arange(length).reshape(length,1))
mean.columns=["Mean"]

for i in range(0, length):
	mean["Mean"][i] = average

print(mean)

ax = plt.subplot()
ax.plot(time, rate, time, mean)
#ax.set_xlim([time[0]], time[length-1])
plt.savefig("graph.png")
