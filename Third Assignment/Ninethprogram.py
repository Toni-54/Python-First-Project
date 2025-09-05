#code is for the Nineth Program 

def Score():
 score = int(input("Enter your score: "))
 if (score >= 90):
     print("You got Grade: A")
 elif (score >= 80):
     print("You got Grade: B")
 elif (score >= 70):
     print("You got Grade: C")
 elif (score >= 60):
     print("You got Grade: D")
 else:
     print("You Failed it")

Score()