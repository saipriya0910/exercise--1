#!/usr/bin/python


import sys

totalsales = 0
prev_state = None

for line in sys.stdin:
	line=line.strip()
	state,sales=line.split('\t' ,1)
	sales=float(sales)
	if prev_state  == state:
		totalsales += sales

	else:
		if prev_state != None:
			print '%s\t%s' %(prev_state,totalsales)
		prev_state = state
		totalsales = sales
if prev_state:
	print '%s\t%s' %(prev_state,totalsales)
