#!/usr/bin/env python3

from q1 import *

#create dnasequence objects using DNA_Sequence Class (in q1.py)
sequence1=DNA_Sequence('AAAGGTGTCCGTAGCTGC','uS5','Homo Sapiens')
sequence2=DNA_Sequence('ACCATTCGGCGATATGGA','Dhr1','Homo Sapiens')

print(f'{sequence1.sequence}:{sequence1.gene_name} from {sequence1.species_name}')
print(f'{sequence2.sequence}:{sequence2.gene_name} from {sequence2.species_name}')

print(f'{sequence1.seqLength()}')
print(f'{sequence1.nt_comp()}')
print(f'{sequence1.gc_content()}')
print(f'{sequence1.fasta_out()}')