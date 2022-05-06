import re
import numpy as np

list_number=list()
while True:
    n= input("Enter number:")
    if n=='done': break
    else:
        try:
            list_number.append(float(n))
        except Exception as e:
            print(f'Error {e}')
print(f'Maximum: {max(list_number)}')
print(f'Manimum: {min(list_number)}')
