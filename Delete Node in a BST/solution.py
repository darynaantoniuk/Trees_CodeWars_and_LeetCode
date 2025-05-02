"""Delete Node in a BST"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """class Solution"""
    def delete_node(self, root, key):
        """delete_node"""
        if not root:
            return None

        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            min_larger_node = self.get_min(root.right)
            root.val = min_larger_node.val
            root.right = self.delete_node(root.right, min_larger_node.val)

        return root

    def get_min(self, node):
        """get_min"""
        while node.left:
            node = node.left
        return node
