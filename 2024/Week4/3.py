#1. Write a function that takes in an odd number and returns the sum 
# of odd numbers from 1 to N:
#
#	1 + 3 + 5 + 7 + 9 + ... + N
#
# Write “main” code (i.e. outside of a function) that asks the user 
# for an odd, positive integer. If the user does not enter an odd, 
# positive integer, your code should keep asking until he/she does. 
# Then call your function and print out the results.  Make sure to check
# that the user enters an N that is odd and greater than zero.


def sum_of_odd(num): 
    ''' (int) -> int
    Returns the sum of odd numbers from 0 to num. Assumes num is odd.
    '''
    my_sum = 0
    i = 1
    while i <= num:
        my_sum += i
        i += 2
    return my_sum


def sum_of_odd_using_range(num): 
    # we haven't got to range() yet in APS106 but this is an alternative
    ''' (int) -> int
    Returns the sum of odd numbers from 0 to num. Assumes num is odd.
    '''
    return sum(range(1,num+1,2))


# Repeatedly ask user for an odd, positive integer
n = 0
while (n < 0) or (n % 2 == 0):    
    n = int(input("Please enter an odd, positive value: "))

s = sum_of_odd(n)
print("The sum of odd numbers from 1 to", n, "is", s)

s = sum_of_odd_using_range(n)
print("The sum of odd numbers from 1 to", n, "is", s)
