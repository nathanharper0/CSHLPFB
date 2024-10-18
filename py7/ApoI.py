#!/usr/bin/env python3
import re
#initialize the empty dictionary, header and sequence lists, and a temporary sequence list

#read in fasta format file
#with open('Python_07_ApoI.fasta','r') as fasta:
    #previousline='' 
    #for line in fasta:
        #line=line.rstrip()
        #if line.find('>')==1:
            #continue
        #else:
            #nts=previousline+line
            #for motif in re.findall(r'[R]AATT[Y]',nts)
            ####This strategy will double count . I can do it if i keep appending to new string until next > (new sequence) and then work with entire thing
sequencefrags=[]
with open('Python_07_ApoI.fasta', 'r') as fasta:
    for line in fasta:
        line = line.rstrip()
        if re.search('>', line):
            continue
        else:
              sequencefrags.append(line)
sequence=''.join(sequencefrags)
occurences=re.findall(r'[AG]AATT[CT]',sequence)
print(occurences)
#physical cut site is R^AATTY so string index 1 in list
#using re.sub
occurencescut=[]
for x in occurences:
    sitelist=list(x)
    sitelist.insert(1,'^')
    site=''.join(sitelist)
    occurencescut.append(site)
print(occurencescut)

for x in range(0,len(occurencescut)-1):
    sequencecut=re.sub(r'[AG]AATT[CT]',occurencescut[x],sequence)
print(sequencecut)


fragments=sequencecut.split('^')
#checking whether this new list (fragments) is correct
print(fragments)
#sort this new list by len in descending order
sortedfragments=sorted(fragments,key=len,reverse=True)
#testing the behavior 
print(sortedfragments)
#for each fragment in sortedfragments, print fragment number (starting at 1, defined outside for), starting index in ORIGINAL
#SEQUENCE using find(frag) which looks for the string frag in sortedfragments in ORIGINAL SEQUENCE and adds 1 to start nt numbering
#at 1. End is the length of this fragment added to the index of the fragment in ORIGINAL SEQUENCE. Then print length
#sortedfragments=sortedfragments.rstrip()

fragnumber=1
for frag in sortedfragments:
	print(f'Fragment Number: {fragnumber}')
	print(f'Start: {sequence.find(frag)+1}')
	print(f'End: {sequence.find(frag)+len(frag)}')
	print(f'Length: {len(frag)}')
	fragnumber +=1

#restart fragnumber at 1 so that fragment 1 above is same as fragment 1 below:

fragnumber=1

#heading for gel

print(f'agarosegel')

#go through sorted fragments, printing length in nt
for frag in sortedfragments:
	print(f'Fragment {fragnumber}: {len(frag)}nt')
	fragnumber+=1