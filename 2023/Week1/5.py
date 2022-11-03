# Write a program to evaluate y = 4x + 3 for any float number 
# the user may pick. Ask the user to input any x, then evaluate y, 
# and present the result to two decimal places. For example:
# Input x: 3.69
# The value of y = 4x + 3 is 17.76

x = float(input("Input x: "))
y = 4 * x + 3

print("Picked x:", '%.2f' % x)
print("The value of y = 4x + 3 is", '%.2f' % y)
