# 4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

# import pi from the math module
from math import pi

# ask user for radius and convert to decimal (float)
radius = float(input('what is the radius of your cirle: '))

# calculate area of the circle
area = pi * radius**2

# round out to 2 decimal places
area = round(area, 4)

# output area
print(area)
