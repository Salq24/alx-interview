#!/usr/bin/python3
"""To open all boxes"""

def canUnlockAll(boxes):
    """houses the function"""

    num = len(boxes)
    opened = set([0])
    stack = [0]

    while stack:
        box = stack.pop()
        for key in boxes[box]:
            if key < num and key not in opened:
                opened.add(key)
                stack.append(key)
    
    return len(opened) == num
