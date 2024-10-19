#!/usr/bin/env python3
import re
import sys

inputenzname=sys.argv[1]
inputfastafile=sys.argv[2]

#make dictionary of IUPAC nts and their corresponding options:
baseDict={}
with open('iupaccodes.txt','r') as code:
    for line in code:
            line=line.rstrip()
            iupac,base=line.split()
            baseDict[iupac] = base
print(baseDict)
#make dictionary of enzymes and their cut sites
linenumber=1
enzymeDict={}
with open('bionet.txt','r') as enzcut:
    for line in enzcut:
        if linenumber>10:
            #print(line)
            line=line.rstrip()
            name=re.search(r'(\S+)\s?\S*\s{2,}(\S*)',line)
            enzymename=name.group(1)
            enzymetarget=name.group(2)
            enzymeDict[enzymename] = enzymetarget
        else:
            linenumber+=1
            continue

print(enzymeDict)
print(inputenzname)
print(inputfastafile)
sequencefrags=[]
with open(inputfastafile,'r') as inputfasta:
    for line in inputfasta:
        line = line.rstrip()
        if re.search('>', line):
            continue
        else:
              sequencefrags.append(line)
    sequence=''.join(sequencefrags)
    #print(sequence)
    if enzymeDict[inputenzname]: #if enzyme is in dictionary
        enzymetemp=str(enzymeDict[inputenzname])
        enzymetargetnocarot=enzymetemp.replace('^','')
        enzymetemplist=list(enzymetargetnocarot)
        translatedtarget=[]
        for i in enzymetemplist:
            translatedtarget.append(baseDict[i])
            #translatedtarget[i]=baseDict[enzymetargetnocarot[]]
        translatedtargetstr=']['.join(translatedtarget)
        #print(translatedtargetstr)
        translatedtargetstr2='['+translatedtargetstr+']'
        #print(enzymetargetnocarot)
        #print(translatedtargetstr2)
        if re.search(translatedtargetstr2,sequence): #if there is a cut site in the fasta
            occurences=[]
            occurences=re.findall(translatedtargetstr2,sequence)
            #print(occurences)
            #in original enzymeDict, where is cut site?
            originalsite=str(enzymeDict[inputenzname])
            cutsiteindex=originalsite.index('^')
            #using the cutsiteindex, modify each occurance
            occurencescut=[]
            for x in occurences:
                if originalsite.index('^'):
                    sitelist=list(x)
                    sitelist.insert(cutsiteindex,'^')
                else:
                    sitelist=list(x)
                    sitelist.insert(0,'^')
                    print(f'No cut site in dictionary. Using start of motif')
                site=''.join(sitelist)
                occurencescut.append(site)
            #print(occurencescut)
        #putbackin original sequence
            for x in range(0,len(occurencescut)-1):
                sequencecut=re.sub(translatedtargetstr2,occurencescut[x],sequence)
            print(f'This is the cut sequence:{sequencecut}')
            ###########
            fragments=sequencecut.split('^')
#checking whether this new list (fragments) is correct
            print(f'Number of fragments: {len(fragments)}')
            print(f'Fragment sequences:{fragments}')
            print(f'Fragments sequences sorted:{sorted(fragments,key=len,reverse=True)}')



#sort this new list by len in descending order
            #sortedfragments=sorted(fragments,key=len,reverse=True)
#testing the behavior 
            #print(sortedfragments)
#for each fragment in sortedfragments, print fragment number (starting at 1, defined outside for), starting index in ORIGINAL
#SEQUENCE using find(frag) which looks for the string frag in sortedfragments in ORIGINAL SEQUENCE and adds 1 to start nt numbering
#at 1. End is the length of this fragment added to the index of the fragment in ORIGINAL SEQUENCE. Then print length
#sortedfragments=sortedfragments.rstrip()
            #print(f'The number of fragments:{len(fragments)}')
            #fragnumber=1
           # for frag in sortedfragments:
                #print(f'Fragment Number: {fragnumber}')
	            #print(f'Fragment Number: {fragnumber}')
                #print(f'Start: {sequence.find(frag)+1}')
                #print(f'End: {sequence.find(frag)+len(frag)}')
                #print(f'Length: {len(frag)}')
                #fragnumber +=1
            ###########
        #else:
            #print('no cut sites found for this dna')
    #else:
        #print('Enzyme not found in dictionary') 
              
