#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    case = 'a' if char % 2 == 0 else 'A'
    print("{}".format(
        chr(char - ord('z') + ord('Z') if case == 'A' else char)
        ), end="")
