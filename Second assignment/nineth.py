# the given code is for the ninth Program of the conditional statements
my_num = int(input("Enter a number: "))
if my_num % 2 == 0 and my_num % 3 == 0:
  print(my_num, ": The number is divisible by both 2 and 3.")
elif my_num % 2 == 0:
  print(my_num, ": The number is divisible by 2.")
elif my_num % 3 == 0:
  print(my_num, ": The number is divisible by 3.")
else:
  print(my_num, ": The number is not divisible by 2 or 3.")
