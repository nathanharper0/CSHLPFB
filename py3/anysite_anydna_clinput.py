#!/usr/bin/env python3
import sys

#argument 1 is string motif
#argument 2 is text file name
#check if inputs are present, else give error
if len(sys.argv)==2:
#set up
	motif = sys.argv[1]
	dna_file = sys.argv[2]
	with open(dna_file,'r') as dna:
		sequence=dna.read()
#find first location
	ntlocationstart=int(sequence.find(motif)+1)
	ntlocationend=ntlocationstart+len(motif)-1
#print first location
	print(f'Motif 5\'-{motif}-3\' startPos:{ntlocationstart} endPos:{ntlocationend} in {sys.argv[2]}')
else:
#print error
	print(f'Please use as anysite_anydna_clinput.py motifstringtosearchfor textfiletosearchagainst')
