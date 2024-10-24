#!/usr/bin/env python3

import sys,re,math

from Bio import SeqIO
import Bio.SeqUtils
import statistics


import sys, re
fastas=[]
with open('ecoli_0.25.contigs.fasta','r') as fasta:
    for sequence_record in SeqIO.parse(fasta,"fasta"):
        fastas.append(sequence_record)

print(f'contig number: {len(fastas)}')
shortestcontig=len(fastas[0])
longestcontig=len(fastas[0])
for sequence in fastas:
    if len(sequence.seq) < shortestcontig:
        shortestcontig=len(sequence.seq)
    else:
        continue
for sequence in fastas:
    if len(sequence.seq) > longestcontig:
        longestcontig=len(sequence.seq)
    else:
        continue
#print(len(sequence.seq))
print(f'shortest contig length: {shortestcontig}')
print(f'longest contig length: {longestcontig}')
totalnts=0
for sequence in fastas:
    totalnts+=len(sequence.seq)
print(f'total contig length: {totalnts}')

#N50 size:
#sort by len(sequence.seq)
sortedcontigs=sorted(fastas,key=len,reverse=True)
running_sum=0
marker=totalnts/2
contigcount=0
for read in sortedcontigs:
    running_sum+=len(read)
    contigcount+=1
    if running_sum>=marker:
        N50=len(read)
        break

print(f'N50: {N50}')
print(f'L50: {contigcount}')










