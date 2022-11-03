import random

def dec2bin(n):
    ''' (int) -> str
    Return the string representing the binary value of the integer passed in.
    '''
    
    bStr = ''
    if n < 0:
        return 'Must be a positive integer'
    
    while n > 0:
        bStr += str(n % 2)
        n //= 2
    
    return bStr[::-1] # return the reversed string


# test the functions based on user input
num = int(input("Enter a positive integer: "))
if num > 0:
    std_bin = dec2bin(num)
    
    print(std_bin)
else:
    print("Not a positive integer. Skipping this step.")

