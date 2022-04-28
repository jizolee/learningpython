romeo=open('romeo.txt')
"""unique_letter=[]
for line in romeo:
    line1=line.split()
    for j in line1:
        if j in unique_letter: continue
        unique_letter.append(j)
unique_letter.sort()
print(unique_letter)
print(len(unique_letter))"""
# Another solution from web
# Better use read()
romeo1=romeo.read()
words = romeo1.split()

unique_letter=list()
for j in words:
    if j not in unique_letter:
        unique_letter.append(j)
unique_letter.sort()
print(unique_letter)