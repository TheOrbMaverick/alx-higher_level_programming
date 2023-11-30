#!/usr/bin/python3
from sys import argv

# Skip the script name (argv[0]) and convert the rest to integers
arguments = [int(arg) for arg in argv[1:]]

# Calculate the sum of all arguments
result = sum(arguments)

# Print the result
print(result)
