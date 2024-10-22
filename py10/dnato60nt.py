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

print(ntsixty(dna))

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

print(ntsixty(dna2)) #first func doesnt work with newline chars
print(ntsixtynewlinesinterval(dna2,70)) #second one does work

#using argparse and cl arguments
import argparse
parser=argparse.ArgumentParser(description='takes a .fasta and a value for number of characters to wrap. returns a string')
parser.add_argument("fasta",help='fasta file')
parser.add_argument("value",type=int,help='value of characters to wrap')
args=parser.parse_args()

def ntsixtynewlinesintervalcl(seq,interval): #take fasta and interval from command line
    seq=args.fasta
    seq=args.value
    newseq=''
    tempseqlist=seq.split('\n')
    newseqnowrap=''.join(tempseqlist)
    for x in range(0,len(newseqnowrap),interval):
        if x+interval < len(seq):
            newseq+=newseqnowrap[x:x+interval]+'\n'
        else:
            newseq+=seq[x:len(newseqnowrap)]
    return newseq

print(ntsixtynewlinesintervalcl(dna))
print(ntsixtynewlinesintervalcl(dna2)