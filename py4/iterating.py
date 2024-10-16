#!usr/bin/env python3

numbers=[101,2,15,22,95,33,2,27,72,15,52]
for num in numbers:
	mod=num%2
	if mod==0:
		print(num)
numbers.sort()
totaleven=0
totalodd=0
for num in numbers:
	print(num)
	if num%2==0:
		totaleven=totaleven+num
	else:
		totalodd=totalodd+num
print(f'Sum of even numbers: {totaleven}\nSum of odd numbers: {totalodd}')
