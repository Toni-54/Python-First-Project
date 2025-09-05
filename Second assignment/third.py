# this code is for the third program 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 > num2 and num1 > num3:
    print("The first number is the greatest: ", num1)
elif num2 > num1 and num2 > num3:
    print("The second number is the greatest: ",num2)
else:
    print("The third number is the greatest: ",num3)
