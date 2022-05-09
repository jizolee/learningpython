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
    if len(word)==0 or word[0]!='From': continue
    domain=word[1].split("@")                            #split email adress to sender and domain.
    if domain[1] not in count:
        count[domain[1]]=1
    else:
        count[domain[1]]+=1

print(count)

