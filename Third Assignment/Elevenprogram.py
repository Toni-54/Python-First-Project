# code is for the eleven program
def factorial(n):
    if n < 0:
        return "Factorial is not defined"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
number = int(input("Enter a number to compute its factorial: "))
result = factorial(number)
print("The fact of", number, "is", result)