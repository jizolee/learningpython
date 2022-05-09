import pandas as pd
import matplotlib.pyplot as plt

filename = input('Enter filename: ')
#Open the file
try:
    mail = open(filename)
except Exception as e:
    print(f'Found a error: {e}')


#Counting 
count=dict()
for line in mail:
    word=line.split()
    if len(word) == 0 or word[0]!='From': continue
    count[word[1]] = count.get(word[1],0) + 1

#print result:
print(count)