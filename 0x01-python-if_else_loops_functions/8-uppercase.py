#!/usr/bin/python3
def uppercase(s):
    for char in s:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert the lowercase letter to uppercase using ASCII values
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            print(uppercase_char, end="")
        else:
            # Print non-alphabetic characters as they are
            print(char, end="")
    
    # Print a new line after the entire string
    print()
