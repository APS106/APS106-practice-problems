# Write a function that takes an integer input and returns an integer 
# equal to the number of digits it has.

def count_digits(num):
    '''
    (int) -> int
    Returns the number of digits in num.
    '''
    num = abs(num) # deal with negative integers
    
    count = 1
    while num // 10 > 0:
        count += 1
        num //= 10
    return count

print(count_digits(123456))
