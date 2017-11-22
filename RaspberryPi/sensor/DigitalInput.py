# This program is written in Python3

# Library to use GPIO
import RPi.GPIO as GPIO
import time

# define input pin number
PIN = 21
# select GPIO.BCM or GPIO.BOARD
# GPIO.BCM is based on GPIO pin number
# GPIO.BOARD is based on Raspberry Pi's pin number
GPIO.setmode(GPIO.BCM)
# initial setting to use GPIO
GPIO.setup(PIN, GPIO.IN)

print("start\n")

# open file to record log
fp = open("log.txt", "w")

# variable for numbering of data
i = 0

try:
	# wait control + c
	while True:
		#t1 = time.clock()
		# digit
		value = GPIO.input(PIN)
		# write digital value to log file
		fp.write( str(value) + "\n")
		print( str(i) + ":" + str(value) )
		i += 1
		time.sleep(1/100)
		#t2 = time.clock()
		#print( str(t2 - t1) + "[s]")
except(KeyboardInterrupt):
		fp.close()
		GPIO.cleanup()
		print("end\n")
