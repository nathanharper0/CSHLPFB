#!/usr/bin/env python3
import re
string=''
with open('Python_07_nobody.txt',"r") as text:
    for line in text:
        #line=line.rstrip() counting or not counting new line chars
        string+=line

list=[]
iterator=re.finditer(r'Nobody',string)
for match in iterator:
    list.append(match.start())

print(list)
#print(list)
with open('Python_07_nobody.txt',"r") as text, open('Michael.txt','w') as newpoem:
    for line in text:
        newpoem.write(re.sub('Nobody','Michael',line))

