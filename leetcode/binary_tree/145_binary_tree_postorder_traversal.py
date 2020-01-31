"""
Given a binary tree, return the postorder traversal of its nodes' values.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def postorder_traversal_rec(root):
    """
    Space complexity: O(h)
    Time complexity: O(n)
    """
    def post_helper(root, res):
        if not root:
            return
        post_helper(root.left, res)
        post_helper(root.right, res)
        res.append(root.val)
    res = []
    post_helper(root, res)
    return res

def postorder_traversal_iter(root):
    """
    Stack used to process current nodes in reverse order, so rightmost branches
    are at the beginning of result list. When done, return list in reverse to
    get the correct order.
    """
    res, s = [], [root]
    while s:
        curr = s.pop()
        if curr:
            res.append(curr.val)
            s += [curr.left, curr.right]
    return res[::-1]
