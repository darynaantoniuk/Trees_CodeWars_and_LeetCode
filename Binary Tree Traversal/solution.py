"""Binary Tree Traversal"""


class Node:
    """class Node"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Pre-order traversal
def pre_order(node):
    """pre-order"""
    if node is None:
        return []

    result = [node.data]
    result += pre_order(node.left)
    result += pre_order(node.right)

    return result

# In-order traversal
def in_order(node):
    """in_order"""
    if node is None:
        return []

    result = in_order(node.left)
    result += [node.data]
    result += in_order(node.right)

    return result

# Post-order traversal
def post_order(node):
    """post_order"""
    if node is None:
        return []

    result = post_order(node.left)
    result += post_order(node.right)
    result += [node.data]

    return result
