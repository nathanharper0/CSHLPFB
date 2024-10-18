#!/usr/bin/env python3

#initialize the empty dictionary, header and sequence lists, and a temporary sequence list
fastaDict={}
fastaHeaders=[]
fastaSeqs=[]
temp_seq=[]
#read in fasta format file
with open('Python_06.fasta','r') as fasta:  
    for line in fasta: #read line in file
        line=line.rstrip() #remove \n
        if line.find('>')==0: #if the line is a header
                if temp_seq: #and if temp_seq=true i.e. it has things in it i.e. the sequence is done
                    fullsequence=''.join(temp_seq) #join the fragments
                    fastaSeqs.append(fullsequence) #join the full sequence to fastaSeqs
                    temp_seq=[] #reset temp_seq
                fastaHeaders.append(line) #add header to fastaHeaders regardless of if temp_seq=true 
                #to deal with first header in file
        else: #if not a header, its a sequence so append the line to temp_seq
            temp_seq.append(line)
    #the final sequences left in the last sequence in temp_seq need to be joined and appended to fastaSeqs
    fullsequence=''.join(temp_seq)
    fastaSeqs.append(fullsequence)
#check contents of header and sequence lists
#print(fastaHeaders)
#print(fastaSeqs)
#Fix the formatting of the headers to be 'seq1' not '>seq1'
fastaHeaders2=[]
for x in fastaHeaders: #for each header in the headers
    fixedhead='' #make an empty string
    fixedhead=x.replace('>','') #assign fixedhead to the string in fastaHeaders[x] but replace > with 
    #nothing ''
    fastaHeaders2.append(fixedhead) #now append this new string to the new fastaHeaders2 list
#check that formatting worked
#print(fastaHeaders2)
#Now i need to populate fastaDict{}. x counts through the indices of formatted headers fastaHeaders2
#defining fastaDict key with fastaHeaders2[x] and fastaDict value with fastaSeqs[x]
for x in range(0,len(fastaHeaders2)):
    fastaDict[fastaHeaders2[x]]=fastaSeqs[x]
#print fastaDict
print(fastaDict)
