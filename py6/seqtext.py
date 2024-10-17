#!/usr/bin/env python3

#lines alternate between name and sequence so name\nseq\nname2\nseq2\nname3...
with open('Python_06.seq.txt','r') as inputseqs:
#with open('revcomptest.txt','r') as inputseqs:

    seqs={}
    for line in inputseqs:
        line=line.rstrip()
        seqname,dna=line.split()
        seqs[seqname]=dna
#print(seqs)
sequencenames=dict.keys(seqs)
print(sequencenames)
c_seqs=seqs.copy()
rc_seqs=seqs.copy()
for name in sequencenames:
    sequence=seqs[name]
    complement=sequence[::-1]
    c_seqs[name]=complement
    reversecomplement=''
    for x in range(0,len(complement)):
	    if complement[x] == "G":
		    reversecomplement += "C"
	    elif complement[x] == "C":
		    reversecomplement += "G"
	    elif complement[x] == "A":
		    reversecomplement += "T"
	    elif complement[x] == "T":
		    reversecomplement += "A"
    rc_seqs[name]=reversecomplement
	
for gene in rc_seqs:	
    print(f'>{gene} Reverse Complement:\n{rc_seqs[gene]}')
	