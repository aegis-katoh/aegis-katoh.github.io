# This program is written in Python3

import RPi.GPIO as GPIO
from os import path
from datetime import datetime
from datetime import timedelta
from time import sleep
import csv
import signal

# sampling frequency [Hz]
sampling_rate = 5
sampling_period = timedelta(seconds = 1. / sampling_rate)
#print(sampling_period)
# save period [sec]
save_period = 10
present_value = 0
previous_value = 1
count = 0

# date
date = datetime.now().strftime("%Y%m%d")
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
	present_value = GPIO.input(PIN)

	return present_value

def set_previous(present_value):
	previous_value = present_value

	return previous_value

def detect_edge(present_value, previous_value):
	different = present_value - previous_value
	if (different == 1):
		edge = 1
	else:
		edge = 0

	return edge

def count_edge(edge, count):
	if (edge == 1):
		count += 1

	return count

def calc_timedelta(standard_time, sampling_period):
	current_time = datetime.now()
	dif = current_time - standard_time
#	print(standard_time)
#	print(current_time, dif)
	timedelta = (dif % sampling_period).total_seconds()

	return timedelta

def calc_product_rate(count, save_period):
	product_rate = count / save_period * 60

	return product_rate

def reset_count():
	count = 0

	return count

def save_to_csv(dum1, dum2):
	global logfile
	global count
	global save_period

	if path.exists(logfile, ):
		writer = csv.writer(open(logfile, "a"))
	else:
		writer = csv.writer(open(logfile, "a"))
		writer.writerow(["Time", "Count", "Rate"])

	record_time = datetime.now().strftime("%H:%M:%S")
	product_rate = calc_product_rate(count, save_period)
	writer.writerow([record_time, count, product_rate])

	count = reset_count()

standard_time = datetime.now()

signal.signal(signal.SIGALRM, save_to_csv)
signal.setitimer(signal.ITIMER_REAL, 1, save_period)

while True:
	previous_value = set_previous(present_value)
	present_value = get_sensor_value(PIN)
	edge = detect_edge(present_value, previous_value)
	count = count_edge(edge, count)
	print(datetime.now().strftime("%H:%M:%S.%f"), count, edge)
	wait_time = sampling_period.total_seconds() - calc_timedelta(standard_time, sampling_period)
#	print(wait_time)
	sleep(wait_time)
