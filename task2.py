import math

try:
    num = float(input("Enter a number: "))

    if num < 0:
        print("Square root not defined for negative numbers")

    elif num == 0:
        print("Logarithm not defined for zero")

    else:
        print("Square root:", math.sqrt(num))
        print("Logarithm:", math.log(num))
        print("Sine:", math.sin(num))

except ValueError:
    print("Invalid input. Please enter a number.")
