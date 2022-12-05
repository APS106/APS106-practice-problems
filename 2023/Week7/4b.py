# Write a program that gets the user to enter a string and an integer k 
# such that the length of the string is a multiple of k.
# Chop the string into segments of length k, then print the segments in the 
# reverse order (separated by a space) and also the characters in each 
# segment reversed.
#
# Example
# Please enter the string: University
# Please enter k: 2
# yt is re vi nU

s = input("Please enter the string: ")
k = int(input("Please enter k: "))

# check if k is a factor on n and exit with an error if not
n = len(s)
if n % k != 0:
    print(k, "does not divide evenly into the string length,", n,)
else:
    rev_s = s[::-1]
    for i in range(0,n,k):
        print(rev_s[i:i+k],end=" ")
    print()   
