#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1
plural_s = 's' if argc != 1 else ''
end_char = ':' if argc != 0 else '.'

print("Number of argument{}{}{}".format(plural_s, 's' if argc else '', end_char))

for i, arg in enumerate(argv[1:], start=1):
    print("{}: {}".format(i, arg))
