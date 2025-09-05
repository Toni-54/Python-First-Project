# Code is for the Last Program of the Lists 
Gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]

my_str = [i for i in Gadgets if isinstance(i, str)]
my_num = [i for i in Gadgets if isinstance(i, (int, float))]
print(f"This is String list: {my_str}")
print(f"This is Number list: {my_num}")

A_strings = sorted(my_str)
D_strings = sorted(my_str, reverse=True)
print(f"Ascending: {A_strings}")
print(f"Descending: {D_strings}")

length_sorted_strings = sorted(my_str, key=len)
print(f"Strings sorted by length: {length_sorted_strings}")

A_numbers = sorted(my_num)
D_numbers = sorted(my_num, reverse=True)
print(f"Again Ascending: {A_numbers}")
print(f"And Descending : {D_numbers}")