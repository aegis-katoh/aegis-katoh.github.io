# This program is written in Python3

# Library to use GPIO
import RPi.GPIO as GPIO
# Library to get date
from datetime import datetime

import signal
import time
import csv
from os import path

# initial setting
# sampling frequency [Hz]
sampling_freq = 5
# show interval [sec]
interval = 10

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

# start time
start_time = datetime.now().timestamp()

def sampling(arg1, arg2):
	# value now
	value_now = GPIO.input(PIN)
	# differential
	diff = value_now - value_past

	count = counter(diff)

	# product per minute
	product_rate = count / interval * 60

	value_past = value_now

def counter(self, diff):
	if (diff == 1):
		count += 1
	return count

def record(self, count, product_rate):
	# open file to record log
	if path.exists(logfile,):
		writer = csv.writer(open(logfile, "a"))
	else:
		writer = csv.writer(open(logfile, "a"))
		writer.writerow(["Time", "Count", "Rate"])

	# record time
	record_time = datetime.now().strftime("%H:%M:%S.%f")

	# write digital value to log file
	writer.writerow([record_time, count, product_rate])
	print(record_time, value_now, count, product_rate)

signal.signal(signal.SIGALRM, sampling)
signal.setitimer(signal.ITIMER_REAL, wait_time, wait_time)

while True:
	time.sleep(wait_time)
