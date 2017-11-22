# This program is written in Python3

from datetime import datetime

t1 = datetime.now()

import pandas as pd
t8 = datetime.now()
import numpy as np
t9 = datetime.now()
import matplotlib.pyplot as plt

t2 = datetime.now()

filepath = "Analyse_Pulse_Signal/20171121_log.csv"

data = pd.read_csv(filepath, parse_dates=[0])

t3 = datetime.now()

average = data.Rate.mean()
length = len(data.index)

t4 = datetime.now()

mean = pd.DataFrame(np.arange(length).reshape(length,1))
mean.columns=["Mean"]

t5 = datetime.now()

for i in range(0, length):
	mean["Mean"][i] = average

t6 = datetime.now()

plt.figure(figsize=(9,6))
plt.plot(data.Time, data.Rate, label = "product rate")
plt.plot(data.Time, mean, label = "mean")
plt.legend(loc="best")
plt.title("product rate of MACHINE")
plt.xlabel("time")
plt.ylabel("product rate [product per minute]")
#ax.set_xlim([time[0]], time[length-1])
plt.savefig("graph.png")

t7 = datetime.now()

print("import libraries : ", t2 - t1)
print("import pandas : ", t8 - t1)
print("import numpy", t9 - t8)
print("import matplotlib.pyplot", t2 - t9)
print("read csv : ", t3 - t2)
print("average : ", t4 - t3)
print("create pandas data frame : ", t5 - t4)
print("for loop : ", t6 - t5)
print("plot : ", t7 - t6)
print("total : ", t7 - t1)
