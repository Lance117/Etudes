"""
Given a binary tree, return the inorder traversal of its nodes' values.
Visit leftmost, process node's value, then repeat for right branch (if exists).
Otherwise move up the tree.
"""

def inorder_traversal_rec(root):
    def inorder_helper(root, res):
        if not root:
            return
        inorder_helper(root.left, res)
        res.append(root.val)
        inorder_helper(root.right, res)
    res = []
    inorder_helper(root, res)
    return res

def inorder_traversal_iter(root):
    """
    Keep traversing left until hit dead end, pushing nodes to stack along the
    way. Process top of stack, then move to the right branch.
    """
    res, s = [], []
    while root or s:
        if root:
            s.append(root)
            root = root.left
        else:
            res.append(s[-1].val)
            root = s.pop().right
    return res
