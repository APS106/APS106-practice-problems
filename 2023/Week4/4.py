# Write a program that repeatedly asks a user for integers, until the user 
# enters a zero.  Calculate the number of positive and negative integers 
# that were entered.

num_pos = 0
num_neg = 0
n = int(input("Enter an integer (0 to exit): "))

while n != 0:
    if n < 0:
        num_neg += 1
    elif n > 0:
        num_pos += 1

    n = int(input("Enter an integer (0 to exit): "))

print("You entered", num_pos, "positive and", num_neg, "negative values.")
