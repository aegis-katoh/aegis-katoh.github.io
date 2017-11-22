# This program is written in Python3

import pandas as pd
import matplotlib.pyplot as plt

logfile = "Analyse_Pulse_Signal/20171121_log.csv"

data = pd.read_csv(logfile, parse_dates=[0])

time = data.Time
rate = data.Rate

print(time, rate)

plt.plot(time, rate)
plt.savefig("graph.png")
