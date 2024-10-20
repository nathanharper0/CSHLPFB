#!/usr/bin/env python3
import sys
import re

fastafile=sys.argv[1]

seq_composition={}
seq_name=''
with open(fastafile,'r') as fasta:
    for line in fasta: #read line in file
        line=line.rstrip() #remove \n
        if line.startswith('>'): #if the line is a header
            seq_name=line[1:].split(maxsplit=1)[0]
            seq_composition[seq_name]={'A':0,'T':0,'G':0,'C':0}
        else:
            for nt in line.upper():
                seq_composition[seq_name][nt]+=1

for seq_name in seq_composition:
    print(seq_name, end='\t')
    for nt in ('A','T','G','C'):
        print(f'{nt}:{seq_composition[seq_name][nt]}\t',end='')
    print()
            