#!/usr/bin/env python3

import re
import sys
import argparse

dna = 'GAGADKFJKLDFJLKDSFJKLDSJFKLSDJFKSDJFSDJFIIEJFKLDNFKLDSJFDKLSFJSKDJFKLSDFkFSDFDSFDSFDSFDSFDSDFSDFSDFDSFDSFDSFDFSDFFDSFDSFSFDDSDSFSDFDSFFDSFDSFDSFDSFDSFDSFDSFDSFDSFDSFSDFDSFDSFDSFDSFDSFDSFDSFDSFDSFDSFSDFSDFSDFKLDSKLFJ'

dna2 = 'GAGADKFJKLDFJLKDSFJK\nLDSJFKLSDJFKSDJFSDJFIIEJFKLDNFKL\nDSJFDKLSFJSKDJFKLSDFkFSDFDSFDSFDSFDSFDSDFSDFSDFDSFDSFDSFDFSDFFDSFDSFSFDDSDSFSDFDSFFDSFDSFDSFDSFDSFDSFDSFDSFDSFDSFSDFDSFDSFDSFDSFDSFDSFDSFDSFDSFDSFSDFSDFSDFKLDSKLFJ'



def ntsixty(seq):
    interval=60
    newseq=''
    for x in range(0,len(seq),interval):
        if x+interval < len(seq):
            newseq+=seq[x:x+interval]+'\n'
        else:
            newseq+=seq[x:len(seq)]
    return newseq

#print(ntsixty(dna))

#same strategy but prepare a new sequence first by splitting and joining seq on \n to remove them then
#passing that into the same text "wrapper"
def ntsixtynewlinesinterval(seq,interval):
    newseq=''
    tempseqlist=seq.split('\n')
    newseqnowrap=''.join(tempseqlist)
    for x in range(0,len(newseqnowrap),interval):
        if x+interval < len(seq):
            newseq+=newseqnowrap[x:x+interval]+'\n'
        else:
            newseq+=seq[x:len(newseqnowrap)]
    return newseq

def GCcontent(seq):
    upperseq=seq.upper()
    gccount=0
    for nt in seq:
        if nt=='G' or 'C':
            gccount+=1
    gccontent=gccount/len(seq)
    return gccontent

#print(ntsixty(dna2)) #first func doesnt work with newline chars
#print(ntsixtynewlinesinterval(dna2,70)) #second one does work

#using argparse and cl arguments

parser=argparse.ArgumentParser(description='takes a .fasta and a value for number of characters to wrap. returns a string')
parser.add_argument("fasta",help='fasta file')
parser.add_argument("value",type=int,help='value of characters to wrap')
args=parser.parse_args()
seq=args.fasta
interval=args.value

def ntsixtynewlinesinterval(seq,interval): #take fasta and interval from command line
    newseq=''
    tempseqlist=seq.split('\n')
    newseqnowrap=''.join(tempseqlist)
    for x in range(0,len(newseqnowrap),interval):
        if x+interval < len(seq):
            newseq+=newseqnowrap[x:x+interval]+'\n'
        else:
            newseq+=seq[x:len(newseqnowrap)]
    return newseq

#print(ntsixtynewlinesinterval(dna,60))
#print(ntsixtynewlinesinterval(dna2,60))

####DO STUFF######
inputfasta=open(seq,'r')
outfile=open('testfile_output.fasta','w')
sequence=''
for line in inputfasta:
    line=line.rstrip()
    if line.startswith('>'):
        if sequence:
            outfile.write(f'{ntsixtynewlinesinterval(sequence,interval)}\n')
            sequence=''
        outfile.write(f'{ntsixtynewlinesinterval(line,interval)}\n')
    else:
        sequence+=line
outfile.write(ntsixtynewlinesinterval(sequence,interval))
