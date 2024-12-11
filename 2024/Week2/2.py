# Write a function that asks a user for a positive integer, 
# and then calculates the minimum number of quarters, dimes, nickels, 
# and pennies needed to make up that amount. For example:
# 
# Enter an amount: 67
# 2 quarter(s), 1 dime(s), 1 nickel(s), 2 penny(ies)

def make_change(num):
    '''(int) -> NoneType
    Print out the number of quarters, dimes, nickels, and pennies
    needed to make up num cents
    '''
    num_quarters = num // 25
    num -= num_quarters * 25
    
    num_dimes = num // 10
    num -= num_dimes * 10
    
    num_nickels = num // 5
    num -= num_nickels * 5
    
    print(num_quarters, "quarters,", num_dimes, "dimes,", 
          num_nickels, "nickels,", num, "penny(ies)")
    
    
amount = int(input("Enter a number of cents: "))
make_change(amount)