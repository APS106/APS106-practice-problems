# Write a function that takes an integer as input and 
# returns that integer flipped. 

def flipper(num):
    '''
    (int) -> int
    Returns the num flipped (e.g., 12 -> 21, 123 -> 321).
    '''
    # Repeatedly peel off the ones digit and add it to 10 times
    # the value accumulated in flipped_num
    flipped_num = 0
    while num > 0:
        flipped_num *= 10          # make space for the new ones_digit
        ones_digit = num % 10      # grab the ones digit
        flipped_num += ones_digit
        num //= 10                 # discard the old ones digit

    return flipped_num

print(flipper(1230567))
