#!/usr/bin/env python3

import sys,re

hit_files=[]
hits_list=[]
fields=['query id','subject id','% identity','alignment length','mismatches','gap opens','q. start','q.end','s.start','s.end','evalue','bit score']
for hit_file in sys.argv[1:]:
    with open(hit_file, 'r') as results:
        for line in results:
            line=line.rstrip()
            if line.startswith('#'):
                continue
            hit_data=dict(zip(fields,line.split('\t'))) 
            hit_data['file']=hit_file
            hits_list.append(hit_data)
            break #only want the top hit so stop after 1
#print(hits_list)
print(f'_matrix_name''\n''_% identity''\n''_alignment length''\n''_evalue')
for entry in hits_list:
    print('\t'.join([entry[x] for x in ('file','% identity','alignment length','evalue')]))