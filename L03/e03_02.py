# Checking input data
try:
    fltHour = float(input("Enter Hours: "))
    fltRate = float(input("Enter rate: "))
    x = 1
except:
    x = -1
if x > 0:  # Calculate if input data is a numeric
    if fltHour > 40:
        fltOverHour = fltHour - 40  # Calculate Overtime Hours
        fltOverRate = fltRate * 1.5  # Calculate Overtime Rate
        print("Pay:", 40 * fltRate + fltOverHour * fltOverRate)
    else:
        print("Pay:", fltHour * fltRate)
else:
    print("Error, please enter numeric input")
    quit()
