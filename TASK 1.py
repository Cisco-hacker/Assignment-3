def factorial(num):
    if num < 0:
        return 0
    elif num < 2:
        return 1
    else:
        return num * (factorial(num-1))

number = int(input("Enter a number: "))
fact = factorial(number)

if fact == 0:
    print("Factorial cannot be negative")
else:
    print("Factorial of", number, "is:", fact)