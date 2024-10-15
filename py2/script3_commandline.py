#!/usr/bin/env python3
import sys

#workingversion:

anumber=int(sys.argv[1])

print("is your number pos/neg, greater or less than 50. If it is less than 50, is it even? If it is more than 50, is it divisible by 3?")
if anumber>=0:
	if anumber<50:
		if anumber%2==0 and anumber!=0:
			print("even and smaller than 50")
		elif anumber==0:
			print("the number is zero")
		else:
			print("it is smaller than 50 but not even")
	elif anumber>50:
		if anumber%3==0:
			print("it is larger than 50 and divisible by 3")
		else:
			print("it is larger than 50 but not divisible by 3")
	else:
		print("the number is 50")
else:
	print("the number is negative")
