"""Sort binary tree by levels"""


def tree_by_levels(node):
    """tree_by_levels"""
    if node is None:
        return []

    queue = [node]
    path = []

    while queue:
        curr = queue.pop(0)
        path.append(curr.value)
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)

    return path
