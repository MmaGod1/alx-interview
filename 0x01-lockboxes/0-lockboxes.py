def canUnlockAll(boxes):
    unlocked = [0]
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            unlocked.append(key)
            keys.update(boxes[key])

    return len(unlocked) == len(boxes)
