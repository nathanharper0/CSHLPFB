#!/usr/bin/env python3



#if anumber%2!=0:
	#print("negative")
#elif anumber==0:
	#print("zero")
#elif anumber%2==0:
	#if anumber<50:
		#print("it is an even number that is less than 50")

#workingversion:

anumber=50

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
