# Write a function that asks a user for a floating point number and 
# then prints two values: the number truncated to the first decimal place 
# and the number rounded to the first decimal place. For example:
# Enter a number: 4.158
# Truncated to one decimal place: 4.1
# Rounded to one decimal place: 4.2

import math

num = float(input("Enter a number: "))

# Truncate: there are a number of ways to do this

# use conversion to int to truncate
trunc_num = int(num * 10) / 10
print("Truncated to one decimal place: ", trunc_num)

# use math.trunc truncate
trunc_num = math.trunc(num * 10) / 10
print("Truncated to one decimal place: ", trunc_num)

# Round: most straighforward is to use round function
round_num = round(num,1)
print("Rounded to one decimal place: ", round_num)
