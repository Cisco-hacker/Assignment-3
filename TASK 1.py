def factorial(num):
    if num < 2:
        return 1
    else:
        return num * (factorial(num-1))

try:
    number = int(input("Enter a number: "))

    if number < 0:
        print("Factorial cannot be negative")
    else:
        print("Factorial of", number, "is:", factorial(number))

except ValueError:
    print("Number not valid")
