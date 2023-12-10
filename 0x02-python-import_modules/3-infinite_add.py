#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    # Extract command-line arguments (excluding script name)
    args = argv[1:]

    # Initialize the sum to 0
    total_sum = 0

    # Iterate through each argument, cast to int, and add to the sum
    for arg in args:
        total_sum += int(arg)

    # Print the result
    print(total_sum)
