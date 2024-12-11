# Write a program that repeatedly asks a user for integers, until the user 
# enters a zero.  Calculate the number of positive and negative integers 
# that were entered and, separately, the sum of the positive integers
# and the sum of the negative integers

num_pos = 0
sum_pos = 0
num_neg = 0
sum_neg = 0
n = int(input("Enter an integer (0 to exit): "))

while n != 0:
    if n < 0:
        num_neg += 1
        sum_neg += n
    elif n > 0:
        num_pos += 1
        sum_pos += n

    n = int(input("Enter an integer (0 to exit): "))

print("\nYou entered", num_pos, "positive and", num_neg, "negative values.")
print("The sum of positive integers is:", sum_pos)
print("The sum of negative integers is:", sum_neg)
