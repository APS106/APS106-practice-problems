# Write a program that takes an integer input less than 100000 and 
# prints if the number is a 5-digit, 4-digit number, 3-digit number, 2-digit number, 
# or a 1-digit number

import math


def count_digits_log(number):
    '''
    (int) -> int
    Returns the number of digits in number. -1 is returned is the 
    number is greater than 99999
    '''
    return int(math.log(number, 10)) + 1 # Do you understand why this works?

def count_digits_string(number):
    '''
    (int) -> int
    Returns the number of digits in number. -1 is returned is the 
    number is greater than 99999
    '''
    return len(str(number)) # Do you understand why this works?

number = int(input("Please input a number less than 100000: "))

# Doing it with a log
num_digits = count_digits_log(number)
print("You number has", num_digits, "digits.")

# Doing it with a string
num_digits = count_digits_string(number)
print("You number has", num_digits, "digits.")
