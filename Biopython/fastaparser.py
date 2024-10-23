#!/usr/bin/env python3

from Bio import SeqIO
import Bio.SeqUtils
import statistics


import sys, re
fastas={}
with open('Python_08.fasta','r') as fasta:
    for sequence_record in SeqIO.parse(fasta,"fasta"):
        fastas[sequence_record.id]=sequence_record.seq

#total number of sequences is len(fastas)
#total number of nucleotides:
total_nts=0
for sequence in fastas:
    total_nts+=len(fastas[sequence])
    average_length=total_nts/len(fastas)



shortest_length=average_length
longest_length=average_length
for sequence in fastas:
    #shortest length
    if len(fastas[sequence])>shortest_length:
        continue
    else:
        shortest_length=len(fastas[sequence])
for sequence in fastas:
    #longest length
    if len(fastas[sequence])>longest_length:
        longest_length=len(fastas[sequence])
    else:
        continue
#GC counter
gc_contents=[]
for sequence in fastas:
    gc_contents.append(Bio.SeqUtils.gc_fraction(sequence_record.seq))
average_gc=statistics.mean(gc_contents)


print(f'sequence count: {len(fastas)}')
print(f'total number of nucleotides:{total_nts}')
print(f'avg len: {average_length:.1f}')
print(f'shortest len: {shortest_length}')
print(f'longest len: {longest_length}')
print(f'avg GC content: {average_gc:.2f}')
print(f'lowest GC content: {min(gc_contents):.2f}')
print(f'highest GC content: {max(gc_contents):.2f}')


