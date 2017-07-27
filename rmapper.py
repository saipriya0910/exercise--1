#!/usr/bin/python

import sys

for line in sys.stdin:
	data=line.strip().split(",")
	if len(data) == 5:
		transactionId,name,category,state,amount=data
		print state,'\t',amount
		
		
