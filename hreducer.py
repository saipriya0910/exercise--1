#!/usr/bin/python


import sys

tsales=0
prev_category = None
prev_state = None

for line in sys.stdin:
	line=line.strip()
	state,category,sales = line.split('\t')
	sales=float(sales)
	if prev_category == category and prev_state == state:
		tsales += sales
	else:
		if prev_category != None and prev_state != None:
			print prev_state,'\t',prev_category,'\t',tsales
		prev_category = category
		prev_state = state
		tsales=sales
if prev_category and prev_state:
	print prev_state,'\t',prev_category,'\t',tsales

