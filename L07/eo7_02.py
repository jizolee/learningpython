sFilename=input("Enter the file name: ")
try:
    fhanle=open(sFilename)
except:
    print("File not exist")
    exit()
fsum=0
icount=0
for line in fhanle:
    #print(line.find("X-DSPAM-Confidence:"))
    if line.startswith("X-DSPAM-Confidence:")== True:
        fsum+=float(line[-7:])
        icount+=1
print("Average:",fsum/icount)

