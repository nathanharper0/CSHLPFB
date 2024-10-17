#!/usr/bin/env python3

with open("Python_06.txt","r") as poem, open("Python_06_uc.txt","w") as ucpoem:
    for line in poem:
        line = line.rstrip()
        print(line.upper())
        ucpoem.write(f'{line.upper()}\n')