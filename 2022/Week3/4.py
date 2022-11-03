# Write a little trigonometry function. 
# Ask a user for an angle, specified in degrees.
# Then print the sine, cosine, and tangent of that angle. 
# For example:
# Enter an angle: 60.
#    sin(60.00) is 0.866025
#    cos(60.00) is 0.500000
#    tan(60.00) is 1.732051


import math

angle = float(input("Enter an angle in degrees: "))
angle_in_radian = math.radians(angle)

print("sin(", angle, ") is ", math.sin(angle_in_radian), sep='')
print("cos(", angle, ") is ", math.cos(angle_in_radian), sep='')
print("tan(", angle, ") is ", math.tan(angle_in_radian), sep='')
