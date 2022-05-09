

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
    count[word[1]] = count.get(word[1],0) + 1

#Count max number of email.
email_max=None
for email_name in count.keys():
    if email_max==None or email_max < count[email_name]:
        email_max=count[email_name]
        name=email_name
print(name,email_max)