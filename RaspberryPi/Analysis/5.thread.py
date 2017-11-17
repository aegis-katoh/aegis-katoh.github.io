# This program is written in Python3

from threading import Timer

def hello():
	print("hello")

def hi():
	print("hi")

while True:
	t1 = Timer(1, hello)
	t2 = Timer(2, hi)
	t1.start()
	t2.start()
