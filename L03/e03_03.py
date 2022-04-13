try:
    fltGrade=float(input("Enter Grade:"))
except:
    fltGrade=2
if fltGrade>1 or fltGrade<0:
    print("Bad score")
    quit()
elif fltGrade>=0.9: print("A")
elif fltGrade>=0.8: print("B")
elif fltGrade>=0.7: print("C")
elif fltGrade>=0.6: print("D")
else: print("F")