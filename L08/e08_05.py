import pandas as pd
import numpy as np

filename = input('Enter filename: ')
try:
    mail = open(filename)
except Exception as e:
    print(f'Found a error: {e}')
finally:
    print("Check you file")

count=0
for line in mail:
    word=line.split()
    if len(word)==0 or word[0]!='From': continue
    print(word[1])
    count+=1

print(f'There were {count} lines in the file with From as the first word')