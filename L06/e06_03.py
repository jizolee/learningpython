def count(word,find_letter):
    c=0
    for letter in word:
        if letter ==find_letter:
            c+=1
    return c

x=count("Monty Python","y")
print(x)