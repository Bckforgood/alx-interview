#!/usr/bin/python3
"""
UTF-8 validation module
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing UTF-8 encoded data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes in the current character
    num_bytes = 0

    # Iterate through each integer in the data
    for byte in data:
        # Check the 8th bit from the left
        mask = 1 << 7

        # If the 8th bit is 0, it's a single-byte character
        if not (byte & mask):
            if num_bytes != 0:
                return False  # Continuation byte without a start byte
        elif num_bytes == 0:
            # Count the number of leading 1s to determine the number of bytes
            while byte & mask:
                num_bytes += 1
                mask >>= 1

            # A character can be 1 to 4 bytes long
            if num_bytes == 0 or num_bytes > 4:
                return False

            # Decrement num_bytes to account for the initial byte
            num_bytes -= 1
        else:
            # Check if the current byte is a continuation byte
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False

            # Decrement the number of expected continuation bytes
            num_bytes -= 1

    return num_bytes == 0
