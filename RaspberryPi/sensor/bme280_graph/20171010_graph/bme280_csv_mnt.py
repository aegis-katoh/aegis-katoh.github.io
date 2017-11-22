#coding: utf-8

#import lib
import smbus
import datetime
import csv
import os.path

#set instance
bus_number  = 1
i2c_address = 0x76
DATA_DIR = '/mnt/wind/'     #データ保存用のディレクトリを設定
bus = smbus.SMBus(bus_number)

digT = []
digP = []
digH = []

t_fine = 0.0


def writeReg(reg_address, data):
	bus.write_byte_data(i2c_address,reg_address,data)

def get_calib_param():
	calib = []
	
	for i in range (0x88,0x9F+1):
		calib.append(bus.read_byte_data(i2c_address,i))
	calib.append(bus.read_byte_data(i2c_address,0xA1))
	for i in range (0xE1,0xE7+1):
		calib.append(bus.read_byte_data(i2c_address,i))

	digT.append((calib[1] << 8) | calib[0])
	digT.append((calib[3] << 8) | calib[2])
	digT.append((calib[5] << 8) | calib[4])
	digP.append((calib[7] << 8) | calib[6])
	digP.append((calib[9] << 8) | calib[8])
	digP.append((calib[11]<< 8) | calib[10])
	digP.append((calib[13]<< 8) | calib[12])
	digP.append((calib[15]<< 8) | calib[14])
	digP.append((calib[17]<< 8) | calib[16])
	digP.append((calib[19]<< 8) | calib[18])
	digP.append((calib[21]<< 8) | calib[20])
	digP.append((calib[23]<< 8) | calib[22])
	digH.append( calib[24] )
	digH.append((calib[26]<< 8) | calib[25])
	digH.append( calib[27] )
	digH.append((calib[28]<< 4) | (0x0F & calib[29]))
	digH.append((calib[30]<< 4) | ((calib[29] >> 4) & 0x0F))
	digH.append( calib[31] )
	#fixed get param
	#T2-T3
	for i in range(1,3):
		if digT[i] & 0x8000:
			digT[i] = (-digT[i] ^ 0xFFFF) + 1
	#P2-P9
	for i in range(1,9):
		if digP[i] & 0x8000:
			digP[i] = (-digP[i] ^ 0xFFFF) + 1
	#H2,H4,H5
	for i in [1,3,4]:
		if digH[i] & 0x8000:
			digH[i] = (-digH[i] ^ 0xFFFF) + 1  

def readData():
	#get record_time and date
	record_datetime = datetime.datetime.now()  #現在の日時と時刻を取得
	record_file_name = record_datetime.strftime('%Y%m%d')+'_bme280.csv'
	record_time = record_datetime.strftime('%X')   #時刻文字列を生成
	
	#get data
	data = []
	
	for i in range (0xF7, 0xF7+8):
		data.append(bus.read_byte_data(i2c_address,i))
	pres_raw = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
	temp_raw = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)
	hum_raw  = (data[6] << 8)  |  data[7]
	
	T=compensate_T(temp_raw)   #温度データの取得
	P=compensate_P(pres_raw)   #気圧データの取得
	H=compensate_H(hum_raw)    #湿度データの取得
	
	#record data
	if os.path.exists(DATA_DIR+record_file_name,):
		writer = csv.writer(open(DATA_DIR+record_file_name,'ab'))   #アペンドモード
		writer.writerow([record_time,T,P,H])		              #時刻、温度、気圧、湿度を記録
	else:
		writer = csv.writer(open(DATA_DIR+record_file_name,'ab'))   #アペンドモード
		writer.writerow(['time','temperature','pressure','humidity'])
		writer.writerow([record_time,T,P,H])		              #時刻、温度、気圧、湿度を記録



def compensate_P(adc_P):
	global  t_fine
	pressure = 0.0
	
	v1 = (t_fine / 2.0) - 64000.0
	v2 = (((v1 / 4.0) * (v1 / 4.0)) / 2048) * digP[5]
	v2 = v2 + ((v1 * digP[4]) * 2.0)
	v2 = (v2 / 4.0) + (digP[3] * 65536.0)
	v1 = (((digP[2] * (((v1 / 4.0) * (v1 / 4.0)) / 8192)) / 8)  + ((digP[1] * v1) / 2.0)) / 262144
	v1 = ((32768 + v1) * digP[0]) / 32768
	
	if v1 == 0:
		return 0
	pressure = ((1048576 - adc_P) - (v2 / 4096)) * 3125
	pressure = (pressure * 2.0) / v1
	v1 = (digP[8] * (((pressure / 8.0) * (pressure / 8.0)) / 8192.0)) / 4096
	v2 = ((pressure / 4.0) * digP[7]) / 8192.0
	pressure = pressure + ((v1 + v2 + digP[6]) / 16.0)  

	print "pressure : %7.2f hPa" % (pressure/100)
	return pressure/100

def compensate_T(adc_T):
	global t_fine
	v1 = (adc_T / 16384.0 - digT[0] / 1024.0) * digT[1]
	v2 = (adc_T / 131072.0 - digT[0] / 8192.0) * (adc_T / 131072.0 - digT[0] / 8192.0) * digT[2]
	t_fine = v1 + v2
	temperature = t_fine / 5120.0
	print "temp : %-6.2f ℃" % (temperature) 
	return temperature

def compensate_H(adc_H):
	global t_fine
	var_h = t_fine - 76800.0
	if var_h != 0:
		var_h = (adc_H - (digH[3] * 64.0 + digH[4]/16384.0 * var_h)) * (digH[1] / 65536.0 * (1.0 + digH[5] / 67108864.0 * var_h * (1.0 + digH[2] / 67108864.0 * var_h)))
	else:
		return 0
	var_h = var_h * (1.0 - digH[0] * var_h / 524288.0)
	if var_h > 100.0:
		var_h = 100.0
	elif var_h < 0.0:
		var_h = 0.0
	print "hum : %6.2f ％" % (var_h)
	return var_h


def setup():
	#changed settting to indoor navigation
	osrs_t = 1			#Temperature oversampling x 1
	osrs_p = 5			#Pressure oversampling x 16
	osrs_h = 2			#Humidity oversampling x 2
	mode   = 3			#Normal mode
	t_sb   = 0			#Tstandby 0.5ms
	filter = 4			#Filter 16 
	spi3w_en = 0			#3-wire SPI Disable

	ctrl_meas_reg = (osrs_t << 5) | (osrs_p << 2) | mode
	config_reg    = (t_sb << 5) | (filter << 2) | spi3w_en
	ctrl_hum_reg  = osrs_h

	writeReg(0xF2,ctrl_hum_reg)
	writeReg(0xF4,ctrl_meas_reg)
	writeReg(0xF5,config_reg)


setup()
get_calib_param()


if __name__ == '__main__':
	try:
		readData()
	except KeyboardInterrupt:
		pass





