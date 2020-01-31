"""
Given a binary tree, return the preorder traversal of its nodes' values.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorder_traversal_rec(root):
    """
    Time complexity: O(n)
    Space complexity: O(h) since size of call stack depends on tree's height
    """
    def pre_helper(root, res):
        if not root:
            return
        res.append(root.val)
        pre_helper(root.left, res)
        pre_helper(root.right, res)

    res = []
    pre_helper(root, res)
    return res

def preorder_traversal_iter(root):
    """
    Use stack to keep track of current node, and add children right then left
    so that the left nodes enter the results list first after popped.
    """
    res, s = [], [root]
    while s:
        curr = s.pop()
        if curr:
            res.append(curr.val)
            s += [curr.right, curr.left]
    return res