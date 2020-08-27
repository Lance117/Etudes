"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
def isValidBST(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def helper(curr, lower, upper):
        if not curr:
            return True
        if not lower < curr.val < upper:
            return False
        left = helper(curr.left, lower, curr.val)
        right = helper(curr.right, curr.val, upper)
        return left and right
    return helper(root, float('-inf'), float('inf'))
