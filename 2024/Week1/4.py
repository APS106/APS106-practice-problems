# Write a program that for a temperature in degrees Celsius, 
# prints the equivalent temperature in degrees Fahrenheit
# (multiply C by 1.8, then add 32). For example:
# Celsius temperature: 30
# Fahrenheit equivalent is: 86
#
# As with Q#3, first put the Celsius temperature in your program directly and get it
# working. Then add the functionality to prompt the user for the Celsius temperature.

# hard-coded 
celsius = 30
fahrenheit = celsius * 1.8 + 32
print("Celsius temperature is:", celsius)
print("Fahrenheit equivalent is:", fahrenheit)

# ask the user
print("\n")
celsius = float(input("Enter a Celsius temperature: "))
fahrenheit = celsius * 1.8 + 32
print("Celsius temperature is:", celsius)
print("Fahrenheit equivalent is:", fahrenheit)
