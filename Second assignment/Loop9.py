# Code is for the 9th Program of the Loop
password = "123amer"
while True:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted.")
        break
    else:
        print("Access denied.")
        continue