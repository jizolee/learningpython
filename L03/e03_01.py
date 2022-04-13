fltHour=float(input("Enter Hours: "))
fltRate=float(input("Enter rate: "))
if fltHour>40:
    fltOverHour=fltHour-40 #Calculate Overtime Hours
    fltOverRate=fltRate*1.5 #Calculate Overtime Rate
    print("Pay:",40*fltRate+fltOverHour*fltOverRate)
else:
    print("Pay:",fltHour*fltRate)

