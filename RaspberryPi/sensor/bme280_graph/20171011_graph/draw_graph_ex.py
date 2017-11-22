# -*- coding: utf-8 -*-
import datetime
import pandas as pd
import matplotlib.pyplot as plt

fig=plt.figure();

filepath="../../data/20171003_BME280/20170925_bme280.csv"

data = pd.read_csv(filepath, parse_dates=[0]) #1

print data

plt.subplots_adjust(hspace=0.3) #2

plt.figure(figsize=(16,9))

plt.subplot(3,1,1)
plt.plot(data.time, data.temperature, color='red') #3
plt.ylabel('temperature [deg]', x=-1)

plt.subplot(3,1,2)
plt.plot(data.time, data.humidity, color='blue')
plt.ylabel('humidity [%]', x=-1)

plt.subplot(3,1,3)
plt.plot(data.time, data.pressure, color='green')
plt.ylabel('pressure [hPa]', x=-1)


plt.savefig("graph.png")

plt.show()



########## 参考文献 ##########
# 1. 日付がたでファイルを読み込み
# http://nehan.io/blog/python-data-transform/id-20
# 
# 2. subplotグラフ間の余白の設定
# http://ailaby.com/subplots_adjust/
# 
# 3. マーカーの設定
# http://www.maroon.dti.ne.jp/koten-kairo/works/fft/Section_PythonGraph/python_graph5.html
# 
# 4. 凡例の位置を自動で適切な場所に設置
# http://whitecat-student.hatenablog.com/entry/2017/02/27/215842
#
# 5. 
#
#############################
