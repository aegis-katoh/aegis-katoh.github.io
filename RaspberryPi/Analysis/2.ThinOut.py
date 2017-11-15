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

# get number of log file
line = len(open(logfile).readlines())

# get latest line
latest = linecache.getline(logfile, line)
print(latest)

# open file
writer = csv.writer(open(thinfile, "a"))

# set label
if not path.exists(thinfile,):
	writer.writerow(["Time", "Count", "Rate"])




