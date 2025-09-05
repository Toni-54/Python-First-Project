# This code is for the First Program of List

my_list = ["Faryad",16,"AI and Machine Learning", True]
for i in my_list:
    print(i)

# Code is for Separating Data  Structures 
my_str  = []
my_int = []
my_bool = []

for i in my_list:
    if isinstance(i, str):
        my_str.append(i)
    elif isinstance(i, int):
        my_int.append(i)
    elif isinstance(i, bool):
        my_bool.append(i)
    else:
        print("Items not found")    

print(my_str)
print(my_int)
print(my_bool)

