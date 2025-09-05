# This code is for the 7th Program of the Loop
fact = int(input("Enter a number to find its factorial: "))
result = 1
for i in range(1, fact + 1):
    result *= i
print("The factorial of", fact, "is", result)