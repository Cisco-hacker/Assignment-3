from math import *

try:
    num = int(input("Enter a number: "))
    if num < 0:
        print("Negative number not allowed")
    else:
        print("Square root:", sqrt(num))
        print("Logarithm:", log(num))
        print("Sine:", sin(num))

except ValueError:
    print("Number not valid")
