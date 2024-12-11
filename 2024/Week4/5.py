# The Fibonacci sequence (https://en.wikipedia.org/wiki/Fibonacci_sequence) is:
#
#	0, 1, 1, 2, 3, 5, 8, 13, 21, 38, ...
#
# Starting with 0 and 1 as the first two entries, each subsequent entry is the 
# sum of the previous two entries.
#
# Write a function that takes an integer, i, as input and returns the ith 
# Fibonacci number. 


def fib(i):
    '''(int) -> int
    Returns the ith Fibonacci number
    '''
    if i == 1:
        fib = 0
    elif i == 2:
        fib = 1
    else:
        prev = 1
        fib = 1
        counter = 4
        while counter < i:
            new_fib = prev + fib
            
            # update for next time
            prev = fib
            fib = new_fib
            #print(counter, fib)
            
            counter += 1
    
    return fib

print(2, fib(2))
print(3, fib(3))
#print(fib(4))
#print(fib(5))
print(fib(20))
