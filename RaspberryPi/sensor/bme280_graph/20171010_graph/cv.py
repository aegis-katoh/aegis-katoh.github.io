# -*- coding: utf-8 -*-
import datetime
import cv2 
import pandas as pd
import matplotlib.pyplot as plt

DATA_DIR = '/mnt/wind/'     #データ保存用のディレクトリを設定

record_datetime = datetime.datetime.now()  #現在の日時と時刻を取得
record_file_name = record_datetime.strftime('%Y%m%d')

data = pd.read_csv(record_file_name+"_bme280.csv", index_col='time')
df_tmp = data.iloc[:, [0]]
df_tmp.plot()
plt.savefig(DATA_DIR+record_file_name+"_tmp.png")
df_pressure= data.iloc[:, [1]]
df_pressure.plot()
plt.savefig(DATA_DIR+record_file_name+"_pressure.png")
df_humid = data.iloc[:, [2]]
df_humid.plot()
plt.savefig(DATA_DIR+record_file_name+"_humid.png")
#plt.show()

img1=cv2.imread(DATA_DIR+record_file_name+"_tmp.png")
img2=cv2.imread(DATA_DIR+record_file_name+"_pressure.png")
img3=cv2.imread(DATA_DIR+record_file_name+"_humid.png")

img5=cv2.vconcat([img1,img2])
img6=cv2.vconcat([img5,img3])

cv2.imwrite(DATA_DIR+record_file_name+"_data.png",img6)
