#Christopher Kirk
#03/08/2025
#P2LAB1
#I am doing circle formulas 

import math

radius = float(input("What is the radius of the circle?"))

diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print(f"The diameter of the circle is : {diameter:.1f}")
print(f"The circumference of the circle is : {circumference:.2f}")
print(f"The area of the circle is : {area:.3f}")
