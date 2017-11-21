# -*- coding: utf-8 -*-
import time
import datetime
import pandas as pd
import matplotlib.pyplot as plt

t0=time.clock()

fig=plt.figure();

t1=time.clock()

filepath="../../data/20171003_BME280/20170925_bme280.csv"

t2=time.clock()

data = pd.read_csv(filepath, parse_dates=[0]) #1

t3=time.clock()

# print data

plt.subplots_adjust(hspace=0.3) #2

plt.subplot(3,1,1)
plt.plot(data.time, data.temperature, color='red', marker="o", markersize=4) #3
plt.legend(loc='best') #4

plt.subplot(3,1,2)
plt.plot(data.time, data.humidity, color='blue', marker="x", markersize=4)
plt.legend(loc='best')

plt.subplot(3,1,3)
plt.plot(data.time, data.pressure, color='green', marker="*", markersize=4)
plt.legend(loc='best')

t4=time.clock()

plt.savefig("graph.png")

t5=time.clock()

plt.pause(.01)

t6=time.clock()

print("prepare canvas:" + str(t1-t0) + "[s]")
print("define filepath:" + str(t2-t1) + "[s]")
print("read csv data:" + str(t3-t2) + "[s]")
print("plot graph:" + str(t4-t3) + "[s]")
print("save graph:" + str(t5-t4) + "[s]")
print("show graph:" + str(t6-t5) + "[s]")
print("total time:" + str(t6-t0) + "[s]")

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
