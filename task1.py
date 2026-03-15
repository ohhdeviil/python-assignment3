def factorial(n):
    """
    This function calculates factorial using recursion
    """

    # base case
    if n == 0 or n == 1:
        return 1

    # recursive case
    return n * factorial(n - 1)


try:
    num = int(input("Enter a number: "))

    if num < 0:
        print("Factorial not defined for negative numbers")

    else:
        print("Factorial of", num, "is:", factorial(num))

except ValueError:
    print("Invalid input. Please enter an integer.")
