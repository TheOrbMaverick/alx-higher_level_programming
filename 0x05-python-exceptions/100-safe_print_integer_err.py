#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        integer_value = int(value)
        print("{:d}".format(integer_value))
        return True
    except ValueError:
        error_message = "Exception: value is not an integer"
        print(error_message, file=sys.stderr)
        return False
