#!/usr/bin/env python3
import sys

value1=int(sys.argv[1])
value2=int(sys.argv[2])
for number in range(value1,value2+1):
	if number%2!=0:
		print(number)
