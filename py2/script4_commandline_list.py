#!/usr/bin/env python3
import sys

#workingversion:

threenumbers=[int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])]

print("are your numbers pos/neg, greater or less than 50. If they are less than 50, are they even? If they are more than 50, are they divisible by 3?")
for i in range(3):
	if threenumbers[i]>=0:
		if threenumbers[i]<50:
			if threenumbers[i]%2==0 and threenumbers[i]!=0:
				print(threenumbers[i])
				print("the number is even and smaller than 50")
			elif threenumbers[i]==0:
				print(threenumbers[i])
				print("the number is zero")
			else:
				print(threenumbers[i])
				print("the number is smaller than 50 but not even")
		elif threenumbers[i]>50:
			if threenumbers[i]%3==0:
				print(threenumbers[i])
				print("the number is larger than 50 and divisible by 3")
			else:
				print(threenumbers[i])
				print("the number larger than 50 but not divisible by 3")
		else:
			print(threenumbers[i])
			print("the number is 50")
	else:
		print(threenumbers[i])
		print("the number is negative")
