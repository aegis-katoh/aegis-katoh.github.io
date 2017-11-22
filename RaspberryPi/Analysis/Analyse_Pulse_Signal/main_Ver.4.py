# This program is written in Python3
# Author : Masazumi Katoh
# coding UTF-8

# to use Raspberry Pi's GPIO
import RPi.GPIO as GPIO
# to check whether path exists or not
from os import path
# to get date and time
from datetime import datetime
from datetime import timedelta
# to sleep
from time import sleep
# to write data to csv file
import csv
# to run function per fixed time
import signal

# sampling frequency [Hz]
sampling_rate = 5
# sampling period [sec]
sampling_period = timedelta(seconds = 1. / sampling_rate)
# save period [sec]
save_period = 10
# variable that stores digit value
present_value = 0
previous_value = 1
# counter
count = 0

# date
date = datetime.now().strftime("%Y%m%d")
# logfile's name
logfile = date + "_log.csv"

# select GPIO.BCM or GPIO.BOARD
# GPIO.BCM is based on GPIO pin number
# GPIO.BOARD is based on Raspberry Pi's pin number
GPIO.setmode(GPIO.BCM)
# define input pin number
PIN = 21
# initial setting to use GPIO
GPIO.setup(PIN, GPIO.IN)

def get_sensor_value(PIN):
	# get value of PIN number
	present_value = GPIO.input(PIN)

	return present_value

def set_previous(present_value):
	# save present value as previous value
	previous_value = present_value

	return previous_value

def detect_edge(present_value, previous_value):
	# calculate different of present value and previous value
	different = present_value - previous_value
	if (different == 1):
		edge = 1
	else:
		edge = 0

	return edge

def count_edge(edge, count):
	# edge counter
	if (edge == 1):
		count += 1

	return count

def calc_timedelta(standard_time, sampling_period):
	# calculate timedelta
	current_time = datetime.now()
	dif = current_time - standard_time
	timedelta = (dif % sampling_period).total_seconds()

	return timedelta

def calc_product_rate(count, save_period):
	# calculate product rate
	product_rate = int(count / save_period * 60)

	return product_rate

def reset_count():
	# reset counter
	count = 0

	return count

def save_to_csv(dum1, dum2):
	global logfile
	global count
	global save_period

	record_time = datetime.now().strftime("%X")
	product_rate = calc_product_rate(count, save_period)

	# open csv file to record data
	if path.exists(logfile, ):
		f = open(logfile, "a")
		writer = csv.writer(f)
	else:
		f = open(logfile, "a")
		writer = csv.writer(f)
		writer.writerow(["Time", "Count", "Rate"])

	# record data
	writer.writerow([record_time, count, product_rate])
	# close csv file
	f.close()

	count = reset_count()

# get standard time
standard_time = datetime.now()

# function to run function per fixed time
signal.signal(signal.SIGALRM, save_to_csv)
signal.setitimer(signal.ITIMER_REAL, 1, save_period)

while True:
	previous_value = set_previous(present_value)
	present_value = get_sensor_value(PIN)
	edge = detect_edge(present_value, previous_value)
	count = count_edge(edge, count)
	# print(datetime.now().strftime("%H:%M:%S.%f"), count, edge)
	wait_time = sampling_period.total_seconds() - calc_timedelta(standard_time, sampling_period)
	sleep(wait_time)
