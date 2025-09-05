# This code is for the Fifth Program 

def Age():

 age = int(input("Enter your age: "))
 if(age < 18):
  print("You are a Minor")
 elif(age >= 18 and age < 60):
  print("You are an Adult")
 else:
  print("You are a Senior")

Age()


