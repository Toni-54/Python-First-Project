# Code is for the 11 Program of the Loop
sumo_even = 0
sumo_odd = 0
for i in range(1,51):
    if(i % 2 == 0):
        sumo_even += i
    else:
        sumo_odd += i
print("Total of even numbers between 1 and 50 is:", sumo_even)
print("Total of odd numbers between 1 and 50 is:", sumo_odd)
