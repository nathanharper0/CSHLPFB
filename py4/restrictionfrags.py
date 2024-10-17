#!/usr/bin/env python3

#sequence='GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCGCTACGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGGTCATCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC'
sequence='GSDFLKJDFGAATTCDFSFHDJKFHGAATTCSDKLFJSDKLFJKSDGAATTCLSSDFSDJFS'

ecori='GAATTC'
#count total occurences of ecori (totalsites) and create list of indices for these sites (siteindices)
totalsites=0
startindex=0
siteindices=[]
#go through sequence starting looking at index 0 (startindex). if a site is found (-1 is NOT returned by find and assigned to site)
#then add 1 to total sites running total, append the index+1 of the site to siteindices, and +1 to startindex makes sure
#the next loop of find only starts looking after the last occurence of ecori
for i in range(0,len(sequence)):
	site=sequence.find(ecori,startindex)
	if site!=-1:
		startindex=site+1
		totalsites+=1
		siteindices.append(site+1)
	else:
		print(f'No sites found')
		break

#check:what is number of total sites and what does site indices look like?
#print(f'totalsites{totalsites}')
#print(f'"siteindices"{siteindices}')

#convert sequence to a list
sequence_list=list(sequence)
#go through each siteindex (in siteindices) and insert ^. after each insertion, the list becomes 1 longer so the c variable
#iterates +1 to account for the added entry in sequence_list. The carot is put in after the G in GAATCC not before because 
#siteindices were appended with +1 to start to make the first nt position 1 but doubles here as it pushes the carot to after G

c=0
for z in siteindices:
	sequence_list.insert(z+c,'^')
	c+=1

#check if the list has ^ in correct places
#print(f'{sequence_list}')

#convert back to string with ''.join()
carotsequence=''.join(sequence_list)
#checking that carotsequence is correct
#print(carotsequence)
#split carotsequence into strings contained in a list
fragments=carotsequence.split('^')
#checking whether this new list (fragments) is correct
#print(fragments)
#sort this new list by len in descending order
sortedfragments=sorted(fragments,key=len,reverse=True)
#testing the behavior 
#print(fragments)
#print(sortedfragments)
#for each fragment in sortedfragments, print fragment number (starting at 1, defined outside for), starting index in ORIGINAL
#SEQUENCE using find(frag) which looks for the string frag in sortedfragments in ORIGINAL SEQUENCE and adds 1 to start nt numbering
#at 1. End is the length of this fragment added to the index of the fragment in ORIGINAL SEQUENCE. Then print length

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



	



