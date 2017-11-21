# This program is written in Python3

import signal
import time
from datetime import datetime

i=0

def test(dum1, dum2):
	global i
	i += 1
	print(datetime.now(), i)

signal.signal(signal.SIGALRM, test)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
	if (i % 10 == 0):
		print("yes!")
	time.sleep(0.1)
