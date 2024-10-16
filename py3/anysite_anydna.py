#!/usr/bin/env python3
import sys


motif = sys.argv[1]
dna_file_path = "dnaseq.txt"
with open(dna_file_path) as dna:
	sequence=dna.read()
#sequence=str(dna)

ntlocationstart=int(sequence.find(motif)+1)
ntlocationend=ntlocationstart+len(motif)-1

print(f'Motif 5\'-{motif}-3\' startPos:{ntlocationstart} endPos:{ntlocationend} in {sequence}')
