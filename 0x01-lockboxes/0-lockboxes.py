def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    boxes (list of lists): A list of lists where each inner list represents a box
                           and contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Start with the first box

    while stack:
        box_index = stack.pop()
        if visited[box_index]:
            continue
        visited[box_index] = True

        for key in boxes[box_index]:
            if 0 <= key < n and not visited[key]:
                stack.append(key)

    return all(visited)
