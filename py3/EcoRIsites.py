#!/usr/bin/env python3

dna = 'ACGGGTGGAATTCAAAGAATTCGGA'
ecorI = 'GAATTC'

ntlocationstart=int(dna.find(ecorI)+1)
ntlocationend=int(dna.find(ecorI)+6)

print(f'EcoRI startPos:{ntlocationstart} endPos:{ntlocationend}')
