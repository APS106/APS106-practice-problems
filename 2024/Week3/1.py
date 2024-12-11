# Write a function that takes the role of a store clerk. 
#
# Ask a user to enter two floating point numbers: 
# the cost of an item and the amount of money remitted to pay for the item.
# Then respond appropriately: calculate the change due to the customer 
# or ask the customer for more money. 
#
# For example:
#
# Cost of the item: 3.56
# Amount tendered: 5.00
# Change: 1.44
# or
# Cost of the item: 3.56
# Amount tendered: 3.00
# Still due: 0.56
#
# Hint: You will need some Week 4 material to do this one.

cost = float(input("Cost of the item: "))
tendered = float(input("Amount tendered: "))

if cost > tendered:
    print("Still due:", cost - tendered)
else:
    print("Change:", tendered - cost)

# Bonus question: figure out how to print out the change/amount due to 
#                 only two decimal points