#!/usr/bin/env python3
import sys
import re

fastafile=sys.argv[1]

sequences={}
seq_name=''
with open(fastafile,'r') as fasta:
    for line in fasta: #read line in file
        line=line.rstrip() #remove \n
        if line.startswith('>'): #if the line is a header
            seq_name=line[1:].split(maxsplit=1)[0]
            sequences[seq_name]=''
        else:
            sequences[seq_name]+=line.upper()


for seq_name in sequences:
    print(f'{seq_name}-frame-1-codons')
    sep=' '
    for i in range(0,len(sequences[seq_name]),3):
        print(f'{sequences[seq_name][i:i+3]}',end=sep)
    print()

with open('Python_08.codons-6frames.nt','w') as newfile:
    for seq_name in sequences:
        newfile.write("seq_name-frame-1-codons\n")
        sep=' '
        for i in range(0,len(sequences[seq_name]),3):
            newfile.write(sequences[seq_name][i:i+3]+sep)
        newfile.write('\n')
        newfile.write("seq_name-frame-2-codons\n")
        sep=' '
        for i in range(1,len(sequences[seq_name]),3):
            newfile.write(sequences[seq_name][i:i+3]+sep)
        newfile.write('\n')
        newfile.write("seq_name-frame-3-codons\n")
        sep=' '
        for i in range(2,len(sequences[seq_name]),3):
            newfile.write(sequences[seq_name][i:i+3]+sep)
        newfile.write('\n')
        reversesequence=sequences[seq_name][::-1]
        reversesequencecompl=''
        for nt in range(0,len(reversesequence)):
            if reversesequence[nt] == 'C':
                reversesequencecompl+='g'
            elif reversesequence[nt] == 'G':
                reversesequencecompl+='c'
            elif reversesequence[nt] == 'T':
                reversesequencecompl+='a'
            elif reversesequence[nt] == 'A':
                reversesequencecompl+='t'
        revcompupper=reversesequencecompl.upper()
        newfile.write("seq_name-frame-4-codons\n")
        sep=' '
        for i in range(0,len(revcompupper),3):
            newfile.write(revcompupper[i:i+3]+sep)
        newfile.write('\n')
        newfile.write("seq_name-frame-5-codons\n")
        sep=' '
        for i in range(1,len(revcompupper),3):
            newfile.write(revcompupper[i:i+3]+sep)
        newfile.write('\n')
        newfile.write("seq_name-frame-6-codons\n")
        sep=' '
        for i in range(2,len(revcompupper),3):
            newfile.write(revcompupper[i:i+3]+sep)
        newfile.write('\n')