# Write a program that calculates the final cost of a set of items. 
# For example, if each item costs 1.43 and we need 9 of them. Then, print 
# the final cost.
# Cost? 1.43
# How many? 9
# Total cost is $12.87.
# First do it by “hard-coding” the numbers. Once you have that working, 
# add the ability to ask the user to input the numbers.

# hard-coding
cost = 1.43
how_many = 9
print("Cost? ", cost)
print("How many? ", how_many)
print("The total cost is $", cost * how_many, sep='')

# asking the user
print("\n")
cost = float(input("Cost? "))
how_many = int(input("How many? "))
print("The total cost is $", cost * how_many, sep='')
