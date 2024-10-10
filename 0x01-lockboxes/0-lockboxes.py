#!/usr/bin/python3
"""
This module defines the canUnlockAll function to determine if all boxes 
in a list of locked boxes can be opened using keys found in the boxes.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list): A list of lists where each sublist contains keys
                  to other boxes.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    unlocked = [0]
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            unlocked.append(key)
            keys.update(boxes[key])

    return len(unlocked) == len(boxes)
