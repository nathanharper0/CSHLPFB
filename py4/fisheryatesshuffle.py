#!/usr/bin/env python3
import random
dna=['C','G','T','T','A','G']
for swap in range(1,len(dna)):
	randomA=random.randrange(1,len(dna)-1)
	randomB=random.randrange(1,len(dna)-1)
	ntA=dna[randomA]
	ntB=dna[randomB]
	dna[randomA]=ntB
	dna[randomB]=ntA
print(dna)
