# Make Q2 work in Canada where there are no longer any pennies.
# When making change round to the nearest nickel 
# (up if 3 or more, down if 2 or fewer)
#
# Changes from Q2 are marked below - in the line where the change is calculated
#
# Ask a user to enter two floating point numbers: 
# the cost of an item and the amount of money remitted to pay for the item.
# Then respond appropriately: calculate the change due to the customer 
# or ask the customer for more money. If you own them change, figure out
# how many $100, $50, $20, toonies, loonies, quarters, dimes, nickels, and
# pennies you need to give them

def make_change(num):
    '''(float) -> NoneType
    num is a dollar figure and may not be integer
    Print out the number of $100, $50, $20, toonies, loonies, quarters, dimes, 
    nickels, and pennies needed to make up num dollars
    '''

    # since we are using 2 decimal points with money, multiple dollar
    # by 100 and then just use ints. In other words, do everything in
    # cents
    num *= 100
    
    num_100 = int(num // 10000)
    num -= num_100 * 10000
    
    num_50 = int(num // 5000)
    num -= num_50 * 5000
    
    num_20 = int(num // 2000)
    num -= num_20 * 2000
    
    num_10 = int(num // 1000)
    num -= num_10 * 1000

    num_5 = int(num // 500)
    num -= num_5 * 500
    
    num_2 = int(num // 200)
    num -= num_2 * 200
    
    num_1 = int(num // 100)
    num -= num_1 * 100
    
    num_quarters = int(num // 25)
    num -= num_quarters * 25
    
    num_dimes = int(num // 10)
    num -= num_dimes * 10
    
    num_nickels = int(num // 5)
    num -= num_nickels * 5
    
    num = round(num)
    
    print(num_100, "$100 bill(s),", 
          num_50, "$50 bill(s),", 
          num_20, "$20 bill(s),", 
          num_10, "$10 bill(s),", 
          num_5, "$5 bill(s),",
          num_2, "toonies,",
          num_1, "loonies,",
          num_quarters, "quarters,",
          num_dimes, "dimes,", 
          num_nickels, "nickels,",
          num, "penny(ies)")

    # Bonus question: why am I using all those int() functions?

# ###############
# Change Q2
def round_to_nickel(change):
    '''(float) -> float
    change is a dollar figure rounded to two decimal places. Returns change
    rounded to nearest nickel.
    '''
    change = int(change * 100) # convert to cents (and an int)
    pennies = change % 10      # get ones digit (i.e., the # of pennies)
    change -= pennies          # subtract current pennies
    
    new_pennies = 0
    if pennies >= 8:
        new_pennies = 10 # need to round up to 10 cents
    elif pennies >= 3:
        new_pennies = 5  # need to round (up or down) to 5 cents
        
    return (change + new_pennies) / 100 # remember to convert back to dollars
# ###############
    
cost = float(input("Cost of the item: "))
tendered = float(input("Amount tendered: "))

if cost > tendered:
    print("Still due:", round(cost - tendered,2))
else:
    change = round(tendered - cost,2)
    print("Rounded change:", change)
    
    # ###############
    # Change from Q2
    change = round_to_nickel(change)
    print("Rounded change:", change)
    # ###############
    
    make_change(change)

# Bonus question: figure out how to print out the change/amount due to 
#                 only two decimal points