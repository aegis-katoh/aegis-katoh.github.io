# This program is written in Python3

import PRi.GPOP as GPIO
from os import path
from datetime import datetime
from datetime import timedelta
from time import sleep
import csv


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
	timedelta = (dif % sampling_period).total_seconds()

	return timedelta

def calc_product_rate(count, interval):
	product_rate = count / interval * 60

	return calc_product

def save_to_csv(logfile, count, product_rate):
	if path.exists(logfile, ):
		writer = csv.writer(open(logfile, "a"))
	else:
		writer = csv.writer(open(logfile, "a"))
		writer.writeroe(["Time", "Count", "Rate"])

	record_time = datetime.now().strftime("%H:%M:%S.%f")

	writer.writerow([record_time, count, product_rate])

def reset_count():
	global count
	count = 0

# Main program
initial_setting()

standard_time = datetime.now()

signal.signal(signal.SIGALRM, get_sensor_value)
signal.setitimer(signal.ITIMER_REAL, save_period, save_period)

while True:
	previous_value = set_previous(present_value)
	present_value = get_sensor_value(PIN)
	edge = detect_edge(present_value, previous_value)
	count = count_edge(edge, count)
	wait_time = calc_timedelta(standard_time, sampling_period)
	sleep(wait_time)
