#!/usr/bin/env python3

with open('Python_06.fastq','r') as fastq:
    linetotal=0
    charactersinlinex=[]
    for line in fastq:
        charactershere=len(line)
        linetotal+=1
        charactersinlinex.append(charactershere)
    charactertotal=0
    for x in charactersinlinex:
        charactertotal+=x
print(f'Total number of lines: {linetotal}')
print(f'Total number of characters: {charactertotal}')
print(f'Average line length: {charactertotal/linetotal}')