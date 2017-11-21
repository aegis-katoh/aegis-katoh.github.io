# -*- coding: utf-8 -*-
import datetime
import pandas as pd
import matplotlib.pyplot as plt

filepath="../data/20171003_BME280/20170925_bme280.csv"

data = pd.read_csv(filepath, index_col='time')
df_tmp = data.iloc[:, [0]]
df_tmp.plot()
plt.savefig("tmp.png")
df_pressure= data.iloc[:, [1]]
df_pressure.plot()
plt.savefig("pressure.png")
df_humid = data.iloc[:, [2]]
df_humid.plot()
plt.savefig("humid.png")
plt.show()
