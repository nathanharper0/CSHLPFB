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
        descriptions.append(re.search(r"OS=.+OX",sequence_record.id))
        fastas[sequence_record.id]=sequence_record.seq

print(len(fastas))

for id in fastas:
    