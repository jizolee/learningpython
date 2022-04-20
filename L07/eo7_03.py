sFilename=input("Enter the file name: ")
try:
    fhanle=open(sFilename)
except:
    if sFilename=="na na boo boo": print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else: print("File not exist")
    exit()
icount=0
for line in fhanle:
    if line.startswith(" "):
        line.rstrip().rsplit()
        icount+=1

print("There was ", icount," lines in this file")