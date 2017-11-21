# This program is written in Python3

import PRi.GPOP as GPIO

def get_sensor_value(PIN):
	present_value = GPIO.input(PIN)

	return present_value
