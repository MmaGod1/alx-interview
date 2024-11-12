#!/usr/bin/python3
"""Valid UTF-8 encoding."""


def validUTF8(data):
    """
    data: integers to verify
    Return: True or False if data is UTF-8 encoding or not.
    """
    # Number of bytes remaining to complete the current character
    remain_bytes = 0
    
    for byte in data:
        # Only consider the last 8 bits of each integer (0–255)
        byte = byte & 0xFF
        
        if remaining_bytes == 0:
            # Determine the number of bytes for the new character
            if (byte >> 5) == 0b110:
                remaining_bytes = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3  # 4-byte character
            elif (byte >> 7) == 0b1:
                # Invalid single-byte character if it starts with `10xxxxxx`
                return False
        else:
            # Check that the byte is in the form `10xxxxxx`
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    # Ensure no remaining bytes are expected
    return remaining_bytes == 0
