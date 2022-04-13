fltGrade=input("Enter Grade:")
try:
    fltGrade=float(fltGrade)
except:
    fltGrade=-1
def computegrade(grade):
    if grade>=0.9: x="A"
    elif grade>=0.8: x="B"
    elif grade>=0.7: x="C"
    elif grade>=0.6: x="D"
    else: x="F"
    return x
if fltGrade>1 or fltGrade<0:
    print("Bad score")
else:
    print(computegrade(fltGrade))



