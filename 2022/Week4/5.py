# Write a function that evaluates tanh-1(x) from the series
#
# tanh-1(x) = x + x3/3 + x5/5 + x7/7 + x9/9 + ...
#
# where x < 1.0 and x > -1.0.  The function should take x and, epsilon, 
# and return the estimate when the absolute value of the next term is the 
# series is less than epsilon. 


def estimate_tanh_inv(x, epsilon):
    '''(float, int) -> float
    Returns an estimate of tanh^-1 based on the series:
    tanh-1(x) = x + x3/3 + x5/5 + x7/7 + x9/9 + ...
    Stops when the estimate is with next item is the series is less than
    or equal to epsilon
    '''
    tanh_inv = 0
    term = x
    num = 3
    while abs(term) > epsilon:
        #print(term, num)
        tanh_inv += term
        term = x**num/num
        num += 2
        
    return tanh_inv

x = -2
while x < -1.0 or x > 1.0:
    x = float(input("Enter x between -1 and 1: "))
    eps = float(input("Enter epsilon: "))

tanh_inv = estimate_tanh_inv(x,eps)
print("tanh-1(", x, ") = ", tanh_inv, sep="")

