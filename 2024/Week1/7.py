# Write a program to calculate the chemical rate constant

# Calculate the rate constant

A = 80          # pre-exponential factor
e = 2.718281828 # Euler's number
Ea = 108000     # Activation energy
Tf = 95         # temperature in fahrenheit
R = 8.3144598   # universal gas constant
# k should be 3.9474300434096683e-17

kelvin = (Tf - 32) * 5/9 + 273.15
exponent = -Ea / (R * kelvin)

k = A * e**exponent
print(k)