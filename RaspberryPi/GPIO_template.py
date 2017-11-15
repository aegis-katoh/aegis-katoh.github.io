# This program is written in Python3

# Library to use GPIO
import RPi.GPIO as GPIO
# Library to get date
from datetime import datetime
import time

# sampling frequency [Hz]
sampling_freq = 50
wait_time = 1 / sampling_freq

# date
date = datetime.now().strftime("%Y%m%d_%H:%M:%S")
logfile = date + "_log.txt"

# select GPIO.BCM or GPIO.BOARD
# GPIO.BCM is based on GPIO pin number
# GPIO.BOARD is based on Raspberry Pi's pin number
GPIO.setmode(GPIO.BCM)
# define input pin number
PIN = 10
# initial setting to use GPIO
GPIO.setup(PIN, GPIO.IN)

# open file to record log
fp = open(logfile, "w")
print("opened log file ", logfile)

i = 0
while True:
	# digit
	value = GPIO.input(PIN)
	# write digital value to log file
	fp.write( str(value) + "\n")
	print( str(i) + ":" + str(value) )
	i += 1
	time.sleep(wait_time)
