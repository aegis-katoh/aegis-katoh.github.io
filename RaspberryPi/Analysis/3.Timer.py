import signal
import time
from datetime import datetime

def task(arg1, arg2):
    print(datetime.now())

signal.signal(signal.SIGALRM, task)
signal.setitimer(signal.ITIMER_REAL, 0.1, 0.1)

while True:
	time.sleep(0.01)
