sFilename=input("Enter the file name: ")
try:
    fhanle=open(sFilename)
except:
    print("File not exist")
    exit()
for line in fhanle:
    line=line.rstrip()
    print(line.upper())