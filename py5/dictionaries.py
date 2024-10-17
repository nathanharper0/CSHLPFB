#!/usr/bin/env python3
import sys
#make dictionary of cool things
print('#####book######')
cool_dict={'book':'dune','song':'baki','tree':'oak','organism':'s.cerevisiae'}
#print cool book
print(cool_dict['book'])
print('######bookasvariable#####')
#assigning the cool book to a new variable and using that to print
favorite_thing=cool_dict['book']
print(favorite_thing)
print('######organism#####')
#you can reassign this favorite_thing variable to another thing in cool_dict to change what is printed
favorite_thing=cool_dict['organism']
print(favorite_thing)
print('######allvaluesindict#####')
#printing all values (cool things) in cool_dict
for thing in cool_dict:
       print(cool_dict[thing])
print('######take key input from cl and print value at that key#####')
#take an argument from cl and print the value of that key
favorite_thing=sys.argv[1]
print(f'{cool_dict[favorite_thing]}')
print('######what are the options (keys) to choose from#####')
#lets print all of the keys to see what is in the dictionary
print(f'all keys:')
for key in cool_dict:
        print(key)
print('######change value of organism via input()#####')
#lets change organism using user input (input())
print('Enter your favorite organism:')
neworganism=input()
cool_dict['organism']=neworganism
print('#####lets double check it worked by printing value of organism######')
#confirm it worked via print
print(cool_dict['organism'])
print('######use input to input a new value for the key in favorite_thing (the argument from cl)#####')
newvalue=input()
cool_dict[favorite_thing]=newvalue
print('####confirm it worked######')
print(f'your new favorite {favorite_thing} is {cool_dict[favorite_thing]}')


