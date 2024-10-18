#!/usr/bin/env python3
import re

headerlines=[]
headers=[]
with open('Python_07.fasta', 'r') as fasta:
    linenumber=1
    for line in fasta:
        line=line.rstrip()
        if re.search(r'>',line):
            headerlines.append(linenumber)
            headers.append(line)    
        linenumber+=1
with open('Python_07.fasta', 'r') as fasta:
    for line in fasta:
        line=line.rstrip()
        for match in re.finditer(r">(\S+)\s(.+)",line):
            print(f'id:{match.group(1)} desc:{match.group(2)}')

        #if re.search(r'>',line):
            #headerlines.append(linenumber)
            #eaders.append(line)    
#print(headerlines)
#print(headers)

#headers2=[]
#or x in headers: #for each header in the headers
    #fixedhead='' #make an empty string
    #fixedhead=x.replace('>','') #assign fixedhead to the string in fastaHeaders[x] but replace > with 
    #nothing ''
    #headers2.append(fixedhead) #now append this new string to the new fastaHeaders2 list
#print(headers2)
for x in headers:
    for (seqname,seqDesc) in re.findall(r">(\S+)\s(\*$)",x):
        print(f'id:{seqname} desc:{seqDesc}')