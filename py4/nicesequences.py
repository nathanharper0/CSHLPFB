#!/usr/bin/env python3

sequences=['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
print(f'_index\n_sequencelength\n_sequence')
for seq in sequences:
	print(f'{sequences.index(seq)}\t{len(seq)}\t{seq}')
