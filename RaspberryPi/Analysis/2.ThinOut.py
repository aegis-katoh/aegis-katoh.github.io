# This program is written in Python3

# Library to get particular row
import linecache
# Library to get date
from datetime import datetime

import csv
from os import path

# date
date = datetime.now().strftime("%Y%m%d")
logfile = date + "_log.csv"
thinfile = date + "_thin.csv"

length = len(open(logfile).readlines())
latest = linecache.getline(logfile, length)
print(latest)

# open file
if path.exists(thinfile,):
	writer = csv.writer(open(thinfile, "a"))
else:
	writer = csv.writer(open(thinfile, "a"))
	writer.writerow(["Time", "Count", "Rate"])

writer.writerow([str(latest)])

