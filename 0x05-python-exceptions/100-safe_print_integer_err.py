#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    except ValueError as ve:
        error_message = "Exception: {}".format("Unknown format code 'd' for object of type 'str'" if isinstance(value, str) else ve)
        print(error_message, file=sys.stderr)
        return False
