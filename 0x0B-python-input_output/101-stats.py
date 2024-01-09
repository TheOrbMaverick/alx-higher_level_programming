#!/usr/bin/python3
"""
Module documentation: log_metrics

This module defines a script that reads stdin line by line, computes metrics,
and prints statistics.

"""

import signal
import sys

def calculate_metrics(lines):
    """
    Function documentation: calculate_metrics

    This function calculates metrics based on the provided lines.

    Args:
        lines (list): A list of lines in the specified input format.

    Returns:
        tuple: A tuple containing total file size and a dictionary with
               status code counts.

    """
    total_size = 0
    status_counts = {}

    for line in lines:
        parts = line.split()
        if len(parts) >= 9:
            status_code = parts[-2]
            file_size = parts[-1]

            total_size += int(file_size)

            if status_code in status_counts:
                status_counts[status_code] += 1
            else:
                status_counts[status_code] = 1

    return total_size, status_counts

def print_metrics(total_size, status_counts):
    """
    Function documentation: print_metrics

    This function prints the computed metrics.

    Args:
        total_size (int): The total file size.
        status_counts (dict): A dictionary with status code counts.

    """
    print("Total file size:", total_size)

    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")

def handle_interrupt(signum, frame):
    """
    Function documentation: handle_interrupt

    This function handles keyboard interruption (CTRL + C).

    Args:
        signum (int): The signal number.
        frame: The current stack frame.

    """
    print("\nInterrupt received. Printing current metrics:")
    print_metrics(current_total_size, current_status_counts)
    sys.exit(0)

# Register the interrupt signal handler
signal.signal(signal.SIGINT, handle_interrupt)

# Initialize variables
lines_buffer = []
current_total_size = 0
current_status_counts = {}

try:
    for line in sys.stdin:
        lines_buffer.append(line.strip())

        if len(lines_buffer) == 10:
            current_total_size, current_status_counts = calculate_metrics(lines_buffer)
            print_metrics(current_total_size, current_status_counts)
            lines_buffer = []

except KeyboardInterrupt:
    pass

# Print final metrics after keyboard interruption
print("Final metrics:")
print_metrics(current_total_size, current_status_counts)
