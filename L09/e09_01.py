import os
import re

fhand=open('words.txt')
dict_word=dict()
for line in fhand:
    for word in line.split():
        dict_word[word]=dict_word.get(word,0)+1

check = input("Input word you want to check: ")       
print( dict_word)