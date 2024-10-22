#!/usr/bin/env python3
import sys

class DNA_Sequence(object):
    def __init__(self, sequence, gene_name, species_name):
        self.sequence=sequence
        self.gene_name=gene_name
        self.species_name=species_name


    def seqLength(self):
        return len(self.sequence)
    
    def nt_comp(self):
        nts={}
        for nt in self.sequence:
            if nt in nts:
                nts[nt]+=1
            else:
                nts[nt]=1
        return nts
    
    def gc_content(self):
        gc=0
        seq_upper=self.sequence.upper()
        print(seq_upper)
        for nt in seq_upper:
            if nt == 'C' or nt == 'G':
                gc+=1
        #print(gc)
        return gc/len(self.sequence)
    
    def fasta_out(self):
        elements=['>']
        elements.append(self.gene_name+' ')
        elements.append(self.species_name+'\n')
        elements.append(self.sequence+'\n')
        fasta=''.join(elements)
        return fasta




def main():
    sys.exit(0)  # always good practice to indicate worked ok!



if __name__ == '__main__':
    main()