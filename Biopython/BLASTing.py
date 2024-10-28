#!/usr/bin/env python3

from Bio import SeqIO
import Bio.SeqUtils
import statistics
import re


import sys, re
fastas={}
descriptions=[]
with open('uniprot_sprot.fasta','r') as fasta:
    for sequence_record in SeqIO.parse(fasta,"fasta"):
        description=re.findall(r'OS=\S+\s{1}\S',sequence_record.id)
        descriptions.append(description)
        fastas[sequence_record.id]=sequence_record.seq

print(len(fastas))
print(len(descriptions))
genusspeciesseqcount={}
for species in descriptions:
    genusspeciesseqcount[species]=0
for species in genusspeciesseqcount:
    occurences=
