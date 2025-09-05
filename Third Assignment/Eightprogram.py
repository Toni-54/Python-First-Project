# code is for the Eighth Program
def Calculator(radius):
    area = 3.14159 * radius * radius
    circumference = 2 * 3.14159 * radius
    return area, circumference

radius = float(input("Enter the radius: "))
area, circumference = Calculator(radius)
print(f"Area: {area}")
print(f"Circumference: {circumference}")
