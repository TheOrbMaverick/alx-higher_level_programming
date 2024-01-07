#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_chars = ['.', '?', ':']

    current_line = ""
    for char in text:
        current_line += char

        if char in punctuation_chars:
            print(current_line.strip())
            print()  # Print 2 new lines
            current_line = ""

    if current_line.strip():  # Print any remaining text if not empty
        print(current_line.strip())
