iHour=float(input("Enter Hours:"))
iRate=float(input("Enter Rate:"))

def computepay(fltHours,fltRate):
    if fltHours>40:
        fltOvertime=fltHours-40
        fltOverrate=fltRate*1.5
        fltPay=40*fltRate+fltOvertime*fltOverrate
    else:
        fltPay=fltHours*fltRate
    print("Pay:",fltPay)

computepay(iHour,iRate)
    