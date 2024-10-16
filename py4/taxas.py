#!/usr/bin/env python3

taxa_string="sapiens : erectus : neanderthalensis"
print(taxa_string)
taxa_list=taxa_string.split(' : ')
print(taxa_list)
print(taxa_list[1])
sortedtaxa_list=sorted(taxa_list)
print(sortedtaxa_list)
lensorttaxa_list=sorted(taxa_list,key=len)
print(lensorttaxa_list)
