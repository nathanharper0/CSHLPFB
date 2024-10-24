#!/usr/bin/env python3

import sys,re,math

from Bio import SeqIO
import Bio.SeqUtils
import statistics


import sys, re
fastas=[]
with open('D_melanogaster_genomic.fna','r') as fasta:
    for sequence_record in SeqIO.parse(fasta,"fasta"):
        fastas.append(sequence_record)

print(f'contig number: {len(fastas)}')
ntcontent={'A':0,'T':0,"G":0,"C":0,'a':0,'t':0,"g":0,"c":0,"N":0}


for sequence in fastas:
    for nt in sequence:
        if nt == 'A':
            ntcontent['A']+=1
        if nt == 'T':
            ntcontent['T']+=1
        if nt == 'G':
            ntcontent['G']+=1
        if nt == 'C':
            ntcontent['C']+=1
        if nt == 'a':
            ntcontent['a']+=1
        if nt == 't':
            ntcontent['t']+=1
        if nt == 'g':
            ntcontent['g']+=1
        if nt == 'c':
            ntcontent['c']+=1
        if nt == 'N':
            ntcontent['N']+=1

print(ntcontent)
#is it faster using regex?


totalnts=0
for sequence in fastas:
    totalnts+=len(sequence.seq)
print(f'total contig length: {totalnts}')
print(f'gap proportion: {ntcontent["N"]/totalnts:.4f}')
