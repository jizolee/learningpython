def my_function(*kid):
    print("The youngest child is",kid[2])

def my_funtion1(**kid2):
    print("The youngest child is",kid2["lname"])

#my_funtion1(lname="hall",sname="Hal")

def default_function(country="Vietnam"):
    print("Hello", country)
#default_function("Italian")
#default_function()

def toy_function(toy):
    for y in toy:
        print(y)

x=["car","swing","paper"]
#toy_function(x)

def return_function(x):
    return 5*x

#print(return_function(10))
import math
#print(round(math.pi,2))



