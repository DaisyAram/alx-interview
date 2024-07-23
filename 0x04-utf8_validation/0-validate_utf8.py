#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    method that determines if a given data set represents
    a valid UTF-8 encoding
    Args:
    data (list): A list of integers representing bytes of data.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else return False
    """

    i = 0
    while i < len(data):
        # Calculate the number of bytes required for the current character
        byte_count = 0
        if data[i] < 0x80:
            byte_count = 1
        elif data[i] < 0xC0:
            return False
        elif data[i] < 0xE0:
            byte_count = 2
        elif data[i] < 0xF0:
            byte_count = 3
        else:
            return False

        # Check if the required number of bytes are available
        if i + byte_count > len(data):
            return False

        # Check if the subsequent bytes are valid
        for j in range(1, byte_count):
            if data[i + j] < 0x80 or data[i + j] >= 0xC0:
                return False

        # Move to the next character
        i += byte_count

    return True
