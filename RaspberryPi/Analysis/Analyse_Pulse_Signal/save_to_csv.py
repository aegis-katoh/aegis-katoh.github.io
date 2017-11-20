# This program is written in Python3

from os import path
import csv
from datetime import datetime

def save_to_csv(logfile, count, product_rate):
	if path.exists(logfile, ):
		writer = csv.writer(open(logfile, "a"))
	else:
		writer = csv.writer(open(logfile, "a"))
		writer.writeroe(["Time", "Count", "Rate"])

	record_time = datetime.now().strftime("%H:%M:%S.%f")

	writer.writerow([record_time, count, product_rate])
