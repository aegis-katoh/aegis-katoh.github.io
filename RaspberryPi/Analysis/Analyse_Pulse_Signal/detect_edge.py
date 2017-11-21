# This program is written in Python3

def detect_edge(present_value, previous_value):
	different = present_value - previous_value
	if (different == 1):
		edge = 1
	else:
		edge = 0

	return edge
