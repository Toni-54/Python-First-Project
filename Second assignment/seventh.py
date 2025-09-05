# this code is for the Seventh Program of the conditonal statements 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation = input("Enter operations (+, -, *, /): ")
if operation == '+':
 print("The sum is: ", num1 + num2)
elif operation == '-':
  print("The Minus is: ", num1 - num2)
elif operation == '*':
  print("The Multiplication is: ", num1 * num2)
elif operation == '/':
  print("The Division is: ", num1 / num2)
else:
  print("You entered an invalid operation:")
