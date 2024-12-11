# Ask the user for a three digit integer and output the “flipped” version. 
#
# For example:
# Enter a positive number less than 1000: 177
# That number flipped is 771
#
# Hint: Represent the user’s input as a integer and use the arithmetic 
#       operators // and % to do it.
#
# Make sure it works if the user enters a one or two digit integers. 
# For example, 37 flipped is 730, and 8 flipped is 800. 


def flip_number_int(num):
    '''(int) -> int
    Return the 3-digit integer with its digits reversed including leading 0s if necessary
    '''

    ones_digit = num % 10
    tens_digit = (num // 10) % 10
    hundreds_digit = (num // 100)
        
    return 100 * ones_digit + 10 * tens_digit + hundreds_digit


num_represented_as_str = input("Enter a positive number less than 1000: ")
num_represented_as_int = int(num_represented_as_str)

print(flip_number_int(num_represented_as_int))

