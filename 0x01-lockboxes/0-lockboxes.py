#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list): A list of lists where each list represents a box and
                      contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True  

    keys_stack = [0]

    while keys_stack:
        current_box = keys_stack.pop()

        for key in boxes[current_box]:
            if 0 <= key < n and not unlocked[key]:
                unlocked[key] = True
                keys_stack.append(key)

    return all(unlocked)
