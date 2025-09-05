# Code is for the List second program 

List = ["apple", "raspberry", "pineapple", "cherry"]
print(List)

# code is to find apple in the given list 
if "apple" in List:
  ind = List.index("apple")
  print(f"Apple is present at: {ind} index ")
else:
  print("Apple is not found")
 
# code is to replace a item at index 1 and 2
List[1:3] = ["Orange"]
print(List)
# code is for the insert method in python 
List.insert(2, "apricot")
print(List)

# code is for extend method in python 
List.extend(["car", "bike","aeroplane"])
print(List)