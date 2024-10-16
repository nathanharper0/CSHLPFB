#!/usr/bin/env python3
import sys


dna = 'ACGGGTGGAATTCAAAGAATTCGGA'
motif = sys.argv[1]

ntlocationstart=int(dna.find(motif)+1)
ntlocationend=ntlocationstart+len(motif)-1

print(f'Motif 5\'-{motif}-3\' startPos:{ntlocationstart} endPos:{ntlocationend}')
