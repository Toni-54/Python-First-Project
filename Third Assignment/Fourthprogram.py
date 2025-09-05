# code is for the Fourth Program of functions 

def Largest_Number(a,b,c):
    if a > b and a > c:
        print(f"The largest number is: {a}")
        return a
    elif b > c:
        print(f"The largest number is: {b}")
        return b
    else:
        print(f"The largest number is: {c}")
        return c
    
Largest_Number(98, 56, 78)    
