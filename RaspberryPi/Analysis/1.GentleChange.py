# This program is written in Python3

# Library to use GPIO
import RPi.GPIO as GPIO
# Library to get date
from datetime import datetime

import time
import csv
from os import path

# sampling frequency [Hz]
sampling_freq = 5
wait_time = 1. / sampling_freq
value_now = 0
value_past = 1
count = 0

# date
date = datetime.now().strftime("%Y%m%d")
logfile = date + "_log.csv"

# select GPIO.BCM or GPIO.BOARD
# GPIO.BCM is based on GPIO pin number
# GPIO.BOARD is based on Raspberry Pi's pin number
GPIO.setmode(GPIO.BCM)
# define input pin number
PIN = 10
# initial setting to use GPIO
GPIO.setup(PIN, GPIO.IN)

# open file to record log
if path.exists(logfile,):
	writer = csv.writer(open(logfile, "a"))
else:
	writer = csv.writer(open(logfile, "a"))
	writer.writerow(["Time", "Switch", "Count", "Rate"])

# start time
start_time = datetime.now().timestamp()

while True:
	# record time
	record_time = datetime.now().strftime("%H:%M:%S")
	# digit
	value_now = GPIO.input(PIN)
	# differential
	diff = value_now - value_past

	if (diff == 1):
		count += 1

	# time to calclate differential
	now_time = datetime.now().timestamp()

	# product per minute
	product_rate = count / (now_time - start_time) * 60

	value_past = value_now

	# write digital value to log file
	writer.writerow([record_time, value_now, count, product_rate])
	print(record_time, value_now, count, product_rate)
	time.sleep(wait_time)
