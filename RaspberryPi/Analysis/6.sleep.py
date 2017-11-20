# This program is written in Python3

from datetime import datetime
from datetime import timedelta
from time import sleep

test = timedelta(microseconds=100000)

t1 = datetime.now()
print("t1 : ", t1)

sleep(10.25)

t2 = datetime.now()
print("t2 : ", t2)

dif = t2 - t1
print("dif : ", dif)

an = (dif % test).total_seconds()
print("an : ", an)
