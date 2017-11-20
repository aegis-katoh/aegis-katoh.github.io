# This program is written in Python3

from datetime import datetime
from datetime import timedelta

sampling_period = timedelta(seconds=0.1)
standard_time = datetime(2017, 11, 20, hour=13, minute=39, second=5, microsecond=123141)

def calc_timedelta(standard_time, sampling_period):
	current_time = datetime.now()
	dif = current_time - standard_time
	timedelta = (dif % sampling_period).total_seconds()

	return timedelta
